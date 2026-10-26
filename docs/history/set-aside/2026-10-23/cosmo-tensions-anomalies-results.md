# Set aside from cosmo-tensions-anomalies/references/results.md

Numbers run of 2026-10-23 (plan of 2026-10-23, steps 1 and 3; owner's rule: no number computed by an agent). The blocks below held agent-computed values (Gaussian differences, quadrature sums, conversions). They are copied verbatim from the file as it stood at commit 2b5e381 before removal; line numbers are those of that version.

## Lines 54-69 (Section 1.2, Gaussian-difference table and its check)

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

Significances the papers themselves print, all in the one parameter H0 and without a named metric beyond "statistical significance" or "tension": 5.0σ for SH0ES 2022 against Planck, computed as 0.176 ± 0.035 mag in 5 log H0 (arXiv:2112.04510) [sec: h0]; for H0DN, 7.1σ against the flat-ΛCDM CMB value 67.24 ± 0.35 (Planck + SPT + ACT, Eq. 54 of the first version of arXiv:2506.20707) and 5.0σ against DESI DR2 BAO + BBN, 68.51 ± 0.58 (arXiv:2510.23823) [src: abstract, Sect. IV]; for SPT, against SH0ES taken as 73.17 ± 0.86: 6.2σ from SPT-3G D1 alone, 6.4σ from CMB-SPA, 4.9σ from the SPT TE/EE spectra alone (66.1 ± 1.2) (arXiv:2506.20707) [src: Sect. VII.2.2]; 4.5σ between DESI + BBN and SH0ES "independent of the CMB", which still assumes standard pre-recombination physics for r_d (arXiv:2503.14738) [src: Sect. VI].

The H0DN paper adopts 67.24 ± 0.35 for Planck + SPT + ACT, which is the first arXiv version of the CMB-SPA value; the second version reads 67.19 ± 0.38 [sec: cmb]. Both give 7.1σ against 73.50 ± 0.81 [der: (73.50 − 67.24) / sqrt(0.81² + 0.35²) = 7.09; (73.50 − 67.19) / sqrt(0.81² + 0.38²) = 7.05].

## Lines 104-139 (Section 2.2 with its derived columns, and Section 2.3)

### 2.2 S8 by probe, with one common derived difference
<!-- key: s8-by-probe-with-one-common-derived-difference -->

Columns "vs 0.836" and "vs 0.819" are Gaussian differences [der] against the combined-CMB endpoint (error 0.0125) and the Planck PR4 endpoint (error 0.014). A leading "+" means the probe lies above the endpoint.

| Probe | S8 | Tension as printed by the paper | vs 0.836 | vs 0.819 | Citation | Flag |
|---|---|---|---|---|---|---|
| KiDS-Legacy cosmic shear | 0.815 (+0.016/−0.021) | 0.76σ in S8; 0.73σ in Σ8 = σ8(Ω_m/0.3)^0.58 = 0.821 (+0.014/−0.016); marginal Hellinger distance to Planck Legacy; 1.01σ in Σ8 with band powers | 0.9 | 0.2 | Wright et al. 2025, arXiv:2503.19441 | [src: Sect. 6, Sect. 7] |
| DES Y6 cosmic shear, NLA | 0.798 (+0.014/−0.015) | parameter shift against Planck + ACT + SPT primary: 2.0σ in S8, 1.1σ full space (p = 0.28); suspiciousness 0.9σ | 2.0 | 1.0 | DES Collaboration 2026, arXiv:2602.10065 | [src: Sect. VI.2.1] |
| DES Y6 cosmic shear, TATT | 0.783 (+0.019/−0.015) | same metric: 2.3σ in S8, 1.7σ full space (p = 0.09); suspiciousness 1.4σ | 2.5 | 1.6 | arXiv:2602.10065 | [src: Sect. VI.2.1] |
| DES Y6 3×2pt | 0.789 ± 0.012 | parameter shift against Planck + ACT + SPT primary: 2.6σ in S8, 2.2σ in S8–Ω_m, 1.8σ full space (1.5σ in Y3); 1.0σ full space against Planck 2018 alone | 2.7 | 1.6 | DES Collaboration 2026, arXiv:2601.14559 | [src: Sect. V.2, Table 4] |
| HSC Y3 shear, DESI clustering redshifts | 0.804 (+0.019/−0.018) | "towards Planck" | 1.4 | 0.6 | Choppin de Janvry et al. 2025, arXiv:2511.18134 | [sec: wl] |
| DES Y3 shear, external IA and baryon calibration | 0.832 (+0.013/−0.017) | posterior moves up by 1.5σ | 0.2 | +0.6 | Bigwood et al. 2025, arXiv:2512.04209 | [sec: wl] |
| unWISE × ACT DR6 + Planck lensing | 0.810 ± 0.015 | consistent with the primary CMB | 1.3 | 0.4 | Farren et al. 2023, arXiv:2309.05659 | [sec: x] |
| DESI LRG × ACT DR6 + Planck PR4 lensing | 0.775 (+0.019/−0.022) | 1.6–2.2σ low | 2.5 | 1.8 | Sailer et al. 2024, arXiv:2407.04607 | [sec: x] |
| tSZ × galaxies, compiled ⟨b P_e⟩(z), FLAMINGO model | 0.72 ± 0.03 | — | 3.6 | 3.0 | Salcido et al. 2026, arXiv:2605.11083 | [sec: x] |
| eRASS1 cluster counts | 0.86 ± 0.01 | at the Planck level | +1.5 | +2.4 | Ghirardini et al. 2024, arXiv:2402.08458 | [sec: cl] |
| SPT clusters + DES and HST lensing | 0.795 ± 0.029 | 1.1σ from Planck 2018 | 1.3 | 0.7 | Bocquet et al. 2024, arXiv:2401.02075 | [sec: cl] |
| Planck PSZ2 + DES shear + Chandra | 0.791 (+0.023/−0.021) | 1.6σ from the CMB | 1.8 | 1.1 | Aymerich et al. 2025, arXiv:2509.02068 | [sec: cl] |
| KiDS-1000 AMICO clusters | 0.74 ± 0.03 | 2.8σ from Planck | 3.0 | 2.4 | Lesci et al. 2025, arXiv:2507.14285 | [src] |

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

## Lines 160-172 (Section 3.1, A_L table with derived distances)

Model: ΛCDM + A_L, one parameter; "distance from 1" is (A_L − 1)/σ unless the paper prints it.

| Value | Data | Distance from 1 | Citation | Flag |
|---|---|---|---|---|
| 1.180 ± 0.065 | Planck PR3 Plik TT,TE,EE + lowE | 2.7σ (paper) | arXiv:1807.06209 | [src: Sect. 2.2.1] |
| 1.185 ± 0.067 (A_2pt, T and E, no φφ) | Planck PR3, SPT rerun | 2.8σ [der] | arXiv:2506.20707 | [src: Sect. VII.2.3] |
| 1.095 ± 0.056 | Planck PR4 CamSpec | 1.7σ (as quoted by ACT) | arXiv:2503.14452 | [src: Sect. VIII.5] |
| 1.039 ± 0.052 | Planck PR4 HiLLiPoP | 0.75σ (as quoted by ACT) | arXiv:2309.10034 | [src: Sect. 11.1] |
| 1.007 ± 0.057 | ACT DR6 | 0.1σ [der] | arXiv:2503.14452 | [src: Sect. VIII.5] |
| 1.081 ± 0.043 | P-ACT | 1.9σ [der] | arXiv:2503.14452 | [src: Sect. VIII.5] |
| A_2pt = 0.991 (+0.083/−0.10) (T and E); A_lens = 0.972 (+0.079/−0.089) with A_2pt = A_recon | SPT-3G D1 | 0.1σ, 0.3σ below [der] | arXiv:2506.20707 | [src: Sect. VII.2.3, Eq. 67] |
| A_2pt = 1.016 (+0.048/−0.054) | SPT + ACT, T and E spectra | 0.3σ [der] | arXiv:2506.20707 | [src: Sect. VII.2.3] |
| A_2pt = 1.079 ± 0.038, A_recon = 1.041 ± 0.031; A_lens = 1.052 ± 0.032 coherent | CMB-SPA | A_2pt 2.1σ in one parameter [der]; 1.6σ in the (A_2pt, A_recon) plane (paper) | arXiv:2506.20707 | [src: Sect. VII.2.3, Eq. 69] |

## Line 195 (Section 3.2, derived PR4 distance)

Size: the BAO-preferred value is in "≃ 3–5σ tension with Planck low-ℓ polarization data when taken at face value": about 5σ at face value, about 3.8σ "when accounting for the prior width", one parameter (arXiv:2504.16932) [src: abstract, note 72]; against PR4, (0.090 − 0.058) / sqrt(0.012² + 0.006²) = 2.4σ [der]. Every Planck reprocessing from 2018 to 2023 lies in 0.051–0.063 [sec: cmb], with uncertainties from 0.005 to 0.009 depending on the likelihood and data combination (0.0086 for lowE alone, 0.0073 with TT,TE,EE and lensing, 0.006 for PR4) [src: Eq. 2 and Table 2 of arXiv:1807.06209; Eq. 14 of arXiv:2309.10034]. The τ question is not an anomaly in a measurement; it is the statement that one parameter, measured by one instrument, would absorb the CMB–BAO mismatch if it were wrong by about 0.03.

## Lines 259 and 262 (Section 5.2, ln 5 conversion)

| DESI DR2 + CMB + DES-Dovekie | odds "approximately 5:1", ln B ≈ 1.6 [der: ln 5] | arXiv:2511.07517 | [sec: de] |

The two evidence analyses differ for every supernova sample (DESY5: 4.88 against 3.32; Union3: 3.03 against 1.37; Pantheon+: −0.66 against −1.70; DES-Dovekie: about +1.6 against −0.30). Both use PolyChord and DESI's w0, wa priors; DESI substitutes H0 for θ_MC as a sampled parameter (arXiv:2503.14743) [src: App. A], and Ong et al. use Planck 2018 with CamSpec and convert ln B to an upper bound on the significance through B ≤ −1/(e p ln p) and σ = Φ⁻¹(1 − p/2) (arXiv:2511.10631) [src: Sect. II, Eqs. 1, 2]. Neither paper states the cause of the difference, and this file does not reconcile it. Quote the paper, not "the Bayes factor". DESI's own caution: a wider prior on w0, wa favours ΛCDM, but reversing the DESY5 ranking would need a prior range more than ten times wider in both parameters (arXiv:2503.14743) [src: App. A].

## Line 403 (Section 11, derived curvature significance)

| Ω_K | +0.0023 ± 0.0011 (2.1σ, open side [der, sec: inf]) | DESI DR2 BAO + CMB, ΛCDM + Ω_K | arXiv:2503.14738 | [sec: inf] |

## Line 43 (Section 1.1, quadrature total)

| Local | 70.39 ± 1.22 (stat) ± 1.33 (sys) ± 0.70 (σ_SN); total 1.94 [der, quadrature] | CCHP TRGB, 24 SN Ia calibrators, anchor NGC 4258 | Freedman et al. 2024, arXiv:2408.06153 | [src: Sect. I, Fig. 1] for the value; [sec: h0] for the sample |
