# Lyα synthetic data: how mocks are built, tuned and contaminated — cosmo-lyman-alpha dossier

Scope: how the 3D Lyα mocks used to validate BAO and full-shape analyses are
produced (density field, skewers, small-scale power, optical depth, redshift
space), which statistics they are tuned to and how, how continua,
contaminants, instrument and redshift errors are added, what each mock family
does and does not contain, and how the catalogue-level AP blinding scheme is
applied; the validation thresholds and mock-based results are in L2.
Snapshot: 2026-10-19.
From: DESI 2024 IV (arXiv:2404.03001), Sect. 6.

Already in L2, not repeated here: the list of mock families with one line each
(`surveys-and-data.md#fast-mocks-for-3d-analyses`); the σ/3 validation
thresholds, mock biases, splits and variations of DR1 and DR2 BAO and full
shape (`systematics.md#g1-desi-dr2-lyalpha-bao-arxiv-2503-14739-mocks`,
`systematics.md#g2-desi-dr1-lyalpha-bao-arxiv-2404-03001`,
`systematics.md#g6-desi-dr1-lyalpha-full-shape-arxiv-2509-15308`,
`systematics.md#g7-desi-dr2-lyalpha-full-shape-arxiv-2607-27411`); the BAO-shift
studies on AbacusSummit and CoLoRe-2LPT
(`systematics.md#d1-non-linear-bao-broadening-and-shift`); blinding practice of
each DESI analysis (`systematics.md#a4-blinding`,
`physics-and-methods.md#covariance-likelihood-and-blinding-practice`); P1D
synthetic spectra (`deep/p1d-estimation.md`). Galaxy fast mocks (COLA, EZmocks)
are in `cosmo-simulations-mocks/deep/fast-mocks.md`.

Notation. δ_G a Gaussian field; δ = ρ/ρ̄ − 1; τ the optical depth;
F = e^(−τ); F̄ the mean transmission; τ_0, α the FGPA amplitude and exponent,
α = 2 − 0.7(γ − 1) with γ the slope of the temperature–density relation;
η_∥ the line-of-sight velocity gradient; b_Lyα, β_Lyα the forest bias and RSD
parameter; "raw" mocks are transmission skewers, "cooked" (or contaminated)
mocks add continua, contaminants and noise.

## How it is done
<!-- key: how-it-is-done -->

The DESI chain has two stages: a cosmological stage that produces quasar
positions and Lyα transmission skewers (LyaCoLoRe, Saclay, CoLoRe-QL,
CoLoRe-2LPT, or AbacusSummit painted with the FGPA), and a survey stage
(quickquasars in desisim) that turns skewers into DESI-like spectra
(arXiv:2401.00303, Sects. 2–3; arXiv:2503.14741, Sect. II) [src].

### Step 1. Generate the large-scale field and the quasars
<!-- key: step-1-generate-the-large-scale-field-and-the -->

| Item | LyaCoLoRe (eBOSS, DESI DR1) | Saclay (eBOSS, DESI DR1–DR2) | CoLoRe-2LPT (DESI DR2 full shape) |
|---|---|---|---|
| Field | Gaussian field at z = 0 in a box, radial velocity from the potential, v_r = −2f_0/(3H_0²Ω_M) (e_r·∇)φ (Eq. 1); lognormal for sources | Gaussian δ_m from CAMB P_m (Eq. 1); velocity v̂_j = i f a H k_j/k² δ̂_m (Eq. 2); six boxes of η̂_pq = f k_p k_q/k² δ̂_m (Eq. 3) | 2LPT displacements Ψ = D_1∇φ_1 + D_2∇φ_2 with D_2 = −(3/7)D_1² Ω_M^(−1/143), f_2 = 2Ω_M^(6/11) (Eqs. 1–4) |
| Grid | 4096³ cells, O(1) h⁻¹Mpc | voxel a = 2.19 h⁻¹Mpc; forest pixels of 0.2 h⁻¹Mpc | 400 full-sky light cones ~10 h⁻¹Gpc, 4096³ cells of ~2.4 h⁻¹Mpc, ~12 M quasars over 0 < z < 3.8 |
| Quasars | lognormal field Poisson-sampled with input n(z), b(z) | placed with probability tied to the density, matched to the survey n(z) | threshold biasing calibrated on AbacusSummit snapshots; b_Q(z) = 0.523(1+z)^1.475 (Eq. 6) and a fitted threshold t(z) (Eq. 7); bias within 5% of the DESI DR1 measurement |
| Place read | arXiv:1912.02763, Sects. 2.1–2.2 | arXiv:2310.18996, Sects. 2.1–2.3 | arXiv:2607.27412, Sects. 2.1, 2.3.2, 2.4 |

