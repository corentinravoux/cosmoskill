# GREEN test — wave 3 and 4 skills — 2026-10-12

Rules: every answer below comes only from the files of the nine skill directories (cosmo-inflation-primordial, cosmo-statistics-inference, cosmo-simulations-mocks, cosmo-surveys-facilities, cosmo-tensions-anomalies, cosmo-reionization-21cm, cosmo-multimessenger, cosmo-theory-foundations, cosmo-software-ecosystem) under `<skills>/`, with no web, no arXiv tools, no other files, no answer from memory and no reading of `baseline-wave34.md`; the one exception used is an explicit by-name pointer to another cosmo-* skill for a value, followed twice (both to `cosmo-cmb`) and flagged where used.

Method: for each question, SKILL.md of the chosen skill was read first, its file map used to pick the reference file, the passage located by grep and then read. Paths are relative to `claude/skills/`. Flags `[src]`, `[sec]`, `[der]` are the skills' own provenance flags. All arXiv IDs are copied from the skill files and were not checked against arXiv.

---

## 1. Spectral index and tensors

**n_s by CMB data combination** (68%, flat ΛCDM, power law, pivot 0.05 Mpc⁻¹):

| n_s | Data | arXiv |
|---|---|---|
| 0.9649 ± 0.0042 | Planck 2018 (Plik PR3) T + P + lensing | 1807.06211 |
| 0.9709 ± 0.0038 | P-ACT (ACT DR6 + Planck PR3 cut at ℓ < 1000 TT, ℓ < 600 TE/EE) | 2503.14452 |
| 0.974 ± 0.003 (four-digit form 0.9743 ± 0.0034) | P-ACT-LB (P-ACT + CMB lensing + DESI DR1 BAO) | 2503.14452 |
| 0.9679 ± 0.0033 (v2; v1 gave 0.9684 ± 0.0030) | CMB-SPA (SPT-3G D1 + ACT DR6 + Planck) | 2506.20707 |
| 0.951 ± 0.011 | SPT-3G D1 alone | 2506.20707 |

In extended models: 0.9758 ± 0.0064 (Planck + ACT + SPT + DESI DR2, ΛCDM + α_s + N_eff + Σm_ν; arXiv:2609.35964); 0.9667–0.9716 with Ω_K and/or w0wa free (arXiv:2607.28445). The skill's reading: the high 0.974 belongs to CMB + DESI BAO in ΛCDM, not to the CMB alone.

**Latest limit on r**: r_0.05 < 0.036 at 95%, σ(r) = 0.009, BICEP/Keck BK18 (data to 2018, with WMAP and Planck maps), arXiv:2110.00483, dated 2021. The tighter-looking r < 0.032 (BK18 + Planck PR4 + BAO, arXiv:2112.07961) and r < 0.038 (P-ACT-LB + BK18, arXiv:2503.14454) reuse the same B-mode data.

**Newer B-mode result?** No newer BICEP/Keck r limit exists at the snapshot (search of 2026-10-09); a "BK24" release (data 2016–2024) is in preparation, undated (arXiv:2608.25016). One later, independent B-mode limit exists and is not competitive: SPT-3G 2019–2020, r < 0.25, σ(r) = 0.067 (arXiv:2505.02827, 2025). The causal-source limit r_ect < 0.0077 (arXiv:2601.20958) is a different parameter.

Confidence: high (all rows `[src]`).

Found in: `cosmo-inflation-primordial/references/results.md` lines 13–33 (n_s), 72–94 (r); `SKILL.md` lines 24–28; `references/open-questions.md` line 31; `references/surveys-and-data.md` lines 24, 151, 165 (BK24).

Pointer followed: `results.md` line 33 says PR4 n_s values "are in `cosmo-cmb`". Followed: `cosmo-cmb/references/results.md` lines 113–126 give Planck PR4 HiLLiPoP + LoLLiPoP n_s = 0.9681 ± 0.0039, and 0.9690 ± 0.0035 with lensing and BAO (arXiv:2309.10034).

Navigation: SKILL.md sent to `results.md` at the first try.

CONFLICT: see consolidated item C3 (wording "latest B-mode measurement").

---

## 2. Primordial non-Gaussianity

**Planck f_NL** (68%):

