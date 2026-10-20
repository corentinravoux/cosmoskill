# P1D estimation: FFT and QMLE, and their corrections — cosmo-lyman-alpha dossier

Scope: how each step of a P1D measurement is carried out (continuum, noise
power, resolution, weights, masks, covariance), how the FFT and optimal
quadratic (QMLE) routes differ at each step and why each analysis chose as it
did, how corrections are derived and validated on synthetic data, and what a
user of the published DESI DR1 measurements must do.
Snapshot: 2026-10-16.
From: McQuinn 2016 review (arXiv:1512.00086), Sect. 2.1.2; Weinberg et al.
2003 review (arXiv:astro-ph/0301186), Sect. 2; DESI P1D working group
(arXiv:2505.09493, arXiv:2505.07974).

Already in L2, not repeated here: the estimator table and the DR1 estimator
equations, sub-forest length, fiducial power form, bootstrap covariance
(`physics-and-methods.md#estimators-2`); measurement history, sample sizes
and k ranges (`results.md#the-one-dimensional-flux-power-spectrum`); the
per-term systematic budgets of the two DR1 measurements and the "why 30%"
rule (`systematics.md#g4-desi-dr1-p1d-fft-estimator-arxiv-2505-09493`,
`systematics.md#g5-desi-dr1-p1d-optimal-qmle-estimator-arxiv`); resolution,
noise and masking as systematics with their mitigations
(`systematics.md#c1-spectral-resolution`, `systematics.md#c2-noise-power`,
`systematics.md#c4-masking-sky-lines-dlas-bals-in-fourier-space`).

Notation: δ_F the flux contrast, s a sub-forest (FFT), q a quasar, k in Å⁻¹
for the FFT papers and in s/km for the QMLE papers (conversion in
`physics-and-methods.md#conventions-units-and-where-the-community-is`),
R_s(k) the Fourier transform of the resolution matrix, R_z = cΔλ/[(1+z)λ_α]
the pixel width in velocity units with Δλ = 0.8 Å, θ_α the band-power
deviations from a fiducial, C = S + N the pixel covariance (signal plus noise).

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Continuum: same algorithm, different parameterisation and code
<!-- key: step-1-continuum-same-algorithm-different -->

| Item | DR1 FFT (picca) | DR1 QMLE (qsonic) | Place read |
|---|---|---|---|
| Per-quasar term | (a_q + b_q λ), linear in λ | (a_q + b_q Λ), Λ ~ log λ_RF | arXiv:2505.09493, Eq. 3; arXiv:2505.07974, Sect. 3.1 |
| Rest-frame range | 1050–1180 Å | — (forest region) | arXiv:2505.09493, Sect. 3.1 |
| Mean-continuum binning | 2.67 Å (rest frame) | 0.4 Å (rest frame), converges after 5 iterations | same |
| Variance in the fit | pipeline noise normalised by F̄C_q | η σ²_pipe + σ²_LSS (a_q + b_qΛ)² F̄² C̄² (Eq. 2) | same |
| Selection | mean S/N > 1 per quasar | — | arXiv:2505.09493, Eq. 5 |
| Final step | stack of all δ set to zero | — | arXiv:2505.09493, Sect. 3.1 |

The 3D pipeline's polynomial in log λ (`physics-and-methods.md#definition`)
is therefore not the one written in the DR1 FFT P1D paper; the two P1D papers
also use different codes. eBOSS DR14 tested a rest-frame-linear term
a_q + b_q(λ_RF − λ̄_RF) against a multiplicative constant: after each one's
correction the spectra agreed to < 1%, and the linear form gave the larger
bias, so it was dropped (arXiv:1812.03554) [src: Sect. 4.2]. The QMLE paper
states that a_q and b_q "also absorb the effect of the mean IGM flux and the
underlying large-scale overdensity field", which biases P1D (Sect. 3.1) and
is corrected in Step 6.

Masks applied before the fit (QMLE): DLA regions with more than 20%
absorption from a Voigt profile, wings corrected; all possible BAL troughs
masked without correction; major sky lines (arXiv:2505.07974) [src: Sect. 3.1].
FFT sub-forests shorter than 75 pixels or with more than 120 masked pixels are
removed; z_min = 2.1 avoids λ ≲ 3700 Å where atmospheric absorption raises
the noise (arXiv:2505.09493) [src: Sect. 3.2].

