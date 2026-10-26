# Cross-survey coordination: overlaps, shared ground data and joint processing — cosmo-surveys-facilities dossier

Scope: what each wide survey needs from the others and at which
specification, how overlaps were negotiated and why the footprints and
deep fields sit where they do, how external imaging is ingested into
another survey's pipeline, what joint pixel-level processing and same-sky
cross-correlations have been shown to gain (and what they cost), and how
the follow-up spectroscopy is shared, as read in the Euclid overview, the
Rubin–Euclid derived-data-products report, the LSST–Euclid synergy paper,
the Roman time-allocation report, the UNIONS overview, the Snowmass
report and the shape-measurement and same-sky forecast papers.
Snapshot: 2026-10-18.
From: Snowmass CF6 (arXiv:2209.08654), Sect. 5; Euclid overview
(arXiv:2405.13491), Sects. 4.4–4.5.

Already in L2 or another dossier, not repeated here: UNIONS depths and the
Euclid PSF-colour need in `surveys-and-data.md#imaging-surveys` and
`systematics.md#point-spread-function`; the Roman HLWAS tiers and the
committee's reasons for the wide tier (Rubin and DESI overlap, overlap with
Euclid) in `deep/footprint-tiling-depth.md`; the SO LAT sky-fraction trade
for LSST and DESI overlap in `deep/survey-forecasts.md` ("Area or overlap
for a CMB survey"); Rubin deep-drilling budgets, the Euclid Deep Field
South (EDFS) recommendation and TiDES host redshifts in
`deep/cadence-time-domain.md`. Photometric-redshift calibration methods
(SOM, clustering redshifts) are in `cosmo-photometry-photoz`; the 6×2pt
analyses themselves in `cosmo-cmb-lss-cross-correlations`; deblending
algorithms in `cosmo-data-pipelines`.

Notation. EWS, EDS: Euclid Wide and Deep Surveys; EDF-N, EDF-F, EDF-S:
Euclid Deep Fields North, Fornax, South; WFD: Rubin's wide-fast-deep
survey; DDF: Rubin deep-drilling field; DDP: Rubin–Euclid derived data
product; SEF: single-epoch frame (a detrended, calibrated CCD image with
its PSF model and catalogue); n_eff: effective number density of galaxies
for lensing; σ_SN: intrinsic shape noise; δε: per-galaxy ellipticity
measurement error; FoM: dark-energy figure of merit.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Write down what each survey needs from the others
<!-- key: step-1-write-down-what-each-survey-needs-from -->

The dependencies are asymmetric and stated as requirements.

- **Euclid needs ground ugriz.** Euclid relies on optical ground-based
  imaging for photometric redshifts and "to assign the correct SED-weighted
  PSF to each galaxy in the lensing analysis" [src: arXiv:2405.13491,
  Sect. 4.4]. Its VIS band is "of limited use for the photometric
  redshifts"; a full g, r, i, z set is "critical", and u improves low-z
  photo-z [src: arXiv:1710.08489, Sect. IV.4.2]. Euclid requires
  σ_z/(1 + z) < 0.05 [src: arXiv:2503.13783, Sect. II.1.4].
- **At which depth.** The average requirement for the ground complement,
  5σ point-source PSF magnitudes, is u 25.4, g 25.6, r 25.3, i 25.3,
  z 24.9; LSST reaches it in 23, 4, 5, 11, 13 visits, 56 in all, about
  28 min of integration or 37 min with overheads, i.e. about 10 months of
  uniform WFD progress for griz and four years for u [src: arXiv:1710.08489,
  Table 1, Sect. IV.4.2]. Because Euclid's zodiacal background varies by
  more than 1.2 mag between ecliptic poles and plane at fixed exposure, the
  ground data "should as much as possible match the space data depth or
  anchor on its deepest part" [src: same].
- **At which uniformity.** The ingested ground data must give 1%
  single-filter photometric homogeneity over the whole EWS and sub-percent
  colour homogeneity over the VIS field of view, from three surveys
  (UNIONS, DES, LSST) on five telescopes with different filters and more
  than 450 detectors [src: arXiv:2405.13491, Sect. 7.3].
