# Weak lensing — surveys and data releases

Scope: the imaging surveys used for cosmic shear and galaxy–galaxy lensing,
past, current and planned, with the numbers a referee checks (area, source
density, depth, redshift bins) and where the data are.
Snapshot: 2026-10-07

Flags: `[src]` read this session in the cited paper or on the named official
page; `[sec]` from a named secondary source; `[der]` derived.

## 0. Summary table of shear catalogues
<!-- key: summary-table-of-shear-catalogues -->

Numbers are those of the cited catalogue or cosmology abstract; "n_eff" follows
each survey's own definition, so the column is indicative, not homogeneous.

| Catalogue | Area (deg²) | Galaxies | n_eff (arcmin⁻²) | Shape method | Citation | Flag |
|---|---|---|---|---|---|---|
| CFHTLenS | 154 | 4.2 million (0.2 < z < 1.3) | — | lensfit | arXiv:1212.3338, arXiv:1210.8201 | [src] |
| KiDS-450 | ~450 | ~15 million | — | lensfit (self-calibrating) | arXiv:1606.05338 | [src] |
| DES Y1 | 1321 | 26 million used; catalogues of 34.8 million (metacalibration, riz) and 21.9 million (im3shape, r) | — | metacalibration and im3shape; σ_m = 0.013 and 0.025 | arXiv:1708.01538, arXiv:1708.01533 | [src] |
| HSC Y1 | 137 | — | ~17 after cuts | — (catalogue: arXiv:1705.06745) | arXiv:1809.09148 | [src] |
| KiDS-1000 | 1006 | 21 million | 6.17 | lensfit | arXiv:2007.01845 | [src] |
| DES Y3 | 4143 | 100,204,026 | 5.59 (σ_e = 0.261) | metacalibration | arXiv:2011.03408 | [src] |
| HSC Y3 | 433.48 catalogue; 416 cosmology | >25 million | 19.9 catalogue; 15 cosmology | — | arXiv:2107.00136, arXiv:2304.00702 | [src] |
| DECADE (north cap) | 5412 | 107 million | 4.59 | metacalibration | arXiv:2502.17674 | [src] |
| KiDS-Legacy | 1347 | — | — | lensfit, calibrated on the SKiLLS multi-band image simulations | arXiv:2503.19441, arXiv:2210.07163 | [src] |
| DES Y6 | 4422 | 151,922,791 catalogue; ≈140 million cosmology | 8.22 catalogue; 8.29 cosmology (σ_e = 0.29) | metadetection | arXiv:2501.05665, arXiv:2602.10065 | [src] |
| DECADE + DES Y3 | 13,000 | 270 million | — | — | arXiv:2509.03582 | [src] |
| UNIONS-3500 | ~3500 (2894 used for B modes) | 62 million | 4.96 (σ_ε = 0.27) | — | arXiv:2605.13549, arXiv:2604.03227 | [src] |

Dashes mark quantities not stated in the abstracts read this session. The
shape-measurement method is given only where an abstract read this session
names it.

## 1. Past and completed Stage-II / Stage-III surveys
<!-- key: past-and-completed-stage-ii-stage-iii-surveys -->

### CFHTLenS
<!-- key: cfhtlens -->

CFHTLenS spans 154 deg² in five optical bands, with 4.2 million galaxies at
0.2 < z < 1.3 in the 2D analysis and a median redshift of 0.70 in the
tomographic one (arXiv:1212.3338, arXiv:1303.1808) [src]. The survey and its
systematics-driven catalogue construction are described in Heymans et al. 2012
(arXiv:1210.0032). Shapes come from lensfit (Miller et al. 2013,
arXiv:1210.8201). Cosmology: 2D cosmic shear (Kilbinger et al. 2013,
arXiv:1212.3338) and tomography with intrinsic-alignment mitigation (Heymans
et al. 2013, arXiv:1303.1808). UNIONS reuses the same camera (MegaCam) and
sees the same detector-scale additive pattern in COSEBI B modes
(arXiv:2604.03227) [src].

### KiDS (VST/OmegaCAM + VISTA/VIKING), complete
<!-- key: kids-vst-omegacam-vista-viking-complete -->

