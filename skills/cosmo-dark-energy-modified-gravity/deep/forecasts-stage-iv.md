# Forecasting dark energy and gravity for Stage-IV surveys — cosmo-dark-energy-modified-gravity dossier

Scope: how a Stage-IV dark-energy or modified-gravity forecast is set up
(observables, scale cuts, nuisance parameters, priors, Fisher or sampled
posterior), how forecast codes are validated and to what tolerance, how
systematic-error requirements are derived from a forecast, and what the
collaboration forecasts give for `w0`–`wa`, γ, μ–Σ and `f(R)`, with the
settings each number depends on; for a reader about to produce, compare
or referee a forecast.
Snapshot: 2026-10-18.
From: Euclid 2025 review (arXiv:2512.09748), Sects. 2, 3.2 and 4.2; Euclid forecast validation (arXiv:1910.09273).

Already in L2, not repeated here: the FoM definitions and the warning that
conventions differ (`physics-and-methods.md#definitions`); the
"factor of three from cross-correlations" sentence and the Caldwell–Linder
target `sigma(w') ≈ 1 + w` (`surveys-and-data.md#what-comes-next`); the
release dates of DESI, Euclid and Rubin (same file). The general theory of
Fisher matrices and the underestimate of `w0`–`wa` errors by Fisher
matrices for geometric probes belong to `cosmo-statistics-inference`
(`results.md#fisher-forecasts-against-full-posteriors` there).

Notation. `F` is the Fisher matrix, `C = F^-1` the parameter covariance,
`F_tilde_{w0 wa}` the inverse of the (`w0`, `wa`) block of `C` (the
marginalised Fisher sub-matrix). GCs: spectroscopic galaxy clustering;
GCph: photometric galaxy clustering; WL: cosmic shear; XC: the
cross-spectra between GCph and WL; 3×2pt: WL + GCph + galaxy–galaxy
lensing. "Pessimistic" and "optimistic" are the Euclid settings defined
below.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Fix the observables and their model
<!-- key: step-1-fix-the-observables-and-their-model -->

Euclid's recipe (arXiv:2512.09748, Sect. 2.2, following arXiv:1910.09273):

- **Spectroscopic clustering.** Observed power spectrum
  `P_obs(k_ref, mu_ref; z)` with Alcock–Paczynski rescaling `q_perp =
  D_A/D_A,ref`, `q_par = H_ref/H` (Eqs. 1–3, 7), Kaiser term with `b sigma8`
  and `f sigma8`, Lorentzian fingers of God with `sigma_p`, de-wiggled
  spectrum `P_dw = P_lin e^{−g_mu k^2} + P_nw (1 − e^{−g_mu k^2})` (Eq. 4),
  redshift-error damping `F_z = exp(−k^2 mu^2 sigma_r^2)` (Eq. 6) and a
  residual shot noise `P_s` as nuisance [src: Sect. 2.2]. The spectrum is
  linear theory with phenomenological damping; `sigma_p = g_mu` is fixed per
  bin "for simplicity" [src: same].
- **Photometric probes.** Limber `C_ij^XY(ell)` (Eq. 8) on the non-linear
  matter spectrum, with kernels in which Σ multiplies the lensing kernel
  (Eq. 10) and an extended NLA intrinsic-alignment kernel (Eqs. 11–12).
  eNLA, built in GR, is kept for modified gravity because IA arise on
  galaxy and cluster scales where the potentials revert to the GR form
  [src: Sect. 2.2].
- **Covariance.** Gaussian, sky fraction by rescaling the full-sky
  covariance; no super-sample or connected non-Gaussian terms; GCs and the
  photometric probes treated as uncorrelated, with GCph and galaxy–galaxy
  lensing cut to `z < 0.9` in the pessimistic combination to avoid overlap
  [src: Sect. 2.2]. Magnification bias is neglected in the baseline recipe
  and treated separately (Step 6) [src: Sect. 2.2].

### Step 2. Choose scale cuts as settings, not as one number
<!-- key: step-2-choose-scale-cuts-as-settings-not-as-one -->

