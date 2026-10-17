# Light-cones and lensing maps — cosmo-simulations-mocks dossier

Scope: how a simulation is turned into a past light-cone and into lensing
maps (box and observer geometry, on-the-fly or snapshot light-cones,
haloes on the cone, Born or multiple-plane ray-tracing, shell thickness,
map interpolation, assignment to galaxies), and what replication, shell
thickness, the Born approximation and interpolation each cost.
Snapshot: 2026-10-17.
From: Angulo & Hahn 2021 review (arXiv:2112.05165), Sect. 9.6; LSST DESC
Survey Computing & Simulation working group.

Already in L2, not repeated here: the four constructions of a light-cone
and the founding papers (Hubble Volume, MoMaF, Kitzbichler & White, Merson
et al., the onion universe) in
`physics-and-methods.md#light-cones-and-survey-realism`; the layers of
survey realism and the pseudo-light-cones of the DESI DR1 EZmocks (same
section and `systematics.md#light-cone-and-survey-realism-limits`); the
Flagship 2, FLAMINGO, Last Journey and HalfDome light-cone outputs
(`physics-and-methods.md#light-cones-and-survey-realism`). How the fast
mocks that fill such cones are made is in `deep/fast-mocks.md`; lensing
analyses that use the maps belong to `cosmo-weak-lensing`.

Symbols. χ: comoving radial distance; f_K(χ): comoving angular-diameter
distance; z_s: source redshift; κ, γ = γ_1 + iγ_2, ω: convergence, shear,
rotation; A_ij: distortion (Jacobian) matrix of the lens mapping; β, θ:
true and observed angular positions; α: deflection; Δχ: comoving thickness
of a lens shell; N_side: HEALPix resolution parameter (pixel side
0.43 arcmin at 8192, 0.21 at 16384, as stated in arXiv:1706.01472,
Sect. II.2); SSC: super-sample covariance.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Fix the geometry: box, observer and replication
<!-- key: step-1-fix-the-geometry-box-observer-and -->

A snapshot at distance r is taken where the light-cone crosses it,
∫_{a_r}^{1} c da/(a² H(a)) = r(a_r) (Angulo & Hahn 2021, arXiv:2112.05165,
Eq. 112); a box of side L therefore covers structure only to a finite
redshift, z ≈ 1.4 for L = 3000 h⁻¹ Mpc, beyond which the box must be
replicated [src: Sect. 9.6]. The layouts in use:

| Run | Box | Observer and copies | Coverage without repetition | Place read |
|---|---|---|---|---|
| AbacusSummit base | 2 h⁻¹ Gpc, 6912³ | 10 h⁻¹ Mpc inside a corner; the box plus two copies along y and z | an octant to 1990 h⁻¹ Mpc (z ≈ 0.8), then two patches of about 900 deg² each to 3990 h⁻¹ Mpc (z ≈ 2.45) | arXiv:2110.11413, Sect. 2.2 |
| AbacusSummit huge | 7.5 h⁻¹ Gpc, 8640³ | box centre, one copy | full sky to z ≈ 2.18 | arXiv:2110.11413, Sect. 2.2 |
| Euclid Flagship 2 | 3600 h⁻¹ Mpc | box replicated and translated around the observer | all sky to z ≈ 2.0; one replication to z_max = 3 | arXiv:2405.13495, Sect. 3 |
| MillenniumTNG lensing runs | 3 Gpc (2.04 h⁻¹ Gpc), 10240³ CDM + 2560³ neutrinos | chosen "to avoid repetitions of the simulation volume along the line of sight" | as stated, extent not read | arXiv:2406.08540, Sect. 3.1 |
| Takahashi et al. full-sky set | 14 nested boxes, 450 to 6300 h⁻¹ Mpc in steps of 450, 2048³ each, 6 realisations per size | three lens shells per box; 18 observer positions per box give 108 realisations | each shell drawn from a box that contains it | arXiv:1706.01472, Sect. II.1–II.2 |

The nested-box design gives better mass and spatial resolution to the
inner shells: particle masses run from 8.2 × 10⁸ to 2.3 × 10¹² h⁻¹ M_⊙
and softenings from 8 to 108 h⁻¹ kpc [src: arXiv:1706.01472, Table 1].
Beyond z = 7.1 the shells are Gaussian surface-density fields from the
linear spectrum, for the CMB-lensing maps [src: Sect. II.2]. An
alternative for narrow surveys remaps the periodic cube one-to-one into an
elongated box, preserving volume and local structure (Carlson & White
2010, arXiv:1003.3178) [src].

