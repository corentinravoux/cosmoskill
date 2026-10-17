# Fast mocks — cosmo-simulations-mocks dossier

Scope: how an approximate mock set is generated and tuned (the COLA and
FastPM integrators and their settings, the effective-bias model of EZmocks
and its calibration, occupation models fitted on fast-mock haloes, the
application of survey effects, control variates), and how to choose
between these routes and their settings.
Snapshot: 2026-10-17.
From: Angulo & Hahn 2021 review (arXiv:2112.05165), Sect. 4.4; DESI mock
challenge (arXiv:2307.14197); LSST DESC Survey Computing & Simulation
working group.

Already in L2, not repeated here: the families of approximate methods with
the accuracy each paper states
(`physics-and-methods.md#approximate-methods-and-fast-mocks`); the mock
sets of BOSS, eBOSS and DESI with their counts and calibration chains
(`physics-and-methods.md#what-the-main-suites-ran`,
`surveys-and-data.md#fast-mock-sets-used-by-surveys`); the comparison of
seven methods against 300 N-body runs and the DESI DR1 rescaling of the
EZmock covariance (`systematics.md#covariance-from-approximate-mocks`,
`results.md#accuracy-of-approximate-methods`). The finite-mock corrections
and the choice between analytic and mock covariances belong to
`cosmo-statistics-inference` (its `deep/covariance-estimation.md`).

Symbols used throughout. a: scale factor; z_i: starting redshift; N_s:
number of global time steps; B: force-mesh factor, the ratio of the force
mesh N_m to the number of particles per side N_g (FastPM notation,
arXiv:1603.00476, Sect. 3; ICE-COLA writes the same quantity PM_grid);
Ψ: Lagrangian displacement; D(a): linear growth factor; P_1, P_2: power
spectra of the approximate and the reference field.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Choose the dynamics: a quasi-N-body integrator or LPT alone
<!-- key: step-1-choose-the-dynamics-a-quasi-n-body -->

Two families supply the matter field. Quasi-N-body codes (COLA, FastPM)
take a few particle-mesh steps and form haloes with a finder; LPT-plus-bias
methods (EZmocks and its relatives) displace particles once and paint
tracers on the grid with a stochastic bias, with no haloes at all. The
review places both among methods "widely-adopted to more efficiently
create large ensembles" accurate on mildly non-linear scales, and notes
that for neither COLA nor FastPM has the order of convergence been
discussed in the literature [src: arXiv:2112.05165, Sect. 4.4].

### Step 2a. COLA: integrate the residual about an LPT trajectory
<!-- key: step-2a-cola-integrate-the-residual-about-an -->

COLA rewrites the equation of motion in the frame of "LPT observers":
∂²_t x_res = −∇Φ − ∂²_t x_LPT, with x_res ≡ x − x_LPT (Tassev et al.
2013, arXiv:1301.0322, Eq. 2), and discretises ∂²_t only on the left-hand
side while using the exact LPT fictitious force [src: Sect. 2]. With 2LPT
trajectories, the large scales are exact to second order in the
overdensity for any number of steps, even one; the errors are at most
third order [src: Sect. 2]. The review writes the same scheme as modified
drift and kick operators, D_COLA X = D X + Ψ_LPT(t + ε) − Ψ_LPT(t) and
K_COLA P = K P + M[Ψ̇_LPT(t + ε) − Ψ̇_LPT(t)] (arXiv:2112.05165,
Eqs. 55a–b), accurate at first order only, and at the cost of storing the
LPT fields for every particle [src: Sect. 4.4].

The time dependence of the residual velocity is modelled as u(a) ∝ a^{n_LPT}
(arXiv:1301.0322, App. A.3.2). n_LPT is a free parameter: it depends on
the initial-condition code, z_i, box size, force resolution, particle mass
and grid or glass load, and "one should always fit n_LPT for the
particular initial set-up at hand before generating numerous
realizations"; the paper's set-up has n_LPT = −2.5, insensitive to ±0.5
[src: App. A.3.2]. The authors add that their modified discretisation
performed better in all their experiments but "experimentation is always
advised" [src: same].

### Step 2b. FastPM: modified kick and drift factors, no LPT storage
<!-- key: step-2b-fastpm-modified-kick-and-drift-factors -->

