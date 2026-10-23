# ISW — cosmo-cmb-lss-cross-correlations dossier

Scope: how an integrated Sachs–Wolfe measurement is built and how its
significance is obtained — CMB map and mask, tracer bias and magnification
inputs, bandpowers, covariance from end-to-end, Gaussian or analytic
simulations, the amplitude fit and the three significance conventions,
the matched filter and blind stacking on superstructures, and the internal
ISW–lensing bispectrum — with the choices that separate the analyses.
Snapshot: 2026-10-18.
From: skill scope; Nishizawa 2014 review (arXiv:1404.5102); not a section
of the two 2022–2025 sources.

Already in L2, not repeated here: the ISW kernel and the C_ℓ^Tg template of
the unWISE analysis (`physics-and-methods.md#integrated-sachs-wolfe-effect`);
the unWISE per-sample amplitudes, map-to-map spread and b dN/dz error
(`systematics.md#isw-cosmic-variance-selection-of-structures-and`); all
measured amplitudes and their history (`results.md#cross-correlation-of-temperature-with-lss`,
`results.md#stacking-on-voids-and-superclusters`, `results.md#isw`); the
supervoid controversy (`open-questions.md#isw-from-superstructures`). Void
lensing is in `cosmo-beyond-two-point/deep/void-lensing-cmb.md`; the
lensing–ISW bias on primordial f_NL is in `cosmo-inflation-primordial`.

Symbols: T CMB temperature; g tracer overdensity; C_ℓ^Tg their angular
cross-spectrum; A_ISW measured amplitude over the ΛCDM template; d, t data
and template bandpower vectors; Cov their covariance; b(z) linear bias;
dN/dz normalised redshift distribution; s number-count slope; f growth rate;
Φ gravitational potential; λ_v, λ_c the void and supercluster observables
of Nadathur 2016; R_v void radius; TS test statistic.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Choose the route
<!-- key: step-1-choose-the-route -->

| Route | Data | Analyses read |
|---|---|---|
| Tomographic C_ℓ^Tg with a fixed template, amplitude A_ISW | full tracer field × CMB temperature, ℓ ≲ 100–300 | Krolewski 2021 (arXiv:2110.13959); Ghodsi Yengejeh 2026 (arXiv:2607.22461); Stölzner 2017 (arXiv:1710.03238); Planck 2015 XXI (arXiv:1502.01595), Sect. 3 |
| Matched filter on catalogued superstructures, templates from simulation | void and supercluster catalogue × CMB | Nadathur 2016 (arXiv:1608.08638) |
| Blind stacking with mock templates | 2D superstructures × CMB, lensing first | Hang 2021 (arXiv:2105.11936) |
| ISW–lensing bispectrum, CMB alone | T (and E) × reconstructed lensing | Planck 2015 XXI, Sect. 3.3 |

### Step 2. CMB map and mask
<!-- key: step-2-cmb-map-and-mask -->

- **unWISE** (arXiv:2110.13959, Sects. 3.2, 4): Planck 2018 SMICA, with the
  "common" temperature confidence mask apodised with a 1° FWHM Gaussian;
  the galaxy map is masked separately and corrected by an "area lost" mask
  for Gaia stars. The m = 0 modes are removed from the pseudo-C_ℓ sum
  "since the azimuthal modes of the map are most affected by Galactic
  latitude-dependent foregrounds"; the change is < 0.25σ and is validated
  on Gaussian simulations.
- **Quaia** (arXiv:2607.22461, Sects. 2.1, 2.5): Planck PR3 SMICA degraded
  to N_side = 256, with the common intensity mask binarised at coverage
  > 0.99 "to prevent boundary leakage"; the analysis mask is the
  intersection of the CMB and Quaia masks, ~24,000 deg² (low-z bin and full
  sample) and ~21,000 deg² (high-z bin), split into Galactic North and South
  as a test.
- **Five catalogues** (arXiv:1710.03238, Sect. III): Planck 2015 SEVEM by
  default, with the union of the four confidence masks, and 100, 143 and
  217 GHz maps as achromaticity checks.
- **Planck 2015 XXI** (Sect. 3.1): N_side = 64 maps; the expected signal and
  its covariance both come from 10,000 of 11,000 coherent CMB–tracer
  simulations.

### Step 3. Template: bias, redshifts, magnification
<!-- key: step-3-template-bias-redshifts-magnification -->

