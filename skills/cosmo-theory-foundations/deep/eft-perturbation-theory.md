# Perturbation theory and EFTofLSS: kernels, loops, renormalisation — cosmo-theory-foundations dossier

Scope: how the one-loop matter spectrum is derived (equations of motion,
F_n and G_n kernels, P22 and P13), why standard perturbation theory (SPT) is
UV-sensitive and how the EFT counterterm is fixed by renormalisation, what
the Einstein–de Sitter (EdS) time-dependence approximation costs in ΛCDM,
how the Lagrangian form differs from the Eulerian one, and what two loops
add, for a reader who must implement or check a one-loop code.
Snapshot: 2026-10-18.
From: Ivanov 2026 lecture notes (arXiv:2607.28314), Chs. 3, 4 and 7; DESI DR1
full-shape key paper (arXiv:2411.12021), Sect. 4.3. L3 dossier exists in a
sibling: cosmo-galaxy-clustering/deep/full-shape-modelling.md.

Already in L2 or in the sibling, not repeated here: the galaxy one-loop
model of Ivanov et al. 2020 (Eqs. 3.1–3.10, A.1–A.12), its counterterms and
their link to fingers of God, IR resummation (Eqs. A.4–A.9), the AP mapping,
bias bases and their conversions, the validity ranges per code
(`physics-and-methods.md#perturbation-theory-and-eftoflss-ingredients`,
`physics-and-methods.md#bias-expansions`,
`results.md#perturbation-theory-and-eftoflss-validity-ranges`); the DESI
pipelines, priors, analytic marginalisation and code comparison
(`cosmo-galaxy-clustering/deep/full-shape-modelling.md`); EdS against
neutrino kernels (`cosmo-neutrinos-dark-matter/deep/neutrino-mass-full-shape.md`)
and against modified-gravity kernels
(`cosmo-dark-energy-modified-gravity/deep/nonlinear-beyond-lcdm.md`).

Notation: δ density contrast, θ ≡ ∇·v velocity divergence, ℋ = aH the
conformal Hubble rate, τ conformal time, D_1 (or D) the linear growth factor,
f ≡ d ln D_1/d ln a, P_L the linear spectrum, k_12 ≡ k_1 + k_2.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Write the fluid equations in Fourier space, with a stated convention
<!-- key: step-1-write-the-fluid-equations-in-fourier -->

Bernardeau et al. 2002 (arXiv:astro-ph/0112551) [src: Sect. 2.4.1, Eqs. 36–39]
use Ã(k) = ∫ d³x/(2π)³ exp(−ik·x) A(x) (Eq. 36) and write

∂δ̃(k)/∂τ + θ̃(k) = −∫ d³k_1 d³k_2 δ_D(k − k_12) α(k_1, k_2) θ̃(k_1) δ̃(k_2)  (Eq. 37),

∂θ̃(k)/∂τ + ℋ θ̃(k) + (3/2) Ω_m ℋ² δ̃(k) = −∫ d³k_1 d³k_2 δ_D(k − k_12) β(k_1, k_2) θ̃(k_1) θ̃(k_2)  (Eq. 38),

α(k_1, k_2) ≡ k_12·k_1/k_1²,  β(k_1, k_2) ≡ k_12² (k_1·k_2)/(2 k_1² k_2²)  (Eq. 39),

α from the continuity equation, β from the Euler equation, Ω_m the
time-dependent matter fraction. With that transform the review defines
⟨δ(k)δ(k')⟩ = δ_D(k + k') P(k) and ξ(r) = ∫ d³k P(k) e^(ik·r) (Eqs. 116,
119–120), and states that the other "popular choice" puts the (2π)³ in
⟨δδ⟩ = (2π)³ δ_D P [src: Sect. 3.2.2]. The review's P is therefore
(2π)⁻³ times the P of CLASS-PT, velocileptors and Ivanov et al. (L2), and
its loop integrals ∫ d³q become ∫ d³q/(2π)³ in that convention [der].
The sign of its exponent is also opposite to Hamilton's (L2 §7).

### Step 2. Solve order by order in EdS: F_n and G_n
<!-- key: step-2-solve-order-by-order-in-eds-fn-and-gn -->

