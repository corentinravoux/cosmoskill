# Level test — second L3 test of 2026-10-20

Item C of `docs/plans/2026-10-20-plan.md`. Five skills: `cosmo-statistics-inference`
(failed the pilot's "beats L2" clause; now six dossiers), `cosmo-cmb`,
`cosmo-weak-lensing`, `cosmo-supernovae`, `cosmo-bbn`. Forty questions, eight per
skill, are in `docs/tests/levels/l3-questions-2.md`. Each was answered twice from the
skill files only: an **L2 run** (the skill's `SKILL.md` plus one reference file chosen
from the file map) and an **L3 run** (the same plus at most one dossier of `deep/`,
chosen from the file map). Model memory was not used to fill gaps. This run tests; no
skill file was changed. `cosmo-lyman-alpha` was not used.

The run was cut by a usage limit after `cosmo-cmb` and resumed; the questions file was
already written and committed and was not changed. Source checks after the resumption
were limited to 10 by the coordinator; 9 were used in all.

## Procedure

1. **Questions first.** Written from the five `subtopics.tsv` files, the file names of
   `deep/` and `references/`, and the one-line skill descriptions of the skill listing,
   before any `SKILL.md` body, reference file or dossier of the five skills was opened.
   Per skill, six questions fall one each on the six dossier subtopics and two on
   subtopics whose `files` column lists no dossier (controls).
2. **Preliminaries read.** The pilot run and its questions, the level table of
   `skills/observational-cosmology/SKILL.md` ("Choosing the level"), `docs/layers.md`.
   Layer check: no `.cosmoskill/` in the working directory, its parents or the home
   directory; `COSMOSKILL_HOME` unset; layer `base` for every question.
3. **Isolation.** One session answered all questions: each file was read once and each
   answer was then restricted to the passages of the files assigned to that run. As in
   the pilot this is weaker than a fresh session per run; every L2 grade names the
   passage it rests on.
4. **Grading.** (a) Y answers, P partly, N not; (b) locator: Y when the load-bearing
   statements carry paper + section, table or equation. **Tightened rule** (pilot
   recommendation 3): an L2 answer graded P counts as an L2 failure.
5. **Pass rule per skill.** The L3 run answers (Y) at least 5 of the 6 dossier questions
   with locators, including at least 3 that the L2 run failed (P or N); each L3 question
   loads at most one dossier. Controls should show no L3 gain.
6. **Source checks.** At most 15 in all (`fetch_paper.py --grep` or `--section`); the
   coordinator lowered the budget to 10 after an interruption.

## Files loaded per question

`methods` = `references/physics-and-methods.md`, `syst` = `references/systematics.md`,
`open` = `references/open-questions.md`, `surveys` = `references/surveys-and-data.md`.
Every run also loaded the skill's `SKILL.md`.

| Q | L2 reference file | L3 dossier |
|---|---|---|
| S1 | methods | `deep/likelihood-form.md` |
| S2 | methods | `deep/covariance-estimation.md` |
| S3 | methods | `deep/profile-likelihoods.md` |
| S4 | methods | `deep/model-comparison.md` |
| S5 | methods | `deep/tension-metrics.md` |
| S6 | syst | `deep/pipeline-validation.md` |
| S7 (control) | methods | `deep/covariance-estimation.md` (row "Building, correcting, validating a covariance": χ² of mocks) |
| S8 (control) | methods | `deep/pipeline-validation.md` (closest row; no blinding row) |
| C1 | syst | `deep/beams-calibration-polarisation.md` |
| C2 | methods | `deep/high-ell-likelihoods.md` |
| C3 | methods | `deep/component-separation.md` |
| C4 | methods | `deep/low-ell-polarisation-tau.md` |
| C5 | methods | `deep/lensing-reconstruction.md` |
| C6 | methods | `deep/damping-tail-light-relics.md` |
| C7 (control) | methods | `deep/high-ell-likelihoods.md` (row covers masks, mode coupling, filtering) |
| C8 (control) | open | `deep/high-ell-likelihoods.md` (likelihood choice; no A_L row) |
| W1 | methods | `deep/two-point-statistics.md` |
| W2 | syst | `deep/shear-calibration.md` |
| W3 | syst | `deep/intrinsic-alignments.md` |
| W4 | syst | `deep/baryonic-feedback.md` |
| W5 | methods | `deep/blinding-consistency.md` |
| W6 | methods | `deep/ggl-3x2pt.md` |
| W7 (control) | syst | `deep/ggl-3x2pt.md` (lens n(z), shear ratio; no redshift row) |
| W8 (control) | syst | `deep/shear-calibration.md` (closest row; no PSF row) |
| N1 | methods | `deep/photometric-calibration.md` |
| N2 | methods | `deep/light-curve-models.md` |
| N3 | methods | `deep/dust-intrinsic-scatter.md` |
| N4 | methods | `deep/selection-bias-corrections.md` |
| N5 | methods | `deep/covariance-likelihood-blinding.md` |
| N6 | surveys | `deep/stage-iv-photometric-samples.md` |
| N7 (control) | methods | `deep/dust-intrinsic-scatter.md` (row "dust/scatter model": mass step) |
| N8 (control) | methods | `deep/stage-iv-photometric-samples.md` (row "photometric Rubin/Roman": classification) |
| B1 | methods | `deep/nuclear-reaction-rates.md` |
| B2 | methods | `deep/bbn-codes.md` |
| B3 | syst | `deep/deuterium.md` |
| B4 | syst | `deep/helium-4.md` |
| B5 | methods | `deep/baryon-density.md` |
| B6 | methods | `deep/neff-new-physics.md` |
| B7 (control) | methods | `deep/bbn-codes.md` (row "weak-rate corrections": τ_n normalisation) |
| B8 (control) | open | none: no file-map row |

Every L3 run loaded at most one dossier (B8 none).

## Answers, cosmo-statistics-inference

**S1 — Gaussian likelihood at low multipoles; alternatives; test.**
- L2 (methods §1): where it fails (few modes, large angles, small areas, counts), the
  exact Wishart and Hamimeche–Lewis forms (arXiv:0801.0554, Sect. 3.5), lognormal and
  WMAP forms, documented sizes (arXiv:1803.06348; arXiv:1905.03779; arXiv:2012.06267).
  How to test a given data vector is not in the file (it is in `syst` §4, not loaded).
  **P.**
- L3: one-point skewness against 2/√N_k in the whitened basis (arXiv:2604.01309,
  Sects. 3.2, 4), pairwise MISE with Gaussian calibration runs (arXiv:1707.04488,
  Sect. 2), k-NN divergence against a Gaussian null (arXiv:1803.06348, Sect. III),
  hold-out KS/MMD (arXiv:1905.03779, Sect. 4); Edgeworth, GMM, ICA+KDE, learned
  likelihoods; importance reweighting; head-to-head table. **Y.**

**S2 — Fixed or parameter-dependent covariance; iteration; bias.**
- L2 (methods §1): fixed covariance required inside a Gaussian likelihood
  (arXiv:1204.4724), iterate at the best fit (arXiv:0810.4254), bias ≤ O(10%) of σ
  (arXiv:1811.11584). **Y.**
- L3: adds DES Y3's 100-cosmology test, extra best-fit scatter of 3–5% that iteration
  does not remove (arXiv:2012.08568, Sect. 2), DES Y6 recomputing at the blind MAP. **Y.**

**S3 — Wilks or Neyman; toys.**
- L2 (methods §§7.1–7.2): the three Wilks conditions, Planck-lite findings per model
  (arXiv:2408.07700). How toys are generated and how many: not in the file. **P.**
- L3: decision rule (arXiv:2408.07700, Sects. II.2–II.3), the three mock checks and
  their staging with 250, 3 × 100, 100–200 mocks drawn from the published covariance
  (Sects. III.7, VI), DESI DR1 100-realisation coverage test with binomial error
  (arXiv:2508.11811, App. A). **Y.**

**S4 — Computing the evidence; accuracy; prior sensitivity.**
- L2 (methods §§5.1, 8): nested sampling, Savage–Dickey ratio, linear prior-volume
  dependence, Ockham factor, MultiNest inconsistency (arXiv:2202.08233). No learned
  harmonic mean, no accuracy check beyond one sampler comparison, no quantified prior
  sensitivity. **P.**
- L3: SDDR conditions and procedure (arXiv:2506.04339, Sect. 2.2; arXiv:astro-ph/0504022,
  Eqs. 7–9, App. C), estimator comparison including learned harmonic mean
  (arXiv:2506.04339, Tables 3–4), fit/Ockham split (arXiv:2503.14743, Eq. 21, Table 4),
  prior widening on identical data (arXiv:2609.04334, Sect. IV.1). **Y.**

**S5 — Tension metric for correlated data; subspace.**
- L2 (methods §9): rule (ii), Q_UDM with KL-mode selection 0.2 < λ − 1 < 100
  (arXiv:2012.09554, Eq. 17), posterior predictive tests (arXiv:2011.03410),
  subspace rule (i). **Y.**
- L3: adds the conditional-Gaussian PPD for disjoint correlated parts (arXiv:2610.03447,
  Sects. 2.2–2.3), why non-shared parameters drop out (arXiv:2105.03324, Sect. II.1),
  choice list. **Y.**

**S6 — Pipeline validation and pass criterion.**
- L2 (syst §§5, 16): noiseless vector through the full pipeline, DES Y6 pre-registered
  1σ caveat and 0.5σ pulls (arXiv:2601.14559), ACT DR6 0.5σ foreground rule
  (arXiv:2503.14452). Contaminated vectors and how a threshold is set: not in the file.
  **P.**
- L3: MAP recovery (arXiv:2007.01844, Sect. 7), two-code Δχ² < 0.2 floor, 0.3σ_2D and
  Δχ² < 1 with the budget reason (arXiv:2105.13548, Sects. IV.1, V), stacked σ/3
  (arXiv:2503.14741, Sect. IV.1), noise calibration of variant shifts
  (arXiv:2305.17173, App. F). **Y.**

**S7 (control, goodness of fit).**
- L2 (methods §9): N_eff = N − tr[C_Π⁻¹C_p] (arXiv:1806.04649, Eq. 21) inside the
  Q_DMAP row; PPD named. No procedure for a single-data-set χ². **P.**
- L3 (`covariance-estimation`): KiDS-1000 χ²_min distribution, three N_Θ,eff estimators
  and α_p (arXiv:2007.01844, Sect. 6.3, Eqs. 44–46, Table 4), DES Y3 ⟨χ²⟩ = 507.6.
  **Y. The control was not inert**: the covariance dossier serves `goodness-of-fit`.

**S8 (control, blinding).**
- L2 (methods §4): level table with strengths and weaknesses, requirements a scheme must
  meet. Which tests and criteria are fixed: only generic. **P.**
- L3 (`pipeline-validation`): points to blinding lists in other skills; no gain. **P.**

## Answers, cosmo-cmb

**C1 — Beam errors and calibration in the likelihood.**
- L2 (syst §§1–3): beams on planets, decomposed into modes, covariance or nuisance;
  cross-calibration to Planck; efficiency degenerate with Ω_c h². No eigenmode
  construction, no efficiency procedure. **P.**
- L3: ACT 10 + 3 beam modes (arXiv:2112.12226, Sect. IV.6), SPT nine sampled eigenmodes
  (arXiv:2506.20707, Sect. V.2.1, Eq. 43), Planck ignoring beam error (arXiv:1907.12875,
  Sect. 3.3.5); calibration estimators (arXiv:2503.14452, Sect. V.3, Eq. 15); efficiency
  from TT best fit or free (arXiv:1907.12875, Sect. 3.3.4, Eq. 44). **Y.**

**C2 — Plik, CamSpec or HiLLiPoP.**
- L2 (methods §§4–6, 10): ℓ ranges, nuisance counts, likelihood form, Jense et al.
  (arXiv:2510.09430). Foreground strategy of CamSpec and TE treatment: not in the file.
  **P.**
- L3: splits, masks, ℓ cuts with reasons (arXiv:1907.12875, Sects. 3.2.1–3.2.4;
  arXiv:2205.10869, Sects. 3.2–3.3; arXiv:2309.10034, Sect. 3.2), templates against
  spectrum-level cleaning (arXiv:2205.10869, Eq. 1), full- versus cut-range shifts
  (arXiv:2510.09430, Sects. III.2.2–III.2.3). **Y.**

**C3 — Choosing a component-separation method; residuals.**
- L2 (methods §5): four method papers and their uses. How to choose for a use and how to
  quantify residuals: not in the file. **P.**
- L3: pipeline-by-purpose table and validation table (arXiv:1807.06208, Sects. 4.2–4.10,
  6), NILC ILC bias and deprojection (arXiv:2307.01258, Sect. III.3.2, App. C),
  spectral ILC (arXiv:2509.10604). **Y.**

**C4 — τ from low-ℓ EE; systematics; prior without Planck large scales.**
- L2 (methods §6): SimAll, LoLLiPoP, momento/density estimation, τ inputs of ACT and
  SPT, "single-point failure" (arXiv:2504.16932). Dominant systematics and prior choice:
  not in the file. **P.**
- L3: full SimAll and SRoll2 recipes (arXiv:1907.12875, Sect. 2.2.3; arXiv:1908.09856,
  Sect. 4), NPIPE transfer function (arXiv:2007.04997, Sect. 4.3), within-band bias
  (arXiv:2103.14378, Sect. 7), CLASS × Planck (arXiv:2501.11904). The choice of a τ
  prior when Planck large scales are not used is answered only by the ground-based
  CLASS value; the dossier gives no rule. **P.**

**C5 — N0, N1, mean field; foregrounds.**
- L2 (methods §3): RDN0 from noiseless simulations, N¹ from pairs sharing φ, mean field,
  MC term, bias hardening and gradient cleaning (arXiv:2304.05202; arXiv:2608.31136,
  Eqs. 23–27). **Y.**
- L3: adds counts and formulae (arXiv:2304.05202, App. E), semi-analytic N⁰, N^MFcorr,
  cross-split estimator, hardening variants compared. **Y.**

**C6 — N_eff and Y_P from the damping tail.**
- L2 (methods §§2, 7): BBN consistency against free Y_P, damping ratio and phase shift
  (arXiv:1104.2333; arXiv:astro-ph/0310198). Degeneracy direction and forecast limits:
  not in the file. **P.**
- L3: θ_d/θ_s ∝ H^0.5 (arXiv:1104.2333, Sect. II.2, Eq. 1), four symmetry-breaking
  causes (arXiv:2210.16335, Sect. V), N_eff–Y_P anticorrelation with ACT numbers
  (arXiv:2503.14454, Eq. 46), phase-shift templates and forecasts (arXiv:2501.13788),
  foreground and chromatic-beam biases. **Y.**

**C7 (control, maps and band powers).** L2 (methods §4): ACT transfer matrix from 800
simulations, SPT 500 + 4000 simulations, MASTER relation and NaMaster. **Y.** L3 adds
reasons (SPT ℓ_min = 400, ACT neglect of filter ℓ–ℓ′ coupling). **Y**, no gain needed.

**C8 (control, A_L).** L2 (open §2): definition, history, likelihood dependence, the
reconstruction comparison (arXiv:1912.06601), reporting rule. **Y.** L3: no A_L
content. **Y**, no gain.

## Answers, cosmo-weak-lensing

**W1 — Choosing ξ±, COSEBIs, band powers, pseudo-Cℓ; comparing them.**
- L2 (methods §3): statistic table with E/B properties, ℓ support, KiDS and UNIONS
  comparisons named. How the expected difference is computed: not in the file. **P.**
- L3: fine-binning, bin-averaged theory, scale-cut rules per statistic
  (arXiv:2203.07128, Sect. 3.5; arXiv:2011.06469, Eq. 17), expected ΔS8 from joint mocks
  (arXiv:2007.15633, App. B.1; arXiv:2605.13543, Sect. 5.3). **Y.**

**W2 — m from metacalibration/metadetection or simulations; blending; prior.**
- L2 (syst §§1–2): both families, per-analysis m and how it enters, blending F(z), G(z)
  (arXiv:2105.13543, Eq. 22). **Y.**
- L3: step-by-step routes A–D (arXiv:1702.02601, Eqs. 10–14, 25; arXiv:2501.05665,
  Sect. 4.1; arXiv:2210.07163, Sects. 5.1–5.2), design choices. **Y.**

**W3 — NLA or TATT; priors; S8.**
- L2 (syst §5): models, per-analysis priors and posteriors, S8 under alternatives,
  evidence ratio (arXiv:2602.10065, Sect. VII.3.1). **Y.**
- L3: normalisation conventions (arXiv:1708.09247, Eqs. 40, 42), NLA-M and blue-null
  prior recipes (arXiv:2503.19441, App. B; arXiv:2512.04209, App. B), calibrated Δχ²
  model selection (arXiv:2211.02800). **Y.**

**W4 — Scale cuts or baryon model.**
- L2 (syst §6): per-analysis feedback model, cut rule (OWLS-AGN, 0.3σ, Δχ² < 0.5;
  BAHAMAS, 0.5σ) and S8 shifts. **Y.**
- L3: DES Y3/Y6 procedure and budget (arXiv:2601.14859, Sects. III.1, VI.1–VI.2),
  HMcode-2020 calibration range (arXiv:2009.01858, Sects. 6.3–6.4), emulators. **Y.**

**W5 — Internal-consistency tests and pre-unblinding criteria.**
- L2 (methods §§5.1, 6–7): KiDS three tiers named, DES Δ_PPD > 0.01, blinding table.
  How correlated subsets are handled and what each tier computes: not in the file. **P.**
- L3: KiDS tiers with split models and the conditional TPD (arXiv:2503.19442, Eqs. 4–19),
  DES Y6 stage list with exemption (arXiv:2601.14559, Sect. IV.8, App. A.1), HSC
  criteria (arXiv:2304.00705, Sect. IV). **Y.**

**W6 — Point mass, magnification, non-linear bias.**
- L2 (methods §5): point-mass "analytic marginalisation" named, magnification one
  coefficient per bin with prior, R_min for linear or non-linear bias. How the
  marginalisation works and the alternatives: not in the file. **P.**
- L3: PM marginalisation with the covariance update (arXiv:2105.13541, Eqs. 29–34),
  Υ/Y-transform/project-out comparison (arXiv:2212.03734, Sect. 5), magnification
  definitions (arXiv:2601.14833, Eqs. 11–13), bias models. **Y.**

**W7 (control, redshift calibration).** L2 (syst §4): SOM, clustering redshifts, shear
ratio, combination, per-analysis priors. **Y.** L3 (`ggl-3x2pt`): adds lens n(z) modes
and the Y6 shear-ratio set. **Y**, no gain needed.

**W8 (control, PSF).** L2 (syst §3): ρ statistics, leakage models per survey, B-mode
PTEs and thresholds. **Y.** L3 (`shear-calibration`): defers PSF to L2. **Y**, no gain.

## Answers, cosmo-supernovae

**N1 — Cross-calibration and its covariance.**
- L2 (methods §9): CALSPEC, tertiary stars, Supercal, Fragilistic (covariance output),
  Dovekie (PS1 + Gaia, filter shifts, DA white dwarfs), joint propagation through
  retraining (arXiv:2609.05053). How the joint fit and its covariance are built, and its
  effect on w: not in the file. **P.**
- L3: Fragilistic equations, priors and floors (arXiv:2112.03864, Sect. III.1, Eqs. 4–5),
  Dovekie three-term posterior with NUTS (arXiv:2506.05471, Eqs. 14–21), filter shifts,
  white-dwarf tie (arXiv:2412.08809), validation by injected offsets and per-survey
  residuals, training-versus-fitting FoM loss (arXiv:2604.19746, Table 5). **Y.**

**N2 — SALT2, SALT3 or BayeSN; training; validity range.**
- L2 (methods §2.3): models with ranges and training sizes, model-choice Δw
  (arXiv:2301.10644), coupling of calibration and training. Training procedure and
  trusted fitting range: not in the file. **P.**
- L3: SALT3 definitions, error model and training (arXiv:2104.07795, Sects. II–V),
  trusted 3000–8000 Å and phase rules (arXiv:2301.10644, Sect. 4.2; arXiv:2311.12098,
  Sect. III.2.1), surface ensembles (arXiv:2506.05471, Eq. 23), SALT against BayeSN
  table (arXiv:2008.07538; arXiv:2606.19429). **Y.**

**N3 — Scatter models in the bias correction; mass step and w.**
- L2 (methods §§3–4): G10/C11, BS21, P23, W22; 4D correction needed for host-dependent
  scatter (arXiv:2102.01776); γ depends on the scatter model (arXiv:2202.04077); BS21
  shifts w by up to 0.04. **Y.**
- L3: colour model and Dust2Dust fit (arXiv:2004.10206, Eqs. 9–15; arXiv:2112.04456,
  Sect. IV.3), variant scoring by Δχ²_S (arXiv:2401.02945, Eq. 13), w biases of the wrong
  model (arXiv:2004.10206, Table 3). **Y.**

**N4 — BBC or forward-modelled selection.**
- L2 (methods §4, §4.1): BBC steps and dimensionalities, UNITY error-function selection,
  25-simulation validation and the 0.7–3.0 data–simulation criterion. **Y.**
- L3: fakes, trigger and E_spec (arXiv:1811.02379, Sects. 4–9), grid rules
  (arXiv:1610.04677, Sect. V.2), Steve's selected-data likelihood (arXiv:1811.02381,
  Eq. 11), volume-limited alternative. **Y.**

