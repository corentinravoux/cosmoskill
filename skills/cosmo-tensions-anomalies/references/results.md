# Tensions and anomalies — current sizes

Scope: one table per tension or anomaly: current size, data sets, metric, reference endpoint, what moved it and when.

Snapshot: 2026-10-07

Flags. `[src]`: read this session in the cited paper. `[sec: X]`: taken from the reference files of the sibling skill X, where the number is flagged `[src]` against the same arXiv ID; the sibling is the secondary source. `[der]`: derived here, derivation stated. Sibling abbreviations: `h0` = `cosmo-distance-ladder-h0`, `wl` = `cosmo-weak-lensing`, `cmb` = `cosmo-cmb`, `de` = `cosmo-dark-energy-modified-gravity`, `cl` = `cosmo-clusters`, `x` = `cosmo-cmb-lss-cross-correlations`, `nu` = `cosmo-neutrinos-dark-matter`, `pv` = `cosmo-peculiar-velocities`, `inf` = `cosmo-inflation-primordial`, `stat` = `cosmo-statistics-inference`, `b2p` = `cosmo-beyond-two-point`. Sections 1–6, 8 and 11 are a synthesis of those siblings; Sections 7, 9 and 10 were researched for this skill. H0 is in km/s/Mpc, the model is flat ΛCDM unless a row says otherwise, and S8 ≡ σ8 (Ω_m/0.3)^0.5.

A "Gaussian difference" below is n = |a − b| / sqrt(σ_a² + σ_b²) with asymmetric errors symmetrised and the two measurements taken as independent. It is the crudest tension metric (see `physics-and-methods.md` §1) and is given only so that every row of a table shares one definition.

## 0. Summary of sizes at the snapshot
<!-- key: summary-of-sizes-at-the-snapshot -->

| Tension or anomaly | Current size | Depends most on | Section |
|---|---|---|---|
| H0, ladder against early Universe | 4.4σ to 7.1σ for SH0ES and H0DN; 0.9σ to 1.8σ for CCHP | which local team and which early endpoint | 1 |
| S8, lensing against CMB | 0.7σ (KiDS-Legacy) to 2.6σ (DES Y6 3×2pt, projected on S8; 1.8σ in full space) | survey, metric, CMB reference | 2 |
| S8, spread among low-redshift probes | 0.72 to 0.86 between published values | probe and astrophysical model | 2 |
| A_L (peak smoothing) | 2.7σ in Planck PR3 Plik; ≤ 1σ in PR4 HiLLiPoP, ACT DR6, SPT-3G; about 2σ in CMB-SPA | Planck TT at ℓ ≈ 1100–2000 | 3 |
| τ, BAO-preferred against measured | 0.090 ± 0.012 against 0.051–0.063 | whether low-ℓ EE is dropped | 3 |
| CMB against DESI DR2 BAO in ΛCDM | 1.6σ to 3.7σ | CMB data set | 4 |
| w0wa preference | 1.7σ BAO alone; 3.1σ + CMB; 3.0σ to 3.4σ + SNe after recalibration | SN sample, CMB lensing, statistic | 5 |
| Effective neutrino mass below the oscillation minimum | 3σ in ΛCDM; absent in w0waCDM or with free lensing amplitudes | model, τ, lensing | 6 |
| Number-count dipole against the CMB kinematic expectation | 3.3σ to 5.7σ for CatWISE quasars depending on the null model (6.7σ with a forward-modelled Eddington bias); 5.4σ for three radio surveys; the DESI redshift dipole agrees with the CMB velocity | catalogue, null model, source evolution | 7 |
| CF4 bulk flow at 150–200 h⁻¹Mpc | 0.11% probability (mock errors); 2.3σ full range in a shell analysis | error model, window, 6dFGS | 8 |
| Large-angle CMB anomalies | individual p-values at the per mille to per cent level; a claimed joint ≤ 3 × 10⁻⁸ becomes 2σ to 3σ after a look-elsewhere correction; nothing in polarisation | choice and number of statistics, mask | 9 |
| JWST early-galaxy abundance | no spectroscopic sample above the ΛCDM baryon limit; two objects need about 50% efficiency [der: three in arXiv:2309.02492 minus the one revised in arXiv:2602.03030] | redshift method, stellar-mass systematics, star-formation efficiency | 10 |
| Curvature | −0.044 (Planck PR3 alone) and +0.0023 ± 0.0011 (DESI DR2 + CMB): opposite signs | same features as A_L and CMB–BAO | 11 |
| Isotropic birefringence | 0.277° ± 0.057°, 4.8σ, not claimed as a detection | absolute angle calibration | 11 |
| Parity-odd 4PCF | no detection | mocks, 8PCF bias | 11 |

## 1. H0 tension
<!-- key: h0-tension -->

### 1.1 The two sides
<!-- key: the-two-sides -->

| Side | Value | Data | Citation | Flag |
|---|---|---|---|---|
| Local | 73.50 ± 0.81 | H0 Distance Network baseline (Gaia, DEBs, NGC 4258; Cepheids + TRGB; SN Ia, SBF, masers) | H0DN Collaboration 2025, arXiv:2510.23823 | [sec: h0] |
| Local | 73.18 ± 0.88 | SH0ES: HST + JWST Cepheids + 35 TRGB calibrations, 55 SN Ia calibrators | Riess et al. 2025, arXiv:2509.01667 | [sec: h0] |
| Local | 73.04 ± 1.04 | SH0ES HST-only baseline, 42 calibrators | Riess et al. 2022, arXiv:2112.04510 | [sec: h0] |
| Local | 70.39 ± 1.22 (stat) ± 1.33 (sys) ± 0.70 (σ_SN); total 1.94 [der, quadrature] | CCHP TRGB, 24 SN Ia calibrators, anchor NGC 4258 | Freedman et al. 2024, arXiv:2408.06153 | [sec: h0] |
| Local, one-step | 71.6 (+3.9/−3.3) | TDCOSMO-2025, 8 lensed quasars, mass-sheet degeneracy free | TDCOSMO Collaboration 2025, arXiv:2506.03023 | [sec: h0] |
| Early | 67.4 ± 0.5 | Planck 2018 TT,TE,EE + lowE + lensing | Planck Collaboration 2018, arXiv:1807.06209 | [sec: h0] |
| Early | 67.64 ± 0.52 | Planck PR4 HiLLiPoP + LoLLiPoP | Tristram et al. 2023, arXiv:2309.10034 | [sec: cmb] |
| Early | 66.66 ± 0.60 | SPT-3G D1 TT/TE/EE + lensing | Camphuis et al. 2025, arXiv:2506.20707 | [sec: h0, cmb] |
| Early | 67.19 ± 0.38 | CMB-SPA (SPT + ACT + Planck), second arXiv version | arXiv:2506.20707 | [sec: cmb] |
| Early | 67.62 ± 0.50 | P-ACT | Louis et al. 2025, arXiv:2503.14452 | [sec: cmb] |
| Early, no CMB anisotropies | 68.51 ± 0.58 | DESI DR2 BAO + BBN | DESI Collaboration 2025, arXiv:2503.14738 | [sec: h0] |
| Early + BAO | 68.43 ± 0.27 | P-ACT + CMB lensing + DESI DR2 BAO | arXiv:2503.14452 | [sec: cmb] |

