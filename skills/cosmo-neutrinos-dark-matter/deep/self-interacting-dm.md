# Self-interacting dark matter on group and cluster scales — cosmo-neutrinos-dark-matter dossier

Scope: how a limit on the self-interaction cross section per unit mass is
produced from cluster mergers (offsets and the drag model) and from the
inner density profiles of relaxed groups and clusters (isothermal Jeans
model, r₁ matching, ensemble combination), which cross section and which
velocity average a limit refers to, and how each method has been
calibrated and criticised. The two worked methods come from the
Massey–Harvey–Robertson (offsets) and Kaplinghat–Tulin–Sagunski (Jeans)
lineages; the other cluster routes (Bullet simulations, BCG wobbles, halo
and X-ray shapes, weak-lensing profiles, the cluster RAR, lensing with
kinematics), the dwarf and rotation-curve routes and the gravothermal
calibration are given one line each by other teams.
Snapshot: 2026-10-22.
From: Snowmass 2021 halo-measurements white paper (Bechtol et al.,
arXiv:2203.07354), Sects. 2.2.1, 3.2.1–3.2.2, 4.2.3.

Already in L2, not repeated here: the headline limits and their history
(`results.md#self-interacting-dark-matter-cross-section-per`,
`results.md#self-interaction-cross-section-on-cluster-scales`); the
velocity-dependent picture and core collapse in rotation curves
(`open-questions.md#self-interacting-dark-matter`); the one-paragraph
systematics (`systematics.md#interacting-and-self-interacting-dark-matter`);
the definition of σ/m as a velocity-labelled quantity
(`physics-and-methods.md#self-interactions`).

## How it is done
<!-- key: how-it-is-done -->

Notation: σ/m is a cross section per unit dark-matter mass in cm²/g; v
or v_rel the relative velocity of two particles; σ₀ (Jeans papers) or v₀
(particle papers) the one-dimensional velocity dispersion; ⟨·⟩ an average
over a Maxwell–Boltzmann distribution; t₀ or t_age the age of the system.

### Step 0. Say which cross section
<!-- key: step-0-say-which-cross-section -->

The total cross section σ = ∫dΩ dσ/dΩ is not what the astrophysical
probes measure when scattering is anisotropic. Two proxies are in use
(Colquhoun et al. 2020, arXiv:2011.04679, Sect. I):

- momentum-transfer cross section σ_T ≡ ∫dΩ (1 − cos θ) dσ/dΩ (Eq. 4);
  it governs the drag force and evaporation of a subhalo moving through a
  host, but weights backward scattering, which leaves distributions
  unchanged, and is ill-defined for identical particles;
- viscosity cross section σ_V ≡ ∫dΩ sin²θ dσ/dΩ (Eq. 5); it is the kinetic
  theory quantity for viscosity and heat conduction, which fluid
  descriptions of halo evolution use, and is well defined for identical
  particles [src: Sect. I]. For identical particles σ_T = σ and the
  relevant quantity is σ_V; in one regime σ_V^even ≈ 2σ_T [src:
  Sect. II.3].

What the analyses state:

| Analysis | Cross section named | Place read |
|---|---|---|
| Harvey et al. 2015, 72 mergers | "momentum transfer cross-section" | arXiv:1503.07675, main text |
| Andrade et al. 2020, cluster lensing | "scattering transfer cross section"; for a sharp velocity dependence, the velocity-averaged transfer cross section | arXiv:2012.06611, Sect. 6.1 |
| Sagunski et al. 2020, Jeans | σ defined through Eq. 8; for anisotropic scattering "the appropriate angular moment" | arXiv:2006.12515, Sect. II.1, footnote 1 |
| Robertson, Massey & Eke 2016, Bullet simulations | isotropic, velocity-independent, dσ/dΩ = σ/4π | arXiv:1605.04307, Sect. 2.1.1 |
| TNGC-SIDM I 2026, merger simulations | isotropic, velocity-independent σ_T/m = 1 (and 0.5) cm²/g | arXiv:2610.18957 [src] |
| Sabarish et al. 2023, merger simulations | velocity-dependent, both rare (isotropic) and frequent (small-angle) scattering | arXiv:2310.07769 [src] |
| Adhikari et al. 2024, ACT × DES weak lensing | isotropic, elastic σ/m; also dissipative SIDM | arXiv:2401.05788 [src] |
| Zavala et al. 2013, dwarf spheroidals | σ_T/m, velocity-independent | arXiv:1211.6426 [src] |

### Step 1. Say which velocity average
<!-- key: step-1-say-which-velocity-average -->

For a Maxwell–Boltzmann distribution with dispersion v₀ the mean relative
velocity is ⟨v_rel⟩ = 4v₀/√π (arXiv:2011.04679, Eq. 90; the same factor in
arXiv:2006.12515, Sect. II.1, and arXiv:2012.06611, Sect. 6.1). The
observational papers define

  σ/m = ⟨σv⟩/m / ⟨v⟩   (arXiv:2006.12515, Eq. 8),

