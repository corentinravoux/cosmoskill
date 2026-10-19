# N-body accuracy settings and convergence — cosmo-simulations-mocks dossier

Scope: how the accuracy parameters of a gravity-only run are chosen
(softening length and law, time-step criterion and parameter, tree opening
angle, mesh size and force split) and how a convergence test is designed
and read, for the matter power spectrum and for halo properties, with the
settings the code comparisons actually used and what each choice was
found to cost.
Snapshot: 2026-10-19.
From: Angulo & Hahn 2021 review (arXiv:2112.05165), Sects. 3–5, 8.1, 8.5;
Crain & van de Voort 2023 review (arXiv:2309.17075), Sect. 2.5.

Already in L2, not repeated here: the force solvers and codes with their
papers (`physics-and-methods.md#n-body-methods-and-codes`), the agreement
levels of the code comparisons and their history
(`results.md#code-comparison-agreement-levels`), the box-size and
mass-resolution requirements of the Euclid comparison, the k_sn/3 rule, the
Aemulus halo-mass-function deficit, the Klypin & Prada box-size study, the
Euclid "standard" settings and the DESI comparison results
(`systematics.md#resolution-and-box-size-effects`,
`systematics.md#initial-condition-and-time-stepping-errors`). Initial
conditions (LPT order, starting redshift) are in the same L2 sections;
halo-finder settings in `deep/halo-finding.md`; hydrodynamical convergence
in `deep/hydro-subgrid-calibration.md`.

Symbols used throughout. ℓ = (V/N)^{1/3}: mean inter-particle separation;
ε: softening length (ε_p Plummer-equivalent, ε_s spline); r_200, N_200,
V_200: radius, particle number and circular velocity of a halo at 200
times the critical density; Δt: time step; η: dimensionless time-step
parameter; A_i or a_i: acceleration of particle i; θ: tree opening angle;
N_g, N_p: numbers of mesh points and particles; H_g, H_p: mesh spacing and
mean particle spacing (GINKAKU notation, H_p = ℓ); r_s: tree–mesh force
split scale; ε_g = r_s/H_g.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Choose the softening law and length
<!-- key: step-1-choose-the-softening-law-and-length -->

**Law.** Plummer softening replaces the Green's function of the
acceleration by −r/[4π(r² + ε²)^{3/2}]; it is only asymptotically Newtonian,
and peaks at r = ε/√2 [src: arXiv:2112.05165, Sect. 8.2, Eqs. 108–109].
Kernel or spline softenings become exactly Newtonian at a few softening
lengths [src: Sect. 8.2]. Abacus uses a single-split spline,
F = [10 − 15(r/ε_s) + 6(r/ε_s)²] r/ε_s³ for r < ε_s and r/r³ beyond,
derived from a Taylor expansion of Plummer softening with a smooth
transition up to the second derivative; the reason given is that Plummer
softening "affects the growth of structure on scales many times larger
than ε_p" and is inconsistent with the 1/r² far field [src:
arXiv:2110.11392, Sect. III.2, Eqs. 2–3]. A softening is always specified
as its Plummer equivalent and converted so that both give the same minimum
pairwise orbital time; for the Abacus spline ε_s = 2.16 ε_p [src: Sect.
III.2].

**Length.** The review lists four kinds of criterion [src:
arXiv:2112.05165, Sect. 8.2 and Fig. 22]:

- the coarse-graining argument, ε ∼ ℓ, which would make haloes of 100
  particles (virial radius ≈ 0.3 ℓ) unresolved, so that large runs use
  values 30–100 times smaller;
- collisionality bounds (ε_v from the binding energy of two particles at
  separation ε, ε_acc from the change of acceleration in an encounter,
  ε_90 from large-angle deflections), called "qualitative estimates";
- two-body relaxation: profiles converge to about 10% where the
  relaxation time of the enclosed particles exceeds the Hubble time
  (Power et al. 2002, below);