| Setting | GCs `k_max` | WL `ell_max` | GCph, XC `ell_max` | Other | Source |
|---|---|---|---|---|---|
| Linear (GCs code tests) | 0.25 h/Mpc, `sigma_p = sigma_v = 0` | — | — | — | arXiv:1910.09273, Sect. 4.2.2 |
| Pessimistic | 0.25 h/Mpc, `sigma_p`, `sigma_v` marginalised | 1500 | 750 | GCph `z < 0.9` when combined with GCs | arXiv:1910.09273, Eq. 197 |
| Intermediate (GCs) | 0.30 h/Mpc, marginalised | — | — | — | arXiv:1910.09273, Sect. 4.2.2 |
| Optimistic | 0.30 h/Mpc, `sigma_p`, `sigma_v` fixed | 5000 | 3000 | no redshift cut | arXiv:1910.09273, Eq. 198 |
| Quasi-linear (GCs) | 0.15 h/Mpc | — | — | used for non-linear-method studies | arXiv:2512.09748, Sect. 2.2 |

The authors' own caveat: `k_max = 0.25 h/Mpc` is called "pessimistic", but
"one may argue that it is not pessimistic or even optimistic", since the
one-halo term is a 30% correction to linear theory there
[src: arXiv:1910.09273, Sect. 4.2.2, footnote 22]. In the optimistic
setting the non-linear GCs parameters are assumed perfectly known, which
is part of why it is optimistic [src: same].

### Step 3. Choose the parameter space and the priors
<!-- key: step-3-choose-the-parameter-space-and-the-priors -->

- Euclid: `w0`–`wa` with flat and non-flat geometry; growth with γ
  [src: arXiv:1910.09273, Sect. 5]. γ is implemented as
  `(γ, Sigma_MG = 1)`: `mu_MG(a, γ) = (2/3) Omega_m^{γ−1} [Omega_m^γ + 2 +
  H'/H + γ Omega_m'/Omega_m + γ' ln Omega_m]` (Eq. 38), lensing unchanged.
  Stated reasons: comparability with the Euclid Red Book, and
  `Sigma_MG = 1` is realised in Brans–Dicke and `f(R)`; the authors note
  that γ alone is "incomplete" because general linear perturbations need
  two free functions [src: Sect. 2.4].
- μ–Σ forecasts use `mu(z) = 1 + mu0 Omega_DE(z)/Omega_DE(0)` and the same
  for Σ (Eqs. 32–33), with a ΛCDM background for `Omega_DE(z)`, MGCAMB or
  MGCLASS II for the linear spectrum and ReACT for the non-linear one,
  computed in two limits: unscreened (US, no screening in the non-linear
  spectrum) and super-screened (SS, the spectrum returns to GR as fast as
  possible beyond linear scales) [src: arXiv:2512.09748, Sect. 4.1.1].
- LSST DESC SRD: `w0waCDM`, seven parameters with weak Gaussian priors
  "necessary to regularize the Fisher matrix" (fiducial; σ): `Omega_m`
  (0.3156; 0.2), `sigma8` (0.831; 0.14), `n_s` (0.9645; 0.08), `w0`
  (−1.0; 0.8), `wa` (0.0; 2.0), `Omega_b` (0.0492; 0.006), `h`
  (0.6727; 0.063); neutrino mass fixed to zero "for the sake of
  expediency"; no curvature. Supernovae are forecast by MCMC with the prior
  `w(a) < 0`, and the chain covariance is then combined with the Fisher
  matrices of the static probes. Stage-III priors are the Planck 2015
  "TT+TE+EE+lowP+lensing+ext" chain with `w0`, `wa` free
  [src: arXiv:1809.01669, App. I2].
- DESI design forecasts include Planck priors in all cases and the
  curvature projection that the DETF FoM definition requires
  [src: arXiv:1611.00036, Sect. 2.4.3].

### Step 4. Compute the forecast: Fisher or sampled posterior
<!-- key: step-4-compute-the-forecast-fisher-or-sampled -->

