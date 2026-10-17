# Primordial deuterium from quasar absorbers — cosmo-bbn dossier

Scope: how a D/H value is extracted from one quasar absorber (system
selection, joint absorber–continuum model, Doppler-parameter ties, blinding,
error budget) and how single systems are combined into (D/H)_P, with the
choices that separate the groups and what each costs.
Snapshot: 2026-10-17.
From: Cooke 2024 review, Sect. 3.1 and 6.3; Keck/HIRES, VLT/UVES and
ESPRESSO groups.

Already in L2, not repeated here: the abundance values per system and per
compilation in `results.md#primordial-deuterium`; the list of programmes,
instruments and fitting codes in
`surveys-and-data.md#deuterium-quasar-absorption-line-programmes`; the
mechanisms (continuum, interlopers, low column, KHT profile, astration) in
`systematics.md#deuterium`; the conversion from D/H to Ω_b h² and its rate
dependence in `results.md#baryon-density-from-bbn` and
`systematics.md#nuclear-rates`.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Select the absorber
<!-- key: step-1-select-the-absorber -->

The "Precision Sample" criteria of Cooke et al. (2014, arXiv:1308.3240)
[src: Sect. II.2.1] are the reference that later papers test against:

1. H I Lyα with Lorentzian damping wings, log N(H I)/cm⁻² ≥ 19, so that
   the wings fix the total H I column "independently of the cloud model".
2. Lyα wings not strongly blended: the edges of neighbouring strong H I
   troughs at least 500 km s⁻¹ away, and modelled simultaneously.
3. At least two resolved, apparently unblended, optically thin D I
   transitions, so that N(D I) does not depend on the cloud model.
4. Echelle data with R ≥ 30 000 (v_FWHM ≤ 10 km s⁻¹) and S/N ≳ 10 per
   ~3 km s⁻¹ pixel at Lyα and at the weakest D I line used.
5. Several unblended metal lines of one species (ideally O I, Si II) when
   only one optically thin D I line exists, to fix the velocity structure
   and the partly ionised gas.

Why damped systems: the damping wings fix N(H I), and the many D I Lyman
lines of widely varying oscillator strength pin N(D I); "neither of these
two advantages applies to Lyman limit systems", whose N(H I) can be three
orders of magnitude lower [src: arXiv:1308.3240, Sect. III.2]. Four
literature systems passed in 2014 [src: Sect. II.2.1]. Cooke et al. (2018)
restated the criteria with S/N > 10 per pixel and N(H I) > 10¹⁹ cm⁻², and
added that all systems were analysed by the same group, because other
determinations "may introduce unaccounted for systematic errors because of
the different analysis techniques" (arXiv:1710.11129) [src: Sect. IV.1].

Lower-column systems are still analysed by other groups: the ESPRESSO
system towards PKS1937−101 has log N(H I) = 17.923 ± 0.015
(Guarneri et al. 2024, arXiv:2402.05586) [src: Sect. 3.2], and Q1009+2956
has 17.362 (Zavarygin et al. 2018, arXiv:1706.09512) [src: Table 5].

### Step 2. Build the joint model
<!-- key: step-2-build-the-joint-model -->

Every group fits Voigt profiles to H I, D I and metal lines together; the
codes and ties differ.

- **Components and broadening.** Each component has a redshift, a column
  density per species and a total Doppler parameter
  b_total² = b_turb² + 2 k_B T_gas/m_ion (arXiv:1710.11129, Eq. 1), with
  b_turb the turbulent part, T_gas the gas temperature, m_ion the mass of
  the absorbing ion and k_B Boltzmann's constant. The same form is Eq. 1 of
  Kislitsyn et al. (2024, arXiv:2401.12797), who fit b_turb and T
  independently in each component [src: Sect. 3.1].
- **Ties (Cooke et al.).** All species share redshift and b_turb, while the
  D I and H I thermal components are fitted separately, because a single
  T and b_turb per component is "too simplistic" at the S/N of D/H data
  [src: arXiv:1710.11129, Sect. III]. In J1358+6522 a single cloud with
  common turbulence and thermal width ∝ m^{-1/2} could not fit metals, D I
  and H I; a second component reduced χ²_min by ≃ 660 (arXiv:1308.3240)
  [src: Sect. III.3, footnote 8].