In EdS, a ∝ τ², ℋ = 2/τ, and the growing-mode expansion
δ̃(k, τ) = Σ_n a^n(τ) δ_n(k), θ̃(k, τ) = −ℋ(τ) Σ_n a^n(τ) θ_n(k) [src: Eq. 40]
has time-independent coefficients:
δ_n(k) = ∫ d³q_1 … d³q_n δ_D(k − q_1…n) F_n(q_1, …, q_n) δ_1(q_1) … δ_1(q_n)
(Eq. 41), and the same with G_n for θ_n (Eq. 42). The recursion (n ≥ 2,
k_1 = q_1 + … + q_m, k_2 = q_(m+1) + … + q_n, F_1 = G_1 = 1) is [src: Eqs. 43–44]

F_n = Σ_(m=1)^(n−1) G_m(q_1…q_m)/[(2n+3)(n−1)] × [(2n+1) α(k_1, k_2) F_(n−m)(q_(m+1)…q_n) + 2 β(k_1, k_2) G_(n−m)(q_(m+1)…q_n)],

G_n = Σ_(m=1)^(n−1) G_m(q_1…q_m)/[(2n+3)(n−1)] × [3 α(k_1, k_2) F_(n−m) + 2n β(k_1, k_2) G_(n−m)],

giving [src: Eqs. 45–46]

F_2(q_1, q_2) = 5/7 + (1/2)(q_1·q_2/(q_1 q_2))(q_1/q_2 + q_2/q_1) + (2/7)(q_1·q_2)²/(q_1² q_2²),

G_2(q_1, q_2) = 3/7 + (1/2)(q_1·q_2/(q_1 q_2))(q_1/q_2 + q_2/q_1) + (4/7)(q_1·q_2)²/(q_1² q_2²).

F_3 and F_4 are not written in the review ("given in [270]"). Properties of
the symmetrised kernels F_n^(s) that a code can test [src: Sect. 2.4.2]:

1. F_n^(s) ∝ k² as k = Σq_i → 0 with the q_i finite (momentum conservation).
2. F_n^(s)(q_1, …, q_(n−2), p, −p) ∝ k²/p² for p ≫ q_i (Eq. 47).
3. An IR divergence q_i/q_i² when one argument goes to zero, from α and β.

Spherically averaged vertices ν_n ≡ n! ∫ dΩ_1/4π … F_n and μ_n (same with
G_n) (Eqs. 48–49) obey a recursion with ᾱ = 1, β̄ = 1/3 (Eqs. 50–51), and
are pure numbers, printed as ν_2 = 34/21, ν_3 = 682/189, μ_2 = −26/21, μ_3 = 142/63
[src: Eq. 52, HTML rendering]; they reproduce spherical collapse (Eqs. 53–54).
Evaluating Eqs. 50–51 exactly gives ν_2 = 34/21, ν_3 = 682/189, μ_3 = 142/63
and μ_2 = +26/21 [der: rational arithmetic on the printed recursion]. The
sign of the printed μ_2 may follow from the sign convention for the velocity
divergence rather than be a slip; this was not resolved at source: check the
convention of the code or paper you compare with before using either sign.

### Step 3. Decide the time dependence outside EdS
<!-- key: step-3-decide-the-time-dependence-outside-eds -->

For general Ω_m, Ω_Λ the solutions are "non-separable functions of τ and k"
[src: Sect. 2.4.3]. Writing δ = Σ D_n(τ) δ_n, θ = −ℋ f Σ E_n(τ) θ_n
(Eqs. 63–64), the n-th order equations (Eqs. 65–66) contain the factor
3Ω_m/(2f²); "if f(Ω_m, Ω_Λ) = Ω_m^(1/2), then the system of equations becomes
indeed separable, with D_n = E_n = (D_1)^n", and the recursion is the EdS one
[src: Sect. 2.4.4]. This is the "EdS approximation" of every production
code: EdS kernels with the true D_1 and f. The review's justification:
for Ω_Λ = 0 the exact second-order growth is
D_2/D_1² = 1 + (3/17)(Ω_m^(−2/63) − 1), "extremely insensitive to Ω_m"
[src: Sect. 2.4.4], and the cosmology dependence of ν_2 and ν_3 "is a few
percent effect at most" [src: Sect. 2.4.3, Eqs. 57–58].