### Step 2. Noise power (FFT) or noise matrix (QMLE)
<!-- key: step-2-noise-power-fft-or-noise-matrix-qmle -->

**FFT, pipeline model.** P_noise,s is the mean |FFT|² of N_G = 2500 Gaussian
realisations with the per-pixel pipeline σ (arXiv:2505.09493) [src: Sect. 3.2].
Because the pipeline can underestimate the noise, an additive correction α is
taken as ⟨P_raw − P_noise⟩ over k > k_res,98 = 3.1 Å⁻¹, where the resolution
damping exceeds 98% and no signal is left. DR1: α = 6.9 × 10⁻⁴ Å, a 2.8%
noise underestimate, against 1.09 × 10⁻³ for the EDR+M2 sample [src: Sect. 4.2].

**FFT, eBOSS DR14 route.** Noise from the semi-difference of two coadds built
from even- and odd-numbered exposures, renormalised by
α = 4 E[N_exp/2] E[(N_exp+1)/2]/N_exp² (α = 1 for even N_exp, 0.98 for five
exposures); then, because this noise did not reach the small-scale asymptote
of P_raw at low z, rescaled by β (≈ 0.95 in the first three redshift bins)
fitted on k > 0.02 (km/s)⁻¹ (arXiv:1812.03554) [src: Sect. 3.2]. The same
principle as DESI's α: the smallest scales calibrate the noise.

**FFT, cross-exposure.** Correlate distinct exposures m ≠ n of the same
quasar (arXiv:2505.09493, Eqs. 11–13); the noise terms vanish if noise is
independent between exposures, checked on DR1 by verifying that the
noise-including terms average to zero [src: Sect. 4.2]. Choices and reasons
[src: same]:

- One exposure per quasar per night, to remove noise shared through the same
  bias and flat calibrations (not dark calibrations, which are not nightly).
- Continuum fitted on each exposure as if it were a separate quasar; fitting
  on the coadd or on the highest-S/N exposure "introduces biases and spurious
  oscillations".
- Only 35–39% of the catalogue qualifies, so it is the baseline only at
  z = 2.2, 2.4, 2.6, where small-scale and amplifier discrepancies appear;
  above, the α-corrected estimate is kept for its smaller errors. With this,
  the noise systematic is dropped from the budget.

**QMLE.** Diagonal noise matrix N_ii = σ_i², the pipeline noise divided by
continuum and F̄ (arXiv:2008.06421) [src: Sect. 2.1], with η(λ) calibrated in
side bands: moments ⟨δ⟩, ⟨δ²⟩, ⟨δ⁴⟩ in log σ²_pipe bins, jackknife
covariance, all three side bands giving similar η; flux calibration from the
side-band stack on an 8 Å grid, with errors up to 4% at the Balmer and Ca II
H&K lines (arXiv:2505.07974) [src: Sect. 4.3, Fig. 3]. A per-amplifier η_a was
tried and abandoned: the one-amplifier-removed jackknifes became strongly
inconsistent because "each η_a estimate captures amplifier-specific defects
that are not necessarily a simple scaling of the noise variance" [src:
Sect. 4.4.5]. The cross-exposure QMLE (xQMLE) removes N altogether.

### Step 3. Resolution
<!-- key: step-3-resolution -->

FFT: divide by R_s², the Fourier transform of the pipeline resolution matrix
averaged per pixel (arXiv:2505.09493, Eq. 7) [src: Sect. 3.2]. QMLE: the
signal matrix is S̃ = R S Rᵀ with the per-pixel resolution matrix; the 2020
method paper approximated a constant resolution, S_ij = ∫ dk/π cos(k v_ij)
W²(k) P_fid(k, z_ij) with W(k) = e^{−k²R²/2} sinc(kΔv/2) (arXiv:2008.06421,
Eqs. 16–17) [src: Sect. 2.1], and called DESI's resolution matrix "one of
QMLE's strengths for future analyses" [src: same]. Residual resolution error
is not corrected but put in the covariance (Step 7).

### Step 4. Estimate
<!-- key: step-4-estimate -->

**FFT.** Average (P_raw − P_noise)/R² over sub-forests with weights
w = 1/σ²(S/N), σ²(S/N) = a/(S/N − 1)² + b fitted per (k, z) bin from the
scatter of individual spectra in S/N bins (arXiv:2505.09493, Eqs. 8–9); by
construction w → 0 as S/N → 1, matching the S/N > 1 cut [src: Sect. 3.2].
Each sub-forest is assumed an independent realisation; correlations between
sub-forests and between redshift bins are neglected, although sub-forests near
a bin edge put half their pixels in the next bin [src: same]. The SNR
weighting makes the averaged noise power non-flat below 2 Å⁻¹ even though each
individual one is flat [src: Sect. 4.2].

