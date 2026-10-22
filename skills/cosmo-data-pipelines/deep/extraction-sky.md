# CCD pre-processing, spectral extraction, flux calibration and sky subtraction — cosmo-data-pipelines dossier

Scope: how a fibre spectrograph's calibration products are built and used
(pixel variance, 2D PSF, traces and wavelengths, fibre flat, sky model and
its residual corrections, standard stars, aperture losses, cross-talk,
co-addition), with the reason for each setting, and how to choose between
variants. The DESI pipeline paper is the most complete description and sets
the step order; each step also gives what SDSS/BOSS (idlspec2d), SDSS-V,
AAOmega, LAMOST, FLAMES, WEAVE and Euclid NISP slitless do, from their own
papers. 4MOST, PFS and MOONS have no pipeline paper readable on arXiv
(Not verified).
Snapshot: 2026-10-21.
From: Guy et al. 2023, Sect. IV.2–IV.11 (copied from
`references/subtopics.tsv`).

Already in L2, not repeated here: the DESI order of operations, the three
sky-subtraction families with the DESI sky fit (Guy et al. Eq. 14), the
ε_λ term (`physics-and-methods.md#spectral-extraction-calibration-and-sky`);
the sky-residual, white-dwarf and LAMOST numbers
(`results.md#spectral-extraction-and-sky-subtraction`); the sky-residual
systematic (`systematics.md#sky-subtraction-residuals`) and the DR1
variance bug (`systematics.md#data-product-defects-found-after-release`).
Zero points and dust maps: `cosmo-photometry-photoz`. Notation of Guy et
al. 2023 (arXiv:2209.14482): k fibres, i bins of the extracted spectrum,
j bins of a deconvolved model; F̃_{k,i} extracted flux, w_{k,i} its
inverse variance, R_{k,i,j} resolution matrix, T_{k,i} fibre flat.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Pre-process the CCD and model the pixel variance
<!-- key: step-1-pre-process-the-ccd-and-model-the-pixel -->

- **Cosmic rays.** A pixel is masked if it exceeds its two neighbours by
  N σ along at least two of four axes (Eq. 1a) and its gradient is steeper
  than the PSF allows along one (Eq. 1b), N = 6, c = 3, c₂ = 0.5 "adjusted
  on the data"; a second pass at N = 3 on neighbours repeats until nothing
  new is masked; the mask is grown by one pixel and a morphological closure
  with seven 11 × 11 elements joins track fragments, the vertical one
  dropped as it would align with the traces [src: arXiv:2209.14482,
  Sect. IV.2.4]. Unmasked hits become false emission lines and wrong ELG
  redshifts [src: same].
- **Negative trails** behind bright charge along the serial direction in
  some red and NIR amplifiers are linear and subtracted as a convolution
  with K(x) = −(A/L) exp(−x/L), A = 5 × 10⁻⁵–1.2 × 10⁻³, L = 4–35 pixels
  per amplifier; new readout parameters did not remove them
  [src: Sect. IV.2.5, Table 1]. **Scattered light** was modelled only for
  early, fogged-window data [src: Sect. IV.2.7].
- **Pixel variance.** Read noise from the overscan: 3.4, 2.7, 2.5 e⁻ rms
  (blue, red, NIR) [src: Sect. IV.2.9]. The usual σ̃²_P = σ²_R + P (Eq. 2)
  correlates variance with pixel value, biasing an inverse-variance mean
  of P by −1 at leading order, and is truncated at low counts [src: same].
  DESI takes the Poisson term from a model image (boxcar extraction, flat,
  mean sky, target spectrum smoothed with a σ = 10 Å Gaussian, projected
  back with a Gaussian cross-section), keeping the data value only where a
  pixel departs by more than 5σ [src: same].
- **Peers.** BOSS idlspec2d: bias and dark models, a pixel flat taken
  about every six months through a slithead without fibre structure, read
  noise from the overscan per amplifier and exposure, variance from read
  noise and observed counts (its bias: Choices), defect and cosmic-ray
  masks (Dawson et al. 2013, arXiv:1208.0022) [src: Sect. IV.3]. SDSS adds
  a 10⁻⁴ f² variance term that caps S/N below 100; LAMOST does not, so it
  quotes higher S/N at high flux (Bai et al. 2017, arXiv:1705.02079)
  [src: Sect. 4.4, Eqs. 11–12]. SDSS-V (idlspec2d v6_0_4) raised its
  cosmic-ray outlier rejection from 4σ to 50σ to keep sky-line peaks for
  wavelength calibration (What goes wrong) (arXiv:2301.07688)
  [src: Sect. X.1].

### Step 2. Fit the 2D spectrograph PSF on arc lamps
<!-- key: step-2-fit-the-2d-spectrograph-psf-on-arc-lamps -->

The PSF is the fibre tip (51 μm, 3.4 pixels after a demagnification of
0.48) convolved with the camera blur, hence a central plateau
[src: arXiv:2209.14482, Sect. IV.3.1]. DESI models the core as
Gauss–Hermite functions (Eq. 3):

PSF_H(x, y) = Σ_{i,j} a_{ij} He_i((x − x_c)/σ_x) He_j((y − y_c)/σ_y)
× exp[−(x − x_c)²/2σ_x² − (y − y_c)²/2σ_y²] / (2π σ_x σ_y),

with He_i probabilists' Hermite polynomials of degree 0–6, (x_c, y_c) the
trace and every coefficient a Legendre polynomial in wavelength per fibre
[src: same]. Reasons: a linear basis converges easily, is orthogonal
(uncorrelated coefficients for small pixels) and integrates analytically
over pixels, as the sharp profile requires; degree 6 is needed for a
partly resolved disk [src: same].

