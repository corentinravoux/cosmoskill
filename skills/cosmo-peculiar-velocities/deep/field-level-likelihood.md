# Field-level likelihood — cosmo-peculiar-velocities dossier

Scope: how a "maximum-likelihood fields" growth-rate fit is assembled — data vector, gridding,
the terms added to the model covariance (gridding window, shot noise, η errors, σ_v, the extra
density integral), the free and fixed parameters, the numerics — and how to choose between
gridded and per-object data, covariance models, mesh settings and error calibrations.
Snapshot: 2026-10-22.
From: Turner 2024 review (arXiv:2411.19484), Sect. 5.4; DESI DR1 PV maximum-likelihood-fields
paper (arXiv:2512.03229); DESI DR1 consensus paper (arXiv:2512.03230), Sect. 1.

Who does it. The DESI DR1 consensus paper lists as maximum-likelihood analyses "that analytically
model the covariance between the velocity and galaxy density fields" Johnson et al. 2014,
Huterer et al. 2017, Adams & Blake 2020 and Lai et al. 2023 [src: arXiv:2512.03230, Sect. 1].
Four lines of implementation are read here: the 6dFGS line (Johnson et al. 2014, arXiv:1404.3799;
Adams & Blake 2017 and 2020, arXiv:1706.05205, arXiv:2004.06399); the SDSS PV and DESI DR1 line
(Lai et al. 2023, arXiv:2209.04166; Lai et al. 2025, arXiv:2512.03229); per-object SN and
galaxy covariances without a grid (Huterer et al. 2017, arXiv:1611.09862; the flip code, Ravoux
et al. 2025, arXiv:2501.16852, and its DESI BGS × ZTF simulation study, arXiv:2609.34508); and
Bayesian reconstructions that sample the field itself rather than marginalising it (VIRBIuS,
BORG-PV, HAMLET, the Cosmicflows-4 fields; last choice below). Turner 2024 notes that the method
"has seen more uptake in supernova cosmology groups, thanks in part to the software package
flip", and calls Adams & Blake 2020 "one of the more prominent examples" [src: arXiv:2411.19484,
Sect. 6.1].

Field-level inference as a general method (samplers, forward models, gains
over compressed statistics) is in `cosmo-beyond-two-point/deep/field-level-inference.md`;
this dossier covers the Gaussian velocity-field likelihood only.

Already in L2, not repeated here: the principle, the flip decomposition and the closed-form
C_vv, the table of covariance models (AB17, AB20, C23, L22, RC25) and the zero-point
marginalisation (eq. 32 of arXiv:2512.03229) in
`physics-and-methods.md#field-level-likelihood-maximum-likelihood-fields`; the DESI DR1 priors,
σ_u slope, ×1.64 inflation, TF/FP split and density-cell cut in
`systematics.md#desi-dr1-maximum-likelihood-fields-lai-et-al`; the SDSS PV field-level budget in
`systematics.md#sdss-pv-growth-rate-field-level-lai-et-al-2023`; the 6dFGSv budget in
`systematics.md#6dfgsv-field-level-fits-johnson-et-al-2014`; σ_u values in
`systematics.md#non-linear-velocities-and-the-damping-model`.

Notation: S is the data vector, C its model covariance; η the log-distance ratio; κ(z) the
factor turning a velocity into η; Γ(k) the angle-averaged Fourier transform of the gridding
kernel; σ_g (h⁻¹Mpc) the finger-of-God damping of the density; σ_u (h⁻¹Mpc) the sinc damping of
the velocity; σ_v (km/s) an additive non-linear velocity dispersion; b_add an amplitude for
density power above k_max. Equations are numbered as in the paper cited beside them.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Build the data vector
<!-- key: step-1-build-the-data-vector -->

- **Density per cell.** DESI DR1: δ_g^grid = (w − α w_r)/(α w_r), w = Σ w_i^comp w_i^FKP over the
  galaxies of the cell, w_i^FKP = 1/(1 + n̄_g P_0) with P_0 = 1 600 h⁻³Mpc³, α the ratio of
  weighted data to random counts (arXiv:2512.03229, Eqs. 16–19) [src: Sect. 3.2.2]. SDSS PV used
  unweighted counts against randoms (arXiv:2209.04166, Eq. 27) [src: Sect. 4.1.2]; flip, counts
  over expected counts with an NGP, CIC, TSC or PCS assignment [src: arXiv:2501.16852, Sect. 3.2].
