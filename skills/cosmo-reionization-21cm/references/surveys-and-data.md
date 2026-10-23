# Surveys and data — reionisation, 21 cm, line-intensity mapping

Scope: experiments and data releases, past, current and planned.
Snapshot: 2026-10-13

Instrument facts here are those stated in the cited papers. Apertures, element counts and sites
that were not read at source are left out and listed under "Not verified". General facility
facts for CHIME, MeerKAT, SKA and SPHEREx also live in `cosmo-surveys-facilities`.

## 1. Global-signal experiments
<!-- key: global-signal-experiments -->

| Experiment | Band | What it published | Status on the snapshot date | Citation | Flag |
|---|---|---|---|---|---|
| EDGES (2010 result) | 100–200 MHz, all-sky spectrum | lower limit Δz > 0.06 on the duration of reionisation (95%) | first global-signal constraint | Bowman & Rogers 2010, arXiv:1209.1117 | [src: abstract] |
| EDGES low-band | profile at 78 MHz | claimed absorption profile (2018) | raw data of earlier papers and the full calibration pipeline made public in May 2026 | Bowman et al. 2018, arXiv:1810.05912; Murray et al. 2026, arXiv:2605.16643 | [src] |
| SARAS 3 | 55–85 MHz radiometer | non-detection; rejects the EDGES best-fit profile at 95.3% | the only direct test of EDGES | Singh et al. 2021, arXiv:2112.06778 | [src: abstract] |
| LEDA, BIGHORNS, SARAS (earlier generations) | — | have published global-signal data | — | listed in HERA Collaboration 2025, arXiv:2511.21289, introduction | [sec] |
| REACH, RHINO, MIST, PRIZM | — | described as "upcoming" in November 2025 | no sky result found in the date-sorted search of 2026-10-10 | arXiv:2511.21289, introduction | [sec] |

The HERA collaboration summarises the SARAS 3 result as a non-detection "with a confidence level
of 2σ" [src: arXiv:2511.21289, introduction]; the SARAS paper's own wording is 95.3% [src:
arXiv:2112.06778].

## 2. Epoch-of-reionisation interferometers
<!-- key: epoch-of-reionisation-interferometers -->

### Past
<!-- key: past -->

| Experiment | Outcome | Citation | Flag |
|---|---|---|---|
| GMRT EoR | completed; its first limit was revised after signal loss in the foreground filter was found | named in arXiv:2511.21289; case study in Liu & Shaw 2019, arXiv:1907.08211, section 12.5 | [sec] |
| PAPER (64-antenna configuration) | completed; original limits withdrawn for signal loss; final limits from a lossless re-analysis over z ~ 7.5–11 | Cheng et al. 2018, arXiv:1810.05175; Kolopanis et al. 2019, arXiv:1909.02085 | [src] |

### Current
<!-- key: current-2 -->

| Experiment | Configuration and data, as stated in the papers | Latest limits paper | Flag |
|---|---|---|---|
| HERA Phase I | fewer than 60 antennas, repurposed PAPER dipoles, 100–200 MHz; observing season 2017–2018; 18 nights (~36 h) then the full 94 nights | HERA Collaboration 2022, arXiv:2210.04912 (first: arXiv:2108.02263) | [src] |
| HERA Phase II | new signal chain, correlator and Vivaldi feeds; band 47–234 MHz (z = 5.1–29.3); 180 dual-polarisation antennas online in the two-week October 2022 data set analysed; eight bands over 5.6 ≤ z ≤ 24.4 | HERA Collaboration 2025, arXiv:2511.21289 | [src] |
| LOFAR (high band) | North Celestial Pole field, 10 nights reprocessed, z ≈ 8.3, 9.1, 10.1 | Mertens et al. 2025, arXiv:2503.05576; nights from Ghara et al. 2025, arXiv:2505.00373 | [src] |
| LOFAR, second field | 3C196 field (an ≈ 80 Jy source at the centre); one 6-hour night analysed, z = 9.16 | Ceccotti et al. 2025, arXiv:2504.18534 | [src: abstract] |
| MWA | EoR0 field (RA 0h, Dec −27°), data collected 2013–2023, 268 h retained, z = 6.5, 6.8, 7.0 | Nunhokee et al. 2025, arXiv:2505.09097; Trott et al. 2025, arXiv:2508.04164 | [src] |
| NenuFAR | Cosmic Dawn; four nights on a field chosen to minimise sidelobe leakage; 26.1 h at z = 20.3 and 23.6 h at z = 17.0 | Munshi et al. 2025, arXiv:2507.10533 | [src: abstract] |
| LWA, uGMRT | listed as ongoing | arXiv:2511.21289, introduction | [sec] |

