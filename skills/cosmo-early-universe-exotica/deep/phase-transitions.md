# First-order phase transitions: from transition parameters to a GW template and a fit — cosmo-early-universe-exotica dossier

Scope: how the four transition parameters are turned into a gravitational-
wave spectrum (kinetic efficiency, amplitude and peak-frequency formulae,
spectral shape, the sound-wave lifetime suppression, the redshift factor),
how PTA and LISA analyses fit such templates (free or fixed shapes,
geometric or thermodynamic parameters, foregrounds, dark-radiation
likelihood), and how large the theory error from the effective potential is;
the fitted values are in the reference files.
Snapshot: 2026-10-22.
From: LISA Cosmology WG 2022, Sect. 6 and 9.2.2; Carr et al. 2026 PBH
review, Sect. II.2.1; PTA new-physics papers.

Already in L2, not repeated here: the parameter definitions (T_*, α, β/H_*,
v_w) and the history of sources in
`physics-and-methods.md#first-order-phase-transitions`; NANOGrav's Bayes
factors and T_* intervals in `results.md#phase-transitions-and-the-pta-signal`;
the peak-factor, slope-prior, effective-potential and α-definition entries
in `systematics.md#theory-templates-for-cosmological-backgrounds`. The PTA
likelihood itself is in `deep/sgwb-pta.md`; how ΔN_eff enters BBN in
`cosmo-bbn` (`deep/neff-new-physics.md`).

## How it is done
<!-- key: how-it-is-done -->

Notation. T_* is the temperature at percolation (about 34% of the volume
converted; NANOGrav, arXiv:2306.16219, Sect. V.3); α_* (or α) the
transition strength; R_* the mean bubble separation, H_* the Hubble rate at
percolation, so H_*R_* is the separation in Hubble units; β the inverse
duration; v_w (ξ_w in the 2024 LISA paper) the wall speed; c_s the sound
speed; K the fraction of the total energy in bulk fluid kinetic energy; κ
the efficiency, normalised to the released vacuum energy. f is the GW
frequency today.

### Step 1. Fix the strength parameter and the efficiency
<!-- key: step-1-fix-the-strength-parameter-and-the -->

The bag model writes α = ε/(a_+ T⁴), with ε the bag constant and a_+ the
radiation coefficient in the symmetric phase (Caprini et al. 2020,
arXiv:1910.13125) [src: Eq. 9]; the kinetic energy fraction of one bubble
is K = κα/(1+α) [src: Eq. 11], with κ from the self-similar fluid profile
[src: Eq. 10]. Because the bag model is crude, the 2020 LISA paper adopts
the trace-based definition α_θ = (4/3) Δθ(T_n)/w_+(T_n), θ = (e − 3p)/4
the trace of the energy–momentum tensor, w_+ the enthalpy in the symmetric
phase [src: Eq. 12], on the argument that the hydrodynamics depends mainly
on Δθ even beyond the bag model [src: Sect. 2.2]. The alternative α_e uses
the energy difference [src: Eq. 13]; for strong transitions α ≈ α_θ ≈ α_e,
for weak ones Δe ≈ 4Δθ, so α_e "tends to overestimate the kinetic energy"
[src: Sect. 2.2].

NANOGrav defines α_* through the change of the trace across the transition
over the radiation density at percolation, and uses κ_s = α_*/(0.73 +
0.083√α_* + α_*) for the fraction going into sound waves [src:
arXiv:2306.16219, Sect. V.3]. The 2024 LISA pipeline instead uses K ≃
0.6 κα/(1+α): the 0.6 is the bulk-fluid efficiency relative to a single
bubble found in "Higgsless" simulations, described as conservative relative
to the 2020 report (Caprini et al. 2024, arXiv:2403.03723) [src: Sect.
2.2.1].

The bubble separation is related to β by H_*R_* = (8π)^(1/3) v_w H_*/β
(NANOGrav, with v_w = 1) [src: arXiv:2306.16219, Sect. V.3], or with
max(ξ_w, c_s) in place of v_w [src: arXiv:2403.03723, Eq. 11].

