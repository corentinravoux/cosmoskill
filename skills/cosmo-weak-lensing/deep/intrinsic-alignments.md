# Intrinsic-alignment modelling — cosmo-weak-lensing dossier

Scope: how an intrinsic-alignment (IA) model, its redshift scaling and its
priors are chosen and built for a cosmic-shear or 3×2pt analysis (NLA,
TATT, mass- or colour-informed NLA, halo model), how the choice is decided
before unblinding, and what each choice has been shown to cost on synthetic
and real data.
Snapshot: 2026-10-17.
From: Pantos 2026 review (arXiv:2602.12238), Sects. 4.1.1 and 7.3; Chisari
2025 IA review (arXiv:2510.15738), Sects. 2 and 7.3.

Already in L2, not repeated here: the NLA and TATT formulas and constants as
KiDS-Legacy, DES Y6 and HSC Y3 write them
(`physics-and-methods.md#estimators`); the model, prior, posterior and S8
shift of each main analysis, and the direct measurements
(`systematics.md#intrinsic-alignments`); the IA share of the error budget
(`systematics.md#other-effects-a-complete-analysis-treats`).

Symbols. γ^I: intrinsic shape (or intrinsic shear) field; s_ij: tidal
tensor; δ: matter density contrast; GI and II: the shear–intrinsic and
intrinsic–intrinsic contributions to the shear power spectrum; A₁ (A_IA in
NLA), A₂: dimensionless amplitudes of tidal alignment and tidal torquing;
b_TA (written b_ta in HSC, A₁δ or C₁δ in Blazek et al.): the density-weighting
coefficient; η₁, η₂: redshift power-law indices about a pivot z₀; C̄₁:
normalisation constant; ρ_crit: critical density today; D(z) or G(z): linear
growth factor normalised to one at z = 0.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Write the expansion and know what each term is
<!-- key: step-1-write-the-expansion-and-know-what-each -->

TATT is a perturbative expansion of the intrinsic shape in the tidal field,
γ^I_ij = C₁ s_ij + C₂ (s_ik s_kj − δ_ij s²/3) + C₁δ (δ s_ij) + C_t t_ij + …
(Blazek et al. 2017, arXiv:1708.09247, Eq. 8) [src: Sect. II.2]. The C's
play the role of bias parameters and absorb small-scale physics; the
velocity-shear term t_ij is dropped in the paper, so the model is not
formally equivalent between Eulerian and Lagrangian treatments [src: Sect.
II.2]. Spin-2 symmetry makes s_ij enter at linear order, unlike for galaxy
density [src: Sect. II.2]. The authors note that the "intrinsic shape" is
not uniquely defined and depends on the shape-measurement method, which
also changes the measured C's [src: Sect. II.2]: an amplitude is a property
of a sample and a shape estimator, not of galaxies.

The power spectra as HSC Y3 implements them, to one loop with FAST-PT
(arXiv:2304.00702, Eq. 19) [src: Sect. IV.2]:
P^E_GI = c₁P_δ + b_ta c₁P_0|0E + c₂P_0|E2;
P^E_II = c₁²P_δ + 2b_ta c₁²P_0|0E + b_ta² c₁²P_0E|0E + c₂²P_E2|E2 +
2c₁c₂P_0|E2 + 2b_ta c₁c₂P_0E|E2; and a B-mode P^B_II from the b_ta and c₂
terms. The tidal-torquing term c₂ has no leading-order GI contribution, so
its overall effect on shear is suppressed relative to a C₁ term of equal
windowed variance [src: arXiv:1708.09247, Sect. III.5.2].

### Step 2. Fix the normalisation convention
<!-- key: step-2-fix-the-normalisation-convention -->

