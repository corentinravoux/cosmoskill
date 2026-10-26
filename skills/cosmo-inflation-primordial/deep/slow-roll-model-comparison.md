# Slow-roll parameters, model comparison and reheating — cosmo-inflation-primordial dossier

Scope: how an inflationary model is confronted with CMB data in practice —
which parametrisation is fitted (Hubble-flow or potential slow-roll
parameters, numerical mode integration with a Taylor-expanded or
free-form potential, specific potentials), how the number of e-folds N_*
is tied to reheating and which priors are put on it, how Bayesian
evidences are computed and how prior choices drive them, and how far the
usual leading-order (n_s, r) predictions are from the exact slow-roll ones.
Snapshot: 2026-10-19.
From: Planck 2018 X (arXiv:1807.06211), Sects. 4–5; LiteBIRD 2022 review
(arXiv:2202.02773), Sects. 2.2 and 2.4.

Already in L2, not repeated here: the parametrisation of P_R and P_t and
the slow-roll dictionary, first-order Hubble-flow results, the R² range
of N_* and the ACT η_V value
(`physics-and-methods.md#slow-roll-dictionary-textbook`); the
α-attractor and Higgs leading-order formulas and ASPIC as a library
(`physics-and-methods.md#slow-roll-dictionary-textbook`); the n_s debate,
the reheating equation-of-state bound and the stiff-epoch
gravitational-wave argument (`open-questions.md#has-ns-moved-and-does-it-exclude-starobinsky`);
the dependence of n_s on data combination and model
(`systematics.md#a1-dependence-on-the-data-combination`,
`systematics.md#a2-dependence-on-the-cosmological-model`). Tension and
evidence metrics in general are in `cosmo-statistics-inference`.

## How it is done
<!-- key: how-it-is-done -->

Notation (Planck 2018 X, arXiv:1807.06211, Table 1): Hubble-flow
functions (HFF) ε_1 = −Ḣ/H², ε_(n+1) = ε̇_n/(H ε_n); potential parameters
ε_V = M_Pl² V_φ²/(2V²), η_V = M_Pl² V_φφ/V, ξ²_V = M_Pl⁴ V_φ V_φφφ/V²,
ϖ³_V = M_Pl⁶ V_φ² V_φφφφ/V³; N_* the number of e-folds between Hubble
exit of the pivot k_* and the end of inflation; B = 𝓔_2/𝓔_1 the Bayes
factor between models of evidences 𝓔_i; Δχ² = 2[ln L_max(M1) − ln
L_max(M2)] the best-fit comparison [src: Sect. 2.1].

### Step 1. Choose how much of the model is assumed
<!-- key: step-1-choose-how-much-of-the-model-is-assumed -->

Planck 2018 runs the analysis at increasing levels of model commitment:

1. Phenomenological (n_s, r, running) at a pivot: L2.
2. HFF parameters, with the primordial spectra from the approximate
   analytic expressions of the Green's-function method, to first or second
   order in the HFFs; potential parameters follow "by an exact remapping"
   [src: Sect. 4.1].
3. Taylor expansion of V(φ) to order n = 2, 3 or 4 around φ_*, the field
   value when k_* = 0.05 Mpc⁻¹ exits the Hubble radius, restricted to the
   observable window and with no assumption on the end of inflation; the
   spectrum comes from full numerical integration of the Fourier modes in
   the inflationary module of CLASS, without slow roll (arXiv:1807.06211) [src: Sect. 5.1].
   The same with a Taylor expansion of H(φ), which also marginalises over
   the initial φ̇ [src: Sect. 5.2].
4. Taylor expansion of the full V(φ), trusted until inflation ends at
   ε_V = 1, with N_* fixed to 55: CLASS integrates the background to the
   end of inflation, steps back 55 e-folds and matches k_* there (arXiv:1807.06211) [src:
   Sect. 5.3].
5. Free-form reconstruction: d² ln V/dφ² as a linear spline with N movable
   knots, integrated twice (Eqs. 49–50), the number of knots chosen by
   evidence [src: Sect. 5.4].