- empirical "optimal" values, compared in the table below.

| Prescription | Form | In units of ℓ | Basis | Place read |
|---|---|---|---|---|
| Power et al. 2002 | ε_opt = 4 r_200/√N_200 | ≈ 0.03 | profiles of one galaxy-sized halo; minimises the number of steps | arXiv:astro-ph/0201544, Sect. 3.4 (Eq. 15); arXiv:2112.05165, Sect. 8.2 |
| Zhang et al. 2018 | ε_opt = 2 r_200/√N_200 | — | P03 "works well but is over conservative"; too small ε overpredicts inner density | arXiv:1810.07055, abstract; arXiv:2112.05165, Sect. 8.2 |
| van den Bosch & Ogiya 2018 | ε_opt/r_200 ≈ 2.3 N_200^{−1/3} | ≈ 0.017 | subhaloes under 1000 particles artificially disrupted | [sec: arXiv:2112.05165, Sect. 8.2, Fig. 22]; [sec: arXiv:2008.08591, Eq. 21] |
| Mansfield & Avestruz 2020 | — | ≈ 0.008 | V_max bias below sample variance in their model | arXiv:2008.08591, Sect. 6.2, Eq. 22 |
| Garrison et al. 2021 (scale-free tests) | fixed in physical coordinates | 0.033 | self-similarity of scale-free runs | [sec: arXiv:2112.05165, Sect. 8.2] |

Values used in large runs, in units of ℓ: Bolshoi 0.016, MultiDark
0.015–0.026, the Millennium runs 0.022, Euclid Flagship 0.02 [sec:
arXiv:2112.05165, Sect. 8.2]; AbacusSummit and the DESI comparison Abacus
runs 1/40 (0.025) in proper coordinates, capped at 0.3 at early times;
GADGET-2 and SWIFT in the DESI comparison 1/25 (0.04) comoving, Plummer
equivalent [src: arXiv:2112.09138, Sects. 3.1.1–3.1.3]. Power et al.
explain why a single value cannot be optimal: ε_opt ∝ r_200/N_200^{1/2} ∝
N_200^{−1/6}, so a value optimal for the most massive haloes is too small
for the others [src: arXiv:astro-ph/0201544, Sect. 5.1]. Mansfield &
Avestruz add that their 0.008 rests on V_max only, that properties set
inside R_max need smaller ε, that their suites did not establish a
converged range of ε, and that standard time stepping can contract haloes
for ε somewhat below 0.008 [src: arXiv:2008.08591, Sect. 6.2].

Comoving or physical. Fixing ε in physical coordinates, usual in zoom and
hydrodynamical runs, makes the Hamiltonian time-dependent; the review
judges the error acceptable for large runs, with the gain of fewer time
steps at high redshift [src: arXiv:2112.05165, Sect. 8.2]. The scale-free
tests of Garrison et al. found that physical softening uses fewer steps at
fixed error budget [sec: arXiv:2110.11392, Sect. III.1].

### Step 2. Choose the time-step criterion and its parameter
<!-- key: step-2-choose-the-time-step-criterion-and-its -->

The criteria in use [src: arXiv:2112.05165, Sect. 4.2.1, Eqs. 44–47]:

- CFL-like, Δt_i = C Δx/|P_i/M_i|, C ∼ 0.25, or C √(Δx/|A_i|), the latter
  common in PM codes;
- the acceleration criterion Δt_i ≃ η √(ε/|A_i|), "the most common" in
  large runs, used by PKDGRAV-3 with η = 0.2 and by GADGET;
- a tidal criterion Δt_i ≃ η/√‖T‖, with T the tidal tensor, which avoids
  the non-physical scale ε and gives shorter steps in halo centres and
  longer ones outside, at the cost of a noisier estimate;
- a global cap Δ log a < B, B ∼ 0.01, used in PM and COLA codes and, with
  the others, in high-resolution runs because it "appears to be necessary
  for a precise agreement with linear theory predictions at high
  redshift".

