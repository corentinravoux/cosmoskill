# Galaxy–halo connection — systematics

Scope: what biases an inferred galaxy–halo connection, or a cosmological result
drawn from small-scale clustering and lensing through it; mechanism, size where
a paper quantifies it, mitigation, validation test and the paper a referee
expects.
Snapshot: 2026-10-16

Flags: `[src]` abstract read this session; `[src: Sect. n]`, `[src: Table n]`
body read; `[sec]` named secondary source; `[der]` derived here.

Cluster mass calibration (weak-lensing mass bias, hydrostatic bias, projection
effects of richness) is in `cosmo-clusters`; shear calibration,
photometric-redshift calibration of sources and intrinsic alignments are in
`cosmo-weak-lensing` and `cosmo-photometry-photoz`. This file keeps what is
specific to the galaxy–halo connection.

## 1. Halo definition and finder
<!-- key: halo-definition-and-finder -->

- Mechanism. Mass and radius depend on Δ, on the reference density and on the
  finder; SO masses correlate with each other much better than with FoF masses
  (arXiv:astro-ph/0011495) [src]; FoF (b = 0.2) halo bias is ~10% below that of
  Δ = 200 haloes (arXiv:1001.3162) [src]; SO masses pseudo-evolve
  (arXiv:1207.0816) [src].
- Size. In the Euclid mass-function calibration the halo finder is the one
  calibration term that "could lead to biased cosmological inference"; the
  other terms are largely subdominant (arXiv:2208.02174) [src]. Most finders
  lose subhaloes below 30–40 particles (arXiv:1104.0949) [src].
- Mitigation. State Δ, reference density and finder with every occupation
  parameter; refit an HOD rather than transfer it between simulations with
  different finders.
- Test. Re-run the occupation fit on a second finder or mass definition.

## 2. Halo mass function and bias calibration
<!-- key: halo-mass-function-and-bias-calibration -->

- Mechanism. Fitting functions are not universal at the per-cent level
  (arXiv:0803.2706) [src]; baryons lower halo masses (arXiv:1502.07357) [src];
  the peak-background split leaves ~20% residuals in bias (arXiv:1001.3162)
  [src].
- Size. Tinker 2008 calibration ≲ 5% for 10¹¹–10¹⁵ M_⊙/h; Tinker 2010 bias
  scatter ~6% [src]; emulators reach ~1% (arXiv:1804.05866) [src]. A
  Planck-like cluster sample moves by Δσ8 ≃ 0.02 between the Magneticum and
  Tinker 2008 functions (arXiv:1502.07357) [src].
- Mitigation. Emulators of halo statistics over cosmology (Aemulus, Dark
  Emulator) or direct forward modelling on simulations (section 8 of
  `physics-and-methods.md`), with an emulator-error term in the covariance.

## 3. Profiles, concentration and their scatter
<!-- key: profiles-concentration-and-their-scatter -->

- Mechanism. NFW is a fit, not a law: profiles deviate beyond 0.5 R200m and
  steepen sharply near R200m (arXiv:1401.1216) [src]; concentration–mass
  relations differ by tens of per cent between calibrations (e.g. Duffy et al.
  2008 sits 16–23% below Millennium-based values, arXiv:0804.2486) [src];
  scatter σ_ln c ~ 0.3 is usually ignored [src: Sect. 5.8 of arXiv:2303.08752];
  baryons modify c(M) (arXiv:2610.03544) [src].
- Mitigation. A free concentration amplitude, or forward modelling on
  simulations; satellite profiles allowed to differ from the dark matter.

## 4. Stellar-mass and luminosity estimates
<!-- key: stellar-mass-and-luminosity-estimates -->

- Mechanism. Stellar-mass systematics (initial mass function, population
  synthesis, dust, photometry of extended light) move the whole SHMR.
- Size. For z < 1 stellar-mass estimates are the largest uncertainty of the
  SHMR (arXiv:1001.0015) [src]. Abundance-matching relations underestimate BCG
  stellar masses by a factor ~2–4 when the stellar mass function is built from
  photometry that misses the outer profiles of massive galaxies (Kravtsov et
  al. 2018, arXiv:1401.7329) [src]. Typical stellar-mass uncertainties are
  0.2–0.3 dex, and measured scatter includes them in quadrature [src: Sect. 6.2
  of arXiv:1804.03097].
- Mitigation. Quote the IMF and the photometry; propagate a measurement-scatter
  term separately from the intrinsic scatter.

## 5. Scatter–slope degeneracy
<!-- key: scatter-slope-degeneracy -->

- Mechanism. At high mass, the scatter of stellar mass at fixed halo mass and
  the slope of the SHMR are degenerate when only abundances are fitted;
  neglecting scatter alone biases the relation for centrals of massive haloes
  by as much as stellar-mass errors (arXiv:1001.0015) [src].
