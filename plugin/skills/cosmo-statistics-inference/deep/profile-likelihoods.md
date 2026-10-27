# Profile likelihoods — cosmo-statistics-inference dossier

Scope: how a cosmological profile likelihood is computed in practice (best fit, grid, optimiser,
initialisation, interpolation), how it is turned into an interval near and away from a boundary,
how its validity is checked with mocks, and how it is used, next to the MAP with a projected
interval, to diagnose projection effects; the definitions, the boundary formulae and the
published comparisons are in the reference files.
Snapshot: 2026-10-16.
From: CosmoVerse White Paper, Sect. 3.6; Herold et al. 2024, Sects. II-III.

Prerequisites at L2: the profile, Wilks, Wald and boundary-corrected statistics and the
Feldman–Cousins ordering are in `physics-and-methods.md#construction`; when the graphical
construction can be trusted (Planck-lite tests) in
`physics-and-methods.md#when-the-graphical-construction-can-be-trusted`; the published
profile-against-posterior pairs in `results.md#profile-likelihood-against-posterior-on-the`;
projection effects in `systematics.md#projection-prior-volume-effects`; the debate in
`open-questions.md#frequentist-against-bayesian-intervals-in`. Notation: `μ` the profiled
parameter, `ν` all others, `ν̂̂(μ)` their conditional maximum-likelihood values, as in Herold et
al. 2024 (arXiv:2408.07700).

## How it is done
<!-- key: how-it-is-done -->

### Step 0. Decide between the graphical construction and a Neyman construction
<!-- key: step-0-decide-between-the-graphical -->

The CosmoVerse review and Herold et al. 2024 give the same decision rule. A full Neyman
construction guarantees coverage but is "computationally expensive"; if mock data and likelihood
evaluations are fast it is feasible, otherwise "the only feasible option might be the graphical
profile likelihood method", used "while acknowledging that correct coverage might not be
fulfilled" (arXiv:2408.07700) [src: Sects. II.2–II.3]. The cookbook then has two steps: compute
the profile with an efficient minimiser; read the interval from iso-likelihood contours if no
boundary is near, or with the boundary-corrected construction if one is [src: Sect. II.3].

A parabolic profile is not evidence that the graphical interval covers. "A parabolic profile
likelihood shows only that the likelihood for the observed data is Gaussian"; coverage needs a
Gaussian likelihood "for all choices of model parameters and (hypothetically observed) data".
w0CDM with Planck-lite has a near-parabolic profile around the best fit while the mock tests
show Wilks' theorem failing (arXiv:2408.07700) [src: Sect. II.2].

### Step 1. Find the global best fit
<!-- key: step-1-find-the-global-best-fit -->

The denominator of the likelihood ratio is the global maximum; an error there shifts every interval.

- DESI DR1 full shape (Morawetz et al. 2025, arXiv:2508.11811): the MAP with the L-BFGS
  algorithm of Optim.jl, from 50 independent optimisations with random starting locations [src:
  Sect. 3.2]; the maximum-likelihood point by the same procedure with the Gaussian priors on the
  EFT nuisance parameters removed [src: Sect. 3.3]. The likelihood is an emulator, which makes a
  quasi-Newton optimiser usable.
- KiDS-1000 (Joachimi et al. 2021, arXiv:2007.01844): "the largest posterior returned by a suite
  of tens of optimisation runs, each started at the position of a different posterior sample
  with high probability mass" [src: Sect. 6.4]. DES Y6 starts a Powell optimiser from the 20
  best samples (`surveys-and-data.md#des`).
- Procoli (Karwal et al. 2024, arXiv:2401.14225) starts from the MAP and covariance of a
  converged MCMC to find the global best fit before profiling (as summarised in the CosmoVerse
  White Paper, Di Valentino et al. 2025, arXiv:2504.01669) [src: Sect. 3.6.3.a].

### Step 2. Choose the grid of profiled values
<!-- key: step-2-choose-the-grid-of-profiled-values -->