6. Named potentials with reheating marginalised, giving Δχ² and ln B
   relative to R² (Table 5) [src: Sect. 4.2].

The stated reason for stopping at the observable window in level 3:
"what happens after the inflaton rolls down beyond this range might not
be captured by the simplest descriptions" (a non-trivial shape before the
end, a waterfall field, several short inflationary stages); it assumes a
potential smooth enough for a fourth-order Taylor expansion, which excludes
sharp features [src: Sect. 5.1].

### Step 2. Tie N_* to the post-inflationary history
<!-- key: step-2-tie-n-to-the-post-inflationary-history -->

Planck uses (arXiv:1807.06211, Eq. 47)
N_* ≃ 67 − ln(k_*/a_0H_0) + ¼ ln(V_*²/(M_Pl⁴ ρ_end)) + [(1 − 3w_int)/(12(1 + w_int))] ln(ρ_th/ρ_end) − (1/12) ln g_th,

with ρ_end the energy density at the end of inflation, V_* the potential
at Hubble exit of k_*, w_int the effective equation of state between the
end of inflation and thermalisation at ρ_th, g_th the bosonic degrees of
freedom there. Settings: g_th = 10³, ε_end = 1; w_int = (p − 2)/(p + 2)
when the potential is ∝ φ^p during the oscillations, or w_int = 0 when the
potential describes only the inflationary stage; logarithmic prior on ρ_th
over [(1 TeV)⁴, ρ_end]; spectra to second order in the HFFs, computed with
modified ASPIC routines; pivot 0.002 Mpc⁻¹ in this section to match the
(n_s, r) figure (arXiv:1807.06211) [src: Sect. 4.2].

The ASPIC Bayesian scan parametrises all reheating histories with one
number, the rescaled reheating parameter R = R_rad ρ_end^(1/4)/M_Pl, R_rad
= (a_end/a_reh)(ρ_end/ρ_reh)^(1/4) (Martin et al. 2014, arXiv:1312.3529,
Eq. 10), with prior ln R ~ U(−46, 15) (Eq. 11), whose bounds encompass
−1/3 < w̄_reh < 1 and ρ_nuc < ρ_reh < ρ_end with ρ_nuc^(1/4) = 10 MeV, so
that reheating ends after inflation and before nucleosynthesis [src: Sect.
3.1].

The inverse use — reheating from a measured n_s — takes a reheating
duration N_rh, equation of state ω and temperature T_rh (end of reheating
at ρ = 2ρ_R) and solves T_rh(ω, N_*, H_*, V_end) (Drees and Xu 2025,
arXiv:2504.20757, Eq. 20), valid for ω ≠ 1/3 and with the
temperature-dependent g_* and g_*s of the Standard Model; at ω = 1/3 no
relation between inflationary predictions and reheating follows [src:
Sect. 4].

### Step 3. Put priors on the model parameters
<!-- key: step-3-put-priors-on-the-model-parameters -->

Planck model comparison [src: arXiv:1807.06211, Sect. 4.2, Tables 4–5]:
uniform priors 0.019 < Ω_b h² < 0.025, 0.095 < Ω_c h² < 0.145, 1.03 <
100θ_MC < 1.05, 0.01 < τ < 0.4; logarithmic prior on 10¹⁰A_s over [e^2.5,
e^3.7]; model parameters log-uniform over stated ranges, for example −4 <
log₁₀ ξ < 4 for the non-minimal coupling, 0.3 < log₁₀(f/M_Pl) < 2.5 for
natural inflation, −2 < log₁₀ α < 4 for the E- and T-model α-attractors.

The rule ASPIC states for choosing a prior shape [src: arXiv:1312.3529,
Sect. 2.2]: a parameter whose order of magnitude is unknown (a coupling in
a perturbative expansion) gets a Jeffreys prior, uniform in its logarithm;
a scale parameter whose order of magnitude is known gets a uniform prior.
The range matters because, when the likelihood is much narrower than the
prior, 𝓔 ∝ 1/(θ_max − θ_min) for uniform priors (Eq. 8); the dependence is
mild on the logarithmic Jeffreys scale, and a parameter the data do not
constrain leaves the Bayes factor unchanged, which is why a complexity
measure is also needed [src: same]. A potential that admits several
theory-motivated priors is treated as several models [src: same].

