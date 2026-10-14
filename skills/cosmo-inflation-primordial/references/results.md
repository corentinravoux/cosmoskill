# results — cosmo-inflation-primordial

Snapshot: 2026-10-14

Scope: current measurements of the primordial scalar spectrum (n_s, running, binned P(k)), the tensor-to-scalar ratio, primordial non-Gaussianity, isocurvature, spatial curvature, primordial features and cosmic birefringence, with the history of each number.

Flags: `[src]` read this session in the cited paper; `[sec]` read in a secondary source, which is named; `[der]` derived here. All searches were run on 2026-10-09.

## 1. Scalar spectral index n_s
<!-- key: scalar-spectral-index-ns -->

All values are 68% intervals in flat ΛCDM with a power-law spectrum, pivot k_* = 0.05 Mpc⁻¹, unless the model column says otherwise.

| n_s | Data | Model | Citation | Flag |
|---|---|---|---|---|
| 0.9649 ± 0.0042 | Planck 2018 temperature, polarisation and lensing | ΛCDM | arXiv:1807.06211 (abstract) | [src] |
| 0.9709 ± 0.0038 | P-ACT: ACT DR6 + Planck PR3 cut at ℓ < 1000 (TT) and ℓ < 600 (TE, EE) | ΛCDM | arXiv:2503.14452, section "Joint results from ACT and Planck" | [src] |
| 0.9730 ± 0.0055 (TT), 0.974 ± 0.014 (TE), 0.976 ± 0.012 (EE) | P-ACT split by spectrum | ΛCDM | arXiv:2503.14452, table of TT/TE/EE constraints | [src] |
| 0.974 ± 0.003 | P-ACT-LB: P-ACT + ACT and Planck CMB lensing + DESI DR1 BAO | ΛCDM | arXiv:2503.14452 (abstract) | [src] |
| 0.9743 ± 0.0034 | P-ACT-LB, the four-digit form of the previous row | ΛCDM | quoted in McDonald 2025, arXiv:2505.07488, and Shobcha et al. 2026, arXiv:2606.24131 | [sec] |
| 0.9679 ± 0.0033 | CMB-SPA: SPT-3G D1 + ACT DR6 + Planck (second arXiv version; the first gave 0.9684 ± 0.0030) | ΛCDM | arXiv:2506.20707, "Summary of results" | [src] |
| 0.951 ± 0.011 | SPT-3G D1 alone (4.1σ from scale invariance) | ΛCDM | arXiv:2506.20707, cosmology section | [src] |
| 0.9758 ± 0.0064 | Planck + ACT + SPT ("CMB-PAS") + DESI DR2 | ΛCDM + α_s + N_eff + Σm_ν (nine parameters) | Cheslog et al. 2026, arXiv:2609.35964 | [src] |
| 0.9667 ± 0.0041 | Planck + DESI (BAO and full shape) | ΛCDM + Ω_K | Chudaykin et al. 2026, arXiv:2607.28445 | [src] |
| 0.9692 ± 0.0035 | Planck + ACT + SPT + DESI | ΛCDM + Ω_K | arXiv:2607.28445 | [src] |
| 0.9716 ± 0.0032 | Planck + ACT + SPT + DESI | w0waCDM | arXiv:2607.28445 | [src] |
| 0.9694 ± 0.0035 | Planck + ACT + SPT + DESI | w0waCDM + Ω_K | arXiv:2607.28445 | [src] |

Reading the table.

- The "ACT n_s shift" is two steps. Adding ACT DR6 to a truncated Planck moves n_s from 0.9649 to 0.9709, that is by +0.0060 [der: difference of the two rows], because the small-scale data break the n_s–Ω_b h² degeneracy: the two parameters are positively correlated in Planck and anti-correlated in ACT (arXiv:2503.14452). Adding CMB lensing and DESI BAO moves it again to 0.974.
- The CMB-only combination of all three experiments, CMB-SPA, gives 0.9679 ± 0.0033, which is 9.9σ from scale invariance (9.8σ in the conclusions of the same version) and lower than P-ACT-LB (arXiv:2506.20707). The high value 0.974 therefore belongs to CMB + DESI BAO in ΛCDM, not to the CMB alone.
- Because CMB and DESI BAO disagree in ΛCDM (2.8σ for CMB-SPA against DESI DR2, arXiv:2506.20707), forcing them into one ΛCDM fit pulls Ω_m h² down and n_s up. Any extension that absorbs that disagreement (curvature, evolving dark energy) brings n_s back to 0.967–0.972 (arXiv:2607.28445). Ferreira et al. 2025, arXiv:2507.12459 made this point explicitly: see `open-questions.md`, section 1.
- Planck's own n_s quoted above is the Plik PR3 value. Values from the PR4 likelihoods are in `cosmo-cmb`.

## 2. Running of the spectral index
<!-- key: running-of-the-spectral-index -->

Definition: ln P_R(k) = ln A_s + [n_s − 1 + ½ (dn_s/dln k) ln(k/k_*)] ln(k/k_*), with k_* = 0.05 Mpc⁻¹ (arXiv:2503.14454).

| dn_s/dln k | Data | Citation | Flag |
|---|---|---|---|
| −0.0041 ± 0.0067 | Planck 2018 CMB + lensing + BAO | arXiv:1807.06211, as quoted in arXiv:2503.14454 section 4.1 | [sec] |
| −0.0045 ± 0.0067 | Planck 2018 TT,TE,EE + lowE + lensing (no BAO); with running of running free: 0.002 ± 0.010 and d²n_s/dln k² = 0.010 ± 0.013 (TT alone 0.013 ± 0.012 and 0.022 ± 0.012) | arXiv:1807.06211 [src: Sect. 3.3, Eqs. 15–18] | [src] |
| 0.034 ± 0.022 | ACT DR6 alone | arXiv:2503.14454 | [src] |
| 0.0060 ± 0.0055 | P-ACT | arXiv:2503.14454 | [src] |
| 0.0062 ± 0.0052 | P-ACT-LB | arXiv:2503.14454 (abstract and section 4.1) | [src] |
| 0.0080 ± 0.0064 | Planck + ACT + SPT + DESI DR2, with N_eff and Σm_ν free | arXiv:2609.35964 | [src] |
| −0.010 ± 0.004 | eBOSS Lyα P1D + Planck (Palanque-Delabrouille et al. 2020, arXiv:1911.09073) | as quoted in arXiv:2503.14454 section 4.1 | [sec] |
| 0.0014 ± 0.0041 | DESI DR1 Lyα P1D + DESI BAO + Planck, ACT, SPT-3G | Chaves-Montero et al. 2026, arXiv:2601.21432 (abstract) | [src] |

