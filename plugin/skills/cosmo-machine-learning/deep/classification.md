# Classification — cosmo-machine-learning dossier

Scope: how a classifier of light curves, spectra or images is trained and validated in practice
(input representation and normalisation, augmentation of a non-representative training set, class
balance and the loss that encodes it, splits that avoid leakage, training on partial light curves,
calibration, operating threshold, out-of-distribution behaviour), and how to choose between
feature-plus-trees, sequence networks, image networks and latent-space models, between flat and
hierarchical taxonomies, and between flat-weighted and redshift-weighted objectives.
Snapshot: 2026-10-19.
From: Huertas-Company & Lanusse 2022 review (arXiv:2210.01813), Sect. 3.1; Dvorkin et al. 2022
Snowmass white paper (arXiv:2203.08056), Sect. 2.2; PLAsTiCC and ELAsTiCC challenge papers.

Already in L2, not repeated here: the table of classifiers and their tasks
(`physics-and-methods.md#classification-of-transients-and-spectra`); the official PLAsTiCC
scores and the flat-weight 0.468 of arXiv:1907.04690 (abstract) (`results.md#challenge-outcomes-and-classifier-performance`);
SCONE out of distribution, Superphot+ on Rubin DP1, the ELAsTiCC-based w bias and the list of
mitigations (`systematics.md#non-representative-training-sets-for-classifiers`); challenge
organisation (`surveys-and-data.md#time-domain-classification-challenges`). How class
probabilities enter an SN Ia Hubble diagram (BEAMS, contamination systematic, SCONE trained on
the bias-correction simulation) is in `cosmo-supernovae` (`deep/stage-iv-photometric-samples.md`);
template redshift fitting and visual inspection are in `cosmo-data-pipelines`.

Symbols. p(m ∣ d_n): probability that object n with data d_n belongs to class m; N_m: number of
objects of class m; w_m: class weight of a metric or loss; TPR = TP/(TP + FN), FPR = FP/(FP + TN),
purity = TP/(TP + FP), completeness = recall = TPR (arXiv:1907.04690, Eqs. 5–8); AUC: area under
the ROC curve (TPR against FPR); F1: harmonic mean of precision and recall.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Choose the input representation and normalise it
<!-- key: step-1-choose-the-input-representation-and -->

Four representations are in use, each with its preprocessing read in the bodies.

- **Engineered features, then trees.** Avocado fits a two-dimensional Gaussian process (GP) in
  time and wavelength to all bands at once, extracts features from the GP model, and trains a
  LightGBM boosted-tree classifier; the most important features were the host photometric
  redshift, the peak brightness and the colours at maximum (arXiv:1907.04690) [src: Sect. III.6,
  Fig. 5]. In PLAsTiCC LightGBM was common to most solutions; features came from SALT2 or Bazin
  template fits or from the "more time-consuming but less model-dependent" GP fits
  (arXiv:2012.12392) [src: Sect. 3.1].
- **Raw photometric sequence, recurrent network.** SuperNNova groups observations within eight
  hours into one time step, gives a special value to unobserved filters, and feeds fluxes and
  errors in g, r, i, z, the time since the previous step and a one-hot code of which filters are
  present; host redshift and its error, when used, are repeated at every step
  (arXiv:1901.06384) [src: Sect. 2.4, "RNN training details", "RNN training data"]. Fluxes f are
  log-transformed, f_l = log(−min(f) + f + ε), then standardised, either globally or per filter
  [src: same]. ORACLE pads sequences to 500 steps with a masking layer, marks missing static
  features with −9, divides FLUXCAL and its error by 1000, rescales MJD to
  (MJD − min MJD)/100, encodes each band by its mean wavelength, and concatenates 25 host and
  field features (redshifts, host magnitudes, separation, Milky Way extinction, field flags)
  (arXiv:2501.01496) [src: Sect. IV, Table 1, Sect. V].