FastPM keeps a plain kick–drift–kick particle-mesh scheme but replaces the
drift and kick factors by the ones that make a Zel'dovich trajectory exact
over a step: D_FastPM = Δ[G_p]/(a_r³ E(a_r) g_p(a_r)), with G_p = D,
g_p = dD/da, E = H/H_0, a_r the reference time of the step, and the kick
factor built the same way from g_f = d(a³E g_p)/da (Feng et al. 2016,
arXiv:1603.00476, Eqs. 15–20 and 24–25) [src: Sect. 2.5]. The stated
reason: with few steps a standard kick–drift–kick fails to give the linear
growth (1.5% error for one step from a = 0.1 to 0.2), while COLA's fix
costs memory and a force split "which requires tuning that is somewhat
dependent on the number of time steps" [src: Sect. 2.5]. FastPM has no
free integration parameter [src: Sect. 3.2]. The review records the
counter-view that no such modification is needed if the time stepping is
chosen appropriately (Klypin & Prada 2018a, as cited) [sec:
arXiv:2112.05165, Sect. 4.4].

Force kernel. FastPM's default is the finite-difference kernel of its
Eqs. 3–4, with no deconvolution of the cloud-in-cell window and no
Gaussian smoothing, because even a mild smoothing with r_s = L/N_m
"significantly reduces the number of halos at the low mass end"
[src: arXiv:1603.00476, Sect. 2.1].

### Step 3. Set steps, mesh and starting redshift
<!-- key: step-3-set-steps-mesh-and-starting-redshift -->

Time sampling. FastPM accepts steps linear in a (better mass function,
needs help for linear growth with few steps), linear in log a (better
large-scale growth, fewer haloes), or a hybrid (δa/a)⁻¹ =
√((1/a_1)² + (a/a_2)²) (arXiv:1603.00476, Eq. 6) [src: Sect. 2.1].
ICE-COLA compared linear, logarithmic and a^p sampling with 40 steps from
z_i = 39 and found linear in a the best at all redshifts; the logarithmic
choice oversamples early times and starves z < 2 of steps [src:
arXiv:1509.04685, Sect. 4.2].

Number of steps, as measured against MICE-GC (ICE-COLA, mesh factor 3):

- 10 steps from z_i = 9: matter P(k) at 5% to k ≈ 0.5 h/Mpc; the halo mass
  function "severely underestimated" at z = 1, within 15% at z = 0.5 and
  5% at z = 0; halo bias overestimated by up to 20% at z = 1 [src:
  arXiv:1509.04685, Sect. 3]. The stated cause is a coarse time grid that
  prevents relaxation inside haloes, so that masses come out low at high
  redshift [src: same].
- 2% agreement on P(k) at z = 0 up to k ≈ 0.4, 0.6 and 0.8 h/Mpc for 10,
  20 and 40 steps; doubling the steps roughly doubles that wavenumber
  [src: Sect. 4.1].
- The low-mass end of the mass function converges with 20 steps; the most
  massive haloes need 40 [src: Sect. 4.1]. The rule drawn: at least 10
  steps before the redshift of interest, so 20 or more to z = 0 [src:
  Sect. 4.5].

Starting redshift. A first guess is z_i equal to the step width in a
(z_i = 9 for 10 steps); for 40 steps z_i = 9 leaves percent-level
transients, z_i ≳ 19 are nearly equivalent, and too early a start smooths
the small peaks that seed low-mass haloes; z_i = 19 was adopted [src:
arXiv:1509.04685, Sect. 4.3]. FastPM finds the same competition: with 10
steps z_i = 9 or 19 beats z_i = 75, while with many steps matching the z_i
of the reference run is best [src: arXiv:1603.00476, App. B].