### Step 2. Choose which sources contribute
<!-- key: step-2-choose-which-sources-contribute -->

NANOGrav runs two separate analyses: pt-sound, assuming walls interact with
the plasma and do not run away, and pt-bubble, assuming runaway walls; it
says whether runaway occurs is "model dependent or affected by large
theoretical uncertainties" [src: arXiv:2306.16219, Sect. V.3]. Turbulence is
ignored as "usually subleading" [src: footnote 3]. The 2020 LISA report also
neglects turbulence "to be conservative", because its amplitude and shape
are not settled, while noting that most models of interest have shock
formation within a Hubble time and therefore likely turbulence [src:
arXiv:1910.13125, Sects. 3.2, 3.4]. EPTA, by contrast, fits a decaying
(M)HD-turbulence template at the QCD scale (arXiv:2306.16227) [src: Sect.
4.3.1].

### Step 3. Write the amplitude
<!-- key: step-3-write-the-amplitude -->

NANOGrav [src: arXiv:2306.16219, Eqs. 33–36]:

- Bubbles: Ω_b(f) = 𝒟 Ω̃_b (α_*/(1+α_*))² (H_*R_*)² 𝒮(f/f_b), Ω̃_b = 0.0049
  [src: arXiv:2306.16219, Eq. 33 and the text after Eq. 34].
- Sound waves: Ω_s(f) = 𝒟 Ω̃_s Υ(τ_sw) (κ_s α_*/(1+α_*))² (H_*R_*)
  𝒮(f/f_s), Ω̃_s = 0.036 [src: arXiv:2306.16219, Eq. 34 and the text after
  it].
- Redshift: 𝒟 = (π²/90)(T₀⁴/(M_Pl² H₀²)) g_* (g_*,s^eq/g_*,s)^(4/3) ≃ 1.67 ×
  10⁻⁵, with T₀ and H₀ today, g's at T_* and g_*,s^eq at matter–radiation
  equality [src: arXiv:2306.16219, Eq. 35].
- Lifetime suppression: Υ(τ_sw) = 1 − (1 + 2τ_sw H_*)^(−1/2), with τ_sw ≈
  R_*/Ū_f and Ū_f² ≈ 3κ_s α_*/[4(1+α_*)] the mean-square fluid velocity.

The 2020 LISA report [src: arXiv:1910.13125, Eqs. 19–20, 29, 32]:

- Today's factor F_gw,0 = Ω_γ,0 (g_s0/g_s*)^(4/3) g_*/g_0 = (3.57 ± 0.05) ×
  10⁻⁵ (100/g_*)^(1/3) [src: arXiv:1910.13125, Eqs. 19–20].
- Long-lasting sound waves: dΩ_gw,0/d ln f = 0.687 F_gw,0 K² (H_*R_*/c_s)
  Ω̃_gw C(f/f_p,0), Ω̃_gw ~ 10⁻² from simulations [src: arXiv:1910.13125,
  Eq. 29 and the text after it, Sect. 3.3].
- If the shock time H_*τ_sh = H_*R_*/K^(1/2) is below one: multiply by it,
  giving K^(3/2)(H_*R_*/√c_s)² instead of K²(H_*R_*/c_s).

The 2024 LISA pipeline [src: arXiv:2403.03723, Eq. 10]: h²Ω_int = h²F_GW,0
A_sw K² (H_*τ_sw)(H_*R_*), A_sw ≃ 0.11 averaged over simulations, H_*τ_sw =
min[H_*τ_sh, 1], H_*τ_sh = H_*R_*/√(v̄_f²), v̄_f² = K/Γ with Γ = 4/3 [src:
Sect. 2.2.1].

Why the suppression matters: in the long-lasting case Ω ∝ K²(H_*R_*),
in the short-lived one Ω ∝ K^(3/2)(H_*R_*)² [src: arXiv:1910.13125, Eqs.
25–26]; since H_*R_* < 1, omitting the factor overestimates the signal of
strong, slow transitions, which is "typically used in the literature" [src:
Sect. 3.3].

