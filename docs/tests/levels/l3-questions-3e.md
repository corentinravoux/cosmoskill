# Level test — third L3 questions, part 3e

Thirty-two specialist questions, eight per skill, for item C of
`docs/plans/2026-10-20-plan.md` ("the domains not yet tested"). With this part every
domain skill has had an L3 test. Written on 2026-10-20 from each skill's
`references/subtopics.tsv` and from the level rule's description of L3 ("how a result is
derived and how to choose between methods"), **before any `SKILL.md` body, reference
file or dossier of the four skills was opened**. What was known when they were written:
the subtopic keys, titles, sources and `files` columns of the four `subtopics.tsv` files,
the file names under `deep/` and `references/`, and the one-line skill descriptions shown
in the skill listing (the `description` field of each `SKILL.md` front matter). Part 3d,
run at the same time by another agent on other skills, has its own file.

Each question is one a practitioner preparing or refereeing an analysis would ask; none
is answered by a single headline number. Per skill, questions 1–6 fall one each on the
six subtopics that have a dossier; questions 7–8 fall on subtopics whose `files` column
lists no dossier, and are controls, where L3 should not help. Questions follow the field
as a whole: where several groups, codes or methods compete, the question names them, not
one group's choice. The id letters L, O, U and Y are not used by the earlier question
files.

For all four skills the six dossiers under `deep/` match, by name, the six rows whose
`files` column lists a dossier; no reassignment was needed.

## cosmo-simulations-mocks

Dossier subtopics: `nbody-codes-convergence` (L1), `halo-finding` (L2),
`hydro-subgrid-calibration` (L3), `fast-mocks` (L4), `light-cones-survey-mocks` (L5),
`constrained-simulations` (L6). Controls: `initial-conditions` (L7),
`neutrino-modified-gravity` (L8).

- **L1** (referee, N-body codes) How do the gravity solvers (PM, tree-PM, FMM, AMR) and
  time-stepping choices of the production codes (for instance GADGET, ABACUS, PKDGRAV,
  RAMSES, HACC, SWIFT) differ, how is per-cent agreement of the matter power spectrum
  between codes demonstrated, and how are mass resolution, force softening and box size
  tested for convergence at a given k and redshift?
- **L2** (analyst, halo finding) How do friends-of-friends, spherical-overdensity and
  phase-space finders (for instance SUBFIND, ROCKSTAR, AHF, CompaSO, HBT+) differ in how
  they identify haloes and subhaloes, how does the mass definition (M_FoF, M200c, Mvir)
  change the mass function and halo bias, and how are merger trees built and their
  failures (lost subhaloes, fly-bys, mass swapping) diagnosed?
- **L3** (referee, hydrodynamical calibration) How are sub-grid feedback parameters
  calibrated in the competing galaxy-formation suites (for instance IllustrisTNG, EAGLE,
  SIMBA, FLAMINGO), which observables are used for the calibration and which are kept for
  validation, what do "strong" and "weak" convergence mean, and how does the calibration
  choice propagate into the cosmological predictions taken from the suite?
- **L4** (analyst, fast mocks) How are approximate methods (COLA, FastPM, EZmocks,
  lognormal and LPT-plus-bias mocks) calibrated against full N-body runs to make
  covariance mocks — which statistics are matched, what fails at small scales or for
  higher-order statistics — and how is the resulting error on the covariance and on the
  parameters assessed, as in the DESI mock challenge?
- **L5** (analyst, light-cones) How is a light-cone built from a periodic box
  (on-the-fly output against snapshot interpolation, box replication and its spurious
  repetition), how are lensing maps made (multiple-plane ray-tracing against the Born
  approximation, shells), and which survey-realism ingredients (footprint, n(z), masks,
  fibre assignment, photo-z) are added and validated?
- **L6** (referee, constrained simulations) How are initial conditions of the local
  Universe constrained — Hoffman–Ribak constrained realisations from peculiar velocities
  (CLUES, HESTIA, Cosmicflows-based runs) against posterior resimulations from
  field-level inference (BORG, CSiBORG, Manticore) — how is agreement with observed
  structures (Virgo, Coma, the Local Group) quantified, and how much cosmic variance
  remains in each approach?
