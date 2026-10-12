# Quantified facts — agreement between codes, stated accuracies, timings

Scope: documented agreement between codes (Boltzmann solvers, perturbation-theory codes, estimators, samplers), accuracies the reference papers state, and benchmark timings where a paper gives them.

Snapshot: 2026-10-11

Flags: `[src]` read this session in the cited paper (abstract unless a section is named), in an installed package or at a repository; `[sec]` taken from a secondary source that is named; `[der]` derived, with the derivation stated.
Every accuracy below holds for the configuration its paper tested (model, scales, precision settings). None is a property of "the code" in general.

## 1. Boltzmann solvers: CAMB against CLASS, and the modified-gravity forks

### 1.1 Agreement between CAMB and CLASS

| Statement | Value | Conditions | Citation | Flag |
|---|---|---|---|---|
| Lensed CMB and matter power spectra computed by the two codes agree | 0.01 % | concordance cosmology, a given recombination history, after "a few tiny changes in CAMB" | Lesgourgues 2011, arXiv:1104.2934 | [src] |
| Speed at fixed precision, lensed CMB spectra of a ΛCDM model | CLASS about 2.5 times faster than CAMB | 2011 versions of both codes | arXiv:1104.2934 | [src] |
| Same agreement as summarised fifteen years later | "at the ∼10⁻⁴ level for flat ΛCDM" | "with matched physical assumptions and strongly boosted settings" | Lewis 2026, arXiv:2607.14854, section 9 | [src] |
| Cost of one massive neutrino | CLASS 1.5 times slower; "about 5 times in other codes" | fixed accuracy requirements, 2011 | Lesgourgues & Tram 2011, arXiv:1104.2935 | [src] |
| Precision settings both codes need for Euclid forecasts | established, not a single number | weak lensing, photometric and spectroscopic clustering Fisher forecasts | Casas et al. 2023, arXiv:2303.09451 | [src] |

### 1.2 CAMB v2 default accuracy (arXiv:2607.14854)

| Statement | Value | Conditions | Flag |
|---|---|---|---|
| Design target of the unboosted defaults | 10⁻³ pointwise agreement with a boosted reference, for interior lensed CMB spectra and quasi-linear matter power; looser at spectrum ends, in the high-ℓ tail and in the non-linear regime | harness `camb.check_accuracy`, grid of more than a hundred parameter files (curvature, neutrino hierarchies, N_eff, dynamical dark energy, tensors) | [src, section 9] |
| Likelihood-level size of the default error | median Δχ² ≃ 0.4, maximum ≃ 1.0 | SO-like Gaussian proxy over 2 ≤ ℓ ≤ min(4000, ℓ_max), about one hundred CMB models | [src, section 9] |
| CAMB v1.6.6 with the same high-k lensing support (`lens_potential_accuracy=5`) | below 10⁻³ up to ℓ ∼ 1900; 2.6 % in TT, 1.1 % in EE and 14 % in lensed BB at ℓ = 4000; Δχ² ≃ 10² | flat ΛCDM, ℓ_max = 4000, against the boosted reference | [src, section 9] |
| CAMB v1.6.6 with its historical default lensing cutoff, max(kη₀) = 10375 | 1.5 % error in TT by ℓ = 3000; Δχ² ≃ 6 × 10³ | same model and proxy | [src, section 9] |
| Current default lensing source range | max(kη₀) = 90000, or k_max = 6.36 Mpc⁻¹ | Planck-2018 ΛCDM model, lensed spectra to ℓ_max = 4000 | [src, section 11] |
| Edge effect in CLASS lensed spectra | 1.8 × 10⁻² at ℓ = 4000 when stopping at ℓ = 4000 instead of computing to 6000 and truncating | CLASS v3.3.4, `cl_permille` settings | [src, section 11] |
| Effect of the CLASS CMB source cutoff | 2.2 × 10⁻³ in the TT, EE, TE envelope at ℓ = 4000 | CLASS default cutoff against the high-k cutoff | [src, section 11] |

