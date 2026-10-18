# Generative models — cosmo-machine-learning dossier

Scope: how a generative model of a cosmological field, catalogue or image is set up,
trained, selected and validated (role of the model, preprocessing, objective, network,
checkpoint selection, sampler, validation ensemble), how it is used as a prior, a likelihood
or an amortised posterior, and how to choose between GANs, VAEs, diffusion and flow-matching
models, between pixel, patch and point-cloud representations, and between a learned prior
with an explicit likelihood and an amortised joint posterior. Snapshot: 2026-10-18. From:
Huertas-Company & Lanusse 2022 review (arXiv:2210.01813), Sects. 3.4, 4.2.3 and 6.1.2.

Already in L2, not repeated here: the table of families with their first cosmological use
(`physics-and-methods.md#generative-models-of-fields-and-catalogues`); the headline fidelity
numbers of the GAN, flow-matching, Cosmo-FOLD and initial-condition models
(`results.md#generative-model-fidelity`); the variance-field failure of generative
posteriors of initial conditions (same two sections). Field-level inference with a physical
forward model and sampled initial conditions belongs to `cosmo-beyond-two-point`
(`deep/field-level-inference.md`); networks that correct a gravity solver deterministically
are in `references/physics-and-methods.md#learned-corrections-of-fast-simulations`.

Symbols. x: a field, image or point set; θ: the cosmological (and astrophysical) parameters
the model is conditioned on; d or γ_obs: observed data. Diffusion (DDPM) convention: x_0 is
the clean sample, x_T pure Gaussian noise after T steps, β_t the variance schedule, ᾱ_t =
Π_{t'≤t}(1 − β_t'), ε ~ N(0, I) the injected noise and ε_φ the network that predicts it.
Flow-matching convention (reversed): x_0 is the source (noise) sample at t = 0, x_1 the data
sample at t = 1, v_θ the learned velocity field. The papers keep their own convention; so
does this file.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Fix the role of the model
<!-- key: step-1-fix-the-role-of-the-model -->

The same network family serves four roles, which set the training data and the validation:

| Role | What is learned | Data enter through | Example | Place read |
|---|---|---|---|---|
| Emulator of fields | p(x ∣ θ) | nothing: samples replace simulations | flow matching on κ maps at 57 cosmologies | arXiv:2605.23114, Sect. 3.2 |
| Prior for an inverse problem | p(x) at a fixed cosmology | an explicit likelihood p(d ∣ x) added to the learned score | DES Y3 mass maps | arXiv:2511.14667, Sect. 2.1–2.2 |
| Likelihood for θ | log p(x ∣ θ) through the diffusion variational bound | the field itself | CAMELS dark-matter maps, HMC over (Ω_m, σ8) | arXiv:2405.05255, Sect. IV.2 |
| Amortised posterior | p(x, θ ∣ d) or p(x ∣ d) | the data as a conditioning input | joint κ and wCDM posterior; initial conditions | arXiv:2606.31988, Sect. 3.4; arXiv:2606.10023, Sect. 2.3 |

An emulator is judged on the distribution of summary statistics across realisations; a prior
or a posterior is judged on calibration (Steps 7–9).

### Step 2. Build and transform the training set
<!-- key: step-2-build-and-transform-the-training-set -->

Training sets read in the bodies:

| Model | Training data | Place read |
|---|---|---|
| DDPM, CAMELS dark matter | CMD log₁₀ cold-dark-matter density of IllustrisTNG at z = 0, 25 h⁻¹Mpc on a side; 60% of the 1000 parameter vectors at 64², 70% at 128²; 15 fields per vector | arXiv:2211.12444, Sect. 3 (Dataset) |
| Diffusion-HMC | same suite; 700 parameter vectors (10 500 fields), conditioned on Ω_m, σ8 only | arXiv:2405.05255, Sect. II (Datasets) |
| RLCFM κ maps | 57 flat-ΛCDM models in (Ω_m, σ8), 12 000 maps of 128 × 128 pixels (5° × 5°) each; 46 cosmologies (552 000 maps) for training, 11 (132 000) held out | arXiv:2605.23114, Sect. 3.2 |
| DES Y3 diffusion prior | 50 full-sky pkdgrav3 ray-traced maps at one cosmology, four tomographic bins, 2146 flat 256 × 256 maps at 1 arcmin per full-sky map (> 100 000) | arXiv:2511.14667, Sect. 2.2 |
| Point-cloud diffusion | Quijote Latin hypercube, 2000 runs of 512³ particles in 1 h⁻¹Gpc, split 90/10; heaviest 5000 FoF haloes per box; 50 fiducial runs for validation | arXiv:2311.17141, Sect. II.1 |
| JADE (joint κ, θ) | 10⁵ draws of (θ, κ, γ_obs) from a log-normal LSST-Y10-like simulator, six wCDM parameters, 5 tomographic bins, 128² pixels over 5 × 5 deg² | arXiv:2606.31988, Sect. 4 |
| Flow-VAE galaxies | 81 500 COSMOS F814W < 25.2 stamps (80 000 training, 1500 test), 128 × 128 at 0.03″/pix, each with its PSF and noise power spectrum | arXiv:2008.03833, Sect. 4.1 |
| GAN slices | 10 L-PICOLA boxes per size; 1500 slices per box (15 000), 256 × 256 pixels, smoothed by a one-pixel Gaussian against shot noise | arXiv:1801.09070, Sect. 3 |

