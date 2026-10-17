# Time-delay cosmography — cosmo-distance-ladder-h0 dossier

Scope: how a lensed-quasar or lensed-supernova H0 is produced (time-delay
measurement, lens-model families, line-of-sight convergence, stellar
kinematics and the population model for the internal mass sheet, external
lens samples), and how to choose between the assumptions that move the
result.
Snapshot: 2026-10-17.
From: Verde et al. 2023 review (arXiv:2311.13305), Sect. 4.1; Freedman &
Madore 2023 (arXiv:2309.05618), Sect. 8.3; TDCOSMO collaboration
(arXiv:2506.03023).

Already in L2, not repeated here: the time-delay and mass-sheet equations
and founding papers in `physics-and-methods.md#time-delay-cosmography`; the
headline values (H0LiCOW, TDCOSMO-IV, TDCOSMO-2025, single lenses, lensed
SNe) in `results.md#one-step-routes-independent-of-the-ladder-and`; the
kinematic biases of Forés-Toribio et al. and the TDCOSMO 2025 list of terms
outside the baseline in `systematics.md#time-delay-cosmography` and
`systematics.md#error-budgets-term-by-term`; the debate after Kochanek
(2020) and the forecasts in
`open-questions.md#time-delay-cosmography-after-the-mass-sheet`; the
samples in `surveys-and-data.md#lensing-time-delays`.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Measure the delays
<!-- key: step-1-measure-the-delays -->

Optical monitoring from 1 m and 2 m telescopes (COSMOGRAIL) over several
seasons is needed to separate quasar variability from microlensing by stars
in the deflector, which can mimic intrinsic features [src: arXiv:1907.04869,
Sect. 3.2]. Delays come from curve shifting: a function is fitted to each
image's light curve and the shifts that minimise their differences are
found; the PyCS package also estimates delay errors in the presence of
microlensing, and recovered delays to about 3% on average with negligible
bias on blind simulated light curves [src: same]. High-cadence,
high-signal-to-noise monitoring can separate microlensing from intrinsic
variability within one season by catching short intrinsic variations; this
was used for WFI2033−4723 and PG1115+080 and agrees with decade-long
light curves [src: same]. B1608+656 is a radio lens, timed with the VLA
over three seasons [src: same].

The current pipeline, as applied to SDSSJ1433+6007 [src: arXiv:2604.14145,
Sect. 4]: photometric calibration with `lightcurver`; STARRED forward-models
the quasar point sources and deblends the lens galaxy, fitting all epochs
at once with a pixelated background and epoch-specific PSFs from field
stars; PyCS3 aligns the light curves with free-knot splines for the
intrinsic signal and polynomials or splines for microlensing; errors and
covariances come from mock light curves with injected red noise. Light
curves from observatories with different filters are not merged but
combined at the likelihood level, which there improved the delay error by
a factor of about 1.5 on average [src: Sect. 4, Fig. 3].

The "microlensing time delay" (differential magnification of a
lamp-post-lit accretion disc reweighting delayed emission) is not detected
in the H0LiCOW data and does not enter its main result; it is quantified
for speculative models in the individual lens papers [src:
arXiv:1907.04869, Sect. 3.2].

### Step 2. Model the lens imaging
<!-- key: step-2-model-the-lens-imaging -->

Two codes were used in H0LiCOW: Glee, which reconstructs the source on a
regularised pixel grid, and Lenstronomy, which describes the source with a
parametric profile plus shapelets; the second was meant as a check on code
systematics [src: arXiv:1907.04869, Sect. 3.3]. Two mass families were
fitted to every lens after B1608+656 [src: Sect. 3.3; arXiv:1912.08027,
Sect. 6.4]:

