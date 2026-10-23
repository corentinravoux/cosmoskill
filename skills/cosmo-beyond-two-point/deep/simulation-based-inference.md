# Simulation-based inference — cosmo-beyond-two-point dossier

Scope: how a simulation-based (implicit-likelihood) analysis of a
beyond-two-point statistic is built and validated (training-set design,
learned compression, posterior or likelihood estimation, ensembles, coverage
tests, misspecification diagnostics), and how to choose between neural
posterior and neural likelihood estimation, between compression losses, and
between ways of treating data that fall outside the training distribution.
Snapshot: 2026-10-17.
From: Beyond-2pt challenge (arXiv:2405.02252), Sect. V.4 (SBI P & B);
Leclercq 2025 (arXiv:2509.13435), Sect. 6.4; SimBIG (arXiv:2211.00660) and
the DES Y3 SBI series (arXiv:2606.11309).

Already in L2, not repeated here: the founding papers (DELFI, IMNN, score
compression, SBC, TARP) in `physics-and-methods.md#method`; the SimBIG
training and test sets in `physics-and-methods.md#simbig`; sensitivity to
gravity solver, halo finder and HOD in
`systematics.md#sensitivity-to-the-simulation-ingredients`; the
statistic-dependent robustness table in
`systematics.md#robustness-is-statistic-dependent`; the DES Y3
post-unblinding repair in `systematics.md#simulation-suite-fidelity-and-coverage`;
results in `results.md#simulation-based-inference-on-galaxy-clustering` and
`results.md#higher-order-weak-lensing`.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Design the training set
<!-- key: step-1-design-the-training-set -->

The training set is a sample of pairs (θ, x), θ the parameters and x the
summary, drawn from a simulation sampling distribution p^sim(θ) times the
forward model p(x|θ) [src: arXiv:2405.02252, Sect. V.4.3; arXiv:2606.11309,
Sect. 2.2]. Two designs are in use.

- **Latin hypercube with nested HOD draws (galaxy clustering).** The
  Beyond-2pt SBI entry uses the 2000 Quijote high-resolution LH boxes
  (1024³ particles, 1 h⁻¹Gpc), 10 HOD draws each, 20 000 catalogues split
  1500 / 200 / 300 simulations for training, validation and test
  [src: arXiv:2405.02252, Sects. V.4.2–V.4.3]. Cosmological priors are the
  hypercube bounds: Ω_m U[0.1, 0.5], σ8 U[0.6, 1.0], Ω_b U[0.03, 0.07],
  n_s U[0.8, 1.2], h U[0.5, 0.9] (Eq. 26). The HOD has nine parameters
  (Zheng et al. five plus assembly, concentration and velocity biases)
  [src: Sect. V.4.2, Table 3]. The centres of the log M_min, log M_0 and
  log M_1 priors are moved with cosmology to match the target number
  density, with widths ±0.15, ±0.2, ±0.3; the stated reason is to spend
  simulations only where they are "loosely consistent with the data" [src:
  Sect. V.4.3]. The number density n̄ is appended to the data vector: it
  adds no constraining power but stabilises the analysis when n̄ varies
  widely across the hypercube [src: Sect. V.4.1, footnote 22].
- **Active learning plus prior draws (weak lensing).** The Gower Street
  suite has 791 simulations [src: arXiv:2403.02314, Sect. 4.2]. Ω_m and σ8
  were placed by active learning: first following existing DES constraints,
  then, after a blind power-spectrum analysis, where the ensemble of density
  estimators disagreed most, with an exclusion zone around used values; the
  other parameters were drawn from priors with Sobol and Halton sequences,
  not i.i.d. [src: Sects. 2.5, 4.2]. Those priors are n_s ~ N(0.9649,
  0.0063) (Planck with the width ×1.5), h ~ N(0.7022, 0.0245) (between
  SH0ES and Planck), Ω_b h² ~ N(0.02237, 0.00015), w ~ N(−1, 1/3) truncated
  to −1 < w < −1/3 except for about 64 early runs with w < −1, and
  log m_ν ~ U[log 0.06, log 0.14] after the first 192 runs [src: Sect. 4.2].

