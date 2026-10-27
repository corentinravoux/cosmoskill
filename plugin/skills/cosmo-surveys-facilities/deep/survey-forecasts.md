# Survey forecasts — cosmo-surveys-facilities dossier

Scope: how the reach of a planned survey is forecast (Fisher matrix for a
galaxy survey, the BAO-only Seo–Eisenstein recipe, CMB noise curves,
figure-of-merit computation, code validation, sampling-based forecasts),
which settings move the answer, and how far past forecasts missed the
delivered errors.
Snapshot: 2026-10-17.
From: Euclid overview (arXiv:2405.13491), Sect. 8 (science performance
verification, expected constraints); Flaugher et al. 2022 Snowmass report
(arXiv:2209.08654), Sects. 3.3 and 5; Simons Observatory science goals and
forecasts (arXiv:1808.07445).

Already in L2, not repeated here: the FKP weight, the integral form of
V_eff and the n̄P ≈ 1 rule in
`physics-and-methods.md#number-density-np-and-effective-volume`; rules for
comparing figures of merit and the Euclid figure-of-merit forecast in
`physics-and-methods.md#dark-energy-task-force-stages-and-the-figure-of`;
the Knox band-power error and current CMB map depths in
`physics-and-methods.md#cmb-sensitivity-map-depth-resolution-and-sky`; the
SO 2018 baseline and goal noise per band in
`surveys-and-data.md#cmb-experiments`.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Specify the survey as forecast inputs
<!-- key: step-1-specify-the-survey-as-forecast-inputs -->

A galaxy-survey forecast needs, per redshift bin, the volume V_s, the
number density n(z), the bias and the redshift error; Euclid converts the
expected counts per unit area and redshift to
n(z) = (dN/dΩdz)(A_survey/V_s) Δz (Euclid Collaboration: Blanchard et al.
2020, arXiv:1910.09273, Eq. 88) [src: Sect. 3.2.4]. The DESI Survey
Validation forecasts list, per Δz = 0.1 bin, the surface density, n̄P at
k = 0.14 h Mpc⁻¹ and μ = 0.6, and V_eff, and use the densest tracer where
several overlap "to keep our forecasts conservative" [src:
arXiv:2306.06307, Sect. VI.1, Table 7].

A CMB forecast needs white-noise levels per band computed from detector
noise-equivalent temperatures, yield and effective observing time, and a
large-scale noise model N_ℓ = N_red (ℓ/ℓ_knee)^α_knee + N_white (Simons
Observatory 2018, arXiv:1808.07445, Eq. 1), where N_red, ℓ_knee and
α_knee describe atmospheric and electronic 1/f noise [src: Sect. II.2].
SO assumed a five-year survey with 20% of the time usable for science,
"consistent with the realized performance after accounting for data
quality cuts" of Polarbear and ACT, and raised LAT noise to mimic
discarding 15% of the map at the edges [src]. Polarisation noise is √2
times the temperature value [src: Table 1 note].

### Step 2. Build the Fisher matrix
<!-- key: step-2-build-the-fisher-matrix -->

For the observed galaxy power spectrum P_obs(k, μ; z_i) in bin i,

F_αβ^bin(z_i) = (1/8π²) ∫ dμ ∫ k² dk [∂ ln P_obs/∂α][∂ ln P_obs/∂β] V_eff(z_i; k, μ)
(arXiv:1910.09273, Eq. 91, following Tegmark 1997 and Seo & Eisenstein
2003), with the Gaussian covariance
C(k, k′) ≈ 2(2π)³ P_obs² δ_D(k − k′)/V_eff (Eq. 89) and
V_eff = V_s [nP_obs/(nP_obs + 1)]² (Eq. 90) [src: Sects. 3.2.4–3.2.5].
Bins are summed (Eq. 92); redshift-dependent parameters (ln D_A, ln H,
ln fσ8, ln bσ8, shot noise P_s per bin) are independent between bins, so
the full matrix has a block structure of dimension 6 + 5 N_z in the
non-linear case (Eqs. 93–98) [src]. Tegmark's paper introduced the "handy
approximation" for galaxy surveys and stressed that "pinpointing
attainable accuracies to within better than a factor of a few depends
crucially on whether it will be possible to extract useful information
from the mildly nonlinear regime" (arXiv:astro-ph/9706198) [src].

