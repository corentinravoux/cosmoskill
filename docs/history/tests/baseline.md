# RED baseline — answers from memory

2026-10-07. A fresh agent answered `questions.md` with no tools, no skill and
no web access (model knowledge cutoff: June 2026). The sheet is reproduced as
returned. Grading is in `baseline-grading.md`.

---

All answers from memory, no lookup (knowledge cutoff June 2026); arXiv IDs are best recollection.

1. DESI DR2 BAO (arXiv:2503.14738, March 2025), w0waCDM vs ΛCDM. DESI+CMB: 3.1σ. DESI+CMB+Pantheon+: 2.8σ. DESI+CMB+Union3: 3.8σ. DESI+CMB+DESY5: 4.2σ. DESI BAO alone: weak, below 2σ (low confidence). For DESI+CMB+DESY5: w0 = −0.752 ± 0.057, wa = −0.86 (+0.23/−0.20). For DESI+CMB+Pantheon+: w0 = −0.838 ± 0.055, wa = −0.62 (+0.22/−0.19). With the recalibrated DES-SN5YR (Dovekie), the DESY5 combination falls to about 3.2σ. Confidence: high on significances, medium on the last digits of w0/wa.

2. DESI DR2 Lyα BAO (arXiv:2503.14739), auto- plus QSO cross-correlation, z_eff = 2.33. D_H/r_d = 8.632 ± 0.098 (stat) ± 0.026 (sys). D_M/r_d = 38.99 ± 0.52 (stat) ± 0.12 (sys). Precision: about 1.1% on D_H, 1.3% on D_M, 0.65% on the isotropic scale. Model: fiducial-ΛCDM template with BAO dilation parameters; first Lyα analysis with a quoted theoretical-systematic term. Confidence: high on z_eff and precision, medium-high on central values.

3. Two releases have a published P1D, each with both estimators.
- EDR + two months of main survey (2023): FFT, Ravoux et al., arXiv:2306.06311; QMLE, Karaçaylı et al., arXiv:2306.06316. 2.0 ≤ z ≤ 3.8; k up to about half Nyquist (~2 Å⁻¹) for FFT, lower for QMLE.
- DR1 (2025): FFT, Ravoux et al., arXiv:2505.09493; QMLE, Karaçaylı et al., arXiv:2505.07974. 2.2 ≤ z ≤ 4.2; k roughly 10⁻³ to a few 10⁻² s/km.
- No DR2 P1D that I know of as of June 2026.
Confidence: high on releases/estimators and EDR IDs; medium on DR1 IDs and z range; low on k ranges.

4. ACT DR6 power spectra and ΛCDM parameters, Louis et al., arXiv:2503.14452 (March 2025), flat ΛCDM.
- ACT alone: H0 = 66.11 ± 0.79 km/s/Mpc, ns = 0.9666 ± 0.0077.
- P-ACT (ACT + Planck): H0 = 67.62 ± 0.50, ns = 0.9709 ± 0.0038.
- P-ACT-LB (+ CMB lensing + DESI BAO): H0 = 68.22 ± 0.36, ns = 0.9743 ± 0.0034.
- W-ACT (ACT + WMAP): H0 ≈ 66.8 ± 0.7, ns ≈ 0.966 ± 0.005 (low confidence).
Extended-models companion: Calabrese et al., arXiv:2503.14454. Confidence: medium-high on ACT, P-ACT and P-ACT-LB; low on W-ACT.

5. SPT-3G D1 (Camphuis et al., arXiv:2506.20707, June 2025; 2019–2020 main field, TT/TE/EE), flat ΛCDM.
- SPT alone: H0 = 66.66 ± 0.60 km/s/Mpc, 6.2σ from SH0ES.
- SPT+ACT+Planck ("SPA"): H0 = 67.24 ± 0.35, 6.4σ from SH0ES.
The paper also reports a 2.8σ CMB vs DESI DR2 BAO discrepancy in ΛCDM. Confidence: high on H0 values, medium-high on tension figures.

6. DES Y6 3×2pt (arXiv:2601.14559, January 2026), flat ΛCDM: S8 = 0.789 ± 0.012, Ωm = 0.333 (+0.023/−0.028). Agreement with primary CMB (Planck+ACT+SPT): about 1.8σ in the full parameter space, about 2.6σ projected onto S8; I may have these two attributions swapped. Adding the other DES probes (BAO, SN, clusters) gives S8 ≈ 0.794 ± 0.009, about 2.3σ from the CMB. Confidence: medium-high on S8, low on the exact σ attribution.

