# Machine learning in cosmology — methods

Scope: the machine-learning methods used in cosmological analyses, what each does, its defining equations, its codes and its range of validity.
Snapshot: 2026-10-17

Flags: `[src]` abstract read this session; `[src: Sect. n]`, `[src: Eq. n]`,
`[src: Table n]` body read; `[sec]` named secondary source; `[der]` derived here.

## 1. Emulators of summary statistics
<!-- key: emulators-of-summary-statistics -->

An emulator is a regression from parameters θ to a model prediction t(θ),
trained on N_train evaluations of an expensive code (a Boltzmann solver, a
perturbation-theory code, or a suite of simulations) and then used inside a
likelihood. Its error is an interpolation residual against the training-type
calculation, not a theory error against the Universe. The sibling
`cosmo-statistics-inference` holds the error budgets of CosmoPower and
EuclidEmulator2 and their place in likelihoods; `cosmo-simulations-mocks`
holds the simulation suites and the gravity-only emulator comparison. This
section covers the methods.

**Regression families.**

| Family | How it works | Typical training set | Reference |
|---|---|---|---|
| Interpolation over a small simulation design (precision emulation of N-body output) | a limited set of simulations spanning the prior range is interpolated to predict the non-linear spectrum at the required accuracy; the interpolation scheme is not stated in the abstract read | tens of simulations: 37 models for the Coyote Universe wCDM matter power spectrum | Heitmann et al. 2009, arXiv:0902.0429 [src] |
| Gaussian process regression | standard regression for simulation-trained emulators, which "struggle with scalability in sample size and dimensionality" | the earlier Goku emulators | arXiv:2507.07184 [src] |
| Neural network on Boltzmann-code output | dense network maps θ (and z) to the spectrum or its principal components; spectra split as P = P_L × P_NL-corr because the split learns the non-linear parameters better | about 1.8 × 10⁵ training and 2 × 10⁴ test spectra at 420 k values in [10⁻⁵, 10] Mpc⁻¹, z in [0, 5] | Spurio Mancini et al. 2022 (CosmoPower), arXiv:2106.03846 [src: Sect. 3.2] |
| Iteratively trained network | training points drawn where the posterior is, in successive rounds, as a MontePython plug-in | about two orders of magnitude fewer CLASS calls than a traditional run | Nygaard et al. 2022 (CONNECT), arXiv:2205.15726 [src] |
| Multi-fidelity neural network | joint training on many low-resolution and few high-resolution simulations; 2-step architecture, Bayesian hyperparameter search, k-fold training, per-z PCA | Goku suite, ten-dimensional parameter space | Yang et al. 2025 (T2N-MusE, GokuNEmu), arXiv:2507.07184 [src] |
| Network with physical auxiliary inputs | θ supplemented by the linear P(k), resolution descriptors and a summary of the initial Gaussian field; one network across three resolution tiers | Ginkaku simulations, nine-parameter w0waν CDM space: 1000 cosmologies at 1024³ particles in 1024 h⁻¹Mpc (fixed and random phases), nested subsets of 50 at 2048³ and 20 at 3000³ (1000 h⁻¹Mpc), plus 100 fiducial realisations; 11 snapshots from z = 3 to 0 | Tanaka et al. 2026 (DarkEmulator2), arXiv:2605.28596 [src: Sect. 2.3, Table 2] |
| Emulated perturbation-theory kernels | network emulators replace the costly loop integrals; input is a spline representation of the linear P(k), so the cosmological model is not hard-coded | trained on one-loop EFTofLSS outputs; differentiable (JAX) | Reeves et al. 2025 (PyBird-JAX), arXiv:2507.20990 [src] |
| Transformer emulator of multi-tracer multipoles | dense layers plus transformer blocks; inputs are cosmology and bias parameters for several tracers and redshift bins | EFT predictions for SPHEREx | Adamo et al. 2026, arXiv:2603.16003 [src] |
| Symbolic emulator | an analytic expression in θ and ℓ found by symbolic regression | CLASS spectra of C_ℓ^φφ for ΛCDM + Σm_ν + w0wa | Vokrouhlicky et al. 2026 (CMBolic), arXiv:2606.07745 [src] |

**Architectures read in the bodies.** DarkEmulator2: a fully connected
network of three hidden layers of 2000 neurons with ELU activations,
chosen by a CMA-ES search over architecture and training settings; it
regresses P_nl itself (not the boost P_nl/P_lin) with 150 samples of the
linear spectrum as extra inputs, which contains the boost approach as a
special case (arXiv:2605.28596) [src: Sect. 3.2, 4.1, App. E].
T2N-MusE (GokuNEmu): a low-fidelity network plus a low-to-high-fidelity
correction network ("2-step"), per-redshift PCA compression of
lg P(k, z) at 6 × 64 outputs, a two-stage hyperparameter search and
k-fold training (arXiv:2507.07184) [src: Sect. II.1, IV]. PyBird-Emu:
networks trained only on the coefficients of a spline decomposition of
P_lin, so the emulator is independent of the cosmological model that
produced P_lin (arXiv:2507.20990) [src: Sect. 1].

