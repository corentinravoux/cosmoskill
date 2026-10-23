# BBN — systematics

Scope: the canonical systematic errors of the primordial-abundance
determinations, of the nuclear and weak inputs and of the BBN calculation,
each with mechanism, size, mitigation, validation and reference.
Snapshot: 2026-10-16

Flags: `[src]` abstract read this session; `[src: Sect. n]`, `[src: Table n]`
body read; `[sec]` named secondary source; `[der]` derived here.

## 1. Deuterium
<!-- key: deuterium -->

- **Mechanism: continuum placement.** The quasar continuum near each H I and
  D I line sets the absorbed column. Cooke et al. fit the continuum jointly
  with the absorber (Legendre polynomials of degree ≲ 4, degree 8 near Lyα),
  a zero-level parameter per dataset and relative velocity shifts between
  datasets, so the D/H error includes continuum uncertainty
  (arXiv:1710.11129) [src: Sect. III].
- **Mechanism: interlopers and component structure.** Unrelated low-column
  Lyα absorption can contaminate D I: in Q1009+2956 this held the D/H error
  at 17% despite S/N 147 per pixel (arXiv:1706.09512) [src]. The D–H isotope
  shift is −81.6 km s⁻¹, so clouds with larger Doppler motions blend D into
  H (arXiv:2409.06015) [src: Sect. 3.1].
- **Mechanism: low H I column.** For log N(H I) ≈ 18, modelling uncertainty
  becomes the main term of the error budget (Guarneri et al. 2024,
  arXiv:2402.05586) [src: abstract]. Damped and sub-damped systems are preferred
  because the H I column is fixed by the damping wings.
- **Mechanism: line-profile physics.** The Voigt profile is insufficient for
  very high column-density damped systems; a Kramers–Heisenberg profile with
  thermal broadening (KHT) produces wing asymmetries that, if unmodelled,
  bias D/H, and is implemented in VPFIT (Lee, Webb & Carswell 2020,
  arXiv:1910.02913) [src].
- **Ionisation and astration.** D I/H I equals D/H to within 0.1% through
  charge exchange; astration changes D/H by ≲ 0.1% below ~1% solar
  metallicity (arXiv:2409.06015) [src: Sect. 3.1].
- **Size.** In J1332+0052 the systematic term is 0.012 dex against
  0.008 dex statistical (arXiv:2401.12797) [src: abstract].
- **Sample selection.** Different compilations give different means:
  (2.527 ± 0.030) × 10⁻⁵ for seven homogeneously analysed systems
  (arXiv:1710.11129) [src: abstract] against (2.545 ± 0.025) × 10⁻⁵ for 13
  systems after least-trimmed-squares rejection (arXiv:1706.09512)
  [src: abstract]. State the sample.
- **Validation.** The seven systems of the precision sample, spanning
  different metallicities, are consistent with one value
  (arXiv:1710.11129) [src: Sect. V.1].

## 2. Helium-4
<!-- key: helium-4 -->

- **Mechanism: degeneracies of the emission-line model.** Temperature,
  density, optical depth, underlying He stellar absorption, neutral-H
  collisional correction and emissivities are fitted per target; optical
  lines alone leave temperature and density degenerate. He I 10830 breaks
  the density degeneracy and reduced the Y_P error by over 50%
  (arXiv:1503.08146) [src: abstract].
- **Size: emissivities.** Switching to the Del Zanna & Storey He
  emissivities raised y⁺ by 0.9% on average (40 of 41 targets up), 0.95% with
  the updated Hβ emissivity (arXiv:2601.22238) [src: Sect. VI.2].
- **Size: extrapolation.** On the same 41 LBT targets, weighted least
  squares gives 0.2451 ± 0.0022 and linmix with intrinsic scatter gives
  0.2466 ± 0.0025; the slope is unconstrained (14 ± 12), so the team uses
  a weighted average of the 15 lowest-metallicity targets
  (arXiv:2601.22238) [src: Sect. VII.3]. Regressing y rather than Y removes
  the dependence on Z (arXiv:2601.22238 citing Hsyu et al.)
  [src: Sect. VII.3].
- **Mechanism: sample.** Extremely metal-poor galaxies pull Y_P low:
  EMPRESS finds 0.2370 and 0.2402, ~1σ below most earlier estimates
  (arXiv:2203.09617, arXiv:2506.24050) [src]. Izotov et al. (2014) found
  0.2551 ± 0.0022 from a selection on EW(Hβ) > 150 Å and O²⁺/O > 0.8
  (arXiv:1408.6953) [src]. Intrinsic scatter is significant in the LBT
  sample (σ_int = 0.00262 ± 0.00048) (arXiv:2601.22238) [src: Sect. VII.3].
- **Mechanism: metallicity determination.** The O/H used for the
  extrapolation depends on the H II-region temperature structure (t²
  formalism, arXiv:2105.12260) [src].
