# Galaxy properties versus web environment — cosmo-cosmic-web dossier

Scope: how an analysis of galaxy or halo properties against the cosmic
web separates the web from its confounders once the web exists: the
environment classes and distances, the matched, weighted and reshuffled
control samples, the group catalogue that fixes halo mass and central or
satellite status, the halo-mass-only null model, the significance
estimators, and what each choice has been found to change.
Snapshot: 2026-10-19.
From: Libeskind et al. 2018, Sect. 1.3 and 5.4; M. Einasto 2025, Sect. 9;
GAMA, SDSS and DESI environment papers.

Already in L2, not repeated here: the four families of environment
variable with their definitions (`physics-and-methods.md#environment-measures-for-haloes-and-galaxies`),
the headline trends (`results.md#haloes-and-galaxies-in-filaments-sheets-and`,
`results.md#void-galaxies`), the debate (`open-questions.md#does-the-web-affect-galaxies-beyond-halo-mass`)
and the confounding mechanism (`systematics.md#confounding-by-density-and-halo-mass`).
How the skeleton or T-web is built from galaxies, including the ⟨D_z⟩
normalisation of distances, is in `deep/web-classification.md`. Shuffling
tests of assembly bias in clustering are in `cosmo-galaxy-halo-connection`
(`deep/assembly-bias.md`).

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Define the environment of each galaxy
<!-- key: step-1-define-the-environment-of-each-galaxy -->

Two styles, which answer different questions.

**Continuous distances to skeleton features.** Malavasi et al. (2022,
arXiv:2109.14623) define three distances in TNG [src: Sect. 3.1]:

- d_fil, from the galaxy to the midpoint of the closest filament segment;
- d_CP, to the closest maximum or bifurcation, computed only for d_fil > 1
  Mpc (outside filament cores), to follow isotropic infall onto nodes;
- d_skel, along the closest filament from the galaxy's projection to the
  denser of its two end points, computed only for d_fil < 1 Mpc, to follow
  flow along filaments.

The 1 Mpc core is "roughly four times the best-fit scale radius" of the
generalised NFW filament profile of Galárraga-Espinosa et al. 2020, a
compromise between that radius and the 27 Mpc extreme extent; thresholds
of 0.25, 0.5, 1, 10 and 27 Mpc leave the conclusions unchanged
(arXiv:2109.14623) [src: Sect. 3.1].

**Discrete classes from distances.** The scheme used on SDSS DR18 groups,
after Galárraga-Espinosa et al. 2023 (Izzo Dominguez et al. 2025):
(arXiv:2509.09800) [src: Sect. 2]:

| Class | Definition |
|---|---|
| Clusters | within R_200 of a FoF halo with M ≥ 10¹³ h⁻¹M☉ |
| Cluster outskirts | R_200 to 3R_200 of such haloes |
| Filaments | within 1 h⁻¹Mpc of a DisPerSE filament axis |
| Filament outskirts | 1–2 h⁻¹Mpc from the axis |
| Others | the rest |

O'Kane et al. (2024, arXiv:2409.09028) use the same logic in projection:
filaments D_fil < 1 Mpc, filament outskirts 1–2.5 Mpc, field D_fil > 2.5
Mpc outside groups, clusters and their outskirts [src: Sect. 3.4.1–3.4.3].
The 1 Mpc radius rests on the literature value of a ~1 Mpc characteristic
filament radius; the outskirts class is a "buffer zone" that raises the
contrast between filament and field galaxies [src: Sect. 3.4.1, 3.4.2].

**Overlaps.** A galaxy can satisfy several criteria. O'Kane et al. assign
the denser class, with cluster outskirts ranked above filaments "to
account for backsplash galaxies" and groups above cluster outskirts to
keep infalling groups as groups [src: Sect. 3.5]. Izzo Dominguez et al.
measure distances from the central galaxy of each group, because centrals
sit near the potential minimum and are "less affected by redshift-space
distortions compared to satellites" [src: Sect. 3.1]. A pure distance-to-
critical-point selection cannot isolate environments, since a group close
to a maximum can also be close to a filament or a minimum [src: Sect.
3.1].

