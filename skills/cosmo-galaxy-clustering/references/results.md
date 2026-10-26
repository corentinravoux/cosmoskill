# Galaxy clustering — results

Scope: headline BAO, RSD, full-shape and scale-dependent-bias measurements
from spectroscopic surveys, with the history of the key numbers.
Snapshot: 2026-10-20.

Flags: `[src]` read this session in the cited paper; `[sec]` taken from the
named secondary source; `[der]` derived here. Errors are 1σ unless stated.
"DESI" without qualifier in a DR2-era row means DESI DR2 BAO (galaxies,
quasars and Lyα). The latest DESI BAO release is DR2 (March 2025); the latest
DESI full-shape data are still DR1 (November 2024). No DESI DR2 galaxy
full-shape key paper was found in date-sorted searches up to 2026-10-07.

## 1. BAO distance ladder
<!-- key: bao-distance-ladder -->

### 1.1 DESI DR2 (current)
<!-- key: desi-dr2-current -->

DESI Collaboration 2025, arXiv:2503.14738. Systematic errors included.
Distances (Lyα row included) from its Table 4, N_tracer and V_eff from its
Table 3. All [src: arXiv:2503.14738, Tables 3 and 4].

| Tracer | z range | z_eff | D_V/r_d | D_M/r_d | D_H/r_d | r(M,H) | N_tracer | V_eff [Gpc³] |
|---|---|---|---|---|---|---|---|---|
| BGS | 0.1–0.4 | 0.295 | 7.942 ± 0.075 | — | — | — | 1,188,526 | 3.8 |
| LRG1 | 0.4–0.6 | 0.510 | 12.720 ± 0.099 | 13.588 ± 0.167 | 21.863 ± 0.425 | −0.459 | 1,052,151 | 4.9 |
| LRG2 | 0.6–0.8 | 0.706 | 16.050 ± 0.110 | 17.351 ± 0.177 | 19.455 ± 0.330 | −0.404 | 1,613,562 | 7.6 |
| LRG3+ELG1 | 0.8–1.1 | 0.934 | 19.721 ± 0.091 | 21.576 ± 0.152 | 17.641 ± 0.193 | −0.416 | 4,540,343 | 14.8 |
| ELG2 | 1.1–1.6 | 1.321 | 24.252 ± 0.174 | 27.601 ± 0.318 | 14.176 ± 0.221 | −0.434 | 3,797,271 | 8.3 |
| QSO | 0.8–2.1 | 1.484 | 26.055 ± 0.398 | 30.512 ± 0.760 | 12.817 ± 0.516 | −0.500 | 1,461,588 | 2.7 |
| Lyα | 1.8–4.2 | 2.330 | 31.267 ± 0.256 | 38.988 ± 0.531 | 8.632 ± 0.101 | −0.431 | 1,289,874 | — |

Not used for cosmology because superseded by the combined bin [src]:
LRG3 alone, z_eff = 0.922, D_M/r_d = 21.648 ± 0.178, D_H/r_d = 17.577 ± 0.213;
ELG1 alone, z_eff = 0.955, D_M/r_d = 21.707 ± 0.335, D_H/r_d = 17.803 ± 0.297
(arXiv:2503.14738) [src: Table 4 and its caption].

Notes [src]:

- BGS is an isotropic fit (monopole only). ELG1 and QSO were promoted from
  isotropic fits in DR1 to anisotropic fits in DR2.
- BAO detection significance ranges from 5.6σ (QSO) to 14.7σ (LRG3+ELG1)
  (arXiv:2503.14738) [src: Sect. III.1].
- The Lyα paper quotes D_H/r_d = 8.632 ± 0.098 ± 0.026 and
  D_M/r_d = 38.99 ± 0.52 ± 0.12 (statistical, then theory systematic), a
  0.65% isotropic measurement at z_eff = 2.33 (arXiv:2503.14739, abstract).
- Joint fit of all bins: best-fit χ²/dof = 10.2/(13 − 2) (arXiv:2503.14738)
  [src: Sect. III.3.1].
- Statistical precision improved by between 30% and 50% over DR1
  (arXiv:2503.14738) [src: Sect. III.3.1].

Update at z = 2.33 (July 2026): adding the Lyα full-shape AP measurement to
Lyα BAO gives D_H/r_d = 8.600 ± 0.066 and D_M/r_d = 39.32 ± 0.33 [src: abstract]
(DESI Collaboration 2026, arXiv:2607.27410). AP alone is measured to 1%,
twice as tight as BAO from the same data [src]. Detail: `cosmo-lyman-alpha`.

Unified-tracer reanalysis (August 2026): a single bias-weighted catalogue of
all overlapping DR2 tracers, including QSO to z = 1.6, gives distances "highly
consistent" with the baseline and finds no tracer-dependent systematics in
0.8 < z < 1.6; a finer redshift binning reproduces the w0wa preference
(Sanders et al. 2026, arXiv:2608.27830). The abstract gives no numbers.

