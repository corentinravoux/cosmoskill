# Cosmic web — physics and methods

Scope: the theory of web formation (Zel'dovich, the cosmic-web paradigm, tidal
torques), the classification schemes and structure finders with their defining
equations and parameters, statistics of web components, environment measures,
spin-alignment measures, and the methods behind filament-gas stacking and web
reconstruction.
Snapshot: 2026-10-16

Flags: `[src]` abstract read this session; `[src: Sect. n]`, `[src: Eq. n]`,
`[src: Table n]` body read; `[sec]` named secondary source; `[der]` derived
here.

## 1. Formation of the web
<!-- key: formation-of-the-web -->

**Anisotropic collapse.** The web is the transitional stage between linear and
non-linear structure, produced by anisotropic gravitational collapse; matter
flows from voids into walls and then along filaments into the cluster nodes
(Cautun et al. 2014, arXiv:1401.7866) [src]. The Zel'dovich approximation is
the linear Lagrangian description behind this picture; the Hessian
classifications of section 2 are built on a local orbit-stability criterion
that "closely relates to the Zel'dovich approximation" (Hahn et al. 2007,
arXiv:astro-ph/0610280) [src]. The classic review of the non-linear,
intermittent structure that results is Shandarin & Zel'dovich 1989
(doi:10.1103/RevModPhys.61.185) [src].

**Cosmic-web paradigm.** Bond, Kofman & Pogosyan (1996,
arXiv:astro-ph/9512141) showed that the final web is present in embryonic form
in the initial overdensity pattern, non-linear dynamics only sharpening it;
the web is defined by the positions and primordial tidal fields of rare peaks,
the strongest filaments joining nearby clusters whose tidal tensors are nearly
aligned [src]. The same paper proposed probing cluster–cluster bridges with
weak lensing, X-rays and the SZ effect, and galaxy–galaxy bridges at high
redshift with low-column Lyα absorption [src]; these are the programmes of
sections 6 and 7.

**Hierarchical evolution.** In NEXUS+ applied to large simulations, early
times are dominated by tenuous filaments and sheets that merge, so that
today's web has fewer but much more massive structures; long, almost straight
filaments exceed 100 h⁻¹Mpc and bridge massive clusters (arXiv:1401.7866)
[src]. In the multi-stream (phase-space) description, voids are single-stream
regions, walls have three or a few streams, haloes sit at filament crossings
and filaments at wall crossings (Ramachandra & Shandarin 2015,
arXiv:1412.7768) [src].

**Tidal torques.** The standard reference for the growth of protogalactic
angular momentum by tidal torques is White 1984 (doi:10.1086/162573); only its
metadata were read this session. Because both the tidal tensor that shapes the
web and the torque that spins up haloes come from the same potential, spins
correlate with web directions (section 5).

## 2. Classification schemes and structure finders
<!-- key: classification-schemes-and-structure-finders -->

Libeskind et al. (2018, arXiv:1705.03021) compared twelve methods on one
dark-matter simulation, with results gridded on 100³ cells of (2 h⁻¹Mpc)³
[src: Sect. 5.3]. Not all methods find all components: the maximum number of
methods that can agree on a halo is 6 for knots, 12 for filaments, 9 for
sheets and 10 for voids [src: Sect. 5.3, caption of the halo-agreement
figure]. The families and their defining choices:

