# Shear calibration — cosmo-weak-lensing dossier

Scope: how a multiplicative shear bias m and its prior are produced, step by
step, for the three families in use (self-calibration by metacalibration or
metadetection, calibration of a fixed estimator on image simulations, and
analytic responses), and how to choose between them and between simulation
designs.
Snapshot: 2026-10-17.
From: Pantos 2026 review (arXiv:2602.12238), Sects. 4.1.1 and 7.2; DES Y6
shape catalogue (arXiv:2501.05665); KiDS-Legacy SKiLLS calibration
(arXiv:2210.07163); UNIONS-3500 I (arXiv:2605.13549).

Already in L2, not repeated here: the m values per tomographic bin of
KiDS-1000, DES Y3, HSC Y3, KiDS-Legacy and DES Y6, how each enters the fit,
and what fixing or widening them costs in S8
(`systematics.md#shear-measurement-bias-noise-model-selection`); the blending
sizes per analysis (`systematics.md#blending`); the Stage-IV allocations and
noise-bias scaling (`physics-and-methods.md#shape-measurement`); the estimator
with m or ⟨R⟩ in the denominator (`physics-and-methods.md#estimators`).
PSF modelling and leakage are a separate subtopic, mapped by the Liaudat
2023 review (arXiv:2306.07996, Sects. 7 and 9) and treated in
`systematics.md#psf-modelling-and-leakage`.

Symbols used throughout. e (or ε): measured ellipticity, a spin-2 quantity
with components e₁, e₂. γ: shear; g = γ/(1 − κ): reduced shear. m, c:
multiplicative and additive bias in e_obs = (1 + m)(e_int + γ) + c (DES Y6
writes this as Eq. 1 of arXiv:2602.10065). R: the 2 × 2 response matrix
∂e/∂γ at γ = 0. Δγ: the artificial shear applied in metacalibration. S/N or
ν_SN: signal-to-noise ratio of a detection; R₂ (HSC) or 𝓡 (KiDS): the
resolution factor, a measure of galaxy size relative to the PSF.

## How it is done
<!-- key: how-it-is-done -->

### Route A. Metacalibration: response measured on the data
<!-- key: route-a-metacalibration-response-measured-on -->

1. **Shear the image artificially.** Deconvolve the PSF, apply a small shear,
   reconvolve with a slightly larger PSF (arXiv:2501.05665, Sect. 4.1) [src].
   DES makes five images, unsheared and ±γ₁, ±γ₂ with amplitude 0.01 [src:
   Sect. 4.1]; KiDS-1000 reanalysis also uses 0.01, so that Δγ = 0.02 in the
   finite difference [src: arXiv:2510.01122, Sect. 3.1].
2. **Correct the sheared correlated noise ("fixnoise").** Pass a noise image
   through the same operations with the opposite shear and add it
   (arXiv:1702.02601, Eq. 25) [src: Sect. IV.1]. DES states that without it
   the method produces "catastrophic biases at the order of ∼10%"
   [src: arXiv:2501.05665, Sect. 4.1]. Cost: S/N of each measurement drops by
   √2, and in the original tests the uncertainty of the recovered shear rose
   by about 20% at S/N > 10; lowering the S/N cut to win back objects raised
   the variance [src: arXiv:1702.02601, Sect. VIII.2.4]. UNIONS quotes "an
   approximate 20% loss in SNR" for the same step (arXiv:2605.13549,
   Sect. 3.3) [src]; the two numbers describe different quantities (per-object
   S/N in the original paper, an overall SNR in UNIONS).
3. **Form the shear response.** Mean shear response by finite difference,
   ⟨R_γ⟩ = (⟨e_i⁺⟩ − ⟨e_i⁻⟩)/Δγ_j (arXiv:1702.02601, Eq. 10) [src].
