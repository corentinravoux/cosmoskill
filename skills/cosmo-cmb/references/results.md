# CMB primary anisotropies and lensing — current results

Scope: headline parameter constraints from Planck, ACT and SPT-3G spectra and
lensing, alone and combined, with the model stated for each; then the history
of the key numbers so that superseded values can be recognised.
Snapshot: 2026-10-14

Flags: `[src: <place>]` read in the cited paper at that place; `[sec: <place>]`
taken from the named secondary source at that place. Errors are 68% and
limits 95% unless stated. Years next to names are arXiv submission years.

Data-set names used below, as defined by the papers themselves:

- **Planck (SPT rerun)**: Planck PR3 TT/TE/EE + PR4 lensing + τ prior from
  PR4, as rerun by Camphuis et al. 2025 (arXiv:2506.20707).
- **Planck (ACT rerun)**: PR3 high-ℓ TT/TE/EE + SRoll2 low-ℓ EE, as rerun by
  Louis et al. 2025 (arXiv:2503.14452).
- **SPT-3G D1**: D1 TT/TE/EE + SPT-3G lensing (Ge et al. 2024) + τ prior.
- **ACT DR6 (SPT rerun)**: DR6 TT/TE/EE + ACT DR6 lensing + τ prior.
- **ACT (ACT's own)**: DR6 TT/TE/EE + Planck SRoll2 large-scale EE for the
  optical depth, no lensing reconstruction (Louis et al. 2025,
  arXiv:2503.14452, Table 5).
- **SPT+ACT**: the two above together. **CMB-SPA**: SPT+ACT + Planck.
- **P-ACT**: ACT DR6 + Planck PR3 cut at ℓ < 1000 (TT), ℓ < 600 (TE, EE) +
  low-ℓ TT + SRoll2 (arXiv:2503.14452, Sect. VIII.3). **W-ACT**: ACT DR6 + WMAP9 + SRoll2.
  **P-ACT-LB / -LB2**: P-ACT + ACT and Planck lensing + DESI DR1 / DR2 BAO.

---

## 1. Base ΛCDM from the CMB alone
<!-- key: base-lambdacdm-from-the-cmb-alone -->

All rows of this table are from Table 1 of Camphuis et al. 2025
(arXiv:2506.20707) [src]. Every column includes T&E spectra, a lensing
reconstruction and the same τ prior, which makes the columns comparable.
θ uses the CLASS definition.

From arXiv:2506.20707, Table 1 (Sect. II):

| Parameter | Planck (SPT rerun) | SPT-3G D1 | ACT DR6 (SPT rerun) | SPT+ACT | SPT+Planck | CMB-SPA |
|---|---|---|---|---|---|---|
| 10⁴ θ_s^⋆ | 104.184 ± 0.029 | 104.171 ± 0.060 | 104.157 ± 0.030 | 104.158 ± 0.025 | 104.176 ± 0.026 | 104.161 ± 0.023 |
| 100 Ω_b h² | 2.238 ± 0.014 | 2.221 ± 0.020 | 2.257 ± 0.016 | 2.247 ± 0.013 | 2.230 ± 0.011 | 2.2398 ± 0.0095 |
| 100 Ω_c h² | 11.98 ± 0.11 | 12.14 ± 0.16 | 12.26 ± 0.17 | 12.22 ± 0.12 | 12.050 ± 0.089 | 12.028 ± 0.094 |
| n_s | 0.9657 ± 0.0040 | 0.951 ± 0.011 | 0.9682 ± 0.0069 | 0.9671 ± 0.0058 | 0.9636 ± 0.0035 | 0.9679 ± 0.0033 |
| ln(10¹⁰ A_s) | 3.042 ± 0.011 | 3.054 ± 0.015 | 3.038 ± 0.012 | 3.042 ± 0.011 | 3.046 ± 0.010 | 3.047 ± 0.010 |
| τ | 0.0535 ± 0.0056 | 0.0506 ± 0.0059 | 0.0513 ± 0.0060 | 0.0514 ± 0.0059 | 0.0538 ± 0.0054 | 0.0549 ± 0.0055 |
| H₀ [km/s/Mpc] | 67.41 ± 0.49 | 66.66 ± 0.60 | 66.51 ± 0.64 | 66.59 ± 0.46 | 67.07 ± 0.38 | 67.19 ± 0.38 |
| Ω_m | 0.3145 ± 0.0067 | 0.3246 ± 0.0091 | 0.330 ± 0.010 | 0.3277 ± 0.0072 | 0.3189 ± 0.0054 | 0.3175 ± 0.0055 |
| σ₈ | 0.8099 ± 0.0051 | 0.8158 ± 0.0058 | 0.8171 ± 0.0055 | 0.8169 ± 0.0042 | 0.8132 ± 0.0042 | 0.8137 ± 0.0037 |
| r_d [Mpc] | 147.13 ± 0.25 | 146.92 ± 0.47 | 146.20 ± 0.46 | 146.43 ± 0.34 | 147.06 ± 0.23 | 147.00 ± 0.24 |
| 10⁹ A_s e^(−2τ) | 1.883 ± 0.010 | 1.915 ± 0.021 | 1.884 ± 0.013 | 1.889 ± 0.011 | 1.8890 ± 0.0092 | 1.8871 ± 0.0079 |
| Age [Gyr] | 13.797 ± 0.022 | 13.826 ± 0.027 | 13.797 ± 0.021 | 13.805 ± 0.016 | 13.812 ± 0.017 | 13.805 ± 0.014 |

Notes on this table.

- The CMB-SPA column changed between arXiv versions: H₀ went from
  67.24 ± 0.35 (v1) to 67.19 ± 0.38 (v2) and n_s from 0.9684 ± 0.0030 (v1)
  to 0.9679 ± 0.0033 (v2) (arXiv:2506.20707v1 and v2) [src: Sect. II of
  each version]. Quote the v2 values and say so.
- The τ row is a posterior under a common prior, not six measurements.
- SPT-3G D1 alone is 6.2σ from the SH0ES value used by the paper; CMB-SPA
  is 6.4σ (arXiv:2506.20707) [src: Sect. II]. The paper prints the n_s = 1
  exclusion for CMB-SPA as 9.9σ in Sect. II and as 9.8σ in Sect. VII.2.2.
- Parameter-level agreement over (H₀, Ω_b h², Ω_c h², n_s, A_s e^(−2τ)):
  SPT-3G D1 versus Planck 0.4σ, versus ACT DR6 1.1σ (1.4σ when the
  Planck-calibrated amplitude is excluded) (arXiv:2506.20707) [src: Sect. VII.2.2].

ACT's own combinations, base ΛCDM (Louis et al. 2025, arXiv:2503.14452) [src].
The "ACT" rows are the ACT-alone column of the paper's Table 5 (ACT DR6 +
SRoll2 low-ℓ EE), read on 2026-10-08 in the current arXiv PDF because the
table is an image in the LaTeX source; the W-ACT, P-ACT and Planck columns of
the same table reproduce the values the paper prints in its text. The other
rows were read in the text on 2026-10-23, at the place given.