The review states that the choices are "usually heuristically motivated",
that a factor 4 in CPU time was saved by adjusting steps while keeping
P(k) and the mass function after a mass correction, and that no systematic
study of the optimal strategy for large-scale simulations at the accuracy
of upcoming surveys has been published [src: Sect. 4.2.1]. Block
(hierarchical) time steps, ε_ℓ = 2^{−ℓ} ε₀ per level, are used by
PKDGRAV-3 and GADGET; GADGET-4 computes the kick on level ℓ from particles
on levels ≥ ℓ only [src: Sect. 4.2.2, Eq. 48].

Power et al. compared criteria on one halo: all deliver convergence at
comparable cost, the acceleration-and-softening criterion Δt_i =
η √(ε_i/a_i) with η ∼ 0.2 being the most efficient; criteria without ε need
η reduced as ε is reduced below ε_opt; multi-stepping beats a single step
"only for softenings well below the optimal value" [src:
arXiv:astro-ph/0201544, Sects. 4.4 and 7].

Abacus uses one global step chosen at each step from the ratio of the RMS
velocity to the maximum acceleration in each cell, the most conservative
cell setting Δa, with a global ratio as a guard against abnormally cold
cells and a cap η_H a of about 33 steps per e-fold; the result is about
1100 steps for AbacusSummit [src: arXiv:2110.11392, Sect. III.1, Eq. 1].
With η = 0.25 the small-scale correlation function misses about 1% at
twice the softening length against an 8000-step reference; the authors
expect O(1000) steps to suffice for applications that marginalise over
halo interiors, but not if steps were fixed in a or log a [src: Sect.
III.1]. The DESI comparison used η_Accel = 0.25, "mildly more
conservative" than the 0.3 of the Abacus Euclid run [src:
arXiv:2112.09138, Sect. 3.1.1].

### Step 3. Set the force accuracy: opening angle, mesh, split scale
<!-- key: step-3-set-the-force-accuracy-opening-angle -->

- **GADGET-type TreePM.** In the DESI comparison: mesh of N³ for N³
  particles, ErrTolTheta = 0.5, ErrTolForceAcc = 0.0025,
  MaxRMSDisplacementFac = 0.2, MaxSizeTimestep = 0.01, global steps even in
  log a with shorter steps for large accelerations [src: arXiv:2112.09138,
  Sect. 3.1.2]. In GADGET a rare tail of large tree errors, when open
  nodes are not guaranteed to exclude the particle, slows convergence;
  without the compile-time option that forbids it, f_acc ≲ 0.003 is needed,
  with it there is almost no trend even for f_acc ≈ 1 [src:
  arXiv:astro-ph/0201544, Sect. 5.3].
- **SWIFT.** FMM plus a periodic mesh; mesh of 648³ for 1296³ and 2592³
  particles and 864³ for 1728³, "the largest allowed by the code which
  would not introduce aliasing with the initial particle grid" [src:
  arXiv:2112.09138, Sect. 3.1.3].
- **PKDGRAV3** in the GINKAKU comparison: opening angle 0.4 at z > 20,
  0.55 at 2 < z < 20 and 0.7 at z < 2; fifth-order FMM; η = 0.15 in
  Δt_i = η √(ε_p H_p/|a_i|) [src: arXiv:2605.28581, Sect. 4.2, table
  notes].
- **Abacus.** Multipole order p = 8, 405³ cells in the DESI runs [src:
  arXiv:2112.09138, Sect. 3.1.1]; median force error 1.2 × 10⁻⁶ on a z = 0
  ΛCDM snapshot (512³ in 150 h⁻¹ Mpc) against an order-16 double-precision
  reference, with rare 0.1% islands and a 1% far-field tail where a halo
  straddles the near/far transition, absent in the total force [src:
  arXiv:2110.11392, Sect. III.5.4].

