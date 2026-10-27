# Lyα tomography: maps, voids and protoclusters — cosmo-lyman-alpha dossier

Scope: how a 3D Lyα tomographic map is made from sightline pixels (pixel
selection, coordinates, Wiener-filter covariance, noise floor, solver, map
variance), how it is validated on mocks, how voids and protoclusters are found
in it and calibrated, and how the Wiener filter compares with non-parametric,
constrained (ORCA), forward-model (TARDIS, Bayesian HMC) and learned
reconstructions; the void–forest RSD fit itself is left to the sibling dossier.
Snapshot: 2026-10-20.
From: Tomography survey groups (CLAMATO, arXiv:1710.02894; LATIS,
arXiv:2002.10676; Stripe 82 eBOSS map, arXiv:2004.01448).

Already in L2, not repeated here: the survey list with areas, sightline
densities and map resolutions (`surveys-and-data.md#tomography-surveys`); the
origins of the method (Pichon et al. 2001, Caucci et al. 2008), the sightline
requirements of Lee et al. 2014 and the two regimes
(`physics-and-methods.md#tomography-and-voids`); the void, map and
cross-correlation results (`results.md#tomography-voids-and-cross-correlations`);
the tomography systematics list (`systematics.md#tomography-specific`); the
open questions (`open-questions.md#tomography-what-cosmology-can-it-deliver`).
The void–forest model, its β and the "tomographic effect" correction are in
`cosmo-beyond-two-point/deep/void-galaxy-rsd-ap.md`.

Notation. δ_F = F/⟨F(z)⟩ − 1 the flux contrast of a pixel, F = S/C the
continuum-normalised spectrum (S flux, C continuum), ⟨F⟩ the mean
transmission (arXiv:2002.10676, Eq. 1); δ_F^rec the reconstructed map;
⟨d_⊥⟩ the mean transverse separation between sightlines at a given redshift;
L_⊥, L_∥ (written l_⊥, l_∥ or σ_⊥, σ_∥ in some papers) the transverse and
line-of-sight correlation lengths of the Wiener prior; σ_F² its amplitude; N
the noise covariance and σ_N,i (or n_i, σ_δ) the pixel noise; σ_map a map's
standard deviation; ρ̄ the mean matter density; M_desc the z = 0 mass of the
most massive descendant halo. Positive δ_F means low density. CLAMATO
notation (arXiv:1710.02894) is followed.

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
  because CLAMATO is in the ⟨d_⊥⟩ ≳ 1.5 h⁻¹Mpc shot-noise-dominated regime (arXiv:1710.02894) [src: Sect. IV].
- Continua: mean-flux-regulated PCA for quasars over 1041–1185 Å; a fixed
  galaxy template over 1040–1195 Å for galaxies, with ± 7.5 Å (observed)
  masks around N II 1084, N I 1134, C III 1176 and Si II 1190, 1193. ⟨F⟩(z)
  from Faucher-Giguère et al. Continuum errors ~10% rms at S/N ~ 2 per pixel, ~4% at S/N ~ 10 (arXiv:1710.02894) [src: Sect. IV].
- Result: 240 spectra; projected density 1455 deg⁻², but the differential
  density averaged over the map is 866 deg⁻² (⟨d_⊥⟩ = 2.35 h⁻¹Mpc), 673 and
  451 deg⁻² at the two redshift ends, peak 1099 deg⁻² at z = 2.32. The
  authors stress that a projected density over all redshifts (quoted as
  16 deg⁻² for BOSS) overstates the density at one redshift (9 deg⁻² peak for BOSS) (arXiv:1710.02894) [src: Sect. IV].

LATIS (arXiv:2002.10676) [src: Sects. VIII.1–VIII.2]:

- Sightlines whose forest overlaps z_Lyα = 2.2–2.8, with high-confidence
  redshifts: 1071 (98% LBGs), 1850 deg⁻²; ⟨d_⊥⟩ = 70.6 n^(−1/2) h⁻¹ cMpc at
  z = 2.5 for n sightlines per deg², ≃ 2.5 h⁻¹ cMpc over z = 2.2–2.6 (arXiv:2002.10676) [src: Sects. VIII.1–VIII.2].
- The map stops at z = 2.8, where ⟨d_⊥⟩ ≈ 4 h⁻¹ cMpc, "the maximum useful
  value based on the simulations by Stark et al." Median CNR 1.7–2.7 per pixel (arXiv:2002.10676) [src: Sects. VIII.1–VIII.2].
- σ_δ is random noise and continuum uncertainty in quadrature; the data
  release feeds this σ_tot to the same code (arXiv:2510.08815, Sect. VI.1)
  [src].

### Step 2. Choose the map coordinates
<!-- key: step-2-choose-the-map-coordinates -->

