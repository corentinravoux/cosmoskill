# Fuzzy and ultralight dark matter — cosmo-neutrinos-dark-matter dossier

Scope: how an ultralight boson is put into a Boltzmann code (field
before oscillation, effective fluid after), how its non-linear effect is
modelled for galaxy clustering and CMB lensing (EFT with one or two
fluids, halo model), how the Lyα and dwarf-kinematics limits are
produced (modified initial conditions or wave dynamics, emulators,
priors on the mass), and what each choice was found to cost.
Snapshot: 2026-10-19.
From: Snowmass 2021 halo-measurements white paper (Bechtol et al.,
arXiv:2203.07354), Sect. 2.3.2; ACT DR6 extended models
(arXiv:2503.14454), Sect. VI.3.

Already in L2, not repeated here: the limits for all and part of the
dark matter and the hints that did not survive combination
(`results.md#fuzzy-ultralight-dark-matter`,
`results.md#sub-component-upper-limits-on-the-axion`); the fuzzy
transfer-function fit and half-mode mass of the satellite analysis
(`physics-and-methods.md#half-mode-scale-and-the-kev-conversion`); the
thermal-history dependence of the Lyα limit and the dwarf-kinematics
systematics in one line each
(`systematics.md#lyman-alpha-forest-the-thermal-history`,
`systematics.md#stellar-streams-luminosity-functions-dwarf`); the
production dependence (`open-questions.md#fuzzy-and-ultralight-dark-matter`).
The Lyα emulator machinery in general is in
`cosmo-lyman-alpha/deep/p1d-emulators.md`; the strong-lensing route in
`deep/strong-lensing-substructure.md`.

## How it is done
<!-- key: how-it-is-done -->

Notation: m_a (or m_FDM, m_ψ) the boson mass; Ω_a the axion density,
Ω_d = Ω_a + Ω_c the total dark-matter density, and the fraction written
Ω_a/Ω_d, f_ax or f_FDM depending on the paper; H the Hubble rate; a_osc
the scale factor at which the field starts to oscillate; k_J the Jeans
wavenumber; T(k) = [P(k)/P_CDM(k)]^(1/2) the linear transfer function;
P_F or P_f the 1D Lyα flux power; T₀, γ the temperature at mean density
and slope of the temperature–density relation; u₀ the cumulative heat
injected per proton; τ_eff the effective optical depth.

### Step 1. Linear theory: field, then fluid
<!-- key: step-1-linear-theory-field-then-fluid -->

The modified Boltzmann codes used (axionCAMB, its successor axiECAMB,
and the codes built on them) follow the scheme of Hlozek et al. 2015
(arXiv:1410.2896 [src]):

1. **Before oscillation** (m_a ≤ 3H): solve the homogeneous field and
   its perturbation exactly, with the field's energy density in H
   everywhere, including the recombination module and the visibility
   function; choose the initial field value by shooting to the requested
   Ω_a/Ω_d to 10⁻⁴ [src: Sect. III.4].
2. **After oscillation** (m_a ≥ 3H): direct integration becomes
   "computationally prohibitive" once m_a ≫ 3H (already for m_a ≳
   10⁻²⁷ eV), so a WKB average over the oscillation period gives an
   effective fluid with w_a ≈ 0 and sound speed
   c_a² = [k²/(4m_a²a²)]/[1 + k²/(4m_a²a²)] (Eq. 32),
   which interpolates between pressureless matter on large scales and a
   cut-off below the Jeans scale; the fluid equations are Eqs. 33–34
   (synchronous gauge) [src: Sect. III.3].
3. **Check the switch.** Results are insensitive to moving the matching
   time by δτ = 10/m; the fluid code agreed with direct integration of
   the perturbed field up to m_a ~ 10⁴ H₀, and the approximation
   improves with mass [src: Sect. III.3].

### Step 2. Sample a two-parameter model whose degeneracies change with mass
<!-- key: step-2-sample-a-two-parameter-model-whose -->

