# Halo model and non-linear matter prescriptions — cosmo-theory-foundations dossier

Scope: how the non-linear matter power spectrum is built from the halo model
and from the halofit and HMcode-2020 prescriptions (equations, fitted
parameters, filters, spherical-collapse inputs, massive neutrinos), how the
low-mass part of the two-halo integral is made to converge, which version a
code actually runs, and how to check a prescription against its calibration.
Snapshot: 2026-10-17.
From: Asgari 2023 halo-model review (arXiv:2303.08752), Sects. 2, 3 and 5;
DES Y3 (halofit, arXiv:2105.13548) and KiDS-Legacy (HMcode-2020,
arXiv:2503.19441) choices. Feedback in sibling dossier
cosmo-weak-lensing/deep/baryonic-feedback.md.

Already in L2, not repeated here: the general one- and two-halo terms,
the ingredients as the review writes them (σ(R), ν, Sheth–Tormen, NFW,
peak-background bias) in `physics-and-methods.md#halo-model`; the stated
accuracy of each prescription and the Mira-Titan comparison in
`results.md#transfer-function-and-non-linear-prescriptions` and
`systematics.md#non-linear-prescription-outside-its-calibration`. The known
limits of the halo model (large-scale one-halo term, transition region,
exclusion, concentration scatter) are in
`cosmo-galaxy-halo-connection/references/physics-and-methods.md`; the
HMcode-2020 feedback parameter T_AGN in
`cosmo-weak-lensing/deep/baryonic-feedback.md`.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. The matter halo model and its two normalisation conditions
<!-- key: step-1-the-matter-halo-model-and-its-two -->

For matter, W_m(M, k) = M U_m(M, k)/ρ̄ and the terms become
P^1h_mm = (1/ρ̄²) ∫ M² Û_m² n dM and
P^2h_mm = P^lin_mm [(1/ρ̄) ∫ M Û_m b n dM]², ignoring non-linear halo bias
[src: Asgari et al. 2023, arXiv:2303.08752, Eqs. 34–35]. The correct
large-scale limit needs both

∫₀^∞ M n(M) dM = ρ̄ [src: Eq. 32], ∫₀^∞ M b(M) n(M) dM = ρ̄ [src: Eq. 33]:

"all matter is contained in haloes" and matter is unbiased with respect to
itself. Achieving them numerically is "difficult" because standard mass
functions put much mass in low-mass haloes; "some popular mass function and
bias relations enforce these consistency relations while others do not"
[src: Sect. 2.3].

### Step 2. Make the two-halo integral converge at low mass
<!-- key: step-2-make-the-two-halo-integral-converge-at -->

Mead & Verde 2020 (arXiv:2011.08858, App. A) put all mass below the lower
limit M_min into haloes of exactly M_min [src: Eqs. 33–34]:

n(M) → n(M) Θ(M − M_min) + A(M_min) δ_D(M − M_min)/[b(M_min) M_min/ρ̄],
A(M_min) = 1 − (1/ρ̄) ∫_{M_min}^∞ M b(M) n(M) dM,

with A "between zero and unity, with ∼0.5 being typical for standard mass
functions and standard integration limits" [src]. The trick is valid because
linear halo bias tends to a constant at low mass and as long as the result
does not depend on the profiles of haloes below M_min; the one-halo term is
unaffected because its extra W keeps it dominated by high-mass haloes
[src]. With beyond-linear bias the same substitution splits the double
integral into four terms I^11, I^12, I^21, I^22 (Eqs. 35–39); moving M_min
from 10⁸ to 10⁶ or 10¹⁰ h⁻¹M_⊙ changes their results by ∼2%; 10¹⁶ h⁻¹M_⊙ is a
sensible upper limit for ΛCDM at z = 0 [src: App. A]. HMcode-2020 uses the
same procedure when a mass function violates the normalisation (its
footnote 6) [src: arXiv:2009.01858, Sect. 3.2].

### Step 3. halofit: two fitted terms in the halo-model spirit
<!-- key: step-3-halofit-two-fitted-terms-in-the-halo -->

Smith et al. 2003 (arXiv:astro-ph/0207664) write, with Δ²(k) = k³P/(2π²)
[src: App. C, Eqs. 69–76]:

Δ²_NL = Δ²_Q + Δ²_H;
Δ²_Q = Δ²_L [(1 + Δ²_L)^β_n/(1 + α_n Δ²_L)] exp[−f(y)], y ≡ k/k_σ,
f(y) = y/4 + y²/8;
Δ²_H = Δ'²_H/(1 + μ_n y⁻¹ + ν_n y⁻²),
Δ'²_H = a_n y^(3f1(Ω))/{1 + b_n y^(f2(Ω)) + [c_n f3(Ω) y]^(3−γ_n)};

