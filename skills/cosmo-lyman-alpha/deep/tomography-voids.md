# Lyα tomography: maps, voids and protoclusters — cosmo-lyman-alpha dossier

Scope: how a 3D Lyα tomographic map is made from sightline pixels (pixel
selection, coordinates, Wiener-filter covariance, noise floor, solver, map
variance), how it is validated on mocks, how voids and protoclusters are found
in it and calibrated, and how the Wiener filter compares with the constrained
(ORCA) and forward-model (TARDIS) reconstructions; the void–forest RSD fit
itself is left to the sibling dossier.
Snapshot: 2026-10-19.
From: Tomography survey groups (CLAMATO, arXiv:1710.02894; Stripe 82 eBOSS
map, arXiv:2004.01448).

Already in L2, not repeated here: the survey list with areas, sightline
densities and map resolutions (`surveys-and-data.md#tomography-surveys`); the
origins of the method, the sightline requirements of Lee et al. 2014 and the
two regimes (`physics-and-methods.md#tomography-and-voids`); the void, map and
cross-correlation results (`results.md#tomography-voids-and-cross-correlations`);
the tomography systematics list (`systematics.md#tomography-specific`); the
open questions (`open-questions.md#tomography-what-cosmology-can-it-deliver`).
The void–forest cross-correlation model, its β and the "tomographic effect"
correction are in `cosmo-beyond-two-point/deep/void-galaxy-rsd-ap.md`.

Notation. δ_F = f/(C⟨F⟩) − 1 the flux contrast of a pixel (C continuum, ⟨F⟩
mean transmission); δ_F^rec the reconstructed map; ⟨d_⊥⟩ the mean transverse
separation between sightlines at a given redshift; L_⊥, L_∥ the transverse and
line-of-sight correlation lengths of the Wiener prior; σ_F² its amplitude;
N the noise covariance and σ_N,i (or n_i) the pixel noise; positive δ_F means
low absorption, hence low density.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Select sightlines and compute δ_F
<!-- key: step-1-select-sightlines-and-compute-deltaf -->

CLAMATO DR1 (arXiv:1710.02894) [src: Sect. IV]:

- Signal-to-noise is first estimated as a continuum-to-noise ratio (CNR) with
  a quick continuum (power law redward of 1216 Å for galaxies, principal
  components for quasars) in three absorption-redshift ranges. Every spectrum
  with redshift confidence ≥ 3 and ⟨CNR⟩ ≥ 1.2 in one range is kept: "an
  aggressive choice" justified because the Wiener filter weights by noise and
  because CLAMATO is in the ⟨d_⊥⟩ ≳ 1.5 h⁻¹Mpc shot-noise-dominated regime.
- Continua: mean-flux-regulated PCA for quasars over 1041–1185 Å; a fixed
  galaxy template over 1040–1195 Å for galaxies, with ± 7.5 Å (observed)
  masks around N II 1084, N I 1134, C III 1176 and Si II 1190, 1193. ⟨F⟩(z)
  from Faucher-Giguère et al. Continuum errors ~10% rms at S/N ~ 2 per pixel,
  ~4% at S/N ~ 10.
- Result: 240 spectra; projected density 1455 deg⁻², but the differential
  density averaged over the map is 866 deg⁻² (⟨d_⊥⟩ = 2.35 h⁻¹Mpc), 673 and
  451 deg⁻² at the two redshift ends, peak 1099 deg⁻² at z = 2.32. The
  authors stress that a projected density over all redshifts (quoted as
  16 deg⁻² for BOSS) overstates the density at one redshift (9 deg⁻² peak for
  BOSS).

LATIS feeds each pixel with its total uncertainty σ_tot to the same code
(arXiv:2510.08815) [src: Sect. VI.1].

### Step 2. Choose the map coordinates
<!-- key: step-2-choose-the-map-coordinates -->

