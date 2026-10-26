# Set aside from cosmo-theory-foundations/deep/linear-growth.md

Numbers run of 2026-10-23 (plan of 2026-10-23, steps 1 and 3; owner's rule: no number computed by an agent). The blocks below held agent-computed values: checks run with CAMB 2.0.4 and with a direct ODE solution of the growth equation ([der: CAMB], [der: ODE]), and values the agent evaluated from closed-form formulae ([der]). They are copied verbatim from the file as it stood at commit 2b5e381 before removal; line numbers are those of that version.

## Lines 23-27

Checks flagged [der: CAMB] were run this session with CAMB 2.0.4
(H0 = 67.36, ω_b = 0.02237, ω_c = 0.1200, A_s = 2.1 × 10⁻⁹, n_s = 0.965,
N_eff = 3.044) against a direct numerical solution of the growth equation
(scipy `solve_ivp`, relative tolerance 10⁻¹⁰), flat background with
Ω_m = 0.3138 unless stated. They are derivations, not published accuracies.

## Lines 56-68


and Eqs. 10–11 (L2). "All these forms are equivalent" [src], but as printed
Eq. 10 carries G on the Ω_w term, (3/2)[1 − w(a)] G Ω_w(a) g. Substituting
(ln Ω_m)' = 3wΩ_w (flat, matter + w) into Eq. 11 gives the g coefficient
(3/2)(1 − G) + (3/2)(G − w)Ω_w, which equals Eq. 10's only for G = 1 [der].
For a modified-gravity G, integrate Eq. 8, 9 or 11, not Eq. 10.

Huterer writes the same equation for the suppression factor relative to
EdS: 2 d²g/d(ln a)² + [5 − 3w(a)Ω_DE(a)] dg/d ln a + 3[1 − w(a)]Ω_DE(a) g = 0
[src: arXiv:2212.05003, Eq. 10], equal to Linder's Eq. 10 with G = 1 [der].

For the growth rate itself, Linder & Cahn 2007 use G ≡ d ln(δ/a)/d ln a,
so f = 1 + G [der], and [src: arXiv:astro-ph/0701317, Eq. 3]

## Lines 83-106

The matter-era growing mode is δ ∝ a (Step 1), so a code starts at a_ini in
matter domination with D = a, dD/d ln a = a. Two normalisations then
coexist:

| Name | Definition | Source |
|---|---|---|
| D, normalised today | D(a) = δ(a)/δ(1), D(1) = 1 | arXiv:2212.05003, Eq. 9 [src] |
| g, suppression relative to EdS | D(a) ≡ a g(a)/g(1); g = 1 in EdS; g(z = 0) ≃ 0.78 for Ω_M = 0.3 | arXiv:2212.05003, Eq. 11 and Sect. 2.3 [src] |

At Ω_m = 0.3138, g(z = 0) = 0.787 [der: ODE]. Using a D normalised to a at
early times where D(1) = 1 is expected rescales σ8(z) by that factor, a 21%
error [der].

What the initial condition and radiation cost, against CAMB with massless
neutrinos [der: CAMB]:

| Quantity | CAMB | ODE, matter + Λ, D = a at a = 10⁻⁴ | ODE with radiation in H, D = a at a = 10⁻³ |
|---|---|---|---|
| D(z = 2)/D(0) | 0.41759 (from σ8(z)/σ8(0)) | 0.41748 (−0.03%) | 0.41758 (−0.002%) |
| f(z = 0) | 0.52593 (from fσ8/σ8) | 0.52594 | 0.52592 |
| f(z = 0.5) | 0.75995 | 0.76006 | 0.75993 |

The radiation term matters at the 10⁻⁴ level on D at z ≲ 2; Ω_r h² ≈ 4.15 ×
10⁻⁵ was assumed for this test [der, value assumed, not read].

## Lines 108-149

### Step 4. Use the growth index only where its error on f is known
<!-- key: step-4-use-the-growth-index-only-where-its -->

Linder's accuracy figures are for the growth factor g (L2). On f itself
the error is larger at z = 0 [der: ODE, Ω_m = 0.3138, f = Ω_m(z)^γ]:

| Model | γ | z = 0 | z = 0.5 | z = 1 | z = 2 |
|---|---|---|---|---|---|
| ΛCDM | 0.55 | +0.51% | −0.04% | −0.07% | −0.03% |
| w = −0.8 | 0.55 | +1.34% | +0.38% | +0.14% | +0.03% |
| w = −0.8 | 0.56 (Linder Eq. 17) | +0.17% | −0.22% | −0.21% | −0.11% |
| w0 = −0.75, wa = −0.8 | 0.55 | +0.85% | −0.17% | −0.19% | −0.07% |
| w0 = −0.75, wa = −0.8 | 0.547 (Linder Eq. 18, w(z = 1) = −1.15) | +1.21% | −0.01% | −0.12% | −0.05% |

The effective index of exact ΛCDM growth today is ln f/ln Ω_m = 0.554 [der],
so γ = 0.55 overpredicts f(0) by 0.5%. An fσ8 model accurate to 0.1% must
solve the equation.

Closed forms for γ, all derived under near-matter domination:

- Linder & Cahn: γ ≈ 3(1 − w_∞)/(5 − 6w_∞) − B x a^x/[(5 − 6w_∞)(5 − 6w_∞ + 2x)]
  [src: Eq. 18], w_∞ the early-time equation of state, Ω_w ∝ a^(−3w_∞)(1 + B a^x)
  (Eq. 17); for w0wa, B = 3wa, x = 1, and the correction coefficient is
  −(3/143) wa, "generally ≲ 0.01" [src: Sect. III]. For w_∞ = −1 the leading
  term is 6/11 = 0.545 [der].
- Wang & Steinhardt, as quoted by Kiakotou, Elgarøy & Lahav 2008: f = Ω_m^α(z),
  α = α_0 + α_1[1 − Ω_m(z)], α_0 = 3/[5 − w/(1 − w)],
  α_1 = (3/125)(1 − w)(1 − 3w/2)/(1 − 6w/5)³ for constant w [src:
  arXiv:0709.0253, Eqs. 13–15]; for w = −1, α_0 = 6/11 and α_1 = 0.0113, so
  α(z = 0) ≈ 0.553 at Ω_m = 0.31 [der].
- Stability of the definition: with G = Ω_m^γ − 1, γ "varies from its present
  value by less than 2% back to a ≪ 1 and 6% forward to a = 5" for Λ; the two
  alternative definitions −G/Ω_w and G/ln Ω_m do not stay constant [src:
  arXiv:astro-ph/0701317, Sect. III, Eq. 16].
- A non-clustering fraction Ω_e of matter-like density (early dark energy, and
  by the same equation massive neutrinos below their free-streaming scale)
  gives g ∝ a^((−5 + sqrt(25 − 24Ω_e))/4) ≈ a^(−(3/5)Ω_e), i.e. γ = 3/5, and
  γ ≈ 3/5 + (3/125)Ω_e at next order [src: Eq. 19].
- DGP: γ_∞,DGP = 11/16 = 0.6875 [src: Eq. 26]; numerically 0.665 today for
  Ω_m = 0.28, and "the single parameter γ = 0.68 is an excellent approximation
  for growth at any time through the present, holding constant to 2%"
  [src: Sect. IV.2].

## Lines 151-188

### Step 5. Know which "fσ8" the code returns
<!-- key: step-5-know-which-fsigma8-the-code-returns -->

CAMB 2.0.4's `get_fsigma8` docstring: "For general models fσ8 is defined as
in the Planck 2015 parameter paper in terms of the velocity-density
correlation: σ²_vd/σ_dd for 8 h⁻¹Mpc spheres" [src: CAMB 2.0.4 source,
`camb/results.py`]; `get_sigmaR` takes `var1`, `var2` (default `delta_tot`)
and R in h⁻¹Mpc or Mpc [src: same]. With massive neutrinos the three
quantities that are called fσ8 or σ8 separate [der: CAMB, ω_c fixed,
z = 0 unless stated]:

| Σm_ν, states | σ8^cb/σ8^tot − 1 | CAMB fσ8 (vd) / [f_ODE σ8^tot] − 1 |
|---|---|---|
| 0.06 eV, one massive | +0.43% (z = 0), +0.44% (z = 2) | +0.16% (z = 0), +0.13% (z = 2) |
| 0.3 eV, three degenerate | +1.99% (z = 0), +2.11% (z = 2) | +0.73% (z = 0), +0.79% (z = 2) |

f_ODE is the scale-independent solution for the total Ω_m. The 0.43% is the
Boltzmann-code value of the cb-against-total σ8 gap that L2 estimated as
"about f_ν, 0.45%" (`results.md#neutrino-effects-on-sigma8-growth-and-the-power`).

Scale dependence of f itself, z = 0.5, finite differences of d ln δ/d ln a
on CAMB linear spectra, relative to a massless-neutrino run with the same
ω_c and ω_b (so Ω_m is not held fixed) [der: CAMB]:

| Σm_ν, states | field | k = 0.01 | 0.05 | 0.1 | 0.3 h/Mpc |
|---|---|---|---|---|---|
| 0.06 eV, one | cb | +0.03% | −0.09% | −0.11% | −0.13% |
| 0.3 eV, three | cb | +0.32% | −0.31% | −0.50% | −0.61% |
| 0.3 eV, three | total | +0.58% | +0.02% | −0.28% | −0.55% |

