# Cosmic dipoles — cosmo-tensions-anomalies dossier

Scope: how a number-count dipole is turned into a significance against the
kinematic expectation — catalogue cuts, measurement of the count slope x and
spectral index α at the flux limit, the estimator or likelihood, the content
of the null mocks, the clustering dipole, joint fits across catalogues and
the redshift dipole — and how to choose between the variants that move the
same CatWISE dipole from about 3σ to about 7σ.
Snapshot: 2026-10-17.
From: CosmoVerse white paper (arXiv:2504.01669), Sect. 2.3.6; Abdalla et
al. 2022 review (arXiv:2203.06142), Sect. VIII.6.

Already in L2, not repeated here: the Ellis–Baldwin amplitude and the
assumptions of the test in `physics-and-methods.md#cosmic-dipole`; every
published amplitude and significance in
`results.md#number-count-dipoles-against-the-kinematic`; the redshift and
aberration velocities in
`results.md#measurements-that-agree-with-the-cmb-velocity`; the mundane
explanations with verdicts in `systematics.md#cosmic-dipole`; the dispute
in `open-questions.md#the-number-count-dipole-above-5sigma-or-about`.
Tension metrics in general belong to `cosmo-statistics-inference`
(`deep/tension-metrics.md`); bulk flows to `cosmo-peculiar-velocities`.

Notation. D (vector **D**, or **d**) is the fractional dipole of the counts,
N(n̂) = N̄(1 + **D**·n̂); β = v/c the observer velocity; D_kin =
[2 + x(1 + α)]β the Ellis–Baldwin expectation, with S_ν ∝ ν^(−α) and integral
counts dN/dΩ(>S_ν) ∝ S_ν^(−x) (arXiv:2009.14826, Eq. 1). C_ℓ is the angular
power of the count map; f_sky the unmasked sky fraction.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Build a flux-limited, homogeneous catalogue
<!-- key: step-1-build-a-flux-limited-homogeneous -->

The CatWISE quasar sample of 2021 [src: arXiv:2009.14826, Sect. II]:

- Selection W1 − W2 ≥ 0.8 (AGN-dominated, power-law emission), W1 and W2
  corrected for Galactic extinction with the Planck dust map "to avoid any
  potential directional bias from uncorrected Galactic reddening" [src: arXiv:2009.14826, Sect. II].
- Magnitude window 9 < W1 < 16.4 (Vega): fainter than 16.4, "uneven source
  density appears due to overlaps in the ecliptic scanning pattern of WISE";
  the bright bound guards against saturation. Equivalent flux window 77.77 >
  S_ν > 0.09 mJy [src: arXiv:2009.14826, Sect. II].
- Masks: |b| < 30° (density drops below that latitude), 291 further regions
  (nebulae, Magellanic Clouds and M31 at six times their 2MASS isophotal
  radii, bright stars with log₁₀(r/deg) = −0.134 K − 0.471), and 57 objects
  with coverage depth w1cov < 80. Final sample 1,355,352 quasars [src: arXiv:2009.14826, Sect. II].
- A residual linear trend of density with absolute ecliptic latitude (slope
  −0.051, intercept 68.89 deg⁻²) is fitted and used "as a correction and
  weighting function" [src: arXiv:2009.14826, Sect. II].
- Redshifts from a Stripe 82 subsample matched to SDSS spectra: mean z = 1.2,
  99% at z > 0.1, used to argue that local clustering is small [src: arXiv:2009.14826, Sect. II].

The 2022 version of the sample, used by most later work, cuts at W1 < 16.5
(0.078 mJy) and keeps 1,567,586 sources after masking [src:
arXiv:2503.02470, Sect. 3.3, Table 1]; its mask removes 52.6% of the sky,
f_sky ≈ 0.474 [src: arXiv:2511.00822, Sect. II].

Radio catalogues, as homogenised for the 2025 joint fit [src:
arXiv:2503.02470, Sects. 3.1–3.4]: NVSS (1.4 GHz, north of −40°) and
RACS-low (887.5 MHz, south of +30°), both cut at 15 mJy; |b| < 7° masked;
0.3° around sources brighter than 2.5 Jy masked; sources matched to 2MRS
galaxies at z < 0.02 removed (4681 NVSS, 4314 RACS, 66 CatWISE) because an
earlier analysis found local structure adding to the amplitude; empty
HEALPix cells and their neighbours masked "to remove edge effects".