- **Ties (ESPRESSO).** Metals, H and D share the number of components,
  redshifts and Doppler broadening; column densities are free; the summed
  H I and D I columns are fitted directly [src: arXiv:2402.05586,
  Sect. 3.2].
- **One D/H for the whole absorber.** All three groups force every H I
  component to share one D I/H I ratio [src: arXiv:1308.3240, Sect. III.2;
  arXiv:2401.12797, Sect. 3.1; arXiv:2402.05586, Sect. 3.2]; the ESPRESSO
  paper notes this assumes that any D I depletion affects all components
  equally [src: Sect. 3.2].
- **Metallicity.** [O/H] from N(O I)/N(H I), because O I traces H I through
  charge transfer, summed over the components where O I is detected; with
  log(O/H)_⊙ + 12 = 8.69 this gives [O/H] = −2.769 ± 0.028 for Q1243+307
  [src: arXiv:1710.11129, Sect. III].

### Step 3. Fit the continuum, zero level and instrument with the lines
<!-- key: step-3-fit-the-continuum-zero-level-and -->

| Nuisance | Cooke et al. (ALIS) | Kislitsyn et al. (spectro) | Guarneri et al. (VPFIT) |
|---|---|---|---|
| Continuum | Legendre polynomials, degree ≲ 4, degree 8 near Lyα, fitted with the lines [src: arXiv:1710.11129, Sect. III] | spline from absorption-free regions for metals; Chebyshev of order 5 (Lyα), 3 (Lyβ), 1 (other Lyman lines) fitted with the lines [src: arXiv:2401.12797, Sect. 3.1] | small continuum adjustments per region in VPFIT; separate test with 10 randomly perturbed continua [src: arXiv:2402.05586, Sect. 3.3.5] |
| Zero level | one global parameter per dataset (background residuals, partial covering) [src: arXiv:1710.11129, Sect. III] | — | — |
| Instrument | Gaussian instrumental profile with free FWHM [src: arXiv:1308.3240, Sect. III.2] | effective resolutions R_UVES, R_HIRES fitted [src: arXiv:2401.12797, Sect. 3.1] | — |
| Velocity offsets between spectrographs | two free global shifts [src: arXiv:1710.11129, Sect. III] | — | precomputed per region and fixed to the average [src: arXiv:2402.05586, Sect. 6.2] |

The stated reason for fitting the continuum with the absorber is that the
final D/H error then includes continuum uncertainty
[src: arXiv:1710.11129, Sect. III]; Cooke et al. 2014 judged continuum
placement the dominant systematic, ahead of instrumental profile, cloud
model and zero level [src: arXiv:1308.3240, Sect. III.2]. The Kislitsyn
team chose order five near Lyα after orders 3 and 4 failed to fit and
higher orders showed no scatter in log N(H I), "a compromise between the
unacceptably simple model and the overfitting" [src: arXiv:2401.12797,
Sect. 3.3]. Different continua per dataset are allowed because the quasar
may vary over the 16 years the data span and because spectrograph
efficiency changes the apparent continuum [src: arXiv:1710.11129,
Sect. III, footnote 10].

**Fitting window.** Cooke et al. fit Lyα pixels within
−470 ≤ v/km s⁻¹ ≤ +580, where τ ≳ 0.7 (residual intensity ≲ 50%), modelling
every blend inside; outside, only pixels judged free of absorption by eye
[src: arXiv:1710.11129, Sect. III].

### Step 4. Model the interlopers
<!-- key: step-4-model-the-interlopers -->

Every D I line is cross-checked against the Lyman series of unrelated
higher-redshift H I and against metal systems on the sightline; each blend
is constrained by its unblended lines elsewhere (for example Fe II λ1608 for
an Fe II λ1063 blend on D I Ly9) [src: arXiv:1710.11129, App. A]. In
Q1243+307 three D I lines (Lyε, Ly7, Ly9) were blended; the lower-S/N
earlier data had revealed only one of these blends [src: Sect. III]. The
ESPRESSO analysis models interlopers as Lyβ or Lyγ with their Lyα
counterpart when possible, for tighter constraints [src: arXiv:2402.05586,
Sect. 3.2].