- **L7** (control, `initial-conditions`) How are the starting redshift and the LPT order
  (Zel'dovich, 2LPT, 3LPT) chosen, which transients and discreteness errors does each
  choice leave, and what do fixed-and-paired initial conditions gain and bias for which
  statistics?
- **L8** (control, `neutrino-modified-gravity`) How are massive neutrinos included in
  N-body runs (particles, linear response on a grid, hybrid), which shot-noise and
  initial-velocity problems does each have, and how are modified-gravity simulations
  (f(R), nDGP) solved and compared across codes?

## cosmo-software-ecosystem

Dossier subtopics: `boltzmann-solvers` (O1), `modified-gravity-solvers` (O2),
`theory-facades` (O3), `samplers-frameworks` (O4), `estimator-codes` (O5),
`maintenance-validation` (O6). Controls: `perturbation-theory-codes` (O7),
`lyman-alpha-tools` (O8).

- **O1** (analyst, Boltzmann solvers) How are the precision settings of CAMB and CLASS
  chosen for a given dataset (Stage-IV CMB, CMB lensing, small-scale matter power), at
  what level and on which outputs is the agreement between the two documented, and how
  are the newer differentiable solvers validated against them?
- **O2** (referee, modified-gravity forks) How do EFTCAMB, hi_class, MGCAMB and MGCLASS
  differ in their parametrisation (EFT functions, α_i, μ–Σ), their stability conditions
  and their quasi-static assumptions, what did the 2017 code comparison find, and what
  should a user check when two forks give different spectra for the same model?
- **O3** (analyst, theory façades) When choosing among CCL, cosmoprimo,
  astropy.cosmology, jax-cosmo and CLOE/cloelib (or CosmoLike), what differs in
  parameter inputs (A_s or σ8, h units), neutrino treatment, default non-linear model and
  back-end, how is each façade validated against the Boltzmann code underneath, and which
  pitfalls arise when switching between them?
- **O4** (referee, samplers and frameworks) How do Cobaya, MontePython, CosmoSIS and
  desilike differ in the samplers they offer (Metropolis–Hastings with covariance
  learning and fast–slow splitting, nested samplers such as PolyChord, dynesty or
  nautilus, gradient-based NUTS), which convergence criteria they use, and what does the
  2026 sampler comparison say about which sampler to use for which problem?
- **O5** (analyst, estimator codes) How do pair counters (Corrfunc, pycorr, TreeCorr) and
  FFT power-spectrum codes (pypower, nbodykit) differ in binning, weights (FKP, PIP),
  mass assignment, interlacing and window treatment, how is agreement between them
  tested, and how do pseudo-C_ℓ codes such as NaMaster handle mode coupling and B-mode
  purification?
- **O6** (referee, maintenance and validation) How does one judge whether a cosmology
  code is maintained and validated — test suites, continuous integration, reproduction of
  published results, release practice — which widely used codes are no longer maintained
  and what replaced them, and how should codes and versions be reported in a paper so the
  result is reproducible?
- **O7** (control, `perturbation-theory-codes`) How do velocileptors, PyBird, FOLPS and
  CLASS-PT differ (Eulerian against Lagrangian, IR resummation, bias basis,
  counterterms, stochastic terms), and what did the DESI full-shape code comparison find
  about their agreement and the mapping between their parameters?
- **O8** (control, `lyman-alpha-tools`) How do picca and Vega divide the work in a Lyα
  BAO analysis, how is the distortion matrix computed and validated, and how do the P1D
  emulators (LaCE, ForestFlow, lym1d) differ in training simulations, parameters and
  accuracy?

## cosmo-surveys-facilities

Dossier subtopics: `footprint-tiling-depth` (U1), `cadence-time-domain` (U2),
`requirements-flowdown` (U3), `survey-forecasts` (U4), `cmb-survey-design` (U5),
`cross-survey-coordination` (U6). Controls: `fibre-assignment-completeness` (U7),
`radio-21cm-facilities` (U8).

- **U1** (analyst, footprint and depth) How is the depth-against-area trade decided for
  a wide survey (Euclid Wide Survey, DESI tiling and passes, Rubin wide-fast-deep), how
  are tiling, passes and exposure times adapted to observing conditions (for instance an
  effective-time scheme), and how is depth uniformity measured and fed back into the
  survey plan?
- **U2** (referee, cadence) How is a time-domain cadence designed and optimised — survey
  simulators and metric frameworks, the Rubin Survey Cadence Optimization Committee
  process, rolling cadence, deep drilling fields, the Roman time-domain survey choices —
  and how are competing science cases (SN cosmology, transients, static science) weighed
  against one another?
- **U3** (analyst, requirements flow-down) How are cosmology requirements (a figure of
  merit, a shear multiplicative bias, PSF ellipticity, redshift purity) flowed down to
  instrument and survey specifications, for instance in Euclid compared with Rubin or
  DESI, how is the error budget allocated among subsystems, and how is compliance
  verified before and after launch or first light?
- **U4** (referee, forecasts) How is a survey forecast made — Fisher matrices with
  effective volume and nP, which nuisance parameters and scale cuts are included, which
  figure of merit is used — how are CMB forecasts such as those of Simons Observatory
  built (noise curves, foregrounds, delensing), and how well have earlier forecasts
  matched realised performance?
- **U5** (analyst, CMB survey design) How are detector count, map depth (μK-arcmin),
  beam, sky fraction and aperture traded in the ground and space programmes (Simons
  Observatory, SPT-3G, CMB-S4, LiteBIRD), why are large and small apertures split, and
  how does the choice of sky fraction differ for B-modes against lensing and SZ science?
- **U6** (referee, cross-survey coordination) How are overlapping footprints and joint
  processing planned among Euclid, Rubin, DESI and Roman (joint pixel-level processing,
  ground photometry for Euclid photo-z, spectroscopic calibration samples), what is
  gained over separate analyses, and which practical obstacles (data rights, release
  timing, calibration) limit the coordination?
- **U7** (control, `fibre-assignment-completeness`) How is fibre assignment done in DESI
  compared with PFS and 4MOST (positioner patrol radius, target priorities, passes), what
  completeness results, and how is the incompleteness corrected downstream?
- **U8** (control, `radio-21cm-facilities`) How do interferometric (CHIME, HIRAX, HERA)
  and single-dish (MeerKAT in single-dish mode, SKA-Mid) approaches to 21 cm surveys
  differ in calibration requirements, foreground handling and the scales they reach?

## cosmo-theory-foundations

Dossier subtopics: `sound-horizon` (Y1), `linear-growth` (Y2),
`eft-perturbation-theory` (Y3), `halo-model-nonlinear` (Y4),
`projected-statistics-limber` (Y5), `relativistic-wide-angle` (Y6). Controls:
`flrw-distances` (Y7), `rsd-models` (Y8).

- **Y1** (referee, sound horizon) How are r_s(z_*), r_d, θ_* and θ_MC defined and
  computed — numerical integration in a Boltzmann code against fitting formulae (for
  instance Eisenstein–Hu and later calibrated formulae) — what accuracy does each fitting
  formula reach, and which are safe in a BAO + BBN analysis or beyond ΛCDM (extra N_eff,
  massive neutrinos, early dark energy)?
- **Y2** (analyst, linear growth) How are D(a), f and the growth index γ defined when
  growth is scale-dependent (massive neutrinos, modified gravity), how is fσ8 defined
  (total matter against cold dark matter plus baryons, density against velocity
  divergence), and how do the definitions used by Planck and by eBOSS-like RSD analyses
  differ when a measurement is compared with theory?
- **Y3** (referee, EFTofLSS) How are the perturbation-theory kernels, counterterms and IR
  resummation set up in the EFTofLSS and in Lagrangian perturbation theory, how is the
  time dependence handled (Einstein–de Sitter kernels against exact ΛCDM or beyond-ΛCDM
  kernels), how large is the error of the EdS approximation, and how do renormalisation
  choices differ between implementations?
- **Y4** (analyst, non-linear matter) How do halofit, HMcode (2016, 2020) and the halo
  model compare for the non-linear matter power spectrum — accuracy in k and z, the
  transition between one- and two-halo terms, massive neutrinos — and why did DES Y3 and
  KiDS-Legacy choose different prescriptions?
- **Y5** (referee, Limber) When does the Limber approximation fail (low ℓ, narrow
  kernels, RSD in angular clustering), which non-Limber methods exist and how were they
  compared, how are flat- and curved-sky correlation functions related to C_ℓ, and how
  did DES Y3 handle these choices?
- **Y6** (analyst, relativistic and wide-angle terms) Which relativistic projection
  effects (magnification, Doppler, lensing, evolution bias) enter galaxy clustering on
  large scales, how are magnification and evolution biases measured from the sample, how
  are wide-angle terms in the multipoles modelled (for instance in the BOSS DR12
  analysis), and when do these effects matter for f_NL or for RSD?
- **Y7** (control, `flrw-distances`) How are D_M, D_H, D_V and D_A defined, how is the
  Alcock–Paczynski mapping parametrised (α_∥, α_⊥, α_iso, ε) in DESI DR2 against earlier
  conventions, and which fiducial-cosmology rescalings must be applied when comparing
  results?
- **Y8** (control, `rsd-models`) How do the Kaiser formula, fingers-of-God damping
  (Lorentzian against Gaussian), the TNS model and the Gaussian streaming model differ,
  at which scales each breaks, and how are the Legendre multipoles and Fourier
  conventions normalised?