- **η per cell.** The unweighted mean η^grid = (1/N) Σ η_i, with error
  σ_η = (1/N) sqrt(Σ σ²_η,i) (arXiv:2512.03229, Eqs. 20–21) [src]. The authors give their reason
  for applying no completeness weight: "the missing galaxies may not have the same log-distance
  ratio as the observed galaxies", and individual η are noise-dominated, so duplicating them "may
  not be appropriate"; an FKP-like weight (momentum FKP × κ²) and inverse-variance weights were
  both tried on mocks with "negligible" or "little" impact [src: Sect. 3.2.2, footnotes 5–6].
  The 6dFGSv analysis averaged magnitude fluctuations δm in cells in the same way, with the
  error σ_δm,i = N_i^{-3/2} Σ σ_j (arXiv:1404.3799, Eq. 28) [src: Sect. 3.5]. Adams & Blake 2020
  use η rather than v because 6dFGS velocities have log-normal errors, while η "does have a
  Gaussian distribution" [src: arXiv:2004.06399, Sect. 3.3.1].
- **Per-object data, no grid.** Huterer et al. 2017 keep one entry per SN or galaxy: SN
  residuals Gaussian in the magnification μ = −2[10^{Δm/5} − 1] (Eqs. 9–10), because at z < 0.01
  the signal is Gaussian in μ but not in magnitude; galaxies (~27 % distance errors) Gaussian
  in log-distance [src: arXiv:1611.09862, Sect. 3.2]. flip keeps one velocity per SN,
  v_i = −(c ln10/5) J(p_i) Δμ_i, with the Tripp parameters fitted with fσ8 (arXiv:2501.16852,
  Eqs. 34–36) [src: Sect. 3.2]; its BGS × ZTF study meshes only the density [src:
  arXiv:2609.34508, Sect. 3].
- **Cuts.** DESI DR1 removes cells with δ_g > 10 and η beyond 4σ [src: arXiv:2512.03229, Sect.
  4.4.2]; SDSS PV removed δ_g > 20, because high-δ_g cells drove the worst reduced χ² of the
  galaxy block and the quasi-linear model "breaks down when δ_g ≫ 1" [src: arXiv:2209.04166,
  Sect. 5.4].

The DESI DR1 vector is S = (δ_g^grid, η^grid) (arXiv:2512.03229, Eq. 31) [src: Sect. 3.2.5].

### Step 2. Model the field covariance
<!-- key: step-2-model-the-field-covariance -->

DESI DR1 writes C_gg, C_gv, C_vv as sums over spherical-harmonic weighting functions H^l_{p,q}
(Eq. 6) and Hankel-type integrals ξ^{p,q,n}_{ab,l}(r, σ_u) = ∫_{k_min}^{k_max} k²dk/(2π²) P_ab(k)
j_l(kr) k^{2(p+q)} D_u^n(k, σ_u) (Eq. 4), with the Gaussian finger-of-God D_g expanded in μ²
(Eq. 3) and D_u = sin(kσ_u)/(kσ_u) (Eq. 5) [src: arXiv:2512.03229, Sect. 3.1]. Settings and
their stated reasons [src: same]:

- k_max = 0.20 h Mpc⁻¹, "where our quasi-linear model breaks down"; k_min = 0.0002 h Mpc⁻¹
  "since the DESI DR1 data may be affected by modes larger than the survey volume".
- Power spectra from standard perturbation theory instead of the RPT of the SDSS PV analysis,
  to match the two companion DESI papers; App. A shows fσ8 is unaffected.
- p_max = q_max = 3 in the D_g expansion, "equivalent to using a third-order Taylor expansion",
  enough because kσ_g ≲ 1. The flip paper describes the same L22 model as "calculated to the
  p = 4 order" [src: arXiv:2501.16852, Sect. 3.1]; the two statements are as printed.
- C_vv has only l = 0 and 2 terms, because the highest combined power of μ1, μ2 is 2 (Eq. 10).
- The Lai et al. (L22) pipeline was kept rather than flip's RC25 because varying σ_g in RC25
  needs pre-computed covariances on a σ_g grid, "computationally expensive", and the two give
  consistent covariances at k_max = 0.20.

Other choices of the same step:

- **Huterer et al. 2017**: C = A S + N, with A the amplitude of the signal covariance (A = 1 the
  fiducial ΛCDM, A = 0 noise only) (Eq. 3); S from the halofit non-linear P(k), "important"
  because the nearest objects (z ≲ 0.01) weigh most; a Legendre sum to ℓ_max = 20, or 200 for
  nearly aligned pairs (cos θ > 0.95); cosmology fixed near Planck, so the result depends on
  cosmology mainly through fσ8 and the shape of P(k) [src: arXiv:1611.09862, Sect. 3.1].
