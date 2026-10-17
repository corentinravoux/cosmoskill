# BBN — physics and methods

Scope: what big-bang nucleosynthesis measures, the standard calculation and
its inputs (expansion rate, weak rates, neutron lifetime, nuclear rates), how
each light-element abundance is inferred, BBN codes, and how BBN enters a
cosmological likelihood.
Snapshot: 2026-10-16

Flags: `[src]` abstract read this session; `[src: Sect. n]`, `[src: Eq. n]`,
`[src: Table n]` body read; `[sec]` named secondary source; `[der]` derived here.

## 1. What BBN measures
<!-- key: what-bbn-measures -->

BBN is a competition between the nuclear reaction rates, free-neutron decay
and the expansion rate (Cooke 2024 review, arXiv:2409.06015)
[src: Sect. 2]. In the Standard Model with N_ν = 3 its single free parameter
is the baryon-to-photon ratio η = n_B/n_γ, related to the baryon density by

    η = (273.78 ± 0.18) × 10⁻¹⁰ × Ω_b h²

(Steigman 2006, as quoted in arXiv:2409.06015 [sec: Cooke 2024, Sect. 2];
the same factor is used in arXiv:1710.11129 [src: Sect. V.2]). With
Ω_b h² from the CMB, standard BBN has no free parameter; with the
abundances alone it measures Ω_b h² at t ~ 1 s–10 min, and with Ω_b h² fixed
it measures the expansion rate, usually parameterised by ΔN_ν or N_eff
(arXiv:2409.06015) [src: Sect. 2].

**Sensitivities.** Each nuclide answers a different question
(arXiv:2409.06015) [src: Sect. 2]:

- D/H is the best baryometer: ⁷Li/H is slightly more sensitive to Ω_b h²,
  but the deuterium reactions are better known.
- D/H is also the most sensitive nuclide to the expansion rate, but rate
  uncertainties limit N_eff from D/H alone to ~2%.
- Y_P is nearly insensitive to Ω_b h² and could reach ~0.5% on N_eff,
  i.e. ΔN_ν ≃ 0.015, because its inputs (chiefly τ_n) are well known.

Numerical scalings around η₁₀ = 6.115, N_ν = 3, τ_n = 878.4 s (Yeh, Olive &
Fields 2023, arXiv:2303.04140) [src: Sect. III, Eqs. 13–16]:

    Y_P   = 0.2467      (η₁₀/6.115)^0.040  (N_ν/3)^0.163  (τ_n/878.4 s)^0.730
    D/H   = 2.496e-5    (η₁₀/6.115)^-1.634 (N_ν/3)^0.405  (τ_n/878.4 s)^0.413
    ³He/H = 1.041e-5    (η₁₀/6.115)^-0.570 (N_ν/3)^0.138  (τ_n/878.4 s)^0.127
    ⁷Li/H = 4.937e-10   (η₁₀/6.115)^2.117  (N_ν/3)^-0.285 (τ_n/878.4 s)^0.431

From these, a 1% error on D/H maps to 0.6% on η [der: 1/1.634, at fixed
N_ν and rates], and a 1 s shift in τ_n moves Y_P by ≈ 0.0002
[der: 0.730 × 0.2467/878.4].

## 2. The standard calculation
<!-- key: the-standard-calculation -->

- **Radiation content.** Before neutrino decoupling ρ_R/ρ_γ = 43/8 for γ,
  e± and three neutrino species; after e± annihilation
  ρ_R/ρ_γ = 1 + (7/8)(4/11)^{4/3} N_eff. Non-instantaneous decoupling gives
  N_eff = 3.043 for N_ν = 3 (Cielo et al. 2023, as quoted in
  arXiv:2409.06015) [sec: Cooke 2024, Sect. 2]. BBN papers often quote
  N_ν with baseline 3; CMB papers N_eff with baseline 3.044; see
  `cosmo-neutrinos-dark-matter` for the precise value and its derivation.