Parameters drawn from a prior and left out of the density estimator are
marginalised implicitly, with their simulated distribution acting as the
prior [src: arXiv:2403.02314, Sect. 2.5].

### Step 2. Compress
<!-- key: step-2-compress -->

| Scheme | Loss and output | Used by | Reason given | Place read |
|---|---|---|---|---|
| None | full 301-element P_ℓ + n̄ | SimBIG P_ℓ | a regression-network compression gave no significant difference for P_ℓ | arXiv:2211.00660, Sect. III.5 |
| Regression (MSE) | f_i(t_i) trained to predict θ_j by mean-square error, averaged over data products with weights from validation losses (Eqs. 29–30) | DES Y3, Jeffrey et al. | converges to the posterior mean; locally equivalent to MOPED; optimal when the parameters are Gaussian distributed | arXiv:2606.11309, Sect. 6.2.1 |
| VMIM | F* = argmax I(Θ; F(x)) = argmin h(Θ|F(x)) (Eq. 9), estimated as −⟨ln q̃(θ_i|F(x_i))⟩ (Eq. 10), with q̃ a density network trained jointly with F | DES Y3 hybrid | maximises mutual information rather than one moment of the posterior | arXiv:2606.11309, Sect. 3.2 |
| VMIM + VICReg | adds variance, covariance and invariance terms (Eqs. 11–14), weights set to unity, in the final step only | DES Y3 hybrid | the summary space becomes "substantially easier" for the density estimator to condition on | arXiv:2606.11309, Sect. 3.4 |

Here I(Θ; F(x)) is the mutual information between parameters and compressed
data, h the differential entropy, and q̃ the density network of the loss.
The DES Y3 hybrid chain (arXiv:2606.11309): the 440-element E/B C_ℓ vector goes to 10 numbers
through a fully connected network (ten layers of 256); each of three map
patches (eight channels of 512² pixels) goes to 4 numbers through a CNN;
four restarts give 88 summaries, compressed to 7 [src: Sect. 6.2]. The
surrogate q̃ is a mixture of four Gaussians with one hidden layer of 100,
because simpler networks balanced the optimisation between compressor and
density estimator [src: same]. Inputs are standardised and augmented with
Gaussian noise of 10⁻³ times their scatter at each epoch [src: same].

### Step 3. Estimate the posterior or the likelihood
<!-- key: step-3-estimate-the-posterior-or-the-likelihood -->

- **NPE** trains q_φ(θ|x) by maximising Σ_i log q_φ(θ_i|x_i), which
  minimises the KL divergence to the true posterior [src: arXiv:2211.00660,
  Sect. III.5; arXiv:2405.02252, Sect. V.4.3]. Sampling is direct and cheap
  but tied to one prior [src: arXiv:2606.11309, Sect. 2.2].
- **NLE** trains q_φ(t|θ) with the loss U(φ) = −Σ_i ln q(t_i|θ_i; φ)
  (arXiv:2606.11309, Eq. 2; arXiv:2403.02314, Eq. 3), then samples the
  posterior with an ordinary MCMC over any prior [src: arXiv:2606.11309,
  Sects. 2.2, 6.3].

Settings read:

| Analysis | Estimator | Architecture and training | Place read |
|---|---|---|---|
| SimBIG P_ℓ | NPE, one MAF (sbi) | 6 MADE blocks, 9 hidden layers, 186 units; Adam, learning rate 5 × 10⁻⁴; 90/10 split; stop after 20 epochs without validation gain; flows of similar validation loss agree to ≲ 5% | arXiv:2211.00660, Sect. III.5 |
| Beyond-2pt SBI P + B | NPE, ensemble of MAFs (sbi) | 200 networks per statistic over width, depth, learning rate and batch size; the 10 with best validation loss mixed with equal weights | arXiv:2405.02252, Sect. V.4.3 |
| DES Y3 (Jeffrey et al.) | NLE, pydelfi | four MAFs (3, 5 or 6 MADEs, two hidden layers of 40 or 50); MDNs for validation only, because MAFs behave better at hard prior edges such as w ≈ −1 | arXiv:2403.02314, Sect. 2.2 |
| DES Y3 hybrid | NLE, ltu-ili | eight MAFs, hidden size 200, 6–9 transformations, independent initialisations; 30% held out, early stopping; affine-invariant MCMC on the learned likelihood | arXiv:2606.11309, Sect. 6.3 |

The DES Y3 hybrid analysis trains the compressors on 9 264 mocks (three
noise realisations of 3 088), uses a fourth realisation for early stopping,
and keeps a fifth one of 3 088 mocks, never seen by the compressors, to
train and validate the likelihood; overfitting of the compressor then only
widens the posterior instead of biasing it [src: arXiv:2606.11309,
Sect. 6.2].

### Step 4. Validate the calibration
<!-- key: step-4-validate-the-calibration -->

- **Rank (SBC) histograms.** On held-out simulations the rank of the true
  value within each marginal posterior should be uniform within Poisson
  scatter; uniformity "suggests (but does not guarantee)" accurate marginals
  [src: arXiv:2405.02252, Sect. V.4.4, Fig. 11].
- **Joint coverage (TARP).** For θ_test drawn from a prior, run forward
  model, compressor and inference, and count how often θ_test falls inside
  each credible region; DES Y3 does this in the joint (Ω_m, S8, w) space,
  with bootstrap error bands [src: arXiv:2606.11309, Sect. 7.1]. Because
  TARP needs posterior samples and the MCMC needs an analytic prior, while
  the active-learning p^sim has none, the test prior is a truncated Gaussian
  fitted to p^sim and sampled by rejection from the simulation parameters;
  the simulation of each θ_test is removed from the likelihood training
  [src: same].
- **Expected coverage.** The quantity tested is
  E_{p(θ,x)}[1(θ ∈ Θ_p̂(1−α))] (Hermans et al. 2021, arXiv:2110.06581,
  Eq. 2), with Θ_p̂(1−α) the 1−α highest-posterior-density region; curves
  above the diagonal are conservative, below overconfident [src: Sects. 2.2,
  3.4]. Divergence metrics such as a classifier two-sample test cannot tell
  an overconfident from a conservative approximation (both give AUROC = 0.7
  in their example) [src: Sect. 2.2].
- **Ensemble agreement.** Independently trained estimators converge as the
  number of simulations grows; disagreement signals too few simulations
  [src: arXiv:2403.02314, Sect. 2.4.2].

### Step 5. Test against other simulators and the data
<!-- key: step-5-test-against-other-simulators-and-the -->

- **Changed forward model.** Train on one halo finder and test on the other
  (FoF and Rockstar for Quijote): the Beyond-2pt SBI entry repeated its rank
  test on the FoF hypercube and found consistent results [src:
  arXiv:2405.02252, Sect. V.4.4]. The SimBIG criterion is the distribution of
  (μ − θ_fid)/σ, μ and σ the posterior mean and standard deviation, which
  must agree between test sets made with different simulators [src:
  arXiv:2507.03086, Sect. II.2.4].
- **Posterior variability on the data.** Estimators with similar validation
  losses should give similar posteriors for in-distribution data; a large
  spread on the observation flags it as out of distribution. SimBIG
  formalises this as a score D_v from pairwise KL divergences between
  posteriors of different architectures [src: same].
- **Data inside the simulation cloud.** DES Y3 checks before unblinding that
  the compressed data lie inside the cloud of compressed simulations (see L2)
  [src: arXiv:2606.11309, Sect. 7.4].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### NPE or NLE
