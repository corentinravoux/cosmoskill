# Lyman-alpha forest — surveys, samples and data releases

Scope: every data set that matters for Lyα forest cosmology and IGM physics — survey-grade samples (SDSS/BOSS/eBOSS, DESI), high-resolution samples, tomography surveys, simulations and mock suites treated as data products, and what is planned.
Snapshot: 2026-10-07

Flags: `[src]` read this session in the cited paper; `[der]` derived here; `[sec]` from a named secondary source. Forecasts are labelled.

## 1. Two regimes of data
<!-- key: two-regimes-of-data -->

Lyα forest data come in two regimes that are analysed differently and are rarely interchangeable.

| Regime | Typical resolution and S/N | Number of sightlines | What it is used for |
|---|---|---|---|
| Survey-grade (SDSS/BOSS/eBOSS, DESI) | moderate resolution, low S/N per pixel (BOSS forests at S/N ~ 2, arXiv:1108.6080 [src]) | e.g. 210,005 forest quasars in eBOSS DR16 (arXiv:2007.08995) and > 820,000 in DESI DR2 (arXiv:2503.14739) [src: abstract of each paper] | BAO and AP from 3D correlations; P1D at k ≲ 0.02 (km/s)⁻¹ for BOSS/eBOSS (arXiv:1812.03554 [src]); wide-area tomography at ~13 h⁻¹Mpc (arXiv:2004.01448 [src]) |
| High resolution (HIRES, UVES, MIKE, X-shooter) | R from ~4000–7000 (X-shooter, arXiv:1607.08776 [src]) to 36,000–103,000 (HIRES, arXiv:1707.07905 [src]), high S/N | e.g. 100 (XQ-100, arXiv:1607.08776) and 538 (KODIAQ + SQUAD + XQ-100, arXiv:2108.10870) [src: abstract of each paper] | P1D at k ≳ 0.02 s/km, "unavailable in SDSS and DESI analyses" (arXiv:2108.10870 [src]); thermal state; WDM and FDM limits |
| Dense deep fields (Keck/LRIS, Magellan/IMACS) | R ~ 1000 (LATIS, arXiv:2510.08815 [src: abstract]), faint galaxies as background sources | 360, 1200 and 3300 per deg² needed at g = 24.0, 24.5, 25.0 (design study, arXiv:1309.1477) [src: abstract] | Mpc-scale IGM tomography |

## 2. Past: SDSS-I/II, BOSS, eBOSS
<!-- key: past-sdss-i-ii-boss-eboss -->

| Release | Lyα content | Key Lyα papers | Flag |
|---|---|---|---|
| SDSS-I/II | 3,035 high-z QSO spectra used for P1D | arXiv:astro-ph/0405013 [src: abstract] (measurement), arXiv:astro-ph/0407377 (linear power), arXiv:astro-ph/0407372 (parameters) | [src] |
| SDSS DR7 | 6,065 spectra in mean-flux composites; 12,069 z > 2.3 spectra with MF-PCA continua | arXiv:1208.2584, arXiv:1108.6080 | [src: abstract] |
| BOSS year 1 | ~14,000 z > 2.1 QSOs; first 3D correlations | arXiv:1104.5244 | [src: abstract] |
| BOSS DR9 | 48,640 QSOs (2.1 ≤ z ≤ 3.5) for the first BAO detection; 13,821 selected spectra for P1D; fitting code and inputs public (baofit) | arXiv:1211.2616, arXiv:1301.3459, arXiv:1301.3456, arXiv:1306.5896 | [src: abstract] |
| BOSS DR11 | 137,562 QSOs (auto); >164,000 QSOs (cross) | arXiv:1404.1801, arXiv:1311.1767 | [src: abstract] |
| BOSS DR12 | 157,783 QSOs (auto); 168,889 forests and 234,367 QSOs (cross) | arXiv:1702.00176, arXiv:1708.02225 | [src: abstract] |
| eBOSS DR14 | 179,965 Lyα-region spectra plus 56,154 Lyβ-region spectra (first use of the Lyβ region); 266,590 QSOs (1.77 < z < 3.5) for the cross; 43,751 selected of 180,413 visually inspected spectra for P1D | arXiv:1904.03400, arXiv:1904.03430, arXiv:1812.03554 | [src: abstract] |
| eBOSS DR16 (final) | 210,005 QSOs at z > 2.10 for forests; 341,468 tracer QSOs at z > 1.77; `picca`, the delta catalogue and the Δχ² surfaces are public | arXiv:2007.08995 | [src: abstract] |
| eBOSS DR16 DLA catalogue | 117,458 absorber candidates (2 ≤ z_DLA ≤ 5.5, 19.7 ≤ log N_HI ≤ 22), 57,136 with log N_HI ≥ 20.3, from a CNN; completeness and purity > 90% for 20.1 ≤ log N_HI ≤ 22 in bright forests | arXiv:2107.09612 | [src: abstract] |
| SDSS DR16Q Gaussian-process DLA catalogue | posterior DLA probabilities per spectrum, including the Lyβ region | arXiv:2103.10964 | [src] |