4. **Form the selection response.** Any cut (S/N, size, weights, tomographic
   bin) is a selection S(e); its response is the mean unsheared ellipticity
   with the selection made on quantities measured on the sheared images,
   ⟨R_S⟩ = (⟨e_i⟩^{S+} − ⟨e_i⟩^{S−})/Δγ_j, and the total is ⟨R⟩ = ⟨R_γ⟩ +
   ⟨R_S⟩ (arXiv:1702.02601, Eqs. 13–14) [src]. In UNIONS-3500, R_sel,1 =
   0.016 and R_sel,2 = 0.015; an S/N cut gives a positive selection response
   and a size cut a negative one, as UNIONS recalls from DES Y1 [src:
   arXiv:2605.13549, Sect. 3.3].
5. **Calibrate two-point functions with the product of mean responses.** If
   galaxy shapes are uncorrelated in the absence of lensing, ⟨R^2pt⟩ =
   ⟨R_α⟩⟨R_β⟩, and for an auto-correlation ⟨R⟩² (arXiv:1702.02601, Eqs.
   21–22) [src]. The authors warn that this fails if neighbouring objects
   have correlated shapes without lensing (intrinsic alignments) or if image
   processing biases depend on local density [src: Sect. III.2]. DES Y6
   states that a mean scalar response per tomographic bin is sufficient at
   DES precision [src: arXiv:2501.05665, Sect. 4.1].
6. **Calibrate the residual on image simulations.** Metacalibration alone does
   not see detection: run on existing detections, it leaves a percent-level
   bias from shear-dependent detection in blends [src: arXiv:2501.05665,
   Sect. 4.1]. Every metacalibration analysis therefore adds a residual m
   from simulations (UNIONS: Sect. 3.4 of arXiv:2605.13549; KiDS-1000
   reanalysis: Sect. 4 of arXiv:2510.01122) [src].

Rules from the method paper [src: arXiv:1702.02601, Sect. III.3]: never cut
directly on ellipticity (a step function in e has an infinite derivative);
place cuts well above the detection threshold so that objects can move in
and out of the sample under shear; a cut that selects redshift changes the
true shear and must be handled separately.

### Route B. Metadetection: detection inside the loop
<!-- key: route-b-metadetection-detection-inside-the-loop -->

1. **Build coadds with a continuous PSF.** DES Y6 coadds into cells of 200 ×
   200 pixels [src: arXiv:2602.10065, Sect. II.1]. The Rubin implementation
   plans 250 × 250 pixel cells overlapping by 50 pixels, rejecting any input
   image with an edge inside a cell; smaller cells reject fewer images but
   complicate deblending [src: arXiv:2303.03947, Sect. 2.10].
2. **Shear the whole cell, not each object.** Five sheared cell images; then
   detection (sep with the main-survey settings in DES) on each [src:
   arXiv:2501.05665, Sect. 4.1].
3. **Measure, select, and average per catalogue.** ⟨R_ij⟩ = (⟨e_i⁺⟩ −
   ⟨e_i⁻⟩)/Δγ_j over the separately selected catalogues (Eq. 6 of
   arXiv:2501.05665) [src]. The five catalogues cannot be matched, because
   the number of detections differs; no per-object response exists; the
   response already contains the shear and selection parts; tomographic
   binning is a selection and gives one response per bin [src: Sect. 4.1].
4. **Residual m from image simulations, including blends at different
   redshifts** (step 4 of route C below).

Consequences for the rest of the pipeline, as the method paper states
[src: arXiv:1911.02505, Sect. 7]: every selection, including the
assignment to redshift bins, must be repeated on each sheared catalogue;
the natural object weight for non-shear averages such as n(z) is the
response, which metadetection cannot give per object; the paper suggests
mean responses in fine redshift bins, interpolated, as a substitute.

### Route C. Calibration of a fixed estimator on image simulations
<!-- key: route-c-calibration-of-a-fixed-estimator-on -->

Used with lensfit (KiDS), re-Gaussianization (HSC), and as the residual step
of routes A and B. The steps as the KiDS-Legacy (SKiLLS) and HSC Y3 papers
carry them out:

1. **Input galaxies.** SKiLLS: SURFS-Shark semi-analytic galaxies with
   nine-band synthetic photometry to r = 27, Sérsic morphologies learned from
   HST-ACS fits, positions from the SURFS N-body run [src: arXiv:2210.07163,
   Table 1]. HSC Y3: postage stamps cut from COSMOS HST images, which forces
   one constant shear per stamp [src: arXiv:2107.00136, Sect. 3.8]. DES Y6:
   fitvd model fits to the data, with clustering from the Cardinal
   simulation and a corrected bright end; stars from TRILEGAL and Gaia EDR3,
   because the pipeline uses Gaia positions [src: arXiv:2501.05665,
   Sect. 7].
2. **Observing conditions.** SKiLLS: 108 PSF sets with spatial variation
   within each exposure, 108 noise levels, the real CCD gaps; COllege, its
   predecessor, had 13 constant Moffat PSF sets and one noise level [src:
   arXiv:2210.07163, Table 1]. DES Y6: about 1000 random tiles simulated with
   the observed masks, backgrounds, WCS and PSF solutions, run through the
   identical coadd and metadetection pipeline [src: arXiv:2501.05665,
   Sect. 7].
3. **Constant-shear runs with noise cancellation.** SKiLLS: four constant
   shears (±0.0283, ±0.0283), each tile paired with a copy rotated by 90°,
   864 deg² in total, equivalent to about 5170 deg² after shape-noise
   cancellation, about four times the KiDS-Legacy area [src:
   arXiv:2210.07163, Sect. 5.1]. DES Y6: pairs with g₁ = ±0.02 and the
   estimators m̂ = (⟨ĝ⁺⟩ − ⟨ĝ⁻⟩)/(2|g|) − 1 and ĉ = (⟨ĝ⁺⟩ + ⟨ĝ⁻⟩)/2
   (arXiv:2501.05665, Eqs. 17–18, after Pujol et al. 2019), with jackknife
   errors over tiles [src: Sect. 7]. HSC Y3: γ₁ = ±0.02 with identical noise
   in both images [src: arXiv:2107.00136, Sect. 3.8].
4. **Variable-shear runs for blends at different redshifts.** A constant
   shear cannot capture the response of one object to the shear of a
   neighbour at another redshift ("shear interplay"); SKiLLS adds 32
   variable shear fields (cosmic shear learned from MICE-GC plus NFW
   tangential shear), applied to a blending-only catalogue of r < 25
   galaxies with a neighbour closer than 4″, 7776 deg², and corrects m by
   Δm = m^varShear − m^constShear measured in true-redshift bins [src:
   arXiv:2210.07163, Sect. 5.2]. HSC Y3 shears one redshift bin at a time
   and leaves the others unsheared; the excess m grows with seeing and
   "marginally meets" the Y3 requirement at the mean HSC seeing; it is not
   in the fiducial calibration and is marginalised over in the cosmology
   [src: arXiv:2107.00136, Sect. 3.8]. DES Y6 derives m, an effective n(z)
   and the redshift-mode parameters jointly, so that their covariance is
   kept [src: arXiv:2602.10065, Sect. II.3].
5. **Transfer to the data.** KiDS reweights: per tomographic bin, the
   simulated galaxies are split into 20 × 20 cells of ν_SN and 𝓡 of equal
   lensfit weight, m is measured per cell, and each data galaxy takes the m
   of its cell; the bin value is the weighted mean [src: arXiv:2210.07163,
   Sect. 5.1]. HSC fits m(SNR, R₂) + const ∝ (R₂/0.5)^1.66 (SNR/20)^−1.24
   and interpolates residuals (arXiv:2107.00136, Eq. 13) [src: Sect. 3.5.1].