<!-- key: npe-or-nle -->

The galaxy-clustering analyses use NPE; the DES lensing analyses use NLE.
The DES reasons: the simulation distribution can differ from the analysis
prior, which matters when simulations are expensive and placed by active
learning; the prior can be changed after the simulations exist; and
simulations can be added where the estimators disagree [src:
arXiv:2403.02314, Sect. 2.5; arXiv:2606.11309, Sect. 2.2]. The cost is an
MCMC on the learned likelihood and a need to keep the simulated support
wider than the prior: the hybrid analysis trains on −1.05 < w < −0.3 and
applies the hard w > −1 prior afterwards to avoid artefacts at a training
boundary, checking that posteriors and coverage do not depend on the cut
[src: arXiv:2606.11309, Sect. 6.3]. With NPE the prior is whatever the
training set was, hypercube bounds included [src: arXiv:2405.02252,
Sect. V.4.3]. No head-to-head comparison of NPE and NLE on the same
cosmological data was found.

### One flow, a selected ensemble, or many flows
<!-- key: one-flow-a-selected-ensemble-or-many-flows -->

All benchmarked SBI algorithms (NPE, NRE, sequential NLE, ABC) produced
overconfident posteriors on at least one problem, most often for
non-amortised methods at small simulation budgets; a large budget does not
guarantee conservativeness [src: arXiv:2110.06581, Sect. 3.4]. Deep
ensembles of five models had consistently higher expected coverage than
single models, though they can still be overconfident; bagging did not
always help [src: same, Fig. 3]. Practice follows: 10 of 200 flows in
Beyond-2pt, 4 then 8 MAFs in DES Y3 (the enlargement from 4 to 8 was a
post-unblinding fix, see L2) [src: arXiv:2405.02252, Sect. V.4.3;
arXiv:2606.11309, Sect. 6.3]. SimBIG P_ℓ used a single selected flow
[src: arXiv:2211.00660, Sect. III.5].

### Compression: MSE or mutual information
<!-- key: compression-mse-or-mutual-information -->

MSE regression targets the posterior mean and is optimal only for Gaussian
parameter posteriors [src: arXiv:2606.11309, Sect. 6.2.1]. VMIM targets the
whole conditional density; its estimate is noisier because the simulations
sample p^sim(θ, x) rather than p(θ, x), and its compressor is hierarchical
and not permutation invariant over patches [src: Sects. 3.2, 6.2]. The
summary dimension is a bottleneck hyperparameter (10 for C_ℓ, 4 per patch,
7 at the end) [src: Sects. 3.2, 6.2]. The hybrid analysis reports a gain of
60% in the (Ω_m, S8, w) figure of merit over the previous best DES Y3
analysis (L2); no comparison isolating the compression loss was read.

### Out of distribution: cut, transform, or drop the statistic
<!-- key: out-of-distribution-cut-transform-or-drop-the -->

For the SimBIG wavelet scattering transform (3 677 coefficients), the 2023
analysis removed all small scales (L2). The 2025 method is two-step [src:
arXiv:2507.03086, Sects. III.1–III.2]:

1. Discard coefficients whose means differ between TEST0 and TEST1 (same
   cosmology, different simulators) by more than 1σ; some differ by up to
   12σ, and just under half are removed, mostly small-scale but not all
   [src: arXiv:2507.03086, Sect. III.1].
2. Learn a transformation η_ψ of the summaries jointly with the NPE, with
   loss −Σ_i log q_φ(θ_i|η_ψ(s_i)) + λ d({η_ψ(s_i)}, η_ψ(s_obs)) (Eqs. 5–6),
   d a distance between distributions; λ is set to the smallest value at
   which D_v on the data drops, λ = 1, since larger values pull posteriors
   to the prior centre and λ → ∞ collapses them to the prior.

