# Surveys and data — dark energy and modified gravity

Scope: the data sets that enter current constraints on `w(z)` and on gravity,
what each contributes to the combination, their status and what comes next.
Instrument and survey details live in the probe skills; this file records what
a dark-energy analysis needs to know about each input.

Snapshot: 2026-10-07

Flags: `[src]` read this session in the cited paper; `[sec]` from a named
secondary source (a sibling skill or an official web page); `[der]` derived
here.

## 1. What each probe contributes to a `w0wa` fit
<!-- key: what-each-probe-contributes-to-a-w0wa-fit -->

| Input | What it fixes | Why the fit needs it | Flag |
|---|---|---|---|
| BAO (galaxies, quasars, Lyα) | `D_M/r_d`, `D_H/r_d`, `D_V/r_d` over `0.1 < z < 4.2` | shape of the distance–redshift relation; alone it defines only a degeneracy direction in `w0`–`wa` | [src] arXiv:2503.14738 |
| CMB, compressed | `theta_*`, `omega_b`, `omega_bc` | anchors `r_d` and `Omega_m`; "most of the information that the CMB provides on w(z)" | [src] arXiv:2503.14738 |
| CMB lensing and full spectra | lensing amplitude, ISW | changes `Delta chi2` (−9.7 → −12.5) without moving the posterior | [src: Sect. IX] arXiv:2503.14738 |
| Type Ia supernovae, uncalibrated | relative `d_L(z)`, densest at `z < 1` | measure `w0` "well independently of wa"; break the BAO degeneracy | [src] arXiv:2503.14738 |
| 3×2pt (cosmic shear + clustering + galaxy–galaxy lensing) | `Omega_m`, `S8` | can replace the CMB as the `Omega_m` anchor, giving a low-redshift-only test | [src] arXiv:2503.14738, arXiv:2605.27221 |
| Full-shape clustering, RSD | `f sigma8`, shape of `P(k)`, AP | growth information; needed for `mu` | [src] arXiv:2411.12026 |
| CMB lensing × galaxies, galaxy–galaxy lensing | Weyl potential | needed for `Sigma` and `E_G` | [src] arXiv:2401.12971 |

BAO + supernovae alone leave `omega_m` poorly determined; "the full
statistical power of the data is achieved through the combination of the BAO,
CMB and SNe datasets" (arXiv:2503.14738) [src].

## 2. Past data sets (superseded for dark energy, still cited)
<!-- key: past-data-sets-superseded-for-dark-energy-still -->

| Data set | Role in this domain | Key numbers | Source | Flag |
|---|---|---|---|---|
| Supernova discovery samples and pre-2022 compilations | established acceleration; first `w` constraints | see `cosmo-supernovae` | — | — |
| Planck 2018 (PR3) | CMB anchor of most 2018–2024 analyses; origin of the Σ0 and lensing-smoothing anomalies | parameter paper: Planck Collaboration 2018, arXiv:1807.06209 | arXiv:2411.12026 | [src] |
| SDSS BOSS / eBOSS (CMASS, LOWZ, DR12, DR16) | BAO and RSD before DESI; lens samples for `E_G`; BOSS full shape still used in EFT dark-energy fits | `E_G` rows in `results.md` Section 8 | arXiv:1511.04457, arXiv:2401.12971, arXiv:2507.00118 | [src] |
| Reyes et al. sample (2010) | first `E_G` measurement, `0.39 ± 0.06` | — | Reyes et al. 2010, arXiv:1003.2185 | [src] |
| KiDS-1000 + BOSS + 2dFLenS | 3×2pt extensions: `w`, `Omega_K`, `Sum m_nu`, `f_R0` | `w = −0.99 (+0.11/−0.13)` | Tröster et al. 2020, arXiv:2010.16416 | [src] |
| DES Y3 3×2pt | extensions: (`w_p`, `wa`), Σ0, μ0, binned `sigma8(z)` | `Sigma0 = 0.6 (+0.4/−0.5)` alone | DES Collaboration 2022, arXiv:2207.05766 | [src] |
| X-ray cluster samples | `f(R)` from the mass function | `log10 abs(f_R0) < −4.79` | Cataneo et al. 2014, arXiv:1412.0133 | [src] |
| GW170817 + GRB 170817A (17 August 2017) | speed of gravitational waves | `abs(c_g/c − 1) ≤ 5 × 10^-16` | LIGO Scientific Collaboration et al. 2017, arXiv:1710.05834; arXiv:1710.05901 | [src] |
| DESI DR1 BAO (2024) | first `w0wa` preference | over 6 million objects, seven redshift bins, `0.1 < z < 4.2` | DESI Collaboration 2024, arXiv:2404.03002 | [src] |
| DES-SN5YR, Union3 (original releases) | supernova inputs of the 2024–2025 claims | superseded by DES-Dovekie and Union3.1 | arXiv:2511.07517, arXiv:2601.19424 | [src] |

