# Level test — third L3 test of 2026-10-20, part b

Item C of `docs/plans/2026-10-20-plan.md` ("the domains not yet tested"), part 3b.
Five skills: `cosmo-dark-energy-modified-gravity`, `cosmo-neutrinos-dark-matter`,
`cosmo-inflation-primordial`, `cosmo-cmb-lss-cross-correlations`,
`cosmo-beyond-two-point`. Forty questions, eight per skill, are in
`docs/tests/levels/l3-questions-3b.md`. Each was answered twice from the skill files
only: an **L2 run** (the skill's `SKILL.md` plus one reference file chosen from the
file map, no `deep/`) and an **L3 run** (the same plus at most one dossier of `deep/`,
chosen from the file map). Model memory was not used to fill gaps. This run tests; no
skill file was changed. Part 3a ran at the same time on other skills and wrote only
its own files.

The file was written progressively, one skill at a time, so that a cut run can be
resumed from the last completed skill.

## Procedure

1. **Questions first.** Written from the five `subtopics.tsv` files, the file names of
   `deep/` and `references/`, and the one-line skill descriptions of the skill listing,
   before any `SKILL.md` body, reference file or dossier of the five skills was opened.
   Per skill, six questions fall one each on the six dossier subtopics and two on
   subtopics whose `files` column lists no dossier (controls).
2. **Preliminaries read.** The second run (`run-2026-10-20-l3-second.md`) and its
   questions (`l3-questions-2.md`), the level table of
   `skills/observational-cosmology/SKILL.md` ("Choosing the level"). Layer check: no
   `.cosmoskill/` in the working directory, its parents or the home directory;
   `COSMOSKILL_HOME` unset; layer `base` for every question.
3. **Isolation.** One session answered all questions: each file was read once and each
   answer was then restricted to the passages of the files assigned to that run. As in
   the earlier runs this is weaker than a fresh session per run; every L2 grade names
   the passage it rests on.
4. **Grading.** (a) Y answers, P partly, N not; (b) locator: Y when the load-bearing
   statements carry paper + section, table or equation. **Tightened rule**: an L2
   answer graded P counts as an L2 failure.
5. **Pass rule per skill.** The L3 run answers (Y) at least 5 of the 6 dossier questions
   with locators, including at least 3 that the L2 run failed (P or N); each L3 question
   loads at most one dossier. Controls should show no L3 gain; when one gains, the
   dossier that served it is named.
6. **Source checks.** At most 10 in all (`fetch_paper.py --grep` or `--section`).
7. **Generality.** Per skill, any answer that leans on one research group's work where
   the field has several is flagged with file and section.

## Files loaded per question

`methods` = `references/physics-and-methods.md`, `syst` = `references/systematics.md`,
`open` = `references/open-questions.md`, `surveys` = `references/surveys-and-data.md`,
`results` = `references/results.md`. Every run also loaded the skill's `SKILL.md`.

| Q | L2 reference file | L3 dossier |
|---|---|---|
| D1 | methods | `deep/wz-reconstruction.md` |
| D2 | methods | `deep/interacting-dark-energy.md` |
| D3 | methods | `deep/fr-screening.md` |
| D4 | methods | `deep/nonlinear-beyond-lcdm.md` |
| D5 | methods | `deep/eg-statistic.md` |
| D6 | surveys | `deep/forecasts-stage-iv.md` |
| D7 (control) | methods | `deep/interacting-dark-energy.md` (closest: "One-sided priors and corner limits"; no model-comparison row) |
| D8 (control) | methods | `deep/forecasts-stage-iv.md` (closest: μ–Σ forecast set-up; no μ–Σ row) |

## Answers, cosmo-dark-energy-modified-gravity

**D1 — w(z) reconstruction: method, correlation prior, artefact or signal.**
- L2 (methods §2.4): table of the six DESI-era reconstructions (binned + PCA, GP,
  crossing statistics, Horndeski correlation prior, joint EFT, SVD) with one-line
  outcomes and identifiers. How each works, how the correlation length and amplitude
  are set, and how a prior-driven artefact is told apart: not in the file. **P.**
- L3: basis forms (arXiv:2503.14743, Eqs. 13, 23, 28–29; arXiv:2405.04216, Eqs. 1,
  5–7), high-z closure, prior table with stated reasons (GP GIG prior on `l_f`,
  App. C; Chebyshev `N(ΛCDM, 3)`, Table 1, App. C; correlation prior Eqs. 6–8 of
  arXiv:2504.06118 from the Horndeski ensembles of arXiv:1703.05297, Table 1), fixed
  or floating fiducial (arXiv:1112.1693, Eqs. 19–21), `Δ ln E` against `N_eff`
  (arXiv:2504.06118, Sect. IV), mock validation including the unrecovered fast-thawing
  mock (arXiv:2503.14743, App. E), PCA caveats (App. B). **Y.**

**D2 — Interacting dark energy: perturbations, stable coupling, distinguishing from w0wa.**
- L2 (methods §2.3): one table row (coupled quintessence or fluid, Li et al. 2026);
  `SKILL.md` says IDE absorbs the same mismatch as `w0wa`. No perturbation treatment,
  no stability condition, no separation test. **N.**
- L3: coupled equations (arXiv:2601.07361, Eqs. 1, 7–8), realisation table, the
  large-scale instability (arXiv:0804.0232) and doom factor (arXiv:0901.1611, Eqs. 13,
  40, 56), ePPF and IDECAMB mapping (arXiv:1404.5220; arXiv:2601.07361, Eqs. 2–3), sign
  conventions table, the dark degeneracy and explicit mapping (arXiv:astro-ph/0702615;
  arXiv:1911.02618, Eqs. 29–30), so only perturbations separate IDE from `w0wa`
  (arXiv:2601.07361, Conclusion); Δχ² split by probe (Table 2). **Y.**

**D3 — f(R): clusters, profiles, galaxy tests; screening; calibrating simulations.**
- L2 (methods §§4.5, 5): KiDS-1000 and DESI DR1 `f(R)` cards (ReACT on HMcode; Yukawa
  growth, screening neglected at `k_max = 0.17`), test table naming cluster abundance,
  lensing versus kinematics, morphology, distance ladder. How screening is modelled per
  test and which simulations calibrate: not in the file. **P.**
- L3: cluster-abundance recipe (HMF ratio times Tinker, arXiv:1412.0133, Eqs. 10–13;
  eRASS1 mass-dependent threshold and screening mass, arXiv:2402.08459, Eqs. 17–21, 32;
  BRIDGE-calibrated nDGP ratio, arXiv:2512.05819, Eq. 19), lensing masses kept GR and
  why, morphology screening map and likelihood (arXiv:2009.08743, Sects. III.1, IV.1.4,
  IV.3), neutrino degeneracy by regime, prior dependence. Cluster profiles and distance
  indicators stay at L2 depth. **Y.**

**D4 — Non-linear scales beyond ΛCDM: choosing the route, scale cuts, validation.**
- L2 (methods §4.5): what DESI DR1 (EdS kernels checked against fkpt), DES Y3 (Halofit
  ratio, Δχ² < 1 linear cuts, 256 of 462 points) and KiDS-1000 (ReACT) did. No
  comparison between routes, no emulators, no general cut rule. **P.**
- L3: regime table (arXiv:2512.09748, Sect. 6), kernel tests by model class (Sects.
  6.1.1–6.1.3; arXiv:2311.13529), `Xi` predictions table, ReACT pseudo-cosmology
  (arXiv:1812.05594, Eqs. 51–54), Euclid cut settings (arXiv:2512.09748, Sect. 2.2),
  theory-error term (arXiv:2409.03524, Eqs. 35–39), prescription-to-prescription biases
  (Tables 8–9), N-body code agreement (arXiv:1506.06384). **Y.**