The halo selection is by number density rather than by a mass threshold "since in
observations we only have access to the former" [src: arXiv:2311.17141, Sect. II.1].

**Transforms.** Every model compresses the dynamic range before training:

- log₁₀ of the density, then a min–max map to [−1, 1] over the whole training set (DDPM)
  [src: arXiv:2211.12444, Sect. 3]; Diffusion-HMC pegs the min–max to the log range [9.42,
  15.44] of the full data set [src: arXiv:2405.05255, Sect. II];
- inverse log-normal transform κ = e^y − κ_min (arXiv:2502.04158, Eq. 16), then a min–max to
  [0, 1] per tomographic bin (Eq. 17) [src: Sect. III.1.1]; the flow-matching model applies
  the logarithm to the stored shifted field and standardises by the global mean and standard
  deviation of all training pixels (arXiv:2605.23114, Eq. 27) [src: Sect. 3.2];
- the GAN uses s(x) = 2x/(x + a) − 1 with a = 4 (arXiv:1801.09070, Eq. 2), chosen to enhance
  the contrast of filaments and haloes against voids [src: Sect. 3].

**Augmentation.** Rotations and flips give 54 000 = 9000 × 6 fields at 64²; with
translations, allowed by the periodic boundary, 252 000 = 10 500 × 24 at 128² [src:
arXiv:2211.12444, Sect. 3]. Point clouds are randomly translated and rotated respecting
periodicity [src: arXiv:2311.17141, Sect. III]. The point-cloud authors note that
augmentation is "significantly less data-efficient" than building the symmetry into the
network [src: Sect. IV].

### Step 3. Choose the objective
<!-- key: step-3-choose-the-objective -->

- **DDPM.** Forward process q(x_t ∣ x_{t−1}) = N(√(1 − β_t) x_{t−1}, β_t I) and the
  simplified loss L_simple = E_{t,x_0,ε} ‖ε − ε_φ(√ᾱ_t x_0 + √(1 − ᾱ_t) ε, t)‖² with t
  uniform in 1…T (Ho et al. 2020, arXiv:2006.11239, Eq. 14). It drops the weights of the
  variational bound and so down-weights small-t terms, which "leads to better sample
  quality" [src: Sect. 3.4]. The CAMELS DDPM uses a linear schedule in [10⁻⁴, 2 × 10⁻²] with
  T = 2000 and a Huber loss [src: arXiv:2211.12444, Sect. 3]; a cosine schedule was tried
  and found worse for the iterations explored [src: App. A.1]. Diffusion-HMC uses T = 1000
  with a non-linear schedule (smaller steps at small t) and notes that its Huber loss stays
  below 1, so it is in effect an MSE [src: arXiv:2405.05255, Sect. II].
- **Variational diffusion (ELBO).** The point-cloud model trains on the evidence lower bound
  log p(x) ≥ ELBO(x), sum of a prior-matching, a reconstruction and a diffusion term
  (arXiv:2311.17141, Eqs. 4–5); the same expression later gives the likelihood (Step 9)
  [src: Sect. II.3].
- **Flow matching.** Conditional flow matching regresses v_θ(t, x) on the conditional target
  u_t(x ∣ x_1) (arXiv:2605.23114, Eq. 5), with the same gradients as the intractable
  marginal objective (Eq. 4) [src: Sect. 2.2]. The residual label-conditional variant
  (RLCFM) uses a label-specific Gaussian source with mean μ_0(y) = E[x_1 ∣ y] and width
  σ_0(y) = α √(tr Cov[x_1 ∣ y]/d), σ_1 = β σ_0 (Eqs. 18–20), linear paths (Eqs. 16–17), and
  learns in the residual space r_t = x_t − μ_0(y) (Eqs. 21–24) [src: Sect. 2.3]; α = 1.2 and
  β = 0.04, α > 1 "increases the coverage of the initial distribution, which improves
  learning of large-scale structure" [src: App. A]. μ_0 and σ_0 are themselves regressed
  from the 46 training cosmologies (Gaussian process or polynomial ridge plus a boosted-tree
  correction clipped at 2%, Eqs. 32–33) [src: App. A].
