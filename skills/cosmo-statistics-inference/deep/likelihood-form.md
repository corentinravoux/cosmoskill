# Likelihood form — cosmo-statistics-inference dossier

Scope: how to test on mocks whether a Gaussian likelihood is adequate for a given data vector
(one-point, pairwise and multivariate diagnostics, their calibration and pass criteria), how a
non-Gaussian likelihood is built from mocks when it is not (Edgeworth, Gaussian mixture,
independent components, density ratio, learned likelihood) and propagated to parameters, and what
each comparison found on the same data; the exact Wishart and Hamimeche–Lewis forms, the
parameter-dependent-covariance rule and the list of documented cases are in the reference files.
Snapshot: 2026-10-19.
From: KiDS-1000 methodology (Joachimi et al. 2021), Sect. 6.2; Herold et al. 2024, Sect. III.1.

Prerequisites at L2: the table of departures from the Gaussian form, the Hamimeche–Lewis likelihood
and the rules of judgment in `physics-and-methods.md#likelihoods-and-when-the-gaussian-approximation`;
documented sizes in `results.md#non-gaussian-likelihood-and-parameter-dependent`; the failure mode
and its mitigations in `systematics.md#non-gaussian-likelihood-treated-as-gaussian`; the t-distribution
from a noisy covariance in `physics-and-methods.md#sample-covariance-from-mocks-and-its-corrections`
and `deep/covariance-estimation.md`; learned likelihoods in
`physics-and-methods.md#simulation-based-inference` and
`cosmo-beyond-two-point/deep/simulation-based-inference.md`. The low-ℓ CMB likelihoods are in
`cosmo-cmb`. Equation numbers are those of the paper cited next to them.

Symbols. `X_n` the `n`-th of `N_s` mock data vectors, `X^(i)` its `i`-th element; `x = d − t` data
minus theory; `λ` the precision matrix; `y = P x` the whitened ("uncorrelated basis") vector with
identity covariance; `S_3` the reduced skewness; `k_3,ijk` the third-order cumulant tensor; `N_k` the
number of independent Fourier modes in a shell; FoM the figure of merit `1/sqrt(det Φ̂)` with `Φ̂`
the parameter covariance (Euclid Collaboration 2026, arXiv:2604.01309, Eq. 30).

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Know where non-Gaussianity is expected before testing
<!-- key: step-1-know-where-non-gaussianity-is-expected -->

- **Few modes.** For the power spectrum of a Gaussian field the skewness of each band is
  `S_3,G = 2/sqrt(N_k)`, with `N_k = V_k k̃_F^-3 / 2` and `V_k = 4π k² k̃_F` the shell volume; for
  non-periodic geometries `2.2/sqrt(N_k)` "provides a better fit" and is the reference adopted
  (arXiv:2604.01309) [src: Sect. 3.2]. Skewness rises on large scales as the volume falls, through
  the `k̃_F^-2 = V^-2/3` scaling of `N_k` [src: Sect. 3.2].
- **Mask mixing on small scales.** An excess of skewness on small scales grows as the volume falls;
  it is "due to the mixing of modes caused by the presence of a mask", and the integral constraint is
  "partly responsible" [src: arXiv:2604.01309, Sect. 3.2]. In the correlation function the skewness
  peaks near `r ≈ 5 Mpc/h`, at `S_3 ≈ 0.1` for a 1 (Gpc/h)³ box and 0.7 for the smallest geometry
  tested [src: same].
- **Low signal-to-noise elements.** In BOSS DR12 power-spectrum multipoles, cutting the largest
  scales (`k_min = 0.05`) reduces the measured non-Gaussianity, cutting small scales (`k_max = 0.1`)
  increases it, and among the multipoles "the hexadecapole contributes most"; both are attributed to
  "low signal-to-noise and failure to satisfy the Central Limit Theorem" (Hahn et al. 2019,
  arXiv:1803.06348) [src: Sect. III].
- **Counts-like statistics.** The group multiplicity function likelihood is "likely Poisson — not
  Gaussian" [src: arXiv:1803.06348, Sect. III].
- **Shot noise suppresses it.** Euclid-like galaxy mocks show no detectable excess skewness at high
  `k` because their density is much lower than that of the dark-matter mocks, and shot noise
  "attenuates the skewness on small scales" [src: arXiv:2604.01309, Sect. 6]. Dark-matter mocks
  therefore overstate the problem for a sparse tracer.
