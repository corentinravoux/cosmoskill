# Data pipelines — physics and methods

Scope: how raw spectra, images and time-ordered data become redshift
catalogues, object catalogues, maps, masks and randoms; the algorithms and
their defining equations, and the public pipelines with their reference papers.
Snapshot: 2026-10-16

Flags: `[src]` abstract read this session; `[src: Sect. n]`, `[src: Table n]`,
`[src: Eq. n]` body read; `[sec]` named secondary source; `[der]` derived here.

## 1. Target selection
<!-- key: target-selection -->

A spectroscopic survey observes what its target selection chose from earlier
imaging, so the selection function of every redshift catalogue starts in the
photometric catalogue. Photometric calibration and the dust maps that enter
the colour cuts are treated in `cosmo-photometry-photoz`; this section keeps
the algorithms and their bookkeeping.

The selections of each survey are tabulated in `surveys-and-data.md`
(Sect. 1).

DESI's targeting bookkeeping (TARGETID, bitmasks, sky fibres, randoms,
north–south resolve) is in `surveys-and-data.md` (Sect. 1).

**Selection as a systematic.** The target density depends on depth, seeing,
extinction and stellar density; the regression of target density on those
maps is in Sect. 9. 4MOST CRS validated its BG and LRG catalogues with
w(θ), mask tests (Legacy Surveys MASKBITS, unWISE W1 artefact masks for
LRGs) and clustering redshifts against DESI DR1 before observing
(arXiv:2510.02449) [src].

**Next targets.** DESI's second phase moves to Lyman-break galaxies at
z ~ 2–4.5, where decontamination from quasars and low-redshift ELGs is done
after target selection by networks trained on visually inspected spectra
(Choppin de Janvry et al. 2026, arXiv:2608.10080) [src].

## 2. Fibre assignment and survey operations
<!-- key: fibre-assignment-and-survey-operations -->

Fibre assignment decides which targets get a spectrum. Its imprint on
clustering, and the corrections (PIP weights, θ-cut, altMTL completeness), are
in `cosmo-galaxy-clustering` (systematics, Sect. 4); this section gives the
algorithms and the operational bookkeeping that make those corrections
possible.

**Plates.** SDSS placed 640 fibres in a tile of 1.49° radius, with no two
fibres closer than 55″; tile centres were perturbed away from a uniform
covering to follow the large-scale structure of the targets, reaching a
sampling rate above 92% for all targets and above 99% for non-colliding ones,
at an efficiency above 90% (Blanton et al. 2003, arXiv:astro-ph/0105535)
[src: abstract].

**Robotic positioners.** With patrol regions that overlap, the number of
targets reached depends on the assignment scheme. Proposed schemes: a
"draining" algorithm that maximises targets in the first tiles and a gain of
3.5–4.5% from small focal-plane rotations (Morales et al. 2011,
arXiv:1103.0988) [src]; simulated annealing ("Configure") for the ~960 WEAVE
fibres (Hughes et al. 2022, arXiv:2209.01145) [src]; a two-step
assign-then-resolve-collisions algorithm that gains 10% in completeness over
rank ordering in a 150-fibre field (Kwon et al. 2026, arXiv:2601.02795)
[src].

**More targets than fibres.** In deep surveys such as PFS the number of
galaxies per field is nearly fixed by the number of fibres, which erases
modes longer than the field and favours underdense regions; weighting by the
number of targets per field and by individual inverse probability recovers
the correlation function to better than 1% above 10 h⁻¹ Mpc (Sunayama et al.
2020, arXiv:1912.06583) [src]. The same assignment correlates structure at
different redshifts and suppresses galaxy–lensing cross-spectra; individual
inverse-probability weights correct the cross-spectrum to ~1%, while the
auto-spectrum is not fully corrected at k ≳ 0.2 h Mpc⁻¹ (Makiya et al. 2021,
arXiv:2110.04883) [src].

