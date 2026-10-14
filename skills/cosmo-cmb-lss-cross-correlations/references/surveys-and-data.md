# Surveys and data — CMB × LSS cross-correlations

Scope: the CMB maps and the large-scale-structure tracers that enter published cross-correlations, with areas, sample sizes, redshift ranges, public locations and status; then what comes next.
Snapshot: 2026-10-13

Flags: `[src]` read this session in the cited paper; `[sec]` from a named secondary source;
`[der]` derived here. Instrument descriptions of the CMB experiments and their release history are
in `cosmo-cmb`; this file records only what the cross-correlation papers state about the products
they used. A cell left with "—" was not verified this session.

## 1. Reading guide
<!-- key: reading-guide -->

A cross-correlation has two data sets and its area is their overlap. Three numbers are therefore
needed for each analysis and they are often confused: the CMB map area, the tracer area, and the
overlap. Examples: the ACT DR4 lensing map used with DES Y3 covers ~436 deg² while the MagLim
sample covers ~4143 deg² (Marques 2023, arXiv:2306.17268) [src]; SPT-3G D1 covers 1646 deg²
(Chaubal 2026, arXiv:2601.20551) and its overlap with DES Y3 shear is ~1,300 deg² (Ouellette 2026,
arXiv:2606.26223) [src].

## 2. CMB data products
<!-- key: cmb-data-products -->

### 2.1 Past
<!-- key: past -->

| Product | Content as used | Used for | Citation | Flag |
|---|---|---|---|---|
| WMAP + Planck foreground-cleaned temperature maps | combined cleaned maps; an "asymmetric" estimator combines differently cleaned maps | projected-field kSZ | Hill 2016, arXiv:1603.01608; Kusiak 2021, arXiv:2102.01068 | [src] |
| Planck 2015 temperature, polarisation and lensing map | ISW cross-correlations, ISW map, ISW–lensing bispectrum | ISW | Planck Collaboration 2015, arXiv:1502.01595 | [src] |
| Planck PR3 (2018) lensing map | first DESI-LRG and unWISE tomography; void lensing | κ × galaxies | White 2021, arXiv:2111.09898 (PR3 as identified in arXiv:2407.04607); Sartori 2026, arXiv:2605.19763 | [src] |
| Planck y maps | 2013: first all-sky map, from the 100–857 GHz channels; 2015: from 30–857 GHz, delivered with masks and noise characterisation | tSZ × LSS | Planck Collaboration 2013, arXiv:1303.5081; Planck Collaboration 2015, arXiv:1502.01596 | [src] |
| ACTPol, two seasons, 146 GHz | 660 deg² with BOSS CMASS | first velocity-weighted kSZ stack | Schaan 2015, arXiv:1510.06442 | [src] |
| ACT DR4 lensing | ~436 deg² | DES Y3 MagLim × κ | arXiv:2306.17268 | [src] |
| ACT DR4 + Planck lensing, tSZ-cleaned | — | DES Y3 shear × κ | Shaikh 2023, arXiv:2309.04412 | [src] |
| ACT DR4 component-separated map | night-time 2014–2015 data; 2,089 deg² overlap with SDSS DR15 | pairwise kSZ cross-check | Calafut 2021, arXiv:2101.08374 | [src] |
| ACT DR5 co-added 150 and 98 GHz maps | 2008–2018 data; 3,700 deg² overlap with SDSS DR15 | pairwise and stacked kSZ, tSZ | arXiv:2101.08374; Schaan 2020, arXiv:2009.05557 | [src] |
| SPT-SZ + Planck lensing map | 2500 deg² SPT-SZ survey combined with full-sky Planck; built to minimise tSZ bias | DES Y3 5×2pt and 6×2pt | Chang 2022, arXiv:2203.12440 | [src] |
| SPT + Planck Compton-y maps | y maps built from SPT and Planck data; the SPT resolution gives access to the mean gas profile | galaxies × y | Sánchez 2022, arXiv:2210.08633 | [src] |

### 2.2 Current
<!-- key: current -->

