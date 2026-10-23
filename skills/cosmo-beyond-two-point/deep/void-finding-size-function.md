# Void finding and the void size function — cosmo-beyond-two-point dossier

Scope: how a void size function (VSF) measurement is turned into a
cosmological constraint (finder output, cleaning, radius cut, model with its
threshold, bias, redshift-space and Alcock–Paczynski corrections, likelihood,
calibration), and how to choose between the calibrated, free-threshold,
finder-built-for-the-model and simulation-based (emulator, implicit
likelihood, HOD forward model) routes, with the other finders and teams at
each step.
Snapshot: 2026-10-22.
From: Cai & Neyrinck 2025 review (arXiv:2503.22532), Sect. 3 (distribution
function of voids; finding voids); Beyond-2pt challenge (arXiv:2405.02252),
Sect. V.7 (void size function).

Already in L2, not repeated here: the list of finders and the Colberg et al.
comparison (`physics-and-methods.md#void-finders`); the Sheth–van de Weygaert
and Jennings et al. models in one paragraph
(`physics-and-methods.md#void-size-function-vsf`); the headline BOSS DR12 and
DR16 values (`results.md#void-size-function`); spurious voids
(`systematics.md#spurious-poisson-voids`); the Beyond-2pt light-cone outcome
(`surveys-and-data.md#the-beyond-2pt-challenge`); Euclid forecasts
(`open-questions.md#forecasts-all-forecast`).

## How it is done
<!-- key: how-it-is-done -->

The backbone below is the procedure of the BOSS DR12 analysis (Contarini et
al. 2023, arXiv:2212.03873), which the Euclid forecast (arXiv:2205.11525) and
the Beyond-2pt void entry (arXiv:2405.02252, Sect. V.7) share, built on the
void tools of the CosmoBolognaLib (Ronconi & Marulli 2017, arXiv:1703.07848,
designed to be independent of the void finder [src]). Each step then lists
what other teams do. Notation follows
arXiv:2212.03873: superscript L for linear and NL for non-linear density
contrasts, subscript "tr" for the tracer field and "DM" for the matter field.

### Step 1. Find voids
<!-- key: step-1-find-voids -->

The analyses run VIDE, a ZOBOV-based watershed finder: a Voronoi tessellation
of the tracers gives a density per cell, local minima are found, and cells are
merged into basins separated by overdense ridges [src: arXiv:2212.03873,
Sect. III.1]. Each void gets a volume-weighted centre and an effective radius,

  X = Σ_i x_i V_i / Σ_i V_i,  R_eff = [(3/4π) Σ_i V_i]^{1/3}
  (arXiv:2212.03873, Eq. 8),

with x_i the position of the i-th tracer of the void and V_i its Voronoi-cell
volume. Galaxy coordinates are computed with a fiducial cosmology, so R_eff,
volumes and densities depend on it [src: arXiv:2405.02252, Sect. V.7.1]. On a
light cone VIDE needs a footprint mask; the Beyond-2pt team built a HEALPix
mask at n_side = 128 from the mock galaxy positions [src: same]. In BOSS DR12,
galaxies at z > 0.65 were dropped because their density is very low and voids
there are exposed to the survey boundary [src: arXiv:2212.03873, Sect. III.1].

Song et al. 2025 (BOSS DR16) also run VIDE but use the unmerged low-density
zones "for avoiding the void-in-void issue", and add an ellipticity
ε_v = 1 − (I_min/I_max)^{1/4} from the eigenvalues of the inertia tensor of the
member tracers (arXiv:2501.07817, Eqs. 3–4) [src: Sect. 2.2].

Other finders in use for the VSF, one line each:

- **VIDE on simulations.** GIGANTES runs VIDE on the Quijote halo catalogues:
  over 10⁹ voids for thousands of cosmological models (arXiv:2107.02304)
  [src]; Lehman et al. 2025 use VIDE on Quijote halos for their emulators,
  voids being basins bounded by density maxima of the Voronoi field
  (arXiv:2502.05262) [src: Sect. 2.3]. Salcedo et al. 2025 keep the original
  VIDE merging rule, zones joined only if their boundary density is below
  0.2 times the mean tracer density, to stay sensitive to the galaxy–halo
  connection in intra-void filaments (arXiv:2504.08221) [src: Sect. II.3].
- **VIDE on BOSS with implicit likelihood.** Thiele et al. 2023 keep VIDE
  because earlier work found shape-agnostic finders constrain Σm_ν better
  than spherical ones (arXiv:2307.07555) [src: Sect. III.1].
- **Spherical finder.** Bayer et al. 2021 use a spherical void finder on
  Quijote, and suggest another finder might extract more information
  (arXiv:2102.05049) [src: Sects. IV.3, VI].
- **Watershed without spherical shape plus an ellipticity cut**, CSST
  forecast on a Jiutian semi-analytic mock (Song et al. 2024,
  arXiv:2402.05492) [src], the route later applied to DR16 above.
