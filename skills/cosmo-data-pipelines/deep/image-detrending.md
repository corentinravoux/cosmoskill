# Instrument signature removal, sensor effects and astrometry — cosmo-data-pipelines dossier

Scope: how imaging pipelines build and apply their calibration products
(overscan, bias, dark, linearity, crosstalk, flats, star or illumination
flats, defect masks), how the brighter-fatter correction is derived from
flat-field statistics and how well each variant works, how tree rings,
edge distortions, charge-transfer inefficiency and new sensor anomalies are
handled, and how the background is subtracted; compared across HSC, DES,
Rubin DP1 and Euclid VIS, with the reason given for each choice.
Snapshot: 2026-10-18.
From: Bosch et al. 2018, Sects. 3.1–3.2, 4.1–4.2; DES and Rubin
data-management groups (copied from `references/subtopics.tsv`).

Already in L2, not repeated here: the Rubin DP1 ISR order, the
brighter-fatter physics and the DECam pixel-shift correction in one
paragraph each, the DECam and Rubin astrometric models
(`physics-and-methods.md#image-detrending-and-astrometry`); astrometric and
depth figures (`results.md#imaging-pipeline-performance`); the sensor and
astrometric systematics (`systematics.md#sensor-effects-brighter-fatter-charge-transfer`,
`systematics.md#astrometric-residuals`). Photometric calibration
(ubercal, FGCM, Gaia standards) is in `cosmo-photometry-photoz`
(deep/photometric-calibration); PSF modelling in
`physics-and-methods.md#psf-modelling-in-imaging-pipelines`; the shear
consequences in `cosmo-weak-lensing`.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Calibration products and the order they are applied
<!-- key: step-1-calibration-products-and-the-order-they -->

All pipelines work backwards through the signal chain, from ADU to
photoelectrons (arXiv:2603.23786) [src: Sect. IV.2.1]. What differs is how
each product is built.

| Product | HSC (Bosch et al. 2018, arXiv:1705.06766) [src: Sect. 4.1] | DES (Morganson et al. 2018, arXiv:1801.03177) [src: Sects. III.1–III.3] | Euclid VIS Q1 (arXiv:2503.15303) [src: Sect. 3] |
|---|---|---|---|
| Overscan | 30th-order Akima spline along rows, one rejection iteration | row by row: mean of the middle 40 of 50 overscan columns after dropping min and max, no fit between rows | — |
| Bias | mean of ~10 overscan-corrected zero frames | 5σ-rejected mean of ~150 zero frames per epoch | bias and dark (Sect. 3.5, not read) |
| Linearity | cubic polynomial per amplifier from dome flats of varying exposure | CCD-dependent lookup table | LED pulses of random length: linear from 300 to ~1000 ADU, then 2–4% until saturation; nothing applied below 300 ADU |
| Crosstalk | one intra-CCD matrix for all CCDs from commissioning bright sources | linear coefficient per source–victim amplifier pair, ΔN_victim = −C_VS N_source (Eq. 1) | 1584 coefficients (12 victims × 11 sources × 12 readout blocks) by regression on bright source pixels |
| Dark | mean of 3–5 closed-shutter frames scaled by time since wipe | — | — |
| Flat | mean of ~10 dome flats, normalised to unity over the camera | 5σ-rejected mean of 50–100 dome flats of 8–20 s, per epoch | PRNU flats from LEDs at 573, 592, 638, 697 nm and 10, 25, 40 kADU; final small-scale flat = mean of the four 10 kADU flats |
| Large-scale response | joint calibration (Sect. 3.2) | star flat from 22 dithered 30 s exposures of star fields | illumination ("large-scale") flat from 15,000 stars of the self-calibration field |
| Fringes | scaled fringe frame for y and NB0921 | in the PCA sky templates (Step 5) | — |

**Stated reasons.**

- HSC uses dome flats "because they are easy to obtain, easy to repeat
  with the same conditions", and the lamp spectrum resembles that of the
  science sources better than the night sky [src: arXiv:1705.06766,
  Sect. 4.1]. Their weakness, scattered light and lamps that age
  differently, is passed to the joint calibration [src: same].