Force mesh. ICE-COLA: going from mesh factor 3 to 2 saves 70% of the time
and 30% of the memory and changes P(k) by about 1% for k ≲ 1 h/Mpc, but the
mass function within 5% then holds only above about 10¹³ instead of
10¹²·⁵ M_⊙/h; the rule given is about 8 force cells across the typical
size of the smallest halo wanted [src: arXiv:1509.04685, Sect. 4.4].
FastPM with N_s = 10: B ≥ 2 recovers 90% of the mass function above
10¹² M_⊙/h, B = 1 only 80% at 10¹³; B = 2 against B = 3 costs about 2% in
stochasticity for the lightest haloes at a third of the time, and
N_s = 10, B = 2 uses about 10% of the CPU of N_s = 40, B = 3 with nearly
identical halo benchmarks [src: arXiv:1603.00476, Sect. 3.3].

### Step 4. Turn haloes into a catalogue
<!-- key: step-4-turn-haloes-into-a-catalogue -->

Abundance matching of masses. Approximate codes misassign masses; both
papers re-rank haloes by mass against a reference mass function before
populating them [src: arXiv:1603.00476, Sect. 3.1; arXiv:1509.04685,
Sect. 5.1]. In ICE-COLA this repairs bias only where the catalogue is
complete, M ≳ 10¹³ M_⊙/h; below that, missing haloes are mixed with haloes
of other clustering [src: Sect. 5.1]. An alternative shifts masses by
δ ln M = (∂b/∂ln M)⁻¹ b δ ln b (arXiv:1509.04685, Eq. 4) with
δ ln b = 0.02, the residual bias offset found, giving bias within 1% to
k ≲ 0.5 h/Mpc for most samples [src: Sect. 5.2].

Occupation fitted to an N-body target (DESI mock challenge). FastPM boxes
(505 Mpc/h; 778 at 1296³ and 141 at 1536³ particles; B = 2; 40 steps
linear from a = 0.05 to 0.96; FoF haloes above 5.72 × 10¹⁰ M_⊙/h) were
populated with a five-parameter Zheng et al. HOD plus a satellite
line-of-sight velocity factor v_disp (arXiv:2307.14197, Eqs. 8–11) [src:
Sects. 2.2, 3.2]. The target was the clustering of 139 SLICS N-body
catalogues populated with an ELG occupation model [src: Sect. 2.1]. The
authors chose the simple HOD because FastPM haloes are less accurate than
N-body ones, so the fitted parameters are not expected to keep their
physical meaning; what matters is that clustering and covariance match
[src: Sect. 3.2]. The fit has two steps [src: Sects. 3.3.1–3.3.2]:

1. Fit ξ_0, ξ_2 on s ∈ [0, 50] Mpc/h and the number density with a
   diagonal covariance σ_i = 3/s_i² (Eq. 17), on 123 FastPM runs sharing
   the SLICS initial conditions.
2. Refit with the covariance of the paired differences
   Δ = (FastPM − SLICS) over the 123 pairs (Eqs. 18–20), in P_ℓ for
   k ∈ [0.02, k_max] with k_max = 0.5, 0.4 or 0.3 h/Mpc, or in ξ_ℓ for
   s ∈ [s_min, 50] with s_min = 0, 5 or 10 Mpc/h (Table 3).

The paired-difference covariance is used because shared white noise makes
the standard covariance of either set "obsolete" for the fit [src:
Sect. 5].

Effective bias on the grid (EZmocks). The original recipe applies, until
convergence: Zel'dovich field on a grid; rank-ordered mapping of the halo
PDF of the reference; scatter; threshold and saturation fitted to P(k) and
the bispectrum; a tilt (1 + Ak) and a BAO enhancement
(P_lin − P_nw) exp(k²/k_*²) + P_nw of the input spectrum; Zel'dovich
velocities plus a Gaussian dispersion (Chuang et al. 2014,
arXiv:1409.1124, Sect. 3 and Eqs. 4–8) [src]. The authors chose direct
prescriptions for the clustering statistics instead of a physical bias
model, "at the expense of giving up more explicit physical relations",
because parameter finding is then much more efficient [src: Sect. 3].
The eBOSS version replaces these steps with one bias function (Zhao et al.
2020, arXiv:2007.08997, Sect. 2.2):

- ρ_t = θ(ρ_m − ρ_c) ρ_sat [1 − exp(−ρ_m/ρ_exp)] B_s (Eq. 16), with ρ the
  density in units of its mean on the grid (Eq. 13), θ the step function,
  ρ_c a critical density and ρ_exp an exponential cut-off;
