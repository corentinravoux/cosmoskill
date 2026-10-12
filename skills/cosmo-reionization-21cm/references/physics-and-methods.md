# Physics and methods — reionisation, 21 cm, line-intensity mapping

Scope: observables, estimators, models and codes for reionisation, 21 cm and line mapping.
Snapshot: 2026-10-07

Numbers carry [src] (read in the cited paper this session), [sec] (taken from the named
secondary source) or [der] (derived here, derivation stated).

## 1. Reionisation observables

### 1.1 Thomson optical depth

- Definition (textbook): τ is the line-of-sight integral of n_e σ_T from today to recombination.
  Free electrons after reionisation rescatter the CMB quadrupole and create the low-ℓ EE
  "reionisation bump"; they also damp the primary anisotropies by e^(−2τ), so high-ℓ data
  constrain the product A_s e^(−2τ) and not τ.
- Consequence used in every 2025–2026 debate: without low-ℓ polarisation, τ is fixed only
  through CMB lensing and BAO, and it is negatively correlated with the matter fraction [src:
  Sailer et al. 2025, arXiv:2504.16932].
- Parametrisations in use. (i) The "instantaneous" tanh transition, the default of Planck
  analyses [src: Planck Collaboration 2016, arXiv:1605.03507]. (ii) Symmetric and asymmetric
  transitions fitted with kSZ information [src: arXiv:1605.03507]. (iii) A Gompertz form
  calibrated on simulations, asymmetric by construction [src: Montero-Camacho & Mao 2026,
  arXiv:2607.26373]. (iv) tanh plus a transient high-redshift "flash" [src: Upadhyay et al.
  2026, arXiv:2609.24989].
- τ maps to a midpoint only inside a parametrisation: τ = 0.059 ± 0.006 gives z_re = 8.14 ± 0.61
  for tanh [src: Pagano et al. 2019, arXiv:1908.09856]; the Planck 2016 models give mean
  redshifts between 7.8 and 8.8 and an ionised fraction below 10% above z ~ 10 [src:
  arXiv:1605.03507].
- Likelihoods for the low-ℓ EE data are not Gaussian and are built from simulations: the
  simulation-based likelihood (SimBaL) of the Planck legacy papers, the maximum-entropy
  "momento" likelihood and a density-estimation scheme give consistent τ on SRoll2 maps [src: de
  Belsunce et al. 2021, arXiv:2103.14378]. Details belong to `cosmo-cmb`.

### 1.2 Lyman-series absorption in quasar spectra

- Logic of the dark-pixel fraction: "Any spectral region showing transmission must be highly
  ionized, while dark regions could be ionized or neutral", so the dark fraction is a nearly
  model-independent upper limit on the neutral volume fraction, "modulo choices in binning scale
  and dark pixel definition" [src: Davies et al. 2025, arXiv:2510.25829]. The 2025 analysis bins
  at 3.3 comoving Mpc and uses the negative-pixel method on Lyα, Lyβ and Lyγ [src:
  arXiv:2510.25829].
- Lyβ has a lower optical depth than Lyα and is therefore more sensitive to residual neutral gas
  [src: Zhu et al. 2022, arXiv:2205.04569].
- Dark gaps: contiguous regions where the transmission averaged over 1 h⁻¹Mpc bins falls below
  5%; the statistic F₃₀ is the fraction of sightlines with a gap longer than 30 h⁻¹Mpc [src: Zhu
  et al. 2021, arXiv:2109.06295].
- Effective optical depth τ_eff = −ln⟨F⟩ over a fixed path. Its sightline-to-sightline scatter
  at z > 5.3 is "too strong to be caused by fluctuations in the density field alone" [src:
  Davies et al. 2023, arXiv:2312.08464]. Two model families fit it: residual neutral islands
  from a late end of reionisation, and a fluctuating ionising background with a short, spatially
  varying mean free path [src: arXiv:2312.08464; Zhu et al. 2021, arXiv:2109.06295].
