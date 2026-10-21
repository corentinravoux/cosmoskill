# Level test — third L3 test of 2026-10-20, part 3a

Item C of `docs/plans/2026-10-20-plan.md` ("the domains not yet tested"). Five skills:
`cosmo-distance-ladder-h0`, `cosmo-tensions-anomalies`, `cosmo-peculiar-velocities`,
`cosmo-lyman-alpha`, `cosmo-clusters`. The first four were edited on 2026-10-20 for
generality. Forty questions, eight per skill, are in `docs/tests/levels/l3-questions-3a.md`.
Each was answered twice from the skill files only: an **L2 run** (the skill's `SKILL.md`
plus one reference file chosen from the file map) and an **L3 run** (the same plus at
most one dossier of `deep/`, chosen from the file map). Model memory was not used to
fill gaps. This run tests; no skill file was changed. Part 3b (other skills) runs at the
same time and writes its own files.

Status: complete; five skills.

## Procedure

1. **Questions first.** Written from the five `subtopics.tsv` files, the file names of
   `deep/` and `references/`, and the one-line skill descriptions of the skill listing,
   before any `SKILL.md` body, reference file or dossier of the five skills was opened.
   Per skill, six questions fall one each on the six dossier subtopics and two on
   subtopics whose `files` column lists no dossier (controls).