**Tidal anisotropy as a continuous class.** From the eigenvalues λ₁ ≤ λ₂
≤ λ₃ of the tidal tensor T_ij smoothed on R, the shear is q²_R ≡ I₁² −
3I₂ = ½[(λ₃ − λ₁)² + (λ₃ − λ₂)² + (λ₂ − λ₁)²], with I₁ and I₂ the first
two rotational invariants (Paranjape, Hahn & Sheth 2018,
arXiv:1706.09906, Eq. 9), and α_R ≡ (1 + δ_R)⁻¹ √(q²_R) (Eq. 10) [src:
Sect. 3.2]. The normalisation by (1 + δ_R) is there because q²_R of the
non-linear field is "quite strongly correlated" with δ_R, while for a
Gaussian field it is independent of the trace [src: Sect. 3.2]. With R =
4R_200b, haloes with α_R ≲ 0.2 (isotropic) and ≳ 0.5 (filament-like)
show opposite signs of the concentration–bias correlation at all masses
[src: abstract]. The SDSS variant α₅ with exponent n = 0.55 is in L2.

### Step 2. Fix stellar mass, local density and halo mass
<!-- key: step-2-fix-stellar-mass-local-density-and-halo -->

Four implementations are in use; they are not interchangeable.

1. **Nearest-neighbour matching without replacement.** For each pair of
   environments, each galaxy of the smaller class is paired with the
   closest-mass galaxy of the other if within 0.1 dex; for mass and
   density matching, among all galaxies within 0.1 dex in mass, the
   closest in local density, again within 0.1 dex (arXiv:2409.09028)
   [src: Sect. 4.1.3, 4.1.4]. The local density is Σ*₃ = M₃/πR₃², the
   stellar mass M₃ within the projected distance R₃ to the third nearest
   neighbour, chosen as mass rather than number density because number
   density "depends strongly on the selection of the sample" [src: Sect.
   3.2]. Galaxies whose R₃ circle crosses the region edge (787, 3.4%) are
   dropped [src: Sect. 3.2].
2. **Binned matching with repeated draws.** In ten equipopulated stellar
   mass bins, the smaller population is the reference and N_match = 20
   samples of the larger one are drawn with ΔM* < 0.1 dex, each galaxy used
   once per sample but repeatable across samples; for density matching,
   ten equipopulated bins of log(1 + δ) and ten repetitions, with pairs
   within 0.1 in the joint (log M*, log(1 + δ)) space (Kraljic et al.
   2018, arXiv:1710.02676) [src: App. A.1, A.2]. Varying N_match, ΔM* and
   the number of bins "does not alter our conclusions" [src: App. A.1].
3. **Weighting to a common halo-mass distribution.** Each GAMA central is
   weighted, per web class, so that the weighted halo-mass distribution of
   every class equals that of the full sample (Tojeiro et al. 2017,
   arXiv:1612.08595) [src: Sect. 4.2]. The authors call the scheme "poor
   in terms of shot noise", since rare cells such as high-mass haloes in
   voids are strongly up-weighted [src: Sect. 4.2].
4. **Reshuffling within density bins.** Permute the galaxy property among
   galaxies of the same density bin and recompute the trend against
   distance: the property–density relation survives, the property–
   distance relation is destroyed. Kraljic et al. use ten equipopulated
   bins of 1 + δ = n/n(z), with n in a Gaussian kernel, and five
   reshuffled samples; for colours, ten mass bins inside each density bin
   [src: Sect. 6]. Malavasi et al. shuffle 1000 times within DTFE density
   bins, keeping d_CP, d_fil, d_skel fixed [src: Sect. 4.4 of
   arXiv:2109.14623].

### Step 3. Choose the scale of the density that is held fixed
<!-- key: step-3-choose-the-scale-of-the-density-that-is -->

