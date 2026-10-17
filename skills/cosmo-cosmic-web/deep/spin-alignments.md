# Spin–filament alignments — cosmo-cosmic-web dossier

Scope: how a spin–filament alignment is measured in data and in simulations
(skeleton, spin axis, galaxy–segment assignment, statistic, null
distribution, transition mass), what each choice costs, the amplitudes
actually measured per mass bin, and the tests that separate a signal from
line-of-sight and selection artefacts.
Snapshot: 2026-10-17.
From: Libeskind et al. 2018, Sect. 1.3; SAMI, MaNGA and SDSS alignment papers.

Already in L2, not repeated here: the theory of the flip (conditional tidal
torques, winding flows) in `physics-and-methods.md#spin-and-shape-alignments-with-the-web`;
the list of detections and their history in
`results.md#spin-and-shape-alignments`; the stellar-versus-Hα and
filament-diameter dependences as systematics in
`systematics.md#alignment-measurement-systematics`; the debate in
`open-questions.md#the-spin-alignment-transition`. Intrinsic alignments of
shapes as a weak-lensing systematic are in `cosmo-weak-lensing`.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Build the skeleton the spins are compared with
<!-- key: step-1-build-the-skeleton-the-spins-are -->

The observational analyses use three skeleton families:

| Analysis | Finder and input | Settings and stated reason | Place read |
|---|---|---|---|
| SAMI (Welker et al. 2020, arXiv:1909.12371) | DisPerSE on a mass-weighted Delaunay density of all GAMA DR3 galaxies, in redshift space | no prior smoothing, "which might impact the directions of filaments"; 3σ persistence baseline, 2σ network as a test of fainter, smaller-scale filaments | Sect. 3.1.1 |
| SAMI bulges (Barsanti et al. 2022, arXiv:2208.10767) | DisPerSE on 35,882 GAMA galaxies (DTFE density) | 3σ, "in accord with previous studies" | Sect. 3.2 |
| MaNGA 3D (Kraljic et al. 2021, arXiv:2104.08275) | DisPerSE on the SDSS galaxy catalogue of Tempel et al. 2014 | 3σ | Sect. 2.5 |
| MaNGA 2D (Krolewski et al. 2019, arXiv:1902.09797) | Cosmic Web Reconstruction density ridges in (α, δ) slices of δz = 0.005 (c δz = 1500 km s⁻¹, ~20 Mpc), Gaussian kernel of 5–10 Mpc growing with redshift | 2D to remove spurious line-of-sight filaments from redshift-space distortions and to follow the redshift-dependent galaxy density; the 10% least dense galaxies (30th-neighbour distance) removed to suppress noisy filaments | Sect. II.1 |
| SDSS, Siena Galaxy Atlas, edge-on discs (arXiv:1308.2816, arXiv:2509.02062, arXiv:2507.07334) | Bisous spines of Tempel et al. 2014 | groups first spherised with a friends-of-friends algorithm to suppress fingers of God | arXiv:1308.2816, Sect. II |

In the MaNGA 2D analysis the local filament direction is the first principal
component of the covariance of the ten nearest filament points, and its
uncertainty comes from 100 bootstrap resamples of the filament catalogue;
the filament-direction error dominates the position-angle error [src:
arXiv:1902.09797, Sects. II.1, II.3].

Simulations use either the skeleton of a smoothed density, Gaussian R = 5
h⁻¹Mpc with σ(R) = 0.66, "mildly non-linear large-scale structures at
cluster scales" (Horizon 4π; Codis et al. 2012, arXiv:1201.5794, Sect. 2.2),
or NEXUS+ and NEXUS velocity-shear filaments (P-Millennium; Ganeshaiah Veena
et al. 2018, arXiv:1805.00033, Sect. 2.2). At higher redshift Codis et al.
choose R(z) from σ²(R(z), z) = σ²(R₀, 0) to keep the same level of
non-linearity [src: Sect. 2.3].

### Step 2. Measure the spin axis
<!-- key: step-2-measure-the-spin-axis -->