- **C₁.** C₁(z) = −A₁(z) C̄₁ρ_crit Ω_m G(z)⁻¹ (arXiv:1708.09247, Eq. 40),
  with C̄₁ = 5 × 10⁻¹⁴ h⁻² M⊙⁻¹ Mpc³, C̄₁ρ_crit ≈ 0.014, fixed from the
  windowed ellipticity variance in SuperCOSMOS assuming NLA [src: Sect.
  III.5.1]. The minus sign makes positive A₁ mean alignment towards
  overdensities [src]. An older growth-factor normalisation differs by about
  30% [src: footnote to Eq. 40]. DES Y6 and HSC Y3 print the constant as
  5 × 10⁻¹⁴ M⊙ h⁻² Mpc² [src: arXiv:2602.10065, Sect. IV.2;
  arXiv:2304.00702, Sect. IV.2]; the number is the same, the units as printed
  differ from Blazek et al.; L2 copies the DES and HSC form. KiDS-Legacy's
  C₁ρ_cr ≈ 0.0134 (L2) is the same constant to more digits.
- **C₂.** C₂(z) = A₂ (5C̄₁ρ_crit/Ω_m,fid) Ω_m² G(z)⁻² (Eq. 42); the factor 5
  makes |A₁| = |A₂| give about the same windowed II variance at z = 0 [src:
  Sect. III.5.2]. The paper calls these scalings "somewhat arbitrary", useful
  for comparing surveys, and warns that care is needed when limiting the
  allowed redshift dependence [src: Sect. III.5.2]. The expected sign of A₂
  is unknown; hydrodynamical simulations disagree [src].
- **C₁δ.** If density weighting is the only origin, C₁δ = b₁C₁ at one loop
  [src: Sect. III.5.1]; analyses parametrise it as b_TA a₁ (DES Y6,
  arXiv:2602.10065, Eq. 15) [src].
- **Shape noise.** Constant k → 0 contributions of higher-order II terms are
  absorbed into an effective shape noise; the IA "shape noise" on finite
  scales is decoupled from the zero-lag ellipticity variance, so n_eff
  estimated from one-point statistics need not include it [src:
  arXiv:1708.09247, Sect. III.7.2].

### Step 3. Choose the redshift and population dependence
<!-- key: step-3-choose-the-redshift-and-population -->

Four forms are in use:

1. **Power law** ((1 + z)/(1 + z₀))^η on each amplitude, pivot 0.3 (DES Y6,
   "to match the peak sensitivity of DES Y6 cosmic shear") or 0.62 (HSC Y3)
   [src: arXiv:2602.10065, Sect. IV.2; arXiv:2304.00702, Sect. IV.2]. A power
   law cannot cross zero, so it assumes the amplitude keeps its sign with
   redshift, a concern if blue galaxies change sign at high redshift [src:
   arXiv:2510.15738, Sect. 7.3.1]. In the Euclid Flagship IA simulation the
   power law fails above z = 1.1; including the luminosity dependence fixes
   this [src: arXiv:2601.07784, Abstract].
2. **Linear in scale factor** (KiDS-Legacy NLA-z, L2).
3. **Population-weighted (NLA-M).** Only the red fraction f_r of each bin
   aligns, with amplitude ∝ (⟨M_h⟩/M_h,piv)^β (arXiv:2503.19441, Eq. 11)
   [src: Sect. 2.4.4]. The reasons given: early types are the only
   significant detections on cosmological scales, late types should align
   through torquing (quadratic), spheroids linearly, and the early-type
   amplitude scales with halo mass as a power law [src: Sect. 2.4.4].
4. **Bin-by-bin amplitudes with informed priors** (DES Y3 blue sample:
   NLA, one free amplitude per bin) [src: arXiv:2512.04209, Sect. III.2,
   App. B].

### Step 4. Build the prior
<!-- key: step-4-build-the-prior -->

**Wide flat priors.** HSC Y3: A₁, A₂, η₁, η₂ ∈ [−6, 6], b_ta ∈ [0, 2], because
"the IA signal is very sensitive to the properties (e.g., color, magnitude)
of the galaxy sample" and reliable Gaussian priors could not be derived for
its shear catalogue [src: arXiv:2304.00702, Sect. IV.2].

**Informed by direct measurements of red galaxies (KiDS-Legacy NLA-M).**
The recipe [src: arXiv:2503.19441, Sect. 2.4.4 and App. B]:

1. f_r per bin from the bpz template index T_B < 1.9, which includes any
   galaxy with an elliptical-template contribution, validated against the
   red sequence on a KiDS–GAMA matched sample; varying the cut by ±0.1
   changes f_r by less than 0.02, so f_r is fixed.
