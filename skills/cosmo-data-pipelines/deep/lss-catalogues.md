# Catalogue construction: masks, randoms, completeness and imaging-systematics weights — cosmo-data-pipelines dossier

Scope: how a clustering catalogue is assembled step by step (vetoes and
their area cost, completeness definitions, redshift-failure weights,
imaging-systematics regression with its map choice and null-test pass
criterion, randoms and their normalisation, total and FKP weights), with
the stated reason for each setting, compared across DESI DR1, eBOSS DR16,
DES Y3 lenses and the Euclid design.
Snapshot: 2026-10-21.
From: Ross et al. 2025 (DESI LSS catalogues); eBOSS and DES clustering
working groups (copied from `references/subtopics.tsv`).

Already in L2, not repeated here: the definition of a clustering catalogue
and the mangle mask format
(`physics-and-methods.md#catalogue-construction-masks-randoms`), the table
of imaging-weight method families with their foundation papers (same
section), the DESI weight table in one line each
(`surveys-and-data.md#spectroscopic-surveys`), and the weight and random
systematics (`systematics.md#imaging-systematics-weights-over-and-under`,
`systematics.md#random-catalogue-and-footprint-errors`). How the radial and
angular integral constraints enter the window is in
`cosmo-galaxy-clustering` (`deep/estimators-window.md`); the
mode-removal correction and polynomial marginalisation for full shape are
in `cosmo-galaxy-clustering` (systematics, Sect. 5). Injection-based weights
are in `deep/source-injection.md`.

## How it is done
<!-- key: how-it-is-done -->

The sequence follows DESI DR1 (DESI 2024 II, arXiv:2411.12020); eBOSS DR16
(Ross et al. 2020, arXiv:2007.09000) and DES Y3 (Rodríguez-Monroy et al.
2022, arXiv:2105.13540) are compared under "Choices and what they cost".

### Step 1. Start from potential assignments, not from the footprint
<!-- key: step-1-start-from-potential-assignments-not -->

DESI randoms come from the targeting team in files of 2500 deg⁻² each;
up to 18 are provided, together more than 100 times the density of all
DR1 LSS catalogues; each random carries the imaging metadata at its
position [src: arXiv:2411.12020, Sect. 2.1]. The fibre-assignment code is
run with the real tiles and positioner states to list every target and
random that a positioner could have reached ("potential assignments"); a
point is typically reachable from several tiles and fibres, since an area
is observable up to seven times and two positioners overlap over much of
the focal plane [src: same]. The catalogue is then reduced to one entry
per TARGETID with a sorting that puts each object at its most relevant
tile and fibre [src: Sect. 5.1].

### Step 2. Apply vetoes, data and randoms alike
<!-- key: step-2-apply-vetoes-data-and-randoms-alike -->

| Veto | DESI DR1 definition | Area or data lost | Stated reason |
|---|---|---|---|
| Bad hardware | ZWARN_MTL flags from the Iron reduction; TSNR2_ELG > 80 (dark), TSNR2_BGS > 1000 (bright); 60 poorly performing fibres | 2.3% (bright), 3.1% (dark); TSNR2 cuts < 1% of data | success "declines dramatically" below the TSNR2 thresholds; flag only points reachable solely by bad hardware, to minimise lost area [src: Sect. 4.1] |
| Priority | an occurrence is vetoed if the fibre went to a higher-priority class (QSO and strong-lens candidates at priority 4000 in dark time; white dwarfs, 2998, in bright time); LRGs do not veto ELGs | 1666.7 deg², 20% of the DR1 footprint for LRG and ELG | areas where the class could not be observed; LRGs excluded because 10% of ELGs share their priority and they overlap in redshift [src: Sect. 4.2] |
| Bright objects (targeting) | Legacy Surveys bits 1 (Tycho or Gaia G < 13), 12 (bright galaxy, not for BGS), 13 (globular clusters); g, r, z coverage | — | bright galaxies (mostly z < 0.15) corrupt photometry for the dark tracers but are real BGS targets [src: Sect. 4.3.1] |
| Extra star masks | MEDIUM star mask (bit 11, G < 16) for BGS, ELG, QSO; WISE W1, W2 bits for QSO; custom WISE and Gaia masks for LRG; ELG custom mask (dwarf satellites, ghosts) | 4.5% (ELG), 5.2% (BGS), 6.3% (QSO), 0.1% (ELG custom) | ELG and QSO densities 10–20% lower inside; QSO success 53% inside against 67% outside; LRG density higher inside (photometry inflated) [src: same] |
| Imaging-property tails | E(B−V)_SFD < 0.15, Gaia stellar density < 10^4.4, PSF size and galaxy-depth limits per band (Table 5) | 3.4% (QSO, BGS), 3.2% (ELG, LRG) | outliers in property space would drive the regressions; the E(B−V) cut matches SDSS [src: Sect. 4.3.2] |