- DES moved from nightly calibrations to "supercals" combined over
  several nights after the first year, because "the camera response was
  more stable than the individual nightly calibration exposures"; products
  are remade per "processing epoch", declared each year and after each
  thermal cycle, since a warm-up changes the flat by ≪ 1% and the CCD
  positions by a few microns [src: arXiv:1801.03177, Sects. III, III.2].
  The row-by-row overscan is needed because CCDs sharing a backplane with
  the focus CCDs see a bias jump half-way through readout [src: Sect. III.1].
- Rubin DP1 had no flat-field screen installed and relied entirely on
  twilight flats, dithered in azimuth and rotator angle against star
  print-through, at 10,000–20,000 e⁻ (arXiv:2603.23786) [src: Sect. II.3];
  an amplifier-offset correction based on the Pan-STARRS pattern-continuity
  algorithm removes background steps at amplifier boundaries
  [src: Sect. IV.2.1].
- Euclid VIS needs linearity to "better than one part in 6 × 10⁻⁴" above
  about 10 k e⁻ for the PSF requirement; on-sky methods failed because of
  cosmic rays and jitter, so the ground LED technique, stable to < 10⁻⁴
  over an hour, is used [src: arXiv:2503.15303, Sect. 3.6]. Crosstalk below
  4 × 10⁻⁵ is not corrected, to avoid adding noise; a saturated source
  pixel invalidates its victims [src: Sect. 3.4].

**Order in DES.** Bias, nonlinearity, saturation mask, bad-pixel mask,
column fixes, gain, brighter-fatter, dome flat; then sky subtraction and
division by the star flat [src: arXiv:1801.03177, Sects. III.3, IV.3].
HSC applies brighter-fatter after crosstalk and before dark and flat
[src: arXiv:1705.06766, Sect. 4.1].

### Step 2. Defect masks: what is masked and what is repaired
<!-- key: step-2-defect-masks-what-is-masked-and-what-is -->

DES builds a bad-pixel mask per epoch from flats, biases and ~50 g-band
sky exposures: cold if below 50% of the camera mean in any flat input, hot
if above 150% in three or more, hot if > 500 e⁻ and warm if > 20 e⁻ in
any bias, an 11 × 3 box around hot pixels, the 15 edge rows and columns
(EDGE), 25 columns where the star flat is unreliable at 1–2% (NEAREDGE),
and six ~1.5 mm "tape bumps" per CCD whose electrostatic properties change
with each thermal cycle [src: arXiv:1801.03177, Sect. III.2]. About 3% of
pixels are near an edge, 0.2% otherwise unusable and ~1% TAPEBUMP or
SUSPECT; one amplifier with gain unstable at 10% is not used
[src: same]. Columns offset in level but with normal variance (within 25%
of neighbours) are repaired by subtracting the offset rather than masked
[src: Sect. III.3].

Rubin DP1 masks every new anomaly for which no correction exists: vampire
pixels (bright defects surrounded by depressed flux, charge-conserving but
with no unique way to redistribute it), phosphorescent photoresist residue
whose brightness depends on previous exposures, edge bleeds and "ITL dips"
below saturated stars (arXiv:2603.23786) [src: Sect. V.1].

### Step 3. Brighter-fatter: from flat-field statistics to a kernel
<!-- key: step-3-brighter-fatter-from-flat-field -->

**What is measured.** The area of pixel (0, 0) changes with the charge
Q_ij in pixel (i, j) as δA = A g Σ a_ij Q_ij (Astier & Regnault 2023,
arXiv:2301.03274, Eq. 1), with g the gain and a_ij the "area
coefficients", a_00 < 0 and the others positive, subject to the sum rule
Σ a_ij = 0 (Eq. 3) [src: Sect. 2.1]. Flat-field pair covariances then
follow C_ij(μ) = (μ/g)[δ_i0 δ_j0 + a_ij μ g + (2/3)(a ⊗ a)_ij (μg)² + …]
+ n_ij/g² (Eq. 4), μ the mean in ADU, n_ij the noise, ⊗ a discrete
convolution; the photon transfer curve is C_00 = n_00/g² + μ/g + a_00 μ²
+ O(μ³) (Eq. 5) [src: same]. A quadratic non-linearity μ_m = μ_t + k μ_t²
(Eq. 6) shifts the fitted a_00 to a_00 + 3k/g (Eq. 7) but leaves the other
a_ij unchanged at order μ², which is why linearity must be fixed first
[src: same]. The LSST camera study adds a b_ij term for time-dependent
processes (Broughton et al. 2023, arXiv:2312.03115, Eq. 2) and recalls that
the μ² term carries 20% of the variance loss [src: Sect. II.1].

