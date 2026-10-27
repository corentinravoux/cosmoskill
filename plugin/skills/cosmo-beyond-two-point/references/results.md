# Results — statistics beyond the two-point function

Scope: headline constraints from each statistic, with an explicit status column: survey data with blinding or mock challenge, survey data without, or simulations only.
Snapshot: 2026-10-26


## 0. Status of every statistic: data or simulations
<!-- key: status-of-every-statistic-data-or-simulations -->

"Validated" names the strongest test reported in the papers read this
session. "Collab." marks a result published by the survey collaboration.

| Statistic | Cosmological constraint from survey data? | Strongest validation | Collab. |
|---|---|---|---|
| Bispectrum monopole with P (tree level or one loop) | Yes: BOSS, DESI DR1 | Large-volume N-body fits; Beyond-2pt masked challenge (EFT P + B) | Yes (DESI DR1) |
| Bispectrum f_NL (equilateral, orthogonal) | Yes: DESI DR1, external reanalysis | EFT scale cuts | No |
| Trispectrum full shape | No | 200 h⁻³Gpc³ of simulations (arXiv:2610.08908, abstract) | — |
| Parity-odd 4PCF | Measured in BOSS and DESI DR1; no accepted detection | Cross-patch and 8PCF-free statistics give nulls | Yes (DESI DR1 measurement) |
| Void–galaxy AP and RSD | Yes: SDSS MGS, BOSS, eBOSS | Survey mocks; Beyond-2pt light cone (Ω_m recovered within 95%; arXiv:2405.02252, Sect. II.2) | Yes (eBOSS DR16) |
| Void size function | Yes: BOSS DR12, DR16 | Model calibrated on mocks; Beyond-2pt light cone with informative priors | No |
| Void lensing (shear, CMB lensing) | Detections and amplitude tests only | Matched mocks | DESI paper for CMB lensing |
| Void–Lyα forest cross-correlation | Detection (8σ; arXiv:2203.11045, abstract) and forest β; no cosmological parameter | Simulated Stripe 82 observations | No |
| Density-split clustering | Yes: BOSS CMASS | 84× volume recovery (arXiv:2309.16541, abstract); Beyond-2pt redshift-space mocks | No |
| kNN | No data result found | Beyond-2pt redshift-space mocks | — |
| Wavelet scattering transform (clustering) | Yes: BOSS CMASS | Mock recovery (emulator); failed σ8 robustness in SimBIG | No |
| Minkowski functionals (clustering) | Yes: BOSS CMASS | Internal and external mocks, including non-HOD | No |
| Marked power spectrum | Yes: 10% of BOSS (arXiv:2310.15243, abstract), via SimBIG | SimBIG test sets | No |
| Galaxy multiplets | Galaxy–halo connection only (DESI DR2 LRG) | Comparison with HOD mocks | Yes |
| Third-order shear ⟨M_ap³⟩ | Yes: DES Y3, HSC Y3, KiDS-Legacy | Simulated likelihood analyses, internal consistency | Yes (DES, KiDS) |
| Lensing peaks, PDF, MFs, scattering, topology, CNN | Yes: DES Y3, HSC Y1, KiDS-450/1000 | Coverage tests, feedback contamination tests | Yes (DES Y3) |
| Field-level inference with sampled initial conditions | No parameters; reconstructions of 2M++, BOSS, Quaia | Posterior predictive tests; CMB-lensing cross-correlation; Beyond-2pt real space, σ8 only | No |
| Gaussian field-level likelihood | Yes: one of the three DESI DR1 peculiar-velocity fσ8 estimators [sec, `cosmo-peculiar-velocities`] | 675 mocks (Bautista et al. 2025, arXiv:2512.03228, abstract) | Yes |
| Neural field-level (CNN summary, LiFT) | Yes: 10% of BOSS (arXiv:2310.15243, abstract); DESI DR1 LRG BAO | Changed-forward-model mock sets | No |
| SBI of P + B | Yes: 10% of BOSS (arXiv:2310.15243, abstract) | SimBIG mock challenge; Beyond-2pt | No |

## 1. Bispectrum, trispectrum, parity-odd four-point function
<!-- key: bispectrum-trispectrum-parity-odd-four-point -->

### 1.1 Bispectrum full shape — current values
<!-- key: bispectrum-full-shape-current-values -->

All rows are fits to survey data validated on mocks. "P+B" means power
spectrum multipoles plus bispectrum monopole unless stated.