**Correction families** (detail in `cosmo-galaxy-clustering`):
pair-inverse-probability (PIP) weights from rerunning the assignment with
varied priorities (Bianchi & Percival 2017, arXiv:1703.02070) [src], shown
unbiased for DESI after any number of passes, with BAO errors (**forecast**, mocks) a factor 2
worse after one pass but similar to a random-sampling survey after three
(Bianchi et al. 2018, arXiv:1805.00951) [src]; a modified statistic that
nulls the nearly angular modes affected by assignment (Burden et al. 2017,
arXiv:1611.04635) [src]. DESI produces the PIP realisations as alternate
merged target ledgers that are propagated through the real observing history
and hardware state (Lasker et al. 2024, arXiv:2404.03006) [src].

DESI's survey-operations loop, which feeds redshifts back into targeting,
is in `surveys-and-data.md` (Sect. 1).

## 3. Spectral extraction, calibration and sky subtraction
<!-- key: spectral-extraction-calibration-and-sky -->

**Order of operations in a fibre pipeline** (DESI, Guy et al. 2023,
arXiv:2209.14482, Sect. IV): bias, dark and overscan subtraction; gains;
electronic cross-talk; cosmic rays; flat field; scattered light; bad pixels and
variance; spectrograph PSF fit; wavelength and trace calibration from arcs and
sky lines; extraction; fibre flat field; sky subtraction; stellar-template
fit to standard stars; flux calibration; fibre cross-talk; co-addition;
classification and redshift [src: Sect. IV outline]. The pipeline serves 5000
fibres on 30 CCDs over 3600–9800 Å at R = 2000–5000, and each night is
processed by the next morning [src].

**Extraction.** Optimal extraction weights the cross-dispersion profile by
inverse variance (Horne 1986, doi:10.1086/131801); it is exact only for
separable PSFs. Spectro-perfectionism forward-models the 2D pixels with the
full 2D PSF, giving statistically independent samples at native resolution
and a resolution matrix R with which any model must be convolved before a χ²
(Bolton & Schlegel 2010, arXiv:0911.2689) [src]. DESI uses it: every fibre is
on a common wavelength grid with uncorrelated noise, at the price that R is
not flux-conserving, so one fits R·M to F rather than M
[src: arXiv:2209.14482, Sect. IV.5.7].

**Sky subtraction.** The three families:

| Family | Idea | Reference |
|---|---|---|
| Mean or model sky from dedicated sky fibres | fit one deconvolved sky spectrum S through each fibre's resolution matrix and flat field, optionally with a polynomial over focal-plane position and wavelength: χ² = Σ_k Σ_i w_ki (F̃_ki − T_ki Σ_j R_kij P(x_k, y_k, λ_j) S_j)² | DESI, arXiv:2209.14482 [src: Sect. IV.7.1, Eq. 14] |
| PCA of sky residuals | removes systematic residuals left by the mean model; in AAOmega the residual falls as t^−0.32 instead of t^−0.5 over 200 h of data | Sharp & Parkinson 2010, arXiv:1007.0648 [src: abstract] |
| Beam switching or nod-and-shuffle | the object fibre also measures the sky; cross-beam switching and dual stare reach < 1% accuracy on FLAMES | Rodrigues et al. 2016, arXiv:1609.06142 [src] |

Variants: a 2D background model built before rectification, insensitive to
cosmic rays, so that sky subtraction can come right after the flat field
(Kelson 2003, arXiv:astro-ph/0303507) [src]; non-negative matrix
factorisation in place of PCA, giving about 10 times as many valid
eigenspectra (Kolganov et al. 2023, arXiv:2312.06761) [src]; LAMOST uses
sky emission lines to correct ~4% fibre-throughput uncertainty, then PCA
(Bai et al. 2017, arXiv:1705.02079) [src].

**Flux calibration.** Standard stars fitted with stellar templates per
exposure; DESI checks the result on DA white dwarfs and corrects for
fibre-aperture losses [src: arXiv:2209.14482, Sect. IV.9]. Calibration of
the photometric scale itself is in `cosmo-photometry-photoz`.

**Noise model.** DESI adds a term ε_λ to the variance of sky-subtracted
spectra to absorb flat-field, wavelength and PSF errors on sky lines; with it
the scatter in sky fibres matches the model at most wavelengths, which
matters for the redshift fitter's Δχ² [src: arXiv:2209.14482,
Sect. IV.7.4–IV.7.5].

