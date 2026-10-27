# BBN codes and their agreement — cosmo-bbn dossier

Scope: how a BBN code turns (η, N_eff, τ_n, nuclear rates) into abundances
— background thermodynamics, weak n ↔ p rates and their corrections,
staged nuclear network, integrator, rate sampling — what each public code
includes, how large each omitted piece is, how far the codes agree when
their inputs are aligned, and how a code is coupled to a sampler.
Snapshot: 2026-10-18.
From: Cooke 2024, Sect. 6.2 (BBN theory and calculations); code papers of
PArthENoPE, PRIMAT, AlterBBN, PRyMordial, LINX.

Already in L2, not repeated here: the code table (language, rate
philosophy, references) in `physics-and-methods.md#bbn-codes`; the
abundance scalings with η, N_ν and τ_n in
`physics-and-methods.md#what-bbn-measures`; the Ω_b h² obtained with each
rate set in `results.md#code-and-rate-comparisons`; how laboratory
S-factors become rates, lognormal rate sampling and the full versus
summarised BBN likelihood in `deep/nuclear-reaction-rates.md`.

Notation. η = n_b/n_γ (baryon-to-photon ratio), η₁₀ = 10¹⁰ η; ω_b = Ω_b h²;
T the photon (plasma) temperature, T₉ = T/(10⁹ K); T_ν the neutrino
temperature; Y_i = n_i/n_b the yield of nuclide i; Y_P the primordial ⁴He
mass fraction, defined in the codes as 4 Y(⁴He); τ_n the neutron lifetime;
g_A the nucleon axial coupling; ΔY_P^(4) ≡ 10⁴ ΔY_P, the unit PRIMAT uses
for corrections. <!-- num: not a value -->

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Solve the background
<!-- key: step-1-solve-the-background -->

The code first computes the plasma and neutrino thermodynamics and the
expansion, then uses T(t) in all rates.

- **PRIMAT** obtains a(T) from entropy conservation, or from the entropy
  change caused by heat transfer to neutrinos when incomplete decoupling is
  included; inverts it to T(a); solves the Friedmann equation for a(t); and
  so gets T(t) (Pitrou et al. 2018, arXiv:1801.08023) [src: Sect. V.1].
  It integrates in time, "instead of integrating differential equations in
  the plasma temperature" as PArthENoPE and AlterBBN do [src: Sect. V.1].
  The 2021 paper corrects this for AlterBBN: PRIMAT integrates in time "as
  also does AlterBBN", PArthENoPE in plasma temperature, and "both methods
  are of course equivalent" (Pitrou et al. 2021, arXiv:2011.11320)
  [src: Sect. 1].
- **PArthENoPE** evolves the electron chemical-potential variable φ_e and
  the mass fractions X_i as functions of z = m_e/T (its Eqs. 13–14), from
  z_in = m_e/(10 MeV), with nucleons in weak equilibrium,
  X_n = (exp(q̂ z_in) + 1)⁻¹ with q̂ = (M_n − M_p)/m_e (Eq. 18), and nuclei at
  their nuclear-statistical-equilibrium (NSE) values (Eq. 20), applied only
  above the numerical zero YMIN = 10⁻³⁰ (Pisanti et al. 2008,
  arXiv:0705.0290) [src: Sect. II.2]. Entropy transfer during e⁺e⁻
  annihilation is followed instead of imposing entropy conservation
  [src: Sect. V].
- **LINX** integrates in time with no preset end point and does not use
  entropy conservation; it stops when T falls below 5.2 keV by default
  (Giovanetti et al. 2024, arXiv:2408.14538) [src: Sect. IV.1, item 3].
- **PRyMordial** computes T, T_ν, a(T) and N_eff by solving coupled
  Boltzmann equations for the energy densities, and can store the
  background for later runs (Burns, Tait & Valli 2024, arXiv:2307.07061)
  [src: Sect. 3.2]; Burns 2026 (arXiv:2603.22414) describes the same three
  stages [src: Sect. 3].

