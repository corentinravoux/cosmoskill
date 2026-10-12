# Physics and methods — cosmological simulations and mocks

Scope: the numerical methods behind simulations and mock catalogues used in survey cosmology, each with its reference paper.
Snapshot: 2026-10-07

Citation years in this skill are arXiv submission years, as in `sources.tsv`; the journal year is often one later.

## 1. N-body methods and codes

The reference review of collisionless simulations is Angulo & Hahn 2021 (arXiv:2112.05165). It covers the equations and their link to general relativity, the discretisation of phase space (N-body, Lagrangian submanifold, Schrödinger–Poisson), force calculation (direct summation, mesh, tree), initial conditions, extensions (baryons, neutrinos, primordial non-Gaussianity, modified gravity), and the path to observables (structure finding, emulators, light-cones). Read its section list before writing a methods paragraph.

A gravity-only simulation samples the cold-matter phase-space sheet with N particles of mass m_p = Ω_m ρ_crit L³ / N, softens the two-body force below a length ε, and integrates with a symplectic (kick–drift–kick) scheme. The codes differ in how they compute the force.

| Code | Force solver | Stated property | Reference |
|---|---|---|---|
| GADGET-4 | TreePM, with a momentum-conserving fast multipole method (FMM) as an alternative; two SPH flavours; 2LPT initial-condition generator built in | public release with on-the-fly group finding and merger trees | Springel et al. 2020, arXiv:2010.03567 |
| PKDGRAV3 | FMM with individual adaptive time steps, on GPU nodes | 2 trillion particles to z = 0 in under 80 h on 4000+ GPU nodes of Piz Daint [src] | Potter et al. 2016, arXiv:1609.08621 |
| Abacus | static multipole mesh; exact split into near field (direct 1/r² sum) and far field (convolution over multipoles) | median fractional force error 10⁻⁵; 70 million particle updates per second per Summit node [src] | Garrison et al. 2021, arXiv:2110.11392 |
| SWIFT | FMM coupled to a particle mesh for periodic volumes; task-based parallelism; several SPH flavours; particle neutrinos | open source; weak scaling shown with about 300 billion particles [src] | Schaller et al. 2023, arXiv:2305.13380 |
| HACC | framework designed for many-core and accelerated supercomputers (solver details not read) | ran Outer Rim, Last Journey and Frontier-E (see surveys file) | Heitmann et al. 2019, arXiv:1904.11970 |
| GINKAKU | TreePM on the FDPS framework, with linear-response source terms in the N-body gauge for neutrinos, radiation and clustering dark energy | code-to-code differences in the non-linear P(k) against GADGET, PKDGRAV3 and RAMSES can be reduced below about 1% by tuning accuracy parameters [src] | Nishimichi et al. 2026, arXiv:2605.28581 |

The GADGET-4 paper states that the code offers both a classic entropy-conserving SPH and a pressure-based SPH (arXiv:2010.03567). The 2026 code releases found by the date-sorted search are GPU-native: GINKAKU (above), gevolution 2.0 and the differentiable FMM code JZ-FMM appeared between May and September 2026; only GINKAKU was read in full and is cited here.

**Variance suppression.** "Fixed and paired" simulations fix the initial mode amplitudes to the ensemble mean and run a second box with opposite phases; a fixed pair can be as precise on non-linear scales as an average over 50 traditional simulations, for P(k), the redshift-space multipoles, the halo mass function and the reduced bispectrum at z = 1 [src] (Angulo & Pontzen 2016, arXiv:1603.05253). The UNIT project found the two- and three-point statistics unbiased, the variance of two-point statistics greatly reduced, and the variance of three-point statistics not significantly reduced [src] (Chuang et al. 2018, arXiv:1811.02111). A fixed-amplitude box therefore cannot be used to estimate a covariance. Zel'dovich control variates are the other variance-reduction technique in production: Aemulus ν reports effective-volume gains of 10 to 10⁵ depending on the statistic [src] (DeRose et al. 2023, arXiv:2303.09762).

## 2. Initial conditions

Initial conditions displace particles from a grid or glass with Lagrangian perturbation theory (LPT) at a starting redshift z_i. Three papers define current practice.

- Crocce, Pueblas & Scoccimarro 2006 (arXiv:astro-ph/0606505): Zel'dovich (1LPT) initial conditions excite long-lived transients. Started at z_i = 49, they underestimate the non-linear power spectrum by about 2, 4 and 8% at z = 0, 1 and 3, and the halo mass function by 5% at 10¹⁵ M_⊙/h at z = 0 [src]. 2LPT became the standard after this paper.
- Hahn & Abel 2011 (arXiv:1103.6031), the MUSIC code: multi-scale ("zoom") initial conditions by real-space convolution of white noise with the transfer function and a multigrid Poisson solver; RMS relative errors of order 10⁻⁴ on displacements and velocities in the refined region [src]. This is the reference for zoom-in initial conditions, including those used to resimulate a region of a constrained realisation.
- Michaux et al. 2020 (arXiv:2008.09588): with 3LPT, truncation errors are small enough to start as late as z = 12 at the resolution studied; late starts suppress particle-discreteness errors, which behave as decaying modes amplified by early starts. Late-start 3LPT agrees with the continuum fluid limit within 1% for the power spectrum and bispectrum at z = 0 up to the particle Nyquist wavenumber, k about 3 h/Mpc in their runs [src]. The recommendation is to start as late as possible with 3LPT, the opposite of the older "start early" habit.