| Release / analysis | Area | Key facts | Citation | Flag |
|---|---|---|---|---|
| KiDS-450 | ~450 deg² | nearly 15 million galaxies; self-calibrating lensfit | Hildebrandt et al. 2017, arXiv:1606.05338 | [src] |
| KiDS+VIKING-450 | 450 deg² | optical + VIKING near-infrared, which allowed higher-redshift sources | Hildebrandt et al. 2020, arXiv:1812.06076 | [src] |
| KiDS-1000 (DR4) | 1006 deg² | 21 million gold-sample galaxies, 6.17 arcmin⁻² [src: arXiv:2007.01845]; shear catalogue arXiv:2007.01845; redshifts arXiv:2007.15635; methodology arXiv:2007.01844; cosmic shear arXiv:2007.15633; 3×2pt with BOSS and 2dFLenS arXiv:2007.15632 | Asgari et al. 2021; Heymans et al. 2021 | [src] |
| KiDS DR5 / KiDS-Legacy | 1347 deg² of nine-band imaging plus 23 deg² of KiDS-like imaging over deep spectroscopic fields | sources to z_B ≤ 2.0; ~32% gain in constraining power on Σ8 over previous KiDS analyses | Wright et al. 2024, arXiv:2503.19439 (DR5); Wright et al. 2025, arXiv:2503.19441 (cosmology) | [src] for the numbers, from arXiv:2503.19441 |

The KiDS DR5 page gives 1347 deg² in u, g, r, i with two i-band epochs,
combined with VIKING near-infrared photometry, served through the ESO archive,
Astro-WISE and the KiDS website (https://kids.strw.leidenuniv.nl/DR5/, fetched
2026-10-07) [src]. The redshift-calibration paper speaks of 27 deg² of
dedicated optical and near-IR imaging over spectroscopic fields
(arXiv:2503.19440) [src], against 23 deg² in the cosmology abstract
(arXiv:2503.19441) [src]; the difference is not explained in the abstracts.

KiDS-Legacy companion papers: redshift calibration (Wright et al. 2025,
arXiv:2503.19440), consistency tests and joint constraints (Stölzner et al.
2025, arXiv:2503.19442), image simulations SKiLLS (Li et al. 2023,
arXiv:2210.07163), covariance and OneCovariance (Reischke et al. 2024,
arXiv:2410.06962), extensions (arXiv:2512.11041), second- plus third-order
shear (arXiv:2606.12389), BNT k-cut (arXiv:2607.04384).

### DES (Blanco/DECam), complete
<!-- key: des-blanco-decam-complete -->

| Analysis | Area | Sources | Key facts | Citation | Flag |
|---|---|---|---|---|---|
| DES SV | — | 2.12 million (im3shape) and 3.44 million (ngmix) | first DES shear catalogues, two independent pipelines | Jarvis et al. 2016, arXiv:1507.05603 | [src] |
| DES Y1 | 1321 deg² | 26 million, four bins | shape catalogues arXiv:1708.01533; cosmic shear arXiv:1708.01538; 3×2pt arXiv:1708.01530 | Troxel et al. 2018; DES Collaboration 2018 | [src] area and counts from arXiv:1708.01538 |
| DES Y3 | 4143 deg² effective | 100,204,026 galaxies in riz, n_eff = 5.59 arcmin⁻², σ_e = 0.261, four bins, cosmic-shear S/N = 40 | shapes (metacalibration) arXiv:2011.03408; PSF arXiv:2011.03409; redshifts arXiv:2012.08566; image simulations arXiv:2012.08567; cosmic shear arXiv:2105.13543 and arXiv:2105.13544; 3×2pt arXiv:2105.13549 | Gatti et al. 2021; Amon et al. 2022 | [src] numbers from arXiv:2011.03408 and arXiv:2105.13543 |
| DES Y6 (final) | shape catalogue 4422 deg² (151,922,791 galaxies, n_eff = 8.22 arcmin⁻², σ_e = 0.29) [src: arXiv:2501.05665]; survey ≈5000 deg²; GGL footprint 4031 deg² | cosmology sample ≈140 million, 8.29 arcmin⁻², 50% complete at i = 24.0, four bins centred at ⟨z⟩ = 0.414, 0.538, 0.846, 1.157 | metadetection shapes arXiv:2501.05665; PSF arXiv:2501.05781; Balrog injection arXiv:2501.05683; Gold photometry arXiv:2501.05739; lens sample MagLim++ with ≈9 million galaxies in six bins | arXiv:2602.10065, arXiv:2601.14559, arXiv:2601.15175, arXiv:2510.23566 | [src] |

