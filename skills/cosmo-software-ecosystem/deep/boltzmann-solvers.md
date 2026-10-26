# Boltzmann solvers — cosmo-software-ecosystem dossier

Scope: how an Einstein–Boltzmann run is configured for a stated purpose
(MCMC, Fisher derivatives, reference spectra): which approximation schemes
CLASS switches on and what each costs, how the massive-neutrino sector is
sampled, which precision settings published analyses used, how two solvers
are matched for a like-for-like comparison, and what differentiable solvers
change.
Snapshot: 2026-10-19.
From: cloelib software paper (arXiv:2605.23839), State of the Field (CAMB,
CLASS); Snowmass2021 CompF white paper (arXiv:2203.07347), Sect. 5.3
(verification and validation).

Already in L2, not repeated here: what the family computes and the CAMB and
CLASS conventions (`physics-and-methods.md#what-the-family-computes`,
`physics-and-methods.md#camb-against-class`); CAMB v2 tolerances, timings
and the 2011 CAMB–CLASS comparison
(`results.md#camb-v2-default-accuracy-arxiv-2607-14854`,
`results.md#timings-quoted-in-the-camb-v2-paper`,
`systematics.md#code-comparisons-read-in-paper-bodies`); default
settings, neutrino defaults and the CAMB v2 accuracy hierarchy
(`systematics.md#default-accuracy-and-non-linear-settings-of`,
`systematics.md#default-neutrino-sector`). Self-convergence, regression
and cross-code testing as practices are in `deep/maintenance-validation.md`;
modified-gravity forks in `deep/modified-gravity-solvers.md`. Which r_d or
z_* a code returns is in `cosmo-theory-foundations/deep/sound-horizon.md`.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. State what the run is for, because it sets the precision
<!-- key: step-1-state-what-the-run-is-for-because-it -->

Default precision of CAMB and CLASS was tuned between 2011 and 2013 "to
avoid biasing the results of MCMC analyses of, typically, Planck and
SDSS/BOSS data, while keeping them as fast as possible" (Euclid
Collaboration: Casas et al. 2023, arXiv:2303.09451) [src: Sect. 6]. The
same paper ranks three uses:

- MCMC: random numerical errors "tend to be averaged out each time that
  results are marginalised over unwanted parameters"; its MCMC runs use
  default CLASS precision [src: Sect. 6].
- Fisher matrices from first derivatives need more precision, because a
  derivative compares spectra at very small parameter steps whose
  difference "should be dominated by physical effects rather than
  numerical errors" [src: Sect. 6].
- Fisher matrices from second derivatives of the likelihood (their
  MontePython method) need more still [src: Sect. 6].

A reference run for a code comparison sits above all three (Step 5).

### Step 2. Know which approximation is active where (CLASS)
<!-- key: step-2-know-which-approximation-is-active-where -->

CLASS integrates exact equations only around Hubble crossing of each mode
and in the super-Hubble region with non-tightly-coupled photons; elsewhere it
uses three schemes, summarised in the (k, τ) plane for `cl_3permille.pre`
(0.3 % on C_ℓ to ℓ = 3000, P(k) to 1 h Mpc⁻¹) (Blas, Lesgourgues & Tram
2011, arXiv:1104.2933) [src: Sect. 5, Fig. 10]:

- **Tight-coupling approximation (TCA)** before recombination, which
  removes the stiffness of the photon–baryon equations. Schemes selected by
  `tight_coupling_approximation`: `first_order_MB`, `first_order_CAMB`
  (only c_s² ∝ a⁻¹ approximated, as in CAMB), `first_order_CLASS`,
  `second_order_CRS`, `second_order_CLASS`, and the default
  `compromise_CLASS` (second-order shear, leading second-order slip, no h″
  term so one Einstein equation fewer) [src: Sect. 2.5, Eq. 29]. The
  authors chose the compromise because it carries the leading
  second-order correction for high-k modes, "precisely ... the modes [for
  which] the first order approximation fails first" [src: same]. It is
  switched off per mode when τ_c/τ_H or τ_c/τ_k exceeds
  `tight_coupling_trigger_tau_c_over_tau_h` or `..._tau_c_over_tau_k`,
  where τ_c is the Thomson scattering time, τ_H the Hubble time and τ_k
  = 1/k [src: Sect. 2.7].