**N5 — Systematic covariance, M marginalisation, blinding.**
- L2 (methods §§7, 10): C_syst formula (arXiv:2202.04077, Eq. 7), unbinned gain, budgets
  not additive, blinding per analysis. The M marginalisation is only named. **P.**
- L3: derivative and difference forms (arXiv:1104.1443, Eq. 6; arXiv:2401.02945,
  Eq. 11), analytic 𝓜 marginalisation (arXiv:1104.1443, App. C, Eq. 7), sampler and
  priors, DES-Dovekie unblinding criteria (arXiv:2511.07517, Sect. 6.3). **Y.**

**N6 — Fully photometric Stage-IV sample.**
- L2 (surveys §5): forecast FoMs and remaining biases (arXiv:2512.06319;
  arXiv:2506.04402), calibration requirement. How photo-z and contamination are
  propagated: not in the file. **P.**
- L3: SN + host photo-z fit (arXiv:2512.06319, Eqs. 3–6), classifier on the same
  simulation, D_CC on a 3D grid, no σ_μ^z term and the colour–redshift
  self-correction (arXiv:2407.16744, Sects. 4.7, 5.4), Roman photo-z precision and
  binning comparison (arXiv:2506.04402). **Y.**

**N7 (control, mass step).** L2 (methods §§2.1, 4): sigmoid at 10¹⁰ M⊙, u−r tracer,
4D bias correction including host mass, γ depending on the correction dimension
(arXiv:2001.11294). **Y.** L3 (`dust-intrinsic-scatter`) adds the no-step simulation
and host-tracer choices. **Y**, no gain needed.

