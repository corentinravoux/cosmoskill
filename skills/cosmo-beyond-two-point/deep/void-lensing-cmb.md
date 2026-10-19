# Lensing by voids (shear and CMB convergence) — cosmo-beyond-two-point dossier

Scope: how a stacked void-lensing measurement is built (void sample and
finder for lensing, rescaled stacking, ΔΣ or κ estimator, random-point
subtraction, covariance by analytic formula, random maps or jackknife,
profile or template fit, what A_κ and b_Vg mean), and how to choose between
2D and 3D voids, rescaled and unrescaled stacks, profile models and
simulation templates; void ISW is left to the sibling skill.
Snapshot: 2026-10-18.
From: Cai & Neyrinck 2025, Sects. 5 (gravitational lensing by voids) and 6
(imprints on the CMB).

Already in L2, not repeated here: the one-paragraph description and status
(`physics-and-methods.md#void-lensing`); the headline UNIONS and DESI Legacy
values (`results.md#void-lensing`); the photometric-redshift and sparseness
matching that removed "lensing is low" (`systematics.md#mask-selection-and-photo-z`);
bias conversion (`systematics.md#bias-conversion`); Euclid and other
forecasts (`open-questions.md#forecasts-all-forecast`). Void ISW stacking,
supervoid excesses and the Cold Spot are in `cosmo-cmb-lss-cross-correlations`
(`results.md`, ISW section) and `cosmo-tensions-anomalies`.

## How it is done
<!-- key: how-it-is-done -->

Notation. R_V (or r_v) is the effective void radius, R the projected
distance from the void centre; ΔΣ(R) = Σ̄(<R) − Σ(R) is the excess surface
mass density, γ_t the tangential shear, Σ_c the critical surface density,
κ the convergence. A_κ = κ_data/κ_mock is the amplitude of the data profile
relative to a simulated template of fixed shape. b_Vg is the ratio of the
void–galaxy to the void–matter profile. "Void-in-void" and "void-in-cloud"
denote voids in large-scale underdense and overdense surroundings.

### Step 1. Choose a void sample suited to lensing
<!-- key: step-1-choose-a-void-sample-suited-to-lensing -->

Lensing measures the projected matter profile, so the finder determines
both the signal-to-noise and what "the profile" means.

| Sample | Finder and settings | Stated reason | Place |
|---|---|---|---|
| BOSS LOWZ/CMASS voids × UNIONS shear | REVOLVER after RSD-removing reconstruction (β = 0.37), circumcentre (largest empty sphere); no radius cut, voids binned by radius in 10 h⁻¹Mpc steps for the void–galaxy model | the radius cut of the RSD analysis is not needed for lensing | arXiv:2507.13450, Sect. 2.3, 3.4.2 |
| DES Y3 redMaGiC × Planck κ | 2D finder: 15 slices of 100 h⁻¹Mpc at 0.15 < z < 0.8, Gaussian smoothing σ = 10 h⁻¹Mpc, centre at least 30% underdense, R_v from annuli until mean density, R ≳ 20 h⁻¹Mpc | slice ≈ photo-z scatter of LRGs; the smoothing keeps voids "which carry most of the lensing signal"; the density threshold and radius cut remove spurious voids | arXiv:2203.11306, Sect. 2.3 |
| DESI Legacy DR9 LRG × Planck κ | REVOLVER (ZOBOV), 3D, photo-z; centre = circumcentre of the four lowest-density cells; 0.35 < z < 0.95; split by λ_v = δ̄_v (R_v/1 h⁻¹Mpc)^1.2 into (−∞, −5], (−5, 5], (5, ∞) | 3D voids chosen to address earlier tensions involving 3D voids and to limit spurious signals from void alignments; λ_v separates void-in-void from void-in-cloud | arXiv:2412.02761, Sect. 3.2, 3.2.1 |
| DES SV | 2D slices of at least twice the photo-z scatter; void counts within 20% of spectroscopic ones for all sizes | photometric line-of-sight errors of about 50 h⁻¹Mpc erase many 3D voids | arXiv:1605.03982, abstract |
| SDSS DR7 LRG | 2D holes in slices of a volume-limited sample, about 20 000 voids with 15–55 h⁻¹Mpc radii at 0.16–0.37 | algorithm "designed to maximize the lensing signal" | arXiv:1404.1834, abstract |