**From a_ij to a correction.** The data constrain how much each pixel's
area changes, not its shape: turning the scalar a_ij into boundary shifts
is ill-posed [src: arXiv:2301.03274, Sect. 4.1]. The variants:

| Variant | How the boundary shifts are obtained | Where |
|---|---|---|
| Pixel-shift kernel with imposed ratios | ratios between directions estimated from the area changes | DES, CCD-dependent kernel of Gruen et al. 2015 (arXiv:1801.03177) [src: Sect. III.2] |
| Scalar curl-free kernel | the deflection is the gradient of a potential fitted to flat noise correlations; correction F̂ = F + ½∇·V with V = F∇(K ⊗ F) | HSC (arXiv:1705.06766) [src: Sect. 4.2]; Rubin; formula as quoted in arXiv:2312.03115 [src: Sect. V.3] |
| Poisson-equation kernel, iterated | 11 × 11 kernel solving Poisson's equation with the zero-sum-adjusted covariance as source; flux-conserving transfers iterated until successive changes < 10⁻⁶ | Euclid VIS (arXiv:2503.15303) [src: Sect. 3.9] |
| Electrostatic model | geometric parameters of a simple field model fitted to a_ij give the 2D boundary displacements, sum rule satisfied by construction | HSC reanalysis (arXiv:2301.03274) [src: Sect. 4.1] |
| Kernel chosen to linearise the PTC | scalar kernel picked to reconstruct the linear PTC, absorbing higher-order terms | LSST camera laboratory data (arXiv:2312.03115) [src: Sect. VI] |

The authors' reasons against the curl-free assumption: a solution of the
Poisson equation violates it, and the anisotropy between a_01 and a_10
questions it at short distance (arXiv:2301.03274) [src: Sect. 4.1]; the
LSST camera stars are corrected less well than flats, which the authors
attribute to an unmodelled curl component (arXiv:2312.03115)
[src: Abstract].

**How well it works.** The requirement used is a PSF size bias
δT/T ≤ 10⁻³ for LSST (T the trace of the second-moment matrix) and, for
Euclid, transferred ellipticity 5 × 10⁻⁵ rms and size 5 × 10⁻⁴ rms, as
quoted in arXiv:2301.03274 [src: Sect. 6.1]. Results on the same metric:

- HSC, electrostatic model: δT/T < 10⁻³ in all five bands at all image
  qualities; residual ellipticity mostly < 10⁻⁴; all residual trends
  indicate a slight over-correction; obtained blind [src: arXiv:2301.03274,
  Sect. 6.1].
- DECam, imposed ratios: over-corrects and leaves a negative slope about
  −1/3 of the uncorrected one, "certainly too large" for a large cosmic
  shear survey [sec: arXiv:2301.03274, Sect. 6.1, reading Gruen et al.
  2015 Fig. 12].
- HSC, curl-free kernel: corrected star sizes vary by about 0.2% over
  three magnitudes, adequate for HSC year 1 [sec: arXiv:2301.03274,
  Sect. 6.1, eyeball estimate from Mandelbaum et al. 2018]; Bosch et al.
  note an uncorrected magnitude-independent bias [src: arXiv:1705.06766,
  Sect. 4.2].
- LSST camera laboratory: the PTC-linearising kernel removes 95–97% of the
  effect in flats, but only up to the parallel deferred-charge turnoff at
  10⁵ e⁻; stars are corrected by 96–99% along serial and 85–90% along
  parallel; the effect is 16% anisotropic and 67% of the anisotropy
  survives correction [src: arXiv:2312.03115, Sect. VI].
- Euclid VIS: the flux-ratio deficit of bright stars (I_E < 19) in a small
  aperture disappears after correction [src: arXiv:2503.15303, Sect. 3.9].