**D5 — E_G: estimator, scale cuts, magnification, redshift mismatch, ΛCDM expectation.**
- L2 (methods §6): definition, GR and MG forms (arXiv:2401.12971, Eqs. 5–7), reference
  values, lensing tracers, the `Omega_m,0` dependence and posterior-predictive test
  (arXiv:2511.19194). Estimators, scale cuts, magnification and `z_eff` matching: not in
  the file. **P.**
- L3: three forms. Harmonic: `z_eff` reweighting (arXiv:2401.12971, Eqs. 25–28),
  estimator (Eqs. 35–36), magnification factor (Eqs. 41–42), ℓ cuts from `k = 0.2`
  (Sect. VI.1), ratio pdf, PTE tests (Eqs. 66–69). Real space: `Upsilon` statistics and
  ML estimator (arXiv:2507.16098, Eqs. 18–19, 43–46), `R_0` from mocks (Sect. 5).
  Weyl/growth ratio (arXiv:2403.13709, Eq. 3). **Y.**

**D6 — Stage-IV forecast: Fisher or sampling, nuisances, cuts, code validation.**
- L2 (surveys §5): the Euclid cross-correlation statement (FoM × 3, arXiv:1910.09273),
  optimistic and pessimistic settings named, a derived `sigma(wa)` target. How a
  forecast is built or validated: not in the file. **P.**
- L3: observables and Gaussian covariance (arXiv:2512.09748, Sect. 2.2), settings table
  (arXiv:1910.09273, Eqs. 197–198), priors (arXiv:1809.01669, App. I2), derivative
  lessons (arXiv:1910.09273, Sect. 4.5.1; arXiv:2608.03876, Sect. 5.1), sampled
  forecasts and projection effects (arXiv:2510.09153, Sects. 6.3.3, 6.4), FoM
  conventions, Fisher-bias requirement `r = sqrt(b C⁻¹ b)` (arXiv:1809.01669, App. H2),
  code agreement criteria (arXiv:1910.09273, Eq. 65; arXiv:2608.03876, Sect. 4). **Y.**

**D7 (control, model comparison).** L2 (methods §7): statistics table, Wilks with two
degrees of freedom, `Δχ²_MAP` including non-uniform priors, DIC scale, nested sampling
and the fit/Occam split, profile against Bayesian intervals (arXiv:2503.14738,
arXiv:2503.14743, arXiv:2506.12004, arXiv:2508.11811). A parameter on a boundary is not
treated. **P.** L3 (`interacting-dark-energy`, "What goes wrong"): one-sided priors
put ΛCDM on a prior corner, so a marginalised "σ from zero" is not a two-sided test;
check with a profile likelihood. Still no conversion rule for a boundary. **P**, no
gain.

**D8 (control, μ–Σ).** L2 (methods §§4.1, 4.5): forms tied to `Omega_DE(a)`, binned and
scale-dependent forms (arXiv:2411.12026, Eqs. 6–9), DES Y3 linear cuts, CAMB prior
`mu0 < 2 Sigma0 + 1`, growth measures μ and lensing Σ. **Y.** L3
(`forecasts-stage-iv`): adds the μ–η degeneracy direction `Sigma = mu(1 + eta)/2`
(arXiv:2603.11895) and the US/SS bracket. **Y**, no gain needed.

| Q | L2 (a) | L3 (a) | L3 locator | Gain |
|---|---|---|---|---|
| D1 | P | Y | Y | yes |
| D2 | N | Y | Y | yes |
| D3 | P | Y | Y | yes |
| D4 | P | Y | Y | yes |
| D5 | P | Y | Y | yes |
| D6 | P | Y | Y | yes |
| D7 (c) | P | P | Y | no |
| D8 (c) | Y | Y | Y | — |

**Verdict: pass** (6 of 6 with locators; 6 L2 failures answered; one dossier per
question; controls inert). The methods file is a catalogue of what each analysis did;
every "how to choose" question failed at L2.

Generality flags:
- `deep/interacting-dark-energy.md`, Steps 3–5, "Constant, running or binned coupling"
  and Numbers: the perturbation scheme (ePPF), the code (IDECAMB), the 2026 application,
  the binned coupling and the review that frames the dossier come from one group's
  series of papers. No IDE fit with another perturbation treatment or pipeline is
  worked through. The dossier's own "Not verified" notes that no collaboration IDE
  analysis was found.
- `deep/fr-screening.md`, Regime 2: the astrophysical regime, which gives the
  strongest bound, rests on one method paper (arXiv:2009.08743); the distance-indicator
  and cluster-profile tests stay at L2 depth.

Source checks for this skill: E1 (table at the end).

## Answers, cosmo-neutrinos-dark-matter

Files loaded:

| Q | L2 reference file | L3 dossier |
|---|---|---|
| V1 | methods | `deep/neutrino-mass-full-shape.md` |
| V2 | surveys (no reference file mentions PTOLEMY or relic detection; searched all five) | `deep/relic-neutrino-background.md` |
| V3 | methods | `deep/strong-lensing-substructure.md` |
| V4 | methods | `deep/fuzzy-ultralight-dm.md` |
| V5 | methods | `deep/interacting-decaying-dm.md` |
| V6 | methods | `deep/self-interacting-dm.md` |
| V7 (control) | methods | `deep/fuzzy-ultralight-dm.md` (closest: Lyα IGM priors and thermal history; no WDM row) |
| V8 (control) | methods | `deep/neutrino-mass-full-shape.md` (closest: effective-mass peaks; no effective-mass row) |

**V1 — Full-shape Σm_ν: free streaming, cb or total-matter bias, nuisance priors, prior volume.**
- L2 (methods §1.2 and §1.7, "DESI full shape"): the three channels, ΔP/P ≈ −8 f_ν,
  seven EFT nuisances per tracer, the background-only and X_rsd tests (arXiv:2503.14744,
  Sect. VI, Eqs. 39–42). Bias on cb or total matter, kernels and prior-volume handling:
  not in the file. **P.**
- L3: cb prescription in all three pipelines and its reason (arXiv:2404.07269, Eq. 18;
  arXiv:1311.0866), fk-kernels against EdS (arXiv:2404.07269, Eqs. 31–32, Sect. 7.4),
  DESI and external prior tables (arXiv:2411.12021, Table 4; arXiv:2601.16165, Table 2),
  shape-or-wiggles test (arXiv:2407.06117, Sect. V), prior-weight and prior-volume
  diagnostics (arXiv:2411.12021, Sect. 4.5), the geometric origin of both CMB-combined
  gains (arXiv:2601.16165, Sect. 4.3; arXiv:2411.12022, Sect. 4.1). **Y.**

**V2 — Relic-neutrino detection: resolution, rate, clustering, substrate, other routes.**
- L2: no reference file holds the subtopic (the dossier says so in its scope line). **N.**
- L3: capture kinematics and Dirac/Majorana rates (arXiv:1405.7654, Eqs. 37, 44, 53–57),
  resolution criterion Δ ≲ 0.7 m_ν (Fig. 3) and 20 meV for 50 meV masses
  (arXiv:2101.10069), the KATRIN overdensity fit (arXiv:2202.04587, Eqs. 1–4), PTOLEMY
  Asimov forecast (arXiv:1902.05508, Sects. 4, 6), zero-point broadening on graphene
  (arXiv:2101.10069, Eqs. 5–6, Table 1) and the collaboration reply (arXiv:2203.11228,
  Sect. V), simulated clustering factor (arXiv:2306.16444, Sect. 4.1). Other routes: the
  dipole ("wind") and annual modulation with why they are weaker; Stodolsky, coherent
  scattering and ion beams only named as not researched. **Y.**

**V3 — Strong-lensing substructure: flux ratios or gravitational imaging; inference; WDM limit.**
- L2 (methods §§3.2–3.3): probe rows (macromodel multipoles, source size, tidal
  stripping, globular clusters, subhalo prior), half-mode-to-keV relations and the
  confidence criterion (arXiv:2511.07765, Sects. VIII.1, IX). How the inference is run:
  not in the file. **P.**
