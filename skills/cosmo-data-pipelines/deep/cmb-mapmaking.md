# CMB time-ordered data processing and map-making — cosmo-data-pipelines dossier

Scope: what happens to CMB detector timestreams before and inside the map
solver (data selection at sample, detector and observation level, time-domain
calibration, preparation, the noise model built from the data, pointing
matrix, cut-sample and model-error degrees of freedom, filter-and-bin
settings), which maps and splits are released, and how map-level null
tests are built and passed; compared across ACT DR6 (maximum likelihood),
SPT-3G D1 (filter and bin) and Planck HFI 2018 (destriper), with the reason
given for each setting.
Snapshot: 2026-10-18.
From: Planck HFI and LFI data-processing papers (2018); ACT, SPT and Simons
Observatory map-making papers (copied from `references/subtopics.tsv`).

Already in L2, not repeated here: the linear problem d = P m + n and its
generalised least-squares solution, the families of map-makers in a table,
the null-test outline (`physics-and-methods.md#cmb-time-ordered-data-to-maps`);
ACT's three-pass scheme and its injection transfer function (Eq. 13)
(`surveys-and-data.md#cmb-experiments`); map depths
(`results.md#cmb-map-making-performance`); model error and power loss
(`systematics.md#cmb-map-maker-model-error-and-transfer-function`) and the
filter-and-bin debate (`open-questions.md#cmb-map-making-filter-and-bin-or-unbiased`).
Beams, absolute and polarisation calibration are in `cosmo-cmb`
(deep/beams-calibration-polarisation); MASTER, spectrum-level transfer
functions and the ACT null-test counts in `cosmo-cmb` (physics-and-methods,
Sect. 4; systematics).

