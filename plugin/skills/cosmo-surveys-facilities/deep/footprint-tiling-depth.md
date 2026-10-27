# Footprint, tiling and the depth-versus-area trade — cosmo-surveys-facilities dossier

Scope: how a wide survey's region, tiles, passes, dithers, exposure depth
and time budget are designed and checked against simulations, and what each
choice (depth against area, layered against single-tier, depth-first,
fixed against target-driven tiling, rolling cadence) costs, as read in the
survey-definition and operations papers of Euclid, DESI, Rubin, HSC, 4MOST
and Roman.
Snapshot: 2026-10-17.
From: Euclid overview (arXiv:2405.13491), Sect. 4.1 and Sect. 5.5; DESI
survey operations (arXiv:2306.06309); Bianco et al. 2022 Rubin cadence
review (arXiv:2108.01683), Sect. V.

Already in L2, not repeated here: etendue and survey-speed scaling in
`physics-and-methods.md#imaging`; DESI nightly scheduling and the 7% speed
gain in `physics-and-methods.md#completeness-and-fibre-assignment`; dynamic
exposure times in `physics-and-methods.md#uniformity-and-calibration-as-specifications`;
Rubin, HSC and Roman tier depths and areas in `surveys-and-data.md#imaging-surveys`
and `surveys-and-data.md#roman-2-4-m-space-telescope-l2-slitless`; the
Rubin strategy finding of Lochner et al. in
`physics-and-methods.md#cadence-and-time-domain-strategy`.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Draw the region of interest
<!-- key: step-1-draw-the-region-of-interest -->

The footprint starts as a region where the core probes meet their depth and
contamination requirements; the survey is then built inside it.

- **Euclid.** The region of interest (RoI) is set by zodiacal background,
  Galactic extinction and stray light from Galactic stars; cirrus was
  ignored as at least five magnitudes fainter than the total background
  over most of the RoI [src: arXiv:2108.01201, Sect. 5.2.1]. Its outline
  excludes |β| ≤ 10° (ecliptic latitude) and |b| ≤ 23° (Galactic latitude),
  with |b| ≤ 25° excluded at δ ≥ +30° because the northern ground surveys
  were started in 2017 on the Red Book value [src: Sect. 5.2.1, LaTeX
  source]. The Red Book limit E(B−V) = 0.08 mag, applied rigidly, gave
  convoluted contours and holes, so 0.09 mag was adopted with local
  excursions to 0.17 mag; the median over the RoI is 0.037 mag [src:
  Sect. 5.1.2]. Result: 17,354 deg² in four pieces (northern and southern
  "mainlands" of 7142 and 6937 deg², "islands" of 1575 and 1700 deg²),
  from which any 15,000 deg² could form the wide survey [src: Table 6].
- **DESI.** The goal is "a large, contiguous region that could be
  efficiently observed for extragalactic targets as part of a year-round
  survey from Kitt Peak" [src: arXiv:2306.06309, Sect. III]. Footprint:
  inside Legacy Surveys DR9; −18° < δ < 77.7°; b > 0° or δ < 32.2° (the
  south Galactic cap north of 32° had no Legacy imaging); |b| > 22° for
  −90° < l < 90°, otherwise |b| > 20° [src: Sect. III]. No explicit
  extinction cut: the imaging survey had already avoided high E(B−V) [src].
- **HSC.** Wide fields along the celestial equator, observable from both
  hemispheres, spread in right ascension so that some field is reachable
  all year, low in extinction, in three contiguous regions "to enable
  cosmological analyses on large scales", and placed on SDSS and Pan-STARRS1
  for first-order calibration and on ACT, XXL, VIKING and spectroscopic
  fields for synergy [src: arXiv:1704.05858, Sects. 3.1, 3.1.1].
- **Rubin (strategy studies).** The effective cosmology area is the area
  with E(B−V) < 0.2, chosen because dust properties change near that value,
  and with i-band coadded 5σ point-source depth above 24.65, 25.25, 25.62
  and 25.9 after years 1, 3, 6 and 10; the year-10 cut follows the SRD
  "gold sample" goal i < 25.3 [src: arXiv:2104.05676, Sect. III.1].

