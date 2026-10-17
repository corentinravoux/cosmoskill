# Reconstruction of w(z) — cosmo-dark-energy-modified-gravity dossier

Scope: how a non-parametric or semi-parametric reconstruction of the
dark-energy equation of state is set up (basis, high-redshift closure,
priors, perturbations, summary statistics, mock validation), and how to
choose between binning, Chebyshev expansions ("crossing statistics"),
Gaussian processes and correlation priors.
Snapshot: 2026-10-17.
From: Li 2026 review (arXiv:2606.21826), Sect. II.4; DESI extended
dark-energy paper (arXiv:2503.14743).

Already in L2, not repeated here: the one-line outcome of each DESI
reconstruction (binned, GP, crossing, Horndeski correlation prior, joint EFT,
SVD of distances) in `physics-and-methods.md#non-parametric-and-semi-parametric`;
why CPL forces a crossing and the 3.2% mock rate for a spurious crossing in
`systematics.md#parameterisation-artefacts`; prior dependence of Bayes factors
in `systematics.md#priors-on-the-dark-energy-parameters-themselves`.

Notation. `w(z)` is the equation of state; `f_DE(z) ≡ rho_DE(z)/rho_DE,0` the
normalised dark-energy density, related to `w` by
`f_DE(z) = exp(3 ∫_0^z [1 + w(z')] dln(1 + z'))` (Calderon et al. 2024,
arXiv:2405.04216, Eq. 4), and entering
`H^2/H0^2 = Omega_m,0 (1+z)^3 + Omega_r,0 (1+z)^4 + (1 − Omega_m,0 − Omega_r,0) f_DE(z)`
(Eq. 3). DESI DR2 papers use the same symbols; Gu et al. 2025
(arXiv:2504.06118) write `Omega_M` for `Omega_m,0`.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Choose the function to reconstruct
<!-- key: step-1-choose-the-function-to-reconstruct -->

| Target | What it allows | Cost | Used by |
|---|---|---|---|
| `w(z)` | any equation of state with `rho_DE > 0` | `f_DE < 0` excluded by construction | DESI DR2 binning, GP, Chebyshev (arXiv:2503.14743, Sects. IV.2, V) |
| `f_DE(z)` | effective density that changes sign, as in some modified-gravity and dark-sector-interaction models | perturbations ill-defined for `rho_DE < 0`, so the CMB enters only as compressed `(theta_*, omega_b, omega_bc)` | arXiv:2503.14743, Sect. IV.2; arXiv:2405.04216, Sect. 2.2.2 |
| `h(z) = H(z)/H0`, then `w` by differentiation | fewest assumptions on the dark sector | differentiation "amplifies noise and systematic uncertainties" | named as the reason for the `w_0`-probe of Bag et al. 2026, arXiv:2605.27230 [src: abstract] |

The `f_DE` expansion has one parameter fewer than the `w` expansion of the
same order because `f_DE(0) = 1` is imposed [src: arXiv:2503.14743, Sect.
IV.2]. DESI reports that compressed CMB gives "almost identical constraints"
to the primary anisotropies in this case [src: same].

### Step 2. Choose the basis
<!-- key: step-2-choose-the-basis -->

1. **Smoothed bins** (DESI DR2):
   `w(z) = w_0 + Σ_{i=1}^{N} [(w_i − w_{i−1})/2] [1 + tanh((z − z_i)/s)]`
   (arXiv:2503.14743, Eq. 13), with `w_i` the bin amplitudes, `z_i` the
   edges and `s = 0.02`, chosen so the amplitude varies by less than 1%
   within `Δz = 0.01` of an edge; no prior correlation between bins [src:
   Sect. V.1]. Equivalent basis form: tanh-smoothed top hats
   `e_j = ½[tanh((z − z_j)/s) − tanh((z − z_{j−1})/s)]` (Eq. 23). Uniform
   bins between `z = 0` and 2.1 are shown; logarithmic, tracer-aligned and
   uneven schemes "do not change qualitatively" [src: Sect. V.1]. The
   reason for tanh rather than top-hat bins, given by the method's
   originators: a stable time derivative of `w`, needed for dark-energy
   perturbations with CMB and LSS data (Crittenden et al. 2012,
   arXiv:1112.1693, Sect. III.2) [src].
