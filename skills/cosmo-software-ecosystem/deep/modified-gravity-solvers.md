# Modified-gravity solvers — cosmo-software-ecosystem dossier

Scope: how a linear modified-gravity or dark-energy Boltzmann code is set
up (choice of basis, background, stability tests, initial conditions,
quasi-static switching, precision) and how to choose between EFTCAMB,
H-EFTCAMB, hi_class, mochi_class, EoS_class, MGCAMB and ISiTGR for a given
model; how the non-linear scales are reached with modified-gravity N-body
codes (ECOSMOG, ISIS, MG-Gadget, MG-Arepo, MG-GLAM, PySCo); and the
code-comparison results read in the papers.
Snapshot: 2026-10-22.
From: cloelib software paper (arXiv:2605.23839), State of the Field
(hi_class, mgclass II, mochi_class); the linear comparison of Bellini et
al. 2017 (arXiv:1709.09135); the N-body comparisons of Winther et al. 2015
(arXiv:1506.06384) and Euclid Collaboration: Adamek et al. 2024
(arXiv:2409.03522).

Already in L2, not repeated here: the list of forks, their bases and
references in `physics-and-methods.md#modified-gravity-forks`; the
sub-per-cent agreement headline and the 2017 precision settings in
`results.md#modified-gravity-and-differentiable-solvers` and
`systematics.md#code-comparisons-read-in-paper-bodies`; the EFTCAMB
`import camb` shadowing in `systematics.md#documented-cases-where-a-default-changed-a`;
succession EFTCAMB → H-EFTCAMB in `open-questions.md#deprecated-or-superseded-codes`.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Choose what the code is told: a theory, a basis, or phenomenology
<!-- key: step-1-choose-what-the-code-is-told-a-theory-a -->

Three ways of specifying a model exist, and each code takes a different
subset.

| Route | What the user supplies | Codes | Place read |
|---|---|---|---|
| Covariant Lagrangian | the Horndeski functions G_2…G_5 of the scalar φ and X = −½ g^{μν}∂_μφ∂_νφ (arXiv:2603.01662, Eqs. 4–5) and initial field values; background and perturbations follow | hi_class (Galileon, nKGB, quintessence, Brans–Dicke since 2019), H-EFTCAMB Horndeski module (`EFTflag = 5`) | arXiv:1909.01828, Sect. 3.3; arXiv:2603.01662, Sect. 2.2.1 |
| Effective basis of time functions | a background (w_DE(a) or ρ_DE) plus four functions of time | hi_class (α basis), EFTCAMB pure EFT (`EFTflag = 1`, Ω and γ_i basis), EFTCAMB alternative parametrisations (`EFTflag = 2`), mochi_class (stable basis), EoS_class (α_x, solved in the equation-of-state formalism) | arXiv:1605.06102, Sects. 2.2, 3.2; arXiv:1405.3590, Sect. II; arXiv:2407.11968, Sect. 2.1; arXiv:1905.06795, Sects. 1, 3 |
| Phenomenological growth functions | μ(a, k) and γ(a, k) or Σ(a, k) in the Poisson and slip equations, on a w or Ω_X background | MGCAMB, MGCLASS II, ISiTGR (also Q, R, D; functional, binned or hybrid in a and k; curved backgrounds) | arXiv:2305.05667, Sect. II.1; arXiv:1908.00290, Sects. IV.1–IV.5 |

Definitions used below.

- **α basis** (hi_class; arXiv:1605.06102, Sect. 2.2): M_*²(τ), the
  dimensionless cosmological strength of gravity; α_M = d ln M_*²/d ln a
  (Eq. 2.11), the Planck-mass run rate; α_T = c_T² − 1, the tensor speed
  excess; α_B, the braiding (kinetic mixing of scalar and metric; a pure
  conformal coupling gives α_M + α_B = 0); α_K, the kineticity (raising it
  lowers the scalar sound speed). α_K cannot be constrained from
  quasi-static scales [src: Sect. 2.2].
- **EFT basis** (EFTCAMB; arXiv:1405.3590): the background functions c, Λ
  and the time functions Ω(a) and γ_1…γ_6(a); with `PureEFTHorndeski` the
  code sets γ_4, γ_5, γ_6 to cancel higher derivatives and ignores user
  values for them [src: Sect. II].
- **μ, γ, Σ** (MGCAMB; arXiv:2305.05667, Eqs. 1–7): k²Ψ =
  −4πG μ a²[ρΔ + 3(ρ+P)σ] and k²[Φ − γΨ] = 12πG μ a²(ρ+P)σ, with Ψ, Φ the
  Newtonian-gauge potentials of Eq. 3, Δ the comoving density contrast and
  σ the anisotropic stress; Σ is defined by k²(Φ+Ψ) =
  −4πG Σ a²[2ρΔ + 3(ρ+P)σ] (Eq. 6), and Σ = μ(1+γ)/2 only once relativistic
  anisotropic stress is negligible (Eq. 7) [src: Sect. II.1].
- **Q, R, D** (ISiTGR; arXiv:1908.00290, Eqs. 18–20): (k² − 3K)Φ =
  −4πG a² Q Σ_i ρ_iΔ_i and k²(Ψ − RΦ) = −12πG a² Q Σ_i ρ_i(1+w_i)σ_i, with
  D ≡ Q(1+R)/2, which avoids the Q–R degeneracy and is what lensing and ISW
  probe; ISiTGR implements both pairs. Σ = D, like Σ = μ(1+γ)/2, holds only
  for zero anisotropic shear [src: Sect. IV.3].