| Family | Method | Definition and parameters used in the comparison | Reference |
|---|---|---|---|
| Hessian of potential (T-web) | eigenvalues of T_αβ = ∂²φ/∂x_α∂x_β with ∇²φ = δ; number of eigenvalues above λ_th = 0, 1, 2, 3 gives void, sheet, filament, knot | ~1 h⁻¹Mpc cells, λ_th = 0.2 [src: Sect. 4.5]; the original paper finds the visual web already at λ_th = 0.1 and percolating voids coexisting with connected filaments for 0.2 < λ_th < 0.4; a dynamical argument suggests λ_th ≈ 1 [src] | Hahn et al. 2007, arXiv:astro-ph/0610280 (λ_th = 0, per arXiv:1705.03021 Sect. 4.4); Forero-Romero et al. 2009, arXiv:0809.4135 |
| Velocity shear (V-web) | Σ_αβ = −(1/2H₀)(∂v_α/∂r_β + ∂v_β/∂r_α); 0, 1, 2, 3 eigenvalues above threshold = void, sheet, filament, knot | Gaussian smoothing at least one cell of a 256³ grid; λ_th = 0.44 for ΛCDM [src: Sect. 4.4]; resolves structure below 0.1 h⁻¹Mpc against ~1 h⁻¹Mpc for the tidal web [src] | Hoffman et al. 2012, arXiv:1201.3367 |
| Multiscale Hessian (MMF, NEXUS, NEXUS+) | Hessian eigenvalue ratios of the field smoothed over a set of scales R_n = 2^(n/2) R₀; maximum signature over scales; knots, then filaments, then walls, rest voids | NEXUS+: log-density filter, DTFE on 600³ grid (0.33 h⁻¹Mpc), seven scales 0.5–4 h⁻¹Mpc; thresholds from virialisation (knots) and from the peak of mass change with signature (filaments, walls) [src: Sect. 4.6.1] | Aragón-Calvo et al. 2007, arXiv:0705.2072; Cautun et al. 2013, arXiv:1209.2043 |
| Topological (DisPerSE) | discrete Morse theory on the Delaunay tessellation with DTFE densities; persistence threshold in "number of sigmas" | scale-free and parameter-free apart from the persistence level [src]; works for very sparse samples, sufficient even when half the particles are noise for persistence ≥ 3σ [src] | Sousbie 2011, arXiv:1009.4015; Sousbie et al. 2011, arXiv:1009.4014 |
| Topological (watershed, SpineWeb) | watershed basins of the density field; separatrices give walls and the spine (filaments and nodes) | — | Aragón-Calvo et al. 2010, arXiv:0809.5104 |
| Stochastic (Bisous) | marked point process of interacting cylinders fitted by MCMC; returns filament-detection and orientation fields, then spines | filament radius prior 0.4–1.0 h⁻¹Mpc; visit-map threshold 0.05; orientation strength > 0.7 [src: Sect. 4.2] | Tempel et al. 2014, arXiv:1308.2533 |
| Graph (adapted MST) | minimal spanning tree on group centroids, then galaxies within distance r; "tendrils" and isolated void galaxies in a second pass | linking length chosen so that ≥ 90% of groups with M ≥ 10¹¹ M☉ are in filaments [src: Sect. 4.1] | Alpaslan et al. 2014, arXiv:1311.1211 |
| Node-to-node (FINE) | highest-density paths between nodes on a Voronoi density | nodes M > 5 × 10¹³ M☉, skeleton threshold 5 times the mean Voronoi density [src: Sect. 4.3] | Libeskind et al. 2018, Sect. 4.3 |
| Phase-space (ORIGAMI) | shell-crossing along 3, 2, 1, 0 orthogonal axes = halo, filament, wall, void | dynamical, density-independent; needs particle Lagrangian positions [src] | Falck et al. 2012, arXiv:1201.2353 |
| Phase-space (MSWA) | number of streams; voids single-stream | simulations only [src] | Ramachandra & Shandarin 2015, arXiv:1412.7768 |
| Linearised Hessian (CLASSIC) | Lagrangian-perturbation linearisation of the density, then a Hessian classification | — | Libeskind et al. 2018, Sect. 4.7 |

**Conventions that differ between papers.** Eigenvalue order (λ₁ > λ₂ > λ₃ in
T-web and V-web, λ₁ < λ₂ < λ₃ in MMF-2) [src: Sect. 4.4–4.6]; normalisation of
the tensor (4πGρ̄ for T-web, H₀ for V-web) [src: Sect. 4.4–4.5]; and whether
the method returns a volume-filling partition into four classes (Hessian,
NEXUS, ORIGAMI) or only filament spines (Bisous, FINE, MST). A statement
"galaxy X is in a filament" is therefore always relative to a method, a
tracer, a smoothing scale and a threshold.

