# Samplers and frameworks — cosmo-software-ecosystem dossier

Scope: how a practitioner configures a sampler inside a cosmology
framework (settings for test and publication runs, proposal and
mass-matrix tuning, stopping and convergence tests) and how to choose
between Metropolis–Hastings, nested, ensemble and gradient-based samplers
for a given likelihood cost, dimension and need for the evidence, with the
head-to-head results read in comparison papers.
Snapshot: 2026-10-17.
From: Nygaard et al. 2026 (arXiv:2606.04895), Sects. 2–4 (sampling
methods, implementation, comparison); Snowmass2021 CompF white paper
(arXiv:2203.07347), Sect. 4.3 (parameter exploration).

Already in L2, not repeated here: the families, frameworks and their
mechanisms in `physics-and-methods.md#sampler-families` and
`physics-and-methods.md#frameworks`; library defaults (Cobaya, emcee,
dynesty, nautilus, NumPyro, BlackJAX) and their traps in
`systematics.md#sampler-defaults`; the DES Y1 MultiNest–PolyChord evidence
table in `systematics.md#code-comparisons-read-in-paper-bodies`; headline
speed-ups in `results.md#samplers-documented-comparisons`; the debate in
`open-questions.md#which-sampler`. Convergence theory, priors and
projection effects belong to `cosmo-statistics-inference`.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. State what the run must deliver
<!-- key: step-1-state-what-the-run-must-deliver -->

Three outputs pull in different directions.

- **Posterior only.** Any sampler; the question is cost to a target
  accuracy of credible intervals.
- **Evidence for model comparison.** Nested sampling (NS) computes Z
  directly; MCMC needs a separate estimator such as the learned harmonic
  mean, whose quoted error covers only scatter over sample subsets, not a
  flow that fails to capture the posterior shape (Lovick et al. 2025,
  arXiv:2509.13307, Sect. 4.2) [src].
- **Very high dimension.** NS cost "scales very harshly with dimension",
  so field-level problems stay out of its reach even on GPUs, where HMC
  is already used (arXiv:2509.13307, Sect. 4.2) [src].

Then state the cost and form of the likelihood: seconds per call
(Boltzmann code inside), milliseconds (emulator), differentiable or not,
vectorisable over a batch or not. The ranking of samplers changes with
these (Choices, below).

### Step 2. Set up the parameter space
<!-- key: step-2-set-up-the-parameter-space -->

- **Scale parameters to similar size.** In the CosmoSIS
  Metropolis–Hastings sampler used for DES, A_s had to be sampled as
  10⁹A_s, because the tiny raw values made the proposal covariance
  ill-conditioned (Lemos et al. 2022, arXiv:2202.08233, Sect. 2.2.2) [src].
- **Separate fast and slow parameters.** The same DES set-up used one
  Gaussian proposal per subspace, oversampled the 9 fast parameters by a
  factor of 5, and drew a third of jump lengths from an exponential
  distribution "to better explore parameter tails" [src: Sect. 2.2.2].
  Cobaya's blocking and dragging are in L2.
- **Give an initial covariance.** Lemos et al. took the proposal from a
  finished high-quality PolyChord chain and did not tune it, for
  simplicity; a diagonal start plus tuning would reach the same posterior,
  more slowly [src: Sect. 2.2.2]. Mootoovaloo et al. 2024 likewise gave
  Cobaya a proposal covariance in all runs and note that this
  "vastly helps" acceptance (arXiv:2406.04725, Sect. 4.4) [src].
