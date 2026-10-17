# Covariance estimation — cosmo-statistics-inference dossier

Scope: how current analyses build, correct and validate the data covariance, and how to choose
between mock-based, analytic, semi-analytic and hybrid routes and between the finite-mock
corrections; the formulae and sizes already in the reference files are referred to, not
repeated.
Snapshot: 2026-10-16.
From: KiDS-1000 methodology, Sect. 5 and Apps. D-E; DESI, DES and ACT covariance papers.

Prerequisites at L2: the Hartlap, Dodelson–Schneider, Percival 2014, Sellentin–Heavens and
Percival 2022 formulae are in
`physics-and-methods.md#sample-covariance-from-mocks-and-its-corrections`; their sizes for
typical mock counts in `results.md#size-of-the-corrections-for-typical-mock-counts`; jackknife
and bootstrap in `physics-and-methods.md#internal-estimates-jackknife-and-bootstrap`; what each
collaboration uses in `surveys-and-data.md#summary-table`. Notation here follows Percival et al.
2022 (arXiv:2108.10402): `n_s` mocks, `n_d` data points, `n_θ` parameters, `S` the sample
covariance; where Percival et al. 2014 (arXiv:1312.4841) is quoted, its `n_b`, `n_p`, `A`, `B`,
`D` are kept.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Decide which error the covariance must deliver
<!-- key: step-1-decide-which-error-the-covariance-must -->

Three different quantities are affected by an imperfect covariance, and a validation that checks
one does not check the others.

- The scatter of the best fit over data realisations, written `σ[π̂]` in DES Y3, against the
  width of the posterior read from the likelihood, `σ_π`. DES Y3 tabulates the two separately
  for every covariance effect it studies, because a covariance error can widen one without the
  other (Friedrich et al. 2021, arXiv:2012.08568) [src: Sect. 2, Table 1].
- The best-fit `χ²` and its probability to exceed. DES Y3 states that `χ²` and parameter
  constraints are "the two measures by which our final (on-shot) data analysis will be
  interpreted and judged", and therefore studies covariance errors only through them [src: Sect.
  2].
- Bias of the central value. KiDS-1000 estimates it separately (Step 4 below).

Percival et al. 2014 formalise the first distinction for finite mocks. "Three different
corrections to create unbiased error estimates exist in different situations" (arXiv:1312.4841)
[src: Sect. 7]:

1. Variance from the distribution of best fits on data independent of the mocks that built the
   covariance: the Dodelson–Schneider expression, the true error on a measurement [src: Sect. 7,
   Eq. 12].
2. Variance read from the likelihood, whether fitted to independent mocks, to the covariance
   mocks or to the data: apply `m_1` [src: Sect. 7, Eq. 18].
3. Variance from the distribution of best fits on the same mocks that built the covariance:
   these best fits scatter as `⟨p_α p_β⟩ = [(1 − D)(1 + A + B(n_p + 1))] F^-1_αβ` [src: Eq. 21],
   so the factor is `m_2 = V_αβ/⟨p_α p_β⟩ = (1 − D)^-1 m_1` [src: Eq. 22], with `D = (n_b +
   1)/(n_s − 1)`. Condition: the same mocks enter the covariance and the test.

Case 3 is the trap of the usual pipeline test, "apply any data analysis pipeline to mock data":
if all mocks were used for the covariance, "we should not expect to recover a distribution of
best-fit solutions that matches" the independent-data expressions (arXiv:1312.4841) [src: Sect.
4].

### Step 2. Choose the source of the covariance
<!-- key: step-2-choose-the-source-of-the-covariance -->

The routes in use in 2024–2026, with the procedure as each paper describes it.

**Analytic, validated by a linearised likelihood (DES Y3, arXiv:2012.08568).** The paper argues
that brute-force coverage tests on simulations fail for two reasons: a Bayesian credible region
does not contain the truth at its nominal frequency even with a perfect covariance (the
prior-volume effect), and "it is not (yet) feasible to generate enough sufficiently accurate
mock data sets"; DES Y1 had 18 realistic simulated data sets for pipeline validation [src: Sect.
2]. The strategy is instead:

1. Build the fiducial analytic covariance (Gaussian, connected four-point and super-sample
   terms) with exact finite angular-bin averaging, which Y1 had approximated by computing a fine
   binning and re-summing [src: Sect. 2].