### Step 4. Write the peak frequency and the shape
<!-- key: step-4-write-the-peak-frequency-and-the-shape -->

- NANOGrav: f_{b,s} ≃ 48.5 nHz g_*^(1/2)(g_*,s^eq/g_*,s)^(1/3)(T_*/GeV)
  f*_{b,s}R_*/(H_*R_*), with f*_b = 0.58/R_* and f*_s = 1.58/R_* at emission
  [src: arXiv:2306.16219, Eq. 37]; shape 𝒮(x) = (1/𝒩)(a+b)^c/(b x^(−a/c) + a
  x^(b/c))^c, with a and b the low- and high-frequency slopes, c the peak
  width and 𝒩 a normalisation making the log-integral unity [src: Eqs.
  38–39]. a, b, c float within the Table 3 priors "to roughly reflect the
  typical uncertainties of numerical simulations" [src: Sect. V.3].
- 2020 LISA: C(s) = s³ (7/(4+3s²))^(7/2) [src: arXiv:1910.13125, Eq. 30],
  peak f_p,0 ≃ 26 (1/H_*R_*)(z_p/10)(T_*/100 GeV)(g_*/100)^(1/6) μHz, z_p ≃
  10 from simulations [src: Eq. 31]. The shape fails near the
  Chapman–Jouguet speed, where sound shells are thin [src: Sect. 3.3].
- 2024 LISA: a double broken power law with breaks f₁ ≃ 0.2 H_*,0
  (H_*R_*)⁻¹ (bubble size) and f₂ ≃ 0.5 H_*,0 Δ_w⁻¹ (H_*R_*)⁻¹ (shell
  thickness Δ_w = ξ_shell/max(ξ_w, c_s)), slopes n₁ = 3, n₂ = 1, n₃ = −3
  and smoothness a₁ = 2, a₂ = 4 [src: arXiv:2403.03723, Eqs. 8–9, Sect.
  2.2.1]; Ω₂ ≈ 0.55 Ω_int for ξ_w ≈ 1 [src: Eq. 12]. Strong supercooled
  transitions use a single broken power law for bubble collisions and
  highly relativistic fluid shells [src: Sect. 2.1].

### Step 5. Fit
<!-- key: step-5-fit -->

- **NANOGrav (PTA).** Free parameters log₁₀(T_*/GeV) ∈ [−4, 4], log₁₀ α_* ∈
  [−2, 1], log₁₀ H_*R_* ∈ [−3, 0], plus a, b, c (pt-bubble: a, b, c ∈ [1,
  3]; pt-sound: a ∈ [3, 5], b ∈ [2, 4], c ∈ [3, 5]), with v_w = 1 fixed
  [src: arXiv:2306.16219, Table 3, Sect. V.3]. Each model is fitted alone
  and with the SMBHB term. Fixing v_w = 1 is called "the optimistic
  assumption" for sound waves, where a subluminal terminal velocity is
  expected, and is justified because the remaining v_w dependence sits in
  κ_s and is weak for the preferred α_* ~ 0.3–10 [src: Sect. V.3].
- **EPTA (PTA, turbulence).** A fast free-spectrum fit on the first nine
  bins of DR2new with log-uniform priors log₁₀(λ_*ℋ_*) ∈ [−3, 0], log₁₀ Ω_*
  ∈ [−2, 0], log₁₀(T_*/MeV) ∈ [1, 3], where Ω_* is the turbulent energy
  fraction and λ_*ℋ_* the turbulence scale in Hubble units [src:
  arXiv:2306.16227, Sect. 4.3.2]; amplitude Ω_GW = 3𝒜 Ω_*²(λ_*ℋ_*)² F_GW,0
  S_turb, 𝒜 ≃ 1.75 × 10⁻³, F_GW,0 ≃ 8 × 10⁻⁵ (10/g_*)^(1/3) [src: Eqs.
  21–22].
