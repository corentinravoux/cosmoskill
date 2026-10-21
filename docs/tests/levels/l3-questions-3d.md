# Level test — third L3 questions, part 3d

Thirty-two specialist questions, eight per skill, for item C of
`docs/plans/2026-10-20-plan.md` ("the domains not yet tested"), part 3d. Written on
2026-10-20 from each skill's `references/subtopics.tsv` and from the level rule's
description of L3 ("how a result is derived and how to choose between methods"),
**before any `SKILL.md` body, reference file or dossier of the four skills was
opened**. What was known when they were written: the subtopic keys, titles, sources
and `files` columns of the four `subtopics.tsv` files, the file names under `deep/`
and `references/`, and the one-line skill descriptions shown in the skill listing
(the `description` field of each `SKILL.md` front matter). Parts 3a, 3b and 3c
(`l3-questions-3a.md`, `l3-questions-3b.md`, `l3-questions-3c.md`) cover other
skills; their question ids use the letters B, C, D, E, F, G, H, I, J, K, N, P, Q, S,
T, V, W, X, so this part uses M, A, Z and R. Other parts run at the same time and
write their own files.

Each question is one a practitioner preparing or refereeing an analysis would ask;
none is answered by a single headline number. Per skill, questions 1–6 fall one each
on the six subtopics that have a dossier; questions 7–8 fall on subtopics whose
`files` column lists no dossier, and are controls, where L3 should not help.
Questions follow the field as a whole: where several groups or methods compete, the
question names them, not one group's choice. None repeats a question of
`l3-questions.md`, `l3-questions-2.md`, `l3-questions-3a.md`, `l3-questions-3b.md`
or `l3-questions-3c.md`.

Note on `cosmo-machine-learning` and `cosmo-photometry-photoz`: each `deep/` holds
six dossiers, but the `files` column of `subtopics.tsv` lists a dossier for only
three rows. In `cosmo-machine-learning` the dossiers `emulators.md`,
`generative-models.md` and `learned-simulation-corrections.md` match the keys of
three rows that do not list them; in `cosmo-photometry-photoz` the dossiers
`photometric-calibration.md`, `population-forward-models.md` and
`narrow-many-band-photometry.md` do the same. As in part 3a, the questions on those
rows were assigned by name, and the controls were taken from rows with no dossier of
that name.

## cosmo-machine-learning

Dossier subtopics: `emulators` (M1), `classification` (M2), `generative-models`
(M3), `interpretability` (M4), `learned-simulation-corrections` (M5),
`uncertainty-reproducibility` (M6).
Controls: `neural-density-estimation` (M7), `anomaly-detection` (M8).

- **M1** (referee, emulators) How is an emulator of a summary statistic (P(k),
  C_ℓ, halo mass function) built and validated — design of the training set (Latin
  hypercube, Sobol, active learning), architecture (neural network as in CosmoPower
  against Gaussian process as in DarkEmulator or the Euclid and Aemulus emulators,
  PCA compression of the outputs), the accuracy target set against the data errors —
  and how does the emulator error enter the likelihood (added covariance,
  marginalised, or ignored)?
- **M2** (analyst, classification) For photometric classification of transients
  (PLAsTiCC, ELAsTiCC), how do feature-based classifiers (boosted trees) compare with
  sequence or image networks (SuperNNova, SCONE), how is the non-representative
  spectroscopic training set (bright, low-redshift) handled — augmentation,
  redshift or brightness reweighting — and how is the contamination of a photometric
  SN Ia sample propagated into a cosmological fit?
- **M3** (referee, generative models) When GANs, VAEs, normalising flows,
  diffusion or flow-matching models are used to emulate fields, maps or catalogues,
  how is their fidelity validated beyond the power spectrum (bispectrum, one-point
  PDF, peak counts, Minkowski functionals, cross-correlation with the target for a
  conditional model), and which failure modes (mode collapse, memorisation,
  extrapolation in cosmological parameters) should be tested?
- **M4** (analyst, interpretability) How do analyses find out what a network has
  learned — saliency or attribution maps, ablation of inputs, symbolic regression of
  a learned relation or of graph-network messages — and how is a symbolic
  expression validated (out of sample, across simulators) before it is read as
  physics?
- **M5** (referee, learned simulation corrections) How are fast simulations
  corrected or replaced by learning — corrections of COLA-type runs (NECOLA),
  field-level N-body emulators, baryon painting onto dark-matter-only runs — what
  are the input and target pairs, at which scales and statistics are they
  validated, and how is their dependence on cosmology and on the hydrodynamical
  model (IllustrisTNG, SIMBA, Astrid) tested?
- **M6** (analyst, uncertainty and reproducibility) How should a network-based
  cosmological inference quantify and test its uncertainty — deep ensembles,
  Bayesian networks, MC dropout, coverage tests of posteriors (simulation-based
  calibration, TARP, expected coverage) — and what reproducibility practice
  (released weights and training sets, seeds, versioned simulations, blinding)
  should a referee ask for?
