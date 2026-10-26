# Galaxy-cluster cosmology — results

Scope: headline cosmological constraints from cluster samples, with model and provenance, and the history of the cluster S8.
Snapshot: 2026-10-26

## eROSITA eRASS1 (X-ray selected, weak-lensing calibrated)
<!-- key: erosita-erass1-x-ray-selected-weak-lensing -->

All rows use the eRASS1 cosmology sample of 5259 clusters over 12791 deg² [src: abstract] with weak-lensing mass calibration from DES Y3, KiDS-1000 and HSC (Ghirardini et al. 2024, arXiv:2402.08458).

| Quantity | Value | Model | Data | Citation | Flag |
|---|---|---|---|---|---|
| Ω_m | 0.29 +0.01/−0.02 | flat ΛCDM | eRASS1 counts + WL | arXiv:2402.08458 | [src: abstract] |
| σ8 | 0.88 ± 0.02 | flat ΛCDM | same | arXiv:2402.08458 | [src: abstract] |
| S8 = σ8 (Ω_m/0.3)^0.5 | 0.86 ± 0.01 | flat ΛCDM | same | arXiv:2402.08458 | [src: abstract] |
| Σm_ν | < 0.22 eV (95%) | νΛCDM | eRASS1 (as stated in the abstract; the abridged abstract does not list the external data entering this limit) | arXiv:2402.08458 | [src] |
| Σm_ν | 0.08 +0.03/−0.02 eV (normal) or 0.12 +0.03/−0.01 eV (inverted) | νΛCDM | eRASS1 + CMB + oscillation experiments | arXiv:2402.08458 | [src] |
| w | −1.12 ± 0.12 | flat wCDM | eRASS1 | arXiv:2402.08458 | [src: abstract] |
| log10 \|f_R0\| | < −4.31 (95%) | Hu–Sawicki f(R), massless neutrinos | eRASS1 counts + WL | Artis et al. 2024, arXiv:2402.08459 | [src: abstract] |
| log10 \|f_R0\|, Σm_ν | < −4.12 and < 0.44 eV (95%) jointly | Hu–Sawicki f(R) + massive neutrinos | same | arXiv:2402.08459 | [src: abstract] |
| growth index γ | 1.19 ± 0.21 | ΛCDM background + γ | eRASS1 counts + WL | Artis et al. 2024, arXiv:2410.09499 | [src: abstract] |
| f_EDE (max. early-dark-energy fraction) | < 0.3 | axion-like EDE | eRASS1 counts alone, 0.1 < z < 0.45 subsample | Strunk et al. 2026, arXiv:2609.07834 | [src: abstract] |
| f_EDE, H0 | 0.10 +0.04/−0.03; 71.4 ± 1.4 km/s/Mpc (about 3.2σ for non-zero EDE) | axion-like EDE | eRASS1 + primary CMB + BAO + CMB lensing, no distance ladder | arXiv:2609.07834 | [src: abstract] |
| Ω_c h² | 0.12 +0.03/−0.02 | ΛCDM, HOD modelling of cluster clustering | projected correlation function of 6493 eRASS1 clusters | Seppi et al. 2024, arXiv:2402.08460 | [src: Sect. 5.1] |
| cluster bias | 2.95 ± 0.21 (L_X = 4.63e43 erg/s, 0.1 < z < 0.2) to 4.34 ± 0.62 (L_X = 1.77e44 erg/s, 0.1 < z < 0.6) | HOD | eRASS1 volume-limited samples | arXiv:2402.08460 | [src: abstract] |

Reading notes.

- eRASS1 is the only current cluster sample whose S8 lies *above* the cosmic-shear values and at the Planck level. The growth-index result γ = 1.19 ± 0.21, in tension with 0.55 [src: abstract], comes from the same data: when the linear power spectrum is given an extra low-redshift degree of freedom, the eRASS1 S8 "recovers the value inferred by cosmic shear studies" (arXiv:2410.09499). The two statements are not contradictory, but they are often quoted separately as if they were.
- The EDE result of arXiv:2609.07834 uses only the 0.1 < z < 0.45 subsample and its 3.2σ preference appears only in the combination with CMB, BAO and CMB lensing. [src: abstract]

## South Pole Telescope (SZ selected, weak-lensing calibrated)
<!-- key: south-pole-telescope-sz-selected-weak-lensing -->