**N8 (control, BEAMS and classifier calibration).** L2 (methods §§4, 6): BEAMS mixture
with simulated D_CC (arXiv:2401.02945, Eqs. 3–5), contamination budget
(arXiv:2111.10382). Calibration of classifier probabilities: not in the file. **P.**
L3 (`stage-iv-photometric-samples`): classifier trained on the same simulation, its
calibration checked as true-Ia fraction against P_Ia (arXiv:2506.04402, Sect. IV.3),
D_CC grid. **Y. The control was not inert.**

## Answers, cosmo-bbn

**B1 — d(p,γ)³He and d+d rates; effect on D/H and Ω_b h².**
- L2 (methods §3 and `SKILL.md`): S-factor to rate, ab-initio against data-driven
  against GP, evaluation table, D/H 1.7–2σ low with ab-initio and GP rates, Ω_b h² by
  rate philosophy (arXiv:2401.15054). **Y.**
- L3: rate integral and windows (arXiv:2011.11537, Eqs. 3–4, 12), dataset rules and
  disputed sets (arXiv:2604.16600, Sect. III.3; arXiv:2609.12065, Sect. 2.1), four
  fitting methods with mock biases, same-code D/H table (arXiv:2604.16600, Table 2). **Y.**

**B2 — Code differences and their size.**
- L2 (methods §5): code table, AlterBBN precision remark. Code-to-code numbers are in
  `results.md` §7, not loaded. **P.**
