# Source injection and end-to-end pipeline simulation — cosmo-data-pipelines dossier

Scope: how a synthetic-source-injection run is designed and executed (input
truth catalogue, rendering, where in the pipeline the sources enter,
injection pattern and density, matching back, outputs), how its products are
turned into selection functions, weights, depth, magnification and n(z)
inputs, and how to choose between the DES, Legacy Surveys, HSC and Rubin
variants.
Snapshot: 2026-10-17.
From: Bosch et al. 2018, Sect. 5; DES (Balrog) and Legacy Surveys (Obiwan)
validation programmes (copied from `references/subtopics.tsv`).

Already in L2, not repeated here: the one-paragraph definition of injection
as a measured transfer function (`physics-and-methods.md#source-injection-and-end-to-end-simulation-of`),
the programme-by-programme table of scales and headline results
(`results.md#source-injection-results`), injections used as randoms
(`physics-and-methods.md#catalogue-construction-masks-randoms`), and
injection as one of the imaging-weight methods
(`systematics.md#imaging-systematics-weights-over-and-under`). The DESI
clustering consequences of the ELG weights are in `cosmo-galaxy-clustering`
(systematics, Sect. 5).

## How it is done
<!-- key: how-it-is-done -->

The procedure below follows DES Y3 Balrog (Everett et al. 2022,
arXiv:2012.12825), the most fully documented run; the other programmes are
compared to it under "Choices and what they cost".

### Step 1. Decide where the sources enter the pipeline
<!-- key: step-1-decide-where-the-sources-enter-the -->

Balrog Y3 re-runs the DES data-management (DESDM) chain for each
44′ × 44′ co-add tile [src: arXiv:2012.12825, Sect. II.1]:

1. Fetch the single-epoch, flattened, sky-subtracted, masked images in griz
   with their PSFs, zero points and astrometric solutions; set weights of
   flagged pixels (cosmic rays) to zero ("null-weighting").
2. Rebuild the co-add and detection catalogue without injections, as a
   cross-check that the emulation reproduces the Y3 Gold detections.
3. Inject the same objects in every overlapping exposure and band with the
   local PSF, zero point and extinction.
4. Re-co-add and re-detect (SWarp, SExtractor).
5–9. Single-object fitting (SOF, bulge + disk CModel with neighbours
   masked), optionally multi-object fitting (MOF), metacalibration,
   Gaussian-aperture (GAp) fluxes, and BFD shears on special runs.
10. Match injections to detections and compute the Gold value-added columns.

What injection cannot test follows from where it enters: the existing PSF
models, zero points and WCS are reused unchanged, so biases from PSF
modelling and image detrending upstream of step 3 are not probed
[src: Sect. II.1.1]. The same holds for HSC SynPipe, which takes the
pipeline's single-visit background subtraction and PSF as given and so
cannot test background over-subtraction around bright objects or PSF-model
errors (Huang et al. 2018, arXiv:1705.01599) [src: Sect. 3.3].

### Step 2. Build the truth catalogue
<!-- key: step-2-build-the-truth-catalogue -->

Balrog Y3 does not inject deep-field images but idealised profiles rendered
from the ngmix "bdf" model fits (bulge + disk sharing one size, fixed size
ratio) of ~3 million sources detected in DES deep fields (three supernova
fields and COSMOS), whose co-adds have S/N about √10 times the wide survey,
with Poisson noise added [src: arXiv:2012.12825, Sect. III.1]. Selection
[src: Sect. III.4]:

| Cut | Stated reason |
|---|---|
| flags = 0, mask_flags = 0 | remove fit failures and masked deep-field regions |
| in VHS footprint | near-infrared bands needed for photo-z calibration |
| bdf_T < 100 arcsec² (~10″) | limit injection–injection blends on the grid |
| flux/err > −3 in every band | excess of extremely negative fluxes found by inspection |
| riz detection magnitude < 25.4 | objects fainter have < 1% chance of detection in a 200-tile test; still ~2 mag deeper than the wide field |