| Quantity | Value | Data | Model and priors | Citation | Flag |
|---|---|---|---|---|---|
| Ω_m | 0.310 ± 0.012 | DESI DR1 P+B, ShapeFit | ΛCDM | arXiv:2603.19356 | [src: abstract] |
| H0 | 68.92 ± 0.97 km/s/Mpc | same | ΛCDM | arXiv:2603.19356 | [src: abstract] |
| Σm_ν | < 0.1 eV (95%) | same | ΛCDM + Σm_ν | arXiv:2603.19356 | [src: abstract] |
| Gain on ln(10¹⁰A_s) from B | about 20% smaller error | same | ΛCDM | arXiv:2603.19356 | [src: abstract] |
| Shift of σ8, S8 when adding B | +1.1σ, +1.2σ; errors smaller by 26%, 28% | DESI DR1 FS (P+B, LRG bispectrum) + DR2 BAO | ΛCDM | arXiv:2606.23936 | [src: abstract] |
| Ω_m, σ8, h, S8 | 0.3085 ± 0.0085, 0.868 ± 0.025, 0.6841 ± 0.0059, 0.880 ± 0.026; S8 about 3σ above DES Y6 and within about 1σ of CMB-only values, per the paper | same, with BBN and a wide n_s prior | ΛCDM | arXiv:2606.23936 | [src: Eq. 18, Sect. 4.2.1] |
| w0wa preference | 2.8σ with CMB; 1.6σ with DES-Dovekie SNe; 3.1σ with both; within 1σ of Λ for DESI alone | same | w0waCDM | arXiv:2606.23936 | [src: abstract] |
| Σm_ν | 0.26 ± 0.17 eV, < 0.57 eV (95%) | same, DESI only | ΛCDM + Σm_ν | arXiv:2606.23936 | [src: abstract] |
| μ0 | 0.12 ± 0.49 | same, DESI only | modified gravity (μ0) | arXiv:2606.23936 | [src: abstract] |
| Ω_m, H0, σ8 | 0.284 ± 0.011, 70.7 ± 1.1, 0.811 ± 0.030 | DESI DR1 P_ℓ + B0, independent pipeline | ΛCDM, priors on ω_b and n_s | arXiv:2507.13433 | [src: abstract] |
| Ω_m, H0, σ8 | 0.296 ± 0.007, 68.8 ± 0.6, 0.818 ± 0.029 | same + DESI DR2 BAO | ΛCDM | arXiv:2507.13433 | [src: abstract] |
| Gain on ω_cdm and amplitude from B0 | 15% and 10% (combined LRG); 6% and 4% (all tracers) | DESI DR1 LRG ×3 + QSO | ΛCDM, tree-level B | arXiv:2610.01836 | [src: abstract] |
| Gain on σ8 from B_000, same pipeline | 5% (combined LRG), 1% (all tracers); 2–14% per LRG bin | same, k_max = 0.20 h Mpc⁻¹ | ΛCDM | arXiv:2610.01836 | [src: Table 3] |
| Gain on ω_cdm, Ω_m, σ8 from B_0 | 11%, 8%, 10%; Ω_m moves up by 0.8σ | DESI DR1 six tracers, B at k < 0.08 h Mpc⁻¹ | ΛCDM | arXiv:2507.13433 | [src: Sect. VI.1] |
| f/f^fid per LRG bin | 0.888 +0.186/−0.089, 0.977 +0.182/−0.220, 1.030 +0.368/−0.085 | DESI DR1 LRG P+B | ShapeFit, Planck fiducial | arXiv:2503.09714 | [src: abstract] |
| Cumulative precision | 10.1% on f, 8.4% on σ_s8; σ(α_iso) = 0.9%, σ(α_AP) = 2.3%, σ(fσ_s8) = 5.1% | DESI DR1 LRG + QSO P+B | ShapeFit | arXiv:2503.09714 | [src: abstract] |
| σ8, h, Ω_m | 0.794 ± 0.037, 0.692 ± 0.011, 0.311 ± 0.010 | BOSS DR12, one-loop B0 + tree B2 | ΛCDM, n_s fixed, BBN prior | arXiv:2206.08327 | [src: abstract] |
| H0, Ω_m, σ8, S8 | 68.2 ± 0.8, 0.33 ± 0.01, 0.736 ± 0.033, 0.77 ± 0.04 | BOSS DR12 P_ℓ + B_ℓ + real-space P + BAO | ΛCDM, BBN, Planck n_s | arXiv:2302.04414 | [src: abstract] |
| H0, σ8 | 68.31 +0.83/−0.86, 0.722 +0.032/−0.036 | BOSS DR12 P+B0 | ΛCDM, n_s from Planck | arXiv:2112.04515 | [src: abstract] |
| H0, σ8, n_s | 69.6 +1.1/−1.3, 0.692 +0.035/−0.041, 0.870 +0.067/−0.064 | same | ΛCDM, n_s free, BBN prior | arXiv:2112.04515 | [src: abstract] |
| S8 | 0.751 ± 0.039 | same | abstract does not say which n_s treatment | arXiv:2112.04515 | [src] |

The DESI DR1 P+B Σm_ν limit of arXiv:2603.19356 (< 0.1 eV, abstract) and the DESI-only
value of arXiv:2606.23936 (0.26 ± 0.17 eV, abstract) are not in conflict as stated: the
abstracts describe different data combinations, and the second is explicitly
"DESI-only". Read the body before comparing them.

### 1.2 Primordial non-Gaussianity from the bispectrum
<!-- key: primordial-non-gaussianity-from-the-bispectrum -->

| Quantity | Value (68%) | Data | Citation | Flag |
|---|---|---|---|---|
| f_NL^loc | −0.1 ± 7.4 | DESI DR1 P + B, one-loop EFT | arXiv:2512.04266 | [src: abstract] |
| f_NL^equil | 719 ± 390 | same | arXiv:2512.04266 | [src: abstract] |
| f_NL^orth | −200 ± 100 | same | arXiv:2512.04266 | [src: abstract] |
| f_NL^equil, f_NL^orth | 200 ± 230, −24 ± 86 | high-z DESI + BOSS, simulation-based bias priors | arXiv:2512.04266 | [src: abstract] |
| f_NL^loc | −0.0 ± 4.1 | DESI DR1 + CMB | arXiv:2512.04266 | [src: abstract] |