2. Linearise the model in all 28 parameters, so that Bayesian intervals have a frequency
   interpretation and thousands of simulated analyses cost no MCMC [src: Sect. 2].
3. For each effect left out or approximated (bin averaging, connected four-point function,
   curved sky, non-Limber and RSD, mask geometry, non-Poissonian shot noise, cosmology
   dependence, effective shape noise), compute the change of `⟨χ²⟩`, `σ[χ²]`, `σ[π̂]` and `σ_π`,
   analytically or with lognormal simulations rather than N-body ones [src: Sects. 2, 4.3, 6].

The justification for lognormal rather than N-body validation: for DES-like analyses the
trispectrum term is negligible, because the smallest scales are cut for modelling reasons and
the small-scale covariance is dominated by shot and shape noise [src: Sect. 2]. Within this
framework super-sample covariance and trispectrum also have negligible impact for the Y3 setup
[src: Sect. 2].

**Analytic, validated against lognormal mocks with survey realism (KiDS-1000, Joachimi et al.
2021, arXiv:2007.01844).** Flask + Salmo lognormal mocks are run in three set-ups: rectangular
mask with uniform depth (Buceros), the real footprint (Cygnus), and the real footprint with
depth variations (Egretta) [src: Sect. 5.3]. The mocks validate the Gaussian terms; the
lognormal four-point function is "less accurate", acceptable because those terms are subdominant
[src: Sect. 5.3]. The analytic model uses pair counts measured on the real data, which is how it
captures most survey-property effects [src: Sect. 5.3].

**Semi-analytic, calibrated on the data jackknife (DESI BAO, RascalC).** The procedure for DESI
DR1 (Rashkovetskyi et al. 2024, arXiv:2404.03007) [src: Sect. 2.1]:

1. From the random catalogue and the measured two-point function, RascalC builds models of both
   the full covariance and the jackknife covariance; the code integrates the disconnected
   four-point terms with the survey geometry.
2. Repeated overdensities at one position are replaced by the shot-noise approximation `(δ_i)² ≈
   (α_SN/n_i)(1 + δ_i)` [src: Eq. 2.4], whose Poisson expectation is `α_SN = 1`; `α_SN` (one per
   tracer) is the single free parameter that stands in for the missing non-Gaussian
   contributions.
3. `α_SN` is fitted by matching the jackknife model to the jackknife covariance measured on the
   data, and inserted into the full model. An alternative pipeline fits the full model to a mock
   sample covariance; it is used only for tests [src: Sect. 2.1].
4. The advantage stated by the authors: the jackknife pipeline "only requires mocks for the
   initial validation", and then produces covariances for new set-ups without new simulations
   [src: Sect. 2.1].

DESI DR2 BAO uses RascalC "in the same way as for the DESI DR1 BAO analysis", with shot-noise
rescaling calibrated by jackknife resampling, and notes that covariance estimation for DR2 is
"less challenging than DR1" because the footprint is simpler and completeness higher (DESI
Collaboration 2025, arXiv:2503.14738) [src: Sect. III.1].

**Mock-based, rescaled to a semi-analytic matrix (DESI DR1 full shape).** Described in
`systematics.md#analytic-covariance-missing-terms-and-cosmology`: the mock-realism rescaling is
larger than the finite-mock correction there.

### Step 3. Correct for the finite number of mocks, for the likelihood actually used
<!-- key: step-3-correct-for-the-finite-number-of-mocks -->

The correction depends on the likelihood it is combined with.

- Gaussian likelihood with `S` plugged in: Hartlap scaling of the precision, plus `m_1` on the
  parameter covariance (Step 1), or the single matrix `S'` of Percival et al. 2022, which
  "matches the method proposed in Percival et al. (2014), replacing one of the approximations
  used there with an exact expression" (arXiv:2108.10402) [src: Sect. 7, Eq. 56].
- t-distribution posterior: the matching-prior form `[1 + χ²/(n_s − 1)]^(−m/2)` with `χ²`
  computed from `S^-1` itself; "this expression does not require any extra factors of h, or
  other terms" (arXiv:2108.10402) [src: Sect. 7, Eqs. 52–55].