The conclusion depends on it. Kraljic et al. compute the density at 8 Mpc,
"the 'smallest' scale at which the effect of the anisotropic large-scale
tides can be detected", so as to average out binary interactions, mergers
and outflows (arXiv:1710.02676) [src: Sect. 6]. In Horizon-AGN,
reshuffling on the DTFE density leaves the mass and sSFR gradients
"almost unchanged", whereas a Gaussian density at ~5 Mpc (~1.5 times the
mean inter-galaxy separation) cancels them [src: App. D.2]. O'Kane et al.
hold fixed a third-nearest-neighbour density with R₃ ~ 1 Mpc on average
[src: Sect. 3.2 of arXiv:2409.09028]. A "fixed local density" test with a
1 Mpc density and one with a 5–8 Mpc density are therefore different
tests: the first removes small-scale processes, the second removes the
large-scale density field that the web itself is made of.

### Step 4. Fix halo mass and central or satellite status
<!-- key: step-4-fix-halo-mass-and-central-or-satellite -->

- **From a group catalogue.** GAMA: friends-of-friends groups (G3Cv06),
  central = brightest group galaxy, halo mass M_h = M_p (L_B/L₀)^α from
  total corrected group luminosity, with (log M_p, L₀, α) = (13.40 ±
  0.12, 2 × 10¹¹ h² L☉, 1.09 ± 0.22) fitted to weak-lensing masses and an
  M_p–α correlation of −0.13 (arXiv:1612.08595) [src: Sect. 4.1.1]. SDSS
  DR18: FoF plus an iterative halo-based refinement with abundance
  matching of group luminosity; central = brightest member; groups with at
  least one spectroscopic member (arXiv:2509.09800) [src: Sect. 1.2].
- **Propagating the halo-mass calibration.** Tojeiro et al. redraw (M_p,
  α) 100 times from their correlated errors, shift the halo-mass bin
  edges by the change in mean so that bin populations stay fixed, and
  repeat the full analysis [src: Sect. 4.4.3 of arXiv:1612.08595].
- **From the history, in simulations.** In TNG50, only galaxies that stay
  centrals throughout (satellite defined as non-central in a halo of
  log M_halo ≥ 10 for at least two consecutive snapshots) are kept, which
  removes ~65% of low-mass z = 0 galaxies; of 7342, 431 field-to-filament
  and 2147 field galaxies remain (Zakharova et al. 2026, arXiv:2605.23457)
  [src: Sect. 2.2]. Filament infall time is the first crossing of 1
  h⁻¹Mpc from a spine, distances being medians over ten DisPerSE runs on
  85% subsamples at 5σ persistence [src: Sect. 2.2].

### Step 5. Build the halo-mass-only null model
<!-- key: step-5-build-the-halo-mass-only-null-model -->

Alam et al. (2019, arXiv:1801.04878) populate Bolshoi haloes (ROCKSTAR, z
= 0.1, 250 h⁻¹Mpc box) with an iHOD in which stellar mass depends only on
halo mass (a mean stellar-to-halo relation with mass-dependent log-normal
scatter, satellites from a conditional stellar mass function, NFW
positions) and colours ranked at fixed M* by halo mass only [src: Sect.
2.2]. The mock and the data go through the same T-web pipeline, and any
difference measures web dependence beyond the halo mass function. Two
practical choices [src: Sect. 4.1]:

- Split by quantiles, not fixed bin edges, to absorb small differences
  between the δ₈ and α₅ distributions of data and mock.
- To split by α₅ independently of δ₈, take α₅ quantiles at each ten
  percentile of δ₈ and combine them.

Result (arXiv:1801.04878): the red fraction rises from ~68% at low δ₈ to ~78% at high δ₈,
shows little change with α₅ at fixed δ₈, and the halo-quenching mock
tracks the colour-split stellar mass functions in all nine (δ₈, α₅)
cells [src: Sect. 4.2].

### Step 6. Estimate errors and significance
<!-- key: step-6-estimate-errors-and-significance -->