The template is C_ℓ^Tg for a fixed fiducial cosmology, binned like the data
(arXiv:2110.13959, Sect. 5.1). Quaia writes it with pyCCL in Limber,
C_ℓ^XY = ∫ W_X W_Y P_m((ℓ + 1/2)/χ, z) dχ/χ² (Eq. 4), the ISW kernel
W_ISW ∝ H(z) χ² [1 − f(z)] (Eq. 6) and the number-count kernel ∝ b(z) dN/dz
(Eq. 7), with CAMB + halofit, RSD omitted [src: arXiv:2607.22461,
Sect. 2.3]. The tracer bias is fixed before the ISW fit, by one of three
routes:

| Route | Analysis | Detail |
|---|---|---|
| CMB lensing cross-spectrum C_ℓ^κg | unWISE | b^eff = ∫ b dN/dz from a fit of Eq. 12 over 20 < ℓ < 1000, with the shape f(z)dN/dz from clustering redshifts; errors ≤ 3%; ℓ < 300 gives b^eff = 1.54, 2.27, 3.16 against 1.50, 2.23, 3.19 [src: arXiv:2110.13959, Sects. 3.1.2, 5.1] |
| Galaxy auto-spectrum | five catalogues | linear bias fitted in 4 bins over 10 ≤ ℓ ≤ 60 per redshift bin; variations of ~10% with binning and ℓ_max 40–80, larger than the statistical errors, so "systematics- rather [than] statistics-limited" [src: arXiv:1710.03238, Sect. VII.1] |
| Bias evolution from an earlier lensing-tomography fit | Quaia | b_0 = 1.26 times a growth-factor evolution from Piccirilli 2024; an alternative quasar bias model as a test [src: arXiv:2607.22461, Sect. 2.2] |

For one tracer bin the ISW signal is linear in b, so the fit constrains
b A_ISW and the significance barely depends on b, while A_ISW does
(arXiv:1710.03238, Sect. VII.1) [src].

Magnification enters through dN/dz alone. unWISE uses COSMOS cross-match
redshifts for it, a subdominant term (arXiv:2110.13959, Sect. 3.1.2) [src];
Quaia neglects it because the measured s = 0.404 ± 0.004 is close to 0.4,
where the term vanishes (arXiv:2607.22461, Sect. 2.2) [src]. Other
relativistic terms change the unWISE total by < 2% (< 0.3% at ℓ > 20)
[src: arXiv:2110.13959, Fig. 3 caption]. The Rees–Sciama term is about 10%
of linear ISW at ℓ ≥ 200 in the temperature auto-spectrum and further
suppressed in cross-correlation with a sparse tracer (arXiv:2607.22461,
Sect. 2.3) [src].

### Step 4. Bandpowers and covariance
<!-- key: step-4-bandpowers-and-covariance -->

| Analysis | Estimator and bins | Covariance |
|---|---|---|
| unWISE | NaMaster (MASTER) bandpowers; Δℓ = 16 over 20 < ℓ < 100, plus 7 < ℓ < 20 for Blue only; theory multiplied by the bandpower windows, checked on 100 noiseless Gaussian simulations | 300 Planck FFP10 end-to-end simulations crossed with the unWISE data, including the covariance between samples; Hartlap correction "tiny" for 5 bins; errors close to Gaussian [src: arXiv:2110.13959, Sect. 4] |
| Quaia | NaMaster; 6 logarithmic bins to ℓ_max = 300 | 2000 correlated Gaussian realisations of T and g from (C_ℓ^TT, C_ℓ^gg, C_ℓ^Tg), a power law added to C_ℓ^gg to reproduce the observed excess, Planck noise added to T, Poisson-sampled quasar counts; Hartlap factor 0.996 [src: arXiv:2607.22461, Sects. 2.4, 2.6] |
| Five catalogues | PolSpice; 4 bins over 4 ≤ ℓ ≤ 100, unweighted bin averages | PolSpice analytic covariance, block-averaged; nearly diagonal but used in full [src: arXiv:1710.03238, Sects. VI, VII.1] |
| Planck 2015 XXI | ACPS at N_side = 64 | 10,000 coherent simulations [src: Sect. 3.1] |

