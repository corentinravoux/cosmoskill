# GREEN test — wave 1 skills — 2026-10-08

Rules: every answer below comes only from the files of the six skill directories (`cosmo-cmb`, `cosmo-galaxy-clustering`, `cosmo-lyman-alpha`, `cosmo-weak-lensing`, `cosmo-supernovae`, `cosmo-distance-ladder-h0`) under `<skills>/`, with no web, no arXiv tool, no other file and no recall from memory; each skill was entered through its `SKILL.md` and its file map; gaps are marked "NOT IN SKILL:" and cross-skill disagreements "CONFLICT:".

Paths are relative to `<skills>/`. Confidence is the confidence that the skill text supports the answer, not an independent check of the paper. All values carry the skills' own `[src]` flag unless stated.

Summary: 8 questions fully answered (1, 2, 5, 6, 7, 8, 9, 12); 4 answered with a gap (3, 4, 10, 11); no CONFLICT between skills; 0 wrong-file navigation failures, 4 cases where a second file or a second skill was needed.

---

## 1. DESI DR2 BAO: w0wa preference by combination and SN sample

Answer (flat w0waCDM against ΛCDM, DESI Collaboration 2025, arXiv:2503.14738, March 2025):

| Combination | Preference | Δχ² | w0 | wa |
|---|---|---|---|---|
| DESI DR2 BAO alone | 1.7σ | — | — | — |
| DESI + CMB | 3.1σ | −12.5 | −0.42 ± 0.21 | −1.75 ± 0.58 |
| DESI + CMB + Pantheon+ | 2.8σ | −10.7 | −0.838 ± 0.055 | −0.62 (+0.22/−0.19) |
| DESI + CMB + Union3 | 3.8σ | −17.4 | −0.667 ± 0.088 | −1.09 (+0.31/−0.27) |
| DESI + CMB + DESY5 | 4.2σ | −21.0 | −0.752 ± 0.057 | −0.86 (+0.23/−0.20) |

Status that the supernova skill adds: these SN-dependent figures are superseded. After the DES-Dovekie recalibration and the host-mass correction they become 3.2σ (corrected Pantheon+), 3.4σ (Union3.1), 3.4σ (DES-Dovekie, Hoyt et al. re-run with DESI DR2 + Planck), arXiv:2601.19424; the DES analysis itself quotes 3.2σ with CMB = Planck + ACT + SPT (arXiv:2511.07517); Unite gives 3.3σ (arXiv:2609.05053). With the 2026 Lyα AP measurement added: 2.7σ (DESI + CMB), 3.2σ (with SNe), arXiv:2607.27410.

Confidence: high.

Found in: `cosmo-galaxy-clustering/references/results.md` lines 213–230 (table, Δχ², posteriors); `cosmo-galaxy-clustering/SKILL.md` lines 31–32; update in `cosmo-supernovae/references/results.md` lines 66–75 and 107–120, `cosmo-supernovae/SKILL.md` lines 33–38.

Navigation: `cosmo-galaxy-clustering/SKILL.md` sent to `results.md` at the first try. The revised significances are only in `cosmo-supernovae`; the galaxy-clustering skill lists that skill under "Related skills" but nowhere says that the 2.8–4.2σ figures were revised, so a reader of that skill alone reports superseded numbers.

NOT IN SKILL: any DESI + supernovae combination without the CMB (no such row in either skill); the question does not strictly require it.

## 2. DESI DR2 Lyα forest BAO

Answer (DESI DR2 Lyα auto + Lyα×QSO, BAO only, arXiv:2503.14739; geometric measurement, no dark-energy model assumed, distances in units of r_d):

