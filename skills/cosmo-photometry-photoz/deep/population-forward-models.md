# Bayesian hierarchical and population (forward) models — cosmo-photometry-photoz dossier

Scope: how a population-model n(z) is built step by step (generative
chain, choice of population model, data model, selection and binning,
fitting of the hyper-parameters, propagation of their uncertainty), how a
histogram-type hierarchical model differs from it, how either is validated,
and what each choice has been shown to cost on mocks and data.
Snapshot: 2026-10-18.
From: Newman & Gruen 2022 review, Sect. 2.4, 4.1.3, 5.1; Tortorelli & Grün
2026 review, Sect. 3.0.2–3.0.3 (copied from `references/subtopics.tsv`).

Already in L2, not repeated here: why stacking per-galaxy posteriors is
biased and the CHIPPR argument
(`physics-and-methods.md#hierarchical-and-forward-population-models`); the
table of approaches with their headline accuracies (same section) and the
corresponding rows of `results.md#ensemble-n-z-characterisation`; the
arguments for and against forward modelling and the review's list of
required checks (coverage tests, posterior predictive checks, end-to-end
parameter shifts) in
`open-questions.md#spectroscopic-reweighting-versus-forward`; the
KiDS-1000 population-model debate and the KV450 hierarchical S8 in
`open-questions.md#did-redshift-calibration-make-stage-iii-lensing`.
How image simulations and source injection are built is in
`cosmo-data-pipelines` (`deep/source-injection.md`); generative networks
in general are in `cosmo-machine-learning`.

Symbols, following Alsing et al. 2023 (arXiv:2207.05819, Table 1): φ, the
stellar-population-synthesis (SPS) parameters of one galaxy (stellar,
gas and dust content); z, its redshift; ψ, the hyper-parameters of the
population model P(φ, z | ψ); η, the data-model parameters (zero points,
error floors); σ, the per-band flux uncertainties, drawn from an
uncertainty model P(σ | f, 𝒪) with assumptions 𝒪; f, the noiseless model
fluxes; d, the measured fluxes; S, selection into the analysis sample;
S^(k), selection into tomographic bin k; ẑ(d, σ), the photo-z estimator
used for binning. For the histogram model of Kyriacou et al. 2026
(arXiv:2605.15078): t, a template index; m, the r-band magnitude; f_ijk,
the fraction of the population in cell (template i, redshift j,
magnitude k).

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Write the generative chain
<!-- key: step-1-write-the-generative-chain -->

Model fluxes follow from the SPS spectrum l(λ; φ) redshifted, attenuated
by the intergalactic optical depth τ(z, λ) and integrated through the
passband W_b: f_b = (1+z)⁻¹/(4π d_L²) ∫ l(λ/(1+z); φ) e^{−τ} W_b dλ
(arXiv:2207.05819, Eq. 1) [src: Sect. II.1]. The chain is six steps
[src: Sect. II.2]: (1) draw (φ, z) from P(φ, z | ψ); (2) compute f with
the SPS model; (3) draw σ from the uncertainty model; (4) draw d from the
data model P(d | f, σ, η); (5) apply the selection cuts on the noisy
photometry, P(S | d, σ) ∈ {0, 1}; (6) assign a bin label with the survey's
own estimator, the bin being z_l^(k) < ẑ(d, σ) < z_u^(k) (Eq. 2). Repeating
until N objects pass gives one mock catalogue of the observed size;
repeating to N → ∞ and histogramming the true redshifts in each bin gives
n_k(z) = P(z | S^(k), ψ, η, 𝒪), an integral over population, data and
selection models (Eq. 3) that is never evaluated directly [src:
Sect. II.2]. The joint posterior of hyper-parameters and per-galaxy
latents carries the selection term P(S_i | ψ, σ_i, η) in the denominator
of each galaxy's factor (Eqs. 4–5); computing it for every galaxy at every
step is the bottleneck, which is why an emulator of the selection integral
or simulation-based inference (SBI) is needed [src: Sect. II.4].