**Fisher.** Derivatives of the observables times the inverse Gaussian
covariance [src: arXiv:2512.09748, Sect. 2.2]. Euclid now differentiates
`P_obs` directly with respect to the cosmological parameters instead of
projecting from (`ln D_A`, `ln H`, `ln f sigma8`, `ln b sigma8`) per bin
as in arXiv:1910.09273 [src: same]. Numerical lessons from the Euclid
code comparison [src: arXiv:1910.09273, Sect. 4.5.1]:

- interpolate `log10 P` against `log10 k` with cubic splines and avoid
  other interpolations; 50 steps per decade in `k` was the default after
  tests at 20, 50 and 200 [src: arXiv:1910.09273, Sect. 4.5.1];
- use numerical derivatives for all parameters: semi-analytic
  derivatives with respect to `ln H` and `ln D_A` disagree with numerical
  ones for `k > 0.1 h/Mpc` and are unstable under rebinning;
- three-point stencils carry errors of order `epsilon^2`, five-point of
  order `epsilon^4`; check convergence in the step; single-probe results
  can be step-dependent while the combination is not.

DESC's Augur uses a five-point stencil with a step of 5% of each
parameter's uniform prior range (a numerical normalisation, not a prior);
the heuristic is to start near 10% and decrease until the FoM changes by
less than 1% [src: arXiv:2608.03876, Sect. 5.1].

**Sampled posterior.** CLOE samples synthetic noiseless Euclid data
vectors with Nautilus (4000 live points, 16 networks, 512 evaluations per
step), validated against PolyChord, in 58–61 dimensions for the full
combination; the FoM is computed from the area of the 68% and 95%
contours (matplotlib polygon) rather than from a Gaussian formula, after
marginalising over all cosmological and nuisance parameters
[src: arXiv:2510.09153, Sect. 2.2; Sect. 6.4]. The Euclid review uses
MCMC instead of Fisher "for some cases, given the strong non-Gaussian
nature of the parameter distribution" [src: arXiv:2512.09748, Sect. 2.2],
and re-samples the `f(R)` Fisher matrix computed in `log10 abs(f_R0)` back
into `abs(f_R0)` to show non-Gaussian contours [src: Sect. 5.2].
Srinivasan et al. 2026, arXiv:2603.11895, run full MCMC forecasts for
redshift-binned μ and η by emulating the modified-gravity boost to < 1%
of COLA simulations [src: abstract].

### Step 5. Summarise: the figure of merit and its convention
<!-- key: step-5-summarise-the-figure-of-merit-and-its -->

Euclid: `FoM = sqrt(det F_tilde_{w0 wa})`, "inverse proportional to the
area of the 2σ contour", equivalent within a constant to other literature
definitions [src: arXiv:1910.09273, Eqs. 48–49]. DESI: `(sigma_{w_p}
sigma_{w'})^-1` with `w(z) = w_p + (a_p − a) w'` and `a_p` chosen to
decorrelate the two [src: arXiv:1611.00036, Sect. 2.4.3]. For a 2×2
marginal covariance the two expressions coincide, since `det C` is
invariant under the pivot shift and `w' = wa` [der: `w_p = w0 + (1 − a_p)
wa` is a unit-determinant linear map of (`w0`, `wa`)]. What differs between
papers is the data set behind the number: Euclid-only, Euclid + CMB, DESI
with Planck priors, DESC with Stage-III priors (rows below).

The Stage-IV threshold itself depends on the document: DESI takes 110,
ten times a Stage-II value of 11 [src: arXiv:1611.00036, Sect. 2.4.3];
the DESC SRD requires a combined FoM above 500, about ten times a Stage-II
FoM of 54 from the DETF clusters + supernovae + weak lensing combination
[src: arXiv:1809.01669, Sect. 4, RH1]. Compare FoMs only within one
document's convention and data.

### Step 6. Turn the forecast into requirements and bias budgets
<!-- key: step-6-turn-the-forecast-into-requirements-and -->