### Step 5. Blind the fit, then explore the minimum
<!-- key: step-5-blind-the-fit-then-explore-the-minimum -->

- **Cooke et al.** Only χ² and plots of the fit are shown until the model
  converges; no change to model or reduction after unblinding
  [src: arXiv:1308.3240, Sect. III.2]. In 2018: start log(D I/H I) drawn
  uniformly in (−4.7, −4.5); 2000 Monte Carlo restarts perturbed by twice
  the covariance matrix with a fresh D/H draw each, keep the lowest χ²
  [src: arXiv:1710.11129, Sect. III]. In 2014, 20 restarts gave a 0.002 dex
  error contribution and a 0.002 dex bias, corrected for
  [src: arXiv:1308.3240, Sect. III.2].
- **Kislitsyn et al.** Not fully blind; MCMC with an affine-invariant
  sampler, flat priors on b_turb, T_kin, z, log N, continuum coefficients
  and resolutions; maximum-posterior value and 68.3% highest-density
  interval [src: arXiv:2401.12797, Sect. 3.1]. Their argument: any prior
  from earlier results spans ~0.1 dex around log(D/H) = −4.61 and all
  their model variants sit inside it, so confirmation bias would act only
  at the level of choosing −4.6 against −4.4 [src: Sect. 4.2].

### Step 6. Build the per-system error
<!-- key: step-6-build-the-per-system-error -->

Three practices:

1. **Statistical only, with post-unblinding checks** (Cooke et al. 2018).
   Widening the Lyα window to ±1250 km s⁻¹ left D/H unchanged and raised
   the error by ~2.7%; four extra metal components improved χ²
   (11972/13678) and raised the error by 6.4% (0.015 → 0.016 dex); neither
   enters the quoted error [src: arXiv:1710.11129, Sects. III.1–III.2].
2. **Mixture over model variants** (Kislitsyn et al. 2024). Refit with each
   H I line region excluded, H I tied to Al II, C II, Si II or O I, one Lyα
   wing only, UVES or HIRES alone; the posterior chains of all variants are
   pooled and the 0.014 dex total error read from the pooled posterior,
   keeping "neutrality among these alternatives" [src: arXiv:2401.12797,
   Sect. 3.3]. This 0.014 dex is the quadrature sum of the 0.008 dex
   statistical and 0.012 dex systematic terms quoted in L2
   [der: √(0.008² + 0.012²) = 0.0144].
3. **Half the difference between two blending models**, added in
   quadrature: σ_sys(log D/H) = 0.08 for Q1009+2956, giving
   log(D/H) = −4.606 ± 0.066 [src: arXiv:1706.09512, Sect. 3.9]. The number
   of components was chosen with the corrected Akaike criterion
   AICc = χ² + 2p + 2p(p + 1)/(n − p − 1), p parameters and n pixels;
   ΔAICc > 10 means no support [src: Sect. 3.8].

### Step 7. Combine systems into (D/H)_P
<!-- key: step-7-combine-systems-into-d-h-p -->

- **Weighted mean after a scatter test** (Cooke et al. 2018). Each value
  d_i ± σ_i is drawn from an intrinsic Gaussian of mean DH_P and width σ,
  so Pr(d_i | DH_P) is Gaussian with variance σ_i² + σ²
  (arXiv:1710.11129, Eqs. 3–5); maximising the product (Eq. 6) gives
  DH_P = −4.5976 ± 0.0072 and σ ≤ 0.027 dex (95%), with maximum-likelihood
  σ = 0 (Eqs. 7–8); the weighted mean is then quoted (Eq. 9) [src:
  Sects. IV.3, V.1]. The authors attribute the excess scatter of older
  heterogeneous samples to differing techniques and unsuitable systems
  [src: Sect. IV.3].