Notes.

- HERA Phase II newly covers the EDGES band and the tail end of reionisation at z = 5–6 [src:
  arXiv:2511.21289, introduction].
- The MWA limits come from one field and one decade of data with strict data-quality cuts; the
  2025 "Gaussian information" paper re-uses the same 268 hours [src: arXiv:2508.04164]. [src: abstract]
- No interferometer has published a detection. Every number in section 3 of `results.md` is an
  upper limit.

## 3. Post-reionisation HI intensity-mapping instruments
<!-- key: post-reionisation-hi-intensity-mapping -->

### Past and pathfinding
<!-- key: past-and-pathfinding -->

| Instrument | Data | Result type | Citation | Flag |
|---|---|---|---|---|
| Green Bank Telescope | 0.6 < z < 1; ~41 deg², 190 h (2012); 100 deg² (2021) | cross-correlation with WiggleZ and eBOSS | Masui et al. 2012, arXiv:1208.0331; Wolz et al. 2021, arXiv:2102.04946 | [src] |
| Green Bank Telescope, first maps | z = 0.53–1.12 | stack on ~10⁴ DEEP2 galaxies, ~4σ; then auto-power as an upper bound (0.6 < z < 1, ~41 deg², 190 h) | Chang et al. 2010, arXiv:1007.3709; Switzer et al. 2013, arXiv:1304.3712 | [src] |
| Parkes | 0.057 < z < 0.098, ~1300 deg² in two fields | cross-correlation with 2dF, 5.18σ; also stacking on galaxies | Anderson et al. 2018, arXiv:1710.00424; named in Cunnington et al. 2026, arXiv:2606.25955, section 3 | [src] |

### Current
<!-- key: current -->

| Instrument | Mode | Data sets used in results | Citation | Flag |
|---|---|---|---|---|
| CHIME | drift-scan interferometer | 102 nights stacked on eBOSS LRG, ELG, QSO (0.78 < z < 1.43); 88 days in 400–500 MHz × eBOSS Lyα forest (1.8 < z < 2.5); 94 nights in 608.2–707.8 MHz for the auto-spectrum (z = 1.01–1.34) | arXiv:2202.01242, arXiv:2309.04404, arXiv:2511.19620 | [src] |
| MeerKAT (MeerKLASS) | 64 dishes in single-dish (total-power) mode, L-band | pilot: ~10 h, ~200 deg², 973–1015 MHz, × WiggleZ 11hr field (4031 galaxies); deep field (2021): ~40 h, 971.2–1023.6 MHz, × GAMA G23 (2269 galaxies), ~236 deg² for the auto-spectrum | Cunnington et al. 2022, arXiv:2206.01579; arXiv:2606.25955, section 3; MeerKLASS Collaboration 2026, arXiv:2610.12158 | [src] |
| MeerKAT, interferometric mode | DEEP2 and MIGHTEE fields | small-scale HI power: tentative detection and upper limits | Mazumder et al. 2026, arXiv:2606.24730 | [src] |
| MeerKAT, interferometric mode, L-band | z ≈ 0.32 and 0.44, foreground avoidance | auto-power on Mpc scales, 3.2–9.18σ depending on the flagging scheme | Paul et al. 2023, arXiv:2301.11943 | [src: abstract] |
| Tianlai cylinder pathfinder | drift scan | 20 days, 714.4–781.7 MHz (z ≈ 0.82–0.99), drone-measured beam | Deng et al. 2026, arXiv:2604.27465 | [src: abstract] |

Notes.

- Both MeerKLASS L-band data sets span only the RFI-free range 0.39 < z < 0.46 and ~200 deg²
  [src: arXiv:2606.25955, section 3].