- Inference is by forward modelling. Gaikwad et al. post-process the Sherwood simulations with
  the EX-CITE code to generate photo-ionisation-rate fluctuation models and fit the τ_eff
  distribution for the mean free path, the photo-ionisation rate and the neutral fraction [src:
  Gaikwad et al. 2023, arXiv:2304.02038]. Davies et al. use approximate Bayesian computation on
  the same statistic [src: arXiv:2312.08464].
- Mean free path of ionising photons, direct method: stack quasar spectra below the Lyman limit
  and fit the transmission profile, correcting for the quasar proximity zone [src: Zhu et al.
  2023, arXiv:2308.04614]. Units are proper Mpc.

### 1.3 Damping wings

- A neutral IGM in front of a source imprints Lyα damping-wing absorption redward of the line
  centre. In stacked forest spectra the wing extends more than 1000 km/s beyond a Gunn–Peterson
  trough when x_HI ≳ 0.1 [src: Spina et al. 2024, arXiv:2405.12273].
- Quasars. The three difficulties are the stochastic patchy topology, the degeneracy with the
  quasar lifetime, and the unknown intrinsic spectrum near Lyα [src: Davies et al. 2018,
  arXiv:1802.06066]. Current pipelines predict the intrinsic continuum from the red side: a
  covariance-based reconstruction of Lyα and N V from C IV, Si IV and C III] [src: Greig et al.
  2024, arXiv:2404.12585], or a PCA model trained on 15,559 SDSS/BOSS quasars, for which six
  parameters perform best and machine-learning alternatives give no gain [src: Hennawi et al.
  2024, arXiv:2406.12070].
- Galaxies. JWST/NIRSpec prism spectra of UV-bright galaxies show a softening of the break at
  rest 1216 Å with redshift, fitted with an ionised bubble of radius R_b in an IGM of neutral
  fraction x_HI [src: Umeda et al. 2023, arXiv:2306.00487]. Local damped absorption in the
  galaxy or its circumgalactic gas is degenerate with the IGM wing at prism resolution (section
  3 of `systematics.md`).

### 1.4 Lyα emission from galaxies

- Observable: the fraction X_Lyα of UV-selected galaxies with Lyα equivalent width above a
  threshold (25 Å or 10 Å in arXiv:2609.40363), or the Lyα luminosity function. Both fall when
  the surrounding IGM is neutral.
- The inference needs the intrinsic (post-reionisation) equivalent-width distribution as a
  baseline, taken at z ~ 5–6 [src: Prieto-Lyon et al. 2025, arXiv:2509.18302], and a
  reionisation simulation for the transmission, for example THESAN [src: Kundu et al. 2026,
  arXiv:2609.40363].

### 1.5 Kinetic SZ

- The small-scale CMB temperature spectrum contains kSZ power from the late-time ionised
  Universe ("homogeneous") and from ionised bubbles during reionisation ("patchy"). Only the
  sum, D_3000^kSZ, is measured; the patchy part, and hence the duration, follows after
  subtracting an assumed late-time template [src: Chaubal et al. 2026, arXiv:2601.20551;
  Beringue et al. 2025, arXiv:2506.06274].
- Duration is defined differently in each paper: Δ⁵⁰z from x_e = 25% to 75% and Δ⁹⁰z from 5% to
  95% in SPT-3G D1 [src: arXiv:2601.20551].
- The kSZ trispectrum (a quadratic estimator on two temperature maps that reconstructs the
  large-scale velocity modulation of the small-scale kSZ) is contaminated by CMB lensing and
  foregrounds, which must be simulated and subtracted [src: Raghunathan et al. 2024,
  arXiv:2403.02337].

### 1.6 Ionising-photon budget

- Bookkeeping (textbook): the ionising emissivity is the UV luminosity density times the
  ionising efficiency ξ_ion times the escape fraction f_esc, balanced against recombinations set
  by a clumping factor.