- **Potentials swap names between codes.** ISiTGR's Φ is
  MGCAMB's Ψ in the Poisson equation: check each paper's equations before
  mapping parameters [der from the two equations as written].
- **Hybrid binning** (ISiTGR): bins in redshift, and inside each bin a
  function of scale X_1 e^(−k/k_c) + X_2 (1 − e^(−k/k_c)) (Eqs. 32–33),
  which gives a smoother P(k) than binning in k too [src: Sect. IV.5.2].
- **EoS approach** (EoS_class; arXiv:1905.06795): the dark sector is
  described by its equation of state for perturbations, entropy
  perturbation w_dsΓ_ds and anisotropic stress w_dsΠ_ds, written in terms
  of the α_x; implemented in CLASS, first for f(R) as CLASS_EOS_FR, then
  for full Horndeski [src: Sects. 1, 3].
- **Stable basis** (mochi_class; arXiv:2407.11968, Eq. 26): D_kin, M_*²,
  c_s² and α_B0 = α_B(z = 0), plus a background function; α_B is obtained
  by integrating the non-linear equation Eq. 27 with source Eq. 28, then
  α_K from D_kin [src: Sect. 2.1].

The bases are not interchangeable in practice. A simple form in one basis
explores a different region than the same form in another: α_B ∝ a with
Ω = 0 maps to γ_2 ∝ ℋ, which scales as a, a^{−1/2} and a^{−1} in the dark
energy, matter and radiation eras (arXiv:1709.09135, Sect. IV.7) [src].
EFTCAMB translates α's to its own basis with a built-in module, and hi_class
translates (Ω, γ_i) to α's [src: same].

### Step 2. Fix the background
<!-- key: step-2-fix-the-background -->

- hi_class 2016: `expansion_model_smg` = `lcdm` or `w0wa`; the α's then
  set the perturbations (arXiv:1605.06102, Table 1a) [src].
- hi_class covariant models: the background is integrated with
  constraint-violation damping, and a root finder sets a user-chosen
  quantity (φ(τ_ini), φ′(τ_ini) or another parameter) so that today's
  Ω_φ H_0² is reached (arXiv:1909.01828, Sects. 3.2–3.3; summarised in
  arXiv:2407.11968, Sect. 3.1) [src].
- EFTCAMB designer route (`EFTflag = 3`, and pure EFT with `PureEFTmodel = 1`):
  the expansion is fixed by w_DE through `EFTwDE`, and c and Λ follow from
  ℋ and Ω(a) (arXiv:1405.3590, Sect. IV.2, Eqs. 5–7); the authors call this
  designer approach "common" because the background alone already has many
  degrees of freedom and the focus is on linear perturbations [src].
- EFTCAMB full mapping (`EFTflag = 4`): the model is fully specified and
  the code solves its background (first example: low-energy Hořava
  gravity) [src: Sect. II].
- H-EFTCAMB: for Jordan–Brans–Dicke, Λ is found by shooting on H_0; the
  authors run the shooting as an external Python script around the
  wrapper and recommend that route generally (arXiv:2603.01662, Sect. 3.2)
  [src].
- mochi_class adds non-parametric `wext` (w_φ table) and `rho_de` (ρ_φ
  table, p_φ from Eq. 32) and skips the root finder when ρ_φ is given,
  using closure instead (arXiv:2407.11968, Sect. 3.1) [src].
- MGCAMB: w constant or (w_0, w_a), and since 2023 an Ω_X(a)
  parametrisation (arXiv:2305.05667, Sect. II.1) [src].

### Step 3. Let the code test viability
<!-- key: step-3-let-the-code-test-viability -->

hi_class tests each background before solving perturbations
(arXiv:1605.06102, Sect. 2.3, Eqs. 2.12–2.15) [src]:

- no scalar ghost: Q_S = 2M_*²D/(2 − α_B)² > 0 with D ≡ α_K + (3/2)α_B² > 0;
- no scalar gradient instability: c_s² > 0 (Eq. 2.13);
- no tensor ghost: Q_T = M_*²/8 > 0; no tensor gradient instability:
  c_T² = 1 + α_T > 0.

Tachyonic (negative mass squared) instabilities are not tested: the authors
let the data exclude them, because they grow only as a power law on large
scales and come under control inside the sound horizon [src]. The checks
can be relaxed or disabled by the user [src].

EFTCAMB enforces physical conditions (ghost and gradient, Eqs. 42–43 in
the W̃ notation of Eqs. 44–51) only for the GLPV subset, γ_3 = −γ_4 and
γ_6 = 0, which contains all Horndeski models; outside it the user must set
stability conditions by hand (arXiv:1405.3590, Sect. IV.6) [src].
Its "mathematical" conditions on the π-field equation (Eq. 52: a well-
defined leading coefficient, no growth rate above H_0, well-defined tensor
equation) are off by default and enforced from k = 0 to CAMB's k_max; the
flags are `EFT_mathematical_stability`, `EFT_physical_stability` and
`EFT_additional_priors` in `params_EFT.ini` [src: Sect. IV.6].
H-EFTCAMB adds a cosmological positivity bound and early-time initial
conditions behind `EFT_positivity_bounds` and `EFT_IC_type`
(arXiv:2603.01662, Sect. 2.2.4) [src].