2. **Chebyshev series ("crossing statistics")**:
   `y(z) = Σ_{i=0}^{N} C_i T_i(x)`, `x ≡ 1 − 2 (z_max − z)/(z_max − z_min)`
   (arXiv:2405.04216, Eq. 1), with `z_min = 0`, `z_max = 3.5` and four terms
   [src: Sect. 2.1]; `w(z) = −Σ C_i T_i(x)` (Eq. 5) or
   `f_DE(z) = C_0 + Σ_{i≥1} C_i T_i(x)` with `C_0 = 1 − Σ C_i (−1)^i` from
   `f_DE(0) = 1` (Eqs. 6–7). ΛCDM is `C_0 = 1`, `C_{i>0} = 0`. The
   coefficients `C_i` are the "hyper-parameters" of the Bayesian
   interpretation of Shafieloo 2012 (arXiv:1202.4808), in which they
   "perform as discriminators between correct and wrong models" [src:
   abstract].
3. **Gaussian process** (DESI DR2):
   `w(z) ~ GP(m(z) = −1, K)` with the squared-exponential kernel
   `k(x_i, x_j) = sigma_f^2 exp[−(x_i − x_j)^2/(2 l_f^2)]`
   (arXiv:2503.14743, Eqs. 28–29); `sigma_f` is the typical deviation from
   the mean function and `l_f` the correlation length [src: App. C].
   Samples are drawn on a dense grid from `z = 0` to 10.
4. **Bins plus a correlation prior** (Gu et al. 2025): 29 piecewise-constant
   bins uniform in scale factor for `z < 2.5`, plus a fixed wide bin
   `w_wide = −1` from 2.5 to recombination, because freeing it left it
   "largely unconstrained" and almost uncorrelated with the others [src:
   arXiv:2504.06118, Sect. VI.3]. The method's originators found binning
   variable (uniform in `a`, `ln a` or `z`) irrelevant once `N ≥ 20` with
   `a_min = 0.4` [src: arXiv:1112.1693, Sect. III.2].
5. **Principal components of bins** (diagnostic, not a separate fit):
   the binned covariance `C` from the chains is diagonalised,
   `C^{-1} = O^T Λ O` (arXiv:2503.14743, Eq. 24), new amplitudes
   `q_i = Σ_j O_ij w_j` (Eq. 25), new basis `e'_i = Σ_j O_ij e_j` (Eq. 26)
   and errors from the eigenvalues (Eq. 27). The idea that the data, not a
   familiar series, should set the basis, keeping "a few of the
   best-measured modes", is Huterer and Starkman 2003,
   arXiv:astro-ph/0207517 [src: abstract].

### Step 3. Close the function at high redshift
<!-- key: step-3-close-the-function-at-high-redshift -->

Every implementation returns to `w = −1` beyond the data, so that the early
expansion is ΛCDM-like and the CMB acoustic scale keeps its standard
meaning:

- GP: `w(z ≥ z_max) = −1` with `z_max = 10`, checked not to alter the
  conclusions [src: arXiv:2503.14743, Sect. V.2].
- Chebyshev with CMB: beyond `z_max = 3.5`, the transition
  `−1 + (B_0 + B_1 u) exp(−u^2/Δ^2)`, `u = log[(1+z)/(1+z_max)]`, with
  `B_0, B_1` set for continuity and differentiability [src:
  arXiv:2405.04216, Sect. 2.2.1]; `z_max = 2.35` gives similar results
  [src: Sect. 2.1, App. B].
- Correlation-prior bins: `w_wide = −1` above `z = 2.5` [src:
  arXiv:2504.06118, Sect. VI.3].
- DESI bins: the highest bin "effectively extends to high redshifts" [src:
  arXiv:2503.14743, Sect. V.1].

### Step 4. Put priors on the free function
<!-- key: step-4-put-priors-on-the-free-function -->

This is the step that decides the answer; the settings in use:

| Method | Prior | Authors' reason | Place |
|---|---|---|---|
| DESI bins | flat amplitudes, no inter-bin correlation | localised analysis "motivated by the data" | arXiv:2503.14743, Sect. V.1 |
| Chebyshev, `w` | `C_i ~ N(ΛCDM value, sigma = 3)` | unbounded coefficient posteriors when `f_DE` falls steeply at high z (indistinguishable distances) cause prior-volume bias; Gaussian prior "intentionally favouring ΛCDM" | arXiv:2405.04216, Table 1, App. C |
| Chebyshev, `f_DE` | `C_i ~ N(ΛCDM value, sigma = 1)` | same | same |
| GP | `sigma_f = 1` fixed; generalised inverse Gaussian prior on `l_f`, `f(x | p, b) ∝ x^{p−1} exp[−(x + b/x)/2]` (Eq. 30) with `p = 3`, `b = 2` | penalise small `l_f` ("excessive freedom") and large `l_f` (oversampling "nearly linear functions"); `sigma_f = 1` admits a broad range of behaviour | arXiv:2503.14743, App. C |
| GP sampling aid | latent variable `w(z_l)` at `z_l = 0.4` with Gaussian prior of width `sigma_f`, other values drawn conditionally | faster convergence; results "reasonably robust" for `z_l` in [0.2, 1.5] and for `sigma_f ~ U[0, 2]` | same |
| Correlation prior | `chi2 = chi2_data + A chi2_prior`, `chi2_prior = D_w^T C_Pi^{-1} D_w` (Eq. 8), `D_w = (I − S) w`, fiducial `w_fid = S w` = running average of 5 neighbouring bins; `A = 1` | prior "enforces smoothness and mitigates flat directions"; covariance taken from Horndeski simulations | arXiv:2504.06118, Sects. III, VI.3 |

The Horndeski correlation prior of Gu et al. is
`C(a, a') = sqrt[C(a) C(a')] R(a, a')`, with `C(a) = 0.05 + 0.8 a^2` and
`R(a, a') = exp[−(|ln a − ln a'|/0.3)^1.2]` (arXiv:2504.06118, Eqs. 6–7).
It comes from fits to ensembles of viable scalar-field models in Raveri et
al. 2017 (arXiv:1703.05297), whose best fits are [src: Table 1]:

| Class | Variance `C(a)` | Correlation `R` | Fixed-CPZ correlation |
|---|---|---|---|
| Quintessence | `0.03 + 0.3 exp[6.5 (a − 1)]` | `exp[−(|δa|/0.7)^1.8]` | `[1 + (|δa|/0.6)^2]^{-1}` |
| Generalised Brans–Dicke | `0.05 + 0.8 exp[1.8 ln a]` | `exp[−(|δ ln a|/0.3)^1.3]` | `[1 + (|δ ln a|/0.2)^2]^{-1}` |
| Horndeski | `0.05 + 0.8 exp[2 ln a]` | `exp[−(|δ ln a|/0.3)^1.2]` | `[1 + (|δ ln a|/0.2)^2]^{-1}` |

Variance is larger for Horndeski than for quintessence, whose variance is
"clipped by the hard bound of `w_DE ≥ −1`"; both are small at high
redshift [src: arXiv:1703.05297, Sect. IV.2]. The ensemble covariance is
computed without data constraints because even mild constraints
"overwhelm" the theory correlations [src: same].

### Step 5. Handle perturbations
<!-- key: step-5-handle-perturbations -->

- Crossing of −1 with the CMB: PPF as implemented in CLASS, sound speed
  `c_s^2 = 1` [src: arXiv:2405.04216, Sect. 2.2.1].
- GP `w(z)`: a modified CAMB [src: arXiv:2503.14743, Sect. V.2].
- `f_DE < 0`: background only, or compressed CMB (Step 1).
- Gu et al. restrict themselves to background observables because
  modelling perturbations "requires additional assumptions"; their CMB is
  `100 theta_* = 1.04098 ± 0.00042` from Planck PR4 with the error inflated
  by 75% for extended models, plus a BBN prior
  `Omega_b h^2 = 0.02196 ± 0.00063` [src: arXiv:2504.06118, Sect. VI.1].

### Step 6. Sample, then summarise
<!-- key: step-6-sample-then-summarise -->

- Background-only runs sample `{Omega_m,0, C_0..C_3, H0 r_d}`, `H0 r_d`
  being a nuisance; CMB runs sample the six ΛCDM parameters plus the `C_i`;
  supernova magnitudes are marginalised analytically [src:
  arXiv:2405.04216, Sect. 2.4]. Gu et al. vary `Omega_M`, `Omega_b h^2`,
  `H0` and the supernova magnitude `M_b` with `w_i` flat in [−6, 4] [src:
  arXiv:2504.06118, Sect. VI.3].