Each step alone fails one of the two diagnostics: filtering fixes the
simulator robustness but not the variability on the data, the transform the
reverse [src: Sect. III.2.3]. Result on BOSS CMASS (arXiv:2507.03086): Ω_m = 0.32 ± 0.02 and
σ8 = 0.80 ± 0.02, 1.4 and 3.1 times tighter than a perturbative power-spectrum
analysis [src: abstract]. The transform uses the observation during
training, so the posterior is conditioned on a summary space chosen with the
data; the paper tests robustness to the prior choice (Sect. IV.2.2), not
read here.

### Box volume against survey volume
<!-- key: box-volume-against-survey-volume -->

Training on (1 h⁻¹Gpc)³ boxes for (2 h⁻¹Gpc)³ data forces a large-scale cut
k_min = 0.009 h Mpc⁻¹ and makes the learned likelihood over-dispersed,
especially for Ω_m, which loses its informative large-scale modes [src:
arXiv:2405.02252, Sect. V.4.4]. The authors name a hybrid EFT (large
scales) plus SBI (small scales) analysis as the way out [src: same].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Training catalogues | 20 000 = 2000 LH × 10 HOD; 1500/200/300 sims train/validation/test | Beyond-2pt SBI | arXiv:2405.02252 | Sect. V.4.3 |
| Data-vector size | P_ℓ 79 × 3, B_0 1898, plus n̄; 0.009 < k < 0.5 h Mpc⁻¹ | Beyond-2pt SBI | arXiv:2405.02252 | Sect. V.4.1 |
| Ensemble | 10 best of 200 MAFs, equal weights | Beyond-2pt SBI | arXiv:2405.02252 | Sect. V.4.3 |
| Single flow | 6 MADE, 9 layers, 186 units; lr 5 × 10⁻⁴; patience 20 epochs | SimBIG P_ℓ | arXiv:2211.00660 | Sect. III.5 |
| Posterior dimension | 15 parameters, 301-element summary | SimBIG P_ℓ | arXiv:2211.00660 | Sect. III.5 |
| Gower Street suite | 791 sims, first 192 verification runs | DES Y3 | arXiv:2403.02314 | Sect. 4.2 |
| Implicit priors | h N(0.7022, 0.0245); n_s N(0.9649, 0.0063); Ω_b h² N(0.02237, 0.00015) | DES Y3 | arXiv:2403.02314 | Sect. 4.2 |
| NLE ensemble | 4 MAFs (2024); 8 MAFs, hidden 200, 6–9 transforms (2026) | DES Y3 | arXiv:2403.02314; arXiv:2606.11309 | Sect. 2.2; Sect. 6.3 |
| Training w range | −1.05 < w < −0.3, prior applied afterwards | DES Y3 hybrid | arXiv:2606.11309 | Sect. 6.3 |
| Compression sizes | 440 → 10 (C_ℓ); 512² × 8 channels → 4 per patch; 88 → 7 | DES Y3 hybrid | arXiv:2606.11309 | Sect. 6.2 |
| Mock split | 9 264 for compression, 3 088 held out for the likelihood | DES Y3 hybrid | arXiv:2606.11309 | Sect. 6.2 |
| Compression patience | 100 epochs | DES Y3 hybrid | arXiv:2606.11309 | Sect. 6.2 |
| Coefficient filter | > 1σ TEST0–TEST1 mean difference; ≈ half of 3 677 removed | SimBIG WST | arXiv:2507.03086 | Sect. III.1 |
| Robust-transform weight | λ = 1 | SimBIG WST | arXiv:2507.03086 | Sect. III.2.3 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Overconfident estimator.** Every SBI family can be overconfident [src:
  arXiv:2110.06581, Sect. 3.4]. Test: expected-coverage curve or TARP;
  require it on or above the diagonal, not only a uniform rank histogram.