- **Roman needs Rubin and spectra.** The HLWAS "will require optical
  photometry from Rubin, as well as ground-based calibration spectroscopy
  within the deep fields"; the HLTDS needs Rubin DDF SNe Ia at z ~ 0.5 and
  a low-z Hubble-flow sample [src: arXiv:2505.10574, Sect. VI.2]. The
  committee assumed that all ancillary data needed for core requirements
  would be public, and did not count data that only improve Roman science
  [src: same].
- **Every photometric survey needs spectra.** Euclid's baseline is direct
  calibration of the colour–redshift relation: a SOM of galaxy colours
  showed regions without secure redshifts, which motivated C3R2 (Keck,
  VLT, LBT) to i = 25; more than 5100 Keck spectra plus over 600 from the
  other telescopes raised the colour-space coverage from about 51% to more
  than 90%, the empty cells being low-density ones [src: arXiv:2405.13491,
  Sect. 4.5, Fig. 19 caption].

### Step 2. Negotiate the overlap in area and in time
<!-- key: step-2-negotiate-the-overlap-in-area-and-in-time -->

Each survey's footprint is fixed by its own constraints first, and the
overlap is what is left to negotiate.

- **Euclid's footprint.** Stellar contamination and Galactic stray light,
  reddening at fixed exposure time and zodiacal background exclude low
  Galactic latitude, dusty sky and the ecliptic; the area is defined as |b|
  > 25°, |β| > 15° and E(B − V) < 0.08 (up to 0.15 to avoid holes)
  [src: arXiv:1710.08489, Sect. IV.4.1]. The DDP report quotes 17,400 deg²
  compatible with the requirements, of which the six-year baseline covers
  the required 15,000 deg² [src: arXiv:2201.03862, Sect. 6, Fig. 2
  caption]; the current survey area is in L2.
- **Rubin's footprint.** The original WFD (18,000 deg², +2° to −62°) was
  set so that weak-lensing data are taken at airmass below 1.4 [src:
  arXiv:1710.08489, Sect. IV.4.1]. DESC asked for a footprint bounded by a
  dust-extinction cut; the Tri-Agency task force endorsed it because a WFD
  from +12.5° to −70° creates "up to a 9400 deg² of overlap" with Euclid
  and helps northern follow-up (Keck, DESI, PFS) [src: arXiv:2201.03862,
  Sect. 6]. A northern g, r, i (plus z) mini-survey would add 2600 deg²,
  bringing the possible overlap to 12,500 deg² [src: same].
- **Why the overlap numbers differ.** Rhodes et al. estimated nearly
  11,000 deg² with a 3000 deg² extension to +30°, needing 43 visits per
  field without u, about 222 h (27 nights) [src: arXiv:1710.08489,
  Sect. IV.4.1]; DESC simulations gave 8202 deg² (baseline) and 9332 deg²
  (dust-cut footprint) of Euclid overlap [src: arXiv:2104.05676, Table 4];
  the Euclid overview quotes 7534 deg² of the EWS overlapped by LSST
  [src: arXiv:2405.13491, Sect. 4.4]. They describe different footprint
  versions and definitions; quote the one of the strategy analysed.
- **Filling the gaps.** In the north, KiDS and HSC lacked area and lay near
  the ecliptic, and the Legacy Surveys were "one magnitude too shallow", so
  UNIONS was set up in 2017 to cover 5711 deg² of the northern EWS, joining
  LSST at +15° in the north Galactic cap; DES covers about 3750 deg² of the
  EWS in the south, enough for DR1 [src: arXiv:2405.13491, Sect. 4.4]. The
  north Galactic cap is "the highest quality sky for Euclid" (low
  zodiacal light, stellar density, extinction and cirrus) [src:
  arXiv:2503.13783, abstract].