- MeerKLASS counts three cross-correlation detections with galaxy surveys and a stacking
  detection on GAMA galaxies (8.66σ as an angular map, 7.45σ as a spectrum); the stacked
  spectrum shows an oscillating systematic at the frequency of the MeerKAT primary-beam ripple
  [src: arXiv:2606.25955, section 3].
- An HI auto-power detection with MeerKAT as an interferometer, on small non-linear scales,
  preceded the single-dish one [src: Paul et al. 2023, arXiv:2301.11943; sec: arXiv:2606.25955,
  section 3].

### Under construction
<!-- key: under-construction -->

| Instrument | Design as stated | Status | Citation | Flag |
|---|---|---|---|---|
| CHORD | 512 six-metre dishes in a core at the Dominion Radio Astrophysical Observatory, 300–1500 MHz, drift scan; two 64-dish outriggers at Hat Creek and Green Bank | three-dish engineering array evaluated; 64-dish pathfinder being commissioned; "The full array will be commissioned in 2028" | The CHORD Collaboration 2026, arXiv:2607.09374 | [src: abstract] |
| HIRAX | six-metre fibreglass dishes with f/D = 0.21, at the SARAO SKA site in South Africa; target redshift 0.78–2.55 | "being deployed"; metrology of the first 28 dishes published; surface accuracy within requirements, feed-placement precision not yet | Studer et al. 2026, arXiv:2607.26972 | [src: abstract] |
| SKA-Mid | Band 1 covers 350–1050 MHz; the "Wide" HI survey assumes AA4, z = 0.35–3, 20,000 deg², 10,000 h | under construction on the Karoo site next to MeerKAT | arXiv:2606.25955; Wolz et al. 2026, arXiv:2607.03259, section 2.1 | [src] |
| SKA-Low | the "Deep" HI survey assumes AA4, 100 deg², ~5,000 h, 200–350 MHz (3 < z < 6) | under construction [sec: web search of SKAO documents, below] | arXiv:2607.03259, section 2.1 | [src] |

SKA staging, from a web search of SKAO documents on 2026-10-10 (https://www.skao.int,
staged-delivery document SKAO-TEL-0002299) [sec]: the array assemblies are AA0.5, AA1, AA2, AA*
and AA4; construction pauses at AA*, which comprises 144 dishes (80 SKA-Mid dishes with the 64
MeerKAT dishes) and 307 SKA-Low stations; AA2 is the start of science verification. The dates
found disagree between SKAO documents (AA* in 2028 on one page, 2029 in another) and the SKAO
timeline page could not be opened; no date is given here.

## 4. Line-intensity mapping experiments (CO, [CII], Lyα)
<!-- key: line-intensity-mapping-experiments-co-cii -->

