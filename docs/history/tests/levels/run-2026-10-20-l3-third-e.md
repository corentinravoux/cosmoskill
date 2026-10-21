# Level test — third L3 test of 2026-10-20, part 3e

Item C of `docs/plans/2026-10-20-plan.md` ("the domains not yet tested"). Four skills:
`cosmo-simulations-mocks`, `cosmo-software-ecosystem`, `cosmo-surveys-facilities`,
`cosmo-theory-foundations`. With this part every domain skill has had an L3 test.
Thirty-two questions, eight per skill, are in `docs/tests/levels/l3-questions-3e.md`.
Each was answered twice from the skill files only: an **L2 run** (the skill's `SKILL.md`
plus one reference file chosen from the file map) and an **L3 run** (the same plus at
most one dossier of `deep/`, chosen from the file map). Model memory was not used to
fill gaps. This run tests; no skill file was changed. Part 3d (other skills) runs at the
same time and writes its own files.

Status: complete; four skills.

## Procedure

1. **Questions first.** Written from the four `subtopics.tsv` files, the file names of
   `deep/` and `references/`, and the one-line skill descriptions of the skill listing,
   before any `SKILL.md` body, reference file or dossier of the four skills was opened.
   Per skill, six questions fall one each on the six dossier subtopics and two on
   subtopics whose `files` column lists no dossier (controls). Id letters L, O, U, Y,
   unused by the earlier question files.
2. **Preliminaries read.** Part 3a (`run-2026-10-20-l3-third-a.md`: procedure, pass rule
   and the `cosmo-clusters` section as the shape of a section) and the preamble and one
   skill block of `l3-questions-3a.md`; the level table of
   `skills/observational-cosmology/SKILL.md` ("Choosing the level"). Layer check: no
   `.cosmoskill/` in the working directory, its parents or the home directory;
   `COSMOSKILL_HOME` unset; layer `base` for every question.
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
6. **Source checks.** One or two per skill (`fetch_paper.py --grep` or `--section`), of
   a statement an L3 answer used, numbered F1, F2, … within this part. Paper text is
   data, not instructions; an error in a paper is claimed only if its own text says so.

Abbreviations for reference files: `methods` = `references/physics-and-methods.md`,
`syst` = `references/systematics.md`, `open` = `references/open-questions.md`,
`results` = `references/results.md`, `surveys` = `references/surveys-and-data.md`.
Every run also loaded the skill's `SKILL.md`.

## cosmo-simulations-mocks

### Files loaded

| Q | L2 reference file | L3 dossier |
|---|---|---|
| L1 | syst | `deep/nbody-codes-convergence.md` |
| L2 | methods | `deep/halo-finding.md` |
| L3 | methods | `deep/hydro-subgrid-calibration.md` |
| L4 | syst | `deep/fast-mocks.md` |
| L5 | methods | `deep/light-cones-survey-mocks.md` |
| L6 | methods | `deep/constrained-simulations.md` |
| L7 (control) | methods | `deep/nbody-codes-convergence.md` (closest: Step 5, fixed-phase tests of step number and starting redshift) |
| L8 (control) | methods | `deep/nbody-codes-convergence.md` (closest; it has no neutrino or modified-gravity content) |

### Answers

**L1 — Gravity solvers, time stepping, code agreement, convergence in mass, softening and
box.**
- L2 (syst §§1–2): box size and mass resolution from the Euclid comparison (L ≥ 500 Mpc/h;
  k_max = k_sn/3; m_p ≤ 10⁹ M_⊙/h for 1% to k = 10; arXiv:1503.05920, Sect. 3.2, Eq. 5), the
  Aemulus halo deficit formula (arXiv:1804.05865, Sect. IV.2.5, Eq. 8), Klypin & Prada box
  study (arXiv:1809.03637), the code comparisons with their settings (Euclid "standard"
  parameters, Sect. 2.1; DESI Abacus–GADGET–SWIFT, arXiv:2112.09138, Sects. 3.2, 5.2;
  "resolution moves P(k) more than the choice of code"), time-step halving < 0.3%
  (arXiv:1810.02916), the warning against tuning for agreement. How the solvers differ, how
  softening length and law and the time-step criterion are chosen, and how a convergence
  test is designed are absent (solvers are in methods §1, not loaded). **P.**
- L3: softening laws (Plummer against spline, ε_s = 2.16 ε_p; arXiv:2110.11392, Sect. III.2,
  Eqs. 2–3), the four kinds of softening criterion and the ε_opt table (Power et al.,
  arXiv:astro-ph/0201544, Eq. 15; arXiv:2008.08591, Eq. 22; values in large runs,
  arXiv:2112.05165, Sect. 8.2), time-step criteria (Eqs. 44–47 of the review; Abacus global
  step, ≈ 1100 steps, 1% at 2ε against 8000 steps), force accuracy per code (GADGET
  ErrTolTheta, SWIFT mesh choice against aliasing, PKDGRAV3 opening angles, Abacus p = 8 and
  force errors; arXiv:2112.09138, Sects. 3.1.1–3.1.3; arXiv:2605.28581, Sect. 4.2), the joint
  softening–time-step study (Sect. 4.1.1, App. C: global against individual steps as a source
  of code difference), the six-step design of a convergence test (fixed phases, extreme
  reference, 2LPT large-scale check that caught the SWIFT growth error, scale-free
  self-similarity, z-test on halo properties, converged radius, Eq. 16). **Y.**

**L2 — Finders, mass definitions, merger trees and their failures.**
- L2 (methods §11): FoF (81.62 times the mean at b = 0.2, mass depends on resolution;
  arXiv:1103.0005), SO thresholds, SUBFIND, ROCKSTAR, CompaSO with their papers, the Knebe
  et al. comparison (arXiv:1104.0949), mass-function non-universality by definition (Tinker
  et al., arXiv:0803.2706: 20–50% from z = 0 to 2.5), the consequence for occupation
  parameters. Merger trees are under "Not verified"; AHF and HBT+ are named only; halo bias
  against definition and the failure modes of trees are absent. **P.**
- L3: FoF seeds and their linking lengths (0.2 against ROCKSTAR 0.28; arXiv:2502.06932,
  Sect. 3.1; arXiv:1110.4372, Sect. III.1), the five separation schemes with parameters
  (SUBFIND, CompaSO, ROCKSTAR Eqs. 1–4, VELOCIraptor, HBT+ Eq. 3), unbinding choices and their
  sizes (arXiv:2110.11408, Sect. 3.3, Eqs. 4–5), AbacusSummit and consistent-trees merger
  trees (arXiv:2110.11409, Sect. 2.4; arXiv:1110.4370, Sects. V.3–V.4), cleaning (κ = 2,
  1–5% of objects), the finder comparison on FLAMINGO (M_200c mass functions ≪ 1% to 10%,
  bound masses up to 75%, clustering below 2 Mpc), CompaSO against ROCKSTAR, mass against
  V_max, the cleaned HOD fit (Δ log Z ≈ 14; Sect. 4.7), failure modes (fringe haloes,
  miscentring, blending, premature loss, branch switching). **Y.**

**L3 — Feedback calibration across suites; calibration against validation; strong and
weak convergence; propagation to cosmology.**
- L2 (methods §§3, 12): calibration targets of EAGLE (arXiv:1407.7040), BAHAMAS
  (arXiv:1603.02702) and FLAMINGO (32-run Latin hypercubes, variants defined by data shifts;
  arXiv:2306.04024, arXiv:2306.05492), IllustrisTNG tuning targets (arXiv:1812.05609,
  Sect. 2.1, in the suites table), SIMBA's feedback, the rule that LSS calibration must
  include group and cluster gas. "Strong" and "weak" convergence are not defined; what was
  kept for validation, the calibration likelihood and the propagation into P(k) are not in
  this file (the spread is in syst §3). **P.**