### 1.2 Size, one definition for every cell
<!-- key: size-one-definition-for-every-cell -->

Gaussian difference [sec: h0, `results.md` §5, where the table is flagged `[der]`]:

| Local value | vs Planck 2018 | vs SPT-3G D1 | vs CMB-SPA | vs DESI DR2 + BBN |
|---|---|---|---|---|
| SH0ES 2022, 73.04 ± 1.04 | 4.9 | 5.3 | 5.3 | 3.8 |
| SH0ES 2025, 73.18 ± 0.88 | 5.7 | 6.1 | 6.2 | 4.4 |
| H0DN 2025, 73.50 ± 0.81 | 6.4 | 6.8 | 7.1 | 5.0 |
| CCHP TRGB, 70.39 ± 1.94 | 1.5 | 1.8 | 1.6 | 0.9 |
| TDCOSMO-2025, 71.6 ± 3.6 | 1.2 | 1.4 | 1.2 | 0.8 |

Significances the papers themselves print [sec: h0]: 5.0σ for SH0ES 2022 against Planck, computed as 0.176 ± 0.035 mag in 5 log H0 (arXiv:2112.04510); 7.1σ against Planck + SPT + ACT and 5.0σ against BBN + DESI DR2 BAO for H0DN (arXiv:2510.23823); 6.2σ for SPT-3G alone and 6.4σ for CMB-SPA against SH0ES (arXiv:2506.20707); 4.5σ between DESI + BBN and SH0ES "independent of the CMB" (arXiv:2503.14738).

The H0DN paper adopts 67.24 ± 0.35 for Planck + SPT + ACT, which is the first arXiv version of the CMB-SPA value; the second version reads 67.19 ± 0.38 [sec: cmb]. Both give 7.1σ against 73.50 ± 0.81 [der: (73.50 − 67.24) / sqrt(0.81² + 0.35²) = 7.09; (73.50 − 67.19) / sqrt(0.81² + 0.38²) = 7.05].

### 1.3 What moved it and when
<!-- key: what-moved-it-and-when-3 -->

| When | What changed | Effect on the tension | Citation | Flag |
|---|---|---|---|---|
| 2022 | SH0ES 42 calibrators, Pantheon+, full covariance | 5.0σ against Planck 2018 | arXiv:2112.04510 | [sec: h0] |
| 2024 | JWST CCHP ladder: TRGB 70.39 with total error 1.94 | a local value within 2σ of the CMB, from a subsample of calibrators | arXiv:2408.06153 | [sec: h0] |
| 2025 | SH0ES + JWST Cepheids in 19 hosts + 35 TRGB | 73.18 ± 0.88; "~6σ" | arXiv:2509.01667 | [sec: h0] |
| 2025 | SPT-3G D1 and ACT DR6: ground-based CMB as tight as Planck and lower in H0 | early endpoint moves down and tightens: 67.4 ± 0.5 to 67.19 ± 0.38 | arXiv:2506.20707, arXiv:2503.14452 | [sec: cmb] |
| 2025 | DESI DR2 BAO + BBN | 4.5σ from SH0ES with no CMB anisotropy data | arXiv:2503.14738 | [sec: h0] |
| 2025 | TDCOSMO with the mass-sheet degeneracy free | lensing no longer sides with the ladder at high precision: 71.6 (+3.9/−3.3) | arXiv:2506.03023 | [sec: h0] |
| 2025 | H0DN community combination | 73.50 ± 0.81, the highest quoted significance (7.1σ) | arXiv:2510.23823 | [sec: h0] |
| 2026 | Statistical reanalyses of the SH0ES likelihood | 70.6 ± 1.0 with volume priors and no selection term; SH0ES calibration recovered within 0.5σ once Milky Way selection is modelled | Högås & Mörtsell 2026, arXiv:2601.22215; Stiskalek et al. 2026, arXiv:2603.09880 | [sec: h0] |

The central local value has stayed between 73.0 and 74.0 since 2016 while its error halved [sec: h0]; the growth of the significance from 5σ to 7σ is shared between the smaller local error and the tighter, lower CMB endpoint.

## 2. S8 tension
<!-- key: s8-tension -->

### 2.1 Reference endpoints in use
<!-- key: reference-endpoints-in-use -->

| Endpoint | Value | Source | Flag |
|---|---|---|---|
| Planck PR3, as quoted by the PR4 paper | S8 = 0.834 ± 0.016 | arXiv:2309.10034 | [sec: cmb] |
| Planck PR4 HiLLiPoP + LoLLiPoP | S8 = 0.819 ± 0.014 | arXiv:2309.10034 | [sec: cmb] |
| P-ACT | S8 = 0.830 ± 0.014 | arXiv:2503.14452 | [sec: cmb] |
| "Combined CMB" (Planck + ACT DR6 + SPT-3G) | S8 = 0.836 (+0.012/−0.013) | Pantos & Perivolaropoulos 2026, arXiv:2602.12238 (review abstract) | [sec: wl] |
| CMB-SPA | σ8 = 0.8137 ± 0.0037, Ω_m = 0.3175 ± 0.0055 | arXiv:2506.20707 | [sec: cmb] |

The four S8 endpoints span 0.819 to 0.836, a range larger than the error of the best lensing measurement (0.012). A quoted "tension with the CMB" is not comparable between papers unless the endpoint is the same: KiDS-Legacy compares with Planck alone, DES Y6 with Planck 2018 + ACT DR6 + SPT-3G DR1 [sec: wl].

### 2.2 S8 by probe, with one common derived difference
<!-- key: s8-by-probe-with-one-common-derived-difference -->

Columns "vs 0.836" and "vs 0.819" are Gaussian differences [der] against the combined-CMB endpoint (error 0.0125) and the Planck PR4 endpoint (error 0.014). A leading "+" means the probe lies above the endpoint.