### Step 2. Fix the unit observation
<!-- key: step-2-fix-the-unit-observation -->

The unit observation sets depth per visit, overheads and therefore the area
reachable per day.

- **Euclid reference observation sequence (ROS).** Four dithered pointings
  per field over the 0.53 deg² common field; at each pointing a VIS image and
  a simultaneous red-grism exposure of about 570 s, then three NISP images
  of 112 s; dither slews of 66 s; grisms used at two angles each offset by
  4° to decontaminate overlapping spectra [src: arXiv:2108.01201,
  Sect. 4.1]. Total 4214 s, 4396 s with the mean 182 s field slew, under
  the 4400 s system-level budget [src].
- **LSST visit.** With two visits per night, the mean revisit time is
  n = (t_vis/10 s)(A_sky/10,000 deg²)(10 deg²/A_FOV) days (Eq. 1), the
  number of visits N_visit = (3000/n)(T/10 yr) (Eq. 2), and the efficiency
  ε = t_vis/(t_vis + 9 s) (Eq. 3) [src: arXiv:0805.2366, Sect. II.2.2].
  Here t_vis is the visit exposure time, A_sky the area covered, A_FOV the
  field area and T the survey length. n < 4 days and N_visit > 800 require
  t_vis < 40 s; efficiency losses below about 30% require t_vis > 20 s;
  the adopted 2 × 15 s visit gives ε = 77% [src].
- **DESI effective time.** Depth is expressed as the time needed to reach a
  goal uncertainty in nominal conditions (1.1″ seeing, r-band sky of 21.07
  mag arcsec⁻², photometric, zenith, no dust), weighted over wavelength to
  track redshift success; dark tiles aim for 1000 s, bright for 180 s,
  backup for 60 s [src: arXiv:2306.06309, Sect. V.2, Table 8]. Fiducial
  sources: an exponential profile of 0.45″ half-light radius with an LRG
  spectrum (dark) and a de Vaucouleurs profile of 1.5″ with a BGS spectrum
  (bright) [src: Table 1].
- **HSC.** Wide layer: 10 min (g, r) or 20 min (i, z, y) split into four
  or six visits, separated by more than half an hour to sample independent
  atmospheres, plus one 30 s exposure per field and filter for unsaturated
  calibration stars [src: arXiv:1704.05858, Table 4, Sect. 3.3].

### Step 3. Lay out tiles and passes
<!-- key: step-3-lay-out-tiles-and-passes -->

- **Euclid.** A tile is the largest latitude–longitude rectangle inside one
  field; tiles are laid along parallels with a 1% overlap to absorb
  pointing error, the number per row falling with latitude [src:
  arXiv:2108.01201, Sect. 7.3.1]. Above about 79° latitude adjacent tiles
  sit more than 3.6° apart in longitude and cannot be reached by a sideways
  small slew, so the polar caps use a separate tiling [src: Sect. 7.3.3;
  arXiv:2405.13491, Sect. 4.1.1]. Minimum average overlap between fields:
  2.2% in area [src: arXiv:2405.13491, Sect. 4.1.1].
- **DESI.** One pass is a Hardin et al. icosahedral tiling, 4112 centres
  over the sphere, matched to the focal-plane size; 1427 non-overlapping
  tiles per pass fall in the footprint, and about 75% of the footprint is
  reachable by a fibre in a given pass [src: arXiv:2306.06309, Sect. III].
  The dark programme has seven passes and the bright four, rotated to fill
  gaps, giving 5.2 and 3.2 passes on average; 9929 dark tiles cover
  14,200 deg² (9800 NGC, 4400 SGC) [src]. The pass count follows from
  target densities: about 3000 deg⁻² science fibres needed in dark time
  and 700 deg⁻² in bright time, against about 600 fibres deg⁻² per tile,
  hence five dark and one bright coverage, plus extra passes for targets
  sharing a patrol radius and for lower-priority completeness [src].
  Tile centres are shifted in 10″ steps so that no G < 6 star lands within
  25″ of a guide-focus-alignment camera, whose filter would scatter it into
  a ghost [src: Sect. III.1].