- L3: weak-rate correction ladder (arXiv:1801.08023, Table 5), staged networks,
  aligned-input agreement ≤ 0.15% (arXiv:2408.14538, Table 4), own-rate spread of 4% in
  D/H (arXiv:2208.12600, Table 1). **Y.**

**B3 — D/H from one absorber; combining systems.**
- L2 (syst §1): continuum, interlopers, low N(H I), KHT profile, sample choice (7 against
  13 systems). How systems are combined and the scatter tested: not in the file. **P.**
- L3: Precision Sample criteria (arXiv:1308.3240, Sect. II.2.1), joint model and ties,
  blind restarts, three error practices, intrinsic-scatter likelihood
  (arXiv:1710.11129, Eqs. 3–9), LTS (arXiv:1706.09512, Eq. 2). **Y.**

**B4 — Y_P from H II regions; why groups disagree.**
- L2 (syst §2): fitted parameters, He I 10830, emissivities, WLS against linmix, sample
  effects (EMPRESS, Izotov selection). **Y.**
- L3: target criteria, LBT and YMCMC models (arXiv:2601.22238, Eq. 1; arXiv:2506.24050,
  Eqs. 6–7), screening, three extrapolations, same-data comparison (arXiv:1503.08146,
  Sect. 6). **Y.**