**Fisher bias.** A systematic shifts the best fit by a vector `b` in
(`w0`, `wa`); its size relative to the marginalised statistical ellipse is
`r = sqrt(b · C^-1 · b)` (Eq. 2), reducing to the quadrature sum of
`b/sigma` for axis-aligned ellipses (Eq. 3). DESC sets each requirement
where `r = 1` and splits the budget in quadrature (`r = 1/sqrt(2)` for two
equal shares) [src: arXiv:1809.01669, App. H2]. Stated reason for `r = 1`
rather than `r^2 = 2.3` (the 2D 1σ `Delta chi2`): with `r^2 = 2.3` some
directions of bias would leave the 1σ ellipse, which matters when other
Stage-IV data shrink the allowed area [src: same]. `C` must be the
marginalised (`w0`, `wa`) block of `F^-1`, not a sub-block of `F`, which
would fix the other parameters and give "overly small uncertainties and
too-conservative requirements" [src: same, footnote 20].

**High-level requirements (DESC).** RH1: combined FoM > 500 with the Y10
data including systematics and Stage-III priors; if the forecast exceeds
500, the calibratable-systematics budget is enlarged until the FoM is
exactly 500. RH2: for each probe, total calibratable systematic
uncertainty below the marginalised statistical uncertainty in the
(`w0`, `wa`) plane (the only requirement applicable to Y1). RH3: at least
one growth probe and one expansion probe meet RH1–RH2, "Deviations from
General Relativity are best detected with two complementary probes".
RH4: blind analyses. Goal G1: each probe FoM > 2× its Stage-III value,
thresholds 12, 1.5, 1.3, 19 and 40 for clusters, LSS, strong lensing,
supernovae and WL [src: arXiv:1809.01669, Sect. 4].

**A worked bias.** Neglecting magnification in Euclid would bias
`w0`, `wa` by ≈ 1σ (GCph alone) and 2–5σ (GCph + WL + galaxy–galaxy
lensing); the authors warn that shifts this large, obtained from a
first-order expansion, "cannot be quantitatively trusted" but show that
magnification must be modelled. For the spectroscopic multipoles the
`w0`, `wa` shifts are ≈ 0.1σ, but the growth in the highest redshift bin
can be biased by up to 1σ [src: arXiv:2512.09748, Sects. 7.1.2, 7.2.2].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Fisher or sampled forecast
<!-- key: fisher-or-sampled-forecast -->

Fisher is cheap and exact only for a Gaussian posterior. Augur's Fisher
correlation matrices agree with PolyChord on the noiseless data vector
within `abs(Delta Corr) ≤ 0.05` for all parameters, once a numerically
stable step is chosen; with unstable steps or adaptive defaults the FoM
can come out larger and the degeneracy direction wrong
[src: arXiv:2608.03876, Sects. 5.1, 5.4]. The linear Fisher-bias formula
recovers an imposed shift to 10% only up to ≈ 1σ in `w0` and ≈ 0.5σ in
`wa` (Y1 set-up, `sigma(w0) = 0.12`, `sigma(wa) = 0.42`)
[src: Sect. 5.5]. A sampled forecast captures projection effects that a
Fisher matrix cannot: CLOE finds ΛCDM 3×2pt posteriors on `sigma8` and
`S8` shifted from the truth, traced to the degeneracy between the BBN
prior on `Omega_b h^2` and the 26 per-bin redshift shifts; it vanishes
with the shifts fixed or a flat `Omega_b h^2` prior [src: arXiv:2510.09153,
Sect. 6.3.3]. Its full-combination FoM matches the pessimistic Fisher
value of arXiv:1910.09273 despite a higher photometric `ell_max`, which
the authors attribute to the larger sampled parameter space
[src: Sect. 6.4]. Cost: computational; CLOE calls for SBI and Hamiltonian
Monte Carlo for future analyses [src: Sect. 7].

### Optimistic or pessimistic scale cuts
<!-- key: optimistic-or-pessimistic-scale-cuts -->

