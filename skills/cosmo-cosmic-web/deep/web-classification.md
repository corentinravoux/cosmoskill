# Web classification applied to galaxy surveys — cosmo-cosmic-web dossier

Scope: how a web classification is built from a real galaxy catalogue
(tracer selection, redshift-space treatment, DisPerSE, Bisous and T-web
set-up, persistence and threshold calibration, survey edges, photometric
redshifts), how each choice is validated on mocks, and what is known about
the agreement of finders run on the same data.
Snapshot: 2026-10-17.
From: Libeskind et al. 2018, Sect. 1.4, 2 and 4.

Already in L2, not repeated here: the list of finders with their defining
equations and the parameters used on the simulation of the comparison
project (`physics-and-methods.md#classification-schemes-and-structure-finders`);
the mass and volume fractions per finder (`results.md#mass-and-volume-fractions-per-web-component`);
the effect of the eigenvalue threshold and of smoothing
(`systematics.md#smoothing-scale-and-threshold`); redshift-space and
photometric-redshift damage in general terms
(`systematics.md#redshift-space-distortions-photometric`); probabilistic
reconstructions (BORG, ASTRA, Cosmicflows) in
`physics-and-methods.md#reconstructing-the-web-from-data`. Void finders
built for cosmology are in `cosmo-beyond-two-point`
(`deep/void-finding-size-function.md`).

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Choose the tracer sample
<!-- key: step-1-choose-the-tracer-sample -->

- **Constant comoving density.** For skeletons at z = 0–4 in MillenniumTNG,
  Galárraga-Espinosa et al. (2024, arXiv:2309.08659) select all subhaloes
  with M* > 10⁹ M☉ at z = 0, N_gal = 3,083,441, a density n_gal = 7.7 ×
  10⁻³ Mpc⁻³ "compatible with" DESI BGS at low redshift, and the same
  number of most massive subhaloes at each higher redshift, "precisely with
  the goal of working at constant (comoving) density of tracers", so that
  high-z filaments belong to the same spatial scales [src: Sect. 3.1]. They
  reject the progenitors of z = 0 galaxies as tracers because no survey can
  select them and because they are poor tracers of the largest scales [src:
  Sect. 3.1, App. A].
- **Flux-limited sample with distances rescaled.** Kraljic et al. (2018,
  arXiv:1710.02676) run DisPerSE on the flux-limited GAMA sample and
  normalise every distance to the skeleton by the redshift-dependent mean
  inter-galaxy separation ⟨D_z⟩ ≡ n(z)^(−1/3), n(z) the galaxy number
  density at z, "to account for the variation of the sampling throughout
  the survey"; ⟨D_z⟩ runs from 3.5 to 7.7 Mpc over 0.03 ≤ z ≤ 0.25, mean
  ~5.6 Mpc [src: Sect. 3.2].
- **Galaxies, not matter.** Compared with skeletons from the dark matter,
  galaxy tracers have "a negligible impact on the positions" of filaments
  (Laigle et al. 2018, Appendix C, as cited in arXiv:2309.08659, Sect. 3.1)
  but change the number recovered (Zakharova et al. 2023,
  arXiv:2307.05240). In GAEA, with DisPerSE tuned to give the same total
  skeleton length for both tracers and the 10% shortest filaments removed,
  about 60% of dark-matter filaments have a galaxy counterpart for M* > 10⁹
  M☉, and about 41% do not contain enough galaxies to be detected whatever
  the mass cut; neither adding M* < 10⁹ M☉ galaxies nor keeping only M* >
  10¹⁰ M☉ improves the match [src: arXiv:2307.05240, Sect. 5].

### Step 2. Treat redshift-space distortions before the finder
<!-- key: step-2-treat-redshift-space-distortions-before -->

