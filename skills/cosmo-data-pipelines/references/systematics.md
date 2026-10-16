# Data pipelines — systematics

Scope: pipeline-level systematics — mechanism, size where a paper quantifies
it, mitigation, validation test, and the paper a referee expects. The
propagation of each into a cosmological parameter is in the probe skills.
Snapshot: 2026-10-16

Flags: `[src]` abstract read this session; `[src: Sect. n]`, `[src: Table n]`
body read; `[sec]` named secondary source; `[der]` derived here.

## 1. Sky-subtraction residuals

- Mechanism. Errors in the fibre flat field, wavelength solution and PSF
  shape leave residuals on bright OH lines; the residual looks like an
  emission line and can be fitted as one.
- Size. DESI: excess scatter of 1–3% of the sky level on the brightest lines
  in 1000 s exposures, consistent with noise in the continuum
  [src: arXiv:2209.14482, Sect. IV.7.5]; < 1% systematic overall
  [src: arXiv:2503.14745, Table 6]. LAMOST ~3% on lines and continuum
  (arXiv:1705.02079) [src]. In long fibre integrations a systematic floor is
  reached after 4–10 h on AAOmega (arXiv:1007.0648) [src].
- Mitigation. An extra variance term on sky lines (DESI ε_λ,
  arXiv:2209.14482, Sect. IV.7.4) [src]; PCA of residuals
  (arXiv:1007.0648) [src]; throughput modelled against positioner location
  in DESI DR1 [src: arXiv:2503.14745, Sect. III.1.3]; beam switching
  (arXiv:1609.06142) [src].
- Test. RMS of sky-fibre residuals against the noise model, as a function
  of wavelength; false-positive redshifts on sky fibres, which the DESI
  archetype refit lowers by 5–40% (arXiv:2405.19288) [src].

## 2. Redshift failures and catastrophic redshifts

- Mechanism. Line confusion ([O II] vs other lines, quasar line
  misidentification), low S/N, spectral steps between arms, and host-galaxy
  dominated or reddened quasars that templates miss.
- Size. DESI DR1 outliers ≤ 0.3% for BGS, LRG and ELG, 0.7% for quasars at
  z < 2.1 and 1.8% above [src: arXiv:2503.14745, Table 6]; the standard DESI
  pipeline recovers ~86% of VI quasars against ~94% with after-burners
  (arXiv:2208.08517) [src]; BOSS CMASS ~0.2% wrong among confident
  redshifts (arXiv:1207.7326) [src].
- Dependence on conditions. The LRG redshift efficiency varies with source
  brightness and effective exposure time (arXiv:2208.08515) [src]; the
  observed variation of success with observing conditions and its weights
  are in `cosmo-galaxy-clustering` (systematics, Sect. 6).
- Mitigation. Quality cuts on Δχ² (and [O II] S/N for ELGs), after-burners,
  redshift-failure weights in the LSS catalogue (Sect. 8).
- Test. VI truth tables, repeat observations, deep co-adds.

## 3. Redshift-error calibration

- Mechanism. The formal error from photon noise can be wrong in either
  direction.
- Size. BOSS: underestimated by a factor 1.19–1.34 for galaxies and 2 for
  quasars (arXiv:1207.7326) [src]; eBOSS redmonster: overestimated by ~54%
  (arXiv:1607.02432) [src].
- Test. Distribution of repeat differences scaled by the quoted errors.
- Why it matters. Redshift errors smear the line-of-sight clustering and set
  the floor for peculiar-velocity and Lyα work (see `cosmo-galaxy-clustering`
  and `cosmo-lyman-alpha`).

## 4. Slitless-spectroscopy contamination and line misidentification

- Mechanism. Overlapping traces of neighbours contaminate each spectrum;
  single-line spectra are ambiguous.
- Size. Euclid Q1 reaches 89% success at 0.9 < z < 1.8 only with tuned
  quality cuts (arXiv:2503.15308) [src]; in pixel-level simulations,
  contaminants in the same redshift range as the targets cause about 4% of
  the total degradation from cross-contamination
  (Euclid Collaboration 2026, arXiv:2606.24697) [src].