| Analysis | Coordinates and grid | Stated reason or cost | Place read |
|---|---|---|---|
| Keck pilot map (Lee et al. 2014, arXiv:1409.5632) | fixed dχ/dz at z = 2.325; (0.5 h⁻¹Mpc)³ cells; 6 × 14 × 230 h⁻¹Mpc | "avoids a flared map geometry"; small effect over the limited z range | Sect. III |
| CLAMATO DR1 | fixed H(z) at ⟨z⟩ = 2.30, one-to-one (RA, Dec) ↔ (x, y); 60 × 48 × 876 cells of 0.5 h⁻¹Mpc | comparisons with coeval galaxies; evolving H(z) changed the void analysis negligibly; "more detailed cosmological analyses ... would tend to directly use the pixel data" | arXiv:1710.02894, Sect. IV |
| LATIS | redshift-dependent radial and transverse comoving distances, so sightlines flare outward; (1 h⁻¹ cMpc)³ voxels; maps in velocity (redshift) space, no peculiar-velocity correction | enough to compare with galaxies; transverse area not fully sampled at the low-z end; 3.96 × 10⁶ h⁻³ cMpc³ inside the sightlines in the data release | arXiv:2002.10676, Sect. VIII.2; arXiv:2510.08815, Sect. VI.1, Eq. 2 |
| eBOSS Stripe 82 | sightlines treated as parallel, transverse distances at z = 2.65; ~1 h⁻¹Mpc pixels over 0.94 h⁻³Gpc³ | few-percent errors along Dec; along the 88° RA direction the approximation "does not hold at all", so the map "is not adapted for studies on large-scale distances" | arXiv:2004.01448, Sect. 3 |

### Step 3. Wiener-filter the pixels
<!-- key: step-3-wiener-filter-the-pixels -->

The map is the Wiener (minimum-variance linear) estimate

    δ_F^rec = C_MD · (C_DD + N)⁻¹ · δ_F                     (arXiv:1710.02894, Eq. 2)

with a Gaussian signal covariance between points r_1, r_2

    C(r_1, r_2) = σ_F² exp[−Δr_∥²/(2L_∥²)] exp[−Δr_⊥²/(2L_⊥²)]   (Eq. 3)

and diagonal N_ii = σ_N,i². Stark et al. (2014, arXiv:1412.1507) write the
same operator as L = S_mp (S_pp + N)⁻¹ (m map, p pixel coordinates; their
Eqs. 1–2), "the minimum variance, unbiased linear estimator of the field
(under the assumption of a normal distribution)", following Caucci et al.
2008; they point to Pichon et al. for a more general method and to Cisewski
et al. for a non-parametric one, and find the reconstruction "not sensitive
to the form assumed" for the covariance [src: Sect. IV]. When field and noise
are Gaussian the Wiener filter "can be shown to correspond to the maximum a
posteriori estimate in certain Bayesian approaches" (Pichon et al., as
summarised in arXiv:2002.10676, Sect. VIII.2) [sec]. The Gaussian form "was
found by Stark et al. to be a reasonable approximation to the true
correlation function" (arXiv:1710.02894, Sect. IV) [src].

Solver (dachshund; arXiv:1412.1507, App. A.3) [src]: Jacobi-preconditioned
conjugate gradient, needing only products of A = S_pp + N with a vector, so
A is never stored: memory ~50 MB instead of ~8 TB for N_pix = 10⁶. Against a
direct Cholesky solve on 4000 pixels, the maximum PCG error relative to the
map noise was 30, 4.5, 0.47, 0.059 for tolerances 1, 0.1, 0.01, 10⁻³, so 0.01
is "a conservative choice". Masked pixels (n = ∞) are handled by the form
m = S_mp w (w S_pp w + I)⁻¹ w d with w = n⁻¹ (Eq. A1). CLAMATO and LATIS use
this code, as does the Stripe 82 map (row below); CLAMATO ran it at tolerance
10⁻³ in ~1000 s on one laptop core for 64,332 (DR1) or 84,608 (DR2) pixels
[src: arXiv:1710.02894, Sect. IV; arXiv:2109.09660, Sect. IV.2;
arXiv:2002.10676, Sect. VIII.2].

| Analysis | L_⊥ | L_∥ | σ_F² | Noise floor | Place read |
|---|---|---|---|---|---|
| Keck pilot map | 3.5 h⁻¹Mpc (⟨d_⊥⟩ ≈ 2.3) | 2.7 h⁻¹Mpc | written σ_F = 0.8 | — | arXiv:1409.5632, Sect. III |
| CLAMATO DR1 and DR2 | 2.5 h⁻¹Mpc | 2.0 h⁻¹Mpc | 0.05 | σ_N,i ≥ 0.2 | arXiv:1710.02894, Sect. IV; arXiv:2109.09660, Sect. IV.2 |
| LATIS | 2.5 h⁻¹ cMpc | σ_∥² = σ_⊥² − σ_inst², σ_inst = 1.4 h⁻¹ cMpc | 0.05 | σ_δ > 0.2 | arXiv:2002.10676, Sect. VIII.2 |
| eBOSS Stripe 82 | 13 h⁻¹Mpc | 13 h⁻¹Mpc | 0.01 | n_min = 0.1 (6.3% of pixels) | arXiv:2004.01448, Sect. 3 |