exact for a contact interaction and used "as a definition" otherwise, so
that systems of different velocity can be placed on one plot [src:
Sect. II.1]. Colquhoun et al. show that the momentum and energy transfer
rates go as ⟨σ_T v_rel²⟩ and ⟨σ_V v_rel³⟩, not ⟨σ v_rel⟩, and define
averaged cross sections (Eq. 91)

  σ̄_T = ⟨σ_T v_rel²⟩ / (16√2 v₀²/π),  σ̄_V = ⟨σ_V v_rel³⟩ / (24 v₀³/√π),

with rates Γ_p = (ρ/m) σ̄_T ⟨v_rel⟩ and Γ_E = (ρ/m) σ̄_V ⟨v_rel⟩ (Eq. 92);
core formation is expected where Γ_E t₀ > 1 [src: Sect. IV.2]. For a
velocity-independent cross section σ̄_T ≈ 0.83 σ_T and σ̄_V ≈ 1.34 σ_V
[src: same]. These weightings favour the faster collisions and stay
finite for σ ∝ v⁻⁴, unlike ⟨σv⟩ [src: same]. A limit converted to a
particle model must therefore state the moment and the weighting used.

### Step 2a. Mergers: offsets to a drag coefficient
<!-- key: step-2a-mergers-offsets-to-a-drag-coefficient -->

Harvey et al. 2015 (arXiv:1503.07675):

1. **Positions.** Gas from Chandra X-ray, galaxies from optical imaging,
   total mass from HST weak lensing; clumps matched automatically in both
   directions, with literature priors inserted by hand for A520 and A2744
   [src: "Positional offsets between components"].
2. **Geometry.** The galaxy-to-gas vector δ_SG defines the direction of
   motion; δ_SI is the lensing-mass offset along it from the intersection
   point I, δ_DI the perpendicular offset, used as a control [src: same].
   The lensing position is corrected for the pull of a subdominant
   component, f δ e^(−0.01δ/r_s) for a component holding a fraction f of
   the mass at offset δ [src: same].
3. **Errors.** The rms of the control δ_DI between systems, 60 kpc, is
   adopted as the error on every δ_DI, δ_SI and δ_SG, because some
   individual errors were "anomalously low" [src: same].
4. **Statistic.** β = δ_SI/δ_SG, chosen because it removes the dependence
   on the angle of the collision to the line of sight and, under quasi
   steady state, "should be the same for every system" [src:
   "Interpreting positional offsets"]. Per-system posteriors are taken as
   Gaussian (although the ratio is Cauchy distributed) and multiplied
   [src: "Positional offsets"].
5. **Drag model.** ⟨β⟩ = B[1 − exp(−(σ_DM − σ_gal)/σ*)] (Eq. S1), with
   σ_gal ≈ 0; B (Eq. S2) compares drag coefficients, sizes, masses and
   ambient densities of dark matter and gas, conservatively B ≳ 1; σ*/m,
   the cross section at which the halo becomes optically thick, is
   6.5 ± 3 cm²/g for M₂₀₀ = 10^(14±1) M⊙ NFW haloes and is marginalised
   analytically [src: same]. The prescription follows simulations in which
   frequent, low-momentum-transfer interactions produce a drag; isotropic
   "billiard ball" scattering instead produces mass loss [src: same].
6. **Result.** ⟨β⟩ = −0.04 ± 0.07 (68%), σ_DM/m = −0.25 (+0.42/−0.43)
   cm²/g (68%, two-tailed), < 0.47 cm²/g (95%, one-tailed); control
   ⟨β_⊥⟩ = −0.06 ± 0.07 [src: main text].

Peer on a single system: for the Bullet Cluster, Randall et al. ran SIDM
N-body simulations of 1E 0657-56 against X-ray, lensing and optical data;
the absence of a subcluster mass–galaxy offset gives σ/m < 1.25 cm²/g
(68%), and the subcluster mass-to-light ratio, if equal to the main
cluster's before the merger, σ/m < 0.7 cm²/g [src: arXiv:0704.0261,
abstract].

### Step 2b. Relaxed haloes: the isothermal Jeans model
<!-- key: step-2b-relaxed-haloes-the-isothermal-jeans -->

Used by Sagunski et al. 2020 (arXiv:2006.12515, Sect. II.1) and Andrade et
al. 2020 (arXiv:2012.06611, Sect. 6.1), both following Kaplinghat et al.
2016 (cited there):

1. **Matching radius.** r₁ is where a particle has scattered once on
   average over the age of the system:
   ρ_SIDM(r₁) ⟨σv⟩/m t₀ = 1 (arXiv:2006.12515, Eq. 1; arXiv:2012.06611,
   Eq. 5). Sagunski et al. set t₀ = 5 Gyr for groups and clusters; Andrade
   et al. use the cosmic time at each cluster's redshift [src: both].
2. **Inner halo.** Isothermal, from the time-independent Jeans equation
   ∇(σ₀² ρ_iso) = −ρ_iso ∇Φ_tot (Eq. 2), with Φ_tot including baryons; two
   parameters, ρ₀ and an isotropic, spatially uniform σ₀ [src:
   arXiv:2006.12515]. Andrade et al. use the strong-lensing BCG (dPIE
   profile) as the baryons and start the integration at 1% of the stellar
   core radius [src: arXiv:2012.06611, Sect. 6.1].
