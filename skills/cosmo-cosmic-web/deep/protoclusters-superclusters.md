# Protoclusters and superclusters — cosmo-cosmic-web dossier

Scope: how a protocluster candidate is selected from a galaxy overdensity
(estimator, aperture, threshold, contamination test), how its descendant
mass and its probability of being a protocluster are calibrated on
simulations, how a supercluster is delimited (percolation, density level,
future collapse, velocity basins), and how the mass, shape and dynamical
state of either structure are estimated, with what each choice costs.
Snapshot: 2026-10-19.
From: M. Einasto 2025 supercluster review, Sect. 2, 11-13; HSC, LATIS and
Lyα protocluster surveys.

Already in L2, not repeated here: headline objects and the z > 5
abundance debate (`results.md#protoclusters`, `results.md#superclusters`,
`open-questions.md#protoclusters-tracer-discrepancies-and-abundance`).
Protoclusters in Lyα tomographic maps: `cosmo-lyman-alpha`
`deep/tomography-voids.md`, Step 7.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Fix what "protocluster" means before measuring anything
<!-- key: step-1-fix-what-protocluster-means-before -->

- **Descendant definition.** A cluster is a bound, virialised dark-matter
  halo with mass > 10¹⁴ h⁻¹M☉ at z = 0, and a protocluster is "simply the
  high redshift progenitor of such a galaxy cluster"; it is not a single
  virialised object but "a large region in space containing all the dark
  matter and baryons that merge into one massive bound virialized
  structure by z = 0" (Chiang, Overzier & Gebhardt 2013, arXiv:1310.2938)
  [src: Sect. II.2]. Their mass is m_tophat, the mass within the radius
  where the overdensity equals the spherical-collapse threshold, on
  average ~25% above m_crit200; "Fornax", "Virgo" and "Coma" types are
  1.37–3 × 10¹⁴, 3–10 × 10¹⁴ and > 10¹⁵ M☉ [src: Sect. II.2].
- **Effective radius.** R_e ≡ √[(1/M) Σ_i m_i (x_i − x_c)²], where M is the mass in bound haloes
  at that redshift, m_i and x_i the mass and position of each halo and x_c
  the centre of mass (arXiv:1310.2938, Eq. 4) [src: Sect. III.2]. At 2 ≲ z
  ≲ 5 about 65% of the bound-halo mass and 40% of the total protocluster
  mass lie inside R_e, independent of cluster mass [src: Sect. III.2].
  Comoving 2R_e is 13.0, 9.0 and 6.4 Mpc at z ~ 2 for Coma, Virgo and
  Fornax types, about 18.8, 13.2 and 9.6 Mpc at z ~ 5 [src: Sect. III.2].
- **Extent of the whole structure.** 90% of the protocluster mass is
  spread across ~35 h⁻¹Mpc comoving at z = 2 (~30 arcmin), and the "main
  halo" holds fewer than 20% of protocluster galaxies with M* > 10⁹
  h⁻¹M☉ at z > 2 (Muldrew, Hatch & Cooke 2015, arXiv:1506.08835) [src:
  Sect. 4]. Only 10% of z = 2 protoclusters are dominated by a single
  halo (no other member above 20% of the main halo mass) and a fifth have
  a second-ranked halo above 0.8 of the first [src: Sect. 4].
- **Operational definition in a survey.** A significant, large
  overdensity "unlikely to occur by chance alone" with enough mass to
  collapse to ≥ 10¹⁴ M☉ by z = 0 (ODIN, Ramakrishnan et al. 2024,
  arXiv:2406.08645) [src: Sect. IV.1].

The consequence for a referee: a "protocluster" detected through its most
massive halo (X-ray, SZ, a massive central galaxy) belongs to the minority
with a dominant halo; such techniques "are likely to miss the majority of
cluster progenitors with no dominant halo" (arXiv:1506.08835) [src: Sect.
4].

### Step 2. Measure the galaxy overdensity
<!-- key: step-2-measure-the-galaxy-overdensity -->

