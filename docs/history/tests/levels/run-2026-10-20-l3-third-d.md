# Level test — third L3 test of 2026-10-20, part 3d

Item C of `docs/plans/2026-10-20-plan.md` ("the domains not yet tested"), part 3d. Four
skills: `cosmo-machine-learning`, `cosmo-multimessenger`, `cosmo-photometry-photoz`,
`cosmo-reionization-21cm`. Thirty-two questions, eight per skill, are in
`docs/tests/levels/l3-questions-3d.md`. Each was answered twice from the skill files only:
an **L2 run** (the skill's `SKILL.md` plus one reference file chosen from the file map, no
`deep/`) and an **L3 run** (the same plus at most one dossier of `deep/`, chosen from the
file map). Model memory was not used to fill gaps. This run tests; no skill file was
changed. Part 3c runs at the same time on other skills and writes its own files.

Status: complete; four skills.

## Procedure

1. **Questions first.** Written from the four `subtopics.tsv` files, the file names of
   `deep/` and `references/`, and the one-line skill descriptions of the skill listing,
   before any `SKILL.md` body, reference file or dossier of the four skills was opened
   (preamble of `l3-questions-3d.md`). Per skill, six questions fall one each on the six
   dossier subtopics and two on subtopics whose `files` column lists no dossier
   (controls). The questions file was written by an earlier agent, cut by a usage limit
   before it opened any skill body; this run resumed from it without changing it.
2. **Preliminaries read.** Part 3a (`l3-questions-3a.md`, `run-2026-10-20-l3-third-a.md`)
   as the template for method and format. Layer check: no `.cosmoskill/` in the working
   directory, its parents or the home directory; `COSMOSKILL_HOME` unset; layer `base`
   for every question.
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
6. **Source checks.** One or two per skill, numbered D1, D2, … within this part, read at
   source with `skills/observational-cosmology/scripts/fetch_paper.py` (`--grep` or
   `--section`), of a statement an L3 answer used; the place read and match or mismatch
   are given. Paper text was treated as data.
7. **Generality.** Per skill, a dossier or answer that rests mostly on one group, code
   or data set where the field has several is flagged, with citation counts where they
   help.

Abbreviations for reference files: `methods` = `references/physics-and-methods.md`,
`syst` = `references/systematics.md`, `open` = `references/open-questions.md`,
`results` = `references/results.md`, `surveys` = `references/surveys-and-data.md`.
Every run also loaded the skill's `SKILL.md`.

## cosmo-machine-learning

The `files` column of `subtopics.tsv` names a dossier for three rows only; the file map of
`SKILL.md` names all six (emulator design; generative field models; networks correcting fast
solvers; classifier training; network uncertainties; saliency and symbolic regression), so
M1, M3 and M5 load their dossier through the file map. No file-map row names a dossier for
neural density estimation or anomaly detection.

### Files loaded

| Q | L2 reference file | L3 dossier |
|---|---|---|
| M1 | methods | `deep/emulators.md` |
| M2 | syst | `deep/classification.md` |
| M3 | methods | `deep/generative-models.md` |
| M4 | methods | `deep/interpretability.md` |
| M5 | methods | `deep/learned-simulation-corrections.md` |
| M6 | syst | `deep/uncertainty-reproducibility.md` |
| M7 (control) | methods | none: no file-map row for NPE, NLE, NRE |
| M8 (control) | methods | none: no file-map row for anomaly detection |

### Answers

**M1 — Emulator construction and validation; design, architecture, accuracy target; error
in the likelihood.**
- L2 (methods §1): regression families with training sets (Coyote 37 models,
  arXiv:0902.0429; GP for Goku, arXiv:2507.07184; CosmoPower P_L × P_NL-corr split,
  arXiv:2106.03846, Sect. 3.2; CONNECT iterative rounds, arXiv:2205.15726), architectures
  (DarkEmulator2 CMA-ES, Sect. 3.2; GokuNEmu per-z PCA, Sect. II.1), four validation metrics
  (test-set percentiles, Δχ² 0.069, posterior shift, leave-one-out), error propagation named
  (arXiv:2205.11587). How the designs compare (Latin hypercube against hypersphere or
  posterior-concentrated), why PCA or whitening, how the accuracy target is set in survey
  units, and the form in which the emulator error enters the likelihood are absent. **P.**
- L3: what the network replaces, matter spectrum against observable against EFT pieces
  (arXiv:2106.03846, Sect. 5.2; arXiv:2501.04639, Sect. 2.2; arXiv:2507.20990, Sect. 2.1);
  five designs with reasons, including the CONNECT T = 5 loop and the hypersphere volume ratio
  (arXiv:2205.15726, Sects. 3–3.2, Eq. 4), copula inflation α = 1.2 (arXiv:2507.20990,
  Eqs. 2.4–2.7); hypersphere against hypercube, median Δχ² two orders lower, exponents 0.798
  and 0.771 (arXiv:2603.16003, Sect. IV.2, Eq. 11); log, PCA (512 TE, 64 φφ components;
  arXiv:2106.03846, App. A.2) and whitening (arXiv:2603.16003, Eqs. 4–5); network and loss
  table (Step 4); NN against GP trade-off (arXiv:2106.03846, Sect. 5.2; arXiv:2607.17942,
  Sect. 5.1); targets in survey units, 0.1σ CMB with SO noise (arXiv:2106.03846, Eqs. 11–13),
  Stage-IV σ (arXiv:2507.20990, Sect. 2.2), median Δχ² < 1 (arXiv:2603.16003, Sect. IV.2);
  in-inference tests (Step 6); propagation P ∝ exp(−½[ξ − Δ̄]ᵀΨ[ξ − Δ̄]), Ψ = (C + Σ)⁻¹ and
  its preconditions (arXiv:2205.11587, Eqs. 7–8, Sects. 2.1–3), GP variance on the diagonal
  (arXiv:2607.17942, App. A), and the statement that no survey adopted the propagation.
  DarkEmulator and the Euclid and Aemulus emulators are named only through siblings (Euclid,
  Mira-Titan, BACCO under "Not verified"). **Y.**

**M2 — Transient classifiers: trees against sequence or image networks; non-representative
training set; contamination in the cosmological fit.**
- L2 (syst §5): PLAsTiCC built on a small pristine training set (arXiv:2012.12392,
  Sect. 3.2); SCONE 99.73% in distribution against 80.61% on the photometric sample, 83% and
  87% on low-z subsets (arXiv:2106.04370, Sect. III.1.2, Table 5); Superphot+ on Rubin DP1
  (arXiv:2507.22864, Sect. IV.2); ELAsTiCC w bias 0.01–0.03 that vanishes with a perfect
  classifier (arXiv:2512.06319, Sects. IV.1, IV.4, Table 7); mitigations listed (augmentation,
  Bayesian networks, unseen class). No comparison of trees with RNN or CNN on one data set,
  and no reweighting recipe; BEAMS is sent to `cosmo-supernovae`. **P.**
- L3: four input representations with preprocessing (Avocado GP + LightGBM, arXiv:1907.04690,
  Sect. III.6; SuperNNova, arXiv:1901.06384, Sect. 2.4; SCONE heatmaps, arXiv:2106.04370,
  Sects. II.4, II.6; ParSNIP latents, arXiv:2602.13036, Sect. 4.2); same-data comparison RNN
  96.3% against random forest 95.15% and 1D CNN 94.53% (arXiv:1901.06384, Sect. 3.3, Fig. 3);
  the Avocado eight-step augmentation (arXiv:1907.04690, Sect. III.4) and the ZTF
  noisification with z^z_scale draws (arXiv:2602.13036, Sects. 2.2.1, 3.3); class weights and
  the redshift-weighted metric (arXiv:1907.04690, Sect. II.2.2, Eq. 3; arXiv:2012.12392,
  Eq. 1) and their cost (Sect. IV.2, Figs. 7–8); leakage-free splits (Step 4); calibration
  (Step 7). The cosmological propagation rests on the L2 statement (ELAsTiCC w bias) and the
  pointer to `cosmo-supernovae`. **Y.**

**M3 — Generative models: validation beyond P(k); failure modes.**
- L2 (methods §4): families table; validation by one-point PDF, peaks, P(k), bispectrum and
  P(k) covariance against an ensemble (arXiv:2605.23114); the variance-field failure of
  generative IC posteriors, up to ~30% (arXiv:2606.10023, Sects. 3.2, 5.1–5.2). Minkowski
  functionals, cross-correlation tests, mode collapse, held-out cosmologies and checkpoint
  selection are absent. **P.**