How to set the flux limit. The review by the discovering group warns that a
catalogue's quoted completeness may come from small deep patches: NVSS is
99% complete at 3.4 mJy by that measure, yet dipole studies find its uniform
limit at about 10–15 mJy [src: arXiv:2505.23526, Sect. III.4.1]. It also
warns against choosing the cut where the dipole direction converges to the
CMB direction, since there is "no reason why a dipole inconsistent in
amplitude with the kinematic prediction from the CMB should nevertheless
align with it" [src: same].

### Step 2. Measure x and α at the flux limit
<!-- key: step-2-measure-x-and-alpha-at-the-flux-limit -->

The kinematic modulation acts only on sources near the flux limit, so x and
α must be measured there: sources brighter than the narrow modulated range
"are counted once and only once", and the fractional flux shift across the
sky is bounded by ΔS/S < 2(1 + α)β, below 0.5% for α ≈ 1 (arXiv:2505.23526,
Sect. III.4.2, Eq. 41) [src]. For quasars, the mean mid-infrared SED of
sources at W1 ≈ 16.5 is close to a power law within the W1 band, because
the wide redshift range smears emission lines (same paper, Sect. III.4.3)
[src].

| Catalogue | Cut | x | α | D_kin for β = 1.23 × 10⁻³ (arXiv:2511.00822, Sect. V) | Place read |
|---|---|---|---|---|---|
| CatWISE 2021 | W1 < 16.4 | 1.7 (sample mean) | 1.26 (sample mean, from W1 − W2 via synthetic AB magnitudes) | 0.0072 | arXiv:2009.14826, Sect. II; arXiv:2212.07733, Sect. 2.2; arXiv:2511.00822, Sect. II |
| CatWISE 2022 | W1 < 16.5 (0.078 mJy) | 1.90 | 1.07 (mean below 0.08 mJy) | 0.73 × 10⁻² | arXiv:2503.02470, Sect. 3.3 |
| NVSS | 15 mJy | 0.74 | 0.75 (adopted; no spectral indices in NVSS) | 0.41 × 10⁻² | arXiv:2503.02470, Sect. 3.1 |
| RACS-low | 15 mJy | 0.72 | 0.88 (median from RACS–NVSS comparisons) | 0.41 × 10⁻² | arXiv:2503.02470, Sect. 3.2 |

The two CatWISE choices differ in both inputs yet give nearly the same
expectation (table). The 2025 paper
explains its lower α: "spectral indices are generally lower for sources with
lower flux densities" [src: arXiv:2503.02470, Sect. 3.3]. The neural
ratio analysis quotes D̃ = 4.31 × 10⁻³ (NVSS), 4.27 × 10⁻³ (RACS-low) and
7.25 × 10⁻³ (CatWISE) from an earlier paper of its group [src:
arXiv:2607.25703, Sect. 4.2].

Uncertainty of x and α. The joint fit treats them as fixed, not as nuisance
parameters, because they "would add a significant number of additional
nuisance parameters"; it accepts that this "can in principle lead to an
underestimation" of the dipole errors, expected to be small since they are
measured on the whole catalogue [src: arXiv:2503.02470, Sect. 3]. The
Bayesian CatWISE analysis bounds the effect of a spread in x and α: the
prefactor becomes Ā_k = A_k + ρ σ_x σ_α (arXiv:2212.07733, Eq. 25), with ρ
the x–α correlation; taking a maximum-entropy exponential p(x) with mean
1.7 and σ_α = 0.597 gives Ā_k ≤ 6.7 against A_k = 5.8, a correction of at
most 17% [src: Sect. 3.3].

### Step 3. Pixelise and estimate
<!-- key: step-3-pixelise-and-estimate -->

All recent analyses use HEALPix N_side = 64 (cells of 55′; about 57 CatWISE
sources per cell) [src: arXiv:2503.02470, Sect. 3.4; arXiv:2212.07733,
Sect. 2.2]. Four estimators are in use.

1. **Least squares.** Minimise Σ_p [n_p − (A_0 + Σ_j A_1j d_j,p)]² over
   unmasked pixels, d_j the three dipole templates; **D** = A_1/A_0
   (arXiv:2009.14826, Eq. 2; healpy `fit_dipole`). Chosen because the
   minimum is analytic, cheap enough for 10⁷ mocks, and "not prone to
   leakage into higher multipoles, as it does not force a spherical
   harmonic decomposition on an incomplete sky"; verified unbiased on the
   paper's simulations [src: Sect. III.1]. The same estimator, with
   optional pixel weights w_p = 1, is Eq. 7 of arXiv:2511.00822 [src].
