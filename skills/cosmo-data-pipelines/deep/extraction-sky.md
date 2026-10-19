# CCD pre-processing, spectral extraction, flux calibration and sky subtraction — cosmo-data-pipelines dossier

Scope: how a fibre spectrograph's calibration products are built and used
(pixel variance, 2D PSF, traces and wavelengths, fibre flat, sky model and
its residual corrections, standard stars, aperture losses, cross-talk,
co-addition), with the reason for each setting, and how to choose between
variants; read in the DESI pipeline paper, with BOSS, AAOmega and
spectro-perfectionism for the alternatives.
Snapshot: 2026-10-18.
From: Guy et al. 2023, Sect. IV.2–IV.11 (copied from
`references/subtopics.tsv`).

Already in L2, not repeated here: the order of operations of the DESI
pipeline, the three sky-subtraction families with the DESI sky-fit equation
(Guy et al. Eq. 14), the ε_λ noise term in one sentence
(`physics-and-methods.md#spectral-extraction-calibration-and-sky`); the
sky-residual, white-dwarf and LAMOST numbers
(`results.md#spectral-extraction-and-sky-subtraction`); the sky-residual
systematic (`systematics.md#sky-subtraction-residuals`) and the DR1 variance
bug (`systematics.md#data-product-defects-found-after-release`). Photometric
zero points and dust maps are in `cosmo-photometry-photoz`. Notation follows Guy et al. 2023 (arXiv:2209.14482): k indexes fibres, i
the wavelength bins of the extracted spectrum, j the bins of a
deconvolved (high-resolution) model; F̃_{k,i} is the extracted flux,
w_{k,i} its inverse variance, R_{k,i,j} the resolution matrix, T_{k,i} the
relative fibre transmission (fibre flat).

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Pre-process the CCD and model the pixel variance
<!-- key: step-1-pre-process-the-ccd-and-model-the-pixel -->

- **Cosmic rays.** A pixel is masked if it stands above its two
  neighbours along at least two of four axes by N σ (Eq. 1a) and if its
  gradient is steeper than the spectrograph PSF allows along one axis
  (Eq. 1b), with N = 6, c = 3 and c₂ = 0.5 "adjusted on the data"; a
  second pass at N = 3 on neighbours of masked pixels is repeated until
  nothing new is masked, the mask is grown by one pixel, and a
  morphological closure with seven 11 × 11 structuring elements joins
  track fragments, the vertical element being dropped because it would
  align with the traces [src: arXiv:2209.14482, Sect. IV.2.4]. The reason
  for this care: unmasked hits become spurious emission lines and wrong
  ELG redshifts [src: same].
- **Negative trails.** Some red and NIR amplifiers leave a negative trail
  behind bright charge along the serial direction; it is linear and is
  subtracted as a convolution with K(x) = −(A/L) exp(−x/L), A between
  5 × 10⁻⁵ and 1.2 × 10⁻³ and L between 4 and 35 pixels per affected
  amplifier [src: Sect. IV.2.5, Table 1]. Changing the readout parameters
  did not remove it [src: same].
- **Scattered light** was modelled only for early, fogged-window data
  [src: Sect. IV.2.7].
- **Pixel variance.** Read noise from the overscan: 3.4, 2.7 and 2.5 e⁻
  rms in the blue, red and NIR CCDs [src: Sect. IV.2.9]. The common
  estimate σ̃²_P = σ²_R + P (Eq. 2) correlates the variance with the pixel
  value, so that an inverse-variance weighted mean of P is off by −1 at
  leading order, and it is truncated at low counts [src: same]. DESI
  instead builds a model image (boxcar extraction, flat, mean sky, target
  spectrum smoothed with a σ = 10 Å Gaussian, projected back with a
  Gaussian cross-section) and takes the Poisson term from the model,
  keeping the data value only where the pixel departs by more than 5σ
  [src: same].

### Step 2. Fit the 2D spectrograph PSF on arc lamps
<!-- key: step-2-fit-the-2d-spectrograph-psf-on-arc-lamps -->