- L3: role sets the validation (Step 1); statistics list incl. Minkowski functionals,
  scattering coefficients, kNN, MS-SSIM (arXiv:2605.23114, Eq. 28, Sect. 4; arXiv:2311.17141,
  Sect. III; arXiv:2502.04158, Eqs. 25–26); Wasserstein-1 per bin on 46 training and 11
  held-out cosmologies (arXiv:2605.23114, Sect. 5.3, App. B.2); CV covariance test χ² 33.4
  against 36.6 (arXiv:2405.05255, Eqs. 8–9, Sect. III); checkpoint selection on statistics
  (arXiv:2211.12444, Sect. 3); mode collapse in the GAN (arXiv:1801.09070, Sect. 7), GAN
  against flow matching on the same split (arXiv:2605.23114, App. B.1); missing large scales
  (BAO in point clouds, box-scale limit of patches; arXiv:2311.17141, Sect. IV;
  arXiv:2601.14377, Sect. 3.2.3); cross-correlation that "can remain high even when the
  posterior variance is incorrect" (arXiv:2606.10023, Sects. 2.2, 5.2); worst case at grid
  edges. Memorisation of training samples is not tested by any paper read; the nearest is the
  GAN replicating noise patterns (arXiv:2008.03833, Sect. 2.2). **Y.**

**M4 — What a network has learned; validating a symbolic expression.**
- L2 (methods §8): attribution findings (κ < 0 carries 69–86%, arXiv:2007.06529, Sect. IV.2;
  SHAP with mask control, arXiv:2604.05290; neural marks), symbolic-regression tools and
  results (GNN distillation generalising out of distribution, arXiv:2006.11287, Sect. 4.3;
  PySR; ESR on H(z); symbolic P_L(k)). How saliency methods are checked, how a formula is
  selected, and the cross-simulator test of a formula are absent. **P.**
- L3: saliency families and the model-randomisation test with Pearson, Spearman, Kendall
  (arXiv:2007.06529, Sect. IV.1, Table 2: deep Taylor r = 0.882 dropped); squared saliency
  binned in κ (Sect. IV.2); Partition SHAP with mask, null-class and channel controls and PCA
  fitted on training only (arXiv:2604.05290, Eq. 12, Sects. 3.4–4.2); SR set-up: residual
  target (arXiv:2311.15865, Eq. 5), operator tables, PySR, Operon, ESR and distillation
  (arXiv:2305.01582, Eq. 2; arXiv:2211.11461, Sect. II-E); selection by MDL
  (arXiv:2211.11461, Eq. 6), loss-per-complexity score, survey accuracy target
  (arXiv:2606.07745, Sects. 4.3–4.5); out-of-sample test with δ > 1 halos masked (0.142
  against 0.0892, arXiv:2006.11287); across simulators only with refitted coefficients
  (arXiv:2602.07651, Sect. III.1, Table 3); domain of validity tied to CLASS + HMcode
  (arXiv:2606.07745, Sect. 5.2). **Y.**

**M5 — Learned corrections of fast simulations; inputs and targets; validation; dependence
on cosmology and hydrodynamical model.**
- L2 (methods §5): approaches table with input → output and accuracy (D³M, styled U-Net,
  NECOLA, MG-NECOLA, hybrid ODE, LDL, LNCA, SR GAN, Tröster painting, BIND); the styled U-Net
  split and its BAO mis-shaping at one cosmology (arXiv:2206.04594); the residual pattern;
  "every row above was validated on summaries of the same simulation family". Losses,
  crop-and-pad, the order of the tests, the out-of-cosmology tests and the hydro-model
  dependence are absent. **P.**
- L3: input → target table with the residual learned (Step 1, arXiv:2111.02441,
  Sect. II.2.1; arXiv:2604.19613, Eqs. 5–6); training pairs and splits (Step 2); losses
  (arXiv:2111.02441, Sect. II.2.2; arXiv:2604.19613, Eqs. 7–9; arXiv:2010.02926, Eqs. 8–9);
  validation in six steps: particle residuals, T(k) and r(k) (P(k) matched while r(k) is
  not, arXiv:2207.05509, Sect. 5), haloes +10–20% (arXiv:2206.04594, Halos), out-of-cosmology
  tests of NECOLA on 100 Latin-hypercube, M_ν and w runs (arXiv:2111.02441, Sect. III.2),
  MG-NECOLA against fRemu (Sects. IV.5.1–IV.5.2), the BIND hydro-replace ceiling ~65%
  (arXiv:2609.10709, Sect. VII.1); hydrodynamical-model dependence: BIND is IllustrisTNG only
  and needs retraining or a cross-code test (Sect. VIII), which answers that it has not been
  tested; the measured transfer costs are in L2 `syst` §1 (not loaded here). **Y.**

**M6 — Uncertainty of a network inference; coverage; reproducibility practice.**
- L2 (syst §§4, 6): overconfidence of all benchmarked SBI algorithms and ensembles of five
  (arXiv:2110.06581, Sects. 3.3–3.4); deep ensembles named (arXiv:1612.01474); balanced NRE;
  conformal prediction for classifiers (arXiv:2607.08044); coverage tests run (KiDS-SBI TARP,
  DES Y3 HPD and TARP, the DES Y3 hybrid TARP bug; arXiv:2404.15402, Sect. 7.1;
  arXiv:2511.04681, Sect. VI.2; arXiv:2606.11309, Sects. 7.1, 7.5); release practice, LtU-ILI,
  k-fold tuning, blinding protocols of KiDS-1000, KiDS-SBI and DES Y3 (§6). MC dropout and
  Bayesian layers, how a regression or class uncertainty is calibrated, and seed variance
  are absent. **P.**
- L3: aleatoric against epistemic (arXiv:1911.08508, Sect. III); Gaussian NLL output and the
  failure of MSE-ensemble spreads, 80% → 20% (arXiv:1612.01474, Eq. 1, App. A.2); MC dropout,
  Bayes by backprop, Flipout, deep ensembles with settings (Step 3 table; arXiv:1901.06384,
  Sects. 4.2–4.3; arXiv:1708.08843, Sects. II.1–II.3); coverage by noise level
  (arXiv:1708.08843, Sect. III.1) and reliability with ECE (arXiv:1706.04599, Eq. 3);
  recalibration in training, by temperature scaling, or conformally (arXiv:1911.08508,
  Table 5; arXiv:1706.04599, Eq. 9; arXiv:2607.08044, Eqs. 1–3, 6); seed, architecture and
  split variance table and ensemble pruning (arXiv:2610.19891, Sect. 5.2). SBC and TARP sit
  in L2 and in siblings; the dossier records that no cosmology analysis reports the
  seed-to-seed scatter of a published constraint. **Y.**

**M7 (control, neural density estimation).** L2 (methods §3): NPE, NLE, NRE with sequential
variants and their foundations (arXiv:1605.06376; arXiv:1905.07488; arXiv:1805.07226;
arXiv:1903.04057); choice: no uniformly best algorithm, C2ST scoring (arXiv:2101.04653,
Sects. 2.2, 3), Thiele's defaults (arXiv:2605.10719, Sect. 2.7); simulation counts (KiDS-SBI
5000 converged, 18 000 used, Sect. 5.4; multi-fidelity N ~ 100–120, arXiv:2606.23346,
Sect. 4.2.1); prior: NPE carries it and must not be multiplied, VMIM posterior discarded for
its Sobol prior (arXiv:2511.04681, Sect. IV.1.1); compression before the estimator (§2).
**Y.** L3: no dossier row. **Y**, no gain.

**M8 (control, anomaly detection).** L2 (methods §7): four designs with scores (unsupervised
forest, isolation forest on a VRAE latent, autoencoder + flow, predictive model;
arXiv:1611.07526; arXiv:2103.12102; arXiv:2307.07664; arXiv:2111.00036), active learning
(arXiv:1909.13260; arXiv:2010.11202), Fink's ten candidates per night and its yield
(arXiv:2603.29511), comparison of three active frameworks (arXiv:2609.36096). The false
positives are controlled by a fixed follow-up budget and by purity counts; no calibration of
the score is described. **P.** L3: no file-map row. The nearest material sits in other
dossiers: `classification` Step 6 (TPR0, TPR10 and the contamination formula of the lens
challenge, arXiv:1802.03609, Eq. 14) and `uncertainty-reproducibility` Step 5
(anomaly-stratified conformal coverage); neither would be loaded from the file map. **—**,
no gain.

### Grades

| Q | L2 (a) | L3 (a) | L3 locator | Gain |
|---|---|---|---|---|
| M1 | P | Y | Y | yes |
| M2 | P | Y | Y | yes |
| M3 | P | Y | Y | yes |
| M4 | P | Y | Y | yes |
| M5 | P | Y | Y | yes |
| M6 | P | Y | Y | yes |
| M7 (c) | Y | — (no dossier) | Y | — |
| M8 (c) | P | — (no dossier) | Y | — |