- Mattera 2026 (arXiv:2606.18446), with an expected negative log-likelihood loss: the Hartlap
  covariance scaling is the optimum under the Gaussian plug-in likelihood, "whereas the unscaled
  sample covariance is optimal under the Sellentin–Heavens likelihood", so that "an additional
  Hartlap-type global scaling is not favoured once covariance uncertainty is marginalised"
  [src]. Rule: never apply the Hartlap factor and the t-distribution together.

How the options perform on the same mock experiment (Percival et al. 2022, arXiv:2108.10402)
[src: Sect. 6]: a DES 5-year-like tomographic shear vector of 450 points (`ξ±`, 5 source bins,
5000 deg²), 1000 Gaussian realisations around `(Ω_m, σ8, w0) = (0.3156, 0.831, −1)`, covariances
drawn from a Wishart distribution, analysed with CosmoLike. With `n_s = 650`, `n_θ = 4`,
contours from the Sellentin–Heavens posterior scatter visibly around those from the true
covariance, the Dodelson–Schneider effect seen directly [src: Sect. 6, Fig. 3]. In the 3D
parameter-space coverage test, the matched prior reaches "approximately 68% and 95%", and
"simply re-scaling the Gaussian log-likelihood in the manner advocated by Percival et al.
(2014)" is "also close" [src: Sect. 6, Fig. 4]. The Hartlap-corrected Gaussian and the
Sellentin–Heavens posterior are plotted on the same figure as functions of `n_s`; their values
were not transcribed.

Limits stated by the authors: the derivation assumes a linearised model; the results "will not
be valid for arbitrary non-linear models or reparametrisations"; the matching prior depends on
`n_s`, `n_d` and `n_θ`, which "conflict[s] with the Bayesian notion of the prior as an
expression of the state of knowledge" (arXiv:2108.10402) [src: Sect. 8].

Compression interacts with the correction. With a t-distribution posterior, linearly compressing
to `n_c = n_θ` numbers with `M = F_S^-1 (dμ/dθ)^T S^-1` [src: Eq. 70] returns a parameter
covariance `(n_s − 1)/(m − n_d − 2) F_S^-1` [src: Eq. 74], the value averaged over data
realisations rather than the one for the observed realisation; "data compression works
differently than when analysing using a Gaussian posterior for which linear compression is
sufficient" (arXiv:2108.10402) [src: App. C].

### Step 4. Validate
<!-- key: step-4-validate -->

1. **Compare matrices with measures whose noise expectation is known.** RascalC uses three,
   computed with the inverse of the model (not of the noisier mock matrix) (arXiv:2404.03007)
   [src: Sect. 2.2]: the Kullback–Leibler divergence `D_KL(C_R^-1, C_S) = (1/2)[tr(C_R^-1 C_S) −
   N_bins − ln det(C_R^-1 C_S)]` [src: Eq. 2.16], used to fit `α_SN`; the directional RMS
   difference `R_inv = sqrt{tr[(C_R^-1 C_S − I)²]/N_bins}` [src: Eq. 2.17]; and `χ²_red =
   tr(C_R^-1 C_S)/N_bins` [src: Eq. 2.18], distributed as a reduced χ² with `N_bins (n_S − 1)`
   degrees of freedom if the model is right, and sensitive to overall scaling. The first two are
   not zero even for a perfect model, so their expected values for `n_S` Gaussian samples are
   computed theoretically and by Monte Carlo (10 000 chunks), the theoretical value kept unless
   the two differ by more than 3σ [src: Sect. 2.2].
2. **Project into parameter space.** Agreement in observable space is not the criterion; DESI
   projects both matrices through the Fisher matrix of the BAO, ShapeFit and full-modelling
   parameters (arXiv:2404.03007) [src: Sects. 2.3, 7.2].