2. **Poisson likelihood.** λ_i = Ω_pix f_ecl(n̂_i) N̄(1 + **d**·n̂_i), with
   f_ecl = 1 − Υ_ecl c_ecl |b_ecl| and c_ecl = 7.4 × 10⁻⁴ (arXiv:2212.07733,
   Eqs. 4–8); Υ_ecl = 1 recovers the 2021 correction, 0 none. At high
   occupancy its maximum-likelihood estimator equals the quadratic
   estimator; its advantage is uncertainty quantification without
   simulations and direct comparison with a theory prior [src: Sect. 2.2].
   For the 2022 sample c_ecl = 9.15 × 10⁻⁴ [src: arXiv:2607.25703, Eq. 15].
3. **Super-Poisson likelihoods.** The one-point distribution of CatWISE
   cell counts is overdispersed with respect to Poisson; the Gamma–Poisson
   (negative binomial) and the generalised Poisson likelihoods both fit it
   (arXiv:2510.23769, Fig. 1, Eqs. 24–25) [src: Sect. 3.3–3.4]. In radio
   catalogues the overdispersion comes from multi-component sources, and
   the negative-binomial estimator lowers RACS-low + NVSS from 4.8σ to 4.5σ
   (arXiv:2509.16732) [src: abstract].
4. **Joint multi-catalogue likelihood.** A product of Poisson likelihoods
   with a monopole per catalogue j and **d**_j = [2 + x_j(1 + α_j)]**β** +
   **d**_resid (arXiv:2503.02470, Eqs. 7–8): the different count slopes
   separate the kinematic part from a common residual [src: Sect. 2.2].

### Step 4. Build the null distribution
<!-- key: step-4-build-the-null-distribution -->

Three routes are in use, and they are the main source of the spread in
quoted significance.

**Shot-noise mocks (2021).** Isotropic source vectors aberrated for a boost
**v**; each source gets a flux and an α drawn from the empirical
distributions, its flux is boosted, the flux cut and the mask are applied,
and the sample is subsampled to the observed size. The p-value is the
fraction of mocks with amplitude larger than observed "and with angular
distance from the CMB dipole closer than our sample": 5 of 10⁷ [src:
arXiv:2009.14826, Sects. III.2, IV].

**Clustering-aware lognormal mocks (2025).** Five components added in pixel
space [src: arXiv:2511.00822, Sect. V, Eqs. 17–20]:

1. Kinematic: m_i = δ_i^(2+x(1+α)) N_0 with δ_i = (1 + β cos θ_i)/√(1 − β²),
   β = 1.23 × 10⁻³, x = 1.7, α = 1.26 [src: arXiv:2511.00822, Sect. V].
2. Shot noise: Poisson draw with mean m_i, keeping only ℓ ≤ 1.
3. Clustering at ℓ ≥ 2: FLASK lognormal fields in 35 shells over 0 < z < 3.5
   (Δz = 0.1), CLASS spectra, bias b(z) = 1.54 + 0.53z + 0.50z², n(z) ∝
   z^a₁ exp[−(z/a₂)^a₃] with a₁ = 0.86, a₂ = 1.48, a₃ = 2.36, Poisson
   sampled, with ℓ = 0, 1 removed; ℓ_max = 3N_side − 1, with ℓ_max ≈ 64
   found sufficient [src: arXiv:2511.00822, Sect. V].
4. Clustering dipole: amplitude 0.81 × 10⁻³ (C_1 = 0.91 × 10⁻⁶) from the
   same bias and n(z), varied with cosmic variance ΔC_1/C_1 = √(2/(3 f_sky))
   = 118.6% for f_sky = 0.474 (arXiv:2511.00822, Eq. 14).
5. Six sets: S0 (2021 assumptions), S1 (no clustering dipole), S2 (random
   direction), S3 (aligned with the CMB dipole), S4 and S5 (clustering
   dipole at its 2σ value 1.48 × 10⁻³, random or aligned) [src:
   arXiv:2511.00822, Sect. V].