**Verdict: pass.** L3 answers 6 of 6 with locators; 6 L2 failures answered; one dossier per
question; controls inert. Each dossier opens with an "Already in L2" list and none repeats
the L2 tables. M8 is weak at L2 (no score calibration) and no dossier serves it; the file map
offers no anomaly-detection row.

### Source checks (2 used)

- **D1** `deep/emulators.md`, Step 7, used in M1: Gaussian propagation with Ψ = (C + Σ)⁻¹,
  10 000 CAMB spectra split 70/20/10 and a fresh set of 10 000 for Δ̄ and Σ, errors up to 5%
  and 40% for the two nets. arXiv:2205.11587, Sect. 2.2, Eqs. 7–8, and Sect. 3: "70% for
  training, 20% for the validation set and 10% for test", "a fourth set V including new 10000
  power spectra", "up to 5% ... for the accurate neural net, and 40% for the inaccurate model".
  Match.
- **D2** `deep/classification.md`, "Flat-weighted or redshift-weighted objective", used in M2:
  "only 0.6% of training SNe Ia lie at z < 0.1". arXiv:1907.04690, Sect. IV.2: "Only 0.6% of
  the SNe Ia in the sample are at a redshift less than 0.1", in a paragraph that points to
  Figure 2, whose caption (Sect. II.1) reads "for the PLAsTiCC test dataset". The 0.6%, the
  80% peak at z = 0.8, the ~70% SN Ia fraction there and the < 40% nearby match; the word
  "training" does not: the paper says "the sample" and its figure is the test set. Mismatch
  of the referent; the dossier should say "in the sample (Fig. 2, the test set)".

### Generality flags

- `references/systematics.md` §1 ("Simulator dependence") and the M5 L3 answer: every
  cross-simulator test is a CAMELS or Quijote suite pair (IllustrisTNG, SIMBA, Astrid,
  Magneticum, SWIFT-EAGLE), and the baryon-painting rows of `deep/learned-simulation-corrections.md`
  (BIND, LDL) are trained on IllustrisTNG only; the dossier says so ("One sub-grid model").
  Acceptable as stated; the hydro-model dependence asked in M5 is answered by "not tested".
- `deep/interpretability.md`, symbolic-regression half: 22 of 67 citations are to
  arXiv:2311.15865 and arXiv:2211.11461 (Bartlett et al.), with PySR (arXiv:2305.01582) and
  CMBolic as the others; the selection rules (MDL, score, accuracy target) are set side by
  side, so the method choice is not one group's. Mild.
- Other dossiers spread their citations: the top source carries 16 of 77 (classification), 22
  of 95 (emulators), 20 of 134 (generative), 17 of 108 (learned corrections), 16 of 82
  (uncertainty). No flag.

## cosmo-multimessenger

The `files` column and the file map agree: six dossier rows, and no dossier for
`galaxy-catalogue-dark-sirens` or `modified-gw-propagation`.

### Files loaded

| Q | L2 reference file | L3 dossier |
|---|---|---|
| A1 | methods | `deep/spectral-sirens.md` |
| A2 | methods | `deep/gw-lss-cross-correlation.md` |
| A3 | open | `deep/next-generation-siren-forecasts.md` |
| A4 | syst | `deep/gw-lensing.md` |
| A5 | methods | `deep/frb-baryon-distribution.md` |
| A6 | methods | `deep/frb-hubble-constant.md` |
| A7 (control) | syst | none: no file-map row for the catalogue method |
| A8 (control) | methods | none: no file-map row for modified propagation |

### Answers

**A1 — Spectral sirens: features, population models, selection; tests of mis-specification
and evolution.**
- L2 (methods §§4, 5): principle m_det = (1 + z) m_src and its history (arXiv:1108.5161;
  arXiv:1908.09084; arXiv:2202.08240, five features); features in data (peaks near 10 and
  35 M☉, roll-off above 46, 63.3 M☉; arXiv:2605.27226; arXiv:2410.07416; arXiv:2601.03257);
  the three LVK models in words with parameter counts (arXiv:2605.27227, Sect. II.3),
  non-parametric and flow alternatives; the FullPop gain of 51–56% (arXiv:2509.04348,
  Sect. IV.1); the hierarchical likelihood with ξ(Λ) from injections and the two codes
  (arXiv:2605.27227, Eq. 1; arXiv:2509.04348, App. A). How mis-specification and evolution
  are tested is only pointed to ("systematics file, §5"). **P.**
- L3: model equations PLP, MLTP, FullPop-4.0 with the notch and pairing function
  (arXiv:2509.04348, App. C, Eqs. C5–C20); GWTC-5.0 priors and the narrower GWTC-4.0 widths
  (arXiv:2605.27227, Tables 5–8; arXiv:2509.04348, Tables 3–5); Madau–Dickinson rate and why
  (arXiv:2605.27227, Eq. A.2) against a delay-time convolution (arXiv:2604.26273, Eqs. 1–3);
  linear and sigmoid evolution with priors and 45 hyperparameters (arXiv:2605.20112,
  Sects. II.1–II.2, Eqs. 3–5); Gaussian-process and spline alternatives (arXiv:2404.02210,
  Sect. II.3; arXiv:2604.14290, Sect. IV); blinded MDC protocol and outcomes, 1.5σ-type
  failure and ~60% bias for 40–50% evolution (arXiv:2412.14244, Sects. II, V.2;
  arXiv:2604.26273, Sect. V.1); the evolving-model shift −0.30σ removed by fixing the
  high-mass peak, and its reversal at O5 sensitivity (arXiv:2605.20112, Table 1,
  Sects. III.3–III.4); parametric bias of unknown sign (arXiv:2404.02210, App. D);
  diagnostics (`p(m1)` in three z bins; compression when cosmology is freed). **Y.**

**A2 — Siren × galaxy cross-correlation: construction, what it needs against the catalogue
method, measurements.**
- L2 (methods §6): principle (correlation maximal on the true d_L(z)), b_GW as nuisance
  (arXiv:2007.02943), lensing magnification (arXiv:1603.02356), insensitivity to
  incompleteness (arXiv:2007.04271), Peak Sirens and the first detection (arXiv:2512.15380),
  first GWTC-3 application (arXiv:2203.03643), forecast requirement (arXiv:2510.19931). No
  estimator, no treatment of the localisation as a window, no covariance, and the
  comparison with the catalogue method is one line. **P.**
- L3: event and catalogue selection in two analyses (arXiv:2203.03643, Sect. III;
  arXiv:2512.15380, Sect. III); maps, completeness weight (Eq. 4); pseudo-C_ℓ estimator
  (Eqs. 1–2; arXiv:2203.03643, Eqs. 2–3); localisation as a beam, k_eff and
  B_ℓ = exp[−ℓ(ℓ+1)σ²/2] with the double-smoothing caveat (arXiv:2007.02943, Sect. III;
  arXiv:2603.13053, Eq. 68, Sect. V.1); three signal models (Limber with lensing term,
  arXiv:1603.02356, Eqs. 6–20; measured-auto ratio, arXiv:2203.03643, Eq. 8; rescaled
  GLASS template, arXiv:2412.00202, Eqs. 15–17); bias treatment (b_g σ8 = 0.85 ± 0.13,
  b_gw free); four covariance choices (Step 7 table); detection test by Fréchet-fitted null,
  3.4σ and 5.9σ, then H0 = 67 (+18/−15) (arXiv:2512.15380, Sect. IV); what it needs that the
  catalogue method does not (3D clustering, b_gw, no host in the catalogue, no luminosity
  weighting) and the reverse (arXiv:2603.13053, abstract; arXiv:2412.00202, Sect. 4.2);
  forecasts with the disagreement between the method papers. **Y.**

**A3 — Next-generation siren forecasts: construction; assumptions that move H0 or w0wa.**
- L2 (open §4): a table of 23 forecast claims each with its assumptions (counterparts,
  catalogue completeness, mass model, A# with spectroscopy, ET bright sirens saturating
  above z ≈ 1, LISA EMRIs and massive binaries), and the track record (counterparts that
  never came, rates). How a forecast is built (population and rate, Fisher errors, per-event
  budget, counterpart model) is absent. **P.**
- L3: network and duty cycle table (Step 1); rate normalisation as the largest lever and the
  choices of five groups (arXiv:2412.00202, Sect. 3.1; arXiv:2402.03120, App. B.2;
  arXiv:2609.12053, Sect. III; arXiv:2607.20413, Eqs. 6–7), the BNS-rate warning
  (arXiv:2503.12263, footnote 21); Fisher codes and thresholds, three treatments of the
  face-on degeneracy and the failure of 2/SNR (arXiv:2303.15923, Sect. 6.4.1;
  arXiv:2503.12263, Sect. 2.3.1); per-event budget with σ_lens and σ_v (arXiv:1601.07112,
  Eqs. 12, 16–17) and the 0.05 z alternative; counterpart models with time budgets
  (arXiv:2303.15923, Table 10; arXiv:2402.03120, Sect. 4.2); inference by Fisher or scattered
  mocks; what moves the answer: ET geometry and LF instrument (×7), kilonova against GRB,
  bright against golden dark, external priors ("clearly dominated by the Planck prior"),
  LISA source classes (arXiv:2204.05434, Sect. 2.3.2). w0wa is reached only through LISA
  and the Fisher set-up; no w0wa precision is given per assumption. **Y.**