**B5 — BBN prior on Ω_b h² for BAO.**
- L2 (methods §6): likelihood forms, Planck and ACT compressed treatments
  (arXiv:2609.12065). The prior DESI uses and the effect on BAO + BBN: not in the file.
  **P.**
- L3: abundances, theory error, Schöneberg prior (arXiv:2401.15054, Eqs. 4–7), DESI use
  with and without N_eff (arXiv:2503.14738, Eqs. 14–15, 19), Planck's three pipelines
  (arXiv:1807.06209, Eq. 71). **Y.**

**B6 — N_eff from BBN alone and with the CMB.**
- L2 (methods §§1, 6): sensitivities and scalings (arXiv:2303.04140, Eqs. 13–16), the
  product likelihood without a Y_P–η link. Degeneracy and combination: only implied.
  **P.**
- L3: meaning of ΔN_eff and negative values (arXiv:2507.23354), N_ν–N_eff mapping
  (arXiv:1801.08023, Eq. 165), convolution likelihood and Y_P marginalisation
  (arXiv:2207.13133), N_ν ∝ η⁴ at fixed D/H, one-sided limits. **Y.**

**B7 (control, τ_n).** L2 (methods §4): bottle against beam, scaling ≈ 0.0002 in Y_P per
second, BBN + CMB predict 870 ± 16 s, τ_n dominates the Y_P theory error but is below
the observational one. **Y.** L3 (`bbn-codes`) adds normalisation schemes. **Y**, no
gain needed.

