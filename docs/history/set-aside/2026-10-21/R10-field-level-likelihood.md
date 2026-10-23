# R10 set-aside — cosmo-peculiar-velocities/deep/field-level-likelihood.md

Run R10 of step 4 (docs/plans/2026-10-21-plan.md), 2026-10-22. Verbatim copies, before shortening,
of the passages of the dossier that rest on the owner's papers (flip, arXiv:2501.16852; DESI BGS × ZTF
simulation study, arXiv:2609.34508). Line numbers are those of the file at commit add8d13 plus the
working tree of 2026-10-22, before R10. The base keeps a condensed line for each; the depth is for the
owner's personal layer.

From `### Step 1. Build the data vector`, line 37:

- **Density per cell.** DESI DR1: δ_g^grid = (w − α w_r)/(α w_r), w = Σ w_i^comp w_i^FKP over the
  galaxies of the cell, w_i^FKP = 1/(1 + n̄_g P_0) with P_0 = 1 600 h⁻³Mpc³, α the ratio of
  weighted data to random counts (arXiv:2512.03229, Eqs. 16–19) [src: Sect. 3.2.2]. SDSS PV used
  unweighted counts against randoms (arXiv:2209.04166, Eq. 27) [src: Sect. 4.1.2]. flip builds
  δ_g,i = N_cell,i/N_exp,i − 1 with pypower mesh assignment (NGP, CIC, TSC or PCS) [src:
  arXiv:2501.16852, Sect. 3.2].

From `### Step 1. Build the data vector`, line 51:

- **Per-object velocities.** For SNe Ia, flip and its applications keep one entry per SN, with
  v_i = −(c ln10/5) J(p_i) Δμ_i (arXiv:2501.16852, Eq. 34) and Δμ_i written with the Tripp
  parameters (M_0, α, β, σ_M) fitted with fσ8 (Eqs. 35–36) [src: Sect. 3.2]. In the DESI BGS ×
  ZTF study only the density is meshed [src: arXiv:2609.34508, Sect. 3].

From `### Step 2. Model the field covariance`, line 75:

- p_max = q_max = 3 in the D_g expansion, "equivalent to using a third-order Taylor expansion",
  enough because kσ_g ≲ 1. The flip paper describes the same L22 model as "calculated to the
  p = 4 order" [src: arXiv:2501.16852, Sect. 3.1]; the two statements are as printed.

From `### Step 2. Model the field covariance`, line 83:

flip's RC25 model, used in the BGS × ZTF study, writes the three spectra with the full
exponential FoG and the D_u damping (arXiv:2609.34508, Eq. 16), and the input spectra in the
Bel et al. (2019) form: P_mm = P_HF/σ8², P_mθ and P_θθ damped by fitted functions of σ8 (Eq. 17)
[src: Sect. 3].

From `### Step 3. Convert velocities to η`, line 91:

C_ηη = κ(z1)κ(z2) C_vv, C_ηg = κ(z1) C_vg, C_gη = κ(z2) C_gv, with
κ(z) = (1 + z)/[ln10 D(z) H(z)] (arXiv:2512.03229, Eqs. 12–15) [src: Sect. 3.2.1]. The
alternative is to fit velocities with a per-object error propagated from σ_η or σ_Δμ (flip,
arXiv:2501.16852, Sect. 3.2) [src].

From `### Step 4. Correct the model for the grid`, line 99:

- **Window.** P_XY → P_XY Γ(k)² (arXiv:2512.03229, Eq. 22), with
  Γ(k) = (1/4π) ∫∫ sinθ dφ dθ sin k_x sin k_y sin k_z/(k_x k_y k_z), k_{x,y,z} = (kL/2)(…) (Eqs.
  23–24) [src: Sect. 3.2.2]. With different grids per field, one Γ per field enters the cross
  term, Γ_δg Γ_vp (Adams & Blake 2017, arXiv:1706.05205, Eqs. 31–35) [src: Sect. 3.7]. For a
  mesh assignment of order n (1 NGP, 2 CIC, 3 TSC, 4 PCS) the kernel is raised to the n-th
  power (arXiv:2609.34508, Eq. 18), and only the meshed field carries it: P_mθ × Γ, P_mm × Γ²
  [src: Sect. 3].

From `### Step 5. Add the observational and nuisance terms`, line 133:

For per-object SN velocities the stochastic term per object is σ_v (and σ_M through Δμ) [src:
arXiv:2609.34508, Sect. 4.2]. In the magnitude formulation of Johnson et al., σ_i² = σ²_obs +
(5/ln10)² (1 − (1 + z)²/(H d_L))² σ_v² (arXiv:1404.3799, Eq. 19), and σ_obs is not fitted since
it is degenerate with σ_v [src: Sect. 3.2.2].

From `### Step 6. Evaluate and sample the likelihood`, line 155:

flip instead pre-computes covariance terms per parameter coefficient and interpolates over σ_g
(density fits) or σ_u (combined fits), minimising with iminuit (MIGRAD, MINOS) [src:
arXiv:2609.34508, Sects. 4.1, 4.3].

From `### Gridded or per-object data`, line 176:

- Per-object fits avoid the grid window; in flip's N-body validation, without gridding,
  k_max = 100 h Mpc⁻¹ is used "to avoid aliasing in the integration without the grid window
  function" [src: arXiv:2501.16852, Sect. 4.4]. In the BGS × ZTF tests on per-object SN
  velocities, k_max = 0.2 h Mpc⁻¹ biases fσ8 in dense configurations (6 000 SNe within 150
  h⁻¹Mpc) and 1.0 does not; 1.0 is adopted [src: arXiv:2609.34508, Sect. 4.2].

