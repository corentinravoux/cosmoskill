# Siren × large-scale-structure cross-correlation — cosmo-multimessenger dossier

Scope: how a siren–galaxy cross-correlation H0 is produced (event and catalogue
selection, maps, estimator, scale cuts, theory template, bias, covariance,
detection test), and how to choose between the analytic, measured-auto and
simulation-template variants and between Gaussian and simulated covariances.
Snapshot: 2026-10-17.
From: Palmese & Mastrogiovanni 2025 review (arXiv:2502.00239), Sects. 2.3 and
3.4; Einstein Telescope science case (arXiv:2503.12263), Sect. 2.4.1; LISA
Cosmology Working Group (arXiv:2204.05434), Sect. 2.6.1.

Already in L2, not repeated here: the principle (shells in `d_L` against shells
in `z`) and the list of method papers in
`physics-and-methods.md#siren-x-large-scale-structure-cross-correlation`; the
two published H0 values in `results.md`; the tracer debate in
`open-questions.md#tracer-choice-for-a-field-level-siren-h0`; the forecast
rows (Bera 2020, Pan 2025) in `open-questions.md#forecasts`.

## How it is done
<!-- key: how-it-is-done -->

Notation. `C_ℓ(z_i, D_Lj)` is the angular cross-power spectrum between galaxies
in redshift bin `z_i` and sirens in luminosity-distance bin `D_Lj`; `a_ℓm` are
spherical-harmonic coefficients of a map; `b_g`, `b_GW` (also written `b_gw`)
are the linear biases of galaxies and sirens; `ΔΩ` or `Ω_90` is the sky area
of a siren posterior (68% or 90%); `ℓ_max` the largest multipole kept. This
dossier follows the notation of de Matos et al. 2025 (arXiv:2512.15380) for
the data analysis and of Ferri et al. 2025 (arXiv:2412.00202) for the
simulation template.

### Step 1. Select sirens and a galaxy catalogue that overlap in volume
<!-- key: step-1-select-sirens-and-a-galaxy-catalogue -->

Only events whose distance posterior, converted with an H0 inside the prior,
falls inside the catalogue's redshift range carry signal. Two selections on
GWTC-3:

| Analysis | Cut | Events kept | Galaxy catalogue | Place read |
|---|---|---|---|---|
| Mukherjee et al. 2022 (arXiv:2203.03643) | network SNR ≥ 11 and `ΔΩ ≤ 30` deg² at 68.3% | 8 events, grouped into three GW maps by the position of the `d_L` posterior peak; usable sky `f_sky ≈ 2%` | 2MPZ at `z < 0.1` (`σ_z = 0.015`), WISE×SuperCOSMOS at `z > 0.1` (`σ_z/(1+z) = 0.033`); mask leaves about 65% of the sky; `z > 0.5` excluded | Sect. III |
| de Matos et al. 2025 (arXiv:2512.15380) | event inside GLADE+ range for H0 in [20, 120]; well localised | GW190814 (`Ω_90 = 18.5` deg²) and GW170817 (sky position of NGC 4993 fixed, its redshift not used); GW190425 dropped (one detector, poor localisation); GWTC-4.0 O4a events dropped (no Virgo, poor localisation) | GLADE+ `K` band, about 2.8 × 10⁵ galaxies after cuts | Sect. III |

Reasons given: the technique is "most effective for sources with better sky
localization error" and high-SNR sources are "the most constraining"
[src: arXiv:2203.03643, Sect. III]. Events are grouped by distance peak "to
enhance the cross-correlation signal" [src: same]. DECaLS was rejected there
because its northern footprint misses four of the eight events [src: same].

### Step 2. Build the maps
<!-- key: step-2-build-the-maps -->

- **Overdensity maps** (Mukherjee et al. 2022): `δ^X(θ, φ) = n_X(θ, φ)/n̄_X − 1`,
  `X ∈ {GW, g}` [src: arXiv:2203.03643, Eq. 1].
- **Probability-weighted voxels** (de Matos et al. 2025): HEALPix `nside = 32`
  (about 4 deg² pixels); galaxies counted in redshift bins of `Δz = 0.01`,
  three times narrower at `z < 0.02` "which is crucial to locate the
  cross-correlation peak of the nearest GW sources"; each photo-z Gaussian is
  integrated over the voxel; the GW map `N_gw(D_Lj, n̂)` is the sum over events
  of the 3D localisation posterior (marginalised over masses and spins)
  integrated per voxel [src: arXiv:2512.15380, Sects. II, III]. Distance bins
  are those that map onto the galaxy redshift bins in the fiducial cosmology
  [src: Sect. III].