- Effective redshift: z_eff = 2.33.
- Precision: 1.1% along the line of sight, 1.3% transverse, 0.65% isotropic (0.64% statistical, 0.7% with systematics on the optimal combination).
- D_H/r_d = 8.632 ± 0.098 (stat) ± 0.026 (theory sys); combined 8.632 ± 0.101.
- D_M/r_d = 38.99 ± 0.52 (stat) ± 0.12 (theory sys); combined 38.99 ± 0.53.
- Correlation ρ = −0.457 (stat), −0.431 (stat + sys).

Later values from the same data with the full shape (arXiv:2607.27410): D_H/r_d = 8.600 ± 0.066, D_M/r_d = 39.32 ± 0.33, ρ = +0.225.

Confidence: high.

Found in: `cosmo-lyman-alpha/references/results.md` lines 14–18, 21, 23–25; `cosmo-lyman-alpha/SKILL.md` lines 24–25. Cross-check: `cosmo-galaxy-clustering/references/results.md` line 29 gives 38.988 ± 0.531, 8.632 ± 0.101, ρ = −0.431, z_eff = 2.330 — identical.

Navigation: `SKILL.md` already holds the values; the precision needed `results.md`, reached at the first try.

## 3. DESI Lyα P1D: releases, estimators, k and z ranges

Answer:

| Release | Estimator | Sample | z range | k range | arXiv |
|---|---|---|---|---|---|
| EDR (SV + first two months, "M2") | FFT | 26,330 QSOs | z > 2.1 | not given | 2306.06311 |
| EDR (same) | QMLE | 54,600 QSOs | not given | not given | 2306.06316 |
| DR1 | QMLE, cross-exposure noise estimator, correlations between z bins | > 300,000 Lyα QSOs at S/N > 1 | 11 bins, z = 2.2–4.2, Δz = 0.2 | measurement range not given; cosmology uses 10⁻³ s/km < k < 0.5π/R_z = 0.0255 (z = 2.2) to 0.0414 s/km (z = 4.2) [der in the skill] | 2505.07974 |
| DR1 | FFT, cross-exposure noise estimator, no cross-bin correlations | same parent sample, different quasar selection | same bins | not given | 2505.09493 |
| DR2 | none published | — | — | — | — |

Companions for DR1: estimator validation arXiv:2509.13593; cosmology arXiv:2601.21432 (QMLE, 62,807 quasars at S/N > 3).

Confidence: medium (releases, estimators, IDs high; ranges incomplete).

Found in: `cosmo-lyman-alpha/references/results.md` lines 150–153, 159–163; `cosmo-lyman-alpha/references/surveys-and-data.md` lines 41–43; `cosmo-lyman-alpha/references/open-questions.md` line 153 (no DR2 P1D found).

Navigation: `results.md` at the first try for the table; `surveys-and-data.md` was needed as a second file to confirm that "DESI early data" in the table means EDR and that DR2 has no P1D. The table gives year 2024 for arXiv:2306.06316 while the identifier is from 2023.

NOT IN SKILL: the k range of both EDR measurements; the z range of the EDR QMLE measurement; the k range of the two DR1 measurement papers (line 163 states it "was not read"). Only the k range used for DR1 cosmology is given.

## 4. ACT DR6 power spectra: H0 and n_s in ΛCDM

Answer (base ΛCDM):

| Data set | H0 [km/s/Mpc] | n_s | Source |
|---|---|---|---|
| ACT DR6 alone, as rerun by SPT (DR6 TT/TE/EE + ACT DR6 lensing + τ prior) | 66.51 ± 0.64 | 0.9682 ± 0.0069 | arXiv:2506.20707, Table 1 |
| P-ACT (ACT DR6 + Planck PR3 cut at ℓ < 1000 TT, ℓ < 600 TE/EE, + low-ℓ TT + SRoll2) | 67.62 ± 0.50 | 0.9709 ± 0.0038 | arXiv:2503.14452 |
| W-ACT (ACT DR6 + WMAP9 + SRoll2) | 66.78 ± 0.68 | 0.9660 ± 0.0046 | arXiv:2503.14452 |
| P-ACT-LB (+ lensing + DESI DR1 BAO) | 68.22 ± 0.36 | 0.974 ± 0.003 | arXiv:2503.14452 |