After the cuts the main and auxiliary input catalogues hold about 1.23
million and 746,000 objects; stars were added separately at 10% of the
injections, sampled to g = 27 [src: Sect. III.4].

Extinction: each deep-field object is dereddened with the mean SFD E(B−V)
of five points of its CCD and re-reddened with the five-point mean of the
wide tile, a chip-and-tile-level approximation; per-object corrections were
planned for Y6 [src: Sect. III.1.1].

The Y6 run keeps the same detections and cuts (Eq. 3.1 of Anbajagane et al.
2025, arXiv:2501.05683), refits the models with the Y6 version of the
fitter, injects real deep-field stars instead of a simulated star sample,
and down-weights probable stars with a sigmoid in size and magnitude
(Eq. 3.2) [src: arXiv:2501.05683, Sects. 3.1, 3.4].

### Step 3. Render and add
<!-- key: step-3-render-and-add -->

Each object is convolved with the local single-epoch PSF model (PSFEx in Y3)
and drawn by GalSim from a configuration file generated per tile; the
rendered stamp, with its own Poisson noise, is added to the image
[src: arXiv:2012.12825, Sects. II.2.4–II.2.5]. The authors chose
configuration files over the Python API because they make runs reproducible
and allow runs that differ only by, for example, a magnification factor
[src: Sect. II.2.5]. FFT grids are capped at 16,384 pixels per side; larger
objects are skipped [src: same]. SynPipe also adds a variance plane for the
injected flux, using a per-amplifier gain map, and sets a FAKE mask bit
[src: arXiv:1705.01599, Sect. 3.2.2].

### Step 4. Choose the pattern and density
<!-- key: step-4-choose-the-pattern-and-density -->

Balrog Y3 places objects on a hexagonal lattice with 20″ spacing in a single
realisation, about 7.8 objects arcmin⁻², ~40% of the Y3 object density
[src: arXiv:2012.12825, Sect. III.4]. Stated reasons: a lattice, unlike
random positions, keeps the self-blending rate low at high density, which
matters because one Y3 tile realisation costs ~40 times one SV or Y1
realisation [src: same]. Cost: clustering of the injections cannot be used
below the grid scale, which was well below the ~10′ Y3 scale cuts
[src: same]. Y6 keeps the 20″ lattice, with a 10″ padding from tile edges,
justified by the 10″ half-light-radius limit of the inputs
[src: arXiv:2501.05683, Sect. 3.2].

### Step 5. Match injections to detections
<!-- key: step-5-match-injections-to-detections -->

Re-detection changes the number of objects and can merge injected and real
sources. "Any matched catalog from an injection pipeline has made
assumptions about ambiguous matches and blending" [src:
arXiv:2012.12825, Sect. III.5]. Balrog Y3 therefore saves the full
remeasured catalogue and applies a two-step match [src: same]:

- Injection positions matched to the nearest detection within
  r₁ = 0.5″.
- Then matched to Y3 Gold within r₂ = 0.5″–2.0″ in 0.25″ steps; the
  "antecedent" of a blend is the brighter of the contributors by mean riz
  GAp flux (4″ FWHM Gaussian aperture on the PSF-deconvolved profile);
  injections fainter than a real neighbour get match_flag = 2 and are cut.
- Over 96% of candidates have no Gold source within the aperture;
  ambiguous cases are < 1.5% at the Y3 injection density.

Y6 replaces this with a more conservative flag: every detected injection
with a real object within 1.5″ is removed, whatever their relative
brightness; this is < 0.2% of the catalogue [src: arXiv:2501.05683,
Sect. 3.4]. SynPipe matches within 2 pixels and rejects injections within
2 pixels of a real object as "ambiguously blended" [src: arXiv:1705.01599,
Sect. 4.3]; original Balrog ran SExtractor in association mode, measuring
only detections within 2 pixels of an injection position, with detection
still run over the full image [src: Suchyta et al. 2016, arXiv:1507.08336,
Sect. 2.3].

