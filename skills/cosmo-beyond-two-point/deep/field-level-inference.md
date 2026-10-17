# Field-level inference — cosmo-beyond-two-point dossier

Scope: how a field-level analysis with sampled initial conditions is set up
and run (parametrisation of the initial field, forward model and its
resolution, likelihood and noise, bias marginalisation, sampler, mass
matrix, convergence tests, survey effects), and how to choose between the
block (Gibbs) and joint samplers, the Poisson and Gaussian likelihoods, and
gravity models of different cost.
Snapshot: 2026-10-17.
From: Leclercq 2025 lecture notes (arXiv:2509.13435), Sects. 3–6;
Beyond-2pt challenge (arXiv:2405.02252), Sect. V.3 (EFT field-level
inference).

Already in L2, not repeated here: the three meanings of "field-level"
(`physics-and-methods.md#three-things-called-field-level`); the founding
papers and the marginal posterior of arXiv:2509.09673, Eq. 38 (same
section); the forward-model families and what BORG runs deliver
(`physics-and-methods.md#forward-model-families`,
`physics-and-methods.md#what-the-outputs-are`); the noise-model failure and
the LEFTfield effective sample sizes
(`systematics.md#likelihood-noise-model-misspecification`,
`systematics.md#sampler-performance`); the information debate
(`open-questions.md#how-much-information-lies-beyond-the-power`).

## How it is done
<!-- key: how-it-is-done -->

### Step 1. The linear case as reference: the Wiener filter
<!-- key: step-1-the-linear-case-as-reference-the-wiener -->

For data d = s + noise with Gaussian signal covariance S and noise
covariance N, the posterior of the signal s is Gaussian with mean
μ_{s|d} = μ_s + S(S + N)⁻¹(d − μ_d) and covariance
C_{s|d} = (S⁻¹ + N⁻¹)⁻¹ (Leclercq 2025, arXiv:2509.13435, Eqs. 10–11). The
mean is both the maximum a posteriori and the minimum-mean-square-error
linear estimate, and constrained realisations follow as
s̃ = μ_{s|d} + √C_{s|d} ξ for white noise ξ [src: Sect. 2.3]. The equivalent
forms of Eq. 11 differ in numerical stability for ill-conditioned matrices;
the notes advise checking which one is stable [src: same]. This is the limit
in which a field-level run can be checked against an exact answer: the
LEFTfield consistency tests recover the analytic posterior of the purely
linear model in N_dim ∼ 10⁵–10⁶ dimensions [src: Kostić et al. 2022,
arXiv:2212.07875, Sect. 6].

### Step 2. Parametrise the initial field as white noise
<!-- key: step-2-parametrise-the-initial-field-as-white -->

LEFTfield samples normalised initial conditions ŝ with a unit Gaussian
prior and builds the linear field as

  δ^(1)(k, z) = α [N_grid³/L³ P_L(k, z)]^{1/2} ŝ(k)
  (Beyond-2pt, arXiv:2405.02252, Eq. 17),

with P_L the linear spectrum at the fiducial cosmology, L and N_grid the box
size and grid, and α = σ8/σ8^fid the amplitude parameter [src: Sect. V.3.3].
A finite box and a cut-off Λ make a finite grid sufficient; in the challenge
this was 90³ ≈ 730 000 sampled modes [src: Sects. V.3, V.3.3]. The general
rule in the notes: parametrise the target field as white noise and "whiten"
every other parameter to values of order [−1, 1]; this is essential when
everything is updated in one proposal [src: arXiv:2509.13435, Sect. 5.2].
A further preconditioning, used with a particle-mesh model, divides each
mode by its linear-theory posterior variance, multiplying by (P_L + N)/N, so
that all k-space voxels have roughly unit variance [src: Bayer et al. 2023,
arXiv:2307.09504, Sect. 4].

### Step 3. Choose the forward model and its resolution
<!-- key: step-3-choose-the-forward-model-and-its -->

The forward model must be differentiable, because the sampler needs the
gradient of the log posterior with respect to every mode [src:
arXiv:2509.13435, Sects. 3.2.2, 6.2]. Choices in use:

| Analysis | Gravity | Grid and resolution | Reason given | Place read |
|---|---|---|---|---|
| BORG on BOSS | 1LPT with a distance-dependent growth factor for the light cone | ≈ 16 h⁻¹Mpc | only mildly non-linear dynamics at that resolution; the light-cone shortcut neglects coherent distortions of ≈ 10 h⁻¹Mpc at the far edge, still acceptable at that resolution | arXiv:1909.06396, Sect. 2.2 |
| BORG on 2M++ | particle mesh | 256³, 2.65 h⁻¹Mpc (see L2) | log Bayes factors of LPT against PM, −log(L_s/L_0), from −159 to −3 778 over the 16 galaxy subsamples: PM "generally outperforms" LPT, most for bright galaxies | arXiv:1806.11117, Table 1 |
| BORG on 2M++, cluster masses | COLA, 20 linear steps from z = 50 | 256³ | 10–20 COLA steps reproduce ∼ 10¹⁵ h⁻¹M_⊙ cluster masses as in GADGET; at ∼ 10¹⁴ the limit is spatial (grid 2.65 against R_200c ≈ 0.75 h⁻¹Mpc), so masses come from N-body posterior resimulations | arXiv:2304.09193, Sects. 3.1, 2.1.5 |
| LEFTfield, Beyond-2pt | 2LPT (n-LPT shown convergent to n = 6) | 90³ modes, cut-off Λ, k_max = Λ/1.4 | k_max < Λ reduces higher-derivative terms controlled by Λ⁻¹; the ratio was not optimised | arXiv:2405.02252, Sect. V.3.2–V.3.3 |
| Perturbative LPT model, NumPyro | 2LPT-based EFT model | L = 2000 h⁻¹Mpc, z = 0.5; inference on 128³ initial and Eulerian grids, mock built on 512³ | isolates the likelihood: same model, different resolution | arXiv:2509.09673, Sect. III.2.3, Table 1 |