**B8 (control, lithium).** L2 (open §4): three solution classes, depletion estimates,
SMC and ω Cen tests. 3D NLTE and the T_eff scale: not in the file. **P.** L3: no
file-map row, answered at L2. **P.**

## Grades

Y answers, P partly, N not. "Gain" means an L2 failure (P or N) that the L3 run
answers (Y). Every L2 and L3 answer above carries locators (paper and section, table
or equation) for its load-bearing statements; no answer was graded N.

| Q | L2 (a) | L3 (a) | L3 locator | Gain | Q | L2 (a) | L3 (a) | L3 locator | Gain |
|---|---|---|---|---|---|---|---|---|---|
| S1 | P | Y | Y | yes | N1 | P | Y | Y | yes |
| S2 | Y | Y | Y | — | N2 | P | Y | Y | yes |
| S3 | P | Y | Y | yes | N3 | Y | Y | Y | — |
| S4 | P | Y | Y | yes | N4 | Y | Y | Y | — |
| S5 | Y | Y | Y | — | N5 | P | Y | Y | yes |
| S6 | P | Y | Y | yes | N6 | P | Y | Y | yes |
| S7 (c) | P | Y | Y | yes (control) | N7 (c) | Y | Y | Y | — |
| S8 (c) | P | P | Y | no | N8 (c) | P | Y | Y | yes (control) |
| C1 | P | Y | Y | yes | B1 | Y | Y | Y | — |
| C2 | P | Y | Y | yes | B2 | P | Y | Y | yes |
| C3 | P | Y | Y | yes | B3 | P | Y | Y | yes |
| C4 | P | P | Y | no | B4 | Y | Y | Y | — |
| C5 | Y | Y | Y | — | B5 | P | Y | Y | yes |
| C6 | P | Y | Y | yes | B6 | P | Y | Y | yes |
| C7 (c) | Y | Y | Y | — | B7 (c) | Y | Y | Y | — |
| C8 (c) | Y | Y | Y | — | B8 (c) | P | P (no dossier) | Y | no |
| W1 | P | Y | Y | yes | | | | | |
| W2 | Y | Y | Y | — | | | | | |
| W3 | Y | Y | Y | — | | | | | |
| W4 | Y | Y | Y | — | | | | | |
| W5 | P | Y | Y | yes | | | | | |
| W6 | P | Y | Y | yes | | | | | |
| W7 (c) | Y | Y | Y | — | | | | | |
| W8 (c) | Y | Y | Y | — | | | | | |