Validation: the shot-noise-subtracted C_ℓ of the data lies within the 2σ
band of 1000 masked FLASK mocks for ℓ ≥ 5 (NaMaster) [src: arXiv:2511.00822, Fig. 4]. The
p-value counts mocks whose amplitude "match or exceed D^obs" — amplitude
only, unlike the 2021 criterion [src: Sect. VI]. The drop from S0 to S1
"can be attributed to the inclusion of stochastic clustering modes at
multipoles ℓ ≥ 2, with the dominant contribution arising from ℓ = 3": the
CatWISE mask couples odd multipoles into the dipole and biases it high,
while even multipoles only add scatter (1000 injection simulations with
10°, 30° and CatWISE masks) [src: Sects. IV.1, VI].

**Bayesian evidence or simulation-based evidence.** Model comparison
between fixed and free dipoles (arXiv:2212.07733, Table 1), or neural ratio
estimation of the evidence ratio R calibrated on matched and mismatched
simulations (arXiv:2607.25703, Sects. 2.3, 4.2). In the latter the mocks
are Poisson skies with expectation N̄(1 + D(v) cos θ), D(v) = D̃ v/v_CMB, the
ecliptic term for CatWISE, and priors v ~ 20 v_CMB U[0, 1], N̄ within ±10%,
Υ_ecl ∈ [−2, 2] [src: Sect. 4.2, Eqs. 15–16].

### Step 5. Bound the clustering dipole separately
<!-- key: step-5-bound-the-clustering-dipole-separately -->

The ΛCDM clustering dipole is D_cls = √(9 C_1/4π), C_ℓ = b² (2/π) ∫ f_ℓ(k)²
P(k) k² dk with f_ℓ(k) = ∫ j_ℓ(kr) f(r) dr and f(r) the normalised radial
distribution (arXiv:2009.14826, Eqs. A1–A4). Three evaluations for the same
catalogue:

| Evaluation | Value | Bias assumed | Place read |
|---|---|---|---|
| 2021, b = 1 | D_cls = 0.00024 | constant b = 1 | arXiv:2009.14826, App. A |
| 2025 mocks | D_clus = 0.81 × 10⁻³ | b(z) = 1.54 + 0.53z + 0.50z² | arXiv:2511.00822, Sect. V(d) |
| 2025 clustering fit | Ĉ_1^clus = (2.21 ± 1.81) × 10⁻⁶, 140 times below the observed Ĉ_1 = (3.10 ± 0.75) × 10⁻⁴; 1σ effect on the amplitude 4.84% | b_g ≈ 2.25 from the small-scale C_ℓ | arXiv:2510.23769, Sect. 5 |

Putting the last two rows on one scale: the 2025 mocks quote D_clus with
|D|² = 9C_1/4π (arXiv:2511.00822, Eq. 4; 0.91 × 10⁻⁶ gives 0.81 × 10⁻³).
Whether the two papers share the C_1 normalisation, and hence whether they
agree on the clustering dipole and differ only through the ℓ ≥ 2 power, is
not stated in either; the conversion that an earlier version of this file
made is set aside.

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Estimator: least squares or likelihood
<!-- key: estimator-least-squares-or-likelihood -->

- **Same mocks, both methods** (N̄ = 50 per pixel, N_side = 64, D = 0.007,
  Galactic cuts 0°–80°, polar caps, patchy surveys): `fit_dipole` is
  unbiased in its Cartesian components at all coverages, but the amplitude
  and angles derived from it are biased (amplitude high) when coverage is
  low, because the Cartesian-to-spherical transformation distorts its
  Gaussian distribution; variances should be computed in Cartesian
  components and propagated with a Jacobian. The Bayesian posterior instead
  widens towards zero amplitude, and the dipole-versus-monopole Bayes
  factor reaches ≈ 1 at a ±70° Galactic cut, which flags the result as
  inconclusive [src: Mittal, Oayda & Lewis 2025, arXiv:2509.20651, Sects.
  4.1, 5, 6].
- **Linear (vector-sum) estimator.** Biased on a masked sky; for NVSS it
  needs the −40° limit mirrored by a +40° cut, about 20% of the catalogue,
  and still a directional correction [src: arXiv:2505.23526, Sect.
  IV.2.2]. Not used for current claims.
- **Gaussian or Poisson noise.** A quadratic estimator is misspecified for
  Poisson counts; the bias becomes noticeable below about 600,000 sources
  (≲ 15 deg⁻²), slightly for NVSS, not for CatWISE [src: arXiv:2505.23526,
  Sect. IV.2.2].