- **GP heatmap, image network.** SCONE evaluates a 2D GP (Matérn-3/2 kernel, fixed 6000 Å length
  scale in wavelength, fitted in time) on a grid t_peak − 50 ≤ t ≤ t_peak + 130 days in 1-day
  steps and 3000 < λ < 10 100 Å in 221.875 Å steps, stacks the GP mean and its uncertainty as two
  channels and divides by the maximum flux (arXiv:2106.04370) [src: Sect. II.4]. The network has
  22 441 (binary) or 22 606 (six-class) trainable parameters: four convolutional blocks whose
  kernels span the full wavelength axis, 2 × 2 max pooling, 50% and 30% dropout, a 32-unit dense
  layer [src: Sect. II.6].
- **Learned latent space, then trees.** The ZTF classifier of Townsend et al. encodes each light
  curve with the ParSNIP variational autoencoder into three intrinsic latent parameters plus
  reference time, amplitude and colour, whose "physics layer" makes the representation
  invariant to redshift; LightGBM then classifies on these, their uncertainties and detection
  counts (arXiv:2602.13036) [src: Sect. 4.2].

For spectra, QuasarNET downsamples BOSS spectra from about 4400 to 443 log-wavelength pixels
between 360 nm and 1 μm and subtracts the inverse-variance-weighted mean and divides by the
weighted rms, because large input variations (the quasar luminosity function) slow learning
(arXiv:1808.09955) [src: Sect. 3]. Each emission line has a "line finder": 13 coarse sigmoid
units give the confidence that the line centre lies in each of 13 wavelength intervals, 13 more
give the offset within the interval, after the object-detection scheme of image recognition
[src: Sect. 3]. Seven finders cover Lyα, C IV, C III], Mg II, Hβ, Hα and a C IV BAL feature,
chosen so that at least two lines are visible in BOSS for 0 < z < 5.45 [src: Sect. 3].

### Step 2. Augment a training set that does not represent the target
<!-- key: step-2-augment-a-training-set-that-does-not -->

Spectroscopic training sets are biased to bright, low-redshift objects (L2). Two recipes were
read in full.

**Avocado (simulated PLAsTiCC test set)** [src: arXiv:1907.04690, Sect. III.4]:

1. Fit a GP to a training light curve as a template.
2. Choose a new redshift (extragalactic) or brightness (Galactic).
3. Evaluate the GP mean at the redshifted wavelengths; the 2D GP then contains the
   k-correction for smooth spectra; scale the flux by the change in distance modulus at a
   fiducial cosmology.
4. Drop observations (season gaps, degraded sampling) to match the test-set cadence.
5. Add noise representative of the test-set depth; the GP uncertainty is propagated as
   measurement error, not used as intrinsic variation.
6. Keep only light curves that would be detected.
7. Draw a photometric redshift from the test set's spectroscopic–photometric mapping.
8. Repeat: up to 100 versions per object, 591 410 light curves in total (arXiv:1907.04690,
   Sect. III.4).

The stated reason for not targeting the test-set rates (as the earlier propensity-score method
STACCATO did) in arXiv:1907.04690 is that SN rates above z = 1 are known only to about 50%; Avocado instead
simulates every object the same number of times over a range of redshifts and makes the
classifier independent of the training redshift distribution through the metric of Step 3
[src: Sect. III.4].

**ZTF noisification (real spectroscopic sample)** [src: arXiv:2602.13036, Sects. 2.2.1, 3.3,
4.1]: train on the brightest 90% of each class (BrightZTF) and test on the faintest 10%
(FaintZTF). Draw z_sim in [z_true, z_true + 0.1] with probability ∝ z^z_scale (z_scale = 0 flat,
or 2 for a constant volumetric rate, dV ∝ z² dz); scale the flux and the flux error, add Gaussian
noise on top of the original noise ("conservative", since the original noise cannot be removed),
k-correct; keep curves with a peak above S/N 5 and at least five S/N > 5 detections; then thin
dense sampling (cadence_scale) or subsample randomly (subsampling_rate). The split into training
and test is made before augmentation "to ensure that no copies of the same object appear in both
sets" [src: Sect. 4.1].

### Step 3. Encode class balance in the sampling or in the loss
<!-- key: step-3-encode-class-balance-in-the-sampling-or -->