DESI DR1, the most fully documented collaboration recipe (arXiv:2508.11811) [src: Sect. 3.3]:

1. Profile bounds fixed in advance from test runs, to cover approximately the `Δχ² ≤ 9` (3σ) region.
2. 16 entries per one-dimensional profile, with extra entries where the interpolation showed
   features (arXiv:2508.11811) [src: Sect. 3.3].
3. 10 to 20 independent optimisations per entry (arXiv:2508.11811) [src: Sect. 3.3]: the first started from the exact
   maximum-likelihood point (profiled parameter excepted), the others from the
   maximum-likelihood point displaced at random by amounts proportional to the MCMC variance;
   more for data sets without supernovae, and more again for noisy entries.
4. Quadratic interpolation in log-likelihood space between entries, so that the minimum `χ²` is
   not tied to a grid point and the `Δχ²` crossings can be found.
5. Two-dimensional profiles on a 16 × 16 grid, contours by cubic interpolation (arXiv:2508.11811) [src: Sect. 3.3].

The intervals are read at `Δχ²(θ_i) < 1 (4)` in one dimension and `Δχ²(θ_i, θ_j) < 2.30 (6.17)`
in two, with `Δχ² ≡ −2 log(L(θ_i)/L_max)` [src: Eqs. 2–3]; the paper states that the asymptotic
assumption "does not strictly hold" for some of its likelihoods, particularly in w0waCDM [src:
Sect. 3.3].

### Step 3. Choose the optimiser
<!-- key: step-3-choose-the-optimiser -->

Two families, with the reason for each.

- **Gradient-based**: MIGRAD of MINUIT, a variable-metric algorithm on finite-difference
  derivatives, "computationally efficient" in several profile analyses (arXiv:2504.01669) [src:
  Sect. 3.6.3.a]; L-BFGS on an emulated likelihood (arXiv:2508.11811) [src: Sect. 3.2]. DESI DR2
  neutrino profiles use iminuit, with 14 free parameters for DESI BAO + CMB and up to 44 for
  DESI full shape + BAO + CMB (Elbers et al. 2025, arXiv:2503.14744) [src: Sect. V.1].
- **Simulated annealing**: cosmological likelihoods "can be noisy due to the use of different
  approximation schemes in different parts of the parameter space or insufficient precision" of
  the Boltzmann solver, and then annealing "often outperform[s]" gradient methods
  (arXiv:2408.07700) [src: Sect. IV]. Procoli calls it "rapidly becoming the industry standard"
  for cosmological profiles (arXiv:2401.14225) [src: Sect. II.1].

How annealing is set up, in the notation of each code:

- Acceptance on a tempered likelihood: the move is accepted if `x < (L_new/L_old)^(1/T)` for `x`
  uniform in [0, 1] (Procoli, arXiv:2401.14225) [src: Sect. II.1]; equivalently a Metropolis
  chain on `L̃ ≡ L^(1/T)` (PROSPECT, Holm et al. 2023, arXiv:2312.02972) [src: Sect. 3.1, Eq.
  4]; pinc writes the acceptance as `P ∼ exp(−(L_{i+1} − L_i)/T)` with `L` the negative
  log-likelihood [src: arXiv:2408.07700, Eq. 11].
- Step size falls with temperature. Procoli steps by `Δθ_j ≃ δ sqrt(Σ_jj)` [src: Eq. 3], against
  `δ ≈ 2.4` for an ordinary Metropolis–Hastings chain, and aims at a roughly constant acceptance
  rate [src: Sect. II.1]. PROSPECT adapts the step size each iteration, `S_{i+1} = (1 − m) S_i`
  if the acceptance rate `A_i < A_t` and `(1 + m) S_i` otherwise [src: Eq. 5], with `m ≈ 0.5`
  and `A_t ≈ 0.2` found to work well [src: Sect. 3.1].