### Step 2. Record the cone
<!-- key: step-2-record-the-cone -->

**On the fly.** Particles are written when the light-cone crosses them,
at the time resolution of the N-body step [src: arXiv:2112.05165,
Sect. 9.6]. In Abacus, trajectories are linearly interpolated within each
step to the crossing time and positions and velocities updated to it;
HEALPix maps of all particles are written at N_side = 16384 for 0.3 bytes
per particle after compression, and particle outputs keep only a 10%
subsample [src: arXiv:2110.11413, Sect. 2.2]. The MillenniumTNG
"mass-shell" output stores, per shell of fixed comoving thickness, the
cumulative mass of the particles crossing the hypersurface, at
N_side = 8192 [src: arXiv:2406.08540, Sect. 3.1]. Flagship 2 decomposes
its cone into all-sky shells of about 95.22 Myr in look-back time up to
z = 10, finer at higher redshift, at N_side = 8192 [src: arXiv:2405.13495,
Sect. 3]. The review's caveat: a run that discards particles outside the
cone ("shrinking domain") is incompatible with Newtonian instantaneous
forces, and any such optimisation yields one cone per run [src:
arXiv:2112.05165, Sect. 9.6].

**From snapshots.** Structure at r is taken from the snapshot closest to
a_r; this is accurate on large scales but discontinuous at the snapshot
transitions; interpolating particles underestimates halo central
densities; interpolating haloes along merger trees leaves objects that
appear twice or never; and the method needs 50–100 snapshots [src:
arXiv:2112.05165, Sect. 9.6].

### Step 3. Put haloes on the cone
<!-- key: step-3-put-haloes-on-the-cone -->

AbacusSummit combines both routes, because running a finder on all
light-cone particles needs too much storage, and a "cookie cutter" on
snapshot positions duplicates or misses boundary haloes and displaces
haloes from their own particles, which alters the one-halo term and
galaxy–matter cross-correlations [src: arXiv:2110.11413, Sect. 3.1]:

1. Split the cone into 33 redshift catalogues from z = 0.1 to 8, each
   owning the haloes that cross between its two half-redshifts [src:
   Sect. 3.2].
2. For a halo with a merger-tree progenitor, find the crossing distance
   χ* assuming constant radial velocity between epochs (Eqs. 1–2), then
   interpolate position, velocity and mass linearly to χ* (Eq. 3); mark
   its progenitors ineligible to avoid duplicates [src: Sect. 3.2].
3. Without a progenitor, keep the halo only if it lies inside the shell
   and drift it with its velocity, x_interp = x_i + v_i [t(r_i) − t(χ_i)]
   (1 + z_i) (Eq. 4) [src: Sect. 3.2]. About 1/3 of all haloes have no
   progenitor, but only about 5%, 2.5% and 1% of haloes with 100, 1000 and
   10,000 particles [src: Sect. 3.2, Fig. 3].
4. Match the haloes' subsample particles to the light-cone particle
   output, as satellite tracers [src: Sect. 3.3].

The stated justification of linear motion: at z ≲ 0.5 a halo at
500 km/s moves about 300 kpc between catalogues spaced by Δz = 0.05
[src: Sect. 3.1].

### Step 4. Compute the lensing fields: Born or ray-tracing
<!-- key: step-4-compute-the-lensing-fields-born-or-ray -->

**Born.** Integrating along the unperturbed path gives
κ_born(θ, z_s) = ∫₀^{χ_s} dχ (3H₀²Ω_m/2c²)(1 + z) f_K(χ) f_K(χ_s − χ)/f_K(χ_s)
× δ_m(θ, χ) (Ferlito et al. 2024, arXiv:2406.08540, Eq. 6, neglecting
boundary terms and assuming matter domination) [src: Sect. 2.1]. In
practice it is a weighted sum of the shell maps (the onion universe);
shear, deflection and flexion follow from the lensing potential in
harmonic space, κ_ℓm = −½ ℓ(ℓ + 1) φ_ℓm (Flagship 2, arXiv:2405.13495,
Eq. 2) [src: Sect. 3]. Flagship 2 uses this route and states its
agreement with ray-tracing "in the Born approximation limit" [src: same].
AbacusSummit maps of shear, deflection and convergence for z_s =
0.15–2.45 in steps of 0.05, and for the CMB, are Born maps at
N_side = 16384 [src: arXiv:2305.11935, abstract].