- B_s = 1 + G(λ) for G ≥ 0, exp G(λ) otherwise, G Gaussian of width λ
  (Eq. 17);
- cell occupation numbers from P(n_t) = A bⁿᵗ, normalised to the target
  number density so that only b is free, assigned to cells ranked by ρ_t
  (Eqs. 18–21); tracers placed on dark-matter particles of the cell, or at
  random where there are none;
- velocities u_t = a f H Ψ_ZA + G(ν), an isotropic Gaussian of width ν in
  km/s (Eqs. 22–24).

ρ_sat = 10 and λ = 10 are fixed because they are degenerate with the other
parameters, leaving ρ_c, ρ_exp, b and ν free (Table 1) [src: Sects.
2.2.2–2.2.6]. Because the final densities are re-ranked, the exact form of
the scatter does not matter, only the order of cells [src: Sect. 2.2.3].
The BAO enhancement of the original recipe is dropped, because only 6, 16
and 4% of LRGs, ELGs and QSOs land at random positions and the BAO
strength matters little for covariances compared with the broad-band
amplitude [src: Sect. 2.2.4].

### Step 5. Calibrate
<!-- key: step-5-calibrate -->

eBOSS EZmocks [src: arXiv:2007.08997, Sect. 2.5 and Sect. 2.2.6]:

1. Calibrate on complete light-cones (footprint, no observational
   systematics), because the systematics act mainly outside the
   calibration scales and are expensive to apply.
2. Match ξ_0, ξ_2 on 10–50 Mpc/h, P_0, P_2 on 0.1–0.3 h/Mpc (0.24 for the
   QSO NGC) and one bispectrum configuration (k_1 = 0.1, k_2 = 0.05 h/Mpc,
   all angles), in broad overlapping redshift bins, because the fine bins
   have too few tracers for precise two- and three-point statistics.
3. Interpolate each parameter in redshift with
   p = c_0 + c_1 z_eff + c_2 z_eff⁽²⁾ (Eq. 36).
4. Tune by hand on one realisation, validate on 50, then mass-produce.

The parameters must be recalibrated whenever the grid changes at fixed
volume [src: Sect. 2.2.1]. The 2014 paper found that grids coarser than
its 960³ in 2500 Mpc/h damp the BAO peak [src: arXiv:1409.1124,
Sect. 3.1]. For DESI DR1 the target was not the data but the two-point
clustering of the AbacusSummit HOD mocks, snapshot by snapshot (see L2).

### Step 6. Apply the survey
<!-- key: step-6-apply-the-survey -->

eBOSS applied, after calibration, depth-dependent radial densities,
angular photometric systematics, fibre collisions found with an angular
friends-of-friends on the mock tracers and resolved by sector, with
up-weighting of collided objects, and redshift failures drawn from the
data's model by attaching each mock object to the fibre of the nearest
data tracer, refitting f_fail on each mock and weighting by
1/(1 − f_fail) [src: arXiv:2007.08997, Sects. 2.6.3–2.6.4]. DESI DR1
applied the Y1 footprint and a fast fibre-assignment emulator to the
concatenated pseudo-light-cone [src: arXiv:2411.12027, Sect. 2.1].

### Step 7. Optionally pair each mock with a cheap control
<!-- key: step-7-optionally-pair-each-mock-with-a-cheap -->

A control variate pairs each mock with a Zel'dovich realisation from the
same initial conditions: Y_ij = X_ij − β_ij (C_ij − μ_ij), with X and C
the sample covariances of the mocks and of their Zel'dovich partners and
μ the true Zel'dovich covariance (Hadzhiyska & White 2026,
arXiv:2605.28817, Eqs. 11–14) [src]. The optimal β = Cov[X, C]/Var[C]
leaves Var[Y] = Var[X](1 − ρ²) (Eqs. 16–18), so the effective number of
simulations grows by 1/(1 − ρ²): ρ = 0.95 makes 1000 paired runs worth
about 10,000 [src: Sect. II.2.2]. μ is estimated from 10,000 Zel'dovich
realisations passed through the same mask, because the mask couples modes
in a way that is cumbersome to compute analytically [src: Sect. II.2.1].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### COLA or FastPM
<!-- key: cola-or-fastpm -->