- Schedule. Annealing is "only provably convergent to the global optimum when the temperature
  decreases logarithmically", which is slow; PROSPECT uses an exponential schedule by default,
  without the guarantee, which "works well when starting the optimisation from the basin of the
  global optimum" [src: Sect. 3.1].
- Repeats. PROSPECT runs `m` independent optimisations per profile point, "typically around 2 –
  3", and keeps the best [src: Sect. 3.1]; Procoli takes the minimum over parallel annealed
  chains [src: Sect. II.1].
- Hyperparameters matter: annealing "is very sensitive to its hyperparameters", namely the
  starting point, the proposal covariance and the cooling rate (arXiv:2504.01669) [src: Sect.
  3.6.3.a].

### Step 4. Initialise each point of the profile
<!-- key: step-4-initialise-each-point-of-the-profile -->

Three strategies are in use (arXiv:2504.01669) [src: Sect. 3.6.3.a]:

| Strategy | Code | Gains | Cost |
|---|---|---|---|
| One MCMC per fixed value of the profiled parameter, its best fit and covariance as start | earlier profile analyses | "great initial points and local covariance matrices" | extra MCMCs |
| Bins of an existing converged MCMC: start and local covariance from the points nearest the fixed value | CAMEL, PROSPECT | good starts at no sampling cost | "sensitive to the quality of the initial mcmc" |
| Sequential: each optimisation starts from the result of the previous profile point | Procoli | "great initial points" | no parallelism along the profile |

PROSPECT's bin is the fraction `ξ` of chain points with the profiled parameter closest to the
target, starting from the highest-likelihood point among them; `ξ ≈ 0.1` "to work well for all
cases studied", `ξ = 0.1` and `0.01` giving start points only `Δ log L ≈ 5` above the converged
profile (arXiv:2312.02972) [src: Sect. 3.2].

The binned chain is a start, not a profile. On Planck CMB primaries for early dark energy, the
MAPs of narrow MCMC bins lie more than 4 in `χ²` above the Procoli minima, the binned curve is
"extremely jagged" and biased towards low `f_ede`, partly by prior volume (arXiv:2401.14225)
[src: Sect. III.2]. With the same inputs, a sequential Minuit profile stayed in the local
minimum with `log10 z_c > 3.7` for every `f_ede`, while annealing found the global best fit at
`log10 z_c = 3.57`, the MCMC MAP being at 3.82 [src: Sect. III.2]. The authors add that this
example "does not generalize divergent results" between the two optimiser families [src: Sect.
III.2].

### Step 5. Turn the profile into an interval near a boundary
<!-- key: step-5-turn-the-profile-into-an-interval-near-a -->

The neutrino-mass recipe of DESI DR2 (arXiv:2503.14744) [src: Sect. V.1], reproduced in the
frequentist overview of Chebat et al. 2025 (arXiv:2507.12401) [src: Sects. 2.1–2.2]:

1. Profile only the physical side, `Σm_ν > 0`; nuisance parameters of the CMB and full-shape
   likelihoods keep "penalties as prescribed by their respective frameworks", so the profile is
   not entirely prior-free [src: arXiv:2503.14744, Sect. V.1].