Normalisation and reheating priors are made identical across models:
the potential scale M is traded for the measured amplitude P_* through
M⁴ = 24π² (ε_1/v_*) P_* at first order (Eq. 22), and ln R has the same
prior for all, so these Occam factors cancel in Bayes factors. The stated
assumption: "all models have the same ability to reheat the universe
after inflation and to produce the observed amplitude"; a model that
predicts M or the reheating would need its evidence recomputed [src:
arXiv:1312.3529, Sect. 3.3].

For numerical Taylor reconstructions Planck puts flat priors on the
combinations that equal ε_V, η_V, ξ²_V, ϖ³_V rather than on V, V_φ, …,
V_φφφφ, because the former "provide nearly linear contributions to the
tilt, running, running of the running" and flat priors on the raw
coefficients make convergence "plagued by complicated parameter
degeneracies" [src: arXiv:1807.06211, Sect. 5.1]. In the full-potential
case (level 4) the extra e-fold condition makes the raw coefficients
constrained enough to sample them with flat priors directly [src: Sect.
5.3]. Free-form priors: N discrete uniform in [0, 8]; ln V_* uniform in
[−25, −15]; d ln V_*/dφ log-uniform in [10⁻³, 10^−0.3]; knot heights
uniform in [−0.5, 0.5]; sorted-uniform knot positions inside the
observable window estimated from the N = 0 potential (k from 10⁻⁴ to
10^−0.3 Mpc⁻¹); inflation must continue and the field roll downhill
through the window, with 2 < ln 10¹⁰P_R(k) < 4 [src: Sect. 5.4, Table 9].

### Step 4. Compute the evidence
<!-- key: step-4-compute-the-evidence -->

Planck: posteriors with CosmoMC or Monte Python, evidences with nested
sampling (MultiNest or PolyChord); |ln B| > 5 is "strong" evidence;
Table 5 quotes 0.3 as the error on ln B [src: arXiv:1807.06211, Sect. 2.1,
Table 5].

ASPIC's fast route [src: arXiv:1312.3529, Sects. 3.1, 3.3]:

- The likelihood depends on the inflationary model only through P_ζ(k),
  which for slow-roll models is a series in ln(k/k_*) whose coefficients
  a_i depend on the HFFs ε_n (Eq. 16). The post-inflationary parameters θ_s
  are integrated out once, giving an effective likelihood L_eff(P_*, ε_n)
  (Eq. 19), interpolated with a neural network (under a microsecond per
  call).
- Each model only maps its potential and reheating parameters to
  (P_*, ε_n) through the ASPIC functionals, so the evidence integral is at
  most four-dimensional (three potential parameters plus ln R) (Eq. 18),
  assuming separable priors (Eq. 20).
- MultiNest with target accuracy 10⁻⁴ on the evidence and 30,000 live
  points, about one CPU hour per model; numerical errors are not quoted
  because they are negligible against prior sensitivity (arXiv:1312.3529)
  [src: Sect. 3.3].
- Result for Planck 2013: of 193 models, 34% ruled out with very strong
  evidence, 26% favoured (15 potential shapes), 9% if Bayesian complexity
  is included (9 shapes, all plateau) (arXiv:1312.3529) [src: abstract].

### Step 5. Place predictions on the r–n_s plane
<!-- key: step-5-place-predictions-on-the-r-ns-plane -->