- **Joint flow matching.** JADE predicts the clean sample and rebuilds the velocity, L =
  E‖(d_φ(x_t, t, γ_obs) − x_t)/max(1 − t, 0.05) − (x_1 − x_0)‖² (arXiv:2606.31988, Eq. 14),
  with t drawn logit-normal (μ = −0.8, σ = 0.8) to favour mid-to-high noise [src: App. A.5].
  Field and parameter tokens enter one unweighted MSE; a relative weight "would no longer
  target the true joint velocity field" and would bias the joint posterior [src: App. A.5].
- **VAE with a latent flow.** The galaxy model maximises an ELBO with free bits, L_λ = E[log
  p(x ∣ z)] − max(λ, D_KL[q(z ∣ x) ‖ p(z)]) (arXiv:2008.03833, Eq. 10), to avoid
  over-regularised, blurry solutions, then fits a conditional masked autoregressive flow to
  the aggregate latent posterior (Eqs. 11–15), because sampling a weakly regularised VAE
  from its Gaussian prior gives distorted images [src: Sects. 3.2–3.3]. The likelihood is
  Gaussian after convolving the generated profile with each stamp's PSF (Eq. 4), so the
  model learns deconvolved galaxies from noisy, PSF-convolved data [src: Sects. 2.2, 4.2.1].
- **GAN.** DCGAN-type generator and discriminator (five convolutional layers each, 3.2 × 10⁷
  trainable parameters in total), standard or Wasserstein-1 loss [src: arXiv:1801.09070,
  Sect. 4].

### Step 4. Build the network
<!-- key: step-4-build-the-network -->

- **U-Net for maps.** Four down- and up-sampling stages of two ResNet blocks with group
  normalisation and attention, as in Ho et al. [src: arXiv:2211.12444, Sect. 3].
  Diffusion-HMC adds circular convolutions for periodic fields, normalises each parameter to
  [0, 1] over its range (Ω_m ∈ [0.1, 0.5], σ8 ∈ [0.6, 1.0]), and injects θ through an MLP
  into the time embedding and every ResNet block; 31.2 million parameters [src:
  arXiv:2405.05255, Sect. II]. The RLCFM U-Net has widths 32 → 64 → 128 → 128, attention
  only at 16 × 16, and a label embedding of Fourier features plus "physics-inspired
  features, including an S_8 term with learnable gating" [src: arXiv:2605.23114, App. A,
  Table 1].
- **Point clouds.** The score network must be permutation-equivariant, accept any
  cardinality and model joint attributes; a graph network on a k = 20 nearest-neighbour
  graph rebuilt at every diffusion step with periodic distances (637 373 parameters), or a
  transformer without positional encoding (4 776 281 parameters) where a pre-layer-norm was
  "crucial for training stability" [src: arXiv:2311.17141, Sect. II.4].
- **Transformers for joint posteriors.** JADE treats θ as extra tokens next to field
  patches; the observed shear enters as further tokens, with a coarser patch size because
  shape noise removes small-scale information [src: arXiv:2606.31988, Sect. 3.4].
- **Galaxy VAE.** Seven ResNet stages per side, depth 16 to 512, a 16-dimensional latent,
  softplus output for positive light profiles, a total-variation penalty of weight 0.01
  against unconstrained high frequencies, and the PSF image fed to the encoder [src:
  arXiv:2008.03833, Sect. 4.2.1, Table 1].

### Step 5. Train and select the checkpoint
<!-- key: step-5-train-and-select-the-checkpoint -->

The loss does not tell when the samples are right. Practice read in the bodies:

| Model | Training | Selection rule | Place read |
|---|---|---|---|
| CAMELS DDPM | 60 000 iterations, batch 40, Adam at 5 × 10⁻⁴ (64²) or 2 × 10⁻⁴ (128²); 1.25 h and 13.5 h on one A100 | 100 samples from each of the last 10 checkpoints; keep the one with the lowest P(k) error and best Minkowski agreement | arXiv:2211.12444, Sect. 3, App. A.1 |
| Diffusion-HMC | 64² for 60 000 iterations, then the 64² weights initialise the 256² model, trained for over 400 000 iterations (faster convergence) | reduced χ² of P(k) of 50 samples at each of 10 validation parameters, eight checkpoints from 200k to 340k; 260k gives 2.29 ± 0.49 against a leave-one-out floor of 1.70 ± 0.36 among the 15 true fields | arXiv:2405.05255, Sect. II, App. B |
| Point-cloud diffusion | 300 000 AdamW iterations, peak 3 × 10⁻⁴, 5000 warm-up steps, cosine decay, batch 16; about 12 h on 4 A100 | smallest KL divergence between generated and validation 2PCFs at r < 55 h⁻¹Mpc (both taken Gaussian) | arXiv:2311.17141, Sect. III, App. B |
| RLCFM | AdamW, 2 × 10⁻⁴ cosine-decayed to 3 × 10⁻⁵, batch 128 mixing cosmologies, EMA weights used for sampling; stable metrics after ~15 epochs | validation summary statistics at held-out cosmologies | arXiv:2605.23114, App. A, B.1 |
| JADE | batch 128, 750 epochs, ~48 h on one GH200 | — | arXiv:2606.31988, Sect. 4 |
| GAN | early stopping at the best P(k) agreement: epochs 17 (500 Mpc) and 21 (100 Mpc), 16.1 h and 7 h on a GTX 1080 | power spectrum | arXiv:1801.09070, Sect. 4 |
| Cosmo-FOLD | 100 000 steps, AdamW, batch 8, cosine warm restarts between 3 × 10⁻⁴ and 10⁻⁶ every 20 epochs | lowest-loss checkpoint | arXiv:2601.14377, Sect. 2.2.3 |

The reason given for selecting on statistics: "convergence in terms of the loss does not
imply that the converged models are stationary with respect to the distribution of the
summary statistics"; across the last ten checkpoints the mean absolute fractional P(k)
difference was about 10% (64²) and 15% (128²), and at least one checkpoint below 5% could be
found [src: arXiv:2211.12444, Sect. 3, Summary Statistics]. In the point-cloud model "a
small decrease in the loss value produces a sharp decrease in the KL-divergence" [src:
arXiv:2311.17141, App. B].

### Step 6. Sample
<!-- key: step-6-sample -->

| Model | Sampler and cost | Place read |
|---|---|---|
| CAMELS DDPM | 10 images in ~40 s (64²) or ~110 s (128²) on an A100 | arXiv:2211.12444, App. A.1 |
| Diffusion-HMC | 50 fields of 256² in 310 s (6.2 s per field) | arXiv:2405.05255, Sect. II |
| Point cloud | 1000 timesteps, ~5 s per cloud on an A100 | arXiv:2311.17141, Sect. III |
| RLCFM | dopri5 ODE solver; 5000 maps in ~4 min on an A100 | arXiv:2605.23114, App. A |
| JADE | Heun second-order, 256 steps; ~0.2 s per joint sample | arXiv:2606.31988, App. A.8, Sect. 4 |
| Cosmo-FOLD | 100–400 denoising steps; a 1024³ TNG300-2 volume in ~5–10 h on one A100; time scales linearly with T | arXiv:2601.14377, Sect. 2.2.3, Table 2 |

**Fields larger than the training box (Cosmo-FOLD).** A 256³ target is cut into 4³ chunks of
64³ (the training size), each chunk is denoised one step conditioned on its piece of the
conditioning field (arXiv:2601.14377, Eq. 5), the chunks are tiled back, and the whole field
and its conditioning field are shifted by one voxel along each axis with periodic wrapping
before the next step (Algorithm 1) [src: Sect. 2.3]. No fixed grid is privileged, so edge
artefacts are smoothed by later passes "provided that the noise increment per time step is
sufficiently small" [src: same]. Periodic positional encodings p(x) = Σ_i α_i[sin(2πx f_i) +
β cos(2πx f_i)] (Eq. 8), with n = 4, α_i = [0.33, 0.29, 0.25, 0.21, 0.19] and β = 1.5 chosen
heuristically, were added to recover the bispectrum [src: Sect. 2.3].

### Step 7. Validate an emulator against an ensemble
<!-- key: step-7-validate-an-emulator-against-an-ensemble -->

Statistics used: pixel and peak histograms, C_ℓ or P(k), bispectrum, Minkowski functionals
(arXiv:2605.23114, Eq. 28), the correlation matrix R_ℓℓ′ of the power spectrum and MS-SSIM
[src: arXiv:2605.23114, Sect. 4]; 2PCF, k-nearest-neighbour distributions, mean pairwise
velocity and halo mass function for point clouds [src: arXiv:2311.17141, Sect. III]; first-
and second-order scattering coefficients (arXiv:2502.04158, Eqs. 25–26) and covariance
eigenvalues of noisy-map statistics [src: arXiv:2502.04158, Sect. IV.1]; second moments,
size, ellipticity and Gini–M20 or MID morphology for galaxy images [src: arXiv:2008.03833,
Sect. 4.4].

What the validation needs:

- **A reference ensemble with independent initial conditions at the same θ.** The RLCFM test
  compares distributions, not means: a per-bin normalised Wasserstein-1 distance averaged
  over bins gives 0.039 and 0.058 (pixels), 0.033 and 0.046 (C_ℓ), 0.035 and 0.042
  (bispectrum) on training and held-out cosmologies [src: arXiv:2605.23114, Sect. 5.3]. The
  point-cloud authors could not quantify fidelity across θ because Quijote's Latin hypercube
  has one seed per cosmology, and compared 50 generated against 50 N-body boxes at the
  fiducial point only [src: arXiv:2311.17141, Sect. III].
- **A covariance test.** Diffusion-HMC generated 405 fields to match the 405 of the CAMELS
  CV set, built the P(k) covariance from 350 true fields with the Hartlap factor
  (arXiv:2405.05255, Eqs. 8–9) and found mean reduced χ² of 33.4 (true) and 36.6 (generated)
  for 35 bins; the generated standard deviation is slightly low for k < 5 h Mpc⁻¹ and
  correlations are slightly excessive near 5 h Mpc⁻¹ [src: Sect. III].
- **Parameter response at fixed seed.** One-parameter sets generated from 15 seeds reproduce
  the CAMELS 1P ratios of P(k) [src: arXiv:2405.05255, Sect. III, Fig. 2].
- **Held-out cosmologies.** RLCFM holds out 11 of 57 cosmologies and reports mean, worst
  case and spread across them [src: arXiv:2605.23114, App. B.2].

### Step 8. Use as a prior: diffusion posterior sampling
<!-- key: step-8-use-as-a-prior-diffusion-posterior -->

The posterior score is the likelihood score plus the learned prior score (arXiv:2511.14667,
Eq. 1). DPS evaluates the likelihood at the Tweedie posterior mean κ̂_{0∣t}; because errors
accumulated early in the reverse process push latent maps out of distribution, the
likelihood term is multiplied by A(t) = Sigmoid((t̄ − t)/σ_t) with t̄ = 500 and σ_t = 20
(Eq. 2), tuned until the TARP coverage test passes [src: Sect. 2.1]. The likelihood is
Gaussian in the shear with independent per-pixel shape noise (Eq. 3) and masked pixels left
out; validation used σ_ε = 0.26 and DES Y3 densities; one posterior map takes about 1 minute
on an A40 [src: Sects. 2.2, 3.1]. The method paper shows the latent maps going out of
distribution in their first-order scattering coefficients without the scaling [src:
arXiv:2502.04158, Sect. III.2.1, Fig. 4] and a generated-map P(k) bias at the few-per-cent
level (1024 samples) [src: Sect. IV.1, Fig. 1]. Changing the likelihood (non-Gaussian noise,
a new mask) needs no retraining, which the authors call the "plug-and-play" advantage [src:
arXiv:2511.14667, Sect. 4].

### Step 9. Use as a likelihood or an amortised posterior
<!-- key: step-9-use-as-a-likelihood-or-an-amortised -->

- **Diffusion likelihood.** log p(x ∣ θ) ≃ −Σ_{t<T_MAX} L_t, sampled with HMC under flat
  priors (arXiv:2405.05255, Eqs. 5–6). Terms at large t constrain θ less, so T_MAX = 20 is
  used; it shifts the mean Ω_m and σ8 by −0.26% and −1.27% relative to all 1000 terms; 500
  HMC samples take about 32 minutes per field [src: Sects. IV.1–IV.2].
- **ELBO likelihood for point clouds.** 32 evaluations of the ELBO with 50 steps give a
  converged relative log-likelihood in about 10 s; the absolute log-likelihood varies by
  O(100) between evaluations against O(1) for the relative one [src: arXiv:2311.17141, Sect.
  III, App. C].
- **Amortised joint posterior.** JADE samples (κ, θ) given γ_obs by integrating the
  conditional ODE; validated against NUTS on the same differentiable log-normal model and by
  MIRA and TARP on 500 observations with 500 samples each [src: arXiv:2606.31988, Sects. 4,
  5.2].
- **Posterior ratios.** Where the model has an exact density (GLOW), test log-posterior
  ratios between pairs of samples against the true ratio (arXiv:2606.10023, Eq. 13) [src:
  Sect. 5.4].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### GAN, VAE, diffusion or flow matching
<!-- key: gan-vae-diffusion-or-flow-matching -->

- **Mode collapse.** The cosmic-web GAN matched P(k) to 1–2% on 500 Mpc slices but reached
  20% errors on the more inhomogeneous 100 Mpc slices, attributed to mode collapse (the
  model over-produces, for example, empty regions), and missed large-scale P(k) correlations
  by ~20%; the authors conclude GANs suit "large, homogeneous datasets" [src:
  arXiv:1801.09070, Sect. 7]. A GAN fed no noise samples "tries to learn some noise patterns
  that are actually replicated from image to image" [src: arXiv:2008.03833, Sect. 2.2].
