# Interpretability and symbolic regression — cosmo-machine-learning dossier

Scope: how an attribution study of a trained network is run and checked (saliency family,
model-randomisation sanity test, mapping attributions onto a physical variable, masked and
null-class controls), and how a symbolic regression is set up and its formula chosen (target
transform, operator set and complexity weights, search engine, selection by description length,
loss-per-complexity score or accuracy target, post-processing, validation and domain of
validity); and how to choose between gradient and propagation saliency, Shapley attributions,
genetic and exhaustive searches, direct regression and distillation of a network.
Snapshot: 2026-10-19.
From: Huertas-Company & Lanusse 2022 review (arXiv:2210.01813), Sects. 5.3 and 7.3.3.

Already in L2, not repeated here: the attribution findings on lensing CNNs and CMB maps and the
neural marked spectrum, and the symbolic-regression tools and results (ESR on H(z), the symbolic
P_L(k) and CMBolic accuracies) (`physics-and-methods.md#interpretability-and-symbolic-regression`);
the debate on whether interpretation is needed and what symbolic emulators reach
(`open-questions.md#interpretability`, `open-questions.md#emulators-neural-gaussian-process-or-symbolic`).
Neural emulators and their error budgets are in `deep/emulators.md`.

Symbols. M: the trained network, mapping an input x of d pixels to n outputs; S(x): a saliency
map of the same size as x; φ_i: Shapley attribution of input i; c or C(E): complexity of an
expression E (node count, possibly weighted); L(D): description length of data D; 𝓛:
likelihood; θ̂: maximum-likelihood parameters of a formula; I_ii: diagonal Fisher element;
k: number of nodes; n: number of distinct operators; p: number of free parameters.

## How it is done
<!-- key: how-it-is-done -->

### A. Attribution of a trained network
<!-- key: attribution-of-a-trained-network -->

**Step A1. Choose candidate saliency methods.** Zorrilla Matilla et al. compare two families on a
CNN that regresses (Ω_m, σ8) from 512 × 512 convergence maps (arXiv:2007.06529)
[src: Sect. IV]:

- gradient based: S(x) = ∂M/∂x (for a linear model, the regression coefficients) and
  input × gradient, S(x) = x ⊙ ∂M/∂x (for a linear model, each pixel's contribution);
- propagation based: guided backpropagation, deconvnet, deep Taylor decomposition, and
  layer-wise relevance propagation with the ε rule R_i = Σ_j a_i w_ij/(ε + Σ_i a_i w_ij) R_j
  (a_i activations, w_ij weights) or the αβ rule.

SmoothGrad and integrated gradients were set aside for cost after a check on a few maps gave
qualitatively similar results [src: Sect. IV].

**Step A2. Run the model-parameter randomisation test** (arXiv:2007.06529). Recompute each saliency map after
randomising the weights layer by layer from the output to the first convolution; a map that does
not change cannot reflect what the network learned [src: Sect. IV.1]. Score the similarity of
the trained and fully randomised maps with Pearson r, Spearman ρ and Kendall τ, with "no
correlation" as the null hypothesis [src: same, Table 2]. Only the two gradient methods kept the
null for all three tests (Pearson r = −0.002 and −0.003); deep Taylor gave r = 0.882 and
deconvnet −0.731, so they were dropped [src: Table 2]. Visually, three propagation methods
highlighted high-κ peaks while the gradient methods put relevance near local minima: the
methods disagree on the same map before any test [src: Sect. IV.1, Fig. 4].

**Step A3. Map attributions onto a physical variable** (arXiv:2007.06529). Square the saliency (so that signs do not
cancel), sum it over pixels in 20 linear bins of κ in [−2.5, 5] in units of each map's rms
σ_κ, add the Ω_m and σ8 outputs, and also divide by the pixel count per bin; do this for each of
the 101 cosmologies, with and without shape noise [src: Sect. IV.2]. Noiseless: negative-κ
pixels carry 86% (gradient) and 83% (input × gradient) of the squared saliency; with noise only
13% and 2%, while κ > 3σ_κ carries 36% and 68% [src: Sect. IV.2]. The dip of input × gradient at
κ = 0 is an artefact of the zero input [src: same].

**Step A4. Shapley attribution with controls.** For a CMB-map classifier (ΛCDM against a
primordial-feature model), Ocampo & Cañas-Herrera define φ_i = Σ_{S ⊆ M∖{i}} |S|!(M − |S| −
1)!/M! [f_S(x ∪ {i}) − f_S(x)], with M the number of input features and f_S the model restricted
to the subset S (arXiv:2604.05290, Eq. 12). They use Partition SHAP, which clusters pixels
hierarchically to respect spatial correlations, and project φ back onto the HEALPix sphere
[src: Sect. 3.5]. Three controls are read: the Galactic mask (no border effect at the cut), the
other class (ΛCDM attribution maps are "essentially featureless"), and the three channels T, Q,
U (balanced contributions) [src: Sect. 4.2]. Before the attribution, the PCA stage was fitted on
the training data only, to prevent leakage [src: Sect. 3.4]. The authors state that SHAP
"provides a diagnostic of model behaviour and decision-making, rather than a proof of localized
physical causation" [src: Sect. 4.2].

### B. Symbolic regression of a smooth target
<!-- key: symbolic-regression-of-a-smooth-target -->

**Step B1. Transform the target and the inputs.** Fit a residual on top of a physical
approximation: P(k; θ) = P_EH(k; θ) F(k; θ) with P_EH the zero-baryon Eisenstein–Hu fit, so that
only a few-per-cent residual with the BAO is learned; regress 100 log F, which keeps P positive
and makes the target O(1) (arXiv:2311.15865) [src: Sect. 5, Eq. 5]. For galaxy properties, build
dimensionless combinations first (arXiv:2602.07651) [src: Sect. II.3]; for pairwise forces, use
Δx and r = (Δx² + Δy² + Δz²)^½ instead of raw positions (arXiv:2006.11287) [src: App. C].

**Step B2. Fix the operator set, constraints and complexity measure.**

| Study | Operators | Constraints and complexity | Place read |
|---|---|---|---|
| GNN distillation (eureqa) | +, −, ×, /, >, <, ^, exp, log, IF(·,·,·), real constants | node count; ^, exp, log and IF weighted three times | arXiv:2006.11287, App. C |
| Symbolic P_L(k) (Operon) | +, −, ×, log, cos, power, analytic quotient aq(x, y) = x/√(1 + y²) | a scaling parameter on every terminal, fitted by Levenberg–Marquardt; "length" excludes them, "complexity" includes them | arXiv:2311.15865, Sects. 3, 5 |
| ESR | {x, a, inv, +, −, ×, ÷, pow} up to complexity 10 | exhaustive; duplicates removed by simplification | arXiv:2211.11461, Sect. II-E |
| Ω_m from one galaxy (PySR) | +, −, ×, /, power; exp, ln, abs, √, sigmoid | exponents in [−3, 3]; no nesting of identical unary operators; coefficients re-optimised | arXiv:2602.07651, Sect. II.2.1 |

**Step B3. Run the search.**

- PySR: a multi-population evolutionary algorithm with tournament selection, age-regularised
  replacement (the oldest member is replaced), simulated annealing of mutations
  (rejection probability exp((L_F − L_E)/(αT))), an evolve–simplify–optimise loop and migration
  between populations; defaults n_p = 40 populations of L = 1000 expressions, 3 × 10⁵ mutations
  per evolve call, crossover probability 0.01, migration fractions 0.05
  (arXiv:2305.01582) [src: Sect. 2.1, Algorithms 1–2]. Its complexity penalty is adaptive,
  ℓ(E) = ℓ_pred(E) exp(frecency[C(E)]), so that each complexity keeps about as many expressions
  as the others and the search does not specialise early [src: Sect. 2.1, Eq. 2]. Noisy data can
  be denoised by a Gaussian process first or weighted by 1/σ² [src: "Additional Features"].
- Operon: genetic programming with NSGA2 non-dominated sorting and ε-dominance (objective values
  within ε treated as equal), ε = 10⁻³ and 10⁸ function evaluations for P_L(k); chosen for
  speed, memory and benchmark performance (arXiv:2311.15865) [src: Sects. 3, 5].
- ESR: generate every valid tree, simplify and remove duplicates, optimise the parameters of the
  unique ones: of a naive ~168 million functions to complexity 10, 5.2 million are valid trees,
  134 234 unique, and 119 861 need optimisation (arXiv:2211.11461) [src: Sect. II-E].
- Distillation: train a GNN with an L1 (or KL) penalty on its messages so that they become
  compact, keep the message components of largest standard deviation (largest μ² + σ² − log σ²
  for the KL model), fit each with symbolic regression on 5000 examples, substitute the
  expressions into the model and refit all constants on the original data "to avoid the
  accumulated approximation error" (arXiv:2006.11287) [src: "Compact internal
  representations", App. C, Sect. 4.3]. The stated gain: a search over f(Σ g(x)) costs
  2 × 10⁹ instead of 10¹⁸ candidate equations when f and g are fitted separately
  [src: "Symbolic regression"].

**Step B4. Select one formula from the Pareto front.**

- With statistical errors, minimise the description length (arXiv:2211.11461, Eq. 6):
  L(D) = −log 𝓛(θ̂) + k log n − (p/2) log 3 + Σ_j log c_j + Σ_i [½ log I_ii + log |θ̂_i|],
  where c_j are integer constants created by simplification. It follows from a two-part code,
  functional form plus residuals, with each parameter sent to the precision Δ_i = (12/I_ii)^½
  that minimises the expected codelength (Eqs. 1–5); a parameter with |θ̂_i|/Δ_i < 1 is set to
  zero and p reduced by one [src: Sect. III]. The authors chose MDL because AIC, BIC and DIC count
  parameters but not functional complexity [src: Sect. III].
- Without noise (emulating a code): maximise −Δ log(MAE_c)/Δc between successive best models
  (arXiv:2006.11287) [src: App. C]; PySR's "score" is the same idea (as described in
  arXiv:2311.15865, Sect. 3). The symbolic P_L(k) instead keeps formulas whose loss is below a
  set level and whose training and validation losses agree, then inspects them by eye; it
  reports length 77 (37 parameters), at a plateau of accuracy between lengths ~65 and 80 beyond
  which doubling the length gains a factor ~2 and the training and validation curves part
  [src: Sect. 5]. The score rule would have picked length 80, of almost identical form
  [src: same].