Reasons given (places as in the table) [src, except the first]. Caucci et
al. suggested L_⊥ ≈ ⟨d_⊥⟩, which suppresses structure below the sightline
separation (as cited by the pilot map and LATIS) [sec]. The pilot map (arXiv:1409.5632) took L_⊥ = 3.5 > ⟨d_⊥⟩ as "a conservative choice taking into account the low-S/N"
of its spectra, L_∥ as the resolution element, and calls the choice
"somewhat arbitrary since small changes do not qualitatively change the
resulting map features". CLAMATO's values (arXiv:1710.02894) were "approximately optimal" on
Stark et al. mocks, with L_∥² ≈ L_⊥² − σ_lsf² to make the kernel isotropic
after the spectrograph smoothing; LATIS adopts them to compare with CLAMATO
where they overlap. The 0.2 floor stops a few bright quasars with S/N
> 10× the mean from dominating (arXiv:1710.02894, Sect. IV). The 13 h⁻¹Mpc map (arXiv:2004.01448) sets L_∥ = L_⊥, a maximal contrast of 1 as in
CLAMATO, and a lower floor against numerical divergence.

Post-smoothing. Krolewski et al. apply no extra smoothing to the CLAMATO map
for void finding, "following Stark et al." (arXiv:1710.02612, Sect. II)
[src]. LATIS smooths isotropically (σ_kern = 2 h⁻¹ cMpc for display, 4 for
quantitative work) and applies a calibration factor (Step 5)
(arXiv:2002.10676, Sect. VIII.2) [src]. The data
release maps are δ_F/σ_map after 4 h⁻¹ cMpc smoothing, σ_map computed
excluding voxels within 4 h⁻¹ cMpc of an edge: σ_map = 0.0496, 0.0476,
0.0458 in D1, D2, D4 (arXiv:2510.08815, Sect. VI.1) [src].

### Step 4. Attach an uncertainty to the map
<!-- key: step-4-attach-an-uncertainty-to-the-map -->

- **Analytic Wiener variance** (CLAMATO). Var(δ_F^rec) = C_MD (C_DD + N)⁻¹
  C_DM (arXiv:1710.02894, Eq. 4), a factor N_pix more expensive than the map.
  It contains intrinsic forest variance, pixel noise and sampling;
  subtracting the intrinsic variance Var^intr measured on simulations binned
  and smoothed like the map gives a global
  S/N^wiener = sqrt{ Var^intr / (⟨Var(δ_F^rec)⟩ − Var^intr) } (Eq. 5),
  ≈ 0.65 per 0.5 h⁻¹Mpc voxel for DR1, rising to ≈ 1.8, 3.4, 5.2 over
  top-hats of 2, 3, 4 h⁻¹Mpc (⟨Var⟩ = 0.0219, Var^intr = 0.00654) [src:
  Sect. VI.1].
- **Mock-survey variance** (LATIS). S/N_ε² = Var(δ_F^true) /
  Var(δ_F^true − δ_F^rec), both fields smoothed at 4 h⁻¹ cMpc, the
  denominator evaluated per voxel over 90 mock surveys (arXiv:2002.10676,
  Eq. 3) [src: Sect. VIII.3]: ≃ 1.8 over z = 2.2–2.6 (noise about half the
  intrinsic fluctuation), against ≈ 2–2.5 called good by Lee et al. (as cited
  there). Recomputed this way with a revised noise model, CLAMATO DR1 drops
  ≃ 20%, and LATIS is ≃ 10% below it over a 4.4× larger volume [src: same].

### Step 5. Validate on mock surveys built like the data
<!-- key: step-5-validate-on-mock-surveys-built-like-the -->

Sources by column, as in the last row: CLAMATO: arXiv:1409.5632, Sect. III; arXiv:1710.02612, Sect. IV.1; LATIS: arXiv:2002.10676, Sect. VIII.3; arXiv:2510.08815, Sect. VI.2, Table 3; eBOSS Stripe 82: arXiv:2004.01448, Sects. 4.1–4.2.

