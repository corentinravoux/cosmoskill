# Maintenance status, superseded codes and misconceptions

Scope: which codes are actively maintained, which are deprecated or superseded and by what, method debates between code families, and the misconceptions about codes that still circulate.

Snapshot: 2026-10-14

Dates are the last push to the GitHub repository (any branch) and the latest PyPI upload, as given by the GitHub REST API (`https://api.github.com/repos/<owner>/<repo>`) and the PyPI JSON API (`https://pypi.org/pypi/<name>/json`). Rows that carry a doc flag were re-read on the date of the flag, and their dates are those of that day; rows without one were read on 2026-10-11 and 2026-10-12; the table headings refer to the 2026-10-14 snapshot. A recent push shows activity, not a tested release; an old push shows a quiet repository, not a broken code.

## 1. Maintenance status at the repositories
<!-- key: maintenance-status-at-the-repositories -->

### 1.1 Pushed within the three months before the snapshot
<!-- key: pushed-within-the-three-months-before-the -->

| Code | Last push | Latest tagged or indexed release |
|---|---|---|
| CAMB | 2026-10-14 | GitHub release 2.0.3 of 2026-08-24; PyPI 2.0.5 of 2026-10-14 [doc: https://api.github.com/repos/cmbant/CAMB/releases/latest; https://api.github.com/repos/cmbant/CAMB; https://pypi.org/pypi/camb/json, 2026-10-26] |
| CLASS | 2026-10-04 | PyPI classy 3.4.1.0 of 2026-10-05 (no GitHub "release" object) [doc: https://api.github.com/repos/lesgourg/class_public; https://pypi.org/pypi/classy/json, 2026-10-26] |
| EFTCAMB / H-EFTCAMB | 2026-09-17 | none tagged |
| hi_class | 2026-09-16 | GitHub release v2.0 of 2019-09-11 |
| CLASS-PT | 2026-09-18 | GitHub release v2.0 of 2022-01-15 |
| class_sz | 2026-08-07 | PyPI classy_sz 0.1.70.post40 of 2025-12-12 [doc: https://api.github.com/repos/CLASS-SZ/class_sz; https://pypi.org/pypi/classy_sz/json, 2026-10-26] |
| SymBoltz.jl | 2026-10-09 | not read |
| cosmoprimo | 2026-10-15 | none tagged; not on PyPI [doc: https://api.github.com/repos/cosmodesi/cosmoprimo; https://pypi.org/pypi/cosmoprimo/json (404), 2026-10-26] |
| pyccl | 2026-10-14 | PyPI 3.3.6 of 2026-07-28 [doc: https://api.github.com/repos/LSSTDESC/CCL; https://pypi.org/pypi/pyccl/json, 2026-10-26] |
| astropy | 2026-10-26 | PyPI 8.0.2 of 2026-10-15 [doc: https://api.github.com/repos/astropy/astropy; https://pypi.org/pypi/astropy/json, 2026-10-26] |
| cloelib | 2026-10-12 | not read |
| Cobaya | 2026-08-25 | PyPI 3.6.2 of 2026-03-27 [doc: https://api.github.com/repos/CobayaSampler/cobaya; https://pypi.org/pypi/cobaya/json, 2026-10-26] |
| CosmoSIS | 2026-10-16 | PyPI 3.26 of 2026-09-03 [doc: https://api.github.com/repos/cosmosis-developers/cosmosis; https://pypi.org/pypi/cosmosis/json, 2026-10-26] |
| desilike | 2026-10-09 | none tagged; not on PyPI |
| emcee | 2026-10-24 | PyPI 3.1.6 of 2024-04-19 [doc: https://api.github.com/repos/dfm/emcee; https://pypi.org/pypi/emcee/json, 2026-10-26] |
| dynesty | 2026-10-26 | PyPI 3.1.0 of 2026-07-17 [doc: https://api.github.com/repos/joshspeagle/dynesty; https://pypi.org/pypi/dynesty/json, 2026-10-26] |
| nautilus | 2026-10-21 | PyPI 1.0.6 of 2025-12-29 [doc: https://api.github.com/repos/johannesulf/nautilus; https://pypi.org/pypi/nautilus-sampler/json, 2026-10-26] |
| NumPyro | 2026-10-22 | PyPI 0.22.0 of 2026-09-18 [doc: https://api.github.com/repos/pyro-ppl/numpyro; https://pypi.org/pypi/numpyro/json, 2026-10-26] |
| BlackJAX | 2026-10-08 | PyPI 1.7.1 of 2026-10-02 [doc: https://api.github.com/repos/blackjax-devs/blackjax; https://pypi.org/pypi/blackjax/json, 2026-10-26] |
| UltraNest | 2026-10-26 | PyPI 4.6.3 of 2026-10-13 [doc: https://api.github.com/repos/JohannesBuchner/UltraNest; https://pypi.org/pypi/ultranest/json, 2026-10-26] |
| GetDist | 2026-08-05 | PyPI 1.7.7 of 2026-05-08 [doc: https://api.github.com/repos/cmbant/getdist; https://pypi.org/pypi/getdist/json, 2026-10-26] |
| FAST-PT (`jablazek/FAST-PT`) | 2026-10-23 | PyPI 4.1.1 of 2026-10-20 [doc: https://api.github.com/repos/jablazek/FAST-PT; https://pypi.org/pypi/fast-pt/json, 2026-10-26] |
| TreeCorr | 2026-09-01 | PyPI 5.1.4 of 2026-09-01 [doc: https://api.github.com/repos/rmjarvis/TreeCorr; https://pypi.org/pypi/treecorr/json, 2026-10-26] |
| NaMaster | 2026-08-05 | PyPI pymaster 3.0.1 of 2026-08-04 [doc: https://api.github.com/repos/LSSTDESC/NaMaster; https://pypi.org/pypi/pymaster/json, 2026-10-26] |
| Corrfunc | 2026-08-16 | PyPI 2.5.3 of 2024-08-06 [doc: https://api.github.com/repos/manodeep/Corrfunc; https://pypi.org/pypi/corrfunc/json, 2026-10-26] |
| Triumvirate | 2026-10-23 | PyPI 0.5.0 of 2024-08-09 [doc: https://api.github.com/repos/MikeSWang/Triumvirate; https://pypi.org/pypi/triumvirate/json, 2026-10-26] |
| pyrecon | 2026-09-17 | none tagged |
| picca | 2026-10-21 | PyPI 9.21.7 of 2026-10-21 [doc: https://api.github.com/repos/igmhub/picca; https://pypi.org/pypi/picca/json, 2026-10-26] |
| Vega | 2026-10-14 | GitHub release v1.8.0 of 2026-10-10 [doc: https://api.github.com/repos/andreicuceu/vega/releases/latest; https://api.github.com/repos/andreicuceu/vega, 2026-10-26] |
| LaCE, ForestFlow | 2026-10-07, 2026-10-11 | not on PyPI |
| healpy | 2026-10-23 | PyPI 1.20.1 of 2026-10-03 [doc: https://api.github.com/repos/healpy/healpy; https://pypi.org/pypi/healpy/json, 2026-10-26] |
| flip | 2026-10-26 | PyPI flipcosmo 2.0.10 of 2026-09-09 [doc: https://api.github.com/repos/corentinravoux/flip; https://pypi.org/pypi/flipcosmo/json, 2026-10-26] |
| JaxPM | 2026-09-28 | PyPI 0.1.6 of 2025-06-29 [doc: https://api.github.com/repos/DifferentiableUniverseInitiative/JaxPM; https://pypi.org/pypi/jaxpm/json, 2026-10-26] |
| Capse.jl, Effort.jl | 2026-09-28, 2026-08-30 | not read |

### 1.2 Quieter repositories
<!-- key: quieter-repositories -->

| Code | Last push | Latest release | Reading |
|---|---|---|---|
| velocileptors | 2026-04-23 | PyPI 3.1 of 2026-04-23 [doc: https://api.github.com/repos/sfschen/velocileptors; https://pypi.org/pypi/velocileptors/json, 2026-10-26] | released in 2026 |
| PyBird | 2026-05-13 | PyPI pybird-lss 0.3.2 of 2025-08-02 [doc: https://api.github.com/repos/pierrexyz/pybird; https://pypi.org/pypi/pybird-lss/json, 2026-10-26] | active in 2026 |
| pmwd | 2026-06-12 | no PyPI record under that name | active in 2026 |
| lym1d | 2026-06-15 | — | active in 2026 |
| candl | 2026-06-05 | PyPI candl-like 2.2.0 of 2025-10-10 [doc: https://api.github.com/repos/Lbalkenhol/candl; https://pypi.org/pypi/candl-like/json, 2026-10-26] | active in 2026 |
| DISCO-DJ | 2026-05-16 (repository created 2025-09-23) | — | new code |
| pypower | 2026-03-27 | none tagged; `pypower/_version.py` on `main` gives 1.0.0 [doc: https://api.github.com/repos/cosmodesi/pypower; cosmodesi/pypower/pypower/_version.py, 2026-10-26] | pushed in 2026 |
| PolyChordLite | 2026-02-26 | GitHub release 1.22.2 of 2025-11-25 [doc: https://api.github.com/repos/PolyChord/PolyChordLite/releases/latest; https://pypi.org/pypi/pypolychord/json, 2026-10-26] | maintained; its PyPI record is stale |
| pycorr | 2026-01-13 | none tagged | pushed in 2026 |
| DISCO-EB | 2025-11-13 | — | — |
| MGCAMB | 2025-11-07 | none tagged | — |
| nbodykit | 2025-11-07 | PyPI 0.3.16 of 2025-08-14 [doc: https://api.github.com/repos/bccp/nbodykit; https://pypi.org/pypi/nbodykit/json, 2026-10-26] | maintenance releases |
| cosmopower-jax | 2025-11-27 | PyPI 0.5.8 of 2025-11-28 [doc: https://api.github.com/repos/dpiras/cosmopower-jax; https://pypi.org/pypi/cosmopower-jax/json, 2026-10-26] | — |
| pocoMC | 2025-09-11 | PyPI 1.2.6 of 2024-09-20 [doc: https://api.github.com/repos/minaskar/pocomc; https://pypi.org/pypi/pocomc/json, 2026-10-26] | — |
| FOLPS-nu | 2025-06-22 | — | the JAX port `folpsax` was last pushed 2024-09-10 |
| jax-cosmo | 2025-06-27 | PyPI 0.1.0 of 2023-02-05 [doc: https://api.github.com/repos/DifferentiableUniverseInitiative/jax_cosmo; https://pypi.org/pypi/jax-cosmo/json, 2026-10-26] | one indexed release, from the year of the paper |
| LensTools | 2025-06-29 | PyPI 1.2 of 2021-01-21 [doc: https://api.github.com/repos/apetri/LensTools; https://pypi.org/pypi/lenstools/json, 2026-10-26] | — |
| CosmoPower | 2024-12-21 | PyPI 0.2.0 of 2024-07-28 [doc: https://api.github.com/repos/alessiospuriomancini/cosmopower; https://pypi.org/pypi/cosmopower/json, 2026-10-26] | — |
| FAST-PT (`JoeMcEwen/FAST-PT`) | 2024-07-26 | — | development moved to `jablazek/FAST-PT` (PyPI homepage) |
| MontePython | 2024-06-20 | none tagged; not on PyPI | no push for more than two years |
| HMcode (standalone Fortran) | 2023-09-22 | — | the model lives on inside CAMB |
| MultiNest | 2022-03-01 | pymultinest 2.12 of 2023-07-28 [doc: https://api.github.com/repos/farhanferoz/MultiNest; https://pypi.org/pypi/pymultinest/json, 2026-10-26] | no push for more than four years |
| CosmoMC | 2022-01-14 | — | see section 2 |
| FlowPM (`modichirag/flowpm`) | 2021-04-25 | — | no push for more than five years |

## 2. Deprecated or superseded codes
<!-- key: deprecated-or-superseded-codes -->

| Older code or version | Successor | Evidence |
|---|---|---|
| CosmoMC | Cobaya | The Cobaya documentation describes its MCMC sampler as "the Markov Chain Monte Carlo Metropolis sampler used by CosmoMC" [doc: https://cobaya.readthedocs.io/en/latest/sampler_mcmc.html, 2026-10-26]; the CosmoMC repository was last pushed on 2022-01-14 [doc: https://api.github.com/repos/cmbant/CosmoMC, 2026-10-26]. MGCAMB added a Cobaya interface in 2023 (arXiv:2305.05667) and H-EFTCAMB is built around Cobaya (arXiv:2603.01662). |
| EFTCAMB | H-EFTCAMB | "the official successor to EFTCAMB" (arXiv:2603.01662); the repository `EFTCAMB/EFTCAMB` now carries the H-EFTCAMB README [doc: https://raw.githubusercontent.com/EFTCAMB/EFTCAMB/HEAD/README.md, 2026-10-26]. |
| MGCAMB (2008 release) | MGCAMB of 2011 and later | The 2011 patch "replaces the previously publicly released code MGCAMB" (arXiv:1106.4543); the 2019 and 2023 versions follow (arXiv:1901.05956, arXiv:2305.05667). |
| CAMB v1.x (last release v1.6.6) | CAMB v2 | arXiv:2607.14854; default accuracy and lensing support changed (see `results.md`, section 1.2). pyccl 3.3.6 still requests the v1 behaviour through `AccuracyTarget` = 0 [doc: installed pyccl 3.3.6, pyccl/boltzmann.py, 2026-10-26]. |
| picca `fitter2` | Vega | Vega "is based on picca fitter2" [doc: https://raw.githubusercontent.com/andreicuceu/vega/master/README.rst, 2026-10-26]; the picca README sends model computation and fitting to Vega [doc: https://raw.githubusercontent.com/igmhub/picca/main/README.md, 2026-10-26]. |
| HMcode 2015 and 2016 | HMcode-2020 | `mead2020` is the default `halofit_version` of camb 2.0.4; the older versions remain selectable [doc: installed camb 2.0.4, camb/nonlinear.py, 2026-10-26]. |
| N_eff = 3.046 | N_eff = 3.044 | arXiv:2012.02726; current code defaults in `results.md`, section 7. |
| FAST-PT original repository | `jablazek/FAST-PT` | PyPI homepage of `fast-pt` 4.1.1 [doc: https://pypi.org/pypi/fast-pt/json, 2026-10-26]. |
| FlowPM (TensorFlow) | JAX particle-mesh codes (JaxPM, pmwd, DISCO-DJ) | Inferred from repository activity only: FlowPM was last pushed in 2021, the JAX codes in 2026. No statement of succession was read. |
| MultiNest for DES-type posteriors | PolyChord, then nautilus | arXiv:2202.08233; sibling `cosmo-statistics-inference`. |
| `pypolychord` on PyPI | PolyChordLite from GitHub | PyPI record 1.15.1 of 2019-01-17 against GitHub release 1.22.2 of 2025-11-25 [doc: https://pypi.org/pypi/pypolychord/json; https://api.github.com/repos/PolyChord/PolyChordLite/releases/latest, 2026-10-26]. |

Not superseded, despite appearances: MontePython has no recent push, but MGCLASS II (arXiv:2112.14175) and the Euclid forecast validation (arXiv:2303.09451) rely on it, and desilike keeps a binding to it [doc: https://raw.githubusercontent.com/cosmodesi/desilike/main/README.md, 2026-10-26].

## 3. Method debates
<!-- key: method-debates -->

### 3.1 Exact fast codes, differentiable codes or emulators
<!-- key: exact-fast-codes-differentiable-codes-or -->

Three routes now compete to make full-shape and CMB inference fast.

- Emulate the expensive step: CosmoPower and its descendants (arXiv:2106.03846, arXiv:2303.01591, arXiv:2405.07903), Capse.jl (arXiv:2307.14339), Effort.jl (arXiv:2501.04639), PyBird-JAX with internal emulators (arXiv:2507.20990).
- Make the exact code differentiable: DISCO-EB (arXiv:2311.03291), SymBoltz (arXiv:2608.24682), `elf` (arXiv:2610.08023), candl (arXiv:2401.13433).
- Make the exact code fast enough without either: `neckar` claims "up to two orders of magnitude faster than similar existing codes without relying on emulators" (arXiv:2610.03466, abstract); CAMB v2 targets 10⁻³ default accuracy (arXiv:2607.14854, Sect. IX) at 1.1 s wall time for ℓ_max = 4000 (arXiv:2607.14854, Sect. XI, Table 1).

What decides between them is the model space: an emulator is tied to its training ranges and precision settings, while an exact code extends to a new model at the price of speed.
No head-to-head study of the three routes on one likelihood was read this session.

### 3.2 Which sampler
<!-- key: which-sampler -->

- Nested sampling gives evidences but its accuracy depends on the implementation: the DES study found MultiNest unreliable for evidences and intervals where PolyChord was not (arXiv:2202.08233).
- Gradient-based samplers are not automatically the fastest once likelihoods are emulated: on differentiable emulators NUTS needs the fewest samples but MALA and plain Metropolis–Hastings "remain highly competitive" by wall time (arXiv:2606.04895).
- GPU nested sampling is presented as putting nested sampling back "on equal computational footing" with MCMC plus decoupled evidence estimation (arXiv:2509.13307).
- nautilus and pocoMC both claim order-of-magnitude gains over classical nested samplers (arXiv:2306.16923, arXiv:2207.05652); each comparison was made by the authors of the faster code.

### 3.3 Eulerian or Lagrangian perturbation theory
<!-- key: eulerian-or-lagrangian-perturbation-theory -->

The DESI comparison concludes that velocileptors, PyBird and FOLPSν give consistent constraints for 0.02 < k ≲ 0.2 h Mpc⁻¹ once bias freedom and scale cuts are matched, and that remaining differences are of two-loop order (arXiv:2404.07272, Sect. 6).
The open points are practical: no direct mapping of bias parameters exists between all models, priors act differently in each basis, and prior-volume (projection) effects appear when the parameter space is opened beyond ΛCDM (arXiv:2404.07272, Sect. 6 "Conclusion").
The 2026 `neckar` paper reopens the question of numerical accuracy of infrared resummation in existing Eulerian implementations (arXiv:2610.03466).

### 3.4 Code written with AI agents
<!-- key: code-written-with-ai-agents -->

The CAMB v2 abstract states that "essentially all of the new algorithms and code were developed with LLMs or AI agents under human supervision", and the paper has a section "Agentic testing and tuning" (arXiv:2607.14854).
Its accuracy claims rest on a deterministic validation harness, `camb.check_accuracy`, and on a fixed-reference regression suite (arXiv:2607.14854) [src: Sect. IX].
How collaborations will treat such code in their validation requirements is not settled in anything read this session.

### 3.5 What the next releases will decide
<!-- key: what-the-next-releases-will-decide -->

- Euclid: cloelib "is intended to serve as the reference theory computation infrastructure for Euclid's first cosmological release" (arXiv:2605.23839, Summary); CLOE agrees with benchmark codes to better than 0.1 σ (arXiv:2510.09141, abstract).

- pyccl and CAMB v2: pyccl 3.3.6 pins `AccuracyTarget` to the v1 behaviour [doc: installed pyccl 3.3.6, pyccl/boltzmann.py, 2026-10-26]; whether and when it adopts the v2 defaults, and by how much its validated predictions then move, is open.
- Lyα: ForestFlow is presented as enabling "full-scale cosmological analyses of Lyman-α forest measurements from the DESI survey" (arXiv:2409.05682).
- Which estimator and perturbation-theory codes the DESI DR2 full-shape analysis uses was not read.

## 4. Misconceptions
<!-- key: misconceptions -->

1. **"CAMB and CLASS agree to 0.01 %."** That figure is for concordance ΛCDM, a shared recombination history and tuned precision in 2011 (arXiv:1104.2934, abstract). At default settings and high ℓ the codes and versions differ at the per-cent level: CAMB v1.6.6 defaults are off by 1.5 % in TT at ℓ = 3000 (arXiv:2607.14854, Sect. IX), and CLASS lensed spectra move by 1.8 × 10⁻² at ℓ = 4000 depending on the ℓ margin (arXiv:2607.14854, Sect. XI).
2. **"CLASS is faster than CAMB."** True in the 2011 comparison, by a factor of about 2.5 (arXiv:1104.2934, abstract); the 2026 CAMB v2 paper measures the opposite for lensed spectra to ℓ_max = 4000 (arXiv:2607.14854, Sect. XI, Table 1).
 Both statements come from the author of the faster code.
3. **"The linear power spectrum is unambiguous."** At k above about 1 Mpc⁻¹ it depends on the reionisation-heating convention (arXiv:2607.14854, App. B), and in massive-neutrino cosmologies on whether the total-matter or the CDM-plus-baryon field is meant.
4. **"Halofit" names one model.** CAMB 2.0.4 lists eleven `halofit_version` names, including three HMcode generations [doc: installed camb 2.0.4, `camb.nonlinear.halofit_version_names`, 2026-10-26].
5. **"`FlatLambdaCDM(H0=70, Om0=0.3)` is a realistic cosmology."** Its defaults are `Tcmb0 = 0 K` and `m_nu = 0`, so it has no radiation and no neutrinos [doc: installed astropy 8.0.1, `FlatLambdaCDM` signature, 2026-10-26].
6. **"astropy `Planck18` is the CMB-only Planck cosmology."** Its metadata give the source as Planck 2018 Paper VI, Table 2, "TT, TE, EE + lowE + lensing + BAO" [doc: installed astropy 8.0.1, `Planck18.meta`, 2026-10-26]. cosmoprimo's `DESI()` fiducial is instead the "base_plikHM_TTTEEE_lowl_lowE_lensing mean" of AbacusSummit c000 [doc: installed cosmoprimo 1.0.0, `fiducial.DESI` docstring, 2026-10-26]. The two "Planck 2018" cosmologies are not the same.
7. **"The EFT codes disagree."** The σ8 differences between BOSS analyses came from priors, bias parameterisations and pipeline settings (arXiv:2404.07272); a blinded challenge had already recovered the truth with two independent implementations (arXiv:2003.08277).
8. **"`pip install <name>` gets the collaboration code."** Not for `pycorr`, `pyrecon` or `lace`, which are other projects on PyPI; cosmoprimo, desilike, MontePython and pmwd have no PyPI record under their own name, and Vega has none under `vega-lya` [doc: https://pypi.org/pypi/<name>/json for `pycorr`, `pyrecon`, `lace`, `cosmoprimo`, `desilike`, `montepython`, `pmwd` and `vega-lya`, 2026-10-26]. The PyPI names `pypower` and `vega` were not queried.
9. **"picca fits the correlation functions."** Since Vega, picca measures and Vega models and fits [doc: https://raw.githubusercontent.com/igmhub/picca/main/README.md; https://raw.githubusercontent.com/andreicuceu/vega/master/README.rst, 2026-10-26].
10. **"flip does field-level inference like BORG."** flip evaluates a Gaussian likelihood of the observed field values with a model covariance (arXiv:2501.16852); BORG samples initial conditions through a forward model (arXiv:1806.11117). The word "field-level" covers both.
11. **"A nested sampler gives the posterior and the evidence at the default settings."** Cobaya's own PolyChord defaults set `num_repeats: 2d`, and its documentation recommends `5d` "if accurate evidences needed or weird posterior shapes" [doc: https://cobaya.readthedocs.io/en/latest/sampler_polychord.html, 2026-10-26]; nautilus keeps exploration-phase points unless told otherwise (`discard_exploration=False`) [doc: johannesulf/nautilus/nautilus/sampler.py on `main`, 2026-10-26].
12. **"HEALPix maps are interchangeable."** Ordering (RING or NESTED), the order of polarisation spectra in `synfast` against `anafast`, and the polarisation sign convention each have two possibilities [doc: installed healpy 1.19.0, `read_map` and `synfast` signatures and docstrings; https://namaster.readthedocs.io/en/latest/api/pymaster.field.html, 2026-10-26].
13. **"`import camb` is CAMB."** In an environment where EFTCAMB was built, the module named `camb` is the patched code [doc: https://raw.githubusercontent.com/EFTCAMB/EFTCAMB/HEAD/README.md, 2026-10-26].
14. **"The repository URL in the paper is where the code lives."** CosmoSIS moved from Bitbucket to `cosmosis-developers/cosmosis`, hi_class to `hiclass-code/hi_class_public`, PolyChord from the CCPForge address of its papers to `PolyChord/PolyChordLite`, FAST-PT to `jablazek/FAST-PT` [doc: https://github.com/joezuntz/cosmosis and https://github.com/miguelzuma/hi_class_public (HTTP 301 redirects); https://github.com/PolyChord/PolyChordLite; https://pypi.org/pypi/fast-pt/json, 2026-10-26].

## Not verified
<!-- key: not-verified -->

- BORG: the public repository page `git.aquila-consortium.org/Aquila-Consortium/borg_public` was opened; its default branch is `release/2.1` [doc: https://git.aquila-consortium.org/Aquila-Consortium/borg_public, 2026-10-26]. Its initial-import date and which modules are under access control were not read there.
- Whether MontePython, CosmoPower or LensTools have newer development elsewhere than the repositories listed was not checked.
- The codes used in the DESI DR2 clustering pipeline (power-spectrum estimator, perturbation-theory code, sampler) were not read; a repository `cosmodesi/jax-power` does not exist under that name.
- No statement on the long-term maintenance of pypower and pycorr was read.
- The CLASS version history between 3.2.3 (the checkout read) and 3.4.1.0 (PyPI) was not read [doc: lesgourg/class_public/explanatory.ini at tag v3.2.3; https://pypi.org/pypi/classy/json, 2026-10-26].
