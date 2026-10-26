# Tension metrics — cosmo-statistics-inference dossier

Scope: how each tension metric in current use is computed from chains (density estimators,
nested-sampling outputs, mode selection, Gaussianisation, conversion to σ), how a collaboration
fixes and calibrates its metric before unblinding, and how to choose a metric for a given pair
of data sets; the defining formulae and the published values are in the reference files.
Snapshot: 2026-10-16.
From: CosmoVerse White Paper, Sect. 3.1.8; DES tension-metric suite (Lemos et al. 2021).

Prerequisites at L2: definitions of the Bayes ratio, information ratio, suspiciousness, Bayesian
model dimensionality, parameter difference, update form, goodness-of-fit loss, eigentension and
posterior predictive tests in `physics-and-methods.md#tension-metrics`; values on the same data
in `results.md#tension-metrics-on-the-same-data`; correlated data in
`physics-and-methods.md#combining-probes-and-correlated-datasets`; the open points in
`open-questions.md#which-tension-metric-and-is-n-sigma-meaningful`. Equation numbers are those
of the paper cited next to them.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Fix the question, the metric and the threshold before the data are seen
<!-- key: step-1-fix-the-question-the-metric-and-the -->

- DES chose its metric before the Year 3 release by simulation: "the motivation is to decide on
  a metric of tension between these two surveys ahead of the DES Y3 data release" (Lemos et al.
  2021, arXiv:2012.09554) [src: Sect. 7].
- DES Y6 writes the rule into the analysis plan: the parameter-difference probability, reported
  as an effective number of σ, with `n_σ < 3` "as the criterion for different data sets agreeing
  well enough that it makes sense to examine their combined constraint"; headline numbers are
  full-parameter tensions, with 1D or 2D values "when needed" (DES Collaboration 2026,
  arXiv:2601.14559) [src: Sect. IV.6].
- KiDS-Legacy fixes a different metric and a different threshold: the Hellinger distance between
  one-dimensional marginal mode summaries, with surveys called consistent if `|ΔX| ≤ 2.6σ`, `X`
  being Σ8 or S8 (Wright et al. 2025, arXiv:2503.19441) [src: Sect. 6, Fig. 14].
- With many pairwise tests, a look-elsewhere threshold. Ong et al. 2025 flag the DESI
  DR2–DES-SN5YR conflict as "exceeding our 2.88σ look-elsewhere threshold" (arXiv:2511.10631)
  [src: Sect. III].

### Step 2. Calibrate the metric on synthetic tension
<!-- key: step-2-calibrate-the-metric-on-synthetic-tension -->

The DES recipe for an "a-priori Gaussian tension" (arXiv:2012.09554) [src: Sect. 3.1]:

1. From the baseline posteriors, compute the marginal variances of Ω_m and σ8 for both
   experiments, and the unit shift `δθ = sqrt(var(θ_DES) + var(θ_Planck))` [src: Eq. 2].
2. Generate synthetic DES data vectors with Ω_m or σ8 shifted by integer multiples of `δθ`; a σ8
   shift is a change of `A_s`; an Ω_m shift is compensated by a counter-shift of `A_s` so that
   σ8 does not move with it.
3. Assign each shift its expected significance from `χ² = δθ^T (C_D + C_P)^-1 δθ` with the 2 × 2
   covariances in (Ω_m, A_s), two degrees of freedom [src: Eq. 3], converted with `N_σ ≡ sqrt(2)
   Erf^-1(PTE)` [src: Eq. 4].
4. Run every candidate metric on the synthetic chains and compare with the a-priori value (the
   table is in `results.md#tension-metrics-on-the-same-data`).

The authors state that their conclusions on the metrics "apply to any problem of tension
quantification", but that the Bayes ratio would have to be recalibrated "to a different problem
with uninformative priors" [src: Sect. 7]. A metric adopted from another analysis without this
step inherits that analysis's calibration.

### Step 3. Choose the parameter space
<!-- key: step-3-choose-the-parameter-space -->