- **Adams & Blake 2020**: RSD in the density and cross terms (the AB20 model of L2), and a
  scaling α_b of the bias in the cross-covariance only (b → α_b b, Eqs. 34–36), because the
  velocity sample lies at lower redshift than the density sample of a magnitude-limited survey
  [src: arXiv:2004.06399, Sect. 3.3.4].
- **flip, RC25**: full exponential FoG with D_u (arXiv:2609.34508, Eq. 16) and input spectra
  in the Bel et al. (2019) form (Eq. 17) [src: Sect. 3].

### Step 3. Convert velocities to η
<!-- key: step-3-convert-velocities-to-eta -->

C_ηη = κ(z1)κ(z2) C_vv, C_ηg = κ(z1) C_vg, C_gη = κ(z2) C_gv, with
κ(z) = (1 + z)/[ln10 D(z) H(z)] (arXiv:2512.03229, Eqs. 12–15) [src: Sect. 3.2.1]; Adams &
Blake write the same factor ξ(z_obs) (arXiv:2004.06399, Eqs. 20–24), following Johnson et al.,
Adams & Blake 2017 and Hui & Greene 2006 [src: Sect. 3.3.1]. Huterer et al. convert to magnitude
residuals instead, S_ij = [5/ln10]² (1 + z_i)²/(H d_L)_i (1 + z_j)²/(H d_L)_j ξ_ij (Eq. 4) [src:
arXiv:1611.09862, Sect. 3.1]; flip fits velocities with a per-object error propagated from σ_η
or σ_Δμ [src: arXiv:2501.16852, Sect. 3.2].

### Step 4. Correct the model for the grid
<!-- key: step-4-correct-the-model-for-the-grid -->

- **Window.** P_XY → P_XY Γ(k)² (arXiv:2512.03229, Eq. 22), with
  Γ(k) = (1/4π) ∫∫ sinθ dφ dθ sin k_x sin k_y sin k_z/(k_x k_y k_z), k_{x,y,z} = (kL/2)(…) (Eqs.
  23–24) [src: Sect. 3.2.2]. With different grids per field, one Γ per field enters the cross
  term, Γ_δg Γ_vp (Adams & Blake 2017, arXiv:1706.05205, Eqs. 31–35) [src: Sect. 3.7]. For an
  assignment of order n (1 NGP to 4 PCS) flip raises the kernel to the n-th power, on the meshed
  field only (arXiv:2609.34508, Eq. 18) [src: Sect. 3].
- **Variance of a cell mean of N objects** (Abate et al. 2008, as adopted):
  C_ηη^grid → C_ηη^grid + (C_ηη − C_ηη^grid)/N on the diagonal (arXiv:2512.03229, Eq. 25;
  arXiv:1706.05205, Eq. 36); off-diagonal terms are left, being "negligible on small scales"
  [src].
- **Degeneracy with σ_u.** The 20 h⁻¹Mpc grid kernel "is similar to applying the RSD damping
  with σ_u = 10 h⁻¹Mpc", 30 h⁻¹Mpc to σ_u = 15; a gridded analysis's σ_u is therefore not
  comparable to an ungridded one [src: arXiv:2512.03229, Sect. 3.2.2, Fig. 4 caption].

### Step 5. Add the observational and nuisance terms
<!-- key: step-5-add-the-observational-and-nuisance-terms -->

[src: arXiv:2512.03229, Sects. 3.2.3–3.2.4]

    C_gg^err = C_gg^grid + σ²_δg δ_D,     σ_δg = 1/sqrt(N_g^r(x))      (Eqs. 26–27)
    C_ηη^err = C_ηη^grid + σ²_η δ_D,
    σ²_η = (σ_η^grid)² + κ(z1)κ(z2) σ_v²                               (Eq. 28)
    C_gg^add = Σ_pq … b_add² ξ_mm (k from k_max to 1.0 h Mpc⁻¹)          (Eq. 29)