| Probe | S8 | Tension as printed by the paper | vs 0.836 | vs 0.819 | Citation | Flag |
|---|---|---|---|---|---|---|
| KiDS-Legacy cosmic shear | 0.815 (+0.016/−0.021) | 0.73σ from Planck Legacy | 0.9 | 0.2 | Wright et al. 2025, arXiv:2503.19441 | [sec: wl] |
| DES Y6 cosmic shear, NLA | 0.798 (+0.014/−0.015) | 2.0σ in S8, 1.1σ full space | 2.0 | 1.0 | DES Collaboration 2026, arXiv:2602.10065 | [sec: wl] |
| DES Y6 cosmic shear, TATT | 0.783 (+0.019/−0.015) | 2.3σ in S8, 1.7σ full space | 2.5 | 1.6 | arXiv:2602.10065 | [sec: wl] |
| DES Y6 3×2pt | 0.789 ± 0.012 | 2.6σ in S8, 1.8σ full space | 2.7 | 1.6 | DES Collaboration 2026, arXiv:2601.14559 | [sec: wl] |
| HSC Y3 shear, DESI clustering redshifts | 0.804 (+0.019/−0.018) | "towards Planck" | 1.4 | 0.6 | Choppin de Janvry et al. 2025, arXiv:2511.18134 | [sec: wl] |
| DES Y3 shear, external IA and baryon calibration | 0.832 (+0.013/−0.017) | posterior moves up by 1.5σ | 0.2 | +0.6 | Bigwood et al. 2025, arXiv:2512.04209 | [sec: wl] |
| unWISE × ACT DR6 + Planck lensing | 0.810 ± 0.015 | consistent with the primary CMB | 1.3 | 0.4 | Farren et al. 2023, arXiv:2309.05659 | [sec: x] |
| DESI LRG × ACT DR6 + Planck PR4 lensing | 0.775 (+0.019/−0.022) | 1.6–2.2σ low | 2.5 | 1.8 | Sailer et al. 2024, arXiv:2407.04607 | [sec: x] |
| tSZ × galaxies, compiled ⟨b P_e⟩(z), FLAMINGO model | 0.72 ± 0.03 | — | 3.6 | 3.0 | Salcido et al. 2026, arXiv:2605.11083 | [sec: x] |
| eRASS1 cluster counts | 0.86 ± 0.01 | at the Planck level | +1.5 | +2.4 | Ghirardini et al. 2024, arXiv:2402.08458 | [sec: cl] |
| SPT clusters + DES and HST lensing | 0.795 ± 0.029 | 1.1σ from Planck 2018 | 1.3 | 0.7 | Bocquet et al. 2024, arXiv:2401.02075 | [sec: cl] |
| Planck PSZ2 + DES shear + Chandra | 0.791 (+0.023/−0.021) | 1.6σ from the CMB | 1.8 | 1.1 | Aymerich et al. 2025, arXiv:2509.02068 | [sec: cl] |
| KiDS-1000 AMICO clusters | 0.74 ± 0.03 | 2.8σ from Planck | 3.0 | 2.4 | Lesci et al. 2025, arXiv:2507.14285 | [sec: cl] |

Derivation check on the DES rows: the paper's own 2.0σ and 2.6σ are reproduced to 0.1σ by the Gaussian difference against 0.836, which confirms that DES Y6 uses a three-experiment CMB endpoint near that value [der].

Further values held by siblings and not repeated with their IDs here: DES Y3 redMaPPer clusters 0.864 ± 0.035 and XXL 0.867 ± 0.063 (`cosmo-clusters`); DES Y3 shear × tSZ 0.811 (+0.015/−0.012), DESI DR1 quasars × Planck lensing 0.922 (+0.059/−0.073) (`cosmo-cmb-lss-cross-correlations`); third-order shear 0.806 (KiDS-Legacy), 0.780 (DES Y3), 0.736 ± 0.020 (HSC Y3 with the original redshift calibration) (`cosmo-beyond-two-point`, `cosmo-weak-lensing`); DESI DR1 full shape σ8 = 0.842 ± 0.034 against BOSS EFT 0.69–0.73 (`cosmo-galaxy-clustering`); TF + SN velocities S8 = 0.798 ± 0.035 (`cosmo-peculiar-velocities`) [all sec].

### 2.3 The internal spread is larger than the CMB tension
<!-- key: the-internal-spread-is-larger-than-the-cmb -->

| Pair | Gaussian difference | Flag |
|---|---|---|
| eRASS1 clusters (0.86 ± 0.01) against DES Y6 3×2pt (0.789 ± 0.012) | 4.5σ | [der: 0.071 / sqrt(0.01² + 0.012²)] |
| eRASS1 clusters against KiDS AMICO clusters (0.74 ± 0.03) | 3.8σ | [der: 0.12 / sqrt(0.01² + 0.03²)] |
| eRASS1 clusters against tSZ × galaxies (0.72 ± 0.03) | 4.4σ | [der: 0.14 / sqrt(0.01² + 0.03²)] |
| DES Y6 3×2pt against KiDS-Legacy shear (0.815, error 0.0185) | 1.2σ | [der: 0.026 / sqrt(0.012² + 0.0185²)] |

No low-redshift probe is more than 3σ from the CMB except the tSZ cross-correlation and the KiDS cluster counts, while two cluster samples differ from each other by almost 4σ. "The S8 tension" in 2026 is therefore better described as a disagreement among low-redshift amplitude measurements with strong astrophysical modelling, in which cosmic shear has moved to within 1σ to 2.6σ of the CMB.

### 2.4 What moved it and when
<!-- key: what-moved-it-and-when-2 -->

| When | What changed | Effect | Citation | Flag |
|---|---|---|---|---|
| 2020–2021 | KiDS-1000 (0.759) and DES Y3 (0.759 fiducial) | the "2–3σ low" era | values in `cosmo-weak-lensing` `results.md` §3 | [sec: wl] |
| 2023 | Planck PR4 | Planck S8 falls from 0.834 ± 0.016 to 0.819 ± 0.014 | arXiv:2309.10034 | [sec: cmb] |
| 2023–2024 | CMB-lensing tomography corrected (lensing normalisation, redshifts, neutrino consistency, projection effect) | unWISE 0.784 to 0.810; DESI LRG 0.73 to 0.775 | arXiv:2309.05659, arXiv:2407.04607 | [sec: x] |
| 2025 | KiDS-Legacy: new redshift calibration | 0.759 to 0.815, +0.056 [der, sec: wl] | arXiv:2503.19441 | [sec: wl] |
| 2025 | HSC Y3 with DESI clustering redshifts | 0.769 to 0.804 | arXiv:2511.18134 | [sec: wl] |
| 2025 | Planck clusters with DES shear mass calibration | 3.7σ (2015, top of a prior-dependent range) to 1.6σ | arXiv:2509.02068 | [sec: cl] |
| 2026 | DES Y6 | shear 0.798 (NLA); 3×2pt 0.789 ± 0.012; the tightest lensing result remains 2.6σ low in S8 | arXiv:2602.10065, arXiv:2601.14559 | [sec: wl] |

## 3. CMB lensing anomaly A_L and optical depth
<!-- key: cmb-lensing-anomaly-al-and-optical-depth -->

### 3.1 Peak-smoothing amplitude
<!-- key: peak-smoothing-amplitude -->

All rows [sec: cmb, `results.md` §3]. Model: ΛCDM + A_L.