- **Fixed masses.** The 2023 BOSS + CMB analysis does not vary m_a but
  runs at fixed masses in [10⁻³², 10⁻²⁴] eV, because "the full posterior
  projected in the m_a–Ω_ah² plane has a highly non-trivial degeneracy,
  which is difficult to sample numerically in a converged manner"
  (Rogers et al. 2023, arXiv:2301.08361 Sect. 3.4 [src]). The ACT
  lensing analysis does the same for four masses from 10⁻²⁶ to 10⁻²⁴·⁵
  eV, because different masses "lead to distinct parameter degeneracies
  and are thus often treated as separate cosmological models" (Laguë et
  al. 2026, arXiv:2606.06410 Sect. IV.1 [src]).
- **Free mass.** When both are varied, Metropolis–Hastings "performs
  poorly"; nested sampling (dynesty, 50 live points per free parameter,
  eleven parameters, stop at dlogz < 0.001) is used, and the fraction
  limit at the high-mass end is quoted from samples restricted to a mass
  range, because "naively marginalizing over the axion mass ... would
  lead to spurious results" [src: arXiv:2606.06410 Sect. IV.2].
- **Mass prior.** Uniform in log₁₀ m_a over −33 to −22 in the first CMB
  + galaxy analysis, called "the most conservative" (a Jeffreys prior)
  and the string-landscape preference; flat priors on Ω_ah² and Ω_ch²
  in 10⁻⁵–0.3 so that fractions down to 10⁻⁴ are reached, rather than a
  prior uniform in the misalignment angle (P ∝ (Ω_ah²)^(−1/2)) [src:
  arXiv:1410.2896 Sect. V.3]. ACT: Ω_ah² uniform in [10⁻⁶, 0.15],
  log₁₀ m_a fixed or uniform in [−26, −24.5] [src: arXiv:2606.06410
  Table 1].

### Step 3. Non-linear scales for a sub-component
<!-- key: step-3-non-linear-scales-for-a-sub-component -->

| Analysis | Treatment | Stated reason | Source |
|---|---|---|---|
| CMB + WiggleZ, 2015 | k ≲ 0.2 h/Mpc only, linear bias | halofit "has not been calibrated using simulations of ULA DM", and wrong non-linear modelling "could lead to spurious constraints" | arXiv:1410.2896 Sect. V.1 [src] |
| Planck + BOSS P(k) and bispectrum, 2023 | axions only in the background and the linear spectrum fed to the one-loop EFT; counterterms assumed to have the CDM functional form with free coefficients; full EFT nuisance set marginalised | the axion effect is "qualitatively the same as for free-streaming neutrinos", for which the extra counterterms have the CDM form; linear axion-wave corrections are negligible; unbiased recovery on a simulated BOSS catalogue with axions (both from an earlier paper) | arXiv:2301.08361 Sect. 2.2.3 [src] |
| DESI DR1 full shape + Planck + ACT, 2026 | two-fluid EFT: δ_a^[n] = (δ_a^[1]/δ_c^[1]) δ_c^[n] (Eq. 7); galaxies trace both fields, δ_g ⊃ b_cδ_c + b_aδ_a (Eq. 8); two new counterterms −2c_ca,ℓ k²P_ca^L − 2c_aa,ℓ k²P_aa^L (Eq. 9); ACT lensing non-linearities also perturbative | the standard EFT relies on factorised growth, valid only for scale-free cosmologies; two components must be biased separately "to avoid overconfident and potentially biased inference" | Verdiani et al. 2026, arXiv:2607.11876 Sect. III [src] |
| ACT DR6 lensing + CMB + BAO, 2026 | axionHMcode halo model: axion field split into a halo fraction F_h and a linear part (Eq. 13); total P_m from axion, cross and cold-plus-baryon spectra (Eq. 14); calibrated on mixed Schrödinger–Poisson simulations, accurate to k ~ 10 h/Mpc; cosmopower-style neural emulator | CMB lensing at high multipoles needs non-linear corrections; solitons enhance power by up to ~30% in the axion spectrum at k ~ 0.1–1 h/Mpc for 10⁻²⁴–10⁻²⁵ eV | arXiv:2606.06410 Sect. II.1, II.3, Appendix B [src] |