| Statistic | Error | Analysis | Place read |
|---|---|---|---|
| Median distance to filament per mass bin | half width at half maximum of the Gaussian fitted to 100 bootstrap medians | GAMA (arXiv:1710.02676) | Table 1 notes |
| Difference between two PDFs | residual Δ₁₋₂/√(σ₁² + σ₂²) per bin | GAMA (arXiv:1710.02676) | Sect. 4.2.1 |
| Original against reshuffled trend | (H_O − H_R)/√(σ_O² + σ_R²) | TNG (arXiv:2109.14623) | Sect. 4.4 |
| Distribution of ΔSFMS or T-type between matched samples | Kolmogorov–Smirnov p, significant at p < 0.05, highly at p < 0.01 | SDSS (arXiv:2409.09028) | Fig. 7 caption |
| Medians across four web classes at fixed halo mass | Kruskal–Wallis test, p < 0.05, plus a monotonicity count over 100 calibration draws | GAMA (arXiv:1612.08595) | Sect. 4.4.3 |
| w_p and colour-split stellar mass functions | 200 jackknife regions (data), 100 (mock) | SDSS (arXiv:1801.04878) | Sect. 4.1, 4.2 |
| HOD per environment | 100 jackknife subsamples, stable for ≥ 50 | SDSS DR18 (arXiv:2509.09800) | Sect. 3.1 |
| Red fraction per T-web class | 1σ binomial | DESI DR1 (arXiv:2604.02463) | Fig. 5–7 captions |

ΔSFMS in the O'Kane et al. analysis is the vertical logarithmic distance
to a main sequence log SFR = 0.7 log(M*/M☉) + b with b = −7; blue cloud
ΔSFMS > −0.52, red sequence < −1.02 [src: Sect. 3.1 of arXiv:2409.09028].
The DESI DR1 red/blue split is a mass-dependent Otsu threshold on g − r,
k* = argmax_k σ²_bc(k) with σ²_bc = w(1 − w)(μ_B − μ_R)² (arXiv:2604.02463,
Eqs. 12–13), recomputed in each redshift and stellar-mass bin [src: Sect.
3.3].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Matching, weighting or reshuffling
<!-- key: matching-weighting-or-reshuffling -->

Matching discards galaxies but keeps them unweighted; weighting keeps all
galaxies at the cost of shot noise in rare cells (arXiv:1612.08595) [src:
Sect. 4.2]. Reshuffling does not discard anything and tests a specific
null (the property depends on density only), but its answer is set by
the density scale (Step 3). The outcomes on comparable questions:

- SDSS filaments against field: differences at fixed stellar mass,
  none at fixed stellar mass and Σ*₃; differences remain only against
  cluster interiors (arXiv:2409.09028) [src: Sect. 4.1.4].
- GAMA gradients towards filaments: the mass-gradient deviation between
  the extreme mass bins exceeds 3σ before reshuffling and is ~1σ after;
  the colour gradient "is similarly nearly cancelled out" (arXiv:1710.02676)
  [src: Sect. 6]. With galaxies within 3.5 Mpc of nodes removed, the
  reshuffling cancels the mass gradients towards filaments [src: Fig. 15
  caption].
- TNG: mass- and SFR-related distributions "do not change visibly" after
  reshuffling, so their trends cannot be separated from density, while the
  fraction of spins perpendicular to filaments does change, at small d_CP
  outside filaments (arXiv:2109.14623) [src: Sect. 4.4].

So the GAMA colour gradient, which L2 lists at fixed stellar mass, does
not survive the authors' own large-scale density reshuffling at the
quoted significance; quote it with that test.

### Projected or 3D distances
<!-- key: projected-or-3d-distances -->

O'Kane et al. run DisPerSE on 2D slices of Δz = 0.02 (~5600 km s⁻¹) and
use projected distances [src: Sect. 3.3, 2.1 of arXiv:2409.09028]; the
small-angle approximation they use for distances costs at most ~8% over
~100 Mpc [src: Sect. 3.4.1, footnote 3]. They chose a persistence of 2.5
to keep "the strongest, most significant filaments", the effect of
filaments being expected to be subtle, and five smoothing passes, "largely
an aesthetic choice" [src: Sect. 3.3]. 3D analyses (GAMA, TNG) avoid
projection but inherit fingers of God; their treatment is in
`deep/web-classification.md`.

### Filament radius for membership
<!-- key: filament-radius-for-membership -->