| Value | Data | Distance from 1 | Citation |
|---|---|---|---|
| 1.180 ± 0.065 | Planck PR3 Plik TT,TE,EE + lowE | 2.7σ (paper) | arXiv:1807.06209 |
| 1.039 ± 0.052 | Planck PR4 HiLLiPoP | 0.75σ [der] | arXiv:2309.10034 |
| 1.007 ± 0.057 | ACT DR6 | 0.1σ [der] | arXiv:2503.14452 |
| 1.081 ± 0.043 | P-ACT | 1.9σ [der, sec: cmb] | arXiv:2503.14452 |
| 0.972 (+0.079/−0.089) | SPT-3G D1 | 0.3σ below [der] | arXiv:2506.20707 |
| 1.016 (+0.048/−0.054) | SPT + ACT, T and E spectra | 0.3σ [der] | arXiv:2506.20707 |
| A_2pt = 1.079 ± 0.038 | CMB-SPA | 2.1σ [der, sec: cmb] | arXiv:2506.20707 |

Lensing reconstructions show no excess: ACT DR6 + SPT-3G + Planck PR4 give a reconstruction amplitude 1.025 ± 0.017 relative to the P-ACT best fit (Qu et al. 2025; ID in `cosmo-cmb` `results.md` §4), and the SPT-3G D1 quadratic-estimator amplitude is unity at 2% (Omori et al. 2026, arXiv:2608.31136) [sec: cmb]. Motloch & Hu 2019 (arXiv:1912.06601) quantified the Planck legacy smoothing as 2σ high relative to the lensing reconstruction and 2.8σ high relative to the ΛCDM expectation from the unlensed information [sec: cmb].

What moved it: PR4 reprocessing and likelihoods (2022–2023), then ACT DR6 and SPT-3G D1 (2025), which do not show the oscillatory TT residual at 1000 < ℓ < 2000 that drives the Planck value [sec: cmb]. It survives at about 2σ only in combinations that keep the full Planck TT range.

### 3.2 Optical depth
<!-- key: optical-depth -->

All rows [sec: cmb, `results.md` §5 and `open-questions.md` §1].

| τ | Data | Citation |
|---|---|---|
| 0.054 ± 0.007 | Planck 2018 | arXiv:1807.06209 |
| 0.058 ± 0.006 | Planck PR4 LoLLiPoP + HiLLiPoP | arXiv:2309.10034 |
| 0.053 (+0.018/−0.019) | CLASS 90 GHz × Planck, ground-based | Li et al. 2025; ID and detail in `cosmo-cmb` `results.md` §5 |
| 0.090 ± 0.012 | DESI BAO + high-ℓ CMB + CMB lensing, no low-ℓ EE | Sailer et al. 2025, arXiv:2504.16932 |
| 0.091 ± 0.011 | CMB without low-ℓ EE and lensing constraints, Σm_ν = 0.06 eV | Jhaveri et al. 2025, arXiv:2504.21813 |
| 0.0552 (+0.0019/−0.0026 stat) (+0.0075/−0.0049 sys) | Planck without low-ℓ EE + reionisation history from Lyα forest and damping wings | Kageura et al. 2026, arXiv:2601.09644 |

Size: the BAO-preferred value is "3–5σ" from Planck low-ℓ polarisation according to arXiv:2504.16932 [sec: cmb]; against PR4, (0.090 − 0.058) / sqrt(0.012² + 0.006²) = 2.4σ [der]. Every Planck reprocessing from 2018 to 2023 lies in 0.051–0.063 with errors near 0.006 [sec: cmb]. The τ question is not an anomaly in a measurement; it is the statement that one parameter, measured by one instrument, would absorb the CMB–BAO mismatch if it were wrong by about 0.03.

## 4. CMB-DESI discrepancy within LCDM
<!-- key: cmb-desi-discrepancy-within-lcdm -->

All rows [sec: cmb, `results.md` §2]. The compared data are DESI DR2 BAO and the named CMB data, in ΛCDM.

| CMB data | Distance from DESI DR2 | Subspace | Citation |
|---|---|---|---|
| P-ACT | 1.6σ | — | arXiv:2503.14452 |
| DESI's own CMB combination | 2.3σ | — | arXiv:2503.14738 |
| CMB as summarised by Sailer et al. | 2.2σ | — | arXiv:2504.16932 |
| CMB-SPA | 2.8σ | Ω_m–h r_d plane | arXiv:2506.20707 |
| SPT + Planck | 3.0σ | same | arXiv:2506.20707 |
| SPT + ACT | 3.7σ | same | arXiv:2506.20707 |

In parameters: DESI BAO alone give Ω_m = 0.2975 ± 0.0086 and h r_d = 101.54 ± 0.73 Mpc [sec: h0]; the CMB gives Ω_m = 0.3145 ± 0.0067 (Planck, SPT rerun), 0.3246 ± 0.0091 (SPT-3G D1), 0.330 ± 0.010 (ACT DR6, SPT rerun) and 0.3175 ± 0.0055 (CMB-SPA) [sec: cmb]. The ground-based experiments prefer a higher Ω_m than Planck, which is why the discrepancy is larger without Planck.

The same mismatch is what four different extensions absorb (Sections 3.2, 5, 6 and 11): a higher τ, evolving dark energy, a negative effective neutrino mass, or positive Ω_K. They are four readings of one discrepancy, not four anomalies; see `open-questions.md` §1.

What moved it: DESI DR1 to DR2 (smaller BAO errors, same direction); ACT DR6 and SPT-3G D1 in 2025 (higher Ω_m on the CMB side); the 2026 SPT-3G D1 lensing reconstruction, with which the curvature and w0wa preferences from CMB + DESI drop to about 2σ (arXiv:2608.31136) [sec: cmb].

## 5. Dynamical dark energy preference
<!-- key: dynamical-dark-energy-preference -->

### 5.1 Frequentist significance by combination
<!-- key: frequentist-significance-by-combination -->

Significance is the conversion of Δχ²_MAP with two extra degrees of freedom [sec: de]. All rows [sec: de, `results.md` §1, §2, §9].

| Combination | Significance | Status | Citation |
|---|---|---|---|
| DESI DR2 BAO alone | 1.7σ | current | arXiv:2503.14738 |
| DESI DR2 + compressed CMB priors (θ*, ω_b, ω_bc) | 2.4σ | current | arXiv:2503.14738 |
| DESI DR2 + CMB | 3.1σ | current | arXiv:2503.14738 |
| DESI DR2 + CMB + Pantheon+ / Union3 / DESY5 | 2.8σ / 3.8σ / 4.2σ | superseded | arXiv:2503.14738 |
| DESI DR2 + CMB + DES-Dovekie | 3.2σ | current, DES's own paper | Popovic et al. 2025, arXiv:2511.07517 |
| DESI DR2 + Planck + corrected Pantheon+ / Union3.1 / DES-Dovekie | 3.2σ / 3.4σ / 3.4σ | current, rerun "exactly as done by DESI DR2" | Hoyt et al. 2026, arXiv:2601.19424 |
| Unite (2884 SNe) + CMB + DES and DESI BAO | 3.3σ (MAP), 3.1σ (maximum likelihood) | current | Camilleri et al. 2026, arXiv:2609.05053 |
| DES Y6 SN + BAO + 3×2pt alone | 2.2σ | current | DES Collaboration 2026, arXiv:2605.27221 |
| DES Y6 + DESI DR2 BAO + primary CMB | 3.0σ; 2.6σ without SNe | current | arXiv:2605.27221 |
| DESI DR1 P + B + DR2 BAO + CMB + DES-Dovekie | 3.1σ, "driven primarily by the CMB" | current | Forero-Sánchez et al. 2026, arXiv:2606.23936 |
| DESI DR1 P + B + DR2 BAO, DESI only | within 1σ of Λ | current | arXiv:2606.23936 |

