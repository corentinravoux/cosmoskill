# Maintenance and validation — cosmo-software-ecosystem dossier

Scope: how a theory code is validated numerically (self-convergence,
regression, cross-code), how the model grid, metric and precision budget
of such a test are chosen, how a run is kept reproducible across code
versions, what test and release practice the code papers state, and how a
code is cited.
Snapshot: 2026-10-22.
From: Snowmass2021 CompF white paper (arXiv:2203.07347), Sect. 5.3
(verification and validation); cloelib (arXiv:2605.23839), Documentation
and Availability; the validation sections of the CAMB 2 (arXiv:2607.14854),
CLASS (arXiv:1104.2932, arXiv:1104.2934) and CCL (arXiv:1812.05995) papers;
the Boltzmann code comparisons of Seljak et al. 2003
(arXiv:astro-ph/0306052) and Bellini et al. 2017 (arXiv:1709.09135).

Already in L2, not repeated here: repository activity and superseded codes
(`open-questions.md#maintenance-status-at-the-repositories`,
`open-questions.md#deprecated-or-superseded-codes`); installation names
(`systematics.md#documented-cases-where-a-default-changed-a`); the code
comparisons and their sizes (`systematics.md#code-comparisons-read-in-paper-bodies`);
CAMB v2 tolerances (`results.md#camb-v2-default-accuracy-arxiv-2607-14854`).
The metrics and case grid of the CLOE validation are in
`deep/theory-facades.md` (Step 7). Validation of a whole inference
pipeline on mocks (noiseless recovery, two implementations, contaminated
vectors) is in `cosmo-statistics-inference/deep/pipeline-validation.md`.

The Snowmass section that names this subtopic is about simulations: it
asks that codes and analysis tools deliver accuracy at least at the
percent level of the dark-energy targets, records progress through
comparison projects and convergence studies, and notes that "not all
differences between the codes and analysis tools have been fully resolved
and/or understood" [src: arXiv:2203.07347, Sect. 5.3]. It gives no
procedure; the procedure below is read in code papers.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Run three different tests, because each answers one question
<!-- key: step-1-run-three-different-tests-because-each -->

- **Self-convergence.** Compare the default run with the same code at
  raised precision. CAMB v2's `camb.check_accuracy` compares a default run
  with a reference that doubles the main accuracy boosts and reports
  fractional differences per output and per ℓ or k range (Lewis 2026,
  arXiv:2607.14854) [src: Sect. IX]. CLASS keeps every accuracy parameter
  in one precision structure (`include/common.h`), set by the input
  module and overwritten by a `.pre` file; "the user will not find a
  single accuracy parameter declared and hard-coded locally" (Lesgourgues
  2011, arXiv:1104.2932) [src: Sect. 2.3]. Its reference files
  `cl_ref.pre` and `pk_ref.pre` give 0.01 % accurate C_ℓ^TT and P(k) for
  2 ≤ ℓ ≤ 3000 and k ≤ 1 h Mpc⁻¹ (EE error twice larger), `pk_ref.pre`
  keeping it for the linear P(k) to k ≤ 50 h Mpc⁻¹; degraded settings are
  calibrated against them (arXiv:1104.2934) [src: Sect. 3].
- **Regression.** Compare with stored outputs. The standard CAMB test
  suite generates scalar, tensor, lensed, transfer and matter-power outputs
  over a broad grid and compares them with precomputed references made at
  boosted accuracy [src: same]. The authors state why both are needed:
  "check_accuracy bounds the distance to a more converged calculation,
  while the regression suite guards against unintended changes and
  reproduces the released outputs across the model grid" [src: same].
  The CAMB README says the suite runs on GitHub Actions for new commits
  and pull requests, with reference results kept in a separate test-outputs
  repository [sec: web https://github.com/cmbant/CAMB README, read
  2026-10-19]. CCL in 2018 ran accuracy checks in C and unit tests in
  Python on a continuous-integration service, "ensuring that the code
  remains reliable as we continue to improve it" (Chisari et al. 2018,
  arXiv:1812.05995) [src: Sect. V]. CCL compares each output with known
  analytic solutions where they exist, with simulations for its Cosmic
  Emulator path, and otherwise with "one or multiple independent
  implementations" that are shipped in the CCL repository with the
  library; each feature gets a numerical accuracy parameter 𝒜, and tests
  "pertain to numerical accuracy alone" [src: arXiv:1812.05995, Sect. IV].