| Analysis | Mechanism | Stated reason | Place read |
|---|---|---|---|
| PLAsTiCC metric | weighted log-loss L = −Σ_m w_m Σ_n τ_{n,m} ln p(m ∣ d_n), τ the true-class indicator, w_m = J/N_m with J = 2 for rare classes (μ-lensing, TDE, kilonova, SLSN, "Other") and 1 otherwise | to stop entrants classifying everything as the most populous class | arXiv:2012.12392, Sect. 2.3, Eq. 1, Table 1 |
| Avocado, flat-weighted | same with w_i = 1 for classes in the training set, 0 for unseen ones | each class counts equally; for a classifier optimal on it, p can be read as a probability in a class-balanced sample | arXiv:1907.04690, Sect. II.2.1, Eqs. 1–2 |
| Avocado, redshift-weighted | objects reweighted so every class has the same redshift distribution: 10 log bins in 0.1 < z < 3 plus one Galactic bin, floor of 100 objects per bin, Galactic weight ≈ 5 | otherwise the classifier learns the training-set redshift distribution of each class | arXiv:1907.04690, Sect. II.2.2, Eq. 3 |
| SCONE | subsample the majority class to the minority count (992 spectroscopic, 12 256 main-sample objects); 80/10/10 split per class | balanced sets make accuracy interpretable and give examples of each class | arXiv:2106.04370, Sect. II.3 |
| ORACLE | cap of 40 000 per class in training and 20 000 in testing; weighted hierarchical cross-entropy | performance against training time; class imbalance | arXiv:2501.01496, Sects. IV, VI |
| QuasarNET | the two binomial terms of the loss normalised separately by the number of full and empty wavelength bins | equal prefactors would bias the confidences to zero, since most bins hold no line | arXiv:1808.09955, Sect. 3, Eq. 1 |
| ZTF noisification | augmentation count per class: balanced, unbalanced or hybrid (10 copies per SN Ia, other classes matched to twice the original SN Ia number) | hybrid gave the best mean SN Ia recall, balanced next; unbalanced the best recall of the other classes | arXiv:2602.13036, Sects. 4.1, 5.1, Table 3 |

The hierarchical loss of ORACLE (weighted hierarchical cross-entropy, WHXE, of Villar et al.
2023, cited there) is, for a class C at height h(C) of the taxonomy tree [src: arXiv:2501.01496,
Eqs. 2–7]:

- p(C) = Π_{l=0}^{h(C)−1} p(C^(l) ∣ C^(l+1)), the conditional probabilities obtained by summing
  leaf probabilities under each node (Eqs. 2–3);
- λ(C^(l)) = exp(−α d(C)), d the depth of the node; α = 0 weighs all levels equally, α > 0
  favours the top of the tree (Eq. 4); ORACLE uses α = 0.5 (arXiv:2501.01496) [src: Table 4];
- W(C^(l)) = N/(N_nodes N_c), N the number of events, N_nodes the number of classes, N_c the
  count of class C (Eq. 6);
- L_WHXE = −Σ_l W(C^(l)) λ(C^(l)) log p(C^(l) ∣ C^(l+1)) (Eq. 7).

### Step 4. Split without leakage and tune
<!-- key: step-4-split-without-leakage-and-tune -->

- Avocado: five-fold cross-validation on the augmented set, folds stratified by class, with
  "all light curves generated from the same original light curve" kept in one fold; test
  predictions average the five classifiers; hyperparameters scanned one at a time on the
  flat-weighted metric (Table 4: max_depth 7, num_leaves 50, min_child_weight 2000,
  colsample_bytree 0.05, early stopping 50 rounds) (arXiv:1907.04690) [src: Sect. III.6].
- ZTF noisification: LightGBM defaults, 10-fold cross-validation, min_child_weight = 100 "to
  prevent any overfitting to the augmented light curves"; results averaged over five random
  train–test splits (arXiv:2602.13036) [src: Sects. 4.2, 5.2].
- QuasarNET: ten random 80/20 training/validation splits, with spectra of targets present in the
  training sample excluded from the validation sample (BOSS has repeat spectra: 491 797 spectra
  of 449 013 objects); quoted uncertainties are the rms over the splits; Adam with AMSGrad,
  mini-batches of 256, 100 epochs (arXiv:1808.09955) [src: Sects. 2, 3, 4.1].