- **4MOST.** Tiles are not a fixed lattice. Each tile is a marked point
  (centre, position angle, exposure time) in a marked point process, and
  the set is chosen by Metropolis–Hastings with simulated annealing on an
  energy that rewards completed targets and penalises overhead, tile
  interactions and departures from the bright/grey/dark time split
  [src: arXiv:2007.03307, Sects. 3, 5]. Inputs per target: position,
  resolution mode, required exposure time in bright, grey and dark sky, and
  the completeness fraction its sub-survey asks for [src: Sect. 2.1].
  Tiles share a centre and position angle within an observing block (OB)
  of at most 75 min, at most 30 min per exposure, with overheads of 3.5 min
  per OB and 4.4 min per exposure; the five-year time split is about 32%
  bright, 21% grey, 47% dark [src: Sect. 2.1]. About 40,000 tiles for about
  50 million targets take a few days on 24 cores [src: Sect. 5].

### Step 4. Dither to meet coverage requirements
<!-- key: step-4-dither-to-meet-coverage-requirements -->

- **Euclid requirements** [src: arXiv:2108.01201, Sect. 4.2]: 95% of the
  area with at least three VIS exposures and 90% with at least three in
  each NISP band; 90% of each field with three or more spectroscopic
  exposures and 50% with four or more, at different grism orientations;
  NISP imaging fainter than 24.0 mag (5σ point source) on average. Dither
  steps are bounded below at 100″ by the reaction wheels and above at 396″
  by the attitude-control star catalogue; commanded steps add 11″ for the
  3σ pointing error [src: Sect. 4.2.1]. Of seven four-vertex patterns,
  only "J" (the Red Book's) and "S" met all constraints; "S" was adopted
  because it cut single-exposure pixels from 0.59% to 0.23% (VIS) and from
  3.47% to 0.99% (NISP) [src: Sect. 4.2.2]. Coverage was computed on
  pixel-level simulations with Monte Carlo pointing errors, 500
  realisations [src: Table 2].
- **HSC Wide** dithers by Δr = 0.6° (equatorial) or 0.3° (north) around
  fiducial pointings at position angles θ_j = θ_0 + (2π/N_dith) j, with
  θ_0 ≈ 63° for gr and 27° for izy, chosen for homogeneous depth; visits
  are retaken if seeing exceeds 1.2″ or transparency falls below 0.7 [src:
  arXiv:1704.05858, Sect. 3.3].
- **Rubin.** Overlap structure from tiling is removed by translational and
  rotational dithers; the i-band depth standard deviation varies by less
  than 5% across the simulated strategies, read as evidence that the
  dithering is effective [src: arXiv:2104.05676, Sect. III.1.1].

### Step 5. Correct exposure for extinction and airmass
<!-- key: step-5-correct-exposure-for-extinction-and -->

DESI scales the time needed per tile by f_dust = 10^(2 × 2.165 E(B−V)/2.5)
(Eq. 1), with E(B−V) the median SFD reddening over the 3.21° tile, and by
f_airmass = X^1.75 (Eq. 2), an empirical factor for throughput, sky and
seeing at airmass X [src: arXiv:2306.06309, Sect. IV.1]. The design mean
of the product is 1.51 [src: Table 8]. Euclid uses A = A_λ × 3.1 E(B−V)
(Eq. 5) with A_λ = 0.68 (VIS), 0.34, 0.23, 0.16 (Y, J, H) and 0.18 (red
grism) [src: arXiv:2108.01201, Sect. 5.1.2, Table 5].

### Step 6. Budget the time
<!-- key: step-6-budget-the-time -->

- **Euclid.** One degree of ecliptic longitude is swept per day and about
  10 deg² of wide survey are observed per day, so six years allow at most
  60 deg² per degree of longitude, reduced to 48 by the about 20% spent on
  calibration and deep fields [src: arXiv:2108.01201, Sect. 5.2.1]. The
  RoI is not uniform in longitude, so "unallocated time" appears where the
  Galactic and ecliptic planes cross, with a six-month period and growing
  towards the end [src: Sects. 5.2.1, 8.2]. Reference survey RSD_2021A:
  2190 − 427 (calibration, auxiliary and deep fields) − 39 (spacecraft
  operations) − 292 (unallocated) = 1432 days, at 10.1 deg² per day after a
  3% mean overlap, giving 14,514 deg²; 15,000 deg² needs fewer than 240
  unallocated days [src: Sect. 8.3]. Yearly areas: 2656, 2762, 2708, 2400,
  2147, 1840 deg² [src: Table 9].
- **DESI.** Effective hours per year = hours (3481) × open-shutter fraction
  (58.4%) × programme fraction × mean speed, giving 1383 dark and 207
  bright effective hours, against 833 and 86 hours needed per year; the
  computed dark margin was 39% and the observed 36% [src: arXiv:2306.06309,
  Table 8]. Survey speed is the rate of effective-time accumulation at
  zenith with no dust in current conditions, from 0 to about 2.5 [src:
  Sect. V.3]. Tile hour angles are assigned by simulated annealing so that
  the needed LST distribution matches the available one while minimising
  total time [src: Sect. IV.1].

### Step 7. Check against survey simulations
<!-- key: step-7-check-against-survey-simulations -->

DESI compared observed and simulated completeness of the dark programme
through June 2022 (29.0% against 27.0%) and decomposed the difference:
dark speed +14%, weather +11%, time in dark programme −3%, neglected slews
−3%, technical downtime −2%, tiles not counted −2%, overexposure −2%;
after adjustment the survey ran 4% slower than simulated, "good
agreement" [src: arXiv:2306.06309, Sect. VIII.1, Table 10]. Euclid
recomputed its reference survey from 2015 to 2021, each version moving the
available time by changes in calibration, RoI or ROS length [src:
arXiv:2108.01201, Sect. 8.3].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Depth against area
<!-- key: depth-against-area -->

- **Etendue sets the menu.** A system with one sixth of LSST's etendue
  would, at equal conditions, be about 1 mag shallower in the same time
  (samples smaller by 4 for Euclidean counts, 2–3 for galaxies near z ~ 1),
  or need a six times smaller area (about 3500 deg²) to keep the coadd
  depth; the authors derive a minimum etendue of about 300 m² deg² for
  addressing all LSST goals with one data set [src: arXiv:0805.2366,
  Sect. II.3].
- **Area first, as a rule.** Doubling the time spent doubles the source
  count if used for area, but buys only about 0.4 mag at fixed area, which
  more than doubles the count only for count slopes k > 0.75 in
  log N = C + k m; almost all populations have k ≤ 0.6, hence LSST
  maximises area first [src: arXiv:0805.2366, Sect. II.2.1, footnote 7].
- **Which probes want what.** Across Rubin simulations the 3×2pt figure of
  merit rises linearly with area and is nearly indifferent to depth once
  depth suffices; photometric redshifts prefer depth; weak-lensing shear
  systematics improve with more visits; supernova and kilonova counts rise
  by up to 27% for deeper surveys, through cadence [src: arXiv:2104.05676,
  Sect. VI.1]. Preferred: keep 18,000 deg² of wide-fast-deep but define it
  by a dust-extinction cut, which gains area without losing depth [src:
  Sects. VI.1, VI.2].
- **Cost of area in a space mission.** Euclid's 3% shortfall (486 deg², a
  month and a half of observing) translates into a comparable or smaller
  loss of the dark-energy figure of merit, preliminarily from 500 to about
  480 (**forecast**), because the unobserved RoI is of lower quality [src:
  arXiv:2108.01201, Sect. 8.3].