- **Poisson or super-Poisson.** The Poisson model is "strongly deviant" from
  the CatWISE one-point distribution; both super-Poisson likelihoods fit it,
  and the dipole stays anomalous with either [src: arXiv:2510.23769, Sects.
  3.3, 6].

### Ecliptic-latitude correction: fixed, free, or forward-modelled
<!-- key: ecliptic-latitude-correction-fixed-free-or -->

- Fixed linear correction (2021), as a correction and weight [src:
  arXiv:2009.14826, Sect. II].
- Free amplitude Υ_ecl: the models with free ecliptic bias have a much
  higher ln Z than the same models without it (M8 against M4,
  arXiv:2212.07733, Table 1); leaving it out "yields an even higher dipole
  amplitude" [src: arXiv:2503.02470, Sect. 2.1, citing that paper].
- Forward model of Eddington bias (CatSIM): positions drawn uniformly,
  colours from the CatWISE W1–W2 distribution, aberration and boosting per
  source, photometric errors from the WISE coverage, then the colour and
  magnitude cuts; an extra error η_extra ∈ [0, 8] added in quadrature is
  needed to reproduce the depletion near the ecliptic poles, so the
  catalogue errors are underestimated or another selection effect acts
  [src: arXiv:2607.25703, Sect. 5.1]. Cost: 900,000 Poisson skies in 1.8
  minutes on 48 cores against about 140 hours for CatSIM, a factor of about
  4700 [src: Sect. 6]. Result (L2): ≈ 5.7σ → ≈ 6.7σ.

### Higher multipoles: fit them or simulate them
<!-- key: higher-multipoles-fit-them-or-simulate-them -->

The two 2025 analyses disagree here, on the same catalogue.

- **Simulate (lower significance).** ΛCDM clustering at ℓ ≥ 2 in the mocks
  lowers 4.82σ (S0) to 3.63σ (S1), mainly through ℓ = 3 leakage; fitting an
  octupole raises the fitted amplitude and the variance (condition number
  of the normal equations) [src: arXiv:2511.00822, Sect. VI, App. B]. The
  mocks are validated against the data only at ℓ ≥ 5 [src: Fig. 4].
- **Fit them (unchanged significance).** After the ecliptic trend, power at
  2 ≤ ℓ ≤ 4 is consistent with noise; a free octupole is 2.3σ, not a
  detection, and raises the dipole by almost 10% (D = 0.0163 +0.0027/−0.0024
  with or without a free quadrupole); evidence favours dipole + ecliptic
  models over any with an octupole; the authors advise against reading
  pseudo-C_ℓ of masked data at ℓ < 10 [src: arXiv:2510.23769, Sects.
  3.5.4, 5].

What a referee can ask: whether the mock ℓ = 2–4 power matches the
data's real-space multipole fits, since that power is what moves the
significance. Neither paper reports that comparison in the sections read.

### Clustering-dipole amplitude and direction
<!-- key: clustering-dipole-amplitude-and-direction -->

Random against aligned direction moves S2 → S3 from 3.44σ to 3.27σ; the 2σ
amplitude with alignment gives 2.93σ [src: arXiv:2511.00822, Table 1, Sect.
VI]. The aligned case is motivated by NVSS and RACS clustering dipoles that
appear aligned with the CMB dipole [src: Sect. V].

The bias model matters more than the direction: compare the constant-bias
and the evolving-bias clustering dipoles of the table above [der].

### Joint catalogues
<!-- key: joint-catalogues -->

- Hypothesis (i), common direction: β < 2.34 × 10⁻³ (95%), consistent with
  zero and with 1.23 × 10⁻³, but ln B = −3.0 favours the purely kinematic
  hypothesis (0), which needs β ≈ 2.6 × 10⁻³ [src: arXiv:2503.02470, Sect.
  4.2]. Hypothesis (iii), kinematic part fixed to the CMB: residual 39° ±
  8° from it, 4.6σ [src: same].
- Cost: the separation assumes one residual dipole common to all
  catalogues; a frequency-dependent residual breaks it [src: arXiv:2503.02470,
  Sect. 5.1].
  NVSS and RACS-low disagree in direction, which lowers their combined
  amplitude and hence β [src: Sect. 4.2]. Raising the cuts to 20 mJy and
  W1 < 16.4 raises both radio amplitudes [src: same].