| Quantity | Value | Model | Data | Citation | Flag |
|---|---|---|---|---|---|
| Ω_m | 0.286 ± 0.032 | flat ΛCDM, Σm_ν marginalised | 1005 SPT clusters (SPT-SZ + SPTpol ECS + SPTpol 500d, 5200 deg², 0.25 < z < 1.78) + DES Y3 lensing (688 clusters, z < 0.95) + HST lensing (39 clusters, 0.6 < z < 1.7) | Bocquet et al. 2024, arXiv:2401.02075 | [src: abstract] |
| σ8 | 0.817 ± 0.026 | same | same | arXiv:2401.02075 | [src: abstract] |
| σ8 (Ω_m/0.3)^0.25 | 0.805 ± 0.016 | same | same | arXiv:2401.02075 | [src: abstract] |
| S8 = σ8 (Ω_m/0.3)^0.5 | 0.795 ± 0.029; 1.1σ from Planck 2018 TT,TE,EE+lowE | same | same | arXiv:2401.02075 | [src: abstract] |
| Σm_ν | < 0.18 eV (95%) | νΛCDM | SPT clusters + Planck 2018 | arXiv:2401.02075 | [src: abstract] |
| w | −1.45 ± 0.31 (clusters); −1.34 +0.22/−0.15 with Planck, 2.2σ from −1 | wCDM | as above | arXiv:2401.02075 | [src: abstract] |
| Ω_m, σ8 | 0.300 ± 0.017, 0.797 ± 0.026 | ΛCDM, Σm_ν free, 52 astrophysical nuisance parameters | SPT cluster abundance + DES Y3 3×2pt | Bocquet et al. 2025, arXiv:2412.07765 | [src: abstract] |
| S8 | 0.796 ± 0.013, 1.6σ below Planck | same | same | arXiv:2412.07765 | [src: abstract] |
| Σm_ν | < 0.25 eV (95%) | νΛCDM | SPT clusters + DES 3×2pt + Planck | arXiv:2412.07765 | [src: abstract] |
| w | −1.15 +0.23/−0.17; −1.20 +0.15/−0.09 with Planck (1.7σ from −1) | wCDM | same | arXiv:2412.07765 | [src: abstract] |
| log10 \|f_R0\| | < −5.32 (95%) | Hu–Sawicki f(R) | SPT clusters + Planck 2018 primary CMB | Vogt et al. 2024, arXiv:2409.13556 | [src: abstract] |
| halo bias; ln A_SZ | 5.30 ± 0.24; 0.43 +0.17/−0.21 (clustering detected at 12.8σ) | ΛCDM, analytic covariance | SPT-3G Main 5-year clusters, 0.25 < z < 1.1 | Martsen et al. 2026, arXiv:2610.08947 | [src: abstract] |

Superseded SPT values.

| Quantity | Value | Data | Citation | Flag |
|---|---|---|---|---|
| Ω_m, σ8, σ8 (Ω_m/0.3)^0.2 | 0.276 ± 0.047, 0.781 ± 0.037, 0.766 ± 0.025 (flat νΛCDM) | 343 SPT-SZ clusters at ξ > 5, 0.25 < z < 1.75; lensing for 32 clusters (Magellan, HST); Chandra for 89 | Bocquet et al. 2019, arXiv:1812.01679 | [src: abstract] |
| w | −1.55 ± 0.41 (νwCDM) | same | arXiv:1812.01679 | [src: abstract] |
| S8 | 0.831 ± 0.020 (ΛCDM) | SPT-SZ clusters + Planck power spectra; the 3.1σ CMB-cluster-lensing detection does not change the error | Chaubal et al. 2022, arXiv:2111.07491 | [src: abstract] |

Note the exponent: SPT quotes σ8 (Ω_m/0.3)^0.2 in 2019 (arXiv:1812.01679) and ^0.25 in 2024, with the standard S8 (^0.5) separately. The best-constrained combination has the small exponent; the S8 error is 0.029 against 0.016 for the optimal combination [src: abstract of each, arXiv:2401.02075].

## Atacama Cosmology Telescope (SZ selected)
<!-- key: atacama-cosmology-telescope-sz-selected -->

No cosmological analysis of the ACT DR5 or DR6 cluster number counts with ΛCDM parameters as output was found as of 2026-10-26. What exists:

| Quantity | Value | Model | Data | Citation | Flag |
|---|---|---|---|---|---|
| σ8, Ω_m | 0.829 ± 0.024, 0.292 ± 0.025 | ΛCDM, marginalised over a 15% dynamical-mass bias | 15 high-S/N ACT equatorial clusters + 7 southern clusters with dynamical masses + WMAP7 | Hasselfield et al. 2013, arXiv:1301.0816 | [src: abstract] |
| Σm_ν | < 0.29 eV (95%) | νΛCDM | ACT clusters + WMAP7 + BAO + H0 | arXiv:1301.0816 | [src: abstract] |
| 1 − b required to match CMB cosmology | Planck 2016 sample: 0.61 ± 0.03; ACT 2018 sample: 0.75 ± 0.06 | CMB cosmology fixed, Planck cluster model | Planck + ACT counts | Lee et al. 2024, arXiv:2403.19542 | [src: abstract] |
| w (or scaling-relation evolution β) | w = −0.82 ± 0.07, or β = 0.86 ± 0.07 | CCCP-based lensing normalisation | Planck + ACT counts | arXiv:2403.19542 | [src: abstract] |
| f_NL (local) | 55 ± 125 (68%) | ΛCDM with external priors, Log–Edgeworth mass function; scales 5–10 Mpc/h | 1201 ACT DR6 clusters in the 10347 deg² Legacy region | Sarieddine et al. 2026, arXiv:2602.03917 | [src: abstract] |
| residual mass bias | 16.4%, "heavily informed by our adopted priors" | same | same | arXiv:2602.03917 | [src: abstract] |

ACT weak-lensing mass calibration (the quantity 1 − b_SZ = M_SZ / M_WL, where M_SZ uses an X-ray-calibrated relation):

| 1 − b | Sample | Lensing | Citation | Flag |
|---|---|---|---|---|
| 0.65 ± 0.05 | 157 ACT DR5 clusters at > 5σ, mean uncorrected M_SZ = 3.64e14 M_sun | KiDS | Robertson et al. 2024, arXiv:2304.10219 | [src: abstract] |
| 0.74 +0.06/−0.05 (full); 0.81 +0.08/−0.06 (low z) and 0.58 +0.06/−0.05 (high z); redshift power-law index −1.8 +0.5/−0.6 | 443 ACT DR5 clusters, mean WL M500c = 5.4e14 M_sun; 7% precision on normalisation | DES Y3 | Shin et al. 2025, arXiv:2512.18935 | [src: abstract] |
| mean M500c = (1.7 ± 0.4)e14 M_sun, 4.2σ detection | 677 MaDCoWS clusters, mean z = 1.08 | CMB lensing (ACT + Planck) | Madhavacheril et al. 2020, arXiv:2009.07772 | [src: abstract] |