| Family | Form | Where defined |
|---|---|---|
| Power law (PEMD) + external shear | κ(θ₁, θ₂) = (3 − γ_pl)/2 [θ_E / √(q_m θ₁² + θ₂²/q_m)]^(γ_pl − 1) | arXiv:2506.03023, Eq. 22 |
| Composite | NFW dark halo, ρ = ρ_s / [(r/r_s)(1 + r/r_s)²], plus a "Chameleon" baryonic profile (difference of two isothermal ellipsoids, close to Sérsic) | arXiv:1912.08027, Eq. 14, Sect. 2.3.2 |

Here κ is the convergence, γ_pl the logarithmic slope, q_m the axis ratio
and θ_E the Einstein radius. Significant line-of-sight perturbers enter
through the multi-plane lens equation; models varying the parametrisation,
source reconstruction and pixel weighting were combined, first with equal
weights, later weighted by the Bayesian Information Criterion [src:
arXiv:1907.04869, Sect. 3.3].

### Step 3. Estimate the external convergence κ_ext
<!-- key: step-3-estimate-the-external-convergence -->

Perturbers whose "flexion shift" is large are modelled explicitly; all
others are summarised by κ_ext [src: arXiv:1907.04869, Sect. 3.4].
κ_ext is estimated by weighted galaxy number counts within 120″ of the lens
(down to i ≈ 23–24), weighted by projected distance, stellar mass,
redshift or external shear, compared with control fields (CFHTLenS), then
mapped to κ by selecting Millennium-simulation lines of sight with the same
relative counts and ray-tracing them [src: same]. Weak-lensing estimates
for some systems agree with the number counts [src: same]. TDCOSMO 2025
adds a population layer: κ_ext follows a generalised extreme-value
distribution whose parameters are fitted on SL2S lenses, so that the
prior can depart from random Millennium lines of sight; the lens lines of
sight are found overdense, as expected for massive early-type galaxies
[src: arXiv:2506.03023, Sect. 7.2.3].

### Step 4. Add stellar kinematics
<!-- key: step-4-add-stellar-kinematics -->

The model velocity dispersion separates into a cosmological and a model
part [src: arXiv:2506.03023, Eq. 12]:

    σ_los² = (1 − κ_s)/(1 − κ_ds) · (D_s/D_ds) · c² J(ξ_lens, β_ani, λ_int)

with J a dimensionless function of the lens parameters ξ_lens, the
anisotropy β_ani and the seeing and aperture, κ_s and κ_ds the
line-of-sight convergences to the source from observer and deflector, and,
for a sheet much more extended than the effective radius,
J(ξ, β, λ_int) ≈ λ_int J(ξ, β) (Eq. 13). Time delays and kinematics then
give two distances [src: Eqs. 14–15]:

    D_Δt = c Δt_AB / [(1 − κ_ext) λ_int Δτ_AB]
    D_d  = c Δt_AB / [(1 + z_d) Δτ_AB] · c² J / (λ_int σ_los²)

where Δτ_AB is the Fermat-potential difference. D_d is invariant under a
pure external mass sheet, and becomes independent of λ_int when Eq. 13
holds [src: Sect. 3.2]. H0LiCOW already used joint P(D_Δt, D_d) for the
three single-plane lenses with kinematics and a kernel density estimate of
the chains to keep their correlation [src: arXiv:1907.04869, Sect. 3.7].

### Step 5. Hierarchical inference over the lens population
<!-- key: step-5-hierarchical-inference-over-the-lens -->

The posterior on cosmology π factorises over lenses i with individual
parameters ξ_i (lens model, source and lens light) and population
parameters ξ_pop, with the interim priors p(ξ_i) of the single-lens fits
divided out [src: arXiv:2506.03023, Eqs. 20–21]. The internal mass sheet
is a population parameter with a linear trend and a scatter [src: Eq. 23,
Table 3]:

    λ_int(R_eff/θ_E) = λ_int,0 + α_λ (R_eff/θ_E − 1)

