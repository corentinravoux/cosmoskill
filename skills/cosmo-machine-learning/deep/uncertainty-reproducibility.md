# Uncertainty quantification and reproducibility — cosmo-machine-learning dossier

Scope: how a network that predicts a value or a class is given an uncertainty (heteroscedastic
likelihood loss, MC dropout, variational Bayesian layers, deep ensembles, conformal prediction),
how that uncertainty is calibrated during or after training and tested by coverage or
reliability, and how seed, architecture and split variance is measured and reported; and how to
choose between these routes and between seed, architecture and pruned ensembles.
Snapshot: 2026-10-19.
From: Huertas-Company & Lanusse 2022 review (arXiv:2210.01813), Sect. 7.3.2; Dvorkin et al. 2022
Snowmass white paper (arXiv:2203.08056), Sects. 7 and 10.

Already in L2, not repeated here: overconfidence of neural density estimators, ensembles and
balanced NRE as remedies, and the coverage tests run by KiDS-SBI and DES Y3
(`systematics.md#overconfident-posteriors-and-training-set-size`); release practice, blinding
protocols and the KiDS-1000 benchmark networks (`systematics.md#reproducibility-practice`); the
HSC Y1 architecture scan (`results.md#neural-summaries-and-field-level-networks`). Coverage, TARP
and SBC for simulation-based inference are in `cosmo-beyond-two-point/deep/simulation-based-inference.md`
and `cosmo-statistics-inference`; propagation of an emulator's validation error into a Gaussian
likelihood, Ψ = (C + Σ)⁻¹, is in `deep/emulators.md`; calibrated photo-z PDFs are in
`cosmo-photometry-photoz/deep/machine-learning-photoz.md`.

Symbols. x: input (map, light curve, spectrum); y: target (parameter or class); ω: network
weights; μ(x), σ²(x): predicted mean and variance; M: ensemble size; p̄: ensemble-mean class
probabilities; H: entropy; MI: mutual information between label and weights; α: miscoverage
level of a conformal procedure; ECE: expected calibration error.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Decide which uncertainty the network must carry
<!-- key: step-1-decide-which-uncertainty-the-network -->

Two kinds are separated in every paper read. Aleatoric uncertainty is the noise in the input,
which more training data does not remove; epistemic uncertainty comes from limited training data
and shrinks where training examples are dense (arXiv:1911.08508) [src: Sect. III]. A
heteroscedastic output layer captures the first; a distribution over weights (Bayesian layers,
dropout) or an ensemble captures the second (arXiv:1708.08843) [src: Sects. II.1–II.3]. A network
that regresses parameters with these uncertainties returns intervals whose coverage is measured
over the test-set distribution of parameters, which plays the role of the prior [der: the
coverage tests below average over test sets drawn from the training ranges]. For a posterior
with an explicit prior, the neural density estimators of `physics-and-methods.md#neural-posterior-likelihood-and-ratio-estimation`
are the route.

### Step 2. Give the output a likelihood (aleatoric part)
<!-- key: step-2-give-the-output-a-likelihood-aleatoric -->

The network outputs μ(x) and σ²(x) and is trained on the Gaussian negative log-likelihood
−log p(y ∣ x) = ½ log σ²(x) + (y − μ(x))²/(2σ²(x)) + const (arXiv:1612.01474, Eq. 1); the
variance passes through a softplus with a floor of order 10⁻⁶ [src: Sect. 2.2.1, footnote].
No labels for σ are needed: the log σ² term penalises large values and the squared term small
ones (arXiv:1708.08843) [src: Sect. II.2, Eq. 6]. For several parameters the loss is
½ log|Σ| + ½ (y − μ)ᵀ Σ⁻¹ (y − μ), Σ a predicted covariance (arXiv:1911.08508, Eq. 19).