| Choice | CLAMATO DR1 | eBOSS Stripe 82 | LATIS |
|---|---|---|---|
| Coordinates | fixed H(z) at ⟨z⟩ = 2.30: one-to-one (RA, Dec) ↔ (x, y) | all sightlines parallel, transverse distances at z = 2.65; ΛCDM with Ω_m = 0.3147, h-free units | (X, Y, Z) from D_C(z) per pixel, so sightlines flare outward |
| Grid | 60 × 48 × 876 cells of 0.5 h⁻¹Mpc; 30 × 24 h⁻¹Mpc transverse | 5856 × 180 × 834 pixels, ~1 h⁻¹Mpc; 0.94 h⁻³Gpc³ | (1 h⁻¹ cMpc)³ voxels; 3.96 × 10⁶ h⁻³ cMpc³ inside the sightlines |
| Stated reason or cost | preserves comparisons with coeval galaxies; a run with evolving H(z) changed the void analysis negligibly; "more detailed cosmological analyses ... would tend to directly use the pixel data" | errors of a few percent along Dec over z = 2.1–3.2; along the 88° RA direction the approximation "does not hold at all", so the map "is not adapted for studies on large-scale distances" | transverse area not fully sampled at the low-z end |
| Place read | arXiv:1710.02894, Sect. IV | arXiv:2004.01448, Sect. 3 | arXiv:2510.08815, Sect. VI.1, Eq. 2 |

### Step 3. Wiener-filter the pixels
<!-- key: step-3-wiener-filter-the-pixels -->

The map is the Wiener (minimum-variance linear) estimate

    δ_F^rec = C_MD · (C_DD + N)⁻¹ · δ_F                     (arXiv:1710.02894, Eq. 2)

with a Gaussian signal covariance between points r_1, r_2

    C(r_1, r_2) = σ_F² exp[−Δr_∥²/(2L_∥²)] exp[−Δr_⊥²/(2L_⊥²)]   (Eq. 3)

and diagonal N_ii = σ_N,i². Stripe 82 writes the same operator as
L = S_mp (S_pp + N)⁻¹ (arXiv:2004.01448, Eqs. 3–5) and notes that, under the
hypotheses of the Bayesian derivation of Pichon et al., the Bayesian approach
"is mathematically equivalent to applying a Wiener filter" [src: Sect. 3]. All
survey maps here use the public conjugate-gradient code dachshund
(a high-performance implementation of this map-making is presented in
arXiv:1412.1507, abstract) [src: arXiv:1710.02894,
Sect. IV; arXiv:2004.01448, Sect. 3; arXiv:2510.08815, Sect. VI.1].

| Parameter | CLAMATO DR1 and DR2 | eBOSS Stripe 82 | Reason given |
|---|---|---|---|
| L_⊥ | 2.5 h⁻¹Mpc | 13 h⁻¹Mpc | CLAMATO: L_⊥ ≈ ⟨d_⊥⟩; Stripe 82: no transverse structure below ⟨d_⊥⟩ can be reconstructed, and L_⊥ > ⟨d_⊥⟩(z) for z < 2.8 |
| L_∥ | 2.0 h⁻¹Mpc | 13 h⁻¹Mpc | CLAMATO: L_∥² ≈ L_⊥² − σ_lsf², so that with the spectrograph smoothing the kernel is isotropic; Stripe 82: L_∥ = L_⊥ "reduces the amplitude of anisotropies" and removes small-scale line-of-sight fluctuations |
| σ_F² | 0.05 | 0.01 | CLAMATO: approximately optimal on mocks (Stark et al.); Stripe 82: chosen so that the maximal map contrast is 1, as in CLAMATO |
| Noise floor | σ_N,i ≥ 0.2 | n_min = 0.1 (applied to the 6.3% lowest-noise pixels) | CLAMATO: stops a few bright quasars with S/N > 10× the mean from dominating; Stripe 82: avoids numerical divergence; the floor also sets the maximal contrast through σ_F²/n_min²; CLAMATO's higher floor reflects noisier LBG spectra |
| Solver | preconditioned conjugate gradient, tolerance 10⁻³; ~1000 s on one laptop core for 64,332 (DR1) or 84,608 (DR2) pixels | same code, field cut into chunks overlapping by L_⊥ to avoid edge effects | — |
| Place read | arXiv:1710.02894, Sect. IV; arXiv:2109.09660, Sect. IV.2 | arXiv:2004.01448, Sect. 3 | same |

