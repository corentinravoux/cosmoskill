# Traps — default units, conventions and settings of each code

Scope: the units and conventions each code uses by default (h, Mpc, k, the sigma8 field, neutrino treatment, Fourier convention, accuracy settings) and the documented cases where a default changed a published result.

Snapshot: 2026-10-14

Provenance: "installed" is a docstring or signature read in the released package at the stated version (camb 2.0.4, pyccl 3.3.6, astropy 8.0.1, healpy 1.19.0, emcee 3.1.6, cosmoprimo 1.0.0); "checkout" is the source repository read at the stated version (CLASS v3.2.3, pypower 1.0.0) or at a development state (picca, flip); "context7" is library documentation fetched on 2026-10-11. The installed versions were re-read on 2026-10-26 [doc: installed camb 2.0.4, pyccl 3.3.6, astropy 8.0.1, healpy 1.19.0, emcee 3.1.6, cosmoprimo 1.0.0, 2026-10-26]; a statement with its own doc flag was re-read at that source on the flag's date. Defaults change between versions: re-read them for the version in use.

## 1. Units of k, P(k) and distances: which codes carry h
<!-- key: units-of-k-p-k-and-distances-which-codes-carry-h -->

### 1.1 The table
<!-- key: the-table -->

| Code | k | P(k) | Distances | H(z) | Source |
|---|---|---|---|---|---|
| CAMB (`camb`) | `get_matter_power_spectrum(minkh, maxkh)` works in k/h; `get_matter_power_interpolator` has `k_hunit=True` and `hubble_units=True` by default; but `set_matter_power(kmax=...)` takes "just k, not k/h" | follows `hubble_units` | `comoving_radial_distance` in Mpc | `H0` in km/s/Mpc | installed |
| CLASS (`classy`) | `pk(k, z)`: k in 1/Mpc; `get_pk_and_k_and_z(h_units=False)` by default | Mpc³ | Mpc | — | checkout, `classy.pyx` |
| pyccl | Mpc⁻¹ | Mpc³ | Mpc | `h_over_h0` is dimensionless | installed |
| cosmoprimo | h/Mpc [der: from P in (Mpc/h)³ and the comment "K in (h/Mpc)^2"; not read in a docstring] | (Mpc/h)³ | Mpc/h (`comoving_radial_distance`, `angular_diameter_distance`) | `hubble_function` in km/s/Mpc; `efunc` dimensionless | installed |
| astropy.cosmology | no P(k) | — | `Quantity` in Mpc | `Quantity` in km/(Mpc s) | installed |
| flip | h Mpc⁻¹ | — | Mpc h⁻¹; RA and Dec in radians; velocities in km/s | — | checkout, `docs/covariance_models.md` |
| picca | — | — | Mpc/h, because the fiducial `Cosmo` class hard-codes H0 = 100 | — | [doc: igmhub/picca/py/picca/constants.py on `main`, 2026-10-26] |
| velocileptors | not stated in the README: the output is in the units of the input `klin`, `plin` | same | — | — | repository README |

### 1.2 Traps that follow
<!-- key: traps-that-follow -->