Running of the running from the same DESI DR1 P1D combination: β_s = −0.0006 ± 0.0048 [src]; the P1D tightens α_s by a factor 1.27 and β_s by a factor 1.90 relative to CMB + BAO (arXiv:2601.21432).

P-ACT alone excludes dn_s/dln k = −0.010 at more than 3σ (arXiv:2503.14454) [src]. Planck alone prefers a slightly negative running and ACT a slightly positive one; the combination sits at zero within 1.2σ [der: 0.0062/0.0052]. Slow-roll inflation predicts |dn_s/dln k| of order (1 − n_s)², about 10⁻³ [der: (0.03)² ≈ 9 × 10⁻⁴, textbook scaling], five times below the present error. The P1D measurement itself is described in `cosmo-lyman-alpha`.

## 3. Binned primordial power spectrum
<!-- key: binned-primordial-power-spectrum -->

ACT DR6 reconstructs e^(−2τ) P_R(k) in 30 bins (4 at k = 10⁻⁴ to 10^(−2.5) Mpc⁻¹, then 26 logarithmic bins over 0.011 ≲ k ≲ 0.43 Mpc⁻¹), which adds 28 parameters to ΛCDM (arXiv:2503.14454) [src].

| Quantity | Value | Data | Flag |
|---|---|---|---|
| Fractional error on e^(−2τ) P_R at k = 0.15 Mpc⁻¹ | 2.8% | Planck alone | [src] |
| same | 1.4% | ACT alone | [src] |
| same | 1.2% | P-ACT | [src] |
| same | 1.1% | P-ACT-LB | [src] |
| Fractional error at k = 0.2 Mpc⁻¹ | 0.5% | Planck + ACT + SPT (arXiv:2609.35964) | [src] |
| same, SO-like and CMB-HD-like surveys | 0.1% | **forecast**, arXiv:2609.35964 | [src] |

Planck alone has no two-sided posterior above k = 0.15 Mpc⁻¹; ACT has one up to 0.32 Mpc⁻¹ and a one-sided 95% limit to 0.43 Mpc⁻¹, a threefold extension of the constrained range. Neighbouring bins are correlated at 30–40%, and bins 6–9 near k = 0.01 Mpc⁻¹ are anti-correlated at up to 90% (arXiv:2503.14454) [src]. No bin departs from the power law. The Planck 2018 non-parametric reconstructions reached the same conclusion (arXiv:1807.06211).

## 4. Tensor-to-scalar ratio r
<!-- key: tensor-to-scalar-ratio-r -->

All limits are 95% upper limits. BICEP/Keck quotes r at k = 0.05 Mpc⁻¹; Planck 2018 quotes r at k = 0.002 Mpc⁻¹. With n_t = −r/8 the two differ negligibly at the present limit, but the subscript should be copied with the number.

| r (95%) | σ(r) | Data | Citation | Flag |
|---|---|---|---|---|
| r_0.05 < 0.12 | — | BICEP2/Keck 150 GHz × Planck, about 400 deg² | BICEP2/Keck and Planck 2015, arXiv:1502.00612 | [src] |
| r_0.002 < 0.10 | — | Planck 2018 alone | arXiv:1807.06211 | [src] |
| r_0.002 < 0.056 | — | Planck 2018 + BK15 | arXiv:1807.06211 | [src] |
| r < 0.158 | 0.069 from BB at ℓ = 2–150 | Planck PR4 B modes only, more than 50% of the sky | Tristram et al. 2021, arXiv:2010.01139 | [src] |
| r < 0.069 | — | Planck PR4 EE, BB, EB | arXiv:2010.01139 | [src] |
| r < 0.056 | — | Planck PR4 polarisation + TT | arXiv:2010.01139 | [src] |
| r < 0.044 | — | Planck PR4 + BK15 | arXiv:2010.01139 | [src] |
| r_0.05 < 0.090 → 0.082 | 0.024 → 0.022 | BK14 before and after delensing with SPTpol and Planck | BICEP/Keck and SPTpol 2021, arXiv:2011.08163 | [src] |
| r < 0.11 (Feldman–Cousins), < 0.19 (Bayesian) | — | SPIDER 2015 flight, 4.8% of the sky, 95 and 150 GHz | SPIDER 2021, arXiv:2103.13334 | [src] |
| **r_0.05 < 0.036** | **0.009** | BK18: BICEP2, Keck Array, BICEP3 to 2018, with WMAP and Planck maps | BICEP/Keck 2021, arXiv:2110.00483 | [src] |
| r < 0.032 | — | BK18 + Planck PR4 + BAO, all six ΛCDM parameters free | Tristram et al. 2022, arXiv:2112.07961 | [src] |
| r < 0.038 | — | P-ACT-LB + BK18 | arXiv:2503.14454 | [src] |
| r < 0.25 | 0.067 | SPT-3G 2019–2020, about 1500 deg², 32 ≤ ℓ < 502 | Zebrowski et al. 2025, arXiv:2505.02827 | [src] |

Status at the snapshot.