The priority veto assumes the higher-priority sample is uncorrelated with
the masked one, which is not strictly true for QSO against LRG and ELG;
this is why mocks with all three tracers processed through the same
pipeline are needed [src: Sect. 4.2].

### Step 3. Define and apply completeness
<!-- key: step-3-define-and-apply-completeness -->

DESI splits assignment incompleteness in two, mimicking SDSS
[src: arXiv:2411.12020, Sect. 5.1]:

- f_TLID: for each observed target, the inverse of the number of unique
  targets of that class at its tile and fibre, i.e. those that competed
  for the fibre (analogous to SDSS close-pair weights).
- f_tile: the completeness per t_group, the set of good-hardware tiles that
  could reach a point (analogous to SDSS sectors), counting the targets
  already in f_TLID as observed. It captures fibres lost to standard stars,
  sky fibres or, for ELGs, to LRGs, which depend only on random
  subpriorities, so they should be uniform within a t_group [src: same].

Weights [src: Sect. 5.3]: w_comp = 1/f_TLID on the data (Eq. 3); f_tile is
applied to the randoms; t_groups present only in randoms get f_tile = 1.
This is not unbiased for close pairs, hence the θ-cut at 0.05° (pairs below
it removed and folded into the window). Alternative: 128 altMTL
realisations stored as BITWEIGHTS, p_obs = N_assign/129 counting the real
assignment (Eq. 2), recommended for small scales [src: Sect. 5.2].
Stated reasons for not using PIP as baseline: several days on a 128-core
node per 128 realisations, impossible for 1000 covariance mocks; and
zero-probability pairs in single-pass areas, which PIP cannot correct
without angular up-weighting [src: Sect. 5.3]. With PIP weights, the
randoms must not also carry f_tile [src: same].

### Step 4. Model redshift failures
<!-- key: step-4-model-redshift-failures -->

DESI fits the success rate G_z against TSNR2 (tracer template S/N squared,
proportional to effective time, independent of the target), with fibre
flux φ_fib as second variable for BGS, LRG, QSO, and against TSNR2_ELG and
redshift for ELGs; w_zfail = G_z(∞, φ_fib)/G_z(TSNR2, φ_fib) (Eq. 5), an
error-function model evaluated at infinite depth [src:
arXiv:2411.12020, Sect. 7.1]. The details and reasons are in
`deep/redshift-fitting.md` (Step 6). Investigations of trends with survey
speed, number of exposures, date and focal-plane position found the impact
on two-point statistics negligible even uncorrected, but led to replacing
one night's data (12 Dec 2021) [src: same].

### Step 5. Regress density on survey-property maps
<!-- key: step-5-regress-density-on-survey-property-maps -->

DESI DR1 principle: the minimal set of maps with the simplest regression
that brings trends against all validation maps to the level seen in mocks
[src: arXiv:2411.12020, Sect. 6]. Stated reason: early catalogues that ran
non-linear regressions (SYSNet, Regressis) on all maps removed more power
from uncontaminated LRG and BGS mocks than the contamination they removed,
so linear regression is tried first and non-linear only if null tests
require it [src: same].

| Tracer | Bins | Method | Maps regressed |
|---|---|---|---|
| BGS | 0.1 < z < 0.4 | linear | r-band depth, stellar density, H I column density [src: Sect. 6.1] |
| LRG | 0.4–0.6, 0.6–0.8, 0.8–1.1 | linear, per bin | stellar density, H I, z-band galaxy depth, r-band PSF size, W1 PSF depth; one extra map per bin in DECam only [src: Sect. 6.2] |
| ELG | 0.8–1.1, 1.1–1.6 | SYSNet neural network | all validation maps except E(B−V)_noCIB, judged redundant with H I [src: Sect. 6.4] |
| QSO | 0.8–1.3, 1.3–2.1, 2.1–3.5 | Regressis random forest; DES and DECaLS fitted separately | all validation maps except E(B−V)_noCIB [src: Sect. 6.3] |