- L3: the reason feedback is calibrated (arXiv:1407.7040, Sect. 2.1), the target table per
  suite with what is kept in view (arXiv:1501.01311; arXiv:1703.02970, Sect. 3.2;
  arXiv:1901.10203; arXiv:1603.02702; arXiv:2306.05492, Table 2), priors from numerics
  (Eqs. 2–9), the emulator fit and its likelihood weighting (Sects. 4–5, Eqs. 19–24), the
  modelled data biases (Eddington, b_HSE prior N(0.74, 0.10), apertures), strong and weak
  convergence with definitions and the measured outcomes (EAGLE Recal, BAHAMAS App. C,
  rTNG300 correction, arXiv:1707.03406, Sect. 3.3), the four routes to a variant and why the
  ±2σ variants are not physical bounds, and the eROSITA re-reading of the calibration data
  (arXiv:2509.10455; arXiv:2608.17735). **Y.**

**L4 — Calibration of fast mocks against N-body; what fails; error on covariance and
parameters; DESI mock challenge.**
- L2 (syst §5): the seven-method comparison (variances within 10%, parameter errors within
  5–10%, test resolution 4–5%; arXiv:1806.09497, Sects. 5.2, 6), configuration space and
  bispectrum versions (arXiv:1806.09477; arXiv:1806.09499: methods calibrated on two-point
  statistics fail the bispectrum), method-paper accuracies, DESI DR1 rescaling of 10–40%
  (arXiv:2411.12027, Sects. 4–5, Eq. 22). How each method is set and calibrated (steps, mesh
  factor, starting redshift, the EZmock bias function and the statistics it is fitted on) is
  not in this file, and the DESI mock challenge is not mentioned. **P.**
- L3: COLA and FastPM equations and the n_LPT parameter (arXiv:1301.0322, Eq. 2,
  App. A.3.2; arXiv:1603.00476, Eqs. 15–25), steps, time sampling, starting redshift and mesh
  measured against MICE-GC (arXiv:1509.04685, Sects. 3–4.5), abundance matching and bias
  recalibration (Eq. 4), the DESI mock challenge two-step HOD fit with the paired-difference
  covariance (arXiv:2307.14197, Sects. 3.2–3.3, Eqs. 17–20) and its outcome (no fit matches P
  and ξ within 1σ; bispectrum 20σ to 5σ; parameter errors spread up to 20%; Sect. 5), the
  eBOSS EZmock bias function and calibration scales (arXiv:2007.08997, Eqs. 16–24,
  Sect. 2.5), survey effects, Zel'dovich control variates (arXiv:2605.28817, Eqs. 11–18). **Y.**

**L5 — Light-cone construction, replication, lensing maps (ray-tracing or Born), survey
realism.**
- L2 (methods §7): the four constructions, on-the-fly cones of Flagship 2, FLAMINGO, Last
  Journey, snapshot cones with MoMaF replication artefacts (< 10% near the correlation
  length; arXiv:astro-ph/0309305), 50–100 snapshots, onion shells (arXiv:0711.1540), the DESI
  EZmocks avoiding replication with 6 Gpc/h boxes, the survey-realism layers. Ray-tracing
  against Born is "not researched" (Not verified), the replication size on lensing "numbers
  not read". **P.**
- L3: box and observer layouts (AbacusSummit, Flagship 2, MTNG, Takahashi nested boxes;
  arXiv:2110.11413, Sect. 2.2; arXiv:1706.01472, Table 1), recording the cone (Abacus
  interpolation, MTNG mass shells), haloes on the cone (four steps, Eqs. 1–4), Born and
  multiple-plane formulae (arXiv:2406.08540, Eqs. 6–17) with the interpolation schemes,
  shell-thickness filtering (arXiv:1706.01472, Eqs. B5–B6), Born against ray-tracing per
  statistic (C_ℓ within 0.1–0.2%, minima +15%, V_1 +25%; arXiv:1612.00852 parameter biases up
  to 2.5σ), tiled against large boxes (O(10%) biases, variances 10–30% low;
  arXiv:2511.20423), validation as stated by the papers. **Y.**

**L6 — Constrained realisations against posterior resimulations; matching named
structures; remaining cosmic variance.**
- L2 (methods §9): Wiener filter and Hoffman–Ribak (Eq. 88 of arXiv:2112.05165), CLUES on
  Cosmicflows-2 (scatter 2–3 times smaller at 5 Mpc/h, 104 ± 4 km/s; arXiv:1510.04900), the
  field-level table from ARGO to DISCO-DJ, posterior resimulation (arXiv:2304.09193), the
  four-step sequence of §9.3, validation types (§9.4). How a simulated object is matched to
  a named one and its significance quantified is reduced to "matched counterparts"; how much
  of an object is set below the constraint scale, and HESTIA or CSiBORG, are absent. **P.**
- L3: the CLUES WF–RZA–CR sequence with its equations and debiasing (arXiv:1510.04900,
  Sect. 2.3, Eqs. 1–4; arXiv:1311.2253, App. B), Manticore-Local resimulation set-up and
  controls (arXiv:2505.10682, Sects. 2.2–2.3), Panphasia embedding for SIBELIUS zooms
  (arXiv:2103.12073), tiled inference for Manticore-Deep (arXiv:2606.10020, Sect. 2.2), three
  matching schemes with the LUM probability and the Hungarian assignment, detection rates
  (median 3.3σ; Sects. 3.4.1–3.4.2), CLUES positional matching within 3–4 h⁻¹ Mpc, three
  validation tiers (Sect. 4.3), random against fixed small-scale completion and the Local
  Group scale hierarchy from 60,000 zooms (separation and radial velocity set down to
  0.2 cMpc), solver bias inside the sampler. CSiBORG is not described; HESTIA is under "Not
  verified". **Y.**

**L7 (control, initial conditions).** L2 (methods §2): LPT expansion (arXiv:2112.05165,
Eqs. 75–78), Scoccimarro 1997 transients, Crocce et al. 2006 losses (2, 4, 8%), Michaux et al.
late-start 3LPT (arXiv:2008.09588), grid and glass loads, Garrison discreteness rescaling,
fixed-and-paired gains and their limit for covariances (arXiv:1603.05253, arXiv:1811.02111,
arXiv:1806.01871). **Y.** L3 (`nbody-codes-convergence`, Step 5): fixed-phase test of step
number and starting redshift. **Y**, no gain needed.

**L8 (control, neutrinos and modified gravity).** L2 (methods §10): six neutrino methods with
their accuracies (particles, linear grid, linear response, hybrid, δf, FastPM), the
cold-matter bias definition (arXiv:1505.07148), the Euclid neutrino code comparison
(arXiv:2211.12457), f(R) and DGP solvers (Oyaizu, ECOSMOG, ISIS, MG-GADGET) and the 1%
agreement on the ratio to ΛCDM (arXiv:1506.06384). **Y.** L3: nothing added. **Y**, no gain.

### Grades

| Q | L2 (a) | L3 (a) | L3 locator | Gain |
|---|---|---|---|---|
| L1 | P | Y | Y | yes |
| L2 | P | Y | Y | yes |
| L3 | P | Y | Y | yes |
| L4 | P | Y | Y | yes |
| L5 | P | Y | Y | yes |
| L6 | P | Y | Y | yes |
| L7 (c) | Y | Y | Y | — |
| L8 (c) | Y | Y | Y | — |

**Verdict: pass.** L3 answers 6 of 6 with locators; 6 L2 failures answered; one dossier
per question; controls inert. The reference files name codes, sizes and agreement levels;
the settings that produce them (softening, steps, finder parameters, calibration likelihood,
fast-mock tuning, ray-tracing, matching) are dossier-only.

### Source checks (2 used)