### Step 4. Explore softening and time step jointly
<!-- key: step-4-explore-softening-and-time-step-jointly -->

GINKAKU varied ε_p and a global time-step multiplier η_global together,
on 500³-particle runs in three box sizes, against a reference with
ε_p = 0.43% of H_p and η_global = 0.1 [src: arXiv:2605.28581, Sect.
4.1.1]. Its reasons: below some ε at fixed Δt, two-body scattering is
expected to contaminate small scales, and earlier studies varied ε at fixed
time-step criterion, so the two effects were not separated. Findings: at
the fiducial step, P(k) depends non-monotonically on ε, with the least
suppression at ε_p = 1.71% of H_p, adopted for the "accurate" setting; with
steps ten times shorter, P(k) rises monotonically as ε decreases, down to
0.43%, "roughly an order of magnitude below the ∼ 5% ansatz commonly
adopted", "with no indication of spurious two-body collisionality" [src:
Sect. 4.1.1]. At fixed resolution θ = 0.5 suffices for 1% to the Nyquist
wavenumber, the dependence on θ being strongest in the highest-resolution
box [src: Sect. 4.1.2]. With a coarse mesh (N_g = N_p/2³) the tree covers
more scales and θ = 0.5 suppresses small-scale power; for N_g < N_p the
authors recommend ε_g ≳ 4.5 with θ ≲ 0.3 [src: Sect. 4.1.4]. The
remaining difference between L-GADGET2 and GINKAKU, both TreePM, decays as
η_global is lowered in both, which traces it to individual against global
time steps [src: App. C].

### Step 5. Design the convergence test
<!-- key: step-5-design-the-convergence-test -->

What the sources do, in the order they apply it:

1. **Same phases, one parameter at a time, then jointly.** Every test read
   fixes the initial phases so that cosmic variance cancels in ratios
   (arXiv:2605.28581, Sect. 4.2; arXiv:2112.09138, Sect. 3.2). Power et
   al. checked that doubling or halving the step number or the starting
   redshift had no effect before varying ε [src: arXiv:astro-ph/0201544,
   Sect. 5.1]; GINKAKU shows that ε and Δt must then be explored together
   (Step 4).
2. **Reference far beyond production settings.** Abacus: 8000 steps
   (arXiv:2110.11392, Sect. III.1); GINKAKU: ε_p = 0.43%, η_global = 0.1,
   θ = 0.1 (arXiv:2605.28581, Sects. 4.1.1–4.1.2).
3. **Check large scales against perturbation theory, not linear
   rescaling.** The DESI codes agree at low k within 0.1%; rescaling the
   initial spectrum by the growth factor did not reproduce the large-scale
   power at sub-percent level, which the authors attribute likely to mode
   coupling, while 2LPT evolved to low redshift did; this test exposed a
   0.5% large-scale growth error in SWIFT from incorrect force integration
   [src: arXiv:2112.09138, Sect. 3.2].
4. **Scale-free self-similarity.** In an n = −2 scale-free run, finite
   mass resolution sets a lower bound of about 5% on the error at 3ε to 6ε
   for epochs typical of ΛCDM runs, an order of magnitude above the
   < 0.5% time-step error for η ≤ 0.2 [sec: arXiv:2110.11392, Sect. III.1,
   describing Joyce et al. 2020, not read]; self-similarity is used by
   Garrison et al. 2021 to tune ε (same place).
5. **Halo properties against higher-resolution suites.** Mansfield &
   Avestruz compare each simulation's mean relation X(M_vir) with a
   combined fit to higher-resolution suites, separately for isolated haloes
   and subhaloes and per cosmology, and call a mass "unconverged" where a
   z-test with tolerance δ rejects agreement at p < 0.05; the conservative
   limit of a property is the N_vir at which 90% of simulations show no
   deviation [src: arXiv:2008.08591, Sects. 2.5 and 3.1].