- **Kinematic position angle (PA) from IFS.** SAMI and MaNGA fit the global
  PA of the stellar velocity map with FIT_KINEMATIC_PA (Krajnović et al.
  2006); the plane-of-sky spin is perpendicular to it [src:
  arXiv:1902.09797, Sect. II.3; arXiv:1909.12371, Sect. 2.1.1]. SAMI uses
  spaxels with S/N > 3 and V_err < 30 km s⁻¹, takes the 1σ PA error from
  the χ² contours, and redraws each PA from a Gaussian of that width when
  computing significance contours [src: arXiv:1909.12371, Sect. 2.1.1].
- **3D spin by the thin-disc approximation** (Lee & Erdogdu 2007, as
  written in arXiv:2104.08275, Eqs. 1–3): L̂_r = cos i,
  L̂_θ = (1 − cos² i)^{1/2} sin PA, L̂_φ = (1 − cos² i)^{1/2} cos PA, with
  the inclination from cos² i = ((b/a)² − p²)/(1 − p²) (Eq. 2), b/a the
  axis ratio and p the intrinsic flatness, then rotated to equatorial
  Cartesian components with α = π/2 − Dec, β = RA (Eq. 3). Values of p:
  morphology-dependent from 0.23 (S0) to 0.1 (Scd–Sdm); Kraljic et al. adopt
  the mean 0.158, Barsanti et al. the SAMI mean 0.171; i = π/2 when b/a < p
  [src: arXiv:2104.08275, Sect. 2.6; arXiv:2208.10767, Sect. 3.1].
- **Sign ambiguity.** Which side of the disc is nearer is unknown. Kraljic
  et al. and Barsanti et al. keep the positive sign of L̂_r, which "is
  expected to decrease the strength of the alignment signal", and check
  that assigning both signs (Lee 2011; Eq. 4 of arXiv:2104.08275) changes
  no conclusion [src: arXiv:2104.08275, Sect. 2.6 and App. A]. Tempel &
  Libeskind and the Siena Galaxy Atlas analysis use both spin vectors for
  every galaxy; the doubling "dilutes the signal and boosts the
  significance", the two effects cancelling [src: arXiv:1308.2816,
  Sect. III.3; arXiv:2509.02062, Sect. 3.1].
- **Shape as a spin proxy.** Without kinematics the short axis of the light
  distribution stands for the spin; ellipticals are assigned i = 90°, so
  the projected short axis is taken as the spin [src: arXiv:2509.02062,
  Sect. 3.1]. Barsanti et al. extend the thin-disc model to bulge-dominated
  galaxies on the grounds that their short and spin axes are aligned and
  their velocity maps regular [src: arXiv:2208.10767, Sect. 3.1].
- **Edge-on discs.** Galaxies inclined by more than 85° fix the spin axis
  in 3D without an inclination model; the price is the sample, about 1% of
  discs, 2861 galaxies against 15,421 Bisous filaments [src:
  arXiv:2507.07334, Sects. 2 and 5].
- **Haloes.** J = m_p Σ_i (r_i − r̄) × (v_i − v̄) over FOF particles
  (arXiv:1201.5794, Sect. 2.2), or e_J = J/|J| within radii holding 10%, 50%
  and 100% of the halo mass (arXiv:1805.00033, Eq. 12), with at least 300
  particles inside R₂₀₀ following Bett et al. 2007, hence M₂₀₀ > 3.2 × 10¹⁰
  h⁻¹M☉ in P-Millennium [src: arXiv:1805.00033, Sect. 3].

### Step 3. Assign each galaxy to a filament segment
<!-- key: step-3-assign-each-galaxy-to-a-filament-segment -->

SAMI assigns each galaxy to the nearest segment by 3D Euclidean distance
and measures the angle with the segment projected on the sky [src:
arXiv:1909.12371, Sect. 4.1]. Kraljic et al. assign each galaxy its two
closest segments "to increase the statistics", and keep galaxies within
13 Mpc of a filament and at least 0.5 Mpc from a node, a compromise between
a clean and a large sample; including distant or node galaxies weakens the
signal [src: arXiv:2104.08275, Sect. 3]. Tempel & Libeskind keep only
galaxies within 0.5 h⁻¹Mpc of the axis, brighter than M_r = −20.5 (fainter
spins uncertain), and 3 h⁻¹Mpc from the survey border [src:
arXiv:1308.2816, Sect. II]. Codis et al. take the five haloes closest to
each segment, regardless of mass [src: arXiv:1201.5794, Sect. 2.2].