### Step 4. Fuzzy dark matter as all of the dark matter: the Lyα forest
<!-- key: step-4-fuzzy-dark-matter-as-all-of-the-dark -->

1. **Modified initial conditions only.** Every Lyα analysis read
   suppresses the initial power at z = 99 with the fuzzy transfer
   function and evolves an ordinary hydrodynamical simulation; quantum
   pressure is not followed. The reason given in 2017: quantum pressure
   dominates only for k > k_J; for the lightest mass simulated (10⁻²²
   eV) at z = 5.4, k_J = 64.7 h/Mpc against k_max = 12.7 h/Mpc for the
   data, and the growth-rate ratio is ξ > 0.995 below 12.7 h/Mpc (ξ =
   0.55 at 40 h/Mpc) (Iršič et al. 2017, arXiv:1703.04683 [src]). The
   2020 analysis follows earlier work "as this is sufficient for the
   current sensitivity of data" (Rogers & Peiris 2020, arXiv:2007.12705
   [src]); the 2026 analysis calls it sufficiently accurate for pure
   fuzzy dark matter but "a non-trivial assumption" for a mixture (Liu,
   Gong & Zhou 2026, arXiv:2606.06969 Sect. 2.3 [src]).
2. **Transfer function.** Either a published fit or a polynomial fit of
   T(k) = [1 + (α k)^β]^γ to axionCAMB output, with α, β, γ functions of
   m_a [src: arXiv:2007.12705]. The 2017 simulations used both a
   published fit and axionCAMB, with "negligible impact on the simulated
   flux power" [src: arXiv:1703.04683].
3. **Simulation and emulator.** 2017: GADGET-3, 20 Mpc/h, 2 × 768³, five
   masses (1, 4, 5.7, 15.7, 30 × 10⁻²² eV, chosen to share k_1/2 with
   1–3.87 keV thermal relics), grids in T₀, γ, σ8, n_eff, z_rei, UV
   fluctuations and τ_eff, interpolated around a fiducial model [src:
   arXiv:1703.04683]. 2020: Bayesian-optimised Gaussian-process
   emulator, which the authors contrast with Taylor-expansion
   interpolation that "can bias power spectrum estimation and weaken
   parameter constraints" [src: arXiv:2007.12705]. 2026: MP-Gadget,
   10 Mpc/h, 2 × 512³, convergence within 10% (at most 15%); Latin
   hypercube in (m_FDM, f_FDM); a two-stage neural emulator that first
   predicts the CDM flux power and then the flux transfer function
   T_f²(k_f), so that weak fuzzy effects are not absorbed by thermal
   parameters and the CDM limit is exact; ten held-out simulations for
   validation; patchy-reionisation and Si III corrections [src:
   arXiv:2606.06969 Sects. 3.1–3.2].
4. **IGM priors.** 2020: no change of T₀ above 5000 K or of u₀ above
   10 eV/m_p between adjacent bins; Gaussian T₀ priors of width 3000 K
   around the fiducial model; Gaussian prior on the optical-depth
   rescaling (1 ± 0.05); Planck-motivated priors on n_s and A_s [src:
   arXiv:2007.12705]. 2026: the same continuity prior with 5 eV/m_p,
   Gaussian T₀ priors of width 1000 K [src: arXiv:2606.06969 Sect. 4].
5. **Mass prior.** 2017: the posterior is built on 1/m_FDM [src:
   arXiv:1703.04683 Fig. 2]. 2020: uniform in log m_a over [−22, −19],
   which the authors "argue is less informative than in previous
   studies ... where the prior is usually uniform in m_a⁻¹" [src:
   arXiv:2007.12705]. 2026: uniform in log₁₀ m_FDM and in f_FDM [src:
   arXiv:2606.06969 Sect. 4].