- **Weak freeze-out.** The n/p ratio freezes out when the weak rates
  (∝ τ_n⁻¹ T⁵) fall below H (∝ G^{1/2} T²), so T_f ∝ τ_n^{1/3}; then free
  neutrons decay until the deuterium bottleneck breaks at t_BBN ≈ 322 s.
  With T_f = 0.84 MeV and (n/p)_f = 1/4.66, (n/p)_BBN = 1/7.17 and
  ΔY_P/Y_P ≈ (0.42 + 0.37) Δτ_n/τ_n = 0.79 Δτ_n/τ_n analytically
  (arXiv:2303.04140) [src: Sect. II–III, Eqs. 7–12].
- **Timeline.** n–p freeze-out ~2 s; ¹H and ⁴He frozen at ~6 min; ⁷Be at
  ~4 h; ²H, ³H, ³He, ⁷Li at ~8–10 h; ³H then decays to ³He (τ ≈ 12.32 yr) and
  ⁷Be to ⁷Li by electron capture at z ~ 35 000–27 500. Hence "³He" means
  ³H + ³He and "⁷Li" means ⁷Li + ⁷Be (arXiv:2409.06015) [src: Sect. 2].
- **Weak-rate corrections** that set Y_P to 10⁻⁴: radiative
  zero-temperature corrections, finite nucleon mass, finite-temperature
  radiative corrections, weak magnetism and QED plasma effects, all included
  self-consistently with detailed balance in PRIMAT
  (arXiv:1801.08023) [src].
- **Neutrino decoupling with oscillations** and the full collision term is
  treated in Froustey, Pitrou & Volpe (2020, arXiv:2008.01074) [src];
  PRyMordial includes non-instantaneous decoupling and returns N_eff
  (arXiv:2307.07061) [src].

## 3. Nuclear reaction rates
<!-- key: nuclear-reaction-rates -->

**Which rates matter.** For deuterium the three burning reactions dominate:
radiative capture d(p,γ)³He and the two transfer reactions d(d,n)³He and
d(d,p)³H (Schöneberg 2024, arXiv:2401.15054) [src: Sect. 3, Eqs. 1–3]. After
the LUNA measurement of d(p,γ)³He, the remaining differences between codes
are mostly in the two transfer reactions (arXiv:2401.15054) [src: Sect. 3],
and the error budget of the BBN + CMB deuterium prediction is dominated by
d(d,n)³He and d(d,p)³H (Yeh, Olive & Fields 2021, arXiv:2011.13874) [src].
Helium-4 depends essentially on the weak rates that set the neutron-to-proton
ratio, not on nuclear rates (Pitrou et al. 2018, arXiv:1801.08023) [src].
For lithium the destruction of ⁷Be by neutrons, ⁷Be(n,p)⁷Li and ⁷Be(n,α)⁴He,
was the main nuclear unknown until the n_TOF measurements
(arXiv:1606.09420, arXiv:1803.05701) [src].

**Cross section, S-factor, thermal rate.** Laboratory cross sections are
measured above the Gamow window or reach into it underground; they are
expressed as an astrophysical S-factor, fitted in energy, and integrated over
a Maxwell–Boltzmann distribution to a thermal rate. Two approaches coexist:
the energy dependence of the S-factor from ab-initio theory with the
normalisation fitted to data (PRIMAT; Coc et al. 2015, arXiv:1511.03843), or
fits to measured data alone (PArthENoPE; the Fields–Olive–Yeh code with
polynomial fits) (arXiv:2401.15054) [src: Sect. 3]. In all cases the
normalisation is fitted to experiment; the difference lies also in which
data are kept and how they are fitted (arXiv:2401.15054) [src: Sect. 3,
footnote 5].

**Rate evaluations in use.**