with σ²(R_G) ≡ ∫ Δ²_L exp(−k²R_G²) d ln k (a **Gaussian** filter),
σ(k_σ⁻¹) ≡ 1, 3 + n_eff ≡ −d ln σ²/d ln R|_σ=1 and the curvature
C ≡ −d² ln σ²/d ln R²|_σ=1. The coefficients a_n … ν_n are polynomials in n
and C (Eqs. 77–84); f1,2,3 are powers of Ω, with separate open (Eq. 85) and
flat (Eq. 86) sets and linear interpolation in Λ suggested in between [src].
Why not the halo model itself: the quasi-linear term was made empirical
because quasi-linear effects "cannot be cleanly separated from the convolving
effects of halo profiles"; the original requires (1/ρ̄)∫ dM b n M = 1 for its
large-scale limit [src: Sect. 6.1, Eqs. 45–48]. Stated fit: rms 8.6% over its
simulations, < 3% against the J98 ΛCDM boxes for z < 3, k < 10 h/Mpc
[src: App. C].

Takahashi et al. 2012 (arXiv:1208.2701) keep the form and refit every
coefficient [src: App. A, Eqs. A1–A14]: e.g. log10 a_n = 1.5222 + 2.8553 n_eff
+ 2.3706 n_eff² + 0.9903 n_eff³ + 0.2250 n_eff⁴ − 0.6038 C + 0.1749 Ω_w(z)(1+w)
(Eq. A6), a w term also in b_n (Eq. A7), μ_n = 0 (Eq. A12), α_n taken in
absolute value "to avoid divergence" (Eq. A10), and the flat-case
f1,2,3(Ω_m) = Ω_m^(−0.0307), Ω_m^(−0.0585), Ω_m^(0.0743) at the redshift
considered (Eq. A14). The χ² of the fit weights k < 0.3 h/Mpc at z ≤ 3 by
10, 0.3–10 h/Mpc by 1, z > 3 by 0.2 and k ≥ 10 h/Mpc by 0.1, "so that the
final fitting formula gives a better accuracy at the BAO scales at low
redshifts"; the k-bin covariance is ignored and σ_i² = P²_sim [src: Sect. III,
Eq. 3].

### Step 4. HMcode-2020: the halo model with fitted modifications
<!-- key: step-4-hmcode-2020-the-halo-model-with-fitted -->

Mead et al. 2021 (arXiv:2009.01858) start from P^2H and P^1H with
W(M, k) = (1/ρ̄) ∫₀^r_v 4πr² [sin(kr)/(kr)] ρ(M, r) dr and M = (4/3)π r_v³
Δ_v(z) ρ̄ [src: Sect. 2, Eqs. 2–5], a **top-hat** filter T(x) =
(3/x³)(sin x − x cos x) in σ²_ij(R) = ∫ Δ²_lin,ij T²(kR) d ln k (Eqs. 8–9),
the displacement variance σ²_v = (1/3) ∫ Δ²_lin/k² T² d ln k (Eq. 10), and
n_eff evaluated at R_nl where σ(R_nl) = δ_c (Eq. 11) [src]. The model then
adds:

| Element | Equation as written | Eq. | Fitted value (Table 2) |
|---|---|---|---|
| De-wiggled linear spectrum | P_dwl = P^lin − (1 − e^(−k²σ²_v,mm))P_wig, P_wig from dividing by the Eisenstein–Hu no-wiggle form and smoothing in ln k with σ = 0.25 | 14–15 | no free parameter |
| Two-halo damping | P^2H = P_dwl[1 − f (k/k_d)^n_d/(1 + (k/k_d)^n_d)] | 16 | k_d = 0.05699 σ8,cc^(−1.089) h/Mpc; f = 0.2696 σ8,cc^(0.9403); n_d = 2.853 |
| One-halo large-scale damping | P^1H × (k/k_*)⁴/[1 + (k/k_*)⁴] | 17 | k_* = 0.05618 σ8,cc^(−1.013) h/Mpc |
| Sheth–Tormen mass function | F(ν)dν = A[1 + (qν²)^(−p)]e^(−qν²/2)dν, p = 0.3, q = 0.707, A ≃ 0.216 | 18 | not refitted |
| Halo bloating | ρ ∝ 1/{r/(ν^η r_s)[1 + r/(ν^η r_s)]²}, truncated at ν^η r_v | 19 | η = 0.1281 σ8,cc^(−0.3644) |
| Concentration | c = B[1 + z_f(M, z)]/(1 + z), g(z_f)σ_cc(γM, z)/g(z) = δ_c(z), γ = 0.01 | 20–21 | B = 5.196 |
| Dark-energy correction | c → c [g(z_c)/g_Λ(z_c)][g_Λ(z)/g(z)], z_c = 10 | 22 | — |
| Transition | Δ²_HM = [(Δ²_2H)^α + (Δ²_1H)^α]^(1/α) | 23 | α = 1.875 × 1.603^(n_eff,cc) |