**Validation metrics in use.** (i) Fractional error percentiles on a held-out
test set as a function of k: CosmoPower reports the 68, 95 and 99 percentiles
[src: Sect. 3.2]. (ii) Δχ² between emulated and exact predictions with the
survey covariance: the SPHEREx emulator quotes a median Δχ² = 0.069 on its
test set [src, arXiv:2603.16003]. (iii) Posterior comparison on a full
likelihood: shift of the 1D best fit in units of σ and change of the 1D error
(0.078σ and 0.82% for SPHEREx, arXiv:2603.16003) [src]; 0.01–0.1σ for
CONNECT against CLASS (arXiv:2205.15726) [src]. The CosmoPower authors state
that a full inference test is "the only way" to validate an emulator for a
given analysis [src: Sect. 3.2, arXiv:2106.03846]. (iv) Leave-one-out
cross-validation on the simulation design, the only option when each
training point is a simulation (arXiv:2507.07184) [src].

**Error propagation.** Grandón et al. 2022 (arXiv:2205.11587) propagate
the approximation error that a network reports on its validation set into
the likelihood, which removes the bias "even for strongly biased neural
nets" [src]. Whether survey analyses adopt it is tracked in
`cosmo-statistics-inference`.

## 2. Neural compression and field-level networks
<!-- key: neural-compression-and-field-level-networks -->

A compression network F_φ maps a high-dimensional field or data vector x to
summaries t = F_φ(x) with dim(t) = dim(θ); the summaries then enter a
likelihood or a neural density estimator (§3). The results obtained with
these summaries on survey data belong to `cosmo-beyond-two-point` and the
probe skills; this section fixes what each method is.

**Optimal compression, the reference point.** Compression to the score,
t = ∇_θ ln L at a fiducial θ, preserves the Fisher information with
n = dim(θ) numbers; it generalises Karhunen–Loève (MOPED-type) linear
compression to non-Gaussian data (Alsing et al. 2018, arXiv:1712.00012)
[src]. It is optimal only locally, around the fiducial point.

**Training objectives for a compression network** (review of the losses in
Lanzieri et al. 2024, arXiv:2407.10877 [src: Sect. 3]):

| Loss | Definition | What the summary estimates | Sufficient? |
|---|---|---|---|
| Mean squared error | L = (1/N_θ) Σ_i (t_i − θ_i)² | the posterior mean | not guaranteed: two posteriors can share a mean [src: Sect. 3] |
| Mean absolute error | L = (1/N_θ) Σ_i abs(t_i − θ_i) | the posterior median | same pathology as MSE [src: Sect. 3] |
| Gaussian negative log-likelihood | network predicts mean and variance | mean and spread, Gaussian form | not in general (appendix of arXiv:2407.10877) |
| Fisher information (IMNN) | maximise ln det F of the summaries at a fiducial point, from simulations at and around it | locally sufficient summaries | at the fiducial point; one retraining at the recovered point restores optimality (arXiv:2107.07405) [src] |
| Variational mutual-information maximisation (VMIM) | L = −ln q(θ ∣ F_φ(x); φ′), with q a conditional density estimator trained jointly; a lower bound on I(t, θ) = D_KL(p(t,θ) ‖ p(t)p(θ)) | sufficient summaries, given network flexibility and data | yes in the limit [src: Sect. 3, Eq. Loss_vmim] |

In the controlled test of arXiv:2407.10877 the VMIM summaries improve the
(Ω_c, σ8) figure of merit by 1.24 times over MSE and 1.1 times over MAE,
and similar factors hold for (Ω_c, w0) and (σ8, w0) [src: Sect. 6.3, Table 4]. The marginals
move as well: w0 = −1.00 (+0.20/−0.22) with VMIM against −1.01
(+0.19/−0.20) from the full-field HMC truth, but −1.13 (+0.23/−0.22) with MSE,
−1.16 ± 0.22 with MAE and −0.73 (+0.19/−0.22) with a Gaussian
negative-log-likelihood loss [src: Table 5]. The GNLL loss should in
principle give the MSE summaries but is "hard to train" because it also
fits the covariance [src: Sect. 6.3]. A poorly chosen loss therefore biases
the parameters, not only widens them.

The IMNN was introduced by Charnock et al. 2018
(arXiv:1802.03537) [src]; VMIM in cosmology by Jeffrey et al. 2021 on DES SV
lensing maps (arXiv:2009.08459) [src; attribution from arXiv:2407.10877,
Sect. 3].

**Architectures by data geometry.**

| Data | Architecture | First or reference cosmology use |
|---|---|---|
| 3D matter density cubes | 3D convolutional network | Ravanbakhsh et al. 2017, arXiv:1711.02033 [src] |
| Flat lensing convergence maps | 2D CNN | Gupta et al. 2018, arXiv:1802.01212 [src] |
| Full-sky tomographic lensing maps | graph-convolutional network on HEALPix (n_side = 512) | Fluri et al. 2022, KiDS-1000, arXiv:2201.07771 [src: abstract] |
| 2D total-mass maps from hydrodynamical runs | CNN with likelihood-free marginalisation over feedback | Villaescusa-Navarro et al. 2021, arXiv:2109.10360 [src] |
| 21 cm light-cones | self-supervised Vision Transformer (JEPA pre-training) as a frozen encoder | Pietschke et al. 2026 (SKATR), arXiv:2608.26354 [src: abstract] |

