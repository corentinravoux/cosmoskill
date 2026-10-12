# Code catalogue — one entry per code

Scope: the core catalogue of the cosmology software an analyst meets: what each code computes, its reference paper, repository, language and interface, licence, last release or activity read at the repository, and who uses it.

Snapshot: 2026-10-11

## How to read the tables

- **Repository** is the GitHub `owner/name`; the URL is `https://github.com/<owner>/<name>`. Every name below was returned by the GitHub API on 2026-10-11 [src: GitHub REST API].
- **Licence** is the SPDX identifier the GitHub API reports, or the licence string of the PyPI record. "custom" means the repository has a licence file that GitHub does not classify; "none detected" means the API reports no licence file. Neither is a legal statement: read the file before redistributing.
- **Release / activity** gives the latest PyPI release (version, upload date) where the code is on PyPI, and the date of the last push to the GitHub repository (any branch). All were read on 2026-10-11 [src: PyPI JSON API; GitHub REST API]. A push date is not a release date.
- **Users** lists only uses read this session in a cited paper, a docstring or a repository description. An empty cell means "not verified", not "unused".
- A code without a paper is cited by its repository and has no row in `sources.tsv`.

## 1. Boltzmann solvers and modified-gravity forks

| Code | Computes | Reference | Repository | Language, interface | Licence | Release / activity | Users |
|---|---|---|---|---|---|---|---|
| CAMB | Linear Einstein–Boltzmann solution: CMB TT/TE/EE/BB and lensing spectra, matter transfer functions and P(k), background distances; non-linear P(k) through halofit/HMcode variants | Lewis, Challinor & Lasenby 2000, arXiv:astro-ph/9911177; accuracy and massive-neutrino treatment in Howlett et al. 2012, arXiv:1201.3654; version 2 in Lewis 2026, arXiv:2607.14854 | `cmbant/CAMB` | Fortran core, Python package `camb` | custom | camb 2.0.4, 2026-08-25 (Python ≥ 3.10); GitHub release 2.0.3, 2026-08-24; last push 2026-09-25; the last v1.x release is v1.6.6 (arXiv:2607.14854) | Default transfer-function engine of pyccl (`transfer_function='boltzmann_camb'`) [src: pyccl 3.3.6 docstring]; a module of CosmoSIS (arXiv:1409.3409); one of the engines of cosmoprimo [src: cosmoprimo 1.0.0 docstring] |
| CLASS | Same scope as CAMB, written to be modular and with explicit precision control; non-cold relics with arbitrary phase-space distributions | Lesgourgues 2011, arXiv:1104.2932 (overview); Blas, Lesgourgues & Tram 2011, arXiv:1104.2933 (approximation schemes); Lesgourgues & Tram 2011, arXiv:1104.2935 (non-cold relics); comparison with CAMB in arXiv:1104.2934 | `lesgourg/class_public` | C core, Python wrapper `classy` | none detected | classy 3.4.1.0, 2026-10-05; last push 2026-10-04 | MontePython is "interfaced with the Boltzmann code class" (arXiv:1210.7183); default engine of the cosmoprimo DESI fiducial cosmology, and the code that produced the AbacusSummit initial power spectrum [src: cosmoprimo 1.0.0 `fiducial.DESI` docstring]; one of three engines of flip [src: flip docs] |
| EFTCAMB | CAMB patch implementing the effective field theory of dark energy and modified gravity: full linear perturbation dynamics with no quasi-static approximation, built-in stability checks (ghost, superluminality), phantom-divide crossing | Hu, Raveri, Frusciante & Silvestri 2013, arXiv:1312.5742; numerical notes arXiv:1405.3590; successor H-EFTCAMB (covariant Horndeski module, Cobaya integration) in Ye et al. 2026, arXiv:2603.01662 | `EFTCAMB/EFTCAMB` | Fortran, Python wrapper that is imported as `camb` | custom | not on PyPI; no tagged GitHub release; last push 2026-09-17. The README of the checkout read this session (commit of 2026-04-02) names the code "H-EFTCAMB" [src: repository README] | — |
| hi_class | CLASS extension to Horndeski scalar-tensor theories (quintessence, Brans–Dicke, f(R), covariant Galileons); second paper adds covariant-Lagrangian models, consistent initial conditions and an automated quasi-static approximation | Zumalacárregui et al. 2016, arXiv:1605.06102; Bellini, Sawicki & Zumalacárregui 2019, arXiv:1909.01828 | `hiclass-code/hi_class_public` (the older `miguelzuma/hi_class_public` redirects to it) | C, Python wrapper | none detected | not on PyPI as `hi_classy`; GitHub release v2.0 of 2019-09-11; last push 2026-09-16 | external validation reference for H-EFTCAMB (arXiv:2603.01662) |
| MGCLASS II | CLASS modification with parameterised deviations from General Relativity on sub-horizon scales and a subset of alternative theories; compatible with MontePython and Cobaya | Sakr & Martinelli 2021, arXiv:2112.14175 | not read | C | — | not read | — |
| MGCAMB | CAMB patch for phenomenological tests of gravity: μ, Σ, γ parameterisations of the modified Poisson and lensing equations, with massive neutrinos and dynamical dark energy; 2023 version adds cubic-spline reconstruction of μ, Σ and Ω_X, a Python wrapper and a Cobaya interface | Zhao et al. 2008, arXiv:0809.3791 (parameterisation); Hojjati, Pogosian & Zhao 2011, arXiv:1106.4543; Zucca et al. 2019, arXiv:1901.05956; Wang et al. 2023, arXiv:2305.05667 | `sfu-cosmo/MGCAMB` (repository created 2023-10-27) | Fortran, Python wrapper | custom | not on PyPI; last push 2025-11-07 | — |
| DISCO-EB | Differentiable linear Einstein–Boltzmann solver in JAX (the Einstein–Boltzmann module of DISCO-DJ); Jacobians of all outputs with respect to all inputs | Hahn, List & Porqueres 2023, arXiv:2311.03291 | `ohahn/DISCO-EB` | Python (JAX) | GPL-3.0 | last push 2025-11-13 | — |
| SymBoltz.jl | "A symbolic-numeric, approximation-free and differentiable linear Einstein-Boltzmann solver" [src: repository description]; Chebyshev interpolation in k and ℓ | Sletmoen 2026, arXiv:2608.24682 (the interpolation method; a dedicated code paper was not read) | `hersle/SymBoltz.jl` | Julia | MIT | last push 2026-10-09 | — |
| class_sz | C and Python code for cross-survey observables: halo model, LSS and CMB, with machine-learning acceleration | Bolliet et al. 2023, arXiv:2310.18482 | `CLASS-SZ/class_sz` | C, Python | MIT | classy_sz 0.1.70.post40, 2025-12-12; last push 2026-08-07 | — |
| HMcode (inside CAMB and CLASS) | Augmented halo-model fit for the non-linear matter power spectrum, with BAO damping, massive neutrinos and a six-parameter baryonic-feedback model | Mead et al. 2020, arXiv:2009.01858 | shipped with CAMB (`halofit_version='mead2020'` is the CAMB 2.0.4 default) | — | — | — | — |
| halofit (Takahashi) | Revised halofit fitting formula for the non-linear matter power spectrum | Takahashi et al. 2012, arXiv:1208.2701 | shipped with CAMB (`halofit_version='takahashi'`) and pyccl (`matter_power_spectrum='halofit'`, the pyccl default) | — | — | — | — |

