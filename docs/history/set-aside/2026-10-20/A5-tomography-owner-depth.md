# Set aside on 2026-10-20 (plan item A.5)

Generality audit, correction 5 (`docs/history/tests/2026-10-20-generality-audit.md`),
plan `docs/plans/2026-10-20-plan.md` item A.5: the tomography dossier now
leads each step with the CLAMATO and LATIS programmes and the method papers
(Stark et al. 2014, 2015; Krolewski et al. 2018; Qezlou et al. 2022; TARDIS,
ORCA), with the eBOSS Stripe 82 map (arXiv:2004.01448) kept as one
application among peers.

For the owner's personal layer. The text below is verbatim from
`skills/cosmo-lyman-alpha/deep/tomography-voids.md` as it stood before the
rebalancing (snapshot 2026-10-19), under its original headings: every
passage that held a statement specific to the owner's analysis and was
removed, shortened or reworded. The CLAMATO, LATIS and Stark et al.
statements inside these passages are kept in the new dossier; they are
copied here only because they share a table or paragraph. Every statement
was verified at source when the dossier was written.

## Step 2. Choose the map coordinates

```
| Choice | CLAMATO DR1 | eBOSS Stripe 82 | LATIS |
|---|---|---|---|
| Coordinates | fixed H(z) at ⟨z⟩ = 2.30: one-to-one (RA, Dec) ↔ (x, y) | all sightlines parallel, transverse distances at z = 2.65; ΛCDM with Ω_m = 0.3147, h-free units | (X, Y, Z) from D_C(z) per pixel, so sightlines flare outward |
| Grid | 60 × 48 × 876 cells of 0.5 h⁻¹Mpc; 30 × 24 h⁻¹Mpc transverse | 5856 × 180 × 834 pixels, ~1 h⁻¹Mpc; 0.94 h⁻³Gpc³ | (1 h⁻¹ cMpc)³ voxels; 3.96 × 10⁶ h⁻³ cMpc³ inside the sightlines |
| Stated reason or cost | preserves comparisons with coeval galaxies; a run with evolving H(z) changed the void analysis negligibly; "more detailed cosmological analyses ... would tend to directly use the pixel data" | errors of a few percent along Dec over z = 2.1–3.2; along the 88° RA direction the approximation "does not hold at all", so the map "is not adapted for studies on large-scale distances" | transverse area not fully sampled at the low-z end |
| Place read | arXiv:1710.02894, Sect. IV | arXiv:2004.01448, Sect. 3 | arXiv:2510.08815, Sect. VI.1, Eq. 2 |
```

## Step 3. Wiener-filter the pixels

```
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
```

## Step 5. Validate on mock surveys built like the data

```
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
```

## Step 6. Find voids

```
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
```

## Step 7. Find protoclusters

```
| Setting | Simulation study (arXiv:1412.1507, Sect. V) | Stripe 82 (arXiv:2004.01448, Sect. 5.1) |
|---|---|---|
| Pre-smoothing | 3D Gaussian σ = 4 h⁻¹Mpc ("much like a matched filter"; 2 and 8 tried, 4 best) | none: the 13 h⁻¹Mpc map smoothing already exceeds protocluster size |
| Threshold | δ_F < −3.5 σ of the field, best for > 3 × 10¹⁴ h⁻¹M☉ descendants | watershed on δ_F < −3.5 σ̃_map |
| Grouping and size | merge points within 4 h⁻¹Mpc; candidate = 4 h⁻¹Mpc sphere on the minimum | R = (3 N_pix V_pix/4π)^(1/3), R_min = 7 h⁻¹Mpc |
| Spurious-detection guard | — | crossing sightline length > 3 × diameter (> 3 sightlines), against residual HCDs and metals |
| Outcome on simulations | 68 candidates (~10⁻³ of the volume) in the ideal field, almost all protoclusters (z = 0 mass > 10¹⁴ h⁻¹M☉), halo counts ~5× the field median | 9 mock candidates, mean radius 10.5 h⁻¹Mpc, all with positive mean matter contrast, ⟨δ_M⟩ = 0.4 |

The Stripe 82 authors stress that interpreting their overdensities as
protoclusters "would require dedicated N-body simulations" [src: Sect. 5.1].
```

## Wiener filter, constrained flux reconstruction or forward model