- SuperNNova: uncertainties from five randomised training/validation/test splits
  (arXiv:1901.06384) [src: Sect. 3.3].
- ORACLE: no formal hyperparameter tuning; the epoch with the lowest mean loss on the augmented
  validation set is kept; 1000 epochs, batch 1024, learning rate 2 × 10⁻⁴ with exponential decay
  (0.9 per 10 000 steps) (arXiv:2501.01496) [src: Sect. VII, Table 4].

### Step 5. Train for partial light curves
<!-- key: step-5-train-for-partial-light-curves -->

Live alert streams need a class before the light curve is complete.

- SuperNNova trains on randomly truncated light curves, which it found "beneficial" for
  incomplete curves; it did not augment otherwise, because the training set was large and
  overfitting limited (arXiv:1901.06384) [src: Sect. 2.4]. On average about 5 observing nights
  give accuracies above 80%, or 2.4 ± 1.2 to 3.3 ± 1.4 epochs when only epochs within 14 days
  before peak are counted; accuracy is above 83% just before maximum, and host redshifts add up
  to 12 points [src: Sect. 3.5].
- ORACLE redraws at each epoch a fraction f ~ U(0.1, 1) of the observations (detections and
  non-detections) and truncates to it; the validation set holds each curve at 10, 40, 60 and
  100%, and the test set at d = 2ⁿ days after first detection, n = 0 … 10
  (arXiv:2501.01496) [src: Sect. IV]. Training and validation truncations differ on purpose, to
  score the model at phases earlier than it was trained on [src: same].

### Step 6. Set the operating point
<!-- key: step-6-set-the-operating-point -->

A probability becomes a sample through a threshold, chosen on the metric the science needs.

- QuasarNET: a spectrum is a quasar if at least ℓ_min lines exceed a confidence c_th, and the
  most confident line gives z; the nominal choice ℓ_min = 1, c_th = 0.4 is where purity and
  completeness are about equal (99.51 ± 0.03% and 99.52 ± 0.03%); two lines with c_th ≈ 0.1 give
  similar values; three lines at c_th = 0.6 give purity above 99.9% but completeness below 45%
  (arXiv:1808.09955) [src: Sect. 4.1]. For BALs c_th = 0.4 gives completeness 98.0 ± 0.4% and
  purity 77 ± 1%, chosen because Lyα BAO analyses prefer completeness [src: Sect. 4.2].
- Lens finding: participants were told to optimise AUROC, but lenses are about one object in a
  thousand while training and test sets are boosted to about half lenses; the contamination
  expected in a survey is FP/TP ≃ (FPR/TPR) × (N_non-lens/N_lens) (arXiv:1802.03609, Eq. 14).
  The challenge therefore adds TPR0, the highest TPR before the first false positive in 100 000
  candidates, and TPR10, the TPR at fewer than ten false positives, which at a lens fraction of
  10⁻³ is about 10% contamination [src: Sect. 5.1].
- Avocado reports SN Ia completeness as a function of redshift at a fixed 95% purity
  (arXiv:1907.04690) [src: Sect. IV.2].

### Step 7. Measure calibration and out-of-distribution behaviour
<!-- key: step-7-measure-calibration-and-out-of -->

- **Reliability diagram.** Predicted probabilities in ten equal bins against the fraction of true
  members in each bin; SuperNNova's "calibration dispersion" is the squared difference between
  the two curves (arXiv:1901.06384) [src: Sect. 5.1]. For the binary task without redshift:
  random forest 0.025 ± 0.002, baseline RNN 0.006 ± 0.001, MC-dropout RNN 0.004 ± 0.002,
  Bayes-by-backprop RNN 0.0005 ± 0.0004; changing the training-set size or nature changed the
  dispersion by up to 50% [src: Sect. 5.1]. Thresholded samples inherit any miscalibration;
  the remedies named are post-processing recalibration or per-bin reweighting [src: same].