- BK18 remains the most recent BICEP/Keck constraint on r. A title search of BICEP papers since 2024 returns instrument and systematics papers for a "BK24" release (data through 2024) and a birefringence paper (BICEP/Keck XXI, arXiv:2603.06812), but no new r limit. The beam-systematics paper for 2016–2024 BICEP3 data (Elwood et al. 2026, arXiv:2608.25016) describes itself as preparation for the BK24 release.
- r < 0.032 and r < 0.036 are the same B-mode data. The first adds Planck PR4 low-ℓ polarisation and BAO and frees the ΛCDM parameters; the gain comes mostly from the Planck large-scale information, since "Planck sensitivity to r is no longer comparable with ground-based measurements" (arXiv:2112.07961).
- r < 0.038 from ACT is weaker than 0.036 only because n_s moved; the B-mode data are again BK18 (arXiv:2503.14454).
- SPT-3G's own limit, r < 0.25, is an independent check and not competitive: its noise knee is at ℓ = 128 (95 GHz) and ℓ = 182 (150 GHz), above the recombination bump (arXiv:2505.02827) [src].
- A different question, causal (post-inflationary) tensor sources, gives r_ect < 0.0077 at 95% from BICEP/Keck, SPTpol, SPT-3G, Planck and WMAP B modes (Zebrowski et al. 2026, arXiv:2601.20958) [src]. This parameter is not the inflationary r and the two limits must not be compared.

BK18 details [src, arXiv:2110.00483]: map depths 2.8, 2.8 and 8.8 μK·arcmin at 95, 150 and 220 GHz; effective area about 600 deg² at 95 GHz and about 400 deg² at 150 and 220 GHz; seven foreground parameters; no external prior on the dust spectral index; the 220 GHz maps reach a higher signal-to-noise on polarised dust than Planck 353 GHz.

### Slow-roll parameters and the r–n_s plane
<!-- key: slow-roll-parameters-and-the-r-ns-plane -->

With r = 16 ε_V and n_s − 1 = 2 η_V − 6 ε_V, P-ACT-LB + BK18 gives η_V = (−95 +23/−30) × 10⁻⁴ (68%) (arXiv:2503.14454) [src]. Planck 2018 concluded that concave potentials, V'' < 0, are favoured (arXiv:1807.06211). With the ACT-era n_s the Starobinsky R² model sits on the 2σ boundary of P-ACT-LB-BK18 for 50–60 e-folds, and power-law potentials closer to linear are accommodated (arXiv:2503.14454).

## 5. Primordial non-Gaussianity from the CMB bispectrum
<!-- key: primordial-non-gaussianity-from-the-cmb -->

All values are 68% intervals. The amplitudes f_NL^local, f_NL^equil and f_NL^ortho multiply the three standard bispectrum templates defined in `physics-and-methods.md`, section 5. Planck values are "statistical" errors from simulations, after subtraction of the lensing–ISW bispectrum.

| f_NL^local | f_NL^equil | f_NL^ortho | Data | Citation | Flag |
|---|---|---|---|---|---|
| — | −125 to 435 (95%) | −369 to 71 (95%) | WMAP 5-year, optimal estimator | Senatore, Smith and Zaldarriaga 2010, arXiv:0905.3746 | [src] |
| 2.5 ± 5.7 | −16 ± 70 | −34 ± 33 | Planck 2015, temperature only | Planck 2015 XVII, arXiv:1502.01592 | [src] |
| 0.8 ± 5.0 | −4 ± 43 | −26 ± 21 | Planck 2015, T + E (labelled preliminary by the collaboration) | arXiv:1502.01592 | [src] |
| **−0.9 ± 5.1** | **−26 ± 47** | **−38 ± 24** | Planck 2018 (PR3), T + E, including 4 ≤ ℓ < 40 polarisation | Planck 2018 IX, arXiv:1905.05697 | [src] |
| −0.1 ± 5.0 | 6 ± 46 | −8 ± 21 | Planck PR4 (NPIPE), T + E, binned bispectrum estimator | Jung et al. 2025, arXiv:2504.00884 | [src] |

Local trispectrum: g_NL^local = (−9.0 ± 7.7) × 10⁴ (Planck 2015, arXiv:1502.01592) and (−5.8 ± 6.5) × 10⁴ (Planck 2018, arXiv:1905.05697), both 68% [src].

Reading the table.

- The Planck 2018 collaboration values remain the reference numbers. The PR4 reanalysis is consistent with them and has errors smaller by up to 12% (for the orthogonal shape); its authors call it "the best Planck constraints" (arXiv:2504.00884). It is a five-author paper, not a Planck Collaboration product, and it uses the binned and integrated-bispectrum estimators only.
- The Planck 2015 T + E errors (5.0, 43, 21) are smaller than the 2018 ones (5.1, 47, 24). The 2015 polarisation result was flagged as preliminary because of a mismatch between the noise model in simulations and data (arXiv:1502.01592); the 2018 result supersedes it although its error bars are larger.
- The lensing–ISW bispectrum is detected by Planck 2018 at 3.5σ (arXiv:1905.05697). It is a contaminant of f_NL^local that has to be subtracted, and its detection is a check of the pipeline.
- The PR4 analysis found that its 600 simulations have a systematically low lensing bispectrum and showed that this does not move the primordial results (arXiv:2504.00884).
- Single-field models: the equilateral and orthogonal limits translate into a lower bound on the inflaton sound speed. WMAP 5-year gave c_s > 0.011 (95%) (arXiv:0905.3746) [src]; Planck 2018 gives c_s ≥ 0.021 (95%), the same number for temperature only and for T + E, after marginalising over the second cubic coefficient (arXiv:1905.05697, section 8) [src].
- No ACT DR6 or SPT-3G primary-CMB bispectrum measurement of f_NL was found in the date-sorted search of 2026-10-09. ACT's published f_NL result is from cluster counts: f_NL = 55 ± 125 from 1,201 SZ clusters over 10,347 deg², probing 5–10 h⁻¹Mpc scales (Sarieddine et al. 2026, arXiv:2602.03917) [src].
- Beyond the three templates: a scan of "cosmological collider" templates, orthogonalised against the single-field shapes, in Planck data with the Modal pipeline peaks at 2.4σ for spin 0 after the look-elsewhere correction, and near 2σ for spins 1 and 2 (Suman et al. 2025, arXiv:2511.17500) [src]. A neural separable-basis method applied to Planck PR4 finds no detection for two strongly mixed collider models (Philcox, Zhong and Sirletti 2025, arXiv:2511.19179) [src].

## 6. Primordial non-Gaussianity from large-scale structure
<!-- key: primordial-non-gaussianity-from-large-scale -->

### 6.1 Local shape from scale-dependent bias (power spectrum)
<!-- key: local-shape-from-scale-dependent-bias-power -->

