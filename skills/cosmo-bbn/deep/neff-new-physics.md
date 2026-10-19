# N_eff and new physics from BBN — cosmo-bbn dossier

Scope: how extra radiation, a neutrino chemical potential, an MeV-scale
thermal relic or a decaying massive relic is put into a BBN calculation
and a likelihood; which assumptions the usual ΔN_eff parametrisation
hides; and how BBN-only, CMB-only and joint N_ν or N_eff limits are set
up and reported.
Snapshot: 2026-10-18.
From: Cooke 2024, Sect. 3.2 and 4; Grohs & Fuller 2023, Sect. 5.

Already in L2, not repeated here: the N_ν and N_eff values with their data
and the table of other new-physics limits in
`results.md#neff-and-new-physics`; the N_ν versus N_eff baseline in
`physics-and-methods.md#conventions-and-where-the-community-is-split`; the
EMPRESS helium debate in
`open-questions.md#helium-systematics-and-neff-from-bbn`; how codes treat
neutrino decoupling in `deep/bbn-codes.md`; full versus summarised BBN
likelihoods and rate nuisances in `deep/nuclear-reaction-rates.md`.

Notation. N_ν is the number of neutrino-like species during BBN (3 in the
Standard Model); N_eff the effective number of relativistic species
measured by the CMB, 3.044 for N_ν = 3; ΔN_eff ≡ N_eff − N_eff^SM; ξ_ν =
μ_ν/T_ν the comoving neutrino degeneracy parameter (μ_ν the chemical
potential); η the baryon-to-photon ratio, η₁₀ = 10¹⁰ η; ω_b = Ω_b h²;
X_n the neutron fraction; T_np ≈ 0.8 MeV the n/p freeze-out temperature;
T_νd ≈ 2 MeV neutrino decoupling; Q = m_n − m_p.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Decide what ΔN_eff means physically
<!-- key: step-1-decide-what-neff-means-physically -->

ΔN_eff enters the expansion rate. To first order,
H ≃ H⁽⁰⁾ (1 + (7/86) ΔN_eff) (Ganguly, Jung & Yun 2025, arXiv:2507.23354)
[src: Eq. 16]. In PArthENoPE the extra density is
ρ_X = (7/8)(π²/30) ΔN_eff T_X⁴ with T_X = T above an effective decoupling
temperature T_d = 2.3 MeV and T_X following the plasma entropy below it;
inputs are allowed in −3.0 ≤ ΔN_eff ≤ 15.0 (Pisanti et al. 2008,
arXiv:0705.0290) [src: Eqs. 23–24, Sect. III.2].

What ΔN_eff does to the weak rates depends on where the energy goes:

- **ΔN_eff > 0, dark radiation.** A component decoupled before neutrino
  decoupling leaves T_νe(T_γ) unchanged (Eq. 5) and only speeds up the
  expansion [src: arXiv:2507.23354, Sect. II].
- **ΔN_eff < 0, entropy injection.** A negative ΔN_eff "necessarily"
  means a lower T_ν/T_γ; the authors model it by an electromagnetic decay
  between T_νd and T_np, with
  T_νe/T_νe⁽⁰⁾ = (1 + x_e ΔN_eff/N_eff⁽⁰⁾)^{1/4} (Eq. 6), where x_e = 1
  dilutes all flavours equally [src: Sect. II]. The rates then change as
  well as H: δT_νe/T_νe⁽⁰⁾ ≃ (x_e/12) ΔN_eff (Eq. 17) and the n ↔ p rates
  shift by Eqs. 22–23 [src: Sect. III.2].
- **Energy into neutrinos.** Dark-radiation bounds "cannot be applied" to
  models that deposit the excess in the neutrino sector, which need the
  neutrino momentum distribution [src: Sect. II].

Mapping N_ν during BBN to N_eff at the CMB:

- PRIMAT assumes extra species do not share the e⁺e⁻ heating (z_ν = 1 for
  them), giving N_eff = 3 (z_ν z^stand/z)⁴ + (N_ν − 3)(z^stand/z)⁴ and
  dN_eff/dN_ν = (z^stand/z)⁴ ≃ 1.0090 (Pitrou et al. 2018,
  arXiv:1801.08023) [src: Eq. 165, Sect. VI.4]; z_ν and z are the
  comoving neutrino and plasma temperatures.
- Yeh et al. 2022 scale all species: N_eff = 1.0147 N_ν (arXiv:2207.13133)
  [src: Eq. 28], i.e. 3.044/3 [der].
- PRIMAT's authors note Cyburt et al. assume their Eq. 65 holds for
  N_ν ≠ 3, and judge the difference "not crucial" given the size of the
  N_ν errors [src: arXiv:1801.08023, Sect. VI.4].

### Step 2. Add a neutrino chemical potential
<!-- key: step-2-add-a-neutrino-chemical-potential -->

For each flavour μ_ν + μ_ν̄ = 0, ξ_ν is frozen, and oscillations
equalise the flavours (arXiv:1801.08023) [src: Sect. VI.3]. The asymmetry
is

    η_ν ≡ (n_ν − n_ν̄)/n_γ ≃ (1/(12 ζ(3))) (T_ν/T)³ (π² ξ_ν + ξ_ν³)      (PRIMAT Eq. 158)

≃ 0.25 ξ_ν [1 + ξ_ν²/π²] with the Standard-Model T_γ/T_ν (Escudero et al.
2022, arXiv:2208.03201) [src: Eq. 1]. Three effects:

1. Extra energy density, flavour- and sign-independent:
   ΔN_eff = Σ_α [(30/7)(ξ_α/π)² + (15/7)(ξ_α/π)⁴] (Escudero Eq. 4); for
   |ξ| ≲ 0.1 this is ≲ 0.01, so Escudero et al. keep only the helium
   effect [src: arXiv:2208.03201, Sect. II].
2. Shifted neutrino distributions in the weak rates (PRIMAT Eq. 160), the
   dominant effect: the equilibrium n/p is multiplied by e^{−ξ_ν}
   (Eq. 161), so ΔY_P/Y_P ≃ −(1 − Y_n^F) ξ_ν (Eq. 162) with Y_n^F the
   freeze-out neutron yield [src: arXiv:1801.08023, Sect. VI.3].
3. Incomplete decoupling with asymmetry, negligible [src: same].

Numerically, for small ξ_ν: ΔY_P/Y_P ≃ −0.96 ξ_ν, Δ(D/H)/(D/H) ≃ −0.53 ξ_ν,
Δ(³He/H)/(³He/H) ≃ −0.18 ξ_ν, Δ(⁷Li/H)/(⁷Li/H) ≃ −0.62 ξ_ν
(arXiv:1801.08023) [src: Eq. 163]; Escudero et al. use the exponential
forms Y_P ≃ Y_P^SBBN e^{−0.96 ξ_νe} and D/H ≃ (D/H)^SBBN e^{−0.53 ξ_νe}
[src: arXiv:2208.03201, Eqs. 2–3].

### Step 3. Add an MeV-scale thermal relic
<!-- key: step-3-add-an-mev-scale-thermal-relic -->

Sabti et al. compute the background (T_γ, T_ν, H and the entropy transfer
function 𝒩 of PRIMAT) externally with NUDEC_BSM and pass it to the PRIMAT
network; the default PRIMAT and the externally computed Standard-Model
background agree to < 0.1% in all abundances (Sabti et al. 2020,
arXiv:1910.01649) [src: Sect. II.2]. A relic acts through three channels:
the expansion rate, the T_ν/T_γ ratio entering n ↔ p rates, and, for
electrophilic species, entropy released after nucleosynthesis that
dilutes the baryons per photon [src: Sect. II.3]. By mass:
m_χ ≲ 0.05 MeV neutrinophilic relics only speed up expansion and raise
Y_P and D/H, electrophilic ones also lower D/H through dilution;
0.5 ≲ m_χ ≲ 10 MeV electrophilic relics lower both Y_P and D/H
[src: Sect. II.3]. PRyMordial exposes the same physics through flags for
electrophilic, neutrinophilic or separate-temperature sectors, plus
phenomenological rescalings of the n ↔ p and nuclear rates
(Burns, Tait & Valli 2024, arXiv:2307.07061) [src: Sect. 3.3].

