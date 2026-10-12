# surveys-and-data — cosmo-inflation-primordial

Snapshot: 2026-10-07

Scope: the experiments and data releases behind primordial-physics constraints — B-mode polarimeters, the CMB temperature and polarisation data that fix n_s, the CMB and galaxy data used for non-Gaussianity, curvature, features and birefringence — past, current and planned.

General CMB instrument descriptions (Planck, ACT, SPT-3G, their likelihoods and release locations) are in `cosmo-cmb`; galaxy-survey descriptions are in `cosmo-galaxy-clustering` and `cosmo-surveys-facilities`. This file keeps what matters for primordial physics.

## 1. B-mode experiments

### Past and completed data sets

| Experiment / release | Sky and depth | Frequencies | Result for r | Citation | Flag |
|---|---|---|---|---|---|
| BICEP2/Keck × Planck (2015) | about 400 deg²; 57 nK·deg in Q and U (BICEP2/Keck); Planck 1.2 μK·deg at 143 GHz | 150 GHz with Planck 30–353 GHz | r_0.05 < 0.12; lensing B modes at 7.0σ | arXiv:1502.00612 | [src] |
| SPIDER, 2015 balloon flight | 4.8% of the sky | 95, 150 GHz | r < 0.11 (Feldman–Cousins) | arXiv:2103.13334 | [src] |
| Planck PR4 (NPIPE) | more than 50% of the sky for B modes | 30–857 GHz | r < 0.056 (with TT) | arXiv:2010.01139 | [src] |
| BK14 + SPTpol + Planck delensing | BICEP/Keck patch | — | first delensed r limit; σ(r) reduced by about 10% | arXiv:2011.08163 | [src] |
| BK18 (BICEP2, Keck Array, BICEP3 to 2018) | about 600 deg² at 95 GHz, about 400 deg² at 150 and 220 GHz; 2.8, 2.8, 8.8 μK·arcmin | 95, 150, 220 GHz, with WMAP and Planck 23–353 GHz | r_0.05 < 0.036, σ(r) = 0.009 | arXiv:2110.00483 | [src] |
| SPT-3G 2019–2020 BB | about 1500 deg² overlapping the BICEP/Keck patch; 9.3 and 6.7 μK·arcmin white noise at 95 and 150 GHz | 95, 150, 220 GHz | r < 0.25, σ(r) = 0.067 | arXiv:2505.02827 | [src] |

### Current

- **BICEP3 and BICEP Array (South Pole).** The collaboration is preparing a "BK24" release covering data from 2016 through 2024. For BICEP3 at 95 GHz over 2016–2024 the residual temperature-to-polarisation leakage after extended deprojection is equivalent to r = (1.12 ± 0.06) × 10⁻³, down from (4.5 ± 0.7) × 10⁻³ with the standard deprojection (arXiv:2608.25016) [src]; the paper calls these results preliminary. BICEP Array receivers at 150 and 220/270 GHz were characterised in the 2026 season and a 90/150 GHz receiver (BA4) is in integration, according to the titles of the August 2026 instrument papers returned by the arXiv search (not cited here individually).
- **Simons Observatory (Atacama).** The original plan was three Small Aperture Telescopes (SATs) observing about 10% of the sky to 2 μK·arcmin, plus a Large Aperture Telescope on about 40% of the sky at 6 μK·arcmin, in six bands at 27, 39, 93, 145, 225 and 280 GHz with 60,000 bolometers, for a **forecast** σ(r) = 0.003 (Simons Observatory 2019, arXiv:1808.07445) [src]. The plan was enlarged: by 2027 six SATs, with 48,160 detectors in the 93 and 145 GHz channels, and a survey extended to 2035 (Simons Observatory 2025, arXiv:2512.15833) [src]. No SO measurement of r was found in the searches of 2026-10-09.
- **SPT-3G (South Pole).** Besides the BB analysis above, SPT-3G supplies the delensing template for BICEP/Keck. A successor receiver, SPT-3G+, is planned for installation in early 2029 with 6,020 dichroic pixels (Natoli et al. 2026, arXiv:2608.20236; from the abstract snippet) [src].