- Mitigation. Contamination modelling from the photometric catalogue in SIR
  (arXiv:2503.15307) [src]; purity-driven cuts; random catalogues built from
  a detection model (see `cosmo-galaxy-clustering`).

## 5. Sensor effects: brighter-fatter, charge transfer, stray fields

- Mechanism. Charge accumulated in a pixel deflects later charge; PSF size
  then depends on flux, so a PSF model built from bright stars is wrong for
  faint galaxies.
- Size. Up to 2% growth in star size over the dynamic range
  (arXiv:1402.0725) [src]; in DECam the induced shape bias on bright stars
  exceeds weak-lensing requirements before correction (arXiv:1501.02802)
  [src].
- Mitigation. Pixel-level reverse charge shifts fitted to flat-field
  correlations (arXiv:1501.02802) [src]; Rubin applies a brighter-fatter
  correction in ISR [src: arXiv:2603.23786, Sect. IV.2.1]; PSF star
  selection that excludes the brightest stars.
- Test. Star size versus flux after correction; flat-field covariance.

## 6. Astrometric residuals

- Mechanism. Atmospheric turbulence, unmodelled stray fields, focal-plane
  shifts, differential chromatic refraction.
- Size. 2–4 mas RMS each from stray fields and from thermal-cycle shifts in
  DECam, after a 7 mas atmospheric interpolation (arXiv:1703.01679) [src].
- Why it matters. Astrometric scatter between exposures blurs co-adds and
  mimics PSF anisotropy: KiDS-Legacy removed 46.6 deg² with large
  inter-exposure astrometric scatter after a B-mode failure
  [sec: cosmo-weak-lensing, systematics Sect. 3, KiDS-Legacy row].
- Test. Repeatability of pair separations (Rubin AM1,
  arXiv:2603.23786, Sect. V.3) [src]; residual maps against Gaia.

## 7. Blending and deblender failures

The shear and n(z) consequences are in `cosmo-weak-lensing` (systematics,
Sect. 2); here the catalogue-level failure.

- Mechanism. Overlapping sources are merged (unrecognised blends) or split
  wrongly; fluxes, colours and positions of children are biased.
- Size. For LSST full depth (**forecast**), ~62% of detected galaxies have at least 1% of
  the flux in their pixels from neighbours, and blending lowers the effective
  number density by ~18%, to at most 39.4 arcmin⁻² in r (Sanchez et al.
  2021, arXiv:2103.02078) [src]. In Rubin DP1, the unrecognised-blend
  fraction against HST/CANDELS is 18.0% for the production catalogue and
  14.9% for DeepDISC (arXiv:2610.10986) [src]. The HSC deblender fails in
  most cluster cores (arXiv:1705.06766) [src: Sect. 4.8.3].
- Mitigation. Multi-band deblenders (SCARLET), blendedness flags,
  undeblended photometry, image simulations with realistic blending
  (Sect. 10).
- Test. Injection–recovery with the same deblender; comparison with deeper
  space imaging; the BTK benchmark (arXiv:2607.28475) [src].

## 8. CMB map-maker model error and transfer function

- Mechanism. Any mismatch between the data model and the data (sub-pixel
  signal structure, detector gain mismatch) leaks into long-wavelength modes
  of the solution.
- Size. O(1) power loss on large scales is possible for realistic
  ground-based conditions, and it is invisible to simulations that do not
  model the error (Naess & Louis 2023, arXiv:2210.02243) [src]. In ACT DR6
  the mapmaker converged to an unbiased map in simulations but a biased one
  against Planck on data, which was traced to model error
  [src: arXiv:2503.14451, Sect. V.2].
- Mitigation. Bilinear pointing matrices for the sub-pixel case
  (arXiv:2210.02243) [src]; model-error degrees of freedom near bright
  sources [src: arXiv:2503.14451, Sect. III.3.4]; transfer functions
  measured by injection into real data rather than pure simulations
  [src: Sect. V.2]; cross-calibration against Planck.