**Beyond Born.** Expanding to second order in the potential adds a
lens–lens coupling term κ_ll and a geodesic term κ_geo,
κ = κ_born + κ_ll + κ_geo + O(Φ³) (arXiv:2406.08540, Eq. 7); κ_ll is the
lowest-order source of rotation ω [src: Sect. 2.1].

**Multiple-plane ray-tracing.** Each shell k is a thin lens with
convergence κ⁽ᵏ⁾ ∝ (1 + z_k)/f_K(χ_k) [Σ⁽ᵏ⁾ − Σ̄⁽ᵏ⁾] (Eq. 9) and lensing
potential from ∇²ψ⁽ᵏ⁾ = 2κ⁽ᵏ⁾ (Eq. 11); deflection and shear matrix are
its first and second covariant derivatives (Eqs. 12–13); ray positions and
the distortion matrix are summed over planes (Eqs. 14–15) or, to save
memory, propagated with the recursion of Hilbert et al. 2009 that needs
only the two previous planes (Eqs. 16–17), starting from β = θ and
A = 1 at the observer [src: arXiv:2406.08540, Sect. 3.2]. On the sphere
the distortion matrix must be parallel-transported between planes [src:
same]. Takahashi et al. solve the shell Poisson equation by spherical
harmonics, assign particles to the nearest pixel, and place lens planes at
r = 150 (i − 0.5) h⁻¹ Mpc and source planes at 150 i h⁻¹ Mpc up to
z_s = 5.3 [src: arXiv:1706.01472, Sect. II.2].

**Interpolation of the fields at the ray positions.** α and U must be
evaluated where each ray actually is, off the pixel centres: nearest grid
point (NGP), bilinear, or a non-uniform FFT (NUFFT) synthesis from the
harmonic coefficients [src: arXiv:2406.08540, Sect. 3.4].

### Step 5. Choose the shell thickness
<!-- key: step-5-choose-the-shell-thickness -->

The multiple-plane approximation drops line-of-sight modes longer than
the shell, and becomes unreliable for too thin planes; MillenniumTNG
therefore uses Δχ = 100 h⁻¹ Mpc [src: arXiv:2406.08540, Sect. 3.2]. The
thickness also filters the shell's own power: for a shell of thickness Δr
at distance r, C_ℓ^shell = r⁻² ∫ dk_∥/2π P_δ(k) sinc²(k_∥ Δr/2) with
k_⊥ = ℓ/r (Takahashi et al. 2017, arXiv:1706.01472, Eq. B5), which tends
to P_δ(ℓ/r)/(r² Δr) for k_∥Δr → ∞ (Eq. B6); thickness matters only for
fluctuations comparable to or larger than Δr [src: App. B]. For
Δr = 150 h⁻¹ Mpc at z = 0.413 it enhances power at ℓ ≲ 10 and suppresses
it at ℓ ≈ 10–100; their ray-tracing uses three contiguous shells per box,
an effective 450 h⁻¹ Mpc, which mitigates it [src: App. B]. GRayTrix puts
each shell at the cone-volume-weighted distance
(3/4)(r₂⁴ − r₁⁴)/(r₂³ − r₁³), slightly beyond its centre, to correct the
volume difference between its halves [src: App. B, footnote].

### Step 6. Attach lensing to galaxies
<!-- key: step-6-attach-lensing-to-galaxies -->

Flagship 2, as MICE before it: find the 3D pixel of the onion grid that
contains the galaxy, read (κ, γ_1, γ_2) of that pixel, assign them [src:
arXiv:2405.13495, Sect. 5.9]. Two limits follow: lensing is accurate only
down to about the pixel scale, and all galaxies in one 3D pixel share the
same lensing values; the remedy stated is a finer N_side or interpolation
[src: same]. Takahashi et al. instead give halo angular positions and
redshifts from the ray-tracing itself, for galaxy–galaxy lensing [src:
arXiv:1706.01472, abstract].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### On-the-fly or snapshot light-cones
<!-- key: on-the-fly-or-snapshot-light-cones -->

- On the fly: every particle at its own crossing time and no snapshot
  storage; but haloes still come from coarse catalogues, so the halo cone
  needs the interpolation of Step 3 [src: arXiv:2110.11413, Sects. 3.1–3.2].
- Snapshots: possible after the run, several observers per box; costs the
  50–100 outputs and the artefacts listed in Step 2 [src:
  arXiv:2112.05165, Sect. 9.6].