Reanalyses of the final SDSS data that are still current: the full-shape AP measurement (arXiv:2209.13942), the 3D power spectrum from 205,012 spectra (arXiv:2403.08241), the small-scale P3D proof of principle at z = 2.2 and 2.4 (arXiv:2310.09116), the 1D bispectrum from 122,066 spectra (arXiv:2410.09150), the Stripe 82 tomographic map and void catalogue (arXiv:2004.01448) and the void–forest cross-correlation (arXiv:2203.11045) [src: abstract] [src for all sample sizes, see `results.md`].

## 3. Current: DESI
<!-- key: current-desi -->

DESI began its 5-year main survey in May 2021 after a five-month Survey Validation that ended in May 2021 (arXiv:2503.14745, arXiv:2306.06308) [src].

| Release | Content relevant to Lyα | Lyα analyses | Flag |
|---|---|---|---|
| Early Data Release (EDR) | Survey Validation spectra; 76,079 objects in the quasar sample (arXiv:2306.06308) [src: abstract] | Lyα catalogue from 88,511 QSOs (SV + first two months, "M2"), public at `https://data.desi.lbl.gov/public/edr/vac/edr/lya/fuji/v0.3` (arXiv:2306.06312); 3D correlations, BAO at 3.8σ (arXiv:2308.10950); P1D with FFT from 26,330 QSOs (arXiv:2306.06311) and QMLE from 54,600 QSOs (arXiv:2306.06316) [src: abstract of each paper]; redshift-error study (arXiv:2402.18009) | [src] |
| DR1 (first 13 months of the main survey + reprocessed SV) | 18.7 M objects with high-confidence redshifts, of which 1.6 M classified as quasars (arXiv:2503.14745) [src: abstract] | BAO from >420,000 forests and >700,000 QSOs (arXiv:2404.03001); cosmology (arXiv:2404.03002); validation on 150 mocks (arXiv:2404.03004); contaminants (arXiv:2404.03003); BAL masking (arXiv:2405.09737); full shape (arXiv:2509.15308); P1D FFT (arXiv:2505.09493), QMLE from >300,000 QSOs (arXiv:2505.07974), estimator validation (arXiv:2509.13593), P1D cosmology (arXiv:2601.21432); mean optical depth from 83,635 spectra (arXiv:2405.06743); CMB-lensing × P1D bispectrum from >280,000 spectra (arXiv:2405.14988) | [src] |
| DR2 (first three years) | forests in >820,000 QSO spectra, >1.2 million QSO positions | BAO (arXiv:2503.14739) and cosmology (arXiv:2503.14738); DLA catalogue with 41,152 candidate DLAs at log N_HI > 20.3 in S/N > 2 spectra (arXiv:2503.14740); validation on 400 mocks (arXiv:2503.14741); multipole BAO (arXiv:2603.04281); three-redshift-bin BAO (arXiv:2607.19619); full-shape AP (arXiv:2607.27410) with validation (arXiv:2607.27411), CoLoRe-2LPT mocks (arXiv:2607.27412) and the P1D-informed priors (arXiv:2607.27413); C IV forest BAO from 1.5 million z > 1.3 QSO sightlines (arXiv:2601.08103) | [src: abstract] |
| DESI LBG pilot (COSMOS, XMM-LSS) | 4,151 forest skewers from Lyman-break galaxy spectra, 13,362 galaxy positions | first LBG-forest auto-correlation, z_eff = 2.70 (arXiv:2507.21852) | [src: abstract] |