These are from an independent reanalysis of public DESI catalogues, not a
collaboration result; the collaboration's own f_NL^loc from the power spectrum
is in `cosmo-galaxy-clustering`. The f_NL^loc value
inherits the b_φ assumption discussed in that skill.

### 1.3 Parity-odd four-point function
<!-- key: parity-odd-four-point-function -->

| Claim | Value | Data | Citation | Flag |
|---|---|---|---|---|
| Parity-odd 4PCF, χ² against Patchy mocks | 7.1σ (CMASS), 3.1σ (LOWZ) | BOSS DR12 | arXiv:2206.03625 | [src: abstract] |
| Rank test, blind | 2.9σ (99.6%) | BOSS CMASS, 20–160 h⁻¹Mpc | arXiv:2206.04227 | [src: Sect. VIII] |
| 18 inflationary templates | all below 2σ | BOSS | Cabass, Ivanov & Philcox 2022, arXiv:2210.16320 | [src: abstract] |
| Noise from GLAM-Uchuu N-body mocks | 1.4σ baseline (was > 3.5σ with Patchy, same cuts) | BOSS CMASS + LOWZ | arXiv:2401.09523 | [src: abstract] |
| χ²_× and χ²_null statistics | parity signal 0–2.5σ; parity-even 8PCF bias term ≈ 6σ | BOSS | Krolewski et al. 2024, arXiv:2407.03397 | [src: abstract] |
| Lyα forest 4PCF | no evidence with bootstrap covariance | SDSS DR16 | arXiv:2405.04660 | [src] |
| Connected parity-even 4PCF (for reference) | 8.1σ; 4.7σ with sides above 14 h⁻¹Mpc | BOSS CMASS | arXiv:2108.01670 | [src: abstract] |
| DESI DR1 LRG, auto | 4–10σ excess over mocks (abstract); in the body 11.4σ (NGC) and 7.0σ (SGC) against 25 Abacus mocks, 6.6σ and 5.7σ against 1000 EZmocks | DESI DR1 | arXiv:2508.09133 | [src: Sect. V.2] |
| DESI DR1 LRG, cross between patches | no detection (−1.0σ NGC, −0.8σ SGC); in significant tension with the auto result | DESI DR1 | arXiv:2508.09133 | [src: Sect. V.4] |
| Kurto spectra | no evidence in BOSS DR12 or DESI DR1 | BOSS, DESI | arXiv:2604.06021 | [src] |

Reading: the auto-correlation excess is real as a number and is reproduced in
DESI, but every test that removes the dependence on the mock noise model
(better mocks, cross-patch statistics, compressed spectra) returns a null.
The current position is "no evidence for parity violation", not "detection".

### 1.4 History of the bispectrum numbers
<!-- key: history-of-the-bispectrum-numbers -->

- 2014: first BOSS (DR11 CMASS) measurement, f^0.43 σ8 = 0.582 ± 0.084 at
  z_eff = 0.57 [src: abstract] (arXiv:1407.5668); combined with the 2PCF it gave
  f = 0.63 ± 0.16 and σ8 = 0.710 ± 0.086 separately [src: abstract] (Gil-Marín et al.
  2014, arXiv:1408.0027).
- 2016: BOSS DR12, fσ8 = 0.427 ± 0.056 (LOWZ) and 0.426 ± 0.029 (CMASS) from
  P + B0 with post-reconstruction BAO [src: abstract]; the γ test with Planck 2015 gave
  γ = 0.733 +0.068/−0.069, about 2.7σ from GR [src: abstract] (arXiv:1606.00439). This
  γ value is superseded and should not be quoted as a current anomaly.
- 2017: 4.1σ detection of BAO in the BOSS CMASS bispectrum [src: abstract] (Pearson &
  Samushia 2017, arXiv:1712.04970).
- 2018–2019: compression raises the triangle count; a compressed fit quotes
  σ8(z_CMASS) = 0.51 ± 0.03 and f = 0.67 ± 0.06 [src: Sect. 5] (arXiv:1806.02853).
- 2021–2023: EFT full-shape P + B. The bispectrum monopole shrinks the σ8 error by 13%
  [src: abstract] (arXiv:2112.04515); one-loop B reduces errors on σ8, h, Ω_m by about
  30%, 18%, 13% [src: abstract] (arXiv:2206.08327); the ℓ > 0 bispectrum multipoles add
  5–10% [src: abstract] (arXiv:2302.04414).
- 2025–2026: DESI DR1. The collaboration's ShapeFit P + B (arXiv:2503.09714,
  arXiv:2603.19356, arXiv:2606.23936) and two external pipelines
  (arXiv:2507.13433, arXiv:2610.01836).

## 2. Cosmic voids
<!-- key: cosmic-voids -->

### 2.1 Void–galaxy cross-correlation, AP and RSD
<!-- key: void-galaxy-cross-correlation-ap-and-rsd -->