- Parameters that only the prior constrains, in both data sets, "can never contribute a shift":
  with constant likelihoods the parameter-difference density is the autocorrelation of the
  prior, maximal at zero shift [src: arXiv:2105.03324, Sect. II.1, Eq. 5]. Parameters
  constrained by flat priors for one data set and not by the other cannot contribute either
  [src: Eq. 6]. Hence "non-shared parameters between two experiments can never contribute any
  shift and can be pre-marginalized over" (Raveri & Doux 2021, arXiv:2105.03324) [src: Sect.
  II.1].
- The full shared space and a projection give different numbers on the same chains. DES Y6 3×2pt
  against the CMB in wCDM: 1.3σ in the full space, 1.0σ projected on S8, 2.1σ in the w–S8 plane
  (arXiv:2601.14559) [src: Sect. V.3]; the ΛCDM pair 1.8σ and 2.6σ is in
  `results.md#tension-metrics-on-the-same-data`.
- A plane chosen for the physics. ACT DR6 quantifies P-ACT against DESI DR2 as "the Gaussian
  separation in 2-dimensional space of the Ω_m–h r_d parameter combination": 1.6σ for P-ACT or
  P-ACT-L, 2.8σ for ACT-L, the latter "partly driven by the τ measurement" (Louis et al. 2025,
  arXiv:2503.14452) [src: App. H, Fig. 43]. SPT-3G quotes its 2.8σ for SPT + ACT + Planck
  against DESI DR2 in the same Ω_m–h r_d plane (Camphuis et al. 2025, arXiv:2506.20707) [src:
  Sect. II]. Same plane, different CMB combinations: the two numbers differ by the CMB data, not
  by the subspace.

### Step 4. Compute the metric
<!-- key: step-4-compute-the-metric -->

**Parameter difference, high-dimensional (DES Y6).** The density of the difference is `P(Δp) = ∫
P(p given A) P(p − Δp given B) dp` [src: arXiv:2601.14559, Eq. 17]; the consistency estimator is
the weighted fraction of difference samples above the iso-density contour through zero, `Δ =
(Σ_i w_i)^-1 Σ_i w_i S(P̂(Δp_i) − P̂(0))`, `S` the Heaviside step and `P̂` the normalising-flow
density [src: Eq. 18], then `n_σ ≡ sqrt(2) erf^-1(Δ)` [src: Eq. 19]; the computation uses
`tensiometer` [src: Sect. IV.6]. The flow procedure (Raveri & Doux 2021, arXiv:2105.03324) [src:
Sect. IV.1]:

1. Build samples of `Δθ` from the two chains.
2. Train a bijective map `T_φ` that Gaussianises them, by minimising `−log φ_D(T_φ(Δθ))` with
   stochastic gradient descent; the density is `q(Δθ) = φ_D(z) |det ∇T_φ|`.
3. Sample `Δθ ~ q`, compute `q` at each sample and at `Δθ = 0`; the fraction with `q(Δθ) > q(0)`
   estimates `Δ`, with a Clopper–Pearson error that more samples reduce.
4. Accuracy is then limited by the flow, not by the number of samples; the result "will depend
   on the choice of NF and neural network architecture", and "if the tension is strong and the
   no-shift point is far from the bulk of samples, the approximation to P(0) may be a poor one".
   Flows are efficient for small to mild tensions and complement the kernel-density method of
   the same paper [src: Sect. IV.1].

**Suspiciousness and dimensionality (evidence-based).** Everything comes from one
nested-sampling run per data set and one for the combination; the sampling error is estimated by
resampling the sample weights, which adds noise to the dimensionality, and the computations are
in `anesthetic` (arXiv:2012.09554) [src: Sect. 4.2]. For Gaussian posteriors, `log S = d/2 −
(1/2)(μ_A − μ_B)(Σ_A + Σ_B)^-1(μ_A − μ_B)` [src: Handley & Lemos 2019, arXiv:1902.04029, Eq.
25]; `d − 2 log S` follows `χ²_d`, `log S` is "typically 0 ± sqrt(d/2)", overly negative values
indicate discordance and overly positive ones "suspicious concordance", and the tension
probability is the upper tail of `χ²_d` above `d − 2 log S` [src: Eq. 26]. For non-Gaussian
posteriors the same test is a proposition, not a theorem [src: Sect. IV.2], helped by Box–Cox
Gaussianisation, which preserves `S` but cannot always Gaussianise both posteriors at once
(arXiv:2012.09554) [src: Sect. 4.2]. `d` is the Bayesian model dimensionality of Eq. 13 of
arXiv:2012.09554, which needs no point estimate [src: Sect. 4.2]. Suspiciousness can be
rewritten as a difference of expected log-likelihoods, which ties it to the goodness-of-fit loss
through the DIC [src: Sect. 4.2].