Photometric 2D voids are preferentially elongated along the line of sight,
which raises their lensing and ISW signal; 2D definitions do slightly better
than 3D ones for lensing in simulations, although 3D ZOBOV voids also give
detections [src: arXiv:2203.11306, Sect. 2.3].

### Step 2. Stack in rescaled radius
<!-- key: step-2-stack-in-rescaled-radius -->

Single voids are undetectable, so sources (or κ pixels) behind all voids are
combined. Bins are scaled by each void's radius, because fixed bins in Mpc
put the walls of small voids inside the underdensity of large ones and
wash the profile out [src: arXiv:2507.13450, Sect. 3.1].

- **Shear.** ΔΣ(R/R_V) = Σ_L Σ_S w_LS γ_t,LS ⟨Σ_c⁻¹⟩⁻¹ / Σ_L Σ_S w_LS
  (arXiv:2507.13450, Eq. 7), with ⟨Σ_c⁻¹⟩ averaged over the source n(z)
  (Eq. 6; UNIONS had no per-source photo-z, so the full n(z) is integrated)
  and the shape-noise-optimal weight w_LS = ⟨Σ_c⁻¹⟩² w_S (Eq. 8), which
  down-weights sources physically close to the lens [src: Sect. 3.1].
  14 radial bins [src: Sect. 3.2].
- **CMB κ, image stack.** For each void a square patch of side five void
  diameters is cut with a gnomonic projection, resampled to 512 × 512
  pixels; mask patches are stacked alongside and divide the κ stack. The
  mean κ of the masked map is non-zero and voids overlap, so the bias is
  estimated from pixels within 5 r_v of the voids, weighted by how often each
  pixel is used. Profile: 25 bins of 0.2 r_v to 5 r_v [src: arXiv:2412.02761,
  Sect. 3.3]. The DES Y3 analysis uses 16 bins of 0.3 R_v [src:
  arXiv:2203.11306, Sect. 2.5]. The Planck map is smoothed with a 0.5° FWHM
  Gaussian [src: arXiv:2412.02761, Sect. 3.4].

### Step 3. Subtract randoms (shear)
<!-- key: step-3-subtract-randoms-shear -->

Tangential shear around random points removes additive shear systematics.
Because bins scale with R_V, randoms need radii and redshifts, and they must
reproduce the edge selection (voids touching the boundary are removed,
favouring small voids near edges). Randoms are therefore drawn void by void
from the 1000 Patchy void catalogues, mixing mocks so that void clustering is
removed, 30 catalogues per data set [src: arXiv:2507.13450, Sect. 3.2]. The
random signal was 10–20% of the void signal, about 4 × 10⁻⁵ in shear, and
larger for mock voids than for uniform random points, which the authors
attribute to boundary selection; the mean of the 30 is subtracted and their
covariance /30 is added [src: Sect. 3.2]. Subtraction also makes the
analytic covariance of Step 4 valid, since it then correlates two mean-zero
fields [src: Sect. 3.3].

### Step 4. Build the covariance
<!-- key: step-4-build-the-covariance -->

