# Constrained simulations — cosmo-simulations-mocks dossier

Scope: how a constrained simulation of the local or survey volume is built
once the constraints exist (linear constrained realisations from peculiar
velocities with the reverse Zel'dovich step, conversion of a field-level
posterior into particle initial conditions, the small-scale completion,
tiling of the inference, the resimulation set-up), how simulated objects
are matched to named observed ones across an ensemble, and how such a
suite is validated. Each step gives the BORG/Manticore implementation
beside its peers: CLUES and its CLONES, HESTIA and SLOW suites on
Cosmicflows-2, Hamlet and Hamlet-PM on Cosmicflows-4, ELUCID on SDSS
groups, KIGEN on 2MRS, and the linear and neural reconstructions used as
benchmarks.
Snapshot: 2026-10-21.
From: Angulo & Hahn 2021 review (arXiv:2112.05165), Sect. 6.3.7.

Already in L2, not repeated here: the two families of methods with their
founding papers, the Hoffman–Ribak formula, the table of field-level steps
from ARGO to DISCO-DJ, the headline results of CLUES, SIBELIUS-DARK,
Manticore-Local, Manticore-Deep and Hamlet-PM, and the list of validation
types (`physics-and-methods.md#constrained-simulations-and-reconstructions-of`,
`surveys-and-data.md#constrained-simulations-of-the-local-universe`,
`results.md#constrained-simulations-quantified-results`,
`systematics.md#constrained-simulation-limits`). How the posterior of the
initial field is sampled (parametrisation, likelihood, sampler, mass
matrix, convergence) is in
`cosmo-beyond-two-point/deep/field-level-inference.md`; the use of a
reconstructed velocity field to measure fσ8 is in
`cosmo-peculiar-velocities/deep/velocity-density-comparison.md`.

Symbols used throughout. x: white-noise field of the initial conditions;
δ: density contrast; v: peculiar velocity; Ψ: Lagrangian displacement;
f = d ln D/d ln a: linear growth rate; C_i: constraints (data) with their
errors; WF: Wiener filter; CR: constrained realisation; RZA: reverse
Zel'dovich approximation; L_WNF: cell size of the inferred white-noise
field; LUM: the probabilistic Local Universe Model used for counterpart
matching.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Decide where the constraints come from
<!-- key: step-1-decide-where-the-constraints-come-from -->

Two routes deliver the large-scale initial field, and the rest of the
pipeline depends on which one is used.

- **Linear constraints from peculiar velocities (CLUES).** No sampling of
  the initial field: a Wiener filter, a reverse Zel'dovich step and the
  Hoffman–Ribak algorithm turn radial velocities into a constrained
  Gaussian field, under a prior power spectrum (step 2).
- **A field-level posterior from galaxy positions (BORG and its
  successors).** The inference returns a Markov chain of white-noise fields
  on a coarse grid; each thinned sample is one constrained initial
  condition (steps 3–4).
- **A field-level posterior from peculiar velocities (Hamlet-PM).** The
  forward model of the second route applied to the data of the first: the
  initial field is sampled by Hamiltonian Monte Carlo with the
  differentiable particle-mesh code pmwd inside the likelihood (128³
  particles in 500 h⁻¹ Mpc, 3.9 h⁻¹ Mpc force resolution, 2LPT to z = 19
  then 5 PM steps), and the model velocity is a hybrid of the
  cloud-in-cell velocity in populated cells and the linear velocity of the
  non-linear density in nearly empty ones, where the cloud-in-cell velocity
  is undefined [src: arXiv:2602.03699, Sect. 3.3, Eqs. 12–14]. The data are
  the grouped Cosmicflows-4 (about 56,000 galaxies in more than 38,000
  groups), cut at cz = 16,500 km/s; the median signal-to-noise of a peculiar
  velocity is below 10%, and the 0.1 mag inter-calibration uncertainty
  between CF4 sub-catalogues is not addressed [src: Sect. 2].

- **A field-level posterior from a group-based density (ELUCID).** The
  data are not galaxies but SDSS DR7 groups: their redshift distortions
  are removed with linear theory applied to the group density (two
  iterations, smoothing at a mass scale of 10^14.75 h⁻¹ M_⊙; mean
  position offset 1.1–1.4 h⁻¹ Mpc on mocks), and a present-day density is
  built by "convolving" each group above a mass threshold with the mean
  density profile of haloes of its mass within their domain, measured in
  eight N-body runs; that field is 10–20% low in power on some scales and
  is corrected by C_p(k) = √(P_sim/P_hd) [src: arXiv:1608.01763, Sects.
  II.2–II.3]. HMC then infers the linear field with a Gaussian likelihood
  of the PM-evolved density against it (σ_hd = 0.5 ρ_hd, zero weight
  outside the survey and a down-weighted boundary layer) [src: Sect. II.4,
  Eq. 1].

Reconstructions that stop before any simulation are the benchmarks these
routes are scored against (Step 7). The linear 2M++ field of Carrick et
al. 2015 places galaxies by an iterative scheme after Yahil et al. 1991:
friends-of-friends groups collapsed against fingers of God, β* raised
"adiabatically" from 0 to 1 in steps of 0.01, at each step a Schechter fit
for luminosity weights, cloning across the Zone of Avoidance, a
4 h⁻¹ Mpc Gaussian smoothing, linear velocities, and the last five
distance predictions averaged to damp triple-valued regions; the scheme
returned an unbiased β* on an N-body test [src: arXiv:1504.04627, Sect.
2.5]. Against Tully–Fisher and supernova velocities it gives
β* = 0.431 ± 0.021 and an external bulk flow of 159 ± 23 km/s preferred at
5.1σ [src: arXiv:1504.04627].

The SLOW authors place the families in the same way: the Hoffman–Ribak
route "goes backwards in time", the Bayesian forward-modelling route
(Kitaura et al., ELUCID, SIBELIUS) was developed over the last decade; the
earliest constrained simulations used redshift-survey densities instead,
for example a 240 h⁻¹ Mpc box with a 160 h⁻¹ Mpc-diameter high-resolution
sphere (Mathis et al. 2002, as cited), and velocities have the advantage
of tracing the potential of all matter independently of the tracer, at the
price of much smaller catalogues with large distance errors [src:
arXiv:2302.10960, Sect. 2].

### Step 2. Linear route: WF, RZA, CR, then a resolution increase
<!-- key: step-2-linear-route-wf-rza-cr-then-a-resolution -->

The CLUES procedure for Cosmicflows-2, as its paper writes it [src:
arXiv:1510.04900, Sect. 2.3, Eqs. 1–4]:

1. Wiener-filter velocity, v^WF_α(r) = Σ_i ⟨v_α(r) C_i⟩ Σ_j ⟨C_i C_j⟩⁻¹ C_j,
   and displacement Ψ^WF = v^WF / (H₀ f(t_init)), the correlation functions
   depending only on the prior power spectrum (Eq. 1).