- **Tails left out on purpose.** A power-law tail exists in the code but
  is unused: extended PSFs would spread every unmasked cosmic ray over
  many fibres and slow the extraction, and the post-hoc cross-talk
  correction (Step 8) is precise enough [src: same].
- **Fit.** One specex fit per arc exposure, Gauss–Newton in three passes
  (trace and wavelength Legendre coefficients; σ_x, σ_y; a_{ij}), line
  intensities fitted throughout, per block of 25 fibres (20 blocks, gaps
  of about two fibre spacings); no positivity in the fit, pixel-integrated
  values forced positive at extraction [src: Sect. IV.3.2].
- **Stability criterion**: the emission-line flux bias from a PSF shape
  error, δF/F = Σ_i P_i P_i^truth / Σ_j P_j² − 1 (Eq. 4; model and true
  PSF integrated in pixel i, normalised), worst in the read-noise limit
  [src: Sect. IV.3.3]. The driver is sky subtraction, since sky residuals
  set the ELG false-identification rate (a level-2 requirement); only
  fibre-to-fibre errors matter, a common one being absorbed by the mean
  sky [src: same].
- **Peers: a 1D cross-dispersion profile.** BOSS takes traces and
  Gaussian widths from quartz-lamp flats and holds them fixed in the
  extraction (arXiv:1208.0022) [src: Sect. IV.3]. For AAOmega a Gaussian
  profile is "an acceptable first approximation"; centroid errors of
  0.2 pixel (6% of the FWHM) are tolerable but widths must be known to
  < 0.1 pixel (~3%) for any extraction method (Sharp & Birchall 2010,
  arXiv:0912.0558) [src: Sects. 4, 4.1].

### Step 3. Trace and wavelength solution, then re-fit on each exposure
<!-- key: step-3-trace-and-wavelength-solution-then-re -->

Per hardware setup, traces come from continuum (LED) lamps and arc peaks
are matched to line lists by voting on ordered triplets in a 4D histogram
(after Valdes et al.) [src: arXiv:2209.14482, Sect. IV.4.1]. On each
science exposure, offsets δX are re-fitted as a low-order 2D polynomial of
(X, Y) with outlier rejection, and δY by cross-correlating boxcar spectra
of all fibres on sky lines, tied to a UVES Paranal sky spectrum at DESI
resolution [src: Sect. IV.4.2]. Reason: traces drift with the room's
humidity (suspected NIR dichroic tilt): ±0.7 pixel peak to peak and
0.3 pixel rms along X in the blue, 0.15 and 0.03 in red and NIR, about
0.05 pixel (≈ 0.03 Å) along Y [src: same, Fig. 17]. Spectra are then
shifted to a vacuum barycentric frame (arXiv:2503.14745)
[src: Sect. III.1.1].

Peers. BOSS shifts flat-field traces to each frame for flexure (Numbers)
and the arc solution to each exposure's sky lines (arXiv:1208.0022)
[src: Sect. IV.3]; SDSS-V adopted the MaNGA arc list and sky lines as a
second-level calibrator for radial velocities (arXiv:2301.07688)
[src: Sect. X.1]; LAMOST corrects a 0.1 Å instability with sky lines, to
about 4.5 km s⁻¹ (arXiv:1705.02079) [src]. Slitless Euclid NISP locates
spectrograms from a photometric source catalogue [src: Abstract]; against
a requirement of < 38% of a resolution element it reaches 17% on the
reference planetary nebula (a lower limit: bright, compact) and < 30% on
the Mg I line of bright stars (Euclid Collaboration: Copin et al. 2025,
arXiv:2503.15307) [src: Sect. 3.2; Numbers].

### Step 4. Extract by forward-modelling the 2D image
<!-- key: step-4-extract-by-forward-modelling-the-2d-image -->

The CCD counts are p = A f + n (Bolton & Schlegel 2010, arXiv:0911.2689,
Eq. 2), A the calibration matrix (traces, wavelength, PSF, flat,
throughput), f the spectrum on a grid. The weighted least-squares f has
C⁻¹ = Aᵀ N⁻¹ A (Eq. 8) but is deconvolved, rings and is strongly
correlated [src: Sect. III]. With the symmetric non-negative root
C⁻¹ = Q Q (Eq. 9), row sums s_ℓ̃ = Σ_ℓ Q_ℓ̃ℓ (Eq. 10) and R = s⁻¹ Q
(Eq. 11), f̃ = R f (Eq. 15) has diagonal covariance C̃ = R C Rᵀ
(Eqs. 12–14) at native resolution; any model must be multiplied by R
before a χ² [src: same]. Against row-by-row optimal extraction: it is
correct only for a separable PSF, I(x, y) = I_x(x) I_y(y) (Eq. 1), which
almost no real PSF is; with sharp sky lines the cross-section depends on
the spectrum and the extraction "becomes ill-defined"; on a simulated
emission-line spectrum the two differ "at the few percent level"
[src: Sects. II, III].

DESI settings: bins whose summed pixel weight is below 10⁻⁴ of the maximum
are regularised towards zero flux, "empirically tuned" between ringing and
bias on bright bins; flags bad2dfit (pixel χ² > 100), somebadpix (> 50% of
input pixels masked), allbadpix [src: arXiv:2209.14482, Sect. IV.5.3]. On
10,000 simulated CCD images pulls have mean 0 and standard deviation 1 and
bins are uncorrelated [src: Sect. IV.5.6].