- **Depth driven by another channel.** Euclid VIS reaches a median S/N of
  15.9 against the required 10 because exposure times are set by the
  spectroscopic channel; spectroscopy has a median S/N of 4.5 against 3.5,
  with less than 50 deg² below requirement [src: arXiv:2108.01201,
  Sect. 5.2.2, Table 7].

### Layered against single-tier
<!-- key: layered-against-single-tier -->

- HSC splits time about 2/3 Wide and 1/3 Deep plus UltraDeep, the Deep
  layers serving galaxy evolution, supernovae and systematics tests of the
  Wide layer at higher S/N [src: arXiv:1704.05858, Sects. 3.1.2, 3.2].
- Roman's wide survey has three tiers: a medium tier of YJH imaging and
  grism over 2415 deg² (about 360 million shapes, n_eff ≈ 41 arcmin⁻², and
  19 million redshifts), a 19.2 deg² deep tier for calibration of shapes,
  photometric redshifts and spectral decontamination, and an H-only wide
  tier of 2700 deg² that uses 80 days, 15% of the allocation, to more than
  double the area (about 260 million shapes, n_eff ≈ 27 arcmin⁻²) [src:
  arXiv:2505.10574, Sect. III.1]. The committee kept the wide tier at full
  size because of public access, a standard band less exposed to chromatic
  PSF effects than Euclid VIS, and overlap with Rubin and DESI (Euclid
  covers only about 470 deg² of it), and rejected the "overguide" southern
  extension as too narrow in impact [src]. Deep-tier observations go early,
  the wide tier late [src].