LATIS smooths the Wiener output further with an isotropic Gaussian of
σ = 4 h⁻¹ cMpc and releases maps of δ_F/σ_map, with σ_map computed away from
the boundaries (excluding voxels within 4 h⁻¹ cMpc of an edge) to limit edge
effects: σ_map = 0.0496, 0.0476, 0.0458 in D1, D2, D4 (arXiv:2510.08815,
Sect. VI.1) [src]. Its covariance parameters are in an earlier LATIS paper not
read here.

### Step 4. Attach an uncertainty to the map
<!-- key: step-4-attach-an-uncertainty-to-the-map -->

The Wiener map variance is Var(δ_F^rec) = C_MD (C_DD + N)⁻¹ C_DM
(arXiv:1710.02894, Eq. 4), a factor N_pix more expensive than the map. It
contains intrinsic forest variance, pixel noise and sampling; subtracting the
intrinsic variance measured on simulations binned and smoothed like the map
gives a global

    S/N^wiener = sqrt{ Var^intr / (⟨Var(δ_F^rec)⟩ − Var^intr) }    (Eq. 5)

which is ≈ 0.65 per 0.5 h⁻¹Mpc voxel for CLAMATO DR1, rising to ≈ 1.8, 3.4,
5.2 over top-hats of 2, 3, 4 h⁻¹Mpc (⟨Var⟩ = 0.0219, Var^intr = 0.00654)
[src: Sect. VI.1].

### Step 5. Validate on mock surveys built like the data
<!-- key: step-5-validate-on-mock-surveys-built-like-the -->

| Item | eBOSS Stripe 82 | LATIS | CLAMATO voids |
|---|---|---|---|
| Truth | Gaussian random field with FGPA, τ = a(z) exp[−b G(z)(δ_m + δ_s + c(z) η_∥)] (Eq. 6); δ_s adds small-scale power tuned to P1D; a and c set to the observed bias and β; b = 2 − 0.7(γ − 1) = 1.58 for γ = 1.6 | FGPA in the MDPL2 snapshot at z = 2.535 | Nyx 100 h⁻¹Mpc hydrodynamical box and a 256 h⁻¹Mpc N-body box |
| Survey effects | quasar positions matched to the DR16 Stripe 82 density and redshift distribution; continua, metals and HCDs from quickquasars, HCDs removed as in the data; no BALs | 100 subvolumes per field with the real sightline layout, resolution, noise and continuum errors (300 mock maps) | CLAMATO-like sightline spacing, realistic noise and continuum error, mean flux rescaled to ⟨F(z = 2.3)⟩ |
| Metric | Pearson r between the map and the input δ_m smoothed at 8 h⁻¹Mpc (smoothing chosen to maximise it) | conditional expectations ⟨δ_true|δ_rec⟩ and ⟨δ_rec|δ_true⟩, δ_true from a 0.25 h⁻¹Mpc grid smoothed at 4 h⁻¹Mpc | void purity and completeness against the redshift-space density field |
| Result | r = −0.34 over z = 2.1–2.7 (the high-z part is largely masked) | ⟨δ_true|δ_rec⟩ close to 1:1, i.e. nearly unbiased; ⟨δ_rec|δ_true⟩ = 0.544 δ_true + … (Table 3), i.e. the map shrinks true fluctuations | see Step 6 |
| Place read | arXiv:2004.01448, Sects. 4.1–4.2 | arXiv:2510.08815, Sect. VI.2 | arXiv:1710.02612, Sect. IV.1 |

The Stripe 82 authors note that their mock noise histogram differs from the
data in the low-S/N tail and checked, by removing high-noise data, that this
has a minor effect because the Wiener filter down-weights noisy pixels
(arXiv:2004.01448, Sect. 4.1) [src]. LATIS locates protoclusters and
estimates their masses by direct comparison with mock maps, so "all that
matters is that the mock observations are faithful" (arXiv:2510.08815,
Sect. VI.2) [src].

### Step 6. Find voids
<!-- key: step-6-find-voids -->

Spherical-overdensity (SO) finder (Stark et al., as applied in
arXiv:1710.02612, Sect. IV.1, and arXiv:2004.01448, Sect. 5.2) [src]: select
all map points with δ_F above a threshold, grow a sphere around each until the
mean δ_F inside falls to a second ("average") threshold, resolve overlaps by
keeping the largest sphere, drop small radii.