| Experiment | Line and redshift | Survey | Status | Citation | Flag |
|---|---|---|---|---|---|
| COPSS (Sunyaev-Zel'dovich Array) | CO(1–0) at z = 2.3–3.3 | 19 fields, 0.7 deg², 27–35 GHz, k = 0.5–10 h Mpc⁻¹; observed 2013–2015 | completed; P_CO > 0 at 98.9% | Keating et al. 2016, arXiv:1605.03971 | [src: abstract] |
| mmIME (ALMA ASPECS + Atacama Compact Array) | CO(2–1), (3–2), (4–3) at z ~ 1–5, 3 mm | Hubble Ultra Deep Field and COSMOS; ACA data from 2016–2018 | shot power detected, zero rejected at 99.99% | Keating et al. 2020, arXiv:2008.08087 | [src: abstract] |
| Planck 545 GHz × SDSS | [CII] at z = 2–3.2 | cross-correlation with quasars and CMASS galaxies | excess compatible with [CII], not required by the data | Pullen et al. 2018, arXiv:1707.06172 | [src: abstract] |
| COMAP Pathfinder | CO(1–0) at z = 2.4–3.4; fainter CO(2–1) from z = 6–8 | 12 deg² in a five-year campaign | Early Science from 13 months of data (2021); Season 2 with a threefold gain in map sensitivity (2024–2025) | Cleary et al. 2021, arXiv:2111.05927; Stutzer et al. 2024, arXiv:2406.07511; Dunne et al. 2025, arXiv:2510.23568 | [src] |
| TIME | [CII] at reionisation redshifts, CO at lower z | — | commissioning run 2021–2022; Galactic-centre maps only | Yang et al. 2025, arXiv:2511.09473 | [src] |
| CCAT / FYST, EoR-Spec | [CII] | Deep Spectroscopic Survey | not yet observing ("will conduct"); pipeline tested on end-to-end simulations | Dev et al. 2026, arXiv:2607.20404 | [src] |
| EXCLAIM | [CII] at z = 2.5–3.5 | pathfinder | simulated forecasts only | Kramer et al. 2026, arXiv:2603.13218 | [src: abstract] |
| SPHEREx | near-infrared lines, 0.75–5.0 μm in 102 bands, resolving power 35–130, 6.2″ pixels | all sky four times in two years; two deep fields near the ecliptic poles for intensity mapping | launched 11 March 2025; spectral images released rapidly; specialised products later in the mission | Bock et al. 2025, arXiv:2511.02985 | [src] |
| HETDEX | Lyα | intensity maps used for stacking | published in 2022 (two papers cited there, not fetched) | named in arXiv:2606.25955, section 3 | [sec] |

SPHEREx depth: 5σ of 19.5–19.9 AB mag over 0.75–3.8 μm and 17.8–18.8 AB mag over 3.8–5.0 μm
after the two-year survey [src: arXiv:2511.02985]. [src: abstract]

## 5. Quasar, galaxy and CMB data used for the reionisation history
<!-- key: quasar-galaxy-and-cmb-data-used-for-the -->

| Data set | Content | Used for | Citation | Flag |
|---|---|---|---|---|
| WMAP first-year polarisation | TE correlation at 23–94 GHz | first detection of the reionisation signature (τ = 0.17 ± 0.04) | Kogut et al. 2003, arXiv:astro-ph/0302213 | [src: abstract] |
| SDSS z ~ 6 quasars | 19 quasars at 5.74 < z < 6.42 | Gunn–Peterson optical depth, dark gaps, H II region sizes | Fan et al. 2006, arXiv:astro-ph/0512082 | [src: abstract] |
| SDSS, Gemini/GMOS (GGG), Keck/LRIS, ESI and X-Shooter stacks | 1800 quasars at z = 3.50–4.34; 163 quasars at z_em > 4.4; z ~ 5–6 samples | Lyman-continuum mean free path | Prochaska et al. 2009, arXiv:0910.0009; Worseck et al. 2014, arXiv:1402.4154; Becker et al. 2021, arXiv:2103.16610 | [src] |
| XQR-30 + archival X-Shooter and ESI | 67 sightlines at z > 5.5 with S/N > 10 per ≤ 15 km/s pixel; XQR-30 itself is 30 quasars at z > 5.7 with S/N > 20 | mean Lyα transmission and τ_eff distributions over 4.9 < z < 6.1 | Bosman et al. 2022, arXiv:2108.03699 | [src: abstract] |
| Planck low-ℓ polarisation | PR3 (2018 legacy), SRoll2 reprocessing of HFI, PR4 | τ | Planck Collaboration 2018, arXiv:1807.06209; Pagano et al. 2019, arXiv:1908.09856; Upadhyay et al. 2026, arXiv:2609.24989 | [src] |
| XQR-30 (VLT/X-Shooter large programme), enlarged | 42 quasars at 5.8 ≲ z ≲ 6.6, high resolution and high signal-to-noise | τ_eff, dark gaps, dark pixels (34 quasars), damping wings (23 of 42 after quality control) | Greig et al. 2024, arXiv:2404.12585; Davies et al. 2025, arXiv:2510.25829 | [src] |
| X-Shooter + Keck/ESI compilation | 55 quasars at z_em > 5.5 | Lyα dark gaps | Zhu et al. 2021, arXiv:2109.06295 | [src] |
| z > 7 quasars | ULAS J1120+0641 (z = 7.09), ULAS J1342+0928 (z = 7.54) | damping wings | Davies et al. 2018, arXiv:1802.06066 | [src: abstract] |
| JWST/NIRSpec prism compilations | 27 galaxies (2023); 581 galaxies at z = 4.5–13 from JADES, UNCOVER, CEERS and GO/DDT programmes (2025) | galaxy damping wings | Umeda et al. 2023, arXiv:2306.00487; Umeda et al. 2025, arXiv:2504.04683 | [src] |
| DAWN JWST Archive | 1428 NIRSpec spectra at 5 < z < 10 | f_esc and ionising budget | Giovinazzo et al. 2026, arXiv:2607.22834 | [src: abstract] |
| DIVER (GOODS-N) | 250 galaxies at 4.8 < z < 11, 84 Lyα detections | Lyα visibility against environment | Zhu et al. 2026, arXiv:2608.19311 | [src: abstract] |
| PASSAGE (JWST/NIRISS pure parallel) | slitless, no photometric preselection | Lyα luminosity function at 7.5–9.5 | Runnholm et al. 2025, arXiv:2502.19174 | [src: abstract] |
| MMT/Binospec in GOODS-N | 236 galaxies at z ~ 5–6, 62 Lyα detections | post-reionisation Lyα baseline | Prieto-Lyon et al. 2025, arXiv:2509.18302 | [src: abstract] |
| JADES NIRCam | 15,721 galaxies at 3 ≤ z ≤ 9, mass-complete | ξ_ion | Simmonds et al. 2024, arXiv:2409.01286 | [src] |
| SPT-SZ + SPTpol; SPT-3G D1 | 2540 + 500 deg²; 1646 deg², two years, 95/150/220 GHz | kSZ power | Reichardt et al. 2020, arXiv:2002.06197; Chaubal et al. 2026, arXiv:2601.20551 | [src] |
| ACT DR6 | multi-frequency power spectra | kSZ power | Beringue et al. 2025, arXiv:2506.06274 | [src] |
| SPT + Herschel-SPIRE | 100 deg², 95/150/220 GHz at 4.5, 3 and 16 μK-arcmin, plus 600 and 857 GHz | kSZ trispectrum | Raghunathan et al. 2024, arXiv:2403.02337 | [src: abstract] |

## 6. Planned
<!-- key: planned -->

| What | Expectation (all **forecast** or schedule) | Citation | Flag |
|---|---|---|---|
| CHORD full array | commissioned in 2028 | arXiv:2607.09374 | [src] |
| SKA-Mid wide HI survey | four orders of magnitude more volume than the MeerKLASS L-band surveys | arXiv:2606.25955, section 3 | [src] |
| COMAP five-year Pathfinder | CO power spectrum at S/N 9–17; CO × galaxy at S/N 19 | arXiv:2111.05927 | [src] |
| CCAT Deep Spectroscopic Survey | combined [CII] + CO power on shot-noise scales (k > 0.1 Mpc⁻¹) with one module at 50% efficiency | arXiv:2607.20404 | [src] |
| τ from 21 cm clustering | competitive with space CMB missions only with a clean wedge at k ≈ 0.1 h/Mpc across 0.2 ≲ x ≲ 0.8; improving on current CMB values needs ~5 years of observation, against the usual O(1000 h) | Sailer, Chen & White 2022, arXiv:2205.11504 | [src: abstract] |
| Large-angle CMB polarisation | LiteBIRD (launch JFY2036) is the next cosmic-variance-limited τ measurement | sibling `cosmo-cmb` | [sec] |
| LOFAR 2.0, SKA-Low EoR surveys | listed as future | arXiv:2511.21289, introduction | [sec] |

## Not verified
<!-- key: not-verified -->

- CHIME, MeerKAT, HERA, LOFAR, MWA and NenuFAR hardware descriptions (element counts, apertures,
  sites) beyond what is quoted above were not read at source in this session. The MWA Phase III
  upgrade paper (Tingay et al. 2026) was seen in a search but is not in the bibliography.
- SKA array-assembly dates: sources disagree and the SKAO timeline page returned an access
  error.
- BINGO, FAST and the Tianlai dish array appear only in forecast or pipeline papers seen in
  searches; no result or status is recorded.
- CONCERTO results were not found in the searches run; COPSS and mmIME are known from their
  abstracts only.
- Public data locations (archives, URLs) were not checked for any experiment except the
  statement that EDGES raw data are released with arXiv:2605.16643.