- Bands: median with 68% and 95% intervals (DESI, Calderon et al.), plotted
  also as `h(z)/h_ΛCDM`, `Om(z) ≡ (h^2 − 1)/[(1+z)^3 − 1]` (equal to
  `Omega_m,0` in ΛCDM) and `q(z)` [src: arXiv:2405.04216, Sect. 3.1, Eqs.
  10–11].
- Fit gain against the number of extra parameters: Δχ² as a function of
  the expansion order (arXiv:2503.14743, Fig. 6; arXiv:2405.04216, App. A).
- Distance from a model: `SNR^2 ≡ (w − w_mod)^T C_w^{-1} (w − w_mod)` with
  `C_w` the posterior covariance of the bins (arXiv:2504.06118, Eq. 1).
- Evidence: PolyChord, and the Gaussian approximation `ln E = ln V + ln L`,
  `ln V = ½ (ln det C_post − ln det C̃_prior)`; because the running average
  gives `C̃_prior` zero eigenvalues, a diagonal `Δ^{-2}` is added, which
  interpolates between ΛCDM (`Δ = 0`) and an unconstrained fiducial and
  sets the effective number of degrees of freedom `N_eff` [src:
  arXiv:2504.06118, Sect. VI.4].

### Step 7. Validate on mocks with known w(z)
<!-- key: step-7-validate-on-mocks-with-known-w-z -->

DESI DR2 used simulated DESI + Pantheon+ + CMB data for a ΛCDM mock and a
`w0 = −0.75`, `wa = −0.85` mock; the truth lies "mostly" within 1σ for three
bins (2σ near bin edges) and within 1σ for the GP; the departure from ΛCDM
is detected at > 2σ in the two lowest bins of the `w0wa` mock. An extreme
thawing mock (algebraic thawing with `w0 = −0.5`, `p = 20`) is not recovered
by either method; tests of kernel choice and hyper-parameter priors are
"left to future work". The same implementation was then applied unchanged
to the data [src: arXiv:2503.14743, App. E]. Gu et al. validated on mocks
for `w = −1`, `w = −1.2`, `w = −1.2 + 0.5(1 − a)` and a cubic in `(1 − a)`,
with the real data covariance [src: arXiv:2504.06118, Suppl. Sect. 4].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Bins, polynomials, GP or correlation prior
<!-- key: bins-polynomials-gp-or-correlation-prior -->

- **Bins without correlation.** Simple and local; suited to testing
  departure from a constant, but more complex behaviour needs more bins
  and larger errors [src: arXiv:2503.14743, Sect. V.1]. A crossing of −1
  "would have to occur at the edge between two adjacent bins", so its
  redshift depends on the number and centres of the bins and is "not ...
  a very robust 'measurement'" [src: same].
- **Chebyshev.** A complete basis; `N ≈ 3` captures smooth functions [src:
  arXiv:2503.14743, Sect. IV.2]. `w(z)` needs two free parameters for the
  best-fit χ² to converge, `f_DE` at least three [src: arXiv:2405.04216,
  App. A]. Higher orders weaken constraints; the order should be "the
  smallest integer compatible with the data" [src: Sect. 2.1, footnote].
- **GP.** A generalisation of binning with a smoothness prior; the mean
  function `m = −1` "places more prior weight on Λ", which DESI presents as
  making departures data-driven [src: arXiv:2503.14743, Sect. V.2]. The
  originators of the correlation prior call a Gaussian prior centred on
  `w = −1` "ad hoc" and unphysical for quintessence, and prefer a prior that
  does not favour `w = −1` over, for example, `w = −0.9` [src:
  arXiv:1112.1693, Sect. IV.3]. The two groups thus read the same choice in
  opposite directions: conservative against a false detection, or biased
  towards Λ.
- **Correlation prior.** Suppresses high-frequency modes and leaves low
  frequencies to the data, stabilises MCMC and removes binning dependence
  when bins are fine compared with the correlation length [src:
  arXiv:1112.1693, Sect. III.2]. "Application of a prior always implies
  some bias", largest for "models which are quickly changing" [src: Sect.
  VII]. A reconstruction "highly sensitive" to the fiducial `w̄_i` "should
  not be trusted" [src: arXiv:1703.05297, Sect. IV.3].