The PSF is the image of the fibre tip (51 μm, 3.4 pixels after the
camera demagnification of 0.48) convolved with the camera blur, so it has
a central plateau [src: arXiv:2209.14482, Sect. IV.3.1]. DESI models its
core as Gauss–Hermite functions (Eq. 3):

PSF_H(x, y) = Σ_{i,j} a_{ij} He_i((x − x_c)/σ_x) He_j((y − y_c)/σ_y)
× exp[−(x − x_c)²/2σ_x² − (y − y_c)²/2σ_y²] / (2π σ_x σ_y),

with He_i the probabilists' Hermite polynomials of degree 0 to 6, (x_c, y_c)
the trace coordinates and every coefficient a Legendre polynomial in
wavelength per fibre [src: same]. Stated reasons: a linear basis converges
easily, is orthogonal (uncorrelated coefficients for small pixels), and
integrates analytically over pixels, which the sharp profile requires;
the cost is that degree 6 is needed for a partly resolved disk [src: same].

- **Tails left out on purpose.** A power-law tail component exists in the
  code but is not used: extended PSFs would spread every unmasked cosmic
  ray over many fibres, slow the extraction, and the post-hoc cross-talk
  correction (Step 8) was found precise enough [src: same].
- **Fit.** One fit per arc exposure with specex, Gauss–Newton least
  squares in three passes (trace and wavelength Legendre coefficients,
  then σ_x, σ_y, then a_{ij}), line intensities fitted throughout,
  separately for each block of 25 fibres (the slit has 20 blocks with a gap
  of about two fibre spacings) [src: Sect. IV.3.2]. No positivity is
  imposed in the fit; pixel-integrated values are forced positive at
  extraction [src: same].
- **Stability criterion.** The metric chosen is the emission-line flux
  bias from a PSF shape error, δF/F = Σ_i P_i P_i^truth / Σ_j P_j² − 1
  (Eq. 4; P_i the model and P_i^truth the true PSF integrated in pixel i,
  both normalised), worst in the read-noise limit [src: Sect. IV.3.3].
  The driver is sky subtraction, because sky residuals set the ELG false
  identification rate, a level-2 requirement; only fibre-to-fibre PSF
  errors matter, since a common error is absorbed by the mean sky
  [src: same].

### Step 3. Trace and wavelength solution, then re-fit on each exposure
<!-- key: step-3-trace-and-wavelength-solution-then-re -->

The initial solution per hardware setup takes traces from continuum (LED)
lamp exposures and matches arc peaks to line lists by voting on ordered
triplets in a four-dimensional histogram (after Valdes et al.)
[src: arXiv:2209.14482, Sect. IV.4.1]. On each science exposure, cross-
dispersion offsets δX are re-fitted as a low-order 2D polynomial of
(X, Y) with outlier rejection, and wavelength offsets δY by
cross-correlating boxcar spectra of all fibres on sky lines, finally tied
to a UVES sky spectrum from Paranal convolved to DESI resolution
[src: Sect. IV.4.2]. Reason: traces drift with the humidity of the
spectrograph room (suspected tilt of the NIR dichroic): ±0.7 pixel peak to
peak and 0.3 pixel rms along X in the blue, 0.15 and 0.03 pixel rms in the
red and NIR, about 0.05 pixel rms along Y (≈ 0.03 Å) in all cameras
[src: same, Fig. 17]. Spectra are then shifted to a vacuum barycentric
frame (arXiv:2503.14745) [src: Sect. III.1.1].

### Step 4. Extract by forward-modelling the 2D image
<!-- key: step-4-extract-by-forward-modelling-the-2d-image -->