**Update form, `Q_UDM` (correlated or nested data).** Compute the Karhunen–Loève modes of the A
and A+B posterior covariances; for each mode, `λ^a − 1` is the variance improvement when B is
added; keep modes with `0.2 < λ^a − 1 < 100`, the lower bound removing directions B does not
update, the upper those A does not constrain [src: arXiv:2012.09554, Sect. 4.4, Eq. 17]. The
modes can be fixed a priori from the Fisher matrix and are invariant under linear
reparameterisation, unlike principal components; the fractional Fisher information `F^a_αα/F_αα`
of each mode says which parameter a tension lives in [src: Sect. 4.4, Eq. 18].

**Hellinger tension (one-dimensional marginals, KiDS).** Heymans et al. 2021 (arXiv:2007.15632)
[src: App. G.1]:

1. Build the two marginal densities from samples twice: a histogram with a number of bins
   scaling as the square root of the number of samples, which overestimates tension
   (under-populated tails), and a Gaussian kernel density estimate with Scott's bandwidth, which
   underestimates it (smoothing); average the two Hellinger distances.
2. Invert the Gaussian relation between Hellinger distance and the difference of means, using
   the sample standard deviations, and insert the resulting mean difference in the Gaussian `τ`
   statistic to express it in σ.
3. Validation on Gaussian variates with the posterior sample sizes: systematic deviations of
   0.1σ or less up to 4σ, scatter ±0.05σ (arXiv:2007.15632) [src: App. G.1].

For KiDS-1000 3×2pt against Planck, `d_H = 0.95`, that is 3.1σ, equal to `τ` and to the S8
parameter-shift estimate [src: Sect. 3.2, App. G.1]. KiDS-Legacy applies the same measure to the
marginal mode summaries (arXiv:2503.19441) [src: Sects. 5.2, 7].

**Posterior predictive tests (correlated subsets, DES).** Doux et al. 2026 (arXiv:2610.03447)
[src: Sects. 2.2–2.3]:

1. Approximate the predictive distribution by a mixture over posterior samples, `P(d' given
   d_obs) ≈ Σ_i w_i P(d' given d_obs, θ_i)`.
2. Goodness of fit (`d'` a new realisation of the same observables or a subset): each component
   is the Gaussian likelihood `N(d'; μ_d'(θ_i), C_d'd')`.
3. Disjoint consistency (`d'` and `d` disjoint parts of a correlated data vector): each
   component is the conditional Gaussian with mean `μ_d'(θ) + C_d'd C_dd^-1 (d − μ_d(θ))` and
   covariance `C_d'd' − C_d'd C_dd^-1 C_dd'`, parameter-independent if the covariance is.
4. `Δ_PPD` is the predictive probability at lower density than the observed `d'`, estimated by
   sampling the mixture; stability checked by bootstrapping the posterior samples.
5. Interpretation: `Δ_PPD` "is not guaranteed to be uniformly distributed over [0,1] under the
   null hypothesis" and "does not constitute a p-value in a formal sense"; DES Y3 had calibrated
   its earlier PPD metric with mock data at the best fit, Y6 does not calibrate `Δ_PPD` [src:
   Sect. 2.3].

**More than two data sets.** Leizerovich 2025 (arXiv:2512.06086) generalise the
difference-in-means statistic `Q_DM` to several data sets at once, with the dominant tension
directions in the shared space; on that basis the reported DESI–Planck increase from 1.9σ (DR1)
to 2.3σ (DR2) becomes 1.18σ_eff to 1.45σ_eff [src: abstract].

### Step 5. Diagnose what the tension is
<!-- key: step-5-diagnose-what-the-tension-is -->