### Step 6. Validate the emulation before using it
<!-- key: step-6-validate-the-emulation-before-using-it -->

Balrog Y3 validation ladder [src: arXiv:2012.12825, Sect. II.3]:

1. Injection switched off: recover the Y3 Gold detections and photometry
   exactly, with the same fitter random seeds.
2. Profiles drawn on blank images compared with independent single-object
   renderings.
3. Blank-image runs on a sparse grid, first with Poisson noise only, then
   with Gaussian sky noise of the CCD SKYVAR; final version on 200 tiles,
   2.3 million injections, 1.6 million detections.

The blank-image runs found a ~7.5 mmag faint offset for one subgroup,
traced to different priors on the bulge fraction (fracdev) in the
deep-field model and in the wide-field CModel; this sets a ~3 mmag floor on
the mean magnitude response measurable with deep-field inputs, while colours
are unaffected [src: Sect. II.3].

### Step 7. Turn the output into a product
<!-- key: step-7-turn-the-output-into-a-product -->

| Product | Construction | Source |
|---|---|---|
| Transfer function for photo-z | p_Balrog(c given ĉ, ŝ, θ): probability that a deep SOM cell c is observed in wide cell ĉ under selection ŝ (Eq. 3) | arXiv:2012.12825 [src: Sect. V.1] |
| Magnification coefficient | rerun with δκ = 0.01 (flux and area +2%), same seeds; C_sample δκ = [n_obs(F; κ+δκ) − n_obs(F; κ)] / n_int(F) (Eq. 8), C_area = −2 | arXiv:2012.12825 [src: Sect. V.2]; Y6: 2% magnification run on 2000 tiles, arXiv:2501.05683 [src: Sects. 3.3–3.4, 5.2] |
| Depth | objects with 9.5 < flux/err < 10.5, extended, mean magnitude per NSIDE = 256 pixel, median over the footprint | arXiv:2501.05683 [src: Sect. 5.3] |
| Imaging-systematics weight | HEALPix N_side = 128 map of selected injections divided by uniform injections, normalised, inverted, used in place of w_sys | Kong et al. 2020, arXiv:2007.08992 [src: Sect. 5.3] |
| Null test of data weights | cross-correlate weighted data with the injected sample; zero if weights remove all shared systematics | arXiv:2501.05683 [src: Sect. 5.4]; arXiv:2105.13540 [src: Sect. 8.5] |
| Radial selection | N(z) by depth quintile from injections fitted as R(z, depth) = F(z) G(depth), broken-linear F, erf G (Eqs. 9–13) | Rosado-Marín et al. 2024, arXiv:2411.12024 [src: Sect. 6.1] |
| Randoms | injections that pass the selection used directly in Landy–Szalay | arXiv:1507.08336 [src: Sect. 5.2] |

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Single-epoch or co-add injection
<!-- key: single-epoch-or-co-add-injection -->

| Choice | Used by | Buys | Costs |
|---|---|---|---|
| Co-add | Balrog SV (arXiv:1507.08336) [src: Sect. 3.3]; Rubin DP1 completeness (arXiv:2603.23786) [src: Sect. V.6] | ~10× cheaper than single-epoch for Balrog SV | co-add PSF a poorer model than the set of single-epoch PSFs; insufficient for lensing |
| Single-epoch | Balrog Y3/Y6, SynPipe, Obiwan | seeing differences between visits and small astrometric errors are included; every step from detection to stacking is exercised (arXiv:1705.01599) [src: Sect. 3.1] | run time: all visits of a tract must be modified |

Balrog SV authors judged the co-add approximation sufficient for clustering
and not for lensing [src: arXiv:1507.08336, Sect. 3.3].

### Emulated pipeline or injection inside the production stack
<!-- key: emulated-pipeline-or-injection-inside-the -->

