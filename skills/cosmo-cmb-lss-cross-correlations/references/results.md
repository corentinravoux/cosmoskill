# Results — CMB × LSS cross-correlations

Scope: current headline measurements from CMB lensing × galaxies and quasars, kSZ, tSZ × LSS, ISW, CIB and the other secondaries, then the history of the key numbers.
Snapshot: 2026-10-07

Flags: `[src]` read this session in the cited paper (its abstract unless a section is named); `[sec]` from a named secondary source; `[der]` derived here, derivation stated. Every constraint assumes flat ΛCDM unless the row says otherwise. Years next to author names are arXiv submission years.

## 1. CMB lensing × galaxies and quasars
<!-- key: cmb-lensing-x-galaxies-and-quasars -->

### 1.1 Amplitude of structure, by tracer
<!-- key: amplitude-of-structure-by-tracer -->

The quoted amplitude is not the same combination everywhere: read the "Quantity" column before comparing two rows. "+ BAO" means that a BAO-based prior was added to break the Ω_m–σ_8 degeneracy. "κ" is the CMB lensing convergence map.

| Tracer (z range) | CMB lensing | Quantity | Value | Citation | Flag |
|---|---|---|---|---|---|
| unWISE blue + green + red (median z ≈ 0.6, 1.1, 1.5) | Planck | S_8 = σ_8(Ω_m/0.3)^0.5 | 0.784 ± 0.015; 2.4σ below Planck primary | Krolewski 2021, arXiv:2105.03421 | [src] |
| unWISE blue + green (0.2 ≲ z ≲ 1.8) | ACT DR6 | S_8 | 0.813 ± 0.021 | Farren 2023, arXiv:2309.05659 | [src] |
| same | ACT DR6 + Planck | S_8 | 0.810 ± 0.015 | arXiv:2309.05659 | [src] |
| same, + BAO | ACT DR6 + Planck | σ_8 | 0.813 ± 0.015 | arXiv:2309.05659 | [src] |
| unWISE cross + auto + lensing auto ("3×2pt") | ACT DR6 + Planck PR4 | S_8^3x2pt = σ_8(Ω_m/0.3)^0.4 | 0.815 ± 0.012 | Farren 2024, arXiv:2409.02109 | [src] |
| same | same | S_8 (exponent 0.5) | 0.816 ± 0.015 | arXiv:2409.02109 | [src] |
| same, + BAO | same | σ_8 | 0.815 ± 0.012 | arXiv:2409.02109 | [src] |
| DESI-targeting LRGs, 4 photo-z bins (0.4 ≤ z ≤ 1), SN + BAO background priors | Planck | S_8 | 0.73 ± 0.03 | White 2021, arXiv:2111.09898 | [src] |
| DESI LRGs, 4 bins (0.4 ≲ z ≲ 1), HEFT | Planck PR4 | S_8 | 0.765 ± 0.023 | Sailer 2024, arXiv:2407.04607 | [src] |
| same | ACT DR6 | S_8 | 0.790 +0.024/−0.027 | arXiv:2407.04607 | [src] |
| same | ACT DR6 + Planck PR4 | S_8 | 0.775 +0.019/−0.022 | arXiv:2407.04607 | [src] |
| same, + BAO | ACT DR6 + Planck PR4 | σ_8 | 0.772 +0.020/−0.023 | arXiv:2407.04607 | [src] |
| DESI LRGs, 4 bins, HEFT to k_max = 0.6 h/Mpc | ACT DR6 | S_8^× = σ_8(Ω_m/0.3)^0.4 | 0.792 +0.024/−0.028 (1.2σ from Planck PR4 primary) | Kim 2024, arXiv:2407.04606 | [src] |
| same | ACT DR6 + Planck PR4 | S_8^× | 0.776 +0.019/−0.021 (2.1σ) | arXiv:2407.04606 | [src] |
| DESI Legacy Imaging galaxies, 3 bins (0.3 < z < 0.8), linear scales | ACT DR6 | S_8 | 0.772 ± 0.040 | Qu 2024, arXiv:2410.10808 | [src] |
| same | ACT DR6 + Planck PR4 | S_8 | 0.765 ± 0.032 | arXiv:2410.10808 | [src] |
| same without the lowest-z bin | ACT DR6 + Planck PR4 | S_8 | 0.785 ± 0.033 (1.8σ below Planck primary) | arXiv:2410.10808 | [src] |
| DESI BGS imaging sample (z ≲ 0.4), HEFT, + DESI BAO | Planck + ACT | σ_8 | 0.876 +0.051/−0.067 | Sailer 2025, arXiv:2503.24385 | [src] |
| BGS + LRG jointly, + BAO | Planck + ACT | σ_8 | 0.791 ± 0.021 | arXiv:2503.24385 | [src] |
| BGS × LRG magnification signal, linear bias, + BAO | none (galaxy × galaxy) | σ_8 | 0.720 ± 0.047 (stat) ± 0.050 (sys) | arXiv:2503.24385 | [src] |
| DESI Legacy LRG angular power spectrum + bispectrum + κ cross | Planck | S_8; σ_8; Ω_m | 0.769 ± 0.020; 0.761 ± 0.020; 0.307 ± 0.015 (~2.5σ from Planck) | Verdiani 2025, arXiv:2510.17796 | [src] |
| 2MASS photo-z and WISE-based samples (z ≲ 0.3), HEFT, DESI BAO prior on Ω_m | Planck | S_8 | 0.79 ± 0.06 | Rubiola 2025, arXiv:2510.09563 | [src] |
| same, no Ω_m prior | Planck | Ω_m | 0.245 ± 0.024 (2.8σ below Planck; driven by the auto-spectrum shape) | arXiv:2510.09563 | [src] |
| DES Y3 MagLim positions + shear, cross-correlations with κ only, linear bias | SPT-SZ + Planck | S_8; Ω_m | 0.736 +0.032/−0.028; 0.272 +0.032/−0.052 | Chang 2022, arXiv:2203.12440 | [src] |
| DES Y3 shear × κ only | SPT-SZ + Planck | S_8 | 0.740 +0.034/−0.029 | arXiv:2203.12440 | [src] |
| DES Y3 3×2pt + its cross-correlations with κ | SPT-SZ + Planck | S_8; Ω_m | 0.773 ± 0.016; 0.344 ± 0.030 | Abbott 2022, arXiv:2206.10824 | [src] |
| DES Y3 6×2pt (adds the lensing auto-spectrum) | SPT-SZ + Planck | S_8; Ω_m | 0.792 ± 0.012; 0.306 +0.018/−0.021 | arXiv:2206.10824 | [src] |
| DES Y3 MagLim, 6 bins (0.20 < z < 1.05) | ACT DR4 | S_8 | 0.75 +0.04/−0.05 | Marques 2023, arXiv:2306.17268 | [src] |
| DES Y3 cosmic shear | ACT DR4 + Planck | S_8 | 0.782 ± 0.059 | Shaikh 2023, arXiv:2309.04412 | [src] |
| DES Y3 cosmic shear, ~1300 deg² | SPT-3G D1, polarisation-only κ | S_8 | 0.833 +0.047/−0.061 | Ouellette 2026, arXiv:2606.26223 | [src] |
| DES Y3 MagLim 6×2pt, shear down to 2.5′, baryon principal components with a gas-fraction prior | Planck PR4 | S_8 | 0.8073 ± 0.0094 | Xu 2025, arXiv:2510.25596 | [src] |
| Quaia, 2 bins (z = 1.0, 2.1), + BAO | Planck (PR4 according to arXiv:2507.08798) | σ_8; Ω_m | 0.766 ± 0.034; 0.343 +0.017/−0.019 | Alonso 2023, arXiv:2306.17748 | [src] |
| Quaia, 2 bins, + BOSS BAO | ACT DR6 + Planck PR4 | σ_8 | 0.802 +0.045/−0.057 | Embil Villagra 2025, arXiv:2507.08798 | [src] |
| Quaia cross + ACT DR6 lensing auto-spectrum | ACT DR6 + Planck PR4 | σ_8 | 0.804 ± 0.013 | arXiv:2507.08798 | [src] |
| DESI DR1 spectroscopic quasars, 3 bins (z_eff = 1.44, 2.27, 2.75), + DESI DR1 BAO Ω_m prior | Planck PR4 | σ_8; S_8 | 0.929 +0.059/−0.074; 0.922 +0.059/−0.073 (1.5σ above Planck PR4 primary) | de Belsunce 2025, arXiv:2506.22416 | [src] |
| CatNorth quasar candidates, z < 1.5 | Planck PR4 | S_8 | 0.844 +0.058/−0.056 | Qin 2026, arXiv:2603.09457 | [src] |
| CatNorth, z > 1.5 | Planck PR4 | S_8 | 0.724 +0.058/−0.054 (authors: incompleteness and/or foregrounds) | arXiv:2603.09457 | [src] |
| DESI DR1 full shape + bispectrum + photometric galaxies + κ cross, + DESI BAO, CMB priors on n_s and ω_b; EFT | not named in the abstract | σ_8; S_8; H_0; Ω_m | 0.838 ± 0.017; 0.834 ± 0.018; 69.08 ± 0.37; 0.2974 ± 0.0050 | Ivanov 2026, arXiv:2601.16165 | [src] |

