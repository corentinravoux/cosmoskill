# Photometric redshifts by machine learning — cosmo-photometry-photoz dossier

Scope: how a training-based photo-z is set up in practice (training
compilation and its weights, input features and missing bands, data
splits and hyper-parameter tuning, PDF construction, post-hoc PDF
calibration, flags for objects outside the training coverage), and how to
choose between reweighting, stratification and domain adaptation when the
training set does not represent the target sample.
Snapshot: 2026-10-19.
From: Newman & Gruen 2022 review, Sect. 2.2; Tortorelli & Grün 2026
review, Sect. 2 (copied from `references/subtopics.tsv`).

Already in L2, not repeated here: the families of codes and what each
paper establishes (`physics-and-methods.md#method-families`); the
implicit-prior argument and the four mechanisms by which training samples
bias learned redshifts (`physics-and-methods.md#implicit-priors-and-imperfect-training-sets`);
point-estimate and PDF metrics, CDE loss, the Euclid F_005/F_015 metrics
(`physics-and-methods.md#metrics-requirements-and-codes`); challenge
results and per-code numbers (`results.md#challenge-results`,
`results.md#photo-z-performance-of-individual-galaxies`); the debate on
usable PDFs (`open-questions.md#can-machine-learning-photo-z-deliver-usable-pdfs`).
PDF recalibration of template and narrow-band codes (ODDS, Bordoloi
remapping, κ outlier term, Lorentzian kernel) is in
`deep/narrow-many-band-photometry.md`; SOM-based n(z) calibration, which
does not need per-galaxy photo-z, is in `physics-and-methods.md#self-organising-maps-som`.
Machine learning outside photo-z belongs to `cosmo-machine-learning`.

Symbols. x: vector of input features (magnitudes, colours, errors, sizes)
of one galaxy; z_spec, z_ref: reference redshift (spectroscopic, grism or
many-band photo-z); f(z | x): conditional density of z given x, the
quantity a PDF code estimates; w_i: weight of training galaxy i;
S, T: source (training) and target (photometric) samples; e(x): propensity
score, the probability that an object with features x is in S;
Δz = (z_phot − z_ref)/(1 + z_ref) unless stated; σ_NMAD and the outlier
fraction η_0.15 (|Δz| > 0.15) as defined in
`results.md#photo-z-performance-of-individual-galaxies`. <!-- num: not a value -->

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Assemble the training set and its quality cuts
<!-- key: step-1-assemble-the-training-set-and-its -->

A production training set is a compilation: spectroscopic, grism or prism,
and many-band photo-z redshifts, each with its own quality scheme to be
homogenised.

- **HSC-SSP DR1.** About 170k spectroscopic and 37k grism/prism redshifts,
  supplemented by about 170k COSMOS2015 many-band photo-z [src:
  arXiv:1704.05988, Sect. 2.1]. Cuts: 0.01 < z < 9, σ_z < 0.005(1+z),
  SDSS/BOSS zWarning = 0, DEEP2 and PRIMUS qFlag = 4, VIPERS and VVDS
  qFlag = 3–4 (> 95% confidence), GAMA and WiggleZ qFlag ≥ 4; 3D-HST
  grism redshifts kept if the 1σ half-width is < 0.05(1+z) and the 2σ one
  < 0.1(1+z); COSMOS photo-z kept only without secondary peaks, with
  χ²(gal) < χ²(star), χ²/N_bands < 5, log M* > 7.5 and a 1σ half-width
  < 0.05(1+z) [src: Sect. 2.1]. Matches are made iteratively at UltraDeep,
  Deep and then Wide depth within 1″ "to take advantage of higher-S/N data
  when available while avoiding possible duplicates" [src: Sect. 2.1].
- **Rubin DP1 (ECDFS).** Reference galaxies matched within 0.75″; kept if
  detected in all six bands with i-band CModel S/N > 20 and confidence
  > 0.9; 70/30 split into 6778 training and 2905 test galaxies; the mean
  confidence 0.97 implies about 3% outliers in the training set, tolerated
  "due to the limited sample size" [src: arXiv:2510.07370, Sect. 2.2.1].
  The training galaxies reach only i < 24.6 against i < 26.7 for the
  object catalogue, and requiring all six bands likely removes dropout
  galaxies [src: Sect. 2.2.1].