| Product | Content | Public location | Citation | Flag |
|---|---|---|---|---|
| Planck PR4 (NPIPE) lensing maps | the Planck lensing map of almost every 2023–2026 analysis in `results.md` §1; reconstruction signal-to-noise almost 20% above PR3, lensing amplitude 1.004 ± 0.024 relative to the Planck 2018 best fit (Carron 2022, arXiv:2206.07773) | — | used in arXiv:2407.04607, arXiv:2506.22416, arXiv:2512.17865 | [src] |
| Planck PR4 frequency maps, nine bands | multi-frequency fits of tSZ, CIB and radio around galaxies | — | Zhao 2026, arXiv:2606.28099 | [src] |
| Planck PR4 NILC Compton-y with CIB moment deprojection | y × κ | — | McCarthy 2023, arXiv:2308.16260 | [src] |
| ACT DR6 lensing map | 9400 deg²; ACT data from 2017 to 2021 | LAMBDA, "ACT (AdvACT) DR6 Lensing Maps", version v1 dated 1 November 2023: κ alm, mask, filter, noise per mode; 400 simulated reconstructions at NERSC | Madhavacheril 2023, arXiv:2304.05203 | [src] for area and years; [sec: LAMBDA product page, read through a web search summary] for the release |
| ACT DR6 component-separated maps | needlet ILC of ACT DR4 + DR6 at ~93, 148, 225 GHz with Planck 30–545 GHz; arcminute-resolution Compton-y, CMB temperature and E-mode maps over ~13,000 deg² | — | Coulton 2023, arXiv:2307.01258 | [src] |
| ACT DR6 temperature maps | co-added 150 GHz, total-frequency and ILC maps "cover 19,000 square degrees" from Advanced ACTPol observations of 2017–2022 | — | Gong 2025, arXiv:2511.23417 | [src] |
| ACT DR6 + Planck co-added 90, 150, 220 GHz maps | stacked tSZ and multi-frequency fits | — | Moore 2026, arXiv:2609.08939; arXiv:2606.28099 | [src] |
| SPT-3G D1 temperature spectra | two years, 95/150/220 GHz, 1646 deg², 1700 ≤ ℓ ≤ 11,000 | — | arXiv:2601.20551 | [src] |
| SPT-3G D1 lensing maps | polarisation-only and temperature-including reconstructions | — | arXiv:2606.26223 | [src] |
| SPT-3G temperature for kSZ | first use with DESI Legacy LRGs; about two thirds of the SPT-3G galaxies are shared with ACT | — | Hotinli 2026, arXiv:2609.17676 | [src] |
| Planck CIB maps, dust-cleaned | lensing tracer; f_NL | — | Hertig 2025, arXiv:2511.21949; Thornton 2026, arXiv:2605.03783 | [src] |

The ACT DR6 lensing map and the ACT DR6 temperature maps do not have the same footprint (9400
against 19,000 deg² as quoted above) [src]: a kSZ analysis and a lensing analysis "with ACT DR6"
do not use the same sky.

ACT and Planck lensing maps are combined in most analyses. They overlap on the sky and share the
lensing signal, so "ACT + Planck" is a joint fit with a cross-covariance, not two independent
measurements [der, from the shared sky and signal]. See `cosmo-cmb` for the reconstructions
themselves.

### 2.3 Planned or starting
<!-- key: planned-or-starting -->

| Experiment | Status | Source | Flag |
|---|---|---|---|
| Simons Observatory | Large Aperture Telescope first light in February 2025 with ~30,000 detectors in bands centred at 90, 150, 220 and 280 GHz; early observations of the 680 deg² Deep56 patch; further LAT upgrades expected to be complete by 2028 | APS April 2026 meeting abstract "The Simons Observatory: Early Maps and Status of the Large Aperture Telescope" and collaboration talks, read through a web search summary on 2026-10-09 | [sec] |
| Simons Observatory data release for cross-correlations | no schedule found | same search | not verified |
| CMB-S4 | lost DOE and NSF support on 9 July 2025 | `cosmo-cmb` SKILL.md | [sec] |

Many forecasts in this domain were written for CMB-S4 and should be reread with that in mind
(`open-questions.md` §9).

## 3. Large-scale-structure tracers
<!-- key: large-scale-structure-tracers -->

### 3.1 Photometric and all-sky samples
<!-- key: photometric-and-all-sky-samples -->