The ℓ_min of unWISE is set where the galaxy auto-spectrum departs from a
model fitted on smaller scales (ℓ = 7 for Blue, 20 for Green and Red); the
authors call the cut conservative, since galaxy systematics should not
correlate with CMB residuals, and lowering it to 5 for Green changes
A_ISW negligibly; ℓ_max = 100 because the signal is small beyond
[src: arXiv:2110.13959, Sect. 4].

### Step 5. Amplitude and significance
<!-- key: step-5-amplitude-and-significance -->

The amplitude is a linear fit (arXiv:2607.22461, Eqs. 9–10):

```
A_ISW = tᵀ Cov⁻¹ d / tᵀ Cov⁻¹ t ,     σ_A = (tᵀ Cov⁻¹ t)^(−1/2)
```

Three significance numbers circulate:

1. **S/N = A_ISW/σ_A** (arXiv:2607.22461, Sect. 2.6; also tabulated in
   arXiv:1710.03238 "for comparison with other works") [src].
2. **√TS with TS = χ²(A = 0) − χ²_min**, distributed as χ² with one degree
   of freedom; the five-catalogue combination gives √22.16 = 4.7σ, against
   4.0σ without redshift binning [src: arXiv:1710.03238, Sect. VII.1].
   This is the rejection of the null, not the distance from ΛCDM.
3. **Joint fit of biases, cosmology and A_ISW** ("Method 2"): auto + cross
   with Gaussian Planck + BAO priors gives TS = 22 (4.7σ); cross only, biases
   from the cross-spectra with 4–5 times larger errors, TS = 26.5 (5.1σ);
   with the full Planck + BAO likelihoods, TS = −2Δln𝓛 = 24.9 (5.0σ). The
   authors attribute the gain to the correlations between biases and
   A_ISW, which Method 1 ignores by fixing the biases; ln(Bayes factor)
   ≈ 12 in all cases [src: arXiv:1710.03238, Sect. VII.2].

**Expected significance.** For unWISE Blue an A_ISW = 1 signal would be seen
at 1/0.34 = 2.9σ, and at 3.7σ without the excess low-ℓ power of the Blue
auto-spectrum, against ~4σ expected from earlier forecasts (an
f_sky = 0.6, 10⁸-galaxy survey to z_max = 1 with b = 1.5 was forecast at
S/N ~ 5, before the ℓ_min cut, which costs ~20%) [src: arXiv:2110.13959,
Sect. 5.1].

### Step 6. Superstructures: matched filter and blind stacking
<!-- key: step-6-superstructures-matched-filter-and-blind -->

**Matched filter** (arXiv:1608.08638, Sects. III.1–III.3) [src]:
1. Linear ISW, ΔT/T̄ = −2 ∫ a (1 − f) Φ dz (Eq. 2).
2. From the BigMD simulation, the potential at a void scales with
   λ_v ≡ δ̄_g (R_eff,v/1 h⁻¹Mpc)^1.2 (Eq. 3) and at a supercluster with
   λ_c ≡ δ̄_g (R_eff,c/1 h⁻¹Mpc)^1.6 (Eq. 5); profiles
   Φ̄ = Φ_0/[1 + (r/r_0)²] (voids, Eq. 4) or with a free exponent α
   (superclusters, Eq. 6), all coefficients calibrated on simulation.
   Voids with λ_v > 0 and superclusters with λ_c < 0 are dropped, as they
   do not give an ISW shift of the right sign, leaving 2445 voids and 29,866
   superclusters.
3. Filter ψ^MF_ℓ0 = κ y_ℓ0/C_ℓ with κ⁻¹ = Σ y_ℓ0²/C_ℓ (Eq. 11), unbiased for
   the template amplitude T_0 and of minimum variance, C_ℓ being the
   Planck map spectrum.
4. Each template has expected S/N ≲ 0.1, so structures are binned in λ and
   stacked.
5. Errors from 2000 mocks: random CMB skies at the positions of randomly
   drawn QPM mock catalogues, which capture both CMB and catalogue
   variance.
6. "We constructed the matched filters entirely based on calibration with
   simulations and before any reference to the CMB data. No free parameters
   remain in our analysis, so it is free of any a posteriori bias."

**Blind stacking** (arXiv:2105.11936, Sects. 3.1–3.3, 5.2) [src]:
1. Freeze the superstructure selection on the galaxy maps and on the stacked
   CMB lensing signal, which has much higher S/N; only then stack the
   temperature.