- **Analytic Gaussian (shear).** Starting from the void-lensing formula of
  Krause et al. 2013,
  Cov[γ_t(θ1), γ_t(θ2)] = (4π f_sky)⁻¹ ∫ ℓ dℓ/2π Ĵ2(ℓθ1) Ĵ2(ℓθ2)
  {[C_VV + 1/n_V][C_κκ + σ_ε²/n_g] + C_Vκ²}
  (arXiv:2507.13450, Eq. 9), the C_VV and C_Vκ terms are shown to be
  subdominant (App. A), leaving C_κκ/n_V plus the measured diagonal shape
  noise (Eq. 11), with σ_ε = 0.34 and a linear P(k) in the Limber integral
  (Eq. 12). The C_κκ/n_V term dominates the large-scale part because sparse
  LRG voids at low redshift give bins up to about 8° across, where line-of-
  sight structure is likely [src: Sect. 3.3]. Stated as the first analytic
  covariance used in a void-lensing data analysis, validated against the
  30-random empirical covariance [src: Sect. 3.2, 3.3].
- **Random κ maps (CMB).** 1000 Gaussian realisations with the measured
  Planck C_ℓ^κκ divided by f_sky ≈ 0.66 (first-order mask correction,
  "reliable" only near f_sky = 1; a mode-coupling correction is recommended
  for smaller areas), n_side = 512, smoothed and masked like the data, then
  stacked on the *real* void positions to keep void clustering; Hartlap
  factor with 25 bins, about 2.6% on the covariance. A jackknife over voids
  changed the errors by less than 1.5% per bin [src: arXiv:2412.02761,
  Sect. 3.4, Eqs. 12–13, 16]. The mock template gets its own covariance,
  mean within-realisation covariance plus realisation scatter (Eq. 14).

### Step 5. Fit
<!-- key: step-5-fit -->

- **Profile model (shear).** Σ(R) is the Abel projection of ρ(r)
  (arXiv:2507.13450, Eq. 17) and ΔΣ follows from Eq. 16. The HSW profile
  δ(r) = δ_c [1 − (r/r_s1)^α]/[1 + (r/r_s2)^β] (Eq. 18; β is a slope here)
  is used with r_s2 freed (five parameters). With four parameters the fits
  gave α < 1 and δ_c = −1, a concave centre never seen before, blamed on the
  few sources in the inner bins; the five-parameter fit gives α ≥ 1 and
  δ_c > −1 [src: Sect. 3.4.1]. Priors: α ≥ 1, and a rejection of profiles
  denser than the small-void best fit at 5 R/R_V, because α ≈ β gave
  constant density to the largest scales [src: Sect. 3.4.3]. Significance:
  Δχ² = χ²_0 − χ² against a null model, read as χ² with five degrees of
  freedom (Wilks) [src: Eqs. 22–23].
- **Bias in voids.** The void–galaxy correlation measured in reconstructed
  space around the same voids, averaged with the lensing-weighted void-size
  distribution, is fitted to ΔΣ with one free b_Vg [src: Sect. 3.4.2].
  Result: b_Vg/b_g = 1.36 ± 0.27 against the large-scale bias of the same
  samples from an external analysis; consistent with the up-to-25% excess
  expected from the void-finding selection effect, not significant [src:
  Sect. 4.3]. Excluding bins below 0.5 R/R_V pushed b_Vg to about 3 with
  errors up to four times larger, so the inner bins were kept [src: Sect. 4.3].
- **Template fit (CMB).** A_κ minimises
  χ² = Σ (x^L − A_κ x^B)[(C^L)⁻¹ + A_κ² (C^B)⁻¹](x^L − A_κ x^B)
  (arXiv:2412.02761, Eq. 15; L data, B mocks), σ(A_κ) from Δχ² = 1; S/N is
  the largest bin-wise M_j/σ_j (Eq. 17). A_κ = 1 means agreement with the
  ΛCDM mock that defines the template, *at the mock's cosmology*; it is a
  consistency test, not a parameter [src: Sect. 3.4]. The template comes
  from mock catalogues with the same finder: MICE in DES (Ω_m = 0.25,
  σ8 = 0.8), Buzzard (12 combined full-sky samples) for DESI Legacy [src:
  arXiv:2203.11306, Sect. 4; arXiv:2412.02761, Sect. 4.2].

