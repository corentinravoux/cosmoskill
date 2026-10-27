# Emulators — cosmo-machine-learning dossier

Scope: how a neural or Gaussian-process emulator of a theory code or of a simulation suite is
built (what is emulated, training design, target transforms, network, loss, schedule,
hyperparameter search), how its accuracy requirement is set in units of the target survey and
tested inside the analysis it serves, and how its residual error is propagated; and how to choose
between Latin-hypercube, hypersphere, posterior-concentrated and copula designs, between direct,
PCA and whitened outputs, and between emulating the matter spectrum, the observable or the
perturbation-theory pieces.
Snapshot: 2026-10-18.
From: Huertas-Company & Lanusse 2022 review (arXiv:2210.01813), Sect. 4.1; Dvorkin et al. 2022
Snowmass white paper (arXiv:2203.08056), Sect. 4.

Already in L2, not repeated here: the regression families and the architectures of
DarkEmulator2, GokuNEmu and PyBird-Emu
(`physics-and-methods.md#emulators-of-summary-statistics`); headline accuracies
(`results.md#emulator-accuracy`); error budgets against held-out simulations and the
P_L × P_NL-corr split (`systematics.md#emulator-error`). The simulation designs of the
gravity-only emulators (Coyote, Mira-Titan, EuclidEmulator2, BACCO) are in
`cosmo-simulations-mocks` (physics-and-methods, Sect. 8); the error budget of an emulator inside a
likelihood, in the order a referee asks for it, is in `cosmo-statistics-inference`
(physics-and-methods, Sect. 11); the P1D emulators of the Lyα forest have their own dossier,
`cosmo-lyman-alpha/deep/p1d-emulators.md`.

Symbols. θ: input parameters; t(θ): the exact prediction (Boltzmann code, one-loop code or
simulation); t̂(θ): the emulated one; Δ = t − t̂: emulator residual; C: data covariance;
Σ: covariance of Δ over a validation set; Δχ² = (t̂ − t)ᵀ C⁻¹ (t̂ − t); σ: the 1σ data error per
bin of the target survey; LF/MF/HF: low, middle, high resolution.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Choose what the network replaces
<!-- key: step-1-choose-what-the-network-replaces -->

| Level emulated | What stays analytic | Gain | Cost | Example, place read |
|---|---|---|---|---|
| Matter P(k) or CMB C_ℓ | n(z), nuisance and projection to the observable | one emulator serves any redshift distribution or nuisance model; "train once, use repeatedly" | smaller speed-up than emulating the observable | CosmoPower, arXiv:2106.03846, Sects. 3.2, 5.2 |
| The observable (band powers, MOPED coefficients) | nothing | largest speed-up | tied to one n(z) and one nuisance parametrisation | GP band-power emulators, as discussed in arXiv:2106.03846, Sect. 5.2 |
| EFT pieces 𝒫_ij,ℓ(k; θ) with biases and counterterms outside, P_ℓ = Σ b_i b_j 𝒫_ij,ℓ + S_ℓ (arXiv:2501.04639, Eq. 1) | bias, counterterms, stochastic terms | lower-dimensional emulated space, smaller networks | one network set per code convention | Effort, arXiv:2501.04639, Sect. 2.2 |
| Loop integrals as a function of a spline of P_lin | the Boltzmann code and the linear and counterterm pieces | not tied to a cosmological model | 80-knot input; features finer than Δk ~ 0.01 h Mpc⁻¹ unresolved | PyBird-Emu, arXiv:2507.20990, Sect. 2.1 |
| Multipoles per tracer and redshift bin, bias inside | nothing | small networks, easy to add bins | number of inputs grows with tracers | SPHEREx, arXiv:2603.16003, Sect. III |
| Simulation P(k) | — | non-linear scales | inherits resolution, volume and shot noise of the runs | DarkEmulator2, arXiv:2605.28596, Sects. 2–4 |

Effort keeps biases out of the network, unlike EmulateLSS, because including them "can lead to
the need for more complex NNs" [src: arXiv:2501.04639, Sect. 2.2]. PyBird-Emu emulates only the
numerically expensive parts: one-loop terms with one network per multipole and two networks for
the IR-resummation corrections of the linear and counterterm pieces [src: arXiv:2507.20990,
Sect. 2.1, Training].