## 4. Redshift fitting, classification and visual inspection
<!-- key: redshift-fitting-classification-and-visual -->

**Template χ² fitting.** The standard is a χ² scan over redshift of linear
template combinations, per spectral class, with the class and redshift of the
lowest χ² retained and Δχ² to the next solution as the confidence measure.
BOSS fitted PCA templates for stars, galaxies and quasars and characterised
success with visual inspection and repeat observations (Bolton et al. 2012,
arXiv:1207.7326) [src]. eBOSS redmonster used physical archetypes with
additive polynomials, choosing the number of terms and the Δχ²_r threshold
empirically (Hutchinson et al. 2016, arXiv:1607.02432) [src]. DESI Redrock
fits PCA templates of STAR, GALAXY and QSO on class-dependent redshift grids
and reports Z, ZERR, SPECTYPE, CHI2, DELTACHI2 and the warning bitmask ZWARN;
DELTACHI2 = 25 reads as a 5σ preference before systematics (DESI DR1,
arXiv:2503.14745) [src: Sect. III.1.2]. Redrock's PCA fits have no physical
constraint beyond penalising negative [O II] flux, which makes them prone to
false fits when sky subtraction or arm-to-arm calibration leaves steps
[src: arXiv:2209.14482, Sect. IV.13]. Archetype refits address that
(Anand et al. 2024, arXiv:2405.19288) [src]. DESI quasar templates were
rebuilt as two eigenspectrum sets for overlapping redshift ranges, covering
0.05 < z < 7.0 (Brodzeller et al. 2023, arXiv:2305.10426) [src].

**Cross-correlation codes.** GAMA's autoz cross-correlates high-pass
filtered spectra with templates, clips large deviations, and calibrates a
single figure of merit against repeats with a tanh fit (Baldry et al. 2014,
arXiv:1404.2626) [src].

**After-burners.** For DESI, emission-line fits, an Mg II λ2800 fit and the
QuasarNET classifier run after Redrock, and are needed to judge ELG
redshifts and to classify some quasars [src: arXiv:2503.14745,
Sect. III.1.2]. QuasarNET treats classification and redshift as feature
detection by a convolutional network (Busca & Balland 2018,
arXiv:1808.09955) [src].

**Slitless spectroscopy.** Euclid has no target selection and no fibres: the
SIR processing function extracts spectra from NISP grism images using a
source catalogue from photometry, subtracts cross-contamination by
neighbouring traces and calibrates wavelength and flux (Euclid
Collaboration 2025, arXiv:2503.15307) [src]; the SPE function then
measures redshifts, line fluxes and classes. Because most spectra show one
line or none, quality cuts on the redshift probability and on Hα flux and
S/N are required to avoid noise peaks and misidentified lines (Euclid
Collaboration 2025, arXiv:2503.15308) [src].

**Truth tables.** Success and purity are defined against visual inspection
of deep co-adds and repeats; the VI programmes are listed in `results.md`
(Sect. 1).

**Definitions to pin down when comparing success rates.** "Success" can
mean the fraction of targets, of observed fibres, or of good-hardware fibres
passing a quality cut; "purity" is measured against VI or repeats with a
velocity tolerance (3000 km/s for DESI quasars in arXiv:2208.08517) [src: abstract].
Numbers from different surveys are comparable only after these are matched.

## 5. Image detrending and astrometry
<!-- key: image-detrending-and-astrometry -->

**Instrument signature removal (ISR).** The pipeline works backward through
the signal chain, from ADU to photoelectrons. The Rubin DP1 order is ADU
dithering, serial overscan, saturation masking, gain normalisation,
crosstalk, parallel overscan, linearity, serial charge-transfer
inefficiency, image assembly, bias, dark, brighter-fatter correction, defect
masking and interpolation, variance plane, flat field and amplifier-offset
correction (Rubin Observatory Team 2026, arXiv:2603.23786)
[src: Sect. IV.2.1]. The pipeline of each imaging survey is in
`surveys-and-data.md` (Sect. 2).

**Sensor effects that must be modelled, not only flat-fielded.**