| Analysis | Treatment | Stated reason | Place read |
|---|---|---|---|
| GAMA, DisPerSE (arXiv:1710.02676) | anisotropic friends-of-friends groups, compressed radially until transverse and radial dispersions are equal; only groups with more than six members | the Fingers of God (FoG) "may lead to the identification of spurious filaments"; the Kaiser effect, "expected to be much less significant", is not corrected; only large groups are elongated; "the precise correction of the FoG effect is not sought" | Sect. 2.2 |
| SDSS MGS and LOWZ+CMASS, DisPerSE (Malavasi et al. 2020, arXiv:2002.01486) | around each known cluster, remove galaxies in a cylinder of radius 3 R_vir and half-height dz = 3(σ_v/c)(1 + z), σ_v = (G M_vir/5R_vir)^(1/2); add one particle at the cluster carrying the mean DTFE density of the removed galaxies; rebuild the tessellation without recomputing densities | keeping old densities "avoids the formation of spurious minima" in the holes; the method changes the shape of the field but not its values | Sect. 5.1 |
| SDSS, Bisous (arXiv:1308.2816) | groups spherised with friends-of-friends | suppress FoG | see `deep/spin-alignments.md#step-1-build-the-skeleton-the-spins-are` |
| SDSS T-web variables (Alam et al. 2019, arXiv:1801.04878) | none: work in redshift space with uncorrected Kaiser anisotropy; δ₈ on 8 h⁻¹Mpc spheres | 8 h⁻¹Mpc is large enough to make FoG negligible; a model-dependent correction is avoided; mocks are processed identically | Sect. 3.3, 3.4 |
| DESI DR1 T-web (Ullah et al. 2026, arXiv:2604.02463) | none stated in the method | the authors note that RSD and survey boundaries "could smooth environmental contrasts" relative to simulations | Sect. 4.5 |

Malavasi et al. find the Coma line-of-sight filament still present after
removal, though reshaped, and the distributions of filament length,
critical-point density, connectivity and curvature L_S/L_C (straight-line
over path length) unchanged; for the straightest filaments (L_S/L_C >
0.99) the angle to the line of sight is "rather uniform" with or without
the correction [src: arXiv:2002.01486, Sect. 5.1].

### Step 3. Topological route: DisPerSE
<!-- key: step-3-topological-route-disperse -->

The procedure as written in the "user's guide" of arXiv:2309.08659 (Sect.
2.2), which gives the command-line keywords:

1. `delaunay_3d` computes the Delaunay tessellation field estimator (DTFE)
   density ρ_DTFE at each tracer, with `--btype periodic` for a box.
2. `netconv --smoothData field_value N1` replaces each vertex density by
   the mean of its tessellation neighbours, N1 times, "effectively reducing
   the contamination by shot noise". Malavasi et al. call N1 = 0, 1, 2
   SD0, SD1, SD2 (smoothing cycles) [src: arXiv:2002.01486, Sect. 3.1].
3. `mse --forceLoops --robustness --manifolds --upSkl -nsig N2` finds the
   critical points and the ridges joining maxima (CPmax) to saddles, and
   cancels persistence pairs below N2.
4. `skelconv --to NDskl_ascii -smooth 1` writes the skeleton; the `-smooth`
   step moves segment positions, "exclusively for aesthetic reasons" in
   arXiv:2309.08659 [src: Sect. 2.2]. Skeleton smoothing averages each
   segment end with its neighbours [src: arXiv:2002.01486, Sect. 3.1]; it
   can shift the filament axis and change density profiles if overdone
   [src: arXiv:2307.05240, Sect. 2.2].

N1 and N2 are "the only two parameters of the code" [src: arXiv:2309.08659,
Sect. 2.2], which qualifies the "parameter-free apart from persistence"
description quoted in L2 from the DisPerSE abstract.

**What N2 means.** For a persistence pair q_k of critical simplices of
order k and k + 1, the persistence ratio is r(q_k) = F_ρ(σ_{k+1})/F_ρ(σ_k)
(Sousbie 2011, arXiv:1009.4015, Eq. 3), F_ρ the DTFE density at each
simplex; its significance in "sigmas" is S(q_k) = Erf⁻¹((P_k(r) + 1)/2)
(Eq. 4), with P_k(r) the Monte Carlo probability that a pair of ratio ≥ r
exists in a Poisson sample, fitted in Eqs. 5–7 (3D) and 8–9 (2D) [src:
Sect. 6.3]. N2 is therefore a significance against Poisson noise, not a
density contrast; the probability that a feature is spurious is quoted as
~5% at 2σ and 0.006% at 4σ (Sousbie 2011 and Malavasi et al. 2017, as cited
in arXiv:2002.01486, Sect. 3.1).