- Mitigation. Add clustering, lensing, groups or satellite kinematics; the iHOD
  breaks the degeneracy "without the need to assume a strong prior on the
  scatter" by modelling ~80% more galaxies (arXiv:1505.02781) [src].

- How scatter is constrained [src: Sect. 6.2 of arXiv:1804.03097]: the stellar
  mass function alone cannot constrain σ_log M*; clustering constrains it where
  halo bias varies strongly with mass (log M_h = 12.7–13.7 for BOSS); group
  catalogues through the scatter of central mass at fixed group mass, after
  running the mocks through the same group finder; satellite kinematics at
  lower halo masses; dynamical scaling relations at the low-mass end. Most
  measured values are the quadratic sum of intrinsic and measurement scatter,
  with stellar-mass uncertainties of 0.2–0.3 dex.

## 6. Occupation statistics and the central condition
<!-- key: occupation-statistics-and-the-central-condition -->

- Mechanism. Bernoulli centrals, Poisson satellites and the central condition
  are mutually incompatible; imposing the condition changes the satellite mean
  and creates a central–satellite covariance [src: Sect. 4.1 of
  arXiv:2303.08752]. Mass-dependent non-Poisson satellite statistics can bias
  cosmology if ignored (same section) [src].
- Size. KiDS-1000 strongly prefers sub-Poisson satellite variance, improving
  the reduced χ² by 0.18 (arXiv:2210.03110) [src]; allowing non-Poisson
  satellites lowers the SDSS CLF σ8 from 0.763 to 0.744 (arXiv:1207.0503)
  [src].
- Mitigation. A free satellite-variance parameter; state whether the central
  condition is imposed.

## 7. Assembly bias and secondary dependencies
<!-- key: assembly-bias-and-secondary-dependencies -->

- Mechanism. A mass-only occupation model mispredicts clustering and the
  lensing inferred from it when occupation depends on concentration, formation
  time or environment (section 9 of `physics-and-methods.md`).
- Size. Statistically significant errors in the inferred HOD for reasonable
  assembly bias (arXiv:1311.1818) [src]; up to a factor two at r ~ 200 kpc and
  ~15% in the linear regime (arXiv:1512.03050) [src]; 10–15% clustering excess
  for DESI-like LRGs in TNG (arXiv:2202.12911) [src]; assembly bias ~20%
  (Planck) or ~10% (low S8) in SHAMe fits of BOSS (arXiv:2305.09637) [src]. In
  HSC-Y1 × SDSS, galaxy–halo uncertainties bias S8 by < ~50% of its statistical
  error "unless the assembly bias effect is unexpectedly large"
  (arXiv:2111.02419) [src].
- Mitigation. Decorated or environment-dependent HODs fitted with the cosmology
  (arXiv:2512.15962) [src: Sect. III.2]; a theoretical-error term that spans
  zero (arXiv:2202.07440) [src: Sect. 4.2]; methods stated to be insensitive to
  assembly bias (satellite kinematics, arXiv:2409.03105) [src].
- Subtlety. Galaxy assembly bias contributes to two-halo clustering only
  through halo assembly bias; a simulation-based model includes the latter
  automatically and needs to model only the former [src: Sect. 4.2 of
  arXiv:2202.07440]. The secondary property matters: concentration alone does
  not capture the effect (arXiv:2010.04182) [src], and the strength and sign
  depend on the halo definition (arXiv:1705.04327) [src].

## 8. Satellite distribution, velocity bias and orphans
<!-- key: satellite-distribution-velocity-bias-and-orphans -->

- Mechanism. Satellites placed on an NFW profile of the host neglect subhaloes
  and segregation; velocities drawn from the dark matter neglect velocity bias;
  disrupted subhaloes remove satellites.
- Size. BOSS CMASS velocity bias: centrals 0.22, satellites 0.86 of the
  dark-matter dispersion (arXiv:1407.4811) [src]. "Roughly 80 per cent of all
  subhalo disruption is numerical rather than physical" (van den Bosch 2017,
  quoted by the review), and orphans are 10–30% of galaxies in some SAMs [sec:
  arXiv:1804.03097, Sect. 6.5.2]. Subhalo finders agree except below ~50
  particles and at host-centre passages, and merger-tree codes give "distinct
  results" on the same simulation [sec: arXiv:1804.03097, Sect. 6.5.2]. Smooth
  satellite profiles under-predict small-scale lensing (arXiv:2512.15962) [src:
  Sect. III.2]; satellite segregation is one of the three galaxy-formation
  effects behind the lensing-is-low excess in TNG300 (arXiv:2211.01744) [src].
- Mitigation. Free satellite concentration and velocity-bias parameters;
  restrict comparisons to resolution-converged regimes (as done by Reddick et
  al. 2013 and Lehmann et al. 2017 [sec: arXiv:1804.03097, Sect. 6.5.2]); scale
  cuts.

## 9. Lensing and clustering systematics in joint fits
<!-- key: lensing-and-clustering-systematics-in-joint-fits -->