### Step 6. Match the mocks to the data before comparing
<!-- key: step-6-match-the-mocks-to-the-data-before -->

In the DESI Legacy analysis the mock photo-z errors are replaced by draws
from the data's z_spec − z_phot distribution in 75 bins of Δz = 0.01, using
the 10% of LRGs with spectra; mocks are then subsampled per Δz = 0.01 to the
data's mean galaxy separation, separately in north and south, leaving
density differences below 5% where mocks were too sparse (0.35–0.50 and
z > 0.8) [src: arXiv:2412.02761, Sect. 3.1.1, 3.1.2]. The matched template
gives A_κ = 1.016 ± 0.054 for 140 712 voids [src: Sect. 4.2, Table 3].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### 2D or 3D voids
<!-- key: 2d-or-3d-voids -->

2D slice voids maximise S/N and suit photometric data; 3D voids give a
cleaner void-in-void / void-in-cloud split and a profile that relates to the
3D void literature. On Roman-like mocks, 2D voids with rescaled profiles give
the highest S/N: about 13σ (2D) against 8σ (3D) with Planck, 22σ/13σ with SO
and 31σ/18σ with a CMB-S4-like map (**forecast**) [src: arXiv:2605.22630,
abstract]. For 3D voids a cut at two mean tracer separations removes
shot-noise voids and raises S/N; for 2D voids a radius cut only selects
angular sizes [src: Sect. 5.2.1].

### Rescaled or unrescaled stacking
<!-- key: rescaled-or-unrescaled-stacking -->

Rescaling aligns walls and maximises total S/N for a full sample;
unrescaled stacks keep the physical scale, show steep small void-in-cloud
and shallow large void-in-void profiles for 2D voids, keep the CMB noise
distribution consistent across scales, and need binning by size or type,
which costs S/N for a Roman-sized footprint of about 2000 deg² unless a joint
fit across bins is used [src: arXiv:2605.22630, Sect. 5.1.4, 5.2.1].
Unrescaled stacks can reach comparable S/N with matched filtering of the
CMB map, per the studies cited there [src: Sect. 5.2.1].

### Splitting by environment
<!-- key: splitting-by-environment -->

λ_v bins in DESI Legacy: A_κ = 0.944 ± 0.064 (S/N 16.9) for λ_v ≤ −5,
1.093 ± 0.090 (11.3) for −5 to 5, 0.975 ± 0.060 (17.0) for λ_v > 5; the two
outer bins each exceed the full-sample S/N of 14.1 [src: arXiv:2412.02761,
Table 3]. The text of Sect. 4.2 gives ±0.060 for the first bin, the table
±0.064; L2 quotes the table. In DES Y3 the deepest (δ_c < −0.6) and largest
(R_v > 35 h⁻¹Mpc) voids gave A_κ ≈ 0.56 ± 0.14 and 0.66 ± 0.15, and the
low-redshift half 0.55 ± 0.23 [src: arXiv:2203.11306, Sect. 4].

### Template or profile model
<!-- key: template-or-profile-model -->

A simulation template has fixed shape and tests one cosmology plus one
galaxy–halo model plus one photo-z model at once. A fitted HSW profile
measures the void matter profile but has no cosmological dependence written
in. The Euclid photometric forecast avoids both by keeping only large
scales: P_vm = b_v^eff P_mm with a smooth low-pass filter at
k_ref = 0.25 h Mpc⁻¹ (k ≈ 2π/r̄_v, void exclusion), Limber C_ℓ^vγ over
10 ≤ ℓ ≤ 1500 in ten equi-populated galaxy bins, a pessimistic void bias of
about −11.9 [src: arXiv:2206.14211, Sect. 2, 3, Eqs. 1–4]. Its stated
reason: no accurate model of the cosmological dependence of the void
profile exists [src: Sect. 2]. Equi-populated void bins instead of galaxy
bins worsened constraints by 10–15% [src: Sect. 5.6].

### Covariance route
<!-- key: covariance-route -->

