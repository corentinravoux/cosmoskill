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
  other terms are largely subdominant (arXiv:2208.02174) [src]. Counting only
  bound particles inside the SO radius lowers the cumulative HMF by ~5% [src:
  Sect. 4.3.3]; FoF-based finders merge small objects through particle
  bridges [src: Sect. 4.3.1]; a VELOCIraptor or SUBFIND calibration analysed
  with the ROCKSTAR one biases (Ω_m, σ8) of Euclid cluster counts by ≲ 1σ in
  that plane with 3–5% mass–observable priors, ≲ 2σ with 1%; AHF stays ≲ 1σ
  [src: Sect. 5.4.1, Table 5]. Most finders lose subhaloes below 30–40
  particles (arXiv:1104.0949) [src].
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
  term separately from the intrinsic scatter. DES Y3 marginalises the lens
  stellar-mass distribution alongside shear and redshift nuisances [src:
  Sect. 3.5 of arXiv:2506.22367].
- Model choice. Replacing the Kravtsov et al. 2018 SHMR form by the Moster et
  al. 2013 one in DES Y3 changes the SHMR by about 1σ near log M* ~ 10.8 and
  less elsewhere; Planck 2018 instead of the hybrid DES Y3 + Planck cosmology
  has a negligible effect [src: Sect. 7.2.2–7.2.3 of arXiv:2506.22367].

## 5. Scatter–slope degeneracy
<!-- key: scatter-slope-degeneracy -->

- Mechanism. At high mass, the scatter of stellar mass at fixed halo mass and
  the slope of the SHMR are degenerate when only abundances are fitted;
  neglecting scatter alone biases the relation for centrals of massive haloes
  by as much as stellar-mass errors (arXiv:1001.0015) [src].
- Mitigation. Add clustering, lensing, groups or satellite kinematics; the iHOD
  breaks the degeneracy "without the need to assume a strong prior on the
  scatter" by modelling ~80% more galaxies (arXiv:1505.02781) [src].

- Group-based masses. DESI DR1 group masses have ~0.2 dex typical errors
  (arXiv:2610.20919) [src: Sect. VI.2], and the Yang et al. DESI groups carry
  ~0.2 dex scatter between abundance-matched and true mass, absorbed by an
  occupation-bias parameter in the assembly-bias test (arXiv:2510.20896)
  [src: main text]. HOD and group-catalogue satellite fractions of DESI BGS
  disagree because groups place fewer satellites in haloes below 10^12.5
  h⁻¹M_⊙ (arXiv:2609.04351) [src: Sect. VI.2].

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
- Size, KiDS-1000. Forcing Poisson satellites (𝒫 ≡ ⟨N_s(N_s−1)⟩/⟨N_s⟩² = 1)
  moves the halo-model result to S8 = 0.951 (+0.037, −0.036), Ω_m = 0.330 ±
  0.019, against 0.773 fiducial; the full fit stays formally acceptable (p =
  0.02) but w_p alone fails (p ~ 10⁻⁴), and GAMA groups are sub-Poisson below
  10¹³ h⁻¹M_⊙ [src: Sect. 4.4, Eqs. 51–52 of arXiv:2210.03110].
- Size. For DESI ELGs, imposing strict conformity divides f_sat by five and
  changes all HOD parameters except velocity dispersion, while f_1h and the
  mean halo mass stay put (arXiv:2306.06319) [src: Sect. 7.1].
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
  (arXiv:2111.02419) [src]. HSC-Y3 × SDSS: S8 is recovered to better than
  ~0.5σ on most mock catalogues (satellites on DM particles or subhaloes,
  off-centred centrals, central incompleteness, FoF haloes, Illustris-like
  baryons), while the two "worst-case" concentration-based assembly-bias
  mocks shift it by more than 0.5σ [src: Sect. III.7, App. A, Table 4 of
  arXiv:2304.00704]. The diagnostic is the shift of S8 between (2, 3) and (8,
  12) h⁻¹Mpc cuts; the data give p ≈ 50% for no assembly bias [src: Sect.
  VI.2]. In DESI DR2 LRG multiplets, concentration-based terms barely move
  w_p or multiplets, environment-based terms move both (arXiv:2511.15354)
  [src: Sect. 6.2].
- Budget by effect (TNG300 BOSS-like mock, lensing/clustering ratio A):
  galaxy-formation effects give A = 0.73–0.80 on all scales depending on the
  baryon strength and A = 0.91 above 4 h⁻¹Mpc, against 0.76 ± 0.03 and 0.86 ±
  0.06 measured; assembly bias contributes ΔA = 0.14 (all scales) and 0.07
  (large scales), the largest single term; baryons slightly more than
  parametric occupation or satellite segregation; subhalo lensing and halo
  triaxiality reduce the tension by ΔA ≈ 0.10 [src: Sect. 5.3 of
  arXiv:2211.01744].
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
  dark-matter dispersion (arXiv:1407.4811) [src]. Roughly 80% of subhalo
  disruption in Bolshoi is numerical rather than physical, "a serious
  road-block" for small-scale clustering (van den Bosch 2017,
  arXiv:1611.02657) [src]; idealised runs trace it mainly to inadequate force
  softening plus a discreteness-noise runaway instability, and give two
  criteria for discarding unreliable subhaloes (van den Bosch & Ogiya 2018,
  arXiv:1801.05427) [src]. Orphans are 10–30% of galaxies in some SAMs [sec:
  arXiv:1804.03097, Sect. 6.5.2]. Subhalo finders agree except below ~50
  particles and at host-centre passages, and merger-tree codes give "distinct
  results" on the same simulation [sec: arXiv:1804.03097, Sect. 6.5.2]. Smooth
  satellite profiles under-predict small-scale lensing (arXiv:2512.15962) [src:
  Sect. III.2]; satellite segregation is one of the three galaxy-formation
  effects behind the lensing-is-low excess in TNG300 (arXiv:2211.01744) [src].
  Baryons in MTNG put satellites 3–4% closer to halo centres than in the
  dark-matter-only twin and lower their velocities, changing clustering by
  10–20% at 0.1 h⁻¹Mpc (1–3σ for DESI-like errors), less on larger scales and
  less than sample selection (Contreras et al. 2025, arXiv:2512.04080) [src].