- **Whiten for gradient samplers too.** The BEST framework of Nygaard et
  al. estimates a covariance from the walker ensemble after each burn-in
  iteration and whitens with it (Cholesky-regularised) for MH, HMC, NUTS
  and MALA (MALA: Metropolis-adjusted Langevin algorithm); the
  affine-invariant ensemble sampler (AIES, emcee's stretch move) is left
  out because it is invariant under such transformations
  (arXiv:2606.04895, Sect. 3.2) [src].

### Step 3. Choose run settings by purpose
<!-- key: step-3-choose-run-settings-by-purpose -->

DES recommendations, obtained on the wCDM DES Y1 3×2pt likelihood and used
for DES Y3 (arXiv:2202.08233, Sect. 5, Table 3) [src]:

| Case | Sampler | n_live | tol | n_repeats | other | Wall time on 128 cores |
|---|---|---|---|---|---|---|
| I, publication quality | PolyChord | 500 | 0.01 | 60 | `fast_fraction` = 0.01 | ∼ 4 days |
| II, testing (noisy contours) | PolyChord | 250 | 0.1 | 30 | `fast_fraction` = 0.0 | ∼ 1 day |
| III, very preliminary only | MultiNest | 250 | 0.1 | — | efficiency 0.3, `constant_efficiency` F | ∼ 6 hours |

Case III gives unreliable evidences and Ω_m and σ8 widths underestimated
by ∼ 10 % (arXiv:2202.08233) [src: Sect. 5, on Case III of Table 3]. Here n_live is the number of live points, tol
the stopping tolerance on the remaining evidence, n_repeats the length of
PolyChord's slice-sampling chains, efficiency MultiNest's ellipsoid
enlargement control. The authors warn that the exact settings need
adjusting when the dimension or posterior shape changes "significantly"
[src: Sect. 5].

Other settings read in the papers:

- **nautilus**, KiDS-Legacy cosmic shear: chosen "due to its superior
  efficiency, robustness of uncertainties, and accurate evidence
  estimation", run inside CosmoSIS with CosmoPower emulation (Wright et
  al. 2025, arXiv:2503.19441, Sect. 5.1) [src]. The nautilus authors ask
  that exploration-phase points be discarded for publication (L2).
- **NUTS (NumPyro)** on a 25-parameter DES Y1 shear-clustering likelihood
  with a Gaussian-process P(k) emulator: maximum tree depth 8 (so at most
  2⁸ − 1 leapfrog steps per iteration), initial step size 0.01, 500
  warm-up steps, two chains of 15 000 samples; Cobaya MH with
  R − 1 ≤ 0.01, two chains of 5 × 10⁵ requested samples
  (arXiv:2406.04725, Sect. 4.4) [src].
- **HMC + harmonic evidence** (cosmic shear, 39 dimensions): 60 chains,
  warm-up/samples 100/400 (CMB) and 400/2000 (shear), replicating an
  earlier analysis; GPU NS with 1000 live points
  (arXiv:2509.13307, Sect. 3) [src].

### Step 4. Decide when to stop
<!-- key: step-4-decide-when-to-stop -->

- **Metropolis–Hastings.** Cobaya's multivariate R − 1 normalises the
  covariance of chain means B and the mean chain covariance W by the
  diagonal of B, d_i = √B_ii, and takes the largest absolute eigenvalue of
  W̃⁻¹B̃ (arXiv:2606.04895, Eqs. 17–18, described as "inspired by the
  implementation in Cobaya") [src: Sect. 4.1]. It measures mixing, not
  closeness to the true posterior [src].
- **Nested sampling.** MultiNest estimates the remaining evidence from the
  maximum likelihood so far, max L × X, PolyChord from the mean, L̄ × X;
  both stop when ΔZ/Z ≤ tol, X being the remaining prior volume (Ashton et
  al. 2022, arXiv:2205.15570, Sect. 2.5) [src]. No criterion guarantees
  that a narrow high-likelihood spike was not missed [src].
- **Sampler variance across runs.** DES required the scatter of
  parameter means across independent chains to stay below a tenth of the
  mean single-chain standard deviation, σ_c[θ̄] < 0.1⟨σ_s[θ]⟩_c,
  "closely related" to a Gelman–Rubin threshold (arXiv:2202.08233,
  Sect. 4.4) [src]; the context is the DES Y3 requirement that unmodelled
  systematics shift the maximum posterior in (Ω_m, S8) by no more than
  0.3σ [src].

### Step 5. Validate the run
<!-- key: step-5-validate-the-run -->

- Compare the NS posterior with an MH chain on the same likelihood; DES
  validated PolyChord this way (arXiv:2202.08233, Sect. 5) [src].
- Run 20 independent chains per setting on a fast approximate likelihood
  and compare the spread of log Z with each run's own error bar
  (arXiv:2202.08233, Sect. 4.4) [src]. PolyChord's error bars matched the
  empirical scatter; MultiNest's quoted error was much larger than the
  scatter while its mean drifted with n_live [src].
- Test the insertion indices: if new live points are drawn independently
  from the constrained prior, their likelihood ranks among the current
  live points are uniform; `anesthetic` implements this for PolyChord and
  MultiNest output, and nessai and UltraNest run it on the fly
  (arXiv:2205.15570, Sect. 3) [src]. A failure with other checks passing
  points to an inadequate exploration strategy [src].
- For emulator-based studies with a reference posterior, Nygaard et al.
  use the credible metric Δ^CM_α (Eq. 19: summed offsets of upper and
  lower α-credible limits over the reference interval width, maximum over
  parameters, at α = 68 % and 95 %) and the sliced Wasserstein distance,
  which probes correlations that 1D limits miss (arXiv:2606.04895,
  Sect. 4.1) [src].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### MultiNest or PolyChord
<!-- key: multinest-or-polychord -->

- MultiNest samples within an enlarged bounding ellipsoid; if the
  enlargement (inverse of efficiency) is too small, volume is cut off and
  the evidence biased (arXiv:2202.08233, Sect. 2.2.2, Fig. 2 caption)
  [src].
- MultiNest evidences "were systematically biased except at extreme
  values" of efficiency, and its credible intervals were consistently
  ∼ 10 % smaller than PolyChord's; good PolyChord results needed only
  n_repeats ∼ D, D being the dimension; raising n_live had the largest
  effect on accuracy for both (arXiv:2202.08233, Sect. 5) [src]. Raising
  n_live is also the most efficient way to reduce both stochastic and
  systematic error according to the work cited there [src: Sect. 4.4].
- MultiNest's speed advantage "is not present when sufficiently accurate
  sampling hyperparameters are used" [src: Sect. 5].
- PolyChord's evidence error is derived analytically (Keeton 2011, as
  cited); MultiNest's rests on the relative entropy and information-
  theoretic arguments [src: Sect. 4.4].