Eq. 26 is printed with N_g^r, the random count of the cell. The total is
C = [[C_gg^err + C_gg^add, C_gη^grid], [C_ηg^grid, C_ηη^err]] (Eq. 30). The extra integral comes
from Adams & Blake 2017: the density auto-covariance had "a significant contribution" above
0.15 h Mpc⁻¹, so a second integral to k_add = 1.0 h Mpc⁻¹, where Γ² is close to zero, raises
the covariance "without needing to provide an advanced model of the bias on non-linear scales"
(Eq. 37) [src: arXiv:1706.05205, Sect. 3.8]. In 6dFGS simulations b_add = 0 was disfavoured by
Δχ² = 241.27; b_add was then fixed, not left free, so as not to bring non-linear information in
[src: Sect. 4.2]. DESI DR1 and SDSS PV leave b_add σ8 free in [0, 10] (`systematics.md`).

Per-object analyses put the stochastic terms on the diagonal. Huterer et al.: N holds
measurement error, intrinsic scatter and correlated systematics, and the fit adds
N → N + Δσ²_int I and Δm_i → Δm_i + ΔM, both with flat priors, because the published residuals
fixed these nuisances before the signal covariance was modelled (Eqs. 11–12) [src:
arXiv:1611.09862, Sect. 3.2]. Johnson et al., in magnitudes: σ_i² = σ²_obs + (5/ln10)²
(1 − (1 + z)²/(H d_L))² σ_v² (arXiv:1404.3799, Eq. 19), σ_obs not fitted, being degenerate with
σ_v [src: Sect. 3.2.2]. flip: σ_v per object, and σ_M through Δμ [src: arXiv:2609.34508, Sect.
4.2].

### Step 6. Evaluate and sample the likelihood
<!-- key: step-6-evaluate-and-sample-the-likelihood -->

The likelihood is Gaussian in S with C, plus the analytic zero-point marginalisation (L2). For
DESI DR1 [src: arXiv:2512.03229, Sect. 3.4]:

- The SDSS PV analysis approximated the log-likelihood by a second-order Taylor expansion around
  50 points in fσ8, with nuisances at their best fit: more than ten times faster, with posterior
  shifts "much less than the uncertainty". DESI DR1 dropped it because a ~5 % forecast error
  "could potentially introduce significant systematics".
- JAX with Cholesky decomposition: about 1 s per evaluation for an ~11 000 × 11 000 matrix;
  adaptive Metropolis–Hastings in NumPyro; convergence at |R − 1| ≤ 0.01, ~40 000 iterations,
  within a day; 140 GB of memory at 20 h⁻¹Mpc [src: Sects. 3.4, 4.4.2 footnote 13].
- Only σ_u requires recomputing the covariance; every other parameter rescales a pre-computed
  block, so σ_u is fixed and its effect taken as a finite-difference systematic (Eq. 33) [src:
  Sect. 4.1].

The other implementations:

- **Adams & Blake 2020**: emcee, 500 walkers × 800 steps, the first 150 discarded, R̂ − 1 < 0.05;
  C⁻¹Δ by a LAPACK Cholesky solve; σ_g and σ_u fixed and varied by hand, since they sit inside the
  k-integral and varying them "would involve a recalculation of the entire covariance matrix"
  [src: arXiv:2004.06399, Sect. 3.4.3].
- **Huterer et al. 2017**: the per-object S for O(10⁴) objects is O(10⁸) evaluations, "about 12
  hours on a modern 24-core desktop computer" once growth, P(k) and Bessel functions are
  tabulated; it is computed once and scaled by A [src: arXiv:1611.09862, Sect. 3.1].
- **flip**: covariance terms pre-computed per parameter coefficient and interpolated over σ_g
  (density) or σ_u (combined fits), minimised with iminuit (MIGRAD, MINOS) [src:
  arXiv:2609.34508, Sects. 4.1, 4.3].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Gridded or per-object data
<!-- key: gridded-or-per-object-data -->

- Gridding cuts the dimension (a ~500 000 × 500 000 brute-force matrix for DR1) and "helps
  smooth out the nonlinearity", making the Gaussian likelihood more appropriate [src:
  arXiv:2512.03229, Sect. 3.2.2].
- Its cost is sample variance missing from the model. On 675 mocks the mean Hessian error
  (0.036) is below the scatter of best fits (0.066 before the data cuts, 0.059 after), with
  reduced χ² ≈ 1; the authors' reasons: the grid "will remove all small-scale information below
  20 h⁻¹Mpc, but the true sample variance includes fluctuations on all scales", the k-integral
  stops at k_max, and σ_u varies between mocks but is fixed [src: Sect. 4.4.2, Table 1]. The
  data error is rescaled by 0.059/0.036 following Sugiyama et al. 2023 [src].