- **Cuts.** Galactic mask `|b| > 20°`; galaxies whose photo-z PDF has more
  than 0.15% support below `z = 0` removed [src: arXiv:2512.15380, Sect. III].
- **Completeness.** `f̂_S(n̂, z) = ∫_{L(m_th(n̂))}^{L_max} φ(L) dL / ∫_{L_min}^{L_max}
  φ(L) dL` (arXiv:2512.15380, Eq. 4), Schechter with `M* = −23.39`,
  `M_min = −27`, `M_max = −19`, `α = −1.09` for GLADE+ `K` band [src: Sect. III].
  Only the pixel-to-pixel variation matters for a two-point statistic, so the
  denominator and `L_min` are irrelevant here, unlike in the catalogue method
  [src: arXiv:2512.15380, App. B].

### Step 3. Estimate the cross-spectrum
<!-- key: step-3-estimate-the-cross-spectrum -->

`C_ℓ(z_i, D_Lj) = (2ℓ+1)⁻¹ Σ_m a^g_ℓm(z_i) a^gw*_ℓm(D_Lj)` (arXiv:2512.15380,
Eq. 1), with `N_X(r_Xi, n̂) = Σ a_ℓm Y_ℓm(n̂)` (Eq. 2); on masked maps this is a
pseudo-spectrum, binned as `Ĉ_ℓb = Σ_{ℓ∈b} W_ℓ C_ℓ` (arXiv:2203.03643,
Eqs. 2–3) [src]. de Matos et al. use NaMaster for the masked estimate [src:
Sect. III]. Shot noise enters only the auto-spectra: Ferri et al. subtract
`δ_ij δ^αβ N̄^α(r_i)` from the raw coefficients (arXiv:2412.00202, Eq. 5) [src];
in de Matos et al. the cross shot noise, estimated from simulations with
galaxies and sirens uniform on the sky, was negligible and removed [src:
App. A]. Neither data analysis uses the GW auto-spectrum: with current events it
is shot-noise dominated [src: arXiv:2512.15380, Sect. II;
arXiv:2412.00202, Fig. 2 caption].

### Step 4. Choose the scales
<!-- key: step-4-choose-the-scales -->

The siren localisation acts as a beam. Three ways it is set:

- Mukherjee et al. 2020: a Gaussian sky error smooths the GW field for
  `k > k_eff(z) ≡ √(8 ln 2) / (ΔΩ_GW^{1/2} d_c(z))`, applied as
  `δ_GW(k) e^{−k²/k²_eff}` [src: arXiv:2007.02943, Sect. III].
- Mukherjee et al. 2022: `ℓ ≤ 30` "due to the poor sky localization", bins
  `Δℓ = 5` or 15, first bin dropped "to minimize low-ℓ contamination" [src:
  arXiv:2203.03643, Sect. II].
- de Matos et al. 2025: `ℓ > 180°/√(Ω_90/π)` excluded (the resolution of
  GW190814), `Δℓ = 5` "which minimizes correlations introduced by the mask",
  first two bins dropped (cosmic variance, Galactic mask): bin centres 14,
  19, …, 69 [src: arXiv:2512.15380, Sect. III].

Cheng & Gair 2026 give the per-event beam `B_ℓ(σ) = exp[−ℓ(ℓ+1)σ²/2]`
(arXiv:2603.13053, Eq. 68) and state the assumptions behind using it: Gaussian
posteriors, and MAP positions Gaussian-distributed about the true positions;
taking the posteriors themselves as the map adds a second convolution and
"doubly" suppresses small scales [src: Sect. V.1]. Radial errors enter through
an effective window `φ(d_L)` that marginalises the bin edges over the
distribution of `Δln d̂_L` within the bin (Eq. 97) [src: Sect. V.3].

### Step 5. Model the signal
<!-- key: step-5-model-the-signal -->

Three model routes are in use.