δ_m, δ_h, δ_gal ≡ (n − ⟨n⟩)/⟨n⟩ for matter, haloes and galaxies
(arXiv:1310.2938, Eqs. 1–3), in top-hat windows of a few to several tens of
Mpc [src: Sect. II.3]. Three estimators are in use:

| Estimator | Set-up as published | Analysis | Place read |
|---|---|---|---|
| Counts in a circular aperture | g-dropouts with i < 25.0 counted within 1.8 arcmin (0.75 physical Mpc) radius, apertures on a 1 arcmin grid; apertures with > 50% masked excluded; mean 6.4 and σ = 3.2 galaxies per aperture, close to Poisson | HSC-SSP z ~ 3.8 (arXiv:1708.09421) | Sect. 2.2 |
| Gaussian-smoothed surface density | LAEs, 2D Gaussian kernel of FWHM 10 cMpc chosen by leave-one-out likelihood maximisation (Eq. 1); holes filled with randoms; mean and σ from a Gaussian fit within ±1.5σ after clipping | ODIN z = 3.1 (arXiv:2406.08645) | Sect. III.1 |
| Voronoi Monte Carlo (VMC) in redshift slices | spectroscopic and photometric redshifts, 100 Monte Carlo realisations, overlapping slices of 7.5 pMpc depth in steps δz ~ 0.002, threshold in units of the fitted σ of log(1 + δ_gal) per slice | VUDS z ~ 2.45 (arXiv:1806.06073) | Sect. 3.1 |

Stated reasons:
- *1.8 arcmin aperture*: "expected to be the typical extent of regions
  which will coalesce into a single massive halo of > 10¹⁴ M☉ by z = 0",
  citing Chiang et al. 2013; the cost, stated by the authors, is that
  progenitors of groups are diluted (arXiv:1708.09421) [src: Sect. 2.2].
- *Kernel width by cross-validation*: the kernel is chosen to maximise
  ∏_j p(r_j), p(r_j) = Σ_{i≠j} (2π)^(−1/2) σ⁻¹ exp[−(r_i − r_j)²/2σ²]
  (arXiv:2406.08645, Eq. 1); a fixed kernel favours structures of its own
  size and shape, hence a parallel tessellation map [src: Sect. III.1].
- *7.5 pMpc slices*: a compromise between line-of-sight elongation of
  peaks and noise in the density reconstruction; 5 pMpc slices were tried
  (arXiv:1806.06073) [src: Sect. 3.1]. The mean density is obtained from a
  3σ-clipped Gaussian fit to log Σ, with ⟨Σ⟩ = 10^μ e^(2.652σ²), because Σ
  is log-normal [src: Sect. 3.1].

### Step 3. Select candidates and measure contamination
<!-- key: step-3-select-candidates-and-measure -->

- **Peak threshold.** HSC candidates are regions whose peak overdensity
  significance exceeds 4σ; 216 such regions, of which 37 lie within 8
  arcmin of a more overdense one and are treated as its substructures,
  giving 179 unique candidates (arXiv:1708.09421) [src: Sect. 2.2]. The
  number of 4σ regions is ~30 times the Poisson expectation, and a
  light-cone model reproduces the observed significance distribution
  except above 6σ [src: Sect. 2.2].
- **Source extraction on the map.** ODIN pixelates the maps at 3.6 arcsec
  (115 ckpc) and runs SEP (SExtractor) with DETECT_THRESH = 3σ and
  DETECT_MINAREA = 4600 pixels (≃ 60 cMpc²) on the Gaussian-smoothed map
  (arXiv:2406.08645) [src: Sect. IV.1]. The Voronoi map is smoothed with a
  5 cMpc FWHM kernel before detection and thresholded at 4.5σ [src: Sect.
  IV.1, V.2].
- **Point-cloud clustering.** HDBSCAN, "a minimum cluster size of 15 LAEs
  and the 10th nearest neighbor distance", median surface density > 0.23
  arcmin⁻² [src: Sect. IV.2 of arXiv:2406.08645].
- **Contamination from random maps.** ODIN draws random subsets of all
  continuum and line emitters in the narrowband image, matched in number
  and narrowband magnitude to the LAEs, builds the same maps, and takes
  the ratio of detections in random and real maps as the contamination
  fraction (30 iterations) [src: Sect. IV.1]. Result: < 0.1% for the
  Gaussian-smoothed set-up, ≈ 20% for the Voronoi and HDBSCAN samples
  [src: Sect. IV.1, IV.2].