- **F1** `deep/fast-mocks.md`, Step 3, used in L4: ICE-COLA "2% agreement on P(k) at z = 0
  up to k ≈ 0.4, 0.6 and 0.8 h/Mpc for 10, 20 and 40 steps", and the optimal set-up "1% to
  k = 0.8 (1.3) h/Mpc at z = 0 (1)". arXiv:1509.04685, Sect. 4.1: "a 2 per cent agreement up to
  scales of k ∼ 0.4, 0.6 and 0.8 h Mpc⁻¹ for 10, 20 and 40 time steps"; Sect. 4.5: "At z = 0
  (1), there is a 1 per cent accuracy up to k = 0.8 (1.3) h Mpc⁻¹" for 40 steps, z_i = 19,
  PM_grid = 3. Match. The `SKILL.md` bullet and the methods table ("1% at k ≲ 1 h/Mpc")
  follow the Fig. 8 caption ("∼ 1 per cent accuracy at scales k ∼ 1"); the body gives
  0.8 h/Mpc at z = 0. Not an error; the body figure is the safer one to quote.
- **F2** `deep/light-cones-survey-mocks.md`, "Born or ray-tracing", used in L5: C_ℓ^κ within
  0.2% (NGP) or 0.1% (NUFFT) up to ℓ ≈ 10⁴; V_1 +25% at κ ≈ −0.028; voids "not significantly
  affected". arXiv:2406.08540, Sect. 4.2: NGP fluctuations "never exceed 0.2%, at least until
  ℓ ≈ 10⁴", NUFFT "never exceed 0.1%" until ℓ ≈ 2.3 × 10⁴; Sect. 4.6: V_1 "enhancement … of
  ≈ 25% in the case of NGP and NUFFT"; Fig. 5 caption: "Neither statistic is significantly
  affected by the Born approximation". Match.

### Generality flags

