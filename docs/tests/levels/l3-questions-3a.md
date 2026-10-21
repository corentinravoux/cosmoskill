# Level test — third L3 questions, part 3a

Forty specialist questions, eight per skill, for item C of
`docs/plans/2026-10-20-plan.md` ("the domains not yet tested"). Written on
2026-10-20 from each skill's `references/subtopics.tsv` and from the level
rule's description of L3 ("how a result is derived and how to choose between
methods"), **before any `SKILL.md` body, reference file or dossier of the five
skills was opened**. What was known when they were written: the subtopic keys,
titles, sources and `files` columns of the five `subtopics.tsv` files, the file
names under `deep/` and `references/`, and the one-line skill descriptions
shown in the skill listing (the `description` field of each `SKILL.md` front
matter). Part 3b, run at the same time by another agent on other skills, has its
own file.

Each question is one a practitioner preparing or refereeing an analysis would
ask; none is answered by a single headline number. Per skill, questions 1–6
fall one each on the six subtopics that have a dossier; questions 7–8 fall on
subtopics whose `files` column lists no dossier, and are controls, where L3
should not help. Questions follow the field as a whole: where several groups or
methods compete, the question names them, not one group's choice. None repeats
a question of `l3-questions.md` or `l3-questions-2.md`.

Note on `cosmo-tensions-anomalies`: `deep/` holds six dossiers, but the
`files` column of `subtopics.tsv` lists a dossier for only three rows
(`large-angle-cmb-anomalies`, `high-redshift-galaxies`,
`theoretical-resolutions`). The dossiers `anomaly-significance.md`,
`cmb-bao-mismatch.md` and `cosmic-dipoles.md` match the keys of three rows that
do not list them. Questions T2–T4 were assigned to those rows by name; the
controls T7–T8 were taken from rows with no dossier of that name.

## cosmo-distance-ladder-h0

Dossier subtopics: `cepheid-sn-ladder` (H1), `trgb` (H2), `jagb-miras` (H3),
`megamasers` (H4), `time-delay-cosmography` (H5), `inverse-ladder` (H6).
Controls: `ladder-statistics` (H7), `high-z-standardisable-candles` (H8).

- **H1** (referee, Cepheid–SN ladder) How is the Cepheid period–luminosity
  relation calibrated inside the joint ladder fit — Wesenheit index (optical or
  near-infrared), crowding corrections from artificial stars, metallicity
  term — and how does one test whether crowding biases the host-galaxy
  Cepheids (for instance with JWST photometry), and what do the groups that
  reanalysed the SH0ES data do differently?
- **H2** (analyst, TRGB) How is the tip magnitude measured — edge detector,
  smoothing of the luminosity function, field and colour selection, contrast
  ratio — how are the systematic choices of the detection quantified, and why
  do TRGB analyses of overlapping hosts give different H0?
- **H3** (referee, JAGB and Miras) How is the JAGB reference magnitude defined
  (mode, median, model fit of the luminosity function) and its colour window
  chosen, how are Mira period–luminosity relations calibrated (O-rich or
  C-rich, period range), and what limits each as an SN Ia calibrator?
- **H4** (analyst, megamasers) How is a geometric distance derived from a
  maser disc — VLBI positions, line-of-sight velocities, accelerations, disc
  warp — and how are host peculiar velocities treated when several maser
  distances are turned into H0?
- **H5** (referee, time delays) How is the mass-sheet degeneracy handled —
  power-law or composite lens models, stellar kinematics (aperture or spatially
  resolved), external convergence from the line of sight — how does the choice
  of assumptions move H0, and how are the analyses blinded?
- **H6** (analyst, inverse ladder) How is an inverse-ladder H0 built from BAO
  and SNe with r_d calibrated by the CMB or by BBN, how does it depend on the
  r_d prior and on the SN sample, and how is a sound-horizon-free H0 obtained?
- **H7** (control, `ladder-statistics`) How is the ladder likelihood built —
  covariance between rungs, outlier rejection, a distance network against a
  linear fit — and how are selection effects on calibrator distances treated?
- **H8** (control, `high-z-standardisable-candles`) How is a quasar Hubble
  diagram built from the X-ray–UV relation, how is it calibrated, and how does
  one test whether the relation evolves with redshift or is circular?

## cosmo-tensions-anomalies