The CCD counts are p = A f + n (Bolton & Schlegel 2010, arXiv:0911.2689,
Eq. 2), with A the calibration matrix (traces, wavelength, PSF, flat,
throughput) and f the input spectrum on a discrete grid. The weighted
least-squares f has inverse covariance C⁻¹ = Aᵀ N⁻¹ A (Eq. 8), but it is
deconvolved, rings and is strongly correlated [src: Sect. III]. Taking the
symmetric non-negative square root C⁻¹ = Q Q (Eq. 9), row sums
s_ℓ̃ = Σ_ℓ Q_ℓ̃ℓ (Eq. 10) and R = s⁻¹ Q (Eq. 11) gives a reconvolved spectrum
f̃ = R f (Eq. 15) with diagonal covariance C̃ = R C Rᵀ (Eqs. 12–14) at the
native resolution; any model must be multiplied by R before a χ²
[src: same]. Reason against row-by-row optimal extraction: it is correct
only for a separable PSF, I(x, y) = I_x(x) I_y(y) (Eq. 1), which almost no
real PSF is; with sharp sky lines the cross-section depends on the
spectrum itself and the extraction "becomes ill-defined"; on a simulated
emission-line spectrum the two extractions differ "at the few percent
level" [src: Sect. II, Sect. III].

DESI settings: wavelength bins whose summed pixel weight is below 10⁻⁴ of
the maximum get a regularisation term towards zero flux, "empirically
tuned" between ringing and bias on bright bins; flags bad2dfit (pixel
χ² > 100), somebadpix (> 50% of input pixels masked) and allbadpix
[src: arXiv:2209.14482, Sect. IV.5.3]. On 10,000 simulated CCD images the
pulls have mean 0 and standard deviation 1 and the bins are uncorrelated
[src: Sect. IV.5.6].

### Step 5. Fibre flat field from the dome screen
<!-- key: step-5-fibre-flat-field-from-the-dome-screen -->

The relative transmission T_{k,i} and a mean deconvolved spectrum S_j are
fitted together, χ² = Σ_k Σ_i w_{k,i} (F̃_{k,i} − T_{k,i} Σ_j R_{k,i,j} S_j)²
with ⟨T_{k,i}⟩_k = 1 (Eq. 12), first with smooth functions and outlier
rejection for cosmic rays, then exactly [src: arXiv:2209.14482,
Sect. IV.6.1]. Twelve 2-min exposures are combined [src: Fig. 24].

- **Why a lamp and not the sky.** Night sky would imprint its lines and
  needs prohibitive time in the faint continuum; twilight is better but
  not ideal; LEDs on a white dome screen are smooth and stable, at the
  cost of an illumination that differs from the night sky [src:
  Sect. IV.6].
- **One lamp at a time.** Exposures with each of the four lamps are flat-
  fielded separately and then combined, because an intensity change of
  one lamp is absorbed in S_j when lamps are used singly but becomes a
  gradient when they are used together [src: Sect. IV.6.2]. Four lamps
  give an azimuthally uniform illumination to better than 0.1%, with an
  expected radial difference from the sky of about 1% from vignetting
  [src: same]. All cameras of one type are normalised to the same mean
  spectrum, which inter-calibrates the ten spectrographs [src: same].
- **Validation.** Twilight flats after correction show a few-percent
  gradient along one axis (sky brightness with elevation) and are the same
  in the three cameras, i.e. geometric and achromatic; dark-sky fibres over
  four nights show a 2% radial pattern, a bit above the simulated 1%
  [src: Sect. IV.6.3, Fig. 28]. This residual is absorbed by the per-fibre
  sky normalisation (Step 6) [src: same].
- **Humidity.** Collimator reflectivity dips at 3800 and 4400 Å move with
  humidity (8% in winter to 50% in summer); a model binned in humidity
  corrects the change between afternoon calibration and night
  [src: Sect. IV.6.4].

### Step 6. Sky model, its normalisation and its residual corrections
<!-- key: step-6-sky-model-its-normalisation-and-its -->

The mean sky is fitted on sky fibres per camera (Guy et al. Eq. 14, in
L2), with an optional polynomial P over focal-plane position and
wavelength; iteration stops when the χ² decrement falls below a threshold
and no outlier remains [src: arXiv:2209.14482, Sect. IV.7.1]. Variations
of OH-line intensities relative to the continuum are not modelled in that
version [src: same].