### Planned

| Experiment | Configuration | Target (all **forecasts**) | Citation | Flag |
|---|---|---|---|---|
| Simons Observatory, expanded SATs | six SATs by 2027, survey to 2035 | σ(r) = 1.2 × 10⁻³ for r = 0, ℓ_knee = 50, moderately complex foregrounds, 70% of lensing B modes removed; 7 × 10⁻⁴ with optimistic noise and foregrounds; about 2.5 times better than the original three-SAT, five-year plan | arXiv:2512.15833 | [src] |
| LiteBIRD, 2021 concept | 15 bands over 34–448 GHz, 2.2 μK·arcmin, 0.5° at 100 GHz, three-year survey, launch then given as the late 2020s | see paper | LiteBIRD Collaboration 2022, arXiv:2202.02773 | [src] |
| LiteBIRD after the mission reformation that followed the 2024 Mission Definition Review | one cross-Dragone telescope of 500 mm aperture, 12 bands with centres from 40 to 402 GHz (optical coverage 34–448 GHz), cooled to about 5 K, detectors at 0.1 K, L2 Lissajous orbit, nominal three-year survey | total δr < 0.002 (68%), including foreground residuals, statistics, systematics and margin | LiteBIRD Collaboration 2026, arXiv:2607.25285 | [src] |
| CMB-S4 | — | no longer supported: DOE and NSF withdrew support on 9 July 2025 | reported in the `cosmo-cmb` skill | [sec] |

The LiteBIRD requirement was relaxed with the reformation: the pre-reformation literature quotes δr < 0.001, the 2026 overview δr < 0.002. Only the second number was read at source this session (arXiv:2607.25285); the first is listed under "Not verified". The launch date after reformation is given as JFY2036 in the `cosmo-cmb` skill [sec]; it is not in the abstract read here.


## 2. CMB temperature and E-mode data (n_s, running, binned P(k), isocurvature, curvature, features)

Instrument descriptions, likelihood names and data locations are in `cosmo-cmb`. What matters here is which combination a primordial constraint is quoted for, because the named combinations differ in content.

| Name in the literature | Content | Used for | Citation | Flag |
|---|---|---|---|---|
| Planck 2018 (PR3) | temperature, polarisation, lensing; Plik high-ℓ likelihood | n_s = 0.9649 ± 0.0042; r_0.002 < 0.10; isocurvature; features; non-parametric P(k) | arXiv:1807.06211 | [src] |
| Planck PR4 (NPIPE) | reprocessed maps; more than 50% of the sky for B modes; 600 simulations for the bispectrum analysis | r from Planck alone; f_NL; feature searches with CamSpec | arXiv:2010.01139, arXiv:2504.00884, arXiv:2605.30236 | [src] |
| ACT DR6 | small-scale TT, TE, EE; binned P(k) to k = 0.43 Mpc⁻¹ | running, binned P(k), small-scale isocurvature | arXiv:2503.14452, arXiv:2503.14454 | [src] |
| P-ACT | ACT DR6 + Planck PR3 cut at ℓ < 1000 (TT) and ℓ < 600 (TE, EE) | n_s = 0.9709 ± 0.0038 | arXiv:2503.14452 | [src] |
| P-ACT-LB | P-ACT + ACT and Planck CMB lensing + DESI DR1 BAO | n_s = 0.974 ± 0.003; running; Ω_K; with BK18, r < 0.038 | arXiv:2503.14452, arXiv:2503.14454 | [src] |
| SPT-3G D1 | 2019–2020 observations of the SPT-3G Main field, 4% of the sky | enters CMB-SPA | arXiv:2506.20707 (abstract snippet) | [src] |
| CMB-SPA | SPT-3G D1 + ACT DR6 + Planck | n_s = 0.9679 ± 0.0033 | arXiv:2506.20707 | [src] |
| "CMB-PAS" | Planck + ACT + SPT as combined by Cheslog et al. | n_s and α_s with N_eff and Σm_ν free; binned P(k) to 0.5% at k = 0.2 Mpc⁻¹ | arXiv:2609.35964 | [src] |
| "CMB" in DESI papers | CamSpec rather than Plik, with ACT lensing added | Ω_K = 0.0023 ± 0.0011 with DESI DR2 | arXiv:2503.14738 | [src] |