- **Synthetic out-of-distribution inputs.** SuperNNova (arXiv:1901.06384) feeds time-reversed, shuffled,
  random-flux and sinusoidal curves at the survey cadence; these are rarely called SNe Ia
  (≤ 4.8% binary for reversed curves with MC dropout, < 3% with Bayes by backprop), mostly
  core-collapse types [src: Sect. 5.3, Fig. 9]. The entropy gap between OOD and normal test
  sets was positive for some OOD types and negative for others, which the authors trace to RNNs
  collapsing onto one class with high probability [src: Sect. 5.3].

The method of the Bayesian networks themselves (MC dropout, Bayes by backprop) is in
`deep/uncertainty-reproducibility.md`.

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Features plus trees, sequence network, heatmap CNN or latent space
<!-- key: features-plus-trees-sequence-network-heatmap -->

| Variant | Assumes | Buys | Costs | Comparison on the same data |
|---|---|---|---|---|
| GP features + boosted trees (Avocado) | a smooth light curve the GP can model | redshift augmentation with k-corrections from the 2D GP; feature importances | features must be designed; GP fit per object | best PLAsTiCC flat-weighted score, 0.468 against 0.481 for the next model [src: arXiv:1907.04690, Sect. IV.3] |
| Raw sequence RNN (SuperNNova, ORACLE) | none on the light-curve shape | no feature engineering; partial curves natively; improves with training-set size | needs large training sets | SALT2-fitted set: RNN 96.3 ± 0.4%, AUC 0.995; random forest 95.15 ± 0.07%, AUC 0.9929; 1D CNN 94.53 ± 0.07%, AUC 0.9887; the forest stays flat with more data while the RNN improves [src: arXiv:1901.06384, Sect. 3.3, Fig. 3] |
| GP heatmap CNN (SCONE) | GP interpolation across bands | filter-set independent; 22 k parameters | GP fit per object; full curve needed in the published set-up | heatmaps from 32 × 180 down to 4 × 10 pixels lose at most 2.67% test accuracy [src: arXiv:2106.04370, Sect. III.1.1] |
| VAE latent + trees (ParSNIP features) | an intrinsic-spectrum model with explicit redshift and amplitude | redshift-invariant features; physical latent axes | an autoencoder to train first | SN Ia recall on faint ZTF 90% → 95% (real) and 86% → 96% (noise-augmented test) when the training set is augmented [src: arXiv:2602.13036, Sect. 5.2] |

Why the random forest does not need redshift to use it: SALT2-fit features carry the redshift
implicitly (arXiv:1901.06384) [src: Sect. 3.3.2]; Avocado makes the same point for any light-curve
feature (colours, time dilation), so withholding redshift does not stop a classifier from
learning the training redshift distribution [src: arXiv:1907.04690, Sect. II.2.2]. ORACLE quotes
interpretability as the argument for trees and accuracy for deep networks without settling it
[src: arXiv:2501.01496, Sect. V].

### Flat-weighted or redshift-weighted objective
<!-- key: flat-weighted-or-redshift-weighted-objective -->

At fixed 95% purity on the PLAsTiCC WFD sample, the flat-weighted classifier peaks at 80% SN Ia
completeness at z = 0.8, where about 70% of objects are SNe Ia, and falls below 40% nearby,
because only 0.6% of the SNe Ia in the sample (the paper points to its Fig. 2) lie at z < 0.1; the redshift-weighted classifier keeps about
70% at low redshift and declines smoothly with S/N, and in the DDF stays above 80% at most
redshifts up to z = 1.55 (arXiv:1907.04690) [src: Sect. IV.2, Fig. 7]. When SNe Ia are dropped
from the training set with p(z) = exp(−z) or min(exp(z) − 1, 1), the flat-weighted completeness
changes by more than a factor of two at low and high redshift; the redshift-weighted one barely
moves [src: Sect. IV.2, Fig. 8]. The cost: global scores are similar (0.500 on the redshift-weighted
metric against 0.609 for the next model), but the probabilities then refer to an arbitrary common
redshift distribution, not to the survey's class fractions [src: Sects. IV.2, IV.3]. All other
PLAsTiCC entries were trained on the Kaggle metric and showed the flat-weighted behaviour
[src: Sect. IV.3].

### Flat or hierarchical taxonomy
<!-- key: flat-or-hierarchical-taxonomy -->