- **Survey area.** For shear correlation functions the skewness and `(mode − mean)/σ` "decrease
  with the survey area as `f_sky^-1/2`" (Lin et al. 2020, arXiv:1905.03779) [src: Sect. 6].

### Step 2. One-point test of each element, in the right basis
<!-- key: step-2-one-point-test-of-each-element-in-the -->

1. Estimate the reduced skewness of each element over the mocks [src: arXiv:2604.01309, Eqs. 15–17]:
   `Ŝ_3^i = N_s^-1 Σ_n [X_n^(i) − X̄_i]³ / σ̂_i³`.
2. Compare with the Gaussian-field expectation (Step 1), not with zero.
3. Repeat in the whitened basis `y = P x` in which the covariance is the identity [src: Eq. 23].
   This basis is the one that enters the likelihood, and it changes the picture: off-diagonal
   cumulants that are large in the original basis "are reduced to a level compatible with the noise
   in the estimator", fluctuating around zero with standard deviation 0.01 [src: Sect. 4]; some
   elements keep a significant one-point skewness [src: same]. Lin et al. 2020 find likewise that the
   PCA rotation "reduces the level of skewness and kurtosis in the principal components
   significantly" [src: Sect. 6].
4. Lin et al. test each principal component with two-sample Kolmogorov–Smirnov tests in 10-fold
   cross-validation: 932 realisations split into 10 subsets, the model built on 9, 90 realisations
   drawn from it and compared with the held-out tenth; `p < 0.05` taken as rejection [src: Sect. 4].
5. For a compressed data vector, test the compressed summaries, not only the raw bins. Vinciguerra
   et al. 2026 (arXiv:2607.17942) standardise each compressed bin over 20 400 realisations at the
   fiducial cosmology and apply a one-sample KS test against `N(0, 1)`, passing at 5% when
   `D_N < 1.36/sqrt(N_real)`; then compare the distribution of `χ²_i` of the realisations with χ²
   for the number of summaries [src: Sect. 5.2]. MOPED summaries pass or fail mildly (KS 0.004 and
   0.050 against a critical 0.010); neural-network summaries fail clearly (0.067 and 0.081), which
   "also reflects the properties of the non-linear compression" [src: Sect. 5.2].

### Step 3. Pairwise and multivariate tests, calibrated on Gaussian copies
<!-- key: step-3-pairwise-and-multivariate-tests -->

**Pairwise, element by element** (Sellentin & Heavens 2018, arXiv:1707.04488) [src: Sect. 2.1]:

1. For each pair `(e, f)`, whiten with the 2 × 2 sub-covariance (Cholesky), chosen so that a detected
   coupling "refers to" identified data points rather than to principal components.
2. Histogram the sum `s = x^e + x^f` over the `N_s` mocks and compare with its Gaussian expectation
   `G(0, 2)` by the mean integrated squared error [src: Eq. 7]:
   `S⁺_e,f = (1/B) Σ_b [H_b(s^e,f) − G(0, 2)]²`; repeat for the product and the ratio [src: Eqs.
   9–12].
3. Sum each column to a total contamination `ε_e^tot = Σ_{f≠e} S_e,f` [src: Eq. 8].
4. Why MISE: the Kullback–Leibler divergence was found "overly sensitive to the tails of the
   distribution for our purposes", and the L1 norm performs similarly to MISE [src: Sect. 2.1].
5. Calibration before testing: draw `N_s` truly Gaussian data sets with the same covariance, 10 or 20
   such runs per setup, choose the number of histogram bins that minimises shot-noise structures,
   then leave the pipeline untouched and run the real mocks; show the calibration matrices next to
   the tested ones [src: Sect. 2.2].

**Multivariate divergence from the Gaussian pseudo-likelihood** (Hahn et al. 2019) [src: Sect. III]:

1. Draw a reference sample `Y_ref` from the Gaussian with the mock mean and covariance, of size
   comparable to the mocks (2000 and 10 000 in their two analyses).
2. Estimate the Rényi-α or Kullback–Leibler divergence between mocks and reference with
   `k`-nearest-neighbour estimators [src: Eq. 10], with `k = 10`; results "not significantly
   impacted" for `5 < k < 20`.
3. Compute the same estimator between two Gaussian samples (`X_ref` against `Y_ref`) as the null, and
   resample `Y_ref` 100 times for both. The shift `ΔD̂` between the two distributions measures the
   non-Gaussianity [src: Sect. III, Fig. 1].