- **Per-fibre scale α_k.** Each sky line in a list is fitted with a local
  background in a 9 Å window, and the amplitudes are combined with
  inverse-variance weights and 3σ clipping into one achromatic factor per
  fibre and camera, typically 1% [src: Sect. IV.7.2]. It absorbs trace
  centring errors, flat errors and real throughput changes from fibre
  flexure (focal-ratio degradation) or vignetting [src: same]. In DR1
  (Iron) this per-fibre, per-exposure scale was replaced by a model of
  fibre throughput as a function of positioner location
  (arXiv:2503.14745) [src: Sect. III.1.3].
- **PCA of calibration offsets.** Real data showed residuals on bright
  lines, worst above 9000 Å, equivalent to wavelength errors of about
  0.02 Å (3% of a pixel) and LSF-width errors of a few 0.1 Å, stable in
  time, correlated over 10–20 fibres; the cause is not understood, the
  working hypothesis being dome-versus-sky illumination differences
  [src: arXiv:2209.14482, Sect. IV.7.3]. For each sky line and sky fibre
  an amplitude, Δλ and ΔLSF are fitted; Δλ and ΔLSF maps from 2020 sky
  data are decomposed by PCA and four components per camera are stored;
  on each exposure the sky fibres set the coefficients, applied to all
  fibres (Eq. 15: sky = α_k R P S + Σ_l X_l^(λ) ∂_λ S̃ C_l^(λ) + Σ_p
  X_p^(LSF) ∂_LSF S̃ C_p^(LSF), the LSF derivative from an extra σ = 0.3 Å
  Gaussian) [src: same].
- **Variance after subtraction** (Eq. 16): σ²_corr = σ²_extract T⁻² +
  σ²_S̃ + (σ_T S̃)² + (ε_λ ∂_λ S̃)², with σ_S̃ the sky-model error for the
  mean resolution, σ_T the flat error, ε_λ set per sky line to give
  χ²/ndf = 1 within ±3 Å on sky fibres and applied to all fibres only in
  those windows; typical ε_λ = 0.025 Å [src: Sect. IV.7.4, Fig. 32]. The
  deconvolved sky has neighbour correlations of about −0.8; the
  reconvolved one only a few percent, which is why only the diagonal for
  the mean R is stored [src: same, Fig. 31].

### Step 7. Standard stars and flux calibration
<!-- key: step-7-standard-stars-and-flux-calibration -->

- **Selection.** About ten F stars per petal: 0 < g − r < 0.35,
  r − z < 0.2, 15 < g < 18 (bright) or 16 < g < 19 (faint), Gaia parallax
  < 1 mas to favour low-metallicity halo stars, proper motion
  > 2 mas yr⁻¹ to avoid peculiar cool-kinematics stars
  [src: arXiv:2209.14482, Sect. IV.8].
- **Model fit.** Grid of Allende Prieto et al. models (R = 10,000;
  T_eff in 500 K steps, [Fe/H] −5 to +1 in 0.5 dex, log g 1 to 5 in 1 dex)
  [src: Sect. IV.8.1]. Data and model are divided by a 160 Å sliding-median
  continuum (width chosen empirically) so that no prior calibration is
  needed; an extra variance term 0.12 is added; sky lines, tellurics and
  Ca H&K (interstellar) are masked [src: Sect. IV.8.2]. Radial velocity by
  cross-correlation with a 6000 K, log g = 4, [Fe/H] = −1.5 model over
  ±1500 km s⁻¹ in 15 km s⁻¹ steps; candidate models restricted to
  dust-corrected g − r within ±0.2; trilinear interpolation on the grid;
  the fit is redone after a first calibration [src: same]. Check: model
  versus catalogue g − r rms 0.023, about 100 K [src: same, Fig. 37].
- **Rejection.** 3σ outliers in the ratio of measured to model r-band
  flux over 6000–7300 Å, and stars whose model and catalogue g − r differ
  by more than 0.1 + 0.2 E(B − V), relaxed with extinction because of
  reddening-law uncertainty [src: Sect. IV.9.1].
- **Calibration vector.** Per camera, Eq. 17 fits a mean deconvolved
  calibration C_j with a scale α_k per star for positioning offsets and
  outlier rejection, then convolves it with each fibre's R
  [src: Sect. IV.9.2].