A hierarchical model returns every level of the tree in one inference step and "can replace a
whole family of classifiers" (arXiv:2501.01496) [src: Sect. VIII.2]. With α = 0.5 it learns the
top of the tree first, which the authors give as the reason for slightly worse early bottom-level
performance than the flat ATAT classifier: bottom-level macro F1 0.60 at trigger + 2 days against
≈ 0.65 read off an ATAT figure; at 1024 days 0.84 against 83.5 ± 0.6 (as printed) [src:
Sect. VIII.2, Table 8]. The comparison table mixes 19-, 20-, 12-, 6- and 5-way tasks on ELAsTiCC,
ZTF and PLAsTiCC, and the authors state that one-to-one comparison "is not possible" [src: Table 8].

### Augmentation strength
<!-- key: augmentation-strength -->

Class scaling mattered most in the ZTF study; removing points helped the other classes' recall
and hurt SN Ia recall; jittering observation times by as little as 0.1 day degraded SN Ia
precision, because relative band shifts change the inferred colours and raise confusion with
SNe Ib/c (arXiv:2602.13036) [src: Sect. 5.1]. In PLAsTiCC the second-placed team dropped 30% of
measurements and adjusted redshifts and fluxes, but added augmentation late and did not retrain
fully on it (arXiv:2012.12392) [src: Sect. 3.3].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Augmented training set | ≤ 100 versions per object; 591 410 curves | Avocado | arXiv:1907.04690 | Sect. III.4 |
| Redshift-weight bins | 10 log bins 0.1–3 + 1 Galactic; floor 100 per bin | Avocado | arXiv:1907.04690 | Sect. II.2.2 |
| PLAsTiCC class weights | J = 2 for rare classes and "Other", 1 otherwise; w_m = J/N_m | PLAsTiCC | arXiv:2012.12392 | Sect. 2.3, Table 1 |
| Heatmap grid | 32 λ × 180 t bins, 2 channels | SCONE | arXiv:2106.04370 | Sects. II.4, II.6 |
| Optimiser, schedule | Adam 10⁻³, 400 epochs, (sparse) binary cross-entropy | SCONE | arXiv:2106.04370 | Sect. II.6 |
| Phase augmentation | f ~ U(0.1, 1) per epoch; test at 2ⁿ days, n ≤ 10 | ORACLE | arXiv:2501.01496 | Sect. IV |
| Sample sizes | ~450 000 train, ~24 000 (×4) validation, ~225 000 (×11) test | ORACLE | arXiv:2501.01496 | Sect. IV |
| WHXE level weight | α = 0.5 | ORACLE | arXiv:2501.01496 | Table 4 |
| Line-finder grid | 13 intervals × 7 lines; 443 input pixels | QuasarNET | arXiv:1808.09955 | Sect. 3 |
| Quasar threshold | ℓ_min = 1, c_th = 0.4 | QuasarNET | arXiv:1808.09955 | Sect. 4.1 |
| Lens challenge sets | 20 000 training, 100 000 test candidates of 101 × 101 pixels; 48 h to submit | lens finding challenge | arXiv:1802.03609 | Sect. 2 |
| Best TPR0 | 0.22 (Manchester SVM, ground; CMU DeepLens ResNet, space) | lens finding challenge | arXiv:1802.03609 | Sect. 5.2, Table 4 |
| MC-dropout samples | 50 per light curve; dropout 0.01, weight decay 10⁻⁷ | SuperNNova | arXiv:1901.06384 | Sect. 4.2 |
| Faint-sample SN Ia recall | 98.1 ± 0.4% over five splits; > 96% to peak magnitude 20.5 | ZTF noisification | arXiv:2602.13036 | abstract |
| Augmentation counts | balanced 2–5, unbalanced 2–15, hybrid 10 per object | ZTF noisification | arXiv:2602.13036 | Table 3 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **The classifier learns the training redshift distribution.** Shows up as completeness that
  varies with redshift and with the training-set composition. Test: retrain after dropping
  members of one class with a redshift-dependent probability (the Avocado test above); if
  completeness at fixed purity moves, the classifier encodes the training priors
  (arXiv:1907.04690) [src: Sect. IV.2].