6. **Additive leakage.** KiDS fits the PSF-leakage fraction α on the same
   grid with α_p = a₀ + a₁ν⁻² + a₂ν⁻³ + b₁𝓡 + c₁𝓡ν⁻² and corrects each galaxy,
   then removes the residual directly (arXiv:2210.07163, Eqs. 9–10) [src:
   Sect. 4.2.2]; the reason given is a negative tail of α at low ν_SN,
   traced to selection effects, which forbids a direct correction alone
   [src].
7. **Ensemble validation.** HSC splits the calibrated simulations by
   properties used in the model (SNR, R₂, photo-z) and by properties not
   used (magnitude, seeing, other photo-z codes): residuals stay below 0.5%
   except for the best- and worst-seeing bins [src: arXiv:2107.00136,
   Sect. 3.6].

### Route D. Analytic responses
<!-- key: route-d-analytic-responses -->

The analytic method derives the linear shear responses of smoothed pixel values and of
galaxy magnitude, size and shape from those of the basis functions, and
corrects detection and selection analytically, with noise bias to second
order; at HSC conditions it reports m = −0.12 ± 0.10% for isolated galaxies
and about −0.3 ± 0.1% for blends, after correcting a detection/selection bias
of about −4%, at about 1000 galaxies per CPU second (Li & Mandelbaum 2022,
arXiv:2208.10522) [src]. It is not yet the shear method of a published
cosmic-shear cosmology among the analyses this skill tracks.

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

| Choice | What it assumes | What it buys | What it costs | Who uses it |
|---|---|---|---|---|
| Metacalibration on existing detections | detection independent of shear | response on the data, little dependence on simulated morphology | misses detection bias in blends (percent level); fixnoise costs S/N; residual m still from simulations | DES Y3, DECADE, UNIONS (L2) |
| Metadetection on cell coadds | the space between objects is sheared coherently | detection bias removed to a few tenths of a per cent (L2) | no per-object response; every selection repeated on five catalogues; continuous-PSF coadds required | DES Y6; planned for Rubin |
| Fixed estimator + image simulations | simulations match data in the reweighting variables | estimator choice free; one pipeline for shear and n(z) | m depends on the realism of input morphology and faint galaxies | KiDS (lensfit), HSC (reGauss) |
| Analytic response | linear response of the basis functions | speed; no external simulation for first-order bias | blends still at −0.3% | tested on HSC-like simulations |

The reasons the papers give for their choice:

- **DES moved from metacalibration to metadetection** because "object
  detection is shear-dependent especially in the presence of blending",
  which produces a percent-level multiplicative bias in metacalibration
  [src: arXiv:2501.05665, Sect. 4.1].
- **KiDS kept lensfit for KiDS-Legacy** and judged it "robust within the
  requirements of lensing analyses with KiDS", while recommending, for
  tighter requirements, a method "less sensitive to the galaxy properties"
  [src: arXiv:2210.07163, Abstract]; the sensitivity test that motivates
  this is a shift of all input Sérsic indices, sizes or axis ratios by 1–3
  times their median fit uncertainty (5%, 5%, 10%) [src: Sect. 6.2].
- **KiDS-1000 reanalysis chose weighted moments (HSM) inside
  metacalibration**, because "more important is that the results are robust
  against limitation of the image simulations" than an intrinsically small
  bias [src: arXiv:2510.01122, Sect. 3.1]; it chose stacked postage stamps
  (five image manipulations instead of 25) and a fixed weight function,
  which minimises the selection response [src: Sect. 3.1]; and it set
  fix_noise = False because fixnoise "leads to noisier measurements",
  leaving the resulting bias to the SKiLLS calibration [src: Sect. 3.1].
- **UNIONS kept its SExtractor FLAGS = 0 cut** although it creates an
  uncalibrated selection bias, because the DES-like FLAGS ≤ 2 cut produced
  B modes on all scales of unknown origin [src: arXiv:2605.13549,
  Sect. 3.4.2].

Comparisons on the same data or the same simulations:

- **Metacalibration against lensfit on KiDS-1000 and SKiLLS.** Fixed-shear
  m is comparable in the first three bins and considerably smaller for
  metacalibration in the three highest [src: arXiv:2510.01122, Sect. 4.1];
  under extreme morphology shifts both stay "well within requirements", with
  metacalibration more robust to the axis-ratio shift at high redshift [src:
  Sect. 4.4]. Metacalibration m tracks the bias of a perfect estimator after
  selection (computed from the input sheared ellipticities with the same
  weights) [src: Sect. 4.1]. The cosmology is in L2.
- **Metadetection in DES Y6 simulations, by configuration** (paired
  jackknife on the same seeds) [src: arXiv:2501.05665, Sect. 7, Table 7]:
  evaluating the PSF at the median galaxy colour changes m by
  (0.035 ± 2.017) × 10⁻³ in blended scenes; removing stars by
  (0.063 ± 3.675) × 10⁻³; isolated grid galaxies show sub-percent bias.
- **Coherent-shear assumption of metadetection.** Shearing each object
  without shearing the space between objects, an upper bound on
  incoherence, leaves biases of order −0.3%, larger for a DES-like than an
  LSST-like setup; a trend with density in the DES-like case was "not fully
  understood" [src: arXiv:1911.02505, Sect. 5.3].
- **PSF variation in metadetection.** A single, strongly variable PSF gives
  m = −0.0065 ± 0.00044 when one PSF is used per coadd; coadding 30 epochs
  reduces it to −0.00035 ± 0.00037 [src: arXiv:1911.02505, Sect. 6].

Simulation design choices:

- **Shear amplitude.** Larger input shears shrink the error on m for a given
  volume but excite non-linear response; KiDS uses |γ| = 0.04 and verifies
  linearity, claiming more than an order of magnitude saved in volume [src:
  arXiv:2510.01122, Sect. 4.1].
- **Noise cancellation.** 90° rotated pairs are standard. On Euclid-like
  simulations measured with KSB, the response method reduces runtime for m
  by a factor 145 on a grid and 70 for randomly placed galaxies at small
  shears; pixel-noise cancellation on top of shape-noise cancellation gives
  a factor 7; rotating whole scenes rather than single galaxies helps when
  blends are present (Jansen et al. 2024, arXiv:2401.08239) [src]. SKiLLS
  stays with one 90° copy because selection effects erode the gain of more
  rotations [src: arXiv:2210.07163, Table 1 note].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Metacalibration artificial shear | 0.01 per component, five images | DES Y6, KiDS-1000 reanalysis | arXiv:2501.05665; arXiv:2510.01122 | Sect. 4.1; Sect. 3.1 |
| Bias without fixnoise | ∼10% | metacalibration | arXiv:2501.05665 | Sect. 4.1 |
| Cost of fixnoise | S/N ÷ √2; shear error +∼20% | metacalibration tests | arXiv:1702.02601 | Sect. VIII.2.4 |
| Selection response | 0.016, 0.015 | UNIONS-3500 | arXiv:2605.13549 | Sect. 3.3 |
| m from fiducial Y6 simulations | (+3.4 ± 6.1) × 10⁻³, 3σ error, 981 tiles | DES Y6 catalogue | arXiv:2501.05665 | Sect. 7, Table 7 |
| m per bin with blending | four values, see L2 | DES Y6 cosmic shear | arXiv:2602.10065 | Sect. II.3 |
| Incoherent-shear bound | ∼ −0.3% | metadetection | arXiv:1911.02505 | Sect. 5.3 |
| Simulation volume | 864 deg² (≈ 5170 deg² effective) + 7776 deg² variable shear | SKiLLS | arXiv:2210.07163 | Sects. 5.1, 5.2 |
| lensfit weight constants | σ_ε,pop = 0.253, ε_max = 0.804 | SKiLLS / KiDS | arXiv:2210.07163 | Sect. 4.1, Eq. 5 |
| HSC m model | ∝ (R₂/0.5)^1.66 (SNR/20)^−1.24 | HSC Y3 | arXiv:2107.00136 | Eq. 13 |
| HSC Y3 requirement | \|δm\| ≲ 0.25/SNR = 9.3 × 10⁻³, SNR = 27 | HSC Y3 | arXiv:2107.00136 | Eq. 24 |
| LSST requirement | \|m_tomo\| < 0.003 per bin; 0.002 adopted, "somewhat arbitrary" | Rubin metadetection | arXiv:2303.03947 | Sect. 6.1 |
| Euclid total budget on m | 2 × 10⁻³ | Euclid | arXiv:1902.00044 | Abstract |
| Undetected faint galaxies | few × 10⁻³ unclustered; ∼10⁻² clustered | Euclid VIS simulations | arXiv:1902.00044 | Abstract |
| Morphology update | percent-level change in m, five times the Euclid budget | Euclid | arXiv:2604.26684 | Abstract |
| UNIONS total m | −0.0572 ± 0.0047, tripled to ± 0.0141 | UNIONS-3500 | arXiv:2605.13549 | Sect. 3.4.2 |
| Analytic-response residual | −0.12 ± 0.10% isolated; −0.3 ± 0.1% blended | HSC-like simulations | arXiv:2208.10522 | Abstract |

