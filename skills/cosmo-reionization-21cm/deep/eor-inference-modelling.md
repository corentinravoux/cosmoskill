# From 21 cm limits to astrophysics — cosmo-reionization-21cm dossier

Scope: how a 21 cm power-spectrum upper limit is turned into a statement about
the IGM and early galaxies (likelihood for a limit, forward model and its
parameters, priors, emulators, samplers, joint likelihoods with other
reionisation data), and how to choose between the variants in use.
Snapshot: 2026-10-17.
From: SKA EoR/CD Science Working Group inference chapter (Acharya et al.
2026, arXiv:2606.27858); Gnedin & Madau 2022 review (arXiv:2208.02260),
Sects. 5–6.

Already in L2, not repeated here: the limits themselves and what each
collaboration says they exclude in `results.md#21-cm-power-spectrum-upper-limits-at-z-6`;
the 21 cm brightness-temperature equations in
`physics-and-methods.md#the-21-cm-signal`; the list of codes and suites in
`physics-and-methods.md#codes-and-simulations`; the joint midpoint and
duration of Sims et al. in `open-questions.md#rapid-or-extended-where-is-the-midpoint`;
signal-loss budgets in `systematics.md#21-cm-interferometry-at-z-6`.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Write the likelihood of an upper limit
<!-- key: step-1-write-the-likelihood-of-an-upper -->

Notation of the HERA theory paper (HERA Collaboration 2021b,
arXiv:2108.07282, Sect. III.2), followed here. The data vector d stacks the
measured Δ²₂₁(k_i, z_j), of length N_d = N_k × N_z; m(θ) is the model mean
for parameters θ of a model M; W is the window-function matrix (the point
spread function of the measurement in k); Γ = Σ⁻¹ is the precision matrix;
u is an unknown systematic power in each bin. The Gaussian likelihood is
L ∝ exp(−½ rᵀΓr) with r = d − u − Wm(θ) (Eq. 9). The variances come from
antenna auto-correlations, with signal–noise cross terms modelled from the
measured power; cosmic variance is not expected to matter at current depth
[src: Sect. III.2].