### Step 2. Design the training set
<!-- key: step-2-design-the-training-set -->

Five designs are in use:

- **Latin hypercube over broad ranges.** CosmoPower trains on ranges chosen to make the tool "as
  general as possible" (its Table 1) and uses ~5 × 10⁵ CAMB spectra per CMB probe; the sampling
  scheme mattered less than the number of points, with orthogonal or plain uniform sampling giving
  "essentially the same accuracy", because scheme differences fade as the number of parameters
  grows [src: arXiv:2106.03846, Sects. 2, 4.1]. Effort uses 60 000 Latin-hypercube points with
  z as an input (0.25–2.0) [src: arXiv:2501.04639, Sect. 4.1, Table 1].
- **Uniform hypersphere.** SPHEREx samples inside a hypersphere, cutting low-probability corners;
  four million ps_1loop evaluations, split 80/10/10 [src: arXiv:2603.16003, Sect. II.2].
- **Posterior-concentrated, iterative.** CONNECT trains a first network on ~10⁴ Latin-hypercube
  points, runs a high-temperature MCMC with it (L → L^{1/T}, T = 5, so samples lie mainly inside
  the 5σ contour), computes CLASS only at the kept points, retrains and repeats until the kept
  points of two iterations agree [src: arXiv:2205.15726, Sects. 3, 3.1]. The motivation is the
  volume ratio of a hypersphere to its cube, r_n = π^{n/2}/(2ⁿ Γ(n/2 + 1)) (Eq. 4): with 9
  parameters less than 1% of the cube lies in the sphere [src: Sect. 3]. New points closer than
  two standard deviations of the local neighbour distance are discarded, because oversampled
  regions weigh more in the loss and bias the network; the first iteration (and the initial
  hypercube) is dropped because it is off target [src: Sect. 3.2]. For decaying dark matter the
  final set had 19 999 + 7475 + 4781 + 2415 points from iterations 2–5 [src: Sect. 3.2].
- **Copula-inflated bank.** PyBird-Emu draws 10⁶ CLASS spectra from wide Gaussians around Planck
  values (two to three times the BOSS 1σ widths; 25 times the BBN width for ω_b), maps each to 80
  log band powers plus P_max and f, fits a Gaussian copula to their correlations, inflates its
  covariance by α = 1.2 to reach beyond the parent bank while keeping smooth spectra
  (Eqs. 2.4–2.7), and runs PyBird-JAX on 10⁷ such samples [src: arXiv:2507.20990, Sect. 2.1,
  Table 1]. z is drawn log-normal (peak at 0.6, clipped to [0.005, 4]) because a uniform z gives
  amplitudes piled up near zero [src: same].
- **Weighted sequential design with a linear-spectrum cut** (simulations). DarkEmulator2 draws
  Ω_m, σ8 inside a curved band set by the HSC Y1 shear constraints, the other parameters uniformly
  (w0 and w0 + w_a in [−1.5, −0.5] with |w_a| < 0.5), and keeps draws whose mean fractional
  distance to the fiducial linear spectrum is D < 5 (Eq. 2), which removes extreme linear shapes
  while covering −2.9σ/+5.8σ in Ω_m and −3.3σ/+3.8σ in σ8 relative to HSC Y1 [src:
  arXiv:2605.28596, Sect. 2.2].

### Step 3. Transform the target
<!-- key: step-3-transform-the-target -->

- **Log and standardise.** CosmoPower takes log P and standardises each feature, because the log
  makes an MSE loss optimise fractional accuracy and standardisation speeds convergence [src:
  arXiv:2106.03846, Sect. 2]. CONNECT compared min–max, log and standardisation of outputs:
  standardisation was slightly better than min–max and both beat log scaling once derived
  parameters share the output layer [src: arXiv:2205.15726, Sect. 2.4].