1. **Analytic Limber** (Oguri 2016, arXiv:1603.02356). The observed distance is
   log-normal about the true one with `σ_lnD` (Eqs. 1–2; 0.05 assumed for an
   Einstein-Telescope-like network) and is lensed, `D = D̄ μ^{−1/2} ≈ D̄(1 − κ)`
   (Eq. 3). A distance bin has selection
   `S_i(z) = ½[erfc x(D_i,min) − erfc x(D_i,max)]` (Eq. 6), so the projected GW
   overdensity is `∫ dz [W^s_i δ_GW + W^t_i κ]` (Eq. 8) with a lensing kernel
   `T_i(z)` (Eq. 9). The cross-spectrum has a clustering term
   `C^{s_i g_j} = ∫ dz W^s_i W^g_j (H/χ²) b_GW b_g P_m((ℓ+½)/χ; z)` (Eq. 19)
   and a lensing term (Eq. 20) that correlates well-separated bins [src:
   Sects. II.1–II.4]. The lensing term "can make dominate contributions to
   correlation signals, because the convergence contains accumulated
   information along the line-of-sight" [src: Sect. II.2].
2. **Ratio to the measured galaxy auto-spectrum** (Mukherjee et al. 2022):
   `C^{GW g}_ℓ(z) = [b_GW(z)/b_g(z)] C^{gg}_ℓ(z)` (arXiv:2203.03643, Eq. 8), with
   `b_g` from the galaxy auto-spectrum (their App. A) and `b_GW(z) = b_GW (1+z)^α`
   [src: Sect. II].
3. **Simulation template rescaled in redshift** (Ferri et al. 2025; de Matos
   et al. 2025). Galaxy and siren mocks are made once in a fiducial cosmology
   (GLASS lognormal light cones); for another cosmology the theory is
   `C^{gb}_ℓ(z_j, D_i, θ) = Σ_{z_λ ∈ z(D_i, θ)} C^{gb}_ℓ(z_j, z_λ, θ_fid)`, a sum
   over thin fiducial redshift bins that fall in the distance bin
   (arXiv:2412.00202, Eq. 15) [src]. The justification is the Limber limit
   (Eq. 17): the cross-spectrum is proportional to
   `δ_D[χ(z_g, θ) − χ(D_L, θ)]`, so distance parameters (mainly H0 and Ω_m)
   set the peak position and everything else, biases included, sets the
   amplitude [src: Sect. 2.2]. Ferri et al. give the reason for the shortcut:
   a thousand GLASS realisations per point of parameter space take "several
   hours", against about 10⁴ points for an MCMC [src: Sect. 2.2]. de Matos et al.
   rescale the galaxy redshift bins rather than the distance bins, "more robust
   against the density profiles of each GW event since there are very few GW
   events versus an abundant numbers of galaxies", and neglect the cosmology
   dependence of the spectrum shape as sub-leading [src: arXiv:2512.15380,
   Sect. II, footnote 2]. Their fiducial is H0 = 67.36, Ω_m = 0.3153 [src].

### Step 6. Treat the biases
<!-- key: step-6-treat-the-biases -->

The amplitude depends on `b_g b_gw σ8²`. de Matos et al. take `b_gw(1+z)` with
`b_gw` free, read `b_g (σ8/σ8^fid) = 0.85 ± 0.13` from the amplitude of the
galaxy auto-spectrum against the simulations, and fix `σ8 = 0.8111 ± 0.0060`
from the CMB [src: arXiv:2512.15380, Sects. II, IV]. In their likelihood
`b_gw` only multiplies the template (made with `b_gw = 1`), on the argument
that for Gaussian fields the covariance depends negligibly on the bias of the
much sparser field [src: Sect. II]. `b_gw` is "the mean GW bias of the
particular sample", for which "bias stochasticity can be significant" [src:
Sect. II]. Mukherjee et al. 2022 sample `b_GW` on U[0.1, 6] and `α` on
U[−2, 2] [src: arXiv:2203.03643, Sect. IV].

### Step 7. Build the covariance and the likelihood
<!-- key: step-7-build-the-covariance-and-the-likelihood -->

All three use a Gaussian likelihood in the data vector of cross-spectra
(arXiv:2512.15380, Eq. 3; arXiv:2203.03643, Eqs. 6–7; arXiv:2412.00202,
Eq. 8) [src]. The covariance differs:

| Choice | Form | Analysis | Stated reason | Place read |
|---|---|---|---|---|
| Analytic, diagonal | Gaussian `(C^XX + n^X)(C^YY + n^Y)` structure over `(2ℓ+1) f_sky Δℓ` (Eq. 4); only the diagonal kept | Mukherjee et al. 2022 | small number of sources; off-diagonal terms "will be appropriate" with more | arXiv:2203.03643, Sect. II |
| Analytic, full | `Cov[C^ij, C^mn] = (4π/Ω_s) δ_ℓℓ' / ((2ℓ+1)Δℓ) × (C̃^im C̃^jn + C̃^in C̃^jm)` (Eq. 21), `C̃` including shot noise (Eq. 22) | Oguri 2016 (Fisher) | Gaussian statistics | arXiv:1603.02356, Sect. III.2 |
| Hybrid | mean `Γ_ℓ` from 1000 simulations, Gaussian Fisher form (Eq. 10); auto-spectra signal marginalised by keeping only their noise before inversion (Eq. 11) | Ferri et al. 2025 | for `ℓ_max = 100` and about 150 radial bins the covariance has about 10¹⁰ entries and would need "millions of simulations" | arXiv:2412.00202, Sect. 2.1 |
| Sample covariance from constrained simulations | almost 6000 simulations of "the same" two events placed in random hosts; simulations with an event more than 5% in the mask rejected | de Matos et al. 2025 | with two events the cross-spectrum is not Gaussian; the total number of sirens is fixed, not Poisson | arXiv:2512.15380, App. A, App. B |

### Step 8. Test for a detection, then infer
<!-- key: step-8-test-for-a-detection-then-infer -->

de Matos et al. cross galaxy and GW maps from different simulations to build
a null (uncorrelated) distribution of `Δχ²` between "signal" and "noise"
models, fit Fréchet distributions to it, and read a p-value for the data:
6.7 × 10⁻⁴ (3.4σ two-sided) for GW190814 alone, 1.9 × 10⁻⁹ (5.9σ) with
GW170817 added, over all bin pairs and multipoles together [src:
arXiv:2512.15380, Sect. IV]. Inference then runs MCMC with flat priors
H0 ∈ [20, 120] and `b_gw` ∈ [0, 10]: H0 = 53 (+31/−18) with GW190814 alone
and 67 (+18/−15) with both (68% highest-density), `b_gw < 6.2` and `< 4.3`
(95%); relative to galaxies `b_gw/b_g < 8.1` and `< 5.7`, a ratio that does
not depend on `σ8` [src: Sect. IV]. H0 and `b_gw` act "almost transversally"
(peak position against amplitude); they correlate because the peak redshift
sets the number of galaxies at the peak, and the contour is triangular
because the signal-to-noise scales with `b_gw` [src: Sect. IV].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Cross-correlation or catalogue method
<!-- key: cross-correlation-or-catalogue-method -->

- **Formal relation.** The cross-correlation method "is an extension of the
  angular part of the galaxy catalog method in which we effectively
  marginalize over all possible realizations of the unknown galaxy field,
  jointly adding information from galaxy–galaxy clustering" [src: Cheng &
  Gair 2026, arXiv:2603.13053, abstract]. In the catalogue method clustering
  enters only along radial lines of sight; the cross-correlation uses 3D
  clustering and not the galaxies along the line of sight at the GW position
  [src: arXiv:2512.15380, Sect. V, App. B].
- **Incompleteness.** Ferri et al. removed every true host from the mocks
  and found no significant loss, because about 99% of their O5 events have
  `ΔΩ > 1` deg², about 15 Mpc radius at `z = 1` [src: arXiv:2412.00202,
  Sect. 4.2]. In the de Matos simulations hosts are drawn from the complete
  mock and need not survive the selection [src: arXiv:2512.15380, Sect. V].
- **Host weighting.** Not used: all galaxies are equally likely hosts
  (`b_gw/b_g = 1` fiducial); the link to galaxy properties is carried by
  `b_gw` instead, at the cost of no luminosity-weighting gain [src:
  arXiv:2512.15380, App. A, Sect. V].
- **Independence of information.** With GWTC-3 the cross-correlation H0 comes
  "only from the galaxy catalog", whereas the LVK dark-siren values are driven
  by the mass spectrum [src: arXiv:2512.15380, Sect. V]. Combining with the
  multi-peak spectral result, neglecting correlations, gives 68 (+16/−8)
  [src: Sect. IV]. A study of the covariance between the methods is "underway"
  [src: Sect. V].