## Planck SZ clusters and the mass-bias question
<!-- key: planck-sz-clusters-and-the-mass-bias-question -->

Definition used throughout: (1 − b) = M_SZ / M_true, where M_SZ is the mass obtained from the SZ signal through a scaling relation calibrated on X-ray hydrostatic masses. A smaller (1 − b) means heavier clusters and a higher σ8 from the same counts.

| Quantity | Value | Model / calibration | Data | Citation | Flag |
|---|---|---|---|---|---|
| σ8, Ω_m, σ8 (Ω_m/0.27)^0.3 | 0.75 ± 0.03, 0.29 ± 0.02, 0.764 ± 0.025 | flat ΛCDM, (1 − b) flat in [0.7, 1.0] | 189 clusters at S/N > 7 | Planck 2013 XX, arXiv:1303.5080 | [src: abstract] |
| σ8 (Ω_m/0.27)^0.3; σ8 | 0.78 ± 0.01; 0.77 ± 0.02 | (1 − b) fixed at 0.8 | same | arXiv:1303.5080 | [src: Sect. 5.1] |
| bias needed to match the 2013 primary CMB | "about 40%" | — | — | arXiv:1303.5080 | [src: abstract] |
| tension with primary CMB | from "a little over one standard deviation" to 3.7σ depending on the (1 − b) prior | flat ΛCDM | 439 clusters at S/N > 6 (PSZ2 cosmology sample) | Planck 2015 XXIV, arXiv:1502.01597 | [src: abstract] |
| σ8 (Ω_m/0.33)^0.25; 1 − b_SZ | 0.765 ± 0.035; 0.71 ± 0.10; no tension with primary CMB | ΛCDM, CMB-lensing masses of all 433 clusters | Planck MMF3 cosmology sample | Zubeldia & Challinor 2019, arXiv:1904.07887 | [src: abstract] |
| α_SZ; (1 − b)_SZ; Ω_m | 1.49 +0.07/−0.10 (about 4σ from self-similar 1.8); 0.69 +0.07/−0.14; 0.30 ± 0.03 (Planck alone: 0.37 +0.02/−0.06) | νΛCDM | Planck + SPT-SZ clusters with SPT lensing and X-ray follow-up | Salvati et al. 2022, arXiv:2112.03606 | [src: abstract] |
| σ8, Ω_m, S8 | 0.77 ± 0.02, 0.31 ± 0.02, 0.78 ± 0.02 (self-similar evolution); S8 = 0.81 ± 0.02 with fitted evolution | flat ΛCDM | Planck cosmology sample; Chandra Y_X relation; CCCP + MENeaCS lensing | Aymerich et al. 2024, arXiv:2402.04006 | [src: abstract] |
| 1 − b | 0.89 ± 0.04 (Chandra-calibrated relation); 0.76 ± 0.04 (XMM-calibrated relation) | CCCP + MENeaCS lensing | subset of the Planck cosmology sample | arXiv:2402.04006 | [src: abstract] |
| Ω_m, σ8, S8, 1 − b | 0.312 +0.018/−0.024, 0.777 ± 0.024, 0.791 +0.023/−0.021, 0.844 +0.055/−0.062 | flat ΛCDM, constant bias | PSZ2 cosmology sample + DES shear profiles + Chandra + BAO | Aymerich et al. 2025, arXiv:2509.02068 | [src: abstract] |
| Ω_m, σ8, S8 | 0.353 +0.025/−0.031, 0.751 ± 0.023, 0.814 +0.019/−0.020 | mass-dependent bias | same | arXiv:2509.02068 | [src: abstract] |
| tension | 1.6σ with CMB; 2.9σ with eRASS1 clusters | — | same | arXiv:2509.02068 | [src: abstract] |
| 1 − b_SZ from clustering | 0.62 +0.14/−0.11; σ8 unconstrained | Planck CMB priors on cosmology | redshift-space 2PCF of 920 Planck clusters at z ≤ 0.8, 10–150 Mpc/h | Lesci et al. 2023, arXiv:2302.14074 | [src: abstract] |

Direct lensing calibrations of the Planck mass scale, in order of publication:

| M_Planck / M_WL | Sample | Citation | Flag |
|---|---|---|---|
| 0.688 ± 0.072 (22 clusters); 0.698 ± 0.062 (38 clusters) | Weighing the Giants | von der Linden et al. 2014, arXiv:1402.2670 | [src: abstract] |
| 0.76 ± 0.05 (stat) ± 0.06 (syst) | CCCP, 50 clusters | Hoekstra et al. 2015, arXiv:1502.01883 | [src: abstract] |
| 0.71 ± 0.10 | Planck CMB lensing, 433 clusters | arXiv:1904.07887 | [src: abstract] |
| 0.73 +0.10/−0.11 at z_eff ≈ 0.24 | 19 Planck clusters, HSC-SSP Y3 | Plazas Malagón et al. 2026, arXiv:2606.17984 | [src: abstract] |
| 0.72 ± 0.11 (unit slope, no evolution); M_SZ/M_500 = 0.83 ± 0.09 at 7e14 M_sun, z = 0.25 (baseline regression); 8% systematic | 41 CHEX-MATE clusters, Subaru and CFHT | Umetsu et al. 2026, arXiv:2606.24142 | [src: abstract] |
| 0.844 +0.055/−0.062 (relative to a *Chandra*-calibrated relation, not the Planck XMM one) | PSZ2 + DES | arXiv:2509.02068 | [src: abstract] |