- Brighter-fatter: star sizes grow linearly with flux by up to 2% over the
  CCD dynamic range, because accumulated charge shifts pixel boundaries;
  the same physics makes flat-field pixels correlated (Antilogus et al.
  2014, arXiv:1402.0725) [src]. In DECam the flat-field correlations fall
  as r^−2.5, vary by 20% between chips with silicon resistivity, and bias
  shapes of bright stars beyond lensing requirements unless reverse charge
  shifts are applied at pixel level; residuals in stellar size remain
  (Gruen et al. 2015, arXiv:1501.02802) [src].
- Stray electric fields in CCDs, crosstalk, charge-transfer inefficiency,
  vampire pixels, phosphorescence and bleed trails appear as known issues in
  Rubin DP1 [src: arXiv:2603.23786, Sect. V.1 outline].

**Astrometry.** The DECam model includes optical distortion, stray fields in
the detectors, chromatic terms, CCD shifts of up to ~10 μm with thermal
cycles, and per-exposure low-order distortions; its error is dominated by
atmospheric turbulence of 10–30 mas in 30 s with 5–10′ coherence, which a
Gaia-density reference catalogue interpolates to 7 mas RMS; the remaining
solution is accurate to 3–6 mas (Bernstein et al. 2017, arXiv:1703.01679)
[src]. Rubin DP1 fits a per-detector degree-4 polynomial and a per-visit
degree-6 polynomial with gbdes against Gaia DR3, accounting for proper motion
and parallax; differential chromatic refraction was not corrected in DP1
[src: arXiv:2603.23786, Sect. IV.3.2].

## 6. PSF modelling in imaging pipelines
<!-- key: psf-modelling-in-imaging-pipelines -->

The PSF model of an imaging pipeline feeds PSF photometry, model fitting,
star–galaxy separation, deblending and shear. Its effect on shear (ρ
statistics, leakage coefficients, B modes) is in `cosmo-weak-lensing`
(systematics, Sect. 3); here only the pipeline step.

**Steps.** (1) Select a clean star sample; (2) model each star in pixels or
in a basis; (3) interpolate across the CCD or the full focal plane; (4)
propagate to co-adds. A review of physical contributors (optics, detector,
atmosphere), parametric and non-parametric models, and validation metrics is
Liaudat et al. 2023, arXiv:2306.07996 [src].

The star selection and model of each survey are tabulated in
`surveys-and-data.md` (Sect. 2).

Piff is to be the default PSF software for Rubin lensing analyses
(arXiv:2501.05781) [src].

**Co-add PSF.** Dithers make the effective co-add PSF discontinuous, so
there are too few stars per continuous region to model it from the co-add.
HSC instead resamples and combines the single-exposure PSF models with the
same transforms and weights as the pixels, evaluated on demand at each
object (the Jee & Tyson approach) [src: arXiv:1705.06766, Sect. 3.3.1]. The
approximation that the PSF at an object's centre holds for the whole object
fails where the number of inputs changes [src: Sect. 3.3.1].

## 7. Detection, deblending, co-addition and photometry
<!-- key: detection-deblending-co-addition-and-photometry -->

**Co-addition.** For detection and flux, the S/N-optimal combination of
images with different seeing is to matched-filter each image with its own
PSF and then sum with weights; PSF homogenisation before co-addition, or
filtering after, loses sensitivity, and the optimal scheme gains between a
few and 25% in survey speed over weighted co-addition (Zackay & Ofek 2017a,
arXiv:1512.06872) [src]. In the background-dominated limit a "proper"
co-add exists with uncorrelated pixels, no information loss at any spatial
frequency, and a PSF as narrow as or narrower than the best input (Zackay &
Ofek 2017b, arXiv:1512.06879) [src]. Production pipelines (HSC, Rubin) build
weighted, warped co-adds with clipping and a co-add PSF assembled from the
inputs (Sect. 6) [src: arXiv:1705.06766, Sect. 3.3].

**Detection and deblending.** SExtractor set the standard for detection and
segmentation (Bertin & Arnouts 1996, doi:10.1051/aas:1996164). Successors:

| Method | Principle | Where | Source |
|---|---|---|---|
| SDSS-heritage template deblender | symmetric templates per peak; fails when three or more peaks are aligned, in cluster cores and near bright galaxies or stars | HSC SSP early releases | arXiv:1705.06766 [src: Sect. 4.8.3] |
| SCARLET | constrained non-negative matrix factorisation, multi-band, positivity, symmetry and monotonicity, band-dependent PSFs; better fluxes, colours and morphologies than the HSC-SDSS deblender in crowded simulations; sensitive to undetected sources | HSC, Rubin | Melchior et al. 2018, arXiv:1802.10157 [src] |
| Forward-model photometry (Tractor) | probabilistic inference of source shapes and fluxes across bands and WISE | Legacy Surveys | Dey et al. 2019, arXiv:1804.08657 [src] |
| DeepDISC | scene-level network: detection, segmentation, star–galaxy class in one pass | applied to Rubin DP1 | Yadav et al. 2026, arXiv:2610.10986 [src] |
| BLISS | simulation-based inference: posterior over number, positions and types of sources; flux posteriors | LSST year-10 simulations | Mendoza et al. 2026, arXiv:2601.03422 [src] |

HSC mitigates its deblender's failures by suppressing minor peaks before
deblending, by a blendedness metric, and by photometry on undeblended pixels
at the child positions [src: arXiv:1705.06766, Sect. 4.8.3].

**Benchmarks.** The LSST DESC Blending ToolKit benchmark finds SCARLET best in
segmentation and reconstruction, DeepDISC best in recall for faint sources,
and SourceExtractor accurate in peak finding only; unrecognised blends are
the regime that biases cosmology (Berres et al. 2026, arXiv:2607.28475)
[src].

## 8. CMB time-ordered data to maps
<!-- key: cmb-time-ordered-data-to-maps -->

Power-spectrum estimation, transfer-function correction in pseudo-C_ℓ
(MASTER), ranges used in the likelihoods, and foreground separation are in
`cosmo-cmb` (physics-and-methods, Sects. 4–5). This section holds the
map-making problem itself.

**The linear problem.** Time-ordered data d = P m + n, with P the pointing
(and polarisation-angle) matrix and noise covariance N. The generalised
least-squares map m̂ = (Pᵀ N⁻¹ P)⁻¹ Pᵀ N⁻¹ d is unbiased if the data were not
filtered beyond what N⁻¹ captures, and optimal if N is the true noise
covariance; solving it iteratively (conjugate gradients) and stopping early
biases it [src: arXiv:2503.14451, Sect. V.2]. For Gaussian data the COBE
method and Wiener-filter variants keep all the cosmological information of
the TOD, while simple pixel averaging, maximum entropy and most non-linear
methods destroy information (Tegmark 1997, arXiv:astro-ph/9611130) [src]. An
introduction to the problem and to MAPPRAISER is Biquard 2024,
arXiv:2405.10239 [src].

**Families.**

| Family | Idea | Example | Source |
|---|---|---|---|
| Destriping | low-frequency noise as a sum of baselines whose amplitudes are fitted by maximum likelihood; Madam adds the noise spectrum as a prior | Planck LFI | Keihänen et al. 2005, arXiv:astro-ph/0412517 [src] |
| Destriping by Gibbs sampling | noise filtering and binning as two cheap steps; baselines down to one sample; chain gives residual-noise information; CG faster for a single ML map | BeyondPlanck, Planck 30 GHz | Keihänen et al. 2020, arXiv:2011.06024 [src] |
| Template fitting of instrument effects | ADC non-linearity and polarisation efficiencies fitted from data redundancy | Planck HFI SRoll2 | Delouis et al. 2019, arXiv:1901.11386 [src] |
| Maximum likelihood with extended data model | d = P m + C c + S s + n, with cut-sample amplitudes c and model-error degrees of freedom s near bright sources; maximum-posterior solution (AᵀN⁻¹A + Π)⁻¹AᵀN⁻¹d, a ~10⁹ × 10⁹ system solved by preconditioned CG | ACT DR6 | arXiv:2503.14451 [src: Sect. III.3, Eqs. 3–5] |
| Filter and bin | high-pass filter each detector's TOD, then bin; transfer function from simulations | SPT-3G | Quan et al. 2026, arXiv:2603.20163 [src] |
| Filtering with explicit correction | a filtering operator that removes chosen modes is equivalent to marginalising them in the map solution; unbiased but not always best for pseudo-spectra | POLARBEAR | Poletti et al. 2017, arXiv:1608.01624 [src] |
| Half-wave-plate demodulation-style marginalisation | marginalise all signals slow compared with the polarimeter angle rotation; near-optimal noise when unpolarised signals vary slower than a quarter HWP period | POMME in FURAX, for upcoming ground surveys | Sohn et al. 2026, arXiv:2606.31720 [src] |

