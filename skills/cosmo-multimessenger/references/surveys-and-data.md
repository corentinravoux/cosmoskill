# Surveys and data — gravitational-wave detectors and catalogues, galaxy catalogues, FRB facilities, lensed-transient samples

Scope: every detector run, catalogue and sample that enters multi-messenger cosmology, past to planned, with status at the snapshot date.
Snapshot: 2026-10-13 (deepening pass, 12–13 October; first build 2026-10-07, searches 2026-10-10)

Provenance flags as in the other files. Instrument descriptions of LIGO–Virgo–KAGRA,
CHIME, MeerKAT and SKA are in `cosmo-surveys-facilities`; this file holds what a
cosmological analysis needs: which events, which catalogue, how complete.

## 1. Gravitational-wave detector runs and catalogues
<!-- key: gravitational-wave-detector-runs-and-catalogues -->

### 1.1 Runs
<!-- key: runs -->

| Run | Dates (UTC) | Catalogue | Content | Source |
|---|---|---|---|---|
| O1, O2 | not read this session | GWTC-1 | includes GW170817 (O2) and GW170814 | arXiv:1908.06060 |
| O3a | not read this session | GWTC-2, GWTC-2.1 | includes GW190814, GW190521 | arXiv:2101.12660 |
| O3b | 2019-11-01 15:00 to 2020-03-27 17:00 [src] | GWTC-3 | 35 new candidates with `p_astro > 0.5`; 90 in total over O1–O3 [src] | arXiv:2111.03606 |
| O4a | 2023-05-24 15:00 to 2024-01-16 16:00 [src] | GWTC-4.0 | 128 new candidates with `p_astro ≥ 0.5`, 86 with false-alarm rate below 1 yr⁻¹; 218 in total [src] | arXiv:2508.18082 |
| O4b | 2024-04-10 15:00 to 2025-01-28 17:00, plus four days of engineering run from 2024-04-06 [src] | GWTC-5.0 | 161 new candidates, all consistent with BBH, 104 with false-alarm rate below 1 yr⁻¹; O1–O4a re-analysed to 229; cumulative 390 with `p_astro ≥ 0.5` [src] | arXiv:2605.27225 |
| O4c | 2025-01-28 to 2025-11-18 [der: end of O4b to end of O4] | none yet | data "under detailed examination" at the end of the run [sec: LVK announcement] | LVK news item, see below |
| IR1 | planned six-month run "beginning early- to mid-November of 2026" [src] | — | Virgo joins with possible interruptions; KAGRA joins later as available [src] | LVK observing-plan page |
| O5 | no date: "plans and timeline … are being refined" [src] | — | — | LVK observing-plan page |

Official pages read on 2026-10-10: the LVK observing plan,
`https://observing.docs.ligo.org/plan/` (last updated 3 September 2026, next update
announced for 15 October 2026 or sooner), and, through a web search, the LVK
announcement "LIGO-Virgo-KAGRA Collaboration successfully wraps up its fourth Observing
Run" on `ligo.org`, which gives the O4 span as 24 May 2023 to 18 November 2025 and
about 250 candidates observed in real time [sec]. The O4c boundaries are inferred from
those two dates and were not read on a page that names O4c.

### 1.2 Three different "sizes" of GWTC-5.0
<!-- key: three-different-sizes-of-gwtc-5-0 -->

A count without its definition is the most common error with this catalogue.

| Number | What it counts | Source |
|---|---|---|
| 390 | cumulative candidates with `p_astro ≥ 0.5`, not vetoed | arXiv:2605.27225 |
| "over 300" | merging binaries, as worded in the introduction paper of the release [sec: abstract of the GWTC-5.0 introduction paper, seen in a title search] | — |
| 267 | mergers used for the population analysis | arXiv:2605.27226 |
| 236 | sources used for cosmology | arXiv:2605.27227 |
| 235 | BBH used in an external spectral-siren analysis | arXiv:2609.25662 |

For GWTC-4.0 the corresponding numbers are 218 candidates and 142 used for cosmology
(arXiv:2509.04348); an external analysis states the cosmology cut as a false-alarm rate
below 0.25 yr⁻¹ (arXiv:2601.03257) [src]. For GWTC-3: 90 candidates, 47 used for
cosmology (arXiv:2111.03604) [src].

### 1.3 Events that carry the cosmological information
<!-- key: events-that-carry-the-cosmological-information -->