DES Y6 mean-redshift uncertainties per source bin are σ⟨z⟩ = 0.012, 0.008,
0.009, 0.024 (arXiv:2510.23566) [src]. The Y6 cosmic-shear signal-to-noise is
83, twice that of Y3 (arXiv:2602.10065) [src]. The Y6 tangential-shear S/N is
173 before scale cuts, 17% above Y3, and 75 (90) after the cuts at R_min = 6
(4) h⁻¹Mpc used with linear (non-linear) galaxy bias (arXiv:2601.15175) [src].

### DECADE (DECam, community and archival imaging)
<!-- key: decade-decam-community-and-archival-imaging -->

The DECADE project builds DES-like shear catalogues from DECam imaging outside
the DES footprint: 107 million galaxies over 5,412 deg² in the northern
Galactic cap, with effective density 4.59 arcmin⁻² (Anbajagane et al. 2025,
arXiv:2502.17674 shape catalogue; arXiv:2502.17675 redshifts; arXiv:2502.17676
pipeline validation on inhomogeneous data; arXiv:2502.17677 cosmology) [src].
Paper V combines the northern and southern Galactic caps of DECADE with DES
Y3: 270 million galaxies over 13,000 deg², the largest lensing data set to
date by galaxy count and area; shear catalogues, data vectors and likelihoods
are public (arXiv:2509.03582) [src].

### HSC-SSP (Subaru/Hyper Suprime-Cam)
<!-- key: hsc-ssp-subaru-hyper-suprime-cam -->

| Analysis | Key facts | Citation | Flag |
|---|---|---|---|
| HSC Y1 | 137 deg², ~17 arcmin⁻² after cuts (i < 24.5, 0.3 ≤ z ≤ 1.5), four bins, Cℓ S/N = 16 over 300 ≤ ℓ ≤ 1900 [src: arXiv:1809.09148]; shear catalogue arXiv:1705.06745; Cℓ analysis arXiv:1809.09148; ξ± analysis arXiv:1906.06041 | Mandelbaum et al. 2018; Hikage et al. 2019; Hamana et al. 2020 | [src] |
| HSC Y3 | catalogue 433.48 deg² in six fields, raw density 22.9 and effective 19.9 arcmin⁻² at i < 24.5 [src: arXiv:2107.00136]; cosmology footprint 416 deg², 15 arcmin⁻² in the adopted redshift range, mean i-band seeing 0.59 arcsec, more than 25 million galaxies in four bins over 0.3–1.5 [src: arXiv:2304.00701, arXiv:2304.00702]; shear catalogue arXiv:2107.00136; n(z) inference arXiv:2211.16516; Cℓ arXiv:2304.00701; ξ± arXiv:2304.00702; 3×2pt measurements arXiv:2304.00703 and cosmology arXiv:2304.00704, arXiv:2304.00705 | Li et al. 2022; Rau et al. 2023; Dalal et al. 2023; Li et al. 2023; More, Miyatake, Sugiyama et al. 2023 | [src] |
| HSC Y3 recalibrated | DESI clustering redshifts replace the wide Δz priors of the two highest bins | arXiv:2511.18134 | [src] |

### UNIONS (CFHT/MegaCam r band, northern sky)
<!-- key: unions-cfht-megacam-r-band-northern-sky -->

UNIONS-3500 is the first cosmic-shear catalogue of the survey: about 3500 deg²
in r with median seeing 0.7 arcsec, 62 million galaxies, effective density
4.96 arcmin⁻², shape noise σ_ε = 0.27 (Hervas-Peters et al. 2026,
arXiv:2605.13549) [src]. The B-mode validation uses 2894 deg² with n_eff ≈ 5.0
arcmin⁻² (Daley et al. 2026, arXiv:2604.03227) [src]. The first cosmology is
non-tomographic, in configuration space (arXiv:2605.13547) and harmonic space
(arXiv:2605.13543). UNIONS is the ground-based optical complement to Euclid in
the north.

## 2. Spectroscopic partners (lenses and redshift calibration)
<!-- key: spectroscopic-partners-lenses-and-redshift -->