### Fixed or floating fiducial
<!-- key: fixed-or-floating-fiducial -->

Three options exist (arXiv:1112.1693, Sect. IV.3) [src]: a fixed fiducial
(often −1); marginalising a constant fiducial with a weak prior of variance
`sigma_fid^2`, which turns the prior covariance into
`C̃_ij = C_ij + sigma_fid^2 u_i u_j` (Eq. 19) and leaves the mean level to
the data; or a floating fiducial `w_fid = S w`, e.g. the bin average
(Eq. 20) or a running average, which modifies the inverse covariance to
`C̃^{-1} = (I − S)^T C^{-1} (I − S)` (Eq. 21). Gu et al. use the 5-bin
running average [src: arXiv:2504.06118, Sect. VI.3]. The running average
reduces the lowest-frequency eigenvalues of the prior and leaves the
high-frequency ones unchanged [src: arXiv:1112.1693, Fig. 4 caption]; it is
also what makes the Gaussian prior volume ill-defined and forces the `Δ`
regularisation of Step 6 [src: arXiv:2504.06118, Sect. VI.4].

### Shape and strength of the correlation
<!-- key: shape-and-strength-of-the-correlation -->

- Shape: the original CPZ form `xi_w(δa) = xi_w(0)/[1 + (δa/a_c)^2]`
  (arXiv:1112.1693, Eq. 15), whose normalisation can be set by the allowed
  variance of the mean equation of state,
  `sigma_w̄^2 ≃ pi xi(0) a_c/(1 − a_min)` (Eq. 16) [src]. Theory ensembles
  prefer an exponential decay; in Horndeski models the correlation is
  better expressed in `ln a` than in `a` [src: arXiv:1703.05297, Table 1].
- Strength: Gu et al. set `A = 1` for their main result [src:
  arXiv:2504.06118, Sect. VI.3] and scan `Δ`: `ln L` rises and `ln V` falls
  monotonically with `N_eff`; with BAO alone `Δ ln E` stays consistent with
  zero at every `N_eff`; with supernovae it peaks at `N_eff` of 2–3 [src:
  Sect. IV].
- Data-driven choice of `N_eff`: Gu et al. quote the largest SNR among
  reconstructions that still have `Δ ln E ≥ 0`, as the strongest departure
  "without overfitting" [src: Sect. IV].

### Reconstructing w, f_DE or h
<!-- key: reconstructing-w-fde-or-h -->

- `w` and `f_DE` Chebyshev reconstructions agree with each other and with
  CPL for DESI DR2 + compressed CMB with and without Union3 [src:
  arXiv:2503.14743, Sect. IV.2].
- `f_DE` binning shows a turnover in `0.5 < z < 1.0`, with `f_DE > 0` at
  about 2σ in most bins [src: Sect. V.1].
- A GP on `h(z)` avoids priors on `w` but needs a derivative for `w`; Bag et
  al. 2026 propose reading `w_0` from `Om(z)` without extra
  differentiation, and use χ²-limited samples to "mitigate potential
  over-constraining from GP priors" [src: arXiv:2605.27230, abstract].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| tanh smoothing | `s = 0.02` | DESI DR2 bins | arXiv:2503.14743 | Sect. V.1, footnote |