2. Reverse Zel'dovich: move each constraint to the position of its
   progenitor, x^RZA_init = r − Ψ^WF, and replace its noisy radial velocity
   by the full three-component WF velocity (Eq. 2); linear theory at first
   order is taken as valid down to 2 h⁻¹ Mpc.
3. Constrained realisation:
   δ^CR(r) = δ^RR(r) + Σ_i ⟨δ(r) C_i⟩ Σ_j ⟨C_i C_j⟩⁻¹ (C_j − C̄_j), with
   δ^RR a random realisation and C̄_j the constraint values in it; the
   initial velocity follows from ∇·v(t_init) = −ȧ f δ^CR (Eq. 3).
4. Convert δ^CR to white noise with δ(k) = √(P(k) V) ω(k), add random small-
   scale modes, and convert back at higher resolution (Eq. 4).

Why the reverse step. The constrained realisation is "formulated in an
Eulerian way": it ignores the displacement between where galaxies are
today and where their progenitors were, so constraints are relocated first
[src: arXiv:1311.2253, Sect. 2]. The RZA position is
r_init = r − v/(H₀ f), from the Zel'dovich displacement and v = H₀ f Ψ at
z = 0 [src: App. B, Eqs. 5–9]. Two refinements were compared on mocks
(step "RZA3D" against "RZA-radial"): using WF three-component velocities
as constraints and building the initial conditions with null errors, to
avoid suppressing the signal twice (once by the WF, once by the CR) [src:
Sect. 2]. A σ_NL term in the data covariance absorbs non-linear radial
velocities [src: Sect. 2]. The RZA papers quantify the gain on mocks: the
progenitor positions of grouped tracers are recovered with a median error
of 1.36 h⁻¹ Mpc, 5 h⁻¹ Mpc for realistic sparse, noisy data, against errors
of 10 h⁻¹ Mpc or more when the displacement is neglected [src: Doumler et
al. 2013a, arXiv:1212.2806]; resimulations then recover haloes down to
about 10¹⁴ h⁻¹ M_⊙ within about 2 h⁻¹ Mpc and a factor 2 in mass, whereas
CR without RZA recovers only haloes above about 5 × 10¹⁴ h⁻¹ M_⊙, shifted
by about 10 h⁻¹ Mpc [src: Doumler et al. 2013c, arXiv:1212.2810].

Before step 1, the catalogue is debiased: the four distance biases of
Cosmicflows-2 (the selection bias, already nulled in the catalogue; the
homogeneous and inhomogeneous Malmquist biases; the lognormal error
distribution) "lead mainly to a major infall onto the Local Volume", and an
iterative method minimises that infall and the spurious non-Gaussianity of
the radial-velocity distribution [src: arXiv:1510.04900, Sect. 2.2].

Periodic boxes keep only the divergent part of the velocity field (motions
due to densities inside the box), so tidal flows from outside are removed
[src: arXiv:1311.2253, Sect. 4.2].

The same six steps (grouping, bias minimisation, WF, RZA, CR, resolution
increase) build the initial conditions of the CLONES boxes used by SLOW
and of HESTIA, both on Cosmicflows-2, but with different groupings of the
same catalogue: 5562 galaxies and groups for SLOW (Sorce & Tempel 2018, as
cited), "the original grouping proposed for CF2" giving 4837 data points
for HESTIA [src: arXiv:2402.01834, Sect. 2.1; arXiv:2008.04926, Sect.
2.1]. Grouping "filters the non-linear component of the large scale
velocity field" [src: arXiv:2008.04926, Sect. 2.1]. SLOW places the linear
threshold at 3–4 Mpc, below which there is "no reason to work with density
and velocity fields with resolution higher than that of the galaxy groups
and clusters", and adds small-scale features with Ginnungagap [src:
arXiv:2402.01834, Sect. 2.1]. HESTIA stresses why the CR step cannot be
dropped: with very noisy, incomplete data "the WF alone would provide no
density fluctuations at all in most parts of the simulation volume" [src:
arXiv:2008.04926, Sect. 2.1].

### Step 3. Field-level route: from a chain sample to particles
<!-- key: step-3-field-level-route-from-a-chain-sample-to -->

The Manticore-Local configuration [src: arXiv:2505.10682, Sects. 2.2–2.3]:

- Inference in a 1000 Mpc parent box on a 256³ grid, L_WNF ≈ 3.9 Mpc [src: arXiv:2505.10682,
  Sect. 2.3], with the observer at the centre and constraints out to about 200
  Mpc, where the signal-to-noise stays above unity [src: App. D, Fig. 24]; 32 galaxy
  subcatalogues of 2M++, each with its own bias parameters; fixed DES Y3
  "3×2pt + All Ext." ΛCDM cosmology with h = 0.681, chosen to match FLAMINGO [src: Sect. 2.2 and Table 1].
- Fifty posterior samples are resimulated. monofonIC places 1024³ particles
  (m_p = 3.7 × 10¹⁰ M_⊙) on the 256³ constrained field and injects Gaussian
  random modes beyond the Nyquist frequency of the inference grid; 2LPT at
  z = 69; SWIFT to z = 0; the same cosmology as the inference [src: arXiv:2505.10682, Sect. 2.3].
- The posterior spread then mixes constrained-mode uncertainty and the
  random small-scale completion; separating them "would require sampling
  many small-scale realizations per posterior sample", judged
  computationally prohibitive [src: Sect. 2.3].
- Haloes with HBT+, at least 20 bound particles, analysis restricted to
  M_200c ≥ 10¹³ M_⊙ (> 200 particles), positions and velocities from the
  most-bound particle; literature M_500c converted to M_200c with a
  concentration–mass relation [src: arXiv:2505.10682, Sect. 2.3.1].
- Ten control runs with random phases and the same box, resolution and
  pipeline [src: Sect. 2.3.2].
- The z = 0 snapshot is used instead of a light-cone, assuming negligible
  evolution for 0 < z < 0.045 [src: arXiv:2505.10682, Sect. 2.3].

Manticore-Deep makes a different choice for the completion: the injected
small-scale modes "are held fixed across all 15 posterior samples, ensuring
that differences between realizations reflect only the uncertainty in the
large-scale, data-constrained structure" [src: arXiv:2606.10020, Sect.
2.4]. Its resimulations use 4096³ particles in 4096 h⁻¹ Mpc (1 h⁻¹ Mpc
spacing, m_p = 8.49 × 10¹⁰ h⁻¹ M_⊙), 2LPT at z = 69, softening
0.04 h⁻¹ Mpc (1/25 of the spacing), an on-the-fly light-cone to z ≈ 0.7, 79
outputs as in FLAMINGO, HBT-HERONS haloes, about 6.5 × 10⁵ CPU-h per
resimulation [src: Sect. 2.4].