3. **Test the χ² distribution, with the effective number of parameters.** KiDS-1000 builds the
   distribution of `χ²_min` from 1000 mock data vectors through the full pipeline; it is well
   fitted by a χ² distribution with a free mean, and stays χ²-shaped even for a model sabotaged
   with two redshift distributions shifted by 5σ of their prior, which is then incompatible with
   the baseline at `p < 10^-5` (arXiv:2007.01844) [src: Sect. 6.3, Fig. 18]. The free parameter
   is `k_dof,eff = N_d − N_Θ,eff`. Three estimators of `N_Θ,eff` are compared: `N_Θ,var =
   2[⟨(χ²)²⟩ − ⟨χ²⟩²]` over the posterior [src: Eq. 44], `N_Θ,like = ⟨χ²⟩ − χ²_min` [src: Eq.
   45], `N_Θ,post = ⟨χ²⟩ − χ²(MAP)` [src: Eq. 46]; the adopted one is `(N_Θ,like + N_Θ,post)/2`
   [src: Sect. 6.3]. Conditions under which the plain `N_d − N_Θ` holds, none of which hold in
   cosmology: normally distributed data, parameters entering linearly, priors not restrictive
   [src: Sect. 6.3]. DES Y3 reaches the same point with its linearised likelihood: 28
   parameters, 13 with Gaussian priors, expected `⟨χ²⟩ ≈ 507.6`, that is `N_param,eff ≈ 23.4`
   (arXiv:2012.08568) [src: Sect. 2].
4. **Bound the bias of the central value.** KiDS-1000 draws data vectors `d_i = μ + L_i z` with
   the same standard-normal `z` and the Cholesky factors of two candidate covariances, so that
   the difference has variance `σ²_ΔCov,α = Σ_i (L_B,αi − L_A,αi)²` [src: Eq. 42]; between the
   simple and realistic analytic set-ups, `σ_ΔCov,α/μ_α` is between 4 × 10^-3 and 10^-4 for
   galaxy–galaxy lensing and below 5 × 10^-5 for cosmic shear, "well below the sensitivity of
   the current generation of surveys" (arXiv:2007.01844) [src: Sect. 5.3].
5. **Run the inference with each candidate covariance on the same synthetic data.** KiDS-1000
   runs analytic and mock (5000 realisations) covariances, each in the simple and the realistic
   set-up, through the full pipeline; none has a significant impact on the marginal constraints
   (arXiv:2007.01844) [src: Sect. 7, Table 5, IDs 9–12].

### Step 5. Cosmology at which the covariance is evaluated
<!-- key: step-5-cosmology-at-which-the-covariance-is -->

DES Y3 computed the covariance at 100 cosmologies drawn from a chain around the fiducial data
vector. The differences add scatter to the maximum-posterior parameters, about 3% for Ω_m and σ8
and 5% for w, while "the width of the derived parameter constraints hardly changes"; "re-running
the analysis with a covariance updated to the best-fit parameters does not mitigate this effect"
(arXiv:2012.08568) [src: Sect. 2]. Iteration at the best fit, the usual remedy, removes the
error of a wrong fiducial cosmology but not this scatter. DES Y6 still recomputes at the blind
MAP (`surveys-and-data.md#des`); the two statements address different errors.

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

| Route | Assumes | Buys | Costs | Used by | Head-to-head result |
|---|---|---|---|---|---|
| Mock sample covariance, Gaussian likelihood with Hartlap + `m_1` (or `S'`) | Gaussian data, independent mocks, linear model | survey realism if the mocks have it | noise growing with `n_d/n_s`; mock realism limited to what the mocks match | DESI DR1 full shape (rescaled, below) | reaches nominal coverage in the 450-point shear test with `n_s = 650` (arXiv:2108.10402) [src: Sect. 6] |
| Mock sample covariance, matching-prior t-posterior | as above | coverage-matched credible intervals, no extra factors | prior depends on `n_s, n_d, n_θ`; not valid for arbitrary non-linear models; compression subtleties | not found in a 2025–2026 collaboration analysis (`open-questions.md#covariance-mocks-analytic-or-neither`) | ≈68%, ≈95% coverage in the same test [src: Sect. 6] |
| Analytic (halo model, Gaussian + connected + super-sample) | correct survey-geometry treatment; trispectrum model; one fiducial cosmology | no noise, cheap to iterate | missing or approximated terms, found only by comparison | DES Y3/Y6, KiDS-1000/Legacy | KiDS-1000: analytic against 5000 mocks, simple and realistic geometry, no significant change of marginal constraints (arXiv:2007.01844) [src: Sect. 7] |
| Semi-analytic, jackknife-calibrated (RascalC) | non-Gaussianity captured by one shot-noise rescaling per tracer | adapts to the measured clustering; mocks needed only for validation | shot-noise rescaling limited where the four-point term matters (dense samples) | DESI DR1 and DR2 BAO | BAO error bars within 8% of a 1000-mock covariance whose own expected scatter is about 2.4% (arXiv:2404.03007) [src: Sect. 8] |
| Mock covariance rescaled to a data-tuned semi-analytic one | the semi-analytic matrix carries the data's realism | survey effects of fibre assignment | a rescaling larger than the finite-mock correction | DESI DR1 full shape | see `systematics.md#analytic-covariance-missing-terms-and-cosmology` |
| Internal jackknife or bootstrap, uncorrected | regions are independent realisations | no mocks | scale-dependent bias, no super-sample term | not used for a 2025–2026 headline | `physics-and-methods.md#internal-estimates-jackknife-and-bootstrap` |
| Sub-sample covariance with smoothed correlation matrix (Lyα forest) | smoothing restores invertibility | data-driven | "does not fully capture the true correlation structure" | DESI Lyα (as described in arXiv:2606.04089) [src] | a mock-conditioned multi-eigenbasis denoiser improves matrix metrics and posteriors against a many-mock reference (arXiv:2606.04089) [src] |
| Shrinkage with marginalised intensity | a spherical target; prior on the shrinkage intensity | conditioning; propagates uncertainty on the amount of regularisation | one more inferential layer | method paper only | Monte Carlo experiments only (arXiv:2606.18446) [src] |

