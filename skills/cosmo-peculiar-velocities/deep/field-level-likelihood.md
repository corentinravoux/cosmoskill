# Field-level likelihood — cosmo-peculiar-velocities dossier

Scope: how a "maximum-likelihood fields" growth-rate fit is assembled — data vector, gridding,
the terms added to the model covariance (gridding window, shot noise, η errors, σ_v, the extra
density integral), the free and fixed parameters, the numerics — and how to choose between
gridded and per-object data, covariance models, mesh settings and error calibrations.
Snapshot: 2026-10-17.
From: Turner 2024 review (arXiv:2411.19484), Sect. 5.4; DESI DR1 PV maximum-likelihood-fields
paper (arXiv:2512.03229).

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
  unweighted counts against randoms (arXiv:2209.04166, Eq. 27) [src: Sect. 4.1.2]. flip builds
  δ_g,i = N_cell,i/N_exp,i − 1 with pypower mesh assignment (NGP, CIC, TSC or PCS) [src:
  arXiv:2501.16852, Sect. 3.2].
- **η per cell.** The unweighted mean η^grid = (1/N) Σ η_i, with error
  σ_η = (1/N) sqrt(Σ σ²_η,i) (arXiv:2512.03229, Eqs. 20–21) [src]. The authors give their reason
  for applying no completeness weight: "the missing galaxies may not have the same log-distance
  ratio as the observed galaxies", and individual η are noise-dominated, so duplicating them "may
  not be appropriate"; an FKP-like weight (momentum FKP × κ²) and inverse-variance weights were
  both tried on mocks with "negligible" or "little" impact [src: Sect. 3.2.2, footnotes 5–6].
  The 6dFGSv analysis averaged magnitude fluctuations δm in cells in the same way, with the
  error σ_δm,i = N_i^{-3/2} Σ σ_j (arXiv:1404.3799, Eq. 28) [src: Sect. 3.5].
- **Per-object velocities.** For SNe Ia, flip and its applications keep one entry per SN, with
  v_i = −(c ln10/5) J(p_i) Δμ_i (arXiv:2501.16852, Eq. 34) and Δμ_i written with the Tripp
  parameters (M_0, α, β, σ_M) fitted with fσ8 (Eqs. 35–36) [src: Sect. 3.2]. In the DESI BGS ×
  ZTF study only the density is meshed [src: arXiv:2609.34508, Sect. 3].
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

flip's RC25 model, used in the BGS × ZTF study, writes the three spectra with the full
exponential FoG and the D_u damping (arXiv:2609.34508, Eq. 16), and the input spectra in the
Bel et al. (2019) form: P_mm = P_HF/σ8², P_mθ and P_θθ damped by fitted functions of σ8 (Eq. 17)
[src: Sect. 3].

### Step 3. Convert velocities to η
<!-- key: step-3-convert-velocities-to-eta -->

C_ηη = κ(z1)κ(z2) C_vv, C_ηg = κ(z1) C_vg, C_gη = κ(z2) C_gv, with
κ(z) = (1 + z)/[ln10 D(z) H(z)] (arXiv:2512.03229, Eqs. 12–15) [src: Sect. 3.2.1]. The
alternative is to fit velocities with a per-object error propagated from σ_η or σ_Δμ (flip,
arXiv:2501.16852, Sect. 3.2) [src].

### Step 4. Correct the model for the grid
<!-- key: step-4-correct-the-model-for-the-grid -->

- **Window.** P_XY → P_XY Γ(k)² (arXiv:2512.03229, Eq. 22), with
  Γ(k) = (1/4π) ∫∫ sinθ dφ dθ sin k_x sin k_y sin k_z/(k_x k_y k_z), k_{x,y,z} = (kL/2)(…) (Eqs.
  23–24) [src: Sect. 3.2.2]. With different grids per field, one Γ per field enters the cross
  term, Γ_δg Γ_vp (Adams & Blake 2017, arXiv:1706.05205, Eqs. 31–35) [src: Sect. 3.7]. For a
  mesh assignment of order n (1 NGP, 2 CIC, 3 TSC, 4 PCS) the kernel is raised to the n-th
  power (arXiv:2609.34508, Eq. 18), and only the meshed field carries it: P_mθ × Γ, P_mm × Γ²
  [src: Sect. 3].
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