- Test. Map-level comparison with Planck at low ℓ; null splits by PWV,
  elevation, time and detector position [src: arXiv:2503.14451,
  Sect. III.6 outline].

## 9. Instrument non-linearity, bandpass and polarisation-efficiency errors

- Mechanism. ADC non-linearity, bandpass mismatch between detectors, and
  polarisation-efficiency errors distort polarisation at large angles and
  leak intensity into polarisation.
- Mitigation. Fit them inside map-making from data redundancy (SRoll2,
  arXiv:1901.11386; HFI 2018 bandpass-mismatch coefficients,
  arXiv:1807.06207) [src]; half-wave-plate map-makers that marginalise slow
  unpolarised signals (arXiv:2606.31720) [src].
- Test. Null tests and end-to-end simulations; the component-separation
  simulations still differ from data by a few percent (arXiv:1807.06208)
  [src].

## 10. Imaging-systematics weights: over- and under-correction

- Mechanism. Target density responds to depth, seeing, extinction, stellar
  density; regressing it out removes spurious power but also real modes, and
  each method has its own bias.
- Size. Template subtraction in its original form is biased; extended mode
  projection is biased; basic mode projection is not; all add variance
  (arXiv:1509.08933) [src]. eBOSS QSO null-test χ²/dof 776/10 before weights,
  6/8 after (arXiv:2007.09000) [src].
- Mitigation. Cross-validated regressions (arXiv:1907.11355) [src];
  comparing several methods and carrying their spread as a systematic
  (arXiv:2105.13540) [src]; forward modelling by injection
  (arXiv:2007.08992) [src].
- Test. Density against each map after weighting; contaminated mocks through
  the same regression. The cosmological consequence and the f_NL case are in
  `cosmo-galaxy-clustering`.

## 11. Imaging-region inhomogeneity and anisotropic n(z)

- Mechanism. Parent imaging of different depth (DES vs DECaLS, North vs
  South) changes both the density and the redshift distribution of the
  same colour selection.
- Size. In DESI DR2, ELGs in the DES footprint have a higher density, lack
  targets with extreme colours and have a distinct n(z) by colour
  subsample; DES is now treated separately in the catalogue pipeline,
  "in some cases, imperative" (arXiv:2606.18581) [src]. For photometric
  samples, using one global n(z) underestimates w(θ) by up to ~10% at small
  scales in the highest bin; for an LSST-like setup (**forecast**) σ8 is biased low by 1.7σ
  (Zhang et al. 2026, arXiv:2609.15542) [src].
- Mitigation. Regions treated separately for weights and for the randoms'
  redshifts (arXiv:2405.16593, Sect. 7.2) [src]; north–south resolve at
  targeting (arXiv:2208.08518) [src].

## 12. Random-catalogue and footprint errors

- Mechanism. Randoms that do not follow the true selection (missing vetoes,
  wrong coverage count, mismatched dN/dz) create spurious clustering.
- Mitigation and its cost. Sampling random redshifts from the data nulls
  radial modes (radial integral constraint, arXiv:2405.16593, Sect. 7.2)
  [src]; for slitless surveys, randoms from a detection model of line S/N
  (arXiv:2511.20856) [src]; randoms from injected sources
  (arXiv:1507.08336) [src].
- Test. Data/random ratio against every survey property and against the
  coverage count N_tile.

## 13. Pipeline-version dependence of the selection function

- Mechanism. In a survey with spectroscopic feedback, the redshifts that
  decided re-observation were made with the pipeline version of the night,
  while the catalogue uses a later reduction.
- Example. DESI applies ZWARN_MTL from the same reduction as the redshifts
  for the footprint, which complicates the alternative-MTL realisations
  used for pair probabilities [src: arXiv:2405.16593, Sect. 4.2]; every tile
  is re-designed the next morning to check reproducibility
  [src: arXiv:2306.06309, Sect. V.9].
- Test. Re-run of targeting and assignment from stored ledgers; releases that
  state every code and reduction version.

## Not verified