## 2. Theory facades

| Code | Computes | Reference | Repository | Language, interface | Licence | Release / activity | Users |
|---|---|---|---|---|---|---|---|
| cosmoprimo | One Python `Cosmology` object in front of several engines (`class`, `camb`, `eisenstein_hu`, `eisenstein_hu_nowiggle`, `bbks`; optional `isitgr`), returning background, thermodynamics, primordial, transfer, harmonic and Fourier sections; FFTLog-based transforms; fiducial cosmologies `DESI`, `AbacusSummit`, `BOSS`, `Planck2018FullFlatLCDM` | no paper; cite the repository | `cosmodesi/cosmoprimo` | Python; the `class` engine goes through the separate wrapper `pyclass` (`adematti/pyclass`) [src: cosmoprimo 1.0.0 package metadata] | BSD-3-Clause | not on PyPI (installed from GitHub); version 1.0.0 read in the installed package; last push 2026-10-06 | DESI (hosted in the `cosmodesi` organisation); one of three engines of flip [src: flip docs] |
| pyccl (CCL) | Distances, growth, linear and non-linear P(k), halo mass function and bias, halo model, angular power spectra (Limber and non-Limber) and correlation functions, with documented numerical accuracy | Chisari et al. 2018, arXiv:1812.05995 | `LSSTDESC/CCL` | C library with Python interface `pyccl` | BSD-3-Clause | pyccl 3.3.6, 2026-07-28 (Python ≥ 3.10); last push 2026-10-03 | Rubin LSST DESC (the paper's stated purpose); one of three engines of flip [src: flip docs] |
| astropy.cosmology | FLRW background only: distances, ages, H(z), densities, with units attached; built-in realisations WMAP1/3/5/7/9, Planck13/15/18 | Astropy Collaboration 2013, arXiv:1307.6212; Astropy Collaboration 2022, arXiv:2206.14220 | `astropy/astropy` | Python | BSD-3-Clause | astropy 8.0.1, 2026-07-05 (Python ≥ 3.11); last push 2026-10-10 | general astronomy; LensTools builds on it (arXiv:1606.01903) |
| jax-cosmo | Differentiable background, linear and halofit P(k) with the Eisenstein–Hu transfer function, Limber angular spectra for clustering and lensing | Campagne et al. 2023, arXiv:2302.05163 | `DifferentiableUniverseInitiative/jax_cosmo` | Python (JAX) | MIT | jax-cosmo 0.1.0, 2023-02-05; last push 2025-06-27 | — |
| cloelib | "Library of theoretical model predictions for photometric and spectroscopic large-scale structure observables" [src: repository description], with JAX automatic differentiation and interfaces to Boltzmann solvers | Bonici et al. 2026, arXiv:2605.23839; validation of the CLOE likelihood in Euclid Collaboration 2025, arXiv:2510.09141 | `cloe-org/cloelib` | Python (JAX) | MIT | last push 2026-10-12 | Euclid: intended reference theory code for its first cosmological release (arXiv:2605.23839) |

## 3. Samplers and inference frameworks

### 3.1 Frameworks (theory code + likelihoods + samplers)

| Code | Computes | Reference | Repository | Language, interface | Licence | Release / activity | Users |
|---|---|---|---|---|---|---|---|
| Cobaya | General Bayesian analysis framework: parameter blocking by speed, caching of intermediate results, several samplers, maximisation and importance reweighting; interfaces to Boltzmann codes and likelihoods | Torrado & Lewis 2020, arXiv:2005.05290 | `CobayaSampler/cobaya` | Python, YAML or dictionary input | custom | cobaya 3.6.2, 2026-03-27 (Python ≥ 3.10); last push 2026-08-25 | MGCAMB ships a Cobaya interface (arXiv:2305.05667) |
| CosmoMC | Fortran Metropolis–Hastings sampler coupled to CAMB; fast–slow parameter decorrelation and dragging | Lewis & Bridle 2002, arXiv:astro-ph/0205436; Lewis 2013, arXiv:1304.4473 | `cmbant/CosmoMC`; see `open-questions.md` for its status | Fortran | none detected | last push 2022-01-14 | The EFTCAMB and MGCAMB patches were first released for CosmoMC (arXiv:1405.3590, arXiv:1106.4543) |
| MontePython | Parameter inference code interfaced with CLASS; version 3 adds jumping-factor adaptation and a Fisher-matrix proposal | Audren et al. 2012, arXiv:1210.7183; Brinckmann & Lesgourgues 2018, arXiv:1804.07261 | `brinckmann/montepython_public` | Python | MIT | not on PyPI; last push 2024-06-20 | — |
| CosmoSIS | Modular parameter-estimation framework: a pipeline of interchangeable modules (CAMB, Planck likelihoods, cosmic-shear calculations) and a suite of samplers | Zuntz et al. 2014, arXiv:1409.3409 | `cosmosis-developers/cosmosis` (the older `joezuntz/cosmosis` redirects to it; the Bitbucket URL in the paper abstract is historical) | Python core, modules in C, Fortran or Python | custom | cosmosis 3.26, 2026-09-03; last push 2026-09-24 | DES: the Y3 sampler study uses the full DES Y1 likelihood (arXiv:2202.08233) |
| desilike | "Cosmological Inference Framework Used by the Dark Energy Spectroscopic Instrument (DESI)" [src: repository description]: likelihoods for BAO and RSD analyses, wrappers of velocileptors, pybird and FOLPS-nu, Taylor-expansion and MLP emulators, ShapeFit, samplers and profile-likelihood tools, bindings to Cobaya, CosmoSIS and MontePython [src: repository README] | no paper and no citation request in the README; cite the repository | `cosmodesi/desilike` | Python, optional JAX | BSD-3-Clause | not on PyPI (`pip install git+https://github.com/cosmodesi/desilike`); no tagged release; last push 2026-10-09 | DESI |

### 3.2 Samplers

| Code | Method | Reference | Repository | Licence | Release / activity | Users |
|---|---|---|---|---|---|---|
| emcee | Affine-invariant ensemble MCMC (Goodman & Weare stretch move) | Foreman-Mackey et al. 2012, arXiv:1202.3665 | `dfm/emcee` | MIT | emcee 3.1.6, 2024-04-19; last push 2026-10-05 | MCMC backend of flip [src: flip docs, "MCMC (emcee)"]; LensTools (arXiv:1606.01903) |
| dynesty | Static and dynamic nested sampling | Speagle 2019, arXiv:1904.02180 | `joshspeagle/dynesty` | MIT | dynesty 3.1.0, 2026-07-17; last push 2026-10-11 | — |
| MultiNest | Ellipsoidal multimodal nested sampling | Feroz, Hobson & Bridges 2008, arXiv:0809.3437 | `farhanferoz/MultiNest`; Python access through `pymultinest` | none detected (Fortran repository); pymultinest GPLv3 | pymultinest 2.12, 2023-07-28; last push of the Fortran repository 2022-03-01 | DES Y1 analyses (arXiv:2202.08233) |
| PolyChord | Nested sampling with slice sampling inside the likelihood constraint; exploits a hierarchy of parameter speeds | Handley, Hobson & Lasenby 2015, arXiv:1502.01856 and arXiv:1506.00171 | `PolyChord/PolyChordLite` | custom | GitHub release 1.22.2, 2025-11-25; last push 2026-02-26; the PyPI record `pypolychord` is stale (1.15.1, 2019-01-17) | DES Y3 baseline sampler (arXiv:2202.08233); interfaced in Cobaya [src: Cobaya docs via context7] and in Vega [src: Vega README] |
| nautilus | Importance nested sampling with neural-network regression for the proposal | Lange 2023, arXiv:2306.16923 | `johannesulf/nautilus` | MIT | nautilus-sampler 1.0.6, 2025-12-29; last push 2026-08-18 | DES Y6 and KiDS-Legacy [sec: sibling skill `cosmo-statistics-inference`] |
| pocoMC | Preconditioned Monte Carlo: normalising-flow preconditioning plus sequential Monte Carlo | Karamanis et al. 2022, arXiv:2207.05652 | `minaskar/pocomc` | GPL-3.0 | pocomc 1.2.6, 2024-09-20; last push 2025-09-11 | sampler interface in Vega [src: Vega README] |
| NumPyro | Probabilistic programming on JAX; JIT-compiled iterative NUTS | Phan, Pradhan & Jankowiak 2019, arXiv:1912.11554; NUTS itself in Hoffman & Gelman 2011, arXiv:1111.4246 | `pyro-ppl/numpyro` | Apache-2.0 | numpyro 0.22.0, 2026-09-18 (Python ≥ 3.11); last push 2026-10-10 | — |
| BlackJAX | Library of composable sampling and variational-inference kernels on JAX, working on an un-normalised log-density | Cabezas et al. 2024, arXiv:2402.10797 | `blackjax-devs/blackjax` | Apache-2.0 | blackjax 1.7.1, 2026-10-02 (Python ≥ 3.11); last push 2026-10-08 | — |
| iminuit | Python front-end to MINUIT2 (minimisation, HESSE and MINOS errors) | no paper cited here | PyPI `iminuit` | — | iminuit 2.33.0, 2026-09-17 | minimiser of flip [src: flip docs, "Maximum likelihood (Minuit)"] and of Vega [src: Vega README] |

### 3.3 Chain analysis

| Code | Computes | Reference | Repository | Release / activity |
|---|---|---|---|---|
| GetDist | Kernel-density marginalised 1D and 2D densities from weighted, correlated samples; convergence diagnostics; tables and triangle plots | Lewis 2019, arXiv:1910.13970 | `cmbant/getdist` | getdist 1.7.7, 2026-05-08; last push 2026-08-05 |
| anesthetic | Nested-sampling post-processing | no paper cited here | `handley-lab/anesthetic` (PyPI record) | anesthetic 2.16.0, 2026-08-31 |

Other samplers with a PyPI record read this session, not researched further: `ultranest` 4.5.2 (2026-09-19; repository `JohannesBuchner/UltraNest`, last push 2026-10-11) and `zeus-mcmc` 2.5.4 (2023-01-12).
A JAX-based GPU nested-sampling framework is demonstrated in Lovick et al. 2025, arXiv:2509.13307, and a TensorFlow package of batched samplers for emulated likelihoods, BEST, in Nygaard et al. 2026, arXiv:2606.04895 (PyPI name `best-inference` according to the abstract; not queried).

## 4. Perturbation-theory codes

| Code | Computes | Reference | Repository | Language | Licence | Release / activity | Users |
|---|---|---|---|---|---|---|---|
| velocileptors | One-loop redshift-space power spectrum and correlation function of biased tracers in Lagrangian and Eulerian perturbation theory, through velocity-moment expansions and a fully resummed LPT model, with counterterms and stochastic terms | Chen, Vlah & White 2020, arXiv:2005.00523; Chen, Vlah, Castorina & White 2020, arXiv:2012.04636 | `sfschen/velocileptors` | Python (numpy, scipy, pyFFTW) | MIT | velocileptors 3.1, 2026-04-23; last push 2026-04-23 | DESI DR1 full-shape pipeline validation (Maus et al. 2024, arXiv:2404.07312); wrapped in desilike [src: desilike README] |
| CLASS-PT | One-loop auto- and cross-spectra of matter and biased tracers in real and redshift space inside CLASS: non-linear bias, RSD, infrared resummation, counterterms, Alcock–Paczynski | Chudaykin, Ivanov, Philcox & Simonović 2020, arXiv:2004.10607 | `Michalychforever/CLASS-PT` | C (fork of CLASS) | none detected | GitHub release v2.0, 2022-01-15 ("CLASS-PT with Equilateral and Orthogonal fNL"); last push 2026-09-18 | BOSS full-shape analysis in the reference paper |
| CLASS-OneLoop | One-loop power spectrum of biased tracers inside CLASS, Eulerian moment expansion, loops by direct integration or FFT, fast–slow parameter decomposition | Linde et al. 2024, arXiv:2402.09778 | not read | C (inside CLASS) | — | not read | — |
| PyBird | One-loop EFTofLSS power spectrum of biased tracers in redshift space | D'Amico, Senatore & Zhang 2020, arXiv:2003.07956 | `pierrexyz/pybird` | Python | MIT | pybird-lss 0.3.2, 2025-08-02; last push 2026-05-13 | DESI DR1 validation (Lai et al. 2024, arXiv:2404.07283); wrapped in desilike [src: desilike README] |
| PyBird-JAX | Differentiable JAX implementation of PyBird with internal neural-network emulators | Reeves, Zhang & Zheng 2025, arXiv:2507.20990 | not read (no repository `pierrexyz/pybird-jax` exists) | Python (JAX) | — | not read | — |
| FOLPSν | One-loop redshift-space power spectrum with kernels beyond Einstein–de Sitter, for massive neutrinos; FFTLog evaluation | Noriega et al. 2022, arXiv:2208.02791 | `henoriega/FOLPS-nu`; JAX version `cosmodesi/folpsax` | Python | none detected | last push 2025-06-22 (`FOLPS-nu`), 2024-09-10 (`folpsax`) | DESI DR1 validation (Noriega et al. 2024, arXiv:2404.07269) |
| FAST-PT | FFT-based evaluation of one-loop mode-coupling integrals (SPT, renormalisation-group); version II extends to tensor quantities: intrinsic alignments, Ostriker–Vishniac, redshift-space one-loop P(k) | McEwen et al. 2016, arXiv:1603.04826; Fang et al. 2016, arXiv:1609.05978 | `jablazek/FAST-PT` (PyPI homepage; created 2023-10-20); original `JoeMcEwen/FAST-PT` | Python | MIT | fast-pt 4.1.0, 2026-09-23; last push 2026-10-10 (`jablazek`), 2024-07-26 (`JoeMcEwen`) | — |
| elf | One-loop galaxy power spectrum in Eulerian and Lagrangian perturbation theory, automatically differentiable | Kobayashi & Akitsu 2026, arXiv:2610.08023 | "publicly available" per the abstract; URL not read | Python (JAX) | — | not read | — |
| neckar | One-loop matter and galaxy power spectrum and correlation function in the Eulerian EFTofLSS, FFTLog-based, with bootstrap kernels | Harder et al. 2026, arXiv:2610.03466 | "public code" per the abstract; URL not read | C with Python wrapper | — | not read | — |
| Effort.jl | Emulator of the EFTofLSS galaxy power spectrum, validated against PyBird | Bonici et al. 2025, arXiv:2501.04639 | `CosmologicalEmulators/Effort.jl` | Julia | MIT | last push 2026-08-30 | — |

The configuration-space counterpart for DESI DR1 (Gaussian streaming model with convolution Lagrangian perturbation theory and EFT terms) is validated in Ramirez-Solano et al. 2024, arXiv:2404.07268.
The three Fourier-space codes are compared with each other in Maus et al. 2024, arXiv:2404.07272; an earlier blinded test of two EFT implementations is Nishimichi et al. 2020, arXiv:2003.08277, which the velocileptors README also asks users to cite.

## 5. Two-point and higher-order estimators

| Code | Computes | Reference | Repository | Language | Licence | Release / activity | Users |
|---|---|---|---|---|---|---|---|
| pypower | Auto- and cross-power-spectrum multipoles and the associated window functions, for periodic boxes and survey geometry, plane-parallel or with first odd wide-angle corrections [src: repository README] | no paper; cite the repository | `cosmodesi/pypower` | Python on `pmesh`, MPI | BSD-3-Clause | not on PyPI (README: install from GitHub); version 1.0.0 read in a checkout; last push 2026-03-27 | DESI (hosted in `cosmodesi`) |
| pycorr | "2-pt correlation function estimation" [src: repository description]: θ, s, (s, μ) and (r_p, π) binning, PIP and angular weights, analytical counts for periodic boxes, jackknife covariance, MPI [src: repository README] | no paper; the README asks users of pycorr with Corrfunc to cite the Corrfunc papers (arXiv:1911.03545) | `cosmodesi/pycorr` | Python wrapper of Corrfunc (cosmodesi fork, `desi` branch) | BSD-3-Clause | no tagged release; last push 2026-01-13. The PyPI package named `pycorr` is an unrelated project | DESI (hosted in `cosmodesi`); supplies pairwise weights to pypower [src: pypower docstring] |
| pyrecon | "package for BAO reconstruction" [src: repository description] | no paper; cite the repository | `cosmodesi/pyrecon` | Python | BSD-3-Clause | last push 2026-09-17. The PyPI package named `pyrecon` is an unrelated project | DESI (hosted in `cosmodesi`) |
| nbodykit | MPI-parallel toolkit: power spectrum, two- and three-point correlation functions, friends-of-friends, HOD mocks, FastPM | Hand et al. 2017, arXiv:1712.05834 | `bccp/nbodykit` | Python, MPI | GPL-3.0 | nbodykit 0.3.16, 2025-08-14; last push 2025-11-07 | — |
| TreeCorr | Tree-based two- and three-point correlation functions of counts, scalars and shear | Jarvis, Bernstein & Jain 2003, arXiv:astro-ph/0307393 (the tree algorithm) | `rmjarvis/TreeCorr` | Python with C++ core | custom (PyPI: BSD) | TreeCorr 5.1.4, 2026-09-01; last push 2026-09-01 | — |
| NaMaster | Pseudo-C_ℓ angular power spectra of any pair of spin-0 or spin-2 fields, with contaminant deprojection and E/B purification, curved or flat sky | Alonso, Sanchez & Slosar 2018, arXiv:1809.09603 | `LSSTDESC/NaMaster` | C with Python interface `pymaster` | BSD-3-Clause | pymaster 3.0.1, 2026-08-04 (Python ≥ 3.10); last push 2026-08-05 | Rubin LSST DESC |
| Corrfunc | OpenMP pair counting: ξ(r), w_p, ξ(r_p, π), ξ(s, μ), angular w(θ), on boxes and on the sky | Sinha & Garrison 2019, arXiv:1911.03545 | `manodeep/Corrfunc` | C with Python interface | MIT | Corrfunc 2.5.3, 2024-08-06; last push 2026-08-16 | — |
| Triumvirate | Three-point correlation function and bispectrum multipoles in the tri-polar spherical-harmonic decomposition; two-point statistics for completeness | Wang, Beutler & Sugiyama 2023, arXiv:2304.03643 | `MikeSWang/Triumvirate` | C++ with Python interface | GPL-3.0 | Triumvirate 0.5.0, 2024-08-09 (Python ≥ 3.10); last push 2026-10-08 | — |

## 6. Lyman-alpha tools

| Code | Computes | Reference | Repository | Language | Licence | Release / activity | Users |
|---|---|---|---|---|---|---|---|
| picca | "set of tools for continuum fitting, correlation function calculation, cosmological fits" [src: repository description]: flux-transmission field (deltas), auto- and cross-correlations with their distortion and metal matrices, P1D | du Mas des Bourboux et al. 2020, arXiv:2007.08995 (the eBOSS DR16 Lyα BAO paper, which releases the code) | `igmhub/picca` | Python | GPL-3.0 | picca 9.21.1, 2026-10-05 (Python ≥ 3.11); last push 2026-10-09 | eBOSS DR16 (arXiv:2007.08995); DESI Lyα analyses (sibling skill `cosmo-lyman-alpha`) |
| Vega | "Lyman-alpha forest correlation function modeling and analysis" [src: repository description]: 3D correlation-function and power-spectrum models and fits, based on picca `fitter2`; minimiser iminuit, sampler interfaces to PolyChord and pocoMC [src: repository README] | the README asks for a link to the repository and names as best descriptions Cuceu et al. 2022 (DOI 10.1093/mnras/stad1546; on arXiv as arXiv:2209.12931, see `Not verified`) and Cuceu et al. 2025, arXiv:2509.15308 | `andreicuceu/vega` (default branch `master`) | Python ≥ 3.11 | GPL-3.0 | GitHub release v1.8.0, 2026-10-10; installed from the release wheel, not from PyPI; last push 2026-10-10 | Lyα auto- and cross-correlations, metal, DLA and SBLA analyses, DESI BAO and full-shape analyses [src: repository README]; pipeline validation in Cuceu et al. 2024, arXiv:2404.03004 |
| LaCE | "Emulator for the one-dimensional Lyman-alpha flux power spectrum" [src: repository description]: Gaussian-process and neural-network emulators of P1D as a function of the amplitude and slope of the linear power spectrum and of the IGM state | Pedersen et al. 2020, arXiv:2011.15127; Cabayol-Garcia et al. 2023, arXiv:2305.19064 | `igmhub/LaCE` | Python | none detected | last push 2026-10-07. The PyPI package named `lace` is an unrelated project | — |
| lym1d | Likelihood framework for the Lyα P1D with a Gaussian-process emulator built on the Lyssa suite of Nyx simulations | Walther et al. 2024, arXiv:2412.05372 | `schoeneberg/lym1d` (repository of that name returned by the GitHub API; its link to the paper was not read) | Python (notebooks) | none detected | last push 2026-06-15 | eBOSS DR14 P1D constraints in the reference paper |
| ForestFlow | "neural network emulator for the 3D flux power spectrum of the Lyman-alpha forest" [src: repository description], using conditional normalising flows | Chaves-Montero et al. 2024, arXiv:2409.05682 | `igmhub/ForestFlow` | Python | none detected | last push 2026-10-11 | — |

The picca README gives du Mas des Bourboux et al. 2020 as "the current reference" and states that picca v4.0 produced that measurement [src: picca README, checkout]. The picca facts in this file were read at version 9.21.0, in a development state of the repository, not a tagged release.

## 7. Lensing and sphere tools

| Code | Computes | Reference | Repository | Language | Licence | Release / activity | Users |
|---|---|---|---|---|---|---|---|
| HEALPix / healpy | Equal-area iso-latitude pixelisation of the sphere and fast spherical-harmonic transforms; `healpy` is the Python package | Górski et al. 2004, arXiv:astro-ph/0409513 | `healpy/healpy` | Python with C++ core | GPL-2.0 | healpy 1.20.1, 2026-10-03 (Python ≥ 3.10); last push 2026-10-04 | CMB and LSS map analysis in general; NaMaster works on HEALPix maps |
| LensTools | Weak-lensing simulation pipeline (ray-tracing with external CAMB and Gadget2 runs), feature measurement (peaks, moments, power spectra), parameter sampling | Petri 2016, arXiv:1606.01903 | `apetri/LensTools` | Python | MIT (PyPI record) | lenstools 1.2, 2021-01-21; last push 2025-06-29 | — |

Shear two-point functions are measured with TreeCorr (section 5) and pseudo-C_ℓ with NaMaster (section 5); CMB likelihood codes are in section 8 (candl) and in the sibling `cosmo-cmb`.

## 8. Differentiable and field-level codes

| Code | Computes | Reference | Repository | Language | Licence | Release / activity | Users |
|---|---|---|---|---|---|---|---|
| flip | Likelihood-based field-level inference of fσ8 from velocity and density fields: fast covariance of the fields from model power spectra (several analytical models, with wide-angle terms), Gaussian likelihood, Minuit and emcee fits, Fisher forecasts | Ravoux et al. 2025, arXiv:2501.16852; the README asks to cite also Carreres et al. 2023, arXiv:2303.01198, on which the package was started | `corentinravoux/flip` (PyPI name `flipcosmo`; documentation at flip.readthedocs.io) | Python, optional JAX | MIT | flipcosmo 2.0.10, 2026-09-09 (Python ≥ 3.10); last push 2026-09-30 | peculiar-velocity analyses (sibling skill `cosmo-peculiar-velocities`) |
| BORG | Bayesian reconstruction of the initial density field from galaxy surveys with a physical forward model (2LPT in the first paper, particle-mesh in the 2018 paper) sampled by Hamiltonian Monte Carlo | Jasche & Wandelt 2012, arXiv:1203.3639; Jasche & Lavaux 2018, arXiv:1806.11117 | `git.aquila-consortium.org/Aquila-Consortium/borg_public` [sec: web search snippets; see `Not verified`] | not read | not read | release branch 2.1 [sec] | Aquila consortium analyses (siblings `cosmo-beyond-two-point`, `cosmo-simulations-mocks`) |
| pmwd | Differentiable particle-mesh N-body with the adjoint method (reverse time integration, low memory) | Li et al. 2022, arXiv:2211.09958 | `eelregit/pmwd` | Python (JAX) | BSD-3-Clause | no PyPI record named `pmwd`; last push 2026-06-12 | — |
| JaxPM | "JAX-powered Cosmological Particle-Mesh N-body Solver" [src: repository description] | no paper; cite the repository | `DifferentiableUniverseInitiative/JaxPM` | Python (JAX) | MIT | jaxpm 0.1.6, 2025-06-29; last push 2026-09-28 | — |
| DISCO-DJ | Differentiable particle-mesh N-body module of the DISCO-DJ package: theory-informed time integrators (BullFrog), non-uniform FFT forces, forward- and reverse-mode differentiation | List et al. 2025, arXiv:2510.05206; Einstein–Boltzmann module in arXiv:2311.03291 | `cosmo-sims/DISCO-DJ` (created 2025-09-23) | Python (JAX) | GPL-3.0 | last push 2026-05-16 | — |
| FlowPM | Differentiable, distributed particle-mesh solver in TensorFlow (FastPM scheme) | Modi, Lanusse & Seljak 2020, arXiv:2010.11847 | `modichirag/flowpm` (URL given in the paper abstract) | Python (TensorFlow) | MIT | last push 2021-04-25 | — |
| candl | Differentiable CMB power-spectrum likelihood in JAX, shipped with SPT and ACT data | Balkenhol et al. 2024, arXiv:2401.13433 | `Lbalkenhol/candl` | Python (JAX) | MIT | candl-like 2.2.0, 2025-10-10; last push 2026-06-05 | — |

## 9. Emulators

Emulators of N-body and hydrodynamical quantities (halo mass function, non-linear P(k), baryonic suppression) belong to the sibling `cosmo-simulations-mocks`. The entries here replace a Boltzmann or perturbation-theory code inside an inference pipeline.

| Code | Emulates | Reference | Repository | Language | Licence | Release / activity |
|---|---|---|---|---|---|---|
| CosmoPower | Matter power spectrum and CMB temperature, polarisation and lensing-potential spectra from a Boltzmann code, with neural networks | Spurio Mancini et al. 2021, arXiv:2106.03846 | `alessiospuriomancini/cosmopower` | Python (TensorFlow) | GPL-3.0 | cosmopower 0.2.0, 2024-07-28; last push 2024-12-21 |
| CosmoPower-JAX | JAX implementation of CosmoPower for gradient-based sampling | Piras & Spurio Mancini 2023, arXiv:2305.06347 | `dpiras/cosmopower-jax` | Python (JAX) | GPL-3.0 | cosmopower-jax 0.5.8, 2025-11-28; last push 2025-11-27 |
| CosmoPower emulator sets | High-accuracy emulators of CMB spectra, P(k), distances, BAO and RSD observables for ΛCDM, wCDM, N_eff and Σm_ν models (Bolliet et al. 2023, arXiv:2303.01591); packaging standard and CAMB-based emulators (Jense et al. 2024, arXiv:2405.07903) | same | "CosmoPower Organisation" repository named in arXiv:2303.01591; URL not read | Python | — | not read |
| Capse.jl | CMB temperature, polarisation and lensing spectra | Bonici, Bianchini & Ruiz-Zapatero 2023, arXiv:2307.14339 | `CosmologicalEmulators/Capse.jl` | Julia | MIT | last push 2026-09-28 |
| Effort.jl | EFTofLSS galaxy power spectrum (see section 4) | Bonici et al. 2025, arXiv:2501.04639 | `CosmologicalEmulators/Effort.jl` | Julia | MIT | last push 2026-08-30 |
| LaCE | Lyα P1D (see section 6) | arXiv:2011.15127, arXiv:2305.19064 | `igmhub/LaCE` | Python | none detected | last push 2026-10-07 |

## 10. Installation names that differ from the code name

| Code | Import or package name | Where it installs from | Flag |
|---|---|---|---|
| CLASS | `classy` | PyPI | [src: PyPI] |
| NaMaster | `pymaster` | PyPI | [src: PyPI] |
| flip | `flipcosmo` (import `flip`) | PyPI | [src: PyPI; flip checkout] |
| nautilus | `nautilus-sampler` | PyPI | [src: PyPI] |
| PyBird | `pybird-lss` | PyPI | [src: PyPI] |
| candl | `candl-like` | PyPI | [src: PyPI] |
| FAST-PT | `fast-pt` | PyPI | [src: PyPI] |
| class_sz | `classy_sz` | PyPI | [src: PyPI] |
| cosmoprimo with CLASS | `pyclass`, repository `adematti/pyclass` (last push 2026-07-06) | GitHub | [src: cosmoprimo metadata; GitHub API] |
| cosmoprimo, desilike, pypower, pycorr, pyrecon | same as the code | GitHub organisation `cosmodesi` | [src: GitHub API; READMEs of pypower and desilike; cosmoprimo package metadata] |
| EFTCAMB / H-EFTCAMB | `camb` (shadows CAMB) | GitHub, compiled locally | [src: repository README] |
| Vega | `vega` | wheel from GitHub Releases | [src: repository README] |

## Not verified

- BORG: the repository address comes from web-search snippets of the Aquila consortium Git server; the live page, its licence and its language were not read.
- The licences marked "custom" and "none detected" were not opened.
- "Users" cells left empty were not researched; they do not mean the code is unused.
- Vega: the README cites its first reference by DOI (10.1093/mnras/stad1546); that this is the journal version of arXiv:2209.12931 was inferred from author, year and subject.
- Repository URLs of MGCLASS II, CLASS-OneLoop, PyBird-JAX, `elf`, `neckar` and of the CosmoPower emulator organisation were not read.
- lym1d: that `schoeneberg/lym1d` is the code of arXiv:2412.05372 was inferred from the name and from the author list of the paper.
- A dedicated code paper for SymBoltz.jl was not searched for.
- The DESI papers that state which estimator codes (pypower, pycorr, pyrecon) produced the published measurements were not read; "DESI" in the Users column rests on the hosting organisation and READMEs.