6. **Converged radius of a halo profile.** Converged to better than 10% in
   mass where r > ε, the enclosed number exceeds 100 and
   a(r) = V_c²/r ≲ a_ε = χ_ε V_200²/ε with χ_ε ∼ 0.5; with ε ≈ ε_opt, the
   minimum converged radius obeys t_circ(r_conv) ≈ 15 (Δt/t₀)^{5/6}
   t_circ(r_200) [src: arXiv:astro-ph/0201544, Sect. 7, Eq. 16]. A worked
   example: 3 × 10⁶ particles inside r_200, r_conv = 0.005 r_200,
   ε = 0.0025 r_200, about 5000 equal steps or η = 0.15, z_i = 49 [src:
   Sect. 5.5].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Large or small softening
<!-- key: large-or-small-softening -->

Large ε (≈ ε_opt of Power et al.) minimises steps and discreteness but
biases halo interiors: Mansfield & Avestruz find that haloes simulated at
ε_opt "exhibit large biases at the particle counts that cosmological
simulations typically consider", and that V_max, shape c/a and subhalo
abundances depend strongly on ε, with biases comparable to the effect of
baryons [src: arXiv:2008.08591, Sects. 6.2 and 7]. Multidark and
IllustrisTNG-Dark have converged internally to different solutions, which
the authors attribute mostly to softening [src: Sect. 7]. Small ε needs
proportionally short steps: Power et al. find that profiles at
ε ≈ 12 h⁻¹ kpc (just above ε_opt) deviate out to more than five softening
lengths whereas ε ≈ 6 h⁻¹ kpc converges almost to one softening length,
so "assuming that mass profiles are affected out to a certain multiple of
the softening length is an oversimplification" [src:
arXiv:astro-ph/0201544, Sect. 5.1]; GINKAKU sees no collisional signature
in P(k) down to 0.43% of H_p once steps are shortened (Step 4). For the
matter P(k) alone the choice matters less than for halo properties: the
DESI codes, with ε of 1/40 and 1/25 of ℓ, agree within 1% to
k = 10 h/Mpc (L2).

In hydrodynamical runs the sensitivity is stronger: softening imposes a
minimum resolved escape speed, feedback can over-cool below a critical ε,
and small ε segregates stars and dark matter in halo centres, so that
galaxy sizes can grow as ε shrinks [src: arXiv:1908.05019, abstract].

### Global or individual time steps
<!-- key: global-or-individual-time-steps -->

A global step (Abacus, GINKAKU) is set by the densest region and wastes
work elsewhere; Abacus takes about 1100 steps where sub-cycling codes take
"up to a few times more steps at the finest level" [src:
arXiv:2110.11392, Sect. III.1]. Individual block steps are favoured when ε
is well below optimal [src: arXiv:astro-ph/0201544, Sect. 4.4]. The two
schemes are a measurable source of code-to-code difference in P(k) at
standard settings, vanishing as steps shrink [src: arXiv:2605.28581, App.
C]. Mansfield & Avestruz conclude that commonly used time stepping is
unlikely to bias halo properties significantly, while listing open
questions [src: arXiv:2008.08591, Sect. 7].

### Mesh size against tree accuracy
<!-- key: mesh-size-against-tree-accuracy -->

In TreePM the mesh size changes P(k) by more than 1%, more than most other
parameters, and non-monotonically, in studies that kept ε_g fixed; a mesh
of 2N_p^{1/3} per dimension was suggested from comparisons with EFT [sec:
arXiv:2605.28581, Sect. 4.1.3, describing Smith et al. 2014 and Baldauf et
al. 2015]. GINKAKU's standard is N_g = 2³ N_p; a coarse mesh to save memory
requires a larger split scale and a smaller opening angle (Step 4).

### Tune to agree or tune to converge
<!-- key: tune-to-agree-or-tune-to-converge -->