Baryons and dark matter have different transfer functions; MUSIC generalises to two-component initial conditions and recommends the local Lagrangian approximation for the initial baryon density on mesh codes (arXiv:1103.6031). Suites that include neutrinos, radiation or dark-energy perturbations at linear order work in the N-body gauge (EuclidEmulator2, arXiv:2010.11288; GINKAKU, arXiv:2605.28581), so that Newtonian particle positions can be read in a relativistic framework.

Two flagship runs show how far practice is spread. FLAMINGO uses multi-fluid 3LPT initial conditions (monofonIC, modified for massive neutrinos) at z = 31, chosen "as late as possible to limit discreteness errors", in the N-body gauge, with partially fixed amplitudes (modes with (kL)² < 1025 set to the mean variance) and phases taken from Panphasia so that zoom resimulations are possible [src] (arXiv:2306.04024, section 2.4). Euclid Flagship 2 uses 1LPT at z = 99 [src] (arXiv:2405.13495, section 2.1).

## 3. Hydrodynamics and sub-grid models

Reviews: Vogelsberger et al. 2019 (arXiv:1909.07976) for methodology; Crain & van de Voort 2023 (arXiv:2309.17075) for what the galaxy-formation suites get right and where they disagree; Chisari et al. 2019 (arXiv:1905.06082) for the consequences for survey cosmology.

**Hydrodynamic solvers in the suites cited here.** Moving mesh (AREPO: IllustrisTNG, MillenniumTNG, part of CAMELS; arXiv:1703.02970, arXiv:2210.10060, arXiv:2010.00619); smoothed particle hydrodynamics (implemented in GADGET-4 and SWIFT, arXiv:2010.03567, arXiv:2305.13380; FLAMINGO runs on SWIFT, arXiv:2306.04024 section 2.1); meshless finite mass (GIZMO: SIMBA and part of CAMELS; arXiv:1901.10203, arXiv:2010.00619); Eulerian finite-volume grid for the intergalactic medium (Nyx, section 4); adaptive mesh refinement (RAMSES, section 4). The solvers of EAGLE, BAHAMAS and OWLS were not read at source.

**Sub-grid models.** Star formation, stellar evolution and enrichment, radiative cooling, stellar feedback, black-hole seeding, growth and feedback all act below the resolution and are implemented as parametrised recipes. Three statements from the reviews and suite papers set the level of trust:

1. The feedback efficiencies cannot be predicted from first principles and are calibrated. EAGLE calibrates to the z about 0 galaxy stellar mass function, the black-hole mass relation and galaxy sizes, and reproduces the mass function to within about 0.2 dex over 10⁸ < M_*/M_⊙ < 10¹¹ [src] (Schaye et al. 2014, arXiv:1407.7040).
2. Similar galaxy populations emerge from dissimilar feedback implementations, which predict markedly different gas flows into and out of haloes; circumgalactic and intragroup gas is where the suites differ [src] (arXiv:2309.17075).
3. For large-scale-structure cosmology the calibration target must include the gas content of groups and clusters, because that is what sets the matter power spectrum. BAHAMAS calibrates stellar and AGN feedback to the present-day stellar mass function and the hot gas mass fractions of groups and clusters (McCarthy et al. 2016, arXiv:1603.02702). FLAMINGO does the same with Gaussian-process emulators trained on Latin hypercubes of 32 small-volume runs, separately at three resolutions spanning a factor of 64 in particle mass, and defines its model variations by shifts of the calibration data rather than by sub-grid parameter values [src] (Schaye et al. 2023, arXiv:2306.04024; Kugel et al. 2023, arXiv:2306.05492).

**AGN feedback implementations named in the abstracts read.** EAGLE: thermal energy injection without switching off cooling (arXiv:1407.7040). IllustrisTNG: multi-mode black-hole feedback with a new kinetic mode at low accretion rates, revised galactic winds, and magnetohydrodynamics (Pillepich et al. 2017, arXiv:1703.02970). SIMBA: kinetic bipolar outflows of about 10³ km/s at high Eddington ratio rising to about 8000 km/s below 2%, plus X-ray energy; torque-limited accretion from cold gas (Davé et al. 2019, arXiv:1901.10203). FLAMINGO: thermal by default, collimated jets as an alternative (arXiv:2306.04024).

**Baryonic correction without hydrodynamics.**