Every entry constrains the product f_NL · b_φ. The column "p" gives the assumed response, b_φ = 2 δ_c (b_1 − p): p = 1 is the universal mass function, p = 1.6 the recent-merger value used for quasars (Slosar et al. 2008, arXiv:0805.3580). Values are 68% unless stated.

| f_NL^local | Data | p assumed | Citation | Flag |
|---|---|---|---|---|
| −29 to +70 (95%) | SDSS compendium, dominated by photometric quasars | 1 | arXiv:0805.3580 | [src] |
| −31 to +70 (95%) | same | 1.6 for quasars | arXiv:0805.3580 | [src] |
| −51 to +21 (95%) | eBOSS DR14 quasars, redshift-weighted P(k) | 1 | Castorina et al. 2019, arXiv:1904.08859 | [src] |
| −81 to +26 (95%) | same | lower response | arXiv:1904.08859 | [src] |
| −12 ± 21 | eBOSS DR16, 343,708 quasars, 0.8 < z < 2.2, 4808 deg² | 1.6 (default); p = 1 gives −18 to 11 at 68% [src: Sect. 8.1] | Mueller et al. 2021, arXiv:2106.13725 | [src] |
| −4 to +27 | eBOSS DR16 quasars, optimal weights | 1 | Cagliari et al. 2023, arXiv:2309.15814 | [src] |
| −23 to +21 | same | lower response | arXiv:2309.15814 | [src] |
| 16 ± 16 down to 230 ± 226 | BOSS DR12 galaxies, one data vector, different b_φ(b_1) relations | varied | Barreira 2022, arXiv:2205.05673 | [src] |
| **−3.6 +9.0/−9.1** | DESI DR1: 1,631,716 LRGs (0.6 < z < 1.1) and 1,189,129 QSOs (0.8 < z < 3.1), blinded | 1 for LRG, 1.6 for QSO | Chaussidon et al. 2024, arXiv:2411.17623 | [src] |
| 3.5 +10.7/−7.4 | same | 1 for both | arXiv:2411.17623 | [src] |
| −3.3 ± 9.2 | DESI DR1, with a simulation prior p̄ ≈ 1.4 for quasars (IllustrisTNG, checked on CAMELS) | 1.4 | Fondi et al. 2026, arXiv:2602.12357 | [src] |
| 2.1 +8.8/−8.3 | DESI DR1 LRG and QSO auto- and cross-spectra | (not in abstract) | Rosado-Marín et al. 2026, arXiv:2604.05213 | [src] |
| −3 ± 12 (LRG alone −3 +22/−21; QSO alone 0 +17/−16) | DESI DR1, configuration-space 2PCF, simulation-based model | Gaussian priors 1.0 ± 0.1 (LRG), 1.6 ± 0.1 (QSO) | Brown et al. 2026, arXiv:2606.24651 | [src] |

The DESI DR1 result is 2.3 times more precise than the eBOSS one (arXiv:2411.17623) [src]. Adding the LRG × QSO cross-spectrum improves the DR1 error by about 9%; adding ELGs brings no clear gain (arXiv:2604.05213) [src]. No DESI DR2 f_NL measurement was found in the search of 2026-10-09.

### 6.2 Cross-correlations and other large-scale probes
<!-- key: cross-correlations-and-other-large-scale-probes -->

| f_NL^local | Data | Assumption | Citation | Flag |
|---|---|---|---|---|
| −20.5 +19.0/−18.1 | Quaia quasars, auto + CMB-lensing cross, two redshift bins | p = 1 | Fabbian et al. 2025, arXiv:2504.20992 | [src] |
| −28.7 +26.1/−24.6 | same | p = 1.6 | arXiv:2504.20992 | [src] |
| −13.8 +26.7/−25.0 | Quaia × CMB lensing only | p = 1 | arXiv:2504.20992 | [src] |
| 6 +20/−24 | 1.2 million DESI DR1 quasars × Planck PR4 lensing, three bins over 0.8 < z < 3.5, f_sky about 20% | p = 1.0 | Chiarenza et al. 2025, arXiv:2512.17865 | [src] |
| 2 +28/−34 | same | p = 1.6 | arXiv:2512.17865 | [src] |
| 19 +25/−31 | same, optimal weights | p = 1.6 | arXiv:2512.17865 | [src] |
| −39 +40/−33 | kSZ velocity reconstruction, ACT DR5 × DESI Legacy Imaging LRGs | — | Hotinli, Smith and Ferraro 2025, arXiv:2506.21657 | [src] |
| 15.9 +34.6/−34.4 | kSZ velocity reconstruction, DESI DR2 × ACT DR6 | — | Chaussidon et al. 2026, arXiv:2604.04867, as reported in the `cosmo-cmb-lss-cross-correlations` skill | [sec] |
| 43 ± 23 | CIB × CMB lensing | — | Thornton et al. 2026, arXiv:2605.03783, as reported in the `cosmo-cmb-lss-cross-correlations` skill | [sec] |
| 55 ± 125 | ACT DR6 cluster counts | external priors | arXiv:2602.03917 | [src] |

The DESI quasar × Planck PR4 lensing result improves on the earlier Legacy Imaging Survey DR9 analysis by about 35% (arXiv:2512.17865) [src]. Details of the cross-correlation estimators are in `cosmo-cmb-lss-cross-correlations`.

### 6.3 Galaxy bispectrum
<!-- key: galaxy-bispectrum -->

| f_NL^local | f_NL^equil | f_NL^ortho | Data and model | Citation | Flag |
|---|---|---|---|---|---|
| — | 940 ± 600 | −170 ± 170 | BOSS P + B, all cosmological and nuisance parameters varied | Cabass et al. 2022, arXiv:2201.07238 | [src] |
| — | 260 ± 300 | −23 ± 120 | same, quadratic bias and cosmology fixed | arXiv:2201.07238 | [src] |
| 52 ± 34 | 207 ± 292 | −68 ± 73 | BOSS P + B, one-loop EFT for both, ΛCDM fixed to Planck | D'Amico et al. 2022, arXiv:2201.11518 | [src] |
| −0.1 ± 7.4 | 719 ± 390 | −200 ± 100 | DESI DR1 public data, P + B, one-loop EFT | Chudaykin, Ivanov and Philcox 2025, arXiv:2512.04266 | [src] |
| — | 200 ± 230 | −24 ± 86 | high-redshift DESI DR1 + BOSS, simulation-based bias priors | arXiv:2512.04266 | [src] |
| −0.0 ± 4.1 | — | — | DESI DR1 P + B combined with the CMB | arXiv:2512.04266 | [src] |