**A4 — Weak lensing of siren distances in the likelihood; strongly lensed GW identification
and cosmography; false alarms.**
- L2 (syst §3): weak lensing adds a few per cent of variance per GWTC-3 siren, does not bias
  the mean, strong-lensing probability below 1%, both ignored (arXiv:2111.03604,
  Sect. V.3). No lensing PDF, no delensing, nothing on identification or cosmography;
  `open` "Not verified" lists lensed GWs as not read. **N.**
- L3: regimes (w = 8πGM_L f, geometric against wave optics; arXiv:2204.05434, Eqs. 13–15);
  σ_WL in the per-siren variance with its fitting form and coefficients (arXiv:2402.19476,
  Eqs. 4–11, Sect. IV.3), magnification PDF with detection selection (Eqs. 9–10); de-lensing
  gains and the cost argument (arXiv:0907.3635; arXiv:1007.2468; arXiv:2211.15160);
  identification by the LVK tiered workflow: Posterior Overlap and Phazap at FPP < 1%,
  Fast-GOLUM priors on magnification, delay and Morse phase, Hanabi Bayes factor with
  population and selection, 3486 → 105 → 50 pairs, 254 unlensed injections
  (arXiv:2512.16347, Sects. III.1–IV.1, Eq. 1); cosmography: bright lensed siren D_Δt
  (arXiv:1703.04151) and dark lensed siren host search with its H0 prior
  (arXiv:2004.13811, App. A.5); false alarms growing as N² (arXiv:2201.04619), waveform
  systematics mimicking lensing (GW231123, log10 B from 3.8 to 0.1), the
  similarity-transformation degeneracy (arXiv:2608.28765). **Y.**

**A5 — FRB DM as a baryon locator: foreground mapping, DM–galaxy cross-correlation,
scatter as a feedback probe; host and Milky Way; degeneracies with cosmology.**
- L2 (methods §7): budget and Macquart relation (arXiv:2005.13161, Eq. 2), Ω_b H0 f_d
  degeneracy (§7.2), the Connor et al. partition likelihood with θ = {f_IGM, f_X, μ_host,
  σ_host} (arXiv:2409.16952), host log-normal, Milky Way halo 50–80 (arXiv:1901.11051),
  foreground mapping and DM–galaxy stacking named (arXiv:2402.00505; arXiv:2506.04186;
  arXiv:2601.21336; arXiv:2608.11296), kSZ combination named. How the foreground and
  two-point routes are built and the F–feedback link (in `syst` §7.7) are absent. **P.**
- L3: definitions of IGM and halo gas per analysis (Step 1 table); one-point route with
  the bivariate TNG300 log-normal, the DM cliff and the 30% error inflation
  (arXiv:2409.16952, Methods); FLIMFLAM in six steps: NE2001 + 40 ± 15 halo, ARGO density
  reconstruction (Eq. 7), mNFW haloes (Eq. 11), Gaussian likelihood with quadrature
  variances (Eqs. 15–17), priors (Table 4) (arXiv:2402.00505, Sects. IV–V); three two-point
  implementations with statistic, foreground cut, covariance and model (Step 2c table;
  arXiv:2506.04186; arXiv:2601.21336, Eqs. 4–6; arXiv:2608.11296, Eqs. 1, 4, 12–13); gas
  physics from TNG profiles, FLAMINGO amplitude, BCEmu, and the τ̂_FRB link to kSZ
  (Step 3); the f_igm–f_gas degeneracy set by the f_d prior (arXiv:2402.00505, Sect. VI);
  selection biases (arXiv:2506.03258; arXiv:2511.16850). The cosmology degeneracy rests
  on the L2 statement Ω_b H0 f_d. **Y.**

**A6 — FRB H0: localised against forward-model routes; host DM, scatter, Ω_b h², selection;
why the values differ.**
- L2 (methods §7.3): likelihood table (Macquart 2020; James 2022 with Ω_b h² fixed and
  ⟨DM_cosmic⟩ ∝ 1/H0, Eq. 10; Connor 2024), the two likelihood styles and why the forward
  model gives larger errors, unlocalised bursts weak (arXiv:2604.03769), F degenerate with
  H0 (arXiv:2305.07022), Konietzka on simulated p(DM|z), host log-normal. Why published
  values differ (62 to 85) is not in this file (it is in `syst` §7.7 and `results`). **P.**
- L3: zDM forward model in seven steps with equations (arXiv:2208.00819, Eqs. 1–16;
  arXiv:2609.04765, Eqs. 23–29), where H0 comes from (lower edge, rotation, redshift reach
  degenerate with E_max; arXiv:2208.00819, Sect. 3), completeness corrections and
  host-completeness cuts; localised likelihood with priors (arXiv:2610.15536, Eqs. 4–10,
  Table 1); unlocalised DM distribution with CHIME selection functions (arXiv:2604.03769,
  Eqs. 7–15); BAO in place of BBN (Table 2); why values differ: the F prior alone moves H0
  from 63.29 to 45.74 (arXiv:2510.09463, Sect. III.1, Eqs. 18, 21), host shape preferred at
  ln B up to 74 (Table 5), extragalactic DM model moves H0 by 2.6 and halves its error
  (arXiv:2610.15536, Table 3); per-survey drivers (FRB 20190102, Sect. 5.1). **Y.**

**A7 (control, galaxy-catalogue dark sirens).** L2 (syst §6): GLADE+ complete to 47 Mpc
(arXiv:2110.06184); homogeneous against multiplicative completion and their direction
(arXiv:2310.08991, Sect. 4), line-of-sight gain (arXiv:2608.24992); weighting regimes in
N_GAL and band choice (arXiv:2405.14818, Sects. III–V; arXiv:2608.26307); photo-z against
spectroscopic (arXiv:2302.12037; arXiv:2312.05302); catalogue gain over spectral-only 2–8%
by pipeline, f_cov 5% and 7% (arXiv:2605.27227, Table 1, Sect. IV.1); DES redshift cuts
moving H0 by 14 (arXiv:2602.04766); LVK list of unmodelled choices (Sect. V.2); the
`icarogw`/`gwcosmo` completeness difference is in `methods` §3.1 (not loaded), but the
pipeline dependence is in the syst table. **Y.** L3: no dossier row. **Y**, no gain.

**A8 (control, modified GW propagation).** L2 (methods §1.4, §5): d_L^GW/d_L^EM = Ξ0 +
(1 − Ξ0)/(1 + z)^n and its status as an assumption (arXiv:2605.27227, Eq. 11,
Sect. II.4.2; arXiv:1805.08731), the running-Planck-mass c_M alternative (Sect. IV.2), the
degeneracy with the rate slope γ, with H0 and the population (arXiv:2112.05728), the priors
of the modified-gravity runs and why H0 is narrowed (§5), the GW-speed bound as a separate
test (arXiv:1710.05834). Which data constrain it is given as the LVK dark + spectral
sample; the bright-siren contribution is not separated. **Y.** L3: no dossier row. **Y**, no
gain.

### Grades

| Q | L2 (a) | L3 (a) | L3 locator | Gain |
|---|---|---|---|---|
| A1 | P | Y | Y | yes |
| A2 | P | Y | Y | yes |
| A3 | P | Y | Y | yes |
| A4 | N | Y | Y | yes |
| A5 | P | Y | Y | yes |
| A6 | P | Y | Y | yes |
| A7 (c) | Y | — (no dossier) | Y | — |
| A8 (c) | Y | — (no dossier) | Y | — |

**Verdict: pass.** L3 answers 6 of 6 with locators; 6 L2 failures answered; one dossier per
question; controls inert. GW lensing is absent from L2 apart from one sentence (A4, N).

### Source checks (2 used)

- **D3** `deep/gw-lensing.md`, Step 2, used in A4 (and `deep/next-generation-siren-forecasts.md`,
  Step 4): Mpetha et al. state that the factor 1/2 is missing in Tamanini et al. 2016 because
  the original expression is for σ(ln d_L²) = 2σ(d_L)/d_L; Pop III coefficients C = 0.061,
  β = 0.264, α = 1.89. arXiv:2402.19476, Sect. IV.3, Eq. 11: "Note the factor of 1/2, which is
  missing in Ref. [55]. This is because the original expression is for the uncertainty in
  σ(ln d_L²) = 2σ(d_L)/d_L"; Ref. [55] is Tamanini et al. 2016 (JCAP 2016, 002); coefficients
  as quoted. Match. The claim of an error in Tamanini et al. is the 2024 paper's own
  statement, as the dossier says.