- **Other groups, other data.**
  - *NANOGrav 15 yr, strong transitions* (Ellis et al. 2023,
    arXiv:2308.08546): α ≫ 1 is assumed, where fluid and bubble sources
    behave alike, with one broken power law (a = b = 2.4, c = 4, A = 5.1 ×
    10⁻², f_p = 0.7 f_H(T_*) β/H) times a function S_H that turns the
    spectrum into the causality tail beyond the horizon scale, its
    sharpness δ fixed to 1 after checking it matters little [src: Sect.
    III.2, Eqs. 19–20]. Free parameters are T_* and β/H only.
  - *NANOGrav 15 yr + EPTA DR2new free spectra* (Figueroa et al. 2023,
    arXiv:2307.02399): phase transitions among seven source classes, the
    two data sets treated as independent, bin-averaged templates and an
    extra flat component (method in `deep/scalar-induced-gw.md`, Step 4)
    [src: main text; SM Sect. I].
  - *CPTA DR1* (Wang 2023, arXiv:2307.15970): four parameters {T_*, α_*,
    H_*/β, η}, η a friction parameter, alone ("PTO") or with SMBHBs
    ("PTBBH", nine parameters, Planck 2018 background) [src: Sect. IV].
  - *HD free spectra of EPTA, PPTA and NANOGrav* (Bian et al. 2023,
    arXiv:2307.02376), with strings, domain walls and curvature
    perturbations as alternatives [src: abstract].
  - *NANOGrav 15 yr and IPTA DR2 from a Lagrangian* (Puchades-Ibáñez &
    Schwaller 2026, arXiv:2609.12098): a classically conformal Abelian
    Higgs model with the nucleation rate at NLO in the dimensionally reduced
    theory, propagated through percolation, reheating and GW production
    [src: abstract].
- **Dark-radiation likelihood (Bringmann et al. 2023, arXiv:2306.09411).**
  The PTA likelihood is multiplied by ℒ_cosmo [src: Sect. 4]. For a stable
  dark sector, ℒ_cosmo is a Gaussian in N_eff = 3.044 + ΔN_eff(θ_DS) with
  measured N_eff = 2.941 ± 0.143 [src: Eq. 15]; for a dark sector decaying
  into photons or electrons, the mediator mass is fixed to 5 MeV and the
  lifetime τ_φ sampled, with a BBN + CMB likelihood [src: Sect. 4.2]. The
  GWs themselves contribute ΔN_eff ≲ 10⁻³ and are irrelevant to this bound
  [src: footnote 8].
- **LISA (forecast).** SGWBinner simulates data with instrument noise
  (test-mass and optical-metrology amplitudes A = 3, P = 15, 20% Gaussian
  priors), an extragalactic compact-binary foreground log₁₀(h²Ω_Ext) =
  −12.38 ± 0.17 at 1 mHz with slope 2/3, and a Galactic foreground
  integrated over the mission, without using its yearly modulation, which
  the authors call conservative [src: arXiv:2403.03723, Sect. 3.3].
  Templates are fitted either in geometric parameters (amplitude, breaks)
  or in thermodynamic ones; the two agree after conversion "provided one
  takes care to discard the regions ... leading to unphysical values for
  the thermodynamic ones" [src: Sect. 7].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Sound waves or bubble collisions
<!-- key: sound-waves-or-bubble-collisions -->

The two templates give different T_* for the same data, partly from f*_b =
0.58/R_* against f*_s = 1.58/R_*, partly from the low-slope prior: a can go
down to 1 for pt-bubble, which lets a peak above the band still feed the
lowest bins [src: arXiv:2306.16219, Sect. V.3]. With a = 3 fixed by
causality the two T_* posteriors move closer; pt-sound shows "very minor
differences", pt-bubble moves to slightly smaller T_* [src: App. C.3].
pt-sound alone struggles with the lowest bins; adding SMBHBs helps it
(Bayes factor 3.7 → 6.5) and opens a plateau where SMBHBs carry the signal
[src: Sect. V.3].

### Same data, different conclusions
<!-- key: same-data-different-conclusions -->