The BOSS sound-speed limit from the first row is c_s ≥ 0.013 at 95% (arXiv:2201.07238) [src], comparable to the WMAP 5-year one. The DESI DR1 P + B analysis is an external reanalysis of public data, not a DESI Collaboration result; its combination with the CMB is quoted by its authors as 18% tighter than the CMB alone (arXiv:2512.04266) [src]. Its f_NL^local = −0.1 ± 7.4 carries a b_φ assumption that the abstract does not state.

### 6.4 History of the local f_NL error from large-scale structure
<!-- key: history-of-the-local-fnl-error-from-large-scale -->

σ(f_NL^local) from scale-dependent bias went from about 25 (SDSS 2008; [der] half of the 95% interval −29 to +70 divided by 2) to 21 (eBOSS DR16), then to 9 (DESI DR1), against 5.1 for Planck. The comparison with Planck holds only for a fixed b_φ: for the same BOSS data the error ranges from 16 to 226 as the b_φ(b_1) relation is changed (arXiv:2205.05673), and from 19 to 165 between the 33% highest- and lowest-concentration halo populations (Lazeyras et al. 2023, arXiv:2209.07251) [src].

## 7. Isocurvature perturbations
<!-- key: isocurvature-perturbations -->

No isocurvature mode is detected. The ACT DR6 analysis follows the Planck parametrisation: power-law spectra P_RR, P_II, P_RI defined by their amplitudes at k_1 = 0.002 Mpc⁻¹ and k_2 = 0.1 Mpc⁻¹, written P^(1) and P^(2), sampled with uniform priors on the amplitudes at the two scales rather than on an amplitude and a tilt (arXiv:2503.14454, section 4.3). All limits below are one-tail 95% and all are read in that section [src]. The "Planck only" column is Planck as re-run by ACT, not the Planck Collaboration's own table.

| Model | Parameter | Planck only | P-ACT | P-ACT-LB |
|---|---|---|---|---|
| Uncorrelated CDI, scale-invariant | 10¹⁰ P_II^(1) | < 0.9 | < 1.1 | unchanged |
| Uncorrelated NDI, scale-invariant | 10¹⁰ P_II^(1) | < 2.1 | < 1.8 | unchanged |
| Uncorrelated CDI, free tilt | 10¹⁰ P_II^(1) | (tighter than P-ACT) | < 0.7 | unchanged |
| Uncorrelated CDI, free tilt | 10¹⁰ P_II^(2) | < 59 | < 26 | unchanged |
| Uncorrelated NDI, free tilt | 10¹⁰ P_II^(1) | — | < 1.6 | — |
| Uncorrelated NDI, free tilt | 10¹⁰ P_II^(2) | — | < 6.1 | < 5.4 |

Reading the table.

- CDI is cold-dark-matter density isocurvature, NDI neutrino density isocurvature. Baryon isocurvature is not fitted separately because it is indistinguishable from CDI at linear order up to a rescaling by Ω_c and Ω_b; neutrino velocity isocurvature is not considered by ACT (arXiv:2503.14454).
- The gain from ACT is on small scales: the limit on a blue-tilted CDI amplitude at k = 0.1 Mpc⁻¹ improves from 59 to 26 (in units of 10⁻¹⁰), while the large-scale limit at k = 0.002 Mpc⁻¹ does not improve. For scale-invariant CDI the P-ACT limit is slightly weaker than the Planck one because the higher n_s of P-ACT is positively correlated with the CDI amplitude (arXiv:2503.14454).
- A small, insignificant peak at non-zero NDI amplitude in the Planck-only posterior disappears when ACT DR6 is added (arXiv:2503.14454).
- Fully correlated and anti-correlated CDI models are also constrained by ACT (arXiv:2503.14454, section 4.3.2 and appendix table); those values were not read this session.
- Adding SPT to Planck and ACT for axion-type CDI with red to blue tilts moderately improves the limit on the isocurvature spectral index and does not tighten the amplitude limits at fixed index (Petretti et al. 2026, arXiv:2606.11312) [src].

### Planck Collaboration limits (2018)
<!-- key: planck-collaboration-limits-2018 -->

Planck quotes the primordial isocurvature fraction β_iso(k) = P_II(k) / [P_RR(k) + P_II(k)] at k_low = 0.002, k_mid = 0.05 and k_high = 0.1 Mpc⁻¹, and the non-adiabatic fraction of the observed temperature variance, α_non-adi = 1 − (ΔT)²_RR / (ΔT)²_tot summed over ℓ = 2–2500. All limits are 95% from Planck TT,TE,EE + lowE + lensing and are read in arXiv:1807.06211, section 9 and conclusions [src].

| Model | Limit |
|---|---|
| Generally correlated CDI, NDI, NVI: β_iso(k_low) | < 2.5%, < 7.4%, < 6.8% |
| Generally correlated CDI, NDI, NVI: non-adiabatic fraction of the temperature variance | < 1.3%, < 1.7%, < 1.7% |
| Uncorrelated CDI with n_II = 1 ("axion I"): β_iso(k_mid) | < 0.038 |
| same: α_non-adi | < 1.55% |
| Fully correlated CDI ("curvaton I"): β_iso | < 0.00095 |
| Fully anti-correlated CDI ("curvaton II"): β_iso | < 0.00107 |
| Compensated baryon–CDM isocurvature: variance Δ²_rms | 0.0037 +0.0016/−0.0021 (68%) |

The fully correlated limits are about 40 times stronger than the uncorrelated one because the cross-term P_RI is linear in the isocurvature amplitude (arXiv:1807.06211). Planck 2018 states that the polarisation data "provide a stringent test of the adiabaticity of the initial conditions" (abstract).