- **Volume of a 3D structure.** Hyperion is the set of contiguous voxels
  above 2σ_δ, grown iteratively from a seed region in one slice; the 2σ_δ
  level corresponds to δ ~ 0.65 (3, 4, 5σ_δ to δ ~ 1.1, 1.7, 2.55) and was
  retained because the bridge between the two main components is evident
  at that level (arXiv:1806.06073) [src: Sect. 3.1, 3.2].

### Step 4. Turn an overdensity into a protocluster probability
<!-- key: step-4-turn-an-overdensity-into-a-protocluster -->

- **Overdensity thresholds for a given purity.** Chiang et al. tabulate
  the δ_m, δ_h and δ_gal at which 50% and 80% of regions are protoclusters,
  per redshift, window and tracer (arXiv:1310.2938) [src: Tables 2–4].
  Example for SFR > 1 M☉ yr⁻¹ galaxies in (15 Mpc)³ windows at z = 3:
  δ_gal = 2.08 (50%) and 3.14 (80%); in (25 Mpc)³ windows, 0.64 and 1.10
  [src: Table 4]. Higher-bias tracers need higher δ_gal [src: Sect.
  III.7].
- **Classification of random apertures.** Lovell, Thomas & Wilkins (2018,
  arXiv:1710.02148) draw 100,000 random cylinders of radius R and depth D,
  label each Proto, PartProto, ProtoField or Field from the completeness C
  and purity P of its galaxies with respect to each descendant cluster,
  with C_lim and P_lim set to the 5th percentile of the protocluster
  population for that aperture and selection, and read off the fraction of
  each class as a function of measured δ [src: Sect. 3.4.1]. Their stated
  difference from the earlier calibration: Chiang et al. count a region as
  a protocluster when its centre lies within half a box length of a
  protocluster centre, an assumption of spherical symmetry that "may
  identify regions with significant field galaxy populations"; the
  aperture-shape-aware procedure gives lower protocluster probabilities
  [src: Sect. 3.4.1; abstract].
- **Purity versus completeness of a threshold sample.** At > 4σ, 76% of
  HSC candidates are expected to become > 10¹⁴ M☉ clusters, but only ~6%
  of the progenitors of such clusters sit on > 4σ regions at z ~ 4,
  because projection over the dropout redshift range lowers their
  overdensity (arXiv:1708.09421) [src: Sect. 2.2]. The sample is clean and
  biased to the richest structures, average descendant ~5 × 10¹⁴ M☉ [src:
  Sect. 2.2].

### Step 5. Estimate the descendant (z = 0) mass
<!-- key: step-5-estimate-the-descendant-z-0-mass -->

Five routes, in order of how much they assume:

1. **Volume × overdensity (the Steidel formula).** M_{z=0} = (1 + δ_m) ⟨ρ⟩
   V, with δ_m = δ_gal/b (arXiv:1310.2938, Eq. 5; arXiv:1806.06073, Eq. 1;
   arXiv:2406.08645, Eqs. 4–5). In 2D, ODIN approximates the volume by
   V_PC = A_PC^1.5 (a cube built on the area) with b_g = 1.8 (Eq. 6) [src:
   Sect. V.2 of arXiv:2406.08645]. Hyperion: V ≈ 9.5 × 10⁴ cMpc³,
   ⟨δ_gal⟩ ~ 1.24, b = 2.55, M_tot ~ 4.8 × 10¹⁵ M☉ [src: Sect. 3.2 of
   arXiv:1806.06073].
2. **Effective-volume correction.** Because only ~40% of the total mass
   lies in the cube of side 2R_e, Chiang et al. propose M_est ≡ C_e (1 +
   δ_m,e) ⟨ρ⟩ V_e, with V_e ≡ (2R_e)³ and C_e ~ 2.5 (arXiv:1310.2938, Eq.
   6); errors "in general less than a factor of 2" with no significant
   bias across mass and redshift [src: Sect. III.8].