CoLoRe-QL, used for DESI DR2 BAO, is LyaCoLoRe generated from a quasi-linear
rather than linear input power: the isotropic BAO-fit model evaluated at
k_∥ = 0 with Σ_⊥ = 3.26 h⁻¹Mpc. Reason: DR1 mock BAO errors were
"systematically smaller" than the data's, explained by the non-linear
broadening of the peak absent from Gaussian mocks; with CoLoRe-QL the errors
agree better with DR2, while the non-updated Saclay mocks still give smaller
errors (arXiv:2503.14741, Sect. II.1.2) [src].

### Step 2. Add the small-scale power the grid cannot hold
<!-- key: step-2-add-the-small-scale-power-the-grid -->

The grid cell (~1–2 h⁻¹Mpc) is an order of magnitude above the Jeans scale
(~100 h⁻¹kpc), so P1D and the pixel variance would be too low; realistic
small-scale power is needed "so that the covariance matrices in our final
analyses are realistic" (arXiv:1912.02763, Sect. 2.2.1) [src]. Both families
add an independent 1D Gaussian field per skewer, uncorrelated between
sightlines, which therefore leaves the 3D correlation unchanged except as
noise:

- LyaCoLoRe: δ_G = δ_C + σ_ε(z) δ_ε (Eq. 3), δ_ε with
  P1D ∝ [1 + (k/k_1)^n]⁻¹ (Eq. 2), after nearest-grid-point interpolation of
  the CoLoRe skewers "to avoid introducing additional smoothing". Power is
  added to the density, not the velocity, because tuning velocities would
  require recomputing the RSD weight matrix at each step [src: Sect. 2.2.1].
- Saclay: g = δ_L + δ_S + c_GP(z) η_∥ (Eq. 5); δ_L and η_∥ interpolated from
  voxels with a Gaussian kernel of width one voxel over 7³ neighbours to
  suppress aliasing above the Nyquist wavenumber; δ_S drawn per spectrum
  [src: arXiv:2310.18996, Sect. 2.3].

### Step 3. Map to optical depth and redshift space
<!-- key: step-3-map-to-optical-depth-and-redshift-space -->

- **Lognormal + FGPA (LyaCoLoRe, CoLoRe-2LPT).**
  1 + δ = exp[D δ_G − D²σ_G²/2] (arXiv:1912.02763, Eq. 4) and
  τ = τ_0(z)(1 + δ)^α(z) (Eq. 5; arXiv:2607.27412, Eq. 11). RSD by moving τ
  along the skewer with the peculiar velocity, τ(s) = ∫ τ(x) K(s − x − v_r) dx
  (arXiv:1912.02763, Eq. 6) with K a Dirac delta: a thermal-broadening
  Gaussian kernel is available but its width is usually below the cell size,
  so its effect is small [src: Sect. 2.2.3].
- **Saclay.** F = exp[−a_GP(z) exp(b_GP(z) g)], g as above (Eq. 6), with
  c_GP = β_Lyα/f setting the RSD directly; wavelengths use the unperturbed
  cosmological redshift (arXiv:2310.18996, Sect. 2.4) [src]. RSD thus enters
  as a velocity-gradient term in the Gaussian field rather than as a shift of
  pixels.
- **AbacusSummit.** FGPA τ = τ_0 ρ^α on the N-body matter field (Method I),
  plus a modified variant (Method II, not read in detail); RSD by a velocity
  kernel; tuned against IllustrisTNG300-1 skewers using its dark-matter-only
  twin TNG300-3-DM with the same seed (arXiv:2305.08899, Sects. 3.3, 3.5)
  [src].