- Residual errors of the AbacusSummit hybrid: dispersion of interpolated
  halo velocities and particle positions biased by at most about 2–4%;
  interpolated against particle-averaged centres differ by about
  30 h⁻¹ kpc and 40 km/s for haloes of 2500–5000 particles; both can be
  absorbed by HOD velocity and position parameters; recommended use
  N ≳ 100 particles (M > 2.1 × 10¹¹ h⁻¹ M_⊙ at base resolution) [src:
  arXiv:2110.11413, Sect. 4.4 and abstract]. The ELG multipoles on the
  cone agree with those of the full-box snapshot [src: abstract].

### Born or ray-tracing
<!-- key: born-or-ray-tracing -->

| Statistic | Ray-tracing against Born | Analysis | Place read |
|---|---|---|---|
| κ power spectrum | within 0.2% (NGP) or 0.1% (NUFFT) up to ℓ ≈ 10⁴; differences dominated by interpolation, not by post-Born physics | MTNG, z_s = 1, N_side = 8192 | arXiv:2406.08540, Sect. 4.2 |
| κ PDF | central part within 1%; high tail −1.5% at κ ≈ 0.09; low tail +10% at κ ≈ −0.025; Born overestimates the high tail and underestimates the low one | same | Sect. 4.3 |
| Peaks | −1.5% at κ ≈ 0.15 | same, 1 arcmin smoothing | Sect. 5 |
| Minima | +15% at κ ≈ −0.025, −7% at κ ≈ 0.03 | same | Sects. 4.4, 5 |
| Minkowski functional V_1 | +25% (NGP, NUFFT) at κ ≈ −0.028 | same | Sect. 5 |
| Void abundance and profiles | not significantly affected | same | Sect. 5 |
| Parameter bias, power spectrum | negligible for an LSST-like survey once shape noise is included | 260 h⁻¹ Mpc, 512³ Gadget2 runs, LensTools | arXiv:1612.00852, abstract and Sect. II |
| Parameter bias, κ skewness and kurtosis | up to 2.5σ | same | arXiv:1612.00852, abstract |
| Cost | Born a factor 4 cheaper for the convergence | LensTools | arXiv:1612.00852, abstract |

Post-Born terms Gaussianise the κ distribution, since geodesic
displacements and lens–lens coupling both act as a mixing [src:
arXiv:2406.08540, Sect. 4.3]. Petri et al. find the Born-to-ray-traced
differences in power spectrum, skewness and kurtosis consistent with the
lowest-order post-Born terms alone, implying cancellations among higher
orders [src: arXiv:1612.00852, abstract]. The effect grows with source
redshift [src: arXiv:2406.08540, Sect. 5]. Rule from these two papers: Born
is enough for two-point lensing; higher-order statistics need
ray-tracing.

### Which interpolation
<!-- key: which-interpolation -->

Bilinear interpolation smooths: −1% in C_ℓ at ℓ ≈ 1500, a uniform −2.5% in
peak and minimum counts, up to 40% on the void abundance and 5% on void
profiles; NGP agrees with NUFFT at N_side = 8192 after 1 arcmin smoothing,
but NGP accuracy degrades at lower N_side; NUFFT is the most accurate and
is preferred [src: arXiv:2406.08540, Sects. 4.2, 4.4, 5].

### Large box or tiled small boxes
<!-- key: large-box-or-tiled-small-boxes -->

Test: 11 HalfDome FastPM runs of 3750 h⁻¹ Mpc (6144³, m_p = 1.95 × 10¹⁰
h⁻¹ M_⊙, 60 steps from z = 9, 80 shells with Δa = 0.01 at N_side = 8192)
against 20 runs of 625 h⁻¹ Mpc tiled to the same cone; Born convergence for
z_s = 0.5–2.5; 10° × 10° patches on a Fibonacci grid [src: Tokiwa et al.
2025, arXiv:2511.20423, Sects. 3.1–3.2]. Results [src: abstract,
Sects. 5.1 and 6]:

- Along directions of repeated structure: O(10%) bias in the mean PDF and
  Minkowski functionals, O(1%) in C_ℓ, bispectrum, peaks and minima, and
  O(10%) in covariances, rising with z_s and ℓ to about 25% at
  z_s = 2.5.
- A patch centred on a replication direction under gnomonic projection:
  biases up to O(100%) at high redshift.
- After removing those patches, means agree within 1%, but variances
  differ by 10–30% (super-sample effect), and survey shape noise for DES,
  KiDS, HSC, LSST, Euclid or Roman does not remove it.