Without neutrinos f(k) is flat to 10⁻⁵ over the same range [der: CAMB]. A
fitting form for f(k) with neutrinos: f ≈ μ(k, f_ν, Ω_DE) Ω_m^α(z), μ = 1 −
A(k)Ω_DE f_ν + B(k) f_ν² − C(k) f_ν³, with A, B, C tabulated in the paper's
Table II; at 8 h⁻¹Mpc, f ≈ (1 − 0.8 Ω_DE f_ν + 3.9 f_ν² − 9.8 f_ν³) Ω_m^α(z),
valid for f_ν ≤ 0.15 [src: arXiv:0709.0253, Eqs. 16–18]; on small scales
μ = (1 − f_ν)^α_0 [src: Eq. 19]. The same paper's simplified neutrino growth
equation df/d ln a = −f² − [1/2 − (3/2) w(1 − Ω_m(z))] f + (3/2) Ω_m(z)(1 − f_ν)
[src: Eq. 12] differs from CAMB by "at most 7.5%" in ln δ [src: Sect. III.2].

## Lines 200-232

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Solve, or use Ω_m^γ
<!-- key: solve-or-use-omegam-gamma -->

Solving costs one ODE per cosmology. Ω_m^0.55 costs +0.5% on f(0) in ΛCDM
and 0.4–1.3% at z ≤ 0.5 for w = −0.8 or a DESI-like w0wa (Step 4). Linder's
w-dependent γ halves the z = 0 error for constant w but not for w0wa,
because a single w(z = 1) does not describe a crossing equation of state
[der from the table].

### Normalise to today or to the early universe
<!-- key: normalise-to-today-or-to-the-early-universe -->

D(1) = 1 is the convention of σ8(z) = σ8 D(z) (Huterer Eq. 9). Growth
suppression g is the convention of growth-index work. Mixing them is a
factor g(1) ≈ 0.79.

### Total-matter or cb growth
<!-- key: total-matter-or-cb-growth -->

DESI's template and bias use the cb field (L2). The cb growth rate at
0.06 eV is 0.1% below the massless value at 0.05–0.3 h/Mpc; at 0.3 eV
0.3–0.6% [der: CAMB]. For Stage-IV precision on fσ8 at the per-cent level
this is a modelling choice to state, not a negligible term.

### Which fσ8
<!-- key: which-fsigma8 -->