| Event | Why it matters | Source |
|---|---|---|
| GW170817 | the only confident bright siren: BNS, counterpart within about 10 arcsec of NGC 4993 [src]; `d_L = 43.8 (+2.9/−6.9)` Mpc [sec: arXiv:1909.08627 §6.1]; host distance 40.7 ± 1.4 ± 1.9 Mpc from surface-brightness fluctuations [src: arXiv:1801.06080] | arXiv:1710.05835 |
| GW170814 | first BBH dark siren with a deep photometric catalogue (DES) | arXiv:1901.01540 |
| GW190814 | best-localised event of GWTC-3; the only GWTC-3 event whose H0 information does not rest on the mass model [src]; gives 3.4σ of the 5.9σ cross-correlation peak [src] | arXiv:2111.03604, arXiv:2512.15380 |
| GW190521 | candidate counterpart ZTF19abanrhr at `z = 0.438` [src]; association not established | arXiv:2009.14199, arXiv:2009.14057 |
| GW230518, GW230529 | NSBH candidates in O4a [src]; no counterpart | arXiv:2508.18082 |
| GW230814, GW231226 | first BBH with network signal-to-noise above 30 [src] | arXiv:2508.18082 |
| GW250114_082203 | loudest signal to date, signal-to-noise 76.9 [src]; in O4b by its date | arXiv:2605.27225 |

No new source containing a neutron star is in the GWTC-5.0 population sample
(arXiv:2605.27226) [src], and the neutron-star merger rate estimates decreased after the
latest run (arXiv:2609.12053) [src]. Nine years after GW170817 there is still one bright
siren.

### 1.4 Public data
<!-- key: public-data -->

Catalogue papers are arXiv:2111.03606 (GWTC-3), arXiv:2508.18082 (GWTC-4.0) and
arXiv:2605.27225 (GWTC-5.0). The data-release location (GWOSC, Zenodo records of the
cosmology papers) was not read this session; see "Not verified".

## 2. Galaxy catalogues used for dark sirens
<!-- key: galaxy-catalogues-used-for-dark-sirens -->

| Catalogue | Type | Completeness and depth as quoted | Used in | Source |
|---|---|---|---|---|
| GLADE+ | all-sky compilation of six catalogues (GWGC, 2MPZ, 2MASS XSC, HyperLEDA, WISE×SCOS photo-z, SDSS DR16Q) [src] | complete to `d_L = 47 (+4/−2)` Mpc in total B-band luminosity; holds the brightest galaxies giving 90% of B- and K-band luminosity to about 130 Mpc [src] | GWTC-3, GWTC-4.0, GWTC-5.0 (alternative), Peak Sirens | arXiv:2110.06184 |
| GLADE (previous version) | all-sky | — | GWTC-2 dark sirens | arXiv:2101.12660 |
| DES Y3 photo-z | photometric | — | GW170814 | arXiv:1901.01540 |
| DES Y6 Gold | photometric; restricted to `0.05 < z < 0.50` to keep the galaxy distribution consistent with uniform in comoving volume [src] | — | GWTC-4.0 external analysis; fiducial catalogue of GWTC-5.0 with luminosity weighting [src] | arXiv:2602.04766, arXiv:2605.27227 |
| DESI Legacy Imaging Survey | photometric, photo-z PDFs from a deep-learning model [src] | magnitude-limited; incompleteness modelled in the 2026 analysis [src] | 8, 15, then 17 well-localised dark sirens | arXiv:2111.06445, arXiv:2404.16092, arXiv:2603.20195 |
| DELVE | photometric (DECam) | — | GW190924_021846, GW200202_154313 | arXiv:2310.13695 |
| 2MPZ, WISE×SuperCOSMOS | photometric, all-sky | — | GWTC-3 cross-correlation | arXiv:2203.03643 |
| DESI spectroscopy around NGC 4993 | spectroscopic, dedicated | 39 group galaxies, five times more than before [src] | GW170817 host environment | arXiv:2512.08818 |
| HETDEX internal release 5 (VIRUS) | spectroscopic, integral-field | "exquisite completeness within z = 0.2" [src] | **forecast** for follow-up of golden and silver sirens | arXiv:2512.21729 |

The mismatch that defines the field: GLADE+ is complete to 47 Mpc, while the
dark-siren constraint of GWTC-4.0 is most data-driven at `z = 0.44` (arXiv:2511.11795)
[src]. The LVK statement for GWTC-3 was that the catalogue result "is strongly
impacted by assumptions about the BBH source mass distribution" (arXiv:2111.03604), and
for GWTC-5.0 that "the main driver of the Hubble constant measurement remains the
presence of features in the mass distribution" (arXiv:2605.27227 §4.1) [src].

Depth actually required (**forecasts** on mocks): complete spectroscopy to `r ≈ 19` for
the ten best-localised events per year (arXiv:2607.17284); or only the brightest 1% of
galaxies, `M_i < −22.43`, if hosts live in haloes above `2 × 10^11 h⁻¹ M☉` and the events
are well localised (arXiv:2511.04786) [src].