| Method | Idea | Stated accuracy | Reference |
|---|---|---|---|
| Baryonic correction model ("baryonification") | displace particles of a gravity-only run so that each halo follows a profile made of bound gas, ejected gas, stars and relaxed dark matter; the key quantities are the ejected gas fraction and the ejection radius | cluster X-ray and SZ data implied suppression above k about 0.5 h/Mpc with a maximum of 10–25% around k about 2 h/Mpc [src] | Schneider & Teyssier 2015, arXiv:1510.06034 |
| Baryonification, 2025 version | particles split into dark-matter and baryon parts; gas pressure and temperature assigned; validated on FLAMINGO and TNG | reproduces the hydrodynamical P(k) suppression to 2% up to k = 5 h/Mpc redshift by redshift; a 2+1-parameter version to better than 2.5% [src] | Schneider et al. 2025, arXiv:2507.07892 |
| BACCO baryon emulator | neural network on more than 50,000 baryonified spectra in 15 dimensions | 1–2% for 0.01 < k < 5 h/Mpc, 0 < z < 1.5, also against 74 hydrodynamical simulations; one parameter, M_c, suffices at a given epoch [src] | Aricò et al. 2020, arXiv:2011.15018 |
| HMcode-2020 | augmented halo model; six-parameter gas-expulsion model, or a one-parameter version | gravity-only spectra: RMS error 2.5% for k < 10 h/Mpc, z < 2, never above 16%; feedback response matched to < 1% for z < 1, k < 20 h/Mpc [src] | Mead et al. 2020, arXiv:2009.01858 |
| SP(k) | fit to the 400-run ANTILLES suite; input is the mean halo baryon fraction | approaching the percent level for k ≲ 10 h/Mpc, z ≤ 3; the effect is driven by haloes of 10¹³–10¹⁴ M_⊙ [src] | Salcido et al. 2023, arXiv:2305.09710 |
| van Daalen et al. model | empirical relation from 92 spectra of OWLS, cosmo-OWLS and BAHAMAS | 1% for k < 1 h/Mpc at z = 0 given only the mean baryon fraction of groups [src] | van Daalen et al. 2019, arXiv:1906.00968 |
| FLAMINGO response emulator | Gaussian process over the FLAMINGO variations | better than 1% to k = 10 h/Mpc and z = 3 for the FLAMINGO models [src] | Schaller et al. 2024, arXiv:2410.17109 |

These accuracies are all statements about reproducing simulations, not about the real Universe. Which point of the model space nature occupies is the open question (see `open-questions.md` §1.1), and its consequences for S8 are treated in `cosmo-weak-lensing` and `cosmo-cmb-lss-cross-correlations`.

## 4. Hydrodynamical simulations for the Lyα forest

The forest at 2 < z < 5 comes from gas near the mean density, so the simulation problem differs from galaxy formation: uniform resolution of low-density gas matters more than sub-grid physics, and the thermal and ionisation history of the intergalactic medium replaces feedback as the main nuisance. The analyses themselves (P1D, P3D, BAO, thermal state, dark-matter limits) are in `cosmo-lyman-alpha`.

**Codes and the reason each is used.**

| Code | Method | Why it matters for the forest | Reference |
|---|---|---|---|
| Nyx | particle-mesh gravity; finite-volume Eulerian hydrodynamics on a grid | low-density gas, where the forest forms, is not under-sampled as it is by SPH particles (arXiv:2207.05023); 20 kpc/h cells give 1% convergence of flux statistics to k = 10 h/Mpc, and L > 40 Mpc/h suppresses missing-mode errors below 1% [src] | Lukić et al. 2014, arXiv:1406.6361 |
| CRK-HACC | Tree-PM gravity; conservative reproducing-kernel SPH | agrees with Nyx to ≲ 1% in P1D only when the density is reconstructed by tessellation instead of the SPH kernel [src] | Chabanier et al. 2022, arXiv:2207.05023 |
| SPH codes (code names not in the abstracts read; PRIYA uses "the code and hydrodynamic model of the ASTRID simulation") | particle-based hydrodynamics | Sherwood, Sherwood-Relics, PRIYA; allow galaxy-formation physics and warm dark matter in the same run | Bolton et al. 2016, arXiv:1605.03462; Bird et al. 2023, arXiv:2306.05471 |
| RAMSES | adaptive mesh refinement | Horizon-AGN series used to bound the AGN-feedback signature in P1D | Chabanier et al. 2020, arXiv:2002.02822 |

**Standard approximations and what each costs.**
- Optically thin, spatially uniform ultraviolet background (Haardt & Madau 2012 or Faucher-Giguère et al. 2009 tables). With the former, Nyx gives T_0 about 10⁴ K and γ about 1.55 at z = 2 and a mean flux close to observations; with the latter the mean flux is 10–15% low at z = 2 and a factor 2 low at z = 4 [src] (arXiv:1406.6361).
- Rescaling optical depths in post-processing to match an assumed mean flux. It is universal practice and it changes the apparent convergence rate [src] (arXiv:1406.6361). It is also why the amplitude of the linear power is degenerate with the mean transmission in P1D fits (Walther et al. 2024, arXiv:2412.05372).
- Splicing: combining a large low-resolution box with a small high-resolution box to emulate a large high-resolution one. Lukić et al. find it accurate only at the 10% level for P1D [src] (arXiv:1406.6361). Any analysis that still splices carries this as a model error.
- Instantaneous, homogeneous reionisation. Sherwood-Relics replaces it with a hybrid radiative-transfer scheme that follows the patchy ionising field; patchy reionisation leaves large-scale temperature fluctuations that persist after reionisation and raise the flux power on large scales at z > 4 [src] (Puchwein et al. 2022, arXiv:2207.13098). PRIYA includes patchy hydrogen and helium reionisation models and finds that patchy helium reionisation adds large-scale P1D power [src] (arXiv:2306.05471).
- No galaxy formation. AGN feedback suppresses the P1D at all scales, more at low redshift; ignoring it shifts σ_8 by 2% and n_s by 1% [src] (arXiv:2002.02822).