Notation: d is the timestream vector (detector × sample), m the T, Q, U
map, P (A in SPT's paper) the pointing matrix, N the noise covariance, ψ
the detector polarisation angle on the sky.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Select data at three levels
<!-- key: step-1-select-data-at-three-levels -->

ACT DR6 cuts whole observations, then detectors, then sample ranges
(Naess et al. 2025, arXiv:2503.14451) [src: Sect. II.2, App. A].

- **Unit of data.** A "TOD" is typically 11 minutes: "around 260k samples
  each for 700 selected detectors, for a total of around 200 million
  samples" [src: arXiv:2503.14451, Sect. II.2 and its footnote 4].
- **Per sample.** Glitches: high-pass at 5 Hz, Gaussian smoothing of
  FWHM ≈ 0.015 s (the typical glitch duration), noise from the
  inter-quartile range, flag at S/N > 10, pad by 200 samples (~0.5 s),
  merge gaps under 30 samples. Bright sources (f090 > 500 mJy) are masked
  within 3′ for glitch finding only, so they are not cut as glitches.
  Scan turnarounds, scan-speed anomalies and Sun or Moon in the far
  sidelobes are cut [src: arXiv:2503.14451, App. A.1, Sect. II.2].
- **Per detector.** A valid bias-step responsivity is required. Eight
  "pathology" statistics are computed per detector and TOD (Table 13):
  gain, corr and norm from an SVD common mode in 0.01–0.1 Hz (atmosphere),
  averaged over ten bins shifted by 0.05 Hz for robustness; rms, skewness
  and kurtosis in 10–20 Hz after removing the 10 strongest correlated
  modes; a drift error below 0.03 Hz after 3 modes; a mid-frequency error
  in 0.3–1 Hz after 8 modes, a sign of thermal contamination
  [src: arXiv:2503.14451, App. A.2]. Outliers are cut against the seasonal distribution per
  array and band, with thresholds "determined by manual inspection"; a
  detector is also cut above 20,000 glitches or when > 40% of its samples
  are cut [src: same]. Using the pre-selected well-behaved detectors only
  to extract the common mode, rather than as the only detectors mapped
  (DR4), raises the yield by up to 10% [src: same].
- **Per TOD.** Rejected below 100 usable detectors, or when
  PWV/sin(el) > 4 mm (PWV the precipitable water vapour, el the elevation)
  [src: arXiv:2503.14451, App. A.3], or when the daytime beam deforms too much
  [src: Sect. II.2].
- **Yield.** About 75% of night and 50% of day TODs pass; ~30% of
  detectors never work, ~80% of the others pass per TOD, for ~55% overall;
  ~1% of samples of selected detectors are cut at night and more by day
  (kept fractions 98.5–99.2% at night, 94.9–97.3% by day)
  [src: arXiv:2503.14451, Sect. II.2, Tables 2–3].

Planck HFI selects at the level of pointing periods ("rings"). For 2018
it stopped at ring 26050 instead of 27005, dropping the end of the
cryogenic phase when the 100 mK stage fluctuated; the test was a χ² on
ℓ = 3–20 cross-spectra of difference maps between the full data and 26
subsets each missing 1000 consecutive rings, in which the dropped block
stood out (Planck Collaboration 2018 III, arXiv:1807.06207)
[src: Sect. 2.1.3].

### Step 2. Calibrate and clean in the time domain
<!-- key: step-2-calibrate-and-clean-in-the-time-domain -->

**ACT DR6** [src: arXiv:2503.14451, Sects. II.3–II.4, III.1].

- Each sample is converted to power as d^pW_it = R_it f_it d^DAQ_it
  (Eq. 1), with R the responsivity from the last bias step (at least
  hourly) and f the optical flat field (relative gain).
- The flat field comes from each detector's correlation with the
  atmosphere at 0.01–0.1 Hz, after separating atmospheric modes from
  ground pickup, magnetic and cryostat drifts; a monthly average replaced
  per-TOD values because it minimised the low-ℓ power loss in tests. It
  is still accurate only to a few percent and is "probably the dominant
  cause" of the low-ℓ bias that forces TT below ℓ = 600–1000 to be
  discarded; the authors point to an external calibrator such as the
  Simons Observatory LAT stimulator, provided bandpass mismatches are
  ≪ 1% [src: arXiv:2503.14451, Sect. II.4.1].
- Detector time constants (median 0.74–1.35 ms in 2017–2019, about
  0.3 ms longer after 2020) would cost 0.1%, 1% and 10% of power at
  ℓ = 2000, 6000 and 19,000; each detector's mean value from Uranus is
  deconvolved, and the later increase is absorbed by the pointing-jitter
  term of the beam [src: arXiv:2503.14451, Sect. II.3, Table 4].
- Preparation: divide the gain; gap-fill glitches only, from the
  detector–detector covariance (so extreme values do not enter the noise
  model; gap-filled samples never reach the map); subtract a linear trend
  between the means of the first and last 8 samples to reduce the Fourier
  discontinuity; deconvolve the anti-aliasing filter and time constants;
  Fourier-downsample for all but the last pass; use 32-bit floats (enough
  for per-sample S/N 10⁷, checked against 64-bit); subtract the polarised
  sidelobe model from the previous pass [src: arXiv:2503.14451, Sect. III.1].
- Ground pickup is no longer subtracted in the time domain: in DR4 it was
  not effective enough to avoid map-space filtering and needed costly
  time-domain simulations [src: Sect. III.1].

**Planck HFI** [src: arXiv:1807.06207, Sect. 2.1.2]: ADC non-linearity
correction; demodulation (running-average baseline, multiplication by the
bias parity); glitch detection with fitted templates for tails shorter
than 3 s; a quadratic bolometer non-linearity from ground data; a thermal
template from the two dark bolometers against slow drifts; fitted 4 K
cooler lines; deconvolution of a multi-time-constant transfer function
with a regularising low-pass; jump correction; then compression into
HEALPix-binned rings for the map-maker. Time constants comparable to the
spin period and glitch tails of 20–30 s are not removed there; an
empirical transfer function is fitted inside SRoll from odd–even survey
differences, accurate to "a few tenths of a percent" [src: Sects. 5.8,
5.11.1].

**SPT-3G D1** (Quan et al. 2026, arXiv:2603.20163): a pointing model with
flexure and bearing tilts, plus per-observation corrections to the two
parameters that drift over hours, measured on bright AGN against AT20G
positions (at least five sources above 10σ per map), bringing
observation-to-observation pointing errors to a few arcseconds
[src: Sect. III.2.4]. Detector gains rise as the telescope climbs in
elevation (less atmospheric loading): ~6% across the lowest subfield at
150 GHz, measured with calibrator stares before and after each
observation and shown negligible for spectra with a sawtooth toy model
[src: Sect. VI.1].

### Step 3. Build the noise model from the data
<!-- key: step-3-build-the-noise-model-from-the-data -->

ACT models Fourier modes of each TOD as independent and detectors as
correlated: Ñ_ff′dd′ = (D_{b_f d} + V_di E_{b_f i} Vᵀ_id′) δ_ff′ (Eq. 2),
with b_f one of ~60 unequal frequency bins, D the uncorrelated part, V
eigenvectors whose amplitude exceeds 16 times the median eigenvalue in
0.25–4 Hz (atmosphere) or 4–200 Hz (instrument), typically ~10 modes, and
E their power per bin (arXiv:2503.14451) [src: Sect. III.2]. A noise model
measured on data that contain the sky biases the signal low, because
noise that cancels the signal looks lower-variance and gets more weight;
hence the signal estimate of the previous pass is subtracted before the
model is rebuilt (the multipass scheme in L2) [src: same].

SPT gives every sample of a detector timestream one weight, the inverse
of the mean PSD between frequencies matching ℓ_x = 320 and 4000
(Eq. 8), chosen to optimise the 1D TT and EE noise of the maps over that
range (arXiv:2603.20163) [src: Sect. III.2.5].

Planck HFI noise: white plus a thermal 1/f² term shared by all bolometers
plus 1/f^α with α ≈ 1, Gaussian after deglitching; the knee frequency is
almost independent of the noise level, which simulations explain by
undetected glitches and glitch tails, "a very likely source candidate for
the 1/f noise" (arXiv:1807.06207) [src: Sects. 2.1.4, 5.8]. The
end-to-end noise is adjusted by a few percent to match the odd–even ring
null test [src: Sect. 2.1.5].

The resulting map noise, N(ℓ) ≈ σ²[1 + (ℓ/ℓ_knee)^α] (Eq. 12, σ² the
white level), has α ≈ −3 and ℓ_knee ≈ 2100, 3000, 3800 in ACT temperature
at f090, f150, f220 and 300–640 in polarisation; the paper quotes
1200/1900/2100 (T) and 200 (E) with a slope near −4 for SPT, and ℓ_knee ~ 50
with slope near −1 for Planck (arXiv:2503.14451) [src: Sect. V.1].

### Step 4. Write the data model
<!-- key: step-4-write-the-data-model -->

**Pixels.** ACT DR6 uses Plate Carrée at 0.5′ (43,200 × 10,320 pixels,
−60° < dec < 20°) with half-integer pole coordinates (Fejer's first rule)
instead of DR4's Clenshaw–Curtis grid, so that maps can still be
harmonic-transformed after 2 × 2 downgrading; DR6 is shifted by half a
pixel in declination relative to DR4 [src: arXiv:2503.14451,
Sect. III.3.1]. SPT bins into HEALPix N_side = 8192 (0.43′) and a ZEA
projection with 0.5625′ pixels (arXiv:2603.20163) [src: Sect. III.2.5].

**Pointing matrix.** Nearest-neighbour, P_dtps = δ_{p q_dt}
[1, cos 2ψ_dt, sin 2ψ_dt]_s (Eq. 6), models the sky as steps between
pixels; with a highly correlated noise model this sub-pixel error causes an
O(1) bias at any scale where N is correlated, i.e. low-ℓ TT from the
ground (arXiv:2503.14451) [src: Sect. III.3.2]. ACT DR6 switched to
bilinear interpolation (Eq. 7), which makes the error second order in pixel
size; shrinking pixels instead would need 100 times more pixels for a
tenfold reduction and leave many unhit [src: same]. Bilinear P is about
four times slower and breaks the diagonality of PᵀP on which binning,
filter-and-bin and destriping rely (Naess & Louis 2023, arXiv:2210.02243)
[src: Sect. 2.2.3].

**Cut samples.** Skipping cut samples is impossible with a Fourier noise
model (the FFT needs equi-spaced samples), and setting them to zero biases
the map, so they become degrees of freedom c with response C (rows of P
zeroed) (arXiv:2503.14451) [src: Sect. III.3.3, Eq. 8]. To save memory
they are Legendre coefficients: 1, 2, 3, 4 degrees of freedom for cuts of
up to 1, 3, 6, 20 samples, then the integer nearest 5 + T/4 for a cut of T
seconds [src: same].

**Model error near bright sources.** Around objects such as 3C 273
(12 Jy at f090), model error produces X-shaped stripes at ~0.1% of the
peak extending ~3°. Each sample hitting such a region gets its own degree
of freedom s (rows of P kept), with a prior Π a = W R s (Eq. 9): W the
uncorrelated inverse noise variance, R an edge taper from 10 at the region
edge to 0.01 at 2′ inside, so that anything representable by the map goes
into m [src: arXiv:2503.14451, Sect. III.3.4]. It cannot be used
everywhere: the extra degrees of freedom spread the data too thin and
degrade the noise [src: same].

### Step 5. Filter-and-bin settings (SPT-3G D1)
<!-- key: step-5-filter-and-bin-settings-spt-3g-d1 -->

With N assumed diagonal after high-pass filtering, the solution reduces to
weighted binning per pixel with a 3 × 3 T, Q, U weight matrix (Eqs. 3–6),
and the filtering bias is calibrated by simulations (arXiv:2603.20163)
[src: Sect. III.1].

- **High-pass.** Least-squares removal of Legendre polynomials to order
  30 and sines and cosines up to f_c = (ℓ_x,c/360) v_α cos δ, with
  ℓ_x,c = 300, v_α = 1° s⁻¹ in right ascension and δ the declination,
  i.e. 0.29–0.62 Hz [src: arXiv:2603.20163, Sect. III.2.1]. The filtered timestreams are
  not white (the atmosphere is flat only above ~1 Hz), but if the
  atmosphere is "frozen" over a scan, binning is close to optimal for the
  modes kept [src: same]. ℓ_x,c was chosen from four runs on 5% of the
  data with ℓ_x,c from 100 to 400, using left-minus-right scan noise maps:
  going from 100 to 400 lowers noise in all modes by ~10% at 150 and
  220 GHz and a few percent at 95 GHz; 300 is the compromise against mode
  loss [src: same].
- **Masking in the filter.** 2118 sources above 16σ (6 mJy at 150 GHz)
  and 537 clusters above 10σ are masked when fitting the templates, to a
  radius where significance × PSF profile falls below one (2′–3′ for the
  faintest, 15′ for the brightest), which removes "filtering wings" but
  leaves oscillatory "filtering artifacts", subtracted as an additive
  spectrum bias [src: arXiv:2603.20163, Sect. III.2.2]. The real-space least-squares filter
  exists because of this masking [src: Sect. III.2.1].
- **Low-pass.** F^AA(f) = exp[−(f/f_c)⁶] (Eq. 7) at ℓ_x = 13,000
  (12–27 Hz), applied by FFT without masking; no ringing is seen
  [src: arXiv:2603.20163, Sect. III.2.3].

### Step 6. Products, splits and map-level null tests
<!-- key: step-6-products-splits-and-map-level-null-tests -->

**ACT DR6** (arXiv:2503.14451). Four noise splits per array-band and data
set, mapped independently so that spectra use cross-correlations only
[src: Sect. III.5]. Because maximum-likelihood null maps are expensive,
four null splits only: PWV < 0.70 mm (33% of TODs) against > 0.70 mm
(loading and correlated noise); boresight elevations 40°, 45° and 47°
(ground pickup); before and after February 2019 (a focus change in May
2018, kept undiluted); inner against outer detectors of each optics tube,
at equal sensitivity [src: Sect. III.6]. Depth-1 maps of single scans
(about 30,000 map sets, median depth 230–780 μK′ by array-band) use one
pass of 100 CG steps, set by the convergence of the cut degrees of
freedom, and carry their own caveats (calibration drift, artefacts,
daytime beams) [src: Sect. III.7, Table 7]. Raw maps show
azimuth-synchronous stripes of ~100 μK, partly ground-screen sidelobes and
partly internal pickup; removing modes with m < 5 cleans them visually, but
spectra needed m < 77 (|ℓ_x| < 90, ℓ_x = 1.171 m on that patch) to pass
the null tests [src: Sect. V.3].

**SPT-3G D1** (arXiv:2603.20163) [src: Sect. VII.1].

- Six splits: Sun and Moon above or below the horizon, azimuth within
  ±90° of 153° (three nearby buildings) or not, 2019 against 2020, scan
  direction, and two groups of five wafers ordered by their gain drift
  (the high-drift group also shows a 1.42 Hz cryocooler line)
  [src: arXiv:2603.20163, Sect. VII.1.1].
- 25 equal-depth bundles per half; 25 difference bundles; the null
  spectrum is the mean of the 300 cross-spectra between distinct bundles
  (Eq. 39); χ² over 400 ≤ ℓ ≤ 4000 in Δℓ = 50 bins against an expectation
  C_exp (Eq. 40), zero except for scan and wafer splits, where time
  constants and a pointing time-stamp offset leave signal residuals
  modelled by simulation [src: arXiv:2603.20163, Sects. VII.1.2–VII.1.3].
- Threshold p_sys = 0.05/54 ≈ 0.00093 (Bonferroni over 54 spectra:
  6 splits × 3 bands × TT, TE, EE) [src: Sect. VII.1.2]. Two variances: σ²_n (scatter of the
  300 cross-spectra) and σ²_{n+s} adding 0.01% of the sample variance.
  Outcomes: pass with σ_n; "detected but negligible" if it passes only with
  σ_{n+s}; investigate otherwise. The 0.01% fraction was scaled down from
  the 1% shown harmless for the 2018 data because the noise is ten times
  lower [src: arXiv:2603.20163, Sect. VII.1.4]. No uniformity test of the p-value
  distribution, since the added variance correlates the p-values
  [src: same].
- Result: a narrowband contamination at ℓ ≈ 600, m ≈ 400 (a ~1.1 Hz
  timestream line, mostly at the field edges and lowest elevations, cause
  unknown) was masked in harmonic space (500 ≤ ℓ ≤ 680, 350 ≤ m ≤ 425);
  afterwards five TT null spectra still fail with σ_n but all 54 pass with
  σ_{n+s} [src: arXiv:2603.20163, Sects. VII.3–VII.4, Table 6].

**Planck HFI.** Survey, odd–even ring and half-ring null tests on data,
and end-to-end simulations whose noise is tuned to the odd–even null
(arXiv:1807.06207) [src: Sects. 2.1.5, 3.2 outline].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Maximum likelihood, filter and bin, or destriper
<!-- key: maximum-likelihood-filter-and-bin-or-destriper -->

| | Maximum likelihood (ACT DR6) | Filter and bin (SPT-3G D1) | Generalised destriper (Planck SRoll) |
|---|---|---|---|
| What the TOD step must supply | cut-sample degrees of freedom, a data-derived noise model, several passes, model-error regions | masks for the filter, per-detector weights, simulations for the transfer function | redundancy between rings, detectors and angles |
| What it buys | low ℓ kept without TOD filtering | cheap per-observation maps and splits | instrument parameters (offsets, empirical transfer function, calibration and bandpass mismatch) solved from the sky |
| What it costs | null maps expensive, hence four splits; noise-model bias needs multipass | filtering artefacts; mode loss below ℓ_x,c; transfer function from simulations | needs the redundancy of a space scan |
| Source | arXiv:2503.14451 [src: Sects. III.2–III.6] | arXiv:2603.20163 [src: Sects. III.1–III.2] | arXiv:1807.06207 [src: Sect. 2.2.1] |

On the same 1D toy with a smooth long mode and ground-like correlated
noise, a nearest-neighbour pointing matrix makes maximum likelihood,
filter-and-bin debiased with an observation matrix, and a maximum-likelihood
limit destriper all recover only 1/3 of the amplitude; filter-and-bin
debiased with a simulated transfer function does worse; a plain binned map
is unbiased but very noisy (arXiv:2210.02243) [src: Sect. 2.1.5]. With a
signal that matches the nearest-neighbour model the bias disappears except
for the transfer-function route, which assumes independent Fourier modes
[src: Sect. 2.1.6]. The mechanism: a smooth residual costs little under a
noise model whose inverse is small at low frequency, so the solver gives
up large-scale signal to avoid jagged residuals [src: same]. Time-dependent
gain errors cause comparable loss only in unrealistic cases; constant
detector-to-detector gain mismatch is the serious one [src: Sect. 3.3].

### Clean in the time domain or in the map
<!-- key: clean-in-the-time-domain-or-in-the-map -->

ACT moved ground pickup from TOD subtraction (DR4) to map-space mode
removal (DR6) because the map-level structure is simple and its
characterisation needs no time-domain simulations [src: arXiv:2503.14451,
Sects. III.1, V.3]. SPT keeps a TOD high-pass and pays with simulations
and source masks [src: arXiv:2603.20163, Sect. III.2]. Planck cleans
instrumental effects in the TOD and leaves the residual to an empirical
transfer function in the map-maker [src: arXiv:1807.06207, Sects. 2.1.2,
5.11.1].

### Relative gains from the atmosphere or from a stimulator
<!-- key: relative-gains-from-the-atmosphere-or-from-a -->

The atmosphere fills the beam like the CMB, but has a different spectrum
and is confused with pickup and drifts; ACT's monthly atmospheric flat
field is good to a few percent and limits low-ℓ TT [src: arXiv:2503.14451,
Sect. II.4.1].

### Null-test statistics
<!-- key: null-test-statistics -->

SPT tests each spectrum against a Bonferroni threshold with a second,
sample-variance-inflated χ² to rank relevance [src: arXiv:2603.20163,
Sect. VII.1.4]; in ACT's ~2000 null tests the lowest PTE (0.05%) was
judged acceptable given their number (`cosmo-cmb` systematics). The SPT choice states its own
limitation: correlated p-values forbid a uniformity test [src: same].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| TOD length; samples | ~11 min; ~260k × ~700 detectors | ACT DR6 | arXiv:2503.14451 | Sect. II.2 |
| Glitch flag | 5 Hz high-pass, 0.015 s smoothing, S/N > 10, ±200 samples | ACT DR6 | arXiv:2503.14451 | App. A.1 |
| Detector cuts | > 20,000 glitches or > 40% samples cut | ACT DR6 | arXiv:2503.14451 | App. A.2 |
| TOD cut | < 100 detectors or PWV/sin(el) > 4 mm | ACT DR6 | arXiv:2503.14451 | App. A.3 |
| Detector yield | ~70% alive, ~80% of those per TOD, ~55% total | ACT DR6 | arXiv:2503.14451 | Sect. II.2 |
| TOD acceptance | ~75% night, ~50% day | ACT DR6 | arXiv:2503.14451 | Sect. II.2 |
| Time constants | 0.74–1.35 ms (2017–19); +0.3 ms after 2020 | ACT DR6 | arXiv:2503.14451 | Table 4 |
| Flat-field accuracy | a few percent; TT cut below ℓ = 600–1000 | ACT DR6 | arXiv:2503.14451 | Sect. II.4.1 |
| Noise model | ~60 bins; modes > 16 × median eigenvalue; ~10 modes | ACT DR6 | arXiv:2503.14451 | Sect. III.2 |
| ℓ_knee (T) | 2100, 3000, 3800 (f090, f150, f220); pol 300–640 | ACT DR6 | arXiv:2503.14451 | Sect. V.1 |
| Cut-sample dof | 1/2/3/4 for ≤ 1/3/6/20 samples; then 5 + T/4 | ACT DR6 | arXiv:2503.14451 | Sect. III.3.3 |
| Model-error prior taper | 10 at edge → 0.01 at 2′ | ACT DR6 | arXiv:2503.14451 | Sect. III.3.4 |
| Pickup mode cut | m < 5 visual; m < 77 (|ℓ_x| < 90) for nulls | ACT DR6 | arXiv:2503.14451 | Sect. V.3 |
| PWV null split | 0.70 mm (33% / 67%) | ACT DR6 | arXiv:2503.14451 | Sect. III.6.1 |
| High-pass | Legendre ≤ 30; ℓ_x,c = 300; 0.29–0.62 Hz | SPT-3G D1 | arXiv:2603.20163 | Sect. III.2.1 |
| Filter masks | 2118 sources (> 6 mJy), 537 clusters; 2′–15′ | SPT-3G D1 | arXiv:2603.20163 | Sect. III.2.2 |
| Anti-alias | exp[−(f/f_c)⁶], ℓ_x = 13,000 | SPT-3G D1 | arXiv:2603.20163 | Sect. III.2.3 |
| Weight band | ℓ_x 320–4000 | SPT-3G D1 | arXiv:2603.20163 | Sect. III.2.5 |
| Elevation gain drift | ~6% (150 GHz, lowest subfield) | SPT-3G D1 | arXiv:2603.20163 | Sect. VI.1 |
| Null threshold | p_sys = 0.05/54; inflation 0.01% of sample variance | SPT-3G D1 | arXiv:2603.20163 | Sects. VII.1.2, VII.1.4 |
| Harmonic mask | 500 ≤ ℓ ≤ 680, 350 ≤ m ≤ 425 | SPT-3G D1 | arXiv:2603.20163 | Sect. VII.3 |
| Glitch-tail templates | < 3 s fitted; 20–30 s not | Planck HFI 2018 | arXiv:1807.06207 | Sects. 2.1.2, 5.8 |
| Empirical TF accuracy | a few tenths of a percent | Planck HFI 2018 | arXiv:1807.06207 | Sect. 5.11.1 |
| Toy power loss, nearest-neighbour P | 2/3 of a long mode lost | toy | arXiv:2210.02243 | Sect. 2.1.5 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Model error invisible to simulations.** A simulation that reads the
  sky with the same pointing matrix as the map-maker is blind to sub-pixel
  error, and one without gain errors in both data and noise model is blind
  to gain-mismatch loss (arXiv:2210.02243) [src: Sect. 4]. Tests proposed:
  compare with a space telescope; split by PWV (higher correlated-to-white
  ratio, more vulnerable); remap with a noise model of reduced dynamic
  range (less biased, noisier) and compare; vary the pixel size, since the
  nearest-neighbour bias scales with it [src: Sect. 5]. Most at risk:
  ground-based, total intensity, high frequency (< 60 GHz relatively safe,
  > 200 GHz vulnerable), sensitive detectors, many detectors close on the
  sky [src: Sect. 6].
- **Relative gain errors** of a few percent limit low-ℓ TT in ACT DR6
  [src: arXiv:2503.14451, Sect. II.4.1]. Test: Planck comparison at low ℓ
  and the PWV and inner-outer splits [src: Sect. III.6].
- **Noise model biased by the signal** when estimated on data containing
  it; mitigated by multipass [src: arXiv:2503.14451, Sect. III.2].
- **Bright sources** leave X-shaped artefacts (maximum likelihood) or
  filtering wings (filter and bin) [src: arXiv:2503.14451, Sect. III.3.4;
  arXiv:2603.20163, Sect. III.2.2].
- **Instrument lines and pickup.** SPT's ~1.1 Hz contamination appeared
  only in scan and wafer nulls and was masked in harmonic space
  [src: arXiv:2603.20163, Sect. VII.3]; ACT's azimuth-synchronous pickup
  needed m < 77 removed [src: arXiv:2503.14451, Sect. V.3].
- **Unstable instrument periods.** Planck's last rings showed 100 mK
  instability and were removed after a leave-one-block-out test
  [src: arXiv:1807.06207, Sect. 2.1.3].
- **Uncorrected time constants and time-stamp offsets** make scan-direction
  nulls non-zero; model them in the expectation spectrum rather than
  assume zero [src: arXiv:2603.20163, Sect. VII.1.3].

## Reading list
<!-- key: reading-list -->

- Method, ground ML: Naess et al. 2025 (ACT DR6), arXiv:2503.14451,
  Sects. II–III, V and App. A — every cut, the noise model, cut-sample and
  model-error degrees of freedom, splits.
- Method, filter and bin: Quan et al. 2026 (SPT-3G D1), arXiv:2603.20163,
  Sects. III and VII — filter settings with their tests, map-level null
  tests with a stated decision rule.
- Method, space: Planck Collaboration 2018 III, arXiv:1807.06207,
  Sects. 2.1–2.2, 5.8, 5.11 — TOI processing chain, SRoll's solved
  parameters, glitches and 1/f noise.
- Critique: Naess & Louis 2023, arXiv:2210.02243 — why model error loses
  large-scale power, which tests catch it, who is at risk.
- Foundations in L2: Tegmark 1997, arXiv:astro-ph/9611130; Keihänen et al.
  2005, arXiv:astro-ph/0412517; Poletti et al. 2017, arXiv:1608.01624.

## Not verified
<!-- key: not-verified -->

- No Simons Observatory pre-processing or on-sky map-making paper found
  in one search; its reduction workflow is in L2 only.
- SPT-3G pointing model paper (Chichura et al.) and the C25 filtering
  artefact method not read.
- ACT DR6 near and far sidelobe appendices (B, C) and per-TOD pointing
  correction (App. E) not read.
- Planck LFI and NPIPE TOD processing beyond L2 not read.