[src: Sects. 4.1–4.5, 5.1, Table 2, whose caption counts "a total of 12
fitted parameters", i.e. the coefficients of these seven functions]. At z = 0 in ΛCDM (Ω_m = 0.3, σ8 = 0.8):
k_d = 0.073, k_* = 0.070 h/Mpc, f = 0.219, η = 0.139, α = 0.719 [src: Table 2].

Why each element, in the authors' words:
- The full two-halo integral was dropped (set to its k → 0 limit) because
  the halo-bias choice has "an insignificant effect" on matter power and
  de-wiggled linear theory reduces scatter near k ~ 0.1 h/Mpc; this also
  "approximately halv[es] the computational time" [src: Sect. 3.1].
- Eq. 17 respects the physical P_1H ∝ k⁴ limit from mass and momentum
  conservation; without it the one-halo term adds power at
  k ≲ 0.01 h/Mpc where linear theory is "near perfect" [src: Sect. 4.3].
- f = 0.22 is larger than the expected perturbative damping (≃ 10% at
  k = 0.1 h/Mpc); α < 1 adds the power back through the transition: the
  two parameters compensate each other [src: Sect. 5.3].
- η bloats a ν = 3 halo (∼10¹⁵ h⁻¹M_⊙ at z = 0) by ≃ 16%; earlier versions
  needed η ≃ 0.4 [src: Sect. 5.3].
- The Dolag-type factor g_Λ(z)/g(z) in Eq. 22 is new, needed for the high-z
  limit; the 1.5 exponent of HMcode-2016 was dropped [src: Sect. 4.4].
- Parameters are functions of σ8,cc(z) and n_eff,cc(z), not of h, Ω_m, w,
  because structure formation "is driven by the spectral shape and
  amplitude" [src: Sect. 5.1].

### Step 5. Spherical-collapse inputs and halo definition
<!-- key: step-5-spherical-collapse-inputs-and-halo -->

HMcode-2020 uses the virial definition, the Sheth–Tormen mass function and
the Mead 2017 fits [src: Sects. 3.2–3.3, App. A]:
δ_c/[1.686(1 − 0.041 f_ν)] = 1 + Σ_{i=1,2} f_i(g/a, G/a)[log10 Ω_m(a)]^α_i and
Δ_v/[177.7(1 + 0.763 f_ν)] = 1 + Σ_{i=3,4} f_i(g/a, G/a)[log10 Ω_m(a)]^α_i,
with f_i(x, y) = p_i,0 + p_i,1(1 − x) + p_i,2(1 − x)² + p_i,3(1 − y), g the
unnormalised growth (g = a early) and G = ∫₀^a g(ã)/ã dã [src: Eqs. 27–31,
Table 7]. For Ω_m = 0.3 ΛCDM, g(1) ≃ 0.779, G(1) ≃ 0.930, and Δ_v ≃ 308
against ≃ 337 from Bryan & Norman, because dark-energy "buoying" is not
included [src: App. A]. Choices compared [src: Sects. 3.2–3.4]:

- Mass function: Sheth–Tormen "slightly outperforms" Tinker 2008/2010 for
  the power spectrum although Tinker fits simulated mass functions better;
  Despali et al. is best for k < 1 h/Mpc and worse beyond; Press–Schechter
  is poor.
- Halo boundary: M_200c "far less accurate" than M_200 or M_vir.
- Concentration: Bullock et al. (cosmology-dependent) strongly reduces the
  scatter against Duffy et al. power laws; affects only k > 1 h/Mpc.
- δ_c choice matters little; Δ_v from Mead 2017 improves mean and scatter.

### Step 6. Massive neutrinos
<!-- key: step-6-massive-neutrinos -->

- HMcode-2020: σ_cc (cold matter) in ν = δ_c/σ_cc; the one-halo window
  lowered by (1 − f_ν), f_ν = Ω_ν/Ω_m, because "hot neutrinos cannot cluster
  in haloes"; neutrino mass counted in δ_c and Δ_v through Eqs. 27–28 with
  f_ν; all fitted dependences through σ8,cc and n_eff,cc [src: Sects. 2, 3.5,
  5.1]. Mean and variance are minimised with σ_cc and the (1 − f_ν) factor,
  "in agreement with" Massara et al. 2014 [src: Sect. 3.5].
- Concentration with scale-dependent growth: the large-scale growth "with
  neutrinos clustered along with CDM" is used in Eq. 21 [src: Sect. 4.4].
- halofit: three published versions. Takahashi refitted all parameters and
  added w; Bird et al. kept most of Smith et al. and added ν terms; the
  default in CAMB is an **unpublished** reconfiguration of Bird et al. on the
  Takahashi base, identical to Takahashi for m_ν = 0 [src: App. B]. On the
  26 massive-neutrino Mira-Titan nodes this CAMB version "performs worse,
  especially for high neutrino masses" than Takahashi without explicit ν
  dependence; the authors suspect differences in how simulations treat
  neutrinos (linear, semi-linear, particle) [src: App. B].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### halofit or HMcode-2020
<!-- key: halofit-or-hmcode-2020 -->

| | halofit (Takahashi) | HMcode-2020 |
|---|---|---|
| Structure | 2 fitted terms, coefficients polynomial in n_eff, C, with w terms | halo model + 7 fitted functions (12 fitted numbers), plus a separate baryon model |
| Filter for σ | Gaussian | top-hat |
| Calibration | 6 WMAP-like models fitted, 10 Coyote kept as check (L2) | 37 FrankenEmu nodes, k = 0.01–10 h/Mpc, z = 0, 0.5, 1, 2, equal log-k weight [src: Sect. 5.1] |
| Neutrinos | only via the unpublished CAMB variant | cold-field σ, (1 − f_ν) window, f_ν in δ_c, Δ_v |
| Baryons | none | built in (sibling dossier) |
| Other spectra | matter only | matter only [src: arXiv:2303.08752, Sect. 3.7] |

Both "cannot be used to predict any spectra other than that of matter", and
HMcode's "effective haloes" should not be taken physically; it is "not
obvious" its tweaks would work for other tracers [src: arXiv:2303.08752,
Sect. 3.7.2].