- **D4** `deep/frb-hubble-constant.md`, "Prior on F", used in A6: loose prior H0 = 45.74
  (+2.74/−3.81), narrow Macquart priors H0 = 63.29 (+2.81/−3.77), with Ω_b h² = 0.02237 and
  f_IGM = 0.83 fixed. arXiv:2510.09463, Sect. III.1, Eqs. 18 and 21: both values as quoted;
  "we adopt Ω_b h² = 0.02237 from the Planck 2018 result [4] and f_IGM = 0.83". Match.

### Generality flags

- `deep/frb-hubble-constant.md`, Route A (forward model) rests on one group's code: 28 of 55
  citations are to arXiv:2208.00819 and arXiv:2609.04765 (James et al., ASKAP/CRAFT `zDM`),
  and no other survey forward model is described or said not to exist. Routes B–D come from
  three other groups, so the choice between routes is not one group's; the forward-model
  route is.
- `deep/gw-lss-cross-correlation.md`: arXiv:2512.15380 (de Matos et al.) carries 33 of 93
  citations, and with arXiv:2412.00202 (Ferri et al.) 50 of 93 for the template route, its
  covariance and the detection test; the Mukherjee et al. papers and Cheng & Gair supply the
  alternatives and the critique. The subfield has one detection; mild.
- `deep/spectral-sirens.md`: LVK papers and four external groups (Agapito, Gennari, Farah,
  MDC teams) spread the citations (top source 12 of 68). No flag.

## cosmo-photometry-photoz

As in `cosmo-machine-learning`, the `files` column names a dossier for three rows only;
the file map of `SKILL.md` names all six, so Z1, Z4 and Z6 load their dossier through
the file map. No file-map row names a dossier for template fitting or SOM n(z); the
row "Narrow-band photo-z: line templates, zero points, PDF fixes" overlaps the template
control Z7, which was therefore run with that dossier to see whether a control gains.

### Files loaded

| Q | L2 reference file | L3 dossier |
|---|---|---|
| Z1 | methods | `deep/photometric-calibration.md` |
| Z2 | methods | `deep/chromatic-extinction.md` |
| Z3 | methods | `deep/machine-learning-photoz.md` |
| Z4 | methods | `deep/population-forward-models.md` |
| Z5 | methods | `deep/clustering-redshifts-shear-ratio.md` |
| Z6 | surveys | `deep/narrow-many-band-photometry.md` |
| Z7 (control) | methods | `deep/narrow-many-band-photometry.md` (file-map row "line templates, zero points, PDF fixes") |
| Z8 (control) | results | none: no file-map row for SOM calibration |

### Answers

**Z1 — Survey-wide calibration: ubercal against FGCM, absolute tie; residual
non-uniformity and its effect on photo-z and clustering.**
- L2 (methods §2): ubercal separating relative from absolute calibration, SDSS ~1% and
  PS1 < 10 mmag (arXiv:astro-ph/0703454; arXiv:1201.2208), sky-flat errors
  (arXiv:1111.2058), FGCM with standard passbands and chromatic corrections, DES Y3 7 mmag
  and Y6 < 1.8 mmag tied to CALSPEC C26202 at ~1% (arXiv:1706.01542; arXiv:2305.01695),
  hardware metrology (arXiv:astro-ph/0604285; arXiv:2606.31822), stellar standards pointed
  to `surveys` §1. The fit, its degeneracies, the uniformity test and any propagation to
  photo-z or clustering are absent. **P.**
- L3: photometric models (arXiv:astro-ph/0703454, Eqs. 3–4; arXiv:1201.2208, Eq. 9;
  arXiv:1706.01542, Eqs. 7–12, 19, 26); star selection table (Step 2); the solve with error
  floors, the linear normal-matrix trick and the degeneracies handled by eigenmode
  projection (Eqs. 7–8, 27–29; arXiv:astro-ph/0703454, Eqs. 28–29); grey and
  non-photometric data (Sect. IV.3–IV.4); chromatic corrections (Sect. V.4); uniformity
  against Gaia DR1 and DR3, SDSS, SCR and corrected XPSP with pixel sizes
  (arXiv:1706.01542, Sect. V.3; arXiv:2305.01695, Sect. II; arXiv:2309.11225, Sects. III–IV);
  SCR and XPSP equations (Eqs. 1–3); uniformity is not the absolute scale. The effect on
  photo-z and on clustering is not answered: the dossier's "Not verified" says "How
  calibration errors propagate into photo-z and n(z): no paper read here quantifies it",
  and no clustering test of calibration residuals is described. **P.**

**Z2 — Chromatic effects and Milky Way extinction; testing dust maps; propagation into
photo-z and densities.**
- L2 (methods §3): chromatic errors 2% → < 0.3% (arXiv:1601.00117), FGCM folding, Rubin
  filter-edge shifts; four maps with their tracers (SFD, SF11 0.86 and F99, CSFD, DESI
  stellar; arXiv:1012.4804; arXiv:2306.03926; arXiv:2409.05140); extragalactic imprint in
  nine of ten maps (arXiv:1808.03294). How R_b is computed for a passband and SED, the map
  tests and the propagation into photo-z and counts are absent. **P.**
- L3: map construction and units (arXiv:1012.4804, Sect. I; arXiv:2306.03926,
  Sect. III.4–III.5; arXiv:2409.05140, Eqs. 1, 5–6); R_b from Eq. A1 with N = 0.78 kept
  apart from 0.86 (App. A, Table 6); SED dependence for stars and galaxies
  (arXiv:2409.05140, Sect. 5.4; arXiv:2310.14716, App. B.1); passband correction inside the
  template χ² (arXiv:2310.14716, Eqs. 6–9) and Δz = −0.0033 per nm (Sect. 4.2.1); chromatic
  errors per band for galaxies (arXiv:1601.00117, Table 4); four map tests (Eq. 18 stacks,
  galaxy back light, two-colour consistency, power spectra); propagation into counts
  (arXiv:1808.03294, Eqs. 9–16, 27–28; arXiv:1211.1015, Eqs. 37, 40), target density
  (+10 mmag → +11.0% ELG), colours [der]. Per-mmag photo-z shifts are stated as not found.
  **Y.**

**Z3 — ML photo-z methods; calibrated p(z); incomplete training sets; comparison with
templates in challenges.**
- L2 (methods §§5, 10): families with what each paper establishes (ANNz, TPZ, DNF, GPz
  variance terms, CNN, domain adaptation, UMAP-kNN), implicit priors and the four
  training-sample mechanisms (arXiv:2605.06790, Sects. 2.0.5–2.0.6), damage metrics
  (arXiv:2601.10797), the Euclid challenge PIT and F_005/F_015 (arXiv:2009.12112,
  Sect. 4.2), CDE loss (arXiv:2001.03621). How a PDF is produced per code, how it is
  calibrated after training, and the weighting or coverage-cut recipes are absent. **P.**
- L3: training compilations with quality cuts (arXiv:1704.05988, Sect. 2.1;
  arXiv:2510.07370, Sect. 2.2.1; arXiv:2512.11700, Sect. 3); CSL weights (arXiv:2203.01949,
  Eq. 4) used in validation too; features (asinh, errors as features, missing bands and the
  MNAR trap); splits and CDE-loss tuning (arXiv:1704.08095, Eq. 5); PDF construction per
  code (Step 5 table); post-hoc calibration by credible intervals (arXiv:2203.01949,
  Eqs. 7–9) and PIT diagnosis (arXiv:1704.05988, Sect. 6.2); coverage flags (Step 7);
  reweighting against GMM-Divide, StratLearn on the propensity score (arXiv:2106.11211,
  Sects. 3.1–4.3), adversarial domain adaptation; ML against templates in the Euclid
  challenge (better at z < 0.8, worse above; hybrid best; arXiv:2009.12112, Sects. 5.2,
  5.4). **Y.**

**Z4 — Hierarchical and population forward models of n(z); comparison with SOM and
clustering; remaining systematics.**
- L2 (methods §6): why stacking is biased (arXiv:2206.13633; CHIPPR, arXiv:2007.12178); table
  of approaches with headline accuracies (Leistedt 2016, Sánchez & Bernstein, Alarcon 2020,
  Alsing 2023 with its six-step chain in one line, pop-cosmos, GalSBI, learned SED prior);
  "most numbers come from simulations". How the population is fitted, the data model and
  selection, the comparison with SOM and clustering, and the population-model systematic
  are absent (pointer to `open`). **P.**