The earlier 2M++ resimulations used genetIC to oversample the 256³ BORG
white noise to 512³ particles (2 × 10¹¹ h⁻¹ M_⊙) by tricubic
interpolation, GADGET-2 from z = 50 in 677.7 h⁻¹ Mpc, AHF haloes, and 20
samples 300 steps apart, longer than any measured correlation length; they
also ran inverted initial conditions to obtain "anti-haloes" as void
tracers [src: arXiv:2304.09193, Sect. 2.2].

Hamlet-PM, the velocity-constrained counterpart, runs ten chains of 5000
steps and keeps one sample every 500, giving 100 constrained initial
conditions, about one independent sample per GPU-hour (10 h per chain on a
V100); its own routine injects random small-scale power from 128³ to 512³
particles (7.8 × 10¹⁰ h⁻¹ M_⊙), 2LPT to z = 63, AREPO gravity to z = 0,
friends-of-friends haloes (b = 0.2) with at least 32 particles, i.e.
≥ 2.5 × 10¹² h⁻¹ M_⊙ [src: arXiv:2602.03699, Sect. 3.4]. The CLONES-based
SLOW suite starts from one realisation (number 8) of a 500 h⁻¹ Mpc,
512³-grid constrained field, adds small-scale features per resolution with
Ginnungagap, and runs it as dark matter only (768³ to 6144³ particles),
non-radiative magnetohydrodynamics with cosmic rays (2 × 3072³), and full
galaxy formation (2 × 768³ to 2 × 3072³, the last only to z = 2), with
SubFind haloes [src: arXiv:2302.10960, Sect. 3.4].

The KIGEN-based 2MRS runs choose samples by a criterion rather than by
thinning: among converged chain samples, those whose ALPT-evolved density
has a cross-power with the galaxy field above a threshold at
k_th = 1 h Mpc⁻¹, keeping the most correlated of each set of first and
second chain neighbours, "representative of the PDF" with full power
[src: arXiv:1304.6565, Sect. 2.3, Eqs. 1–5]. The white noise is built by
dividing the sampled modes by the theoretical linear P(k); dividing by the
power measured in the sample itself (perfectly flat white noise) gave
"significantly less correlated" fields after evolution; small scales are
added on a finer mesh with ginnungagap, then GADGET-3 from z = 100 and AHF
haloes [src: Sects. 2.4–2.5].

ELUCID resimulates a single sample: the linear field at HMC step 1500,
sampled with 3072³ particles (3.09 × 10⁸ h⁻¹ M_⊙) at z = 100, the modes
above the inference Nyquist frequency given random phases, evolved with
L-GADGET with 100 snapshots between z = 19 and 0 [src: arXiv:1608.01763,
Sect. II.5]. The typical scatter between the input group-based density and
the constrained simulation is 0.018 dex at 4 h⁻¹ Mpc smoothing and about
0.13 dex at 2 h⁻¹ Mpc; on a mock the scatter against the true density is
0.10 and 0.23 dex, close to that of the group-based density itself (0.09 and
0.20 dex), so that the main errors come from the redshift-distortion
correction, the group finder and the halo-domain step, not from the
HMC + PM inference [src: Sect. II.5].

### Step 4. Multi-scale embedding for zooms (SIBELIUS)
<!-- key: step-4-multi-scale-embedding-for-zooms-sibelius -->

To resimulate a small region at high resolution inside a constrained
volume, SIBELIUS converts the BORG 256³ white noise (1000 cMpc box,
≈ 3.9 cMpc cells) into the Panphasia octree basis: an unconstrained octree
white-noise field is generated, its Fourier amplitudes are overwritten by
the BORG modes as linear constraints, and the result is converted back
[src: arXiv:2103.12073, Sects. 2.2–2.3]. The octree is used rather than
Fourier modes because its functions have compact support, which makes
multi-scale initial conditions cheaper when only a small region is refined
[src: Sect. 2.1]. The constraints occupy levels 19–21 (240³ degrees of
freedom, slightly fewer than BORG's, so some of the shortest BORG modes are
dropped) and constrain modes down to λ_cut(21) = 6.48 cMpc; deeper levels
are free to be randomised [src: Sects. 2.1 and 2.3]. The sample chosen was
the last of the chain (iteration 9350), among samples of comparable
likelihood, because it reproduced Virgo and Fornax well [src: Sect. 2.2].

HESTIA zooms on a linear constrained field by trial and error instead.
Each constrained realisation needs two random seeds, one for the
unconstrained regions and incomplete sampling, one for the scales below the
reconstruction scale; close to 1000 dark-matter-only constrained initial
conditions were run in 100 h⁻¹ Mpc boxes (256³, with a 10 h⁻¹ Mpc-radius
zoom at 512³ effective, 6 × 10⁸ M_⊙) and searched for a Virgo halo above
2 × 10¹⁴ M_⊙ within 7.5 Mpc of its expected position, a Local-Group-like
pair within 5 Mpc of the origin (8 × 10¹¹–3 × 10¹² M_⊙, 0.5–1.2 Mpc apart,
isolated, mass ratio > 0.5, infalling), a LG–Virgo distance within 3.5 Mpc
of the true one, and no more massive cluster within 20 Mpc [src:
arXiv:2008.04926, Sect. 3.2.1]. Successful seeds are regenerated at 4096³
effective in a 5 h⁻¹ Mpc sphere with Auriga magnetohydrodynamics
(m_dm = 1.2 × 10⁶ M_⊙, ε = 340 pc), and three at 8192³ effective
(m_dm = 1.5 × 10⁵ M_⊙, ε = 220 pc) [src: Sect. 3.2.2]. The resulting Virgo
masses, 3–4 × 10¹⁴ M_⊙, are possibly below the observed value, which the
authors attribute to the small box: constrained runs in larger boxes give
more massive Virgo clusters [src: Sect. 3.2.1].

### Step 5. Tile the inference when the volume is too large
<!-- key: step-5-tile-the-inference-when-the-volume-is -->

Manticore-Deep needs a 4096 h⁻¹ Mpc parent box at 4 h⁻¹ Mpc, a 1024³
inference "beyond the memory and runtime limits of current field-level
inference methods" [src: arXiv:2606.10020, Sect. 2.2]. The box is cut into
4 × 4 × 4 tiles of 1024 h⁻¹ Mpc, each inferred on a 256³ grid; 27 contain
data, the other 37 are filled with prior Gaussian phases resampled for each
realisation [src: Sect. 2.2]. Each tile has a 64 h⁻¹ Mpc buffer: its outer
32 h⁻¹ Mpc is excluded from the likelihood and absorbs periodic-boundary
artefacts; its inner 32 h⁻¹ Mpc duplicates galaxies of neighbouring tiles
to avoid discontinuities; both are removed after sampling, leaving a 224³
core per tile [src: Sect. 2.2, Fig. 1]. Buffer width was set in
8 h⁻¹ Mpc pilot runs: smaller buffers hindered exploration and produced
edge artefacts, larger ones needed more tiles [src: Sect. 2.2]. The authors
stress that the product of tile posteriors "is not the factorisation of a
single global posterior": it pools no information across tiles [src: Sect.
2.3, Eq. 2]. Each tile has its own bias parameters and is evolved to a
fixed scale factor between a ≈ 0.55 and 0.9; the resimulation starts from
the reassembled field and evolves continuously [src: Table 1 and Sect.
2.4].