- **Aperture losses.** With a Moffat focal-plane PSF (β = 3.5), the
  fibre radius r_F (varying with plate scale), seeing s and positioning
  offset, the point-source acceptance F_PSF gives the applied "flat to
  PSF" factor ⟨F_PSF(s)⟩ / F_PSF(s, r_F) × r_F² / ⟨r_F²⟩ (Eq. 18); a
  "PSF to fiber" factor for a 1.5″ fibre in 1″ seeing with an exponential
  profile (Eq. 19) is stored as PSF_TO_FIBER_SPECFLUX, not applied
  [src: Sect. IV.9.3]. The default calibration is therefore a total flux
  for point sources and a lower limit for extended ones [src: Sect. IV.9].

### Step 8. Fibre cross-talk and co-addition
<!-- key: step-8-fibre-cross-talk-and-co-addition -->

**Cross-talk.** The omitted PSF tails are modelled as a kernel K(r) ∝ r² (1 + r²)^−(1+p/2),
p ≈ 2.5, normalised per camera against sky-fibre residuals over several
hundred exposures; contamination from first and second neighbours is
subtracted from the extracted spectra, without iteration because it is
small [src: arXiv:2209.14482, Sect. IV.10]. Adjacent-fibre cross-talk is
0.1–0.2% in blue and red, rising above 8900 Å in the NIR to 1.5% at
9800 Å [src: same, Fig. 42].

**Co-addition.** Inverse-variance weighted mean per wavelength bin (no resampling, since
all fibres share one grid), resolution R_coadd = Σ_i w_i R_i with the same
weights (Eq. 20), 4σ outlier rejection in the main survey; cameras are not
merged before the redshift fit, to avoid mixing resolutions
[src: arXiv:2209.14482, Sect. IV.11]. In DR1 the coadd R was mis-weighted
(L2 known issues) (arXiv:2503.14745) [src: App. E].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Row-by-row optimal extraction or 2D forward model
<!-- key: row-by-row-optimal-extraction-or-2d-forward -->

Row-wise optimal extraction is cheap and gives uncorrelated pixels, but
only for a separable PSF, and rebinning to combine exposures correlates
them (arXiv:0911.2689) [src: Sect. II]. The 2D model needs a calibrated 2D
PSF per fibre and wavelength (Step 2) and a large sparse solve, and its
output is not flux-conserving per bin (fit R·M, not M; L2), but keeps
native resolution and independent pixels and makes co-addition a weighted
mean (Step 8). DESI chose the 2D model; the comparison on one simulation
gives few-percent differences and a sharper LSF for the 2D extraction
[src: arXiv:0911.2689, Sect. III].

### PSF core only, or core plus tails
<!-- key: psf-core-only-or-core-plus-tails -->

Modelling tails inside the extraction would treat cross-talk exactly but
spreads cosmic rays; DESI models the core and corrects cross-talk after
extraction (Step 8) [src: arXiv:2209.14482, Sects. IV.3.1, IV.10]. The
price is a separate, camera-dependent calibration that reaches 1.5% in the
NIR.

### Where the sky-line residual correction comes from
<!-- key: where-the-sky-line-residual-correction-comes -->

| Variant | What it fits | Cost | Used by |
|---|---|---|---|
| Per-fibre achromatic scale from sky lines | one α_k per fibre and camera, ~1% | cannot follow wavelength or LSF errors | DESI EDR [src: arXiv:2209.14482, Sect. IV.7.2] |
| Throughput model versus positioner location | replaces α_k | needs the positioner history | DESI DR1 (arXiv:2503.14745) [src: Sect. III.1.3] |
| PCA of calibration offsets (Δλ, ΔLSF) from a sky library | four components per camera, coefficients from sky fibres per exposure | assumes a stable pattern; cause unknown | DESI [src: arXiv:2209.14482, Sect. IV.7.3] |
| Frame-by-frame PCA of continuum-subtracted residual spectra | 30 leading components from ~400 spectra, 20–25 of them sky fibres | rolling-median continuum removal can touch the source | AAOmega / GAMA (arXiv:1007.0648) [src: Sect. 2.3] |
| Nod-and-shuffle | sky through the object fibre | 2√2 loss in S/N for fixed time under the paper's baseline assumptions (half the time, half the fibres, twice the sky) | comparison baseline (arXiv:1007.0648) [src: App. B.2] |