- **Ellis et al. on NANOGrav 15 yr**: pure transition best fit T_* = 0.34
  GeV, β/H = 6.0, −2Δℓ = −2.3 against the SMBHB baseline; with SMBHBs
  (environmental effects included) the fit is dominated by the transition,
  and requiring ≥ 5% probability for the 4 nHz candidate event gives T_* =
  2.6 GeV, β/H = 4.0 [src: arXiv:2308.08546, Sect. III.2, Eqs. 21–22].
  ΔBIC = −4.9 against SMBHBs with environment (2.9 when the two are
  combined); the combined fit beats SMBHBs alone only for phase
  transitions and domain walls [src: Sect. IV, Table 1]. PBH overproduction
  requires β/H ≳ 4 (≳ 6 in another reference they cite), and most of the
  1σ region passes [src: Sect. III.2].
- **Figueroa et al. on NANOGrav + EPTA**: SIGWs and, less so, audible axions
  and superstrings have the largest Bayes factors against SMBHBs; phase
  transitions are among "the remaining models" with lower BF and AIC [src:
  arXiv:2307.02399, main text].
- **CPTA DR1**: 2σ range T_* ∈ [1.3 MeV, 29.5 GeV], against [1 MeV, 100
  GeV] for NANOGrav 12.5 yr; H_*/β > 0.014, α_* > 0.21, η < 8.12 (2σ);
  "slightly tighter" than NANOGrav 12.5 yr, weaker than 15 yr; the
  integrated bound Ω̃_GW < 10⁻⁶ (CMB, BBN, astrometry) barely helps, and
  adding SMBHBs loosens all four parameters [src: arXiv:2307.15970, Sect.
  IV].
- **Bian et al. on three arrays**: no strong preference for any source
  [src: arXiv:2307.02376, abstract].

### Free or fixed spectral shape
<!-- key: free-or-fixed-spectral-shape -->

NANOGrav floats a, b, c to absorb double-peak features seen in simulations
and model dependence [src: Sect. V.3, footnote 4]; the cost is a template
whose low-frequency slope can violate causality (a < 3). The posterior of a
peaks near 2 for pt-bubble (the slope of the signal) and at the prior edge
3 for pt-sound [src: App. C.3]. The LISA pipeline fixes all slopes from
simulations and frees only amplitude and break frequencies, which reduces
degeneracies and eases sampling [src: arXiv:2403.03723, Sects. 2.2.1, 7].

### Lifetime suppression: three conventions
<!-- key: lifetime-suppression-three-conventions -->

NANOGrav's smooth Υ = 1 − (1+2τ_swH_*)^(−1/2) [src: arXiv:2306.16219, Eq.
36]; the 2020 LISA switch between Eq. 29 and Eq. 32 at H_*τ_sh = 1 [src:
arXiv:1910.13125, Sect. 3.3]; the 2024 LISA min[H_*τ_sh, 1] [src:
arXiv:2403.03723, Sect. 2.2.1]. Note that NANOGrav's τ_sw uses Ū_f² ≈
3κ_sα_*/[4(1+α_*)] while LISA 2024 uses v̄_f² = K/Γ with K ≃ 0.6 κ α/(1+α)
[src: arXiv:2403.03723, Sect. 2.2.1].