| Evaluation | Method | Reactions | Citation | Flag |
|---|---|---|---|---|
| Coc et al. 2015 | ab-initio S-factor shapes, systematic uncertainties included | d(p,γ), d(d,n), d(d,p); D/H = (2.45 ± 0.10) × 10⁻⁵ (2σ) | arXiv:1511.03843 | [src] |
| Gómez Iñesta, Iliadis & Coc 2017 | Bayesian S-factor fits | d(d,n), d(d,p); D/H lower by 0.16% | arXiv:1710.01647 | [src] |
| Yeh, Olive & Fields 2021 | world-average data, model-independent polynomials | d(p,γ) with LUNA | arXiv:2011.13874 | [src] |
| Pisanti et al. 2021 (PArthENoPE) | statistical analysis of data with theoretical-uncertainty study | d(p,γ), d(d,n), d(d,p) | arXiv:2011.11537 | [src] |
| NACRE II | compilation of measured rates; used by PRyMordial in its data-driven mode | network | named in arXiv:2401.15054 | [sec: arXiv:2401.15054, Sect. 3] |
| Launders, Giovanetti & Liu 2026 | Gaussian-process regression on data; finds low-degree polynomial fits systematically over-predict D/H | d(p,γ), d(d,n), d(d,p) | arXiv:2604.16600 | [src] |
| Spartà et al. 2025 | Trojan-Horse indirect rates run through PRIMAT | several, jointly for the first time | arXiv:2512.24358 | [src] |

**Theory of the deuterium-burning reactions.** Ab-initio four-body
calculations of d(d,p)³H and d(d,n)³He with chiral two- and three-nucleon
interactions give S-factors with a theory error from cutoff variation
(Viviani et al. 2022, arXiv:2207.01433) [src]. For d(p,γ)³He the LUNA data
lie below the ab-initio benchmark; an effective-field-theory fit to capture
data with nuclear-theory priors gives S(0) = 0.209 ± 0.008 eV b and traces
the offset to one next-to-leading contact term (Tait 2026,
arXiv:2607.05514) [src].

## 4. The neutron lifetime and the weak rates
<!-- key: the-neutron-lifetime-and-the-weak-rates -->

τ_n has two roles: it normalises the zero-temperature n ↔ p matrix element
(rates ∝ 1/τ_n), and it sets free-neutron decay after freeze-out. A longer
τ_n gives earlier freeze-out and more surviving neutrons, hence more ⁴He
(Yeh, Olive & Fields 2023, arXiv:2303.04140) [src; Sect. II]. τ_n
dominates the error budget of the Y_P prediction but remains below the
observational error on Y_P, even given the spread of recent measurements; it
contributes negligibly to the other nuclides (arXiv:2303.04140) [src].
Inverting, BBN + CMB "predict" τ_n = 870 ± 16 s (arXiv:2303.04140) [src].

The two experimental methods measure different things. A **bottle**
counts surviving ultracold neutrons after storage (material or
magneto-gravitational traps); a **beam** counts decay products from a cold
beam of known fluence. Lifetime and axial coupling are linked by
τ_n(1 + 3g_A²) = 5172.0(1.1) s (Czarnecki, Marciano & Sirlin 2018,
arXiv:1802.01804) [src]. Measured values are in `results.md` §8 and the
puzzle in `open-questions.md` §3.

## 5. BBN codes
<!-- key: bbn-codes -->