2. ⟨M_h⟩ per bin from r-band luminosities through a linear relation fitted
   to weak-lensing halo masses of SDSS early types:
   log₁₀M_h = γ[1/(1 + ⟨z⟩) − 1/(1 + z_piv)] + δ log₁₀(⟨L_r⟩/L₀) + ΔM
   (Eq. 28), z_piv = 0.3417, L₀ = 10¹¹ (h/0.7)⁻² L⊙, γ = 1.25 ± 0.33,
   δ = 1.42 ± 0.16, ΔM = 13.56 ± 0.02.
3. The uncertainty on log₁₀M_h (about 0.2 in bin 1, 0.1 elsewhere, bins
   correlated above 0.9) enters as a multivariate Gaussian prior of width 0.2
   in every bin.
4. A_IA and β with a bivariate Gaussian prior from a fit to early-type
   measurements, pivot 10^13.5 h⁻¹ M⊙.
5. No central/satellite distinction; the paper argues blue satellites matter
   less because early-type satellite fractions are about twice those of late
   types at fixed mass and redshift.

Resulting per-bin values: f_r = 0.15, 0.20, 0.17, 0.24, 0.19, 0.03 and
log₁₀M_eff = 11.69 to 13.21 from bin 1 to bin 6 [src: App. B, Table 5]. The
sixth bin has almost no early types, which is why the NLA-M amplitude drops
there [src: arXiv:2510.15738, Sect. 7.3.1].

**Informed null for blue galaxies (DES Y3 blue sample).** The recipe [src:
arXiv:2512.04209, App. B]: per bin, a zero-centred Gaussian whose width
combines, by inverse variance in each redshift slice, the uncertainties of
DESI BGS and ELG, eBOSS ELG and PAUS null measurements (Eq. 5); the part of
the bin's n(z) not covered by any measurement, f_u,b(z) (Eq. 4), receives a
wide width ΔA_u = 3, added in weighted quadrature (Eq. 6); the bin width is
the n(z)-weighted mean (Eq. 7); priors truncated at [−3, 3]. Widths obtained:
0.66, 0.77, 0.68, 0.86 [src: App. A, Table 2]. The stated reason for a zero
centre: no high-confidence alignment of these galaxies exists [src: App. B].
What makes it legitimate: the bluest galaxies (rest-frame M_r − M_z < 0.50,
about the bluest 30% of DESI BGS) show no shape–density correlation at 3σ,
and colour, the 4000 Å break and specific star-formation rate are equally
efficient selectors (Siegel et al. 2025, arXiv:2507.11530) [src: Sect. 4.3].

### Step 5. Decide the model before unblinding
<!-- key: step-5-decide-the-model-before-unblinding -->

Three practices exist:

- **Run two models in parallel and keep both.** DES Y6: "limited a priori
  evidence to justify either excluding or including the higher-order TATT
  contributions", and no thoroughly validated data-based selection, so NLA
  and TATT were both kept as fiducial [src: arXiv:2602.10065, Sect. IV.2].
  HSC Y3 analysed all blinded data vectors with both and compared S8 and χ²
  [src: arXiv:2304.00702, Sect. IV.2].
- **Calibrated Δχ² threshold** (Campos et al. 2022, arXiv:2211.02800)
  [src: Sect. 4.4]: draw 10–30 IA scenarios (21 from DES Y1 TATT
  posteriors), make noiseless data vectors, fit with both models, map the
  bias in the Ω_m–S8 plane against Δχ², add about 50 noise realisations per
  scenario (1050 noisy vectors, importance sampling), compute the probability
  that the bias exceeds a chosen threshold, then read the Δχ² of the blinded
  data. Theoretical thresholds from χ² p-values were found "overly
  optimistic", failing to exclude biases of about 1–2σ [src: Abstract]. Applied
  to the published DES Y3 Δχ², the chance that an NLA fiducial would have
  been biased by more than 0.3σ is about 30% [src: Abstract].