Detection significances. unWISE × Planck: S/N ≈ 80 for the three samples combined (arXiv:2105.03421) [src]. DESI LRG × ACT DR6: 38σ, and 50σ with Planck PR4 added (arXiv:2407.04606) [src]. DES Y3 × SPT-SZ + Planck: 23.9 with linear-bias scale cuts, 25.7 with non-linear bias (arXiv:2203.12440) [src]. DESI DR1 quasars × Planck PR4: 21.7 for the cross-spectrum and 27.2 for the quasar auto-spectrum (arXiv:2506.22416) [src]. DES Y3 shear × SPT-3G D1 polarisation-only lensing: ~14σ (arXiv:2606.26223) [src]. DES Y3 shear × ACT DR4: 7.1 (arXiv:2309.04412) [src]. DES Y3 MagLim × ACT DR4: 9.1σ, with a lensing map of ~436 deg² (arXiv:2306.17268) [src].

### 1.2 Growth at high redshift
<!-- key: growth-at-high-redshift -->

| Quantity | Value | Data | Citation | Flag |
|---|---|---|---|---|
| σ_8(z = 2.72) | 0.22 ± 0.06, ~1σ from the Planck ΛCDM prediction | Quaia, 3 bins centred at z = 0.69, 1.59, 2.72, × Planck κ | Piccirilli 2024, arXiv:2402.05761 | [src] |
| σ_8(z̃ = 5.1), the amplitude at z > 3 | 0.146 +0.021/−0.014 (a 12% constraint), 1.4σ from Planck | ACT DR6 lensing auto-spectrum + Quaia cross-correlations | arXiv:2507.08798 | [src] |
| integrated matter fluctuations above z = 2.4 | 3.3% constraint, consistent with the ΛCDM fit to the Planck primary CMB | ACT DR6 + Planck PR4 lensing auto + unWISE cross | arXiv:2409.02109 | [src] |

### 1.3 Other parameters extracted from the same spectra
<!-- key: other-parameters-extracted-from-the-same-spectra -->