Two properties follow from this form and are the authors' stated reasons
for the approach [src: Sect. II.4]: spectroscopic redshifts or extra bands
for any subset enter as additional likelihood terms, and their
non-representativeness does not matter "provided selection cuts are only
performed with respect to the main survey data"; and the population model
is global, the same for every bin and every survey, so external
constraints on galaxy evolution become priors on ψ. Image-level cuts
(shear quality, star–galaxy separation, deblending) are not photometric
selections; they can be absorbed into an effective population prior with
extra hyper-parameters, or neglected only if the photometric cuts are
shown to dominate (arXiv:2207.05819, App. A as summarised in Sect. VI)
[src: Sect. VI].

### Step 2. Choose the population model
<!-- key: step-2-choose-the-population-model -->

Four families are in use:

| Family | Parameters | Constrained by | Analysis |
|---|---|---|---|
| SPS with literature scaling relations | P(φ, z) = P(mass, z) P(metallicity \| SFR, mass) P(SFR \| mass, z) P(dust \| SFR, mass, metallicity) P(age \| SFR, mass) (Eq. 8); two-Schechter mass function with Leja et al. evolution; Planck 2015 volume element | defaults from the literature, not fitted | Alsing et al. 2023, arXiv:2207.05819 [src: Sect. III.2] |
| SPS with a learned population (pop-cosmos) | 16 SPS parameters of a Prospector-α variant: six-bin non-parametric star-formation history, two-component dust with variable law slope, AGN torus, free gas metallicity and ionisation, CLOUDY nebular emission [src: arXiv:2602.03935, Sect. III.1, Table 1]; density represented by a score-based diffusion model with 37,264 weights [src: arXiv:2402.00935, Sect. IV] | COSMOS2020, 26 bands | Alsing et al. 2024, arXiv:2402.00935; Leistedt et al. 2026, arXiv:2602.03935 |
| Phenomenological (GalSBI) | luminosity functions of a red and a blue population, Sérsic morphology, SEDs as Dirichlet-distributed mixtures of five kcorrect templates whose modes are interpolated between anchors at z = 0 and z = 3, α_i(z) = α_{i,0}^{1−z/3} α_{i,3}^{z/3} (Eq. 5); 53 parameters in the fiducial model | HSC deep and ultra-deep images | Fischbacher et al. 2024, arXiv:2412.08701 [src: Sect. 2.1.2, 4.3] |
| Histogram over template, redshift, magnitude | f_ijk with a uniform (Dirichlet) prior; z in steps of 0.05 to 3, m from 19 to 25 in steps of 0.1 | the survey's own fluxes | Kyriacou et al. 2026, arXiv:2605.15078 [src: Sect. 2, Eq. 3] |

Two pop-cosmos versions exist and should not be mixed when quoting the
training sample: the 2024 paper fits 140,938 galaxies with r < 25, two
magnitudes above the 3σ limit, because calibration and star–galaxy
separation degrade beyond i ≈ 25 [src: arXiv:2402.00935, Sect. II]; the
KiDS application uses the later Thorp et al. model trained on ~420,000
galaxies with IRAC Ch. 1 < 26, chosen because ~96% of r < 25 galaxies
would pass that cut, so the model is complete at KiDS depth [src:
arXiv:2602.03935, Sect. III.1]. SPS calls are emulated (Speculator), to
better than ~3% in flux over 99.9% of parameter space and ~1% over 99%
[src: arXiv:2602.03935, Sect. III.1]; emulation gave a 10⁴ speed-up over
FSPS [src: arXiv:2207.05819, Sect. II.3].

In the histogram model the template set is the prior on galaxy type: with
a uniform prior per template, a set holding six ellipticals per spiral
favours ellipticals [src: arXiv:2605.15078, Sect. 2.2]. Kyriacou et al.
start from ~300 BPZ templates, group them by k-means in the space of the
first four principal components into five groups and draw ten per group,
to avoid over-representing near-duplicates [src: Sect. 2.2].

### Step 3. Build the data model
<!-- key: step-3-build-the-data-model -->