| | local | equilateral | orthogonal | Source |
|---|---|---|---|---|
| Planck 2018 (PR3), T + E, collaboration reference | −0.9 ± 5.1 | −26 ± 47 | −38 ± 24 | arXiv:1905.05697 |
| Planck PR4 (NPIPE), T + E, binned estimator, latest (2025) | −0.1 ± 5.0 | 6 ± 46 | −8 ± 21 | Jung et al. 2025, arXiv:2504.00884 |

The PR4 result is a five-author reanalysis, not a collaboration product; the 2018 values remain the reference. Both are after subtraction of the lensing–ISW bispectrum.

**DESI f_NL from scale-dependent bias**: f_NL^local = −3.6 (+9.0/−9.1), DESI DR1, 1,631,716 LRGs (0.6 < z < 1.1) and 1,189,129 QSOs (0.8 < z < 3.1), blinded (Chaussidon et al. 2024, arXiv:2411.17623). Assumption: the measured quantity is f_NL · b_φ with b_φ = 2 δ_c (b_1 − p); the quoted value takes p = 1 (universal mass function) for LRGs and p = 1.6 (recent mergers) for quasars. With p = 1 for both the value is 3.5 (+10.7/−7.4). Later DR1 reanalyses: −3.3 ± 9.2 (p̄ ≈ 1.4 simulation prior, arXiv:2602.12357), 2.1 (+8.8/−8.3) (auto + cross, arXiv:2604.05213), −3 ± 12 (configuration space, arXiv:2606.24651). No DESI DR2 f_NL was found by the skill's search of 2026-10-09.

Confidence: high.

Found in: `cosmo-inflation-primordial/references/results.md` lines 106–119 (CMB), 130–148 (LSS); `SKILL.md` lines 30–31.

Navigation: right file at the first try.

---

## 3. Cosmic birefringence

Latest joint measurement: β = 0.277° ± 0.057° (68%), ACT DR6 + Planck PR4 maps including cross-spectra between the two telescopes, instrumental priors taken at face value; Eskilt 2026, arXiv:2608.06480. Significance of β ≠ 0: 4.8σ (3.5σ in the dust-robust variant). Authors' conclusion: no detection claimed — "unresolved systematics in the data must be understood before we can draw strong cosmological conclusions"; the 4.8σ is conditional on the ACT instrumental priors, and β = 0 would need both the dust EB model and the instrumental priors to fail together.

Inputs: 0.342° (+0.094/−0.091), 3.6σ, WMAP + Planck PR4 (arXiv:2205.13962); 0.215° ± 0.074°, 2.9σ, ACT DR6 (arXiv:2509.13654).

Confidence: high.

Found in: `cosmo-inflation-primordial/references/results.md` lines 279–292; `SKILL.md` line 36.

Navigation: right file at the first try.

---

## 4. Evolving dark energy, DESI DR2 + CMB alone

- Frequentist: Δχ²_MAP = −12.5 (w0waCDM minus ΛCDM), converted with 2 extra degrees of freedom to 3.1σ; companion Δ(DIC) = −8.7. DESI Collaboration 2025, arXiv:2503.14738, §7.1. (Without CMB lensing: −9.7, 2.7σ; with a compressed CMB prior: −8.0, 2.4σ.)
- Bayes factor, independent analysis: ln B = −0.57 ± 0.26 for w0waCDM against ΛCDM on DESI DR2 BAO + Planck CMB, nested sampling (PolyChord), mildly favouring ΛCDM; Ong, Yallup & Handley 2025, arXiv:2511.10631 (extended in arXiv:2603.05472).
- Why they disagree: neither is an error; they answer different questions. Δχ² compares best fits and ignores the prior volume of w0, wa; the evidence is the likelihood averaged over the prior, so it scales inversely with the prior volume of the two extra parameters (Ockham factor). In addition, where the evidence does favour w0wa (with the original DES-SN5YR, ln B = +3.32 ± 0.27) the same paper traces it to a 2.95 ± 0.04σ ΛCDM tension between DESI DR2 and that supernova sample, falling to ln B = −0.30 ± 0.19 with DES-Dovekie.

Confidence: high.

Found in: `cosmo-statistics-inference/references/results.md` lines 111–128 (Δχ² table), 132–142 (evidence); `references/systematics.md` lines 94–96 (prior-volume mechanism); `references/open-questions.md` lines 24–26; `SKILL.md` line 29. Same numbers, flagged `[sec: stat]`, in `cosmo-tensions-anomalies/references/results.md` lines 224–235 and `SKILL.md` line 29.