### 1.3 Timings quoted in the CAMB v2 paper

Four threads on "a typical laptop"; flat case: Planck-2018 ΛCDM with m_ν = 0.06 eV, lensed spectra to ℓ_max = 4000 (arXiv:2607.14854, table in section 11) [src].

| Case | CPU [s] | Wall [s] |
|---|---|---|
| CAMB current default | 4.2 | 1.1 |
| CAMB v1.6.6, same high-k support | 5.0 | 1.3 |
| CAMB v1.6.6, historical low-k default | 2.8 | 0.70 |
| CLASS default, ℓ = 4000 | 13 | 4.3 |
| CLASS `cl_permille`, ℓ = 4000 | 14 | 4.6 |
| CLASS default, high-k, ℓ = 6000 → 4000 | 17 | 5.3 |
| CLASS `cl_permille`, high-k, ℓ = 6000 → 4000 | 20 | 6.1 |
| Non-flat, 10-model geometric mean: CAMB current default | 5.8 | 1.5 |
| Non-flat: CAMB v1.6.6, same high-k support | 98 | 25 |
| Non-flat: CLASS default | 18 | 4.4 |
| Non-flat: CLASS `cl_permille` | 32 | 7.6 |

The paper notes that the non-flat CLASS timings exclude hyperspherical-Bessel table precomputation, and that the non-flat CAMB cost fell by a factor of 17 between v1.6.6 and v2.
These timings come from the author of one of the two codes; the 2011 comparison (section 1.1) came from the author of the other and found the opposite ordering.

### 1.4 Modified-gravity and differentiable solvers

| Statement | Value | Conditions | Citation | Flag |
|---|---|---|---|---|
| Agreement between Einstein–Boltzmann solvers with modified gravity | "sub-percent level" on the CMB angular power spectrum and the dark-matter power spectrum | three general scalar-tensor codes, three Jordan–Brans–Dicke codes, f(R), covariant Galileon, Hořava–Lifshitz and non-local gravity codes | Bellini et al. 2017, arXiv:1709.09135 | [src] |
| hi_class quasi-static approximation | "order-of-magnitude improvement in computing performance without sacrificing accuracy" | wide classes of Horndeski models | arXiv:1909.01828 | [src] |
| H-EFTCAMB Horndeski module | validated internally against EFTCAMB models and externally against hi_class; no number in the abstract | covariant Horndeski Lagrangians | arXiv:2603.01662 | [src] |
| MGCLASS II | "good agreement with the results existing in the literature" | parameterisations used by the Planck collaboration | arXiv:2112.14175 | [src] |
| DISCO-EB against CAMB and CLASS | "per-mille level" | including massive neutrinos and a dark-energy fluid | arXiv:2311.03291 | [src] |
| Chebyshev against cubic-spline interpolation in k and ℓ | 10⁻⁴–10⁻⁵ relative error with 50–80 points per variable, against about 10⁻⁴ with 200 points; a 2.5–4 times speed-up | typical CMB temperature spectrum, SymBoltz | Sletmoen 2026, arXiv:2608.24682 | [src] |

### 1.5 Ingredients inside the solvers