MSE training gives no uncertainty. An ensemble of five MSE networks whose spread is used as the
error "consistently underestimates the true uncertainty": its 80% interval held 20% of test
points on the Year Prediction MSD benchmark, while NLL-trained networks were calibrated
(arXiv:1612.01474) [src: App. A.2]. In cosmology the Gaussian NLL loss is also "hard to train"
as a compression loss (L2, `physics-and-methods.md#neural-compression-and-field-level-networks`).

### Step 3. Add weight uncertainty (epistemic part)
<!-- key: step-3-add-weight-uncertainty-epistemic-part -->

| Method | What is sampled | Training objective | Settings read | Place read |
|---|---|---|---|---|
| MC dropout | Bernoulli masks on the weight rows; same mask at every time step for an RNN | likelihood plus L2 weight decay (the KL term to a Gaussian prior approximated as L2) | SuperNNova: 50 forward passes per light curve, median reported; dropout 0.01, weight decay 10⁻⁷ chosen from p ∈ {0.01, 0.05, 0.1, 0.2} | arXiv:1901.06384, Sect. 4.2 |
| MC dropout + heteroscedastic output | dropout masks, then a Gaussian draw of variance σ_k² added to each sample | Eq. 5 with the Gaussian likelihood of Eq. 6 | strong-lens parameters: dropout keep rate tuned to 97% | arXiv:1708.08843, Sects. II.1–II.3, III.1 |
| Bayes by backprop | each weight w = μ + σ ε, ε ~ N(0, 1) | KL(q ∥ P)/n_B − E_q[log P(D_j ∣ w)] per mini-batch (Eq. 7), prior a two-Gaussian mixture | π = 0.75; log σ1, log σ2 = −1, −7 (recurrent layer) and −0.5, −0.1 (output layer); no cyclic learning rate | arXiv:1901.06384, Sect. 4.3 |
| Reparameterisation trick, Flipout | Gaussian weight posteriors (mean-field) | KL to a N(0, 1) prior; posterior variance initialised at N(−9, 0.01) before softplus | regulariser on the posterior scale tuned per architecture | arXiv:1911.08508, Sect. VI "Training", VIII.2 |
| Deep ensemble | M independently initialised networks on the full training set, data reshuffled | proper scoring rule per member (NLL); optional adversarial training with ε = 1% of the input range | M = 5 recommended; bagging "deteriorated performance" because each member sees only 63% unique points | arXiv:1612.01474, Sect. 2.4, Algorithm 1 |

Combining the ensemble: p(y ∣ x) = M⁻¹ Σ_m p_θm(y ∣ x), i.e. averaged class probabilities, or a
Gaussian mixture approximated by μ* = M⁻¹ Σ_m μ_m and σ*² = M⁻¹ Σ_m (σ_m² + μ_m²) − μ*²
(arXiv:1612.01474) [src: Sect. 2.4]. For classes, the entropy of p̄ splits into a mean member
entropy (aleatoric) and the mutual information MI(y; θ ∣ x) (epistemic, member disagreement)
(arXiv:2607.08044, Eq. 4).

### Step 4. Test calibration on held-out data
<!-- key: step-4-test-calibration-on-held-out-data -->

- **Regression coverage.** For each test input, take the interval holding 68.3, 95.5 and 99.7%
  of the predicted distribution and count how often the true value falls inside it
  (arXiv:1708.08843) [src: Sect. III.1]; the same with 1σ, 2σ, 3σ in arXiv:1911.08508
  [src: Table 5]. Repeat in batches of fixed noise level to check that σ follows the noise:
  for the Einstein radius 74.7, 96.8, 99.5% at peak S/N 100 per pixel and 71.0, 95.9, 99.4% at
  S/N 10 (arXiv:1708.08843) [src: Sect. III.1].
