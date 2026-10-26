# Linear growth, growth rate and growth index: solving and checking — cosmo-theory-foundations dossier

Scope: how D(a) and f are computed in practice (which equation, which
initial condition, which normalisation), how accurate the closed-form
shortcuts are on f itself rather than on the growth factor, how codes define
the fσ8 they output when growth is scale-dependent, what second-order growth
and the growth index look like beyond ΛCDM, and the checks that catch a wrong
growth module.
Snapshot: 2026-10-18.
From: Huterer 2023, Sects. 2.1–2.3 and 4.1; Ivanov 2026, Sect. 2.1; Planck
2018 (arXiv:1807.06209) and eBOSS fσ8 definitions.

Already in L2, not repeated here: Linder's growth equations
(arXiv:astro-ph/0507263, Eqs. 7, 11), the growth-index formula
γ = 0.55 + 0.05[1 + w(z = 1)] (same paper, Eq. 17) and its accuracy on the
growth factor g, the Planck and eBOSS definitions of fσ8 (arXiv:1807.06209,
Eq. 27; arXiv:2007.08991, Eq. 19), the 0.6 against 0.55 exponent, the neutrino growth δ_cdm ∝ a^(1 − 3f_ν/5)
(`physics-and-methods.md#linear-growth-and-its-approximations`,
`results.md#growth-rate-and-growth-index-approximations`,
`systematics.md#growth-rate-approximations-used-outside-their`). Measured γ,
μ–Σ and modified-gravity kernels: `cosmo-dark-energy-modified-gravity`;
velocity-survey fσ8: `cosmo-peculiar-velocities`.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Know the equation's assumptions before solving it
<!-- key: step-1-know-the-equation-s-assumptions-before -->

Huterer 2023 (arXiv:2212.05003) starts from
δ̈_k + 2(ȧ/a) δ̇_k = (4πGρ_M − k² c_s²/a²) δ_k − (2/3)(T/a²) k² S_k [src: Eq. 2]
and reduces it to δ̈ + 2Hδ̇ − 4πGρ_M δ = 0 [src: Eq. 4] under five
assumptions: general relativity, adiabatic initial conditions, sub-horizon
scales (k ≫ H0), scales above the Jeans length, and linear theory, "which
corresponds roughly to scales k ≲ 0.1 h/Mpc today" [src: Sect. 2.1]. Eq. 4 is
stated for 0.001 ≲ k ≲ 0.1 h/Mpc; near the horizon "Equation (4) is modified
… due to relativistic effects", and modified gravity and massive neutrinos
make growth scale-dependent [src: Sects. 2.1, 2.3]. Single-component
solutions [src: Eqs. 5–8]: δ = A_1 + A_2 ln t (radiation), B_1 t^(2/3) + B_2 t⁻¹
(matter), C_1 + C_2 e^(−2H_Λ t) (Λ).

### Step 2. Write it in the variable the code integrates
<!-- key: step-2-write-it-in-the-variable-the-code -->

Linder 2005 gives four forms in g ≡ δ/a, primes d/d ln a, G = G/G_Newton
[src: arXiv:astro-ph/0507263, Sect. III, Eqs. 8–11]:

g'' + [4 + (1/2)(ln H²)'] g' + [3 + (1/2)(ln H²)' − (3/2) G Ω_m(a)] g = 0  (Eq. 8),

g'' + [3 − q] g' + [2 − q − (3/2) G Ω_m(a)] g = 0  (Eq. 9), q = −aä/ȧ²,

and Eqs. 10–11 (L2). "All these forms are equivalent" [src], but as printed
Eq. 10 carries G on the Ω_w term, (3/2)[1 − w(a)] G Ω_w(a) g. Substituting
(ln Ω_m)' = 3wΩ_w (flat, matter + w) into Eq. 11 gives the g coefficient
(3/2)(1 − G) + (3/2)(G − w)Ω_w, which equals Eq. 10's only for G = 1 [der].
For a modified-gravity G, integrate Eq. 8, Eq. 9 or Eq. 11, not Eq. 10.

Huterer writes the same equation for the suppression factor relative to
EdS: 2 d²g/d(ln a)² + [5 − 3w(a)Ω_DE(a)] dg/d ln a + 3[1 − w(a)]Ω_DE(a) g = 0
[src: arXiv:2212.05003, Eq. 10], equal to Linder's Eq. 10 with G = 1 [der].

For the growth rate itself, Linder & Cahn 2007 use G ≡ d ln(δ/a)/d ln a,
so f = 1 + G [der], and [src: arXiv:astro-ph/0701317, Eq. 3]

dG/d ln a + [4 + (1/2) d ln H²/d ln a] G + G² + 3 + (1/2) d ln H²/d ln a − (3/2) Ω_m(a) = 0,

with the formal quadrature [src: Eq. 4]

G(a) = −1 + [a⁴H(a)]⁻¹ ∫_0^a (da'/a') a'⁴ H(a') [1 + (3/2) Ω_m(a') − G²(a')].

Neglecting G² "g(a) = δ/a agrees with the exact solution to ∼0.2%" [src:
arXiv:astro-ph/0701317, Sect. II]; that is an analytic shortcut, not a substitute for integrating
Eq. 3.

### Step 3. Start in the growing mode, and choose the normalisation
<!-- key: step-3-start-in-the-growing-mode-and-choose-the -->

The matter-era growing mode is δ ∝ a (Step 1), so a code starts at a_ini in
matter domination with D = a, dD/d ln a = a. Two normalisations then
coexist:

| Name | Definition | Source |
|---|---|---|
| D, normalised today | D(a) = δ(a)/δ(1), D(1) = 1 | arXiv:2212.05003, Eq. 9 [src] |
| g, suppression relative to EdS | D(a) ≡ a g(a)/g(1); g = 1 in EdS; g(z = 0) ≃ 0.78 for Ω_M = 0.3 | arXiv:2212.05003, Eq. 11 and Sect. 2.3 [src] |

Using a D normalised to a at early times where D(1) = 1 is expected
rescales σ8(z) by the factor g(z = 0) [der]. How much the start epoch and the
radiation term in H change D and f was not read in a paper.

### Step 4. Use the growth index only where its error on f is known
<!-- key: step-4-use-the-growth-index-only-where-its -->

Linder's accuracy figures are for the growth factor g, not for f: with
Eq. 17, better than 0.05% for Λ over Ω_m ∈ [0.22, 1], 0.2% (0.4%) for
w = −0.8 (−0.5) over Ω_m ∈ [0.2, 1], 0.25% for w0 = −0.82, wa = 0.58
[src: arXiv:astro-ph/0507263, Sect. V.1; L2 `systematics.md`]. No paper
giving the error of f = Ω_m(z)^γ on f itself was read. Linder writes that the
formula's "primary purpose is not a fit as such (the exact solution requires
only solving a second order differential equation)" [src: Sect. V.1]: a
precision fσ8 model solves the equation.

Closed forms for γ, all derived under near-matter domination:

- Linder & Cahn: γ ≈ 3(1 − w_∞)/(5 − 6w_∞) − B x a^x/[(5 − 6w_∞)(5 − 6w_∞ + 2x)]
  [src: Eq. 18], w_∞ the early-time equation of state, Ω_w ∝ a^(−3w_∞)(1 + B a^x)
  (Eq. 17); for w0wa, B = 3wa, x = 1, and the correction coefficient is
  −(3/143) wa, "generally ≲ 0.01" [src: arXiv:astro-ph/0701317, Sect. III].
  For w = −1, "the asymptotic value is γ_∞ = 6/11 = 0.545 compared to the
  numerically obtained fit γ = 0.55 for the whole growth history" [src:
  arXiv:astro-ph/0701317, Sect. II].
- Wang & Steinhardt, as quoted by Kiakotou, Elgarøy & Lahav 2008: f = Ω_m^α(z),
  α = α_0 + α_1[1 − Ω_m(z)], α_0 = 3/[5 − w/(1 − w)],
  α_1 = (3/125)(1 − w)(1 − 3w/2)/(1 − 6w/5)³ for constant w [src:
  arXiv:0709.0253, Eqs. 13–15].
- Stability of the definition: with G = Ω_m^γ − 1, γ "varies from its present
  value by less than 2% back to a ≪ 1 and 6% forward to a = 5" for Λ; the two
  alternative definitions −G/Ω_w and G/ln Ω_m do not stay constant [src:
  arXiv:astro-ph/0701317, Sect. III, Eq. 16].
- A non-clustering fraction Ω_e of matter-like density (early dark energy, and
  by the same equation massive neutrinos below their free-streaming scale)
  gives g ∝ a^((−5 + sqrt(25 − 24Ω_e))/4) ≈ a^(−(3/5)Ω_e), i.e. γ = 3/5, and
  γ ≈ 3/5 + (3/125)Ω_e at next order [src: arXiv:astro-ph/0701317, Eq. 19].