**QMLE.** Newton–Raphson on the Gaussian likelihood with the Fisher matrix in
place of the curvature:
θ̂_α = ½ Σ F⁻¹_αα′ (d_α′ − b_α′ − t_α′), d = xᵀC⁻¹QC⁻¹x, b = Tr(C⁻¹QC⁻¹N),
t = Tr(C⁻¹QC⁻¹S_fid), F = ½ Tr(C⁻¹Q_αC⁻¹Q_α′) (arXiv:2008.06421,
Eqs. 3–7), with Q_α = ∂C/∂θ_α, top-hat k bands and linear interpolation in z
(Eqs. 18–19) [src: Sect. 2]. C is block-diagonal by quasar, so F and the
bracket are accumulated quasar by quasar [src: Sect. 2.1]. Choices and
reasons:

- **Fiducial.** No fiducial still recovers P1D; a fiducial refitted from a
  first pass "decisively outperforms" none; iterations after the first mainly
  correct the error estimates (arXiv:2008.06421) [src: Sect. 4.3]. DR1 uses
  one iteration around a fitted fiducial (`physics-and-methods.md#estimators-2`).
- **Fisher sparsity.** Keeping the diagonal plus one off-diagonal element in
  k and in z cuts the Fisher computation time per iteration by 95% (64% for
  the whole iteration) without changing χ² on 800,000 spectra [src: Sect. 4.4].
- **Interpolation in z.** Linear rather than top hat, for smoothness; it
  forces each pixel pair into two redshift bins [src: Sect. 2.1].

### Step 5. Masks
<!-- key: step-5-masks -->

FFT: masked pixels are set to δ_F = 0, so the measured power is the true one
convolved with the squared Fourier transform of the mask; because P1D falls
with k this lowers large-scale and raises small-scale power (arXiv:1812.03554)
[src: Sect. 4.3]. DESI derives one multiplicative correction per effect as the
masked/unmasked ratio on quickquasars mocks, fitted by a polynomial in each
redshift bin (arXiv:2509.13593) [src: Sect. 5.3]. QMLE: masked pixels get
large errors and drop out; on 100,000 DESI-lite spectra with 15% carrying a
25 Å masked HCD, ignoring the mask gave χ² ~ 4000 and the large-error
treatment χ² = 234, "close to the original case" (arXiv:2008.06421) [src:
Sect. 4.1].

### Step 6. Continuum bias and continuum modes
<!-- key: step-6-continuum-bias-and-continuum-modes -->

QMLE marginalises continuum modes by C′ = C + N t tᵀ with N large (Slosar et
al. 2013, App. B, as used in arXiv:2008.06421) [src: Sect. 4.2]; with
N_0 = N_1 = 1000 on amplitude and slope the first two bins
(5 × 10⁻⁴ and 1.5 × 10⁻³ s/km) are restored, at a 25–45% error increase in
the first [src: same]. This is why k < 10⁻³ s/km is unusable on data
(arXiv:2509.13593) [src: Sect. 4.1].

Marginalisation does not remove a second effect: "the continuum fitting adds
extra power to all scales through three-point correlations", detected at
p ≈ 0 on 20 mocks (arXiv:2509.13593) [src: Sect. 4.1]. DESI models it as
P_meas/P_true − 1 = b(k), a first-order polynomial in x = k/(0.009 s/km),
b ~ 6 × 10⁻³, and corrects P_corr = P_meas − [b/(1+b)] P_smooth [src: same].
The correction applied to data comes from fully contaminated mocks (BALs,
DLAs, sky masks), where b is larger than in clean mocks at all z except 3.8,
"caused by the continuum-fitting response to the underlying large-scale
density field within the unmasked forest region" [src: Sect. 4.2, Table 1].
For the FFT, the continuum effect is 1% at z ≤ 3.2 and up to 2% at z ≥ 3.4
[src: Sect. 5.2, Fig. 8]; eBOSS DR14 found 1.02–1.05 (arXiv:1812.03554)
[src: Table 3].

### Step 7. Covariance
<!-- key: step-7-covariance -->