- **PCA when the log is impossible.** C_ℓ^TE crosses zero, so CosmoPower emulates 512 principal
  components; C_ℓ^φφ is emulated through 64 components, which worked better, possibly because its
  log values (−6 to −20) cause numerical issues [src: arXiv:2106.03846, Sect. 2, App. A.2].
  PyBird-Emu compresses outputs of size O(10⁴) to 256 components for memory and stability [src:
  arXiv:2507.20990, Sect. 2.1].
- **Whitening.** SPHEREx rotates each multipole vector into the eigenbasis of the data covariance
  and subtracts the fiducial, P̂ = (Q⁻¹P − Q⁻¹P_fid)/√Σ (arXiv:2603.16003, Eqs. 4–5); unlike PCA
  it keeps all components [src: Sect. II.2].
- **Physics-based rescaling.** Effort divides P_11 and the counterterm piece by A_s D²(z) and the
  loop by (A_s D²)², leaving the network the residual from IR resummation and neutrinos [src:
  arXiv:2501.04639, Sect. 2.3]. On 20 000 and 60 000 training points the rescaling improves the
  95% error band more than tripling the training set does [src: Sect. 4.1, Fig. 2].
- **Fiducial-normalised boost with a taper** (simulations). DarkEmulator2 divides by the fiducial
  linear spectrum, B_fid = P_sim/P_lin,fid (Eq. 6), so all targets share one denominator, takes
  log₁₀, and multiplies by (k/k_0)^{−3/4} above k_0 = 0.1 h Mpc⁻¹ to make residuals closer to
  homoscedastic under an L2 loss; k_0 and −3/4 are "empirical choices" [src: arXiv:2605.28596,
  Sect. 2.5].

### Step 4. Choose the network, loss and schedule
<!-- key: step-4-choose-the-network-loss-and-schedule -->

| Emulator | Network | Loss | Schedule and data split | Place read |
|---|---|---|---|---|
| CosmoPower | 4 hidden layers × 512; trainable activation f(x) = (γ + (1 + e^{−β⊙x})⁻¹ ⊙ (1 − γ)) ⊙ x (Eq. 14), slightly better than tanh or ReLU | MSE | Adam; lr 10⁻² divided by 10 after 20 epochs without validation gain, down to 10⁻⁶; batch 10³ → 10⁴ → 5 × 10⁴; 20% validation | arXiv:2106.03846, App. A.1 |
| CONNECT | 6 × 512; same activation; above ~12 layers (~3 × 10⁶ parameters) slower than the Planck-lite likelihood | MSE, or L_CV = (1/n) Σ (2ℓ + 1)/2 (x_i − y_i)² (Eq. 2) for CMB, which trades low-ℓ for high-ℓ accuracy and improves inference | — | arXiv:2205.15726, Sects. 2.1–2.3 |
| Effort | 5 × 64 | MSE; 1/k²-weighted for the PT challenge | 60 000 points, 80/20, batch 128, 10⁵ epochs, Adam 10⁻⁴; ~1 h on 8 CPU cores; weights kept only when test loss improves | arXiv:2501.04639, Sect. 4.1 |
| SPHEREx | 4 residual MLP blocks of 2 layers, then one transformer block; one network per auto or cross spectrum | χ² loss ⟨Δχ²⟩ or ⟨√(1 + 2Δχ²)⟩ − 1 (Eqs. 9–10), equivalent within 0.5% | Adam, lr 0.005; ÷10 after 15 epochs without gain; early stop after 25; batch 200 | arXiv:2603.16003, Sects. III, IV.1, Table 2 |
| PyBird-Emu | 3 × 512, CosmoPower activation | MSE on PCA coefficients | 10⁷ samples, 80/20; batch 1024; 1000 epochs at each of 5 learning rates from 10⁻³ to 5 × 10⁻⁵ | arXiv:2507.20990, Sect. 2.1 |
| DarkEmulator2 (non-linear) | 3 × 2000, ELU, LAMB optimiser | RMSE of the tapered target (Eq. 12) | 2240 runs from 1000 cosmologies; Monte Carlo cross-validation with five 90/10 splits by cosmology; 5000 epochs, batch 50 | arXiv:2605.28596, Sect. 3.2, Table 3 |