- **Grid-based finder on DESI.** AVISM runs on a regular grid with a survey
  mask, on DESI DR1 BGS and LRG data first corrected for redshift-space
  distortions and with the velocity field reconstructed, in two
  1400³ cMpc³ cubes (Monllor-Berbegal et al. 2026, arXiv:2610.18348) [src:
  abstract, Sect. 2.3].
- **Delaunay against Voronoi.** DIVE (Delaunay: voids from empty
  circumspheres) and VIDE (Voronoi) are both tessellation-based; small
  changes in tracer positions or density rearrange the tessellation and add
  scatter to the VSF, which Liu et al. 2026 reduce by subsampling and
  averaging (arXiv:2606.21864) [src: Sects. I–II]. Their list of families:
  Delaunay-based WVF, DIVE, Delfin++; Voronoi-based ZOBOV, VIDE, REVOLVER,
  VAST, VEGA [src: Sect. I].

### Step 2. Clean the catalogue to match the model's definition of a void
<!-- key: step-2-clean-the-catalogue-to-match-the-model-s -->

The excursion-set model counts spherical, non-overlapping regions that enclose
a fixed density contrast; a watershed void is neither. The calibrated route
therefore changes the catalogue rather than the model, with the cleaning code
of Ronconi & Marulli, which has one free setting, the threshold δ_v,tr^NL in the
tracer field [src: arXiv:2212.03873, Sect. III.2]:

1. Reject a void if a sphere of radius R_central = 2 MGS(z) around its VIDE
   centre does not reach δ_v,tr(R_central) < −0.7. MGS(z) = n_gal(z)^{−1/3} is
   the mean galaxy separation [src: arXiv:2212.03873, Sect. III.2].
2. Rescale each surviving void to the radius R at which the enclosed tracer
   density contrast equals δ_v,tr^NL.
3. Remove overlapping voids one by one, rejecting the one with the higher
   central density.

The authors' reason for the step: it yields "a sample of voids ideally free of
spurious Poissonian fluctuations and shaped in agreement with the theoretical
definition" [src: Sect. III.2]. The galaxy density used in the rescaling is a
spline fit to n_gal(z) [src: same].

What the cleaning removes, Euclid Flagship light cone (redshift space,
0.95 < z < 1.70): VIDE finds 33 828 voids above f_cut MGS, and 2 054 remain
after cleaning [src: arXiv:2205.11525, Table 1].
The authors expect the sharp fall, since cleaning keeps the largest and
deepest underdensities and shrinks them, which pushes many below the radius
cut [src: Sect. 2.2].

Routes without cleaning. Simulation-based analyses model the voids exactly
as the finder returns them: Salcedo et al. note that a forward model can
take "any void finder" (arXiv:2504.08221) [src: Sect. II.3]; Lehman et al.
argue that analytic models describe only a subset of watershed voids, while
emulators of the uncleaned statistics retain more information
(arXiv:2502.05262) [src]. The free-threshold route (Song et al.) selects by
ellipticity instead of cleaning (Step 1). Liu et al. report 20–40% gains in
constraining power from stabilising the tessellation, a different fix for
catalogue noise (arXiv:2606.21864) [src: Sect. I].

### Step 3. Choose the threshold
<!-- key: step-3-choose-the-threshold -->

All three analyses of this family take δ_v,tr^NL = −0.7 [src: arXiv:2212.03873,
Sect. III.2; arXiv:2205.11525, Sect. 2.2; arXiv:2405.02252, Sect. V.7.2]. The
stated trade-off: a more negative threshold gives voids freer of Poisson
contamination and a stronger cosmological dependence, but fewer voids, fewer
tracers per void and a noisier rescaled radius; a less negative one gives
larger voids, more of which overlap and are discarded, and more shallow,
possibly spurious ones [src: arXiv:2205.11525, Sect. 2.2; arXiv:2405.02252,
Sect. V.7.2]. The Euclid analysis repeated everything with −0.6 and found
consistent results [src: arXiv:2205.11525, Sect. 2.2]. The model must be
evaluated with the same threshold as the cleaning [src: same].
Elsewhere: in the CSST forecast the fitted linear thresholds run from about
−0.4 to −0.1 between z = 0.5 and 1.1, far from the δ_v ≃ −2.7 of spherical
evolution with particle tracers (arXiv:2402.05492) [src]; the DESI DR1
AVISM catalogue is compared with the SvdW + Vdn model at δ_V^L = −0.55
(arXiv:2610.18348) [src: Sect. 4.2, Fig. 4].

### Step 4. Cut small radii
<!-- key: step-4-cut-small-radii -->

Sparse tracers lose small voids, and the loss is not modelled, so the radius
range affected by incompleteness is excluded [src: arXiv:2205.11525, Sect. 2.2;
arXiv:2405.02252, Sect. V.7.4, Caveats]. The cut is set in units of MGS:

| Analysis | Cut | Resulting minimum radius | Place read |
|---|---|---|---|
| BOSS DR12 | 2.5 MGS at the mean redshift of each bin; one cut applied to both bins | 36.37 and 35.13 h⁻¹Mpc; ≈ 35 h⁻¹Mpc used | arXiv:2212.03873, Sect. III.4, App. C.3 |
| Euclid Flagship | f_cut(z) MGS, f_cut from 2.30 (lowest bin) to 2.00 (highest), chosen from the drop of counts and the departure from the model | MGS 10.28–14.45 h⁻¹Mpc | arXiv:2205.11525, Sect. 2.2, Table 1 |
| Beyond-2pt light cone | fixed R̃_min = 33 h⁻¹Mpc in three redshift bins | 6, 7, 6 non-empty radius bins | arXiv:2405.02252, Sect. V.7.4 |
| BOSS DR16 (free threshold) | ≈ 2.5 MGS, and bins with fewer than 5 voids dropped | 40 and 45 h⁻¹Mpc in the two bins | arXiv:2501.07817, Sect. 3 |

| BOSS CMASS NGC, implicit likelihood | 32 linear bins over 30–80 h⁻¹Mpc, "well above the mean tracer separation"; two z bins split at z = 0.53 | 30 h⁻¹Mpc | arXiv:2307.07555, Sect. III.1 |
| Quijote, spherical finder (Fisher) | 15 linear bins, set by convergence of the derivatives | 10.4–29.9 h⁻¹Mpc | arXiv:2102.05049, Sect. IV.3 |

The Euclid analysis also removed voids whose centre lies within 30 h⁻¹Mpc of
the footprint edge and corrected the model for the selected volume [src:
arXiv:2205.11525, Sect. 2.2].

### Step 5. Predict the counts
<!-- key: step-5-predict-the-counts -->

The multiplicity function of the two-barrier excursion set (Sheth & van de
Weygaert) is

  f_lnσ(σ) = 2 Σ_{j≥1} exp[−(jπx)²/2] jπ x² sin(jπ𝒟),
  𝒟 = |δ_v^L| / (δ_c^L + |δ_v^L|),  x = 𝒟 σ / |δ_v^L|
  (arXiv:2212.03873, Eqs. 1–2),

where σ is the rms of the linear matter field on the Lagrangian scale R_L,
δ_v^L the linear void-formation threshold and δ_c^L the linear collapse
threshold. δ_c^L lies between 1.06 and 1.686 and only changes the number of
very small voids, which the cut removes [src: arXiv:2212.03873, Sect. II.1,
footnote to Eq. 2]. The
volume-conserving (Vdn) model of Jennings et al. gives the counts per unit
log radius,

  dn/dln R = [f_lnσ(σ)/V(R)] dln σ⁻¹/dln R_L |_{R_L = R_L(R)}
  (arXiv:2212.03873, Eq. 3; the same form is arXiv:2405.02252, Eq. 36).

The non-linear threshold maps to the linear one by Bernardeau's fit,
δ_v^L = 𝒞[1 − (1 + δ_v^NL)^{−1/𝒞}], 𝒞 = 1.594 (arXiv:2212.03873, Eq. 4); the
Euclid paper states that this conversion is cosmology and redshift
independent to high accuracy for ΛCDM and the dark-energy models it tests
[src: arXiv:2205.11525, Sect. 3.2]. The Vdn model reproduces voids in the
matter field only if they are non-overlapping spheres enclosing δ_v,DM^NL
[src: arXiv:2212.03873, Sect. II.1].

Predicting the counts without the excursion set: Lehman et al. emulate the
VSF and void profiles with neural networks trained on Quijote (arXiv:2502.05262)
[src]; Thiele et al. populate approximate gravity-only simulations with
massive-neutrino particles with an 11-parameter HOD and use implicit
likelihood inference, rejecting an emulator plus Gaussian likelihood
because a 17-dimensional emulator is hard to build and the VSF is not
Gaussian (arXiv:2307.07555) [src: Sect. I]; Salcedo et al. model the VSF on a
grid of N-body simulations with an HOD including central and satellite
assembly bias (arXiv:2504.08221) [src]. In that route the tracer bias of
Step 6 is replaced by the HOD: raising σ_log M or lowering M_min puts
centrals in low-mass haloes in underdense regions, which fracture large
voids into smaller ones (arXiv:2504.08221) [src: Sect. III.1].

### Step 6. Map the tracer threshold to the matter threshold
<!-- key: step-6-map-the-tracer-threshold-to-the-matter -->

Voids in biased tracers have deeper profiles, so at fixed enclosed contrast
their radius is larger [src: arXiv:2212.03873, Sect. II.2]. The extended Vdn
model sets

  δ_v,DM^NL = δ_v,tr^NL / ℱ,  ℱ(b_eff) = B_slope b_eff(z) + B_offset
  (arXiv:2212.03873, Eq. 6; arXiv:2205.11525, Eqs. 7, 9),