**Post-processing.**

- *Cleaning.* Remove zero-length filaments between superposed maxima and
  saddles (Poisson-noise defects) and maxima connected to a single
  filament, on the prior that such nodes are not expected (Codis et al.
  2018 as cited) [src: arXiv:2309.08659, Sect. 2.2; arXiv:2002.01486, Sect.
  3.3, Table 4]. In SDSS the counts removed fall from 1833 (MGS, SD0, 3σ)
  to 1 (SD2, 5σ) [src: arXiv:2002.01486, Table 4].
- *Edges.* With smooth boundary conditions DisPerSE adds guard particles
  outside the domain, following the interpolated density, and tags every
  critical point and filament touched by them; bifurcation points are added
  afterwards and carry no tag. Malavasi et al. remove tagged points and
  bifurcations within 100 Mpc (MGS) or 200 Mpc (LOWZ+CMASS) of the convex
  hull of tagged points, "a very conservative cut" chosen only to show the
  effect; they suggest a redshift-dependent criterion for users [src:
  arXiv:2002.01486, Sect. 3.2]. Interior holes are not tagged because the
  tetrahedra cross them, interpolating the density over empty regions
  [src: same].
- *Disconnected structures.* In MTNG, filaments whose nodes match no
  massive halo (8.5% at z = 0, 22.7% at z = 4) are discarded as structures
  connecting low-mass haloes [src: arXiv:2309.08659, Sect. 3.3, Table 1].

### Step 4. Calibrate the persistence threshold on mocks
<!-- key: step-4-calibrate-the-persistence-threshold-on -->

No paper read defines a true skeleton. Galárraga-Espinosa et al. argue that
comparing finders characterises methods "but would not provide conclusive
results regarding the accuracy" [src: arXiv:2309.08659, Sect. 3.2], and use
a physical anchor instead: the fraction of CPmax inside R₂₀₀c of a massive
friends-of-friends halo (purity) and the fraction of clusters (M₂₀₀c ≥ 5 ×
10¹³ h⁻¹M☉) hosting a CPmax (completeness), over eight skeletons (N1 = 0 or
1, N2 = 1–4σ). The best are smoothed 2σ (S, 2σ) and unsmoothed 4σ (noS,
4σ); the latter has filaments as short as 0.03 Mpc, "likely" noise, so
S, 2σ is adopted "given the n_gal density of tracers" [src: Sect. 3.2,
App. B Table 2]. The same parameters are kept at all redshifts to retrieve
structures of the same scale and density contrast [src: Sect. 3.3].

The miniJPAS+DESI analysis calibrates its own data the same way and adopts
3σ [src: arXiv:2506.15345, Sect. 4.2], which shows that the threshold
depends on tracer density and geometry (2D local cylinders there), not on
a universal value.

### Step 5. Stochastic route: Bisous
<!-- key: step-5-stochastic-route-bisous -->

Bisous fills the volume with marked cylinders and minimises an energy by
Metropolis–Hastings with simulated annealing; stacking realisations gives a
visit map (probability that a cylinder covers a point) and a directional
strength (alignment of the cylinders), both in [0, 1] [src: Muru & Tempel
2021, arXiv:2103.06619, Sect. 3]. Settings in use: visit-map threshold
0.05, "close to the signal-to-noise ratio for a Poisson process", and
directional strength 0.8, calibrated to minimise noise, resemble a
filamentary network visually and give an appropriate volume fill [src:
same]; the comparison project used orientation strength > 0.7 (L2). The
filament radius is fixed near 1 Mpc, "found to be the most suitable for
filaments traced by gas" in a hydrodynamical simulation; several hundred to
a thousand realisations are stacked [src: Sects. 3, 4.2]. Across N_R = 200
full runs, a galaxy's filament probability is
P = Σ_R 1{vm_R ≥ vm_t ∧ ds_R ≥ ds_t}/N_R (Eq. 1), vm and ds the visit-map
and directional-strength values and vm_t, ds_t the thresholds [src: Sect.
4.3].