- **Least trimmed squares** (Zavarygin et al. 2018). Trimming fraction
  0.85 keeps k = 13 of n = 15; at each combination all errors are inflated
  in quadrature by σ_rand until χ²/dof = 1, and the combination with the
  smallest σ_rand wins; it was zero; weighted mean
  (2.545 ± 0.025) × 10⁻⁵ [src: arXiv:1706.09512, Sect. 4.2, Eq. 2]. Stated
  reason: to avoid subjective decisions on which values are "good"
  [src: same].
- **All literature values** (Kislitsyn et al. 2024). Weighted mean of all
  17 entries of their Table 4, (2.533 ± 0.024) × 10⁻⁵ (Eq. 2), "conservative
  ... in the sense that it incorporates all previous determinations"; the
  nine systems meeting the Cooke et al. 2014 criteria give
  (2.501 ± 0.028) × 10⁻⁵ (Eq. 3); 2.2σ and 1.4σ above the PRIMAT
  prediction (2.439 ± 0.037) × 10⁻⁵ respectively [src: Sect. 4.1]. They
  argue for using all data "until this presumption is demonstrated
  conclusively" [src: same].
- **All literature values, other compilation** (Guarneri et al. 2024).
  16 systems: simple mean (2.32 ± 0.4) × 10⁻⁵, weighted mean
  (2.512 ± 0.028) × 10⁻⁵; restricting to errors below 10% gives simple mean
  2.53 ± 0.09 and weighted mean 2.531 ± 0.029 (× 10⁻⁵); the weighted mean
  tracks the Precision Sample because 7 of the 16 belong to it and carry
  the smallest errors [src: arXiv:2402.05586, Sect. 6.1].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Damped systems only, or all absorbers
<!-- key: damped-systems-only-or-all-absorbers -->

- **Damped only** buys a cloud-model-independent N(H I) and many D I lines,
  and a sample with no detectable intrinsic scatter (σ ≤ 0.027 dex)
  [src: arXiv:1710.11129, Sect. IV.3]. It costs sample size: four
  literature systems qualified in 2014 [src: arXiv:1308.3240,
  Sect. II.2.1], nine by 2024 [src: arXiv:2401.12797, Table 4].
- **Lyman-limit and sub-damped systems** add redshift range (to z = 3.572)
  [src: arXiv:2402.05586, Sect. 6.1] but the error becomes systematic.
  On PKS1937−101, a ±400 km s⁻¹ Lyα window lowered log N(H I) to
  17.905 ± 0.023 and raised D/H to (2.76 ± 0.16) × 10⁻⁵, against
  (2.638 ± 0.128) × 10⁻⁵ in the base fit, because VPFIT then lowers the
  continuum [src: Sects. 3.2, 3.3.4]; with continuum adjustments this
  moves D/H by nearly 1σ [src: Sect. 6.2].
- **Same system, two analyses.** Riemer-Sørensen et al. (2017) gave
  (2.62 ± 0.05) × 10⁻⁵ for the z = 3.572 system [as listed in
  arXiv:1706.09512, Table 5]; the ESPRESSO team finds a larger error,
  (2.608 ± 0.102) × 10⁻⁵ with UVES, and argues the earlier error scaled
  anomalously (single-spectrum errors three times the joint one instead of
  √(S/N) scaling), implying ~0.11 before systematics [src:
  arXiv:2402.05586, Sects. 6.1–6.2].

### Combining spectrographs
<!-- key: combining-spectrographs -->

Joint fits of UVES, HIRES and ESPRESSO need relative velocity shifts and
separate continua. In J1332+0052 the UVES-only and HIRES-only D/H differ
by ≈ 1.7σ, traced to log N(D I) rather than N(H I) [src: arXiv:2401.12797,
Sect. 3.3]; on PKS1937−101 HIRES alone gives (2.89 ± 0.23) × 10⁻⁵, higher
than ESPRESSO or UVES, and the authors read the larger joint error as "the
increased incompatibility of the input spectra" [src: arXiv:2402.05586,
Sect. 6.2].

### Homogeneous sample or all literature
<!-- key: homogeneous-sample-or-all-literature -->