| Code | Language, interface | Rates | Distinctive features | Reference | Flag |
|---|---|---|---|---|---|
| PArthENoPE | Fortran; v1 needed NAG, v2 uses ODEPACK and a GUI; v3 ("Revolutions") revisits d(p,γ), d(d,n), d(d,p) | fits to data | widely used in CMB codes and BAO + BBN analyses | Pisanti et al. 2008, arXiv:0705.0290; Consiglio et al. 2018, arXiv:1712.04378; Gariazzo et al. 2022, arXiv:2103.05027 | [src] |
| PRIMAT | Mathematica | ab-initio-shaped S-factors | weak rates with radiative, finite-mass, finite-temperature, weak-magnetism and QED-plasma corrections computed self-consistently; network up to CNO | Pitrou et al. 2018, arXiv:1801.08023; upgrade in arXiv:2011.11320 | [src] |
| AlterBBN | C | compiled rates | alternative cosmologies (expansion rate, entropy, η, N_eff); v2 has no closed external library | Arbey 2012, arXiv:1106.1363; Arbey et al. 2020, arXiv:1806.11095 | [src] |
| PRyMordial | Python, optional Julia | NACRE II-based or PRIMAT tables, switchable | non-instantaneous neutrino decoupling, N_eff computed; marginalisation over rate uncertainties | Burns, Tait & Valli 2024, arXiv:2307.07061 | [src] |
| LINX | Python/JAX | — | differentiable, for gradient-based inference and joint CMB + BBN fits on personal hardware | Giovanetti et al. 2024, arXiv:2408.14538 | [src] |
| Fields–Olive–Yeh code | — | polynomial fits to data | descends from the 1999 update of the Wagoner code; basis of the PDG Ω_b h² | named in arXiv:2401.15054 | [sec: arXiv:2401.15054, Sect. 3 footnote 3] |

Schöneberg (2024) judges that AlterBBN "does not yet implement the nuclear
reactions at the same level of precision" as PRIMAT and PArthENoPE
(arXiv:2401.15054) [src: Sect. 3]. The four public codes were run side by
side on variations of nuclear observables by Meißner & Metsch
(2022, arXiv:2208.12600) [src]. For agreement in numbers, see
`results.md` §7.

## 6. From abundances to parameters
<!-- key: from-abundances-to-parameters -->

- **Likelihood.** The standard construction multiplies a BBN likelihood
  L_BBN(η, N_ν; D/H, Y_P, …) by a CMB likelihood L_CMB(η, Y_P) without an
  a priori link between Y_P and η, and optionally a τ_n likelihood
  (Yeh, Olive & Fields 2023, arXiv:2303.04140) [src: Sect. III, Eq. 17].
- **Rate nuisances.** Rate uncertainties are carried either by one
  temperature-dependent rescaling nuisance per reaction with a Gaussian
  prior (PRIMAT, PRyMordial) or by Gaussian processes; a careful analysis
  marginalises them in the likelihood (arXiv:2609.12065) [src: Sect. 1].
- **Compressed BBN likelihoods** in CMB analyses: Planck estimates the
  deuterium prediction error by shifting all rates by ±1σ together, which
  overestimates it, and adds it as a constant; ACT uses a constant combined
  theory-plus-observation error (arXiv:2609.12065) [src: Sect. 1]. These
  choices matter less in combination with the CMB than for BBN alone
  (arXiv:2609.12065) [src: Sect. 1].
- **Data selection for rate fits.** Akharman et al. and Launders et al.
  recommend excluding cross-section data far outside 0.015–0.6 MeV (for
  example a dataset whose lowest point is at 1.96 MeV, used by PArthENoPE and
  the Fields–Olive–Yeh network but excluded by PRIMAT) and treating
  Trojan-Horse data, whose normalisation comes from other datasets, with care
  (arXiv:2609.12065) [src: Sect. 2.1].
- **BBN consistency in CMB fits.** CMB analyses either fix Y_P from BBN as a
  function of (ω_b, N_eff) or free Y_P; that machinery and the effect on
  damping-tail constraints are held in `cosmo-cmb`.
- **Differentiable pipelines.** LINX (arXiv:2408.14538) and the
  differentiable Boltzmann solver ABCMB with a BBN treatment
  (Zhou, Giovanetti & Liu 2026, arXiv:2602.15104) [src] enable joint
  CMB + BBN sampling with gradients.

## 7. Conventions and where the community is split
<!-- key: conventions-and-where-the-community-is-split -->