- **Ultra-relativistic fluid approximation (UFA)** for massless neutrinos
  inside the Hubble radius, which replaces the truncated hierarchy by
  fluid equations; triggered by `ur_fluid_trigger_tau_over_tau_k`, with hierarchy
  length `l_max_ur` before it; schemes MB, HU and CLASS, the CLASS one
  "one order of magnitude better" for P(k) [src: Sect. 3.6]. The paper
  states it had not been in public Boltzmann codes before [src: Sect. 1].
- **Radiation streaming approximation (RSA)** after photon decoupling deep
  inside the Hubble radius, for photons and massless neutrinos, including
  reionisation (`rsa_MD_with_reio`); on when both kτ ≥
  `radiation_streaming_trigger_tau_over_tau_k` and τ_c/τ ≥
  `radiation_streaming_trigger_tau_c_over_tau` [src: Sect. 4.5, Table 4].
  After decoupling the code integrates about four smooth equations, and
  thanks to the UFA about 30 equations in total before it (arXiv:1104.2933)
  [src: Sect. 5].

Integrator: CLASS's stiff `ndf15` is the default; without it "it would
have been essentially impossible to launch test runs with no approximation
schemes" [src: Sect. 1].

### Step 3. Sample the massive-neutrino sector
<!-- key: step-3-sample-the-massive-neutrino-sector -->

Massive neutrinos add (l_max_ncdm + 1) equations per momentum bin q, so
the number of momenta dominates the cost (Lesgourgues & Tram 2011,
arXiv:1104.2935) [src: Sect. 4.3; App. B, Table 1]. Two devices cut it:

- **Quadrature in momentum.** CLASS reaches 0.2–0.3 % on C_ℓ, 0.1 % on
  P(k) and Δχ² ∼ 1 with five momenta, where "traditional Boltzmann codes
  employ 14 momenta"; this halves the run time [src: Sect. 4.3]. CAMB's
  scheme uses three to five bins whose nodes and weights (three-point: q =
  0.913201, 3.37517, 7.79184; weights 0.0687359, 3.31435, 2.29911) are
  tabulated in the DISCO-EB paper from a reference it cites (Hahn, List &
  Porqueres 2023, arXiv:2311.03291) [src: Sect. 2.4, Eq. 2]. CAMB v2
  defaults to three points, more for heavier eigenstates
  (`systematics.md#default-neutrino-sector`).
- **Non-cold dark matter fluid approximation (NCDMFA)** inside the Hubble
  radius, schemes MB, Hu and CLASS (Eq. 26a–c), the CLASS one being the
  default because it is "slightly better for predicting the matter power
  spectrum on small scales" [src: arXiv:1104.2935, Sect. 3.5]. It adds a
  25 % speed-up at standard settings; with quadrature, one massive
  neutrino makes CLASS 1.5 times slower instead of 4.5 [src: Sect. 4.3].

Where the fluid approximation fails (arXiv:1104.2935): harmless on the CMB (0.02 % at
ℓ = 2750 for three 1 eV species) but P(k) "wrong by 1 to 3 % for
k ∈ [0.05; 1] h Mpc⁻¹" with three 1 eV neutrinos; the authors recommend
it "for any value of the mass when computing CMB anisotropies, and only
below a total mass of one or two eV's when computing the matter power
spectrum" [src: Sect. 3.5]; around m = 2 eV the user "should either turn
off the approximation, or increase the value of the kτ trigger" [src:
App. B].

Validation tests the authors of arXiv:1104.2935 ran, reusable for any code: CAMB against
CLASS with Ω_ν = 0.02 (m ≃ 0.923 eV) agreed to better than 0.1 % in CMB
and P(k), about six times the massless-case difference; and the massless
limit, m = 10⁻⁸ eV in CLASS, approached three massless species to 0.03 %
in C_ℓ and 0.05 % in P(k) [src: Sect. 4.1].

Mass split (arXiv:1104.2935): normal against inverted hierarchy at equal M_ν = 0.100,
0.115, 0.130 eV offsets P(k) at large k by 0.03 % to 0.22 % [src:
Sect. 4.4, Fig. 5].

### Step 4. Choose precision settings for the target
<!-- key: step-4-choose-precision-settings-for-the-target -->

**CLASS precision files** [src: arXiv:1104.2935, App. B]:

| File | Built for | ncdm settings (tol_ncdm, l_max_ncdm, q in perturbations, fluid trigger kτ) | Accuracy read |
|---|---|---|---|
| `cl_ref.pre` | reference | 10⁻¹⁰, 51, 28, no fluid approximation | reference |
| `chi2pl0.1.pre` | Δχ² ∼ 0.1 for a Planck-like CMB experiment | 10⁻⁴, 16, 8, 30 | Δχ² 0.083–0.157 for m = 10⁻³–2 eV (Table 2) |
| `chi2pl1.pre` | Δχ² ∼ 1 | 10⁻³, 12, 5, 16 | Δχ² 0.90–1.10 (Table 2) |
| `cl_permille.pre`, `cl_2permille.pre`, `cl_3permille.pre` | 0.1, 0.2, 0.3 % on C_ℓ^TT, 2 < ℓ < 3000 | fluid trigger raised for P(k) | P(k) error ≤ 0.05 % (k < 0.2 h Mpc⁻¹) and 0.12 % (0.2–1) for m ≤ 0.1 eV; 0.2 % and 1.5 % at m = 2 eV (Table 3) |

The trap: the `chi2pl` files "are optimised for fitting the CMB spectra
only" and give P(k) errors "of the order of a few per cents in the range
k ∈ [0.05; 1] h Mpc⁻¹"; the authors send P(k) users to the permille files
[src: App. B].

**Euclid settings (2023).** For CAMB, three levels P1/P2/P3: `accuracy_boost`
2/2/3, `l_accuracy_boost` 2/2/3, `halofit_tol_sigma` 10⁻³/10⁻⁶/10⁻⁶, always
with `do_late_rad_truncation = T`, `high_accuracy_default = T`,
`transfer_interp_matterpower = T`, `accurate_reionization = F`; P3 is used
throughout [src: arXiv:2303.09451, App. A.5]. `halofit_tol_sigma` is a
parameter the authors added: CAMB's halofit finds the non-linear scale by
bisection with a tolerance "hard-coded to 10⁻³" [src: Sect. 6.1]. For
CLASS, default precision (DP) for MCMC, and a high-precision (HP) list for
second-derivative Fisher matrices: `l_max_g = 20`, `l_max_pol_g = 15`,
`radiation_streaming_approximation = 2`,
`radiation_streaming_trigger_tau_over_tau_k = 240`,
`radiation_streaming_trigger_tau_c_over_tau = 100`,
`tol_ncdm_synchronous = 1e-5`, `l_max_ncdm = 22`,
`ncdm_fluid_trigger_tau_over_tau_k = 41`, `background_Nloga = 6000`,
`thermo_Nz_log = 20000`, `thermo_Nz_lin = 40000`,
`tol_perturbations_integration = 1e-6`, `halofit_tol_sigma = 1e-8`
(CLASS's halofit default is 10⁻⁶) [src: App. A.5; Sect. 6.1]. The authors
"recommend using at least the precision settings discussed in Sect. 6 in
any forecast or real data analysis, for Euclid or experiments with
comparable sensitivity" [src: Sect. 4.2.1]. These CAMB names are of the
version used then; CAMB v2's own recommendations (`AccuracyBoost` rarely
above 1, `Transfer.high_precision` for P(k)) are in
`systematics.md#default-accuracy-and-non-linear-settings-of`.

### Step 5. Match the physics before comparing two solvers
<!-- key: step-5-match-the-physics-before-comparing-two -->

The codes model the same "standard" inputs differently; a comparison of
numerics must remove that first.