**Two-sample distances with hold-out** (Lin et al. 2020): maximum mean discrepancy with a Gaussian
kernel, bandwidth by the median heuristic `h² = median(‖X_i − X_j‖²)` [src: Eq. 23 and footnote], and
the energy distance [src: Eq. 22], both invariant under orthogonal transformations such as PCA
[src: Sect. 4].

Pass criterion. None of these papers states a numerical threshold on the diagnostic itself. The
operational criterion is downstream: the parameter shift or the change of the figure of merit when a
non-Gaussian likelihood replaces the Gaussian one (Steps 5–6).

### Step 4. If the test fails, build a non-Gaussian likelihood from the mocks
<!-- key: step-4-if-the-test-fails-build-a-non-gaussian -->

| Model | Form | Built from | Where it worked | Source |
|---|---|---|---|---|
| Edgeworth, one-point only ("scenario 1") | `−2 ln L = χ² − 2 ln(1 + H_1pt)` in the whitened basis | diagonal skewness `⟨y_i³⟩_c` | Euclid-like P(k) and ξ(r); adopted as sufficient | arXiv:2604.01309, Eqs. 19–27 |
| Edgeworth, full tensor ("scenario 2") | adds two- and three-point cumulants, Eq. 28 | `⟨y_i² y_j⟩_c`, `⟨y_i y_j y_k⟩_c` | rejected: "injects noise without improving accuracy" | arXiv:2604.01309, abstract, Sect. 5 |
| Edgeworth per principal component | Petrov expansion with `κ_3`, `κ_4` [Eq. 15] | cumulants of each PC | 100 deg² shear | arXiv:1905.03779, Sect. 3.5 |
| Gaussian mixture | `Σ_i π_i N(x; θ_i)` [Eq. 12], EM initialised by k-means++, number of components by minimum BIC [Eq. 13] among `k < 30` | whitened mocks | group multiplicity function | arXiv:1803.06348, Sect. IV.1 |
| Independent components + 1D kernel densities | `p(x) = Π_n p_n(x^IC_n)` [Eq. 14], FastICA on whitened mocks, Gaussian kernel with Scott's bandwidth [Eq. 19] | whitened mocks | BOSS `P_ℓ`, 37 dimensions, 2048 mocks | arXiv:1803.06348, Sect. IV.2 |
| Density ratio to the Gaussian | `β(x) = f(x)/g(x)` by `k`-NN kernel or spectral series [Eq. 19], sampled by importance weighting | mocks | 100 deg² shear; no better than Edgeworth on hold-out | arXiv:1905.03779, Sects. 3.5, 6 |
| Learned likelihood (neural density estimator) | ensemble of flows; or Gaussian-only mixture density networks to isolate the cosmology-dependent covariance | forward simulations at many cosmologies | KiDS-1000 pseudo-C_ℓ, 18 000 realisations | arXiv:2404.15402, Sect. 8 |

Reasons stated for the choices. The Gaussian mixture "fails to accurately estimate the 37-dimensional
`P_ℓ` likelihood"; independent components reduce the problem to "37 one dimensional distributions
with 2048 samples each" [src: arXiv:1803.06348, Sect. IV.2]. PCA components are not used for this
because, for a non-Gaussian likelihood, they are "uncorrelated but not necessarily statistically
independent" [src: same]. The full Edgeworth tensor was dropped because its off-diagonal terms are
noise at 10 000 mocks; three random tensors of the same noise level shifted the contours "in different
directions", as a noisy covariance does, so "any potential systematic shift is, at most, comparable in
size to those caused by noise" [src: arXiv:2604.01309, Sect. 5, Fig. 9].

Practical checks on the Edgeworth form: it is "not positive definite" and can exceed unity in
amplitude, so check that the likelihood never turns negative on the sampled region
[src: arXiv:2604.01309, Sect. 4; arXiv:1905.03779, Sect. 3.5]. With the covariance fixed, drop the
Gaussian normalisation and transform `x → y` inside the sampler before evaluating
[src: arXiv:2604.01309, Sect. 5].

### Step 5. Propagate to parameters
<!-- key: step-5-propagate-to-parameters -->

- Rerun the chains with the new likelihood when the model is cheap (Euclid: MontePython 3.3.0,
  covariance from 9999 of the 10 000 mocks, data vector from the remaining one, two redshifts fitted
  jointly, BBN prior on `ω_b`) [src: arXiv:2604.01309, Sect. 5, Table 2].