For `w0`, `wa` with Euclid alone the full-combination FoM goes from 377
(pessimistic) to 1257 (optimistic), flat [src: arXiv:1910.09273, Sect. 6]. For
μ–Σ it is larger and model-dependent: with conservative cuts
(`k_max^{3×2pt} = 0.25 Mpc^-1`, `k_max^{GCsp} = 0.1 Mpc^-1`) 3×2pt alone
gives 278% (SS) or 169% (US) on `mu_bar_0` and 35% or 22% on
`Sigma_bar_0`; 3×2pt + GCsp gives 24% (23%) and 3% (3%); optimistic
`k_max^{3×2pt}` brings both to ≈ 1%, which "requires ensuring that the
modelling of nonlinear scales can reach a high level of accuracy"
[src: arXiv:2512.09748, Sect. 4.2.1]. The screening prescription (SS
versus US) therefore changes the 3×2pt-only μ error (278% against 169%
above).

### Fiducial model
<!-- key: fiducial-model -->

Forecasts are centred on ΛCDM. Changing the μ–Σ fiducial to
`mu0 = −0.5`, `Sigma0 = 0.5` tightens 3×2pt alone but weakens the
combination (34% and 3% on `mu_bar_0` and `Sigma_bar_0` in SS) because
the probes become less complementary [src: arXiv:2512.09748, Sect. 4.2.1].
The direction of the supernova `w0`–`wa` degeneracy rotates from
`wa ≈ −(w0 + 1)` to `wa ≈ +(w0 + 1)` as the `Omega_m` prior tightens
[src: arXiv:1809.01669, App. I2]. Model-selection forecasts on noiseless
ΛCDM data favour ΛCDM by construction; CLOE notes that noise realisations
"may yield fluctuations that occasionally favour extended models"
[src: arXiv:2510.09153, Sect. 7].

### Euclid alone or with the CMB
<!-- key: euclid-alone-or-with-the-cmb -->

Adding SO-like CMB lensing to pessimistic Euclid raises the FoM by 20%;
full Euclid × CMB doubles it again; 1σ errors on dark-energy parameters
drop by 23–58% depending on settings; CMB curvature information cancels
the non-flat degradation [sec: Ilić et al. 2022, as summarised in
arXiv:2512.09748, Sect. 3.2.1, Table 1].

### γ alone or a two-function parameterisation
<!-- key: gamma-alone-or-a-two-function-parameterisation -->

γ with `Sigma_MG = 1` is one function; Srinivasan et al. find for binned
μ and η the "characteristic degeneracy" between them, with the
best-constrained direction `Sigma = mu (1 + eta)/2`, and CMB lensing
extending the redshift reach [src: arXiv:2603.11895, abstract]. A γ
forecast therefore says nothing about Σ.

## Numbers
<!-- key: numbers -->

All rows are **forecasts**.