The exact ΛCDM time dependence is an integral over the linear Green's
function G(a, ã). Carrasco, Hertzberg & Senatore 2012 (arXiv:1206.2926)
write P22 with the factors ∫_0^a0 dã ã² G(a0, ã) ℋ²(ã) D'(ã)² and
3ℋ0² Ω_m ∫_0^a0 dã G(a0, ã) D(ã)²/ã in place of the EdS numbers
[src: Eq. 55], and P13 through six functions 𝒟_1…𝒟_6 of App. B
[src: Eq. 56]. Their App. C approximation to the time dependence gives
results "close to these ones, at percent level", but "it is potentially
dangerous to trust this approximation at high k's for percent level
precision" [src: Sect. 5].

### Step 4. Assemble the one-loop SPT spectrum
<!-- key: step-4-assemble-the-one-loop-spt-spectrum -->

[src: arXiv:astro-ph/0112551, Sect. 4.2.2, Eqs. 162–166, review convention]

P(k, τ) = P^(0) + P^(1) + …, P^(0) = [D_1^(+)]² P_L(k) (Eqs. 162–163),

P^(1) = P_22 + P_13 (Eq. 164),

P_22(k, τ) ≡ 2 ∫ [F_2^(s)(k − q, q)]² P_L(abs(k − q), τ) P_L(q, τ) d³q (Eq. 165),

P_13(k, τ) ≡ 6 ∫ F_3^(s)(k, q, −q) P_L(k, τ) P_L(q, τ) d³q (Eq. 166).

P_22 is positive and is mode coupling (if P_L = 0 above k_c, P_22 vanishes
only above 2k_c); P_13 "is in general negative", proportional to P_L(k), and
is "the one-loop correction to the propagator" [src]. For scale-free
spectra P_L = A a² k^n with cut-offs ε and k_c [src: Table 5]:

| n | P_13/(πA²a⁴) | P_22/(πA²a⁴) |
|---|---|---|
| 1 | −(122/315) k³ k_c² | (18/49) k⁴ k_c |
| 0 | −(244/315) k² k_c | (29π²/196) k³ |
| −1 | (128/225) k − (4/3) k ln(k_c/ε) − (176/315) k ln(k/k_c) | (80/147) k + (4/3) k ln(k/ε) |
| −2 | 5π²/(28k) − 4/(3ε) | 75π²/(196k) + 4/(3ε) |

Two structural facts follow [src: Sect. 4.2.2]. IR divergences (n ≤ −1, the
1/ε terms) cancel between P_22 and P_13 because "a homogeneous flow cannot
affect equal-time correlation functions because of Galilean invariance".
UV divergences do not cancel: P_13 diverges for n ≥ −1 (P_22 for n ≥ 1),
so "one-loop corrections to the power spectrum are meaningless at face
value" for such spectra. For CDM spectra the integrals converge, but the
UV region still contributes a k² P_L term from scales where SPT does not
apply; this is what the EFT counterterm absorbs (Step 5).

### Step 5. Renormalise: the EFT counterterm
<!-- key: step-5-renormalise-the-eft-counterterm -->

Carrasco, Hertzberg & Senatore 2012 smooth the fields on a scale Λ⁻¹ and
compute [src: arXiv:1206.2926, Sect. 3.2.2, Eqs. 53–57]

⟨δ_l(k) δ_l(q)⟩ = (2π)³ δ³(k + q) [P_11 + P_22 + P_13 + P_13,c²_comb]  (Eq. 53),

P_13,c²_comb(k, a0) = −2 (k²/D(a0)) ∫_0^a0 dã G(a0, ã) c²_comb(ã) D(ã) P_11,l(k, Λ)  (Eq. 57),

where c²_comb is "the combination of c_s², c_bv² and c_sv²" (sound speed,
bulk and shear viscosity) relevant at one loop, written with c the speed of
light [src: Sect. 1]. The logic [src: Sect. 3.2.3]:

1. P_13 and P_22 depend on Λ through the smoothed spectrum; "the Λ
   dependence of P_13 is to be cancelled by P_13,c²_comb, while the one of
   P_22 from the stochastic fluctuations". The stochastic counterterm counts
   as order δ_l⁵ and is dropped at this order.
2. P_13,c² goes as k², so the k → 0 limit of P_13 must too, "as can be
   readily verified".
3. Split c²_comb(a, Λ) = c²_comb;ren.(a, k_ren.) + c²_comb;ctr.(a, Λ)
   (Eq. 58): the counterterm part cancels the cutoff dependence; the
   renormalised part "is determined by matching to simulations or to
   observations at a specific k = k_ren.".