Marginalising u over a uniform prior, with Γ diagonal, gives a product of
one-dimensional integrals (Eqs. 11–12). The prior u ≥ 0 ("systematics can
only add power") then gives, with t_i = d_i − (Wm)_i and σ_i the standard
deviation of d_i [src: Eq. 13]:

p(θ | d, M) ∝ p(θ | M) Π_i ½ [1 + erf(t_i / (√2 σ_i))].

The authors' reasons for u ≥ 0: unbounded systematics would be fully
degenerate with the model; negative biases seen in earlier experiments
(PAPER re-analysis) have been mitigated by absolute calibration; large
negative values do not appear in null tests or validation simulations; the
most likely remaining systematic, chromaticity common to all elements,
couples positive foreground power beyond the wedge [src: Sect. III.2.1].
The same form appears in LOFAR and earlier work, as cited there [src].
Consequence stated by HERA: the likelihood is flat for Δ² well below the
limit, so "our results can therefore be heavily impacted by the prior" and
by what it considers the smallest viable power spectrum [src: HERA
Collaboration 2022, arXiv:2210.04912, Sect. VII.1].

The diagonal Γ is made true by "decimation": every second k bin is
discarded, after which the residual correlation is 1–2%; of the four
even/odd choices the one giving the strongest limits is kept [src:
arXiv:2108.07282, Sect. III.2.1]. HERA 2022 keeps the same rule and keeps
the absolute lowest limits [src: arXiv:2210.04912, Sect. VII.1].

An "inverse likelihood" L_inv = 1 − L_m/L_0, with L_0 the maximum of L_m
(usually the zero-power model), shows which parameter combinations the
limits alone exclude; models inside the projections are not necessarily
excluded, and it is for intuition only [src: arXiv:2108.07282, Eq. 14,
Sect. III.2.2]. LOFAR uses the same construction as its main tool: an
"exclusion likelihood" L_ex = 1 − Π_i ½[1 + erf((Δ²₂₁ − Δ²_m)/(√2σ))]
(Ghara et al. 2025, arXiv:2505.00373, Eq. 3), with a joint version over
the three redshifts (Eq. 4), and reports the IGM properties of the
disfavoured models [src: Sect. 2.2.5].

### Step 2. Choose the forward model
<!-- key: step-2-choose-the-forward-model -->

HERA interprets the same limits with four models [src: arXiv:2210.04912,
Sect. VII.2]: a density-driven linear-bias model; a phenomenological
"reionisation-driven" model that parametrises the bubble size distribution
and the spin temperature directly; 21cmFAST with the 21cmMC inference
engine; and a second semi-numerical model with an excess radio background.
Their reason for keeping four: the first two have no explicit source model
(lighter, but with implicit priors on IGM properties), the semi-numerical
ones tie the signal to galaxies and so can be combined with luminosity
functions, but their constraints are "only sensible if their
parameterization is flexible enough" [src].

The 21cmFAST galaxy model used by HERA has nine parameters (Park et al.
2019 parametrisation; arXiv:2108.07282, Sect. V.1) [src]:

- stellar-to-halo mass ratio M⋆/M_h = f⋆,10 (M_h/10¹⁰ M_⊙)^α⋆ (Ω_b/Ω_m),
  f⋆ restricted to [0, 1] (arXiv:2108.07282, Eq. 18): parameters f⋆,10, α⋆;
- star-formation rate Ṁ⋆ = M⋆/(t⋆ H⁻¹): parameter t⋆, in units of the
  Hubble time;
- duty cycle f_duty = exp(−M_turn/M_h): parameter M_turn;
- escape fraction f_esc = f_esc,10 (M_h/10¹⁰ M_⊙)^α_esc (arXiv:2108.07282, Eq. 19):
  f_esc,10, α_esc;
- X-ray emissivity per star formation integrated from E_0 to 2 keV,
  L_X<2keV/SFR (Eq. 20), with SED index α_X and escape threshold E_0
  (E_0 ~ 0.5 keV corresponds to an H I column of ~10^21.4 cm⁻²) [src: arXiv:2108.07282,
  Sect. V.1, Eq. 20].

Ionising and soft-UV emission assume Pop II SEDs, ~5000 ionising photons
per stellar baryon (Starburst99, Scalo IMF, 0.05 solar metallicity) [src:
arXiv:2108.07282, Sect. V.1]. Simulation settings: 250 cMpc box, initial conditions on 512³,
radiation fields on 128³, 2LPT, sub-grid RSD; the model power spectra are
spherically averaged, which does not match HERA's line-of-sight mode
selection, accepted because the density-dominated regime where it matters
is already excluded [src: Sect. V.2].

Other model families in use:

| Analysis | Simulator | Free parameters (prior) | Fixed assumptions | Place read |
|---|---|---|---|---|
| LOFAR 2025 | GRIZZLY on N-body haloes | ζ ∈ [10⁻³, 10³], f_X ∈ [10⁻³, 10³], M_min and M_min,X ∈ [10⁹, 10¹²] M_⊙, A_r ∈ [0, 416]; log-uniform | f⋆ = 0.02; T_S = T_K (strong Lyα coupling); X-ray SED index 1.2 over 0.1–10 keV; parameters independent of z | arXiv:2505.00373, Sects. 2.2.2–2.2.3, Table 2 |
| Joint 21 cm + Lyman lines + CMB | 21cmSPACE, 384 Mpc boxes, linear density and velocity, modified Press–Schechter | f⋆ logU(0.001, 0.5); V_c logU(4.2, 100) km/s; f_X logU(10⁻⁴, 10³); τ U(0.04, 0.1); f_radio logU(1, 99500) | R_MFP = 40 Mpc, "a parameter to which the data is relatively insensitive" | arXiv:2504.09725, Sect. 3.2, Table 2 |
| 21cmEMUv3 (HERA reanalysis) | 21cmFASTv3.0.4, atomic- and molecular-cooling galaxies | ten astrophysical parameters plus σ₈, truncated Gaussian priors (e.g. log₁₀ f⋆,10 ~ N(−1.2, 0.2) in [−2, −0.5]; σ₈ ~ N(0.8118, 0.01)) | α⋆ shared by both populations | arXiv:2606.00219, Sect. 2.1, Table 1 |

In GRIZZLY, ζ multiplies 2.85 × 10⁴⁵ s⁻¹ M_⊙⁻¹ and f_X multiplies 10⁴²
s⁻¹ M_⊙⁻¹, both per unit halo mass; f_X = 1 matches local high-mass X-ray
binaries over 0.5–8 keV; the radio background is T_γ,eff = T_γ[1 +
A_r(ν_obs/78 MHz)^−2.6] (Eq. 1), the upper bound of A_r being the LWA1
603 mK at 1.42 GHz [src: arXiv:2505.00373, Sect. 2.2.2]. In 21cmSPACE the
minimum halo mass scales as M_min ∝ V_c³/(1 + z)^{3/2} (Eq. 11); V_c = 4.2
km/s is the molecular-cooling threshold (≈ 10⁶ M_⊙ at z = 10), 16.5 km/s
the atomic one (≈ 8 × 10⁷ M_⊙), 100 km/s ≈ 2 × 10¹⁰ M_⊙ [src:
arXiv:2504.09725, Sect. 3.2].

### Step 3. Add the theory error
<!-- key: step-3-add-the-theory-error -->

| Analysis | Theory term added to σ | Reason given | Place read |
|---|---|---|---|
| HERA (21cmFAST on the fly) | 20% modelling error and simulation sample variance, in quadrature; no emulator error | "conservative" modelling error; power spectra computed from 4D realisations | arXiv:2108.07282, Sect. V.2 |
| LOFAR (GRIZZLY, interpolated grid) | 30% of the model power, σ = √(Δ⁴_err + Δ⁴_m,err) | GRIZZLY matches C2-Ray to < 10% for T_S ≫ T_γ, but accuracy over the whole space and with T_S fluctuations is unknown; also covers interpolation error | arXiv:2505.00373, Sect. 2.2.5 |
| 21cmEMU inference | median emulator error in quadrature with each likelihood term | — | arXiv:2309.05697, Sect. 4.1 |

The SKA chapter states the standard: emulator error well below the
observational error (~10% of it), and, if not negligible, its covariance in
the likelihood [src: arXiv:2606.27858, Sect. 2.4].

### Step 4. Combine with the other reionisation data
<!-- key: step-4-combine-with-the-other-reionisation -->

HERA multiplies L_total = L_m × L_LFs × L_DF × L_τ [src: arXiv:2108.07282,
Sect. V.2]:

- UV luminosity functions at z = 6–10, faint end M_UV > −20 (HST) (arXiv:2108.07282, Sect. V.2);
- dark-pixel limit x_HI < 0.06 + 0.05 (1σ) at z ~ 5.9 as a one-sided
  Gaussian (arXiv:2108.07282, Sect. V.2);
- τ_e = 0.0569 (+0.0081/−0.0066) (Planck 2018 as re-analysed by Qin et al.) [sec: arXiv:2108.07282, Sect. V.2].

The 21cmEMUv3 paper quotes the HERA prior on τ as 0.0569 (+0.0081/−0.0086)
[src: arXiv:2606.00219, Sect. 5.1]; the two readings disagree on the lower
error. The HERA theory paper footnotes that later Lyα-forest work favours an
end about Δz ~ 0.5 later, which could slightly weaken its constraints
because the power peaks near the midpoint [src: arXiv:2108.07282, Sect.
V.2]. The 21cmEMU paper then replaced the dark fraction and τ by a "late
EoR" Gaussian likelihood x_HI(6) = 0.25 ± 0.07, x_HI(7) = 0.58 ± 0.1,
x_HI(8) = 0.79 ± 0.09 (Qin et al. 2021a), ignoring covariance between
redshifts; this narrows f_esc,10 and constrains α_esc to ± 0.3, and τ moves
lower [src: Breitman et al. 2024, arXiv:2309.05697, Sect. 4.3]. MWA uses
the same three points [src: Nunhokee et al. 2025, arXiv:2505.09097, Sect.
VI].

LOFAR uses τ differently: a stepwise history, neutral until z_i, ionised
at x_HII,max until z = 6, with τ = 0.061 (the 1σ upper end of 0.054 ±
0.007), giving x_HII,max = 1, 0.79 and 0.57 at z = 8.3, 9.1 and 10.1 [src:
arXiv:2505.00373, Sect. 2.2.5].

The joint analysis of Sims et al. replaces the 21 cm likelihoods by a
neural density estimator (margarine) trained on the posterior of an earlier
fit to HERA, LOFAR and MWA, log L_NDE = log L_HERA + log L_LOFAR + log
L_MWA (Eq. 19), and does the same for the Planck posterior; Lyα-emitter
x_HI PDFs enter as spline priors on x_HI(z_i) (Eq. 22) [src:
arXiv:2504.09725, Sects. 3.4.2 and 3.4.4]. Dark-pixel limits and emitter
clustering use a "contaminated upper limit" likelihood that marginalises a
positive nuisance ε ∈ [ε_min, ε_max] (Eq. 31); with ε ∈ [0, 1],
L_CUL = ½[erf((1 + m − d)/(√2σ)) − erf((m − d)/(√2σ))] (Eq. 32) [src: App.
A]. Here ε is the dark fraction not due to neutral IGM (damped absorbers,
dense ionised gas), or the host-mass part of the emitter clustering.

### Step 5. Sample and report
<!-- key: step-5-sample-and-report -->

HERA: 21cmMC with MultiNest [src: arXiv:2210.04912, Sect. VII.4]. LOFAR:
10⁵ precomputed spectra per redshift, linear interpolation in 5D, cobaya
MCMC with 10 walkers and 10⁶ steps; only the three smallest k bins are used
because larger-k limits exceed every simulated spectrum [src:
arXiv:2505.00373, Sect. 2.2.5]. MWA: 21cmEMU with dynesty, East–West and
North–South polarisations as independent constraints [src:
arXiv:2505.09097, Sect. VI]. 21cmEMUv3: nautilus, ~100k likelihood calls,
~20 GPU-minutes [src: arXiv:2606.00219, Sect. 5.1].

Credible intervals: HERA reports highest-posterior-density intervals in the
sampled (log or linear) space, and equal-tailed intervals for derived Δ²,
whose posterior can be multimodal and include zeros for ionised models
[src: arXiv:2210.04912, Sect. VII.2, footnote 23]. It stresses that a 95%
credible limit depends on the model, its parametrisation and its priors;
excluding one model at 95% confidence needs a direct comparison with the
tabulated Δ² and errors [src: footnote 22]. Sims et al. quote a parameter
only when its prior-to-posterior KL divergence exceeds 3 × 0.0033 nats (the
sampling-noise level), and quote one-sided limits when the HPD interval
touches a prior edge [src: arXiv:2504.09725, Sect. 3.1.3].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### erf likelihood or Gaussian likelihood
<!-- key: erf-likelihood-or-gaussian-likelihood -->

The erf form treats every bin as an upper limit and is only appropriate
when claiming limits; claiming a detection needs constraints on the
systematic contribution, probably high-S/N detections at several k,
redshifts and fields with jackknives [src: arXiv:2210.04912, Sect. VII.1].
Because it is not Gaussian, constraints do not scale as 1/√N: a limit with a
larger measured Δ² and a smaller error is not equivalent to one with the
same 2σ value but smaller Δ² and larger error [src]. Forecasts use a
Gaussian with fixed variance at a fiducial point; Prelogović & Mesinger
find this "overconfident and biased", with true values outside the 95%
interval when they should be inside the 68% one; including the covariance
between k and z bins "dramatically improves" inference, even if computed
only at the fiducial point; a single realisation may replace the mean if
pre-selected to lie near the mean; a Gaussian-mixture neural likelihood is
most accurate, trained on 20–30k simulations [src: arXiv:2305.03074, Sect.
5]. They add that the choice is "unlikely to be important for current noisy
21-cm observations" [src].

### Several k bins or the single deepest one
<!-- key: several-k-bins-or-the-single-deepest-one -->

Combining k modes tightens the constraints, more so at z = 10.4 where the
spectrum is steeper; using only the best single limit is "somewhat worse";
almost all the information comes from k < 1 h Mpc⁻¹ [src: arXiv:2210.04912,
Sect. VII.1]. To visualise the combined likelihood, HERA assumes Δ² ∝ k^α
with α = 1.3 (z = 10.4) and 0.0 (z = 7.9), the median slope of 21cmMC
models not yet reionised; the flattening with time is "a generic
consequence of inside-out reionization" [src]. The posteriors themselves
compare models at the measured k, not through the power law [src]. In the
first HERA theory paper the constraints were driven by the two lowest-k
limits, the model spectra being much flatter than the limits [src:
arXiv:2108.07282, Sect. V.2, Fig. 3 caption].

### Direct simulation, interpolation, emulator or neural likelihood
<!-- key: direct-simulation-interpolation-emulator -->

- Direct simulation (HERA 2021): ~10⁵ likelihood calls at ~1 core-hour each,
  ~10⁵ core-hours [src: arXiv:2309.05697, Sect. 1]; no emulator error, but
  sample variance of one seed.
- Grid plus interpolation (LOFAR): cheap, but interpolation error is folded
  into a flat 30% term [src: arXiv:2505.00373, Sect. 2.2.5].
- Emulator (21cmEMU): median (68%) fractional error ≲ 0.5% (1%) over
  summaries, trained on 1.3M samples taken from the HERA posterior; the
  posteriors from 21cmFAST and 21cmEMU are nearly identical, t⋆ slightly
  broader [src: arXiv:2309.05697, Sects. 3.7, 4.1]. The training set is the
  HERA "with-HERA" sample, so the emulator is accurate where that
  posterior was; performance falls sharply below ~100k training samples
  [src: Sects. 1, 5]. 21cmEMUv3 learns the seed-averaged mean, its error
  being smaller than the sample variance of one realisation, with ≲ 1%
  accuracy that does not degrade at prior edges [src: arXiv:2606.00219,
  Sect. 4.1].
- Neural likelihood of a previous posterior (Sims et al.): a factor of
  several faster and one joint term instead of three, but it fixes the
  parameter set of the earlier fit, which is why R_MFP is frozen at 40 Mpc
  [src: arXiv:2504.09725, Sects. 3.2, 3.4.2].

### Sampler
<!-- key: sampler -->

With the same emulator and likelihood, the sampler changes some marginals
more than the simulator does: UltraNest is more accurate towards prior
edges than MultiNest, and about 10 times faster when vectorised [src:
arXiv:2309.05697, Sect. 4.1]. On one 21cmEMUv1 inference with 2k live
points: UltraNest 2.3M likelihood calls (efficiency 0.004), MultiNest 52k
(0.15), nautilus 113k (0.09); nautilus reproduces UltraNest and MultiNest
under-samples prior edges [src: arXiv:2606.00219, App. B, Table 5]. For
HERA-type results, which are lower limits on L_X/SFR against a prior edge,
this matters directly.

### Galaxy model and priors
<!-- key: galaxy-model-and-priors -->

- **Single or two source populations.** HERA's L_X/SFR bound assumed atomic-
  cooling galaxies only; adding molecular-cooling (Pop III) galaxies makes
  values below ≈ 10^39.5 erg s⁻¹ M_⊙⁻¹ yr "no longer strongly disfavored"
  (Lazare et al. 2023, arXiv:2307.15577) [src]. 21cmEMUv3 reproduces this
  and shows it depends on the prior on molecular-cooling star formation;
  with a prior informed by the Renaissance simulations the posterior lies
  between the two earlier ones and disfavours the local HMXB relation at
  ~93% [src: arXiv:2606.00219, Sect. 5.1]. Reason: a higher prior on
  molecular-cooling star formation lets HERA's heating be reached with less
  X-ray output per unit SFR [src].
- **Extrapolated luminosity functions.** 21cmMC models fitted to the z ~ 6–8
  luminosity functions all show a rapid rise in stellar mass density
  between z = 10.4 and 7.9, by a factor ~3, so modest heating demanded at
  z = 10.4 becomes strong heating at z = 7.9; the strong spin-temperature
  limit at z = 7.9 is "informed in large part" by the weaker z = 10.4 limit
  [src: arXiv:2210.04912, Sects. VII.4, VII.6]. A new source population
  would break this and is "not included in the prior" [src: Sect. VII.4].
- **Redshift-independent parameters.** LOFAR combines redshifts only with
  caution because its source parameters do not evolve [src:
  arXiv:2505.00373, Sect. 2.2.5].
- **What the four HERA models agree on.** All require heating above the
  adiabatic limit at both z = 10.4 and 7.9 at > 95% credibility; the lower
  limits differ by model [src: arXiv:2210.04912, Sect. VII.2].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Residual k-bin correlation after decimation | 1–2% | HERA | arXiv:2108.07282 | Sect. III.2.1 |
| k range used (first HERA theory paper) | 0.13–0.64 cMpc⁻¹, Field 1, z = 10.4, 7.9 | HERA | arXiv:2108.07282 | Sect. III.2 |
| Power-law slope for combining k | α = 1.3 (z = 10.4), 0.0 (z = 7.9) | HERA | arXiv:2210.04912 | Sect. VII.1 |
| Modelling error | 20% (21cmFAST); 30% (GRIZZLY) | HERA; LOFAR | arXiv:2108.07282; arXiv:2505.00373 | Sect. V.2; Sect. 2.2.5 |
| L_X<2keV/SFR, 95% | 10^40.4–10^41.8 erg s⁻¹ M_⊙⁻¹ yr, prior < 10^42 | HERA 2022 | arXiv:2210.04912 | Sect. VII.4.1 |
| T̄_S, 95% HPD | 4.7–171.2 K (z = 10.4); 15.6–656.7 K (z = 7.9); averaged over cells with x_HI > 0.95 | HERA 2022 | arXiv:2210.04912 | Sect. VII.4.2 |
| T̄_S, 95% HPD | 2.5–797.8 K (z = 6.5), 2.3–758.6 K (6.8), 2.2–727.3 K (7.0) | MWA 2025 | arXiv:2505.09097 | Sect. VI |
| L_X<2keV/SFR | > 10³⁹ erg s⁻¹ M_⊙⁻¹ yr; local values still allowed | MWA 2025 | arXiv:2505.09097 | Sect. VI |
| x_HII,max prior from τ | 1, 0.79, 0.57 at z = 8.3, 9.1, 10.1 | LOFAR 2025 | arXiv:2505.00373 | Sect. 2.2.5 |
| Precomputed grid | 10⁵ spectra per z, 5D linear interpolation | LOFAR 2025 | arXiv:2505.00373 | Sect. 2.2.5 |
| KL threshold for "constrained" | 3 × 0.0033 nats | Joint analysis | arXiv:2504.09725 | Sect. 3.1.3 |
| x_HI emulator RMSE | ~1% (globalemu) | Joint analysis | arXiv:2504.09725 | Sect. 3.3 |
| Emulator error | median ≲ 0.5%, 68% ≲ 1%; 1.3M training samples | 21cmEMU | arXiv:2309.05697 | Sect. 3.7 |
| Training set for neural likelihood | 57k train, 14k validation, 7k test; 20–30k sufficient, 6k good | SKA1-Low mock, 1000 h | arXiv:2305.03074 | Sect. 5 |
| Sampler cost (2k live points) | UltraNest 2.3M, MultiNest 52k, nautilus 113k calls | 21cmEMUv1 | arXiv:2606.00219 | App. B, Table 5 |
| Model evaluations for a 21 cm inference | ~10⁶ | review | arXiv:2606.27858 | Sects. 2.4, 6.1 |
| Semi-numerical against radiative transfer | ~10% on large-scale statistics | review | arXiv:2606.27858 | Sect. 6.1 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Prior-driven "constraint".** The erf likelihood is flat below the limit,
  so the posterior below it is the prior [src: arXiv:2210.04912, Sect.
  VII.1]. Test: compare with the posterior without 21 cm data (HERA shows
  both; arXiv:2210.04912, Fig. 29 description), or, as LOFAR does, set the
  likelihood to a constant (0.5) and read the IGM posterior the source
  priors alone induce [src: arXiv:2505.00373, App. A]; for LOFAR this shows
  that the limits barely constrain x_HII, f_heat and T̄_K [src].
- **Credible read as confidence.** A 95% credible bound is not a 95%
  exclusion of a model [src: arXiv:2210.04912, footnote 22]. Check which
  is meant.
- **Model misspecification.** In SKA mocks built with Pop III stars (EOS21),
  an emulator trained on Pop II only (21cmEMUv1) fits the power spectrum
  well while the true T_b and x_HI histories fall outside its posterior; an
  SBI emulator on a different simulator (Loreli II) diverges more [src:
  arXiv:2606.27858, Sect. 6.1]. Test: infer on mocks from a different
  simulator or physics (**forecast** setting).
- **Two-population physics.** Values of L_X/SFR below ≈ 10^39.5 that the
  single-population fit disfavours become allowed when molecular-cooling
  galaxies are added (arXiv:2307.15577, abstract) [src]. Test: rerun with a
  second population and a stated prior on its star formation.
- **Sampler at prior edges.** MultiNest under-samples edges [src:
  arXiv:2606.00219, App. B]. Test: repeat with UltraNest or nautilus.
- **Emulator outside its training region.** 21cmEMU is trained on the HERA
  posterior [src: arXiv:2309.05697, Sect. 1]; 21cmEMUv3 truncates its
  priors "to avoid samples too far outside the training range" [src:
  arXiv:2606.00219, Sect. 5.1]. Test: check that the new posterior lies in
  the training prior; add the emulator covariance if its error is not
  ≲ 10% of the data error [src: arXiv:2606.27858, Sect. 2.4].
- **Mode selection.** Spherically averaged model spectra against
  wedge-excluded data overstate or understate density-dominated power
  [src: arXiv:2108.07282, Sect. V.2]. Test: apply the data's k selection
  and window to the model.
- **Inconsistent history inputs.** A late end of reionisation can weaken the
  limits' constraints [src: arXiv:2108.07282, Sect. V.2]; HERA, LOFAR and
  MWA each encode τ and the forest differently (Step 4). Report which.
- **Assumed T_S = T_K.** LOFAR's assumption removes Lyα-coupling
  fluctuations; it is justified by a strong Lyα background at z ≈ 8–10
  [src: arXiv:2505.00373, Sect. 2.2.3]. A reader should not compare its
  T_K with HERA's T_S directly.

## Reading list
<!-- key: reading-list -->

- Foundation: Greig & Mesinger 2015, arXiv:1501.06576 — 21CMMC, Bayesian
  inference with on-the-fly semi-numerical simulations.
- Foundation: Park et al. 2019, arXiv:1809.08995 — the mass-dependent
  galaxy parametrisation of 21cmFAST, combined with UV luminosity functions.
- Method: HERA Collaboration 2021b, arXiv:2108.07282 — the systematics-
  marginalised erf likelihood, inverse likelihood, 21cmFAST settings.
- Application: HERA Collaboration 2022, arXiv:2210.04912 — four models, how
  the two bands interact, credible-interval conventions.
- Application: Ghara et al. 2025, arXiv:2505.00373 — exclusion likelihood,
  grid interpolation, prior-only test.
- Application: Sims et al. 2025, arXiv:2504.09725 — joint 21 cm, Lyman-line
  and CMB likelihood with neural density estimators; CUL likelihood.
- Application: Nunhokee et al. 2025, arXiv:2505.09097 — MWA limits through
  21cmEMU.
- Method: Breitman et al. 2024, arXiv:2309.05697 — 21cmEMU, emulator error,
  sampler dependence, late-EoR likelihood.
- Method: Breitman et al. 2026, arXiv:2606.00219 — 21cmEMUv3, two source
  populations, sampler comparison.
- Critique: Prelogović & Mesinger 2023, arXiv:2305.03074 — tests of the
  Gaussian likelihood with simulation-based inference.
- Critique: Lazare et al. 2023, arXiv:2307.15577 — Pop III sources weaken
  the HERA X-ray bound.
- Review: Acharya et al. 2026, arXiv:2606.27858 — simulators, emulators,
  SBI and misspecification for SKA-Low.

## Not verified
<!-- key: not-verified -->

- The prior table of the nine HERA 21cmFAST parameters (Sect. 5.1 of
  arXiv:2108.07282 refers to it; the ranges were not read).
- The reionisation-driven phenomenological model and the radio-background
  model of HERA (Sects. VI and VIII of arXiv:2108.07282) were not read.
- The earlier interferometric fit used to train the NDE of Sims et al.
  ("B24" there) was not identified or read.
- The LOFAR variational-autoencoder reprocessing mentioned by the MWA paper
  was not read; no identifier is recorded.
- Abstract-level only: arXiv:1501.06576, arXiv:1809.08995, arXiv:2307.15577.