### Step 6. Match named objects across the ensemble
<!-- key: step-6-match-named-objects-across-the-ensemble -->

Three matching schemes are in use [src: arXiv:2505.10682, Sect. 3.4.1]:

- the most massive halo within a fixed radius, typically ≈ 30 Mpc (earlier
  BORG and SIBELIUS-DARK work), which becomes ambiguous in superclusters [src: arXiv:2505.10682, Sect. 3.4.1];
- a hierarchical selection that matches clusters to group catalogues and
  searches out to 65 Mpc, with X-ray temperature, luminosity and dynamical
  state as tie-breakers (SLOW) [src: arXiv:2505.10682, Sect. 3.4.1];
- the LUM: for each observed–simulated pair the probability
  p(r, M_200c) of finding a halo of that mass at that separation from a
  random point in an unconstrained simulation, evaluated for all haloes
  above 10¹⁴ h⁻¹ M_⊙, followed by a one-to-one assignment with the Hungarian
  algorithm that minimises the summed probabilities. Manticore adopts it [src: arXiv:2505.10682, Sect. 3.4.1].

The detection significance is 1 − p, and the "detection rate" is the
fraction of posterior resimulations in which a counterpart exceeds a given
significance [src: Sect. 3.4.2]. The CLUES studies match by position and
mass instead: a replica within about 6 h⁻¹ Mpc with a mass of the same
order (mock tests) [src: arXiv:1311.2253, Sect. 4.2]; Virgo candidates
within 3–4 h⁻¹ Mpc in every Cosmicflows-2 run, with an "inaccuracy"
normalised by reference values independent of the cluster so that distant
or massive haloes do not look artificially better [src: arXiv:1510.04900,
Sect. 3.4].

The SLOW procedure, read at source, for 46 local clusters: the observed
centre is taken from the Tully group catalogue, the mass from Compton-y
M_500 (else X-ray or dynamical); all massive haloes within a small search
radius above a lower mass cut are taken, the radius being enlarged up to
typically 45 h⁻¹ Mpc if needed (median replica distance ≈ 25 h⁻¹ Mpc);
temperature, luminosity, dynamical state and, in superclusters such as
Hydra–Centaurus or Shapley, the geometry of the surrounding filaments break
ties [src: arXiv:2402.01834, Sect. 3.3]. SLOW states its search radius in
h⁻¹ Mpc and Manticore-Local in Mpc, so the two radii are compared only after
a conversion with the Hubble constant of each paper. Hamlet-PM uses the LUM and adds
an "opt-LUM" that moves each target iteratively to the mass-weighted centre
of its matched haloes (converging in fewer than 10 iterations), to separate
a systematic offset of a tight halo cloud from random scatter; its
p-values are relative to that centre and are "not meant to replace" those
of the LUM [src: arXiv:2602.03699, Sect. 4.2.2, Eqs. 15–16].
ELUCID matches greedily: groups in decreasing mass order take the halo
within Δd_mx with the smallest |log M_gr/M_h| below Δm_mx, mass taking
priority over distance; about half of the groups above 10¹⁴ h⁻¹ M_⊙ have a
match within 1 h⁻¹ Mpc and 0.15 dex, more than 95% within 4 h⁻¹ Mpc and
0.5 dex, against much less than 5% for the same halo sample rotated by a
large angle, which serves as the null test [src: arXiv:1608.01763, Sect.
IV.1].

### Step 7. Validate in tiers
<!-- key: step-7-validate-in-tiers -->

Manticore-Local proposes three tiers [src: arXiv:2505.10682, Sect. 4.3]:
(1) statistical consistency of the parent volume with ΛCDM — Gaussianity
of the white noise (its power spectrum, PDF and a Q–Q comparison), halo
mass function, power spectrum and bispectrum against control runs, which
apart from the Gaussianity were not used in the inference [src: Sect.
3.1]; (2) fidelity to observed structure — cluster detection rates with a
community-standard cluster catalogue, and the Bayesian evidence of the
reconstructed velocity field against direct distance tracers; (3)
physically enriched comparisons — SZ and X-ray profiles, stellar
populations, voids, ISW. A complementary internal metric, the halo overlap
of Lagrangian patches across resimulations, measures precision as distinct
from accuracy [sec: arXiv:2505.10682, Sect. 4.3, describing Stiskalek et
al. 2024, not read].

Other programmes validate differently: ELUCID by a full mock run and a
rotated-halo null test (Steps 3 and 6); SLOW compares replicas of 46 clusters with Compton-y, X-ray and
dynamical data one by one [src: arXiv:2402.01834, Sect. 3.3], and its
first paper sets the virial masses of Coma, Perseus and Virgo in SLOW
(1.8 × 10¹⁵, 1.0 × 10¹⁵, 9.8 × 10¹⁴ M_⊙) beside those of CORUSCANT
(7.6 × 10¹⁴, 1.3 × 10¹⁵, 5.5 × 10¹⁴) and SIBELIUS (1.5 × 10¹⁵,
3.3 × 10¹⁵, 4.3 × 10¹⁴, converted from 1.2 M_200c) and the observed
dynamical masses (1.4 × 10¹⁵, 1.5 × 10¹⁵, 6.3 × 10¹⁴) [src:
arXiv:2302.10960, Table 1].