- With a survey accuracy target: CMBolic sets 1% from the lensing-reconstruction noise of
  Planck, ACT DR6, SO and a CMB-S4-like design, requires the 2σ validation band under 1%, hence
  an RMSE near 0.5%, and checks the ℓ-dependent 68% and 95% bands so that no localised residual
  hides behind a small mean (arXiv:2606.07745) [src: Sects. 4.3, 4.5].

**Step B5. Post-process, refit and validate.** CMBolic removes offsets below the target
accuracy and terms that do not contribute, rounds two coefficients within 10⁻⁵ of unity, refits,
then rounds all coefficients to four significant figures and repeats the tests; complexity fell
by 6 without loss of accuracy, which the authors attribute to bloat in genetic programming
(arXiv:2606.07745) [src: Sect. 4.4]. Validation is on the full grid of 5000 multipoles, not only
the log-subsampled training multipoles [src: Sect. 4.5]. Training sets can be small: 100
Latin-hypercube cosmologies for training and 100 for validation, 200 k values in
9 × 10⁻³ – 9 h Mpc⁻¹, for the symbolic P_L(k) (arXiv:2311.15865) [src: Sects. 4, 5].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Gradient, propagation or Shapley attribution
<!-- key: gradient-propagation-or-shapley-attribution -->

Gradient maps passed the randomisation test and propagation maps did not on the lensing CNN, so
only the cheapest methods were trusted (arXiv:2007.06529) [src: Sect. IV.1, Table 2]. Shapley
values attribute the output itself and can follow spatial correlation through a hierarchical
masker, at the price of many model evaluations; the CMB study fed SHAP a PCA-plus-MLP pipeline,
partly because it suits the SHAP analysis and because CNNs trained on raw maps with Adam or SGD
failed to converge [src: arXiv:2604.05290, Sect. 3.4]. Neither study isolates a physical
process: the lensing paper relates relevance to κ ranges, the CMB paper to "global variance"
[src: arXiv:2007.06529, Sect. IV.2; arXiv:2604.05290, Sect. 4.2].

### Genetic search or exhaustive search
<!-- key: genetic-search-or-exhaustive-search -->

| Engine | Buys | Costs | Place read |
|---|---|---|---|
| PySR, Operon (genetic) | high complexities (length 77 for P_L(k)); several inputs | stochastic: a run "may yield slightly different analytic forms" with deterministic = False; no guarantee of the best function | arXiv:2602.07651, Sect. II.2.1; arXiv:2311.15865, Sect. 5 |
| ESR (exhaustive) | every function to the given complexity is scored, so the best one is found if the parameter optimisation finds global optima | complexity ≲ 10, univariate applications only; memory and runtime grow with the basis set; duplicate detection imperfect | arXiv:2211.11461, Sect. V-A |