| Quantity | Value | Data, z | Method | Citation | Flag |
|---|---|---|---|---|---|
| Ω_m (AP on stacked voids) | 0.38 +0.18/−0.15 | BOSS DR12 CMASS, 0.43–0.7 | Stacked ellipticity against mocks, flat ΛCDM | arXiv:1602.06306 | [src: abstract] |
| D_A H/c (D_A taken as the proper distance; see physics §2.3) | 0.4367 ± 0.0045 | BOSS CMASS, z = 0.57 | Reconstruction + void–galaxy CCF | arXiv:1904.01030 | [src: abstract] |
| fσ8 from voids alone | 0.501 ± 0.051 | same | same | arXiv:1904.01030 | [src: abstract] |
| fσ8, voids + BAO + galaxy RSD | 0.453 ± 0.022 | same | consensus | arXiv:1904.01030 | [src: abstract] |
| f/b; D_A H/c (comoving D_A) | 0.540 ± 0.091; 0.588 ± 0.004 | BOSS DR12, z = 0.51 | Deprojection, calibration-free | arXiv:2007.07895 | [src: abstract] |
| Ω_m | 0.312 ± 0.020 | same | flat ΛCDM | arXiv:2007.07895 | [src: abstract] |
| f/b; Ω_m, mock-calibrated | 0.347 ± 0.023; 0.310 ± 0.017 | same | calibrated on survey mocks; "less robust" per the authors | arXiv:2007.07895 | [src: abstract] |
| β | 0.58 +0.33/−0.28 (LRG, z = 0.703); 0.15 +0.13/−0.12 (QSO, z = 1.53) | eBOSS DR14 | void–galaxy multipoles | arXiv:1909.04394 | [src: abstract] |
| β | 0.415 ± 0.087 (LRG+CMASS, z = 0.74); 0.665 ± 0.125 (ELG, z = 0.85); 0.313 ± 0.134 (QSO, z = 1.48) | eBOSS DR16 | stat + sys | arXiv:2007.09013 | [src: abstract] |
| fσ8 | 0.50 ± 0.11; 0.52 ± 0.10; 0.30 ± 0.13 | same | β × consensus linear bias from eBOSS companion papers | arXiv:2007.09013 | [src: abstract] |
| fσ8; D_M/D_H | 0.356 ± 0.079; 0.868 ± 0.017 | eBOSS DR16 LRG, z_eff = 0.69 | Reconstruction + watershed | arXiv:2008.06060 | [src: abstract] |
| fσ8, D_M/r_d, D_H/r_d with galaxy BAO + FS | 0.447 ± 0.039, 17.48 ± 0.23, 20.10 ± 0.34 | same | errors smaller by 13%, 23%, 28% than galaxy clustering alone | arXiv:2008.06060 | [src: abstract] |
| Ω_m | 0.337 +0.026/−0.029 | SDSS MGS + BOSS + eBOSS, 0.07 < z < 1.0 | voids only, flat ΛCDM | arXiv:2205.06258 | [src: abstract] |
| Ω_m | 0.356 ± 0.024 | same | void–galaxy + galaxy–galaxy, ΛCDM | Woodfinden et al. 2023, arXiv:2303.06143 | [src: abstract] |
| Ω_m, w | 0.391 +0.028/−0.021, −1.50 +0.43/−0.28 | same | wCDM | arXiv:2303.06143 | [src: abstract] |

### 2.2 Void size function
<!-- key: void-size-function -->

| Quantity | Value | Data | Model | Citation | Flag |
|---|---|---|---|---|---|
| Ω_m, σ8 | 0.29 ± 0.06, 0.79 +0.09/−0.08 | BOSS DR12 | ΛCDM, extended Vdn with two nuisance parameters calibrated on mocks | arXiv:2212.03873 | [src: abstract] |
| w | −1.1 ± 0.2 | same | wCDM | arXiv:2212.03873 | [src: abstract] |
| w, Ω_m, σ8 | −1.263 +0.329/−0.396, 0.293 +0.060/−0.053, 0.897 +0.159/−0.192 | BOSS DR16, 0.2 < z < 0.8 | excursion set with δ_v and B free | arXiv:2501.07817 | [src: abstract] |
| Σm_ν | < 0.43 eV (galaxy P alone), < 0.35 eV (P + VSF + void–galaxy P), 95% | BOSS CMASS NGC | implicit likelihood, k_max = 0.15 h Mpc⁻¹, Planck-inspired ΛCDM prior | arXiv:2307.07555 | [src: abstract] |

### 2.3 Void lensing
<!-- key: void-lensing -->

| Quantity | Value | Data | Citation | Flag |
|---|---|---|---|---|
| Void shear profile | 6.2σ detection; large versus small void profiles differ at 2.3σ; galaxy bias 2.45 ± 0.36 | UNIONS shear × BOSS LOWZ, CMASS voids | arXiv:2507.13450 | [src: abstract] |
| CMB lensing amplitude A_κ | 1.016 ± 0.054 (14σ); void-in-void 0.944 ± 0.064, void-in-cloud 0.975 ± 0.060 (17σ) | DESI Legacy DR9 LRG voids × Planck 2018 lensing | arXiv:2412.02761 | [src: abstract] |

### 2.4 Lyα tomography voids
<!-- key: lyalpha-tomography-voids -->