In the short-lifetime limit the three conventions agree to leading order
and differ by order-unity factors when the lifetime approaches a Hubble
time [der: expansion of NANOGrav's smooth Υ].

### Efficiency normalisation
<!-- key: efficiency-normalisation -->

NANOGrav's amplitude carries the single-bubble κ_s squared, (κ_sα_*/(1+α_*))²
[src: arXiv:2306.16219, Eq. 34], while LISA 2024 uses K ≃ 0.6 κ α/(1+α),
the 0.6 accounting for the efficiency of bulk fluid motion relative to the
single bubble [src: arXiv:2403.03723, Sect. 2.2.1].

Because the efficiency enters the amplitude squared, the LISA 2024 factor
lowers Ω_sw relative to the NANOGrav convention [der]. NANOGrav argues such prefactors
are absorbed by a rescaled α_* in a fit, and peak-frequency factors by a
rescaled T_* [src: arXiv:2306.16219, Sect. V.3]; the absorption holds for
fit quality, not for the physical α_* or T_* quoted.

### Geometric or thermodynamic parameters
<!-- key: geometric-or-thermodynamic-parameters -->

Geometric parameters (Ω_p or Ω₂, f₁, f₂) are less degenerate; thermodynamic
ones (K, H_*R_*, ξ_w, T_*) carry the physics but are degenerate [src:
arXiv:2403.03723, Sect. 7]. In the PTA fit, log₁₀T_* and log₁₀H_*R_* are
linearly correlated through the peak frequency, and for α_* ≲ 1 α_* ~
1/(H_*R_*) (bubbles) or α_*² ~ 1/(H_*R_*) (sound) through the amplitude
[src: arXiv:2306.16219, Sect. V.3].

### Stable or decaying dark sector
<!-- key: stable-or-decaying-dark-sector -->

A stable dark sector at MeV temperatures adds ΔN_eff and is constrained by
BBN and CMB; a decaying one transfers its energy to the Standard Model and
depends on the lifetime: for a Higgs-mixed scalar, laboratory limits give
τ_φ ≳ 10⁻² s while cosmology requires τ_φ ≲ 10⁻¹ s, leaving a window [src:
arXiv:2306.09411, Sect. 4.2]. With the 15 yr data, NANOGrav's higher T_*
"allows the phase transition signal to safely evade bounds from BBN and CMB"
around T_* ~ 1 MeV [src: arXiv:2306.16219, Sect. V.3].

### How the transition parameters are computed from a Lagrangian
<!-- key: how-the-transition-parameters-are-computed-from -->

Daisy-resummed perturbation theory has renormalisation-scale dependence
that amounts to two to three orders of magnitude in the peak amplitude;
dimensional reduction to a 3D effective theory reduces it and is gauge
invariant (Croon et al. 2020, arXiv:2009.10080) [src: abstract]. For
supercooled conformal U(1) models, a Fisher forecast at LISA finds the
daisy scheme's theory error larger than the reconstruction error (Kierkla
et al. 2026, arXiv:2607.18233) [src: abstract]; a 3D EFT with consistent
running reduces scale dependence, while simple analytic bounce-action
parametrisations deviate at large supercooling (Christiansen et al. 2025,
arXiv:2511.02910) [src: abstract]. The 2024 LISA paper states that
inference from a Lagrangian to data is "prohibitive" with current tools and
maps models through thermodynamic parameters instead [src:
arXiv:2403.03723, Sect. 7]. TransitionListener v2.0 (arXiv:2605.15259)
provides a potential-to-spectrum pipeline with true-vacuum fraction,
backreaction on expansion, reheating and PTA likelihood interfaces [src:
abstract]. Fitting NANOGrav 15 yr and IPTA DR2, the NLO nucleation rate
shifts the preferred gauge coupling by 9% and 13% and the input scale by
18% (NANOGrav); after calibrating the determinant, the largest remaining
uncertainties are the GW spectra and the R_*–β/H relation [src:
arXiv:2609.12098, abstract].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Amplitude constants | Ω̃_b = 0.0049, Ω̃_s = 0.036 | NANOGrav templates | arXiv:2306.16219 | Sect. V.3 |
| Peak at emission | f*_b = 0.58/R_*, f*_s = 1.58/R_* | NANOGrav | arXiv:2306.16219 | Sect. V.3 |
| Redshift factor | 𝒟 ≃ 1.67 × 10⁻⁵ | NANOGrav | arXiv:2306.16219 | Eq. 35 |
| Sound-wave efficiency | κ_s = α_*/(0.73 + 0.083√α_* + α_*) | NANOGrav | arXiv:2306.16219 | Sect. V.3 |
| PT priors | log₁₀ T_*/GeV ∈ [−4, 4]; log₁₀ α_* ∈ [−2, 1]; log₁₀ H_*R_* ∈ [−3, 0] | NANOGrav | arXiv:2306.16219 | Table 3 |
| α_*, H_*R_* posteriors | pt-bubble α_* > 1.1 (0.29), H_*R_* > 0.28 (0.14); pt-sound α_* > 0.42 (0.37), H_*R_* ∈ [0.053, 0.27] ([0.046, 0.89]) at 68% (95%) | NANOGrav 15 yr | arXiv:2306.16219 | Sect. V.3 |
| Today's factor | F_gw,0 = (3.57 ± 0.05) × 10⁻⁵ (100/g_*)^(1/3) | LISA 2020 | arXiv:1910.13125 | Eq. 20 |
| Sound-wave constants | Ω̃_gw ~ 10⁻², z_p ≃ 10 | LISA 2020 | arXiv:1910.13125 | Sect. 3.3 |
| Vorticity fraction | ε = K_⊥/K = 0.05 (valid for Ū_f ≲ 0.05) | earlier LISA report, as discussed | arXiv:1910.13125 | Sect. 3.2 |
| Sound-wave constants (2024) | A_sw ≃ 0.11; K ≃ 0.6 κα/(1+α); n₁, n₂, n₃ = 3, 1, −3 | LISA 2024 | arXiv:2403.03723 | Sect. 2.2.1 |
| LISA reconstruction | ≲ 10% relative errors (68%) for Ω_p ≳ 10⁻¹² at ~3 mHz; ≳ 10⁻¹³ if the Galactic foreground were fully removed — **forecast** | LISA 2024 | arXiv:2403.03723 | Sect. 7 |
| Nucleation criteria | S_c ≃ 140 (onset, EW scale); percolation Eq. 5 | LISA 2020 | arXiv:1910.13125 | Eqs. 3–5 |
| Turbulence efficiency | 𝒜 ≃ 1.75 × 10⁻³ (decaying stage only, conservative) | EPTA | arXiv:2306.16227 | Sect. 4.3.1 |
| Strong-PT template | a = b = 2.4, c = 4, A = 5.1 × 10⁻², f_p = 0.7 f_H β/H | Ellis et al., NG15 | arXiv:2308.08546 | Eq. 19 |
| Strong-PT best fit | T_* = 0.34 GeV, β/H = 6.0; ΔBIC −4.9 | Ellis et al., NG15 | arXiv:2308.08546 | Eq. 21, Table 1 |
| CPTA PT range | T_* ∈ [1.3 MeV, 29.5 GeV] (2σ); α_* > 0.21; H_*/β > 0.014 | CPTA DR1, Wang | arXiv:2307.15970 | Sect. IV |
| NLO nucleation shift | gauge coupling 9% (NG15), 13% (IPTA DR2); scale 18% | conformal U(1) | arXiv:2609.12098 | abstract |
| N_eff likelihood | 2.941 ± 0.143 (Gaussian) | Bringmann et al. | arXiv:2306.09411 | Sect. 4.1 |
| Daisy-scheme theory error | two to three orders of magnitude in peak amplitude | SMEFT study | arXiv:2009.10080 | abstract |