### Step 5. Fuzzy dark matter as all of the dark matter: dwarf heating
<!-- key: step-5-fuzzy-dark-matter-as-all-of-the-dark -->

The ultra-faint-dwarf limit (Dalal & Kravtsov 2022, arXiv:2203.05750
[src]) is a simulation-based inference:

1. **Potential.** The wave function is built as a sum of eigenfunctions
   of a static NFW potential, accurate to first order in perturbation
   theory; results depend mainly on the mass inside the half-light
   radius, so the halo is parameterised by v_1/2 ≡ [GM(r_1/2)/r_1/2]^(1/2)
   and v_max, the latter fixed as a multiple of v_1/2 because the
   posterior is "nearly independent" of it [src: Sects. II–III].
2. **Solitons left out.** Solitons "can enormously enhance heating", but
   their masses are uncertain, so the limits use simulations without
   them; this "significantly weakens" the bound [src: Sect. II].
3. **Stars.** Test particles with an exponential projected profile and
   isotropic Maxwellian velocities from the Jeans equation, evolved for
   10 Gyr; the initial scale length r₀ is a nuisance parameter standing
   for star formation and baryonic heating [src: Sect. II].
4. **Likelihood.** p_vel from the line-of-sight velocity distribution of
   500 projections against each star's measured velocity (Eq. 2), times
   a Gaussian on the projected half-light radius (Eq. 3), p_tot =
   p_vel × p_size (Eq. 4); stellar positions are not modelled because the
   spectroscopic selection function is unknown [src: Sect. III].
5. **Priors.** Uniform r₀ (0–37.5 pc Segue 1, 0–50 pc Segue 2) and v_1/2
   (1–12.5 and 1–5 km/s); the result is not sensitive to them; uniform
   prior on 1/m_FDM, i.e. ∝ m_FDM⁻², which "heavily favours light FDM
   masses and strongly disfavours CDM" and so makes the limit
   conservative [src: Sects. III–IV].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Half-mode mapping from warm dark matter
<!-- key: half-mode-mapping-from-warm-dark-matter -->

Before dedicated simulations, fuzzy limits were obtained by matching
k_1/2 with a thermal-relic limit. With simulations of both: the XQ-100
WDM limit of 1.34 keV maps reasonably at k_1/2, but the HIRES/MIKE
limit of 4.7 keV "translates into a FDM limit which is much weaker than
the one that would be obtained using the k_1/2 mapping"; k_0.75 (power
at 75% of ΛCDM) maps better at higher masses, because the cut-off moves
into more non-linear scales; the conclusion holds for the 1D linear
power too (arXiv:1703.04683 [src]). The fuzzy cut-off in the flux power
shows "no significant degeneracies" with the other parameters [src].

### Gaussian-process against neural emulator, glass against grid
<!-- key: gaussian-process-against-neural-emulator-glass -->

The 2026 pure-fuzzy limit (1.9 × 10⁻²¹ eV) is an order of magnitude
below the 2020 one (2 × 10⁻²⁰ eV) on the same type of data. The 2026
authors give two possible reasons: glass initial conditions for the gas
in 2020 against offset grids in 2026, and a Gaussian-process emulator
optimised for the narrow pure-fuzzy posterior against a two-stage
neural emulator built for the broad mixed posterior [src:
arXiv:2606.06969 Sect. 4.1]. Both use log-uniform mass priors (above),
so the prior does not explain that gap [der: from the priors read]. The
2020 authors attribute their gain over 2017 to k_max = 0.2 instead of
0.08 s/km, the emulator, a thermal model in which T₀ and γ are tied to
the heating history through u₀, and the log prior; with k_max = 0.126
or 0.08 s/km their limit falls to log₁₀ m > −20.24 or −20.64 [src:
arXiv:2007.12705].

### Prior on the mass
<!-- key: prior-on-the-mass -->