| Quantity | Value | Set-up | Source | Place read |
|---|---|---|---|---|
| Fisher numerical precision needed | ≈ 10^-4 per element, for ≤ 10% on errors and FoM and ≤ 2% on orientation (assumes `r_{αβ} ≤ 0.999`) | Euclid IST | arXiv:1910.09273 | Sect. 3.1.6, Eq. 65 |
| Agreement achieved between codes | < 10% on parameter errors; GCs codes ~4% | 11 codes | arXiv:1910.09273 | Sect. 6; Sect. 4.2.3 |
| Augur agreement criteria | step-stability ≤ 10% per Fisher element at ±50% step; `max abs(Delta Corr) ≤ 0.1`; FoM within 20% | DESC 3×2pt | arXiv:2608.03876 | Sect. 4 |
| DESC 3×2pt DEFOM, Y1 / Y10 | 36.95 (SRD pipeline), 41.36 (Augur) / 147.2, 145.0 | 3×2pt only | arXiv:2608.03876 | Sect. 5.4, Fig. 8 |
| Euclid `sigma(w0)`, `sigma(wa)`, FoM, flat, GCs + WL + GCph + XC | 0.040, 0.17, 377 (pess.); 0.025, 0.092, 1257 (opt.) | Euclid only | arXiv:1910.09273; arXiv:2512.09748 | Table 13 and Sect. 6 (the conclusions point to Table 13); Sect. 3.2.1 |
| Same without XC | FoM 123 (pess.), 398 (opt.) | — | arXiv:2512.09748 | Sect. 3.2.1 |
| Same, non-flat | 0.044, 0.30, 128 (pess.); 0.026, 0.14, 500 (opt.) | — | arXiv:2512.09748 | Sect. 3.2.1 |
| WL alone without IA modelling | FoM 27 (pess., flat): "higher (but more unreliable)" | — | arXiv:1910.09273 | Table 13 caption |
| CLOE full combination | FoM > 400 (flat `w0wa`), sampled | 3×2pt + GCsp, `ell_max` 5000/3000 | arXiv:2510.09153 | abstract; Sect. 6.4 |
| `sigma(w0)/1`, `sigma(wa)`, flat, Euclid + full CMB | 0.027/0.011, 0.099/0.048 (pess./opt.) | SO-like CMB | Ilić et al. 2022 [sec] | arXiv:2512.09748, Table 1 |
| `sigma(γ)/γ`, flat `w0wa + γ` | 0.015/0.0077 Euclid; 0.0088/0.0058 with full CMB | all Euclid probes | Ilić et al. 2022 [sec] | arXiv:2512.09748, Table 1 |
| `sigma(γ)/γ`, GCs + WL only | 0.070 (pess.), 0.052 (opt.) | no GCph, no XC | arXiv:1910.09273 | Table 14 |
| `mu_bar_0`, `Sigma_bar_0` relative errors | 24% (23%), 3% (3%), SS (US), 3×2pt + GCsp, conservative cuts | ΛCDM fiducial | arXiv:2512.09748 | Sect. 4.2.1 |
| `abs(f_R0) = 5 × 10^-6` | 3% (7%) GCs; 1.4% (3%) 3×2pt; 1% (1.8%) all, opt. (pess.); > 3σ from ΛCDM (opt.) | Hu–Sawicki | arXiv:2512.09748 | Sect. 5.2 |
| DESI DETF FoM | 133 galaxy BAO; 169 with Lyα BAO; 332 adding galaxy broadband; 121 for a 9000 deg² BAO survey; Stage-IV threshold 110 | with Planck priors | arXiv:1611.00036 | Sect. 1; Sect. 2.4.3 |
| DESC requirement | combined FoM > 500 (Y10, systematics, Stage-III priors); Stage-II 54 | all DESC probes | arXiv:1809.01669 | Sect. 4 |