- **Classifier reliability.** Bin the predicted probability into ten (SuperNNova) or fifteen
  (Guo et al.) equal bins and plot the true-class fraction against the mean probability
  (arXiv:1901.06384, Sect. 5.1; arXiv:1706.04599, Sect. 2). The scalar summary is
  ECE = Σ_m (|B_m|/n) |acc(B_m) − conf(B_m)|, B_m the bins and n the sample size
  (arXiv:1706.04599, Eq. 3). For Bayesian networks, build the diagram from all samples per
  object, not the median: SuperNNova finds it better calibrated that way and reads it as
  evidence of meaningful predictive uncertainty [src: arXiv:1901.06384, Sect. 5.1].
- **Epistemic behaviour.** The epistemic part should shrink with more training data:
  SuperNNova trains on 43% and on the whole set and checks that the mean uncertainty and the
  entropy decrease (Δ⟨σ̂⟩ = 0.005 and 0.007; ΔH > 0.01) (arXiv:1901.06384) [src: Sect. 4.4.2]. It
  should rise on inputs unlike the training set: on MNIST with NotMNIST letters the entropy of
  a deep ensemble rose faster with M than that of MC dropout, which kept confident predictions
  for some unseen inputs (arXiv:1612.01474) [src: Sect. 3.5]; on light curves the entropy gap
  for synthetic OOD inputs had mixed signs (arXiv:1901.06384) [src: Sect. 5.3].

### Step 5. Recalibrate where the test fails
<!-- key: step-5-recalibrate-where-the-test-fails -->

- **Through a training hyperparameter.** The dropout rate (keep rate 97% in arXiv:1708.08843
  [src: Sect. III.1]; lower keep rates overestimated the errors, 99% was "mildly permissive") or
  the regulariser on the variational scale: Flipout coverage at 1σ moved from 63.3% unregularised
  to 68.2% at Reg = 6 × 10⁻⁶ and 89.6% at 10⁻⁴ (arXiv:1911.08508) [src: Table 5]. This failed on
  the VGG architecture, which stayed overconfident (arXiv:1911.08508) [src: Sects. VII, VIII.2].
- **After training, on a validation set.** Temperature scaling divides the logits by one scalar
  T > 0 fitted by NLL on the validation set; it leaves the predicted class unchanged
  (arXiv:1706.04599) [src: Sect. 4.2, Eq. 9]. For regression the analogue is Σ → sΣ, s > 0, or
  Σ → LΣLᵀ with L lower triangular; beta calibration fits β(x; a, b, c) = 1/(1 + (e^c
  x^a/(1 − x)^b)⁻¹) to the reliability curve (arXiv:1911.08508) [src: Eq. 20, Sect. VIII.5].
  The CMB study argues that temperature scaling acts on the aleatoric part only, and refits the
  last layer instead; all variants still gave 77–80% at 1σ against 68.3% nominal
  [src: Sect. VIII.5, Table 8].
- **Distribution-free, after training: conformal prediction.** With a calibration set of n pairs
  and a nonconformity score s, the p-value of a new point is (number of calibration scores
  ≥ s(x*) + 1)/(n + 1); Mondrian conformal prediction applies it within each predicted class
  (arXiv:2607.08044) [src: Sect. VI.1, Eqs. 1–2]. Adaptive prediction sets keep every class with
  p(y ∣ x*) ≥ 1 − q̂_α, q̂_α the finite-sample-corrected (1 − α) quantile of 1 − p on the
  calibration set [src: Sect. VI.2, Eq. 3]. The guarantee needs exchangeability between
  calibration and test data and is marginal; ASTRANet stratifies the calibration set by
  predicted class and anomaly-score quintile (Eq. 6) to get conditional coverage, with a
  fallback to the class threshold for cells under n_min = 10 [src: Sect. VI.8].

### Step 6. Measure and report seed, architecture and split variance
<!-- key: step-6-measure-and-report-seed-architecture-and -->