### 2.1 Peculiar-velocity products applied to a siren host
<!-- key: peculiar-velocity-products-applied-to-a-siren -->

| Product | Used by | Source |
|---|---|---|
| 6dFGSv Fundamental Plane velocities (more than 8000 galaxies, `z ≲ 0.055`) [src] | LVC 2017 | arXiv:1710.05835 |
| Cosmicflows-3, 2MTF, 6dFGSv with several group catalogues | Howlett & Davis | arXiv:1909.00587 |
| BORG reconstruction on 2M++ | Mukherjee et al.; also shipped in GLADE+ for `z < 0.05` | arXiv:1909.08627, arXiv:2110.06184 |
| 2M++ linear reconstruction (within 200 h⁻¹ Mpc) [src] | cross-check in LVC 2017 | arXiv:1504.04627 |
| DESI Fundamental Plane; Cosmicflows-4 surface-brightness-fluctuation distance of NGC 4993 | Amsellem et al. | arXiv:2512.08818 |

Survey descriptions and the current state of these velocity data are in
`cosmo-peculiar-velocities`.

## 3. Fast-radio-burst facilities and localised samples
<!-- key: fast-radio-burst-facilities-and-localised -->

### 3.1 Facilities and catalogues
<!-- key: facilities-and-catalogues -->

| Facility / sample | Band, localisation | Sample | Status | Source |
|---|---|---|---|---|
| CHIME/FRB Catalog 1 | 400–800 MHz | 536 bursts, 2018-07-25 to 2019-07-01, 62 from 18 repeaters; sky rate 525 ± 30 (stat) +140/−130 (sys) per sky per day above 5 Jy ms at 600 MHz [src] | superseded | arXiv:2106.04352 |
| CHIME/FRB Catalog 2 | 400–800 MHz, `O(10')` positions, 0.983 ms resolution [src] | 4539 bursts from 3641 sources, 2018-07-25 to 2023-09-15, 981 bursts from 83 repeaters; all Catalog 1 events reprocessed [src] | current | arXiv:2601.09399 |
| ASKAP / CRAFT | arcsecond localisation | 16 localised bursts in the 2022 H0 analysis, with 60 unlocalised from Parkes and ASKAP [src] | operating | arXiv:2208.00819 |
| DSA-110 | arcsecond localisation with host association in Pan-STARRS1 [src] | 11 bursts in the first catalogue; 30 hosts in the 2024 host study [src] | operating | arXiv:2307.03344, arXiv:2409.16964 |
| FLIMFLAM DR1 | foreground spectroscopy | 8 sightlines [src] | first release | arXiv:2402.00505 |
| DSA (with Chronoscope backend) | 1650 antennas of 6.15 m, 0.7–2 GHz, Nevada; localisation ≲ 250 mas [src] | **forecast**: about `10^4` bursts per year per sub-band, about `10^5` over the nominal five-year survey [src] | planned | arXiv:2608.30943 |

CHIME outrigger stations for VLBI localisation appear in 2025–2026 titles on arXiv; no
paper on them was read (see "Not verified").

### 3.2 Growth of the localised sample used for cosmology
<!-- key: growth-of-the-localised-sample-used-for -->

| Year of analysis | Localised bursts used | Source |
|---|---|---|
| 2020 | published sample plus four new (`z` = 0.291, 0.118, 0.378, 0.522) [src] | arXiv:2005.13161 |
| 2021 | 9 | arXiv:2104.04538 |
| 2021 | 14 | arXiv:2108.00581 |
| 2022 | 16 (with 60 unlocalised) | arXiv:2208.00819 |
| 2023 | 21 (with 57 unlocalised) [der: 78 − 21] | arXiv:2305.07022 |
| 2025 | 61 | arXiv:2506.04186 |
| 2025 | 124 | arXiv:2506.03536 |
| 2025 | 95 used of 117 | arXiv:2507.18946 |
| 2026 | 133 (cross-correlation with 2MASS) | arXiv:2601.21336 |
| 2026 | 130 (cross-correlation with the DESI Legacy Bright Galaxy Sample) | arXiv:2608.11296 |
| 2026 | 2124 unlocalised, CHIME Catalog 2 | arXiv:2604.03769 |

The localised sample grew by an order of magnitude between 2021 and 2025. It is a
heterogeneous union of surveys with different selection functions, which is why the
survey-forward-modelling likelihood exists (physics file, §7.3).

### 3.3 Hosts
<!-- key: hosts -->

FRB hosts are not a fair sample of star-forming galaxies: Sharma et al. 2024
(arXiv:2409.16964) find a deficit of low-mass hosts [src], while James et al. 2026
(arXiv:2609.04765) find that ASKAP bursts prefer hosts fainter than star formation
predicts [src]. The two statements use different samples and weighting; the host
population model is part of the cosmological likelihood through `DM_host`.