The weighted mean moves little between choices — 2.527 (seven, one group),
2.501 (nine meeting the criteria), 2.512–2.533 (16 or 17, all
literature), 2.545 (13 after LTS), all × 10⁻⁵ with errors 0.024–0.030
[src: arXiv:1710.11129, Eq. 10; arXiv:2401.12797, Eqs. 2–3;
arXiv:2402.05586, Sect. 6.1; arXiv:1706.09512, Eq. 2]. The tension
statement moves more: 2.2σ (all) against 1.4σ (nine) relative to the same
PRIMAT prediction [src: arXiv:2401.12797, Sect. 4.1]. State the sample
with the significance.

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Minimum H I column (Precision Sample) | log N(H I) ≥ 19 | Cooke et al. | arXiv:1308.3240 | Sect. II.2.1 |
| Lyα separation from strong neighbours | ≥ 500 km s⁻¹ between trough edges | Cooke et al. | arXiv:1308.3240 | Sect. II.2.1 |
| Resolution and S/N | R ≥ 30 000; S/N ≳ 10 per ~3 km s⁻¹ pixel | Cooke et al. | arXiv:1308.3240 | Sect. II.2.1 |
| Lyα fit window | −470 to +580 km s⁻¹ (τ ≳ 0.7) | Q1243+307 | arXiv:1710.11129 | Sect. III |
| Continuum polynomial | Legendre ≲ 4, 8 near Lyα | Cooke et al. | arXiv:1710.11129 | Sect. III |
| Continuum polynomial | Chebyshev 5 / 3 / 1 (Lyα / Lyβ / others) | J1332+0052 | arXiv:2401.12797 | Sects. 3.1, 3.3 |
| Restarts for the global minimum | 2000, start log(D/H) ∈ (−4.7, −4.5) | Q1243+307 | arXiv:1710.11129 | Sect. III |
| Error growth, window ±1250 km s⁻¹ | +2.7% | Q1243+307 | arXiv:1710.11129 | Sect. III.1 |
| Error growth, four extra metal components | +6.4% | Q1243+307 | arXiv:1710.11129 | Sect. III.2 |
| χ²/dof, best model | 12115/13697 ≃ 0.885 (pixel correlations ignored) | Q1243+307 | arXiv:1710.11129 | Sect. III |
| Intrinsic scatter, Precision Sample | ≤ 0.027 dex (95%) | seven systems | arXiv:1710.11129 | Eq. 8 |
| Total error, model-variant mixture | 0.014 dex | J1332+0052 | arXiv:2401.12797 | Sect. 3.3 |
| Bias from an unmodelled H I at −81.5 km s⁻¹ | Δ log(D/H) = −0.06 (not in final error) | J1332+0052 | arXiv:2401.12797 | Sect. 3.3 |
| Continuum-perturbation error | (2.639 ± 0.010) × 10⁻⁵ over 10 realisations, σ = 0.05 | PKS1937−101 | arXiv:2402.05586 | Sect. 3.3.5 |
| Blending-model systematic | 0.08 dex (half the 6a–6b difference) | Q1009+2956 | arXiv:1706.09512 | Sect. 3.9 |
| Start-parameter bias | 0.002 dex, corrected | Cooke et al. 2014 | arXiv:1308.3240 | Sect. III.2 |
| Weighted mean, nine criteria-meeting systems | (2.501 ± 0.028) × 10⁻⁵ | literature | arXiv:2401.12797 | Eq. 3 |
| Weighted mean, 17 literature values | (2.533 ± 0.024) × 10⁻⁵ | literature | arXiv:2401.12797 | Eq. 2 |
| Weighted mean, 16 literature values | (2.512 ± 0.028) × 10⁻⁵ | literature | arXiv:2402.05586 | Sect. 6.1 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Hidden H I at the D I position.** An extra H I component at
  −81.5 km s⁻¹ fits the D I lines and lowers log(D/H) by 0.06 in
  J1332+0052; "there is always such opportunity for any considered D/H
  measurement" [src: arXiv:2401.12797, Sect. 3.3]. Test: require several D I
  lines of different oscillator strength to agree, and metal-line
  kinematics that exclude the component.