**Hyperparameter search.** CosmoPower did not search exhaustively and found at least three hidden
layers of a few hundred neurons necessary [src: arXiv:2106.03846, App. A.1]. SPHEREx varied one
hyperparameter at a time around defaults, scored by the median Δχ²_tot, and kept batch 200 and one
transformer block although smaller batches and more blocks were marginally better, for training
time [src: arXiv:2603.16003, Sect. IV.1]. DarkEmulator2 used CMA-ES over layers (1–11), neurons
(400–3000), epochs, batch, six activations, six optimisers and eight schedulers, because the
mixed discrete–continuous, noisy objective and batch-parallel evaluation made grid search,
Nelder–Mead and GP Bayesian optimisation less practical [src: arXiv:2605.28596, App. E, Table 10].

### Step 5. Set the accuracy requirement in units of the survey
<!-- key: step-5-set-the-accuracy-requirement-in-units-of -->

- **CMB.** Error in units of σ_ℓ = √(2/(f_sky(2ℓ + 1))) (C_ℓ + N_ℓ) with Simons Observatory goal
  noise and f_sky = 0.4 (arXiv:2106.03846, Eqs. 11–13); 99% of test spectra lie within 0.1σ on a
  5σ Planck range and reach 0.2σ on the full training range [src: Sect. 4.1].
- **Galaxy multipoles.** PyBird-Emu quotes residuals in units of a Stage-IV σ for
  V_eff = 50 Gpc³ and n̄ = 5 × 10⁻⁴ h³ Mpc⁻³: 95% below 0.1σ to k_max = 0.2 h Mpc⁻¹, ~0.5σ at
  0.3 h Mpc⁻¹, and notes the volume per redshift bin is usually below 10 Gpc³ [src:
  arXiv:2507.20990, Sect. 2.2]. SPHEREx requires the median
  Δχ²_tot < 1, "the criterion used by both the DES collaboration, and other cosmological
  emulators", and obtains 0.069 [src: arXiv:2603.16003, Sect. IV.2].
- **Per-bin requirement.** A redshift bin holds less volume than the total survey volume used for
  the PyBird-Emu units, so the requirement per bin is looser than the quoted one [der].
- **Why a per-cent residual is not a requirement.** "It is the inference pipeline that dictates
  the accuracy threshold"; emulators that performed well for Stage III failed on a simulated
  Stage IV survey [src: arXiv:2106.03846, Sect. 5.2].

### Step 6. Validate inside the inference
<!-- key: step-6-validate-inside-the-inference -->

| Test | Outcome | Place read |
|---|---|---|
| CosmoPower against CLASS, Euclid-like cosmic shear, 10 bins, PolyChord | contours agree; log Z = −45.92 ± 0.33 (CLASS) against −45.99 ± 0.34; speed-up ~50 on 48 cores | arXiv:2106.03846, Sect. 3.4 |
| CONNECT against CLASS, Planck lite, DCDM and massive-neutrino models | means and widths within 0.01–0.1σ (DCDM) and ≲ 10⁻²σ except H0 at ~10⁻¹σ (neutrinos); ~5000 against ~10 CPU core-hours; agreement out to 5σ | arXiv:2205.15726, Sect. 4.2 |
| SPHEREx emulator against ps_1loop, nautilus | one tracer and bin (12 parameters): mean cosmology best-fit shift 0.091σ, width change 1.38%; two tracers and bins: 0.145σ, 1.44%; Δlog Z = −0.06 and 0.78 against log Z = −33.03 and −86.28 | arXiv:2603.16003, Sect. V, Table 3 |
| Effort against PyBird, PT challenge (566 (h⁻¹Gpc)³, k_max = 0.12) and BOSS (k_max 0.23 CMASS, 0.20 LOWZ) | agreement "consistent with Montecarlo noise"; ~10 minutes on a laptop with NUTS and MCHMC | arXiv:2501.04639, Sect. 4.2 |