### Few events or many
<!-- key: few-events-or-many -->

The two method papers disagree on when the method pays off. de Matos et al.
call it a "common misconception" that many events are needed, an intuition
from auto-correlations; the detection comes from the many GW–galaxy pairs
and narrow tomographic bins [src: arXiv:2512.15380, Sect. II, App. B, Sect. V].
They project about 4% on H0 from 100 events with GW190814-like sky maps,
using signal-to-noise `∝ √N̄_gw` at fixed resolution [src: Sect. V;
**forecast**]. Cheng & Gair "remain pessimistic about the cross-correlation
method until these next generation detectors are online, due to its implicit
requirement of large-number statistics" [src: arXiv:2603.13053, abstract].
A referee should ask which statistic (cross only, or with autos) and which
covariance a projection uses.

### Analytic, measured or simulated template
<!-- key: analytic-measured-or-simulated-template -->

| Route | Assumes | Buys | Costs | Place read |
|---|---|---|---|---|
| Analytic Limber (Oguri) | linear P(k), Limber, log-normal distance error, lensing term | full model including lensing and Ω_m, `w` | Limber breaks for thin bins (Cheng & Gair, below) | arXiv:1603.02356, Sect. II |
| Measured `C^gg` ratio (Mukherjee 2022) | linear bias ratio, non-overlapping bins | no theory for galaxy clustering | galaxy shot noise enters; overlapping photo-z bins break the independence assumption | arXiv:2203.03643, Sects. II, IV |
| Simulation rescaled in z (Ferri; de Matos) | peak position set by the Hubble diagram only | photo-z, mask and sparse-sample statistics carried by mocks | one fiducial cosmology; shape dependence neglected | arXiv:2412.00202, Sect. 2.2; arXiv:2512.15380, Sect. II |

Tests of the template route on ET+2CE mocks [src: arXiv:2412.00202, Sect. 4.2]:
data generated at Planck 2018 (H0 = 67.4, Ω_m = 0.315) analysed with the
fiducial template (H0 = 70.0, Ω_m = 0.3; Eq. 19) recover H0 = 67.41 ± 0.42,
Ω_m = 0.315 ± 0.011; switching HALOFIT off in the template leaves the result
unchanged; ignoring lensing magnification entirely gives
H0 = 69.87 (+0.50/−0.49), Ω_m = 0.3010 ± 0.0098, against 69.99 ± 0.42 and
0.301 ± 0.010 in the baseline (their Table 1).

### Adding the galaxy auto-spectrum
<!-- key: adding-the-galaxy-auto-spectrum -->

On 2 ET + 1 CE mocks (233 499 BBH in two years, SNR ≥ 25, local rate 20
Gpc⁻³ yr⁻¹), cross-only gives 1% on H0 and 5% on Ω_m; the full 3×2pt
(siren–galaxy, galaxy–galaxy, siren–siren) gives 0.5% and 1% [src:
arXiv:2603.13053, Sects. VII.1.3, VIII]. The galaxy autos introduce a ≈ 2σ bias
on Ω_m, removed by a first-order scale-dependent bias correction; candidate
causes are spectral leakage, lognormal non-Gaussianity and the Limber
approximation for thin bins. The galaxy auto has total SNR 800 against 30
for the cross, so its precision "can often approach or exceed unmodeled
systematics"; the cross-only posteriors are unbiased [src: Sect. VIII].

### Bin widths and redshift prior range
<!-- key: bin-widths-and-redshift-prior-range -->