## Verdict per skill

| Skill | L3 answers with locators (need ≥ 5 of 6) | L2 failures answered by L3 (need ≥ 3) | One dossier per L3 question | Controls | Verdict |
|---|---|---|---|---|---|
| cosmo-statistics-inference | 6 | 4 (S1, S3, S4, S6) | yes | S7 gained (covariance dossier serves goodness of fit); S8 inert | **pass** |
| cosmo-cmb | 5 (C4 partial) | 4 (C1, C2, C3, C6) | yes | inert (both answered at L2) | **pass** |
| cosmo-weak-lensing | 6 | 3 (W1, W5, W6) | yes | inert (both answered at L2) | **pass**, at the threshold |
| cosmo-supernovae | 6 | 4 (N1, N2, N5, N6) | yes | N8 gained (Stage-IV dossier serves classification); N7 inert | **pass** |
| cosmo-bbn | 6 | 4 (B2, B3, B5, B6) | yes | inert (B7 answered at L2; B8 no dossier) | **pass** |

- Statistics, which failed the pilot's second clause, passes: the four new questions on
  likelihood form, model comparison and pipeline validation, and the Wilks/Neyman
  question, failed at L2 under the tightened rule. Its `physics-and-methods.md` still
  answers S2 and S5 in full, as in the pilot.
- Weak lensing passes with exactly three gains: `systematics.md` already answers the
  shear-calibration, intrinsic-alignment and baryon questions with per-analysis tables.
- Two of ten controls were not inert (S7, N8), against one of eight in the pilot. In
  both, a dossier's step serves a neighbouring subtopic whose `subtopics.tsv` row does
  not list it.
- The only dossier question that stayed partial at L3 is C4: the τ dossier explains how
  τ is measured and what limits it, but gives no rule for choosing a τ prior when Planck
  large-scale polarisation is left out; that material sits in `open-questions.md` §1.

## Suspected errors checked at source (9 checks)

No skill statement checked was found wrong. Four are faithful copies of a statement that
is itself inconsistent in the paper; one L2 statement copies a unit as the paper prints
it without saying so.

| # | File | Statement | What the paper says |
|---|---|---|---|
| E1 | SI `deep/pipeline-validation.md` | stacked α_∥ bias −0.0052 ± 0.0005 against a σ/3 threshold of 0.0038; paper calls it "near the threshold" | arXiv:2503.14741, Table 1: Combined (400) −0.0052 ± 0.0005; Fig. 6 caption: σ_DESI/3 = 0.0038 for α_∥. Both confirmed; the paper's wording is loose, as the dossier says. |
| E2 | CMB `deep/beams-calibration-polarisation.md` | DR6 effective FWHM "1.42/2.07/1.01′ at f090/f150/f220 (first two appear transposed)" | arXiv:2503.14451, Sect. II.7: printed exactly so. A 90 GHz beam narrower than at 150 GHz is implausible for one telescope; the dossier's warning stands. |
| E3 | WL `references/physics-and-methods.md` §2 | C̄₁ = 5 × 10⁻¹⁴ M⊙ h⁻² Mpc² | arXiv:2602.10065, Sect. IV.2: printed so (and ρ_c = 3H₀/8πG, without the square). The dossier `intrinsic-alignments.md` gives Blazek's h⁻² M⊙⁻¹ Mpc³ and notes the difference; the L2 file copies the paper's units without a flag. |
| E4 | SN `deep/covariance-likelihood-blinding.md` | Pantheon+ prints w = w0 + wa(1 + z) | arXiv:2202.04077, Sect. II.3 (HTML): "w = w_0 + w_a (1+z)". Confirmed; not the CPL form the other analyses print. The dossier leaves it unresolved, correctly. |
| E5 | SN `deep/stage-iv-photometric-samples.md` | DES-SN5YR: classification under 10% of the systematic budget (against "~1/3" in M25) | arXiv:2401.02945, abstract: "less than 10% of the total systematic uncertainty budget". Confirmed; the M25 statement was not checked. |
| E6 | CMB `deep/low-ell-polarisation-tau.md` | the sentence after Planck Eq. 5 names α and β in the opposite order to the equation | arXiv:1907.12875, Sect. 2.2.1: "α and β are the amplitudes of dust and synchrotron templates, respectively", while the templates listed first are 30 GHz (synchrotron) then 353 GHz (dust). Confirmed as the dossier describes. |
| E7 | WL `deep/two-point-statistics.md` | UNIONS configuration against harmonic: 2.18σ with the correlation, ±0.2σ | arXiv:2605.13543, Sect. 5.3: p = 1.5 × 10⁻², 2.18σ, ±0.2σ from mock counting. Confirmed (the abstract calls it a "2.18σ agreement", the conclusion a "difference"). |
| E8 | SI `deep/model-comparison.md` | (w0, wa) prior areas 1.096 and 15.5 | arXiv:2609.04334, App. A.1, Table 3: confirmed. The 0.6 gap between the ln B shift and ln of the area ratio, flagged by the dossier, was not pursued. |
| E9 | SN `references/physics-and-methods.md` §3 and `deep/dust-intrinsic-scatter.md` | Dust2Dust σ_w = 0.005 (L2) against 0.014 ± 0.001 (dossier, body) | arXiv:2112.04456: the current arXiv abstract gives σ_w = 0.005; the HTML body, an earlier version, gives 0.014 ± 0.001 and an "upper threshold" of 0.014(1) in its own abstract. Both confirmed; the version difference is real and the dossier records it. |