- JWST values of ξ_ion with low-redshift f_esc calibrations overproduce photons [src: Muñoz et
  al. 2024, arXiv:2404.07250]; later mass-complete samples lower ξ_ion [src: Simmonds et al.
  2024, arXiv:2409.01286]; spectral fitting of f_esc object by object gives an end at z ~ 5.8
  [src: Giovinazzo et al. 2026, arXiv:2607.22834].

## 2. The 21 cm signal

Equations in this section are quoted from the review of Liu & Shaw 2019, arXiv:1907.08211,
section 2.1 [sec for the numbers].

- Spin temperature: n₁/n₀ = 3 exp(−h ν₂₁ / k_B T_s), with ν₂₁ ≈ 1420.406 MHz.
- Brightness temperature against the CMB: T_b = [1 − exp(−τ_HI)] (T_s − T_γ)/(1 + z), with 1 + z
  = ν₂₁/ν.
- Optical depth: τ_HI = (3 ħ c³ A₁₀ / 16 k_B ν₂₁²) x_HI n_H / [(1 + z)(dv_∥/dr_∥) T_s], with A₁₀
  = 2.85 × 10⁻¹⁵ s⁻¹. It is ≲ 4% everywhere of interest, so T_b ∝ x_HI n_H (1 − T_γ/T_s) / [(1 +
  z)² (dv_∥/dr_∥)].
- For T_s ≫ T_γ the signal no longer depends on T_s. This is the regime of post-reionisation
  intensity mapping and of late reionisation with a heated IGM.
- Two observables: the global (sky-averaged) spectrum T̄_b(ν), and the fluctuations, summarised
  by the dimensionless power spectrum Δ²₂₁(k) = k³ P(k)/2π² in mK².
- Frequency coverage: 47–234 MHz corresponds to z = 5.1–29.3 [src: HERA Collaboration 2025,
  arXiv:2511.21289].
- Sequence of epochs. Lyα photons from the first stars couple T_s to the cold gas and produce
  absorption; X-ray heating then raises the gas above the CMB temperature; reionisation removes
  the signal. EDGES read its profile edges as the onset of Lyα coupling by 180 Myr and heating
  less than 100 Myr later [src: Bowman et al. 2018, arXiv:1810.05912].
- The EDGES depth requires one of three things: gas colder than adiabatic cooling allows (for
  example dark-matter–baryon scattering), a radio background in excess of the CMB at high
  redshift, or an unmodelled systematic [src: arXiv:2511.21289, introduction; arXiv:1810.05912].
- Limits are interpreted through a galaxy-formation model. Parameters that current limits touch:
  the X-ray luminosity per star-formation rate (heating), the radio efficiency of early
  galaxies, and the minimum halo mass [src: HERA Collaboration 2022, arXiv:2210.04912; Dhandha
  et al. 2025, arXiv:2508.13761; Sims et al. 2025, arXiv:2504.09725].
- A perturbative, symmetries-based bias expansion of the 21 cm field exists for large scales and
  is the basis of **forecasts** of τ from 21 cm data [src: Sailer, Chen & White 2022,
  arXiv:2205.11504].

## 3. Post-reionisation HI intensity mapping

- After reionisation the residual neutral hydrogen (x_HI ~ 2%) sits in self-shielded gas inside
  haloes of ~10¹⁰–10¹³ M_⊙ and is seen in emission [sec: arXiv:1907.08211, section 2.4].
- Abundance targets quoted by the same review: Ω_HI ~ (3.9 ± 0.6) × 10⁻⁴ at z < 0.06 from
  ALFALFA, and Ω_HI = 9.8 (+2.0/−1.8) × 10⁻⁴ at z = 4.9 from damped Lyα systems [sec:
  arXiv:1907.08211, section 2.4].