| Item | Conventions in use | Trap |
|---|---|---|
| Baryon density | η₁₀ = 10¹⁰ η; Ω_b h² = ω_b; η₁₀ = 273.78 Ω_b h² (arXiv:1710.11129 [src: Sect. V.2]) | quoting η from one paper and ω_b from another with a different conversion |
| Helium | Y_P mass fraction vs y_P = n(He)/n(H); Y = 4y(1−Z)/(1+4y) (arXiv:2601.22238 [src: Sect. VII.3]) | regressions in Y depend on Z, in y do not |
| Expansion rate | N_ν (BBN, baseline 3) vs N_eff (CMB, baseline 3.044); ΔN_ν = 0 ↔ N_eff ≈ 3.043–3.044 (arXiv:2409.06015 [src: Sect. 2]; arXiv:2207.13133 [src]) | comparing N_ν from BBN with N_eff from the CMB without the 0.044 offset |
| Helium-3 | ³He means ³He + ³H; ⁷Li means ⁷Li + ⁷Be (arXiv:2409.06015 [src: Sect. 2]) | — |
| Lithium | A(Li) = log₁₀(Li/H) + 12 | mixing A(Li) with Li/H |
| Deuterium | 10⁵ (D/H) or log₁₀(D/H) | errors on the log are not symmetric on the linear value |
| Rate philosophy | ab-initio-shaped S-factors (PRIMAT) vs fits to data (PArthENoPE, Fields–Olive–Yeh) vs Gaussian processes (Launders et al.) (arXiv:2401.15054 [src: Sect. 3]; arXiv:2604.16600 [src]) | a "BBN prior" without the rate set |
| τ_n | bottle (~878 s) or beam (~888 s) or PDG average (arXiv:1802.01804 [src]) | — |

**Where the community is split.**

1. Which deuterium-burning rates to adopt: the ab-initio side (Coc,
   Iliadis, Pitrou, Uzan, Vangioni; arXiv:1511.03843, arXiv:2011.11320)
   against data-driven fits (PArthENoPE, arXiv:2011.11537; Fields–Olive–Yeh,
   arXiv:2011.13874), with Gaussian processes siding with the lower D/H
   predictions (arXiv:2604.16600) [src].
2. Whether to marginalise over rates (arXiv:2401.15054,
   arXiv:2609.12065) or to use compressed BBN likelihoods with constant
   theory errors, as Planck and ACT do (arXiv:2609.12065) [src: Sect. 1].
3. Weighted average versus regression for Y_P (arXiv:2601.22238)
   [src: Sect. VII.3]; and whether extremely metal-poor galaxies give a
   lower Y_P (arXiv:2506.24050) [src].
4. Stellar versus primordial explanations of the lithium deficit (§4 of
   `open-questions.md`).

Standard reviews: Cyburt et al. 2016 (arXiv:1505.01076), which notes that
D/H observations became more precise than predictions and that D/H with the
CMB baryon density gives N_ν < 3.2 at 2σ [src]; Fields et al. 2020
(arXiv:1912.01132); Pitrou et al. 2018 (arXiv:1801.08023); Cooke 2024
(arXiv:2409.06015); Grohs & Fuller 2023 (arXiv:2301.12299) [src: section
titles]; Iliadis & Coc 2020 on rates (arXiv:2008.12200) [src: abstract
snippet].

## Not verified
<!-- key: not-verified -->

- Steigman 2006 (η–Ω_b h² conversion) and Cielo et al. 2023 (N_eff = 3.043)
  were taken from the Cooke 2024 review, not read.
- The NACRE II compilation and the Wagoner-code lineage of the
  Fields–Olive–Yeh code are named from arXiv:2401.15054, not read.
- The EFT contact-term interpretation of d(p,γ)³He (arXiv:2607.05514) is a
  single 2026 paper; no independent confirmation read.