### How many live points
<!-- key: how-many-live-points -->

Each NS iteration compresses the prior volume by Δlog X ≈ 1/n_live, so run
time scales as n_live and errors as 1/√n_live; the evidence error is
Δlog Z ≈ √(H/n_live), with H the Kullback–Leibler information of posterior
relative to prior (arXiv:2205.15570, Sect. 1.5, Eqs. 16–21) [src]. n_live
is also a resolution: only modes with prior footprint larger than about
X/n_live are reliably found, and n_live should exceed the dimension
[src: Sect. 2.1]. The Δlog Z formula "can be unreliable"; repeated
simulation of the compression is the authority [src: Sect. 1.5].

### Gradient samplers or Metropolis–Hastings
<!-- key: gradient-samplers-or-metropolis-hastings -->

- **Per sample.** On differentiable emulator likelihoods, NUTS converges in
  the fewest samples per chain, then HMC, MALA, and last MH and AIES; NUTS
  and HMC settle on a good covariance after one burn-in iteration, MALA
  and MH benefit from three (arXiv:2606.04895, Sect. 4.2) [src].
- **Per second.** In wall time the order changes: MALA fastest, then HMC,
  MH, and NUTS with AIES last; "all the methods seem to converge very
  similarly in terms of wall time" (arXiv:2606.04895) [src: Sect. 4.2]. Throughput on one
  V100 with XLA compilation and 1000 chains is 2932 (MH), 1028 (MALA),
  294 (HMC), 46 (NUTS) and 2901 (AIES) steps per second (Table 1)
  [src: Sect. 3.3].
- **Non-Gaussian posteriors.** For the sterile-neutrino extension MALA
  became sensitive to covariance estimation and burn-in; HMC and NUTS
  stayed robust (arXiv:2606.04895, Sect. 5) [src]. The authors conclude
  that no single sampler is optimal [src].
- **On a survey likelihood.** NUTS against Cobaya MH on DES Y1 (25
  parameters): parameter means differ by at most δ ∼ 0.1 (Eq. 30,
  δ = |μ_1 − μ_2|/√(σ_1² + σ_2²)); effective sample size gain O(10); with a
  gradient costing ∼ 4.5 likelihood evaluations in reverse-mode autodiff,
  the net gain is roughly 2 (arXiv:2406.04725, Sects. 4.5, 7) [src]. On
  multivariate Gaussians NUTS is preferable above d ∼ 100
  [src: Sect. 7]. The earlier Julia/Turing study cited there found an
  effective-sample gain of ∼ 1.7 and a gradient cost ratio of ∼ 5.5 with
  forward mode [src: Sect. 4.5].

### GPU nested sampling or CPU nested sampling or HMC
<!-- key: gpu-nested-sampling-or-cpu-nested-sampling-or -->