- **Dimensionality of the conflict.** Ong et al. 2025 read the Bayesian dimensionality of the
  conflict: DESI DR2 against DES-SN5YR in ΛCDM, 2.95 ± 0.04σ with `log S = −3.83 ± 0.03` and
  `d_G = 0.989 ± 0.073`, "a highly localised, low-dimensional conflict"; in w0waCDM, 1.56 ±
  0.03σ, `log R ≈ +3.5`, `d_G = 3.54 ± 0.14`; adding the CMB, 3.00 ± 0.08σ with `log S = −5.56 ±
  0.09` in ΛCDM, 1.50 ± 0.05σ in w0waCDM with `d_G = 5.98 ± 0.45`; with DES-Dovekie the pairwise
  tension falls to 1.96 ± 0.04σ (arXiv:2511.10631) [src: Sect. III]. Setting: PolyChord through
  Cobaya with CAMB, DESI's priors `w0 ∈ [−3, 1]`, `wa ∈ [−3, 2]`, Planck 2018 CamSpec [src:
  Sect. II].
- **Which parameters.** KL modes with their fractional Fisher information (Step 4); the
  per-data-set `χ²` along a profile (`deep/profile-likelihoods.md`).
- **Before combining.** A combination inside a model in which the inputs are in tension is the
  case `systematics.md#tension-metric-chosen-after-the-fact-or` warns about.

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

| Metric | Question answered | Needs | Prior dependence | Correlated data | Cost | Used by |
|---|---|---|---|---|---|---|
| Gaussian difference in 1D or a 2D plane | distance in a chosen subspace | means and covariances | none | no | trivial | ACT DR6, SPT-3G against DESI (Ω_m–h r_d) |
| Hellinger tension | distance between 1D marginals, Gaussian-calibrated | samples; histogram + KDE | through the marginals | no | trivial | KiDS-1000, KiDS-Legacy |
| Parameter difference with flows | full shared-space shift | two chains; a trained flow | low (non-shared parameters drop out) | no (convolution assumes independence) | flow training | DES Y6, DES Y3 |
| Update form `Q_UDM` | does adding B move A | A and A+B chains | low | yes, by construction | cheap | DES suite; KiDS-1000 table |
| Suspiciousness + dimensionality | likelihood-level conflict, prior-volume removed | nested-sampling runs of A, B, A+B | removed for Gaussian posteriors | no | three evidences | DES suite; Ong et al. 2025 |
| Bayes ratio `R` | can one parameter set fit both | evidences | proportional to prior volume | no | three evidences | DES Y1 (abandoned) |
| Posterior predictive `Δ_PPD` | is subset d' predicted by d | posterior samples, joint covariance | through the posterior | yes | mixture sampling | DES Y6 |
| Multi-set `Q_DM` | joint discordance of N data sets | means, covariances | low | not stated in the abstract | cheap | method paper |

Head-to-head results. On simulated DES Y1 shifts, eigentension, goodness-of-fit loss, parameter
differences and suspiciousness "agree with the a-priori tension, as well as amongst themselves",
while the Bayes ratio is "unsuitable" because it is "proportional to the width of the chosen
uninformative prior" and needs a problem-dependent calibration of the Jeffreys scale; on the
real DES Y1 and Planck data all four give about 2.3σ, which remains with Planck 2018
(arXiv:2012.09554) [src: Sect. 7]. On KiDS-1000 3×2pt against Planck, three estimators that do
and do not assume Gaussian marginals all give 3.1σ (arXiv:2007.15632) [src: Sect. 3.2]. The
choice of metric matters less, on these two cases, than the choice of subspace and of reference
data: compare the DES Y6 numbers of Step 3 and the 1.6σ, 2.3σ and 2.8σ CMB–BAO figures
(arXiv:2503.14452, arXiv:2503.14738, arXiv:2506.20707; abstract of each), a spread that comes from
the CMB combination.

When to use which:

- Independent surveys, a pre-registered parameter (S8): a 1D measure (Hellinger or Gaussian),
  with the full-space parameter difference beside it.
- Independent surveys, no pre-registered parameter: the full-space parameter difference, or
  suspiciousness if nested-sampling runs exist anyway; report the dimensionality.
- Same sky or shared calibration: the update form or a posterior predictive test, not a
  convolution of posteriors.