- **Same data, GAN against flow matching.** On the same split and metrics, RLCFM keeps
  pixel-distribution Wasserstein distances below 1% against a few per cent for the GAN, P(k)
  below 1% for most test points against a few to over 5%, correlation-matrix differences
  around 3% (up to ~9%) against 5–15% (up to ~40%), bispectrum below 5% against ~10% (edges
  above 20%); it reaches stable metrics after ~15 epochs against 40 [src: arXiv:2605.23114,
  App. B.1]. The largest GAN errors sit at the edges of the parameter grid [src: same].
- **Flows in latent space.** The galaxy model uses a normalising flow rather than a GAN for
  its latent sampler because flows have an exact likelihood, are "significantly more stable
  than GANs" and are not susceptible to mode collapse [src: arXiv:2008.03833, Sect. 3.3].

### Shared or label-specific source distribution
<!-- key: shared-or-label-specific-source-distribution -->

In the flow-matching ablation over 11 held-out cosmologies a label-specific prior alone
(LCFM) is worst on every metric; residual-space training alone (RCFM) improves the
non-Gaussian statistics; both together (RLCFM) give the lowest mean, worst case and spread
[src: arXiv:2605.23114, App. B.2]. The stated reason: with label-specific sources, a
velocity network shared across labels must represent vector fields that vary less smoothly
with y, which hurts interpolation between training labels [src: same].

### Pixels, patches, point clouds or latents
<!-- key: pixels-patches-point-clouds-or-latents -->

- **Point clouds** avoid voxelisation and select by number density, but the message-passing
  GNN does not reproduce the BAO feature of the 2PCF (~120 h⁻¹Mpc), which the authors
  attribute to oversmoothing and limited long-range expressivity, and the cumulative mass
  function is slightly offset [src: arXiv:2311.17141, Sects. III, IV].
- **Patches with overlap** (Cosmo-FOLD) reach 1024³ volumes, but trained on 25 h⁻¹Mpc CAMELS
  boxes and applied to TNG300-2 they reproduce P(k) within 10% only up to the training box
  scale (to k ≤ 6 h Mpc⁻¹) and lose power on larger scales, which "cannot learn or
  reconstruct large-scale modes that are absent from the training volumes" [src:
  arXiv:2601.14377, Sect. 3.2.3].
- **Pixel-space transformers** (JADE) grow in sequence length with resolution; the authors
  propose latent diffusion as the remedy, at the cost of an autoencoder stage [src:
  arXiv:2606.31988, Sect. 6].

### Learned prior with explicit likelihood, or amortised posterior
<!-- key: learned-prior-with-explicit-likelihood-or -->

| | Prior + DPS (DES Y3 mass maps) | Amortised joint posterior (JADE) |
|---|---|---|
| Trained on | 50 full-sky maps at one cosmology | 10⁵ (θ, κ, γ_obs) triplets across the prior |
| Survey changes (mask, noise model) | no retraining | retraining |
| Cosmology | fixed in the prior; not inferred | inferred jointly |
| Tuning | A(t) hyperparameters tuned on TARP | none reported |
| Cost per sample | ~1 min (A40) | ~0.2 s |
| Place read | arXiv:2511.14667, Sects. 2.1–2.2, 3.1, 4 | arXiv:2606.31988, Sects. 4, 6 |

JADE needed 10⁵ simulations against 4.36 × 10⁶ simulator calls for the ten NUTS chains on
one observation, "one order of magnitude more" [src: arXiv:2606.31988, Sect. 4].

### Where the training simulations are placed
<!-- key: where-the-training-simulations-are-placed -->

Training generative posteriors of initial conditions on samples concentrated in the
posterior (HMC samples) rather than random joint draws reaches comparable accuracy with
about ten times fewer simulations; with random draws, 262 144 samples still had not
converged and "at least another order of magnitude" may be needed [src: arXiv:2606.10023,
Sect. 6.2]. For comparison the same paper puts typical field-level SBI in cosmology at ≲
2000 simulations [src: Sect. 2.3].

### Generative likelihood or regression network
<!-- key: generative-likelihood-or-regression-network -->

Diffusion-HMC gives narrower (Ω_m, σ8) constraints than an NPE on the power spectrum plus
mean on the same fields, and under added white noise (σ = 0.01–0.02, a 4–6% change of the
smallest-scale P(k)) its estimates move far less than a regression network's, which shift by
~6–23% [src: arXiv:2405.05255, Sects. IV.2–IV.3]. Its mean biases over ten validation fields
are −0.006 on Ω_m (2%) and 0.01 on σ8 (1.26%), with mean |z| of 2.75 (Ω_m) and 1.14 (σ8):
error bars too small, attributed to the truncation of the bound [src: Sect. IV.2].

