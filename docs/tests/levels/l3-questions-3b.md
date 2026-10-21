# Level test — third L3 questions, part b

Forty specialist questions, eight per skill, for item C of
`docs/plans/2026-10-20-plan.md` ("the domains not yet tested"), part 3b. Written on
2026-10-20 from each skill's `references/subtopics.tsv` and from the level rule's
description of L3 ("how a result is derived and how to choose between methods"),
**before any `SKILL.md` body, reference file or dossier of the five skills was
opened**. What was known when they were written: the subtopic keys, titles, sources
and `files` columns of the five `subtopics.tsv` files, the file names under `deep/`
and `references/`, and the one-line skill descriptions shown in the skill listing
(the `description` field of each `SKILL.md` front matter).

Each question is one a practitioner preparing or refereeing an analysis would ask;
none is answered by a single headline number. Questions follow the weight of each
field, not one group's research. Per skill, questions 1–6 fall one each on the six
dossier subtopics; questions 7–8 fall on subtopics whose `files` column lists no
dossier, and are controls, where L3 should not help. None repeats a question of
`l3-questions.md` or `l3-questions-2.md`.

## cosmo-dark-energy-modified-gravity

Dossier subtopics: `wz-reconstruction` (D1), `interacting-dark-energy` (D2),
`fr-screening` (D3), `nonlinear-beyond-lcdm` (D4), `eg-statistic` (D5),
`forecasts-stage-iv` (D6). Controls: `model-comparison` (D7), `mu-sigma-growth` (D8).

- **D1** (referee, w(z) reconstruction) Binned w(z) with a correlation prior,
  Gaussian processes or crossing statistics: how does each reconstruction work, how
  are the correlation length and amplitude of the prior chosen, and how does one tell
  a data-driven departure from a prior-driven artefact (ΛCDM mocks, principal
  components, prior-only runs)?
- **D2** (analyst, interacting dark energy) For a coupling Q ∝ Hρ_c or Q ∝ Hρ_de,
  how are the perturbations treated (large-scale instabilities, frame of the
  momentum transfer, PPF-type schemes), which sign and form of coupling is stable,
  and how does one decide whether a preference for the coupling is distinguishable
  from a w0wa preference in the same data?
- **D3** (referee, f(R) and screening) How is |f_R0| constrained from cluster
  abundance, cluster profiles or galaxy-scale tests (distance indicators, rotation
  curves, dwarf kinematics); how is screening modelled in each test, and which
  simulations calibrate the non-linear predictions?
- **D4** (analyst, non-linear scales) Halo-model reaction, perturbation theory with
  modified kernels, emulators or full N-body: how does one choose to model the
  non-linear scales in a modified-gravity analysis, how are scale cuts set for each,
  and how is the choice validated?
- **D5** (referee, E_G) How is E_G estimated from galaxy–galaxy or CMB lensing,
  clustering and β = f/b — which estimator (annular Υ statistic or projected
  spectra), which scale cuts, how are lens magnification and the mismatch of lens
  and source redshift distributions handled — and how is the ΛCDM expectation
  computed for the comparison?
- **D6** (analyst, Stage-IV forecasts) How is a Stage-IV forecast for w0wa or μ–Σ
  built — Fisher matrix against sampling of a synthetic data vector, which nuisance
  parameters and scale cuts, how are cross-probe covariances included — and how are
  forecast codes validated against each other?
- **D7** (control, `model-comparison`) For a w0wa preference, how does one turn a
  Δχ² into a significance when the prior is informative or the parameters are
  bounded, and how do the profile likelihood, the Bayes factor and information
  criteria differ in what they report?
- **D8** (control, `mu-sigma-growth`) How are μ and Σ parameterised in time (tied to
  Ω_DE(a) or binned) and in scale, how are non-linear scales cut, and which data
  combinations break the μ–Σ degeneracy?

## cosmo-neutrinos-dark-matter

Dossier subtopics: `neutrino-mass-full-shape` (V1), `relic-neutrino-background`
(V2), `strong-lensing-substructure` (V3), `fuzzy-ultralight-dm` (V4),
`interacting-decaying-dm` (V5), `self-interacting-dm` (V6). Controls:
`wdm-lyman-alpha` (V7), `effective-mass-tension` (V8).

- **V1** (analyst, full shape) What does full-shape clustering add to Σm_ν beyond
  BAO geometry: how is the free-streaming suppression modelled in an EFT or
  perturbative fit (bias defined on cold matter or total matter, scale-dependent
  growth), which nuisance priors matter, and how are prior-volume effects handled?