The Aymerich values of (1 − b) cannot be compared directly with the others: the Chandra-calibrated relation already shifts masses, so that the same lensing data give 0.89 for Chandra and 0.76 for XMM [src, arXiv:2402.04006]. The cosmology is unchanged by that choice. [src: abstract]

The physical test of Aymerich et al. 2025 (arXiv:2509.08673): with the mass calibration fixed, the Planck cosmology sample would contain 498 clusters in the SPT best-fit cosmology and 1098 in the eROSITA one, against 439 observed [src: abstract]; fitting only the bias gives 0.790 ± 0.070 (SPT) and 0.630 ± 0.034 (eROSITA) [src]; the predicted tSZ power spectrum in the eROSITA cosmology is "two times higher at all scales" than the Planck measurement [src].

## X-ray selected samples before eROSITA
<!-- key: x-ray-selected-samples-before-erosita -->

| Quantity | Value | Model | Data | Citation | Flag |
|---|---|---|---|---|---|
| w0; Ω_Λ > 0 significance | −1.14 ± 0.21; about 5σ | flat, constant w | 36 clusters at ⟨z⟩ = 0.55 (400 deg² ROSAT survey) + 49 at z ≈ 0.05 (RASS), Chandra follow-up | Vikhlinin et al. 2009, arXiv:0812.2720 | [src: abstract] |
| w0 | −0.991 ± 0.045 (stat) ± 0.039 (sys) | flat, constant w | clusters + SN + WMAP + BAO | arXiv:0812.2720 | [src: abstract] |
| Σm_ν | < 0.33 eV (95%) | νΛCDM | same four data sets | arXiv:0812.2720 | [src: abstract] |
| Ω_m, σ8, w | 0.23 ± 0.04, 0.82 ± 0.05, −1.01 ± 0.20 | flat, constant w | 238 RASS clusters with Chandra follow-up | Mantz et al. 2010, arXiv:0909.3098 | [src: abstract] |
| σ8 (Ω_m/0.3)^0.17; Ω_m; σ8 | 0.81 ± 0.03; 0.26 ± 0.03; 0.83 ± 0.04 | flat ΛCDM, minimal neutrino mass | RASS clusters + Chandra + Weighing the Giants lensing (mass scale to 8%) | Mantz et al. 2015, arXiv:1407.4516 | [src: abstract] |

## Gas-mass fraction of relaxed clusters (a distance and Ω_m probe, not a growth probe)
<!-- key: gas-mass-fraction-of-relaxed-clusters-a -->

| Quantity | Value | Model | Data | Citation | Flag |
|---|---|---|---|---|---|
| Ω_m | 0.28 ± 0.06 | priors on H0 and Ω_b h² | 6 clusters at z < 0.15 out of 42 Chandra clusters (kT > 5 keV, 0.05 < z < 1.1) | Allen et al. 2008, arXiv:0706.0033 | [src: abstract] |
| Ω_de; w | 0.86 ± 0.21 (non-flat ΛCDM); −1.14 ± 0.31 (flat wCDM) | as stated | 42 clusters | arXiv:0706.0033 | [src: abstract] |
| h^{3/2} Ω_b/Ω_m | 0.089 ± 0.012 | insensitive to dark energy | lowest-redshift clusters among 40 relaxed Chandra clusters, lensing-calibrated | Mantz et al. 2014, arXiv:1402.6212 | [src: abstract] |
| Ω_m | 0.27 ± 0.04 | priors on h and Ω_b h² | same | arXiv:1402.6212 | [src: abstract] |
| Ω_Λ; w | 0.65 +0.17/−0.22 (non-flat ΛCDM); −0.98 ± 0.26 (flat wCDM) | as stated | 40 clusters to z > 1 | arXiv:1402.6212 | [src: abstract] |
| intrinsic scatter of f_gas | (7.4 ± 2.3)% in the shell 0.8–1.2 r2500 | — | same | arXiv:1402.6212 | [src: abstract] |
| h | 0.722 ± 0.067 | f_gas at z < 0.16 + CMB baryon fraction | updated sample (adds Perseus and two clusters at z > 0.97) | Mantz et al. 2022, arXiv:2111.09343 | [src: abstract] |
| Ω_Λ; w | 0.865 ± 0.119 (non-flat ΛCDM); −1.13 +0.17/−0.20 (flat wCDM) | priors on Ω_b h² and h | same | arXiv:2111.09343 | [src: abstract] |
| f_gas scatter in distance | 3% | — | same | arXiv:2111.09343 | [src] |
| lensing / X-ray hydrostatic mass at r2500 | 0.96 ± 9% (stat) ± 9% (sys) | fixed cosmology | relaxed clusters with WtG lensing | Applegate et al. 2016, arXiv:1509.02162 | [src: abstract] |

The f_gas method uses only the hottest, most relaxed clusters (57 of 361, 16%, pass the SPA morphology test of Mantz et al. 2015, arXiv:1502.06020 [src: abstract]) and measures in a shell around r2500, where the X-ray hydrostatic mass agrees with lensing. It is immune to most of the selection-function problems of count experiments and depends instead on the gas depletion factor from simulations.