### Step 6. Hessian route: a T-web from galaxies
<!-- key: step-6-hessian-route-a-t-web-from-galaxies -->

DESI DR1 (arXiv:2604.02463):

1. Cloud-in-cell assignment of galaxies and randoms, with DESI clustering
   weights, on a 256³ grid in an 800 Mpc box (3.125 Mpc cells) [src: Sects.
   3.1–3.2].
2. ϱ(x) = n_g(x)/(γ n_r(x)) − 1, γ = Σw_g/Σw_r (Eq. 2), n_g and n_r the
   weighted galaxy and random fields; Gaussian smoothing R_s.
3. ∇²Φ = ϱ (Eq. 3), solved as Φ̂(k) = −ϱ̂(k)/k² with the k = 0 mode set to
   zero (Eq. 4); T_ij = ∂²Φ/∂x_i∂x_j (Eq. 5), eigenvalues λ₁ > λ₂ > λ₃.
4. λ_th = 0; environments kept only in cells "well sampled by the random
   catalogue" to mitigate window effects [src: Sect. 3.1].

R_s = 10 Mpc (BGS), 7 Mpc (LRG), 10 Mpc (ELG) are "representative" values
of tracer-dependent ranges; no galaxy-bias rescaling or RSD correction is
described [src: Sect. 3.2].

SDSS (arXiv:1801.04878):

1. Cut the light cone to a box of 195 × 340 × 198 h⁻¹Mpc keeping 98.5% of
   galaxies (65% of the box filled) [src: Sect. 3.1].
2. Density at each galaxy from a Voronoi-type estimate, near masks and
   edges from the count of nearest randoms, which encode the angular and
   radial selection [src: Sect. 3.2].
3. Interpolate to 5 h⁻¹Mpc cells and smooth with a 5 h⁻¹Mpc Gaussian;
   ∇²Φ = 4πGρ̄ δ_g^s/b_g (Eq. 1), δ_g^s the redshift-space galaxy
   overdensity and b_g the linear bias, reduced to ∇²Φ̃ = δ_g^s (Eq. 2);
   T̃_ij^k = k_i k_j δ_g^k/k² (Eq. 4) [src: Sect. 3.3]. The bias drops out
   of the sign pattern of the eigenvalues; RSD are ignored, "reasonable on
   large linear scales" [src: same].
4. Continuous variables instead of classes: δ₈ (Eq. 5), tidal torque q²_R
   (Eq. 6), tidal anisotropy α₅ = (q²₅)^(1/2)(1 + δ₅)^(−0.55) (Eq. 7); n =
   0.55 instead of Paranjape et al.'s n = 1, because the δ–α correlation
   depends on smoothing and on the bias of the sample, and a fixed R = 5
   h⁻¹Mpc replaces 4R₂₀₀b, unknown for galaxies [src: Sect. 3.4].

### Step 7. Photometric redshifts: classify in 2D
<!-- key: step-7-photometric-redshifts-classify-in-2d -->

- **Slices (Euclid preparation, arXiv:2508.15915).** DisPerSE in 2D on
  overlapping slices of 75 comoving Mpc (39 slices for 0.1 ≤ z ≤ 0.5,
  mean width Δz = 0.02), a thickness larger than δ₇₀, the interval holding
  70% of a galaxy's photo-z PDF, for M* > 10¹⁰ M☉ [src: Sect. 3.2]. A
  galaxy enters a slice if its PDF integral in the slice exceeds p_t (0.2–
  0.6); mass limits log M_lim = 10.0, 10.25, 10.5; no density smoothing
  "so as not to introduce another variable", two skeleton-smoothing passes
  needed for angle measurements; N_σ^2D = 2.0–3.5 [src: Sect. 3.2]. The
  reference is a 3D true-z skeleton (M* ≥ 10⁹ M☉, N_σ^3D = 5.5–8.0) cut
  into the same slices and projected, keeping only filaments and
  filament-type saddles, so that projected walls cannot pose as filaments
  in the reference [src: Sect. 3.3].
