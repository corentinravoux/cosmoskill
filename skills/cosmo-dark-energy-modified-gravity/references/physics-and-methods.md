# Physics and methods — dark energy and modified gravity

Scope: how the equation of state of dark energy and departures from general
relativity are parameterised, measured and compared with Λ; the models,
estimators, statistics and codes in current use.

Snapshot: 2026-10-07

Flags: `[src]` read this session in the cited paper; `[sec]` from a named
secondary source; `[der]` derived here. Equations without a flag are textbook
definitions.

## 1. What is measured
<!-- key: what-is-measured -->

Two classes of observable carry the information, and the whole field is
organised around keeping them apart.

- **Background (geometry).** Distances and expansion rates: `D_M(z)`,
  `D_H(z) = c/H(z)`, `D_V(z)` from BAO in units of the sound horizon `r_d`;
  relative luminosity distances from supernovae; the angular acoustic scale
  `theta_*` from the CMB. Dark energy enters through `H(z)` only. Data side:
  `cosmo-galaxy-clustering`, `cosmo-lyman-alpha`, `cosmo-supernovae`,
  `cosmo-cmb`.
- **Perturbations (growth and lensing).** The growth rate `f sigma8` from
  redshift-space distortions and peculiar velocities, the lensing (Weyl)
  potential from cosmic shear, galaxy–galaxy lensing and CMB lensing, the ISW
  effect. Modified gravity changes these even when the background is that of
  ΛCDM. Data side: `cosmo-weak-lensing`, `cosmo-peculiar-velocities`,
  `cosmo-cmb-lss-cross-correlations`.

Comparing the two histories is the classic test: Linder 2005,
arXiv:astro-ph/0507263, argues that precision comparison of expansion history
and growth history distinguishes a smooth dark-energy component from a
modification of the field equations [src]. Reviews: Huterer and Shafer 2017,
arXiv:1709.01091 (dark-energy observables and consistency tests); Ishak 2018,
arXiv:1806.10122, Koyama 2015, arXiv:1504.04623, and Ferreira 2019,
arXiv:1902.10503 (tests of gravity); Joyce et al. 2014, arXiv:1407.0059
(theory beyond Λ).

## 2. Dark-energy equation of state
<!-- key: dark-energy-equation-of-state -->

### 2.1 Definitions
<!-- key: definitions -->

- Equation of state `w = p/(rho c^2)`; Λ has `w = −1`.
- Density evolution for general `w(a)`: `rho_DE(a)/rho_DE,0 = exp{3 ∫_a^1 [1 +
  w(a')] dln a'}`.
- **CPL** (Chevallier and Polarski 2000, arXiv:gr-qc/0009008; Linder 2002,
  arXiv:astro-ph/0208512): `w(a) = w0 + wa (1 − a)`, for which
  `rho_DE(a)/rho_DE,0 = a^{−3(1 + w0 + wa)} exp[−3 wa (1 − a)]`. `w0` is the
  value today; `w0 + wa` is the value at early times; the slope is `dw/dln a =
  −wa a`.
- **Pivot.** `w_p = w0 + wa (1 − a_p)`, with `a_p` chosen so that `w_p` and
  `wa` are uncorrelated for the data set at hand. `z_p` depends on the data:
  0.53 for DESI DR2 + CMB, 0.31 with DESY5 added (arXiv:2503.14738) [src];
  0.24 for DES Y3 alone (arXiv:2207.05766) [src].
- **Figure of merit.** The Dark Energy Task Force (Albrecht et al. 2006,
  arXiv:astro-ph/0609591) defined progress through the inverse area of the
  error ellipse in the `w0`–`wa` plane, equivalently `1/[sigma(w_p)
  sigma(wa)]` up to a constant. Definitions differ by constant factors between
  papers (the sibling `cosmo-supernovae` records a factor 19.4 between two
  conventions [sec]); compare only values computed the same way. Unite quotes
  315 (arXiv:2609.05053) [src].
- **Phantom divide.** `w = −1`. `w < −1` means a dark-energy density that
  grows with time and, for a single non-interacting fluid, a violation of the
  null energy condition.

