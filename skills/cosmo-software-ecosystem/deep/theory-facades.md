# Theory facades — cosmo-software-ecosystem dossier

Scope: what a facade (pyccl, cosmoprimo, jax-cosmo, cloelib/CLOE) passes
to its engine, how its splines, extrapolations, tolerances and halo-model
calculator are set and raised, how a facade is validated against a
benchmark, and how to choose between facades and their settings.
Snapshot: 2026-10-19.
From: cloelib (arXiv:2605.23839), State of the Field and Software Design;
LSST DESC (CCL) and Euclid (CLOE) code families.

Already in L2, not repeated here: the table of facades, engines and units
(`physics-and-methods.md#theory-facades`, `systematics.md#the-table`); the
CCL per-quantity accuracies and the N5K run times
(`results.md#theory-facades-validated-accuracy`); the CCL 2018 comparison
against independent codes (`systematics.md#code-comparisons-read-in-paper-bodies`);
the cosmoprimo and pyccl cosmological defaults
(`systematics.md#default-accuracy-and-non-linear-settings-of`). Limber
against non-Limber and the choice of a non-Limber method are in
`cosmo-theory-foundations/deep/projected-statistics-limber.md`.

"Installed" means read in the package source (pyccl 3.3.6, cosmoprimo
1.0.0, camb 2.0.4) on 2026-10-19; where the 2018 CCL paper differs, both
are given.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Know the order of operations of the facade
<!-- key: step-1-know-the-order-of-operations-of-the -->

CCL is used in three steps: a cosmology object that fixes the parameters
and the choice of power-spectrum method (enough for distances, H and
growth); a tracer object holding the bias, the redshift distribution and
the modelling options (magnification, for instance); then the angular
spectra for a list of multipoles [src: arXiv:1812.05995, Sect. V].
For speed, initialising a cosmology computes the linear and non-linear
P(k) once and stores them as splines that every later call interpolates
[src: same, Sect. III.2].
So every downstream quantity is bounded by the spline grid of Step 3,
not only by the engine; and the numerical parameters are read when the
cosmology is built. In pyccl 3.3.6 they are global objects
(`pyccl.spline_params`, `pyccl.gsl_params`), and `Cosmology._build_cosmo`
copies them into the object's `_spline_params`, `_gsl_params` and
`_accuracy_params` [src: pyccl 3.3.6 installed, `cosmology.py`]. Set them
before creating the cosmology [src: installed, `tracers.py` warning:
"before instantiating the Cosmology passed"].

### Step 2. Know what the facade asks the engine for
<!-- key: step-2-know-what-the-facade-asks-the-engine-for -->

A facade does not call its engine with the engine's own defaults. What
the installed wrappers set:

**pyccl → CAMB (`transfer_function='boltzmann_camb'`, the default)**
[src: pyccl 3.3.6 installed, `boltzmann.py`, `get_camb_pk_lin`]:

- `camb.config.AccuracyTarget = 0` unless overridden, with the comment
  that CAMB 2.x defaults to 1 and the legacy value keeps "behavior closer
  to CAMB 1.x".
- `set_for_lmax(lmax=5000, lens_potential_accuracy=0)`, commented "to
  match CAMB v1 behavior"; CMB and lensing outputs are switched off
  (`WantCls`, `DoLensing`, `Want_CMB` all False).
- `set_matter_power(kmax=10.0)` unless `extra_parameters['camb']['kmax']`
  is given; CAMB's `kmax` is in Mpc⁻¹ (`systematics.md#traps-that-follow`).
- Normalisation by σ8: CAMB is first run with A_s = 2.1 × 10⁻⁹, σ8 is
  computed by CCL from that linear spectrum, and A_s is rescaled by
  (σ8,target/σ8)². When A_s is given it is passed directly.
- Neutrinos: `share_delta_neff = False`, and the CAMB degeneracy factor is
  set to g = (T_ncdm/(11/4)^{−1/3})⁴ with T_ncdm = 0.71611, so that "both
  codes use the same neutrino temperature" as CLASS. Y_He comes from CAMB's
  BBN predictor with ΔN_eff = N_eff − 3.044.
- Dark energy: `dark_energy_model='fluid'` unless set to `'ppf'`; the code
  raises an error asking for PPF when w(a) crosses −1 with the fluid model.