| Item | CLAMATO | LATIS | eBOSS Stripe 82 |
|---|---|---|---|
| Truth | pilot: simulation mocks with identical sightline layout, resolution and S/N; voids: Nyx 100 h⁻¹Mpc hydrodynamical box and a 256 h⁻¹Mpc N-body box | FGPA on MDPL2 particles at z = 2.535, CIC on a 0.25 h⁻¹ cMpc grid, temperature–density relation from Rudie et al.; P1D matches BOSS above k⁻¹ ~ 50 km s⁻¹ | Gaussian random field with FGPA (Eq. 6), small-scale power tuned to P1D |
| Survey effects | 7% rms random continuum errors (pilot); CLAMATO-like spacing, noise, continuum error, mean flux rescaled to ⟨F(z = 2.3)⟩ (voids) | 90 sub-volumes with the exact sightline layout, smoothing, sampling, per-sightline noise, continuum errors drawn from the CNR (data release: 100 sub-volumes per field, 300 mock maps; δ_true from a 0.25 h⁻¹Mpc grid smoothed at 4 h⁻¹Mpc) | DR16 quasar density and n(z); continua, metals and HCDs from quickquasars; no BALs |
| Metric | 1-point PDF of the map; void purity and completeness against the redshift-space density | linear fit of δ_rec on δ_true; conditional expectations ⟨δ_true|δ_rec⟩, ⟨δ_rec|δ_true⟩ | Pearson r with δ_m smoothed at 8 h⁻¹Mpc |
| Result | PDF of the data differs from one mock; 24 independent volumes show a scatter that covers part of the gap (cosmic variance), and DM-only simulations do not give the right PDF | slopes 0.69, 0.77, 0.85 at σ = 2, 3, 4 h⁻¹ cMpc (COSMOS; 0.73, 0.86, 0.98 in D1); ⟨δ_true|δ_rec⟩ close to 1:1, ⟨δ_rec|δ_true⟩ = 0.544 δ_true + … | r = −0.34 over z = 2.1–2.7 |
| Place read | arXiv:1409.5632, Sect. III; arXiv:1710.02612, Sect. IV.1 | arXiv:2002.10676, Sect. VIII.3; arXiv:2510.08815, Sect. VI.2, Table 3 | arXiv:2004.01448, Sects. 4.1–4.2 |

The LATIS slopes are below one "primarily because of reconstruction errors
that scatter δ_F^rec away from the peak"; multiplying by the least-squares
slope minimises Var(δ_F^rec − δ_F^true) at fixed δ_F^rec, and cancels in any
map normalised by σ_map; the map histograms agree with the mocks, with "a
slight deficit of voxels with high δ_F" (arXiv:2002.10676, Sect. VIII.3)
[src]. Since LATIS calibrates protocluster masses on mock maps, "all that
matters is that the mock observations are faithful" (arXiv:2510.08815,
Sect. VI.2) [src]. Two-survey check, "a first comparison of Mpc-resolution
tomographic maps produced by independent groups": in the CLAMATO–LATIS
overlap (z = 2.2–2.55) three of four strong overdensities agree in position
and morphology, two of three LATIS voids appear in CLAMATO at lower
significance, and one CLAMATO void is absent from LATIS for no clear reason
(arXiv:2002.10676, Sect. IX.1) [src].

### Step 6. Find voids
<!-- key: step-6-find-voids -->

Spherical-underdensity finder (Stark et al. 2015, arXiv:1504.03290)
[src: Sect. 2.2]: select grid points below a density threshold, grow a sphere
around each until the mean enclosed density reaches a target, keep the
largest sphere where voids overlap, discard r < 2 h⁻¹Mpc. On density,
ρ_thresh = 0.2 ρ̄ (central density at shell-crossing) and ρ̄_enc = 0.4 ρ̄ so
that spheres reach the visible void edges; the catalogue is "not very
sensitive to these settings", though radii scale with the target; 16,167
voids fill 15% of the volume. On the flux: δ_F ≥ 0.224, average 0.167, to
match the density catalogue; the flux–density mapping "evolves quickly with
redshift", so these values change with redshift and UV background
[src: Sect. 4.1].

Why spheres rather than watersheds (same, Sect. 2.2) [src]: on density the
large voids of both finders agree, but watershed voids have complex shapes
and centres several Mpc away; and "the non-trivial noise we expect in the
maps ... might artificially combine or split watershed regions, whereas the
spherical average in the SO method will be less affected". Krolewski et al.
give the same reason for CLAMATO (arXiv:1710.02612, Sect. IV.1) [src].

Sources by column, as in the last row: Mock maps (Stark et al. 2015): arXiv:1504.03290, Sect. 4.2, Table 1; CLAMATO (Krolewski et al. 2018): arXiv:1710.02612, Sect. IV; eBOSS Stripe 82: arXiv:2004.01448, Sect. 5.2.

| Setting | Mock maps (Stark et al. 2015) | CLAMATO (Krolewski et al. 2018) | eBOSS Stripe 82 |
|---|---|---|---|
| Map | ⟨d_⊥⟩ = 2.5, 4, 6 h⁻¹Mpc ("hires", "midres", "lores") | 2.5 h⁻¹Mpc, unsmoothed | 13 h⁻¹Mpc |
| Thresholds | δ_F ≥ 0.224, average 0.167 (as on the true flux; changes > 0.01 did no better) | δ_F^rec > 0.220, average 0.175 | δ_th = 0.14, δ_av = 0.12 |
| How fixed | match the density catalogue's count and radii | reproduce the void volume fraction of the redshift-space density field (SO thresholds 0.15 ρ̄ and 0.3 ρ̄; 0.173–0.180) on mock reconstructions | scanned on mocks until ~25 h⁻¹Mpc voids are stable |
| Minimum radius | 2 h⁻¹Mpc | 2 h⁻¹Mpc; 5 h⁻¹Mpc for profiles | 7 h⁻¹Mpc, plus sightline-coverage cuts |
| Outcome | matches for r ≥ 6 h⁻¹Mpc: 66% (hires), 48% (midres); lores 48.9% for r ≥ 8 h⁻¹Mpc; random catalogues match 2–3% | 355 voids (48 with r ≥ 5); volume fraction 19.5% in data, 18.0–18.2% in mocks | filling factor 14% |
| Place read | arXiv:1504.03290, Sect. 4.2, Table 1 | arXiv:1710.02612, Sect. IV | arXiv:2004.01448, Sect. 5.2 |

