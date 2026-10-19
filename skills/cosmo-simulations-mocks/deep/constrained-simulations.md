# Constrained simulations — cosmo-simulations-mocks dossier

Scope: how a constrained simulation of the local or survey volume is built
once the constraints exist (linear constrained realisations from peculiar
velocities with the reverse Zel'dovich step, conversion of a field-level
posterior into particle initial conditions, the small-scale completion,
tiling of the inference, the resimulation set-up), how simulated objects
are matched to named observed ones across an ensemble, and how such a
suite is validated.
Snapshot: 2026-10-19.
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
velocities [src: Sect. 2].

Before step 1, the catalogue is debiased: the four distance biases of
Cosmicflows-2 (the selection bias, already nulled in the catalogue; the
homogeneous and inhomogeneous Malmquist biases; the lognormal error
distribution) "lead mainly to a major infall onto the Local Volume", and an
iterative method minimises that infall and the spurious non-Gaussianity of
the radial-velocity distribution [src: arXiv:1510.04900, Sect. 2.2].

Periodic boxes keep only the divergent part of the velocity field (motions
due to densities inside the box), so tidal flows from outside are removed
[src: arXiv:1311.2253, Sect. 4.2].

### Step 3. Field-level route: from a chain sample to particles
<!-- key: step-3-field-level-route-from-a-chain-sample-to -->

The Manticore-Local configuration [src: arXiv:2505.10682, Sects. 2.2–2.3]:

- Inference in a 1000 Mpc parent box (681 h⁻¹ Mpc for h = 0.681) on a 256³
  grid, L_WNF ≈ 3.9 Mpc, with the observer at the centre and constraints out
  to about 200 Mpc; 32 galaxy subcatalogues of 2M++, each with its own bias
  parameters; fixed DES Y3 "3×2pt + All Ext." ΛCDM cosmology, chosen to
  match FLAMINGO (Table 1).
- Fifty posterior samples are resimulated. monofonIC places 1024³ particles
  (m_p = 3.7 × 10¹⁰ M_⊙) on the 256³ constrained field and injects Gaussian
  random modes beyond the Nyquist frequency of the inference grid; 2LPT at
  z = 69; SWIFT to z = 0; the same cosmology as the inference.
- The posterior spread then mixes constrained-mode uncertainty and the
  random small-scale completion; separating them "would require sampling
  many small-scale realizations per posterior sample", judged
  computationally prohibitive [src: Sect. 2.3].
- Haloes with HBT+, at least 20 bound particles, analysis restricted to
  M_200c ≥ 10¹³ M_⊙ (> 200 particles), positions and velocities from the
  most-bound particle; literature M_500c converted to M_200c with a
  concentration–mass relation [src: Sect. 2.3.1].
- Ten control runs with random phases and the same box, resolution and
  pipeline [src: Sect. 2.3.2].
- The z = 0 snapshot is used instead of a light-cone, assuming negligible
  evolution for 0 < z < 0.045 [src: Sect. 2.3].

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
  BORG and SIBELIUS-DARK work), which becomes ambiguous in superclusters;
- a hierarchical selection that matches clusters to group catalogues and
  searches out to 65 Mpc, with X-ray temperature, luminosity and dynamical
  state as tie-breakers (SLOW);
- the LUM: for each observed–simulated pair the probability
  p(r, M_200c) of finding a halo of that mass at that separation from a
  random point in an unconstrained simulation, evaluated for all haloes
  above 10¹⁴ h⁻¹ M_⊙, followed by a one-to-one assignment with the Hungarian
  algorithm that minimises the summed probabilities. Manticore adopts it.

The detection significance is 1 − p, and the "detection rate" is the
fraction of posterior resimulations in which a counterpart exceeds a given
significance [src: Sect. 3.4.2]. The CLUES studies match by position and
mass instead: a replica within about 6 h⁻¹ Mpc with a mass of the same
order (mock tests) [src: arXiv:1311.2253, Sect. 4.2]; Virgo candidates
within 3–4 h⁻¹ Mpc in every Cosmicflows-2 run, with an "inaccuracy"
normalised by reference values independent of the cluster so that distant
or massive haloes do not look artificially better [src: arXiv:1510.04900,
Sect. 3.4].

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

### How many resimulations
<!-- key: how-many-resimulations -->

| Suite | Posterior samples resimulated | Reason or diagnostic stated | Place read |
|---|---|---|---|
| CLUES mock test | 10 constrained ICs | density scatter against the target falls from 0.47 to a plateau of 0.37 (log density) after 8 or more runs | arXiv:1311.2253, Sect. 4.2 |
| CLUES Cosmicflows-2 | 15 constrained plus 10 sharing one random field, against 15 random | cell-to-cell scatter at 5 h⁻¹ Mpc smoothing (L2) | arXiv:1510.04900, Sect. 3.1 |
| BORG 2M++ COLA20 | 20, 300 steps apart | longer than any correlation length measured | arXiv:2304.09193, Sect. 2.2 |
| Manticore-Local | 50, from five chains of 7150 steps (4750 burn-in) | integrated autocorrelation time; multiple chains | arXiv:2505.10682, Sect. 2.3 and App. D |
| Manticore-Deep | 15 per tile, one chain per tile | effective sample size ≈ 15 per tile; no Gelman–Rubin possible | arXiv:2606.10020, App. B |

### Snapshot or light-cone
<!-- key: snapshot-or-light-cone -->

Manticore-Local uses the z = 0 snapshot because its constrained volume
reaches only z < 0.045 [src: arXiv:2505.10682, Sect. 2.3]. Manticore-Deep
infers each tile at its own fixed scale factor but writes an on-the-fly
light-cone in the resimulation [src: arXiv:2606.10020, Table 1 and Sect.
2.4].

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
  the WF (arXiv:1510.04900, Sect. 2.2).

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
  evidence against direct distance tracers.

## Not verified
<!-- key: not-verified -->

- The halo overlap metric (Stiskalek et al. 2024), the LUM paper (Pfeifer
  et al. 2023) and the SLOW matching procedure: described here from the
  Manticore-Local paper only; their identifiers were not retrieved.
- The Doumler et al. 2013 RZA papers and the Cosmicflows debiasing method
  (Sorce 2015): cited through the CLUES papers.
- Hamlet-PM's resimulation set-up beyond what L2 records: not re-read.
- Whether SIBELIUS-DARK's reported local underdensity, as distinct from its
  cluster excess, is also attributed to the PM10 chain: the 2023 paper read
  here names the cluster excess only.
- HESTIA and other CLUES zoom suites: not read.
