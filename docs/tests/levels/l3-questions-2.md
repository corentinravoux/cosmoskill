# Level test — second L3 questions

Forty specialist questions, eight per skill, for item C of
`docs/plans/2026-10-20-plan.md`. Written on 2026-10-20 from each skill's
`references/subtopics.tsv` and from the level rule's description of L3
("how a result is derived and how to choose between methods"), **before any
`SKILL.md` body, reference file or dossier of the five skills was opened**.
What was known when they were written: the subtopic keys, titles, sources
and `files` columns of the five `subtopics.tsv` files, the file names under
`deep/` and `references/`, and the one-line skill descriptions shown in the
skill listing (the `description` field of each `SKILL.md` front matter).

Each question is one a practitioner preparing or refereeing an analysis
would ask; none is answered by a single headline number. Per skill,
questions 1–6 fall one each on the six dossier subtopics; questions 7–8 fall
on subtopics whose `files` column lists no dossier, and are controls, where
L3 should not help. None repeats a pilot question (`l3-questions.md`).

## cosmo-statistics-inference

Dossier subtopics: `likelihood-form` (S1), `covariance-estimation` (S2),
`profile-likelihoods` (S3), `model-comparison` (S4), `tension-metrics` (S5),
`pipeline-validation` (S6). Controls: `goodness-of-fit` (S7), `blinding` (S8).

- **S1** (referee, likelihood form) The analysis uses a Gaussian likelihood
  for band powers down to the lowest multipoles or largest scales. When is
  the Gaussian form inadequate, which alternatives are used (for instance
  Hamimeche–Lewis, offset-lognormal, Wishart or Gamma forms), and how does
  one test whether the Gaussian assumption biases the parameters?
- **S2** (analyst, covariance) Should the covariance be fixed at a fiducial
  cosmology or vary with the parameters in the likelihood; how is the
  fiducial iterated when it is fixed, and what bias does each choice cause?
- **S3** (referee, profile likelihood) How does one decide whether Wilks'
  theorem holds for a given profile likelihood, and when is a Neyman
  construction with simulated (toy) data sets needed instead — how are the
  toys generated and how many are needed?
- **S4** (analyst, model comparison) How is the Bayesian evidence computed
  in practice (nested sampling, Savage–Dickey density ratio, learned
  harmonic mean or other estimators), how does one check its accuracy, and
  how sensitive is a Bayes factor to the prior width of the extra
  parameters?
- **S5** (analyst, tension metrics) When the two data sets are correlated
  (overlapping sky, shared nuisance parameters or calibration), how is a
  tension metric computed, which metrics allow for the correlation, and how
  is the shared-parameter subspace chosen?
- **S6** (referee, pipeline validation) How is the inference pipeline
  validated on synthetic data before unblinding — noiseless data vectors,
  contaminated data vectors, mock ensembles — and which pass criterion (a
  fraction of σ in which parameters) is used, and how is it set?
- **S7** (control, `goodness-of-fit`) How is the effective number of degrees
  of freedom computed for a χ² goodness-of-fit test when nuisance parameters
  have informative priors, and which posterior predictive tests are used
  instead of, or with, the χ² p-value?
- **S8** (control, `blinding`) Catalogue-level, data-vector-level or
  parameter-level blinding: how does one choose, and which tests and
  criteria are fixed before unblinding?

## cosmo-cmb

Dossier subtopics: `beams-calibration-polarisation` (C1),
`high-ell-likelihoods` (C2), `component-separation` (C3),
`low-ell-polarisation-tau` (C4), `lensing-reconstruction` (C5),
`damping-tail-light-relics` (C6). Controls: `maps-and-band-powers` (C7),
`lensing-amplitude-anomalies` (C8).

- **C1** (referee, beams and calibration) How are the beam window functions
  and their uncertainties propagated into the power-spectrum likelihood
  (beam eigenmodes, marginalisation), and how are the absolute calibration
  and the polarisation efficiency determined and marginalised?