- **COSMOS-trained CNN for HSC.** COSMOS2020 redshifts replaced by spectra
  where available (~19% at i < 25), about 2700 bright spectra added; the
  large-scale-structure spikes of the pencil-beam field were trimmed by
  removing galaxies from the densest RA–Dec regions in each redshift
  interval protruding above a KDE-smoothed n(z), about 14% at i < 25,
  because such spikes "tend to bias the photometric redshift estimates of
  trained algorithms" and over-represent massive red cluster galaxies; the
  trimming is redrawn at each training epoch [src: arXiv:2512.11700,
  Sect. 3].

### Step 2. Weight the training set to the target sample
<!-- key: step-2-weight-the-training-set-to-the-target -->

The training sample is reweighted so that its distribution in observable
space matches the target's (the Lima et al. idea, `physics-and-methods.md#direct-reweighting`).

- HSC DR1 computes colour–magnitude weights with a generalisation of the
  Lima et al. nearest-neighbour approach, and all its statistics are
  computed with these weights [src: arXiv:1704.05988, Sect. 2.1–2.2].
- Duncan 2022 (Legacy Surveys DR8) estimates the densities with Gaussian
  mixture models (GMM) in the same feature space for the full photometric
  and training samples, and uses the cost-sensitive-learning (CSL) weight

    w_i = [p_full(m̂_i) + ε] / [p_train(m̂_i) + ε]  (arXiv:2203.01949, Eq. 4),

  with ε = 0.001 (arXiv:2203.01949; against 0.01 in the method paper it follows) and a
  maximum weight of 100 (against 20), larger dynamic range being allowed
  by the larger training set; ε stops sparse regions of the training GMM
  from producing extreme weights [src: Sect. 3.2]. The GMM space is g − r,
  r − z and asinh m_z, plus half-light radius for resolved sources or
  z − W1 for point sources [src: Sect. 3.1–3.2]. Median weights span more
  than three orders of magnitude across g − r / r − z; colour-selected
  BOSS/eBOSS ELG and LRG samples get very low weights [src: Sect. 3.2].
- The weights also enter the validation: Duncan 2022 (arXiv:2203.01949) draws 1000 test
  galaxies with probability proportional to their CSL weight, 100 times,
  to quote "representative" σ_NMAD and η_0.15 [src: Sect. 3.3], and
  weights the credible-interval distribution used to calibrate the errors
  (Step 6) [src: Sect. 3.4].

### Step 3. Choose and preprocess the features
<!-- key: step-3-choose-and-preprocess-the-features -->

- **Magnitudes, not fluxes, with asinh softening.** Duncan 2022 trains in
  log-flux space because magnitudes gave better results for this kind of
  method in earlier work, and uses asinh magnitudes so that non-detections
  and negative fluxes are kept:
  m = −2.5/ln(10) × asinh[(f/f₀)/(2b)] + ln(b), f₀ = 3631 Jy (Eq. 1), with
  σ_m from Eq. 2; the softening b is set per source to the local 1σ PSF
  depth in each band because depth varies within and between the North and
  South imaging [src: arXiv:2203.01949, Sect. 2.1.2]. Results were not
  sensitive to the exact b [src: Sect. 2.1.2, App. A]. Fluxes and errors
  are dereddened (SFD E(B−V) with the catalogue coefficients) before the
  asinh transform [src: Sect. 2.1.2]. HSC also uses asinh magnitudes
  [src: arXiv:1704.05988, Fig. 1 caption].
- **Errors as features.** GPz feeds the five SDSS modelMag magnitudes and
  their errors, the errors replaced by their logarithm so that all features
  share the real domain, then decorrelated by PCA to zero mean and unit
  covariance ("sphering") without dimensionality reduction, for speed and
  numerical stability [src: arXiv:1604.03593, Sect. 6.2].
- **Magnitude plus colours.** The FlexCode/StratLearn photo-z test uses the
  r-band magnitude and the four adjacent colours [src: arXiv:2106.11211,
  Sect. 4.3]; the Duncan 2022 GPz uses seven asinh magnitudes (g, r, z,
  W1–W4) plus half-light radius for resolved sources [src:
  arXiv:2203.01949, Sect. 3.3].
- **Which flux.** On DP1, GAaP 1.0″, CModel and Sérsic fluxes performed
  better than other flux types in scatter and outliers and comparably to
  each other; GAaP 1.0″ was adopted [src: arXiv:2510.07370, Sect. 4.1].