- **Cross-code.** Compare with an independent implementation under
  matched physics. CAMB v2 against CLASS 3.3.4 used the same non-linear
  model (HMcode-2020 without feedback), the same lensing source cutoff,
  fixed Y_He = 0.245, Planck-era RECFAST and one massive eigenstate of
  0.06 eV, and CLASS computed to ℓ = 8000 then truncated to avoid
  lensing edge effects [src: arXiv:2607.14854, Sect. IX, Fig. 3 caption].
  The authors call it "a like-for-like numerical test, not a statement
  that the shared physical model is the most accurate description of the
  Universe" [src: same]. Earlier like-for-like tests: Seljak et al. 2003
  compared three independent codes and, by removing the main sources of
  numerical instability, improved their agreement by an order of
  magnitude, to below 0.1 % in the matter P(k) and below sampling variance
  up to ℓ = 3000 in TT, TE and EE (arXiv:astro-ph/0306052) [src]; CLASS
  against CAMB, both at reference precision, differ by Δχ² = 0.027 in a
  simplified three-channel Planck likelihood, so "the effective χ²
  obtained with Planck will only be accurate up to 0.03"
  (arXiv:1104.2934) [src: Sect. 3].

None of the three measures physical accuracy. CCL makes the same
separation: what it validates is numerical accuracy, physical accuracy
of each model being discussed separately (`physics-and-methods.md#theory-facades`).

### Step 2. Choose a metric that does not create false failures
<!-- key: step-2-choose-a-metric-that-does-not-create -->

- Relative differences blow up where a spectrum crosses or approaches
  zero. CAMB measures TE as |ΔC_ℓ^TE|/√(C_ℓ^TT C_ℓ^EE), "the normalized TE
  error", instead of a relative difference [src: arXiv:2607.14854,
  Sect. IX]. The modified-gravity comparison found EE differences above 1 %
  on the largest scales and explained that "their amplitude approaches
  zero and then the relative difference is artificially boosted"
  (Bellini et al. 2017, arXiv:1709.09135) [src: Sect. IV.1].
- Above ℓ = 3000, where foregrounds dominate temperature, CAMB plots
  only |ΔEE|/EE [src: arXiv:2607.14854, Fig. 3 caption].
- A tolerance in fractional units says nothing about inference. CAMB
  (arXiv:2607.14854) adds
  a likelihood-level proxy: a Gaussian Δχ² between default and boosted
  runs for an SO-like experiment over 2 ≤ ℓ ≤ min(4000, ℓ_max), excluding
  number-count, tensor-only and matter-only files [src: Sect. IX]. Its
  numbers are in `results.md#camb-v2-default-accuracy-arxiv-2607-14854`.
- The Δχ² metric is older than CAMB 2: CLASS III computes Δχ² against
  reference spectra in a simplified Planck likelihood (three channels,
  f_sky = 0.8, χ² to ℓ = 3000) and notes that Δχ² ∼ 1 is roughly 0.1–0.2 %
  on the C_ℓ, except on the largest and smallest angular scales
  (arXiv:1104.2934) [src: Sect. 3].
- For observables of a survey, express the difference in units of the
  data error (CCL's |ΔC_ℓ|/σ_ℓ; CLOE's d_max and χ² criteria in
  `deep/theory-facades.md`). CCL's stated goal: numerical uncertainty in
  correlation functions "within a fraction of the expected statistical
  uncertainty for LSST" [src: arXiv:1812.05995, Sect. IV].

### Step 3. Build the model grid so that it can fail
<!-- key: step-3-build-the-model-grid-so-that-it-can-fail -->