## 4. Lensed transients
<!-- key: lensed-transients -->

| Object | Type, source redshift | Lens | Delay data | H0 paper |
|---|---|---|---|---|
| SN Refsdal | multiply imaged supernova; reappearance observed in 2015 as predicted [src] | massive galaxy cluster, MACS J1149 [src: arXiv:2305.06367, Supplementary] | reappearance delay | arXiv:2305.06367, arXiv:2509.09979 |
| SN H0pe | Type Ia, `z = 1.78`, three images [src] | cluster PLCK G165.7+67.0, `z = 0.35` [src] | JWST photometry and spectroscopy, two relative delays [src] | arXiv:2403.18902 |
| SN Encore | Type Ia, `z = 1.95` [src] | cluster MACS J0138.0−2155 [src] | `Δt = −39.8 (+3.9/−3.3)` days [src] | arXiv:2509.12301 |
| SN Requiem | sibling of Encore in the same host; a fourth image is expected within a few years [src] | same cluster | pending | arXiv:2509.12301 |
| SN 2025wny | Type I superluminous, `z = 2.015`, first of its class to be strongly lensed; four deblended images [src] | galaxy-scale lens | `Δt_AB = −10.6 (+2.2/−2.5)` days photometric [src] | arXiv:2608.28427 |
| TDCOSMO-2025 | 8 lensed quasars, with 11 SLACS and 4 SL2S non-time-delay lenses [src] | galaxy-scale lenses | long-term monitoring | arXiv:2506.03023 |

Three lensed supernovae had given H0 by September 2025 (Refsdal, H0pe, Encore;
arXiv:2509.12301) [src]; SN 2025wny is the fourth, and the only galaxy-scale system
with an H0 among the papers read. Lensed quasars are covered in `cosmo-distance-ladder-h0`. No lensed
gravitational-wave event and no lensed FRB has produced a cosmological measurement; the
literature on both is forecasts (open-questions file).

## 5. Planned: detector upgrades, third generation, LISA, radio
<!-- key: planned-detector-upgrades-third-generation-lisa -->

| Facility | What is planned | Cosmology case | Source |
|---|---|---|---|
| LIGO A+ and A# with LIGO-India | detector networks assumed in 2026 forecasts: Hanford–Livingston–Virgo at A+; Hanford–Livingston–India at A# [src] | dark sirens with spectroscopic follow-up | arXiv:2607.17284 |
| Einstein Telescope | European third-generation observatory; two geometries under study, a single-site triangle or two L-shaped detectors [src] | bright sirens to `z > 1`, spectral sirens | arXiv:2503.12263 |
| Cosmic Explorer and networks | next-generation networks compared for bright, golden dark and spectral sirens | sub-percent `H(z)` (**forecast**) | arXiv:2402.03120 |
| LISA | extreme-mass-ratio inspirals at `z ≲ 1` with galaxy redshifts, massive black-hole binaries at `z ≳ 1` with counterparts [src] | H0 and `w0` (**forecast**) | arXiv:2603.23612 |
| DSA with Chronoscope | see §3.1 | baryon distribution below 10 Mpc scales | arXiv:2608.30943 |
| Wide-field multi-object spectroscopy in the 2040s | host redshifts for bright and dark sirens | photometric redshifts degrade constraints by up to an order of magnitude (**forecast**) [src] | arXiv:2512.18369 |

Status and dates of the Einstein Telescope, Cosmic Explorer and LISA projects (site
decision, adoption, launch) were not read on official pages this session.

## Not verified
<!-- key: not-verified -->

- Dates of O1, O2 and O3a, and the content of GWTC-1 and GWTC-2, were not read.
- The O4c start and end are inferred, not read on a page naming O4c.
- The ICRR page returned by the web search is reported to say that O5 "is currently
  planned to start in 2028"; the official observing-plan page gives no date. Treat 2028
  as unconfirmed.
- Binary-neutron-star ranges of each detector in O4 and the O5 targets: the plan page
  shows them only in a figure.
- GWOSC and Zenodo release locations.
- CHIME/FRB outriggers, MeerTRAP, CRACO, FAST, CHORD and DSA-2000 as FRB localisers:
  not researched. CHORD's schedule is in `cosmo-surveys-facilities`.
- SN Zwicky and iPTF16geu (galaxy-scale lensed Type Ia supernovae with short delays)
  were not fetched.
- Closed on 2026-10-13: the cluster lensing SN Refsdal is MACS J1149 (§4).
- Einstein Telescope, Cosmic Explorer and LISA project milestones.