```
- **Wiener filter (dachshund).** Linear, Gaussian prior with no explicit
  cosmology dependence; "technical simplicity" and inclusion of instrumental
  properties are the reasons given (arXiv:2004.01448, Sect. 3) [src]. Cost:
  the map is biased towards zero by noise, can exceed F = 1, and assumes
  Gaussianity, which suits a 13 h⁻¹Mpc map whose fluctuations are "nearly
  Gaussian" (same) [src] better than a 2 h⁻¹Mpc one.
```

## Smoothing lengths: tied to sightline spacing or isotropised

```
Both conventions set L_⊥ by ⟨d_⊥⟩. They differ along the line of sight:
CLAMATO keeps L_∥ < L_⊥ to make the effective kernel isotropic after the
instrumental smoothing; Stripe 82 sets L_∥ = L_⊥ far above the resolution.
Even with an isotropic filter the Stripe 82 stacked mock void is elongated
across the line of sight, axis ratio d_yz = 1.37 ± 0.01 (d_xy = 0.98 ±
0.005); switching off RSD in the mock gives 1.33, and subsampling the
sightlines reduces it, so most of the anisotropy comes from the parallel
sightline geometry (arXiv:2004.01448, Sect. 5.3) [src]. This is the geometric
anisotropy that the void–forest RSD model must remove (sibling dossier).
```

## Map statistics or pixel statistics

```
CLAMATO's authors state that detailed cosmological analyses would use the
pixels rather than the map (arXiv:1710.02894, Sect. IV) [src]; the Stripe 82
void–forest measurement does this: voids from the map, correlation with the
pixel δ_F (`cosmo-beyond-two-point/deep/void-galaxy-rsd-ap.md`). Map-level
quantities (void sizes, protocluster masses, LATIS conditional expectations)
are calibrated only through mocks with the same sightline pattern.
```

## Numbers

```
| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Wiener prior | (13, 13 h⁻¹Mpc, 0.01) | eBOSS Stripe 82 | arXiv:2004.01448 | Sect. 3 |
| Noise floor | σ_N ≥ 0.2 (CLAMATO); n_min = 0.1 (Stripe 82) | — | arXiv:1710.02894; arXiv:2004.01448 | Sect. IV; Sect. 3 |
| Map–matter correlation | r = −0.34 (δ_m smoothed 8 h⁻¹Mpc, z = 2.1–2.7) | Stripe 82 mocks | arXiv:2004.01448 | Sect. 4.2 |
| Void filling factor | 19.5% (CLAMATO data); 14% (Stripe 82) | — | arXiv:1710.02612; arXiv:2004.01448 | Sect. IV.2; Sect. 5.2 |
| Stacked void axis ratio | 1.37 ± 0.01 (1.33 without RSD) | Stripe 82 mocks | arXiv:2004.01448 | Sect. 5.3 |
```

## What goes wrong

```
- **Projected instead of differential sightline density.** Quoting the
  all-redshift density overstates the map resolution; CLAMATO 1455 versus
  866 deg⁻², BOSS 16 versus 9 deg⁻² (arXiv:1710.02894, Sect. IV) [src]. Test:
  plot ⟨d_⊥⟩(z) (Stripe 82 Fig. 2; CLAMATO Fig. 8) and compare with L_⊥.
- **L_⊥ below ⟨d_⊥⟩.** At z > 2.8 the Stripe 82 L_⊥ is below the
  sightline spacing, "a fact which must be considered when interpreting the
  map" (arXiv:2004.01448, Sect. 3) [src]; structures there are interpolation.
- **Spurious overdensities from HCDs and metals.** Guard: require several
  crossing sightlines (arXiv:2004.01448, Sect. 5.1) [src].
- **Edges and chunking.** LATIS excludes 4 h⁻¹ cMpc from the boundary when
  normalising; Stripe 82 overlaps chunks by L_⊥; TARDIS overlaps subvolumes
  and keeps data away from periodic edges, checked on mocks
  (arXiv:2510.08815; arXiv:2004.01448; arXiv:2109.09660) [src].
- **Coordinate approximations.** Parallel sightlines or a fixed H(z) are
  harmless for local structure finding but bias any large-scale distance
  measurement (arXiv:2004.01448, Sect. 3; arXiv:1710.02894, Sect. IV) [src].
- **Missing contaminants in mocks.** The Stripe 82 mocks contain no BALs
  (arXiv:2004.01448, Sect. 4.1) [src].
```

## Reading list

```
- Application: Ravoux et al. 2020, arXiv:2004.01448 — wide-area map: parameter choices at 13 h⁻¹Mpc, mocks, voids and overdensities.
```