Two numbers that look different from L2 but are not in conflict. The DES Y6
catalogue value (+3.4 ± 6.1) × 10⁻³ is one overall m with a 3σ error,
before blending at different redshifts; the four per-bin values with 1σ
errors in L2 come from the later joint shear–redshift simulation
calibration (arXiv:2602.10065, Sect. II.3) [src]. For the KiDS-1000
metacalibration, L2 quotes |m| < 0.017 from the abstract; Sect. 4.1 gives
the fixed-shear value of bin 2 as m = −0.0227 ± 0.0023, before the
variable-shear and selection corrections that produce the final values of
its Table 2, which were not read here [src: arXiv:2510.01122, Sect. 4.1].

How the HSC requirement is derived (arXiv:2107.00136, Sect. 4.1–4.2) [src]:
a systematic residual is allowed at 0.5σ of the integrated signal,
δξ± < ξ±/(2 SNR) (Eq. 20); δm changes ξ+ by 2δm ξ+ (Eq. 23); hence
|δm| ≲ 0.25/SNR (Eq. 24). SNR = 27 is the Y1 tomographic SNR averaged over
the Fourier and real-space analyses and rescaled by the Y3/Y1 galaxy number
[src: Sect. 4.1]. The same paper notes an error in the Y1 PSF-size
requirement (its Eq. 19 should read 0.25 σ_ξ+) [src: Sect. 4.1, footnote].

## What goes wrong
<!-- key: what-goes-wrong -->

- **Selection the response cannot see.** A flag that is constant across the
  sheared branches is not calibrated by metacalibration; in UNIONS, more
  elliptical objects trigger SExtractor deblending flags more often, giving
  Δm ≈ −0.02 found only in image simulations [src: arXiv:2605.13549,
  Sect. 3.4.2]. Test: run the full data selection on ± sheared simulations.
- **Software defects.** UNIONS found WCS offsets not propagated between
  epochs, visible as non-zero mean shear responses of stars, worth Δm ≈
  −0.02; with a further Δm_blend ≈ −0.017 the total was m = −0.0572 and the
  error was tripled [src: arXiv:2605.13549, Sect. 3.4.2]. Test: stars must
  deconvolve to points and have zero response.
- **Cuts near the detection limit or on ellipticity.** Biased selection
  response [src: arXiv:1702.02601, Sect. III.3]. Test: vary the cut, check
  R_S.
- **Blends at different redshifts.** Not captured by constant-shear
  simulations; HSC with COSMOS stamps cannot include it in the fiducial
  calibration [src: arXiv:2107.00136, Sect. 3.8]. Test: variable-shear or
  bin-by-bin shear simulations (SKiLLS Sect. 5.2; HSC Sect. 3.8).