**What the survey map-level analyses did** (method sections read):

| Analysis | Network and input | Loss | Training set and schedule | Inference |
|---|---|---|---|---|
| KiDS-1000 GCNN (arXiv:2201.07771) | DeepSphere graph CNN on padded HEALPix maps, ten channels (two shear components × five bins), residual layers repeated five times; three fiducial and three benchmark networks [src: Sect. IV.6, Table 2] | information-maximising loss L = log det Cov_θ(ŝ) − 2 log abs(det ∂Ψ_θ(ŝ)/∂θ) with a regulariser λ = 100, trained on only (Ω_M, σ8, w0, A_IA) because the other parameters made training unstable [src: Eq. 6, 7] | CosmoGrid fiducial and perturbed runs; 100 000 steps, batch 64 on 8 GPUs, Adam at 10⁻⁴; networks overfit the 16 000 fiducial noise maps if trained long enough, so evaluation uses new noise [src: Sect. IV.6.1] | outputs of three GCNNs and three fully connected power-spectrum networks MOPED-compressed per network and averaged, because a single MOPED on 240 outputs was numerically unstable; then GPABC [src: Sect. IV.7, IV.8.2] |
| HSC Y1 CNN (arXiv:2301.01354) | residual CNN on 4 × 104 × 104 convergence maps of 3 × 3 deg² sub-fields, n_ch = 64, n_block = 10 [src: Sect. IV.1.3, Table 3] | mean squared error on normalised (Ω_m, S8, A_IA) and, optionally, four baryon parameters [src: Eq. 32] | 800 ray-tracing realisations per cosmology (1.2 × 10⁶ maps), or 1600 with free baryons (2.4 × 10⁶); eight epochs [src: Sect. IV.1.4] | Gaussian likelihood of the CNN outputs averaged over 19 sub-fields, covariance from 800 independent realisations with the Anderson–Hartlap factor, interpolated through its Cholesky factor [src: Sect. V, Eq. 34–38] |
| DES Y3 C_ℓ × CNN (arXiv:2403.02314) | three flat 512 × 512 patches (A, B, C) cut from n_side = 1 superpixels, eight channels (E and B modes, four bins); four CNNs per patch, averaged with sky-fraction weights; MLP ensembles of 12 for C_ℓ and peaks [src: Sect. 6.2, 6.3] | mean squared error, one output per parameter [src: Sect. 6.2] | 9264 mock data sets (three noise realisations of 3088 Gower Street maps), up to 200 epochs with early stopping on a fourth noise realisation [src: Sect. 6.3] | NLE; TARP in (Ω_m, S8, w) from 50 leave-one-out repetitions [src: Sect. 7.2.2] |
| DES Y3 hybrid statistics (Williamson et al. 2026, arXiv:2606.11309) | the same C_ℓ MLP (ten summaries) and patch CNNs (four per patch), stacked hierarchically to 22 numbers, repeated with four initialisations to 88, compressed to 7 [src: Sect. 6.2] | VMIM through a four-Gaussian mixture density network, plus VICReg on the last step (added after unblinding) [src: Sect. 6.2, 7.5] | same 9264 maps; a fourth noise realisation of 3088 mocks kept blind to the compressors for the density estimation [src: Sect. 6.2] | ensemble of eight MAFs in ltu-ili, 30% validation, emcee sampling [src: Sect. 6.3] |
| DES Y3 lensing + clustering design (arXiv:2511.04681) | DeepSphere graph CNN on n_side = 512 partial-sky maps, eight channels (four κ and four n_g bins), 6.87 million parameters, dropout 0.01 [src: Sect. IV.1.2, Table 3] | VMIM, L = −log q(θ ∣ S_φ(x); φ) with q a Gaussian mixture over ten parameters; q discarded after training [src: Eq. 14, 15] | 10⁶ grid maps (400 per cosmology × 2500) plus 40 000 at the fiducial, over 15 TB; 500 000 steps (forty epochs, ~24 hours) at global batch 256 on four Perlmutter nodes of four A100 GPUs [src: Sect. III.7, IV.1.2] | NLE with a conditional sum-of-sigmoids flow, loss −log q(s ∣ θ) [src: Sect. IV.2.1, Eq. 17] |

The design paper gives the reason for discarding the variational posterior
of the VMIM step: it would carry the non-uniform Sobol prior of the
CosmoGridV1 sampling, while a separately learned likelihood allows a plain
uniform prior [src: Sect. IV.1.1]. The DES Y3 hybrid paper notes that the
earlier MSE scheme of arXiv:2403.02314 is optimal only for Gaussian
parameter posteriors [src: Sect. 6.2.1, Eq. 29–30].