Growth of the DESI Lyα BAO sample: DR2 is about twice DR1 (arXiv:2503.14739 [src: abstract]). The DR1 P1D sample is 1.7 times the eBOSS one (arXiv:2505.07974 [src: abstract]); the DESI end-of-survey P1D sample was expected to be five times the SDSS one (arXiv:2306.06311 [src], a pre-survey expectation).

Instrument facts that matter for the forest (arXiv:2503.14739, Sects. 2.4 and 6.3) [src]: the DESI blue channel has resolution 2000–3000 against 1500–2000 for the SDSS spectrographs; forests are measured over 3600–5772 Å (the lower bound is the design minimum wavelength, the upper the blue–red dichroic transition); DR1 quasars mostly had a single observation, so the typical S/N of DR1 was somewhat lower than eBOSS DR16, whereas most DR2 quasars have multiple observations. For P1D only the high-S/N subset is used: 62,807 spectra in the DR1 cosmological analysis, against 13,821 (BOSS) and 43,751 (eBOSS) (arXiv:2601.21432, Sect. 6.2) [src].

Public-data status. EDR was released on 13 June 2023 and DR1 on 19 March 2025 [sec: DESI data-release page `data.desi.lbl.gov/doc/releases/`, fetched 2026-10-08]; the papers are arXiv:2306.06308 and arXiv:2503.14745. For DR2 only the cosmology chains and supporting products were released, on 6 October 2025, with the full DR2 to follow "in some months" [sec: DESI collaboration news page of that date, fetched 2026-10-08]; the release page listed no DR2 spectra when fetched. The DR1 P1D data vectors are on Zenodo (records 16943723 for QMLE and 17100543 for FFT; arXiv:2601.21432, Sect. 2.1) [src]. The EDR Lyα delta catalogue is a public value-added catalogue (arXiv:2306.06312) [src].

## 4. High-resolution and intermediate-resolution samples
<!-- key: high-resolution-and-intermediate-resolution -->

| Sample | Instrument | Content | Lyα use | Citation | Flag |
|---|---|---|---|---|---|
| KODIAQ DR2 | Keck/HIRES, 36,000 ≤ R ≤ 103,000 | 300 QSOs at 0.07 < z_em < 5.29, 831 spectra, ~4.9 Ms total exposure, public at the Keck Observatory Archive | P1D, column-density statistics | arXiv:1707.07905 | [src: abstract] |
| XQ-100 | VLT/X-shooter, R ~ 4000–7000, 315–2500 nm | 100 QSOs at z ~ 3.5–4.5; median S/N 33, 25, 43 at rest 1700, 3000, 3600 Å; all products public | P1D at z = 3–4.2, k = 0.003–0.06 s/km (arXiv:1702.01761) | arXiv:1607.08776 | [src: abstract] |
| KODIAQ + SQUAD + XQ-100 combined | HIRES, UVES, X-shooter | 538 QSOs, z = 2.0–4.6, k < 0.1 s/km; KODIAQ and SQUAD combined at the spectrum level, XQ-100 estimated separately because of its large resolution correction | QMLE P1D | arXiv:2108.10870 | [src: abstract] |
| Walther et al. sample | HIRES + UVES | 74 spectra, 1.8 < z < 3.4 | P1D to k ~ 0.1 s/km, thermal history | arXiv:1709.07354 | [src: abstract] |
| HIRES/MIKE z > 4 | Keck/HIRES, Magellan/MIKE | 25 QSOs at z > 4 | WDM limits (z = 4.2–5.4) | arXiv:1306.2314 | [src: Sect. III] |
| Boera et al. sample | HIRES + UVES | 15 spectra, 4.0 ≲ z ≲ 5.2 | smallest-scale P1D, thermal history, WDM | arXiv:1809.06980 | [src: abstract] |
| Gaikwad et al. sample | high resolution | 103 spectra, ten bins over 2 ≤ z ≤ 4 | T_0, γ from four statistics | arXiv:2009.00016 | [src: abstract] |
| XQR-30 (+ archival) | VLT/X-shooter | 30 QSOs at z > 5.7 with S/N > 20 per pixel; 67 sightlines at z > 5.5 in the extended sample | mean transmission 4.9 < z < 6.1, end of reionisation | arXiv:2108.03699 | [src: abstract] |
| Faucher-Giguère et al. sample | Keck/ESI, HIRES, Magellan/MIKE | 86 spectra, 2 < z < 4.2 | absolute τ_eff(z) | arXiv:0710.4522 | [src: abstract] |