The Euclid comparison warns that codes could be tuned into agreement on a
wrong answer (L2). GINKAKU set its fiducial parameters "to roughly
reproduce the L-GADGET2 runs" of the Dark Quest I suite, and its accurate
setting from internal convergence against a stricter reference [src:
arXiv:2605.28581, App. C and Sect. 4.1.1]; the second is the convergence
statement, the first a consistency statement.

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Abacus spline ↔ Plummer | ε_s = 2.16 ε_p | Abacus | arXiv:2110.11392 | Sect. III.2 |
| Abacus steps | ≈ 1100 (AbacusSummit); η_H ≈ 33 steps per e-fold | AbacusSummit | arXiv:2110.11392 | Sect. III.1 |
| Abacus time-step error | ≈ 1% on ξ at 2ε for η = 0.25; < 0.5% for η ≤ 0.2 | 8000-step reference | arXiv:2110.11392 | Sect. III.1 |
| DESI comparison, Abacus | ε = ℓ/40 proper (cap 0.3 ℓ), p = 8, 405³ cells, η_Accel = 0.25 | DESI N-body project | arXiv:2112.09138 | Sect. 3.1.1 |
| DESI comparison, GADGET-2 | mesh N³, ε_p = ℓ/25 comoving, ErrTolTheta 0.5, ErrTolForceAcc 0.0025, MaxSizeTimestep 0.01 | DESI N-body project | arXiv:2112.09138 | Sect. 3.1.2 |
| DESI comparison, SWIFT | mesh 648³ (1296³, 2592³ particles), 864³ (1728³), ε_p = ℓ/25 | DESI N-body project | arXiv:2112.09138 | Sect. 3.1.3 |
| PKDGRAV3 settings | θ = 0.4 / 0.55 / 0.7 at z > 20 / 2–20 / < 2; η = 0.15 | GINKAKU comparison | arXiv:2605.28581 | Sect. 4.2 |
| GINKAKU accurate ε_p | 1.71% of H_p; reference 0.43%, η_global = 0.1 | 500³ runs, 3 boxes | arXiv:2605.28581 | Sect. 4.1.1 |
| GINKAKU opening angle | θ = 0.5 for 1% to Nyquist at N_g = 2³N_p; θ ≲ 0.3 with ε_g ≳ 4.5 if N_g < N_p | — | arXiv:2605.28581 | Sects. 4.1.2, 4.1.4 |
| Power et al. criteria | ε_acc = r_200/√N_200; ε_opt = 4 ε_acc; η ∼ 0.2; χ_ε ∼ 0.5 | one galaxy-sized halo | arXiv:astro-ph/0201544 | Sect. 7 |
| GADGET tree tolerance | f_acc ≲ 0.003 without the node-exclusion option | — | arXiv:astro-ph/0201544 | Sect. 5.3 |
| Softening in large runs | 0.016 (Bolshoi), 0.015–0.026 (MultiDark), 0.022 (Millennium), 0.02 (Euclid Flagship) of ℓ | — | arXiv:2112.05165 | Sect. 8.2 |
| Halo-property convergence | V_max, c/a need N_vir ≈ 10⁵–10⁶ for high agreement | many public suites | arXiv:2008.08591 | Sect. 7 |
| Global step cap | Δ log a < B, B ∼ 0.01 | review | arXiv:2112.05165 | Sect. 4.2.1, Eq. 47 |
| Abacus force error | median 1.2 × 10⁻⁶, ΛCDM z = 0 | — | arXiv:2110.11392 | Sect. III.5.4 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Softening varied at a fixed step.** P(k) then responds
  non-monotonically to ε and an apparent optimum appears that disappears
  with shorter steps; vary both (arXiv:2605.28581, Sect. 4.1.1).
- **One softening for all haloes.** ε_opt scales as N_200^{−1/6}, so a
  run tuned for clusters is under-softened for small haloes; quote halo
  properties only above the convergence limit of the property
  (arXiv:astro-ph/0201544, Sect. 5.1; arXiv:2008.08591, Table 3).
