# Code families — what each does and how the members differ

Scope: what each family of cosmology codes computes, the method each member uses, and the differences that matter when choosing or comparing them.

Snapshot: 2026-10-14

Provenance of API facts: "installed" means the docstring or signature was read in the released package at the stated version (camb 2.0.4, pyccl 3.3.6, astropy 8.0.1, healpy 1.19.0, emcee 3.1.6, cosmoprimo 1.0.0). "checkout" means the source repository was read at the stated version or commit (CLASS v3.2.3, pypower 1.0.0, EFTCAMB commit of 2026-04-02; picca and flip at a development state, not a release, so their facts should be re-read in the release in use). "context7" means library documentation fetched through the context7 documentation service on 2026-10-11. The installed versions were re-read on 2026-10-26 [doc: installed camb 2.0.4, pyccl 3.3.6, astropy 8.0.1, healpy 1.19.0, emcee 3.1.6, cosmoprimo 1.0.0; lesgourg/class_public/explanatory.ini at tag v3.2.3; cosmodesi/pypower/pypower/_version.py, 2026-10-26].

## 1. Boltzmann solvers and their modified-gravity forks
<!-- key: boltzmann-solvers-and-their-modified-gravity -->

### 1.1 What the family computes
<!-- key: what-the-family-computes -->

An Einstein–Boltzmann solver integrates the linearised Einstein and Boltzmann equations for photons, baryons, cold dark matter, neutrinos and dark energy, and returns transfer functions, the CMB angular power spectra and the linear matter power spectrum.
Every downstream code in this skill (facades, perturbation theory, emulators, likelihood frameworks) consumes its output.
The two reference implementations are CAMB (Lewis, Challinor & Lasenby 2000, arXiv:astro-ph/9911177) and CLASS (Lesgourgues 2011, arXiv:1104.2932).

Foundations of the family:

- **Line-of-sight integration** (Seljak & Zaldarriaga 1996, arXiv:astro-ph/9603033): the temperature anisotropy is a time integral of a model-independent geometrical term (radial eigenfunctions, precomputable) times a source term built from photon, baryon and metric perturbations; the source varies slowly with wavenumber and is evaluated at few points, which is where the speed-up comes from [src]. CAMB implements this method and extended it to closed models (arXiv:astro-ph/9911177) [src].
- **Equations and gauges** (Ma & Bertschinger 1995, arXiv:astro-ph/9506072): linear scalar perturbations of CDM, baryons, photons, massless and massive neutrinos in the synchronous and conformal Newtonian gauges, with a phase-space treatment of neutrinos and isentropic super-horizon initial conditions [src].

Conventions read in the code papers:

| Aspect | CAMB v2 | CLASS |
|---|---|---|
| Units and time | conformal time, megaparsec units [src: arXiv:2607.14854, Sect. II] | — |
| Gauge | covariant equations in the zero-acceleration (CDM) frame, "equivalent to the synchronous gauge"; `camb.symbolic` projects them into Newtonian or synchronous gauge and maps each symbol to a code variable [src: arXiv:2607.14854, Sect. II] | — |
| Lensed spectra | all-sky correlation-function method | same method as CAMB, different numerical implementation based on quadrature weights [src: arXiv:1104.2934, Sect. 2.2] |
| Precision control | boost hierarchy: `AccuracyBoost`, `lSampleBoost`, `lAccuracyBoost`, sub-boosts, and `lens_potential_accuracy` [src: arXiv:2607.14854, App. C] | separate precision file (`cl_ref.pre`, `pk_ref.pre`, `cl_permille.pre`, …) passed after the parameter file; parameters declared in `include/common.h` [src: arXiv:1104.2934, Sect. 2, 3]; all accuracy parameters sit in one "precision structure", none hard-coded locally, initialised in the input module and overwritten by a `.pre` file; default values of input parameters are "defined in the input module" [src: arXiv:1104.2932, Sect. 2.2, 2.3] |
| Reionisation | tanh in y = (1+z)^{3/2}, z_re obtained from τ by a root find [src: arXiv:2607.14854, Sect. V.3] | — |
| Massive neutrinos | one eigenstate with 0.06 eV by default; sparse momentum quadrature (three points by default) [src: arXiv:2607.14854, Sect. VI] | non-cold relics with automatic momentum sampling (arXiv:1104.2935) |

### 1.2 CAMB against CLASS
<!-- key: camb-against-class -->