**Parametrising the three-dimensional flux power.** Arinyo-i-Prats et al. 2015 (arXiv:1506.04519) introduced the fitting formula for the non-linear P3D of the transmission, with a transition scale from linear to non-linear anisotropy and a pressure (Jeans) cut-off, and predicted the two linear biases b_δ and b_η from hydrodynamical simulations. The six small-scale parameters that ForestFlow emulates are deviations of this kind.

**Emulators trained on these simulations.**

| Emulator | Training set | Parametrisation | Stated accuracy | Reference |
|---|---|---|---|---|
| LaCE (neural network) | hydrodynamical suite of the LaCE project | amplitude and slope of the linear power at the forest scale plus IGM state, per redshift, instead of cosmological parameters | sub-percent on P1D for k_∥ = 0.1–4 Mpc⁻¹, z = 2–4.5, including massive neutrinos, running and curvature not in the training set; 1% for unseen thermal histories; percent level to k_∥ = 8 Mpc⁻¹ [src] | Cabayol-Garcia et al. 2023, arXiv:2305.19064 |
| ForestFlow (conditional normalising flow) | 30 fixed-and-paired hydrodynamical simulations, z = 2–4.5 | b_δ, b_η and six parameters of the small-scale P3D | 3% on P3D to k = 5 Mpc⁻¹ and 1.5% on P1D to k_∥ = 4 Mpc⁻¹ [src] | Chaves-Montero et al. 2024, arXiv:2409.05682 |
| PRIYA (multi-fidelity Gaussian process) | 48 low-fidelity + 3 high-fidelity runs | 4 cosmological + 5 astrophysical or thermal parameters | interpolation error < 1%; simulations converged at the percent level for z = 5.4–2.2 [src] | Bird et al. 2023, arXiv:2306.05471 |
| Lyssa / lym1d (Gaussian process) | 18 Nyx runs | A_Lyα, n_Lyα and thermal parameters | each run sub-percent converged in P1D; percent-level agreement with the previous emulator [src] | Walther et al. 2024, arXiv:2412.05372 |

Units differ between these emulators (Mpc⁻¹ for LaCE and ForestFlow, h/Mpc for Nyx convergence statements, s/km for data); convert before comparing a k_max.

**Synthetic spectra for BAO analyses.** Lyα BAO mocks are not hydrodynamical. LyaCoLoRe turns Gaussian-random-field skewers into transmitted-flux skewers with fast approximations, recovers the BAO signal and literature-like bias parameters, and can add high-column-density systems and metals (Farr et al. 2019, arXiv:1912.02763). The date-sorted search of 2025–2026 found hybrid-EFT and field-level forward models validated on AbacusSummit with a painted forest and on Sherwood (titles seen: arXiv IDs not cited because the abstracts were not read in full).

## 5. Approximate methods and fast mocks

Approximate methods exist because a covariance matrix or a field-level inference needs hundreds to millions of forward evaluations, and a tree code cannot supply them. They fall into four families, ordered by decreasing cost.

**5.1 Quasi-N-body particle-mesh schemes.** A particle-mesh solver with few global time steps, made accurate on large scales by building perturbation theory into the integrator.

| Scheme | Principle | Stated performance | Reference |
|---|---|---|---|
| COLA | solve the equations of motion in the frame comoving with the LPT trajectories; the N-body part only supplies the residual | 10 time steps suffice for halo statistics down to 10¹¹ M_⊙/h in a 100 Mpc/h box with 5 × 10⁹ M_⊙/h particles; the same accuracy without COLA needs at least 3 times more steps [src] | Tassev et al. 2013, arXiv:1301.0322 |
| ICE-COLA (optimised COLA) | parameter study against MICE-GC | with 40 linearly spaced steps from z_i about 20 and a force mesh three times finer than the particle grid: matter P(k) within 1% for k ≲ 1 h/Mpc; halo mass function within 5%; halo bias within 2% for k ≲ 0.7 h/Mpc; redshift-space halo monopole and quadrupole within 4% for k ≲ 0.4 h/Mpc; valid for 0 < z < 1 and M > 10¹²·⁵ M_⊙/h [src] | Izard et al. 2015, arXiv:1509.04685 |
| FastPM | plain particle mesh with modified kick and drift factors that enforce the correct linear (1LPT) growth; no force splitting and no separate 2LPT solution | N_s = 10 steps with force-resolution factor B = 2 costs 10 times less than N_s = 40, B = 3 with very similar halo benchmarks at z = 0; lower halo stochasticity than COLA at equal step number [src] | Feng et al. 2016, arXiv:1603.00476 |
| sCOLA, tiled | COLA in space as well as time: the volume is cut into tiles evolved independently, with a buffer region and Dirichlet boundary conditions from LPT | degree of parallelism equal to the number of tiles; "perfectly parallel" [src] | Leclercq et al. 2020, arXiv:2003.04925 |
| BullFrog | second-order integrator whose steps reproduce 2LPT without computing 2LPT displacements; converges to the exact solution as the step number grows, also after shell crossing | improves on FastPM and COLA at no extra cost; trivial to add to a code that already has FastPM stepping [src] | Rampf et al. 2024, arXiv:2409.19049 |