A uniform prior on 1/m weights light masses (∝ m⁻² in m, as stated in
arXiv:2203.05750 Sect. IV [src]) and gives a conservative lower limit;
a log-uniform prior weights them as m⁻¹ [der: Jacobian of log m] and is
called less informative in arXiv:2007.12705. A lower limit has to be
quoted with its prior and its range (−22 to −19 there), because the
range sets the mass that counts as "indistinguishable from CDM". The
2026 analysis adds a frequentist check: a Neyman construction with a
profile-likelihood statistic gives m_FDM > 1.1 × 10⁻²¹ eV against the
Bayesian 1.9 × 10⁻²¹ eV, "suggesting that our constraint is not
primarily driven by prior-volume effects" [src: arXiv:2606.06969 Sect.
4.1].

### Thermal history in the 2017 analysis
<!-- key: thermal-history-in-the-2017-analysis -->

Power-law T(z) gives 37.5 × 10⁻²² eV; temperature jumps up to 5000 K
between bins 0.2 apart give 20.0 × 10⁻²² eV, called "the most
conservative" because such jumps are not plausible; Gaussian Planck
priors on n_eff and σ8 move the combined limit to 32.2 × 10⁻²² eV [src:
arXiv:1703.04683]. The 2020 analysis instead ties the instantaneous
temperature to the heating history and finds no significant degeneracy
between log m_a and T₀ [src: arXiv:2007.12705]. The 2026 posterior has
a secondary feature at log₁₀ m ≈ −20.8 compensated by low u₀ [src:
arXiv:2606.06969 Sect. 4.1].

### One-fluid against two-fluid EFT for a sub-component
<!-- key: one-fluid-against-two-fluid-eft-for-a-sub -->

The 2023 BOSS analysis puts the axion in the linear spectrum only and
reports a 2.7σ preference at 10⁻²⁶ eV from BOSS alone
(`results.md#sub-component-upper-limits-on-the-axion`); the 2026 DESI
analysis builds a two-fluid model with an axion bias b_a and two extra
counterterms, and adds, as a proof of principle, theory priors that
scale with the fraction, b_a ~ 𝒩(0, (b_c f_ax)²) and c ~ 𝒩(0,
(60 f_ax)²) (Eq. 10), because galaxies should be proportionally less
sensitive to a small sub-component [src: arXiv:2607.11876 Sect. III.4].
The DESI-only runs use a BBN prior on Ω_bh² (0.02218 ± 0.00055), a
Gaussian n_s prior (0.9649 ± 0.0422) and τ fixed at 0.0544, with Σm_ν
fixed at 0.06 eV; allowing larger neutrino masses "would yield tighter
constraints on the ULA density" [src: Sect. III.4].

### Halo model for CMB lensing
<!-- key: halo-model-for-cmb-lensing -->