3. **Outer halo.** NFW (or NFW with adiabatic contraction, AC) for r > r₁,
   matched in density and enclosed mass at r₁ [src: both]. Andrade et al.
   first match γ_M(r) = M(r)/(4πr³ρ(r)) to get r₁/r_s, which fails if
   γ_M(r₁) < 0.5 because NFW has γ_M ≥ 0.5; such cases are rare and
   unphysical [src: arXiv:2012.06611, Sect. 6.1].
4. **Parameters.** Without AC: (ρ₀, σ₀), (M₂₀₀, c) and r₁, three
   independent after matching; AC adds w [src: arXiv:2006.12515]. Andrade
   et al. sample R₀ = ρ₀ (σ/m)(4/√π) σ₀ t_age instead of ρ₀, with R₀ > 1,
   so that r₁ always exists [src: arXiv:2012.06611, Sect. 6.1].
5. **Two solutions.** For given data a small σ/m (core growth) and a large
   σ/m (core collapse) can both fit. Sagunski et al. keep only core growth
   through ΔU = U_SIDM − U_CDM > 0 [src: arXiv:2006.12515]; Andrade et al.
   do not search for the second solution [src: arXiv:2012.06611].
6. **Projection and shape.** Andrade et al. make the halo ellipsoidal
   along the line of sight, κ_e(R) = κ(R)/s, with a prior on s from
   simulations (Vega-Ferrero et al. 2017 PDF below 0.5, flat above) [src:
   Sect. 6.1]; the data prefer s ≈ 0.5 for all clusters [src: same].

The data side differs. Sagunski et al. fit stellar kinematics, projected
stellar density, effective Einstein radius and virial mass for the Newman
et al. groups and clusters, with free Υ⋆ and stellar anisotropy β
[src: Sect. IV.2, V]. Andrade et al. fit the dark-matter surface density
from Qlens strong-lensing models of eight clusters between 10 and 150 kpc
[src: abstract].

A peer on one cluster: O'Donnell et al. fit MACS J0138-2155 with strong
lensing and spatially resolved BCG kinematics; they compute the isothermal
Jeans SIDM profile at every step instead of fitting a cored NFW and
converting "after-the-fact" as Andrade et al. did, and take the halo age
as the age of the Universe at the cluster redshift (9.9 Gyr), "the same
as Andrade et al." [src: arXiv:2508.20179, Sects. I.2, III.1]. They
justify the core-growth branch by an estimate (relation of Outmezguine
et al.) that such a cluster begins collapsing after 216 Gyr at
0.1 cm²/g, 22 Gyr at 1 cm²/g [src: Sect. III.1, footnote 2]. Code:
`sidm_halos` [src: same]. A method comparison on nine isolated galaxies
and BCGs finds gravothermal-fluid and isothermal cross sections
consistent at 1σ, the isothermal method preferring values ~3 times larger
[src: Yang et al. 2023, arXiv:2305.05067, abstract].

### Step 3. Combine systems
<!-- key: step-3-combine-systems -->

- **Merger ensemble.** Product of per-system Gaussians in β [src:
  arXiv:1503.07675]. Inverse-variance weights go as
  w_i ∝ δ_SG,i² / (1 + δ_SI,i²/δ_SG,i²) (arXiv:1701.05877, Eq. 3), so
  substructures with large galaxy–gas separations dominate: 16 of 72 carry
  85% of the weight [src: Sect. II].
- **Jeans, age marginalised.** Because Eq. 1 depends on (σ/m)t₀,
  (σ/m)_n = (σ/m) t_n/t₀ (Eq. 16) and the joint density is
  P(σ/m) ∝ Π_n ∫dt_n π(t_n) P_n((σ/m)_n) (Eq. 17), with π(t_n) Gaussian,
  5 ± 2 Gyr [src: arXiv:2006.12515, Sect. III.2]. Individual posteriors
  are not quoted because their medians are skewed by long tails [src:
  same].
- **Lensing, systematic floor.** L = Π_i N(μ_i | μ_true,
  √(ε_i² + ε_model²)) on μ = log₁₀(σ/m) (Eq. 9), uniform priors
  μ_true ∈ [−2, 0], ε_model ∈ [0, 2]; ε_model = 0.27 dex, larger than any
  individual error; 0.27/√8 ≈ 0.1 dex on the mean reproduces the 95%
  bound 0.082 × 10^0.2 ≈ 0.13 cm²/g [src: arXiv:2012.06611, Sect. 6.3].
  Linear and truncated-normal alternatives agree [src: same].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Offsets or profiles
<!-- key: offsets-or-profiles -->

| | Merger offsets | Jeans profiles |
|---|---|---|
| Physics assumed | drag analogy, quasi steady state, B ≳ 1 (arXiv:1503.07675) | inner equilibrium, optically thin (σ/m ≲ 10 cm²/g), spherical or LOS-ellipsoidal (arXiv:2006.12515, Sect. II.1) |
| Sensitive to | interactions that exchange little momentum (long-range, anisotropic) | energy redistribution (core size) |
| Main nuisance | centroid method and peak identification | baryons, age, anisotropy, AC, LOS elongation |
| Typical velocity | cluster collision velocities | ⟨v⟩ = 1150 km/s (groups), 1900 km/s (clusters) (arXiv:2006.12515, Table 3); 1458 km/s (arXiv:2012.06611) |