Mukherjee et al. 2022 varied `Δℓ` (5, 15), `Δz` (0.05, 0.1; about 1.5 and 3
times the WISE×SuperCOSMOS photo-z error) and the upper edge `z_max` of the
flat siren-redshift prior (0.5, 2; 4 checked) [src: arXiv:2203.03643,
Sect. IV]. Dark-only medians range from 67.5 to 82.4 with no detected signal
(Table 1). Narrower `Δz` enlarges the errors because photo-z kernels overlap
and violate the assumption of uncorrelated neighbouring bins; larger `z_max`
adds prior volume at high H0 where the catalogue has no galaxies [src:
same]. No sensitivity was found to the galaxy bias within its errors, a ×4
covariance, S8 = 0.832 or 0.75 and H0 = 67 or 74 in the galaxy-bias fit, or a
stricter star–galaxy cut (`p_gal > 0.67`) [src: same].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Event cuts | SNR ≥ 11, `ΔΩ ≤ 30` deg² (68.3%) → 8 events; `f_sky ≈ 2%` | GWTC-3 × 2MPZ/WSC | arXiv:2203.03643 | Sect. III |
| Multipoles | `ℓ ≤ 30`, `Δℓ` = 5 or 15, first bin dropped | same | arXiv:2203.03643 | Sect. II |
| Priors | H0 U[20, 120]; Ω_m U[0.1, 0.4]; `b_GW` U[0.1, 6]; `α` U[−2, 2]; `z` U[0, z_max] | same | arXiv:2203.03643 | Sect. IV |
| Pixels and bins | `nside = 32`; `Δz = 0.01` (÷3 at `z < 0.02`); `|b| > 20°` | GWTC-3 × GLADE+ | arXiv:2512.15380 | Sect. III |
| Multipoles | centres 14–69, `Δℓ = 5`; `ℓ_max = 180°/√(Ω_90/π)` | same | arXiv:2512.15380 | Sect. III |
| Covariance | ≈ 6000 constrained simulations | same | arXiv:2512.15380 | App. A |
| Detection | 3.4σ (GW190814), 5.9σ (+ GW170817), p from Fréchet fit to null Δχ² | same | arXiv:2512.15380 | Sect. IV |
| `b_g σ8/σ8^fid` | 0.85 ± 0.13 from galaxy auto amplitude | same | arXiv:2512.15380 | Sect. IV |
| GW bias | `b_gw < 4.3` (95%); `b_gw/b_g < 5.7` | same | arXiv:2512.15380 | Sect. IV |
| Peak + bright | H0 = 72 ± 11 (GW170817 as bright siren with the GW190814 peak siren) | same | arXiv:2512.15380 | Sect. IV |
| Template simulations | 1000 GLASS realisations per configuration; 50 distance bins over `0 < z < 2` | Ferri forecasts | arXiv:2412.00202 | Sects. 2.2, 4.1 |
| Event counts | 377 (LVK O5, 3 yr, 80% duty), 54 991 (LVK+ET, 5 yr), 73 260 (ET+2CE, 5 yr); SNR > 12; `ι` within 5° of face-on removed | Ferri forecasts | arXiv:2412.00202 | Sect. 3.1 |
| Forecast H0 | 70.4 ± 3.0 (O5, Ω_m fixed); 69.96 ± 0.67 (LVK+ET), 69.99 ± 0.42 (ET+2CE), ΛCDM; **forecast** | Ferri | arXiv:2412.00202 | Table 1 |
| Forecast, 2ET+1CE | 1% H0, 5% Ω_m (cross only); 0.5%, 1% (3×2pt); **forecast** | Cheng & Gair | arXiv:2603.13053 | Sect. VIII |
| Original Fisher | `σ(h)` = 0.016 (`ℓ_max` = 100), 0.007 (300); `σ_lnD = 0.05`; 6 distance × 12 redshift bins, `0.3 < z < 1.5`; **forecast** | Oguri 2016 | arXiv:1603.02356 | Sect. III.2, Table 1 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **No signal, prior-shaped posterior.** With eight GWTC-3 events and a shallow
  photometric catalogue the cross-spectrum is consistent with zero in every
  bin, and the H0 posterior is "uninformative" and bimodal [src:
  arXiv:2203.03643, Sect. IV]. Test: report a detection significance from
  uncorrelated simulations before quoting H0 (arXiv:2512.15380, Sect. IV).
- **Null tests.** Random galaxy catalogues with the data `n(z)`, and with
  constant `n(z)`, through the same mask must give no H0 constraint [src:
  arXiv:2203.03643, App. C].
- **Overlapping photo-z bins.** Bins narrower than the photo-z error break the
  bin-independence assumption of a diagonal covariance [src: arXiv:2203.03643,
  Sect. IV]. Test: vary `Δz` around the photo-z width; or carry bin-to-bin
  correlations in the covariance, as Ferri et al. require for thin bins [src:
  arXiv:2412.00202, Sect. 2.1].
- **Double smoothing of the GW map.** Using the localisation posteriors as the
  map convolves twice when MAP points scatter about the truth [src:
  arXiv:2603.13053, Sect. V.1]. Test: forward-model the map construction in
  mocks, as the constrained simulations of arXiv:2512.15380 do.