- **V2** (analyst, relic neutrinos) How would a tritium-capture experiment of the
  PTOLEMY type detect the cosmic neutrino background — required energy resolution
  against m_ν, event rate and clustering enhancement, solid-state effects of the
  tritium substrate — and which other detection routes are considered and why are
  they weaker?
- **V3** (referee, strong-lensing substructure) Flux-ratio anomalies of quadruply
  imaged quasars or gravitational imaging of extended arcs: how is the substructure
  signal inferred (forward modelling with approximate Bayesian computation or a
  likelihood), how are line-of-sight haloes, macromodel complexity (multipoles,
  discs) and source size treated, and how is the result turned into a
  warm-dark-matter limit?
- **V4** (analyst, fuzzy dark matter) How is the ultralight-axion mass constrained
  from the Lyα forest, from CMB + LSS for a sub-component, and from dwarf-galaxy
  dynamics or subhalo counts — which modelling (Boltzmann codes with axions, wave
  simulations, solitons) and how robust is each route?
- **V5** (referee, interacting and decaying DM) How are dark matter–baryon
  scattering cross sections constrained from the CMB and from Milky Way satellites
  (velocity dependence σ ∝ vⁿ, interacting fraction), how is decaying dark matter
  constrained, and how does one choose between data sets for a given model?
- **V6** (referee, SIDM) How is σ/m constrained from cluster mergers (offsets),
  cluster central densities and dwarf rotation curves; which simulations calibrate
  the mapping from observable to cross section, and how does a velocity-dependent
  cross section change the inference?
- **V7** (control, `wdm-lyman-alpha`) How is the thermal history of the IGM
  marginalised in a Lyα warm-dark-matter analysis, and how is the half-mode scale
  converted to thermal-relic and sterile-neutrino masses?
- **V8** (control, `effective-mass-tension`) How is an effective (signed) neutrino
  mass defined and fitted, and how is a profile likelihood used to quote the
  tension with the oscillation lower bound?

## cosmo-inflation-primordial

Dossier subtopics: `slow-roll-model-comparison` (I1), `tensor-bmode-likelihood`
(I2), `bmode-foreground-separation` (I3), `delensing` (I4), `cmb-bispectrum` (I5),
`lss-bispectrum-png` (I6). Controls: `scale-dependent-bias` (I7),
`cosmic-birefringence` (I8).

- **I1** (analyst, model comparison) How is an inflationary model confronted with
  (n_s, r): how are the number of e-folds and the reheating history treated, how is
  the Bayesian evidence across models computed, and which conclusions on Starobinsky
  or α-attractor models after the ACT DR6 shift in n_s depend on the reheating
  assumptions?
- **I2** (referee, B-mode likelihood) How is a BICEP/Keck-type B-mode likelihood
  built — likelihood form for cross-spectra at several frequencies, band-power
  window functions, simulated bias and covariance, E-to-B leakage from filtering —
  and how is the 95% upper limit on r constructed (Bayesian with a prior r ≥ 0, or
  frequentist)?
- **I3** (analyst, foregrounds for r) Parametric cross-spectrum fitting, map-based
  parametric separation, or blind methods (NILC): how does one choose, how are dust
  decorrelation and the spatial variation of the spectral indices treated (moment
  expansion), and how is the residual bias on r estimated?
- **I4** (analyst, delensing) Internal reconstruction against CIB or galaxy tracers:
  how is the lensing B-mode template built, how does it enter the likelihood (as an
  extra map in the cross-spectra or by subtraction), and which biases arise (shared
  modes, noise in the template)?
- **I5** (referee, CMB bispectrum) KSW, binned and modal estimators: how do they
  differ, how is the linear term for masks and anisotropic noise handled, how are
  the lensing–ISW and point-source bispectra subtracted, and how is the estimator
  validated on simulations?
- **I6** (analyst, LSS bispectrum and f_NL) How is local or equilateral f_NL
  constrained from the galaxy bispectrum — model with primordial terms, prior on
  b_φ, window and covariance — and how does map-level (field-level) inference of
  f_NL compare with it?
- **I7** (control, `scale-dependent-bias`) How is b_φ chosen for quasars or LRGs and
  how does it change f_NL from scale-dependent bias; how are imaging systematics on
  large scales mitigated?
- **I8** (control, `cosmic-birefringence`) How is a miscalibration of the
  polarisation angle separated from cosmic birefringence (Galactic foreground EB as
  calibrator), and which systematic dominates?

## cosmo-cmb-lss-cross-correlations