- Internal splits of one data vector: posterior predictive tests with the conditional Gaussian.
- Several external data sets in play: a look-elsewhere threshold or a multi-set statistic.

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Criterion for combining data sets | `n_σ < 3` | DES Y6 | arXiv:2601.14559 | Sect. IV.6 |
| Consistency criterion between surveys | `|ΔX| ≤ 2.6σ` (Hellinger, marginal mode) | KiDS-Legacy | arXiv:2503.19441 | Sect. 6 |
| Look-elsewhere threshold over the pairwise tests | 2.88σ | Ong et al. 2025 | arXiv:2511.10631 | Sect. III |
| Mode selection in `Q_UDM` | `0.2 < λ − 1 < 100` | DES suite | arXiv:2012.09554 | Eq. 17 |
| Hellinger estimator accuracy on Gaussian variates | ≤ 0.1σ bias up to 4σ; ±0.05σ scatter | KiDS-1000 | arXiv:2007.15632 | App. G.1 |
| Hellinger distance KiDS-1000 3×2pt against Planck | `d_H = 0.95`, 3.1σ | KiDS-1000 | arXiv:2007.15632 | App. G.1 |
| Typical spread of `log S` for consistent Gaussian data | 0 ± sqrt(d/2) | analytic | arXiv:1902.04029 | Sect. IV.2 |
| DES Y6 3×2pt against CMB, wCDM: full; S8; w–S8 | 1.3σ; 1.0σ; 2.1σ | DES Y6 | arXiv:2601.14559 | Sect. V.3 |
| DES Y6 against Planck 2018 alone, ΛCDM (Y3: 1.5σ) | 1.0σ | DES Y6 | arXiv:2601.14559 | Sect. V.2 |
| DES Y6 3×2pt against CMB (SPT + ACT + Planck), full space (Y3: 1.5σ) | 1.8σ | DES Y6 | arXiv:2601.14559 | Sect. V.2 |
| DES 3×2pt + SN + BAO against CMB | 2.5σ | DES Y6 | arXiv:2601.14559 | Sect. VI |
| P-ACT (or P-ACT-L) against DESI DR2; ACT-L against DESI DR2; Ω_m–h r_d plane | 1.6σ; 2.8σ | ACT DR6 | arXiv:2503.14452 | App. H |
| DESI DR2 against DES-SN5YR, ΛCDM: σ, `log S`, `d_G` | 2.95 ± 0.04; −3.83 ± 0.03; 0.989 ± 0.073 | Ong et al. 2025 | arXiv:2511.10631 | Sect. III |
| Same, w0waCDM: σ, `d_G` | 1.56 ± 0.03; 3.54 ± 0.14 | Ong et al. 2025 | arXiv:2511.10631 | Sect. III |
| DESI–Planck, DR1 and DR2, multi-set `Q_DM` against the reported values | 1.18σ_eff and 1.45σ_eff against 1.9σ and 2.3σ | Leizerovich 2025 | arXiv:2512.06086 | abstract |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Prior-dependent metric.** The Bayes ratio scales with the prior volume and reads extreme
  agreement or extreme tension on the Jeffreys scale "in most cases" (arXiv:2012.09554) [src:
  Sect. 7]. Test: halve and double a flat prior; a usable metric does not move.
- **Flow or KDE failure at strong tension.** The density at zero shift is poorly estimated when
  zero is far from the samples (arXiv:2105.03324) [src: Sect. IV.1]. Symptom: `n_σ` that changes
  with the architecture or the seed. Test: retrain, compare flow and KDE, check on a Gaussian
  approximation of the same chains. The benchmark accuracy of the estimators, 0.2σ generally and
  0.5σ in difficult cases, is in `results.md#tension-metrics-on-the-same-data`.
- **Non-shared parameters left in the comparison.** They cannot contribute a shift
  (arXiv:2105.03324) [src: Sect. II.1] but add dimensions to the density estimate.
  Pre-marginalise them.
- **Subspace chosen after the result.** 1.0σ, 1.3σ or 2.1σ from the same DES Y6 wCDM chains
  (arXiv:2601.14559) [src: Sect. V.3]. Test: the analysis plan names the subspace.