### Step 2. Compute the weak n ↔ p rates
<!-- key: step-2-compute-the-weak-n-p-rates -->

The Born rates (infinite nucleon mass) are phase-space integrals over
electron and neutrino distributions,

    Γ_{n→p}^∞ = G̃_F² ∫ dE_e E_e √(E_e² − m_e²) (E_ν⁻)² [f_ν(E_ν⁻) f_e(−E_e) + f_ν(−E_ν⁻) f_e(E_e)]

with E_ν^± = E_e ± Q, Q = m_n − m_p, and G̃_F² = N/m_e⁵, where N is a
normalisation factor (Burns 2026, arXiv:2603.22414) [src: Sect. 3, Eq. 6];
Γ_{p→n} is the same with E_ν⁺. Two normalisations exist:

- **τ_n normalisation.** All rates are proportional to 1/τ_n, so τ_n is a
  single measured nuisance fixing their magnitude; LINX does this, and
  notes that other anchors "are currently regarded as less precise"
  (arXiv:2408.14538) [src: Sect. III.3.1]. PRIMAT fixes the constant K of all
  rates from its Eq. 90 with the free-neutron decay rate λ₀ of its
  Eq. 119 [src: arXiv:1801.08023, Sect. V.1; Sect. III.3 title
  "Calibration from free neutron decay rate"].
- **Fundamental normalisation** from g_A, V_ud and G_F; PRyMordial lets the
  user switch (arXiv:2408.14538, footnote 6) [src: Sect. III.3.1], and
  Burns 2026 runs both [src: Tables 8–9].

Corrections are then added. PRIMAT's Table 5 gives each one at its
baseline η (arXiv:1801.08023) [src: Table 5, Sect. V.3]:

| Corrections included | Y_P | ΔY_P^(4) from Born | 10⁵ D/H |
|---|---|---|---|
| Born | 0.24262 | 0 | 2.423 |
| Born + incomplete decoupling (ID) | 0.24274 | 1.2 | 2.432 |
| Born + finite nucleon mass (FM) + weak magnetism (WM) | 0.24390 | 12.8 | 2.430 |
| zero-temperature radiative corrections (RC, resummed, relativistic Fermi function) | 0.24577 | 31.5 | 2.440 |
| RC + FM + WM | 0.24705 | 44.3 | 2.447 |
| RC + FM + WM + finite-T radiative (ThRC), no bremsstrahlung | 0.24736 | 47.4 | 2.449 |
| RC + FM + WM + ThRC + bremsstrahlung (BS) | 0.24705 | 44.3 | 2.447 |
| all, + ID + QED plasma | 0.24709 | 44.7 | 2.459 |

The corrections raise Y_P by 1.84% in total [src: Table 5]. LINX
reproduces the pattern with its own implementation: Born 0.24279,
RC + FM + WM 0.24715, "approximately 2%" in all (arXiv:2408.14538)
[src: Sect. III.3.1, Table 2].

PArthENoPE and AlterBBN instead "rely on" the fit of Appendix C of
Serpico et al. 2004 for the weak rates (arXiv:2011.11320) [src: Sect. 1];
PArthENoPE already included finite nucleon mass and non-thermal neutrino
spectra in those fits "not as effective corrections added a posteriori"
(arXiv:0705.0290) [src: Sect. V]. The PRIMAT authors state that weak rates
"differ by less than 0.2% between e.g. PRIMAT and PArthENoPE"
(arXiv:2011.11320) [src: Discussion].

### Step 3. Integrate the network in stages
<!-- key: step-3-integrate-the-network-in-stages -->

The network is a set of Boltzmann equations for the yields,

    dY_i/dt = Σ_R S_{i,R} [ Γ^(R)_{…→i…} Π_j Y_j^{S_{j,R}}/S_{j,R}! − Γ^(R)_{i…→…} Π_k Y_k^{S_{k,R}}/S_{k,R}! ]