Wittman et al. note that self-interaction models other than drag-like
ones "are not well probed by the DM offset" [src: arXiv:1701.05877,
Sect. II, footnote 3].

### Centroid method in simulated mergers
<!-- key: centroid-method-in-simulated-mergers -->

In Bullet-like idealised simulations, the method used to locate stars and
dark matter changes the offset by as much as changing the cross section
does, "particularly soon after core passage" [src: arXiv:1605.04307,
Sect. 4.3]. Mechanism: isotropic scattering kicks only a subset of
particles, which form a wake that pulls back unscattered dark matter and
galaxies alike; a measured offset is a fit to that wake [src: same].
With σ/m = 1 cm²/g, 13% of bullet-halo particles scatter off the main
halo [src: same]. Shrinking circles over all dark matter, as used for the
2008 Bullet limit, gives large offsets and is sensitive to the starting
position and radius; parametric fits to projected density or shear are
recommended [src: Sects. 4.3, 5]. Fiducial σ/m = 2 cm²/g gives ~20 kpc,
inside the observed 25 ± 29 kpc, so the 1.25 cm²/g (68%) limit is
"strongly overstated" [src: Sect. 5]. Weak lensing locates the bullet halo
to ±40 kpc with 80 galaxies/arcmin² [src: Sect. 4.3]. Gas stripping
introduces radially dependent asymmetries, so methods probing different
radii can show an offset where none exists [src: abstract, Sect. 5].

Other simulation teams, one line each:

- Equal-mass 10¹⁵ M⊙ mergers give maximal galaxy–dark-matter offsets
  ≲ 20 kpc at 1 cm²/g, an order of magnitude below those measured in
  (near-)equal-mass mergers, so "competitive cross-section constraints are
  thus unlikely to emerge from offsets"; BCGs then oscillate on ~100 kpc
  orbits for Gyr [src: Kim, Peter & Wittman 2017, arXiv:1608.08630,
  abstract].
- With the intracluster medium included, offsets just after first
  pericentre hardly change, but can be amplified later; mergers near first
  apocentre may be more informative [src: Fischer et al. 2023,
  arXiv:2302.07882, abstract].
- For velocity-dependent rare and frequent scattering at current upper
  bounds, offsets just after first pericentre are ≤ 10 kpc in
  dark-matter-only runs; the BCG offset grows later [src: Sabarish et al.
  2023, arXiv:2310.07769, abstract].

### Re-measured offsets of the 72-merger sample
<!-- key: re-measured-offsets-of-the-72-merger-sample -->

Wittman, Golovich & Dawson 2018 re-examine the 16 highest-weight
substructures with fuller data and correct "several substantial errors"
in the offsets [src: arXiv:1701.05877, abstract]. They marginalise σ* =
3.5–9.5 cm²/g numerically on a grid instead of in quadrature [src:
Sect. IV]. Results [src: same]:

| Variant | 95% limit |
|---|---|
| H15 offsets, 60 kpc errors, no physical prior | σ/m < 0.5 cm²/g; 70% confidence that σ/m < 0 |
| Corrected full sample | < 1.71 cm²/g |
| Reviewed subsample only | < 2.27 cm²/g |
| Prior σ/m ≥ 0 | moves the corrected limits by ≤ 0.15 cm²/g |

Using H15's individual offset errors instead of the uniform 60 kpc shifts
the peak by about 2σ, in the same direction as the corrections [src:
same]. The strict H15 limit "is possible only if the physical prior is
discarded" [src: same]; many clusters violate the prescription's
assumptions, so even the revised limit "should be used with caution"
[src: abstract].

### Adiabatic contraction and other Jeans nuisances
<!-- key: adiabatic-contraction-and-other-jeans-nuisances -->

AC of the outer halo raises the inner density, which the fit offsets
with a larger σ/m: groups 0.4 → 0.6 cm²/g, clusters 0.15 → 0.20 cm²/g;
95% limits < 0.9 → < 1.1 (groups), < 0.28 → < 0.35 cm²/g (clusters)
[src: arXiv:2006.12515, Sect. III.2, Eqs. 18–21]. The headline Table 3
values (0.5 ± 0.2, 0.19 ± 0.09) are mean and standard deviation of the
sum of the with- and without-AC densities, and the 95% limits are taken
from the AC case "since these are more conservative" [src: Sect. V,
Table 3]. AC follows a modified adiabatic invariant with r₀ = 0.03 r₂₀₀,
A₀ = 1.6, w in 0.6–1.3 [src: Sect. II.1]. Only 3 of 8 groups and 3 of 7
clusters improve χ² by more than 1 over CDM [src: Sect. III.2].

### How strong-lensing densities drive the cluster bound
<!-- key: how-strong-lensing-densities-drive-the-cluster -->