Maps are HEALPix N_side = 256; the inverse of the fitted model per pixel
and redshift bin is w_imsys [src: Sect. 6]. Maps of the difference between
DESI-star and SFD extinction (ΔEBV) are kept for validation, not
regression, because they carry CIB contamination that correlates with
large-scale structure; replacing SFD by a CIB-cleaned map shrinks the
residual trends (e.g. LRG 0.8 < z < 1.1 χ²_null from 31.6 to 13.2), so
regressing them out would remove real modes [src: Sects. 6.1–6.2].

### Step 6. Validate with a null test calibrated on mocks
<!-- key: step-6-validate-with-a-null-test-calibrated-on -->

Normalised density against each map in 10 equal bins, with completeness
weights and a 2D FKP weight w_FKP,2D = 1/[1 + n₀⟨C_assign⟩(n_tile) P₀]
(Eq. 4), n₀ = 5 × 10⁻⁴ (BGS, ELG), 4 × 10⁻⁴ (LRG), 2 × 10⁻⁵ (QSO)
h³ Mpc⁻³; errors Poisson from weighted counts, known to be only
approximately right, so the same statistic is computed on 25 Abacus altMTL
mocks with no contamination, put through the same regression
[src: arXiv:2411.12020, Sect. 6]. The DR1 Poisson errors were also
divided by mistake by the pre-refactoring mean completeness weight of the
full sample, which under-estimates them; the paper states that this was
applied consistently to data and mocks and so does not affect the
data-against-mock null tests [src: Sect. 6, footnote 14]. Pass
criterion, fixed while blinded:
the total χ²_null over all tested maps below that of at least one of the 25
mocks, and each map's χ²_null below at least two mocks; failures were
investigated, and the maps and methods were never changed after
unblinding [src: same]. Outcome: the weights lower the total χ²_null by
a factor close to 2 for BGS in DECam; by more than five for ELG,
consistent with mocks; by more than five for QSO in DECam, but at the edge
of the mock range; LRG 0.6 < z < 0.8 total exceeds every
mock [src: Sects. 6.1–6.4].

### Step 7. Give the randoms redshifts and weights, then normalise
<!-- key: step-7-give-the-randoms-redshifts-and-weights -->

Each random takes the redshift and all weights (w_comp, w_zfail, w_imsys)
of a randomly chosen galaxy, separately in each photometric region
(BASS/MzLS and DECam; for QSO also DES against DECaLS, because the QSO
selection differs there), then is multiplied by f_tile; weights are
normalised so that weighted data over weighted randoms is the same in each
region [src: arXiv:2411.12020, Sect. 8.1]. Stated reason: "shuffled"
randoms were the least biased option for BOSS CMASS; the cost is the
radial integral constraint [src: same].

### Step 8. Combine weights and add FKP
<!-- key: step-8-combine-weights-and-add-fkp -->

w′_tot = w_comp w_zfail w_imsys (Eq. 6); then w_tot = w′_tot /
⟨w_comp⟩(n_tile) (Eq. 7), the WEIGHT column, so that counts sum to about
the observed number while keeping all variations; n_x(z, n_tile) = n(z)
⟨C_assign⟩(n_tile) (Eq. 8) and w_FKP = 1/[1 + n_x P₀] (Eq. 9) with P₀ =
7000 (BGS), 10,000 (LRG), 4000 (ELG), 6000 (QSO) (h⁻¹ Mpc)³, chosen near
P₀(k = 0.15 h Mpc⁻¹) and acknowledged as only roughly matched to the
samples [src: arXiv:2411.12020, Sect. 8.2]. Reason for the refactoring:
completeness weights are all above 1 and would otherwise up-weight
incomplete regions in the FKP sense [src: same].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Close-pair weights or PIP; how completeness is counted
<!-- key: close-pair-weights-or-pip-how-completeness-is -->