- **Internal-tension check.** In DES Y3-like mocks with NLA, IA scenarios
  that bias cosmic shear by up to 5σ bias γ_t + w(θ) by about 1σ only,
  thanks to the redshift separation in galaxy–galaxy lensing; the 3×2pt
  combination is still biased by its cosmic-shear part; tension between ξ±
  and γ_t + w is proposed as a model-sufficiency test (Samuroff et al. 2024,
  arXiv:2402.15573) [src: Abstract].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

| Model | Free parameters | Assumes | Buys | Costs | Used by |
|---|---|---|---|---|---|
| NLA | A₁ (and η₁) | linear response to the tidal field, extended with non-linear P(k) | fewest parameters | misses torquing and density weighting; redshift-independent form biases A₁ on Euclid mocks | KiDS-1000, DES Y6 (one of two), joint DES + KiDS (L2) |
| TATT | A₁, A₂, η₁, η₂, b_TA | perturbative expansion to second order | covers NLA; recovers both mock types | weakly constrained terms at large k_min; projection effects (L2) | DES Y3, HSC Y3, DES Y6 (one of two) |
| TATT with b_TA = 1 | four | density weighting fixed | one fewer parameter | large bias when b_TA ≠ 1 in the truth (below) | DES Y6 |
| NLA-M | A_IA, β (informed), masses | only red galaxies align; mass power law | ≈ 5% tighter than NLA (L2) | depends on f_r, halo-mass extrapolation, no satellites | KiDS-Legacy |
| Tailored NLA, blue sample | one amplitude per bin, informed null | blue galaxies do not align | factor 1.7 in σ(S8) (L2) | shot noise from discarding red galaxies | DES Y3 blue (reanalysis) |
| Halo model | central and satellite terms | radial satellite alignment, HOD | small-scale IA | depends on satellite fractions and halo exclusion | forecasts, simulation studies |

Stated reasons for fixing b_TA in DES Y6: "guided by simulated tests"
of its modelling paper [src: arXiv:2602.10065, Sect. IV.2]. The Euclid DR1
study reaches the opposite conclusion for its setup: zTATT with b_TA = 1
"shows a large bias in all of its four parameters" because b_TA = 1 does not hold
in the Flagship data vectors, and b_TA > 0 also fails in MassiveBlack-II at
high redshift and in the DES Y3 redMaGiC low-z sample, as cited there [src:
arXiv:2602.16448, Sect. 5.2].

Comparisons on the same synthetic data (Euclid DR1 3×2pt, six bins, about
2500 deg², data vectors from zNLA and zTATT with IA values measured in
Flagship) [src: arXiv:2602.16448, Sects. 5.1–6]:

- With weak-lensing k_max = 1 h Mpc⁻¹ the higher-order TATT terms are
  unconstrained; with k_max = 3 h Mpc⁻¹ they are constrained and TATT loses
  "virtually" no constraining power relative to NLA [src: Sect. 6].
- Only zTATT recovers cosmology for both generating models. Redshift-
  independent NLA and TATT bias A₁; most biases above 0.3σ occur in w0waCDM
  with zTATT data vectors [src: Sect. 5.2].
- The dangerous region is low Δχ²_ν with high bias, undetectable from the
  fit quality alone: six cases in the S8–Ω_m plane, three of them zTATT with
  b_TA = 1. A Δχ²_ν of about 0.08 corresponds to a 2% PTE [src: Sect. 5.2].
- Narrowing the IA priors (two narrower sets listed) leaves the cosmological
  constraints "virtually the same" [src: Sect. 5.1.4]. This contrasts with
  the KiDS-Legacy and DES Y3 blue-sample gains from informed priors (L2),
  which come from real-data analyses with less constraining power per bin.
- Degeneracy with photo-z: none with Stage-III-like Gaussian Δz priors; it
  appears with flat priors three times wider; none with A₂, η₂ [src:
  Sect. 6].
- The fixed cosmological parameters in this study exclude projection
  effects, so its shifts are lower limits in that sense [src: Sect. 3.2].