P-ACT, CMB-SPA and "CMB-PAS" are three different products. The first truncates Planck to avoid double counting with ACT; the second and third are built by different groups. A value of n_s must be attributed to one of them by name.

**Forecast** for the scalar spectrum: SO-like and CMB-HD-like surveys would constrain e^(−2τ) P_R at k = 0.2 Mpc⁻¹ to 0.1%, and a CMB-HD-like survey would reach k = 30 Mpc⁻¹ to within a factor of ten (arXiv:2609.35964) [src].

## 3. Lyman-α forest data for the running

The 1D flux power spectrum reaches k of order 1 Mpc⁻¹ and is the long lever arm for dn_s/dln k. Two generations exist: the eBOSS DR14 P1D, which with Planck gave dn_s/dln k = −0.010 ± 0.004 (arXiv:1911.09073, quoted through arXiv:2503.14454) [sec], and the DESI DR1 P1D, which with DESI BAO and Planck, ACT and SPT-3G gives 0.0014 ± 0.0041 (arXiv:2601.21432) [src]. The data and their systematics are described in `cosmo-lyman-alpha`.

## 4. Data used for primordial non-Gaussianity

### CMB

| Data set | Content | Result | Citation | Flag |
|---|---|---|---|---|
| WMAP 5-year | temperature | first optimal equilateral and orthogonal limits | arXiv:0905.3746 | [src] |
| Planck 2015 | full-mission T and E; polarisation labelled preliminary | f_NL^local = 0.8 ± 5.0 (T + E) | arXiv:1502.01592 | [src] |
| Planck 2018 (PR3) | T and E, including polarisation at 4 ≤ ℓ < 40; KSW, binned and modal estimators | f_NL^local = −0.9 ± 5.1 | arXiv:1905.05697 | [src] |
| Planck PR4 | T and E; binned and integrated-bispectrum estimators; 600 simulations | f_NL^local = −0.1 ± 5.0 | arXiv:2504.00884 | [src] |
| ACT DR6 SZ cluster catalogue | 1,201 clusters, 10,347 deg² Legacy region | f_NL = 55 ± 125 from counts | arXiv:2602.03917 | [src] |

No ground-based primary-CMB bispectrum measurement of f_NL (ACT, SPT) was found in the searches of 2026-10-09.

### Galaxy and quasar surveys

| Survey / sample | Size and range | Statistic | Citation | Flag |
|---|---|---|---|---|
| SDSS compendium (2008) | several samples; dominated by photometric quasars | power spectra | arXiv:0805.3580 | [src] |
| BOSS DR12 galaxies | — | P(k) scale-dependent bias; P + B with EFT | arXiv:2205.05673, arXiv:2201.07238, arXiv:2201.11518 | [src] |
| eBOSS DR14 quasars | — | redshift-weighted P(k) | arXiv:1904.08859 | [src] |
| eBOSS DR16 quasars | 343,708 quasars, 0.8 < z < 2.2, 4808 deg² | P(k) monopole, neural-network imaging weights | arXiv:2106.13725 | [src] |
| DESI DR1 LRG | 1,631,716 galaxies, 0.6 < z < 1.1 | P(k), blinded | arXiv:2411.17623 | [src] |
| DESI DR1 QSO | 1,189,129 quasars, 0.8 < z < 3.1 | P(k), blinded | arXiv:2411.17623 | [src] |
| DESI DR1 LRG, QSO, ELG | 0.8 < z < 3.1 | auto- and cross-spectra | arXiv:2604.05213 | [src] |
| DESI DR1 public catalogues | six tracers | external P + B reanalysis; feature search | arXiv:2512.04266, arXiv:2610.10530 | [src] |
| DESI DR1 QSO × Planck PR4 lensing | 1.2 million quasars, 0.8 < z < 3.5, f_sky about 20%, three bins | pseudo-C_ℓ cross-spectra | arXiv:2512.17865 | [src] |
| Quaia (Gaia–unWISE quasars) | two tomographic bins | angular auto-spectra and CMB-lensing cross-spectra | arXiv:2504.20992 | [src] |
| DESI Legacy Imaging LRGs × ACT DR5 | northern Galactic hemisphere | kSZ velocity reconstruction, 11.7σ detection | arXiv:2506.21657 | [src] |