| Sample | Size and selection | Redshift | Calibration of dN/dz | Citation | Flag |
|---|---|---|---|---|---|
| unWISE blue, green, red | three infrared-selected samples, > 500 million galaxies in total; average halo mass ~1–5 × 10¹³ h⁻¹M⊙ | median z ≈ 0.6, 1.1, 1.5; blue 0.2 ≲ z ≲ 1.1, green 0.3 ≲ z ≲ 1.8 | cross-correlation redshifts with spectroscopic samples | arXiv:2102.01068; Krolewski 2021, arXiv:2105.03421; Farren 2023, arXiv:2309.05659 | [src] |
| unWISE Low-z and Mid-z | — | z̄ = 0.14 and 0.23 | — | arXiv:2606.28099 | [src] |
| DESI Legacy Imaging LRGs (the DESI LRG target sample) | ~500 deg⁻² over 18,000 deg² in 2021; LS DR9 samples of ~20,000 deg²; an extended sample with 2–3 times the density | 4 photometric bins over 0.4 ≤ z ≤ 1 | DESI spectroscopy; magnification coefficients and imaging weights released with the sample | White 2021, arXiv:2111.09898; Zhou 2023, arXiv:2309.06443 | [src] |
| DESI Legacy Imaging galaxies | three samples | 0.3–0.45, 0.45–0.6, 0.6–0.8 | — | Qu 2024, arXiv:2410.10808 | [src] |
| DESI BGS imaging sample | — | z ≲ 0.4 | DESI spectroscopy | Sailer 2025, arXiv:2503.24385 | [src] |
| DESI Legacy LRG for f_NL | ~40% of the sky, to z ~ 1.4, neural-network imaging weights | — | DESI Y1 LRG spectra | Bermejo-Climent 2024, arXiv:2412.10279 | [src] |
| 2MASS photometric redshifts and WISE-based low-z samples | — | z ≲ 0.3 | photometric redshifts | Rubiola 2025, arXiv:2510.09563 | [src] |
| Quaia (Gaia + unWISE quasars) | 1,295,502 quasars with G < 20.5; 755,850 with G < 20.0; from 6,649,162 Gaia candidates; selection-function model provided | used in bins centred from z = 0.69 to 2.72 | Gaia BP/RP redshifts improved with SDSS-trained kNN; 6% (10%) of the G < 20.0 sample have \|Δz/(1+z)\| > 0.2 (0.1) | Storey-Fisher 2023, arXiv:2306.17749; Piccirilli 2024, arXiv:2402.05761 | [src] |
| CatNorth quasar candidates | 1.5 million candidates; machine-learnt selection function | split at z = 1.5 | — | Qin 2026, arXiv:2603.09457 | [src] |
| DES Y3 MagLim | ~4143 deg², six bins | 0.20 < z < 1.05 | DES pipeline (see `cosmo-weak-lensing`) | arXiv:2306.17268 | [src] |
| DES Y3 shear catalogue | — | — | see `cosmo-weak-lensing` | arXiv:2606.26223 | [src] |
| KiDS-1000 shear | 1000 deg² | — | see `cosmo-weak-lensing` | Tröster 2021, arXiv:2109.04458 | [src] |
| HSC Y3 shear | used for the lensing side of the f_gas ratio | — | — | Liu 2026, arXiv:2609.22466 | [src] |
| NVSS, SDSS photometric, WISE × SuperCOSMOS, 2MASS photo-z, SDSS QSO | the classical ISW tracer set | to z ~ 0.4 for WISE × SuperCOSMOS | — | Stölzner 2017, arXiv:1710.03238; arXiv:1502.01595 | [src] |

Quaia is public at zenodo.org/records/10403370 (arXiv:2306.17749) [src]. The DESI LRG
cross-correlation samples "will be made publicly available" together with LS DR9 photometric
redshifts trained on DESI spectra (arXiv:2309.06443) [src]; the present location was not checked.

### 3.2 Spectroscopic samples
<!-- key: spectroscopic-samples -->