2. **Preliminaries read.** The second run (`run-2026-10-20-l3-second.md`) and its
   questions, the level table of `skills/observational-cosmology/SKILL.md` ("Choosing the
   level"), plan item C. Layer check: no `.cosmoskill/` in the working directory, its
   parents or the home directory; `COSMOSKILL_HOME` unset; layer `base` for every
   question.
3. **Isolation.** One session answered all questions: each file was read once, and each
   answer was then restricted to the passages of the files assigned to that run. As in
   the earlier runs this is weaker than a fresh session per run; every L2 grade names the
   passage it rests on.
4. **Grading.** (a) Y answers, P partly, N not; (b) locator: Y when the load-bearing
   statements carry paper + section, table or equation. **Tightened rule**: an L2 answer
   graded P counts as an L2 failure.
5. **Pass rule per skill.** The L3 run answers (Y) at least 5 of the 6 dossier questions
   with locators, including at least 3 that the L2 run failed (P or N); each L3 question
   loads at most one dossier. Controls should show no L3 gain; when one gains, the
   dossier that served it is named.
6. **Source checks.** At most 10 in all (`fetch_paper.py --grep` or `--section`).

Abbreviations for reference files: `methods` = `references/physics-and-methods.md`,
`syst` = `references/systematics.md`, `open` = `references/open-questions.md`,
`results` = `references/results.md`, `surveys` = `references/surveys-and-data.md`,
`alt` = `references/alternative-distance-probes.md`, `cp` =
`references/cosmological-principle.md`. Every run also loaded the skill's `SKILL.md`.

## cosmo-distance-ladder-h0

### Files loaded

| Q | L2 reference file | L3 dossier |
|---|---|---|
| H1 | syst | `deep/cepheid-sn-ladder.md` |
| H2 | methods | `deep/trgb.md` |
| H3 | methods | `deep/jagb-miras.md` |
| H4 | methods | `deep/megamasers.md` |
| H5 | methods | `deep/time-delay-cosmography.md` |
| H6 | methods | `deep/inverse-ladder.md` |
| H7 (control) | methods | `deep/cepheid-sn-ladder.md` (file-map row "Cepheid photometry, cuts, PL form": outlier rejection) |
| H8 (control) | alt | none: no file-map row for quasar Hubble diagrams |

### Answers

**H1 — Cepheid PL calibration in the joint fit; crowding test; reanalyses.**
- L2 (syst §§1, 2, 5, 4, 6): artificial stars injected at the PL-predicted magnitude and
  iterated with the fit, 20% background floor as within-host covariance
  (arXiv:2112.04510, Eq. 8); HST − JWST −0.01 ± 0.03 mag, distance-growing bias rejected
  at 8.2σ (arXiv:2401.04773), 19 hosts −0.022 ± 0.029 (arXiv:2509.01667, Sect. III.2.3);
  γ on [Fe/H] against [O/H] (arXiv:2404.08038, Sects. IV.3, V); R = 0.386 and NIR against
  optical Wesenheit (arXiv:2112.04510, Sects. 6.3, 6.13); reanalyses: Efstathiou's
  LMC–NGC 4258 inconsistency (arXiv:2007.10716), volume prior and Gaia offset
  (arXiv:2601.22215), Madore & Freedman on metallicity (arXiv:2602.13397). The period
  mismatch is listed as "not transcribed" (syst, Not verified); colour cuts, outlier
  rejection and per-host colour relations are absent. **P.**
- L3: discovery and Hertzsprung-progression validation (arXiv:2112.04510, Sects. 3.1–3.2),
  NIR photometry and artificial-star cycle (Sects. 3.3–3.4), cut table with reasons
  (Sects. 3.4, 4.6, 6.1, Table 3), metallicity assignment (Sect. 3.5, App. C), JWST
  quality cuts and Wesenheit systems (arXiv:2401.04773, Sects. II–III.3); reanalyses
  side by side: per-host colour–luminosity relations (arXiv:2105.11461), period-matched
  resampling and broken PL with their costs (arXiv:2412.07840, Sects. VI.1–VI.3), CCHP
  "uncrowded" selection and photometry-package critique (arXiv:2408.06153, App. B), with
  SH0ES's replies (arXiv:2401.04773, Sect. III.3, Table 4). **Y.**

**H2 — TRGB tip measurement; systematic choices; why analyses differ.**
- L2 (methods §2.4 and table): two families (edge detection, LF fitting), contrast
  ratio and CATS standardisation (arXiv:2304.06693, Sect. III.1), Sobel origin, JWST
  calibrations and colour term (arXiv:2503.11769, Eq. 8). Field selection, smoothing,
  tip-error rules and the cause of group differences are absent from this file (the
  108-variant spread is in syst §11, not loaded). **P.**
- L3: three field-selection prescriptions with reasons (arXiv:2503.11769, Sect. III.3;
  arXiv:2401.04776, Sect. IV.1; arXiv:2304.06693, Sect. II.1.1), 1D, 2D and LF-fit edge
  methods, tip-error rules per group (arXiv:2304.06693, Eq. 2; arXiv:2503.11769,
  Sect. IV.1.2), smoothing and Poisson-weighting drift (arXiv:2401.04776, Sect. IV.3),
  multi-peak choice worth 3.6 in H0 (arXiv:2304.06693, Table 4), the contrast debate
  both ways (arXiv:2503.11769, App. D.2), and the NGC 4258 field choice by group worth
  ~1.6 in H0 (arXiv:2304.06693, Sect. V.2). **Y.**

**H3 — JAGB reference magnitude and colour window; Mira PL calibration; limits.**
- L2 (methods §2.4): colour box 1.5 < J − K < 2.0, statistic not standardised
  (arXiv:2502.05259), the JWST box (arXiv:2502.05259, Sect. II.4), O-rich Miras with
  P < 400 d and three anchors (arXiv:2507.10658). How the statistic and window are chosen,
  the Mira period-range test, carbon contamination and the limits are not in this file.
  **P.**
- L3: CCHP convergence algorithm against fixed ellipses (arXiv:2408.03474, Sect. III.4.1;
  arXiv:2502.05259, Sect. V.1.1), colour boxes and magnitude windows with reasons
  (arXiv:2005.10792, Sect. II; arXiv:2502.05259, Sect. II.4), mode against middle of 25
  variants and its 73.3 against 71.2 (arXiv:2502.05259, Sects. III, IV.1, Table 3), Mira
  selection cuts, boxcar period range, carbon-rich model and the two- or three-anchor
  zero point (arXiv:2312.08423, Sects. III.1–V.2, Eqs. 2–9; arXiv:2507.10658,
  Sect. IV.2, Eq. 4), limits (two SN hosts; field-to-field 0.11 mag). **Y.**

**H4 — Maser-disc distance; host velocities in the H0 step.**
- L2 (methods §§3, 2.6): spot observables, D = r/θ, warped-disc model, MCP likelihood
  L_D × L_v with flat ΛCDM at Ω_m = 0.315 (arXiv:2001.09213, Sect. 3), the 2026
  joint refit with distance prior and selection (arXiv:2609.17684), field-level
  marginalisation (arXiv:2505.10682). Accelerations' role, error floors, priors and the
  alternative velocity treatments with their H0 are absent. **P.**
- L3: per-spot data and warped Keplerian equations (arXiv:2609.17684, Sect. 3.1,
  Eqs. 1–13), error floors as parameters (arXiv:1908.05625, Sect. II), priors and
  sampling (arXiv:2609.17684, Table 2, Sect. 3.5), outlier rules, four MCP velocity
  treatments with H0 (arXiv:2001.09213, Sects. 3.1–3.4), the hierarchical velocity model
  and selection (arXiv:2609.17684, Eqs. 21–26), σ_v dependence (arXiv:2608.06247,
  Sect. 3), field-lookup coordinate and real- against redshift-space reading
  (arXiv:2609.17684, Sect. 5.1). **Y.**

**H5 — Mass-sheet degeneracy; what moves H0; blinding.**
- L2 (methods §§4, 7, and `SKILL.md`): MST and λ_int, hierarchical λ_int constrained by
  kinematics (arXiv:2007.02941), external lenses, κ_ext named, resolved kinematics,
  Ω_m prior, blinding table (arXiv:1907.04869; arXiv:2506.03023); 73.3 assumed profiles
  against 71.6 with the MSD free (`SKILL.md`). How κ_ext is estimated, the anisotropy
  prior, the power-law/composite comparison and the size of each assumption are absent.
  **P.**
- L3: delay measurement (arXiv:1907.04869, Sect. 3.2; arXiv:2604.14145, Sect. 4), the two
  mass families (arXiv:2506.03023, Eq. 22; arXiv:1912.08027, Eq. 14), κ_ext from weighted
  counts and the GEV population model (arXiv:1907.04869, Sect. 3.4; arXiv:2506.03023,
  Sect. 7.2.3), kinematics equations (Eqs. 12–15), priors (Table 3), costs: λ_int free
  2% → 4.5% (arXiv:2007.02941, Sect. 8.2), anisotropy prior 1.5 km/s/Mpc (Sect. 4.2),
  Ω_m information 2.1 (arXiv:2506.03023, Sect. 10.1.1), external samples
  (Sects. 8.1–10.1.2); blinding by median subtraction (arXiv:1907.04869, Sect. 3.6).
  **Y.**

**H6 — Inverse ladder; r_d prior and SN sample; sound-horizon-free H0.**
- L2 (methods §6): construction (arXiv:1411.1074), DESI r_d formula
  (arXiv:2503.14738, Eq. 2), BBN prior, history, sound-horizon-free routes named
  (arXiv:2411.16677; arXiv:2509.16202). How H0 depends on the r_d prior, the SN sample
  and the expansion order: not in this file. **P.**
- L3: cosmography to fifth order (arXiv:2406.05049, Eqs. 5–14), r_d priors with reasons
  and the H0 × 147.49/r_d form (arXiv:1411.1074, Eq. 23), order selection by ΔAIC
  (arXiv:2406.05049, Table 1), SN-compilation swaps (arXiv:2602.12822, Sect. 4.1),
  D_M against D_H, three sound-horizon-free set-ups with their priors and projection
  effects (arXiv:2411.16677, Eq. 3, Sect. 4.4, Table 2; arXiv:2509.16202,
  Sects. II.1–IV.1; arXiv:2511.19332). **Y.**

**H7 (control, ladder statistics).** L2 (methods §§2.1, 2.2, 2.7): linear system and the
three off-diagonal covariance terms (arXiv:2112.04510, Eqs. 6, 8, 9), SN outlier cut,
H0DN network with pseudo-inverse (arXiv:2510.23823, Eq. B1, Sect. B.2), volume prior and
selection (arXiv:2511.03394; arXiv:2603.09880; arXiv:2607.22425). **Y.** L3
(`cepheid-sn-ladder`): adds Cepheid outlier variants (arXiv:2112.04510, Sect. 6.1).
**Y**, no gain needed.

**H8 (control, quasar Hubble diagram).** L2 (alt §2): distance from the X-ray–UV relation,
SN cross-calibration (arXiv:2008.08586, Sect. 3.1), standardisability test by model
dependence (arXiv:2012.09291), sub-sample heterogeneity (arXiv:2107.07600), reverberation
comparison, dispersion model; referee list. **Y.** L3: no dossier row. **Y**, no gain.

### Grades

| Q | L2 (a) | L3 (a) | L3 locator | Gain |
|---|---|---|---|---|
| H1 | P | Y | Y | yes |
| H2 | P | Y | Y | yes |
| H3 | P | Y | Y | yes |
| H4 | P | Y | Y | yes |
| H5 | P | Y | Y | yes |
| H6 | P | Y | Y | yes |
| H7 (c) | Y | Y | Y | — |
| H8 (c) | Y | — (no dossier) | Y | — |

**Verdict: pass.** L3 answers 6 of 6 with locators; 6 L2 failures answered; one dossier
per question; controls inert. Every dossier opens with an "Already in L2" list, and the
L2 file stops at the principle, so the split between the levels is clean.

### Source check (1 used)

- **E1** `methods` §4 says the TDCOSMO 2025 results "are stable across the choice" of
  Ω_m prior; `deep/time-delay-cosmography.md` says the Ω_m information moves the
  TDCOSMO-only H0 by 2.1. arXiv:2506.03023, abstract and Sects. 8.2.1–8.2.2: Pantheon+
  (Ω_m = 0.334 ± 0.018) gives 71.6 (+3.9/−3.3), DES-SN5YR (0.352 ± 0.017) 71.2
  (+3.7/−3.6), and "DESI-DR2 ... instead of Pantheon+ yields very similar results". Both
  statements hold: the L2 one is about the informative priors, the dossier's 2.1 is
  uniform against Pantheon+. The L2 sentence omits that the uniform-prior result
  differs by 2.1, which a reader comparing with TDCOSMO-IV needs.

### Generality flags

- `methods` §2.6 ("Redshifts and peculiar velocities") calls field-level conditioning on
  Manticore-Local realisations "the current practice" and cites arXiv:2505.10682,
  arXiv:2509.09665 and arXiv:2609.29996; per `sources.tsv` all three come from one
  collaboration (McAlpine; Stiskalek). Linear 2M++ corrections (Peterson et al.,
  arXiv:2110.03487) are used by SH0ES and H0DN in the same section; "current practice"
  overstates one group's method. `syst` §9 "Mitigation" repeats it with
  arXiv:2509.09665 alone.
- `deep/megamasers.md` writes the disc model "as written in the 2026 reanalysis"
  (Stiskalek & Desmond, arXiv:2609.17684) and gives that paper's diagnosis of Watkins &
  Feldman at length (§"Where the field is read"); the dossier says itself that "this is
  one group's diagnosis of the other; no reply was found". Acceptable as flagged, but
  the H4 answer rests mostly on one group's reanalysis.

## cosmo-tensions-anomalies

The `files` column of `subtopics.tsv` names a dossier for three rows only; the file map of
`SKILL.md` names all six (rows "Dipole significance", "CMB–DESI distance", "Anomaly
p-values"), so the L3 runs for T2–T4 followed the file map.

### Files loaded

| Q | L2 reference file | L3 dossier |
|---|---|---|
| T1 | methods | `deep/large-angle-cmb-anomalies.md` |
| T2 | methods | `deep/anomaly-significance.md` |
| T3 | methods | `deep/cmb-bao-mismatch.md` |
| T4 | methods | `deep/cosmic-dipoles.md` |
| T5 | methods | `deep/high-redshift-galaxies.md` |
| T6 | methods | `deep/theoretical-resolutions.md` |
| T7 (control) | methods | `deep/theoretical-resolutions.md` (closest: its §"S8"; no S8 row in the file map) |
| T8 (control) | cp | none: no file-map row |

### Answers

**T1 — Significance of S_1/2, hemispherical asymmetry, Cold Spot; mask and map.**
- L2 (methods §7): the statistics as defined (arXiv:2310.12859, Eqs. 7–13), the null of
  isotropic Gaussian ΛCDM skies, the a posteriori status and polarisation as the
  independent test (arXiv:1906.02552, conclusions). Estimators for the dipolar
  modulation, the Cold Spot kernel, and how mask and map move each p-value: not in the
  file. **P.**
- L3: QML modulation estimator and its ℓ_max dependence (arXiv:1906.02552, Sect. 7.2,
  Eqs. 54–62, Tables 24–25), local-variance estimator and its definition and mask
  dependence (Sect. 7.1, Table 21; arXiv:2509.03720, Sects. III.5, IV), Cold Spot kernel
  and comparison ensemble (arXiv:0908.3988; arXiv:1703.07894), profile and polarisation
  test (arXiv:1906.02552, Sect. 6.5, Eqs. 51–52, Table 20), supervoid lensing test
  (arXiv:2211.16139, Sects. 4–5), mask table for five statistics (arXiv:2509.03720,
  Sect. IV). **Y.**

**T2 — Correcting for a posteriori choices and look-elsewhere; independent tests.**
- L2 (methods §§1.2, 7): N p_local rule, the Guth & Namjoo product-of-p-values
  correction with 16 and 50 effective tests (arXiv:2602.10178, Sects. II, IV–V),
  polarisation as "largely independent" (arXiv:1906.02552). The correction for a free
  parameter inside one statistic (angle, ℓ_max) and the power of the independent tests
  are absent. **P.**
- L3: null ensembles and their resolution floors (arXiv:1906.02552, Sect. 4;
  arXiv:2310.12859, Methods), tail conventions, global p-value by scanning on every
  simulation (arXiv:1906.02552, Sects. 6.1, 6.3), joint counting against product
  (arXiv:2310.12859, Tables 1–3), the Guth & Namjoo density (arXiv:2602.10178,
  Eqs. 8–15), cut- against full-sky S_1/2 (arXiv:0911.5399, Sects. 4.2, 5), T–E estimator
  correlations, constrained realisations (arXiv:2206.05920, App. C, Eq. C3), Copi
  falsification test (arXiv:1906.02552, Table 14), forecasts labelled. **Y.**

**T3 — Quantifying the CMB–BAO mismatch; choosing among extensions.**
- L2 (methods §4): the (Ω_m, h r_d) Gaussian difference (arXiv:2503.14738, Eq. 18), SPT's
  form (arXiv:2506.20707, Sect. VII.3), dependence on the CMB set, τ–Ω_m anticorrelation
  (arXiv:2504.16932), "five parameters respond to one mismatch". What separates the
  extensions, and the size of each input choice, is not in the file. **P.**
- L3: inputs and compressed CMB (arXiv:2503.14738, Sect. IV.2, Eqs. 16, 35–36), subspace
  and conversion check, combination thresholds, per-CMB-set and per-τ distances
  (arXiv:2506.20707, Sect. VII.3, App. I), localisation by rotated distances and SVD
  modes (arXiv:2505.02658, Eqs. 4–7, Table 1; arXiv:2606.30527, Eq. 3), direction of each
  extension (arXiv:2504.21813, Eq. 4, Table 1), and four tests of whether an extension
  only absorbs the mismatch: χ² split by likelihood (arXiv:2506.20707, Table 7), a new
  measurable SVD mode, pivot rotation, anchor swap. **Y.**

**T4 — Number-count dipole: estimator, mask, x, α, templates; expectation and
significance.**
- L2 (methods §6): D_kin = [2 + x(1 + α)]β (arXiv:2009.14826, Eq. 1), the three
  assumptions and the theory exchange (arXiv:2111.03616; arXiv:2404.07929), the
  estimator table, the clustering-aware null (arXiv:2511.00822). How x and α are
  measured, the mask and the ecliptic template are not in the file (its "Not verified"
  says the radio D_kin were not read). **P.**
- L3: catalogue cuts and masks with reasons (arXiv:2009.14826, Sect. II;
  arXiv:2503.02470, Sects. 3.1–3.4), x and α at the flux limit with a table per
  catalogue and the x–α correlation bound (arXiv:2212.07733, Eq. 25), four estimators
  (arXiv:2009.14826, Eq. 2; arXiv:2212.07733, Eqs. 4–8; arXiv:2510.23769, Eqs. 24–25;
  arXiv:2503.02470, Eqs. 7–8), three null constructions and the p-value criteria
  (arXiv:2511.00822, Eqs. 17–20), ecliptic correction fixed, free or forward-modelled
  (arXiv:2607.25703, Sect. 5.1), fit-or-simulate higher multipoles, redshift dipole
  (arXiv:2608.30914). **Y.**

**T5 — JWST "too massive" test; deciding whether it is cosmological.**
- L2 (methods §9): the baryon bound and Eqs. 1–5 (arXiv:2208.01611, Sect. 2), observed-side
  systematics named (arXiv:2604.18683), dependence on spectroscopy. Cosmic variance,
  Eddington bias, the IMF and the choice of statistic are absent. **P.**
- L3: three observables, mass function and its calibration (arXiv:2604.13866, Eqs. 2–6;
  arXiv:2208.01611, Sect. 4), ε fixed, distributed or free, sample and Poisson variance
  (arXiv:2511.13708, Eq. 8), two Eddington corrections (arXiv:2208.10479, Eq. 13;
  arXiv:2511.13708, Eq. 11), SED systematics as a shift, binary, extreme-value or
  one-sided likelihood statistics (arXiv:2208.10479, Eq. 4; arXiv:2604.13866, Eq. 12),
  how cosmology enters (w, Ω_K, EDE), IMF flagged as unquantified. **Y.**

**T6 — Comparing H0 solutions fairly.**
- L2 (methods §§1.1, 1.3, 11): the World Cup classes and its criterion (−ΔAIC > 10 or
  ln BF > 3 with the M_B prior; arXiv:2607.13283, Sect. III.3), metric definitions
  (Eqs. 16–20), rule 6 on prior volume, no-go arguments. Which data form the baseline,
  why M_B and not H0 in numbers, the frequentist–Bayesian dispute and the per-data
  shifts are absent. **P.**
- L3: two-question structure (arXiv:2607.13283, Sect. III; arXiv:2107.10291, Sect. 2),
  baseline data with exclusions (arXiv:2607.13283, Sect. IV.1–IV.2), M_B prior with the
  worked hockey-stick case (arXiv:2101.08641, Table 3) and the double-counting caveat
  (arXiv:2602.06293, App. A), three tension metrics and two preference metrics with
  thresholds in a table, EDE Bayesian against profile likelihood (arXiv:2507.23355;
  arXiv:2505.08051, Sect. VI), knockout tests with S8, BBN, Σm_ν (arXiv:2607.13283,
  Sects. V.1–V.7). **Y.**

**T7 (control, S8).** L2 (methods §3): definition, how each probe's side is computed,
the probe-specific exponents, conventions that break comparisons (exponent, point
estimate, CMB reference, projected or full space). Which scales and which baryon
treatment: only named. **P.** L3 (`theoretical-resolutions`, §"S8"): S8 in an H0 model
and the "S8 inferred under ΛCDM" caveat (arXiv:2503.14454, Sect. VIII.2); nothing on scale
cuts or baryons across probes. **P**, no gain.

**T8 (control, homogeneity and inhomogeneous models).** L2 (cp §§2, 4): D₂ and the 1%
R_H definition (arXiv:1205.6812), angular θ_H (arXiv:2606.07854), selection-function bias
(arXiv:2006.15022), LTB failures on kSZ, CMB, BAO (arXiv:1009.3967; arXiv:1007.3725;
arXiv:1201.2790), backreaction exchange, timescape fits and disputes, referee list. **Y.**
L3: none. **Y**, no gain.

### Grades

| Q | L2 (a) | L3 (a) | L3 locator | Gain |
|---|---|---|---|---|
| T1 | P | Y | Y | yes |
| T2 | P | Y | Y | yes |
| T3 | P | Y | Y | yes |
| T4 | P | Y | Y | yes |
| T5 | P | Y | Y | yes |
| T6 | P | Y | Y | yes |
| T7 (c) | P | P | Y | no |
| T8 (c) | Y | — (no dossier) | Y | — |

**Verdict: pass.** L3 answers 6 of 6 with locators; 6 L2 failures answered; one dossier
per question; controls inert. `physics-and-methods.md` defines each statistic but stops
before estimators and nulls, which the dossiers hold.

### Source checks (2 used)

- **E2** `SKILL.md`, "What an expert holds in mind", fifth bullet: "CMB against DESI DR2
  in ΛCDM: 1.6σ (P-ACT) to 3.7σ (SPT + ACT) (arXiv:2503.14452)". arXiv:2503.14452
  (ACT DR6, March 2025), abstract: "ΛCDM parameters agree between the P-ACT and DESI DR2
  data at the 1.6σ level"; no SPT + ACT combination appears in it (two searches). The
  3.7σ is from SPT-3G D1, arXiv:2506.20707, Sect. VII.3, as `deep/cmb-bao-mismatch.md`
  ("Which CMB data") cites it. The bullet's citation covers only the lower endpoint;
  arXiv:2506.20707 should be added.

### Generality flags

- `deep/theoretical-resolutions.md` and `methods` §§1.1, 11 judge every H0 model through
  the H0 World Cup (arXiv:2607.13283) and the H0 Olympics (arXiv:2107.10291), both
  Schöneberg et al.; the thresholds (−ΔAIC > 10 or ln BF > 3; ΔAIC ≤ −6.91) are that
  framework's. The dossier attributes them and adds SPT-3G (arXiv:2507.23355) and Poulin
  et al. (arXiv:2505.08051), so the lean is visible, but no comparison framework from
  another group is described.
- `cp` §5, critiques of the local void: two of three critiques (arXiv:2506.10518,
  arXiv:2505.10682) come from the Manticore/Stiskalek collaboration flagged under the
  ladder skill; Kenworthy et al. (arXiv:1901.08681) is independent. The file's own
  attribution note covers the proponents' side only.

## cosmo-peculiar-velocities

### Files loaded

| Q | L2 reference file | L3 dossier |
|---|---|---|
| V1 | syst | `deep/distance-indicators.md` |
| V2 | methods | `deep/two-point-statistics.md` |
| V3 | methods | `deep/field-level-likelihood.md` |
| V4 | methods | `deep/velocity-density-comparison.md` |
| V5 | methods | `deep/bulk-flows.md` |
| V6 | syst | `deep/supernova-velocities.md` |
| V7 (control) | syst | `deep/distance-indicators.md` (closest: Step 3 f_n, Step 6 zero-point) |
| V8 (control) | methods | `deep/field-level-likelihood.md` (closest: σ_u fixed or sampled, k_max) |

### Answers

**V1 — Fitting FP or TF for velocities; selection; intrinsic-scatter model.**
- L2 (syst §§0, 2, 9b): the DESI DR1 3D-Gaussian FP likelihood with 8 parameters, p < 0.01
  clipping, selection in f_n and S_n (arXiv:2512.03226, Sects. 5.2.1, 6.1), the SDSS PV f_n per
  trial distance (arXiv:2201.03112, Sect. 5.1), the DESI TF HyperFit in redshift bins
  (arXiv:2512.03227, Sect. IV.3). The choice between direct, inverse and orthogonal fits, the
  error-matrix terms and how the scatter model is tested are absent. **P.**
- L3: FP observables with aperture and evolution corrections and their reasons
  (arXiv:2201.03112, Eqs. 2–5; arXiv:2512.03226, Sect. 5.1), the censored 3D Gaussian with its
  error matrix (arXiv:2201.03112, Eqs. 16–17), S_n against f_n and the integral of Eq. 21, η
  posteriors as skew-normals, DESI and CF4 TF practice (arXiv:2512.03227, Eqs. 8–18;
  arXiv:2004.14499, Sect. III), a direct/inverse/orthogonal table with the selection each
  tolerates (arXiv:2301.12648, Sects. 3.2, 6.1), curved TF and magnitude-dependent scatter
  (Eq. 19), hemispheric zero-point (arXiv:1409.6161, Sect. 3.2), the ξ^{vg}_0 null test
  (arXiv:2602.23033, App. C). **Y.**

**V2 — Momentum P(k) or ψ1, ψ2: estimator, window, covariance; choosing the space.**
- L2 (methods §4): momentum estimator and shot noise (arXiv:1906.02875), DESI DR1 data vector,
  window matrix from randoms and k ranges (arXiv:2512.03231), ψ estimators and the A(r), B(r)
  geometry (arXiv:2512.03230, Sect. 3), mock or analytic covariance (§8), linear-template bias
  (arXiv:2309.14457). How to choose between the two spaces: only that DESI runs both. **P.**
- L3: why momentum rather than velocity (arXiv:2512.03231, Sect. 3.1), field weights and the
  different P_FKP of the two DESI analyses (Eqs. 25–26; arXiv:2512.03230, Eqs. 21–22), the
  imaginary cross spectrum (Eq. 17, App. B), the one-loop model and σ_vT, σ_vS
  (Eqs. 29–31; arXiv:1906.02875, App. A.1), window convolution to ℓ_max = 4 (Sect. 4.3),
  Gaussianity of the multipoles and Box–Cox (arXiv:1906.02875, Sect. 6.3), linear against PT
  template by r_min (arXiv:2309.14457, Sects. 4–5), equivalence of the power-spectrum and
  full-covariance reconstruction errors (arXiv:2408.05660). **Y.**

**V3 — Field-level covariance for many galaxies; non-Gaussian η errors; limits.**
- L2 (methods §§1, 3, 8): covariance from P(k) by Hankel transforms (arXiv:2501.16852,
  Sect. 2.2), gridding (arXiv:0802.1935), named covariance models, analytic zero-point
  marginalisation (arXiv:2512.03229, Eq. 32), η as the observable because errors are Gaussian
  in log distance (arXiv:1404.3799), DESI DR1 cost (~140 GB, σ_u fixed, JAX), Hessian errors
  inflated ×1.64. **Y.**
- L3: data vector and cell definitions (arXiv:2512.03229, Eqs. 16–21, 31), covariance terms,
  grid window and cell-mean correction (Eqs. 22–25), nuisance and extra-density terms
  (Eqs. 26–30; arXiv:1706.05205, Sect. 3.8), numerics and sampler (Sect. 3.4), gridded against
  per-object data, mesh settings (arXiv:2609.34508, Sect. 4.1), Fisher against likelihood.
  **Y**, no gain.

**V4 — β or fσ8 from velocity–density comparison; external flow; forward or inverse; limits.**
- L2 (methods §5): linear prediction scaled by β, reference analyses, VIRBIUS and the joint
  indicator calibration (arXiv:1512.04534; arXiv:2509.20235), the particle forward models and
  the absence of fσ8 from them. V_ext, the forward-against-inverse choice and the limits (method
  bias, cosmic variance, σ8 linearisation) are not in this file. **P.**
- L3: the seven-step 2M++ reconstruction (arXiv:1504.04627, Sect. 2.5), bias normalisation and
  its alternatives (arXiv:2312.03904, Eq. 11), line-of-sight likelihoods with V_ext
  (arXiv:1504.04627, Eqs. 17–21; arXiv:2509.20235, Eqs. 12–19), β* → fσ8 and three
  linearisation recipes, mock calibration ζ†, forward likelihood against inverse VELMOD against
  χ² on the same field (arXiv:1504.04627, Table 1), diagonal against full reconstruction
  covariance (arXiv:2408.05660, Eqs. 30–32), stochasticity correction (arXiv:2306.16664). **Y.**

**V5 — Bulk-flow estimator, window, ΛCDM expectation, significance.**
- L2 (methods §6): two definitions, the r⁻² identity, Kaiser MLE, ηMLE, MV weights with their
  constraints (arXiv:1808.07772), Wiener filter, MV's ΛCDM prior (arXiv:1508.03860), mock-tested
  errors (arXiv:2306.11269). The window integral, the expected covariance and the χ²: not in
  this file. **P.**
- L3: velocity conventions per analysis, object placement, MV target and weights, Kaiser MLE
  correction, shell fits (arXiv:2608.14265, Eqs. 8–12), tensor window (arXiv:2302.02028,
  Eqs. 30–31), R_ij and the χ²(3 dof) (Eq. 32), shell covariance (arXiv:2608.14265,
  Eqs. 16–24), mock calibration and error rescaling (arXiv:2306.11269, Sect. 5.1), Gaussian
  against r⁻² window on the same data, MV against Kaiser MLE (Table 3). **Y.**

**V6 — SN Ia velocities as signal; correlated velocities as a nuisance.**
- L2 (syst §§0, 3, 6, 8, 9b): SN-specific systematics listed, the ZTF selection limit z < 0.06
  and the redshift-binned bias-correction warning (arXiv:2303.01198, Sects. 5, 5.4), the TITAN
  intrinsic-scatter term (arXiv:2606.14962), the nuisance size: neglecting the covariance moves
  H0 by ~1.0 km/s/Mpc (arXiv:2405.20409). Standardisation fixed or fitted, the
  residual-to-velocity conversion and the choice of likelihood are absent. **P.**
- L3: four standardisation practices (arXiv:2303.01198, Eqs. 17–20; arXiv:1611.09862, Eq. 11;
  arXiv:2604.06361; arXiv:2606.14962), residual-to-velocity conversion and its variants
  (arXiv:2303.01198, Eq. 21, App. A), magnitude or magnification likelihood
  (arXiv:1611.09862, Eq. 9), velocity- and magnitude-space covariances (Eq. 38; Eqs. 4–6), the
  double-counted σ_v of compilations (arXiv:2604.06361, Sect. 2.1), redshift windows, group
  redshifts (arXiv:2408.14560), scatter-model and contamination effects (arXiv:2606.14962,
  Sect. V.3; arXiv:2507.00157, Sect. 5). With the L2 nuisance size, **Y.**

**V7 (control, zero point and Malmquist).** L2 (syst §§1–2): anchors per survey, full
correlation in the η covariance (arXiv:2512.03232), analytic marginalisation, effect on
spectra against flows (arXiv:1609.08247; arXiv:1511.04849), inhomogeneous Malmquist through the
tracer bias b1 (arXiv:2509.20235, Sect. 5), forward models, validation. **Y.** L3
(`distance-indicators`): adds f_n as the homogeneous correction and the hemispheric
zero-point. **Y**, no gain needed.

**V8 (control, σ_u and k_max).** L2 (methods §§2, 3, 4a): sinc D_u and its validity to
k ≤ 0.2 (arXiv:1312.1022), EFT and emulator replacements, σ_u fixed with a finite-difference
systematic (arXiv:2512.03229), k_max 0.3 and the k^p ≤ 0.1 cut with its reason
(arXiv:2512.03231). **Y.** L3 (`field-level-likelihood`): grid–σ_u equivalence, k_max for
per-object velocities. **Y**, no gain needed.

### Grades

| Q | L2 (a) | L3 (a) | L3 locator | Gain |
|---|---|---|---|---|
| V1 | P | Y | Y | yes |
| V2 | P | Y | Y | yes |
| V3 | Y | Y | Y | — |
| V4 | P | Y | Y | yes |
| V5 | P | Y | Y | yes |
| V6 | P | Y | Y | yes |
| V7 (c) | Y | Y | Y | — |
| V8 (c) | Y | Y | Y | — |

**Verdict: pass.** L3 answers 6 of 6 with locators; 5 L2 failures answered (V1, V2, V4, V5,
V6); one dossier per question; controls inert. The fold of the hub files into
`physics-and-methods.md` leaves the field-level method fully answerable at L2 (V3), as the
second run found for the statistics skill's S2 and S5.

### Source check (1 used)

- **E3** `deep/two-point-statistics.md`, "What goes wrong": the DESI DR1 correlation-function
  paper attaches [j0 − 2j1/(kr)] to Ψ⊥ and j1/(kr) to Ψ∥, the opposite of `methods` §4b.
  arXiv:2512.03230, Sect. 3.1.1, Eqs. 8–9: printed exactly so ("Ψ⊥(r) = … [j0(kr) −
  2 j1(kr)/(kr)]", "Ψ∥(r) = … j1(kr)/(kr)"). The dossier's warning stands; `methods` §4b uses the
  Gorski assignment of arXiv:2604.08314 and does not mention the swap.

### Generality flags

- `methods` §9 ("Conventions, units"), first bullet: "flip units: RA/Dec in radians, comoving
  distances in h⁻¹Mpc … (workspace `CLAUDE.md` §5)". A package skill cites the owner's
  workspace file and gives one code's units as the field's convention.
- `methods` §3 names the field-level covariance models by the labels of one paper (AB17, AB20,
  C23, L22, RC25, "labels of arXiv:2501.16852"), and writes the general decomposition as "the
  flip code". `deep/field-level-likelihood.md` cites the flip papers (arXiv:2501.16852,
  arXiv:2609.34508) 38 times against 37 for the DESI and SDSS analyses (arXiv:2512.03229,
  arXiv:2209.04166) and 13 for the Blake-group papers; its "Mesh settings", "σ_u … prior" and
  "Analytic Fisher" subsections rest on the flip papers alone, one a simulation study. The
  method is shared by three groups (Johnson/Adams–Blake, Lai–Howlett, flip); the weight is
  heavy for the smallest of them.
- `methods` §0 ("Method families") sets its own classification axis ("by what the estimator does
  to the data before fitting, not by the optimiser") and corrects the review's Table 1
  (Turner 2024). The argument is sourced, but the taxonomy is the skill's, not the field's.
- `deep/velocity-density-comparison.md`, "Tracer bias b1": the likelihoods of Said et al. 2020
  and Boubel et al. 2024 are described only as Stiskalek 2025 reads them (the dossier says so
  under "Not verified"); the critique is one-sided.

## cosmo-lyman-alpha

### Files loaded

| Q | L2 reference file | L3 dossier |
|---|---|---|
| F1 | methods | `deep/continuum-distortion.md` |
| F2 | methods | `deep/p1d-estimation.md` |
| F3 | methods | `deep/p1d-emulators.md` |
| F4 | methods | `deep/theory-sbi-field-level.md` |
| F5 | syst | `deep/validation-mocks-blinding.md` |
| F6 | methods | `deep/tomography-voids.md` |
| F7 (control) | syst | `deep/validation-mocks-blinding.md` (closest: Step 5, contaminant insertion) |
| F8 (control) | methods | `deep/p1d-emulators.md` (closest: IGM post-processing and the mean-flux prior) |

### Answers

**F1 — Continuum fit, distortion of the correlations, effect on BAO and full shape.**
- L2 (methods §§2.1–2.2, 4.1, 4.3): the DESI continuum model and its maximum-likelihood fit
  (arXiv:2503.14739, Sect. 2.4), the projector η and the distortion matrix
  (arXiv:1702.00176; arXiv:2404.03001, Eq. 7), the alternative per-object continua with
  accuracies (arXiv:1108.6080; arXiv:2405.06743), the small-scale leakage into the AP fit and
  its marginalisation (arXiv:2607.27410, Sect. 3.3). The iteration, the matrix construction and
  the comparison of approaches (fitted broadbands, mode de-weighting, mode marginalisation) are
  absent; what the distortion leaves in β is not stated. **P.**
- L3: the iterative fit with the variance model (arXiv:2306.06312, Eqs. 4–6, Sect. 3.3), forest
  cuts, why the projection makes δ^mp = δ^tp (arXiv:2506.15262, Eqs. 5–9), the matrix with its
  redshift evolution and settings (Eqs. 14–18; arXiv:2404.03001, Sect. 4.3), the template
  marginalisation (arXiv:2607.27410, Eqs. 16–18), a five-approach table with costs
  (arXiv:1702.00176, Sect. 4.3; arXiv:2503.15619, Sects. 3.4, 4.1.3), and the BAO-against-full-
  shape reading: β ≈ 4% low on mocks while BAO is unaffected (arXiv:2506.15262, Table 1). **Y.**

**F2 — FFT or QMLE; resolution, noise, masks; covariance.**
- L2 (methods §3.2): estimator table with strengths and weak points, the DR1 FFT and QMLE
  equations (arXiv:2505.09493, Eqs. 6–7; arXiv:2505.07974, Eqs. 3–6), noise subtraction or
  cross-exposure, resolution matrix, mock-derived masking and continuum corrections for the FFT,
  bootstrap covariance regularised against the Gaussian one, validation (arXiv:2509.13593).
  **Y.**
- L3: step-by-step continuum, noise (α correction, exposure differences, side-band η),
  resolution, masks, continuum three-point bias b(k), covariance tests, FFT–QMLE table, window-
  matrix critique (arXiv:2505.02904, Eqs. 26–27), user recommendations. **Y**, no gain.

**F3 — Building a P1D emulator; emulator error; out-of-sample validation.**
- L2 (methods §§6.3, 7): emulator table (LaCE GP and NN, ForestFlow, PRIYA, Lyssa) with inputs
  and accuracies, the two philosophies (arXiv:2011.15127), the DESI DR1 implementation with the
  emulator covariance in the likelihood and mocks from Lyssa and Sherwood
  (arXiv:2601.21432, Sects. 2, 6–8), stated limits (leave-one-out overestimates). **Y.**
- L3: suite design by pipeline, IGM post-processing, input choices with reasons, smooth-model
  training, error terms per pipeline (arXiv:2601.21432, App. A; arXiv:2309.03943, Eqs. 6–7),
  nuisance structure, compression tests (App. B), cross-code mocks (Sect. 5.3). **Y**, no gain.

**F4 — EFT and SBI for the forest: valid scales, nuisances, validation.**
- L2 (methods §6.4): EFT accuracy to 3 h/Mpc (Sherwood) and 2 h/Mpc (ACCEL²), first data
  application with simulation-informed priors (arXiv:2405.13208), field-level and hybrid models
  named, SBI on CAMELS (arXiv:2603.13011). How k_max is chosen, how the biases and counterterms
  are treated and how SBI is validated are absent. **P.**
- L3: the line-of-sight bias expansion (arXiv:2309.10133, Eqs. 3.11–3.22), calibration fits and
  priors (Eq. 5.3), k_max by posterior stability (Sect. 5.2), the P1D renormalisation (Eq. 6.9),
  the b_O(b_1) prior route and its factor-3 effect on σ_8 (arXiv:2405.13208), the Fisher
  compression (arXiv:2604.09407, Sects. 3–4), field-level and HEFT reach (arXiv:2507.00284;
  arXiv:2512.13681), SBI coverage and cross-simulator tests (arXiv:2603.13011, Sects. IV.2–IV.4),
  the independent tree-level test (arXiv:2608.21226). **Y.**

**F5 — Validating a 3D analysis on synthetic data; blinding.**
- L2 (syst A4, D1, G1, G2, G6, G7): the σ/3 threshold, the mock suites and their stacked biases,
  the origin of the α_∥ bias (arXiv:2503.14741, Sect. IV.1, Table 1), splits and variations,
  blinding by an additive BAO-like term (arXiv:2404.03001, Sect. 6.1) or likelihood offsets
  (arXiv:2509.15308, Sect. II.4), the catalogue-level AP scheme (arXiv:2607.07875). Which
  contaminants are injected, and how, is given only as what the mocks lack. **P.**
- L3: how each family builds the field and quasars (arXiv:1912.02763; arXiv:2310.18996;
  arXiv:2607.27412), small-scale power, the τ mapping and RSD, tuning targets and procedures
  (table of Step 4), insertion of HCDs, metals, BALs and redshift errors (arXiv:2401.00303,
  Sects. 2.3.1–2.3.3; arXiv:2503.14741, Sect. II.2), quickquasars, which family for which test,
  and the AP blinding algorithm with its limits (arXiv:2607.07875, Sects. 2, 3.5). **Y.**

**F6 — Tomographic reconstruction, voids, protoclusters, mock calibration.**
- L2 (methods §5): Wiener filtering, resolution set by the sightline separation, the Lee et
  al. requirements (arXiv:1309.1477), SO void finder calibrated on hydrodynamics
  (arXiv:1710.02612), Stripe 82 catalogues with mock performance (arXiv:2004.01448). The
  correlation lengths, noise floor, map variance and finder thresholds are absent. **P.**
- L3: pixel selection (arXiv:1710.02894, Sect. IV; arXiv:2002.10676, Sect. VIII), coordinates,
  the Wiener operator and solver (Eqs. 2–3; arXiv:1412.1507, App. A.3), a prior-parameter table
  for four maps, map variance (Eqs. 4–5; arXiv:2002.10676, Eq. 3), mock validation by survey,
  void and protocluster finders with thresholds and purity (arXiv:1504.03290, Table 1;
  arXiv:2507.10948, Sect. III), Wiener against ORCA, TARDIS, HMC and learned maps. **Y.**

**F7 (control, HCDs and metals in 3D).** L2 (syst B1–B2, with methods §4.2): masking with three
finders and their purity (arXiv:2503.14740), the Voigt F_HCD model and its test
(arXiv:1711.06275; arXiv:2506.13005), L_HCD and the metal matrix with the peak positions,
metal-bias sizes (arXiv:2503.14739). **Y.** L3 (`validation-mocks-blinding`): how mocks insert
the same contaminants. **Y**, no gain needed.

**F8 (control, IGM thermal state).** L2 (methods §§1.2–1.3, 7): the FGPA and T = T_0 Δ^(γ−1)
(arXiv:astro-ph/9612232), the line-width cut-off method (arXiv:astro-ph/9912432), P1D
sensitivity to T_0 and the pressure history, the mean-flux–T_0–γ degeneracy. Curvature and
wavelet statistics are not named; how each statistic is calibrated is absent. **P.** L3
(`p1d-emulators`): T_0 and γ as emulator nuisances, the A_Lyα–T_0 anticorrelation and the
mean-flux prior (arXiv:2412.05372, Sect. 5.3.1); no thermal-statistics method. **P**, no gain.

### Grades

| Q | L2 (a) | L3 (a) | L3 locator | Gain |
|---|---|---|---|---|
| F1 | P | Y | Y | yes |
| F2 | Y | Y | Y | — |
| F3 | Y | Y | Y | — |
| F4 | P | Y | Y | yes |
| F5 | P | Y | Y | yes |
| F6 | P | Y | Y | yes |
| F7 (c) | Y | Y | Y | — |
| F8 (c) | P | P | Y | no |

**Verdict: pass.** L3 answers 6 of 6 with locators; 4 L2 failures answered (F1, F4, F5, F6);
one dossier per question; controls inert. The P1D estimator and emulator questions are
answered at L2 by `physics-and-methods.md` §§3, 6–7, which already carry the DR1 equations
and the emulator table; the two P1D dossiers add depth but no gain.

### Source check (1 used)

- **E4** `deep/validation-mocks-blinding.md`, Step 5 (Metals): the four silicon lines "give
  peaks at r_∥ = 104, −21, −54, −61 h⁻¹Mpc (Si II 1260, Si III 1207, Si II 1193, 1190) at
  z = 2.35 by Eq. 2 of arXiv:2401.00303". arXiv:2401.00303, Sect. 2.3.3: printed so; but the
  same paper's Sect. 4.3 gives −59, −52, 104 and −21 h⁻¹Mpc for Si II 1190, Si II 1193,
  Si II 1260 and Si III 1207 "calculated using equation 2" at z_eff = 2.37. Eq. 2,
  r_∥ = (1 + z) D_H Δλ/λ_Lyα, gives about −52 (1193) and −59 (1190) at z = 2.35 [der: flat
  ΛCDM, Ω_m = 0.315], matching Sect. 4.3 and `methods` §4.2 (|Δr_∥| ≈ 52, 59), not 54 and 61.
  The dossier copies the paper's inconsistent Sect. 2.3.3 values without flagging them.

### Generality flags

- `deep/p1d-estimation.md` covers the DESI DR1 and eBOSS pipelines only; the high-resolution
  P1D measurements (KODIAQ, XQ-100, HIRES/UVES) and their estimation choices are absent, and
  the dossier says so ("Not verified": whether high-resolution pipelines use the same
  treatment). For the small-scale P1D behind WDM and thermal constraints those analyses carry
  the field's weight.
- `deep/validation-mocks-blinding.md` is, by its subject, DESI-only (LyaCoLoRe, Saclay,
  CoLoRe-2LPT, quickquasars); acceptable because DESI is the only current 3D Lyα analysis, but
  the eBOSS-era mock and validation practice of other groups is not described.
- `deep/tomography-voids.md` is now balanced: CLAMATO, LATIS and Stripe 82 each have a column,
  and ORCA, TARDIS, HMC and DeepCHART are compared with the Wiener filter. No flag.

## cosmo-clusters

### Files loaded

| Q | L2 reference file | L3 dossier |
|---|---|---|
| K1 | syst | `deep/optical-selection-projection.md` |
| K2 | syst | `deep/x-ray-selection-function.md` |
| K3 | syst | `deep/sz-selection-function.md` |
| K4 | methods | `deep/cmb-cluster-lensing.md` |
| K5 | methods | `deep/cluster-clustering.md` |
| K6 | methods | `deep/gas-mass-fraction.md` |
| K7 (control) | syst | `deep/optical-selection-projection.md` (closest: Step 4, selection bias of stacked lensing) |
| K8 (control) | open | `deep/cmb-cluster-lensing.md` (closest: Step 6, "Why not a mass ratio") |

### Answers

**K1 — Projection effects on richness: model, calibration, lensing bias; DES, KiDS, HSC.**
- L2 (syst §§8, 13): mechanism, the size estimate growing from ≤ 5% (arXiv:1303.3562) to a
  0.05 S8 bias without projection (arXiv:1807.07072) and 20–30% on DES Y1 masses
  (arXiv:2002.11124, Sect. III.3), simulated boosts (arXiv:2002.03867; arXiv:2203.05416),
  spectroscopic 16% (arXiv:2011.07070), SPT confirmations (arXiv:2101.04984), the mitigation
  list; DES Y1 richness model and projection systematic (Sect. IV.1, App. B), DES Y3 empirical
  scale-dependent model (arXiv:2503.13632, Sect. III.2), KiDS σ_OP = 0.03 (arXiv:2507.14285,
  Eqs. 44–46), SDSS + HSC Y3 boost model at 0.816 (arXiv:2309.13025). How the projection
  kernel in P(λ|M) is built and calibrated, the formalism of the lensing bias and the
  scale-cut contrast are absent. **P.**
- L3: P(λ^ob|λ^true) convolution and λ^ob = λ^true + Δ^bkg + Δ^prj (arXiv:1807.07072, Eqs. 1–3),
  injection calibration (Sect. 3.1, Eqs. 5–6), correlated projections with kernel and
  percolation (Eqs. 4, 13–15), KiDS SinFoniA data-driven route (arXiv:2507.14285, Sect. 3,
  Eqs. 2–3, 22–23), the bivariate selection-bias formula (arXiv:2203.05416, Eq. 8), six model
  families in a table: DES Y1 correction, Π(R) boost used for SDSS + HSC Y3 (arXiv:2112.09059,
  Eqs. 14–16), DES Y3/Y6 ratio (arXiv:2503.13631, Eq. 23), analytic, Euclid post-processing,
  simulation-based; scale cuts KiDS 0.4–3.5 against DES > 2 h⁻¹Mpc (Sect. III.0.5); SZ and
  DESI validation (arXiv:2502.12914, Sects. 3–4; arXiv:2506.06249). HSC enters only through
  SDSS redMaPPer with HSC lensing; the HSC finder CAMIRA is listed as not read. **Y.**

**K2 — X-ray selection function: simulated sky, count rate and extent, contaminants;
validation.**
- L2 (syst §§5, 13): mechanism (core state, morphology, exposure, point sources), simulated
  skies named (arXiv:2402.08457), optical confirmation at ≈ 95% purity (arXiv:2402.08452), the
  eRASS1 contaminant mixture priors (arXiv:2402.08458, Table 1), cross-matches with SPT-3G and
  AMICO as validation. How the twin is built, which variables the selection depends on, the
  classifier and the validation tests are absent. **P.**
- L3: L_det, L_ext cuts (arXiv:2402.08457, Sect. 3.1), the UNIT1i–SIXTE–eSASS twin
  (Sect. 3.2), photon against positional matching (Sect. 3.3.3), Θ_sel = (CR, z, H) with the
  count-rate formula and its reasons (Sect. 5.3, Eq. 7; arXiv:2402.08458, Sect. 2.2), GP
  classifier set-up (Sect. 3.3), the logistic surface-brightness model with AGN dependence
  (arXiv:2402.08457, Sect. 4.2, Eq. 5), the count integral and mixture model
  (arXiv:2402.08458, Eqs. 7–11), XXL (CR, θ_c) selection (arXiv:2109.13171, Sect. 3.2.2),
  internal precision–recall and external eFEDS/SPTpol tests with their failures
  (arXiv:2402.08457, Sects. 5.4, 6.1–6.5), AGN-peaked clusters (arXiv:2301.11196). **Y.**

**K3 — SZ selection: matched filter, observed against unbiased significance, optimisation
bias; completeness and purity.**
- L2 (syst §§6, 13): contamination sizes (dust, radio, relativistic, CIB), purity values
  (arXiv:1502.01598; arXiv:2607.01175), Planck matched filter with the Arnaud profile and θ500
  range (arXiv:1502.01597, Sect. 2), SPT ξ > 5 sample ≳ 95% pure (arXiv:2401.02075,
  Sect. II.1). The ξ–ζ relation, optimisation bias and how completeness is computed are
  absent. **P.**
- L3: filter equation and per-experiment template and scales (arXiv:2009.11043, Eqs. 1–2;
  arXiv:2311.07512, Eq. 1, Sect. 3), iterative noise covariance (arXiv:2408.06189,
  Sect. 3.3.5; arXiv:2507.21459, Sect. 2.2.2), optimal against fixed-scale observables
  (arXiv:2009.11043, Sect. II.3), SPT P(ξ|ζ) = N(√(ζ²+3), 1) (arXiv:2310.12213, Eqs. 40–43),
  Planck ERF completeness (arXiv:1502.01597, Eqs. 3, 5, 10, 14), ACT completeness with
  optimisation-bias correction p = 2.1 (arXiv:2507.21459, Eqs. 4–10, App. B), purity from tSZ
  simulations and MCMF confirmation (arXiv:2311.07512, Sect. 6.4; arXiv:2310.12213,
  Sect. II.1), validation by injection and end-to-end skies, the cost of ignoring the bias
  (arXiv:2106.03718, Sect. 3.4.2; arXiv:2408.06189, Sect. 9.2). **Y.**

**K4 — CMB-lensing cluster mass: estimator, gradient cleaning; tSZ, kSZ, miscentring.**
- L2 (methods §6 table): the principle (distortion of the CMB gradient, no source redshifts),
  precisions reached (arXiv:2009.07772; arXiv:2111.07491; arXiv:1904.07887), the limitation
  "contamination of the estimator by the cluster's own SZ signal" (arXiv:2404.02153). No
  estimator, no gradient treatment, no kSZ or miscentring handling; syst "Not verified"
  points to the dossier. **N.**
- L3: signal size (arXiv:2305.06326, Sect. 2), QE with band-limited gradient l_f = 2000
  (arXiv:1904.07887, Eqs. 5–9, 13; arXiv:2009.07772, App. A, Eq. A1), MV QE on joint maps
  (arXiv:2402.18346), rotated stack in six steps (arXiv:2404.02153, Sect. 3.1, Eqs. 1–4), MLE
  (arXiv:1705.00411, Eqs. 4–5), gradient inversion (arXiv:1710.10236), mean field
  (arXiv:2009.07772, App. A), five tSZ treatments with costs, kSZ in stack against
  per-cluster fits (arXiv:1705.00411, Sect. 4.5; arXiv:2402.18346, Sect. 6.1), miscentring
  model in Fourier space (arXiv:2404.02153, Eq. 5) and its sizes (arXiv:1904.07887,
  Sect. 4.3.3; arXiv:2305.06326, Sect. 5.3.1), estimator comparison (arXiv:2305.06326,
  Sect. 5.2). **Y.**

**K5 — Clustering added to counts: statistic, halo-bias model, counts–clustering
covariance; self-calibration gained.**
- L2 (methods §§3, 5, 7): statistics in use per analysis (arXiv:2402.08460; arXiv:2302.14074;
  arXiv:2310.12224; arXiv:2610.08947; arXiv:2503.13632), P_cc = b² P_m with Tinker 2010
  (arXiv:1001.3162), counts and clustering uncorrelated in Euclid-like mocks
  (arXiv:2510.13509), gains: the forecasts (arXiv:astro-ph/0305341; arXiv:2510.13509;
  arXiv:2510.14464) and (1 − b) = 0.62 from Planck clustering (arXiv:2302.14074). How the
  effective bias is integrated through the observable–mass relation, which bias model each
  analysis uses, and a data-side self-calibration other than Planck's are absent. **P.**
- L3: selection-carrying randoms (table, arXiv:2402.08460, Sect. 2.2), Landy–Szalay and w_p
  choices with π_max (Sects. 3; arXiv:2610.08947, Sect. III), effective-bias integrals
  (arXiv:2610.08947, Eqs. 11, 13; arXiv:2302.14074, Eqs. 13–17), Aemulus against Tinker
  against HOD with reasons (arXiv:2610.08947, Sect. IV.2; arXiv:2503.13631, Sect. II.3.2;
  arXiv:2402.08460, Sect. 3.1.2), RSD and photo-z terms, covariance table, combination with
  counts (XXL as an extra Gaussian term, arXiv:2109.13171, Sect. 4.2), self-calibration
  numbers: SPT-3G ln A_SZ = 0.43 +0.17/−0.21 from clustering (arXiv:2610.08947, Sect. VII.1),
  Planck (1 − b_SZ) variants, Euclid scale-range ΔFoM (arXiv:2510.13509, Table 4). The
  counts–clustering covariance rests on the L2 statement. **Y.**

**K6 — f_gas: relaxed selection, shell, lensing calibration, depletion; weight of the
priors.**
- L2 (methods §8): principle (d^1.5, Ω_b/Ω_m, Sasaki 1996), SPA selection 57 of 361
  (arXiv:1502.06020), r2500, lensing/hydrostatic ratio 0.96 (arXiv:1509.02162), depletion from
  simulations (arXiv:0706.0033; arXiv:1402.6212). Shell, model equation, prior values and
  how much the priors drive the result are absent. **P.**
- L3: SPA statistics and cuts (arXiv:1502.06020, Sect. 5.4), semi-parametric hydrostatic fit
  and blinding (arXiv:1402.6212, Sect. 2.3), shell 0.8–1.2 r2500 with reasons (Sect. 3.1),
  2022 model (arXiv:2111.09343, Eqs. 1–6), depletion prior U(0.71, 0.87) with the corrected
  centre and its posterior equal to the prior (Sect. 3, Table 7), K0 from 12 WtG clusters and
  W(z) (Sects. 2.3, 3, 4.5), model history table, shape-only Ω_m = 0.200 ± 0.044
  (Sect. 4.2), clumping cost, the inverse use for the hydrostatic bias (arXiv:2204.12823,
  Eq. 6; arXiv:1805.00034). **Y.**

**K7 (control, weak-lensing mass calibration).** L2 (syst §§1–3, 13): NFW-fit bias and
scatter (arXiv:1011.1681; arXiv:2409.02783), the Grandis shear-library method
(arXiv:2103.16212), radial ranges, member dilution by boost factor or P(z) decomposition
(arXiv:2512.18935, Sect. 3.4), two-component miscentring (arXiv:1901.07119), budgets per
analysis (eRASS1, SPT, DES Y1, KiDS, HSC). **Y.** L3 (`optical-selection-projection`):
selection bias of richness-selected stacks. **Y**, no gain needed.

**K8 (control, 1 − b).** L2 (open §§3, 5): values by route (lensing of the Planck scale,
CMB lensing, clustering, simulations and X-COP, CMB requirement, Planck × DES against Chandra;
arXiv:1402.2670; arXiv:1904.07887; arXiv:2302.14074; arXiv:2409.07849; arXiv:2403.19542;
arXiv:2509.02068), reasons for disagreement: temperature weighting (arXiv:2404.08539),
Chandra–XMM reference (arXiv:2402.04006), mass and redshift trends. **Y.** L3
(`cmb-cluster-lensing`, Step 6): the ratio-estimator bias under SZ selection behind 0.99
against 1.41 (arXiv:1904.07887, Sects. 5, 8). **Y**, no gain needed.

### Grades

| Q | L2 (a) | L3 (a) | L3 locator | Gain |
|---|---|---|---|---|
| K1 | P | Y | Y | yes |
| K2 | P | Y | Y | yes |
| K3 | P | Y | Y | yes |
| K4 | N | Y | Y | yes |
| K5 | P | Y | Y | yes |
| K6 | P | Y | Y | yes |
| K7 (c) | Y | Y | Y | — |
| K8 (c) | Y | Y | Y | — |

**Verdict: pass.** L3 answers 6 of 6 with locators; 6 L2 failures answered; one dossier
per question; controls inert. `physics-and-methods.md` and `systematics.md` give sizes and
names but no estimator or selection construction; the CMB-lensing method is absent from L2
altogether (K4, N).

### Source checks (2 used)

- **E5** `deep/optical-selection-projection.md`, Step 4 (c), used in K1: "the cluster
  autocorrelation ratio is its square (Eq. 23)". arXiv:2503.13631, Sect. II.3.5, Eq. 23: the
  lensing ratio equals b_s1 + b_s2 exp(−θχ/r0), equals the w_cg ratio, and equals
  √(w_cc ratio); "contributes twice to the cluster clustering signal leading to a quadratic
  boost". Match. `deep/cluster-clustering.md`, Step 5, says the same paper uses "its square
  root for w_cc" and that "the square root comes from" the quadratic boost: the w_cc ratio is
  the square of the lensing ratio, not its square root. The two dossiers disagree; the
  clustering one misreads the √ in Eq. 23.
- **E6** `deep/gas-mass-fraction.md`, Step 5, used in K6: depletion prior centred on 0.79
  after a "misinterpretation", width 20%, posterior reproducing the prior. arXiv:2111.09343,
  Sect. 3: "centering the prior at Υ0 = 0.79, maintaining the full width of 20 per cent (2.3
  times the difference between the two simulations)"; Table 7: Υ0 U(0.71, 0.87) marked as a
  prior whose posterior "essentially reproduces the prior". Match.

### Generality flags

- `deep/gas-mass-fraction.md` rests on one group's relaxed-cluster series: of about 75
  citations, 61 are to arXiv:2111.09343, arXiv:1402.6212, arXiv:1502.06020, arXiv:0706.0033
  and arXiv:1509.02162 (Allen, Mantz and collaborators). The X-COP and Planck-ESZ analyses
  appear only for the inverse use (hydrostatic bias); no f_gas cosmology analysis by another
  group is described, and the dossier does not say whether one exists.
- `deep/optical-selection-projection.md` is DES-heavy (arXiv:2503.13631, arXiv:1807.07072,
  arXiv:2510.25706, arXiv:2502.12914, arXiv:2510.00753 together 42 citations), with KiDS
  AMICO (10) and Euclid (5) as the alternatives; HSC CAMIRA and the Euclid finders are under
  "Not verified", so the HSC part of K1 rests on SDSS redMaPPer with HSC lensing.
- `deep/x-ray-selection-function.md` is mostly eRASS1 (44 of about 67 citations), with XXL
  as the comparison; acceptable, since Steps 1–5 set the two side by side.
- `deep/cmb-cluster-lensing.md`: SPT papers carry the largest share (arXiv:1705.00411,
  arXiv:2305.06326, arXiv:2404.02153, arXiv:2111.07491), with ACT and Planck each cited about
  16 times and a Planck + SPT analysis; balanced across three experiments. No flag.