Peers.
- **BOSS, row-wise optimal extraction**, in bundles of 20 fibres on the
  flat-field Gaussian profiles, fitting only amplitudes per wavelength and
  a linear cross-dispersion background per bundle for scattered light; on
  native pixels the bins are independent but not aligned in wavelength
  between spectra or exposures (arXiv:1208.0022) [src: Sect. IV.3].
- **AAOmega, multi-profile deconvolution**: all overlapping profiles fitted
  at once, which avoids the double counting of a sum (default mode: 392
  fibres, pitch 10.0 px, FWHM 3.4 px; contamination levels in Numbers);
  exact in the noise-free model, and on SPIRAL IFU data an order of
  magnitude less cross-talk signature (arXiv:0912.0558) [src: Sect. 4,
  Table 1, Sect. 9].
- **Euclid slitless**: neighbours' spectra are modelled and subtracted
  first [src: Abstract]; the 2D spectrogram is resampled once (4 × 4
  hyperbolic-tangent kernel), rotated and sheared so the source's long axis
  (the "virtual slit") lies across the dispersion, minimising
  self-contamination and the effective LSF (Eq. 1); the 1D spectrum is the
  mean of unmasked pixels times the aperture width, NOT_USE (LOW_SNR) below
  50% (75%) unmasked (arXiv:2503.15307) [src: Sect. 2.3.7].

### Step 5. Fibre flat field from the dome screen
<!-- key: step-5-fibre-flat-field-from-the-dome-screen -->

T_{k,i} and a mean deconvolved spectrum S_j are fitted together,
χ² = Σ_k Σ_i w_{k,i} (F̃_{k,i} − T_{k,i} Σ_j R_{k,i,j} S_j)² with
⟨T_{k,i}⟩_k = 1 (Eq. 12), first with smooth functions and cosmic-ray
rejection, then exactly [src: arXiv:2209.14482, Sect. IV.6.1]; twelve
2-min exposures are combined [src: Fig. 24].

- **Why a lamp.** Night sky imprints its lines and needs prohibitive time
  in the faint continuum; twilight is better but not ideal; LEDs on a white
  dome screen are smooth and stable but illuminate unlike the night sky
  [src: Sect. IV.6].
- **One lamp at a time.** Each of the four lamps is flat-fielded
  separately, then combined: a change in one lamp is absorbed in S_j when
  used singly but becomes a gradient when lamps are used together; four
  lamps give azimuthal uniformity better than 0.1%, with about 1% radial
  difference from the sky expected from vignetting; all cameras of a type
  share one mean spectrum, which inter-calibrates the ten spectrographs
  [src: Sect. IV.6.2].
- **Validation.** Corrected twilight flats show a few-percent gradient
  along one axis (sky brightness with elevation), the same in the three
  cameras, i.e. geometric and achromatic; dark-sky fibres over four nights
  show a 2% radial pattern against 1% simulated, absorbed by the per-fibre
  sky normalisation (Step 6) [src: Sect. IV.6.3, Fig. 28].
- **Humidity.** Collimator reflectivity dips at 3800 and 4400 Å move with
  humidity (8% in winter to 50% in summer); a humidity-binned model
  corrects afternoon calibrations to the night [src: Sect. IV.6.4].
- **Peers.** BOSS divides by extracted quartz-lamp flat spectra
  (arXiv:1208.0022) [src: Sect. IV.3]. LAMOST uses twilight flats, then
  rescales each fibre by its sky-line flux over the median of all fibres
  ([OI] 5577 Å in the blue, median of 19 OH lines in the red, Eq. 6), the
  role of DESI's α_k (Step 6): scale factors scatter by 5.8% (vignetting,
  positioner), the blue-to-red ratio by 2.8%, taken as the correction's
  accuracy and matched to 1.5% per line and 1.6% per twilight flat
  (arXiv:1705.02079) [src: Sect. 3.3].

### Step 6. Sky model, its normalisation and its residual corrections
<!-- key: step-6-sky-model-its-normalisation-and-its -->

The mean sky is fitted on sky fibres per camera (Guy et al. Eq. 14, in
L2), optionally with a polynomial P in focal-plane position and
wavelength, iterating until the χ² decrement is below a threshold and no
outlier remains; OH-line intensity variations relative to the continuum
are not modelled in that version [src: arXiv:2209.14482, Sect. IV.7.1].

- **Per-fibre scale α_k.** Sky lines from a list are fitted with a local
  background in 9 Å windows and combined (inverse-variance weights, 3σ
  clipping) into one achromatic factor per fibre and camera, typically 1%,
  absorbing trace-centring and flat errors and real throughput changes from
  fibre flexure (focal-ratio degradation) or vignetting [src: Sect. IV.7.2].
  DR1 (Iron) replaced it by a fibre-throughput model versus positioner
  location (arXiv:2503.14745) [src: Sect. III.1.3].
- **PCA of calibration offsets.** Real data left bright-line residuals,
  worst above 9000 Å, equivalent to wavelength errors of about 0.02 Å (3%
  of a pixel) and LSF-width errors of a few 0.1 Å, stable in time,
  correlated over 10–20 fibres, of unknown cause (working hypothesis:
  dome-versus-sky illumination) [src: arXiv:2209.14482, Sect. IV.7.3].
  Per sky line and sky fibre an amplitude, Δλ and ΔLSF are fitted; Δλ and
  ΔLSF maps from 2020 sky data are decomposed by PCA, four components per
  camera stored, and each exposure's sky fibres set the coefficients for
  all fibres (Eq. 15: sky = α_k R P S + Σ_l X_l^(λ) ∂_λ S̃ C_l^(λ) + Σ_p
  X_p^(LSF) ∂_LSF S̃ C_p^(LSF), the LSF derivative from an extra
  σ = 0.3 Å Gaussian) [src: same].