- L3: generative chain with Eq. 3 and the selection term (arXiv:2207.05819, Sects. II.2–II.4,
  Eqs. 1–5); four population families (Step 2 table); data models (Eqs. 16–19;
  arXiv:2602.03935, Sect. III.2); reproducing binning and selection (Sects. III.3–III.5);
  fitting by fixed defaults, optimal transport, ABC or Gibbs (Step 5 table; arXiv:2402.00935,
  Eq. 11; arXiv:2412.08701, Eq. 12; arXiv:2605.15078, Eqs. 6–7); model against sample
  variance (arXiv:2606.23783, Eq. 17); comparisons: BHM against stacking and against DIR and
  CC on KV450 (arXiv:2605.15078, Table 1, Sect. 4.3), hierarchical colours + clustering
  (arXiv:1910.07127, Eqs. 2, 17, Sect. 7); systematics: population model (shark against
  pop-cosmos, Δz ~ 0.05–0.1; arXiv:2602.03935, Sect. IV.1), dust and metallicity priors,
  extrapolation below training depth, inherited image simulation, ABC distance choice
  (arXiv:2412.08701, Eq. 26). **Y.**

**Z5 — Clustering redshifts and shear ratios; combination with SOM in DES, KiDS, HSC; what
they constrain.**
- L2 (methods §8): principle and Newman's error scaling, bias-evolution shift
  (arXiv:0805.1409, Eq. 21), Ménard's cell-by-cell variant, results table (KiDS mocks, DES Y3,
  DES Y6 importance sampling with its model equation, Euclid Flagship 1 and 2), shear ratios
  (arXiv:astro-ph/0306046; arXiv:2105.13542: up to 38%, 31%, 10%), HSC Y3 cross-correlations
  with LRGs (§7.2). Scales, estimator, reference-bias calibration, how WZ becomes an n(z)
  constraint and the shear-ratio construction are absent. **P.**
- L3: reference slicing and scales with reasons for DES Y6, Euclid and KiDS-Legacy
  (arXiv:2510.23565, Sects. II.2.1, IV.2.2; arXiv:2505.10416, Sects. 4.4–4.6;
  arXiv:2503.19440, Sects. 5.2, 6.2.2); DP against LS (Eqs. 19–20); reference bias
  (Eq. 6; KiDS Eq. 4); the sawtooth-basis model with magnification and Legendre systematic
  function, priors from Cardinal (Eqs. 7–18, Sect. IV.1); Euclid M0–M5 bias treatments
  (Eq. 49); covariances (Step 5); three routes to n(z): KiDS shift fit of the SOM template
  with excess-scatter term (arXiv:2503.19440, Eqs. 5–6), Euclid SSM and SGP
  (arXiv:2505.10416, Eqs. 72–77), DES Y6 importance sampling of ~10⁸ SOM realisations
  (arXiv:2510.23565, Sect. II.4); what they constrain (mean and width, shape freedom kept or
  not; template-shape leakage into D_z, Table 7); shear-ratio likelihood (arXiv:2105.13542,
  Eqs. 3–5, 24–27, Sects. III–IV). HSC rests on the L2 line (`methods` §7.2); the dossier
  has no HSC step. **Y.**

**Z6 — Many- and narrow-band surveys: how the precision is reached; role and limits as
calibration samples.**
- L2 (surveys §3): COSMOS2020, COSMOS2025, PAUS (design, COSMOS, wide), miniJPAS,
  J-PLUS/S-PLUS with precision and role ("the reference truth for many SOM and
  forward-model calibrations"), SPHEREx forecast and spectral confusion (arXiv:2312.04636;
  arXiv:2510.01410). How the precision is reached (templates, lines, zero points, PDFs) is
  absent. **P.**
- L3: NB flux calibration without standards (arXiv:2406.06850, Sects. 2.1, 4); template
  sets with emission lines in five configurations (Step 2 table; arXiv:1809.04375,
  Sects. 4.4–4.5; arXiv:2007.11132, Eq. 12; arXiv:2110.13923, Sect. V; arXiv:2108.03271,
  Sects. 3–4); the BCNz2 χ² with NB/BB scaling (arXiv:1809.04375, Eqs. 4–8); four zero-point
  schemes (Step 3 table); priors, ODDS and Q_z (Eqs. 15–16), PDF recalibration (κ = 0.13;
  Bordoloi remapping; Lorentzian; error rescaling ×2); template against ML on the same NB
  data (arXiv:2408.16864, Sect. 4.3); limitations: NB information vanishes at i ≳ 22.5
  (arXiv:2312.07581, Sect. 3.4), COSMOS2020 errors underestimated beyond i = 22.5
  (arXiv:2110.13923, Sect. V.3), mixed outlier thresholds. Sample variance and area of the
  fields are not discussed in either loaded file (they are in `syst` §7), and SPHEREx rests
  on the L2 forecast. **Y.**

**Z7 (control, template fitting).** L2 (methods §§4, 10): χ² and BPZ priors
(arXiv:astro-ph/9811189, Eqs. 5, 11–12), hyperz, LePhare zero-point training on 468 spectra
(arXiv:astro-ph/0603217, Sects. 4.1–5.1), EAZY linear combinations and template error
function (arXiv:0807.1533, Eqs. 1–2), what templates need; PDF calibration only as the
diagnosis "template PDFs too narrow (U-shaped PIT)" (arXiv:2009.12112, Sect. 4.2). Emission
lines and how a p(z) is recalibrated are absent. **P.** L3 (`narrow-many-band-photometry`):
emission-line templates and their measured ratios, COSMOS2020 LePhare and EAZY
configurations with offsets (arXiv:2110.13923, Sect. V, Table 3), four zero-point schemes,
priors, PDF recalibration (arXiv:1809.04375, Eq. 18; arXiv:2312.07581, Eq. 14;
arXiv:2108.03271, Eq. 7). **Y**: the control gains, served by
`deep/narrow-many-band-photometry.md`, whose Steps 2–5 are a template-fitting dossier for
many-band data.

**Z8 (control, SOM n(z)).** L2 (results §3): DES Y3 and Y6 SOMPZ budgets term by term,
including Balrog transfer < 0.001 and the deep–wide link p(z|b) = Σ p(z|c,b) p(c|ĉ) p(ĉ|b)
through Balrog injections (arXiv:2012.08566, Table 2; arXiv:2510.23566, Sects. 4.1–5.1,
Eqs. 5–11, Table 2), the calibration-sample term set by missing faint spectra (19% of the
calibration sample in the top bin), COSMOS2020 and PAUS perturbed by their offsets; KiDS
gold weights and SKiLLS biases (arXiv:2503.19440, Sects. 4.1–4.2, Table 8); HSC Y3 sample
variance carried in a logistic GP (arXiv:2211.16516, Sect. 5.4). **Y.** L3: no file-map row.
**Y**, no gain.

### Grades

| Q | L2 (a) | L3 (a) | L3 locator | Gain |
|---|---|---|---|---|
| Z1 | P | P | Y | partial |
| Z2 | P | Y | Y | yes |
| Z3 | P | Y | Y | yes |
| Z4 | P | Y | Y | yes |
| Z5 | P | Y | Y | yes |
| Z6 | P | Y | Y | yes |
| Z7 (c) | P | Y | Y | yes (control) |
| Z8 (c) | Y | — (no dossier) | Y | — |

**Verdict: pass.** L3 answers 5 of 6 with locators; 5 L2 failures answered (Z2–Z6); one
dossier per question. Z1 stays P: the calibration dossier builds and tests the calibration
but states that no paper read quantifies the propagation of residual zero-point errors
into photo-z or n(z), and gives no clustering test. Control Z7 gains, through
`deep/narrow-many-band-photometry.md` (template configurations, emission lines, zero
points, PDF recalibration); the file map's description of that dossier ("Narrow-band
photo-z") hides that it also serves broad-band template questions.

### Source checks (2 used)

- **D5** `deep/chromatic-extinction.md`, Step 5, used in Z2: in a step-function toy model
  Δz = −0.0033 Δμ per nm; 1 nm matches Euclid's 0.002 requirement; off-axis passbands bias
  photo-z high. arXiv:2310.14716, Sect. 4.2.1: "Δz = −0.0033 Δμ/1 nm", "a shift of 1 nm
  leads to a bias that is of similar amplitude to Euclid's requirement on the bias,
  Δz/(1+z) = 0.002", "photometric redshifts are expected to be biased positively if the
  central passbands are used". Match.