| Quantity | Value | Data | Citation | Flag |
|---|---|---|---|---|
| Void–forest RSD detection | 8σ | eBOSS Stripe 82, median z = 2.49 | arXiv:2203.11045 | [src: abstract] |
| β of the Lyα forest around voids | 1.21 ± 0.18 | same, linear RSD model with tomographic effect | arXiv:2203.11045 | [src: abstract] |
| Galaxy underdensity in tomography voids | 5.95σ against random cells, 432 coeval galaxies | CLAMATO, z ≈ 2.3 | arXiv:1710.02612 | [src: abstract] |

This is the one place where the void–forest β is quoted; `cosmo-lyman-alpha`
points here. Its map figures, 13 h⁻¹Mpc and 220 deg² (arXiv:2004.01448, abstract), match the sources read here.

### 2.5 History and what is superseded
<!-- key: history-and-what-is-superseded -->

- The 2016 ellipticity test (Ω_m = 0.38 +0.18/−0.15; Mao et al. 2016, arXiv:1602.06306, abstract) is superseded by the
  void–galaxy cross-correlation method, which fits the full ξ_vg(s, μ).
- The 2019 BOSS CMASS result (arXiv:1904.01030) and the eBOSS DR16 LRG result
  (arXiv:2008.06060) are superseded as headline numbers by the six-bin SDSS
  analysis (arXiv:2205.06258, arXiv:2303.06143).
- The eBOSS DR14 β values (arXiv:1909.04394) are superseded by DR16
  (arXiv:2007.09013).
- No void–galaxy cosmology from DESI was found; SDSS remains the reference.

## 3. Alternative clustering statistics on survey data
<!-- key: alternative-clustering-statistics-on-survey-data -->

All rows: BOSS DR12 CMASS, flat ΛCDM, emulator on AbacusSummit with an HOD
galaxy model unless stated. None of the abstracts reports blinding of the data
analysis.

| Statistic | Quantity | Value | Scales, z | Citation | Flag |
|---|---|---|---|---|---|
| DSC + 2PCF | ω_cdm, σ8, n_s | 0.1201 ± 0.0022, 0.792 ± 0.034, 0.970 ± 0.018 | down to 1 h⁻¹Mpc, z ≈ 0.525 | arXiv:2309.16541 | [src: abstract] |
| DSC + 2PCF | fσ8 | 0.462 ± 0.020 | same | arXiv:2309.16541 | [src: abstract] |
| MFs + 2PCF | ω_cdm, σ8, n_s | 0.1172 +0.0020/−0.0023, 0.783 ± 0.026, 0.966 +0.019/−0.015 | 0.45 < z < 0.58 | arXiv:2501.01698 | [src: abstract] |
| MFs + 2PCF | fσ8 | 0.453 ± 0.016 | same | arXiv:2501.01698 | [src: abstract] |
| MFs, Hermite amplitude | Ω_c h² n_s | 0.110 ± 0.006 (CMASS), 0.111 ± 0.008 (LOWZ) | large smoothing scales | arXiv:2110.06109 | [src: abstract] |
| WST + 2PCF | precision on ω_c, σ8, n_s | 0.9%, 2.3%, 1% | 0.46 < z < 0.57 | arXiv:2310.16116 | [src: abstract] |
| WST + 2PCF | precision on h, fσ8 | 0.7%, 2.5% | same | arXiv:2310.16116 | [src: abstract] |
| WST (first application) | errors relative to P_0, P_2 | tighter by factors 3–5, or 3–8 with a BBN prior; "investigative" | 0.46 < z < 0.60 | arXiv:2204.13717 | [src: abstract] |
| WST with SimBIG | all ΛCDM parameters | robust to the forward model except σ8 at k_max = 0.5 h Mpc⁻¹; scales below k ≈ 0.3 removed; authors "still raise concerns" | k_max = 0.5 h Mpc⁻¹ | arXiv:2310.15250 | [src: abstract] |

Claimed gains over the two-point function, from the same emulator pipelines:

| Statistic | Gain when added to the 2PCF | Basis | Citation | Flag |
|---|---|---|---|---|
| DSC | factors 2.9, 1.9, 2.1 on ω_cdm, σ8, n_s | emulator forecast | arXiv:2309.16539 | [src: abstract] |
| MFs | factors 2.0, 1.9, 1.6 on ω_cdm, σ8, n_s; 1.9 on fσ8 | BOSS CMASS data | arXiv:2501.01698 | [src: abstract] |
| WST | factors 2.5–6 over the 2PCF | BOSS CMASS data | arXiv:2310.16116 | [src: abstract] |
| kNN | more than a factor 2 for matter at 10–40 h⁻¹Mpc | simulations, Fisher | arXiv:2007.13342 | [src: abstract] |
| Marked P(k) | more than a factor 2 on all parameters; 4.3σ on the minimum Σm_ν in 1 (h⁻¹Gpc)³ with P + marked P | 22 000 Quijote simulations, matter field, Fisher | arXiv:2001.11024 | [src: abstract] |
| Marked P(k), realistic tracers | does not surpass P + B at k ≲ 0.25 h Mpc⁻¹ for BOSS-like number density | Fisher with EFT model | Marinucci et al. 2024, arXiv:2411.14377 | [src: abstract] |