ACT DR6's multipass scheme and transfer-function measurement are in
`surveys-and-data.md` (Sect. 3).

Planck's processing chains are summarised in `surveys-and-data.md`
(Sect. 3).

## 9. Catalogue construction: masks, randoms, completeness, weights
<!-- key: catalogue-construction-masks-randoms -->

A clustering catalogue is a weighted data sample paired with a weighted
random sample that is an unclustered draw from the probability that the
survey could have observed an object at each position (Ross et al. 2025,
arXiv:2405.16593) [src]. How the weights enter the estimators, the window
and the integral constraints is in `cosmo-galaxy-clustering`.

**Masks.** Angular masks were long stored as spherical polygons: an SDSS mask
has ~300,000; mangle pixelises them so overlap tests go from O(N²) to O(N)
and point-in-mask from O(N) to O(1), and converts to and from HEALPix
(Swanson et al. 2008, arXiv:0711.4352) [src]. DESI defines its footprint and
coverage count at sub-arcsecond precision from the observing history and
hardware state (arXiv:2405.16593) [src]. Vetoes then cut to good hardware
(ZWARN_MTL from the same reduction as the redshifts; bad fibres re-evaluated
per release, 60 removed for DR1) and to a threshold in template S/N squared
(TSNR2), which depends on exposure and fibre noise, not on source
brightness [src: arXiv:2405.16593, Sect. 4.2]. Imaging masks (bright stars,
large galaxies, WISE artefacts) come from the parent imaging; 4MOST CRS
uses Legacy Surveys MASKBITS and unWISE W1 masks (arXiv:2510.02449) [src].

**Randoms.** Angular positions from the targeting randoms (Sect. 1);
redshifts and weights sampled from the data within each photometric region
(DECam vs BASS/MzLS; DES vs non-DES for quasars), so the weighted dN/dz of
randoms equals that of data, at the cost of nulling radial modes (radial
integral constraint) [src: arXiv:2405.16593, Sect. 7.2]. Euclid, with no
target list, builds randoms from a detection model of redshift success as a
function of emission-line S/N, the "visibility mask"; with perfect
knowledge of it the power spectrum is recovered to sub-per cent by
convolving theory with the random-catalogue window (Euclid Collaboration
2025, arXiv:2511.20856) [src]. Synthetic injections can serve as randoms:
using Balrog injections in the Landy–Szalay estimator suppressed variable
selection by at least two orders of magnitude for the faintest DES galaxies
(Suchyta et al. 2016, arXiv:1507.08336) [src].

**Weights.** Completeness (fibre assignment), imaging-systematics,
redshift-failure and FKP weights multiply into a total weight for data and
randoms; the DESI DR1 definitions are in `surveys-and-data.md` (Sect. 1).
The FKP weight is from Feldman, Kaiser & Peacock 1994, arXiv:astro-ph/9304022
[src]. BOSS released its catalogue code MKSAMPLE (arXiv:1509.06529) [src];
eBOSS DR16 catalogues apply analogous corrections, the quasar χ²/dof
against imaging depth going from 776/10 to 6/8 (Ross et al. 2020,
arXiv:2007.09000) [src].

**Imaging-systematics weights: methods.**