- **C2** (analyst, high-ℓ likelihood) Plik, CamSpec or HiLLiPoP: how do they
  differ in masks, choice of cross-spectra, foreground model and TE/EE
  treatment, and how should one choose between them and read the parameter
  shifts they produce?
- **C3** (analyst, component separation) How does one choose between
  ILC/NILC, SMICA, SEVEM and Commander for a given use (lensing, low-ℓ
  polarisation, B modes, cross-correlation), and how are foreground
  residuals in the cleaned map quantified?
- **C4** (referee, τ) How is τ measured from low-ℓ EE — pixel-based
  likelihood, simulation-based likelihood from cross-spectra — which
  systematics dominate, and how should a τ prior be chosen when Planck
  large-scale polarisation is not used?
- **C5** (analyst, lensing) How are the N0, N1 and mean-field biases computed
  and subtracted (realisation-dependent N0, simulations), and how is
  extragalactic-foreground contamination handled (bias hardening, profile
  hardening, shear-only estimators)?
- **C6** (referee, light relics) How are N_eff and Y_P constrained from the
  damping tail, what degeneracies are involved, how does one choose between
  free Y_P and BBN-consistent Y_P, and what limits a forecast for the next
  experiments?
- **C7** (control, `maps-and-band-powers`) In a ground-based pseudo-C_ℓ
  analysis, how is the transfer function of the time-domain filtering
  estimated and corrected, and how is the mode-coupling matrix handled?
- **C8** (control, `lensing-amplitude-anomalies`) How is A_L defined and
  fitted, and how does one tell a real lensing excess from a fluctuation or
  from the choice of likelihood; how should a paper report it?

## cosmo-weak-lensing

Dossier subtopics: `two-point-statistics` (W1), `shear-calibration` (W2),
`intrinsic-alignments` (W3), `baryonic-feedback` (W4),
`blinding-consistency` (W5), `ggl-3x2pt` (W6). Controls:
`redshift-calibration` (W7), `psf-modelling` (W8).

- **W1** (analyst, two-point statistics) ξ±, COSEBIs, band powers or
  pseudo-C_ℓ: how does one choose, how does each separate E and B modes and
  apply scale cuts, and how are results from several statistics on the
  same data compared?
- **W2** (referee, shear calibration) Metacalibration or metadetection
  against lensfit with image-simulation calibration: how is the
  multiplicative bias m determined, how does blending enter (including its
  redshift dependence), and what prior is put on m in the likelihood?
- **W3** (analyst, intrinsic alignments) NLA or TATT (or a halo-model or
  mass-dependent model): how does one choose, which priors are taken from
  direct measurements, and how does the choice project onto S8?
- **W4** (referee, baryons) Scale cuts or baryon modelling (HMcode with
  log T_AGN, baryonification, external gas priors): how are scale cuts
  derived (contaminated data vectors from hydrodynamical simulations, a
  Δχ² or parameter-shift threshold), and how large are the S8 shifts
  between the choices?
- **W5** (referee, consistency) How are the internal-consistency tests (by
  redshift bin, statistic, sky region) designed — which metric, which
  threshold, how correlated subsamples are handled — and what is fixed
  before unblinding?
- **W6** (analyst, galaxy–galaxy lensing) How are the point-mass
  contribution and the non-local small scales handled in galaxy–galaxy
  lensing (analytic marginalisation, annular statistics), and how are lens
  magnification and non-linear bias included in a 3×2pt analysis?
- **W7** (control, `redshift-calibration`) SOM, clustering redshifts or
  shear ratio: how does each calibrate n(z), how are they combined, and
  what prior on the mean shifts results?
- **W8** (control, `psf-modelling`) How are PSF leakage and PSF modelling
  errors measured (ρ and τ statistics) and propagated into the
  likelihood, and what is the pass criterion for B modes?

## cosmo-supernovae