The resolution mismatch between data and model is itself a signal: short
modes absent from the model damp the data field by exp(−k²Σ_S²/2), with
Σ_S² = (1/3) ∫_{Λ'} d³k/(2π)³ P_lin(k)/k² (arXiv:2509.09673, Eqs. 49–50),
which appears as a counterterm c_0 = −Σ_S²/2 ≈ −1.3 (h⁻¹Mpc)² for a 128³
cut-off, whereas the power-spectrum analysis shows no such term [src:
Sect. VI.1]. A field-level counterterm away from zero is therefore expected
and is not evidence of new physics.

### Step 4. Write the likelihood
<!-- key: step-4-write-the-likelihood -->

Two families, with the reasons given:

- **Poisson in configuration space (BORG).** Galaxy counts in voxel i are
  Poisson with intensity λ_i = R_i N̄ (1 + δ)^β exp[−ρ_g (1 + δ)^{−ε_g}]
  (arXiv:1806.11117, Eqs. 19–22), where R_i is the survey response (angular
  times radial selection) and (N̄, β, ρ_g, ε_g) are four positive bias
  parameters per subsample with Heaviside priors (Eq. 23). The exponential
  factor suppresses clustering in underdense regions; the noise is
  signal-dependent, not additive [src: Sect. 3.4]. The 2M++ run uses 16
  subsamples split by K-band absolute magnitude and apparent-magnitude cut
  [src: same]. The notes list Gaussian, Poisson, negative-binomial and
  generalised Poisson forms, the latter able to carry super-Poisson variance
  in dense regions [src: arXiv:2509.13435, Sect. 6.2].
- **Gaussian in Fourier space (EFT).**
  ln L = −½ Σ_{k≠0}^{k_max} [ln 2πσ_ε² + |d̂_Λ(k) − δ_g,Λ(k)|²/σ_ε²]
  (arXiv:2405.02252, Eq. 18), with δ_g,Λ = Σ_O b_O O[δ_Λ] the bias expansion
  (Eq. 13) over operators O ∈ {δ, δ² − ⟨δ²⟩, K² − ⟨K²⟩, ∇²δ} (Eq. 14),
  K² the squared tidal field (Eq. 15). The stated justification is that
  stochasticity is homogeneous and isotropic in the rest frame, so its
  covariance is diagonal in Fourier space; the form does not capture
  density-dependent or non-Gaussian noise [src: Sect. V.3.3]. In general
  σ_ε(k) = σ_ε,0 [1 + σ_ε,k² k² + σ_ε,k⁴ k⁴ + …] (Eq. 19); the challenge
  baseline fixed σ_ε,0 at the Poisson value because the k-dependent terms
  "add significant parameter degeneracies" [src: same].

### Step 5. Marginalise what enters linearly
<!-- key: step-5-marginalise-what-enters-linearly -->

Bias coefficients enter the Gaussian likelihood linearly and can be
integrated out analytically: with C, B_O and A_OO' the residual norm, the
projections and the operator overlaps weighted by 1/σ_ε² (arXiv:2403.03220,
Eq. 15), the marginal likelihood is ∝ |A|^{−1/2} exp[−C/2 + ½ B A⁻¹ B]
(Eq. 16) [src: App. A.2]. Reason: fewer dimensions and faster sampling;
the marginalised likelihood shortens the correlation length, "in particular
for α" [src: arXiv:2212.07875, Sect. 6]. In LEFTfield a chain with b_δ left
free reached about 21 effective samples, far fewer than the fully
marginalised chains [src: arXiv:2403.03220, App. A.2].

### Step 6. Choose the sampler and its tuning
<!-- key: step-6-choose-the-sampler-and-its-tuning -->

Hamiltonian Monte Carlo is "the only known way" to sample the multi-hundred
to multi-million dimensional posteriors of non-linear field-level models
[src: arXiv:2509.13435, Sect. 3.2.2]. Its settings are the mass matrix M,
the leapfrog step ε and the number of steps N_steps between acceptance tests
(Eqs. 20–26) [src: same]. The cost of an independent sample scales as
N_dim^{1/4} for HMC against N_dim for a random walk [src: arXiv:2212.07875,
Sect. 3.2]. Two layouts are used (next section). Tuning signs from trace
plots: acceptance ≳ 90% with slow drift means ε or N_steps too small (or a
parameter too "heavy"); ≲ 5% with plateaus means too large [src:
arXiv:2509.13435, Sect. 3.3.1].

### Step 7. Add survey effects inside the model
<!-- key: step-7-add-survey-effects-inside-the-model -->

- **RSD.** Particle positions are shifted to s = r(1 + γ v·r/|r|²),
  γ = a/H(a) (arXiv:1806.11117, Eq. 18), so the dynamical information in
  RSD is used rather than corrected [src: Sect. 3.3].
- **Known foregrounds.** The predicted count is multiplied by
  R_i Π_a (1 + α_a F_a,i) (arXiv:1909.06396, Eq. 8), with F_a the template
  maps and α_a one free amplitude per template and catalogue; eleven SDSS
  templates were used [src: Sects. 2.4, Fig. 3]. The model is limited to
  effects for which sky maps exist [src: Sect. 2.4].
- **Unknown foregrounds.** Voxels are grouped into HEALPix-extruded patches
  𝒜_p, each with a free amplitude A_p under a Jeffreys prior; marginalising
  gives a likelihood in ratios N_i/Σ_{j∈𝒜_p} N_j (Eqs. 9–10), insensitive to
  the absolute intensity on each patch [src: Sect. 2.5]. Motivation: below
  k ≈ 10⁻² h Mpc⁻¹ the systematics of BOSS are not understood [src: same].
- **Model error.** The 2M++ run tempers the Poisson likelihood by a power
  β = 0.3, equivalent to keeping a homogeneous sub-sample N_i → βN_i, hence
  conservative errors [src: arXiv:1806.11117, Sect. 3.5, Eq. 24].

### Step 8. Diagnose convergence
<!-- key: step-8-diagnose-convergence -->

- Gelman–Rubin: R̂ = √(var⁺/var⁻) from between-chain and within-chain
  variances (arXiv:2509.13435, Eqs. 27–32); the notes aim for R̂ − 1 ≲ 10⁻²
  and call the threshold arbitrary [src: Sect. 3.3.2].
- Effective sample size n_eff = n/τ̂, with τ̂ = 1 + 2Σ_{τ=1}^{m} ρ̂(τ) (Eq. 35)
  estimated by FFT; the figure of merit is ESS per gradient or model
  evaluation [src: Sect. 3.3.3]. LEFTfield chooses the window T as the
  smallest integer with T ≥ C τ̂(T), C ∈ [5, 10], and also uses the revised
  Gelman–Rubin R̂_r ≈ √(1 + M/Ê_s) (M chains, Ê_s effective samples) to set
  the target ESS a priori [src: arXiv:2212.07875, App. D, Eqs. 48, 52].
- Initialisation tests: one chain from the true phases and several from
  random phases must become indistinguishable after warm-up [src:
  arXiv:2403.03220, App. B.1]; BORG tests burn-in from a field of too low an
  amplitude (see L2).
- Values achieved, Beyond-2pt stage 2: a Gelman–Rubin target written
  "R̂ ∼ 0.01" and ≈ 255 independent samples of α; ten analyses gave ESS
  193–311 and Gelman–Rubin values 0.003–0.035, two chains each, computed with
  GetDist [src: arXiv:2405.02252, Sect. V.3.3]. Values this small can only
  be R̂ − 1 [der]. Perturbative LPT model, eight chains of 200 000 samples:
  ESS 1 415–73 834 and R̂ ≤ 1.007, slowest for A, b_1 and log P_err; this is
  the least efficient case of that paper, and redshift space or a higher
  k_max mix faster because degeneracies are broken [src: arXiv:2509.09673,
  App. G, Table 7].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Block (Gibbs) sampling or one joint HMC
<!-- key: block-gibbs-sampling-or-one-joint-hmc -->

| | Block: HMC-within-Gibbs | Joint: one HMC/NUTS |
|---|---|---|
| Used by | BORG; LEFTfield (HMC on ŝ, sequential univariate slice sampling for α, b_O, σ_ε) | Almanac (per the notes); NumPyro NUTS in arXiv:2509.09673 |
| Gains | conditionals known; no gradient needed for parameters; slice sampling is rejection-free | diagonal moves in the joint space |
| Costs | cannot move diagonally when field and parameters are degenerate | gradients for every parameter; hard mass-matrix tuning when parameters of different nature act on different scales |
| Place read | arXiv:2509.13435, Sect. 5.2; arXiv:2212.07875, Sect. 3.2; arXiv:2405.02252, Sect. V.3.3 | arXiv:2509.13435, Sect. 5.2; arXiv:2509.09673, Sect. III.2.3 |

The LEFTfield authors judged joint HMC "unfeasible": α and the biases change
all modes while one ŝ(k) changes one, so a common step must be small and
exploration is slow [src: arXiv:2212.07875, Sect. 3.2]. The joint NUTS
implementation answers that problem with a block mass matrix, dense for the
cosmological and bias parameters (which are correlated, such as amplitude
and bias) and diagonal for the modes (nearly independent a priori, and too
many for a dense block), tuned in warm-up so that the larger curvature of θ
gets larger mass entries [src: arXiv:2509.09673, Sect. III.2.2, Eq. 37]. No
comparison of the two layouts on the same problem was found.

### HMC or microcanonical Langevin Monte Carlo
<!-- key: hmc-or-microcanonical-langevin-monte-carlo -->

On pmwd particle-mesh fields with 4 h⁻¹Mpc voxels, sampling the modes with
Ω_m and σ8, HMC (step tuned to 65% acceptance, 40 leapfrog steps) and
MCLMC (energy fluctuation per dimension below 10⁻⁴) give the same
posteriors; MCLMC has higher ESS per gradient evaluation in all cases, by
two orders of magnitude for 2LPT and least for 5-step PM, and by factors 40
(modes) and 80 (cosmological parameters) at 64³ for 1LPT [src: Bayer et al.
2023, arXiv:2307.09504, Sect. 4]. Stated reason: HMC must shrink its step
as the energy grows with dimension, MCLMC need not [src: same]. The test
volumes are small (up to 64³ voxels).

### Poisson or Gaussian likelihood
<!-- key: poisson-or-gaussian-likelihood -->

The Gaussian EFT likelihood keeps the analysis under perturbative control up
to k_max with free bias operators and analytic marginalisation (Step 5); its
known gaps are density-dependent and non-Gaussian noise [src:
arXiv:2405.02252, Sect. V.3.3], whose consequence is in L2. Inferring σ_ε
freely under a wide prior made it collapse to "an unphysically low value",
a known problem of Gaussian likelihoods with unknown covariance on noisy,
sparse samples [src: Sect. V.3.4, Caveats]. The Poisson likelihood with a
non-linear local bias works voxel by voxel without a scale cut and handles
masks, selection and foregrounds as multiplicative terms [src:
arXiv:1806.11117, Sect. 3.4; arXiv:1909.06396, Sect. 2.4], but needs the
tempering of Step 7 to stay robust to model error [src: arXiv:1806.11117,
Sect. 3.5].

### Bias order and noise model: fixed priors or freedom
<!-- key: bias-order-and-noise-model-fixed-priors-or -->

The Beyond-2pt LEFTfield baseline (second-order bias, Poisson-fixed σ_ε)
gave a biased σ8. The post-unmasking rerun with the four third-order
operators (priors U(−4, 4)) and σ_ε(k) = σ_ε,0(1 + σ_ε,k² k²) with
σ_ε,0 ∈ U(0.9, 1.1) σ_Poisson and σ_ε,k² ∈ U(−10, 100) removed the bias at
the cost of a larger error bar (arXiv:2405.02252, Eqs. 24–25) [src:
Sect. V.3.4, Post-unmasking studies]. The baseline choice was made to afford
ten free-IC analyses [src: same].

### Scale cut
<!-- key: scale-cut -->

LEFTfield sets k_max as the largest value for which α stays stable between
model variants (second- against third-order bias, Eulerian against
Lagrangian basis), requiring Δα/σ_α = (⟨α⟩_A − ⟨α⟩_B)/(σ_A² + σ_B²)^{1/2}
< 2 (arXiv:2405.02252, Eq. 23); this gave k_max = 0.1 h Mpc⁻¹, "the maximum
scale up to which the second-order bias expansion is expected to be
reliable" [src: Sect. V.3.4]. The cut-off convergence was tested at fixed
initial conditions, which is cheap [src: Sect. V.3.4, Unmasking criteria].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Sampled modes | 90³ ≈ 730 000 | LEFTfield, Beyond-2pt | arXiv:2405.02252 | Sect. V.3 |
| k_max/Λ | 1/1.4 (not optimised) | LEFTfield, Beyond-2pt | arXiv:2405.02252 | Sect. V.3.3 |
| k_max | 0.1 h Mpc⁻¹, stability criterion Δα/σ_α < 2 | LEFTfield, Beyond-2pt | arXiv:2405.02252 | Eq. 23, Sect. V.3.4 |
| Bias priors (baseline) | α U(0.5, 1.5); b_δ U(0, 4); b_δ², b_K² U(−4, 4); b_∇²δ U(−20, 20) | LEFTfield, Beyond-2pt | arXiv:2405.02252 | Eqs. 20–21 |
| Convergence achieved | ESS 193–311; Gelman–Rubin 0.003–0.035 (R̂ − 1 [der]) | LEFTfield, ten boxes | arXiv:2405.02252 | Sect. V.3.3 |
| Convergence target | R̂ − 1 ≲ 10⁻² (arbitrary) | notes | arXiv:2509.13435 | Sect. 3.3.2 |
| Autocorrelation window | T ≥ C τ̂(T), C ∈ [5, 10] | LEFTfield tests | arXiv:2212.07875 | App. D |
| HMC scaling | N_dim^{1/4} against N_dim for random walk | — | arXiv:2212.07875 | Sect. 3.2 |
| HMC tuning in a PM test | 65% acceptance, 40 leapfrog steps; 10 000 samples after 2 000 burn-in | pmwd | arXiv:2307.09504 | Sect. 4 |
| MCLMC gain | ×40 (modes), ×80 (parameters) in ESS per gradient at 64³, 1LPT | pmwd | arXiv:2307.09504 | Sect. 4 |
| Likelihood tempering | β = 0.3 | BORG 2M++ | arXiv:1806.11117 | Sect. 3.5 |
| COLA steps for 10¹⁵ h⁻¹M_⊙ masses | 10–20; adopted 20, chain converged by ≈ 7 000 of 15 000 steps | BORG 2M++ | arXiv:2304.09193 | Sects. 3.1, 2.1.5 |
| BOSS model resolution | ≈ 16 h⁻¹Mpc, 1LPT | BORG BOSS | arXiv:1909.06396 | Sect. 2.2 |
| Foreground templates | 11 SDSS maps | BORG BOSS | arXiv:1909.06396 | Sect. 2.4 |
| Grids, perturbative tests | data 512³, inference 128³ (Lagrangian 192³), L = 2000 h⁻¹Mpc | NumPyro | arXiv:2509.09673 | Table 1 |
| Resolution counterterm | c_0 ≈ −1.3 (h⁻¹Mpc)² at 128³ | NumPyro | arXiv:2509.09673 | Sect. VI.1 |
| Chains and samples | 8 chains, ≥ 10³ effective samples | NumPyro | arXiv:2509.09673 | Sect. III.2.3 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Noise amplitude collapses.** Free σ_ε under a wide prior runs to an
  unphysical low value on sparse samples [src: arXiv:2405.02252,
  Sect. V.3.4]. Test: free-σ_ε run against a Poisson-fixed one; the
  Beyond-2pt fix was a narrow prior, U(0.9, 1.1) σ_Poisson.
- **Model too restricted for the data.** Second-order bias with fixed white
  noise biased σ8 in the challenge [src: same, Post-unmasking studies].
  Test: the bias-order and basis scan of the scale-cut criterion (Eq. 23).
- **Unconverged amplitude.** α, b_1 and the noise mix most slowly [src:
  arXiv:2509.09673, App. G; arXiv:2212.07875, App. D]. Test: ESS and R̂ of
  those parameters specifically, not of the modes; chains started from the
  true and from random phases [src: arXiv:2403.03220, App. B.1].
- **Joint sampler with a poor mass matrix.** Field and parameters differ in
  curvature by large factors; without a tuned block mass matrix the step
  collapses [src: arXiv:2212.07875, Sect. 3.2; arXiv:2509.09673,
  Sect. III.2.2]. Test: acceptance rate and trace plots (Step 6).
- **Fields mistaken for a resolved halo model.** At a 2.65 h⁻¹Mpc grid,
  M_200c of 10¹⁴ h⁻¹M_⊙ clusters does not converge with more time steps;
  only M_100m does [src: arXiv:2304.09193, Sect. 3.1]. Test: posterior
  N-body resimulations before quoting small-scale quantities.
- **Large-scale systematics read as signal.** Templates cover only mapped
  effects [src: arXiv:1909.06396, Sect. 2.4]; the patch likelihood discards
  information on scales above the patch size by construction [src:
  Sect. 2.5]. Test: cross-correlation of the inferred field with an
  independent tracer (L2: Planck lensing).
- **Light-cone shortcut.** Scaling D_+ with distance neglects ≈ 10 h⁻¹Mpc
  coherent distortions at the far edge; acceptable at 16 h⁻¹Mpc resolution,
  not at finer resolution [src: arXiv:1909.06396, Sect. 2.2].
- **Fixed-IC success taken as free-IC success.** The Beyond-2pt stage-1
  tests used the true phases; only stage 2 sampled them [src:
  arXiv:2405.02252, Sect. V.3.4]. Report which was done.

## Reading list
<!-- key: reading-list -->

- Review: Leclercq 2025, arXiv:2509.13435 — Wiener filter, HMC, Gelman–Rubin,
  ESS, block against joint sampling.
- Foundation: Jasche & Wandelt 2013, arXiv:1203.3639 — BORG (see L2).
- Method: Jasche & Lavaux 2019, arXiv:1806.11117 — HMC, block sampling,
  Poisson likelihood with non-linear bias, RSD, tempering.
- Method: Lavaux, Jasche & Leclercq 2019, arXiv:1909.06396 — light cone,
  foreground templates, robust patch likelihood.
- Method: Kostić et al. 2022, arXiv:2212.07875 — why HMC plus slice sampling;
  convergence statistics; analytic bias marginalisation.
- Application: Beyond-2pt challenge, arXiv:2405.02252, Sect. V.3 — a
  complete EFT field-level analysis with priors, scale cut and diagnostics.
- Application: Nguyen et al. 2024, arXiv:2403.03220 — marginalised
  likelihood, initialisation tests.
- Method: Bayer et al. 2023, arXiv:2307.09504 — MCLMC against HMC.
- Method: Stopyra et al. 2023, arXiv:2304.09193 — gravity-solver accuracy,
  posterior resimulation.
- Critique: Akitsu et al. 2025, arXiv:2509.09673 — joint NUTS with a block
  mass matrix; resolution-mismatch counterterm.

## Not verified
<!-- key: not-verified -->

- The Almanac code named in arXiv:2509.13435, Sect. 5.2: no paper read.
- Porqueres et al. 2019 (the robust likelihood test) and Jasche & Lavaux 2017
  (the foreground model), cited in arXiv:1909.06396: not read; no identifier
  recorded.
- A free-IC redshift-space EFT field-level sampler: announced as future work
  in arXiv:2212.07875, Sect. 6; its status was not checked beyond the L2
  entry for arXiv:2609.16719.
- Convergence diagnostics of the Quaia and Manticore-Local runs.