- **Unrealistic simulation inputs.** Faint undetected galaxies must be
  simulated with their clustering down to magnitude 28 for Euclid
  [src: arXiv:1902.00044, Abstract]; morphology learned from Euclid data
  moves m at the per cent level relative to the Flagship input
  [src: arXiv:2604.26684, Abstract]. Test: shift input sizes, axis ratios,
  Sérsic indices (arXiv:2210.07163, Sect. 6.2; arXiv:2510.01122, Sect. 4.4).
- **Spatially selected subsamples.** HSC residuals exceed the requirement in
  the best- and worst-seeing bins, so an analysis with strict area cuts must
  re-evaluate the seeing distribution after the cuts [src:
  arXiv:2107.00136, Sect. 3.6].
- **Star contamination.** The largest metacalibration m in the KiDS-1000
  reanalysis (bin 2) comes mainly from stars [src: arXiv:2510.01122,
  Sect. 4.1]; high stellar density gives the only hint of sensitivity [src:
  Sect. 4.4].
- **Per-object responses in two-point functions.** ⟨R⟩² assumes shapes
  uncorrelated without lensing [src: arXiv:1702.02601, Sect. III.2]. Test:
  compare with responses computed per pair class or density bin.

Validation suites as stated: DES Y6 checks mean shear against PSF
properties, focal-plane, cell and tile coordinates, tangential shear around
stars and field centres, B modes, and survey-property maps, before the image
simulations [src: arXiv:2501.05665, outline of Sects. 5–7]. HSC Y3 accepts
calibration residuals below 0.5% in m and in fractional additive bias when
binned by modelled and marginalised properties [src: arXiv:2107.00136,
Sect. 3.6].

## Reading list
<!-- key: reading-list -->

- Foundation: Huff & Mandelbaum 2017, arXiv:1702.02600 — the metacalibration
  idea.
- Method: Sheldon & Huff 2017, arXiv:1702.02601 — selection response,
  two-point response, fixnoise, rules for cuts.
- Method: Sheldon et al. 2019, arXiv:1911.02505 — metadetection, coherent
  shear assumption, PSF variation, pipeline consequences.
- Application: Yamamoto et al. 2025, arXiv:2501.05665 — first metadetection
  catalogue, cell coadds, simulation configurations.
- Application: Li et al. 2022, arXiv:2210.07163 — SKiLLS: lensfit
  calibration, reweighting, variable-shear blends.
- Application: Li et al. 2021, arXiv:2107.00136 — HSC Y3 calibration and the
  requirement derivation.
- Application: Hervas-Peters et al. 2026, arXiv:2605.13549 — metacalibration
  plus simulations in UNIONS, and what simulations caught.
- Test: Yoon et al. 2025, arXiv:2510.01122 — metacalibration against lensfit
  on the same data and simulations.
- Critique: Euclid Collaboration 2019, arXiv:1902.00044 — undetected
  galaxies bias simulation calibration.
- Critique: Euclid Collaboration 2026, arXiv:2604.26684 — morphology
  realism moves m beyond the Euclid budget.
- Method: Li & Mandelbaum 2022, arXiv:2208.10522 — analytic responses.
- Method: Jansen et al. 2024, arXiv:2401.08239 — cheaper calibration
  simulations.

## Not verified
<!-- key: not-verified -->

- The DES Y6 joint shear–redshift image-simulation paper (cited as Mau,
  Becker et al. 2025 in arXiv:2501.05665 and as [111] in arXiv:2602.10065):
  its identifier was not found in this session.
- The final m values of the KiDS-1000 metacalibration reanalysis (its
  Table 2) and of SKiLLS (its Table 2): not read.
- Euclid's own shape method (LensMC) and its calibration for DR1: not read.
- The claim of the Pantos 2026 review that ΔS8/S8 ≈ m (Sect. 4.1.1) was read
  but not checked against an analysis.