For weak lensing, the per-multipole weight is
𝓕_jk(ℓ) = f_sky (2ℓ + 1)/(2[C_jk(ℓ) + N_jk(ℓ)]²), with shape noise
N_jk = σ²δ_jk/N_g,j and σ = 0.3 per component, and
F_αβ = Σ 𝓕_jk ∂C_jk/∂α ∂C_jk/∂β (Paykari et al. 2020,
arXiv:1910.10521, Eqs. 18–19) [src: Sect. 2.5].

### Step 3. Isolate the BAO if a robust distance forecast is wanted
<!-- key: step-3-isolate-the-bao-if-a-robust-distance -->

Seo & Eisenstein 2007 (arXiv:astro-ph/0701079) keep only the acoustic
information [src: Sect. II]:

- Non-linear damping of the BAO by Lagrangian displacements:
  P_b,nl = P_b,lin exp(−k⊥²Σ⊥²/2 − k∥²Σ∥²/2) (arXiv:astro-ph/0701079,
  Eqs. 3–4), with
  Σ⊥ = Σ0 G and Σ∥ = Σ0 G(1 + f), Σ0 = 12.4 h⁻¹ Mpc for σ8 = 0.9 and
  scaling with σ8; G is the growth function normalised to 0.758 at z = 0
  and f = dlnG/dlna.
- The damping is placed outside the derivatives, equivalent to
  marginalising over Σ⊥ and Σ∥, so no distance information comes from the
  damping itself; broadband shape information is removed by subtracting a
  Fisher matrix computed with Ω_b = 0.005; the Alcock–Paczynski
  information from the assumed redshift-space distortion is removed by
  setting β ≈ 0 in the derivatives [src: arXiv:astro-ph/0701079, Sect. II].
  Reason stated: both
  AP and broadband information are "less robust than the BAO" because
  quasilinear redshift distortions and broadband systematics (tilt,
  non-linear bias, non-linear growth) are not understood well enough [src].
- The fitting formula (Eq. 25) gives the Fisher matrix for
  p₁ = ln s⊥⁻¹ and p₂ = ln s∥ (equivalent to D_A/s and sH) as
  V_survey A0² ∫₀¹ dμ f_i f_j ∫ dk k² exp[−2(kΣ_s)^1.4]
  / (P(k)/P_0.2 + 1/(nP_0.2 R(μ)))² × exp[−k²(1−μ²)Σ⊥² − k²μ²Σ∥²],
  with f₁ = μ² − 1, f₂ = μ² (Eqs. 20–21), R(μ) = (1 + βμ²)², P_0.2 the
  power at k = 0.2 h Mpc⁻¹, Σ_s = 1/k_silk the Silk scale, and
  A0 = 0.4529 (WMAP1) or 0.5817 (WMAP3) [src: arXiv:astro-ph/0701079,
  Sect. IV]. A 20-point μ grid
  and 50 k points to 0.5 h Mpc⁻¹ converge [src].
- Photometric redshift errors or fingers of God enter by
  R(k, μ) = (1 + βμ²)² exp(−k²μ²Σ_z²) (Eq. 27), acting like extra shot
  noise; putting peculiar-velocity smearing into Σ∥ instead is more
  conservative [src: Sect. IV.1].

Reconstruction in forecasts: Font-Ribera et al. 2014 use this code with
"50% reconstruction", multiplying Σ⊥ = 9.4 (σ8(z)/0.9) h⁻¹ Mpc and
Σ∥ = (1 + f)Σ⊥ by 0.5, degraded at low density by a multiplier r(x)
interpolated over r = (1.0, 0.9, 0.8, 0.70, 0.6, 0.55, 0.52, 0.5) at
x = n̄P(k = 0.14, μ = 0.6)/0.1734 = (0.2, 0.3, 0.5, 1.0, 2.0, 3.0, 6.0,
10.0) [src: arXiv:1308.4164, Sect. IV.1.1]. Several tracers in one volume
are combined mode by mode, (n̄P)_combined = Σ n̄_i P_i [src]. The D_A/s and
Hs errors of galaxies and quasars have a correlation coefficient close to
0.4 [src].

### Step 4. Choose the scale cuts and non-linear nuisance treatment
<!-- key: step-4-choose-the-scale-cuts-and-non-linear -->

Euclid's validated recipe defines four settings for spectroscopic
clustering [src: arXiv:1910.09273, Sect. 4.2.2]:

| Setting | k_max [h Mpc⁻¹] | Non-linear model | σ_p, σ_v |
|---|---|---|---|
| Linear | 0.25 | none | 0 |
| Pessimistic | 0.25 | full non-linear recipe | free |
| Intermediate | 0.30 | full | free |
| Optimistic | 0.30 | full | fixed at reference values |