- DGP: γ_∞,DGP = 11/16 = 0.6875 [src: arXiv:astro-ph/0701317, Eq. 26]; numerically 0.665 today for
  Ω_m = 0.28, and "the single parameter γ = 0.68 is an excellent approximation
  for growth at any time through the present, holding constant to 2%"
  [src: Sect. IV.2].

### Step 5. Know which "fσ8" the code returns
<!-- key: step-5-know-which-fsigma8-the-code-returns -->

CAMB's (version `2.0.4`) `get_fsigma8` docstring: "For general models fσ8 is defined as
in the Planck 2015 parameter paper in terms of the velocity-density
correlation: σ²_vd/σ_dd for 8 h⁻¹Mpc spheres" [src: CAMB source,
`camb/results.py`]; `get_sigmaR` takes `var1`, `var2` (default `delta_tot`)
and R in h⁻¹Mpc or Mpc [src: same]. With massive neutrinos the
velocity–density fσ8, f × σ8 of total matter and σ8 of the cb field are
different quantities [der]; their sizes were not read in a paper.

A fitting form for f(k) with neutrinos: f ≈ μ(k, f_ν, Ω_DE) Ω_m^α(z), μ = 1 −
A(k)Ω_DE f_ν + B(k) f_ν² − C(k) f_ν³, with A, B, C tabulated in the paper's
Table II; at 8 h⁻¹Mpc, f ≈ (1 − 0.8 Ω_DE f_ν + 3.9 f_ν² − 9.8 f_ν³) Ω_m^α(z),
valid for f_ν ≤ 0.15 [src: arXiv:0709.0253, Eqs. 16–18]; on small scales
μ = (1 − f_ν)^α_0 [src: Eq. 19]. The same paper's simplified neutrino growth
equation df/d ln a = −f² − [1/2 − (3/2) w(1 − Ω_m(z))] f + (3/2) Ω_m(z)(1 − f_ν)
[src: Eq. 12] differs from CAMB by "at most 7.5%" in ln δ [src: Sect. III.2].

### Step 6. Second order, for 2LPT initial conditions and PT kernels
<!-- key: step-6-second-order-for-2lpt-initial-conditions -->

Bernardeau et al. 2002 [src: arXiv:astro-ph/0112551, Sect. 2.7]: for open
models D_2 ≈ −(3/7) D_1² Ω_m^(−2/63) (Eq. 96); for flat models with Λ,
0.01 ≤ Ω_m ≤ 1, D_2 ≈ −(3/7) D_1² Ω_m^(−1/143), "to better than 0.6%"
(Eq. 97); the 2LPT displacement is x(q) = q − D_1 ∇_q φ^(1) + D_2 ∇_q φ^(2)
(Eq. 98). The EdS-kernel shortcut and its cost in loop calculations are in
`deep/eft-perturbation-theory.md`.

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Solve, or use Ω_m^γ
<!-- key: solve-or-use-omegam-gamma -->

Solving costs one ODE per cosmology. The fixed index is accurate on g at
the levels Linder states (Step 4), not on f, and a single w(z = 1) does not
describe a crossing equation of state [der].

### Normalise to today or to the early universe
<!-- key: normalise-to-today-or-to-the-early-universe -->

D(1) = 1 is the convention of σ8(z) = σ8 D(z) (Huterer Eq. 9). Growth
suppression g is the convention of growth-index work. Mixing them is a
factor g(z = 0), ≃ 0.78 for Ω_M = 0.3 (arXiv:2212.05003, Sect. 2.3).

### Total-matter or cb growth
<!-- key: total-matter-or-cb-growth -->

DESI's template and bias use the cb field (L2). The cb growth rate departs
from the massless one in a scale-dependent way (Step 5); how large the
departure is was not read in a paper. It is a modelling choice to state
[der].

### Which fσ8
<!-- key: which-fsigma8 -->