| Setting | CLAMATO (2.5 h⁻¹Mpc map) | Stripe 82 (13 h⁻¹Mpc map) |
|---|---|---|
| Thresholds | δ_F^rec > 0.220, average 0.175 | δ_th = 0.14, δ_av = 0.12 |
| How fixed | to reproduce the void volume fraction of the redshift-space density field (SO thresholds 0.15 ρ̄ and 0.3 ρ̄; volume fraction 0.173–0.180) on mock reconstructions | scanned on the mock map until the positions of ~25 h⁻¹Mpc voids are stable |
| Minimum radius | r > 2 h⁻¹Mpc; r ≥ 5 h⁻¹Mpc for profiles | R_min = 7 h⁻¹Mpc (larger than the smoothing) |
| Extra cuts | — | void crossed by sightlines of total length > its radius (≥ 2 sightlines); < 5% of its volume farther than 20 h⁻¹Mpc from any sightline |
| Outcome | 355 voids (48 with r ≥ 5); volume fraction 19.5% in data, 18.0–18.2% in mocks | filling factor 14% |

Reasons for the SO finder: watershed finders "may lead to poor performance in
the presence of noise", and simplicity for a first detection (arXiv:1710.02612,
Sect. IV.1) [src]; the SO method is "more robust than the watershed algorithm
with respect to noise on large scales" (arXiv:2004.01448, Sect. 5.2) [src].
Reason the thresholds must come from realistic mocks: the void fraction
depends on the mean flux and on continuum error, which acts as
δ_cont F/⟨F⟩ and so matters most at high transmission; with identical
thresholds continuum error raises the void fraction from 18% to 24%
(arXiv:1710.02612, Sect. IV.1) [src].

### Step 7. Find protoclusters
<!-- key: step-7-find-protoclusters -->

| Setting | Simulation study (arXiv:1412.1507, Sect. V) | Stripe 82 (arXiv:2004.01448, Sect. 5.1) |
|---|---|---|
| Pre-smoothing | 3D Gaussian σ = 4 h⁻¹Mpc ("much like a matched filter"; 2 and 8 tried, 4 best) | none: the 13 h⁻¹Mpc map smoothing already exceeds protocluster size |
| Threshold | δ_F < −3.5 σ of the field, best for > 3 × 10¹⁴ h⁻¹M☉ descendants | watershed on δ_F < −3.5 σ̃_map |
| Grouping and size | merge points within 4 h⁻¹Mpc; candidate = 4 h⁻¹Mpc sphere on the minimum | R = (3 N_pix V_pix/4π)^(1/3), R_min = 7 h⁻¹Mpc |
| Spurious-detection guard | — | crossing sightline length > 3 × diameter (> 3 sightlines), against residual HCDs and metals |
| Outcome on simulations | 68 candidates (~10⁻³ of the volume) in the ideal field, almost all protoclusters (z = 0 mass > 10¹⁴ h⁻¹M☉), halo counts ~5× the field median | 9 mock candidates, mean radius 10.5 h⁻¹Mpc, all with positive mean matter contrast, ⟨δ_M⟩ = 0.4 |

The Stripe 82 authors stress that interpreting their overdensities as
protoclusters "would require dedicated N-body simulations" [src: Sect. 5.1].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Wiener filter, constrained flux reconstruction or forward model
<!-- key: wiener-filter-constrained-flux-reconstruction -->

- **Wiener filter (dachshund).** Linear, Gaussian prior with no explicit
  cosmology dependence; "technical simplicity" and inclusion of instrumental
  properties are the reasons given (arXiv:2004.01448, Sect. 3) [src]. Cost:
  the map is biased towards zero by noise, can exceed F = 1, and assumes
  Gaussianity, which suits a 13 h⁻¹Mpc map whose fluctuations are "nearly
  Gaussian" (same) [src] better than a 2 h⁻¹Mpc one.