Navigation: right skill and file at the first try (file-map row "Δχ² against evidence" → `results.md`). The mechanism behind the disagreement is in `systematics.md` §7, a second file; `results.md` line 142 gives it in one sentence only.

---

## 5. Covariance from mocks, 1000 mocks

- 100 data points: parameter error bar × 1.100, i.e. +10%.
- 400 data points: × 1.647, i.e. +65%.

Both are `[der]`: computed in the skill for n_θ = 10 fitted parameters, Gaussian data and independent mocks, from the formulae of arXiv:2108.10402 and arXiv:1312.4841; they are the factor by which a naive error (Gaussian likelihood with uncorrected S⁻¹) must be multiplied. Decomposition: Hartlap factor on the covariance 1.113 and 1.671; Dodelson–Schneider variance factor 1.100 and 1.653; S'/S variance factor 1.209 and 2.712.

Corrections involved:
1. Hartlap factor, h = (n_s − 1)/(n_s − n_d − 2): unbiased precision matrix only (Hartlap, Simon & Schneider 2007, arXiv:astro-ph/0608064).
2. Dodelson–Schneider: scatter of the best fit, V = [1 + B(n_d − n_θ)] F⁻¹, B = (n_s − n_d − 2)/[(n_s − n_d − 1)(n_s − n_d − 4)] (arXiv:1304.2593).
3. Percival et al. 2014 factor m_1 = [1 + B(n_d − n_θ)]/[1 + A + B(n_θ + 1)] on the measured parameter covariance (arXiv:1312.4841).
4. Percival, Friedrich, Sellentin & Heavens 2022: t-distribution posterior with matching prior, S'/S = (n_s − 1)[1 + B(n_d − n_θ)]/(n_s − n_d + n_θ − 1), no Hartlap factor applied (arXiv:2108.10402). The Sellentin–Heavens t-distribution (arXiv:1511.05969) is the alternative likelihood and does not contain the Dodelson–Schneider term.

Confidence: high for the sizes as derived quantities; they are not numbers printed in a paper.

Found in: `cosmo-statistics-inference/references/results.md` lines 12–28; `references/physics-and-methods.md` lines 28–44; `SKILL.md` line 24. Repeated as `[sec]` in `cosmo-simulations-mocks/references/results.md` lines 61 and 104.

Navigation: right file at the first try; the formulae behind the table are in `physics-and-methods.md` §2.1, to which `results.md` line 12 points.

NOT IN SKILL: the constant A of the Percival 2014 m_1 factor ("not transcribed", `physics-and-methods.md` lines 36 and 374).

---

## 6. Simulation accuracy

- N-body code agreement on P(k): within 1% at k ≤ 1 h/Mpc and within 3% at k ≤ 10 h/Mpc for RAMSES, PKDGRAV3, GADGET-3 on one set of initial conditions at standard run parameters (Schneider et al. 2015, arXiv:1503.05920). 1% to k = 10 h/Mpc only with tuned settings: Abacus, GADGET, SWIFT (arXiv:2112.09138); GINKAKU against GADGET, PKDGRAV3, RAMSES (arXiv:2605.28581).
- COLA with 40 steps (ICE-COLA, 40 linearly spaced steps from z_i about 20, force mesh three times the particle grid): matter P(k) to 1% for k ≲ 1 h/Mpc at 0 < z < 1; halo mass function 5% for M > 10^12.5 M_⊙/h; halo bias 2% to k ≲ 0.7 h/Mpc; redshift-space halo multipoles 4% to k ≲ 0.4 h/Mpc (arXiv:1509.04685).
- Baryonic suppression at k = 1 h/Mpc from data: 10 ± 2%, eROSITA gas fractions + SDSS/DESI × ACT kSZ with baryonification, 0 < z < 1 (Siegel et al. 2025, arXiv:2512.02954); the older X-ray sample (HSC-XXL gas fractions alone) gives 5 ± 4%. Disputed: fiducial FLAMINGO is more than 8σ off in one analysis (arXiv:2509.10455) and tracks the data in another (arXiv:2609.22466).

Confidence: high.

Found in: `cosmo-simulations-mocks/references/results.md` lines 10–18, 46–50, 75–76, 84–87; `references/physics-and-methods.md` line 111; `SKILL.md` lines 24, 28, 30.

Navigation: right file at the first try.

---

## 7. Constrained simulations of the local Universe