**Reducing the training cost.** An ensemble of CNNs trained on low-resolution
particle-mesh fields stays informative on simulations about a thousand times
more costly, and on halo catalogues; a single network can be less
informative than the power spectrum (Sáez-Casares et al. 2026,
arXiv:2610.19891) [src]. Multi-fidelity training (pre-training on GLASS
log-normal mocks, fine-tuning on N-body) gives calibrated KiDS-Legacy-like
posteriors from 60 high-fidelity simulations (Saoulis et al. 2026,
arXiv:2606.23346) [src]. Its training sets are about 100 000 log-normal
mocks from about 6500 CAMB cosmologies and about 47 000 Gower Street mocks
at 590 cosmologies, augmented to 80 pseudo-independent footprints per
simulation [src: Sect. 2.5]. In the body, fine-tuned models are
overconfident at small N: they inherit the too-tight widths of the
log-normal problem and need N ~ 100 high-fidelity simulations to "unlearn"
it; calibration matches the high-fidelity-only models from N ≥ 120, and
below N = 400 transfer learning gains a factor 2–3 in constraining power
[src: Sect. 4.2.1]. Fine-tuning the compressor as well as the density
estimator works better than freezing the compressor [src: Sect. 4.2.1].

## 3. Neural posterior, likelihood and ratio estimation
<!-- key: neural-posterior-likelihood-and-ratio-estimation -->

Simulation-based (implicit, likelihood-free) inference replaces an explicit
likelihood by a density or ratio learned from pairs (θ_i, x_i) drawn from
the prior and the simulator; the review is Cranmer et al. 2020
(arXiv:1911.01429) [src]. How to validate the result (coverage, TARP,
calibration at fixed θ, the simulation count against Dodelson–Schneider) is
statistics and lives in `cosmo-statistics-inference`; this section gives the
estimators.

**The three targets.**

| Estimator | Learns | Then | Foundation |
|---|---|---|---|
| Neural posterior estimation (NPE) | q_φ(θ ∣ x) ≈ p(θ ∣ x) with a conditional density estimator; amortised over x | sample q directly; sequential variants (SNPE) need a proposal correction | Papamakarios et al. 2016, arXiv:1605.06376 [src]; APT/SNPE-C, Greenberg et al. 2019, arXiv:1905.07488 [src] |
| Neural likelihood estimation (NLE) | q_φ(x ∣ θ) ≈ p(x ∣ θ) | multiply by the prior and sample with MCMC or nested sampling; data sets combine by product | Sequential Neural Likelihood, Papamakarios et al. 2019, arXiv:1805.07226 [src]; DELFI with active learning, Alsing et al. 2019, arXiv:1903.00007 [src] |
| Neural ratio estimation (NRE) | a classifier between joint (θ, x) and marginal p(θ)p(x) pairs gives r(x, θ) = p(x ∣ θ)/p(x) | use r in MCMC, or directly as posterior/prior | Hermans et al. 2020, arXiv:1903.04057 [src]; truncated marginal NRE (swyft), Miller et al. 2021, arXiv:2107.01214 [src] |

**Density estimators.** Normalising flows (an invertible map of a simple
base density; Rezende et al. 2015, arXiv:1505.05770 [src]), of which the
masked autoregressive flow is the most used in cosmology (Papamakarios et
al. 2017, arXiv:1705.07057 [src]); mixture density networks; and, more
recently, continuous flows trained by flow matching, which allow
unconstrained architectures and scale to large problems (Dax et al. 2023,
arXiv:2305.17161 [src]).

**A worked survey case: KiDS-SBI** (arXiv:2404.15402). Score compression of
pseudo-C_ℓ to the parameter dimension [src: Sect. 5.3]; an ensemble of six
conditional MAFs, each of three to eight MADEs with two hidden layers of 50
neurons; 2000 initial Latin-hypercube points, then active learning until the
validation loss stops decreasing for 20 epochs; the loss converged after
5000 realisations but 18 000 were used; the six flows are stacked with
weights from their validation losses and sampled with nautilus, checked with
emcee; the compression is redone at the MAP of the first run
[src: Sect. 5.4, Eq. 44].

**Choice between estimators.** In the 2021 benchmark no algorithm was
uniformly best, the choice of performance metric was critical, and
sequential estimation improved sample efficiency (Lueckmann et al. 2021,
arXiv:2101.04653) [src]. The benchmark scores posteriors by a
classifier two-sample test (C2ST: 1 for a fully distinguishable posterior,
0.5 for a perfect one) because MMD was sensitive to its kernel choice, the
median distance can be "gamed" by a good point estimate, and the
log-probability of the true parameter averaged over 10 observations
correlated only at 0.3–0.6 with C2ST [src: Sect. 2.2, 3]. For several
tasks no algorithm solved the problem within the budget [src: Sect. 3].
Thiele 2026 recommends NPE as the default, NLE for several i.i.d. data sets
or many parameters, NRE when a flow is inconvenient, and simple linear
compression (MOPED) before neural compression for tabular summaries
(arXiv:2605.10719) [src: Sect. 2.7]. NLE and NRE allow data sets to be combined and
analysis choices changed after training: Merlin applies scale cuts, changes
the area or drops cosmic shear from a 3×2pt bank at no extra model
evaluation, with a 50-dimensional parameter space and two orders of
magnitude fewer CPU-hours than nautilus (Wernersson et al. 2026,
arXiv:2609.24946) [src]. All benchmarked algorithms can be overconfident and
ensembles help (Hermans et al. 2022, arXiv:2110.06581) [src].