7. KiDS-Legacy cosmic shear (Wright et al., arXiv:2503.19441, March 2025; 1347 deg², six tomographic bins to z_phot ≈ 2), flat ΛCDM: S8 = 0.815 (+0.016/−0.021). Consistent with Planck at 0.73σ, so no S8 tension; the shift from KiDS-1000 is attributed mainly to improved redshift calibration. Consistency companion: Stölzner et al., arXiv:2503.19442. Confidence: high on S8 and 0.73σ, medium on the companion ID.

8. DES-SN5YR (arXiv:2401.02929): 1829 SNe Ia, i.e. 1635 photometrically classified DES SNe plus 194 low-z. SN-only flat wCDM: w = −0.80 (+0.14/−0.16); flat ΛCDM Ωm = 0.352 ± 0.017. Recalibration ("Dovekie", Popovic et al., arXiv:2511.07517, late 2025): redone photometric cross-calibration, retrained SALT light-curve model, updated host-mass/bias-correction treatment, sample about 1820 SNe. Ωm drops to about 0.330 ± 0.015, and the DESI+CMB+SN w0wa preference falls from 4.2σ to about 3.2σ. Confidence: high on original numbers; medium on Dovekie values; low on its ID and sample size.

9. Flat ΛCDM, SN only.
- Pantheon+ (Brout et al., arXiv:2202.04077): 1701 light curves of 1550 distinct SNe Ia, 0.001 < z < 2.26; Ωm = 0.334 ± 0.018.
- Union3 (Rubin et al., arXiv:2311.12098): 2087 SNe Ia from 24 datasets, UNITY1.5 Bayesian framework, 22 binned distance nodes; Ωm = 0.356 (+0.028/−0.026).
Confidence: high.

10. SH0ES, latest I know: Breuval et al. 2024 (arXiv:2404.08038), H0 = 73.17 ± 0.86, Cepheids + SNe Ia with four anchors (NGC 4258 maser, Milky Way Gaia parallaxes, LMC and SMC eclipsing binaries); baseline Riess et al. 2022 (arXiv:2112.04510), 73.04 ± 1.04. JWST cross-check (arXiv:2408.11770): 72.6 ± 2.0. The broader Local Distance Network (2025) gives about 73.50 ± 0.81 (low confidence).
CCHP: Freedman et al. (arXiv:2408.06153; ApJ 2025), 70.39 ± 1.22 (stat) ± 1.33 (sys) ± 0.70 (σ_SN) from TRGB with HST+JWST; preprint combination of TRGB, JAGB and Cepheids 69.96 ± 1.05 ± 1.12.
Confidence: medium.

11. Public to my knowledge:
- Early Release Observations (ERO): 23 May 2024.
- Quick Release Q1: 19 March 2025, about 63 deg² (three Deep Fields at single-visit wide depth); overview arXiv:2503.15302.
- DR1 (first year, about 1900 deg²): scheduled for 21 October 2026, so not yet public on 7 October 2026 if that date held.
I cannot confirm from memory any slip or change after June 2026. Confidence: high on ERO and Q1; medium on the DR1 date; low on the Q1 ID.

12. (a) Cosmic shear:
- PSF modelling/leakage: Jarvis+ 2011.03408.
- Shear calibration: Sheldon & Huff 1702.02601.
- Blending: MacCrann+ 2012.08567.
- Redshift calibration: Myles+ 2012.08566.
- Intrinsic alignments: Blazek+ 1708.09247.
- Baryonic feedback: van Daalen+ 1104.1174.
- Nonlinear P(k): Mead+ 2009.01858.
- B-modes: Asgari+ 2007.15633.

(b) Lyα 3D BAO:
- Continuum distortion: Bautista+ 1702.00176.
- Metals: du Mas des Bourboux+ 2007.08995.
- HCDs/DLAs: Font-Ribera & Miralda-Escudé 1205.2018.
- BALs: Ennesser+ 2111.09439.
- Quasar redshift errors: Youles+ 2205.06648.
- Correlated sky/instrument noise: Guy+ 2404.03003.
- UV fluctuations: Gontcho A Gontcho+ 1404.7425.
- Nonlinear peak broadening: Kirkby+ 1301.3456.
- Mock validation: Cuceu+ 2404.03004.

Confidence: high on the lists, medium on IDs.