From `### Mesh settings of the density field`, line 183:

<!-- key: mesh-settings-of-the-density-field -->

From `### Mesh settings of the density field`, line 185:

On 27 BGS mocks and 192 mesh configurations, varying one setting from a baseline (30 h⁻¹Mpc
voxel, 150 h⁻¹Mpc spherical mesh, NGP, k_max = 1.0) [src: arXiv:2609.34508, Sect. 4.1]:

From `### Mesh settings of the density field`, line 188:

- total mesh size > 250 h⁻¹Mpc biases fσ8 through its correlation with σ_g, which the fit uses to
  absorb BAO-peak smoothing once the volume reaches BAO scales; fixing σ_g from a small-volume
  fit removes the bias;

From `### Mesh settings of the density field`, line 191:

- a 10 h⁻¹Mpc voxel biases fσ8, "as our linear model is inaccurate at such small scales";

From `### Mesh settings of the density field`, line 192:

- the footprint cut moves bσ8, not fσ8.

From `### Mesh settings of the density field`, line 194:

In the combined fit, σ_g is fixed to 6.0 h⁻¹Mpc from the density fit, because a joint (σ_g,
σ_u) interpolation needs "a very large number of covariance matrices" and the two are
correlated; the authors flag this as a possible bias [src: Sect. 4.3]. The configuration
L = 30, R = 300 h⁻¹Mpc gives a 1.8 % mean bias and σ(fσ8) = +0.047/−0.048 (a **forecast** on
simulations); L = 20 with large R shows a ~1σ bias [src: Sect. 4.3].

From `### Taylor-expanded or exact finger-of-God`, line 203:

L22 keeps σ_g as a linear parameter at the price of the kμσ_g ≪ 1 assumption; RC25 removes the
expansion, extending the model to k > 0.1 h Mpc⁻¹, but must interpolate σ_g [src:
arXiv:2501.16852, Sect. 3.1]. DESI DR1 chose L22 for cost, with consistent covariances at
k_max = 0.20 (Step 2).

From `### Velocity only or density + velocity`, line 216:

- BGS × ZTF simulations: adding the density reduces the fσ8 error by up to 50 % without bias
  for 30 h⁻¹Mpc voxels, and narrows σ_u [src: arXiv:2609.34508, Sect. 4.3].

From `### σ_u fixed, sampled with a prior, or interpolated`, line 224:

DESI DR1 fixes it (cost, memory). The BGS × ZTF study puts a Gaussian prior centred on 21.5 with
width 10 h⁻¹Mpc to "stabilize the fit" along the σ_u–fσ8 degeneracy, and states that a σ_u prior
"should be very large to avoid dependence on a specific set of simulations"; 21.5 was measured
on AbacusSummit at z = 0.2 and exceeds the OuterRim value of Carreres et al. [src:
arXiv:2609.34508, Sect. 4.2].

From `### Analytic Fisher or full likelihood`, line 240:

A Fisher matrix from the field covariance at the real positions, F_ij = ½ Tr[A_i A_j], A_i =
C⁻¹C_,i (arXiv:2501.16852, Eq. 52), is on average 30 % closer to the likelihood errors than a
volume Fisher (Eqs. 50–51) on 27 ZTF realisations, the difference being attributed to geometry
and nuisance parameters [src: Sect. 5].

From `## Numbers`, line 263:

| σ_u prior | N(21.5, 10) h⁻¹Mpc | BGS × ZTF sims | arXiv:2609.34508 | Sect. 4.2 |

From `## Numbers`, line 264:

| σ_g fixed | 6.0 h⁻¹Mpc | BGS × ZTF sims | arXiv:2609.34508 | Sect. 4.3 |

From `## Numbers`, line 265:

| SN z_max | 0.07 | ZTF sims | arXiv:2609.34508 | Sect. 4.2 |

From `## Numbers`, line 266:

| Fisher vs volume Fisher | 30 % closer to likelihood errors | ZTF sims | arXiv:2501.16852 | Sect. 5 |

From `## What goes wrong`, line 283:

- **k_max too low for per-object velocities.** Biased fσ8 in dense samples [src:
  arXiv:2609.34508, Sect. 4.2]. Test: vary k_max and the object density at fixed volume.

From `## What goes wrong`, line 285:

- **σ_g absorbing BAO smoothing.** In large meshes fσ8 drifts with σ_g; test: fix σ_g from a
  small-volume fit [src: arXiv:2609.34508, Sect. 4.1].

From `## What goes wrong`, line 289:

- **SN selection.** Beyond z ≈ 0.07 the ZTF-like sample biases fσ8 and the Hubble-diagram
  parameters [src: arXiv:2609.34508, Sect. 4.2].

From `## Reading list`, line 305:

- Method and code: Ravoux et al. 2025, arXiv:2501.16852 — flip, RC25, interpolation in σ_g,
  survey-geometry Fisher.

From `## Reading list`, line 309:

- Application (simulation): Ravoux et al. 2026, arXiv:2609.34508 — mesh configurations, per-SN
  velocities, σ_u prior, density gain.

From `## Not verified`, line 317:

- Appendix A of arXiv:2512.03229 (SPT against RPT) and Appendix D of arXiv:2501.16852 (numerical
  regularisation) were not read.

From `## Not verified`, line 321:

- The mesh-assignment-scheme result of arXiv:2609.34508 (Sect. 4.1 beyond its first sentence)
  was cut off in reading.