- L3: the flux-ratio route in full: microlensing-free fluxes and SED separation
  (arXiv:2511.07765, Sects. III, V), hyper-parameters and their ranges (arXiv:2511.07513,
  Sect. IV.3), pyHalo rendering with line-of-sight cone, two-halo term and mass sheets
  (Sect. IV.1.1, Eqs. 13–16), macromodel solved per realisation (Sect. II.2.1, Eqs.
  23–24), Gaussian likelihood against ABC (Eq. 7; arXiv:1908.06983, Eq. 4), KDE and
  convergence (Apps. A–B). Extended arcs enter only as importance weights on the
  macromodel (Eq. 9); gravitational imaging of subhaloes in arcs, the other route the
  question names, is listed as "not read". The choice between the two routes cannot be
  made from the dossier. **P.**

**V4 — Fuzzy dark matter: Lyα, CMB + LSS sub-component, dwarfs; modelling and robustness.**
- L2 (methods §§3.1–3.3): fuzzy transfer-function fit and half-mode mass
  (arXiv:2512.01361, Eqs. 5–7), probe rows for dwarf kinematics and for CMB + galaxy
  spectra. How each limit is produced: not in the file. **P.**
- L3: field-to-fluid switch (arXiv:1410.2896, Eqs. 32–34), fixed-mass sampling and why
  (arXiv:2301.08361, Sect. 3.4; arXiv:2606.06410, Sect. IV), non-linear treatments
  table (one-fluid EFT, two-fluid EFT arXiv:2607.11876 Eqs. 7–10, axionHMcode), Lyα
  modified-initial-condition argument (arXiv:1703.04683), emulators and IGM priors
  (arXiv:2007.12705; arXiv:2606.06969, Sects. 3–4), dwarf-heating inference
  (arXiv:2203.05750, Eqs. 2–4) and its critiques. **Y.**

**V5 — DM–baryon scattering and decays: CMB, satellites, velocity dependence, data choice.**
- L2 (methods §§3.1, 3.5, 5): model rows (σ ∝ vⁿ, −4 ≤ n ≤ 2 from Planck and Lyα,
  arXiv:1311.2937), the two decay models (arXiv:2203.07440), Bayesian against
  frequentist for decays. Satellites for scattering and the data choice: not in the
  file. **P.**
- L3: drag and temperature equations with c_n (arXiv:1311.2937, Eqs. 10–16), three
  bulk-velocity prescriptions (arXiv:1808.00001, Eqs. 4–8) and their cost, interacting
  fraction, satellite half-mode mapping (arXiv:1904.10000, Sect. III, Eq. 8), dedicated
  Lyα simulations against mappings (arXiv:2607.15020, Sects. 2–6), decay equations and
  gauge (arXiv:1606.02073, Sect. 2.2), warm-daughter methods table, prior choices
  (arXiv:2008.09615, App. D). **Y.**

**V6 — SIDM: mergers, cluster densities, dwarf rotation curves; calibration; velocity dependence.**
- L2 (methods §§3.3–3.4): σ/m at a stated velocity, core growth and collapse, the
  cluster-merger probe row (arXiv:1605.04307). Methods and calibration: not in the file.
  **P.**
- L3: cross-section proxies σ_T, σ_V and velocity weighting (arXiv:2011.04679, Eqs. 4–5,
  90–92), merger β statistic and drag model (arXiv:1503.07675, Eq. S1), re-measured
  offsets (arXiv:1701.05877), isothermal Jeans model and ensemble combination
  (arXiv:2006.12515, Eqs. 1–2, 16–17; arXiv:2012.06611, Eq. 9), centroid tests in
  simulations (arXiv:1605.04307, Sects. 4.3, 5). The dossier's scope is groups and
  clusters only: dwarf rotation curves, which the `subtopics.tsv` title names and where
  the velocity-dependent case is decided, are deferred to `open-questions.md`. **P.**

**V7 (control, WDM in the Lyα forest).** L2 (methods §3.2): conversion chain from T(k)
to k_hm, M_hm and keV with every relation and its source (arXiv:astro-ph/0501562;
arXiv:2309.04533; arXiv:2512.01361), sterile-neutrino mapping. Thermal-history
marginalisation: only "thermal history" named and the simulation grid in 1/m_WDM. **P.**
L3 (`fuzzy-ultralight-dm`, Step 4 items 3–4 and "Thermal history in the 2017
analysis"): grids in T₀, γ, z_rei, τ_eff, continuity priors on T₀ and u₀, Gaussian T₀
priors, power-law against jumps and their effect on the limit (arXiv:1703.04683;
arXiv:2007.12705; arXiv:2606.06969). **Y. The control was not inert**: the fuzzy
dossier serves `wdm-lyman-alpha`, whose IGM machinery is the same.

**V8 (control, effective mass).** L2 (methods §§1.4–1.5): three effective-mass
parameters and their implementations (arXiv:2405.00836, Sect. 2.2; arXiv:2503.14744,
App. A, Eq. 48; arXiv:2511.01967, Eq. 1), profile parabola and Feldman–Cousins
(Table 3), tension metrics. **Y.** L3 (`neutrino-mass-full-shape`): adds the external
effective-mass peaks and the two significance constructions (arXiv:2601.16165,
Sect. 4.3). **Y**, no gain needed.

| Q | L2 (a) | L3 (a) | L3 locator | Gain |
|---|---|---|---|---|
| V1 | P | Y | Y | yes |
| V2 | N | Y | Y | yes |
| V3 | P | P | Y | no |
| V4 | P | Y | Y | yes |
| V5 | P | Y | Y | yes |
| V6 | P | P | Y | no |
| V7 (c) | P | Y | Y | yes (control) |
| V8 (c) | Y | Y | Y | — |

**Verdict: fail** on the first clause (4 of 6 answered with locators; 4 L2 failures
answered, so the second clause holds; one dossier per question). Both partial answers
are scope gaps, not errors: `deep/strong-lensing-substructure.md` covers the flux-ratio
route of its subtopic "flux ratios and extended arcs" and not gravitational imaging, and
`deep/self-interacting-dm.md` covers groups and clusters of its subtopic "cluster
mergers, density profiles and rotation curves" and not rotation curves. One control
gained (V7).

Generality flags:
- `deep/strong-lensing-substructure.md`, Steps 1–8 and "Choices": the whole
  forward model (pyHalo rendering, macromodel solver, importance-weighted arcs, KDE
  combination, subhalo priors) is one group's pipeline (arXiv:1908.06983,
  arXiv:2511.07513, arXiv:2511.07765). The gravitational-imaging analyses of other
  groups are cited only as "not read"; the one independent statistic (cusp relation,
  arXiv:2601.16818) gets a paragraph.
- `deep/self-interacting-dm.md`, Step 2b: the profile route rests on the
  Kaplinghat-type isothermal Jeans model in two applications; other halo-structure
  routes (simulation-calibrated profile fits, BCG wobble) are only noted.

Source checks for this skill: E2 and E3 (table at the end).

## Answers, cosmo-inflation-primordial

Files loaded:

| Q | L2 reference file | L3 dossier |
|---|---|---|
| I1 | methods | `deep/slow-roll-model-comparison.md` |
| I2 | methods | `deep/tensor-bmode-likelihood.md` |
| I3 | syst | `deep/bmode-foreground-separation.md` |
| I4 | syst | `deep/delensing.md` |
| I5 | methods | `deep/cmb-bispectrum.md` |
| I6 | methods | `deep/lss-bispectrum-png.md` |
| I7 (control) | syst | `deep/lss-bispectrum-png.md` (closest: PNG-bias treatment; no scale-dependent-bias row) |
| I8 (control) | syst | `deep/tensor-bmode-likelihood.md` (closest: calibration terms; no birefringence row) |

For I3–I5 both `methods` and `syst` were read and the better of the two was assigned
to the L2 run; I5 is graded on either, with the same result.