mochi_class imposes only no-ghost and no-gradient conditions, D_kin > 0,
M_*² > 0, c_s² > 0 (arXiv:2407.11968, Eq. 22), treats tachyonic modes as
not necessarily harmful, and writes the mathematical condition with a
tunable growth-rate ceiling ξH_0 (Eqs. 24–25) [src: Sect. 2.1]. In the
stable basis these conditions hold by construction; the code still checks
that α_B never crosses 2, a test hi_class did not have, so
`skip_stability_tests_smg = yes` is safe there [src: Sect. 3.1].

### Step 4. Set initial conditions for the scalar perturbation
<!-- key: step-4-set-initial-conditions-for-the-scalar -->

- EFTCAMB starts the dark-energy perturbation π at τ_π with the
  quasi-static values of Eq. 53 (arXiv:1405.3590, Sect. IV.7);
  `EFTturnonpiInitial` defaults to 0.01 (a scale factor) and must be lowered
  for early modified gravity; matter and curvature start at a ∼ 10⁻⁸ [src].
  The stated reason is speed for models close to GR at early times [src].
- hi_class derives two attractor solutions, external-field (GR recovered
  early; α_i, Ω_DE ≪ 1 around the initial time) and gravitating
  (modification significant but time-independent early) (arXiv:1909.01828,
  Sects. 4.2–4.3). Dark-energy isocurvature modes grow as τ^{n_±+1}
  (Eq. 4.7); by default models whose isocurvature mode outgrows the
  adiabatic one in the radiation era are excluded, for predictivity [src:
  Sect. 4.2].
- MGCAMB switches modified equations on at a_trans (`GRtrans`, default
  10⁻³ per arXiv:2407.11968, App. A) [src].
- mochi_class requires `method_gr_smg = on`: standard equations, the scalar
  acting as Λ with vanishing α's, down to `z_gr_smg` = 99 by default
  (arXiv:2407.11968, Sect. 3.1) [src].

### Step 5. Decide where the quasi-static approximation (QSA) is used
<!-- key: step-5-decide-where-the-quasi-static -->

The QSA drops time derivatives of the scalar perturbation inside its sound
horizon (c_s²k² ≫ a²H²), turning its equation into a constraint
(arXiv:2407.11968, Sect. 2.2, Eq. 29) [src]. The codes differ
[src: arXiv:2407.11968, Sect. 2.2]:

| Code | QSA use |
|---|---|
| MGCAMB, mgclass | on all scales and at all times |
| EFTCAMB | never (full dynamics) |
| QSA_class (CLASS branch for this test) | three QSA formulations against the exact solution (arXiv:2011.05713) |
| hi_class (2019) | per mode and per epoch, three modes: FFD (full dynamics always), FQS (QSA always), AUTO (switching) |
| mochi_class | hybrid, with the QSA allowed until late times |

hi_class AUTO uses four user precision parameters (arXiv:1909.01828,
Sect. 5.2) [src]:

- z_FD: below it the QSA is forbidden, so late-time dark-energy dynamics
  are not missed;
- T_μ: mass trigger, μ² > T_μ² ≫ 1, μ being the effective scalar mass in
  the perturbation equation (Eq. 5.4);
- T_r: radiation trigger, μ_r² ≡ (μ²/Ω_r²)(aH/c_r k)² > T_r², with
  c_r = 1/√3 (Eq. 5.5);
- ε_decay: the switch to QSA is delayed until oscillations about the QS
  solution have decayed by this factor, using the decay slope s of
  Eq. 5.7 and a_fin > ε_decay^{−1/s} a_ini (Eq. 5.9).

The time sampling of the triggers follows Eq. 5.10 with bounds N_min,
N_max, and at most 6 switches are honoured, the rest forced to full
dynamics, because the authors prefer the QSA at early times, when dark
energy does not gravitate, to the QSA at late times [src: Sect. 5.3]. The
method must be set explicitly to AUTO; otherwise full dynamics is used, and
the defaults were chosen for accuracy over speed [src: Sect. 5.3].

Which QSA is applied also matters. Pace et al. 2021 (arXiv:2011.05713)
compare three formulations, the QSA applied to the field equations, to
the equations of the two metric potentials, and the attractor solution of
the EoS approach: all agree on very small scales; except in f(R), where
all three coincide, they depart from the exact solution at
k ≲ 3–4 × 10⁻³ h Mpc⁻¹; the field-equation and EoS forms reproduce
P(k), C_ℓ^TT and lensing within 1 % for k/H_0 of a few and ℓ > 5, while
the potential-equation form has "limited applicability" [src]. Most
modified-gravity N-body codes also take the QSA (Step 6).

### Step 6. Go non-linear: modified-gravity N-body codes
<!-- key: step-6-go-non-linear-modified-gravity-n-body -->

The Boltzmann codes stop at linear scales. Beyond them the scalar-field
equation, non-linear because of screening, is solved on a mesh by
Newton–Gauss–Seidel relaxation with multigrid acceleration
(arXiv:1506.06384, Sect. 3.2) [src]. The codes, one line each:

| Code | Base and mesh | Models and extras | Source |
|---|---|---|---|
| DGPM | fixed-grid PM, FFT Poisson solver; residual < 10⁻¹⁰ within 3 V-cycles | DGP (Vainshtein) | arXiv:1506.06384, Sect. 4.1.1 |
| ECOSMOG | RAMSES AMR, multigrid on all refinement levels | f(R), DGP, dilaton, symmetron, Galileons | arXiv:1110.1379; arXiv:1506.06384, Sect. 4.1.2 |
| ISIS | RAMSES, non-linear multigrid; `isis-nonstatic` keeps time derivatives | f(R), symmetron, disformal, cubic Galileon | arXiv:1307.6748; arXiv:1506.06384, Sect. 4.1.4 |
| MG-Gadget | P-Gadget3 TreePM+SPH, AMR grid built from the oct-tree | f(R) with hydrodynamics, cooling and star formation, AGN feedback studied; massive neutrinos | arXiv:1305.2418; arXiv:1506.06384, Sect. 4.1.3 |
| MG-Arepo | Arepo moving mesh, TreePM; AMR relaxation solver; MG force on larger time steps | f(R), nDGP; δf massive neutrinos | arXiv:2409.03522, Sect. 3.1.1 |
| MG-GLAM | GLAM parallel PM, multigrid relaxation; full solver, accuracy limited by the PM grid | f(R) variants, symmetron, coupled quintessence; Vainshtein and K-mouflage in a companion code | arXiv:2110.00328, abstract, Sect. 1 |
| PySCo-EFT, ECOSMOG-EFT | Python PM and RAMSES AMR, multigrid with Vainshtein screening | Horndeski with c_T = 1, in EFT of dark energy | arXiv:2604.15434 |
| MG-COLA, PANDA | approximate MG solvers (COLA: fixed-grid PM with 2LPT) | in the Euclid comparison, nDGP within 1 % of MG-Arepo even at k > 1 h Mpc⁻¹ | arXiv:2409.03522, Sects. 3.2, 4 |

Run time: MG-GLAM takes about 3–5 times the time of the same ΛCDM GLAM run
and is "at least 100 times faster" than ECOSMOG and MG-Arepo for the same
box and particle number (arXiv:2110.00328, Sect. 1) [src]. In the Euclid
comparison full field solvers cost up to a factor of ten more CPU time
than ΛCDM, the approximate ones not significantly more
(arXiv:2409.03522, Sect. 4) [src].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### QSA: what it buys and where it fails
<!-- key: qsa-what-it-buys-and-where-it-fails -->

- **Speed.** Quartic Galileon (sound speed near c): AUTO ≈ 2.6 times
  faster than FFD with sub-per-cent differences; FQS ≈ 6.5 times faster
  but wrong at k ≲ 10⁻³ h Mpc⁻¹ (arXiv:1909.01828, Sect. 5.3, Fig. 9:
  T_μ = 100, T_r = 10, ε_decay = 0.01, z_FD = 0) [src]. Brans–Dicke with
  ω_BD = 50: AUTO and FQS faster by 2 and 1.25 [src]. For low kineticity
  the gain is orders of magnitude, and the authors state that without the
  approximation such models "cannot be sensibly studied" [src].
- **Hard limit.** k ∼ 10⁻³ h Mpc⁻¹ is the largest scale at which the QSA
  can work in the best case, set by the cosmological horizon
  (arXiv:1909.01828) [src: Sect. 5.3].

- **Sound speed.** As c_s decreases the speed gain disappears and the
  1 %-accurate range shrinks; for c_s² ≲ O(10⁻⁴) no linear scale has
  better than 1 % accuracy in QSA [src: Sect. 5.3]. Sawicki & Bellini
  2015 place the breakdown at the dark-energy sound horizon, not the
  cosmological horizon; as an order of magnitude, the QSA is usable for
  current weak-lensing and velocity surveys only if c_s ≳ 1 % of c, for
  Euclid-class surveys if c_s ≳ 10 %, never for the CMB ISW effect, and
  for CMB lensing only if c_s ≳ 10 % (arXiv:1503.06831) [src].
- **Small-scale QSA error in f(R).** The hi_class-style QSA (Eq. 29) can
  misplace small-scale matter perturbations in some f(R) models; the
  metric-potential QSA as in MGCAMB "performs significantly better" for
  f(R) at k ≳ 0.1 h Mpc⁻¹ (arXiv:2407.11968, Sect. 2.2, Fig. 1) [src].
- **Cost of QSA off at late times.** In mochi_class, enabling the QSA for
  z < 10 cuts perturbation time by up to 50 %; the hi_class comparison
  run forced full dynamics from z = 10 "as recommended by its developers"
  (arXiv:2407.11968, Sect. 4.3, Table 1) [src].

### α basis or stable basis
<!-- key: alpha-basis-or-stable-basis -->

- In the α basis, viability is found by trial and error. In a
  two-parameter scan with a stable region of 22 % of the prior volume,
  unstable models outnumber viable ones 3.5 to 1, so starting from the
  stable basis gives an overall 56 % background-module speed-up although
  each background takes twice as long (arXiv:2407.11968, Sect. 4.3) [src].