**Phase-space versus Eulerian definitions.** ORIGAMI and MSWA are dynamical
(counting shell-crossings or streams) and need simulation particles; they
cannot be applied to galaxy catalogues. DisPerSE, Bisous and MST work directly
on discrete tracers without a smoothed field [src: arXiv:1009.4015,
arXiv:1308.2533], which is why they dominate observational filament catalogues
(`surveys-and-data.md`).

## 3. Statistics of web components
<!-- key: statistics-of-web-components -->

The statistics in use, each defined relative to a finder (values in
`results.md` §1–2):

- **Mass and volume filling fractions** per component, on a grid
  (arXiv:1705.03021) [src: Sect. 5.3].
- **Density PDF per component** and the **halo mass function per environment**
  (arXiv:1705.03021) [src: section titles 5.2 and 5.4].
- **Filament length function, radius and radial profiles**, from stacking
  tracers around spines; profiles of short and long filaments are fitted with
  the same empirical forms (generalised NFW, β-model, single and double power
  laws) with distinct parameters (arXiv:2003.09697) [src]. The filament radius
  is defined where the logarithmic slope of the stacked profile is minimal
  (arXiv:2402.11678) [src].
- **Connectivity and multiplicity**: the number of filaments globally
  connected to a node (κ) and the number emerging locally; predicted from peak
  theory and measured with the persistent skeleton (arXiv:1803.11477) [src].
  Galárraga-Espinosa et al. (2024, arXiv:2309.08659) provide a user guide and
  a physics-driven calibration of DisPerSE for filament catalogues from
  galaxies [src].
- **Topological summaries**: Betti numbers and Euler characteristic recovered
  directly from particles as a function of the persistence threshold
  (arXiv:1009.4014) [src]. Their use as cosmological summary statistics is in
  `cosmo-beyond-two-point`.

**Voids and walls as structures.** In the excursion-set picture, the void size
distribution is peaked about a characteristic size that evolves
self-similarly; voids-in-voids merge, voids-in-clouds are squeezed out, so the
model needs a two-barrier random walk and two parameters (Sheth & van de
Weygaert 2004, arXiv:astro-ph/0311260) [src]. A void defined from galaxies
need not be empty of matter: for seven nearby voids inside the Cosmicflows-3
volume, all show a positive radial gradient of galaxies but only three a clear
central matter underdensity from peculiar velocities, so emptiness "should be
derived from dynamical information" (Courtois et al. 2023, arXiv:2211.16388)
[src]. With photometric redshifts, a quasi-gravitational potential with a
watershed finder recovers dynamically dominant voids in J-PAS-like FLAMINGO
mocks, the main damage being galaxies scattered into void interiors (Mansour
et al. 2026, arXiv:2607.26932) [src]. Void finders, the void size function,
void–galaxy cross-correlations, void lensing and every cosmological use of
voids belong to `cosmo-beyond-two-point`.

## 4. Environment measures for haloes and galaxies
<!-- key: environment-measures-for-haloes-and-galaxies -->

Four families of environment variable are in use; results obtained with one
are not directly comparable with another.