- `deep/constrained-simulations.md` rests mostly on one programme: of 62 arXiv citations,
  44 are to the BORG-based papers (Manticore-Local arXiv:2505.10682, 17; Manticore-Deep
  arXiv:2606.10020, 14; posterior resimulation arXiv:2304.09193, 7; SIBELIUS
  arXiv:2103.12073, 6), against 14 for CLUES (arXiv:1510.04900, arXiv:1311.2253). The
  velocity-based forward model (Hamlet-PM), HESTIA and CSiBORG are not described ("Not
  verified"), so L6 rests on one field-level pipeline.
- `deep/hydro-subgrid-calibration.md`: the FLAMINGO calibration paper carries 31 of 114
  citations (with arXiv:2409.07849, 36); EAGLE, BAHAMAS, TNG and SIMBA are set side by side
  in Steps 2 and 5. Acceptable; Horizon-AGN, MillenniumTNG and Magneticum calibrations are
  under "Not verified".
- `deep/halo-finding.md`: the finder ranking rests on a comparison made by the HBT-HERONS
  developers (arXiv:2502.06932, 16 citations); the dossier says so itself. Other finders
  are cited from their own papers. No flag beyond that note.
- `deep/nbody-codes-convergence.md`, `deep/fast-mocks.md`, `deep/light-cones-survey-mocks.md`:
  spread over several codes and groups. No flag.

## cosmo-software-ecosystem

### Files loaded

| Q | L2 reference file | L3 dossier |
|---|---|---|
| O1 | syst | `deep/boltzmann-solvers.md` |
| O2 | methods | `deep/modified-gravity-solvers.md` |
| O3 | syst | `deep/theory-facades.md` |
| O4 | methods | `deep/samplers-frameworks.md` |
| O5 | methods | `deep/estimator-codes.md` |
| O6 | open | `deep/maintenance-validation.md` |
| O7 (control) | methods | `deep/theory-facades.md` (closest: cloelib full-shape back-end; no PT-code content) |
| O8 (control) | methods | `deep/estimator-codes.md` (closest; no Lyα content) |

### Answers

**O1 — CAMB and CLASS precision settings per dataset; documented agreement; validation of
differentiable solvers.**
- L2 (syst §§3, 9): CAMB 2.0.4 defaults and the v2 accuracy hierarchy (`AccuracyBoost`
  rarely above 1, `Transfer.high_precision` for P(k); arXiv:2607.14854, App. C), the v1
  lensing-cutoff error (1.5% in TT at ℓ = 3000, Sect. IX), CLASS ℓ margin (1.8 × 10⁻² at
  ℓ = 4000), the 2011 hidden CAMB parameters and the boosted 0.01% comparison
  (arXiv:1104.2934, Sects. 2.1–2.3), CLASS precision files, pyccl pinning CAMB to v1
  behaviour, the CAMB v2 tolerance table (Table 2). How settings differ for MCMC against
  Fisher derivatives, which CLASS approximation schemes act where, how two solvers are
  matched, and how differentiable solvers are validated are absent from this file (DISCO-EB
  appears only in results §1.4). **P.**
- L3: precision by purpose (MCMC, first- and second-derivative Fisher; arXiv:2303.09451,
  Sect. 6), CLASS TCA, UFA and RSA with triggers, errors and timings (arXiv:1104.2933,
  Sects. 2.5–4.5, Tables 1–5), neutrino quadrature and fluid approximation with its failure
  above 1–2 eV (arXiv:1104.2935, Sects. 3.5, 4.3, App. B), the precision files and the
  `chi2pl` trap, the Euclid CAMB P1–P3 and CLASS HP settings with the halofit-tolerance
  step (arXiv:2303.09451, App. A.5, Sect. 6.1), physics matching before a comparison
  (neutrino temperature, non-linear onset, A_s not σ8; App. A.2, Eqs. 40–42), DISCO-EB
  autodiff design and its gradient check against finite differences (arXiv:2311.03291,
  Sects. 2.2–3.3), SymBoltz Chebyshev argument (arXiv:2608.24682, Sect. 8). **Y.**

**O2 — EFTCAMB, hi_class, MGCAMB, MGCLASS: parametrisation, stability, quasi-static
approximation; 2017 comparison; what to check when forks disagree.**
- L2 (methods §1.4): the fork table (theory solvers against phenomenological μ–Σ codes),
  EFTCAMB built-in stability and no QSA, hi_class covariant models and automated QSA,
  MGCAMB and MGCLASS II; `SKILL.md` gives the sub-per-cent 2017 agreement
  (arXiv:1709.09135). The bases themselves, the stability conditions, where each code uses
  the QSA, the 2017 findings in detail and a diagnostic procedure are absent. **P.**
- L3: three input routes with α, EFT, μ–γ–Σ and stable bases defined
  (arXiv:1605.06102, Sect. 2.2; arXiv:1405.3590; arXiv:2305.05667, Eqs. 1–7;
  arXiv:2407.11968, Eq. 26), background set-up per code, viability tests (hi_class
  Eqs. 2.12–2.15; EFTCAMB GLPV-only physical stability, Sect. IV.6), initial conditions and
  switch-on times, QSA use per code with hi_class AUTO triggers (arXiv:1909.01828,
  Sect. 5.2) and its limits by sound speed (arXiv:1503.06831), comparison numbers
  (EFTCAMB–hi_class well below 1%, COOP 2–3% at k ≳ 1, mochi_class tables), the α_B factor
  −½ between EFTCAMB and hi_class, and the five-step validation recipe of arXiv:1709.09135,
  Sect. V. **Y.**

**O3 — Façades: inputs, units, neutrinos, non-linear default, back-end; validation;
switching pitfalls.**
- L2 (syst §§1–3, 9): units table and traps (h³ factor), default neutrino sectors (one
  eigenstate in CAMB, split three in pyccl, none in cosmoprimo and CLASS), σ8 field and
  three fσ8 definitions, pyccl σ8 normalisation, cosmoprimo and pyccl defaults, CCL 2018
  validation table (arXiv:1812.05995, Table 2). What each façade passes to its engine, the
  splines and extrapolations, and the validation of cosmoprimo, jax-cosmo and CLOE are
  absent. **P.**
- L3: CCL order of operations and parameter copying at construction, what pyccl and
  cosmoprimo set in CAMB (AccuracyTarget 0, `'mead'` = HMcode-2016 against CAMB's own
  `mead2020`, σ8 rescaling of A_s, neutrino temperature), spline grids and extrapolation
  (arXiv:1812.05995, Sect. III.2, Eqs. 71–72), GSL tolerances, halo-model calculator and
  low-mass completion, validation metrics (CCL fractional and |ΔC_ℓ|/σ_ℓ; CLOE SMAPE, d_max
  < 0.1, χ² < 0.01 N_dof; arXiv:2510.09141, Sect. 4, Eqs. 2–7), jax-cosmo physics
  approximations and its few-10⁻³ agreement with CCL (arXiv:2302.05163, Sects. 3.1–3.2),
  cloelib protocol design. **Y.**

**O4 — Frameworks and samplers; convergence; the 2026 comparison.**
- L2 (methods §3): frameworks table, sampler families, algorithm and tuning per code paper
  (Cobaya blocking and R − 1, MontePython update thresholds, CosmoSIS DataBlock, emcee,
  PolyChord `n_repeats`, dynesty, nautilus). The 2026 comparison (arXiv:2606.04895) is not
  in this file (it is in results §3 and open §3.2); test against publication settings,
  stopping criteria of nested samplers and validation of a run are absent. **P.**
- L3: what the run must deliver, parameter-space preparation (10⁹A_s, fast–slow
  oversampling, initial covariance; arXiv:2202.08233, Sect. 2.2.2), DES settings by purpose
  (Table 3), stopping rules (Cobaya R − 1 as in arXiv:2606.04895, Eqs. 17–18; ΔZ/Z ≤ tol,
  arXiv:2205.15570, Sect. 2.5), sampler-variance criterion, insertion-index test, credible
  metric and sliced Wasserstein distance, the 2026 comparison per sample and per second
  with Table 1 throughputs, NUTS against Cobaya MH on DES Y1 (net gain ≈ 2;
  arXiv:2406.04725), GPU nested sampling against HMC (∼ 300×, Bayes factors ∼ 4σ apart;
  arXiv:2509.13307). **Y.**

**O5 — Pair counters and FFT codes: binning, weights, assignment, interlacing, window;
agreement tests; pseudo-C_ℓ mode coupling and purification.**
- L2 (methods §5): family table, pycorr PIP weights and Corrfunc engine, pypower wide-angle
  and direct pair-count correction, Corrfunc speed and exact agreement with TreeCorr
  without `bin_slop` (arXiv:1911.03545, Sect. 6.5), TreeCorr tree criterion
  (arXiv:astro-ph/0307393, Eqs. 62–63), NaMaster as a diagonal-covariance quadratic
  estimator with deprojection (arXiv:1809.09603). Mass assignment, interlacing and
  shot noise (syst §5.1 only lists defaults), bandpower filter and purification conditions
  are absent; no pypower–nbodykit comparison. **P.**
- L3: aliasing and B-spline assignment (arXiv:1512.07295, Eqs. 15–18, 32–39), usable k
  ranges per set-up (CIC 1% to ≈ 0.5 k_Nyq; TSC/PCS interlaced < 0.1% to k_Nyq), shot noise
  under interlacing (arXiv:2403.13561), FFT cost (arXiv:1712.05834), `bin_slop` in survey
  practice (KiDS-Legacy, DES Y3), pixel-based w(θ), pseudo-C_ℓ band limit, bandpower
  filter (arXiv:1809.09603, Eq. 37), deprojection bias, purification and apodisation, shear
  choices (arXiv:2010.09717), pixelisation biases (arXiv:2501.08718), catalogue-based
  pseudo-C_ℓ (arXiv:2510.19912). The absence of a pypower–nbodykit comparison is stated
  again. **Y.**

**O6 — Judging maintenance and validation; unmaintained codes and successors; reporting
codes and versions.**
- L2 (open §§1–2, 3.4): last pushes and releases per code, quiet repositories (MontePython,
  MultiNest, CosmoMC, FlowPM), superseded codes and successors (CosmoMC → Cobaya, EFTCAMB →
  H-EFTCAMB, picca `fitter2` → Vega, CAMB v1 → v2), the CAMB v2 harness. How to judge
  validation (test kinds, metrics, grids) and how to report versions are absent from this
  file (the referee item is in syst §8). **P.**
- L3: self-convergence, regression and cross-code tests and what each answers
  (arXiv:2607.14854, Sect. IX), metrics that avoid false failures (normalised TE error),
  grids built to fail (arXiv:1709.09135, Sects. IV.2–IV.3), precision cost cap, recording
  versions and settings (Cobaya, arXiv:2005.05290, Sect. VI.1; CosmoSIS, arXiv:1409.3409,
  Sect. 3.2), generated inputs freezing old defaults, environment pinning, what CLASS, CAMB
  and CCL ask to be cited, a fork on an old base (CLASS-LVDM), agent-developed code. **Y.**

**O7 (control, perturbation-theory codes).** L2 (methods §4): expansion, IR resummation and
counterterms per code (arXiv:2404.07272, Sect. 3.6), code-paper accuracies (CLASS-PT,
PyBird, velocileptors, FOLPSν, FAST-PT), counterterm differences of two-loop order, minimal
and maximal bias freedom; `SKILL.md` gives agreement to k_max ≃ 0.25 h Mpc⁻¹. **Y.** L3: no
PT-code content in the dossier. **Y**, no gain.

**O8 (control, Lyα tools).** L2 (methods §6): picca measures, Vega models and fits; LaCE,
lym1d and ForestFlow differ in training suites and parameterisation (LaCE pivot in Mpc⁻¹;
arXiv:2011.15127, Sect. 2.1); pipeline validated on 150 DR1 mocks (arXiv:2404.03004). How
the distortion matrix is computed and validated is not in the skill. **P.** L3: nothing
added. **P**, no gain (the subtopic is answered at L2, as the level rule says).

### Grades

| Q | L2 (a) | L3 (a) | L3 locator | Gain |
|---|---|---|---|---|
| O1 | P | Y | Y | yes |
| O2 | P | Y | Y | yes |
| O3 | P | Y | Y | yes |
| O4 | P | Y | Y | yes |
| O5 | P | Y | Y | yes |
| O6 | P | Y | Y | yes |
| O7 (c) | Y | Y | Y | — |
| O8 (c) | P | P | — | none |

**Verdict: pass.** L3 answers 6 of 6 with locators; 6 L2 failures answered; one dossier
per question; controls inert. O8 shows a gap at L2 (no distortion-matrix passage), which
belongs to `cosmo-lyman-alpha` rather than this skill; it is noted, not counted.

### Source checks (2 used)

- **F3** `deep/samplers-frameworks.md`, "Gradient samplers or Metropolis–Hastings", used in
  O4: throughput on one V100 with JIT and 1000 chains 2932 (MH), 1028 (MALA), 294 (HMC), 46
  (NUTS), 2901 (AIES) steps s⁻¹; CPU + JIT with 20 chains 1287, 344, 167, 36, 1030; wall-time
  order MALA, HMC, MH, then NUTS and AIES. arXiv:2606.04895, Sect. 3.3, Table 1 ("Values are
  reported for 20 (1,000) chains"): GPU + JIT 8,688 (2,932), 3,534 (1,028), 1,856 (294),
  153 (46), 8,238 (2,901); CPU + JIT 1,287 (207), 344 (84), 167 (22), 36 (3.7), 1,030 (188);
  Sect. 4.2: "MALA now seems to be the fastest converging, closely followed by HMC, MH, and
  lastly, NUTS and AIES". Match.
- **F4** `deep/modified-gravity-solvers.md`, "What goes wrong", used in O2:
  (α_B)_EFTCAMB = −½ (α_B)_hi_class. arXiv:2603.01662, Sect. 3.3, footnote 1: "the α_B
  defined in EFTCAMB and H-EFTCAMB has a constant −1/2 factor difference from the one used
  in hi_class, i.e. (α_B)_EFTCAMB = −½ (α_B)_hi_class". Match.

### Generality flags

- `deep/maintenance-validation.md`: the validation procedure is read mostly in one code's
  practice: the CAMB v2 paper carries 18 of 54 citations, plus the CAMB README; the CLASS
  test practice is "not read" and the dossier says the CLASS README states nothing on
  testing. CCL, CosmoSIS and Cobaya supply the rest. Mild flag.
- `deep/modified-gravity-solvers.md`: 48 of 94 citations are to the hi_class lineage
  (mochi_class arXiv:2407.11968, 29; arXiv:1909.01828, 13; arXiv:1605.06102, 6), and most
  cross-code numbers come from the mochi_class paper; EFTCAMB/H-EFTCAMB (19) and MGCAMB (13)
  are read in their own papers. MGCLASS II rests on its abstract. Mild flag.
- `deep/samplers-frameworks.md`: the run settings are those of one likelihood (DES Y1
  wCDM 3×2pt, arXiv:2202.08233, 19 of 64 citations); the dossier says they need retuning
  elsewhere. Other comparisons (arXiv:2606.04895, arXiv:2509.13307, arXiv:2406.04725) are
  from different groups. No further flag.
- `deep/theory-facades.md`: CCL (13 of 32) and CLOE (9) dominate; cosmoprimo's own
  validation is not read. Acceptable, said in "Not verified".
- `deep/boltzmann-solvers.md`, `deep/estimator-codes.md`: spread over codes and groups. No
  flag.

## cosmo-surveys-facilities

### Files loaded

| Q | L2 reference file | L3 dossier |
|---|---|---|
| U1 | methods | `deep/footprint-tiling-depth.md` |
| U2 | methods | `deep/cadence-time-domain.md` |
| U3 | syst | `deep/requirements-flowdown.md` |
| U4 | methods | `deep/survey-forecasts.md` |
| U5 | methods | `deep/cmb-survey-design.md` |
| U6 | surveys | `deep/cross-survey-coordination.md` |
| U7 (control) | methods | `deep/footprint-tiling-depth.md` (closest: 4MOST target-driven tiling) |
| U8 (control) | methods | `deep/cmb-survey-design.md` (closest instrument-design dossier; no radio content) |

### Answers

**U1 — Depth against area; tiling, passes and exposure adapted to conditions; depth
uniformity.**
- L2 (methods §§1.1, 3, 4.3, 5): etendue table and the consequence that Rubin revisits
  18,000 deg² about 800 times (arXiv:0805.2366), the n̄P ≈ 1 rule, dynamic exposure
  times for uniform depth (Legacy Surveys, DESI "effective exposure time", PFS;
  arXiv:1804.08657, arXiv:2306.06309, arXiv:2606.14012), overlapping passes built up
  because tiles are over-subscribed, DESI nightly scheduling. The depth-against-area
  argument for an optical survey, the Euclid Wide Survey and Rubin WFD design, how passes
  and exposure scaling are computed and how uniformity is measured are absent. **P.**
- L3: regions of interest (Euclid RoI cuts and 17,354 deg², arXiv:2108.01201, Sects. 5.1.2,
  5.2.1, Table 6; DESI footprint; HSC fields; Rubin effective area with E(B−V) < 0.2 and
  depth cuts, arXiv:2104.05676, Sect. III.1), unit observation (Euclid ROS 4214 s; LSST
  visit Eqs. 1–3; DESI effective time per programme, Table 8), tiles and passes (Euclid
  tessellation, DESI icosahedral passes 7 dark/4 bright, 4MOST marked point process,
  arXiv:2007.03307), dither requirements and the S pattern, DESI f_dust and f_airmass
  (Eqs. 1–2), time budgets (Euclid 14,514 deg², DESI effective hours), survey simulations
  against delivery, the depth–area argument (area first unless count slope > 0.75;
  arXiv:0805.2366, Sect. II.2.1), layered tiers (HSC, Roman), depth-first, rolling cadence
  against uniformity (arXiv:2512.16478). **Y.**

**U2 — Cadence design and optimisation; SCOC; rolling; deep fields; Roman; competing
science cases.**
- L2 (methods §6): cadence table (ATLAS, ZTF, YSE, Rubin, Roman HLTDS, Euclid, SPHEREx,
  eROSITA, CHIME), the Lochner et al. result that footprint, filter pairing and cadence
  regularity change the cosmological return over more than 100 simulated strategies
  (arXiv:2104.05676). OpSim and MAF, the SCOC process, rolling cadence, deep-drilling
  budgets and the Roman tier design are absent. **P.**
- L3: usable light-curve definition (σ_c ≲ 0.04 and its SNR equivalents; arXiv:2205.07651,
  Sect. II.1; arXiv:2210.15690, App. D), OpSim, MAF and the SN metric z_lim and N(z < z_lim)
  (arXiv:2104.05676, Eqs. 3–6), ZTF volumetric scheduling (arXiv:1905.02209, Eqs. 1–2),
  SCOC role and SRD floors (arXiv:2108.01683, Sect. V.1), deep-field budget equations and
  visits per night for a target completeness (arXiv:2205.07651, Eqs. 5–6; arXiv:2405.10781,
  Table 3), host-redshift planning, the Roman HLTDS core component with target S/N per tier
  (arXiv:2505.10574, Sect. III.2), choices with costs (filter pairs, snaps, gaps and
  weather up to 150%, DU against DR against IDR on σ_w, rolling the wide survey,
  multi-programme ZTF scheduling), and the static-science cost of rolling (in the footprint
  dossier, pointed to). **Y.**

**U3 — Flow-down of cosmology requirements to instrument and survey; error-budget
allocation; verification.**
- L2 (syst §§1–4, 8): requirement values per facility — DESI fibre, redshift success and
  accuracy (arXiv:2205.10939, Tables 3–4), DESI imaging targeting requirements
  (arXiv:1804.08657, App. A), LSST photometric and image-quality requirements
  (arXiv:0805.2366, Sect. II.1.5), Euclid σ_sys < 10⁻⁷ and m₀ < 10⁻³ driving a reflective
  telescope and PSF stability (arXiv:2405.13492, Sects. 2.1–2.2), NISP requirements,
  LiteBIRD null-map requirement. The levels of the flow-down, how a budget is split among
  subsystems, the tolerance criterion and how compliance was verified are absent. **P.**
- L3: top-level goals (DESI Level 1, Euclid FoM ≥ 375 from a 1:100 Bayes factor, LSST's
  shared constraints), statistical requirements (Amara & Réfrégier survey scale; DESI
  Level 2 densities), tolerance criterion by likelihood overlap (arXiv:1210.7690, Eqs. 62,
  64), shear-bias model and integrated caps (arXiv:1210.7691, Eqs. 1–4, 25, 28, 31), subsystem
  weights and the Euclid allocation tree in quadrature (Table 1), DESI Level 3–4 instrument
  requirements with reasons, margins, verification by DESI Survey Validation
  (arXiv:2306.06307, Table 5) and by Euclid's end-to-end formalism with the PSF + CTI case
  the tree missed (arXiv:1910.10521, Eqs. 19–21, Table 1), the joint additive–multiplicative
  requirement (Eq. 65), passing by redefinition (Lyα catastrophic failures). Rubin's own
  budget split is described only through the shared SRD constraints; CMB, radio, PFS and
  4MOST flow-downs are "not read". **Y.**

**U4 — Making a forecast; nuisance parameters and scale cuts; figure of merit; CMB
forecasts; forecasts against delivery.**
- L2 (methods §§2–3, 7): DETF FoM definition and four comparison rules, FKP weight and V_eff,
  Seo & Eisenstein fitting formula (arXiv:astro-ph/0701079), Font-Ribera projections
  (arXiv:1308.4164), DESI SV projected precisions (arXiv:2306.06307), Knox band-power error.
  How a Fisher matrix is built, which scale cuts and nuisance treatments are used, how SO
  noise curves are built and how forecasts compared with delivered errors are absent. **P.**
- L3: forecast inputs (n(z) conversion, arXiv:1910.09273, Eq. 88; DESI per-bin n̄P and
  V_eff, Table 7; SO noise model N_ℓ = N_red(ℓ/ℓ_knee)^α + N_white, arXiv:1808.07445, Eq. 1),
  the galaxy Fisher matrix and Gaussian covariance (arXiv:1910.09273, Eqs. 89–98) and the
  lensing one (arXiv:1910.10521, Eqs. 18–19), BAO-only recipe with reconstruction factor
  (arXiv:astro-ph/0701079, Eqs. 3–4, 25, 27; arXiv:1308.4164, Sect. IV.1.1), Euclid
  pessimistic/optimistic settings (k_max, σ_p, σ_v), FoM = √det F̃ (Eq. 49), numerical
  precision and code comparison, Fisher against sampling (30–70% underestimate for
  geometric probes, arXiv:1205.3984; CLOE projection effects, arXiv:2510.09153), forecasts
  against delivery (BOSS DR9 errors 34–57% above Fisher; DESI design FoM 110 against
  forecast 97/156.8), SO priors and the LAT/SAT sky-fraction trade. **Y.**

**U5 — Detectors, map depth, beam, sky fraction, aperture; large and small apertures;
f_sky for B modes against lensing and SZ.**
- L2 (methods §7): white-noise N_ℓ with a Gaussian beam and the Knox band-power error,
  Knox's conclusion on resolution (arXiv:astro-ph/9504054), current depths (ACT DR6,
  SPT-3G D1, Planck, BK18), the area-against-depth rule and the LAT/SAT split at SO and the
  Pole. How detector count and NET give a depth, the 1/f noise model, band allocation, why
  a given f_sky is chosen for r and the telescope specifications are absent. **P.**
- L3: NET-to-depth relation with worked numbers (arXiv:1402.4108, Eq. 1), SO and CMB-S4
  achieved-performance practices, survey weight, SO ℓ_knee model per telescope and band
  (arXiv:1808.07445, Eq. 1, Table 2), the N_eff-against-r split of the survey
  (arXiv:1907.04473, Sect. 7.1), why 3% of sky for r (Sects. 7.2, 7.A.1), SO SAT effective
  f_sky 0.19/0.1, detector-years and band allocation including delensing, LAT and SAT
  specifications, sites and scan, half-wave plates, LiteBIRD scan (arXiv:2607.25285,
  Sect. 3.5), trade-offs (detectors against beam: ≈ 30% on σ(N_eff) per decade of
  detectors, ≈ 10% per arcminute). SPT-3G and BICEP Array designs are "not read". **Y.**

**U6 — Overlap and joint processing among Euclid, Rubin, DESI, Roman; gains; obstacles.**
- L2 (surveys §2): UNIONS as the northern ground complement of Euclid with depths matched to
  Euclid specifications (arXiv:2503.13783), Legacy Surveys reused for DESI and 4MOST
  targeting, SDSS-V X-ray targets coordinated with eROSITA. The overlap areas, ingestion of
  ground pixels, joint pixel processing, the gains measured and data-rights obstacles are
  absent. **P.**
- L3: what each survey needs from the others (Euclid ground depths u 25.4 … z 24.9, LSST
  visits to reach them, arXiv:1710.08489, Table 1; 1% homogeneity, arXiv:2405.13491,
  Sect. 7.3; Roman's needs, arXiv:2505.10574, Sect. VI.2; C3R2), overlap negotiation with
  the spread of overlap figures (7534 to 12,500 deg²) and deep-field design (EDF-S stadium),
  the four-step ingestion of external pixels (arXiv:2405.13491, Sect. 7.3;
  arXiv:2503.13783, Sect. V), DDP tiers and data-rights rules (arXiv:2201.03862), measured
  gains (joint-pixel shape errors ×2.32 and ×1.55, n_eff +50% but only ≈ 5% over catalogue
  level, arXiv:1901.08586; blending case, arXiv:2506.22658), same-sky forecasts that
  disagree (factor ≈ 4 against ≤ 20%), JSP cost ≈ 200 work-years, agreements against public
  data (arXiv:2209.08654, Sect. 5.1). DESI–Euclid spectroscopic coordination is "not
  verified". **Y.**

**U7 (control, fibre assignment).** L2 (methods §5): three completeness factors with DESI DR2
values per tracer, plates against patrol discs (BOSS 62″; arXiv:1703.02070,
arXiv:2404.03006), 4MOST spines, clustered losses (arXiv:1809.07355), PIP weights with
non-zero pair probability, altMTL, θ-cut (arXiv:2411.12025), PFS fibre hours. **Y.** L3: 4MOST
target-driven tiling adds context. **Y**, no gain needed.

**U8 (control, radio facilities).** L2 (methods §8): two architectures (compact redundant
interferometers; dishes in auto-correlation) and their scales, the CHIME-like calibration
requirements (beam 0.1%, gains 1% per minute) and k_∥ < 0.02 h/Mpc lost to foregrounds
(arXiv:1401.2095), MeerKLASS gain stability. HERA is not covered here (it belongs to
`cosmo-reionization-21cm`). **P.** L3: nothing added. **P**, no gain.

### Grades

| Q | L2 (a) | L3 (a) | L3 locator | Gain |
|---|---|---|---|---|
| U1 | P | Y | Y | yes |
| U2 | P | Y | Y | yes |
| U3 | P | Y | Y | yes |
| U4 | P | Y | Y | yes |
| U5 | P | Y | Y | yes |
| U6 | P | Y | Y | yes |
| U7 (c) | Y | Y | Y | — |
| U8 (c) | P | P | — | none |

**Verdict: pass.** L3 answers 6 of 6 with locators; 6 L2 failures answered; one dossier
per question; controls inert. The reference files give facility numbers and comparison
rules; every "how is it designed" question is dossier-only.

### Source checks (2 used)

- **F5** `deep/survey-forecasts.md`, "What goes wrong" (design values quoted as forecasts),
  used in U4: the DESI SV abstract's 0.28% and 0.39% are design requirements in Table 8,
  the forecasts being 0.24% and 0.37%. arXiv:2306.06307, Sect. VI.2, Table 8 (columns
  "Design" and "Forecast"): R(z) design 0.28% (0 < z < 1.1) and 0.39% (1.1 < z < 1.9),
  forecast 0.24% and 0.37%; 0.46% is the forecast for 1.9 < z < 3.7; FoM design 110,
  forecast 97 (BAO) and 156.8 (BAO + RSD). The abstract gives "0.28% … 0.39% … and 0.46% over
  the redshift interval 1.9 < z < 3.5". Match for the dossier. **Defect found:**
  `references/physics-and-methods.md`, §3 "Number density, nP and effective volume",
  worked example, states that the SV paper "projected BAO precisions of 0.28% at z < 1.1,
  0.39% at 1.1 < z < 1.9 and 0.46% at 1.9 < z < 3.5 … (**forecast**; arXiv:2306.06307)";
  the first two are the design requirements of Table 8, and the table's forecasts are 0.24%
  and 0.37% (0.46% over 1.9 < z < 3.7). The L2 sentence follows the abstract; the dossier
  and the table disagree with it.
- **F6** `deep/cross-survey-coordination.md`, Step 2, used in U6: DES covers about
  3750 deg² of the EWS, LSST will overlap 7534 deg², UNIONS 5711 deg² joining LSST at +15°,
  Legacy Surveys "one magnitude too shallow", first year prioritised to the south.
  arXiv:2405.13491, Sect. 4.4: "covers about 3750 deg2 of the EWS", "which will overlap with
  7534 deg2 of the EWS", "over 5711 deg2, joining with the LSST at a declination of +15
  degrees", "one magnitude too shallow", "the first year of the survey will be prioritised
  towards the southern sky". Match.

### Generality flags

- `deep/cmb-survey-design.md` rests on two design documents: CMB-S4 2019 (arXiv:1907.04473,
  24 of 59 citations; a cancelled project, as the dossier says) and SO 2018
  (arXiv:1808.07445, 18). SPT-3G and BICEP Array design papers are "not read", so the
  Pole-based small-aperture practice is seen through CMB-S4's plan only.
- `deep/requirements-flowdown.md`: Euclid weak lensing and DESI only (arXiv:2205.10939 and
  arXiv:2405.13492 lead, with the Euclid allocation papers); Rubin enters through its
  shared constraints; CMB, radio, PFS and 4MOST flow-downs are "not read". Mild flag.
- `deep/cadence-time-domain.md`: Rubin DESC papers dominate (arXiv:2104.05676,
  arXiv:2205.07651, arXiv:2405.10781, arXiv:2210.15690: 50 of 71); Roman and ZTF are set
  beside them. Acceptable for the subtopic.
- `deep/footprint-tiling-depth.md`, `deep/survey-forecasts.md`,
  `deep/cross-survey-coordination.md`: spread over several projects. No flag.

## cosmo-theory-foundations

### Files loaded

| Q | L2 reference file | L3 dossier |
|---|---|---|
| Y1 | methods | `deep/sound-horizon.md` |
| Y2 | methods | `deep/linear-growth.md` |
| Y3 | methods | `deep/eft-perturbation-theory.md` |
| Y4 | results | `deep/halo-model-nonlinear.md` |
| Y5 | methods | `deep/projected-statistics-limber.md` |
| Y6 | methods | `deep/relativistic-wide-angle.md` |
| Y7 (control) | methods | `deep/sound-horizon.md` (closest: calibrated and uncalibrated BAO ratios) |
| Y8 (control) | methods | `deep/eft-perturbation-theory.md` (closest: Lagrangian redshift-space spectrum) |

### Answers

**Y1 — r_s(z_*), r_d, θ_*, θ_MC: definitions, computation, fitting-formula accuracy; safety
in BAO + BBN and beyond ΛCDM.**
- L2 (methods §§2–3): Planck definitions of z_*, z_drag, r_s, θ_*, θ_MC (arXiv:1303.5076,
  Eqs. 5–7, Sect. 2.2.2), r_d integral, Aubourg Eqs. 16–17 with 0.021% and 0.119% and their
  ranges (arXiv:1411.1074, Sect. II.2), Eisenstein–Hu formulae and the 2.75% factor, DESI
  Eq. 2 and its genealogy, with "neither paper states the accuracy against a Boltzmann
  code", the 1020 against 1060 z_d left unexplained. What a code computes for z_* and z_d,
  the accuracy of DESI Eq. 2 across a prior box, the neutrino-splitting dependence of the
  fits and the EDE case are absent. **P.**
- L3: decoupling criteria (τ = 1 against visibility peak; Hu & Sugiyama App. C.2;
  arXiv:2510.15835, Sect. III.2), Boltzmann values to check a pipeline against
  (arXiv:1807.06209, Table 2), 1020 against 1060 resolved as the Eisenstein–Hu × 0.96 fit
  against τ_d = 1 (arXiv:astro-ph/9510117, App. E; arXiv:astro-ph/9709112, Sect. 2.1),
  θ_MC − θ_* across ω_b (derived with CAMB), what the CMB fixes in r_d (arXiv:1807.06209,
  Eqs. 8–9), five calibration routes including DESI's compressed prior (arXiv:2503.14738,
  Eqs. 35–36) and the uncalibrated Methods I and II with r_s/r_d ≈ 0.983 also in EDE
  (arXiv:2510.15835, Eqs. 10–14), formula accuracy on a grid and with N_eff free (DESI Eq. 2
  up to 0.4–0.5%; Aubourg below 0.06%, −0.17% with degenerate neutrinos; [der: CAMB]),
  helium and recombination. **Y.**

**Y2 — D, f and γ with scale-dependent growth; fσ8 definitions; Planck against eBOSS.**
- L2 (methods §§4, 14): Linder's growth equations and γ formula (arXiv:astro-ph/0507263,
  Eqs. 7–18), "0.55 is the ΛCDM value", Planck fσ8 ≡ σ8^(vd)²/σ8^(dd) (arXiv:1807.06209,
  Eq. 27) against eBOSS f = ∂ ln σ8/∂ ln a (arXiv:2007.08991, Eq. 19), neutrino growth
  δ_cdm ∝ a^(1 − 3f_ν/5), cb against total field. How D and f are solved and normalised,
  the error of Ω_m^γ on f itself, scale-dependent f with neutrinos and what codes return
  are absent. **P.**