## 8. Spatial curvature
<!-- key: spatial-curvature -->

Convention: Ω_K = 1 − Ω_tot, so Ω_K < 0 is a closed universe (positive spatial curvature K) and Ω_K > 0 an open one (negative K). All values are 68% in ΛCDM + Ω_K unless the model column says otherwise.

| Ω_K | Data | Model | Citation | Flag |
|---|---|---|---|---|
| −0.056 +0.028/−0.018 | Planck 2018 TT + lowE | ΛCDM + Ω_K | Planck 2018 VI, arXiv:1807.06209, section on curvature | [src] |
| −0.044 +0.018/−0.015 | Planck 2018 TT,TE,EE + lowE (Plik) | ΛCDM + Ω_K | arXiv:1807.06209 | [src] |
| −0.037 +0.019/−0.014 | same with the CamSpec likelihood | ΛCDM + Ω_K | arXiv:1807.06209 | [src] |
| −0.0106 ± 0.0065 | Planck 2018 TT,TE,EE + lowE + lensing | ΛCDM + Ω_K | arXiv:1807.06209 | [src] |
| 0.0007 ± 0.0019 | Planck 2018 + lensing + BAO (pre-DESI) | ΛCDM + Ω_K | arXiv:1807.06209 | [src] |
| 0.0004 ± 0.0018 | Planck with a new likelihood built by the authors + BAO and other data | ΛCDM + Ω_K | Efstathiou and Gratton 2020, arXiv:2002.06892 | [src] |
| 0.0022 ± 0.0015 | Planck + lensing + DESI DR1 BAO ("Planck-LB") | ΛCDM + Ω_K | arXiv:2503.14454, section 7.1 | [src] |
| 0.0019 ± 0.0015 | P-ACT-LB | ΛCDM + Ω_K | arXiv:2503.14454, section 7.1 | [src] |
| −0.0107 +0.0064/−0.0053 | CMB as defined by DESI (CamSpec rather than Plik, with ACT lensing added) | ΛCDM + Ω_K | DESI 2025, arXiv:2503.14738, table of cosmological constraints | [src] |
| 0.025 ± 0.041 | DESI DR2 BAO alone | ΛCDM + Ω_K | arXiv:2503.14738 | [src] |
| **0.0023 ± 0.0011** | DESI DR2 BAO + CMB | ΛCDM + Ω_K | arXiv:2503.14738 | [src] |
| 0.0011 ± 0.0013, 0.0006 ± 0.0013, 0.0008 ± 0.0013 | DESI DR2 + CMB + Pantheon+, Union3, DES-SN5YR | w0waCDM + Ω_K | arXiv:2503.14738 | [src] |
| about 0.003 | Planck, ACT, SPT + DESI BAO and full shape | ΛCDM + Ω_K | arXiv:2607.28445 (abstract) | [src] |

Reading the table.

- The Planck 2018 primary spectra alone give "an apparent detection of curvature at well over 2σ": the 99% region for TT,TE,EE + lowE is −0.095 < Ω_K < −0.007, with about 1 sample in 10,000 at Ω_K ≥ 0, and Δχ²_eff = −11 for one extra parameter. Planck attributes it to the same feature of the spectra that gives A_L > 1 (arXiv:1807.06209) [src]. Di Valentino, Melchiorri and Silk 2019 (arXiv:1911.02087) read this as a preference for a closed universe at more than 99% and a possible "crisis"; Handley 2019 (arXiv:1908.09139) measured the curvature tension between Planck, CMB lensing and BAO at 2.5 to 3σ and gave betting odds of over 50:1 against flatness from Planck alone; Efstathiou and Gratton 2020 (arXiv:2002.06892) found Planck consistent with flatness using a different likelihood.
- The fate of the closed-universe preference follows the fate of A_L, which is told in `cosmo-cmb`: with PR4 likelihoods and with ACT DR6 the lensing excess shrinks. ACT DR6 alone prefers a flat geometry and pulls the Planck contours towards Ω_K = 0 (arXiv:2503.14454). The CMB-only value used by DESI, −0.0107 +0.0064/−0.0053, is 1.7σ from zero [der: 0.0107/0.0064].
- With DESI DR2 BAO the sign changes: Ω_K = +0.0023 ± 0.0011, 2.1σ from flat on the open side [der: 0.0023/0.0011]. DESI states that it finds no significant preference for a non-flat model (arXiv:2503.14738). The positive value is another face of the CMB–DESI distance tension in ΛCDM: once w0wa is free it falls to (0.6–1.1) × 10⁻³ ± 1.3 × 10⁻³, and freeing curvature does not remove the w0wa preference (arXiv:2503.14738).
- Curvature radius: P-ACT-LB gives R_K > 105 Gpc (closed) and R_K > 66 Gpc (open) at 95% (arXiv:2503.14454) [src].
- Planck 2018 summarised the pre-DESI situation as flatness "confirmed at a precision of 0.4% at 95% CL" with BAO (arXiv:1807.06211, abstract) [src].
- For inflation: Efstathiou and Gratton conclude that the data support a large number of e-folds and disfavour incomplete inflation (arXiv:2002.06892). Chudaykin et al. 2026 discuss open-universe inflation models compatible with Ω_K ≈ 3 × 10⁻³ (arXiv:2607.28445), a value not significant on its own.
- Late-time-only determinations (BAO, supernovae, time delays, chronometers, without the CMB power spectra) lean open in ΛCDM: "2σ evidence for an open universe" from DESI BAO + SNe Ia, rising above 3σ with the acoustic scale θ* and to 5σ with DES-SN5YR (Wang et al. 2025, arXiv:2512.19565) [src]; Ω_K = 0.049 ± 0.037 from DESI DR2 BAO, supernovae, lensing time delays and cosmic chronometers, a preference that vanishes in extensions of ΛCDM and that its author calls a model artefact (Wu 2026, arXiv:2604.23492) [src]. These are not independent of the w0wa discussion in `cosmo-dark-energy-modified-gravity`.

## 9. Primordial features
<!-- key: primordial-features -->