with b_eff the large-scale effective bias of the tracers. Because b_eff from
the two-point function is degenerate with σ8, the BOSS analysis rewrites it
as ℱ(b_eff σ8) = C_slope b_eff(z) σ8(z) + C_offset (Eq. 7), so that the input
is the product b_eff σ8, which the 2PCF measures directly [src: Sect. II.2].
The same linear function is used to absorb the redshift-space enlargement of
voids [src: same; arXiv:2205.11525, Sect. 4.1]. Its physical content, as the
Euclid paper puts it: ℱ is the tracer bias measured inside voids (b_punct in
earlier work) [src: arXiv:2205.11525, Sect. 3.2, footnote 6].

### Step 7. Correct the radius for the fiducial cosmology
<!-- key: step-7-correct-the-radius-for-the-fiducial -->

With q_∥ = H*(z)/H(z) and q_⊥ = D_A(z)/D_A*(z), the asterisk denoting the
fiducial cosmology and D_A the comoving angular-diameter distance, the radius
of the sphere with the volume of the distorted void is R = q_∥^{1/3} q_⊥^{2/3} R*
(arXiv:2212.03873, Eq. 5 and text; arXiv:2405.02252, Eq. 39). The correction
shifts the predicted counts to smaller or larger radii [src: arXiv:2212.03873,
Sect. II.1]. The predicted density is turned into counts with the effective
volume, computed as the sum of all Voronoi cells, which accounts for voids
removed at the survey boundary [src: Sect. III.1].

### Step 8. Fit
<!-- key: step-8-fit -->

The BOSS likelihood is a product of Poisson terms over radius bins i and
redshift bins j,
L = Π_{i,j} N(r_i, z_j|Θ)^{N(r_i,z_j|D)} exp[−N(r_i,z_j|Θ)] / N(r_i,z_j|D)!
(arXiv:2212.03873, Eq. 9). Wide uniform priors are put on Ω_m and σ8 (ΛCDM)
or Ω_m and w (wCDM); h, Ω_b h², n_s and τ get uniform priors centred on the
Patchy cosmology, ten times the Planck 2018 68% width [src: Sect. III.3]. The
power spectrum comes from the Eisenstein–Hu transfer-function approximation,
and the pipeline is CosmoBolognaLib [src: same]. The BOSS sample has 3 280
VIDE voids above 30 h⁻¹Mpc, against 5 111.85 on average in the Patchy mocks
[src: Sect. III.1], in two redshift bins (0.2 < z ≤ 0.45, 0.45 < z < 0.65)
holding three and four independent radius bins on the data [src: Sect. IV.1].
Thiele et al. test the Poisson assumption directly and find the VSF "very
close to Poisson distributed (as long as bins are chosen wide enough)"
(arXiv:2307.07555) [src: Sect. I]; Song et al. use a Gaussian χ²
instead (Choices below).

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Calibrated (fixed or relaxed) against marginalised nuisance
<!-- key: calibrated-fixed-or-relaxed-against -->

The BOSS analysis calibrates (C_slope, C_offset) on the median counts of 100
Patchy mocks, with b_eff σ8 from each mock's 2PCF as a Gaussian prior and the
Patchy cosmology fixed [src: arXiv:2212.03873, Sect. III.4]. It then runs two
versions on the data [src: arXiv:2212.03873, Sect. III.4, Table 1]:

| Version | What is assumed | Ω_m (ΛCDM) | σ8 (ΛCDM) | w (wCDM) |
|---|---|---|---|---|
| Fixed calibration | (C_slope, C_offset) = (−1.62, 4.30), no uncertainty: "volume-unlimited" mocks that reproduce the data perfectly | 0.293 +0.067/−0.059 | 0.839 +0.055/−0.058 | −0.97 +0.15/−0.16 |
| Relaxed calibration | the full mock posterior of (C_slope, C_offset) as prior | 0.285 +0.063/−0.057 | 0.793 +0.090/−0.076 | −1.11 ± 0.24 |

Relaxing the calibration loosens σ8 and w, not Ω_m [src: Sect. IV.2]. The two
calibration coefficients are strongly anti-correlated, and their posterior is
skewed by the physical bound δ_v,DM^NL > −1 [src: Sect. III.4].

The Beyond-2pt entry marginalised (C_slope, C_offset) with wide uniform
priors, U[−50, 10] and U[−10, 50], because no calibration existed for the
challenge tracers; it therefore reported Ω_m only and stated that σ8 needs an
independent calibration of the bias inside voids from realistic mocks [src:
arXiv:2405.02252, Sect. V.7.2, Table 4, Sect. II.2].

Cost of weaker calibration, BOSS mocks: inflating the calibration errors by
2, 3, 4 times the Poisson error (mimicking mocks 4, 9, 16 times smaller)
leaves σ(Ω_m)/Ω_m near 14% but raises σ(σ8)/σ8 from 9% to 23% and σ(w)/|w|
from 18% to 25%; the truth stays inside 68% throughout [src:
arXiv:2212.03873, App. C.1].

### Free threshold and free RSD factor (no mock calibration)
<!-- key: free-threshold-and-free-rsd-factor-no-mock -->