A caution on combining high-resolution compilations: the KODIAQ-SQUAD P1D favours a significantly higher primordial amplitude than XQ-100 or eBOSS when fitted with PRIYA, "driven by the selection bias toward high-column density absorbers" of archival samples (arXiv:2509.18271) [src]. Archival HIRES/UVES samples were built from individual programmes that often targeted known absorbers; XQ-100 was a homogeneous legacy survey (arXiv:1607.08776) [src].

## 5. Tomography surveys
<!-- key: tomography-surveys -->

| Survey | Instrument | Area and depth | Sightlines | Map | Status | Citation | Flag |
|---|---|---|---|---|---|---|---|
| CLAMATO pilot | Keck-I/LRIS | 5′ × 15′ in COSMOS | 24 star-forming galaxies, z ~ 2.3–2.8, ~2 h⁻¹Mpc separation | 2.20 ≤ z ≤ 2.45, ≈ 3.5 h⁻¹Mpc resolution | superseded | arXiv:1409.5632 | [src: abstract] |
| CLAMATO DR1 | Keck-I/LRIS | 0.157 deg² | 240 galaxies and QSOs at 2.17 < z < 3.00 | 2.05 < z < 2.55, 2.5 h⁻¹Mpc smoothing, 3.15 × 10⁵ h⁻³Mpc³ | public (redshifts, spectra, pixels, map) | arXiv:1710.02894 | [src: abstract] |
| CLAMATO DR2 | Keck-I/LRIS | ~0.2 deg² | 320 objects | Wiener-filtered maps plus a forward-modelled dark-matter field from a joint galaxy + forest likelihood; public on Zenodo (record 7524313) as stated in the abstract | final | arXiv:2109.09660 | [src] |
| LATIS | Magellan/IMACS, R ~ 1000, ~12 h integrations | CFHTLS D1, D2 (COSMOS), D4; planned 1.7 deg² | planned ~3800 galaxy spectra; released 7408 spectra, 5575 secure redshifts | 1.65 deg², z = 2.2–2.8, 4 h⁻¹ cMpc, 4.7 × 10⁵ pixels | complete; data release October 2025 | arXiv:2002.10676, arXiv:2510.08815 | [src: abstract] |
| eBOSS Stripe 82 | SDSS/BOSS spectrographs | 220 deg² | 37 QSO spectra per deg², S/N 2 per Å | 0.94 h⁻³Gpc³, 13 h⁻¹Mpc; void and protocluster-candidate catalogues | published | arXiv:2004.01448 | [src: abstract] |
| WEAVE-QSO | WHT/WEAVE | large area, high QSO density | — | Wiener-filter maps smoothed at ≈ 16 Mpc/h (**forecast**) | see §7 | arXiv:2201.02606 | [src: abstract] |

The two regimes of tomography are distinct: deep-field maps with galaxies as sources, at 2.5 h⁻¹Mpc (CLAMATO, arXiv:1710.02894) and 4 h⁻¹ cMpc over 1.65 deg² (LATIS, arXiv:2510.08815), and wide-area maps with quasars only, at 13 h⁻¹Mpc (Stripe 82, arXiv:2004.01448) and ≈ 16 Mpc/h in the WEAVE-QSO forecast (arXiv:2201.02606) [src: abstract of each paper]. Void finding in the first regime was demonstrated in CLAMATO (arXiv:1710.02612); the void–forest RSD measurement was done in the second (arXiv:2203.11045).