- **Time.** Euclid prioritised the southern sky in its first year while
  UNIONS kept observing, to balance north and south by DR2, because the
  space and ground footprints must overlap "at every Euclid data release"
  [src: arXiv:2405.13491, Sect. 4.4]. DDP recommendation REC-11-SO asks to
  maximise wide overlap and to align Rubin's rolling cadence on the
  mini-surveys with Euclid's increasing-declination strategy [src:
  arXiv:2201.03862, Sect. 6].
- **Deep fields.** EDF-F (10 deg²) was chosen to match the CDF-S DDF. EDF-S
  (23 deg²) was given a stadium shape to minimise the Rubin time needed for
  20 contiguous deg² at uniform depth; two half-speed DDF pointings would
  have left less than 20 deg² at depth, while a custom translational dither
  reaches the Euclid depth over 21.6 deg²; transient science is "affected
  but not undermined" [src: arXiv:2201.03862, Sect. 6, Fig. 3 caption].
  Euclid visits EDF-F and EDF-S for 5–6 days every six months from its
  second year [src: same].

### Step 3. Ingest the other survey's pixels
<!-- key: step-3-ingest-the-other-survey-s-pixels -->

Euclid shows the procedure for a space survey that depends on ground data.

1. **Common input.** Every external survey delivers SEFs under one data
   model; they are produced with the external survey's own software
   (Pan-STARRS for i, HSCpipe for WHIGS and WISHES g and z, MegaPipe for
   CFHT u and r), while DES and other DECam data are reprocessed by Euclid
   with DES-derived pipelines; LSST products arrive through the joint
   Euclid–Rubin working group under a collaboration agreement [src:
   arXiv:2405.13491, Sect. 7.3].
2. **Recalibration.** Euclid's external-data unit does not redo detrending
   or astrometry but redoes the photometric calibration with Gaia: colour
   terms from G, BP, RP in a first phase, then synthetic photometry from
   Gaia DR3 spectra as in-field standards, bootstrapped to a denser
   catalogue [src: arXiv:2503.13783, Sect. V]. Gaia is used because its
   photometry is stable across the sky to about 2 mmag [src:
   arXiv:2405.13491, Sect. 7.3].
3. **Coadds and PSF.** The SEFs are stacked (SWarp) with a dedicated PSF
   model that combines the position-dependent PSFs of all inputs [src:
   arXiv:2405.13491, Sect. 7.3].
4. **Merge.** Forced photometry with SourceXtractor++ and TPHOT uses the
   Euclid images as a prior, because Euclid resolves sources merged in the
   ground data; the catalogue is "optimized specifically for Euclid", and
   each release contains ground data only over the Euclid footprint of
   that release [src: arXiv:2503.13783, Sect. V]. The products are
   therefore not the UNIONS products, a distinction the UNIONS paper makes
   explicitly [src: same].

### Step 4. Decide the level at which data are combined
<!-- key: step-4-decide-the-level-at-which-data-are -->