- **Homogenise photometric systems first.** Legacy North and South differ
  in filter curves; offsets measured on > 10σ point sources in the overlap
  reach +0.1 in g for the reddest sources, ≈ 0.03 in r and ≈ −0.02 in z,
  fitted by cubic polynomials in (g − z)_N, clipped to 0.3 < (g − z)_N <
  3.3 to avoid over-correcting noisy colours; mean applied offsets 0.056,
  0.012, −0.010 in g, r, z, so one model can be trained on both hemispheres
  [src: arXiv:2203.01949, Sect. 2.1.3].
- **Missing bands.** In CSST mocks with bands removed completely at
  random, k-nearest-neighbour imputation was best with a complete training
  set, but with 30% of training entries missing its photo-z outlier fraction
  rose to 22.36%, while a self-attention imputer (SAITS) stayed at 4.07%
  [src: arXiv:2605.13219, Sect. 4.2.3]. Imputing non-detections (missing
  not at random, set by the magnitude limit) was "detrimental"; the
  recommendation is to impute only random gaps and leave non-detections,
  which needs forced photometry to tell them apart [src: Sect. 6].

### Step 4. Split, tune and choose the loss
<!-- key: step-4-split-tune-and-choose-the-loss -->

- **Splits.** HSC: five random folds of ~75k, folds 1–3 to train, 4 to
  validate, 5 to test; only FRANKEN-Z used rotating cross-validation
  [src: arXiv:1704.05988, Sect. 2.2]. GPz paper: three random sets of
  100,000 for training, model selection and testing [src: arXiv:1604.03593,
  Sect. 6.2]. COSMOS-trained CNN: 80/20 cross-validation, PDFs averaged
  over six runs [src: arXiv:2512.11700, Sect. 4.2].
- **Tune to the loss that matches the product.** FlexCode estimates
  f(z | x) = Σ_i β_i(x) φ_i(z) on an orthonormal basis (Eq. 1–3), each
  β_i(x) = E[φ_i(Z) | x] being an ordinary regression; the cutoff I of the
  expansion is chosen on a validation set by minimising the estimated
  L² (CDE) loss L̂ = Σ_i (1/n′) Σ_k β̂_i²(x′_k) − (2/n′) Σ_k f̂(z′_k | x′_k)
  (Eq. 5) [src: arXiv:1704.08095, Sect. 2–2.1]. In HSC, MLZ was tuned on
  σ_conv instead of the loss used to compare codes, which "might partly be
  the reason" it did worse than the other machine-learning codes [src:
  arXiv:1704.05988, Sect. 3.4].
- **Hyper-parameters used on DP1** (RAIL v1.2 defaults in brackets): TPZ
  10 bootstrap samples (8), 10 trees (5), minimum leaf 2 (5); kNN 10
  neighbours (7); GPz variable diagonal covariance and 1000 iterations
  (200, "does not converge"); FlexZBoost 50 basis functions (35); PDFs on
  0 < z < 3 [src: arXiv:2510.07370, Sect. 4.1]. The authors do not regard
  them as fully optimised for future Rubin data [src: Sect. 4.1].
- **Point estimate.** HSC defines L(Δz) = 1 − 1/[1 + (Δz/γ)²], γ = 0.15
  (Eq. 14), a continuous outlier rate, and takes z_best = argmin of the
  risk R(z_phot) = ∫ P(z) L[(z_phot − z)/(1+z)] dz (Eqs. 15–16); z_best
  beats mean, median and mode, and R is a better reliability flag than the
  ±0.03 confidence C(z) [src: arXiv:1704.05988, Sect. 4.1–4.2].

### Step 5. Turn the regression into a PDF
<!-- key: step-5-turn-the-regression-into-a-pdf -->