Stark et al. note that the volume overlap stays high even when matches fail,
so the poor matching is "more the fault of our simple void finding method
than the maps truly missing the voids", and that a finder using the map noise
estimate should do better (arXiv:1504.03290, Sect. 4.2) [src]. Reason the
thresholds must come from realistic mocks: the void fraction depends on the
mean flux and on continuum error, which acts as δ_cont F/⟨F⟩ and so matters
most at high transmission; with identical thresholds continuum error raises
the void fraction from 18% to 24% (arXiv:1710.02612, Sect. IV.1) [src].

### Step 7. Find protoclusters
<!-- key: step-7-find-protoclusters -->

Smooth and threshold (Stark et al. 2014, arXiv:1412.1507, Sect. V) [src]:
a 3D Gaussian of σ = 4 h⁻¹Mpc ("much like a matched filter"; 2 and 8 tried,
4 best), then δ_F < −3.5 σ of the field, best for > 3 × 10¹⁴ h⁻¹M☉
descendants; points within 4 h⁻¹Mpc merged, candidate = 4 h⁻¹Mpc sphere on
the minimum; on the ideal field 68 candidates (~10⁻³ of the volume), almost
all protoclusters (z = 0 mass > 10¹⁴ h⁻¹M☉), halo counts ~5× the field
median.

Sources by column, as in the last row: COSMOS map of Lee et al. 2016: arXiv:1509.02833, abstract; LATIS (Newman et al. 2025, after Qezlou et al. 2022): arXiv:2507.10948, Sects. III.1–III.2; arXiv:2112.03930, abstract; eBOSS Stripe 82: arXiv:2004.01448, Sect. 5.1.

| Setting | COSMOS map of Lee et al. 2016 | LATIS (Newman et al. 2025, after Qezlou et al. 2022) | eBOSS Stripe 82 |
|---|---|---|---|
| Map | 58 sightlines, ⟨d_⊥⟩ ~ 2.4 h⁻¹Mpc, effective σ_3d ≈ 3.5 h⁻¹Mpc | σ_kern = 4 h⁻¹ cMpc, a "rough matched filter" | 13 h⁻¹Mpc map, no extra smoothing |
| Selection | IGM overdensity at a known galaxy protocluster | δ_F/σ_map < −3 (as in CLAMATO work; Stark proposed < −3.5; Qezlou explored < −2.35); peaks closer than 4 h⁻¹ cMpc merged | watershed on δ_F < −3.5 σ̃_map, R_min = 7 h⁻¹Mpc, > 3 crossing sightlines |
| Mass | M_dm(z = 2.45) = (9 ± 4) × 10¹³ h⁻¹M☉ from matched simulations; M(z = 0) = (3 ± 2) × 10¹⁴ h⁻¹M☉ | M_desc per peak from IllustrisTNG-300 LATIS-like mocks; watershed boundaries (Qezlou) | mean matter contrast of mock candidates ⟨δ_M⟩ = 0.4 |
| Outcome | protocluster detected in absorption | 37 overdensities (20, 9, 8 in COSMOS, D1, D4), 4.0–7.1σ detections; expected 85% protoclusters, 98% protoclusters or protogroups | 9 mock candidates, mean radius 10.5 h⁻¹Mpc |
| Place read | arXiv:1509.02833, abstract | arXiv:2507.10948, Sects. III.1–III.2; arXiv:2112.03930, abstract | arXiv:2004.01448, Sect. 5.1 |

Purity and completeness (Qezlou et al. 2022, as quoted in arXiv:2507.10948,
Sect. III.1) [sec]: peaks with δ_F/σ_map below −3.5 have median M_desc = 10^14.6 M☉, 93%
protoclusters; −3.5 to −3.0, 10^14.4 M☉ and 81%; most failures are
progenitors of 10^13.5–14.0 M☉ groups. Completeness 10%, 50%, 90% is reached
at M_desc = 10^13.8, 10^14.6, 10^15.0 M☉ for a −2.35 cut and 10^14.2,
10^14.8, 10^15.1 M☉ for −3; noiseless surveys fare only slightly better.
Peak positions are uncertain by 2.7 h⁻¹ cMpc per sky coordinate and
1.5 h⁻¹ cMpc along the line of sight (arXiv:2507.10948, Sect. III.2) [src]. A forward model gives a sharper definition: TARDIS II
evolves the joint reconstruction to z = 0, giving "a rigorous definition of
'proto-cluster' as regions which will evolve into clusters"
(arXiv:2007.15994, abstract) [src].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Wiener filter, constrained flux reconstruction or forward model
<!-- key: wiener-filter-constrained-flux-reconstruction -->