| Quantity | Value | Data and model | Citation | Flag |
|---|---|---|---|---|
| H_0, sound-horizon free | 66.4 +3.2/−3.7 km/s/Mpc | ACT DR6 + Planck PR4 lensing, unWISE cross and auto | arXiv:2409.02109 | [src] |
| H_0, sound-horizon free | 64.3 +2.1/−2.4 | same + uncalibrated Pantheon+ supernovae | arXiv:2409.02109 | [src] |
| H_0, sound-horizon free | 69.1 +2.2/−2.6 | DESI DR1 quasars × Planck PR4 + ACT DR6 and Planck PR4 lensing auto | arXiv:2506.22416 | [src] |
| H_0 from the turnover scale alone | 62.7 ± 17.2; turnover detected at 2.3–3.1σ | Quaia × Planck lensing + supernovae (inverse ladder) | Alonso 2024, arXiv:2410.24134 | [src] |
| Σm_ν | < 0.12 eV (95%) | unWISE 3×2pt + SDSS BAO + primary CMB | arXiv:2409.02109 | [src] |
| Σm_ν | < 0.049 eV (95%, ΛCDM); < 0.077 eV (w0waCDM) | DESI DR1 full shape with κ cross + BAO + CMB + SNe | arXiv:2601.16165 | [src] |
| f_NL (local) | 39 +40/−38 from C_ℓ^κg alone; 24 +20/−21 with C_ℓ^gg and an ℓ_min cut | DESI Legacy DR9 LRG × Planck; not blinded | Bermejo-Climent 2024, arXiv:2412.10279 | [src] |
| f_NL (local), p = 1 | −20.5 +19.0/−18.1 (auto + cross); −13.8 +26.7/−25.0 (κ cross alone) | Quaia × CMB lensing, 2 bins | Fabbian 2025, arXiv:2504.20992 | [src] |
| f_NL (local), p = 1.6 | −28.7 +26.1/−24.6 (auto + cross); −15.6 +42.3/−34.8 (κ cross alone) | same | arXiv:2504.20992 | [src] |
| f_NL (local), p = 1.6 | 2 +28/−34; with optimal weights 19 +25/−31 | DESI DR1 quasars × Planck PR4, 3 bins, 0.8 < z < 3.5, f_sky ~ 20% | Chiarenza 2025, arXiv:2512.17865 | [src] |
| f_NL (local), p = 1.0 | 6 +20/−24 | same | arXiv:2512.17865 | [src] |
| E_G(z_eff = 0.555) | 0.31 +0.06/−0.05 (ACT); 0.34 ± 0.05 (ACT + Planck PR4); GR prediction 0.401 ± 0.005 | ACT DR6 lensing × BOSS CMASS | Wenzl 2024, arXiv:2405.12795 | [src] |
| E_G(z_eff = 0.316) | 0.49 +0.14/−0.11 (ACT); 0.43 +0.11/−0.09 (ACT + Planck PR4); GR prediction 0.452 ± 0.005 | ACT DR6 lensing × BOSS LOWZ | arXiv:2405.12795 | [src] |

The response parameter p sets the non-Gaussian bias through b_φ ∝ (b − p). An f_NL value quoted without its p cannot be compared with another: the same Quaia data give errors of ~19 for p = 1 and ~25 for p = 1.6 (arXiv:2504.20992) [src].

### 1.4 Lensing by voids
<!-- key: lensing-by-voids -->

| Quantity | Value | Data | Citation | Flag |
|---|---|---|---|---|
| A_κ (observed / mock template) | 1.016 ± 0.054; two independent ~17σ detections (void-in-void and void-in-cloud) | DESI Legacy DR9 LRG voids, 0.35 < z < 0.95, × Planck 2018 lensing; Buzzard templates recalibrated with DESI spectra | Sartori 2026, arXiv:2605.19763 | [src] |

The same paper describes earlier reports as a "lensing-is-low" discrepancy between observed void imprints and mocks, and attributes it to the mismatch in photometric-redshift errors and sparseness between data and mocks.

## 2. Kinematic Sunyaev–Zel'dovich effect
<!-- key: kinematic-sunyaev-zel-dovich-effect -->

The kSZ measurements come in three estimator families that Smith 2018 (arXiv:1810.13423) showed to be special cases of one ⟨ggT⟩ bispectrum, with two observables: the small-scale galaxy–electron spectrum P_ge and the large-scale galaxy–velocity spectrum P_gv. The tables are split accordingly: gas (P_ge side) and velocities (P_gv side). See `physics-and-methods.md` §3 for the estimators.

### 2.1 Detections, by estimator
<!-- key: detections-by-estimator -->