**I1 — Confronting a model with (n_s, r): e-folds, reheating, evidence, ACT shift.**
- L2 (methods §2, "Slow-roll dictionary"): ε_V, η_V and Hubble-flow definitions,
  Planck first-order constraints (arXiv:1807.06211, Eqs. 37–40), α-attractor formulas
  (arXiv:1311.0472), ASPIC named, "N depends on reheating". Evidence computation and
  which conclusions depend on reheating: not in the file. **P.**
- L3: six levels of model commitment (arXiv:1807.06211, Sects. 4.1–5.4), N_* matching
  (Eq. 47) with Planck's reheating priors, the ASPIC reheating parameter and prior
  (arXiv:1312.3529, Eqs. 10–11) and prior-shape rule (Sect. 2.2), the fast evidence
  route (Eqs. 16–20), leading-order against refined R² predictions (arXiv:2504.20757,
  Eqs. 13–18) and their effect on the P-ACT-LB-BK18 2σ edge, Δχ² against ln B ranking
  (arXiv:1807.06211, Table 5). **Y.**

**I2 — B-mode likelihood: form, windows, simulations, E-to-B leakage, the 95% limit.**
- L2 (methods §3, "BICEP/Keck-style likelihood", "Quoting a limit"): Hamimeche–Lewis on
  66 spectra, 499 simulations, flat prior r ≥ 0, Feldman–Cousins against Bayesian for
  SPIDER (arXiv:2103.13334). Window functions, purification and filtering leakage: not
  in the file. **P.**
- L3: matrix purification (arXiv:1603.05976, Eqs. 11–19, 72–74) against NaMaster pure-B,
  window functions (Eq. 76, Table 2), noise debiasing by sign-flip or cross-splits and
  its trade-off (arXiv:0801.0554, App. C), covariance conditioning (arXiv:1810.05216,
  App. H), the HL likelihood (arXiv:0801.0554, Eqs. 41–49) and its offset form
  (arXiv:2610.18036, Eqs. 29–30), null-test criteria (arXiv:2505.02827, Sect. V.2),
  limit validation on 200 simulations (arXiv:2110.00483, App. E.3). How BK turns the
  posterior into the 95% limit is "not verified" in the dossier; the L2 statement covers
  it. **Y.**

**I3 — Foreground separation for r: which family, decorrelation and moments, residual bias.**
- L2 (syst §§B1, B2, B9): dust-complexity bias up to 0.03 and the d10/s5 findings
  (arXiv:2508.00073, Sect. IV.2), BK18 foreground budget. How to choose between
  parametric cross-spectrum, map-based and blind methods: not in the file. **P.**
- L3: the three SO pipelines (arXiv:2302.04276, Sects. 2.1–2.3, Eqs. 1–12), the
  minimal moment model and its assumptions (arXiv:2011.11575, Eqs. 15–23), cMILC and
  residual templates (arXiv:2603.11026, Eqs. 7–8, 16), LiteBIRD multi-resolution fit
  (arXiv:2202.02773, Sect. 5.2.3), same-simulation comparison (arXiv:2302.04276,
  Table 4), parametric against blind under line-of-sight complexity (arXiv:2411.11649,
  Sect. 4.4), and the recommended rule for choosing pipeline complexity (Sect. 4.4). **Y.**

**I4 — Delensing: internal against external tracers, template, likelihood entry, biases.**
- L2 (syst §B3): template from polarisation plus a tracer, entered as a pseudo-frequency
  map, BK14 gain and CIB–φ misestimate size (arXiv:2011.08163, Sects. IV.2, VI.1). The
  choice of tracers and the internal-delensing bias: not in the file. **P.**
- L3: multitracer co-addition (arXiv:2405.01621, Eqs. 12–13), E filter, gradient-order
  template (arXiv:2110.09730, Eqs. 17, 24) and why (arXiv:2010.14286), map subtraction
  against cross-spectral use and their equivalence (arXiv:2405.01621, Eqs. 14–24),
  efficiency definitions (arXiv:2511.21949, Eqs. 32–33, 44–45), internal-delensing bias
  and the cut-not-model rule (arXiv:2007.01622, Sect. 8), its appearance in ACT data
  (arXiv:2511.21949, App. C). **Y.**

**I5 — CMB bispectrum: KSW, binned, modal; linear term; lensing and point sources; validation.**
- L2 (methods §5, "CMB bispectrum estimators"; syst §§C1–C3): estimators named with
  their foundations, Planck set-up, lensing-subtraction sizes and joint fit
  (arXiv:1905.05697, Table 5). How the estimators differ in construction, how the linear
  term is built and the validation sequence: not in either file. **P.**
- L3: optimal estimator and its linear term (arXiv:1905.05697, Eqs. 25–28), KSW
  (arXiv:astro-ph/0305189, Eqs. 6–14), binned with the cos²θ loss (arXiv:0911.1642,
  Eqs. 21–34, Table 2), modal and its convergence (arXiv:0912.5516, Eqs. 81–86), the
  contaminant-bias and joint-fit formulae (arXiv:2504.00884, Sect. 3.2), the eight-step
  Planck validation with stated criteria (arXiv:1502.01592, Sects. 5.1–5.2;
  arXiv:1905.05697, Sect. 6), estimator choice table. **Y.**

**I6 — Galaxy-bispectrum f_NL: model, b_φ prior, window, covariance; map-level comparison.**
- L2 (methods §5, "Galaxy bispectrum"): one-loop EFT fits named (arXiv:2201.07238,
  arXiv:2201.11518, arXiv:2512.04266), prior dependence 600 → 300, BORG forecast
  σ = 2.3 (arXiv:2507.15819). **P.**
- L3: shapes and template caveat (arXiv:2201.07238, Eqs. 2–5, footnote 2), the three PNG
  channels (Eqs. 8–12; arXiv:2512.04266, Eqs. 20–26; arXiv:2204.01781, Eq. 34), PNG-bias
  table by analysis, window-free estimators (arXiv:2107.06287), cuts and their reasons,
  perturbativity prior (arXiv:2201.11518, Eqs. 36, 45–46, 50), simulation validation and
  theory bias (arXiv:2507.22110, Sect. 5.3), simulation-based priors (arXiv:2402.13310).
  Map-level inference: "no analysis read here; see `cosmo-beyond-two-point`", so the
  comparison rests on the one L2 forecast number. The subtopic title names "map-level
  inference"; the dossier covers only the bispectrum half. **P.**

**I7 (control, scale-dependent bias).** L2 (syst §§D1–D2b): b_φ sizes for BOSS and DESI
(arXiv:2205.05673; arXiv:2209.07251; arXiv:2411.17623), simulation priors on p
(arXiv:2602.12357), imaging-weight budget (arXiv:2411.17623, Table 11), integral
constraints. **Y.** L3 (`lss-bispectrum-png`, Step 3): per-sample p values and the reason
for fixing PNG biases. **Y**, no gain needed.

**I8 (control, birefringence).** L2 (syst §§H, H1–H2): the three calibration routes,
dust EB as an effective angle (arXiv:2201.07682, Eqs. 1–2), ACT optics priors and
leakage (arXiv:2509.13654, Tables 2–3), joint ACT + Planck variations
(arXiv:2608.06480). **Y.** L3: no birefringence content. **Y**, no gain.

| Q | L2 (a) | L3 (a) | L3 locator | Gain |
|---|---|---|---|---|
| I1 | P | Y | Y | yes |
| I2 | P | Y | Y | yes |
| I3 | P | Y | Y | yes |
| I4 | P | Y | Y | yes |
| I5 | P | Y | Y | yes |
| I6 | P | P | Y | no |
| I7 (c) | Y | Y | Y | — |
| I8 (c) | Y | Y | Y | — |

**Verdict: pass** (5 of 6 with locators; 5 L2 failures answered; one dossier per
question; controls inert). `systematics.md` answers both controls in full with
per-analysis budgets, as `cosmo-weak-lensing` did in the second run.