### Step 4. Add a decaying massive relic
<!-- key: step-4-add-a-decaying-massive-relic -->

Bianco et al. 2026 order the effects of injecting Standard-Model particles
by injection time t_inj (arXiv:2605.26824) [src: Sect. 3]:

| Effect | When it dominates | Mechanism |
|---|---|---|
| Interconversion | 0.1 s ≲ t_inj ≲ 10² s | mesons and nucleons convert p ↔ n; in a proton-dominated plasma π⁻ p → n X wins, so hadronic injection raises n/p and Y_P |
| Hadrodisintegration | t_inj ≳ 10² s | injected nucleons no longer thermalise first and break up formed nuclei |
| Photodisintegration | t_inj ≳ 10⁴ s | electromagnetic cascade photons above nuclear thresholds |

Only π±, K±, K_L, n, n̄, p, p̄ live long enough to interconvert; charged
hadrons thermalise in ~10⁻¹² s even at 0.1 MeV [src: Sect. 3.1.1].
Photodisintegration needs E_N^th < E_ee^th ≃ m_e²/(22T), so it acts only
for T ≲ O(keV), after standard BBN, and the two factorise; above the
pair threshold the cascade gives the universal spectrum
f_γ ∝ (E/E_X)^{−3/2} below E_X = m_e²/(80T), ∝ (E/E_X)^{−2} up to E_ee^th,
zero above (Kawasaki & Moroi form) [src: Sect. 3.3, Eq. 67]. Energy
injected only into the electromagnetic sector after neutrino decoupling
lowers T_ν/T and hence N_eff (Eq. 72) [src: Sect. 3.4]. The pipeline:
PYTHIA for hadronisation and final-state radiation, a modified AlterBBN
("AlterAlterBBN") for thermal BBN with hadronic injection, ACROPOLIS for
late disintegration [src: Sects. 2–4].

### Step 5. Build the likelihood
<!-- key: step-5-build-the-likelihood -->

- **Convolution form (Fields–Olive–Yeh).** A Monte Carlo over rates gives
  L_NBBN(X; η, N_ν) for X = (Y_P, D/H, ³He/H, ⁷Li/H); Gaussian
  observational likelihoods are convolved with it (Eq. 27); flat priors on
  η and N_ν are "implicitly" assumed; only D/H and Y_P are used because
  ³He lacks a primordial value and ⁷Li may not be primordial
  (arXiv:2207.13133) [src: Sect. 3]. The CMB term uses Planck chains that
  do not impose the BBN Y_P(ω_b) relation, converted to the BBN Y_P
  convention, and marginalised over Y_P (Eq. 29); the joint likelihood
  integrates the product over Y_P (Eq. 34), which links BBN and CMB when
  helium data are used [src: Sects. 3, 4.1].
- **χ² with theory errors in quadrature.** Sabti et al.:
  χ²_BBN = Σ (X − X_obs)²/(σ_theo² + σ_obs²) for Y_P and D/H (Eq. 13), with
  σ_theo(Y_P) = 0.00017 and σ_theo(D/H) = 0.036 × 10⁻⁵ from PRIMAT
  (arXiv:1910.01649) [src: Sect. III.1]; Escudero et al. use the same
  with σ_theo(D/H) = 0.07 × 10⁻⁵ (PArthENoPE rates) or 0.04 × 10⁻⁵ (PRIMAT
  rates) (arXiv:2208.03201) [src: Sect. III, footnote 1]; Ganguly et al.
  use σ_mod²(Y_P) = 0.00003² + 0.00012² and σ_mod(D/H) = 0.06 × 10⁻⁵
  (arXiv:2507.23354) [src: Eq. 31].