- **Wiener filter (dachshund).** Linear, Gaussian prior with no explicit
  cosmology dependence; noise weighting and regularisation are its stated
  advantages, and where errors exceed the prior variance it "suppresses the
  signal in favor of the prior δ_F = 0" (arXiv:2002.10676, Sect. VIII.2)
  [src]. LATIS reconstructs the flux "rather than attempting to recover the
  underlying density field" (same) [src]. Cost: amplitudes shrink (Step 5),
  F can exceed 1, Gaussianity is assumed.
- **Non-parametric smoothing.** Local polynomial smoothing between the lines
  of sight, tested on simulations and applied to a BOSS region (Cisewski et
  al. 2014, arXiv:1401.1867) [src: abstract]; CLAMATO names it as the
  alternative to its Wiener filter (arXiv:1710.02894, Sect. IV) [src].
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
  match the CLAMATO δ_F^rec PDF (arXiv:2102.12306).
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
  calibrated on a separate volume. TARDIS II adds a galaxy survey: the forest
  reconstructs low densities and galaxies trace the peaks, and for the cosmic
  web the joint fit "is equivalent to a Lyman Alpha survey with significantly
  increased sight-line spacing" (wording of arXiv:2007.15994, abstract) [src].
- **TARDIS on data** (CLAMATO DR2, arXiv:2109.09660) [src: Sects. IV.3, V.2]:
  joint with zCOSMOS galaxies, chosen because it has a well-characterised
  selection function (~45% of galaxies in the volume); four overlapping
  128 h⁻¹Mpc subvolumes (15 h⁻¹Mpc radial overlap, data offset 10 h⁻¹Mpc from
  periodic edges), ~30 min on one GPU. The TARDIS-derived flux and the Wiener
  map correlate at Pearson 0.86, and the deformation-tensor classifications
  at 0.83. The authors read large differences, if found, as signs of
  departures from the FGPA such as cluster feedback.
- **Bayesian sampling (HMC).** A fully Bayesian forward model draws initial
  and evolved density fields and the 3D flow with Hamiltonian Monte Carlo; on
  simulated quasar spectra it recovers an unbiased mass distribution and the
  matter power at all scales, handles multi-modal IGM parameters, and gives
  cluster mass profiles (Porqueres et al. 2019, arXiv:1907.02973) [src:
  abstract].
- **Learned inverse map.** DeepCHART, a 3D variational autoencoder with a
  U-Net trained on hydrodynamical simulations, reaches a voxel Pearson ρ ≃ 0.77
  over 0.4 < Δ_DM < 15 (Δ_DM dark-matter density over its mean) for
  ⟨d_⊥⟩ = 2.4 h⁻¹ cMpc, S/N ≈ 2, R = 2500, and ρ ≃ 0.90 at ⟨d_⊥⟩ ≃ 1 h⁻¹ cMpc
  (Maitra et al. 2025, arXiv:2507.00135) [src: abstract]. A recent review
  groups all these routes under field-level inference (arXiv:2605.22489,
  Sect. 0.6.4) [src].
- **Single-sightline inversion** (a different problem): at high resolution,
  Gauss–Newton inversion is the most accurate at low S/N but the costliest
  and most assumption-laden of the methods compared on lognormal mocks
  (Müller et al. 2020, arXiv:2006.07162) [src: abstract].

### Smoothing lengths: tied to sightline spacing or isotropised
<!-- key: smoothing-lengths-tied-to-sightline-spacing-or -->

All maps set L_⊥ by ⟨d_⊥⟩ (Step 3). Along the line of sight CLAMATO and
LATIS keep L_∥ < L_⊥ so that the kernel is isotropic after instrumental
smoothing; the pilot map set L_∥ to the resolution element; the 13 h⁻¹Mpc map
sets L_∥ = L_⊥, far above it. Even with an isotropic filter, stacked mock voids in a
parallel-sightline map are elongated across the line of sight (axis ratio
1.37 ± 0.01, 1.33 with RSD switched off), mostly from the sightline geometry
(arXiv:2004.01448, Sect. 5.3) [src]; this geometric anisotropy is what the
void–forest RSD model must remove (sibling dossier). Narrow survey geometry
is a separate limit: deformation-tensor classification of the flux map
recovers 70% of the dark-matter web volume (99% within one eigenvalue), but
degrades unless the survey is ≳ 60 h⁻¹Mpc or ≳ 1 deg across (Lee & White
2016, arXiv:1603.04441) [src: abstract].

### Map statistics or pixel statistics
<!-- key: map-statistics-or-pixel-statistics -->