| Survey | Completeness weight | Cost stated |
|---|---|---|
| eBOSS DR16 | w_cp = (N_cp + N_z + N_badclass + N_star)/(N_z + N_badclass + N_star) per collision group (Eq. 2) | unbiased transverse clustering on large scales, radial clustering biased, worse in Fourier space; individual analyses quantify residuals [src: arXiv:2007.09000, Sect. 5.3] |
| DESI DR1 | 1/f_TLID on data, f_tile on randoms, θ-cut | not unbiased for close pairs [src: arXiv:2411.12020, Sect. 5.3] |
| DESI DR1 alternative | PIP from 129 realisations | cost and zero-probability pairs [src: same] |

### Redshift-failure model
<!-- key: redshift-failure-model -->

eBOSS models the efficiency per spectrograph per plate as a linear relation
between f_i = N_goodz/N_zfail and S_i, the square of the median i-band
spectral S/N at i = 20.2, giving f_good = 1 − 1/(1 + a_S + b_S S_i)
(Eqs. 5–6), plus a fibre-ID term for CCD position [src: arXiv:2007.09000,
Sect. 5.3]. Reason: LRG classification uses absorption lines whose
significance is set by continuum S/N, so LRG efficiency depends more on
S_i than quasar efficiency, which rests on strong emission lines
[src: same]. DESI's asymptotic TSNR2 model corrects only the depth
variation, not the absolute failure rate [src: arXiv:2411.12020,
Sect. 7.1].

### Imaging weights: map set and regression
<!-- key: imaging-weights-map-set-and-regression -->

- **eBOSS DR16.** Multivariate linear regression, w_sys = [A_sys +
  C_sys · P]⁻¹ (Eq. 13), on N_side = 512 SDSS maps (g depth, i PSF, i
  sky, airmass, SFD E(B−V)) and an N_side = 256 stellar-density map,
  separately for NGC and SGC; band choice "mostly arbitrary" because SDSS
  bands were observed nearly simultaneously [src: arXiv:2007.09000,
  Sect. 5.5]. Null-test χ²/d.o.f. after weights 79/55 (quasars) and 91/55
  (LRGs), the largest residual being E(B−V) even though it was regressed
  [src: same, Table 5].
- **DES Y3 lenses.** 107 survey-property maps (several statistics per
  property) reduced to an orthogonal basis by PCA at N_side = 4096; the
  first 50 principal-component maps (~98% of the variance) are used,
  because a reduced map set is a hard prior of no contamination from the
  dropped maps while the full 107 over-correct and correlate with
  large-scale structure [src: arXiv:2105.13540, Sect. 4.2]. Iterative
  Systematics Decontamination (ISD): at N_side = 512, the 1D relation of
  density against each map in ten equal-area bins is fitted by a line
  (Eq. 7); significance S_1D = Δχ²/Δχ²(68) with Δχ² = χ²_null − χ²_model
  (Eqs. 8–9) and Δχ²(68) from 1000 log-normal mocks; the most significant
  map is corrected by w = 1/F(s) (Eq. 10), and iteration stops when no map
  exceeds T_1D [src: Sect. 5.3.1]. Fiducial T_1D = 2, chosen after testing
  2, 4 and 9 for over- and under-correction on mocks [src: Sect. 6].
- **DESI DR1.** Minimal maps, simplest method, mock-calibrated pass
  criterion (Steps 5–6).

### How the weight uncertainty is carried
<!-- key: how-the-weight-uncertainty-is-carried -->

DES Y3 adds Δw_method Δw_methodᵀ (ISD minus ElasticNet, both on the 50 PC
maps, smoothed by a polynomial fit to avoid adding data noise) plus the
residual mock bias term to the covariance, i.e. analytic marginalisation
over two unit-Gaussian amplitudes (Eqs. 20–23) [src: arXiv:2105.13540,
Sect. 8.4]. The over-correction measured by running ISD on 400
uncontaminated mocks was at most ~20% of the statistical error and was not
added [src: Sect. 7.1]. DESI's analogous treatment for full shape is in
`cosmo-galaxy-clustering`.

### Randoms: shuffled, model-based, or injected
<!-- key: randoms-shuffled-model-based-or-injected -->

- Shuffled redshifts (eBOSS, DESI): random positions take a random
  galaxy's redshift and weights; eBOSS copies the completeness C_eBOSS into
  the random's w_sys first [src: arXiv:2007.09000, Sect. 5.6;
  arXiv:2411.12020, Sect. 8.1].