### Local-source removal and redshift cuts
<!-- key: local-source-removal-and-redshift-cuts -->

Removing 2MRS sources at z < 0.02 lowers the NVSS amplitude from 1.39 to
1.20 (× 10⁻²) and RACS-low from 1.43 to 1.34 [src: arXiv:2503.02470, Table
1]. Redshift cuts change the expectation itself: of order 1% for z < 0.02,
10% for z < 0.1 in NVSS-like catalogues [src: Sect. 3.4, footnote].

### Velocity without counts: the redshift dipole
<!-- key: velocity-without-counts-the-redshift-dipole -->

Each tracer is split into narrow redshift shells (3000, 280, 240 and 390 for
BGS, LRG, ELG, QSO); in each shell the model is z′ = z_j − (1 + z_j) n̂·**β**,
the monopole z_j is re-estimated by de-Dopplering at each trial **β**, and
**β** minimises a χ² weighted by the DESI completeness, redshift-failure and
imaging weights; errors come from 1000 EZmocks [src: arXiv:2608.30914,
Sects. III.1–III.2, Eqs. 4–9]. The amplitude grows as (1 + z)β, and the
result rises with redshift: 118 (BGS), 263 (LRG), 220 (ELG), 358 km/s (QSO,
0.8 < z < 2.1), read by the authors as local structure dominating at low z
[src: Sect. IV.1]. It does not use x or α, so it tests the kinematic
reading independently of Step 2.

### The expectation formula itself
<!-- key: the-expectation-formula-itself -->

Beyond the 2022–2024 exchange held in L2, 2026 papers generalise D_kin: a
"functional" of the selection function acting on the population, of which
Ellis–Baldwin is a limit (Takeuchi 2026, arXiv:2602.07389); a
generalisation to arbitrary luminosity distributions and SEDs, after which
the CatWISE anomaly "persists" (Bonnefous 2026, arXiv:2602.05700); a new
WISE AGN selection with an adapted formalism, 2.5 times the kinematic
amplitude at 5.3σ (Lee et al. 2026, arXiv:2608.06458) [src: abstract of each].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Mocks exceeding the CatWISE dipole, 2021 criterion | 5 of 10⁷ | CatWISE 2021 | arXiv:2009.14826 | Sect. IV |
| Same, reproduced, amplitude-only criterion | 9 of 10⁷ (4.82σ) | Bashir et al. | arXiv:2511.00822 | Sect. VI |
| Mask-variation stability | amplitude ≲ 5%, direction ≲ 5° | CatWISE 2021 | arXiv:2009.14826 | Sect. IV |
| CatWISE f_sky | 0.474 | 2022 mask | arXiv:2511.00822 | Sect. II |
| Cosmic variance of C_1 at that f_sky | 118.6% | ΛCDM | arXiv:2511.00822 | Eq. 14 |
| ℓ_max needed in lognormal mocks | ≈ 64 | Bashir et al. | arXiv:2511.00822 | Sect. V |
| Max. correction from x–α correlation | ≤ 17% (A_k 5.8 → ≤ 6.7) | Dam et al. | arXiv:2212.07733 | Sect. 3.3 |
| Sources per N_side = 64 cell | ≈ 57 | CatWISE | arXiv:2212.07733 | Sect. 2.2 |
| Quadratic-estimator bias threshold | ≲ 600,000 sources (≲ 15 deg⁻²) | review | arXiv:2505.23526 | Sect. IV.2.2 |
| Bayes factor dipole vs monopole at ±70° cut | ≈ 1 | mocks, N̄ = 50 | arXiv:2509.20651 | Sect. 5 |
| CatSIM vs Poisson simulation cost | ≈ 4700 times | NRE | arXiv:2607.25703 | Sect. 6 |
| Clustering-dipole effect on amplitude | 4.84% (1σ) | CatWISE | arXiv:2510.23769 | Sect. 5 |
| Octupole with free ecliptic term | 0.0247 +0.0107/−0.0110 (2.3σ) | CatWISE | arXiv:2510.23769 | Eq. 36 |
| Joint-fit β bound | < 2.34 × 10⁻³ (95%) | NVSS + RACS + CatWISE | arXiv:2503.02470 | Sect. 4.2 |
| Redshift-dipole bins | 3000 / 280 / 240 / 390 | DESI DR1 BGS/LRG/ELG/QSO | arXiv:2608.30914 | Sect. III.2 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Null without large-scale power.** Shows up as a significance that falls
  when clustering is added (4.82σ → 3.63σ, 3.44σ or 3.27σ). Test: mocks whose ℓ ≥ 2
  power matches the data, checked at ℓ = 2–4 with real-space template fits,
  not only at ℓ ≥ 5 (arXiv:2511.00822 Fig. 4; arXiv:2510.23769 Sect. 5).