4. The time dependence of the counterterm is taken from the k → 0 limit of
   P_13 (Eqs. 59–61), with the approximation that the renormalised and
   counterterm parts share it ("we will check this approximation in a
   forthcoming paper").

Result: matching at k_ren. = 0.16 h/Mpc and extrapolating Λ → ∞ gives
c²_comb(a0, Λ = ∞) ≃ 6.2 × 10⁻⁷, against a naive virialisation estimate of
order 10⁻⁵; the one-loop EFT "agrees at percent level with the CAMB non-linear
fit up to k ≃ 0.24 h/Mpc" for Ω_m = 0.25, Ω_b = 0.04, h = 0.7, n_s = 1
[src: Sect. 5]. Matching at k = 0.1 and 0.18 h/Mpc brackets the value
("the dependence on the renormalization scale is a measure of the importance
of higher loops"), and the value is confirmed by measuring the stress tensor
directly in N-body runs at Λ = 1/3 and 1/6 h/Mpc [src: Sect. 3.2.3, Fig. 3].
c²_comb > 0 "tends to slow down the collapse of structures" and grows with
time until a ≃ 0.7 [src: Fig. 2]. The galaxy-survey form −2c_ℓ² k² P_lin of
Ivanov et al. (L2) is Eq. 57 with the time integral absorbed into a free
coefficient per redshift bin and multipole [der].

### Step 6. Or work in Lagrangian space
<!-- key: step-6-or-work-in-lagrangian-space -->

Chen et al. 2021 (arXiv:2012.04636) [src: Sects. 2–3]: x(q, t) = q + Ψ(q, t);
1 + δ_m(x) = ∫ d³q δ_D(x − q − Ψ(q)) (Eq. 1); linear solution
Ψ^(1) = −D(z) ∇_q⁻¹ δ_0(q), the Zel'dovich approximation; tracers as
1 + δ_g(x) = ∫ d³q F(q) δ_D(x − q − Ψ) with a local bias functional F of the
initial field (Eq. 2). In EdS the redshift-space displacement at order n is
Ψ^(s,(n)) = Ψ^(n) + n f (n̂·Ψ^(n)) n̂ ≡ R^(n) Ψ^(n), R^(n)_ij = δ_ij + n f n̂_i n̂_j
(Eq. 3), so each order transforms with its own n: A^(s,(13))_ij =
R^(1)_in R^(3)_im A^(13)_nm but A^(s,(22))_ij = R^(2)_in R^(2)_im A^(22)_nm
[src: Sect. 3], A_ij ≡ ⟨Δ_iΔ_j⟩_c the pairwise-displacement cumulant
(Eq. 5). The spectrum is P(k) = ∫ d³q e^(ik·q) ⟨e^(ik·Δ) F(q_1) F(q_2)⟩, with
ln⟨e^(ik·Δ)⟩ = −(1/2) k_i k_j A_ij − (i/6) k_i k_j k_k W_ijk + … [src: Sect. 3].
The one-loop redshift-space result (Eq. 4) keeps exp(−(1/2) k_i k_j A^(s,<)_ij)
of the long-wavelength linear displacements unexpanded and ends with
k²(α_0 + α_2 μ² + α_4 μ⁴ + α_6 μ⁶) P_s,Zel(k) + R_h³(1 + σ_2 k²μ² + σ_4 k⁴μ⁴),
the counterterms α_n multiplying the Zel'dovich spectrum and the stochastic
terms σ_n with R_h "the typical scale of halo/galaxy formation" [src: Eq. 4].
Keeping that exponential is the IR resummation: large-scale displacements
damp the BAO and "must be manually resummed in order-by-order expansions
such as Eulerian perturbation theory (EPT)" [src: Sect. 3]. The paper itself
works in EdS and the distant-observer limit [src: Sect. 2].

### Step 7. Go to two loops only if the extra parameters are affordable
<!-- key: step-7-go-to-two-loops-only-if-the-extra -->

Philcox 2026 (arXiv:2610.13867) [src: abstract]: a complete two-loop
redshift-space galaxy model has "a total of 49 free coefficients"
(fifth-order bias, counterterms, stochasticity); k_max rises "from
0.2 h/Mpc to 0.34 h/Mpc for a luminous red galaxy sample at z = 0.5", but
"constraints on σ8 are not significantly enhanced", because much of the
information "is absorbed by the numerous fifth-order biases and
counterterms".

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### EdS kernels or exact time dependence
<!-- key: eds-kernels-or-exact-time-dependence -->

| Comparison | Size | Source |
|---|---|---|
| Third-order coefficients λ_3^(l) (density) and κ_3^(l) (velocity), ΛCDM against EdS | "around 1% and 4%" at late times | Choustikov, Vlah & Challinor 2023, arXiv:2305.09337 [src: Sect. II.2, Fig. 2] |
| Cosmology dependence of ν_2, ν_3 | "a few percent effect at most" | arXiv:astro-ph/0112551 [src: Sect. 2.4.3] |
| D_2/D_1² for Ω_Λ = 0 | 1 + (3/17)(Ω_m^(−2/63) − 1) | arXiv:astro-ph/0112551 [src: Sect. 2.4.4] |
| Approximate against exact time dependence, one-loop EFT matter P(k) | percent level; unsafe "at high k's for percent level precision" | arXiv:1206.2926 [src: Sect. 5] |
| Exact (gauge-transformed) against standard EdS method with ν, real-space one loop | below 0.7% for M_ν < 0.30 eV | Fidler et al. 2026, arXiv:2605.05114 [src: abstract] |
| Same, one-loop quadrupole | 1.7% at k = 0.3 h/Mpc, z = 0, "with the largest contribution coming from the effect of the cosmological constant on the growth of the velocity field" | arXiv:2605.05114 [src: abstract] |

What exactness costs: Choustikov et al. present a Chebyshev spectral method
"orders of magnitude more efficient than direct numerical solvers", N = 2
components already reproducing λ_3^(1) to better than 0.03% [src: abstract,
Sect. IV.1]; Fidler et al. state that their gauge method "does not incur any
additional computational cost" [src: abstract]. The velocity kernels are the
ones that depart most, so the quadrupole (and any velocity statistic) is
where EdS is weakest; a 4% shift of a third-order velocity coefficient is
not a 4% shift of P_2, and the 1.7% figure is the one measured on the
spectrum.

### Eulerian or Lagrangian
<!-- key: eulerian-or-lagrangian -->

EPT expands everything, then resums the IR by hand (wiggle/no-wiggle split,
L2); LPT exponentiates the linear long-wavelength displacements, so the BAO
damping is built in, and its counterterms multiply P_Zel rather than P_lin
(L2: a two-loop-order difference). Before IR resummation the DESI codes are
"essentially equivalent" (sibling full-shape dossier). In redshift space the
LPT bookkeeping is heavier because each perturbative order transforms with
R^(n) (Step 6).

### Renormalisation scale, cutoff and matching
<!-- key: renormalisation-scale-cutoff-and-matching -->

For matter, c²_comb is matched at k_ren. and Λ → ∞ is taken "to drive to zero
any effect from higher derivative terms down by powers of k/Λ"; at finite Λ
it must be run with Eq. 62, and only "as k_ext → 0" is the extracted value
independent of the external momentum [src: arXiv:1206.2926, Sect. 3.2.3,
Fig. 4]. For galaxies the coefficient is free and fitted, so the matching
choice becomes a prior choice (sibling dossier, Step 3).

### One loop or two
<!-- key: one-loop-or-two -->

One loop: 7–10 nuisance parameters per sample (L2). Two loops: 49
coefficients, wider k range, no σ8 gain on the sample tested
(arXiv:2610.13867).

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| EdS vertices | ν_2 = 34/21, ν_3 = 682/189, μ_2 = −26/21 as printed (+26/21 from the recursion, sign convention unresolved), μ_3 = 142/63 | EdS | arXiv:astro-ph/0112551 | Eq. 52; μ_2 sign [der] from Eqs. 50–51 |
| c²_comb(a0, Λ = ∞) | ≃ 6.2 × 10⁻⁷; naive estimate 10⁻⁵ | Ω_m = 0.25, matched at 0.16 h/Mpc | arXiv:1206.2926 | Sect. 5 |
| c²_comb peak in time | a ≃ 0.7 | same | arXiv:1206.2926 | Fig. 2 caption |
| One-loop EFT matter, percent agreement | k ≃ 0.24 h/Mpc, z = 0 | against CAMB non-linear fit | arXiv:1206.2926 | Sect. 5 |
| One-loop SPT critical index | n_c ≈ −1.4 (one-loop correction vanishes) | scale-free | arXiv:astro-ph/0112551 | Sect. 4.2.2 |
| EdS error, third-order kernels | 1% (density), 4% (velocity) | ΛCDM | arXiv:2305.09337 | Sect. II.2 |
| EdS error, one-loop P | < 0.7% (real space), 1.7% (quadrupole, k = 0.3 h/Mpc, z = 0) | M_ν < 0.30 eV | arXiv:2605.05114 | abstract |
| Two-loop galaxy model | 49 coefficients; k_max 0.2 → 0.34 h/Mpc | LRG, z = 0.5 | arXiv:2610.13867 | abstract |

## What goes wrong
<!-- key: what-goes-wrong -->

- **(2π)³ convention mixed between kernel source and code.** Loop terms off by
  (2π)³ relative to P_11. Test: in a scale-free run, reproduce Table 5 of
  Bernardeau et al. in their convention, or the k → 0 behaviour of P_22
  (∝ k⁴ for n = 1) in yours.
- **Unsymmetrised kernels.** Eqs. 165–166 use F_n^(s). Test: F_2(q, −q) = 5/7 − 1 + 2/7 = 0
  [der: Eq. 45] and F_n^(s) ∝ k² as k → 0 (property 1).
- **IR cancellation broken numerically.** P_22 and P_13 computed on different
  grids or with different low-q cut-offs leave a spurious 1/ε residual
  (Table 5, n = −2). Test: vary the IR cut-off; the sum must not move.
- **UV sensitivity mistaken for physics.** P_13 depends on the UV end of
  P_L; without a counterterm, its value at k ~ 0.2 h/Mpc carries scales
  where SPT does not apply. Test: vary the UV cut-off Λ; only P_13 + counterterm
  may be cutoff-independent (arXiv:1206.2926, Sect. 3.2.3).
- **Counterterm amplitude read as a measured property.** c² is matched, and
  the renormalisation-scale dependence (k_ren. = 0.1 against 0.18 h/Mpc) is
  "a measure of the importance of higher loops".
- **EdS velocity kernels in a precision RSD fit.** The quadrupole error
  reaches 1.7% at k = 0.3 h/Mpc, z = 0 (arXiv:2605.05114). Test: rerun with
  exact time dependence (spectral or gauge method) at the highest k_max.
- **Copied vertex values.** Reproduce ν_n, μ_n from Eqs. 50–51 rather than
  copying Eq. 52: its printed μ_2 differs in sign from what Eqs. 50–51
  give, and the convention behind the difference was not resolved (Step 2).

## Reading list
<!-- key: reading-list -->

- Bernardeau et al. 2002, arXiv:astro-ph/0112551 (review): Sects. 2.4.1–2.4.4
  for the equations, kernels and the EdS separability condition; Sect. 4.2.2
  for P22, P13, the scale-free table and the IR and UV structure.
- Carrasco, Hertzberg & Senatore 2012, arXiv:1206.2926 (foundation):
  Sects. 3.2.2–3.2.3 for the counterterm diagram, renormalisation and running;
  Sect. 5 for the matter comparison.
- Baumann et al. 2012, arXiv:1004.2488 (foundation): the effective-fluid
  construction (L2; not re-read here).
- Chen et al. 2021, arXiv:2012.04636 (method): Sects. 2–3 for the Lagrangian
  redshift-space spectrum and its counterterms.
- Choustikov, Vlah & Challinor 2023, arXiv:2305.09337 (method): size of the
  EdS error on kernels, and a fast exact solver.
- Fidler et al. 2026, arXiv:2605.05114 (method): exact time dependence and
  linear GR corrections through Newtonian-motion gauges; error sizes.
- Philcox 2026, arXiv:2610.13867 (method): the two-loop redshift-space galaxy
  model and its parameter count.
- Ivanov et al. 2020, arXiv:1909.05277 (application): the galaxy one-loop
  model used in BOSS fits (L2).

## Not verified
<!-- key: not-verified -->

- F_3 explicitly and the UV (k → 0) coefficient of P_13 in units of σ_v²:
  the review defers F_3 to its reference [270]; Carrasco et al. give P_13
  through App. B functions not read.
- The units in which c²_comb ≃ 6.2 × 10⁻⁷ is quoted (the introduction
  writes it with c, the speed of light), and its conversion to the
  c_0² in (Mpc/h)² of galaxy fits.
- Fidler et al. and Philcox were read in abstract only; method sections,
  validation simulations and the two-loop priors were not read.
- The size of the EdS error on the galaxy (biased) one-loop multipoles in
  ΛCDM without neutrinos, separately from the matter case.