- Source photometric redshifts. For z_L = 0.55, a 30% change in ΔΣ needs a
  photo-z bias Δz = 0.16 at z_S = 1; the measured impact of photo-z errors on
  the CMASS ΔΣ is at the 3% level [src: Sect. 5.1 of arXiv:1611.08606].
- Boost factor and intrinsic alignments. Boost factors are below 15% at the
  smallest scales and negligible at larger scales, so at most 15% of
  small-scale sources are associated with the lens; the intrinsic-alignment
  impact is argued to be negligible [src: Sect. 4.3 of arXiv:2202.07440].
  Leauthaud et al. do not apply a boost and instead show invariance to
  lens–source separation cuts [src: Sect. 5.1 of arXiv:1611.08606].
- Shear calibration. Three independent shear catalogues with different
  calibrations gave the same ΔΣ; the total fractional systematic on ΔΣ is
  estimated below 5–10% [src: Sect. 5.1 of arXiv:1611.08606]. Survey-level
  shear and n(z) calibration is in `cosmo-weak-lensing` and
  `cosmo-photometry-photoz`.
- Baryonic effects on ΔΣ. TNG300 suppresses lensing by up to 10% at 1 h⁻¹Mpc,
  Illustris by 15% at 3 h⁻¹Mpc; a kSZ-based estimate gives 20% below 1 h⁻¹Mpc
  and accounts for half of the Leauthaud et al. discrepancy [src: Sect. 4.1 of
  arXiv:2202.07440]. Baryons are usually handled by a concentration
  normalisation (f_conc ~ 0.8 preferred by GAMA groups, same section) or by
  scale cuts.
- Lens selection and its redshift evolution. The CMASS mean stellar mass rises
  by a factor of 1.8 over 0.43 < z < 0.7, so SHAM predicts a 3.5-fold rise in
  mean halo mass, while the lensing and clustering are constant: colour
  incompleteness and luminosity estimates of extended light are suspects [src:
  Sect. 5.3 of arXiv:1611.08606]. A halo-mass-dependent selection of satellites
  removes the small-scale discrepancy (arXiv:2010.01143) [src].
- Cosmology dependence of distances. Dynamical dark energy of the DESI kind
  lowers GGL relative to clustering by up to 7% through the lensing kernel
  (arXiv:2508.05746) [src].

## 10. Residual redshift-space distortions, exclusion and scale cuts
<!-- key: residual-redshift-space-distortions-exclusion -->

- Residual RSD in w_p with a finite π_max cause errors > 20% at r_p ≳ 10 h⁻¹Mpc
  if ignored; scale-dependent halo bias and exclusion errors exceed 40% at ~1
  h⁻¹Mpc if ignored (arXiv:1206.6890) [src].
- The transition region between one- and two-halo terms is under-predicted by
  linear halo bias, by up to a factor ~2 in the two-halo term at k ~ 0.7 h/Mpc
  (arXiv:2011.08858) [src].
- Scale cuts are the main control of baryons and assembly bias; their values
  differ by a factor of several between analyses (0.4 vs 2 h⁻¹Mpc for
  clustering, 2.5 vs 3 vs 5.25 h⁻¹Mpc for lensing in arXiv:2512.15962,
  arXiv:2111.02419, arXiv:2202.07440) [src: Sect. III.2, IV.3, abstract].
- Simulation resolution: in DESI DR1, AbacusSummit resolution was insufficient
  for the faintest BGS sample [src: Sect. III.5 of arXiv:2512.15962]; halo
  finders lose substructure below 30–40 particles (arXiv:1104.0949) [src].

## What a referee checks in a results section
<!-- key: what-a-referee-checks-in-a-results-section -->

1. Halo mass definition, finder and simulation (resolution) behind every
   occupation parameter.
2. Cosmology held fixed during HOD or SHMR fits, and whether conclusions
   survive a second cosmology.
3. Occupation form: central shape (incompleteness, decay at high mass for
   ELGs), satellite statistics, central condition.
4. Assembly bias: modelled (which secondary property), bracketed by a
   theoretical error, or argued irrelevant.
5. Satellite profile and velocity bias free or fixed.
6. Stellar-mass systematics: IMF, photometry of extended light, measurement
   scatter separated from intrinsic scatter.
7. Lens sample selection and completeness in stellar mass and colour, and their
   redshift evolution.
8. For lensing: source n(z), shear calibration, boost or lens–source cuts,
   baryon treatment, scale cuts justified on mocks.
9. Residual RSD and π_max in w_p; exclusion and non-linear halo bias in
   analytic models.
10. Covariance from mocks or jackknife, with the Hartlap-type correction;
    blinding stated.

## Not verified
<!-- key: not-verified -->

- van den Bosch 2017 on numerical subhalo disruption and Pujol et al. 2017 on
  orphan fractions are quoted through the Wechsler & Tinker review, not read.
- No systematics budget table of the DES Y3 or DESI DR1 SHMR analyses was read.