- Latest 2M++-based reconstruction: Manticore-Local (BORG with a non-linear solver, refined bias model, physics-informed priors; McAlpine et al. 2025, arXiv:2505.10682). It finds "no evidence for a large local underdensity"; counterparts of 14 clusters within 1° at 2–4σ. Contrast: SIBELIUS-DARK finds an underdensity of about 5% within 200 Mpc (arXiv:2202.04099); the two are not reconciled in the abstracts read.
- Extension to the SDSS and BOSS volumes: Manticore-Deep (five galaxy redshift surveys, tiled BORG inference; McAlpine et al. 2026, arXiv:2606.10020): (4 Gpc/h)³ to z about 0.7 at a resolution of about 4 Mpc/h. Validation: CMB-lensing cross-correlation at 7.4σ (Planck PR3); kSZ from 64,750 clusters at 3.5σ.

Confidence: high (`[src]`, from abstracts).

Found in: `cosmo-simulations-mocks/references/results.md` lines 131–136, 142; `references/surveys-and-data.md` lines 92, 94–95; `references/open-questions.md` lines 49–52; `SKILL.md` line 36.

Navigation: right at the first try; the file map lists "constrained projects" under `surveys-and-data.md` and the same facts are duplicated in `results.md` §7, so either file answers.

---

## 8. Facilities

**Euclid, public releases**: Early Release Observations, 23 May 2024; Quick Data Release 1 (Q1, 63.1 deg² of the deep fields), 19 March 2025; Quick Data Release 2 (Q2, Galactic bulge), 24 June 2026. No cosmology product is public.

**Euclid, planned (all "tentative", ESA timeline)**: DR1-Foundation 12 November 2026 (images, catalogues, spectra over about 1900 deg²); DR1 with clustering and lensing products mid 2027; Q3 2028; DR2 June 2029; Q4 2030; DR3 October 2031.

**Latest public DESI spectra**: DR1, public 19 March 2025, 18.7 million spectra (observations May 2021 to June 2022), at `data.desi.lbl.gov/public/dr1` (arXiv:2503.14745). DR2 (6 October 2025) is BAO likelihoods and chains only; DR2 spectra and LSS catalogues are not public.

**eROSITA-DE DR2** (news item of 31 July 2026; Ramos-Ceja et al. 2026, arXiv:2607.27772): catalogue-only release of the cumulative first three all-sky surveys (eRASS:3, 12 December 2019 to 16 June 2021) for the German (western Galactic) half: 1,911,744 point-like and 63,796 extended sources in 0.2–2.3 keV. No event files after eRASS1; eight passes were planned.

Confidence: high for dates read at source (`[src]`); the ERO date and Q1 contents are `[sec: GC]`.

Found in: `cosmo-surveys-facilities/references/results.md` lines 65, 77–78, 84, 100, 106 (chronology), 117, 120, 135 (public today), 146, 154, 158, 161–162 (upcoming), 171–181; `references/surveys-and-data.md` lines 212 and 216–219 (Euclid row 2.10), 263–277 (eROSITA); `SKILL.md` lines 24–29, 41–42.

Navigation: `results.md` at the first try for all three; the DR2 source counts needed `surveys-and-data.md` §6. One broken cross-reference: `surveys-and-data.md` line 159 (Euclid NISP) says "Releases and calendar: Sect. 2.7", but row 2.7 is UNIONS; the Euclid releases are in row 2.10 (line 212).

CONFLICT (documented in the file, external sources): Euclid DR2 is June 2029 on the ESA timeline and March 2029 at IPAC (`results.md` line 161). eROSITA survey start: 13 December 2019 in arXiv:2010.03477, 12 December on the DR2 page (`results.md` line 39).

---

## 9. Cosmic dipole

- CatWISE quasar number-count dipole as first quoted: amplitude "over twice as large as expected", p = 5 × 10⁻⁷, 4.9σ one-sided, 1.36 million CatWISE2020 quasars, null = purely kinematic dipole with the CMB velocity (Secrest et al. 2021, arXiv:2009.14826). Later Bayesian analyses: 5.7σ (arXiv:2212.07733); 6.7σ with a forward-modelled Eddington bias (arXiv:2607.25703).
- With clustering-aware mocks (lognormal mocks with clustering, radial selection, exact sky coverage): 3.63σ without a clustering dipole, 3.44σ with a randomly oriented one, 3.27σ with one aligned with the kinematic dipole (Bashir, Chingangbam & Appleby 2025, arXiv:2511.00822).
- DESI redshift dipole: v = 357.95 (+55.05/−48.47) km/s from quasars in DESI DR1 (BGS, LRG, ELG, QSO, 0.1 < z < 2.1; 1,000 EZmocks), against 369.82 ± 0.11 km/s from the CMB, i.e. consistent; the number-count dipole of the same catalogues is "significantly enhanced", attributed to leakage of large-scale power and footprint incompleteness (Wu & Xia 2026, arXiv:2608.30914).