CLAMATO's authors state that detailed cosmological analyses would use the
pixels rather than the map (arXiv:1710.02894, Sect. IV) [src]; the
void–forest cross-correlation does so, with map voids and pixel δ_F (sibling
dossier). Map-level quantities (void sizes, protocluster masses, LATIS
conditional expectations) are calibrated only through mocks with the same
sightline pattern.

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Wiener prior (L_⊥, L_∥, σ_F²), floor | (2.5, 2.0 h⁻¹Mpc, 0.05), 0.2 | CLAMATO DR1, DR2; LATIS (σ_∥ from σ_inst = 1.4) | arXiv:1710.02894; arXiv:2002.10676 | Sect. IV; Sect. VIII.2 |
| Wiener prior | (3.5, 2.7 h⁻¹Mpc, σ_F = 0.8) | Keck pilot map | arXiv:1409.5632 | Sect. III |
| Pixel selection | ⟨CNR⟩ ≥ 1.2 in one z range (CLAMATO); median CNR 1.7–2.7 (LATIS) | — | arXiv:1710.02894; arXiv:2002.10676 | Sect. IV; Sect. VIII.1 |
| Sightline density | 866 deg⁻² mean, ⟨d_⊥⟩ = 2.35 h⁻¹Mpc (CLAMATO DR1); 1850 deg⁻², ⟨d_⊥⟩ ≃ 2.5 h⁻¹ cMpc (LATIS) | — | arXiv:1710.02894; arXiv:2002.10676 | Sect. IV; Sect. VIII.1 |
| Map S/N | S/N^wiener 0.65 per 0.5 h⁻¹Mpc voxel, 5.2 at 4 h⁻¹Mpc (CLAMATO DR1); S/N_ε ≃ 1.8 at 4 h⁻¹ cMpc (LATIS) | — | arXiv:1710.02894; arXiv:2002.10676 | Sect. VI.1; Sect. VIII.3 |
| Map shrinkage | slope 0.69, 0.77, 0.85 at σ = 2, 3, 4 h⁻¹ cMpc; ⟨δ_rec|δ_true⟩ slope 0.544 | LATIS mocks | arXiv:2002.10676; arXiv:2510.08815 | Sect. VIII.3; Table 3 |
| Void recovery | completeness and purity 30–45% at r ~ 6 h⁻¹Mpc; 40–45% of r ≥ 5 h⁻¹Mpc voids recovered (not 60%); match fraction ~5% at r ~ 2 h⁻¹Mpc | CLAMATO-like mocks | arXiv:1710.02612 | Sect. IV.1 |
| Effect of continuum error on voids | completeness and purity lower by 5–10 points; void fraction 18% → 24% at fixed thresholds | CLAMATO-like mocks | arXiv:1710.02612 | Sect. IV.1 |
| Void filling factor | 15% (density, simulation); 19.5% (CLAMATO data) | — | arXiv:1504.03290; arXiv:1710.02612 | Sect. 2.2; Sect. IV.2 |
| Protocluster threshold | −3.5 σ after 4 h⁻¹Mpc smoothing (Stark); δ_F/σ_map < −3 (LATIS catalogue) | — | arXiv:1412.1507; arXiv:2507.10948 | Sect. V; Sect. III.1 |
| Exposure scaling | t_exp ∝ SNR_min² ⟨d_⊥⟩^(−1.6), quoted from Lee et al. | mock-survey design | arXiv:1412.1507 | Sect. VI |
| TARDIS mock surveys | ⟨d_⊥⟩ = 3.7, 2.4, 1.0 h⁻¹Mpc (363, 863, 4970 deg⁻²) | DESI-like, CLAMATO/PFS-like, 30-m-like | arXiv:1903.09049 | Table 1 |
| WF vs TARDIS on data | Pearson 0.86 (flux), 0.83 (web classification) | CLAMATO DR2 | arXiv:2109.09660 | Sect. V.2 |
| ORCA vs WF | slope 0.677 vs 0.653, r 0.711 vs 0.680 | Nyx mocks | arXiv:2102.12306 | Sect. III.2 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Projected instead of differential sightline density.** Quoting the
  all-redshift density overstates the map resolution; CLAMATO 1455 versus
  866 deg⁻², BOSS 16 versus 9 deg⁻² (arXiv:1710.02894, Sect. IV) [src]. Test:
  plot ⟨d_⊥⟩(z) (CLAMATO Fig. 8; LATIS Fig. 20) and compare with L_⊥.
- **L_⊥ below ⟨d_⊥⟩.** Where the spacing grows past the prior length the map
  interpolates; LATIS stops at ⟨d_⊥⟩ ≈ 4 h⁻¹ cMpc (arXiv:2002.10676,
  Sect. VIII.1) [src], and its S/N_ε falls towards the back of the volume with
  the sightline density (same, Sect. VIII.3) [src].
- **Continuum error makes and erases voids.** It is correlated along a
  sightline, so it "will both create spurious voids and erase real voids"
  (arXiv:1710.02612, Sect. IV.1) [src]. Test: mocks with and without
  continuum error; thresholds valid "only ... to the data presented".