For comparison, the perturbative P + B results on BOSS in §1.1 give σ8 = 0.722
+0.032/−0.036 (arXiv:2112.04515, abstract) and 0.794 ± 0.037 (arXiv:2206.08327, abstract). The emulator-based values, σ8 = 0.783 ± 0.026 (arXiv:2501.01698, abstract) and 0.792 ± 0.034 (arXiv:2309.16541, abstract), are tighter because they use scales down to 1 h⁻¹Mpc (arXiv:2309.16541, Sect. 4.4.3) and assume
an HOD.

Galaxy–halo connection result: DESI DR2 LRG multiplets are more clustered than
AbacusSummit HOD mocks that reproduce the two-point function; adding
environment-dependent secondary bias restores agreement (arXiv:2511.15354).
DSC on CMASS likewise finds "signatures of environment-based assembly bias"
(arXiv:2309.16541).

## 4. Higher-order weak lensing
<!-- key: higher-order-weak-lensing -->

All rows are fits to survey data. S8 = σ8 (Ω_m/0.3)^0.5 throughout. <!-- num: not a value -->

| Data | Statistic | S8 | Other | Model | Citation | Flag |
|---|---|---|---|---|---|---|
| KiDS-Legacy | COSEBIs + ⟨M_ap³⟩ | 0.806 +0.025/−0.023 | Ω_m = 0.297 +0.056/−0.040; FoM(Ω_m, S8) more than doubled; within 1σ of Planck | ΛCDM | arXiv:2606.12389 | [src: abstract] |
| DES Y3 | ξ± + ⟨M_ap³⟩ | 0.780 ± 0.015 | Ω_m = 0.266 +0.039/−0.040; FoM +111%; 2.3σ from Planck | ΛCDM | arXiv:2508.14018 | [src: abstract] |
| DES Y3 | ξ± + ⟨M_ap³⟩ | 0.749 +0.027/−0.026 | w0 = −1.39 ± 0.31 | wCDM | arXiv:2508.14018 | [src: abstract] |
| HSC Y3 | ξ± + ⟨M_ap³⟩ | 0.736 ± 0.020 | FoM +80%; 3.2σ from Planck 2018 in the S8–Ω_m plane | ΛCDM | arXiv:2508.14019 | [src: abstract] |
| DES Y3 | SBI: moments + wavelet phase harmonics + scattering transform | 0.794 ± 0.017 | FoM(S8, Ω_m) +70% over second moments; ≤ 2.2σ from Planck | ΛCDM | arXiv:2405.10881 | [src: abstract] |
| DES Y3 | same | 0.817 ± 0.021 | FoM +90% | wCDM | arXiv:2405.10881 | [src: abstract] |
| DES Y3 | SBI: power spectrum + CNN map-level | 0.804 +0.025/−0.017 | Ω_m = 0.283 +0.020/−0.027; w < −0.80 (68%), prior −1 < w < −1/3 | wCDM | arXiv:2403.02314 | [src: abstract] |
| DES Y3 | SBI: Betti numbers + second moments | 0.821 ± 0.018 | Ω_m = 0.304 ± 0.037; 70% tighter than two-point in the plane | wCDM | arXiv:2506.13439 | [src: abstract] |
| DES Y3 | SBI: hybrid statistics (seven summaries) | 0.808 ± 0.017 | Ω_m = 0.325 ± 0.024; w < −0.766 (68%); FoM(Ω_m, S8, w) +60% over previous best, almost ×3 over two-point | wCDM | arXiv:2606.11309 | [src: abstract] |
| DES Y3 | Peaks + C_ℓ, Gaussian-process emulator | 0.797 +0.015/−0.013 | about 38% tighter than C_ℓ alone; 1.5σ below Planck 2018 | ΛCDM | Zürcher et al. 2021, arXiv:2110.10135 | [src: abstract] |
| HSC Y1 | Peaks + minima + power spectrum | 0.810 +0.022/−0.026 | 35% tighter than the power spectrum alone | ΛCDM | Marques et al. 2023, arXiv:2308.10866 | [src: abstract] |
| HSC Y1 | Convergence PDF + power spectrum | 0.798 +0.029/−0.042 | PDF alone 0.860 +0.066/−0.109; PDF improves the power-spectrum constraint by about 10% | ΛCDM | Thiele et al. 2023, arXiv:2304.05928 | [src: abstract] |
| KiDS-1000 | Density split statistics (shear around foreground-density quantiles) | 0.74 +0.03/−0.02 | Ω_m = 0.28 ± 0.02; b = 1.32 +0.12/−0.10 | ΛCDM | Burger et al. 2022, arXiv:2208.02171 | [src: abstract] |
| HSC Y1 | SBI: power spectrum + PDF + peaks + minima + MFs | 0.804 +0.041/−0.040 | Ω_m = 0.344 +0.083/−0.090; power spectrum alone 0.766 +0.054/−0.056 | ΛCDM | arXiv:2409.01301 | [src: abstract] |

Reading the table.

- Within DES Y3, the higher-order analyses of the table give S8 from 0.780 (arXiv:2508.14018, ΛCDM) to 0.821 (arXiv:2506.13439, wCDM), all read in the abstracts, apart from the 2+3-point wCDM value of 0.749 (arXiv:2508.14018, abstract).
  They are not independent: same shapes, same redshifts, and at least three
  of them state that they use the Gower Street simulations.