with S_{i,R} the stoichiometric coefficient of species i in reaction R
(arXiv:2307.07061) [src: Eq. 2.16]. Only forward rates are tabulated;
reverse rates follow from detailed balance as
⟨σv⟩_rev = α_R T₉^{β_R} exp(γ_R/T₉) ⟨σv⟩_fwd, with α_R, β_R, γ_R set by
masses and spins [src: Eq. 2.19]. The integration is split because the
system is stiff (arXiv:1801.08023, Sect. V.1; arXiv:2307.07061, Sect. 2.3):

| Stage | PRIMAT (arXiv:1801.08023, Sect. V.1) | PRyMordial (arXiv:2307.07061, Sect. 2.3) |
|---|---|---|
| 1 | 10¹¹ ≥ T ≥ 10¹⁰ K: n and p only, nuclear rates "not tabulated above 10¹⁰ K" | from O(10) MeV to weak freeze-out near 1 MeV, n ↔ p only |
| 2 | 10¹⁰ ≥ T ≥ 1.25 × 10⁹ K: n, p, ²H, ³H, ³He, ⁴He, ⁶Li, ⁷Li, ⁷Be from NSE; first-order backward differentiation (BDF, backward Euler) because "very stiff" | 18 key rates, nuclides up to A = 8, Z = 5, down to ~0.1 MeV where D photodissociation stops |
| 3 | 1.25 × 10⁹ ≥ T ≥ 6 × 10⁷ K: full network, second-order BDF "to fasten" the integration | full set to O(keV), after e⁺e⁻ annihilation |

PArthENoPE replaced the single-step Runge–Kutta of the Kawano code with a
multistep BDF method, tuned so that the relative accuracy on Y_P is
~10⁻⁴, "below the level of theoretical uncertainties" (arXiv:0705.0290)
[src: Sect. V]. AlterBBN offers a choice of integrators through a
`failsafe` switch (Appendix B of its paper); the HTML rendering read is a
later arXiv version than v1 (Arbey et al., arXiv:1806.11095)
[src: Appendices B–C].

Network sizes: PRyMordial 12 key reactions (small network) or 63
(large) (arXiv:2307.07061) [src: Sect. 2.3]; LINX "key" or "full", the
full one with 61 reactions; PRIMAT's full network 422 reactions with
nuclides up to ²³Na (arXiv:2408.14538) [src: Sect. IV.1]. Burns 2026
finds only 12 of the 63 PRyMordial reactions move any abundance by
≥ 0.001% for a 1% rate change (arXiv:2603.22414) [src: Sect. 3].

### Step 4. Sample the inputs
<!-- key: step-4-sample-the-inputs -->

PRIMAT draws rates from lognormal distributions (its Eq. 146) and τ_n from
a normal one, 20 000 Monte Carlo points, and quotes quantiles
(arXiv:1801.08023) [src: Sect. V.5, Table 7]; PRyMordial's Eq. 2.22 and
LINX's Eq. 10 use the same form with one temperature-independent N(0, 1)
coefficient per reaction (details in `deep/nuclear-reaction-rates.md`).
AlterBBN has five modes: central rates (err = 0), all rates high (1) or
low (2) together, a covariance matrix from one-at-a-time variations (3),
and Gaussian random rates (4), the last commented out by default because
of run time, niter = 1000 (arXiv:1806.11095) [src: Sect. 3.3]. The
authors use err = 0 for conservative limits and err = 3 for χ² analyses
[src: Sect. 3.3].

To propagate a CMB prior, PRIMAT approximates P(Y_i | ω_b) by a Gaussian
N[Ȳ_i(ω_b), σ_i^th(ω_b)] (Eq. 147) and marginalises over ω_b (Eqs.
149–150), in practice by drawing ω_b in the same Monte Carlo
[src: Sect. V.5].

### Step 5. Report the outputs in the right convention
<!-- key: step-5-report-the-outputs-in-the-right -->