- **Map noise in the finder.** Noise scatters points across the SO threshold
  and biases the spherical averages; small voids are mostly lost, and in the
  ⟨d_⊥⟩ = 4 and 6 h⁻¹Mpc maps large voids (r ≥ 7 h⁻¹Mpc) are about doubled
  in number (arXiv:1504.03290, Sect. 4.2) [src].
- **Single opaque sightlines and contaminants.** A LATIS–CLAMATO mismatch was
  traced to a feature "enhanced by one sightline that is nearly opaque"
  (arXiv:2002.10676, Sect. IX.1) [src]; against residual HCDs and metals the
  Stripe 82 finder requires several crossing sightlines (arXiv:2004.01448,
  Sect. 5.1) [src].
- **Noise-biased amplitudes.** Wiener (and TARDIS) maps shrink fluctuations;
  corrections are linear fits on mocks (arXiv:1903.09049, App. C;
  arXiv:2002.10676, Sect. VIII.3; arXiv:2102.12306, Sect. III.2) [src]. ORCA's
  authors do not apply the linear correction because it pushes more voxels
  above F = 1 [src: same].
- **Edges and chunking.** LATIS drops voxels within 4 h⁻¹ cMpc of the
  boundary (arXiv:2002.10676, Sect. VIII.3); TARDIS overlaps subvolumes away
  from periodic edges (arXiv:2109.09660, Sect. IV.3); the Stripe 82 map is
  solved in chunks overlapping by L_⊥ (its Sect. 3) [src].
- **Coordinate approximations and small volumes.** A fixed dχ/dz or H(z), or
  parallel sightlines, is harmless locally but biases large-scale distances
  (Step 2 table) [src]. The map PDF scatters strongly between pilot-sized
  volumes (arXiv:1409.5632, Sect. III), and web classification needs
  ≳ 60 h⁻¹Mpc across (arXiv:1603.04441, abstract) [src].
- **FGPA truth.** Nearly every mock above and the TARDIS forward model use
  the FGPA. Hydrodynamical simulations show that it holds at low density but
  breaks at high density (feedback, non-linear hydrodynamics), a difference
  CLAMATO-like data could not yet detect (arXiv:2201.10169, abstract) [src].
  On dark-matter-only mocks it is adequate for protoclusters ≳ 10^14.2 M☉ but
  merges some lower-mass structures with neighbours (arXiv:2112.03930,
  abstract) [src]. See also `systematics.md#tomography-specific`.

## Reading list
<!-- key: reading-list -->

- Foundation: Lee et al. 2014, arXiv:1309.1477 — sightline-density and S/N requirements (in L2).
- Foundation and code: Stark et al. 2014, arXiv:1412.1507 — Wiener filter as used (dachshund, PCG, masking), protocluster finder, mock-survey design.
- Method: Stark et al. 2015, arXiv:1504.03290 — the SO void finder, its parameters, and its performance at three sightline spacings.
- Data: Lee et al. 2018, arXiv:1710.02894 — CLAMATO pixel selection, prior parameters, map variance, S/N^wiener.
- Data: Newman et al. 2020, arXiv:2002.10676 — LATIS map construction, mock calibration slopes, S/N_ε, first two-survey map comparison.
- Method: Krolewski et al. 2018, arXiv:1710.02612 — SO voids in CLAMATO calibrated on Nyx; purity, completeness, continuum error.
- Method and data: Newman et al. 2025, arXiv:2507.10948 — IGM-selected protocluster catalogue, thresholds, purity and completeness.
- Method: Horowitz et al. 2019, arXiv:1903.09049 — TARDIS forward-model reconstruction and its comparison with the Wiener filter; applied to CLAMATO DR2 in arXiv:2109.09660.
- Method: Li et al. 2021, arXiv:2102.12306 — ORCA, a constrained flux reconstruction outperforming the Wiener filter on mocks.
- Application: Ravoux et al. 2020, arXiv:2004.01448 [src: abstract] — the wide-area, quasar-based regime at 13 h⁻¹Mpc.
- Critique: Kooistra et al. 2022, arXiv:2201.10169 — where the FGPA behind the mocks and forward models fails.

## Not verified
<!-- key: not-verified -->

- Qezlou et al. 2022 (body not rendered; numbers via arXiv:2507.10948 [sec])
  and Lee et al. 2016 (abstract only; the −3 CLAMATO threshold is from the same).
- arXiv:1907.02973, 2007.15994, 2507.00135, 1401.1867, 2006.07162: abstracts
  only; no same-data comparison of these with the Wiener filter was read.
  Pichon et al. and Caucci et al. are read through the papers citing them.
- Stark et al. 2014 App. A.2 and A.4; the Ozbek et al. BOSS tomography named
  in arXiv:1710.02894 (not identified); the Stripe 82 delta extraction; the
  reconstruction behind the WEAVE-QSO forecast (arXiv:2201.02606).