3. **Empirical δ–mass relation.** Median descendant mass against δ in a
   fixed window, intrinsic scatter ~0.2 dex (arXiv:1310.2938) [src: Sect.
   III.8]; or the fit M_200/(10¹⁴ M☉) = a (1 + z)^b (1 + δ)^c + C in a
   cylinder of radius and depth R_C = 10 cMpc, with (a, b, c, C) = (0.146,
   −1.077, 2.628, 1.752) for SSFR1 galaxies (arXiv:1710.02148, Eq. 15)
   [src: Table 2]; none below δ_gal < 4.5 [src: Sect. 3.4.2].
4. **Main-halo extrapolation.** Extrapolating the most massive halo at z
   = 2 to z = 0 has 0.54 dex RMS error for dominated protoclusters if the
   evolutionary state is ignored, 0.15 dex if the mass ratio M₂/M₁ of the
   two most massive haloes is used (M₂/M₁ < 0.15) (arXiv:1506.08835) [src:
   Sect. 3.2.2].
5. **Abundance matching of the candidate density.** HSC candidates have n
   = 4.6 × 10⁻⁷ h³Mpc⁻³, matching haloes of ~0.8–1.1 × 10¹³ h⁻¹M☉ at z ~
   3.8; descendants ~6.3 × 10¹⁴ h⁻¹M☉, or ~7.6 × 10¹⁴ h⁻¹M☉ if
   candidates within 20 arcmin merge (number density down by 37%)
   (arXiv:1708.09421) [src: Sect. 4.1].

**Calibrate the formula on mocks processed like the data.** ODIN runs its
selection on 90 TNG300 slices at z = 3: Eq. 6 underestimates the true
M_200,z=0 about 80% of the time, with M_est ≈ 0.35 M_200 for the Voronoi
selection; the correction factors are ~3 (Voronoi), ~2 (Gaussian
smoothing) and ~1.15 (HDBSCAN) (arXiv:2406.08645) [src: Sect. V.2, Fig. 8
caption, Sect. VI.2]. Corrected median masses: log(M_z=0/M☉) = 14.35,
14.75 and 14.52 for the Voronoi, HDBSCAN and Gaussian samples [src:
Sect. VI.2]. Lack of radial information alone introduces ~0.4 dex [src:
abstract].

### Step 6. Delimit a supercluster
<!-- key: step-6-delimit-a-supercluster -->

Three definitions are in use (M. Einasto 2025 review, arXiv:2505.22082)
[src: Sect. 2]:

1. **Percolation or density level before percolation.** Friends-of-friends
   on groups or clusters with a linking length below percolation; for
   Abell clusters 24 h⁻¹Mpc, close to their Poisson radius R_P = 26
   h⁻¹Mpc, giving largest superclusters of ~100–150 h⁻¹Mpc [src: Sect. 2].
   On a luminosity-density field: smoothing with a B₃ spline of 8 h⁻¹Mpc
   (the field called D8), then a level D in units of the mean, D = 5 for
   SDSS MAIN; fixed or adaptive per-supercluster levels (Liivamägi et al.
   2012, as described in the review) [src: Sect. 2]. "Typically,
   superclusters determined using these criteria are not gravitationally
   bound" [src: Sect. 2].
2. **Future collapse ("superstes-clusters").** Only regions that will
   collapse despite the accelerated expansion (Chon, Böhringer & Zaroubi
   2015, arXiv:1502.04584) [src: abstract]. The overdense region is a
   homogeneous sphere evolved from z = 500 with the Friedmann equation,
   its Ω_m raised iteratively until it collapses in the future [src: Sect.
   2]. Criterion: density ratio R = ρ_ov/ρ_m today, or the equivalent
   infall velocity; the two radii agree in 570 simulated cases bar five
   [src: Sect. 2, 2.1].
3. **Basins of attraction.** Volumes where peculiar velocities converge on
   an attractor (Laniakea and successors); see `cosmo-peculiar-velocities`
   for the velocity data [src: Sect. 2 of arXiv:2505.22082].

The critical values depend on Ω_m (arXiv:1502.04584, Table 1) [src:
Appendix A]:

| Ω_m | R for future collapse | R at turnaround | Δ_c (future collapse) |
|---|---|---|---|
| 0.24 | 9.811 | 14.31 | 1.36 |
| 0.27 | 8.732 | 13.12 | 1.36 |
| 0.30 | 7.858 | 12.15 | 1.36 |
| 0.318 (Planck-based best fit as tabulated, h = 0.670) | 7.409 | 11.66 | 1.36 |
| 1.0 (EdS) | — | 5.54 | — |

Δ_c = (ρ_ov − ρ_c)/ρ_c is the overdensity relative to the critical
density; R varies with background Ω_m while Δ_c "hardly changes" [src:
Sect. 2]. The review quotes Δρ_turn = 13.1 and Δρ_FC = 8.73 for ΛCDM
[src: Sect. 8 of arXiv:2505.22082]; these are the Ω_m = 0.27 row of the
table above [der: comparison of the two tables], so with a Planck-like
Ω_m ≈ 0.32 the future-collapse threshold is ~7.4. The review also lists
Δρ_ZG = 5.41 (zero gravity) and Δρ = 1 (Einstein–Straus radius, roughly
the cocoon boundary) [src: Sect. 8].

### Step 7. Estimate supercluster mass, shape and dynamical state
<!-- key: step-7-estimate-supercluster-mass-shape-and -->

- **Mass by summing members.** M_scl = Σ M_gr,cl + Σ M_single + M_gas +
  M_DM(additional) (arXiv:2505.22082, Eq. 6) [src: Sect. 4]. Group M_500
  converted to M_200 = (200/500)(R_200/R_500)³ M_500 with R_500 ≈ 0.65
  R_200 for NFW concentrations 4–8, then M_bound ~ 2.2 M_200 (one
  catalogue); or M_200 ≈ 1.46 M_500 and a simulation ratio M_cl = 0.39
  M_scl (an eROSITA catalogue) [src: Sect. 4]. Budget in one study: rich
  groups and clusters ~75%, poor groups ~10%, single galaxies ~5%, rest
  gas; ~10% of supercluster mass in intercluster gas. From light: M/L ≈
  400 for poor superclusters, 250–300 for rich ones [src: Sect. 4].
- **Mass from the density field.** Lietzen et al. (2016, arXiv:1602.08498)
  sum M = ρ_c D V over grid cells, D the luminosity density in mean units
  and V = 27 h⁻³Mpc³ per 3 h⁻¹Mpc cell, giving 2.4 × 10¹⁷ h⁻¹M☉ for the
  BOSS Great Wall; a stellar-mass route with a Moster et al. stellar-to-halo
  relation and an SDSS-main incompleteness ratio of 0.082 gives 1.6 × 10¹⁷
  h⁻¹M☉ [src: Sect. 4.1]. The threshold D = 5–7 was chosen because the
  CMASS supercluster-volume distribution at those levels is close to that
  of the SDSS main-sample superclusters at D = 5 [src: Sect. 3].
- **Mass inside a sphere.** M(R) = 1.45 × 10¹⁴ Ω_m0 Δρ (R/5 h⁻¹Mpc)³ (1 +
  z)³ h⁻¹M☉ (arXiv:2505.22082, Eq. 7) [src: Sect. 8].
- **Shape.** Minkowski functionals V₀ = V, V₁ = S/6, V₂ = C/3π with C the
  integrated mean curvature, V₃ = χ/2 with χ the Euler characteristic
  (Eqs. 1–3), shapefinders H₁ = 3V/S (thickness), H₂ = S/C (breadth), H₃ =
  C/4π (length), planarity K₁ = (H₂ − H₁)/(H₂ + H₁) and filamentarity K₂ =
  (H₃ − H₂)/(H₃ + H₂) [src: Sect. 3 of arXiv:2505.22082]. The review
  writes "Prolate ellipsoids (pancakes)" for H₁ ≪ H₂ ≈ H₃ and "oblate
  ellipsoids (filaments)" for H₁ ≈ H₂ ≪ H₃ [src: Sect. 3]; by the usual
  geometric meaning the labels are swapped (pancakes are oblate,
  filaments prolate) [der: definition of oblate and prolate], so quote
  the H inequalities, not the adjectives. Rich superclusters with K₁/K₂ <
  0.5 are the more elongated [src: Sect. 3].