| Code | How the PDF is made | Source |
|---|---|---|
| DNF | residuals s_i = z_spec,i − a·m_i of the neighbours about the local hyperplane added to z_phot, z_i = z_phot + s_i, then histogrammed (Eqs. 16–17) | arXiv:1511.07623, Sect. 5.2 |
| DEmP | 500 Monte Carlo realisations of the input photometry × 500 bootstraps of the training set per galaxy | arXiv:1704.05988, Sect. 3.1 |
| MLZ (SOM) | N_boot × N_MC perturbed catalogues, 24 × 16, with N_pix = 16 | arXiv:1704.05988, Sect. 3.4 |
| FlexCode / FlexZBoost | basis expansion; negative values and spurious bumps removed afterwards | arXiv:1704.08095, Sect. 2.1 |
| ANNz | second network trained on the squared residuals gives the variance; calibrated only for large, representative training sets and near-Gaussian f(z | x) | arXiv:2009.12112, Sect. 3.6 |
| GPz | Gaussian with input-dependent variance (model term plus noise term) | arXiv:1604.03593, Sect. 5; arXiv:2203.01949, Sect. 3.4 |

Duncan 2022 divides the population into GMM components and trains one GPz
per component ("GMM-Divide"), 500 basis functions shared as 500/N per
component; sources go to their best-matching component, because a
probability-weighted sum over components would take k times longer to
predict [src: arXiv:2203.01949, Sect. 3.1, 3.3]. Training GPz several times
on noise-perturbed data (non-Gaussian posteriors) gave a "small
statistical improvement" not worth the linear cost [src: Sect. 3.3].

### Step 6. Calibrate the PDFs after training
<!-- key: step-6-calibrate-the-pdfs-after-training -->

Duncan 2022 computes for each test galaxy the threshold credible interval
c_i = erf(|z_spec − z_phot| / (√2 σ_i)) (Eq. 7), compares the cumulative
F̂(c) with the 1:1 line (below it: errors too small), and rescales
σ_new = σ_old α(m), α = α_η for m ≤ m_η and α_η + κ(m − m_η) beyond
(Eqs. 8–9), with m_η = 16 in r, α_η and κ fitted per morphology by MCMC on
the distance to the 1:1 line, F̂(c) being CSL-weighted [src:
arXiv:2203.01949, Sect. 3.4]. Before calibration the GPz errors were
over-estimated (under-confident) across magnitudes and morphologies;
after it F̂(c) follows the 1:1 line except at 0.8 < c < 1 for PSF, DEV and
REX sources, where the tails stay too thin, a limit of Gaussian posteriors
[src: Sect. 3.4]. The step is needed because training sets are not
representative, CSL weights do not fully fix that, input errors may be
wrong and GPz posteriors are unimodal [src: Sect. 3.4].

HSC DR1 shows the alternative diagnosis: a convex PIT (EPHOR_AB) means
over-dispersed PDFs, a concave one (Mizuki) under-dispersed, and spikes at
both ends mean outliers absent from the PDFs; it announced PIT-based
recalibration for later releases [src: arXiv:1704.05988, Sect. 6.2].

### Step 7. Flag objects outside the training coverage
<!-- key: step-7-flag-objects-outside-the-training -->

- GPz's predictive variance can be used to reject objects; on SDSS its
  variable-covariance variant (gpvc) improves on TPZ, ANNz2 and other GP
  variants in RMSE, mean log-likelihood and outlier fractions across the
  whole rejection range, especially beyond 20% of the data [src:
  arXiv:1604.03593, Sect. 7.3, Table 2].
- In degraded-training tests, PzFlow "rarely produces estimates" for data
  poorly represented in training; GPz returns "identifiably extreme"
  parameters that a cut on mean or width can catch; FlexZBoost's failures
  are not identified (multimodality was rare even with GAMA-like training);
  CMNN has "little to no notion" of failure [src: arXiv:2601.10797,
  Sect. 4.3].
- Strong rejection must match the science: METAPHOR and DNF keep their
  precision by rejecting mostly z > 1 sources, which makes them
  "incompatible with the goals of the weak-lensing analysis" in the Euclid
  challenge [src: arXiv:2009.12112, Sect. 5.2, 5.4].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Reweighting, population division, or both
<!-- key: reweighting-population-division-or-both -->

- *CSL weights alone.* Assume the target lies inside the training support;
  improve σ_NMAD and η for all morphologies when the population is not
  divided [src: arXiv:2203.01949, Sect. 3.3, Fig. 6].
- *GMM-Divide* (arXiv:2203.01949). Lowers scatter and especially outliers for all
  morphologies; beyond a sufficient N there is no universal gain; for
  z > 3 quasars η_0.15 falls from 0.71 (one model for all PSF sources) to
  0.2 with 10 components, and rises to ≈ 0.32 with 15–20 [src: Sect. 3.3].
  More than four GMM dimensions gave too many components without training
  galaxies [src: Sect. 3.1].