### Step 4. Tree rings, edge distortions and charge-transfer inefficiency
<!-- key: step-4-tree-rings-edge-distortions-and-charge -->

**Transverse fields are not QE.** Doping gradients, guard rings and
lattice stress create fields parallel to the CCD surface that move charge;
in DECam flats they appear as tree rings (~1%) and edge distortions (~10%)
(Plazas et al. 2014, arXiv:1403.6127) [src: Abstract]. Because these are
pixel-size variations, "naively dividing by the flat-field images could
lead to systematic errors" [src: Sect. I]: the flux is right per unit area
but the astrometry is not. The remedy is templates from high-S/N dome
flats, binned in distance from each ring centre or from each edge,
high-pass filtered against slow QE changes, and fed to the astrometric and
photometric solutions [src: Sect. IV]. Ring profiles in different bands
differ by a scale factor, g > r > i > z > Y, as expected since blue photons
convert nearer the back surface where the drift is longest; edge profiles
have a more complex wavelength dependence [src: same, Fig. 6].

**Charge-transfer inefficiency.** In Euclid VIS, radiation-damage traps
delay electrons during readout; faint sources lose fractionally more. Q1
applies no correction; for an S/N = 200 star far from the register, the
parallel CTI at end of May 2024 gives ΔF/F ≈ −(3 ± 2) × 10⁻⁴ and a
spurious shift Δy ≈ (2 ± 1) × 10⁻³ pixel, growing roughly linearly with
time plus jumps at solar coronal mass ejections (arXiv:2503.15303)
[src: Sect. 3.8]. Traps are monitored by trap pumping, whose dipole
intensity I(t_ph) = N P [exp(−t_ph/τ) − exp(−2t_ph/τ)] (Eq. 1; N shuffles,
P capture efficiency, τ emission time, t_ph the phase time) gives τ and P
per trap, and by extended pixel edge response trails modelled with arCTIc
[src: same]. Correction is planned for a later release [src: same].
Rubin applies a serial CTI correction in ISR (arXiv:2603.23786)
[src: Sect. IV.2.1].

### Step 5. Cosmic rays and background
<!-- key: step-5-cosmic-rays-and-background -->

**Cosmic rays (HSC).** Inherited from SDSS: a pixel not adjacent to
saturation, n = 6 σ above the mean of each of the four neighbour pairs,
and sharper than the PSF allows for at least one pair,
z − c N(z) > PSF(d)(z̄ + c N(z̄)) (Eq. 2; z the pixel value, N(z) its
standard deviation, z̄ the mean of the pair at distance d), with c = 2.5
and a factor c₂ = 0.6 on PSF(d) to spare star cores
[src: arXiv:1705.06766, Sect. 4.4]. The DESI spectroscopic pipeline uses
the same SDSS algorithm with N = 6, c = 3, c₂ = 0.5
(`deep/extraction-sky.md`).

**Background.**

- HSC and Rubin: 3σ-clipped mean in 128 × 128 pixel bins with detected
  objects masked, then a sixth-order 2D Chebyshev fit, inverse-variance
  weighted [src: arXiv:1705.06766, Sect. 4.6; arXiv:2603.23786,
  Sect. IV.2.2]. Chebyshev fitting is preferred to 512-pixel bins with
  splines because it is less sensitive to where bin edges fall relative to
  bright objects [src: arXiv:1705.06766, Sect. 4.6]. Because detection
  needs a background and the background needs a mask, the background is
  re-estimated each time detection goes fainter (twice per CCD, once on
  the coadd, where only a constant is removed) [src: same]. A temporary
  64 × 64 spline background is subtracted just before peak finding and
  added back, to stop the wings of bright objects creating spurious peaks
  that steal flux in deblending [src: Sect. 4.7.2].
- HSC PDR3: a global sky (1k × 1k superpixels fitted by 2D polynomials,
  plus a scaled sky frame stacked from dithered visits, plus a 256 × 256
  pass with masks grown to 2.4 times the PSF around > 2.5σ footprints,
  iterated three times) and, before detection and measurement, a local sky
  with 128-pixel superpixels (≈ 21.5″), chosen as the trade-off between
  detection efficiency and over-subtraction of moderately extended sources;
  sources up to ~30″ are unaffected and two kinds of coadd are released
  (Aihara et al. 2022, arXiv:2108.13045) [src: Sects. 3.5–3.6].