- **M7** (control, `neural-density-estimation`) How does one choose between
  neural posterior, likelihood and ratio estimation (NPE, NLE, NRE, and their
  sequential variants) for simulation-based inference on a cosmological summary,
  how many simulations does each need, and how do the prior and the compression
  enter each?
- **M8** (control, `anomaly-detection`) How are anomaly-detection methods
  (autoencoders, isolation forests, density estimators, similarity search) set up on
  survey images or spectra, how is the anomaly score calibrated, and how is the
  false-positive rate controlled when each candidate needs follow-up?

## cosmo-multimessenger

Dossier subtopics: `spectral-sirens` (A1), `gw-lss-cross-correlation` (A2),
`next-generation-siren-forecasts` (A3), `gw-lensing` (A4),
`frb-baryon-distribution` (A5), `frb-hubble-constant` (A6).
Controls: `galaxy-catalogue-dark-sirens` (A7), `modified-gw-propagation` (A8).

- **A1** (referee, spectral sirens) How is H0 or the expansion history inferred
  from features of the source-frame mass spectrum of binary black holes — which
  features (the peak near 35 M_sun, the pair-instability edge, the lower mass gap),
  which population models (power law plus peak, broken power law, non-parametric),
  how selection effects enter — and how are mis-specification and redshift
  evolution of the mass spectrum tested so that they do not bias H0?
- **A2** (analyst, siren × LSS) How is the cross-correlation of GW sources with
  galaxies built — angular or tomographic spectra, the GW bias and the sky
  localisation as a window — what does it need that a galaxy-catalogue dark-siren
  analysis does not (and the reverse), and which measurements or forecasts use it?
- **A3** (referee, forecasts) How are siren forecasts for O5, Einstein Telescope,
  Cosmic Explorer and LISA built — event catalogue from a population model,
  counterpart rates (kilonova, GRB detection), per-event error budget (inclination,
  peculiar velocity, lensing, calibration) — and which assumptions, as the different
  forecasting groups make them, most change the forecast H0 or w0wa precision?
- **A4** (analyst, GW lensing) How does weak lensing scatter siren distances and
  how is it put into the likelihood (a lensing PDF, delensing with galaxy or
  shear maps), and how would strongly lensed GW events be identified (parameter
  overlap, time-delay and magnification priors, Morse phase) and used for
  cosmography, with which false-alarm problems?
- **A5** (referee, FRB baryons) How is the FRB dispersion measure used to locate
  baryons — mapping foreground haloes along localised sightlines, DM–galaxy
  cross-correlation, the scatter of DM_cosmic as a feedback probe — how are host and
  Milky Way halo contributions treated, and which degeneracies with cosmology
  remain?
- **A6** (analyst, FRB H0) How is H0 obtained from FRBs — localised bursts
  through the Macquart relation against survey forward models that include
  unlocalised bursts — how do the host DM distribution, the DM_cosmic scatter, the
  Ω_b h² prior and the survey selection enter, and why do the published values
  differ?
- **A7** (control, `galaxy-catalogue-dark-sirens`) How is the line-of-sight
  redshift prior built from an incomplete galaxy catalogue (GLADE+, DESI) —
  completeness correction (homogeneous or multiplicative), luminosity weighting of
  hosts, photometric against spectroscopic redshifts — and how sensitive is the H0
  posterior to these choices and to the population model, as the LVK pipelines
  implement them?
- **A8** (control, `modified-gw-propagation`) How is the ratio of GW to EM
  luminosity distance parametrised (Ξ0 and n, a running Planck mass), which data
  constrain it (bright sirens, dark and spectral sirens), and how is it degenerate
  with H0 and with population assumptions?

## cosmo-photometry-photoz

Dossier subtopics: `photometric-calibration` (Z1), `chromatic-extinction` (Z2),
`machine-learning-photoz` (Z3), `population-forward-models` (Z4),
`clustering-redshifts-shear-ratio` (Z5), `narrow-many-band-photometry` (Z6).
Controls: `template-fitting` (Z7), `nz-direct-som` (Z8).

- **Z1** (referee, calibration) How is a survey-wide photometric calibration
  built — ubercal from repeated overlapping exposures against a forward global
  calibration with an atmosphere model (FGCM), tied to an absolute scale (CALSPEC,
  Gaia XP synthetic photometry) — and how are the residual zero-point
  non-uniformity and its effect on photo-z and on clustering tested?
- **Z2** (analyst, chromatic effects and extinction) How are chromatic effects
  (bandpass variation across the focal plane and with airmass, SED-dependent
  corrections) and Milky Way extinction (SFD, CSFD, other maps; SED-dependent
  reddening coefficients) handled, how are dust-map errors tested (extragalactic
  contamination of the map, correlation with galaxy density), and how do they
  propagate into photo-z and number densities?