| Measure | Definition as used | Example | Flag |
|---|---|---|---|
| Discrete web class | T-web (or V-web) class of the cell containing the galaxy or group | GAMA groups in voids, sheets, filaments, knots (Tojeiro et al. 2017, arXiv:1612.08595); SDSS DR18 sheets, filaments, clusters (Nandi & Pandey 2025, arXiv:2507.18614) | [src] |
| Distance to skeleton features | 3D distance of each galaxy to the nearest node, filament and wall of a DisPerSE skeleton | GAMA, 0.03 ≤ z ≤ 0.25 (Kraljic et al. 2018, arXiv:1710.02676); SIMBA, z = 3–0 (Jego et al. 2025, arXiv:2509.18077) | [src] |
| Overdensity plus tidal anisotropy | δ₈ from a top-hat of 8 h⁻¹Mpc radius (500 random points per sphere); tidal torque q²_R from the eigenvalues of the tidal tensor of the density smoothed with a 5 h⁻¹Mpc Gaussian; α_R ≡ √(q²_R) (1 + δ_R)^(−n), with n = 1 and R = 4 R_200b in simulations (Paranjape et al.), and n = 0.55 at fixed R = 5 h⁻¹Mpc chosen to remove the δ₈–α₅ correlation in SDSS | Alam et al. 2019, arXiv:1801.04878 | [src: Sect. 3.3–3.4] |
| Halo-scale tidal anisotropy | α at ~4 times the halo radius | Ramakrishnan et al. 2019, arXiv:1903.02007 | [src] |
| Matched samples | compare filament and field galaxies at fixed stellar mass and, in addition, at fixed local galaxy density | SDSS DR8 (O'Kane et al. 2024, arXiv:2409.09028) | [src] |

The Hessian classification of a given galaxy position "is not unique, but
depends on the choice of thresholds in the eigenvalues", which is why
continuous variables were introduced (arXiv:1801.04878) [src: Sect. 1]. δ₈ and
α₅ in that analysis are apparent redshift-space quantities with the Kaiser
anisotropy left uncorrected; the 8 h⁻¹Mpc radius was chosen to make fingers of
God negligible [src: Sect. 3.4].

**Interpretive frameworks.** Anisotropic assembly bias from an excursion-set
treatment with filamentary tides: at fixed mass the accretion rate varies with
orientation and distance to filaments (arXiv:1710.02676) [src]. Cosmic-web
detachment: galaxies accrete cold gas through primordial filaments until
shell-crossing on intergalactic scales detaches them (Aragón-Calvo, Neyrinck &
Silk 2016, arXiv:1607.07881) [src]. Statistical decomposition: halo
concentration, shape, velocity anisotropy and spin correlate with large-scale
bias b₁ only through α, p(α, b₁, c) ≃ p(α) p(b₁|α) p(c|α), for 8 × 10¹¹ <
M_vir/(h⁻¹M☉) < 5 × 10¹⁴ (arXiv:1903.02007) [src]. The halo-occupation view of
assembly bias and its detections is in `cosmo-galaxy-halo-connection`.

## 5. Spin and shape alignments with the web
<!-- key: spin-and-shape-alignments-with-the-web -->

**Observable.** The cosine μ = |cos θ| between a halo or galaxy axis (spin,
minor or major shape axis, velocity) and the local filament direction or wall
normal, compared with the uniform distribution; for galaxies the spin is a
kinematic axis from integral-field spectroscopy (SAMI, MaNGA) or a spin normal
inferred from the disc shape (SDSS, Siena Galaxy Atlas), often only in
projection (arXiv:1909.12371, arXiv:2509.02062) [src].

**Theory.** In conditional tidal-torque theory around filament-type saddle
points, the constrained misalignment between the tidal tensor and the density
Hessian predicts spins of less massive objects aligned with the filament and
an azimuthal (perpendicular) orientation for more massive ones, with a
transition mass that scales with the mass of non-linearity (Pichon et al.
2014, arXiv:1409.2608) [src]. The kinematic picture: low-mass haloes form by
the winding of flows in misaligned walls and acquire spin along the resulting
filament, high-mass haloes by later mergers along the filament, which converts
orbital angular momentum into perpendicular spin (Codis et al. 2012,
arXiv:1201.5794) [src]. In P-Millennium, low-mass haloes accrete mainly
perpendicular to their filament and high-mass haloes along it (Ganeshaiah
Veena et al. 2018, arXiv:1805.00033) [src].

**Boundary.** Alignments of galaxy shapes with the tidal field as a
contaminant of cosmic shear (NLA, TATT, their amplitudes in KiDS, DES, HSC)
belong to `cosmo-weak-lensing`. This skill treats the alignment as a property
of galaxy formation in the web. The two meet in Storck et al. (2024,
arXiv:2409.13010): halo orientation relative to a filament changes by up to
80% under changes of the non-linear environment at fixed initial patch, which
they flag as a limit for intrinsic-alignment models [src].

## 6. Gas in the web: methods
<!-- key: gas-in-the-web-methods -->

**Expected state.** Simulations put the missing baryons in filaments as
warm-hot intergalactic medium (WHIM) at ~5–200 times the mean baryon density
and 10⁵ < T < 10⁷ K (Walker & Lau 2022 review, arXiv:2202.07056) [src: Sect.
4.7]. In TNG300 the WHIM holds more than 80% of the baryon budget at r ~ 1 Mpc
from filament spines; filament gas is isothermal to ~1.5 Mpc with T_core =
4–13 × 10⁵ K, P_core = 4–12 × 10⁻⁷ keV cm⁻³ (about 1000 times below observed
clusters), and predicted core Compton parameters 0.5 < y < 4.1 × 10⁻⁸
(Galárraga-Espinosa et al. 2021, arXiv:2010.15139) [src].

**Four observational routes.**

1. *Individual bridges between close cluster pairs*, ideally aligned along the
   line of sight to maximise the column; detections "remain rare and limited
   to a handful of cases" (A222/223, A399/401, A2804/2811, A3556/3558,
   A2029/2033, A133, A3391/3395) plus the filaments around Abell 2744
   (arXiv:2202.07056) [src: Sect. 4.7].