- **D6** `deep/population-forward-models.md`, "Which population model" and the Numbers row
  "Population-model shift | Δz ~ 0.05–0.1, highest bin", used in Z4. arXiv:2602.03935,
  Sect. IV.1: "the largest shift in the highest-redshift bin (Δz ~ 0.05–0.1)" (match for the
  sentence read); abstract and Sect. VI: "In the first (0.1 < z < 0.3) and last
  (0.9 < z < 1.2) tomographic bins we find systematic differences in the mean redshifts of
  Δz ~ 0.05–0.1". The dossier omits the first bin, which `SKILL.md` ("edge-bin means") and
  `results.md` ("bins 1 and 5") include. Incomplete; the dossier should say "first and last
  bins".

### Generality flags

- `deep/clustering-redshifts-shear-ratio.md`: 40 of 68 citations are to the two
  d'Assignies et al. 2025 papers (DES Y6, arXiv:2510.23565; Euclid, arXiv:2505.10416), and
  HSC appears once; the HSC Y3 cross-correlation route (Rau et al., arXiv:2211.16516) is not
  described, although the question and the subtopic name DES, KiDS and HSC. The DES-recipe
  bias is acknowledged in the reading list ("the most complete current recipe").
- `deep/population-forward-models.md`: 56 of 98 citations are to the pop-cosmos papers
  (Alsing, Leistedt et al.: arXiv:2602.03935, arXiv:2207.05819, arXiv:2402.00935); GalSBI
  (three papers) and Kyriacou et al. give the alternatives in their own steps. Mild.
- `deep/narrow-many-band-photometry.md`: 65 of 99 citations are to six PAUS papers; COSMOS2020
  and miniJPAS are the other configurations, and SPHEREx, named in the subtopic, is under
  "Not verified" (its photo-z method was not read).
- `deep/photometric-calibration.md`: FGCM/DES carries 36 of 78 citations, with SDSS, PS1 and
  J-PLUS set beside it in every step. No flag.

## cosmo-reionization-21cm

The `files` column and the file map agree: six dossier rows; none for `damping-wings` or
`global-signal`. The `files` column of `eor-cross-correlations` lists only
`open-questions.md` besides the dossier, so R4's L2 run loads `open`.

### Files loaded

| Q | L2 reference file | L3 dossier |
|---|---|---|
| R1 | methods | `deep/lya-emitters.md` |
| R2 | methods | `deep/ionising-photon-budget.md` |
| R3 | methods | `deep/eor-inference-modelling.md` |
| R4 | open | `deep/eor-cross-correlations.md` |
| R5 | methods | `deep/hi-intensity-mapping.md` |
| R6 | methods | `deep/line-intensity-mapping.md` |
| R7 (control) | syst | none: no file-map row for damping wings |
| R8 (control) | syst | none: no file-map row for the global signal |

### Answers

**R1 — x_HI from Lyα fractions and LAE luminosity functions: baseline, IGM transmission,
ISM, inflows, velocity offsets; why x_HI(z) differ.**
- L2 (methods §1.4): observable (X_Lyα above 25 or 10 Å, or the LAE luminosity function),
  origins (arXiv:astro-ph/0407408; arXiv:1003.5244), the Mason et al. Bayesian framework with
  velocity offsets and the full EW distribution (arXiv:1709.05356), the z ~ 5–6 baseline
  (arXiv:2509.18302) and THESAN transmission (arXiv:2609.40363). No baseline forms, no
  transmission model, no likelihood, no account of why analyses differ. **P.**
- L3: line measurement with JWST grating and prism and from the ground, limits,
  completeness and slit loss (arXiv:2408.01507, Sects. II.2–II.5; arXiv:2509.18302,
  Sect. 3.1); four baseline forms with their parameters (Step 2 table; arXiv:1709.05356,
  Eq. 4; arXiv:2609.40363, Eqs. 4–5); transmission τ_IGM = τ_D + τ_HII with three
  treatments of infall, line profile and simulation (Step 3 table; arXiv:1709.05356,
  Eqs. 1–2, 5–6; arXiv:2609.40363, Eqs. 6–11); likelihoods (Eqs. 9–13); why values differ:
  baseline redshift and form (≈ 0.1–0.2 in fraction), EW against bright-end LF calibration,
  line widths and offsets, topology and box size, threshold and envelope statistics,
  field-to-field structure (arXiv:2505.24080, Sect. V.2). The LAE luminosity-function route
  named in the question is not described: the dossier's "Not verified" says "The Lyα
  luminosity-function and clustering route (narrow-band surveys) was not read at source";
  only its use as a contaminated upper limit in a joint fit is recorded
  (arXiv:2504.09725, Eq. 21). **P.**

**R2 — Closing the photon budget: LF to a limiting magnitude, ξ_ion, f_esc, clumping; JWST
ξ_ion; weighing AGN, lower f_esc, faint cutoff.**
- L2 (methods §1.6): bookkeeping, the Madau–Haardt–Rees criterion
  (arXiv:astro-ph/9809058), clumping and f_esc > 0.2 (arXiv:0807.3963), the pre-JWST budget
  (arXiv:1502.02024), JWST overproduction (arXiv:2404.07250), mass-complete correction
  (arXiv:2409.01286), per-object f_esc (arXiv:2607.22834). No equations, no measurement
  recipes and no weighing of the resolutions. **P.**
- L3: balance equation and its static and mass-weighted variants (arXiv:2404.07250,
  Eqs. 1–2; arXiv:2606.14671, Eq. 10; arXiv:1311.2152; arXiv:2004.07854); emissivity
  integral (Eq. 3); ξ_ion from Hα, [O III] or SED (arXiv:2409.01286, Sect. 5.1); five f_esc
  prescriptions with their calibrations (Step 4); LF choices and cutoffs, lognormal mean
  correction ×4.0 [der] (Step 5); clumping table including C ≈ 12 from Γ_HI and λ_mfp
  (arXiv:2406.18186, Eqs. 5, 12–13); checks against τ and the forest emissivity
  (arXiv:1307.2259, Eqs. 2–5); weighing: cutoff −17 with 15% or −11 with 3%, C = 20 still
  > 3σ, lower f_esc at fixed β or an f_esc–ξ_ion anti-correlation (arXiv:2404.07250,
  Sect. 4), strong leakers giving 87% of photons, the cutoff mattering < 0.1 in z with a
  simulation-calibrated relation (arXiv:2606.14671, Sect. 4.5); four routes compared
  (table). AGN are only named as left out ("not researched"). **Y.**

**R3 — 21 cm upper limits to astrophysics: simulators, emulators, likelihood of a limit,
parametrisations; joint inference with τ, LFs, forest.**
- L2 (methods §§2, 5.3, 6): parameters the limits touch (L_X/SFR, radio efficiency, minimum
  halo mass; arXiv:2210.04912; arXiv:2508.13761; arXiv:2504.09725), codes (21cmFAST,
  21cmEMUv3, GRIZZLY), reporting conventions (2σ, k and z). The likelihood of an upper limit,
  the model parameters and priors, and the joint likelihoods are absent. **P.**
- L3: systematics-marginalised erf likelihood with u ≥ 0 and its reasons
  (arXiv:2108.07282, Eqs. 9–13, Sect. III.2.1), decimation, inverse and exclusion
  likelihoods (Eq. 14; arXiv:2505.00373, Eqs. 3–4); four HERA models and the nine 21cmFAST
  parameters (Eqs. 18–20); GRIZZLY, 21cmSPACE and 21cmEMUv3 parametrisations including the
  radio background (arXiv:2505.00373, Eq. 1; arXiv:2504.09725, Table 2); theory error 20%
  or 30%; joint L_m × L_LFs × L_DF × L_τ, the late-EoR Gaussian and the LOFAR stepwise τ
  (arXiv:2108.07282, Sect. V.2; arXiv:2309.05697, Sect. 4.3); NDE likelihoods and the
  contaminated-upper-limit form (arXiv:2504.09725, Eqs. 19, 31–32); erf against Gaussian
  against neural likelihood (arXiv:2305.03074, Sect. 5); samplers at prior edges; the Pop III
  population weakening the X-ray bound (arXiv:2307.15577; arXiv:2606.00219, Sect. 5.1).
  **Y.**

**R4 — 21 cm cross-correlations during reionisation: sign and scale, foreground avoidance,
galaxy redshift precision; measurements and forecasts.**
- L2 (open): nothing on EoR cross-correlations; §3 corrects "21 cm has only
  cross-correlation detections" for post-reionisation HI only. **N.**
- L3: tracer and statistic table (Step 1), cylindrical cross-power on modes outside the
  wedge with m(z) and three foreground scenarios (arXiv:2502.20447, Eqs. 20–21), the
  window forms W_fg and W_gal (arXiv:2609.35957, Eqs. 6–7), variance with redshift-error
  suppression (arXiv:2502.20447, Eqs. 22–27), Monte Carlo errors (arXiv:2407.14588, Eq. 24),
  sign change and turnover (arXiv:2404.08266), squared-field statistics for photometric
  galaxies and kSZ with their filters (arXiv:2609.35957, Eqs. 9–11; arXiv:2503.09462,
  Eqs. 8–20); redshift precision against area: narrow band fails, Roman grism 8σ per beam
  and 54.8σ for 47 beams, MOONS ~3σ (arXiv:2502.20447, Sect. 5.1, Tables 2–3); the only data,
  MWA × Planck, consistent with zero (arXiv:1803.00756). **Y.**