Balrog Y3 had to replicate DESDM because the injection code did not exist
when Y3 was processed; differences (fewer SExtractor parameters, MOF
skipped, chromatic and grey zero-point corrections not applied, partial Gold
value-adds) are listed in Sect. II.1.1 of arXiv:2012.12825 [src]. The
authors recommend placing injection in the production software, as HSC did
with SynPipe and as planned for LSST [src: Sect. VI]. Rubin DP1 uses the
`source_injection` package of the LSST pipelines [src: arXiv:2603.23786,
Sect. V.8.2]. In DES Y6 Balrog and the shear-calibration image simulations
share one code base (Eastlake) for steps 1–8, which makes them identical in
image processing [src: arXiv:2501.05683, Sect. 3.4].

### Injection into real images or fully simulated images
<!-- key: injection-into-real-images-or-fully-simulated -->

DES Y6 keeps both: Balrog measures the transfer function in the real images
but lacks truth for the real sources already present, so it cannot replace
the image simulations used for shear and redshift-algorithm biases, which in
turn are not realistic enough to give the transfer function
[src: arXiv:2501.05683, Sect. 3.4]. SynPipe chose injection over a fully
generative simulation so that blends, bright-object proximity, bleed trails
and artefacts enter [src: arXiv:1705.01599, Sect. 3.1].

### Truth: model profiles, model of the survey's own fitter, or real stamps
<!-- key: truth-model-profiles-model-of-the-survey-s-own -->

- Model profiles from deep data (Balrog: bdf fits; SynPipe: single-Sérsic
  COSMOS fits from HST and 100,000 extreme-deconvolution resampled stars
  from 14,472 HST-classified stars) [src: arXiv:2012.12825, Sect. III.1;
  arXiv:1705.01599, Sect. 4.2]. SynPipe's galaxy sample (58,210 objects)
  lacks galaxies brighter than i = 20.5 [src: same].
- The survey's own model types (Obiwan injects Tractor models, so a
  noiseless injection is fitted perfectly) [src: arXiv:2007.08992,
  Sect. 3.1]. For DESI LRGs the Tractor ellipticity prior biases both the
  deep truth shapes and the remeasurement, so the truth shapes are
  de-biased first (Kong et al. 2024, arXiv:2405.16299) [src: Sect. 5.1].
- Real deep stamps: capability built in Balrog but not used, because of
  artefacts, masking, truncated neighbours and extra noise when injecting
  into exposures with better seeing than the deep co-add, and because
  "truth" is ill-defined for a stamp [src: arXiv:2012.12825, Sects. III.1,
  VI].

### Lattice or random positions; how dense
<!-- key: lattice-or-random-positions-how-dense -->

| Programme | Pattern | Spacing or density | Stated reason |
|---|---|---|---|
| Balrog SV | random, 1000 per ~0.5 deg² per realisation, 100 realisations per tile | ~as many injections as DES detections | keep injection–injection blends low [src: arXiv:1507.08336, Sect. 3.3] |
| Balrog Y3/Y6 | hexagonal lattice | 20″; ~7.8 arcmin⁻² | maximise density at low self-blending [src: arXiv:2012.12825, Sect. III.4] |
| Obiwan eBOSS ELG | random, injections within 5″ of another deferred to the next iteration | 3200 deg⁻² (3152 after deferral), 1.2M galaxies | only real–synthetic blends wanted [src: arXiv:2007.08992, Sects. 3.1, 5] |
| Obiwan DESI ELG | hexagonal | 37.728″ (144 pixels) per 0.25° brick | grid from the LRG run [src: arXiv:2411.12024, Sect. 5.1] |
| Obiwan DESI LRG | hexagonal | 94″ (360 pixels) | avoid blending in WISE images [src: arXiv:2405.16299, Sect. 5.2] |
| SynPipe | random | 1000 stars or 500 galaxies per CCD | enough useful objects without unrealistic crowding [src: arXiv:1705.01599, Sect. 4.2] |
| Rubin DP1 | input catalogue from DC2 | stars brighter than 17.5 and galaxies brighter than 15 or fainter than 26.5 (six-band total) excluded, half of the rest injected | avoid deblender failures from excess density [src: arXiv:2603.23786, Sect. V.6] |