## 6. Simulations, emulators and mock suites used as data products
<!-- key: simulations-emulators-and-mock-suites-used-as -->

### 6.1 Hydrodynamical suites
<!-- key: hydrodynamical-suites -->

| Suite | Code | Size | Purpose | Citation | Flag |
|---|---|---|---|---|---|
| Nyx reference runs | Nyx (N-body + Eulerian finite-volume hydro, AMR-capable) | convergence: 20 h⁻¹kpc cells for 1% in flux statistics to k = 10 h/Mpc; boxes L > 40 h⁻¹Mpc for sub-percent missing-mode error | resolution and box requirements, 2 ≤ z ≤ 4 | arXiv:1301.4498, arXiv:1406.6361 | [src: abstract] |
| Sherwood | SPH (code not named in the abstract) | volumes 10³–160³ h⁻³Mpc³, up to 17.2 billion particles | reference comparison to high-resolution data, 2 < z < 5 | arXiv:1605.03462 | [src] |
| Sherwood-Relics | hydrodynamics with a hybrid radiative-transfer scheme | over 200 simulations | patchy reionisation and pressure smoothing at z > 4 | arXiv:2207.13098 | [src: abstract] |
| Nyx vs CRK-HACC | Eulerian vs SPH | — | ≲ 1% agreement in P1D when CRK-HACC densities are reconstructed by tessellation | arXiv:2207.05023 | [src] |
| ACCEL² | Nyx | up to 640 h⁻¹Mpc boxes, and smaller boxes down to 25 h⁻¹kpc resolution | 3D power on all scales, bias parameters, BAO in a hydro box | arXiv:2407.04473 | [src: abstract] |
| PRIYA | MP-Gadget with the ASTRID galaxy-formation model | 48 low-fidelity runs (1536³ particles) and 3 high-fidelity runs (3072³) in 120 Mpc/h boxes; 9 parameters (4 cosmological, 5 astrophysical/thermal) | multi-fidelity emulator of P1D and mean T; includes DLAs, AGN feedback, patchy H and He reionisation | arXiv:2306.05471 | [src: abstract] |
| Lyssa | Nyx | 18 runs, 4096³ cells in 120 Mpc (~81 Mpc/h) boxes | Gaussian-process emulator in the `lym1d` likelihood | arXiv:2412.05372 | [src: abstract] |
| LaCE training set | not named in the abstracts read | 30 fixed-and-paired simulations (as used by ForestFlow), z = 2–4.5 | P1D emulators (Gaussian process, neural network) and ForestFlow | arXiv:2011.15127, arXiv:2305.19064, arXiv:2409.05682 | [src: abstract] |
| Cholla WDM grid | Cholla (GPU) | 1080 simulations | thermal histories × WDM free streaming | arXiv:2209.14220 | [src: abstract] |
| CAMELS (IllustrisTNG, SIMBA) | — | small boxes | simulation-based inference test for P1D; cross-model training bias of ~10% on σ_8 | arXiv:2603.13011 | [src: abstract] |

### 6.2 Fast mocks for 3D analyses
<!-- key: fast-mocks-for-3d-analyses -->

| Mock family | Method | Use | Citation | Flag |
|---|---|---|---|---|
| LyaCoLoRe | Gaussian/lognormal fields → flux skewers with fast approximations; HCDs and metals added | eBOSS and DESI DR1 BAO validation; covariance for the eBOSS P3D | arXiv:1912.02763 | [src] |
| Saclay mocks | FGPA on FFT Gaussian fields with the velocity-gradient field for RSD; HCD catalogue placed at high density | 100 realisations over the 14,000 deg² DESI footprint at 100 QSOs per deg² | arXiv:2310.18996 | [src: abstract] |
| quickquasars synthetic spectra | continua, contaminants, DESI instrument model applied to the transmission skewers | DESI EDR/DR1 analyses, full-survey BAO forecast | arXiv:2401.00303 | [src] |
| CoLoRe-QL | quasi-linear input power spectrum to reproduce BAO broadening | 400 realisations for DESI DR2 BAO | arXiv:2503.14741 | [src: abstract] |
| CoLoRe-2LPT | second-order Lagrangian perturbation theory; reproduces bias, β, mean flux and P1D within 10% of DESI; QSO bias to < 5% | DESI DR2 full-shape validation | arXiv:2607.27412 | [src: abstract] |
| AbacusSummit Lyα | FGPA painted on N-body (2 h⁻¹Gpc boxes, 6912³ particles, z = 2.5), calibrated on IllustrisTNG | BAO-shift measurement, full-shape validation | arXiv:2305.08899 [src: abstract], arXiv:2503.13442 | [src] |
| Lognormal 1D mocks | lognormal spectra for P1D | estimator validation (20 realisations of DR1) | arXiv:2509.13593 | [src: abstract] |