### Depth-first against breadth-first
<!-- key: depth-first-against-breadth-first -->

DESI completes all passes of a region before moving on, so that early
regions are science-ready and so that a schedule slip leaves "a complete
13,000 sq. deg. survey [rather] than an inhomogeneous 14,000 sq. deg.
survey"; the field selector prefers equatorial tiles, neighbours of
observed tiles and started tiles [src: arXiv:2306.06309, Sect. IV]. A
structural constraint enforces it: each observation depends on earlier
overlapping ones (quasars at z > 2.1 found on a first pass are reobserved
for the Lyα forest), so no two overlapping tiles of a programme are
observed in one night [src]. HSC reached full depth in all five filters
within a few lunations before building area, because five-band photometry
is needed by most goals [src: arXiv:1704.05858, Sect. 3.2].

### Rolling cadence against uniform depth
<!-- key: rolling-cadence-against-uniform-depth -->

Rubin's rolling cadence observes half the declination range at high
cadence for a season and swaps; a full cycle takes about 2.5 years [src:
arXiv:2512.16478, Sect. II.4]. In the v3.4 baseline the coadd was uniform
only after year 1 and at year 10; the old rolling could lose nearly half
the survey for static science at intermediate releases and cut the
dark-energy figure of merit by about 40% [src: Sects. II.3, IV]. "Uniform
rolling" inserts a non-rolling season between cycles so that depth returns
to near uniformity at years 4 and 7 (a three-year cycle); presented to the
Survey Cadence Optimization Committee in June 2024, it became the v4
baseline [src: Sects. II.5, IV]. Strategies with four rolling cycles
cannot return to uniformity at those years [src: Sect. IV]. The time-domain
cost was reported by the committee as "limited" [src: Sect. II.5].

### Fixed lattice against target-driven tiling
<!-- key: fixed-lattice-against-target-driven-tiling -->

DESI's uniform icosahedral passes give a known coverage pattern (twelve
star-shaped regions of lower coverage at the icosahedron vertices [src:
arXiv:2306.06309, Fig. 3 caption]). 4MOST's tiling follows the target
density; disabling the optimisation of position angle, exposure time or
overhead costs up to 8% more telescope time, and dropping overhead
minimisation alone about 30% more overhead at equal exposure [src:
arXiv:2007.03307, Sect. 4.5]. A naive tiling ignoring target density is
"significantly worse" [src]. 4MOST also asks repeated OB centres to avoid
each other, to keep the field shape out of the selection function [src:
Sect. 2].

### Conditions tiering
<!-- key: conditions-tiering -->