- **"Converged" by internal resolution steps only.** Two suites can each
  converge internally to different halo properties because of their
  softening; compare with an independent suite (arXiv:2008.08591, Sect.
  3.3).
- **Large-scale growth errors.** A sub-percent offset at low k is caught
  by comparing with 2LPT evolved to the output redshift on the same phases;
  linear rescaling is not precise enough (arXiv:2112.09138, Sect. 3.2).
- **Rare large tree errors.** A tail of force errors in tree walks biases
  halo centres; test the cumulative force-error distribution against a
  high-accuracy reference (arXiv:astro-ph/0201544, Sect. 5.3;
  arXiv:2110.11392, Sect. III.5.4).
- **Aliasing with the particle grid.** A mesh that aliases with the
  initial lattice is avoided in SWIFT by its mesh-size choice
  (arXiv:2112.09138, Sect. 3.1.3).
- **Coarse mesh with default θ.** Small-scale power is suppressed when the
  tree carries more of the force than the default opening angle can
  support (arXiv:2605.28581, Sect. 4.1.4).
- **Assuming time steps dominate.** For Abacus settings, mass resolution
  and softening dominate the small-scale error budget, not the step
  (arXiv:2110.11392, Sect. III.1).

## Reading list
<!-- key: reading-list -->

- Review: Angulo & Hahn 2021, arXiv:2112.05165, Sects. 4.2 and 8.1–8.2 —
  time-step criteria, softening criteria and the values large runs use.
- Foundation: Power et al. 2002, arXiv:astro-ph/0201544 — softening,
  time step, force accuracy and convergence radius for halo profiles.
- Method: Garrison et al. 2021, arXiv:2110.11392, Sects. III.1–III.5 —
  spline softening, a global step criterion and force-error tests.
- Method: Nishimichi et al. 2026, arXiv:2605.28581, Sect. 4 and App. C —
  joint softening and time-step study, tree and mesh accuracy.
- Application: Grove et al. 2021, arXiv:2112.09138, Sect. 3 — the
  settings three codes used for DESI, and the large-scale growth test.
- Critique: Mansfield & Avestruz 2020, arXiv:2008.08591 — convergence
  limits of halo properties and their softening dependence.
- Critique: Zhang et al. 2018, arXiv:1810.07055 — a less conservative
  optimal softening.
- Critique: Ludlow et al. 2019, arXiv:1908.05019 — softening in
  hydrodynamical runs.
- Comparison: Schneider et al. 2015, arXiv:1503.05920 (in L2) — box,
  resolution and code requirements for 1% on P(k).

## Not verified
<!-- key: not-verified -->

- Joyce et al. 2020 and Garrison et al. 2021 (scale-free self-similarity
  and the 0.033 ℓ physical softening): read only as described by the review
  and the Abacus paper; identifiers not retrieved.
- van den Bosch & Ogiya 2018, Green et al. 2021 (artificial subhalo
  disruption, at most 10–20% on the subhalo mass function according to the
  review), Smith et al. 2014 and Baldauf et al. 2015 (mesh size): through
  the review and the GINKAKU paper only.
- The review states that Schneider et al. (2016, the journal year of
  arXiv:1503.05920) require 10⁹ h⁻¹ M_⊙ for percent-level convergence at
  k ∼ 1 h/Mpc [sec: arXiv:2112.05165, Sect. 8.1]; the paper body, as read
  in `systematics.md#resolution-and-box-size-effects`, gives 10⁹ M_⊙/h for
  1% up to k = 10 h/Mpc and about 8 × 10¹⁰ M_⊙/h for k ≤ 1 h/Mpc. The
  difference is left unresolved here; the paper body is the primary source.
- The GINKAKU convergence table (Sect. 4.2) was printed garbled; only its
  footnotes are quoted.
- Time-integration schemes beyond KDK leapfrog and block steps
  (symplectic higher-order, tidal criteria in production): not read.