## Hydrostatic bias: what simulations and X-ray data say
<!-- key: hydrostatic-bias-what-simulations-and-x-ray -->

| Statement | Value | Source | Flag |
|---|---|---|---|
| Median hydrostatic bias, fiducial FLAMINGO | b_HSE ≈ −0.1 at group scale to −0.2 at cluster scale (true mass), nearly independent of hydrostatic mass; scatter ≈ 0.1 at M500c ~ 1e14 M_sun | Braspenning et al. 2025, arXiv:2409.07849 | [src: abstract] |
| FLAMINGO, clusters with M500c > 7.5e14 M_sun, z = 0 | bias 0.22 ± 0.01 with X-ray spectroscopic-like temperatures; −0.05 ± 0.01 with SZ y-weighted temperatures; scatter ≈ 0.2 in the SZ case | Kay et al. 2024, arXiv:2404.08539 | [src: abstract] |
| X-COP, 12 nearby clusters, XMM + Planck | non-thermal pressure about 6% at R500 and 10% at R200; with the Planck mass calibration the universal gas fraction implies 1 − b = 0.85 ± 0.05; the bias required by Planck CMB + counts is "excluded at high significance, unless the most massive halos are missing a substantial fraction of their baryons" | Eckert et al. 2019, arXiv:1805.00034 | [src: abstract] |
| Planck-ESZ gas fractions | amplitude B ≈ 0.8 in all variants; a constant bias would require Ω_m > 0.849; 3.8σ evidence for redshift dependence with a Planck prior on Ω_m, but "entirely dependent on the cluster sample" | Wicker et al. 2023, arXiv:2204.12823 | [src: abstract] |

The tension in one sentence: X-COP gas fractions with the Planck mass calibration give 1 − b = 0.85 ± 0.05 (arXiv:1805.00034) and FLAMINGO a median b_HSE of about −0.1 to −0.2 (arXiv:2409.07849); lensing of SZ-selected samples gives 0.688 ± 0.072 (arXiv:1402.2670) and 0.76 ± 0.05 ± 0.06 (arXiv:1502.01883) for the XMM-calibrated Planck scale; the Planck primary CMB with the Planck cluster model needs 0.61 ± 0.03 (arXiv:2403.19542) [src: abstract of each]. Part of the gap between the first two is X-ray temperature calibration (Chandra versus XMM), which is not a departure from hydrostatic equilibrium at all (arXiv:2402.04006).

## Optically selected samples (redMaPPer richness)
<!-- key: optically-selected-samples-redmapper-richness -->

| Quantity | Value | Model | Data | Citation | Flag |
|---|---|---|---|---|---|
| S8 | 0.79 +0.05/−0.04 | flat ΛCDM with massive neutrinos, blind | SDSS redMaPPer, λ ≥ 20, 0.1 < z < 0.3, counts + stacked lensing | Costanzi et al. 2019, arXiv:1810.09456 | [src: abstract] |
| h | 0.66 ± 0.02 | same + BAO + BBN | same | arXiv:1810.09456 | [src: abstract] |
| S8; Ω_m | **0.65 ± 0.04; 0.179 +0.031/−0.038** — 2.4σ from DES Y1 3×2pt, 5.6σ from Planck; attributed by the authors to systematics | flat ΛCDM, blind, with post-unblinding changes | DES Y1 redMaPPer counts + stacked lensing | DES Collaboration 2020, arXiv:2002.11124 | [src: abstract] |
| Ω_m; σ8 | 0.305 +0.055/−0.038; 0.783 +0.064/−0.054 | flat νΛCDM | DES Y1 cluster abundances + three cluster cross-correlations + galaxy auto-correlation (large scales only) | To et al. 2021, arXiv:2010.01138 | [src: abstract] |
| S8 | 0.718 +0.024/−0.021, "clearly inconsistent with other CMB/LSS based cosmology results" | flat ΛCDM, forward model with anisotropic boosts | SDSS redMaPPer abundance + lensing + clustering | Park et al. 2023, arXiv:2112.09059 | [src: abstract] |
| S8 | 0.816 +0.041/−0.039 | flat ΛCDM, blind, same forward model | SDSS redMaPPer + HSC Y3 lensing | Sunayama et al. 2024, arXiv:2309.13025 | [src: abstract] |
| S8; Ω_m | 0.864 ± 0.035; 0.265 +0.019/−0.031 | ΛCDM | DES Y3: about 16000 redMaPPer clusters over nearly 5000 deg², cluster-based data vector | DES Collaboration 2025, arXiv:2503.13632 | [src: abstract] |
| S8; Ω_m | 0.811 +0.022/−0.020; 0.294 +0.022/−0.033; PTE 0.6 against Planck; 24% gain in the Ω_m–S8 figure of merit over 3×2pt alone | ΛCDM | DES Y3 clusters + 3×2pt | arXiv:2503.13632 | [src: abstract] |
| Σm_ν | < 0.26 eV (95%) | νΛCDM | DES 3×2pt + DES clusters + Planck | arXiv:2503.13632 | [src: abstract] |
| Ω_m; σ8 | 0.254 +0.026/−0.020; 0.826 +0.030/−0.034; 2.58σ from Planck | flat ΛCDM, simulation-based forward model with counts-in-cylinders selection, miscentring and baryons | DES Y1 redMaPPer abundance + lensing | Salcedo et al. 2025, arXiv:2510.25706 | [src: abstract] |

### The DES Y1 lesson
<!-- key: the-des-y1-lesson -->