- Detection model (Euclid design, Euclid Collaboration 2025,
  arXiv:2511.20856): galaxies from the Euclid Deep Survey are placed at
  random positions; the noise at their line positions in the NISP dithers
  gives a line S/N S, mapped to detection probability by the sigmoid
  P_det(S) = c/[1 + (S/S₀)^−β] (Eq. 22) [src: Sect. 3.3]. On a simulated
  calibration set, S₀ = 3.69 ± 0.42, β = 4.98 ± 1.25, c consistent with 1;
  the errors are counted pessimistically by points above and below the
  curve [src: same]. Full injection through SIR and SPE is planned only for
  limited areas because of cost [src: same]. For tests, a tabulated
  detection probability is built from the Flagship mock in 10 flux, 90
  redshift and 3 E(B−V) bins, smoothed in redshift except across the jump
  at z = 1.42 where [O III] enters the grism [src: Sect. 4.3]. Using
  different extinction maps for data and randoms leaves BAO accurate to
  sub-per cent but changes large scales, P15 deviating most
  [src: Sect. 5.1.2].
- Injected sources as randoms: see `deep/source-injection.md`.

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Random file density | 2500 deg⁻² per file; 18 files > 100× data | DESI DR1 | arXiv:2411.12020 | Sect. 2.1 |
| TSNR2 hardware thresholds | TSNR2_ELG > 80 (dark), TSNR2_BGS > 1000 (bright) | DESI DR1 | arXiv:2411.12020 | Sect. 4.1 |
| Area lost to bad hardware | 2.3% bright, 3.1% dark | DESI DR1 | arXiv:2411.12020 | Sect. 4.1 |
| Priority-veto area | 1666.7 deg² (20%) for LRG and ELG; 25.9 deg² BGS; 38.5 deg² QSO | DESI DR1 | arXiv:2411.12020 | Sect. 4.2 |
| Imaging-tail mask | 3.2–3.4% of footprint | DESI DR1 | arXiv:2411.12020 | Sect. 4.3.2, Table 5 |
| Assignment completeness C_assign | BGS 63.6%, LRG 69.3%, ELG 35.2%, QSO 87.4% | DESI DR1 | arXiv:2411.12020 | Table 2 |
| altMTL realisations | 128 (+1 real) | DESI DR1 | arXiv:2411.12020 | Sect. 5.2 |
| θ-cut | 0.05° | DESI DR1 | arXiv:2411.12020 | Sect. 5.3 |
| Imaging-map resolution | N_side = 256 | DESI DR1 | arXiv:2411.12020 | Sect. 6 |
| Null-test mocks; bins | 25 uncontaminated altMTL mocks; 10 bins per map | DESI DR1 | arXiv:2411.12020 | Sect. 6 |
| FKP P₀ (h⁻¹ Mpc)³ | 7000 BGS, 10,000 LRG, 4000 ELG, 6000 QSO | DESI DR1 | arXiv:2411.12020 | Sect. 8.2 |
| QSO success at low fibre flux | ~30%, varying ~10% with depth | DESI DR1 | arXiv:2411.12020 | Sect. 7.1 |
| Map resolution | N_side = 512 (stars 256) | eBOSS DR16 | arXiv:2007.09000 | Sect. 5.5 |
| Null-test χ²/d.o.f. after weights | 79/55 (QSO), 91/55 (LRG) | eBOSS DR16 | arXiv:2007.09000 | Sect. 5.5 |
| S_i reference magnitude | i = 20.2 | eBOSS DR16 | arXiv:2007.09000 | Sect. 5.3 |
| SP maps; PC maps kept | 107; 50 (~98% variance) | DES Y3 | arXiv:2105.13540 | Sect. 4.2 |
| ISD threshold; mocks | T_1D = 2; 1000 log-normal (significance), 400 (bias) | DES Y3 | arXiv:2105.13540 | Sects. 5.3.1, 6, 7.1 |
| False-correction bias | ≤ ~20% of σ | DES Y3 | arXiv:2105.13540 | Sect. 7.1 |
| Detection-model parameters | S₀ = 3.69 ± 0.42, β = 4.98 ± 1.25 | Euclid (simulated calibration) | arXiv:2511.20856 | Sect. 3.3 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Weights fitted on maps that trace structure.** E(B−V) maps carry CIB,
  which correlates with galaxies; regressing ΔEBV removes real modes. Test:
  repeat the null test with a CIB-cleaned map; DESI keeps ΔEBV as
  validation only [src: arXiv:2411.12020, Sects. 6.1–6.2].