Planck and CAMB: σ²_vd/σ_dd for total matter; eBOSS: f = ∂ ln σ8/∂ ln a
(L2); a template fit: f × σ8 at the fiducial shape. With 0.06 eV they differ
by 0.1–0.2%, with 0.3 eV by 0.7–0.8% [der: CAMB].

## Lines 234-249

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Validity of the growth ODE | 0.001 ≲ k ≲ 0.1 h/Mpc | GR, adiabatic, linear | arXiv:2212.05003 | Sect. 2.1 |
| g(z = 0) | ≃ 0.78 (Ω_M = 0.3); 0.787 (Ω_m = 0.3138) | flat ΛCDM | arXiv:2212.05003; this session | Sect. 2.3; [der: ODE] |
| Neglecting G² in the quadrature | ∼0.2% on g | ΛCDM | arXiv:astro-ph/0701317 | Sect. II |
| Ω_m^0.55 error on f | +0.51% (z = 0), < 0.1% (z = 0.5–2) | ΛCDM, Ω_m = 0.3138 | this session | [der: ODE] |
| Effective γ today | 0.554 | same | this session | [der: ODE] |
| γ in DGP | 11/16 early; 0.665 today (Ω_m = 0.28); 0.68 to 2% | DGP | arXiv:astro-ph/0701317 | Eq. 26, Sect. IV.2 |
| Ω^0.6 instead of Ω^0.55 | "needless 6% error in β", bias 0.03 (11%) on Ω_m | concordance | arXiv:astro-ph/0701317 | Sect. III |
| D_2/D_1² | −(3/7) Ω_m^(−1/143), < 0.6% | flat Λ, 0.01 ≤ Ω_m ≤ 1 | arXiv:astro-ph/0112551 | Eq. 97 |
| σ8^cb/σ8^tot − 1 | 0.43% (0.06 eV, one state); 1.99% (0.3 eV, three) | z = 0 | this session | [der: CAMB] |
| f_cb(k) relative to massless | −0.1% (0.06 eV); −0.3 to −0.6% (0.3 eV), k = 0.05–0.3 h/Mpc | z = 0.5, ω_c fixed | this session | [der: CAMB] |
| Neutrino growth-rate fit | valid f_ν ≤ 0.15 | CMBFAST-calibrated | arXiv:0709.0253 | Eq. 18 |

## Lines 251-263

## What goes wrong
<!-- key: what-goes-wrong -->

- **Eq. 10 of Linder used with G ≠ 1.** Gives the wrong modified-gravity
  growth (Step 2). Test: the four forms must agree numerically for the G
  used.
- **Growth started in a decaying mode.** Initial dD/d ln a ≠ D at a_ini
  leaves a t⁻¹ mode (Huterer Eq. 6). Test: move a_ini by a factor 10;
  D(z)/D(0) must not change beyond 10⁻⁴.
- **Normalisation mixed.** σ8(z) off by g(1) ≈ 0.79. Test: D(0) = 1 and
  D(z) → a/g(1) at high z.
- **Ω_m^0.55 in a precision fσ8 model.** +0.5% at z = 0 in ΛCDM, more for
  w ≠ −1. Test: compare with the ODE at the lowest redshift fitted.

## Lines 286-299

## Not verified
<!-- key: not-verified -->

- The Heath (1977) integral solution D ∝ H ∫ da/(aH)³ for ΛCDM: cited by
  Linder (ref. 13) but not on arXiv and not read.
- Wang & Steinhardt 1998 itself (arXiv:astro-ph/9804015) for α_0 and α_1: read
  only as quoted by Kiakotou et al.
- The k-dependence of the CAMB velocity–density fσ8 for the cb field (CAMB
  computes it for `delta_tot` by default; a cb version was not run).
- Table II of arXiv:0709.0253 (A, B, C as functions of k): not read.
- Huterer Sect. 4.1 (parametrised growth constraints) was not read; measured
  γ values belong to `cosmo-dark-energy-modified-gravity`.
- The radiation density used in the Step 3 test (Ω_r h² ≈ 4.15 × 10⁻⁵) was
  assumed, not read; it affects only the 10⁻⁴-level comparison.