Planck draws first-order slow-roll predictions at k = 0.002 Mpc⁻¹ for 50 <
N_* < 60 [src: arXiv:1807.06211, Sect. 4.2]; ACT draws the same band at
k_* = 0.05 Mpc⁻¹ and notes that N "depends on the (highly uncertain)
post-inflation reheating history" [src: arXiv:2503.14454, Sect. IV.4,
Fig. 10 and footnote]. For the R² potential, slow-roll formulas evaluated
without the large-N expansion give r = (4/3)[3(1 − n_s) + 2 − 2√(3(1 − n_s)
+ 1)] (arXiv:2504.20757, Eq. 13) and N_* as a closed function of t = 1 −
n_s (Eq. 14), whose expansion is N_* ≃ 2/(1 − n_s) + (3/4) ln(1 − n_s) +
0.47 (Eq. 15). Inverting it gives the refined approximation
n_s ≃ 1 − 2/[N_* − (3/4) ln(2/N_*)], r ≃ 12/[N_* − (3/4) ln(2/N_*)]² (Eq. 17),

which reduces to the usual n_s ≃ 1 − 2/N_*, r ≃ 12/N_*² (Eq. 18) when the
term −(3/4) ln(2/N_*) — 2.41 at N_* = 50 and 2.55 at N_* = 60 — is dropped
(arXiv:2504.20757) [src: Sect. 2]. Their "exact" curve is the first-order slow-roll formulas
(Eqs. 6–8) evaluated exactly, not a numerical mode integration [src:
Sect. 2].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### First or second order in the Hubble-flow functions
<!-- key: first-or-second-order-in-the-hubble-flow -->

Planck TT,TE,EE + lowE + lensing (+ BK15): to second order, ε_1 < 0.0097
(0.0044) at 95%, ε_2 = 0.032 +0.009/−0.008 (0.035 ± 0.008), ε_3 = 0.19
+0.55/−0.53 (0.12 +0.36/−0.42) at 95%; ε_V < 0.0097 (0.0044), η_V = −0.010
+0.007/−0.011 (−0.015 ± 0.006), ξ²_V = 0.0035 +0.0078/−0.0072 (0.0029
+0.0073/−0.0069) at 95% [src: arXiv:1807.06211, Eqs. 41–46]. Freeing ε_3
loosens the ε_1 bound from 0.0063 to 0.0097 without BK15, but with BK15
the bound barely moves (0.0039 to 0.0044), since the B modes fix ε_1
[src: Eqs. 37 and 41]. A first-order fit is therefore a choice to set the
running to its slow-roll value.

### Slow-roll formulas or numerical mode integration
<!-- key: slow-roll-formulas-or-numerical-mode-integration -->

The numerical Taylor reconstruction (level 3) gives ε_V < 0.0042, 0.0045,
0.0048 and η_V = −0.0124 +0.0033/−0.0052, −0.0163 +0.0057/−0.0063, −0.0082
+0.0096/−0.0120 for n = 2, 3, 4, with Δχ² of −0.22 (n = 3 against 2) and
−0.82 (n = 4 against 3); n_s and τ "remain extremely stable" [src:
arXiv:1807.06211, Table 6, Sect. 5.1]. Planck states that these results
"are close to those of Sect. 4.1, obtained under the slow-roll
approximation", because the data show no running [src: same]. So, at
current precision, slow-roll formulas lose nothing for smooth potentials;
the numerical route is needed for features and for potentials not smooth
in the window.

### Observable window or the whole potential
<!-- key: observable-window-or-the-whole-potential -->

Trusting the Taylor expansion to the end of inflation with N_* = 55 is
"much more constrained": a pure quadratic gives n_s = 0.963 and r_0.002 =
0.136, in tension with the data; a cubic term lowers χ²_eff by 13.18 and a
quartic by 3.50 more; the posterior prefers potentials with an inflection
point [src: arXiv:1807.06211, Sect. 5.3, Table 8]. The running in this
case is fixed at about −6 × 10⁻⁴ by the model class, "not directly
measured, but rather predicted"; testing it would need about ten times the
sensitivity of current CMB + BAO data [src: same]. The cost of this level:
it assumes a single smooth potential, ε_V = 1 at the end and no later
inflation [src: same].

### Free-form or parametric potential
<!-- key: free-form-or-parametric-potential -->