Planck and CAMB: σ²_vd/σ_dd for total matter; eBOSS: f = ∂ ln σ8/∂ ln a
(L2); a template fit: f × σ8 at the fiducial shape. With massive neutrinos
they differ; no paper giving the size was read.

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Validity of the growth ODE | 0.001 ≲ k ≲ 0.1 h/Mpc | GR, adiabatic, linear | arXiv:2212.05003 | Sect. 2.1 |
| g(z = 0) | ≃ 0.78 (Ω_M = 0.3) | flat ΛCDM | arXiv:2212.05003 | Sect. 2.3 |
| Neglecting G² in the quadrature | ∼0.2% on g | ΛCDM | arXiv:astro-ph/0701317 | Sect. II |
| Growth-index formula on g | better than 0.05% (Λ, Ω_m ∈ [0.22, 1]); 0.2% (w = −0.8) | Eq. 17 | arXiv:astro-ph/0507263 | Sect. V.1 |
| Asymptotic γ for Λ | 6/11 = 0.545, against the fit 0.55 | ΛCDM | arXiv:astro-ph/0701317 | Sect. II |
| γ in DGP | 11/16 early; 0.665 today (Ω_m = 0.28); 0.68 to 2% | DGP | arXiv:astro-ph/0701317 | Eq. 26, Sect. IV.2 |
| Ω^0.6 instead of Ω^0.55 | "needless 6% error in β", bias 0.03 (11%) on Ω_m | concordance | arXiv:astro-ph/0701317 | Sect. III |
| D_2/D_1² | −(3/7) Ω_m^(−1/143), < 0.6% | flat Λ, 0.01 ≤ Ω_m ≤ 1 | arXiv:astro-ph/0112551 | Eq. 97 |
| Neutrino growth-rate fit | valid f_ν ≤ 0.15 | CMBFAST-calibrated | arXiv:0709.0253 | Eq. 18 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Eq. 10 of Linder used with G ≠ 1.** Gives the wrong modified-gravity
  growth (Step 2). Test: the four forms must agree numerically for the G
  used.
- **Growth started in a decaying mode.** Initial dD/d ln a ≠ D at a_ini
  leaves a t⁻¹ mode (Huterer Eq. 6). Test: move a_ini by a factor of ten;
  D(z)/D(0) must not change at the precision the analysis needs.
- **Normalisation mixed.** σ8(z) off by g(z = 0), ≃ 0.78 for Ω_M = 0.3
  (arXiv:2212.05003, Sect. 2.3). Test: D(0) = 1 and
  D(z) → a/g(1) at high z.
- **Ω_m^γ in a precision fσ8 model.** Its stated accuracy is on g, not on f
  (Step 4). Test: compare with the ODE at the lowest redshift fitted.
- **Today's Ω_m in Ω_m^γ.** The index takes Ω_m(z) = Ω_m(1 + z)³/E²(z) (L2).
- **Scale-independent f with massive neutrinos.** Test: compute f(k) from the
  Boltzmann code at two redshifts, for the cb field.
- **fσ8 compared across definitions.** Test: state σ²_vd/σ_dd or f × σ8, and
  the field.

## Reading list
<!-- key: reading-list -->

- Huterer 2023, arXiv:2212.05003 (review): Sects. 2.1–2.3 for the equation,
  its assumptions and the two normalisations.
- Linder 2005, arXiv:astro-ph/0507263 (foundation): Sect. III for the four
  forms of the growth equation; Sect. V for the index and its accuracy (L2).
- Linder & Cahn 2007, arXiv:astro-ph/0701317 (method): the G equation and
  quadrature, the asymptotic γ, early dark energy, DGP.
- Kiakotou, Elgarøy & Lahav 2008, arXiv:0709.0253 (method): scale-dependent f
  with massive neutrinos, and the Wang–Steinhardt α quoted there.
- Bernardeau et al. 2002, arXiv:astro-ph/0112551 (review): Sect. 2.7 for
  second-order growth.
- Planck Collaboration 2018, arXiv:1807.06209 (results): Eq. 27, the
  velocity–density fσ8 (L2).

## Not verified
<!-- key: not-verified -->

- The Heath (1977) integral solution D ∝ H ∫ da/(aH)³ for ΛCDM: cited by
  Linder in his reference list but not on arXiv and not read.
- Wang & Steinhardt 1998 itself (arXiv:astro-ph/9804015) for α_0 and α_1: read
  only as quoted by Kiakotou et al.
- The k-dependence of the velocity–density fσ8 for the cb field, and the
  sizes of the cb-against-total gaps in σ8 and f: not read in a paper. The
  CAMB and ODE checks that stood here before 2026-10-23 were agent
  computations and are set aside in
  `docs/history/set-aside/2026-10-23/cosmo-theory-foundations-linear-growth.md`.
- The error of f = Ω_m(z)^γ on f itself (Linder states it on g).
- Table II of arXiv:0709.0253 (A, B, C as functions of k): not read.
- Huterer Sect. 4.1 (parametrised growth constraints) was not read; measured
  γ values belong to `cosmo-dark-energy-modified-gravity`.