- **Monte Carlo local cylinders (miniJPAS+DESI, arXiv:2506.15345).** 100
  realisations of the catalogue drawn from the redshift uncertainties;
  around each of 1547 targets a cylinder of radius 3 pMpc and height 2 × 15
  pMpc, the height set by the confusion length (~20 pMpc at z = 0.2, 35
  pMpc at z = 0.8); stellar-mass-weighted Delaunay vertices, which enhance
  the contrast and give more robust nodes (Kuchner et al. 2020, as cited);
  connectivity K counted at 20 R₁, R₁ a stellar-mass-based galaxy size,
  and K_MC the median over realisations [src: Sects. 4.1–4.4].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Density smoothing against persistence
<!-- key: density-smoothing-against-persistence -->

On MTNG galaxies (Table 2 of arXiv:2309.08659, z = 0): without smoothing,
1σ gives 697,234 filaments with 72.7% of CPmax matched to a halo; with one
smoothing cycle, 2σ gives 169,497 filaments, 90.6% matched, and 91.3% of
clusters hosting a CPmax; smoothed 4σ keeps 94.4% purity but only 59.1% of
clusters [src: App. B]. Smoothing and persistence trade against each other:
noS 4σ reaches 89.6% purity and 91.3% cluster completeness, close to S 2σ,
but leaves 0.03 Mpc filaments [src: same]. In SDSS each smoothing cycle
also raises the fraction of critical points lost to edges, from 22% (SD0)
to 52% (SD2) at 3σ in the MGS [src: arXiv:2002.01486, Table 3]. With one
smoothing cycle on LOWZ+CMASS, 5σ crashed the code ("it tries to cancel too
many low-persistence pairs"), so 4.5σ was used [src: Sect. 3.1].

### Tracer density
<!-- key: tracer-density -->

- Bisous on MDPL2 galaxies (12 subsets, magnitude limits −21 to −18.5 and
  random dilutions of equal size): filament volume fill and galaxy fraction
  fall monotonically with density; >97% of galaxies classified in filaments
  in a sparse subset are also in filaments in denser ones; 10–15% of grid
  points flagged as filament in sparse subsets are not in the densest; the
  authors judge ~85% of detected filaments reliable at every density [src:
  arXiv:2103.06619, Sect. 4.2]. Random dilution gives lower fractions than
  magnitude cuts, indicating that filaments preferentially hold bright
  galaxies [src: same].
- 2D photo-z DisPerSE: raising p_t or M_lim removes tracers and pushes the
  best-matching 3D skeleton to higher persistence; "the number of tracers
  used has a greater impact on our reconstruction than photo-z
  uncertainty", so looser cuts with noisier redshifts help [src:
  arXiv:2508.15915, Sects. 7.3, 8].
- T-ReX against sparse sampling (2D Illustris slice): with 83% and 60% of
  subhaloes, >95% of the original pattern lies within 1.8 h⁻¹Mpc of the
  new one; with 31%, 90% within 3 h⁻¹Mpc [src: arXiv:1912.00732, Sect.
  6.1.2].

### T-web threshold and smoothing on galaxy fields
<!-- key: t-web-threshold-and-smoothing-on-galaxy-fields -->

With λ_th = 0 the DESI BGS volume fractions barely move with smoothing:
voids 15.6% to 15.2%, filaments 38.0% to 38.5% for R_s = 6–11 Mpc [src:
arXiv:2604.02463, App. A.1 Table 2]; across tracers at representative
scales voids range from 7.40% (ELG) to 15.27% (BGS) [src: Table 1]. The
classification is thus stable in R_s but not across tracers, which the
authors attribute to "galaxy bias and redshift coverage" [src: Sect. 3.2].
Alam et al. avoid classes altogether: continuous (δ₈, α₅) with α₅
decorrelated from δ₈ [src: arXiv:1801.04878, Sect. 3.4].