Pivot: for DESI + CMB + DESY5, w_p = −0.954 ± 0.024 at z_p = 0.31; the signal is a slope, not an offset, and w0waCDM lowers H0 rather than raising it [sec: de].

### 5.2 Bayesian evidence on the same data
<!-- key: bayesian-evidence-on-the-same-data -->

ln B = ln Z(w0wa) − ln Z(Λ); positive favours w0wa.

| Combination | ln B | Analysis | Flag |
|---|---|---|---|
| DESI DR2 + CMB | −0.57 ± 0.26 | Ong, Yallup & Handley 2025, arXiv:2511.10631 | [sec: stat] |
| DESI DR2 + CMB + Pantheon+ | −0.66 ± 0.44 | Lodha et al. 2025, arXiv:2503.14743 | [sec: de] |
| DESI DR2 + CMB + Union3 | 3.03 ± 0.44 | arXiv:2503.14743 | [sec: de] |
| DESI DR2 + CMB + DESY5 (original) | 4.88 ± 0.44 | arXiv:2503.14743 | [sec: de] |
| DESI DR2 + CMB + DES-SN5YR (original) | +3.32 ± 0.27 | arXiv:2511.10631 | [sec: stat] |
| DESI DR2 + CMB + DES-Dovekie | −0.30 ± 0.19 | arXiv:2511.10631 | [sec: stat] |
| DESI DR2 + CMB + DES-Dovekie | odds "approximately 5:1", ln B ≈ 1.6 [der: ln 5] | arXiv:2511.07517 | [sec: de] |
| Unite + CMB + BAO | "only weak preference" | arXiv:2609.05053 | [sec: de] |

Two pairs of rows give different values for the same nominal quantity (DESY5: 4.88 against 3.32; DES-Dovekie: about +1.6 against −0.30). They come from different analyses with their own priors and CMB likelihoods, and the two siblings each carry one of them; neither sibling reconciles them, and this file does not either. Quote the paper, not "the Bayes factor".

Where the Bayesian preference comes from according to arXiv:2511.10631: a 2.95 ± 0.04σ tension between DESI DR2 and DES-SN5YR within ΛCDM, reduced to 1.96 ± 0.04σ with DES-Dovekie [sec: stat].

### 5.3 What moved it and when
<!-- key: what-moved-it-and-when -->

| Date | Event | Pantheon+ / Union3 / DES | Citation | Flag |
|---|---|---|---|---|
| Apr 2024 | DESI DR1 BAO | 2.5σ / 3.5σ / 3.9σ | value in `cosmo-dark-energy-modified-gravity` `results.md` §9 | [sec: de] |
| Mar 2025 | DESI DR2 BAO | 2.8σ / 3.8σ / 4.2σ | arXiv:2503.14738 | [sec: de] |
| Nov 2025 | DES-Dovekie recalibration and colour-law fix | DES: 3.2σ | arXiv:2511.07517 | [sec: de] |
| Jan 2026 | Union3.1; Pantheon+ host masses corrected | 3.2σ / 3.4σ / 3.4σ | arXiv:2601.19424 | [sec: de] |
| May 2026 | DES Y6 all probes + DESI DR2 + CMB | 3.0σ | arXiv:2605.27221 | [sec: de] |
| Jun 2026 | DESI DR1 bispectrum | weakens the preference | arXiv:2606.23936 | [sec: de] |
| Sep 2026 | Unite | 3.3σ | arXiv:2609.05053 | [sec: de] |

The spread between supernova samples (1.4σ in 2025) has closed; the three samples converge on 3.2–3.4σ.

## 6. Negative effective neutrino mass
<!-- key: negative-effective-neutrino-mass -->

All rows [sec: nu, `results.md` §1.4 and `open-questions.md` §1.1].

| Quantity | Value | Data and model | Citation |
|---|---|---|---|
| Σm_ν, 95% upper limit | < 0.0642 eV | DESI DR2 BAO + CMB, ΛCDM | Elbers et al. 2025, arXiv:2503.14744 |
| Σm_ν, 95% upper limit | < 0.163 eV | same, w0waCDM | arXiv:2503.14744 |
| Effective signed mass | −0.101 (+0.047/−0.056) eV | DESI DR2 BAO + CMB, ΛCDM | arXiv:2503.14744 |
| Tension with the oscillation minimum (0.059 eV normal ordering) | 3σ | same | arXiv:2503.14744 |
| Same tension on DR1 | 2.8–3.3σ | Planck + ACT + DESI DR1 | Elbers et al. 2024, arXiv:2407.10965 |
| Effective mass with two lensing amplitudes free | −0.018 (+0.085/−0.089) eV | Planck, Planck + ACT lensing, DESI | Cozzumbo et al. 2025, arXiv:2511.01967 |
| Tension with τ fixed at 0.067 or 0.074 | 2.3σ or 1.7σ | DESI DR2 BAO + CMB | arXiv:2503.14744 |

The tension vanishes in w0waCDM, where the mass returns to 0.06 (+0.15/−0.10) eV (arXiv:2407.10965), with free lensing amplitudes, or with τ ≈ 0.09 (arXiv:2504.16932, arXiv:2504.21813) [sec: nu, de]. What moved it: DESI DR1 (2024) created it; DR2 kept it at 3σ; no data release has removed it. It is not an independent anomaly (Section 4).

## 7. Cosmic dipole
<!-- key: cosmic-dipole -->

Reference endpoint: the CMB temperature dipole read as kinematic, v/c = 0.00123, v = 369 km/s (Planck Collaboration 2013, arXiv:1303.5087) [src], propagated to a number-count dipole with the Ellis & Baldwin 1984 formula (doi:10.1093/mnras/206.2.377; `physics-and-methods.md` §6). All rows [src], abstracts read on 2026-10-10.

### 7.1 Number-count dipoles against the kinematic expectation
<!-- key: number-count-dipoles-against-the-kinematic -->