- **Mixed conventions inside CAMB.** The same object takes `kmax` in Mpc⁻¹ in `set_matter_power` and returns k/h from `get_matter_power_spectrum`. For `maxkh` the docstring says to "check consistent with input params.Transfer.kmax", which is in the other unit [doc: installed camb 2.0.4, `get_matter_power_spectrum` and `set_matter_power` docstrings, 2026-10-26].
- **CLASS has two spellings of the same input.** `P_k_max_h/Mpc` and `P_k_max_1/Mpc` are different parameters; `sigma(R, z)` takes R in Mpc unless `h_units=True`, so σ8 is `sigma(8/h, z)` [doc: https://raw.githubusercontent.com/lesgourg/class_public/v3.2.3/explanatory.ini; https://raw.githubusercontent.com/lesgourg/class_public/v3.2.3/python/classy.pyx, 2026-10-26].
- **cosmoprimo mixes on purpose.** Distances and P(k) are in h-units, but the pivot scale `k_pivot` is in Mpc⁻¹ and `hubble_function` is in km/s/Mpc [doc: installed cosmoprimo 1.0.0, cosmoprimo/cosmology.py and cosmoprimo/camb.py docstrings, 2026-10-26].
- **Passing between facades.** A pyccl P(k) handed to a code that expects h-units needs k → k/h and P → P h³; a forgotten h³ is an error of several-fold in amplitude for any realistic h [der], and a wrong k unit alone rescales every scale, the BAO position included, by h.
- **flip sits at such a boundary.** Its three engines (`classy`, `cosmoprimo`, `pyccl`) do not share units, while flip documents k in h Mpc⁻¹ and distances in Mpc h⁻¹ [doc: corentinravoux/flip/docs/power_spectra.md and docs/DataVector.md on `main`, 2026-10-26]. The engine wrappers must do the conversion; how each one does it was not read this session.
- **SN Ia distance moduli in flip.** `VelTrippRelation` requires `rcom_zobs` in Mpc/h and an explicit `h` argument to convert to Mpc inside the distance modulus [doc: corentinravoux/flip/docs/DataVector.md on `main`, 2026-10-26].
- **picca distances are always h⁻¹ Mpc.** The source comment reads: "Using H0=100 implies that we are returning the distances in Mpc/h instead of Mpc" [doc: igmhub/picca/py/picca/constants.py on `main`, 2026-10-26].
- **CAMB CMB spectra are not C_ℓ by default.** `get_cmb_power_spectra` returns ℓ(ℓ+1)C_ℓ/2π, dimensionless unless `CMB_unit='muK'`, in the order TT, EE, BB, TE; "for the lens_potential the power spectrum returned is that of the deflection" [doc: installed camb 2.0.4, `CAMBdata.get_cmb_power_spectra` docstring, 2026-10-26].
- **CAMB θ parameters are scaled.** In `get_derived_params`, "all theta__ derived parameters here are scaled by a factor of 100 for historical reasons" [doc: installed camb 2.0.4, `camb.results.CAMBdata.get_derived_params`, 2026-10-26].
- **CAMB σ8 arrays run backwards in redshift.** `get_sigma8` and `get_fsigma8` return values "in order of increasing time (decreasing redshift)" [doc: installed camb 2.0.4, `get_sigma8` and `get_fsigma8` docstrings, 2026-10-26].

## 2. Neutrinos and the definition of the matter field
<!-- key: neutrinos-and-the-definition-of-the-matter-field -->

### 2.1 Default neutrino sector
<!-- key: default-neutrino-sector -->

| Code | Default N_eff | Default masses | Hierarchy default | Source |
|---|---|---|---|---|
| CAMB `set_cosmology` | `nnu=3.044` | `mnu=0.06` eV | `neutrino_hierarchy='degenerate'` with `num_massive_neutrinos=1`: one massive eigenstate carrying the whole mass | installed |
| CLASS `explanatory.ini` | `N_ur = 3.044` | `N_ncdm` empty (no massive species); the example value is `m_ncdm = 0.06` | — | checkout |
| pyccl `Cosmology` | `Neff` defaults to 3.044 | `m_nu=0.0` | `mass_split='normal'`: a single number is split into three masses | [doc: installed pyccl 3.3.6, `pyccl.Cosmology` signature, 2026-10-26] |
| cosmoprimo `Cosmology` | `N_eff=3.044` | `m_ncdm=None` (no massive neutrinos) | `neutrino_hierarchy=None`: a single value means one massive neutrino | installed |
| cosmoprimo `Planck2018FullFlatLCDM` | 3.044 | `m_ncdm=[0.06]` | one massive neutrino | [doc: installed cosmoprimo 1.0.0, `fiducial.Planck2018FullFlatLCDM()`, 2026-10-26] |
| astropy `Planck18` | `Neff=3.046` | `m_nu=[0, 0, 0.06]` eV | — | installed |
| astropy `FlatLambdaCDM(H0, Om0)` | `Neff=3.04` | `m_nu=0` eV | — | installed |

Consequences:

- The same call "Σm_ν = 0.06 eV" gives one massive eigenstate in CAMB and cosmoprimo and three in pyccl: these are different models of the neutrino sector, so state the split [doc: installed camb 2.0.4, pyccl 3.3.6, cosmoprimo 1.0.0, 2026-10-26]. The size of the difference in P(k) was not read this session.
- CAMB v2 calls the single eigenstate carrying 0.06 eV "the standard default", because for a small fixed total the split has "a very small effect on the CMB"; its normal and inverted settings approximate three masses by two eigenstates (a near-degenerate pair and a single state) fixed by Σm_ν and the measured splittings, and the default three-point momentum quadrature rises to four and five points for heavier eigenstates (arXiv:2607.14854) [src: Sect. VI].
- A code with default `m_nu = 0` (pyccl, cosmoprimo base class, CLASS) compared with CAMB defaults differs by the 0.06 eV neutrino unless it is set by hand [doc: installed camb 2.0.4, pyccl 3.3.6, cosmoprimo 1.0.0; lesgourg/class_public/explanatory.ini at tag v3.2.3, 2026-10-26].
- The Cobaya documentation example runs `classy` with `N_ncdm: 1`, `N_ur: 2.0328` and `m_ncdm: 0.06` [doc: https://cobaya.readthedocs.io/en/latest/cosmo_basic_runs.html, 2026-10-26]: the CLASS input for the Planck baseline is three numbers, not one.
- The benchmark N_eff = 3.0440 ± 0.0002 is from arXiv:2012.02726 [src: abstract]; 3.046 survives in stored cosmologies such as astropy `Planck18` [doc: installed astropy 8.0.1, `Planck18.Neff`, 2026-10-26].

### 2.2 Which field σ8 and P(k) refer to
<!-- key: which-field-sigma8-and-p-k-refer-to -->

- CAMB: the default variable of `get_matter_power_spectrum` is `delta_tot` (total matter, with massive neutrinos); `delta_nonu` (CDM plus baryons) is a separate transfer variable [doc: installed camb 2.0.4, `camb.config.transfer_power_var` and `model.transfer_names`, 2026-10-26].
- CLASS: `pk` is total matter and `pk_cb` is CDM plus baryons; `sigma8()` and `sigma8_cb()` are separate methods [doc: https://raw.githubusercontent.com/lesgourg/class_public/v3.2.3/python/classy.pyx, 2026-10-26].
- cosmoprimo: `pk_interpolator(of='delta_m')` by default; `sigma8_z(z, of='delta_m')`; the caller selects another field through `of` [doc: installed cosmoprimo 1.0.0, `Fourier.pk_interpolator` and `Fourier.sigma8_z` signatures, 2026-10-26].
- pyccl: `sigma8` is the RMS in a top-hat sphere of 8 Mpc/h "with the value of h extracted from cosmo"; when `sigma8` is given as input, "CCL will enforce the linear matter power spectrum to be correctly normalised to this value" even with modified-gravity parameters [doc: installed pyccl 3.3.6, `pyccl.sigma8` and `pyccl.Cosmology` docstrings, 2026-10-26].
- Which of the two fields a galaxy-clustering model should be fed in a massive-neutrino cosmology is a theory question treated in the sibling `cosmo-theory-foundations`; the software check is which spectrum the pipeline actually requests from the engine.

### 2.3 Three definitions of fσ8
<!-- key: three-definitions-of-fsigma8 -->

| Code | Definition | Source |
|---|---|---|
| CAMB `get_fsigma8` | "defined as in the Planck 2015 parameter paper in terms of the velocity-density correlation: σ²_vd/σ_dd for 8 h⁻¹ Mpc spheres" | installed |
| CLASS `effective_f_sigma8` | "an estimation of f(z)*sigma8(z) at the scale of 8 h/Mpc, computed as (d sigma8/d ln a)" | checkout |
| CLASS `scale_independent_growth_factor_f` and pyccl `growth_rate` | f = d ln D / d ln a of the scale-independent growth factor; pyccl warns it "is not able to compute the scale-dependent growth rate for cosmologies with massive neutrinos" | checkout, installed |

cosmoprimo's README defines "fsigma8 as the amplitude of velocity perturbations in spheres of 8 Mpc/h", a velocity-based definition, whereas CAMB's uses the velocity–density correlation; the README also lists a `capse` emulator engine, absent from the 1.0.0 engine list of section 2 of `physics-and-methods.md` [doc: cosmodesi/cosmoprimo/README.md on `main`; installed cosmoprimo 1.0.0, 2026-10-26].
These agree in ΛCDM without massive neutrinos and differ once the growth is scale dependent.
A peculiar-velocity fσ8 compared with a "Planck prediction" should say which of the three produced the prediction.

## 3. Default accuracy and non-linear settings of Boltzmann solvers
<!-- key: default-accuracy-and-non-linear-settings-of -->

From the installed package [doc: installed camb 2.0.4, `camb.CAMBparams()` and `set_matter_power`, `set_for_lmax`, `set_cosmology` signatures, 2026-10-26]:

| Setting | CAMB 2.0.4 default | Note |
|---|---|---|
| `NonLinear` | `NonLinear_none` | linear spectra unless requested |
| `halofit_version` | `mead2020` | used only when non-linear corrections are on |
| `WantTransfer` | `False` | no P(k) unless `set_matter_power` is called |
| `Transfer.kmax`, `set_matter_power(kmax)` | 0.9; 1.2 | Mpc⁻¹ |
| `max_l`, `DoLensing` | 2500; `True` | — |
| `AccuracyBoost`, `lSampleBoost`, `lAccuracyBoost` | 1.0 each | — |
| `set_for_lmax(lens_potential_accuracy=None)` | automatic "high-accuracy default of max(4, (lmax − 1500)/500)"; 0 reproduces "the previous low-accuracy default" | changed with CAMB v2 |
| Recombination, dark energy | `Recfast`; `DarkEnergyFluid` | class names of the default objects |
| `YHe` | `None` in `set_cosmology`: set from BBN consistency | a bare `CAMBparams()` holds 0.24 until `set_cosmology` is called |
| `TCMB` | 2.7255 K | — |


- **pyccl pins CAMB to its version-1 behaviour.** The pyccl 3.3.6 docstring lists the CAMB extra parameter `AccuracyTarget` as "currently set to 0 to match CAMB v1 behavior" [doc: installed pyccl 3.3.6, `pyccl.Cosmology` docstring, 2026-10-26]. A pyccl prediction and a direct CAMB v2 call therefore do not use the same accuracy defaults.
- **CAMB v1 against v2 at high ℓ.** With its historical lensing cutoff, CAMB v1.6.6 is in error by 1.5 % in TT at ℓ = 3000 (arXiv:2607.14854) [src: Sect. IX]. A Stage-IV CMB forecast or likelihood run with CAMB v1 defaults and ℓ_max above about 1500–2000 needs explicit accuracy settings.
- **CLASS lensed spectra need a margin in ℓ.** Stopping at the requested ℓ_max = 4000 instead of computing to 6000 changes the spectra by 1.8 × 10⁻² at ℓ = 4000 (arXiv:2607.14854) [src: Sect. XI].
- **Hidden CAMB precision parameters (2011).** With all CAMB accuracy boosts at 3, unlensed TT still differed from CLASS by about 0.7 % at low ℓ and 0.1 % at high ℓ. Two hard-coded quantities were responsible: the Bessel-function sampling step (Δx = 1 for x > 25; 0.2 moved C_ℓ by about 0.1 %) and the thermodynamics sampling `nthermo` (default 10 000; 80 000–100 000 gave stable results, taking agreement from 0.1 % to 0.01 %) (Lesgourgues 2011, arXiv:1104.2934) [src: Sect. 2.1].
- **Late-radiation truncation and reionisation in P(k) (2011).** CAMB's `do_late_rad_truncation` had to be switched off for P(k) to converge at 10⁻⁵; a remaining sharp rise of the CAMB/CLASS ratio above 1 h Mpc⁻¹ came from CAMB ignoring reionisation in the baryon sound speed, and with reionisation off the codes agreed at 0.01 % up to k = 50 h Mpc⁻¹ (arXiv:1104.2934) [src: Sect. 2.3]. CLASS precision files `cl_permille.pre`, `cl_2permille.pre`, `cl_3permille.pre` target 0.1, 0.2 and 0.3 % on C_ℓ to ℓ = 3000 [src: Sect. 3].
- **CAMB v2 accuracy hierarchy.** `AccuracyBoost` multiplies most lower-level controls; `lSampleBoost` and `lAccuracyBoost` are "largely orthogonal" to it; `lens_potential_accuracy` stands outside the hierarchy. The paper states that production analyses "should rarely need AccuracyBoost > 1" and that `Transfer.high_precision` "should always be enabled when accurate matter power spectra are needed" (arXiv:2607.14854) [src: App. C].
- **Modified-gravity solvers need raised precision.** The 2017 comparison had to raise default precision for some models to reach sub-per-cent agreement and warns that a user with default precision "might not get exactly the same agreement"; the settings used (CAMB-based: `k_eta_max_scalar = 80000`, `l_max_scalar = 10000`, `do_late_rad_truncation = F`; CLASS-based: `l_max_scalars = 5000`, `P_k_max_h/Mpc = 12`, `k_per_decade_for_pk = 200`) are listed (Bellini et al. 2017, arXiv:1709.09135) [src: Sect. V; App. C].
- **CLASS `explanatory.ini` is not the list of defaults.** The file of v3.2.3 sets `output = tCl,pCl,lCl,mPk`, `lensing = yes`, `P_k_max_h/Mpc = 1.`, `l_max_scalars = 2500`, `recombination = HyRec`, `YHe = BBN`, `gauge = synchronous`, `non_linear` empty, `use_ppf = yes` [doc: https://raw.githubusercontent.com/lesgourg/class_public/v3.2.3/explanatory.ini, 2026-10-26]. It documents options with example values (it requests four outputs and lensing), so its contents should not be quoted as "the CLASS defaults" without checking the code. The CLASS overview paper states that default values of input parameters are "defined in the input module" (arXiv:1104.2932) [src: Sect. 2.2].
- **cosmoprimo calculation defaults.** `non_linear=''`, `lensing=False`, `kmax_pk=10.0`, `ellmax_cl=2500`, `YHe='BBN'`, `use_ppf=True`; cosmological defaults `h=0.7`, `Omega_cdm=0.25`, `Omega_b=0.05`, `sigma8=0.8`, `n_s=0.96`, `T_cmb=2.7255`, `tau_reio=0.06` [doc: installed cosmoprimo 1.0.0, `Cosmology()` and cosmoprimo/cosmology.py, 2026-10-26]. `Cosmology()` without arguments is not the DESI fiducial; that is `fiducial.DESI()`.
- **pyccl defaults.** `transfer_function='boltzmann_camb'`, `matter_power_spectrum='halofit'`, `T_CMB=2.7255`, `Omega_k=0`, `w0=-1`, `wa=0`; `CosmologyVanillaLCDM` is Ω_c = 0.25, Ω_b = 0.05, σ8 = 0.81, n_s = 0.96, h = 0.67 with no massive neutrinos [doc: installed pyccl 3.3.6, `pyccl.Cosmology` signature and `CosmologyVanillaLCDM()`, 2026-10-26].
- **Recombination differs by default.** CAMB uses its `Recfast` class and the CLASS example file HyRec (section 1.2 of `physics-and-methods.md`). The CAMB–CLASS comparison of arXiv:2607.14854 had to impose the same RECFAST settings and a fixed Y_He = 0.245 on both codes to be like for like.
- **Reionisation and the high-k linear spectrum.** The nominally linear P(k) at k above about 1 Mpc⁻¹ depends on a convention for post-reionisation baryon heating; CAMB's default omits the heating, and the optional `include_heating` changes the z = 0 linear power by about 1 % at k ∼ 1 Mpc⁻¹ (arXiv:2607.14854) [src: App. B]. Lyα and small-scale analyses that feed a linear spectrum to an emulator should record the convention.
- **Dark energy across w = −1.** A w0wa model crossing the phantom divide needs the PPF prescription (arXiv:0808.3125). The default CAMB object is a fluid model; the CLASS example file sets `use_ppf = yes` and cosmoprimo defaults to `use_ppf=True`. State the model used. CAMB v2 states that its fluid description "is singular where w crosses −1" and uses PPF for general w(a); it caps the PPF relaxation rate above β⋆ = 30, which reproduces the unregularised equation to ≲ 10⁻⁵ in lensed C_ℓ, matter power and lensing potential (arXiv:2607.14854) [src: Sect. VII].

## 4. Sampler defaults
<!-- key: sampler-defaults -->

| Sampler | Default | Value | Source |
|---|---|---|---|
| Cobaya `mcmc` | `Rminus1_stop` (Gelman–Rubin R − 1 on means) | 0.01 | [doc: CobayaSampler/cobaya/cobaya/samplers/mcmc/mcmc.yaml on `master`, 2026-10-26] |
| Cobaya `mcmc` | `Rminus1_cl_stop` at `Rminus1_cl_level` | 0.2 at 0.95 | [doc: CobayaSampler/cobaya/cobaya/samplers/mcmc/mcmc.yaml on `master`, 2026-10-26] |
| Cobaya `mcmc` | `burn_in`, `proposal_scale`, `learn_proposal` | 0, 2.4, True | [doc: CobayaSampler/cobaya/cobaya/samplers/mcmc/mcmc.yaml on `master`, 2026-10-26] |
| Cobaya `mcmc` | `oversample_power`, `drag` | 0.4, False | [doc: CobayaSampler/cobaya/cobaya/samplers/mcmc/mcmc.yaml on `master`, 2026-10-26] |
| Cobaya `polychord` | `nlive`, `num_repeats`, `precision_criterion` | 25d, 2d, 0.001 (d is the dimension) | [doc: CobayaSampler/cobaya/cobaya/samplers/polychord/polychord.yaml on `master`, 2026-10-26] |
| emcee `EnsembleSampler` | move | `StretchMove(a=2.0)` | [doc: installed emcee 3.1.6, 2026-10-26] |
| emcee `autocorr.integrated_time` | `tol`, `c` | 50, 5 | [doc: installed emcee 3.1.6, `emcee.autocorr.integrated_time` signature, 2026-10-26] |
| dynesty `NestedSampler` | `nlive`, `bound`, `sample` | 500, `'multi'`, `'auto'` (`'unif'` below 10 dimensions, `'rwalk'` from 10 to 20) | [doc: joshspeagle/dynesty/py/dynesty/dynesty.py on `master`, 2026-10-26] |
| dynesty static `run_nested` | `dlogz` | 0.01, or `1e-3 * (nlive - 1) + 0.01` when `add_live=True` (the default) | [doc: joshspeagle/dynesty/py/dynesty/sampler.py on `master`, 2026-10-26] |
| dynesty dynamic `run_nested` | `n_effective`, `pfrac` | `target_n_effective = max(10000, ndim^2)` in the default stopping function; `pfrac = 0.8` in the default weight function (the stopping function's own default is 1.0) | [doc: joshspeagle/dynesty/py/dynesty/dynamicsampler.py on `master`, 2026-10-26] |
| nautilus `Sampler` | `n_live`, `n_networks` | 2000, 4 | [doc: johannesulf/nautilus/nautilus/sampler.py on `main`, 2026-10-26] |
| nautilus `Sampler.run` | `f_live`, `n_eff`, `discard_exploration` | 0.01, 10000, False | [doc: johannesulf/nautilus/nautilus/sampler.py on `main`, 2026-10-26] |
| NumPyro `NUTS` | `target_accept_prob` | 0.8 | [doc: pyro-ppl/numpyro/numpyro/infer/hmc.py on `master`, 2026-10-26] |
| MontePython 3 | jumping factor; `--update` | 2.4; on by default, starting at max(R − 1) < 3 and stopping at < 0.4 | arXiv:1804.07261 [src: Sect. 2.3, 2.4] |
| BlackJAX `nuts` | `max_num_doublings` | 10 | [doc: blackjax-devs/blackjax/blackjax/mcmc/nuts.py on `main`, 2026-10-26] |

Traps:

- **Cobaya's PolyChord defaults are for exploration.** The documentation comment recommends `num_repeats: 5d` "if accurate evidences needed or weird posterior shapes" against the default 2d [doc: CobayaSampler/cobaya/cobaya/samplers/polychord/polychord.yaml on `master`, 2026-10-26].
- **emcee convergence is the user's job.** The autocorrelation estimator raises an `AutocorrError` unless the chain is longer than `tol = 50` autocorrelation times (`quiet=True` turns the error into a warning) [doc: installed emcee 3.1.6, `emcee.autocorr.integrated_time`, 2026-10-26].
- **nautilus exploration points.** With the default `discard_exploration=False` the points of the exploration phase are kept; discarding them is described as "required for a fully unbiased posterior and evidence estimate" [doc: johannesulf/nautilus/nautilus/sampler.py on `main`, `Sampler.run` docstring, 2026-10-26]. The paper recommends discarding them "if using the results for scientific publications", since keeping them "may result in percent-level biases on the posterior and evidence estimates" (arXiv:2306.16923) [src: Sect. 5.4].
- **PolyChord `n_repeats`.** Too low a value correlates live points and makes evidences unreliable while posteriors stay accurate; the paper suggests ∼ 3 × n_dims (arXiv:1506.00171) [src: Sect. 5.7]. Cobaya's default 2d is below that suggestion.
- **dynesty `'auto'` changes algorithm with dimension.** A model that gains a few nuisance parameters and crosses 10 or 20 dimensions silently switches sampling method [doc: joshspeagle/dynesty/py/dynesty/dynesty.py on `master`, 2026-10-26].
- **NUTS step size.** The NUTS paper tunes ε by dual averaging towards a target Metropolis acceptance δ, citing ≈ 0.65 as optimal "under fairly strong assumptions", and runs its tests at δ = 0.65; ε̄ converges "within a few hundred iterations" except for a stochastic-volatility model (Hoffman & Gelman, arXiv:1111.4246) [src: Sect. "Setting ε in HMC", 4.2]. NumPyro's 0.8 target is therefore a library choice above the paper's value.
- **Gradient samplers need non-default settings on hard posteriors.** The NumPyro NUTS default is `target_accept_prob=0.8` [doc: https://num.pyro.ai/en/stable/mcmc.html, 2026-10-26], and the NumPyro hierarchical-regression tutorial runs NUTS with `target_accept_prob=0.97` [doc: https://num.pyro.ai/en/stable/tutorials/bayesian_hierarchical_linear_regression.html, 2026-10-26]; divergences are reported in `get_extra_fields()["diverging"]`.
- **MultiNest.** On the DES Y1 likelihood it gave "somewhat narrower parameter credible intervals" than PolyChord and inconsistent evidences (arXiv:2202.08233). Results obtained with MultiNest at default-like settings deserve this caveat.

Convergence practice and what R − 1 = 0.01 (the Cobaya default above) does and does not guarantee are in the sibling `cosmo-statistics-inference` [doc: CobayaSampler/cobaya/cobaya/samplers/mcmc/mcmc.yaml on `master`, 2026-10-26].

## 5. Estimator conventions
<!-- key: estimator-conventions -->

### 5.1 pypower (`CatalogFFTPower`, version 1.0.0 checkout)
<!-- key: pypower-catalogfftpower-version-1-0-0-checkout -->

| Argument | Default | Note |
|---|---|---|
| `ells` | `(0, 2, 4)` | — |
| `los` | `'firstpoint'` | local line of sight; `'endpoint'`, an axis or a vector are the alternatives |
| `resampler` | `'tsc'` | choices `ngp`, `cic`, `tsc`, `pcs` |
| `interlacing` | 2 | — |
| `position_type` | `'xyz'`, arrays of shape (3, N) | the README example uses `'pos'`, shape (N, 3) |
| `boxpad` | 2.0 | box is twice the extent of the positions when `boxsize` is not given [doc: cosmodesi/pypower/pypower/fft_power.py on `main`, 2026-10-26] |
| `edges` | k up to `np.pi/(boxsize/nmesh)` when given as a dictionary without `'max'` | the Nyquist wavenumber |
| `direct_selection_attrs` | `{'theta': (0., 2 / 60.)}` | pairs below 2 arcminutes for the direct pair-count term |
| `shotnoise` | internal estimate; "0 in case of cross-correlation" | subtracted by default in `get_power(remove_shotnoise=True)` |

All rows: `CatalogFFTPower` on `main`, read on 2026-10-26 (in the signature `los=None`, documented as "default='firstpoint'") [doc: cosmodesi/pypower/pypower/fft_power.py on `main`, 2026-10-26].

### 5.2 Others
<!-- key: others -->

- **pycorr.** The pair counter is Corrfunc, by default the `desi` branch of the cosmodesi fork, which is a different source from the Corrfunc release on PyPI (2.5.3) [doc: cosmodesi/pycorr/README.md on `main`; https://pypi.org/pypi/corrfunc/json, 2026-10-26].
- **TreeCorr.** Defaults: metric `'Euclidean'`, `bin_type='Log'`, `var_method='shot'`, `flip_g1` and `flip_g2` False [doc: https://rmjarvis.github.io/TreeCorr/_build/html/correlation2.html; https://rmjarvis.github.io/TreeCorr/_build/html/catalog.html, 2026-10-26]. The default `bin_slop` is an approximation, not exact pair counting (see `results.md`, section 5). Shear sign conventions differ between catalogues; `flip_g2` is the switch.
- **NaMaster.** `NmtField(mask, maps, *, spin=None, templates=None, beam=None, purify_e=False, purify_b=False, ..., masked_on_input=False, ...)`; `masked_on_input=True` is "not advisable if you're using purification"; "NaMaster uses the same polarization convention as HEALPix", and ellipticities in the IAU convention need the sign of the e2 map swapped [doc: https://namaster.readthedocs.io/en/latest/api/pymaster.field.html, 2026-10-26].
- **picca.** The picca README sends users who want to compute models for its correlations, or to fit them, to Vega, and keeps `fitter2` for some tasks [doc: https://raw.githubusercontent.com/igmhub/picca/main/README.md, 2026-10-26]; a reference to "the picca fitter" describes the pre-Vega `fitter2`.
- **velocileptors.** The LPT module takes an infrared scale `kIR`; the parameter vector changes with the module and with `beyond_gauss` (reduced set `[b1, b2, bs, b3] + [alpha0, alpha2, alpha4] + [sn, sn2]`) [doc: https://raw.githubusercontent.com/sfschen/velocileptors/master/README.md, 2026-10-26]. Counterterm definitions differ between its LPT and EPT modules (section 4 of `physics-and-methods.md`).
- **Fourier convention.** None of the docstrings read this session states the Fourier convention; the pyccl `sigmaR` formula, σ_R² = (1/2π²) ∫ dk k² P(k) |W(kR)|², fixes the P(k) normalisation pyccl uses [doc: installed pyccl 3.3.6, `pyccl.sigmaR` docstring, 2026-10-26]. See `cosmo-theory-foundations` for the conventions.

## 6. Sphere and lensing conventions
<!-- key: sphere-and-lensing-conventions -->

All from healpy 1.19.0 installed docstrings [doc: installed healpy 1.19.0, 2026-10-26].

| Function | Default | Trap |
|---|---|---|
| `read_map` | `nest=False`, `field=0` | returns RING ordering and only the first field (temperature) unless asked |
| `anafast`, `map2alm` | `lmax = 3*nside - 1`, `iter=3`, `pol=True`, `use_weights=False`, `use_pixel_weights=False` | "the input maps must be in ring-ordering"; "No removal of monopole or dipole is performed"; masked pixels are set to 0 |
| `anafast` output order | TT, EE, BB, TE, EB, TB | — |
| `synfast` input order | `new=False`: TT, TE, TB, EE, EB, BB (or TT, TE, EE, BB for four spectra) | opposite to the `anafast` output order; `new=True` is needed to feed `anafast` output back; the docstring adds "We don't plan to change the default order anymore" |
| `synfast`, `smoothing` | `fwhm` in radians, `pixwin=False` | an arcminute value passed as `fwhm` is read as radians, a beam wrong by the arcminute-to-radian factor [der] |
| `ang2pix` | `theta` colatitude and `phi` in radians, `nest=False`, `lonlat=False` | `lonlat=True` switches to longitude and latitude in degrees |
| `ud_grade` | `power=None`, mean of children pixels | "can create artifacts in the power spectra and should be avoided unless the specific application can tolerate that" |
| `UNSEEN` | −1.6375e+30 | a masked map averaged or degraded without care carries this value [doc: installed healpy 1.19.0, `healpy.UNSEEN`, 2026-10-26] |

- The `anafast` docstring recommends removing the monopole before running it "to reduce boundary effects" [src].
- HEALPix NSIDE-partitioned catalogues often use NESTED ordering, whereas healpy functions default to RING: pass `nest=True` consistently.
- pyccl correlation functions warn that "for scales smaller than ∼ 0.1°, the input power spectrum should be sampled to sufficiently high ℓ to ensure the Hankel transform is well-behaved" [doc: installed pyccl 3.3.6, pyccl/correlations.py, 2026-10-26].

## 7. Documented cases where a default changed a published result
<!-- key: documented-cases-where-a-default-changed-a -->

1. **MultiNest in DES Y1.** Credible intervals were "somewhat narrower" and evidences inconsistent compared with PolyChord; DES Y3 changed its baseline sampler and published recommended settings for test and final chains (Lemos et al. 2022, arXiv:2202.08233). The body quantifies it: "fairly standard" MultiNest settings gave Ω_m and σ8 widths "systematically underestimated by about 10%", and the speed advantage of MultiNest "is not present when sufficiently accurate sampling hyperparameters are used"; the paper recommends MultiNest "only be used for preliminary testing and pipeline debugging" [src: Sect. 5; Table 1].
2. **CAMB v1 lensing cutoff.** The Planck-era default max(kη₀) = 10375 leaves 1.5 % errors in TT by ℓ = 3000 and Δχ² ≃ 6 × 10³ on an SO-like proxy (arXiv:2607.14854) [src: Sect. IX]. A high-ℓ analysis run with untouched v1 defaults would carry this error; the paper notes that earlier work "established the boosted settings both codes need" for Stage-IV applications, so the check is whether a given analysis applied them.
3. **EFT full-shape pipelines on BOSS.** Different analyses obtained σ8 "in mild tension with one another", which the DESI comparison attributes to "the settings of pipelines used and modeling choices" (priors and bias parameterisations), not to the theories (arXiv:2404.07272, conclusion).
4. **Infrared resummation in an Eulerian code.** The `neckar` authors report that a previous implementation carried errors of order 1 % in the quadrupole and 10 % in the hexadecapole at k ≳ 0.1 h Mpc⁻¹ (arXiv:2610.03466) [src: abstract]. This
 is the authors' claim in a 2026 preprint; no independent confirmation was read.
5. **Homogeneous reionisation heating.** Halo-model fitting functions fed with a heated linear spectrum return "a percent-level increase of power on quasi-linear scales (k ∼ 0.3–1 Mpc⁻¹)", an artefact, where heating should remove power (arXiv:2607.14854) [src: App. B].
6. **Lyα P1D amplitude and a prior.** With the lym1d emulator, eBOSS DR14 data give A_Lyα < 7.6 (95 %) against a Planck value of 8.79, a tension that "disappears when imposing a well-motivated external prior" on the mean transmission (A_Lyα = 9.8 ± 1.1) (arXiv:2412.05372). The abstract attributes the low value to the correlation of this parameter with the mean transmission: a prior choice on a nuisance parameter moved a cosmological parameter.

Not software defaults but the same family of error:

- **Package names.** On PyPI, `pycorr`, `pyrecon` and `lace` are unrelated projects (a categorical-correlation tool, a file-format library and a mesh library) [doc: https://pypi.org/pypi/pycorr/json; https://pypi.org/pypi/pyrecon/json; https://pypi.org/pypi/lace/json, 2026-10-26]. The cosmodesi codes and LaCE install from GitHub.
- **Module shadowing.** The EFTCAMB Python wrapper is imported with `import camb` [doc: https://raw.githubusercontent.com/EFTCAMB/EFTCAMB/HEAD/README.md, 2026-10-26]: in one environment it replaces CAMB, and results labelled "CAMB" may come from the patched code.
- **Stale index records.** `pypolychord` on PyPI is version 1.15.1 from 2019, while the repository released 1.22.2 on 2025-11-25 [doc: https://pypi.org/pypi/pypolychord/json; https://api.github.com/repos/PolyChord/PolyChordLite/releases/latest, 2026-10-26].

## 8. What a referee checks
<!-- key: what-a-referee-checks -->

1. Code name, version and, for Boltzmann codes, the non-default precision settings; "CAMB" without a version is ambiguous across the v1 to v2 change.
2. Units of every k and P(k) quoted, and whether h is in them; the value of h used for a conversion.
3. Neutrino model: total mass, number of massive eigenstates, N_eff value (3.044 or 3.046) [doc: installed camb 2.0.4 (`nnu=3.044`), astropy 8.0.1 (`Planck18.Neff` = 3.046), 2026-10-26].
4. Which field σ8, fσ8 and the galaxy-clustering model refer to (total matter or CDM plus baryons) and which fσ8 definition.
5. Non-linear prescription by name and version (`takahashi`, `mead2016`, `mead2020`, with or without feedback), not "halofit".
6. Dark-energy perturbation model for any w0wa run (fluid or PPF).
7. Recombination code when two Boltzmann codes are compared or combined.
8. Sampler, its settings (live points, `num_repeats`, stopping criterion), the convergence criterion reached, and whether evidences come from a sampler known to be unreliable for them.
9. For EFT full-shape fits: code, bias basis and priors, counterterm convention, k_max, infrared-resummation scheme.
10. For estimators: line-of-sight definition, mesh size and Nyquist wavenumber, interlacing, shot-noise treatment, pair-count tolerance (`bin_slop`), weights.
11. For maps: HEALPix ordering, N_side, ℓ_max, treatment of the monopole, pixel window, polarisation convention.
12. For emulators: training code and its precision settings, parameter ranges, and a statement that the analysis stays inside them.

## 9. Code comparisons read in paper bodies
<!-- key: code-comparisons-read-in-paper-bodies -->

What was compared, on which quantity and range, with which settings, and how large the disagreement was. Each figure holds for the configuration of its paper only.

| Comparison | Quantity and range | Settings | Disagreement | Citation |
|---|---|---|---|---|
| CAMB against CLASS (2011) | unlensed and lensed TT, EE, 2 ≤ ℓ ≤ 3000; C_ℓ^φφ, 3 ≤ ℓ ≤ 4000 | ΛCDM with h = 0.7, N_eff = 3.04, Y_He = 0.25, n_s = 1; CLASS `cl_ref.pre`; CAMB boosts at 3, `k_eta_max_scalar = 12000`, `nthermo` = 100 000; same reionisation function | lensed TT 0.01 % (except ℓ = 18), EE 0.02 % for ℓ ≥ 40; C_ℓ^φφ 0.025 % (0.07 % at ℓ = 2) | arXiv:1104.2934 [src: Sect. 2, 2.2] |
| Same, linear P(k) | 10⁻⁴ < k < 50 h Mpc⁻¹ | CLASS `pk_ref.pre` (l_ν,max = 150); CAMB `accuracy_boost = 5`, `l_accuracy_boost = 8`, no late-radiation truncation | 0.01 % to 1 h Mpc⁻¹; above, a sharp rise from CAMB's baryon sound speed; 0.01 % to 50 h Mpc⁻¹ with reionisation off | arXiv:1104.2934 [src: Sect. 2.3] |
| Same, on a likelihood | simplified three-channel Planck likelihood, f_sky = 0.8, ℓ ≤ 3000 | reference spectra of each code | Δχ² = 0.027 between the reference spectra; at equal Δχ², CLASS about 2.5 times faster on one CPU | arXiv:1104.2934 [src: Sect. 4] |
| CAMB v2 defaults against a boosted CAMB reference | lensed TT, EE, normalised TE; C_L^φφ; BB; linear and non-linear P(k) | `check_accuracy` with doubled boosts | validated maximum fractional tolerances: 10⁻³ for lensed TT/EE at 600 ≤ ℓ < 3500 and for P(k) at 5 × 10⁻³ < k < 2 h Mpc⁻¹; 3 × 10⁻³ at 2 ≤ ℓ < 600 and 3500 ≤ ℓ < 6000; 5 × 10⁻³ for C_L^φφ at 5 ≤ L < 2500; 10⁻² for non-linear P(k) above 10 h Mpc⁻¹ | arXiv:2607.14854 [src: App. C, Table 2] |
| Same tolerances on an SO-like likelihood | 2 ≤ ℓ ≤ 4000, f_sky = 0.6, 1.4 arcmin beam | errors uniform up to the Table 2 maxima; or all at the maximum | Δχ² ≃ 9.6 (pessimistic envelope); ≃ 34 if coherent | arXiv:2607.14854 [src: App. C] |
| CAMB v2 against CLASS (2026) | lensed CMB to ℓ_max = 4000 | same HMcode-2020 without feedback, same lensing source cutoff, Y_He = 0.245, Planck-era RECFAST settings | like-for-like numerical test; figures in `results.md`, section 1.2 | arXiv:2607.14854 [src: Sect. IX] |
| CCL against independent codes (2018) | χ(z) and D(z), 0.01 ≤ z ≤ 1000; linear CLASS + halofit P(k), 10⁻³ ≤ k ≤ 20 Mpc⁻¹, z = 0, 2; Cosmic Emulator P(k), k ≤ 5 Mpc⁻¹; C_ℓ, 2 ≤ ℓ ≤ 3000; ξ±, ξ_gg, ξ_ggl, 0.01° < θ < 5°; 3D ξ, 0.1 < r < 250 Mpc | benchmarks from CosmoMAD, classy, CosmoLSS and others; BBKS input for the two-point tests | χ 5 × 10⁻⁷; D 6 × 10⁻⁶; CLASS P(k) ∼ 10⁻³; emulator 10⁻² (wCDM), 3 × 10⁻² (νCDM); C_ℓ 0.1 σ_ℓ; angular ξ 0.5 σ_LSST; 3D ξ 4 × 10⁻²; non-Limber clustering 2 × 10⁻² | arXiv:1812.05995 [src: Table 2] |
| Limber against non-Limber C_ℓ (N5K) | LSST Y10 3x2pt, ℓ ≤ 200 | benchmarks computed to high precision | Limber discrepancy "at the level of a few ten per-cent" at low ℓ, dominated by clustering auto-spectra and adjacent-bin cross-spectra (the figure plots differences as fractions of the Gaussian error); for shear, "a few %" of the uncertainties at most; challenge target Δχ² ≈ 0.2, loosened up to 1.7 in a test | arXiv:2212.04291 [src: Sect. 3.3, 5.1, 5.2.1] |
| MultiNest against PolyChord and Metropolis–Hastings | DES Y1 3x2pt, wCDM, 128 cores; log Z and marginal widths | MultiNest `n_live` 250–675, efficiency 1 to 0.001, tolerance 0.3 to 0.01, constant efficiency on or off; PolyChord `n_live` 50–675, `n_repeats` 15–120 | MultiNest log Z drifts with efficiency: −277.68 ± 0.17 at efficiency 1, −282.01 ± 0.18 at 0.001 (n_live 675, tol 0.1), −275.41 ± 0.16 with constant efficiency; PolyChord gives −281.5 to −282.9 across settings; "fairly standard" MultiNest settings underestimate the Ω_m and σ8 widths by about 10 % | arXiv:2202.08233 [src: Table 1, Table 2, Sect. 5] |
| velocileptors (LPT, EPT), PyBird, FOLPSν on the same mocks | P_ℓ(k) of AbacusSummit LRG, ELG, QSO cubic boxes (mean of 25), 0.02 ≤ k ≤ 0.18 h Mpc⁻¹; ShapeFit and Full-Modelling | covariance of one 8 (h⁻¹ Gpc)³ box; "minimal freedom" (tidal and third-order bias at coevolution) and "maximal freedom" bias | all within about 1 σ of the truth at 200 (h⁻¹ Gpc)³, with "noticeable disagreements" there; at 8 (h⁻¹ Gpc)³ very good agreement, better in minimal freedom; in maximal freedom PyBird explores large negative m with b₃ ∼ −100 until a Gaussian prior of width 10 on b₃ is added, and velocileptors LPT has a wider m posterior until N(0, 5) priors on b_s and b₃ | arXiv:2404.07272 [src: Sect. 5.2] |
| Same codes on each other's noiseless predictions | LRG-like data generated by one code, fitted by the two others, as a function of k_max | single-box covariance, minimal freedom | agreement up to k_max ∼ 0.24 h Mpc⁻¹; FOLPSν shifts by ≳ 1 σ in log A_s at k_max ∼ 0.26 h Mpc⁻¹ (Full-Modelling); LPT and FOLPSν differ by ≳ 1 σ in α∥ only from k_max ∼ 0.28 h Mpc⁻¹ (ShapeFit) | arXiv:2404.07272 [src: Sect. 5.3] |
| Corrfunc against TreeCorr and other pair counters | pair counts in the same bins | TreeCorr 3.3.6 with `bin_slop` disabled | counts "exactly agreed"; Corrfunc 1.9–5.7 times faster single-threaded, 1.1–7.3 times multi-threaded; with the default `bin_slop` TreeCorr counts are approximate (section 5.2) | arXiv:1911.03545 [src: Sect. 6.5] |
| NaMaster against input spectra | six spectra between δ, γ_E, γ_B on the curved sky, N_side = 1024; 1000 contaminated realisations, non-binary mask | all contaminants deprojected | residuals consistent with Gaussian scatter for N_dof = 681; PTE ≳ 0.1, "no statistically significant bias" | arXiv:1809.09603 [src: Sect. 4.2] |
| CLASS against high-accuracy CAMB, for emulator training (2023) | TT, TE, EE, linear and non-linear P(k), ℓ < 3000 and k < 10 Mpc⁻¹; ℓ_max = 11000 | camb v1.3.6 with boosts at 2 and `lens_potential_accuracy=8`; CLASS v2.9.4 with `cl_ref.pre` plus `k_max_tau0_over_l_max: 15` | better than 0.1 % with `cl_ref.pre` (about one hour per model); the same match is obtained with three changed CLASS parameters at about one minute; without `accurate_lensing` the lensed spectra above ℓ = 3000 show "non-physical oscillatory features" | arXiv:2303.01591 [src: Sect. 3] |
| CosmoPower against its training code | linear P(k) and non-linear correction, 10⁻⁵ ≤ k ≤ 10 Mpc⁻¹, 0 ≤ z ≤ 5 | ∼ 2 × 10⁴ test spectra | 99 % within 0.1 % (linear) and 0.4 % (non-linear correction); larger errors above k ≳ 1 Mpc⁻¹ | arXiv:2106.03846 [src: Sect. 3.2] |
| Two independent EFTofLSS implementations, blinded ("East Coast" and "West Coast" teams) | (Ω_m, H₀, A_s) and b₁ against the hidden truth, as a function of k_max = 0.08–0.2 h Mpc⁻¹ | BOSS-like mocks; East Coast used monopole and quadrupole only (hexadecapole dominated by leakage on the grid) and no priors on nuisance parameters; West Coast bounded nuisance parameters | truth within or slightly off 1 σ up to k_max = 0.14 h Mpc⁻¹; A_s deviates systematically above it (two-loop terms); H₀ and Ω_m within about 1 σ to 0.2 h Mpc⁻¹; error bars differ by up to a factor ∼ 2 below k_max ≈ 0.1 h Mpc⁻¹, driven by the prior treatment, and agree at higher k_max | arXiv:2003.08277 [src: Sect. IV.2.1, V.3] |
| flip against pairV (through its Python port pypairV) | velocity covariance C_vv of a mock low-z SN Ia sample (z ≈ 0.025 ± 0.025, angular separations 0–180°) | same cosmology, linear spectra, flip model C23; each code with its own P(k) (CLASS in flip, Eisenstein–Hu in pairV) | "excellent" on average; per-cent-level gradients in the ratio from the per-cent P(k) difference, and numerical instabilities traced to pairV's decomposition of the integral | arXiv:2501.16852 [src: Sect. 4.1] |
| Modified-gravity Einstein–Boltzmann solvers (EFTCAMB, hi_class, COOP and six model-specific codes) | CMB spectra to ℓ = 3000; P(k) to k = 10 h Mpc⁻¹ | target 0.1 % (0.5 % for ℓ < 100); precision raised above default for MCMC-usable speed | never worse than 1 % for the models considered; EE at ℓ ≲ 300 exceeds 1 %, judged harmless because noise-dominated; COOP accurate only for k ≲ 1 h Mpc⁻¹ before calibration | arXiv:1709.09135 [src: Sect. IV, V] |

## Not verified
<!-- key: not-verified -->

- How each flip power-spectrum engine converts units was not read in the source.
- Whether CAMB's `get_matter_power_spectrum` output P is in (Mpc/h)³ was inferred from the parameter names, not read in a docstring.
- The k unit of cosmoprimo power spectra was not read in a docstring; the README read on 2026-10-14 does not state it.
- The sizes in section 9 are those of each paper's configuration and code versions (CAMB 2011; camb v1.3.6 and CLASS v2.9.4 in arXiv:2303.01591 [src: Sect. 3, Sect. 2]; TreeCorr 3.3.6 in arXiv:1911.03545 [src: Sect. 6.5]; CCL of 2018); none was re-measured for current versions.
- arXiv:2607.14854 was read in an HTML rendering of an earlier version (titled "CAMB 2"); its section and appendix numbers may differ in the current version.
- Default values of NumPyro `NUTS` other than the target acceptance, and of BlackJAX `window_adaptation`, were not read in an API reference.
- MontePython stopping criterion and CosmoSIS sampler defaults were not read (the MontePython 3 paper gives only the update thresholds and jumping factor).
- CLASS compiled defaults (as opposed to `explanatory.ini`) were not read; nor was any CLASS version later than 3.2.3, although PyPI now has classy 3.4.1.0 [doc: lesgourg/class_public/explanatory.ini at tag v3.2.3; https://pypi.org/pypi/classy/json, 2026-10-26].
- Defaults of desilike, pycorr (estimator choice), Corrfunc, Triumvirate, nbodykit, Vega and LaCE were not read.