**Fingers of God.** In GAMA, 10% of segments have |cos α_los| > 0.95,
against 5% expected for isotropy (α_los the angle between segment and line
of sight) [src: arXiv:1909.12371, Sect. 3.1.1]. SAMI rejects group
compression because GAMA at 0.01 < z < 0.1 has few rich (~10-member)
groups, because individual groups are genuinely stretched along their
filament, and because compression does not remove boundary-induced
line-of-sight filaments; it compares three treatments instead: Method 0, no
correction; Method 1, reassign a galaxy on a segment with |cos α_los| > 0.9
to the next contiguous segment below 0.9 (baseline); Method 2, drop galaxies
on segments above 0.95. Results are "qualitatively independent of the
method"; Method 2 raises the signal and the noise more [src: same].
Barsanti et al. applied the compression and found aligned segments falling
only from ~22% to ~14% [src: arXiv:2208.10767, Sect. 3.2].

### Step 4. Form the statistic
<!-- key: step-4-form-the-statistic -->

The halo-filament alignment parameter is μ_hf = |h · e₃|/(|h||e₃|)
(arXiv:1805.00033, Eq. 13), h the halo vector (spin, shape axis or
velocity), e₃ the filament direction; the absolute value because a filament
has an orientation, not a direction. Isotropy gives μ uniform on [0, 1];
the sample is "preferentially parallel" if the median μ > 0.5 [src:
Sect. 4.1]. In projection the reference values change: a mean
2D dot product of 2/π = 0.6366 for random alignment (arXiv:1902.09797,
Sect. III), or a mean projected angle of 45° (arXiv:1909.12371, Sect. 4.2).
The PDF is written 1 + ξ, ξ the excess probability over uniform
(arXiv:1201.5794, Sect. 2.2); SAMI plots 1 + κξ with κ = 90 to normalise
the uniform distribution of angles to one [src: arXiv:1909.12371,
Sect. 4.1].

### Step 5. Build the null distribution
<!-- key: step-5-build-the-null-distribution -->

The uniform distribution is not the null: neither spin inclinations nor
filament orientations are isotropic with respect to the line of sight
[src: arXiv:1308.2816, Sect. III.3; arXiv:2509.02062, Sect. 3.1]. The
randomisations in use:

| Randomisation | Kept fixed | Realisations | Analysis |
|---|---|---|---|
| move galaxies among filament points | spin orientations | 10,000 | arXiv:1308.2816, Sect. III.3 |
| shuffle galaxy–filament association | spins | 2000 (MaNGA 3D); 3000 (SAMI bulges) | arXiv:2104.08275, Sect. 3; arXiv:2208.10767, Sect. 4.2 |
| reassign galaxies to random segments; flip PAs by ±45° | filaments | 100,000 each | arXiv:1909.12371, Sect. 4.2 |
| shuffle galaxy and filament catalogues | — | 50,000 | arXiv:1902.09797, Sect. III |
| randomise each PA on the sky | positions, filaments | 10,000 | arXiv:2509.02062, Sect. 3.2 |
| 1000 random PAs per filament, spline fit of the null PDF | filaments | 2.86 × 10⁶ test galaxies | arXiv:2507.07334, Sect. 4 |

Uncertainties: bootstrap of galaxies (100 in arXiv:2104.08275; 1000 in
arXiv:2208.10767 and arXiv:1805.00033; 50,000 in arXiv:1902.09797), plus
PA errors, which SAMI finds "very sub-dominant" next to the small sample
[src: arXiv:1909.12371, Sect. 4.2]. MaNGA estimates the covariance between
mass bins by resampling 100 deg² blocks, to keep the correlation between
neighbouring spins, which drops over ~10 h⁻¹Mpc [src: arXiv:1902.09797,
Sect. IV]. Tests: one- and two-sample Kolmogorov–Smirnov against the
randomised median (p < 0.05 adopted) [src: arXiv:2208.10767, Sect. 4.2];
a linear slope of the null-corrected PDF in cos Θ [src: arXiv:2507.07334,
Sect. 4].

### Step 6. Extract a transition
<!-- key: step-6-extract-a-transition -->

- **Simulations.** M_crit is the mass at which ⟨cos θ⟩ = 0.5 [src:
  arXiv:1201.5794, Sect. 2.2], or at which the median μ crosses 0.5 [src:
  arXiv:1805.00033, Sects. 4.1, 4.3].