Template searches write P_R(k) = P_0(k) [1 + A_lin cos(ω_lin k + φ)] or [1 + A_log cos(ω_log ln(k/k_*) + φ)], with P_0 the power law. No search has found a feature with global significance above 3σ. All limits are 95%.

| Result | Data | Citation | Flag |
|---|---|---|---|
| No evidence for parameterised features; oscillatory models tested jointly with the bispectrum | Planck 2018 power spectrum and bispectrum | arXiv:1807.06211 (abstract) | [src] |
| Bounds on oscillatory features exceeding the sensitivity of Planck over a significant range of frequencies | BOSS DR12 galaxy power spectrum | Beutler et al. 2019, arXiv:1906.08758 | [src] |
| Fit improvements of Δχ² ≈ −10 to −15 at a few frequencies ω ≈ 10–100; global significance at most 2.6σ; not supported by Bayesian model comparison | Planck PR3 and PR4, unbinned likelihoods | Raffaelli, Ballardini and Barbieri 2026, arXiv:2605.30236 | [src] |
| A_lin < 0.021, A_log < 0.022, A_log,rf < 0.023 (about 2% of A_s) | Planck 2018 + ACT DR6 + DESI DR2 | Nerval et al. 2026, arXiv:2606.28310 | [src] |
| A_lin < 0.033, A_log < 0.035 over ω_lin ∈ (20, 800) Mpc and ω_log ∈ (2.5, 80), ΛCDM parameters marginalised | DESI DR1 public data, power spectrum and bispectrum of six tracers, Lagrangian EFT | Chen et al. 2026, arXiv:2610.10530 | [src] |
| A_lin < 0.024, A_log < 0.031 | same, cosmology fixed to Planck 2018 | arXiv:2610.10530 | [src] |
| No feature; n_s = 0.976 ± 0.021 from the knot reconstruction | BOSS DR12 LRG + eBOSS DR16 QSO, non-parametric reconstruction to k = 0.3 h Mpc⁻¹ | Martínez-Somonte et al. 2026, arXiv:2605.18615 | [src] |

Reading the table.

- With the cosmology fixed to Planck 2018, DESI DR1 shows an apparent 3σ global preference for a logarithmic feature at ω_log ≈ 15, driven by the LRG2 sample. It vanishes when the cosmological parameters are varied, and the authors attribute it to the DESI–Planck distance-scale tension: the feature's local wavelength matches the apparent BAO scale (arXiv:2610.10530). A feature search at fixed cosmology on data in tension with that cosmology is not interpretable.
- Some Planck PR3 feature "anomalies" shrink with the PR4 CamSpec likelihood (arXiv:2605.30236).
- In Planck + ACT + DESI the oscillation models fit better than ΛCDM but the Bayesian evidence moderately prefers ΛCDM (arXiv:2606.28310).
- Large-scale structure is competitive because oscillations survive non-linear evolution as well as the BAO do, so quasi-linear modes can be used (arXiv:1906.08758).
- **Forecasts**: DESI and Euclid improve on BOSS by up to an order of magnitude over a wider frequency range (arXiv:1906.08758); SO + LiteBIRD improve feature-amplitude bounds by more than an order of magnitude over Planck (arXiv:2605.30236).

The model-independent side of this subject, the binned P(k), is in section 3.

## 10. Cosmic birefringence
<!-- key: cosmic-birefringence -->

Isotropic birefringence is a uniform rotation β of the plane of linear polarisation, which converts E into B and produces C_ℓ^EB = ½ sin(4β) (C_ℓ^EE − C_ℓ^BB). It is not a prediction of inflation; it is in this skill because it is measured with the same polarisation data as r and probes parity-violating light fields. All values are 68% and in degrees.

| β (deg) | Significance of β ≠ 0 | Data and method | Citation | Flag |
|---|---|---|---|---|
| 0.35 ± 0.14 | 2.4σ (99.2%) | Planck 2018 (PR3) polarisation; miscalibration angles fitted jointly using the Galactic foreground EB | Minami and Komatsu 2020, arXiv:2011.11254 | [src] |
| 0.30 ± 0.11 | — (no cosmological significance assigned by the authors) | Planck PR4, nearly full sky | Diego-Palazuelos et al. 2022, arXiv:2201.07682 | [src] |
| 0.342 +0.094/−0.091 | 3.6σ (99.987%) | WMAP + Planck PR4, 23–353 GHz, nearly full sky | Eskilt and Komatsu 2022, arXiv:2205.13962 | [src] |
| 0.30 ± 0.05 | — (instrumental polarisation-angle systematic not included) | Planck legacy data, harmonic-space estimate | Ballardini et al. 2025, arXiv:2507.16714 | [src] |
| 0.215 ± 0.074 | 2.9σ | ACT DR6 EB and TB; priors on miscalibration angles from the ACT optics model; residual intensity-to-polarisation leakage marginalised | Diego-Palazuelos and Komatsu 2025, arXiv:2509.13654 | [src] |
| **0.277 ± 0.057** | **4.8σ** (3.5σ in the dust-robust variant) | ACT DR6 + Planck PR4 maps, including cross-spectra between the two telescopes, instrumental priors "at face value" | Eskilt 2026, arXiv:2608.06480 | [src] |

Reading the table.