The DDP report ranks combinations from catalogue matching to joint pixel
fitting [src: arXiv:2201.03862, Sect. 5]: list-driven multi-band
catalogues (tier T1), forced photometry from joint pixel processing (T2),
deblended photometry from joint pixel processing (T3, "the most complex
approach"), and image cut-outs for transients (T0). Its two most
impactful cross-cutting products are the multi-band catalogues (for photo-z)
and the exchange of image stamps (transients, strong lensing, dropouts)
[src: Executive Summary]. Transient products should come within about
24 h; complex ones with the annual Rubin releases [src: same].

Data rights shape the products: a DDP matching only sources above 5σ in
VIS and NISP protects Rubin's depth advantage, and exporting only isolated
or deblended Rubin sources protects Euclid's resolution advantage; joint
models that infringe either can be withheld or degraded [src: DDP
definition; REC-7-CC].

### Step 5. Quantify the gain before paying for it
<!-- key: step-5-quantify-the-gain-before-paying-for-it -->

The joint-processing gain is measured on image simulations of both
surveys with the same galaxies, comparing four analyses: each survey
alone, a catalogue-level combination, and a joint fit to both sets of
pixels [src: arXiv:1901.08586, abstract]. The figure of merit is

    n_eff = (1/Ω) Σ_j σ²_SN / [(δε_j)² + σ²_SN]

(Schuhmann et al. 2019, arXiv:1901.08586, Eq. 11; Ω the survey area),
which counts perfectly measured galaxies of equal statistical power; it
measures precision, not accuracy [src: Sect. 2.4]. The catalogue-level
combination weights each galaxy's ellipticity by its inverse measurement
variance,

    ε^Comb = [(σ_ε^LSST)⁻² ε^LSST + (σ_ε^Euclid)⁻² ε^Euclid] /
             [(σ_ε^LSST)⁻² + (σ_ε^Euclid)⁻²]

(Zhang et al. 2025, arXiv:2506.22658, Eq. 8, with σ_ε the
bias-corrected uncertainty), assuming independent measurement errors but
not independent intrinsic shapes [src: Eq. 9 and text]. Zhang et al.
distinguish a "joint" catalogue (detected in both surveys) from a
"combined" one (detected in either) [src: Sect. 6.1].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Catalogue-level or joint pixel-level combination
<!-- key: catalogue-level-or-joint-pixel-level-combination -->

- **Isolated galaxies.** On over one million simulated isolated galaxies
  to i = 25.2, a joint-pixel fit shrinks ellipticity errors by a factor
  2.32 on average against LSST alone (most for small galaxies) and 1.55
  against Euclid alone (most for faint ones); n_eff rises by about 50% at
  i ~ 24.5–25 against either survey alone [src: arXiv:1901.08586,
  abstract, Sect. 4]. Against a catalogue-level combination the joint fit
  is up to 20% more precise where neither survey measures well, but this
  gives only about 5% in n_eff because shape noise dominates [src: same].
  The authors call this the minimum gain, since deblending, star–galaxy
  separation and PSF modelling were left out [src: Sect. 4].
- **With blending.** With randomly placed galaxies to magnitude 27.5,
  blending biases shear "particularly in LSST-like data" because of its
  larger PSF; combining all galaxies detected in either survey gives
  n_eff = 44.08 arcmin⁻², against 39.17 (LSST-like) and 30.31
  (Euclid-like), over 20.0–27.5 mag; the joint-object catalogue gains
  about 12% over either survey [src: arXiv:2506.22658, abstract]. Joint
  detection density for 20.0–25.2 mag drops from 33.95 arcmin⁻² on a grid
  to 32.25 arcmin⁻² with random positions [src: Sect. 3]. The authors
  find the joint-object approach suboptimal at catalogue level and leave
  the pixel-level version with blending to future work [src: abstract].
- **Joint deblending.** A scarlet extension that resamples and convolves
  one model into each instrument's frame reduces interpolation errors by
  an order of magnitude or more against GalSim defaults and gives galaxy
  models up to an order of magnitude more accurate than separate modelling,
  over a range of blending levels [src: arXiv:2107.06984, abstract].
- **Chromatic effects.** Pixel-level VIS morphology could improve Rubin's
  differential-chromatic-refraction model by a factor of about 2 [src:
  arXiv:2201.03862, Executive Summary].
- **Cost.** A joint survey processing effort for Euclid, Rubin and Roman
  was scoped at about 200 work-years [src: arXiv:2008.10663, abstract];
  the DDP report recommends developing joint detection and deblending on a
  small area at full depth, with pixels openly shared, EDF-S being the
  candidate (REC-13-SO) [src: arXiv:2201.03862, Sect. 6, REC-7-CC].

### Same sky or different sky for spectroscopy and lensing
<!-- key: same-sky-or-different-sky-for-spectroscopy-and -->

The forecasts disagree on how much overlap buys, and the reasons are in
the abstracts.

- Kirk et al. found a same-sky improvement factor of nearly 4 for dark
  energy and more than 2 for modified gravity over non-overlapping surveys
  (**forecast**), but warn that the factors "can be radically affected by
  a range of forecasts assumption" [src: arXiv:1307.8062, abstract].
- De Putter et al., with statistical errors only and angular and 3D
  two-point information, found the FoM of overlapping surveys "at most
  ~20% better" than disjoint ones, because only a small fraction of the
  modes enters the cross-correlations (**forecast**) [src: arXiv:1308.6070,
  abstract].
- Eriksen and Gaztañaga found, "contrary to some findings in the recent
  literature", important benefits, traced in equal parts to additional
  observables and to sample-variance cancellation; overlap helps by
  decorrelating cosmological from nuisance parameters and correlating the
  nuisance parameters (e.g. bias) of the two samples (**forecast**) [src:
  arXiv:1412.8429, abstract].
- Cai and Bernstein found overlapping lensing and redshift surveys
  equivalent, for the growth index γ, to separated surveys 1.5–2 times
  larger, the gain peaking for spectroscopic mass thresholds of
  10¹³–10¹⁴ h⁻¹ M_⊙ (LRG-like) and shrinking for very deep or very shallow
  spectroscopy (**forecast**) [src: arXiv:1112.4478, abstract].

What to check: whether the forecast includes sample-variance cancellation
in a 3D × 2D covariance and nuisance parameters; the de Putter et al.
result of at most about 20% (arXiv:1308.6070) [src: abstract] is for
statistical errors only, and the large factors depend on the nuisance
model.

### Sharing photometry for photo-z
<!-- key: sharing-photometry-for-photo-z -->

Rhodes et al. compared the lensing signal-to-noise of Euclid and LSST
auto- and cross-spectra with and without shared photometry, for 7000 and
11,000 deg² of overlap and a fraction f_E = 0.75 or 1 of Euclid sources
also usable in LSST, and found the boost "can be quite large even under
the most conservative assumptions", while warning that systematics and
intrinsic alignments were ignored and that an S/N gain does not translate
directly into parameter gains [src: arXiv:1710.08489, Sect. IV.3,
Fig. 5 caption]. No quantitative factor is given in the text.

### CMB overlap
<!-- key: cmb-overlap -->

The Euclid overview quotes, from a 7×2pt study with SO and CMB-S4,
statistical gains of a factor 2–3, and above 10 for some extended models
(**forecast**) [src: arXiv:2405.13491, Sect. 9.4; primary paper not
read]. CMB lensing cross-correlations are free of additive biases, which
is why they help marginalise over systematics [src: same]. The Roman
committee rejected a southern wide-tier extension aimed partly at overlap
with the South Pole Telescope as of insufficiently broad impact [src:
arXiv:2505.10574, Sect. III.1].

### Shared time-domain resources
<!-- key: shared-time-domain-resources -->

Combining LSST and Roman SN Ia samples improves the FoM by up to a factor
2 over independent analyses (**forecast**) [src: arXiv:2104.01199,
Sect. II]. The shared bottleneck is host redshifts: DESC baselined host
redshifts with 4MOST, but 4MOST will not reach the DDF depth where most
DESC SN cosmology is done; Roman has 100 Subaru nights for PFS north of
−30°, and simulations show the Roman SN programme alone could use more
than 100 nights [src: same]. The same paper asks for coordinated deep-field
location, timing, season length and filters, an all-sky network of
SI-traceable standards, shared SN position lists for forced photometry and
source injection on real images [src: same]. A prototype now matches
alerts (ZTF as a proxy for Rubin) to Euclid images, giving joint light
curves and cut-outs; one SN was found in Euclid data about 3 days before
its ground detection [src: arXiv:2602.18173, abstract].

### Agreements or public data
<!-- key: agreements-or-public-data -->

Cross-survey analyses have waited for public data, delaying results, or
run under memoranda of understanding with "additional bureaucratic
hurdles"; Snowmass proposed coordinated overlap, joint processing,
coordinated blinding, joint simulations and dedicated funding [src:
arXiv:2209.08654, Sect. 5.1]. Euclid uses a collaboration agreement for
LSST products and public data for DES [src: arXiv:2405.13491, Sect. 7.3].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Ground depth needed by Euclid (5σ PSF) | u 25.4, g 25.6, r 25.3, i 25.3, z 24.9 | Euclid | arXiv:1710.08489 | Table 1 |
| LSST visits to Euclid depth | 23/4/5/11/13 (ugriz), 56 total, ~37 min | LSST–Euclid | arXiv:1710.08489 | Table 1, Sect. IV.4.2 |
| Euclid photo-z requirement | σ_z/(1 + z) < 0.05 | Euclid | arXiv:2503.13783 | Sect. II.1.4 |
| Ground photometric homogeneity | 1% per filter over EWS; sub-percent colour over VIS field | Euclid | arXiv:2405.13491 | Sect. 7.3 |
| DES area in EWS | ~3750 deg² | Euclid | arXiv:2405.13491 | Sect. 4.4 |
| UNIONS area in EWS | 5711 deg², joins LSST at +15° | Euclid | arXiv:2405.13491 | Sect. 4.4 |
| LSST–EWS overlap | 7534 deg² | Euclid | arXiv:2405.13491 | Sect. 4.4 |
| LSST–Euclid overlap, strategy variants | 8202 (baseline), 9332 (dust cut) deg² | DESC | arXiv:2104.05676 | Table 4 |
| LSST overlap with 4MOST, DESI | 14,421 / 4179 (baseline); 14,925 / 5951 (dust cut) deg² | DESC | arXiv:2104.05676 | Table 4 |
| Possible Rubin–Euclid overlap | 9400 deg² (extended WFD); 12,500 with northern mini-survey | DDP report | arXiv:2201.03862 | Sect. 6 |
| EDF-S at Rubin depth | 21.6 of 23 deg² with custom dithers | DDP report | arXiv:2201.03862 | Fig. 3 caption |
| C3R2 spectra | > 5100 (Keck) + > 600; coverage 51% → > 90% | Euclid | arXiv:2405.13491 | Sect. 4.5 |
| Joint-pixel shape error | ×2.32 vs LSST, ×1.55 vs Euclid; n_eff +50% at i ~ 24.5–25 | isolated galaxies | arXiv:1901.08586 | abstract, Sect. 4 |
| Joint-pixel vs catalogue | ≤ 20% precision; ~5% n_eff | isolated galaxies | arXiv:1901.08586 | Sect. 4 |
| n_eff with blending, 20–27.5 mag | 44.08 combined; 39.17 LSST-like; 30.31 Euclid-like (arcmin⁻²) | simulations | arXiv:2506.22658 | abstract |
| DCR model improvement from VIS | ≈ 2 | DDP report | arXiv:2201.03862 | Executive Summary |
| Joint survey processing cost | ~200 work-years | JSP report | arXiv:2008.10663 | abstract |
| Same-sky gain | ~4 (DE), > 2 (MG) / ≤ 20% FoM (**forecast**) | Kirk / de Putter | arXiv:1307.8062; arXiv:1308.6070 | abstract of each |
| LSST + Roman SN FoM | up to ×2 (**forecast**) | SN community | arXiv:2104.01199 | Sect. II |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Overlap quoted from the wrong footprint.** The Rubin–Euclid overlap
  is 7534 deg² in the Euclid overview (arXiv:2405.13491) [src: Sect. 4.4]
  and 12,500 deg² for an extended WFD with a northern mini-survey in the
  DDP report (arXiv:2201.03862) [src: Sect. 6]; each belongs to its
  footprint version (Step 2).
  Test: name the Rubin strategy version and the Euclid release footprint.
- **Ground data shallower than space data where it matters.** Euclid depth
  varies with zodiacal light; matching the average leaves the deepest
  Euclid regions under-served [src: arXiv:1710.08489, Sect. IV.4.2].
  Test: compare ground and space depth maps, not survey averages.
- **Heterogeneous ground calibration.** Five telescopes and different
  filters must reach 1% homogeneity [src: arXiv:2405.13491, Sect. 7.3].
  Test: calibration residuals against Gaia per survey and across the
  UNIONS–LSST and DES–LSST boundaries.
- **Release-dependent overlap.** Each Euclid release includes ground data
  only over its own footprint [src: arXiv:2503.13783, Sect. V]; an early
  release can have uneven north–south ground coverage [src:
  arXiv:2405.13491, Sect. 4.4]. Test: the ground-coverage mask of the
  release used.
- **Joint-processing gains from idealised simulations.** The 50% result
  assumes isolated galaxies, round Gaussian PSFs and perfect registration
  [src: arXiv:1901.08586, Sect. 4]; blending reduces detections and biases
  shear, mostly in the ground data [src: arXiv:2506.22658, Sect. 3,
  abstract]. Test: a forecast that claims a joint gain should include
  blending and realistic PSFs.
- **Confusing products.** Euclid's products from UNIONS pixels differ from
  UNIONS's own catalogues [src: arXiv:2503.13783, Sect. V]. Test: cite
  which pipeline produced the photometry.
- **Same-sky factor out of context.** The same-sky factors of different
  papers come from different covariance and nuisance treatments (Choices). Test: state the
  forecast assumptions next to the factor.
- **Assumed follow-up.** Host redshifts for DDF SNe exceed what 4MOST
  reaches and what Roman's Subaru time covers [src: arXiv:2104.01199,
  Sect. II]. Test: tie the forecast to a named programme with its depth.