- **Dynamical state.** Mass profile around the most massive cluster of
  each high-density core, compared with Δρ_turn, Δρ_FC and the collapse
  values, then evolved with the spherical model [src: Sect. 8 of
  arXiv:2505.22082]. For protocluster peaks, δ_NL from δ_gal/b is mapped
  to the linear δ_L and grown with D₊(z) (arXiv:1806.06073, Eq. 7) to the
  turnaround (δ_L ≃ 1.062) and collapse (δ_c ≃ 1.686) epochs [src: Sect.
  5.1]. An application to Coma and Leo clusters finds regions of
  influence of R_inf ≈ 4 Mpc with Δρ_inf ≈ 50–60 at the border, collapse
  starting at z ≈ 0.4–0.5 (Einasto et al. 2025, arXiv:2510.19803) [src:
  abstract].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Aperture size
<!-- key: aperture-size -->

Small apertures maximise contrast for the cores, large ones capture the
structure. Lovell et al. find the Bhattacharyya distance between
protocluster and field δ distributions maximal at R = 6 cMpc for almost
all selections and redshifts, but recommend ~10 cMpc as the compromise
between completeness, purity and descendant-mass accuracy
(arXiv:1710.02148) [src: Fig. 7 caption; abstract]. Even the largest
protoclusters keep > 50% of their tracers within R = 10 cMpc, and the
completeness and purity curves cross above 80% [src: Sect. 3.3.1]. With
narrowband or photometric depth, δ_gal is a surface density: for a
narrowband filter of FWHM ~60 Å at z = 3 (Δz ~ 0.05, d_c ~ 50 Mpc) the
protocluster 1 + δ_gal drops by ~40% relative to a 15 Mpc cube, and for Δz
≳ 0.1 only the most overdense systems stand out from random fields
(arXiv:1310.2938) [src: Sect. III.9].

### Map estimator
<!-- key: map-estimator -->

On the same ODIN data, the Gaussian, Voronoi and HDBSCAN routes give 9, 33
and 47 structures (arXiv:2406.08645) [src: Sect. VI.1]. All 9 Gaussian
structures appear in the other two; Voronoi areas are ~1.1–1.8 times and
HDBSCAN areas ~2–5 times the Gaussian ones [src: Sect. VI.1]. HDBSCAN
recovers elongated, lower-density features, but its parameters are harder
to give a physical meaning than an area and a threshold [src: Sect.
VI.1]. Lowering the Voronoi threshold from 4.5σ to 3.5σ raises the
recovery of the 30 most massive TNG300 progenitors from 60% to 80% at
the cost of ~45% contamination instead of ≈ 20% [src: Sect. V.2].

### Tracer completeness
<!-- key: tracer-completeness -->

In TNG-Cluster (352 protoclusters, M_200,z=0 ~ 10^14.3–15.5 M☉), M*-limited
(> 10^9.5 M☉) or SFR-limited (> 10 M☉ yr⁻¹) samples recover the
highest density peak of the M* > 10^8.5 M☉ baseline within 1.0 pMpc in
~60% of cases at z > 2, and ~40–50% above 10^10 M☉ (Baxter et al. 2025,
arXiv:2504.03836) [src: abstract]. Emission-line selection loses low-mass
galaxies quenched in the core, so the line-emitter overdensity "should be
considered unreliable, especially in small apertures, and should not be
used to estimate the z = 0 mass" (arXiv:1506.08835) [src: Sect. 4].

### Halo mass in the virial radius or on Lagrangian scales
<!-- key: halo-mass-in-the-virial-radius-or-on-lagrangian -->