DESI observes dark tiles when survey speed exceeds 0.4, bright tiles down
to 0.08 and backup tiles below, putting the brightest targets in the worst
conditions to limit systematics and overheads [src: arXiv:2306.06309,
Sect. IV]. HSC takes i-band shapes only in seeing below 0.8″ and redder
bands when the Moon is up [src: arXiv:1704.05858, Sect. 3.2].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Survey | Source | Place read |
|---|---|---|---|---|
| RoI exclusions | abs(β) ≤ 10°, abs(b) ≤ 23° (25° at δ ≥ 30°), E(B−V) > 0.09 (local 0.17) | Euclid | arXiv:2108.01201 | Sects. 5.1.2, 5.2.1 |
| RoI area | 17,354 deg² | Euclid | arXiv:2108.01201 | Table 6 |
| ROS length | 4214 s; 4396 s with slews; budget 4400 s | Euclid | arXiv:2108.01201 | Sect. 4.1 |
| Dither step limits | 100″–396″, +11″ commanded margin | Euclid | arXiv:2108.01201 | Sect. 4.2.1 |
| S-pattern coverage | ≥ 3 exposures: 95.43% VIS, 90.88% NISP; ≥ 4 NISP: 50.42% | Euclid | arXiv:2108.01201 | Table 2 |
| Area rate | 10.1 deg² per day | Euclid | arXiv:2108.01201 | Sect. 8.3 |
| Reference footprint | 14,514 deg² (RSD_2021A) | Euclid | arXiv:2108.01201 | Sect. 8.3 |
| Post-launch footprint | 13,416 deg², 13,245 deg² after bright stars | Euclid | arXiv:2405.13491 | Sect. 5.5 |
| Passes | 7 dark (mean 5.2), 4 bright (mean 3.2) | DESI | arXiv:2306.06309 | Sect. III |
| Tiles | 9929 dark, 5676 bright, 1427 per pass | DESI | arXiv:2306.06309 | Sect. III, Table 8 |
| Effective time per tile | 1000 s dark, 180 s bright, 60 s backup | DESI | arXiv:2306.06309 | Table 8 |
| Speed thresholds | dark > 0.4; bright > 0.08 | DESI | arXiv:2306.06309 | Sect. IV |
| Dark margin | 39% computed, 36% observed | DESI | arXiv:2306.06309 | Table 8 |
| Slew overhead | 3.1% of open-shutter time; 2.9% with greedy optimisation | DESI | arXiv:2306.06309 | Sect. IV.2 |
| Visit | 2 × 15 s, ε = 77%, revisit 3 days over 10,000 deg² | LSST | arXiv:0805.2366 | Sect. II.2.2 |
| Effective-area cuts | E(B−V) < 0.2; i5σ > 25.9 at year 10 | Rubin DESC | arXiv:2104.05676 | Sect. III.1 |
| Rolling-cadence cost | up to about half the area and about 40% of the FoM at intermediate releases | Rubin v3.4 | arXiv:2512.16478 | Sect. IV |
| Tiling optimisation gain | up to 8% of telescope time | 4MOST | arXiv:2007.03307 | Sect. 4.5 |
| Time split | 32% bright, 21% grey, 47% dark | 4MOST | arXiv:2007.03307 | Sect. 2.1 |
| Wide-layer split | 2/3 Wide, 1/3 Deep + UltraDeep | HSC | arXiv:1704.05858 | Sect. 3.2 |
| Wide-tier cost | 80 days, 15% of HLWAS, doubles area | Roman | arXiv:2505.10574 | Sect. III.1 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **The time budget erodes area.** Euclid's available time shrank as the
  calibration plan grew (a redefinition added 100 days in 2018) and as the
  RoI was redrawn; each version of the reference survey is a new area [src:
  arXiv:2108.01201, Sect. 8.3]. Test: track available days per survey
  version, not only the area quoted.