Song et al. 2025 fit δ_v^i, the linear threshold, and B^i = β^i δR_v^i in each
redshift bin i, on the argument that there is no strict threshold for void
formation and that any negative value may define a void [src:
arXiv:2501.07817, Sect. 3]. The RSD factor follows Correa et al.:
R_v^obs = q_RSD q_AP R_v with q_RSD = 1 − (1/3) δR_v β Δ(R_v), β = f/b_g and
Δ(R_v) = δ_v^NL (arXiv:2501.07817, Eqs. 10, 12). Only voids with ε_v < 0.15
enter, about 45% of the sample, because the model assumes spherical
evolution; cuts at 0.14 or 0.16 give consistent results, cuts outside that
range move some parameters by more than 1σ [src: Sect. 3]. The likelihood is
Gaussian, χ² with a covariance C of the measured VSF (Eq. 13), sampled with
emcee; h, Ω_b, n_s and A_s get Gaussian priors of ten times the Planck 2018
error [src: Sect. 4]. The fitted thresholds are δ_v = −0.162 +0.022/−0.024 and
−0.123 +0.014/−0.015 [src: Table 2]: shallow linear thresholds, which the
authors themselves call an empirical link between the excursion-set model
and watershed voids [src: Sect. 3]. Cost: σ8 to about 20% against 10% for the
BOSS DR12 relaxed calibration [src: arXiv:2501.07817, Sect. 4;
arXiv:2212.03873, Sect. IV.2].

### Redshift-space enlargement: absorbed or modelled
<!-- key: redshift-space-enlargement-absorbed-or-modelled -->

- **Absorbed into ℱ.** The Euclid calibration gives
  ℱ = (0.96 ± 0.04) b_eff + (0.44 ± 0.07) in redshift space and
  (0.96 ± 0.03) b_eff + (0.26 ± 0.06) in real space (arXiv:2205.11525,
  Eqs. 16–17): same slope, larger offset, which reflects the RSD enlargement
  [src: Sect. 4.1]. The stated reason for this route: it is simple and needs
  no assumption on the void matter-density profile, which a theoretical
  model would have to take from simulations [src: same].
- **Modelled.** For a spherical void finder, a real-space void of radius R
  becomes an ellipsoid with s_∥ = R(1 − β Δ_id/3) (arXiv:2007.12064, Eq. 6),
  Δ_id being the identification threshold; equal volume gives
  q_RSD^s = (1 − β Δ_id/3)^{1/3} (Eq. 7), and the general form is
  q_RSD = 1 − (1/3) δR_v β Δ_id with 0 ≤ δR_v ≤ 1 (Eq. 9). On the MXXL halo
  catalogue (Δ_id = −0.853 at z = 0.99, β = 0.65) q_RSD^s = 1.058, but large
  voids follow δR_v = 0.5, q_RSD^l = 1 − β Δ_id/6 = 1.092 (Eq. 10), which
  corrects the VSF better at large radii [src: Sects. 4.2, 6.3]. The
  real-to-redshift-space count ratio exceeds 4 at the largest radii before
  correction and stays below 0.8 after it [src: Sect. 6.3]. AP and RSD
  factors combine as R^zs = q_AP q_RSD R^rs (Eq. 15); q_AP carries the
  background geometry and q_RSD the growth rate β only [src: Sects. 4.3–4.4].
  The authors present this as foundations, not a complete VSF model [src:
  Sect. 6.1].

### Watershed plus cleaning, or a finder built for the model
<!-- key: watershed-plus-cleaning-or-a-finder-built-for -->

VERSUS (Findlay & Nadathur 2026, arXiv:2605.03779) finds spherical voids
directly by top-hat smoothing of a mesh density field at a list of radii,
from largest to smallest, as the excursion set does, with no post-processing
[src: Sect. 3.1]. Defaults: 4 h⁻¹Mpc cells, radii 25–61 h⁻¹Mpc in steps of
2 h⁻¹Mpc for n ≈ 5 × 10⁻⁴ h³Mpc⁻³, R = 25 h⁻¹Mpc as the minimum because
smaller radii admit spurious voids at that density [src: same]. With randoms
at 50 times the galaxy density and a smoothing of 4 random separations it
recovers the VSF on a BOSS CMASS SGC footprint [src: Sects. 3.1, 5.1]. On an
AbacusSummit LRG-like box both VERSUS and VIDE profiles imply similar void
biases at the void radius (b_v = 3.2 and 2.9), but the cleaned VIDE VSF needs
b_v ≈ 2 to be fitted at the true cosmology, inconsistent with its own
profile, while VERSUS is fitted with the b_v its profile implies [src:
Sect. 5.3]. Read: with watershed voids the bias that enters the VSF is not
the bias measured from the profiles, which is why the calibrated route fits
ℱ to counts rather than to profiles. A full Bayesian VERSUS analysis is left
for later work [src: Sect. 5.3].

### Model: Vdn or the moving-barrier multiplicity function
<!-- key: model-vdn-or-the-moving-barrier-multiplicity -->