| Estimator | CMB data | Tracer | Significance and sample | Citation | Flag |
|---|---|---|---|---|---|
| Pairwise momentum | ACT | BOSS luminous galaxies | probability of a noise origin 0.002; first evidence | Hand 2012, arXiv:1203.4219 | [src] |
| Pairwise | ACT DR5 (+ DR4 component-separated) + Planck | SDSS DR15 LRGs, 343,647 galaxies, 3,700 deg² | 5.4σ | Calafut 2021, arXiv:2101.08374 | [src] |
| Pairwise | ACT DR6 + Planck co-adds, 19,000 deg² of ACT coverage | DESI DR1 LRGs, 913,286 galaxies | 9.3σ | Gong 2025, arXiv:2511.23417 | [src] |
| Pairwise | ACT DR6 | DESI DR1 BGS, 1.6 million galaxies with log M⋆/M⊙ > 10, z ~ 0.3 | 5σ in the best configuration (θ_ap = 3.3′, log M⋆ > 11) | Hadzhiyska 2025, arXiv:2510.14135 | [src] |
| Pairwise, with machine-learning velocities | ACT DR6 ILC and 150 GHz | DESI DR2 LRGs, 7 luminosity samples, epochs z = 0.55 and 0.8 | best SNR 14.2 (reconstructed pairwise velocity) and 15.1 (theory template) for the optical depth | Gong 2026, arXiv:2609.36355 | [src] |
| Velocity-weighted stacking | ACTPol 146 GHz, 660 deg² | BOSS CMASS, 25,537 galaxies | 3.3σ and 2.9σ for two velocity reconstructions | Schaan 2015, arXiv:1510.06442 | [src] |
| Velocity-weighted stacking | ACT DR5 + Planck | BOSS CMASS | 6.5σ (kSZ), 10σ (tSZ); LOWZ 2.9σ (kSZ), 13.9σ (tSZ) | Schaan 2020, arXiv:2009.05557 | [src] |
| Hybrid stacking (spectroscopic velocities interpolated to photometric positions) | ACT DR5, 1000 deg² overlap | DES Y3 photometric + BOSS DR12 | 4.8σ detection; null rejected at 5.1σ | Mallaby-Kay 2023, arXiv:2305.06792 | [src] |
| Stacking with photometric-redshift velocities | ACT | DESI Legacy imaging LRGs | 13σ | Hadzhiyska 2024, arXiv:2407.07152 | [src] |
| Stacking | ACT DR6, ≥ 4,000 deg² overlap | DESI Y1 spectroscopic LRGs, > 800,000 | S/N ≈ 10 | Ried Guachalla 2025, arXiv:2503.19870 | [src] |
| Stacking, real and harmonic space | ACT DR6 | DESI DR2 spectroscopic LRGs, 2.4 million | 18σ; S/N ≈ 5–10 in each of four redshift bins | Qu 2026, arXiv:2604.19744 | [src] |
| Stacking | ACT DR6 | DESI DR2 BGS and ELGs | up to ~9 (BGS) and ~7.5 (ELG) | Hadzhiyska 2026, arXiv:2604.19745 | [src] |
| Harmonic-space P_ge with a momentum template | ACT DR6; SPT-3G | DESI Legacy imaging LRGs | 11.7σ (ACT), 8.4σ (SPT-3G), 12.3σ (SPT-3G + ACT northern cap) | Hotinli 2026, arXiv:2609.17676 | [src] |
| Projected field (kSZ² × galaxies) | Planck + WMAP cleaned maps | WISE galaxies, z ≈ 0.4 | 3.8–4.5σ | Hill 2016, arXiv:1603.01608 | [src] |
| Projected field | Planck + WMAP cleaned maps | unWISE, three samples, > 500 million galaxies | combined S/N > 5 | Kusiak 2021, arXiv:2102.01068 | [src] |
| Velocity reconstruction (quadratic estimator) × BOSS velocity template | ACT DR6 | DESI Legacy LRGs (photometric) | null rejected at 3.8σ; first significant velocity reconstruction | McCarthy 2024, arXiv:2410.06229 | [src] |
| Velocity reconstruction × galaxy density, tomographic QML | ACT DR6 | DESI Legacy DR9 | 11.7σ | Lai 2025, arXiv:2506.21684 | [src] |
| Velocity reconstruction × continuity-equation velocity | ACT DR6 | DESI Legacy LRGs | ~10σ cross; auto-spectrum 2.1σ; combined 11σ | McCarthy 2025, arXiv:2511.15701 | [src] |
| Velocity reconstruction, parity-odd tomographic estimator | ACT DR6 | DESI Legacy imaging galaxies | 11σ | Embil Villagra 2026, arXiv:2603.28746 | [src] |
| Velocity reconstruction, spectroscopic | ACT DR6 | DESI DR2 LRG, ELG, QSO | v–g: 17.0σ (LRG), 8.3σ (ELG), 6.8σ (QSO); v–v: 3.1σ (LRG); cumulative 20.8σ | Chaussidon 2026, arXiv:2604.04867 | [src] |

### 2.2 Gas: what the kSZ profile says about baryons and feedback
<!-- key: gas-what-the-ksz-profile-says-about-baryons-and -->

| Statement | Number | Data | Citation | Flag |
|---|---|---|---|---|
| Baryon abundance from the projected-field amplitude | (f_b/0.158)(f_free/1.0) = 1.48 ± 0.19 (stat) at z ≈ 0.4 | Planck + WMAP × WISE | arXiv:1603.01608 | [src] |
| Projected-field amplitude per unWISE sample (fiducial = 1) | 0.42 ± 0.31 ± 0.14; 5.02 ± 1.01 ± 0.47; 8.23 ± 3.23 ± 1.60 (stat, sys) at z ≈ 0.6, 1.1, 1.5 | Planck + WMAP × unWISE | arXiv:2102.01068 | [src] |
| Gas profile more extended than the dark matter | "> 90σ" formally for the cosmic baryon abundance | ACT DR5 × CMASS | arXiv:2009.05557 | [src] |
| Electron temperature from tSZ/kSZ | measured to 20% in several apertures, comparable to virial | ACT DR5 × CMASS | arXiv:2009.05557 | [src] |
| Feedback energy and non-thermal pressure | ε = (40 ± 9) × 10⁻⁶ (in ε M⋆c²); α_Nth < 0.2 (2σ) | ACT DR5 × CMASS, kSZ + tSZ | Amodeo 2020, arXiv:2009.05558 | [src] |
| Gas extends beyond the dark-matter halo | 99.5% confidence (PTE = 0.005) | DESI Y1 LRG × ACT DR6 | arXiv:2503.19870 | [src] |
| Simulation preference, free amplitude | Illustris (z = 0.5) PTE = 0.37; IllustrisTNG (z = 0.8) PTE = 0.045; "limited statistical significance" | same | arXiv:2503.19870 | [src] |
| Amplitude relative to a halo-model prediction | A = 0.39 ± 0.04 | ACT DR6 × DESI Legacy, velocity reconstruction | arXiv:2506.21684 | [src] |
| kSZ velocity bias b_v (an analogous amplitude; defined in `physics-and-methods.md` §3.2) | 0.339 ± 0.034 (cross); 0.26 +0.11/−0.05 (auto); 0.33 ± 0.03 (combined) | ACT DR6 × DESI Legacy LRG | arXiv:2511.15701 | [src] |
| kSZ velocity bias b_v, spectroscopic LRGs, joint v–g and v–v fit | 0.229 ± 0.022 (90 GHz); 0.233 ± 0.020 (150 GHz); best fits 0.233 and 0.237 | ACT DR6 × DESI DR2 LRG | arXiv:2604.04867, table of LRG fits | [src] |
| Mean halo masses, lensing-calibrated | log(M_halo/(M⊙/h)) ≈ 13.18 (Main LRG), 13.03 (Extended LRG), 13.02 (BGS) | DESI samples × ACT DR6 κ | Hadzhiyska 2025, arXiv:2507.14136 | [src] |
| Gas fractions against TNG300 | lower at fixed radius by ≳ 4σ; all baryons recovered at 2–3 virial radii | same, with the kSZ profiles | arXiv:2507.14136 | [src] |
| Baryon fraction within the virial radius, low-mass groups (10^12.5–10^14 h⁻¹M⊙) | 0.21 ± 0.06 of the universal fraction | DESI Legacy groups × ACT, AbacusSummit forward model | Roper 2025, arXiv:2510.12553 | [src] |
| Gas within the virial radius | 25–33% of the halo's cosmic baryon budget (needs an external halo mass) | ACT DR6 + SPT-3G × DESI Legacy LRG | arXiv:2609.17676 | [src] |
| Fiducial feedback models against DESI Y1 + ACT kSZ | disfavoured at > 3σ; strong-AGN FLAMINGO and BAHAMAS variants and SIMBA within < 2σ | FLAMINGO, ANTILLES, BAHAMAS, SIMBA, FABLE | Bigwood 2025, arXiv:2510.15822 | [src] |
| Fiducial FLAMINGO against kSZ + eROSITA | kSZ combined > 8σ discrepant; eROSITA gas fractions 2× lower than the simulation | DESI + ACT kSZ, eROSITA, galaxy–galaxy lensing | Siegel 2025, arXiv:2509.10455 | [src] |
| Matter power suppression at k = 1 h/Mpc | 10 ± 2% (eROSITA + kSZ); 5 ± 4% (HSC-XXL gas fractions) | baryonification fit | Siegel 2025, arXiv:2512.02954 | [src] |
| S_8 from cosmic shear with kSZ-informed baryons | 0.823 +0.019/−0.020 | DES Y3 shear + ACT DR5 kSZ, baryonification | Bigwood 2024, arXiv:2404.06098 | [src] |
| Model-independent f_gas(R): depletion relative to the cosmic mean | SNR 17.2 (BGS), 13.8 (LRG bin 1); fiducial FLAMINGO "most closely tracks" the data | DESI DR2 × ACT DR6 kSZ / HSC Y3 lensing ratio | Liu 2026, arXiv:2609.22466 | [src] |
| Halo mass bias when baryons are ignored in a lensing fit | ~20% low | BOSS CMASS kSZ + galaxy–galaxy lensing | Sunseri 2025, arXiv:2505.20413 | [src] |
| Optical depth of the Extended LRG sample from patchy screening | τ < 2.5 × 10⁻⁴ (95%), for a mean τ ≈ 1.6 × 10⁻⁴; kSZ detected at 7.2σ in the same analysis | ACT DR5 × DECaLS DR9 LRG | Hadzhiyska 2025, arXiv:2506.17379 | [src] |