- **Analytic (Alsing 2023).** Student-t with two degrees of freedom,
  P(d | f, σ, η) ∝ Π_b [1 + ½((d_b − α_zp,b f_b)/Σ_b)²]^(−3/2) (Eq. 16),
  Σ_b² = σ_b² + (β_b α_zp,b f_b)² (Eq. 17); zero points α_zp fixed to the
  published values and error floors β = 0.03 in all bands for GAMA and
  VVDS [src: Sect. III.3]. The uncertainty model is a 12-component
  mixture-density network with one 256-unit hidden layer, trained on MAP
  fluxes from per-galaxy fits (Eqs. 18–19) [src: Sect. III.4].
- **Learned from image simulations (pop-cosmos on KiDS).** Because SKiLLS
  reports photometry only for detected sources, the model is factorised
  as detection × uncertainty × noise, each conditioned on detection
  (arXiv:2602.03935, Eq. 3) [src: Sect. III.2]. Detection: a random forest
  on r magnitude and GAaP depth, trained on 800,000 SKiLLS objects, plus
  rejection sampling so that magnitude and depth distributions match the
  data [src: Sect. III.2.1]. AUTO-flux uncertainty: a conditional ODE flow
  trained by flow matching on 800,000 objects, needed because the Kron-like
  error depends on morphology and neighbours [src: Sect. III.2.2]. Noise:
  a conditional ODE flow for the ten flux residuals (nine GAaP bands plus
  r AUTO) trained on 100 SKiLLS tiles; normalising flows and correlated
  Student-t models failed to fit the bright and faint ends together [src:
  Sect. III.2.3]. Depths are 1σ GAaP limits, not 5σ detection limits
  [src: Sect. III.2].
- **Full image simulation (GalSBI).** Galaxies are rendered into survey
  images, SExtractor is run in forced-photometry mode and objects are
  matched to the input; an emulator replaces the image step from
  iteration 6 onwards [src: arXiv:2412.08701, Sect. 2.4.1, 4.3].

### Step 4. Reproduce selection, binning and weights
<!-- key: step-4-reproduce-selection-binning-and-weights -->

The mock must pass the same bin assignment as the data. pop-cosmos on
KiDS reruns BPZ, with the DR5 configuration because the public DR4 Z_B
could not be reproduced with the recommended settings; the two
configurations differ by a median |ΔZ_B| of 0.01 and a 95th percentile of
0.69 [src: arXiv:2602.03935, Sect. III.3]. The KiDS-1000 shear-sample flag
cannot be recomputed from DR4 columns, so a random forest on 20
photometric features emulates it, with class labels drawn as Bernoulli
variates; on its test set accuracy is ~63%, ROC area ≃ 0.90, precision
~0.44 and recall ~0.46, in a regime where ~25–30% of DR4 galaxies are in
KiDS-1000 [src: Sect. III.4]. lensfit weights are predicted by a neural
regressor (MAE 2.30, RMSE 3.25, R² = 0.58), the scatter attributed to
morphology and PSF information absent from the catalogue [src:
Sect. III.5]. In Alsing et al. 2023 the binning estimator is a small
neural network trained on GAMA (σ_z ≃ 0.06), with bins 0 < ẑ < 0.2 and
ẑ > 0.2 [src: arXiv:2207.05819, Sect. IV.2].

### Step 5. Fit the hyper-parameters
<!-- key: step-5-fit-the-hyper-parameters -->