**Public codes.** `sbi` (PyTorch; Tejero-Cantero et al. 2020,
arXiv:2007.09114) [src]; `pydelfi` (arXiv:1903.00007) [src]; `swyft`
(arXiv:2107.01214); `sbi_lens` as a differentiable test simulator
(arXiv:2407.10877) [src]. Versions and maintenance belong to
`cosmo-software-ecosystem`.

## 4. Generative models of fields and catalogues
<!-- key: generative-models-of-fields-and-catalogues -->

A generative model learns p(x ∣ c) — a field, an image or a point set x,
conditioned on parameters or on another field c — and samples it fast. Uses
in cosmology: fast surrogate simulations (mocks, covariance ensembles),
upscaling, priors for inverse problems (mass mapping, initial conditions),
and explicit field-level likelihoods.

| Family | Principle | First or reference cosmology use | Reference |
|---|---|---|---|
| Generative adversarial network | generator G and discriminator D in a minimax game; at the optimum G reproduces the data distribution and D = 1/2 | 2D N-body slices of 500 and 100 Mpc; P(k) agreement 1–2% for 0.06 < k < 0.4 | Goodfellow et al. 2014, arXiv:1406.2661 [src]; Rodriguez et al. 2018, arXiv:1801.09070 [src: abstract] |
| Variational autoencoder + flow, conditioned on physical parameters, inside a physical forward model of PSF and noise | learns galaxy morphology from noisy, PSF-convolved HST/ACS COSMOS stamps; GalSim-Hub repository | image simulations for shear calibration | Lanusse et al. 2021, arXiv:2008.03833 [src] |
| Denoising diffusion (score-based) model | learns to reverse a noising process; trained on a weighted variational bound linked to denoising score matching | dark-matter density fields and dust images; fidelity measured with three metrics, issues identified | Ho et al. 2020, arXiv:2006.11239 [src]; Mudur et al. 2022, arXiv:2211.12444 [src] |
| Point-cloud diffusion | galaxies or haloes as a set of 3D points with attributes, no voxelisation; usable for emulation and for the conditional likelihood of a galaxy field | Quijote massive haloes | Cuesta-Lazaro et al. 2023, arXiv:2311.17141 [src] |
| Conditional point-cloud diffusion from dark matter to galaxies | generates galaxies with positions, SFR and stellar mass from a dark-matter field without halo finding; trained on IllustrisTNG | (151.3 Mpc)³ catalogue with SFR > 1 M_⊙/yr in about 10 s on one GPU | Moriwaki et al. 2026, arXiv:2607.19808 [src: abstract] |
| Latent diffusion with overlapping patches | generates arbitrarily large 3D fields conditioned on an input field ("upscaling") | TNG300-2 dark-matter density and gas temperature from training on ~1% of the volume; P(k) within 10% for k ≤ 5 h Mpc⁻¹; a CAMELS 25 h⁻¹Mpc box upscaled to 205 h⁻¹Mpc without fine-tuning | Mishra et al. 2026 (Cosmo-FOLD), arXiv:2601.14377 [src: abstract] |
| Conditional flow matching | continuous flow from label-specific noise to convergence maps conditioned on Ω_m, σ8 | fidelity better than 1% (basic statistics) and 5% (higher-order) against a GAN benchmark at below 10% and 20% | Li & Kacprzak 2026, arXiv:2605.23114 [src: abstract] |
| Diffusion prior in posterior sampling | diffusion model as prior, data enter through the likelihood score (DPS) | DES Y3 mass maps at 1 arcmin; standard DPS biased, corrected by rescaling the likelihood score | Boruah et al. 2025, arXiv:2511.14667 [src] |

**Validation of a generative model.** Pixel one-point distribution, peaks,
P(k), bispectrum and the covariance of P(k) across samples, compared with
an ensemble of simulations from random initial conditions
(arXiv:2605.23114) [src]. For posterior sampling of initial conditions,
Doeser & Jasche 2026 compared a stochastic-interpolant model and a GLOW flow
with about 6 × 10⁴ independent HMC samples of a 32³ field in 1 h⁻¹Gpc:
both recover the posterior mean, the mean-field power spectra agree with
the truth to within 10% on most scales, but the power spectrum of the
voxel-wise variance field deviates by up to ~30%, and training on HMC
samples with a reverse-KL term improves the variance structure
(arXiv:2606.10023) [src: Sect. 3.2, 5.1, 5.2]. Matching means, marginals or
cross-correlation does not imply a correct uncertainty structure [src].

## 5. Learned corrections of fast simulations
<!-- key: learned-corrections-of-fast-simulations -->

