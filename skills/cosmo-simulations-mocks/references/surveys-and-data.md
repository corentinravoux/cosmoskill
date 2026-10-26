# Simulation suites and mock data sets

Scope: one table row per simulation suite or mock set — code, box, particle number or resolution, cosmologies, use, public location — read at source.
Snapshot: 2026-10-13

## 1. Gravity-only suites
<!-- key: gravity-only-suites -->

Units are those of the source: h⁻¹ where the paper uses it, none where it does not. "n/a" means the abstract read does not give the number; such cells are listed under "Not verified". The run parameters read in the body of the suite papers (softening, order and redshift of the initial conditions, number of realisations) are tabulated in `physics-and-methods.md` §12, which takes precedence over a cell here.

| Suite | Code | Box side | Particles / particle mass | Cosmologies | Built for | Public location | Reference, flag |
|---|---|---|---|---|---|---|---|
| Millennium | n/a | n/a | n/a | one | semi-analytic galaxy formation on dark-matter merger trees; shows baryon-induced features surviving in the low-redshift galaxy distribution | n/a | Springel et al. 2005, arXiv:astro-ph/0504097 |
| MultiDark | n/a | volumes up to 50 Gpc³ in total | halo masses 10¹⁰–10¹⁵ M_⊙, more than 60 billion halos in all runs | Planck-like | halo profiles and concentrations; parent of the BOSS MD-Patchy calibration | n/a | Klypin et al. 2014, arXiv:1411.4001 [src] |
| Outer Rim | HACC | 4.225 Gpc | more than one trillion; 10,240³, started at z = 200 with 1LPT [sec: arXiv:2112.05165, Sect. 10.1] | one | eBOSS and DESI synthetic catalogues, LSST DESC data challenge | halo catalogues and downsampled particles released | Heitmann et al. 2019, arXiv:1904.11970 [src] |
| Last Journey | HACC | 5.025 Gpc | more than 1.24 trillion | one, Planck | semi-analytic galaxies from z about 10, in-situ particle light-cones, subhalo cores | subset public; OpenCosmo portal | Heitmann et al. 2020, arXiv:2006.01697 [src] |
| Frontier-E | HACC | n/a | two trillion | n/a | flagship gravity-only run served through OpenCosmo (https://opencosmo.science) with Last Journey, Discovery and a 64-member hydrodynamic suite | OpenCosmo | Wells et al. 2026, arXiv:2607.16059 [src] |
| PKDGRAV3 two-trillion-particle run (the first Euclid Flagship simulation, 10,000³ particles in 3 Gpc/h, according to the review [sec: arXiv:2112.05165, Sect. 10.1]) | PKDGRAV3 | n/a in the abstract | 2 trillion | one | "next era of galaxy surveys" (the abstract does not name Euclid) | n/a | Potter et al. 2016, arXiv:1609.08621 [src] |
| Euclid Flagship 2 | PKDGRAV3 | 3600 Mpc/h | 16,000³ = four trillion; m_p = 10⁹ M_⊙/h; softening 4.5 kpc/h; 1LPT initial conditions at z = 99; light-cone produced on the fly | one (Euclid reference: Ω_m = 0.319, h = 0.67, σ_8 about 0.813, minimal neutrino mass 0.0587 eV) | 16 billion haloes in one octant to z = 3; 3.4 billion galaxies at H_E < 26 from HOD plus abundance matching | n/a | Euclid Collaboration 2024, arXiv:2405.13495, abstract and section 2.1 [src] |
| Uchuu | GreeM, TreePM (arXiv:2007.14720, Sect. 2; arXiv:0910.0121) | 2.0 Gpc/h | 12800³ = 2.1 trillion; 3.27 × 10⁸ M_⊙/h | one, Planck | halos from dwarfs to clusters; DESI and other mocks | Skies & Universes | Ishiyama et al. 2020, arXiv:2007.14720 [src] |
| Shin-Uchuu | same | 140 Mpc/h | 6400³ = 262 billion; 8.97 × 10⁵ M_⊙/h | one | subhalo resolution | Skies & Universes | arXiv:2007.14720 [src] |
| AbacusSummit | Abacus | 2 Gpc/h (base); 500 Mpc/h (covariance boxes) | base: 2 × 10⁹ M_⊙/h, 139 boxes; 1883 small boxes; about 60 trillion particles in total | 97 models, including Planck 2018, a derivative grid and an emulator grid | DESI reference suite; 33 epochs from z = 8 to 0.1; light-cones, halo catalogues | public data release (location n/a) | Maksimova et al. 2021, arXiv:2110.11398 [src] |
| UNIT | full N-body (code n/a) and FastPM | 1 (Gpc/h)³ volume per box | about 1.2 × 10⁹ M_⊙/h | one | fixed-and-paired boxes for emission-line galaxies; two pairs match the variance of about 150 ordinary boxes for a 20 (Gpc/h)³ survey | unitsims.org | Chuang et al. 2018, arXiv:1811.02111 [src] |
| Quijote | GADGET-III (arXiv:1909.05273, Sect. II) | 1 Gpc/h | 256³, 512³ or 1024³; 44,100 simulations | more than 7000 models in {Ω_m, Ω_b, h, n_s, σ_8, M_ν, w} | Fisher information content and machine-learning training | about one petabyte released (location n/a) | Villaescusa-Navarro et al. 2019, arXiv:1909.05273 [src] |
| Aemulus | L-GADGET2 (arXiv:1804.05865, Sect. III) | 1.05 Gpc/h | 3.51 × 10¹⁰ (Ω_m/0.3) M_⊙/h; softening 20 kpc/h; 75 boxes | 47 wCDM models | emulators of halo mass function and galaxy clustering | AemulusProject.github.io | DeRose et al. 2018, arXiv:1804.05865 [src] |
| Aemulus ν | n/a | 1.05 Gpc/h | 3.51 × 10¹⁰ (Ω_cb/0.3) M_⊙/h; 150 boxes | wνCDM, neutrino mass up to 0.5 eV as a second particle species, wide σ_8 range | hybrid-EFT and matter-power surrogates | released with the paper | DeRose et al. 2023, arXiv:2303.09762 [src] |
| Dark Quest | n/a | n/a | 2048³ | 101 flat wCDM models (sliced Latin hypercube) | Dark Emulator: halo mass function, halo–matter and halo–halo correlations, z = 0–1.48 | n/a | Nishimichi et al. 2018, arXiv:1811.09504 [src] |
| Dark Quest II (first runs) | GINKAKU | up to 4 Gpc/h | 3000³ | eight models so far, with massive neutrinos and clustering dark energy | next-generation emulators | n/a | Nishimichi et al. 2026, arXiv:2605.28581 [src] |
| Mira-Titan | n/a | 2.1 Gpc | 3200³; 111 simulations, plus 1776 lower-resolution runs | {ω_m, ω_b, σ_8, h, n_s, w_0, w_a, ω_ν} | Mira-Titan power-spectrum emulator | released with the paper | Heitmann et al. 2015, arXiv:1508.02654; Moran et al. 2022, arXiv:2207.12345 [src] |
| EuclidEmulator2 training set | PKDGRAV3 (arXiv:2010.11288, Sect. 8.2.1) | 1 Gpc/h | 3000³; over 250 simulations, paired and fixed | w0waCDM + Σm_ν, eight parameters | non-linear boost emulator | github.com/miknab/EuclidEmulator2 | Euclid Collaboration 2020, arXiv:2010.11288 [src] |
| BACCO | n/a | about 2 Gpc | 4320³ | 800 points in eight dimensions reached by cosmology rescaling of a few boxes | matter, galaxy and gas emulators | dipc.org/bacco | Angulo et al. 2020, arXiv:2004.06245 [src] |
| HalfDome | n/a | 3.75 Gpc/h | 6144³; minimum halo mass about 6 × 10¹² M_⊙/h; valid to k about 1 h/Mpc | 11 realisations of one cosmology, plus one with f_NL = 20 | full-sky light-cones z = 0–4 for joint Stage-IV analyses | halfdomesims.github.io | Bayer et al. 2024, arXiv:2407.17462 [src] |

Reading the table: three kinds of suite exist and they are not interchangeable. Flagship runs (Outer Rim, Uchuu, Flagship 2, Frontier-E) give one cosmology at high resolution for survey mocks. Emulator grids (Aemulus, Mira-Titan, EuclidEmulator2, Dark Quest, the AbacusSummit grid) trade volume for coverage of parameter space. Ensemble suites (Quijote, the 1883 AbacusSummit small boxes) trade resolution for the number of realisations needed for covariances, Fisher derivatives and neural-network training.

## 2. Hydrodynamical suites (galaxy formation)
<!-- key: hydrodynamical-suites-galaxy-formation -->

| Suite | Code, solver | Box | Resolution | Variations | Calibrated to | Public | Reference, flag |
|---|---|---|---|---|---|---|---|
| OWLS / cosmo-OWLS | n/a | n/a | n/a | many single-process variations; the AGN run solves overcooling | group optical and X-ray properties (AGN run) | power spectra at powerlib.strw.leidenuniv.nl | van Daalen et al. 2011, arXiv:1104.1174; van Daalen et al. 2019, arXiv:1906.00968 [src] |
| Horizon-AGN | RAMSES (per arXiv:2002.02822) | n/a | more than 150,000 galaxies per output at 1.2 < z < 1.8 | with and without AGN; dark-matter-only twin | n/a | horizon-simulation.org (power spectra) | Dubois et al. 2014, arXiv:1402.1165; Chisari et al. 2018, arXiv:1801.08559 [src: abstract] |
| EAGLE | modified GADGET-3, SPH; thermal stellar and AGN feedback | up to 100 comoving Mpc | 1504³ dark-matter particles of 9.70 × 10⁶ M_⊙ in the largest run (arXiv:1407.7040, Table 2) | sub-grid variations | z about 0 stellar mass function, black-hole masses, sizes | n/a | Schaye et al. 2014, arXiv:1407.7040 [src] |
| IllustrisTNG (TNG50, TNG100, TNG300) | AREPO, moving-mesh MHD | 51.7, 106.5 and 302.6 Mpc (arXiv:1812.05609, Table 1) | each with lower-resolution and dark-matter-only twins | none in the flagship runs | (model built on Illustris; see arXiv:1703.02970) | full release, about 1.1 PB, 100 snapshots each, web API | Nelson et al. 2018, arXiv:1812.05609 [src] |
| BAHAMAS | GADGET-3, TreePM-SPH | 400 Mpc/h | 2 × 1024³; dark matter 3.85 × 10⁹ M_⊙/h, baryons 7.66 × 10⁸ M_⊙/h for WMAP-9 (arXiv:1603.02702, Sect. 2.1) | AGN heating variations (used in arXiv:1906.00968) | present-day stellar mass function and hot gas fractions of groups and clusters | n/a | McCarthy et al. 2016, arXiv:1603.02702 [src] |
| SIMBA | GIZMO, meshless finite mass | 100 Mpc/h | 1024³ gas elements | feedback switched off in turn | not calibrated to gas fractions (reproduces hot gas fractions as a result) | n/a | Davé et al. 2019, arXiv:1901.10203 [src: abstract] |
| CAMELS | AREPO and GIZMO, with the IllustrisTNG and SIMBA sub-grid models | 25 Mpc/h each | 256³ dark-matter and 256³ gas elements per run (arXiv:2010.00619, Sect. III); more than 100 billion elements in total | 4233 runs: 2184 hydrodynamical, 2049 N-body; Ω_m, σ_8 and four feedback parameters varied | none: built to span | public | Villaescusa-Navarro et al. 2020, arXiv:2010.00619 [src] |
| ANTILLES | n/a | n/a | n/a | 400 runs over the "feedback landscape" | none: built to span | pyspk model | Salcido et al. 2023, arXiv:2305.09710 [src: abstract] |
| MillenniumTNG | AREPO (hydro), with a dark-matter-only suite | 740 Mpc = 500 Mpc/h (hydro); 3000 Mpc (flagship N-body with neutrinos) | hydro: 4320³ gas cells, baryon mass 3.1 × 10⁷ M_⊙ (2 × 10⁷ M_⊙/h); N-body: up to 4320³, 1.32 × 10⁸ M_⊙/h; flagship: 1.1 trillion particles | fixed-and-paired N-body | IllustrisTNG model unchanged | n/a | Hernández-Aguayo et al. 2022, arXiv:2210.10059; Pakmor et al. 2022, arXiv:2210.10060 [src: abstract] |
| FLAMINGO | SWIFT, SPH (arXiv:2306.04024 section 2.1; arXiv:2305.13380); 3LPT initial conditions at z = 31; δf neutrinos | 1.0 Gpc and 2.8 Gpc | baryon particle mass 10⁸ M_⊙ (1 Gpc) and 10⁹ M_⊙ (2.8 Gpc); the 2.8 Gpc run has 3 × 10¹¹ particles | 12 variations at 10⁹ M_⊙ in 1 Gpc: 8 astrophysical (shifted stellar mass function and/or cluster gas fractions; thermal or jet AGN), 4 cosmological including neutrino masses | z = 0 stellar mass function and cluster gas fractions | n/a | Schaye et al. 2023, arXiv:2306.04024 [src] |
| HACC hydrodynamic suite | HACC | n/a | n/a | 64 members | n/a | OpenCosmo | Wells et al. 2026, arXiv:2607.16059 [src: abstract] |

CAMELS boxes are 25 Mpc/h: its own paper notes that the IllustrisTNG and SIMBA models give similar galaxy properties but significantly different halo baryon fractions and baryonic effects on P(k) [src: abstract] (arXiv:2010.00619). The FLAMINGO baryonic response is converged only for volumes above (200 Mpc)³ [src: abstract] (arXiv:2410.17109), so a P(k) suppression read from a CAMELS box carries a volume caveat.

## 3. Hydrodynamical suites for the Lyα forest
<!-- key: hydrodynamical-suites-for-the-lyalpha-forest -->

| Suite | Code | Box | Resolution | Parameter coverage | Used for | Reference, flag |
|---|---|---|---|---|---|---|
| Nyx convergence suite | Nyx | several, to establish L > 40 Mpc/h | down to 20 kpc/h cells | one ΛCDM model, two UV backgrounds, 2 ≤ z ≤ 4 | resolution, box-size and splicing requirements | Lukić et al. 2014, arXiv:1406.6361 [src: abstract] |
| Sherwood | n/a (code name not in the abstract) | 10 to 160 Mpc/h | almost four orders of magnitude in mass resolution, up to 17.2 billion particles | includes warm dark matter and galactic outflows | comparison with high-resolution forest data at 2 < z < 5 | Bolton et al. 2016, arXiv:1605.03462 [src] |
| Sherwood-Relics | n/a; adds a hybrid radiative-transfer scheme | n/a | n/a | over 200 simulations in astrophysical and cosmological parameters | patchy reionisation and pressure smoothing at z > 4 | Puchwein et al. 2022, arXiv:2207.13098 [src: abstract] |
| Horizon-AGN P1D series | RAMSES | n/a | n/a | eight runs varying AGN feeding, feedback and stochasticity | bounds on the AGN signature in P1D at nine redshifts, z = 4.25–2.0 | Chabanier et al. 2020, arXiv:2002.02822 [src: abstract] |
| Nyx versus CRK-HACC | Nyx and CRK-HACC | n/a | n/a | one model | Eulerian versus SPH agreement for DESI and high-resolution data | Chabanier et al. 2022, arXiv:2207.05023 [src] |
| PRIYA | "the code and hydrodynamic model of the ASTRID simulation" (abstract wording) | 120 Mpc/h | 48 runs at 1536³ particles, 3 runs at 3072³ | 4 cosmological + 5 astrophysical or thermal parameters; supernova and AGN feedback; patchy H and He reionisation; realistic DLA population | P1D emulator for SDSS and DESI | Bird et al. 2023, arXiv:2306.05471 [src] |
| LaCE training suite | n/a | n/a | n/a | amplitude and slope of the linear power, IGM state | P1D emulator for DESI | Cabayol-Garcia et al. 2023, arXiv:2305.19064 [src] |
| ForestFlow training suite | n/a | n/a | n/a | 30 fixed-and-paired runs, z = 2–4.5 | P3D and P1D emulator | Chaves-Montero et al. 2024, arXiv:2409.05682 [src: abstract] |
| Lyssa | Nyx | 120 Mpc (about 80.8 Mpc/h, table in Sect. 1) | 4096³ cells | 18 runs | P1D emulator in the lym1d likelihood | Walther et al. 2024, arXiv:2412.05372 [src: abstract] |

The Lyssa resolution, defined as L/N^{1/3}, is 29.3 kpc, about 19.7 h⁻¹ kpc [src: Sect. 1 and its table, arXiv:2412.05372], close to the 20 kpc/h that Lukić et al. 2014 (arXiv:1406.6361) require for 1% convergence.

Synthetic-spectrum sets for BAO (LyaCoLoRe, arXiv:1912.02763) are described in the methods file. The mock sets and counts used by the DESI Lyα BAO analyses are in `cosmo-lyman-alpha`; they were not re-read here.

## 4. Fast-mock sets used by surveys
<!-- key: fast-mock-sets-used-by-surveys -->

| Survey analysis | Mock set | Method | Count and volume | Calibrated on | Used for | Reference, flag |
|---|---|---|---|---|---|---|
| eBOSS DR16 | EZmocks | Zel'dovich + effective bias, with redshift evolution and photometric and spectroscopic systematics | 1000 realisations per tracer, 0.6 < z < 2.2 | the eBOSS clustering itself | covariance matrices and pipeline tests; data and mocks agree within 1σ down to a few Mpc/h and up to k = 0.3 h/Mpc | Zhao et al. 2020, arXiv:2007.08997 [src: abstract] |
| DESI DR1 (2024) | EZmocks | same | 1000 North and 1000 South Galactic Cap pseudo-light-cones; for each tracer and snapshot 2000 boxes of (6 Gpc/h)³ with 1728³ particles; no box replication; fast fibre assignment applied | two-point clustering of the DESI AbacusSummit HOD mocks, themselves fitted to the DESI one-percent survey | sample covariance; validation of the analytic covariance | Forero-Sánchez et al. 2024, arXiv:2411.12027, section 2.1 [src] |
| DESI DR1 BAO, HOD systematics | AbacusSummit HOD mocks | N-body + three HOD models | the 25 base boxes at z = 0.8 | — | BAO shift between HOD models | Mena-Fernández et al. 2024, arXiv:2404.03008 [src: abstract] |
| DESI DR1 peculiar velocities | DESI-PV mocks | BGS density and clustering at z < 0.1 with Fundamental Plane, Tully–Fisher and SN Ia distance errors | 675 realisations | data properties | tests of the three fσ8 methods and their correlations | Bautista et al. 2025, arXiv:2512.03228 [src: abstract] |
| DESI DR2 Lyα full shape | CoLoRe-2LPT | 2LPT quasars and Lyα skewers with HCDs and metals | count n/a | DESI Lyα measurements; quasars calibrated on AbacusSummit | validation of the Lyα BAO and full-shape analyses | Ruiz-Herrera Bernal et al. 2026, arXiv:2607.27412 [src] |
| Euclid | Flagship 2 galaxy mock | N-body + HOD and abundance matching | one light-cone: box 3600 Mpc/h, 16,000³ particles, m_p = 10⁹ M_⊙/h, softening 4.5 kpc/h, PKDGRAV3; full-sky particle light-cone to z = 3 by box replication (31 trillion particle outputs, about 125 billion ROCKSTAR haloes, lensing maps at HEALPix N_side = 8192); galaxies in one octant | observed luminosity functions and clustering | science-pipeline preparation; designed for the DR1 footprint of about 2500 deg² | Euclid Collaboration 2024, arXiv:2405.13495, section 2.1 [src] |

The Flagship 2 run started from 1LPT (Zel'dovich) initial conditions at z = 99, with linear radiation, neutrino and metric terms applied as a corrective particle-mesh force in the N-body gauge [src] (arXiv:2405.13495, section 2.1). This is worth knowing next to the transient results of `systematics.md` §2.

The BOSS mock sets (600 PTHalos mocks for DR9, arXiv:1203.6609; 12,288 MultiDark-Patchy light-cones for DR12, arXiv:1509.06400) and the WiggleZ COLA mocks (arXiv:1507.05329 [src: abstract of each]) are in `physics-and-methods.md` §12. DESI DR2 reference mocks built with subhalo abundance matching on Uchuu, and the DES and Euclid covariance mocks, are listed under "Not verified".

## 5. Constrained simulations of the local Universe
<!-- key: constrained-simulations-of-the-local-universe -->

| Project | Data constraining it | Inference method | Volume and resolution | Product | Headline statement | Reference, flag |
|---|---|---|---|---|---|---|
| CLUES (Cosmicflows-2) | radial peculiar velocities, Cosmicflows-2 | Wiener filter and constrained realisations | resembles the local Universe to 150 Mpc/h on scales of a few tens of Mpc, and down to a few Mpc (< 5 Mpc/h) in the inner part of the box | constrained N-body runs | cell-to-cell scatter 2–3 times smaller than random runs at 5 Mpc/h in the inner region; velocity scatter 104 ± 4 km/s | Sorce et al. 2015, arXiv:1510.04900 [src: abstract] |
| BORG 2M++ | 2M++ galaxy compilation (redshift-space positions) | BORG with a particle-mesh model | nearby Universe | posterior samples of initial conditions, density and velocity fields | detailed inference of the three-dimensional non-linear dark-matter distribution of the nearby Universe, with velocity fields and formation histories | Jasche & Lavaux 2018, arXiv:1806.11117 [src] |
| SIBELIUS-DARK | n/a (constraint data not named in the abstract) | constrained realisation, dark matter only, galaxies from GALFORM | to 200 Mpc from the Milky Way | public halo and galaxy catalogues | local volume has an unusually high number of very massive clusters and an underdensity of about 5% relative to the mean; rare but not in conflict with ΛCDM | McAlpine et al. 2022, arXiv:2202.04099 [src] |
| BORG posterior resimulations | galaxy counts (catalogue not named in the abstract) | BORG with 20-step COLA, then full N-body | Local Super-Volume, < 135 Mpc/h | masses of nearby massive clusters | mass functions compatible with ΛCDM | Stopyra et al. 2023, arXiv:2304.09193 [src] |
| Manticore-Local | 2M++ | BORG with a non-linear solver, refined bias model, physics-informed priors | local supervolume | suite of posterior resimulations ("digital twins") | no evidence for a large local underdensity; counterparts of 14 clusters within 1° of their sky positions at 2–4σ; highest Bayesian evidence on five peculiar-velocity data sets | McAlpine et al. 2025, arXiv:2505.10682 [src: abstract; Sect. 3.4.2] |
| Manticore-Deep | five galaxy redshift surveys over the SDSS and BOSS volumes | BORG, tiled inference | (4 Gpc/h)³ to z about 0.7 at about 4 Mpc/h | posterior ensemble of density and velocity fields | cross-correlation with Planck PR3 CMB lensing at 7.4σ; kSZ from velocity-weighted stacking of 64,750 clusters at 3.5σ; BOSS Great Wall an overdensity of about 3σ, consistent with ΛCDM | McAlpine et al. 2026, arXiv:2606.10020 [src: abstract] |
| Hamlet-PM on Cosmicflows-4 | peculiar velocities to z < 0.05 (160 Mpc/h) | field-level forward model with a particle-mesh solver, then high-precision N-body | 100 dark-matter-only runs, 512³ particles in (500 Mpc/h)³ | constrained ensemble | twelve nearby clusters matched in mass and separation, with environment-constrained mass estimates; the authors state the method already surpasses the pipeline in use in the peculiar-velocity community, with systematic biases still to be addressed | Valade et al. 2026, arXiv:2602.03699 [src: abstract] |
| TARDIS (mock data) | Lyα tomography at z about 2.5 (CLAMATO-, PFS-, ELT-like) | maximum likelihood with a fast non-linear model | tomographic volumes | initial density, z = 2.5 matter field, evolution to z = 0 | eigenvalues of the deformation tensor recovered at r = 0.95 for 30 m-class data | Horowitz et al. 2019, arXiv:1903.09049 [src: abstract] |

Earlier field-level projects now in the source list (`physics-and-methods.md` §9.2): ELUCID, the SDSS DR7 volume resimulated with 3072³ particles in 500 Mpc/h (Wang et al. 2016, arXiv:1608.01763); the 2MRS constrained runs of Heß et al. 2013 (arXiv:1304.6565), 25 runs in a 180 Mpc/h cube; the 2M++ Gaussian-step analysis (arXiv:1509.05040 [src: abstract of each]). Other projects whose abstracts were read during the first build and which lie outside the source list: HESTIA (Local Group zooms with magnetohydrodynamics), SLOW (a hydrodynamical run from Cosmicflows-2), the SIBELIUS Local Group study, a BORG-based Local Group inference, the BORG reconstruction of Quaia, and CSiBORG-Manticore scored against Planck Compton-y maps. Their sizes are not given here because their papers are not in the source list.

## 6. Neutrino and modified-gravity suites
<!-- key: neutrino-and-modified-gravity-suites -->

| Suite or exercise | Content | Reference, flag |
|---|---|---|
| Quijote | M_ν and w among the seven varied parameters; 44,100 boxes of 1 Gpc/h | arXiv:1909.05273 [src: abstract] |
| Mira-Titan | ω_ν and (w_0, w_a) in an eight-parameter design; 111 runs of 2.1 Gpc, 3200³ | arXiv:2207.12345 [src: abstract] |
| EuclidEmulator2 training set | Σm_ν and (w_0, w_a); neutrinos, photons, dark energy and metric evolved linearly in the N-body gauge | arXiv:2010.11288 [src] |
| Aemulus ν | neutrinos as particles up to 0.5 eV; 150 boxes of 1.05 Gpc/h | arXiv:2303.09762 [src: abstract] |
| FLAMINGO | 4 cosmology variations including different neutrino masses, with hydrodynamics; baseline one massive species of 0.06 eV; δf method | arXiv:2306.04024 [src: abstract; Sect. 2.2] |
| MillenniumTNG flagship N-body | 1.1 trillion dark-matter particles with massive neutrinos in (3000 Mpc)³ | arXiv:2210.10059 [src: abstract] |
| Dark Quest II | massive neutrinos and clustering dark energy by linear response; eight models so far | arXiv:2605.28581 [src] |
| Euclid neutrino code comparison | 11 N-body implementations, 2 approximate schemes, 4 predictors or emulators on common initial data | arXiv:2211.12457 [src: abstract] |
| Modified-gravity code comparison | f(R), DGP and symmetron runs from common initial conditions | arXiv:1506.06384 [src] |
| HalfDome | one run with local primordial non-Gaussianity, f_NL = 20 | arXiv:2407.17462 [src: abstract] |


## 7. Public access, status and what comes next
<!-- key: public-access-status-and-what-comes-next -->

**Where the data are, as stated in the papers read.**
- AbacusSummit: public release with light-cones, particle subsamples and halo catalogues at 33 epochs (arXiv:2110.11398 [src: abstract]).
- Uchuu: Data Release 1 on the Skies & Universes site; lensing maps and mock galaxy, cluster and AGN catalogues announced for later releases (arXiv:2007.14720).
- Quijote: about one petabyte of snapshots, halo and void catalogues and summary statistics (arXiv:1909.05273).
- IllustrisTNG: about 1.1 PB online with a web API and a JupyterLab interface (arXiv:1812.05609 [src: abstract]).
- Aemulus: halo catalogues and snapshots at AemulusProject.github.io (arXiv:1804.05865); Aemulus ν surrogate models released (arXiv:2303.09762).
- UNIT: unitsims.org (arXiv:1811.02111). HalfDome: 300 TB initial release, halfdomesims.github.io (arXiv:2407.17462 [src: abstract of each]).
- HACC runs (Frontier-E, Last Journey, Discovery, a 64-member hydrodynamic suite): the OpenCosmo portal, opencosmo.science, opened in 2026 (arXiv:2607.16059 [src: abstract]).
- Power-spectrum libraries for baryonic effects: powerlib.strw.leidenuniv.nl (arXiv:1906.00968) and the Horizon site (arXiv:1801.08559).
- Emulators: EuclidEmulator2 on GitHub (arXiv:2010.11288); BACCO at dipc.org/bacco (arXiv:2004.06245, arXiv:2011.15018); HMcode in CAMB (arXiv:2009.01858); pyspk (arXiv:2305.09710).
- Codes released with their papers: GADGET-4, SWIFT, DISCO-DJ, a 3LPT initial-condition generator (arXiv:2010.03567, arXiv:2305.13380, arXiv:2510.05206, arXiv:2008.09588).
- SIBELIUS-DARK: halo and galaxy catalogues at z = 0 (arXiv:2202.04099).

**Status at the snapshot.**
- DESI: DR1 analyses used the mock sets of §4; reference mocks for DR2 built with abundance matching on Uchuu and 2LPT Lyα mocks appeared in 2025–2026 (arXiv:2607.27412; the Uchuu papers are outside the source list).
- Euclid: Flagship 2 is the reference mock; no Euclid cosmological analysis is published (the sibling skills give mid-2027 for DR1 lensing and clustering products).
- Dark Quest II: first eight cosmologies run (arXiv:2605.28581).
- Constrained simulations: survey-depth reconstructions exist since 2026 (arXiv:2606.10020).

**Expected next (statements in the papers, not forecasts of ours).**
- Dark Quest II is planned as an emulator-scale ensemble (arXiv:2605.28581).
- Uchuu and HalfDome announce further data releases (arXiv:2007.14720, arXiv:2407.17462).
- The FLAMINGO authors call for a wider range of cosmology variations to confirm the weak cosmology dependence of the baryonic response (arXiv:2410.17109).

## Not verified
<!-- key: not-verified -->

- Codes of Millennium, Dark Quest, BACCO, HalfDome, Sherwood, Mira-Titan: the abstracts do not name them and the paper bodies were not read. (The review, arXiv:2112.05165 Sect. 8.5, attributes an L-GADGET-3 rerun of the Euclid comparison box to the BACCO authors.)
- Box sizes and particle numbers of Millennium, Dark Quest, Frontier-E, ANTILLES, OWLS, Horizon-AGN, Sherwood-Relics, and the LaCE and ForestFlow training suites.
- Public locations marked n/a.
- The identification of the two-trillion-particle PKDGRAV3 run with the first Euclid Flagship simulation is the review's; the abstract of arXiv:1609.08621 does not state it.
- Mock sets of DES, KiDS, HSC and Euclid covariance work; DESI DR2 EZmocks and abundance-matching mocks.
- Constrained-simulation projects named at the end of §5 without an identifier.