The ACT DR6 × DESI results favour gas that is more extended than in the Battaglia profile and in IllustrisTNG (arXiv:2407.07152, arXiv:2604.19744, arXiv:2604.04867) [src]. The counter-evidence is in `open-questions.md` §2.

### 2.3 Velocities: cosmology from the large-scale kSZ signal
<!-- key: velocities-cosmology-from-the-large-scale-ksz -->

| Quantity | Value | Data | Citation | Flag |
|---|---|---|---|---|
| f_NL (local) from v–g | −180 +61/−86 (67%); consistent with zero at 95% | ACT DR6 × DESI Legacy LRG, photometric | arXiv:2511.15701 | [src] |
| f_NL (local) from v–g and v–v | 15.9 +34.6/−34.4 (68%) | ACT DR6 × DESI DR2 LRG, ELG, QSO | arXiv:2604.04867 | [src] |
| f_NL (local), LRGs only, v–g and v–v | mean 11.7, −43.5/+43.4; best fit 8.5 | ACT DR6 × DESI DR2 LRG | arXiv:2604.04867, table of LRG fits | [src] |
| Force-law index n in g ∝ 1/rⁿ, 30–230 Mpc | 2.1 ± 0.3 | ACT × SDSS pairwise kSZ | Gallardo 2026, arXiv:2604.14327 | [src] |
| Per-mode noise of the kSZ velocity field against the galaxy auto-spectrum | lower at k < 0.004 Mpc⁻¹ | ACT DR6 × DESI DR2 | arXiv:2604.04867 | [src] |
| H_0 f σ_8² | constrained only if τ̄ and bias are supplied externally; proof of concept | DESI DR1 BGS × ACT DR6 pairwise | arXiv:2510.14135 | [src] |

No fσ_8 value has been published from kSZ: the amplitude is degenerate with the optical depth (see `systematics.md` §8). The peculiar-velocity reading of these numbers is in `cosmo-peculiar-velocities`.

### 2.4 kSZ auto-power (no LSS tracer)
<!-- key: ksz-auto-power-no-lss-tracer -->

| Quantity | Value | Data | Citation | Flag |
|---|---|---|---|---|
| D_3000^kSZ | 1.75 ± 0.86 μK² (free angular shapes) | SPT-3G D1, 1646 deg², 95/150/220 GHz, 1700 ≤ ℓ ≤ 11,000 | Chaubal 2026, arXiv:2601.20551 | [src] |
| D_3000^tSZ at 143 GHz | 4.91 ± 0.37 μK² | same | arXiv:2601.20551 | [src] |
| Duration of reionisation | Δ⁵⁰z_re < 3.8 (95%, semi-analytic model); Δ⁹⁰z_re < 6.1 (AMBER) | same | arXiv:2601.20551 | [src] |

The paper states that the inferred SZ powers depend on the modelling of the tSZ–CIB correlation.

## 3. Thermal Sunyaev–Zel'dovich × LSS
<!-- key: thermal-sunyaev-zel-dovich-x-lss -->

### 3.1 tSZ × galaxy positions: bias-weighted pressure
<!-- key: tsz-x-galaxy-positions-bias-weighted-pressure -->