- **Hardware surprises after launch.** VIS stray light ten or more times
  the zodiacal background, attributed to a Sun-lit thruster nozzle, forced
  a restricted roll range; allowing ±3° field rotation and a larger
  maximum solar aspect angle (110° to 120°) restored visibility at the cost
  of smaller tiles and 5% of the area [src: arXiv:2405.13491, Sects. 5.4,
  5.5].
- **Unallocated time late in a survey.** It grows from 0 to 292 days over
  six years in Euclid's plan [src: arXiv:2108.01201, Table 9]; candidate
  uses that keep the survey constraints include repeat passes on the
  ecliptic, a 200–300 deg² medium-deep field one magnitude deeper, and
  blue-grism observations [src: Sect. 8.2].
- **Simulations that miss a programme.** DESI's bright programme ran about
  twice as fast as simulated because the simulations had no observing
  within 15° twilight or 4 days of full Moon and a rudimentary bright-sky
  model; it was over 40% complete after little more than a year and had to
  be expanded [src: arXiv:2306.06309, Sect. VIII.1].
- **Depth stripes from cadence.** Rolling cadence leaves large-scale depth
  patterns that regression or deprojection handles exactly only for linear
  contamination; DESC metrics (stripiness, area at risk, tomographic σ8
  bias, mean-z bias) measure the damage [src: arXiv:2512.16478, Sects.
  II.3, III].
- **Tiling imprint.** Field overlaps add structure to the depth map unless
  dithered away; check the depth standard deviation at each planned
  release, not only at the end [src: arXiv:2104.05676, Sect. III.1.1].
- **Bright stars.** Euclid skips tiles with blinding stars (171 deg² lost
  in the latest plan) and could recover some by local re-tessellation;
  DESI shifts tile centres [src: arXiv:2405.13491, Sect. 5.5;
  arXiv:2108.01201, Sect. 8.3; arXiv:2306.06309, Sect. III.1].

## Reading list
<!-- key: reading-list -->

- Method: Scaramella et al. 2022, arXiv:2108.01201 — RoI, ROS, dither
  requirements, tessellation, time budget of the Euclid Wide Survey.
- Application: Euclid Collaboration 2025, arXiv:2405.13491 — the
  post-launch redesign of the survey (Sects. 4.1, 5.4, 5.5).
- Method: Schlafly et al. 2023, arXiv:2306.06309 — DESI footprint, passes,
  effective time, speed tiers, effective-hours table, simulation check.
- Foundation: Ivezić et al. 2019, arXiv:0805.2366 — visit-time equations
  and the etendue argument for depth against area.
- Method: Lochner et al. 2022, arXiv:2104.05676 — metrics and the
  depth–area trade for Rubin cosmology.
- Critique: Leistedt et al. 2025, arXiv:2512.16478 — rolling cadence
  against uniformity and the uniform-rolling fix.
- Method: Tempel et al. 2020, arXiv:2007.03307 — target-driven tiling by a
  marked point process (4MOST).
- Application: Aihara et al. 2018, arXiv:1704.05858 — layered design,
  dithers and condition rules of HSC-SSP.
- Application: Roman Observations Time Allocation Committee 2025,
  arXiv:2505.10574 — tier design and the reasons given for each tier.

## Not verified
<!-- key: not-verified -->

- The DESI bright-programme tile count: Sect. III and Table 8 of
  arXiv:2306.06309 give 5676, Sect. IV gives 2,657; not resolved here.
- The numerical solar-aspect and roll-angle (AA) ranges of Euclid before
  and after the stray-light finding (lost in the rendering of
  arXiv:2405.13491, Sects. 4.1.1 and 5.4).
- The DESI survey-design rationale in the Final Design Report
  (arXiv:1611.00036) and the Hardin et al. tiling, cited by
  arXiv:2306.06309 but not read.
- The 4MOST Survey Strategy Plan (arXiv:1903.02466) and probabilistic
  fibre assignment (Tempel et al. 2020b): seen as titles only.
- The Rubin SCOC Phase 3 report and the adopted v4 baseline numbers.
- Markovič et al. 2017 (Euclid dither study): cited, not read.