- Non-linear: only when the CAMB non-linear spectrum is requested, with
  `halofit_version` defaulting to `'mead'` and the three HMcode baryon
  options passed through.

In CAMB 2.0.4, `'mead'` is the HMcode-2016 name (`mead2016` is documented
as its alias) while CAMB's own `halofit_default` is `mead2020`
[src: camb 2.0.4 installed, `nonlinear.py`]. A pyccl prediction with the
CAMB non-linear spectrum and default extra parameters is therefore
HMcode-2016, not the HMcode-2020 a direct CAMB call would give.

**pyccl → CLASS** sets `P_k_max_1/Mpc` to `K_MAX_SPLINE` and
`z_max_pk = 1/A_SPLINE_MINLOG_PK − 1`, then fills its own (a, k) grid with
`pk_lin`; a code comment states that the lowest CLASS k could not be read
from the Python interface and is set to 10⁻⁵ [src: installed,
`boltzmann.py`].

**cosmoprimo → CAMB** [src: cosmoprimo 1.0.0 installed, `camb.py`]:

- `set_matter_power(kmax=kmax_pk * h)`: `kmax_pk` (default 10) is in
  h Mpc⁻¹ and converted to CAMB's Mpc⁻¹.
- `set_for_lmax(lmax=ellmax_cl)` with no `lens_potential_accuracy`
  argument, hence CAMB v2's automatic value (`systematics.md#default-accuracy-and-non-linear-settings-of`).
- `non_linear='mead'` or `'hmcode'` → CAMB `'mead'` (HMcode-2016);
  `'halofit'` → `'original'`; any other string is passed as the CAMB
  version name, so `'mead2020'` must be written out.
- An extra parameter `accuracy` is passed to `set_accuracy`; any other
  unknown extra key is set as an attribute of `CAMBparams`.
- The neutrino-temperature block is the same construction as pyccl's.
- The PPF class is used when `use_ppf` is true (the default) and the
  dark-energy sound speed is 1; otherwise the fluid class.

### Step 3. Set the spline grids and know where the facade extrapolates
<!-- key: step-3-set-the-spline-grids-and-know-where-the -->

CCL stores P(k, a) as a bicubic spline in ln k and a, with a hybrid
a-grid: linear for a > 0.1 and logarithmic below, so that low redshift is
sampled finely for LSS while CMB lensing remains possible without a full
linear grid [src: arXiv:1812.05995, Sect. III.2]. Between `K_MAX_SPLINE`
and `K_MAX` the spectrum is a second-order Taylor expansion of ln P in
ln k about k₀ = `K_MAX_SPLINE` − 2Δ ln k, with Δ ln k = 10⁻² [src: Eq. 71];
below `K_MIN_SPLINE` it is a power law of index n_s [src: Eq. 72]. The
paper's `K_MIN_SPLINE` is not user-accessible; for CLASS it equalled the
smallest CLASS wavenumber, 7 × 10⁻⁶ Mpc⁻¹, so no low-k extrapolation
occurred; for Eisenstein–Hu only the high-k end was extrapolated; for the
Cosmic Emulator the spline range was fixed to 10⁻³–5 Mpc⁻¹, the emulator's
validity range [src: Sect. III.2].

Defaults in pyccl 3.3.6 [src: installed, `pyccl.spline_params`]:

| Parameter | Default | Meaning as read |
|---|---|---|
| `K_MIN`, `K_MAX` | 5 × 10⁻⁵, 1000 Mpc⁻¹ | integration limits in k |
| `K_MAX_SPLINE` | 50 Mpc⁻¹ | top of the spline; extrapolated above |
| `N_K` | 167 | samples per decade between `K_MIN` and `K_MAX` (`get_pk_spline_nk`) |
| `A_SPLINE_NA_PK`, `A_SPLINE_NLOG_PK` | 40, 11 | linear and logarithmic a-samples of P(k, a); total 40 + 11 − 1 |
| `A_SPLINE_MIN_PK`, `A_SPLINE_MINLOG_PK` | 0.1, 0.01 | a at the linear/log junction and at the bottom (z = 99) |
| `A_SPLINE_NA`, `A_SPLINE_NLOG`, `A_SPLINE_MINLOG` | 250, 250, 10⁻⁴ | background splines |
| `LOGM_SPLINE_MIN`, `_MAX`, `_NM` | 6, 17, 50 | σ(M) spline in log₁₀ M |
| `ELL_MIN_CORR`, `ELL_MAX_CORR`, `N_ELL_CORR` | 0.01, 60000, 5000 | ℓ grid of the correlation-function transforms (named in the `correlation` docstring) |