| Ingredient | Stated accuracy | Conditions | Citation | Flag |
|---|---|---|---|---|
| HYREC-2 recombination | "no noticeable bias in any cosmological parameters even in the case of an ideal cosmic-variance limited experiment up to ℓ = 5000"; runs in under one millisecond | 99.7 % confidence region allowed by Planck | arXiv:2007.14114 | [src] |
| HMcode-2020 non-linear P(k) | RMS error 2.5 %; "rarely exceeds 5 per cent and never exceeds 16 per cent" | k < 10 h Mpc⁻¹, z < 2, against simulations | arXiv:2009.01858 | [src] |
| HMcode-2020 feedback response | matched at the < 1 % level | z < 1, k < 20 h Mpc⁻¹, against hydrodynamical simulations | arXiv:2009.01858 | [src] |
| Takahashi halofit | 5 % for k ≤ 1 h Mpc⁻¹ (the abstract goes on to a looser figure at smaller scales, not read) | fitted over k ≤ 30 h Mpc⁻¹, 0 ≤ z ≤ 10, 16 models around WMAP best fits | arXiv:1208.2701 | [src] |
| Standard-model N_eff | 3.0440 ± 0.0002 | flavour oscillations, finite-temperature QED to O(e³), full collision integral | Bennett et al. 2020, arXiv:2012.02726 | [src] |
| Reionisation-heating convention in the linear P(k) | about 1 % at k ∼ 1 Mpc⁻¹ at z = 0; several tens of per cent by k ∼ 10–20 Mpc⁻¹ | switching on CAMB's optional homogeneous heating, T_reion = 10⁴ K, z_re = 7.7; "only indicative" | arXiv:2607.14854, section 14 | [src] |

## 2. Theory facades: validated accuracy

| Statement | Value | Conditions | Citation | Flag |
|---|---|---|---|---|
| CCL correlation-function predictions | "within a fraction of the expected statistical uncertainty of the observables" | clustering, galaxy–galaxy lensing and cosmic shear, models and scales of interest to LSST | arXiv:1812.05995 | [src] |
| Non-Limber angular spectra, N5K challenge | FKEM (CosmoLike) "produces the fastest run time within the required accuracy by a considerable margin" | fiducial 3x2pt LSST Year 10 scenario; three methods compared (FKEM, Levin, matter) | arXiv:2212.04291 | [src] |
| CLOE against benchmark codes | "all the summary statistics of interest always differ less than 0.1 σ from the chosen benchmark" | Euclid photometric and spectroscopic observables | Euclid Collaboration 2025, arXiv:2510.09141 | [src] |
| jax-cosmo | no accuracy figure in the abstract | — | arXiv:2302.05163 | — |

The pyccl default for the non-Limber method is `non_limber_integration_method='FKEM'`, with `l_limber=-1` and `limber_max_error=0.01` [src: pyccl 3.3.6 installed, `angular_cl` signature].

## 3. Samplers: documented comparisons

| Statement | Value | Conditions | Citation | Flag |
|---|---|---|---|---|
| MultiNest against PolyChord | MultiNest "reports inconsistent estimates of the Bayesian evidence and somewhat narrower parameter credible intervals" | full DES Y1 likelihood and a fast approximate likelihood | Lemos et al. 2022, arXiv:2202.08233 | [src] |
| Nested samplers against Metropolis–Hastings | "good agreement" | same study | arXiv:2202.08233 | [src] |
| nautilus sampling efficiency | "substantially higher than that of all other samplers, often by more than an order of magnitude" | compared with emcee, dynesty, UltraNest and pocoMC on synthetic problems and applications | arXiv:2306.16923 | [src] |
| pocoMC against nested sampling | about 50 and 25 times faster | primordial-feature analysis and gravitational-wave inference | arXiv:2207.05652 | [src] |
| Fast–slow decorrelation with dragging | speed-up "by a factor of five or more" | Planck likelihoods with dozens of fast nuisance parameters | Lewis 2013, arXiv:1304.4473 | [src] |
| Cobaya overhead | "sub-millisecond overhead per posterior evaluation" | — | arXiv:2005.05290 | [src] |
| MontePython 3 proposal adaptation | "can save many hundreds of CPU-hours" | runs with poor prior knowledge of the covariance | arXiv:1804.07261 | [src] |
| HMC with emulators against nested sampling without | speed-up factor O(10³) | Stage IV cosmic shear, 37 parameters; a 157-parameter combination of three surveys is also sampled | Piras & Spurio Mancini 2023, arXiv:2305.06347 | [src] |
| GPU nested sampling | Bayes factors with error bar "in just 2 days on a single A100 GPU"; a further factor of 4 from interpolating the matter power spectrum | 39-dimensional ΛCDM against w0wa cosmic-shear analysis | Lovick et al. 2025, arXiv:2509.13307 | [src] |
| NUTS against MALA and Metropolis–Hastings on emulated likelihoods | NUTS "generally converges in the fewest samples", but by wall time "MALA and even standard MH remain highly competitive" | differentiable neural-network likelihood emulators, ΛCDM and a sterile-neutrino extension | Nygaard et al. 2026, arXiv:2606.04895 | [src] |
| candl derivative-based uses | Fisher matrices without finite differences; NUTS sampling of CMB data | SPT-3G 2018 TT/TE/EE | arXiv:2401.13433 | [src] |