- **Mismatched p-value criteria.** Amplitude-and-direction (2021) against
  amplitude-only (2025) counts; state which one.
- **Spherical parameters from a Cartesian estimator.** Amplitude biased high
  at low coverage. Test: bias and covariance in Cartesian components
  (arXiv:2509.20651, Sect. 6).
- **Poisson likelihood on overdispersed counts.** Test: compare the
  one-point distribution of the residual map with Poisson, Gamma–Poisson
  and generalised Poisson (arXiv:2510.23769, Fig. 1).
- **x and α from the wrong flux range or sample version.** Test: measure
  them after the final cuts and near the limit; report which version of the
  catalogue (arXiv:2503.02470, Sect. 3).
- **Flux cut chosen by direction convergence.** Test: fix the cut from
  density-versus-systematic checks before looking at the dipole
  (arXiv:2505.23526, Sect. III.4.1).
- **Unmodelled scanning or depth pattern.** Test: free ecliptic amplitude
  and model comparison (arXiv:2212.07733), or a forward model of the
  photometric scatter (arXiv:2607.25703).
- **Joint fits that hide a disagreement.** NVSS and RACS-low directions
  differ; a common-dipole fit then lowers the amplitude. Test: fit each
  pair separately (arXiv:2503.02470, Sect. 4.2).
- **Counting analyses as catalogues.** Five CatWISE papers are one data
  set (`surveys-and-data.md#cosmic-dipole-catalogues`).

## Reading list
<!-- key: reading-list -->

- Foundation: Secrest et al. 2021, arXiv:2009.14826 — catalogue cuts,
  least-squares estimator, shot-noise mocks, clustering-dipole formula.
- Method: Dam, Lewis & Brewer 2023, arXiv:2212.07733 — Poisson likelihood,
  ecliptic nuisance, hypotheses, x–α correlation bound.
- Method: Wagenveld et al. 2025, arXiv:2503.02470 — x and α per catalogue,
  joint kinematic + residual fit, local-source removal.
- Critique: Bashir, Chingangbam & Appleby 2025, arXiv:2511.00822 — lognormal
  mocks with clustering; mask mode coupling.
- Reply: von Hausegger et al. 2025, arXiv:2510.23769 — super-Poisson
  likelihoods, multipole fits, clustering dipole from the C_ℓ fit.
- Method: Mittal, Oayda & Lewis 2025, arXiv:2509.20651 — estimator against
  Bayesian inference on the same mocks.
- Method: Land-Strykowski et al. 2026, arXiv:2607.25703 — simulation-based
  evidence, Eddington-bias forward model.
- Review: Secrest et al. 2025, arXiv:2505.23526 — practical rules for flux
  limits, x, α and estimators (one side of the dispute).
- Application: Wu & Xia 2026, arXiv:2608.30914 — tomographic redshift
  dipole.
- Theory: Takeuchi 2026, arXiv:2602.07389; Bonnefous 2026,
  arXiv:2602.05700 — generalised kinematic expectation.

## Not verified
<!-- key: not-verified -->

- The body of Böhme et al. 2025 (arXiv:2509.16732): no HTML rendering and
  the LaTeX source did not resolve; only the abstract numbers are used.
- The bias and redshift fits behind D_clus = 0.81 × 10⁻³ (arXiv:2511.00822
  [src: Sect. V], taken from "Tiwari et al.", one of its references), the 2025 RACS–CatWISE–NVSS tension paper
  ("L25") and the CatSIM paper ("OL26") of arXiv:2607.25703: not identified
  or read here.
- Whether α = 1.06, the index quoted in Fig. 1 of arXiv:2505.23526 for its
  reference sample, refers to the 2022 catalogue; it differs from both 1.26
  (2021) and 1.07 (2025).
- The Siewert et al. 2021 quadratic estimator and the Bashir et al.
  higher-multipole fits (App. B): conclusions read, equations not.
- The SKA forecasts of Bertacca et al. 2026 (arXiv:2610.17022): abstract
  only, no number taken.