- **Data, threshold scan.** SAMI splits the sample at M_thresh and plots
  ⟨θ_low⟩ against ⟨θ_high⟩; M_thresh = 10^10.8 M☉ is chosen because it
  maximises the signal-to-noise while keeping both signals above their
  marginal 1σ thresholds; scanning 10^9.5–10^11.2 locates the joint
  detection above 10^10.4 M☉ and a transition in the 10^10.25–10^10.75 M☉
  range [src: arXiv:1909.12371, Sect. 4.2].
- **Data, which property drives it.** Spearman tests per galaxy, then
  residuals Δcos γ = |cos γ|_obs − |cos γ|_exp after a linear fit on a
  candidate primary parameter, partial correlations, and partial
  least-squares regression of the variance [src: arXiv:2208.10767,
  Sect. 4.1].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### 2D or 3D
<!-- key: 2d-or-3d -->

- **Signal lost in 2D.** On MassiveBlack-II subhaloes, 3D filaments give a
  mean dot product 0.4882 ± 0.00136 against 0.5 random (S/N 8.68); 2D
  filaments in δz = 0.005 slices give 0.6293 ± 0.00145 against 0.6366 (S/N
  5.03); exact projections of the 3D filaments give S/N 6.81. The loss is
  ~40% and comes mostly from losing the line-of-sight direction, not from
  the slice width [src: arXiv:1902.09797, App. B]. The authors judge the
  gain unrealisable in data because the line-of-sight spin component is
  much harder to measure [src: same].
- **Cost of 3D.** Inclinations need an intrinsic-thickness model, assume
  oblate shapes, may be biased by the isophote or the bulge, and give
  anisotropic errors [src: arXiv:1902.09797, Sect. II.3].
- **Same data, both ways.** For SAMI, the 2D approach keeps M_bulge as the
  primary parameter with a weaker correlation, ρ = −0.07, p_S = 0.020 [src:
  arXiv:2208.10767, Sect. 5.4].

### Kinematic, photometric or gas spin
<!-- key: kinematic-photometric-or-gas-spin -->

- In MaNGA 3D, photometric PAs keep the signal significant but weaker:
  ⟨|cos γ|⟩ = 0.515 against 0.53 for kinematic PAs (all spirals), 0.482
  against 0.465 (all S0s) [src: arXiv:2104.08275, Table 1].
- Stellar against Hα: the MaNGA mass-dependence tension with simulations
  (χ² = 14.26 for 4 degrees of freedom, p = 0.0065, against MassiveBlack-II;
  11.09/4, p = 0.026, against Illustris) disappears with Hα spins, χ² =
  2.59/4 [src: arXiv:1902.09797, Sect. IV].
- In MaNGA 3D the S0 perpendicular signal is driven by kinematically
  misaligned galaxies, ΔPA > 20° between stars and gas [src:
  arXiv:2104.08275, Sect. 3.2].

### Finder, persistence and smoothing
<!-- key: finder-persistence-and-smoothing -->

- MaNGA 2D: Cosmic Web Reconstruction and Bisous filaments both give null
  results (0.61σ and 1.16σ), "despite the drastic methodological
  differences" [src: arXiv:1902.09797, Sect. III].
- SAMI with the 2σ network: the orthogonal signal already appears at
  M* > 10^10.2 M☉, consistent with a transition mass that scales with the
  filament scale [src: arXiv:1909.12371, Sect. 4.1].
- Haloes: flip at M₂₀₀ = 5.6 × 10¹¹ (NEXUS velocity shear) and 3.8 × 10¹¹
  h⁻¹M☉ (NEXUS+) [src: arXiv:1805.00033, Sect. 4.3]; by filament diameter
  D_f, log₁₀ M_spin-flip/(h⁻¹M☉) = m D_f + c with m = 0.32 h Mpc⁻¹, c =
  10.8 (Eq. 14), from 1.8 × 10¹¹ (thinnest) to 1.8 × 10¹² h⁻¹M☉
  (thickest); D_f is the diameter of a cylinder of length 2R, R = 2 h⁻¹Mpc,
  with the volume of the filament voxels around each spine point [src:
  Sect. 4.4.2].