FFT: a new weighted covariance estimator (arXiv:2509.13593, Eq. 11) [src:
Sect. 3.3.1], found to overestimate the errors on clean mocks (one-sided KS
p = 1, two-sided p = 0) and renormalised by 10%, after which p = 0.85 and
0.27 [src: Sect. 5.2]. QMLE: the Gaussian (Fisher) covariance fails on clean
mocks (p = 0.03) while the bootstrap passes (p = 0.64; two-sided 0.88), which
is why the bootstrap is the baseline [src: Sect. 4.1]. Systematics enter as
correlated templates (resolution, continuum, η) plus uncorrelated diagonal
terms; for noise, only positive jackknife − QMLE differences are added,
because "the optimal estimator gives a Gaussian covariance matrix that is
theoretically the smallest" (arXiv:2505.07974) [src: Sect. 4.4.5]; outliers
beyond 3.5σ̄ of an amplifier-cleaned mean get quadratically inflated errors
(1 at z = 2.2, 2 at 2.4, 3 each at 2.6 and 2.8) [src: same].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### FFT or QMLE
<!-- key: fft-or-qmle -->

| | FFT (picca) | QMLE (lyspeq/qsonic) |
|---|---|---|
| Masks | biased; multiplicative corrections from mocks, 30% error (6% for BAL) | handled by construction (large-error pixels) |
| Continuum | bias corrected from mocks | low-k modes marginalised; residual three-point bias corrected from mocks |
| Weights | per-sub-forest S/N weights; no pixel weights | full pixel covariance per quasar |
| Redshift correlations | neglected | estimated |
| Cost | fast | Fisher accumulation; sparse approximation needed |
| Validation reference | must be measured from mocks: the FFT works in wavelength and the conversion from velocity biases an analytic reference | analytic, in velocity |

Place read: arXiv:2505.09493, Sects. 3.2, 6.2; arXiv:2509.13593, Sects. 3.4,
4.2, 5.3; arXiv:2008.06421, Sects. 4.1, 4.4.

On DR1 the two agree up to half the Nyquist wavenumber; differences are
attributed to correlated fluctuations from systematics and "leftover biases
in the FFT due to missing data", with slightly different samples (S/N
selection, some BALs removed in the FFT sample) (arXiv:2505.07974) [src:
Sect. 5.1, Fig. 8]. The cosmology analysis takes QMLE "since these are not
affected by masking systematics like FFT-based estimates"
(`systematics.md#c4-masking-sky-lines-dlas-bals-in-fourier-space`). In the
resolution image simulations the FFT shows a large-scale bias the QMLE does
not, unexplained and "unlikely to originate from a purely resolution effect"
(arXiv:2509.13593) [src: Sect. 6].

### Mock-derived corrections or a window matrix (critique of the FFT route)
<!-- key: mock-derived-corrections-or-a-window-matrix -->

Lokken et al. 2025 replace multiplicative corrections by a window matrix
M_mn = W_{m−n} R²(k_n) / Σ_o W_{m−o} R²(k_o), with W_m the mean squared DFT
of the pixel weights (masks are binary weights), applied to the theory
(arXiv:2505.02904, Eqs. 26–27); spectra are zero-padded by at least a factor
two to make the k grid fine enough [src: Sects. 2.2, 5]. On MP-Gadget
skewers at z = 3 with ~2% of pixels masked, all mask types except large DLAs
bias P1D by > 1% at k < 3 Mpc⁻¹, and distort Si oscillations and any spike in
the true spectrum; the windowed model reproduces the masked P1D to within
0.5% [src: Sect. 3, Figs. 4–5]. It also allows inverse-variance pixel weights,
"thus far not … used in the picca-fft estimators" [src: Sect. 5]. Stated
limits: masks correlated with the signal (DLAs) are not handled — masking
small DLAs biases more than masking large ones — and a full per-pixel
resolution matrix is not modelled [src: Sect. 5]. The DR1 validation paper
names this as the planned FFT improvement (arXiv:2509.13593) [src: Sect. 7].

### Auto-spectrum or cross-exposure
<!-- key: auto-spectrum-or-cross-exposure -->