A cross-programme test with the same metric is the "Velocity Field
Olympics" (its authors include CSiBORG authors), which scores seven
reconstructions by Bayesian evidence against Tully–Fisher and supernova
samples [src: arXiv:2502.00121, Sects. 2.1 and 5.1]. The contenders, as
that paper describes them: the linear 2M++ field of Carrick et al. 2015
(iterative real-space scheme, luminosity weights, ZoA filled by cloning,
256³ in 400 h⁻¹ Mpc, velocity scaled by β*); the U-Net reconstruction of
2MRS by Lilow et al. 2024 (arXiv:2404.02278), trained on Quijote mocks; CSiBORG1 and CSiBORG2,
resimulations of BORG 2M++ chains with 10-step PM and 20-step COLA; the
CF2 constrained realisation of Sorce (512³ in 500 h⁻¹ Mpc, with the
paired-fixed variant showing that "about 80 per cent of the large-scale
power is already constrained by local data"); and the CF4 reconstruction
of Courtois et al. 2023 (arXiv:2211.16390), an HMC forward model with linear velocities that
samples true distances and a zero-point h_eff (100 samples at 256³)
[sec: arXiv:2502.00121, Sects. 2.1.1–2.1.5]. The evidence "consistently
and strongly favoured CSiBORG2", then Lilow et al. and Carrick et al.,
whereas the Cosmicflows-based reconstructions "consistently underperform",
even on the samples used to constrain them [src: Sect. 5.1]. Smoothing all
fields to one coarse resolution leaves CF-based reconstructions disfavoured
but puts Lilow et al. above CSiBORG2; the authors leave open whether 2M++
is more informative or the methods applied to CF are limited, note that of
38,000 grouped CF4 objects only 18,000 lie at z < 0.05, and state that the
linear Carrick et al. method, "orders of magnitude less computationally
expensive", still beats both CF-based ones [src: Sect. 5.3]. The
velocity-side reply is the Hamlet-PM comparison under "Choices" below.

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Linear velocity constraints or a field-level posterior
<!-- key: linear-velocity-constraints-or-a-field-level -->

The linear route needs only a correlation matrix and its inverse and
assumes curl-free, linear velocities above the virial scale and a prior
cosmology [src: arXiv:1311.2253, Sect. 2]. Its cost is the Eulerian
formulation, repaired only approximately by the RZA, and the dependence on
debiased distances. The field-level route models non-linear dynamics,
redshift-space distortions, bias and selection in the forward model
[src: arXiv:2505.10682, App. A.2] at the price of an MCMC run per data set
(0.5–1.5 × 10⁶ CPU-h per Manticore-Deep tile) [src: arXiv:2606.10020, App.
B]. The two are compared in L2 through the velocity-field evidence
(`systematics.md#constrained-simulation-limits`).

Within the velocity route the debiasing itself has two treatments. Hamlet
samples the linear density and velocity jointly with the undoing of the
lognormal bias by HMC on GPUs, and outperforms the earlier Gibbs-sampling
reconstruction from Cosmicflows-3 "by two to four orders of magnitude in
CPU time" [src: Valade et al. 2022a, arXiv:2203.02369]. On Cosmicflows-3
mocks against the Bias Gaussian correction with a Wiener filter (BGc/WF),
the two "perform roughly equally well" below about 40 h⁻¹ Mpc, Hamlet does
slightly better between 40 and 120 h⁻¹ Mpc, and beyond 120 h⁻¹ Mpc Hamlet
has "better and tighter correlations" but "a somewhat biased
reconstruction", biases "missing from the BGc/WF reconstruction" [src:
Valade et al. 2022b, arXiv:2209.05846, abstract].

The Hamlet-PM paper makes the comparison from the velocity side. On the
velocity-field and LUM metrics both its linear and non-linear results rank
above the other velocity-based reconstructions, and its non-linear
forward model recovers massive clusters "with a higher rate" than an
earlier velocity-based suite, from which the authors infer that "full
forward-modeling is able to put tighter constraints on galaxy clusters than
the standard CLUES pipeline", part of the gain possibly coming from CF4
against CF2 or CF3 [src: arXiv:2602.03699, Sect. 6.2]. Against the
redshift-based route the same paper states that "our method is largely
outperformed by Manticore-Local" and gives the reasons: COLA instead of PM,
a 3.9 against 5.22 Mpc grid, and above all denser and more precise data
(about 69,000 galaxies with a median signal-to-noise below 1% error, against
about 31,000 with more than 180%), plus the weak sensitivity of radial
velocities to transverse shifts of clusters; it expects that advantage of
redshift data "should hold with upcoming surveys" [src: Sect. 6.2]. For
SLOW no ensemble comparison is possible, because one set of initial
conditions was selected out of nine; 96% of the Hamlet-PM runs have more
than three counterparts with p < 0.01 [src: Sect. 6.2].

### Which gravity solver inside the sampler
<!-- key: which-gravity-solver-inside-the-sampler -->

On initial conditions from the earlier 2M++ chain, with 512³ particles in
677.7 h⁻¹ Mpc, COLA and PM with 3 to 128 linear or logarithmic steps were
compared with GADGET-2 [src: arXiv:2304.09193, Sects. 2.1.2 and 3.1]:
10–20 COLA steps reproduce the masses of ∼10¹⁵ h⁻¹ M_⊙ clusters; at
∼10¹⁴ h⁻¹ M_⊙ no number of steps reaches the GADGET M_200c because the
2.65 h⁻¹ Mpc grid exceeds R_200c ≈ 0.75 h⁻¹ Mpc, whereas M_100m
(R_100m ≈ 1.4 h⁻¹ Mpc) converges. The reason given for caring: a solver
that underestimates non-linear growth drives the sampler to exaggerated
initial over- and under-densities, and the resimulated clusters come out
too massive [src: Sect. 2.1.2]. This is what happened: posterior
resimulations of the earlier 10-step PM chain overpredict the halo and
anti-halo mass functions in the central 135 h⁻¹ Mpc relative to
unconstrained regions of equal underdensity (δ = −0.043 ± 0.001), while
the 20-step COLA chain agrees, and the authors state that this explains
the cluster excess of SIBELIUS-DARK and two other works built on the same
chain, which "is not a real effect" [src: Sect. 3.2]. Manticore raises the
COLA force sampling from 2 to 4 during burn-in, following those
convergence studies [src: arXiv:2505.10682, App. D].

ELUCID reached the same concern from the other side: an inaccurate model
"can introduce spurious non-Gaussian features in the reconstructed linear
density field", biasing the predicted haloes, so it uses PM dynamics with
1 h⁻¹ Mpc cells and 20 steps, which it states is "much more accurate than"
the Zel'dovich or higher-order LPT models used before, and smooths model
and data on 4 h⁻¹ Mpc (≥ 3 cells suffice in its tests) to remove the
remaining small-scale discrepancies [src: arXiv:1608.01763, Sect. II.4].
Hamlet-PM's 5 PM steps (Step 1) are "based on preliminary tests" [src:
arXiv:2602.03699, Sect. 3.3].

### Random or fixed small-scale completion
<!-- key: random-or-fixed-small-scale-completion -->

Drawing new small-scale modes for every posterior sample (Manticore-Local)
includes their scatter in the ensemble; fixing them (Manticore-Deep)
isolates the constrained uncertainty but hides how much of a named
object's properties is set below the constraint scale (Step 3 above). The
SIBELIUS study quantifies that dependence for the Local Group from more
than 60,000 GADGET-3 zooms that share the BORG constraints and randomise
octree levels 22 and above (λ_cut ≤ 3.24 cMpc) [src: arXiv:2103.12073,
Sects. 2.4 and 2.5; abstract]. Level 22 determines whether haloes of
∼10¹² M_⊙ exist; the total mass, orientation, orbital energy and angular
momentum of the Local Group are largely set by modes above 1.6 cMpc,
while the Milky Way–M31 separation and radial velocity are transient and
depend on scales down to 0.2 cMpc [src: Sect. 2.4; abstract]. Of the 60,000
runs, 48,323 give a Local-Group-like pair (1–8 × 10¹² M_⊙, 0.5–2 Mpc apart,
no more massive neighbour within 2 Mpc); 6385 pass loose criteria; one
passes the strict criteria, and none once the orientation relative to the
large-scale structure is required within 15° [src: Sect. 3.1]. The
numerical cost was kept low by a refinement mask built from 100 prototype
runs (the union of particles within 8 Mpc of the observer), about 52³
high-resolution particles at 2.4 × 10⁹ M_⊙ and 4.4 core-hours per run
[src: Sect. 2.5].