| Route | How | Settings read | Output |
|---|---|---|---|
| None (validation of defaults) | ψ fixed to literature values; only the uncertainty model is fitted to the data | GAMA: mock drawn under r < 20.65, cuts r < 19.65 and J − K_s > 0.025, run to 5 × 10⁵ selected objects | one n(z) per bin [src: arXiv:2207.05819, Sect. IV.3] |
| Optimal transport (pop-cosmos) | minimise the Sinkhorn approximation of the Wasserstein-2 distance between simulated and real catalogues, 𝓛(ψ, η) = W₂[D(u, s, n \| ψ, η), D̂] (Eq. 11), by gradient descent through the simulator with base draws u, s, n held fixed (reparameterisation) | Adam, learning rate 10⁻⁴, stop after twenty epochs without improvement; distance summed over magnitudes and 25 adjacent-band colours; zero points and emission-line corrections initialised from 12,473 spectroscopic matches (zCOSMOS-bright, DEIMOS, C3R2) and then kept free | a point estimate [src: arXiv:2402.00935, Sect. IV, IV.1–IV.2] |
| Approximate Bayesian computation (GalSBI) | iterative batches on disjoint random sets of tiles; each posterior becomes the next prior (Eq. 12) | 10,000 prior samples, 10 tiles (0.38 deg²) at first, keep the 2,000 lowest distances, resample with a 20-component Gaussian mixture; tiles grow to 30 (1.15 deg²) by iteration 21; 31 iterations used all 746 HSC deep patches | posterior samples of ψ [src: arXiv:2412.08701, Sect. 2.4, 3, 4.3] |
| Gibbs sampling (histogram model) | alternate: draw (i, j, k) for each galaxy with probability f_ijk p(F̂ \| ijk) (Eq. 6), then f_ijk from the Dirichlet–multinomial given the counts n_ijk (Eq. 7) | Gaussian flux errors F̂_b ~ N(aF_b, σ_b²) (Eq. 1); 3000 samples in simulations; four random subsets of 10⁵ KV450 galaxies and their union | samples of n(z) per bin [src: arXiv:2605.15078, Sect. 2.1, 3, 4.2] |

The stated reasons. pop-cosmos minimises an OT distance because the
likelihood (and so the KL divergence) is intractable, while OT estimation
is asymptotically equivalent to maximum likelihood in most settings and
exactly so for score-matching of diffusion models; fitting population
and data-model parameters jointly lets the data "self-calibrate" zero
points and noise rather than fixing them beforehand [src:
arXiv:2402.00935, Sect. IV, IV.2]. GalSBI uses ABC because it is
conservative: SBI with learned high-dimensional posteriors from few
samples can exclude feasible regions early and become overconfident;
random tiles across the footprint limit the cosmic-variance risk of the
iterative scheme [src: arXiv:2412.08701, Sect. 2.4]. Kyriacou et al.
sample the individual (t, z, m) as well as f_ijk, unlike the
marginalised Gibbs scheme of Leistedt et al. 2016, because lensing needs
the redshifts of the galaxies actually in the sample, not the population
they were drawn from; they argue the difference (source clustering) is
negligible at KV450 volumes [src: arXiv:2605.15078, Sect. 2].

### Step 6. Turn the fit into n(z) and an uncertainty
<!-- key: step-6-turn-the-fit-into-n-z-and-an-uncertainty -->

- **Draw to match the data.** pop-cosmos on KiDS picks 200 random DR4
  tiles and, for each real KiDS-1000 object, draws mock galaxies at that
  object's nine-band depth until one passes the selection model [src:
  arXiv:2602.03935, Sect. IV.2].
- **Separate model and sample variance.** GalSBI runs 30 COSMOS-field
  simulations with a fixed population draw and rotated halo catalogues
  (sample variance), and 30 with a fixed halo catalogue and population
  draws from the posterior (model uncertainty), and adds them,
  σ_total² = σ_sample² + σ_model² (arXiv:2606.23783, Eq. 17), checked
  against a suite varying both [src: App. E]. Only the model term shrinks
  with tighter population constraints; only the sample term shrinks with
  area [src: App. E].
- **Posterior samples.** The histogram model passes 5000 (subset) or
  20,000 (union) n(z) samples to the cosmology likelihood [src:
  arXiv:2605.15078, Sect. 4.2].
- **Point estimate.** The pop-cosmos fit has no statistical error bar; the
  authors propose bootstrapping or ensembles of fits and expect systematic
  errors, such as photometric calibration, to dominate [src:
  arXiv:2402.00935, Sect. IV.2]. The KiDS paper defers propagation of
  residual uncertainties and a cosmology run to later work [src:
  arXiv:2602.03935, Sect. IV.2, V].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Which population model
<!-- key: which-population-model -->