- Intensity mapping does not resolve galaxies: each voxel integrates the emission of many
  sources, and the angular resolution is matched to the cosmological scale of interest [sec:
  arXiv:1907.08211]. The MeerKAT beam at L-band corresponds to ~30 Mpc comoving [sec: Cunnington
  et al. 2026, arXiv:2606.25955, section 3].
- What an amplitude measures. The mean brightness temperature scales with Ω_HI, so a cross-power
  with galaxies constrains Ω_HI b_HI r [src: Masui et al. 2012, arXiv:1208.0331], and an
  auto-power constrains Ω_HI b_HI [src: MeerKLASS Collaboration 2026, arXiv:2610.12158]. CHIME
  quotes A_HI ≡ 10³ Ω_HI (b_HI + ⟨fμ²⟩) with ⟨fμ²⟩ = 0.552 for stacking [src: CHIME
  Collaboration 2022, arXiv:2202.01242] and A²_HI ≡ 10⁶ Ω²_HI (b²_HI + ⟨fμ²⟩)² for the
  auto-spectrum [src: CHIME Collaboration 2026, arXiv:2603.25680]. These are different
  combinations; they are not interchangeable.
- Two observing modes. Single-dish (each dish's auto-correlation, scanned over a wide area)
  reaches the largest scales: MeerKLASS, and the planned SKA-Mid survey [src: arXiv:2606.25955].
  Interferometers with compact redundant arrays (CHIME, Tianlai, HIRAX, CHORD) measure smaller
  transverse scales and lose low k_∥ to the foreground filter [src: arXiv:2202.01242; The CHORD
  Collaboration 2026, arXiv:2607.09374].
- BAO analysis planned for SKA: a template fit of the HI power-spectrum multipoles in α_iso and
  α_AP with a Gaussian beam term and broadband splines, as in DESI; no density-field
  reconstruction is assumed because it "has not been tested in the presence of foregrounds"
  [src: Wolz et al. 2026, arXiv:2607.03259, section 4.1].
- The sibling `cosmo-galaxy-clustering` covers BAO template and full-shape practice for
  galaxies, from which this template is adapted.

## 4. Line-intensity mapping in other lines

- Review of record: Bernal & Kovetz 2022, arXiv:2206.15377 (target lines, modelling, statistics,
  synergies).
- Model of the power spectrum (textbook form used by COMAP): a clustering term proportional to
  ⟨Tb⟩² P_m(k), with ⟨Tb⟩ the mean line temperature times bias, plus a scale-independent
  shot-noise term. COMAP quotes its constraint as ⟨Tb⟩² [src: Cleary et al. 2021,
  arXiv:2111.05927].
- Shot noise depends on the scatter of line luminosity at fixed halo mass. JWST-era burstiness
  raises it by a line-dependent factor (B_Hα ≃ 7; 2.5–3.5 for [CII], CO, UV at z ~ 6) [src:
  Kovetz et al. 2026, arXiv:2605.13967].
- Interlopers: one observed frequency contains several lines from different redshifts. For [CII]
  at reionisation redshifts the interlopers are lower-redshift CO lines, and the first CCAT
  measurement is expected to be of the combined [CII] + CO power (**forecast**) [src: Dev et al.
  2026, arXiv:2607.20404]. Interlopers are masked, modelled, or removed by cross-correlation.
- Estimators beyond the auto-power: stacking on an external catalogue, the conditional voxel
  intensity distribution, and the cross-power; simulations for a [CII] pathfinder give
  comparable significance for the three and the best constraints from their combination [src:
  Kramer et al. 2026, arXiv:2603.13218].
- Tomographic clustering redshifts applied to broadband diffuse maps give the mean line
  background without a spectrometer [src: Chiang 2026, arXiv:2602.02658].

## 5. Estimators, covariance and likelihood practice

### 5.1 The foreground wedge

- Foregrounds are spectrally smooth and should occupy the lowest k_∥ modes. An interferometer
  baseline of fixed length probes a k_⊥ that scales with frequency, so the Fourier transform
  along frequency mixes foreground power to higher k_∥ ("mode mixing") [sec: arXiv:1907.08211,
  section 12.1.5].
- For flat-spectrum unclustered sources the leaked power follows the squared primary beam
  evaluated at (k_∥/k_⊥)(c/H₀)(1 + z)/E(z); lines of constant contamination are k_∥ ∝ k_⊥ [sec:
  arXiv:1907.08211, eq. for P̂(k) in section 12.1.5].
- Wedge boundary [der: set the beam argument equal to D_c θ₀, with θ₀ the angle at which the
  beam reaches zero]: k_∥ = k_⊥ H₀ D_c E(z) θ₀ / [c (1 + z)]. With θ₀ at the horizon this is the
  "horizon line"; the region above it is the "EoR window".
- Foreground avoidance restricts the analysis to the window; foreground subtraction or
  statistical separation tries to recover modes inside the wedge, as the LOFAR Gaussian-process
  approach does [sec: arXiv:1907.08211, section 12.1.5; src: Mertens et al. 2017,
  arXiv:1711.10834].

### 5.2 Foreground removal

| Method | Used by | Property to check | Citation |
|---|---|---|---|
| Delay filtering and avoidance | HERA, CHIME | which k_∥ are lost; leakage from mutual coupling and reflections | arXiv:2210.04912, arXiv:2309.04404 |
| Gaussian process regression | LOFAR | recovers k = 0.07–0.3 h/cMpc in simulations and gains a factor ≳ 3 over avoidance; needs foreground coherence ≳ 3 MHz [src] | Mertens et al. 2017, arXiv:1711.10834 |
| Machine-learned GPR covariance | LOFAR 2025 | signal suppression; a bias correction was needed on the 3C196 field [src] | arXiv:2503.05576, Ceccotti et al. 2025, arXiv:2504.18534 |
| Blind source separation (PCA, FastICA) + transfer function | GBT, MeerKLASS | signal loss on all scales, corrected by mock injection [src] | Wolz et al. 2021, arXiv:2102.04946; Cunnington et al. 2023, arXiv:2302.07034 |
| Wavelet-domain PCA | Tianlai | first use with spherical Fourier–Bessel power spectrum [src] | Deng et al. 2026, arXiv:2604.27465 |
| Polynomial or physical foreground + signal model | global-signal experiments | uniqueness of the fit; number of terms [src] | Hills et al. 2018, arXiv:1805.01421 |

### 5.3 Reporting conventions

- Upper limits on Δ² are 2σ and are quoted with the k and z of the most constraining bin. Papers
  add whether the remaining bins are consistent with thermal noise.
- Cross-spectra between independent data splits remove the noise bias: nights or baselines in
  interferometers, "feed groups" in COMAP [src: Stutzer et al. 2024, arXiv:2406.07511], scan-
  and dish-wise subsets in MeerKLASS [src: arXiv:2610.12158].
- Validation practice read in the papers: end-to-end pipeline simulations and statistical tests
  (HERA, arXiv:2210.04912), signal injection (LOFAR, arXiv:2503.05576), 312 difference-map null
  tests (COMAP, arXiv:2406.07511), null and robustness tests on subset cross-spectra (MeerKLASS,
  arXiv:2610.12158).
- Global-signal claims are assessed by Bayesian evidence between data models with and without a
  signal and with and without systematic terms [src: Sims & Pober 2019, arXiv:1910.03165], and
  more recently by null-test evidence ratios [src: Sims et al. 2025, arXiv:2506.20042].
- Blinding. None of the abstracts read for this skill reports a blinded analysis. In MeerKLASS
  papers "blind" refers to blind component separation, which is a foreground-removal technique
  and not analysis blinding [src: arXiv:2610.12158; arXiv:2302.07034].
- Neutral-fraction inferences are Bayesian comparisons with reionisation simulations; the quoted
  intervals are posterior medians with 68% intervals and are bounded by 0 and 1, so error bars
  are strongly asymmetric near the bounds.

## 6. Codes and simulations

| Code or suite | Role | Reference | Flag |
|---|---|---|---|
| 21cmFAST | semi-numerical 3D realisations of density, ionisation, velocity and spin temperature; agrees with a hydrodynamic simulation to tens of percent in the power spectrum on scales ≳ 1 Mpc | Mesinger, Furlanetto & Cen 2010, arXiv:1003.3878 | [src] |
| 21cmEMUv3 | emulator of 21cmFASTv3 summaries (cylindrical and spherical power spectra, global signal, x_HI, T_s, UV luminosity functions, τ) over σ₈ and ten astrophysical parameters; sub-percent median accuracy; public | Breitman et al. 2026, arXiv:2606.00219 | [src] |
| GRIZZLY | 21 cm power-spectrum model used for the LOFAR interpretation | Ghara et al. 2025, arXiv:2505.00373 | [src] |
| EDGES analysis package | open-source end-to-end calibration, analysis and simulation package for global-signal experiments; raw EDGES data released with it | Murray et al. 2026, arXiv:2605.16643 | [src] |
| EX-CITE on Sherwood | post-processing for ionising-background fluctuations in Lyα forest modelling | arXiv:2304.02038 | [src] |
| THESAN, CoDa-III, Aton | radiation-hydrodynamic or radiative-transfer reionisation simulations used as comparison in Lyα and Lyα-emitter work | named in arXiv:2304.02038 and arXiv:2609.40363 | [sec] |
| Lumina | 500 cMpc radiation-hydrodynamic box (AREPO, IllustrisTNG model, GPU M1 transport), through HI and He II reionisation to z = 3 | Zier et al. 2026, arXiv:2605.15310 | [src] |
| AMBER, Agora | reionisation and microwave-sky simulations behind the SPT kSZ duration limits and the trispectrum foreground estimate | named in arXiv:2601.20551 and arXiv:2403.02337 | [sec] |
| UniverseMachine on Uchuu; Shark | empirical and semi-analytic galaxy models compared with JWST luminosity functions | Prada et al. 2026, arXiv:2604.18683; Lagos et al. 2026, arXiv:2609.03537 | [src] |

The sibling `cosmo-simulations-mocks` covers the simulation suites themselves;
`cosmo-software-ecosystem` covers general inference tooling.

## 7. Conventions and traps specific to the domain

- Δ² is quoted either in mK² (HERA: 457 mK²) or as a squared temperature (LOFAR: (68.7 mK)²).
  Square or take the root before comparing.
- Wavenumbers are in h Mpc⁻¹ for 21 cm experiments and in Mpc⁻¹ for COMAP and for CHIME's k_∥
  cut.
- Neutral fractions are volume-weighted in most quasar work and mass-weighted in some galaxy
  work (for example arXiv:2609.40363); the two differ during patchy reionisation.
- Mean free paths are in proper Mpc; dark-gap lengths and bin sizes in comoving h⁻¹Mpc.
- "Duration of reionisation" has at least three definitions (section 1.5).
- "Detection" in intensity mapping can mean a cross-correlation, a stack, or an auto-spectrum;
  these constrain different parameter combinations.

## Not verified

- The numerical prefactor of the 21 cm brightness temperature (the often-quoted tens of mK) was
  not read at source; only the symbolic form above was.
- The saturation threshold of the Gunn–Peterson trough in x_HI and the original Gunn & Peterson
  1965 reference were not fetched.
- The foundational wedge papers (Datta et al. 2010, Morales et al. 2012, Parsons et al. 2012)
  are named in arXiv:1907.08211 but were not fetched; no identifiers are given here.
- The physics reviews of Furlanetto, Oh & Briggs 2006 and Pritchard & Loeb 2012 were not
  fetched.