Three consequences follow for a user of these codes. First, accuracy is a function of (number of steps, force-mesh factor, starting redshift), so "a COLA mock" without these three numbers has no defined accuracy. Second, halo internal structure is not resolved: a 20-step COLA forward model describes the density field around the most massive local clusters but does not give converged virial masses [src] (Stopyra et al. 2023, arXiv:2304.09193), which is why constrained-simulation projects resimulate the inferred initial conditions with a full N-body code (section 9). Third, these codes are in survey production: the DESI N-body comparison included FastPM as a quasi-N-body code planned for some DESI analyses (arXiv:2112.09138), and UNIT ran FastPM boxes beside its full N-body runs (arXiv:1811.02111).

Neutrinos in FastPM: Bayer et al. (2020) add neutrino particles with quasi-random sampling of the Fermi–Dirac distribution and report percent-level CDM and total matter power for M_ν ≲ 0.6 eV at z ≲ 2 in about 25 steps from z = 99 (read this session; not in the source list, see "Not verified").

**5.2 LPT plus an effective bias model.** No N-body step at all: a Zel'dovich or 2LPT density field is mapped to tracers with a parametrised, stochastic bias calibrated on a reference.
- EZmocks: Zel'dovich field plus an effective tracer bias model calibrated on the clustering of the data (eBOSS) or of N-body HOD mocks (DESI); reproduces two- and three-point statistics; cost close to a lognormal mock (Zhao et al. 2020, arXiv:2007.08997; DESI set-up in Forero-Sánchez et al. 2024, arXiv:2411.12027).
- CoLoRe-2LPT: 2LPT density and velocities for quasars and Lyα skewers, replacing the earlier lognormal approach (Ruiz-Herrera Bernal et al. 2026, arXiv:2607.27412).
- Calibrated halo-assignment methods (Patchy, Halogen) and predictive Lagrangian methods (Pinocchio, PeakPatch) are the other entries of the comparison project (Blot et al. 2018, arXiv:1806.09497).

**5.3 Lognormal and Gaussian fields.** A Gaussian field transformed point by point; exact two-point function by construction, wrong higher orders. GLASS builds a light-cone as nested shells of matter, galaxies and lensing, with transformed Gaussian fields generated to essentially arbitrary precision and an iterative line-of-sight integration for lensing; it reaches percent-level two-point statistics for clustering and weak lensing [src] (Tessore et al. 2023, arXiv:2302.01942).

**5.4 Learned surrogates.** Field-level neural emulators and control-variate estimators that pair a few expensive runs with many cheap ones were read this session but lie outside the source list; see "Not verified".

**Choosing between them.** The rule that the comparison papers support is: use the cheapest method whose error on the statistic you need is below your tolerance, and state the reference it was calibrated on. Methods calibrated on two-point statistics are not validated for the bispectrum (section 5 of `systematics.md`).

## 6. Galaxy–halo connection

Review: Wechsler & Tinker 2018 (arXiv:1804.03097), which defines the galaxy–halo connection as the multivariate distribution of galaxy and halo properties. Its summary numbers: star-formation efficiency peaks in haloes near 10¹² M_⊙, where less than 20% of the baryons have turned into stars; the intrinsic scatter in stellar mass at fixed halo mass is below 0.2 dex above that mass [src].

The methods used to populate gravity-only simulations, from fewest to most assumptions about galaxy formation:

| Method | What is assumed | Where it is used in the sources read | Reference |
|---|---|---|---|
| Halo occupation distribution (HOD) | the number of galaxies in a halo depends on halo mass only; a step-like central term plus a power-law satellite term (the "vanilla" five-parameter form) | DESI AbacusSummit mocks; Flagship 2 (with abundance matching); all DESI HOD-systematics tests | Mena-Fernández et al. 2024, arXiv:2404.03008; arXiv:2405.13495 |
| Extended HOD | adds velocity bias, incompleteness, a satellite-profile parameter and an assembly-bias parameter (occupation depends on a secondary halo property such as concentration or environment) | DESI "baseline" and "extended" LRG models | arXiv:2404.03008 |
| Subhalo abundance matching (SHAM) | galaxies are rank-ordered onto subhaloes by a mass or velocity proxy, with scatter; needs resolved subhaloes | DESI DR2 reference mocks on Uchuu (read, outside the source list); Flagship 2 luminosities | arXiv:2405.13495 |
| Semi-analytic models | simplified galaxy-formation physics run on halo merger trees | Millennium; Last Journey; MillenniumTNG (calibrated on its own hydrodynamical run); SIBELIUS-DARK with GALFORM | arXiv:astro-ph/0504097; arXiv:2006.01697; arXiv:2210.10059; arXiv:2202.04099 |
| Hydrodynamical simulation as the galaxy model | everything in section 3 | IllustrisTNG galaxy clustering agrees with SDSS at z about 0.1 as a function of stellar mass and colour [src] | arXiv:1707.03397 |
| Effective bias on an approximate field | no haloes at all; a stochastic, non-local bias fitted to a reference | EZmocks, CoLoRe | arXiv:2007.08997; arXiv:2607.27412 |