The CLUES "Local Group factory" asks the same question on linear CF2
constraints, varying the random field rather than only the small scales:
of 300 constrained simulations, 146 contain a LG obeying isolation, mass
and separation criteria, 51 also the orbital angular momentum and energy,
6 also the phase of the orbit; the authors conclude that the LG "is likely
a robust outcome" of ΛCDM under the CF2 constraints [src: Carlesi et al.
2016, arXiv:1602.03919, abstract]. A third answer replaces random completion by
paired fixed fields (fixed amplitudes, exactly out of phase): constrained
in that way, "only 20% of the power spectrum on large scales (> tens of
megaparsecs) is purely random", and the two members of one pair give an
unbiased average, "the equivalent of hundreds of constrained simulations",
their difference giving the uncertainty [src: Sorce 2020,
arXiv:2006.01838, abstract].

### How many resimulations
<!-- key: how-many-resimulations -->

| Suite | Posterior samples resimulated | Reason or diagnostic stated | Place read |
|---|---|---|---|
| CLUES mock test | 10 constrained ICs | density scatter against the target falls from 0.47 to a plateau of 0.37 (log density) after 8 or more runs | arXiv:1311.2253, Sect. 4.2 |
| CLUES Cosmicflows-2 | 15 constrained plus 10 sharing one random field, against 15 random | cell-to-cell scatter at 5 h⁻¹ Mpc smoothing (L2) | arXiv:1510.04900, Sect. 3.1 |
| BORG 2M++ COLA20 | 20, 300 steps apart | longer than any correlation length measured | arXiv:2304.09193, Sect. 2.2 |
| Manticore-Local | 50, from five chains of 7150 steps (4750 burn-in) | integrated autocorrelation time; multiple chains | arXiv:2505.10682, Sect. 2.3 and App. D |
| Manticore-Deep | 15 per tile, one chain per tile | effective sample size ≈ 15 per tile; no Gelman–Rubin possible | arXiv:2606.10020, App. B |
| Hamlet-PM (CF4) | 100, from ten chains of 5000 steps, one every 500 | internal chain correlation checked minimal | arXiv:2602.03699, Sect. 3.4 |
| KIGEN 2MRS | samples above a cross-power threshold with the galaxy field, neighbours discarded | representative of the posterior with full power | arXiv:1304.6565, Sect. 2.3 |
| ELUCID | 1 (HMC step 1500) | full uncertainty estimated by running the whole reconstruction on a realistic mock | arXiv:1608.01763, Sect. II.5 |
| HESTIA | close to 1000 low-resolution seeds (long × short waves), searched by cosmographic criteria; three run at the highest resolution | trial and error for a Local Group | arXiv:2008.04926, Sects. 3.2.1–3.2.2 |
| SLOW (CLONES) | 1 realisation (number 8) out of nine pre-run | no statistical ensemble (stated by Hamlet-PM) | arXiv:2302.10960, Sect. 3.4; arXiv:2602.03699, Sect. 6.2 |

### Snapshot or light-cone
<!-- key: snapshot-or-light-cone -->