### Agreement between finders on the same data
<!-- key: agreement-between-finders-on-the-same-data -->

- **SDSS through BORG.** On the posterior of the BORG reconstruction of the
  SDSS main sample, T-web, DIVA (shear of the Lagrangian displacement,
  Eq. 4) and ORIGAMI (shell-crossing count) were compared by information
  content rather than voxel overlap. The expected information gain U₁
  (Eqs. 10–12; Kullback–Leibler divergence of the posterior web-type
  probabilities from the prior, averaged over 3,148,504 observed voxels of
  256³) is 0.4573 Sh (T-web), 0.2664 Sh (DIVA), 0.1347 Sh (ORIGAMI); the
  artefact proxy U₁′, information gain in unobserved regions, favours DIVA
  [src: Leclercq et al. 2016, arXiv:1606.06758, Sect. III.1, Table 4]. All
  three agree on red galaxies in clusters and blue in sheets and voids
  [src: Sect. IV]. At first order (Zel'dovich) T-web and DIVA classify
  identically [src: Sect. II.2]. ORIGAMI is usable here only because BORG
  supplies initial conditions; on a catalogue it still needs particles
  (L2).
- **MaNGA 2D.** Cosmic Web Reconstruction and Bisous skeletons give the
  same null alignment (`deep/spin-alignments.md#finder-persistence-and-smoothing`).
- **DESI.** T-web DR1 and ASTRA EDR void fractions differ by a factor of
  four to ten (L2, `results.md#mass-and-volume-fractions-per-web-component`).
- **Simulation slice.** DisPerSE at smoothing 1 overlaps the unthresholded
  T-ReX probability map best at σ_p = 0; there is "no direct
  transposition" of persistence into a T-ReX probability threshold [src:
  arXiv:1912.00732, Sect. 6.1.1].
- **Skeleton-to-skeleton metric.** Distances between segment midpoints in
  both directions (A→B and B→A), angles between matched segments, and Ξ =
  (W · S)^(1/2) with S = (Δ_D, Δ_A) combining residual-shape differences and
  peak values (Eqs. 3–5); the authors call it neither unique nor optimal
  [src: arXiv:2508.15915, Sects. 4.1, 6.3].