2. *Galaxy-pair stacking*: rotate and rescale the maps so that pair members
   fall on common positions, subtract a circularly symmetric halo model for
   each member, and measure the residual between them (Tanimura et al. 2019,
   arXiv:1709.05024; de Graaff et al. 2019, arXiv:1709.10378) [src].
3. *Filament-spine stacking*: stack y, X-ray or lensing maps around filaments
   from a galaxy skeleton, after masking groups, clusters and point sources,
   and subtract the signal 10–20 Mpc from the spine as background (Tanimura et
   al. 2022, arXiv:2206.00084) [src]. In the eRASS:4 analysis the filaments
   are the DisPerSE catalogue of Malavasi et al. on SDSS LOWZ+CMASS (63,391
   filaments after a 3σ persistence cut, no smoothing), of which 7817 with 0.2
   < z < 0.6 and 20 < l_fil < 100 Mpc in 2275 deg² are stacked in 0.3–1.2 keV
   [src: Sect. 2 of arXiv:2406.00105]. Masking: every eRASS:4 source to the
   radius where its profile falls to 10% of the background; eRASS1 clusters
   and groups at 1.5 r_500c; redMaPPer clusters with λ > 20 at 1.5 r_λ; SDSS
   groups with n_sat > 1 at max(400 kpc, 1.5 r_500c); DisPerSE maxima and
   bifurcations at 2 Mpc [src: Sect. 2.1, Table 1 of arXiv:2406.00105].
4. *Oriented (constrained) stacking*: orient each stack on the local
   large-scale structure and decompose into cosine multipoles m; applied to
   tSZ around clusters in superclusters (Lokken et al. 2024, arXiv:2409.04535)
   and to the kSZ around photometric BGS galaxies oriented on 2D filaments
   from the Hessian of the projected potential (Hadzhiyska, Ferraro & Zhou
   2024, arXiv:2412.03631) [src].

**Interpretation models.** Isothermal cylinders with a β-model (β = 2/3)
profile and the gas following the dark matter (arXiv:1911.09706,
arXiv:2206.00084) [src], or density ∝ r_c/r (arXiv:1709.05024) [src];
temperature from an APEC spectral fit (arXiv:2011.05343, arXiv:2406.00105)
[src] or from combining tSZ with lensing (arXiv:1709.10378) [src]. The
pressure–density degeneracy means that a tSZ detection alone constrains δ_c ×
T_e × r_c (arXiv:1709.05024) [src].

The use of the kSZ and tSZ in cross-correlation with galaxy samples for
cosmology and feedback (b_v, gas profiles, baryonic suppression) is in
`cosmo-cmb-lss-cross-correlations`.

## 7. Reconstructing the web from data
<!-- key: reconstructing-the-web-from-data -->

The classifications of section 2 need a density, potential or velocity field;
with data that field must first be reconstructed, and the reconstruction sets
the scale and the reliability of the web.