Generality flags:
- `deep/lss-bispectrum-png.md`, Steps 2–6 and "Choices": five of the eight papers read
  (arXiv:2201.07238, arXiv:2204.01781, arXiv:2402.13310, arXiv:2512.04266,
  arXiv:2107.06287) come from one group's EFT and estimator line; the second pipeline
  (arXiv:2201.11518) is the contrast. The DESI DR1 P + B numbers are an external
  reanalysis, which the dossier says; no collaboration bispectrum PNG analysis is
  worked through.
- No flag on the other four dossiers: the B-mode dossiers draw on BICEP/Keck, SPT-3G,
  SO and LiteBIRD papers; the bispectrum dossier on Planck and two independent
  estimator groups.

Source checks for this skill: E4 (table at the end).

## Answers, cosmo-cmb-lss-cross-correlations

Files loaded:

| Q | L2 reference file | L3 dossier |
|---|---|---|
| X1 | methods | `deep/ksz-gas-profiles.md` |
| X2 | methods | `deep/ksz-velocity-reconstruction.md` |
| X3 | methods | `deep/tsz-cross-correlations.md` |
| X4 | syst | `deep/isw.md` |
| X5 | methods | `deep/cib-cross-correlations.md` |
| X6 | methods | `deep/other-secondaries.md` |
| X7 (control) | methods | `deep/cib-cross-correlations.md` (closest: lensing normalisation per region; no lensing-tomography row) |
| X8 (control) | syst | `deep/cib-cross-correlations.md` (same) |

Both `methods` and `syst` were read; for X1–X3 and X6 neither alone answers and
`methods` was assigned; for X4 and X8 `syst` answers and was assigned.

**X1 — kSZ gas profiles: which estimator, τ–velocity degeneracy, profile to feedback, contamination.**
- L2 (methods §§3.2–3.3): estimator table with what each needs, the DESI × ACT CAP
  stack with r = 0.65 (arXiv:2503.19870), the three-step route from profile to
  feedback (halo masses from lensing or HOD, then simulations or GNFW). How the profile
  is forward-modelled, the gas-model priors, and contamination and miscentring in the
  stack: not in the file (contamination is in `syst` §§10–11). **P.**
- L3: forward-model chain (arXiv:2009.05558, Eqs. 6–8; arXiv:2507.14136, Eqs. 10–11),
  GNFW with priors and truncation (arXiv:2009.05558, Eq. 16; arXiv:2604.19744,
  Eqs. 23–24), baryonification and BCemu (arXiv:2512.02954, Eqs. 5–9, Table 1),
  harmonic template with HOD marginalisation (arXiv:2604.19744, Eqs. 10–18, 33, 36–37),
  simulation stacking with lensing-mass matching (arXiv:2510.15822, Eqs. 1–5), the
  lensing/kSZ ratio (arXiv:2609.22466, Eqs. 14–16, 25), projected field with
  α-cleaning (arXiv:2102.01068, Eqs. 3–9, 20), the non-linear velocity terms
  (arXiv:2607.23339, Eq. 7), satellites and miscentring tests. **Y.**

**X2 — kSZ velocity reconstruction: estimator, b_v, P_ge and foregrounds, f_NL from P_gv.**
- L2 (methods §3.2, "Velocity reconstruction"): ⟨v̂_r⟩ = b_v B n_v v_r, the b_v
  integral, the four-parameter LRG fit and the hmvec fiducial (arXiv:2604.04867,
  Sect. 5.2). The filter and estimator construction, noise, foreground monopole and
  window treatment: not in the file. **P.**
- L3: CMB filter (arXiv:2604.04867, Eqs. 20–21), 3D estimator and normalisation
  (Eqs. 19, 22–24), 2D estimator (arXiv:2506.21684, Eqs. 8–13), N⁽⁰⁾ and the
  N-body excess (arXiv:2010.07193, Eq. 27, Sects. V.2, VI.4), spin-ℓ multipoles
  (arXiv:2604.04867, Eqs. 28–32), the linear model with b_Φ (Eqs. 6–17), surrogate
  fields (Sect. III.5), the fit order with foreground monopole first (Sects. V.1–V.2),
  symmetry arguments against lensing bias, null-test criteria table. **Y.**

**X3 — tSZ cross-correlations: y map, ⟨bP_e⟩, pressure models, CIB and radio leakage.**
- L2 (methods §4): statistics table, ⟨b_h P_e⟩ ∝ S_8^3 in FLAMINGO
  (arXiv:2605.11083), deprojection options and the CIB SED with its moment
  (arXiv:2506.07432, App.). How ⟨bP_e⟩ is extracted and how the pressure model enters,
  and the size of the leakage: not in the file (the leakage is in `syst` §3). **P.**
- L3: ⟨b_h P_e⟩ definition and halo-model form (arXiv:2605.11083, Eq. 2;
  arXiv:2210.08633, Eq. 18), measurement and jackknife covariance (Sect. 4.2, Eq. 26),
  GNFW halo model in two regimes (Eqs. 4–23, Sect. 4.3), coupled gas model and priors
  for shear × y (arXiv:2506.07432, Eqs. 1–4, Table 1), HMx, FLAMINGO amplitude
  (arXiv:2609.31774), map-level against spectrum-level separation (Eqs. 10, 16–18),
  the measured CIB shift of b_H (arXiv:2210.08633, Sect. 4.5, Table 4). **Y.**

**X4 — ISW: significance, amplitude, stacking excess.**
- L2 (syst §13): stacked supervoid A ≈ 4–5 against the matched filter 1.64 ± 0.53 and
  matched-mock stacks −0.10 ± 0.69 (arXiv:1811.07812; arXiv:1608.08638;
  arXiv:2105.11936), unWISE per-sample amplitudes with 300 FFP10 covariances and the
  expected significance (arXiv:2110.13959, Sect. 5.1), the mitigation rule (fix the
  catalogue and filter first, matched mocks, report the full cross-correlation). **Y.**
- L3: adds the three significance conventions (arXiv:1710.03238, Sects. VII.1–VII.2),
  covariance choices, the matched-filter construction (arXiv:1608.08638, Eqs. 2–11) and
  blind stacking (arXiv:2105.11936, Sects. 3.1–3.3). **Y**, no gain needed.

**X5 — CIB: dust cleaning, CIB model, delensing or f_NL use.**
- L2 (methods §6): uses (delensing, f_NL from CIB × κ, star formation) and origins.
  Map cleaning, model, priors and data vector: not in the file. **P.**
- L3: the three map families and HI as an ILC channel (arXiv:1905.00426;
  arXiv:2405.13470, Eqs. 9–10, Sect. V.1), mean-subtraction transfer, disjoint regions,
  the linear CIB model (arXiv:2605.03783, Eqs. 18–27, after arXiv:1801.10146), data
  vector and why the auto-spectrum is restricted (Sect. III.4), priors (Table 1),
  covariance and normalisation (Eqs. 31–32), the CIB in a delensing co-add
  (arXiv:2511.21949, Eqs. 25, 27, 42), map choice by scale. **Y.**

**X6 — Moving lens, polarised SZ, screening: estimators, significance, contaminants.**
- L2 (methods §7): one row per effect with the estimator in a phrase and its paper;
  the screening null of arXiv:2401.13033. Significances and contaminants per effect:
  not in the file. **P.**
- L3: moving-lens estimator, covariance and symmetry arguments (arXiv:2605.18938,
  Eqs. 4–26, Sects. III.4, VI.2), sign estimator and lensing-safe filters
  (arXiv:2401.13033, Sects. II.1–VI.1), lensing share of the stacked screening
  signal (arXiv:2506.17379), power-spectrum screening (arXiv:2608.27458), pSZ
  bispectrum and b_q (arXiv:2607.16071), rotational kSZ, null suites. **Y.**

**X7 (control, lensing tomography).** L2 (methods §§2.1–2.7): Limber kernels with
magnification (arXiv:2407.04607), model table (HEFT and others), quoted amplitudes and
the four exponents, MC normalisation, dN/dz routes, the two main analyses side by side.
**Y.** L3 (`cib-cross-correlations`): only the per-region normalisation. **Y**, no gain.