- A 30 h⁻¹Mpc grid gives mean fσ8 0.491 against 0.460 at 20, with 9.2 % against 7.8 % mean error
  [src: Table 1]. A smaller grid was not run: slower MCMC and more memory [src: footnote 13].
- Per-object fits avoid the grid window but pay in matrix size and in the non-linear part of the
  model: Huterer et al. use the halofit P(k) for their nearest objects (Step 2). flip's N-body
  validation integrates to k_max = 100 h Mpc⁻¹ "to avoid aliasing in the integration without the
  grid window function" [src: arXiv:2501.16852, Sect. 4.4]; in its BGS × ZTF tests k_max = 0.2
  biases fσ8 for dense SN samples (6 000 within 150 h⁻¹Mpc) and 1.0, adopted, does not [src:
  arXiv:2609.34508, Sect. 4.2].

### Mesh settings of the density field
<!-- key: mesh-settings-of-the-density-field -->

One study varies them, on 27 BGS mocks and 192 configurations around 30 h⁻¹Mpc voxels, a
150 h⁻¹Mpc spherical mesh, NGP, k_max = 1.0: meshes beyond 250 h⁻¹Mpc bias fσ8 through σ_g, which
absorbs BAO-peak smoothing (fixing σ_g from a small volume removes it); 10 h⁻¹Mpc voxels bias
fσ8, the linear model being "inaccurate at such small scales"; the footprint cut moves bσ8, not fσ8. In the combined fit σ_g is fixed to 6.0 h⁻¹Mpc (a joint
(σ_g, σ_u) interpolation needs "a very large number of covariance matrices"; flagged as a
possible bias); L = 30, R = 300 h⁻¹Mpc gives a 1.8 % mean bias and σ(fσ8) = +0.047/−0.048, a
**forecast** on simulations, and L = 20 with large R a ~1σ bias [src: arXiv:2609.34508, Sects.
4.1, 4.3]. The data analyses fix one grid and test one variant: 20 and 30 h⁻¹Mpc (DESI DR1,
above); 10 h⁻¹Mpc for P(k) fits and 20 for (Ω_m, σ8) in 6dFGSv (Numbers).

### Taylor-expanded or exact finger-of-God
<!-- key: taylor-expanded-or-exact-finger-of-god -->

L22 keeps σ_g as a linear parameter at the price of the kμσ_g ≪ 1 assumption; RC25 removes the
expansion, extending the model to k > 0.1 h Mpc⁻¹, but must interpolate σ_g [src:
arXiv:2501.16852, Sect. 3.1]. DESI DR1 chose L22 for cost, with consistent covariances at
k_max = 0.20 (Step 2); Adams & Blake 2020 keep the damping functions and fix σ_g (Step 6).

### Velocity only or density + velocity
<!-- key: velocity-only-or-density-velocity -->

- 6dFGS: the complete covariance reduces the statistical fσ8 error by 64 % against the RSD
  auto-covariance alone and by 50 % against the velocity auto-covariance alone [src:
  arXiv:2004.06399, abstract]; the cross-covariance is seen in the data, non-zero to ~50
  h⁻¹Mpc (arXiv:1706.05205, Sect. 5.3, Eqs. 44–45) [src].
- DESI DR1: after error inflation the combined fit has an error similar to velocity only; the
  authors still prefer it because velocity-only fσ8 "is very degenerate with σ_u", while the
  galaxy block does not depend on σ_u [src: arXiv:2512.03229, Sect. 4.4.2]. The best σ_u differs
  between the two (16 against 10 h⁻¹Mpc) "because the cross-covariance also depends on σ_u"
  [src: same].
- Velocity only by design: Huterer et al. 2017 (SNe and 6dFGS FP, A = 1.05 +0.25/−0.21) [src:
  arXiv:1611.09862, abstract].
- BGS × ZTF simulations: the density reduces the fσ8 error by up to 50 % without bias for
  30 h⁻¹Mpc voxels, and narrows σ_u [src: arXiv:2609.34508, Sect. 4.3].
- Fisher forecasts: velocities improve the growth constraint "by about a factor of two compared
  to density alone" if all k < 0.2 h Mpc⁻¹ is used (Koda et al. 2014) [src: arXiv:1312.1022,
  abstract].

### σ_u fixed, sampled with a prior, or interpolated
<!-- key: sigmau-fixed-sampled-with-a-prior-or -->