- DES: four PCA templates from ~1000 exposures per epoch (a median image
  with the pupil scattered-light torus and fringes, two gradients, and a
  pupil/fringe mix that follows the airglow-to-moonlight ratio), fitted on
  128 × 128 superpixels over the whole exposure; then the weight image is
  rebuilt from the sky model, to avoid giving positive fluctuations more
  weight than negative ones [src: arXiv:1801.03177, Sects. III.2, IV.3].
  Fitting the whole exposure rather than each CCD (Y1) matters for objects
  larger than ~1′ [src: Sect. IV.3].
- Euclid VIS: NoiseChisel per quadrant with cosmic-ray pixels set to NaN
  (up to 15% of pixels flagged), falling back to a second run or to the
  SExtractor map when a quadrant has too little blank sky, at the cost of
  over-subtraction inside objects larger than a quadrant
  (arXiv:2503.15303) [src: Sect. 3.11].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Flat source and the large-scale correction
<!-- key: flat-source-and-the-large-scale-correction -->

| Choice | Buys | Costs | Who |
|---|---|---|---|
| Dome flat + joint calibration | repeatable, spectrum close to sources | scattered light, ageing lamps | HSC [src: arXiv:1705.06766, Sect. 4.1] |
| Dome flat + star flat | star flat fixes large-scale response and colour | star flat unreliable near edges | DES [src: arXiv:1801.03177, Sect. III.2] |
| Twilight flats, dithered | available before the screen | non-uniform illumination, print-through | Rubin DP1 [src: arXiv:2603.23786, Sect. II.3] |
| LED PRNU flats + stellar illumination flat | wavelength and fluence coverage; shutter gradient (~6% in short, 1% in nominal exposures) captured | objects in the 10 kADU flats; stars needed for the large scale | Euclid VIS [src: arXiv:2503.15303, Sects. 3.10, 4.4] |

The Euclid illumination flat uses stars with |SPREAD_MODEL| < 0.005,
ellipticity < 0.05, FLAGS = 0 and S/N > 80, on 3 × 3 tiles per quadrant,
separately for short and nominal exposures; uncorrected magnitudes err by
about 0.05 mag in nominal exposures [src: arXiv:2503.15303, Sect. 4.4].

### Correct or mask
<!-- key: correct-or-mask -->

DES repairs offset columns and masks the rest; Rubin DP1 masks all new
anomalies; Euclid masks victims of saturated crosstalk sources and leaves
CTI uncorrected while monitoring it [src: arXiv:1801.03177, Sect. III.3;
arXiv:2603.23786, Sect. V.1; arXiv:2503.15303, Sects. 3.4, 3.8]. Masking
costs area and creates small-scale selection; correcting risks a bias where
the model is wrong (BF near hot pixels is flagged SUSPECT in DES for that
reason) [src: arXiv:1801.03177, Sect. III.2].

### Brighter-fatter method
<!-- key: brighter-fatter-method -->

The scalar curl-free kernel is simple and in production (HSC, Rubin), but
its assumptions (linearity in flux, zero curl) fail at the level the LSST
camera data can see, and its result depends on the flux level at which the
kernel is derived (arXiv:2312.03115) [src: Sect. VI]. The electrostatic
model reaches the LSST size requirement on HSC data but required dropping
some covariances whose excess variance "remains elusive"
(arXiv:2301.03274) [src: Abstract]. Whatever the kernel, PSF stars must be
kept below the flux where correction fails (the parallel deferred-charge
turnoff at 10⁵ e⁻ in the LSST camera) [src: arXiv:2312.03115, Sects. V.3,
VI].

### Background scale
<!-- key: background-scale -->