The calibration simulations are sparse: 10⁻²⁵–10⁻²¹ eV at a fixed 10%
fraction, and fractions 0–0.3 only at 10⁻²⁴·⁵ eV; the model
interpolates between them, uses the full (not de-wiggled) spectrum in
the halo mass function because de-wiggling algorithms create spurious
features with axions, which raises P_m by a percent near k = 0.1 h/Mpc,
and is rescaled by 1.25% in C_L^φφ to match the ΛCDM emulator; it has
no baryonic feedback and treats massive neutrinos through a
multiplicative correction, with Σm_ν fixed at 0.06 eV [src:
arXiv:2606.06410 Sect. II.1, IV.1, Appendix B].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Fluid switch | m_a = 3H; matching time insensitive to δτ = 10/m | axionCAMB scheme | arXiv:1410.2896 | Sects. III.3–III.4 |
| Mass prior, CMB + galaxies | −33 < log₁₀(m_a/eV) < −22 | 2015 | arXiv:1410.2896 | Eq. 39 |
| Quantum-pressure scale vs data | k_J = 64.7 h/Mpc (10⁻²² eV, z = 5.4) vs k_max = 12.7 h/Mpc | Lyα 2017 | arXiv:1703.04683 | main text, footnote 1 |
| Masses simulated, 2017 | 1, 4, 5.7, 15.7, 30 × 10⁻²² eV | Lyα | arXiv:1703.04683 | Simulations |
| k_max and its effect, 2020 | 0.2 s/km; 0.126 → log m > −20.24; 0.08 → −20.64 | Lyα | arXiv:2007.12705 | footnote 4 |
| Mass prior, 2020 | log(m_a/eV) ∈ [−22, −19] | Lyα | arXiv:2007.12705 | Model |
| Half-mode mass of the 2020 limit | 7.2 × 10⁷ M⊙ | Lyα | arXiv:2007.12705 | Results |
| Simulations, 2026 | 10 Mpc/h, 2 × 512³, 10⁴ mock spectra; convergence 10% (15% worst) | Lyα | arXiv:2606.06969 | Sect. 3.1 |
| Frequentist check, 2026 | > 1.1 × 10⁻²¹ eV (Neyman, profile) vs > 1.9 × 10⁻²¹ eV (Bayesian) | Lyα | arXiv:2606.06969 | Sect. 4.1 |
| Fraction beyond reach, 2026 | no useful f_FDM limit for log₁₀ m ≳ −20 | Lyα | arXiv:2606.06969 | abstract |
| Dwarf simulation length; projections | 10 Gyr; 500 | dwarf heating | arXiv:2203.05750 | Sects. II–III |
| Dwarf limit with soliton-free potentials | > 3 × 10⁻¹⁹ eV (99%) | Segue 1 + 2 | arXiv:2203.05750 | Sect. IV |
| Same with Ursa Major III/UNIONS I, if a galaxy | > 8 × 10⁻¹⁸ eV (95%) | update | May, Dalal & Kravtsov 2025, arXiv:2509.02781 | abstract |
| Soliton enhancement in halo model | up to ~30% in P_aa at k ~ 0.1–1 h/Mpc, 10⁻²⁴–10⁻²⁵ eV | ACT lensing | arXiv:2606.06410 | Sect. II.1 |
| Halo-model accuracy | to k ~ 10 h/Mpc in mixed cosmologies | ACT lensing | arXiv:2606.06410 | Sect. II.1 |
| Nested sampling | 50 live points × 11 parameters; dlogz < 0.001 | ACT lensing | arXiv:2606.06410 | Sect. IV.2 |
| Sub-component theory priors | b_a ~ 𝒩(0, (b_c f_ax)²); c_ca, c_aa ~ 𝒩(0, (60 f_ax)²) | DESI full shape | arXiv:2607.11876 | Eq. 10 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Mapping instead of simulating.** A k_1/2 translation of a WDM limit
  overstates the fuzzy limit at high masses (arXiv:1703.04683). Test:
  dedicated simulations, or at least k_0.75.
- **Quantum pressure in mixtures.** For a light fuzzy component in a
  mixture, the local fuzzy fraction near mean density can exceed the
  global one, so quantum pressure may add suppression that modified
  initial conditions miss; the 2026 authors expect their f_FDM limits to
  be conservative for that reason, but state that the size "requires
  dedicated simulations" [src: arXiv:2606.06969 Sect. 2.3].
- **Emulator absorbing the signal.** A one-stage emulator lets thermal
  parameters absorb weak fuzzy effects at large mass; the two-stage
  design fixes the CDM limit; validate on held-out simulations
  (arXiv:2606.06969 Sect. 3.2).
- **Sampling the mass.** Metropolis–Hastings fails with m_a free;
  marginalising over a mass range mixes models with different
  degeneracies (arXiv:2606.06410 Sect. IV.2, arXiv:2301.08361 Sect. 3.4).
- **Uncalibrated non-linear model.** halofit applied to axions can
  produce spurious limits (arXiv:1410.2896 Sect. V.1); the halo model is
  calibrated at few points in (m_a, fraction) and has no baryonic
  feedback (arXiv:2606.06410 Sect. II.1).