From Eq. 5, ρ(r₁) = 1/(⟨σv⟩/m t_age): at z = 0.3 and ⟨v⟩ = 1500 km/s,
σ/m ≥ 0.1 cm²/g requires ρ(r₁) ≤ 3.12 × 10⁶ M⊙ kpc⁻³, so denser haloes
disfavour such cross sections [src: arXiv:2012.06611, Sect. 6.1.1]. The
cored-NFW fits find uniformly high surface densities at 30 kpc, which
"directly lead to the strong constraints"; r₁ lies at 30–140 kpc, outside
the BCG and inside the strong-lensing data, except for A611 [src:
Sects. 6.1.1, 6.3; Fig. 8 caption].

### Other cluster routes, one line each
<!-- key: other-cluster-routes-one-line-each -->

| Route | Result as stated | Source |
|---|---|---|
| BCG wobbles, 10 relaxed clusters vs BAHAMAS-SIDM | consistent with CDM at ~1.5σ; σ/m < 0.12 (0.39) cm²/g at 68% (95%) | Harvey et al. 2019, arXiv:1812.06981 [src: abstract] |
| Cluster Einstein radii vs CLASH, BAHAMAS-SIDM | σ/m > 1 cm²/g at ~1000 km/s "likely incompatible"; SIDM cores not reflected in gas, stars or X-ray luminosity | Robertson et al. 2019, arXiv:1810.05649 [src: abstract] |
| Halo shapes (lensing potentials, X-ray isophotes) | earlier limit of ~0.02 cm²/g "off by more than an order of magnitude"; at least 0.1 cm²/g allowed | Peter et al. 2013, arXiv:1208.3026 [src: abstract] |
| X-ray ellipticity, 84 relaxed Chandra/ROSAT clusters vs adiabatic zooms | non-cool-core clusters agree better with 0.5–1 cm²/g; CDM and 0.1 cm²/g disfavoured at 68%; missing cooling and feedback could reconcile CDM | Shen et al. 2022, arXiv:2202.00038 [src: abstract] |
| Weak-lensing profiles, ACT clusters × DES sources | isotropic elastic σ/m < 1 cm²/g (95%) | Adhikari et al. 2024, arXiv:2401.05788 [src] |
| Cluster radial acceleration relation vs CLASH | σ/m = 0.3 cm²/g disfavoured at 3.8σ using r > 100 kpc | Tam et al. 2022, arXiv:2207.03506 [src: abstract] |
| Lensing + BCG kinematics, MACS J0138 | σ/m < 0.613 cm²/g (95%) at ⟨v_pair⟩ < 2090 km/s | O'Donnell et al. 2025, arXiv:2508.20179 [src: abstract] |

O'Donnell et al. judge the routes that do not reconstruct the inner
profile (merger offsets, BCG offsets, the RAR, ellipticities) "not yet
competitive" with strong-lensing profile constraints, for observational
and theoretical reasons [src: arXiv:2508.20179, Sect. I.2]. The range
preferred by Shen et al. (0.5–1 cm²/g) lies above the 95% limits of the
BCG-wobble and MACS J0138 analyses [der: values in this table]; each
paper states its own caveats, and none compares the routes on common
clusters.

### Velocity-independent or velocity-dependent reading
<!-- key: velocity-independent-or-velocity-dependent -->

Profiles at several velocities combine into ⟨σv⟩/m against ⟨v⟩ (groups
590 ± 370, clusters 300 ± 150 cm²/g × km/s) [src: arXiv:2006.12515,
Table 3]. A cross section falling with velocity, for example a 15 GeV
particle with an 11 MeV dark photon, is consistent with all scales in that
paper's Fig. 3 [src: Fig. 3 caption]. For Yukawa models the averaged
σ̄_T, σ̄_V of Eq. 91 replace evaluation at ⟨v_rel⟩, which smooths the
resonant wiggles [src: arXiv:2011.04679, Sect. IV.2].

### Galaxy and dwarf scales, one line each
<!-- key: galaxy-and-dwarf-scales-one-line-each -->

The velocity dependence is set by combining the cluster limits above with
lower-velocity systems; the claims, both ways:

- **Rotation-curve diversity.** SIDM with a fixed cross section and the
  CDM concentration–mass relation fits galaxies of 25–300 km/s across the
  full diversity, through baryons and assembly scatter [src: Kamada et al.
  2017, arXiv:1611.02716, abstract]. Controlled simulations find the
  observed scatter exceeds dark-matter-only predictions in both CDM and
  SIDM; realistic baryons help, better with SIDM, but feasibility "depends
  on the sampling of the halo mass-concentration relation" [src: Creasey
  et al. 2017, arXiv:1612.03903, abstract]. A strong regime,
  σ/m ≈ 20–40 cm²/g in dwarfs, lets concentrated haloes collapse within
  10 Gyr and accommodates high-density outliers of 14 LSB galaxies [src:
  Roberts et al. 2024, arXiv:2407.15005, abstract].