- **Timeline mismatch.** Decisions fall due at different times in each
  project, a "key obstacle" to coordination [src: arXiv:2104.01199,
  Sect. II]; aligning DDF visits with Euclid is "particularly important and
  challenging" [src: arXiv:2104.05676, Sect. VI.3].

## Reading list
<!-- key: reading-list -->

- Review: Flaugher et al. 2022, arXiv:2209.08654 — Sect. 5, the case and
  the organisational obstacles for cross-survey analyses.
- Foundation: Rhodes et al. 2017, arXiv:1710.08489 — what Euclid needs
  from LSST, visits and time, overlap geometry, photo-z S/N example.
- Method: Guy et al. 2022, arXiv:2201.03862 — DDP tiers, data-rights
  rules, EDF-S design, overlap recommendations.
- Application: Euclid Collaboration 2025, arXiv:2405.13491 — Sects. 4.4,
  4.5 and 7.3, the ground-data campaign and its ingestion.
- Application: Gwyn et al. 2025, arXiv:2503.13783 — Sect. V, how a ground
  survey's pixels become another survey's product.
- Method: Schuhmann et al. 2019, arXiv:1901.08586 — joint-pixel shape
  measurement and the n_eff metric.
- Critique: Zhang et al. 2025, arXiv:2506.22658 — joint shear with
  blending; catalogue-level gains.