**X8 (control, lensing-map systematics).** L2 (syst §§1–2): normalisation sizes and
mitigation (arXiv:2309.05659; arXiv:2407.04606), foreground biases with and without
profile hardening, the hardening estimators and the null-test suite. **Y.** L3: no
further content. **Y**, no gain.

| Q | L2 (a) | L3 (a) | L3 locator | Gain |
|---|---|---|---|---|
| X1 | P | Y | Y | yes |
| X2 | P | Y | Y | yes |
| X3 | P | Y | Y | yes |
| X4 | Y | Y | Y | — |
| X5 | P | Y | Y | yes |
| X6 | P | Y | Y | yes |
| X7 (c) | Y | Y | Y | — |
| X8 (c) | Y | Y | Y | — |

**Verdict: pass** (6 of 6 with locators; 5 L2 failures answered; one dossier per
question; controls inert).

Generality flags:
- `deep/cib-cross-correlations.md`, Steps 1–6: the f_NL route rests on one group's
  sequence of maps and analyses (arXiv:2210.01049, arXiv:2405.13470,
  arXiv:2605.03783), and the CIB model step uses only the linear model of
  arXiv:1801.10146; the other CIB halo models that arXiv:2405.13470 compares are
  "not read".
- `deep/ksz-gas-profiles.md`, Steps 1–6: every analysis worked through uses ACT maps
  with BOSS or DESI tracers; kSZ profile work with SPT or Planck data appears only in
  L2.

Source checks for this skill: E5 (table at the end).

## Answers, cosmo-beyond-two-point

Files loaded:

| Q | L2 reference file | L3 dossier |
|---|---|---|
| T1 | methods | `deep/void-finding-size-function.md` |
| T2 | methods | `deep/void-galaxy-rsd-ap.md` |
| T3 | syst | `deep/void-lensing-cmb.md` |
| T4 | methods | `deep/emulator-summary-statistics.md` |
| T5 | methods | `deep/field-level-inference.md` |
| T6 | methods | `deep/simulation-based-inference.md` |
| T7 (control) | methods | `deep/simulation-based-inference.md` (closest: Beyond-2pt SBI P + B data vector; no bispectrum-window row) |
| T8 (control) | syst | `deep/simulation-based-inference.md` (closest: DES Y3 lensing SBI set-up; no baryon or IA row) |

Both `methods` and `syst` were read in full; `results` and `open` were searched for
T3. For T2, T4 and T5, `syst` answers other parts of the question but not the
whole, with the same grade; for T3 none of the three (`methods` §2.4, `syst`
§§2.6–2.7, `results` §2.3) answers, and `syst` was assigned. Layer `base`
(no `.cosmoskill/`, `COSMOSKILL_HOME` unset).

**T1 — Void finding and the VSF: choice of finder, Vdn with calibrated threshold, tracer bias, mocks.**
- L2 (methods §§2.1–2.2): finder table (VoidFinder, WVF, ZOBOV, VIDE, REVOLVER,
  voxel, spherical, V², back-in-time), "statistics from different finders are not
  interchangeable", the Colberg et al. comparison (arXiv:0803.0918); two-barrier
  model, Vdn within 16% (arXiv:1304.6087), extended Vdn with nuisance parameters tied
  to the large-scale bias and calibrated on mocks (arXiv:2205.11525,
  arXiv:2212.03873), the free-threshold alternative (arXiv:2501.07817). How to choose
  a finder, the threshold, the bias mapping and how mocks calibrate it: not in the
  file. **P.**
- L3: VIDE centre and radius (arXiv:2212.03873, Eq. 8), cleaning to the model's void
  definition (Sect. III.2), threshold −0.7 and its trade-off with the −0.6 rerun
  (arXiv:2205.11525, Sect. 2.2), radius cuts in units of the mean separation (Sect.
  III.4, App. C.3), multiplicity function and Vdn (Eqs. 1–3), Bernardeau mapping
  (Eq. 4), tracer bias ℱ(b_eff σ8) (Eqs. 6–7), AP radius (Eq. 5), Poisson likelihood
  (Eq. 9); calibration on 100 Patchy mocks, fixed against relaxed (Table 1) and the
  cost of weaker calibration (App. C.1), mock scatter above Poisson (Sect. III.4); the
  free-threshold route (arXiv:2501.07817, Sect. 3, Table 2). Finder choice: watershed
  plus cleaning against a spherical finder built for the model, whose profile bias
  matches the count bias while cleaned VIDE voids need b_v ≈ 2 against 2.9
  (arXiv:2605.03779, Sect. 5.3); moving barrier against Vdn (arXiv:2401.14451,
  Sect. 5.1). REVOLVER is not treated for the VSF. **Y.**

**T2 — Void–galaxy RSD and AP: redshift-space model, covariance, redshift-space selection.**
- L2 (methods §2.3): the observable, the linear outflow v_r = −(1/3) f a H r Δ, the
  founding table (linear model inside the void, arXiv:1712.07575; reconstruction
  before finding, arXiv:1805.09349), the two schools in a paragraph, the reference
  analysis (REVOLVER after reconstruction, ξ_0 and ξ_2, four parameters, data vector
  recomputed across β, 1000 mocks with the Percival posterior; arXiv:2205.06258,
  Sects. 3.2, 3.6, Eqs. 18–22). The model equation, where the velocity profile and
  dispersion come from, void-centre displacement, the jackknife route and the
  deprojection school's treatment of selection: not in the file (selection sizes are
  in `syst` §2.1). **P.**
- L3: where voids are found and why (arXiv:2205.06258, Eq. 3, Sects. 3.1, 3.5),
  centre definitions (Sect. 3.2; arXiv:2007.07895, Eqs. 37–38; arXiv:2007.09013,
  Sect. 4.5.6), cuts table, estimators with void randoms (arXiv:2205.06258, Eq. 5;
  arXiv:2007.07895, Eq. 40), the pair-conserving model with linear outflow and
  Gaussian dispersion (arXiv:2205.06258, Eqs. 11–13), its linear form
  (arXiv:1712.07575, Eqs. 14–15) and the ratio estimator (arXiv:2007.07895,
  Eqs. 34–36; arXiv:2007.09013, Eq. 24), the 𝓜–𝓠 model for redshift-space selection
  (arXiv:2007.07895, Eq. 44, Sect. 3.5), real-space ingredients side by side (BigMD
  templates, Eq. 15; inverse Abel, Eq. 27; linear bias wrong by about 25% inside R,
  arXiv:1712.07575, Sect. 3.2), AP scaling (arXiv:2205.06258, Eqs. 16–17), covariance
  from 1000 mocks with β-grid likelihood interpolation (Eqs. 18–22, Sect. 3.6) against
  void jackknife (arXiv:2007.07895, Sect. 3.3), void-centre off-centring
  X̃ = X + V(1 + z)/H and ellipticity selection (arXiv:2107.01314, Eq. 9, Sect. 6),
  AP-only reconstructed-space variant (arXiv:2509.08884, Sects. 5.1–5.2). **Y.**

**T3 — Void lensing and CMB imprints: measurement and model, void sample, significance of an excess.**
- L2 (syst §§2.6–2.7): void bias from lensing, 2.45 ± 0.36 (arXiv:2507.13450); the
  CMB-lensing deficit of photometric voids gone once mocks match sparseness and
  photo-z errors (arXiv:2412.02761). `results` §2.3 adds the void-in-void and
  void-in-cloud amplitudes; `open` §2.6 the single-group ISW sign-change claim
  (arXiv:2506.08832). Estimators, model, covariance and the significance construction:
  in none of the files. **P.**