## 7. Planned and future
<!-- key: planned-and-future -->

| Facility | What is planned for the forest | Source | Flag |
|---|---|---|---|
| DESI (remaining data) | further releases beyond DR2; full-survey BAO forecast in arXiv:2401.00303 | arXiv:2401.00303 | [src] |
| DESI-II | pilot observations of galaxies at higher density and higher redshift (arXiv:2209.03585); "the next phase of DESI, which will start around 2029" in the words of the LBG target-selection study (arXiv:2410.08062); LBG forests are the new Lyα ingredient | arXiv:2209.03585, arXiv:2410.08062 | [src] |
| Wide LBG forest survey | 5000 deg², 1000 LBGs per deg²: 0.4% isotropic BAO, 1.3% AP from BAO, 0.6% AP with full shape (**forecast**) | arXiv:2507.21852 | [src: abstract] |
| Spec-S5 | two 6-m telescopes (upgrades of existing 4-m), 13,000 fibres each, more than 10× DESI spectroscopic capability, operations in the 2030s | arXiv:2503.07923 | [src: abstract] |
| MUST | 6.5-m, >20,000 targets per pointing over ~5 deg², Stage-V survey in the 2030s, >100 million galaxies and quasars to z ~ 5.5, LBGs at 2 < z < 5.5 | arXiv:2411.07970 | [src: abstract] |
| WEAVE-QSO | ~400,000 high-z QSOs on the 4.2-m WHT, targets from J-PAS (r < 23.2) and Gaia (r < 20); the 2016 proceedings anticipated a 2018 start | arXiv:1611.09388 | [src: abstract] |
| Subaru PFS | 2400 fibres, 380–1260 nm, 1.3° field; cosmology survey of emission-line galaxies at 0.8 < z < 2.4 and a galaxy-evolution programme with LBGs and LAEs | arXiv:1206.0737 | [src: abstract] |
| 4MOST | named as a target for full-shape and P3D methods | arXiv:2403.08241, arXiv:2412.06892 | [src] (mention only) |

The first-light dates of PFS and 4MOST are recorded in the hub file `observational-cosmology/references/field-state-2026.md` and were not re-verified here; `cosmo-surveys-facilities` owns facility timelines.

## 8. Sample growth at a glance
<!-- key: sample-growth-at-a-glance -->

Forest sample used for the 3D auto-correlation, and the BAO precision it bought.

| Release | Year | Forest quasars | Tracer quasars (cross) | Radial BAO error | Citation | Flag |
|---|---|---|---|---|---|---|
| BOSS DR9 | 2013 | 48,640 | — | 3% (isotropic peak position) | arXiv:1211.2616 | [src: abstract] |
| BOSS DR11 | 2015 | 137,562 | >164,000 | D_H/r_d = 9.18 ± 0.28 (auto) | arXiv:1404.1801, arXiv:1311.1767 | [src: abstract] |
| BOSS DR12 | 2017 | 157,783 | 234,367 | D_H/r_d = 8.94 ± 0.22 (auto + cross) | arXiv:1702.00176, arXiv:1708.02225 | [src: abstract of arXiv:1708.02225] |
| eBOSS DR16 | 2020 | 210,005 | 341,468 | D_H/r_d = 8.99 ± 0.19 | arXiv:2007.08995 | [src: abstract] |
| DESI EDR + M2 | 2023 | 88,509 | 147,899 | errors 1.7× eBOSS DR16 | arXiv:2308.10950 | [src: abstract] |
| DESI DR1 | 2024 | >420,000 | >700,000 | 2% on H | arXiv:2404.03001 | [src: abstract] |
| DESI DR2 | 2025 | >820,000 (z > 2.09) | >1.2 million (z > 1.77) | 1.1% | arXiv:2503.14739 | [src: abstract; redshift cuts in Sect. II.2] |
| DESI DR2, full shape | 2026 | same | same | 0.77% on D_H/r_d | arXiv:2607.27410 | [src: Sect. V.3] |