No paper read reports a voxel- or galaxy-level overlap fraction between
two finders run on one galaxy redshift survey.

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Tracer density for MTNG skeletons | n_gal = 7.7 × 10⁻³ Mpc⁻³ (M* > 10⁹ M☉), held fixed in number to z = 4 | MTNG | arXiv:2309.08659 | Sect. 3.1 |
| Calibrated DisPerSE set-up | DTFE smoothed once, 2σ; 169,497 filaments, 41,064 CPmax, median length 9.8 Mpc | MTNG z = 0 | arXiv:2309.08659 | App. B Table 2 |
| Filaments kept after node matching | 91.5% (z = 0) to 77.3% (z = 4) | MTNG | arXiv:2309.08659 | Table 1 |
| Spurious-feature probability (as cited) | ~5% at 2σ, 0.006% at 4σ | DisPerSE | arXiv:2002.01486 | Sect. 3.1 |
| SDSS persistence cuts | 3σ and 5σ (4.5σ for LOWZ+CMASS SD1) | SDSS catalogue | arXiv:2002.01486 | Sect. 3.1 |
| Critical points lost to edges | MGS 3σ: 22% (SD0), 35% (SD1), 52% (SD2); LOWZ+CMASS 3σ: 13%, 26%, 45% | SDSS | arXiv:2002.01486 | Table 3 |
| FoG cylinder | R = 3 R_vir, dz = ±3(σ_v/c)(1 + z) | SDSS | arXiv:2002.01486 | Sect. 5.1 |
| FoG compression threshold | groups with > 6 members | GAMA | arXiv:1710.02676 | Sect. 2.2 |
| GAMA sampling scale | ⟨D_z⟩ = 3.5–7.7 Mpc, mean ~5.6 Mpc | GAMA | arXiv:1710.02676 | Sect. 3.2 |
| Node exclusion for filament gradients | D_node > 3.5 Mpc (group size ~1.5 Mpc) | GAMA | arXiv:1710.02676 | App. B.1 |
| Bisous thresholds | visit map 0.05, directional strength 0.8; radius ~1 Mpc; grid step 0.2 Mpc | MDPL2 mocks | arXiv:2103.06619 | Sect. 3 |
| Bisous run-to-run stability | ~60% of galaxies classified identically in 95% of 200 runs; R = 0.98 between runs; vm = 0.05 gives ~40% chance of filament membership | MDPL2 mag2 (SDSS-like at 100 Mpc) | arXiv:2103.06619 | Sect. 4.3, Table 2 |
| DESI T-web grid | 800 Mpc, 256³, 3.125 Mpc cells, λ_th = 0 | DESI DR1 | arXiv:2604.02463 | Sects. 3.1–3.2 |
| SDSS T-web grid | 5 h⁻¹Mpc cells, 5 h⁻¹Mpc Gaussian; α₅ exponent 0.55 | SDSS NYU-VAGC | arXiv:1801.04878 | Sects. 3.3–3.4 |
| Euclid photo-z requirement | scatter < 0.05(1 + z), outliers < 10% | Euclid Wide | arXiv:2508.15915 | Sect. 2 |
| 2D slice set-up | 75 cMpc, 39 overlapping slices, p_t = 0.2–0.6, N_σ^2D = 2.0–3.5 | GAEA light cone, ~22 deg² | arXiv:2508.15915 | Sects. 2, 3.2 |
| 2D–3D persistence mapping | N_σ^2D > 3 matches the highest-persistence 3D skeleton; 2–2.5 the lowest | same | arXiv:2508.15915 | Sect. 7.3 |
| Galaxy versus dark-matter skeleton | ~60% of DM filaments recovered (M* > 10⁹ M☉); ~41% undetectable; 65% of haloes > 10^13.5 M☉ crossed by a filament | GAEA, 27 volumes | arXiv:2307.05240 | Sect. 5 |
| Information gain U₁ | T-web 0.4573, DIVA 0.2664, ORIGAMI 0.1347 Sh | SDSS via BORG | arXiv:1606.06758 | Table 4 |
| Local 2D cylinders | radius 3 pMpc, height 30 pMpc, 100 realisations, 3σ | miniJPAS+DESI | arXiv:2506.15345 | Sects. 4.1–4.3 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Noise filaments.** Low persistence without smoothing gives impure
  skeletons (72.7% purity at noS 1σ) and sub-0.1 Mpc filaments [src:
  arXiv:2309.08659, App. B]. Test: CPmax–halo matching and the
  short-length tail of the length function on a mock at the survey's
  density.
- **Over-pruning.** High persistence loses clusters as nodes (59.1%
  completeness at S 4σ) [src: same]. Test: same matching, completeness side.
- **Edge-tagged features kept.** Edge contamination rises with smoothing
  (Table 3 of arXiv:2002.01486); bifurcations are never tagged [src: Sect.
  3.2]. Test: compare statistics with and without the edge cut and check
  that removed points follow the overall n(z) [src: Sect. 3.2, Fig. 6].
- **Interior masks treated as data.** DTFE interpolates across holes [src:
  arXiv:2002.01486, Sect. 3.2]; grid methods instead restrict to cells
  well sampled by randoms [src: arXiv:2604.02463, Sect. 3.1]. Test: mask
  mocks identically.
- **FoG filaments.** Spurious line-of-sight filaments [src:
  arXiv:1710.02676, Sect. 2.2]. Test: distribution of the angle between
  straight filaments and the line of sight, which should be uniform [src:
  arXiv:2002.01486, Sect. 5.1]; the GAMA excess of line-of-sight segments
  is in `deep/spin-alignments.md#step-3-assign-each-galaxy-to-a-filament-segment`.
- **Sampling gradients read as environment.** In a flux-limited survey
  distances to filaments grow with redshift because tracers thin out; test
  by normalising by ⟨D_z⟩ [src: arXiv:1710.02676, Sect. 3.2] or with a
  volume-limited or constant-density sample [src: arXiv:2309.08659, Sect.
  3.1]. A declination or other large-scale density trend can do the same;
  test with length functions in sky slices [src: arXiv:2002.01486, Sect.
  5.3].