Manticore-Local uses the z = 0 snapshot because its constrained volume
reaches only z < 0.045 [src: arXiv:2505.10682, Sect. 2.3]. Manticore-Deep
infers each tile at its own fixed scale factor but writes an on-the-fly
light-cone in the resimulation [src: arXiv:2606.10020, Table 1 and Sect.
2.4]. ELUCID holds the SDSS DR7 volume in one 500 h⁻¹ Mpc box, untiled,
and writes snapshots (Step 3) [src: arXiv:1608.01763, Sects. II.4–II.5].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Inference box, grid, cell | 1000 Mpc, 256³, 3.9 Mpc; constrained to ≈ 200 Mpc | Manticore-Local | arXiv:2505.10682 | Table 1 |
| Convergence variants | 7.8 Mpc grid (Local-Lo); 500 Mpc box, constraints to 125 Mpc (Mini) | Manticore-Local | arXiv:2505.10682 | Table 1, App. E |
| Resimulation | 1024³, 3.7 × 10¹⁰ M_⊙, 2LPT z = 69, SWIFT, 50 samples, 10 controls | Manticore-Local | arXiv:2505.10682 | Sects. 2.3, 2.3.2 |
| Halo cut | ≥ 20 bound particles kept; M_200c ≥ 10¹³ M_⊙ analysed | Manticore-Local | arXiv:2505.10682 | Sect. 2.3.1 |
| Cluster matching | LUM, haloes > 10¹⁴ h⁻¹ M_⊙, Hungarian assignment; 700 counterparts for 14 clusters; median p = 5.0 × 10⁻⁴ (3.3σ; 10–90%: 2.5σ–4.5σ) | Manticore-Local | arXiv:2505.10682 | Sects. 3.4.1–3.4.2 |
| Detection rate | all 700 above 1σ, ≳ 99% above 2σ; earlier suite 6–35% at ≈ 2σ | Manticore-Local | arXiv:2505.10682 | Sect. 3.4.2 |
| Tiling | 64 tiles of 1024 h⁻¹ Mpc on 256³, 27 with data, 64 h⁻¹ Mpc buffer, 224³ core | Manticore-Deep | arXiv:2606.10020 | Sect. 2.2 |
| Galaxies, data density | 1,664,630 galaxies; 2.5 × 10⁻⁶ to 3.1 × 10⁻⁴ (h⁻¹ Mpc)⁻³ per tile | Manticore-Deep | arXiv:2606.10020 | Sect. 2.3, App. B |
| Burn-in, cost | 2500–4500 steps; 0.5–1.5 × 10⁶ CPU-h per tile | Manticore-Deep | arXiv:2606.10020 | App. B |
| Resimulation | 4096³, 8.49 × 10¹⁰ h⁻¹ M_⊙, ε = 0.04 h⁻¹ Mpc, 79 outputs, 6.5 × 10⁵ CPU-h each | Manticore-Deep | arXiv:2606.10020 | Sect. 2.4 |
| Cluster offsets | 0.5–1° (Local) against 2–3° (Deep), comparable to the 1.5–4° voxel scale at z ≲ 0.05 | Manticore-Deep | arXiv:2606.10020 | App. E |
| Solver adequacy | COLA 10–20 steps for ∼10¹⁵ h⁻¹ M_⊙ masses; M_200c of ∼10¹⁴ not converged on a 2.65 h⁻¹ Mpc grid | BORG 2M++ | arXiv:2304.09193 | Sect. 3.1 |
| Constraint depth of SIBELIUS | octree levels 19–21, λ_cut = 6.48 cMpc; randomised from level 22 (3.24 cMpc) | SIBELIUS | arXiv:2103.12073 | Sects. 2.1, 2.4 |
| RZA linear validity | down to 2 h⁻¹ Mpc | CLUES | arXiv:1510.04900 | Sect. 2.3 |
| RZA3D against RZA-radial scatter | 0.34 against 0.35 (log density), 246 against 258 km/s | CLUES mocks | arXiv:1311.2253 | Sect. 4.2 |
| RZA position recovery | median 1.36 h⁻¹ Mpc (5 h⁻¹ Mpc sparse, noisy) against ≥ 10 h⁻¹ Mpc without RZA | CLUES mocks | arXiv:1212.2806 | abstract |
| Halo recovery with RZA | ≳ 10¹⁴ h⁻¹ M_⊙ within ≈ 2 h⁻¹ Mpc, factor 2 in mass; without RZA ≳ 5 × 10¹⁴, shifted ≈ 10 h⁻¹ Mpc | CLUES mocks | arXiv:1212.2810 | abstract |
| CF2 constraints after grouping | 4837 points (HESTIA grouping); 5562 galaxies and groups (CLONES/SLOW) | HESTIA; SLOW | arXiv:2008.04926; arXiv:2402.01834 | Sect. 2.1; Sect. 2.1 |
| LG search and zooms | ≈ 1000 seeds, 100 h⁻¹ Mpc, 6 × 10⁸ M_⊙; 4096³ eff. (1.2 × 10⁶ M_⊙, 340 pc); three at 8192³ (1.5 × 10⁵ M_⊙, 220 pc) | HESTIA | arXiv:2008.04926 | Sects. 3.2.1–3.2.2 |
| LG success rate | 146, 51 and 6 of 300 constrained runs at three criteria levels | CLUES LG factory | arXiv:1602.03919 | abstract |
| Random large-scale power | 20% purely random above tens of Mpc with paired fixed fields | CLUES/CLONES | arXiv:2006.01838 | abstract |
| SLOW volume and runs | 500 h⁻¹ Mpc, CLONES realisation 8; DMO 768³–6144³, MHD+CR 2 × 3072³, hydro 2 × 768³–2 × 3072³ | SLOW | arXiv:2302.10960 | Sect. 3.4 |
| Replica search | 46 clusters, radius up to ≈ 45 h⁻¹ Mpc, median ≈ 25 h⁻¹ Mpc | SLOW | arXiv:2402.01834 | Sect. 3.3 |
| Velocity forward model | 128³ in 500 h⁻¹ Mpc (3.9 h⁻¹ Mpc), 2LPT to z = 19 + 5 PM steps; CF4 cut at 16,500 km/s | Hamlet-PM | arXiv:2602.03699 | Sects. 2, 3.3 |
| Resimulation | 100 ICs (10 chains × 10), 512³, 7.8 × 10¹⁰ h⁻¹ M_⊙, AREPO, FoF ≥ 32 particles | Hamlet-PM | arXiv:2602.03699 | Sect. 3.4 |
| Group-based inference | 500 h⁻¹ Mpc, 500³ (1 h⁻¹ Mpc), 20 PM steps, 4 h⁻¹ Mpc smoothing, σ_hd = 0.5 ρ_hd | ELUCID | arXiv:1608.01763 | Sect. II.4 |
| Resimulation and scatter | 3072³, 3.09 × 10⁸ h⁻¹ M_⊙, z = 100; 0.10 (0.23) dex against truth on a mock at 4 (2) h⁻¹ Mpc | ELUCID | arXiv:1608.01763 | Sect. II.5 |
| Group–halo matches | ≈ 50% of groups > 10¹⁴ h⁻¹ M_⊙ within 1 h⁻¹ Mpc and 0.15 dex; > 95% within 4 h⁻¹ Mpc and 0.5 dex; ≪ 5% for rotated haloes | ELUCID | arXiv:1608.01763 | Sect. IV.1 |
| Linear 2M++ calibration | β* = 0.431 ± 0.021; external flow 159 ± 23 km/s at 5.1σ | Carrick et al. | arXiv:1504.04627 | abstract |
| CF4 HMC reconstruction | fσ8 = 0.36 ± 0.05 (grouped); bulk flow 230 ± 136 km/s at 300 Mpc; H0 = 74.5 ± 0.1 (grouped CF4 distances) | Courtois et al. | arXiv:2211.16390 | abstract |
| Mass comparison of named clusters | Coma, Perseus, Virgo: SLOW 1.8 × 10¹⁵, 1.0 × 10¹⁵, 9.8 × 10¹⁴; CORUSCANT 7.6 × 10¹⁴, 1.3 × 10¹⁵, 5.5 × 10¹⁴; SIBELIUS 1.5 × 10¹⁵, 3.3 × 10¹⁵, 4.3 × 10¹⁴ M_⊙ (M_vir) | SLOW paper | arXiv:2302.10960 | Table 1 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Solver bias absorbed into the initial conditions.** A forward model
  too coarse in time drives the sampler to exaggerated initial contrasts;
  the symptom is an excess of massive haloes and of anti-haloes in
  posterior resimulations relative to unconstrained regions of the same
  mean density; the test is that comparison, with a convergence study of
  cluster masses against an N-body code on the same initial conditions
  (arXiv:2304.09193, Sects. 3.1–3.2).
- **Reading masses below the grid.** M_200c of haloes whose R_200c is
  smaller than the inference cell is not set by the data; check
  convergence of a larger-aperture mass (M_100m) as well
  (arXiv:2304.09193, Sect. 3.1).
- **One sample quoted as the Universe.** SIBELIUS picked one chain sample
  for its look; eight samples of comparable likelihood share the large
  features but differ visibly locally (arXiv:2103.12073, Sect. 2.2).
  Report the detection rate across the ensemble (arXiv:2505.10682, Sect.
  3.4.2).
- **Fixed-radius matching in dense regions.** Ambiguous in Hydra–Centaurus
  and Shapley; use a probabilistic, one-to-one assignment and state the
  mass threshold and the assumed cluster positions, to which the p-values
  are sensitive; positional errors were not propagated in Manticore-Local
  (arXiv:2505.10682, Sects. 3.4.1–3.4.2).
- **Transient observables of small systems.** Separation and radial
  velocity of a Local Group pair depend on modes down to 0.2 cMpc, far
  below any constraint; the test is a set of runs that randomise only the
  small scales (arXiv:2103.12073, abstract and Sect. 2.4).