Cross-exposure removes pipeline noise, as in CMB cross-spectra, but discards
single-exposure quasars whatever their S/N, so "fully utilizing xQMLE
necessitates a different observational strategy" (arXiv:2505.07974) [src:
Sect. 5.2]. It is not immune to wavelength-calibration shifts v_e between
exposures, which would give P(k) cos(k v_e); shifts would need to exceed
300 km/s (4–6 Å) to matter, while DESI's are ~0.025 Å [src: same]. Excess
fluctuations seen in xQMLE are attributed to limited statistics; Year 3 has
2.5 times more multi-exposure quasars [src: same].

### Resolution: correct or budget
<!-- key: resolution-correct-or-budget -->

DESI does not correct the image-simulation bias but budgets it as a correlated
template, because simulation fidelity must improve, the large-scale FFT offset
is not understood, and the bias partly comes from pipeline-noise estimation
(arXiv:2509.13593) [src: Sect. 6]. The bias is ~1% (Sect. 7), "1–2%
precision" with wavelength-dependent sign (Fig. 12); the QMLE paper uses 1.5%
(arXiv:2505.07974, Sect. 4.4.4). The "few percent" in `results.md` is the
abstract's wording of the same result. The FFT budget instead applies a
correction A_res with a 30% error (arXiv:2505.09493) [src: Sect. 6.2].

### Side bands: metals only, or pipeline residuals too
<!-- key: side-bands-metals-only-or-pipeline-residuals-too -->

Subtracting side-band power (eBOSS SB1 1270–1380 Å, SB2 1410–1520 Å as a
check) removes metals redward of 1380 Å and also pipeline residuals, such as
the blue/red arm overlap at 5800–6350 Å, ~10% of the forest power at high k
at λ ~ 6000 Å (arXiv:1812.03554) [src: Sect. 3.3]. It is statistical: each
redshift bin uses different, lower-z quasars [src: same].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Gaussian noise realisations | N_G = 2500 per sub-forest | DR1 FFT | arXiv:2505.09493 | Sect. 3.2 |
| Noise asymptote scale | k > 3.1 Å⁻¹ (98% resolution damping) | DR1 FFT | arXiv:2505.09493 | Sect. 4.2 |
| Noise underestimate α | 6.9 × 10⁻⁴ Å (2.8%); EDR+M2 1.09 × 10⁻³ | DESI | arXiv:2505.09493 | Sect. 4.2 |
| Cross-exposure usable fraction | 35–39% of quasars | DR1 FFT | arXiv:2505.09493 | Sect. 4.2 |
| Sub-forest cuts | ≥ 75 pixels; ≤ 120 masked | DR1 FFT | arXiv:2505.09493 | Sect. 3.2 |
| Continuum bias b(k) | ~6 × 10⁻³ (QMLE); 1–2% (FFT) | DR1 mocks | arXiv:2509.13593 | Sects. 4.1, 5.2 |
| Mocks for corrections | 20 quickquasars realisations; power tuned to data at 10–20% | DR1 | arXiv:2509.13593 | Sects. 4, 7 |
| KS power with 20 mocks | rules out a 2.85% covariance bias in 80% of trials, 3.75% in 95% (p < 0.05) | DR1 | arXiv:2509.13593 | Sect. 3.4 |
| FFT covariance renormalisation | 10% | DR1 FFT | arXiv:2509.13593 | Sect. 5.2 |
| Image simulations | 675,000 spectra, 15× EDR; z_qso ≤ 3.6 so z_F ≤ 3.4 | DR1 | arXiv:2509.13593 | Sect. 6 |
| Continuum-mode cost | +25–45% error in first k bin | DESI-lite | arXiv:2008.06421 | Sect. 4.2 |
| Fisher sparsity gain | −95% Fisher time, −64% per iteration | DESI-lite | arXiv:2008.06421 | Sect. 4.4 |
| η scatter template | σ_η = 1.5% (z < 3.7), 4% (z > 3.7) | DR1 QMLE | arXiv:2505.07974 | Sect. 4.4.5 |
| Amplifier feature | k = 0.009 s/km = fixed 9.6 Å (0.65 Å⁻¹) | DR1 QMLE | arXiv:2505.07974 | Sect. 4.4.5 |
| Corrections, eBOSS DR14 | continuum 1.02–1.05; sky masking 0.82–1.10; DLA masking 0.99–1.00 | eBOSS DR14 | arXiv:1812.03554 | Table 3 |
| Masking bias, hydro skewers | > 1% at k < 3 Mpc⁻¹ (2% masked); windowed model < 0.5% | MP-Gadget z = 3 | arXiv:2505.02904 | Sect. 3 |
| eBOSS–DESI offset on common quasars | reduced 2–3×, 5% persists | DR1 | arXiv:2505.07974 | Sect. 5.1 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Noise misestimated.** Additive bias at high k. Test: P_raw must tend to
  P_noise where resolution kills the signal (α or β), and the cross-exposure
  estimate must agree at k ≳ 1.5 Å⁻¹ (arXiv:2505.09493) [src: Sect. 4.2].