The AAOmega study concludes that PCA with dedicated sky fibres matches
nod-and-shuffle quality for 10–100 h on source and is superior when
multiplex and efficiency matter [src: arXiv:1007.0648, Sect. 7]. It
differs from the SDSS implementation it derives from by computing the
eigenvectors per frame rather than from a large database [src: Sect. 2.3].

### Pixel variance from the data or from a model
<!-- key: pixel-variance-from-the-data-or-from-a-model -->

The data-based variance (Eq. 2) is simple and biases sky, calibration and
spectra through the value–variance correlation; the model-based variance
needs a first extraction and sky model but keeps the pipeline linear
[src: arXiv:2209.14482, Sect. IV.2.9].

### Calibration stars at the targets' focus or not; total or fibre flux
<!-- key: calibration-stars-at-the-targets-focus-or-not -->

BOSS drilled quasar holes for a design wavelength λ_eff = 4000 Å, to raise
Lyα-forest throughput, while its 20 standards per plate were at 5400 Å; the
pipeline interpolated standard-star calibrations to all fibres without
that difference (Margala et al. 2016, arXiv:1506.04790)
[src: Sects. II, III.3]. The fix scales each spectrum by the ratio of
fibre acceptances at the assumed and actual design wavelengths,
R_i*(λ) = A_i*(λ, λ_c, h_obs) / A_i*(λ, λ_i, h_obs) (Eq. 13), with A* the
acceptance under ideal guiding at hour angle h_obs [src: Sect. III.3]. The
model says BOSS quasar flux was on average 19% too high at 3600 Å and 24%
too low at 10,000 Å [src: Abstract]. Validation used 486 "offset
standards" placed like quasars and a pipeline run calibrated on them:
their g − r residual against imaging goes from −0.117 to +0.006 mag after
correction (0.010 with the offset-standard calibration) [src: Sect. IV,
Table 2]. DESI positions all fibres for the red and accepts a chromatic
focal-plane pattern instead (Step 7; What goes wrong).

Calibrating to point-source total flux is exact for stars and quasars and a
lower limit for galaxies; the stored PSF-to-fibre factor gives fibre
fluxes consistent with imaging for both, with 6% scatter at the bright end
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
| Cross-talk, adjacent fibres | 0.1–0.2% (b, r); up to 1.5% at 9800 Å (z) | DESI | arXiv:2209.14482 | Sect. IV.10 |
| BOSS quasar miscalibration | +19% at 3600 Å; −24% at 10,000 Å | BOSS DR12 | arXiv:1506.04790 | Abstract |
| BOSS offset-standard g−r residual | −0.117 → +0.006 mag (486 stars) | BOSS DR12 | arXiv:1506.04790 | Table 2 |
| AAOmega PCA | 30 components; 20–25 sky fibres of ~400 | GAMA | arXiv:1007.0648 | Sect. 2.3 |
| DESI DR1 noise power underestimate (Lyα forest, k > 3.1 Å⁻¹) | 2.8% (α = 6.9 × 10⁻⁴ Å) | DESI DR1 P1D | arXiv:2505.09493 | Sect. 4.2 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **A model that passes simulations fails on sky lines.** The DESI sky
  model "was successfully tested on simulations", yet real data left
  bright-line residuals that needed the empirical PCA of Step 6
  [src: arXiv:2209.14482, Sect. IV.7.3]. Test: rms of sky-fibre residuals
  against Eq. 16 with ε_λ = 0, flagging bins where the excess exceeds 1%
  and 3% of the sky; then with ε_λ fitted, the scatter must match the model
  at most wavelengths [src: Sect. IV.7.5, Figs. 33–34].
- **PSF or trace drift between afternoon calibration and night.**
  Shows up as continuum offsets between fibres and line residuals. Test:
  Eq. 4 across exposures, dome positions and positioner moves, against the
  1% requirement [src: Sect. IV.3.3]; per-exposure trace re-fit
  [src: Sect. IV.4.2].