The DES Y3 analyses adopted PolyChord as "a good balance of speed and robustness" (arXiv:2202.08233) [src]; DES Y6 and KiDS-Legacy use nautilus [sec: sibling skill `cosmo-statistics-inference`].

## 4. Perturbation-theory codes against each other

| Statement | Value | Conditions | Citation | Flag |
|---|---|---|---|---|
| velocileptors, PyBird and FOLPSν predictions | "in close agreement with one another up to scales of k_max ≃ 0.25 h Mpc⁻¹ and at the level of precision of 8 (h⁻¹ Gpc)³ survey volumes" | AbacusSummit cubic mocks; LRG z = 0.8, ELG z = 1.1, QSO z = 1.4; n_s fixed; ΛCDM | Maus et al. 2024, arXiv:2404.07272, conclusion | [src] |
| Difference between theory multipoles | O(1 %) for k ≤ 0.25 h Mpc⁻¹ | same ΛCDM parameters, other parameters fitted independently | arXiv:2404.07272, conclusion (footnote) | [src] |
| Where the models start to deviate | k_max ∼ 0.26 h Mpc⁻¹ or higher, attributed to the limit of one-loop theory and not to disagreement between the theories | noiseless data generated by one code and fitted by the others | arXiv:2404.07272, conclusion | [src] |
| Range planned as fiducial for DESI DR1 | 0.02 < k ≲ 0.2 h Mpc⁻¹ | — | arXiv:2404.07272, conclusion | [src] |
| ShapeFit against Full-Modelling with PyBird | consistent "at the ∼ 0.5 σ level" in ΛCDM; both consistent with the truth to k_max = 0.20 h Mpc⁻¹ including the hexadecapole | DESI-like cubic boxes | Lai et al. 2024, arXiv:2404.07283 | [src] |
| FOLPSν modelling error | "fully sub-dominant for the DESI statistical precision within the studied range of scales" | AbacusSummit LRG, ELG, QSO | Noriega et al. 2024, arXiv:2404.07269 | [src] |
| Configuration-space pipeline | recovers the mock parameters "within 1 σ in all cases for a 1-year DESI volume" | Gaussian streaming model with CLPT and EFT | arXiv:2404.07268 | [src] |
| Blinded EFT challenge | two independent teams recovered H₀, Ω_m and the clustering amplitude "within sub-percent statistical errors" | mocks mimicking BOSS with a hundred times larger cumulative volume | Nishimichi et al. 2020, arXiv:2003.08277 | [src] |
| Effort.jl against PyBird | posterior "deviations compatible with Monte Carlo noise" | large-volume simulations and BOSS | arXiv:2501.04639 | [src] |
| `elf` numerical error | relative errors of order 0.01 % at k ≲ 1 h Mpc⁻¹ against brute-force integration | Eulerian and Lagrangian one-loop spectra | arXiv:2610.08023 | [src] |
| Infrared-resummation inaccuracies reported by the `neckar` authors | errors "of the order of 1 % for the quadrupole, and of 10 % for the hexadecapole at scales k ≳ 0.1 h Mpc⁻¹" in a previous implementation | Eulerian EFTofLSS | Harder et al. 2026, arXiv:2610.03466 | [src] |

Timings stated by the papers:

| Code | Time per evaluation | Conditions | Citation | Flag |
|---|---|---|---|---|
| CLASS-PT | ∼ 0.3 s for an end-to-end run for one cosmology | 2020 | arXiv:2004.10607 | [src] |
| PyBird-JAX | 1.2 ms on a CPU, 0.2 ms on a GPU; "3–4 orders of magnitude speed-up over PyBird" | redshift-space multipoles, with internal emulators | arXiv:2507.20990 | [src] |
| `elf` | "a few milliseconds on a GPU, after just-in-time compilation" | EPT and LPT spectra | arXiv:2610.08023 | [src] |
| `neckar` | "up to two orders of magnitude faster than similar existing codes without relying on emulators" | — | arXiv:2610.03466 | [src] |
| FAST-PT | "fast enough to embed in Monte Carlo Markov Chain parameter estimation"; no figure in the abstract | — | arXiv:1603.04826 | [src] |

The conclusion of arXiv:2404.07272 also records the history behind the comparison: earlier EFT analyses of BOSS and eBOSS obtained σ8 constraints "in mild tension with one another", differences that "can usually be attributed to the settings of pipelines used and modeling choices" [src].

## 5. Estimators: accuracy and speed

| Statement | Value | Conditions | Citation | Flag |
|---|---|---|---|---|
| Corrfunc speed | a projected correlation function w_p(r_p) for about 1 million galaxies "within a few seconds on a single thread" | — | arXiv:1911.03545 | [src] |
| NaMaster validation | recovers the input power spectra "in the most complex scenarios with no detectable bias" | validation suite resembling next-generation LSS and ground-based CMB observations | arXiv:1809.09603 | [src] |
| TreeCorr default tolerance | `bin_slop` chosen so that `bin_slop × bin_size` = 0.1, or `bin_slop` = 1 when `bin_size` < 0.1 | logarithmic binning; the documentation recommends halving `bin_slop` as a convergence test | [src: TreeCorr 5.1 documentation via context7] | [src] |
| FlowPM against a Python particle-mesh code | "on an average 10x speed-up in terms of wallclock time" | — | arXiv:2010.11847 | [src] |
| DISCO-DJ particle-mesh | 6 time steps for per-cent-level accuracy in the present-day power spectrum at k ≈ 0.2 h Mpc⁻¹ with N = 512³ particles, "which takes just a few seconds" | BullFrog integrator, GPU | arXiv:2510.05206 | [src] |
| Lyα BAO pipeline (picca + Vega) on mocks | model "able to recover unbiased measurements of the BAO position" | 150 synthetic realisations of DESI DR1 | Cuceu et al. 2024, arXiv:2404.03004 | [src] |
| Lyα full-shape fit on mocks | unbiased D_M/D_H(z_eff) with r_min = 25 h⁻¹ Mpc | one hundred eBOSS synthetic data sets | Cuceu et al. 2022, arXiv:2209.12931 | [src] |

No paper comparing pypower with nbodykit, or pycorr with TreeCorr, was found this session; see `Not verified`.

## 6. Emulators and differentiable codes: stated accuracy and speed-up