- **Neutrinos.** Casas et al. made CLASS mimic CAMB's `share_delta_neff =
  T` model. CAMB inputs `num_mass_eigenstates = 1`, `massless_neutrinos =
  2.046`, one massive neutrino, `mnu = 0.06`; CAMB then uses internally
  N_ur = 2 + (2/3)(2.046 − 2) ≃ 2.030666, T_ν/T_γ = (4/11)^{1/3}
  ((1 + 2.046)/3)^{1/4} = 0.7164864 and Ω_ν h² = (0.06 eV/94.07 eV)
  ((1 + 2.046)/3)^{3/4} = 6.451439 × 10⁻⁴; the matching CLASS input is
  `N_ncdm = 1`, `N_ur = 2.030666`, `T_ncdm = 0.7164864`,
  `Omega_ncdm = 0.001437166` [src: arXiv:2303.09451, App. A.2, Eq. 40–42].
  The paper calls CLASS's default modelling "closer to reality" and the
  matching a choice for comparing pipelines, not for fitting data [src:
  same].
- **Non-linear onset.** CLASS applies halofit for k > 10⁻⁴ Mpc⁻¹ and CAMB
  for k > 3.3 × 10⁻³ Mpc⁻¹; set `halofit_min_k_nonlinear = 3.3e-3` in
  CLASS for a like-for-like plot (arXiv:2303.09451) [src: Sect. 6.1].
- **Normalisation.** Pass the same A_s, not the same σ8, when absolute
  spectra are compared, to be "insensitive to very small differences in
  the σ8-to-A_s conversion" [src: Sect. 6.1].
- **Hidden optimisations.** The DISCO-EB comparison found that CLASS
  "enables by default some optimizations which can lead to relatively
  large differences" and had to disable some for massive neutrinos and the
  dark-energy fluid; its reference runs also switched reionisation off in
  both codes [src: arXiv:2311.03291, Sect. 3.2, Tables 2–3].
- The matched set used for CAMB v2 against CLASS (recombination, helium,
  lensing cutoff, non-linear model) is in `deep/maintenance-validation.md`,
  Step 1.

### Step 6. If gradients are needed, know how a differentiable solver gets them
<!-- key: step-6-if-gradients-are-needed-know-how-a -->

- **Two ways through an ODE.** Differentiate through the solver's steps
  ("discretise-then-optimise") or solve a continuous adjoint backwards
  ("optimise-then-discretise"); the second "generally ... yields less
  accurate derivatives" because the backward discretisation is not
  synchronised with the forward one, but uses less memory. Forward mode
  suits few inputs and many outputs (P(k) against a cosmological
  parameter), reverse mode many inputs and few outputs [src:
  arXiv:2311.03291, Sect. 2.2]. DISCO-EB computes the Jacobian of log P
  with `jacfwd` [src: Sect. 3.3].
- **Solver.** DISCO-EB uses the Diffrax Kvaerno5 implicit solver (ESDIRK,
  order 5/4); the Jacobian of the system is obtained by automatic
  differentiation but stored dense, since JAX sparse support is
  experimental, which "is the current performance bottleneck"; modes are
  integrated one by one and vectorised with `vmap` [src: Sect. 2.3].
- **Number of equations.** 8 + 2ℓ_γ,max + ℓ_νUR,max + n_q ℓ_ν,max, with
  the cost of the Jacobian quadratic in it [src: Sect. 2.4, Eq. 1].
  DISCO-EB implements TCA, UFA and RSA but uses none: adaptive switching
  adds complexity on GPUs and none gave an O(1) gain; a factor 2–3 may
  remain to be gained [src: Sect. 2.4].
- **Check the gradients.** Autodiff against second-order central
  differences with relative step ε = 10⁻² agreed "to mostly better than
  one per cent"; smaller ε made finite differences "very noisy", and the
  one significant difference (the neutrino-mass derivative against CLASS)
  was attributed to CLASS run without its fluid approximation at reduced
  accuracy (arXiv:2311.03291) [src: Sect. 3.3, Eq. 5].
- **Approximation-free codes.** SymBoltz is approximation-free and uses
  Chebyshev interpolation in k and ℓ; its author argues that
  approximation-based codes "switch equations in τ, k and ℓ ... and break
  smoothness", which slows global Chebyshev convergence; around the Limber
  switch, piecewise interpolation restored it; cubic splines are "safer
  with approximations" but converge more slowly (Sletmoen 2026,
  arXiv:2608.24682) [src: Sect. 8]. Results there are for SymBoltz 1.7.0
  [src: Sect. 8, footnote 5].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### TCA order and integrator
<!-- key: tca-order-and-integrator -->

With `cl_permille.pre`, ending the TCA at the tca1–tca3 triggers costs
0.02–0.08 % against no TCA; first-order schemes are "roughly ten times
less accurate" than the compromise at the same trigger; first-order at
tca1 matches compromise at tca3 [src: arXiv:1104.2933, Sect. 2.7, Table 1,
Fig. 5]. Perturbation-module times (no-TCA / first-order tca1 / compromise
tca3): Runge–Kutta 1069 / 19.4 / 17.8 s; ndf15 16 / 14.9 / 14.6 s [src:
Table 2]. The authors conclude that CLASS "benefits much more from the
implementation of our stiff integrator than from going beyond the
first-order TCA"; the compromise matters for users who keep Runge–Kutta
[src: Sect. 2.7].

### UFA on or off
<!-- key: ufa-on-or-off -->

At `l_max_ur` = (kτ)_ufa = 18, no UFA gives "very unstable" results with
about twice the CMB error of any UFA scheme; UFA is 10 % faster and more
accurate at fixed ℓ_max (ndf15 16.7 s against 15.2 s) [src:
arXiv:1104.2933, Sect. 3.6, Table 3].

### RSA, and CAMB's late-radiation truncation
<!-- key: rsa-and-camb-s-late-radiation-truncation -->

With the RSA on (triggers 100 and 2), CMB errors stay at the no-RSA level
(0.01 %) and P(k) error grows to 0.04 %; ndf15 time falls from 84.4 to
14.5 s [src: arXiv:1104.2933, Sect. 4.5, Tables 4–5]. CAMB's RSA
(`late_rad_truncation`) "neglects reionisation" and uses a relation valid
only deep in matter domination, so accurate CAMB P(k) required switching
it off in 2011 [src: Sect. 4.5] (`systematics.md#default-accuracy-and-non-linear-settings-of`).
The Euclid 2023 CAMB settings nevertheless keep `do_late_rad_truncation =
T` and report CAMB P3 within 0.07 % of CLASS HP in linear P(k) [src:
arXiv:2303.09451, App. A.5; Sect. 6.1]; whether CAMB's truncation changed
between the two papers was not read, and the difference is left
unresolved.