**R5 — HI intensity mapping, single-dish against interferometer: cleaning, transfer function
by mock injection, Ω_HI b_HI r, detections, BAO.**
- L2 (methods §§3, 5.2, 5.4): two modes and their scales (arXiv:2606.25955;
  arXiv:2202.01242; arXiv:2607.09374), the three amplitude combinations and that they are
  not interchangeable (arXiv:1208.0331; arXiv:2610.12158; arXiv:2603.25680), PCA and FastICA
  with transfer function by mock injection (arXiv:2102.04946; arXiv:2302.07034), per-analysis
  rows: MeerKLASS 2022 T(k) from 100 lognormal mocks (arXiv:2206.01579, Eqs. 19–20),
  MeerKLASS 2026 loss modelled as (k/h Mpc⁻¹)^β, CHIME DAYENU filtering with the stored
  filter applied to the simulations and its Δχ² significance (arXiv:2511.19620); detections
  in `SKILL.md` (CHIME 12.5σ, MeerKLASS S/N 6.2, no BAO) and the SKA BAO template plan
  (arXiv:2607.03259, Sect. 4.1). GPR for HI, FAST and Parkes are absent. **Y.**
- L3: the single-dish chain step by step: scanning and diode calibration, the KATcali
  model and self-calibration (arXiv:2407.21626, Eqs. 1–6), map-making (arXiv:2206.01579,
  Eqs. 1–2), shuffled subsets, reconvolution choices with reasons (Step 4 table), mPCA and
  the N_fg selection rule (arXiv:2610.12158, Sects. 3, 8, Table 3), jackknife covariance
  (Eq. 12), the fitted model with beam, window and D(k) (Eqs. 14–28), null and injection
  tests with p-values (Sects. 10.2, 10.7). The interferometric route, GPR, FAST and Parkes
  are not in the dossier ("not re-examined here"). **Y**, gain in depth only: L2 had
  already answered.

**R6 — CO and [CII] intensity mapping: power spectrum against VID, interlopers, stacking;
L(M_h) constraints.**
- L2 (methods §§4, 5.4): clustering + shot model with ⟨Tb⟩² (arXiv:2111.05927), burstiness of
  shot noise (arXiv:2605.13967), interlopers masked, modelled or crossed (arXiv:2607.20404),
  stack, CVID and cross-power compared (arXiv:2603.13218), tomographic backgrounds
  (arXiv:2602.02658), the COMAP Season 2 row (arXiv:2406.07511, Eqs. 2, 18–20). How an upper
  limit becomes an L(M_h) or ρ_H2 statement, the VID formalism and the interloper
  anisotropy are absent. **P.**
- L3: time-stream cleaning and the η = 0 cut (arXiv:2607.20404, Eqs. 7–10; arXiv:2008.08087,
  Sect. III.2.1); feed-group × elevation cross-spectra and RND errors (arXiv:2406.07511,
  Eqs. 1–13); two-amplitude fit (arXiv:2406.07512, Eqs. 1–5); five-parameter L′_CO(M_h) with
  UM and COLDz priors (Eqs. 6–12) and the Li et al. chain (arXiv:1503.08833, Eqs. 1–5);
  ρ_H2 with α_CO (Eq. 13); matched-filter stack with its attenuation factors
  (arXiv:2510.23568, Eqs. 13–16, Sect. 6); VID and CVID (arXiv:1609.01728, Eqs. 5–18;
  arXiv:2603.13218, Eqs. 8–15); line–line and galaxy crosses (arXiv:2606.10005, Eq. 24);
  estimator comparison on the same simulations (S/N 8.42, 4.47, 3.92; A to 27% combined);
  interloper treatments with the Lidz & Taylor anisotropy (arXiv:1604.05737, Eqs. 5–8).
  CONCERTO and TIME are not covered. **Y.**

**R7 (control, damping wings).** L2 (syst §3): error sources (patchy topology, lifetime,
intrinsic continuum, noise; arXiv:2406.12070), single-object width ±0.2–0.26 after
marginalising the lifetime (arXiv:1802.06066), continuum share ~15% against ~28% with the
proximity zone modelled and coverage-corrected posteriors (arXiv:2406.12070, Sect. 5.7),
PCA predictor (arXiv:1801.07679), the XQR-30 covariance method's 10% bias and its
calibration (arXiv:2404.12585, Sects. 3.3–3.4), dense absorbers; galaxies: local DLA
degeneracy at R ~ 100 and R ~ 1000 (arXiv:2501.13899), template and stacking mitigation
(arXiv:2504.04683), topology prior. **Y.** L3: no dossier row. **Y**, no gain.

**R8 (control, global signal).** L2 (syst §7): foreground-model degeneracy
(arXiv:1805.01421), ground-plane resonance (arXiv:1810.09015), calibration and noise model
in the evidence (arXiv:1910.03165), beam chromaticity and the beam factor with its
assumptions (Eqs. 3–4; arXiv:2605.16643, Eq. 35), its size 370 to 670 mK, foreground
order and forms (Eqs. 10–11), dynamic range, the independent-instrument standard and SARAS 3
(arXiv:2112.06778). **Y.** L3: no dossier row. **Y**, no gain.

### Grades

| Q | L2 (a) | L3 (a) | L3 locator | Gain |
|---|---|---|---|---|
| R1 | P | P | Y | partial |
| R2 | P | Y | Y | yes |
| R3 | P | Y | Y | yes |
| R4 | N | Y | Y | yes |
| R5 | Y | Y | Y | depth only |
| R6 | P | Y | Y | yes |
| R7 (c) | Y | — (no dossier) | Y | — |
| R8 (c) | Y | — (no dossier) | Y | — |

**Verdict: pass.** L3 answers 5 of 6 with locators; 4 L2 failures answered (R2, R3, R4,
R6); one dossier per question; controls inert. R1 stays P: the Lyα-emitter dossier
covers the equivalent-width route only, and says that the luminosity-function route was
not read. R5 is answered at L2 already; the HI dossier deepens the single-dish chain but
adds nothing on the interferometric route, which the question contrasts with it. EoR
cross-correlations are absent from L2 altogether (R4, N).

### Source checks (2 used)

- **D7** `deep/eor-inference-modelling.md`, Step 4, used in R3: the HERA τ prior is
  0.0569 (+0.0081/−0.0066) in the HERA theory paper and quoted as (+0.0081/−0.0086) in
  21cmEMUv3; "the two readings disagree on the lower error". arXiv:2108.07282, Sect. V.2:
  "τ_e = 0.0569^{+0.0081}_{−0.0066}"; arXiv:2606.00219, Sect. 5.1: "τ_e =
  0.0569^{+0.0081}_{−0.0086}". Match: the dossier reports both texts correctly; which is the
  Qin et al. value was not checked here.
- **D8** `deep/eor-cross-correlations.md`, "Galaxy redshift precision against area", used in
  R4: Roman HLS within one SKA-Low AA* beam gives 8σ, and 47 beams in 500 deg² give
  √47 × 8 = 54.8σ. arXiv:2502.20447, Sect. 5.1: "a single patch of the SKA-low AA* beam
  within Roman HLS yields an 8σ detection", "47 patches ... within 500 sq. deg. of
  overlapping area ... √47·8 = 54.8". Match. The paragraph sits in the section titled
  "SKA–Lyman Alpha", which the dossier's "Grism" row does not say; no error.

### Generality flags

- `deep/hi-intensity-mapping.md` rests on one experiment by design: 85 of 86 citations are to
  MeerKLASS or the SKA chapter (arXiv:2610.12158 alone 44); GBT, FAST and Parkes are absent
  and the interferometric route is left to L2. The scope line says so ("follows the
  single-dish MeerKLASS chain"); the file-map row ("Single-dish HI: calibration to Ω_HI
  b_HI") is accurate, but a reader with a CHIME, HIRAX or CHORD question gets no dossier.
- `deep/line-intensity-mapping.md`: COMAP papers carry 29 of 80 citations; CONCERTO and TIME,
  named in the skill's survey file, do not appear. Mild.
- `deep/eor-inference-modelling.md`: HERA papers 32 of 96, with LOFAR, MWA, the joint
  21cmSPACE fit and the 21cmEMU line set beside them. No flag.
- `deep/lya-emitters.md` and `deep/ionising-photon-budget.md`: top source 18 of 66 and 22 of
  101; four or more groups per step. No flag.