From arXiv:2503.14452:

| Quantity | Value | Data set | Place read |
|---|---|---|---|
| H₀ | 66.11 ± 0.79 | ACT (ACT's own) | Table 5 (PDF) |
| H₀ | 67.62 ± 0.50 | P-ACT | Sect. II |
| H₀ | 68.22 ± 0.36 | P-ACT-LB (DESI DR1) | abstract; Sect. II |
| H₀ | 68.43 ± 0.27 | P-ACT-LB2 (DESI DR2) | abstract; Sect. II, footnote 4 |
| H₀ | 66.78 ± 0.68 | W-ACT | Sect. VIII.2, Eq. 38 |
| H₀ | 67.31 ± 0.61 | Planck (ACT rerun) | Sect. VIII.2, Eq. 38 |
| Ω_b h² | 0.02259 ± 0.00017 | ACT (ACT's own) | Table 5 (PDF) |
| Ω_b h² | 0.02250 ± 0.00011 | P-ACT | Sect. VIII.3 |
| Ω_b h² | 0.02263 ± 0.00012 | W-ACT | Sect. VIII.2, Eq. 37 |
| Ω_b h² | 0.02237 ± 0.00015 | Planck (ACT rerun) | Sect. VIII.2, Eq. 37 |
| n_s | 0.9666 ± 0.0077 | ACT (ACT's own) | Table 5 (PDF) |
| n_s | 0.9709 ± 0.0038 | P-ACT | Sect. VIII.3 |
| n_s | 0.9660 ± 0.0046 | W-ACT | Sect. VIII.2, Eq. 36 |
| n_s | 0.9651 ± 0.0044 | Planck (ACT rerun) | Sect. VIII.2, Eq. 36 |
| n_s | 0.974 ± 0.003 | P-ACT-LB | abstract; Sect. II |
| σ₈ | 0.815 ± 0.006 | P-ACT | Sect. VIII.4 |
| σ₈ | 0.813 ± 0.005 | P-ACT-LB | abstract; Sect. VIII.4 |
| Ω_m | 0.312 ± 0.007 | P-ACT | Sect. VIII.4, Eq. 44 |
| Ω_m | 0.303 ± 0.005 | P-ACT-LB | Sect. VIII.4, Eq. 44 |
| Ω_m | 0.3003 ± 0.0035 | P-ACT-LB2 | Sect. VIII.4 |
| S₈ | 0.830 ± 0.014 | P-ACT | Sect. VIII.4 |
| r_d | 147.1 ± 0.3 Mpc | P-ACT | Sect. VIII.4, Eq. 42 |
| H₀ from spectra split | TT 68.47 ± 0.91, TE 66.92 ± 0.76, EE 67.6 ± 1.2 | P-ACT | Sect. VIII.3, table |

The two "ACT alone" entries of this file are not the same fit: ACT's own
(H₀ = 66.11 ± 0.79, n_s = 0.9666 ± 0.0077) uses the DR6 spectra with the
SRoll2 low-ℓ EE likelihood and no lensing reconstruction, while the SPT rerun
of the first table (66.51 ± 0.64, 0.9682 ± 0.0069) adds the ACT DR6 lensing
reconstruction and a τ prior (arXiv:2503.14452, Table 5; arXiv:2506.20707,
Table 1). Say which one is quoted.

Further ACT statements (arXiv:2503.14452): the acoustic scale is measured
to 0.02% by P-ACT [src: Sect. II]; W-ACT excludes n_s = 1 at more than 7σ
independently of Planck high-ℓ data [src: Sect. VIII.2]; P-ACT EE alone
excludes H₀ = 73 at more than 4σ within ΛCDM [src: Sect. VIII.4];
goodness of fit of ΛCDM to ACT is −2 ln L = 1591 for 1617 degrees of
freedom (PTE 67%) [src: Sect. VIII.1]. ACT versus Planck in the
four-dimensional space excluding τ and A_s: 1.6σ against PR3, 2.5σ against
NPIPE [src: Sect. VIII.2].

Planck-only reference values, base ΛCDM; PR3 column from arXiv:1807.06209
(abstract), PR4 column from arXiv:2309.10034 (Table 5):

| Quantity | Planck 2018 (PR3, combined analysis as quoted in the abstract) | Planck PR4 HiLLiPoP+LoLLiPoP (TTTEEE) |
|---|---|---|
| Ω_b h² | 0.0224 ± 0.0001 | 0.02226 ± 0.00013 |
| Ω_c h² | 0.120 ± 0.001 | 0.1188 ± 0.0012 |
| 100 θ* | 1.0411 ± 0.0003 | 1.04108 ± 0.00026 |
| n_s | 0.965 ± 0.004 | 0.9681 ± 0.0039 |
| τ | 0.054 ± 0.007 | 0.0580 ± 0.0062 |
| H₀ | 67.4 ± 0.5 | 67.64 ± 0.52 |
| σ₈ | 0.811 ± 0.006 | 0.8070 ± 0.0065 |
| S₈ | — | 0.819 ± 0.014 |
| Source | arXiv:1807.06209 abstract [src] | arXiv:2309.10034 Table 5 [src] |

PR4 with lensing and BAO (6dF, SDSS DR7, DR16): H₀ = 67.81 ± 0.38,
n_s = 0.9690 ± 0.0035, τ = 0.0605 ± 0.0059 (arXiv:2309.10034) [src: Sect. 10, table].

## 2. CMB + DESI BAO in ΛCDM
<!-- key: cmb-desi-bao-in-lambdacdm -->

From arXiv:2506.20707, Table 6:

| Quantity | SPT-3G D1 + DESI DR2 | CMB-SPA + DESI DR2 | Source |
|---|---|---|---|
| H₀ | 68.21 ± 0.31 | 68.10 ± 0.24 | arXiv:2506.20707 Table 6 [src] |
| Ω_m | 0.3017 ± 0.0039 | 0.3045 ± 0.0033 | same |
| n_s | 0.949 ± 0.012 | 0.9726 ± 0.0028 | same |
| τ | 0.0559 ± 0.0056 | 0.0613 ± 0.0051 | same |
| σ₈ | 0.8079 ± 0.0059 | 0.8122 ± 0.0039 | same |
| r_d [Mpc] | 147.99 ± 0.33 | 147.50 ± 0.18 | same |

Adding DESI pulls Ω_m down, and with it τ and n_s up (τ from 0.0549 to
0.0613, n_s from 0.9679 to 0.9726 for CMB-SPA) (arXiv:2506.20707) [src:
Tables 1 and 6]. That shift is the
parameter-level face of the CMB–BAO discrepancy.

The discrepancy itself, in ΛCDM, depends on which CMB data are used:

| CMB data | Distance from DESI | Source |
|---|---|---|
| DESI's own CMB combination vs DESI DR2 | 2.3σ | DESI Collaboration 2025, arXiv:2503.14738 [src: abstract] |
| P-ACT vs DESI DR2 | 1.6σ | arXiv:2503.14452 [src: abstract] |
| CMB-SPA vs DESI DR2 (Ω_m–h r_d plane) | 2.8σ | arXiv:2506.20707 [src: abstract; Sect. VII.3] |
| SPT+Planck vs DESI DR2 | 3.0σ | arXiv:2506.20707 [src: Sect. VII.3] |
| SPT+ACT vs DESI DR2 | 3.7σ | arXiv:2506.20707 [src: Sect. VII.3] |
| CMB vs DESI as summarised by Sailer et al. | 2.2σ | arXiv:2504.16932 [src: abstract] |

With the 2026 SPT-3G D1 quadratic-estimator lensing in place of the earlier
SPT lensing, the preference for curvature and for (w₀, w_a) ≠ (−1, 0) from
CMB + DESI drops to about 2σ [src] (Omori et al. 2026, arXiv:2608.31136).
Dark-energy conclusions belong to `cosmo-dark-energy-modified-gravity`.

## 3. Lensing amplitude in the spectra (A_L and relatives)
<!-- key: lensing-amplitude-in-the-spectra-al-and -->

| Value | Data and estimator | Model | Source | Flag |
|---|---|---|---|---|
| A_L = 1.180 ± 0.065 (2.7σ) | Planck PR3 Plik TT,TE,EE+lowE | ΛCDM+A_L | arXiv:1807.06209 | [src: Sect. 2.2.1] |
| A_L = 1.142 ± 0.066 (2.1σ) | same, spectrum-based polarisation-efficiency corrections | ΛCDM+A_L | arXiv:1807.06209 | [src: Sect. 2.2.1] |
| A_L differs from 1 at ≤ 2.2σ | CamSpec PR3, 80% sky | ΛCDM+A_L | Efstathiou & Gratton 2019, arXiv:1910.00483 | [src: abstract] |
| A_L = 1.095 ± 0.056 (1.7σ) | CamSpec PR4 TTTEEE | ΛCDM+A_L | Rosenberg et al. 2022, arXiv:2205.10869, Table 6 (1.7σ as quoted in arXiv:2503.14452) | [src: Table 6] |
| A_L = 1.039 ± 0.052 | HiLLiPoP PR4 TTTEEE | ΛCDM+A_L | arXiv:2309.10034 | [src: abstract] |
| A_L = 1.037 ± 0.037 | HiLLiPoP PR4 TTTEEE + PR4 lensing | ΛCDM+A_L | arXiv:2309.10034 | [src: Sect. 11.1] |
| A_lens = 1.01 ± 0.11 | ACT DR4 | ΛCDM+A_lens | Aiola et al. 2020, arXiv:2007.07288, as quoted in arXiv:2503.14452 | [sec: Sect. VIII.5] |
| A_lens = 1.007 ± 0.057 | ACT DR6 | ΛCDM+A_lens | arXiv:2503.14452 Eq. 45 | [src] |
| A_lens = 1.08 (+0.10/−0.12), 1.24 (+0.18/−0.22), 0.89 (+0.10/−0.23) | ACT DR6 TT, TE, EE separately | ΛCDM+A_lens | arXiv:2503.14452 | [src: Sect. VIII.5] |
| A_lens = 1.043 ± 0.049 | W-ACT | ΛCDM+A_lens | arXiv:2503.14452 | [src: Sect. VIII.5] |
| A_lens = 1.081 ± 0.043 | P-ACT | ΛCDM+A_lens | arXiv:2503.14452 | [src: Sect. VIII.5] |
| A_lens = 1.016 (+0.048/−0.054) | SPT+ACT T&E | ΛCDM+A_lens | arXiv:2506.20707 | [src: Sect. II] |
| A_2pt = 0.986 (+0.078/−0.097), A_recon = 0.974 (+0.081/−0.11) | SPT-3G D1 | ΛCDM+A_2pt+A_recon | arXiv:2506.20707 | [src: Sect. VII.2.3] |
| A_2pt = 1.026 ± 0.048, A_recon = 0.990 ± 0.050 | SPT+ACT | same | arXiv:2506.20707 | [src: Sect. VII.2.3] |
| A_2pt = 1.079 ± 0.038, A_recon = 1.041 ± 0.031 | CMB-SPA | same | arXiv:2506.20707 | [src: Sect. VII.2.3] |
| A_lens = 0.972 (+0.079/−0.089); 1.011 (+0.045/−0.051); 1.052 ± 0.032 | SPT-3G D1; SPT+ACT; CMB-SPA, with A_2pt = A_recon | ΛCDM+A_lens | arXiv:2506.20707 Eqs. 67–69 | [src] |
| A_L = 1.087 ± 0.035; 1.053 ± 0.034 | Planck PR3; PR4, each + lensing + non-CMB data without DESI | ΛCDM+A_L | de Cruz Pérez et al. 2026, arXiv:2604.03756 | [src: abstract] |

Reading the table. Ground-based data alone show no excess. The excess is a
Planck temperature feature: the combined ACT+SPT TT posterior mean lies
2.3 standard deviations below the value preferred by Planck TT
(arXiv:2506.20707) [src: Sect. VII.2.3], and an oscillatory residual in
Planck PR3 TT over 1000 < ℓ < 2000 was identified as driving the preference
(arXiv:2503.14452) [sec: Sect. VIII.5]. It has not vanished from
combinations that keep the full Planck TT range: the CMB-SPA A_2pt
(1.079 ± 0.038) and the P-ACT A_lens (1.081 ± 0.043) both lie above unity
(table above). SPT states that the CMB-SPA result is consistent with ΛCDM
at 1.6σ in the (A_2pt, A_recon) plane (arXiv:2506.20707) [src: Sect. VII.2.3].

## 4. Lensing reconstruction
<!-- key: lensing-reconstruction -->

| Quantity | Value | Data | Source | Flag |
|---|---|---|---|---|
| Detection significance | 40σ (9σ from polarisation alone) | Planck 2018 | arXiv:1807.06210 | [src: abstract] |
| σ₈ Ω_m^0.25 | 0.589 ± 0.020 | Planck 2018 lensing + weak priors | arXiv:1807.06210 | [src: abstract] |
| Amplitude vs Planck 2018 best fit | 1.004 ± 0.024 | Planck PR4 | Carron et al. 2022, arXiv:2206.07773 | [src: abstract] |
| σ₈ Ω_m^0.25 | 0.599 ± 0.016 | Planck PR4 lensing + priors | arXiv:2206.07773 | [src: abstract] |
| σ₈; H₀; Ω_m | 0.814 ± 0.016; 68.1 (+1.0/−1.1); 0.313 (+0.014/−0.016) | Planck PR4 lensing + BAO | arXiv:2206.07773 | [src: abstract] |
| A_lens vs Planck 2018 | 1.013 ± 0.023 (43σ, 2.3%) | ACT DR6, 9400 deg², 40 < L < 763 | Qu et al. 2023, arXiv:2304.05202 | [src: abstract; Sect. VI.1] |
| S₈^CMBL ≡ σ₈(Ω_m/0.3)^0.25 | 0.818 ± 0.022 | ACT DR6 | arXiv:2304.05202 | [src: abstract] |
| S₈^CMBL | 0.813 ± 0.018 | ACT DR6 + Planck PR4 | arXiv:2304.05202 | [src: abstract] |
| Amplitude vs Planck 2018 | 1.020 ± 0.060 | SPT-3G 2018, temperature only, 1500 deg² | Pan et al. 2023, arXiv:2308.11608 | [src: abstract] |
| σ₈ Ω_m^0.25 | 0.595 ± 0.026 | SPT-3G 2018 lensing | arXiv:2308.11608 | [src: abstract] |
| S₈ | 0.850 ± 0.017 | SPT-3G 2019–2020 polarisation-only MUSE (unlensed EE + φφ) | Ge et al. 2024, arXiv:2411.06000 | [src: abstract] |
| H₀ | 66.81 ± 0.81 | same | arXiv:2411.06000 | [src: abstract] |
| A_lens^recon vs P-ACT best fit | 1.025 ± 0.017 (S/N 61) | ACT DR6 + SPT-3G + Planck PR4 | Qu et al. 2025, arXiv:2504.20038 | [src: abstract] |
| S₈^CMBL | 0.825 (+0.015/−0.013) | same | arXiv:2504.20038 | [src: abstract] |
| σ₈ | 0.829 ± 0.009 | same + DESI BAO | arXiv:2504.20038 | [src: abstract] |
| H₀ (sound-horizon independent) | 66.4 ± 2.5 | same + uncalibrated Pantheon+ | arXiv:2504.20038 | [src: abstract] |
| σ₈ Ω_m^0.25 | 0.6046 ± 0.0096 | SPT-3G D1 GMV quadratic estimator | Omori et al. 2026, arXiv:2608.31136 | [src: abstract] |
| σ₈ Ω_m^0.25 | 0.6020 ± 0.0084 | SPT-3G D1 + ACT DR6 + Planck PR4 lensing | arXiv:2608.31136 | [src: abstract] |
| Amplitude vs CMB-SPA best fit | unity at 2% precision | SPT-3G D1 | arXiv:2608.31136 | [src] |
| S₈ | 0.811 ± 0.011 | CMB lensing + DES Y3 3×2pt | arXiv:2608.31136 | [src: abstract] |

All models are flat ΛCDM. Lensing-only constraints assume priors on Ω_b h²
and n_s. No CMB lensing reconstruction shows a low amplitude; cross-
correlations with galaxies are covered in `cosmo-cmb-lss-cross-correlations`.

## 5. Optical depth τ
<!-- key: optical-depth-tau -->

| τ | Data | Source | Flag |
|---|---|---|---|
| 0.066 ± 0.016 | Planck 2015 TT + lensing + LFI polarisation | arXiv:1502.01589 | [src: abstract] |
| 0.054 ± 0.007 | Planck 2018 combined | arXiv:1807.06209 | [src: abstract] |
| 0.0566 (+0.0053/−0.0062) | SRoll2 low-ℓ polarisation only | Pagano et al. 2019, arXiv:1908.09856 | [src: abstract] |
| 0.059 ± 0.006 | SRoll2 + Planck TT + high-ℓ | arXiv:1908.09856 | [src: abstract] |
| 0.051 ± 0.006 | NPIPE large-scale polarisation | arXiv:2007.04997 | [src: abstract] |
| 0.0627 (+0.0050/−0.0058) | SRoll2 momento TTTEEE low-ℓ + CamSpec | de Belsunce et al. 2021, arXiv:2103.14378 | [src: abstract] |
| 0.058 ± 0.006 | PR4 LoLLiPoP + HiLLiPoP | arXiv:2309.10034 | [src: Sect. 6] |
| 0.053 (+0.018/−0.019) | CLASS 90 GHz × Planck, ground-based | Li et al. 2025, arXiv:2501.11904 | [src: abstract] |
| 0.090 ± 0.012 | DESI BAO + high-ℓ CMB + CMB lensing, no low-ℓ EE | Sailer et al. 2025, arXiv:2504.16932 | [src: abstract] |
| 0.091 ± 0.011 | CMB without low-ℓ EE and lensing constraints, Σm_ν = 0.06 eV | Jhaveri et al. 2025, arXiv:2504.21813 | [src: abstract] |
| 0.0552 (+0.0019/−0.0026 stat) (+0.0075/−0.0049 sys) | Planck without low-ℓ EE + x_HI(z) from Lyα forest and damping wings | Kageura et al. 2026, arXiv:2601.09644 | [src: abstract] |
| 0.067 ± 0.011 | CMB without low-ℓ polarisation + BAO + quasar damping wings and dark pixels, dynamical dark energy | Montero-Camacho & Mao 2026, arXiv:2607.26373 | [src: abstract] |

SRoll2 corresponds to a mid-point reionisation redshift 8.14 ± 0.61
(arXiv:1908.09856) [src: abstract]. The one-sided 95% limits that frame the debate: Planck
primary data give τ < 0.0696, while all CMB without large-angle
polarisation plus BAO gives τ > 0.074 (Jhaveri et al. 2026,
arXiv:2606.20795) [src: abstract].

## 6. Light relics and neutrino mass
<!-- key: light-relics-and-neutrino-mass -->

N_eff, with BBN consistency for Y_P; ΛCDM+N_eff; standard value 3.044
(arXiv:2506.20707, Sect. VII.2.4).

| N_eff | Data | Source | Flag |
|---|---|---|---|
| 3.84 ± 0.40 | WMAP9 + high-ℓ CMB + BAO + H₀ | Hinshaw et al. 2012, arXiv:1212.5226 | [src: abstract] |
| 3.15 ± 0.23 | Planck 2015 + other data | arXiv:1502.01589 | [src: abstract] |
| 3.00 (+0.57/−0.53), 95% | Planck 2018 TT+lowE | arXiv:1807.06209 | [src: Sect. 7.1] |
| 2.92 (+0.36/−0.37), 95% | Planck 2018 TT,TE,EE+lowE | arXiv:1807.06209 | [src: Sect. 7.1] |
| 2.89 ± 0.19 | Planck 2018 (conclusions) | arXiv:1807.06209 | [src] |
| 2.99 ± 0.17 | Planck 2018 + BAO | arXiv:1807.06209 | [src: abstract] |
| 2.60 (+0.21/−0.29) | ACT DR6 | Calabrese et al. 2025, arXiv:2503.14454 | [src: Sect. VI.1.1] |
| 2.73 ± 0.14 | P-ACT | arXiv:2503.14454 | [src: Sect. VI.1.1] |
| 2.86 ± 0.13 | P-ACT-LB | arXiv:2503.14454 | [src: abstract] |
| 2.89 ± 0.11 | P-ACT-LB + primordial abundances | arXiv:2503.14454 | [src: abstract] |
| 3.18 (+0.29/−0.33) | SPT-3G D1 | arXiv:2506.20707 Eq. 71 | [src] |
| 2.58 (+0.22/−0.25) | ACT DR6 (SPT rerun) | arXiv:2506.20707 | [src: Sect. VII.2.4] |
| 2.78 ± 0.17 | SPT+ACT | arXiv:2506.20707 | [src: Sect. VII.2.4, Eq. 72] |
| 2.82 ± 0.12 | CMB-SPA | arXiv:2506.20707 | [src: Sect. VII.2.4, Eq. 73] |
| 3.23 (+0.35/−0.34), 95% | DESI DR2 BAO + CMB | Elbers et al. 2025, arXiv:2503.14744 | [src: abstract] |

ACT also reports ΔN_eff < 0.32 (ACT), < 0.14 (P-ACT), < 0.17 (P-ACT-LB)
for additional species with N_eff ≥ 3.044, and a one-tail N_eff < 3.08 for
P-ACT-LB (arXiv:2503.14454) [src: Sect. VI.1.1, Eqs. 31 and 32]. Other ACT
DR6 early-universe numbers from the same paper: dn_s/dlnk = 0.0062 ± 0.0052
and N_idr < 0.134 [src: abstract]; Y_P = 0.2312 ± 0.0092 (P-ACT-LB)
[src: Sect. VI.2.2, Eq. 45]; T_CMB = 2.698 ± 0.016 K (P-ACT-LB) [src:
Sect. V.4, Eq. 28].

Σm_ν, 95% upper limits, ΛCDM+Σm_ν unless stated.

| Limit [eV] | Data | Source | Flag |
|---|---|---|---|
| < 0.44 | WMAP9 + high-ℓ CMB + BAO + H₀ | arXiv:1212.5226 | [src: abstract] |
| < 0.23 | Planck 2015 + other data | arXiv:1502.01589 | [src: abstract] |
| < 0.54 | Planck 2018 TT+lowE (CMB alone) | arXiv:1807.06209 | [src: Sect. 7.5.1, Eq. 56a] |
| < 0.26 | Planck 2018 TT,TE,EE+lowE (CMB alone) | arXiv:1807.06209 | [src: Sect. 7.5.1, Eq. 56b] |
| < 0.60 | Planck lensing + BAO + θ_MC (no spectra) | arXiv:1807.06209 | [src: Sect. 7.5.1, Eq. 59] |
| < 0.12 | Planck 2018 + BAO | arXiv:1807.06209 | [src: abstract] |
| < 0.30 | SPT-3G 2018 spectra + lensing + BAO | arXiv:2308.11608 | [src: abstract] |
| < 0.075 | Planck + ACT + SPT (2024) + BAO | arXiv:2411.06000 | [src: abstract] |
| < 0.089 | P-ACT-LB (DESI DR1) | arXiv:2503.14454 v2 | [src: Sect. VI.1.1, Eq. 33] |
| < 0.088 | W-ACT-LB | arXiv:2503.14454 | [src: Sect. VI.1.1] |
| < 0.13 | P-ACT + lensing + BOSS BAO | arXiv:2503.14454 | [src: Sect. VI.1.1, Eq. 34] |
| < 0.23 | P-ACT + lensing + SNe, no BAO | arXiv:2503.14454 | [src: Sect. VI.1.1] |
| < 0.064 | DESI DR2 BAO + CMB | arXiv:2503.14738 (0.0642 in arXiv:2503.14744) | [src: abstract] |
| < 0.16 | DESI DR2 BAO + CMB, w₀w_a CDM | arXiv:2503.14738 | [src: abstract] |
| < 0.072 | CMB-SPA + SPT-3G D1 QE lensing + DESI DR2 | arXiv:2608.31136 | [src: abstract] |

The ACT extended-models paper (arXiv:2503.14454) exists with two values.
The abstract returned by the arXiv API on 2026-10-23 quotes 0.082 eV; the
abstract and Eq. 33 of the current HTML rendering quote 0.089 eV [src:
abstract; Sect. VI.1.1, Eq. 33]. The INSPIRE record still showed 0.082 on
2026-10-07.

## 7. Curvature
<!-- key: curvature -->

| Ω_K | Data | Source | Flag |
|---|---|---|---|
| −0.0027 (+0.0039/−0.0038) | WMAP9 + external | arXiv:1212.5226 | [src: abstract] |
| −0.044 (+0.018/−0.015) | Planck PR3 Plik, spectra only | Planck 2018, as quoted in arXiv:2309.10034 | [sec: Sect. 11.2] |
| −0.025 (+0.013/−0.010) | CamSpec PR4 TTTEEE, spectra only | Rosenberg et al. 2022, arXiv:2205.10869, Table 6 | [src: Table 6] |
| −0.012 ± 0.010 | HiLLiPoP PR4 TTTEEE | arXiv:2309.10034 | [src: abstract] |
| 0.001 ± 0.002 | Planck 2018 + BAO | arXiv:1807.06209 | [src: abstract] |
| 0.0004 ± 0.0018 | Planck (CamSpec) + BAO | Efstathiou & Gratton 2020, arXiv:2002.06892 | [src: abstract] |
| 0.014 (+0.023/−0.026), 95% | SPT-3G 2018 spectra + lensing | arXiv:2308.11608 | [src: abstract] |

## 8. Tensor modes and parity (status only)
<!-- key: tensor-modes-and-parity-status-only -->

| Quantity | Value | Data | Source | Flag |
|---|---|---|---|---|
| r_0.05 | < 0.12 | BICEP2/Keck + Planck joint analysis | arXiv:1502.00612 | [src: abstract] |
| r_0.05 | < 0.036, σ(r) = 0.009 | BICEP/Keck through 2018 (BK18) + WMAP + Planck | arXiv:2110.00483 | [src: abstract] |
| r | < 0.032 | BK18 + Planck PR4 + BAO, ΛCDM parameters free | Tristram et al. 2021, arXiv:2112.07961 | [src: abstract] |
| Lensing B modes | 7.0σ | BICEP2/Keck + Planck | arXiv:1502.00612 | [src: abstract] |
| Residual lensing BB after template delensing | A_lens^res ≃ 0.48 over 20 ≤ ℓ ≤ 200 | SPT-3G D1 + Planck CIB template | Nakato et al. 2026, arXiv:2608.06343 | [src: abstract] |
| Birefringence angle β | 0.215° ± 0.074° (2.9σ) | ACT DR6 EB and TB | Diego-Palazuelos & Komatsu 2025, arXiv:2509.13654 | [src: abstract] |

BK18 remains the most constraining published B-mode data set at the
snapshot date; no BICEP/Keck result with data after 2018 was found in the
searches run on 2026-10-07. Inflation-model implications belong to
`cosmo-inflation-primordial`.

## 9. Secondary anisotropy numbers quoted in primary-CMB papers
<!-- key: secondary-anisotropy-numbers-quoted-in-primary -->

| Quantity | Value | Source | Flag |
|---|---|---|---|
| D_3000^tSZ at 143 GHz | 4.91 ± 0.37 μK² | Chaubal et al. 2026, arXiv:2601.20551 | [src: abstract] |
| D_3000^kSZ | 1.75 ± 0.86 μK² | arXiv:2601.20551 | [src: abstract] |
| Duration of reionisation | Δz(25–75%) < 3.8 (95%, semi-analytic model) | arXiv:2601.20551 | [src: Sect. 4] |
| Duration of reionisation | Δz_rei < 4.4 (conservative, ACT DR6 kSZ) | Beringue et al. 2025, arXiv:2506.06274 | [src: abstract] |

These depend on the tSZ–CIB correlation model [src] (arXiv:2601.20551);
the physics belongs to `cosmo-cmb-lss-cross-correlations` and
`cosmo-reionization-21cm`.

## 10. History of the key numbers
<!-- key: history-of-the-key-numbers -->

H₀ from the CMB in ΛCDM:

| Year | H₀ | Data | Source | Status |
|---|---|---|---|---|
| 2015 | 67.8 ± 0.9 | Planck 2015 TT + lensing | arXiv:1502.01589 [src: abstract] | superseded |
| 2018 | 67.4 ± 0.5 | Planck 2018 | arXiv:1807.06209 [src: abstract] | reference Planck-only value |
| 2020 | 67.6 ± 1.1 | ACT DR4 + WMAP | arXiv:2007.07288 [src: abstract] | superseded by DR6 |
| 2020 | 67.9 ± 1.5 | ACT DR4 alone | arXiv:2007.07288 [src: abstract] | superseded by DR6 |
| 2022 | 68.3 ± 1.5 | SPT-3G 2018 TT/TE/EE | Balkenhol et al. 2022, arXiv:2212.05642 [src: abstract] | superseded by D1 |
| 2023 | 67.64 ± 0.52 | Planck PR4 HiLLiPoP | arXiv:2309.10034 [src: Sect. 6] | current PR4 value (one of two likelihoods) |
| 2024 | 66.81 ± 0.81 | SPT-3G polarisation MUSE | arXiv:2411.06000 [src: abstract] | complementary to D1 |
| 2025 | 67.62 ± 0.50 | P-ACT | arXiv:2503.14452 [src: Sect. II] | current |
| 2025 | 66.66 ± 0.60 | SPT-3G D1 | arXiv:2506.20707 [src: abstract] | current |
| 2025 | 67.19 ± 0.38 | CMB-SPA | arXiv:2506.20707 v2 [src: abstract] | current tightest CMB-only |

What superseded what:

- **τ = 0.066 ± 0.016** is the Planck 2015 value, obtained with LFI
  polarisation (arXiv:1502.01589) [src: abstract]. Every Planck-based τ
  from 2018 to 2023 in Section 5 is lower, from 0.051 ± 0.006
  (arXiv:2007.04997) to 0.0627 (+0.0050/−0.0058) (arXiv:2103.14378) [src:
  abstract]. Higher values still found in older texts predate the HFI
  low-ℓ analyses.
- **A_L = 1.180 ± 0.065** is the PR3 Plik number (arXiv:1807.06209,
  Sect. 6.2, Eq. 34b). PR4 reanalyses give 1.039 ± 0.052 (HiLLiPoP,
  arXiv:2309.10034) [src: abstract] and 1.095 ± 0.056 (CamSpec, as quoted
  in arXiv:2503.14452) [sec: Sect. VIII.5]; ACT DR6 gives 1.007 ± 0.057
  (arXiv:2503.14452, Sect. VIII.5).
- **Ω_K = −0.044 from Planck alone** is the PR3 Plik number (as quoted in
  arXiv:2309.10034) [sec: Sect. 11.2]; PR4 HiLLiPoP gives −0.012 ± 0.010
  [src: abstract].
- **"Planck drives CMB parameters"** stopped being true in 2025: SPT+ACT
  matches Planck on H₀ and σ₈ and beats it on N_eff [src] (arXiv:2506.20707).
- **Σm_ν < 0.12 eV** (Planck 2018 + BAO, arXiv:1807.06209) [src: abstract]
  is superseded by DESI-era limits, from < 0.064 eV (arXiv:2503.14738)
  [src: abstract] to < 0.089 eV (arXiv:2503.14454, Sect. VI.1.1, Eq. 33),
  which are model and data-set dependent.
- **SPT-3G lensing**: the 2018 temperature-only measurement (6% amplitude
  error) is superseded by the polarisation MUSE analysis and then by the
  2026 GMV analysis (2%).
- **S₈ from Planck "in tension with lensing surveys"**: PR4 HiLLiPoP gives
  S₈ = 0.819 ± 0.014, against 0.834 ± 0.016 for PR3 (arXiv:2309.10034)
  [src: Sect. 6]; the weak-lensing side is in `cosmo-weak-lensing`.

## Not verified
<!-- key: not-verified -->

- The WMAP9 τ value and the Planck 2013 parameter values were not re-read
  and are not tabulated.
- Rosenberg et al. 2022: A_L and Ω_K now read in its Table 6; its other
  numbers are still quoted through ACT DR6 and Tristram et al. 2023.
- The SH0ES value against which SPT quotes 6.2σ and 6.4σ (arXiv:2506.20707,
  Sect. II) was read only as quoted by ACT DR6 (73.17 ± 0.86 km/s/Mpc,
  arXiv:2503.14452) [sec: Sect. VIII.4]; see `cosmo-distance-ladder-h0`.
- The Planck (SPT rerun) N_eff of 2.87 ± 0.19, tabulated here before
  2026-10-23, is not a Planck (SPT rerun) result: Sect. VII.2.4 of
  arXiv:2506.20707 quotes N_eff = 2.87 ± 0.19 as "the Planck constraint",
  with a citation (its reference 35), and Table 5 gives SPT-3G D1, SPT+ACT,
  CMB-SPA and SPT-3G D1 + DESI only (read 2026-10-24); the row stays
  removed.