- **Same data model, two populations.** With the KiDS data model, shark
  (semi-analytic) galaxies reproduce the SKiLLS truth to < 0.005 in every
  bin mean, which validates the data model; replacing shark by pop-cosmos
  moves the mean redshift of the first (0.1 < z < 0.3) and last
  (0.9 < z < 1.2) bins by Δz ~ 0.05–0.1 [src: arXiv:2602.03935, abstract,
  Sect. IV.1]. The mechanism given: at high redshift pop-cosmos galaxies
  span broader and redder r − i and i − Z colours, and its colour–redshift
  relation has ridges from Hα, [O III] and Hβ crossing the bands; BPZ then
  sends more intermediate-z objects to the top bin and scatters some
  high-z ones down [src: Sect. IV.1]. shark matches luminosity functions
  and masses but was not validated on colour evolution at 0.5 ≲ z ≲ 2,
  and reproduces the z > 0.4 colour bimodality less well [src: Sect. V].
  The authors read the shift as the sensitivity of forward-modelled n(z)
  to the population calibration [src: Sect. V].
- **Literature defaults are not enough at depth.** Fixed defaults gave
  biases of 0.003 and 0.001 on GAMA (r < 19.65) [src: arXiv:2207.05819,
  Sect. IV.3]; the SPS-based GalSBI-SPS with literature parameters,
  compared with COSMOS2020 template photo-z, has median offsets of 0.002
  to 0.007 at i ≤ 21 growing to ~0.1 at i ≤ 23, while its mean is pulled
  up by bright high-z objects passing the i cut [src: arXiv:2505.21610,
  Sect. 5.2]. Quote medians and means separately for such models.
- **Where the uncertainty sits.** Alsing et al. expect the dust prior to
  carry the largest population-model uncertainty, metallicity next, the
  star-forming sequence and mass function to be better constrained; they
  recommend wider priors on the first two [src: arXiv:2207.05819,
  Sect. VI].

### Error floors or explicit bias terms
<!-- key: error-floors-or-explicit-bias-terms -->

Error floors absorb modelling and calibration errors for single-galaxy
fits, but inflating variances to cover biases over-disperses the
population-level parameters; the authors recommend modelling biases
(rest-frame-wavelength SED errors, emission-line errors, skewness and
tails of the noise) explicitly [src: arXiv:2207.05819, Sect. VI].
pop-cosmos follows this with free zero points and emission-line
corrections and an added emission-line uncertainty σ_EM in quadrature
[src: arXiv:2402.00935, Sect. IV, steps 3–5].

### Catalogue-level or image-level simulation
<!-- key: catalogue-level-or-image-level-simulation -->

Catalogue-level data models (pop-cosmos on KiDS) are fast (~10⁶ galaxies
per GPU-hour) [src: arXiv:2602.03935, Sect. III.1] but inherit the image
simulation they were learned from: SKiLLS uses a single-image
approximation for VIKING, Gaussian noise in the optical, and
polynomial or Moffat PSFs [src: Sect. V]. pop-cosmos has no morphology;
tests with KiDS-like cuts on HSC shape catalogues changed only the tails
of the colour distributions (work in preparation, as reported) [src:
Sect. V]. Image-level models (GalSBI) carry morphology and blending
through the real source extractor at the cost of an emulator and
iterative ABC [src: arXiv:2412.08701, Sect. 2.3–2.4].

### ABC distance
<!-- key: abc-distance -->

On HSC deep fields, replacing MMD by the k-nearest-neighbour universal
divergence worsened all diagnostics except sizes, because that estimator
can go negative in high dimensions; Wasserstein distances improved sizes
and the full redshift distribution but lost sensitivity to the mean
redshift of bright samples; the fiducial combines a magnitude-weighted
Wasserstein-1 with count and mean-redshift terms,
δ = 0.1 d_frac,23 + 0.1 d_frac,25 + 0.1 d_μz,23 + 0.1 d_μz,25 + 0.6 W₁,w
(Eq. 26), where d_frac is the fractional count difference (Eq. 14) and
d_μz the mean-redshift difference against LePhare and EAZY photo-z (Eq. 15),
at i < 23 and 25 [src: arXiv:2412.08701, Sect. 2.4.1, 4.2.5, 4.3]. Both
photo-z codes enter the distance because their bright-sample means differ
by almost 1σ, to avoid overfitting either [src: Sect. 2.4.1].