The γ rows differ because the Table 14 forecast could
not include GCph or XC while varying γ ("none of the available codes allow
us to include GCph or cross-correlation, while also allowing γ to vary")
[src: arXiv:1910.09273, Fig. 13 caption]; quote the row whose probe set
matches the claim.

## What goes wrong
<!-- key: what-goes-wrong -->

| Failure | How it shows | Test or fix | Source |
|---|---|---|---|
| Unconverged derivative step | FoM drifts with step size; single probes step-dependent | scan the step; five-point stencil; ±50% stability criterion | arXiv:1910.09273, Sect. 4.5.1; arXiv:2608.03876, Sect. 4 |
| Semi-analytic AP derivatives | disagreement above `k = 0.1 h/Mpc`, binning-dependent | numerical derivatives throughout | arXiv:1910.09273, Sect. 4.5.1 |
| Covariance too optimistic | no SSC or connected terms; `f_sky` rescaling instead of a mask | state it; Gaussian forecasts are lower bounds on errors | arXiv:2512.09748, Sect. 2.2 |
| Ignoring the GCs–GCph overlap | double counting | pessimistic `z < 0.9` cut on GCph | arXiv:1910.09273, Eq. 197 |
| Magnification omitted from the model | multi-σ shifts of `w0`, `wa` (photometric), up to 1σ in high-z growth | include it; Fisher-bias test | arXiv:2512.09748, Sect. 7 |
| Fisher bias beyond linearity | input bias not recovered (> 10% off) above ≈ 1σ (`w0`) or 0.5σ (`wa`) | sample the likelihood with the biased data vector | arXiv:2608.03876, Sect. 5.5 |
| Requirements from a sub-block of `F` | over-tight requirements | use the marginalised block of `F^-1` | arXiv:1809.01669, App. H2 |
| Flexible nuisance models absorbing a systematic | very loose calibratable requirements | test interactions between systematics models | arXiv:1809.01669, App. H2 |
| Projection effects invisible to Fisher | sampled marginals offset from the truth | check that the truth is the best fit; vary priors (BBN, redshift shifts) | arXiv:2510.09153, Sect. 6.3.3 |
| Comparing FoMs across documents | Stage-IV thresholds 110 against 500 for different probe sets and priors | recompute with one convention and one external-data set | arXiv:1611.00036, Sect. 2.4.3; arXiv:1809.01669, Sect. 4 |
| Screening ignored in non-linear MG forecasts | errors differ between the US and SS limits | quote both limits | arXiv:2512.09748, Sect. 4.2.1 |
| IA model built in GR used in MG | unknown amplitude change | absorb into `A_IA`; no dedicated study exists | arXiv:2512.09748, Sect. 2.2 |

Validation checklist used by the collaborations: common inputs and a
public reference set of Fisher matrices (Euclid provides both, App. A of
arXiv:1910.09273); comparison against the median of several codes;
comparison of correlation matrices, not only of errors, because they
isolate degeneracy directions [src: arXiv:2608.03876, Sect. 4]; a
nested-sampling run on the noiseless data vector; a Fisher-bias recovery
test.

## Reading list
<!-- key: reading-list -->

- Method and code validation: Euclid Collaboration 2019, arXiv:1910.09273 —
  the IST recipe, settings, precision requirement, FoM table, lessons on
  derivatives.
- Review and update: Euclid Collaboration 2025, arXiv:2512.09748 — μ–Σ,
  EFT, named models, `f(R)`, non-linear methods and magnification in
  forecasts.
- Sampled forecast: Euclid Collaboration 2025, arXiv:2510.09153 (CLOE) —
  full-posterior forecasts, projection effects, FoM from contour areas.
- Requirements flow-down: LSST DESC 2018, arXiv:1809.01669 — FoM targets,
  `r = sqrt(b C^-1 b)`, priors, Stage-III inputs.
- Fisher validation: Rogozenski et al. 2026, arXiv:2608.03876 (Augur) —
  step-size and agreement criteria, Fisher-bias limits.
- Design forecast: DESI Collaboration 2016, arXiv:1611.00036 — DETF FoM
  convention and BAO-only Stage-IV numbers.
- MG beyond Fisher: Srinivasan et al. 2026, arXiv:2603.11895 — binned μ–η
  MCMC forecasts with an emulated non-linear boost.
- Statistics background: `cosmo-statistics-inference` (Fisher against full
  posteriors).

## Not verified
<!-- key: not-verified -->

- CLOE Table 4 (FoM per probe and model): only the abstract's "exceed 400"
  (arXiv:2510.09153, abstract) and the text were read.
- Ilić et al. 2022 (Euclid × CMB forecasts): numbers taken from the Table 1
  reproduced in arXiv:2512.09748; the paper itself was not read and its
  identifier is not recorded here.
- The DESI design FoM sentence, read in full on 2026-10-25: "332 including
  galaxy broadband power spectrum to k = 0.1 h Mpc^-1", and 704 out to
  `k < 0.2 h/Mpc` (arXiv:1611.00036, Sect. 1; Table 2.9 in Sect. 2.4.3).
- The Stage-II value of 11 used by DESI comes from its reference [109]
  (arXiv:1611.00036, Sect. 2.4.3), not identified.
- No DESI DR2-era or Rubin-era updated collaboration forecast of `w0`–`wa`
  was read; the SRD (2018) and the DESI design paper (2016) predate the
  current data.
- Fisher-versus-MCMC comparisons for μ–Σ beyond the Srinivasan et al.
  abstract.