- **Faulty amplifiers.** A bump near 0.6 Å⁻¹, or a fixed-Δλ oscillation; caught
  by amplifier splits and one-amplifier-removed jackknifes (arXiv:2505.09493
  [src: Sect. 4.2]; arXiv:2505.07974 [src: Sect. 4.4.5]).
- **Continuum per exposure done wrong.** Biases and spurious oscillations in
  the cross-exposure estimate if a common continuum is used (arXiv:2505.09493)
  [src: Sect. 4.2].
- **Masks treated as independent.** Overlapping masks could make the product
  of corrections overcorrect; tested on mocks with all masks plus continuum
  fitting (one-sided p = 1) (arXiv:2509.13593) [src: Sect. 5.3.4].
- **Masks correlated with the field.** Randomly placed mock HCDs do not test
  this; finders' false positives prefer high-absorption regions; not yet
  quantified (arXiv:2509.13593 [src: Sect. 7]; arXiv:2505.02904 [src: Sect. 5]).
- **Weak validation.** With 20 mocks the KS test can pass a covariance biased
  by a few percent (≥ 5% chance) [src: arXiv:2509.13593, Sect. 3.4].
- **Gaussian covariance trusted.** Fails on clean mocks; use the bootstrap
  (arXiv:2509.13593) [src: Sect. 4.1].
- **Unresolved survey offsets.** DESI and eBOSS differ at large scales; an HCD
  template with small DLAs and sub-DLAs absorbs the offset, the leading (not
  only) explanation being DLA incompleteness and misclassification
  (arXiv:2505.07974) [src: Sect. 5.1].

User recommendations for the DR1 QMLE measurement, as the paper lists them
(arXiv:2505.07974) [src: Sect. 5.4]: apply 10⁻³ s/km < k < 0.5π/R_z; drop the
z = 4.2 and 4.4 bins of the high-S/N sample (unreliable covariance); use the
full covariance (systematics are templates); for an explicit resolution
nuisance remove its template and multiply the theory by e^{2b_res k²R_z²} with
a Gaussian prior σ = 1.5%; model Si III and Si II oscillations and Mg II and
C IV residual doublets, preferably with a free silicon amplitude per redshift
bin; if χ²_ν is bad, "which is likely to happen", inflate the diagonal until
χ²_ν ~ 1.

## Reading list
<!-- key: reading-list -->

- Foundation: Karaçaylı et al. 2020, arXiv:2008.06421 — the QMLE for the
  forest: equations, gaps, continuum marginalisation, fiducial and Fisher
  approximations.
- Method: Chabanier et al. 2019, arXiv:1812.03554 — the FFT route with noise
  from exposure differences, side bands, mock-derived continuum and masking
  corrections.
- Application: Ravoux et al. 2025, arXiv:2505.09493 — DESI DR1 FFT: noise
  asymptote, cross-exposure FFT, S/N weights, budget.
- Application: Karaçaylı et al. 2025, arXiv:2505.07974 — DESI DR1 QMLE:
  side-band calibration, amplifier noise, FFT comparison, user recommendations.
- Validation: Karaçaylı et al. 2025, arXiv:2509.13593 — how both estimators' corrections and
  covariances are validated (KS protocol, continuum bias, masking, resolution).
- Critique and alternative: Lokken et al. 2025, arXiv:2505.02904 — masking
  biases of FFT estimators and the window-matrix fix with pixel weights.

## Not verified
<!-- key: not-verified -->

- The EDR FFT paper (arXiv:2306.06311), source of the DESI correction scheme,
  and the BOSS DR9 two-estimator comparison (arXiv:1306.5896): bodies not read.
- The xQMLE equations and the regularised bootstrap of arXiv:2505.07974
  (Sects. 3.2.1–3.2.2) beyond what L2 states.
- Whether high-resolution P1D pipelines (arXiv:2108.10870) use the same
  continuum-bias and masking treatment.
- The fitted form of the FFT masking corrections per redshift bin in DR1
  (shown only in figures of arXiv:2509.13593).