| Quantity | Value | Data | Citation | Flag |
|---|---|---|---|---|
| Galaxy–y detection | ~12σ in multiple redshift bins; ⟨bP_e⟩ constrained over 0.15 ≲ z ≲ 0.75 | DES Y1 galaxies × Planck y | Pandey 2019, arXiv:1904.13347 | [src] |
| ⟨b_h P_e⟩ in meV cm⁻³ | 0.16 +0.03/−0.04, 0.28 +0.04/−0.05, 0.45 +0.06/−0.10, 0.54 +0.08/−0.07, 0.61 +0.08/−0.06, 0.63 +0.07/−0.08 at z ≈ 0.30, 0.46, 0.62, 0.77, 0.89, 0.97 | DES Y3 galaxies × SPT + Planck y | Sánchez 2022, arXiv:2210.08633 | [src] |
| Preferred AGN heating temperature (cosmo-OWLS profiles) | 10^8.5 K consistent; 10^8.0 K incompatible | same, small scales | arXiv:2210.08633 | [src] |
| ⟨bP_e⟩ and ⟨bρ_SFR⟩ to z ~ 1, jointly | broadly compatible with fiducial FLAMINGO; lower pressure at low z | photometric galaxies × multi-frequency CMB maps | La Posta 2026, arXiv:2603.04269 | [src] |
| Scaling with cosmology in FLAMINGO | ⟨b_h P_e⟩ ∝ S_8^ε with ε ≈ 3 over 0.1 ≤ z ≤ 1 | simulation | Salcido 2026, arXiv:2605.11083 | [src] |
| S_8 from the compiled ⟨bP_e⟩(z) measurements | 0.72 ± 0.03, with a group-mass baryon fraction f_b(10¹³ M⊙, z = 0.1)/(Ω_b/Ω_m) = 0.10 +0.09/−0.05 | SDSS, BOSS, eBOSS, DES, DESI tracers × Planck y, fitted with FLAMINGO | arXiv:2605.11083 | [src] |
| Radio emission in the unWISE × multi-frequency spectra | model with radio preferred at 9.5σ (Low-z, z̄ = 0.14) and 11σ (Mid-z, z̄ = 0.23) | unWISE × Planck PR4 nine bands and ACT DR6 | Zhao 2026, arXiv:2606.28099 | [src] |
| Stacked tSZ, ~2′ disk | S/N > 38 (DESI DR1 LRG), 27 (BGS), 39 (eROMaPPer clusters) at 90 GHz | ACT DR6 + Planck | Moore 2026, arXiv:2609.08939 | [src] |

### 3.2 tSZ × lensing
<!-- key: tsz-x-lensing-2 -->

| Quantity | Value | Data | Citation | Flag |
|---|---|---|---|---|
| First lensing × tSZ detection | 6σ; (b_gas/1)(T_e/0.1 keV)(n_e/1 m⁻³) = 2.01 ± 0.31 ± 0.21 at z = 0 | CFHTLenS mass map × Planck tSZ map | Van Waerbeke 2013, arXiv:1310.5721 | [src] |
| Shear × y detection | 21σ; data prefer a low small-scale pressure amplitude (strong AGN feedback) | DES Y3 shear × ACT + Planck y | Gatti 2021, arXiv:2108.01600 | [src] |
| S_8; Ω_m from small-scale shear + shear × y | 0.811 +0.015/−0.012; 0.263 +0.023/−0.030 | DES Y3 shear × ACT DR6 + Planck y; shear × y detected at 21σ | Pandey 2025, arXiv:2506.07432 | [src] |
| Matter power suppression | 2–4σ tension with mild-feedback simulations; reduced pressure in haloes with M < 10¹⁴ M⊙/h | same | arXiv:2506.07432 | [src] |
| Shear × tSZ with CIB marginalised at the multi-frequency spectrum level | compatible with FLAMINGO only for low S_8; the Planck S_8 "strongly disfavoured", independently of the FLAMINGO feedback variant | DES shear × Planck frequency maps | Wayland 2026, arXiv:2609.31774 | [src] |
| Gas model from shear × y and shear × X-ray | log₁₀ M_c = 14.83 +0.16/−0.23; Γ = 1.144 +0.016/−0.013; α_T = 1.30 +0.15/−0.28 | DES Y3 shear × Planck y × ROSAT | La Posta 2024, arXiv:2412.12081 | [src] |
| CMB lensing × y amplitude relative to a halo model | A = 0.82 ± 0.21 (PR4 κ); 0.56 ± 0.24 (PR3 κ from a tSZ-deprojected map) | Planck PR4 NILC y with CIB moment deprojection | McCarthy 2023, arXiv:2308.16260 | [src] |

The S_8 values in this subsection do not agree with each other: 0.811 +0.015/−0.012 (arXiv:2506.07432) against 0.72 ± 0.03 (arXiv:2605.11083) and a "strongly disfavoured" Planck value (arXiv:2609.31774). See `open-questions.md` §3.

## 4. Integrated Sachs–Wolfe effect
<!-- key: integrated-sachs-wolfe-effect -->

A_ISW is the measured amplitude divided by the ΛCDM prediction. The two families of measurement, full cross-correlation and stacking on superstructures, are kept apart because they have disagreed.

### 4.1 Cross-correlation of temperature with LSS tracers
<!-- key: cross-correlation-of-temperature-with-lss -->

| Tracer | Result | Citation | Flag |
|---|---|---|---|
| NVSS, SDSS, WISE and the Planck 2015 lensing map | 4σ combined; ~3σ from Planck alone through the ISW–lensing bispectrum; Ω_Λ detected at > 3σ | Planck Collaboration 2015, arXiv:1502.01595 | [src] |
| SDSS DR12 photo-z, 2MASS photo-z, WISE × SuperCOSMOS, SDSS QSO, NVSS, in redshift bins | 4.7–5.0σ; ~4.0σ without tomography | Stölzner 2017, arXiv:1710.03238 | [src] |
| unWISE, 3 samples over 0 < z < 2, × Planck temperature | 3.2σ; A_ISW = 0.96 ± 0.30 | Krolewski 2021, arXiv:2110.13959 | [src] |
| Quaia quasars, tomographic, × Planck temperature | 2.8σ; A_ISW ≃ 1.69 ± 0.61 relative to Planck ΛCDM; the DESI-favoured w0wa models "do not account for" the excess | Ghodsi Yengejeh 2026, arXiv:2607.22461 | [src] |

### 4.2 Stacking on voids and superclusters
<!-- key: stacking-on-voids-and-superclusters -->