| Analysis | What is varied | How the spread is reported | Place read |
|---|---|---|---|
| QuasarNET | ten random 80/20 splits, validation spectra of training targets removed | rms over splits on purity and completeness (± 0.03%) | arXiv:1808.09955, Sects. 3, 4.1 |
| SuperNNova | five randomised train/validation/test splits | mean ± spread of accuracy and calibration dispersion | arXiv:1901.06384, Sects. 3.3, 5.1 |
| ZTF noisification | five random train–test seeds | confusion matrices with standard deviations | arXiv:2602.13036, Sect. 5.2 |
| CNN ensemble on PM fields | grid of 20 architectures (1–5 blocks, 1–2 layers per block, 5 or 10 first-block channels), each tuned by 25 optuna trials | posterior volume V_p = √det C_θ against the number of networks and the pruning rule | arXiv:2610.19891, Sects. 2.4, 3.1, 3.2, Eq. 4 |
| ASTRANet | six checkpoints: three seeds × two architecture revisions; eight ensembling strategies compared | averaging within seed then across seeds beat a flat super-ensemble and a cross-seed-only average | arXiv:2607.08044, Sect. IV.2 |

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Heteroscedastic output, Bayesian layers or an ensemble
<!-- key: heteroscedastic-output-bayesian-layers-or-an -->

| Route | Buys | Costs | Found on the same data |
|---|---|---|---|
| Heteroscedastic NLL only | aleatoric σ(x) at no extra cost; follows the input noise | no epistemic part; Gaussian form unless a mixture is used | — |
| MC dropout | epistemic part from an ordinary network; 50 passes at inference | dropout rate must be tuned for calibration; confident on some OOD inputs | uncertainties twice those of Bayes by backprop on the same light curves; calibration dispersion 0.004 ± 0.002 against 0.0005 ± 0.0004 [src: arXiv:1901.06384, Sects. 4.4.2, 5.1] |
| Bayes by backprop, Flipout | explicit weight posteriors; best calibrated in both studies read | prior and scale hyperparameters; slower training; architecture-dependent calibration | Flipout beat dropout, DropConnect and the reparameterisation trick on CMB maps for both architectures [src: arXiv:1911.08508, abstract, Sect. VIII.2] |
| Deep ensemble | no change to training; parallel; uncertainty rises off the training set faster than MC dropout | M trainings; members must be NLL-trained to be calibrated | entropy on unseen classes rose faster than MC dropout's [src: arXiv:1612.01474, Sect. 3.5] |

Accuracy is barely affected: SuperNNova's Bayesian variants reach 96.87 ± 0.09% (MC dropout) and
96.85 ± 0.05% (Bayes by backprop) without redshift against a baseline efficiency and purity
higher by ≤ 0.5% (arXiv:1901.06384) [src: Sects. 4.2, 4.3]. The CMB Bayesian networks were
"orders of magnitude faster" than MCMC but "less accurate", and their output can seed the MCMC
proposal to raise the acceptance rate (arXiv:1911.08508) [src: abstract].

### Calibrate in training, after training, or conformally
<!-- key: calibrate-in-training-after-training-or -->

In-training calibration ties the uncertainty to a hyperparameter search and failed for one of two
architectures (arXiv:1911.08508) [src: Sect. VII]. Post-hoc scaling preserves accuracy and on
image benchmarks the one-parameter temperature beat vector and matrix scaling, since the
miscalibration is "intrinsically low dimensional"; matrix scaling overfits with many classes
(arXiv:1706.04599) [src: Sect. 5]. Uncalibrated ECE was typically 4–10% across convolutional,
recurrent and averaging networks, and grows with depth and width because NLL keeps falling by
raising confidence once the training set is fitted [src: Sects. 3, 5]. Conformal prediction gives
a finite-sample guarantee: at α = 0.05 marginal coverage 0.949 and Mondrian 0.940 against 0.950,
within ± 0.5 n_ho^(−1/2) ≈ ± 0.012 for n_ho = 1670 held-out spectra (arXiv:2607.08044)
[src: Sect. VI.1, Table 4]. Its cost: the guarantee is marginal. Per-class coverage at
α = 0.025 dropped to 0.787 (TDE, 42 calibration spectra) and 0.917 (CV, 60), and plain Mondrian
coverage was 0.824 in the highest anomaly-score quintile against 0.95 nominal; the stratified
version gives 0.952 ± 0.001 in every quintile but with about 47 calibration points per cell
instead of 233 [src: Sects. VI.1, VI.8, Table 9].