The DES Y1 cluster analysis was blind, internally consistent, and wrong: S8 = 0.65 ± 0.04 and Ω_m = 0.179 [src, arXiv:2002.11124]. What the collaboration and later work established: [src: abstract]

1. The discrepancy "resides in our modeling of the weak lensing signal rather than the cluster abundance"; repeating with λ ≥ 30 "significantly reduces the tension" [src: abstract, arXiv:2002.11124].
2. With the richness–mass relation calibrated on SPT multi-wavelength data instead of stacked lensing, DES Y1 counts give cosmology consistent with SPT and other probes, and the model with projection effects (PRJ) is preferred over the background-only one [src, Costanzi et al. 2021, arXiv:2010.13800].
3. SPT-SZ confirms 207 of 1005 redMaPPer clusters at λ > 40, fewer than expected at low richness; the unconfirmed population ("contaminants", groups of 3–5e13 M_sun) is > 12% at λ = 40 and extrapolates to > 22% at λ = 20 (97.5 percentile limits) [src, Grandis et al. 2021, arXiv:2101.04984]. The same paper finds a richness–mass slope B ≈ 1 against B ≈ 0.75 from purely optical calibration. [src: abstract]
4. Spectroscopy of SDSS redMaPPer shows projection effects contribute about 16% of the weighted richness for the lowest-richness clusters, with a steeper richness dependence than the models then in use [src: abstract, Myles et al. 2021, arXiv:2011.07070].
5. The same DES Y1 data reanalysed in 2025 with a simulation-based forward model of the optical selection give Ω_m = 0.254, σ8 = 0.826 [src, arXiv:2510.25706]. [src: abstract]
6. DES Y3 × SPT cross-matching rules out significant contamination by unvirialised objects at the high-richness end, shows that a simple lognormal scatter is inadequate, and finds redshift trends that the projection-effect simulations do not capture [src, Grandis et al. 2025, arXiv:2502.12914].

The mechanism: a richness-selected sample preferentially contains haloes embedded in line-of-sight structure (filaments, aligned triaxial haloes). Stacked lensing and clustering of such a sample are boosted anisotropically on large scales relative to a mass-selected sample of the same mean mass, so that the standard isotropic model infers the wrong mass.

## KiDS (AMICO), HSC, XXL, UNIONS
<!-- key: kids-amico-hsc-xxl-unions -->

| Quantity | Value | Model | Data | Citation | Flag |
|---|---|---|---|---|---|
| Ω_m; σ8; S8 | 0.22 ± 0.02; 0.86 ± 0.03; **0.74 ± 0.03**, 2.8σ from Planck | flat ΛCDM, blinded through the sample completeness | about 8000 AMICO clusters in KiDS-1000, 839 deg², z < 0.8, counts + stacked lensing | Lesci et al. 2025, arXiv:2507.14285 | [src: abstract] |
| mass precision; intrinsic scatter of log λ*–log M200 | 8% on average; 0.05 ± 0.02 | same | same | arXiv:2507.14285 | [src: App. B] |
| Ω_m; σ8; S8 | 0.24 ± 0.02; 0.86 +0.13/−0.10; 0.77 +0.10/−0.08, 1σ agreement with the KiDS-1000 AMICO counts; 2σ tension in Ω_m with Planck 2018 | ΛCDM, Gaussian priors on the mass–richness relation from the counts + lensing analysis, uniform cosmological priors | multipoles of the 3D two-point correlation function, 5–150 Mpc/h, of 9049 AMICO KiDS-1000 clusters at S/N ≥ 3.5, 0.1 ≤ z < 0.8, 838.78 deg² | Romanello et al. 2026, arXiv:2610.31767 | [src: abstract; Sect. 5] |
| Ω_m; σ8; σ8 (Ω_m/0.3)^0.25; σ8 (Ω_m/0.3)^0.5 | 0.50 +0.28/−0.24; 0.685 +0.161/−0.088; 0.835 +0.041/−0.044; 0.993 +0.084/−0.126 | flat ΛCDM, blind | 129 shear-selected clusters at ν ≥ 4.7 in HSC Y3 mass maps, about 500 deg², z ≲ 0.7 | Chiu et al. 2024, arXiv:2406.11970 | [src: abstract] |
| S8 | 0.867 ± 0.063, plus 3% systematic from neural-network stochasticity | ΛCDM, simulation-based inference (DELFI), 12 parameters | 171 XXL C1 clusters; HSC Y3 lensing for 86 | Tam et al. 2026, arXiv:2602.11989 | [src: abstract] |
| Ω_m; σ8 | 0.34 ± 0.06; 0.77 ± 0.04 | comparison of the mean infall-region lensing profile with a simulation suite | DESI Legacy Imaging Survey clusters with a preliminary UNIONS shape catalogue | Mpetha et al. 2025, arXiv:2501.09147 | [src: abstract] |

The HSC shear-selected sample is the only one whose selection "solely depends on gravity" [src: abstract, arXiv:2406.11970]; its statistical power is still low (129 clusters), and the best-constrained combination is the one with exponent 0.25, not S8.


## Mass-calibration and profile measurements used as inputs
<!-- key: mass-calibration-and-profile-measurements-used -->