## What goes wrong
<!-- key: what-goes-wrong -->

- **No lifetime suppression.** Using Eq. 29-type amplitudes when H_*τ_sh <
  1 overestimates the signal; most models of interest are in that regime
  [src: arXiv:1910.13125, Sect. 3.3]. Test: compute H_*τ_sh from K and
  H_*R_* and state which convention is applied.
- **Mixed α definitions.** α from the energy difference used with κ fits
  calibrated on Δθ overestimates K for weak transitions [src:
  arXiv:1910.13125, Sect. 2.2]. Test: state the definition and the κ fit.
- **Peak-frequency and amplitude factors read physically.** T_* and α_*
  posteriors absorb template prefactors [src: arXiv:2306.16219, Sect.
  V.3]. Test: compare T_* only within one template; when mapping to a
  model, redo the fit with that model's template.
- **Acausal low-frequency slope.** a < 3 fits better but conflicts with
  causality unless a double peak is physical [src: App. C.3]. Test: refit
  with a = 3 and report both.
- **v_w = 1 assumed for sound waves.** Optimistic [src: arXiv:2306.16219,
  Sect. V.3]; the sound-wave shape also fails near the Chapman–Jouguet
  speed [src: arXiv:1910.13125, Sect. 3.3]. Test: vary v_w or restrict to
  regimes where the template was simulated.