What the paper measured: with Δ ln k = 10⁻² and `K_MAX_SPLINE` = 50 Mpc⁻¹,
ln P converges to an accuracy that surpasses the expected baryonic effect
at k > 10 Mpc⁻¹; against a run with all spline parameters raised by an
order of magnitude (ten times the k and a sampling, interpolation ranges
one decade wider at each end), the fiducial interpolation is "negligible
for most applications", though some linear-spectrum applications "might
need to increase the value of K_MAX_SPLINE" [src: Sect. IV.2.2]. With
massive neutrinos (three test cosmologies), CCL-through-CLASS matched
CLASS to better than 10⁻⁴ between `K_MIN` and `K_MIN_SPLINE`, and to
better than 10⁻³ between `K_MAX_SPLINE` and `K_MAX` [src: Sect. IV.2.2].
These tests ran with CLASS, the 2018 default engine (CCL's default
"adopts the halofit implementation by interpolating CLASS power spectra
outputs") [src: Sect. IV.2.2]; the installed default is
`boltzmann_camb`.

### Step 4. Set the integration tolerances
<!-- key: step-4-set-the-integration-tolerances -->

CCL uses GSL for all integrations and interpolations; most
interpolations are Akima, P(k) is bicubic, and the code is in double
precision throughout [src: arXiv:1812.05995, Sect. III]. Defaults of
`pyccl.gsl_params` in 3.3.6 [src: installed]:

| Parameter | Default |
|---|---|
| `INTEGRATION_EPSREL`, `INTEGRATION_LIMBER_EPSREL` | 10⁻⁴ |
| `INTEGRATION_DISTANCE_EPSREL`, `ODE_GROWTH_EPSREL`, `EPS_SCALEFAC_GROWTH` | 10⁻⁶ |
| `INTEGRATION_SIGMAR_EPSREL`, `INTEGRATION_KNL_EPSREL` | 10⁻⁵ |
| `INTEGRATION_GAUSS_KRONROD_POINTS`, `INTEGRATION_LIMBER_GAUSS_KRONROD_POINTS` | 4 |
| `ROOT_EPSREL`, `N_ITERATION`, `ROOT_N_ITERATION` | 10⁻⁴, 1000, 1000 |
| `LENSING_KERNEL_SPLINE_INTEGRATION`, `NZ_NORM_SPLINE_INTEGRATION` | True, True |

For the halo mass function the paper notes that the tolerance of the σ²(M)
integral is "the relevant concern for numerical accuracy" [src:
Sect. IV.3]. The lensing kernel is integrated by spline by default;
pyccl warns, when the n(z) has fewer samples than the lensing-kernel χ
grid, to set `LENSING_KERNEL_SPLINE_INTEGRATION = False` before building
the cosmology [src: installed, `tracers.py`].

### Step 5. Angular spectra and real-space transforms
<!-- key: step-5-angular-spectra-and-real-space-transforms -->

- CCL does not evaluate C_ℓ at every integer ℓ: it samples logarithmically
  at low ℓ and linearly at high ℓ and interpolates with a cubic spline;
  the scheme is configurable [src: arXiv:1812.05995, Sect. III.3].
- The Limber integral (their Eq. 74) is a Gauss–Kronrod quadrature with
  limits adapted to the window functions, bounded by `K_MIN` and `K_MAX`
  [src: Sect. III.3.1]. The installed `angular_cl` defaults are
  `limber_integration_method='qag_quad'`, `l_limber=-1` (Limber
  everywhere), `non_limber_integration_method='FKEM'` [src: installed].
  The 2018 paper's non-Limber route was Angpow, limited to galaxy
  clustering without magnification [src: Sect. III.3.2].
- Real-space correlation functions: the flat-sky Hankel transform is the
  default; brute-force Gauss–Kronrod over Bessel functions is kept
  "primarily for testing and validation", and FFTLog is preferred; FFTLog
  needs C_ℓ sampled to very small scales, which CCL supplies by a power-law
  extrapolation C_ℓ ∝ ℓ^β with β from the last two input values; the
  paper states agreement with brute force "well within cosmic-variance
  uncertainties" [src: Sect. III.4]. The installed `correlation` default
  is `method='fftlog'` [src: installed].
- FFTLog accuracy parameters for 3D Hankel transforms (`FFTLogParams`):
  `padding_lo_fftlog = 0.1`, `padding_hi_fftlog = 10`, `n_per_decade = 100`,
  `extrapol = 'linx_liny'`, `plaw_fourier = −1.5` (the pre-whitening tilt
  P(r) ∝ r^tilt "to avoid aliasing"), `plaw_projected = −1.0` [src:
  installed, `fftlog_params.py`].

### Step 6. Configure the halo-model calculator
<!-- key: step-6-configure-the-halo-model-calculator -->

In pyccl 3.3.6 the halo model is an explicit `HMCalculator` object with
no default mass function or bias: `mass_function` and `halo_bias` are
required keyword arguments; `log10M_min = 8`, `log10M_max = 16`,
`nM = 128` samples uniform in log₁₀ M, `integration_method_M='simpson'`
(or `'spline'`) [src: installed, `halo_model.py`]. Its consistency check
raises "Inconsistent mass definitions" when profiles, mass function and
bias use different mass definitions [src: same]. Eleven mass
functions, four bias models and seven concentration models are shipped
(module listing of `pyccl.halos`); `MassFuncTinker08` defaults to
`mass_def="200m"` [src: installed].

Low-mass completion. The two-halo term should tend to the linear spectrum
as k → 0, which is numerically hard because most mass functions place
much mass in low-mass haloes. The 2018 code integrated between 10⁷ and
10¹⁷ M_⊙ with `GSL_INTEG_GAUSS41` at relative tolerance 10⁻⁴ and added
the missing mass "as a delta function in mass at the lower limit"
[src: arXiv:1812.05995, Sect. III.5]. The installed calculator does the
same: it stores (ρ₀ − ∫ M n dM)/M₀ and, for bias-weighted integrals,
(ρ₀ − ∫ M n b dM)/M₀, and adds that term times the integrand at the lowest
mass [src: installed, `_get_mass_function`, `_get_halo_bias`,
`_integrate_over_mf`]. Lowering `log10M_min` changes how much of the
integral is carried by this correction.

σ(M) and the mass function. dσ⁻¹/dM is obtained from a spline of σ(M)
over 10⁶–10¹⁷ M_⊙ with half-step finite differences; accuracy "is reduced
at the edges of these splines", and extreme mass ranges may need changed
spline parameters [src: Sect. III.5]. For Tinker, the fit parameters are
Akima-interpolated in log Δ between the tabulated values (200 ≤ Δ ≤ 3200,
mean density) rather than using the published fitting formulae, because
at Δ = 200 the formula and the table differ by more than the 10⁻⁴
benchmark tolerance and "the tabulated version is in common use"
[src: Sect. III.5, IV.3].

### Step 7. Validate a facade against a benchmark
<!-- key: step-7-validate-a-facade-against-a-benchmark -->

Two metric families are used, chosen by whether the quantity is
observable.

- Non-observables (distances, growth, kernels, P(k)): a fractional
  difference in CCL [src: arXiv:1812.05995, Sect. IV]; the symmetric mean
  absolute percentage error in CLOE,
  SMAPE = (100/N) Σᵢ |Fᵢ^CLOE − Fᵢ^Bench| / ((|Fᵢ^CLOE| + |Fᵢ^Bench|)/2),
  chosen because it measures agreement "without assuming which of the two
  is correct", and also plotted per point because a single number hides
  trends in redshift or scale (Euclid Collaboration 2025,
  arXiv:2510.09141) [src: Sect. 4.1, Eq. 2].
- Observables: the distance dᵢ = |Oᵢ^CLOE − Oᵢ^Bench|/σ_{Oᵢ}, with σ from
  the diagonal of a Gaussian covariance built on the benchmark, summarised
  as d_mean and d_max; validation requires d_max < 0.1, "within 10% of the
  observational uncertainty" [src: Sect. 4.2, Eq. 3–5]. Because dᵢ ignores
  correlations and gives no overall compatibility, CLOE adds
  χ² = (B − T)ᵀ K⁻¹ (B − T) and requires χ² < 0.01 N_dof, the same 10 %
  criterion in covariance-weighted form [src: Eq. 6–7]. The photometric
  χ² is averaged over N_R = 100 Gaussian data realisations drawn about the
  benchmark [src: Sect. 4.2]. Covariances are Gaussian only (no
  super-sample, connected or mask terms) for Euclid DR3 specifications
  [src: Sect. 4.2].

The case grid matters as much as the metric. CLOE's photometric
validation has 23 cases (P01–P23) varying ten cosmologies (w0wa and
non-flat included), three n(z) of increasing irregularity (ISTF, SPV2,
SPV3, the latter two with 13 bins), four intrinsic-alignment settings,
binned or polynomial galaxy and magnification bias, and RSD on or off
[src: Sect. 3.1, Table 2]. The irregular n(z) were chosen to test "the
stability of the code moving from smooth, simple n(z) ... to more
complicated and realistic distributions" [src: Sect. 3.1].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Default or boosted spline settings
<!-- key: default-or-boosted-spline-settings -->

Defaults buy speed at initialisation; the CCL paper finds them adequate
for most LSS applications (Step 3). When CCL served as a benchmark for
CLOE, its authors boosted "the number of points in z and k used for the
power spectrum splines and the number of points at which the kernels are
evaluated", and used quadrature Limber integration, "the most accurate
and for which the best agreement is found"; CCL v3.0.2 was given CLOE's
matter power spectrum and computed its own growth factor [src:
arXiv:2510.09141, App. C; Sect. 2.1.2]. A facade used as a reference
should be boosted; one used inside a chain can stay at defaults if a
boosted run shows the difference is below the chosen tolerance.

### Which non-linear spectrum a facade returns
<!-- key: which-non-linear-spectrum-a-facade-returns -->

The same request gives different models: pyccl's default
`matter_power_spectrum='halofit'` is CCL's own implementation
(`physics-and-methods.md#non-linear-corrections-shipped-with-the-solvers`);
pyccl with the CAMB non-linear spectrum defaults to CAMB `'mead'`
(HMcode-2016); cosmoprimo maps `'halofit'` to CAMB `'original'` and
`'mead'` to HMcode-2016; a direct CAMB call defaults to HMcode-2020
(Step 2). Write the CAMB version name explicitly whenever the non-linear
spectrum enters a comparison. Accuracy of each model:
`cosmo-theory-foundations/deep/halo-model-nonlinear.md`.

### Accuracy of the engine call inside a facade
<!-- key: accuracy-of-the-engine-call-inside-a-facade -->

pyccl pins CAMB to `AccuracyTarget = 0` and `lens_potential_accuracy = 0`
(Step 2); cosmoprimo leaves CAMB v2's lensing default. For P(k)-only LSS
work pyccl switches lensing off, so the second setting does not enter;
the first sets CAMB's general accuracy target, whose effect on P(k) was
not read (see Not verified). Both facades accept extra engine parameters
(`extra_parameters={'camb': {...}}` in pyccl, `accuracy` or attribute
names in cosmoprimo).

### pyccl or jax-cosmo
<!-- key: pyccl-or-jax-cosmo -->

jax-cosmo (Campagne et al. 2023, arXiv:2302.05163) buys gradients, JIT
compilation and GPU execution at the cost of physics approximations, all
read in its Sect. 3.1:

- background E²(a) = Ω_m a⁻³ + Ω_k a⁻² + Ω_de e^{f(a)}, with "relativistic
  contributions of massless neutrinos and photon radiation, as well as
  the massive neutrino contribution ... currently neglected" [src: Eq. 1–2];
- χ(a) linearly interpolated from 256 log-spaced knots over
  log₁₀ a ∈ [−3, 0], RK4 [src: Sect. 3.1.1];
- no Boltzmann solver: Eisenstein–Hu transfer function, halofit of
  Takahashi or Smith, without the Bird et al. neutrino correction, no
  baryonic feedback [src: Sect. 3.1.2];
- first-order Limber only, Simpson's rule on 512 knots; number counts with
  b(z) and no RSD; NLA-type intrinsic alignments with C ≈ 0.0134
  [src: Sect. 3.1.3, Eq. 8–11].

Validated against CCL 2.5.1 at "few 10⁻³ or better"; the differences come
from integration methods and quadrature points, and raising them costs
speed and "increases the XLA compilation memory requirements
significantly"; the authors state the code "will have to be reviewed to
tackle Stage IV accuracy requirements", non-Limber C_ℓ being one
limitation [src: Sect. 3.2].
On a DES-Y1-like 3×2pt likelihood with 21 parameters, the gain of NUTS
over Cobaya's Metropolis–Hastings in effective samples per model call was
small: ε ≈ 3 % with one call per sample for Cobaya, ε ≈ 50 % with 2⁵ or
more calls per sample for NUTS; the authors expect the advantage at
higher dimension [src: Sect. 5.5, Eq. 33, Table 2].

### cloelib's protocol design or a monolithic facade
<!-- key: cloelib-s-protocol-design-or-a-monolithic-facade -->

cloelib (Bonici et al. 2026, arXiv:2605.23839) separates four layers
(background, perturbations, observables, summary statistics), each a
Python protocol (PEP 544), so that any engine meeting the protocol can be
swapped in; `Background` and `Perturbations` are `@runtime_checkable`,
and compliance can be asserted at the start of an analysis and in
continuous integration [src: Software Design; Protocol Compliance]. The
stated reason: extending CLOE "often required intrusive modifications
across multiple parts of the software, leading to the accumulation of
technical debt" [src: Statement of need]. `JAXBackground` and the JAX
linear and non-linear perturbation classes are differentiable through
`jax.grad`, `jax.jacobian` and `jax.hessian` [src: Automatic
Differentiation with JAX]. Cost per call depends on the Perturbations
backend (Boltzmann solver or emulator) [src: Computational times].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Δ ln k for the high-k Taylor derivative | 10⁻² | CCL | arXiv:1812.05995 | Sect. III.2 |
| CCL `K_MAX_SPLINE` | 50 Mpc⁻¹ (2018 tests and 3.3.6 default) | CCL | arXiv:1812.05995; pyccl 3.3.6 | Sect. IV.2.2; installed |
| Spline vs direct CLASS, massive-ν cosmologies | < 10⁻⁴ (K_MIN–K_MIN_SPLINE); < 10⁻³ (K_MAX_SPLINE–K_MAX) | CCL | arXiv:1812.05995 | Sect. IV.2.2 |
| HMF numerical accuracy | 3 × 10⁻⁵ on σ, 10⁻³ on log σ⁻¹, 5 × 10⁻⁵ on log(M²/ρ̄ dn/dM) | CCL vs CosmoMAD, BBKS input | arXiv:1812.05995 | Sect. IV.3 |
| Halo-model mass range | 10⁷–10¹⁷ M_⊙, rtol 10⁻⁴ (2018); 10⁸–10¹⁶, 128 samples, Simpson (3.3.6) | CCL | arXiv:1812.05995; pyccl 3.3.6 | Sect. III.5; installed |
| jax-cosmo vs CCL 2.5.1 | few 10⁻³ or better | jax-cosmo 0.1 | arXiv:2302.05163 | Sect. 3.2 |
| jax-cosmo grids | χ: 256 knots, RK4; C_ℓ: Simpson, 512 knots | jax-cosmo 0.1 | arXiv:2302.05163 | Sect. 3.1 |
| NUTS against Cobaya MH, 21-parameter 3×2pt | ε ≈ 50 % at ≥ 2⁵ calls/sample vs ε ≈ 3 % at 1 call | jax-cosmo | arXiv:2302.05163 | Sect. 5.5 |
| CLOE validation thresholds | d_max < 0.1; χ² < 0.01 N_dof; N_R = 100 realisations | Euclid DR3 specifications | arXiv:2510.09141 | Sect. 4.2, Eq. 5–7 |
| CLOE photometric case grid | 23 cases, 10 cosmologies, 3 n(z) | CLOE | arXiv:2510.09141 | Sect. 3.1, Table 2 |
| cloelib 3×2pt timing | ≈ 0.06 s per call for 78 spectra (6 bins, 3000 ℓ, 512 k, 500 z, Limber) after 1 s initialisation; ≈ 0.1 s for 351 spectra (13 bins) | Apple M4 laptop; CAMB background, HMCode2020emu | arXiv:2605.23839 | Computational times |
| cloelib full-shape multipoles | ≈ 3 ms per redshift bin | comet-emu backend | arXiv:2605.23839 | Computational times |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Changing a precision parameter after building the cosmology.** The
  values are copied at construction (Step 1); a later change to
  `pyccl.spline_params` does not reach an existing object. Test: compare
  `cosmo._spline_params` with the intended values.
- **"halofit" or "mead" read as one model across facades.** Step 2 and
  "Which non-linear spectrum a facade returns". Test: print the CAMB
  `halofit_version` that the wrapper passed, or compare with a direct CAMB
  call at named version.
- **Extrapolated P(k) taken as computed.** Above `K_MAX_SPLINE` CCL uses a
  quadratic extrapolation of ln P; small-scale projected statistics
  (high-ℓ lensing, σ(R) at small R) can depend on it. Test: rerun with a
  larger `K_MAX_SPLINE` (the paper's own suggestion for some
  linear-spectrum uses) [src: arXiv:1812.05995, Sect. IV.2.2].
- **Halo-model integrals sensitive to the mass bounds.** The low-mass
  completion carries the missing mass (Step 6); the σ(M) spline loses
  accuracy at its edges [src: Sect. III.5]. Test: move `log10M_min` and
  `log10M_max` and check the k → 0 limit of the two-halo term against the
  linear spectrum.
- **Lensing kernel under-sampled.** pyccl's warning (Step 4) is emitted
  with `importance='low'` [src: installed].
- **jax-cosmo outside its physics.** No radiation, no massive neutrinos,
  Eisenstein–Hu transfer, Limber only, no RSD in number counts (pyccl or
  jax-cosmo above). Test: compare with pyccl at the analysis' scales and
  in units of the data error, as in Step 7.
- **A validation that passes on smooth inputs only.** CLOE's distance to
  CCL "increases with the complexity of the source and lens redshift
  distribution", most for photometric clustering, whose kernels are
  narrower [src: arXiv:2510.09141, App. C]. Include realistic n(z) in a
  validation grid.
- **A benchmark that cannot run every case.** CCL v3.0.2 has a different
  RSD recipe, so CLOE's RSD cases were checked against LiFE only [src:
  arXiv:2510.09141, Sect. 2.1.2].