- **ORCA** (arXiv:2102.12306) [src: abstract, Sects. II.2, III.2]. Minimises
  L = k_1 (S_m(s) − s)² + (R(s) − d)ᵀ N⁻¹ (R(s) − d) + k_2 Σ clip(s, 1, ∞)
  + k_3 Σ clip(s, 0, α) (Eq. 3) with L-BFGS, smoothing annealed from 1.25 to
  0.5 h⁻¹Mpc in 0.25 steps; the first two terms alone reproduce the Wiener
  result for L_∥ = L_⊥ = m. The clip terms penalise non-physical
  transmission. On Nyx mocks the reconstructed-versus-true slope and Pearson
  coefficient are 0.677 and 0.711 against 0.653 and 0.680 for the Wiener
  filter, "equivalent to 30–40% additional sight-lines"; ~250 s against
  ~8000 s on the same mock, 10–100× faster on GPU. Parameters
  k_1 = 5, k_2 = 0.3, k_3 = 0.025; the Wiener comparison used σ_F² = 0.082 to
  match the CLAMATO δ_F^rec PDF.
- **TARDIS** (arXiv:1903.09049) [src: Sects. II–III, App. C]. Solves for the
  initial field s maximising the posterior with χ² = sᵀS⁻¹s +
  (d − R(s))ᵀN⁻¹(d − R(s)) (Eq. 3), R the forward operator: Gaussian field →
  FastPM to z = 2.5 → FGPA τ in real space → shift by line-of-sight velocity →
  F = e^(−τ) → select skewers → spectrograph smoothing. Gradients by automatic
  differentiation (vmad), L-BFGS rather than HMC because a most-likely map is
  wanted; ~5 CPU-hours per reconstruction. It returns the matter field (and
  its z = 0 descendant), not only the flux, which allows cosmic-web
  classification. Against the Wiener filter on the CLAMATO/PFS-like mock the
  flux maps are "fairly similar", with some smaller-scale features better
  recovered; both are noise-biased and TARDIS applies a linear correction
  calibrated on a separate volume.
- **TARDIS on data** (CLAMATO DR2, arXiv:2109.09660) [src: Sects. IV.3, V.2]:
  joint with zCOSMOS galaxies, chosen because it has a well-characterised
  selection function (~45% of galaxies in the volume); four overlapping
  128 h⁻¹Mpc subvolumes (15 h⁻¹Mpc radial overlap, data offset 10 h⁻¹Mpc from
  periodic edges), ~30 min on one GPU. The TARDIS-derived flux and the Wiener
  map correlate at Pearson 0.86, and the deformation-tensor classifications
  at 0.83. The authors read large differences, if found, as signs of
  departures from the FGPA such as cluster feedback.

Further routes named by the review (variational autoencoders trained on
hydrodynamical simulations, other Bayesian forward models) are summarised in
arXiv:2605.22489, Sect. 0.6.4 [sec]; not read here.

### Smoothing lengths: tied to sightline spacing or isotropised
<!-- key: smoothing-lengths-tied-to-sightline-spacing-or -->

Both conventions set L_⊥ by ⟨d_⊥⟩. They differ along the line of sight:
CLAMATO keeps L_∥ < L_⊥ to make the effective kernel isotropic after the
instrumental smoothing; Stripe 82 sets L_∥ = L_⊥ far above the resolution.
Even with an isotropic filter the Stripe 82 stacked mock void is elongated
across the line of sight, axis ratio d_yz = 1.37 ± 0.01 (d_xy = 0.98 ±
0.005); switching off RSD in the mock gives 1.33, and subsampling the
sightlines reduces it, so most of the anisotropy comes from the parallel
sightline geometry (arXiv:2004.01448, Sect. 5.3) [src]. This is the geometric
anisotropy that the void–forest RSD model must remove (sibling dossier).

### Map statistics or pixel statistics
<!-- key: map-statistics-or-pixel-statistics -->

