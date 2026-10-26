# Surveys and facilities — facility-by-facility reference

Scope: one compact entry per facility relevant to observational cosmology, with instrument, site, sky area, releases, status and next milestone.
Snapshot: 2026-10-14 (web pages fetched 2026-10-09 unless another date is given)

Flags. `[src]`: read by this skill's author session in the cited paper or on
the named official page. `[sec: GC]`, `[sec: WL]`, `[sec: CMB]`, `[sec: SN]`,
`[sec: CL]`: carried over from `references/surveys-and-data.md` of
`cosmo-galaxy-clustering`, `cosmo-weak-lensing`, `cosmo-cmb`,
`cosmo-supernovae`, `cosmo-clusters`, where the fact is flagged [src] against
the same citation. `[sec: web]`: from a web-search summary of the named page,
not read on the page. `[der]`: derived here. `[src: Table 3]` or
`[src: Sect. 2]` names the place read in the paper body; a plain `[src]`
on a paper means its abstract. Design numbers of facilities not
yet operating are labelled **design** or **forecast**. Sample sizes, n(z) and
analysis detail live in the probe skills; this file holds the hardware, the
footprint, the releases and the calendar.

## 1. Spectroscopic facilities
<!-- key: spectroscopic-facilities -->

### 1.1 Before SDSS-III
<!-- key: before-sdss-iii -->

2dFGRS, 6dFGS and WiggleZ (AAT and UK Schmidt fibre surveys) are described
with their sample sizes in `cosmo-galaxy-clustering`
(`references/surveys-and-data.md`, Sect. 1); they are closed archives.

### 1.2 SDSS-I to SDSS-V (2.5 m Sloan Foundation Telescope, Apache Point; 2.5 m du Pont, Las Campanas)
<!-- key: sdss-i-to-sdss-v-2-5-m-sloan-foundation -->

- **SDSS-I/II design**: imaging of π steradians above Galactic latitude about
  30° in five bands to g′ ≈ 23, and spectra of about one million galaxies and
  10⁵ quasars [src: abstract] (York et al. 2000, arXiv:astro-ph/0006396).
- **BOSS (SDSS-III) design**: 1.5 million luminous galaxies to i = 19.9 over
  10,000 deg² at z < 0.7 and more than 150,000 quasars (g < 22) for the Lyα
  forest at 2.15 < z < 3.5 [src: abstract] (Dawson et al. 2013, arXiv:1208.0022).
- **eBOSS (SDSS-IV) design**: more than 250,000 LRGs (median z = 0.72), about
  195,000 ELGs, more than 500,000 quasars at 0.9 < z < 2.2, and, for the Lyα
  forest at z > 2.1, 60,000 new quasars plus 60,000 BOSS quasars re-observed [src: abstract] (Dawson et al. 2016,
  arXiv:1508.04473). Final BOSS and eBOSS sample counts are in
  `cosmo-galaxy-clustering`. SDSS-IV ran APOGEE-2, MaNGA and eBOSS (with
  SPIDERS and TDSS) from summer 2014, with the du Pont telescope joining in
  early 2017 [src] (Blanton et al. 2017, arXiv:1703.00052).
- **SDSS-V** (Kollmeier et al. 2025, arXiv:2507.06989) [src]: all-sky,
  multi-epoch; at each of the two telescopes 500 robotic positioners feed an
  optical spectrograph (BOSS, R ≈ 2000, 500 fibres) and a near-infrared one
  (APOGEE, R ≈ 22,000, 300 fibres); a separate facility (LVM-I, Las Campanas)
  does integral-field spectroscopy with 1801 fibres over 3600–9800 Å at
  R ≈ 4000 across about 4000 deg². Programmes: Milky Way Mapper, Black Hole
  Mapper, Local Volume Mapper. Robotic MOS operations began in 2021 and LVM
  in 2023. Each Focal Plane System carries 500 positioners with three
  120 μm fibres (metrology, BOSS, APOGEE), only 298 connected to APOGEE at
  a time; the fibre subtends 2″ at Apache Point and 1.3″ at Las Campanas;
  reconfiguration takes ≲ 3 minutes against about 15 for a plug-plate swap
  [src: Sect. III.2]. **SDSS-V has no galaxy-clustering cosmology programme**; its
  extragalactic spectra are AGN and eROSITA counterparts.