Y_P ≡ 4 Y(⁴He) ≃ ρ(⁴He)/ρ_b (PRyMordial Eq. 2.20) "differs at the
sub-percent level" from the CMB helium mass fraction, which uses atomic
masses (arXiv:2307.07061) [src: footnote 8]. Planck quotes the BBN
nucleon fraction Y_P^BBN ≈ 0.2467 against a CMB mass fraction
Y_P ≈ 0.2454 for its ΛCDM fit (Planck 2018, arXiv:1807.06209)
[src: Sect. 2.1]. In the LINX–PRyMordial–PRIMAT comparison ³He/H
includes ³H and ⁷Li/H includes ⁷Be (arXiv:2408.14538) [src: Sect. IV.1];
check this before comparing with a code that reports them separately.

### Step 6. Couple the code to a sampler
<!-- key: step-6-couple-the-code-to-a-sampler -->

- **Interpolation grid.** Planck sets Y_P, when not free, "by
  interpolation on a grid" from PArthENoPE 1.1 (2.0 gives identical
  results) with τ_n fixed at 880.2 s, uncertainties neglected; PRIMAT gives
  Y_P higher by ≈ 0.0005 at the same τ_n, which moves other parameters by
  "well within 0.1σ" (arXiv:1807.06209) [src: Sect. 2.1].
- **Cached background.** PRyMordial stores the thermal background and the
  n ↔ p rates; later runs with the same physics skip them, which is how
  the PDG-style abundance-versus-η plot and Monte Carlo runs are made
  (arXiv:2307.07061) [src: Sect. 3.2].
- **Direct call in the likelihood.** LINX runs in about 1/3 s per point
  ("key" network) and about 1/2 s ("full") on one CPU core after a
  compilation of about one minute (a few minutes for "full"); gradients
  with "key" compile in about one minute and run in about 1/2 s, with
  "full" in about ten minutes and about 1 s (arXiv:2408.14538)
  [src: Sect. IV.2]. AlterBBN takes 0.03 s to 72 s per calculation
  depending on the integrator (arXiv:1806.11095) [src: Appendix C].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Full weak-rate calculation or a fitted one
<!-- key: full-weak-rate-calculation-or-a-fitted-one -->

- **Assumes.** A fit (PArthENoPE, AlterBBN) assumes the corrections
  computed once for the standard background still hold; the full
  calculation (PRIMAT, PRyMordial, LINX) recomputes them.
- **Buys.** The fit is fast; the full calculation adapts to non-standard
  backgrounds.
- **Costs.** PArthENoPE's Y_P accuracy was stated as ~0.2% in 2008
  (arXiv:0705.0290) [src: Sect. V]. With the same Planck ω_b, PArthENoPE
  gives Y_P^BBN = 0.24672 and PRIMAT 0.24714, a shift of ≈ 4.2 × 10⁻⁴
  attributed to the different τ_n "and because PRIMAT includes a more
  elaborate treatment of weak interaction rates"; the Planck authors judge
  it close to the theory errors and an order of magnitude below the Aver
  et al. 2015 observational error (arXiv:1807.06209) [src: Sect. 7.6.1,
  Eqs. 70a–b].
- **Shortcut inside a full code.** LINX takes the ThRC + BS correction from
  a PRyMordial table computed for standard BBN, because the
  two-dimensional quadrature "cannot be straightforwardly performed in
  JAX"; it checked that using the standard-BBN correction for
  BBN + ΔN_eff is a negligible error (arXiv:2408.14538) [src: Sect. III.3.1].

### Corrections that respect detailed balance
<!-- key: corrections-that-respect-detailed-balance -->