For z > 5 candidates, halo masses obtained by applying a stellar-to-halo
relation to all stellar mass in a large aperture are not comparable with
simulated M_200c; recomputing M_200c iteratively within the virial radius
(20–50 pkpc) lowers literature masses by ~0.5 dex on average, up to ~1.5
dex (Witten et al. 2026, arXiv:2605.28930) [src: Sect. 4.1]. Merging
candidates within a Lagrangian radius R_L ~ 10–15 cMpc brings the
protocluster number density to almost exactly the Tinker et al. halo mass
function value [src: Sect. 4.3]. A 0.2 dex halo-mass error raises the
apparent proto-Coma density by 0.65 dex at z = 6 through Eddington bias
[src: Sect. 4.4, Fig. 3 caption]. The probability that the re-measured
candidates are protoclusters ranges from 6% to 90% [src: Sect. 5.1]. The
authors keep M_200c for comparison with simulations but suggest mass on
Lagrangian scales for selection [src: Sect. 5.1].

### Supercluster definition
<!-- key: supercluster-definition -->

Masses differ with the definition: the most massive superclusters are ~1
× 10¹⁵ h⁻¹M☉ in a future-collapse catalogue and ~2.5 × 10¹⁶ M☉ in a
before-percolation catalogue (arXiv:2505.22082) [src: Sect. 4]. High-
density cores of percolation-defined superclusters have 0.5–5 × 10¹⁵ M☉,
the same order as future-collapse superclusters [src: Sect. 6]. Under the
future-collapse criterion Laniakea (80 h⁻¹Mpc, 10¹⁷ h⁻¹M☉) has a density
ratio of about 0.94 and "will disperse", and would need ~5700 km s⁻¹
infall at its boundary against observed 500–700 km s⁻¹
(arXiv:1502.04584) [src: Sect. 3.2]. A velocity basin and a bound
supercluster are therefore different objects; say which one is meant.

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Cluster threshold for "protocluster" | M > 10¹⁴ h⁻¹M☉ at z = 0 (m_tophat) | Millennium + SAM | arXiv:1310.2938 | Sect. II.2 |
| δ_gal for 80% purity, SFR > 1 M☉/yr, z = 3 | 3.14 in (15 Mpc)³, 1.10 in (25 Mpc)³ | same | arXiv:1310.2938 | Table 4 |
| Characteristic aperture | R ~ 10 cMpc (D_B max at 6 cMpc) | L-Galaxies | arXiv:1710.02148 | abstract, Fig. 7 |
| HSC aperture and threshold | 1.8′ (0.75 pMpc), > 4σ peak | HSC-SSP z ~ 3.8 | arXiv:1708.09421 | Sect. 2.2 |
| HSC purity and completeness | 76% and ~6% | light-cone model | arXiv:1708.09421 | Sect. 2.2 |
| ODIN kernel and detection | FWHM 10 cMpc; 3σ, ≃ 60 cMpc² | ODIN z = 3.1 | arXiv:2406.08645 | Sect. III.1, IV.1 |
| ODIN mass correction | ×3 (Voronoi), ×2 (Gaussian), ×1.15 (HDBSCAN) | TNG300 mocks | arXiv:2406.08645 | Sect. VI.2 |
| VUDS slice depth, threshold | 7.5 pMpc; 2σ_δ (δ ~ 0.65) | VUDS + zCOSMOS | arXiv:1806.06073 | Sect. 3.1 |
| Hyperion mass error | +18%/−25% (threshold ±0.2σ_δ: ±15%) | same | arXiv:1806.06073 | Sect. 3.2 |
| Volume filling at D_t ≈ 5 | ~1% | ΛCDM, SDSS | arXiv:2505.22082 | Sect. 2 |
| Future-collapse density ratio | 7.409 (Ω_m = 0.318); 8.732 (Ω_m = 0.27) | spherical model | arXiv:1502.04584 | Table 1 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Projection inflates or erases candidates.** With broad redshift
  windows, chance alignments of small structures look overdense and true
  protoclusters are diluted by foreground and background voids
  (arXiv:1708.09421) [src: Sect. 2.2]. Test: the number of > nσ regions
  against Poisson and against a light-cone mock with the same selection
  [src: Sect. 2.2]; random-source maps for the contamination rate
  (arXiv:2406.08645) [src: Sect. IV.1].