- **Inside a CMB sampler.** Goldstein & Hill run CAMB with PRyMordial in
  Cobaya, with a Gaussian Y_P = 0.2458 ± 0.0013 and, following ACT DR6,
  10⁵ D/H = 2.547 ± 0.104, which already includes the theory error; flat
  priors 0.017 ≤ ω_b ≤ 0.027 and 0.1 ≤ N_eff ≤ 6.0, or 3.044 ≤ N_eff ≤ 6.0
  for ΔN_eff bounds; convergence |R − 1| < 0.02 (arXiv:2603.13226)
  [src: Sect. II]. Their Y_P is the CAMB nucleon fraction, which differs
  from the mass fraction by ~0.5% [src: footnote 2].

### Step 6. Report the limit
<!-- key: step-6-report-the-limit -->

Yeh et al. quote both the two-sided 2σ limit from the mean,
ΔN_ν < 0.180 (Eq. 36), and a one-sided limit normalised over N_ν ≥ 3 only
(Eq. 37), because a two-sided limit "maybe overly aggressive" when the
best fit lies below 3 and three neutrinos are known to exist
(arXiv:2207.13133) [src: Sect. 4.1]. Goldstein & Hill impose the prior
N_eff ≥ 3.044 for their ΔN_eff < 0.107 [src: arXiv:2603.13226, Sect. II,
Fig. 2].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Dark radiation or entropy injection for ΔN_eff < 0
<!-- key: dark-radiation-or-entropy-injection-for-neff-0 -->

- **Assumes.** The conventional fit extrapolates the dark-radiation case
  (T_ν unchanged) to negative ΔN_eff; Ganguly et al. call this
  "unphysical" (arXiv:2507.23354) [src: Sect. IV].
- **What changes.** δX_n,fo/X_n,fo ≃ 0.04 ΔN_eff for dark radiation (Eq.
  28) but O(10⁻³) ΔN_eff for x_e = 1 injection (Eq. 26), an accidental
  cancellation at the 10% level between the shifts of T_νe, H and the
  equilibrium X_n [src: Sect. III.2]. Y_P "loses its sensitivity" to N_eff
  for ΔN_eff < 0, leaving D/H as the only effective constraint on two
  parameters, so BBN alone cannot exclude points such as ΔN_eff ≃ −0.5,
  η₁₀ = 5.82 [src: Sect. IV].
- **Result.** ΔN_eff < 0.74 (95%) from PDG Y_P and D/H with no lower bound;
  the analysis is truncated at N_eff = 2 [src: Eq. 32]. A Y_P as low as
  the EMPRESS value "cannot be realized" by electromagnetic injection;
  hadronic injection raises Y_P; a lepton asymmetry remains possible
  [src: Sect. IV].
- **Validity.** The x_e = 1 treatment matches a continuous-injection
  calculation for 0.1 s ≲ τ_χ ≲ 1 s and remains good up to ~100 s; for
  τ_χ ≲ 0.1 s flavour-dependent dilution matters; beyond ~100 s the
  dilution of η must be included for D/H [src: Sect. II, Appendix A
  summary].

### Which rate set in a new-physics fit
<!-- key: which-rate-set-in-a-new-physics-fit -->

At ω_b = 0.02236 the three groups predict 10⁵ D/H = 2.49 ± 0.08
(Yeh et al. 2022), 2.52 ± 0.07 (Pisanti et al. 2021) and 2.45 ± 0.04
(Pitrou et al. 2021) (arXiv:2208.03201) [src: Eqs. 11a–c], so Escudero et
al. run every fit twice, with PArthENoPE and PRIMAT rates
[src: Sect. III]. The choice can flip a conclusion: with PRIMAT, ξ_ν =
0.001 ± 0.016 from BBN + CMB; with a code predicting D/H ≃ 2.61 × 10⁻⁵
instead of 2.46 × 10⁻⁵ at Planck parameters (PArthENoPE in 2018),
ξ_ν = 0.021 ± 0.016, because Y_P and D/H then both pull ξ_ν positive
through Eq. 163 (arXiv:1801.08023) [src: Sect. VI.3].