Verza et al. 2024 (arXiv:2401.14451) combine the excursion set with peak
theory in Lagrangian space through an effective moving barrier. Against
DEMNUni voids with δ_v^E = −0.409 (linear δ_v = −0.623) at z = 0, the
Eulerian mapping of the Sheth–van de Weygaert model and the Vdn model do not
reproduce the measured VSF; the new model with spherical mapping is within
1σ at large and intermediate radii and overpredicts by about 50% at small
radii [src: Sect. 5.1]. The review reproduces this comparison as its Fig. 4
[src: arXiv:2503.22532, Sect. 3]. No data analysis with this model was found.

### Analytic model or simulation-based model
<!-- key: analytic-model-or-simulation-based-model -->

- **Analytic (Vdn with calibrated or free nuisance).** Cheap, transparent,
  but needs cleaning or a free threshold and a calibration of the bias
  inside voids (Steps 2–6).
- **Emulated summary statistics.** Lehman et al., Quijote halos: Ω_m and σ8
  recovered to 14.4% and 8.4% from void profiles, σ8 to 6.8% adding the VSF;
  robust to resolution, and posteriors unchanged with Magneticum baryons
  (arXiv:2502.05262) [src].
- **Implicit likelihood on data.** BOSS CMASS NGC with the VSF, the
  void–galaxy cross power spectrum and P_gg: Σm_ν < 0.43 eV (P_gg) and
  < 0.35 eV (all), 95%, k_max = 0.15 h Mpc⁻¹, Planck-inspired ΛCDM prior; void
  statistics may constrain Σm_ν "most effectively from below"
  (arXiv:2307.07555) [src: abstract].
- **HOD forward model, forecast.** VSF + w_p,vg + w_p,gg in DESI Y5: 1.5% on
  Ω_m and 0.8% on σ8, **forecast** (arXiv:2504.08221) [src: abstract].
- **Information content, forecasts.** GIGANTES: σ(Σm_ν) = 0.13 eV from voids
  alone and 0.09 eV with halos for 1 h⁻³Gpc³, no CMB prior, **forecast**
  (arXiv:2107.02304) [src: abstract]; Bayer et al.: P(k) + halo mass function + VSF give
  σ(M_ν) = 0.018 eV for 1 (h⁻¹Gpc)³, **forecast**, an underestimate without
  super-sample covariance, baryons and survey systematics (arXiv:2102.05049)
  [src: abstract]. DEMNUni: dark energy and neutrino masses act separably on the VSF
  (Verza et al. 2022, arXiv:2212.09740) [src].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Tracer threshold δ_v,tr^NL | −0.7 (−0.6 tested) | BOSS DR12, Euclid, Beyond-2pt | arXiv:2212.03873; arXiv:2205.11525; arXiv:2405.02252 | Sect. III.2; Sect. 2.2; Sect. V.7.2 |