1 Mpc is the common choice in data (arXiv:2409.09028, arXiv:2509.09800)
and simulations (arXiv:2109.14623; 1 h⁻¹Mpc in arXiv:2605.23457). Tests:
0.25–27 Mpc (arXiv:2109.14623) [src: Sect. 3.1]; 0.5 and 2 h⁻¹Mpc in the
TNG50 infall analysis, "stable against these choices" (arXiv:2605.23457)
[src: Sect. 2.2].

### Skeleton settings
<!-- key: skeleton-settings -->

On SDSS DR18 (z < 0.1), the number of filament vertices falls from 47,978
(3σ, no smoothing) to 3558 (5σ, two smoothings); across the six
combinations the HOD in filaments, outskirts and other regions stays close
to the global one (arXiv:2509.09800) [src: Sect. 3.4, Table 2]. The
authors conclude that large-scale environments "only weakly influence the
HOD" [src: abstract].

### Tracer density over time (simulations)
<!-- key: tracer-density-over-time-simulations -->

For histories, the tracer number is held fixed across snapshots (log M* >
8 at z = 4, ≳ 9 at z = 0) because more tracers yield more filaments and a
galaxy could otherwise "appear to enter a filament simply because that
filament was not detected at previous snapshots" (arXiv:2605.23457) [src:
Sect. 2.2].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Filament core for d_CP and d_skel | 1 Mpc (≈ 4× gNFW scale radius) | TNG | arXiv:2109.14623 | Sect. 3.1 |
| Filament and outskirts radii | < 1 Mpc; 1–2.5 Mpc (projected) | SDSS | arXiv:2409.09028 | Sect. 3.4 |
| Cluster classes | R_200 and 3R_200 of M ≥ 10¹³ h⁻¹M☉ haloes | SDSS DR18 | arXiv:2509.09800 | Sect. 2 |
| Mass matching tolerance | 0.1 dex (pairwise or binned) | SDSS, GAMA | arXiv:2409.09028; arXiv:1710.02676 | Sect. 4.1.3; App. A.1 |
| Matched samples drawn | 20 (mass), 10 (density) | GAMA | arXiv:1710.02676 | App. A.1, A.2 |
| Density scale for reshuffling | 8 Mpc (GAMA); ~5 Mpc (Horizon-AGN) | GAMA, Horizon-AGN | arXiv:1710.02676 | Sect. 6, App. D.2 |
| Node exclusion | 3.5 Mpc | GAMA | arXiv:1710.02676 | Fig. 15 caption |
| Local density | Σ*₃, R₃ ~ 1 Mpc | SDSS | arXiv:2409.09028 | Sect. 3.2 |
| Tidal anisotropy scale | R = 4R_200b; α ≲ 0.2 isotropic, ≳ 0.5 filament-like | N-body | arXiv:1706.09906 | abstract |
| Group mass calibration | log M_p = 13.40 ± 0.12, α = 1.09 ± 0.22 | GAMA + lensing | arXiv:1612.08595 | Sect. 4.1.1 |
| T-web for GAMA groups | 4 h⁻¹Mpc smoothing, λ_th = 0.4 (alternative 10 h⁻¹Mpc, 0.1) | GAMA | arXiv:1612.08595 | Sect. 4.2 |
| Centrals-only cut | removes ~65% of low-mass galaxies | TNG50 | arXiv:2605.23457 | Sect. 2.2 |
| Red fraction vs δ₈ | ~68% to ~78% | SDSS | arXiv:1801.04878 | Sect. 4.2 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Density held fixed at the wrong scale.** A trend that survives at
  fixed 1 Mpc density can vanish at fixed 5–8 Mpc density and vice versa
  (arXiv:1710.02676) [src: Sect. 6, App. D.2]. Test: repeat the matching
  or reshuffling at two scales and report both.
- **Nodes masquerading as filaments.** Galaxies near nodes carry most of
  the mass gradient; removing those within 3.5 Mpc changes the result of
  the reshuffling test (arXiv:1710.02676) [src: Fig. 15 caption].
  Test: exclude a node radius, or use d_CP and d_skel separately
  (arXiv:2109.14623) [src: Sect. 3.1].
