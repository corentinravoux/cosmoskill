# Level test — third L3 questions, part 3c

Thirty-two specialist questions, eight per skill, for item C of
`docs/plans/2026-10-20-plan.md` ("the domains not yet tested"), part 3c. Written on
2026-10-20 from each skill's `references/subtopics.tsv` and from the level rule's
description of L3 ("how a result is derived and how to choose between methods"),
**before any `SKILL.md` body, reference file or dossier of the four skills was
opened**. What was known when they were written: the subtopic keys, titles, sources
and `files` columns of the four `subtopics.tsv` files, the file names under `deep/`
and `references/`, and the one-line skill descriptions shown in the skill listing
(the `description` field of each `SKILL.md` front matter). Parts 3a and 3b
(`l3-questions-3a.md`, `l3-questions-3b.md`) cover other skills; their question ids
use the letters B, C, D, F, G, H, I, K, N, S, T, V, W, X, so this part uses Q, P, E
and J. Other parts run at the same time and write their own files.

Each question is one a practitioner preparing or refereeing an analysis would ask;
none is answered by a single headline number. Per skill, questions 1–6 fall one each
on the six subtopics that have a dossier; questions 7–8 fall on subtopics whose
`files` column lists no dossier, and are controls, where L3 should not help.
Questions follow the field as a whole: where several groups or methods compete, the
question names them, not one group's choice. None repeats a question of
`l3-questions.md`, `l3-questions-2.md`, `l3-questions-3a.md` or `l3-questions-3b.md`.

## cosmo-cosmic-web

Dossier subtopics: `web-classification` (Q1), `environment` (Q2), `spin-alignments`
(Q3), `filament-gas` (Q4), `missing-baryons` (Q5), `protoclusters-superclusters` (Q6).
Controls: `web-statistics` (Q7), `reconstructions` (Q8).

- **Q1** (referee, web classification) How do the main finder families differ in
  what they take as input and how they assign a web class — Hessian of the density or
  of the shear (T-web, V-web, with their eigenvalue threshold), multiscale (NEXUS,
  MMF), topological (DisPerSE, persistence cut), stochastic (Bisous), phase-space
  (ORIGAMI) — which free parameters drive the mass and volume fractions, and how
  should a paper justify its choice of finder and threshold when it applies one to a
  sparse galaxy sample?
- **Q2** (analyst, environment) How does one measure a dependence of galaxy
  properties (colour, star formation, morphology, stellar mass) on web environment —
  distance to the nearest filament or node, web class, tidal anisotropy — while
  separating it from the dependence on local density and halo mass, and what do the
  GAMA, SDSS and DESI analyses conclude about whether any residual web effect
  survives that control?
- **Q3** (referee, spin alignments) How is a spin–filament alignment measured for
  haloes in simulations and for galaxies in integral-field surveys (SAMI, MaNGA) or
  imaging (SDSS) — spin proxy, filament finder, the cosine distribution and its
  null — how is the spin-flip mass defined and measured, and why do different studies
  disagree on the sign or the transition mass?
- **Q4** (analyst, filament gas) How is gas in filaments or cluster bridges detected
  in tSZ (Planck, ACT) stacks, in X-ray (eROSITA) and in radio — how are filaments
  selected for stacking, how is the cluster and halo contribution removed, how are
  the density and temperature inferred — and what limits the comparison of these
  detections with simulations?
- **Q5** (referee, missing baryons) How is the low-redshift baryon census closed —
  which phases are counted by which tracer (Lyα forest, O VI and O VII absorbers,
  tSZ and kSZ, X-ray emission, FRB dispersion measures) — how is the FRB DM–z
  relation turned into a baryon fraction, including the host and Milky Way
  contributions and the cosmic scatter, and where is double counting or model
  dependence most likely?
- **Q6** (analyst, protoclusters and superclusters) How are protoclusters found at
  z > 2 (galaxy overdensities in HSC or narrow-band surveys, spectroscopic LATIS
  maps, Lyα tomography) and superclusters defined at low redshift (luminosity-density
  thresholds, basins of attraction from velocities), how is a protocluster's z = 0
  mass or a supercluster's fate inferred, and what are the purity and completeness
  issues?
- **Q7** (control, `web-statistics`) How are mass and volume fractions in nodes,
  filaments, walls and voids, and the connectivity of nodes, computed and compared
  between simulations and observations, and how do they evolve with redshift and
  smoothing scale?
- **Q8** (control, `reconstructions`) How is the web reconstructed from a galaxy
  redshift survey (2M++), from peculiar velocities (Cosmicflows) and from the Lyα
  forest (CLAMATO, LATIS), and how do the reconstruction noise and its smoothing
  propagate into the web classification drawn from it?