| Result | Data | Method | Citation |
|---|---|---|---|
| Amplitude "over twice as large as expected"; p = 5 × 10⁻⁷, 4.9σ one-sided; direction similar to the CMB dipole | 1.36 million CatWISE2020 quasars, flux-limited, all-sky | p-value of the measured dipole under the purely kinematic null | Secrest et al. 2021, arXiv:2009.14826 |
| Radio p = 8.9 × 10⁻³ (2.6σ); quasars p = 1.2 × 10⁻⁵ (4.4σ); joint 5.1σ; no evidence for frequency dependence | NVSS radio galaxies and WISE quasars, no shared objects | statistic including the directional offset; sample-size-weighted Z-scores | Secrest et al. 2022, arXiv:2206.05624 |
| Amplitude 2.7 times the kinematic expectation, 5.7σ; Galactic mask leaks dipole power to higher multipoles and worsens the discrepancy; source evolution helps "only mildly" | same 1.36 million quasars | Bayesian evidence | Dam, Lewis & Brewer 2023, arXiv:2212.07733 |
| All four radio amplitudes exceed the expectation and increase with decreasing frequency | TGSS-ADR1, WENSS, SUMSS, NVSS, one masking strategy | quadratic estimator, validated on simulations with 10⁷ sources | Siewert, Schmidt-Rubart & Schwarz 2021, arXiv:2010.08366 |
| Residual, non-kinematic dipole D_resid = (0.81 ± 0.14) × 10⁻², offset by 39° ± 8° from the CMB dipole, with the kinematic part fixed to the CMB expectation; a common direction of the two components is disfavoured | NVSS + RACS + CatWISE, joint fit | Bayesian model selection | Wagenveld et al. 2025, arXiv:2503.02470 |
| Dipole 3.67 ± 0.49 times the kinematic expectation, 5.4σ | NVSS + RACS-low + LoTSS-DR2 | negative-binomial counts for multi-component sources | Böhme et al. 2025, arXiv:2509.16732 |
| CatWISE against Planck ≈ 5.7σ; ≈ 6.7σ with a forward model of the CatWISE Eddington bias | Planck, NVSS, RACS, CatWISE | neural ratio estimation of the evidence ratio | Land-Strykowski et al. 2026, arXiv:2607.25703 |
| Significance revised to 3.63σ without a clustering dipole, 3.44σ with a randomly oriented one, 3.27σ with one aligned with the kinematic dipole | CatWISE2020 quasars | lognormal mocks with clustering, radial selection, exact sky coverage | Bashir, Chingangbam & Appleby 2025, arXiv:2511.00822 |

The review by the discovering group states that the discrepancy "now exceeds 5σ" (Secrest et al. 2025, arXiv:2505.23526) [src].

### 7.2 Measurements that agree with the CMB velocity
<!-- key: measurements-that-agree-with-the-cmb-velocity -->

| Result | Data | Citation | Flag |
|---|---|---|---|
| 384 ± 78 (stat) ± 115 (syst) km/s along (l, b) = (264°, 48°), from aberration and modulation of the CMB anisotropies | Planck 2013 | arXiv:1303.5087 | [src] |
| v = 357.95 (+55.05/−48.47) km/s from the redshift dipole of quasars, against 369.82 ± 0.11 km/s from the CMB; the number-count dipole of the same catalogues is "significantly enhanced", attributed by the authors to leakage of large-scale power and footprint incompleteness | DESI DR1 BGS, LRG, ELG, QSO, 0.1 < z < 2.1; 1,000 EZmocks | Wu & Xia 2026, arXiv:2608.30914 | [src] |
| Upper limits on the bulk flow at 200–2000 h⁻¹Mpc consistent with ΛCDM, in "strong tension" with a ~370 km/s flow at R ~ 1000 h⁻¹Mpc | kSZ velocity reconstruction, Planck × WISE×SuperCOSMOS and unWISE | arXiv:2605.12499 | [sec: pv] |

### 7.3 Supernova dipole
<!-- key: supernova-dipole -->

The dipole of the low-redshift Pantheon+SH0ES supernovae "does not agree with the one inferred from the velocity of the solar system as obtained from CMB data", which its authors read as bulk velocities; a monopole and a quadrupole of similar amplitude are also detected, the monopole only at very low redshift (Sorrenti, Durrer & Kunz 2024, arXiv:2403.17741) [src]. The sibling `cosmo-peculiar-velocities` holds the counter-evidence: zero-point dipoles in CF4 and Pantheon+ are better described by local flow structure than by anisotropic expansion (arXiv:2509.14997) [sec: pv].

### 7.4 Size, metric, endpoint, history
<!-- key: size-metric-endpoint-history -->

- Metric: p-value of the observed amplitude (and direction) under the null of a purely kinematic dipole with the CMB velocity, from mock skies; or a Bayesian evidence ratio. The endpoint depends on the sample through its count slope x and spectral index α, so each catalogue has its own expected amplitude.
- Size at the snapshot: 3.3σ to 5.7σ for the CatWISE2020 quasars depending on whether a clustering dipole and mode coupling are simulated; 5.4σ for three radio surveys combined; one direct velocity measurement from redshifts and one from CMB aberration that agree with 370 km/s.
- What moved it: 2020–2021, CatWISE (4.9σ); 2022, joint radio + quasar (5.1σ); 2023, Bayesian reanalysis (5.7σ); 2025, radio with overdispersion (5.4σ) and a clustering-aware reassessment (3.3–3.6σ); 2026, DESI redshift dipole consistent with the CMB.

## 8. Bulk flow
<!-- key: bulk-flow -->

All rows [sec: pv, `results.md` §3]. A bulk flow is defined only with its estimator, window and depth.

| Measurement | Amplitude (km/s) | ΛCDM expectation or verdict | Citation |
|---|---|---|---|
| CF4, minimum variance, top-hat, 150 h⁻¹Mpc | 387 ± 28 | expectation 139; probability 0.023% | Watkins et al. 2023, arXiv:2302.02028 |
| CF4, same, 200 h⁻¹Mpc | 419 ± 36 | expectation 120; probability 0.00021% (table), "less than 0.003%" (abstract) | arXiv:2302.02028 |
| CF4, minimum variance, mock-calibrated errors, 173 h⁻¹Mpc | 428 ± 108 | probability 0.11% | Whitford, Howlett & Davis 2023, arXiv:2306.11269 |
| CF4, monopole + dipole in six radial bins to 300 h⁻¹Mpc | 628 ± 82 in the 120–160 h⁻¹Mpc bin | full range 2.29σ (dipole), 2.36σ (joint); peak bin 3.40σ, 1.56σ without 6dFGS, 3.77σ without SNe | Nusser & Tully 2026, arXiv:2608.14265 |
| CF4 TF, 2MTF, SFI++, Pantheon+ at z < 0.05, forward model | bulk-flow curve | "fully consistent with expectations from the standard cosmological model" | Stiskalek, Desmond & Lavaux 2025, arXiv:2509.14997 |
| kSZ velocity reconstruction, 200–2000 h⁻¹Mpc | upper limits | consistent with ΛCDM; "strong tension" with reading the CatWISE quasar dipole as a ~370 km/s flow at R ~ 1000 h⁻¹Mpc | Gandhi et al. 2026, arXiv:2605.12499 |