2. Because the data are close to Gaussian, fit the profile with a parabola and extend it into
   the unphysical region; report its minimum `μ_0` and scale `σ`, the latter "directly
   interpreted as the constraining power" [src: Sect. V.1]. Chebat et al. write the fit as `x ↦
   (x − μ_0)²/σ² − χ²_0` with `Δχ²` measured from `Σm_ν = 0.005 eV`, the offset `χ²_0` measuring
   the tension between zero mass and the parabola's minimum [src: arXiv:2507.12401, Sect. 2.1,
   Eq. 3].
3. Build the 95% limit `μ_95` from `μ_0` and `σ` with the Feldman–Cousins prescription [src:
   arXiv:2503.14744, Sect. V.1]. Chebat et al. generalise the lower boundary: ordering ratio
   `R(x, μ) = exp(−(x − μ)²/2)` for `x ≥ μ_inf` and `exp(−(x − μ)²/2)/exp(−(μ_inf − μ)²/2)`
   below, applied with `μ_inf = 0`, 59 meV and 100 meV for no prior, normal and inverted
   ordering (arXiv:2507.12401) [src: Sect. 2.2, Eq. 4]. Condition: a Gaussian likelihood in the
   profiled parameter, rescaled by `σ`.
4. For plots, `χ²(Σm_ν) − χ²(Σm_ν = 0) = 3.84` is "a good proxy" for the Feldman–Cousins limit
   and does not depend on the parabolic fit (arXiv:2503.14744) [src: Sect. V.1]; it is "a
   reasonable proxy" unless `μ_0` is "negative and several σ away from zero" (arXiv:2507.12401)
   [src: Sect. 2.1].

The parabola separates two reasons why a limit tightens: a better `σ` or a minimum pushed
further negative. Moving from DESI DR1 to DR2 BAO with CMB, `σ` improved by 0.011 eV while the
curve moved by +0.012 eV, so the limit improved by 0.010 eV only (arXiv:2503.14744) [src: Sect.
V.1].

### Step 6. Check the asymptotic assumptions with mocks
<!-- key: step-6-check-the-asymptotic-assumptions-with -->

The three checks of Herold et al. 2024 (arXiv:2408.07700) [src: Sect. III.7], to run before
using the graphical or the Feldman–Cousins construction:

1. The maximum-likelihood estimates `μ̂` over mock data follow a Gaussian; estimate their variance.
2. Wald's relation: `t_μ^LR` against `μ̂` follows the parabola of Eq. 7, independently of the
   true nuisance values.
3. Wilks: `t_μ^LR` is χ²-distributed, or follows the boundary-modified distribution near a boundary.

How the checks are staged, with Planck-lite mocks drawn from the published covariance around the
Planck 2018 best fit (arXiv:2408.07700) [src: Sects. V.1, VI]: first all other parameters fixed
(250 mocks), then one nuisance parameter free (three sets of 100 mocks at three true `ω_cdm`
values for `h`; 200 mocks with `h` free for `M_ν`), then all ΛCDM parameters free (100 to 200
mocks). The order isolates the failure: for `M_ν` the fixed-parameter test passes because the
spread does not reach zero, and the boundary appears only once `h` is freed [src: Sect. VI.2].
For w0CDM with free ΛCDM parameters (200 mocks, `h` restricted to [0.2, 1.2], so `w0 ≳ −2`), the
`ŵ0` histogram is bimodal and the empirical 68% cut-off of `t^LR` is 0.68 instead of 1 [src:
Sect. VI.3].

A direct coverage test is cheaper when the likelihood is emulated. DESI DR1 draws 100 Gaussian
realisations around a Planck 2018 ΛCDM truth (EFT parameters at the best fit of the most
constraining combination), computes for each the 1σ profile and credible intervals of H0, and
reports coverage with the binomial error `sqrt(p(1 − p)/N)`, `N = 100` (arXiv:2508.11811) [src:
App. A].

### Step 7. Use the profile to locate projection effects and data-set conflicts
<!-- key: step-7-use-the-profile-to-locate-projection -->

- **Mean against maximum likelihood**, model by model: the DESI comparisons are in
  `results.md#projection-prior-volume-effects-documented`.
- **Per-data-set `χ²` along the profile**: Herold et al. 2025 split `χ²_tot = χ²_CMB + χ²_BAO +
  χ²_SNe` [src: arXiv:2506.12004, Eq. 3], each term evaluated at the conditional best fit of the
  combined data, not from separate fits, "so shifts are expected across rows"; in ΛCDM the terms
  prefer different Ω_m, and the disagreement disappears in w0waCDM [src: Sect. IV.1].