Confidence: high (`[src]`, abstracts read 2026-10-10).

Found in: `cosmo-tensions-anomalies/references/results.md` lines 275, 277, 281–282, 291, 300–302; `SKILL.md` line 31.

Navigation: right file at the first try.

---

## 10. Anomalies and the Hubble tension

- Large-angle CMB anomalies, joint claim: four statistics (S_1/2, R^TT, σ²_16, S_QO) jointly, probability "likely ≤ 3 × 10⁻⁸" in Planck temperature, described by the skill as a claimed joint 5σ (Jones et al. 2023, arXiv:2310.12859).
- Reassessment: after a look-elsewhere correction, 3σ if the four were picked from 16 tests and 2σ if from 50, with the measured correlation among the four (10 and 27 tests if uncorrelated); two of the four do not test statistical anisotropy (Guth & Namjoo 2026, arXiv:2602.10178). Nothing is seen in polarisation (arXiv:1906.02552).
- Hubble tension by early endpoint (Gaussian differences, `[der]` in the source skill):

| Local value | vs Planck 2018 (67.4 ± 0.5) | vs SPT-3G D1 (66.66 ± 0.60) | vs CMB-SPA (67.19 ± 0.38) | vs DESI DR2 + BBN (68.51 ± 0.58) |
|---|---|---|---|---|
| SH0ES 2025, 73.18 ± 0.88 (arXiv:2509.01667) | 5.7 | 6.1 | 6.2 | 4.4 |
| H0DN 2025, 73.50 ± 0.81 (arXiv:2510.23823) | 6.4 | 6.8 | 7.1 | 5.0 |
| CCHP TRGB, 70.39 ± 1.94 (arXiv:2408.06153) | 1.5 | 1.8 | 1.6 | 0.9 |

  Range: 4.4σ to 7.1σ for SH0ES and H0DN; 0.9σ to 1.8σ for CCHP. Lowest with DESI DR2 BAO + BBN, highest with CMB-SPA. Early-side sources: arXiv:1807.06209, arXiv:2506.20707, arXiv:2503.14738.

Confidence: high for the anomaly numbers (`[src]`); medium for the tension table (`[sec: h0]`, itself `[der]`).

Found in: `cosmo-tensions-anomalies/references/results.md` lines 331–332, 336–338 (anomalies), 15, 37–48, 54–64 (H0); `SKILL.md` lines 24–25, 32.

Navigation: right file at the first try.

---

## 11. Reionisation and 21 cm

- τ from Planck low-ℓ polarisation: 0.054–0.063, σ ≈ 0.006–0.007. Rows: 0.054 ± 0.007 (Planck 2018, arXiv:1807.06209); 0.0566 (+0.0053/−0.0062) (SRoll2 large-scale polarisation only, arXiv:1908.09856); 0.059 ± 0.006 (SRoll2 + TT + high-ℓ, arXiv:1908.09856); 0.0627 (+0.0050/−0.0058) (SRoll2 momento + CamSpec, arXiv:2103.14378). Model: flat ΛCDM, tanh reionisation. 0.090 ± 0.012 (arXiv:2504.16932) is not a measurement.
- HI intensity-mapping auto-spectrum detections: CHIME, 12.5σ, z = 1.01–1.34 (sub-bands 8.7σ at z ~ 1.08, 9.2σ at z ~ 1.24), 0.4 < k < 1.5 h/Mpc, 94 nights (CHIME Collaboration 2025, arXiv:2511.19620); MeerKLASS, S/N 6.2 at z = 0.42, 10³ Ω_HI b_HI = 1.271 (+1.080/−0.598), 0.095 < k < 0.245 h/Mpc, from cross-spectra of independent subsets, posted 2026-10-08 (arXiv:2610.12158). No BAO.
- Deepest 21 cm power-spectrum limits at z > 6 (all 2σ upper limits; no detection): HERA Phase I, Δ² ≤ 457 mK² at z = 7.9, k = 0.34 h/Mpc, 94 nights (arXiv:2210.04912); MWA Gaussian component, (23.0 mK)² EW and (21.7 mK)² = 470 mK² NS at z = 6.5, k = 0.18 h/Mpc, 268 h (arXiv:2508.04164); LOFAR, (54.3 mK)² at z = 9.1, k = 0.076 h/Mpc (arXiv:2503.05576); NenuFAR, 4.6 × 10⁵ mK² at z = 20.3, k = 0.038 h/Mpc (arXiv:2507.10533). The limits are at different k and cannot be ranked by the number alone.