| Method | Idea | Caveat | Source |
|---|---|---|---|
| Survey-property maps | project depth, seeing, airmass, sky onto the sky per band | needed by all methods below | Leistedt et al. 2016, arXiv:1507.05647 [src] |
| Template subtraction, mode projection | regress or project out template maps in C_ℓ | original template subtraction is biased; basic mode projection unbiased; extended mode projection biased; all add variance | Elsner et al. 2016, arXiv:1509.08933 [src] |
| Common regression framework | all methods as regressions; extension to multiplicative contamination and cleaned maps | — | Weaverdyck & Huterer 2021, arXiv:2007.14499 [src] |
| Neural network (SYSNet) | non-linear density model with k-fold cross-validation and feature elimination; beats linear and quadratic fits on eBOSS ELGs | can remove real modes (see `cosmo-galaxy-clustering`) | Rezaie et al. 2020, arXiv:1907.11355 [src] |
| Iterative and ElasticNet-type decontamination, DES Y3 lenses | several methods, systematic uncertainty from their spread | biases ≤ 0.5σ in (Ω_m, b) on log-normal mocks | Rodríguez-Monroy et al. 2022, arXiv:2105.13540 [src] |
| Forward model by injection (Obiwan, Balrog) | the selection function from the real pipeline | costly; see Sect. 10 | arXiv:2007.08992, arXiv:2012.12825 [src] |

## 10. Source injection and end-to-end simulation of pipelines
<!-- key: source-injection-and-end-to-end-simulation-of -->

Injecting synthetic sources into real images and running the unchanged
pipeline measures the "transfer function" from truth to catalogue: detection
probability, photometric and shape biases, star–galaxy errors, and their
dependence on observing conditions.

The programmes and what each measured are tabulated in `results.md`
(Sect. 5b).

In DES, injection informs source photo-z calibration and lens
magnification (arXiv:2012.12825) [src]; for DESI ELGs, Obiwan simulations
reproduce imaging trends qualitatively but not statistically, so they were
not adopted as the DR1 correction [sec: cosmo-galaxy-clustering,
systematics Sect. 5].

## 11. Data-release practice and validation
<!-- key: data-release-practice-and-validation -->

**Practice in current releases.** A release is the reduction version plus
the catalogues, masks, randoms, survey-property maps and known-issues list
built from it; the contents per survey are in `surveys-and-data.md`
(Sect. 4). DESI develops its pipeline open source with pull-request review,
unit tests on every change and nightly end-to-end tests at NERSC; eBOSS used
DESI's Redrock for its final cosmology, testing it on real data years before
DESI observed [src: arXiv:2209.14482, Sect. V]. Rubin ships task
configurations, logs and calibration products with DP1
[src: arXiv:2603.23786, Sect. III.6 outline]; NPIPE ships the raw and
processed TOD, the software and 600 simulations (arXiv:2007.04997) [src].

**Validation layers.** (1) Internal: repeats, null splits, residual maps
against the noise model. (2) External truth: VI and deep fields for
redshifts; Gaia for astrometry and photometric uniformity; space imaging for
blends and completeness; Planck for ground CMB maps. (3) Injection through the
real pipeline (Sect. 10). (4) Known-issues sections that users must read:
Euclid Q1 produces a redshift for every H_E < 22.5 source (~4.3 million
spectra) while under 10% allow a measurement, and its stacks filter out low
surface brightness [src: arXiv:2503.15302, Sect. 9]; HSC PDR3 warns that the
pipeline is not optimised for crowded fields (arXiv:2108.13045) [src].

**Blinding at catalogue level.** Shifting galaxies along the line of sight
by an AP-like geometric shift and an RSD-like perturbative shift blinds BAO
and growth without touching angular systematics, and works for any
downstream statistic (Brieden et al. 2020, arXiv:2006.10857) [src]. How each
probe blinds is in the probe skills and `cosmo-statistics-inference`.

## Not verified
<!-- key: not-verified -->

- Redrock reference paper (cited by DESI as in preparation) not read.
- Legacy Surveys Tractor algorithm paper not read; cited through the Legacy Surveys overview.
- PSFEx and SWarp reference papers not read.
- 4MOST and PFS reduction pipelines: no pipeline paper found within budget.
- Rubin DP1 deblender (Scarlet variant) not confirmed in the body.