- **Satellites and backsplash in the field sample.** A field or filament
  sample with satellites mixes group pre-processing with the web; rank
  cluster outskirts above filaments (arXiv:2409.09028) [src: Sect. 3.5]
  or keep lifelong centrals (arXiv:2605.23457) [src: Sect. 2.2]. Effects
  of massive haloes reach 2–3 R_vir, beyond the satellite cut [src:
  Sect. 4.4 of arXiv:2605.23457].
- **Halo mass known only through a calibration.** Test: propagate the
  lensing calibration by Monte Carlo and count how often the trend
  survives (arXiv:1612.08595) [src: Sect. 4.4.3]. The detected GAMA
  signal at fixed halo mass is in M_s/M_h with photometric stellar
  masses; spectroscopic M_s/M_h and mass-weighted ages lack the
  statistics [src: Sect. 4.4.3].
- **Underestimated errors.** Binomial errors on red fractions per class
  (arXiv:2604.02463) [src: Fig. 5–7 captions] ignore cosmic variance;
  jackknife regions do not (arXiv:1801.04878, arXiv:2509.09800) [src].
  Ask for jackknife errors before reading a difference of a few per cent
  between classes.
- **Edge galaxies.** Nearest-neighbour densities are biased low at survey
  or slice edges; drop the galaxies whose R₃ crosses the boundary
  (arXiv:2409.09028) [src: Sect. 3.2].
- **Distribution mismatch between data and mock.** Fixed bin edges in δ₈
  or α₅ compare different populations if the mock distributions differ
  slightly; use quantiles (arXiv:1801.04878) [src: Sect. 4.1].
- **Tracer number varying with time in histories.** Spurious infall
  times; hold the tracer number fixed (arXiv:2605.23457) [src: Sect.
  2.2].

## Reading list
<!-- key: reading-list -->

- Method: Kraljic et al. 2018, arXiv:1710.02676 — binned matching,
  density reshuffling and its scale, node exclusion, bootstrap medians
  (Sect. 4.2, 6; App. A, D.2).
- Method: O'Kane et al. 2024, arXiv:2409.09028 — pairwise mass and
  density matching, Σ*₃, class hierarchy, KS tests (Sect. 3, 4.1).
- Method: Malavasi et al. 2022, arXiv:2109.14623 — d_fil, d_CP, d_skel
  and 1000-fold reshuffling in TNG (Sect. 3.1, 4.4).
- Foundation: Paranjape et al. 2018, arXiv:1706.09906 — q²_R and α_R
  (Sect. 3.2, Eqs. 9–10).
- Method: Alam et al. 2019, arXiv:1801.04878 — iHOD halo-mass-only null
  model, quantile splits, jackknife errors (Sect. 2.2, 4).
- Application: Tojeiro et al. 2017, arXiv:1612.08595 — group halo masses,
  halo-mass weighting, Kruskal–Wallis tests under calibration draws
  (Sect. 4.1–4.4).
- Application: Izzo Dominguez et al. 2025, arXiv:2509.09800 — five-class
  scheme on SDSS DR18 groups, HOD per environment, skeleton-setting tests.
- Application: Zakharova et al. 2026, arXiv:2605.23457 — lifelong
  centrals, infall times, fixed tracer number (Sect. 2.2, 4.4).
- Application: Ullah et al. 2026, arXiv:2604.02463 — mass-dependent Otsu
  colour split per redshift bin on DESI DR1 (Sect. 3.3).

## Not verified
<!-- key: not-verified -->

- The Galárraga-Espinosa et al. 2023 environment-classification paper and
  the Eardley et al. 2015 GAMA T-web paper were not read; they enter only
  as cited by arXiv:2509.09800 and arXiv:1612.08595.
- The quantitative HOD ratios per environment and colour in
  arXiv:2509.09800 (Sect. 3.2–3.3) were not read.
- The Zu & Mandelbaum iHOD papers behind the null model of
  arXiv:1801.04878 were not read.
- How DESI DR1 group catalogues have been combined with web classes was
  not searched.