Confidence: high.

Found in: `cosmo-reionization-21cm/references/results.md` lines 13–35 (τ), 159–186 (21 cm limits), 211–240 (HI); `SKILL.md` lines 24, 31–32.

Pointer followed: `results.md` lines 30–31 say `cosmo-cmb` quotes 0.051–0.063 from a PR4 analysis not read for this skill. Followed: `cosmo-cmb/references/results.md` line 228 gives 0.051 ± 0.006 (NPIPE large-scale polarisation, arXiv:2007.04997).

Navigation: right file at the first try.

CONFLICT: see consolidated items C1 (τ range), C2 (CHIME auto-spectrum in the facilities skill), C4 (which MWA number is the headline).

---

## 12. Standard sirens

- Latest LVK H0: 71.7 (+9.4/−7.5) km/s/Mpc (median), GWTC-5.0, 236 sources, flat ΛCDM, combining the mass-spectrum (spectral) method, the DES Y6 galaxy catalogue with luminosity weighting, and the bright siren GW170817; arXiv:2605.27227, May 2026. About 12% `[der]`; consistent with both tension endpoints; driven by mass-spectrum features, not the catalogue. (GWTC-5.0 holds 390 candidates, 267 in the population analysis, 236 in cosmology.)
- GW170817 with jet information: the six values using jet or afterglow information span 64.8 to 75.5, with errors of 4 to 7: 68.9 (+4.7/−4.6) (arXiv:1806.10596), 64.8 (+7.3/−7.2) (arXiv:1909.00587), 68.3 (+4.6/−4.5) (arXiv:1909.08627), 66.2 (+4.4/−4.2) (arXiv:2002.11355), 75.46 (+5.34/−5.39) (arXiv:2305.19914), 65.5 ± 4.4 (arXiv:2605.11437). No single one is "the" result. Without jet information: 70.0 (+12.0/−8.0) (arXiv:1710.05835).
- GLADE+ completeness: complete to d_L = 47 (+4/−2) Mpc in total B-band luminosity; it holds the brightest galaxies giving 90% of B- and K-band luminosity to about 130 Mpc (arXiv:2110.06184).

Confidence: high.

Found in: `cosmo-multimessenger/references/results.md` lines 17–31, 49–54 (GW170817), 72–95 (LVK), 229–250 (history); `references/surveys-and-data.md` lines 36–41 (counts), 77, 87 (GLADE+); `references/systematics.md` line 202; `SKILL.md` lines 26–33, 39.

Navigation: `results.md` at the first try for both H0 items; the GLADE+ value is in `surveys-and-data.md`, as the file map says, so two reference files were needed.

---

## 13. Conventions

- σ8, DESI DR1 full shape against Planck: Planck defines σ8 on total matter (baryons + CDM + massive neutrinos), linear, z = 0, R = 8 h⁻¹Mpc (arXiv:1303.5076, Eq. 9; Planck 2018 σ8 = 0.8111 ± 0.0060, arXiv:1807.06209). DESI DR1 full shape "refer[s] as σ8 to the amplitude of matter fluctuations excluding neutrinos", i.e. the cb field (arXiv:2411.12021, footnote 3; fiducial 0.811355). The two differ by roughly f_ν, about 0.45% in amplitude for Σm_ν = 0.06 eV `[der]`. DESI ShapeFit also quotes fσ_s8, with σ_s8 tied to r_d^fid.
- Limber: the error is O(1/ℓ²) provided the argument is k = (ℓ + 1/2)/χ; with k = ℓ/χ it degrades to O(1/ℓ); with the second-order term, O(1/ℓ⁴) (LoVerde & Afshordi 2008, arXiv:0809.5112).
- Growth index: f ≡ d ln δ/d ln a = Ω_m(a)^γ, from g(a) = exp{∫₀^a d ln a [Ω_m(a)^γ − 1]}, with γ = 0.55 + 0.05[1 + w(z=1)] (0.55 + 0.02[1 + w(z=1)] for w < −1) (Linder 2005, arXiv:astro-ph/0507263, Eqs. 16–18). Accuracy, on the growth factor g: better than 0.05% for Λ with Ω_m between 0.22 and 1; within 0.2% for w = −0.8; 0.25% for a SUGRA-like w0 = −0.82, wa = 0.58. Valid for smooth dark energy in general relativity with scale-independent growth.
- Planck 2018 sound horizon at the drag epoch: r_drag = 147.09 ± 0.26 Mpc (TT,TE,EE+lowE+lensing, base ΛCDM; arXiv:1807.06209, Table 1). For contrast, r_* = 144.43 ± 0.26 Mpc (1.8% smaller).