- **Mask and event position.** Events falling in the mask in simulations
  inflate the covariance; de Matos et al. reject such realisations [src:
  arXiv:2512.15380, App. A]. Mask-induced multipole coupling sets `Δℓ` [src:
  same, Sect. III; arXiv:2412.00202, Sect. 2.1].
- **Detector anisotropy.** The antenna patterns produce artificial siren
  anisotropies at their angular scales; correctable [sec: arXiv:2502.00239,
  Sect. 2.3]. Not simulated by de Matos et al. because with two events shot
  noise dominates [src: arXiv:2512.15380, App. A]. Ferri et al. build the
  observed-sky selection from detector-frame histograms; the LVK O5 network
  shows a deficit of events along the celestial equator [src:
  arXiv:2412.00202, Sect. 3.2.1].
- **Lensing magnification.** Shifts the correlation peak to lower galaxy
  redshift through the asymmetry of the convergence PDF, a bias "if not
  properly taken into account" in next-generation data [src:
  arXiv:2412.00202, Sect. 3.2.3]. Test: template with and without
  magnification (Sect. 4.2).
- **Peculiar velocities.** Not included in the first detection; expected
  negligible for galaxies at its bin sizes, with an H0 shift from distance
  aberration below the quoted error [src: arXiv:2512.15380, Sect. IV].
- **Mass-spectrum dependence of `d_L–z`.** "No systematic studies" for the
  cross-correlation; an earlier paper argues it negligible with current data
  [sec: arXiv:2502.00239, Sect. 2.3].
- **Mismodelled galaxy clustering at small scales.** Biases Ω_m when galaxy
  autos are added [src: arXiv:2603.13053, Sect. VIII]. Test: compare cross-only
  and 3×2pt posteriors.

## Reading list
<!-- key: reading-list -->

- Foundation: Oguri 2016, arXiv:1603.02356 — Limber model with GW selection
  window and lensing term; Gaussian covariance; first Fisher forecast.
- Method: Mukherjee et al. 2020, arXiv:2007.02943 — 3D likelihood with
  `b_GW(z)` as nuisance and the localisation smoothing scale `k_eff`.
- Method: Bera et al. 2020, arXiv:2007.04271 — clustering-redshift version
  (mean redshift per distance bin, then a Hubble-diagram fit); robustness to
  incompleteness on N-body mocks.
- Application: Mukherjee et al. 2022, arXiv:2203.03643 — first application to
  GWTC-3; robustness table on bin widths and `z_max`; random-catalogue null.
- Method/forecast: Ferri et al. 2025, arXiv:2412.00202 — redshift-rescaled
  simulation template, hybrid covariance, lensing and non-linear tests.
- Application: de Matos et al. 2025, arXiv:2512.15380 — first detection;
  constrained-simulation covariance; Fréchet-fitted null distribution.
- Critique/method: Cheng & Gair 2026, arXiv:2603.13053 — relation to the
  catalogue method, beam and radial windows, pessimism for current detectors.
- Review: Palmese & Mastrogiovanni 2025, arXiv:2502.00239, Sect. 2.3 — list of
  modelling ingredients (n(z), bias, magnification, evolution bias, antenna
  pattern).

## Not verified
<!-- key: not-verified -->

- The antenna-pattern correction papers (Cigarrán Díaz & Mukherjee 2022;
  Afroz & Mukherjee 2024) and the GW-bias papers (Scelfo et al., Libanore et
  al., Peron et al., Dehghani et al., Zazzera et al.) are named in
  arXiv:2502.00239, Sect. 2.3; not read, no identifier recorded.
- The paper arguing mass-spectrum effects negligible for the cross-correlation
  (cited as Mukherjee 2022 in arXiv:2502.00239) was not identified.
- The full likelihood of Cheng & Gair (their Eqs. 102 and 105) and their
  appendix on cross shot noise were not read.
- The body of Pan et al. 2025 (arXiv:2510.19931) and the GW–HI intensity-mapping
  variant (Scelfo et al.) were not read.
- Mukherjee et al. 2022, Eq. 4 is printed with an apparent typo in the
  rendering (the `C^XY` term is not squared); the standard Gaussian form is
  given above from Oguri 2016, Eq. 21.