- L3: sample table with finder reasons (arXiv:2507.13450, Sect. 2.3; arXiv:2203.11306,
  Sect. 2.3; arXiv:2412.02761, Sect. 3.2), rescaled stacking and the ΔΣ estimator
  with weights (arXiv:2507.13450, Eqs. 6–8), κ image stack and the void-weighted
  masked-map mean (arXiv:2412.02761, Sect. 3.3), mock-void randoms (arXiv:2507.13450,
  Sect. 3.2), analytic covariance (Eqs. 9–12) against random κ maps (arXiv:2412.02761,
  Eqs. 12–16), HSW fit and a Wilks Δχ² with five degrees of freedom (arXiv:2507.13450,
  Eqs. 17–18, 22–23), template amplitude A_κ (arXiv:2412.02761, Eq. 15) read as a
  consistency test at the mock cosmology, mock matching (Sects. 3.1.1–3.1.2); sample
  dependence: λ_v split (Table 3), deepest and largest DES voids (arXiv:2203.11306,
  Sect. 4), 2D against 3D and rescaled against unrescaled (arXiv:2605.22630,
  Sects. 5.1.4, 5.2.1). The scope line leaves void ISW, supervoid excesses and the
  Cold Spot to `cosmo-cmb-lss-cross-correlations`, so the ISW half of the question
  and the significance of an ISW stacking excess are not answered. **P.**

**T4 — Emulated summary statistics: training, emulator error in the likelihood, scale cuts, HOD validation.**
- L2 (methods §3, §7.1): statistics and emulators (SUNBIRD, AbacusSummit + HOD), the
  result conditional on suite and galaxy–halo model; the density-split covariance
  C_data + C_emu + C_sim with 2048 Patchy, 600 test and 1800 AbacusSummit mocks and
  the Percival factor (arXiv:2309.16541, Eqs. 15–20), fixed θ_*, errors that stop
  shrinking below 20 h⁻¹Mpc (Sect. 4.4.2), the MF pipeline (arXiv:2501.01698,
  Sects. 3.6, 6.3), non-HOD test sets named. Training design (HOD parametrisation and
  priors, number of draws, network and loss), how C_emu is estimated and how much HOD
  freedom to allow: not in the file. **P.**
- L3: suite and cosmology grid (arXiv:2309.16539, Sect. 2.2.1, Table 1), HOD families
  with assembly and velocity bias and their reasons (Eqs. 7–10; arXiv:2310.16116,
  Sect. IV.2; arXiv:2405.02252, Sect. V.5.2), density matching as a hidden prior
  (arXiv:2501.01698, Sect. 3.6.1, Eq. 23), three levels of survey realism
  (arXiv:2309.16539, Sects. 2.2.3–2.2.4; arXiv:2310.16116, Sect. IV.3;
  arXiv:2501.01698, Sect. 3.3), training sets and losses (arXiv:2309.16539, Eq. 13),
  C_emu from test-set residuals because σ_pred is over-confident (Sect. 3.1.2,
  Eqs. 15–16), dropping C_emu biases the Nseries fit by more than 3σ
  (arXiv:2309.16541, Sect. 4.4.4), small scales and the failed kNN DD bins
  (arXiv:2405.02252, Sects. V.6.4, VI.4), the non-HOD validation ladder
  (arXiv:2309.16539, Sect. 3.2.4; arXiv:2310.16116, Sect. V.2.2), MF against WST on
  the same data (arXiv:2501.01698, Table 5, Sect. 6.1). Marked spectra are not
  covered. **Y.**

**T5 — Field-level inference: forward model, likelihood, sampler; BORG-type against LEFTfield-type; diagnostics.**
- L2 (methods §5): the three meanings, founding papers, the marginal posterior for
  Gaussian noise with joint NUTS (arXiv:2509.09673, Eq. 38, Sect. III.2.3), the
  forward-model families table, BORG outputs and its tempered Poisson likelihood
  (arXiv:1806.11117, Sect. 3.5, Eq. 24). How to choose between the two families and
  which diagnostics establish convergence and correctness: not in the file (`syst`
  §5.4 has effective sample sizes only). **P.**
- L3: the Wiener filter as an exact reference (arXiv:2509.13435, Eqs. 10–11;
  arXiv:2212.07875, Sect. 6), white-noise parametrisation (arXiv:2405.02252, Eq. 17),
  forward models with stated reasons (arXiv:1909.06396, Sect. 2.2; arXiv:1806.11117,
  Table 1; arXiv:2304.09193, Sect. 3.1), the resolution counterterm (arXiv:2509.09673,
  Eqs. 49–50), Poisson (arXiv:1806.11117, Eqs. 19–23) against Fourier-space Gaussian
  EFT likelihood (arXiv:2405.02252, Eqs. 18–19), analytic bias marginalisation
  (arXiv:2403.03220, Eqs. 15–16), block against joint sampling with the block mass
  matrix (arXiv:2212.07875, Sect. 3.2; arXiv:2509.09673, Sect. III.2.2, Eq. 37), HMC
  against MCLMC (arXiv:2307.09504, Sect. 4), survey effects in the model
  (arXiv:1909.06396, Eqs. 8–10); diagnostics: Gelman–Rubin and ESS
  (arXiv:2509.13435, Eqs. 27–35), the window rule (arXiv:2212.07875, App. D),
  true-against-random initialisation (arXiv:2403.03220, App. B.1), values achieved
  (arXiv:2405.02252, Sect. V.3.3; arXiv:2509.09673, App. G, Table 7), the scale-cut
  stability criterion and the post-unmasking bias fix (arXiv:2405.02252, Eqs. 23–25,
  Sect. V.3.4). **Y.**

**T6 — SBI: NPE or NLE, compression, coverage, misspecification; number of simulations.**
- L2 (methods §6): the method and the three standard checks (arXiv:2211.00660,
  arXiv:2310.15250), founding table with MOPED, score compression, DELFI with about
  10⁴ simulations (arXiv:1801.01497), pydelfi with O(10³) (arXiv:1903.00007), IMNN,
  SBC and TARP (arXiv:1804.06788, arXiv:2302.03026), the SimBIG training and test sets.
  How each is chosen and how many simulations a given problem needs: not in the file.
  **P.**
- L3: training-set designs and implicit priors (arXiv:2405.02252, Sects. V.4.2–V.4.3,
  Eq. 26; arXiv:2403.02314, Sects. 2.5, 4.2); compression by MSE (locally MOPED,
  optimal for Gaussian posteriors) against VMIM and VICReg (arXiv:2606.11309,
  Eqs. 9–14, Sects. 3.2–3.4, 6.2.1); NPE against NLE and why DES uses NLE (Eq. 2,
  Sects. 2.2, 6.3; arXiv:2403.02314, Sect. 2.5); SBC, TARP with a fitted test prior
  (arXiv:2606.11309, Sect. 7.1), expected coverage and why divergence metrics cannot
  separate over- from under-confidence (arXiv:2110.06581, Eq. 2, Sect. 2.2);
  misspecification by changed simulators, (μ − θ_fid)/σ, the architecture spread D_v
  and the two-step repair (arXiv:2507.03086, Sects. II.2.4, III.1–III.2, Eqs. 5–6).
  Simulation count: no rule, but ensemble disagreement as the sign of too few
  (arXiv:2403.02314, Sect. 2.4.2), overconfidence at small budgets and ensembles as a
  partial remedy (arXiv:2110.06581, Sect. 3.4, Fig. 3), the budgets used, and the box
  volume against the survey (arXiv:2405.02252, Sect. V.4.4). IMNN is not compared
  beyond L2. **Y.**

**T7 (control, `bispectrum-full-shape`).** L2 (methods §§1.4, 1.6): window per analysis
(only the P_NL factor of the monopole, arXiv:2503.09714, Sect. 3.3; window-free
estimators, arXiv:2112.04515, and nearly identical constraints with and without,
arXiv:2507.13433, Sect. VII.3; matrix in the TripoSH basis, arXiv:2610.01836,
App. A.2; windowed linear spectrum in tree-level B, arXiv:2206.08327, Eq. 18) and
covariance (1000 EZmocks, Hartlap ≈ 0.8, Sellentin–Heavens; Gaussian analytic with
the mask and no P–B cross-covariance, arXiv:2507.13433, Sect. VIII; 2048 Patchy with
bins widened for the Hartlap factor; P–B cross-covariance from mocks and the
BAO × ShapeFit block from 100 mocks, arXiv:2606.23936, Sect. 3.4). **Y.** L3
(`simulation-based-inference`, Step 2 and Numbers): in the NPE route no covariance and
no window model enter; nothing on a perturbative joint fit. **Y**, no gain.