P1D uses a quality-selected subset, so the counts are much smaller: 3,035 (SDSS), 13,821 (BOSS DR9), 43,751 (eBOSS DR14), and for DESI DR1 more than 300,000 Lyα quasars in the QMLE measurement at S/N > 1 but 62,807 in the cosmological analysis at S/N > 3 (arXiv:astro-ph/0405013, arXiv:1306.5896, arXiv:1812.03554, arXiv:2505.07974 [src: abstract of each paper]; arXiv:2601.21432 [src: Sect. 2.1]). Quoting "DESI has ten times the eBOSS P1D sample" confuses these two numbers.

## 9. Where the public products are
<!-- key: where-the-public-products-are -->

| Product | Location as stated in the source | Citation | Flag |
|---|---|---|---|
| eBOSS DR16 `picca` code, delta catalogue, Δχ² surfaces | stated public in the abstract | arXiv:2007.08995 | [src] |
| BOSS DR9/DR11 fitting code and correlation functions (`baofit`) | stated public | arXiv:1301.3456, arXiv:1311.1767 | [src] |
| DESI EDR Lyα delta catalogue | `data.desi.lbl.gov/public/edr/vac/edr/lya/fuji/v0.3` | arXiv:2306.06312 | [src] |
| DESI DR1 P1D, QMLE and FFT | Zenodo records 16943723 and 17100543 | arXiv:2601.21432 | [src: Sect. 2.1] |
| DESI DR1 P1D compressed likelihood | `github.com/igmhub/cobaya_lya_p1d` | arXiv:2601.21432 | [src] |
| DESI DR2 cosmology chains | `data.desi.lbl.gov/public/papers/y3/bao-cosmo-params/` | DESI news page of 6 October 2025 | [sec] |
| DESI correlation-function fitter | `github.com/andreicuceu/vega` | arXiv:2503.14739 | [src] |
| Sherwood P3D measurements | `github.com/andreufont/sherwood_p3d` | arXiv:2205.00962 | [src] |
| AbacusSummit Lyα skewers and QSO catalogues | Globus, as stated | arXiv:2305.08899 | [src] |
| Nyx-based non-linear power tables and fit parameters | stated public | arXiv:1506.04519 | [src] |
| CLAMATO DR1 and DR2 | redshifts, spectra, pixel data, maps; DR2 on Zenodo (record 7524313) | arXiv:1710.02894, arXiv:2109.09660 | [src] |
| LATIS | spectra, redshifts, transmission pixels, maps, mock surveys | arXiv:2510.08815 | [src] |
| KODIAQ DR2 | Keck Observatory Archive and igmspec | arXiv:1707.07905 | [src] |
| XQ-100 | all data products public | arXiv:1607.08776 | [src] |
| UVB photo-ionisation and photo-heating tables | provided with the papers | arXiv:1105.2039, arXiv:1607.04218 | [src] |
| High-resolution P1D with covariance | electronic tables | arXiv:1709.07354 | [src] |

## 10. Not verified
<!-- key: not-verified -->

- The date on which the full DESI DR2 becomes public, and the timeline of DR3 Lyα analyses.
- WEAVE-QSO current status: a web search returned project pages on WEAVE first light and on the planned QSO survey size and resolution, but no data release or Lyα result was found, and those pages were not read directly; 4MOST Lyα-specific survey design; PFS IGM-tomography programme parameters (area, sightline density).
- The SQUAD (UVES) data-release paper and sample size; the DESI BAL catalogue paper for EDR (found by search, abstract not read in full).
- The resolution, pixel size and wavelength coverage of the BOSS and DESI spectrographs (to be taken from the instrument papers, owned by `cosmo-surveys-facilities`).