Analytic Gaussian covariance is cheap and noiseless but drops C_VV and
C_Vκ terms that must be shown small for each sample (arXiv:2507.13450,
App. A). Random κ maps capture CMB noise, which dominates the CMB-lensing
error, but not sample variance of the void field, checked by jackknife
(arXiv:2412.02761, Sect. 3.4). On the Roman mocks the CMB noise also
dominates over large-scale structure variance [src: arXiv:2605.22630,
Sect. 4.4].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| UNIONS area used | about 3200 deg² of a planned 6250 deg² | UNIONS × BOSS | arXiv:2507.13450 | Sect. 2.1 |
| Detection | 6.2σ, stacked ΔΣ | UNIONS × BOSS | arXiv:2507.13450 | abstract |
| Random signal | 10–20% of the void signal; ≈ 4 × 10⁻⁵ in γ_t | UNIONS × BOSS | arXiv:2507.13450 | Sect. 3.2 |
| Shape noise | σ_ε = 0.34 | UNIONS | arXiv:2507.13450 | Sect. 3.3 |
| b_Vg / b_g | 1.36 ± 0.27 | UNIONS × BOSS | arXiv:2507.13450 | Sect. 4.3 |
| 2D finder | 15 slices × 100 h⁻¹Mpc; σ = 10 h⁻¹Mpc; ≥ 30% central underdensity; R ≳ 20 h⁻¹Mpc; typical R ≈ 50, max ≈ 150 h⁻¹Mpc | DES Y3 | arXiv:2203.11306 | Sect. 2.3 |
| DES Y3 voids × Planck κ | about 3600 voids; 6.6σ; A_κ ≈ 0.79 ± 0.12 vs MICE | DES Y3 | arXiv:2203.11306 | abstract |
| Voids + superclusters | 10.3σ; A_κ ≈ 0.82 ± 0.08, 2.3σ below MICE | DES Y3 | arXiv:2203.11306 | abstract |
| Earlier A_κ quoted there | DES Y1 ≈ 0.72 ± 0.17; DESI-LS voids + superclusters 0.811 ± 0.057 | as cited | arXiv:2203.11306 | Sect. 4 |
| DES Y1 | S/N ≈ 4, A ≈ 1 vs MICE; no CMB-lensing counterpart to the void ISW excess | DES Y1 × Planck 2015 | arXiv:1911.02951 | abstract |
| Stack geometry | patch side 5 diameters, 512²; 25 bins × 0.2 r_v to 5 r_v | DESI Legacy | arXiv:2412.02761 | Sect. 3.3 |
| Random maps | 1000, n_side 512, f_sky ≈ 0.66, 0.5° smoothing | DESI Legacy | arXiv:2412.02761 | Sect. 3.4 |
| Void counts | 140 712 data; 127 765 mean mock (full sky) | DESI Legacy | arXiv:2412.02761 | Table 1 |
| Combined λ_v bins | A_κ = 1.004 ± 0.072 | DESI Legacy | arXiv:2412.02761 | Fig. 12 caption |
| First CMB-lensing void detection | 3.2σ, close to ΛCDM, ZOBOV CMASS voids | BOSS × Planck | arXiv:1609.00301 | abstract |
| First shear detection | 901 SDSS DR7 voids, depression strongest at R_V | SDSS | arXiv:1309.2045 | abstract |
| SDSS 2D voids | S/N 7, interior underdensity ≈ −0.4, partially compensated | SDSS LRG | arXiv:1404.1834 | abstract |
| DES SV | 87 voids, 18–120 h⁻¹Mpc, 4.4σ | DES SV | arXiv:1605.03982 | abstract |
| Euclid void–lensing filter | k_ref = 0.25 h Mpc⁻¹, a = 1, b = 1.8, N = 3 | Euclid **forecast** | arXiv:2206.14211 | Sect. 2 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Mock template not matched to the data** in photo-z errors and
  sparseness: produced the "lensing is low" deficit (DES Y3 0.79 ± 0.12);
  the matched template gives A_κ ≈ 1 (L2). Test: compare void-size and
  redshift distributions of data and mock voids before stacking
  (arXiv:2412.02761, Fig. 6; arXiv:2203.11306, Fig. 2). The Roman-mock study
  finds the void × CMB-lensing profile much less sensitive to the mock than
  galaxy and void statistics are [src: arXiv:2605.22630, abstract,
  Sect. 5.1.4].