### 2.2 Why CPL, and what it hides
<!-- key: why-cpl-and-what-it-hides -->

- Linder 2007, arXiv:0708.0024: the form `w0 + wa z/(1+z)` "is robust", while
  high-order polynomials and cutting off the high-redshift behaviour "can be
  pathological" [src].
- The same paper is the origin of the "mirage": CMB data consistent with Λ
  force lower-redshift probes to return an average `w ≈ −1` unless they are
  sensitive to `w(z)` [src]. In the `w0`–`wa` plane this is a line through
  (−1, 0) along which the distance to last scattering is nearly that of ΛCDM.
  The DESI posteriors lie along it (arXiv:2503.14743) [src].
- In CPL with `theta_*` and `Omega_m` fixed by the CMB, `w0 > −1` implies
  `wa < 0` and a crossing of −1: "the necessity of such a crossing and the
  redshift at which it occurs is determined by the requirement to match the
  precise CMB measurement of theta_* together with Omega_m" (arXiv:2503.14738)
  [src]. A crossing in the best-fit CPL line is therefore partly a property of
  the parameterisation.
- Wolf and Ferreira 2023, arXiv:2310.07482, argue that surveys will at best
  deliver "a phenomenological description for the microphysics of dark energy"
  and that the current prescriptions are ill-suited to identify the
  fundamental theory [src].

### 2.3 Physical classes used in current analyses
<!-- key: physical-classes-used-in-current-analyses -->

| Class | Definition | Parameters beyond Λ | Reference | Flag |
|---|---|---|---|---|
| Thawing | scalar field frozen at `w = −1` by Hubble friction until recently, now rolling: `w` rises from −1 | 1 (calibrated) or 2 (algebraic, enforces `w ≥ −1`) | Caldwell and Linder 2005, arXiv:astro-ph/0505494; Lodha et al. 2024, arXiv:2405.13588 | [src] |
| Freezing | field slowing as it rolls: `w` falls towards −1 | — | arXiv:astro-ph/0505494 | [src] |
| Emergent | dark energy "comes into being recently, as in phase transition models" | 1 | arXiv:2405.13588 | [src] |
| Mirage | distance to last scattering close to Λ despite dynamics | 1 | arXiv:0708.0024, arXiv:2405.13588 | [src] |
| Padé-`w` | phenomenological thawing trajectories with theory-motivated priors | not read | Shlivko 2025, arXiv:2512.20832 | [src] |
| Quintom / non-minimal coupling | effective `w` crossing −1 through several degrees of freedom or a coupling to gravity | model-dependent | arXiv:2407.15832 | [src] |
| Interacting dark energy | energy exchange between dark matter and dark energy (coupled quintessence, coupled fluid) | same number as CPL in the cited comparison | Li et al. 2026, arXiv:2601.07361 | [src] |

- Caldwell and Linder showed that the simplest scalar-field models occupy
  narrow regions of the `w`–`w'` plane and set the target resolution
  `sigma(w') ≈ (1 + w)` [src].
- Wolf et al. 2024, arXiv:2408.17318: in the (`w0`, `wa`) plane thawing
  quintessence is "only marginally consistent" with the data, and compared
  with ΛCDM there is "scant evidence for thawing quintessence" [src]. Compare
  Shlivko's result in `open-questions.md` Section 1.6.
- A minimally coupled canonical scalar field always has `w ≥ −1`. A fit that
  needs `w < −1` at some redshift excludes this whole class, whatever the
  potential.

### 2.4 Non-parametric and semi-parametric reconstructions
<!-- key: non-parametric-and-semi-parametric -->