- **Degeneracies.** For m_a ≤ 10⁻²⁸ eV the Jeans scale suppresses all
  BOSS wavenumbers alike, degenerate with A_s and b₁; at 10⁻²⁵ eV the
  axion also reduces fingers of God, degenerate with the corresponding
  counterterm [src: arXiv:2301.08361 Sect. 2.2.3]. At 10⁻²⁹ eV the field
  acts as dark energy until after recombination and is constrained
  through the distance to last scattering [src: arXiv:2607.11876 Fig. 4
  caption]. Fixing Σm_ν at 0.06 eV is conservative for the axion density
  in the DESI analysis [src: Sect. III.4].
- **Dwarf-heating assumptions, and the tests.** The perturbative
  wave function is checked against full Schrödinger–Poisson runs, which
  give stronger heating, so the perturbative bound is conservative; the
  tidal radius of Segue 1 is much larger than the galaxy; self-
  interactions cannot evade the bound given large-scale-structure limits
  (arXiv:2509.02781 abstract [src]). The other side: Milky Way tides,
  including the LMC, "significantly alleviate" the tension for Fornax at
  m_a ~ 10⁻²² eV (Yang et al. 2025, arXiv:2507.01686 abstract [src]);
  allowing a diverse core–halo relation in Jeans analyses of eight
  dwarf spheroidals opens a second allowed window, log₁₀(m/eV) =
  −21.81 (+0.39/−0.26), beside −19.72 (+0.64/−0.56) (Wardana et al.
  2026, arXiv:2603.07175 abstract [src]). These test different galaxies
  and different methods; neither paper read here addresses the Segue
  analysis directly.

## Reading list
<!-- key: reading-list -->

- Foundation, linear theory: Hlozek et al. 2015, arXiv:1410.2896 — field
  to fluid switch, c_a², mass and density priors.
- Method, Lyα: Iršič et al. 2017, arXiv:1703.04683 — first dedicated
  simulations, quantum-pressure argument, test of the k_1/2 mapping.
- Application, Lyα: Rogers & Peiris 2020, arXiv:2007.12705 — emulator,
  physical IGM model, log prior, k_max test.
- Application and critique, Lyα: Liu, Gong & Zhou 2026,
  arXiv:2606.06969 — mixed models, two-stage emulator, reasons for the
  weaker limit, frequentist check.
- Method, dwarfs: Dalal & Kravtsov 2022, arXiv:2203.05750 — heating
  simulations, likelihood, conservative choices.
- Update and tests, dwarfs: May, Dalal & Kravtsov 2025, arXiv:2509.02781
  (abstract) — Schrödinger–Poisson check, tides, UMa III.
- Critique, dwarfs: Yang et al. 2025, arXiv:2507.01686; Wardana et al.
  2026, arXiv:2603.07175 (abstracts) — tides; core–halo diversity.
- Method, galaxies: Rogers et al. 2023, arXiv:2301.08361 — EFT with
  axions in the linear input; fixed-mass sampling.
- Method, galaxies: Verdiani et al. 2026, arXiv:2607.11876 — two-fluid
  EFT, axion bias and counterterms, theory priors.
- Method, lensing: Laguë et al. 2026, arXiv:2606.06410 — axion halo
  model, emulator, nested sampling with free mass.

## Not verified
<!-- key: not-verified -->

- The full Schrödinger–Poisson comparison, tidal test and UMa III limit
  of arXiv:2509.02781, and the methods of arXiv:2507.01686 and
  arXiv:2603.07175, were read at abstract level only.
- The axionHMcode equations beyond Eqs. 13–14 of arXiv:2606.06410, and
  the simulation papers it is calibrated on, were not read.
- The fuzzy transfer-function fit used in the 2017 simulations (its
  ref. [1]) and the T(k) polynomial coefficients of arXiv:2007.12705
  were not read.
- The two-fluid EFT derivation paper behind arXiv:2607.11876 (its ref.
  [78]) was not read.
- The ACT DR6 section named in "From" (VI.3) was not read for this
  dossier; whether the ACT extended-model paper uses the same axion code
  was not checked.
- Strong-lensing (arc granule) limits on fuzzy dark matter are covered
  only in L2 (`results.md#all-of-the-dark-matter-lower-limits-on-the`).