- Numerical misclassification: designer f(R) on a ΛCDM background
  (c_s² = 1 exactly) shows spurious c_s² < 0 when c_s² is derived from
  the α's through Eq. 7, because of cancellation errors amplified by a
  small D_kin; the stable basis takes c_s² as input and avoids it
  [src: Sect. 2.1, Fig. 1].
- A dissenting view (Denissenya & Linder 2018, cited there) holds that the
  stable basis brings no advantage; the mochi_class authors disagree
  [src: Sect. 2.1]. That paper was not read here.

### EFT mapping or direct δφ integration (H-EFTCAMB)
<!-- key: eft-mapping-or-direct-deltaphi-integration-h -->

`EFTCAMB_evolve_delta_phi = False` maps the covariant theory to the EFT
and reuses the EFTCAMB solver; `True` integrates the δφ equations directly
(arXiv:2603.01662, Sect. 2.2.1). The direct route is needed when φ̇ crosses
zero (oscillating fields), a coordinate singularity of the unitary gauge
that the EFT route cannot evolve [src].

### μ–γ conversion or direct μ–Σ (MGCAMB)
<!-- key: mu-gamma-conversion-or-direct-mu-sigma-mgcamb -->

Before 2023, a μ–Σ model was converted to μ–γ with γ = 2Σ/μ − 1, valid
only well after the onset of matter domination. `MG_flag = 5` uses μ and
Σ directly in the perturbation equations (arXiv:2305.05667, Sect. II.2.3,
Eqs. 19–22) [src]. For late-time modifications (all models then
implemented) the two give equivalent results; the direct form is for
models with early-time μ, Σ [src].

### Dark-energy perturbations in MGCAMB
<!-- key: dark-energy-perturbations-in-mgcamb -->

`MGDE_pert` adds quintessence or PPF dark-energy perturbations as in
CAMB. Without it, MGCAMB with μ = γ = Σ = 1 and w ≠ −1 differs slightly
from CAMB; with it, a model-agnostic MG test is "strictly speaking,
theoretically inconsistent", since w is then an effective quantity, not a
fluid. The authors leave the choice to context (arXiv:2305.05667,
Sect. II.2.6) [src].

### QSA in N-body codes, and full or approximate solvers
<!-- key: qsa-in-n-body-codes-and-full-or-approximate -->

- The QSA, used by most modified-gravity N-body codes, was tested for the
  symmetron, where non-static effects are expected to be largest:
  `isis` and `isis-nonstatic` differ by < 0.5 % on all scales and
  redshifts shown; in that implementation particles do not follow the
  field's rapid oscillations, because of different time steps
  (arXiv:1506.06384, abstract, Sect. 6) [src].
- Full field solvers against approximate ones: in the Euclid comparison
  the full solvers (MG-Arepo, MG-Gadget, ECOSMOG, ISIS, PySCo) agree on
  the boost to ≲ 1 % up to k ≲ 1 h Mpc⁻¹ and ≲ 3 % up to 10 h Mpc⁻¹; PANDA
  and MG-COLA stay within 3 % up to k ≲ 7 h Mpc⁻¹, at a much lower cost
  (arXiv:2409.03522, Sect. 4) [src].
- PM resolution: a fixed-grid code (COLA, PySCo without AMR) lacks power
  at k ≳ 1 h Mpc⁻¹ in ΛCDM itself (arXiv:2409.03522, Sect. 3.2) [src];
  MG-GLAM's accuracy is likewise "only limited by the resolution of the
  PM grid" (arXiv:2110.00328, Sect. 1) [src].

### Which code for which question
<!-- key: which-code-for-which-question -->

- A theory with a Lagrangian, especially an oscillating scalar:
  H-EFTCAMB direct δφ (only code stated to handle general oscillating
  Horndeski fields; arXiv:2603.01662, Sect. 2.2.1) or hi_class covariant
  models (arXiv:1909.01828).
- Effective-theory constraints with Planck-style forms: hi_class
  `propto_omega`, `propto_scale`, `planck_linear`, `planck_exponential`
  (arXiv:1605.06102, Table 1b), or EFTCAMB; H-EFTCAMB now accepts
  α_i = c_iΩ_DE through `EFTflag = 2`, `AltParEFTmodel = 1`
  (arXiv:2603.01662, Sect. 3.3).
- Non-parametric reconstructions of Horndeski functions: mochi_class
  (input tables of ΔM_*², D_kin, c_s²; arXiv:2407.11968, Sect. 3.1) or
  MGCAMB cubic splines of μ, Σ, Ω_X (arXiv:2305.05667, Sect. II.2.5,
  heading only read).
- Survey-style μ–Σ constraints, Planck and DES forms, f(R) and
  symmetron in QSA: MGCAMB (arXiv:2305.05667, Sect. II.1); with binned or
  hybrid time and scale dependence, Q–R–D forms, curvature and massive
  neutrinos throughout: ISiTGR, a patch to CAMB and CosmoMC
  (arXiv:1908.00290, abstract, Sect. IV).
- Horndeski in the EoS formalism, or f(R) in CLASS: EoS_class
  (arXiv:1905.06795, Sect. 1).