Here σ_p and σ_v are the fingers-of-God and BAO-damping velocity
dispersions. The authors note that k_max = 0.25 may itself be optimistic
"depending on ones confidence in modelling of the non-linear power
spectrum", the one-halo term being a 30% correction at that scale [src:
arXiv:1910.09273, Sect. 4.2.2, "Pessimistic setting"].

### Step 5. Project to cosmological parameters and add priors
<!-- key: step-5-project-to-cosmological-parameters-and -->

Parameters are projected by a Jacobian to the final set (for example
Ω_b, h, Ω_m, n_s, Ω_DE, σ8 for non-flat ΛCDM) [src: arXiv:1910.09273,
Sect. 4.2.2]. External data must be stated: DESI's FoM forecast adds only
Planck temperature and polarisation, varying the Planck likelihood nuisance
parameters, with w0, wa and curvature free [src: arXiv:2306.06307,
Sect. VI.2]. SO adds Planck at 2 ≤ ℓ ≤ 29 over 80% of the sky and at
30 ≤ ℓ ≤ 2500 over a further 20%, a τ = 0.06 ± 0.01 prior, DESI BAO as
r_s/D_V priors and LSST samples over f_sky = 0.4 [src: arXiv:1808.07445,
Sect. II.6].

### Step 6. Compute the figure of merit
<!-- key: step-6-compute-the-figure-of-merit -->

FoM_w0wa = √det F̃_w0wa (arXiv:1910.09273, Eq. 49), with F̃ the
marginalised 2 × 2 Fisher sub-matrix; it is inversely proportional to the
area of the 2σ contour and, the authors say, equivalent within a constant
factor to other definitions in use [src: Sect. 3.1.2]. Contour axes use
A² = 2.3, 6.18, 11.8 for 1σ, 2σ, 3σ two-parameter regions (Eq. 47) [src:
Sect. 3.1.1]. The same construction gives a FoM for any parameter pair,
for example (γ, Ω_m) [src].

### Step 7. Validate numerically and against sampling
<!-- key: step-7-validate-numerically-and-against-sampling -->

- **Numerical precision.** For ≤ 10% error on σ and FoM and ≤ 2% on
  contour orientation, Fisher elements and their inversion need fractional
  precision of about 10⁻⁴, set by δσ/σ ≈ δ_max/(1 − r) with r ≤ 0.999
  (Eq. 65) [src: arXiv:1910.09273, Sect. 3.1.6]. Three-point derivatives
  err as ε², five-point as ε⁴ [src].
- **Code comparison.** Six clustering codes agreed to a few per cent in
  the intermediate setting and about 4% on the redshift-dependent
  parameters; all validated codes agree within the 10% requirement [src:
  arXiv:1910.09273, Sects. 4.2.3, 6].
- **Fisher against posterior sampling.** For purely geometric probes,
  Fisher forecasts underestimate marginalised errors by 30–70%, especially
  when wa is marginalised; for weak lensing the difference is about 5%
  (Wolz et al. 2012, arXiv:1205.3984) [src]. CLOE samples 58 to 61
  parameters and finds the full-probe FoM consistent with the 2020
  pessimistic Fisher setting despite a higher photometric ℓ_max, which it
  attributes to the larger sampled parameter space [src: arXiv:2510.09153,
  Sect. 6.4].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### BAO-only or full shape
<!-- key: bao-only-or-full-shape -->

Isolated BAO is "the most robust, but pessimistic" view, since BAO
survives large unknown systematics [src: arXiv:1308.4164, Sect. IV.1.1].
Broadband and RSD forecasts depend on an effective k_max: BOSS DR9 RSD
matched the projection only for k_max,eff ≈ 0.1 h Mpc⁻¹ although the fit
used scales equivalent to k_max ≈ 0.14, the difference attributed to
marginalising fingers-of-God parameters and non-Gaussian covariance [src:
Sect. IV.4.2]. In DESI's forecast the FoM is 97 from BAO alone and 156.8
with RSD, against a design FoM of 110 [src: arXiv:2306.06307, Table 8].

### Pessimistic or optimistic settings
<!-- key: pessimistic-or-optimistic-settings -->