A small scale removes wings and spurious peaks (better deblending and
detection) but biases bright and extended objects; a large scale keeps
low surface brightness but connects footprints, slows deblending and
lowers faint detection efficiency (arXiv:2108.13045) [src: Sect. 3.6;
arXiv:1705.06766, Sect. 4.7.2]. HSC PDR3 answers with two coadds; Euclid
favours preserving low surface brightness [src: arXiv:2503.15303,
Sect. 3.11].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Bias frames combined | ~10 (HSC); ~150, 5σ rejection (DES) | HSC, DES | arXiv:1705.06766; arXiv:1801.03177 | Sect. 4.1; Sect. III.2 |
| Dome flats combined | ~10 (HSC); 50–100 of 8–20 s (DES) | HSC, DES | same | same |
| Crosstalk coefficients | intra-CCD up to 10⁻³, inter-CCD < 2×10⁻⁴, set to 0 below 10⁻⁶ | DECam | arXiv:1801.03177 | Sect. III.1 |
| Crosstalk coefficients | up to 5×10⁻⁴; not applied below 4×10⁻⁵; edge effect ~5 ADU | Euclid VIS | arXiv:2503.15303 | Sect. 3.4 |
| Non-linearity | 2–4% near saturation; none applied < 300 ADU | Euclid VIS | arXiv:2503.15303 | Sect. 3.6 |
| PRNU amplitude | ~1% | Euclid VIS | arXiv:2503.15303 | Sect. 3.10 |
| Star flat | 22 × 30 s, dithers 10″ to 1° | DES | arXiv:1801.03177 | Sect. III.2 |
| Masked pixel fractions | ~3% edge; 0.2% other; ~1% tape bump or suspect | DES | arXiv:1801.03177 | Sect. III.2 |
| Twilight flat level | 10,000–20,000 e⁻ | Rubin DP1 | arXiv:2603.23786 | Sect. II.3 |
| BF requirement | δT/T ≤ 10⁻³ (LSST); 5×10⁻⁴ rms size, 5×10⁻⁵ rms ellipticity (Euclid) | quoted | arXiv:2301.03274 | Sect. 6.1 |
| BF residual | δT/T < 10⁻³ all bands; ellipticity mostly < 10⁻⁴ | HSC, electrostatic model | arXiv:2301.03274 | Sect. 6.1 |
| BF correction efficiency | flats 95–97% up to 10⁵ e⁻; stars 96–99% serial, 85–90% parallel | LSSTCam laboratory | arXiv:2312.03115 | Sect. VI |
| BF kernel | 11 × 11; iterate to 10⁻⁶ | Euclid VIS | arXiv:2503.15303 | Sect. 3.9 |
| Tree rings, edge distortions in flats | ~1%, ~10% | DECam | arXiv:1403.6127 | Abstract |
| CTI, S/N 200 star (May 2024) | ΔF/F ≈ −(3 ± 2)×10⁻⁴; Δy ≈ (2 ± 1)×10⁻³ px | Euclid VIS Q1, uncorrected | arXiv:2503.15303 | Sect. 3.8 |
| Cosmic-ray thresholds | n = 6, c = 2.5, c₂ = 0.6 | HSC | arXiv:1705.06766 | Sect. 4.4 |
| Background bins | 128 × 128, sixth-order Chebyshev; temporary 64 × 64 | HSC, Rubin | arXiv:1705.06766; arXiv:2603.23786 | Sects. 4.6, 4.7.2; Sect. IV.2.2 |
| Local sky scale | 128 px ≈ 21.5″ | HSC PDR3 | arXiv:2108.13045 | Sect. 3.6 |
| Sky PCA | 4 components from ~1000 exposures | DES Y3 | arXiv:1801.03177 | Sect. III.2 |
| Illumination flat | 15,000 stars, 3 × 3 tiles per quadrant; ~0.05 mag uncorrected | Euclid VIS | arXiv:2503.15303 | Sect. 4.4 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Background subtraction that passes image simulations ruins shapes.**
  The HSC PDR2 global sky subtraction reduced over-subtraction around
  bright galaxies but produced "a considerable population of faint objects
  with anomalously large size measurements", not seen in the image
  simulations used to calibrate shear; the PDR2 shapes were withheld and
  later releases returned to local sky subtraction for measurement
  (arXiv:2108.13045) [src: Sect. 2.3]. Test: object size distributions
  against the sky scheme, on data, not only on simulations.