2. 2D finder: Gaussian smoothing σ = 20 h⁻¹Mpc/d(z); void centres among the
   lowest 10% of smoothed pixels (δ_* ≈ −0.2); radius where the shell
   density first turns positive (R from 1 to 300 h⁻¹Mpc in steps of 2);
   clusters from the densest 5% of the inverted map; voids with less than
   70% of their area in the footprint dropped.
3. Rotate each map to the structure centre, rescale by R_v to 3R_v, divide
   the stacked map by the stacked mask (Eq. 14); ℓ < 10 removed from data
   and simulated ISW maps, which mis-simulate the largest modes.
4. Covariance three ways — 1000 random CMB maps at the data positions,
   1000 random position sets on the real CMB, jackknife over structures —
   in close agreement; Hartlap with p = 15.
5. A_ISW = ΔT_data/ΔT_th against simulated light-cone templates.

### Step 7. ISW–lensing bispectrum
<!-- key: step-7-isw-lensing-bispectrum -->

The lensing potential correlates with the large-scale ISW temperature,
giving a squeezed bispectrum; in polarisation the correlation comes from
lensing × reionisation E modes, the direct ISW term being negligible
(arXiv:1502.01595, Sect. 3.3) [src]. Planck 2015 amplitudes (SMICA):
1.06 ± 0.33 (ISW-paper estimator, Gaussian simulations), 0.90 ± 0.28
(lensing-paper estimator, FFP8), 0.82 ± 0.27 (binned bispectrum, T + E);
temperature only 0.79 ± 0.28 (KSW), 0.72 ± 0.26 (modal), 0.59 ± 0.33
(binned). On 100 FFP8 simulations all bispectrum estimators average ≈ 0.85,
so error bars were divided by each estimator's simulated mean; KSW and modal
correlate at ~95%, each with binned at ~80%, the two lensing-reconstruction
estimators at ~80%, the two classes at 60–70%. A = 0 is excluded at ≈ 3σ
[src: Sect. 3.3].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Where the bias comes from
<!-- key: where-the-bias-comes-from -->

The auto-spectrum route uses the tracer's largest scales, which carry its
imaging systematics; the lensing route uses a second CMB-based spectrum on
smaller scales (ℓ up to 1000), where the measured bias is quasi-linear and
its evolution may differ from the linear one — the unWISE authors test this
with HOD-populated N-body simulations and find the shift smaller than the
dN/dz error (arXiv:2110.13959, Sect. 3.1.2) [src]. A joint fit avoids fixing
the bias at all and raised the five-catalogue significance from 4.7σ to
5.0σ (arXiv:1710.03238, Sect. VII.2) [src]. Changing the Quaia bias model
moves A_ISW from 1.69 to 2.02 at unchanged significance (arXiv:2607.22461,
Sect. 3.3) [src].

### Which simulations make the covariance
<!-- key: which-simulations-make-the-covariance -->

- End-to-end FFP10 maps include noise, systematics and foregrounds processed
  like the data, but only 300 exist (arXiv:2110.13959) [src: Sect. 3.2].
- Correlated Gaussian realisations scale to 2000 and can include the observed
  excess in C_ℓ^gg and Poisson noise; randomising only the CMB and crossing
  with the real tracer map underestimates the errors by ~10% and needs a
  correction term (arXiv:2607.22461, Sect. 2.6, after Cabré et al. 2007)
  [src].
- An analytic covariance (PolSpice) uses the model-independent errors of the
  estimator; the authors note that a model-dependent error would be more
  correct but that the difference is small for binned data
  (arXiv:1710.03238, Sect. VII.1) [src].

### Tomography
<!-- key: tomography -->

Redshift binning raised the five-catalogue significance from 4.0σ to 4.7σ,
mostly through SDSS DR12 and WISE × SuperCOSMOS, while the quasar sample was
unchanged (arXiv:1710.03238, Sect. VII.1) [src]. A joint fit to Quaia's two
bins with their cross-covariance (12 bandpowers) agrees with each bin
(arXiv:2607.22461, Sect. 3.3) [src].

### Matched filter, compensated top-hat, or selected subsamples
<!-- key: matched-filter-compensated-top-hat-or-selected -->