- **Additive shear systematics** at the 10–20% level of the void signal:
  subtract randoms that carry the edge selection, not uniform points
  [src: arXiv:2507.13450, Sect. 3.2].
- **Inner bins** have few sources or pixels and depend on the centre
  definition: they drive degenerate profile fits (δ_c = −1, α < 1) and the
  bias estimate [src: arXiv:2507.13450, Sect. 3.4.1, 4.3].
- **Masked-map mean** not removed with the void-weighted pixel average
  biases κ; a plain mean subtraction is insufficient when voids overlap
  [src: arXiv:2412.02761, Sect. 3.3].
- **Mask correction by 1/f_sky** is only first order; use a mode-coupling
  correction for small areas or for cosmological fits [src: same, Sect. 3.4].
- **Shot-noise voids** dilute the signal; 3D samples need a radius cut near
  two mean tracer separations [src: arXiv:2605.22630, Sect. 5.2.1].
- **No cosmological dependence quantified**: the forecasts state that the
  cosmology dependence of void × CMB lensing "remains to be quantified"
  [src: arXiv:2605.22630, abstract]. Quote A_κ as a consistency test.

## Reading list
<!-- key: reading-list -->

- Review: Cai & Neyrinck 2025, arXiv:2503.22532 — Sects. 5–6, overview of
  shear and CMB lensing by voids.
- Foundation: Melchior et al. 2014, arXiv:1309.2045 — first stacked shear
  detection, public code.
- Method: Clampitt & Jain 2015, arXiv:1404.1834 — 2D voids built for lensing.
- Method: Sánchez et al. 2017, arXiv:1605.03982 — photometric 2D finder.
- Foundation (CMB): Cai et al. 2017, arXiv:1609.00301 — first CMB-lensing
  void detection with simulations defined before looking.
- Application: Kovács et al. 2022, arXiv:2203.11306 — DES Y3 2D voids,
  template fit, the low-A_κ result.
- Application: Sartori et al. 2024, arXiv:2412.02761 — matched mocks,
  random-map covariance, λ_v split.
- Application: Martin et al. 2025, arXiv:2507.13450 — ΔΣ with mock randoms,
  analytic covariance, HSW fit, b_Vg.
- Forecast and critique: Pérez Sar et al. 2026, arXiv:2605.22630 — finder,
  stacking and mock choices on Roman mocks.
- Forecast: Bonici et al. 2022, arXiv:2206.14211 — large-scale void-lensing
  C_ℓ with a filtered P_vm.

## Not verified
<!-- key: not-verified -->

- Krause et al. 2013 (void-lensing covariance and predictions), Fang et al.
  2019 (DES Y1 3D voids), Hang et al. 2021 (DESI-LS κ), Raghunathan et al.
  2020 (unrescaled matched filter), Pollina et al. 2017 (b_Vg against void
  size), Barreira et al. 2015 (five-parameter HSW): cited through the papers
  read; not read, no identifiers recorded.
- A DES Y3 trough-and-peak bias analysis and a CSST void–lensing forecast
  found in the date-sorted search (2025-06-01 onward): titles only, not used.
- The radial range of the 14 UNIONS bins and the UNIONS–BOSS overlap area:
  not in the sections read.
- L2 quotes a void galaxy bias of 2.45 ± 0.36 from arXiv:2507.13450; this
  dossier read the ratio b_Vg/b_g = 1.36 ± 0.27 only.