- The ΛCDM and wCDM rows must not be mixed: the SBI papers mostly quote wCDM.
- The HSC Y3 2+3-point value (0.736, 3.2σ; arXiv:2508.14019, abstract) is
  the outlier. The HSC Y3 two-point S8 moves from 0.769 to 0.804 when the
  source redshifts are recalibrated with DESI clustering redshifts
  (Choppin de Janvry et al. 2025, arXiv:2511.18134, abstract).
- The 2+3-point analysis predates that recalibration (August 2025 against
  November 2025), so its tension figure should be read as provisional; this
  ordering is inferred from the two arXiv dates [der].
- Checked on 2026-10-13: the paper uses the HSC Y3 redshift distributions
  that combine three photo-z codes with CAMIRA-LRG clustering redshifts, with
  Gaussian priors of about 2% on the shifts of bins 1 and 2 and a flat prior
  between −1 and 1 on those of bins 3 and 4, "to allow the self-calibration
  of the residual photo-z bias" [src: Sect. II.1.2, IV.2.2 of
  arXiv:2508.14019]. It does not use DESI clustering redshifts; the high-z
  bins are self-calibrated, as in the HSC Y3 two-point analyses it cites.
- The KiDS-Legacy 2+3-point S8 (0.806 +0.025/−0.023) is not tighter in S8
  than the KiDS-Legacy two-point value quoted in `cosmo-weak-lensing`
  (0.815 +0.016/−0.021, arXiv:2503.19441 [src: abstract]); the gain is in Ω_m and in the figure of merit,
  and the two analyses differ in IA and baryon modelling (arXiv:2606.12389, abstract).

**Forecast** for Euclid (HOWLS, arXiv:2301.12890): on common non-tomographic
mocks without systematics, each of ten higher-order statistics beats the
two-point functions by about a factor two on (Ω_m, σ8), and their
combination by 4.5 [src: abstract]. The first KiDS-1000 2+3-point analysis is Burger
et al. 2023 (arXiv:2309.08602), restricted to equal aperture radii; its
values were not read.

History. CFHTLenS peaks and 2+3-point (arXiv:1412.0757, arXiv:1404.5469)
and DES SV peaks (arXiv:1603.05040) came first. KiDS-450 peaks (arXiv:1709.07678) and the KiDS-450 CNN
(arXiv:1906.03156) were the first data applications; DES Y3 moments
(arXiv:2110.10141) the first Stage-III collaboration result; the 2024–2026
DES Y3 SBI series superseded each other in constraining power, the hybrid
analysis (arXiv:2606.11309) being the current reference.

## 5. Field-level inference
<!-- key: field-level-inference -->

### 5.1 Information content, simulations only
<!-- key: information-content-simulations-only -->

| Setup | Result | Citation | Flag |
|---|---|---|---|
| Halos, rest frame, 8 (h⁻¹Gpc)³; LEFTfield field level against SBI P + B with the same forward model and modes | σ8 error 20.0% → 5.7% at k_max = 0.10 h Mpc⁻¹ (factor 3.5); 17.0% → 3.3% at 0.12 (factor 5.2) | arXiv:2403.03220 | [src: abstract] |
| Halos in real space, one amplitude A; Eulerian PT P + B + T | Trispectrum reduces the error on A by only 20–30%; joint analysis agrees with field-level results in the same setup; disagrees with the likelihood-free P + B baselines | arXiv:2507.05378 | [src: abstract] |
| Mock data from a perturbative model with Gaussian noise; A, ω_cdm, H0; real and redshift space | Field-level errors comparable to P + B with the same model; a Gaussian likelihood applied to non-Gaussian noise gives significant biases | arXiv:2509.09673 | [src] |
| Redshift-space snapshots resembling DESI LRG, LEFTfield; P + B by Fisher forecast | Primordial amplitude twice as precise (ΛCDM); up to a factor 3 in amplitude and 2 in beyond-ΛCDM parameters | Stadler 2026, arXiv:2609.16719 | [src] |
| Toy model: linear field + local quadratic coupling λ | P + B, composite-operator correlators and field level equivalent at λ = 0; loss of the summaries grows with λ and at lower noise; correlators up to the 6-point function still fall short | Nikolac, Schmidt & Tucci 2026, arXiv:2606.18227 | [src] |
| Quijote halos, k_max ≈ 0.1 h Mpc⁻¹, BORG | σ(f_NL^loc) better by a factor of about 1.3 than P + B | arXiv:2603.20855 | [src: abstract] |

### 5.2 Reconstructions from survey data
<!-- key: reconstructions-from-survey-data -->

| Data | Result | Citation | Flag |
|---|---|---|---|
| 2M++ | Non-linear density and velocity fields of the nearby Universe; Coma mass consistent with lensing and X-ray; first vorticity reconstruction | arXiv:1806.11117 | [src] |
| 2M++ (Manticore-Local) | Counterparts for 14 clusters within 1° at 2–4σ; no evidence for a large local underdensity; highest Bayesian evidence across five peculiar-velocity data sets | arXiv:2505.10682 | [src: Sect. 3.4.2 for the 14 clusters] |
| BOSS | Cross-correlation with Planck 2018 lensing recovered; no bias in the a posteriori initial power spectrum at k ≈ 10⁻³–10⁻² h Mpc⁻¹; maps of residual systematics | arXiv:1909.06396 | [src: abstract] |
| Quaia | (10 h⁻¹Gpc)³, 39.1 h⁻¹Mpc; cross-correlation with Planck CMB lensing at about 4σ | arXiv:2602.02363 | [src: abstract] |