The matched filter is fixed by simulation before the data are seen; the
compensated top-hat of the earlier stacks has a free radius (shown for
comparison in arXiv:1608.08638, Fig. 1) [src]. Hang 2021 shows what
selection does: keeping the 10% or 50% largest-R_v structures gives
A_ISW = 0.10 ± 0.99 and 0.57 ± 0.71 for voids, 1.47 ± 0.77 and
2.59 ± 0.73 for clusters, against −0.10 ± 0.69 and 1.52 ± 0.72 for the full
samples, and the authors stress the selection is a posteriori
(arXiv:2105.11936, Sect. 5.4) [src]. The DES supervoid excess used 100 h⁻¹Mpc
slices, δ_* = −0.3, 50 h⁻¹Mpc smoothing and R_v > 100 h⁻¹Mpc; reproducing
those settings on DESI Legacy data inside the DES footprint gives 75 or 64
such voids, comparable to the original 87, and a signal consistent with
ΛCDM rather than three times it (arXiv:2105.11936, Sect. 5.3) [src].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Multipole range | 7 (Blue) or 20 (Green, Red) < ℓ < 100, Δℓ = 16 | unWISE × Planck | arXiv:2110.13959 | Sect. 4 |
| Covariance simulations | 300 FFP10 | same | arXiv:2110.13959 | Sects. 3.2, 4 |
| b^eff uncertainty | ≤ 3% (1–2% statistical) | same | arXiv:2110.13959 | Sects. 3.1.2, 5.1 |
| m = 0 removal | < 0.25σ | same | arXiv:2110.13959 | Sect. 4 |
| Bias-fit window | 4 bins, 10 ≤ ℓ ≤ 60 | five catalogues | arXiv:1710.03238 | Sect. VII.1 |
| ISW fit window | 4 bins, 4 ≤ ℓ ≤ 100 | same | arXiv:1710.03238 | Sect. VII.1 |
| Significance, Method 1 | 4.7σ tomographic; 4.0σ without bins | same | arXiv:1710.03238 | Sect. VII.1 |
| Significance, Method 2 | 4.7σ (AC + CC); 5.1σ (CC only); 5.0σ (with Planck + BAO) | same | arXiv:1710.03238 | Sect. VII.2 |
| Parameters of the joint fit | 22 (15 biases, A_ISW, six ΛCDM) | same | arXiv:1710.03238 | Sect. VII.2 |
| Bins and ℓ_max | 6 logarithmic bins, ℓ_max = 300 | Quaia × Planck | arXiv:2607.22461 | Sect. 2.5, Table 3 |
| Mocks | 2000 correlated Gaussian pairs; Hartlap 0.996 | same | arXiv:2607.22461 | Sects. 2.4, 2.6 |
| Map variation | NILC 1.63 ± 0.61; SEVEM 1.57 ± 0.61 (0.2σ) | same | arXiv:2607.22461 | Sect. 3.3 |
| North / South | 1.36 ± 0.82 / 2.32 ± 0.86 | same | arXiv:2607.22461 | Sect. 3.3 |
| ℓ_max and binning variations | A_ISW 1.30–1.74; ℓ_max = 100: 1.30 ± 0.61 | same | arXiv:2607.22461 | Sect. 3.3 |
| Per bin | 1.19 ± 0.56 (z̄ = 0.97); 2.86 ± 1.62 (z̄ = 2.10) | same | arXiv:2607.22461 | Table 3 |
| Structures kept | 2445 voids, 29,866 superclusters | BOSS CMASS, matched filter | arXiv:1608.08638 | Sect. III.3 |
| Mocks | 2000 (random CMB × QPM catalogues) | same | arXiv:1608.08638 | Sect. III.3 |
| Per-structure expected S/N | ≲ 0.1 | same | arXiv:1608.08638 | Sect. III.2 |
| Void finder | σ = 20 h⁻¹Mpc; lowest 10% (δ_* ≈ −0.2); 70% area | DESI Legacy | arXiv:2105.11936 | Sect. 3.2 |
| Stack χ² against simulation / null, all voids | 12.6 / 10.1 | same | arXiv:2105.11936 | Sect. 5.2 |
| ISW–lensing bispectrum | 0.59–1.06, errors 0.26–0.33; A = 0 excluded at ≈ 3σ | Planck 2015 | arXiv:1502.01595 | Sect. 3.3 |
| Coherent simulations | 10,000 of 11,000, N_side = 64 | same | arXiv:1502.01595 | Sect. 3.1 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Spurious large-scale tracer power.** Excess low-ℓ auto power inflates
  the variance of C_ℓ^Tg: for unWISE Blue the expected significance falls
  from 3.7σ to 2.9σ (arXiv:2110.13959, Sect. 5.1) [src]. Test: compare the
  auto-spectrum with a model fitted on smaller scales and set ℓ_min there;
  in mocks, inject the excess into C_ℓ^gg (arXiv:2607.22461, Sect. 2.4).