### Refit or correct halofit
<!-- key: refit-or-correct-halofit -->

Re-optimising the halofit coefficients against EuclidEmulator2 reduces the
RMS fractional error from 3% to below 2% for k = 9 × 10⁻³ – 9 h/Mpc;
syren-halofit adds a symbolic correction that reaches 1%, 2350 and 3170
times faster than halofit and HMcode implementations (Bartlett et al. 2024,
arXiv:2402.17492) [src: abstract]. The extension with massive neutrinos and
w0–wa reaches 1.3% RMS on the non-linear spectrum against EuclidEmulator2
(Sui et al. 2024, arXiv:2410.14623) [src: abstract]. Their reference is an
emulator, so their error adds to the emulator's own.

### Integrating the full halo model or the fitted model
<!-- key: integrating-the-full-halo-model-or-the-fitted -->

The pure halo model under-predicts power in the transition region (sibling
L2: beyond-linear bias boosts the two-halo term by ∼2 at k ~ 0.7 h/Mpc,
arXiv:2011.08858, abstract). HMcode instead absorbs the deficit into α, f and η
(above). A user who needs galaxies or other fields must use the full
model with its normalisation fix (Step 2), not HMcode.

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Low-mass correction amplitude | A(M_min) ∼ 0.5 typical | halo model | arXiv:2011.08858 | App. A, Eq. 34 |
| M_min sensitivity | ∼2% for 10⁶–10¹⁰ h⁻¹M_⊙ around 10⁸ | halo model with β^NL | arXiv:2011.08858 | App. A |
| halofit filter and scale | Gaussian, σ(k_σ⁻¹) = 1 | Smith 2003, Takahashi 2012 | arXiv:astro-ph/0207664; arXiv:1208.2701 | Eqs. 73–74; A4 |
| Original halofit fit | rms 8.6%; < 3% vs J98 ΛCDM, z < 3, k < 10 h/Mpc | Smith 2003 | arXiv:astro-ph/0207664 | App. C |
| Takahashi χ² weights | 10 (k < 0.3, z ≤ 3), 1, 0.2 (z > 3), 0.1 (k ≥ 10) | Takahashi 2012 | arXiv:1208.2701 | Eq. 3 |
| HMcode-2020 parameters at z = 0 | k_d 0.073, k_* 0.070 h/Mpc; f 0.219; n_d 2.85; η 0.139; B 5.20; α 0.719 | ΛCDM, σ8 = 0.8 | arXiv:2009.01858 | Table 2 |
| HMcode-2020 calibration set | 37 FrankenEmu nodes (≲ 1% at the nodes) | — | arXiv:2009.01858 | Sect. 5.1 |
| De-wiggling smoothing | σ = 0.25 in ln k; insensitive for 0.15–0.35 | HMcode-2020 | arXiv:2009.01858 | Sect. 4.1, footnote 7 |
| Δ_v, Ω_m = 0.3 ΛCDM | ≃ 308 (Mead 2017) vs ≃ 337 (Bryan & Norman) | — | arXiv:2009.01858 | App. A |
| Sheth–Tormen constants | p = 0.3, q = 0.707, A ≃ 0.216 | HMcode-2020 | arXiv:2009.01858 | Eq. 18 |
| syren-halofit | 3% → < 2% (refit) → 1% (corrected) RMS vs EuclidEmulator2 | ΛCDM | arXiv:2402.17492 | abstract |
| syren-new | 1.3% RMS non-linear, 0.3% linear, 0.1% σ8 | ν + w0wa | arXiv:2410.14623 | abstract |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Normalisation not enforced.** Mass functions such as Tinker 2008 and
  Despali do not satisfy the normalisation condition [src:
  arXiv:2009.01858, Sect. 3.2]; with a finite M_min the two-halo matter term
  then has the wrong large-scale limit. Test: compute A(M_min) (Eq. 34) and
  check P^2H/P^lin → 1 as k → 0.