- Three data sets (WMAP, Planck, ACT) and two calibration strategies (foreground-based self-calibration for the satellites, an optics-model prior for ACT) give the same sign and a similar size. Every paper in the table declines to claim a detection: Planck PR4 because β falls as the Galactic mask grows, which may be polarised foreground emission (arXiv:2201.07682); ACT because "there remain systematics in the ACT data that are not understood" (arXiv:2509.13654); the joint analysis because "unresolved systematics in the data must be understood before we can draw strong cosmological conclusions" (arXiv:2608.06480).
- The 4.8σ figure is conditional on the ACT instrumental priors. Obtaining β = 0 would require both the dust EB model and the instrumental priors to fail together (arXiv:2608.06480).
- The 0.30 ± 0.05 of Ballardini et al. has a smaller error than the other Planck values because it omits the polarisation-angle systematic; it must not be quoted as a 6σ detection.
- Frequency dependence: none found over 23–353 GHz (arXiv:2205.13962), which disfavours Faraday rotation. Scale dependence: a constant β is preferred by the Bayesian evidence, with no significant ℓ dependence (up to 1.8σ) (arXiv:2507.16714).
- BICEP/Keck cannot measure a constant β because its polarisation angle is self-calibrated by nulling EB. BK18 instead constrains a multipole-dependent rotation: a step in β(ℓ) is consistent with zero with an uncertainty below 0.15° (68%), and the axion–photon coupling in an early-dark-energy model is g = 0.11 ± 0.37 for f_EDE = 0.087 (BICEP/Keck XXI, arXiv:2603.06812) [src].
- Anisotropic birefringence is not detected. SPT-3G D1 BB spectra give A_CB < 1.2 × 10⁻⁴ (95%), or < 0.53 × 10⁻⁴ with a lensing-amplitude prior (Balkenhol et al. 2025, arXiv:2510.07928) [src]. ACT DR6 gives g_aγ < 4.9 × 10⁻² / H_I (Kramer et al. 2026, arXiv:2608.27458) [src].
- **Forecast**: LiteBIRD would detect β = 0.3° at 5σ to 13σ depending on the pipeline, the best case corresponding to a total error of about 0.02° (de la Hoz et al. 2025, arXiv:2503.22322; computed for the pre-reformation mission) [src]. **Forecast**: SO, LiteBIRD and a CMB-S4-like experiment could reduce the present uncertainty by a factor of about 7 (arXiv:2507.16714) [src]. **Forecast**: with SO SATs calibrated to 0.08° by the wire grid, cross-experiment correlations would calibrate the SO LAT to 0.10° and Planck to 0.17° at about 145 GHz without assuming β = 0 (Rigouzzo et al. 2026, arXiv:2606.11300) [src].

## 11. History of the key numbers
<!-- key: history-of-the-key-numbers -->

A value in the left column must not be quoted as current.

| Quantity | Superseded value(s) | Current value | What changed |
|---|---|---|---|
| n_s, ΛCDM | 0.9649 ± 0.0042 (Planck 2018, arXiv:1807.06211) — still the Planck-only reference | 0.9709 ± 0.0038 (P-ACT), 0.9679 ± 0.0033 (CMB-SPA), 0.974 ± 0.003 (P-ACT-LB) | small-scale ACT and SPT data; DESI BAO (arXiv:2503.14452, arXiv:2506.20707) |
| dn_s/dln k | −0.010 ± 0.004 (eBOSS Lyα + Planck, arXiv:1911.09073) | 0.0062 ± 0.0052 (P-ACT-LB, arXiv:2503.14454); 0.0014 ± 0.0041 (DESI DR1 P1D + CMB + BAO, arXiv:2601.21432) | ACT small scales; DESI P1D with marginalised systematics |
| r (95%) | < 0.12 (arXiv:1502.00612); < 0.056 (Planck 2018 + BK15); < 0.044 (PR4 + BK15, arXiv:2010.01139) | < 0.036 (BK18, arXiv:2110.00483); < 0.032 with Planck PR4 and BAO (arXiv:2112.07961) | BICEP3 95 GHz depth and 220 GHz dust lever arm |
| f_NL^local, CMB | 2.5 ± 5.7 (Planck 2015 T); 0.8 ± 5.0 (2015 T + E, preliminary) | −0.9 ± 5.1 (Planck 2018, arXiv:1905.05697); −0.1 ± 5.0 (PR4, arXiv:2504.00884) | validated polarisation; NPIPE maps |
| f_NL^local, LSS | −51 to +21 at 95% (eBOSS DR14); −12 ± 21 (eBOSS DR16, arXiv:2106.13725) | −3.6 +9.0/−9.1 (DESI DR1, arXiv:2411.17623) | volume: 1.19 million quasars and 1.63 million LRGs |
| f_NL^equil, f_NL^ortho, LSS | 940 ± 600, −170 ± 170 (BOSS, arXiv:2201.07238) | 200 ± 230, −24 ± 86 (DESI DR1 + BOSS with simulation priors, arXiv:2512.04266) | DESI volume and bias priors |
| Ω_K, CMB + BAO | 0.0007 ± 0.0019 (Planck 2018 + BAO, arXiv:1807.06209) | 0.0023 ± 0.0011 (DESI DR2 + CMB, arXiv:2503.14738) | DESI BAO; the central value moved to the open side |
| Ω_K, CMB only | −0.044 +0.018/−0.015 (Planck 2018 Plik) | −0.0107 +0.0064/−0.0053 (DESI's CMB combination, arXiv:2503.14738) | lensing reconstruction and newer likelihoods |
| β | 0.35 ± 0.14 (Planck PR3, arXiv:2011.11254); 0.30 ± 0.11 (PR4, arXiv:2201.07682) | 0.342 +0.094/−0.091 (WMAP + Planck, arXiv:2205.13962); 0.277 ± 0.057 (ACT + Planck, arXiv:2608.06480) | more frequencies; an independent ground-based data set |
| c_s (95%) | > 0.011 (WMAP 5, arXiv:0905.3746) | ≥ 0.021 (Planck 2018, arXiv:1905.05697) | Planck equilateral and orthogonal limits |

## 12. Not verified
<!-- key: not-verified -->

- The Planck 2018 running with BAO (−0.0041 ± 0.0067, quoted through ACT) was not read in the Planck paper; the value without BAO and the running of the running were read (section 2).
- Planck PR4 (HiLLiPoP, CamSpec) values of n_s were not read; they are in `cosmo-cmb`.
- The b_φ assumption behind f_NL^local = −0.1 ± 7.4 in arXiv:2512.04266 was not read in the paper (the eBOSS DR16 one, p = 1.6, was).
- ACT limits on fully correlated isocurvature and on the isocurvature spectral index were not read.
- SPT-3G D1 constraints on Ω_K, on the running and on isocurvature were not found in a search of the paper source (arXiv:2506.20707) and are not given.
- Planck 2018 feature-amplitude limits (per template) were not read; only the abstract statement is used.
- The trispectrum parameter τ_NL and the Planck limits on it were not looked up.
- No search was made for WMAP-era r, n_s or f_NL values; history tables start with Planck or with the first measurement read this session.