- **Milky Way satellites.** σ_T/m ~ 0.1 cm²/g leaves subhaloes too massive
  for Fornax and Sculptor; ~1 cm²/g resolves it [src: Zavala et al. 2013,
  arXiv:1211.6426, abstract]. Simulated subhalo central densities favour
  σ/m < 3 cm²/g [src: Ebisu et al. 2021, arXiv:2107.05967, abstract]. With
  gravothermal collapse in a semi-analytic subhalo model, classical plus
  ultrafaint kinematics "decisively" prefer CDM over velocity-independent
  SIDM above ~0.2 cm²/g [src: Ando et al. 2025, arXiv:2503.13650,
  abstract]. In the opposite direction, 1–5 cm²/g subhaloes are not dense
  enough for the densest dwarfs, which motivates velocity-dependent cross
  sections > 5 cm²/g at satellite velocities so that some collapse [src:
  Silverman et al. 2022, arXiv:2203.10104, abstract]. The two last papers
  differ in velocity dependence and modelling; neither tests the other's.

### Gravothermal-collapse calibration
<!-- key: gravothermal-collapse-calibration -->

- Collapsed vdSIDM subhaloes (σ_T/m up to 100 cm²/g) reach inner slopes
  ≈ −3 down to the resolution limit; resolving the collapse below 1 kpc
  needs tailored runs [src: Turner et al. 2021, arXiv:2010.02924,
  abstract].
- N-body collapse is very sensitive to energy-conservation errors (keep
  them well below 1%) and an oversized SIDM kernel speeds it up
  artificially [src: Fischer, Yu & Dolag 2025, arXiv:2506.06269,
  abstract].
- A spherical DSMC code shows N-body runs converge only with softening
  well below collisionless practice; the harmonic interpolation of
  long- and short-mean-free-path conductivities in fluid models is
  inaccurate; collapse starts somewhat sooner but slows "dramatically"
  once the core is optically thick [src: van den Bosch & Tokayer 2026,
  arXiv:2610.28890, abstract].
- Strong-lensing tests of collapse (dense perturbers in arcs) are in
  `strong-lensing-substructure.md#dense-perturbers-and-sidm-the-competing-readings`; for cluster
  galaxy–galaxy lensing, subhalo inner slopes γ > 2.5, which core collapse
  could produce, alleviate the reported excess [src: Dutra, Natarajan &
  Gilman 2024, arXiv:2406.17024, abstract].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Merger offset error | 60 kpc per offset (rms of control) | 72 mergers | arXiv:1503.07675 | "Positional offsets" |
| Jackknife error | ±0.5 cm²/g | 72 mergers | arXiv:1503.07675 | same |
| σ*/m | 6.5 ± 3 cm²/g (M₂₀₀ = 10^(14±1) M⊙) | 72 mergers | arXiv:1503.07675 | "Interpreting" |
| σ/m vs assumed halo mass | −0.23 ± 0.60 (10¹³ M⊙) to −0.1 ± 0.28 (10¹⁵ M⊙) cm²/g | 72 mergers | arXiv:1503.07675 | Fig. S6 text |
| Hot / cool gas halves | −0.10 ± 0.58 / −0.50 ± 0.64 cm²/g (T >/< 8 keV) | 72 mergers | arXiv:1503.07675 | Fig. S7 text |
| Without gas-pull correction | < 0.54 cm²/g (68%, one-tailed) | 72 mergers | arXiv:1503.07675 | "Positional offsets" |
| Universal baryon ratio assumed | Ω_B/Ω_D = 0.184 | 72 mergers | arXiv:1503.07675 | "Interpreting" |
| Weight concentration | 16 of 72 substructures = 85% | re-analysis | arXiv:1701.05877 | Sect. II |
| System age | 5 Gyr, prior ±2 Gyr in the combination | Jeans | arXiv:2006.12515 | Sects. II.1, III.2 |
| Mock recovery, true 1 cm²/g | 1.1 (+0.5/−0.3), 1.7 (+0.8/−0.5), 1.4 (+0.6/−0.4) cm²/g for slit angles 0°, 45°, 90° | Jeans on SIDM + baryon clusters | arXiv:2006.12515 | Eq. 33 |
| Jeans priors (lensing) | 5 < R₀ < 500; 400 < σ₀ < 1400 km/s; 0.01 < σ/m < 1 cm²/g; 10¹¹ < M_BCG < 10¹³ M⊙; 0.3 < s < 1 | 8 clusters | arXiv:2012.06611 | Sect. 6.1 |
| Model floor | ε_model = 0.27 dex | 8 clusters | arXiv:2012.06611 | Sect. 6.3 |
| μ_true | −1.086 ± 0.125 | 8 clusters | arXiv:2012.06611 | Sect. 6.3 |
| Core recovery of the Jeans model | 10–20% for σ/m < 1 cm²/g (Sokolenko et al. 2018 as cited) | — | arXiv:2012.06611 | Sect. 6.1 |
| Averaged-cross-section factors, constant σ | σ̄_T ≈ 0.83 σ_T, σ̄_V ≈ 1.34 σ_V | — | arXiv:2011.04679 | Sect. IV.2 |
| Bullet simulation, σ/m = 2 cm²/g | ~20 kpc offset vs observed 25 ± 29 kpc | idealised SIDM | arXiv:1605.04307 | Sect. 5 |
| TNGC-SIDM main-cluster DM–BCG offset | up to ~20 kpc, persisting > 4 Gyr after first pericentre | σ_T/m = 1 cm²/g | arXiv:2610.18957 | abstract |
| DARKSKIES suite | 100 clusters, M₂₀₀ > 5 × 10¹⁴ M⊙; σ/m = 0, 0.01, 0.05, 0.1, 0.2 cm²/g | velocity-independent SIDM | arXiv:2509.19842 | abstract |
| Bullet Cluster | σ/m < 1.25 cm²/g (68%, offset); < 0.7 cm²/g (mass-to-light) | SIDM N-body of 1E 0657-56 | arXiv:0704.0261 | abstract |
| Equal-mass merger offsets | ≲ 20 kpc at 1 cm²/g | idealised 10¹⁵ M⊙ mergers | arXiv:1608.08630 | abstract |
| Offsets at current upper bounds | ≤ 10 kpc after first pericentre | velocity-dependent rare / frequent SIDM | arXiv:2310.07769 | abstract |
| Isothermal vs gravothermal cross sections | consistent at 1σ, isothermal ~3× larger | 9 isolated galaxies and BCGs | arXiv:2305.05067 | abstract |
| MACS J0138 collapse onset | 216 Gyr at 0.1 cm²/g; 22 Gyr at 1 cm²/g (estimate) | cluster-scale core growth | arXiv:2508.20179 | Sect. III.1, footnote 2 |
| Dwarf-scale cross sections | σ/m < 3 cm²/g (subhalo densities); CDM preferred above ~0.2 cm²/g (velocity-independent); > 5 cm²/g velocity-dependent motivated; 20–40 cm²/g in LSB dwarfs | MW satellites; LSB rotation curves | arXiv:2107.05967; arXiv:2503.13650; arXiv:2203.10104; arXiv:2407.15005 | abstracts |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Centroid estimator not matched to the observation.** Shows as offsets
  that change with the estimator as much as with σ/m. Test: measure
  simulated positions with the observational method (parametric fits to
  Σ or to shear), not shrinking circles [src: arXiv:1605.04307,
  Sects. 4.3, 5].