**Assembly bias.** Halo clustering depends on properties other than mass (formation time, concentration, environment); if galaxy occupation correlates with those properties, the mass-only HOD is wrong. The test on a hydrodynamical simulation that is most often cited: in TNG300 the mass-only HOD underpredicts the real-space galaxy correlation function by about 15% on 1 < r < 20 Mpc/h; the secondary properties that best repair it are the local environment, the velocity-dispersion anisotropy and σ²R_halfmass, ahead of spin, formation epoch and concentration [src] (Hadzhiyska et al. 2019, arXiv:1911.02610).

**Why this matters for cosmology.** The DESI DR1 BAO analysis detects an HOD-dependent shift of 0.19% in α_AP in configuration space at 3.3σ and none at 3σ elsewhere [src] (arXiv:2404.03008). The DESI DR1 full-shape analysis finds that parameter shifts between HOD models often exceed 20% of the statistical error, and adds a systematic covariance term C_HOD to the data covariance rather than to the posteriors [src] (Findlay et al. 2024, arXiv:2411.12023). Analyses beyond two-point statistics rely on one simulation suite and one HOD family, a point developed in `cosmo-beyond-two-point`.

**Resolution requirement.** Halo statistics are converged at 1% only above 500 particles per halo [src] (arXiv:1804.05865). HalfDome resolves haloes only above about 6 × 10¹² M_⊙/h [src] (arXiv:2407.17462): enough for LRG-like hosts, not for emission-line galaxies. Flagship 2 was sized to resolve 10¹¹ M_⊙/h haloes with m_p = 10⁹ M_⊙/h, that is, with about 100 particles [der: 10¹¹/10⁹ from arXiv:2405.13495 section 2.1], and applies halo-mass corrections for incompleteness and discreteness (section titles of arXiv:2405.13495; content not read).

## 7. Light-cones and survey realism

A survey observes the past light-cone, not a snapshot. Four constructions are in use.

1. **Particle light-cone written on the fly.** Each particle is output when the shrinking light surface of the observer sweeps past it. Flagship 2 does this over the full sky to z = 3 by replicating the 3600 Mpc/h box, giving 31 trillion particle outputs and lensing maps at HEALPix N_side = 8192 (0.43 arcmin pixels) [src] (arXiv:2405.13495, section 2.1). FLAMINGO writes light-cones on the fly for up to 8 observers [src] (arXiv:2306.04024); Last Journey writes particle light-cones in situ from z about 10 [src] (arXiv:2006.01697); MillenniumTNG and AbacusSummit provide direct light-cone outputs (arXiv:2210.10059, arXiv:2110.11398); HalfDome provides full-sky light-cones for z = 0–4 [src] (arXiv:2407.17462).
2. **Pseudo-light-cone from snapshots.** Boxes at a few redshifts are cut to the survey geometry and concatenated. The DESI DR1 EZmocks are of this kind, and the paper states that mocks with actual redshift evolution are not used [src] (arXiv:2411.12027, section 2.1).
3. **Nested shells.** GLASS draws matter shells in sequence, correlating each with the previous ones, and integrates along the line of sight for the lensing fields (arXiv:2302.01942).
4. **Light-cone from an approximate dynamical model during inference.** BORG applied to Quaia includes light-cone effects, redshift-space distortions, bias and selection in an LPT forward model (title and abstract read; outside the source list).

**Box replication.** Replicating a box to fill a light-cone repeats structure and removes modes larger than the box. The DESI EZmocks avoid it with (6 Gpc/h)³ boxes [src] (arXiv:2411.12027); Flagship 2 replicates [src] (arXiv:2405.13495); the size of the effect on lensing statistics is the subject of arXiv:2511.20423 (numbers not read).

**Survey realism.** The layers added on top of a light-cone, each a possible source of mismatch between mocks and data:
- angular footprint and radial selection n(z);
- fibre assignment: the DESI mocks use a fast emulator of the assignment, whose shot-noise properties differ from the real algorithm [src] (arXiv:2411.12027; the difference is noted in the semi-analytic covariance paper, read outside the source list);
- photometric and spectroscopic systematics, included in the eBOSS EZmocks [src] (arXiv:2007.08997);
- galaxy properties: Flagship 2 assigns luminosities, colours, spectral energy distributions, shapes, sizes, intrinsic alignments, emission lines and lensing to each galaxy (arXiv:2405.13495);
- distance-indicator errors: the DESI-PV mocks mimic Fundamental Plane, Tully–Fisher and SN Ia measurements with the statistical properties of the data [src] (arXiv:2512.03228);
- quasar continua, high-column-density systems and metals for the Lyα forest (arXiv:1912.02763, arXiv:2607.27412).

The DESI DR1 clustering of data and simulations agrees to within 2% in the inferred real-space overdensity field according to the DESI 2024 II abstract (read, outside the source list); the instrument and survey side of realism is in `cosmo-surveys-facilities` and `cosmo-galaxy-clustering`.

## 8. Emulators

An emulator interpolates a summary statistic between simulations run on a design in parameter space. The design choices that decide its accuracy:

- **What is emulated.** The non-linear correction to the linear matter power spectrum (EuclidEmulator2, arXiv:2010.11288) or the spectrum itself (Mira-Titan IV, arXiv:2207.12345); baryon emulators predict the ratio to gravity-only (arXiv:2011.15018, arXiv:2410.17109); the Lyα emulators predict P1D as a function of the local linear amplitude and slope (section 4).
- **Design.** Latin hypercubes (PRIYA, arXiv:2306.05471; sliced maximin Latin hypercube in Dark Quest, arXiv:1811.09504); a nested design that can be refined from 26 to 111 models (Mira-Titan, arXiv:1508.02654, arXiv:2207.12345); cosmology rescaling of a few boxes to 800 points (BACCO, arXiv:2004.06245).
- **Variance control.** Fixed-and-paired initial conditions (EuclidEmulator2, ForestFlow); Zel'dovich control variates (Aemulus ν, arXiv:2303.09762).
- **Multi-fidelity.** A few high-resolution runs corrected by many cheap ones: Mira-Titan IV (111 high-resolution, 1776 low-resolution, plus perturbation theory on large scales), PRIYA (3 high- and 48 low-fidelity).
- **Interpolator.** Gaussian processes (Dark Emulator, PRIYA, Lyssa, FLAMINGO response) or neural networks (BACCO baryons, LaCE; DarkEmulator2, read outside the source list).
- **Resolution correction.** EuclidEmulator2 ships a post-processing correction for residual resolution effects (arXiv:2010.11288).

The accuracy table is in `results.md` §2. Two rules for reading it. The quoted figure is measured against held-out simulations of the same suite, so it is an interpolation error; the simulation error (section 1 of `results.md`) and the baryonic effect add to it. And the range of validity in parameters matters as much as the range in k: w_a, neutrino mass and curvature are covered by some emulators and not by others, and the EuclidEmulator2 paper itself reports that adding w_a "significantly increases the complexity and expense" [src] (arXiv:2010.11288). How emulator error enters a likelihood is treated in `cosmo-statistics-inference`.

## 9. Constrained simulations and reconstructions of the local Universe

A constrained simulation is a realisation of the initial conditions chosen so that the evolved field reproduces an observed region. Unconstrained simulations can be compared with the data only statistically; constrained ones allow object-by-object comparison (named clusters, the Local Group, a void). Two families of methods exist, and they differ in what is treated as data and in what is sampled.

**9.1 Constrained realisations from peculiar velocities (linear, Gaussian).** A Wiener filter gives the mean linear field given sparse, noisy radial velocities, and the Hoffman–Ribak algorithm adds a random residual with the correct covariance, giving initial conditions that are then evolved with an N-body code. CLUES built on Cosmicflows-2 is the reference application: the cell-to-cell scatter between constrained runs is 2 to 3 times smaller than between random runs on a 5 Mpc/h scale in the inner region; the scatter between simulated and observation-reconstructed velocity fields is 104 ± 4 km/s; the simulations resemble the local Universe out to 150 Mpc/h on scales of a few tens of megaparsecs [src] (Sorce et al. 2015, arXiv:1510.04900). The constraints are linear, so structure below the constraint scale is a random draw from the prior.

**9.2 Bayesian forward modelling of the initial conditions (field-level inference).** The parameter space is the three-dimensional initial density field; a structure-formation model maps it to the evolved field; a data model (bias, selection, noise) links that to the observations; the posterior is sampled with Hamiltonian Monte Carlo.

| Step | Content | Reference |
|---|---|---|
| BORG with 2LPT | first physical forward model; accurate reconstructions above about 6 Mpc/h on SDSS DR7-like mocks; delivers initial conditions, present density and velocity with uncertainties [src] | Jasche & Wandelt 2012, arXiv:1203.3639 |
| BORG with a particle-mesh model | non-linear dynamics inside the sampler; hierarchical Bayes for galaxy bias, selection and noise, sampled in blocks beside the Hamiltonian sampler; applied to 2M++ | Jasche & Lavaux 2018, arXiv:1806.11117 |
| Accuracy of the dynamics | a 20-step COLA integrator describes the density field around the most massive clusters within 135 Mpc/h but does not give converged virial masses; hence "posterior resimulation": sample initial conditions from the posterior and evolve them with a full N-body code [src] | Stopyra et al. 2023, arXiv:2304.09193 |
| Forward modelling from velocities | Hamlet-PM: the early density field is inferred from sparse, noisy late-time peculiar velocities with a particle-mesh solver, then resimulated at high precision | Valade et al. 2026, arXiv:2602.03699 |
| Tiling | independent tiles with LPT boundary conditions for the dynamics (sCOLA, arXiv:2003.04925); a tiled inference strategy extends Manticore to (4 Gpc/h)³ | McAlpine et al. 2026, arXiv:2606.10020 |
| Differentiable particle-mesh codes | DISCO-DJ: GPU particle mesh in JAX with BullFrog stepping; 6 steps give percent-level P(k) at k about 0.2 h/Mpc with 512³ particles in a few seconds; forward- and reverse-mode derivatives, the latter by an adjoint method with memory independent of the number of steps; demonstrated on recovering σ_8 and the initial conditions from a noisy GADGET density field [src] | List et al. 2025, arXiv:2510.05206 |
| From the Lyα forest | TARDIS: maximum-likelihood reconstruction of the initial density of a z about 2.5 volume observed by Lyα tomography, with a fast non-linear gravity model; recovers smaller scales than Wiener filtering; cosmic-web eigenvalues correlate at r = 0.95 with the truth for 30 m-class data; the field can be evolved to z = 0 [src] | Horowitz et al. 2019, arXiv:1903.09049 |