- **Galactic and component-separation residuals.** Test: repeat on
  Commander, NILC, SEVEM, SMICA-noSZ and single frequencies; the unWISE
  spread stays within the error (L2) and the Quaia spread is 0.2σ
  (arXiv:2607.22461, Sect. 3.3) [src]. Extragalactic emission correlated
  with the tracer (CIB, radio, tSZ) is argued to be subdominant on these
  scales but was not quantified in the parts read.
- **Underestimated errors.** Randomising only the CMB underestimates them
  by ~10% (arXiv:2607.22461, Sect. 2.6) [src]; Hang 2021 notes that random
  positions ignore the clustering of structures (pairs of clusters, few
  close voids) and so give only a rough catalogue term (arXiv:2105.11936,
  Sect. 3.3) [src].
- **A posteriori selection.** Selections on R_v or depth can double the
  predicted signal and pick up fluctuations (arXiv:2105.11936, Sect. 5.4)
  [src]. Test: fix catalogue and filter before unblinding; calibrate the
  selection on the lensing stack (Sect. 3.1).
- **Cosmic variance of a small footprint.** Inside the DES footprint the
  largest DESI Legacy voids give a mean signal closer to the excess, still
  consistent with both null and ΛCDM (arXiv:2105.11936, Sect. 5.3) [src].
- **Bias errors that are systematic.** Auto-spectrum biases move by ~10%
  with binning and ℓ_max; poor χ² in redshift tails points to catalogue
  non-uniformity (arXiv:1710.03238, Sect. VII.1) [src]. Effect on the
  significance is small, on A_ISW not.
- **Outlier bandpowers.** The Quaia spectrum has outliers at ℓ < 10 and near
  ℓ ≈ 200; changing the binning moves them, which the authors read as
  fluctuations (arXiv:2607.22461, Sect. 3.3) [src].
- **Estimator calibration in the bispectrum.** Bispectrum estimators
  average ≈ 0.85 on simulations with A = 1; the published errors are
  rescaled accordingly (arXiv:1502.01595, Sect. 3.3) [src].

## Reading list
<!-- key: reading-list -->

- Foundation: Crittenden 1995, arXiv:astro-ph/9510072 — the
  cross-correlation proposal (in L2).
- Method: Stölzner 2017, arXiv:1710.03238 — two significance methods,
  tomography gain, auto-spectrum biases, Bayes factor.
- Method: Nadathur 2016, arXiv:1608.08638 — simulation-calibrated templates
  and matched filter without free parameters.
- Application: Krolewski 2021, arXiv:2110.13959 — lensing-calibrated bias,
  FFP10 covariance, ℓ_min choice, expected versus achieved significance.
- Application: Ghodsi Yengejeh 2026, arXiv:2607.22461 — Gaussian mock
  covariance with tracer excess power, robustness grid, dark-energy
  templates.
- Application: Planck 2015 XXI, arXiv:1502.01595 — coherent simulations,
  ISW–lensing bispectrum estimators and their calibration.
- Critique: Hang 2021, arXiv:2105.11936 — blind lensing-first stacking,
  covariance comparison, attempt to reproduce the supervoid excess.
- Critique: Kovács 2018, arXiv:1811.07812 — the supervoid excess itself
  (in L2; method not read here).

## Not verified
<!-- key: not-verified -->

- The supervoid selection and compensated top-hat filter of
  arXiv:1811.07812, other than as described in arXiv:2105.11936.
- Planck 2015 XXI stacking and ISW-map results (Sects. 4–5) and the
  equations of its Sect. 3.1 estimator (not rendered).
- The CMB-map and catalogue cross-checks of arXiv:1710.03238 (its
  Sect. VIII).
- The forecast paper cited as ref. [103] in arXiv:2110.13959 was not read;
  its numbers are as quoted there.