Metric and endpoint: χ² of the three flow components against the ΛCDM velocity covariance for the same window. What moved it: the amplitude has not moved (387, 428 and 315 km/s in three analyses differ by less than 2σ); the quoted probability rose from 0.00021% to 0.11% when errors were calibrated on mocks (2023), and a shell analysis with the ΛCDM prediction computed for the actual positions reduced the full-range deviation to 2.3σ (2026) [sec: pv].

## 9. Large-angle CMB anomalies
<!-- key: large-angle-cmb-anomalies -->

Reference endpoint: Gaussian, statistically isotropic ΛCDM skies simulated with the instrument and mask of the data. Metric: the p-value (lower- or upper-tail probability) of a summary statistic among those simulations. All of these statistics were defined after the features were seen in WMAP or Planck temperature maps, so every p-value is a posteriori. All rows [src], abstracts read on 2026-10-10 unless a section is named.

| Anomaly | Size | Data | Citation |
|---|---|---|---|
| All temperature anomalies together | individual p-values "in the per mille to per cent level" | WMAP and Planck 2013–2015 | Schwarz et al. 2016, arXiv:1510.07929 |
| Temperature anomalies in the final Planck collaboration analysis | "confirm the presence of several so-called anomalies on large angular scales"; in polarisation "no unambiguous detections … of anomalies corresponding to those seen in temperature" | Planck 2018 (PR3), four component-separated maps | Planck Collaboration 2019, arXiv:1906.02552 |
| Lack of power at large angular scales | lower-tail probability ≤ 0.33% in PR3 and ≤ 1.76% in PR4, depending on the component-separation method; the two releases differ significantly once polarisation is included | Planck PR3 and PR4, temperature-only estimator | Billi, Barreiro & Martínez-González 2023, arXiv:2312.09989 |
| Lack of correlation, quadrupole–octopole alignment, hemispherical asymmetry | "detected at a similar level to the previous releases" in PR4; thermal and kinetic SZ from the local Universe have negligible impact | Planck PR4; constrained hydrodynamical simulation of a 500 h⁻¹Mpc box | Jung et al. 2024, arXiv:2406.11543 |
| Hemispherical asymmetry as clustering of local bandpower directions | clustering probability below 1% for multipoles between 200 and 2000 in temperature, a wider range than in PR3; no significant clustering in E modes | Planck PR4, end-to-end simulations | Gimeno-Amo et al. 2025, arXiv:2504.05597 |
| Dipolar variation of cosmological parameters across the sky | a dipole in A_s as large as observed in 5 of 600 simulations, aligned with the hemispherical asymmetry; other parameters consistent with ΛCDM | Planck PR4, TT + EE | arXiv:2504.05597 |
| Four statistics jointly: S_1/2 (large-angle correlation), R^TT (odd over even low-ℓ power), σ²_16 (variance in the ecliptic north), S_QO (quadrupole–octopole alignment) | joint probability "likely ≤ 3 × 10⁻⁸", with little correlation among the four | Planck temperature | Jones et al. 2023, arXiv:2310.12859 |
| The same joint probability after a look-elsewhere correction | 3σ if the four were picked from 16 tests, 2σ if from 50, with the measured correlation among the four (10 and 27 tests if uncorrelated); two of the four statistics do not test statistical anisotropy | reanalysis of arXiv:2310.12859 | Guth & Namjoo 2026, arXiv:2602.10178 |
| Cold Spot | p-value ≲ 0.01 in ΛCDM | Planck temperature | Owusu et al. 2023, arXiv:2211.16139 |
| Cold Spot as the imprint of a supervoid | void model disfavoured against ΛCDM with odds 1:13 (SMICA) and 1:20 (NILC) once the Planck lensing signal is used, against 56:1 and 21:1 from temperature alone | Planck temperature and lensing | arXiv:2211.16139 |

Status in Planck PR4 and after. The temperature anomalies are present in PR4 at the level of earlier releases (arXiv:2406.11543); the lack-of-power probability is less extreme in PR4 than in PR3 (≤ 1.76% against ≤ 0.33%, arXiv:2312.09989); the hemispherical asymmetry extends to higher multipoles in PR4 (arXiv:2504.05597). No anomaly has been confirmed in polarisation. The Planck collaboration's own caveats (arXiv:1906.02552, conclusions) [src]: there is of order a 30% chance that the significance of any p-value dip increases when statistically isotropic polarisation data are added; the dipole-modulation and hemispherical-asymmetry statistics measure different weightings of the same ℓ to ℓ ± 1 couplings and are not independent; and even cosmic-variance-limited E modes may not give detections above 3σ.

What moved it: nothing in the temperature data; the Planck 2015 release "essentially corresponded to the limit of our ability to probe CMB anomalies with temperature fluctuations alone" (arXiv:1906.02552, conclusions) [src]. What changed is the accounting: a claimed joint 5σ (2023) against 2σ to 3σ after the look-elsewhere correction (2026), and the exclusion of the supervoid explanation of the Cold Spot by lensing (2023).

## 10. JWST high-redshift galaxy abundance
<!-- key: jwst-high-redshift-galaxy-abundance -->

Reference endpoint: the ΛCDM halo mass function times the cosmic baryon fraction, which bounds the stellar mass a halo can host. Metric: the comoving number density n(> M_*, z) or stellar mass density ρ_*(> M_*, z) of the observed galaxies against that bound, expressed as the required efficiency ε of converting baryons into stars; ε > 1 would contradict ΛCDM, ε below 1 is a statement about galaxy formation. All rows [src], abstracts read on 2026-10-10.

| Result | Data | Status of redshifts and masses | Citation |
|---|---|---|---|
| Six candidate galaxies with M_* > 10¹⁰ M_⊙ at 7.4 < z < 9.1, one with a possible M_* ~ 10¹¹ M_⊙; "if verified with spectroscopy" the stellar mass density would be much higher than anticipated | JWST early release NIRCam imaging | photometric candidates | Labbé et al. 2023, arXiv:2207.12446 |
| The most massive candidates at z ~ 7–10 "lie at the very edge" of the limits set by the halo mass function and the baryon reservoir | the candidates above and similar ones | photometric | Boylan-Kolchin 2023, arXiv:2208.01611 |
| "No tension with the ΛCDM model" in the sample; three ultra-massive galaxies (log M_*/M_⊙ ≳ 11.0) require about 50% of baryons converted into stars, two to three times the most efficient galaxies at later epochs | 36 massive dust-obscured galaxies at z_spec = 5–9, JWST FRESCO | spectroscopic (slitless grism) | Xiao et al. 2024, arXiv:2309.02492 |
| One of those three, S1, moves from z_grism = 5.58 to z_spec = 3.2439 ± 0.0002 (grism contamination by a neighbour) and to log M_*/M_⊙ ~ 10.6; the authors state that the main conclusions of the 2024 paper are unchanged | JWST NIRSpec IFU + ALMA | spectroscopic, multi-line | Xiao et al. 2026, arXiv:2602.03030 |
| UV luminosity functions at 7 ≤ z ≤ 14 reproduced over five magnitudes in ΛCDM; star-formation efficiency rising with redshift at fixed halo mass to 2–3% of baryons by z = 10–12; earlier claims of excess stellar mass at z = 8 attributed to AGN contamination, dust and missing MIRI constraints | UniverseMachine on the Uchuu N-body simulation against spectroscopically confirmed JWST and HST galaxies | model comparison | Prada et al. 2026, arXiv:2604.18683 |