### Step 4. Tune the free parameters to measured statistics
<!-- key: step-4-tune-the-free-parameters-to-measured -->

| Item | LyaCoLoRe | Saclay | CoLoRe-2LPT | AbacusSummit |
|---|---|---|---|---|
| Free parameters | τ_0(z), σ_ε(z), n, k_1 (α = 1.65 fixed; log τ_0 slope fixed to 4.5); velocity factor a_v | a_GP, b_GP, c_GP and P_s(k) at z_t = 1.8, 2.2, 2.6, 3.0, 3.6, interpolated | n, k_1, σ_ε(z), τ_0(z), a_v (α = 1.65 fixed) | τ_0, σ_ε, γ, n, k_1 |
| Targets | BOSS DR9 P1D fit, a literature F̄(z), b_δ,F(z) from BOSS DR12 auto + cross | b_eff = 0.183[(1+z)/3.3]^3.47 and β = 1.76[(1+z)/3.3]^−2.32 from an eBOSS DR16 refit, F̄ = exp(−0.0028(1+z)^3.45), BOSS P1D | DESI DR1 P1D, DESI mean flux, DESI DR2 b_Lyα and β_Lyα: "the first time mocks are fully fitted to DESI statistics" | TNG300-1: ⟨F⟩ = 0.8101, √Var[F] = 0.1878, P1D and P3D to 0.8 h/Mpc |
| Procedure | Minuit on a weighted deviation from targets, 7 bins z = 2.0–3.2; P1D weight ∝ 1/(1 + (k/0.01 s/km)²) below 0.02 s/km and zero above; ~55,000 then ~220,000 skewers | Minuit for a_GP and b_GPσ_g to F̄ and σ_F; P_s iterated ten times by P_s ← P_s × P_target/P1D; final small changes of a_GP, b_GP because the predicted bias came out high | first step as LyaCoLoRe; then 8 × 8 grid of τ_0, σ_ε varied by up to 20% at z = 2.2, 2.4, 2.8, 3.2; finally a_v scanned over [1.0, 1.3] in steps of 0.05 to match β | fits to P3D alone, P1D + P3D, for each method |
| Result | log τ_0 = 1.48 + 4.5 log x, log σ_ε = 6.02 + 0.276 log x, n = 0.732, k_1 = 0.0341, a_v = 1.3 (x = (1+z)/4); P1D, F̄, b within 10% at almost all relevant k, z | raw and cooked biases close to targets, β ~10% low in cooked mocks | within 10% for k_∥ ≲ 0.01 s/km over 2.2 ≤ z ≲ 3.5; tuning files public | no single model fits both: Model 2 (P1D + P3D) gives χ²_1D = 27.5 for 27 points but β = 0.949; Model 3 matches P3D but β = 2.02, against TNG β = 1.432 |
| Place read | arXiv:1912.02763, Sect. 3, Eq. 8 | arXiv:2310.18996, Sects. 2.6, 4.3 | arXiv:2607.27412, Sect. 3.2 | arXiv:2305.08899, Sect. 3.5, Table 1 |

Reasons stated for the choices:

- **Low-k weighting of P1D.** It prioritises the modes relevant for BAO
  (k ≲ 0.005 s/km) and ignores k > 0.02 s/km, where the finite cells cannot
  give realistic power and which BOSS did not measure (arXiv:1912.02763,
  Sect. 3) [src].
- **Effective bias as target.** Saclay targets b_eff = b(1 + 2β/3 + β²/5)^½,
  proportional to the correlation monopole, rather than b (arXiv:2310.18996,
  Sect. 2.6) [src].
- **The velocity factor a_v.** It is not a correction of the velocities
  (CoLoRe velocities give the right quasar anisotropy) but of the
  approximations in the flux recipe, which give "an unrealistic value of β";
  fixed at 1.3 because varying it requires recomputing the RSD weights
  (arXiv:1912.02763, Sect. 3) [src]; CoLoRe-2LPT repeats the argument and
  scans it last (arXiv:2607.27412, Sect. 3.2) [src].