| Emulator | Stated accuracy | Range | Speed | Citation | Flag |
|---|---|---|---|---|---|
| CosmoPower, matter P(k) | emulation error below 0.4 % | k ∈ [10⁻⁵, 10] Mpc⁻¹, z ∈ [0, 5] | "orders-of-magnitude acceleration" | arXiv:2106.03846 | [src] |
| CosmoPower, CMB | error ≲ 10 % of the expected shot noise for the Simons Observatory | 5 σ region around the Planck best fit | — | arXiv:2106.03846 | [src] |
| High-accuracy CosmoPower emulators | CMB better than 0.5 % out to ℓ = 10⁴; P(k) to the same level out to k = 50 Mpc⁻¹ | ΛCDM, wCDM, N_eff, Σm_ν models; validated against CLASS and CAMB | "on a laptop" | arXiv:2303.01591 | [src] |
| CAMB emulators of the CosmoPower framework | recovered parameters "well within 0.1 σ of the input cosmology" in a cosmic-variance-limited experiment | ΛCDM and one- or two-parameter extensions including w0wa | "typically ≲ 1/50 of the evaluation time" | arXiv:2405.07903 | [src] |
| Capse.jl | emulation errors below 0.1 σ for all scales relevant for CMB-S4 | CMB TT, polarisation, lensing | "a few microseconds" per prediction; trained in an hour on 8 cores; a Planck TT+TE+EE analysis "in less than a second" with the fastest combination | arXiv:2307.14339 | [src] |
| LaCE, Gaussian process | sub-per-cent prediction of P1D in a Σm_ν = 0.3 eV cosmology not in the training set | 2 < z < 4 | — | arXiv:2011.15127 | [src] |
| LaCE, neural network | sub-per-cent precision; 1 % for ionisation and thermal histories not in the training set | k∥ = 0.1 to 4 Mpc⁻¹, z = 2 to 4.5 | — | arXiv:2305.19064 | [src] |
| lym1d on the Lyssa suite | "percent level accuracy" against a previous emulator; each simulation converged at the sub-per-cent level | 18 Nyx simulations, 4096³ cells, 120 Mpc box | — | arXiv:2412.05372 | [src] |
| ForestFlow | 3 % for P3D and 1.5 % for P1D | to k = 5 Mpc⁻¹ and k∥ = 4 Mpc⁻¹; 30 fixed-and-paired simulations, z = 2 to 4.5 | — | arXiv:2409.05682 | [src] |

## 7. History of the numbers that changed

| Quantity | Older value | Current value | Where each is still found | Flag |
|---|---|---|---|---|
| Default N_eff | 3.046 | 3.044 | 3.044 in camb 2.0.4 (`nnu`), pyccl 3.3.6 (`Neff`), cosmoprimo 1.0.0 (`N_eff`) and CLASS v3.2.3 (`N_ur` in `explanatory.ini`); 3.046 in astropy `Planck15` and `Planck18`; 3.04 is the default of astropy `FlatLambdaCDM` | [src: installed packages and checkout] |
| CAMB lensing source cutoff | max(kη₀) = 10375 (v1.x default, "tuned for Planck-era requirements") | max(kη₀) = 90000 (v2 default) | arXiv:2607.14854, sections 9 and 11 | [src] |
| CAMB `lens_potential_accuracy` | 0 "to reproduce the previous low-accuracy default" | `None`, meaning max(4, (ℓ_max − 1500)/500) | camb 2.0.4 `set_for_lmax` docstring | [src: installed] |
| CAMB against CLASS speed | CLASS about 2.5 times faster (2011) | CAMB v2 default 1.1 s against 4.3 s wall for CLASS default (2026, four threads, ℓ_max = 4000) | arXiv:1104.2934; arXiv:2607.14854 | [src] |
| HMcode | 2015 and 2016 versions | `mead2020` is the CAMB default version | camb 2.0.4 | [src: installed] |
| EFTCAMB | EFTCAMB | H-EFTCAMB, "the official successor" | arXiv:2603.01662 | [src] |
| DES sampler | MultiNest (Y1) | PolyChord (Y3), nautilus (Y6) | arXiv:2202.08233; sibling `cosmo-statistics-inference` | [src], [sec] |

## Not verified

- No quantitative cross-check between FFT power-spectrum estimators (pypower against nbodykit) or between pair counters (pycorr or Corrfunc against TreeCorr) was read.
- The numerical accuracy table of the CCL paper (per-quantity tolerances) was not read; only the abstract statement is given.
- The second half of the Takahashi halofit accuracy sentence was truncated in the text read.
- The CAMB v2 tolerance table (its appendix "Accuracy parameters") was not read.
- No accuracy figure was read for desilike's Taylor or MLP emulators.