| Input | Method | What is classified | Example | Flag |
|---|---|---|---|---|
| Galaxy redshift survey | Bayesian forward modelling of initial conditions (BORG), then probabilistic web maps with propagated uncertainties | dynamic web elements, posterior probabilities per voxel | Leclercq et al. 2015, arXiv:1512.02242 | [src] |
| Galaxy positions only, no density field | stochastic topological ranking of each object against matched randoms (ASTRA), 100 realisations per tracer and zone | per-object probabilities of void, sheet, filament, knot; thresholds on the rank r recalibrated from |r| = 0.9 to e.g. r ≤ −0.25 for voids to match the GAMA void volume fraction (59% at 4 h⁻¹Mpc smoothing) | Zapata-Zuluaga et al. 2026, arXiv:2604.01456 | [src: Sect. "The rank parameter r", Table 2] |
| Spectro-photometric galaxies | probabilistic DisPerSE on miniJPAS + DESI, local filaments within 3 Mpc of each galaxy with M* > 10¹⁰ M☉ | galaxy connectivity to local filaments | Galárraga-Espinosa et al. 2025, arXiv:2506.15345 | [src] |
| Peculiar velocities | Wiener filter or Hamiltonian Monte Carlo reconstruction of the velocity field, then V-web | attractors, repellers, voids and knots | Hoffman et al. 2017, arXiv:1702.02483 (Cosmicflows-2); Hollinger & Courtois 2026, arXiv:2606.13538 (CF4++ZOA) | [src] |
| Lyα forest tomography | Wiener filtering, or constrained reconstruction of initial conditions with a fast gravity model (TARDIS) | eigenvalues and eigenvectors of the pseudo-deformation tensor | Horowitz et al. 2019, arXiv:1903.09049 | [src] |

**V-web on peculiar velocities.** For CF4++ZOA the threshold is λ_th = 0, "a
conventional choice in the linear regime", where the sign of each shear
eigenvalue separates expansion from compression; structures are kept only if
recovered in at least 68% of the HMC realisations and away from survey
boundaries (arXiv:2606.13538) [src: Sect. 2.1, Sect. 4]. A physically
motivated alternative normalises the V-web by the standard deviation of the
velocity divergence and finds a "constant volume threshold" that conserves
volume fractions for 0 < z < 2, most precisely at ~3 h⁻¹Mpc smoothing (Olex,
Hellwing & Knebe 2025, arXiv:2412.09531) [src].

**Lyα tomography.** Surveys with ≲ 5 h⁻¹Mpc sightline spacing recover the
tidal-tensor eigenvectors well enough to measure galaxy–web alignments at z ~
2.5; CLAMATO-like data with 600 zCOSMOS-Deep galaxies would give 3σ limits
only on extreme models with Δ⟨cos θ⟩ ~ 0.1, while > 10,000 galaxies (Subaru
PFS) are needed for Δ⟨cos θ⟩ ~ 0.03 (Krolewski et al. 2017, arXiv:1612.00067,
**forecast**) [src]. With 30 m-class telescope mocks, TARDIS eigenvalues
correlate with the truth at r = 0.95 and can be evolved to z = 0
(arXiv:1903.09049) [src]. Tomography surveys, map-making and their data are in
`cosmo-lyman-alpha`; constrained simulations of the local web (CLUES,
BORG-2M++, Manticore, Hamlet-PM) are in `cosmo-simulations-mocks`.

## 8. Public codes
<!-- key: public-codes -->

| Code | Use | Reference | Flag |
|---|---|---|---|
| DisPerSE | topological skeleton, walls and voids from discrete tracers; persistence in σ | arXiv:1009.4015 | [src] |
| Multi-block DisPerSE | gigaparsec volumes; 99.6% total length and 94.7% individual filament recovery against a monolithic run on a 300 h⁻¹Mpc MDPL2 subvolume | arXiv:2607.14785 | [src] |
| NEXUS / NEXUS+ | multiscale Hessian on density, log-density, tidal, velocity divergence and shear fields | arXiv:1209.2043 | [src] |
| Bisous | stochastic filament spines and orientation fields | arXiv:1308.2533 | [src] |
| ORIGAMI | phase-space shell-crossing classification of simulation particles | arXiv:1201.2353 | [src] |
| ASTRA | per-object probabilistic web class from positions and randoms; DESI EDR catalogue and pipeline public | arXiv:2604.01456 | [src] |
| T-web, V-web | Hessian classification on grids; implementations differ by group | arXiv:0809.4135, arXiv:1201.3367 | [src] |

Code repositories and versions are not listed here; they were not checked this
session.