### Conditioning on fewer parameters than the simulations vary
<!-- key: conditioning-on-fewer-parameters-than-the -->

Diffusion-HMC conditions on Ω_m and σ8 while the four feedback parameters vary, arguing that
dark-matter maps carry little feedback information [src: arXiv:2405.05255, Sect. II]. The
point-cloud model conditions on Ω_m and σ8 while Ω_b, h, n_s vary, so these are "implicitly
marginalized" and exact agreement is not expected [src: arXiv:2311.17141, Sect. III].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| DDPM schedule | linear β ∈ [10⁻⁴, 2 × 10⁻²], T = 2000 | CAMELS DDPM | arXiv:2211.12444 | Sect. 3 |
| Checkpoint spread in P(k) | ~10% (64²), ~15% (128²) mean abs. fractional | CAMELS DDPM | arXiv:2211.12444 | Sect. 3 |
| P(k) χ²_r of selected checkpoint | 2.29 ± 0.49 vs 1.70 ± 0.36 leave-one-out | Diffusion-HMC | arXiv:2405.05255 | Sect. II |
| CV covariance test | χ² mean 33.4 (true), 36.6 (generated), 35 bins | Diffusion-HMC | arXiv:2405.05255 | Sect. III |
| Truncation of the bound | T_MAX = 20; −0.26% (Ω_m), −1.27% (σ8) | Diffusion-HMC | arXiv:2405.05255 | Sect. IV.2 |
| Calibration of the diffusion likelihood | mean abs. z 2.75 (Ω_m), 1.14 (σ8) | Diffusion-HMC | arXiv:2405.05255 | Sect. IV.2 |
| RLCFM source widths | α = 1.2, β = 0.04 | κ-map emulator | arXiv:2605.23114 | App. A |
| Wasserstein-1, train / test | pixels 0.039/0.058; C_ℓ 0.033/0.046; B_ℓ 0.035/0.042 | κ-map emulator | arXiv:2605.23114 | Sect. 5.3 |
| DPS likelihood scaling | t̄ = 500, σ_t = 20 | DES Y3 mass maps | arXiv:2511.14667 | Sect. 2.1 |
| DPS resolution gain | ρ_c ≈ 0.5 at ℓ ~ 1000 against ℓ ~ 200 previously | DES Y3 mocks | arXiv:2511.14667 | Sect. 3.1 |
| JADE calibration | MIRA 0.635 ± 0.017 joint, 0.659 ± 0.0139 marginal (2/3 ideal, 1/2 worst) | LSST-Y10 log-normal | arXiv:2606.31988 | Sect. 5.2 |
| JADE vs NUTS cost | 10⁵ training simulations vs 4.36 × 10⁶ simulator calls | same | arXiv:2606.31988 | Sect. 4 |
| Point-cloud ELBO likelihood | 32 evaluations × 50 steps, ~10 s; overconfident on Ω_m | Quijote haloes | arXiv:2311.17141 | Sect. III, App. C |
| Simulations for IC posteriors | 59 880 standard, 262 144 extended, not converged | 32³ field | arXiv:2606.10023 | Sects. 2.3, 6.2 |
| VAE galaxies | 4% mean ellipticity, 1% mean size; ~27% size scatter in conditioning | COSMOS | arXiv:2008.03833 | Sect. 4.4.1 |
| GAN | 1–2% P(k) at 0.06 < k < 0.4 (500 Mpc); 20% (100 Mpc) | L-PICOLA slices | arXiv:1801.09070 | Sect. 7 |
| Cosmo-FOLD transfer | P(k) within 10% to k ≤ 6 h Mpc⁻¹ below the 25 h⁻¹Mpc box scale | CAMELS → TNG300-2 | arXiv:2601.14377 | Sect. 3.2.3 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Loss converged, samples not.** The noise-prediction loss does not track sample quality;
  checkpoints differ by ~10–15% in P(k). Test: generate from several late checkpoints and
  select on statistics against a held-out reference [src: arXiv:2211.12444, Sect. 3;
  arXiv:2405.05255, Sect. II]. Selecting on the very statistic later used for validation
  makes that validation optimistic; hold one statistic out [der].
- **Too little diversity at fixed θ.** With continuous conditioning, a sample with too much
  or too little power can resemble another cosmology, so the model may trade diversity for
  parameter discrimination; seen as a slightly low standard deviation of P(k) [src:
  arXiv:2405.05255, Sect. III]. Test: the CV covariance χ² and standard-deviation ratio at
  one θ.