On EmpiricalBench (8 cores, up to 1 h per method), PySR recovered Hubble's law in 5 of 5 runs
against 1 of 5 for DSR and 0 of 5 for Operon, EQL, QLattice and SR-Transformer, and Kepler's law
in 5 of 5 against 4 of 5 for DSR and 0 of 5 for Operon, EQL and QLattice (arXiv:2305.01582)
[src: Sect. 3.2.1, table]. The benchmark is the PySR authors'
own; Operon was chosen by the P_L(k) authors on other benchmarks [src: arXiv:2311.15865, Sect. 3].

### Description length, loss-per-complexity score, or a target accuracy
<!-- key: description-length-loss-per-complexity-score-or -->

MDL is principled only when the data carry noise; for a noiseless code output the P_L(k)
authors "have to rely on heuristic methods" (arXiv:2311.15865) [src: Sect. 3]. The score and
the visual choice agreed there (77 against 80) [src: Sect. 5]. A target set in units of the
survey's noise ties the choice to the use (CMBolic) [src: arXiv:2606.07745, Sect. 4.3].

### Direct regression or distillation of a network
<!-- key: direct-regression-or-distillation-of-a-network -->

Distillation factorises a high-dimensional problem into low-dimensional ones and inherits the
network's inductive bias (arXiv:2006.11287) [src: "Symbolic regression"]. On Quijote halos the
distilled formula for the smoothed overdensity δ_i reached a mean absolute error of 0.0882
against 0.121 for a hand-designed formula [src: Sect. 4.3, Table 2]. With the 20% of halos with
δ_i > 1 masked from training, the GNN's error went from 0.0634 (training) to 0.142 (masked
halos) and the formula's from 0.0811 to 0.0892 [src: "Symbolic generalization"].

### A formula across simulators
<!-- key: a-formula-across-simulators -->

The Ω_m formula from galaxy properties was found on IllustrisTNG only (1000 simulations × 30
galaxies at z = 0) and applied to Astrid, SIMBA and Swift-EAGLE with the same functional form,
but with three coefficients {k_sim, c0_sim, a0_sim} refitted per suite: k_sim = 5.68, 4.71,
14.88, 8.58 (arXiv:2602.07651) [src: Sects. II.2.2, III.1, Table 3]. Finding an equally compact
formula by training on the other suites was "substantially more difficult" [src: Sect. III.1].

A transferable form with per-simulator coefficients is not a transferable estimator: on data the
right coefficients are unknown [der].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Randomisation-test correlation (Pearson) | gradient −0.002, input × gradient −0.003, guided backprop 0.152, deconvnet −0.731, deep Taylor 0.882 | lensing CNN | arXiv:2007.06529 | Table 2 |
| κ binning of attributions | 20 linear bins, κ ∈ [−2.5, 5] σ_κ | lensing CNN | arXiv:2007.06529 | Sect. IV.2 |
| PySR defaults | 40 populations × 1000; 3 × 10⁵ mutations per call; p_cross = 0.01 | PySR | arXiv:2305.01582 | Sect. 2.1, Algorithms 1–2 |
| PySR run for Ω_m formula | 1500 iterations, 30 populations, squared loss, "best" selection | one-galaxy formula | arXiv:2602.07651 | Sect. II.2.1 |
| Operon settings | ε = 10⁻³; 10⁸ evaluations | symbolic P_L(k) | arXiv:2311.15865 | Sect. 5 |
| Training / validation set | 100 + 100 LH cosmologies; 200 k values | symbolic P_L(k) | arXiv:2311.15865 | Sect. 5 |
| Chosen formula | length 77, 37 parameters; sub-percent for 95% of cosmologies | symbolic P_L(k) | arXiv:2311.15865 | Sect. 5 |
| ESR function counts to complexity 10 | ~168 million naive, 5.2 million valid, 134 234 unique, 119 861 optimised | ESR | arXiv:2211.11461 | Sect. II-E |
| Parameter precision in MDL | Δ_i = (12/I_ii)^½ | ESR | arXiv:2211.11461 | Sect. III, Eq. 5 |
| Accuracy target | 1% baseline; RMSE ≈ 0.5% for a 2σ band under 1% | CMBolic | arXiv:2606.07745 | Sects. 4.3, 4.5 |
| Coefficient rounding | 4 significant figures, tests repeated | CMBolic | arXiv:2606.07745 | Sect. 4.4 |
| Distillation sample | 5000 examples per fit; 215 854 halos, 71 neighbours on average | GNN distillation | arXiv:2006.11287 | App. C, Sect. 4.3 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **A saliency map that ignores the weights.** Propagation methods produced maps correlated with
  those of a randomised network (deep Taylor r = 0.882) (arXiv:2007.06529) [src: Table 2]. Test:
  model-parameter randomisation, layer by layer.