- **Variance after subtraction** (Eq. 16): σ²_corr = σ²_extract T⁻² +
  σ²_S̃ + (σ_T S̃)² + (ε_λ ∂_λ S̃)², σ_S̃ the sky-model error for the mean
  resolution, σ_T the flat error, ε_λ (typically 0.025 Å) set per sky line
  for χ²/ndf = 1 within ±3 Å on sky fibres and applied to all fibres only
  there [src: Sect. IV.7.4, Fig. 32]. Neighbour correlations are about −0.8
  in the deconvolved sky but a few percent after reconvolution, so only
  the diagonal for the mean R is stored [src: same, Fig. 31].

Peers (variants and costs side by side in Choices, including Euclid's
slitless background; levels in Numbers).
- **BOSS** subtracts a sky model from the sky fibres that varies smoothly
  over the focal plane (arXiv:1208.0022) [src: Sect. IV.3]. Its OH
  residuals longward of 6700 Å lowered the S/N of many SDSS spectra by
  more than a factor of 2 over substantial ranges (Wild & Hewett 2005,
  arXiv:astro-ph/0501460) [src: Abstract]. Their post-pipeline PCA (15,178
  sky spectra; stopping rule and risk in Choices) removes a 55-pixel median
  continuum and projects the noise-normalised spectrum on the sky
  eigenvectors with known features masked [src: Sects. 2.2.1, 2.3].
- **LAMOST** (method in Choices; levels in L2): on about 11,000 F stars
  of SDSS DR10 and LAMOST DR3 matched in [OI] 5577 Å and OH 7913 Å
  strength and continuum counts, LAMOST has the smaller sky-line
  residuals, more so in the red; its reasons are denser sky sampling (25
  per 250 fibres on the CCD against 32 per 640; sky density in Numbers)
  and the PCA step, which SDSS does not run, while "many other details"
  may contribute (arXiv:1705.02079) [src: Sect. 4.4].
- **FLAMES/GIRAFFE** (VLT, 820–920 nm), three pure-sky fibre pairs,
  residual (object − sky)/median sky, wavelet-smoothed, sky-line regions
  excluded [src: arXiv:1609.06142, Sect. 2.3]: dual stare and cross-beam
  switching reach < 1%, mean and closest sky ten times worse, a result the
  authors limit to instruments as stable as FLAMES-GIRAFFE, expecting dual
  stare to win in the near-IR (Rodrigues et al. 2016) [src: Sect. 3,
  Table 1].
- **WEAVE**: sky subtraction, instrumental signatures and wavelength and
  flux calibration belong to the Core Processing System, whose per-arm
  output carries sky and variance; the survey paper does not describe the
  method (Jin et al. 2023, arXiv:2212.03981) [src: Sect. 2.6].

### Step 7. Standard stars and flux calibration
<!-- key: step-7-standard-stars-and-flux-calibration -->

- **Selection.** About ten F stars per petal (cuts in Numbers), 15 < g < 18
  (bright) or 16 < g < 19 (faint); the parallax cut favours low-metallicity
  halo stars, the proper-motion cut avoids peculiar cool-kinematics stars
  [src: arXiv:2209.14482, Sect. IV.8].
- **Model fit.** Allende Prieto et al. grid (R = 10,000; T_eff in 500 K
  steps, [Fe/H] −5 to +1 in 0.5 dex, log g 1–5 in 1 dex) [src: Sect. IV.8.1].
  Data and model are divided by a 160 Å sliding-median continuum (width
  empirical) so no prior calibration is needed; extra variance 0.12; sky
  lines, tellurics and interstellar Ca H&K masked; radial velocity by
  cross-correlation with a 6000 K, log g = 4, [Fe/H] = −1.5 model over
  ±1500 km s⁻¹ in 15 km s⁻¹ steps; models restricted to dust-corrected
  g − r within ±0.2; trilinear interpolation; refit after a first
  calibration [src: Sect. IV.8.2]. Check: g − r rms 0.023, about 100 K
  [src: Fig. 37].
- **Rejection**: 3σ outliers in measured-to-model r flux over
  6000–7300 Å, and Δ(g − r) > 0.1 + 0.2 E(B − V), relaxed with extinction
  for reddening-law uncertainty [src: Sect. IV.9.1]. **Calibration vector**:
  per camera, a mean deconvolved C_j with a scale α_k per star for
  positioning offsets and outliers (Eq. 17), convolved with each fibre's R
  [src: Sect. IV.9.2].
- **Aperture losses.** With a Moffat focal-plane PSF (β = 3.5), fibre
  radius r_F (varying with plate scale), seeing s and positioning offset,
  the point-source acceptance F_PSF gives the applied "flat to PSF" factor
  ⟨F_PSF(s)⟩ / F_PSF(s, r_F) × r_F² / ⟨r_F²⟩ (Eq. 18); a "PSF to fiber"
  factor for a 1.5″ fibre in 1″ seeing and an exponential profile (Eq. 19)
  is stored as PSF_TO_FIBER_SPECFLUX, not applied [src: Sect. IV.9.3]: the
  default is total flux for point sources, a lower limit for extended ones
  [src: Sect. IV.9].