| Aspect | CAMB | CLASS |
|---|---|---|
| Language | Fortran core, Python package `camb` | C core, Python wrapper `classy` |
| Design statement | line-of-sight code extended to closed models in arXiv:astro-ph/9911177 | "very structured, easy to modify, and offers a rigorous way to control the accuracy of output quantities" (arXiv:1104.2932) |
| Approximation schemes | — | tight-coupling approximation at first or second order, ultra-relativistic fluid approximation, radiation streaming approximation (Blas, Lesgourgues & Tram 2011, arXiv:1104.2933) |
| Non-cold relics | massive-neutrino perturbation treatment documented in the appendix of Howlett et al. 2012, arXiv:1201.3654 | arbitrary phase-space distributions with automatic momentum sampling and a viscous-fluid approximation inside the Hubble radius (arXiv:1104.2935) |
| Recombination default | `Recfast` class [doc: installed camb 2.0.4, default `CAMBparams().Recomb`, 2026-10-26] | `recombination = HyRec` [doc: https://raw.githubusercontent.com/lesgourg/class_public/v3.2.3/explanatory.ini, 2026-10-26]; HYREC-2 is described in Lee & Ali-Haïmoud 2020, arXiv:2007.14114 |
| Dark-energy default | `DarkEnergyFluid` class, `set_dark_energy(..., dark_energy_model='fluid')` [doc: installed camb 2.0.4, `set_dark_energy` signature, 2026-10-26] | `use_ppf = yes` [doc: https://raw.githubusercontent.com/lesgourg/class_public/v3.2.3/explanatory.ini, 2026-10-26] |
| Non-linear default | `NonLinear_none`; when switched on, `halofit_version='mead2020'` (HMcode-2020, arXiv:2009.01858) [doc: installed camb 2.0.4, `CAMBparams()` and camb/nonlinear.py, 2026-10-26] | `non_linear =` left empty [doc: https://raw.githubusercontent.com/lesgourg/class_public/v3.2.3/explanatory.ini, 2026-10-26] |
| Latest method paper | Lewis 2026, arXiv:2607.14854 (CAMB v2) | — |

CAMB v2 (arXiv:2607.14854) is a substantial update: a new treatment of the hyperspherical Bessel functions used for line-of-sight integration in non-flat models, updated integrators, a recalibrated fast recombination model, stabilised parameterised post-Friedmann (PPF) dark-energy evolution and improved CMB-lensing accuracy.
The abstract states that essentially all of the new algorithms and code were developed with LLMs or AI agents under human supervision.
The parameterised post-Friedmann prescription, which allows the equation of state to cross w = −1, is from Fang, Hu & Lewis 2008, arXiv:0808.3125; whether a w0wa run uses the fluid or the PPF model is a setting to state in a paper.

### 1.3 Non-linear corrections shipped with the solvers
<!-- key: non-linear-corrections-shipped-with-the-solvers -->

CAMB 2.0.4 exposes these `halofit_version` names: `original`, `bird`, `peacock`, `takahashi`, `mead` (alias `mead2016`), `halomodel`, `casarini`, `mead2015`, `mead2020`, `mead2020_feedback` [doc: installed camb 2.0.4, `camb.nonlinear.halofit_version_names`, 2026-10-26].
`takahashi` is the revised halofit of Takahashi et al. 2012, arXiv:1208.2701; `mead2020` and `mead2020_feedback` are HMcode-2020 without and with the baryonic-feedback model (arXiv:2009.01858).
pyccl defaults to `matter_power_spectrum='halofit'` and can pass a `halofit_version` to CAMB through `extra_parameters` [doc: installed pyccl 3.3.6, `pyccl.Cosmology` signature and docstring, 2026-10-26].
cosmoprimo leaves `non_linear` empty by default and its docstring recommends "mead" when matching CLASS and CAMB [doc: installed cosmoprimo 1.0.0, cosmoprimo/cosmology.py, 2026-10-26].
Two analyses that both "use halofit" may therefore use different fitting functions; the accuracy of each is in `results.md`.

### 1.4 Modified-gravity forks
<!-- key: modified-gravity-forks -->

| Code | Base | Approach | What distinguishes it | Reference |
|---|---|---|---|---|
| EFTCAMB | CAMB | effective field theory of dark energy, full linear dynamics | no quasi-static approximation; built-in stability conditions (ghost, superluminal propagation); handles phantom-divide crossing | arXiv:1312.5742, arXiv:1405.3590 |
| H-EFTCAMB | CAMB | "the official successor to EFTCAMB": adds a module for an arbitrary covariant Horndeski Lagrangian, solved either through the EFT mapping or directly from the scalar-field equations of motion (needed when the field oscillates) | Python wrapper integrated in Cobaya; validated against EFTCAMB models and against hi_class | Ye et al. 2026, arXiv:2603.01662 |
| hi_class | CLASS | Horndeski scalar-tensor theories | covariant-Lagrangian models (Galileon, nKGB, quintessence, Brans–Dicke), consistent initial conditions in the radiation era, automated quasi-static approximation giving an order-of-magnitude speed-up | arXiv:1605.06102, arXiv:1909.01828 |
| MGCAMB | CAMB | phenomenological modification of the perturbed Einstein equations that preserves covariant conservation of energy-momentum | μ, Σ, γ functions; massive neutrinos and dynamical dark energy since 2019; cubic-spline reconstruction of μ, Σ and Ω_X, direct μ–Σ implementation, CosmoMC and Cobaya interfaces since 2023 | arXiv:0809.3791, arXiv:1106.4543, arXiv:1901.05956, arXiv:2305.05667 |
| MGCLASS II | CLASS | parameterised deviations from General Relativity on sub-horizon scales, plus a subset of alternative theories | compatible with MontePython and Cobaya; validated on the parameterisations used by the Planck collaboration | Sakr & Martinelli 2021, arXiv:2112.14175 |

The split that matters is between codes that solve a theory (EFTCAMB, H-EFTCAMB, hi_class) and codes that parameterise the phenomenology (MGCAMB, MGCLASS II).
The first group guarantees a consistent background and stability; the second maps directly onto the μ–Σ constraints that surveys quote.
Facades expose a subset: pyccl supports only the `MuSigmaMG` parameterisation [doc: installed pyccl 3.3.6, `pyccl.modified_gravity`, 2026-10-26], and cosmoprimo lists an optional `isitgr` extra [doc: installed cosmoprimo 1.0.0, package metadata, 2026-10-26].
The physics of these parameterisations and the survey results belong to the sibling `cosmo-dark-energy-modified-gravity`.

### 1.5 Differentiable and accelerated solvers
<!-- key: differentiable-and-accelerated-solvers -->

DISCO-EB is a JAX solver whose outputs are differentiable with respect to all inputs, with massive neutrinos and a parameterised dark-energy fluid (Hahn, List & Porqueres 2023, arXiv:2311.03291).
SymBoltz.jl is "a symbolic-numeric, approximation-free and differentiable linear Einstein-Boltzmann solver" [doc: https://api.github.com/repos/hersle/SymBoltz.jl, 2026-10-26]; its Chebyshev interpolation in k and ℓ is described in Sletmoen 2026, arXiv:2608.24682.
class_sz is a C and Python code for cross-survey observables (halo model, LSS and CMB), accelerated with emulators (Bolliet et al. 2023, arXiv:2310.18482).
Neural emulators that replace the solver altogether are in section 9.

## 2. Theory facades
<!-- key: theory-facades -->

A facade gives one interface over one or several Boltzmann engines and adds the derived quantities an analysis needs (distances in survey units, σ8, Limber integrals, halo model).

| Facade | Engines | Scope | Units it returns | Differentiable |
|---|---|---|---|---|
| cosmoprimo | `class` (through `pyclass`), `camb`, `eisenstein_hu`, `eisenstein_hu_nowiggle`, `bbks` | background, thermodynamics, primordial, transfer, harmonic, Fourier | distances in Mpc/h, P(k) in (Mpc/h)³, H(z) in km/s/Mpc [doc: installed cosmoprimo 1.0.0, cosmoprimo/camb.py docstrings, 2026-10-26] | partly: "Most of cosmoprimo, apart from Boltzmann solvers, is JAX-friendly", with `jax.jacfwd` examples on the `bbks` and `capse` engines [doc: https://raw.githubusercontent.com/cosmodesi/cosmoprimo/main/README.md, 2026-10-26] |
| pyccl | `boltzmann_camb` (default), other transfer functions and emulators | distances, growth, P(k), halo model, angular spectra with Limber or the non-Limber FKEM method, correlation functions | k in Mpc⁻¹, P(k) in Mpc³, distances in Mpc [doc: installed pyccl 3.3.6, `linear_matter_power` and `comoving_radial_distance` docstrings, 2026-10-26] | no |
| astropy.cosmology | none (analytic FLRW) | background only | `Quantity` objects in Mpc and km/s/Mpc [doc: installed astropy 8.0.1, `Planck18.comoving_distance` and `Planck18.H0` units, 2026-10-26] | no |
| jax-cosmo | Eisenstein–Hu transfer function, halofit | background, P(k), Limber angular spectra for lensing and clustering (arXiv:2302.05163) | not read | yes (JAX) |
| cloelib | interfaces to established Boltzmann solvers | photometric and spectroscopic observables, CMB and cluster cross-correlations; "intended to serve as the reference theory computation infrastructure for Euclid's first cosmological release" (Bonici et al. 2026, arXiv:2605.23839) | not read | yes (JAX) |

Points of difference:

- cosmoprimo carries the DESI fiducial cosmology: `fiducial.DESI()` is the AbacusSummit base cosmology c000, described in its docstring as "Planck2018, base_plikHM_TTTEEE_lowl_lowE_lensing mean", with default engine `class` [doc: installed cosmoprimo 1.0.0, `fiducial.DESI` docstring, 2026-10-26].
- pyccl was built around a validation suite: each predicted quantity has a documented numerical accuracy established against independent codes (Chisari et al. 2018, arXiv:1812.05995). Its non-Limber method is FKEM, the fastest method within the required accuracy in the N5K challenge (Leonard et al. 2022, arXiv:2212.04291).
- What CCL validates is numerical accuracy only; physical accuracy of each model is discussed separately. The accuracy metric is a fractional difference for background quantities and, for C_ℓ, |ΔC_ℓ|/σ_ℓ with the full-sky cosmic-variance error σ_ℓ² = (C_ℓ^aa C_ℓ^bb + (C_ℓ^ab)²)/(2ℓ + 1), required below 0.1; the validation C_ℓ used the BBKS spectrum, and RSD and magnification were "not currently validated" in the 2018 paper (arXiv:1812.05995) [src: Sect. IV, IV.5, Eq. 95–96]. Values are in `systematics.md`, section 9.
- The N5K challenge fixed the accuracy and compared run time: the LSST Y10 3x2pt data vector to Δχ² ≈ 0.2 on ℓ ≤ 200, on 64 cores of one node. FKEM took 0.437 s, the matter method 2.00 s, Levin 4.53 s, against 0.0445 s for CCL's Limber calculation; cosmology-independent precomputations were excluded (arXiv:2212.04291) [src: Sect. 5.1].
- astropy.cosmology solves no perturbations: it has no P(k) and no σ8 calculation; the `sigma8` and `n` entries of `Planck18.meta` are stored metadata [doc: installed astropy 8.0.1, `Planck18.meta` and attribute listing, 2026-10-26].
- flip computes its model power spectra through any of three engines, `class_engine`, `cosmoprimo_engine` and `pyccl_engine` [doc: corentinravoux/flip/docs/power_spectra.md on `main`, 2026-10-26], so the unit conversions of section 1 of `systematics.md` apply at that boundary.

Conventions each survey adopts (fiducial cosmologies, σ8 against σ12, h⁻¹ units) are in the sibling `cosmo-theory-foundations`.

## 3. Samplers and inference frameworks
<!-- key: samplers-and-inference-frameworks -->

### 3.1 Frameworks
<!-- key: frameworks -->

A framework couples a theory code, a set of likelihoods and a sampler, and manages the dependencies between them.

| Framework | Theory codes | Distinctive mechanism | Reference |
|---|---|---|---|
| CosmoMC | CAMB | Metropolis–Hastings with fast–slow decorrelation and dragging (arXiv:1304.4473) | arXiv:astro-ph/0205436 |
| Cobaya | CAMB, CLASS and others through wrappers | automatic blocking of parameters by speed, caching of intermediate results, YAML or Python input; its MCMC sampler is "the Markov Chain Monte Carlo Metropolis sampler used by CosmoMC" and PolyChord is interfaced [doc: https://cobaya.readthedocs.io/en/latest/; https://cobaya.readthedocs.io/en/latest/sampler_mcmc.html; https://cobaya.readthedocs.io/en/latest/theory.html; https://cobaya.readthedocs.io/en/latest/input.html, 2026-10-26] | arXiv:2005.05290 |
| MontePython | CLASS | adaptation of the jumping factor and inverse-Fisher-matrix proposal (version 3) | arXiv:1210.7183, arXiv:1804.07261 |
| CosmoSIS | modules (CAMB and others) | every calculation is a module with declared inputs and outputs | arXiv:1409.3409 |
| desilike | wrappers of velocileptors, pybird and FOLPS-nu | likelihoods for BAO and RSD analyses, Taylor-expansion and MLP emulators, ShapeFit; samplers and profilers provided; bindings to Cobaya, CosmoSIS and MontePython [doc: https://raw.githubusercontent.com/cosmodesi/desilike/main/README.md, 2026-10-26] | none |

### 3.2 Sampler families
<!-- key: sampler-families -->

| Family | Members | Needs gradients | Gives evidence | Note |
|---|---|---|---|---|
| Metropolis–Hastings with speed hierarchy | CosmoMC, Cobaya `mcmc`, MontePython | no | no | fast–slow decorrelation was demonstrated on Planck likelihoods with dozens of fast nuisance parameters (arXiv:1304.4473) |
| Affine-invariant ensemble | emcee (arXiv:1202.3665) | no | no | one or two tuning parameters; the MCMC backend of flip |
| Nested sampling, ellipsoidal | MultiNest (arXiv:0809.3437) | no | yes | see `systematics.md` for the DES result on its credible intervals |
| Nested sampling, slice | PolyChord (arXiv:1502.01856, arXiv:1506.00171) | no | yes | exploits a hierarchy of parameter speeds |
| Nested sampling, dynamic | dynesty (arXiv:1904.02180) | no | yes | allocates live points adaptively to the posterior |
| Importance nested sampling with neural networks | nautilus (arXiv:2306.16923) | no | yes | uses all likelihood evaluations in the estimate |
| Sequential Monte Carlo with normalising flows | pocoMC (arXiv:2207.05652) | no | yes | parallelisable |
| Hamiltonian Monte Carlo, NUTS | NumPyro (arXiv:1912.11554), BlackJAX (arXiv:2402.10797); algorithm in arXiv:1111.4246 | yes | no | requires a differentiable likelihood: JAX theory code or emulator |
| GPU nested sampling | JAX-based framework of Lovick et al. 2025, arXiv:2509.13307 | no | yes | pairs with neural emulators |

Foundations: nested sampling is Skilling 2006, doi:10.1214/06-BA127 (the evidence is "the prime result of the computation", posterior samples "an optional by-product", sampling within a hard likelihood constraint) [src]; the affine-invariant ensemble move of emcee is Goodman & Weare 2010, doi:10.2140/camcos.2010.5.65 (MCMC "whose performance is unaffected by affine tranformations of space") [src]; Hamiltonian Monte Carlo is reviewed in Neal 2012, arXiv:1206.1901 (distant proposals from volume-preserving Hamiltonian dynamics with auxiliary momentum variables) [src]; NUTS adapts the HMC path length (arXiv:1111.4246).

What the code papers say about their algorithms and tuning:

| Code | Algorithm and tuning read in the body | Place |
|---|---|---|
| Cobaya | Metropolis–Hastings "translated from CosmoMC", with oversampling of fast parameters or dragging; automatic blocking that measures the cost of each block and sorts slow before fast blocks with a lower-triangular affine transformation; convergence by a modified Gelman–Rubin R − 1 over parallel chains or over the latest chunks of one chain, optionally also on confidence limits; PolyChord wrapper that uses the same speed blocking; scipy and Py-BOBYQA minimisers; importance reweighting | arXiv:2005.05290 [src: Sect. IV.3; App. A] |
| MontePython 3 | Metropolis–Hastings with a fast–slow scheme; `--update` (on by default in v3) updates the proposal covariance, starting when max(R − 1) over the second half of the chains falls below 3 and stopping below 0.4, and works with or without MPI; `--superupdate` adapts the jumping factor from the default 2.4 towards an acceptance rate ≃ 0.25; normal and inverted hierarchies are sampled through `M_tot_NH` or `M_tot_IH`, individual masses solved from the measured splittings and passed to CLASS | arXiv:1804.07261 [src: Sect. 2.3, 2.4; App. A.1] |
| CosmoSIS | every module reads from and writes to a DataBlock, which stores scalars, arrays and strings but "explicitly cannot store arbitrary structured information"; configuration in extended ini files; a "sampler" is anything that proposes parameter sets (test, grid, maximum likelihood, MCMC, emcee, nested); MPI process-level "Pool" parallelism, because thread parallelism at the sampler level is impossible when codes such as camb "are not thread-safe" | arXiv:1409.3409 [src: Sect. 4.3, 4.4, 4.5] |
| emcee | stretch move Y = X_j + Z[X_k − X_j], with g(z) ∝ 1/√z on [1/a, a], a = 2, and acceptance probability min(1, Z^{N−1} p(Y)/p(X_k)); "autocorrelation time is the best indicator of MCMC performance"; acceptance fraction "should be in the 0.2 to 0.5 range"; a = 2 "is good in essentially all situations" | arXiv:1202.3665 [src: Sect. II, Eq. 7–10; Sect. IV] |
| PolyChord | `n_live` is a resolution parameter: run time ∝ n_live, evidence error ∝ n_live^{−1/2}; `n_repeats` is the slice-chain length: too low gives correlated live points and unreliable evidences, while posteriors "remain accurate"; ∼ 3 × n_dims is typically sufficient, more for curving degeneracies | arXiv:1506.00171 [src: Sect. 5.7] |
| dynesty | dynamic allocation of live points; bounds (unit cube, single and multiple ellipsoids, balls, cubes) and samplers (uniform, random walks, multivariate and Hamiltonian slice); the posterior is "entirely a by-product" of standard nested sampling, which needs a prior transform to the unit cube | arXiv:1904.02180 [src: Sect. 2.7, 4] |
| nautilus | importance nested sampling with an exploration and a sampling phase and neural-network bounds; the authors recommend discarding exploration-phase points for publications, since "not doing so may result in percent-level biases on the posterior and evidence estimates", and checking robustness to the number of live points; on a seven-parameter galaxy–halo fit it needed about 80 000 likelihood calls, against 3–10 × 10⁶ reported with emcee in the original analysis | arXiv:2306.16923 [src: Sect. 4.6, 5.4] |

NumPyro is a probabilistic programming language: the model is written with sampling statements and the library derives the log-density.
BlackJAX is a library of kernels working "directly with the (un-normalized) target log density function" (arXiv:2402.10797): the user supplies the log-posterior.
Chains from any of these are post-processed with GetDist (arXiv:1910.13970), which estimates marginal densities by kernel density estimation with boundary correction.
Convergence criteria, prior-volume effects and evidence interpretation belong to the sibling `cosmo-statistics-inference`.

## 4. Perturbation-theory codes
<!-- key: perturbation-theory-codes -->

All codes below compute the one-loop power spectrum of biased tracers in redshift space with counterterms and stochastic terms; they differ in the expansion, the infrared resummation and the parameter basis.
The comparison below follows section 3.6 of Maus et al. 2024, arXiv:2404.07272 [src].

| Code | Expansion | Infrared resummation | Counterterms and stochastic terms | Other |
|---|---|---|---|---|
| velocileptors (LPT) | Lagrangian | long-wavelength displacements exponentiated, short ones perturbative, split at `k_IR` | counterterms of the form k²P_Zel | also moment expansion, Gaussian and Fourier streaming models, real-space velocity statistics [doc: https://raw.githubusercontent.com/sfschen/velocileptors/master/README.md, 2026-10-26] |
| velocileptors (EPT) | Eulerian | wiggle / no-wiggle split, only the wiggle part is damped | k²P_lin | accepts a no-wiggle spectrum through `pnw` [doc: https://raw.githubusercontent.com/sfschen/velocileptors/master/README.md, 2026-10-26] |
| PyBird | Eulerian (EFTofLSS) | resummation of long-wavelength displacements, as in LPT | k²P_lin; one extra isotropic stochastic term k²/k_M² | reference arXiv:2003.07956 |
| FOLPSν | Eulerian with kernels beyond Einstein–de Sitter | wiggle / no-wiggle split | k²P_lin | scale-dependent growth from massive neutrinos kept in the kernels (arXiv:2208.02791) |
| CLASS-PT | Eulerian, inside CLASS | infrared resummation | full set, with Alcock–Paczynski | arXiv:2004.10607 |
| CLASS-OneLoop | Eulerian moment expansion, inside CLASS | infrared resummation | full set; loops by direct integration or FFT; fast–slow parameter decomposition | Linde et al. 2024, arXiv:2402.09778 |

Foundation of the fast loop codes: FFTLog, "a code for taking the fast Fourier or Hankel transform of a periodic sequence of logarithmically spaced points", is the appendix of Hamilton 2000, arXiv:astro-ph/9905191 [src]. CLASS-PT, FOLPSν, FAST-PT and `neckar` evaluate loop integrals with it; pyccl uses it for Hankel transforms (section 7).

What the code papers say about method, accuracy and validity:

| Code | Method, accuracy and validity read in the body | Place |
|---|---|---|
| CLASS-PT | FFTLog decomposition of the loop integrals into precomputed matrices; default N_FFTLog = 256 gives ∼ 0.1 % on the one-loop term for k ≲ 0.2 h Mpc⁻¹, the "fast mode" N_FFTLog = 128 ∼ 1 % at four times the speed, and the authors encourage the fast mode for practical use; redshift-space multipoles with IR resummation take 1.3 s (default) or 0.3 s (fast); massive neutrinos through the "cb" linear spectrum, the default input (flag `cb=No` for total matter), with EdS kernels; not to be used for k ≳ 3 h Mpc⁻¹, and justified for k < k_NL(z) = 0.45 D(z)^{−4/3.3} h Mpc⁻¹; wiggly/non-wiggly frequency cuts untested far from Planck-like models | arXiv:2004.10607 [src: Sect. 4.1.3, 4.5, 5.2, 5.3, Eq. 5.2] |
| PyBird | standalone Python 3 code whose input is a linear P(k) "from any Boltzmann code"; FFTLog for the one-loop terms and for a fast IR resummation written as the non-resummed spectrum plus IR corrections; can return spectra for given EFT parameters or independently of them (for partial marginalisation or Taylor expansion around a fiducial cosmology); "runs in less than a second on a laptop"; shipped with a MontePython 3 integration | arXiv:2003.07956 [src: Sect. 4, 4.1] |
| velocileptors (LPT) | angular integrals reduced to sums of spherical Bessel functions evaluated by FFTLog, one transform per k, n < 10 terms typically sufficient; validated on halo samples at z = 0.8 in 4 × (4 h⁻¹ Gpc)³ of simulations, with linear displacements resummed up to k_IR = 0.2 h Mpc⁻¹ and fits for k < 0.2 h Mpc⁻¹ "well within the few-percent systematics expected from the N-body data" | arXiv:2012.04636 [src: Sect. 4, Eq. 7–8; Sect. 5.1] |
| FOLPSν | input: linear matter or cb spectrum plus Ω_m, h, M_ν and nuisance parameters {b₁, b₂, b_s², b₃nl, α₀, α₂, α₄, c̃, α₀^shot, α₂^shot}; computes its own no-wiggle spectrum and f₀ (neglecting relativistic species), with G₁(k) = f(k)/f₀ from the Eisenstein–Hu approximation; switch between fk and EdS kernels; FFTLog on N points over 10⁻⁷ < k < 100 h Mpc⁻¹, with N = 128 giving at most ∼ 0.1 % (monopole, quadrupole) and ∼ 0.2 % (hexadecapole) up to k = 0.35 h Mpc⁻¹ against direct integration; validated on Quijote halos with M_ν = 0.1 and 0.4 eV, 100 (h⁻¹ Gpc)³ in total | arXiv:2208.02791 [src: Sect. 5, 6] |
| FAST-PT | P₂₂- and P₁₃-type convolutions by FFT on log-spaced k; a 3000-point grid from k = 10⁻⁴ to 10² with 500 zeros of padding at each end takes ∼ 0.02 s on a laptop; users should sample on a wider grid than needed and trim, to avoid wrapping; agreement "to high precision" with a 2D grid integration, residual noise coming from the input CAMB spectrum | arXiv:1603.04826 [src: Sect. 3.1] |

Counterterms in k²P_Zel and in k²P_lin differ at high k by terms that are formally of two-loop order (arXiv:2404.07272, section 3.6).
The dependence on the wiggle / no-wiggle decomposition is small for the final sum, according to the same section.
Bias parameters do not map one to one between all codes; the DESI comparison uses a "minimal freedom" choice (tidal and third-order bias fixed to coevolution) and a "maximal freedom" choice (four free bias parameters) to compare like with like (arXiv:2404.07272, conclusion).

FAST-PT is a different kind of tool: an FFT algorithm for the mode-coupling integrals themselves (arXiv:1603.04826), extended to tensor quantities such as intrinsic alignments (arXiv:1609.05978); it is a general integrator of perturbation-theory convolutions rather than a galaxy-clustering pipeline.

Recent additions, all aimed at gradient-based or faster inference:

- PyBird-JAX, a differentiable JAX implementation of PyBird with internal emulators (Reeves, Zhang & Zheng 2025, arXiv:2507.20990).
- Effort.jl, an emulator of the EFTofLSS power spectrum validated against PyBird (arXiv:2501.04639).
- `folpsax`, the JAX version of FOLPSν [doc: https://api.github.com/repos/cosmodesi/folpsax, 2026-10-26].
- `elf`, a JAX implementation of the one-loop galaxy power spectrum in both Eulerian and Lagrangian perturbation theory, presented as the first auto-differentiable LPT implementation (Kobayashi & Akitsu 2026, arXiv:2610.08023).
- `neckar`, a C code with a Python wrapper based on the FFTLog expansion, with bootstrap kernels and a revised infrared resummation (Harder et al. 2026, arXiv:2610.03466).

The equations (EFTofLSS counterterms, bias bases, Kaiser limit) are in `cosmo-theory-foundations`; the survey results obtained with these codes are in `cosmo-galaxy-clustering`.

## 5. Two-point and higher-order estimators
<!-- key: two-point-and-higher-order-estimators -->

| Family | Members | Method | When it is the right tool |
|---|---|---|---|
| Exact pair counting | Corrfunc (arXiv:1911.03545); pycorr, which wraps it | counts every pair in bins; pycorr adds estimators, weights and jackknife | galaxy ξ(s, μ), w_p(r_p), where exact counts and pairwise weights matter |
| Tree pair counting | TreeCorr (arXiv:astro-ph/0307393) | ball tree with a tolerance `bin_slop` on the bin assignment | shear and count correlations over many decades in angle; three-point functions |
| FFT power spectrum | pypower, nbodykit (arXiv:1712.05834) | particles painted on a mesh, FFT, multipoles with a local line of sight | P_ℓ(k) of surveys and boxes, with window functions |
| Pseudo-C_ℓ | NaMaster (arXiv:1809.09603) | mode-coupling matrix inversion on masked maps, with deprojection and purification | angular spectra of spin-0 and spin-2 fields |
| Three-point | Triumvirate (arXiv:2304.03643), TreeCorr, nbodykit | tri-polar spherical-harmonic multipoles (Triumvirate) | bispectrum and 3PCF multipoles |
| Reconstruction | pyrecon | density-field reconstruction before BAO fits [doc: https://api.github.com/repos/cosmodesi/pyrecon, 2026-10-26] | post-reconstruction BAO |

Details read this session:

- pycorr supports angular (θ), s, (s, μ) and (r_p, π) binning; its only pair-counting engine is Corrfunc, by default the `desi` branch of the cosmodesi fork; it supports inverse bitwise (PIP) weights with angular upweighting, analytical pair counts for periodic boxes, jackknife covariance and MPI [doc: https://raw.githubusercontent.com/cosmodesi/pycorr/main/README.md, 2026-10-26].
- pypower estimates auto- and cross-power-spectrum multipoles and window functions for periodic boxes and survey geometry, plane-parallel or with the first odd wide-angle corrections; it depends on `pmesh` [doc: https://raw.githubusercontent.com/cosmodesi/pypower/main/README.md, 2026-10-26].
- pypower accepts pairwise weights as a pycorr `WeightTwoPointEstimator` and can compute a direct pair-count correction at small angular separation (`direct_selection_attrs`, default θ between 0 and 2/60 degrees) [doc: cosmodesi/pypower/pypower/fft_power.py on `main`, `CatalogFFTPower` docstring, 2026-10-26].
- nbodykit also contains friends-of-friends, HOD population and FastPM (arXiv:1712.05834); those belong to `cosmo-simulations-mocks`.
- NaMaster handles any pair of spin-0 or spin-2 fields, contaminated by an arbitrary number of linear systematics, with E- or B-mode purification, on the sphere or in the flat sky (arXiv:1809.09603).

Methods read in the code papers:

- **Pair counting (Corrfunc).** The code computes weighted pair-separation histograms; the estimators are built from them, the natural estimator 1 + ξ = DD/RR and the Landy–Szalay estimator, which "also uses an additional DR term" [sec: arXiv:1911.03545, Sect. 2.1]. Speed comes from gridding the particles in cells of size set by R_max (or θ_max for angular functions), sub-dividing cells, associating cell pairs, exploiting autocorrelation symmetry, sorting for early exit, explicit SIMD vectorisation and OpenMP (arXiv:1911.03545) [src: Sect. 4]. Against TreeCorr 3.3.6 with `bin_slop` disabled the pair counts "exactly agreed", Corrfunc being 1.9–5.7 times faster on one thread [src: Sect. 6.5].
- **Tree pair counting (TreeCorr's algorithm).** Brute force is O(N²) for two-point and O(N³) for three-point functions; two cells of radii s₁, s₂ at separation d_c are treated as one pair when (s₁ + s₂)/d_c < b, with b = Δ ln d the bin size, so that any pair is "wrong by at most one bin", reducing the cost from O(N₁N₂) to O(N₁ + N₂) for those cells (Jarvis, Bernstein & Jain 2003, arXiv:astro-ph/0307393) [src: Sect. 4.1, Eq. 62–63]. This is the approximation that `bin_slop` controls; exact counts need it disabled (section 5.2 of `systematics.md`).
- **Pseudo-C_ℓ (NaMaster).** The method descends from MASTER, Hivon et al. 2002, arXiv:astro-ph/0105302, a "Monte Carlo Apodised Spherical Transform EstimatoR" devised for Boomerang [src]. NaMaster describes the pseudo-C_ℓ estimator as a quadratic estimator whose data covariance is assumed diagonal in real space, which brings the cost from O(N_pix³) to O(N_pix^{3/2}) at the expense of optimality, small for non-steep spectra and on small scales; masks are treated as regions of infinite noise; contaminant templates are deprojected under a linear contamination model, and a template must not itself contain signal (arXiv:1809.09603) [src: Sect. 2.1.1, 2.2, 5].

Estimator definitions (Landy–Szalay, FKP, Yamamoto), windows and fibre-collision weights belong to `cosmo-galaxy-clustering`.

## 6. Lyman-alpha tools
<!-- key: lyman-alpha-tools -->

| Code | Role in an analysis | Method |
|---|---|---|
| picca | data side: continuum fitting, flux-transmission deltas, 1D and 3D correlation functions, P1D, covariance matrices [doc: https://raw.githubusercontent.com/igmhub/picca/main/README.md, 2026-10-26] | reference analysis in du Mas des Bourboux et al. 2020, arXiv:2007.08995 |
| Vega | model side: "tool for computing 3D correlation function and power spectrum models", based on picca `fitter2`; minimiser iminuit, sampler interfaces to PolyChord and pocoMC [doc: https://raw.githubusercontent.com/andreicuceu/vega/master/README.rst, 2026-10-26] | used for Lyα auto- and cross-correlations, metal, DLA and SBLA analyses and DESI BAO and full-shape analyses [doc: https://raw.githubusercontent.com/andreicuceu/vega/master/README.rst, 2026-10-26]; described in Cuceu et al. 2022, arXiv:2209.12931, and Cuceu et al. 2025, arXiv:2509.15308 |
| LaCE | P1D emulator | Gaussian process (arXiv:2011.15127) and neural network (arXiv:2305.19064) on the amplitude and slope of the linear power spectrum and IGM parameters |
| lym1d | P1D likelihood framework | Gaussian-process emulator built on the Lyssa suite of Nyx simulations (Walther et al. 2024, arXiv:2412.05372) |
| ForestFlow | P3D emulator | conditional normalising flows predicting the two linear biases and six parameters of small-scale deviations, combined with a Boltzmann solver (Chaves-Montero et al. 2024, arXiv:2409.05682) |

The picca README states that its tools serve both eBOSS and DESI, that "Picca v4.0 was used in du Mas des Bourboux et al. (2020)", and that model computation and fitting are done with Vega; the older `fitter2` remains for some tasks [doc: https://raw.githubusercontent.com/igmhub/picca/main/README.md, 2026-10-26].
LaCE and lym1d differ in training simulations and in parameterisation: LaCE emulates as a function of the linear power spectrum at the redshift of interest, which lets it predict extended models not in the training set (arXiv:2011.15127).
The Lyα BAO pipeline as a whole is validated on 150 synthetic realisations of DESI DR1 in Cuceu et al. 2024, arXiv:2404.03004 [src: abstract].


Read in the bodies:

- **picca in the eBOSS DR16 paper.** "Package for Igm Cosmological-Correlations Analyses": modules to estimate the Lyα forest signal, compute auto- and cross-correlations and their covariance, and fit them "using an input matter power spectrum"; the no-BAO (smooth) template is built from the CAMB linear spectrum by the side-band technique implemented in picca, using nbodykit, and P_peak = P_L − P_sm (arXiv:2007.08995) [src: Sect. I, IV.1]. The fitting described there is the pre-Vega `fitter2` stage.
- **LaCE parameterisation and units.** P1D is emulated as a function of the amplitude Δ²_p = k³P_lin and slope n_p of the CDM-plus-baryon linear spectrum (neutrino clustering excluded) at the pivot k_p = 0.7 Mpc⁻¹, fitted with a second-order log polynomial over 0.5 k_p < k < 2 k_p of a CAMB spectrum; no growth or expansion parameters, justified by Ω_m(z = 2) ≈ 0.91 (arXiv:2011.15127) [src: Sect. 2.1, Eq. 1–2]. The pivot is in Mpc⁻¹, not h Mpc⁻¹. Training set: 30 MP-Gadget simulations, L = 67.5 Mpc, 768³ CDM and baryon particles, with the QuickLymanAlpha option; validation by leave-one-simulation-out tests against the 1 % band and BOSS P1D errors [src: Sect. 3, 4.1].
The physics (continuum distortion, metals, DLAs) and the results belong to the sibling `cosmo-lyman-alpha`.

## 7. Lensing and sphere tools
<!-- key: lensing-and-sphere-tools -->

HEALPix (Górski et al. 2004, arXiv:astro-ph/0409513) is the equal-area iso-latitude pixelisation used for almost all full-sky CMB and LSS maps; `healpy` is its Python package.
Its defaults (RING ordering, three iterations of the harmonic transform, ℓ_max = 3 N_side − 1) are in section 6 of `systematics.md`.
NaMaster (section 5) works on HEALPix or rectangular (CAR) maps and uses the HEALPix polarisation convention [doc: https://namaster.readthedocs.io/en/latest/api/pymaster.field.html, 2026-10-26].
TreeCorr (section 5) measures the shear two- and three-point functions.
pyccl (section 2) predicts the lensing and clustering angular spectra and their correlation functions through FFTLog Hankel transforms [doc: installed pyccl 3.3.6, `correlation(method='fftlog')` signature, 2026-10-26].
FAST-PT (section 4) supplies the one-loop intrinsic-alignment integrals.
LensTools (Petri 2016, arXiv:1606.01903) is a simulation and feature-measurement package: it brings together CAMB and Gadget2 runs into a ray-tracing pipeline and measures lensing features such as peaks and moments.
Survey pipelines, shear calibration and the choice between ξ±, COSEBIs and pseudo-C_ℓ belong to the sibling `cosmo-weak-lensing`.

## 8. Differentiable and field-level codes
<!-- key: differentiable-and-field-level-codes -->

### 8.1 flip
<!-- key: flip -->

flip (arXiv:2501.16852) fits the growth rate from velocity and density fields with a Gaussian likelihood whose covariance is computed from model power spectra; it implements the covariance models of earlier velocity analyses and adds one with wide-angle corrections (arXiv:2501.16852).
It is "field-level" in the sense that the likelihood is written on the field values at the tracer positions; it does not sample initial conditions, unlike the forward models of §8.2.
Fitting is by maximum likelihood (Minuit), MCMC (emcee) or Fisher forecast [doc: corentinravoux/flip/docs/fitting.md on `main`, 2026-10-26]; some covariance terms suffer catastrophic cancellation at small kσ_g and are evaluated in arbitrary precision [src: arXiv:2501.16852, App. D].
The README asks users to cite arXiv:2501.16852 and Carreres et al. 2023, arXiv:2303.01198.
The method, its peers and its results are in `cosmo-peculiar-velocities`.

### 8.2 Forward-model field-level inference
<!-- key: forward-model-field-level-inference -->

BORG samples the three-dimensional initial density field with a physical forward model: second-order Lagrangian perturbation theory in Jasche & Wandelt 2012, arXiv:1203.3639, a particle-mesh model in Jasche & Lavaux 2018, arXiv:1806.11117, with Hamiltonian Monte Carlo inside a block-sampling scheme.
Differentiable particle-mesh codes supply such forward models in JAX: pmwd uses the adjoint method with reverse time integration to keep memory low (Li et al. 2022, arXiv:2211.09958); DISCO-DJ supports forward- and reverse-mode differentiation with memory independent of the number of time steps and uses theory-informed integrators (List et al. 2025, arXiv:2510.05206); JaxPM is a JAX particle-mesh solver cited here by its repository; FlowPM is the earlier TensorFlow implementation (arXiv:2010.11847).
Read in the bodies:

- **BORG (2018).** The posterior has a Gaussian prior on the initial density field at a = 10⁻³ and a Poisson likelihood for galaxy counts at a = 1, linked by 2LPT or a particle-mesh model; galaxies follow the four-parameter local non-linear bias n_g = N̄(1+δ)^β exp[−ρ_g(1+δ)^{−ε_g}] multiplied by the survey response; robustness to model misspecification is obtained by raising the Poisson likelihood to a power between 0 and 1 (tempering); gradients come from a tangent-adjoint model of the PM code (arXiv:1806.11117) [src: Sect. 2.1, 3.4, 3.5, Eq. 19–20; App. C]. DFT conventions are in its Appendix A.
- **pmwd.** Automatic differentiation must store the whole forward history, so memory limits differentiable simulations; pmwd uses the adjoint method with reverse time integration to reconstruct the history, on JAX and GPUs. It places itself after BORG and ELUCID (analytic derivatives) and FastPM and FlowPM (automatic differentiation through vmad and TensorFlow) (arXiv:2211.09958) [src: Summary; Statement of Need].

candl is a differentiable CMB power-spectrum likelihood (arXiv:2401.13433), which makes Fisher matrices exact and NUTS sampling possible for CMB data.
The science done with these (BORG reconstructions, constrained simulations, field-level versus summary information) belongs to the siblings `cosmo-beyond-two-point` and `cosmo-simulations-mocks`.

## 9. Emulators
<!-- key: emulators -->

An emulator in this section replaces the Boltzmann or perturbation-theory call inside the likelihood; it leaves nuisance parameters and redshift distributions to the analytic part of the pipeline (arXiv:2106.03846).

| Emulator | Target | Trained on | Framework |
|---|---|---|---|
| CosmoPower | matter P(k); CMB temperature, polarisation and lensing-potential spectra | Boltzmann-code outputs | TensorFlow (arXiv:2106.03846); JAX version in arXiv:2305.06347 |
| High-accuracy CosmoPower emulators | CMB spectra, P(k), distances, BAO and RSD observables, derived parameters in ΛCDM, wCDM, N_eff and Σm_ν models | high-precision Einstein–Boltzmann settings | Bolliet et al. 2023, arXiv:2303.01591 |
| CosmoPower packaging framework | standards for describing, packaging and distributing emulators, with CAMB-based emulators | CAMB | Jense et al. 2024, arXiv:2405.07903 |
| Capse.jl | CMB temperature, polarisation and lensing spectra | Boltzmann-code outputs | Julia (arXiv:2307.14339) |
| Effort.jl | EFTofLSS galaxy power spectrum | PyBird | Julia (arXiv:2501.04639) |
| LaCE, lym1d, ForestFlow | Lyα P1D and P3D | hydrodynamical simulations | section 6 |

An emulator inherits the precision settings, the neutrino model and the parameter ranges of its training set; outside them it extrapolates silently.

Read in the bodies:

- **CosmoPower (2021).** P(k) is emulated as a linear spectrum times a non-linear correction (HMcode with free c_min and η₀), two separate networks, at 420 k values over [10⁻⁵, 10] Mpc⁻¹ with z ∈ [0, 5] as an input; ∼ 1.8 × 10⁵ training and ∼ 2 × 10⁴ test spectra; 99 % of test spectra within 0.1 % (linear) and 0.4 % (non-linear correction), the error rising above k ≳ 1 Mpc⁻¹; the non-linear part was computed to k_max = 100 Mpc⁻¹ for stability though used to 10 Mpc⁻¹ (arXiv:2106.03846) [src: Sect. 3.2, Eq. 9]. CMB: direct network for TT and EE, PCA plus network for TE (zero crossings) and C_ℓ^φφ [src: Sect. 4.1]. The Planck 2018 plik-lite validation ran in about 10 s on one GPU against ∼ 1.2 × 10⁵ s on 80 CPU cores with CLASS [src: Sect. 4.2].
- **High-accuracy CosmoPower emulators (2023).** Reference: camb v1.3.6 with `lens_potential_accuracy=8`, `lens_margin=2050`, `AccuracyBoost = lSampleBoost = lAccuracyBoost = 2`, `DoLateRadTruncation=False`, `kmax=10`, `k_per_logint=130`, ℓ_max = 11000, HMcode with c_min = 3.13 and η₀ = 0.603; training data from class v2.9.4 with three changed parameters, `accurate_lensing: 1`, `k_max_tau0_over_l_max: 15.`, `perturb_sampling_stepsize: 0.05`, about one minute per sample; one emulator call (TT, TE, EE, linear and non-linear P(k), derived parameters) ≈ 60 ms, a factor 1000 speed-up (arXiv:2303.01591) [src: Sect. 3, 4].
Emulators of N-body outputs (non-linear P(k), halo statistics, baryonic suppression) are in the sibling `cosmo-simulations-mocks`.

## Not verified
<!-- key: not-verified -->

- Which cosmoprimo functions are differentiable beyond the two README examples was not read.
- The units returned by jax-cosmo and cloelib were not read.
- The Vega README gives its first reference as a DOI (`10.1093/mnras/stad1546`,
 "Cuceu et al. 2022"); its identification with arXiv:2209.12931 rests on author, year and subject and was not checked against the journal record.
- The Landy–Szalay paper (Landy & Szalay 1993, "Bias and variance of angular correlation functions", title and DOI confirmed on Crossref) could not be read: Crossref holds no abstract and the ADS page was blocked; it is named here only through the Corrfunc paper, and has no row in `sources.tsv`.
- DISCO-DJ II (arXiv:2510.05206) has no usable HTML rendering; its body was not read.
- arXiv:2607.14854 was read in an HTML rendering titled "CAMB 2", an earlier version than the current abstract ("CAMB v2"); section and appendix numbers quoted here (Sect. II–XI, App. B–C) may differ in the current version.
- The recommended sampler settings of Lemos et al. 2022 (their Table 3) did not render and were not read.
- No body was read for hi_class, EFTCAMB, MGCAMB, jax-cosmo, cloelib, Capse.jl, ForestFlow or Vega in this pass.
- CLASS code defaults were read in `explanatory.ini` of v3.2.3, a 2024 checkout; the current release is classy 3.4.1.0 and was not read [doc: lesgourg/class_public/explanatory.ini at tag v3.2.3; https://pypi.org/pypi/classy/json, 2026-10-26].