## Personal-layer answering test

A throwaway personal layer was created with `COSMOSKILL_HOME` set to a directory in the
session scratchpad (`layers.py init`). The real `~/.cosmoskill` did not exist before or
after. Two entries:

- `layers.py override cosmo-cmb results#optical-depth-tau "FIXTURE-OVERRIDE (layer test
  2026-10-20, not a real value): for me, use tau = 0.0600 +/- 0.0050 as the baseline
  prior."`
- `layers.py suppress cosmo-supernovae physics-and-methods#blinding-practice
  "FIXTURE-SUPPRESS (layer test 2026-10-20): I know SN blinding practice."`

`layers.py check` reported 0 problems. `resolve` printed the τ table under `[base]`
followed by `[personal override — effective for this researcher] FIXTURE-OVERRIDE …`, and
the SN section as `[suppressed by the personal layer: FIXTURE-SUPPRESS …]` with no base
text.

**Question 1 (touches the override).** "Which τ should my ground-based CMB fit adopt as
a baseline prior?" Answer, from `cosmo-cmb/SKILL.md`, `references/physics-and-methods.md`
§6 and the `resolve` output: the package values are labelled `[base]` — Planck 2018
0.054 ± 0.007, SRoll2 low-ℓ 0.0566 (+0.0053/−0.0062), PR4 0.058 ± 0.006, NPIPE
0.051 ± 0.006, with ACT DR6 using the SRoll2 likelihood (equivalent prior
0.0566 ± 0.0058) and SPT-3G D1 a PR4 Gaussian prior; the personal override
"τ = 0.0600 ± 0.0050 (fixture)" is labelled `[personal override]` and is the value used.
Closing line: `[cosmoskill L2 · base + personal · cosmo-cmb/results#optical-depth-tau]`.
**Pass**: base and override both shown, labelled, and the one used named.

**Question 2 (touches the suppressed section).** "Which pre-unblinding tests should a new
SN Hubble-diagram analysis register, following DES-Dovekie and Unite?" Answer, from
`cosmo-supernovae/SKILL.md` and `references/physics-and-methods.md` §4.1 (row
"Validation and blinding"): 25 simulated samples recovering the input cosmology, a
data–simulation reduced χ² window of 0.7–3.0, reproduction of the previous release; the
text of §10 "Blinding practice" is left out, with the statement "§10 is suppressed by
your personal layer (reason: FIXTURE-SUPPRESS … I know SN blinding practice)". Closing
line: `[cosmoskill L2 · base + personal · cosmo-supernovae/physics-and-methods#what-each-main-analysis-did]`.
**Pass**: suppressed text left out and the suppression stated.

Two observations. (i) `layers.py <skill>` describes a suppress as "skip that section
unless the question is about it" (as `docs/layers.md` does), so for Question 2 the
answerer has to decide that a question on pre-unblinding tests touches §10 without being
"about" it; the rule gives no test for that. (ii) The `resolve` header prints the
absolute path of the base file, which would leak a user path into any answer or log that
pastes it verbatim.

The throwaway layer lives only in the session scratchpad; nothing was written to a real
layer.

## Recommendations

1. **List cross-serving dossiers in `subtopics.tsv`.** The pilot asked for this (its
   recommendation 3) and two controls again gained from a neighbouring dossier:
   `goodness-of-fit` is answered by `deep/covariance-estimation.md` (KiDS-1000 N_Θ,eff
   estimators) and `photometric-classification` by
   `deep/stage-iv-photometric-samples.md` (classifier training and calibration). Adding
   them to the `files` column, and to the file maps, would make the L3 route visible and
   the controls honest.
2. **Give every "how to choose" its rule inside the dossier, or point to where it is.**
   C4 stayed partial because `deep/low-ell-polarisation-tau.md` has no step on choosing a
   τ prior without Planck large-scale polarisation; the material is in
   `open-questions.md` §1. Either add that step or add an explicit pointer in the
   dossier's "Choices" section.
3. **Tighten two layer details.** Define when a question is "about" a suppressed section
   (for instance: the section's key or heading is the subject), so that answers are
   reproducible; and print the base file of `resolve` relative to the package root.
   Separately, `references/physics-and-methods.md` §2 of `cosmo-weak-lensing` should flag
   that the C̄₁ unit is copied as DES Y6 prints it (E3).