- **Misidentified peaks in single-band imaging.** Errors "do not
  necessarily average out" when a handful of substructures carry most of
  the weight [src: arXiv:1701.05877, abstract]. Test: list the weight of
  each system (Eq. 3) and audit the top ones against independent data
  [src: Sect. II].
- **A limit that needs negative cross sections.** If the likelihood peaks
  below zero, a limit without the physical prior is not a limit on
  physical models [src: arXiv:1701.05877, Sect. IV].
- **Wrong scattering regime for the drag model.** Isotropic, rare,
  large-momentum scattering produces mass loss rather than drag; the
  offset model assumes the drag case [src: arXiv:1503.07675,
  "Interpreting"]. Cross-check with simulations of the same angular
  dependence.
- **Merging or disturbed clusters in a Jeans or lensing-profile fit.** A
  merging simulated cluster could not be modelled and returned no
  meaningful parameters [src: arXiv:2012.06611, Sect. 3.5]; the
  quasi-steady-state assumption also fails for substructure that passed
  through the core or sits at turnaround [src: arXiv:1503.07675].
- **Age.** The rate equation fixes (σ/m)t₀; a mock bias towards σ/m > 1
  when the truth is 1 cm²/g is attributed to an underestimated age
  (mocks at z = 0, ages since half the BCG mass formed ~8–9 Gyr against
  the 5 Gyr assumed) [src: arXiv:2006.12515, Sect. IV.2]. Test: the age
  marginalisation of Eq. 17.
- **Stellar anisotropy assumed constant.** In the simulated clusters β(r)
  is neither constant nor within the assumed |β| < 0.3; dark matter has
  β ≈ 0 as the model assumes [src: arXiv:2006.12515, Sect. IV.2].
- **Line-of-sight elongation.** Raises apparent concentration and surface
  density; handled by the axis ratio s [src: arXiv:2012.06611,
  Sects. 5.10, 6.1]. One line of sight in the mocks overestimated the
  central dark-matter density by a factor of two [src: arXiv:2006.12515,
  Sect. IV.2].
- **Model outside its validated range.** The Jeans model was validated
  for σ/m ≥ 0.1 cm²/g; Andrade et al. "cannot rule out that systematic
  errors of order 0.1 cm²/g are introduced by the method", which is the
  size of their central value [src: arXiv:2012.06611, Sect. 6.3].
- **Ignoring the core-collapse branch.** Both Jeans papers keep only the
  core-growth solution [src: arXiv:2006.12515, Sect. II.1;
  arXiv:2012.06611, Sect. 6.1]; for clusters this is justified by halo
  shapes excluding σ/m ≳ 10 cm²/g [src: arXiv:2006.12515].
- **Proxy mismatch.** Quoting a σ_T limit for a model whose halo
  evolution is set by σ_V, or using ⟨σv⟩ where the transfer rates need
  ⟨σ_T v²⟩ or ⟨σ_V v³⟩ [src: arXiv:2011.04679, Sects. I, IV.2].
- **Halo shapes mis-modelled.** Ignoring the triaxial mass outside the
  scattering core and the scatter in axis ratios overstated shape limits
  by more than an order of magnitude [src: arXiv:1208.3026].