- When the forward model is expensive, importance-reweight the existing Gaussian-likelihood chain by
  `P'(x|θ)/P(x|θ)`, the ratio of the non-Gaussian to the Gaussian likelihood at each sample
  [src: arXiv:1803.06348, Sect. V, Eqs. 20–21]. Hahn et al. did this for an HOD forward model that
  would have needed ~10^6 evaluations to resample [src: same].
- To separate "non-Gaussian at fixed cosmology" from "covariance that varies with cosmology", run
  three analyses on one mock: standard Gaussian with a fixed covariance, a learned likelihood forced
  to be Gaussian but with cosmology-dependent covariance, and the full learned likelihood
  (arXiv:2404.15402) [src: Sect. 8].

### Step 6. Judge the outcome
<!-- key: step-6-judge-the-outcome -->

Report the shift of each parameter in units of its σ, the change of width, and the FoM ratio, across
the analysis variations that drive non-Gaussianity (volume, geometry, scale cut, statistic). Euclid
checks four geometries, `k_max` from 0.1 to 0.35 h/Mpc, Fourier and configuration space, with and
without the BBN prior [src: arXiv:2604.01309, Sect. 5, Figs. 10–11], and then repeats the skewness
measurement on survey-like galaxy mocks (10 000 COVMOS clones of 1000 Euclid Large Mocks,
`0.9 < z < 1.1`, real and redshift space) [src: Sect. 6].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

- **Pairwise MISE against multivariate divergence.** Pairwise tests locate the offending data points
  and can drive cuts (CFHTLenS); they miss couplings of three or more elements. `k`-NN divergences are
  one number for the whole vector, need a resampled null, and do not say which elements fail.
  Two-sample distances with hold-out (MMD, energy distance) also score candidate likelihood models
  against held-out mocks, which neither of the others does.
- **Edgeworth against non-parametric.** Edgeworth needs only cumulants and stays cheap in the sampler,
  but is accurate only for weak non-Gaussianity and can go negative. Non-parametric estimators make no
  independence assumption but, in 100 deg² shear with 932 realisations, "their performance in terms
  of predicting hold-out data does not exceed that of the Edgeworth model"; the authors expect them to
  need "orders of magnitude" more realisations [src: arXiv:1905.03779, Sect. 6].
- **Cutting non-Gaussian data points against modelling them.** On CFHTLenS (210 points), dropping the
  24 points that make the stripes in the pairwise matrix (11%) moves `s_8 = sqrt(Ω_m) σ_8` towards
  Planck; dropping the 23 points with `ε^tot,+ ≥ 1.8` (10%) changes nothing; dropping the 43 with
  `ε^tot,+ ≥ 1.6` (20%) moves it away; widths change "only insignificantly" (arXiv:1707.04488)
  [src: Sect. 4]. "There is no natural cut on the non-Gaussianity", since all points deviate
  [src: same]. A cut chosen by its effect on the result is an analysis choice in the look-elsewhere
  sense (L2, `systematics.md#look-elsewhere-effect-and-a-posteriori`).
- **Fixed-covariance Gaussian against learned likelihood.** On a noiseless KiDS-1000 mock the learned
  likelihood gives `S_8 = 0.743 (+0.034/−0.031)` and the standard Gaussian `0.733 (+0.034/−0.024)`;
  the Gaussian-only learned likelihood agrees with the full one, so the difference comes from the
  cosmology dependence of the covariance, not from non-Gaussianity at fixed cosmology, and the
  Gaussian assumption "for ℓ > 76 holds well" (arXiv:2404.15402) [src: Sect. 8]. The standard
  analysis used a covariance from 1600 realisations at the fiducial cosmology [src: same].

Head-to-head results, same data, Gaussian against non-Gaussian likelihood.