- **Peers.** BOSS fits the response over the focal plane from standards
  placed at plate design, with their PSF magnitudes as baseline
  (arXiv:1208.0022) [src: Sects. IV.3, VI.1]. WEAVE plans white dwarfs,
  whose mostly pure-hydrogen spectra are modelled to 1–2% at all
  wavelengths with T_eff and log g and carry blue flux; the IFU modes,
  with at most one per pointing, must bootstrap from other exposures or
  known magnitudes (arXiv:2212.03981) [src: Sect. 4.3.1; counts in
  Numbers]. PFS gives several tens of fibres per exposure to F-star
  standards chosen from Pan-STARRS1 and Gaia photometry, for a 2D
  pipeline whose paper is in preparation (arXiv:2604.09875)
  [src: Sect. VII.3]. Euclid derives one sensitivity function per grism
  and tilt from 80 single-dither spectra of the white dwarf GRW+70 5824
  taken in performance verification, against its CALSPEC model convolved
  to 3.3 nm, with flags in Numbers (arXiv:2503.15307) [src: Sect. 2.4.4].

### Step 8. Fibre cross-talk and co-addition
<!-- key: step-8-fibre-cross-talk-and-co-addition -->

**Cross-talk.** The omitted tails are a kernel K(r) ∝ r² (1 + r²)^−(1+p/2),
p ≈ 2.5, normalised per camera on sky-fibre residuals over several hundred
exposures; first- and second-neighbour contamination is subtracted from
the extracted spectra without iteration, being small; adjacent-fibre
levels in Numbers [src: arXiv:2209.14482, Sect. IV.10, Fig. 42].

**Co-addition.** Inverse-variance mean per bin (no resampling: one grid
for all fibres), R_coadd = Σ_i w_i R_i with the same weights (Eq. 20), 4σ
outlier rejection in the main survey; cameras are not merged before the
redshift fit, to avoid mixing resolutions [src: arXiv:2209.14482,
Sect. IV.11]. In DR1 the coadd R was mis-weighted
(L2 known issues) (arXiv:2503.14745) [src: App. E].

**Peers.** BOSS coadds a fibre's exposures on a grid linear in log λ,
merging red and blue over 361–1014 nm, propagating pixel variance and
discarding covariances (arXiv:1208.0022) [src: Sect. IV.3]; SDSS-V groups
exposures by sky position or CatalogID, not plate-MJD-fibre, and coadds
red with blue per exposure, then across exposures (arXiv:2301.07688)
[src: Sect. X.1]. AAOmega removes cross-talk inside the extraction
(Step 4) rather than afterwards (arXiv:0912.0558) [src: Abstract,
Sect. 9].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Row-by-row optimal extraction or 2D forward model
<!-- key: row-by-row-optimal-extraction-or-2d-forward -->

Row-wise optimal extraction (BOSS, Step 4) is cheap and gives
uncorrelated pixels, but only for a separable PSF, and rebinning to
combine exposures correlates them (arXiv:0911.2689) [src: Sect. II]. The
2D model (DESI) needs a calibrated 2D PSF per fibre and wavelength
(Step 2) and a large sparse solve, and is not flux-conserving per bin
(fit R·M, not M; L2), but keeps native resolution and independent pixels
and makes co-addition a weighted mean (Step 8); on one simulation the two
differ by a few percent, the 2D LSF being sharper [src: arXiv:0911.2689,
Sect. III]. On real data, the MINERVA pipeline runs both on 119 exposures
of an RV standard: "both ... achieve nearly identical RV precision" under
six-exposure binning, the 2D extraction taking about 30 min per exposure
(Cornachione et al. 2019, arXiv:1911.04985) [src: Abstract]. Strongly
overlapping profiles need a simultaneous fit in either geometry
(AAOmega, Step 4).

### PSF core only, or core plus tails
<!-- key: psf-core-only-or-core-plus-tails -->

Tails inside the extraction treat cross-talk exactly but spread cosmic
rays; DESI corrects cross-talk after extraction (Steps 2, 8), at the price
of a camera-dependent calibration reaching 1.5% in the NIR
[src: arXiv:2209.14482, Sects. IV.3.1, IV.10]; AAOmega deconvolves
neighbours inside the extraction (Step 4).

### Where the sky-line residual correction comes from
<!-- key: where-the-sky-line-residual-correction-comes -->

| Variant | What it fits | Cost | Used by |
|---|---|---|---|
| Per-fibre achromatic scale from sky lines | one α_k per fibre and camera, ~1% | cannot follow wavelength or LSF errors | DESI EDR [src: arXiv:2209.14482, Sect. IV.7.2] |
| Throughput model versus positioner location | replaces α_k | needs the positioner history | DESI DR1 (arXiv:2503.14745) [src: Sect. III.1.3] |
| PCA of calibration offsets (Δλ, ΔLSF) from a sky library | four components per camera, coefficients from sky fibres per exposure | assumes a stable pattern; cause unknown | DESI [src: arXiv:2209.14482, Sect. IV.7.3] |
| Frame-by-frame PCA of continuum-subtracted residual spectra | 30 leading components from ~400 spectra, 20–25 of them sky fibres | rolling-median continuum removal can touch the source | AAOmega / GAMA (arXiv:1007.0648) [src: Sect. 2.3] |
| Nod-and-shuffle | sky through the object fibre | 2√2 loss in S/N for fixed time under the paper's baseline assumptions (half the time, half the fibres, twice the sky) | comparison baseline (arXiv:1007.0648) [src: App. B.2] |
| Post-pipeline PCA of residuals from a large sky library | components added per spectrum until sky and non-sky pixel rms agree (≤ 150 galaxies, ≤ 200 quasars) | can absorb narrow features on OH lines unless masked | SDSS DR2 spectra, Wild & Hewett (arXiv:astro-ph/0501460) [src: Sects. 2.2.1, 2.3] |
| B-spline master sky, scaled by sky-line throughputs (Step 5), then PCA on the red residuals (a further 25% off the OH residual) | 20 sky fibres per spectrograph; one scale per fibre | throughput scatter 5.8% to correct; 2.8% accuracy | LAMOST DR3+ (arXiv:1705.02079) [src: Abstract, Sect. 3.3] |
| Mean or closest sky fibre | no model | FLAMES, accuracy/precision on three pure-sky pairs: mean 0.07/0.09, 0.16/0.24, 0.04/0.06; closest 0.03/0.03, 0.10/0.10, −0.015/0.037 | FLAMES test (arXiv:1609.06142) [src: Table 1] |
| Dual stare or cross-beam switching | sky through a paired or the same fibre | multiplex lost; FLAMES accuracy within ±0.003, precision 0.006–0.008 on two pairs, 0.09–0.10 on the third, where every method is at that level | FLAMES test (arXiv:1609.06142) [src: Table 1, Sect. 3] |
| Uniform background per detector (slitless, no sky fibres) | mode of pixels outside the 0th- and 1st-order spectrograms of sources with J_E ≤ 23 | no stray-light or ghost model in Q1 | Euclid Q1 (arXiv:2503.15307) [src: Sect. 2.3.5] |