| Parameter | Prior, TDCOSMO 2025 [src: Table 3] |
|---|---|
| H0 | U(0, 150) km/s/Mpc |
| Ω_m | U(0.05, 0.5) |
| λ_int,0 | U(0.5, 1.5) |
| α_λ | U(−1, 1) |
| σ(λ_int) | log-uniform (0.001, 0.5) |
| γ_pl of IFU lenses | U(1.5, 2.5) each |
| ⟨σ_t/σ_r⟩ (constant anisotropy) | U(0.87, 1.12) |
| σ(σ_t/σ_r) | log-uniform (0.01, 1) |
| κ_ext | individual p(κ_ext) per lens |

Reasons given: the PEMD alone breaks the mass-sheet degeneracy, so a
global λ_int is added "to allow for the full flexibility" an MST can
produce; it parametrises departures from a power law and does not imply an
infinite sheet [src: Sect. 7.2.1]. The R_eff/θ_E trend is there because
γ_pl is measured locally at θ_E, whose physical radius depends on the
redshift configuration [src: same]. Physically, a cored component
κ_c = R_c²/(R_c² + θ²) approximates the MST for large core radii
(arXiv:2007.02941, Eqs. 35–38); imaging constrains λ_c to 10% for
R_c = 3θ_E and only to ±0.4 for R_c > 5θ_E, and requiring the core mass
not to exceed the NFW mass and the density to stay positive leaves
λ_int = 1 (+0.07/−0.15) [src: Sects. 2.6.1–2.6.2].

### Step 6. Choose the Ω_m information
<!-- key: step-6-choose-the-omegam-information -->

Flat-ΛCDM H0 is mildly degenerate with Ω_m. Pantheon+ without the SH0ES
calibration acts as Ω_m = 0.334 ± 0.018, and the lenses anchor the SN
distances [src: arXiv:2506.03023, Sect. 8.2.1]. With DESI DR2 BAO the
ruler is left uncalibrated, r_d ~ U(0, 300) Mpc, and the lenses fix it:
r_d = 135.6 (+6.7/−6.1) Mpc, about 1.8σ from Planck [src: Sect. 8.2.3].

### Lensed supernovae
<!-- key: lensed-supernovae -->

For SN H0pe the observables are two delays and three absolute
magnifications, {Δt_a,b, Δt_c,b, μ_a, μ_b, μ_c} (arXiv:2403.18902,
Eq. 6); magnifications help because they correlate with the delays inside
each cluster model [src: Sect. VII.2]. For SN Refsdal, 1000 simulated light
curves with the observed cadence and noise, including subhalo and stellar
microlensing, were used to correct the bias of four curve-fitting
algorithms and to build a Gaussian-mixture likelihood [src:
arXiv:2305.06367, "Likelihood calculation"].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Power law fixed, or λ_int free
<!-- key: power-law-fixed-or-lambdaint-free -->

- **λ_int fixed to 1** is equivalent to assuming the power-law profile;
  TDCOSMO-1 (arXiv:1912.08027) is that case [src: arXiv:2506.03023,
  Sect. 10.1.1]. It gave 74.0 (+1.7/−1.8) for the composite family and
  74.2 ± 1.6 for the power law on six lenses [src: arXiv:1912.08027,
  abstract]. Its defence: when both families fit equally well, which
  happens for real lenses through the "bulge-halo conspiracy", the mean
  convergence in the image annulus is recovered; a pathological mock with
  an inflection inside θ_E gave ΔBIC = 434 between the families and a
  different H0, so the two-family procedure either discriminates or
  enlarges the error [src: Sect. 6.4].
- **The critique.** Lensing constrains θ_E and the combination
  ξ = R_E α''(R_E)/(1 − κ_E), not κ_E, and H0 ∝ 1 − ⟨κ⟩ in the image
  annulus; a two-parameter model fixes κ_E = (3 − n)/2 for a power law of
  index n [src: arXiv:1911.05083, Sect. 2.1, Eqs. 3–12]. Matching ξ,
  power-law fits are within 1–2% only for a de Vaucouleurs + NFW lens with
  25% dark matter inside R_E and break radius a/R_E = 10; for other
  dark-matter fractions or scale lengths the error quickly exceeds 5%, and
  the 15% uncertainty on a used by H0LiCOW "greatly underestimates" the
  lens-to-lens range [src: Sect. 2.3].