- Non-linear P(k), haloes, velocity divergence: a full N-body solver
  (Step 6); many runs for mocks or emulators: MG-GLAM (arXiv:2110.00328,
  abstract); baryons together with f(R): MG-Gadget (arXiv:1305.2418).

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| EFTCAMB vs hi_class, α parametrisation (Eq. 39) | "well below the 1 % level"; two extreme models needed raised precision for EE, TE | 2017 comparison | arXiv:1709.09135 | Sect. IV.6 |
| COOP vs EFTCAMB, P(k) | 2–3 % at k ≳ 1 h Mpc⁻¹; CMB < 1 % | same | arXiv:1709.09135 | Sect. IV.6, V |
| hi_class AUTO speed-up, quartic Galileon | ≈ 2.6 (sub-per-cent); FQS ≈ 6.5 | T_μ = 100, T_r = 10, ε_decay = 0.01, z_FD = 0 | arXiv:1909.01828 | Sect. 5.3 |
| QSA largest usable scale | k ∼ 10⁻³ h Mpc⁻¹ | best case | arXiv:1909.01828 | Sect. 5.3 |
| QSA dead zone | c_s² ≲ O(10⁻⁴): no linear scale within 1 % | α_i = c_iΩ_DE, c_B = 1.5, w_0 = −0.9 | arXiv:1909.01828 | Sect. 5.3, Fig. 11 |
| QSA validity in sound speed | c_s ≳ 1 % (current WL, PV), ≳ 10 % (Euclid, CMB lensing), never for ISW | order-of-magnitude | arXiv:1503.06831 | abstract |
| mochi_class vs CAMB-based codes, CMB | within ∼ 0.25 %; > 0.05 % traced to CLASS vs CAMB | high-precision settings | arXiv:2407.11968 | Sect. 4.1 |
| EFTCAMB vs MGCAMB, low-ℓ TT | ∼ 0.2 %, from different CAMB versions | same | arXiv:2407.11968 | Sect. 4.1 |
| mochi_class vs hi_class, P(k) | ∼ 0.01 % on average | scale-independent-growth models | arXiv:2407.11968 | Sect. 4.2 |
| mochi_class full dynamics vs EFTCAMB | 10⁻⁴ | designer f(R) | arXiv:2407.11968 | Sect. 4.2 |
| mochi_class vs MGCAMB, Hu–Sawicki | > 0.2 % only at k ≳ 1 h Mpc⁻¹, traced to MGCAMB | — | arXiv:2407.11968 | Sect. 4.2 |
| mochi_class run time vs hi_class | −40 % (cubic Galileon), −17 % (`propto_omega`); 13.2 s and 13.3 s total, one thread, Apple M1 Pro | QSA allowed at z < 10 | arXiv:2407.11968 | Table 1 |
| MGCAMB GR limit vs CAMB | < 0.1 % in C_ℓ^TT and P(k), 0.05 ≤ Σm_ν ≤ 0.5 eV, 10⁻⁴ ≤ a_trans ≤ 0.1; for a_trans < 0.005, RSA delayed 20 times, run time doubled | 2019 version | arXiv:1901.05956 | Sect. III.3 |
| MGCosmoMC GR limit, Planck MCMC | same means and errors; Σm_ν < 0.206 (CosmoMC), 0.198 and 0.212 eV (a_trans = 0.01, 0.001) | ΛCDM + Σm_ν | arXiv:1901.05956 | Table 1 |
| EFTCAMB π switch-on | `EFTturnonpiInitial` = 0.01 | default | arXiv:1405.3590 | Sect. IV.7 |
| mochi_class GR-approximation end | `z_gr_smg` = 99 | default | arXiv:2407.11968 | Sect. 3.1 |
| mochi_class input sampling | Δln a ≤ 7.5 × 10⁻⁴ over ln a ∈ [−2, 0] | recommended | arXiv:2407.11968 | Sect. 3.1 |
| hi_class AUTO switches | at most 6 | — | arXiv:1909.01828 | Sect. 5.3 |
| EoS_class vs hi_class, C_ℓ^TT, C_ℓ^φφ, P(k) | sub-per-cent, < 0.1 % in almost all cases; largest at TT ℓ ≳ 1000, from CLASS 2.6.3 vs 2.4.5 | α_x models 1, 3–6 | arXiv:1905.06795 | Sect. 4 |
| QSA formulations vs exact | depart at k ≲ 3–4 × 10⁻³ h Mpc⁻¹; observables within 1 % for k/H_0 of a few, ℓ > 5 | Horndeski models | arXiv:2011.05713 | abstract |
| N-body codes, ΛCDM P(k), MG switched off | 1 % at k ≲ 1 h Mpc⁻¹; ∼ 5 % at k ∼ 5 h Mpc⁻¹ | ECOSMOG, ISIS, MG-Gadget | arXiv:1506.06384 | Sect. 6 |
| N-body codes, f(R) boost P/P_ΛCDM | < 1 % for k ≲ 7 h Mpc⁻¹ | same initial conditions | arXiv:1506.06384 | Sect. 6 |
| DGPM vs ECOSMOG (fixed grid), DGP boost | ≲ 1 % for k ≲ 7 h Mpc⁻¹ | — | arXiv:1506.06384 | Sect. 6 |
| Symmetron, QSA vs non-static | < 0.5 % | `isis` vs `isis-nonstatic` | arXiv:1506.06384 | Sect. 6 |
| Full solvers, boost (F5, F6, N1.2, N5.6) | ≲ 1 % to k ≲ 1, ≲ 3 % to k ≲ 10 h Mpc⁻¹; f(R) < 1 % to k ≈ 10 | MG-Arepo reference, z = 1 and 0.667 | arXiv:2409.03522 | Sects. 3.2, 4 |
| AMR codes, nDGP boost at k > 1 h Mpc⁻¹ | ∼ 2 % from MG-Arepo | ECOSMOG, ISIS | arXiv:2409.03522 | Sect. 3.2 |
| Approximate solvers, boost | ≤ 3 % to k ≲ 7 h Mpc⁻¹ | PANDA, MG-COLA | arXiv:2409.03522 | Sect. 4 |
| Relative halo mass function | within 5 %, except the largest and smallest masses | all codes | arXiv:2409.03522 | Sect. 4 |
| CPU cost relative to ΛCDM | up to × 10 (full solvers); MG-GLAM 3–5, ≥ 100 times faster than ECOSMOG, MG-Arepo | — | arXiv:2409.03522; arXiv:2110.00328 | Sect. 4; Sect. 1 |
| PySCo-EFT, ECOSMOG-EFT | < 0.5 % vs linear theory on large scales, similar between codes non-linearly; numerical effects < 2 % at k = 10 h Mpc⁻¹ | EFT of DE, Vainshtein | arXiv:2604.15434 | abstract |