### Seed, architecture or pruned ensemble
<!-- key: seed-architecture-or-pruned-ensemble -->

Random initialisation with reshuffling suffices to diversify an ensemble and bagging hurts deep
networks (arXiv:1612.01474) [src: Sect. 2.4]. For neural summaries trained on cheap simulations
and applied to costly ones, members must be informative and complementary on the target
simulations: ranking CNNs by test MSE on the low-resolution set picks a first network whose
posterior volume is ~3 times that of the power spectrum; a greedy search on V_p plateaus at about
15 of 19 networks, MSE ranking converges more slowly, and ranking by individual V_p needs the
whole ensemble (arXiv:2610.19891) [src: Sect. 5.2]. Concatenating member outputs beat averaging
them [src: Sect. 3.1]. One of the 20 networks was removed because its outputs failed the
Gaussian-likelihood test [src: Sect. 4.2]. Convergence is declared when V_p/V_p^PS is within 3%
of its minimum, chosen above the ~1% posterior sampling noise [src: Sect. 5.2].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Ensemble size, adversarial step | M = 5; ε = 1% of input range | deep ensembles | arXiv:1612.01474 | Algorithm 1 |
| MSE-ensemble interval coverage | 80% nominal → 20% observed | deep ensembles, MSD data | arXiv:1612.01474 | App. A.2 |
| ECE bins; typical ECE | 15; 4–10% | calibration benchmark | arXiv:1706.04599 | Sect. 5 |
| Dropout keep rate for calibration | 97% | strong-lens CNN | arXiv:1708.08843 | Sect. III.1 |
| MC-dropout passes | 50 | SuperNNova | arXiv:1901.06384 | Sect. 4.2 |
| Calibration dispersion | RF 0.025; RNN 0.006; MC dropout 0.004; BBB 0.0005 | SuperNNova | arXiv:1901.06384 | Sect. 5.1 |
| Flipout 1σ coverage vs regulariser | 63.3% (none), 68.2% (6 × 10⁻⁶), 89.6% (10⁻⁴) | CMB BNN | arXiv:1911.08508 | Table 5 |
| Post-hoc 1σ coverage | 77.2–80.0% for six last-layer and temperature variants | CMB BNN | arXiv:1911.08508 | Table 8 |
| Conformal coverage at α = 0.05 | 0.949 marginal, 0.940 Mondrian | ASTRANet | arXiv:2607.08044 | Table 4 |
| Calibration / held-out split | 1669 / 1670 spectra | ASTRANet | arXiv:2607.08044 | Sect. VI "Calibration setup" |
| Stratified cell floor | n_min = 10 | ASTRANet | arXiv:2607.08044 | Sect. VI.8 |
| Architecture grid | 20 CNNs, 25 optuna trials each, early stopping 25 epochs | CNN ensemble on PM fields | arXiv:2610.19891 | Sects. 2.4, 3.1 |
| Ensemble convergence | within 3% of minimum V_p/V_p^PS; ~15 networks by greedy search | CNN ensemble on PM fields | arXiv:2610.19891 | Sect. 5.2 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Spread of MSE networks read as an error bar.** Undercovers badly (20% in an 80% interval);
  train members on a proper scoring rule (arXiv:1612.01474) [src: App. A.2].