- Same reference (RunPB, TreePM, 2048³ particles in 1380 Mpc/h), same
  initial modes: with N_s = 10 COLA gives a larger matter transfer function
  than FastPM, with N_s = 5 a smaller one and a much worse cross-correlation
  [src: arXiv:1603.00476, Sects. 3 and 3.2].
- Haloes after abundance matching: FastPM is nearly a factor 2 closer to
  the reference at N_s = 5; the advantage shrinks with steps and vanishes
  at 40 [src: Sect. 3.2]. The authors suggest COLA's free parameters may
  have been tuned for the matter field at the expense of haloes [src:
  same].
- Memory: COLA stores the 2LPT fields of each particle; FastPM does not
  [src: arXiv:2112.05165, Sect. 4.4].
- ICE-COLA shows the 2LPT part of COLA still improves on PM-only evolution
  at 20 and 40 steps (its App. B, as summarised in Sect. 4.1) [src:
  arXiv:1509.04685, Sect. 4.1]. The two statements are from different
  codes and settings; no paper read here compares them at one setting.
- Newer second-order steppers (BullFrog) are summarised in L2.

### Haloes plus HOD, or an effective bias on the grid
<!-- key: haloes-plus-hod-or-an-effective-bias-on-the-grid -->

- Haloes plus HOD (FastPM, COLA): galaxies sit in identifiable objects, so
  satellites and velocity dispersions can be modelled; requires a mesh fine
  enough for the host masses (8 cells per halo size in ICE-COLA) and a
  halo finder. In the DESI challenge the low-resolution set reproduced the
  N-body ξ_ℓ, P_ℓ to the DESI Y1 ELG precision for k < 0.5 h/Mpc or
  s > 10 Mpc/h [src: arXiv:2307.14197, abstract].
- Effective bias (EZmocks): one Zel'dovich step on a 1024³ or 1728³ grid,
  no halo finding; the price is that the bias parameters are functions of
  grid, redshift and tracer with no physical meaning (Table 4 of
  arXiv:2007.08997 lists them per redshift slice, e.g. ν from 150 km/s for
  ELGs to 501 km/s for QSOs at z ≈ 2) [src: Sect. 2.5, Table 4].

### Calibrate on data or on N-body mocks
<!-- key: calibrate-on-data-or-on-n-body-mocks -->

- On data (eBOSS): the mocks reproduce the measured clustering by
  construction; L2 records why agreement is then not a test
  (`systematics.md#light-cone-and-survey-realism-limits`).
- On N-body HOD mocks (DESI DR1): the fast mocks inherit the occupation
  model of the reference (L2). The DESI challenge adds that the fitting
  statistic matters: no fit reproduced both P_ℓ and ξ_ℓ of the reference
  within 1σ; a ξ fit with s_min = 10 Mpc/h left the bispectrum 20σ off,
  reduced to 5σ with s_min = 0; the k_max = 0.5 P fit matched the
  hexadecapole below 0.4 h/Mpc, ξ_ℓ above 10 Mpc/h and the bispectrum at
  2σ [src: arXiv:2307.14197, Sect. 5]. The authors raise whether a survey
  then needs two mock sets, one per space [src: same].

### What the fitting choice does to the covariance
<!-- key: what-the-fitting-choice-does-to-the-covariance -->

- With the k_max = 0.5 fit, standard deviations agree with SLICS within 5%
  for s > 10 Mpc/h and k < 0.35 h/Mpc [src: arXiv:2307.14197, Sect. 5].
- Across the six fitting choices, the errors on two clustering-amplitude
  parameters vary by up to 20%, mostly 2–10% [src: abstract].

### More mocks or control variates
<!-- key: more-mocks-or-control-variates -->

- Gain: about an order of magnitude in covariance variance at
  k ≲ 0.05 h/Mpc, a factor 2–3 in convergence at higher k, for masked,
  redshift-space lognormal mocks resembling DESI LRGs [src:
  arXiv:2605.28817, abstract]; diminishing once the target–Zel'dovich
  correlation vanishes near k ≈ 0.2 h/Mpc [src: Sect. IV, summary].
