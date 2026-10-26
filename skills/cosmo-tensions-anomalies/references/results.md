# Tensions and anomalies — current sizes

Scope: one table per tension or anomaly: current size, data sets, metric, reference endpoint, what moved it and when.

Snapshot: 2026-10-26

Flags. `[src]`: read this session in the cited paper. `[sec: X]`: taken from the reference files of the sibling skill X, where the number is flagged `[src]` against the same arXiv ID; the sibling is the secondary source. `[der]`: a derivation in words, without a number (owner's rule of 2026-10-23: no number computed here). Sibling abbreviations: `h0` = `cosmo-distance-ladder-h0`, `wl` = `cosmo-weak-lensing`, `cmb` = `cosmo-cmb`, `de` = `cosmo-dark-energy-modified-gravity`, `cl` = `cosmo-clusters`, `x` = `cosmo-cmb-lss-cross-correlations`, `nu` = `cosmo-neutrinos-dark-matter`, `pv` = `cosmo-peculiar-velocities`, `inf` = `cosmo-inflation-primordial`, `stat` = `cosmo-statistics-inference`, `b2p` = `cosmo-beyond-two-point`. Sect. 1–6, Sect. 8, Sect. 11 are a synthesis of those siblings; Sect. 7, Sect. 9, Sect. 10 were researched for this skill. H0 is in km/s/Mpc, the model is flat ΛCDM unless a row says otherwise, and S8 ≡ σ8 sqrt(Ω_m/0.3).

Every significance below is the one the cited paper prints, with its metric where the paper names it. The Gaussian-difference tables of earlier versions (one definition applied by this skill to every pair) were computed here and were removed on 2026-10-23; they are kept in `docs/history/set-aside/2026-10-23/cosmo-tensions-anomalies-results.md`.

## 0. Summary of sizes at the snapshot
<!-- key: summary-of-sizes-at-the-snapshot -->

| Tension or anomaly | Current size | Depends most on | Section |
|---|---|---|---|
| H0, ladder against early Universe | 4.5σ (SH0ES against DESI DR2 BAO + BBN, arXiv:2503.14738 [src: Sect. VI]) to 7.1σ (H0DN against Planck + SPT + ACT, arXiv:2510.23823 [src: abstract]); CCHP TRGB "consistent with the current standard ΛCDM model" (arXiv:2408.06153) [src: abstract]; without the ladder, late-universe probes combined around TDCOSMO-2026 remain 2.7σ from Planck, 3.7σ without supernovae (arXiv:2610.14881) [src: abstract] | which local team and which early endpoint | Sect. 1 |
| S8, lensing against CMB | 0.73σ (KiDS-Legacy against Planck Legacy, arXiv:2503.19441 [src: abstract]) to 2.6σ projected on S8 and 1.8σ in full space (DES Y6 3×2pt against Planck + ACT + SPT primary CMB, arXiv:2601.14559 [src: abstract]) | survey, metric, CMB reference | Sect. 2 |
| S8, spread among low-redshift probes | 0.72 ± 0.03 (tSZ × galaxies, arXiv:2605.11083) to 0.86 ± 0.01 (eRASS1 clusters, arXiv:2402.08458) [src: abstract of each] | probe and astrophysical model | Sect. 2 |
| A_L (peak smoothing) | 2.7σ in Planck PR3 Plik (arXiv:1807.06209 [src: Sect. 2.2.1]); A_L = 1.039 ± 0.052 in PR4 HiLLiPoP (arXiv:2309.10034 [src: abstract]); "no evidence for excess lensing" in P-ACT (arXiv:2503.14452 [src: abstract]); 1.6σ in the (A_2pt, A_recon) plane for CMB-SPA (arXiv:2506.20707 [src: Sect. VII.2.3]) | the oscillatory Planck TT residual at 1000 < ℓ < 2000 (arXiv:2503.14452) [src: Sect. VIII.5] | Sect. 3 |
| τ, BAO-preferred against measured | 0.090 ± 0.012 (DESI BAO + high-ℓ CMB + lensing, arXiv:2504.16932 [src: abstract]) against 0.058 ± 0.006 (Planck PR4, arXiv:2309.10034 [src: Eq. 14]) | whether low-ℓ EE is dropped | Sect. 3 |
| CMB against DESI DR2 BAO in ΛCDM | 1.6σ (P-ACT, arXiv:2503.14452 [src: abstract]) to 3.7σ (SPT + ACT, arXiv:2506.20707 [src: Sect. VII.3]) in the Ω_m–h r_d plane | CMB data set, τ | Sect. 4 |
| w0wa preference | 1.7σ BAO alone, 3.1σ + CMB, 2.7σ without CMB lensing (arXiv:2503.14738 [src: Table 6]); 1.4σ with a τ prior of 0.09 (arXiv:2504.16932 [src: Sect. III.2]); 3.0σ (DES Y6 all probes, arXiv:2605.27221) to 3.4σ (arXiv:2601.19424) with recalibrated supernovae [src: abstract of each]; a Jeffreys prior turns every ln B for DESI DR2 + Planck 2018 (± SNe) negative (arXiv:2610.26493) [src: Sect. 4.2, Table 4] | SN sample, CMB lensing, τ, statistic, prior | Sect. 5 |
| Effective neutrino mass below the oscillation minimum | 3σ in ΛCDM (arXiv:2503.14744 [src: abstract]); 2.7σ (goodness of fit), 3.0σ (probability to exceed) and 4.0σ (parameter shift) [src: Sect. V.3, Table 4]; absent in w0waCDM (arXiv:2407.10965 [src: abstract]) or with free lensing amplitudes (arXiv:2511.01967 [src: abstract]); geometry and growth channels both negative and mutually consistent at 0.4σ (arXiv:2610.20977) [src: abstract] | model, τ, lensing, metric | Sect. 6 |
| Number-count dipole against the CMB kinematic expectation | CatWISE quasars: 3.63σ (no clustering dipole), 3.44σ (random) or 3.27σ (aligned) with clustering-aware mocks (arXiv:2511.00822 [src: abstract]), 5.7σ (arXiv:2212.07733 [src: abstract]), ≈ 6.7σ with a forward-modelled Eddington bias (arXiv:2607.25703 [src: abstract]); 5.4σ for three radio surveys (arXiv:2509.16732 [src: abstract]); the DESI redshift dipole agrees with the CMB velocity (arXiv:2608.30914 [src: abstract]) | catalogue, null model, source evolution | Sect. 7 |
| CF4 bulk flow at 150–200 h⁻¹Mpc (arXiv:2302.02028 [src: abstract]) | 0.11% probability with mock-calibrated errors (arXiv:2306.11269 [src: abstract]); dipole deviation 2.29σ over the full range in a shell analysis (arXiv:2608.14265 [src: abstract]) | error model, window, 6dFGS | Sect. 8 |
| Large-angle CMB anomalies | individual p-values "in the per mille to per cent level" (arXiv:1510.07929 [src: abstract]); a claimed joint ≤ 3 × 10⁻⁸ (arXiv:2310.12859 [src: abstract]) becomes 3σ if chosen from about 16 tests and 2σ from about 50 (arXiv:2602.10178 [src: abstract]); nothing in polarisation (arXiv:1906.02552) | choice and number of statistics, mask | Sect. 9 |
| JWST early-galaxy abundance | "no tension with the ΛCDM model" in 36 spectroscopic massive galaxies, three of which need 50% of baryons in stars (arXiv:2309.02492 [src: abstract]); one of those three later moved to lower redshift (arXiv:2602.03030 [src: abstract]) | redshift method, stellar-mass systematics, star-formation efficiency | Sect. 10 |
| Curvature | −0.044 (+0.018/−0.015) from Planck 2018 TT,TE,EE + lowE (arXiv:1807.06209 [src: Sect. 7.3, Eq. 44b]); −0.012 ± 0.010 from PR4 (arXiv:2309.10034 [src: abstract]); the opposite sign with DESI DR2 + CMB (Sect. 11) | same features as A_L and CMB–BAO | Sect. 11 |
| Isotropic birefringence | 0.277° ± 0.057°, 4.8σ, with "unresolved systematics" to be understood first (arXiv:2608.06480 [src: abstract]) | absolute angle calibration | Sect. 11 |
| Parity-odd 4PCF | no detection | mocks, 8PCF bias | Sect. 11 |

## 1. H0 tension
<!-- key: h0-tension -->

### 1.1 The two sides
<!-- key: the-two-sides -->

| Side | Value | Data | Citation | Flag |
|---|---|---|---|---|
| Local | 73.50 ± 0.81 | H0 Distance Network baseline (Gaia, DEBs, NGC 4258; Cepheids + TRGB; SN Ia, SBF, masers) | H0DN Collaboration 2025, arXiv:2510.23823 | [src: Eq. 1, Sect. IV] |
| Local | 73.18 ± 0.88 | SH0ES: HST + JWST Cepheids + 35 TRGB calibrations, 55 SN Ia calibrators; "∼6σ above the ΛCDM + CMB expectation" | Riess et al. 2025, arXiv:2509.01667 | [src: abstract] |
| Local | 73.04 ± 1.04 | SH0ES HST-only baseline, 42 calibrators | Riess et al. 2022, arXiv:2112.04510 | [src: abstract] |
| Local | 70.39 ± 1.22 (stat) ± 1.33 (sys) ± 0.70 (σ_SN) | CCHP TRGB, 24 SN Ia calibrators, anchor NGC 4258 | Freedman et al. 2024, arXiv:2408.06153 | [src: abstract; Sect. I, Fig. 1] |
| Local, one-step | 71.1 (+2.4/−2.3), 3.3% "that accounts for the mass-sheet degeneracy"; 3.0% with SLACS and SL2S added; DESI DR2 BAO in place of the DES-Dovekie Ω_m prior "yields fully consistent results" | TDCOSMO-2026, 11 lensed quasars, spatially resolved kinematics for nine, Ω_m prior from DES-Dovekie supernovae; supersedes TDCOSMO-2025 (Sect. 12.1) | TDCOSMO Collaboration 2026, arXiv:2610.14781; companion arXiv:2610.14881 | [src: abstract of each] |
| Local, one-step | 65.0 (+2.0/−1.8), Ω_m = 0.30 (+0.08/−0.09) | SN Refsdal time delays with the host surface brightness (77,000 HST pixels) in MACS J1149.5+2223; cluster total-mass parametrisation held fixed to the earlier point-like model, so its systematics are not in the error | Schuldt et al. 2026, arXiv:2610.12595 | [src: abstract] |
| Local, one-step | 71.7 (+9.4/−7.5), median and 68% interval | GWTC-5.0, 236 sources: mass-spectrum features, GW170817 with its counterpart, DES Y6 galaxy catalogue; 22.0% smaller error than GWTC-4.0 | LVK 2026, arXiv:2605.27227 | [src: abstract] |
| Inverse ladder, r_d fixed to 147.05 ± 0.30 Mpc | 76.25 ± 2.87 with DES-Dovekie SNe only; 67.98 ± 0.69 adding the legacy low-redshift SNe | DESI DR2 BAO + uncalibrated SNe, cosmographic H(a) (fourth-order polynomial in 1 − a) | Nájera, Banik & Desmond 2026, arXiv:2610.23657 | [src: abstract] |
| Early | 67.4 ± 0.5 (67.36 ± 0.54 in the table) | Planck 2018 TT,TE,EE + lowE + lensing | Planck Collaboration 2018, arXiv:1807.06209 | [src: Table 2] |
| Early | 67.64 ± 0.52 | Planck PR4 HiLLiPoP + LoLLiPoP | Tristram et al. 2023, arXiv:2309.10034 | [src: Sect. 6, Eq. 15] |
| Early | 66.66 ± 0.60 | SPT-3G D1 TT/TE/EE + lensing | Camphuis et al. 2025, arXiv:2506.20707 | [src: abstract] |
| Early | 67.19 ± 0.38 | CMB-SPA (SPT + ACT + Planck), second arXiv version | arXiv:2506.20707 | [src: Sect. II] |
| Early | 66.59 ± 0.46 | SPT + ACT, no Planck | arXiv:2506.20707 | [src: Sect. VII.2.2] |
| Early | 67.62 ± 0.50 | P-ACT | Louis et al. 2025, arXiv:2503.14452 | [src: Sect. II; Sect. VIII.4, Eq. 39] |
| Early, no CMB anisotropies | 68.51 ± 0.58 | DESI DR2 BAO + BBN; 68.45 ± 0.47 adding θ_* | DESI Collaboration 2025, arXiv:2503.14738 | [src: Eqs. 19, 20] |
| Early + BAO | 68.43 ± 0.27 | P-ACT + CMB lensing + DESI DR2 BAO | arXiv:2503.14452 | [src: abstract] |

### 1.2 Size, one definition for every cell
<!-- key: size-one-definition-for-every-cell -->

The table of Gaussian differences that stood here was computed by this skill and was removed on 2026-10-23 (set aside in `docs/history/set-aside/2026-10-23/cosmo-tensions-anomalies-results.md`). Only the significances the papers print are given.

Significances the papers themselves print, all in the one parameter H0 and without a named metric beyond "statistical significance" or "tension": 5.0σ for SH0ES 2022 against Planck, computed as 0.176 ± 0.035 mag in 5 log H0 (arXiv:2112.04510) [sec: h0]; for H0DN, 7.1σ against the flat-ΛCDM CMB value 67.24 ± 0.35 (Planck + SPT + ACT, Eq. 54 of the first version of arXiv:2506.20707) and 5.0σ against DESI DR2 BAO + BBN, 68.51 ± 0.58 (arXiv:2510.23823) [src: abstract, Sect. IV]; for SPT, against SH0ES taken as 73.17 ± 0.86: 6.2σ from SPT-3G D1 alone, 6.4σ from CMB-SPA, 4.9σ from the SPT TE/EE spectra alone (66.1 ± 1.2) (arXiv:2506.20707) [src: Sect. VII.2.2]; 4.5σ between DESI + BBN and SH0ES "independent of the CMB", which still assumes standard pre-recombination physics for r_d (arXiv:2503.14738) [src: Sect. VI].

Without the ladder or without supernovae (TDCOSMO Collaboration 2026, arXiv:2610.14881): combining TDCOSMO-2026 with other independent late-universe probes of 5% precision or better, a "no-SN" combination (the DES-Dovekie Ω_m prior replaced by DESI BAO) is 3.7σ from Planck, and a combination with no distance ladder at all is 2.7σ from Planck [src: abstract]; the latter is TDCOSMO-2026 + SLACS + SL2S with megamasers and globular-cluster ages, and every one of the five leave-one-method-out combinations is at 2.7σ or more [src: Sect. IV.2]. In the inverse ladder, DES-Dovekie supernovae alone give an H0 3.1σ above the CMB-calibrated ΛCDM prediction and 1.0σ from SH0ES, and with the legacy low-redshift supernovae 4.7σ below SH0ES; the drop between the two is reached by 1.24% of 10⁴ ΛCDM mocks, which the authors read as a systematic tension between the DES and legacy samples (arXiv:2610.23657) [src: abstract].

The H0DN paper adopts 67.24 ± 0.35 for Planck + SPT + ACT (arXiv:2510.23823) [src: Sect. IV], the value of the first arXiv version of the CMB-SPA paper; the current version of arXiv:2506.20707 reads 67.19 ± 0.38 [src: abstract]. The 7.1σ of H0DN is computed against the first.

### 1.3 What moved it and when
<!-- key: what-moved-it-and-when-3 -->

| When | What changed | Effect on the tension | Citation | Flag |
|---|---|---|---|---|
| 2022 | SH0ES 42 calibrators, Pantheon+, full covariance | "a 5-sigma difference" with Planck + ΛCDM | arXiv:2112.04510 | [src: abstract] |
| 2024 | JWST CCHP ladder: TRGB 70.39 ± 1.22 (stat) ± 1.33 (sys) ± 0.70 (σ_SN), 24 SN Ia calibrators | "consistent with the current standard ΛCDM model" in the authors' words | arXiv:2408.06153 | [src: abstract] |
| 2025 | SH0ES + JWST Cepheids in 19 hosts + 35 TRGB | 73.18 ± 0.88; "~6σ" | arXiv:2509.01667 | [src: abstract] |
| 2025 | SPT-3G D1 and ACT DR6: ground-based CMB as tight as Planck and lower in H0 | early endpoint moves down and tightens: 67.4 ± 0.5 (Planck 2018, arXiv:1807.06209) to 67.19 ± 0.38 (CMB-SPA) | arXiv:2506.20707, arXiv:2503.14452 | [src: abstract of arXiv:1807.06209 and of arXiv:2506.20707] |
| 2025 | DESI DR2 BAO + BBN | 4.5σ from SH0ES with no CMB anisotropy data | arXiv:2503.14738 | [src: Sect. VI] |
| 2025 | TDCOSMO with the mass-sheet degeneracy free | lensing no longer sides with the ladder at high precision: 71.6 (+3.9/−3.3) (superseded, Sect. 12.1) | arXiv:2506.03023 | [src: abstract] |
| 2025 | H0DN community combination | 73.50 ± 0.81, the highest quoted significance (7.1σ) | arXiv:2510.23823 | [src: Sect. IV] |
| 2026 | Statistical reanalyses of the SH0ES likelihood | 70.6 ± 1.0 with volume priors and no selection term; SH0ES calibration recovered within 0.5σ once Milky Way selection is modelled | Högås & Mörtsell 2026, arXiv:2601.22215; Stiskalek et al. 2026, arXiv:2603.09880 | [src: abstract of each] |
| 2026 | GWTC-5.0 sirens | 71.7 (+9.4/−7.5), compatible with both sides | arXiv:2605.27227 | [src: abstract] |
| Oct 2026 | TDCOSMO-2026, 11 lenses | 71.1 (+2.4/−2.3); the late-universe tension with Planck survives at 3.7σ without supernovae and at 2.7σ without the ladder | arXiv:2610.14781; arXiv:2610.14881 | [src: abstract of each] |
| Oct 2026 | Inverse ladder split by supernova sample | 76.25 ± 2.87 (DES only) against 67.98 ± 0.69 (DES + legacy); late-time solutions "are thus viable with the homogeneous DES catalogue, but not with the legacy SNIa as published" | arXiv:2610.23657 | [src: abstract] |

The SH0ES central value moved little between 2022 (73.04 ± 1.04, arXiv:2112.04510) and 2025 (73.18 ± 0.88, arXiv:2509.01667) [src: abstract of each] while its error shrank; the printed significance grew from "5-sigma" (arXiv:2112.04510) to 7.1σ (H0DN, arXiv:2510.23823) [src: abstract of each] with the smaller local error and the tighter, lower CMB endpoint.

## 2. S8 tension
<!-- key: s8-tension -->

### 2.1 Reference endpoints in use
<!-- key: reference-endpoints-in-use -->

| Endpoint | Value | Source | Flag |
|---|---|---|---|
| Planck PR3, as quoted by the PR4 paper | S8 = 0.834 ± 0.016 | arXiv:2309.10034 | [src: Sect. 6] |
| Planck 2018 TT,TE,EE + lowE; with lensing | S8 = 0.834 ± 0.016; 0.832 ± 0.013 | arXiv:1807.06209 | [src: Table 2] |
| Planck PR4 HiLLiPoP + LoLLiPoP | S8 = 0.819 ± 0.014 | arXiv:2309.10034 | [src: Sect. 6, Eq. 17] |
| P-ACT | S8 = 0.830 ± 0.014 | arXiv:2503.14452 | [src: Sect. VIII.4] |
| "Combined CMB" (Planck 2018 + ACT DR6 + SPT-3G primary, no CMB lensing, rerun with the DES priors) | S8 = 0.836 (+0.012/−0.013), Ω_m = 0.324 (+0.007/−0.012) | DES Collaboration 2026, arXiv:2601.14559; quoted in the review Pantos & Perivolaropoulos 2026, arXiv:2602.12238 | [src: Table 4 of arXiv:2601.14559] |
| CMB-SPA | σ8 = 0.8137 ± 0.0037, Ω_m = 0.3175 ± 0.0055 | arXiv:2506.20707 | [src: abstract; Sect. VII.2.2] |

The four S8 endpoints span 0.819 to 0.836, a range larger than the error of the best lensing measurement (0.012). A quoted "tension with the CMB" is not comparable between papers unless the endpoint is the same: KiDS-Legacy compares with the Planck Legacy marginal S8 = 0.834 ± 0.016 (arXiv:2503.19441) [src: Sect. 7], DES Y6 with Planck 2018 + ACT DR6 + SPT-3G DR1 primary anisotropies without CMB lensing (arXiv:2601.14559) [src: Sect. V.2]. Metrics also differ: KiDS quotes a Hellinger distance between marginals [src: Sect. 6]; DES the parameter-difference probability of Eqs. 17–19 of arXiv:2601.14559 in one, two or all shared dimensions [src: Sect. IV.6].

### 2.2 S8 by probe, with one common derived difference
<!-- key: s8-by-probe-with-one-common-derived-difference -->

The two columns of Gaussian differences against fixed CMB endpoints that stood in this table were computed by this skill and were removed on 2026-10-23 (set aside in `docs/history/set-aside/2026-10-23/cosmo-tensions-anomalies-results.md`). The tension column is the paper's own.

| Probe | S8 | Tension as printed by the paper | Citation | Flag |
|---|---|---|---|---|
| KiDS-Legacy cosmic shear | 0.815 (+0.016/−0.021) | 0.76σ in S8; 0.73σ in Σ8 = σ8(Ω_m/0.3)^0.58 = 0.821 (+0.014/−0.016); marginal Hellinger distance to Planck Legacy; 1.01σ in Σ8 with band powers | Wright et al. 2025, arXiv:2503.19441 | [src: Sect. 6, Sect. 7] |
| DES Y6 cosmic shear, NLA | 0.798 (+0.014/−0.015) | parameter shift against Planck + ACT + SPT primary: 2.0σ in S8, 1.1σ full space (p = 0.28); suspiciousness 0.9σ | DES Collaboration 2026, arXiv:2602.10065 | [src: abstract (S8); Sect. VI.2.1] |
| DES Y6 cosmic shear, TATT | 0.783 (+0.019/−0.015) | same metric: 2.3σ in S8, 1.7σ full space (p = 0.09); suspiciousness 1.4σ | arXiv:2602.10065 | [src: abstract (S8); Sect. VI.2.1] |
| DES Y6 3×2pt | 0.789 ± 0.012 | parameter shift against Planck + ACT + SPT primary: 2.6σ in S8, 2.2σ in S8–Ω_m, 1.8σ full space (1.5σ in Y3); 1.0σ full space against Planck 2018 alone | DES Collaboration 2026, arXiv:2601.14559 | [src: Sect. V.2, Table 4] |
| HSC Y3 shear, DESI clustering redshifts | 0.804 (+0.019/−0.018) | "towards Planck" | Choppin de Janvry et al. 2025, arXiv:2511.18134 | [src: abstract] |
| HSC Y3 photometric 3×2pt (one shape catalogue, pseudo-C_ℓ) | 68% interval 0.76 ≤ S8 ≤ 0.81 | none printed; consistent with the HSC Y3 shear analyses, about 25% tighter | Hamana et al. 2026, arXiv:2608.05530 | [src: abstract] |
| DES Y3 shear, external IA and baryon calibration | 0.832 (+0.013/−0.017) | posterior moves up by 1.5σ | Bigwood et al. 2025, arXiv:2512.04209 | [src: abstract] |
| unWISE × ACT DR6 + Planck lensing | 0.810 ± 0.015 | consistent with the primary CMB | Farren et al. 2023, arXiv:2309.05659 | [src: abstract] |
| DESI LRG × ACT DR6 + Planck PR4 lensing | 0.775 (+0.019/−0.022) | consistent with Planck primary CMB "at the ≃ 1.6–2.2σ level", amplitude lower | Sailer et al. 2024, arXiv:2407.04607 | [src: abstract] |
| tSZ × galaxies, compiled ⟨b P_e⟩(z), FLAMINGO model | 0.72 ± 0.03 | — | Salcido et al. 2026, arXiv:2605.11083 | [src: abstract] |
| eRASS1 cluster counts | 0.86 ± 0.01 | "consistent and at a similar precision with the state-of-the-art CMB measurements" | Ghirardini et al. 2024, arXiv:2402.08458 | [src: abstract] |
| SPT clusters + DES and HST lensing | 0.795 ± 0.029 | 1.1σ from Planck 2018 | Bocquet et al. 2024, arXiv:2401.02075 | [src: abstract] |
| Planck PSZ2 + DES shear + Chandra | 0.791 (+0.023/−0.021) | 1.6σ from the CMB; 2.9σ from eROSITA clusters | Aymerich et al. 2025, arXiv:2509.02068 | [src: abstract] |
| KiDS-1000 AMICO clusters | 0.74 ± 0.03 | 2.8σ from Planck | Lesci et al. 2025, arXiv:2507.14285 | [src: abstract] |
| KiDS-1000 AMICO cluster clustering (9049 clusters, 3D correlation multipoles) | 0.77 (+0.10/−0.08); Ω_m = 0.24 ± 0.02 | S8 in 1σ agreement with the AMICO counts; "a 2σ tension is reported in Ω_m" with Planck 2018 and AMICO KiDS-DR3 w(θ) | Romanello et al. 2026, arXiv:2610.31767 | [src: abstract (values); Sect. 5 (tension)] |

Further S8 values are held, with their identifiers and places, by the siblings: DES Y3 redMaPPer and XXL clusters (`cosmo-clusters`); DES Y3 shear × tSZ and DESI DR1 quasars × Planck lensing (`cosmo-cmb-lss-cross-correlations`); third-order shear from KiDS-Legacy, DES Y3 and HSC Y3 (`cosmo-beyond-two-point`, `cosmo-weak-lensing`); DESI DR1 full shape against BOSS EFT analyses (`cosmo-galaxy-clustering`); Tully–Fisher and SN velocities (`cosmo-peculiar-velocities`).

### 2.3 The internal spread is larger than the CMB tension
<!-- key: the-internal-spread-is-larger-than-the-cmb -->

The table of pairwise Gaussian differences that stood here was computed by this skill and was removed on 2026-10-23 (set aside in `docs/history/set-aside/2026-10-23/cosmo-tensions-anomalies-results.md`). What the papers state: eRASS1 clusters give S8 = 0.86 ± 0.01 (arXiv:2402.08458), KiDS-1000 AMICO clusters 0.74 ± 0.03 (arXiv:2507.14285), and the tSZ cross-correlation compilation 0.72 ± 0.03 (arXiv:2605.11083) [src: abstract of each]; the Planck PSZ2 cluster analysis finds itself "in significant tension with results from eROSITA clusters (2.9σ)" and in "very mild tension" (1.6σ) with the CMB (arXiv:2509.02068) [src: abstract]. Among cosmic-shear and 3×2pt results the largest printed distance from the CMB is 2.6σ projected on S8 (DES Y6 3×2pt, arXiv:2601.14559) [src: abstract].

"The S8 tension" in 2026 is therefore better described as a disagreement among low-redshift amplitude measurements with strong astrophysical modelling than as a lensing–CMB discrepancy.

### 2.4 What moved it and when
<!-- key: what-moved-it-and-when-2 -->

| When | What changed | Effect | Citation | Flag |
|---|---|---|---|---|
| 2020–2021 | KiDS-1000 and DES Y3 | the low-S8 era | values and identifiers in `cosmo-weak-lensing` `results.md` §3 | [sec: wl] |
| 2023 | Planck PR4 | Planck S8 falls from 0.834 ± 0.016 to 0.819 ± 0.014 | arXiv:2309.10034 | [src: Sect. 6, Eq. 17] |
| 2023–2024 | CMB-lensing tomography corrected (lensing normalisation, redshifts, neutrino consistency, projection effect) | unWISE × ACT + Planck 0.810 ± 0.015; DESI LRG × Planck 0.765 ± 0.023, "less discrepant with primary CMB measurements than previous DESI LRG cross Planck CMB lensing results", and 0.775 (+0.019/−0.022) with ACT + Planck | arXiv:2309.05659, arXiv:2407.04607 | [src: abstract of each] |
| 2025 | KiDS-Legacy: new redshift calibration | 0.815 (+0.016/−0.021); the increase in S8 over previous KiDS analyses "primarily results from our improved redshift distribution estimation and calibration" | arXiv:2503.19441 | [src: abstract] |
| 2025 | HSC Y3 with DESI clustering redshifts | 0.769 to 0.804 | arXiv:2511.18134 | [src: abstract] |
| 2025 | Planck clusters with DES shear mass calibration | 1.6σ from the CMB (the 2015 Planck cluster tension is held in `cosmo-clusters`) | arXiv:2509.02068 | [src: abstract] |
| 2026 | DES Y6 | shear 0.798 (NLA); 3×2pt 0.789 ± 0.012; the tightest lensing result remains 2.6σ low in S8 | arXiv:2602.10065, arXiv:2601.14559 | [src: abstract of each] |

## 3. CMB lensing anomaly A_L and optical depth
<!-- key: cmb-lensing-anomaly-al-and-optical-depth -->

### 3.1 Peak-smoothing amplitude
<!-- key: peak-smoothing-amplitude -->

Model: ΛCDM + A_L, one parameter. "Distance from 1" is the paper's own figure; "—" where the paper prints none (the values computed here as (A_L − 1)/σ were removed on 2026-10-23).

| Value | Data | Distance from 1 | Citation | Flag |
|---|---|---|---|---|
| 1.180 ± 0.065 | Planck PR3 Plik TT,TE,EE + lowE | 2.7σ (paper) | arXiv:1807.06209 | [src: Sect. 2.2.1] |
| 1.185 ± 0.067 (A_2pt, T and E, no φφ) | Planck PR3, SPT rerun | — | arXiv:2506.20707 | [src: Sect. VII.2.3] |
| 1.095 ± 0.056 | Planck PR4 CamSpec | 1.7σ (as quoted by ACT) | arXiv:2503.14452 | [src: Sect. VIII.5] |
| 1.039 ± 0.052 | Planck PR4 HiLLiPoP | 0.75σ (as quoted by ACT) | arXiv:2309.10034 | [src: Sect. 11.1] |
| 1.007 ± 0.057 | ACT DR6 | — | arXiv:2503.14452 | [src: Sect. VIII.5] |
| 1.081 ± 0.043 | P-ACT | "no evidence for excess lensing in the power spectrum" | arXiv:2503.14452 | [src: Sect. VIII.5; abstract] |
| A_2pt = 0.991 (+0.083/−0.10) (T and E); A_lens = 0.972 (+0.079/−0.089) with A_2pt = A_recon | SPT-3G D1 | — | arXiv:2506.20707 | [src: Sect. VII.2.3, Eq. 67] |
| A_2pt = 1.016 (+0.048/−0.054) | SPT + ACT, T and E spectra | — | arXiv:2506.20707 | [src: Sect. VII.2.3] |
| A_2pt = 1.079 ± 0.038, A_recon = 1.041 ± 0.031; A_lens = 1.052 ± 0.032 coherent | CMB-SPA | 1.6σ in the (A_2pt, A_recon) plane (paper) | arXiv:2506.20707 | [src: Sect. VII.2.3, Eq. 69] |

A_2pt rescales the lensing power used to smooth the T and E spectra and leaves the predicted reconstruction amplitude unchanged; A_recon does the reverse; A_lens ties them (arXiv:2506.20707) [src: Sect. VII.2.3]. The ground-based TT posterior mean (SPT + ACT, A_2pt = 1.014 ± 0.098) lies 2.3 standard deviations below Planck TT (1.239 ± 0.095); SPT gives no consistency statistic because ACT and Planck are correlated, and "cannot make a definitive judgment" on whether the Planck feature is cosmological [src: Sect. VII.2.3].

Lensing reconstructions show no excess: ACT DR6 + SPT-3G + Planck PR4 give a reconstruction amplitude 1.025 ± 0.017 relative to the Planck–ACT best fit (Qu et al. 2025, arXiv:2504.20038) [src: abstract], and the SPT-3G D1 quadratic-estimator amplitude is consistent with unity at 2% relative to the CMB-SPA best fit (Omori et al. 2026, arXiv:2608.31136) [src: abstract]. Motloch & Hu 2019 (arXiv:1912.06601) quantified the Planck legacy smoothing, in a model-independent lensing-potential analysis, as 2σ high relative to the lensing reconstruction and 2.8σ high relative to the ΛCDM expectation from the unlensed information; with reconstruction in the ΛCDM parameters the tension is 2.1σ, with BAO and Pantheon added 2.2σ; the largest change from the previous release came from the tighter τ [src: abstract].

What moved it: PR4 reprocessing and likelihoods (2022–2023), then ACT DR6 and SPT-3G D1 (2025), which do not show the oscillatory TT residual at 1000 < ℓ < 2000 that drives the Planck value (arXiv:2503.14452) [src: Sect. VIII.5]. It survives at about 2σ only in combinations that keep the full Planck TT range.

### 3.2 Optical depth
<!-- key: optical-depth -->

Rows without a place [sec: cmb, `results.md` §5 and `open-questions.md` §1].

| τ | Data | Citation |
|---|---|---|
| 0.0506 ± 0.0086 | Planck 2018 lowE alone | arXiv:1807.06209 [src: Eq. 2] |
| 0.054 ± 0.007 (0.0544 ± 0.0073); 0.0496 to 0.0561 with errors 0.0071 to 0.0090 across the other columns (TT, TE or EE + lowE; + BAO) | Planck 2018 TT,TE,EE + lowE + lensing | arXiv:1807.06209 [src: Table 2] |
| 0.058 ± 0.006 | Planck PR4 LoLLiPoP + HiLLiPoP | arXiv:2309.10034 [src: Eq. 14] |
| 0.053 (+0.018/−0.019) | CLASS 90 GHz × Planck, ground-based | Li et al. 2025, arXiv:2501.11904 [src: abstract] |
| 0.090 ± 0.012 | DESI BAO + high-ℓ CMB + CMB lensing, no low-ℓ EE | Sailer et al. 2025, arXiv:2504.16932 [src: abstract] |
| 0.091 ± 0.011 | CMB without low-ℓ EE and lensing constraints, Σm_ν = 0.06 eV | Jhaveri et al. 2025, arXiv:2504.21813 [src: abstract] |
| 0.0552 (+0.0019/−0.0026 stat) (+0.0075/−0.0049 sys) | Planck without low-ℓ EE + reionisation history from Lyα forest and damping wings; leaves 2.4σ with DESI DR2 BAO | Kageura et al. 2026, arXiv:2601.09644 [src: abstract] |
| total τ ~ 0.073 with a dark-ages contribution Δτ_burst ~ 0.012 (0.001 < Δτ_burst < 0.022 at 95%), preferred at about 2–2.5σ, for PR3 and PR4 likelihoods alike | a redshift-localised early reionisation burst (z ~ 45 to ~ 165 depending on the high-ℓ likelihood), which adds less to low-ℓ polarisation than late sources | Weiner et al. 2026, arXiv:2610.12552 [src: abstract] |
| τ ≃ 0.08–0.10 "compatible with the data" | Planck low-ℓ EE, BB, EB with ALP birefringence much larger at reionisation than at recombination, energy injected at 10 ≲ z ≲ 100 | Sirletti, Namikawa & Sherwin 2026, arXiv:2610.29764 [src: abstract] |

Size: the BAO-preferred value is in "≃ 3–5σ tension with Planck low-ℓ polarization data when taken at face value": about 5σ at face value, about 3.8σ "when accounting for the prior width", one parameter (arXiv:2504.16932) [src: abstract, note 72]. Every Planck reprocessing from 2018 to 2023 lies in 0.051–0.063 [sec: cmb], with uncertainties that depend on the likelihood and data combination (0.0086 for lowE alone, 0.0073 with TT,TE,EE and lensing, 0.006 for PR4) [src: Eq. 2 and Table 2 of arXiv:1807.06209; Eq. 14 of arXiv:2309.10034]. The τ question is not an anomaly in a measurement; it is the statement that one parameter, measured by one instrument, would absorb the CMB–BAO mismatch if it were wrong; the authors call it a "single-point failure" (arXiv:2504.16932) [src: abstract]. Two 2026 models keep the Planck low-ℓ data and still allow a higher τ, by hiding part of it from the EE reionisation bump: an early burst of ionisation (arXiv:2610.12552) and a reionisation-era birefringence rotation that suppresses EE (arXiv:2610.29764) [src: abstract of each]; both are model fits, not measurements of τ.

## 4. CMB-DESI discrepancy within LCDM
<!-- key: cmb-desi-discrepancy-within-lcdm -->

The compared data are DESI DR2 BAO and the named CMB data, in ΛCDM, in the Ω_m–h r_d plane; each paper converts a two-parameter difference to a one-dimensional Gaussian equivalent. DESI writes it as χ² = (p_A − p_B)ᵀ(Cov_A + Cov_B)⁻¹(p_A − p_B) for p = (Ω_m, r_d h), converted through its probability to exceed (arXiv:2503.14738) [src: Eq. 18].

| CMB data | Distance from DESI DR2 | Citation | Flag |
|---|---|---|---|
| P-ACT, or P-ACT + lensing | 1.6σ | arXiv:2503.14452 | [src: App. H, Fig. 43] |
| ACT DR6 + lensing, Planck SRoll2 τ | 2.8σ, "partly driven by the τ measurement" | arXiv:2503.14452 | [src: App. H] |
| DESI's own CMB combination (Planck + ACT lensing) | 2.3σ (1.9σ in DR1); 2.0σ without CMB lensing | arXiv:2503.14738 | [src: Sect. VI] |
| CMB as summarised by Sailer et al. | 2.2σ | arXiv:2504.16932 | [sec: cmb] |
| SPT-3G D1 alone | 2.5σ | arXiv:2506.20707 | [src: Sect. VII.3] |
| ACT DR6 with ACT lensing only, SPT rerun | 3.1σ (2.7σ with Planck lensing and the ACT τ prior) | arXiv:2506.20707 | [src: Sect. VII.3] |
| CMB-SPA | 2.8σ | arXiv:2506.20707 | [src: Sect. VII.3] |
| SPT + Planck | 3.0σ | arXiv:2506.20707 | [src: Sect. VII.3] |
| SPT + ACT | 3.7σ | arXiv:2506.20707 | [src: Sect. VII.3] |

DESI judges 2.3σ "not close to 3σ" and therefore combines DESI and CMB in ΛCDM (arXiv:2503.14738) [src: Sect. VI]. In parameters: DESI BAO alone give Ω_m = 0.2975 ± 0.0086 and h r_d = 101.54 ± 0.73 Mpc (arXiv:2503.14738) [src: Eq. 17]; SPT-3G D1 gives Ω_m = 0.3247 ± 0.0091 and h r_d = 97.9 ± 1.1 Mpc [src: Sect. VII.3 of arXiv:2506.20707]; Planck (SPT rerun) 0.3145 ± 0.0067, ACT DR6 0.330 ± 0.010 and CMB-SPA 0.3175 ± 0.0055 [sec: cmb]. The ground-based experiments prefer a higher Ω_m than Planck, and adding Planck's large angular scales to SPT + ACT lowers Ω_m, which is why the discrepancy is larger without Planck [src: Sect. VII.3 of arXiv:2506.20707]. DESI also finds Ω_m from DESI and from supernovae discrepant in ΛCDM at 1.7σ (Pantheon+), 2.1σ (Union3) and 2.9σ (DESY5) and does not combine them in ΛCDM [src: Sect. VI of arXiv:2503.14738].

The same mismatch is what four different extensions absorb (Sect. 3.2; Sect. 5; Sect. 6; Sect. 11): a higher τ, evolving dark energy, a negative effective neutrino mass, or positive Ω_K. They are four readings of one discrepancy, not four anomalies; see `open-questions.md` §1.

What moved it: DESI DR1 to DR2 (smaller BAO errors, same direction); ACT DR6 and SPT-3G D1 in 2025 (higher Ω_m on the CMB side); the 2026 SPT-3G D1 lensing reconstruction, with which the curvature and w0wa preferences from CMB-SPA + DESI DR2 drop to about 2σ and Σm_ν < 0.072 eV in ΛCDM (arXiv:2608.31136) [src: abstract].

## 5. Dynamical dark energy preference
<!-- key: dynamical-dark-energy-preference -->

### 5.1 Frequentist significance by combination
<!-- key: frequentist-significance-by-combination -->

A model preference, not a tension: Δχ²_MAP of w0waCDM against ΛCDM converted to a frequentist significance "given 2 extra free parameters", with ΔDIC alongside (arXiv:2503.14738) [src: Table 6]. "CMB" in DESI papers includes CMB lensing.

| Combination | Significance | Status | Citation | Flag |
|---|---|---|---|---|
| DESI DR2 BAO alone; + Pantheon+; + Union3; + DESY5 | 1.7σ (Δχ² = −4.7); 1.7σ; 2.7σ; 3.3σ | current (supernova rows superseded by the recalibrations below) | arXiv:2503.14738 | [src: Table 6] |
| DESI DR2 + compressed CMB priors (θ*, ω_b, ω_bc) | 2.4σ (−8.0) | current | arXiv:2503.14738 | [src: Table 6] |
| DESI DR2 + CMB without lensing | 2.7σ (−9.7) | current | arXiv:2503.14738 | [src: Table 6] |
| DESI DR2 + CMB | 3.1σ (−12.5), ΔDIC = −8.7 | current | arXiv:2503.14738 | [src: Table 6] |
| DESI BAO + high-ℓ CMB + lensing, τ prior 0.06 or 0.09 in place of Planck low-ℓ | 2.8σ (−10.75); 1.4σ (−3.82) | current | Sailer et al. 2025, arXiv:2504.16932 | [src: Sect. III.2] |
| DESI DR2 + CMB + Pantheon+ / Union3 / DESY5 | 2.8σ / 3.8σ / 4.2σ | superseded | arXiv:2503.14738 | [src: Table 6] |
| DESI DR2 + CMB + DES-Dovekie | 3.2σ, "reduced from 4.2σ" | current, DES's own paper | Popovic et al. 2025, arXiv:2511.07517 | [src: abstract] |
| DESI DR2 + Planck + corrected Pantheon+ / Union3.1 / DES-Dovekie | 3.2σ / 3.4σ / 3.4σ | current, rerun "exactly as done by DESI DR2" | Hoyt et al. 2026, arXiv:2601.19424 | [src: abstract] |
| Unite (2884 SNe) + CMB + DES and DESI BAO | 3.3σ (MAP), 3.1σ (maximum likelihood) | current | Camilleri et al. 2026, arXiv:2609.05053 | [src: abstract] |
| DES Y6 SN + BAO + 3×2pt alone | 2.2σ | current | DES Collaboration 2026, arXiv:2605.27221 | [src: abstract] |
| DES Y6 + DESI DR2 BAO + primary CMB | 3.0σ; 2.6σ without SNe; 3.4σ with Σm_ν free (through the Σm_ν–wa degeneracy) | current | arXiv:2605.27221 | [src: abstract] |
| DESI DR1 P + B + DR2 BAO + CMB; + DES-Dovekie | 2.8σ; 3.1σ, "driven primarily by the CMB"; DESI + DES-Dovekie without CMB 1.6σ | current | Forero-Sánchez et al. 2026, arXiv:2606.23936 | [src] |
| DESI DR1 P + B + DR2 BAO, DESI only | within 1σ of Λ | current | arXiv:2606.23936 | [src] |
| TDCOSMO-2026 + SLACS + SL2S + DESI DR2 + DES-Dovekie | w = −1 disfavoured at 2.3–2.5σ in wCDM, w0waCDM and w_φCDM; w0 = −0.85 (+0.07/−0.06), w_a = −0.48 (+0.46/−0.44) in w0waCDM | current | arXiv:2610.14781 | [src: abstract] |

Pivot: for DESI + CMB + DESY5, w_p = −0.954 ± 0.024 at z_p = 0.31; the signal is a slope, not an offset [sec: de], and "allowing w(z) to vary does not help resolve the so-called Hubble tension": the w0waCDM H0 is below the Planck ΛCDM value (arXiv:2503.14738) [src: Sect. VII.1].

### 5.2 Bayesian evidence on the same data
<!-- key: bayesian-evidence-on-the-same-data -->

ln B = ln Z(w0wa) − ln Z(Λ); positive favours w0wa.

| Combination | ln B | Analysis | Flag |
|---|---|---|---|
| DESI DR2 + CMB | −0.57 ± 0.26 (−0.38 ± 0.25 without CMB lensing; DESI alone −1.47 ± 0.11) | Ong, Yallup & Handley 2025, arXiv:2511.10631 | [src: Table 1] |
| DESI DR2 + CMB + Pantheon+ | −0.66 ± 0.44 (−1.70 ± 0.26 in arXiv:2511.10631) | Lodha et al. 2025, arXiv:2503.14743 | [src: App. A, Table 4; Table 1 of arXiv:2511.10631] |
| DESI DR2 + CMB + Union3 | 3.03 ± 0.44 (+1.37 ± 0.27 in arXiv:2511.10631) | arXiv:2503.14743 | [src: App. A, Table 4; Table 1 of arXiv:2511.10631] |
| DESI DR2 + CMB + DESY5 (original) | 4.88 ± 0.44 | arXiv:2503.14743 | [src: App. A, Table 4] |
| DESI DR2 + CMB + DES-SN5YR (original) | +3.32 ± 0.27, an upper bound of 3.07 ± 0.10σ | arXiv:2511.10631 | [src: Table 1] |
| DESI DR2 + CMB + DES-Dovekie | −0.30 ± 0.19 | arXiv:2511.10631 | [src: Table 1] |
| DESI DR2 + CMB + DES-Dovekie | odds "approximately 5:1" in favour of w0waCDM, stated as equivalent to the 3.2σ | arXiv:2511.07517 | [src: abstract] |
| Unite + CMB + BAO | "only weak preference" | arXiv:2609.05053 | [src: abstract] |
| DESI DR2 + Planck 2018 (no CMB lensing), uniform prior: BAO + CMB; + DESY5; + DES-Dovekie; + Union3; + Pantheon+ | −0.06 ± 0.18; 3.65 ± 0.21; 0.33 ± 0.21; 2.34 ± 0.19; −1.05 ± 0.21 | Layton, Hall & Robertson 2026, arXiv:2610.26493 | [src: Sect. 4.2, Table 4] |
| Same combinations, Jeffreys prior on the parameters | −11.54 ± 0.18; −5.52 ± 0.21; −9.18 ± 0.21; −10.68 ± 0.19; −10.57 ± 0.21: "all combinations strongly support ΛCDM" | arXiv:2610.26493 | [src: Sect. 4.2, Table 4] |

The two evidence analyses differ for every supernova sample (DESY5: 4.88 against 3.32; Union3: 3.03 against 1.37; Pantheon+: −0.66 against −1.70; DES-Dovekie: odds of about 5:1 for w0wa in arXiv:2511.07517 against −0.30 in arXiv:2511.10631). Both use PolyChord and DESI's w0, wa priors; DESI substitutes H0 for θ_MC as a sampled parameter (arXiv:2503.14743) [src: App. A], and Ong et al. use Planck 2018 with CamSpec and convert ln B to an upper bound on the significance through B ≤ −1/(e p ln p) and σ = Φ⁻¹(1 − p/2) (arXiv:2511.10631) [src: Sect. II, Eqs. 1, 2]. Neither paper states the cause of the difference, and this file does not reconcile it. Quote the paper, not "the Bayes factor". DESI's own caution: a wider prior on w0, wa favours ΛCDM, but reversing the DESY5 ranking would need a prior range more than ten times wider in both parameters (arXiv:2503.14743) [src: App. A]. A Jeffreys prior does reverse it: the w0, wa posteriors barely move, but the larger Occam penalty turns every combination to ΛCDM; the authors state that this does not show evolving dark energy excluded, only that the evidence "should not be interpreted independently of the prior specification" (arXiv:2610.26493) [src: abstract; Sect. 4.2].

Where the Bayesian preference comes from according to arXiv:2511.10631: a 2.95 ± 0.04σ tension between DESI DR2 and DES-SN5YR within ΛCDM, above the authors' 2.88σ look-elsewhere threshold and the only pair with a negative evidence ratio (log R ≈ −0.17) [src: abstract, Sect. III]; reduced to 1.96 ± 0.04σ with DES-Dovekie [sec: stat].

### 5.3 What moved it and when
<!-- key: what-moved-it-and-when -->

| Date | Event | Pantheon+ / Union3 / DES | Citation | Flag |
|---|---|---|---|---|
| Apr 2024 | DESI DR1 BAO | "∼2.5σ to ∼3.9σ depending on the combination of datasets", as summarised by DESI DR2 | arXiv:2503.14738 | [src: Sect. I] |
| Mar 2025 | DESI DR2 BAO | 2.8σ / 3.8σ / 4.2σ | arXiv:2503.14738 | [src: abstract; Table 6] |
| Nov 2025 | DES-Dovekie recalibration and colour-law fix | DES: 3.2σ | arXiv:2511.07517 | [src: abstract] |
| Jan 2026 | Union3.1; Pantheon+ host masses corrected | 3.2σ / 3.4σ / 3.4σ | arXiv:2601.19424 | [src: abstract] |
| May 2026 | DES Y6 all probes + DESI DR2 + CMB | 3.0σ | arXiv:2605.27221 | [src: abstract] |
| Jun 2026 | DESI DR1 bispectrum | weakens the preference | arXiv:2606.23936 | [sec: de] |
| Sep 2026 | Unite | 3.3σ | arXiv:2609.05053 | [src: abstract] |
| Oct 2026 | Jeffreys prior on the evidence | ln B negative for every supernova sample | arXiv:2610.26493 | [src: Table 4] |

The spread between supernova samples has narrowed, from 2.8σ to 4.2σ in March 2025 (arXiv:2503.14738) to 3.2σ (Pantheon+), 3.4σ (Union3.1) and 3.4σ (DES-Dovekie) after the recalibrations, "a significantly improved consistency between SN analyses" (arXiv:2601.19424) [src: abstract of each].

## 6. Negative effective neutrino mass
<!-- key: negative-effective-neutrino-mass -->

Rows without a place [sec: nu, `results.md` §1.4 and `open-questions.md` §1.1].

| Quantity | Value | Data and model | Citation |
|---|---|---|---|
| Σm_ν, 95% upper limit | < 0.0642 eV, marginalised σ = 0.020 eV [src: abstract] | DESI DR2 BAO + CMB, ΛCDM | Elbers et al. 2025, arXiv:2503.14744 |
| Σm_ν, 95% upper limit | < 0.163 eV [src: abstract] | same, w0waCDM | arXiv:2503.14744 |
| Effective signed mass | −0.101 (+0.047/−0.056) eV; 0.000 (+0.10/−0.081) eV in w0waCDM [src: Table 5] | DESI DR2 BAO + CMB, ΛCDM | arXiv:2503.14744 |
| Tension with the oscillation minimum (0.059 eV normal ordering), one parameter, against a uniform terrestrial prior 0.059–1.2 eV | 2.7σ goodness-of-fit loss (Δχ²_MAP = −7.2), 4.0σ parameter shift, 3.0σ probability to exceed; DESI + CMB without lensing 2.5σ, 3.6σ, 2.7σ; CMB alone 1.5σ, 2.5σ, 1.6σ [src: Sect. V.3, Table 4, Eqs. 37–38] | same | arXiv:2503.14744 |
| Same tension on DR1 | 2.8–3.3σ [src: abstract] | Planck + ACT + DESI DR1 | Elbers et al. 2024, arXiv:2407.10965 |
| Effective mass with two lensing amplitudes free | −0.018 (+0.085/−0.089) eV [src: abstract] | Planck, Planck + ACT lensing, DESI | Cozzumbo et al. 2025, arXiv:2511.01967 |
| Tension with τ fixed at 0.067 or 0.074 (2σ or 3σ above 0.054 ± 0.007) | 2.3σ or 1.7σ [src: Sect. V.2.1] | DESI DR2 BAO + CMB | arXiv:2503.14744 |
| Effective mass with a τ prior 0.06 or 0.09 replacing Planck low-ℓ | −0.08 (+0.05/−0.06) eV, about 2.4σ; 0.01 ± 0.06 eV, about 0.9σ [src: Sect. III.1] | DESI BAO + high-ℓ CMB + lensing | arXiv:2504.16932 |
| Mass split into a geometry channel (H(z) for distances) and a growth channel (H(z) for perturbations), both allowed negative | Σm_ν^geo = −0.07 ± 0.10 eV, Σm_ν^growth = −0.13 (+0.10/−0.12) eV (68%); their difference, a null test of ΛCDM, passed at 0.4σ [src: abstract] | Planck primary CMB + Planck, ACT and SPT lensing + DESI BAO | Ge et al. 2026, arXiv:2610.20977 |

The tension vanishes in w0waCDM, where the mass returns to 0.06 (+0.15/−0.10) eV (arXiv:2407.10965), with free lensing amplitudes, or with τ ≈ 0.09 (arXiv:2504.16932, arXiv:2504.21813) [sec: nu, de]. What moved it: DESI DR1 (2024) created it; DR2 kept it at 3σ; no data release has removed it. It is not an independent anomaly (Section 4).

## 7. Cosmic dipole
<!-- key: cosmic-dipole -->

Reference endpoint: the CMB temperature dipole read as kinematic, v/c = 0.00123, v = 369 km/s (Planck Collaboration 2013, arXiv:1303.5087) [src], propagated to a number-count dipole with the Ellis & Baldwin 1984 formula (doi:10.1093/mnras/206.2.377; `physics-and-methods.md` §6). All rows [src]: abstracts read on 2026-10-10, body places added on 2026-10-16. The "σ" of the table rows are not one metric: a mock p-value (Secrest, Bashir), an amplitude ratio over its error (Böhme), a Bayesian evidence ratio (Dam, Land-Strykowski), a parameter difference (Dam Sect. 3.4).

### 7.1 Number-count dipoles against the kinematic expectation
<!-- key: number-count-dipoles-against-the-kinematic -->

| Result | Data | Method | Citation |
|---|---|---|---|
| Amplitude "over twice as large as expected"; p = 5 × 10⁻⁷, 4.9σ one-sided; direction similar to the CMB dipole. Body: D = 0.01554 towards (l, b) = (238.2°, 28.8°), 27.8° from the CMB dipole, against an expected ∼0.007 from Eq. 1; five of 10⁷ kinematic-null simulations exceed it in amplitude within the observed angular distance; mask changes move the amplitude by ≲ 5% [src: Sect. IV] | 1,355,352 CatWISE2020 quasars, flux-limited, all-sky; mean spectral index 1.26 [src: Sect. II] | p-value of the measured dipole under the purely kinematic null, shot noise only | Secrest et al. 2021, arXiv:2009.14826 |
| Radio p = 8.9 × 10⁻³ (2.6σ); quasars p = 1.2 × 10⁻⁵ (4.4σ); joint 5.1σ; no evidence for frequency dependence | NVSS radio galaxies and WISE quasars, no shared objects | statistic including the directional offset; sample-size-weighted Z-scores [src: abstract] | Secrest et al. 2022, arXiv:2206.05624 |
| Amplitude 2.7 times the kinematic expectation, 5.7σ; Galactic mask leaks dipole power to higher multipoles and worsens the discrepancy; source evolution helps "only mildly". Against the ΛCDM prior on the amplitude including clustering, the parameter-difference probability (their Eq. 26, after Raveri & Hu) gives 5.8σ, 5.5σ, 4.3σ or 2.1σ depending on the smoothing scale R, and 3.8σ (3.6σ with source evolution) when marginalising over halo masses 10¹²–10¹⁵ h⁻¹ M_⊙ [src: Sect. 3.4] | same 1.36 million quasars | Bayesian evidence for the amplitude; parameter difference for the tension | Dam, Lewis & Brewer 2023, arXiv:2212.07733 |
| All four radio amplitudes exceed the expectation and increase with decreasing frequency | TGSS-ADR1, WENSS, SUMSS, NVSS, one masking strategy | quadratic estimator, validated on simulations with 10⁷ sources [src: abstract] | Siewert, Schmidt-Rubart & Schwarz 2021, arXiv:2010.08366 |
| Residual, non-kinematic dipole D_resid = (0.81 ± 0.14) × 10⁻², offset by 39° ± 8° from the CMB dipole, with the kinematic part fixed to the CMB expectation; a common direction of the two components is disfavoured | NVSS + RACS + CatWISE, joint fit | Bayesian model selection [src: abstract] | Wagenveld et al. 2025, arXiv:2503.02470 |
| Dipole 3.67 ± 0.49 times the kinematic expectation, 5.4σ in amplitude; direction (5° ± 10°) from the CMB dipole; RACS-low + NVSS alone: 4.8σ with a Poisson estimator, 4.5σ with the negative-binomial one | NVSS + RACS-low + LoTSS-DR2 | negative-binomial counts for multi-component sources [src: abstract; Table 3] | Böhme et al. 2025, arXiv:2509.16732 |
| CatWISE against Planck ≈ 5.7σ; ≈ 6.7σ with a forward model of the CatWISE Eddington bias | Planck, NVSS, RACS, CatWISE | neural ratio estimation of the evidence ratio R, converted to σ through the distribution of log R over matched ("in concordance") simulations, one-sided (Eq. 6, following Bevins, Handley & Gessey-Jones 2024, arXiv:2407.15478) [src: Sect. 2.3] | Land-Strykowski et al. 2026, arXiv:2607.25703 |
| Significance revised to 3.63σ without a clustering dipole, 3.44σ with a randomly oriented one, 3.27σ with one aligned with the kinematic dipole; the shot-noise-only mocks of 2021 reproduce 4.82σ; with every input pushed to its most extreme plausible value, 2.93σ [src: Sect. VI, Table 1] | CatWISE2020 quasars, observed D = 15.54 × 10⁻³ | fraction of 10⁵ FLASK lognormal mocks with clustering, radial selection, exact sky coverage that reach D_obs | Bashir, Chingangbam & Appleby 2025, arXiv:2511.00822 |

The review by the discovering group states that the discrepancy "now exceeds 5σ" (Secrest et al. 2025, arXiv:2505.23526) [src].

### 7.2 Measurements that agree with the CMB velocity
<!-- key: measurements-that-agree-with-the-cmb-velocity -->

| Result | Data | Citation | Flag |
|---|---|---|---|
| 384 ± 78 (stat) ± 115 (syst) km/s along (l, b) = (264°, 48°), from aberration and modulation of the CMB anisotropies | Planck 2013 | arXiv:1303.5087 | [src: abstract] |
| v = 357.95 (+55.05/−48.47) km/s from the redshift dipole of quasars, against 369.82 ± 0.11 km/s from the CMB; the number-count dipole of the same catalogues is "significantly enhanced", attributed by the authors to leakage of large-scale power and footprint incompleteness | DESI DR1 BGS, LRG, ELG, QSO, 0.1 < z < 2.1; 1,000 EZmocks | Wu & Xia 2026, arXiv:2608.30914 | [src: abstract] |
| Upper limits on the bulk flow at 200–2000 h⁻¹Mpc consistent with ΛCDM, in "strong tension" with a ~370 km/s flow at R ~ 1000 h⁻¹Mpc | kSZ velocity reconstruction, Planck × WISE×SuperCOSMOS and unWISE | arXiv:2605.12499 | [src: abstract] |

### 7.3 Supernova dipole
<!-- key: supernova-dipole -->

The dipole of the low-redshift Pantheon+SH0ES supernovae "does not agree with the one inferred from the velocity of the solar system as obtained from CMB data", which its authors read as bulk velocities; a monopole and a quadrupole of similar amplitude are also detected, the monopole only at very low redshift (Sorrenti, Durrer & Kunz 2024, arXiv:2403.17741) [src]. The sibling `cosmo-peculiar-velocities` holds the counter-evidence: zero-point dipoles in CF4 and Pantheon+ are better described by local flow structure than by anisotropic expansion (arXiv:2509.14997) [sec: pv].

### 7.4 Size, metric, endpoint, history
<!-- key: size-metric-endpoint-history -->

- Metric: p-value of the observed amplitude (and direction) under the null of a purely kinematic dipole with the CMB velocity, from mock skies; or a Bayesian evidence ratio. The endpoint depends on the sample through its count slope x and spectral index α, so each catalogue has its own expected amplitude.
- Size at the snapshot: for the CatWISE2020 quasars, 3.63σ (no clustering dipole), 3.44σ (random) or 3.27σ (aligned) with clustering-aware mocks against 5.7σ in the Bayesian analysis, depending on whether a clustering dipole and mode coupling are simulated (2.9σ with extreme mock inputs, arXiv:2511.00822; 5.8σ, 5.5σ, 4.3σ or 2.1σ against the ΛCDM amplitude prior depending on the smoothing scale, arXiv:2212.07733) [src: Sect. VI; Sect. 3.4]; 5.4σ for three radio surveys combined; one direct velocity measurement from redshifts and one from CMB aberration that agree with 370 km/s.
- What moved it: 2020–2021, CatWISE (4.9σ, arXiv:2009.14826); 2022, joint radio + quasar (5.1σ, arXiv:2206.05624); 2023, Bayesian reanalysis (5.7σ, arXiv:2212.07733); 2025, radio with overdispersion (5.4σ, arXiv:2509.16732) and a clustering-aware reassessment (3.63σ, 3.44σ or 3.27σ by clustering dipole, arXiv:2511.00822); 2026, DESI redshift dipole consistent with the CMB (arXiv:2608.30914) [src: abstract of each].

## 8. Bulk flow
<!-- key: bulk-flow -->

Rows without a place [sec: pv, `results.md` §3]. A bulk flow is defined only with its estimator, window and depth.

| Measurement | Amplitude (km/s) | ΛCDM expectation or verdict | Citation |
|---|---|---|---|
| CF4, minimum variance, top-hat, 150 h⁻¹Mpc | 387 ± 28 | expectation 139; χ² = 19.34 for 3 degrees of freedom, probability 0.023% [src: Sect. 7, Table 1] | Watkins et al. 2023, arXiv:2302.02028 |
| CF4, same, 200 h⁻¹Mpc | 419 ± 36 | expectation 120; χ² = 29.13, probability 0.00021% (table), "less than 0.003%" (abstract); "does not quite reach 5σ" in the authors' words [src: Sect. 7, 8] | arXiv:2302.02028 |
| CF4, minimum variance, mock-calibrated errors, 173 h⁻¹Mpc | 428 ± 108 | probability 0.11% "of obtaining a larger χ²"; with the maximum-likelihood estimator 408 ± 165 at 49 h⁻¹Mpc, "in reasonable agreement" [src: abstract] | Whitford, Howlett & Davis 2023, arXiv:2306.11269 |
| CF4, monopole + dipole in six radial bins to 300 h⁻¹Mpc | 628 ± 82 in the 120–160 h⁻¹Mpc bin | ΛCDM prediction for the actual positions and weights; full range 2.29σ (dipole), 2.36σ (joint), four bins to 160 h⁻¹Mpc 2.34σ and 2.42σ [src: abstract]; peak bin 3.40σ, 1.56σ without 6dFGS, 3.77σ without SNe; the SN and 6dFGS dipoles are "mutually consistent in a covariance-aware comparison" [src] | Nusser & Tully 2026, arXiv:2608.14265 |
| CF4 TF, 2MTF, SFI++, Pantheon+ at z < 0.05, forward model | bulk-flow curve | "fully consistent with expectations from the standard cosmological model" [src: abstract] | Stiskalek, Desmond & Lavaux 2025, arXiv:2509.14997 |
| kSZ velocity reconstruction, 200–2000 h⁻¹Mpc | upper limits | consistent with ΛCDM; "strong tension" with reading the CatWISE quasar dipole as a ~370 km/s flow at R ~ 1000 h⁻¹Mpc [src: abstract] | Gandhi et al. 2026, arXiv:2605.12499 |

Metric and endpoint: χ² of the three flow components against the ΛCDM velocity covariance for the same window. What moved it: the minimum-variance amplitudes of the table did not move much between analyses; the quoted probability rose from 0.00021% (arXiv:2302.02028) [src: Sect. 7, Table 1] to 0.11% when errors were calibrated on mocks (arXiv:2306.11269) [src: abstract], and a shell analysis with the ΛCDM prediction computed for the actual positions gives 2.29σ for the dipole over the full range (arXiv:2608.14265) [src: abstract].

## 9. Large-angle CMB anomalies
<!-- key: large-angle-cmb-anomalies -->

Reference endpoint: Gaussian, statistically isotropic ΛCDM skies simulated with the instrument and mask of the data. Metric: the p-value (lower- or upper-tail probability) of a summary statistic among those simulations. All of these statistics were defined after the features were seen in WMAP or Planck temperature maps, so every p-value is a posteriori. All rows [src], abstracts read on 2026-10-10 unless a section is named; body places added on 2026-10-16.

| Anomaly | Size | Data | Citation |
|---|---|---|---|
| All temperature anomalies together | individual p-values "in the per mille to per cent level" | WMAP and Planck 2013–2015 | Schwarz et al. 2016, arXiv:1510.07929 |
| Temperature anomalies in the final Planck collaboration analysis | "confirm the presence of several so-called anomalies on large angular scales"; in polarisation "no unambiguous detections … of anomalies corresponding to those seen in temperature" | Planck 2018 (PR3), four component-separated maps | Planck Collaboration 2019, arXiv:1906.02552 |
| Lack of power at large angular scales | lower-tail probability ≤ 0.33% in PR3 and ≤ 1.76% in PR4, depending on the component-separation method; the two releases differ significantly once polarisation is included | Planck PR3 and PR4, temperature-only estimator | Billi, Barreiro & Martínez-González 2023, arXiv:2312.09989 |
| Lack of correlation, quadrupole–octopole alignment, hemispherical asymmetry | "detected at a similar level to the previous releases" in PR4; thermal and kinetic SZ from the local Universe have negligible impact | Planck PR4; constrained hydrodynamical simulation of a 500 h⁻¹Mpc box | Jung et al. 2024, arXiv:2406.11543 |
| Hemispherical asymmetry as clustering of local bandpower directions | clustering probability below 1% for multipoles between 200 and 2000 in temperature, a wider range than in PR3; no significant clustering in E modes | Planck PR4, end-to-end simulations | Gimeno-Amo et al. 2025, arXiv:2504.05597 |
| Dipolar variation of cosmological parameters across the sky | a dipole in A_s as large as observed in 5 of 600 simulations, aligned with the hemispherical asymmetry; other parameters consistent with ΛCDM | Planck PR4, TT + EE | arXiv:2504.05597 |
| Four statistics jointly: S_1/2 (large-angle correlation), R^TT (odd over even low-ℓ power), σ²_16 (variance in the ecliptic north), S_QO (quadrupole–octopole alignment) | joint probability "likely ≤ 3 × 10⁻⁸", with little correlation among the four. Body: each p ≲ 5% against 10⁸ Planck-best-fit ΛCDM skies, counted in the direction of the data; pairwise p-values exceed the product of single ones by a factor ≃ 30 only for (S_1/2, σ²_16), close to 1 otherwise [src: Results, Table 1] | Planck temperature, four component-separated maps | Jones et al. 2023, arXiv:2310.12859 |
| The same joint probability after a look-elsewhere correction | 3σ if the four were picked from 16 tests, 2σ if from 50, with the measured correlation among the four (10 and 27 tests if uncorrelated); two of the four statistics do not test statistical anisotropy. Body: the distribution of the product of the four smallest of n_T uniform p-values is derived in closed form (Eqs. 1–11); 17 tests published in the literature are listed, and unreported null tests would raise the count [src: Sect. II, V] | reanalysis of arXiv:2310.12859 | Guth & Namjoo 2026, arXiv:2602.10178 |
| Cold Spot | p-value ≲ 0.01 in ΛCDM | Planck temperature | Owusu et al. 2023, arXiv:2211.16139 |
| Cold Spot as the imprint of a supervoid | void model disfavoured against ΛCDM with odds 1:13 (SMICA) and 1:20 (NILC) once the Planck lensing signal is used, against 56:1 and 21:1 from temperature alone | Planck temperature and lensing | arXiv:2211.16139 |

Status in Planck PR4 and after. The temperature anomalies are present in PR4 at the level of earlier releases (arXiv:2406.11543); the lack-of-power probability is less extreme in PR4 than in PR3 (≤ 1.76% against ≤ 0.33%, arXiv:2312.09989); the hemispherical asymmetry extends to higher multipoles in PR4 (arXiv:2504.05597). No anomaly has been confirmed in polarisation; one analysis of SRoll2 HFI 100 × 143 E modes at ℓ ≤ 10 reports a lower-tail S_1/2 probability of 0.4%, "a mild low power anomaly", with ℓ = 2 uncertainties open (Chiocchetta et al. 2021, arXiv:2012.00024) [src: Sect. 5]. The Planck collaboration's own caveats (arXiv:1906.02552) [src: Conclusions]: there is of order a 30% chance that the significance of any p-value dip increases when statistically isotropic polarisation data are added; the dipole-modulation and hemispherical-asymmetry statistics measure different weightings of the same ℓ to ℓ ± 1 couplings and are not independent; and even cosmic-variance-limited E modes may not give detections above 3σ.

What moved it: nothing in the temperature data; the Planck 2015 release "essentially corresponded to the limit of our ability to probe CMB anomalies with temperature fluctuations alone" (arXiv:1906.02552) [src: Conclusions]. What changed is the accounting: a claimed joint 5σ (2023, as stated by arXiv:2602.10178) against 3σ or 2σ after the look-elsewhere correction over about 16 or 50 tests (2026, arXiv:2602.10178 [src: abstract]), and the exclusion of the supervoid explanation of the Cold Spot by lensing (2023).

## 10. JWST high-redshift galaxy abundance
<!-- key: jwst-high-redshift-galaxy-abundance -->

Reference endpoint: the ΛCDM halo mass function times the cosmic baryon fraction, which bounds the stellar mass a halo can host. Metric: the comoving number density n(> M_*, z) or stellar mass density ρ_*(> M_*, z) of the observed galaxies against that bound, expressed as the required efficiency ε of converting baryons into stars; ε > 1 would contradict ΛCDM, ε below 1 is a statement about galaxy formation. All rows [src], abstracts read on 2026-10-10.

| Result | Data | Status of redshifts and masses | Citation |
|---|---|---|---|
| Six candidate galaxies with M_* > 10¹⁰ M_⊙ at 7.4 < z < 9.1, one with a possible M_* ~ 10¹¹ M_⊙; "if verified with spectroscopy" the stellar mass density would be much higher than anticipated | JWST early release NIRCam imaging | photometric candidates [src: abstract] | Labbé et al. 2023, arXiv:2207.12446 |
| The most massive candidates at z ~ 7–10 "lie at the very edge" of the limits set by the halo mass function and the baryon reservoir | the candidates above and similar ones | photometric [src: abstract] | Boylan-Kolchin 2023, arXiv:2208.01611 |
| "No tension with the ΛCDM model" in the sample; three ultra-massive galaxies (log M_*/M_⊙ ≳ 11.0) require about 50% of baryons converted into stars, two to three times the most efficient galaxies at later epochs | 36 massive dust-obscured galaxies at z_spec = 5–9, JWST FRESCO | spectroscopic (slitless grism) [src: abstract] | Xiao et al. 2024, arXiv:2309.02492 |
| One of those three, S1, moves from z_grism = 5.58 to z_spec = 3.2439 ± 0.0002 (grism contamination by a neighbour) and to log M_*/M_⊙ ~ 10.6; the authors state that the main conclusions of the 2024 paper are unchanged | JWST NIRSpec IFU + ALMA | spectroscopic, multi-line | Xiao et al. 2026, arXiv:2602.03030, abstract |
| UV luminosity functions at 7 ≤ z ≤ 14 reproduced over five magnitudes in ΛCDM; star-formation efficiency rising with redshift at fixed halo mass to 2–3% of baryons by z = 10–12; earlier claims of excess stellar mass at z = 8 attributed to AGN contamination, dust and missing MIRI constraints | UniverseMachine on the Uchuu N-body simulation against spectroscopically confirmed JWST and HST galaxies | model comparison [src: abstract] | Prada et al. 2026, arXiv:2604.18683 |

Size at the snapshot: no published spectroscopic sample requires ε > 1. The abundance question has become a galaxy-formation question (how efficiency, burstiness, dust, AGN light and the initial mass function evolve at z > 7) and is treated in `cosmo-reionization-21cm` for its bearing on reionisation. What moved it: 2022, photometric candidates at the ΛCDM limit; 2023–2024, spectroscopy (no tension in the FRESCO sample, with three objects needing 50% of baryons in stars, arXiv:2309.02492 [src: abstract]); 2026, one of those three shown to be a lower-redshift interloper of the grism method, and an empirical ΛCDM model matching the UV statistics.

## 11. Curvature, birefringence, parity-odd 4PCF
<!-- key: curvature-birefringence-parity-odd-4pcf -->

| Quantity | Value | Data | Citation | Flag |
|---|---|---|---|---|
| Ω_K | −0.044 (+0.018/−0.015) | Planck 2018 TT,TE,EE + lowE (Plik), spectra only | arXiv:1807.06209 | [src: Sect. 7.3, Eq. 44b] |
| Ω_K | −0.012 ± 0.010 | Planck PR4 HiLLiPoP TTTEEE | arXiv:2309.10034 | [src: abstract] |
| Ω_K | 0.0004 ± 0.0018 | Planck (CamSpec, more sky) + BAO | Efstathiou & Gratton 2020, arXiv:2002.06892 | [src: abstract] |
| Ω_K | −0.0107 (+0.0064/−0.0053) | CMB as defined by DESI | arXiv:2503.14738 | [src: Table 5 (Sect. VI), given as 10³Ω_K = −10.7 +6.4/−5.3] |
| Ω_K | +0.0023 ± 0.0011 (open side) | DESI DR2 BAO + CMB, ΛCDM + Ω_K | arXiv:2503.14738 | [src: Table 5 (Sect. VI), given as 10³Ω_K = 2.3 ± 1.1] |
| Ω_K | 10³Ω_K = 1.1 ± 1.3 (Pantheon+), 0.6 ± 1.3 (Union3), 0.8 ± 1.3 (DESY5) | DESI DR2 + CMB + SNe, w0waCDM + Ω_K | arXiv:2503.14738 | [src: Table 5 (Sect. VI)] |
| β (isotropic birefringence) | 0.342° (+0.094/−0.091), 3.6σ | WMAP + Planck | Eskilt & Komatsu 2022, arXiv:2205.13962 | [src: abstract] |
| β | 0.215° ± 0.074° (2.9σ) | ACT DR6 EB and TB | Diego-Palazuelos & Komatsu 2025, arXiv:2509.13654 | [src: abstract] |
| β | 0.277° ± 0.057°, 4.8σ; the authors claim no detection | ACT + Planck joint | Eskilt et al. 2026, arXiv:2608.06480 | [src: abstract] |
| Parity-odd 4PCF | 7.1σ (CMASS), 3.1σ (LOWZ) against Patchy mocks | BOSS DR12 | Hou, Slepian & Cahn 2022, arXiv:2206.03625 | [src: abstract] |
| Parity-odd 4PCF | signal 0–2.5σ; parity-even 8PCF bias term ≈ 6σ | BOSS, χ²_× and χ²_null statistics | Krolewski et al. 2024, arXiv:2407.03397 | [src: abstract] |
| Parity-odd 4PCF | auto analysis 4–10σ; cross-patch analysis null | DESI DR1 LRG | Slepian et al. 2025, arXiv:2508.09133 | [src: abstract] |

Reading. The Planck-alone closed-universe preference (Di Valentino, Melchiorri & Silk 2019, arXiv:1911.02087, "more than 99%" [src: abstract]) is the A_L feature in another parameter and has followed A_L down; the 2025 open-side hint is the CMB–DESI mismatch in another parameter and vanishes when w0wa is free [sec: inf]. The birefringence significance is conditional on the ACT instrumental priors on the polarisation angle [sec: inf]. For the 4PCF the position is "no evidence for parity violation" [sec: b2p].

## 12. History: what moved each tension
<!-- key: history-what-moved-each-tension -->

| Tension | Peak quoted size | When | Size now | What moved it |
|---|---|---|---|---|
| H0 | 7.1σ (arXiv:2510.23823 [src: abstract]) | 2025 | 4.5σ (arXiv:2503.14738 [src: Sect. VI]) to 7.1σ; CCHP "consistent with" ΛCDM (arXiv:2408.06153 [src: abstract]); 2.7σ with no ladder (arXiv:2610.14881 [src: abstract]) | smaller local errors; lower, tighter CMB endpoint; no route has closed the gap |
| S8, cosmic shear | about 3σ | 2020–2021 | 0.73σ (arXiv:2503.19441) to 2.6σ (arXiv:2601.14559) [src: abstract of each] | redshift calibration (KiDS, HSC); Planck PR4 |
| S8, CMB-lensing tomography | earlier DESI LRG × Planck results, more discrepant | 2021 | 0.775 (+0.019/−0.022) (arXiv:2407.04607 [src: abstract]) | neutrino consistency, projection effects, lensing normalisation |
| S8, Planck clusters | 2015 analyses (`cosmo-clusters`) | 2015 | 1.6σ (arXiv:2509.02068 [src: abstract]) | lensing mass calibration |
| A_L | 2.7σ (arXiv:1807.06209 [src: Sect. 2.2.1]) | 2018 | 1.039 ± 0.052 in PR4 (arXiv:2309.10034 [src: abstract]); 1.6σ in the (A_2pt, A_recon) plane for CMB-SPA (arXiv:2506.20707 [src: Sect. VII.2.3]) | PR4; ACT DR6; SPT-3G D1 |
| Ω_K < 0 from Planck | "more than 99%" (arXiv:1911.02087 [src: abstract]) | 2019 | −0.012 ± 0.010 (PR4, arXiv:2309.10034 [src: abstract]) | same as A_L |
| w0wa | 4.2σ (arXiv:2503.14738 [src: abstract]) | March 2025 | 3.0σ (arXiv:2605.27221) to 3.4σ (arXiv:2601.19424) [src: abstract of each] | supernova recalibration and host-mass fix |
| CF4 bulk flow | probability 0.00021% (arXiv:2302.02028 [src: Sect. 7, Table 1]) | 2023 | 0.11% (arXiv:2306.11269); 2.29σ full-range dipole (arXiv:2608.14265) [src: abstract of each] | mock-calibrated errors; shell analysis |
| Parity-odd 4PCF | 7.1σ (arXiv:2206.03625 [src: abstract]) | 2022 | 0 to 2.5σ (arXiv:2407.03397 [src: abstract]); null across patches | N-body mocks; 8PCF-free and cross-patch statistics |
| E_G at CMASS | low (`cosmo-dark-energy-modified-gravity`) | 2015 | consistent with GR | matched redshifts, calibrated estimator (`cosmo-dark-energy-modified-gravity`) |
| CatWISE quasar dipole | ≈ 6.7σ (forward-modelled Eddington bias, arXiv:2607.25703 [src: abstract]) | 2026 | 3.63σ (no clustering dipole), 3.44σ (random) or 3.27σ (aligned) with clustering-aware mocks (arXiv:2511.00822); 5.7σ in the Bayesian analysis (arXiv:2212.07733) [src: abstract of each] | null model with clustering, selection and mask; a direct velocity from redshifts |
| CMB large-angle anomalies, joint | ≤ 3 × 10⁻⁸ (arXiv:2310.12859 [src: abstract]) | 2023 | 3σ for about 16 tests, 2σ for about 50 (arXiv:2602.10178 [src: abstract]) | look-elsewhere correction |
| JWST massive candidates | "at the very edge" of the ΛCDM limit | 2022 | no tension in spectroscopic samples | spectroscopy; one grism redshift revised |

Sizes and dates in this table are from the sections above, each with its paper and place.

### 12.1 Superseded values
<!-- key: superseded-values -->

| Quantity | Superseded value | Data | Citation | Superseded by | Flag |
|---|---|---|---|---|---|
| H0 from time-delay lenses (Sect. 1.1) | 71.6 (+3.9/−3.3), mass-sheet degeneracy free | TDCOSMO-2025, 8 lensed quasars | TDCOSMO Collaboration 2025, arXiv:2506.03023 | TDCOSMO-2026, 71.1 (+2.4/−2.3), 11 lenses (arXiv:2610.14781), on 2026-10-26 | [src: abstract of each] |

## Not verified
<!-- key: not-verified -->

- The reconciliation of the two published Bayes factors for DESI DR2 + CMB + DES supernovae (Sect. 5.2).
- The point-estimate convention (mean, mode, MAP) behind each S8 row.
- The magnitude offset behind the SH0ES 2022 "5-sigma" (arXiv:2112.04510; the 5σ is in its abstract): not re-read in the body; the cluster-count tensions of SPT and Planck PSZ2 (arXiv:2401.02075, arXiv:2509.02068): their bodies were not read for the metric.