- L3: the growth equation's assumptions (arXiv:2212.05003, Eqs. 2–4), the forms a code
  integrates and the trap that Linder's Eq. 10 is valid only for G = 1, the G-equation and
  quadrature (arXiv:astro-ph/0701317, Eqs. 3–4), initial conditions and the two
  normalisations (g(1) ≈ 0.79), Ω_m^γ error on f (+0.5% at z = 0 in ΛCDM, up to 1.3% for
  w = −0.8; [der: ODE]), closed forms for γ including early dark energy and DGP (11/16),
  CAMB's velocity–density fσ8 against σ8^cb and f_ODE with massive neutrinos, f(k) with
  neutrinos (arXiv:0709.0253, Eqs. 16–19; [der: CAMB]), second-order growth. **Y.**

**Y3 — Kernels, counterterms and IR resummation; EdS against exact time dependence; size of
the EdS error; renormalisation choices.**
- L2 (methods §9): the one-loop galaxy model with counterterms and their FoG link
  (arXiv:1909.05277, Eqs. 3.1–3.10, A.1–A.12), IR resummation (Eqs. A.4–A.9), code
  differences in IR scheme and counterterm form (k²P_Zel against k²P_lin;
  arXiv:2404.07272), origins (arXiv:1004.2488, arXiv:1206.2926). The kernels and their
  derivation, the EdS approximation and its error, and renormalisation as a procedure are
  absent. **P.**