Dossier subtopics: `ksz-gas-profiles` (X1), `ksz-velocity-reconstruction` (X2),
`tsz-cross-correlations` (X3), `isw` (X4), `cib-cross-correlations` (X5),
`other-secondaries` (X6). Controls: `lensing-tomography` (X7),
`lensing-map-systematics` (X8).

- **X1** (analyst, kSZ gas profiles) Stacking with aperture photometry, pairwise
  momentum or projected-field estimators: which needs reconstructed velocities or an
  optical-depth model, how is the τ–velocity degeneracy broken, how is the profile
  mapped onto a feedback constraint, and how are tSZ/CIB contamination and
  miscentring handled?
- **X2** (referee, kSZ velocity reconstruction) How is the quadratic estimator for
  the large-scale velocity built, how is the optical-depth degeneracy (b_v) treated,
  how are the small-scale galaxy–electron spectrum and foregrounds modelled, and how
  is f_NL extracted from P_gv?
- **X3** (analyst, tSZ cross-correlations) How is the y map built (ILC with CIB or
  CMB deprojection), how is the bias-weighted pressure ⟨bP_e⟩ measured, how do
  pressure-profile models (GNFW, halo model) enter, and how is CIB or radio leakage
  quantified?
- **X4** (referee, ISW) Temperature × tracer cross-spectra or stacking on
  superstructures: how is the significance computed (covariance from simulations,
  a-posteriori choices), what amplitude is fitted, and how should the stacking
  excess be weighed against the cross-spectrum result?
- **X5** (analyst, CIB cross-correlations) How are CIB maps cleaned of Galactic dust
  (H I templates), which halo models of the CIB are fitted, and how is the CIB used
  as a delensing tracer or for f_NL — which cross-spectra and which systematics?
- **X6** (referee, other secondaries) Moving lens, polarised SZ and patchy
  screening: which estimators are used, what detection significance is measured or
  forecast, and which contaminants limit each?
- **X7** (control, `lensing-tomography`) How is S8 or σ8(z) inferred from CMB lensing
  × galaxies (estimator, bias model, redshift distributions), and how should it be
  compared with the lensing auto-spectrum and cosmic shear?
- **X8** (control, `lensing-map-systematics`) How is the extragalactic-foreground
  bias of the lensing map handled in a cross-correlation, and how is the Monte Carlo
  normalisation on the overlap footprint done?

## cosmo-beyond-two-point

Dossier subtopics: `void-finding-size-function` (T1), `void-galaxy-rsd-ap` (T2),
`void-lensing-cmb` (T3), `emulator-summary-statistics` (T4),
`field-level-inference` (T5), `simulation-based-inference` (T6). Controls:
`bispectrum-full-shape` (T7), `lensing-higher-order` (T8).

- **T1** (analyst, void finding and size function) Watershed (ZOBOV, VIDE,
  REVOLVER) or spherical-underdensity finders: how does one choose, how is the void
  size function modelled (Sheth–van de Weygaert, volume-conserving Vdn with a
  calibrated threshold, tracer bias), and how are mocks used to calibrate it?
- **T2** (referee, void–galaxy RSD and AP) How is the void–galaxy cross-correlation
  modelled in redshift space (linear model with or without reconstruction, velocity
  profile, void-centre displacement), how is the covariance built, and how are the
  selection effects of finding voids in redshift space handled?
- **T3** (referee, void lensing and CMB) How are the stacked void shear profile and
  the void imprints on the CMB (ISW, CMB lensing) measured and modelled, how does the
  choice of void sample (void-in-cloud, size cuts) change the signal, and how is the
  significance of an excess assessed?
- **T4** (analyst, emulated summary statistics) Density split, kNN, wavelet
  scattering or marked spectra with simulation emulators: how is the emulator
  trained (simulation suite, galaxy–halo model), how is its error included in the
  likelihood, and how are scale cuts and the galaxy–halo model validated?
- **T5** (analyst, field-level inference) Forward model (LPT, EFT), likelihood
  (Gaussian in Fourier space with EFT noise, Poisson), sampler (HMC and variants):
  how does one choose between BORG-type and LEFTfield-type approaches, and which
  diagnostics establish convergence and correctness?
- **T6** (referee, simulation-based inference) Neural posterior or likelihood
  estimation, compression (MOPED, IMNN, VMIM), coverage tests (SBC, TARP) and
  misspecification checks: how is each chosen, and how many simulations are needed?
- **T7** (control, `bispectrum-full-shape`) How are the bispectrum window and its
  covariance treated in a joint P + B fit?
- **T8** (control, `lensing-higher-order`) Peaks, PDF or third-order shear: how are
  baryons and intrinsic alignments included, and how is the covariance computed?