CLAMATO's authors state that detailed cosmological analyses would use the
pixels rather than the map (arXiv:1710.02894, Sect. IV) [src]; the Stripe 82
void–forest measurement does this: voids from the map, correlation with the
pixel δ_F (`cosmo-beyond-two-point/deep/void-galaxy-rsd-ap.md`). Map-level
quantities (void sizes, protocluster masses, LATIS conditional expectations)
are calibrated only through mocks with the same sightline pattern.

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Wiener prior (L_⊥, L_∥, σ_F²) | (2.5, 2.0 h⁻¹Mpc, 0.05) | CLAMATO DR1, DR2 | arXiv:1710.02894; arXiv:2109.09660 | Sect. IV; Sect. IV.2 |
| Wiener prior | (13, 13 h⁻¹Mpc, 0.01) | eBOSS Stripe 82 | arXiv:2004.01448 | Sect. 3 |
| Noise floor | σ_N ≥ 0.2 (CLAMATO); n_min = 0.1 (Stripe 82) | — | arXiv:1710.02894; arXiv:2004.01448 | Sect. IV; Sect. 3 |
| Pixel selection | ⟨CNR⟩ ≥ 1.2 in one z range, confidence ≥ 3 | CLAMATO DR1 | arXiv:1710.02894 | Sect. IV |
| Sightline density | mean 866 deg⁻² (⟨d_⊥⟩ = 2.35 h⁻¹Mpc), peak 1099 deg⁻² at z = 2.32 | CLAMATO DR1 | arXiv:1710.02894 | Sect. IV, Fig. 8 |
| S/N per voxel | 0.65 (0.5 h⁻¹Mpc); 1.8, 3.4, 5.2 over 2, 3, 4 h⁻¹Mpc | CLAMATO DR1 | arXiv:1710.02894 | Sect. VI.1 |
| Map–matter correlation | r = −0.34 (δ_m smoothed 8 h⁻¹Mpc, z = 2.1–2.7) | Stripe 82 mocks | arXiv:2004.01448 | Sect. 4.2 |
| Map shrinkage | ⟨δ_rec|δ_true⟩ slope 0.544; normalised by σ_map 0.733 | LATIS mocks | arXiv:2510.08815 | Table 3 |
| Void recovery | completeness and purity 30–45% at r ~ 6 h⁻¹Mpc; 40–45% of r ≥ 5 h⁻¹Mpc voids recovered (not 60%); match fraction ~5% at r ~ 2 h⁻¹Mpc | CLAMATO-like mocks | arXiv:1710.02612 | Sect. IV.1 |
| Effect of continuum error on voids | completeness and purity lower by 5–10 points; void fraction 18% → 24% at fixed thresholds | CLAMATO-like mocks | arXiv:1710.02612 | Sect. IV.1 |
| Void filling factor | 19.5% (CLAMATO data); 14% (Stripe 82) | — | arXiv:1710.02612; arXiv:2004.01448 | Sect. IV.2; Sect. 5.2 |
| Stacked void axis ratio | 1.37 ± 0.01 (1.33 without RSD) | Stripe 82 mocks | arXiv:2004.01448 | Sect. 5.3 |
| Protocluster threshold | −3.5 σ after 4 h⁻¹Mpc smoothing | simulations | arXiv:1412.1507 | Sect. V |
| Exposure scaling | t_exp ∝ SNR_min² ⟨d_⊥⟩^(−1.6), quoted from Lee et al. | mock-survey design | arXiv:1412.1507 | Sect. VI |
| TARDIS mock surveys | ⟨d_⊥⟩ = 3.7, 2.4, 1.0 h⁻¹Mpc (363, 863, 4970 deg⁻²) | DESI-like, CLAMATO/PFS-like, 30-m-like | arXiv:1903.09049 | Table 1 |
| WF vs TARDIS on data | Pearson 0.86 (flux), 0.83 (web classification) | CLAMATO DR2 | arXiv:2109.09660 | Sect. V.2 |
| ORCA vs WF | slope 0.677 vs 0.653, r 0.711 vs 0.680 | Nyx mocks | arXiv:2102.12306 | Sect. III.2 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Projected instead of differential sightline density.** Quoting the
  all-redshift density overstates the map resolution; CLAMATO 1455 versus
  866 deg⁻², BOSS 16 versus 9 deg⁻² (arXiv:1710.02894, Sect. IV) [src]. Test:
  plot ⟨d_⊥⟩(z) (Stripe 82 Fig. 2; CLAMATO Fig. 8) and compare with L_⊥.
- **L_⊥ below ⟨d_⊥⟩.** At z > 2.8 the Stripe 82 L_⊥ is below the
  sightline spacing, "a fact which must be considered when interpreting the
  map" (arXiv:2004.01448, Sect. 3) [src]; structures there are interpolation.