| Sample | Size as used | Redshift | Used for | Citation | Flag |
|---|---|---|---|---|---|
| BOSS CMASS | 25,537 galaxies in the first ACTPol overlap | 0.4–0.7 | first kSZ stack | arXiv:1510.06442 | [src] |
| BOSS CMASS and LOWZ (DR10, DR12) | — | z_eff = 0.555 and 0.316 for the E_G analysis | kSZ + tSZ profiles; E_G | arXiv:2009.05557; Wenzl 2024, arXiv:2405.12795 | [src] |
| SDSS DR15 LRGs | 343,647 galaxies, five luminosity samples | — | pairwise kSZ | arXiv:2101.08374 | [src] |
| SDSS, two million spectroscopic references | — | to z ~ 3 for the snapshot spectra | tSZ tomography | Chiang 2020, arXiv:2006.14650 | [src] |
| DESI Y1 / DR1 LRG | > 800,000 overlapping ACT DR6 over ≥ 4,000 deg²; 913,286 in the pairwise analysis | 0.4–1.1 | stacked and pairwise kSZ | Ried Guachalla 2025, arXiv:2503.19870; arXiv:2511.23417 | [src] |
| DESI DR1 BGS | 1.6 million with log M⋆/M⊙ > 10 | z ~ 0.3 | pairwise kSZ | Hadzhiyska 2025, arXiv:2510.14135 | [src] |
| DESI DR1 quasars | 1.2 million over 7,200 deg² (~170 deg⁻²), f_sky ~ 20% | 0.8 ≤ z ≤ 3.5, bins at z_eff = 1.44, 2.27, 2.75 | κ × QSO growth and f_NL | de Belsunce 2025, arXiv:2506.22416; Chiarenza 2025, arXiv:2512.17865 | [src] |
| DESI DR2 LRG | 2.4 million | four redshift bins | stacked kSZ, P_ge | Qu 2026, arXiv:2604.19744 | [src] |
| DESI DR2 BGS and ELG | — | with the LRGs, 0.1 ≲ z ≲ 1.6 overall | stacked kSZ | Hadzhiyska 2026, arXiv:2604.19745 | [src] |
| DESI DR2 LRG, ELG, QSO | — | — | kSZ velocity reconstruction | Chaussidon 2026, arXiv:2604.04867 | [src] |
| eBOSS DR16 quasars | ~800 supervoids | 0.8 < z < 2.2 | ISW stacking | Kovács 2021, arXiv:2107.13038 | [src] |
| SDSS DR7 groups | mean mass 10¹⁴ h⁻¹M⊙ | — | rotational kSZ | Yang 2026, arXiv:2603.14494 | [src] |

DESI DR2 spectroscopic catalogues were used by collaboration papers in 2026 (arXiv:2604.19744,
arXiv:2604.19745, arXiv:2604.04867, arXiv:2609.36355, arXiv:2609.22466) [src]. Whether a given
catalogue is public at the snapshot date was not checked; see `cosmo-galaxy-clustering` and
`cosmo-surveys-facilities`.

### 3.3 Structure catalogues and external gas data
<!-- key: structure-catalogues-and-external-gas-data -->

| Data | Content | Citation | Flag |
|---|---|---|---|
| DES supervoids | 87 supervoids, 0.2 < z < 0.9, 5000 deg² | Kovács 2018, arXiv:1811.07812 | [src] |
| DESI Legacy Survey superstructures | voids and clusters in four bins, 0 < z < 0.8 | Hang 2021, arXiv:2105.11936 | [src] |
| DESI Legacy DR9 LRG voids | 3D voids, 0.35 < z < 0.95, classified by potential | arXiv:2605.19763 | [src] |
| DESI Legacy group catalogue | photometric groups, 10^12.5–10^14 h⁻¹M⊙ and above | Roper 2025, arXiv:2510.12553 | [src] |
| eROSITA X-ray gas masses; HSC-XXL gas fractions | calibration and comparison of feedback models | Siegel 2025, arXiv:2509.10455; Siegel 2025, arXiv:2512.02954 | [src] |
| eROMaPPer clusters | optically selected clusters in the DESI Legacy imaging | arXiv:2609.08939 | [src] |
| ROSAT all-sky X-ray maps | shear × X-ray alongside shear × y | La Posta 2024, arXiv:2412.12081 | [src] |

## 4. Simulations that carry the interpretation
<!-- key: simulations-that-carry-the-interpretation -->

| Simulation | Role | Citation | Flag |
|---|---|---|---|
| WebSky | extragalactic foregrounds for lensing-bias tests | arXiv:2309.05659 | [src] |
| Two independent microwave-sky simulations | ACT DR6 lensing foreground mitigation tests | MacCrann 2023, arXiv:2304.05196 | [src] |
| Buzzard | mocks for LRG fits and void-lensing templates | Sailer 2024, arXiv:2407.04607; arXiv:2605.19763 | [src] |
| AbacusSummit | forward model of group catalogues and kSZ maps | arXiv:2510.12553 | [src] |
| FLAMINGO, ANTILLES, BAHAMAS, SIMBA, FABLE | feedback variants compared with kSZ | Bigwood 2025, arXiv:2510.15822; McCarthy 2024, arXiv:2410.19905 | [src] |
| Illustris, IllustrisTNG (TNG300) | weak- and strong-feedback references for kSZ profiles | arXiv:2503.19870; Hadzhiyska 2025, arXiv:2507.14136 | [src] |
| cosmo-OWLS | AGN heating variants for galaxy × y | arXiv:2210.08633 | [src] |
| Millennium XXL | ΛCDM ISW templates at high redshift | arXiv:2107.13038 | [src] |
| ELUCID constrained simulation | rotational kSZ prediction | arXiv:2603.14494 | [src] |