### 1.2 DESI DR1 (superseded by DR2)
<!-- key: desi-dr1-superseded-by-dr2 -->

DESI Collaboration 2024, arXiv:2404.03002, Sect. 2.3, sample table. All [src: Sect. 2.3].

| Tracer | z_eff | D_M/r_d | D_H/r_d | r or D_V/r_d | N_tracer | V_eff [Gpc³] |
|---|---|---|---|---|---|---|
| BGS | 0.295 | — | — | D_V/r_d = 7.93 ± 0.15 | 300,017 | 1.7 |
| LRG1 | 0.510 | 13.62 ± 0.25 | 20.98 ± 0.61 | −0.445 | 506,905 | 2.6 |
| LRG2 | 0.706 | 16.85 ± 0.32 | 20.08 ± 0.60 | −0.420 | 771,875 | 4.0 |
| LRG3+ELG1 | 0.930 | 21.71 ± 0.28 | 17.88 ± 0.35 | −0.389 | 1,876,164 | 6.5 |
| ELG2 | 1.317 | 27.79 ± 0.69 | 13.82 ± 0.42 | −0.444 | 1,415,687 | 2.7 |
| QSO | 1.491 | — | — | D_V/r_d = 26.07 ± 0.67 | 856,652 | 1.5 |
| Lyα | 2.330 | 39.71 ± 0.94 | 8.52 ± 0.17 | −0.477 | 709,565 | — |