- **Cost of freeing λ_int.** Fixing it gives a 2% H0 error; freeing it
  contributed 4.5% (quadrature) to the 5% TDCOSMO-IV + SLACS total [src:
  arXiv:2007.02941, Sect. 8.2].

### Anisotropy model and its prior
<!-- key: anisotropy-model-and-its-prior -->

- TDCOSMO-IV used Osipkov–Merritt, β_ani(r) = r²/(r_ani² + r²), scaled by
  a_ani = r_ani/r_eff with a population mean and scatter (arXiv:2007.02941,
  Eqs. 51–52) [src: Sect. 3.2.3]. On the time-delay lens modelling
  challenge the prior choice alone moved H0 from 66.9 ± 4.2 (uniform in
  log a_ani) to 68.4 (+3.4/−3.7) (uniform in a_ani), truth 65.413; log was
  adopted as less informative [src: Sect. 4.2]. 13 mock lenses with 5%
  dispersions would fix λ_int to 2.8% with a perfect anisotropy model, but
  the anisotropy uncertainty limited it to 8% [src: same].
- TDCOSMO 2025 switched to a spatially constant anisotropy, because
  resolved kinematics of nearby ellipticals are well fitted by a uniform,
  nearly isotropic, slightly radial anisotropy, generally preferred over
  radially varying profiles such as Osipkov–Merritt [src:
  arXiv:2506.03023, Sect. 7.2.2].
- Single-aperture dispersions cannot break the mass–anisotropy degeneracy;
  spatially resolved kinematics can [src: same]. The single lens
  SDSSJ1433+6007 is fitted with axisymmetric Jeans models (JAM) on its
  kinematic map, a constant anisotropy, a black-hole mass prior and λ_int
  bounded to (0.88, 1.21) by monotonicity of the convergence and the NFW
  mass bound [src: arXiv:2604.14145, Sect. 8, Table 2, Sect. 8.5].

### Projection of the dispersion
<!-- key: projection-of-the-dispersion -->

Spherical Jeans models of the aperture dispersion within R_eff are biased
by about −4% to +1% depending on intrinsic shape and projected axis ratio;
TDCOSMO 2025 applies a statistical axisymmetric correction factor
σ_axi/σ_sph from a deprojection with a realistic shape distribution,
leaving 1% random error, and the correction moves H0 down by at most 1–2%
[src: arXiv:2506.03023, Sects. 7.2.2 and 10.1.1]. Full axisymmetric JAM on
2D maps in the joint fit was judged too costly for that paper [src:
Sect. 7.2.2].

### Adding non-time-delay lenses
<!-- key: adding-non-time-delay-lenses -->

External lenses (SLACS, SL2S) add kinematic constraints on λ_int under the
assumption that they share the time-delay lenses' population, after cuts
chosen to match them [src: arXiv:2506.03023, Sects. 6, 11.2.2]:

| Cut | Value | Reason given | Place read |
|---|---|---|---|
| Light axis ratio | q_light > 0.7 | range of the time-delay lenses (min 0.73); removes likely spirals not modelled by spherical Jeans equations | Sect. 6.1 |
| Lensing information | 𝓘 > 150 (a = 2, b = 0.1) for aperture lenses | enough information to constrain γ | Sect. 6.2 |
| Spectra | S/N > 13 Å⁻¹ | systematics below 2% | Sect. 6.3 |
| Lensing dispersion | σ_SIS in [150, 350] km/s | range of the time-delay lenses | Sect. 6.4 |
| Environment | ζ_1/R < 2.10 (SLACS) | power law + uncorrelated line of sight must hold | Sect. 6.5 |