### Histogram hierarchical model or stacking
<!-- key: histogram-hierarchical-model-or-stacking -->

On simulations drawn from the full ~300-template set (so the 50-template
analysis set is misspecified) with 5% uniform-redshift outliers, the
hierarchical model recovers bin medians to 0.001–0.005 against
0.004–0.014 for the stacked likelihood, and variances far better (stacked
error 0.213 in the first bin); mean χ² over five bins is 18 against 102,
with both worst in the fifth bin (34 and 308) [src: arXiv:2605.15078,
Sect. 3, Table 1]. Template-set size: three sets of 50 random templates
give widely varying KV450 medians, sets of 100 are stable, and the
50-template PCA-grouped set agrees with them [src: Sect. 4.2]. Subsets
of 10⁵ galaxies move S8 by ~0.01 [src: Sect. 4.2]. On KV450 the BHM n(z)
has a weaker high-z tail than the reweighting (DIR) and clustering (CC)
estimates, which is what raises σ8; no positive CC signal falls where the
BHM n(z) vanishes, except in the last bin, where magnification may
contribute [src: Sect. 4.3].

### Adding clustering to the hierarchy
<!-- key: adding-clustering-to-the-hierarchy -->

In a Cox-process model, galaxies are Poisson draws from
n f_tz 𝓑_z(δ̃_z(θ)) p(s | t, θ) (arXiv:1910.07127, Eq. 2), with f_tz = p(z, t)
over SOM phenotypes t and a biasing function of a kernel density estimate
of the tracer field, log₁₀ 𝓑_z = Σ_{k=0}^{4} b_k^z log₁₀(1.1 + δ̂_z)^k
(Eq. 17), constrained to be monotonic [src: Sect. 2.1, 4.2]. The
phenotype likelihood p(F, s | t, θ) is assumed known, e.g. from injection
[src: Sect. 2.1]. On 1000 deg² of N-body mocks, priors from a ~3.5 deg²
spectroscopic field with biases above 0.05 still give the mean to about
3 × 10⁻³ and always a lower KL divergence than photometry alone [src:
Sect. 7]. Limits they list: 0.2 < z < 1.2 only, an idealised tracer
spanning the range, the noise likelihood taken from the full simulation
rather than from limited injections [src: Sect. 7].

### Summing individual posteriors under a learned prior
<!-- key: summing-individual-posteriors-under-a-learned -->