- **Gas physics missing from the comparison set.** Adiabatic zooms cannot
  rule out that cooling and feedback reconcile CDM with X-ray shapes [src:
  arXiv:2202.00038]; SIDM cores leave gas, stars and X-ray luminosities
  unchanged in BAHAMAS-SIDM [src: arXiv:1810.05649].
- **Method choice moves the cross section.** Isothermal fits prefer ~3×
  the gravothermal value [src: arXiv:2305.05067]; quote the method.
- **Under-resolved collapse.** Energy errors, kernel size and softening
  change collapse times [src: arXiv:2506.06269; arXiv:2610.28890]. Test:
  energy error well below 1%, softening below collisionless practice.
- **Sample selection for mergers.** A recent zoom-in study finds the
  offset of the main-cluster halo larger than that of the subcluster and
  concludes that "sample selection plays a key role", favouring double
  radio relic mergers [src: arXiv:2610.18957, abstract].

## Reading list
<!-- key: reading-list -->

- Method (mergers): Harvey et al. 2015, arXiv:1503.07675 — β statistic,
  drag model, error and gas-pull treatment.
- Critique: Wittman, Golovich & Dawson 2018, arXiv:1701.05877 — weight
  concentration, corrected offsets, physical prior.
- Critique (simulation): Robertson, Massey & Eke 2016, arXiv:1605.04307 —
  centroid methods, wake of scattered particles, Bullet limit.
- Method (profiles): Sagunski et al. 2020, arXiv:2006.12515 — Jeans model,
  core-growth test, AC, age marginalisation, mock validation.
- Application: Andrade et al. 2020, arXiv:2012.06611 — lensing surface
  densities, R₀ sampling, LOS axis ratio, systematic floor.
- Theory of the proxy: Colquhoun et al. 2020, arXiv:2011.04679 — σ_T, σ_V
  and the correct velocity weighting.
- Foundation: Kaplinghat, Tulin & Yu 2015, arXiv:1508.03339 — the
  velocity-dependent fit across scales (abstract only here).
- Simulations: Harvey et al. 2025, arXiv:2509.19842 (DARKSKIES); Lee et al.
  2026, arXiv:2610.18957 (TNGC-SIDM I) — current calibration suites.
- Review: Bechtol et al. 2022, arXiv:2203.07354 — place among halo probes.
- Foundation (Bullet): Randall et al. 2008, arXiv:0704.0261 — simulation-based offset and mass-to-light limits.
- Merger simulations, other teams: Kim, Peter & Wittman 2017, arXiv:1608.08630; Fischer et al. 2023, arXiv:2302.07882; Sabarish et al. 2023, arXiv:2310.07769.
- Other cluster routes: Peter et al. 2013, arXiv:1208.3026 (shapes); Robertson et al. 2019, arXiv:1810.05649 (BAHAMAS-SIDM lensing); Harvey et al. 2019, arXiv:1812.06981 (BCG wobbles); Shen et al. 2022, arXiv:2202.00038 (X-ray shapes); Tam et al. 2022, arXiv:2207.03506 (RAR); Adhikari et al. 2024, arXiv:2401.05788 (weak lensing); O'Donnell et al. 2025, arXiv:2508.20179 (lensing + kinematics).
- Method comparison: Yang et al. 2023, arXiv:2305.05067 — isothermal vs gravothermal.
- Galaxies and dwarfs: Zavala et al. 2013, arXiv:1211.6426; Kamada et al. 2017, arXiv:1611.02716; Creasey et al. 2017, arXiv:1612.03903; Ebisu et al. 2021, arXiv:2107.05967; Silverman et al. 2022, arXiv:2203.10104; Roberts et al. 2024, arXiv:2407.15005; Ando et al. 2025, arXiv:2503.13650.
- Gravothermal collapse: Turner et al. 2021, arXiv:2010.02924; Fischer, Yu & Dolag 2025, arXiv:2506.06269; van den Bosch & Tokayer 2026, arXiv:2610.28890; Dutra et al. 2024, arXiv:2406.17024 (cluster galaxy–galaxy lensing).

## Not verified
<!-- key: not-verified -->

- The Kaplinghat et al. 2016 Jeans model paper, the Sokolenko et al. 2018
  calibration and the Robertson et al. 2019 BAHAMAS-SIDM test were read
  only as described in arXiv:2012.06611.
- The Harvey et al. dynamical model behind Eq. S1 (its ref. 28, Eq. 33)
  was not read. The BCG-wobble limit of Harvey et al. 2019, quoted as
  σ/m < 0.39 cm²/g (95%) in arXiv:2012.06611 Sect. 6.3, is now read in
  its abstract (arXiv:1812.06981).
- The peers added on 2026-10-22 were read at abstract level, except
  O'Donnell et al. (Sects. I.2, III.1); their method sections, and the
  Outmezguine et al. collapse relation, were not read.
- Kaplinghat, Tulin & Yu 2015 has no body rendering available here; its
  ⟨σv⟩ definition was not read at source.
- DARKSKIES and TNGC-SIDM I were read at abstract level only.
- No observational merger-ensemble analysis newer than 2018 was read.