- **Methods that disagree.** Different saliency methods highlighted peaks or voids on the same
  map [src: arXiv:2007.06529, Sect. IV.1]. Report the method and the test that selected it.
- **Artefacts of the input.** Input × gradient vanishes where the input is zero, which produced a
  spurious dip at κ = 0 [src: arXiv:2007.06529, Sect. IV.2].
- **Attribution read as causation.** SHAP shows which pixels moved the output, not which
  physical process (arXiv:2604.05290) [src: Sect. 4.2]. A robustness claim needs a
  cross-simulator test (L2, `systematics.md#simulator-dependence`), not an attribution map.
- **Leakage through preprocessing.** A PCA or scaler fitted on all data leaks the test set into
  the attribution pipeline; fit it on the training set only (arXiv:2604.05290) [src: Sect. 3.4].
- **Overfitting along the Pareto front.** Beyond a length of ~80 the P_L(k) training and
  validation losses part (arXiv:2311.15865) [src: Sect. 5]. Test: plot both fronts and choose
  where they still agree (also arXiv:2606.07745, Sect. 4.5).
- **Accumulated fitting error.** Fitting sub-formulas separately compounds their errors; refit
  all constants of the assembled formula on the original data (arXiv:2006.11287, Sect. 4.3;
  arXiv:2606.07745, Sect. 4.4) [src].
- **The formula emulates a code, not the Universe.** CMBolic reproduces CLASS v3.3.0 with HMcode
  2020; switching to Halofit changes C_ℓ^φφ by up to 4.4% for a Planck-like cosmology, and the
  formula is validated only for 2 ≤ ℓ ≤ 5500 and its parameter ranges
  (arXiv:2606.07745) [src: Sect. 5.2].
- **Data too weak to select a law.** ESR found current chronometer and SN data unable to prefer
  ΛCDM over simpler expansion histories; on mocks at the present ~20% fractional precision it
  needs ~10³ H(z) measurements in the same redshift range for "sufficient constraining power"
  (arXiv:2211.11461) [src: Sect. IV-C].
- **Coefficients that encode the simulator.** See the one-galaxy formula above
  (arXiv:2602.07651) [src: Sect. III.1].

## Reading list
<!-- key: reading-list -->

- Method: Zorrilla Matilla et al. 2020, arXiv:2007.06529 — saliency families, the randomisation
  test, attribution binned in κ.
- Method: Ocampo & Cañas-Herrera 2026, arXiv:2604.05290 — Partition SHAP on HEALPix maps with
  mask and null-class controls.
- Foundation: Cranmer et al. 2020, arXiv:2006.11287 — distillation of GNN messages, complexity
  weights, the loss-per-complexity score, out-of-distribution test.
- Code: Cranmer 2023, arXiv:2305.01582 — PySR algorithm, adaptive parsimony, defaults.
- Method: Bartlett et al. 2022, arXiv:2211.11461 — exhaustive search and the MDL criterion.
- Application: Bartlett et al. 2023, arXiv:2311.15865 — residual target, Operon settings,
  selection on a noiseless target.
- Application: Vokrouhlicky et al. 2026, arXiv:2606.07745 — accuracy target from survey noise,
  post-processing, domain of validity.
- Critique: Liao et al. 2026, arXiv:2602.07651 — a symbolic form that transfers across CAMELS
  suites only with refitted coefficients.

## Not verified
<!-- key: not-verified -->

- The saliency sanity-check paper that arXiv:2007.06529 follows (its ref. [55]) and the Partition
  SHAP paper (Lundberg et al. 2020): not read.
- Recent symbolic-regression papers found by the date-sorted search (a symbolic model of the
  non-linear ΛCDM P(k) named SPINE; Sym-EFT for EFTofLSS; two halo-profile regressions from weak
  lensing): seen by title only, no statement made, not added to the sources.
- The R² and RMS values per suite of the one-galaxy formula are in its Fig. 2 and were not read.
- The ESR language-model prior (Bartlett et al. 2023b, cited by arXiv:2311.15865): not read.