DESI DR2 BAO uses more than 14 million galaxies and quasars from three years of operation (arXiv:2503.14738) [src]; no DR2 f_NL analysis was found. According to the `cosmo-galaxy-clustering` skill, DESI completed its planned survey in April 2026 and full-survey results are expected in 2027 [sec].

## 5. SPHEREx and Euclid

### SPHEREx

SPHEREx is the only running experiment whose primary cosmology requirement is f_NL. Facts read in Bock et al. 2025, arXiv:2511.02985 (abstract and requirements section) [src]:

| Item | Value |
|---|---|
| Launch | 11 March 2025 |
| Survey | first all-sky near-infrared spectral survey; the full sky mapped four times in two years; two deep fields near the ecliptic poles |
| Spectral coverage | 102 bands, 0.75–5.0 μm, resolving power 35 to 130 |
| Pixel | 6.2 arcsec |
| Depth (5σ) after four passes | 19.5–19.9 AB mag at 0.75–3.8 μm; 17.8–18.8 AB mag at 3.8–5.0 μm |
| f_NL requirement | Δf_NL < 0.5, "to meaningfully discriminate between single-field and multi-field inflation models" (**forecast**, not a measurement) |
| Flow-down | point-source sensitivity better than 18.4 AB mag (5σ) per spectral channel in bands 1–4; the in-flight median is 19.7 AB mag |
| Systematic allocation | spurious clustering δn/n < 0.2% rms per dex |
| Redshifts | power spectrum: many low-accuracy redshifts, σ_z/(1+z) < 0.2; bispectrum: smaller samples with accuracy up to σ_z/(1+z) = 0.003 |
| Sample | several hundred million galaxies over the full sky |
| Data | spectral images released rapidly to the public; specialised catalogues later in the mission |

The forecast behind Δf_NL < 0.5 assumes the universality relation for b_φ and leaves out the non-Gaussian part of the covariance and the power spectrum–bispectrum covariance; the mission paper states that these effects "might reduce the f_NL sensitivity by tens of percent" and that a multi-tracer analysis may improve it (arXiv:2511.02985) [src]. The original proposal described R = 40 spectra over 0.75–4.1 μm and R = 150 over 4.1–4.8 μm (Doré et al. 2014, arXiv:1412.4872) [src]; the flown instrument differs, so the 2014 numbers are superseded. No SPHEREx cosmology result was found in the searches of 2026-10-09.

### Euclid

All numbers are **forecasts** (Fisher) from Euclid Collaboration 2025, arXiv:2507.15819 [src]; "pessimistic (optimistic)" refers to the paper's two settings.