High density has a cost for non-local deblenders: at the Y3 density nearly
all objects of a tile could join one MOF friends-of-friends group, which is
one reason MOF was skipped for the cosmology runs [src: arXiv:2012.12825,
Sect. III.4].

### Weighting the inputs toward the science sample
<!-- key: weighting-the-inputs-toward-the-science-sample -->

Y6 splits each tile's injections into five classes: one third unweighted
("Y3 scheme"), and four sixths weighted by w(m) = 1 − 1/(1 + exp[−4(m −
m_ref)]) (Eq. 3.3) with m_ref = 21.5 (clustering lenses) or 23.5 (shear
sources), each with or without a requirement of a COSMOS, PAUS or C3R2
redshift [src: arXiv:2501.05683, Sect. 3.2]. Usable injections rise by
factors of 12 (lens samples), 2.7 (shear samples) and 1.6 (the general
catalogue) relative to the Y3 scheme [src: same]. The unweighted third keeps
the full magnitude range, so a misplaced m_ref adds noise, not bias
[src: same].

### Forward-model weights, regression weights, or a hybrid
<!-- key: forward-model-weights-regression-weights-or-a -->

- eBOSS ELG (one chunk of four): Obiwan weights and the linear-regression
  w_sys give multipole differences of χ² = 1.26, 0.54, 0.31 for ℓ = 0, 2, 4
  above 24 h⁻¹ Mpc, after subtracting the regression's mode-removal measured
  on mocks; a residual trend with PSF size remains [src:
  arXiv:2007.08992, Sects. 5.3, 6].
- DESI DR1 ELG: Obiwan reproduces most trends once the DESI dust map
  replaces SFD in post-processing (Eq. 8), but leaves unexplained trends at
  E(B−V) = 0 and above 0.8 mag in the South; Obiwan-only weights leave
  χ² = 73.7 (North) and 107.7 (South) against stellar density for 10 d.o.f.,
  against 5.4 and 4.4 for the SYSNet weights [src: arXiv:2411.12024,
  Sects. 5.2, 7.1]. A hybrid (SYSNet on Obiwan, then SYSNet on the residual)
  gives 5.7 and 3.0, and total χ² over 12 maps of 90.2 against 111.6 (North)
  and 82.8 against 96.5 (South) for 120 d.o.f. [src: Sect. 7.2]. Motivation:
  regression over-corrects as its flexibility grows; the forward model does
  not, but only contains the physics put into it [src: Sect. 7].
- DESI LRG: Obiwan predicts the depth trends, including their dependence on
  intrinsic brightness, but not the extinction trends or a joint
  seeing–depth–brightness dependence [src: arXiv:2405.16299, abstract].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Deep-field input S/N | ~√10 × wide field | DES Y3 | arXiv:2012.12825 | Sect. III.1 |