| Data | Non-Gaussian likelihood | Result | Source |
|---|---|---|---|
| BOSS DR12 `P_ℓ`, 37 elements, 2048 Patchy mocks | ICA + KDE, importance-reweighted | `fσ_8`: 0.478 (+0.053/−0.049) → 0.456 (+0.059/−0.049), −0.44σ; `b_2^SGC σ_8` broadens from (+1.262/−1.175) to (+1.517/−1.377); `α_∥`, `α_⊥` "nearly no change" | arXiv:1803.06348, Sect. V |
| Dark-matter P(k) and ξ(r), four geometries, 10 000 COVMOS mocks | Edgeworth, one-point | FoM change never above 5%, no trend with volume or `k_max` up to 0.35 h/Mpc | arXiv:2604.01309, Sect. 5 |
| Euclid-like Hα galaxy mocks | skewness only | no detectable excess at high `k`; Gaussian likelihood "robust" for Euclid two-point analyses | arXiv:2604.01309, Sect. 6, abstract |
| LSST-like shear ξ±, 100 deg², 932 realisations | Edgeworth per PC; `k`-NN and spectral-series density ratios | "no significant biases" on Ω_m, σ_8 | arXiv:1905.03779, Sect. 6 |
| KiDS-1000 pseudo-C_ℓ, 18 000 forward simulations | flow ensemble against Gaussian MDN | Gaussian at fixed cosmology for ℓ > 76; standard analysis narrower in S_8 | arXiv:2404.15402, Sect. 8 |
| Planck-like tSZ power spectrum, halo-based Compton-y maps | neural posterior and likelihood estimators | for ℓ < 1000 the Gaussian likelihood gives unbiased cosmology; mild broadening of residual-foreground amplitudes | Xu et al. 2026, arXiv:2606.14622, abstract |

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Skewness of a P(k) band, Gaussian field | `2/sqrt(N_k)` periodic; `2.2/sqrt(N_k)` non-periodic | Euclid preparation | arXiv:2604.01309 | Sect. 3.2 |
| Mocks for the Euclid test | 10 000 COVMOS, 1 (Gpc/h)³, 2 × 10^7 particles, `n = 0.02 (Mpc/h)^-3`, z = 0 and 0.5 | Euclid preparation | arXiv:2604.01309 | Sect. 2.1 |
| Scale ranges tested | ξ: 20–124 Mpc/h (105 bins); P: `k_max` 0.1–0.35 h/Mpc (15–55 bins) | Euclid preparation | arXiv:2604.01309 | Sect. 5 |
| Noise of off-diagonal cumulants in the whitened basis, 10 000 mocks | σ ≈ 0.01 | Euclid preparation | arXiv:2604.01309 | Sects. 4–5 |
| FoM change, Gaussian against Edgeworth | < 5% | Euclid preparation | arXiv:2604.01309 | Sect. 5 |
| Galaxy-mock set for the realism check | 1000 ELM cloned to 10 000, `0.9 < z < 1.1` | Euclid preparation | arXiv:2604.01309 | Sect. 6 |
| Nearest neighbours in the divergence estimator | `k = 10`, stable for 5–20 | BOSS DR12, HOD | arXiv:1803.06348 | Sect. III |
| Null resamplings of the divergence | 100 | BOSS DR12, HOD | arXiv:1803.06348 | Sect. III |
| GMM search | `k < 30` components, minimum BIC | BOSS DR12, HOD | arXiv:1803.06348 | Sect. IV.1 |
| Gaussian calibration runs for pairwise tests | 10 or 20 per setup | CFHTLenS | arXiv:1707.04488 | Sect. 2.2 |
| Non-Gaussian contamination of CFHTLenS | "a 30% level" by their definition | CFHTLenS | arXiv:1707.04488 | Sect. 4 |
| Hold-out scheme for likelihood models | 10-fold over 932 realisations, 90 draws per sample, KS `p < 0.05` | LSST-like shear | arXiv:1905.03779 | Sect. 4 |
| KS pass threshold for a standardised compressed bin at 5% | `D_N < 1.36/sqrt(N_real)` (0.010 for 20 400 realisations) | Euclid-like shear mocks | arXiv:2607.17942 | Sect. 5.2 |
| Multipole above which the shear pseudo-C_ℓ likelihood is Gaussian at fixed cosmology | ℓ > 76 (earlier studies: ℓ > 50, as cited there) | KiDS-1000 SBI | arXiv:2404.15402 | Sect. 8 |
| Multipole range with an unbiased Gaussian tSZ likelihood | ℓ < 1000 | Planck-like tSZ | arXiv:2606.14622 | abstract |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Testing in the wrong basis.** Strong couplings in the original basis largely vanish after
  whitening (arXiv:2604.01309) [src: Sect. 4]; a failed test in the original basis is not yet a failed
  likelihood. Test: repeat in the basis `y = P x` that the likelihood uses.