ACT DR6 power-spectrum and ΛCDM paper: Louis et al. 2025, arXiv:2503.14452.

Confidence: high for P-ACT and W-ACT; medium for "ACT alone" (not ACT's own number).

Found in: `cosmo-cmb/references/results.md` lines 19–23 (data-set definitions), 39 and 42 (SPT rerun column), 63–78 (ACT's own combinations), 361–363 (the gap); `cosmo-cmb/SKILL.md` lines 26–28.

Navigation: `SKILL.md` sent to `results.md` at the first try; the gap is declared in the file's "Not verified" section.

NOT IN SKILL: the ACT DR6-alone H0 and n_s as printed in ACT's own paper (Table 5 of arXiv:2503.14452). The file states they "were not extracted"; the only ACT-alone column is the SPT rerun, which includes ACT lensing and a τ prior.

## 5. SPT-3G D1: H0 and the tension with SH0ES

Answer (flat ΛCDM, Camphuis et al. 2025, arXiv:2506.20707):

- SPT-3G D1 alone (TT/TE/EE + SPT-3G lensing + τ prior): H0 = 66.66 ± 0.60 km/s/Mpc; 6.2σ from SH0ES.
- SPT + ACT + Planck (CMB-SPA): H0 = 67.19 ± 0.38 km/s/Mpc (second arXiv version; the first gave 67.24 ± 0.35); 6.4σ from SH0ES.
- The SH0ES value behind these figures was read by the skill only as quoted by ACT DR6: 73.17 ± 0.86 [sec].

Confidence: high.

Found in: `cosmo-cmb/references/results.md` lines 42, 51–57, 335–336, 368–370; `cosmo-cmb/SKILL.md` lines 24–25. Cross-check: `cosmo-distance-ladder-h0/references/results.md` lines 107–109, 133, 145–147 — same values, same 6.2σ and 6.4σ.

Navigation: first try. No conflict: the distance-ladder table also lists 6.1 and 6.2 [der] for the 2025 SH0ES value 73.18 ± 0.88, a different local endpoint, and 67.24 ± 0.35 [sec] as the first-version CMB-SPA value adopted by H0DN.

## 6. DES Y6 3×2pt

Answer (flat ΛCDM, DES Collaboration 2026, arXiv:2601.14559): S8 = 0.789 ± 0.012, Ωm = 0.333 (+0.023/−0.028). Against the CMB, defined as Planck 2018 + ACT DR6 + SPT-3G DR1 primary anisotropies: 2.6σ projected on S8, 1.8σ in the full parameter space. In wCDM: S8 = 0.782 (+0.021/−0.020).

Confidence: high.

Found in: `cosmo-weak-lensing/references/results.md` lines 47–49, 33–37, 184; `cosmo-weak-lensing/SKILL.md` line 26.

Navigation: first try (`SKILL.md` already holds the headline).

## 7. KiDS-Legacy cosmic shear

Answer (flat ΛCDM, Wright et al. 2025, arXiv:2503.19441; KiDS DR5, 1347 deg²): S8 = 0.815 (+0.016/−0.021); Σ8 = σ8(Ωm/0.3)^0.58 = 0.821 (+0.014/−0.016); 0.73σ from Planck Legacy alone. The reference differs from the DES one (question 6), so the two tension figures are not comparable.

Confidence: high.

Found in: `cosmo-weak-lensing/references/results.md` lines 24, 33–37, 180; `cosmo-weak-lensing/SKILL.md` lines 24, 28.

Navigation: first try.

## 8. DES-SN5YR

Answer:

- Hubble diagram: 1635 DES photometrically classified SNe + 194 low-z = 1829 SNe (sum stated as 1829 in the distance-ladder skill; redshift range 0.01 < z < 1.13). DES Collaboration 2024, arXiv:2401.02929.
- Flat wCDM, SNe alone: (Ωm, w) = (0.264 (+0.074/−0.096), −0.80 (+0.14/−0.16)). With Planck, SDSS BAO and DES 3×2pt: (Ωm, w) = (0.321 ± 0.007, −0.941 ± 0.026). Flat ΛCDM: Ωm = 0.352 ± 0.017.
- Recalibration, step 1 — DES-Dovekie (Popovic et al., November 2025, arXiv:2511.07517): (i) the Fitzpatrick 1999 colour law in SNANA, previously a polynomial expansion around R_V = 3.1, replaced by the full law (~0.01 mag in simulated bias corrections); (ii) Dovekie cross-calibration in place of Fragilistic; (iii) retrained SALT3; (iv) regenerated bias-correction simulations; (v) a weighting error on nine calibration variants (0.3 instead of 0.33) that had made DES-SN5YR underestimate its photometric systematic by ~20%; (vi) σ_x1 cut moved from 1.0 to 1.15. Effect: Ωm 0.352 → 0.330 ± 0.015 (shift −0.022), wCDM w = −0.838 (+0.130/−0.142), effective N = 1684, w0wa preference with DESI DR2 + CMB 4.2σ → 3.2σ.
- Step 2 — host masses (January 2026, arXiv:2601.19424; September 2026, arXiv:2609.05321): low- and high-redshift host masses were inconsistent in Union3 and Pantheon+; DES-Dovekie is "essentially unchanged" by the remeasurement; the Hoyt et al. re-run gives 3.4σ for DES-Dovekie. DES-SN5YR is now superseded by DES-Dovekie and merged with Pantheon+ in Unite (2884 SNe, arXiv:2609.05053).

Confidence: high.

Found in: `cosmo-supernovae/references/results.md` lines 25, 43, 45, 71, 74, 89–93, 135–136, 143–145; `cosmo-supernovae/references/surveys-and-data.md` lines 55–56, 69–77; `cosmo-supernovae/SKILL.md` lines 33–38; total 1829 in `cosmo-distance-ladder-h0/references/surveys-and-data.md` line 76.

Navigation: `results.md` at the first try for N and w; the list of what changed is in `surveys-and-data.md`, a second file, which the file map announces as "what is superseded". The supernova skill never prints the total 1829, only "1635 + 194".

## 9. Pantheon+ and Union3

Answer (flat ΛCDM, SNe alone):

| Sample | N | Ωm | Source |
|---|---|---|---|
| Pantheon+ | 1550 SNe (1701 light curves, 18 surveys, 0.001 < z < 2.26) | 0.334 ± 0.018 | Brout et al. 2022, arXiv:2202.04077 (sample: arXiv:2112.03863) |
| Union3 (UNITY1.5) | 2087 SNe from 24 datasets | 0.356 (+0.028/−0.026) | Rubin et al. 2023, arXiv:2311.12098 |
| Union3.1 (supersedes Union3) | ~2000 | 0.344 (+0.026/−0.025) | Hoyt et al. 2026, arXiv:2601.19424 |

Status: Union3 is superseded by Union3.1; Pantheon+ stands as published in 2022 with host masses and calibration since revised (in Unite).

Confidence: high.

Found in: `cosmo-supernovae/references/results.md` lines 22, 24, 26, 133–134, 137; `cosmo-supernovae/references/surveys-and-data.md` lines 53–54, 57. Cross-check: `cosmo-distance-ladder-h0/references/surveys-and-data.md` line 73 gives the same 1701 / 1550.

Navigation: first try.

## 10. Latest H0 from SH0ES and from CCHP (JWST)

Answer:

- SH0ES, latest (Riess et al. 2025, arXiv:2509.01667): H0 = 73.18 ± 0.88 km/s/Mpc from JWST Cepheids in 19 hosts (24 SNe Ia) + HST Cepheids in 37 hosts (42 SNe Ia) + 35 TRGB calibrations, 55 SNe Ia in total, q0 fixed in the intercept; Cepheids only: 73.49 ± 0.93. Indicators: Cepheids and TRGB calibrating SNe Ia. The HST-only four-anchor value (Milky Way, LMC, SMC, NGC 4258) is 73.17 ± 0.86 (Breuval et al. 2024, arXiv:2404.08038). The skill says the JWST ladders rest on NGC 4258 alone.
- CCHP, latest (Freedman et al. 2024, arXiv:2408.06153): H0 = 70.39 ± 1.22 (stat) ± 1.33 (sys) ± 0.70 (σ_SN), total 1.94 [der]; TRGB with 24 SN Ia calibrators from HST + JWST, anchor NGC 4258, Carnegie Supernova Project SNe. JWST-only values in the same paper: TRGB 68.81 ± 1.79 ± 1.32 (10 galaxies, 11 SNe Ia) and JAGB 67.80 ± 2.17 ± 1.64. Follow-up: Hoyt et al. 2025 (arXiv:2503.11769), JWST F115W TRGB, 11 calibrators, 68.4 to 69.6 over four SN magnitude sets.
- Community combination for reference: H0DN 73.50 ± 0.81 (arXiv:2510.23823).

Confidence: high for SH0ES; medium for CCHP (the skill warns that only the current arXiv abstract of arXiv:2408.06153 was read).

Found in: `cosmo-distance-ladder-h0/references/results.md` lines 25–32, 41–44, 183–196; `cosmo-distance-ladder-h0/SKILL.md` lines 27–38; `cosmo-distance-ladder-h0/references/open-questions.md` lines 21–25, 49–54, 284–285.

Navigation: first try. Inside the skill the description of the 70.39 value differs slightly: `results.md` line 29 labels it "CCHP TRGB, 24 SN Ia calibrators from HST + JWST", `open-questions.md` lines 21–22 say "TRGB and JAGB distances from JWST … give 70.39"; which indicators enter that number is therefore ambiguous.

NOT IN SKILL: the CCHP JWST Cepheid H0 (the programme uses TRGB, JAGB and Cepheids, but the Cepheid result is listed as not verified); any CCHP H0 from the 2026 revised Milky Way Cepheid calibration; whether a SH0ES 2026 paper appeared after 1 October 2026; the anchors of the 73.18 value stated in its own row.

## 11. Euclid data releases public as of October 2026

Answer:

- Public: Q1 quick release, March 2025 — 63.1 deg² of the Euclid Deep Fields (North, South, Fornax) at wide-survey depth, about 30 million objects, early pipelines; not a cosmology release (arXiv:2503.15302).
- Not yet public in October 2026: DR1-Foundation (raw and calibrated images, catalogues, spectra over about 1900 deg², Wide Survey observations from 14 February 2024 to 21 May 2025), planned for 12 November 2026; complete DR1 with the galaxy-clustering and weak-lensing products, mid-2027. Source cited by the skills: ESA Euclid DR1 timeline page dated 15 June 2026, and the IPAC DR1 page for the day.
- "Euclid DR1 in October 2026" is listed as a stale claim.

Confidence: medium (planned dates; release list not shown to be exhaustive).

Found in: `cosmo-galaxy-clustering/references/surveys-and-data.md` lines 180–190, 261, 266–267; `cosmo-weak-lensing/references/surveys-and-data.md` line 135; `cosmo-galaxy-clustering/references/open-questions.md` lines 267–269; `cosmo-weak-lensing/SKILL.md` lines 34, 56.

Navigation: first try in either skill (both file maps point to `surveys-and-data.md`). The day of DR1-Foundation (12 November) is only in the galaxy-clustering skill; the weak-lensing skill gives the month.

NOT IN SKILL: the day of the Q1 release (only "March 2025"; the weak-lensing file dates the paper, not the release); whether any other Euclid public release exists besides Q1 (no file states that the list is complete).

## 12. Systematics a referee expects

### (a) Cosmic shear

| Systematic | Reference paper (as given by the skill) |
|---|---|
| Shear measurement bias: noise, model, selection | metacalibration, Sheldon & Huff 2017, arXiv:1702.02601 (metadetection: arXiv:1911.02505) |
| Blending and its coupling to redshift | MacCrann et al. 2022, arXiv:2012.08567 |
| PSF modelling and leakage | Paulin-Henriksson et al. 2008, arXiv:0711.4886 (ρ statistics: Rowe 2010, arXiv:0904.3056) |
| B-mode null tests | Daley et al. 2026, arXiv:2604.03227 |
| Redshift distributions (SOM, clustering redshifts, shear ratio) | review, Newman & Gruen 2022, arXiv:2206.13633 (SOM: Masters et al. 2015, arXiv:1509.03318) |
| Intrinsic alignments | NLA, Bridle & King 2007, arXiv:0705.0166 (TATT: Blazek et al. 2019, arXiv:1708.09247) |
| Baryonic feedback | van Daalen et al. 2011, arXiv:1104.1174 (HMcode-2020: Mead et al. 2021, arXiv:2009.01858) |
| Covariance and goodness of fit | DES Y3 covariance validation, arXiv:2012.08568 (KiDS-Legacy: arXiv:2410.06962) |
| Limber approximation | LoVerde & Afshordi 2008, arXiv:0809.5112 |
| Source clustering, reduced shear | arXiv:2606.12389 |
| Spatially varying depth | Rodríguez-Monroy et al. 2025, arXiv:2509.07943 |
| Blinding and post-unblinding changes | Muir et al. 2020, arXiv:1911.05929 (KiDS: Kuijken et al. 2015, arXiv:1507.00738) |
| Projection and prior-volume effects (mean versus MAP) | DES Y3 + KiDS-1000, arXiv:2305.17173 |
| CMB reference and tension metric | arXiv:2602.12238 |

For galaxy–galaxy lensing and 3×2pt the skill adds magnification (Elvin-Poole et al. 2023, arXiv:2209.09782) and non-linear bias with the point-mass term (Prat et al. 2022, arXiv:2105.13541).

### (b) Lyα 3D BAO

| Systematic | Reference paper (as given by the skill) |
|---|---|
| Continuum fitting and distortion of the correlations | distortion matrix, arXiv:1702.00176 (test: Busca et al. 2025, arXiv:2506.15262) |
| Pixel weighting | arXiv:2306.06312 |
| High-column-density systems (DLA finder, residual HCD model) | Rogers et al. 2018, arXiv:1711.06275 (DR2 catalogue: arXiv:2503.14740) |
| Metal absorption (Si II 1260 near the BAO scale along the line of sight) | Guy et al. 2025, arXiv:2404.03003 |
| BAL quasars | arXiv:2111.09439 (DESI DR1: arXiv:2405.09737) |
| UV-background fluctuations | Gontcho A Gontcho et al. 2014, arXiv:1404.7425 (Pontzen 2014, arXiv:1402.0506) |
| Relics of patchy reionisation | Montero-Camacho et al. 2019, arXiv:1902.02892 |
| Correlated sky-subtraction and calibration noise | Guy et al. 2025, arXiv:2404.03003 |
| Quasar redshift errors | Youles et al. 2022, arXiv:2205.06648 (Bault et al. 2025, arXiv:2402.18009) |
| Non-linear BAO broadening and shift (theory systematic 0.3% per direction in DR2) | arXiv:2412.06892 (opposite sign: arXiv:2503.13442; budget: arXiv:2503.14739) |
| Small-scale leakage through the distortion matrix | arXiv:2607.27410 (mainly an AP issue) |
| Covariance matrix | arXiv:2503.14739, Sects. 4 and 6.3 (multipoles: arXiv:2603.04281) |
| Validation on mocks containing the effects | arXiv:2404.03004 (DR1), arXiv:2503.14741 (DR2) |
| Blinding | arXiv:2404.03001 (practice); method, arXiv:2607.07875 |

Confidence: high that these are the lists and references the skills give.

Found in: `cosmo-weak-lensing/references/systematics.md` lines 17–62, 64–85, 87–113, 115–173, 175–223, 225–279, 294–304, 306–326; `cosmo-weak-lensing/references/physics-and-methods.md` lines 160–170 (blinding); `cosmo-weak-lensing/SKILL.md` lines 28, 33, 37–48. `cosmo-lyman-alpha/references/systematics.md` lines 12–19, 29–37, 41–49, 51–58, 60–64, 66–78, 102–106, 114–120, 124–137, 150–152, 179–194; `cosmo-lyman-alpha/SKILL.md` line 39.

Navigation: both `SKILL.md` files sent to `systematics.md` at the first try. Two limits: (i) the weak-lensing `systematics.md` checklist names blinding, projection effects and the tension metric without a reference; the references had to be taken from `physics-and-methods.md` and from `SKILL.md`; (ii) the Lyα `systematics.md` mixes 3D and P1D effects without marking which apply to BAO, so the subset above (mean flux, resolution, noise power, emulator and thermal priors left out as P1D items) is this reader's selection.

---

## CONFLICT

None found between skills. Values checked in two skills and found identical: DESI DR2 Lyα BAO distances and correlation (lyman-alpha, galaxy-clustering); w0wa significances and posteriors of arXiv:2503.14738 (galaxy-clustering, supernovae); SPT-3G D1 and CMB-SPA H0 and the 6.2σ / 6.4σ figures (cmb, distance-ladder-h0); Pantheon+ counts and the DES-SN5YR total (supernovae, distance-ladder-h0); Euclid release schedule (galaxy-clustering, weak-lensing).

Differences that are not conflicts but can be misread:

- 2.8 / 3.8 / 4.2σ (galaxy-clustering) against 3.2 / 3.4 / 3.4σ (supernovae): original DESI DR2 figures against the 2026 re-runs; only the supernova skill says the former are superseded.
- CMB-SPA H0 67.19 ± 0.38 (cmb, second version) against 67.24 ± 0.35 (distance-ladder-h0 `results.md` line 109, flagged [sec], as adopted by H0DN): first and second arXiv versions, explained in the cmb skill.
- Internal to distance-ladder-h0: the 70.39 CCHP value is described as TRGB with HST + JWST calibrators in `results.md` and as "TRGB and JAGB distances from JWST" in `open-questions.md`.

## NOT IN SKILL — consolidated

1. Q3: k ranges of the DESI EDR P1D (FFT, QMLE), z range of the EDR QMLE, k range of the DR1 measurement papers.
2. Q4: ACT DR6-alone H0 and n_s from ACT's own table.
3. Q10: CCHP JWST Cepheid H0; CCHP H0 with the 2026 Milky Way recalibration; anchors of the SH0ES 73.18 value in its row.
4. Q11: day of the Euclid Q1 release; completeness of the list of Euclid public releases.
5. Q1 (minor): DESI + supernovae without CMB.

## Navigation — consolidated

- Wrong file at the first try: none.
- Second file needed inside one skill: Q3 (`surveys-and-data.md` to identify the releases), Q8 (`surveys-and-data.md` for what changed), Q12a (`physics-and-methods.md` and `SKILL.md` for three references).
- Second skill needed: Q1 (supernova skill for the superseded significances; no warning in the galaxy-clustering skill), Q8 (total 1829 only in the distance-ladder skill).
- Reader's own filtering needed: Q12b (3D against P1D systematics not separated).