The SPHEREx abstract figures carried in L2 (0.078σ, 0.82%) are not single rows of Table 3:
Sect. V.1 gives them as the average 1D best-fit shift and the mean absolute uncertainty
difference over the parameters of Table 3, and Sect. VI assigns them to the multi-tracer analysis
with the stochastic and counterterm parameters fixed; the more ambitious run of Sect. V.1 has the
same 0.078σ average shift but a 3.26% uncertainty difference (arXiv:2603.16003, abstract,
Sects. V.1, VI).

**Map the error over parameter space.** SPHEREx plots the median Δχ²_tot in every 2D projection,
marginalising the other parameters (arXiv:2603.16003, Eq. 12): stable except along edges, so no
bias is expected "so long as said analyses does not hit the parameter domain boundary" [src:
Sect. IV.2, Fig. 4].

### Step 7. Propagate the residual error
<!-- key: step-7-propagate-the-residual-error -->

The marginal posterior over the emulator residual is P(p ∣ x) ∝ ∫ L(x ∣ p, Δ) π(p) D(Δ) dΔ
(Grandón & Sellentin 2022, arXiv:2205.11587, Eq. 1). For Gaussian data and Gaussian residuals with
mean Δ̄ and covariance Σ estimated on V validation points (Eqs. 4–5),
P(p ∣ x) ∝ exp(−½ [ξ(p) − Δ̄]ᵀ Ψ [ξ(p) − Δ̄]) π(p) with ξ = x − μ(p) and Ψ = (C + Σ)⁻¹
(Eqs. 7–8): the mean residual is subtracted and Σ is added to the data covariance [src:
Sects. 2.1–2.2]. Preconditions: the prior on p and the residual distribution factorise, which
fails for unrepresentative training with empty sub-volumes [src: Sect. 2.1]; Δ is Gaussian,
checked per k with histograms, skewness, kurtosis and Kolmogorov–Smirnov tests; Δ does not depend
on p, checked by sub-volume means [src: Sect. 3]. The demonstration used 10 000 CAMB spectra
(70/20/10) and a fresh set of 10 000 for Δ̄ and Σ; an "accurate" net (per-cent errors, up to 5%)
and an "inaccurate" one (up to 40%): the naive posterior of the inaccurate net excludes the input
cosmology, the propagated one includes it and is wider [src: Sect. 3]. For heavy-tailed or bimodal
residuals the closed form does not hold [src: Sect. 4].

A smaller version is common for GP emulators: add the GP predictive variance to the covariance
diagonal. Vinciguerra et al. do so, and check that the data noise per bin exceeds the GP
uncertainty by more than five on average (5.4 and 10.9 for the two MOPED bins) [src:
arXiv:2607.17942, App. A].

### Step 8. Simulation-trained emulators: resolution and cosmic variance
<!-- key: step-8-simulation-trained-emulators-resolution -->

- **Resolution as an input.** DarkEmulator2 feeds N_p^{1/3} and L_box to one network trained on
  1000 LF, 50 MF and 20 HF runs, nested so that 20 cosmologies exist at all three resolutions;
  low-resolution spectra deviate from high-resolution ones from about a third of their Nyquist
  wavenumber [src: arXiv:2605.28596, Sect. 4.2]. On the MF test set, 50 MF runs alone are not
  enough; with the 1000 LF runs the mean error falls steeply for the first ~10 MF runs and levels
  at MAPE ≃ 0.4% (Eqs. 13–14) for N_MF ≃ 40–50 [src: same, Figs. 9–10]. Storage and compute are
  7.2% and 4.2% of an all-HF suite of equal coverage [src: Table 5]. No independent HF test set
  exists yet [src: Sect. 4.2].
- **Cosmic variance.** DarkEmulator2 (arXiv:2605.28596) conditions on a white-noise input W and
  calibrates the single-call prediction at W = 1 to the mean over 500 noise draws, a ~0.1% correction with
  cosmology scatter of a few 10⁻⁴ (Eqs. 22–24) [src: Sect. 4.3.4].
- **A GP on simulation summaries.** 250 of 4609 Latin-hypercube nodes, one GP per compressed bin,
  constant × Matérn-5/2 with one length scale per parameter plus white noise (Eq. 11), 10 restarts
  of the marginal-likelihood optimiser; more nodes gave consistent posteriors [src:
  arXiv:2607.17942, Sect. 5.1].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Latin hypercube, hypersphere or posterior-concentrated design