Effect on the same data [src: Sects. 8.1, 8.2.1, 10.1.2]: TDCOSMO alone
73.7 (+4.7/−4.4) with uniform Ω_m, 71.6 (+3.9/−3.3) with Pantheon+;
adding SLACS 76.8 (+3.9/−4.6), all three samples 77.8 (+3.7/−4.7) with
uniform Ω_m, 74.3 (+3.1/−3.7) with Pantheon+. SLACS requires intrinsic
scatter in λ_int, which limits the gain; TDCOSMO alone is consistent with
zero scatter but with a long tail [src: Sect. 10.1.2]. The SLACS
follow-up prioritised high SDSS dispersions, which can bias the
dispersions high by up to 5%; for that reason TDCOSMO-only and combined
results are reported separately [src: Sect. 11.2.2].

### Ω_m prior
<!-- key: omegam-prior -->

Changing the Ω_m information alone moves the TDCOSMO-only H0 by 2.1 km/s/Mpc
(73.7 uniform against 71.6 Pantheon+) [src: arXiv:2506.03023,
Sect. 10.1.1]. Comparisons with TDCOSMO-IV and TDCOSMO-1 must match the
prior: TDCOSMO-IV used Ω_m = 0.298 ± 0.022 (Pantheon), TDCOSMO-1 the
uniform prior of Wong et al. (2020) [src: same].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| D_Δt error budget per lens: delays / line of sight / model | 1.6–6.4% / 2.7–6.4% / 2.2–8.4%; totals 4.3–9.1% | H0LiCOW, 6 lenses | arXiv:1907.04869 | Table 3 |
| PyCS delay recovery on blind mocks | ~3%, negligible bias | COSMOGRAIL | arXiv:1907.04869 | Sect. 3.2 |
| Longest delay, RXJ1131 / HE0435 | 1.5% / 6.5% (13-yr curves) | COSMOGRAIL | arXiv:1907.04869 | Sect. 3.2 |
| Mean dispersion error, 7 lenses | 4.0% (new) vs 7.7% (TDCOSMO-IV) | TDCOSMO 2025 | arXiv:2506.03023 | Sect. 10.1.1 |
| σ_new/σ_old, 7 lenses | 0.986 ± 0.049 | TDCOSMO 2025 | arXiv:2506.03023 | Sect. 10.1.1 |
| SDSS-SLACS dispersions | 3.3% systematic, 2.3% covariance (as cited) | TDCOSMO 2025 | arXiv:2506.03023 | Sect. 10.1.2 |
| H0 floor from KCWI template covariance | 1.5–2% | SLACS-KCWI | arXiv:2506.03023 | Sect. 10.1.2 |
| α_λ | 0.00 ± 0.05 (TDCOSMO), 0.03 (+0.05/−0.06) (+SLACS) | TDCOSMO 2025 | arXiv:2506.03023 | Sect. 8.2.1 |
| λ_int, TDCOSMO-IV | 1.02 (+0.08/−0.09) | 7 lenses | arXiv:2506.03023 | Sect. 10.1.1 |
| r_d anchored by lenses | 135.6 (+6.7/−6.1) Mpc | TDCOSMO 2025 + DESI DR2 | arXiv:2506.03023 | Sect. 8.2.3 |
| Imaging limit on cored MST | λ_c to 10% at R_c = 3θ_E; ±0.4 at R_c > 5θ_E | mock quad | arXiv:2007.02941 | Sect. 2.6.1 |
| Kinematic shift test | 10% in all dispersions → 0.7% in H0 | TDCOSMO-1 procedure (power law), 7 lenses | arXiv:1912.08027 | abstract |
| Lensed SN H0pe split | ~9% total: 2/5 photometry and spectra, 3/5 lens models (1/4 single-model, 3/4 spread) | SN H0pe | arXiv:2403.18902 | Sect. X.5 |
| Quad selection bias | sub-percent | literature summary | arXiv:2506.03023 | Sect. 11.2.1 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Power-law precision read as accuracy.** Shows up as a small error with
  λ_int fixed. Test: free λ_int with kinematics (arXiv:2007.02941), and
  compare power-law and composite fits; a large ΔBIC or a gap in H0 flags
  an inflected profile [src: arXiv:1912.08027, Sect. 6.4].