### Which helium value
<!-- key: which-helium-value -->

With PArthENoPE rates and N_eff = 3.044, ξ_νe = 0.043 ± 0.015 (EMPRESS,
~3σ) against 0.008 ± 0.013 (PDG-21 Y_P = 0.245 ± 0.003)
(arXiv:2208.03201) [src: Eqs. 12–13]. The helium choice drives the result:
"current constraints on the (electron) lepton asymmetry … are dominated by
BBN data, and in particular by the primordial helium abundance"
[src: Sect. III].

### How the CMB enters
<!-- key: how-the-cmb-enters -->

- **Full chains or a Gaussian.** PRIMAT's Planck 2015 (ω_b, N_ν) prior is
  "very well represented" by a 2D Gaussian, ω_b = 0.022197 ± 0.000245,
  N_ν = 2.945 ± 0.203, correlation 0.7699, which changes the posteriors
  "only marginally" (arXiv:1801.08023) [src: Sect. VI.4].
- **Y_P tied by BBN without helium data.** Using BBN only to tie Y_P to
  (η, N_ν) in the CMB fit, with no abundance data, already gives "a
  noticeably stronger limit on N_ν" than the CMB alone
  (arXiv:2207.13133) [src: Sect. 4.1].
- **Correlation.** BBN alone correlates N_ν and η positively, N_ν ∝ η⁴ at
  fixed D/H since D/H ∝ η^{−1.6} N_ν^{0.4}; the CMB shows little
  correlation; BBN gives slightly better N_ν, the CMB dominates η
  [src: arXiv:2207.13133, Sect. 4.1].
- **Model-independent ω_b.** Sabti et al. alternatively add
  ω_b = 0.02225 ± 0.00066 to χ²_BBN, an error 4.4 times the Planck ΛCDM
  one, chosen to cover a 12-parameter extension of ΛCDM
  (arXiv:1910.01649) [src: Sect. III.3].
- **Large-scale polarisation.** In CMB + BAO N_eff fits, low-ℓ EE has
  "negligible impact" on N_eff, but with it CMB and DESI BAO are
  inconsistent at ~3σ in (H₀r_d, Ω_m, N_eff); Goldstein & Hill therefore
  drop it in the baseline (arXiv:2603.13226) [src: Sects. II–III].

### What freeing ΔN_eff costs elsewhere
<!-- key: what-freeing-neff-costs-elsewhere -->

With σ(ΔN_eff) = 0.070, ΔN_eff carries 88–98% of the Y_P variance and the
Y_P theory error grows from ~0.0003 to ~0.0010; for D/H it carries
5–28% (Burns 2026, arXiv:2603.22414) [src: Sect. 8]. The baryon density
from abundances barely moves: ω_b = 0.02202 ± 0.00021 → 0.02192 ± 0.00026
(PRIMAT rates) and 0.02231 ± 0.00056 → 0.02226 ± 0.00056 (NACRE II), as
"the freedom in ΔN_eff is absorbed almost entirely by Y_P" [src: Sect. 8].

### Decaying relics: which pieces are modelled
<!-- key: decaying-relics-which-pieces-are-modelled -->