DESI has become the common calibration and lens sample of the Stage-III
lensing surveys: more than 256 000 high-quality redshifts in the COSMOS and
XMM/VVDS fields, a factor of three above earlier compilations there (Blanco et
al. 2025, arXiv:2512.15964) [src]; a unified n(z) calibration of DES, HSC and
KiDS (Lange et al. 2025, arXiv:2510.25419); galaxy–galaxy lensing measured
around DESI DR1 BGS and LRG with HSC, KiDS, SDSS and DES sources (Heydenreich
et al. 2025, arXiv:2506.21677). BOSS and eBOSS galaxies and quasars are the
clustering-redshift reference of DES Y6 (arXiv:2510.23565) [src].

## 3. Stage-IV: status today
<!-- key: stage-iv-status-today -->

| Facility | Status on 2026-10-07 | Source | Flag |
|---|---|---|---|
| Euclid | Wide survey of about 14,000 deg² of extragalactic sky (Euclid Collaboration 2024, arXiv:2405.13491) [src]. Public releases to date, complete list as of 2026-10-08: Early Release Observations (ERO) data release, 23 May 2024; Quick Data Release 1 (Q1), 19 March 2025; Quick Data Release 2 (Q2), 24 June 2026; no other public release is listed, and none of the three is a cosmology release [src]. Q1: 63.1 deg² of the Euclid Deep Fields at nominal wide-survey depth, about 30 million objects in EDF-North, EDF-South and EDF-Fornax (Euclid Collaboration 2025, arXiv:2503.15302) [src]. Q2: the Euclid Galactic Bulge Survey, 4.8 deg² over nine adjoining fields, VIS calibrated images with astrometry and photometry catalogues for 60 million stars, no lensing product (Euclid Consortium Q2 page, https://www.euclid-ec.org/science/q2/, fetched 2026-10-08) [src]. A LensMC shear catalogue on Q1 exists for cluster lensing (Congedo et al. 2026, arXiv:2606.20829), not for cosmic shear. DR1 is split: "DR1-Foundation" (raw data, calibrated images, catalogues, spectra over about 1900 deg²) on 12 November 2026; the complete DR1 with the higher-level galaxy-clustering and weak-lensing products in mid-2027. Announced after that, all tentative: Quick Data Release 3 (Q3) 2028; DR2 June 2029; Quick Data Release 4 (Q4) 2030; DR3 October 2031 (the IPAC timeline, https://euclid.caltech.edu/page/data-release-timeline, gives March 2029 for DR2; the ESA page is the reference). No Euclid cosmic-shear cosmology exists yet. | Release list and dates: ESA Euclid data page (https://www.cosmos.esa.int/web/euclid/data) and ESA Euclid timeline (https://www.cosmos.esa.int/web/euclid/timeline), both fetched 2026-10-08; DR1 content: ESA DR1 timeline page, update of 15 June 2026 (https://www.cosmos.esa.int/web/euclid/dr1-timeline) | [src] |
| Rubin LSST | The ten-year survey began on 30 June 2026. Data Preview 1 covers ~15 deg² in seven fields in ugrizy, about 2.3 million objects, median PSF FWHM ≈ 1.14 arcsec, available to data-rights holders on the Rubin Science Platform (Vera C. Rubin Observatory 2026, arXiv:2603.23786) [src]. Early Data Preview 2 was released on 27 July 2026: Science Pipelines v30 processing of LSSTCam observations taken between April 2025 and January 2026, deep coadds over about 3000 deg² and visit images over about 15,000 deg²; the pre-release notice says it delivers cell-based coadds and a `ShearObject` catalogue for the first time. The full DP2 (adding raw, visit, difference and template images) is expected October–December 2026. The LSST Science Pipelines use PIFF for the PSF; an end-to-end simulation test over 100 deg² finds the additive PSF-error contribution to the non-tomographic cosmic-shear data vector well below 30% of its uncertainty at year-1 and year-10 depth (Hébert et al. 2026, arXiv:2608.21688) [src]. No LSST cosmic-shear cosmology exists yet. | Rubin announcement of 30 June 2026 (relayed by https://www.cmu.edu/physics/news-events/2026/0630_rubin-lsst-officially-begins.html); Rubin community forum posts on EDP2 (https://www.rubin.community/t/early-data-preview-2-edp2-release-date-2026-07-27/12226 and https://www.rubin.community/t/early-data-preview-2-is-now-available/12346) | [src] |
| Roman | Launched 30 August 2026 on a Falcon Heavy; in commissioning; first images expected in early 2027. Weak lensing comes from the High Latitude Imaging Survey; 3×2pt Fisher **forecasts** for it are in Cao et al. 2026 (arXiv:2601.00438); the earlier mission design report is Spergel et al. 2015 (arXiv:1503.03757). | NASA mission page (https://science.nasa.gov/mission/roman-space-telescope/, fetched 2026-10-07) for the date and status; press coverage for the vehicle and the first-image expectation | [src] date and status; [sec] vehicle and first images |

### Design documents and forecasts (all **forecast**)
<!-- key: design-documents-and-forecasts-all-forecast -->

| Survey | Document | What it gives | Flag |
|---|---|---|---|
| Euclid | Laureijs et al. 2011, arXiv:1110.3193 (definition study); Euclid Collaboration 2020, arXiv:1910.09273 (validated Fisher forecasts) | reference forecast methodology for weak lensing, clustering and their combination | — |
| Euclid | Euclid Collaboration 2025, arXiv:2510.09153 (CLOE) | **forecast**: w0–wa figure of merit above 400 for all primary probes combined | [src] |
| Euclid DR1 | Euclid Collaboration 2026, arXiv:2604.00805 | **forecast**: the photometric-clustering n(z) mean must be accurate to 0.004(1+z) to keep 80% of the DR1 3×2pt w0wa constraining power | [src] |
| Euclid DR1 | arXiv:2602.16448 | **forecast**-type study: redshift-dependent TATT recommended for DR1 3×2pt | [src] |
| Euclid | Roster et al. 2025, arXiv:2508.02779 | **forecast** on mocks: the requirement \|Δ⟨z⟩\| ≤ 0.002(1+z) per bin is met by eight of ten bins with SOM calibration when tomography is defined on individual photo-z, and by at most six with a C3R2-like calibration sample | [src] |
| Rubin LSST Y10 | Zhang et al. 2025, arXiv:2507.01374 | **forecast**: in 3×2pt, S8 is most sensitive to the mean redshift of the fourth of five source bins; figures of merit grow with the size and z > 1.6 completeness of the spectroscopic training set | [src] |
| Rubin LSST | Ivezić et al. 2019, arXiv:0805.2366 (science drivers and design); LSST DESC 2018, arXiv:1809.01669 (science requirements) | requirements flow-down for a Stage-IV dark-energy analysis | — |
| Rubin LSST | Robertson et al. 2026, arXiv:2602.21863 | **forecast**: baryon uncertainty nearly doubles the S8 error; with tight baryon and redshift priors LSST cosmic shear is more than five times as constraining as existing surveys | [src] |
| Roman | arXiv:2601.00438 | **forecast**: external priors on n_s, Ω_b, h improve the (σ8, Ωm) figure of merit by factors 1.2–3.5; factor-two changes in photo-z and shear-bias priors change it by ≲ 20% | [src] |

## 4. Public data locations
<!-- key: public-data-locations -->

| Data | Location | Flag |
|---|---|---|
| KiDS DR5 | ESO science archive, Astro-WISE, https://kids.strw.leidenuniv.nl/DR5/ | [src] |
| DES Y6 cosmology products | https://des.ncsa.illinois.edu/releases/y6a2 (the page did not render through the fetch tool; address from a web search result). Y6 Gold: nearly 5000 deg² of grizY, 669 million objects, depth i ≈ 23.4 at S/N ≈ 10 for extended objects (Bechtol et al. 2025, arXiv:2501.05739) [src] | [sec] address |
| HSC-SSP PDR3 | https://hsc-release.mtk.nao.ac.jp (third public release 31 August 2021, about 670 deg² at full depth in five bands; Y3 shape catalogue 434 deg² — from a web-search summary of the release site, not read on the page itself) | [sec] |
| DECADE | shear catalogues, data vectors and likelihoods stated public in arXiv:2509.03582 | [src] |

## Not verified
<!-- key: not-verified -->

- Whether the UNIONS-3500 and KiDS-Legacy shear catalogues are public and where.
- Sample sizes and area of the Rubin `ShearObject` catalogue.
- Dates of Rubin DR1 and of the first Roman High Latitude survey data.