## cosmo-data-pipelines

Dossier subtopics: `extraction-sky` (P1), `redshift-fitting` (P2), `image-detrending`
(P3), `cmb-mapmaking` (P4), `lss-catalogues` (P5), `source-injection` (P6). Controls:
`psf-modelling` (P7), `deblending-coaddition` (P8).

- **P1** (referee, extraction and sky) How are fibre spectra extracted — boxcar,
  optimal extraction, spectro-perfectionism with its resolution matrix — how are flux
  calibration and sky subtraction done in DESI, BOSS/eBOSS and 4MOST or WEAVE-type
  pipelines, and which residuals (sky lines, throughput variations, cross-talk) reach
  the Lyα forest or the emission-line redshifts?
- **P2** (analyst, redshift fitting) How do template fitters (Redrock, the BOSS
  idlspec1d `spZbest`) and their afterburners (QuasarNET, the MgII afterburner) decide
  a redshift and a class, how are redshift success and catastrophic failures
  quantified — visual inspection, repeat observations, ΔΧ² cuts — and how do the
  failure rates depend on tracer and depth?
- **P3** (referee, image detrending) What instrument-signature removal steps
  (bias, overscan, crosstalk, nonlinearity, flat field, fringing) and sensor effects
  (brighter-fatter, tree rings, edge distortions) are corrected in DES, HSC and Rubin
  pipelines, how is the brighter-fatter correction derived and validated, and how is
  the astrometric solution calibrated against Gaia?
- **P4** (analyst, CMB map-making) How do maximum-likelihood, destriping and
  filter-and-bin map-makers differ (Planck HFI and LFI, ACT, SPT, Simons Observatory),
  how are the time-ordered data filtered and flagged, how is the resulting transfer
  function or mode loss measured and corrected, and what does each choice cost in
  bias or noise on large scales?
- **P5** (referee, LSS catalogues) How is a clustering catalogue built — footprint
  and veto masks, randoms carrying the completeness, redshift-failure and
  fibre-assignment weights, imaging-systematics weights by linear regression, neural
  networks (SYSNet) or random forests — in DESI, eBOSS and DES, and how does one test
  that the weights neither leave residual systematics nor remove signal?
- **P6** (analyst, source injection) How do Balrog (DES) and Obiwan (Legacy
  Surveys) inject artificial sources into real images, what is the injected
  population drawn from, which quantities are measured from the injections (detection
  completeness, photometric bias, selection transfer function, n(z) for weak lensing),
  and what limits them as a model of the real selection?
- **P7** (control, `psf-modelling`) How are PSF models built and validated in
  imaging pipelines (PSFEx, Piff, the HSC and Euclid models) — interpolation across
  the focal plane, chromatic effects, ρ-statistics — and how do PSF residuals
  propagate into shear and photometry?
- **P8** (control, `deblending-coaddition`) How do deblenders (SDSS, SCARLET, the
  Rubin and HSC implementations) separate overlapping sources, how does co-addition
  choose between weighted means and PSF-homogenised stacks, and how are blending
  biases measured?

## cosmo-early-universe-exotica

Dossier subtopics: `sgwb-pta` (E1), `phase-transitions` (E2), `cosmic-defects` (E3),
`primordial-black-holes` (E4), `scalar-induced-gw` (E5), `spectral-distortions` (E6).
Controls: `early-dark-energy` (E7), `energy-injection` (E8).

- **E1** (referee, PTA background) How is evidence for a gravitational-wave
  background built from pulsar-timing data — common-spectrum process, Hellings–Downs
  correlation, Bayes factors and frequentist detection statistics, noise models per
  pulsar — how do NANOGrav, EPTA/InPTA, PPTA, CPTA and MPTA differ in their noise
  modelling and significance, and how is the SMBHB interpretation tested against a
  cosmological one?
- **E2** (analyst, phase transitions) How is the gravitational-wave spectrum of a
  first-order phase transition computed from the transition parameters (α, β/H,
  wall velocity, temperature) — sound waves, bubble collisions, turbulence, with
  simulation-calibrated templates — and how large are the template uncertainties
  when fitting PTA or forecasting LISA data?
- **E3** (referee, cosmic strings) How are limits on the string tension Gμ derived
  from the CMB (Planck), from LVK stochastic and burst searches and from PTA data,
  how do they depend on the loop-distribution model (Nambu–Goto simulations, the
  BOS and LRS models, field-theory strings) and on the string type (metastable,
  superstrings), and why can the limits differ by orders of magnitude?