Fixed: DESI DR1 (cost, memory) and Adams & Blake 2020 (inside the k-integral) (Step 6).
With a prior: the BGS × ZTF study puts N(21.5, 10) h⁻¹Mpc to "stabilize the fit" along the
σ_u–fσ8 degeneracy, wide "to avoid dependence on a specific set of simulations"; 21.5 was
measured on AbacusSummit at z = 0.2 and exceeds the OuterRim value of Carreres et al. [src:
arXiv:2609.34508, Sect. 4.2]. Interpolated: flip's grid of covariances (Step 6).

### Combining surveys
<!-- key: combining-surveys -->

Johnson et al. combine 6dFGSv and SNe with a hyper-parameter matrix, C^{DiDj} → (α_i α_j)^{-1/2}
C^{DiDj} (arXiv:1404.3799, Eqs. 41–42), and fix σ_v at the single-survey values because it is
degenerate with the hyper-parameters [src: Sect. 3.7]. Huterer et al. combine Supercal SNe with
6dFGS FP galaxies, each with its own likelihood form (Step 1), for A = 1.05 +0.25/−0.21; the
precision of the test "increases slightly" [src: arXiv:1611.09862, abstract, Sect. 3.2]. In
Fisher forecasts, adding 2MTF (~2 000 galaxies) to 6dFGS improves fσ8 by ~20 % (Howlett et al.
2017) [src: arXiv:1609.08247, abstract].

### Analytic Fisher or full likelihood
<!-- key: analytic-fisher-or-full-likelihood -->

The Fisher matrix of correlated density and velocity fields is the method's forecast tool: Koda
et al. 2014, and Howlett et al. 2017 for combined surveys [src: arXiv:1312.1022;
arXiv:1609.08247, abstracts]. Evaluated at the real positions, F_ij = ½ Tr[A_i A_j],
A_i = C⁻¹C_,i (arXiv:2501.16852, Eq. 52), it is on average 30 % closer to the likelihood errors
than a volume Fisher (Eqs. 50–51) on 27 ZTF realisations, from geometry and nuisance parameters
[src: Sect. 5].

### Analytic covariance or sampled field
<!-- key: analytic-covariance-or-sampled-field -->

The Gaussian likelihood above marginalises the field analytically. Bayesian reconstructions
sample it instead, with the true distances, and are the forward-modelled peers of the method;
only some of them estimate growth:

- VIRBIuS (Lavaux 2016) reconstructs the velocity field, true distances and "some cosmological
  parameters" [src: arXiv:1512.04534, abstract]; Prideaux-Ghee et al. describe these as "the
  Hubble constant and power spectrum amplitude" [src: arXiv:2204.00023, Sect. 1].
- BORG-PV (Prideaux-Ghee et al. 2022) infers the initial conditions from velocity tracers with a
  gravity model and HMC, with cosmology fixed (Eisenstein–Hu prior, Planck 2018 parameters): no
  growth estimate [src: arXiv:2204.00023, abstract, Sects. 2.2.2, 3]. Boruah et al. 2022 forward-
  model the field from velocities alone with an analytic line-of-sight Malmquist correction [src:
  arXiv:2111.15535, abstract].
- HAMLET (Valade et al. 2022) samples the linear density and velocity fields by HMC on GPUs, "two
  to four orders of magnitude" faster in CPU time than earlier Gibbs sampling of Cosmicflows-3
  [src: arXiv:2203.02369, abstract]. The hierarchical model of Graziani et al. 2019 fits CF3
  distances and the linear density field together [src: arXiv:1901.01818, abstract].
- Cosmicflows-4 (Courtois et al. 2023) samples distances, the density field, the growth rate,
  σ_NL and a zero point h_eff by HMC, as the Velocity Field Olympics describes it [src:
  arXiv:2502.00121, Sect. 2.1.5]; the paper's abstract gives fσ8 = 0.38 ± 0.04 (ungrouped),
  0.36 ± 0.05 (grouped), 0.30 ± 0.06 (SNe) "using the pairwise correlation of radial peculiar
  velocities" [src: arXiv:2211.16390, abstract].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Grid | 20 h⁻¹Mpc (30 as variant) | DESI DR1 | arXiv:2512.03229 | Sect. 3.2.2, Table 1 |