Binning is part of the choice. With the Gaussian likelihood and a mock covariance, the corrected
error grows with the number of bins, because the covariance-noise terms grow with `n_b`; with
very wide bins information is lost by averaging, so there is an optimum, which is "only an
optimal bin size if you want to retain Eq. (1) as the likelihood equation" (Percival et al.
2014, arXiv:1312.4841) [src: Sect. 7]. For BOSS, after all corrections, the isotropic BAO error
from the mocks is "quite independent of bin size over a broad range", and bins up to 12 h^-1 Mpc
in ξ(s) lose no significant accuracy [src: Sect. 7]. The corrections for joint monopole and
quadrupole BAO and RSD fits were "quite large" [src: Sect. 7].

Which survey effects need mocks. In KiDS-1000, the realistic footprint and depth variations
raise the square root of the covariance diagonal by about 20%, falling to about 10% in the
highest source-bin combinations of cosmic shear, through the number of pairs (shape and shot
noise); the analytic model captures most of this because it uses the measured pair counts, and
fails mainly for the mixed noise–sample-variance term of galaxy–galaxy lensing, which ignores
survey geometry (arXiv:2007.01844) [src: Sect. 5.3]. In DESI, fibre assignment and its weights
are "the main factor" separating the shot-noise rescaling of the mocks from that of the data
(arXiv:2404.03007) [src: Sect. 8]. Mocks matched only to one- and two-point statistics (EZmocks)
are not a perfect reference for a quantity set by three- and four-point functions, so "matching
the mocks perfectly is not necessarily a reasonable goal" [src: Sect. 8].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Realistic simulated data sets available for pipeline validation | 18 | DES Y1 | arXiv:2012.08568 | Sect. 2 |
| Parameters, of which with Gaussian priors | 28, 13 | DES Y3 3×2pt | arXiv:2012.08568 | Sect. 2 |
| Expected `⟨χ²⟩` with a perfect covariance; effective parameters | 507.6; ≈ 23.4 | DES Y3 3×2pt | arXiv:2012.08568 | Sect. 2, Table 1 |
| Excess of `χ²` at maximum posterior from all neglected effects in quadrature | ≈ 4% (Δχ² ≈ 20.3) | DES Y3 3×2pt | arXiv:2012.08568 | Sect. 2 |
| Neglecting exact angular-bin averaging: `⟨χ²⟩`; posterior width of Ω_m, σ8, w | 402.1 instead of 507.6; +7.4%, +8.3%, +7.4% (scatter +0.8% to +1.0%) | DES Y3 | arXiv:2012.08568 | Table 1 |
| Connected four-point function: change of posterior width | −0.8% to −0.9% | DES Y3 | arXiv:2012.08568 | Table 1 |
| Covariance cosmology: extra scatter of the best fit | ≈ 3% (Ω_m, σ8), ≈ 5% (w) | DES Y3 | arXiv:2012.08568 | Sect. 2 |
| Data-vector length; sampled parameters | 120 and 12 (shear); 310 and 20 (joint) | KiDS-1000 | arXiv:2007.01844 | Sect. 6.3 |
| `N_Θ,eff` (adopted) against the `⟨χ²⟩` calibration | 4.5 against 4.5 (shear); 9.1 against 8.7 (shear + GGL) | KiDS-1000 | arXiv:2007.01844 | Table 4 |
| Quality `α_p` of the naive `N_Θ` against the adopted estimator | 22.6 against 0.4 (shear); 32.8 against 1.6 (shear + GGL) | KiDS-1000 | arXiv:2007.01844 | Table 4 |
| Change of reduced `χ²` from the effective degrees of freedom | 7% (shear only) | KiDS-1000 | arXiv:2007.01844 | Sect. 6.3 |
| Mock realisations for the `χ²_min` distribution; for the mock covariance | 1000; 5000 | KiDS-1000 | arXiv:2007.01844 | Sects. 6.3, 7 |
| Survey footprint and depth: increase of sqrt(diagonal) | ≈ 20%, falling to ≈ 10% | KiDS-1000 lensing band powers | arXiv:2007.01844 | Sect. 5.3 |
| Analytic against mock standard deviation at small angular frequency | analytic low by typically 10%; GGL up to +20% on large scales | KiDS-1000 | arXiv:2007.01844 | Sect. 5.3 |
| Bias of the data vector from covariance differences, `σ_ΔCov/μ` | 4 × 10^-3 to 10^-4 (GGL); < 5 × 10^-5 (shear) | KiDS-1000 | arXiv:2007.01844 | Sect. 5.3, Eq. 42 |
| S8 1σ interval width, analytic or mock, simple or realistic geometry | 0.054–0.057 (marginal HPD); 0.057–0.072 (PJ-HPD) | KiDS-1000 synthetic | arXiv:2007.01844 | Table 5, IDs 9–12 |
| BAO error bars, RascalC against 1000-mock sample covariance | ≤ 8%; ≈ 5% without pre-reconstruction BGS | DESI DR1 mocks | arXiv:2404.03007 | Sect. 8 |
| Expected scatter of errors from 1000 mocks | ≈ 2.4% | DESI DR1 | arXiv:2404.03007 | Sect. 8 |
| Monte Carlo chunks for the reference values of the comparison measures | 10 000 | DESI DR1 | arXiv:2404.03007 | Sect. 2.2 |
| Coverage test set-up | `n_d = 450`, `n_s = 650`, `n_θ = 4`, 1000 realisations | DES 5-year-like shear | arXiv:2108.10402 | Sect. 6 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Validating against the mocks that built the covariance.** The best fits then scatter by `(1
  − D)` times less than for independent data; use `m_2` (Eq. 22 of arXiv:1312.4841) or hold out
  mocks. Test: split the mock set.