- Cost: one Zel'dovich run per mock plus 10,000 for μ, all cheap.
- Limit: the test targets are lognormal mocks and the analytic β, ρ assume
  a Gaussian disconnected covariance [src: abstract]; a test with N-body
  or EZmock targets was not read.

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| COLA residual exponent | n_LPT = −2.5, ±0.5 harmless; refit per set-up | COLAcode | arXiv:1301.0322 | App. A.3.2 |
| Linear-growth error, one KDK step a = 0.1 → 0.2 | 1.5% | FastPM tests | arXiv:1603.00476 | Sect. 2.5 |
| FastPM matter field, N_s = 5 / 40 | r = 93% at k = 1 / T ≈ 98%, r ≈ 99% at k = 1 h/Mpc | vs RunPB, z = 0 | arXiv:1603.00476 | Sect. 3.2 |
| FastPM mass function | within 10% for N_s > 10; 80% (PM) and 60% (COLA) at N_s = 5 | vs RunPB | arXiv:1603.00476 | Sect. 3.2 |
| FastPM halo stochasticity, N_s = 10 | 10% (M > 10¹²) to 7% (M > 10¹⁴ M_⊙/h) | vs RunPB | arXiv:1603.00476 | Sect. 3.2 |
| Stochasticity from 0.23 dex mass scatter | 20%, for CMASS-like haloes | RunPB | arXiv:1603.00476 | Sect. 3.1 |
| Cost N_s = 10, B = 2 vs N_s = 40, B = 3 | about 10% of the CPU, nearly identical halo benchmarks | FastPM | arXiv:1603.00476 | Sect. 3.3 |
| ICE-COLA P(k) within 2% at z = 0 | k ≈ 0.4, 0.6, 0.8 h/Mpc for 10, 20, 40 steps | vs MICE-GC | arXiv:1509.04685 | Sect. 4.1 |
| ICE-COLA optimal set-up | 40 steps linear in a, z_i = 19, mesh factor 3; 1% to k = 0.8 (1.3) h/Mpc at z = 0 (1) | vs MICE-GC | arXiv:1509.04685 | Sect. 4.5 |
| Mesh factor 3 → 2 | −70% time, −30% memory; 5% mass function only above about 10¹³ M_⊙/h | ICE-COLA | arXiv:1509.04685 | Sect. 4.4 |
| Bias recalibration | δ ln b = 0.02 → bias within 1% to k ≲ 0.5 h/Mpc | ICE-COLA | arXiv:1509.04685 | Sect. 5.2 |
| EZmock free parameters | ρ_c, ρ_exp, b, ν (ρ_sat = λ = 10 fixed) | eBOSS | arXiv:2007.08997 | Table 1 |
| EZmock calibration scales | ξ: 10–50 Mpc/h; P: 0.1–0.3 h/Mpc; B(k_1 = 0.1, k_2 = 0.05) | eBOSS | arXiv:2007.08997 | Sect. 2.5 |
| EZmock grid | 1024³ in (5 Gpc/h)³ (eBOSS); 960³ in (2.5 Gpc/h)³ (2014) | eBOSS; BOSS CMASS | arXiv:2007.08997; arXiv:1409.1124 | Sect. 2.2.1; Sect. 3.1 |
| Tracers placed at random in cells | 6% LRG, 16% ELG, 4% QSO | eBOSS | arXiv:2007.08997 | Sect. 2.2.4 |
| FastPM HOD challenge | 6 parameters; fits to k_max = 0.3–0.5 h/Mpc or s_min = 0–10 Mpc/h; up to 20% spread in parameter errors | DESI ELG | arXiv:2307.14197 | Sects. 3.2–3.3, abstract |
| Control-variate gain | ≈ 10 at k ≲ 0.05 h/Mpc; 2–3 above; 1/(1 − ρ²) in general | DESI-LRG-like lognormal | arXiv:2605.28817 | abstract, Sect. II.2.2 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Too few steps before the output redshift.** Low halo masses and high
  bias at z ≈ 1 with 10 steps from z_i = 9 [src: arXiv:1509.04685,
  Sect. 3]. Test: count the steps before the redshift of the mock (at
  least 10) and compare the mass function with an N-body run.