Comparisons the papers make: PCA with dedicated sky fibres matches
nod-and-shuffle for 10–100 h on source and is superior when multiplex and
efficiency matter, and differs from the SDSS scheme it derives from by
computing eigenvectors per frame, not from a large library
[src: arXiv:1007.0648, Sects. 7, 2.3]. LAMOST against SDSS and the FLAMES
modes: Step 6.

### Pixel variance from the data or from a model
<!-- key: pixel-variance-from-the-data-or-from-a-model -->

The data-based variance (Eq. 2) is simple and biases sky, calibration and
spectra through the value–variance correlation; the model-based variance
needs a first extraction and sky model but keeps the pipeline linear
[src: arXiv:2209.14482, Sect. IV.2.9]. BOSS DR9 kept the single-pass
data-based variance and states its bias (weighted means suppressed at
zero flux) as known and uncorrected (arXiv:1208.0022) [src: Sect. IV.3].

### Calibration stars at the targets' focus or not; total or fibre flux
<!-- key: calibration-stars-at-the-targets-focus-or-not -->

BOSS drilled quasar holes for λ_eff = 4000 Å, to raise Lyα-forest
throughput, while its 20 standards per plate were at 5400 Å, and the
pipeline interpolated standard-star calibrations to all fibres regardless
(Margala et al. 2016, arXiv:1506.04790) [src: Sects. II, III.3]. The fix
scales each spectrum by the ratio of fibre acceptances at the assumed and
actual design wavelengths, R_i*(λ) = A_i*(λ, λ_c, h_obs) /
A_i*(λ, λ_i, h_obs) (Eq. 13), A* the acceptance under ideal guiding at
hour angle h_obs [src: Sect. III.3]; BOSS quasar flux was on average 19%
too high at 3600 Å and 24% too low at 10,000 Å [src: Abstract]. On 486
"offset standards" placed like quasars, the g − r residual against imaging
goes from −0.117 to +0.006 mag (0.010 with a calibration on the offset
standards themselves) [src: Sect. IV, Table 2]. DESI positions all fibres
for the red and accepts a chromatic focal-plane pattern (Step 7; What goes
wrong). Total point-source flux is exact for stars and quasars and a lower
limit for galaxies; the stored PSF-to-fibre factor gives fibre fluxes
consistent with imaging for both, 6% scatter at the bright end
[src: arXiv:2209.14482, Sect. IV.9.3, Fig. 38].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Cosmic-ray thresholds | N = 6, then 3; c = 3; c₂ = 0.5 | DESI | arXiv:2209.14482 | Sect. IV.2.4 |
| Negative-trail kernel | A = 5×10⁻⁵–1.2×10⁻³; L = 4–35 px | DESI, 8 amplifiers | arXiv:2209.14482 | Table 1 |
| PSF stability, δF/F | ≤ 0.6% over hours; night-to-night above the 1% requirement in one blue camera set | DESI SM10, March 2020 | arXiv:2209.14482 | Sect. IV.3.3 |
| Trace drift rms along X | 0.3 (b), 0.15 (r), 0.03 (z) px; Y 0.05 px ≈ 0.03 Å | DESI SM2 | arXiv:2209.14482 | Fig. 17 |
| Dome vs sky illumination | 1% radial expected; 2% measured | DESI | arXiv:2209.14482 | Sects. IV.6.2–IV.6.3 |
| Sky-line calibration residuals | Δλ ≈ 0.02 Å; ΔLSF a few 0.1 Å; 4 PCA components | DESI | arXiv:2209.14482 | Sect. IV.7.3 |
| ε_λ | ~0.025 Å, ±3 Å windows | DESI | arXiv:2209.14482 | Sect. IV.7.4 |
| Standard-star cuts | 0 < g−r < 0.35, r−z < 0.2, parallax < 1 mas, PM > 2 mas/yr | DESI | arXiv:2209.14482 | Sect. IV.8 |
| Stellar-fit settings | 160 Å continuum; extra variance 0.12; RV ±1500 km/s, 15 km/s steps | DESI | arXiv:2209.14482 | Sect. IV.8.2 |
| Stellar-fit colour check | rms 0.023 in g−r (~100 K) | DESI, one 900 s exposure | arXiv:2209.14482 | Fig. 37 |
| Star rejection | 3σ in r ratio; Δ(g−r) > 0.1 + 0.2 E(B−V) | DESI | arXiv:2209.14482 | Sect. IV.9.1 |
| Focal-plane PSF | Moffat β = 3.5 | DESI | arXiv:2209.14482 | Sect. IV.9.3 |
| Chromatic positioning loss | ~10% for 0.3″ (20 μm) offset; red optimised | DESI | arXiv:2209.14482 | Sect. IV.9.3 |
| Fibre-flux scatter vs imaging | 6% (bright end) | DESI dark tiles | arXiv:2209.14482 | Sect. IV.9.3 |
| Cross-talk, adjacent fibres | 0.1–0.2% (b, r); in z rising above 8900 Å to 1.5% at 9800 Å | DESI | arXiv:2209.14482 | Sect. IV.10, Fig. 42 |
| BOSS quasar miscalibration | +19% at 3600 Å; −24% at 10,000 Å | BOSS DR12 | arXiv:1506.04790 | Abstract |
| BOSS offset-standard g−r residual | −0.117 → +0.006 mag (486 stars) | BOSS DR12 | arXiv:1506.04790 | Table 2 |
| AAOmega PCA | 30 components; 20–25 sky fibres of ~400 | GAMA | arXiv:1007.0648 | Sect. 2.3 |
| DESI DR1 noise power underestimate (Lyα forest, k > 3.1 Å⁻¹) | 2.8% (α = 6.9 × 10⁻⁴ Å) | DESI DR1 P1D | arXiv:2505.09493 | Sect. 4.2 |
| Flexure shift of traces, calibration to science | typically 0.1 Å, up to 1.5 Å | BOSS | arXiv:1208.0022 | Sect. IV.3 |
| Spectrophotometry vs imaging (offset, rms in mag) | standards vs PSF: r 0.014 fainter (0.058), g 0.038 fainter (0.068), g−r 0.022 redder (0.063), r−i 0.004 bluer (0.035); galaxies vs fibre mags: g−r 0.048 (0.058), r−i 0.013 (0.035) redder; stars in the quasar sample: r 0.16 fainter (0.29) | BOSS DR9 | arXiv:1208.0022 | Sect. VI.1 |
| SDSS spectrophotometry, for comparison | rms 5% (g−r), 3% (r−i); ~12% at 3800 Å; small-scale relative calibration 1–2% | SDSS (as quoted by BOSS) | arXiv:1208.0022 [sec] | Sect. VI.1 |
| OH residuals before PCA; PCA components | S/N lowered > 2× over counting statistics in many spectra; ≤ 150 (galaxies), ≤ 200 (quasars) components, 18% / 5% need none | SDSS (DR2) | arXiv:astro-ph/0501460 | Abstract; Sect. 2.2.1, Fig. 8 |
| Fibre throughput scatter from sky lines; correction accuracy; sky-fibre density | 5.8%; 2.8%; 25 per 1.25 deg² (LAMOST) vs 32 per 7 deg² (SDSS) | LAMOST (vs SDSS) | arXiv:1705.02079 | Sects. 3.3, 4.4 |
| Profile tolerances; contamination with summation extraction | centroid 0.2 px (6% FWHM), width < 0.1 px (~3%); < 1.6% for Δmag < 3 at pitch 10 px, > 10% flux error in dense modes for Δmag < 0.3 | AAOmega simulations | arXiv:0912.0558 | Sects. 4, 4.1 |
| Sky residual by method (accuracy/precision, best pair) | mean 0.037/0.058; closest −0.015/0.037; dual stare −0.0002/0.0060; cross-beam −0.0012/0.0059 | FLAMES, 820–920 nm | arXiv:1609.06142 | Table 1 |
| Wavelength accuracy; sensitivity function | 0.23 px = 17% of a resolution element (requirement < 38%), ~0.7 nm rms on stars; 80 spectra of GRW+70 5824, NOT_USE if > 5% off pre-launch, ABS_FLUX where throughput < 80% of maximum | Euclid Q1 red grism | arXiv:2503.15307 | Sects. 3.2, 2.4.4 |
| White-dwarf flux standards | 10–15 per pointing (LR MOS), 3–5 (HR), ≤ 1 (IFU); models good to 1–2% at all wavelengths | WEAVE, planned | arXiv:2212.03981 | Sect. 4.3.1 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **A model that passes simulations fails on sky lines.** The DESI sky
  model "was successfully tested on simulations", yet real data needed the
  empirical PCA of Step 6 [src: arXiv:2209.14482, Sect. IV.7.3]. Test: rms
  of sky-fibre residuals against Eq. 16 with ε_λ = 0, flagging bins whose
  excess exceeds 1% and 3% of the sky; with ε_λ fitted the scatter must
  match the model at most wavelengths [src: Sect. IV.7.5, Figs. 33–34].