- **Hartlap on top of the t-distribution.** Under the Sellentin–Heavens likelihood the unscaled
  sample covariance is the optimum (arXiv:2606.18446) [src]; the matching-prior form also takes
  `S` unscaled (arXiv:2108.10402) [src: Sect. 7]. Symptom: intervals wider than both the
  Gaussian `S'` and the t-distribution results. Test: compare with `S'` from the same mocks.
- **Reading the plain `N_d − N_Θ` as the degrees of freedom.** In KiDS-1000 it scores `α_p ≈ 23`
  and 33, worse than assuming no free parameter at all (arXiv:2007.01844) [src: Table 4, Sect.
  6.3]. Symptom: reduced `χ²` systematically above one. Test: the `χ²_min` distribution from
  mocks or from the posterior predictive distribution; combine several realisations, since one
  maximum-likelihood estimate of `N_Θ,eff` is noisy [src: Sect. 6.3]. The optimiser may be the
  bottleneck: KiDS-1000 could not run fast enough optimisers on many mocks for the joint
  analysis [src: Sect. 6.3].
- **A brute-force coverage test of the covariance.** With a non-linear model and informative
  priors, credible regions miss the truth at the nominal rate even with a perfect covariance
  (arXiv:2012.08568) [src: Sect. 2]. Test the covariance with a linearised likelihood, or
  separate prior-volume effects first (`systematics.md#projection-prior-volume-effects`).