| Input catalogue after cuts | 1.23M (main), 746k (aux) | DES Y3 | arXiv:2012.12825 | Sect. III.4 |
| Star fraction of injections | 10% to g = 27 | DES Y3 | arXiv:2012.12825 | Sect. III.4 |
| Lattice spacing; density | 20″; ~7.8 arcmin⁻² (~40% of Y3) | DES Y3, Y6 | arXiv:2012.12825; arXiv:2501.05683 | Sect. III.4; Sect. 3.2 |
| Match radius r₁; r₂ range | 0.5″; 0.5″–2.0″ | DES Y3 | arXiv:2012.12825 | Sect. III.5 |
| Ambiguous matches | < 1.5% | DES Y3 | arXiv:2012.12825 | Sect. III.5 |
| Real neighbour within 1.5″ | < 0.2%, removed | DES Y6 | arXiv:2501.05683 | Sect. 3.4 |
| Magnitude-response floor | ~3 mmag (fracdev prior mismatch) | DES Y3 | arXiv:2012.12825 | Sect. II.3 |
| Mean CPU per recovered injection | ~80 s, ~12× SV; 4–6 epochs | DES Y3 | arXiv:2012.12825 | Sect. VI |
| Tiles | ~2500 (Y3); 10,169 fiducial + 2000 magnified (Y6) | DES | arXiv:2501.05683 | Sect. 3.4 |
| Magnification step | δκ = 0.01 (~2% flux and area) | DES Y3, Y6 | arXiv:2012.12825; arXiv:2501.05683 | Sect. V.2; Sect. 3.3 |
| Balrog vs Gold S/N = 10 depth | g 24.14/24.16, r 23.82/23.84, i 23.26/23.28, z 22.61/22.62 | DES Y6 | arXiv:2501.05683 | Table 1 |
| Clustering systematic difference Balrog vs Gold | < 1% of galaxy C_ℓ at ℓ > 200, maglim-like 17.5 < i < 21.5 | DES Y3 | arXiv:2012.12825 | Sect. IV.1.4 |
| Balrog σ on mean z of source bins | < 10⁻³ | DES Y3 | arXiv:2012.12825 | Sect. V.1 |
| Balrog SV: per realisation; total CPU | 1000 objects per ~0.5 deg², 100 realisations; ~30,000 CPU h | DES SV | arXiv:1507.08336 | Sect. 3.3 |
| Obiwan eBOSS density; passing selection | 3200 deg⁻² injected; ~20% pass true-parameter selection; 20.4% pass after measurement | eBOSS ELG | arXiv:2007.08992 | Sect. 5 |
| Colour scatter across ELG box | ~0.25 mag | eBOSS ELG | arXiv:2007.08992 | Sect. 6 |
| Obiwan DESI ELG truth sample | dr9-COSMOS, ~10× exposures; colour box widened by 1.2 (g), 0.8 (g−r), 0.5 (r−z) mag | DESI DR1 | arXiv:2411.12024 | Sect. 5.1 |
| Obiwan DESI ELG cost | ~2166 node-hours (DR1 South remainder) | DESI DR1 | arXiv:2411.12024 | App. B |
| Obiwan DESI LRG | 15 million galaxies simulated | DESI | arXiv:2405.16299 | abstract |
| SynPipe cost | ~1.5 h (stars), ~3.0 h (galaxies) per tract per band on 108 cores; +3.5 h stack and measurement | HSC DR1 | arXiv:1705.01599 | Sect. 4.3 |
| SynPipe photometry | 1% (i ~ 19) and 6% (i ~ 25) for stars; 13% (i ~ 20) and 18% (i ~ 25) for CModel galaxies | HSC DR1 | arXiv:1705.01599 | abstract |
| Rubin DP1 misclassification | ~20% of objects at 80% completeness, mostly galaxies as stars | Rubin DP1 ECDFS | arXiv:2603.23786 | Sect. V.6 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Emulation differs from production.** Shows as offsets between injected
  and real catalogues that are not physical. Test: injection switched off
  must reproduce the production catalogue bit for bit with the same seeds
  [src: arXiv:2012.12825, Sect. II.3].
- **Truth defined in a different model from the measurement.** The fracdev
  prior mismatch produced a 7.5 mmag subgroup offset; the Tractor
  ellipticity prior applied twice biases shapes [src: arXiv:2012.12825,
  Sect. II.3; arXiv:2405.16299, Sect. 5.1]. Test: blank-image injections
  and morphology comparison of output with data.
- **Input not representative.** Balrog SV colours interpolated from COSMOS
  SEDs disagreed with Y1 Gold; Y3 deep-field inputs fixed most of it but
  bright PSF-like objects still differ [src: arXiv:2012.12825, Sect. VI].
  Test: compare magnitude, colour and size distributions of recovered
  injections with the data selected the same way.