**9.3 From an inferred field to a simulation.** The sequence used by the current projects is: (i) inference at a few Mpc/h with an approximate solver; (ii) draw posterior samples of the initial conditions; (iii) add unconstrained small-scale modes; (iv) resimulate with a full N-body or hydrodynamical code, possibly as a zoom with multi-scale initial conditions (MUSIC, arXiv:1103.6031). The output is an ensemble; a single constrained run is one posterior sample and carries no error bar.

**9.4 Validation.** Posterior-predictive tests on the power spectrum, bispectrum, Gaussianity of the initial conditions and halo mass function (Manticore, arXiv:2505.10682, arXiv:2606.10020); comparison with data not used in the inference: direct distance tracers scored by Bayesian evidence, residual redshifts, velocity scaling and the need for an external bulk flow (Stiskalek et al. 2025, arXiv:2502.00121); CMB lensing and kSZ stacking (arXiv:2606.10020); matched counterparts of named clusters (arXiv:2505.10682, arXiv:2602.03699).

**9.5 What it is not.** The reconstructions assume a cosmology in the prior and in the forward model. A BORG field is a conditional reconstruction, not a parameter constraint; the distinction between sampled initial conditions, Gaussian field-level likelihoods (flip) and neural approaches is drawn in `cosmo-beyond-two-point`, and the use of reconstructed velocity fields for peculiar-velocity corrections in `cosmo-peculiar-velocities`.

## 10. Neutrino and modified-gravity simulations

**Massive neutrinos.** Three implementations appear in the suites read:
- neutrinos as a second particle species, accurate up to the largest mass simulated (0.5 eV in Aemulus ν, arXiv:2303.09762);
- the δf method in SWIFT, used by FLAMINGO: particles follow the full non-linear neutrino phase-space distribution but are statistically weighted against the background distribution, which minimises shot noise and removes the spurious early back-reaction on cold matter; the weighting is applied in the long-range mesh force only. The FLAMINGO baseline has one massive species of 0.06 eV and two massless ones [src] (arXiv:2306.04024, section 2.2; arXiv:2305.13380);
- linear neutrino perturbations added to the force as a source term or look-up table in the N-body gauge (EuclidEmulator2, arXiv:2010.11288; Flagship 2 with the minimal mass of 0.0587 eV, arXiv:2405.13495; GINKAKU, arXiv:2605.28581);
- particle neutrinos in a fast particle-mesh code (FastPM; read outside the source list).

The Euclid code comparison tested eleven full N-body implementations (not all independent), two schemes with approximate time integration and four codes that predict or emulate P(k), on common initial data; it finds them fully consistent and concludes that the effect of massive neutrinos is modelled at the sub-percent level in the most common summary statistics (power spectrum, bispectrum, halo mass function, halo bias) [src] (Adamek et al. 2022, arXiv:2211.12457).

**Modified gravity.** N-body codes for f(R), DGP and symmetron models solve a non-linear scalar-field equation for the fifth force, including its screening. The code-comparison project finds that the fractional deviation of the matter power spectrum from ΛCDM agrees between codes to better than 1% up to k about 5–10 h/Mpc, with good agreement on the velocity-divergence spectrum, halo abundances and profiles, and that the quasi-static approximation is very good for the observables considered, tested on the symmetron model [src] (Winther et al. 2015, arXiv:1506.06384). The statement is about the ratio to ΛCDM, not about the absolute spectrum. The Euclid collaboration repeated a comparison for a wider set of models in 2024 (title and abstract read, outside the source list). Model definitions and constraints are in `cosmo-dark-energy-modified-gravity`.

**Non-cold dark matter.** Warm dark matter runs are part of Sherwood (arXiv:1605.03462); fuzzy and self-interacting dark matter need dedicated solvers and are covered, with the limits they support, in `cosmo-neutrinos-dark-matter`.

## Not verified

- The Hoffman–Ribak constrained-realisation algorithm is named in section 9 as a textbook method; its original paper (1991) was not fetched and carries no identifier here.
- Relativistic N-body methods (gevolution), GPU-native differentiable fast-multipole codes and other 2026 code releases were seen in the date-sorted search by title only.
- Halo and structure finders, merger-tree builders: not researched.
- Semi-analytic models and empirical models beyond their mention in section 6: not researched.
- Ray-tracing algorithms for lensing light-cones: not researched.
- Read in abstract this session but outside the source list because the cap of 100 was reached: FastPM with neutrino particles (percent-level power for M_ν ≲ 0.6 eV at z ≲ 2, about 25 steps); L-PICOLA (2% on P(k), 5% on the reduced bispectrum at z = 0); the original EZmocks paper (1% to k = 0.55 h/Mpc); the nIFTy mock comparison; PPM-GLAM (about 15,000 runs, 1% to k about 1 h/Mpc); CARPool (about 100-fold variance reduction pairing GADGET with COLA); a field-level neural emulator of N-body displacements (accurate to k about 1 h/Mpc); a 2026 Zel'dovich control-variate estimator for mock covariances; the first halo assembly-bias paper (2005); the original HOD central–satellite paper (2004) and the SHAM paper (2005). Search for them by these descriptions before citing.