- **Validation.** χ² goodness-of-fit screening (47/54 = 87% pass at 95% in
  the LBT sample) and flags for optical depth, stellar absorption,
  temperature agreement and N/O (arXiv:2601.22238) [src; Sect. V titles].
  An independent route, He I absorption in an intergalactic cloud, is not
  yet competitive (arXiv:1810.06561) [src].
- **Referee expects.** The sample, the extrapolation method and its
  alternative, and the emissivities; Aver et al. 2015 and 2026,
  Izotov et al. 2014, EMPRESS, Hsyu et al. 2020.

## 3. Helium-3
<!-- key: helium-3 -->

- **Mechanism.** ³He is both produced and destroyed in stars; inferring the
  primordial value needs a chemical-evolution model whose yields carry
  factor ~2–3 uncertainties (arXiv:2510.08689) [src]. The 2022 Orion
  inference excludes model error (arXiv:2203.11256) [src].
- **Mechanism: ionisation correction** in radio ³He⁺ measurements, applied
  with ⁴He radio recombination lines and nebular models (NEBULA)
  (arXiv:1810.09422) [src].
- **Validation.** Time variability of He I* absorption in Orion limited to
  < 0.17% yr⁻¹ (2σ), supporting radiative equilibrium (arXiv:2605.00122)
  [src: abstract].

## 4. Lithium-7
<!-- key: lithium-7 -->

- **Mechanism: stellar depletion.** Atomic diffusion moderated by extra
  mixing explains heavy-element trends between dwarfs and giants in
  globular clusters and implies plateau stars were born with ~0.3 dex more
  Li (Korn 2021, arXiv:2111.00913) [src: abstract]. Pre-main-sequence
  depletion with cold protostellar accretion from small seeds can exhaust
  Li, while hot accretion converges to standard models within 1 Myr
  (Tognelli et al. 2020, arXiv:2004.14857) [src: abstract].
- **Mechanism: effective temperature scale.** Different T_eff methods differ
  by up to 350 K, i.e. 0.3 dex in A(Li); anchoring to the infrared flux
  method removes much of it (Norris et al. 2023, arXiv:2303.11497) [src: abstract].
- **Mechanism: dispersion and "meltdown".** Below [Fe/H] ≈ −3 the scatter
  grows and A(Li) falls below the plateau (arXiv:2303.11497) [src].
- **Environment test.** The plateau also exists in ω Cen, a probable
  accreted dwarf galaxy (arXiv:1008.1817) [src]; interstellar Li in the SMC
  near the BBN value is free of stellar-atmosphere effects but requires
  fine-tuned depletion if standard BBN holds (arXiv:1207.3081) [src].
- **Nuclear route closed in the main channels.** n_TOF ⁷Be(n,α) and
  ⁷Be(n,p) leave the problem unsolved (arXiv:1606.09420,
  arXiv:1803.05701) [src]; PRIMAT 2021 rate updates bring "no relief"
  (arXiv:2011.11320) [src: Sect. 1].

## 5. Nuclear rates
<!-- key: nuclear-rates -->

- **Mechanism.** At fixed η, faster deuterium burning lowers D/H, so the
  inferred Ω_b h² falls; the d(p,γ)³He rate and the d+d transfer rates set
  the BBN-calculation term of the error budget (arXiv:2401.15054)
  [src: Sect. 4.1].
- **Size.** Changing d(p,γ)³He from the Marcucci et al. ab-initio rate to the
  Adelberger et al. empirical rate moves 100 Ω_b h² from
  2.166 ± 0.015 ± 0.011 to 2.235 ± 0.016 ± 0.033 (first error D/H, second
  BBN calculation) (Cooke et al. 2018, arXiv:1710.11129) [src: Sect. V.2,
  Eqs. 12, 14]. Adding the LUNA rate to PArthENoPE moved Ω_b h² by −0.9σ;
  ab-initio versus data-driven rates differ by ~1.0σ
  (arXiv:2401.15054) [src: Sect. 4.1].
- **Mitigation.** Marginalise over rate uncertainties (PRyMordial; error
  0.00055 against 0.00021–0.00034 without) (arXiv:2401.15054)
  [src: Sect. 4.1]. Gaussian-process fits avoid the over-prediction of D/H
  that low-degree polynomial fits produce in validation tests
  (arXiv:2604.16600) [src].
- **Validation.** Rerun with ab-initio and with data-driven rates; quote both
  or the marginalised result.
- **What would fix it.** New d(d,n)³He and d(d,p)t S-factor data at
  0.1–0.6 MeV (arXiv:2604.16600) [src: abstract].
- **Electron screening** affects laboratory, not primordial, cross sections;
  indirect (Trojan Horse) measurements give the bare S-factor and a
  screening potential (arXiv:1503.08672) [src].
- **Referee expects.** Coc et al. 2015 (arXiv:1511.03843), LUNA
  (doi:10.1038/s41586-020-2878-4), Pisanti et al. 2021 (arXiv:2011.11537),
  Yeh et al. 2021 (arXiv:2011.13874), Pitrou et al. 2021 (arXiv:2011.11320).

## 6. Neutron lifetime
<!-- key: neutron-lifetime -->