Dossier subtopics: `large-angle-cmb-anomalies` (T1), `anomaly-significance`
(T2), `cmb-bao-mismatch` (T3), `cosmic-dipoles` (T4), `high-redshift-galaxies`
(T5), `theoretical-resolutions` (T6). Controls: `s8-tension` (T7),
`cosmological-principle` (T8).

- **T1** (referee, large-angle anomalies) How is the significance of the
  lack of large-angle correlation (S_1/2), the hemispherical power asymmetry
  or the Cold Spot computed — which estimator, which mask, which simulations,
  temperature only or with polarisation — and how does the result depend on
  the mask and the map?
- **T2** (analyst, significance) How does one correct an anomaly's
  significance for the a posteriori choice of statistic and for the look-
  elsewhere effect, and what counts as an independent test that could confirm
  or refute it?
- **T3** (analyst, CMB–BAO) How is the CMB–BAO mismatch quantified (which
  plane, which CMB likelihood or compression, which BAO data), and how does one
  choose between the extensions that absorb it (τ, w0wa, Σm_ν < 0, Ω_K) — what
  data would separate them?
- **T4** (referee, dipoles) How is a number-count dipole measured from a radio
  or infrared quasar catalogue — estimator, mask, the index x of the counts and
  the spectral index α, systematic templates — and how are the expected
  kinematic amplitude and the significance of the excess computed?
- **T5** (referee, JWST galaxies) How is a claim of too many massive galaxies at
  high redshift tested against ΛCDM — stellar-mass estimates (IMF, SED fitting,
  AGN contamination), cosmic variance, the bound from the baryon fraction — and
  how should one decide whether it is a cosmological tension?
- **T6** (analyst, resolutions) How are proposed solutions of the Hubble
  tension (early dark energy, varying m_e, late-time or interacting dark
  energy) compared fairly — which data combinations, which metrics, prior-volume
  effects — and how is one ranked above another?
- **T7** (control, `s8-tension`) How should S8 from cosmic shear, clusters,
  CMB lensing and tSZ be compared with the CMB value — which definition of S8,
  which scales, which baryon treatment — before it is called a tension?
- **T8** (control, `cosmological-principle`) How is the homogeneity scale
  measured from a galaxy survey (counts in spheres, fractal dimension), and how
  are inhomogeneous models (LTB, backreaction, timescape) tested against data?

## cosmo-peculiar-velocities

Dossier subtopics: `distance-indicators` (V1), `two-point-statistics` (V2),
`field-level-likelihood` (V3), `velocity-density-comparison` (V4),
`bulk-flows` (V5), `supernova-velocities` (V6). Controls:
`zero-point-malmquist` (V7), `nonlinear-velocity-modelling` (V8).

- **V1** (analyst, distance indicators) How is a Fundamental Plane or
  Tully–Fisher relation fitted for peculiar-velocity work — 3D Gaussian maximum
  likelihood, forward or inverse fit, orthogonal regression — how are selection
  and truncation included, and how is the model of the intrinsic scatter
  tested?
- **V2** (analyst, two-point) For the momentum power spectrum or the velocity
  correlation functions, how are the estimator, the window function and the
  covariance handled, and how does one choose between configuration and
  Fourier space for fσ8?
- **V3** (referee, field level) In a field-level (maximum-likelihood fields or
  covariance-based) analysis of densities and velocities, how is the
  covariance computed for many galaxies, how is the non-Gaussian error of the
  log-distance ratio treated, and what limits the method in size and speed?
- **V4** (analyst, velocity–density) How is β or fσ8 obtained by comparing
  measured velocities with velocities reconstructed from a redshift survey —
  which reconstruction, how the external bulk flow and the distance-indicator
  model are fitted (forward or inverse), what limits the result?
- **V5** (referee, bulk flows) Which bulk-flow estimator should be used
  (maximum likelihood, minimum variance, η-based), how does its window function
  set the ΛCDM expectation, and how is the significance of a large flow
  computed?
- **V6** (analyst, SN velocities) How are SN Ia velocities used as signal (ZTF,
  Rubin) — intrinsic scatter, host-dependent standardisation, selection — and
  how large is the effect of correlated velocities as a nuisance in a
  Hubble-diagram fit?
- **V7** (control, `zero-point-malmquist`) How is the zero point of a
  peculiar-velocity catalogue set and its uncertainty propagated, and how is
  inhomogeneous Malmquist bias corrected?