- **Continuum pulled by a narrow window.** Shows as a lower N(H I) and a
  higher D/H when the Lyα window shrinks [src: arXiv:2402.05586,
  Sect. 3.3.4]. Test: refit with a wider window, as in arXiv:1710.11129,
  Sect. III.1.
- **Unidentified blends in lower-S/N data.** Only one of three blends on
  Q1243+307 was visible in older HIRES data [src: arXiv:1710.11129,
  Sect. III]. Test: S/N to the Lyman limit and a systematic cross-check of
  every D I line against all systems on the sightline (App. A).
- **Spectrograph-to-spectrograph disagreement.** 1.7σ between UVES and
  HIRES in one system [src: arXiv:2401.12797, Sect. 3.3]. Test: fit each
  spectrum alone before the joint fit.
- **Non-Gaussian noise artefacts.** Features in UVES near D I λ973 absent in
  HIRES were judged reduction artefacts and not fitted
  [src: arXiv:2401.12797, Sect. 3.3]. Test: compare the same region in a
  second instrument.
- **Underestimated χ².** Correlated neighbouring pixels are not in the error
  spectrum, so χ²/dof < 1 is expected and not a sign of overfitting
  [src: arXiv:1710.11129, Sect. III, footnote 14; arXiv:1308.3240,
  Sect. III.3, footnote 7].
- **Error that does not scale with data.** A joint-fit error three times
  smaller than single-spectrum errors signals an underestimate
  [src: arXiv:2402.05586, Sect. 6.2].
- **Under-fitted satellite components found after unblinding.** Handled in
  Q1243+307 by refitting and reporting the change without altering the
  blind value [src: arXiv:1710.11129, Sect. III.2].
- **Damping-wing shape.** A Kramers–Heisenberg deviation from the
  Lorentzian was judged in 2014 to be absorbed by the free continuum
  [src: arXiv:1308.3240, Sect. III.2, footnote 6]; the KHT profile now in
  VPFIT matters at very high column densities, where "significant
  systematics" follow if it is not modelled (Lee et al. 2020,
  arXiv:1910.02913) [src: abstract].
- **Validation of a sample.** No D/H trend with [O/H], N(H I) or redshift;
  χ² consistency of the sample within 2σ [src: arXiv:1710.11129,
  Sect. IV.3; arXiv:2401.12797, Sect. 4.1; arXiv:2402.05586, Sect. 6.1].

## Reading list
<!-- key: reading-list -->

- Foundation/method: Cooke et al. 2014, arXiv:1308.3240 — selection
  criteria, blind analysis, marginalising continuum, zero level and
  instrumental profile.
- Application: Cooke, Pettini & Steidel 2018, arXiv:1710.11129 — the
  reference single-system analysis, restarts, post-unblinding tests,
  intrinsic-scatter likelihood.
- Application: Kislitsyn et al. 2024, arXiv:2401.12797 — MCMC with fitted
  continuum and resolution, model-variant mixture, hidden-H I bias, two
  literature means.
- Application: Guarneri et al. 2024, arXiv:2402.05586 — ESPRESSO Lyman-limit
  system, continuum and window tests, three-spectrograph fits.
- Critique: Zavarygin et al. 2018, arXiv:1706.09512 — AICc model choice and
  least-trimmed-squares combination.
- Method: Lee, Webb & Carswell 2020, arXiv:1910.02913 — KHT line profile.
- Review: Cooke 2024, arXiv:2409.06015 — context and the precision sample.

## Not verified
<!-- key: not-verified -->

- No new quasar D/H determination posted after arXiv:2402.05586 was found
  in a title search restricted to 2024-03 onwards (astro-ph.CO, GA).
- The size of the KHT-profile bias on D/H for a specific system: not stated
  in the text of arXiv:1910.02913 read here.
- Riemer-Sørensen et al. 2015 and 2017, Balashev et al. 2016, Pettini &
  Cooke 2012 and Cooke et al. 2016: cited through the compilations above,
  bodies not read; no identifier recorded.