- **Releases** (sdss.org data-release publication page) [src]: EDR 5 June
  2001; DR7 (end of SDSS-I/II) 31 October 2008; DR8 11 January 2011; DR9
  31 July 2012; DR10 30 July 2013; DR11 and DR12 6 January 2015; DR13 31 July
  2016; DR14 31 July 2017; DR15 10 December 2018; DR16 9 December 2019; DR17
  6 December 2021; DR18 19 January 2023; DR19 10 July 2025; DR20 30 July 2026.
  DR16 holds the complete eBOSS main sample and DR17 closes SDSS-IV [src]
  (Abdurro'uf et al. 2021, arXiv:2112.02026). DR18 is the first SDSS-V
  release and DR19 (July 2025) the first with all three mappers; DR20 has more than 3 million spectra of 1.5 million
  stars and half a million galaxies and quasars, the first southern BOSS
  spectra, and X-ray targets coordinated with eROSITA DR2 [src] (SDSS
  Collaboration 2026, arXiv:2607.26149). Access: `sdss.org/dr20`.

### 1.3 DESI (4 m Mayall, Kitt Peak) and DESI-II
<!-- key: desi-4-m-mayall-kitt-peak-and-desi-ii -->

- **Instrument** (as built; Abareshi et al. 2022, arXiv:2205.10939): 3.2°
  diameter prime-focus corrector, 5020 robotic positioners on a 0.812 m
  focal surface, minimum separation 10.4 mm, in ten petals feeding ten
  three-channel spectrographs over 360–980 nm [src: abstract]. Requirements: field
  ≥ 7.65 deg², fibre density < 700 per deg², R > 1500 (360–555 nm),
  > 3000 (555–656 nm), > 4000 (656–980 nm) [src: Table 4, Sect. II.3]; survey of at
  least 9000 deg², 14,000 deg² "baseline with margin"; BAO distance scale to
  0.28% at 0 < z < 1.1 and 0.39% at 1.1 < z < 1.9, H(z) to 1.05% at
  1.9 < z < 3.7 [src: Table 3, Sect. II.3]. Each positioner reaches a 12 mm diameter
  patrol disc (plate scale about 70 μm per arcsecond, fibre 107 μm)
  [src: Sect. V.2, XIII.3].
- **Survey definition**: the 2016 science, targeting and survey-design
  paper (DESI Collaboration 2016, arXiv:1611.00036) [src: abstract]: LRGs to z = 1.0,
  [O II] ELGs to z = 1.7, quasars as tracers and, at 2.1 < z < 3.5, for the
  Lyα forest, a Bright Galaxy Survey of about 10 million galaxies at median
  z ≈ 0.2 in moonlit time, more than 30 million redshifts in total.
- **Survey as designed**: 14,000 deg² in five years [src] (DESI
  Collaboration 2023, arXiv:2306.06307); survey start May 2021
  (arXiv:2205.10939) [sec: GC]; 15,000 fields, scheduled automatically each night, with
  the dark-time programme running about 7% faster than forecast after 1.1
  years [src] (Schlafly et al. 2023, arXiv:2306.06309). The Survey Validation
  paper projected final samples of 7.2 (MWS), 13.8 (BGS), 7.46 (LRG), 15.7
  (ELG) and 2.87 (QSO) million (**forecast**) [src] (arXiv:2306.06307).
  Target densities: BGS Bright 854, LRG 624, QSO 310 deg⁻²
  (arXiv:2404.03002) [sec: GC]. Targets come from the Legacy Surveys
  (Sect. 2.4).
- **Releases**: EDR 13 June 2023 (1.8 million unique targets, December 2020
  to June 2021); DR1 19 March 2025 (18.7 million spectra, May 2021 to June
  2022), labelled "latest" on the release page fetched 2026-10-09; DR2
  cosmology chains public, **DR2 spectra not public** [src]
  (`data.desi.lbl.gov/doc/releases/`). Papers: arXiv:2306.06308 (EDR),
  arXiv:2503.14745 (DR1), which gives high-confidence redshifts for 18.7M
  objects [src: abstract] from the first 13 months of the main survey, 2021
  May 14 through 2022 June 13 [src: Sect. I.1].
- **Status**: the planned five-year survey was declared complete in April
  2026 with more than 47 million galaxies and quasars against a goal of 34
  million; observations continue through 2028 and extend the footprint from
  14,000 to about 17,000 deg²; full-survey dark-energy results expected in
  2027 [sec: GC] (Berkeley Lab release of 15 April 2026).
- **DESI-II**: introduced in the Snowmass road map as a programme that "will
  pilot observations of galaxies both at much higher densities and extending
  to higher redshifts" [src] (Schlegel et al. 2022, arXiv:2209.03585). The
  2026 DESI papers on Lyman-alpha emitters selected from DECam
  intermediate-band imaging (IBIS) describe themselves as preparation for
  DESI-II; they find a linear bias of 2.31–2.62 for LAEs at 2.26 < z < 3.41
  [src: abstract] (Ebina et al. 2026, arXiv:2606.24852). No DESI-II survey definition
  paper was found.

### 1.4 Subaru PFS (8.2 m, Maunakea)
<!-- key: subaru-pfs-8-2-m-maunakea -->

2386 science fibres over 1.25 deg², offered to the community since March
2025, queue-observed and allocated in "fibre hours"; reduced data are
delivered through the PFS Science Platform (arXiv:2606.14012) [sec: GC] and
[src] for the last clause. As operated (Tanaka et al. 2026) [src: Sect. 2]:
each fibre on a two-axis "cobra" positioner with a patrol disc of about 1′
diameter, fibre about 1.1″ on the sky; four spectrograph modules with
blue (380–650 nm), red (630–970 nm) and near-infrared (940–1260 nm) arms at
R ≈ 2500, 3000 and 4500, plus a red medium-resolution mode at R ≈ 5500
(710–885 nm); after eight positioning iterations, typically three minutes
or less, 75% of fibres are within 10 μm (about 0.1″). Design paper: Tamura
et al. 2016, arXiv:1608.01075 [src], which gives the design count of 2394
fibres. The PFS Subaru Strategic Program is 360 nights, 130 of them
for galaxy evolution [src] (abstract of Greene et al. 2022, "The Prime Focus
Spectrograph Galaxy Evolution Survey", read through an arXiv search); the
cosmology **forecast** (ELGs at 0.8 < z < 2.4, 9.3 (Gpc/h)³) is in Takada et
al. 2014 (arXiv:1206.0737) [sec: GC], which assumed 300 nights in total.

### 1.5 4MOST (4 m VISTA, Paranal)
<!-- key: 4most-4-m-vista-paranal -->

Field of view 4.2 deg²; 1624 fibres feed two low-resolution spectrographs
(R ≈ 6500) and 812 fibres a high-resolution one (R ≈ 20,000) [src: abstract] (de Jong
et al. 2019, arXiv:1903.02464), that is 2436 spectra per pointing through
three spectrographs [src: abstract] (Winkler et al. 2026, arXiv:2606.27882). First light 18 October 2025 (ESO
announcement) [sec: GC]. The project site, fetched 2026-10-09, still reads
"currently going through the Verification, Commissioning, and Survey
Validation Phases" with "an expected start of full science operations in Q2
2026", and carries a news item of 28 January 2026 on commissioning success
[src] (`4most.eu`); a news item of 15 June 2026 reports 76 nights of
Survey Programme Validation data and an "imminent" main-survey start [src].
Five-year programme: at least 25 million objects over
at least 15,000 deg², ten consortium and fifteen ESO community surveys,
data at AIP and ESO archives [src] (same page). Cosmology Redshift Survey:
5.4 million redshifts over about 5700 deg² (arXiv:2510.02449) [sec: GC].

### 1.6 WEAVE (4.2 m William Herschel Telescope, La Palma)
<!-- key: weave-4-2-m-william-herschel-telescope-la-palma -->

2° prime-focus field, nearly 1000 fibres, 20 deployable mini-IFUs and one
large IFU, dual-beam spectrograph covering 366–959 nm at R ≈ 5000 or two
shorter ranges at R ≈ 20,000; eight surveys over five to seven years,
including more than one million spectra of LOFAR radio sources and a z > 2
intergalactic-gas (quasar absorption) survey [src] (Jin et al. 2023,
arXiv:2212.03981). Focal-plane modes [src: Table 2]: 960 (plate A) or 940
(plate B) MOS fibres of 1.3″ (85 μm) deployable over 2°, minimum separation
about 60″, configuration time about 55 minutes (a 2dF-type pick-and-place
positioner); 20 mini-IFUs of 37 fibres; one large IFU of 547 fibres of
2.6″ over 90″ × 78″. WEAVE-QSO plans about 450,000 quasars at z > 2.2 over
up to 10,000 deg², with denser J-PAS-selected sampling over about
6000 deg² and about 420 deg² at high density (**design**)
[src: Sect. 4.8]. Status [src] (ING WHT page): large-IFU surveys since
October 2023; stand-down from 16 September 2024 to July 2025 for a
spectrograph misalignment; all three modes offered for semester 2026B; the
multi-object surveys "are expected to start ~ April 2026", and the page does
not confirm that they did. Once commissioning ends, 70% of WHT time goes to
the WEAVE surveys. No public data release date was found.

### 1.7 MOONS (8 m class VLT, Paranal)
<!-- key: moons-8-m-class-vlt-paranal -->

About 1000 fibres with individual robotic positioners, simultaneous
0.64–1.8 μm coverage at low and high resolution [src: abstract] (Cirasuolo et al.
2020, arXiv:2009.00628); 25-arcminute field, R ≈ 19,700 in the H-band
high-resolution setting [src: abstract] (Gonzalez et al. 2020, arXiv:2009.00635). ESO
announced first observations on 3 September 2026 and expects up to ten
million objects over a ten-year design lifetime [src] (ESO announcement
ann26007). No survey start date is given there.

### 1.8 Euclid NISP (space, L2) — slitless
<!-- key: euclid-nisp-space-l2-slitless -->

16 H2RG detectors at 0.3″ per pixel, field of view 0.57 deg²; slitless grism
spectroscopy at R ≥ 450 over 950–2020 nm; line sensitivity about
2 × 10⁻¹⁶ erg s⁻¹ cm⁻² at S/N = 3.5 at 1.6 μm; photometry to about 24.5 AB
(5σ point source); 14,000 deg² in six years [src] (Euclid Collaboration
2024, arXiv:2405.13493). The pre-launch reference survey covered 14,500 deg²
[src] (Scaramella et al. 2022, arXiv:2108.01201). Mission overview:
arXiv:2405.13491. Mission definition (Phase A "Red Book", Laureijs et
al. 2011, arXiv:1110.3193) [src]: 1.2 m Korsch telescope, common field of
about 0.54 deg², wide survey of 15,000 deg² plus two 20 deg² deep fields,
30–40 resolved galaxies per arcmin² for weak lensing, photo-z
σ_z/(1+z) < 0.05, spectroscopic σ_z/(1+z) = 0.001 at R ≈ 250 (Hα), launch
then foreseen in 2019; these are the 2011 numbers, superseded by the
as-built papers below and by a launch on 1 July 2023. From the NISP paper body [src: Sect. 2]: a 1.20 m
three-mirror anastigmat (Korsch) telescope shared with VIS through a
dichroic; requirements of 900–2000 nm, R ≥ 380 with two grisms, Hα line
limit ≤ 2 × 10⁻¹⁶ erg cm⁻² s⁻¹ at 3.5σ at 1600 nm, 24.0 mag (5σ point
source) in three bands, photometric calibration ≤ 1.5% over the survey;
Euclid Wide Survey about 14,000 deg² and Euclid Deep Survey about 53 deg²,
2 mag deeper, in six years. Initial in-flight values [src: Table 5]: 5σ
point-source limits Y_E 24.6, J_E 24.6, H_E 24.5 AB; PSF FWHM 0.34–0.35″;
red-grism line limit about 2 × 10⁻¹⁶ (3.5σ); no blue-grism limit yet.
Releases and calendar: the Euclid entry of Sect. 2 and the tables of `results.md`.

### 1.9 Roman (2.4 m space telescope, L2) — slitless
<!-- key: roman-2-4-m-space-telescope-l2-slitless -->

2.4 m telescope, Wide Field Instrument field of 0.281 deg² for near-infrared
imaging and slitless spectroscopy [src] (Akeson et al. 2019,
arXiv:1902.05569). Launched 30 August 2026; in commissioning, with the
primary instrument activated (NASA story of 15 September 2026) and the
guidance system checked (30 September 2026) [src] (NASA mission page). The
three Core Community Surveys are the High Latitude Wide Area Survey, the
High Latitude Time Domain Survey and the Galactic Bulge Time Domain Survey;
they receive 74.5% of Wide Field Instrument time and General Astrophysics
Surveys 25.5% [src] (Roman Observations Time Allocation Committee 2025,
arXiv:2505.10574). The High Latitude Wide Area Survey covers "more than
5,000 square degrees (about 12 percent of the sky) altogether in just under
a year and a half": a main part of about 2,500 deg² with spectroscopy and
multi-filter imaging, a wider part of more than twice that area in a single
filter, and a small deep part [src] (NASA HLWAS page). The committee report
[src: Sect. II] gives the tiers: a 2400 deg² medium tier in Y, J, H imaging
and grism spectroscopy, 26.5 mag (AB, 5σ point source, about 600 s) and
1.5 × 10⁻¹⁶ erg cm⁻² s⁻¹ (5σ line flux, about 1500 s); a 2700 deg² wide
tier in H only; a 19.2 deg² deep tier about 1.2 mag deeper in imaging and
2.5 times deeper in line flux. The High Latitude Time Domain Survey images
about 18 deg² (wide) and 6.5 deg² (deep) at about five-day cadence for two
years in the middle of the five-year mission, aiming at S/N ≈ 20 for a SN Ia
at maximum at z ≈ 0.9 and 1.7, with prism spectroscopy over 4.5 and
0.56 deg² [src: Sect. II]. The 2021 reference spectroscopic survey (2000 deg²,
1.0–1.93 μm grism, about 10 million Hα redshifts at z = 1–2; **forecast**)
is in arXiv:2110.01829 [sec: GC]; it predates the committee's definition.

### 1.10 SPHEREx (space, low-Earth orbit) — spectrophotometry
<!-- key: spherex-space-low-earth-orbit-spectrophotometry -->

Launched 11 March 2025; 102 bands from 0.75 to 5.0 μm at R = 35–130 in 6.2″
pixels; four all-sky passes in two years (arXiv:2511.02985) [src: abstract]. The
first all-sky pass was complete by late 2025, and spectral images are
released weekly at IRSA ("QR2" since October 2025) [sec: web]. No redshift
catalogue is public.

### 1.11 Planned Stage-V spectroscopic facilities
<!-- key: planned-stage-v-spectroscopic-facilities -->

| Facility | Design | Status | Source |
|---|---|---|---|
| MUST | 6.5 m; more than 20,000 targets over about 5 deg²; eight-year survey in the 2030s, redshifts for more than 100 million galaxies and quasars [src: abstract], of which up to 40 million at 2 < z < 5.5 [src: Sect. 2.4] (**design**) | "currently under construction" [src: abstract] | Cai et al. 2026, arXiv:2605.10102 |
| Spec-S5 | two existing 4-m telescopes upgraded to 6-m wide-field observatories, 13,000 spectra simultaneously each (**design**) | concept | arXiv:2608.07927 [src: abstract; Table 1] |
| WST | 12 m; 20,000 low-resolution fibres over 3 deg² (Sect. 5.1 assumes a "10–12m class facility") plus a 3 × 3 arcmin² integral-field spectrograph, operating in parallel (**design**) | proposed | Mainieri et al. 2024, arXiv:2403.05398 [src: Summary; Sect. 1.2, 5.1]; Lee et al. 2026, arXiv:2607.01150 |
| MSE | 2018: 11.25 m, 1.52 deg², 4332 spectra per exposure, R = 2500–40,000, replacing CFHT. 2025: quad-mirror 11.5 m, more than 18,000 fibres, 1.5 deg², R = 7000 from 360 nm through H band and R = 40,000 (**design**) | "proposed to replace the Canada-France-Hawai'i Telescope in the 2040s"; a CFHT Board recommendation of December 2024 to wind down MSE activities is reported by a web summary [sec: web] | Hill et al. 2018, arXiv:1810.08695; Frinchaboy et al. 2025, arXiv:2503.15553 [src: abstract of each] |

## 2. Imaging surveys
<!-- key: imaging-surveys -->

| # | Survey | Telescope, camera, site | Footprint and depth | Releases and access | Status / next | Source |
|---|---|---|---|---|---|---|
| 2.1 | SDSS imaging | 2.5 m Sloan, Apache Point | π sr in five bands to g′ ≈ 23; "ubercalibration" reaches about 1% relative calibration in griz over 8500 deg² (2% in u), public from DR6 | SDSS DRs (Sect. 1.2) | closed | arXiv:astro-ph/0006396; Padmanabhan et al. 2008, arXiv:astro-ph/0703454 [src] |
| 2.2 | Pan-STARRS1 3π | PS1 telescope | 3π sr in grizy; stack 5σ depths 23.3, 23.2, 23.1, 22.3, 21.4; photometric calibration systematics 7–12 mmag | MAST (STScI) | closed; the photometric reference of many SN and Legacy-Survey calibrations | Chambers et al. 2016, arXiv:1612.05560 [src: abstract] |
| 2.3 | DES | 4 m Blanco + DECam (2.2° diameter field, 570 Mpix, 62 science CCDs, 0.263″ per pixel), Cerro Tololo | about 5000 deg² in grizY; design [src: Sect. I, II.1.2]: 5000 deg² wide plus 30 deg² supernova fields in 525 nights (105 nights a year for five years), filters g, r, i, z, Y over 400–1065 nm, 250 μm thick fully depleted red-sensitive CCDs, optics goal 0.27″ FWHM as designed and 0.33″ as built; DR2 coadd depth at S/N = 10 (1.95″ aperture) g 24.7, r 24.4, i 23.8, z 23.1, Y 21.7; median PSF FWHM 0.95″ in r; uniformity better than 3 mmag against Gaia | DR2 (six years; about 691 million objects; paper posted January 2021); the Y6 Gold cosmology photometry is described in `cosmo-weak-lensing` | observations complete; Y6 cosmology published 2026 (see `cosmo-weak-lensing`) | Flaugher et al. 2015, arXiv:1504.02900; DES Collaboration 2021, arXiv:2101.05765 [src] |
| 2.4 | DESI Legacy Imaging Surveys | DECam on Blanco (DECaLS and other public DECam data), 90Prime on the Bok (BASS), Mosaic-3 on the Mayall (MzLS) | original three surveys: about 14,000 deg² in g, r, z with dynamic exposure times for uniform depth, plus four WISE bands [src] (Dey et al. 2019, arXiv:1804.08657). DESI targeting requirements [src: App. A]: depths g ≥ 24.0, r ≥ 23.4, z ≥ 22.5 (optimal-extraction depth for an exponential galaxy of 0.45″ half-light radius), at least 14,000 deg², ≥ 90% at full depth in all three bands, z-band FWHM < 1.5″, astrometry < 95 mas random and < 30 mas systematic. DR11: about 22,731 deg² covered in all bands jointly; south (Dec ≤ 32.375°) in griz from DECam including the full DES, DELVE and DeROSITAS; north in grz (BASS/MzLS, reprocessed from DR9); about 3.9 billion sources; DECam data through September 2024; astrometry tied to Gaia DR3 | DR9 was the DESI targeting release and DR10.1 the 4MOST CRS selection [sec: GC]; **DR11 is current** on `legacysurvey.org` (page marked 2026, no release day given) | imaging continues to be reprocessed; the site quotes models over about 31,000 deg² in "optical and infrared bands", a looser count than the 22,731 deg² joint coverage | `legacysurvey.org` and its DR11 description page [src] |
| 2.5 | KiDS | VST + OmegaCAM, Paranal, with VISTA/VIKING near-infrared | final DR5: 1347 deg² in ugri (two i epochs) plus near-infrared, nine bands (design was 1500 deg² [src: abstract], de Jong et al. 2012, arXiv:1206.1254). DR5 body [src: Sect. 3.1.1] (Wright et al. 2025): 1347 tiles of 1° × 1° (the OmegaCAM field) in two stripes, 70° × 9° at the south Galactic pole and 85° × 8° on the equator; KiDS started in 2011 and VIKING in 2009; VIKING was stopped at about 90% of its area and KiDS truncated to match; the planned g-band repeat pass became a second i pass | ESO archive, Astro-WISE, `kids.strw.leidenuniv.nl/DR5/` | complete; KiDS-Legacy is the final cosmology | arXiv:2503.19439 [sec: WL] |
| 2.6 | HSC-SSP | 8.2 m Subaru + Hyper Suprime-Cam, Maunakea | 300-night programme; Wide 1400 deg² in grizy to r ≈ 26 (5σ point source), Deep 26 deg², UltraDeep 3.5 deg² (**design**) [src] (Aihara et al. 2018, arXiv:1704.05858). Camera [src: Table 1]: 1.5° diameter field, 104 science CCDs, 0.168″ pixels, grizy plus four narrow bands, 20 s readout (about 35 s overhead). Wide-layer design depths g 26.5, r 26.1, i 25.9, z 25.1, y 24.4 for 10–20 min per band; Deep 27.5–25.3 and UltraDeep 28.1–26.3 in grizy [src: Table 2]. PDR3: 278 nights, about 670 deg² at full depth in five bands, 1470 deg² including partial coverage [src] (Aihara et al. 2022, arXiv:2108.13045) | PDR3 at `hsc-release.mtk.nao.ac.jp` (paper posted 30 August 2021) | observations complete; a later public release was not checked | as cited |
| 2.7 | UNIONS | CFHT, Pan-STARRS and Subaru, Hawaii | core region 6250 deg² in ugriz; 10σ point-source depths (2″ aperture) 23.7, 24.5, 24.2, 23.8, 23.3; median depths against an original goal of 23.6, 24.5, 23.9, 23.6, 23.4, the metric chosen to match Euclid specifications [src: Sect. II.2.2]; CFHT r band taken only in seeing below 1″, median r image quality 0.7″, driven by weak lensing [src: Sect. II.1.2, III.1.1] | no general public release date read; the UNIONS-3500 shear catalogue is described in `cosmo-weak-lensing` | ongoing; northern ground complement of Euclid | Gwyn et al. 2025, arXiv:2503.13783 [src] |
| 2.8 | DECADE | DECam community and archival imaging outside DES | shear over 5412 deg² (north cap) [src: Sect. IV]; 13,000 deg² with DES Y3 [src: abstract] | catalogues and likelihoods public [sec: WL] | complete as a lensing data set | arXiv:2509.03582 |
| 2.9 | Rubin LSST | Simonyi Survey Telescope, 8.4 m primary (6.5 m effective), 9.6 deg² field, 3.2 Gpix camera, Cerro Pachón | **design**: 18,000 deg² deep-wide-fast survey visited about 800 times in ugrizy (320–1050 nm) over ten years; single-visit depth r ≈ 24.5, coadd r ≈ 27.5; about 90% of the time in the main survey [src: abstract; Sect. II.2.1 for the single-visit depth] (Ivezić et al. 2019, arXiv:0805.2366). Baseline design [src: Table 1]: f/1.234, étendue 319 m² deg², 0.2″ pixels; 5σ single-visit design depths ugrizy 23.9, 25.0, 24.7, 24.0, 23.3, 22.1 (minimum specification 23.4, 24.6, 24.3, 23.6, 22.9, 21.7); mean visits 56, 80, 184, 184, 160, 160; idealised coadd depths 26.1, 27.4, 27.5, 26.8, 26.1, 24.9; about 2.45 million visits in ten years [src: Sect. III.1.1] | DP1: about 15 deg², seven fields (arXiv:2603.23786) [sec: WL]; Early DP2 on 27 July 2026: LSSTCam observations from April 2025 to January 2026, coadds over about 3000 deg², single-epoch products over about 15,000 deg², deep-coadd images only but all catalogues; full DP2 "Oct-Dec 2026"; access for data-rights holders on the Rubin Science Platform [src] (`dp2.lsst.io`, last modified 2026-08-13) | ten-year survey began 30 June 2026 [sec: WL]. DR1 "based on the first year of LSST observations" [src] (RTN-011 v9.1, dated 2026-10-01); no DR1 date was read | as cited |
| 2.10 | Euclid VIS | ESA Euclid, L2; 1.2 m primary; VIS camera of 609 Mpix (6 × 6 CCDs of 4k × 4k), 0.54 deg² field (0.787° × 0.709°), 0.1″ sampling, resolution 0.18″ [src; Sect. 2.2 for the array and field] | about 14,000 deg² in one broad band I_E (r+i+z; 550–920 nm), m_AB ≥ 24.5 at S/N ≥ 10 required; Deep Survey of more than 50 deg² (**design**); survey of 6 years in a 6.5-year mission [src: Sect. 2.2] | ERO May 2024; Q1 19 March 2025; Q2 24 June 2026 (Galactic bulge, no cosmology product) | launched 1 July 2023; nominal survey began 14 February 2024. Next: DR1-Foundation 12 November 2026; DR1 mid-2027; Q3 2028; DR2 June 2029; Q4 2030; DR3 October 2031, all "tentative" | Euclid Collaboration 2024, arXiv:2405.13492 [src]; ESA timeline page, re-fetched 2026-10-09 and unchanged from the siblings' reading of 2026-10-08 [src] |
| 2.11 | Roman imaging | 2.4 m, Wide Field Instrument 0.281 deg² | High Latitude Wide Area Survey (imaging and grism) and High Latitude Time Domain Survey (wide tier 18.3 deg², deep tier 6.5 deg² [sec: SN]) | none | launched 30 August 2026, commissioning (Sect. 1.9); first images expected early 2027 [sec: WL, press] | arXiv:1902.05569; arXiv:2505.10574 [src] |
| 2.12 | CSST | 2 m space telescope co-orbiting with the Chinese space station at about 400 km [src: Sect. 1]; survey camera field about 1.1 deg², 0.074″ pixels [src: Sect. 3.3] | **design**: 17,500 deg² wide and 400 deg² deep surveys "in ten years" [src: Sect. 1, 2.1]; seven bands NUV, u, g, r, i, z, y and three slitless bands at R ≥ 200 over 255–1000 nm [src: Sect. 3.3]; g-band limit "not less than 26 mag" [src: Sect. 4.2] | none | not launched. The 2025 overview says "scheduled to be launched in 2027" [src: Sect. 1]; press listings in 2026 give no earlier than 2027 [sec: web] | CSST Collaboration 2025, arXiv:2507.04618 (body text, HTML version) |

Euclid release contents: Q1 holds 63.1 deg² of the deep fields and about 30
million objects (Euclid Collaboration: Aussel et al. 2025, arXiv:2503.15302)
[src: abstract]; DR1 (about 1900 deg², observations from 14 February 2024
to 21 May 2025, ESA Euclid pages) is detailed in `cosmo-galaxy-clustering`
and `cosmo-weak-lensing` [sec: GC, WL].

## 3. CMB experiments
<!-- key: cmb-experiments -->

All rows are carried over from `cosmo-cmb` unless flagged otherwise; that
skill holds the likelihoods, map depths per band and the data products.

| Experiment | Site, aperture | Bands, sky, depth | Releases | Status / next | Source |
|---|---|---|---|---|---|
| Planck | ESA satellite | nine bands 30–857 GHz, all sky; scanned 12 August 2009 to 23 October 2013. 2018 maps [src: Table 4]: effective beam FWHM 32.3′ (30 GHz) to 9.7′, 7.2′, 4.9′ at 100, 143, 217 GHz and 4.2′ at 857 GHz; white-noise temperature levels 1.29, 0.55, 0.78 μK_CMB deg at 100, 143, 217 GHz (polarisation 1.96, 1.17, 1.75). Mission paper (Planck Collaboration 2011, arXiv:1101.2022) [src]: launched 14 May 2009, surveying "since 13 August 2009" (the 2018 overview's 12 August is the date carried from `cosmo-cmb`) | 2013, 2015 (PR2), 2018 (PR3 "legacy"), PR4/NPIPE 2020 | closed; PR4-based likelihoods are current | arXiv:1807.06205 [sec: CMB] |
| ACT | Atacama | DR6: 98, 150, 220 GHz, 19,000 deg² mapped, median depth 10 μK-arcmin, data 2017–2022. DR6 body [src: Sect. II.1, II.8, Tables 1, 6]: three optics tubes, each a dichroic array with a 0.85° field; 852–1006 detectors per array and band; data 5 May 2017 to 2 July 2022, 46% observing efficiency, 48% of CMB data taken by day; night-time array sensitivity 8.4, 8.9 and 43 μK√s at f090, f150, f220, 6.1 combined; total weight about ten times DR4's. Telescope (Swetz et al. 2011, arXiv:1007.0290) [src]: six-metre off-axis Gregorian on Cerro Toco at 5190 m, commissioned 2007, first receiver three 1000-element arrays at 148, 218, 277 GHz | DR4 2020; DR6 maps and spectra March 2025, on LAMBDA | observations ended 2022; DR6 is the final cosmology release | arXiv:2503.14451 [sec: CMB] |
| SPT-3G | 10 m, South Pole | 95, 150, 220 GHz; Main field 1500 deg²; full survey about 10,000 deg². D1 (2019–2020) coadded white noise 3.3 μK-arcmin in T and 5.1 in polarisation; per band T 5.4, 4.4, 16.2 μK-arcmin (arXiv:2506.20707) [src: Sect. I, IV.5]. Receiver commissioned early 2017 on the 10 m SPT, multichroic (Sobrin et al. 2018, arXiv:1809.00032) [src] | D1 (2019–2020 Main field): spectra June 2025, maps public March 2026 | operating; SPT-3G+ receiver (24,080 detectors) planned for early 2029 | arXiv:2506.20707; arXiv:2608.20236 [sec: CMB] |
| BICEP/Keck, BICEP Array | small refractors, South Pole | one deep patch, effective area ≈ 600 deg² at 95 GHz and ≈ 400 deg² at 150 and 220 GHz; BK18 Q/U depths 2.8, 2.8 and 8.8 μK-arcmin at 95, 150 and 220 GHz [src: abstract] | BK18 (data through 2018) is the latest r constraint | next release uses data through 2024 [sec: CMB] | arXiv:2110.00483 |
| Simons Observatory | Cerro Toco, 5200 m; three 0.5 m SATs and one 6 m LAT | 27–280 GHz, 60,000 bolometers (**design**). 2018 **design** [src: Table 1] (5-year survey, 20% of time usable): SATs over f_sky = 0.1 with FWHM 91′ to 9′ and baseline (goal) polarisation noise 2.6 (1.9) and 3.3 (2.1) μK-arcmin at 93 and 145 GHz; LAT over f_sky = 0.4 with FWHM 2.2′, 1.4′, 1.0′ at 93, 145, 225 GHz and 8.0 (5.8), 10 (6.3), 22 (15) μK-arcmin | **no public data release**: a web search on 2026-10-09 found talks and commissioning papers only [sec: web] | SAT observations since late 2023; LAT first image 22 February 2025; six SATs by 2027; LAT upgrade by 2028 | arXiv:1808.07445; arXiv:2609.26938; arXiv:2503.00636 [sec: CMB] |
| CMB-S4 | was Chile + South Pole | — | — | **cancelled**: DOE and NSF withdrew support on 9 July 2025 | `cmb-s4.org`, read by `cosmo-cmb` on 2026-10-07 [sec: CMB] |
| LiteBIRD | JAXA satellite, L2 | after the 2024–2026 reformation: one 500 mm reflector, 12 bands 40–402 GHz, three-year survey, δr < 0.002 (**design**). Body [src: Sect. 2.2, 3.3, Table 1]: all-sky polarisation over 2 ≤ ℓ ≤ 200; required combined map noise < 8.0, < 10.0, < 10.0 μK-arcmin (LF, MF, HF) at 2 ≤ ℓ ≤ 29 and < 4.7, < 4.5, < 4.7 at 30 ≤ ℓ ≤ 200, defined from null maps; cross-Dragone telescope at about 5 K, one focal plane at 0.1 K; a rotating half-wave plate is the baseline under study, with a no-plate backup | — | passed Mission Definition Review #2 on 26 June 2026; launch JFY2036 (was "late 2020s") | arXiv:2607.25285 [sec: CMB] |

## 4. Time-domain surveys
<!-- key: time-domain-surveys -->

The supernova samples themselves (DES-SN, SNLS, PS1, Foundation, DEBASS,
compilations) are in `cosmo-supernovae`; this table holds the facilities.

| Survey | Telescope and camera | Strategy | Cosmology-relevant releases | Status / next | Source |
|---|---|---|---|---|---|
| ZTF | Palomar 48-inch Schmidt, 47 deg² field, 8 s readout | untargeted, g r i, public alert stream | SN Ia DR2: 3628 spectroscopically classified SNe Ia at z < 0.3 from March 2018 to December 2020, **not usable for cosmological parameters** until the scene-modelling reprocessing ("DR2.5") is out (arXiv:2409.04346) [sec: SN] | operating; NSF added USD 1.6 million in October 2024 for operations in 2025 and 2026; funding after 2026 was not confirmed by the search [sec: web] | Bellm et al. 2019, arXiv:1902.01932 [src: abstract of each] |
| ATLAS | four small telescopes [sec: SN] | all sky, two-day cadence; finds more bright (m < 19) SN candidates than any other ground survey | TITAN recalibration for SN Ia cosmology (see `cosmo-supernovae`) | operating | Tonry et al. 2018, arXiv:1802.00879 [src: abstract] |
| YSE | Pan-STARRS telescopes | griz, about 750 deg² every three days in 2020 with a plan for 1500 deg²; depth about 21.5 in gri and 20.5 in z; about 5000 SNe per year at full capacity (**forecast**) | low-z anchor sample named as forthcoming by the Unite authors [sec: SN] | cosmology sample size not verified | Jones et al. 2021, arXiv:2010.09724 [src: abstract] |
| Rubin LSST | Sect. 2.9 | pairs of visits per night; Wide-Fast-Deep plus Deep Drilling Fields; the footprint, nightly repeat visits in different filters and regular cadence each change the cosmological return across more than 100 simulated strategies | none yet | survey began 30 June 2026 [sec: WL] | arXiv:0805.2366; Lochner et al. 2022, arXiv:2104.05676 [src] |
| Roman HLTDS | Sect. 1.9 | wide 18.3 deg² and deep 6.5 deg² tiers, filter subsets every five days over about two years [sec: SN] | none | commissioning | arXiv:2505.10574 [src] |

## 5. Radio facilities
<!-- key: radio-facilities -->

| Facility | Site and hardware | Survey and cosmology use | Status / next | Source |
|---|---|---|---|---|
| CHIME | DRAO, Penticton; four 100 m × 20 m cylinders, 256 dual-polarisation feeds each; 400–800 MHz; drift scan covering 3/4 of the sky daily. Body (arXiv:2201.07869) [src: Sect. II.2, IV.1, Table 1]: f/0.25 parabolas, reflector surface 7.2 mm rms (λ/50 at 800 MHz); first light 7 September 2017, cosmology data from 7 October 2018; time lost to downtime 17%, daytime 50%, rain 20%, 69% in total; 42% of frequency channels lost to RFI | 21 cm intensity mapping at 0.8 < z < 2.5 for BAO; first interferometric detection by stacking on eBOSS tracers at 0.78 < z < 1.43 (102 nights; 7.1σ LRG, 5.7σ ELG, 11.1σ QSO); also FRBs | operating; auto-power spectrum detected at z ~ 1 from 94 nights, 12.5σ in the arXiv listing abstract and 12.4σ in the abstract of the v2 text (arXiv:2511.19620) [src: abstract] | CHIME Collaboration 2022, arXiv:2201.07869; arXiv:2202.01242 [src] |
| CHORD | DRAO; 512 six-metre dishes, 300–1500 MHz, drift scan; two 64-dish outriggers (Hat Creek, Green Bank) | 21 cm cosmology, FRB localisation, HI galaxies | 64-dish pathfinder in commissioning; "the full array will be commissioned in 2028" | CHORD Collaboration 2026, arXiv:2607.09374 [src: abstract] |
| MeerKAT / MeerKLASS | Karoo, South Africa; 64 dishes; L band and UHF band | single-dish (auto-correlation) HI intensity mapping; proposed as about 4000 deg² in about 4000 hours (**design**), in L band (0 < z < 0.58) or UHF band (0.4 < z < 1.45), with a **forecast** of 0.5–1% on Ω_HI b_HI at z = 0.1–0.5 and 1.1–4.2% at z = 0.6–1.4 [src: Sect. 3.1.1, Table 1]; cross-correlation detections with optical surveys and "continually improving" HI auto-power measurements | operating; the method is the template for SKA-Mid, whose Band 1 (350–1050 MHz) reaches z ≈ 3 | Santos et al. 2017, arXiv:1709.06099; Cunnington et al. 2026, arXiv:2606.25955 [src] |
| ASKAP / WALLABY | Western Australia; 36 twelve-metre dishes with phased-array feeds, about 30 deg² field at 1.4 GHz | WALLABY: HI over −90° < Dec < +30° to z < 0.26 at about 30″; more than half a million galaxies expected at mean z ≈ 0.05 (**forecast**, 2020). Peculiar-velocity use: `cosmo-peculiar-velocities` | 2025–2026 papers still carry the "pilot survey" label; the full-survey footprint as executed was not verified | Koribalski et al. 2020, arXiv:2002.07311 [src: abstract] |
| SKA (Phase 1) | SKA-Mid on the MeerKAT site in the Karoo (arXiv:2606.25955); SKA-Low in Australia (site not re-read) | **design** (2018 Red Book) [src: Sect. 2.1, 2.2, Table 2]: SKA1-Mid = MeerKAT's 64 dishes of 13.5 m plus 133 SKA dishes of 15 m, baselines to 150 km (about 0.3″ at 1.4 GHz); funded receivers Bands 1 (0.35–1.05 GHz, HI at 0.35 < z < 3), 2 (0.95–1.75 GHz, 0 < z < 0.5) and 5; MeerKAT's own UHF (580–1015 MHz) and L (900–1670 MHz) bands differ. SKA1-Low = 512 stations of 256 dipoles at 50–350 MHz, 224 in a 1 km core. Surveys: continuum weak lensing and HI galaxy survey over 5000 deg²; continuum and HI intensity mapping over 20,000 deg² at 0.35 < z < 3; deep intensity mapping over 100 deg² at 3 < z < 6 | under construction. SKAO timeline, version of February 2025: AA2 for SKA-Low 2026 Q4 and for SKA-Mid 2027 Q4, science verification from 2027, AA* 2028 Q3, operations readiness review 2029 Q1; a June 2024 table had the SKA-Mid AA2 in May 2027 [sec: web]. No 2026 confirmation that AA2 was reached | SKA Cosmology SWG 2018, arXiv:1811.02743 [src] |
| HIRAX | SKA site, South Africa; initial 256 six-metre dishes, 400–800 MHz; final 1024 | 21 cm intensity mapping at 0.775 < z < 2.55 over about 15,000 deg² (**design**) | "being deployed"; metrology of the first 28 dishes reported in July 2026 | Crichton et al. 2022, arXiv:2109.13755 [src: abstract]; Studer et al. 2026, arXiv:2607.26972 [src: abstract] |
| DSA-2000 | 2000 five-metre dishes, 0.7–2 GHz, 3.5″ resolution (**design**) | continuum "radio camera": sky above Dec −30° every four months for five years, more than a billion sources at 500 nJy/beam; about 10,000 localised FRBs per year (**forecast**) | proposed in 2019 "with a view to first light in 2026"; current status not verified | Hallinan et al. 2019, arXiv:1907.07648 [src: abstract] |

## 6. X-ray
<!-- key: x-ray -->

**eROSITA on SRG.** Launched 13 July 2019 from Baikonur; all-sky survey
began 13 December 2019 with six-month scans, eight planned by the end of
2023; soft band 0.2–2.3 keV, about 25 times more sensitive than ROSAT
(**design**) [src] (Predehl et al. 2021, arXiv:2010.03477). Hardware [src:
Sect. 3.1, 4.1, Tables 3, 4]: seven Wolter-I mirror modules of 54 nickel
shells, 1600 mm focal length, each with its own CCD camera; on-axis
resolution 16.1″ half-energy width at 1.5 keV on ground, about 18″ on axis
and 26″ averaged over the field after a deliberate 0.4 mm defocus; CCD
energy resolution 49–58 eV FWHM at 0.277 keV and 135–145 eV at 6.4 keV.
Only the western
Galactic hemisphere belongs to the German consortium and is released.
DR1 (January 2024): eRASS1, the first six months completed in June 2020,
nearly 930,000 sources, with calibrated event files, source products and
maps [src] (Merloni et al. 2024, arXiv:2401.17274). DR2 (news item of 31 July
2026): cumulative catalogues of the first three surveys (eRASS:3, 12 December
2019 to 16 June 2021), 1,911,744 point-like and 63,796 extended sources in
0.2–2.3 keV, **catalogue-only** [src] (Ramos-Ceja et al. 2026,
arXiv:2607.27772; `erosita.mpe.mpg.de/dr2`). The DR2 paper quotes a field
of about 1° diameter, effective area peaking near 1365 cm² at 1 keV, HEW
about 18″ on axis and 30″ field-averaged in 0.2–2.3 keV, and an eRASS1
median sensitivity of about 5 × 10⁻¹⁴ erg cm⁻² s⁻¹ (0.5–2 keV, about 50%
completeness); its astrometric calibration file covers eRASS1–eRASS5, so
data of at least five passes exist in the pipeline; its milestone table
lists safe-mode switch-offs at major orbit corrections and micrometeoroid
hits on four cameras during eRASS2–3 [src: Sect. 1, 3.1.4]. Cluster cosmology still rests on
eRASS1: 12,247 clusters and groups over 13,116 deg² (arXiv:2402.08452)
[sec: CL]; see `cosmo-clusters`. The DR2 material describes three complete
surveys, not the eight planned; the reason for the end of the survey is not
given in the sections read.

## 7. Gravitational-wave detectors
<!-- key: gravitational-wave-detectors -->

| Facility | Configuration | Data and catalogues | Status / next | Source |
|---|---|---|---|---|
| LIGO–Virgo–KAGRA | two LIGO detectors, Virgo, KAGRA. Instrument papers [src: abstract of each]: Advanced LIGO (LIGO Scientific Collaboration 2015, arXiv:1411.4547), two identical 4 km Michelson interferometers with Fabry–Perot arms, power and signal recycling, design strain sensitivity ten times initial LIGO near 100 Hz and band edge moved from 40 to 10 Hz; Advanced Virgo (Acernese et al. 2015, arXiv:1408.3978), aiming at three orders of magnitude more observable galaxies than Virgo | GWTC-4.0: O4a (24 May 2023 to 16 January 2024), 128 new candidates, 218 in total with the 90 of GWTC-3.0. GWTC-5.0 (papers from May 2026): through O4b, 267 mergers in the population analysis, no new source containing a neutron star | O4 ended 18 November 2025 [sec: web, AEI and ICRR pages]. Plan page updated 3 September 2026: detectors "in a period of upgrades and commissioning"; a six-month Intermediate Run 1 planned from "early- to mid-November of 2026"; O5 plans "in discussion", no date | LVK 2025, arXiv:2508.18082 [src: abstract]; LVK 2026, arXiv:2605.27226 [src: abstract]; `observing.docs.ligo.org/plan` (plan-page wording and dates; not a paper) |
| Einstein Telescope | **design**: single-site triangle or two L-shaped detectors | — | candidate sites Sardinia, Euregio Meuse-Rhine, Saxony (Lusatia); site decision expected in 2027; not before 2035 [sec: web] | Abac et al. 2025, arXiv:2503.12263 [src] |
| Cosmic Explorer | **design**: two L-shaped detectors in the United States, 20 km and 40 km arms | — | "As of 2025, CE is in its design phase, with plans to begin operations in the 2030s" | Datrier et al. 2025, arXiv:2509.05430 [src: abstract] |
| LISA | three spacecraft, 0.1 mHz to 1 Hz | — | adopted by ESA on 25 January 2024; launch planned for 2035 [sec: web] | Colpi et al. 2024, arXiv:2402.07571 [src: abstract] |

Standard-siren cosmology with these data is in `cosmo-multimessenger` and
`cosmo-distance-ladder-h0`.

## Not verified
<!-- key: not-verified -->

- Values corrected in the numbers run of 2026-10-24/25 (the paper's value
  is now quoted): the CHIME auto-spectrum was given as 12.5σ; the arXiv
  listing abstract says 12.5σ and the abstract of the v2 text 12.4σ
  (arXiv:2511.19620). The eBOSS Lyα sample was given as "120,000 quasars";
  the abstract states 60,000 new plus 60,000 re-observed (arXiv:1508.04473).
  The BICEP/Keck patch was given as "about 400–600 deg²"; the abstract
  gives ≈ 600 deg² at 95 GHz and ≈ 400 deg² at 150 and 220 GHz
  (arXiv:2110.00483). MUST was given as "more than 100 million galaxies and
  quasars to z ≈ 5.5"; the paper gives more than 100 million in total and up
  to 40 million at 2 < z < 5.5 (arXiv:2605.10102). A BICEP/Keck forecast
  σ(r) ≈ 0.005 for the next release was removed (no paper and place read).
- Public release date of the DESI DR2 spectra; the definition, schedule and
  funding status of DESI-II.
- Whether the 4MOST main survey and the WEAVE multi-object surveys have
  formally started (latest official wording: "imminent", 15 June 2026, and
  "expected ~ April 2026"); MOONS science-operations date.
- Roman arrival at L2; the Roman WFI body specifications (arXiv:1902.05569
  has no HTML or LaTeX source readable here). (HLWAS tier areas and depths:
  closed by arXiv:2505.10574, Sect. II; Euclid telescope aperture: closed,
  1.20 m, arXiv:2405.13493 Sect. 2.)
- 4MOST overview body (arXiv:1903.02464 has no HTML or LaTeX source
  readable here): fibre size and positioning specification.
- Rubin DR1 date; whether the full DP2 has been released.
- Legacy Surveys DR11 release day; later HSC-SSP and UNIONS public releases;
  KiDS-Legacy shear-catalogue access.
- The CFHT Board text on MSE (the page fetched did not show it); MUST site;
  Spec-S5 approval status and schedule.
- Simons Observatory first data release date; ACT decommissioning date.
- ZTF funding after 2026; ATLAS and YSE cosmology-sample sizes.
- WALLABY full-survey footprint;
  current SKAO array-assembly dates (the schedule is revised monthly);
  DSA-2000 funding and schedule; LOFAR, FAST, GBT, Tianlai and BINGO were
  not researched.
- Why eROSITA stopped after fewer surveys than planned (the DR2 paper
  shows data through at least eRASS5 in its pipeline, Sect. 3.1.4, but the
  sections read give no reason); any release of the eastern
  (Russian-consortium) hemisphere.
- LVK O4 detector sensitivities (the GWTC-4.0 body could not be read); the
  LiteBIRD beam widths (garbled in the rendering of arXiv:2607.25285).
- The O5 schedule (a web summary of an older announcement says 2028, the
  current plan page gives no date); LIGO-India; ET and CE funding.