With nine broad bands and many sources near the limit, per-galaxy
posteriors under the pop-cosmos prior stay broad and sometimes
multimodal, and summing them would still need the selection function; the
authors prefer propagating the prior through the data model [src:
arXiv:2602.03935, Sect. V].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Error floor, Student-t ν | β = 0.03 all bands; ν = 2 | GAMA, VVDS | arXiv:2207.05819 | Sect. III.3 |
| Uncertainty-model MDN | 12 components, 1 × 256 hidden units | GAMA, VVDS | arXiv:2207.05819 | Sect. III.4 |
| GAMA validation set-up | r < 19.65, J − K_s > 0.025; 5 × 10⁵ mock objects; bias 0.003, 0.001 | GAMA | arXiv:2207.05819 | Sect. IV.3 |
| pop-cosmos training sample | 140,938 at r < 25 (2024); ~420,000 at IRAC Ch. 1 < 26 (KiDS run) | COSMOS2020 | arXiv:2402.00935; arXiv:2602.03935 | Sect. II; Sect. III.1 |
| Diffusion-model size | 37,264 weights | pop-cosmos | arXiv:2402.00935 | Sect. IV |
| Zero-point initialisation | 12,473 spectra, 0 < z < 2 | pop-cosmos | arXiv:2402.00935 | Sect. IV.1 |
| SPS emulator error | < 3% over 99.9%, < 1% over 99% of parameter space | Speculator for KiDS bands | arXiv:2602.03935 | Sect. III.1 |
| Data-model check | shark + data model vs SKiLLS: all bin means < 0.005 | KiDS-1000 | arXiv:2602.03935 | Sect. IV.1 |
| Population-model shift | Δz ~ 0.05–0.1, first and last bins | KiDS-1000 | arXiv:2602.03935 | Sect. IV.1 |
| Selection emulator | accuracy ~63%, AUC ≃ 0.90, precision ~0.44, recall ~0.46 | KiDS-1000 | arXiv:2602.03935 | Sect. III.4 |
| Bin counts mock vs data | differ by ~5–10%; shapes robust | KiDS-1000 | arXiv:2602.03935 | Sect. IV.4 |
| GalSBI ABC | 10⁴ samples, keep 2000, 20-component GMM, 10 → 30 tiles, 31 iterations, 53 parameters | HSC PDR3 deep | arXiv:2412.08701 | Sect. 2.4, 4.3 |
| GalSBI mean z vs LePhare | 0.596 ± 0.006 vs 0.618 (i < 23); 1.143 ± 0.013 vs 1.110 (i < 25); 0.3–1.5σ | COSMOS validation | arXiv:2412.08701 | Table 4 |
| Model vs sample variance | i < 23: ±0.005 (model), ±0.012 (sample); i < 25: ±0.026, ±0.022 | GalSBI with clustering, COSMOS | arXiv:2606.23783 | Sect. 4.2.2, Eq. 15 |
| COSMOS field offset | ~0.015 in mean z at i ~ 23 relative to other deep fields (as cited) | GalSBI-SPS | arXiv:2505.21610 | Sect. 5.2 |
| BHM vs stacking, bin medians | 0.001–0.005 vs 0.004–0.014; mean χ² 18 vs 102 | KV450-like simulation | arXiv:2605.15078 | Table 1, Sect. 3 |
| Template set for stability | ≥ 100 random, or 50 PCA-grouped (5 × 10) | KV450 | arXiv:2605.15078 | Sect. 2.2, 4.2 |
| Hierarchical colours + clustering | mean to ~3 × 10⁻³ with prior biases > 0.05 | 1000 deg² N-body mock | arXiv:1910.07127 | Sect. 7 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Population model mis-specified.** Shows up as bin-mean shifts that a
  data-model validation cannot see (shark vs pop-cosmos) [src:
  arXiv:2602.03935, Sect. IV.1]. Test: rerun with a second population
  model through the same data model; compare noiseless colour–redshift
  relations with per-galaxy SED fits of the real sample [src: Sect. IV.1,
  IV.3].
- **Extrapolation below the training depth.** A model fitted at a flux
  limit should not be applied more than a few noise σ fainter; use it only
  for surveys of similar or shallower depth [src: arXiv:2402.00935,
  Sect. IV.2]. Test: completeness of the training selection at the
  target limit (96% for r < 25 under Ch. 1 < 26) [src: arXiv:2602.03935,
  Sect. III.1].