Dossier subtopics: `photometric-calibration` (N1), `light-curve-models` (N2),
`dust-intrinsic-scatter` (N3), `selection-bias-corrections` (N4),
`covariance-likelihood-blinding` (N5), `stage-iv-photometric-samples` (N6).
Controls: `standardisation-host` (N7), `photometric-classification` (N8).

- **N1** (referee, calibration) How is the cross-calibration of
  heterogeneous SN samples done (Supercal, Fragilistic, Dovekie; CALSPEC
  against white-dwarf standards), and how is the calibration covariance
  built and propagated into w?
- **N2** (analyst, light-curve model) SALT2, SALT3 or BayeSN: how does one
  choose, how is the model trained and its training uncertainty propagated,
  and what wavelength and phase range is valid?
- **N3** (referee, dust and scatter) G10, C11, BS21 or P23/Dust2Dust
  intrinsic-scatter models: how does each enter the bias correction, and
  how does the choice change the host-mass step and w?
- **N4** (analyst, selection) BBC with survey simulations or a forward-
  modelled selection (UNITY): how does each correct selection bias, which
  simulations does each need, and how is the selection model validated?
- **N5** (referee, covariance and blinding) How is the systematic
  covariance built (one shift per systematic, scaling), how is the
  likelihood marginalised over the absolute magnitude, and how were the
  recent samples blinded?
- **N6** (analyst, Stage IV) For a fully photometric LSST sample (host
  photometric redshifts, photometric classification), how are photo-z
  errors and contamination propagated into the cosmology, and what
  requirements follow?
- **N7** (control, `standardisation-host`) How is the host-mass step fitted
  (location, step or sigmoid, local or global host property), and is it
  applied before or after the bias corrections?
- **N8** (control, `photometric-classification`) How does a BEAMS-type
  marginalisation over contamination work, how are classifier
  probabilities calibrated, and how is the contamination systematic
  estimated?

## cosmo-bbn

Dossier subtopics: `nuclear-reaction-rates` (B1), `bbn-codes` (B2),
`deuterium` (B3), `helium-4` (B4), `baryon-density` (B5),
`neff-new-physics` (B6). Controls: `neutron-lifetime` (B7),
`lithium-problem` (B8). (`standard-bbn-theory` also lists
`deep/bbn-codes.md` and was not used as a control.)

- **B1** (analyst, rates) How are the d(p,γ)³He and d+d rates evaluated
  (ab initio theory against data-driven or Bayesian fits of laboratory
  data), and how does the choice change the predicted D/H and the inferred
  Ω_b h²?
- **B2** (referee, codes) PRIMAT, PArthENoPE, AlterBBN, PRyMordial, LINX: how
  do they differ (network, rate compilation, weak-rate corrections,
  neutrino decoupling), and how large are the code-to-code differences in
  D/H and Y_P?
- **B3** (referee, deuterium) How is D/H measured from a quasar absorber —
  choice of systems, velocity-structure model, error floor — and how are
  the measurements combined (weighted mean, test of the scatter)?
- **B4** (analyst, helium) How is Y_P derived from H II regions — which
  emission lines, the role of He I 10830, which physical parameters are
  fitted, the regression to zero metallicity — and why do the groups
  disagree?
- **B5** (analyst, BBN prior) How is a BBN prior on Ω_b h² built for a BAO
  analysis (which D/H, which rates, which code), and how does the choice
  change the result of BAO + BBN?
- **B6** (referee, N_eff) How is N_eff constrained from BBN alone and from
  BBN + CMB — which observables, which degeneracy with Ω_b h², and how are
  Y_P and D/H combined?
- **B7** (control, `neutron-lifetime`) How does one choose between the
  bottle and the beam neutron lifetime in a BBN calculation, and how does
  the choice propagate to Y_P?
- **B8** (control, `lithium-problem`) How are Spite-plateau stars analysed
  for the primordial lithium abundance (depletion models, 3D NLTE), and how
  does one decide whether the lithium problem is astrophysical or nuclear?