## 3. Current data sets
<!-- key: current-data-sets -->

### 3.1 BAO and clustering
<!-- key: bao-and-clustering -->

| Data set | Content | Status at snapshot | Source | Flag |
|---|---|---|---|---|
| DESI DR2 BAO | more than 14 million galaxies and quasars, three years of operation, plus Lyα forest BAO | the current BAO input of every dark-energy fit | DESI Collaboration 2025, arXiv:2503.14738 | [src] |
| DESI DR2 Lyα BAO and full shape | `z_eff = 2.33` | values and caveats in `cosmo-lyman-alpha` | sibling skill | [sec] |
| DESI DR1 full shape | power-spectrum multipoles of the DR1 tracers; latest DESI full-shape data | used for μ, Σ, EFT and `f(R)` tests; combined with DR2 BAO through mock cross-covariance | arXiv:2411.12026, arXiv:2602.18761 | [src] |
| DESI DR1 LRG bispectrum | adds higher-order information | first cosmology in June 2026 | arXiv:2606.23936 | [src] |
| DES Y6 BAO | photometric BAO, part of the DES all-probe combination | — | arXiv:2605.27221 | [src] |

DESI finished its planned survey in April 2026 (Ohio State University news
release of 17 April 2026, "DESI finishes observations for largest 3D map of
universe") [sec]; the sibling `cosmo-galaxy-clustering` gives the same date.
No DESI DR2 full-shape cosmology exists at the snapshot (sibling
`cosmo-galaxy-clustering`) [sec].

### 3.2 Supernovae
<!-- key: supernovae -->

| Sample | Content | Role | Source | Flag |
|---|---|---|---|---|
| DES-Dovekie | ~1600 likely SNe Ia from DES + ~200 low-redshift SNe; recalibrated, SALT3 retrained, colour-law fix | replaces DES-SN5YR | Popovic et al. 2025, arXiv:2511.07517 | [src: abstract] |
| Union3.1 | ~2000 SNe; host properties re-derived from DESI Legacy Imaging Surveys photometry with Prospector; UNITY analysis | replaces Union3 | Hoyt et al. 2026, arXiv:2601.19424 | [src] |
| Pantheon+ with corrected host masses | low-redshift host masses revised | changes 2.8σ to 3.2σ | arXiv:2601.19424 | [src: abstract] |
| Unite | 2884 likely SNe Ia; Pantheon+ ∪ DES-SN5YR with consistent modelling, selection and bias corrections; host masses redetermined for over 98% | the single combined sample | Camilleri et al. 2026, arXiv:2609.05053 | [src: abstract] |

All four share most of the `z < 0.1` anchor. The anchor, its surveys and its
planned replacements are documented in `cosmo-supernovae`.

### 3.3 CMB
<!-- key: cmb -->

| Data | Use | Source | Flag |
|---|---|---|---|
| Planck primary anisotropies with the CamSpec likelihood (DESI DR2 baseline), Plik, or the PR4 `L-H` likelihood; the Planck release behind each is documented in `cosmo-cmb` | primary anisotropies | arXiv:2503.14738 | [src] |
| Planck + ACT CMB lensing | lensing reconstruction in the DESI DR2 baseline | arXiv:2503.14738 | [src] |
| ACT DR6 primary spectra | extended-model tests, with Planck, lensing, DESI DR1, Pantheon+ | Calabrese et al. 2025, arXiv:2503.14454 | [src] |
| SPT-3G D1 + ACT DR6 + Planck ("SPA") | CMB input of the DES-Dovekie, DES Y6 3×2pt and CMBComp analyses | arXiv:2511.07517, arXiv:2601.14559, arXiv:2606.18455 | [src] |
| Compressed likelihoods | (`theta_*`, `omega_b`, `omega_bc`) prior from CamSpec; CMBComp | arXiv:2503.14738, arXiv:2606.18455 | [src] |

Combination names (P-ACT, CMB-SPA), their differences and the τ input are in
`cosmo-cmb`.

### 3.4 Weak lensing and 3×2pt
<!-- key: weak-lensing-and-3x2pt -->

| Data set | Content | Dark-energy / gravity use | Source | Flag |
|---|---|---|---|---|
| DES Y6 3×2pt | ~5000 deg²; 140 million source shapes; 9 million lens positions | `wCDM`; with SN + BAO (+ clusters) the first single-survey all-probe `w0wa` result | DES Collaboration 2026, arXiv:2601.14559, arXiv:2605.27221 | [src] |
| KiDS-Legacy | 1347 deg², `z ≤ 2.0` (as described in an external μ–Σ analysis) | `Sigma0` with CMB | Du et al. 2026, arXiv:2602.03110 | [src: abstract] |
| KiDS-1000, DES Y3, HSC | sources for DESI DR1 and BOSS `E_G` measurements | Rauhut et al. 2025, arXiv:2507.16098 | [src] |
| DES Y3 3×2pt | still the 3×2pt likelihood in DESI DR2 and DESI DR1 MG combinations | arXiv:2503.14738, arXiv:2411.12026 | [src] |

No DES Y6 collaboration paper on modified gravity or other extensions beyond
`w` and `w0wa` was found in a title search on 2026-10-08 (the search returned
the 3×2pt, shear, calibration and dynamical-dark-energy papers only) [src:
arXiv listing].

### 3.5 Probes of screening
<!-- key: probes-of-screening -->

| Data | Used for | Source | Flag |
|---|---|---|---|
| Statistical samples of gas–star offsets and stellar-disk warps | thin-shell-screened fifth forces, Compton wavelength 0.3–8 Mpc | Desmond and Ferreira 2020, arXiv:2009.08743 | [src] |
| Nine massive clusters from CLASH and CLASH-VLT | chameleon and `f(R)` from lensing and kinematic mass profiles | Pizzuti et al. 2026, arXiv:2604.23631 | [src] |
| SH0ES Cepheid–supernova ladder and four TRGB data sets | screened fifth force in distance calibrators | Högås et al. 2025, arXiv:2512.14814 | [src] |
| DESI DR1 power spectrum, all tracers | scale-dependent growth, `f(R)` | Gonzalez et al. 2026, arXiv:2604.26915 | [src] |

## 4. Public products useful for reanalysis
<!-- key: public-products-useful-for-reanalysis -->

| Product | Location or reference | Flag |
|---|---|---|
| DESI DR2 BAO distances and covariance; DESI chains | arXiv:2503.14738, "Data Availability"; locations in `cosmo-galaxy-clustering` | [sec] |
| Compressed CMB prior (means and covariance printed in the paper) | arXiv:2503.14738, appendix on early-Universe priors | [src] |
| CMBComp compressed likelihoods and notebooks | github.com/Amoghsriv/CMBComp, arXiv:2606.18455 | [src] |
| DEslider, supernova systematics in the `w0`–`wa` plane | github.com/sdhawan21/DEslider, arXiv:2409.18668 | [src] |
| hi_class | www.hiclass-code.net, arXiv:1605.06102 | [src] |
| MGCAMB, ISiTGR, EFTCAMB | arXiv:2305.05667, arXiv:1908.00290, arXiv:1312.5742 | [src] |
| Supernova Hubble diagrams and covariances | `cosmo-supernovae` | [sec] |

## 5. What comes next
<!-- key: what-comes-next -->

| Data | When | What it decides | Source | Flag |
|---|---|---|---|---|
| DESI full five-year survey: BAO, then full shape | first dark-energy results expected in 2027 | whether the BAO + CMB preference grows as `sqrt(volume)` or stalls; DR2 full shape for μ, Σ | Ohio State University news release, 17 April 2026 | [sec] |
| Euclid DR1 | "DR1-Foundation" (raw and calibrated images, catalogues, spectra, about 1900 deg²) in November 2026; complete DR1 with clustering and weak-lensing science products in mid-2027 | independent BAO, RSD and lensing; first Euclid `w0wa` and μ–Σ | ESA Euclid "DR1 Timeline" page, www.cosmos.esa.int/web/euclid/dr1-timeline, as returned by a web search on 2026-10-08 | [sec] |
| Modern low-redshift supernova anchors (DEBASS, ZTF) | pending | the low-redshift half of the supernova signal | `cosmo-supernovae` | [sec] |
| Rubin LSST lensing with DESI lenses | full survey | `E_G` able to reject GR for some modified-gravity scenarios (**forecast**) | Leonard et al. 2025, arXiv:2511.19194 | [src] |
| Independent τ (large-scale CMB polarisation, reionisation probes) | see `cosmo-cmb` | whether the CMB side of the mismatch is a τ problem | arXiv:2504.16932 | [src] |
| Rubin and Roman supernovae | see `cosmo-supernovae`, `cosmo-surveys-facilities` | high-redshift supernova statistics; systematics will dominate | arXiv:2409.18668 | [src] |

Forecast statements read this session:

- Euclid: including cross-correlations between probes "is particularly
  relevant for models beyond a cosmological constant and may allow us to
  increase the dark energy Figure of Merit by at least a factor of three"
  (**forecast**; Euclid Collaboration 2019, arXiv:1910.09273) [src]. Results
  depend on flat versus non-flat models and on the non-linear scale cuts; the
  paper gives optimistic and pessimistic settings.
- Euclid, review of pre-launch forecasts for time-varying dark energy,
  phenomenological μ–Σ-type modifications and specific models, with the
  non-linear modelling they require (**forecast**; Euclid Collaboration 2025,
  arXiv:2512.09748) [src]. No number from it was extracted this session.
- Supernova systematics "can shift the inference of w0–wa by a few times the
  error ellipse for future low- and high-z SN Ia compilations" (**forecast**;
  arXiv:2409.18668) [src].