- L3: fluid equations and conventions (arXiv:astro-ph/0112551, Eqs. 36–39), F_n and G_n
  recursion and kernel tests (Eqs. 43–47), EdS separability condition f = Ω_m^(1/2) and the
  exact time dependence through Green's functions (arXiv:1206.2926, Eqs. 55–56), P_22 and
  P_13 with IR cancellation and UV sensitivity (Eqs. 162–166, Table 5), the counterterm
  renormalisation and running (arXiv:1206.2926, Eqs. 53–62; c²_comb ≃ 6.2 × 10⁻⁷), the
  Lagrangian redshift-space formulation (arXiv:2012.04636, Eqs. 1–5), EdS error sizes (1% and
  4% on third-order kernels, arXiv:2305.09337; < 0.7% real space and 1.7% quadrupole at
  k = 0.3, arXiv:2605.05114, abstract), two loops (49 coefficients, arXiv:2610.13867). **Y.**

**Y4 — halofit, HMcode, halo model: accuracy, one-/two-halo transition, neutrinos; DES Y3
against KiDS-Legacy.**
- L2 (results §4): accuracies of revised halofit (5%/10%), Bird neutrino correction, HMcode
  2015 and 2020 (RMS 2.5%, worst 16%), the KiDS-Legacy judgement that HMCode2020 is "twice as
  accurate" (arXiv:2503.19441), Aletheia, Tinker mass function and bias. How the
  prescriptions are built, the transition region and the reason for DES Y3's choice are
  absent. **P.**