Finite-temperature radiative corrections alone raise Y_P by ΔY_P^(4) ≃ 3.1;
with the bremsstrahlung terms that restore detailed balance the net is
≃ 0, against −4 reported by Esposito et al. (arXiv:1801.08023)
[src: Sect. V.3.3]. The authors' reason: a correction that violates
detailed balance acts like a change of the n–p mass gap and displaces the
equilibrium n/p, so "an overestimated enhancement of Γ_{p→n}" raises Y_P
artificially [src: Sect. V.3.3]. They also count the electron mass shift
as part of the finite-temperature corrections, not of the plasma
thermodynamics, which explains a 1.4 × 10⁻⁴ difference with Lopez &
Turner [src: Sects. V.3.3–V.3.4].

### Neutrino decoupling: thermal approximation or full spectra
<!-- key: neutrino-decoupling-thermal-approximation-or -->

Implemented in PRIMAT with neutrino spectra from an external
quantum-kinetic calculation (Froustey, Pitrou & Volpe 2020), relative to
instantaneous decoupling (arXiv:2008.01074) [src: Sect. 5, Tables 2–3]:

| Implementation | δY_P (%) | δ(D/H) (%) | δ(⁷Li/H) (%) |
|---|---|---|---|
| common temperature T̂_ν, with oscillations | 0.021 | 0.375 | −0.418 |
| T_νe, no spectral distortions | 0.007 | 0.367 | −0.427 |
| T_νe, with distortions (full) | 0.042 | 0.387 | −0.404 |

where T̂_ν ≡ [(T_νe⁴ + T_νμ⁴ + T_ντ⁴)/3]^{1/4}. The authors conclude that
the common-temperature shortcut is less accurate with oscillations but
still gives abundances to "a few 10⁻⁴" relative precision, well beyond
observational errors [src: Sect. 5]. The D/H increase comes mostly from
the clock effect: faster expansion leaves less time to burn deuterium
[src: Sect. 5]. Finite-mass corrections depend on T_ν, so the two effects
do not add: together they give ΔY_P^(4) ≃ −0.6 less than separately, and
PRIMAT's authors ask for a joint treatment (arXiv:1801.08023)
[src: Sect. V.3.2]. LINX, for its validation, switches PRIMAT back to the
older fitting-function decoupling (NEVO = False), a change of less than
0.1% in the abundances (arXiv:2408.14538) [src: Sect. IV.1].

### Small or large network
<!-- key: small-or-large-network -->

At aligned inputs, LINX's 61-reaction network and PRIMAT's 422-reaction
network agree to better than 0.15% in Y_P, D/H and N_eff and 0.22% in
⁷Li/H, which the LINX authors take as showing 61 reactions are enough up
to ⁷Li (arXiv:2408.14538) [src: Sect. IV.1, Table 4]. PRyMordial's
12-reaction option is offered for "precise predictions of the helium-4 and
deuterium abundances", the 51 extra reactions for ⁷Li (arXiv:2307.07061)
[src: Sect. 2.3].

### Default rate set of each code
<!-- key: default-rate-set-of-each-code -->

With constants, masses, reverse-rate constants and the n + p → d + γ rate
aligned, but each code's own other rates, at η = 6.14 × 10⁻¹⁰ and
τ_n = 879.4 s (Meißner & Metsch 2022,
arXiv:2208.12600) [src: Sect. IV, Table 1]:

| Code | 10⁵ D/H | 10⁵ (³H + ³He)/H | Y_P | 10¹⁰ (⁷Li + ⁷Be)/H |
|---|---|---|---|---|
| NUC123 | 2.550 | 1.040 | 0.247 | 4.577 |
| PArthENoPE | 2.511 | 1.032 | 0.247 | 4.672 |
| AlterBBN | 2.445 | 1.031 | 0.247 | 5.425 |
| PRIMAT | 2.471 | 1.044 | 0.247 | 5.413 |