- **E4** (analyst, primordial black holes) How are PBH abundance limits derived
  from microlensing (HSC, OGLE, EROS, MACHO), from LVK merger rates and sub-solar
  searches, and from accretion onto PBHs in the CMB, which assumptions (mass
  function, clustering, finite-source effects, accretion geometry) move each limit,
  and how should a referee treat the claimed OGLE excess?
- **E5** (referee, scalar-induced GWs) How is the scalar-induced GW spectrum computed
  from an enhanced curvature power spectrum — kernel, gauge choice, non-Gaussianity,
  equation of state during reentry — how does a fit of the PTA signal with SIGWs
  connect to PBH overproduction, and which treatment choices decide whether the fit
  is viable?
- **E6** (analyst, spectral distortions) How are μ and y limits derived from
  COBE/FIRAS and its reanalyses — calibration, foreground model, monopole
  subtraction — how is the distortion of a given energy-injection history computed
  (Green's functions, CosmoTherm), and what limits PIXIE-type or balloon forecasts?
- **E7** (control, `early-dark-energy`) How is an early-dark-energy fit set up — the
  axion-like potential, f_EDE and z_c, priors and the prior-volume effects of
  profile against marginal posteriors — and how do Planck, ACT DR6 and SPT-3G data
  change the preference for it?
- **E8** (control, `energy-injection`) How is the CMB limit on dark-matter
  annihilation p_ann derived — energy deposition efficiency f_eff(z), DarkHistory or
  principal components — and how does it translate into a cross-section limit as a
  function of mass and channel?

## cosmo-galaxy-halo-connection

Dossier subtopics: `profiles-concentration` (J1), `hod-clf` (J2),
`abundance-matching-shmr` (J3), `empirical-sam-hydro` (J4), `assembly-bias` (J5),
`satellites` (J6). Controls: `lensing-clustering` (J7), `mass-function-bias` (J8).

- **J1** (referee, profiles and concentration) Which concentration–mass relations
  are in use (Duffy, Diemer–Kravtsov or Diemer–Joyce, Ludlow, Child), how do they
  differ in definition, fitting method and halo sample, how does the choice and its
  scatter enter a halo-model or lensing analysis, and how do baryons modify the
  profile in hydrodynamical simulations?
- **J2** (analyst, HOD per tracer) How do the HOD parametrisations used for LRG,
  ELG, QSO and BGS samples differ (Zheng-type, Gaussian or asymmetric central term
  for ELGs, satellite conformity), how are they fitted to the projected clustering
  and number density with emulators or direct mock population (AbacusHOD, other
  frameworks), and how does an HOD relate to a conditional luminosity function?
- **J3** (referee, abundance matching and SHMR) How is subhalo abundance matching
  set up — which halo property (M_peak, V_peak, V_max), how the scatter is
  implemented and constrained, how incompleteness and orphans are handled — and how
  do the stellar-to-halo mass relations from abundance matching, lensing (HSC, DES,
  COSMOS) and clustering compare, including the high-mass slope and scatter?
- **J4** (analyst, empirical, semi-analytic and hydro) How do empirical models
  (UniverseMachine, EMERGE), semi-analytic models (Galacticus, SAGE, L-Galaxies) and
  hydrodynamical simulations (IllustrisTNG, EAGLE, FLAMINGO) differ in what they
  calibrate on and what they predict for the galaxy–halo connection, and when is
  each the right choice for building mocks or testing an HOD?
- **J5** (referee, assembly bias) How is galaxy assembly bias defined and
  distinguished from halo assembly bias, how is it parametrised in decorated HODs or
  secondary-property SHAM, which observational detections (cluster concentration,
  conformity, split clustering) survive tests for projection and selection effects,
  and how much does it bias a cosmological fit if ignored?
- **J6** (analyst, satellites) How are satellite fractions and velocity bias
  measured — group catalogues (Yang, Tinker), satellite kinematics, small-scale
  redshift-space clustering — how does a group finder's purity and completeness
  propagate into the measured satellite fraction, and how does velocity bias enter
  RSD fits on small scales?
- **J7** (control, `lensing-clustering`) How is "lensing is low" defined — which
  clustering and lensing measurements on which scales, with which HOD — what
  explanations (baryonic feedback, assembly bias, cosmology, systematics) are
  proposed, and how do DES, KiDS, HSC and DESI analyses differ on its size?
- **J8** (control, `mass-function-bias`) How are halo mass functions and halo bias
  calibrated (Tinker, emulators such as Aemulus or the Dark Emulator), how do they
  depend on the halo definition, and how is their uncertainty propagated into
  cluster counts or galaxy bias priors?