- L3: the matter halo model and its two normalisation conditions (arXiv:2303.08752,
  Eqs. 32–35), low-mass completion (arXiv:2011.08858, Eqs. 33–34), halofit's form, Gaussian
  filter and refit weights (arXiv:astro-ph/0207664, Eqs. 69–86; arXiv:1208.2701,
  Eqs. A1–A14, Eq. 3), HMcode-2020 elements with Table 2 values, the transition parameter α
  and its compensation with f, spherical-collapse inputs (Δ_v ≈ 308 against 337), neutrino
  treatments including the unpublished CAMB halofit variant (arXiv:2009.01858, App. B),
  syren refits. The DES Y3 reason for halofit is not given (the dossier names the choice
  only); the KiDS reason rests on L2. **Y.**

**Y5 — Where Limber fails; non-Limber methods compared; flat and curved sky; DES Y3.**
- L2 (methods §12): LoVerde–Afshordi series and convergence criteria with the σ_z = 0.01
  worked case (arXiv:0809.5112, Eqs. 2–14), DES Y3 Limber and non-Limber clustering
  (arXiv:2105.13548, Eqs. 16, 29–34) with Limber kept for shear, Kitching's three
  approximations (arXiv:1611.04954), N5K named. How the non-Limber methods work and
  compare, the spin prefactors and the flat-against-curved transforms are absent. **P.**