- Size of the satellite-profile choice (Basilisk, SDSS satellite kinematics
  + abundance): with n_sat(r) ∝ (r/𝓡r_s)^(−γ)(1 + r/𝓡r_s)^(γ−3) fitted per
  cosmology, the data prefer γ = 1 and 𝓡 ≈ 2.2 [src: Sect. 2.5, Eq. 14,
  Sect. 5.2 of arXiv:2512.14889]; imposing satellites that trace the dark
  matter (𝓡, γ) = (1, 1) gives ~2σ tension with Planck in the opposite
  direction to the usual S8 tension, and a subhalo-like cored profile (2.4, 0)
  gives ~5σ low Ω_m and σ8, with equally good luminosity-function fits [src:
  Sect. 5.2]. Baryonic corrections to the satellite velocity dispersion from
  no to extreme feedback (f_eject = 0–0.77 at 10¹² h⁻¹M_⊙) move (Ω_m, σ8) but
  stay within 2σ of Planck; an Illustris-2-like feedback model does not [src:
  Sect. 5.1].
- Mitigation. Free satellite concentration and velocity-bias parameters;
  restrict comparisons to resolution-converged regimes (as done by Reddick et
  al. 2013 and Lehmann et al. 2017 [sec: arXiv:1804.03097, Sect. 6.5.2]); scale
  cuts.

## 9. Lensing and clustering systematics in joint fits
<!-- key: lensing-and-clustering-systematics-in-joint-fits -->

- Source photometric redshifts. For z_L = 0.55, a 30% change in ΔΣ needs a
  photo-z bias Δz = 0.16 at z_S = 1; the measured impact of photo-z errors on
  the CMASS ΔΣ is at the 3% level [src: Sect. 5.1 of arXiv:1611.08606].
- Lens–source overlap. DES Y3 SHMR keeps only lens–source bin pairs with
  boost factors mostly within ~10% of unity and drops points above that
  [src: Sect. 5.4 of arXiv:2506.22367]; DES Y6 corrects γ_t by B(θ) = 1 +
  ω_LS(θ) [src: Sect. IV.3, Eq. 15 of arXiv:2601.15175].
- Source photo-z in DESI DR1 × HSC: dropping the HSC mean-redshift offsets
  raises S8 from 0.791 to 0.841 (~2.5σ) at Δχ² = +7.1, an extra ~0.019 on
  σ(S8) if marginalised; HSC-based results are photo-z limited [src: Sect.
  IV.2 of arXiv:2512.15962]. HSC-Y3 × SDSS shows that a N(0, 0.1) prior on
  the source shift biases S8 by > 1σ when the true shift is −0.2, hence its
  flat prior [src: Sect. III.7, App. A of arXiv:2304.00704].
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
- Baryonic effects on ΔΣ. In TNG300 vs Dark-TNG, baryons move mass outward
  and lower the cumulative mass around BOSS-like galaxies by ≃ 10% at ~1
  h⁻¹Mpc, so a DM-only HOD over-predicts small-scale GGL by about that much
  [src: Sect. 4.6 of arXiv:2211.01744]. In Illustris vs its gravity-only run,
  ΔΣ of matched parent haloes is up to 20% lower at intermediate radii,
  converging above 4 h⁻¹Mpc; at fixed number density (n̄ = 4 × 10⁻⁴ h³Mpc⁻³)
  the hydro run has twice the satellite fraction (22% vs 11%), and baryons
  change ΔΣ by 10–30% overall [src: Sect. 5.5 of arXiv:1611.08606]. Massive
  neutrinos (0.15–0.3 eV) lower ΔΣ by ~10% at most [src: Sect. 5.6]. TNG300 suppresses lensing by up to 10% at 1 h⁻¹Mpc,
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
- Lens magnification. Corrected with α_lmag = 1.93 ± 0.05 (LOWZ) and 2.62 ±
  0.28 (CMASS); the correction grows with redshift and stays below ~10% for
  the highest-z CMASS bin [src: Sect. 5.1.4 of arXiv:2202.07440].
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
- Mock validation of the DESI DR1 pipeline: a diffsky-based GalSampler LRG
  mock at z = 0.5 on UNIT (mass + concentration occupation) is fitted with χ²
  = 10.6 (p = 0.32) and the true cosmology lies at Δχ² = 3.4 in (S8, Ω_m),
  exceeded by 19% of Gaussian draws; only one LRG-like sample was tested
  [src: Sect. III.4 of arXiv:2512.15962].
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

- Pujol et al. 2017 on orphan fractions is quoted through the Wechsler &
  Tinker review, not read (van den Bosch 2017 was read on 2026-10-16).
- DES Y3 SHMR: its systematics-test section (Sect. 5.3 of arXiv:2506.22367)
  was not read; the sizes quoted come from its Sect. 3.5, 5.4 and 7.2.
- The DESI DR1 full-scale analysis has no systematics budget table: its
  verification is the single mock test above [src: Sect. III.4 of
  arXiv:2512.15962].