- **PSF or trace drift between afternoon calibration and night**: continuum
  offsets between fibres and line residuals. Test: Eq. 4 across exposures,
  dome positions and positioner moves against the 1% requirement
  [src: Sect. IV.3.3]; per-exposure trace re-fit [src: Sect. IV.4.2].
- **Variance wrong in the released spectra.** DR1's flux-calibration
  variance bug (factor up to 5 at S/N ≈ 100 per pixel) is a known issue
  (arXiv:2503.14745) [src: App. E]; independently, the DR1 Lyα P1D finds
  the noise power 2.8% below the small-scale power and uses a
  cross-exposure estimator for z < 2.7 (arXiv:2505.09493) [src: Sects. 4.2,
  7]. Test: raw against noise power where resolution kills the signal;
  pulls on repeats.
- **Bad calibration data for one night** on spectrograph 9 gave wrong
  redshifts for 8500 spectra, fixed by reprocessing with better calibration
  data; DR1 backup-programme data show 2–3 km s⁻¹ radial-velocity scatter
  (up to 20) from wavelength calibration (arXiv:2503.14745) [src: App. E].
- **Chromatic aperture losses.** Stellar spectroscopic-to-imaging flux
  ratios show focal-plane structure in blue and NIR from corrector
  chromatic distortion, not corrected in EDR [src: arXiv:2209.14482,
  Sect. IV.9.3, Fig. 39]; in BOSS, the design-wavelength offset of quasars
  (arXiv:1506.04790) [src: Sect. III.3]. Test: offset standards or star
  flux ratios over the focal plane.