The 4% spread in D/H is the rate philosophy, not the software: PRIMAT's
authors attribute their D and ⁷Li differences with Cyburt et al. to NACRE
II rates for d(p,γ)³He, d(d,n)³He, d(d,p)³H and ³He(α,γ)⁷Be, and the
larger gap with Planck's PArthENoPE D/H "again, probably" to the
deuterium-destruction rates (arXiv:1801.08023) [src: Sect. V.6]. PRyMordial
switches between NACRE II-based and PRIMAT key rates with one flag
(`nacreii_flag`), and its authors show the "deuterium anomaly" appears
with PRIMAT rates and is "completely washed out" with NACRE II
(arXiv:2307.07061) [src: Sect. 3.2]. PArthENoPE 3.0 reads the three
deuterium-burning rates from an optional `rates.dat`, with keywords
PIS2020 (default), LUNA2019, IL2016, MARCII, COC2015, MARCI, AD2011 for
d(p,γ)³He and PIS2020, PIS2020noTH (no Trojan-Horse data), GI2017,
COC2015, PIS2007, CY2004 for d + d (Gariazzo et al. 2022,
arXiv:2103.05027) [src: Sect. 2, Table 1].

### Normalising the weak rates by τ_n or by g_A
<!-- key: normalising-the-weak-rates-by-taun-or-by-ga -->

Under τ_n normalisation, τ_n carries 67.1% (PRIMAT rates) or 45.2% (NACRE
II rates) of the Y_P variance; under the fundamental normalisation g_A
carries 78–83% and V_ud ~12% (arXiv:2603.22414) [src: Sect. 7.2,
Tables 8–9]. τ_n and the fundamental parameters never enter the same
scheme, so their correlation does not arise; the maximal g_A–V_ud
correlation inflates the fundamental-normalisation Y_P error by at most
~25% [src: Sect. 7.1].

### Interpolation and solver settings
<!-- key: interpolation-and-solver-settings -->

Switching PRIMAT between linear and cubic interpolation of rate tables
changes ⁷Li/H by up to 2%; solver tolerances "can also lead to nontrivial
shifts", so the LINX comparison uses linear interpolation and default
tolerances in all codes (arXiv:2408.14538) [src: Sect. IV.1]. In AlterBBN,
relative to its most precise setting (failsafe = 12: Y_P = 0.2472,
10⁵ D/H = 2.463, 10¹⁰ ⁷Li/H = 5.370), the fastest setting (failsafe = 0,
0.03 s) gives Y_P lower by 0.0010, D/H lower by 0.120 × 10⁻⁵ (~5%) and
⁷Li/H higher by 0.310 × 10⁻¹⁰; failsafe = 3 is within 0.004 × 10⁻⁵ in
D/H in 0.5 s (arXiv:1806.11095, later arXiv version) [src: Appendix C].

### Differentiable code
<!-- key: differentiable-code -->