A kSZ or tSZ "preference for strong feedback" is always relative to one of these. The simulation
families are described in `cosmo-simulations-mocks`.

## 5. Which data sets are shared between results
<!-- key: which-data-sets-are-shared-between-results -->

- unWISE: arXiv:2105.03421, arXiv:2309.05659, arXiv:2409.02109 (lensing); arXiv:2110.13959 (ISW);
  arXiv:2102.01068 (kSZ); arXiv:2606.28099 (tSZ); arXiv:2511.21949 (delensing tracer).
- DESI Legacy imaging samples (the LRG sample in most cases): arXiv:2111.09898, arXiv:2407.04607, arXiv:2407.04606,
  arXiv:2510.17796, arXiv:2412.10279 (lensing); arXiv:2407.07152, arXiv:2410.06229,
  arXiv:2506.21684, arXiv:2511.15701, arXiv:2603.28746, arXiv:2609.17676 (kSZ);
  arXiv:2605.18938 (moving lens).
- ACT DR6 lensing: every "ACT DR6" row of `results.md` §1.
- ACT DR6 temperature + DESI spectroscopy: arXiv:2503.19870, arXiv:2511.23417, arXiv:2510.14135,
  arXiv:2604.19744, arXiv:2604.19745, arXiv:2604.04867, arXiv:2609.36355, arXiv:2609.22466.
- DES Y3: arXiv:2203.12440, arXiv:2206.10824, arXiv:2306.17268, arXiv:2309.04412,
  arXiv:2606.26223, arXiv:2510.25596 (lensing); arXiv:2108.01600, arXiv:2506.07432,
  arXiv:2609.31774, arXiv:2412.12081 (tSZ); arXiv:2404.06098 (kSZ-informed shear).

Results inside one of these groups are correlated and cannot be averaged as independent.

## 6. What comes next
<!-- key: what-comes-next -->

- **DESI DR2 and later.** The DR1 BGS pairwise analysis expects "roughly a factor of two" better
  statistical precision with BGS DR2 (arXiv:2510.14135) [src, **forecast**]. Stacked kSZ with ACT,
  DESI Y3 and Rubin is forecast at S/N ~ 50 (arXiv:2503.19870) [src, **forecast**].
- **CMB lensing × DESI spectroscopic clustering.** No collaboration measurement of κ × DESI DR2
  galaxies was found in a date-sorted search on 2026-10-09; the DR1 quasar analyses
  (arXiv:2506.22416, arXiv:2512.17865) and an external DR1 reanalysis (Ivanov 2026,
  arXiv:2601.16165) are the latest [src].
- **DES Y6, Euclid, Rubin × CMB lensing.** No cosmological cross-correlation result with DES Y6,
  Euclid or Rubin data was found in the same search. The newest DES measurement is still Y3 shear
  × SPT-3G D1 (arXiv:2606.26223) [src]. Rubin LSST began on 30 June 2026 and Euclid DR1 lensing
  products are expected in mid-2027 [sec: `cosmo-weak-lensing` SKILL.md].
- **Simons Observatory.** Observing (§2.3); the screening, moving-lens, polarised-SZ and
  velocity-reconstruction papers all name it as the experiment that turns their marginal
  detections into measurements (arXiv:2608.27458, arXiv:2605.18938, arXiv:2607.16071,
  arXiv:2604.04867) [src].
- **SPT-3G.** The D1 release already supports polarisation-only lensing cross-correlations
  (arXiv:2606.26223) and kSZ (arXiv:2609.17676) [src]. The SPT-3G release sequence is in
  `cosmo-cmb`.

## Not verified
<!-- key: not-verified -->

- Release dates and public locations of the Planck PR4 lensing maps, the ACT DR6 component-
  separated maps, the SPT-3G D1 products and the DESI DR2 catalogues.
- The area of the unWISE samples and their number densities per sample.
- Any Simons Observatory data-release date.