- **Filter mixed between codes.** halofit's k_σ and n_eff use a Gaussian
  filter, HMcode's σ and n_eff a top-hat (Eq. 73 against Eq. 9): plugging one
  code's n_eff into the other's fitted forms is wrong [der from the
  definitions].
- **"halofit" ambiguous.** Smith, Takahashi, Bird, and the unpublished CAMB
  variant are four models; the CAMB default with massive neutrinos is the
  unpublished one and is worse than Takahashi for heavy neutrinos
  (arXiv:2009.01858, App. B). State the version, not the name.
- **HMcode versions mixed.** 2015/2016 used linear theory for the two-halo
  term and an exponential one-halo damping; η ≃ 0.4 there against 0.139 now;
  2016 had an extra 1.5 exponent in the Dolag correction [src:
  arXiv:2009.01858, Sects. 3.1, 4.3, 4.4, 5.3].
- **Bryan–Norman Δ_v with HMcode-2020.** A 9% different Δ_v (337 against
  308) changes the halo radii the fit was tuned with [der from App. A].
- **Total-matter σ in the mass function with neutrinos.** Raises the
  scatter; HMcode uses σ_cc (Sect. 3.5). Same rule as the cb field in L2.
- **Using HMcode for a galaxy or gas spectrum.** Not designed for it
  (arXiv:2303.08752, Sect. 3.7.2).
- **Emulator-based accuracy claims.** A fit judged against EuclidEmulator2
  (arXiv:2402.17492, arXiv:2410.14623) inherits the emulator's own error;
  compare with N-body where the paper does.

## Reading list
<!-- key: reading-list -->

- Review: Asgari, Mead & Heymans 2023, arXiv:2303.08752 — matter
  normalisation conditions, halofit and HMcode in context.
- Foundation: Smith et al. 2003, arXiv:astro-ph/0207664 — halofit form,
  Gaussian-filter k_σ, n_eff, C.
- Method: Takahashi et al. 2012, arXiv:1208.2701 — refitted coefficients,
  w terms, weighting.
- Method: Mead et al. 2021, arXiv:2009.01858 — HMcode-2020 equations,
  Table 2 parameters, δ_c and Δ_v fits, halofit-neutrino versions.
- Method: Mead & Verde 2020, arXiv:2011.08858 — low-mass normalisation trick
  and beyond-linear bias.
- Critique: Bartlett et al. 2024, arXiv:2402.17492 — refit and symbolic
  correction of halofit.
- Application: Sui et al. 2024, arXiv:2410.14623 — symbolic spectra with
  neutrinos and w0wa.
- Context: Mead et al. 2015, arXiv:1505.07833 — original HMcode (in L2).

## Not verified
<!-- key: not-verified -->

- Bird, Viel & Haehnelt 2012 (arXiv:1109.4416) correction terms: not read.
- The Mead et al. 2015 and 2016 parameter tables: not read; version
  differences are given as HMcode-2020 describes them.
- The Smith et al. coefficients for f1,2,3 in non-flat Λ models: only the
  interpolation advice was read.
- The baryonic part of HMcode-2020 (Sect. 6): left to the sibling dossier.
- Whether current CAMB and CLASS releases still default to the halofit
  variants described in arXiv:2009.01858 (2020): no code documentation read.