| Quantity | Forecast | Assumption |
|---|---|---|
| σ(f_NL^local) | 2.2 | spectroscopic P + B, k_max = 0.15 h Mpc⁻¹, universal mass function |
| σ(f_NL^equil) | 108 | same |
| σ(f_NL^ortho) | 33 | same |
| σ(f_NL^local), field level | 2.3 | BORG at 62.5 h⁻¹Mpc resolution on Euclid-like data |
| σ(Ω_K) | 0.0044 (0.003) | spectroscopic + photometric probes |
| σ(α_s) | 0.004 (0.0015) | fiducial α_s = −0.001 |
| Feature amplitude, relative error | 21% (18%) linear, 22% (18%) logarithmic | fiducial amplitude 0.01 |

According to the `cosmo-galaxy-clustering` skill, Euclid DR1 clustering products are expected in mid-2027 [sec].

## 6. Polarisation data used for birefringence

| Data | Role | Citation | Flag |
|---|---|---|---|
| Planck PR3 polarisation | first joint fit of β and miscalibration angles | arXiv:2011.11254 | [src] |
| Planck PR4 | nearly full sky; dependence on the Galactic mask studied | arXiv:2201.07682 | [src] |
| WMAP + Planck PR4 | 23–353 GHz; test of frequency dependence | arXiv:2205.13962 | [src] |
| ACT DR6 | EB and TB with optics-model priors on the angles | arXiv:2509.13654 | [src] |
| ACT DR6 + Planck PR4 maps | cross-spectra between the two telescopes | arXiv:2608.06480 | [src] |
| BK18 (95, 150, 220 GHz) | multipole-dependent rotation only | arXiv:2603.06812 | [src] |
| SPT-3G D1 and SPTpol BB | anisotropic birefringence; foreground-marginalised likelihoods public at github.com/lbalkenhol/candl_data | arXiv:2510.07928 | [src] |
| ACT DR6 | anisotropic birefringence and screening | arXiv:2608.27458 | [src] |

## 7. What comes next

| When | What | Decides | Source | Flag |
|---|---|---|---|---|
| not dated in the sources read | BICEP/Keck "BK24" (data 2016–2024) | whether σ(r) falls below 0.009 | arXiv:2608.25016 | [src] |
| by 2027, survey to 2035 | SO with six SATs | **forecast** σ(r) = 1.2 × 10⁻³ | arXiv:2512.15833 | [src] |
| early 2029 | SPT-3G+ installation | delensing and small-scale polarisation | arXiv:2608.20236 | [src] |
| 2027 (per `cosmo-galaxy-clustering`) | DESI full-survey results | f_NL from the full quasar and LRG samples | sibling skill | [sec] |
| mission in progress (two-year survey from 2025) | SPHEREx galaxy catalogue | **forecast** Δf_NL < 0.5 | arXiv:2511.02985 | [src] |
| mid-2027 (per `cosmo-galaxy-clustering`) | Euclid DR1 | **forecast** σ(f_NL^local) = 2.2 for the full survey | arXiv:2507.15819 | [src] |
| JFY2036 (per `cosmo-cmb`) | LiteBIRD launch | **forecast** δr < 0.002; β = 0.3° at 5–13σ (pre-reformation design) | arXiv:2607.25285, arXiv:2503.22322 | [src] |

## 8. Not verified

- LiteBIRD's pre-reformation requirement, usually quoted as δr < 0.001: not in the abstract of arXiv:2202.02773 and not read in its body.
- LiteBIRD launch date after reformation: taken from the `cosmo-cmb` skill, not from arXiv:2607.25285.
- Simons Observatory: no first-light date, data release or measured r was read; only forecasts and the expansion plan.
- BICEP Array receiver status in 2026: from titles of instrument papers only, not cited.
- The date of the BK24 release: not stated in any abstract read.
- SPHEREx public data-release schedule and the number of all-sky passes completed by October 2026: not read.
- Sample sizes of BOSS DR12 and eBOSS DR14 as used in the f_NL analyses: not in the abstracts read.
- AliCPT, CLASS, POLARBEAR/Simons Array, QUIJOTE and other B-mode experiments: not researched within the budget.
- CMB-S4 status: taken from the `cosmo-cmb` skill.