Halo model and redshift scaling [src: Fortuna et al. 2020,
arXiv:2003.02700]: satellites are modelled as radially aligned sticks,
γ^I = γ̄(r, M) sin θ e^{2iφ} (Eq. 9), density-weighted by N_g u(r|M) (Eq. 10)
[src: Sect. 4.1]. Injecting halo-model IA into a KV450-like ξ± analysis
(θ₊ from 3′ to 72′, θ₋ from 6′ to 153′), NLA and NLA-z recover cosmology for
Stage III [src: Sect. 6.2]; for a 15,000 deg² Stage-IV setup NLA biases Ω_m
by 1σ or more than 2σ depending on the luminosity scaling, while NLA-z
recovers cosmology, its fit being driven by the low-redshift bins [src:
Sect. 6.2.1].

Prior values that differ from L2. L2 gives the KiDS-Legacy NLA-M prior as
A_IA = 5.74 ± 0.29, β = 0.44 ± 0.03, correlation −0.59; that is the
bivariate Gaussian approximation stated in arXiv:2503.19441, Sect. 2.4.4.
The KiDS-1000 LRG paper whose amplitude and slope it matches quotes
A = 5.74 ± 0.32 and β_M = 0.44 ± 0.04 over 1.9 × 10¹² to 3.7 × 10¹⁴ h⁻¹ M⊙
(Fortuna et al. 2024, arXiv:2409.15416) [src: Abstract]; the papers read do
not say why the widths differ. KiDS-Legacy cites "Fortuna et al. (2025)";
the identification with arXiv:2409.15416 rests on the identical central
values.

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| C̄₁ | 5 × 10⁻¹⁴ h⁻² M⊙⁻¹ Mpc³; C̄₁ρ_crit ≈ 0.014 | convention | arXiv:1708.09247 | Eq. 40, Sect. III.5.1 |
| Torquing normalisation factor | 5 | convention | arXiv:1708.09247 | Eq. 42 |
| Pivot redshift | 0.3 (DES Y6); 0.62 (HSC Y3) | — | arXiv:2602.10065; arXiv:2304.00702 | Sect. IV.2 |
| HSC Y3 TATT priors | [−6, 6]; b_ta ∈ [0, 2] | HSC Y3 | arXiv:2304.00702 | Sect. IV.2 |
| Euclid fiducial IA priors | A₁ ∈ [0, 3], A₂ ∈ [−2, 2], b_TA ∈ [−5, 3], η₁ ∈ [0, 4], η₂ ∈ [−6, 6] | Euclid DR1 forecast | arXiv:2602.16448 | Sect. 5.1.4 |
| Bias threshold | 0.3σ in 2D | Euclid; Campos et al. | arXiv:2602.16448; arXiv:2211.02800 | Sect. 5.2; Abstract |
| NLA-M per-bin f_r | 0.15, 0.20, 0.17, 0.24, 0.19, 0.03 | KiDS-Legacy | arXiv:2503.19441 | Table 5 |
| NLA-M halo-mass relation | γ = 1.25 ± 0.33, δ = 1.42 ± 0.16, ΔM = 13.56 ± 0.02 | KiDS-Legacy | arXiv:2503.19441 | App. B, Eq. 28 |
| Blue-sample prior widths | 0.66, 0.77, 0.68, 0.86, truncated [−3, 3] | DES Y3 blue | arXiv:2512.04209 | Table 2, App. B |
| Blue cut with no detection | M_r − M_z < 0.50 (bluest ≈ 30%) | DESI Y1 BGS | arXiv:2507.11530 | Sect. 4.3 |
| Fit ranges for direct IA | NLA 6–65, TATT 2–65 h⁻¹ Mpc | DESI Y1 | arXiv:2507.11530 | Sect. 3.2 |
| NLA/TATT valid in Flagship | down to 6–7 h⁻¹ Mpc | Euclid Flagship IA | arXiv:2601.07784 | Abstract |
| Model-selection calibration | 21 scenarios × 50 noise = 1050 vectors | DES Y3 setup | arXiv:2211.02800 | Sect. 4.4 |
| P(bias > 0.3σ) had NLA been fiducial | ≈ 30% | DES Y3 | arXiv:2211.02800 | Abstract |
| Cosmic shear vs 2×2pt robustness | up to 5σ vs ≈ 1σ | DES Y3-like mocks | arXiv:2402.15573 | Abstract |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Model too simple but fit acceptable.** IA residuals absorbed by a shift
  in cosmology with low Δχ² [src: arXiv:2602.16448, Sect. 5.2]. Test:
  calibrated Δχ² thresholds from mocks, not p-values (arXiv:2211.02800).