Networks that replace or correct a gravity or hydrodynamics solver at the
field level. They differ from the emulators of §1 by predicting particles
or fields, not a summary. The simulation codes they correct (COLA, FastPM,
LPT) and their accuracy are in `cosmo-simulations-mocks`.

| Approach | Input → output | Accuracy and range stated | Reference |
|---|---|---|---|
| Deep Density Displacement Model (D³M), U-Net | Zel'dovich displacements → non-linear displacements | beats 2LPT point-wise and in 2- and 3-point functions; extrapolates to other cosmological parameters | He et al. 2019, arXiv:1811.06533 [src] |
| Style-parameter CNN emulator | linear displacements → non-linear displacements and velocities, Ω_m as a style parameter at each layer | accurate to k ~ 1 h Mpc⁻¹ in density, displacement and momentum spectra, bispectrum, halo abundances and profiles; generalises to primordial non-Gaussianity without retraining; differentiable | Jamieson et al. 2023, arXiv:2206.04594 [src] |
| NECOLA, CNN correction of COLA | COLA particle positions → Quijote N-body positions | sub-percent to k ≃ 1 h Mpc⁻¹; trained at one cosmology, within ≃ 1% to k = 1 h Mpc⁻¹ when Ω_m, Ω_b, h, n_s, σ8, w, M_ν vary | Kaushal et al. 2022, arXiv:2111.02441 [src] |
| MG-NECOLA | MG-PICOLA f(R) snapshots → Quijote-MG N-body | ≲ 1% in P(k) and bispectrum to k ≃ 1 h Mpc⁻¹; below 5% outside the training cosmology; recovers the GR limit and M_ν ≤ 0.4 eV suppression though trained massless; speed-up ~1500 | Orjuela-Quintana et al. 2026, arXiv:2604.19613 [src: abstract] |
| Hybrid physical–neural ODE | Fourier-space network adds an effective force to a particle-mesh solver | P(k) gain similar to PGD; better cross-correlation; more robust to resolution and cosmology changes | Lanzieri et al. 2022, arXiv:2207.05509 [src] |
| Lagrangian Deep Learning | FastPM dark matter → stellar, gas density and temperature maps through learned displacement layers (gradient of an effective potential) | ~10 learned parameters; nearly four orders of magnitude cheaper than hydrodynamics | Dai et al. 2021, arXiv:2010.02926 [src: abstract] |
| Lagrangian neural cellular automaton | residual corrections to Zel'dovich, iterated on a comoving lattice; equivariant; gives trajectories | trained on Quijote across redshifts and cosmologies; built as a differentiable forward model | Jacobus et al. 2026, arXiv:2607.27320 [src] |
| Stochastic super-resolution | low-resolution N-body → 512 times more particles | from 16 low/high-resolution training pairs: P(k) to percent level to 16 h⁻¹Mpc, halo mass function within 10% to 10¹¹ M_⊙; deployed in a box 1000 times larger | Li et al. 2021, arXiv:2010.06608 [src: abstract] |
| Baryon painting (VAE, GAN) | BAHAMAS matter density → gas pressure, applied to SLICS | tSZ maps and κ × tSZ spectrum and variance consistent with BAHAMAS | Tröster et al. 2019, arXiv:1903.12173 [src] |
| BIND, conditional flow matching | dark-matter-only halo → hydrodynamical dark matter, gas and stars; CAMELS SB35, 1024 paired runs, 35 parameters | masses at the percent level, profiles ≲ 10%; reproduces the projected P(k) suppression to the ceiling set by pasting the hydrodynamical haloes | Lee et al. 2026, arXiv:2609.10709 [src: abstract] |