LINX buys gradients for gradient-based samplers and joint CMB + BBN fits;
its cost is compilation (one to ten minutes) and a GPU advantage only for
batches ≳ 550 points, because of frequent host synchronisation, so CPU is
preferred for sequential Monte Carlo (arXiv:2408.14538) [src: Sect. IV.2].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Total weak-rate corrections on Y_P | +1.84% (0.24262 → 0.24709) | PRIMAT | arXiv:1801.08023 | Table 5 |
| Zero-T radiative corrections | ΔY_P^(4) = 31.0 (non-resummed), +0.5 resummed | PRIMAT | arXiv:1801.08023 | Sect. V.3.1 |
| FM + WM | ΔY_P^(4) = 12.8 (+0.53%); WM ≈ 12% of FM | PRIMAT | arXiv:1801.08023 | Sect. V.3.2 |
| Incomplete decoupling (clock effect) | ΔY_P^(4) ≃ 1.2 | PRIMAT | arXiv:1801.08023 | Sect. V.3.5 |
| PRIMAT 2021 additions (oscillating ν, pair-production corrections to radiative captures, O(e³) QED) | 10⁵ D/H shifts +0.0015, −0.0021, −0.0003; Y_P +0.00005 from the first only | PRIMAT 2021 | arXiv:2011.11320 | Sect. 1 |
| QED corrections to photon-emitting nuclear rates | D/H at the 0.2% level | LINX validation of PRIMAT | arXiv:2408.14538 | Sect. IV.1 |
| Monte Carlo theory errors (σ/mean) | Y_P 0.068%, D/H 1.49%, ³He/H 2.43%, ⁷Li/H 4.39% | PRIMAT 2018, 20 000 draws | arXiv:1801.08023 | Table 7 |
| PArthENoPE 2.0 → 3.0 | 10⁵ D/H 2.58 ± 0.09 ± 0.03 → 2.51 ± 0.06 ± 0.03; Y_P 0.24684 → 0.24687 (errors: rates, ω_b); τ_n = 879.4 ± 0.6 s gives the 0.00012 Y_P error | ω_b = 0.02242 ± 0.00014 | arXiv:2103.05027 | Sect. 2 |
| τ_n error to Y_P error | σ(τ_n) = 1.0 s → 3.0 × 10⁻⁴; 0.8 s → 2.4 × 10⁻⁴ | PArthENoPE, PRIMAT | arXiv:1807.06209 | Sect. 7.6.1 |
| LINX vs PRyMordial, same network and rates | ≤ 0.05% in Y_P, D/H, N_eff; ≤ 0.12% in ⁷Li/H | ω_b = 0.02242, τ_n = 879.4 s | arXiv:2408.14538 | Table 4 |
| LINX vs PRIMAT v0.2.2 | < 0.15% in Y_P, D/H, N_eff; 0.22% in ⁷Li/H | same | arXiv:2408.14538 | Table 4 |
| N_eff from the background | 3.0444 (LINX, PRyMordial); 3.0435 (PRIMAT) | same | arXiv:2408.14538 | Table 4 |
| PArthENoPE vs Kawano code, Y_P | 0.7%, mainly weak-rate corrections | PArthENoPE 2008 | arXiv:0705.0290 | Sect. V |
| PArthENoPE ΔN_eff input range | −3.0 to 15.0; extra radiation at T_X = T above T_d = 2.3 MeV, Eq. 24 below | PArthENoPE 2008 | arXiv:0705.0290 | Sect. III.2 |
| Rate correlations, worst case | total error × 1.01 (Y_P), × 1.4–1.6 (D/H), × 2.3 (⁷Li/H) | PRyMordial, 63 rates | arXiv:2603.22414 | Sect. 7.1 |
| D/H variance shares | PRIMAT rates: ω_b 51%, d(p,γ) 23%, d(d,n) 15%, d(d,p) 10%; NACRE II: d(d,n) 62%, d(d,p) 27%, ω_b 7% | τ_n normalisation | arXiv:2603.22414 | Table 8 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **A rate difference reported as a code difference.** Shows up as a D/H
  offset of several percent between codes at the same η (Table 1 of
  arXiv:2208.12600 above). Planck found PArthENoPE 1.10 higher than the
  Nollett & Holder code by Δ(10⁵ D/H) = 0.04 with the same d(p,γ)³He rate,
  which those authors attribute to the d + d rates (arXiv:1807.06209)
  [src: Sect. 7.6.1]. Test: rerun with aligned rates, as LINX did
  against PRyMordial and PRIMAT; remaining differences should be ≲ 0.1%.
- **Stale τ_n defaults.** Planck's PArthENoPE grid used τ_n = 880.2 s,
  PRIMAT 2018 879.5 s; PRIMAT gives Y_P = 0.24726 at τ_n = 880.3 s against
  0.24709 at 879.5 s (arXiv:1801.08023) [src: Table 8, note h]. Test: print
  τ_n with every tabulated Y_P.
- **Corrections that break detailed balance.** Shows as a Y_P shift of the
  wrong sign for a rate enhancement (arXiv:1801.08023) [src: Sect. V.3.3].
  Test: check that corrected forward and reverse rates still satisfy the
  equilibrium ratio.