- **Anisotropy prior driving H0.** Test: rerun with uniform and
  log-uniform anisotropy priors, as on the modelling challenge, where the
  shift was 1.5 km/s/Mpc [src: arXiv:2007.02941, Sect. 4.2]; better,
  resolved kinematics.
- **Ω_m prior mismatch** in comparisons between analyses: 2.1 km/s/Mpc on
  the same lenses [src: arXiv:2506.03023, Sect. 10.1.1].
- **External-lens population mismatch.** SLACS pre-selection on noisy
  high SDSS dispersions; intrinsic scatter in λ_int [src: Sect. 11.2.2].
  Test: report the time-delay-only result and each external sample
  separately, as TDCOSMO 2025 does. The TDCOSMO-IV + SLACS value
  67.4 (+4.1/−3.2) relied on SDSS dispersions now judged unsuited for
  cosmography and "should not be considered as valid anymore" [src:
  Sect. 10.1.2].
- **κ_ext from random lines of sight.** Lens fields are overdense; a
  population model fitted on lens samples is needed [src: Sect. 7.2.3].
  Test: weak-lensing κ_ext against number counts [src: arXiv:1907.04869,
  Sect. 3.4].
- **Microlensing in short light curves.** Test: a longer, sparser second
  data set or mock light curves with red noise [src: arXiv:2604.14145,
  Sect. 4].
- **Confirmation bias.** H0LiCOW blinded D_Δt, D_d, H0 by subtracting the
  median of each PDF so shapes and covariances stay visible; results are
  published without change after unblinding [src: arXiv:1907.04869,
  Sect. 3.6]. TDCOSMO 2025 did not blind the dispersions themselves but
  had three team members measure them independently and froze them before
  unblinding [src: arXiv:2506.03023, Sect. 10.1.1].
- **Disagreeing cluster models (lensed SNe).** The spread between models
  dominates; magnifications reweight the models [src: arXiv:2403.18902,
  Sect. X.5].

## Reading list
<!-- key: reading-list -->

- Review: Birrer et al. 2024, arXiv:2210.10833 — full method review.
- Foundation: Refsdal 1964, doi:10.1093/mnras/128.4.307 — delays give H0.
- Method: Birrer et al. 2020, arXiv:2007.02941 — hierarchical λ_int,
  cored MST bounds, anisotropy priors, modelling challenge.
- Method: Millon et al. 2020, arXiv:1912.08027 — power law against
  composite, kinematics sensitivity.
- Application: Wong et al. 2020, arXiv:1907.04869 — delays, κ_ext, blind
  procedure, per-lens budgets.
- Application: TDCOSMO 2025, arXiv:2506.03023 — current priors, external
  lens cuts, projection correction, Ω_m choices.
- Application: Sheu et al. 2026, arXiv:2604.14145 — single lens with JAM
  and free λ_int; current delay pipeline.
- Application: Pascale et al. 2025, arXiv:2403.18902 — lensed SN Ia with
  magnifications.
- Critique: Kochanek 2020, arXiv:1911.05083 — what lens data constrain.
- Critique: Forés-Toribio et al. 2026, arXiv:2602.03934 — kinematic
  systematics (sizes in L2).

## Not verified
<!-- key: not-verified -->

- The time-delay equation numbered Eq. 9 in arXiv:2506.03023 (cited by its
  Sect. 3.2) and the Table 6 posteriors of the population parameters were
  not read.
- The sizes of the microlensing time-delay effect per lens, and the PyCS3
  method papers (Tewes et al. 2013; Millon et al. 2020), cited through
  arXiv:2604.14145 and arXiv:1907.04869, not read; no identifier recorded.
- The generalised extreme-value κ_ext model (Wells et al. 2024) and the
  projection correction (Huang et al. 2025): cited through
  arXiv:2506.03023, bodies not read.
- Forés-Toribio et al. 2026 body: only its outline was fetched in this run.