<!-- key: latin-hypercube-hypersphere-or-posterior -->

- **Same emulator, two designs.** Hypersphere sampling gives a median Δχ²_tot two orders of
  magnitude below a Latin hypercube with the same number of points; both improve as
  Med(Δχ²_tot) = A N^{−x} (Eq. 11) with x = 0.798 (hypersphere) and 0.771 (hypercube), so
  doubling the accuracy needs about 2.4 times more samples [src: arXiv:2603.16003, Sect. IV.2].
  The cost is global generalisation: centre the sphere on a reference cosmology and retrain if a
  posterior reaches the boundary [src: same].
- **Iterative against hypercube.** For DCDM, a CONNECT network trained on 34 670 iteratively
  sampled points beats Latin-hypercube networks with 34 670 and 10⁶ points; for massive neutrinos
  more than 10⁶ hypercube points are needed to approach 38 959 iterative ones, and a hypercube
  fails to represent models near a prior boundary toward which the likelihood rises [src:
  arXiv:2205.15726, Sect. 4.2]. The reason given: a finite network spends capacity on the
  irrelevant corners [src: same]. The cost: the emulator is accurate only near the posterior of the
  likelihood used to train it, out to roughly the temperature chosen [src: Sect. 3].
- **Broad-range training** buys reuse across analyses (KiDS and Euclid-like with the same
  emulator) [src: arXiv:2106.03846, Sect. 3.2] and costs accuracy on the full range (0.2σ against
  0.1σ near the Planck region) [src: Sect. 4.1].

### What the inputs are
<!-- key: what-the-inputs-are -->

Cosmological parameters fix the model: CosmoPower cannot sample both A_s and σ8 and recovers the
other through a GP (ARD Matérn-3/2, Eqs. 15–16) [src: arXiv:2106.03846, Sect. 2, App. A.3]. A
spline of P_lin removes the model dependence; the 80-knot spline costs at most 3% of a Stage-IV σ
at the 95% quantile [src: arXiv:2507.20990, Sect. 2.1, Fig. 1]. The authors rejected an FFTLog
basis (512 functions in PyBird) as too large and an optimised few-function basis (COBRA, N ~ 10)
because it is tuned to a cosmology bank and needs re-testing outside it [src: same].

### Neural network or Gaussian process
<!-- key: neural-network-or-gaussian-process -->

GPs need fewer training samples and give a predictive uncertainty that can be propagated, but
give smaller speed-ups [src: arXiv:2106.03846, Sect. 5.2]. GokuNEmu replaced its GP by a neural
multi-fidelity network for scalability (L2). On a two-parameter problem a GP on 250 nodes and an
MLP cross-check gave "highly consistent results" [src: arXiv:2607.17942, Sect. 5.1].

### One emulator for all redshifts or one per bin
<!-- key: one-emulator-for-all-redshifts-or-one-per-bin -->

Effort trains one emulator with z as input so that no retraining is needed, and notes that a
fixed-z emulator "naturally leads to a more precise surrogate" when a survey has few effective
redshifts [src: arXiv:2501.04639, Sect. 4.1].

### Hierarchical or integrated multi-fidelity
<!-- key: hierarchical-or-integrated-multi-fidelity -->

Hierarchical schemes keep one model per fidelity and learn a correction between levels; resolution
as a continuous input avoids fixing the hierarchy in advance [src: arXiv:2605.28596, Sect. 4.2].
The integrated scheme is validated only to MF so far [src: same].

### Propagate the error or show it is negligible
<!-- key: propagate-the-error-or-show-it-is-negligible -->