| PCA set-up | 10 uniform bins in 0.1 < z < 2.1 plus one bin on each side (12 amplitudes) | DESI DR2 + CMB + Union3 | arXiv:2503.14743 | Sect. V.1 |
| First PC | error at least 20 times smaller than any other; peaks in 0.1 < z ≤ 0.3; second in 0.3 < z ≤ 0.5 | same | arXiv:2503.14743 | Sect. V.1, Fig. 8 |
| Lowest bin | `w > −1` at more than 3σ; higher bins within 2σ of −1 | DESI + CMB + Union3 | arXiv:2503.14743 | Sect. V.1 |
| Chebyshev range and order | z in [0, 3.5], 4 terms | DESI DR1 | arXiv:2405.04216 | Sect. 2.1 |
| Chebyshev priors | `N(ΛCDM, 3)` for `w`, `N(ΛCDM, 1)` for `f_DE` | DESI DR1 | arXiv:2405.04216 | Table 1 |
| Background-only priors | `Omega_m,0 ~ U[0.01, 0.99]`, `H0 r_d ~ U[3650, 18250]` km/s | DESI DR1 | arXiv:2405.04216 | Table 1 |
| Δχ² against ΛCDM, 4 extra parameters | −5.5 (DESI BAO), −9.1 (+ Union3), −14.6 (+ Union3 + Planck) | DESI DR1, Chebyshev `w` | arXiv:2405.04216 | Sect. 3.1 |
| BAO + SN `Omega_m,0`, `H0 r_d` | 0.339 (+0.022/−0.015), 9808 ± 150 km/s (Union3); 0.328 (+0.026/−0.011), 9891 ± 100 (DES-SN5YR); 0.327 (+0.017/−0.012), 10030 ± 110 (Pantheon+) | DESI DR1, Chebyshev `w` | arXiv:2405.04216 | Table 2 |
| GP settings | `sigma_f = 1`, GIG(`p = 3`, `b = 2`) on `l_f`, `z_l = 0.4`, `z_max = 10` | DESI DR2 | arXiv:2503.14743 | App. C; Sect. V.2 |
| Correlation-prior binning | 29 bins uniform in `a` for z < 2.5; `w_i` flat in [−6, 4]; 5-bin running average; `A = 1` | Gu et al., DESI DR1/DR2 | arXiv:2504.06118 | Sect. VI.3 |
| SNR of `w ≠ −1` | DR2: 2.6 (BAO), 3.7 (+ Pantheon+), 4.3 (+ Union3), 4.5 (+ DESY5); DR1: 2.6, 3.9, 3.9, 4.2 | Gu et al., BAO + BBN + `theta_*` | arXiv:2504.06118 | Sect. III, Eq. 1 |
| Peak `Δ ln E` | 5.2 ± 0.7 at `N_eff = 3` (DR2 + DESY5); 3.3 ± 0.7 (DR2 + Union3); 1.4 ± 0.7 (DR2 + Pantheon+, "weak") | Gu et al. | arXiv:2504.06118 | Sect. IV |
| Max SNR with `Δ ln E ≥ 0` | 4.3 (DR2 + DESY5), 3.9 (+ Union3), 3.1 (+ Pantheon+) | Gu et al. | arXiv:2504.06118 | Sect. IV |
| Minimum bin number for binning independence | `N ≥ 20` with `a_min = 0.4` | method paper | arXiv:1112.1693 | Sect. III.2 |

Two cautions on the Gu et al. rows. Their SNR is a distance in the space of
prior-coupled bins, not a Δχ² converted with a fixed number of degrees of
freedom, so it is not comparable with the DESI σ values of L2; the paper's
abstract summarises the evidence as "≈3σ tension with ΛCDM (and higher for
some data sets)" [src: abstract, v3]. The DESY5 rows use DES-SN5YR before
the Dovekie recalibration, which L2 records as having lowered the
significance (`results.md`, Section 2).

## What goes wrong
<!-- key: what-goes-wrong -->

- **Flat directions and prior volume.** With BAO alone, `Omega_m`, the
  dark-energy evolution and `H0 r_d` are degenerate; peculiar `f_DE` shapes
  compensated by large `Omega_m` fit DESI DR1 with Δχ² ≈ −5.5 for four extra
  parameters [src: arXiv:2405.04216, Sect. 3.1]. Coefficient posteriors are
  unbounded where `f_DE` vanishes at high z [src: App. C]. Test: add
  supernovae or a CMB anchor before reading the shape; report the prior on
  the coefficients.
- **Methods cannot follow fast transitions.** The DESI extreme-thawing mock
  is not recovered by binning or GP [src: arXiv:2503.14743, App. E]; the
  correlation prior biases most strongly models that change quickly [src:
  arXiv:1112.1693, Sect. VII]. Test: mocks spanning the model classes of
  interest, including one with a late, rapid change.
- **Crossing redshift read off a reconstruction.** It depends on bin edges
  [src: arXiv:2503.14743, Sect. V.1] and differs between parameterisations
  (Chebyshev `z_c ≃ 0.5`, higher than CPL; "not statistically significant")
  [src: Sect. IV.2]. Test: vary the bin edges; quote the crossing only as a
  range.