- Scaling given by the authors: replication-induced covariance falls as
  L⁻² to L⁻³, so doubling the box cuts it by 4–8; σ_b², the variance of
  the box-scale mode (Eq. 15), is 13.2 times smaller for 1250 than for
  625 h⁻¹ Mpc, turning a 20% SSC effect into about 1.5%.

Their reading: tiling is acceptable for the mean if the affected patches
are cut; covariances need large boxes [src: Sect. 6]. Rotating shells
suppresses repetition but creates discontinuities at shell boundaries,
untested for higher-order statistics [src: Sect. 6].

### Shell thickness
<!-- key: shell-thickness -->

Thinner shells resolve the radial weight better but lose long radial
modes; the Takahashi maps with 150 h⁻¹ Mpc planes underpredict shear
correlations by at most 5–10% at θ = 10–10³ arcmin (ℓ = 10–100) and
overpredict the CMB deflection power by up to 70% at ℓ = 2–10 [src:
arXiv:1706.01472, Sect. V]. Their mocks agree with theory within 5% to
ℓ = 3000 [src: abstract].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Snapshots needed for a snapshot light-cone | 50–100 | review | arXiv:2112.05165 | Sect. 9.6 |
| AbacusSummit light-cone map resolution | N_side = 16384, 0.3 bytes per particle; 10% particle subsample | AbacusSummit | arXiv:2110.11413 | Sect. 2.2 |
| AbacusSummit halo-cone recommended range | ≥ 100 particles, M > 2.1 × 10¹¹ h⁻¹ M_⊙ | base | arXiv:2110.11413 | abstract, Sect. 4.4 |
| Haloes without progenitor | 1/3 overall; 5%, 2.5%, 1% at 10², 10³, 10⁴ particles | AbacusSummit, z = 0.8 | arXiv:2110.11413 | Sect. 3.2 |
| Interpolation residuals | ≤ 2–4% on dispersions; 30 h⁻¹ kpc, 40 km/s on centres | AbacusSummit | arXiv:2110.11413 | Sect. 4.4 |
| Flagship 2 shell width | ≈ 95.22 Myr look-back, to z = 10 | Flagship 2 | arXiv:2405.13495 | Sect. 3 |
| MTNG shell thickness | Δχ = 100 h⁻¹ Mpc | MTNG ray-tracing | arXiv:2406.08540 | Sect. 3.2 |
| Takahashi planes | lens at 150 (i − 0.5), sources at 150 i h⁻¹ Mpc; effective 450 h⁻¹ Mpc continuity | full-sky set | arXiv:1706.01472 | Sect. II.2 |
| Particles per pixel | about 2–10 at N_side = 8192 for z ≳ 0.3 | Takahashi | arXiv:1706.01472 | Sect. II.2 |
| Born vs ray-traced C_ℓ^κ | ≤ 0.1–0.2% to ℓ ≈ 10⁴ | MTNG | arXiv:2406.08540 | Sect. 4.2 |
| Born vs ray-traced minima | +15% at κ ≈ −0.025 | MTNG | arXiv:2406.08540 | Sect. 5 |
| Born bias on κ skewness, kurtosis | up to 2.5σ, LSST-like | Petri et al. | arXiv:1612.00852 | abstract |
| Replication bias | O(10%) on PDF and Minkowski functionals; O(10%) on covariances, about 25% at z_s = 2.5 | 625 tiled vs 3750 h⁻¹ Mpc | arXiv:2511.20423 | abstract |
| Super-sample variance difference | 10–30% | same | arXiv:2511.20423 | Sect. 6 |
| σ_b² ratio | 13.2 between 625 and 1250 h⁻¹ Mpc boxes | same | arXiv:2511.20423 | Sect. 6, Eq. 15 |
| Shell-thickness effect | −5 to −10% on ξ_± at ℓ = 10–100; +70% CMB deflection power at ℓ = 2–10 | Takahashi | arXiv:1706.01472 | Sect. V |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Repeated structure.** Shows up as excess correlation along the box
  axes and a skewed PDF in those patches [src: arXiv:2511.20423,
  Sect. 5.1]. Test: split patches into replication-influenced and
  replication-minimal sets by their position against the symmetry axes of
  the tiling (their criterion, Sect. 5.1) and compare.
- **Gnomonic patch centred on a replication direction.** Up to O(100%)
  bias [src: arXiv:2511.20423, abstract]. Test: check patch centres
  against the axes.