| Central-density rejection | δ_v,tr(2 MGS) < −0.7 required | BOSS DR12 | arXiv:2212.03873 | Sect. III.2 |
| Bernardeau constant 𝒞 | 1.594 | all | arXiv:2212.03873 | Eq. 4 |
| Linear void threshold, Einstein–de Sitter | −2.71 | — | arXiv:2212.03873 | footnote to Eq. 2 |
| δ_c^L range | 1.06–1.686 | — | arXiv:2212.03873 | footnote to Eq. 2 |
| Calibrated (C_slope, C_offset) | (−1.62, 4.30); data posterior −2.02 +0.66/−0.61, 4.74 +0.87/−0.82 | BOSS DR12, Patchy | arXiv:2212.03873 | Table 1 |
| b_eff σ8, data | 1.36 ± 0.05 (0.2 < z ≤ 0.45), 1.28 ± 0.06 (0.45 < z < 0.65) | BOSS DR12 | arXiv:2212.03873 | Sect. IV.1 |
| b_eff σ8, mocks | 1.33 ± 0.02, 1.26 ± 0.02 (b_eff 1.94, 2.02) | Patchy | arXiv:2212.03873 | Sect. III.4 |
| Radius bins on mocks | 6 and 5 logarithmic bins | Patchy | arXiv:2212.03873 | Sect. III.4 |
| Euclid ℱ calibration | 0.96 b_eff + 0.44 (z space), + 0.26 (r space) | Flagship | arXiv:2205.11525 | Eqs. 16–17 |
| Voids before and after cleaning | 33 828 → 2 054, six bins with ≥ 340 each | Flagship, 0.95 < z < 1.70 | arXiv:2205.11525 | Table 1 |
| Edge cut | centres ≥ 30 h⁻¹Mpc from the footprint edge | Flagship | arXiv:2205.11525 | Sect. 2.2 |
| Beyond-2pt VSF priors | Ω_m U[0.05, 0.9], σ8 U[0.2, 2]; h, Ω_b h², n_s three Planck widths | light cone | arXiv:2405.02252 | Table 4 |
| Radius-cut scan | R_min 35 → 40 h⁻¹Mpc: errors ×1.9 (Ω_m), ×1.2 (σ8) in ΛCDM, ×1.6 in wCDM | Patchy | arXiv:2212.03873 | App. C.3 |
| Fiducial Ω_m test | 0.279 and 0.335 (±3σ Planck): Ω_m 0.265 and 0.270, truth 0.307 | Patchy | arXiv:2212.03873 | App. C.2, Table 3 |
| Ellipticity cut | ε_v < 0.15 keeps ≈ 45% | BOSS DR16 | arXiv:2501.07817 | Sect. 3 |
| Free thresholds | δ_v = −0.162, −0.123 | BOSS DR16 | arXiv:2501.07817 | Table 2 |
| q_RSD on MXXL halos | 1.058 (q^s), 1.092 (q^l); δR_v = 0.315 and 0.5 | spherical finder, z = 0.99 | arXiv:2007.12064 | Sect. 4.2 |
| Σm_ν from BOSS voids (implicit likelihood) | < 0.43 eV (P_gg), < 0.35 eV (VSF + P_vg + P_gg), 95% | CMASS NGC | arXiv:2307.07555 | abstract |
| VSF radius bins, CMASS | 32 linear, 30–80 h⁻¹Mpc, split at z = 0.53 | VIDE | arXiv:2307.07555 | Sect. III.1 |
| Emulated void statistics | Ω_m 14.4%, σ8 8.4% (profiles); σ8 6.8% with VSF | Quijote | arXiv:2502.05262 | abstract |
| DESI DR1 voids (AVISM) | 1114 BGS (0.1 < z < 0.3), 216 LRG (0.4 < z < 0.8); bias in voids 1.31 ± 0.02, 2.14 ± 0.04 | DESI DR1 | arXiv:2610.18348 | abstract |
| SvdW + Vdn threshold for DESI DR1 overlay | δ_V^L = −0.55 | DESI DR1 | arXiv:2610.18348 | Sect. 4.2 |
| Free thresholds, CSST mock | ≈ −0.4 to −0.1, z = 0.5–1.1 | Jiutian SAM | arXiv:2402.05492 | abstract |
| DESI Y5 VSF + w_p forecast | Ω_m 1.5%, σ8 0.8% (**forecast**) | HOD grid | arXiv:2504.08221 | abstract |
| Tessellation stabilisation | 20–40% better constraints | DIVE, VIDE | arXiv:2606.21864 | Sect. I |
| VERSUS speed | < 20 s at 500³ cells for (2 h⁻¹Gpc)³; ≈ 8 times faster than VIDE for ≈ 4 × 10⁶ galaxies | AbacusSummit | arXiv:2605.03779 | Sect. 5.1 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Model and catalogue thresholds differ.** The model is valid only for the
  δ_v,tr^NL used in cleaning, converted through ℱ and Bernardeau's formula
  [src: arXiv:2205.11525, Sect. 2.2; arXiv:2212.03873, Sect. III.2]. Test: run
  the whole chain at a second threshold (−0.6 in the Euclid paper).
- **Small-radius incompleteness.** The counts fall below the model near the
  MGS, at R_eff < 35 h⁻¹Mpc in BOSS [src: arXiv:2212.03873, Sect. III.1].
  Test: scan R_min; the Beyond-2pt team found the posterior "mildly" depends
  on the cut and states that this error is neither quantified nor included
  [src: arXiv:2405.02252, Sect. V.7.4, Caveats].
- **Poisson errors too small.** In Patchy the scatter of cleaned counts is
  larger than the Poisson error, which "represents an underestimation of the
  true error" [src: arXiv:2212.03873, Sect. III.4]. The data errors were
  therefore taken from the mocks, rescaled by the square root of the volume
  ratio [src: Sect. III.1]. Off-diagonal covariance was negligible; a Gaussian
  likelihood with the full mock covariance gave no significant change [src:
  Sect. III.4]. The Beyond-2pt VSF used pure Poisson diagonal errors [src:
  arXiv:2405.02252, Sect. V.7.3].
- **Fiducial-cosmology dependence.** Rerunning finder and cleaning at
  fiducial Ω_m = 0.279 or 0.335 recovers the Patchy truth within 68%, but the
  underestimate "starts to become statistically significant" for a fiducial
  Ω_m below the truth [src: arXiv:2212.03873, App. C.2]. The radius cut is
  recomputed from MGS in each fiducial cosmology [src: same].
- **Calibration mocks at one cosmology.** All Patchy mocks share the
  MultiDark Planck 2013 cosmology; the authors argue from earlier tests that ℱ
  depends negligibly on cosmology [src: arXiv:2212.03873, Sects. II.2, III.1].
  ℱ does depend on tracer type and selection [src: arXiv:2205.11525,
  Sect. 4.1]: calibrate on mocks of the same sample.
- **Calibration absorbs information.** Part of the constraining power goes
  into (C_slope, C_offset) when they are not fixed [src: arXiv:2212.03873,
  App. B]. A fixed-calibration σ8 or w is optimistic by construction.