| Method | Use in DESI analyses | Reference | Flag |
|---|---|---|---|
| Binned `w(z)` with PCA of the bins | DR2: consistent with CPL; lowest-redshift bin favours `w > −1` | arXiv:2503.14743, arXiv:2503.14738 | [src] |
| Gaussian-process regression | DR2: consistent with CPL | arXiv:2503.14743 | [src] |
| Crossing statistics | DR1: Λ outside the 95% interval over some redshift ranges, significance varying with data set | Calderon et al. 2024, arXiv:2405.04216 | [src] |
| Shape function and correlation prior motivated by Horndeski theory | DR2: `w(z)` varies with redshift at ≈ 3σ | arXiv:2504.06118 | [src] |
| Reconstruction of `w_DE(a)` and EFT functions together | DR1, DR2: phantom crossing at `z ≲ 1`, non-minimal coupling preferred | arXiv:2407.15832, arXiv:2503.19898 | [src] |
| SVD of the distance data into measurable modes | DR2: tension concentrated in the `Omega_m h^2` mode | arXiv:2606.30527 | [src] |

### 2.5 The null-energy-condition bound on acoustic observables
<!-- key: the-null-energy-condition-bound-on-acoustic -->

Lewis and Chamberlain 2024, arXiv:2412.13894: for standard early-universe
physics `theta_*` fixes the ratio of the sound horizon to the distance to last
scattering independently of the late-time model; the null energy condition
then imposes "strict inequalities" on `D_H(z)`, `D_M(z)`, `D_V(z)` and
`F_AP(z)` relative to the ΛCDM prediction for any non-interacting dark energy
in FRW [src]. A data point on the wrong side of the inequality cannot be
fitted by quintessence at any parameter value; it needs phantom behaviour, an
interaction, modified gravity, a change of early-universe physics, or a
systematic error.

## 3. How the `w0wa` analyses are run
<!-- key: how-the-w0wa-analyses-are-run -->