Confidence: high.

Found in: `cosmo-theory-foundations/references/physics-and-methods.md` lines 150 (σ8), 277–280 (Limber), 111–112 (γ); `references/results.md` lines 50–51 (r_drag), 62–76 (γ accuracy), 89 (σ8 values), 126–128 (Limber order); `references/systematics.md` lines 70, 124; `SKILL.md` lines 27, 30, 32, 36.

Navigation: file map correct; the four sub-questions are spread over `physics-and-methods.md` and `results.md`, and each was found at the first try. SKILL.md line 11 says "Read first" the hub file `observational-cosmology/references/conventions.md`, which is outside the allowed set; it was not read and was not needed.

NOT IN SKILL: Planck 2018 r_drag for any data combination other than TT,TE,EE+lowE+lensing; a Planck 2018 value of z_drag (only DESI's z_d ≈ 1060 and eBOSS's "around 1020" are given, `physics-and-methods.md` line 61).

---

## 14. Codes

- CAMB v2 (Lewis 2026, arXiv:2607.14854): new treatment of the hyperspherical Bessel functions for line-of-sight integration in non-flat models; updated integrators; recalibrated fast recombination model; stabilised PPF dark-energy evolution; improved CMB-lensing accuracy. The defaults changed: unboosted runs now target 10⁻³ pointwise agreement with a boosted reference (median Δχ² ≃ 0.4 on an SO-like proxy); default lensing source range max(kη₀) = 90000 against the v1 historical 10375, with which v1.6.6 is off by 1.5% in TT at ℓ = 3000. Non-flat cost fell by a factor of 17. pyccl 3.3.6 still pins `AccuracyTarget` = 0, the v1 behaviour.
- Successor of EFTCAMB: H-EFTCAMB, "the official successor to EFTCAMB" (Ye et al. 2026, arXiv:2603.01662): adds a module for an arbitrary covariant Horndeski Lagrangian, Python wrapper integrated in Cobaya; the repository `EFTCAMB/EFTCAMB` now carries the H-EFTCAMB README.
- flip units (Ravoux et al. 2025, arXiv:2501.16852; cite also arXiv:2303.01198): k in h Mpc⁻¹; distances in Mpc h⁻¹; RA and Dec in radians; velocities in km/s.

Confidence: high (CAMB and H-EFTCAMB `[src]` from the papers; flip units `[src]` from the flip checkout, `docs/covariance_models.md`).

Found in: `cosmo-software-ecosystem/references/physics-and-methods.md` lines 28–30 (CAMB v2 changes), 47 (H-EFTCAMB); `references/results.md` lines 26–30, 52 (v2 accuracy, timing); `references/open-questions.md` lines 84, 86 (succession); `references/systematics.md` lines 20, 30–31, 95–96 (flip units, pyccl pin); `SKILL.md` lines 26–27, 32, 37.

Navigation: SKILL.md bullets answer all three parts. In the references the CAMB v2 answer is split over three files: the list of algorithmic changes sits in `physics-and-methods.md` §1.2 ("CAMB against CLASS"), which the file map does not signpost for "what changed in a version"; the file-map row for "release" leads to `surveys-and-data.md`, which gives the reference only.

---

## Consolidated lists

### NOT IN SKILL