- *Both.* Mixed: some morphologies better with weights, others with
  uniform weights; weights kept as standard because resolved sources gain
  or lose negligibly [src: Sect. 3.3].
- *Uniform resampling (DEmP).* Flattening the training population did not
  help in HSC because the dense COSMOS photo-z already give local neighbours
  of similar colour and magnitude [src: arXiv:1704.05988, Sect. 3.1].

### Importance weighting or stratification on the propensity score
<!-- key: importance-weighting-or-stratification-on-the -->

StratLearn estimates e(x) = P(s = 1 | x) with a probabilistic classifier
(logistic regression, all potential confounders as main effects), splits
source and target into k = 5 strata at quantiles of e(x), and fits one
model per stratum; conditional on e(x) the source and target joint
distributions are equal (Proposition 1, Eqs. 4–9); five strata follow
Cochran's result that they remove at least 90% of the bias for many
continuous distributions; sparse strata borrow neighbours at some cost in
bias [src: arXiv:2106.11211, Sect. 3.1–3.2]. On the SDSS photo-z set-up
(467,710 galaxies, r plus four colours, an r-dependent beta-function
rejection to make the target, 2800 training, 1200 validation, 6000 test
galaxies) the stratified combination of kernel-NN and series estimators
has the lowest target risk in all three covariate sets, and its advantage
over importance weighting grows with the number of (added noise)
covariates [src: Sect. 4.3]. Cost: one model per stratum, and the
covariate-shift assumption p_S(z | x) = p_T(z | x) itself, which fails if
spectroscopic success depends on unobserved properties [src: Sect. 3.2;
arXiv:2206.13633, Sect. 2.2].

### Domain adaptation on images
<!-- key: domain-adaptation-on-images -->

An adversarial branch, fed by the fifth convolutional layer, tries to tell
COSMOS training images from 100,000 unlabelled images of another field;
the main network is trained to fool it while predicting redshift [src:
arXiv:2512.11700, Sect. 5.1]. Pairing source and target galaxies by
i-band magnitude (one target among the 30 nearest in i) to avoid negative
transfer made no significant difference [src: Sect. 5.1]. On DEEP2 the
adversarial model trained on COSMOS alone (v2) improved markedly over the
baseline (v0) and gave n(z) of unlabelled faint galaxies closer to the
reference; adding DEEP2 spectra to training (v3) improved the metrics on
the spectroscopic sample but induced a stronger negative bias on 1600
[O II] emitters at z ≈ 1.47, read as a sign that "even a small fraction of
unrepresentative target sources" in training biases the result and that
spectroscopic-sample metrics "remain misleading"; v2 was adopted [src:
Sect. 5.2]. Training on u* and predicting on u data "significantly
degrades" performance, so each field uses a model trained on its own band
set [src: Sect. 4.2].

### Machine learning, template fitting, or a hybrid
<!-- key: machine-learning-template-fitting-or-a-hybrid -->

In the Euclid challenge, machine-learning methods beat template codes at
z < 0.8 and lose above it, and the gap widens on the many-band (L15)
sample less represented in training; below z = 0.5 every template code is
outmatched, read as missing low-z templates or priors that training sets
supply implicitly [src: arXiv:2009.12112, Sect. 5.2]. A hybrid that takes
METAPHOR where its USE flag is 1 and z_phot < 0.6, and Phosphoros
elsewhere, is the best non-rejecting method, ⟨F_005⟩_corrected = 0.27 on
the weighted spectroscopic sample [src: Sect. 5.4]. On Rubin DP1 the
machine-learning codes have less bias across magnitude than template codes
[src: arXiv:2510.07370, Fig. 5 caption]; results in
`results.md#photo-z-performance-of-individual-galaxies`.

### Metric used to judge damage
<!-- key: metric-used-to-judge-damage -->