### Halofit tolerance for derivatives
<!-- key: halofit-tolerance-for-derivatives -->

CAMB P1 and P2 differ only in `halofit_tol_sigma` and give identical
linear spectra, but non-linear spectra differ by 0.25 % for the fiducial
model: a 10⁻³ tolerance "leads to a poorly converged bisection in
Halofit, and thus, to a spurious step-like response of the nonlinear
spectrum to small variations in the cosmological parameters", which
compromises numerical derivatives [src: arXiv:2303.09451, Sect. 6.1]. CLASS
DP stays below 0.1 % of HP on large scales and slightly above 0.12 % on
small scales for linear P(k); HP was kept for stability of second
derivatives against step size [src: same].

### Autodiff or finite differences
<!-- key: autodiff-or-finite-differences -->

Finite differences need two solver calls per parameter and a step chosen
by bias–variance trade-off (ε ≈ 10⁻² in the DISCO-EB test); autodiff
returns all derivatives with "fewer signs of numerical artefacts" [src:
arXiv:2311.03291, Sect. 3.3]. The DISCO-EB authors declined a timing
comparison because of "the large impact of optimizations and specific
parameter choices on the performance of the EB solvers" [src: same].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| TCA trigger settings | τ_c/τ_H: 7, 8, 9 × 10⁻³; τ_c/τ_k: 3, 5, 8 × 10⁻² (tca1–3) | CLASS v1.1 | arXiv:1104.2933 | Table 1 |
| TCA error | 0.02–0.08 % vs no TCA | `cl_permille.pre` | arXiv:1104.2933 | Sect. 2.7 |
| RSA triggers (default scheme) | kτ ≥ 100, τ_c/τ ≥ 2 | CLASS v1.1 | arXiv:1104.2933 | Table 4 |
| Neutrino momenta | 5 (CLASS quadrature) vs 14 (traditional) | CLASS | arXiv:1104.2935 | Sect. 4.3 |
| Cost of one massive ν | ×1.5 (CLASS) instead of ×4.5 | CLASS | arXiv:1104.2935 | Sect. 4.3 |
| Fluid-approximation P(k) error, 3 × 1 eV | 1–3 % at 0.05–1 h Mpc⁻¹ | CLASS | arXiv:1104.2935 | Sect. 3.5 |
| NH vs IH, M_ν = 0.100–0.130 eV | 0.03–0.22 % in P(k) at large k | CLASS | arXiv:1104.2935 | Sect. 4.4 |
| CAMB P3 vs CLASS HP | < 0.07 % linear P(k); 0.2 % spike at k ≃ 3.3 × 10⁻³ Mpc⁻¹ non-linear | Euclid validation | arXiv:2303.09451 | Sect. 6.1 |
| Halofit tolerance effect | 0.25 % in non-linear P(k) (10⁻³ vs 10⁻⁶) | CAMB P1 vs P2 | arXiv:2303.09451 | Sect. 6.1 |
| Matched-neutrino CLASS input | N_ur = 2.030666, T_ncdm = 0.7164864, Ω_ncdm = 0.001437166 | for CAMB `share_delta_neff = T` | arXiv:2303.09451 | App. A.2 |
| DISCO-EB vs CAMB 1.5.0, CLASS 3.2.0 | few per mille (massive-ν spectrum > 1 % at k ≳ 1 Mpc⁻¹) | ℓ_max = 32, 5-point q | arXiv:2311.03291 | Sect. 3.2 |
| Reference CAMB run (DISCO-EB) | AccuracyBoost = lAccuracyBoost = 3, no late-radiation truncation, `Nu_int`, high-precision transfer, no reionisation | — | arXiv:2311.03291 | Table 2 |
| Reference CLASS run (DISCO-EB) | all hierarchies l_max = 64, approximations set to 3, no PPF, no reionisation | — | arXiv:2311.03291 | Table 3 |
| Autodiff vs finite differences | mostly < 1 % with ε = 10⁻² | DISCO-EB | arXiv:2311.03291 | Sect. 3.3 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **CMB-tuned precision used for P(k).** `chi2pl` files give per-cent P(k)
  errors at 0.05–1 h Mpc⁻¹ [src: arXiv:1104.2935, App. B]. Test: rerun
  with a permille file and compare P(k) at the analysis' k_max.