**T8 (control, `lensing-higher-order`).** L2 (syst §§4.1–4.4, 4.6): baryon biases and
mitigation (arXiv:2403.03807; arXiv:2606.12389, Sect. 5.4; one baryon model at one
cosmology in arXiv:2606.11309, Sect. 7.2), IA treatments (four models in KiDS-Legacy,
Sects. 5.2, 5.4; NLA at both orders in DES Y3, arXiv:2508.14018, Sect. II.2; forward
modelled in DES SBI), covariance (1944 KiDS-Legacy mocks capping the vector at 291
entries, Eqs. 28–32; 796 CosmoGridV1 mocks for DES Y3; coverage tests for SBI). **Y.**
L3 (`simulation-based-inference`): no baryon or IA content. **Y**, no gain.

| Q | L2 (a) | L3 (a) | L3 locator | Gain |
|---|---|---|---|---|
| T1 | P | Y | Y | yes |
| T2 | P | Y | Y | yes |
| T3 | P | P | Y | no |
| T4 | P | Y | Y | yes |
| T5 | P | Y | Y | yes |
| T6 | P | Y | Y | yes |
| T7 (c) | Y | Y | Y | — |
| T8 (c) | Y | Y | Y | — |

**Verdict: pass** (5 of 6 with locators; 5 L2 failures answered; one dossier per
question; controls inert). The partial T3 is a scope gap, as in V3 and V6:
`deep/void-lensing-cmb.md` covers shear and CMB lensing of its subtopic "lensing by
voids and void imprints on the CMB" and sends void ISW to
`cosmo-cmb-lss-cross-correlations`; `open-questions.md` "Not verified" lists void ISW
stacking results as not read, so within this skill void ISW is one fragile claim.

Generality flags:
- `deep/void-finding-size-function.md`, Steps 1–8: the whole procedure is one
  group's pipeline (VIDE, Ronconi–Marulli cleaning, extended Vdn, CosmoBolognaLib:
  arXiv:2212.03873, arXiv:2205.11525 and the Beyond-2pt VSF entry, which the dossier
  says share it). The alternatives (arXiv:2501.07817, arXiv:2007.12064,
  arXiv:2605.03779, arXiv:2401.14451) get one paper each under "Choices".
- `deep/emulator-summary-statistics.md`, Steps 1–7: one simulation suite
  (AbacusSummit) and one sample (BOSS CMASS) under every pipeline. This is the state
  of the field as `SKILL.md` and `methods` §3 record it, not a selection by the
  dossier, which shows in "Same data, different statistics" that the shared
  ingredients do not force agreement. The BACCO hybrid emulator is not read.
- No flag on the other four. `deep/field-level-inference.md` works through BORG
  (arXiv:1806.11117, arXiv:1909.06396) and LEFTfield (arXiv:2212.07875,
  arXiv:2403.03220, Beyond-2pt Sect. V.3) side by side, with a third group
  (arXiv:2509.09673) and pmwd (arXiv:2307.09504); the framing review
  (arXiv:2509.13435) is by a BORG author. The dossier covers sampled initial
  conditions only; the Gaussian field likelihood (the meaning edited on 2026-10-20)
  has no dossier. At L2, `methods` §5.1 names its originators (arXiv:1404.3799,
  arXiv:1706.05205, arXiv:2209.04166), but `results` §5.4 (key
  `gaussian-field-level-likelihood-flip`) has two rows, both flip papers
  (arXiv:2501.16852, arXiv:2609.34508), and `syst` §5.7 cites only arXiv:2501.16852.
  `deep/void-galaxy-rsd-ap.md` works through both schools; its void–forest part rests
  on arXiv:2203.11045, the only analysis of that kind. `deep/void-lensing-cmb.md` and
  `deep/simulation-based-inference.md` draw on several groups and surveys (UNIONS,
  DES, DESI Legacy, Roman, Euclid; SimBIG, Beyond-2pt, DES Y3).

Source checks for this skill: E6 and E7 (table at the end). Rows for that table:

| # | File | Statement | What the paper says |
|---|---|---|---|
| E6 | B2pt `deep/void-finding-size-function.md`, "Calibrated (fixed or relaxed)" | fixed calibration (C_slope, C_offset) = (−1.62, 4.30): Ω_m 0.293, σ8 0.839, w −0.97; relaxed: 0.285, 0.793, −1.11 ± 0.24 | arXiv:2212.03873, Sect. IV.2, Table 1: printed so, with the relaxed calibration posterior −2.02, 4.74 as in the dossier's Numbers. The text gives about 21% on Ω_m for both and 10% (relaxed) against 7% (fixed) on σ8, which bears out "relaxing loosens σ8, not Ω_m". Match. |
| E7 | B2pt `deep/field-level-inference.md`, Step 8 | Beyond-2pt stage 2: target "R̂ ∼ 0.01", ≈ 255 samples of α, ESS 193–311, Gelman–Rubin 0.003–0.035, two chains, GetDist | arXiv:2405.02252, Sect. V.3.3, "MCMC convergence and autocorrelation": printed so, with mean and median ESS 254.4 and 259.5. Match. The dossier's [der] that the values are R̂ − 1 agrees with the paper's EFT-entry criterion, written "R−1<0.03" (section "Sampling & validation"). |

## Source checks E1–E5

Recovered on 2026-10-21 from the transcript of the run that was stopped; the
paper text below is what the paper reader returned at the time.

| # | File | Statement | What the paper says |
|---|---|---|---|
| E1 | DE `deep/fr-screening.md`, Numbers and the note after it | eRASS1 `log10 abs(f_R0)` < −4.31 (95%, massless ν) in the abstract and Eq. 50, while Table 2 prints < −5.12 | match: the abstract gives "< −4.31 at 95% confidence level"; Sect. 5.2, Table 2, row "HS-f(R)", prints "< −5.12" (Ω_m 0.28 ± 0.02, σ8 0.89 ± 0.04, S8 0.85 ± 0.04); the dossier reports the inconsistency without picking one (arXiv:2402.08459) |
| E2 | neutrinos–DM `deep/interacting-decaying-dm.md`, Not verified | Mosbech et al. quote the Planck optical depth as τ = 0.054 ± 0.0007 | match: Sect. 5 prints "τ_CMB = 0.054 ± 0.0007" (arXiv:2607.15020) |
| E3 | same | the error of E2 was "not checked against the Planck paper" | Planck 2018 gives τ = 0.0544 ± 0.0073 (arXiv:1807.06209, Sect. 3, base-ΛCDM table): the error printed in arXiv:2607.15020 is ten times smaller; the paper does not comment on it |
| E4 | inflation `deep/slow-roll-model-comparison.md`, "χ² or Bayes factor" | D-brane p = 2: Δχ² = −2.0, ln B = +0.6 | match: Sect. 4.2, Table 5, row "D-brane inflation (p = 2)": −2.0, 0.6 (arXiv:1807.06211); the p = 4 row was cut in the output and not compared |
| E5 | CMB × LSS `deep/ksz-velocity-reconstruction.md`, filter matching | arXiv:2604.04867 writes the filter ratio as b_l^150/b_l^90 | match: Sect. IV.1, Eq. 39, F_l^150 = (b_l^150/b_l^90) F_l^90 (arXiv:2604.04867) |

One more check of the same run, for `cosmo-beyond-two-point`, was made before the stop and is not numbered: the void galaxy bias b_g = 2.45 ± 0.36 quoted in `results.md` and `systematics.md` matches the abstract and conclusions of arXiv:2507.13450.