- With a fully vectorisable emulated CMB likelihood, nested slice sampling
  on a GPU took 12 s against 1 hour for PolyChord, ∼ 300 times faster,
  because it evolves 500 live points in parallel where PolyChord updates
  one per iteration (arXiv:2509.13307, Sect. 3.1) [src].
- When the likelihood itself is the bottleneck (cosmic shear), GPU NS and
  HMC sit on "a fairly equal footing"; interpolating P(k) sped HMC up by
  2 and GPU NS by more than 4 [src: Sect. 4.1].
- HMC cannot be parallelised the same way: 500 chains of 20 samples would
  be dominated by warm-up and too short, whereas 10 chains of 1000 give a
  sound posterior but only 10 parallel evaluations (arXiv:2509.13307)
  [src: Sect. 4.1].
- **Evidence disagreement.** GPU NS and HMC + learned harmonic mean
  Bayes factors were ∼ 4σ apart for both likelihoods; a difference of 2
  in log B separates "decisive" from "inconclusive", so "models certainly
  cannot be compared across methods … even on identical likelihoods"
  (arXiv:2509.13307) [src: Sect. 4.2].
 HMC also under-represented a secondary peak of a
  nuisance parameter (A_IA,10) found by few chains [src].

### Ensemble sampler (emcee/AIES)
<!-- key: ensemble-sampler-emcee-aies -->

In the vectorised emulator setting AIES reaches ∼ 10⁴ steps per second
(all walkers) on a V100 and remains "a viable alternative" at the price
of a larger sample from long autocorrelations (arXiv:2606.04895,
Sects. 3.3, 4.2) [src]. nautilus needed ∼ 80 000 likelihood calls on a
seven-parameter galaxy–halo fit where the original emcee analysis reported
3–10 × 10⁶ (L2, `physics-and-methods.md#sampler-families`).

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Publication PolyChord settings | n_live 500, tol 0.01, n_repeats 60; ∼ 4 days on 128 cores | DES Y1 wCDM 3×2pt, used in Y3 | arXiv:2202.08233 | Table 3 |
| Test PolyChord settings | n_live 250, tol 0.1, n_repeats 30; ∼ 1 day | same | arXiv:2202.08233 | Table 3 |
| MultiNest preliminary | n_live 250, eff 0.3, tol 0.1; ∼ 6 h; widths −10 % | same | arXiv:2202.08233 | Table 3 |
| "High-quality" reference chains | PolyChord n_live 1000, n_repeats 120, tol 0.001; 20 chains per setting | fast DES Y1 likelihood | arXiv:2202.08233 | Sect. 4.4 |
| Sampler-variance criterion | σ_c[θ̄] < 0.1⟨σ_s[θ]⟩_c | DES Y3 | arXiv:2202.08233 | Sect. 4.4 |
| MH fast oversampling | factor 5, 9 fast parameters; 1/3 exponential jumps | CosmoSIS, DES | arXiv:2202.08233 | Sect. 2.2.2 |
| NS evidence error | Δlog Z ≈ √(H/n_live) | general | arXiv:2205.15570 | Eq. 21 |
| Sampling speeds, V100 + JIT, 1000 chains | MH 2932, MALA 1028, HMC 294, NUTS 46, AIES 2901 steps s⁻¹ | ΛCDM emulator | arXiv:2606.04895 | Table 1 |
| Sampling speeds, M4 Pro CPU + JIT, 20 chains | MH 1287, MALA 344, HMC 167, NUTS 36, AIES 1030 steps s⁻¹ | same | arXiv:2606.04895 | Table 1 |
| NUTS vs Cobaya MH | δ ≤ 0.1; N_eff gain O(10); gradient/likelihood cost 4.5; net ∼ 2 | DES Y1, 25 parameters | arXiv:2406.04725 | Sects. 4.5, 7 |
| Dimension where NUTS wins | d > 100 | Gaussian tests | arXiv:2406.04725 | Sect. 7 |
| GP emulator used | 1000 Latin-hypercube CLASS runs (∼ 1 h) + GP training (∼ 2 h); P ≤ 1 %, growth ≤ 0.01 % | DES Y1 | arXiv:2406.04725 | Sect. 4.5 |
| GPU NS vs PolyChord | 12 s vs 1 h (∼ 300×), 500 live points evolved in parallel | emulated CMB TT | arXiv:2509.13307 | Sect. 3.1 |
| GPU NS vs HMC Bayes factor | ∼ 4σ apart | CMB and 39-D shear | arXiv:2509.13307 | Sect. 4.2 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Biased evidence from MultiNest at standard efficiency.** Shows as
  log Z drifting with n_live or efficiency by more than its quoted error
  (arXiv:2202.08233, Sect. 4.4) [src]. Test: repeat at higher n_live;
  compare with PolyChord; run the insertion-index test
  (arXiv:2205.15570, Sect. 3).