- **V8** (control, `nonlinear-velocity-modelling`) How is the non-linear
  damping of the velocity power spectrum (σ_u) modelled, and how is the k_max
  of the fit chosen?

## cosmo-lyman-alpha

Dossier subtopics: `continuum-distortion` (F1), `p1d-estimation` (F2),
`p1d-emulators` (F3), `theory-sbi-field-level` (F4),
`validation-mocks-blinding` (F5), `tomography-voids` (F6). Controls:
`contaminants-3d` (F7), `igm-thermal-state` (F8).

- **F1** (referee, continuum) How are quasar continua fitted (mean continuum
  with per-quasar amplitude and slope, PCA or predicted continua), how is the
  resulting distortion of the correlations modelled (distortion matrix or
  forward projection), and how does the choice affect BAO against full-shape
  fits?
- **F2** (analyst, P1D estimation) FFT or QMLE: how does one choose, how are
  resolution, noise power and masking corrected, and how is the covariance
  estimated?
- **F3** (analyst, emulators) How is a P1D emulator built (Gaussian process or
  neural network; which IGM and cosmological parameters), how is emulator error
  included in the likelihood, and how is it validated against simulations it
  was not trained on?
- **F4** (referee, theory and SBI) For EFT-based or simulation-based inference
  of the forest, which scales are valid, how are the nuisance parameters
  (b, b_η, counterterms) treated, and how is a simulation-based or field-level
  forward model validated?
- **F5** (analyst, validation) How are synthetic data sets used to validate a
  3D Lyα analysis — which mocks, which contaminants injected, which recovery
  criterion — and how was the analysis blinded?
- **F6** (analyst, tomography) How is a Lyα tomographic map reconstructed
  (Wiener filter, correlation lengths, noise model, sightline density), how are
  voids or protoclusters found in it, and how are reconstruction effects
  calibrated with mocks?
- **F7** (control, `contaminants-3d`) How are high-column-density absorbers
  treated in the 3D correlations (masking against a template, its length
  parameter), and how are metal-line correlations modelled?
- **F8** (control, `igm-thermal-state`) How are T0 and γ inferred from the
  forest — which statistics (curvature, line widths, wavelets, P1D) — and how do
  pressure smoothing and degeneracies enter?

## cosmo-clusters

Dossier subtopics: `optical-selection-projection` (K1),
`x-ray-selection-function` (K2), `sz-selection-function` (K3),
`cmb-cluster-lensing` (K4), `cluster-clustering` (K5), `gas-mass-fraction`
(K6). Controls: `weak-lensing-mass-calibration` (K7), `hydrostatic-mass-bias`
(K8).

- **K1** (referee, optical selection) How are projection effects on richness
  modelled and calibrated (simulations, spectroscopy, a projection kernel in
  P(λ|M)), how do they bias stacked lensing, and how do the DES, KiDS and HSC
  analyses differ in treating them?
- **K2** (analyst, X-ray selection) How is an X-ray selection function computed
  (simulated sky with injected clusters, dependence on count rate and extent,
  AGN and point-source contamination), and how is it validated?
- **K3** (analyst, SZ selection) How is the SZ selection built — matched filter
  and its profile, observed against unbiased signal-to-noise, optimisation
  bias — and how are completeness and purity estimated?
- **K4** (referee, CMB cluster lensing) How is a cluster mass measured from CMB
  lensing (quadratic estimator or maximum likelihood, gradient cleaning), and
  how are tSZ and kSZ contamination and miscentring handled?
- **K5** (analyst, clustering) How is cluster clustering added to counts —
  which statistic, which halo-bias model, the covariance between counts and
  clustering — and how much mass self-calibration does it give?
- **K6** (referee, f_gas) How is the gas-mass fraction measured and used for
  cosmology — relaxed-sample selection, the measurement shell, mass calibration
  by lensing, the depletion factor from simulations — and how much do the priors
  drive the result?
- **K7** (control, `weak-lensing-mass-calibration`) How is the weak-lensing mass
  of a cluster sample calibrated — shear-profile model, M_WL–M bias from
  simulations, miscentring, boost factors?
- **K8** (control, `hydrostatic-mass-bias`) How is 1 − b estimated, and why do
  the routes (lensing, CMB lensing, simulations, counts against the CMB)
  disagree?