The style-parameter emulator was trained on 2000 Latin-hypercube Quijote
cosmologies split 1757 / 122 / 121 into training, validation and test
(arXiv:2206.04594) [src: Sect. "Setup"]; a network trained at one cosmology
mis-shapes the BAO bump at k ~ 0.04 h Mpc⁻¹ when Ω_b/Ω_m moves away from
its single training value [src: Sect. "Displacement Power Spectra"], and its
transfer to f_NL = ±100 local, orthogonal and equilateral initial
conditions was tested on seven Quijote-PNG runs [src: Sect. "Primordial
non-Gaussianity"].

**Common pattern.** Learning a residual on top of a physical approximation
(Zel'dovich, COLA, PM) keeps large scales exact by construction and
generalises across cosmology better than learning the full map
(arXiv:2607.27320, arXiv:2111.02441, arXiv:2604.19613) [src]. Every row
above was validated on summaries of the same simulation family as its
training set.

## 6. Classification of transients and spectra
<!-- key: classification-of-transients-and-spectra -->

Classifiers assign a class probability to a light curve, a spectrum or an
image. In cosmology they decide which supernovae enter a photometric Hubble
diagram, which spectra are quasars (and at what redshift), and which images
are strong lenses. How the class probabilities enter SN Ia cosmology (BEAMS,
the contamination term of the systematic budget) is in `cosmo-supernovae`;
redshift fitting and visual inspection in spectroscopic pipelines are in
`cosmo-data-pipelines`.

| Task | Method | Key design choice | Reference |
|---|---|---|---|
| SN light curves, PLAsTiCC winner | Gaussian-process fit of all bands, augmentation of the training set in redshift and observing conditions, boosted decision trees | augmentation makes the classifier independent of the training-set redshift distribution | Boone 2019 (Avocado), arXiv:1907.04690 [src] |
| SN light curves | recurrent neural network on photometry only, with optional host redshift; Bayesian RNN variants | measures calibration and overconfidence out of distribution | Möller et al. 2019 (SuperNNova), arXiv:1901.06384 [src] |
| SN light curves | CNN on 2D Gaussian-process "flux heatmaps" in wavelength–time, with uncertainty heatmaps | independent of the filter set; no redshift needed | Qu et al. 2021 (SCONE), arXiv:2106.04370 [src] |
| Alert stream, hierarchical | GRU recurrent network with a hierarchical cross-entropy over an observational taxonomy, host context concatenated | classifies after a single observation | Shah et al. 2025 (ORACLE), arXiv:2501.01496 [src] |
| Alert broker | tree-based classifiers on engineered features plus deep networks; CATS architecture | infrastructure tested on ELAsTiCC | Fraga et al. 2024 (Fink), arXiv:2404.08798 [src] |
| SN spectra | CNN classifying type, age, redshift and host instead of template matching; trained on over 4000 spectra | speed independent of the template library size | Muthukrishna et al. 2019 (DASH), arXiv:1903.02557 [src: abstract] |
| Quasar spectra | CNN posed as feature detection: line presence gives the class, line wavelength the redshift; BAL extension | line confusion below 0.2% | Busca et al. 2018 (QuasarNET), arXiv:1808.09955 [src: abstract] |
| Strong-lens images | CNNs, SVMs, arc and ring finders and visual inspection compared blind on 100 000 candidates | false-positive rate is the controlling metric | Metcalf et al. 2018, arXiv:1802.03609 [src: abstract] |

**The metric matters.** PLAsTiCC scored entries with a weighted
multi-class logarithmic loss; Avocado's 0.468 is on a flat-weight log-loss
(arXiv:1907.04690) [src], while the official leaderboard scores of the top
three were 0.685, 0.699 and 0.700 (arXiv:2012.12392) [src: Sect. 3.4, Fig. 7].
On the test set without the unseen "Other" class the first two places swap
(arXiv:2012.12392) [src: Sect. 3]. A classification number is meaningful
only with its metric, its class weights and whether unseen classes were
present.

## 7. Anomaly detection
<!-- key: anomaly-detection -->

Anomaly detection ranks objects by how poorly a model of the known
population describes them; there is no label for the target class. Three
designs recur, and the review of Huertas-Company & Lanusse (arXiv:2210.01813,
Sect. 5.2) groups the astronomy applications into transients and
imaging/spectroscopic outliers.

| Design | Score | Example and data | Reference |
|---|---|---|---|
| Unsupervised random forest on features | dissimilarity from an unsupervised forest | more than two million SDSS galaxy spectra; the top 400 include lenses, double-peaked emitters, extreme line ratios | Baron et al. 2017, arXiv:1611.07526 [src: abstract] |
| Isolation forest on a learned latent space | isolation depth | variational recurrent autoencoder trained on 1% of PLAsTiCC; 1 129 184 events ranked; ~95% pure sample of rare transients, flagged before peak | Villar et al. 2021, arXiv:2103.12102 [src: abstract] |
| Autoencoder + normalising flow | low probability under a flow in a redshift-invariant latent space | DESI EDR Bright Galaxy Survey; many outliers are stars misclassified as galaxies, traced to the PCA star templates of the pipeline | Liang et al. 2023, arXiv:2307.07664 [src] |
| Predictive model of known classes | deviation from the predicted light curve, as a function of time | ZTF light curves; a Bayesian parametric model reaches area under the precision–recall curve above 0.79 for most rare classes, and beats a flexible neural model | Muthukrishna et al. 2022, arXiv:2111.00036 [src: abstract] |
| Active anomaly detection | isolation forest re-weighted by expert feedback | ~80% more true anomalies than a static isolation forest on the Open Supernova Catalog (Ishida et al. 2021, arXiv:1909.13260 [src: abstract]); Astronomaly roughly doubles the interesting anomalies in the first 100 objects viewed (Lochner et al. 2021, arXiv:2010.11202 [src: abstract]) | — |

**Operational use.** The Fink broker runs an isolation forest on ZTF
features from 25 January 2023, sends the 10 most anomalous candidates each
night to experts, and retrains with Active Anomaly Discovery; in its first
year it triggered 33 supernovae (30 previously unreported) and nine new
dwarf novae (Pruzhinskaya et al. 2026, arXiv:2603.29511) [src: abstract]. A
comparison of three active frameworks finds that the best one depends on
the data: on ZTF light curves Protege, PineForest and Astronomaly recover
83, 78 and 38 variable stars in the first 100 objects, on Euclid images
PineForest finds 70 disturbed galaxies against 29 and 19 (Sreejith & Nichol
2026, arXiv:2609.36096) [src: abstract].

**Why flexible models are worse here.** A network flexible enough to fit
the known classes well also fits the anomalies; the parametric model wins
for that reason (arXiv:2111.00036) [src]. In PLAsTiCC the unseen "Other"
class made the classifiers assign it the probabilities of known classes
("subsumed-to" confusion) (arXiv:2012.12392) [src: Sect. 5].

**Cosmological use.** The same tools test the data model: scale-dependent
neural summaries with normalising flows estimate the Bayesian evidence of
CAMELS fields under each sub-grid model and identify the scale where a
model breaks down (Akhmetzhanova et al. 2025, arXiv:2508.05744) [src]. See
`systematics.md` §2.

## 8. Interpretability and symbolic regression
<!-- key: interpretability-and-symbolic-regression -->

Two routes: explain a trained network (attribution, latent-space geometry),
or replace it by an expression a physicist can read (symbolic regression).
The review lists interpretability among the open challenges of deep
learning in surveys (arXiv:2210.01813, Sect. 7.3.3) and treats discovery of
physical laws separately (Sect. 5.3).

**Attribution.**

| Study | Method | Finding | Reference |
|---|---|---|---|
| CNN on simulated lensing convergence | saliency maps; attribution = squared input-space saliency | the network improves (Ω_m, σ8) by 20% over power spectrum + peaks + Minkowski functionals with shape noise; noiseless maps: negative-κ regions carry 69–86% of the attribution (abstract; the body gives 86% for Gradient and 83% for Input × gradient saliency, Sect. IV.2); with noise, 36–68% lies in κ > 3σ_κ | Zorrilla Matilla et al. 2020, arXiv:2007.06529 [src] |
| CMB map classifier (ΛCDM against a feature model) | SHAP attribution with a Galactic mask as a control | attribution correctly excludes the mask; the decision rests on global variance over the unmasked sky; public SkyExplain pipeline | Ocampo et al. 2026, arXiv:2604.05290 [src] |
| Neural marked power spectrum | physically parametrised marks learned with a contrastive objective | at k_max = 0.2 h Mpc⁻¹, 2.9 times tighter σ8 and 1.8 times tighter Ω_m than classical marks (Fisher level); latent axes align with Ω_m and σ8 | Semenzato et al. 2026, arXiv:2606.11295 [src: abstract] |

**Symbolic regression.**

| Tool or result | What it does | Reference |
|---|---|---|
| GNN + symbolic distillation | sparse latent messages in a GNN, then symbolic regression on its components; recovers force laws and Hamiltonians, and finds a formula for the smoothed dark-matter overdensity at each Quijote halo from the masses and distances of its neighbours (the abstract calls it the "concentration of dark matter"), which generalises out of distribution better than the GNN | Cranmer et al. 2020, arXiv:2006.11287 [src: abstract; Sect. 4.3] |
| PySR / SymbolicRegression.jl | multi-population evolutionary search with an evolve–simplify–optimise loop; EmpiricalBench benchmark | Cranmer 2023, arXiv:2305.01582 [src] |
| Exhaustive symbolic regression | enumerates all expressions to a given complexity; selection by minimum description length; on cosmic chronometers + Pantheon+, ~40 of 5.2 million functions describe H(z) more economically than the Friedmann equation | Bartlett et al. 2022, arXiv:2211.11461 [src: abstract] |
| Symbolic linear P(k) | learns the ratio to an existing fitting function; RMS fractional error 0.2% for 9 × 10⁻³ < k < 9 h Mpc⁻¹; 950 times faster than CAMB, 36 times faster than the BACCO network; σ8 formula at 0.1% | Bartlett et al. 2024, arXiv:2311.15865 [src: abstract] |
| Symbolic CMB lensing spectrum (CMBolic) | see §1 | arXiv:2606.07745 [src] |

Symbolic emulators match neural ones in accuracy for smooth targets
(arXiv:2311.15865, arXiv:2606.07745) [src] and remain usable after the
codes they were trained on are outdated (arXiv:2311.15865) [src]; their
search cost grows quickly with the number of inputs.

## 9. Reviews and entry points
<!-- key: reviews-and-entry-points -->

Huertas-Company & Lanusse 2022 (deep learning for galaxy surveys,
arXiv:2210.01813); Dvorkin et al. 2022 (Snowmass white paper,
arXiv:2203.08056); Cranmer et al. 2020 (simulation-based inference,
arXiv:1911.01429); Thiele 2026 (SBI chapter of a 2026 series on machine
learning in astrophysics and cosmology; identifies training with limited
simulation budgets as the critical problem, arXiv:2605.10719) [src]; the
LSST DESC AI/ML white paper (arXiv:2601.14235) [src].

## 10. Not verified
<!-- key: not-verified -->

- Closed 2026-10-16: DarkEmulator2 and GokuNEmu architectures (§1), and
  the DES Y3 map-level loss (VMIM, Eq. 15 of arXiv:2511.04681) and
  calibration (§2 here, `systematics.md` §4).
- Whether flow-matching posterior estimation has been used on survey data
  in cosmology.
- Diffusion-model fidelity numbers of arXiv:2211.12444 (abstract gives
  none).