- **Too many maps or too flexible a regression.** More power removed from
  uncontaminated mocks than contamination removed (DESI early catalogues);
  107 DES maps over-correct [src: arXiv:2411.12020, Sect. 6;
  arXiv:2105.13540, Sect. 4.2]. Test: run the identical regression on
  uncontaminated mocks and measure the false-correction bias
  (arXiv:2105.13540, Eq. 18) [src: Sect. 7.1].
- **Null test judged on analytic errors.** Poisson errors from weighted
  counts are approximate; compare to the same statistic on mocks
  [src: arXiv:2411.12020, Sect. 6].
- **Masks that change the sample, not only the area.** Inside star masks
  ELG and QSO densities drop 10–20% and QSO success falls to 53%; LRG
  density rises [src: arXiv:2411.12020, Sect. 4.3.1]. Test: n(z) and
  completeness-corrected density inside against outside each mask.
- **Priority veto correlated with the vetoed sample.** QSO and LRG/ELG
  overlap in redshift [src: arXiv:2411.12020, Sect. 4.2]. Test: mocks with
  all tracers through the same pipeline.
- **Random redshifts drawn across regions.** Different imaging regions have
  different n(z); DESI draws per region (and DES/DECaLS for QSO) and
  normalises per region [src: arXiv:2411.12020, Sect. 8.1].
- **f_tile counted twice.** With PIP weights the randoms must not carry
  f_tile [src: arXiv:2411.12020, Sect. 5.3].
- **Detection model with hidden dependencies.** The S/N–P_det model holds
  only if its residuals do not correlate with other galaxy properties, and
  it assumes perfect photometry [src: arXiv:2511.20856, Sect. 3.3].
- **Pipeline-version mismatch in vetoes.** DESI vetoes use ZWARN_MTL from
  the Iron reduction while operations used the daily pipeline
  [src: arXiv:2411.12020, Sect. 4.1, footnote].
- **Residual trends left open.** eBOSS E(B−V) and DESI LRG 0.6 < z < 0.8
  stellar density exceed expectations after weighting [src:
  arXiv:2007.09000, Sect. 5.5; arXiv:2411.12020, Sect. 6.2]; the
  consequence for BAO and full shape is assessed in the probe analyses.

## Reading list
<!-- key: reading-list -->

- Foundation: Feldman, Kaiser & Peacock 1994, arXiv:astro-ph/9304022 — the
  weight that Step 8 generalises.
- Method: Ross et al. 2020, arXiv:2007.09000 — eBOSS close-pair, redshift-
  failure and linear imaging weights; shuffled randoms.
- Method: Rodríguez-Monroy et al. 2022, arXiv:2105.13540 — PCA map basis,
  ISD, mock-calibrated significance, method spread in the covariance.
- Application: DESI 2024 II, arXiv:2411.12020, Sects. 2–8 — the current
  full recipe with area costs and pass criteria.
- Method: Ross et al. 2025, arXiv:2405.16593 — DESI pipeline detail
  behind the summary in DESI 2024 II.
- Alternative: Euclid Collaboration 2025, arXiv:2511.20856 — randoms from a
  detection model for a slitless survey.
- Method: Weaverdyck & Huterer 2021, arXiv:2007.14499 — why dropping maps
  is a prior; common regression view.
- Forward model: Rosado-Marín et al. 2024, arXiv:2411.12024 — injection
  plus regression hybrid (see `deep/source-injection.md`).

## Not verified
<!-- key: not-verified -->

- DESI DR2 catalogue changes (QSO weights moved to linear regression per
  `cosmo-galaxy-clustering`; DES region treated separately per
  arXiv:2606.18581): the DR2 catalogue method was not read here.
- Ross et al. 2025 Sects. 3.1, 4.3, 7.2–7.3 (sorting to unique TARGETID,
  t_group construction) not read in this run.
- eBOSS ELG catalogue (Raichoor et al. 2021) and its depth-dependent n(z)
  correction not read.
- KiDS, HSC and UNIONS lens-sample catalogue practice not read.