- **Shot noise of the diagnostic mistaken for signal.** Histogram-based tests show "tartan-like"
  structures even for Gaussian data (arXiv:1707.04488) [src: Sect. 2.2]. Test: calibration runs on
  Gaussian copies with the same covariance, frozen before the real test.
- **Noisy higher-order cumulants.** Estimating the full skewness tensor from a finite mock set
  injects noise that moves and shrinks contours, like a noisy covariance (arXiv:2604.01309)
  [src: Sect. 5]. Test: replace the off-diagonal tensor by random draws at the measured noise level;
  if the contours move as much, keep the diagonal only.
- **A Gaussian mixture in too many dimensions.** It failed at 37 dimensions with 2048 mocks
  (arXiv:1803.06348) [src: Sect. IV.2]. Test: the divergence of the fitted model from the mocks must
  fall to the null level of Step 3 [src: Sect. IV.1].
- **An Edgeworth likelihood that turns negative.** Check over the sampled region
  (arXiv:2604.01309, Sect. 4; arXiv:1905.03779, Sect. 3.5) [src].
- **Dark-matter mocks used to judge a sparse tracer.** They overstate small-scale skewness
  (arXiv:2604.01309) [src: Sect. 6]. Test: repeat on mocks with the survey's density and selection.
- **Cuts on non-Gaussian points chosen after seeing the parameters.** CFHTLenS shows that different
  cuts move `s_8` in either direction (arXiv:1707.04488) [src: Sect. 4]. Fix the cut on the diagnostic
  before looking at parameters, or model the likelihood instead.
- **A covariance effect read as non-Gaussianity, or the reverse.** The width difference in KiDS-SBI
  comes from the cosmology dependence of the covariance (arXiv:2404.15402) [src: Sect. 8]; inside a
  Gaussian likelihood a parameter-dependent covariance is not allowed (L2, Carron 2013), so the two
  questions need the three-way comparison of Step 5.
- **Mocks shared between the covariance, the test and the data.** Euclid takes the data vector from a
  mock excluded from the covariance (arXiv:2604.01309) [src: Sect. 5]; Lin et al. score models on
  held-out folds (arXiv:1905.03779) [src: Sect. 4].

## Reading list
<!-- key: reading-list -->

- Foundation: Hamimeche & Lewis 2008, arXiv:0801.0554 — exact and approximate C_ℓ likelihoods (L2).
- Method: Sellentin & Heavens 2018, arXiv:1707.04488 — pairwise whitened sum, product and ratio tests
  with Gaussian calibration runs; consequences of cutting non-Gaussian points (Sects. 2, 4).
- Method: Hahn et al. 2019, arXiv:1803.06348 — divergence estimators against a Gaussian null; GMM and
  ICA likelihoods; importance reweighting of existing chains (Sects. III–V).
- Method: Lin et al. 2020, arXiv:1905.03779 — PCA, Edgeworth and non-parametric likelihood models
  scored by cross-validated two-sample tests (Sects. 3.4–4).
- Application: Euclid Collaboration (Gouyou Beauchamps et al.) 2026, arXiv:2604.01309 — Edgeworth
  likelihood in the whitened basis, one-point against full tensor, FoM across geometries and scale
  cuts, check on survey-like galaxy mocks (Sects. 3–6).
- Application: von Wietersheim-Kramsta et al. 2024, arXiv:2404.15402 — three-way comparison that
  separates non-Gaussianity from cosmology-dependent covariance (Sect. 8).
- Application: Xu et al. 2026, arXiv:2606.14622 — learned likelihood as a validation tool for a
  Planck-like tSZ power spectrum.
- Critique of the opposite assumption: Carron 2013, arXiv:1204.4724 — why a parameter-dependent
  covariance cannot sit inside a Gaussian likelihood (L2).

## Not verified
<!-- key: not-verified -->

- The companion paper of arXiv:2604.01309 (cited there as B-2025) with the derivation of `S_3,G` and
  the penta-spectrum dependence was not read.
- The numerical values of the BOSS and group-multiplicity divergences (Fig. 1 of arXiv:1803.06348)
  and the per-component KS outcomes of arXiv:1905.03779 were not read; only the stated conclusions.
- The body of arXiv:2606.14622 (simulation design, ℓ range of the failure, size of the broadening) was
  not read.
- Copula and Box–Cox (Gaussianising) likelihoods for two-point data were not researched.
- The Hamimeche–Lewis or pixel-based treatment in the Planck PR4 and ACT DR6 likelihoods is left to
  `cosmo-cmb`.