For per-object SN velocities the stochastic term per object is σ_v (and σ_M through Δμ) [src:
arXiv:2609.34508, Sect. 4.2]. In the magnitude formulation of Johnson et al., σ_i² = σ²_obs +
(5/ln10)² (1 − (1 + z)²/(H d_L))² σ_v² (arXiv:1404.3799, Eq. 19), and σ_obs is not fitted since
it is degenerate with σ_v [src: Sect. 3.2.2].

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

flip instead pre-computes covariance terms per parameter coefficient and interpolates over σ_g
(density fits) or σ_u (combined fits), minimising with iminuit (MIGRAD, MINOS) [src:
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
- Per-object fits avoid the grid window; in flip's N-body validation, without gridding,
  k_max = 100 h Mpc⁻¹ is used "to avoid aliasing in the integration without the grid window
  function" [src: arXiv:2501.16852, Sect. 4.4]. In the BGS × ZTF tests on per-object SN
  velocities, k_max = 0.2 h Mpc⁻¹ biases fσ8 in dense configurations (6 000 SNe within 150
  h⁻¹Mpc) and 1.0 does not; 1.0 is adopted [src: arXiv:2609.34508, Sect. 4.2].

### Mesh settings of the density field
<!-- key: mesh-settings-of-the-density-field -->

On 27 BGS mocks and 192 mesh configurations, varying one setting from a baseline (30 h⁻¹Mpc
voxel, 150 h⁻¹Mpc spherical mesh, NGP, k_max = 1.0) [src: arXiv:2609.34508, Sect. 4.1]:

- total mesh size > 250 h⁻¹Mpc biases fσ8 through its correlation with σ_g, which the fit uses to
  absorb BAO-peak smoothing once the volume reaches BAO scales; fixing σ_g from a small-volume
  fit removes the bias;
- a 10 h⁻¹Mpc voxel biases fσ8, "as our linear model is inaccurate at such small scales";
- the footprint cut moves bσ8, not fσ8.

In the combined fit, σ_g is fixed to 6.0 h⁻¹Mpc from the density fit, because a joint (σ_g,
σ_u) interpolation needs "a very large number of covariance matrices" and the two are
correlated; the authors flag this as a possible bias [src: Sect. 4.3]. The configuration
L = 30, R = 300 h⁻¹Mpc gives a 1.8 % mean bias and σ(fσ8) = +0.047/−0.048 (a **forecast** on
simulations); L = 20 with large R shows a ~1σ bias [src: Sect. 4.3].

### Taylor-expanded or exact finger-of-God
<!-- key: taylor-expanded-or-exact-finger-of-god -->

L22 keeps σ_g as a linear parameter at the price of the kμσ_g ≪ 1 assumption; RC25 removes the
expansion, extending the model to k > 0.1 h Mpc⁻¹, but must interpolate σ_g [src:
arXiv:2501.16852, Sect. 3.1]. DESI DR1 chose L22 for cost, with consistent covariances at
k_max = 0.20 (Step 2).

### Velocity only or density + velocity
<!-- key: velocity-only-or-density-velocity -->

- DESI DR1: after error inflation the combined fit has an error similar to velocity only; the
  authors still prefer it because velocity-only fσ8 "is very degenerate with σ_u", while the
  galaxy block does not depend on σ_u [src: arXiv:2512.03229, Sect. 4.4.2]. The best σ_u differs
  between the two (16 against 10 h⁻¹Mpc) "because the cross-covariance also depends on σ_u"
  [src: same].
- BGS × ZTF simulations: adding the density reduces the fσ8 error by up to 50 % without bias
  for 30 h⁻¹Mpc voxels, and narrows σ_u [src: arXiv:2609.34508, Sect. 4.3].
- 6dFGS: the cross-covariance is seen directly in the data, non-zero to separations of ~50
  h⁻¹Mpc (arXiv:1706.05205, Sect. 5.3, Eqs. 44–45) [src].

### σ_u fixed, sampled with a prior, or interpolated
<!-- key: sigmau-fixed-sampled-with-a-prior-or -->

DESI DR1 fixes it (cost, memory). The BGS × ZTF study puts a Gaussian prior centred on 21.5 with
width 10 h⁻¹Mpc to "stabilize the fit" along the σ_u–fσ8 degeneracy, and states that a σ_u prior
"should be very large to avoid dependence on a specific set of simulations"; 21.5 was measured
on AbacusSummit at z = 0.2 and exceeds the OuterRim value of Carreres et al. [src:
arXiv:2609.34508, Sect. 4.2].

### Combining surveys
<!-- key: combining-surveys -->

Johnson et al. combine 6dFGSv and SNe with a hyper-parameter matrix, C^{DiDj} → (α_i α_j)^{-1/2}
C^{DiDj} (arXiv:1404.3799, Eqs. 41–42), and fix σ_v at the single-survey values because it is
degenerate with the hyper-parameters [src: Sect. 3.7].

### Analytic Fisher or full likelihood
<!-- key: analytic-fisher-or-full-likelihood -->

A Fisher matrix from the field covariance at the real positions, F_ij = ½ Tr[A_i A_j], A_i =
C⁻¹C_,i (arXiv:2501.16852, Eq. 52), is on average 30 % closer to the likelihood errors than a
volume Fisher (Eqs. 50–51) on 27 ZTF realisations, the difference being attributed to geometry
and nuisance parameters [src: Sect. 5].

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
| b_add from 6dFGS sims | b_add σ8 = 1.306, b_fit σ8 = 1.29; b_add = 0 at Δχ² = 241.27 | GiggleZ | arXiv:1706.05205 | Sect. 4.2 |
| σ_u prior | N(21.5, 10) h⁻¹Mpc | BGS × ZTF sims | arXiv:2609.34508 | Sect. 4.2 |
| σ_g fixed | 6.0 h⁻¹Mpc | BGS × ZTF sims | arXiv:2609.34508 | Sect. 4.3 |
| SN z_max | 0.07 | ZTF sims | arXiv:2609.34508 | Sect. 4.2 |
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
- **k_max too low for per-object velocities.** Biased fσ8 in dense samples [src:
  arXiv:2609.34508, Sect. 4.2]. Test: vary k_max and the object density at fixed volume.
- **σ_g absorbing BAO smoothing.** In large meshes fσ8 drifts with σ_g; test: fix σ_g from a
  small-volume fit [src: arXiv:2609.34508, Sect. 4.1].
- **Indicator split.** TF-only fits at all z gave fσ8 = 0.85 ± 0.11 with reduced χ² 1.08, so a
  good χ² does not guarantee a sound sample [src: arXiv:2512.03229, App. B, Table 2].
- **SN selection.** Beyond z ≈ 0.07 the ZTF-like sample biases fσ8 and the Hubble-diagram
  parameters [src: arXiv:2609.34508, Sect. 4.2].
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
- Method: Lai et al. 2023, arXiv:2209.04166 — wide-angle RSD model, cell definitions, δ_g cut,
  Taylor-approximated likelihood.
- Method and code: Ravoux et al. 2025, arXiv:2501.16852 — flip, RC25, interpolation in σ_g,
  survey-geometry Fisher.
- Application: Lai et al. 2025, arXiv:2512.03229 — the DESI DR1 implementation, numerics, error
  rescaling.
- Application (simulation): Ravoux et al. 2026, arXiv:2609.34508 — mesh configurations, per-SN
  velocities, σ_u prior, density gain.

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