- **Mechanism.** τ_n enters Y_P with exponent 0.730 and D/H with 0.413
  (arXiv:2303.04140) [src: Eqs. 13–14]. The beam and bottle averages differ
  by 8.6(2.1) s (arXiv:1802.01804) [src: abstract]; the best Y_P
  measurement has an error of 0.0013 (arXiv:2601.22239) [src: abstract].
- **Consequence.** Choosing the beam rather than the bottle average moves
  the predicted Y_P, through the exponent above, by an amount of the order
  of the error of the best Y_P measurement [der: exponent applied to the
  beam–bottle difference; no paper read here states the shift].
- **Beam-method systematics.** Absolute neutron fluence dominated the 2005
  NIST error (2.7 s), reduced by a direct efficiency measurement
  (arXiv:1309.2623) [src: abstract]; charge exchange of trapped protons with residual
  H₂ occurs but is "unlikely to have significantly affected" the NIST result
  (Caylor et al. 2025, arXiv:2506.01682) [src].
- **Bottle-method systematics.** Wall losses in material traps; magnetic
  traps (UCNτ, τSPECT) remove them and replace them with spin-flip and
  phase-space-evolution effects (arXiv:2503.15239) [src].
- **Exotic explanations.** A dark decay channel is excluded with high
  confidence using neutron-decay correlation data (Dubbers et al. 2018,
  arXiv:1812.00626) [src]; the τ_n–g_A relation bounds exotic branching
  ratios below 0.27% (arXiv:1802.01804) [src: abstract].
- **Mitigation for BBN.** State the τ_n adopted and whether its error is
  inflated for the beam–bottle spread; Y_P observations are not yet precise
  enough to discriminate, which needs σ(Y_P) = 0.001 (arXiv:2303.04140)
  [src: abstract].

## 7. Code and network choices
<!-- key: code-and-network-choices -->

- **Mechanism.** Codes differ by rate set, weak-rate corrections, neutrino
  decoupling treatment, and the N_eff assumed in tabulated outputs. The
  dominant code-to-code difference in Ω_b h² is the deuterium-burning rate
  set "characterized ... by the underlying code" (arXiv:2401.15054) [src].
- **Size.** Up to ~1σ in Ω_b h² between rate philosophies; see `results.md`
  §7 (arXiv:2401.15054) [src: Sect. 4.1].
- **Helium.** With all weak-rate corrections, PRIMAT claims "a 10⁻⁴
  accuracy" on Y_P = 0.24709 ± 0.00017, the error coming from the τ_n
  uncertainty (arXiv:1801.08023) [src: abstract; Sect. V.4]; codes without
  the corrections differ by more than this.
- **Mitigation.** Name the code, version and rate set with every BBN prior;
  use a code that marginalises over rates, or quote the spread.

## 8. Referee checklist
<!-- key: referee-checklist -->

1. D/H: which systems, which compilation (seven systems, arXiv:1710.11129
   [src: abstract]; 13, arXiv:1706.09512 [src: abstract]; nine or 17,
   arXiv:2401.12797 [src: Sect. 5]), and the continuum, interloper and
   component-structure treatment.
2. Y_P: which group and sample; weighted average or regression; intrinsic
   scatter; emissivities; He I 10830 used.
3. Lithium: T_eff scale; whether stellar depletion is modelled; plateau
   value adopted.
4. Rates: which d(p,γ)³He, d(d,n)³He and d(d,p)t evaluation; ab-initio or
   data-driven; marginalised or not.
5. Code and version (PArthENoPE v2 or v3, PRIMAT 2018 or 2021, PRyMordial
   mode, LINX, AlterBBN), and the N_eff assumed in any tabulated Y_P.
6. τ_n value and whether the beam–bottle spread is propagated.
7. N_ν or N_eff baseline (3, or 3.044 as in arXiv:2603.13226
   [src: abstract]) stated.
8. BBN-only, CMB-only and joint results kept apart; whether Y_P is tied to
   ω_b by BBN in the CMB fit.
9. A "BBN prior" quoted with code, rates and abundances; full likelihood or
   compressed.
10. For new physics: which abundances constrain which epoch (⁴He and D
    early, ³He/D late for decays; arXiv:hep-ph/0604251) and whether negative
    ΔN_eff is treated consistently (arXiv:2507.23354).

## Not verified
<!-- key: not-verified -->

- Before the numbers pass of 2026-10-23 §7 said that the weak-rate
  corrections fix Y_P to ±0.00017 in PRIMAT; arXiv:1801.08023 (Sect. V.4)
  attributes σ(Y_P) ≃ 0.00017 to the neutron-lifetime uncertainty, and the
  statement now says so. The Y_P shift from the beam–bottle choice, given
  before as a value computed from the τ_n exponent, is not stated by any paper read
  here and was removed.
- An error budget table for D/H across all systems was not read; only
  per-system statements.
- The LBT Y_p Project sample-testing results per flag (Sect. V) were not
  read beyond titles.
- A quantitative stellar-depletion budget for the Spite plateau beyond the
  globular-cluster estimate was not read.