- **Oscillations in w(z).** Gu et al. find `w > −1` at `z ≲ 0.2`, `w < −1`
  near `z ~ 0.75`, and oscillations once supernovae are added, stable from
  DR1 to DR2 and across supernova samples, which they interpret as "a robust
  physical signal" [src: arXiv:2504.06118, Sect. III]. Against reading too
  much into it: the second and third principal components, which carry the
  oscillation, become constrained only with supernovae, and are oscillatory
  at low redshift [src: same]; the prior is designed to suppress
  high-frequency modes and its strength sets `N_eff` (above); DESI's own
  reconstructions find that more freedom "does not significantly improve the
  fit" and that the data favour a smooth evolution well described by CPL
  [src: arXiv:2503.14743, Sect. IV.2]. Test: `Δ ln E` against `N_eff`; the
  supernova-sample split; a mock with smooth truth to see how often
  oscillations appear.
- **PCA over-interpreted.** Eigenvectors of the inverse covariance are
  "formally not well-defined", depend on the binning and on the variable,
  and their errors have no a priori scale [src: arXiv:2503.14743, App. B].
- **Evidence in non-Gaussian cases.** The Gaussian evidence formula departs
  from PolyChord for BAO alone, where the posterior is not Gaussian [src:
  arXiv:2504.06118, Sect. IV]. Test: compute both.
- **Supernova sample dependence.** BAO + Pantheon+ gives "weak" evidence in
  the reconstruction as in CPL; Gu et al. suggest a mild tension between the
  Pantheon+ distance scale and BAO, not yet attributed [src:
  arXiv:2504.06118, Sect. IV]. The sample-dependence discussion of L2
  (`open-questions.md#supernova-sample-dependence`) applies unchanged.
- **Agreement with CPL taken as independent confirmation.** All methods use
  the same BAO, CMB and supernova data; agreement shows that the result is
  not a CPL artefact, not that it is free of data systematics. The DESI
  paper's claim is the first, "the trend is not driven by the choice of
  parametrization" [src: arXiv:2503.14743, Fig. 5 caption].

## Reading list
<!-- key: reading-list -->

- Foundation: Huterer and Starkman 2003, arXiv:astro-ph/0207517 —
  principal components of `w(z)` as a data-chosen basis.
- Foundation/method: Crittenden et al. 2012, arXiv:1112.1693 — correlation
  prior, fiducial marginalisation and running average (Eqs. 15–21), bias.
- Method: Raveri et al. 2017, arXiv:1703.05297 — theory-based prior
  covariances for quintessence, Brans–Dicke and Horndeski (Table 1).
- Method: Shafieloo 2012, arXiv:1202.4808 — Bayesian crossing statistic and
  its hyper-parameters.
- Application: Calderon et al. 2024, arXiv:2405.04216 — Chebyshev `w` and
  `f_DE` with DESI DR1; priors and order (Table 1, Apps. A, C).
- Application: Lodha et al. 2025, arXiv:2503.14743 — DESI DR2 binning, PCA,
  GP settings and mock validation (Sect. V, Apps. B, C, E).
- Application: Gu et al. 2025, arXiv:2504.06118 — Horndeski correlation
  prior, SNR, evidence against `N_eff` (Sects. III, IV, VI).
- Critique/alternative: Bag et al. 2026, arXiv:2605.27230 — why
  differentiating `h(z)` is noisy; GP-prior over-constraining.
- Critique: Keeley et al. 2025, arXiv:2506.15091 — mock rate of spurious
  crossings (in L2).

## Not verified
<!-- key: not-verified -->

- The Gu et al. body was read in its HTML rendering; the arXiv abstract is
  v3 and does not print the SNR or `Δ ln E` values, so the version behind
  the body numbers was not established.
- The original CPZ paper (Crittenden, Pogosian and Zhao, cited as [17] in
  arXiv:1112.1693), the GP papers of Holsclaw et al. and Shafieloo et al.,
  and earlier correlation-prior applications (e.g. a 2017 reconstruction by
  Zhao et al.): cited in the papers read, not read here; no identifier
  recorded.
- Gu et al. supplementary tables (CPL constraints per data set) and the
  covariant PCA of their supplement.
- The binned `w(z)` of the DESI DR2 key paper (its Fig. 12, three uniform
  bins), referred to in arXiv:2503.14743, Sect. V.1, but not read in
  arXiv:2503.14738 itself.