- **Fixed α.** Equivalent to γ = 1.5, "in reasonable agreement with the
  literature" (arXiv:1912.02763, Sect. 3) [src].
- **Second calibration for 2LPT.** The LyaCoLoRe procedure "was not designed
  for 2LPT skewers, specifically for the computation of b_Lyα"
  (arXiv:2607.27412, Sect. 3.2) [src].

### Step 5. Insert the astrophysical contaminants
<!-- key: step-5-insert-the-astrophysical-contaminants -->

| Contaminant | How it is inserted | Place read |
|---|---|---|
| HCDs | candidate positions where the Gaussian (LyaCoLoRe, Saclay) or 2LPT (CoLoRe-2LPT) density exceeds a threshold set for b_HCD = 2 independent of redshift; Poisson-sampled to the pyigm column-density distribution; sampled before adding small-scale power so they correlate with the 3D field; Voigt profiles added by desisim. For 2LPT the threshold–bias relation is not analytic and is fitted on 2 h⁻¹Gpc boxes: t_HCD(z) = 5.331(1+z)^−2.444 − 0.260 (Eq. 21). At z = 2.35 ~0.39 HCDs and 0.054 DLAs per forest (1040–1200 Å) | arXiv:1912.02763, Sect. 5.1; arXiv:2310.18996, Sect. 2.7; arXiv:2607.27412, Sect. 5.1.1; arXiv:2401.00303, Sect. 2.3.2 |
| Metals | τ_X = A_X τ_α (or F_m = exp(−C_m τ_Lyα)) moved to λ_obs = (1+z_abs)λ_m; RSD from the same weights as Lyα; the four silicon lines give peaks at r_∥ = 104, −21, −54, −61 h⁻¹Mpc (Si II 1260, Si III 1207, Si II 1193, 1190) at z = 2.35 by Eq. 2 of arXiv:2401.00303. C IV is not included because its forest-region absorption arises at z ≈ 1.32, outside the raw-mock transmission range | arXiv:1912.02763, Sect. 5.2; arXiv:2401.00303, Sect. 2.3.3; arXiv:2310.18996, Sect. 2.8 |
| BALs | 1500 templates from the SDSS DR14 BAL catalogue (944.6–1686.5 Å; O VI, Lyα, N V, Si IV, C IV troughs) applied to a random 16% of quasars, uncorrelated with neighbours | arXiv:2401.00303, Sect. 2.3.1 |
| Quasar velocities and redshift errors (DR2) | Gaussian σ_FoG = 150 km/s on quasar redshifts to mimic non-linear velocities (no collapsed objects in the mocks); Gaussian catalogue errors σ_z = 400 km/s, now in the baseline | arXiv:2503.14741, Sect. II.2 |

Two placement philosophies coexist for metals: proportional to the local Lyα
optical depth (used, following eBOSS practice) or in density peaks like HCDs
(proposed, not adopted) (arXiv:2310.18996, Sect. 2.8; arXiv:1912.02763,
Sect. 5.2) [src]. The proportional method was chosen because what matters for
BAO is the 3D clustering strength of the contaminant, which it reproduces
with one amplitude per line [src: arXiv:1912.02763, Sect. 5.2].

### Step 6. Emulate the survey and the instrument
<!-- key: step-6-emulate-the-survey-and-the-instrument -->

quickquasars (arXiv:2401.00303) [src: Sects. 2.2, 3.2] and its DR2 use
(arXiv:2503.14741, Sect. II.2) [src]:

1. Down-sample the mock quasars to the footprint and n(z); assign r-band
   magnitudes and numbers of exposures from the observed distributions. DR2
   adds the ~15% of quasars targeted as ELGs, with one exposure each.
2. Continua from SIMQSO by default: broken power law with slopes tuned in the
   forest to the eBOSS DR16 mean continuum and PCA dispersion (m = −1.5 below
   1100 Å, −0.5 from 1100 to 5700 Å, σ_m = 0.7), and Gaussian emission lines
   adjusted to the DESI EDR+M2 mean continuum. A PCA option exists.