Propagation (Step 7) needs a validation set of 10⁴ fresh evaluations and Gaussian, parameter-
independent residuals [src: arXiv:2205.11587, Sect. 3]. CosmoPower and CONNECT instead rerun the
final inference with the exact code (Step 6). The statistics sibling found no survey analysis
that adopted the propagation (`cosmo-statistics-inference`, open-questions, Sect. 7).

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| CMB training set | ~5 × 10⁵ CAMB spectra per probe, LHS | CosmoPower | arXiv:2106.03846 | Sect. 4.1 |
| CMB accuracy | 99% within 0.1σ (5σ range), 0.2σ (full range), SO noise, f_sky = 0.4 | CosmoPower | arXiv:2106.03846 | Sect. 4.1 |
| PCA components | 512 (TE), 64 (φφ) | CosmoPower | arXiv:2106.03846 | App. A.2 |
| Boltzmann k_max requested | 100 Mpc⁻¹ for use to 10 Mpc⁻¹ | CosmoPower | arXiv:2106.03846 | Sect. 3.2 |
| Evidence, exact vs emulated | −45.92 ± 0.33 vs −45.99 ± 0.34 | Euclid-like shear | arXiv:2106.03846 | Sect. 3.4 |
| Sampling temperature | T = 5 (≈ 5σ coverage) | CONNECT | arXiv:2205.15726 | Sect. 3 |
| Iterative vs LHS | 34 670 iterative points beat 10⁶ LHS points | CONNECT, DCDM | arXiv:2205.15726 | Sect. 4.2 |
| Hypersphere vs LHS | median Δχ²_tot × 10⁻²; scaling exponents 0.798, 0.771 | SPHEREx | arXiv:2603.16003 | Sect. IV.2 |
| Accuracy criterion | median Δχ²_tot < 1; achieved 0.069 | SPHEREx | arXiv:2603.16003 | Sect. IV.2 |
| Posterior shifts | 0.091σ / 1.38% (1 tracer), 0.145σ / 1.44% (2 tracers) | SPHEREx | arXiv:2603.16003 | Table 3 |
| Copula inflation | α = 1.2; 10⁷ training samples; 80 knots in (10⁻⁴, 0.7) h Mpc⁻¹ | PyBird-Emu | arXiv:2507.20990 | Sect. 2.1 |
| Spline error | ≤ 3% of a Stage-IV σ at the 95% quantile | PyBird-Emu | arXiv:2507.20990 | Sect. 2.1 |
| Effort network | 5 × 64; 60 000 samples; ~1 h on 8 cores; 15 µs per multipole | Effort | arXiv:2501.04639 | Sects. 2.1, 4.1 |
| MF runs needed | MAPE ≃ 0.4% plateau at N_MF ≃ 40–50 with 1000 LF | DarkEmulator2 | arXiv:2605.28596 | Sect. 4.2 |
| Mixed-resolution cost | 7.2% storage, 4.2% compute of all-HF | DarkEmulator2 | arXiv:2605.28596 | Table 5 |
| Supported resolution | stable to N_p^{1/3} = 3100; artefacts from 3200 | DarkEmulator2 | arXiv:2605.28596 | App. D |
| Error propagation set | 10 000 fresh spectra; Ψ = (C + Σ)⁻¹ | toy P(k) | arXiv:2205.11587 | Sect. 3, Eq. 8 |
| GP calibration flag | WARN if abs(a − 1) > 0.10 or abs(b) > 0.10; bin 1: a = 0.710, b = 0.335 | Euclid-like GRF | arXiv:2607.17942 | App. A |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Residuals pass, posterior fails.** Sub-percent residuals did not guarantee unbiased Stage-IV
  contours [src: arXiv:2106.03846, Sect. 5.2]. Test: full inference with the exact code on mock
  data with the target covariance.
- **Small predictive variance, wrong mean.** For one compressed bin the GP uncertainty was ten
  times below the data noise, yet the true-versus-predicted slope was 0.710; this, with mild
  likelihood non-Gaussianity, made the explicit likelihood miscalibrated in TARP and up to about
  twice as wide in Ω_m as the learned likelihood [src: arXiv:2607.17942, Sect. 7.1, App. A].
  Test: regress predicted on true over test nodes, flag abs(a − 1) or abs(b) above 0.10 [src:
  App. A]. The bin carried little cosmological information, which the authors give as the reason it
  was hard to emulate; more realisations per node would help [src: Sect. 5.1].