Euclid's FoM for all probes combined, flat w0wa, is 377 (pessimistic) or
1257 (optimistic) [src: arXiv:1910.09273, Sect. 6]. Including the
photometric clustering–lensing cross-correlations raises the w0wa FoM by
about 3.6 (pessimistic) or 3.3 (optimistic) relative to treating the
probes as independent, with negligible effect in ΛCDM [src]. Single-probe
spectroscopic errors, flat w0wa: σ(w0) = 0.39 and σ(wa) = 1.4 pessimistic
against 0.15 and 0.45 optimistic [src: Table 11]. Quote the setting with
every forecast number.

### Fisher or sampling
<!-- key: fisher-or-sampling -->

Fisher is fast and validated for code comparison but fails for
non-elliptical posteriors [src: arXiv:1205.3984]. Sampling exposes
projection effects that Fisher cannot show: CLOE's ΛCDM 3×2pt posteriors
shift in σ8 and S8 through a degeneracy between Ω_b h² (under a BBN prior)
and the 26 per-bin redshift-shift nuisance parameters; the shift vanishes
when those parameters are fixed or the BBN prior is replaced by a flat one
[src: arXiv:2510.09153, Sect. 6.3.3]. The cost is computational; the
authors call for simulation-based inference or Hamiltonian Monte Carlo
[src: Sect. 7]. Their model-selection numbers assume data peaked exactly
on the fiducial model, so evidence differences are overstated for a real
noise realisation [src].

### Which tracer in overlapping bins
<!-- key: which-tracer-in-overlapping-bins -->

DESI's forecasts use the densest tracer in each bin, a conservative
choice [src: arXiv:2306.06307, Sect. VI.1]; Font-Ribera et al. sum n̄P over
tracers, the optimal multi-tracer combination [src: arXiv:1308.4164,
Sect. IV.1.1]. The two give different answers for the same survey.

### Area or overlap for a CMB survey
<!-- key: area-or-overlap-for-a-cmb-survey -->

SO compared LAT sky fractions of 10%, 20% and 40%: a small LAT area
maximises overlap with the SATs for delensing, but limiting the LAT area
had no significant effect on r, so the LAT covers about 40% to overlap
with LSST and DESI; the SATs cover an effective 10–20% set by field of
view, Galactic emission and elevation limits [src: arXiv:1808.07445,
Sect. II.3]. Large-scale B modes are forecast by end-to-end simulations
rather than Fisher matrices because foregrounds dominate there [src:
Sect. II.6].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Context | Source | Place read |
|---|---|---|---|---|
| Fisher numerical precision | ~10⁻⁴ for ≤ 10% on σ and FoM | Euclid IST | arXiv:1910.09273 | Sect. 3.1.6 |
| Inter-code agreement | few %; ~4% on z-dependent parameters; all < 10% | Euclid IST | arXiv:1910.09273 | Sects. 4.2.3, 6 |
| Euclid FoM, all probes, flat w0wa | 377 pessimistic, 1257 optimistic (**forecast**) | Euclid IST | arXiv:1910.09273 | Sect. 6 |
| Cross-correlation gain in FoM | ×3.6 pessimistic, ×3.3 optimistic | Euclid IST | arXiv:1910.09273 | Sect. 6 |
| Sampled forecast | FoM > 400 with 58–61 parameters (**forecast**) | Euclid CLOE | arXiv:2510.09153 | Sect. 6.4 |
| Fisher underestimate | 30–70% (geometric probes); ~5% (weak lensing) | DETF III/IV surveys | arXiv:1205.3984 | abstract |
| BAO damping scale | Σ0 = 12.4 h⁻¹ Mpc at σ8 = 0.9 | Seo–Eisenstein | arXiv:astro-ph/0701079 | Sect. II |
| Reconstruction in forecasts | Σ × 0.5 at high n̄P, none at x < 0.2 | DESI-era forecasts | arXiv:1308.4164 | Sect. IV.1.1 |
| DESI forecast R(z) | 0.24% (0 < z < 1.1), 0.37% (1.1–1.9), 0.46% (1.9–3.7); 0.18% total (**forecast**) | DESI SV | arXiv:2306.06307 | Table 8 |
| DESI FoM | 97 (BAO), 156.8 (BAO + RSD), design 110; SDSS 24 | DESI SV + Planck | arXiv:2306.06307 | Table 8 |
| SO survey efficiency assumed | 5 years, 20% usable; 15% LAT edge discarded | SO 2018 | arXiv:1808.07445 | Sect. II.2 |
| BOSS DR9 error / Fisher | 1.34 before, 1.57 after reconstruction (mocks) | BOSS CMASS | arXiv:1308.4164 | Sect. IV.4.1 |
| BOSS DR11 error / Fisher | ~1.27 pre and post reconstruction (mocks) | BOSS | arXiv:1308.4164 | Sect. IV.4.1 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Fisher too optimistic for BAO.** BOSS DR9 mock errors exceeded the
  Fisher projections by about 34% before and 57% after reconstruction;
  the measured data errors (1.7%) sat between [src: arXiv:1308.4164,
  Sect. IV.4.1]. Candidate causes discussed: spherical averaging (~7%),
  finite mocks (~3%), sub-optimal estimators, extra small-scale power, and
  the "significantly stripey" DR9 geometry; with the compact DR11
  footprint the excess fell to about 27%, pre and post reconstruction
  alike [src]. Test: compare forecast with the mock scatter of the actual
  footprint.