- **Z3** (referee, ML photo-z) How do machine-learning photo-z methods differ
  (nearest neighbours, random forests, neural networks including CNNs on images,
  mixture-density and Gaussian-process methods), how do they produce calibrated p(z)
  and handle an incomplete training set (weighting, augmentation, coverage cuts),
  and how have challenges compared them with template fitting?
- **Z4** (analyst, population forward models) How do hierarchical and population
  forward models infer n(z) — sampling the n(z) histogram jointly with the
  photometry, forward modelling a galaxy population from stellar-population
  synthesis, image simulations — how do they compare with SOM and clustering
  calibration, and which systematics of the population model remain?
- **Z5** (referee, clustering redshifts and shear ratio) How are clustering
  redshifts measured (cross-correlation with a spectroscopic sample in thin bins,
  bias evolution of both samples, magnification) and shear-ratio constraints built
  (lens–source ratios at small scales, intrinsic alignments, baryons), how are they
  combined with SOM n(z) in DES, KiDS and HSC, and what parts of n(z) do they
  constrain?
- **Z6** (analyst, many- and narrow-band) How do many-band and narrow-band
  surveys (COSMOS, PAUS, SPHEREx) reach their photo-z precision — template fitting
  against ML, emission-line treatment, narrow-band zero-points — and what is their
  role as training or calibration samples for broad-band surveys, with which
  limitations (depth, sample variance, area)?
- **Z7** (control, `template-fitting`) How do template-fitting codes (BPZ,
  LePhare, EAZY) differ — template sets, magnitude and type priors, emission lines,
  template error function, zero-point offsets iterated on spectroscopic samples —
  and how is the p(z) they return calibrated?
- **Z8** (control, `nz-direct-som`) How is a SOM calibration of n(z) done (DES
  deep–wide transfer function with Balrog, KiDS gold selection), how are
  spectroscopic incompleteness and sample variance of the calibration fields
  propagated, and how are the mean-redshift uncertainties set?

## cosmo-reionization-21cm

Dossier subtopics: `lya-emitters` (R1), `ionising-photon-budget` (R2),
`eor-inference-modelling` (R3), `eor-cross-correlations` (R4),
`hi-intensity-mapping` (R5), `line-intensity-mapping` (R6).
Controls: `damping-wings` (R7), `global-signal` (R8).

- **R1** (referee, Lyα emitters) How is x_HI inferred from the Lyα fraction among
  Lyman-break galaxies and from LAE luminosity functions — the intrinsic
  equivalent-width distribution assumed after reionisation, the IGM transmission
  from simulated bubbles, the treatment of the ISM, inflows and velocity offsets —
  and how do different modelling choices and the JWST spectroscopic samples lead to
  different x_HI(z)?
- **R2** (analyst, photon budget) How is the ionising-emissivity budget closed —
  UV luminosity function integrated to a limiting magnitude, ξ_ion, f_esc (indirect
  proxies, LyC leakers), clumping factor — how do JWST measurements of ξ_ion change
  it, and how are the competing resolutions (AGN, lower f_esc, faint-galaxy cut-off)
  weighed?
- **R3** (referee, inference) How are 21 cm power-spectrum upper limits turned
  into astrophysical constraints — semi-numerical simulators, emulators, the
  likelihood of an upper limit (Gaussian, one-sided, simulation-based),
  parametrisations (X-ray heating, an excess radio background) — and how are joint
  inferences with τ, UV luminosity functions and the forest built?
- **R4** (analyst, cross-correlations) How are 21 cm × galaxy, × LAE, × other line
  and × kSZ cross-correlations designed — expected sign and scale dependence,
  foreground avoidance in the cross-spectrum, redshift precision required of the
  galaxy tracer — and which measurements or forecasts exist?
- **R5** (referee, HI intensity mapping) How is post-reionisation HI intensity
  mapping done in single-dish (MeerKAT, GBT, FAST, Parkes) against interferometric
  (CHIME, HIRAX, CHORD) mode — foreground cleaning (PCA, FastICA, GPR), the
  signal-loss transfer function and its estimation by mock injection, the amplitude
  Ω_HI b_HI r and its degeneracies, cross-correlation and auto-correlation detections
  and the BAO status?
- **R6** (analyst, line-intensity mapping) How are CO and [CII] intensity-mapping
  data (COMAP, mmIME, CONCERTO, TIME, SPHEREx) analysed — power spectrum against
  voxel intensity distribution, interloper lines (masking, anisotropy, cross),
  stacking on galaxy catalogues — and how are luminosity–halo-mass models
  constrained by them?
- **R7** (control, `damping-wings`) How is a Lyα damping wing towards a z > 7
  quasar modelled — intrinsic-continuum reconstruction, proximity zone, quasar
  lifetime degeneracy — and how do galaxy damping wings from JWST differ in their
  systematics (local DLAs, ISM absorption)?
- **R8** (control, `global-signal`) How is a global 21 cm detection tested —
  foreground model choice, beam chromaticity, ground plane and receiver systematics,
  comparison with SARAS 3 — and what does a referee check when such a detection is
  reported?