- **Continuum error makes and erases voids.** It is correlated along a
  sightline, so it "will both create spurious voids and erase real voids"
  (arXiv:1710.02612, Sect. IV.1) [src]. Test: mocks with and without
  continuum error; thresholds valid "only ... to the data presented".
- **Spurious overdensities from HCDs and metals.** Guard: require several
  crossing sightlines (arXiv:2004.01448, Sect. 5.1) [src].
- **Noise-biased amplitudes.** Wiener (and TARDIS) maps shrink fluctuations;
  corrections are linear fits on mocks (arXiv:1903.09049, App. C; LATIS
  Table 3; arXiv:2102.12306, Sect. III.2) [src]. ORCA's authors do not apply
  the linear correction because it pushes more voxels above F = 1 [src:
  same].
- **Edges and chunking.** LATIS excludes 4 h⁻¹ cMpc from the boundary when
  normalising; Stripe 82 overlaps chunks by L_⊥; TARDIS overlaps subvolumes
  and keeps data away from periodic edges, checked on mocks
  (arXiv:2510.08815; arXiv:2004.01448; arXiv:2109.09660) [src].
- **Coordinate approximations.** Parallel sightlines or a fixed H(z) are
  harmless for local structure finding but bias any large-scale distance
  measurement (arXiv:2004.01448, Sect. 3; arXiv:1710.02894, Sect. IV) [src].
- **FGPA truth.** Every mock above and the TARDIS forward model use the
  FGPA. Hydrodynamical simulations show that it describes low densities well
  but breaks at high density because of feedback and non-linear
  hydrodynamics, a difference CLAMATO-like data could not yet detect
  (arXiv:2201.10169, abstract) [src]. Protocluster and void calibrations at
  the dense end therefore carry a model error (see also the protocluster
  without absorption in `systematics.md#tomography-specific`).
- **Missing contaminants in mocks.** The Stripe 82 mocks contain no BALs
  (arXiv:2004.01448, Sect. 4.1) [src].

## Reading list
<!-- key: reading-list -->

- Foundation: Stark et al. 2014, arXiv:1412.1507 — Wiener-filter implementation (dachshund), protocluster finder and mock-survey design.
- Foundation: Lee et al. 2014, arXiv:1309.1477 — sightline-density and S/N requirements (in L2).
- Method and data: Lee et al. 2018, arXiv:1710.02894 — CLAMATO pixel selection, prior parameters, map variance, S/N^wiener.
- Method: Krolewski et al. 2018, arXiv:1710.02612 — SO void finder calibrated on Nyx; purity, completeness, continuum error.
- Application: Ravoux et al. 2020, arXiv:2004.01448 — wide-area map: parameter choices at 13 h⁻¹Mpc, mocks, voids and overdensities.
- Method: Horowitz et al. 2019, arXiv:1903.09049 — TARDIS forward-model reconstruction and its comparison with the Wiener filter.
- Application: Horowitz et al. 2022, arXiv:2109.09660 — TARDIS on CLAMATO DR2 with zCOSMOS; WF versus TARDIS on data.
- Method: Li et al. 2021, arXiv:2102.12306 — ORCA, a constrained flux reconstruction outperforming the Wiener filter on mocks.
- Data: Newman et al. 2025, arXiv:2510.08815 — LATIS maps, mock maps and the conditional-expectation calibration.
- Critique: Kooistra et al. 2022, arXiv:2201.10169 — where the FGPA behind all mocks and forward models fails.

## Not verified
<!-- key: not-verified -->

- The comparison of reconstruction methods by Müller et al. 2020, the
  Bayesian forward models of Porqueres et al. 2019 and the VAE reconstruction
  of Maitra et al. 2025: known only through the review (arXiv:2605.22489,
  Sect. 0.6.4), not identified or read.
- The LATIS Wiener-filter covariance (in an earlier LATIS paper, Sect. 8.2,
  not read) and the Stripe 82 delta extraction (its Sect. 2, not read).
- The Stark et al. void-finder paper cited by arXiv:1710.02612 (not
  identified); the TARDIS joint galaxy reconstruction paper (title seen in a
  search, not read).
- The reconstruction method behind the WEAVE-QSO forecast (arXiv:2201.02606).