- Skeleton smoothing: M₀(R) ≃ M₀(R₀)(R/R₀)^α (arXiv:1201.5794, Eq. 3) with
  α^s ≃ 0.8 ± 0.1 for skeleton filaments and α^t ≃ 0.28 ± 0.04 for
  tidal-tensor directions; in mass, M_crit ∝ M_smooth^0.27 (skeleton) and
  ∝ M_smooth^0.09 (shear), "rather weak" [src: App. D.1].

### Sample selection
<!-- key: sample-selection -->

- SAMI keeps a loose PA-error cut, Δ_PA < 25°, because over-selecting fast
  rotators would "erase the high mass signal" carried by slow rotators;
  the cut removes 40–50% of galaxies below 10^9.5 M☉ and 10–15% between
  10¹⁰ and 10¹¹ M☉; 1418 galaxies remain [src: arXiv:1909.12371,
  Sect. 2.1.2]. MaNGA removes σ_PA > 5° (858 galaxies, rotation poorly
  defined by eye); σ_PA < 3° changes results by ≲ 1σ [src:
  arXiv:1902.09797, Sect. II.3].
- Morphology: MaNGA 3D spirals need a debiased vote fraction of 0.9; S0s
  T-type ≤ 0 with P_S0 > 0.5, looser because of numbers [src:
  arXiv:2104.08275, Sects. 3.1–3.2].
- Distance to the spine: Tempel & Libeskind find spiral alignment at 0.2–0.5
  h⁻¹Mpc from the axis and none at 0–0.2 h⁻¹Mpc [src: arXiv:1308.2816,
  Sect. IV.2]. Barsanti et al. find mean |cos γ| rising with D_fil, the
  galaxy–filament distance [src: arXiv:2208.10767, Sect. 4.1].
- SAMI excludes the SAMI cluster targets [src: arXiv:1909.12371,
  Sect. 2.1], and notes that most simulation predictions include group and
  cluster galaxies, where dynamical friction and local torques on
  satellites weaken the signal, as highlighted by Dubois et al. 2014 [src:
  arXiv:1909.12371, Sect. 4.1].

### What the significance means
<!-- key: what-the-significance-means -->