Under realistic survey-like degradation, the RMSE barely moves; KL
divergence and Wasserstein distance track training-set coverage; the CDE
loss separates estimators more than it separates training sets; CvM is
misleadingly low for some poor cases; outlier rejection can give an
"artificially low" outlier rate when estimation is very poor [src:
arXiv:2601.10797, Sect. 5]. CDE loss falls monotonically with the
fraction of redshift–magnitude cells covered by training, while training
size alone scatters [src: Sect. 4.2.3].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| HSC training compilation | ~170k spec-z, 37k g/prism-z, ~170k COSMOS2015 photo-z; folds of ~75k | HSC DR1 | arXiv:1704.05988 | Sect. 2.1–2.2 |
| Spec-z error cut | σ_z < 0.005(1+z) | HSC DR1 | arXiv:1704.05988 | Sect. 2.1 |
| Loss scale γ | 0.15 | HSC DR1 | arXiv:1704.05988 | Sect. 4.1 |
| DP1 training cuts | 0.75″ match, all 6 bands, i S/N > 20, confidence > 0.9; 6778 / 2905 | Rubin DP1 | arXiv:2510.07370 | Sect. 2.2.1 |
| DP1 training depth vs target | i < 24.6 vs i < 26.7 | Rubin DP1 | arXiv:2510.07370 | Sect. 2.2.1 |
| CSL ε, maximum weight | 0.001, 100 (method paper: 0.01, 20) | LS DR8 | arXiv:2203.01949 | Sect. 3.2 |
| GMM components | 10 per morphology; ≤ 4 dimensions | LS DR8 | arXiv:2203.01949 | Sect. 3.1, 3.3 |
| GPz basis functions | 500 total, 500/N per component | LS DR8 | arXiv:2203.01949 | Sect. 3.3 |
| Error rescaling pivot | m_η = 16 (r band) | LS DR8 | arXiv:2203.01949 | Sect. 3.4 |
| North → South offsets (mean) | 0.056, 0.012, −0.010 in g, r, z | LS DR8 | arXiv:2203.01949 | Sect. 2.1.3 |
| GPz data split | 3 × 100,000 from 2,120,465 SDSS DR12 galaxies | SDSS | arXiv:1604.03593 | Sect. 6.2 |
| COSMOS spike trimming | ~14% removed at i < 25; ~155,000 kept | HSC CNN | arXiv:2512.11700 | Sect. 3 |
| StratLearn strata | k = 5 | method | arXiv:2106.11211 | Sect. 3.2 |
| DP1 FlexZBoost basis | 50 (default 35) | Rubin DP1 | arXiv:2510.07370 | Sect. 4.1 |
| Imputation, 30% missing in training | η: kNN 22.36%, SAITS 4.07% | CSST mocks | arXiv:2605.13219 | Sect. 4.2.3 |
| Training-limited bias level | |⟨Δz⟩/(1+z)| > 0.008 "commonly" | review | arXiv:2206.13633 | Sect. 2.2 (margin note) |
| Training size range in degradation test | ~200 (pseudo-BOSS) to ~80,000 (VVDS-like) | LSST DESC mocks | arXiv:2601.10797 | Sect. 2.3.2 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Over-fitting through shared photometry.** FRANKEN-Z's PIT peaked at
  the centre, "PDF is too accurate", tentatively traced to training
  objects whose Wide-depth and Deep/UltraDeep photometry are not
  independent, so training and target realisations of the same galaxy
  agree better than their errors allow; hold-out tests on the native
  training sample did not show it [src: arXiv:1704.05988, Sect. 6.2].
  Test: PIT on held-out data whose photometry is independent of the
  training photometry.
- **A flat PIT proves nothing on its own.** A method with no predictive
  power can have a perfect PIT (the trainZ example) [src:
  arXiv:2009.12112, Sect. 5.2]; pair PIT with a precision or CDE-loss
  metric.
- **Large-scale structure in a small training field** is learned as a
  prior; trim or smooth it (Step 1) [src: arXiv:2512.11700, Sect. 3].
- **Training brighter or higher-S/N than the target.** DP1 trains on
  i-band S/N > 20 while the catalogue goes ~2 mag deeper, and PRIMUS and
  ASTRODEEP dominate the low- and high-z ends, so their selections may be
  imprinted on the photo-z [src: arXiv:2510.07370, Sect. 2.2.1].
- **Different band sets between training and target fields** degrade the
  result even when the bands are nominally equivalent (u vs u*) [src:
  arXiv:2512.11700, Sect. 4.2]; homogenise systems first [src:
  arXiv:2203.01949, Sect. 2.1.3].