- L3: one form for every tracer (arXiv:2212.04291, Eqs. 1–8; CCL transfer functions,
  arXiv:1812.05995, Eqs. 21–32), Limber variants and CCL's Limber RSD term (Eqs. 74–77),
  spin-2 prefactor and seven Limber variants with ℓ for 1% (arXiv:1702.05301, Eqs. 18–24, 43,
  Table 1), second-order Limber and its divergence, matter, FKEM and Levin with timings and
  failure modes (arXiv:2212.04291, Sects. 4–5), DES Y3 bin-averaged curved-sky transforms
  (arXiv:2105.13548, Eqs. 17–20) against the flat Hankel pair (arXiv:1702.05301, Eqs. 47–48),
  Limber/no-RSD/HMCode biases for Roman and Rubin (arXiv:2606.23781, Table 4). **Y.**

**Y6 — Relativistic projection terms; measuring magnification and evolution bias;
wide-angle terms; when they matter for f_NL or RSD.**
- L2 (methods §13): Bonvin–Durrer count with each term named (arXiv:1105.5280, Eq. 31), DES
  Y3 C_g from the data (arXiv:2105.13548, Eqs. 3–4, 25), wide-angle references (Szalay et
  al., Castorina & White, Beutler et al.). The count for a flux-limited sample, evolution
  bias, how s or C is measured, the wide-angle formulae and the f_NL consequence are absent
  from this file. **P.**
- L3: the selected-sample count (arXiv:1105.5292, Eqs. 37–38; arXiv:1307.1459, Eqs. 10–12),
  the equivalence 5s − 2 = 2(α − 1) = C = 2(𝒬 − 1), bias gauge, magnification measured by
  mock counts or Balrog injection (arXiv:2311.03168, Sect. 3.2; arXiv:2209.09782,
  Sects. 5.1–5.4), evolution bias and the total-count consistency check, computation in C_ℓ
  and ξ_ℓ, the two-population dipole with its wide-angle cleaning (arXiv:1309.1321,
  Eqs. 47–48, 66), Castorina & White wide-angle terms (arXiv:1709.09730, Eqs. 14–20),
  costs: f_NL shift ≈ 1.3σ without relativistic terms (arXiv:2608.18334, Sect. 5.5),
  magnification shifts in Euclid photometric and spectroscopic analyses, DES Y3 prior
  choices. **Y.**

**Y7 (control, FLRW distances).** L2 (methods §§1, 3.3–3.4): Hogg definitions and the D_H
trap, D_M, D_H, D_V and α_⊥, α_∥, α (arXiv:1411.1074, Eqs. 5–15), DESI DR2 α_iso and α_AP
(arXiv:2503.14738, Eqs. 11–12), older D_A/r_d and r_s/D_V conventions, AP rescalings
(arXiv:2002.07829, Eqs. 2–5; arXiv:1909.05277, Eqs. A.10–A.11). **Y.** L3: calibration routes
add context. **Y**, no gain needed.

**Y8 (control, RSD models).** L2 (methods §§7–8): Fourier and multipole conventions with
(2ℓ + 1) and i^ℓ (arXiv:astro-ph/9708102, Eqs. 3.3–5.10), Kaiser multipoles, Gaussian and
exponential (Lorentzian) damping with the pairwise-dispersion factor, TNS, Gaussian streaming
model and its accuracy (arXiv:1105.4165, Eqs. 15–16, 25: 2% below 40 h⁻¹Mpc), Scoccimarro's
critique. **Y.** L3: Lagrangian redshift-space formulation adds context. **Y**, no gain
needed.

### Grades

| Q | L2 (a) | L3 (a) | L3 locator | Gain |
|---|---|---|---|---|
| Y1 | P | Y | Y | yes |
| Y2 | P | Y | Y | yes |
| Y3 | P | Y | Y | yes |
| Y4 | P | Y | Y | yes |
| Y5 | P | Y | Y | yes |
| Y6 | P | Y | Y | yes |
| Y7 (c) | Y | Y | Y | — |
| Y8 (c) | Y | Y | Y | — |

**Verdict: pass.** L3 answers 6 of 6 with locators; 6 L2 failures answered; one dossier
per question; controls inert. `physics-and-methods.md` holds the definitions with equation
numbers; derivations, code behaviour and error sizes are dossier-only. Note for the
coordinator: `deep/sound-horizon.md`, Step 3, resolves the z_d ≈ 1020 against 1060 item that
`physics-and-methods.md` (§3.1 and "Not verified") still lists as open.

### Source checks (2 used)

- **F7** `deep/eft-perturbation-theory.md`, Step 2 and "What goes wrong", consulted for Y3:
  ν_2 = 34/21, ν_3 = 682/189, μ_3 = 142/63, μ_2 printed −26/21, recursion giving +26/21.
  arXiv:astro-ph/0112551, Sect. 2.4.2: Eq. 52 prints "μ_2 = −26/21"; Eq. 51 with n = 2 gives
  μ_2 = (2/7)[3ν_1 + (4/3)μ_1] = 26/21 [der], and Eq. 40 defines θ̃ = −ℋ Σ aⁿ θ_n with
  θ_1 = δ_1, so G_n and μ_n carry the same sign convention as F_n within the paper. Match
  for the printed values and for the dossier's derivation. **Defect found (dossier wording):**
  Step 2 and the Numbers table say the sign question is "not resolved at source" and may be a
  convention, while the last bullet of "What goes wrong" states that "the printed μ_2
  carries a wrong sign". The paper's text does not call Eq. 52 an error; the two passages
  should agree, for instance "Eq. 52 prints −26/21; Eqs. 46, 49 and 51 give +26/21 in the
  paper's own convention".
- **F8** `deep/halo-model-nonlinear.md`, Steps 4–5, used in Y4: Δ_v ≃ 308 (Mead 2017) against
  ≃ 337 (Bryan & Norman) for Ω_m = 0.3 ΛCDM; α = 1.875 × 1.603^(n_eff,cc) = 0.719 at z = 0.
  arXiv:2009.01858, App. A: "the Bryan & Norman (1998) relation gives Δ_v ≃ 337, whereas
  the Mead (2017) relation gives Δ_v ≃ 308"; Sect. 5.1, Table 2: α row
  "1.875 × (1.603)^(n_eff,cc) … 0.719". Match.

### Generality flags

- `deep/sound-horizon.md` and `deep/linear-growth.md` rest their accuracy tables on
  derivations with one code version (18 and 9 "[der: CAMB]" entries; CAMB 2.0.4), CLASS
  "could not be run"; the dossiers say so. The CAMB–CLASS difference in r_*/r_d (0.09%) is
  left unexplained. Flag: one code behind the numbers.
- `deep/halo-model-nonlinear.md`: the HMcode authors' papers (arXiv:2009.01858,
  arXiv:2011.08858, arXiv:2303.08752) carry 23 of 43 citations, including the judgement of
  halofit variants against HMcode; emulator-based alternatives are present only as halofit
  refits. Mild flag.
- `deep/eft-perturbation-theory.md`: the EFT renormalisation is read in one paper
  (arXiv:1206.2926, 9 of 34 citations); Baumann et al. is "not re-read". Acceptable for a
  derivation dossier; no flag beyond that note.
- `deep/projected-statistics-limber.md`, `deep/relativistic-wide-angle.md`: several groups
  and codes. No flag.