Previous limits (Kawasaki et al. 2018) differ at long lifetimes through
photodisintegration and hadrodisintegration modelling; at short lifetimes
the new bounds are "much stronger", which the authors attribute to new
interconversion rates and to PYTHIA final-state radiation, since
interconversions "do not seem to have been considered at all" for e⁺e⁻
injection before (arXiv:2605.26824) [src: Sect. 5.5]. The new LBT ⁴He
value "improves the interconversion bounds significantly" [src: Sect. 5.5].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| H shift per unit ΔN_eff | 7/86 | first order | arXiv:2507.23354 | Eq. 16 |
| dN_eff/dN_ν | 1.0090 (extra species unheated) vs 1.0147 (all scaled) | PRIMAT vs Fields–Olive–Yeh | arXiv:1801.08023; arXiv:2207.13133 | Eq. 165; Eq. 28 |
| δX_n,fo/X_n,fo per ΔN_eff | 0.04 (dark radiation); O(10⁻³) (EM injection, x_e = 1) | analytic | arXiv:2507.23354 | Eqs. 26, 28 |
| ΔN_eff, BBN only, consistent treatment | < 0.74 (95%), no lower bound | PDG Y_P and D/H | arXiv:2507.23354 | Eq. 32 |
| Abundance response to ξ_ν | −0.96 (Y_P), −0.53 (D/H), −0.18 (³He), −0.62 (⁷Li) per unit ξ_ν | PRIMAT | arXiv:1801.08023 | Eq. 163 |
| ξ_ν, BBN + CMB | 0.001 ± 0.016 (PRIMAT); 0.021 ± 0.016 with PArthENoPE-like D/H | Aver 2015 Y_P, Cooke D/H | arXiv:1801.08023 | Sect. VI.3, Eq. 164 |
| ξ_νe, N_eff = 3.044 | 0.043 ± 0.015 (EMPRESS); 0.008 ± 0.013 (PDG-21) | PArthENoPE rates | arXiv:2208.03201 | Eqs. 12–13 |
| Planck priors used for ξ fits | ω_b = 0.02239 ± 0.00018, Y_P = 0.242 ± 0.012, ρ = 0.663; with N_eff free: N_eff = 2.97 ± 0.29, ρ(N_eff, Y_P) = −0.686 | Planck 2018 as quoted | arXiv:2208.03201 | Eqs. 9–10 |
| BBN theory errors used in χ² | σ(Y_P) = 0.00017; σ(D/H) = 0.036 × 10⁻⁵ (PRIMAT), 0.07 × 10⁻⁵ (PArthENoPE) | thermal relics; lepton asymmetry | arXiv:1910.01649; arXiv:2208.03201 | Sect. III.1; Sect. III fn. 1 |
| Model-independent ω_b | 0.02225 ± 0.00066 | thermal relics | arXiv:1910.01649 | Sect. III.3 |
| N_ν, separate and joint (Planck 2018) | CMB 2.800 ± 0.294; BBN (Y_P + D) 2.889 ± 0.229; CMB + BBN + Y_P + D 2.898 ± 0.141 | Fields–Olive–Yeh | arXiv:2207.13133 | Table 2 |
| N_eff reproductions | abundances only 2.976 ± 0.093; Planck only 2.89 ± 0.19; abundances + Planck 2.961 ± 0.082 | PRyMordial + CAMB | arXiv:2603.13226 | Sect. III |
| N_eff, CMB-PAS (no low-ℓ EE) + abundances | 2.943 ± 0.072; with DESI DR2 2.990 ± 0.070 | same | arXiv:2603.13226 | Sect. III, Eq. 4 |
| D/H likelihood in CMB analyses | 10⁵ D/H = 2.547 ± 0.104 (observation + theory) | ACT DR6 practice | arXiv:2603.13226 | Eq. 3 |
| Y_P theory error with ΔN_eff free | ~0.0003 → ~0.0010 | PRyMordial | arXiv:2603.22414 | Sect. 8 |
| Decay regimes | interconversion 0.1–10² s; hadrodisintegration ≳ 10² s; photodisintegration ≳ 10⁴ s | Standard-Model injections | arXiv:2605.26824 | Sect. 3 |
| Non-thermal-rate errors | ±20% on hadrodisintegration and interconversion rates | high/mean/low runs | arXiv:2605.26824 | Sect. 3.5 |
| SBBN with that pipeline | Y_P = 0.2472 ± 0.0008; ³He/D = 0.410 ± 0.003 | AlterAlterBBN | arXiv:2605.26824 | Eqs. 78–79 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Negative ΔN_eff read with the dark-radiation formula.** Shows as a
  BBN preference for N_eff < 3 driven by Y_P; the consistent treatment
  removes the Y_P sensitivity (arXiv:2507.23354) [src: Sect. IV]. Test:
  state which T_ν(T_γ) the code used for ΔN_eff < 0.