- **Line-of-sight elongation.** Photometric-redshift errors (Δz ~ 0.1 for
  σ_zp = 0.03(1 + z)), slice depth (Δz ~ 0.02) and fingers of God (Δz ~
  0.006 for 500 km s⁻¹) elongate a 3D structure and lower its δ_gal but
  leave the galaxy count, hence the Eq. 1 mass, unchanged; a Kaiser
  volume correction acts the other way (arXiv:1806.06073) [src: Sect. 3.2,
  footnote 5]. Check which dominates in mocks before correcting.
- **Wrong bias.** δ_m = δ_gal/b assumes a field bias; if the protocluster
  stellar mass function differs from the field, the bias "depends on
  environment" (arXiv:1506.08835) [src: Sect. 4]. Test: field-size
  dependence of δ_gal; apertures > 10 cMpc are less affected [src: Sect. 4].
- **The cube approximation.** V_PC = A^1.5 biases masses low for most
  structures (80% of TNG300 cases) (arXiv:2406.08645) [src: Sect. V.2].
  Test: run the identical finder on simulation slices and derive the
  correction.
- **Spherical-collapse thresholds taken from another cosmology.**
  The future-collapse ratio falls from 9.811 to 7.134 between Ω_m = 0.24
  and 0.33 (arXiv:1502.04584) [src: Table 1]; check that the
  quoted threshold matches the Ω_m used for distances.
- **Mass-density convention.** The BOSS Great Wall cell mass is written M
  = ρ_c D V with ρ_c the critical density (arXiv:1602.08498) [src: Sect.
  4.1], whereas the protocluster formula uses the mean matter density ρ_m
  = Ω_m ρ_c (arXiv:1806.06073, Eq. 1) [src: Sect. 3.2]; for the same D
  the two differ by 1/Ω_m [der: ρ_m = Ω_m ρ_c]. Compare supercluster and
  protocluster masses only after checking which density multiplies V.
- **Merged or main-halo-selected candidates.** Neighbours within 8 arcmin
  (HSC) or within R_L (z > 5) can be one structure (arXiv:1708.09421,
  Sect. 4.1; arXiv:2605.28930, Sect. 4.3) [src]; main-halo selections are
  not comparable with all-progenitor predictions (Step 1).

## Reading list
<!-- key: reading-list -->

- Foundation: Chiang et al. 2013, arXiv:1310.2938 — R_e, purity thresholds, C_e mass formula (Sect. II–III).
- Critique: Muldrew et al. 2015, arXiv:1506.08835 — extent, main-halo minority, M₂/M₁, line-emitter bias.
- Method: Lovell et al. 2018, arXiv:1710.02148 — aperture choice, Proto probability, δ–mass fit.
- Application: Toshikawa et al. 2018, arXiv:1708.09421 — aperture counts, purity against completeness.
- Application: Ramakrishnan et al. 2024, arXiv:2406.08645 — three estimators, random maps, TNG calibration.
- Application: Cucciati et al. 2018, arXiv:1806.06073 — VMC density, 2σ_δ volume, mass error budget.
- Critique: Witten et al. 2026, arXiv:2605.28930 — virial-aperture masses, mergers, Eddington bias.
- Systematics: Baxter et al. 2025, arXiv:2504.03836 — completeness limits and core identification.
- Review: M. Einasto 2025, arXiv:2505.22082 — supercluster definitions, shapefinders, masses, collapse.
- Method: Chon et al. 2015, arXiv:1502.04584 — future-collapse criterion and its Ω_m dependence.
- Application: Lietzen et al. 2016, arXiv:1602.08498 — density level at z ≈ 0.5, two mass routes.

## Not verified
<!-- key: not-verified -->

- The Steidel et al. 1998 paper behind the volume × overdensity formula
  and its redshift-space correction was not read; it enters only as cited
  by arXiv:1310.2938 and arXiv:2406.08645.
- Liivamägi et al. 2012 (the adaptive-level SDSS supercluster catalogue)
  and the Sankhyayan et al. 2023 and Chen et al. 2024 catalogues were not
  read; their settings come from the review arXiv:2505.22082.
- The body of arXiv:2504.03836 and of arXiv:2510.19803 was not read; only
  their abstracts.
- The Table 1 classification thresholds (C_lim, P_lim conditions) of
  arXiv:1710.02148 were not read.