| Grid used in 6dFGSv tests | 10 h⁻¹Mpc for P(k) fits, 20 for (Ω_m, σ8) | 6dFGSv | arXiv:1404.3799 | Sect. 4 |
| k range of the field model | 0.0002–0.20 h Mpc⁻¹ | DESI DR1 | arXiv:2512.03229 | Sect. 3.1 |
| k range, 6dFGS | 0.0025–0.15; extra density integral to 1.0 | 6dFGS | arXiv:1706.05205 | Sect. 3.8 |
| k_max, 6dFGSv (Ω_m, σ8) | 0.15 h Mpc⁻¹ | 6dFGSv | arXiv:1404.3799 | Sect. 4 |
| FKP P_0 for the density cells | 1 600 h⁻³Mpc³ | DESI DR1 | arXiv:2512.03229 | Sect. 3.2.2 |
| Grid ↔ σ_u equivalence | 20 → σ_u ≈ 10; 30 → ≈ 15 h⁻¹Mpc | DESI DR1 | arXiv:2512.03229 | Fig. 4 caption |
| Density-cell cut | δ_g > 10 (DESI), δ_g > 20 (SDSS PV) | — | arXiv:2512.03229; arXiv:2209.04166 | Sect. 4.4.2; Sect. 5.4 |
| Mock error vs scatter | 0.036 vs 0.066 (0.059 after cuts) | DESI DR1, 675 mocks | arXiv:2512.03229 | Table 1 |
| Mock error vs scatter | 0.062 vs 0.068 (σ_u = 22, k_max = 0.15) | SDSS PV mocks | arXiv:2209.04166 | Sect. 5.4 |
| Likelihood cost | ~1 s for 11 000², 140 GB | DESI DR1 | arXiv:2512.03229 | Sects. 3.4, 4.4.2 |
| Taylor-likelihood speed-up | > 10× | SDSS PV | arXiv:2512.03229 | Sect. 3.4 |
| Per-object covariance cost | O(10⁸) entries, ~12 h on 24 cores | Supercal + 6dFGS | arXiv:1611.09862 | Sect. 3.1 |
| Signal amplitude, fσ8 | A = 1.05 +0.25/−0.21; fσ8 = 0.428 +0.048/−0.045 at z_eff = 0.02 | Supercal + 6dFGS FP | arXiv:1611.09862 | abstract |
| fσ8, β | 0.384 ± 0.052 (stat) ± 0.061 (sys); β = 0.289 +0.044/−0.043 ± 0.049 | 6dFGS density + velocity | arXiv:2004.06399 | abstract |
| Gain of the complete covariance | −64 % vs RSD only, −50 % vs PV only (stat error) | 6dFGS | arXiv:2004.06399 | abstract |
| Sampler | emcee 500 × 800, burn-in 150, R̂ − 1 < 0.05 | 6dFGS | arXiv:2004.06399 | Sect. 3.4.3 |
| b_add from 6dFGS sims | b_add σ8 = 1.306, b_fit σ8 = 1.29; b_add = 0 at Δχ² = 241.27 | GiggleZ | arXiv:1706.05205 | Sect. 4.2 |
| Velocity gain over density, **forecast** | factor ~2 for k < 0.2 h Mpc⁻¹ | Fisher | arXiv:1312.1022 | abstract |
| σ_u prior | N(21.5, 10) h⁻¹Mpc | BGS × ZTF sims | arXiv:2609.34508 | Sect. 4.2 |
| σ_g fixed | 6.0 h⁻¹Mpc | BGS × ZTF sims | same | Sect. 4.3 |
| SN z_max | 0.07 | ZTF sims | same | Sect. 4.2 |
| Fisher vs volume Fisher | 30 % closer to likelihood errors | ZTF sims | arXiv:2501.16852 | Sect. 5 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Error bar from the Hessian alone.** Shows as mock scatter above the mean error with
  reduced χ² near 1; test on the full mock set and report the ratio (0.059/0.036 in DESI DR1)
  [src: arXiv:2512.03229, Sect. 4.4.2].
- **Gridding kernel coded without its Jacobian.** The DESI DR1 paper notes a typo in earlier
  papers (Howlett et al. 2017b, Lai et al. 2022) where Γ(k) misses sin θ [src:
  arXiv:2512.03229, footnote 7]; the SDSS PV text also prints k_z = (kL/2) cos φ (arXiv:2209.04166,
  Eq. 30) where DESI writes cos θ (Eq. 24). Test: Γ(k) → 1 as k → 0 and its integral against a
  numerical cell average.
- **σ_u compared across analyses with different grids.** The kernel absorbs part of the damping
  [src: arXiv:2512.03229, Fig. 4 caption].
- **High-density cells.** Inflate χ² of the density block; test: χ² of gg alone, then a δ_g cut
  [src: arXiv:2209.04166, Sect. 5.4].