| Structures | Result | Citation | Flag |
|---|---|---|---|
| BOSS CMASS voids and superclusters, matched filter | A_ISW = 1.64 ± 0.53 (3.1σ), in agreement with ΛCDM | Nadathur 2016, arXiv:1608.08638 | [src] |
| 87 DES supervoids, 0.2 < z < 0.9, 5000 deg² | A_ISW ≈ 4.1 ± 2.0; with BOSS 5.2 ± 1.6 (3.3σ detection, 2.6σ from ΛCDM) | Kovács 2018, arXiv:1811.07812 | [src] |
| ~800 eBOSS DR16 quasar supervoids | A_ISW ≈ 3.6 ± 2.1 at 0.8 < z < 1.2; opposite-sign signal at 1.5 < z < 2.2, 2.7σ from ΛCDM | Kovács 2021, arXiv:2107.13038 | [src] |
| DESI Legacy Survey superstructures, 4 bins, 0 < z < 0.8 | voids A_ISW = −0.10 ± 0.69; clusters 1.52 ± 0.72; "strongly inconsistent with previous claims" of many times ΛCDM | Hang 2021, arXiv:2105.11936 | [src] |
| Nearby underdensities, z < 0.03 | temperature excess found in < 0.2% of simulated maps; amplitude an order of magnitude above ISW + Rees–Sciama and of opposite sign | Hansen 2025, arXiv:2506.08832 | [src] |

The stacked CMB lensing signal of the same DESI Legacy superstructures agrees with mocks except in the highest-redshift density peaks, where the mock prediction is higher by a factor ~1.3 (arXiv:2105.11936) [src].

## 5. Cosmic infrared background
<!-- key: cosmic-infrared-background -->

The CIB appears in this domain in three roles: a high-redshift matter tracer correlated with CMB lensing, a probe of the star-formation history, and the main contaminant of tSZ and lensing cross-correlations (for the last, see `systematics.md` §3).

| Quantity | Value | Data | Citation | Flag |
|---|---|---|---|---|
| f_NL (local) from CIB × κ | 43 ± 23; a factor ~2 better than earlier CIB analyses | new large-scale dust-cleaned Planck CIB maps × Planck lensing | Thornton 2026, arXiv:2605.03783 | [src] |
| Correlation of a co-added tracer (ACT DR6 κ + unWISE + Planck CIB) with the true convergence | 55–85% at L ≤ 2000 | ACT DR6 | Hertig 2025, arXiv:2511.21949 | [src] |
| Lensing B-mode power removed with that template | ~39% at 100 ≤ ℓ ≤ 1500 (ACT DR6 B modes); 47% at 30 ≤ ℓ ≤ 300 (Planck B modes); 23% of the sky | same | arXiv:2511.21949 | [src] |
| Variance reduction of κ power and κ cross-correlations when a third tracer (CIB or LRGs) removes structure from κ | 10–20% | Planck + DESI Legacy Surveys | Baleato Lizancos 2023, arXiv:2301.10242 | [src] |
| ⟨bρ_SFR⟩(z) to z ~ 1, fitted jointly with ⟨bP_e⟩ | broadly compatible with fiducial FLAMINGO | photometric galaxies × multi-frequency CMB maps | arXiv:2603.04269 | [src] |
| Effective CIB dust parameters correlated with low-z unWISE galaxies | β_0 = 1.79 ± 0.29, T_0 = 22.0 ± 5.1 K (z̄ = 0.14); β_0 = 1.41 ± 0.13, T_0 = 28.0 ± 4.2 K (z̄ = 0.23) | unWISE × Planck PR4 | arXiv:2606.28099 | [src] |

## 6. Other secondaries (status)
<!-- key: other-secondaries-status -->

| Effect | Status | Number | Data | Citation | Flag |
|---|---|---|---|---|---|
| Moving lens (transverse velocities) | First detection reported in 2026 | b_ML = 1.24 ± 0.26 (4.8σ, extended LRG sample); 0.93 ± 0.25 (3.7σ, main sample); consistent with the halo-model prediction | ACT DR6 NILC map × DESI Legacy LRGs | Hotinli 2026, arXiv:2605.18938 | [src] |
| Patchy (anisotropic) screening, stacked on LRGs | ~4.1σ signal in excess of the kSZ-based expectation, attributed to CMB lensing contamination | τ < 2.5 × 10⁻⁴ (95%) after accounting for lensing | ACT DR5 × DECaLS DR9 extended LRGs | arXiv:2506.17379 | [src] |
| Anisotropic screening power spectrum (no tracer) | No detection; upper limit two orders of magnitude above reionisation-model predictions; evidence of foreground contamination at one frequency | ACT DR6 | Kramer 2026, arXiv:2608.27458 | [src] |
| Rotational kSZ | 2.3σ measurement | rotational velocity ~100–200 km/s peaking near half the virial radius, groups of mean mass 10¹⁴ h⁻¹M⊙ | Planck temperature, oriented stacking on SDSS DR7 groups | Yang 2026, arXiv:2603.14494 | [src] |
| Polarised SZ (remote quadrupole) | Not detected; expected S/N of order 1 | b_q = 1.02 ± 2.64; τ_rei = −0.01 ± 0.14 | Planck + ACT × unWISE and Planck CIB | Krywonos 2026, arXiv:2607.16071 | [src] |

## 7. History of the key numbers
<!-- key: history-of-the-key-numbers -->

### 7.1 CMB lensing tomography
<!-- key: cmb-lensing-tomography -->