- **Bayesian counterpart, MAP with PJ-HPD** (KiDS-1000, arXiv:2007.01844) [src: Sect. 6.4]: sort
  the posterior samples by decreasing posterior density; step through the list, recording for
  each parameter the range spanned by all samples so far; stop when that range holds the
  fraction α of the marginal posterior mass; interpolate the boundaries linearly between the
  samples around the stopping point. The interval always contains the MAP, reduces to the
  marginal HPD in one dimension and to the marginal 1σ interval for a Gaussian posterior, and is
  usually slightly wider; it need not be connected for a multimodal posterior [src: Sect. 6.4].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

| Construction | Assumes | Buys | Costs | Used by | Same-data comparison |
|---|---|---|---|---|---|
| Marginal posterior, HPD or mean ± σ | prior is meaningful | standard, cheap from chains | projection effects; credible ≠ confidence | collaboration headlines | w0waCDM H0 credible intervals undercover "dramatically" on DESI DR1 mocks (arXiv:2508.11811) [src: App. A] |
| MAP + PJ-HPD | posterior samples dense near the MAP | contains the best fit, Bayesian | boundaries scatter (tens of samples set them); a few tens of optimisations | KiDS-1000, KiDS-Legacy, DES Y6 | KiDS-1000 synthetic runs, analytic and mock covariances: S8 1σ widths 0.054, 0.056, 0.054, 0.057 marginal against 0.072, 0.062, 0.057, 0.066 PJ-HPD (arXiv:2007.01844, Table 5, IDs 9–12; `deep/covariance-estimation.md`) |
| Profile, graphical `Δχ² = 1, 4` | Wilks and Wald hold; no boundary | no prior; reparameterisation invariant | 16+ optimisations per point, ×10–20 restarts | DESI DR1 frequentist; Herold 2025 | ΛCDM and w0waCDM H0 profile coverage consistent with 68.3% on 100 DESI mocks (arXiv:2508.11811) [src: App. A] |
| Profile + parabola + Feldman–Cousins | Gaussian in the profiled parameter, near a boundary | boundary-correct limit; separates `σ` from `μ_0` | parabolic-fit dependence | DESI DR2 neutrinos; Chebat 2025 | DESI DR2 BAO + CMB: 0.053 eV in both papers (arXiv:2503.14744, arXiv:2507.12401, where it is 53 meV with Planck PR4 and CMB lensing) [src: abstract of each] |
| Full Neyman construction with mocks | fast mocks and likelihood | exact coverage | prohibitive for Boltzmann-code likelihoods | not used for a headline | recommended for w0CDM with Planck-lite (`physics-and-methods.md#when-the-graphical-construction-can-be-trusted`) |
| Profile binned from an MCMC | dense chains | free, a quick projection test | noisy, biased by prior volume, can miss the minimum | initialisation in PROSPECT and Procoli | > 4 in `χ²` above the optimised profile for EDE (arXiv:2401.14225) [src: Sect. III.2] |

