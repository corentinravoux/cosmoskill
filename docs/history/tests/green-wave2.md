# GREEN test — wave 2 skills — 2026-10-09

Rules: open-book, answers taken ONLY from the files of the six skill directories (`cosmo-peculiar-velocities`, `cosmo-dark-energy-modified-gravity`, `cosmo-neutrinos-dark-matter`, `cosmo-clusters`, `cosmo-cmb-lss-cross-correlations`, `cosmo-beyond-two-point`), SKILL.md read first and its file map used to pick the reference file; no web, no arXiv tools, no memory, `baseline-wave2.md` not read; the only exception used is the explicit path pointer from `cosmo-peculiar-velocities` to the hub files `pv-surveys.md` and `fsigma8-pv-compilation.md`, flagged where followed.

Path prefix for all "Found in" entries: `<skills>/`. Confidence = confidence that the answer reproduces what the skill states (all values carry the skill's own `[src]` flag unless noted).

---

## Q1. DESI DR1 peculiar velocities

**Answer.**
- Correlation functions (galaxy + momentum; Turner et al.): fσ8 = 0.391 +0.080/−0.081 — arXiv:2512.03230.
- Power spectra (Qin et al.): fσ8 = 0.440 +0.080/−0.096 — arXiv:2512.03231.
- Maximum-likelihood fields / field-level (Lai et al.): fσ8 = 0.483 +0.080/−0.043 (stat) ± 0.018 (sys) — arXiv:2512.03229.
- Consensus (correlated combination, correlations 27–39 % from 675 mocks): fσ8 = 0.4497 ± 0.0548 at z_eff = 0.07 — arXiv:2512.03230 (construction described in arXiv:2512.03228 §9).
- Velocities entering: 73 686 FP and 2 929 TF after the 4σ cut on η (TF at z > 0.05 removed); 76 615 (correlation functions) / 76 616 (field-level) velocities in the fit, with 415 523 BGS redshifts. "Over 90 %" FP.
- Dataset/model: DESI DR1 PV + BGS, one catalogue, three estimators; z_eff = mean redshift of all galaxies.
- Confidence: high.

**Found in:** `cosmo-peculiar-velocities/SKILL.md` L28–32 (central values, consensus, counts); `references/results.md` L32, L38–45, L57–60 (which estimator gives which value, consensus construction); `references/surveys-and-data.md` L76–87 (cut flow, counts, z_eff). Per-estimator uncertainties only via the hub pointer (followed, as `results.md` L7–10 and L21 send there by path): `observational-cosmology/references/pv-surveys.md` L203–206 and `fsigma8-pv-compilation.md` L117–120.

**Navigation:** SKILL.md alone answered most of it; file map sent me to `results.md` correctly at first try for the estimator labels. The per-estimator error bars are not in any file of the skill — `results.md` says "the three fσ8 values … are in the hub table", so a second hop outside the skill was required.

**NOT IN SKILL:** uncertainties of the three individual estimators (present only in the hub files).

**CONFLICT (minor, internal):**
- TF clustering-sample size: "6 807 in the clustering catalogue" (`results.md` L28, `surveys-and-data.md` L69) vs "6 806" (`surveys-and-data.md` L79, `systematics.md` L158).
- Source attributed to the consensus: arXiv:2512.03228 + 2512.03230 (`SKILL.md` L30), 2512.03230 (`results.md` L32) with construction in 2512.03228 §9 (`results.md` L38), 2512.03230 + 2512.03231 (hub `fsigma8-pv-compilation.md` L120).

---

## Q2. Cosmicflows-4 bulk flow

**Answer.**
- Claimed excess (Watkins et al. 2023, arXiv:2302.02028; CF4, minimum-variance top-hat estimator): 387 ± 28 km/s at 150 h⁻¹Mpc (ΛCDM expectation 139) and 419 ± 36 km/s at 200 h⁻¹Mpc (expectation 120).
- Significance as first quoted: χ² probability 0.023 % at 150 and 0.00021 % at 200 h⁻¹Mpc (Table 1; "less than 0.003 %" in the abstract); circulating as "4.8σ" (hub: 4.81σ at 200 h⁻¹Mpc).
- As reassessed (Whitford, Howlett & Davis 2023, arXiv:2306.11269; mock-calibrated errors): 428 ± 108 km/s at 173 h⁻¹Mpc, probability 0.11 %; amplitude confirmed, errors had been underestimated. CF4++ gives 315 ± 40 km/s at 150 h⁻¹Mpc (arXiv:2502.01308).
- Latest (2026) reanalysis: Nusser & Tully 2026, arXiv:2608.14265 (August 2026) — monopole + dipole in six radial bins to 300 h⁻¹Mpc with the ΛCDM prediction for the actual positions and covariances: full range 2.29σ (dipole), 2.36σ (joint), "broadly consistent with ΛCDM"; localised excess at 120–160 h⁻¹Mpc, |V_dip| = 628 ± 82 km/s, 3.40σ, falling to 1.56σ without 6dFGS and rising to 3.77σ without SNe. Also 2026: Do et al. (arXiv:2606.17142) SN Ia flows ~100–400 km/s, consistent with ΛCDM.
- Confidence: high.

**Found in:** `cosmo-peculiar-velocities/SKILL.md` L48–50, L69; `references/results.md` L139–142, L144, L148–149, L183–187, L291; `references/open-questions.md` L18–22, L32–38, L235. Hub pointer followed for the σ figure: `observational-cosmology/references/pv-surveys.md` L328–332.

**Navigation:** right file at first try (`results.md`, "bulk-flow record").

**NOT IN SKILL:** the origin of the "4.8σ" figure (which depth, which paper statement) — the skill's own files only name it as a stale claim (`SKILL.md` L69, `open-questions.md` L235) next to probabilities; the depth (200 h⁻¹Mpc, 4.81σ) is only in the hub.

---

## Q3. Evolving dark energy

**Answer** (flat w0waCDM vs ΛCDM, Δχ²_MAP converted to σ unless stated).
- DESI DR2 BAO alone 1.7σ; + CMB 3.1σ (w0 = −0.42 ± 0.21, wa = −1.75 ± 0.58); with compressed CMB priors 2.4σ — arXiv:2503.14738 (March 2025). Still current.
- DESI DR2 + CMB + SN as published in March 2025: Pantheon+ 2.8σ, Union3 3.8σ, DESY5 4.2σ (arXiv:2503.14738) — superseded.
- Current, after the supernova revisions:
  - DES-Dovekie: 3.2σ, w0 = −0.803 ± 0.054, wa = −0.72 ± 0.21 (Popovic et al. 2025, arXiv:2511.07517); 3.4σ as recomputed by Hoyt et al. (arXiv:2601.19424).
  - Union3.1: 3.4σ, w0 = −0.719 ± 0.084, wa = −0.95 +0.29/−0.26 (Hoyt et al. 2026, arXiv:2601.19424).
  - Pantheon+ with corrected host masses: 3.2σ (arXiv:2601.19424).
  - Unite (2884 SNe) + CMB + DES and DESI BAO: 3.3σ (MAP), 3.1σ (maximum likelihood) (Camilleri et al. 2026, arXiv:2609.05053, Sept 2026).
- DES Y6 all probes (SN + BAO + 3×2pt): alone 2.2σ (w0 = −0.84 ± 0.10, wa = −0.44 +0.60/−0.55); + DESI DR2 BAO, no CMB 2.3σ; + DESI DR2 BAO + primary CMB 3.0σ (w0 = −0.82 ± 0.05, wa = −0.63 +0.21/−0.18); same without supernovae 2.6σ — DES Collaboration 2026, arXiv:2605.27221 (May 2026).
- Bayesian evidence (ln B = ln Z(w0wa) − ln Z(Λ), Lodha et al. 2025, arXiv:2503.14743, DR2 + CMB +): Pantheon+ −0.66 ± 0.44 (inconclusive, on the side of Λ, although 2.8σ in Δχ²), Union3 3.03 ± 0.44 (moderate), DESY5 4.88 ± 0.44 (almost strong). After revisions: Dovekie odds ≈ 5:1 (ln B ≈ 1.6 [der]), "only a weak preference" (arXiv:2511.07517); Unite "only weak" (arXiv:2609.05053).
- Confidence: high.

**Found in:** `cosmo-dark-energy-modified-gravity/SKILL.md` L24–35; `references/results.md` L22–35 (DR2 table), L115–139 (revised SN, DES Y6), L156–180 (evidence), L329–342 (history).

**Navigation:** right file at first try.

**CONFLICT (documented in the skill):** DESI DR2 + CMB + DES-Dovekie is 3.2σ (arXiv:2511.07517) and 3.4σ (arXiv:2601.19424) — `results.md` L117, L119, L127–130.

---

## Q4. Modified gravity

**Answer.**
- μ0, Σ0 from DESI full shape with external data (convention GR = 0, time dependence ∝ Ω_DE(a)): DESI DR1 (FS + BAO) + CMB + DES Y3 + DESY5 SN, ΛCDM background: μ0 = 0.05 ± 0.22, Σ0 = 0.008 ± 0.045; w0wa background: μ0 = −0.24 +0.32/−0.28, Σ0 = 0.006 ± 0.043 — Ishak et al. 2024, arXiv:2411.12026 (Nov 2024). DESI only (DR1 FS + BAO + BBN + n_s prior): μ0 = 0.11 +0.44/−0.54; DESI DR1 P + LRG bispectrum + DR2 BAO: μ0 = 0.12 ± 0.49 (arXiv:2606.23936, June 2026). No DESI DR2 full-shape MG analysis exists. (Non-DESI-FS, non-collaboration: KiDS-Legacy + CMB + DESI DR2 BAO + Dovekie gives Σ0 = 0.149 ± 0.051, 3.0σ, arXiv:2602.03110.)
- E_G: the skill's headline value is 0.36 +0.06/−0.05 at z = 0.555 (Planck lensing × CMASS) against GR 0.401 ± 0.005, and 0.40 +0.11/−0.09 at z = 0.316 (LOWZ) against 0.452 ± 0.005 — Wenzl et al. 2024, arXiv:2401.12971. The latest listed measurement is Zhang et al. 2026, arXiv:2604.24631 (April 2026): 0.503 ± 0.054 at z = 0.38 and 0.444 ± 0.054 at z = 0.61 (KiDS-1000 × BOSS/2dFLenS, no Planck prior), "consistent" with GR.
- Tightest Hu–Sawicki bound: f_R0 < 1.4 × 10⁻⁸ (n = 1; galaxy morphology: gas–star offsets, disk warps) — Desmond & Ferreira 2020, arXiv:2009.08743. Cosmological-scale bounds are 10⁻⁵-level: log10|f_R0| < −4.59 (95 %, DESI DR1 full-shape P, arXiv:2604.26915), < −4.79 (clusters, arXiv:1412.0133); the clusters skill adds < −5.32 (SPT clusters + Planck, arXiv:2409.13556) and < −4.31 (eRASS1, arXiv:2402.08459).
- Confidence: high for μ0/Σ0 and f_R0; medium for "latest E_G" (see below).

**Found in:** `cosmo-dark-energy-modified-gravity/SKILL.md` L46–54, L79; `references/results.md` L228–237, L293–303, L309–315, L364–366; `references/open-questions.md` L275–280; `cosmo-clusters/references/results.md` L18, L45; `cosmo-cmb-lss-cross-correlations/references/results.md` L80–81.

**Navigation:** right file at first try (`results.md`). Misleading point: SKILL.md L53–54 presents the 2024 Wenzl value as "the" E_G, while the results table holds a 2026 measurement; a reader stopping at SKILL.md gives a stale "latest".

**NOT IN SKILL:** the numerical GR prediction for the 2026 E_G values (table says only "consistent"); so "latest E_G against its GR prediction" can be given with numbers only for the 2024 measurement.

**CONFLICT (cross-skill):** E_G at z_eff = 0.555 / 0.316 — `cosmo-dark-energy-modified-gravity/references/results.md` L311–312: 0.36 +0.06/−0.05 and 0.40 +0.11/−0.09 (Planck × BOSS, arXiv:2401.12971); `cosmo-cmb-lss-cross-correlations/references/results.md` L80–81: 0.31 +0.06/−0.05 (ACT), 0.34 ± 0.05 (ACT + Planck PR4) and 0.49 +0.14/−0.11, 0.43 +0.11/−0.09 (ACT DR6 × BOSS, arXiv:2405.12795). Different papers, same GR predictions (0.401, 0.452); neither skill cites the other's paper, so each gives a different "current" value.

---

## Q5. Sum of neutrino masses

**Answer.**
- DESI DR2 BAO + CMB (baseline CamSpec), ΛCDM + Σm_ν, prior Σm_ν > 0, three degenerate states: Σm_ν < 0.0642 eV (95 %), σ = 0.020 eV — Elbers et al. 2025, arXiv:2503.14744 (companion arXiv:2503.14738), March 2025. Other Planck likelihoods: < 0.0691 eV (plik), < 0.0774 eV (LoLLiPoP-HiLLiPoP). Feldman–Cousins: < 0.053 eV.
- w0waCDM: < 0.163 eV (BAO + CMB); < 0.117 / 0.139 / 0.129 eV with Pantheon+ / Union3 / DESY5; Feldman–Cousins < 0.177 eV.
- Effective (signed) mass, DESI DR2 BAO + CMB: Σm_ν,eff = −0.101 +0.047/−0.056 eV (σ = 0.053 eV), 3σ below the oscillation lower limit (0.059 eV normal, 0.10 eV inverted) — arXiv:2503.14744; DR1 predecessor −0.125 +0.058/−0.070 eV, 2.8–3.3σ (Elbers et al. 2024, arXiv:2407.10965). Tension vanishes in w0waCDM, with free lensing amplitudes (−0.018 +0.085/−0.089 eV, arXiv:2511.01967) or τ ≈ 0.09 (arXiv:2504.16932).
- Tightest published limit: Σm_ν < 0.049 eV (95 %), Ivanov et al. 2026, arXiv:2601.16165 — EFT reanalysis of DESI DR1 full shape + bispectrum + cross-correlations + DESI BAO + CMB + SNe, not a DESI Collaboration result (< 0.077 eV in w0waCDM).
- Confidence: high.

**Found in:** `cosmo-neutrinos-dark-matter/SKILL.md` L24–32, L59–60; `references/results.md` L35–39, L50, L57–64, L74, L81–85.

**Navigation:** right file at first try; SKILL.md alone gives every headline number, authors of the 0.049 eV limit only in `results.md`.

**CONFLICT (documented, source-internal):** P-ACT-LB limit 0.089 eV in the paper text vs 0.082 eV in the arXiv abstract (`SKILL.md` L34–35, `results.md` L41, L306). DESI DR1 + CMB limit appears as 0.070 eV (`results.md` L33), 0.072 eV (L34, L305) and 0.077 eV as quoted by ACT (L45).

---

## Q6. Neutrino mass ordering and laboratory limits

**Answer.**
- JUNO (207.2 live days, 8 294 IBD candidates, mean baseline 52.5 km; arXiv:2609.37895, Sept 2026): Δm²_31 = +2.509 +0.027/−0.025 × 10⁻³ eV² (normal) or −2.482 +0.025/−0.026 × 10⁻³ eV² (inverted); sin²θ_12 = 0.3036 ± 0.0064; Δm²_21 = (7.388 ± 0.078) × 10⁻⁵ eV². With long-baseline accelerator Δm²_31: normal ordering favoured at ≥ 2.1σ (one-sided) for all CP phases, Bayes factor 10.18.
- KATRIN: m_ν < 0.45 eV at 90 % CL (m_ν² = −0.14 +0.13/−0.15 eV²; 259 days, 36 million electrons), Aker et al. 2024, arXiv:2406.13516. This is the effective electron-antineutrino mass, not Σm_ν (implied Σm_ν ≲ 1.3 eV).
- Cosmological Bayes factor for normal ordering: K = 10, P(NO) = 0.91 (ΛCDM, DESI DR2 BAO + CMB + NuFIT 6.0, equal prior odds; K = 6 with L-H, 8 with plik), arXiv:2503.14744; frequentist χ²(IO) − χ²(NO) = 4.6. Other priors/data: 46.5 (CMB + DESI DR1 + background probes, arXiv:2407.18047); K > 460 in ΛCDM, > 40 in extensions (Jimenez et al. 2026, arXiv:2606.18987). Oscillations alone are undecided (arXiv:2410.05380).
- Confidence: high.

**Found in:** `cosmo-neutrinos-dark-matter/SKILL.md` L38–42; `references/results.md` L17–22, L107–115.

**Navigation:** right file at first try.

---

## Q7. Warm and fuzzy dark matter

**Answer** (thermal relic making all the dark matter, 95 % lower limits unless stated).
- Lyα forest: range 1.9–5.7 keV depending on the thermal-history prior: > 5.7 keV (HIRES + UVES, z = 4.2–5.0, k_max = 0.2 s/km; > 4.1 keV at k_max < 0.1 s/km), Iršič et al. 2023, arXiv:2309.04533; > 1.9 keV for the coldest allowed reionisation histories, Garzilli et al. 2019, arXiv:1912.09397; > 3.1 keV (Villasenor et al. 2022, arXiv:2209.14220); > 5.3 keV (SDSS DR14 + XQ-100, arXiv:1911.09073; XQ-100 + HIRES/MIKE 2σ, arXiv:1702.01764; 3.5 keV with temperature jumps); > 3.3 keV (arXiv:1306.2314).
- Milky Way satellites: > 6.5 keV (DES + Pan-STARRS1), Nadler et al. 2020, arXiv:2008.00022; MW + M31: > 6.20 keV (arXiv:2512.01361).
- Strong lensing: > 5.2 keV (8 quads, arXiv:1908.06983); JWST flux ratios of 31 lensed quasars > 5.6 keV (Galacticus subhalo prior) or > 6.4 keV (N-body prior), Bayes factor 10:1 (Keeley et al. 2025, arXiv:2511.07765); flux ratios + arcs of 28 quads > 6.5 or > 7.4 keV (Gilman et al. 2025/2026, arXiv:2511.07513, arXiv:2606.05277). Joint lensing + satellites 9.7 keV (arXiv:2101.07810) used the 2019 lensing posterior — not current.
- Fuzzy dark matter from the forest (boson mass, all of the DM): > 2 × 10⁻²⁰ eV (95 %, Rogers & Peiris 2020, arXiv:2007.12705); > 20 × 10⁻²² eV (2σ) with temperature jumps, > 37.5 × 10⁻²² eV for a power-law thermal history (Iršič et al. 2017, arXiv:1703.04683); > 1.9 × 10⁻²¹ eV (95 %, P1D at z = 4.2–5.0, Liu, Gong & Zhou 2026, arXiv:2606.06969 — weakest, own IGM marginalisation). Sub-component: f_FDM < 0.07, 0.12, 0.65 at log10(m/eV) = −23, −22, −21 (arXiv:2606.06969). 10⁻²² eV excluded as all of the dark matter.
- Confidence: high.

**Found in:** `cosmo-neutrinos-dark-matter/SKILL.md` L46–52; `references/results.md` L184–195, L201–211, L228–239, L249, L327–331.

**Navigation:** right file at first try.

---

## Q8. Cluster cosmology

**Answer** (S8 = σ8(Ω_m/0.3)^0.5, flat ΛCDM).
- eRASS1 (5259 clusters, 12791 deg², WL from DES Y3, KiDS-1000, HSC): S8 = 0.86 ± 0.01 — Ghirardini et al. 2024, arXiv:2402.08458.
- SPT (1005 clusters + DES Y3 and HST lensing, Σm_ν marginalised): S8 = 0.795 ± 0.029; best-constrained σ8(Ω_m/0.3)^0.25 = 0.805 ± 0.016 — Bocquet et al. 2024, arXiv:2401.02075. With DES Y3 3×2pt: 0.796 ± 0.013 (arXiv:2412.07765).
- DES Y3 clusters (~16 000 redMaPPer, ~5000 deg²): S8 = 0.864 ± 0.035; 0.811 +0.022/−0.020 with 3×2pt — DES Collaboration 2025, arXiv:2503.13632.
- KiDS-1000 AMICO (~8000 clusters, 839 deg², counts + stacked lensing): S8 = 0.74 ± 0.03, 2.8σ from Planck — Lesci et al. 2025, arXiv:2507.14285.
- Latest Planck PSZ2 reanalysis (PSZ2 cosmology sample + DES shear profiles + Chandra + BAO; Aymerich et al. 2025, arXiv:2509.02068, Sept 2025): S8 = 0.791 +0.023/−0.021 (constant bias; Ω_m = 0.312 +0.018/−0.024, σ8 = 0.777 ± 0.024); 0.814 +0.019/−0.020 with mass-dependent bias; 1.6σ from the CMB, 2.9σ from eRASS1.
- Hydrostatic mass bias it finds: (1 − b) = 0.844 +0.055/−0.062, relative to a Chandra-calibrated relation (not comparable with XMM-referenced values: same lensing gives 0.89 Chandra vs 0.76 XMM, arXiv:2402.04006).
- Confidence: high.

**Found in:** `cosmo-clusters/SKILL.md` L24, L28–29; `references/results.md` L14, L37–38, L42, L93–95, L107–109, L161–162, L183, L225–232.

**Navigation:** right file at first try; SKILL.md gives the five S8 values, `results.md` the (1 − b).

---

## Q9. CMB lensing tomography

**Answer.**
- unWISE (blue + green) × ACT DR6: S8 = 0.813 ± 0.021; × ACT DR6 + Planck: S8 = 0.810 ± 0.015, "fully consistent" with the primary CMB — Farren et al. 2023, arXiv:2309.05659. (3×2pt with lensing auto, arXiv:2409.02109: 0.816 ± 0.015.) Supersedes 0.784 ± 0.015 (unWISE × Planck, arXiv:2105.03421, 2.4σ low).
- DESI LRG (4 photo-z bins, HEFT) × Planck PR4: 0.765 ± 0.023; × ACT DR6: 0.790 +0.024/−0.027; × ACT DR6 + Planck PR4: S8 = 0.775 +0.019/−0.022 (1.6–2.2σ low) — Sailer et al. 2024, arXiv:2407.04607; companion S8^× = 0.776 +0.019/−0.021 (arXiv:2407.04606). Supersedes 0.73 ± 0.03 (arXiv:2111.09898).
- Why both rose (~1σ):
  - unWISE (appendix of arXiv:2309.05659, Planck-only reanalysis): Monte Carlo lensing-normalisation correction +0.6σ, additional spectroscopic data for dN/dz +0.8σ (mostly the Blue sample), galaxy systematics weighting +0.4σ, PR4 instead of PR3 +0.2σ, modelling −0.5σ, PCA dN/dz marginalisation −0.2σ; total +1.3σ with ~15 % wider posteriors.
  - DESI LRG (arXiv:2407.04607, "Planck PR3 reanalysis"): consistent neutrino masses in the emulator ΔS8 = +0.017, Monte Carlo normalisation of the PR3 cross-correlation +0.015, informative prior tying two counterterms (removes a prior-volume/projection effect) +0.014, updated LRG sample −0.012; the 2021 mean (0.725 ± 0.030) sat ~1σ below its own best fit (0.751).
- Confidence: high.

**Found in:** `cosmo-cmb-lss-cross-correlations/SKILL.md` L24–26; `references/results.md` L16–29, L254–255, L258; `references/open-questions.md` L13–17.

**Navigation:** right file at first try (`results.md` §1.1 and §7.1).

---

## Q10. kSZ with DESI DR2 and ACT DR6

**Answer.**
- Detection significances (DESI DR2 × ACT DR6):
  - Velocity-weighted stacking, 2.4 million spectroscopic LRGs: 18σ, S/N ≈ 5–10 in each of four redshift bins — Qu et al. 2026, arXiv:2604.19744; BGS up to ~9, ELG ~7.5 — Hadzhiyska et al. 2026, arXiv:2604.19745.
  - Spectroscopic velocity reconstruction: v–g 17.0σ (LRG), 8.3σ (ELG), 6.8σ (QSO); first v–v auto-spectrum 3.1σ (LRG); cumulative 20.8σ — Chaussidon et al. 2026, arXiv:2604.04867.
  - Pairwise with machine-learning velocities: SNR 14.2 / 15.1 on the optical depth (Gong et al. 2026, arXiv:2609.36355); lensing/kSZ gas-fraction ratio SNR 17.2 (BGS), 13.8 (LRG bin 1) (Liu et al. 2026, arXiv:2609.22466).
- Velocity bias (ratio to a fiducial gas-plus-HOD P_ge): DR2 LRG joint v–g + v–v fit b_v = 0.229 ± 0.022 (90 GHz), 0.233 ± 0.020 (150 GHz) — arXiv:2604.04867; quoted as 0.23 ± 0.02 in SKILL.md. For comparison 0.33 ± 0.03 (ACT DR6 × DESI Legacy LRG, arXiv:2511.15701), A = 0.39 ± 0.04 (arXiv:2506.21684). kSZ measures τ × v: no fσ8, output is f_NL = 15.9 +34.6/−34.4.
- Feedback debate:
  - Strong: DR2 LRG stack favours "feedback efficiencies exceeding those in the Battaglia profile" (arXiv:2604.19744); fiducial simulations disfavoured at > 3σ (arXiv:2510.15822); kSZ > 8σ from fiducial FLAMINGO, eROSITA gas fractions 2× lower (arXiv:2509.10455); 10 ± 2 % matter-power suppression at k = 1 h/Mpc (arXiv:2512.02954); gas fractions ≳ 4σ below TNG300 (arXiv:2507.14136).
  - Not strong / caution: DES Y3 + Planck PR4 6×2pt with gas-fraction prior finds weak feedback (arXiv:2510.25596); model-independent lensing/kSZ ratio on DESI DR2 × ACT DR6 × HSC Y3 is "most closely tracked" by *fiducial* FLAMINGO (arXiv:2609.22466), contradicting the > 8σ; non-linear velocity terms bias stacks by 10–20 % (arXiv:2607.23339); Y1 preference "tentative" with a free amplitude, TNG PTE = 0.045 (arXiv:2503.19870); HSC-XXL gas fractions give 5 ± 4 % suppression; stronger feedback worsens X-ray group gas fractions (arXiv:2410.19905).
- Confidence: high.

**Found in:** `cosmo-cmb-lss-cross-correlations/SKILL.md` L29–31; `references/results.md` L105, L111–112, L120, L134–135, L140–144, L262; `references/open-questions.md` L57–99, L250–255.

**Navigation:** right files at first try, but two were needed and both are signposted (`results.md` for numbers, `open-questions.md` "feedback strength" for the two sides).

**NOT IN SKILL:** b_v for DESI DR2 ELGs and quasars (declared "not read" in `results.md` L277 and `open-questions.md` L284).

**CONFLICT:** range of b_v.
- `cosmo-peculiar-velocities/SKILL.md` L55: "b_v ≈ 0.2–0.45".
- `cosmo-peculiar-velocities/references/open-questions.md` L243: "b_v ≈ 0.3–0.45".
- `cosmo-cmb-lss-cross-correlations/references/open-questions.md` L250–255: 0.23–0.39 read at source, and states that the PV SKILL.md says "0.3–0.45" (no longer what that SKILL.md says).
- The 0.45 +0.06/−0.05 value (arXiv:2506.21657, `cosmo-peculiar-velocities/references/results.md` L217, L242) is absent from the cross-correlation skill; the DR2 values 0.229/0.233 are absent from the PV reference files.

---

## Q11. Beyond two-point clustering

**Answer.**
- Parity-odd 4PCF, BOSS: 7.1σ (CMASS), 3.1σ (LOWZ) against Patchy mocks (arXiv:2206.03625); blind rank test 2.9σ (arXiv:2206.04227); 1.4σ with GLAM-Uchuu N-body mocks (arXiv:2401.09523); cross statistics 0–2.5σ with a parity-even 8PCF term ≈ 6σ (arXiv:2407.03397); inflationary templates all < 2σ (arXiv:2210.16320).
- DESI DR1 LRG: auto 4–10σ excess over mocks; cross between patches: no detection, in tension with the auto result (arXiv:2508.09133); kurto spectra: no evidence in BOSS DR12 or DESI DR1 (arXiv:2604.06021). Status: "no evidence for parity violation", no accepted detection.
- DESI bispectrum and w0wa (DESI DR1 P + LRG bispectrum + DR2 BAO, Forero-Sánchez et al. 2026, arXiv:2606.23936, June 2026): it weakens the preference relative to power-spectrum-only analyses — DESI alone within 1σ of Λ (P-only FS + DR2 BAO: 1.4σ, arXiv:2602.18761); 2.8σ with CMB; 1.6σ with DES-Dovekie only; 3.1σ with CMB + DES-Dovekie, "driven primarily by the CMB". It raises σ8 by 1.1σ (errors −26 %).
- Reference void–galaxy AP/RSD constraint: Ω_m = 0.337 +0.026/−0.029 (voids only, flat ΛCDM; SDSS MGS + BOSS + eBOSS, 0.07 < z < 1.0, six bins; arXiv:2205.06258); with galaxy clustering 0.356 ± 0.024 (Woodfinden et al. 2023, arXiv:2303.06143). No DESI void–galaxy cosmology exists; finder AP response and velocity-profile mismatch were quantified afterwards (arXiv:2407.02699, arXiv:2206.14120).
- Confidence: high.

**Found in:** `cosmo-beyond-two-point/SKILL.md` L24–27; `references/results.md` L17, L48–49, L87–100, L142–143, L175–182; `cosmo-dark-energy-modified-gravity/references/results.md` L145–154 and `references/open-questions.md` L74–76.

**Navigation:** right file at first try; SKILL.md alone answers the three parts.

**NOT IN SKILL:** the power-spectrum-only significances of the same pipeline with CMB and with CMB + Dovekie (the baselines that 2.8σ and 3.1σ are compared with); only the DESI-only pair (1.4σ → within 1σ) is given. The author of arXiv:2205.06258 is not named in the files read.

---

## Q12. Field-level and simulation-based inference

**Answer.**

Produced cosmological parameters from survey data:
- Gaussian field-level likelihood (the method flip implements), DESI DR1 peculiar velocities + BGS: fσ8 = 0.483 (+0.080/−0.043 stat ± 0.018 sys, from the hub table), z_eff = 0.07 — Lai et al. 2025, arXiv:2512.03229; one of three estimators entering the consensus 0.4497 ± 0.0548.
- Neural field-level (SimBIG CNN, ~10 % of BOSS CMASS, flat ΛCDM, k_max = 0.5 h/Mpc): Ω_m = 0.267 +0.033/−0.029, σ8 = 0.762 +0.036/−0.035, H0 = 64.5 ± 3.8; σ8 2.65× tighter than P_ℓ — arXiv:2310.15256.
- SimBIG SBI of summaries (same subsample): bispectrum monopole Ω_m = 0.293 ± 0.027, σ8 = 0.783 +0.040/−0.038, S8 = 0.774 +0.056/−0.053, H0 = 67.6 +2.2/−1.8 with BBN (arXiv:2310.15243, robust); marked power spectrum Ω_m = 0.273 +0.040/−0.030, σ8 = 0.777 +0.077/−0.071 (arXiv:2404.04228); wavelet scattering transform not robust in σ8 (arXiv:2310.15250).
- Neural BAO reconstruction (LiFT) on DESI DR1 LRG: α_iso errors smaller by 13/24/30 %, α_AP by 5/22/30 % in LRG1/2/3, central values consistent with DR1 and DR2 (arXiv:2609.14862) — distance-scale parameters, external group.
- Map-level SBI in weak lensing, DES Y3: hybrid statistics S8 = 0.808 ± 0.017, Ω_m = 0.325 ± 0.024 (wCDM, arXiv:2606.11309); power spectrum + CNN S8 = 0.804 +0.025/−0.017, Ω_m = 0.283 +0.020/−0.027 (wCDM, arXiv:2403.02314; "w < −0.80" is prior-bounded); moments + wavelet phase harmonics + scattering 0.794 ± 0.017 (ΛCDM) / 0.817 ± 0.021 (wCDM) (arXiv:2405.10881); Betti numbers 0.821 ± 0.018 (arXiv:2506.13439); HSC Y1 SBI 0.804 +0.041/−0.040 (arXiv:2409.01301).

Reconstructed fields only (no parameter):
- BORG-type sampled initial conditions: 2M++ density and velocity fields (arXiv:1806.11117); Manticore-Local on 2M++ (arXiv:2505.10682); BOSS (arXiv:1909.06396); Quaia, cross-correlation with Planck lensing at ~4σ (arXiv:2602.02363). "None of these quotes a cosmological parameter."

Simulation tests or forecasts only:
- LEFTfield field level vs SBI P + B on halos: σ8 error factor 3.5–5.2 better (arXiv:2403.03220); equivalence with P + B (+T) under an analytic likelihood (arXiv:2507.05378, arXiv:2509.09673); DESI-LRG-like snapshots (arXiv:2609.16719); toy model (arXiv:2606.18227); BORG f_NL on Quijote halos, factor ~1.3 (arXiv:2603.20855); Beyond-2pt challenge (field level only in real space with σ8 free, arXiv:2405.02252).
- flip forecast: σ(fσ8) = +0.047/−0.048 (10 %) for simulated ZTF 6-year SNe + DESI DR3 BGS (arXiv:2609.34508); Fisher forecast accuracy (arXiv:2501.16852). No fσ8 from ZTF data; no field-level or SBI cosmology from DESI galaxy clustering.
- Confidence: high.

**Found in:** `cosmo-beyond-two-point/SKILL.md` L33–37; `references/results.md` L30–33, L234–239, L272–288, L294–295, L301–306, L315–319; `references/open-questions.md` L195–202, L256, L267–269; `cosmo-peculiar-velocities/references/results.md` L57–58 and `SKILL.md` L53–54; hub pointer `observational-cosmology/references/fsigma8-pv-compilation.md` L117 for the error bars of 0.483.

**Navigation:** right file at first try (`results.md` §0 status table, then §5–§6). The flip data value is not in this skill: it sends to `cosmo-peculiar-velocities`, which in turn sends to the hub for the error bars (two hops).

**NOT IN SKILL:** the fσ8 value of the field-level DESI DR1 fit inside `cosmo-beyond-two-point` (pointer only); central α values of LiFT; parameter values of the SimBIG power-spectrum baseline (arXiv:2211.00660).

---

## Consolidated lists

### NOT IN SKILL
1. Q1/Q12 — uncertainties of the three DESI DR1 PV estimators (0.391, 0.440, 0.483): absent from `cosmo-peculiar-velocities`, present only in the hub files it points to.
2. Q2 — origin and depth of the "4.8σ" first-quoted significance of the CF4 flow: the skill gives probabilities (0.023 %, 0.00021 %) and names "4.8σ" only as a stale claim; "4.81σ at 200 h⁻¹Mpc" is only in the hub.
3. Q4 — numerical GR prediction for the latest (2026, arXiv:2604.24631) E_G values; table says "consistent".
4. Q10 — b_v for DESI DR2 ELGs and quasars (declared not read).
5. Q11 — power-spectrum-only w0wa significances with CMB (and CMB + Dovekie) from the same pipeline as arXiv:2606.23936; first author of arXiv:2205.06258.
6. Q12 — field-level fσ8 value inside `cosmo-beyond-two-point` (pointer to sibling only); LiFT central values; SimBIG P_ℓ baseline parameter values.

### CONFLICT
1. b_v range: `cosmo-peculiar-velocities/SKILL.md` L55 "0.2–0.45"; `cosmo-peculiar-velocities/references/open-questions.md` L243 "0.3–0.45"; `cosmo-cmb-lss-cross-correlations/references/open-questions.md` L250–255 "0.23–0.39", which also misquotes the PV SKILL.md as saying 0.3–0.45. The 0.45 value (arXiv:2506.21657) is not in the cross-correlation skill; the DR2 0.229/0.233 values are not in the PV reference files.
2. E_G at z = 0.555 / 0.316: 0.36 +0.06/−0.05 and 0.40 +0.11/−0.09 (`cosmo-dark-energy-modified-gravity/references/results.md` L311–312, arXiv:2401.12971) vs 0.31 +0.06/−0.05 or 0.34 ± 0.05 and 0.49 +0.14/−0.11 or 0.43 +0.11/−0.09 (`cosmo-cmb-lss-cross-correlations/references/results.md` L80–81, arXiv:2405.12795). Different papers; each skill ignores the other's.
3. DESI DR1 TF clustering sample: 6 807 (`cosmo-peculiar-velocities/references/results.md` L28, `surveys-and-data.md` L69) vs 6 806 (`surveys-and-data.md` L79, `systematics.md` L158).
4. Paper credited with the DESI DR1 PV consensus: 2512.03228 + 2512.03230 (`cosmo-peculiar-velocities/SKILL.md` L30), 2512.03230 (`results.md` L32), 2512.03230 + 2512.03231 (hub `fsigma8-pv-compilation.md` L120).
5. Documented two-value cases (flagged by the skills themselves): DESI DR2 + CMB + DES-Dovekie 3.2σ vs 3.4σ (`cosmo-dark-energy-modified-gravity/references/results.md` L117–130); P-ACT-LB Σm_ν 0.089 eV (text) vs 0.082 eV (abstract) (`cosmo-neutrinos-dark-matter/references/results.md` L41); DESI DR1 + CMB Σm_ν 0.070 / 0.072 / 0.077 eV (same file L33, L34, L45, L305).

### Navigation failures
No question sent me to a wrong file at the first try. Frictions:
1. Q1 — `cosmo-peculiar-velocities` holds the three central values but not their error bars; `results.md` defers to the hub table, so the skill is not self-sufficient for its own headline measurement.
2. Q2 — "4.8σ" is used in SKILL.md "Errors that recur" without the reference files ever stating where it comes from.
3. Q4 — SKILL.md presents the 2024 E_G as the current value while `results.md` §8 lists 2026 measurements; a SKILL.md-only reader answers "latest" with a stale number.
4. Q10 — two files needed (`results.md` + `open-questions.md`), both correctly signposted; the sibling-disagreement note in `open-questions.md` §11 is out of date with the PV SKILL.md.
5. Q12 — the flip data result takes two hops (beyond-two-point → peculiar-velocities → hub).