- **Helium definitions mixed.** A BBN Y_P (nucleon fraction) compared with
  a CMB Y_P (mass fraction) is off by ~0.0013 at Planck values
  (arXiv:1807.06209) [src: Sect. 2.1], larger than the best observational
  error (0.0013 in `results.md#primordial-helium-4`).
- **Integrator or interpolation too coarse.** ⁷Li/H moves by up to 2% with
  interpolation order (arXiv:2408.14538) [src: Sect. IV.1]; AlterBBN's
  fastest integrator is ~5% off in D/H (arXiv:1806.11095) [src: Appendix C].
  Test: halve the tolerances and switch interpolation order; the change
  must be far below the observational error of the nuclide used.
- **Thermal-equilibrium shortcuts in non-standard runs.** A precomputed
  correction table (LINX ThRC + BS) or a fitted weak rate (PArthENoPE)
  assumes a near-standard background. LINX checked the ΔN_eff case only
  (arXiv:2408.14538) [src: Sect. III.3.1]; for other backgrounds, rerun the
  full correction.
- **Independent-rate assumption.** Rate compilations give no correlations;
  the error on D/H could be up to 1.4–1.6 times larger if rates were fully
  correlated (arXiv:2603.22414) [src: Sect. 7.1].
- **Validation recipe used by the code authors.** Fix ω_b = 0.02242 and
  τ_n = 879.4 s, use the same network and rate tables, linear
  interpolation, and default solver settings; compare N_eff, Y_P, D/H,
  ³He/H, ⁷Li/H; the stated aim is agreement "well below the experimental
  uncertainties", achieved at ≤ 0.15% for Y_P and D/H
  (arXiv:2408.14538) [src: Sect. IV.1]. PRyMordial and LINX also agree to
  ≪ 1% for D/H and Y_P across the η range of their Fig. 3 [src: Sect. IV.1].

## Reading list
<!-- key: reading-list -->

- Pitrou et al. 2018, arXiv:1801.08023 (foundation): the full weak-rate
  calculation, Table 5 of corrections, staged integration, Monte Carlo
  errors.
- Pisanti et al. 2008, arXiv:0705.0290 (code): PArthENoPE equations in z,
  initial conditions, ΔN_eff and ξ inputs, differences from the Kawano
  code.
- Gariazzo et al. 2022, arXiv:2103.05027 (code): the third PArthENoPE
  release, its rate keywords and their effect on D/H.
- Arbey et al. 2020, arXiv:1806.11095 (code): AlterBBN error modes,
  integrator accuracy and timing.
- Burns, Tait & Valli 2024, arXiv:2307.07061 (code): PRyMordial network
  stages, rate nuisances, NACRE II versus PRIMAT switch.
- Giovanetti et al. 2024, arXiv:2408.14538 (code, critique): LINX and the
  only aligned-input three-code validation read.
- Froustey, Pitrou & Volpe 2020, arXiv:2008.01074 (method): what neutrino
  decoupling does to the abundances, implementation by implementation.
- Meißner & Metsch 2022, arXiv:2208.12600 (method): four codes run with
  common constants; response matrix to binding energies.
- Burns 2026, arXiv:2603.22414 (method): variance budget per abundance
  under two rate compilations and two weak normalisations.
- Planck 2018, arXiv:1807.06209 (application): how a CMB analysis
  tabulates Y_P and what the code choice costs it.

## Not verified
<!-- key: not-verified -->

- Serpico et al. 2004 (the weak-rate fits used by PArthENoPE and AlterBBN)
  was not read; its role is stated from arXiv:2011.11320.
- The AlterBBN integration table comes from a later arXiv version of
  arXiv:1806.11095 than v1 (it mentions PRIMAT and compilers of 2019); the
  version number was not identified.
- The τ_n entry of the Meißner & Metsch response matrix (their Table 2)
  could not be attributed unambiguously in the rendering and is not
  quoted.
- PRyMordial run times and the temperature dependence of its rate
  nuisances were not read.
- No comparison of AlterBBN with aligned rates was found.