- **b_TA fixed to a value the sample does not have.** Biases all IA
  parameters on Euclid mocks [src: arXiv:2602.16448, Sect. 5.2]. Test: free
  b_TA on mocks with simulation-calibrated IA.
- **Power-law redshift scaling beyond its range.** Fails above z = 1.1 in
  Flagship [src: arXiv:2601.07784, Abstract]; cannot change sign [src:
  arXiv:2510.15738, Sect. 7.3.1]. Test: luminosity-dependent scaling, or
  per-bin amplitudes.
- **Amplitude compared across codes or estimators.** Sign and growth
  normalisation conventions differ (a 30% growth-normalisation difference
  exists in the literature) and the amplitude depends on the shape
  estimator [src: arXiv:1708.09247, Sect. II.2, III.5.1]. Test: state
  C̄₁, D(z) normalisation, pivot and estimator with every A_IA.
- **Informed prior extrapolated.** NLA-M halo masses in bin 1 extrapolate
  the luminosity relation (σ ≈ 0.2 dex) [src: arXiv:2503.19441, App. B]; the
  blue prior relies on null measurements whose high-z DESI point is "noisy
  and very sensitive to choice of scale" [src: arXiv:2512.04209, App. B].
  Test: widen to the uninformative limit and report the S8 shift.
- **Blue sample not pure.** The amplitude rises with redder cuts [src:
  arXiv:2507.11530, Sect. 4.3]. Test: vary the colour cut.
- **3×2pt assumed to self-calibrate IA.** It does not when cosmic shear
  drives the bias [src: arXiv:2402.15573, Abstract]. Test: compare the ξ±
  and γ_t + w posteriors.
- **Bayes ratio quoted as model choice.** For nested models with wide priors
  it is prior-independent only in a limit [src: arXiv:2211.02800, Sect.
  4.2.2]; in DES Y6 it changes by a factor 2 when two priors are scaled by √2
  (L2).

## Reading list
<!-- key: reading-list -->

- Review: Chisari 2025, arXiv:2510.15738 — models from NLA to EFT and halo
  model; mitigation in KiDS and DES.
- Foundation: Blazek et al. 2017, arXiv:1708.09247 — TATT expansion and the
  normalisation conventions in use.
- Method: Fortuna et al. 2020, arXiv:2003.02700 — halo-model IA and its
  Stage-III/IV consequences.
- Method: Campos et al. 2022, arXiv:2211.02800 — calibrated model selection.
- Application: Wright et al. 2025, arXiv:2503.19441 — NLA-M construction.
- Application: DES Collaboration 2026, arXiv:2602.10065 — two fiducial
  models, b_TA fixed.
- Application: Bigwood et al. 2025, arXiv:2512.04209 — tailored null priors
  for a blue sample.
- Data: Siegel et al. 2025, arXiv:2507.11530 — which galaxies do not align.
- Data: Fortuna et al. 2024, arXiv:2409.15416 — mass scaling behind NLA-M.
- Test: Euclid Collaboration 2026, arXiv:2602.16448 — NLA/TATT variants on
  the same synthetic data.
- Test: Euclid Collaboration 2026, arXiv:2601.07784 — where NLA, TATT and
  the power law hold in Flagship.
- Critique: Samuroff et al. 2024, arXiv:2402.15573 — IA mismodelling shows as
  internal tension.

## Not verified
<!-- key: not-verified -->

- The DES Y6 modelling paper's simulated tests behind b_TA = 1 (reference
  [145] of arXiv:2602.10065): not read.
- The Euclid study's numerical biases per case (its Fig. 8 is a figure).
- Effective-field-theory and HYMALAIA IA models (arXiv:2510.15738, Sects.
  2.4–2.7): section titles seen, bodies not read.
- The companion tailored-IA paper (McCullough, Siegel et al., in prep.):
  not available.