- **Tile boundaries.** Too thin a buffer produces edge artefacts and poor
  exploration; independent tiles share no information, so a structure
  crossing a boundary is constrained by two independent chains
  (arXiv:2606.10020, Sects. 2.2–2.3).
- **Single chains.** When one chain per tile is affordable, convergence
  rests on likelihood stabilisation and autocorrelation lengths of voxels
  and power-spectrum modes, not on cross-chain statistics
  (arXiv:2606.10020, App. B).
- **Survey patchwork.** Positional scatter of recovered clusters grows
  where the input catalogues change depth and selection, e.g. near the
  Zone of Avoidance for Perseus (arXiv:2606.10020, App. E).
- **Biased distances in the linear route.** Malmquist and lognormal biases
  produce a spurious infall onto the Local Volume unless minimised before
  the WF (arXiv:1510.04900, Sect. 2.2). A joint HMC treatment (Hamlet)
  removes the bias inside the sampler but leaves "a somewhat biased
  reconstruction" near the edge of the data, beyond about 120 h⁻¹ Mpc,
  where BGc/WF shows no such bias (arXiv:2209.05846).
- **Neglected displacements.** CR without RZA shifts recovered haloes by
  about 10 h⁻¹ Mpc and recovers only the most massive ones
  (arXiv:1212.2810) [src: abstract].
- **Box too small for the named cluster.** HESTIA's Virgo, 3–4 × 10¹⁴ M_⊙
  in 100 h⁻¹ Mpc boxes, is possibly below the observed mass; larger
  constrained boxes give more massive Virgo clusters (arXiv:2008.04926,
  Sect. 3.2.1).
- **Errors upstream of the sampler.** In ELUCID the scatter against the
  truth is set by the redshift-distortion correction, group finder and
  halo-domain density, not by the HMC + PM step (arXiv:1608.01763, Sect.
  II.5).
- **Transverse positions from radial data.** Radial velocities are weakly
  sensitive to transverse shifts of clusters, which flattens the scatter
  of counterparts in velocity-constrained runs (arXiv:2602.03699, Sect.
  6.2); CF4 sub-catalogue inter-calibration (about 0.1 mag) is not
  propagated there (Sect. 2).
- **Metric depends on resolution.** Evidence comparisons favour finer
  fields; at a common coarse smoothing the ranking of the 2M++-based
  reconstructions changes (arXiv:2502.00121, Sect. 5.3).

## Reading list
<!-- key: reading-list -->

- Review: Angulo & Hahn 2021, arXiv:2112.05165, Sect. 6.3.7 — the
  Hoffman–Ribak scheme and its Lagrangian limitation.
- Method: Sorce et al. 2013, arXiv:1311.2253 — WF, RZA and CR in sequence;
  RZA3D tested on mocks.
- Application: Sorce et al. 2015, arXiv:1510.04900 — CLUES on
  Cosmicflows-2: debiasing, the four equations, the resolution step.
- Method: Stopyra et al. 2023, arXiv:2304.09193 — solver accuracy inside
  the sampler and the posterior resimulation recipe.
- Application: McAlpine et al. 2025, arXiv:2505.10682 — Manticore-Local:
  priors, bias, likelihood, resimulation, LUM matching, validation tiers.
- Application: McAlpine et al. 2026, arXiv:2606.10020 — tiled inference,
  buffers, fixed small-scale completion, single-chain diagnostics.
- Method: Sawala et al. 2021, arXiv:2103.12073 — embedding constraints in
  Panphasia and the scale hierarchy of Local Group properties.
- Method: Jenkins 2013, arXiv:1306.5968 (in L2) — the Panphasia octree.
- Validation: Stiskalek et al. 2025, arXiv:2502.00121 (in L2) — velocity
  evidence against direct distance tracers; seven reconstructions from
  2M++, 2MRS and Cosmicflows compared on one metric.
- Method: Doumler et al. 2013a, arXiv:1212.2806, and 2013c,
  arXiv:1212.2810 — the RZA and its resimulation tests.
- Application: Libeskind et al. 2020, arXiv:2008.04926 — HESTIA: CF2
  WF/CR, two seeds, LG selection, magnetohydrodynamic zooms.
- Application: Carlesi et al. 2016, arXiv:1602.03919 — the Local Group
  factory, success rates over 300 constrained runs. [src: abstract]
- Method: Sorce 2020, arXiv:2006.01838 — paired fixed fields for the
  random fraction and the uncertainty.
- Application: Dolag et al. 2023, arXiv:2302.10960, and Hernández-Martínez
  et al. 2024, arXiv:2402.01834 — SLOW: CLONES ICs, hydrodynamical set,
  replica search for 46 clusters [src: abstract of arXiv:2402.01834], mass
  comparison with CORUSCANT and SIBELIUS.
- Method: Valade et al. 2022, arXiv:2203.02369 — Hamlet, HMC from
  peculiar velocities; arXiv:2209.05846 — Hamlet against BGc/WF on mocks.
- Application: Valade et al. 2026, arXiv:2602.03699 (in L2) — Hamlet-PM on
  CF4: PM forward model, resimulation, opt-LUM, comparison with CLUES and
  Manticore.
- Application: Wang et al. 2016, arXiv:1608.01763 (in L2) — ELUCID:
  group-based density, HMC + PM, single-sample resimulation, matching.
- Method: Heß, Kitaura & Gottlöber 2013, arXiv:1304.6565 (in L2) — sample
  selection by cross-power, white-noise construction.
- Data products used as benchmarks: Carrick et al. 2015, arXiv:1504.04627
  (linear 2M++); Lilow et al. 2024, arXiv:2404.02278 (U-Net on 2MRS);
  Courtois et al. 2023, arXiv:2211.16390 (CF4 HMC).

## Not verified
<!-- key: not-verified -->

- The halo overlap metric (Stiskalek et al. 2024) and the LUM paper
  (Pfeifer et al. 2023): described here from the Manticore-Local and
  Hamlet-PM papers only; their identifiers were not retrieved. The SLOW
  procedure is now read at source (Step 6).
- The Cosmicflows debiasing method (Sorce 2015) and the BGc method: cited
  through the CLUES, SLOW and Hamlet papers. The Doumler RZA papers are
  read at abstract level only.
- Mathis et al. 2002, CORUSCANT, CLONES (Sorce 2018) and the Virgo zoom of
  Sorce et al. 2021: described through the SLOW paper only. The figures
  quoted for the Sorce and Courtois reconstructions in Step 7 are those of
  arXiv:2502.00121 [sec].
- VIRBIUS and CSiBORG's own papers: not read in this run.
- Whether SIBELIUS-DARK's reported local underdensity, as distinct from its
  cluster excess, is also attributed to the PM10 chain: the 2023 paper read
  here names the cluster excess only.
- CLUES zoom suites other than HESTIA (e.g. the Virgo CLONE): not read.