| Quantity | Value | Data | Citation | Flag |
|---|---|---|---|---|
| Richness–mass normalisation M0 at λ = 40, z = 0.35 (M200m) | [3.081 ± 0.075 (stat) ± 0.133 (sys)] × 1e14 M_sun, 5.0% in total | DES Y1 redMaPPer, stacked lensing in 4 × 3 bins, λ ≥ 20, 0.2 ≤ z ≤ 0.65 | McClintock et al. 2019, arXiv:1805.00039 | [src: abstract] |
| Richness slope F; redshift slope G | 1.356 ± 0.051 ± 0.008; −0.30 ± 0.30 ± 0.06 | same | arXiv:1805.00039 | [src: abstract] |
| Richness–mass slope from SZ cross-calibration | B ≈ 1, against B ≈ 0.75 from optical-only calibration | DES Y1 redMaPPer × SPT-SZ | arXiv:2101.04984 | [src: abstract] |
| Fraction of well-centred redMaPPer clusters | 75 ± 8 % | DES Y1 redMaPPer with archival X-ray centres | Zhang et al. 2019, arXiv:1901.07119 | [src: abstract] |
| Weak-lensing mass bias and scatter of NFW fits | bias 5–10%; scatter about 20% (clusters) to 30% (groups) | about 1e4 haloes, 1 Gpc/h N-body box | Becker & Kravtsov 2011, arXiv:1011.1681 | [src: abstract] |
| Splashback radius, optical selection | smaller than N-body expectation; assembly bias detected at 6.6σ | SDSS redMaPPer × photometric galaxies | More et al. 2016, arXiv:1601.06063 | [src: abstract] |
| Splashback radius, SZ selection | consistent with simulations; redMaPPer about 2σ low in the same analysis | SPT-SZ and ACTPol clusters × DES Y3 galaxies | Shin et al. 2019, arXiv:1811.06081 | [src] |
| Splashback radius, lensing and cluster–galaxy correlation | consistent with ΛCDM; precision 14% (shear) and 10% (w_cg) per stack | 9049 AMICO KiDS-1000 clusters, 0.1 < z < 0.8, M200m in [0.4, 20] × 1e14 M_sun/h | Lesci et al. 2026, arXiv:2602.07114 | [src: abstract] |

## History of the cluster amplitude
<!-- key: history-of-the-cluster-amplitude -->

The table lists the amplitude each analysis quoted, in order of arXiv posting, so that a value met in a manuscript can be dated. The exponent of the combination changes from row to row; do not difference the rows.

| Year | Sample | Quoted amplitude | Status today | Citation | Flag |
|---|---|---|---|---|---|
| 2009 | 238 RASS clusters | σ8 = 0.82 ± 0.05, Ω_m = 0.23 ± 0.04 (flat wCDM) | superseded by the 2014 lensing-calibrated analysis | arXiv:0909.3098 | [src: abstract] |
| 2013 | 15 + 7 ACT clusters + WMAP7 | σ8 = 0.829 ± 0.024 | still the only ACT counts cosmology | arXiv:1301.0816 | [src: abstract] |
| 2013 | Planck PSZ1, 189 clusters | σ8 (Ω_m/0.27)^0.3 = 0.764 ± 0.025; σ8 = 0.75 ± 0.03 | superseded; start of the "Planck cluster tension" | arXiv:1303.5080 | [src: abstract] |
| 2014 | RASS + Weighing the Giants | σ8 (Ω_m/0.3)^0.17 = 0.81 ± 0.03; σ8 = 0.83 ± 0.04 | first lensing-calibrated X-ray counts | arXiv:1407.4516 | [src: abstract] |
| 2015 | Planck PSZ2, 439 clusters | tension with the CMB from just over 1σ to 3.7σ, by (1 − b) prior | superseded by lensing-calibrated reanalyses | arXiv:1502.01597 | [src: abstract] |
| 2018 | SDSS redMaPPer | S8 = 0.79 +0.05/−0.04 | superseded by the 2021 and 2023 reanalyses | arXiv:1810.09456 | [src: abstract] |
| 2018 | SPT-SZ, 343 clusters | σ8 (Ω_m/0.3)^0.2 = 0.766 ± 0.025; σ8 = 0.781 ± 0.037 | superseded by SPT 2024 | arXiv:1812.01679 | [src: abstract] |
| 2019 | Planck MMF3 + CMB lensing | σ8 (Ω_m/0.33)^0.25 = 0.765 ± 0.035 | first Planck counts without a hydrostatic prior | arXiv:1904.07887 | [src: abstract] |
| 2020 | DES Y1 redMaPPer | S8 = 0.65 ± 0.04 | **withdrawn in effect**: attributed to lensing-model systematics | arXiv:2002.11124 | [src: abstract] |
| 2020 | DES Y1 abundances + correlations | σ8 = 0.783 +0.064/−0.054, Ω_m = 0.305 +0.055/−0.038 | superseded by DES Y3 | arXiv:2010.01138 | [src: abstract] |
| 2021 | SDSS redMaPPer, anisotropic boosts | S8 = 0.718 +0.024/−0.021 | superseded by the HSC-lensing version | arXiv:2112.09059 | [src: abstract] |
| 2023 | SDSS redMaPPer + HSC Y3 | S8 = 0.816 +0.041/−0.039 | current for SDSS | arXiv:2309.13025 | [src: abstract] |
| 2023 | AMICO KiDS-DR3, 5162 clusters, angular clustering | Ω_m = 0.32 +0.05/−0.04, σ8 = 0.77 +0.13/−0.09, S8 = 0.80 +0.08/−0.06 (correlation function); Ω_m = 0.24 +0.05/−0.04, S8 = 0.93 +0.11/−0.12 (power spectrum) | superseded by the KiDS-1000 clustering analysis (arXiv:2610.31767) | Romanello et al. 2024, arXiv:2310.12224 | [src: abstract] |
| 2024 | SPT 1005 clusters | S8 = 0.795 ± 0.029; σ8 (Ω_m/0.3)^0.25 = 0.805 ± 0.016 | current for SPT | arXiv:2401.02075 | [src: abstract] |
| 2024 | eRASS1 | S8 = 0.86 ± 0.01 | current for eROSITA | arXiv:2402.08458 | [src: abstract] |
| 2024 | Planck + Chandra | S8 = 0.78 ± 0.02, or 0.81 ± 0.02 with fitted evolution | superseded by the DES-shear version | arXiv:2402.04006 | [src: abstract] |
| 2024 | HSC shear-selected | σ8 (Ω_m/0.3)^0.25 = 0.835 +0.041/−0.044 | current | arXiv:2406.11970 | [src: abstract] |
| 2024 | SPT clusters + DES Y3 3×2pt | S8 = 0.796 ± 0.013 | current joint value | arXiv:2412.07765 | [src: abstract] |
| 2025 | DES Y3 redMaPPer | S8 = 0.864 ± 0.035; 0.811 +0.022/−0.020 with 3×2pt | current for DES | arXiv:2503.13632 | [src: abstract] |
| 2025 | KiDS-1000 AMICO | S8 = 0.74 ± 0.03 | current for KiDS | arXiv:2507.14285 | [src: abstract] |
| 2025 | Planck PSZ2 + DES + Chandra | S8 = 0.791 +0.023/−0.021 (constant bias); 0.814 +0.019/−0.020 (mass-dependent) | current for Planck | arXiv:2509.02068 | [src: abstract] |
| 2025 | DES Y1, simulation-based forward model | σ8 = 0.826 +0.030/−0.034, Ω_m = 0.254 +0.026/−0.020 | reanalysis of the 2020 data | arXiv:2510.25706 | [src: abstract] |
| 2026 | XXL C1 + HSC Y3 | S8 = 0.867 ± 0.063 | current for XXL | arXiv:2602.11989 | [src: abstract] |
| 2026 | AMICO KiDS-1000, 9049 clusters, 3D clustering | S8 = 0.77 +0.10/−0.08, σ8 = 0.86 +0.13/−0.10, Ω_m = 0.24 ± 0.02 | current for cluster clustering in KiDS | arXiv:2610.31767 | [src: abstract] |