- Span the extensions the code will be used for. CAMB's grid has "more
  than a hundred parameter files" covering curvature, massive neutrinos
  and hierarchies, N_eff, dynamical dark energy, tensors, recombination
  and reionisation variants, non-linear and transfer-only configurations
  and several ℓ_max; it is generated by a script distributed with the code
  (in `fortran/tests`) and can be extended [src: arXiv:2607.14854,
  Sect. IX]. A footnote warns that unusual source-count or 21 cm
  configurations outside the grid can show "minor failures, for example at
  the very edge of a requested ℓ_max" [src: same, footnote 9].
- Test the joins between approximations. CAMB's grid includes near-flat
  models down to |Ω_K| ∼ 10⁻⁶ on both sides of zero, checking that the
  curved calculation varies continuously into the flat one with no step at
  the switch (arXiv:2607.14854) [src: Sect. IX].

- Choose parameter values that make differences visible. The 2017
  comparison used covariant-Galileon models "chosen to be bad fits to
  current CMB and expansion history data", and an f(R) value B₀ = 1,
  already excluded, "to make sure no difference between the two codes is
  hidden by the choice of a small parameter", before the realistic
  B₀ = 0.01 [src: arXiv:1709.09135, Sect. IV.2, IV.3]. It also varied
  cosmological and gravitational parameters to check that agreement was
  robust [src: Sect. IV].
- Sample the parameter space, not only points in it. CCL draws 100
  Latin-hypercube points over the five ΛCDM parameters, with ranges
  "significantly wider" than current constraints (h 0.55–0.8, Ω_c
  0.15–0.35, Ω_b 0.018–0.052, A_s 1.5–2.5 × 10⁻⁹, n_s 0.94–0.98),
  massless neutrinos, and compares linear and halofit P(k) through CCL
  with CLASS v2.6.3 run directly, at default and high precision; the test
  also checks CCL's tabulation and interpolation of external spectra
  [src: arXiv:1812.05995, Sects. IV, IV.2.3, Table 5].
- Use realistic inputs, not only smooth ones: CLOE's distance to CCL grows
  with the irregularity of n(z) (`deep/theory-facades.md`, "What goes
  wrong").

### Step 4. Set the precision budget with an explicit cost cap
<!-- key: step-4-set-the-precision-budget-with-an -->

In the 2017 comparison the precision parameters were fixed so that every
test reached the target agreement and each run stayed "fast enough for
MCMC parameter estimation", defined as at most a factor 3–4 slower than
the same model at standard precision [src: arXiv:1709.09135, Sect. IV].
Most of the raised precision was needed only for the small-scale lensed
CMB spectra, "by default 1-2 orders of magnitude worse than the other
spectra" [src: same]. All precision parameters used are listed in its
Appendix C (`systematics.md#default-accuracy-and-non-linear-settings-of`).
CAMB v2 takes the opposite route: defaults designed to reach per-mille
accuracy "without such strong boosting" [src: arXiv:2607.14854,
Sect. IX].

CLASS III gives a recipe tied to a likelihood: from reference spectra,
degrade the accuracy parameters one at a time, assuming they act
independently, and keep the loosest value of each that holds Δχ² below a
target; the files `chi2pl0.1.pre`, `chi2pl1.pre`, `chi2pl10.pre` hold the
results for Δχ² ∼ 0.1, 1, 10, and `cl_permille.pre`, `cl_2permille.pre`,
`cl_3permille.pre` give 0.1, 0.2, 0.3 % on the C_ℓ up to ℓ = 3000
[src: arXiv:1104.2934, Sect. 3]. The authors add that "the only way to
check which precision setting is sufficient is to perform a full
parameter extraction from the data with different settings" [src: same].

### Step 5. Record everything a rerun needs
<!-- key: step-5-record-everything-a-rerun-needs -->

- **Versions in the output.** "Reproducibility is ensured despite possible
  backwards-incompatible changes in the codes used, since Cobaya stores
  both its version and those of the external codes used (here CAMB) in the
  output files" (Torrado & Lewis 2020, arXiv:2005.05290) [src: Sect. VI.1,
  footnote 11].
- **Settings in the output.** "Any pipeline output contains the runtime
  options and assumptions for each module used", so that pipelines "can
  be regenerated easily at a later date for verifiability or comparison
  with collaborators" (Zuntz et al. 2014, arXiv:1409.3409) [src:
  Sect. 3.2].