- **Nuisances frozen at their pre-fit values.** Intrinsic scatter and zero point fitted before
  the signal covariance was modelled can shift once it is; Huterer et al. marginalise both
  [src: arXiv:1611.09862, Sect. 3.2].
- **Gaussian in the wrong variable.** At z < 0.01 a SN signal Gaussian in μ is not Gaussian in
  magnitude [src: arXiv:1611.09862, Sect. 3.2]; 6dFGS velocities are log-normal, η is Gaussian
  [src: arXiv:2004.06399, Sect. 3.3.1].
- **Per-object and mesh settings (simulations).** k_max too low for dense per-object samples,
  σ_g absorbing BAO smoothing in large meshes, and SN selection beyond z ≈ 0.07 each bias fσ8;
  tests: vary k_max at fixed volume, fix σ_g from a small volume, cut in z [src:
  arXiv:2609.34508, Sects. 4.1–4.2].
- **Indicator split.** TF-only fits at all z gave fσ8 = 0.85 ± 0.11 with reduced χ² 1.08, so a
  good χ² does not guarantee a sound sample [src: arXiv:2512.03229, App. B, Table 2].
- **Taylor-approximated likelihood at high precision.** Acceptable at 18 % error, not at ~5 %
  [src: arXiv:2512.03229, Sect. 3.4].

## Reading list
<!-- key: reading-list -->

- Foundation: Abate et al. 2008, arXiv:0802.1935 — gridding the velocity covariance; the
  diagonal correction for cell means.
- Foundation: Johnson et al. 2014, arXiv:1404.3799 — velocity-only likelihood, gridding,
  magnitude errors with σ_v, hyper-parameter combination.
- Method: Adams & Blake 2017, arXiv:1706.05205 — density–velocity cross-covariance, per-field Γ,
  integration bounds and the extra density integral.
- Method and application: Adams & Blake 2020, arXiv:2004.06399 — RSD in the cross-covariance,
  α_b, η instead of v, emcee settings; 6dFGS fσ8.
- Method and application: Huterer et al. 2017, arXiv:1611.09862 — per-object signal-plus-noise
  covariance, μ against magnitude, nuisance marginalisation.
- Method: Lai et al. 2023, arXiv:2209.04166 — wide-angle RSD model, cell definitions, δ_g cut,
  Taylor-approximated likelihood.
- Method and code: Ravoux et al. 2025, arXiv:2501.16852 — flip, RC25, interpolation in σ_g,
  survey-geometry Fisher.
- Application: Lai et al. 2025, arXiv:2512.03229 — the DESI DR1 implementation, numerics, error
  rescaling.
- Forecast: Koda et al. 2014, arXiv:1312.1022; Howlett et al. 2017, arXiv:1609.08247 — Fisher
  matrices for correlated density and velocity fields and for combined surveys.
- Application (simulation): Ravoux et al. 2026, arXiv:2609.34508 — mesh configurations, per-SN
  velocities, σ_u prior, density gain.
- Sampled-field peers: Lavaux 2016, arXiv:1512.04534 (VIRBIuS); Prideaux-Ghee et al. 2022,
  arXiv:2204.00023 (BORG-PV); Valade et al. 2022, arXiv:2203.02369 (HAMLET); Courtois et al. 2023,
  arXiv:2211.16390 (Cosmicflows-4 fields and fσ8).

## Not verified
<!-- key: not-verified -->

- Abate et al. 2008 and Sugiyama et al. 2023 (the error-rescaling reference) were not read in
  the body; the Abate correction is quoted as the DESI and 6dFGS papers write it.
- Appendix A of arXiv:2512.03229 (SPT against RPT) and Appendix D of arXiv:2501.16852 (numerical
  regularisation) were not read.
- Whether "p = 4" (flip) and "p_max = 3" (DESI DR1) describe the same truncation counted from
  0 or from 1 was not resolved.
- The mesh-assignment-scheme result of arXiv:2609.34508 (Sect. 4.1 beyond its first sentence)
  was cut off in reading.
- The body of Courtois et al. 2023 (arXiv:2211.16390) was not read: whether its fσ8 comes from
  the HMC reconstruction (as arXiv:2502.00121 writes) or from a pairwise velocity correlation
  (as its abstract writes) is left as the two papers state it. The method sections of VIRBIuS
  and of Huterer, Shafer & Schmidt 2015 (the "HSS" method of arXiv:1611.09862) were not read.