Agreement when the data are strong. With DESI DR2 BAO, Planck PR3, Planck + ACT DR6 lensing, and
Pantheon+ or DES Y5 supernovae, the w0, wa profiles agree "excellent[ly]" with the Bayesian
constraints; for Ω_m the means and maximum-likelihood values agree within 0.1σ and the error
bars within 9% (Herold et al. 2025, arXiv:2506.12004) [src: abstract, Sect. IV.1]. Settings of
that comparison: pinc with MontePython and CLASS, cross-checked with Procoli; chains converged
at `R − 1 < 0.05`; flat priors `w0 ∈ [−3, 1]`, `w0 + wa ∈ [−5, 0]`; DES Y5 before the Dovekie
recalibration [src: Sect. II]. The authors caution that the w0CDM failure of the Planck-lite
test is "not easily transferrable" to this more constraining data set [src: Sect. II]. The
disagreement documented for DESI DR1 full shape without supernovae
(`results.md#projection-prior-volume-effects-documented`) is therefore a property of weak data
and many nuisance parameters, not of the two frameworks.

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Random-start optimisations for the MAP | 50 | DESI DR1 full shape | arXiv:2508.11811 | Sect. 3.2 |
| Entries per 1D profile; optimisations per entry; 2D grid | 16; 10–20; 16 × 16 | DESI DR1 full shape | arXiv:2508.11811 | Sect. 3.3 |
| Profile range fixed in advance | ≈ Δχ² ≤ 9 | DESI DR1 full shape | arXiv:2508.11811 | Sect. 3.3 |
| Mock realisations for the coverage test | 100 | DESI DR1 full shape | arXiv:2508.11811 | App. A |
| Free parameters in the neutrino profiles | 14 (BAO + CMB) to 44 (FS + BAO + CMB) | DESI DR2 | arXiv:2503.14744 | Sect. V.1 |
| Feldman–Cousins 95% limit, DESI DR2 BAO + CMB, ΛCDM | 0.053 eV | DESI DR2 | arXiv:2503.14744 | Sect. V.1, Eq. 29 |
| Change DR1 → DR2: limit, `σ`, curve position | −0.010 eV, −0.011 eV, +0.012 eV | DESI DR2 | arXiv:2503.14744 | Sect. V.1 |
| Scale `σ` of the parabola, DESI DR2 BAO + Planck PR4 + lensing | 43 meV (ΛCDM); about 78 meV (w0waCDM) | Chebat et al. | arXiv:2507.12401 | abstract, Sect. 4.2 |
| Lower boundaries used in the Feldman–Cousins construction | 0, 59, 100 meV | Chebat et al. | arXiv:2507.12401 | Sect. 2.2 |
| PROSPECT annealing settings | `m ≈ 0.5`, `A_t ≈ 0.2`; 2–3 repeats per point; `ξ ≈ 0.1` | PROSPECT | arXiv:2312.02972 | Sects. 3.1–3.2 |
| Metropolis–Hastings jumping factor, for comparison | δ ≈ 2.4 | Procoli | arXiv:2401.14225 | Sect. II.1 |
| Mocks per Wilks check | 250 (fixed), 3 × 100 or 200 (one nuisance), 100–200 (all free) | Planck-lite | arXiv:2408.07700 | Sect. VI |
| Empirical 68% cut-off of `t^LR`, w0CDM, all free | 0.68 (Gaussian expectation 1) | Planck-lite | arXiv:2408.07700 | Sect. VI.3 |
| Bayesian against frequentist, Ω_m, CMB + DESI DR2 + SNe | means within 0.1σ, errors within 9% | Herold et al. 2025 | arXiv:2506.12004 | Sect. IV.1 |
| Frequentist Ω_m, CMB + DESI DR2, ΛCDM | 0.3011 ± 0.0038 | Herold et al. 2025 | arXiv:2506.12004 | Sect. IV.1 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Local minimum along the whole profile.** Symptom: a smooth profile that is everywhere above
  the global best fit, or a profile that follows one mode of a bimodal parameter. Example:
  Minuit tracking `log10 z_c > 3.7` for early dark energy (arXiv:2401.14225) [src: Sect. III.2].
  Test: restart from several modes; compare two optimiser families; check that the profile
  minimum equals the separately found global best fit.
- **Noisy profile points.** Boltzmann-code precision and approximation switching make gradients
  unreliable (arXiv:2408.07700) [src: Sect. IV]. Test: rerun the noisiest entries with more
  restarts, as DESI did (arXiv:2508.11811) [src: Sect. 3.3]; with CMB lensing, raise the
  precision settings as ACT recommends (arXiv:2506.12004) [src: Sect. II].
- **A binned MCMC presented as a profile.** Biased by prior volume, jagged, can miss the minimum
  (arXiv:2401.14225) [src: Sect. III.2]. Use it as a start or as a quick projection test only.
- **A parabolic profile taken as proof of coverage** (arXiv:2408.07700) [src: Sect. II.2]. Test:
  the three mock checks of Step 6, staged from fixed to free nuisance parameters.