High-precision settings used for the mochi_class comparison
(arXiv:2407.11968, App. A) [src]: CLASS-based, `perturbations_sampling_stepsize = 0.01`,
`l_logstep = 1.026`, `l_linstep = 25`, `k_max_tau0_over_l_max = 8.`,
`k_per_decade_for_pk = 200`, `l_max_scalars = 5000`, `P_k_max_h/Mpc = 12.`,
`delta_l_max = 1000`, `l_switch_limber = 50`, both `start_*` parameters
10⁻⁴; CAMB-based, `transfer_high_precision = T`, `k_eta_max_scalar = 80000`,
`do_late_rad_truncation = F`, the three boosts at 2, `l_max_scalar = 10000`,
`accurate_polarization = T`, `accurate_reionization = T`; EFTCAMB
`EFTCAMB_turn_on_time = 1e-10`, `EFTtoGR = 1e-10`; MGCAMB `GRtrans = 1e-3`.

## What goes wrong
<!-- key: what-goes-wrong -->

- **α_B differs by a factor between codes.** (α_B)_EFTCAMB =
  −½ (α_B)_hi_class (arXiv:2603.01662, Sect. 3.3, footnote) [src]. A prior
  or a constraint on α_B copied between codes without this factor is
  wrong. Test: reproduce one published model in both codes.
- **Isocurvature-sensitive models.** When the modification does not decay
  fast enough to the past, dark-energy isocurvature modes do not decay and
  results depend on initial conditions that the codes set differently;
  such models were excluded from the 2017 comparison (arXiv:1709.09135,
  Sect. IV.6) [src]. Test: check that adiabatic initial conditions are an
  attractor in the radiation era (their step 3, Sect. V; hi_class's
  default exclusion, arXiv:1909.01828, Sect. 4.2).
- **Forced QSA hiding an instability.** Forcing FQS at the initial time
  can hide a rapidly growing homogeneous solution; hi_class keeps the
  initial-condition stability tests under FQS unless disabled
  (arXiv:1909.01828, Sect. 5.3) [src].
- **Spurious instability flags.** Derived c_s² can oscillate negative
  from cancellation errors (designer f(R), small D_kin)
  (arXiv:2407.11968, Sect. 2.1) [src]. Test: compute in the stable basis,
  or check the flagged region with raised precision.
- **Precision is model dependent.** Default precision may not reproduce
  sub-per-cent agreement; the user must raise precision until outputs stop
  changing (arXiv:1709.09135, Sect. V, step 4) [src].
- **Version validated is not version used.** The 2017 comparison validates
  the named versions only (EFTCAMB Sep17, Oct15 for JBD; hi_class v1.1;
  COOP v1.1) [src: Sects. III.1–III.3, V]. A 0.2 % EFTCAMB–MGCAMB low-ℓ
  difference came from the underlying CAMB versions
  (arXiv:2407.11968, Sect. 4.1) [src], and the largest EoS_class–hi_class
  difference, TT at ℓ ≳ 1000, from CLASS 2.6.3 against 2.4.5
  (arXiv:1905.06795, Sect. 4) [src].
- **Base N-body code read as a modified-gravity effect.** ΛCDM differences
  between base codes (RAMSES, P-Gadget3) propagate into the modified
  results; f(R) P(k) differences were "driven almost exclusively" by the
  base codes, so the comparison is made on the ratio to a ΛCDM run of the
  same code from the same initial conditions (arXiv:1506.06384, Sect. 6)
  [src]. AMR refinement criteria made RAMSES-based codes lose small-scale
  power against tree codes (arXiv:2409.03522, Sect. 3.2) [src].
- **Parameter map bugs.** The authors name the map from model parameters
  to the code's basis as "the most probable place" for bugs in a model
  not in the comparison (arXiv:1709.09135, Sect. V, step 2) [src]. Test:
  recover a known limit (their step 5).