- **Rank test at a fixed cosmology.** Out-of-distribution sets sit at one
  cosmology, where a rank test is distorted by the prior (L2); use the
  (μ − θ_fid)/σ distributions instead [src: arXiv:2507.03086,
  Sect. II.2.4].
- **Data outside the training support.** Shows up as posteriors that change
  with the architecture at equal validation loss [src: same]. Test: D_v
  across 10 architectures [src: arXiv:2507.03086, Sect. III.2.3, Fig. 6];
  the data-in-cloud check of DES Y3.
- **Priors hidden in the simulations.** Implicitly marginalised parameters
  carry their simulated distribution as prior [src: arXiv:2403.02314,
  Sect. 2.5]; in DES Y3 h was drawn from a Gaussian centred between SH0ES
  and Planck [src: Sect. 4.2]. Referee check: list p^sim for every
  parameter not in the density estimator.
- **Hard prior edges.** Density estimators misbehave at training-set
  boundaries; MAFs were preferred to MDNs for this reason, and the hybrid
  analysis trains beyond the prior edge [src: arXiv:2403.02314, Sect. 2.2;
  arXiv:2606.11309, Sect. 6.3].
- **Coverage prior unlike the simulation prior.** TARP needs an analytic
  prior; DES fits one to p^sim, and the coverage statement holds for that
  prior [src: arXiv:2606.11309, Sect. 7.1].
- **Compressor overfitting.** Training compressor and likelihood on the same
  mocks can bias the likelihood; holding out a noise realisation turns the
  risk into a loss of precision [src: arXiv:2606.11309, Sect. 6.2].
- **More informative statistic, more misspecification.** The Beyond-2pt
  team expected B and P + B to exacerbate misspecification through higher
  sensitivity and smaller errors [src: arXiv:2405.02252, Sect. V.4.4,
  Caveats]; L2 records the halo-finder bias of the bispectrum σ8.
- **Training volume.** A box smaller than the survey forces a k_min cut and
  inflates errors [src: arXiv:2405.02252, Sect. V.4.4].

## Reading list
<!-- key: reading-list -->

- Foundation: Papamakarios & Murray 2016, arXiv:1605.06376, and Alsing et
  al. 2019, arXiv:1903.00007 — conditional density estimation, NLE with
  active learning (see L2).
- Method: Hahn et al. 2022, arXiv:2211.00660 — NPE set-up and the
  changed-forward-model test sets.
- Application: Beyond-2pt challenge, arXiv:2405.02252, Sect. V.4 — P + B
  with an ensemble of flows, priors and validation.
- Application: Jeffrey et al. 2024, arXiv:2403.02314 — NLE, active learning,
  implicit marginalisation, ensemble convergence.
- Application: Williamson et al. 2026, arXiv:2606.11309 — VMIM and VICReg
  compression, held-out mocks, TARP in three dimensions.
- Critique: Hermans et al. 2021, arXiv:2110.06581 — overconfidence of all
  SBI families; expected coverage; ensembles.
- Critique: Modi et al. 2023, arXiv:2309.15071 — simulator ingredients that
  bias the bispectrum (see L2).
- Method: Pierre et al. 2025, arXiv:2507.03086 — misspecification
  diagnostics and the two-step repair for SimBIG WST.

## Not verified
<!-- key: not-verified -->

- The ltu-ili package paper (Ho et al. 2024) and the sbi package paper,
  named in arXiv:2606.11309 and arXiv:2211.00660: not read; no identifier
  recorded.
- The robust-transformation method that arXiv:2507.03086 builds on (its
  ref. [32]) and its choice of distance d (Sect. III.2.2): not read.
- The Pierre et al. BOSS constraints were read in the abstract only; their
  prior-robustness test (Sect. IV.2.2) was not read.
- How SimBIG chose the bispectrum and CNN ensembles (arXiv:2310.15243,
  arXiv:2310.15256): not re-read here.
- No NPE-against-NLE comparison on the same cosmological data was found.