- **Turbulence neglected or added ad hoc.** Its amplitude and shape are
  unsettled [src: arXiv:1910.13125, Sect. 3.2]; EPTA's template is
  validated only for Ω_* ≲ 0.1, yet its fit prefers Ω_* near 1 [src:
  arXiv:2306.16227, Sects. 4.3.1–4.3.2]. Test: report fits with and
  without turbulence, and the validity range of the template.
- **MeV-scale dark sectors without a dark-radiation likelihood.** Test:
  multiply by ℒ_cosmo (stable) or a BBN + CMB lifetime likelihood
  (decaying) [src: arXiv:2306.09411, Sect. 4].
- **Theory error ignored when mapping to a Lagrangian.** Test: compute the
  parameters with a dimensionally reduced 3D EFT or quote the scale
  dependence [src: arXiv:2009.10080; arXiv:2607.18233].
- **Forecast foregrounds matched to the injection.** The LISA forecast
  injects and fits the same templates, so its errors hold only if theory
  and instrument uncertainties shrink below statistical errors [src:
  arXiv:2403.03723, Sect. 7].

## Reading list
<!-- key: reading-list -->

- Method and application: Afzal et al. 2023, arXiv:2306.16219 — PTA
  templates, priors, posteriors, the a = 3 test (Sect. V.3, App. C.3).
- Method: Caprini et al. 2020, arXiv:1910.13125 — α definitions, κ, time
  scales, sound-wave formulae with and without shocks (Sects. 2–3).
- Method and forecast: Caprini et al. 2024, arXiv:2403.03723 — double
  broken power law, LISA foregrounds and noise priors, geometric versus
  thermodynamic fits.
- Foundation: Hindmarsh et al. 2014, arXiv:1304.2433 — sound waves as the
  main source.
- Application: Antoniadis et al. 2023, arXiv:2306.16227 — turbulence
  template and free-spectrum fit (Sect. 4.3).
- Method: Bringmann et al. 2023, arXiv:2306.09411 — cosmological
  likelihood for stable and decaying dark sectors.
- Critique: Croon et al. 2020, arXiv:2009.10080 — perturbative theory
  error (abstract).
- Critique: Kierkla et al. 2026, arXiv:2607.18233; Christiansen et al.
  2025, arXiv:2511.02910 — resummation schemes for supercooled transitions
  (abstracts).
- Comparison: Ellis et al. 2023, arXiv:2308.08546 — strong-transition
  template and BIC ranking against other sources on the NANOGrav data.
- Application: Figueroa et al. 2023, arXiv:2307.02399 — NANOGrav + EPTA,
  seven source classes.
- Application: Wang 2023, arXiv:2307.15970 — the CPTA DR1 fit.
- Application: Bian et al. 2023, arXiv:2307.02376 — three arrays' free
  spectra (abstract).
- Critique: Puchades-Ibáñez & Schwaller 2026, arXiv:2609.12098 — NLO
  nucleation on NANOGrav and IPTA DR2 (abstract).
- Code: Matuszak & Tasillo 2026, arXiv:2605.15259 — TransitionListener
  v2.0 (abstract).

## Not verified
<!-- key: not-verified -->

- The source of NANOGrav's κ_s fit (its Ref. [116]) and of Υ (its Ref.
  [302]) were not read; the formulae are reported as NANOGrav writes them.
- The 2024 LISA turbulence template (Sect. 2.2.2) and the thermodynamic-
  parameter reconstruction results (Sect. 5) were not read.
- Bodies of arXiv:2009.10080, arXiv:2607.18233, arXiv:2511.02910 and
  arXiv:2605.15259 were not read; only abstracts.
- No phase-transition fit to PPTA DR3 or MPTA data by the collaborations
  was found (one search, 2024 onwards). Which CPTA data product Wang fits
  (the collaboration gives correlations at single frequencies) was not
  read; nor the phase-transition results of Figueroa et al. beyond the
  ranking.
- The LISA Cosmology WG 2022 Sect. 6 body beyond what L2 quotes was not
  re-read.