1. Q5 — the constant A in the Percival et al. 2014 factor m_1 (`cosmo-statistics-inference/references/physics-and-methods.md` lines 36, 374: "not transcribed"). The 10% and 65% figures are derived in the skill for n_θ = 10, not quoted from a paper.
2. Q13 — Planck 2018 r_drag for data combinations other than TT,TE,EE+lowE+lensing, and a Planck 2018 z_drag value.
3. Q1 — Planck PR4 n_s is not in `cosmo-inflation-primordial`; it was obtained by following the explicit pointer to `cosmo-cmb` (0.9681 ± 0.0039).
4. Q11 — the source of the 0.051 lower end of the τ range is not in the two allowed skills that discuss it; obtained by following the explicit pointer to `cosmo-cmb` (NPIPE, 0.051 ± 0.006, arXiv:2007.04997).

No question was left unanswered.

### CONFLICT

- C1 — τ range from Planck reprocessings. 0.054–0.063 in `cosmo-reionization-21cm/SKILL.md` line 24, `references/results.md` lines 29–30, `references/open-questions.md` line 159; 0.051–0.063 in `cosmo-tensions-anomalies/references/results.md` lines 19 and 175 and `references/systematics.md` line 57. The reionisation file acknowledges the difference (lines 30–31) without resolving it. Also σ ≈ 0.006 (SKILL.md) against 0.006–0.007 (results.md) inside the reionisation skill.
- C2 — CHIME auto-power spectrum inside `cosmo-surveys-facilities`. `references/surveys-and-data.md` line 253 says "a cosmological auto-power result was not found by the title search of 2026-10-09" and line 308 lists it as not verified; the same skill's `SKILL.md` lines 48–50 and `cosmo-reionization-21cm/references/results.md` line 224 give the 12.5σ detection (arXiv:2511.19620). `SKILL.md` also omits the MeerKLASS auto-spectrum (arXiv:2610.12158), posted after its snapshot.
- C3 — "latest B-mode measurement" inside `cosmo-inflation-primordial`. `SKILL.md` line 28 calls BK18 "the latest B-mode measurement" and `references/open-questions.md` line 31 says "No newer B-mode limit on inflationary r exists", while `references/results.md` lines 86 and 93 list the later, independent SPT-3G limit r < 0.25 (arXiv:2505.02827, 2025). Wording, not numbers: `results.md` line 90 has the precise form ("most recent BICEP/Keck constraint").
- C4 — headline MWA limit inside `cosmo-reionization-21cm`. `SKILL.md` line 31 quotes (23.0 mK)² (EW polarisation); `references/results.md` lines 184–186 name 470 mK² = (21.7 mK)² (NS) as the deepest MWA value. Both are on `results.md` line 177.
- C5 — documented disagreements between external sources, recorded as such in `cosmo-surveys-facilities/references/results.md`: Euclid DR2 June 2029 (ESA) against March 2029 (IPAC), line 161; eROSITA survey start 13 against 12 December 2019, line 39. Also CMB-SPA n_s 0.9684 ± 0.0030 (arXiv v1) against 0.9679 ± 0.0033 (v2), `cosmo-inflation-primordial/references/results.md` line 20.

No numerical conflict was found for Q2–Q7, Q9, Q10, Q12, Q14; where two skills carry the same number (Q4, Q5, GWTC-5.0 counts) they agree.

### Navigation failures

No question needed more than the files the file map names, and SKILL.md's "What an expert holds in mind" bullets already contained the headline answer to all 14 questions. Frictions:

1. Q8 — broken cross-reference: `cosmo-surveys-facilities/references/surveys-and-data.md` line 159 sends Euclid "Releases and calendar" to "Sect. 2.7", which is UNIONS; the Euclid row is 2.10 (line 212).
2. Q14 — "what CAMB v2 changes" is split over `physics-and-methods.md` §1.2, `results.md` §1.2 and `open-questions.md` §2; the file map has no row for "what changed in a new version".
3. Q4 — the reason for the Δχ²–evidence disagreement is in `systematics.md` §7, not in `results.md` §4 where the file map sends; the topic is also owned by two skills (statistics, tensions), which agree.
4. Q13 — `cosmo-theory-foundations/SKILL.md` line 11 says to read first a hub file outside the nine directories; four sub-questions needed two reference files.
5. Q12, Q8 — one sub-item each (GLADE+ completeness, eROSITA DR2 source counts) sits in `surveys-and-data.md` and not in `results.md`; consistent with the file maps, but a second file is needed.
6. Q7 — constrained-simulation facts are duplicated in `surveys-and-data.md` §5 and `results.md` §7; harmless, either answers.