- Caldwell and Linder's target for distinguishing thawing from freezing fields
  is a resolution `sigma(w') ≈ (1 + w)` (arXiv:astro-ph/0505494) [src]. With
  `1 + w_p ≈ 0.05` (arXiv:2503.14738), this is `sigma(wa)` of order 0.05,
  against ~0.2 today [der: `1 + w_p` from the DESI + CMB + DESY5 pivot value
  −0.954; current `sigma(wa)` from the Unite and Dovekie rows of `results.md`;
  `w'` and `wa` treated as equal at `a ≈ 1`].

## 6. Timeline of releases that changed the dark-energy picture
<!-- key: timeline-of-releases-that-changed-the-dark -->

| Date | Release | Effect | Source |
|---|---|---|---|
| Oct 2017 | GW170817 speed of gravity | removed most non-conformal Horndeski dark energy | arXiv:1710.05901 [src] |
| Jul 2022 | DES Y3 extensions | no evidence beyond ΛCDM | arXiv:2207.05766 [src] |
| Apr 2024 | DESI DR1 BAO | 2.5–3.9σ `w0wa` preference | arXiv:2404.03002 [src: abstract] |
| Nov 2024 | DESI DR1 full shape, modified gravity | GR consistent; PR3 Σ0 tension traced to the likelihood | arXiv:2411.12026 [src] |
| Mar 2025 | DESI DR2 BAO | 2.8–4.2σ | arXiv:2503.14738 [src: abstract] |
| Nov 2025 | DES-Dovekie | 4.2σ → 3.2σ | arXiv:2511.07517 [src: abstract] |
| Jan 2026 | Union3.1; DES Y6 3×2pt | samples converge at 3.2–3.4σ; `w = −1.12 (+0.26/−0.20)` from 3×2pt | arXiv:2601.19424, arXiv:2601.14559 [src] |
| Feb 2026 | DESI DR1 FS + DR2 BAO | 1.4σ without CMB | arXiv:2602.18761 [src] |
| Apr 2026 | DESI survey complete; DESI DR1 `f(R)` | `log10 abs(f_R0) < −4.59` | arXiv:2604.26915 [src] |
| May 2026 | DES Y6 all-probe `w0wa` | 2.2σ alone, 3.0σ with DESI and CMB | arXiv:2605.27221 [src: abstract] |
| Jun 2026 | DESI DR1 bispectrum + DR2 BAO | weakens the DESI-only preference | arXiv:2606.23936 [src] |
| Sep 2026 | Unite | 3.3σ, weak Bayesian evidence | arXiv:2609.05053 [src] |