- **Suspiciousness p-value with non-Gaussian posteriors.** The `χ²_d` reading is exact only for
  Gaussian posteriors (arXiv:1902.04029) [src: Sect. IV.2]; Box–Cox may not Gaussianise both at
  once (arXiv:2012.09554) [src: Sect. 4.2]. Quote `log S` and `d` with their nested-sampling
  errors next to the probability.
- **`Δ_PPD` read as a p-value.** It is not uniform under the null (arXiv:2610.03447) [src: Sect.
  2.3, App.]. Projection effects can push the predictive distribution away from the observed
  data and create apparent tension for consistent data
  (`systematics.md#tension-metric-chosen-after-the-fact-or`).
- **A 1D marginal measure taken as the full story.** The Hellinger measure compares one
  marginal; a tension orthogonal to it is invisible. Report the dimensionality or a full-space
  metric beside it.
- **Reference data changed silently.** DES Y6 is 1.0σ from Planck 2018 alone and 1.8σ from the
  three-experiment CMB (arXiv:2601.14559) [src: Sect. V.2]: "the tension with the CMB" depends
  on which CMB.
- **Many pairs, no trial factor.** Use a look-elsewhere threshold, as Ong et al. do
  (arXiv:2511.10631) [src: Sect. III], or a multi-set statistic (arXiv:2512.06086) [src].

Validation as the papers do it: inject known shifts and compare with the a-priori Gaussian
tension (arXiv:2012.09554) [src: Sect. 3.1]; calibrate a sample-based estimator on Gaussian
variates of the same sample size (arXiv:2007.15632) [src: App. G.1]; bootstrap posterior samples
for a predictive metric (arXiv:2610.03447) [src: Sect. 2.3]; check the effect of the reference
data by rerunning with an alternative (arXiv:2503.14452) [src: App. H].

## Reading list
<!-- key: reading-list -->

- Method and calibration: Lemos et al. 2021 (arXiv:2012.09554), Sects. 3.1, 4.2, 4.4 and 7, for
  the synthetic-shift recipe and the choice among metrics.
- Foundation: Handley & Lemos 2019 (arXiv:1902.04029), Sect. IV.2, for the Gaussian
  suspiciousness and its tension probability.
- Foundation: Raveri & Hu 2019 (arXiv:1806.04649), for `Q_UDM` and `Q_DMAP` (formulae in
  `physics-and-methods.md#tension-metrics`).
- Method: Raveri & Doux 2021 (arXiv:2105.03324), Sects. II.1 and IV, for normalising-flow
  parameter differences and why non-shared parameters drop out.
- Method: Heymans et al. 2021 (arXiv:2007.15632), App. G.1, for the Hellinger tension and its
  calibration.
- Method: Doux et al. 2026 (arXiv:2610.03447), Sects. 2.2–2.3, for posterior predictive tests on
  correlated data.
- Application: DES Y6 3×2pt (arXiv:2601.14559), Sects. IV.6 and V, for the pre-registered
  criterion and full-space against projected values.
- Application: ACT DR6 (arXiv:2503.14452), App. H, and SPT-3G D1 (arXiv:2506.20707), Sect. II,
  for 2D Gaussian separations against BAO.
- Application: Ong et al. 2025 (arXiv:2511.10631), Sect. III, for dimensionality as a diagnostic
  of what a model extension resolves.
- Critique: Leizerovich 2025 (arXiv:2512.06086), for why pairwise figures overstate a
  multi-data-set discordance.

## Not verified
<!-- key: not-verified -->

- The eigentension method of Park & Rozo, and the S8 parameter-shift estimator of App. G.2 of
  arXiv:2007.15632, were not read.
- The Hellinger-distance formula (Eq. 14–15 of arXiv:2007.15632) did not render in the fetch;
  only the procedure is given.
- The KiDS-Legacy companion consistency paper and the metric behind its internal tests were not
  read.
- The DES Y3 calibration of its earlier posterior predictive metric (cited in arXiv:2610.03447)
  was not read; its identifier is not cited here.
- The KDE algorithm of arXiv:2105.03324 (Sect. III) is not described beyond the summary in
  `physics-and-methods.md#tension-metrics`.
- Whether Leizerovich treats correlated data sets was not read beyond the abstract.