- **Variance wrong in the released spectra.** DR1's flux-calibration
  variance bug (factor up to 5 at S/N ≈ 100 per pixel) is a known issue
  (arXiv:2503.14745) [src: App. E]. Independently, the DR1 Lyα P1D finds
  the noise power 2.8% below the measured small-scale power and adopts a
  cross-exposure estimator for z < 2.7 so as not to depend on the
  pipeline noise (arXiv:2505.09493) [src: Sects. 4.2, 7]. Test: compare
  raw and noise power where resolution suppresses all signal; pulls on
  repeated exposures.
- **Bad calibration data for one night.** A calibration problem on
  spectrograph 9 on one night gave wrong redshifts for 8500 spectra, fixed
  by a supplementary reprocessing with better calibration data
  (arXiv:2503.14745) [src: App. E].
- **Wavelength-calibration limits**: 2–3 km s⁻¹ radial-velocity scatter
  (up to 20) in DR1 backup-programme data [src: same].
- **Chromatic aperture losses.** Spectroscopic-to-imaging flux ratios of
  stars show focal-plane structure in blue and NIR from corrector
  chromatic distortion; not corrected in EDR [src: arXiv:2209.14482,
  Sect. IV.9.3, Fig. 39]. In BOSS the equivalent was the design-wavelength
  offset of quasars (arXiv:1506.04790) [src: Sect. III.3]. Test: offset
  standards or star flux ratios mapped over the focal plane.
- **Blue-end flux calibration.** DA white-dwarf residuals show a ~6% step
  below ~3700 Å (L2 row); the authors note part of the structure may come
  from the white-dwarf fitting pipeline and that E(B − V) is not yet
  included [src: arXiv:2209.14482, Sect. IV.9.4].
- **Residual cosmic rays** bias PSF fits and make false lines; caught by
  the bad2dfit flag and the 4σ coadd clipping [src: Sects. IV.5.3, IV.11].
- **Validation suite as the papers state it**: extraction pulls on CCD
  simulations, sky-fibre residuals against Eq. 16, stellar-fit colours,
  white-dwarf residuals and spectroscopic-versus-imaging fibre fluxes
  (DESI, Steps 4–7); synthetic AB magnitudes against imaging with
  normalised-MAD dispersions (BOSS, arXiv:1506.04790) [src: Table 2].

## Reading list
<!-- key: reading-list -->

- Foundation: Bolton & Schlegel 2010, arXiv:0911.2689 — why optimal
  extraction fails for non-separable PSFs; the resolution matrix.
- Method: Guy et al. 2023, arXiv:2209.14482, Sects. IV.2–IV.11 — every
  calibration product, its fit and its validation.
- Application: DESI Collaboration 2025, arXiv:2503.14745, Sect. III.1 and
  App. E — DR1 changes (positioner throughput model) and known issues.
- Method, sky: Sharp & Parkinson 2010, arXiv:1007.0648 — frame-by-frame
  PCA, failure modes of sky fibres (App. A), nod-and-shuffle cost.
- Critique: Margala et al. 2016, arXiv:1506.04790 — how a focal-plane
  design choice miscalibrated BOSS quasars, and the offset-standard test.
- Test from science: DESI DR1 Lyα P1D (FFT estimator), arXiv:2505.09493, Sect. 4.2 — pipeline noise checked
  on the Lyα forest.
- Alternatives (in L2): arXiv:astro-ph/0303507, arXiv:2312.06761,
  arXiv:1609.06142.

## Not verified
<!-- key: not-verified -->

- Wild & Hewett 2005 PCA sky subtraction for SDSS: cited by DESI and
  AAOmega, not read.
- BOSS idlspec2d extraction and sky model (row-wise optimal extraction,
  B-spline sky): no pipeline paper read.
- The DR1 positioner-location throughput model: documented only by a code
  pull request cited in arXiv:2503.14745; its performance was not read.
- 4MOST, PFS, WEAVE and SDSS-V reduction pipelines: no pipeline paper
  found in two searches.
- Horne 1986 (doi:10.1086/131801) body not read; its variance argument is
  quoted through arXiv:2209.14482, Sect. IV.2.9.