- **Data model inherits the image simulation.** Noise approximations and
  PSF models of the simulation propagate silently [src: arXiv:2602.03935,
  Sect. V]. Test: push a known population (the simulation's own input)
  through the learned data model and recover the simulation's bin means
  (< 0.005 for SKiLLS) [src: Sect. IV.1].
- **Binning pipeline not reproduced.** An unreproducible photo-z
  configuration changes which galaxies the mock places in each bin [src:
  arXiv:2602.03935, Sect. III.3]. Test: per-object comparison of mock and
  catalogue Z_B on the same inputs (median and 95th percentile).
- **Selection emulated imperfectly.** Depth variations and classifier
  training data change bin counts by 5–10% [src: arXiv:2602.03935,
  Sect. IV.4]. Test: train the classifier on simulation and data in turn,
  compare counts and shapes.
- **No clustering in the simulation.** n(z) comes out too smooth and the
  quoted error omits sample variance [src: arXiv:2412.08701, Sect. 4.3;
  arXiv:2505.21610, Sect. 5.2]. Fix: halo-based positions and the two
  30-realisation suites of arXiv:2606.23783, App. E.
- **Validation against an uncertain truth.** COSMOS2020 LePhare and EAZY
  disagree by up to 0.8σ on bright means; the forward-model discrepancy
  is largest exactly where the two codes disagree and sample variance
  dominates [src: arXiv:2606.23783, Sect. 4.2.2]. Report agreement with
  both codes and with their sample-variance errors (Table 4 of
  arXiv:2412.08701 does this).
- **Overconfident SBI posteriors.** Learned posteriors from few
  simulations can exclude feasible regions [src: arXiv:2412.08701,
  Sect. 2.4]. Test: check the density estimate at each ABC iteration;
  coverage tests as asked by the review (L2).
- **Template incompleteness.** The KV450 template set does not cover the
  survey colours well in the infrared; a wider set is needed for
  high-precision use [src: arXiv:2605.15078, Sect. 4.2, App. C as
  summarised there]. Test: template stability (random 50 vs 100 vs
  grouped sets).
- **Median and mean disagree.** Bright high-z tails move the mean by
  0.05–0.08 while medians agree to < 0.01 in GalSBI-SPS at i ≤ 21–22
  [src: arXiv:2505.21610, Sect. 5.2]. State which statistic is compared.

Validation as performed: bootstrap KDE of the mean-redshift difference
against spectroscopic histograms (arXiv:2207.05819, Fig. 8 caption) [src];
σ-agreement with two photo-z codes including COSMOS sample variance
(arXiv:2412.08701, Table 4) [src]; data-space comparisons and QQ/PP plots
of the simulation-based fit, described in a companion paper
(arXiv:2402.00935, Sect. IV.2) [src]; consistency with clustering
redshifts where the hierarchical n(z) vanishes (arXiv:2605.15078,
Sect. 4.3) [src]. None of these papers states a numerical pass criterion
beyond comparison with the Stage-III and LSST requirements
(arXiv:2207.05819, Sect. IV.3) [src].

## Reading list
<!-- key: reading-list -->

- Foundation: Alsing et al. 2023, arXiv:2207.05819 — the generative
  chain, Eq. 3 for n_k(z), the selection term, the data-model argument
  against error floors.
- Method: Alsing et al. 2024, arXiv:2402.00935 — fitting a diffusion
  population model and data model by optimal transport; point estimate
  only.
- Application: Leistedt et al. 2026, arXiv:2602.03935 — pop-cosmos on
  KiDS-1000: learned data model, selection and weight emulators, shark
  comparison.
- Method: Fischbacher et al. 2024, arXiv:2412.08701 — image-level
  phenomenological model with iterative ABC; distance-measure tests.
- Application: Fischbacher et al. 2026, arXiv:2606.23783 — adds
  clustering; separates model and sample variance.
- Critique/test: Tortorelli et al. 2025, arXiv:2505.21610 — what an
  SPS population with literature parameters gets wrong before fitting.
- Method/application: Kyriacou et al. 2026, arXiv:2605.15078 — histogram
  hierarchical model on KV450; template-set prior; comparison with
  stacking.
- Method: Alarcon et al. 2020, arXiv:1910.07127 — hierarchical colours
  plus clustering; robustness to biased spectroscopic priors.
- Review: Tortorelli & Grün 2026, arXiv:2605.06790, Sect. 3 — the risks
  and the checks a forward model should pass (summarised in L2).

## Not verified
<!-- key: not-verified -->

- The Thorp et al. pop-cosmos updates (the IRAC-selected model used for
  KiDS) and the companion validation paper with QQ/PP plots: cited in
  arXiv:2602.03935 and arXiv:2402.00935, not read; no identifier recorded.
- Leistedt et al. 2016 (arXiv:1602.05960) and Sánchez & Bernstein 2019
  (arXiv:1807.11873): bodies not read here; their schemes are described
  only as Kyriacou et al. and Alarcon et al. summarise them.
- The GalSBI predecessor whose reweighted mocks give the LePhare and EAZY
  errors (Moser et al. 2024, as named in arXiv:2606.23783), the shark
  model papers and the HSC morphology test (Tudorache et al., in
  preparation): not read.
- Appendix A of arXiv:2207.05819 (image-based selection) was read only
  through its summary in Sect. VI.
- Whether a KiDS cosmology analysis with the pop-cosmos n(z) has
  appeared since arXiv:2602.03935 was not checked.