- **Non-linearity left in the flats** biases a_00 and hence the BF kernel
  (Eq. 7) [src: arXiv:2301.03274, Sect. 2.1]. Test: PTC and covariance
  fits after linearity correction; lamp-drift separation with
  non-monotonic exposure sequences [src: same, Fig. 1].
- **Over-correction of BF**, and colour–flux correlations of stars ignored
  in the assessment, which would make the apparent residual worse
  [src: arXiv:2301.03274, Sect. 6.1]. Test: star size and ellipticity
  slope against peak flux, per band and seeing bin, with colour controlled.
- **PSF stars above the correctable flux.** Correction fails above the
  parallel deferred-charge turnoff [src: arXiv:2312.03115, Sect. VI].
  Test: size versus flux up to saturation; cap the PSF-star magnitude.
- **Flat-fielding pixel-size variations** puts tree-ring and edge
  patterns into photometry and astrometry [src: arXiv:1403.6127,
  Sects. I, IV]. Test: astrometric and photometric residuals binned by
  distance from ring centres and edges.
- **Crosstalk models from the laboratory** leave over-subtracted ghosts
  next to bright stars in Rubin DP1 [src: arXiv:2603.23786, Sect. V.1.3];
  Euclid finds a non-linear edge term of ~5 ADU beyond the linear model
  [src: arXiv:2503.15303, Sect. 3.4]. Test: stack victim amplifiers at
  the positions of bright sources.
- **Unstable hardware between calibrations**: thermal cycles change
  flats, CCD positions and tape-bump behaviour [src: arXiv:1801.03177,
  Sects. III, III.2]; uncorrected CTI grows with time and jumps after
  solar events [src: arXiv:2503.15303, Sect. 3.8]. Test: recompute
  products per epoch; monitor traps.
- **Wings and spurious peaks** steal flux from neighbours in deblending
  when the background is too smooth [src: arXiv:1705.06766, Sect. 4.7.2];
  see `deep/source-injection.md` for injection tests of the full chain.

## Reading list
<!-- key: reading-list -->

- Method, overview: Bosch et al. 2018, arXiv:1705.06766, Sects. 4.1–4.2,
  4.4, 4.6, 4.7.2 — ISR choices, curl-free BF, cosmic rays, background.
- Method, overview: Morganson et al. 2018, arXiv:1801.03177, Sects. III,
  IV.3 — epochs, supercals, mask rules, star flats, PCA sky.
- Application: Rubin DP1, arXiv:2603.23786, Sects. II.3, IV.2, V.1 —
  twilight flats, ISR order, new anomalies and how they are masked.
- Application, space: Euclid Collaboration 2025, arXiv:2503.15303,
  Sects. 3–4 — LED linearity and PRNU, crosstalk thresholds, BF kernel,
  CTI monitoring, illumination flat.
- Foundation, BF: Antilogus et al. 2014, arXiv:1402.0725 (in L2).
- Method, BF: Astier & Regnault 2023, arXiv:2301.03274 — area
  coefficients, PTC, non-linearity bias, electrostatic model, requirement
  test.
- Critique, BF: Broughton et al. 2023, arXiv:2312.03115 — higher-order
  terms, curl, flux ceiling.
- Sensor effects: Plazas et al. 2014, arXiv:1403.6127 — tree rings and
  edge distortions as pixel-size variations; templates.
- Background: Aihara et al. 2022, arXiv:2108.13045, Sects. 2.3, 3.5–3.6 —
  global versus local sky and the PDR2 shape failure.

## Not verified
<!-- key: not-verified -->

- Coulton et al. 2018 (arXiv:1711.06273), the curl-free BF method paper:
  found by search, not read; its method is described here through
  arXiv:1705.06766 and arXiv:2312.03115.
- Gruen et al. 2015 residual slope and Mandelbaum et al. 2018 HSC numbers
  are quoted from arXiv:2301.03274, not read at source.
- Rubin ISR technical papers cited in DP1 (Fagrelius & Rykoff; Plazas
  Malagón et al.) not read; LSSTCam on-sky ISR performance not read.
- Euclid VIS bias and dark construction (Sect. 3.5) not read.
- Differential chromatic refraction and astrometry beyond L2 not read.