The Siena Galaxy Atlas analysis computes three significances from the same
randomised PAs: the mean PDF difference in units of the random standard
deviation ⟨σ⟩, the mean against the distribution of random means
σ_⟨cos θ⟩, and a KS p-value [src: arXiv:2509.02062, Sect. 3.2]. Its
maximum-significance spiral subset gives ⟨σ⟩ = 1.567, σ_⟨cos θ⟩ = 3.859,
p_KS = 4.2 × 10⁻⁵ for the same 23,163 galaxies [src: Table 3]. That subset
was found by Gaussian-process Bayesian optimisation over four cuts
(M_r^min, M_r^max, d_fil^min, d_fil^max) [src: Sect. 4.3]; the section
read describes no correction for that search.

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Mean projected angle, low / high mass (split 10^10.8 M☉) | 43.6 ± 0.7° / 46.5 ± 1.5° (random 45°); spurious-pair probability < 1%, < 0.03% for a split above 10¹¹ | SAMI, 1418 galaxies | arXiv:1909.12371 | Sect. 4.2 |
| Excess probability per bin | ξ = 0.12 ± 0.12 (θ < 30°) for 10⁹–10^9.5 M☉; ξ = 0.1 ± 0.12 (θ > 60°) above 10^10.9 | SAMI | arXiv:1909.12371 | Sect. 4.1 |
| Predicted amplitude | ξ < 0.05 for > 150,000 simulated galaxies at z = 1.2–1.8 and 1–0 (as cited) | Horizon-AGN predictions | arXiv:1909.12371 | Sect. 4.1 |
| Mean 2D dot product, all | 0.6452 ± 0.0075 vs shuffled 0.6406 (0.61σ), 2736 galaxies; Bisous 0.6462 ± 0.0079 vs 0.6370 (1.16σ) | MaNGA, stellar | arXiv:1902.09797 | Sect. III, Table 2 |
| Intrinsic scatter | measurement-error scatter 0.0044; σ_i ≥ 0.0061 | MaNGA | arXiv:1902.09797 | Sect. III |
| 3D ⟨|cos γ|⟩ | spirals 0.53 (611, p_KS = 6.2 × 10⁻³); spirals ≤ 10¹⁰ M☉ 0.55 (230, 4.6 × 10⁻⁶); spirals > 10¹⁰ 0.517 (381, 0.64); S0s 0.465 (269, 6.5 × 10⁻³); S0s ≤ 10¹⁰ 0.425 (114, 5.6 × 10⁻⁴) | MaNGA + DisPerSE | arXiv:2104.08275 | Table 1 |
| Primary parameter | Spearman p_S = 0.014 (M*), 10⁻⁴ (B/T), 10⁻⁵ (M_bulge); PLS variance ~70% M_bulge, ~27% B/T, ~2% M* | SAMI, 1121 galaxies | arXiv:2208.10767 | Sects. 4.1, 6 |
| Low/high mass split, 3D | 10^10.2 M☉; two-sample p_2KS = 0.006 | SAMI | arXiv:2208.10767 | Sect. 4.2 |
| Halo excess probability | up to 12% (perpendicular, high mass), 15% (aligned, low mass) | Horizon 4π, 43 × 10⁶ haloes | arXiv:1201.5794 | Sect. 2.2 |
| Halo M_crit, z = 0 | 4(±1) × 10¹² M☉ in the text, 5(±1) × 10¹² M☉ in Fig. 3 and Eq. 1; M_crit ∝ (1 + z)^−2.5±0.2 | Horizon 4π, R = 5 h⁻¹Mpc | arXiv:1201.5794 | Sects. 2.2–2.3 |
| Tidal-axis M_crit | 8 × 10¹² M☉, (1 + z)^−3±0.3 | same | arXiv:1201.5794 | Eq. 2 |
| Halo flip, NEXUS | 5.6 × 10¹¹ (velocity shear), 3.8 × 10¹¹ h⁻¹M☉ (NEXUS+); inner 50% ~3 times lower | P-Millennium, 3.76 × 10⁶ haloes | arXiv:1805.00033 | Sects. 3, 4.3 |
| Flip vs filament diameter | m = 0.32 h Mpc⁻¹, c = 10.8 | P-Millennium | arXiv:1805.00033 | Eq. 14 |
| 2D signal loss | ~40% (S/N 8.68 → 5.03) | MassiveBlack-II | arXiv:1902.09797 | App. B |
| Edge-on discs | slope 0.03 ± 0.05 (all 2861); 0.13 ± 0.03 for 1890 with 0.7 < (g−i)₀ < 1.3; −0.7 ± 0.2 for 165 with (g−i)₀ > 1.4 | EGIPS × Bisous | arXiv:2507.07334 | Sects. 4, 5 |
| Siena Galaxy Atlas subsets | spirals 0.36–2 Mpc: σ_⟨cos θ⟩ = 3.859; ellipticals ≤ 2 Mpc, M_r ≤ −20.67: σ_⟨cos θ⟩ = 13.792, p_KS = 6.6 × 10⁻²⁸ | SGA × Bisous | arXiv:2509.02062 | Table 3 |
| FoG-aligned segments | 10% with |cos α_los| > 0.95 (5% expected); ~22% → ~14% above 0.9 after compression | GAMA | arXiv:1909.12371; arXiv:2208.10767 | Sect. 3.1.1; Sect. 3.2 |

The halo critical mass of Codis et al. is in M☉ in the body (no h⁻¹),
which settles the units left open in `results.md#not-verified`; the text
and the figure give 4 and 5 × 10¹² M☉ for the same quantity.

## What goes wrong
<!-- key: what-goes-wrong -->

- **Line-of-sight anisotropy read as alignment.** Redshift-space filaments
  and inclination-limited spins are both anisotropic with respect to the
  line of sight, so a uniform null produces a signal with no intrinsic
  alignment [src: arXiv:2509.02062, Sect. 3.1]; with edge-on galaxies the
  null PDF is "quite complex" [src: arXiv:2507.07334, Sect. 4]. Test:
  randomise positions or PAs on the real skeleton (Step 5 table).
- **Mass–redshift degeneracy.** In MaNGA, high-mass galaxies lie at higher
  redshift, where the sparser Main Galaxy Sample gives poorer filaments; a
  simulation built to mimic this showed weak perpendicular alignment at all
  masses instead of a flip [src: arXiv:1902.09797, Sect. IV]. Test: draw
  simulated galaxies from the observed mass–redshift distribution through
  matched filament catalogues (26 realisations there).