1. unWISE × Planck gave S_8 = 0.784 ± 0.015, 2.4σ below Planck (arXiv:2105.03421) [src]. The reanalysis with ACT DR6 lensing, additional spectroscopic redshift calibration, a more flexible model and blinding gave 0.810 ± 0.015 with ACT and Planck together, "fully consistent" with the primary CMB (arXiv:2309.05659) [src]. The 2021 value is superseded. Appendix "Reanalysis of the cross-correlation of Planck lensing and unWISE" of arXiv:2309.05659 itemises the shift for the Planck-only reanalysis: Monte Carlo lensing normalisation correction +0.6σ, modelling improvements −0.5σ, systematics weighting of the galaxies +0.4σ, additional spectroscopic data for the redshift distributions +0.8σ, PR4 instead of PR3 lensing +0.2σ, PCA-based dN/dz marginalisation −0.2σ with ~15% wider posteriors; total +1.3σ with ~15% wider posteriors [src, table in that appendix]. The redshift-distribution change is dominated by the Blue sample (0.74σ, against 0.14σ for Green) [src].
2. DESI-targeting LRGs × Planck gave S_8 = 0.73 ± 0.03 (arXiv:2111.09898) [src]. The reanalysis with spectroscopically calibrated samples, PR4 and ACT DR6 lensing and HEFT gave 0.765 ± 0.023 (Planck) and 0.775 +0.019/−0.022 (ACT + Planck), described by its authors as "less discrepant with primary CMB measurements than previous DESI LRG cross Planck CMB lensing results" (arXiv:2407.04607) [src]. The 2021 value is superseded. Section "Planck PR3 reanalysis" of arXiv:2407.04607 quotes the earlier result as S_8 = 0.725 ± 0.030 with a best fit of 0.751, finds 0.762 ± 0.023 with the new sample and the same PR3 map, and attributes the ≃ 1σ shift of the mean to four changes: consistent neutrino masses in the power-spectrum emulator ΔS_8 = +0.017, the Monte Carlo normalisation correction of the PR3 cross-correlation +0.015, an informative prior tying the two counterterms that removes a "volume effect" +0.014, and the updated LRG sample −0.012 [src, that section]. Part of the old low value was therefore a projection effect: the 2021 mean sat ~1σ below its own best fit [src, section "Volume effect estimation"].
3. DES Y3 × SPT-SZ + Planck cross-correlations alone gave S_8 ≈ 0.74 (arXiv:2203.12440) [src]. The shear × SPT-3G D1 measurement, on ~1300 deg², gives 0.833 +0.047/−0.061 and is consistent with both Planck and DES Y3 shear (arXiv:2606.26223) [src].
4. Quaia × Planck gave σ_8 = 0.766 ± 0.034, with the low value driven by the z ≈ 2.1 bin and tentatively attributed to foreground contamination of the lensing map (arXiv:2306.17748) [src]. The ACT DR6 + Planck PR4 reanalysis finds "no evidence for contamination in the lensing maps" and σ_8 = 0.802 +0.045/−0.057 (arXiv:2507.08798) [src].
5. The LRG-based values remain the lowest of the current set: 0.765–0.776 for S_8 or S_8^× from the DESI LRG samples (arXiv:2407.04607, arXiv:2407.04606, arXiv:2510.17796), against 0.810–0.816 from unWISE (arXiv:2309.05659, arXiv:2409.02109) [src].

### 7.2 kSZ detections and their reading
<!-- key: ksz-detections-and-their-reading -->

1. Significance by estimator. Pairwise: evidence at p = 0.002 (arXiv:1203.4219), 5.4σ (arXiv:2101.08374), 9.3σ with DESI DR1 (arXiv:2511.23417). Velocity-weighted stacking: 3.3σ (arXiv:1510.06442), 6.5σ (arXiv:2009.05557), 13σ photometric (arXiv:2407.07152), ≈ 10 spectroscopic DESI Y1 (arXiv:2503.19870), 18σ DESI DR2 (arXiv:2604.19744). Velocity reconstruction: 3.8σ (arXiv:2410.06229), ~11σ (arXiv:2506.21684, arXiv:2511.15701, arXiv:2603.28746), 17σ for LRGs and 20.8σ cumulative with DESI DR2 (arXiv:2604.04867). All [src].
2. Reading of the amplitude. The 2016 projected-field result, (f_b/0.158)(f_free/1.0) = 1.48 ± 0.19, was taken as showing that "baryons approximately trace the dark matter distribution down to ~Mpc scales" (arXiv:1603.01608) [src]. From 2020 the profile measurements show gas more extended than the dark matter (arXiv:2009.05557), and from 2024 the DESI-based measurements are read as evidence for strong feedback (arXiv:2407.07152 and the rows of §2.2) [src]. The two statements concern different scales and are not in conflict.
3. The z ≈ 1.1 unWISE projected-field amplitude of 5.02 ± 1.01 (arXiv:2102.01068) is an unexplained excess that its authors could not attribute to foregrounds [src]; no later projected-field measurement was found this session.

### 7.3 tSZ × lensing
<!-- key: tsz-x-lensing -->

The first detection, CFHTLenS × Planck at 6σ (arXiv:1310.5721), was followed by KiDS-1000 × Planck + ACT (arXiv:2109.04458), DES Y3 × ACT + Planck at 21σ (arXiv:2108.01600) and the DES Y3 × ACT DR6 joint cosmology and feedback fit, also 21σ (arXiv:2506.07432) [src]. The interpretation has moved from "warm baryons trace the large-scale structure" (2013) to constraints on AGN feedback and, since 2025, to S_8 values that disagree with each other (§3.2).

### 7.4 ISW
<!-- key: isw -->

Planck 2015 combined detection 4σ (arXiv:1502.01595); tomographic five-catalogue analysis 4.7–5.0σ (arXiv:1710.03238); unWISE alone 3.2σ with A_ISW = 0.96 ± 0.30 (arXiv:2110.13959); Quaia alone 2.8σ with 1.69 ± 0.61 (arXiv:2607.22461) [src]. The supervoid excess reported from 2018 (arXiv:1811.07812) was not reproduced in the DESI Legacy analysis of 2021 (arXiv:2105.11936) [src].

## 8. Not verified
<!-- key: not-verified -->

- No value is given here for the tSZ–CIB correlation coefficient, the Planck all-sky y-map properties, or the first CIB × CMB lensing correlations: the papers were not read this session.
- kSZ velocity-bias values for DESI ELGs and quasars (arXiv:2604.04867) were not read beyond the abstract and the LRG table.
- The Planck release behind the lensing map of arXiv:2105.03421 and arXiv:2111.09898 is not stated in their abstracts; arXiv:2309.05659 and arXiv:2407.04607 identify both as PR3 [src, appendix and section named in §7.1].
- Significances quoted "from Planck" use each paper's own metric and Planck likelihood; they were not homogenised.