Size at the snapshot: no published spectroscopic sample requires ε > 1. The abundance question has become a galaxy-formation question (how efficiency, burstiness, dust, AGN light and the initial mass function evolve at z > 7) and is treated in `cosmo-reionization-21cm` for its bearing on reionisation. What moved it: 2022, photometric candidates at the ΛCDM limit; 2023–2024, spectroscopy (no tension in the FRESCO sample, with three objects needing about 50%); 2026, one of those three shown to be a lower-redshift interloper of the grism method, and an empirical ΛCDM model matching the UV statistics.

## 11. Curvature, birefringence, parity-odd 4PCF
<!-- key: curvature-birefringence-parity-odd-4pcf -->

| Quantity | Value | Data | Citation | Flag |
|---|---|---|---|---|
| Ω_K | −0.044 (+0.018/−0.015) | Planck 2018 TT,TE,EE + lowE (Plik), spectra only | arXiv:1807.06209 | [sec: inf, cmb] |
| Ω_K | −0.012 ± 0.010 | Planck PR4 HiLLiPoP TTTEEE | arXiv:2309.10034 | [sec: cmb] |
| Ω_K | 0.0004 ± 0.0018 | Planck (CamSpec, more sky) + BAO | Efstathiou & Gratton 2020, arXiv:2002.06892 | [sec: inf, cmb] |
| Ω_K | −0.0107 (+0.0064/−0.0053) | CMB as defined by DESI | arXiv:2503.14738 | [sec: inf] |
| Ω_K | +0.0023 ± 0.0011 (2.1σ, open side [der, sec: inf]) | DESI DR2 BAO + CMB, ΛCDM + Ω_K | arXiv:2503.14738 | [sec: inf] |
| Ω_K | (0.6–1.1) × 10⁻³ ± 1.3 × 10⁻³ | DESI DR2 + CMB + SNe, w0waCDM + Ω_K | arXiv:2503.14738 | [sec: inf] |
| β (isotropic birefringence) | 0.342° (+0.094/−0.091) | WMAP + Planck | Eskilt & Komatsu 2022; ID in `cosmo-inflation-primordial` `results.md` §10 | [sec: inf] |
| β | 0.215° ± 0.074° (2.9σ) | ACT DR6 EB and TB | value in `cosmo-cmb` `results.md` §8 | [sec: cmb] |
| β | 0.277° ± 0.057°, 4.8σ; the authors claim no detection | ACT + Planck joint | Eskilt et al. 2026, arXiv:2608.06480 | [sec: inf] |
| Parity-odd 4PCF | 7.1σ (CMASS), 3.1σ (LOWZ) against Patchy mocks | BOSS DR12 | Hou, Slepian & Cahn 2022, arXiv:2206.03625 | [sec: b2p] |
| Parity-odd 4PCF | signal 0–2.5σ; parity-even 8PCF bias term ≈ 6σ | BOSS, χ²_× and χ²_null statistics | Krolewski et al. 2024, arXiv:2407.03397 | [sec: b2p] |
| Parity-odd 4PCF | auto analysis 4–10σ; cross-patch analysis null | DESI DR1 LRG | Slepian et al. 2025, arXiv:2508.09133 | [sec: b2p] |

Reading. The Planck-alone closed-universe preference (Di Valentino, Melchiorri & Silk 2019, arXiv:1911.02087, "more than 99%") is the A_L feature in another parameter and has followed A_L down; the 2025 open-side hint is the CMB–DESI mismatch in another parameter and vanishes when w0wa is free [sec: inf]. The birefringence significance is conditional on the ACT instrumental priors on the polarisation angle [sec: inf]. For the 4PCF the position is "no evidence for parity violation" [sec: b2p].

## 12. History: what moved each tension
<!-- key: history-what-moved-each-tension -->

| Tension | Peak quoted size | When | Size now | What moved it |
|---|---|---|---|---|
| H0 | 7.1σ | 2025 | 4.4–7.1σ (SH0ES, H0DN); below 2σ (CCHP, lenses) | smaller local errors; lower, tighter CMB endpoint; no route has closed the gap |
| S8, cosmic shear | about 3σ | 2020–2021 | 0.7–2.6σ | redshift calibration (KiDS, HSC); Planck PR4 |
| S8, CMB-lensing tomography | 0.73 ± 0.03 for DESI LRG | 2021 | 0.775 (+0.019/−0.022) | neutrino consistency, projection effects, lensing normalisation |
| S8, Planck clusters | 3.7σ | 2015 | 1.6σ | lensing mass calibration |
| A_L | 2.7σ | 2018 | ≤ 1σ without Planck high-ℓ TT; about 2σ with it | PR4; ACT DR6; SPT-3G D1 |
| Ω_K < 0 from Planck | "more than 99%" | 2019 | −0.012 ± 0.010 (PR4) | same as A_L |
| w0wa | 4.2σ | March 2025 | 3.0–3.4σ | supernova recalibration and host-mass fix |
| CF4 bulk flow | probability 0.00021% | 2023 | 0.11%; 2.3σ full-range | mock-calibrated errors; shell analysis |
| Parity-odd 4PCF | 7.1σ | 2022 | null | N-body mocks; 8PCF-free and cross-patch statistics |
| E_G at CMASS | 2.6σ low | 2015 | consistent with GR | matched redshifts, calibrated estimator (`cosmo-dark-energy-modified-gravity`) |
| CatWISE quasar dipole | 6.7σ (forward-modelled Eddington bias) | 2026 | 3.3–3.6σ with clustering-aware mocks to 5.7σ in the Bayesian analyses | null model with clustering, selection and mask; a direct velocity from redshifts |
| CMB large-angle anomalies, joint | ≤ 3 × 10⁻⁸ | 2023 | 2σ to 3σ | look-elsewhere correction |
| JWST massive candidates | "at the very edge" of the ΛCDM limit | 2022 | no tension in spectroscopic samples | spectroscopy; one grism redshift revised |

Sizes and dates in this table are from the sections above: [sec] from the siblings named there for the first ten rows, [src] for the last three.

## Not verified
<!-- key: not-verified -->

- The Planck 2018 S8 with its error from the Planck paper itself; the two siblings give 0.834 ± 0.016 (as quoted in arXiv:2309.10034, `cosmo-cmb`) and a derived central value 0.831 (`cosmo-weak-lensing`).
- The reconciliation of the two published Bayes factors for DESI DR2 + CMB + DES supernovae (Section 5.2).
- The point-estimate convention (mean, mode, MAP) behind each S8 row; the Gaussian differences of Section 2 inherit that ambiguity.