- **Tails cut, intervals ∼ 10 % narrow.** MultiNest at high efficiency
  and, to a lesser degree, any NS at low n_live (arXiv:2202.08233,
  Sect. 4.4) [src]. Test: MH chain on the same likelihood.
- **Ill-conditioned proposal.** Raw A_s in an MH proposal
  (arXiv:2202.08233, Sect. 2.2.2) [src]. Fix: sample a rescaled amplitude such as 10⁹A_s.
- **Settings transferred to a different problem.** DES settings are for
  its dimension and posterior; the authors expect retuning when these
  change (arXiv:2202.08233, Sect. 5) [src].
- **Converged chains, wrong posterior.** R − 1 measures mixing only
  (arXiv:2606.04895, Sect. 4.1) [src]. Test: a reference run with another
  sampler, credible metric or sliced Wasserstein distance.
- **Evidence from two methods compared.** NS and harmonic-mean Bayes
  factors on the same likelihood differed by ∼ 4σ (arXiv:2509.13307,
  Sect. 4.2) [src]. Compare models only with one evidence method, and
  state its error budget.
- **Missed mode.** NS misses modes smaller than ∼ X/n_live
  (arXiv:2205.15570, Sect. 2.1); HMC chains miss modes their
  initialisation does not reach (arXiv:2509.13307, Sect. 4.2) [src].
- **Likelihood plateaus.** Flat regions with non-zero prior mass spoil
  NS compression estimates (arXiv:2205.15570, Sect. 6.1) [src]; emulators
  clipped at their training edges can create such regions [der: an
  emulator returning a constant outside its range has L constant there].
- **Improper prior.** NS needs a proper prior, usually as a transform from
  the unit hypercube (arXiv:2205.15570, Sect. 6.1) [src].
- **Wall-time comparisons made on samples.** A sampler that wins per
  sample (NUTS) may lose per second on a cheap likelihood
  (arXiv:2606.04895, Sect. 4.2) [src]; quote both.

## Reading list
<!-- key: reading-list -->

- Critique and settings: Lemos et al. 2022, arXiv:2202.08233 — DES
  sampler tests, Table 3 settings, sampler-variance criterion.
- Review: Ashton et al. 2022, arXiv:2205.15570 — NS error, live points as
  resolution, stopping rules, insertion-index test, limitations.
- Method comparison: Nygaard et al. 2026, arXiv:2606.04895 — five MCMC
  algorithms on emulators, per-sample against per-second, convergence
  metrics.
- Method comparison: Mootoovaloo et al. 2024, arXiv:2406.04725 — NUTS
  against Cobaya MH on DES Y1, gradient cost, NumPyro settings.
- Method: Lovick et al. 2025, arXiv:2509.13307 — GPU nested slice
  sampling, HMC + harmonic evidence, where each wins.
- Application: Wright et al. 2025, arXiv:2503.19441 — nautilus in
  CosmoSIS for a survey cosmic-shear analysis, stated reasons.
- Code papers for tuning: PolyChord arXiv:1506.00171, nautilus
  arXiv:2306.16923, Cobaya arXiv:2005.05290 (summarised in L2).

## Not verified
<!-- key: not-verified -->

- "Lemos et al. 2023" and the DES–KiDS joint analysis cited by
  arXiv:2503.19441 as evidence for nautilus: not read, no identifier
  recorded.
- The learned harmonic mean estimator paper and Yallup et al. 2025 (nested
  slice sampling in BlackJAX), cited in arXiv:2509.13307: not read.
- DES Y6 sampler settings: not read here (L2 carries a secondary
  statement only).
- The Lovick et al. Bayes-factor values (their Table 2) and the
  sterile-neutrino results of Nygaard et al. (Sect. 4.3) were not
  transcribed.
- Keeton 2011 and Higson et al. 2018, cited in arXiv:2202.08233,
  Sect. 4.4: not read.