- **ξ_ν from helium alone.** D/H constrains ξ_νe only if ω_b is supplied
  externally, since D/H ∝ ω_b^{−1.6} (arXiv:2208.03201) [src: Sect. II].
  Test: show the (ω_b, ξ_ν) contours with and without the CMB prior.
- **Rate set left implicit.** The sign of a preferred ξ_ν, or of an N_ν
  shift, can follow the D/H prediction of the code
  (arXiv:1801.08023) [src: Sect. VI.3]. Test: rerun with PRIMAT and with
  PArthENoPE or NACRE II rates, as Escudero et al. do.
- **Double counting.** The combined N_eff = 2.990 ± 0.070 already uses Y_P;
  Burns 2026 warns it "is not strictly independent of the abundance data"
  (arXiv:2603.22414) [src: Sect. 8]. Test: do not combine a published
  joint N_eff with the same abundances again.
- **Helium convention.** CMB chains and BBN codes define Y_P differently;
  both Yeh et al. and Goldstein & Hill convert explicitly
  (arXiv:2207.13133 [src: Sect. 3, footnote 8]; arXiv:2603.13226
  [src: footnote 2]).
- **Two-sided limit below the physical floor.** A best fit below N_ν = 3
  makes a two-sided upper limit too tight; report the one-sided limit
  normalised above 3 (arXiv:2207.13133) [src: Eq. 37].
- **Electromagnetic decays treated as purely electromagnetic.**
  Final-state radiation produces hadrons that interconvert n ↔ p at early
  times (arXiv:2605.26824) [src: Sect. 5.5]. Test: run the decay through
  a shower generator before the BBN code.
- **Validation used by the authors.** Sabti et al. check the modified
  background against default PRIMAT to < 0.1% (arXiv:1910.01649)
  [src: Sect. II.2]; Goldstein & Hill first reproduce the published
  BBN-only and Planck-only N_eff before adding data (arXiv:2603.13226)
  [src: Sect. III].

## Reading list
<!-- key: reading-list -->

- Pitrou et al. 2018, arXiv:1801.08023 (foundation): ξ_ν physics
  (Eqs. 157–164) and the N_ν–N_eff mapping (Eq. 165).
- Pisanti et al. 2008, arXiv:0705.0290 (code): how ΔN_eff and ξ are input
  in PArthENoPE.
- Yeh et al. 2022, arXiv:2207.13133 (method): separate and joint BBN and
  CMB likelihoods, Y_P marginalisation, one-sided limits.
- Ganguly, Jung & Yun 2025, arXiv:2507.23354 (critique): why negative
  ΔN_eff needs a modified T_ν and what remains of the BBN bound.
- Escudero et al. 2022, arXiv:2208.03201 (application): lepton asymmetry
  from Y_P, rate-set and helium-value dependence.
- Sabti et al. 2020, arXiv:1910.01649 (method): thermal relics through an
  external background, χ² with theory errors, model-independent ω_b.
- Bianco et al. 2026, arXiv:2605.26824 (method): decaying relics, regime
  by regime, with error treatment.
- Goldstein & Hill 2026, arXiv:2603.13226 (application): N_eff from
  abundances, CMB and BAO inside one sampler.
- Burns 2026, arXiv:2603.22414 (method): what a free ΔN_eff does to the
  error budget and to ω_b from abundances.

## Not verified
<!-- key: not-verified -->

- Kawasaki, Kohri & Moroi 2005 and Jedamzik 2006 (the decay foundations)
  were not re-read in body; their method is described here through
  arXiv:2605.26824.
- The D/H value used by Bianco et al. is printed in the HTML rendering as
  (25.08 ± 0.029) × 10⁻⁵ and the SBBN prediction as
  (25.23 ± 0.53) × 10⁻⁵; the units are inconsistent with the rest of the
  literature and these values are not quoted in the table.
- The limits on lifetimes and abundances of decaying relics from
  arXiv:2605.26824 (its Figs. 5–16) were not read.
- Grohs & Fuller 2023, Sect. 5, named in `subtopics.tsv`, was not read
  for this dossier.