The free-form reconstruction lets the data choose the number of knots;
Planck finds N = 1 preferred, a constant non-zero d² ln V/dφ² [src:
arXiv:1807.06211, Sect. 5.4, Fig. 17]. It needs derivatives of V, which is
why the spline is put on the second derivative of ln V rather than on V
[src: same].

### Leading-order or refined predictions
<!-- key: leading-order-or-refined-predictions -->

With the refined Eq. 17, the Starobinsky prediction at N_* = 60 lies inside
the P-ACT-LB-BK18 2σ region, whereas Eq. 18 puts N_* ≤ 60 near its
boundary; Eq. 18 "underestimates the spectral index" for a given N_* [src:
arXiv:2504.20757, Sect. 3, Fig. 1]. The authors also note that larger N_*
than 60 follows from a stiff post-inflationary phase, which the matching
of Step 2 must then justify [src: same]. Neither Planck's Table 5 (second
order in HFFs, reheating marginalised) nor ASPIC uses Eq. 18; the
leading-order band is a plotting device [src: arXiv:1807.06211, Sect.
4.2; arXiv:1312.3529, Sect. 3.1].

### Δχ² or Bayes factor
<!-- key: chi2-or-bayes-factor -->

Planck quotes both (Table 5), and they rank models differently: D-brane
p = 4 has the most negative Δχ² in the table (−3.5) but ln B = −0.4, below
D-brane p = 2 (Δχ² = −2.0, ln B = +0.6); the T-model m = 1 has Δχ² = −0.1
and ln B = −1.2 [src: arXiv:1807.06211, Table 5].
The Bayes factor depends on the prior range of the model parameters
(Step 3); Δχ² does not but rewards extra parameters.

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Reheating settings | g_th = 10³; ε_end = 1; ρ_th log-uniform in [(1 TeV)⁴, ρ_end] | Planck 2018 + BK15 | arXiv:1807.06211 | Sect. 4.2 |
| A_s prior (model comparison) | 10¹⁰A_s log-uniform in [e^2.5, e^3.7] | Planck 2018 | arXiv:1807.06211 | Sect. 4.2 |
| ln R prior | U(−46, 15); ρ_nuc^(1/4) = 10 MeV | ASPIC scan | arXiv:1312.3529 | Eq. 11 |
| Evidence settings | MultiNest tolerance 10⁻⁴, 30,000 live points, ~1 CPU h/model | ASPIC scan | arXiv:1312.3529 | Sect. 3.3 |
| ln B vs R² (selection) | φ² −11.5; φ⁴ −56.0; φ −3.9; φ^(2/3) −4.6; natural −6.6; SB SUSY −6.8; non-minimal φ⁴ −2.4; hilltop quartic −1.4; D-brane p = 2 +0.6; E-model n = 1 −0.3; T-model m = 1 −1.2 (error 0.3) | Planck 2018 TT,TE,EE + lowE + lensing + BK15 | arXiv:1807.06211 | Table 5 |
| α-attractor bounds (95%) | log₁₀α^E_1 < 1.3, log₁₀α^E_2 < 1.1; log₁₀α^T_1, log₁₀α^T_2 < 1.0 | same | arXiv:1807.06211 | Sect. 4.2 |
| Non-minimal coupling (95%) | log₁₀ ξ > −1.5 | same | arXiv:1807.06211 | Sect. 4.2 |
| Taylor V, n = 2 | n_s = 0.9650 ± 0.0042, r_0.002 < 0.060 | same | arXiv:1807.06211 | Table 6 |
| Full V, N_* = 55 | n = 3: n_s = 0.9599 +0.0034/−0.0018, r_0.002 = 0.066 +0.010/−0.016 | same | arXiv:1807.06211 | Table 8 |
| −(3/4) ln(2/N_*) | 2.41 (N = 50), 2.55 (N = 60) | R² | arXiv:2504.20757 | Sect. 2 |
| n_s with DESI DR2 | 0.9752 ± 0.0030 (P-ACT-LB with DR2) | ACT DR6 | arXiv:2503.14454 | App. G.1 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Leading-order formulas used for an exclusion.** They bias n_s low at
  fixed N_* (above); test by recomputing the model prediction with Eq. 17
  or numerically before quoting a σ [src: arXiv:2504.20757, Sect. 3].