- **Covariance from small boxes.** 10–30% variance deficit even far from
  repeated directions [src: arXiv:2511.20423, Sect. 6]; see
  `cosmo-statistics-inference` for corrections.
- **Grid-aligned shot noise.** Particles started on a lattice barely move
  at high redshift, so projected shells show noisy arcs at θ = π/2 and
  φ = 0, π/2, π, 3π/2; more serious for the convergence than for the
  deflection, and for high z_s; a glass load avoids it [src:
  arXiv:1706.01472, Sect. V].
- **Low-z_s convergence below the empty-beam value, B-mode excess.** Small
  anomalies of the Takahashi maps attributed to finite angular resolution,
  negligible "for most practical purposes" [src: arXiv:1706.01472,
  Sect. V].
- **Interpolation smoothing taken for physics.** Bilinear smoothing
  exceeds post-Born effects at N_side = 8192 [src: arXiv:2406.08540,
  Sect. 5]. Test: rerun with NGP and NUFFT.
- **Born maps for higher-order statistics.** Minima, PDF tails and
  Minkowski functionals move by 10–25% [src: arXiv:2406.08540, Sect. 5].
- **Galaxies sharing a pixel's lensing.** Small-scale galaxy–galaxy
  lensing below the pixel scale is not modelled [src: arXiv:2405.13495,
  Sect. 5.9].
- **Halo duplication or loss at shell boundaries.** Snapshot cones (review)
  and cookie-cutter haloes (AbacusSummit); in the AbacusSummit hybrid about
  0.0003% of subsample particles are lost at shell boundaries [src:
  arXiv:2112.05165, Sect. 9.6; arXiv:2110.11413, Sects. 3.1, 3.3].

Validation stated by the papers: AbacusSummit compares ELG multipoles on
the cone with the snapshot, and CMB convergence auto- and cross-spectra
with theory at the sub-percent level [src: arXiv:2110.11413, abstract];
Flagship 2 compares C_ℓ^κ at z_s = 1 and 3 with the revised HALOFIT
within sample variance [src: arXiv:2405.13495, Sect. 3]; Takahashi et al.
compare with theory within 5% to ℓ = 3000 [src: arXiv:1706.01472,
abstract].

## Reading list
<!-- key: reading-list -->

- Review: Angulo & Hahn 2021, arXiv:2112.05165, Sect. 9.6 — the two
  routes to a light-cone, replication, snapshot needs.
- Method: Hadzhiyska et al. 2021, arXiv:2110.11413 — haloes on an
  on-the-fly particle cone, step by step, with residual errors.
- Application: Hadzhiyska et al. 2023, arXiv:2305.11935 — public
  AbacusSummit Born lensing maps and lensing mocks.
- Application: Euclid Collaboration 2024, arXiv:2405.13495, Sects. 3, 5.9 —
  onion shells, Born maps, galaxy lensing assignment.
- Method: Takahashi et al. 2017, arXiv:1706.01472 — nested boxes,
  multiple-plane ray-tracing, shell-thickness theory, known issues.
- Critique: Petri et al. 2016, arXiv:1612.00852 — when Born biases
  parameters.
- Critique: Ferlito et al. 2024, arXiv:2406.08540 — full-sky ray-tracing
  versus Born, interpolation schemes.
- Critique: Tokiwa et al. 2025, arXiv:2511.20423 — replication and
  super-sample effects measured.
- Method: Carlson & White 2010, arXiv:1003.3178 — volume remapping of a
  periodic box.

## Not verified
<!-- key: not-verified -->

- Hilbert et al. 2009 (the plane recursion), Becker 2012 (CALCLENS,
  arXiv:1210.3069, title seen) and Das & Bode 2008 (thin planes): cited
  through arXiv:2406.08540 only.
- The shell-rotation scheme of Omori 2024 and the hierarchy of slices of
  Sato et al. 2009: cited through arXiv:2511.20423 only.
- Zorrilla Matilla et al. 2020 on shell thickness for non-Gaussian
  statistics: not found by the search; cited through arXiv:2406.08540.
- Petri et al.'s parameter-bias scaling with galaxy density (their Fig. 6)
  and the Born-versus-ray-tracing numbers of the post-Born terms (Eqs. 9–10
  there): not read.
- The on-the-fly hypersurface algorithm of GADGET-4 and PKDGRAV3: not read.
- The extent of the non-repeated region of the MTNG 3 Gpc box: not read.