- **Leakage between folds.** Augmented copies or repeat spectra of one object in both training
  and validation inflate scores. Test: split by object before augmentation; group copies in one
  fold (arXiv:1907.04690, Sect. III.6; arXiv:2602.13036, Sect. 4.1; arXiv:1808.09955, Sect. 3)
  [src].
- **A ranking metric hides contamination.** AUROC ranked the lens finders differently from TPR0;
  at a lens fraction of 10⁻³, only the low-FPR end of the ROC matters (arXiv:1802.03609)
  [src: Sects. 5.1, 5.2].
- **Unseen classes have no honest probability.** The top five PLAsTiCC teams set the "Other"
  probability with hand-tuned formulae probed on the leaderboard (Avocado: P_99 = P_42 +
  0.6 P_62 + 0.2 P_52 + 0.2 P_95 for extragalactic objects, 4% for Galactic ones), which the
  author calls "not a proper way of identifying new objects" (arXiv:1907.04690)
  [src: Sect. II.2.3, Eq. 4].
- **A probability that is not calibrated.** Boosted trees and SVMs push probabilities away from 0
  and 1, and deep networks trade calibration for accuracy (as cited in arXiv:1901.06384)
  [src: Sect. 5.1]. Test: reliability diagram on a held-out set from the target domain.
- **High confidence on garbage.** OOD curves can be classified with high probability and low
  entropy (arXiv:1901.06384) [src: Sect. 5.3]. Test: synthetic OOD inputs at the survey cadence;
  an explicit anomaly score (L2, `physics-and-methods.md#anomaly-detection`).
- **Leakage through survey design.** Phase windows of [−100, 200] days for SLSNe and IIn against
  [−50, 80] days for others let a classifier infer duration from the span of the data; the ZTF
  authors judge this a physical feature (arXiv:2602.13036) [src: Sect. 4.1]. A referee should
  check that no selection or preprocessing label correlates with the class by construction.
- **Labels are uncertain.** The ZTF training sample still contains peculiar SNe Ia through
  incomplete subtyping, and its labels are preliminary (arXiv:2602.13036) [src: Sect. 2.1];
  QuasarNET removes spectra without a firm visual identification (8939 spectra)
  (arXiv:1808.09955) [src: Sect. 2].

## Reading list
<!-- key: reading-list -->

- Method: Boone 2019, arXiv:1907.04690 — GP augmentation recipe, redshift-weighted metric, the
  biased-training-set test.
- Method: Möller & de Boissière, arXiv:1901.06384 — RNN input encoding, early
  classification, reliability diagrams, synthetic OOD tests.
- Method: Qu et al. 2021, arXiv:2106.04370 — heatmap construction and class balancing.
- Method: Shah et al. 2025, arXiv:2501.01496 — hierarchical WHXE loss and phase augmentation.
- Application: Townsend et al. 2026, arXiv:2602.13036 — augmentation of a real spectroscopic
  sample, bright/faint split, live follow-up.
- Method: Busca et al. 2018, arXiv:1808.09955 — spectra as line detection; threshold choice.
- Critique: Hložek et al. 2020, arXiv:2012.12392 — the metric, its weights, what the top entries
  did.
- Critique: Metcalf et al. 2018, arXiv:1802.03609 — why AUROC is not the figure of merit for rare
  classes.

## Not verified
<!-- key: not-verified -->

- The weighted hierarchical cross-entropy paper of Villar et al. 2023 and the ATAT classifier of
  Cabrera-Vives et al. 2024, both cited by ORACLE: not read; their numbers here are as ORACLE
  quotes them.
- STACCATO (Revsbech et al.) and the representativeness study of Lochner et al. cited by Avocado
  as ref. 32 (arXiv:1907.04690, Sect. I): not read. Avocado quotes the STACCATO AUC without
  augmentation as 0.92 in its introduction (Sect. I) and 0.93 in Sect. III.4.
- ParSNIP (Boone 2021): read only as described in arXiv:2602.13036.
- Calibration and threshold choices of the DESI quasar classification and of the DES-SN5YR
  SuperNNova ensembles: in `cosmo-data-pipelines` and `cosmo-supernovae`, not re-read here.
- No study was found that compares the four input representations on one data set with one
  metric.