- **Node gradients posing as filament gradients.** Test: exclude D_node <
  3.5 Mpc and reshuffle D_skel in bins of D_node (20 samples, 20 bins); the
  filament gradient should survive [src: arXiv:1710.02676, App. B.1].
- **Stochastic finder treated as deterministic.** A single Bisous run
  classifies borderline galaxies inconsistently; use the probability of
  Eq. 1 of arXiv:2103.06619 or the stacked visit map [src: Sect. 4.3].
- **2D skeletons over-read.** Mass gradients survive photo-z but are
  shallower; connectivity–mass "cannot be unequivocally detected even in
  our reference 3D-projected case" at that sampling [src:
  arXiv:2508.15915, Sect. 8].
- **Tracer bias read as missing structure.** Galaxy skeletons miss ~41% of
  dark-matter filaments and undercount filaments ending in massive clusters
  [src: arXiv:2307.05240, abstract and Sect. 5].

## Reading list
<!-- key: reading-list -->

- Foundation: Sousbie 2011, arXiv:1009.4015 — persistence ratio and its
  Poisson significance (Sect. 6.3, Eqs. 3–9).
- Method: Galárraga-Espinosa et al. 2024, arXiv:2309.08659 — DisPerSE
  commands, cleaning, calibration by CPmax–halo matching (Sect. 2.2, 3.2,
  App. B).
- Data: Malavasi et al. 2020, arXiv:2002.01486 — public SDSS DisPerSE
  catalogue; edges, minor defects, FoG removal and their validation.
- Method: Muru & Tempel 2021, arXiv:2103.06619 — Bisous thresholds,
  density dependence and run-to-run reliability.
- Application: Kraljic et al. 2018, arXiv:1710.02676 — GAMA set-up:
  flux-limited sample, FoG compression, ⟨D_z⟩ normalisation, node tests.
- Application: Ullah et al. 2026, arXiv:2604.02463 — T-web on DESI DR1
  with randoms and clustering weights.
- Application: Alam et al. 2019, arXiv:1801.04878 — T-web from galaxies
  with randoms at edges; continuous δ₈ and α₅.
- Method: Euclid Collaboration (Malavasi et al.) 2025, arXiv:2508.15915 —
  2D photo-z skeletons validated against projected 3D ones.
- Method: Galárraga-Espinosa et al. 2025, arXiv:2506.15345 — probabilistic
  local 2D DisPerSE with Monte Carlo redshifts.
- Critique: Zakharova et al. 2023, arXiv:2307.05240 — galaxy versus
  dark-matter skeletons.
- Critique: Leclercq et al. 2016, arXiv:1606.06758 — choosing a classifier
  by utility on SDSS posterior maps.
- Method: Bonnaire et al. 2020, arXiv:1912.00732 — graph-based T-ReX and
  its comparison with DisPerSE.

## Not verified
<!-- key: not-verified -->

- Laigle et al. 2018 (COSMOS2015 2D skeletons, Appendix C on galaxy versus
  matter skeletons), Malavasi et al. 2017, Kuchner et al. 2020 (mass
  weighting) and Codis et al. 2018 (single-filament nodes): read only as
  cited in arXiv:2309.08659, arXiv:2002.01486 and arXiv:2506.15345.
- The calibration "Appendix C of Galárraga-Espinosa et al. (2023)" cited by
  arXiv:2506.15345 was not identified; it may not be arXiv:2309.08659,
  whose calibration is in Sect. 3.2 and App. B.
- Table 1 of arXiv:2103.06619 (galaxy densities of the subsets) did not
  render; the subset densities are not given here.
- The full ELG and LRG smoothing tables of arXiv:2604.02463 (App. A.2–A.3)
  were not read.
- Bahé & Jablonka 2025 (filament identification in simulations) and Cohn
  2021 (clusters in DisPerSE webs) were found in searches but not read.