- Method: Joseph et al. 2021, arXiv:2107.06984 — joint resampling and
  convolution for deblending.
- Critique: de Putter et al. 2013, arXiv:1308.6070, against Kirk et al.
  2013, arXiv:1307.8062, and Eriksen and Gaztañaga 2014, arXiv:1412.8429 —
  how much overlap is worth.
- Application: Rose et al. 2021, arXiv:2104.01199 — SN-specific
  coordination: calibration, host redshifts, deep fields.

## Not verified
<!-- key: not-verified -->

- The Euclid–SO–CMB-S4 7×2pt forecast (Ilić et al. 2022) is quoted from
  the Euclid overview; the primary paper was not read.
- The body of the JSP final report (arXiv:2008.10663 has no HTML
  rendering): only the cost in the abstract was read.
- The Tri-Agency Survey Coordination Task Force note (Cuillandre et al.
  2021) and the Rubin–Euclid collaboration agreement: cited in the papers
  read, not found as arXiv documents.
- The current Rubin baseline's overlap with Euclid, DESI and 4MOST after
  the survey start; the DESI–Euclid and 4MOST–Euclid spectroscopic
  coordination; CSST overlap plans.
- Roman HLWAS footprint coordinates and the Definition Committee reasons
  (Appendix C of arXiv:2505.10574 is not rendered).