- **Mass-function incompleteness hidden by abundance matching.** Matching
  repairs biased masses, not missing haloes, so bias stays wrong below the
  completeness mass [src: arXiv:1509.04685, Sects. 5.1–5.2]. Test: the mass
  function before matching, against the minimum host mass of the tracer.
- **COLA parameter carried over from another set-up.** n_LPT depends on
  z_i, box, mesh and particle load [src: arXiv:1301.0322, App. A.3.2].
  Test: refit it on a few realisations against the reference.
- **Smoothing in a pure PM force.** Removes low-mass haloes [src:
  arXiv:1603.00476, Sect. 2.1].
- **FoF bridging in low-contrast fields.** A shorter linking length, 0.168,
  changes bias and stochasticity by 2% only in the lightest bin
  (10¹² M_⊙/h) [src: arXiv:1603.00476, App. C].
- **Grid changed, parameters kept.** EZmock parameters are grid-specific
  [src: arXiv:2007.08997, Sect. 2.2.1]; too coarse a grid damps the BAO
  peak [src: arXiv:1409.1124, Sect. 3.1].
- **Fit in one space, used in the other.** The covariance of ξ from mocks
  fitted on P (or the reverse) differs, and the bispectrum can be 20σ off
  [src: arXiv:2307.14197, Sect. 5]. Test: compare both spaces and the
  bispectrum against the reference.
- **Calibration done on complete mocks, data analysed with systematics.**
  The eBOSS choice assumes systematics act outside the calibration scales
  [src: arXiv:2007.08997, Sect. 2.2.6]; a referee asks whether the analysis
  scales fall inside them.

Pass criteria stated by the papers: eBOSS validated on 50 realisations
after tuning on one [src: arXiv:2007.08997, Sect. 2.2.6]; the DESI
challenge required χ²_ν ≈ 1 against the paired-difference covariance and
1σ or 2σ agreement per statistic [src: arXiv:2307.14197, Sect. 5].

## Reading list
<!-- key: reading-list -->

- Review: Angulo & Hahn 2021, arXiv:2112.05165, Sect. 4.4 — COLA and FastPM
  as canonical transformations; open questions on convergence order.
- Foundation: Tassev et al. 2013, arXiv:1301.0322 — COLA equations, the
  n_LPT parameter, how to place the steps.
- Method: Feng et al. 2016, arXiv:1603.00476 — FastPM factors, force
  kernels, benchmarks (transfer function, r, stochasticity), N_s and B.
- Method: Izard et al. 2015, arXiv:1509.04685 — how to choose steps, time
  sampling, z_i and mesh for COLA; mass recalibration.
- Foundation: Chuang et al. 2014, arXiv:1409.1124 — the original EZmock
  recipe and why it fits statistics directly.
- Application: Zhao et al. 2020, arXiv:2007.08997 — the eBOSS bias function,
  calibration scales and survey effects step by step.
- Application: Forero-Sánchez et al. 2024, arXiv:2411.12027, Sect. 2.1 —
  DESI DR1 EZmocks on AbacusSummit targets.
- Method: Variu et al. 2023, arXiv:2307.14197 — HOD fitting on fast-mock
  haloes with paired initial conditions.
- Method: Hadzhiyska & White 2026, arXiv:2605.28817 — Zel'dovich control
  variates for mock covariances.
- Critique: Blot et al. 2018, arXiv:1806.09497 (in L2) — what seven methods
  get right on covariances.

## Not verified
<!-- key: not-verified -->

- The FastPM kick factor of Eq. 25 was cut in the text read; its form is
  given here by analogy with the drift factor, as the paper's Eqs. 19–20
  define G_f.
- The second-generation EZmocks and any FastPM or AbacusSummit-based mock
  sets of DESI DR2: not read. The DESI DR2 reference mocks on Uchuu
  (arXiv:2507.01593, arXiv:2606.28559) are abundance-matching mocks, seen
  by title only.
- Klypin & Prada 2018a on time stepping without modified factors: cited
  through the review only.
- The Gaia-unWISE quasar mocks from augmented LPT with a hierarchical
  non-local bias (Sinigaglia et al. 2025, arXiv:2509.15890): abstract read
  only.
- A control-variate test on N-body or EZmock targets: none found.