3. Instrument: specsim with fibre-aperture losses, sky, throughput (including
   the EDR blue-collimator dip at 4400 Å), dispersion, shot, dark and read
   noise; the pipeline's 10 Å Gaussian smoothing of the variance is emulated
   because specsim lacks it.
4. Run the data pipeline unchanged: DLA and BAL finders, masking, continuum
   fit, distortion matrix (for CoLoRe-2LPT with the DR2 projection,
   arXiv:2607.27412, Sect. 6) [src].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Which mock family for which test
<!-- key: which-mock-family-for-which-test -->

| Family | Buys | Lacks or costs | Place read |
|---|---|---|---|
| LyaCoLoRe | full-survey volume, fast; shares the CoLoRe quasar field | linear (Gaussian/lognormal) BAO with no broadening; β needs a_v | arXiv:1912.02763; arXiv:2503.14741, Sect. II.1.2 |
| CoLoRe-QL | BAO broadening, hence realistic BAO errors | broadening put in by hand through the input power, so no non-linear BAO shift | arXiv:2503.14741, Sect. II.1.2 |
| Saclay | independent code and RSD implementation (η_∥ in g); 100 realisations over the DESI footprint | β ~10% low in cooked mocks; DR2 errors smaller than data (not updated) | arXiv:2310.18996, Sect. 4.3; arXiv:2503.14741, Sect. II.1.2 |
| CoLoRe-2LPT | non-linear 2LPT field, tuned to DESI P1D, F̄, b, β; 400 realisations; DR2 correlations reproduced at all r, including metal bumps | cross-correlation near the line of sight off at r ~ 60–70 h⁻¹Mpc, attributed to approximate HCD modelling and Gaussian redshift errors; no UV fluctuations, C IV, sky residuals or proximity effect (full-shape mock model) | arXiv:2607.27412, Sect. 6; `systematics.md#g7-desi-dr2-lyalpha-full-shape-arxiv-2607-27411` |
| AbacusSummit + FGPA | N-body non-linearity and true BAO shift; 2 h⁻¹Gpc boxes | FGPA cannot match TNG P1D and P3D with one parameter set (Table 1); box geometry, not a survey light cone | arXiv:2305.08899, Sect. 3.5 |

Using two families with different codes is itself the systematic test: in
DR1 the two suites differed at the level of the largest mock offset, so no
correction was applied (`systematics.md#g2-desi-dr1-lyalpha-bao-arxiv-2404-03001`).

### Where to put realism: field or post-processing
<!-- key: where-to-put-realism-field-or-post-processing -->

Everything that is not large-scale density and velocity (HCDs, metals, BALs,
continua, noise, redshift errors) is added in post-processing to one set of
raw skewers, so contamination levels can be switched on one by one on the
same realisations; eBOSS DR16 used exactly this ladder of four levels
(`systematics.md#g3-eboss-dr16-lyalpha-bao-arxiv-2007-08995`). The cost is
that contaminants are correlated with the field only through simple biasing
(threshold for HCDs, proportionality for metals), not through physics.

### Redshift errors: realistic or extreme
<!-- key: redshift-errors-realistic-or-extreme -->

The DR2 BAO bias in α_∥ on mocks traces to redshift errors smearing the
mean-continuum emission lines during continuum fitting; the mock
implementation (σ_z = 400 km/s Gaussian on every quasar) is described by the
DR2 papers as "the most extreme version of this effect" (L2 G1). A mock
choice thus sets the size of a systematic that the data may not have.

## Blinding: the catalogue-level AP scheme
<!-- key: blinding-the-catalogue-level-ap-scheme -->

L2 records which DESI analyses were blinded and how; the algorithm of the
proposed catalogue-level scheme (arXiv:2607.07875) [src: Sect. 2]:

1. Precompute a redshift map z′ = z + f(z), with
   f = R⁻¹(R(z|Ω^bld)|Ω^ref) − z matching comoving distances R between a
   blinded and a reference cosmology (Eq. 5), and the derived wavelength map
   g (Eq. 7).