None of these quotes a cosmological parameter.

### 5.3 Neural field-level results on survey data
<!-- key: neural-field-level-results-on-survey-data -->

| Data | Result | Citation | Flag |
|---|---|---|---|
| DESI DR1 LRG, LiFT reconstruction | Errors on α_iso smaller by 13%, 24%, 30% and on α_AP by 5%, 22%, 30% in LRG1, LRG2, LRG3 than the DESI DR1 standard reconstruction; figure of merit × 1.2, 1.7, 2.0; central values consistent with DR1 and DR2 | arXiv:2609.14862 | [src: abstract] |
| BOSS CMASS subsample, SimBIG CNN | Ω_m = 0.267 +0.033/−0.029, σ8 = 0.762 +0.036/−0.035, H0 = 64.5 ± 3.8; σ8 2.65 times tighter than P_ℓ | arXiv:2310.15256 | [src: abstract] |

### 5.4 Gaussian field-level likelihood
<!-- key: gaussian-field-level-likelihood-flip -->

| Quantity | Value | Basis | Citation | Flag |
|---|---|---|---|---|
| σ(fσ8) | +0.047/−0.048, a 10% error; up to 50% smaller than supernovae alone | **forecast**: simulated ZTF 6-year SNe Ia velocities + DESI DR3 BGS density | arXiv:2609.34508 | [src: abstract] |
| Fisher forecast accuracy | 30% closer to the full-likelihood error than a volume Fisher forecast | simulation | arXiv:2501.16852 | [src: abstract] |
| fσ8 with wide-angle and zero-point terms in the model | 0.405 (+0.076/−0.071) stat ± 0.009 sys at z_eff = 0.073; likelihood interpolated for a ~30× faster MCMC | SDSS PV catalogue (method paper's own application) | arXiv:2209.04166 | [src: abstract] |

The data result of this method, fσ8 from DESI DR1 peculiar velocities, is in
`cosmo-peculiar-velocities`. The 10% forecast above (arXiv:2609.34508, abstract) matches the figure that
skill quotes.

## 6. Simulation-based inference on galaxy clustering (SimBIG, BOSS CMASS subsample)
<!-- key: simulation-based-inference-on-galaxy-clustering -->

All rows: flat ΛCDM, k_max = 0.5 h Mpc⁻¹ unless stated (arXiv:2211.00723, abstract), about 10% of the BOSS
volume (arXiv:2310.15243, abstract).

| Statistic | Ω_m | σ8 | Other | Gain over P_ℓ | Citation | Flag |
|---|---|---|---|---|---|---|
| Bispectrum monopole | 0.293 ± 0.027 | 0.783 +0.040/−0.038 | S8 = 0.774 +0.056/−0.053; H0 = 67.6 +2.2/−1.8 with BBN | 1.2× (Ω_m), 2.4× (σ8); σ8 gain equals a sample about 4 times larger | arXiv:2310.15243 | [src: abstract] |
| CNN field-level summary | 0.267 +0.033/−0.029 | 0.762 +0.036/−0.035 | H0 = 64.5 ± 3.8 | 2.65× (σ8) | arXiv:2310.15256 | [src: abstract] |
| Bispectrum + CNN | — | — | — | 1.6, 1.5, 1.7, 1.2, 2.3× on Ω_b, h, n_s, Ω_m, σ8 | arXiv:2310.15246 | [src: abstract] |
| Marked power spectrum | 0.273 +0.040/−0.030 | 0.777 +0.077/−0.071 | — | up to 1.2× on σ8 against a perturbative P analysis; none on other parameters | arXiv:2404.04228 | [src: abstract] |
| Wavelet scattering transform | — | not robust at k_max = 0.5 | posterior depends on flow architecture | "seemingly improved"; authors raise concerns | arXiv:2310.15250 | [src: abstract] |
| Wavelet scattering transform, values (CMASS SGC) | 0.28 ± 0.04 (full); 0.25 ± 0.03 (scales k ≳ 0.3 removed) | 0.84 ± 0.03 (full); 0.75 ± 0.05 (cut) | h = 0.73 ± 0.06, n_s = 1.05 ± 0.06 (full) | SimBIG P_ℓ on the same data: σ8 = 0.81 ± 0.07 | arXiv:2310.15250 | [src: Table 2] |

Reading. The gains are quoted against the SimBIG power-spectrum analysis of
the same subsample (Hahn et al. 2022, arXiv:2211.00723: σ8 27% more precise
than standard analyses, P_ℓ to k_max = 0.5 h Mpc⁻¹ [src: abstract]), whose mock
challenge found it "unbiased, but conservative" (arXiv:2211.00660); a gain over a conservative baseline is an upper estimate
of the gain over an optimal one. On data, the marked power spectrum gave 1.2×
on σ8 (arXiv:2404.04228, abstract) where the matter-field Fisher forecast promised more than 2× on all
parameters (arXiv:2001.11024, abstract; §3).