- **N_* fixed at 50–60 without a reheating model.** The range is a
  convention; Planck marginalises over ρ_th, ASPIC over ln R, and a
  measured n_s maps onto (ω, T_rh) only for ω ≠ 1/3 [src:
  arXiv:1807.06211, Sect. 4.2; arXiv:1312.3529, Sect. 3.1;
  arXiv:2504.20757, Sect. 4].
- **Incomplete potentials.** Hilltop, D-brane, exponential-tail and SB SUSY
  potentials need extra terms to end inflation, and "the precise form of
  the additional terms may affect the scientific interpretation" [src:
  arXiv:1807.06211, Sect. 4.2, footnote 12]; ask what completes the model.
- **Evidence read without its prior.** 𝓔 scales with the prior volume of
  constrained parameters; check the stated range and shape (Jeffreys or
  uniform) and whether the normalisation and reheating priors are common
  to the models compared [src: arXiv:1312.3529, Sects. 2.2, 3.3].
- **Flat priors on raw Taylor coefficients.** Slow convergence from
  degeneracies [src: arXiv:1807.06211, Sect. 5.1].
- **Predicted running read as measured.** In full-potential fits the
  running is fixed by the model class [src: arXiv:1807.06211, Sect. 5.3].
- **"Spoon-like" potentials in reconstruction plots.** Allowed at n = 4 but
  not preferred; Planck warns against reading Fig. 12 as evidence for a
  kink and plateau [src: Sect. 5.1].
- **Pivot mismatch.** Planck's model section uses 0.002 Mpc⁻¹, ACT 0.05
  Mpc⁻¹; copy the pivot with every (n_s, r) or ε value [src:
  arXiv:1807.06211, Sect. 4.2; arXiv:2503.14454, Sect. IV.4].

## Reading list
<!-- key: reading-list -->

- Application: Planck 2018 X, arXiv:1807.06211 — Eq. 47 and Table 5
  (models with reheating), Sects. 5.1–5.4 (potential reconstruction at four
  levels of assumption).
- Method: Martin et al. 2014, arXiv:1312.3529 — effective likelihood in
  slow-roll space, reheating parameter R, prior rules, evidences for 193
  models. [src: abstract]
- Code: Martin, Ringeval and Vennin 2014, arXiv:1303.3787 — the ASPIC
  functionals ε_n(θ_reh, θ_inf) (L2).
- Application: ACT DR6 extended models, arXiv:2503.14454 — r–n_s plane
  with BK18 and the DR2 update (Sect. IV.4, App. G.1).
- Critique: Drees and Xu 2025, arXiv:2504.20757 — exact versus
  leading-order R² predictions (Eqs. 13–18) and the reheating map (Eq. 20).
- Foundation: Kallosh et al. 2013, arXiv:1311.0472 — α-attractor
  predictions (L2).

## Not verified
<!-- key: not-verified -->

- The Green's-function expressions for the spectra in terms of the HFFs,
  the a_i(ε_n) coefficients and the HFF-to-potential remapping (cited in
  arXiv:1807.06211, Sect. 4.1, and arXiv:1312.3529, Eq. 16): not read.
- The H(φ) reconstruction of Planck Sect. 5.2 beyond its first paragraph;
  the free-form reconstruction paper by Handley et al. 2019; the Planck
  2015 inflation paper (cited there).
- ASPIC (arXiv:1303.3787) body and Encyclopaedia priors for individual
  models (App. A of arXiv:1312.3529): not read this session.
- No post-ACT multi-model Bayesian evidence scan was found in a date-sorted
  search from April 2025. Single-model Bayesian or reheating analyses were
  seen by title only: arXiv:2603.25721 (α-Starobinsky with Planck, ACT and
  DESI), arXiv:2505.01129 (reheating for Starobinsky and Higgs inflation),
  arXiv:2606.11725 (inverse-tangent inflation).
- The SPT-3G or CMB-SPA (r, n_s) model-plane statements: not read.