2. For each quasar, after delta extraction: shift its redshift with f; shift
   every pixel of its forest with g; optionally restore the forest range
   (not done in the paper).
3. Resample δ and weights onto a regular grid, so the bin spacing cannot
   reveal the shift; weights are not re-optimised.

Why after delta extraction: the spectrum mixes the quasar continuum and
absorbers at different redshifts, and delta extraction assumes no cosmology,
so earlier blinding is "not meaningful"; all absorption is treated as Lyα
because metal and Lyα contributions at one wavelength cannot be separated
[src: Sect. 2]. Limits: metal peaks keep their atomic wavelength ratios, so
the 1D correlation can hint at the blinding direction, mitigable by an extra
blinding at the correlation or posterior level; rebinning changes weights and
distortion matrices at the percent level without changing parameters; cost
~5% more wall-clock time [src: Sect. 3.5].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| LyaCoLoRe grid | 4096³ cells, O(1) h⁻¹Mpc | LyaCoLoRe | arXiv:1912.02763 | Sect. 2.2.1 |
| LyaCoLoRe tuned parameters | log τ_0 = 1.48 + 4.5 log x; α = 1.65; log σ_ε = 6.02 + 0.276 log x; n = 0.732; k_1 = 0.0341; a_v = 1.3 | LyaCoLoRe | arXiv:1912.02763 | Sect. 3 |
| Saclay voxel, pixel | 2.19 h⁻¹Mpc; 0.2 h⁻¹Mpc | Saclay | arXiv:2310.18996 | Sect. 2.3 |
| Saclay targets | b_eff = 0.183[(1+z)/3.3]^3.47; β = 1.76[(1+z)/3.3]^−2.32 | eBOSS DR16 refit | arXiv:2310.18996 | Sect. 2.6 |
| Saclay cooked-mock fits | χ² 1498–1629 for 1570 dof (auto), 3228–3410 for 3143 (cross), 20 < r < 180 h⁻¹Mpc, 30 realisations | Saclay | arXiv:2310.18996 | Sect. 4.3 |
| CoLoRe-QL broadening | Σ_⊥ = 3.26 h⁻¹Mpc in the input power | DESI DR2 BAO | arXiv:2503.14741 | Sect. II.1.2 |
| CoLoRe-2LPT light cones | 400, ~10 h⁻¹Gpc, 4096³ cells of ~2.4 h⁻¹Mpc, ~12 M quasars | DESI DR2 full shape | arXiv:2607.27412 | Sect. 2.4 |
| Quasar bias law | b_Q = 0.523(1+z)^1.475; within 5% of DESI DR1 | CoLoRe-2LPT | arXiv:2607.27412 | Sect. 2.3.2 |
| HCD bias and threshold | b_HCD = 2; t_HCD = 5.331(1+z)^−2.444 − 0.260 | CoLoRe-2LPT | arXiv:2607.27412 | Sect. 5.1.1 |
| HCD density in mocks | ~0.39 HCDs, 0.054 DLAs per forest at z = 2.35 | quickquasars | arXiv:2401.00303 | Sect. 2.3.2 |
| BAL fraction | 16% of quasars, 1500 templates | quickquasars | arXiv:2401.00303 | Sect. 2.3.1 |
| Redshift dispersion and error | σ_FoG = 150 km/s; σ_z = 400 km/s | DR2 mocks | arXiv:2503.14741 | Sect. II.2 |
| DLA catalogue cuts in the DR2 mock test | red-side SNR > 3, log N_HI > 20.3, CNN CONF > 0.5, GP P_DLA > 0.9, template DLAFLAG = 0 | DR2 mocks | arXiv:2503.14741 | App. B |
| Forest count, EDR+M2 | ~89.7k analysed forests per mock against 88.5k in data | quickquasars | arXiv:2401.00303 | Sect. 4.2 |
| TNG targets for AbacusSummit | ⟨F⟩ = 0.8101, √Var[F] = 0.1878, b = −0.1379, β = 1.432 | AbacusSummit | arXiv:2305.08899 | Table 1 |
| AP blinding cost | ~5% more wall-clock time | DESI DR1 test | arXiv:2607.07875 | Sect. 3.5 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Mock errors smaller than data errors.** Without non-linear broadening
  the BAO peak is too sharp; DR1 BAO errors were underestimated on mocks;
  CoLoRe-QL fixes it by construction, Saclay does not (arXiv:2503.14741,
  Sect. II.1.2) [src]. Test: compare the mean mock σ_α with the data σ_α.