- **Large scales missing.** BAO absent in point clouds; large-scale P(k) correlations off by
  ~20% for the GAN; no power beyond the training box for patch methods [src:
  arXiv:2311.17141, Sect. IV; arXiv:1801.09070, Sect. 7; arXiv:2601.14377, Sect. 3.2.3].
  Test: 2PCF at the BAO scale and P(k) at the box scale against an ensemble.
- **Worst at the edges of the parameter grid.** The GAN degrades most at boundary
  cosmologies [src: arXiv:2605.23114, App. B.1]. Test: report the worst held-out cosmology,
  not only the mean.
- **DPS bias.** Plain DPS gives biased maps because early latents go out of distribution
  [src: arXiv:2502.04158, Sect. III.2.1]. Test: TARP on mocks; the fix needs hand-tuned
  hyperparameters, which the authors list as a limitation [src: arXiv:2511.14667, Sect. 4].
- **Overconfident learned likelihoods.** Point-cloud ELBO likelihoods are overconfident on
  Ω_m, attributed to 1800 training boxes being too few to learn the field-level parameter
  dependence [src: arXiv:2311.17141, Sect. III]; Diffusion-HMC error bars are too small
  after truncation [src: arXiv:2405.05255, Sect. IV.2]. Test: z-scores or coverage over many
  held-out fields.
- **Diagnostics that cannot see the uncertainty.** Cross-correlation with the truth is
  dominated by the mean field and "can remain high even when the posterior variance is
  incorrect"; TARP loses discriminating power in high dimension and gives only average-case
  guarantees [src: arXiv:2606.10023, Sects. 2.2, 5.2]. Test: transfer function of the
  posterior samples against a reference (Eq. 9), posterior-ratio checks (Eq. 13).
- **Relative probabilities wrong by orders of magnitude.** A GLOW posterior orders samples
  correctly but mis-scales log-probabilities, worse on HMC samples than on its own [src:
  arXiv:2606.10023, Sect. 5.4].
- **Real data outside the training distribution.** Both the DES Y3 mass-map and the JADE
  authors flag this as unquantified; the DES Y3 prior is also trained at one fixed cosmology
  [src: arXiv:2511.14667, Sects. 2.2, 4; arXiv:2606.31988, Sect. 6].
- **Retraining for every survey change.** An amortised posterior must be retrained when the
  mask, noise or systematics model change [src: arXiv:2606.31988, Sect. 6].

## Reading list
<!-- key: reading-list -->

- Foundation: Ho et al. 2020, arXiv:2006.11239 — DDPM objective, Eq. 14, and why the
  simplified loss improves samples.
- Method: Mudur et al. 2022, arXiv:2211.12444 — first DDPM on CAMELS fields;
  checkpoint-to-checkpoint variation and selection on statistics.
- Method: Mudur et al. 2024, arXiv:2405.05255 — diffusion model as a likelihood with HMC; CV
  covariance test; calibration of the result.
- Method: Li & Kacprzak 2026, arXiv:2605.23114 — residual label-conditional flow matching,
  held-out cosmologies, comparison with a GAN on the same split.
- Method: Cuesta-Lazaro & Mishra-Sharma 2023, arXiv:2311.17141 — point-cloud diffusion,
  equivariant networks, ELBO likelihood and its miscalibration.
- Method: Lanusse et al. 2021, arXiv:2008.03833 — VAE with a PSF-aware likelihood and a
  latent flow for galaxy images.
- Application: Boruah et al. 2025, arXiv:2502.04158 and arXiv:2511.14667 — diffusion prior
  and likelihood scaling for mass mapping, then DES Y3.
- Application: Remy et al. 2026, arXiv:2606.31988 — amortised joint posterior of field and
  cosmology, MIRA and TARP, cost against NUTS.
- Application: Mishra et al. 2026, arXiv:2601.14377 — overlap patches for volumes larger
  than the training box, and the large-scale limit.
- Critique: Rodriguez et al. 2018, arXiv:1801.09070 — GAN mode collapse on inhomogeneous
  samples.
- Critique: Doeser et al. 2026, arXiv:2606.10023 — what posterior diagnostics miss, and how
  many simulations generative posteriors need.

## Not verified
<!-- key: not-verified -->

- The GAN emulator used as baseline by arXiv:2605.23114 (its reference 16) and the origin of
  its 57-cosmology data set: not identified.
- The MIRA calibration score (Sharief et al. 2026) and the flow-matching foundation paper
  (Lipman et al. 2022): cited inside arXiv:2606.31988 and arXiv:2605.23114, not read.
- The training details of the DES Y3 diffusion network (its reference 4, read only as
  arXiv:2502.04158 Sect. III) beyond the preprocessing and DPS scaling.
- Whether any survey collaboration has adopted a generative model for a headline covariance
  or mock set.