- **Approximate angular-bin averaging.** The largest single effect on `χ²` found for DES Y3,
  with posterior widths changed by about 7%–8% (arXiv:2012.08568) [src: Table 1]. Test: exact
  bin-averaged Gaussian and shot-noise terms.
- **Mixed noise–sample-variance term without survey geometry.** Up to 20% on large-scale
  galaxy–galaxy lensing in KiDS-1000 (arXiv:2007.01844) [src: Sect. 5.3]. Test: mocks with the
  real footprint, Cygnus against Buceros in that paper.
- **Fibre assignment absent from the mocks.** Changes the calibrated shot-noise rescaling
  between mocks and data (arXiv:2404.03007) [src: Sect. 8]. Test: compare the rescaling on mocks
  with and without fibre assignment.
- **Dense tracers in a one-parameter non-Gaussian model.** RascalC is least consistent for BGS,
  where the four-point term matters most; the BGS EZmocks are also a weaker reference
  (arXiv:2404.03007) [src: Sect. 8].
- **Expecting best-fit iteration to cure covariance-cosmology errors.** It does not remove the
  extra best-fit scatter (arXiv:2012.08568) [src: Sect. 2].
- **Compressing before a t-distribution analysis and reading the result as the full-data
  interval** (arXiv:2108.10402) [src: App. C].
- **Non-invertible sub-sample covariances** (long Lyα vectors): smoothing restores invertibility
  without the right correlation structure (arXiv:2606.04089) [src].

Pass criteria stated by the papers: `|α_p| < 1`, the bias of the degrees-of-freedom estimator
below its statistical error (arXiv:2007.01844) [src: Sect. 6.3]; comparison measures within the
spread expected for `n_S` Gaussian samples, from theory unless theory and Monte Carlo differ by
more than 3σ (arXiv:2404.03007) [src: Sect. 2.2]; parameter-space errors within a few per cent
of the mock covariance, against the 2.4% sampling floor of 1000 mocks [src: Sect. 8].

## Reading list
<!-- key: reading-list -->

- Foundation: Percival et al. 2014 (arXiv:1312.4841), Sects. 4 and 7, for which correction
  applies to which error, including `m_2`, and for binning.
- Foundation: Percival et al. 2022 (arXiv:2108.10402), Sects. 6–7 and App. C, for the
  recommended posterior, its coverage test and its interaction with compression.
- Method: Friedrich et al. 2021, DES Y3 (arXiv:2012.08568), Sect. 2 and Table 1, for validation
  by a linearised likelihood and the budget of covariance effects.
- Method: Joachimi et al. 2021, KiDS-1000 (arXiv:2007.01844), Sects. 5.3, 6.3 and 7, for
  mock-against-analytic tests with survey realism and the effective degrees of freedom.
- Method: Rashkovetskyi et al. 2024 (arXiv:2404.03007), Sects. 2 and 8, for the
  jackknife-calibrated semi-analytic route and matrix-comparison measures.
- Application: DESI DR2 BAO (arXiv:2503.14738), Sect. III.1, for current semi-analytic practice.
- Critique: Mattera 2026 (arXiv:2606.18446), for why the scalar correction depends on the
  likelihood.
- Critique: Turner 2026 (arXiv:2606.04089), for the limits of smoothed sub-sample covariances in
  the Lyα forest.

## Not verified
<!-- key: not-verified -->

- The original Friedrich & Eifler 2018 precision-matrix proposal: its identifier was not found
  by the searches of this run; it is described only as summarised in arXiv:2108.10402 [src:
  Sect. 7].
- The coverage values of the Hartlap-corrected Gaussian and of the Sellentin–Heavens posterior
  in Fig. 4 of arXiv:2108.10402 were not transcribed.
- The DES Y6 and KiDS-Legacy covariance validations beyond what `surveys-and-data.md` records;
  the ACT DR6 Monte Carlo correction in detail.
- The distribution of probabilities to exceed as an alternative covariance test (Hall & Taylor
  2019, cited in arXiv:2012.08568) was not read.
- Euclid preparation papers on the non-Gaussian two-point likelihood and on covariance
  validation (leads in `open-questions.md#not-verified`).