- **Generated inputs freeze the generator's defaults.** The Cobaya paper's
  example input, written by its cosmology input generator, contains
  `halofit_version: mead`, `nnu: 3.046` and a PArthENoPE BBN table
  [src: arXiv:2005.05290, App. B]. A rerun of that file with a current
  CAMB gives HMcode-2016 (`'mead'`) and N_eff = 3.046, not the current
  CAMB defaults (`results.md#history-of-the-numbers-that-changed`).
- **Stock or modified external code.** Cobaya interfaces "stock versions
  through light wrappers" and provides a one-line installer for theory
  codes, likelihoods and data; users of modified codes "just need to
  provide paths to the installation folders" [src: arXiv:2005.05290,
  Sect. VI]. The archive of a run therefore needs the path and version of
  any modified code, which the installer does not know.
- **Parameter file with the chains.** MontePython writes in each output
  directory a `log.param` file whose parameter names, ranges and scalings
  its analysis tools read back, and a `.paramnames` file for GetDist
  (Brinckmann et al. 2018, arXiv:1804.07261) [src: App. C].
- **Grids of runs.** Cobaya's batch tool, taken over from CosmoMC, builds
  every model × data combination from common definitions plus two lists of
  variations, with a folder per combination and queue scripts [src:
  Sect. V.2].

### Step 6. Fix the environment
<!-- key: step-6-fix-the-environment -->

- CCL (2018): installable with pip, depends on CMake, GSL and FFTW, with
  instructions to build a Docker image "for portability to different
  architectures" [src: arXiv:1812.05995, Sect. V].
- cloelib: `pip install cloelib`, MIT licence, conda/mamba environment
  files in a separate repository, examples in a playground repository
  (Bonici et al. 2026, arXiv:2605.23839) [src: Availability].
- CAMB v2 ships a devcontainer configuration, related scripts and
  `AGENTS.md` files "for easy future development" [src: arXiv:2607.14854,
  Sect. X].
- Interface checks at start-up: cloelib's `Background` and
  `Perturbations` protocols are runtime-checkable, so compliance of an
  engine can be asserted at the start of an analysis and in continuous
  integration [src: arXiv:2605.23839, Protocol Compliance].

### Step 7. Cite the code and the version
<!-- key: step-7-cite-the-code-and-the-version -->

What each source asks:

| Code | What to cite | Source |
|---|---|---|
| CLASS | "at least" CLASS II: Approximation schemes (arXiv:1104.2933); "Feel free to cite more CLASS papers!" | [sec: web https://github.com/lesgourg/class_public README, read 2026-10-19] |
| CAMB | the CAMB 2 paper (arXiv:2607.14854) and the closed-FRW paper (arXiv:astro-ph/9911177), "and references therein as appropriate" | [sec: web https://github.com/cmbant/CAMB README, read 2026-10-19] |
| CCL | arXiv:1812.05995 and a link to the repository; for external packages used through CCL (CLASS, CAMB, FAST-PT, velocileptors, emulators), follow their licences and cite their papers; no version or DOI rule stated | [sec: web https://ccl.readthedocs.io/en/latest/source/citation.html, read 2026-10-19] |
| flip | arXiv:2501.16852 and arXiv:2303.01198 | `physics-and-methods.md#flip` |
| cosmoprimo, desilike, pypower, pycorr | no code paper found: cite the repository | `SKILL.md` |

Neither the CLASS nor the CAMB README asks for a version number. The CAMB
README lists branches that matter for reproduction: "1.6.6 is the last
Planck-era precision version, as used by Planck analysis", and `CAMB_v0`
"the old Fortran-oriented ... version as used by the Planck 2018
analysis" [sec: web, CAMB README, read 2026-10-19]. The referee check that
a paper names the version is in `systematics.md#what-a-referee-checks`.

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Self-convergence or cross-code comparison
<!-- key: self-convergence-or-cross-code-comparison -->

Self-convergence is cheap and automatic but cannot find an error shared
by default and boosted runs (a wrong equation, a convention), nor one in
a setting the boosts do not reach. In 2011, CAMB with all accuracy boosts
at 3 still differed from CLASS by ≃ 0.7 % in unlensed TT at low ℓ and
0.1 % at high ℓ, and raising the boosts further changed nothing; two
hard-coded quantities were responsible, the Bessel-function sampling
(Δx = 1 for x > 25; 0.2 moved the C_ℓ by ≈ 0.1 %) and the time sampling
of the free-electron fraction (`nthermo`) (arXiv:1104.2934, Sect. 2.1)
[src].
Cross-code comparison can, but only after the physics is matched by hand
(recombination, helium, neutrinos, lensing cutoff, non-linear model,
Step 1), and then it tests only numerics. CAMB v2 uses both and adds the
regression suite [src: arXiv:2607.14854, Sect. IX]. CAMB distributes a
"classy-comparisons" agent skill to guide CLASS installation and
like-with-like runs [src: Sect. X].

### Modular framework or monolithic code
<!-- key: modular-framework-or-monolithic-code -->

CosmoSIS lists the costs of modularity: wrapper overhead and one more
place for bugs; interpolation, because data passed between modules "is
not sampled at the points that a module is expecting", mitigated by
declaring sample spacings and checking accuracy, "some burden on the user
to perform validation tests"; lost short-cuts; more room for misuse when
errors are cosmology dependent; and the temptation to over-complicate
pipelines [src: arXiv:1409.3409, Sect. 3.2]. The gain is that every
output records each module's options (Step 5). cloelib states the same
trade-off from the other side: extending CLOE "often required intrusive
modifications ... leading to the accumulation of technical debt", which
motivated its protocol layers [src: arXiv:2605.23839, Statement of need].

### A fork on an old base version
<!-- key: a-fork-on-an-old-base-version -->

A modified code inherits the numerics of the base version it forked. In
the 2017 comparison, a lensing-spectrum deviation of order 3 % and a
steep rise of P(k) differences above k ≃ 0.1 h Mpc⁻¹ appeared for ΛCDM
too and were attributed to "an inaccuracy in CLASS v1.7, which
CLASS-LVDM is based on, and not by the modification itself"; the issue is
absent in hi_class, based on a newer CLASS [src: arXiv:1709.09135,
Sect. IV.5]. Before a fork is compared or used, compare its ΛCDM limit
with the current base code.

### Code developed with AI agents
<!-- key: code-developed-with-ai-agents -->

CAMB v2 reports that its new low-level approximations and precision
tuning were developed by agents with a human in the loop, against the
deterministic `check_accuracy` harness [src: arXiv:2607.14854, Sect. X].
For accuracy failures it separated roles: a subagent reproduces one
failure in a disposable copy and drills down to the responsible lines, an
orchestrator patches one failure at a time, a read-only subagent audits
scope, gating and physical motivation; the rule is locality, a fix
"gated in its natural coordinate (k, ℓ, redshift, or ν/l)" [src: same].
The authors' finding: the agents "were consistently good at isolating a
minimal change that restores a test harness pass, but markedly less
reliable at finding the right one", since a patch could meet the
tolerances "while resting on a numerical coincidence rather than a
physical mechanism"; the human rejected "passing-but-unphysical
candidates" [src: same]. What it costs: a harness pass is necessary, not
sufficient, and the physical review stays with the developer.

### Pinning an old version or moving to the current one
<!-- key: pinning-an-old-version-or-moving-to-the-current -->

Pinning keeps a published result reproducible; moving gains accuracy.
For CAMB the gap is quantified: v1.6.6 at its historical lensing cutoff
reaches 1.5 % in TT by ℓ = 3000 against the boosted reference
(arXiv:2607.14854, Sect. IX; `results.md#camb-v2-default-accuracy-arxiv-2607-14854`).
A facade may pin the old behaviour for you: pyccl 3.3.6 sets CAMB `AccuracyTarget = 0`
and `lens_potential_accuracy = 0` (`deep/theory-facades.md`, Step 2).
Record which one was used (Step 5).

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Self-convergence reference | main accuracy boosts doubled (strict preset: three, denser high-ℓ sampling) | CAMB v2 | arXiv:2607.14854 | Sect. IX, Fig. 3 caption |
| Validation grid | more than 100 parameter files | CAMB v2 | arXiv:2607.14854 | Sect. IX |
| Near-flat continuity test | down to \|Ω_K\| ∼ 10⁻⁶ | CAMB v2 | arXiv:2607.14854 | Sect. IX |
| Grid Δχ², SO-like proxy | median ≃ 0.4, maximum ≃ 1.0; coherent errors at tolerance edges could give ≃ 34 | CAMB v2 defaults | arXiv:2607.14854 | Sect. IX |
| Accepted errors in a fast Bessel path | a handful between 10⁻⁴ and 2 × 10⁻⁴ | CAMB v2 tuning | arXiv:2607.14854 | Sect. X |
| Cross-code like-for-like settings | Y_He = 0.245, Planck-era RECFAST, one 0.06 eV eigenstate, HMcode-2020 no feedback; CLASS to ℓ = 8000 | CAMB v2 vs CLASS 3.3.4 | arXiv:2607.14854 | Fig. 3 caption |
| Precision cost cap | ≤ 3–4 times slower than standard precision | MG solver comparison | arXiv:1709.09135 | Sect. IV |
| Default lensed-CMB accuracy relative to other spectra | 1–2 orders of magnitude worse | MG solver comparison | arXiv:1709.09135 | Sect. IV |
| CAMB–CLASS low-ℓ TT difference in MG and ΛCDM | up to ≃ 0.5 % for ℓ ≲ 100 | hi_class vs EFTCAMB | arXiv:1709.09135 | Sect. IV.1 |
| Inherited base-code deviation | ≃ 3 % in lensing spectrum, ΛCDM included | CLASS-LVDM (CLASS v1.7) vs EFTCAMB | arXiv:1709.09135 | Sect. IV.5 |
| Planck nuisance-parameter count cited as motivation | about 20 | CosmoSIS | arXiv:1409.3409 | Sect. 2 |
| Three-code agreement after removing instabilities | < 0.1 % in matter P(k); below sampling variance to ℓ = 3000 (TT, TE, EE), ≃ 0.1 % over most of it | 2003 comparison | arXiv:astro-ph/0306052 | abstract |
| CLASS reference precision | 0.01 % in C_ℓ^TT, P(k) for 2 ≤ ℓ ≤ 3000, k ≤ 1 h Mpc⁻¹; EE twice larger | `cl_ref.pre`, `pk_ref.pre` | arXiv:1104.2934 | Sect. 3 |
| CLASS vs CAMB reference spectra | Δχ² = 0.027 | simplified Planck, ℓ ≤ 3000 | arXiv:1104.2934 | Sect. 3 |
| CAMB default accuracy, 2011 | Δχ² = 368 (10 with `accuracy_boost` 1.5, `l_sample_boost` 1.2) | same | arXiv:1104.2934 | Sect. 3 |
| Δχ² ∼ 1 in C_ℓ terms | ≃ 0.1–0.2 %, except largest and smallest scales | same | arXiv:1104.2934 | Sect. 3 |
| CCL benchmark agreement, χ and D | 𝒜 = 5 × 10⁻⁷ and 6 × 10⁻⁶, 0.01 ≤ z ≤ 1000 | CCL v1 | arXiv:1812.05995 | Sect. IV, table |
| CCL parameter-space test | 100 Latin-hypercube points in 5 ΛCDM parameters | vs CLASS v2.6.3 | arXiv:1812.05995 | Sect. IV.2.3 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **A harness pass taken as correctness.** Passing tolerances can rest on
  a numerical coincidence (Choices, AI agents). Test: ask for the physical
  mechanism of each fix and for a check outside the tuned configuration.
- **False alarms where spectra cross zero.** Relative differences of TE,
  or of EE at low ℓ, look like failures [src: arXiv:2607.14854, Sect. IX;
  arXiv:1709.09135, Sect. IV.1]. Use the normalised TE error.
- **A grid that cannot fail.** Small extension parameters hide
  differences; configurations outside the grid (source counts, 21 cm) can
  fail at the ℓ_max edge (Step 3). Test: include an excluded but large
  value of each extension parameter, and the analysis' own configuration.
- **A fork compared without its ΛCDM limit.** Differences from an old
  base version are then attributed to the modification (Choices, fork).
- **Rerunning an archived input with new defaults.** An input file that
  omits a setting picks up whatever the current version defaults to; one
  written by a generator carries the generator's values (Step 5). Test:
  diff the versions and settings stored in the output of the old and new
  runs.
- **Modified external code not archived.** Cobaya records versions, but a
  user-modified code is reached by path only (Step 5). Archive the source
  or commit of the modified code with the chains.
- **Interpolation between modules.** In a modular pipeline a module may
  receive data on a grid it did not ask for [src: arXiv:1409.3409,
  Sect. 3.2]. Test: the CosmoSIS `test` sampler saves every module's
  output for a single parameter point so it can be compared with
  expectations, and can time each module [src: App. A.4].
- **Boost parameters that do not boost everything.** Hard-coded sampling
  in a code escapes its global boosts, and a self-convergence test then
  converges to the wrong answer (Choices, first item). Test: compare with
  an independent code at reference precision, or check that all accuracy
  parameters are exposed, as CLASS's precision structure does.
- **"Tested" read as unit-tested.** CosmoSIS does not enforce unit tests
  for contributed modules, "since most cosmologists are not trained
  programmers", but encourages them and provides a mechanism to run them
  [src: arXiv:1409.3409, Sect. 6.2]. Check what a code's test suite
  actually covers before relying on it.

## Reading list
<!-- key: reading-list -->

- Method: Lewis 2026, arXiv:2607.14854 — Sect. IX for the three
  complementary checks and the grid; Sect. X for agent-assisted
  development and its failure mode.
- Method: Lesgourgues 2011, arXiv:1104.2934 (CLASS III) — Sect. 2.1 for
  hard-coded CAMB settings found by cross-code comparison, Sect. 3 for
  reference and Δχ²-calibrated precision files; arXiv:1104.2932, Sect. 2.3,
  for the single precision structure.
- Critique: Seljak et al. 2003, arXiv:astro-ph/0306052 — the first
  three-code Boltzmann comparison.
- Method: Brinckmann et al. 2018, arXiv:1804.07261 — App. C, what
  MontePython writes with its chains.
- Method: Bellini et al. 2017, arXiv:1709.09135 — Sect. IV for how a
  multi-code comparison chooses targets, models and the precision budget.
- Foundation: Chisari et al. 2018, arXiv:1812.05995 — Sect. IV for
  benchmarks, per-quantity accuracy 𝒜 and the Latin-hypercube test;
  Sect. V for tests, CI and Docker.
- Method: Torrado & Lewis 2020, arXiv:2005.05290 — Sect. VI for stock
  external codes and version recording; App. B for a generated input.
- Method: Zuntz et al. 2014, arXiv:1409.3409 — Sect. 3.2 for the costs of
  modularity; App. A.4 for the single-point test run.
- Application: Bonici et al. 2026, arXiv:2605.23839 — protocol checks and
  environment files.
- Review: Alvarez et al. 2022, arXiv:2203.07347 — Sect. 5.3, the
  community statement of the verification and validation problem.

## Not verified
<!-- key: not-verified -->

- The CAMB README's two statements on which version Planck used (1.6.6
  "as used by Planck analysis", `CAMB_v0` "as used by the Planck 2018
  analysis") are quoted as read; which Planck analyses each refers to was
  not checked.
- The coverage of the CAMB, CCL and CLASS test suites (which outputs,
  which tolerances) was not read; the CLASS README states nothing about
  testing, although the repository lists a `test` directory and workflow
  files.
- Whether Cobaya's current output still stores external-code versions as
  described in 2021 was not checked in a current run.
- No paper on software-citation or reproducibility practice specific to
  cosmology was found in the searches made; Zenodo or ASCL records of the
  codes were not looked up.
- MontePython: only App. C of arXiv:1804.07261 was read; whether it
  records code versions was not found. desilike has no code paper found;
  its test practice was not read.
- The body of Seljak et al. 2003 (which sources of instability) was not
  read; only its abstract.