- **Tuning on the wrong objective** (σ_conv instead of the comparison
  loss) can make a code look worse than it is [src: arXiv:1704.05988,
  Sect. 3.4].
- **Silent failure outside coverage.** Codes differ in whether they flag
  it (Step 7); CMNN and FlexZBoost give no usable flag [src:
  arXiv:2601.10797, Sect. 4.3].
- **Validation on the spectroscopic sample flatters.** Adding target-field
  spectra improved spectroscopic metrics while biasing the [O II] test
  sample [src: arXiv:2512.11700, Sect. 5.2]; weighted-sample tests in the
  Euclid challenge raised η to 13–33% for most codes
  (`results.md#challenge-results`).
- **Imputing non-detections** as if missing at random biases the result
  [src: arXiv:2605.13219, Sect. 6].
- **Gaussian posteriors miss tails**: after calibration, F̂(c) still falls
  below 1:1 at 0.8 < c < 1 for three morphologies [src: arXiv:2203.01949,
  Sect. 3.4]. Lensing needs the tails [src: arXiv:2206.13633, Sect. 2.2].

Validation checklist as the papers practise it: held-out test fold never
used for tuning (HSC, GPz); statistics weighted to the target population
(HSC, LS DR8); PIT or credible-interval Q–Q plot together with a precision
metric (HSC, LS DR8, Euclid); performance against redshift and magnitude
with the requirement band overlaid (DP1, Fig. 5); a test sample selected
independently of the training spectra (the [O II] emitters of
arXiv:2512.11700).

## Reading list
<!-- key: reading-list -->

- Review: Newman & Gruen 2022, arXiv:2206.13633, Sect. 2.2 — the three
  axes on which empirical methods differ and their failure modes.
- Method: Almosallam et al. 2016, arXiv:1604.03593 — GPz preprocessing,
  heteroscedastic variance, rejection curves.
- Method: Izbicki & Lee 2017, arXiv:1704.08095 — FlexCode, the CDE loss as
  a tuning objective.
- Method: De Vicente et al. 2016, arXiv:1511.07623 — DNF neighbourhood fit
  and residual-based PDFs.
- Application: Tanaka et al. 2018, arXiv:1704.05988 — a production
  compilation with quality cuts, weights, folds, risk-based point estimates
  and PIT diagnosis of six codes.
- Application: Duncan 2022, arXiv:2203.01949 — asinh features, system
  homogenisation, GMM-Divide, CSL weights, credible-interval calibration.
- Application: Zhang et al. 2025, arXiv:2510.07370 — RAIL codes on real
  Rubin data with the hyper-parameters changed.
- Method: Autenrieth et al. 2021, arXiv:2106.11211 — stratification on the
  propensity score instead of importance weights.
- Method: Treyer et al. 2025, arXiv:2512.11700 — adversarial domain
  adaptation for image-based photo-z.
- Critique: Crafford et al. 2026, arXiv:2601.10797 — which metrics reveal
  training-set damage; failure flags per code.
- Critique: Euclid Collaboration: Desprez et al. 2020, arXiv:2009.12112,
  Sect. 5 — PIT limits, rejection versus completeness, hybrids.
- Method: Wang et al. 2026, arXiv:2605.13219 — imputation of missing bands
  and the MNAR trap.

## Not verified
<!-- key: not-verified -->

- The Bordoloi et al. 2010 PIT recalibration and the Gomes et al. 2018
  method were not read at source; the recalibration formula quoted in
  `deep/narrow-many-band-photometry.md` comes from arXiv:2312.07581.
- Hatfield et al. 2020 (the GMM-Divide and CSL method paper), Izbicki et
  al. 2017 (importance-weighted CDE) and Moretti et al. 2025 (stratified
  learning for photo-z) were cited by the papers read but not read
  themselves.
- The HSC DNNz and DEmPz codes used for the HSC Y3 lensing n(z)
  (arXiv:2003.01511) and the PzFlow and CMNN method papers were not read.
- The Speagle et al. generalisation of the Lima weights used by HSC was
  "in prep." in arXiv:1704.05988 and was not read.
- Two 2025–2026 papers found in the date-restricted search were seen only
  by title and listing summary: arXiv:2603.19882 (quasar photo-z
  uncertainty models under data shifts, KiDS DR5) and arXiv:2511.03802
  (machine-learning photo-z for sparse JWST filter sets).