- **Wrong extinction or survey-property map in the injection.** Obiwan run
  with SFD failed to predict the DESI ELG E(B−V) trend; corrected in
  post-processing with the DESI map [src: arXiv:2411.12024, Sect. 5.2]. For
  LRGs the residual extinction trend depends on which map is tested,
  implicating large-scale-structure contamination (CIB) of the maps
  [src: arXiv:2405.16299, abstract, Sect. 7.5].
- **Physics not in the simulation.** Obiwan leaves PSF-size residuals for
  eBOSS ELGs and seeing–depth–brightness residuals for DESI LRGs [src:
  arXiv:2007.08992, Sect. 6; arXiv:2405.16299, abstract]. Injection also
  cannot see PSF, background or detrending errors upstream of the injection
  point [src: arXiv:2012.12825, Sect. II.1.1; arXiv:1705.01599, Sect. 3.3].
- **Matching choices hidden in the catalogue.** Brightness-ordered or
  proximity-flagged matches change outlier tails; keep full remeasured
  catalogues and state the rule [src: arXiv:2012.12825, Sect. III.5].
- **Too few injections for the use.** Y3 covered 20% of the footprint in one
  realisation; direct calibration of clustering would need more injections
  than galaxies, and shear-blending calibration over a dozen y3-deep runs
  [src: arXiv:2012.12825, Sect. VI].
- **Pixel weights that ignore brightness.** A single weight per pixel
  over-corrects bright and under-corrects faint galaxies; injections can
  supply magnitude-dependent randoms [src: arXiv:2405.16299, Sect. 7.5].
- **Null test with the injections.** DES Y3: cross-correlation of weighted
  lens samples with their Balrog samples over ~1000 deg² consistent with
  zero, ≤ 5% of the auto-correlation in the five lowest angular bins and
  < 10% below ~30′ [src: arXiv:2105.13540, Sect. 8.5].

## Reading list
<!-- key: reading-list -->

- Foundation: Suchyta et al. 2016, arXiv:1507.08336 — Balrog introduced,
  association-mode measurement, injections as randoms.
- Method: Huang et al. 2018, arXiv:1705.01599 — SynPipe design choices and
  their limits inside the HSC stack.
- Method: Everett et al. 2022, arXiv:2012.12825 — the reference for a
  single-epoch injection run: emulation, truth, lattice, matching,
  validation ladder, uses, limitations.
- Application: Anbajagane et al. 2025, arXiv:2501.05683 — full-footprint
  run, weighted inputs, conservative blend flag, depth and null tests.
- Application: Kong et al. 2020, arXiv:2007.08992 — Obiwan weights replace
  regression weights for eBOSS ELGs.
- Test: Rosado-Marín et al. 2024, arXiv:2411.12024 — where Obiwan fails for
  DESI ELGs and the hybrid with regression; radial selection from
  injections.
- Critique: Kong et al. 2024, arXiv:2405.16299 — LRG trends not reproduced;
  why per-pixel weights are incomplete.
- Application: Rodríguez-Monroy et al. 2022, arXiv:2105.13540, Sect. 8.5 —
  injection cross-correlation as a weight null test.
- Application: Rubin DP1, arXiv:2603.23786, Sects. V.6, V.8.2 — co-add and
  difference-image injection with the LSST `source_injection` package.

## Not verified
<!-- key: not-verified -->

- Obiwan method paper (Burleigh 2018, cited as a thesis) not read.
- Euclid and KiDS injection practice not read; KiDS calibrates with image
  simulations (see `cosmo-weak-lensing`), not covered here.
- Balrog Y3 Table 2 (runtime per stage) and Appendix A configuration not
  read.
- DES Y6 magnification coefficients derived from the Balrog runs: the
  analysis paper was found by search but not read.