- **Stability outside GLPV in EFTCAMB.** Models with γ_3 ≠ −γ_4 or
  γ_6 ≠ 0 have no built-in physical stability test (arXiv:1405.3590,
  Sect. IV.6) [src].
- **Effective w treated as a fluid.** Switching on `MGDE_pert` in a
  model-agnostic MGCAMB test adds fluid perturbations that the MG
  parametrisation does not imply (arXiv:2305.05667, Sect. II.2.6) [src].
- **Early MG with a late switch-on.** MGCAMB's `GRtrans`, EFTCAMB's
  `EFTturnonpiInitial` and mochi_class's `z_gr_smg` all assume GR before a
  time; a model modified earlier needs them moved (arXiv:1405.3590,
  Sect. IV.7; arXiv:2407.11968, Sect. 3.1) [src].

The 2017 validation recipe for a new model or version (arXiv:1709.09135,
Sect. V) [src]: (1) a new version reproduces the validated one on the same
models; (2) the parameter map into the code's basis is checked; (3)
adiabatic initial conditions are an attractor; (4) precision is raised
until outputs stop changing; (5) a known limit is recovered.

## Reading list
<!-- key: reading-list -->

- Critique and validation: Bellini et al. 2017, arXiv:1709.09135 — the
  cross-code test, the extreme-model parameters (App. B.6–B.7) and the
  five-step validation recipe (Sect. V).
- Code: Zumalacárregui et al. 2016, arXiv:1605.06102 — α basis, stability
  tests, the built-in parametrisations.
- Method: Bellini et al. 2019, arXiv:1909.01828 — covariant backgrounds,
  initial conditions, the AUTO QSA and its triggers.
- Code: Hu et al. 2014, arXiv:1405.3590 — EFTCAMB flags, designer
  background, viability conditions, π initial conditions.
- Code: Ye et al. 2026, arXiv:2603.01662 — Horndeski module, δφ
  integration, α_B convention, Cobaya wrapper.
- Code: Cataneo & Bellini 2024, arXiv:2407.11968 — stable basis, QSA
  comparison with MGCAMB, high-precision settings, timings.
- Code: Zucca et al. 2019, arXiv:1901.05956 and Wang et al. 2023,
  arXiv:2305.05667 — MGCAMB GR limit, direct μ–Σ, DE perturbations.
- Critique: Sawicki & Bellini 2015, arXiv:1503.06831 — where the QSA
  breaks, by sound speed and observable; Pace et al. 2021,
  arXiv:2011.05713 — three QSA formulations against exact solutions.
- Code: Garcia-Quintero et al. 2019, arXiv:1908.00290 — ISiTGR
  parametrisations, binning, curvature. Pace et al. 2019,
  arXiv:1905.06795 — EoS_class and its validation against hi_class.
- Critique and validation (non-linear): Winther et al. 2015,
  arXiv:1506.06384 — first MG N-body comparison, QSA test; Euclid
  Collaboration: Adamek et al. 2024, arXiv:2409.03522 — methods review,
  full and approximate solvers, costs.
- Code (N-body): Li et al. 2012, arXiv:1110.1379 (ECOSMOG); Llinares et
  al. 2014, arXiv:1307.6748 (ISIS); Puchwein et al. 2013,
  arXiv:1305.2418 (MG-Gadget); Ruan et al. 2022, arXiv:2110.00328
  (MG-GLAM); Ganjoo et al. 2026, arXiv:2604.15434 (PySCo-EFT,
  ECOSMOG-EFT).

## Not verified
<!-- key: not-verified -->

- The agreement levels quoted from the Euclid code comparison (arXiv:2409.03522,
  Sect. 4) for the full solvers: on 2026-10-22 the coordinator found the
  paper's statements that full solvers agree down to k ≈ 10 h Mpc⁻¹ and that
  the approximate schemes stay within 2% of MG-Arepo, but not the exact
  percentages; they may sit in its figures.
- MGCAMB cubic-spline reconstruction (arXiv:2305.05667, Sect. II.2.5) and
  the CDM-only coupling (Sect. II.2.2): headings read, bodies not.
- MGCLASS II settings (arXiv:2112.14175): only its abstract is in L2; that
  it uses the QSA everywhere is stated by arXiv:2407.11968, Sect. 2.2.
- Denissenya & Linder 2018 (stable basis critique) and Kennedy et al. 2018,
  Lombriser et al. 2018 (stable basis origin): cited in arXiv:2407.11968,
  not read; no identifiers recorded.
- Hu et al. 2014 strategy for mitigating the cost of no QSA in EFTCAMB:
  cited in arXiv:2407.11968, footnote 2, not read.
- hi_class default values of T_μ, T_r, ε_decay, z_FD: the paper reports
  values used in its figures, not the shipped defaults.
- MG-Arepo's own paper (Arnold et al. 2019), COOP's code paper and
  CLASS_EOS_FR's: described here only through arXiv:2409.03522,
  arXiv:1709.09135 and arXiv:1905.06795; not read, no identifiers
  recorded. The MG-GLAM derivative-coupling companion paper
  was seen by abstract only.
- The `EFTflag` numbering read is that of the EFTCAMB notes v3.0 HTML;
  H-EFTCAMB adds `EFTflag = 5` (arXiv:2603.01662), and later numbering was
  not checked against the code.