- **Calibration hyperparameter tuned on the test set.** The dropout rate, the variational
  regulariser and the temperature are fitted on a validation set; the coverage must then be
  measured on a further held-out set. ASTRANet splits its validation pool into calibration and
  exchangeability-test halves and computes the scores out of fold "to avoid leakage of training
  information into calibration" (arXiv:2607.08044) [src: Sect. VI "Calibration setup"]; L2
  records the same advice for SBI diagnostics (`systematics.md#overconfident-posteriors-and-training-set-size`).
- **Calibration that holds only for one architecture.** VGG stayed overconfident when AlexNet
  could be calibrated (arXiv:1911.08508) [src: Sect. VIII.2]. Test: report coverage per
  architecture.
- **Marginal coverage hiding conditional failure.** Coverage averaged over the test set can be
  right while failing for rare classes or atypical inputs (0.787 for a class with 42 calibration
  points; 0.824 in the top anomaly quintile) (arXiv:2607.08044) [src: Sects. VI.1, VI.8]. Test:
  coverage per class, per noise level (arXiv:1708.08843, Sect. III.1) and per anomaly-score bin.
- **Exchangeability broken.** Conformal guarantees and post-hoc temperatures transfer only if the
  data resemble the calibration set; a survey that departs from the simulations (L2,
  `systematics.md#simulator-dependence`) voids them [der].
- **Confident on unseen inputs.** MC dropout gave near-zero entropy for some unseen classes
  (arXiv:1612.01474) [src: Sect. 3.5]; RNNs can collapse onto one class
  (arXiv:1901.06384) [src: Sect. 5.3]. Test: OOD inputs and an explicit anomaly score.
- **Best single network chosen on the wrong set.** The network with the lowest MSE on cheap
  simulations was the least informative on the target simulations (arXiv:2610.19891)
  [src: Sect. 5.2]. Select on the target domain, or report an ensemble.
- **Uncertainty on calibration ignored.** SuperNNova's calibration dispersion changed by up to
  50% with the training-set fraction and nature (arXiv:1901.06384) [src: Sect. 5.1]; ASTRANet's
  finite-sample band is ± 0.012 for 1670 points (arXiv:2607.08044) [src: Sect. VI.1].

## Reading list
<!-- key: reading-list -->

- Foundation: Gal & Ghahramani 2015, arXiv:1506.02142 — dropout as approximate Bayesian inference.
- Foundation: Lakshminarayanan et al. 2016, arXiv:1612.01474 — deep ensembles, NLL loss, mixture
  combination, why bagging and MSE ensembles fail.
- Foundation: Guo et al. 2017, arXiv:1706.04599 — ECE, temperature scaling, why capacity
  miscalibrates.
- Method: Perreault Levasseur et al. 2017, arXiv:1708.08843 — aleatoric plus epistemic
  uncertainty for lens parameters and coverage tests by noise level.
- Method: Hortúa et al. 2019, arXiv:1911.08508 — Bayesian layers on CMB maps; in-training and
  post-hoc calibration; comparison with MCMC.
- Method: Möller & de Boissière, arXiv:1901.06384 — Bayesian RNNs, reliability diagrams,
  epistemic checks.
- Method: Sasli et al. 2026, arXiv:2607.08044 — conformal p-values, prediction sets, stratified
  Mondrian coverage.
- Application: Sáez-Casares et al. 2026, arXiv:2610.19891 — ensemble construction and pruning
  for neural summaries.

## Not verified
<!-- key: not-verified -->

- Concrete dropout, Fortunato et al. (Bayesian RNNs) and the beta-calibration paper, cited by
  arXiv:1911.08508 and arXiv:1901.06384: not read.
- The Gal & Ghahramani paper was read in its abstract only; the dropout-as-variational form
  above is as arXiv:1708.08843 and arXiv:1901.06384 restate it.
- No cosmology analysis was found that reports the seed-to-seed scatter of a published parameter
  constraint from retraining the same network; the DES and KiDS map analyses average several
  initialisations (L2) without quoting the scatter.
- The appendix of arXiv:2607.08044 comparing eight ensembling strategies (App. G): not read.