- **Cancellation.** A mixed-mass sample can hide opposite signals [src:
  arXiv:1902.09797, Sect. IV]. Test: split in stellar or bulge mass.
- **Selection that removes the signal.** Tight PA-quality cuts remove slow
  rotators, which carry the high-mass signal [src: arXiv:1909.12371,
  Sect. 2.1.2].
- **Contaminated IFS fits.** Several kinematically distinct galaxies in one
  bundle make FIT_KINEMATIC_PA return the line joining them; MaNGA excluded
  171 such galaxies after visual inspection [src: arXiv:1902.09797,
  Sect. II.3].
- **Correlated neighbours.** Spins correlate over ~10 h⁻¹Mpc; a
  galaxy-by-galaxy bootstrap then underestimates the covariance [src:
  arXiv:1902.09797, Sect. IV]. Test: block bootstrap.
- **Post-selection significance.** Subsets chosen to maximise significance
  (arXiv:2509.02062, Sect. 4.3). Test: report the trials or a pre-defined
  split.
- **σ from a p-value.** The edge-on paper calls p = 0.002 "4.3σ" and p =
  0.01 "3.5σ" [src: arXiv:2507.07334, Sect. 5]; these σ equal the slope
  over its error (0.13/0.03, 0.7/0.2), while a two-sided Gaussian gives
  ~3.1σ and ~2.6σ for those p-values [der: standard normal quantiles]. Test:
  state which statistic the σ belongs to.
- **Bulge decomposition.** Of 25 strongly rotation-dominated bulges, 8 are
  suspected discs [src: arXiv:2208.10767, Sect. 5.4].
- **Halo resolution.** Spin directions need ≥ 300 particles; the inner 10%
  spin flip could not be resolved [src: arXiv:1805.00033, Sects. 3, 4.3].
- **Comparing transition masses.** Halo masses (M₂₀₀ or FOF, h⁻¹M☉ or M☉),
  stellar masses and bulge masses, skeletons of different smoothing and
  persistence are not one number (Eq. 3 of arXiv:1201.5794; Eq. 14 of
  arXiv:1805.00033).

## Reading list
<!-- key: reading-list -->

- Foundation: Codis et al. 2012, arXiv:1201.5794 — 1 + ξ statistic, M_crit
  definition, redshift and smoothing scaling.
- Method: Ganeshaiah Veena et al. 2018, arXiv:1805.00033 — μ_hf, median
  criterion, flip versus filament diameter.
- Method: Tempel & Libeskind 2013, arXiv:1308.2816 — randomised null with
  fixed orientations; spirals versus ellipticals in SDSS.
- Application: Welker et al. 2020, arXiv:1909.12371 — SAMI 2D kinematic
  measurement, FoG treatments, threshold scan.
- Application: Kraljic et al. 2021, arXiv:2104.08275 — thin-disc 3D spins,
  sign ambiguity, distance cuts.
- Application: Barsanti et al. 2022, arXiv:2208.10767 — primary-parameter
  analysis (Spearman, partial correlation, PLS).
- Critique: Krolewski et al. 2019, arXiv:1902.09797 — null MaNGA result,
  2D versus 3D loss, mass–redshift trap, block bootstrap.
- Application: Muralichandran et al. 2025, arXiv:2509.02062 — three
  significance estimators on one sample.
- Method: Antipova et al. 2025, arXiv:2507.07334 — edge-on galaxies and a
  simulated non-uniform null.
- Forecast: Barsanti et al. 2025, arXiv:2512.15276 — case for joint
  spin–filament and intrinsic-alignment spectroscopic surveys (abstract
  only).

## Not verified
<!-- key: not-verified -->

- Lee & Erdogdu 2007 and Lee 2011 (thin-disc and two-sign methods) and
  Haynes & Giovanelli 1984: read only as written in arXiv:2104.08275;
  identifiers not looked up.
- Codis et al. 2018 and Dubois et al. 2014 Horizon-AGN predictions (ξ <
  0.05): cited through arXiv:1909.12371, not read.
- The per-bin values of Barsanti et al. Table 2 and the SAMI 2σ-network
  results (App. E of arXiv:1909.12371) were not read.
- No Hector or DESI spin–filament measurement was found in the 2025–2026
  search; arXiv:2512.15276 was read at abstract level only.