- **Fluid approximation above 1–2 eV.** P(k) wrong by per cents [src:
  Sect. 3.5]. Test: switch the NCDMFA off or raise its trigger for heavy
  sterile or warm species.
- **Noisy derivatives.** A Fisher forecast or a gradient sampler on
  default precision sees numerical noise; the halofit bisection tolerance
  creates steps in P(θ) [src: arXiv:2303.09451, Sect. 6, 6.1]. Test: vary
  the step size and check that the Fisher matrix is stable, as the Euclid
  paper did for second derivatives.
- **Cross-code differences that are model differences.** Neutrino
  temperature and N_ur, non-linear onset, σ8 normalisation and CLASS
  optimisations (Step 5) each move spectra on their own, whatever the
  numerical precision.
  Test: match them explicitly before attributing a difference to numerics.
- **Comparing at the edge of a free-streaming-suppressed field.** The
  massive-neutrino perturbations differ by more than 1 % at k ≳ 1 Mpc⁻¹,
  where they are 10⁻⁶ of CDM; "not significant for the matter power
  spectrum" [src: arXiv:2311.03291, Sect. 3.2]. Judge differences on the
  quantity that enters the analysis.
- **Runge–Kutta without TCA or RSA.** Without TCA the perturbation module
  took 1069 s with Runge–Kutta against 16 s with ndf15 [src:
  arXiv:1104.2933, Table 2]. Keep
  the stiff integrator for any approximation-free reference run.
- **Old settings carried to a new version.** The Euclid CAMB names
  (`accuracy_boost`, `halofit_tol_sigma`, a modified CAMB) are not CAMB v2
  defaults; re-derive settings for the version in use
  (`deep/maintenance-validation.md`, pinning).

## Reading list
<!-- key: reading-list -->

- Foundation: Blas, Lesgourgues & Tram 2011, arXiv:1104.2933 — TCA, UFA,
  RSA, with triggers, errors and timings (Tables 1–5, Fig. 10).
- Foundation: Lesgourgues & Tram 2011, arXiv:1104.2935 — neutrino
  quadrature, fluid approximation, precision files (App. B).
- Method: Lesgourgues 2011, arXiv:1104.2934 — the boosted CAMB–CLASS
  comparison (summarised in `systematics.md`).
- Application: Euclid Collaboration: Casas et al. 2023, arXiv:2303.09451 —
  Sect. 6 and App. A for Stage-IV settings and physics matching.
- Method: Lewis 2026, arXiv:2607.14854 — CAMB v2 accuracy hierarchy and
  validation (L2).
- Method: Hahn, List & Porqueres 2023, arXiv:2311.03291 — differentiable
  solver design, gradient check.
- Critique of approximation schemes: Sletmoen 2026, arXiv:2608.24682 —
  Sect. 8.

## Not verified
<!-- key: not-verified -->

- The reference that DISCO-EB cites as [42] for CAMB's 3–5 point
  neutrino quadrature was not identified; the nodes are quoted from
  DISCO-EB, not from CAMB's source.
- CLASS parameter names and defaults are those of the 2011 papers
  (v1.1) and of the 2023 Euclid paper; they were not checked against
  CLASS 3.4 (classy 3.4.1.0 on PyPI) or its `explanatory.ini`.
- Whether CAMB's `do_late_rad_truncation` changed between 2011 and the
  version used in arXiv:2303.09451 was not read.
- The CAMB version used in arXiv:2303.09451 was not read.
- The CAMB v2 neutrino quadrature (Sect. VI of arXiv:2607.14854) was not
  re-read in this pass; the L2 summary is used.
- The date-sorted search for 2025–2026 Boltzmann-solver papers was rate
  limited and not repeated;
 the newest papers used are those
  already in L2 (arXiv:2607.14854, arXiv:2608.24682).