- **Bias from profiles used for counts.** With cleaned watershed voids the
  bias implied by the profile does not reproduce the counts (b_v ≈ 2.9 against
  ≈ 2 needed) [src: arXiv:2605.03779, Sect. 5.3]. Do not take ℱ from
  profile measurements in that route.
- **Prior outside the truth.** In Beyond-2pt the informative priors on h, ω_b
  and n_s excluded the true values; post-unmasking analyses showed at most a
  minor bias in Ω_m [src: arXiv:2405.02252, Sect. II.2].
- **Mask and boundaries.** Voids cut by the footprint distort counts; VIDE
  removes voids intersecting boundaries, and the effective volume must be
  computed consistently [src: arXiv:2212.03873, Sect. III.1]; the Euclid
  analysis adds a 30 h⁻¹Mpc edge cut [src: arXiv:2205.11525, Sect. 2.2].

Validation suite of the BOSS analysis, with its criterion: fixed and relaxed
calibration recover the Patchy cosmology within 68% (App. B, Table 2);
calibration-error inflation, fiducial-cosmology and radius-cut variations
keep the truth within 68% (App. C) [src: arXiv:2212.03873].

## Reading list
<!-- key: reading-list -->

- Review: Cai & Neyrinck 2025, arXiv:2503.22532 — Sect. 3, excursion-set VSF,
  finder families, applications.
- Foundation: Sheth & van de Weygaert 2004, arXiv:astro-ph/0311260, and
  Jennings, Li & Hu 2013, arXiv:1304.6087 — two-barrier model and volume
  conservation (see L2).
- Method: Contarini et al. 2022, arXiv:2205.11525 — cleaning, f_cut, ℱ
  calibration, RSD absorbed in ℱ.
- Application: Contarini et al. 2023, arXiv:2212.03873 — the full BOSS DR12
  pipeline, fixed against relaxed calibration, systematics appendix.
- Application: Song et al. 2025, arXiv:2501.07817 — free threshold, RSD
  factor and ellipticity cut.
- Application: Beyond-2pt challenge, arXiv:2405.02252, Sect. V.7 — VSF with
  marginalised calibration on a masked light cone.
- Method: Correa et al. 2020, arXiv:2007.12064 — expansion, AP volume change
  and off-centring of redshift-space voids.
- Method: Verza et al. 2024, arXiv:2401.14451 — moving-barrier multiplicity
  function, failure of Vdn on DEMNUni.
- Critique: Findlay & Nadathur 2026, arXiv:2605.03779 — finder designed for
  the model; profile bias against count bias.
- Code: Ronconi & Marulli 2017, arXiv:1703.07848 — CosmoBolognaLib void
  cleaning and VSF models.
- Application, simulation-based: Thiele et al. 2023, arXiv:2307.07555 — BOSS
  voids with implicit likelihood, Poisson test.
- Method, emulator: Lehman et al. 2025, arXiv:2502.05262 — neural emulators
  of VSF and profiles on Quijote.
- Data set: Kreisch et al. 2022, arXiv:2107.02304 — GIGANTES VIDE catalogues.
- Forecast: Bayer et al. 2021, arXiv:2102.05049 (spherical finder, P + HMF +
  VSF); Salcedo et al. 2025, arXiv:2504.08221 (HOD forward model, DESI Y5);
  Song et al. 2024, arXiv:2402.05492 (CSST, free threshold); Verza et al.
  2022, arXiv:2212.09740 (DEMNUni, dark energy and neutrinos).
- Method, finders: Liu et al. 2026, arXiv:2606.21864 — DIVE against VIDE,
  tessellation instability.
- Data: Monllor-Berbegal et al. 2026, arXiv:2610.18348 — DESI DR1 AVISM void
  catalogues and VSF.

## Not verified
<!-- key: not-verified -->

- Bernardeau 1994 (the fitting formula of Step 5): cited through
  arXiv:2212.03873 and arXiv:2205.11525, not read; no identifier recorded.
  Ronconi & Marulli 2017 (arXiv:1703.07848): abstract read, the cleaning
  algorithm itself is taken from arXiv:2212.03873.
- How Song et al. 2025 built the covariance C of Eq. 13 (not in the sections
  read).
- The companion BOSS paper combining the VSF with other probes (ref. [33] of
  arXiv:2212.03873) and the SDSS DR7 VSF analysis of Fernández-García et al.
  2024 named in arXiv:2503.22532: not read.
- Whether the Poisson approximation holds for cleaned voids at Stage-IV
  volume: L2 cites a simulation check (arXiv:2307.07555), not re-read here.
- No DESI VSF cosmology was found in date-sorted searches (2025-06-01, and
  again 2026-10-22); the DESI DR1 AVISM catalogue (arXiv:2610.18348) shows a
  VSF against theory but fits no cosmology. The DIVE paper (Zhao et al.
  2016), the Pylians void finder and the REVOLVER, VAST and VEGA papers were
  not read.