- **Queries outside the training box.** Errors rise at the edges (SPHEREx Fig. 4; DarkEmulator2,
  L2); resolution extrapolation beyond N_p^{1/3} = 3100 gives oscillatory artefacts; beyond
  z = 3 only qualitative behaviour to z ≃ 4 [src: arXiv:2603.16003, Sect. IV.2;
  arXiv:2605.28596, App. D]. Test: posterior distance to the boundary, error maps over parameter
  pairs.
- **Training points where the posterior is not.** Off-target points (first iteration, initial
  hypercube) cost accuracy where it matters; oversampled regions bias the loss [src:
  arXiv:2205.15726, Sects. 3.1–3.2].
- **Δχ² grows with the data vector.** The total Δχ² exceeds the sum of per-network values because
  of off-diagonal covariance blocks, so adding tracers or bins raises it at fixed per-network
  accuracy [src: arXiv:2603.16003, Sect. IV.2]. Test: quote Δχ² with the full covariance.
- **Non-Gaussian residuals.** The (C + Σ)⁻¹ correction assumes Gaussian residuals; bimodal or
  heavy tails need another D(Δ) or better training [src: arXiv:2205.11587, Sect. 4].
- **Shot-noise floor at high k.** Simulation emulators can flatten at the shot-noise level near
  k ≃ 100 h Mpc⁻¹, which adds spurious power to ξ(r) and C(ℓ) integrals; DarkEmulator2 replaces
  the tail above the point where P = 10 P_sn [src: arXiv:2605.28596, App. D].
- **Numerical noise in the training code.** CosmoPower asks the Boltzmann code for k_max =
  100 Mpc⁻¹ and for every ℓ explicitly to reduce internal interpolation [src: arXiv:2106.03846,
  Sect. 3.2, App. A.1].
- **Fixed parametrisation.** Sampling σ8 instead of A_s with an A_s-trained emulator needs a
  derived-parameter mapping [src: arXiv:2106.03846, Sect. 2].

## Reading list
<!-- key: reading-list -->

- Method: Spurio Mancini et al. 2022, arXiv:2106.03846 — direct and PCA emulation, training
  schedule, survey-unit accuracy, why only full inference validates.
- Method: Nygaard et al. 2022, arXiv:2205.15726 — posterior-concentrated iterative design,
  cosmic-variance loss, normalisation comparison.
- Method: Grandón & Sellentin 2022, arXiv:2205.11587 — closed-form propagation of emulator bias
  and scatter, and its preconditions.
- Method: Bonici et al. 2025, arXiv:2501.04639 — analytic bias, physics-based rescaling of
  outputs, small networks, HMC with differentiable emulators.
- Method: Reeves et al. 2025, arXiv:2507.20990 — model-independent inputs, copula-inflated
  training bank, accuracy in Stage-IV σ.
- Application: Adamo et al. 2026, arXiv:2603.16003 — hypersphere design, Δχ² loss and criterion,
  scaling with training size, end-to-end shifts.
- Application: Tanaka et al. 2026, arXiv:2605.28596 — simulation design, targets, CMA-ES,
  resolution-conditioned training, behaviour outside the domain.
- Critique: Vinciguerra et al. 2026, arXiv:2607.17942 — emulator calibration bias that the
  predictive variance does not reveal, and its effect on an explicit likelihood.
- Foundation: Heitmann et al. 2009, arXiv:0902.0429 — precision emulation of the non-linear
  spectrum from a small simulation design.

## Not verified
<!-- key: not-verified -->

- The GokuNEmu hyperparameter search and k-fold details beyond L2, and the GP emulator it replaced:
  not re-read here.
- EuclidEmulator2, BACCO and Mira-Titan design choices: read only through the
  `cosmo-simulations-mocks` and `cosmo-statistics-inference` reference files.
- The DES "Δχ² < 1" emulator criterion: quoted through arXiv:2603.16003; the DES source was not
  read.
- Capse.jl (the CMB emulator of the Effort authors) and its factor-of-three gain from rescaling by
  A_s: cited inside arXiv:2501.04639, not read.