The aggregate isotropic BAO precision of DR1 is 0.52% for galaxies and
quasars (DESI Collaboration 2024, arXiv:2404.03000) [src: Sect. 9; "∼0.52%" in
the abstract] and 0.49% with Lyα, against 0.60% for the final SDSS
compilation (arXiv:2404.03002) [src: Sect. 2.2, paragraph "The Lyman-α Forest
Sample"]. The most significant single DR1 detection is 9.1σ at z_eff = 0.93,
a 0.86% measurement (arXiv:2404.03000) [src: abstract].

### 1.3 Pre-DESI measurements
<!-- key: pre-desi-measurements -->

| Survey, sample | z_eff | Measurement | Citation | Flag |
|---|---|---|---|---|
| SDSS LRG (first detection) | 0.35 | distance ratio to z = 1089 to 4%; absolute distance to 5% | Eisenstein et al. 2005, arXiv:astro-ph/0501171 | [src: abstract] |
| 6dFGS | 0.106 | D_V = 456 ± 27 Mpc; r_s(z_d)/D_V = 0.336 ± 0.015 | Beutler et al. 2011, arXiv:1106.3366 | [src: abstract] |
| SDSS DR7 MGS | 0.15 | D_V = (664 ± 25)(r_d/r_d,fid) Mpc | Ross et al. 2015, arXiv:1409.3242 | [src: abstract] |
| WiggleZ (reconstructed) | 0.44, 0.60, 0.73 | D_V (r_s^fid/r_s) = 1716 ± 83, 2221 ± 101, 2516 ± 86 Mpc | Kazin et al. 2014, arXiv:1401.0358 | [src: abstract] |
| SDSS LRG, 0.4 < z < 0.6 | 0.51 | D_M/r_d = 13.36 ± 0.21; D_H/r_d = 22.33 ± 0.58 | values as quoted in arXiv:2404.03002 for Alam et al. 2021, arXiv:2007.08991; re-read 2026-10-20 as the BOSS-galaxy BAO-only column | [src: arXiv:2007.08991, Table 3] |
| SDSS LRG, 0.6 < z < 0.85 | 0.70 | D_M/r_d = 17.86 ± 0.33; D_H/r_d = 19.33 ± 0.53 | same; re-read 2026-10-20 as the eBOSS LRG (0.6 < z < 1.0) BAO-only column | [src: arXiv:2007.08991, Table 3] |
| eBOSS LRG (BAO+RSD consensus) | 0.698 | D_M/r_d = 17.65 ± 0.30; D_H/r_d = 19.77 ± 0.47 | Bautista et al. 2020, arXiv:2007.08993 | [src: abstract] |
| eBOSS QSO (consensus) | 1.48 | D_M/r_d = 30.22 ± 0.79; D_H/r_d = 13.26 ± 0.47 | Hou et al. 2020, arXiv:2007.08998 | [src: abstract, consensus values] |
| DESI DR1 + SDSS Lyα | 2.33 | D_M/r_d = 38.80 ± 0.75; D_H/r_d = 8.72 ± 0.14; ρ = −0.48 | arXiv:2404.03002 | [src: Sect. 3.3, Eqs. 13–14] |

The two eBOSS LRG rows differ because one is the BAO-only value used in the
SDSS cosmology compilation and the other the BAO+full-shape consensus of the
LRG paper. State which one is being compared.

BOSS DR12 final: 1.2 million galaxies, three overlapping slices at
z_eff = 0.38, 0.51, 0.61; with Planck 2015, Ω_K = 0.0003 ± 0.0026 and
w = −1.01 ± 0.06; in flat ΛCDM Ω_m = 0.310 ± 0.005 and
H0 = 67.6 ± 0.5 km/s/Mpc [src: abstract] (Alam et al. 2017, arXiv:1607.03155).

## 2. ΛCDM parameters from BAO
<!-- key: lambdacdm-parameters-from-bao -->

Flat ΛCDM. "CMB" is the combination defined in each paper (Planck plus ACT
lensing, with different likelihood versions in DR1 and DR2).

| Dataset | Ω_m | H0 [km/s/Mpc] or h r_d | Citation | Flag |
|---|---|---|---|---|
| DESI DR2 BAO | 0.2975 ± 0.0086 | h r_d = 101.54 ± 0.73 Mpc (r = −0.92) | arXiv:2503.14738 | [src: Sect. VI] |
| DESI DR2 + BBN | 0.2977 ± 0.0086 | 68.51 ± 0.58 | arXiv:2503.14738 | [src: Sect. VI] |
| DESI DR2 + BBN + θ_* | 0.2967 ± 0.0045 | 68.45 ± 0.47 | arXiv:2503.14738 | [src: Sect. VI] |
| DESI DR2 + CMB | 0.3027 ± 0.0036 | 68.17 ± 0.28 | arXiv:2503.14738 | [src: Sect. VI] |
| CMB alone (as used in DR2 paper) | 0.3169 ± 0.0065 | 67.14 ± 0.47 | arXiv:2503.14738 | [src: Sect. VI] |
| DESI DR1 BAO | 0.295 ± 0.015 | — | arXiv:2404.03002 | [src: abstract] |
| DESI DR1 + BBN | 0.295 ± 0.015 | 68.53 ± 0.80 | arXiv:2404.03002 | [src: Table 3, Eq. 18] |
| DESI DR1 + BBN + θ_* | — | 68.52 ± 0.62 | arXiv:2404.03002 | [src: abstract] |
| DESI DR1 + CMB | 0.307 ± 0.005 | 67.97 ± 0.38 | arXiv:2404.03002 | [src: abstract] |
| DESI DR2 Lyα (BAO + AP) + BBN | 0.325 ± 0.018 (AP) | 66.5 ± 1.3 | arXiv:2607.27410 | [src: abstract] |
| Planck 2018 | 0.315 ± 0.007 | 67.4 ± 0.5 | Planck Collaboration 2020, arXiv:1807.06209 | [src: abstract] |

Consistency statements, flat ΛCDM [src]:

- DESI DR2 BAO versus CMB in the (Ω_m, h r_d) plane: 2.3σ, up from 1.9σ in
  DR1; 2.0σ if CMB lensing is excluded (arXiv:2503.14738, Sect. VI).
- With the 2026 Lyα AP measurement the DESI–CMB discrepancy goes from 2.4σ to
  2.2σ (arXiv:2607.27410; that paper's own before-and-after numbers). [src: abstract]
- DESI DR2 + BBN versus SH0ES H0: 4.5σ, independent of the CMB
  (arXiv:2503.14738, Sect. VI).
- Ω_m from DESI DR2 versus supernovae: 1.7σ (Pantheon+), 2.1σ (Union3), 2.9σ
  (DESY5), supernovae preferring higher Ω_m (arXiv:2503.14738, Sect. VI).

## 3. Full-shape constraints, flat ΛCDM
<!-- key: full-shape-constraints-flat-lambdacdm -->

Most use a BBN prior on ω_b (D'Amico et al. 2020 instead fix Ω_b/Ω_c); the
n_s treatment differs and is stated.

| Data and analysis | Ω_m | H0 | σ8 | n_s | Citation | Flag |
|---|---|---|---|---|---|---|
| BOSS DR12, EFT (CLASS-PT lineage) | 0.295 ± 0.010 | 67.9 ± 1.1 | 0.721 ± 0.043 | fixed | Ivanov et al. 2020, arXiv:1909.05277 | [src: abstract] |
| BOSS DR12, EFT (PyBird lineage) | 0.309 ± 0.010 | 68.5 ± 2.2 | ln(10¹⁰A_s) = 2.72 ± 0.13 | fixed | D'Amico et al. 2020, arXiv:1909.05271 | [src: abstract] |
| BOSS DR12, P + bispectrum monopole | — | 69.6 (+1.1/−1.3) | 0.692 (+0.035/−0.041) | free: 0.870 (+0.067/−0.064) | Philcox & Ivanov 2022, arXiv:2112.04515 | [src: abstract] |
| same, n_s from Planck | — | 68.31 (+0.83/−0.86) | 0.722 (+0.032/−0.036) | Planck | arXiv:2112.04515 | [src: abstract] |
| BOSS, LPT, pre-recon P + post-recon ξ | 0.303 ± 0.0082 | 69.23 ± 0.77 | 0.733 ± 0.047 | — | Chen et al. 2022, arXiv:2110.05530 | [src: abstract] |
| DESI DR1 FS + DR1 BAO (key paper) | 0.296 ± 0.010 | 68.63 ± 0.79 | 0.841 ± 0.034 | Gaussian prior | Adame et al. 2024, arXiv:2411.12021 | [src: abstract] |
| same, cosmology paper | 0.2962 ± 0.0095 | — | 0.842 ± 0.034 | weak prior | DESI Collaboration 2024, arXiv:2411.12022 | [src: abstract] |
| DESI DR1 (FS+BAO) + CMB | 0.3056 ± 0.0049 | — | 0.8121 ± 0.0053 | — | arXiv:2411.12022 | [src: abstract] |
| DESI DR1 (FS+BAO) + CMB + DESY3 3×2pt | — | 68.40 ± 0.27 | — | — | arXiv:2411.12022 | [src: abstract] |
| DESI DR1 FS + BAO, HOD-informed priors | 0.2994 ± 0.0090 | — | 0.836 (+0.024/−0.027) | weak prior | Zhang et al. 2025, arXiv:2504.10407 | [src: abstract] |
| DESI DR1 FS + BAO, profile likelihood | 0.3034 ± 0.0110 | 68.96 (+0.81/−0.80) | 0.863 (+0.048/−0.040) | — | Morawetz et al. 2025, arXiv:2508.11811 | [src: abstract] |
| DESI DR1 P + B, independent pipeline | 0.284 ± 0.011 | 70.7 ± 1.1 | 0.811 ± 0.030 | external prior | Chudaykin et al. 2025, arXiv:2507.13433 | [src: abstract] |
| same + DESI DR2 BAO | 0.296 ± 0.007 | 68.8 ± 0.6 | 0.818 ± 0.029 | external prior | arXiv:2507.13433 | [src: abstract] |
| DESI DR1 FS (ShapeFit) + DR2 BAO ("DESI1.5") | 0.3035 ± 0.0085 | h = 0.6876 ± 0.0059 | 0.822 ± 0.034 | wide prior | Forero-Sánchez et al. 2026, arXiv:2602.18761 | [src: abstract] |
| DESI DR1 P with simulation-based priors + DR2 BAO | 0.2987 ± 0.0066 | 68.80 ± 0.35 | 0.766 ± 0.015 | — | Chudaykin et al. 2026, arXiv:2602.18554 | [src: abstract] |
| DESI DR1 P + B + photometric and CMB-lensing cross-correlations + DR2 BAO | 0.2974 ± 0.0050 | 69.08 ± 0.37 | 0.838 ± 0.017 | CMB prior | Ivanov et al. 2026, arXiv:2601.16165 | [src: abstract] |
| Planck 2018 (for reference) | 0.315 ± 0.007 | 67.4 ± 0.5 | 0.811 ± 0.006 | 0.965 ± 0.004 | arXiv:1807.06209 | [src: abstract] |

Reading the table:

- The BOSS full-shape analyses in the table gave σ8 = 0.721 ± 0.043
  (arXiv:1909.05277), 0.692 (+0.035/−0.041) and, with n_s from Planck,
  0.722 (+0.032/−0.036) (arXiv:2112.04515), and 0.733 ± 0.047
  (arXiv:2110.05530), all [src: abstract], against 0.811 ± 0.006 for Planck
  2018 (arXiv:1807.06209) [src: abstract]. DESI DR1 with the collaboration
  pipeline gives 0.841 ± 0.034, which the paper calls consistent with Planck
  (arXiv:2411.12021) [src: abstract].
  The "low σ8 from full shape" narrative rests on BOSS and on prior choices
  (see `open-questions.md`).
- The simulation-based-prior result, σ8 = 0.766 ± 0.015, is low again; its
  authors attribute the downward shift to the quasar HOD assumptions
  (arXiv:2602.18554) [src: abstract].
- Adding the LRG bispectrum to the DESI ShapeFit analysis ("DESI1.5", P+B)
  gives σ8 = 0.868 ± 0.026 and S8 = 0.880 ± 0.028, against σ8 = 0.822 ± 0.034
  and S8 = 0.827 ± 0.036 from the power spectrum alone, with uncertainties
  reduced by 24% and 22% (Forero-Sánchez et al. 2026, arXiv:2606.23936)
  [src: abstract, current arXiv version]. A separate joint P + B
  analysis in the tripolar-spherical-harmonic basis finds 6% and 4% tighter
  ω_cdm and amplitude when all tracers are combined (Guandalin et al.
  2026, arXiv:2610.01836) [src: abstract].
- Bayesian and frequentist DESI results agree in ΛCDM (shifts of 0.8σ, 0.3σ,
  0.7σ in σ8, H0, Ω_m between maximum likelihood and posterior mean) but not
  in w0waCDM, where the shifts are 2.1σ, 4.1σ, 6.5σ, 6.3σ and 6.6σ in σ8,
  H0, Ω_m, w0 and wa [src: abstract; Sect. 4.2 for the parameter order]
  (arXiv:2508.11811).

## 4. Growth rate
<!-- key: growth-rate -->

### 4.1 DESI DR1 ShapeFit (model-agnostic compression)
<!-- key: desi-dr1-shapefit-model-agnostic-compression -->

Adame et al. 2024, arXiv:2411.12021. The quantity is fσ_s8, not fσ8 (see
`physics-and-methods.md`). Ratios to the fiducial are the MAP values of its
Table 9. The absolute fσ_s8 (ShapeFit+BAO) and its diagonal covariance element
C_33 are as printed in its Appendix A, which gives the data vector and the
Gaussian covariance of each bin (in units of 10⁻⁴ for C); the paper prints no
error on the absolute value, and none is computed here. All [src: arXiv:2411.12021, Table 9 and App. A].

| Bin | z_eff | fσ_s8/fid (ShapeFit) | fσ_s8/fid (ShapeFit+BAO) | fσ_s8 (ShapeFit+BAO) | C_33 [10⁻⁴] | Place in App. A |
|---|---|---|---|---|---|---|
| BGS | 0.30 | 0.80 ± 0.20 | 0.84 ± 0.19 | 0.396326 | 80.924891 | Eqs. 31–32 |
| LRG1 | 0.51 | 1.09 (+0.12/−0.14) | 1.16 ± 0.13 | 0.547632 | 35.284297 | Eqs. 33–34 |
| LRG2 | 0.71 | 1.05 ± 0.12 | 1.04 (+0.11/−0.092) | 0.479541 | 23.061044 | Eqs. 35–36 |
| LRG3 | 0.92 | 0.96 (+0.11/−0.10) | 0.997 (+0.10/−0.084) | 0.438454 | 17.011310 | Eqs. 37–38 |
| ELG2 | 1.32 | 0.95 (+0.11/−0.08) | 0.945 (+0.097/−0.077) | 0.372661 | 11.811326 | Eqs. 39–40 |
| QSO | 1.49 | 1.16 ± 0.12 | 1.16 ± 0.12 | 0.436849 | 21.028703 | Eqs. 41–42 |

Combined precision on the RSD amplitude: 4.7% (arXiv:2411.12021)
[src: abstract], which the paper describes as similar to that of twenty years
of earlier surveys; BOSS DR12 fσ8 reached 6 per cent precision
(arXiv:1607.03155) [src: abstract].
There is no DESI DR2 fσ8 measurement from galaxy clustering as of the
snapshot.

### 4.2 Earlier measurements
<!-- key: earlier-measurements -->

| Survey, sample | z_eff | fσ8 | Citation | Flag |
|---|---|---|---|---|
| eBOSS LRG (consensus) | 0.698 | 0.473 ± 0.044 | arXiv:2007.08993 | [src: abstract] |
| eBOSS QSO (consensus) | 1.48 | 0.464 ± 0.045 | arXiv:2007.08998 | [src: abstract] |
| BOSS DR12 (three bins) | 0.38, 0.51, 0.61 | 6% precision; values not in the abstract | arXiv:1607.03155 | [src] |
| BOSS DR12 consensus BAO+FS | 0.38, 0.51, 0.61 | 0.497 ± 0.039 ± 0.024; 0.458 ± 0.035 ± 0.015; 0.436 ± 0.034 ± 0.009 (stat, sys) | arXiv:1607.03155 | [src: Table 7] |
| eBOSS ELG (consensus) | 0.85 | 0.315 ± 0.095 | arXiv:2007.09008; arXiv:2007.09009 | [src: abstract of each] |
| SDSS MGS | 0.15 | 0.53 ± 0.16 | arXiv:2007.08991 | [src: Table 3] |

The SDSS cosmology paper combines six fσ8 measurements [src]
(arXiv:2007.08991). Per-method BOSS values, the pre-BOSS measurements (VVDS,
6dFGS, GAMA, VIPERS, FastSound, BOSS DR9) and the full SDSS compilation table
are in `rsd-modelling.md`, Sects. 3 and 5, and `boss-eboss-euclid.md`,
Sects. 2–3. Low-redshift fσ8 from peculiar velocities belongs to
`cosmo-peculiar-velocities`.

## 5. Extended models (summary; interpretation in sibling skills)
<!-- key: extended-models-summary-interpretation-in -->

### 5.1 w0waCDM preference over ΛCDM
<!-- key: w0wacdm-preference-over-lambdacdm -->

DR1 column from arXiv:2404.03002 (abstract; DESI + CMB from its Sect. 5.2),
DR2 column from arXiv:2503.14738 (Table 6), last column from arXiv:2607.27410
(abstract; Table 4 for the supernova row).
From arXiv:2404.03002, arXiv:2503.14738, arXiv:2607.27410 [src: abstract, Sect. 5.2, Table 6, Table 4]:

| Combination | DR1 BAO | DR2 BAO | DR2 BAO + Lyα AP | Flag |
|---|---|---|---|---|
| DESI alone | — | 1.7σ | — | [src] |
| DESI + CMB | 2.6σ | 3.1σ | 2.7σ | [src] |
| DESI + CMB + Pantheon+ (as published) | 2.5σ | 2.8σ | — | [src] |
| DESI + CMB + Union3 (as published) | 3.5σ | 3.8σ | — | [src] |
| DESI + CMB + DESY5 (as published) | 3.9σ | 4.2σ | — | [src] |
| DESI + CMB + DES-Dovekie SNe (2026 paper) | — | — | 3.2σ | [src] |

Δχ²_MAP for the four DR2 rows with CMB: −12.5, −10.7, −17.4, −21.0
(arXiv:2503.14738) [src: Table 6].

**The supernova rows are the values as published in March 2025 and are
superseded on the supernova side.** Re-running the DESI DR2 + Planck +
supernova combination "exactly as done by DESI DR2" with the recalibrated
samples, Hoyt et al. 2026 (arXiv:2601.19424, abstract) find 3.2σ with the
corrected Pantheon+ (was 2.8σ), 3.4σ with Union3.1 (was 3.8σ with Union3;
w0 = −0.719 ± 0.084, wa = −0.95 (+0.29/−0.26)) and 3.4σ with the DES-Dovekie
recalibration of DES-SN5YR (was 4.2σ) [src]. The DR2 paper's range of
2.8–4.2σ across supernova samples (arXiv:2503.14738, abstract) is therefore
replaced by these three values. What changed in each sample
(host-galaxy masses, the Dovekie calibration) is in the `cosmo-supernovae`
skill; quote the 2025 numbers only as "as published".

DR2 posteriors as published (arXiv:2503.14738) [src: Table 5]: DESI + CMB,
w0 = −0.42 ± 0.21, wa = −1.75 ± 0.58; with Pantheon+, w0 = −0.838 ± 0.055,
wa = −0.62 (+0.22/−0.19); with Union3, w0 = −0.667 ± 0.088,
wa = −1.09 (+0.31/−0.27); with DESY5, w0 = −0.752 ± 0.057,
wa = −0.86 (+0.23/−0.20).

Full-shape side:

- DESI DR1 FS (ShapeFit) + DR2 BAO + BBN, DESI data only:
  w0 = −0.49 ± 0.25, wa = −1.52 ± 0.77, a 1.4σ departure from ΛCDM [src]
  (arXiv:2602.18761, w0waCDM table and abstract). **The arXiv abstract prints
  "w0 = 0.49" without the minus sign; the table in the body gives −0.49.**
- With the LRG bispectrum, DESI-only results are consistent with Λ within 1σ;
  DESI + CMB gives 2.8σ; DESI + CMB + DES-Dovekie supernovae 3.1σ [src: abstract]
  (arXiv:2606.23936).
- With simulation-based priors, w0wa is consistent with Λ within 2.2σ without
  supernovae and 1.4σ with them [src: abstract] (arXiv:2602.18554).
- Independent combined-probe analysis: 2.2σ from low-redshift data with
  Pantheon+, 2.7σ with Planck instead of supernovae [src: abstract] (arXiv:2601.16165).

The dark-energy interpretation is in `cosmo-dark-energy-modified-gravity`.

### 5.2 Other one-parameter extensions
<!-- key: other-one-parameter-extensions -->

| Quantity | Value | Dataset, model | Citation | Flag |
|---|---|---|---|---|
| Σm_ν | < 0.072 eV (95%) | DESI DR1 BAO + CMB, ΛCDM, Σm_ν > 0 prior | arXiv:2404.03002 | [src: abstract] |
| Σm_ν | < 0.071 eV (95%) | DESI DR1 (FS+BAO) + CMB, ΛCDM | arXiv:2411.12022 | [src: abstract] |
| Σm_ν | < 0.064 eV (95%) | DESI DR2 BAO + CMB, ΛCDM | arXiv:2503.14738 | [src: abstract] |
| Σm_ν | < 0.16 eV (95%) | DESI DR2 BAO + CMB, w0waCDM | arXiv:2503.14738 | [src: abstract] |
| 10³ Ω_K | 2.3 ± 1.1 | DESI DR2 BAO + CMB, ΛCDM + Ω_K | arXiv:2503.14738 | [src: Sect. VI] |
| 10³ Ω_K | 25 ± 41 | DESI DR2 BAO alone | arXiv:2503.14738 | [src: Table 5] |
| w | −0.916 ± 0.078 | DESI DR2 BAO alone, wCDM | arXiv:2503.14738 | [src: Sect. VI] |
| w | −1.055 ± 0.036 | DESI DR2 BAO + CMB, wCDM | arXiv:2503.14738 | [src: Sect. VI] |
| w | −0.99 (+0.15/−0.13) | DESI DR1 BAO alone, wCDM | arXiv:2404.03002 | [src: abstract] |
| μ_0 | 0.11 (+0.45/−0.54) | DESI DR1 (FS+BAO) alone | arXiv:2411.12022 | [src: abstract] |
| μ_0, Σ_0 | 0.04 ± 0.22, 0.044 ± 0.047 | DESI DR1 + CMB + DESY3 | arXiv:2411.12022 | [src: abstract] |

Neutrino-mass interpretation: `cosmo-neutrinos-dark-matter`. Modified
gravity: `cosmo-dark-energy-modified-gravity`.

### 5.3 H0 without the sound horizon
<!-- key: h0-without-the-sound-horizon -->

Rescaling the power spectrum to remove r_s information and relying on the
equality scale, with uncalibrated DR1 BAO and θ_*, DESI DR1 gives
H0 = 69.2 (+1.3/−1.4), 70.3 (+1.4/−1.2) and 69.6 (+1.3/−1.8) km/s/Mpc for
three choices of the external Ω_m information [src: abstract] (Zaborowski et al. 2025,
arXiv:2510.19149).

## 6. Local primordial non-Gaussianity from scale-dependent bias (status)
<!-- key: local-primordial-non-gaussianity-from-scale -->

| Data | f_NL^loc (1σ) | Assumption on b_φ | Citation | Flag |
|---|---|---|---|---|
| eBOSS DR16 QSO, P_0 | −12 ± 21 | — | Mueller et al. 2022, arXiv:2106.13725 | [src: abstract] |
| eBOSS DR16 QSO, optimal weights | −4 < f_NL < 27 | standard response | Cagliari et al. 2024, arXiv:2309.15814 | [src: abstract] |
| same | −23 < f_NL < 21 | lower response | arXiv:2309.15814 | [src: abstract] |
| DESI DR1 LRG + QSO, P(k) | −3.6 (+9.0/−9.1) | p = 1 for LRG, recent-merger model for QSO | Chaussidon et al. 2024, arXiv:2411.17623 | [src: abstract] |
| same | 3.5 (+10.7/−7.4) | universality for QSO too | arXiv:2411.17623 | [src: abstract] |
| DESI DR1, simulation prior on p (mean ≈ 1.4) | −3.3 ± 9.2 | IllustrisTNG-based prior | Fondi et al. 2026, arXiv:2602.12357 | [src: abstract] |
| DESI DR1 LRG×QSO cross-correlations added | 2.1 (+8.8/−8.3) | — | Rosado-Marín et al. 2026, arXiv:2604.05213 | [src: abstract] |
| DESI DR1 LRG + QSO, configuration space | −3 ± 12 | p_LRG = 1.0 ± 0.1, p_QSO = 1.6 ± 0.1 | Brown et al. 2026, arXiv:2606.24651 | [src: abstract] |
| DESI DR1 P + B (EFT, one loop) | −0.1 ± 7.4 | — | Chudaykin et al. 2025, arXiv:2512.04266 | [src: abstract] |
| same + CMB | −0.0 ± 4.1 | — | arXiv:2512.04266 | [src: abstract] |
| Planck 2018 bispectrum | −0.9 ± 5.1 | none needed | Planck Collaboration 2020, arXiv:1905.05697 | [src: abstract] |

DESI DR1 improves on eBOSS by a factor 2.3 (arXiv:2411.17623)
[src: abstract]. The same analysis used 1,631,716 LRGs (0.6 < z < 1.1) and
1,189,129 QSOs (0.8 < z < 3.1) [src: abstract]. Non-local shapes from DESI
DR1 P + B: f_NL^equil = 719 ± 390, f_NL^orth = −200 ± 100 (arXiv:2512.04266)
[src: abstract].

## 7. History of the key numbers
<!-- key: history-of-the-key-numbers -->

**BAO precision.**

| Year | Result | Citation | Flag |
|---|---|---|---|
| 2005 | First detections: SDSS LRG ξ(r) (46,748 galaxies) and 2dFGRS P(k) (221,414 galaxies) | arXiv:astro-ph/0501171; arXiv:astro-ph/0501174 | [src: abstract of each] |
| 2012 | First reconstruction on data: 1.9% distance to z = 0.35 | arXiv:1202.0090 | [src: abstract] |
| 2017 | BOSS DR12 consensus, 1.2 million galaxies | arXiv:1607.03155 | [src: abstract] |
| 2021 | SDSS final: eight BAO samples, aggregate 0.60% | arXiv:2007.08991 (eight samples: abstract); precision as quoted in arXiv:2404.03002 | [src: abstract], precision [sec: arXiv:2404.03002, Sect. 2.2, Lyα forest sample paragraph] |
| 2024 | DESI DR1: 0.52% (galaxies and QSO), 0.49% with Lyα | arXiv:2404.03000 (Sect. 9); arXiv:2404.03002 (Sect. 2.2, Lyα forest sample paragraph) | [src] |
| 2025 | DESI DR2: more than 14 million galaxies and quasars; per-bin α_iso and α_AP constraints in its Table 4 | arXiv:2503.14738 | [src: abstract] |

**The LRG bins, DR1 to DR2.**

- LRG2 (z = 0.71) D_M/r_d: 16.85 ± 0.32 in DR1 (arXiv:2404.03002)
  [src: Table 1], 17.351 ± 0.177 in DR2 (arXiv:2503.14738) [src: Table 4],
  against 17.86 ± 0.33 for SDSS at z = 0.70 (arXiv:2007.08991)
  [src: Table 3]. The DESI–SDSS difference went from 3σ in DR1 to about 2.6σ
  in DR2 for an assumed correlation C ≈ 0.57; 2.3σ against DESI's own
  reanalysis of SDSS with C = 0.57; DESI concludes "no significant
  discrepancy" (arXiv:2503.14738) [src: Sect. III.3.2].
- LRG1 (z = 0.51) D_H/r_d: 20.98 ± 0.61 in DR1 (arXiv:2404.03002)
  [src: Table 1], 21.863 ± 0.425 in DR2 (arXiv:2503.14738) [src: Table 4].
- DR1 versus DR2 overall: largest shifts 1.56σ in α_iso (LRG3+ELG1) and 1.93σ
  in α_AP (LRG2), with DR1 treated as a subset; KS p-value 0.40 [src: Sect. III.3.1]
  (arXiv:2503.14738).

**H0 from BAO + BBN.** 68.53 ± 0.80 (DR1; arXiv:2404.03002) [src: Eq. 18]
to 68.51 ± 0.58 (DR2; arXiv:2503.14738) [src: Table 5]. The eBOSS-era inverse
distance ladder gave H0 = 68.18 ± 0.79 km/s/Mpc in the evolving-dark-energy
model of the abstract (arXiv:2007.08991) [src: abstract].

**σ8 from full shape.** BOSS: 0.721 ± 0.043 (arXiv:1909.05277),
0.692 (+0.035/−0.041) (arXiv:2112.04515), 0.733 ± 0.047 (arXiv:2110.05530);
DESI DR1: 0.841 ± 0.034 (arXiv:2411.12021); all [src: abstract]; see Sect. 3.

**f_NL from LSS.** −12 ± 21 from eBOSS DR16 (arXiv:2106.13725) to
−3.6 (+9.0/−9.1) from DESI DR1 (arXiv:2411.17623), against −0.9 ± 5.1 from
Planck (arXiv:1905.05697), all [src: abstract]; see Sect. 6.

## Not verified
<!-- key: not-verified -->

- The aggregate isotropic BAO precision of DESI DR2 (not in the abstract or
  the sections read).
- BOSS DR12 consensus D_M, H and fσ8 values per bin (not in the abstract).
- Bispectrum shift (arXiv:2606.23936): the cached HTML of an earlier version
  gives a 1.1σ shift in σ8, 1.2σ in S8 and error reductions of 26% and 28%
  (abstract and Sect. 5 of that version); the current arXiv abstract gives
  24% and 22%. The file now quotes the current abstract.
- Inverse distance ladder (arXiv:2007.08991): this file said 68.20 ± 0.81 in
  ow0waCDM, the value of the arXiv listing abstract (read 2026-10-24). The
  HTML rendering of the current version gives 68.18 ± 0.79 in its abstract,
  in the Sect. VI table and in Sect. VI.2.1, now quoted; the two versions
  differ. Its Table 5 (Sect. IV.2) gives 67.91 ± 0.87 for
  CMB T&P + BAO + SN in ow0waCDM.
- WiggleZ and BOSS fσ8 values; the eBOSS ELG results (arXiv not re-read for
  this file).
- Whether a DESI DR2 galaxy full-shape key paper exists under a title that
  the searches missed; the 2026 "DESI DR2 Results IV" is the Lyα AP paper and
  no "Results III" was found.