- **Projections built on the wrong survey.** Font-Ribera et al. used 70%
  of the sky for Planck at ℓ > 50 where the analysis used 58% (100 GHz)
  and 37% (143, 217 GHz); low-ℓ polarisation cleanliness, which sets τ,
  was the main remaining uncertainty [src: arXiv:1308.4164, Sect. III.1].
  A survey that changes after the forecast (`open-questions.md#cancelled-descoped-or-redefined-projects`)
  makes the forecast refer to something else.
- **Design values quoted as forecasts.** The DESI Survey Validation
  abstract gives 0.28% and 0.39% for z < 1.1 and 1.1 < z < 1.9, which
  Table 8 lists as design requirements; the forecast column there is
  0.24% and 0.37% [src: arXiv:2306.06307, abstract and Table 8].
- **Unstable derivatives.** Semi-analytic derivatives of P_obs with
  respect to ln H and ln D_A disagree with numerical ones above
  k = 0.1 h Mpc⁻¹ and depend on k binning; single-probe FoMs depend on the
  step, combined ones do not [src: arXiv:1910.09273, Sect. 4.5.1]. Test:
  scan the step; interpolate in log k and log P with cubic splines; use 50
  points per decade [src].
- **FoM compared across different external data.** DESI's design FoM of
  110 and its BAO-only forecast of 97 differ because the design used
  forecast Planck results and the forecast used final ones [src:
  arXiv:2306.06307, Sect. VI.2].
- **Marginal biases or errors hiding degeneracies.** See the CLOE
  projection effect above and the caveat on one-parameter biases in
  arXiv:1910.10521, Sect. 2.5.

## Reading list
<!-- key: reading-list -->

- Foundation: Tegmark 1997, arXiv:astro-ph/9706198 — Fisher information
  for galaxy surveys and the warning about the mildly non-linear regime.
- Method: Seo & Eisenstein 2007, arXiv:astro-ph/0701079 — BAO-only Fisher
  recipe with Lagrangian damping (Eqs. 1–4, 25, 27).
- Application and critique: Font-Ribera et al. 2014, arXiv:1308.4164 —
  multi-survey projections, reconstruction factor, projections against
  BOSS and Planck reality.
- Method: Euclid Collaboration: Blanchard et al. 2020, arXiv:1910.09273 —
  validated recipes, settings, numerical precision, FoM definition.
- Critique: Wolz et al. 2012, arXiv:1205.3984 — where Fisher fails against
  MCMC.
- Application: Euclid Collaboration 2025, arXiv:2510.09153 — sampled
  forecasts, projection effects, FoM > 400. [src: abstract]
- Application: DESI Collaboration 2023, arXiv:2306.06307, Sect. VI —
  per-bin forecast table and FoM against design.
- Application: Simons Observatory 2018, arXiv:1808.07445, Sect. II — CMB
  noise model, efficiency assumption, sky-fraction optimisation.

## Not verified
<!-- key: not-verified -->

- The DETF report body (arXiv:astro-ph/0609591 has no readable rendering
  or source here): stage definitions and the original FoM normalisation
  are taken through arXiv:1910.09273, Sect. 3.1.2 [sec].
- The DESI final-design forecasts (arXiv:1611.00036) and the DESI DR1 and
  DR2 errors set against the Survey Validation forecasts were not compared
  here; see `cosmo-galaxy-clustering` for delivered precisions.
- Seo & Eisenstein 2003 and Kitching et al. 2008, cited as sources of the
  formalism, were not read.
- The SO detector NETs and the companion instrument paper behind Table 1
  of arXiv:1808.07445.