Reference implementation: DESI DR2 (arXiv:2503.14738, section "Cosmological
Inference") [src].

- Sampler and theory code: Cobaya with CAMB; Metropolis–Hastings MCMC;
  convergence `R − 1 < 0.01` or an effective sample size ≳ 10^3.
- Priors on `w0`, `wa`: uniform; the lower bound `wa > −3` is reached by the
  BAO-only and BAO + CMB-prior posteriors [src]. Ranges are those of Table 2
  of arXiv:2404.03002.
- Best fit: iminuit started from the MAP of each chain. `Delta chi2_MAP` is
  twice the difference of the negative log posterior at the two maxima, so it
  includes non-uniform priors.
- **Compressed CMB.** A Gaussian prior on (`theta_*`, `omega_b`, `omega_bc`)
  with means (0.01041, 0.02223, 0.14208), built from the CamSpec likelihood
  after marginalising over late-time effects (ISW, lensing) [src]. It
  reproduces the `w0`–`wa` posterior of the full CMB but not its `Delta chi2`,
  which lensing changes (`results.md` Section 1.1). A shift-parameter
  compression (`R`, `l_A`, `omega_b`) gives consistent results [src].
  Srivastav, Bansal and Huterer 2026, arXiv:2606.18455, publish "CMBComp",
  compressed likelihoods for the SPT-3G D1 + ACT DR6 + Planck combination in
  five model spaces including `w0waCDM`, validated against full-CMB chains
  with DESI DR2 BAO [src].

**Perturbations of dark energy.** When `w(a)` crosses −1 a single perfect
fluid has divergent perturbations, so Boltzmann codes need a prescription for
the crossing. EFTCAMB "handles phantom-divide crossing models" and evolves the
full linear dynamics without a quasi-static approximation (Hu et al. 2013,
arXiv:1312.5742) [src]. State the prescription used whenever a CMB likelihood
with lensing or ISW is combined with a crossing `w(a)`.

## 4. Modified-gravity parameterisations
<!-- key: modified-gravity-parameterisations -->

### 4.1 `mu`, `Sigma`, `eta`
<!-- key: mu-sigma-eta -->

Metric (conformal Newtonian gauge): `ds^2 = a^2 [−(1 + 2 Psi) dtau^2 + (1 − 2
Phi) dx^2]`.

- `k^2 Psi = −4 pi G a^2 mu(a,k) rho Delta` — modified Poisson equation for
  the potential that moves non-relativistic matter. Growth and RSD measure
  `mu`.
- `k^2 (Phi + Psi) = −8 pi G a^2 Sigma(a,k) rho Delta` — the Weyl potential
  that deflects light. Lensing measures `Sigma`.
- `eta = Phi/Psi` — gravitational slip; `Sigma = mu (1 + eta)/2`.
- General relativity with negligible anisotropic stress: `mu = Sigma = eta =
  1`.

Functional forms in use:

| Form | Where | Flag |
|---|---|---|
| `Sigma(k,z) = Sigma0 Omega_Lambda(z)/Omega_Lambda,0`, `mu(k,z) = mu0 Omega_Lambda(z)/Omega_Lambda,0` for the departures from GR; no scale dependence | DES Y3 (arXiv:2207.05766) | [src] |
| Time-only functional form in ΛCDM and `w0wa` backgrounds; then 2 redshift bins; then 2 × 2 bins in redshift and scale (4 and 8 parameters) | DESI DR1 (arXiv:2411.12026) | [src] |
| Cubic-spline reconstruction of `mu`, `Sigma` and the dark-energy density fraction as functions of redshift | MGCAMB 2023 (Wang et al. 2023, arXiv:2305.05667) | [src] |

Convention traps: (i) some papers quote `mu0`, `Sigma0` as departures (GR =
0), others as values (GR = 1); (ii) `eta` is defined as `Phi/Psi` or its
inverse; (iii) MGCAMB historically worked in (`mu`, `gamma_slip`) and
converts, the 2023 version implements (`mu`, `Sigma`) directly
(arXiv:2305.05667) [src]; (iv) the time dependence tied to `Omega_DE(a)`
forces the modification to vanish at high redshift, so a constraint on `mu0`
is a constraint at `z ≲ 1` only.

### 4.2 Growth index
<!-- key: growth-index -->

`f(a) ≡ dln D/dln a = Omega_m(a)^gamma`, introduced by Linder
(arXiv:astro-ph/0507263) with a fitting formula for the linear growth
"accurate to 0.05–0.2%" [src]. General relativity with flat ΛCDM gives
`gamma = 0.55` (arXiv:2302.01331) [src]. `gamma > 0.55` means slower growth
than GR at the same `Omega_m(a)`. One number, scale-independent by
construction; it cannot represent `f(R)`-type scale-dependent growth.

### 4.3 Effective field theory of dark energy and Horndeski
<!-- key: effective-field-theory-of-dark-energy-and -->

- Gubitosi, Piazza and Vernizzi 2012, arXiv:1210.0201: a "universal
  description of dark energy and modified gravity that includes all
  single-field models", written as the most general unitary-gauge action; "the
  background evolution depends on only three operators", the others start at
  quadratic order in perturbations [src].
- Bellini and Sawicki 2014, arXiv:1404.3713: for one universally coupled
  scalar field (Horndeski), all linear cosmology is compressed "into five
  independent and arbitrary functions of time only and one constant": the
  expansion history, the matter density today, and four functions describing
  dark energy [src]. The four are `alpha_K` (kineticity), `alpha_B`
  (braiding), `alpha_M` (running of the Planck mass) and `alpha_T` (tensor
  speed excess).
- **EFT basis** used by EFTCAMB and DESI: a non-minimal coupling function
  `Omega(a)`; DESI DR1 fits a power law `Omega(a) = Omega_0 a^{s_0}`
  (arXiv:2411.12026) [src]. Pan and Ye (arXiv:2503.19898) expand
  `Omega^EFT(a) = Sum_i c_i Omega_DE(a)^i` and find the data constrain up to
  the quadratic order [src].
- **α basis** used by hi_class and DESI: `alpha_i(a) = c_i Omega_DE(a)`; DESI
  DR1 quotes `c_M` and `c_B` (arXiv:2411.12026) [src].
- Stability: viable models must be free of ghost and gradient instabilities;
  EFTCAMB has "a built-in check for the fulfillment of general stability
  conditions such as the absence of ghost and superluminal propagation"
  (arXiv:1312.5742) [src]. Stability conditions act as priors and cut the
  parameter space sharply, which produces one-sided posteriors such as
  `Omega_0 = 0.012 (+0.001/−0.012)` [src].

### 4.4 Horndeski after GW170817
<!-- key: horndeski-after-gw170817 -->

GW170817 and GRB 170817A (arXiv:1710.05834) fixed the speed of gravitational
waves to that of light: `abs(c_g/c − 1) ≤ 5 × 10^-16` (arXiv:1710.05901)
[src]. Consequences read in the three October 2017 papers:

- "A large class of scalar-tensor theories and DE models are highly
  disfavored"; the covariant Galileon is the worked example (arXiv:1710.05901)
  [src].
- "Of the three functions describing quartic and quintic beyond Horndeski
  theories, only one remains and reduces to a standard conformal coupling to
  the Ricci scalar for Horndeski theories"; the relations are stable under
  quantum corrections (arXiv:1710.05877) [src].
- Stringent constraints on general scalar–tensor and vector–tensor theories
  and a bound on the graviton mass in bimetric theories (arXiv:1710.06394)
  [src].

In the α basis this is `alpha_T = 0` today. What survives in Horndeski theory
is the part whose coupling to curvature is conformal [src, arXiv:1710.05877];
Horndeski theory as a whole "includes general relativity and many known
modified gravity theories such as generalized Galileons, f(R) and Brans-Dicke"
(arXiv:2407.15832) [src]. The non-minimal-coupling models proposed for the
DESI signal (Section 2.3) are built inside the surviving subclass. Which named
models survive, and the caveat about the frequency at which the bound applies,
were not re-read this session (`open-questions.md`, "Not verified").

## 5. Screening
<!-- key: screening -->

A light scalar coupled to matter mediates a fifth force that Solar-System
tests exclude unless it is suppressed locally. Reviews: arXiv:1407.0059;
Burrage and Sakstein 2017, arXiv:1709.09071; Brax et al. 2022,
arXiv:2201.10817; arXiv:1504.04623.

| Mechanism | Principle | Canonical reference | Flag |
|---|---|---|---|
| Chameleon | the scalar mass depends on the local matter density: heavy where the density is high, "essentially free" where it is low | Khoury and Weltman 2003, arXiv:astro-ph/0309300 | [src] |
| `f(R)` (Hu–Sawicki) | a chameleon in disguise; the scalar degree of freedom is locked to the GR value "across more than 25 orders of magnitude in density"; requires the galactic halo to keep the galaxy at high curvature | Hu and Sawicki 2007, arXiv:0705.1158 | [src] |
| Symmetron | coupling switched off in dense regions by symmetry restoration | named with chameleons in the abstract of arXiv:1709.09071 | textbook mechanism |
| Vainshtein | derivative self-interactions suppress the force inside a radius around a source (Galileons, DGP-like models) | review: arXiv:1407.0059 | textbook mechanism |

The Hu–Sawicki model is specified by the background field value `f_R0` (and an
index `n`); smaller `abs(f_R0)` means a shorter-range force and closer
agreement with GR. Through the Yukawa connection, the DESI DR1 limit `log10
abs(f_R0) < −4.59` corresponds to a range `lambda < 17.81 Mpc`
(arXiv:2604.26915) [src].

Tests exploit the environment dependence: unscreened objects in low-density
environments behave differently from screened ones.

| Test | Signature | Reference | Flag |
|---|---|---|---|
| Galaxy morphology | offsets between stars and gas, warps of stellar disks, from differential screening of a galaxy's components | arXiv:2009.08743 | [src] |
| Cluster abundance | enhanced halo mass function | arXiv:1412.0133 | [src] |
| Cluster lensing versus kinematics | dynamical and lensing masses differ under a fifth force | arXiv:2604.23631 | [src] |
| Distance ladder | fifth force alters the Cepheid period–luminosity relation in unscreened hosts | arXiv:2512.14814 | [src] |
| Scale-dependent growth in the galaxy power spectrum | Yukawa-like enhancement below the Compton wavelength | arXiv:2604.26915 | [src] |
| Cosmic shear, fully non-linear | change of the non-linear matter power spectrum | arXiv:2010.16416 | [src] |
| Laboratory and astrophysical searches | new tests "both in the laboratory and using astrophysical objects", and reinterpretation of existing data | arXiv:1709.09071 | [src] |

## 6. The `E_G` statistic
<!-- key: the-eg-statistic -->

Zhang et al. 2007, arXiv:0704.1932: an observable "whose expectation value is
equal to the ratio of the Laplacian of the Newtonian potentials to the
peculiar velocity divergence" [src]. In practice

`E_G(l or R) = [lensing–galaxy cross-correlation] / [beta × galaxy
auto-correlation]`, with `beta = f/b`,

so that the linear bias and `sigma8` cancel (arXiv:1511.04457) [src]. In
general relativity `E_G = Omega_m,0 / f(z)` on linear scales,
scale-independent; in terms of Section 4.1 it measures `Sigma Omega_m,0 / f`.
Reference predictions: 0.401 ± 0.005 at `z = 0.555` and 0.452 ± 0.005 at `z =
0.316` for `Omega_m,0` from Planck + SDSS BAO (arXiv:2401.12971) [src].

- Lensing tracer: galaxy–galaxy lensing (Reyes et al., arXiv:1003.2185) or CMB
  lensing (arXiv:1511.04457); CMB lensing reaches higher redshift and avoids
  intrinsic alignments [src].
- The prediction depends on `Omega_m,0`, which must come from elsewhere.
  Leonard et al. 2025, arXiv:2511.19194, propose a posterior predictive test
  to carry that uncertainty and show that the prior on `Omega_m,0` controls
  the power of the test [src].
- The cancellation of bias holds on linear scales only and "a careful
  treatment of galaxy bias is required" (arXiv:2511.19194) [src].

## 7. Model comparison practice
<!-- key: model-comparison-practice -->

| Statistic | Definition | What it answers | Dependence on priors |
|---|---|---|---|
| `Delta chi2_MAP` → σ | difference of `−2 ln` posterior at the two maxima, converted with Wilks' theorem for the number of extra parameters | can the nested null be rejected? | only through non-uniform priors at the maximum |
| Profile likelihood | likelihood maximised over all other parameters at each value of the parameter of interest | frequentist confidence interval | none |
| DIC | `DIC = D(theta_bar) + 2 p_D`, `p_D = <chi2> − chi2(theta_bar)` | fit quality penalised by the effective number of constrained parameters | weak |
| AIC, BIC | `chi2_min + 2k`, `chi2_min + k ln N` | fit quality with a fixed penalty per parameter | none |
| Bayes factor | ratio of evidences `Z = ∫ L pi dtheta` | relative probability of two models given priors | strong: wider priors on the extra parameters favour the simpler model |
| e-value | likelihood-ratio process valid under repeated looks | evidence across successive data releases | needs a pre-specified alternative |

Facts read this session:

- DESI converts `Delta chi2_MAP` with 2 extra degrees of freedom: −12.5 →
  3.1σ, −21.0 → 4.2σ (arXiv:2503.14738) [src].
- DIC scale used by DESI: at least 2 "not insignificant", up to 5 "positive",
  up to 10 "strong", above 10 "decisive"; for non-nested models DIC ranks but
  gives no absolute scale (arXiv:2503.14743) [src]. The definition and
  properties of the information criteria are in Liddle 2007,
  arXiv:astro-ph/0701113, which notes that the DIC, unlike AIC and BIC,
  "allows for parameter degeneracy" [src].
- Evidence is computed with nested sampling (PolyChord) and anesthetic; the
  log-evidence splits into a fit term `<ln L>` and an Occam penalty
  `<ln(P/pi)>` (arXiv:2503.14743) [src]. Review of Bayesian model selection:
  Trotta 2008, arXiv:0803.4089.
- Profile likelihoods agree with the Bayesian intervals for BAO + CMB + SN
  (arXiv:2506.12004) [src] and disagree strongly for full-shape clustering
  without supernovae (arXiv:2508.11811) [src].

**Consistency before combination.** A preference for an extended model
obtained by combining data sets that disagree under the base model is a
restatement of that disagreement. Tools: the estimators of agreement and
disagreement of Raveri and Hu 2018, arXiv:1806.04649, which account for prior
information and give the significance of tensions and of confirmation biases
[src]; the evidence-ratio interpretation of Handley and Lemos 2019,
arXiv:1902.04029, which shows that the DES-type evidence ratio is
prior-dependent, wider priors boosting the apparent agreement [src]. Details
belong to `cosmo-statistics-inference`.

## 8. Blinding
<!-- key: blinding -->

- DESI BAO measurements are blinded: arXiv:2503.14738 has a dedicated
  subsection [src]; the sibling `cosmo-galaxy-clustering` describes the
  catalogue-level procedure [sec].
- DES Y3 extended-model analysis: validated on simulated data and run as
  "blind analyses of real data" (arXiv:2207.05766) [src].
- The dark-energy interpretation itself is not blind in any published
  analysis: the choice of external data (which supernova sample, which CMB
  likelihood, lensing or not) is made after the BAO and supernova results are
  known, and DESI reports all three supernova samples for that reason.
  Independent reanalyses choose their combination knowing the answer.

## 9. Codes
<!-- key: codes -->

| Code | Purpose | Reference | Flag |
|---|---|---|---|
| MGCAMB | (`mu`, `Sigma`) and related phenomenological functions in CAMB; massive neutrinos and dynamical dark energy since 2019; spline reconstruction and Cobaya support since 2023 | Zucca et al. 2019, arXiv:1901.05956; arXiv:2305.05667 | [src] |
| ISiTGR | CAMB/CosmoMC patch: functional, binned and hybrid time and scale dependence of MG parameters, dynamical dark energy, massive neutrinos, curvature | Garcia-Quintero et al. 2019, arXiv:1908.00290 | [src] |
| MGCLASS II | phenomenological modified gravity on sub-horizon scales in CLASS | Sakr and Martinelli 2021, arXiv:2112.14175 | [src] title only |
| EFTCAMB | EFT of dark energy in CAMB; full linear dynamics, stability checks, phantom crossing | arXiv:1312.5742 | [src] |
| hi_class | Horndeski gravity in CLASS: quintessence, Brans–Dicke, `f(R)`, covariant Galileons | Zumalacárregui et al. 2016, arXiv:1605.06102 | [src] |
| CMBComp | compressed CMB likelihoods for late-time extensions | arXiv:2606.18455 | [src] |
| DEslider | visualisation of supernova systematics in the `w0`–`wa` plane | arXiv:2409.18668 | [src] |
| Cobaya, CAMB, iminuit, getdist, PolyChord, anesthetic | sampling, theory, minimisation, plotting, evidence in the DESI analyses | named in arXiv:2503.14738 and arXiv:2503.14743 | [src] |

## 10. Conventions and where the community is split
<!-- key: conventions-and-where-the-community-is-split -->

- `wa` is defined with `(1 − a)`; older papers use `w' = dw/dz` at `z = 0` or
  `dw/dln a`. `w'` of Caldwell and Linder is the derivative in units of the
  Hubble time [src].
- Significance: DESI and the supernova teams quote `Delta chi2_MAP` converted
  to σ; Unite quotes both MAP (3.3σ) and maximum-likelihood (3.1σ) values
  (arXiv:2609.05053) [src]. Bayes factors are quoted as `ln B`, as odds, or in
  words on a Jeffreys scale whose thresholds vary between authors.
- Sign of `Delta DIC` and `ln B`: DESI defines `Delta DIC = DIC(w0wa) −
  DIC(Λ)`, negative favouring `w0wa`, and `ln B = ln Z(w0wa) − ln Z(Λ)`,
  positive favouring `w0wa` [src]. Other papers reverse one or both.
- "CMB" in a combination can mean compressed priors, primary anisotropies
  only, or primary plus lensing, and Planck alone or Planck + ACT + SPT. The
  `w0wa` significance changes with each choice (`systematics.md` Section 4).