- **Blue-end flux calibration.** DA white-dwarf residuals show a ~6% step
  below ~3700 Å (L2 row), partly perhaps from the white-dwarf fitting
  pipeline, with E(B − V) not yet included, as the authors note
  [src: arXiv:2209.14482, Sect. IV.9.4].
- **Residual cosmic rays** bias PSF fits and make false lines; caught by
  bad2dfit and the 4σ coadd clipping [src: Sects. IV.5.3, IV.11].
- **Validation suites as the papers state them**: DESI, Steps 4–7
  (extraction pulls, sky residuals against Eq. 16, stellar-fit colours,
  white dwarfs, fibre fluxes against imaging); BOSS, synthetic against
  imaging magnitudes with normalised-MAD dispersions [src: arXiv:1506.04790,
  Table 2] and repeat plates at two airmasses [src: arXiv:1208.0022,
  Sect. VI.1, Fig. 9]; LAMOST, matched F stars across surveys; FLAMES,
  pure-sky fibre pairs; Euclid, line positions on a planetary nebula and
  bright stars (Steps 3, 6).
- **Refraction and offset focal planes.** BOSS stars targeted as quasars
  are 0.16 mag too faint (Numbers), and a quasar seen at airmass 1.2 and
  1.4 turns bluer at 1.4 (arXiv:1208.0022) [src: Sect. VI.1, Fig. 9];
  correction: Margala et al. (Choices).
- **Trade-offs in the calibration.** SDSS-V's 50σ outlier threshold keeps
  sky lines but can leave a cosmic-ray remnant (arXiv:2301.07688)
  [src: Sect. X.1]; Euclid Q1 over-flagged ABS_FLUX on the blue side by a
  software error, fixed for later releases (arXiv:2503.15307)
  [src: Sect. 2.4.4].

## Reading list
<!-- key: reading-list -->

- Foundation: Bolton & Schlegel 2010, arXiv:0911.2689 (optimal extraction
  and non-separable PSFs; the resolution matrix).
- Method: Guy et al. 2023, arXiv:2209.14482, Sects. IV.2–IV.11 (every DESI
  calibration product, fit and validation); DR1 changes and known issues,
  arXiv:2503.14745, Sect. III.1, App. E.
- Method, sky: Sharp & Parkinson 2010, arXiv:1007.0648 (frame-by-frame PCA,
  sky-fibre failure modes in App. A, nod-and-shuffle cost).
- Critique: Margala et al. 2016, arXiv:1506.04790 (BOSS quasar focal plane,
  offset standards). Test from science: DESI DR1 Lyα P1D, arXiv:2505.09493,
  Sect. 4.2.
- Peer pipelines: BOSS idlspec2d and spectrophotometry, Dawson et al.
  2013, arXiv:1208.0022, Sects. IV.3, VI.1; SDSS-V changes,
  arXiv:2301.07688, Sect. X.1; overlapping-profile extraction, Sharp &
  Birchall 2010, arXiv:0912.0558; 2D against optimal extraction on real
  data, Cornachione et al. 2019, arXiv:1911.04985; SDSS sky-residual PCA,
  Wild & Hewett 2005, arXiv:astro-ph/0501460; LAMOST sky and its SDSS
  comparison, Bai et al. 2017, arXiv:1705.02079; sky modes on sky,
  Rodrigues et al. 2016, arXiv:1609.06142; slitless, Euclid Collaboration:
  Copin et al. 2025, arXiv:2503.15307; WEAVE processing and white-dwarf
  standards, Jin et al. 2023, arXiv:2212.03981, Sects. 2.6, 4.3.1.
- Alternatives (in L2): arXiv:astro-ph/0303507, arXiv:2312.06761.

## Not verified
<!-- key: not-verified -->

- BOSS idlspec2d: read through the survey overview (arXiv:1208.0022);
  the pipeline paper it cites (Schlegel et al.) and the B-spline form of
  the sky model were not read.
- DESI DR1 positioner-location throughput model: only a code pull request
  is cited (arXiv:2503.14745); performance not read.
- 4MOST: the 2019 project overview could not be read (no HTML or LaTeX
  source); no pipeline paper found. MOONS: none found. 2dF/2dfdr beyond
  the AAOmega papers: not read.
- PFS 2D pipeline: paper "in preparation" (Tanaka et al., cited in
  arXiv:2604.09875). WEAVE CPS method papers (Walton et al. 2014, cited in
  arXiv:2212.03981): not read.
- Euclid SIR decontamination, relative flux scaling and location
  calibrations (arXiv:2503.15307, Sects. 2.3.6, 2.3.8, 2.4.1): not read.
- Horne 1986 (doi:10.1086/131801) body not read; its variance argument is
  quoted through arXiv:2209.14482, Sect. IV.2.9.