- **Graphical `Δχ² = 3.84` at a boundary when `μ_0` is several σ negative** (arXiv:2507.12401)
  [src: Sect. 2.1]. Use the Feldman–Cousins limit from `μ_0` and `σ`, and quote both.
- **"Prior-free" claimed while nuisance penalties remain.** The DESI neutrino profiles keep the
  Gaussian penalties of the CMB and full-shape likelihoods (arXiv:2503.14744) [src: Sect. V.1];
  DESI's maximum-likelihood point removes the EFT priors but its MAP keeps them
  (arXiv:2508.11811) [src: Sects. 3.2–3.3]. State which priors remain in the profile.
- **Per-data-set `χ²` read as separate fits.** The terms are evaluated at the joint conditional
  best fit (arXiv:2506.12004) [src: Sect. IV.1].
- **Coverage tests that fix what the data fit frees.** Feldman–Cousins mock fits with fixed
  parameters give intervals that are too narrow
  (`systematics.md#parameter-boundaries-and-one-sided-limits`).
- **A PJ-HPD interval quoted to many digits.** Its boundaries are set by tens of samples and
  scatter (arXiv:2007.01844) [src: Sect. 6.4].

Pass criteria as stated: `μ̂` Gaussian, Wald's parabola independent of the nuisance values,
`t^LR` χ²-distributed or boundary-modified (arXiv:2408.07700) [src: Sect. III.7]; coverage
within the binomial error of the nominal 68.3% (arXiv:2508.11811) [src: App. A]; the MAP
recovers the input of a noiseless mock to the accuracy of the optimiser (better than 1.7% in
KiDS-1000, arXiv:2007.01844) [src: Sect. 7].

## Reading list
<!-- key: reading-list -->

- Review: Herold, Ferreira & Heinrich 2024 (arXiv:2408.07700), Sects. II, III.7, IV and VI, for
  the decision rule, the mock checks and their staging.
- Review: CosmoVerse White Paper (arXiv:2504.01669), Sect. 3.6.3, for optimisers and
  initialisation strategies side by side.
- Foundation: Feldman & Cousins 1998 (arXiv:physics/9711021), for the ordering principle the
  boundary limits use.
- Method: PROSPECT (arXiv:2312.02972), Sect. 3, and Procoli (arXiv:2401.14225), Sects. II and
  III.2, for annealing settings and the failure of binned chains and of a deterministic
  optimiser.
- Method: KiDS-1000 methodology (arXiv:2007.01844), Sect. 6.4, for the MAP with the PJ-HPD interval.
- Application: DESI DR1 frequentist full shape (arXiv:2508.11811), Sect. 3 and App. A, for a
  complete recipe and a coverage test.
- Application: DESI DR2 neutrinos (arXiv:2503.14744), Sect. V.1, and Chebat et al. 2025
  (arXiv:2507.12401), Sect. 2, for parabola plus Feldman–Cousins at a boundary.
- Application: Herold et al. 2025 (arXiv:2506.12004), Sects. II and IV.1, for agreement in
  w0waCDM with strong data and the per-data-set `χ²` breakdown.
- Critique: Barua et al. 2025 (arXiv:2508.10633), for interval constructions compared outside
  the Gaussian regime.

## Not verified
<!-- key: not-verified -->

- CAMEL and the Cobaya profile fork were named in arXiv:2408.07700 but their methods were not read.
- The Neyman construction with nuisance parameters for a cosmological likelihood (profile-based
  belt with mocks at each grid point) is described only in general terms here; no cosmology
  paper doing it in full was read.
- Gómez-Valent 2022 (arXiv:2203.16285): the binned-chain method is described only as summarised
  in arXiv:2312.02972 and arXiv:2504.01669.
- The coverage percentages of DESI App. A (arXiv:2508.11811) were read from the text, not from Fig. 6; only
  "consistent with 68.3%" and "dramatic undercoverage" are quoted.
- Chebat et al. Eq. 4 is quoted for its ordering ratio only; the integrand of their coverage
  condition was not checked against Feldman & Cousins.