## Reading list
<!-- key: reading-list -->

- Foundation: Chisari et al. 2018, arXiv:1812.05995 — Sect. III for the
  spline, extrapolation and integration scheme; Sect. IV for the metrics
  and the halo-mass-function tests.
- Method: Euclid Collaboration 2025, arXiv:2510.09141 — Sect. 4 for SMAPE,
  the d_max and χ² criteria; Table 2 for a validation case grid; App. C
  for how CCL was boosted as a benchmark.
- Method: Bonici et al. 2026, arXiv:2605.23839 — Software Design for the
  protocol layers; Computational times.
- Application and limits: Campagne et al. 2023, arXiv:2302.05163 —
  Sect. 3.1 for what is approximated, Sect. 3.2 for the CCL comparison,
  Sect. 5.5 for the NUTS gain at 21 parameters.

## Not verified
<!-- key: not-verified -->

- The effect of CAMB `AccuracyTarget = 0` (as set by pyccl) on the matter
  power spectrum was not read in the CAMB paper or measured.
- The meaning of the pyccl parameters `DLOGK_INTEGRATION` (0.025),
  `DCHI_INTEGRATION` (5) and `N_K_3DCOR` (100 000) was not read in a
  docstring; only their values.
- cosmoprimo's CLASS engine settings (precision parameters passed to
  `pyclass`) and its JAX-friendly parts were not read.
- cloelib's units and its accuracy against benchmarks were not read
  (the paper read has no accuracy section); CLOE's figures are from
  arXiv:2510.09141, which validates CLOE, not cloelib.
- arXiv:2510.09141, App. C states the CCL comparison is "below the 0.1 σ
  threshold for all the cases investigated" and, in the next paragraph,
  that "the few cases above the threshold" concern the maximum
  photometric-clustering discrepancy at isolated ℓ; both are quoted as
  printed, the figure was not inspected.
- Whether pyccl 3.3.6 still accepts `matter_power_spectrum='camb'` as the
  switch to the CAMB non-linear branch was inferred from the `'camb'`
  entry of its `MatterPowerSpectra` enumeration, not run.
- Spectroscopic CLOE validation (PBJ, COFFE benchmarks) was not read.