The value S8 = 0.831 ± 0.020 of arXiv:2111.07491 combines SPT-SZ clusters with the Planck power spectra and is not a cluster-only number. [src: abstract]

Three patterns in the history. First, the optical samples moved upward when the lensing data or the selection model changed: SDSS from 0.718 (arXiv:2112.09059) to 0.816 (arXiv:2309.13025), DES from 0.65 (arXiv:2002.11124) to 0.864 (arXiv:2503.13632); for Planck the quoted difference from the CMB went from as much as 3.7σ (arXiv:1502.01597) to 1.6σ (arXiv:2509.02068) [src: abstract of each]. Second, the quoted errors did not shrink in proportion to sample size, because the mass calibration floor dominates.

Third, the two smallest errors today, those of eRASS1 and of SPT + DES 3×2pt in the tables above, belong to values that differ by several times either error [der: comparison of the two table rows].

## Agreement with the sibling skills
<!-- key: agreement-with-the-sibling-skills -->

- DES Y6 3×2pt gives S8 = 0.789 ± 0.012 (arXiv:2601.14559) and KiDS-Legacy cosmic shear 0.815 +0.016/−0.021 (arXiv:2503.19441) [src: abstract of each; the papers `cosmo-weak-lensing` cites]. The DES Y3 clusters + 3×2pt value above (0.811, arXiv:2503.13632) uses the Y3 3×2pt data, not Y6; no cluster analysis with DES Y6 lensing was found.
- The SPT + ACT + Planck primary CMB gives σ8 = 0.8137 ± 0.0037 [src: abstract, arXiv:2506.20707, the paper `cosmo-cmb` cites]. The tension statements in the tables above are those of the cluster papers, most of them relative to Planck 2018, and are not recomputed against the newer CMB combination.
- Neutrino-mass limits from clusters with the CMB (< 0.18 eV for SPT + Planck 2018, arXiv:2401.02075) are looser than the CMB + DESI BAO limits, for example < 0.0642 eV (95%, arXiv:2503.14744) and < 0.072 eV (95%, arXiv:2608.31136) [src: abstract of each; papers cited by `cosmo-cmb`]; they are independent of BAO, which is their value.

## Not verified
<!-- key: not-verified -->

- The σ8 or S8 of the 2009 Chandra Cluster Cosmology Project analysis (arXiv:0812.2720): only its dark-energy and neutrino results were read.
- Cosmology from the ACT DR5 or DR6 counts, from SPT-3G five-year counts, from DES Y6 clusters and from Euclid DR1: searched for, not found as of 2026-10-26.
- Results from the nDGP, interacting-dark-sector and ultralight-axion analyses of SPT and eRASS1 counts exist; they were removed from this file to keep the source list within its limit and belong to `cosmo-dark-energy-modified-gravity` and `cosmo-neutrinos-dark-matter`.
- The 2022 forward-model analysis of the XXL C1 sample, superseded here by the 2026 simulation-based analysis, is not listed.
- Stacked ACT × HSC Y3 lensing masses and the HSC lensing of eRASS1 clusters by a second team are not listed, for the same reason.