- **β set by a fudge factor.** a_v absorbs the failure of the flux recipe to
  give the right β; a full-shape test on such mocks probes the model's
  recovery of an input β that is itself tuned (arXiv:1912.02763, Sect. 3;
  arXiv:2607.27412, Sect. 3.2) [src].
- **One FGPA set cannot fit P1D and P3D.** On AbacusSummit, fitting P1D gives
  β ≈ 0.95 and fitting P3D gives β ≈ 2.0 against 1.43 in TNG
  (arXiv:2305.08899, Table 1) [src]. Any FGPA mock is tuned to the statistic
  its users care about.
- **Mock model ≠ data model.** Terms absent from the mocks (sky residuals,
  C IV, transverse proximity, UV fluctuations) are dropped from the mock fit;
  their effect on the data result is not tested by the mocks
  (`systematics.md#g7-desi-dr2-lyalpha-full-shape-arxiv-2607-27411`).
- **Line-of-sight residuals.** Mock and data correlations disagree most in
  the μ ~ 1 wedge, attributed to DLA, redshift-error and metal modelling
  (arXiv:2503.14741, Sect. III.3; arXiv:2607.27412, Sect. 6) [src]: the place
  where the BAO α_∥ bias arises.
- **Contaminants placed by recipe.** HCDs by a density threshold with a
  fixed b_HCD = 2, metals proportional to τ_Lyα; real HCD content and bias are
  uncertain (`systematics.md#b1-high-column-density-systems-dlas-sub-dlas`).
- **Finder tests on old mocks.** The DR2 DLA-finder comparison was run on one
  LyaCoLoRe realisation without BAO broadening (arXiv:2503.14741, App. B)
  [src].
- **Partial unblinding through metals.** Under AP blinding, the 1D
  correlation's metal peaks move and hint at the blinding direction
  (arXiv:2607.07875, Sect. 3.5) [src].

## Reading list
<!-- key: reading-list -->

- Method: Farr et al. 2020, arXiv:1912.02763 — LyaCoLoRe: lognormal skewers, small-scale power, FGPA, tuning, HCD and metal insertion.
- Method: Etourneau et al. 2024, arXiv:2310.18996 — Saclay mocks: η_∥ in the Gaussian field, b_eff tuning, iterative P_s.
- Method: Herrera-Alcantar et al. 2025, arXiv:2401.00303 — quickquasars: continua, BALs, HCDs, metals, specsim, comparison with EDR.
- Application: Casas et al. 2025, arXiv:2503.14741 — CoLoRe-QL, redshift-error injection, DLA-masking tests for DR2.
- Method: Ruiz-Herrera Bernal et al. 2026, arXiv:2607.27412 — 2LPT light cones tuned to DESI statistics, HCD threshold calibration.
- Method: Hadzhiyska et al. 2023, arXiv:2305.08899 — FGPA on AbacusSummit tuned to TNG; why one parameter set cannot fit P1D and P3D.
- Method: Perez-Sanchez et al. 2026, arXiv:2607.07875 — catalogue-level AP blinding for the forest, validation and limits.
- Validation framework: DESI 2024 IV, arXiv:2404.03001, Sect. 6 — how mocks gate a Lyα BAO result (read for L2).

## Not verified
<!-- key: not-verified -->

- The Ohio mocks listed among quickquasars inputs (arXiv:2401.00303,
  Sect. 2.1) and the AbacusSummit Method II prescription.
- The DR1 mock validation paper's own construction details beyond L2
  (arXiv:2404.03004) and the HCD validation appendix of arXiv:2607.27412.
- Mock-to-data P1D and bias agreement figures of CoLoRe-2LPT (Sect. 4, only
  the stated 10% goal read here).
- The DESI DR2 BAO blinding method (as already open in L2).
