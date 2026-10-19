# Spectroscopic systematics in clustering: residual success-rate trends, catastrophic redshifts, redshift errors and interlopers — cosmo-galaxy-clustering dossier

Scope: once redshift-failure weights exist, how an analysis finds and
removes what they miss (bad fibres, focal-plane, survey-speed, exposure and
time trends), how it decides whether a residual matters (χ²_sys, then
parameter fits), and how catastrophic redshifts, redshift errors and line
or noise interlopers are characterised, injected into mocks and modelled
in the fit; with the choices between weighting, removing, cutting and
modelling.
Snapshot: 2026-10-19.
From: DESI 2024 II (arXiv:2411.12020), Sect. 7 (copied from
`references/subtopics.tsv`).

Already in L2 or a sibling, not repeated here: the headline sizes (DR1
success-rate fluctuations, ELG catastrophic rate and redshift error, DR2
success rates, eBOSS rates) and the Euclid detection-model randoms
(`systematics.md#spectroscopic-systematics`); the full-shape budget line
(`systematics.md#two-budgets-to-keep-apart`); how the DESI and eBOSS
redshift-failure weights w_zfail are fitted against TSNR2 or spectral
S/N (`cosmo-data-pipelines/deep/lss-catalogues.md`, Step 4 and
"Redshift-failure model"); fitter templates, VI truth tables, repeat-based
precision and the per-tracer catastrophic rates
(`cosmo-data-pipelines/deep/redshift-fitting.md`).

Notation. f_goodz: redshift success fraction; TSNR2: template
signal-to-noise squared, proportional to effective exposure time;
w_tot = w_comp w_sys w_zfail the catalogue weight (completeness, imaging,
redshift failure) [src: arXiv:2405.17208, Eq. 13]; Δv = c Δz/(1 + z),
the velocity difference between two redshift estimates of one object;
f_tot: total interloper fraction.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Remove fibres whose failures the model cannot describe
<!-- key: step-1-remove-fibres-whose-failures-the-model -->

DESI DR1 [src: arXiv:2405.17208, Sect. 4]: for each fibre, simulate the
success count as a sum of binomials, one per observation with its own
modelled success rate (3 million draws per fibre, the modelled rates
renormalised to the observed mean); convert the p-value of the observed
count to nσ = −√2 erfc⁻¹(2p) (Eq. 27). Stated reasons:

- Monte Carlo, not the central-limit Gaussian with the variance of a sum of
  binomials (Eq. 26): the Gaussian "dramatically overstates" the number of
  4σ outliers in the tail, even with N ≈ 600 LRG observations per fibre.
- Threshold 4σ: fewer than one of the ~4000 usable fibres should exceed it
  by chance.
- Remove rather than up-weight: the success rate of these fibres "cannot
  be modelled well".

Outcome: 55 fibres flagged across tracers plus 5 neighbours removed by
hand (fibres 2675–2691 in petal 5), 60 of 4326 fibres with valid spectra,
1.2% of the redshifts [src: Sects. 4, 7]. A time-variable saturated
feature in the 2D spectra was later identified as the cause of the petal-5
problem [src: Sect. 4, footnote 12].

Per-fibre n(z) inspection also found five petal-2 fibres (1261, 1269,
1295, 1296, 1307) with a spurious ELG spike at z = 1.5 since 1 October
2021, equivalent to about 0.1% in catastrophic rate [src: Sect. 4].

### Step 2. Search the weighted sample for residual trends
<!-- key: step-2-search-the-weighted-sample-for-residual -->

After w_zfail, DESI DR1 checks success against focal-plane position,
survey speed, number of exposures and nights, and time [src:
arXiv:2405.17208, Sects. 5.3–5.4, 7]. For ELGs the companion analysis
found up to 10% f_goodz variation across the focal plane, with
χ²/dof = 4753/4262 (BASS/MzLS) and 4716/4262 (DECam) over 4262 fibres, and
about 1% higher success near the focal centre, because TSNR2-based
weights carry no focal-plane information [src: arXiv:2405.16657,
Sect. 4.2]. Fibre-wise correction η_zfail,i = f̄_goodz/f_goodz(i)
(Eq. 23), entering as w_comp w_sys (w_zfail η_zfail) (Eq. 24) [src: same].
The ELG w_zfail itself is linear in S_spec,obs with a redshift-dependent
slope, clipped at zero (Eqs. 18–21), because ELG success depends on
[O II] flux against sky lines [src: Sect. 4.1.2].

Time: two outlier periods, one a calibration error in the "iron"
processing (fixed for the clustering catalogues) and one a 10-day
amplifier instability on petal 6 (Z camera), which lowered success
uniformly without changing n(z) [src: arXiv:2405.17208, Sect. 7].

### Step 3. Decide whether a residual matters: χ²_sys, then fits
<!-- key: step-3-decide-whether-a-residual-matters -->

Statistic [src: arXiv:2405.17208, Sect. 2.4, Eq. 9]:

χ²_sys = ΔP_ℓ(k_i) (C⁻¹)^{ij} ΔP_ℓ(k_j), ΔP_ℓ = P_ℓ^{extra wt.} − P_ℓ^{std},

with C the power-spectrum covariance. Rule as stated: a parameter can move
by at most √χ²_sys (in σ) if the weight and the parameter are perfectly
degenerate; if χ²_sys ≪ 1 no fit is needed; if χ²_sys ≳ 1, fit BAO and
full shape with and without the weight to see how much projects onto
cosmological rather than nuisance parameters [src: same]. Measurement:
P_0, P_2, P_4 from pypower, 0 < k < 0.4 h Mpc⁻¹, Δk = 0.005, 6 h⁻¹ Mpc
cells, FKP weights with completeness-dependent n̄ [src: same, Eqs. 10–14].

Fits behind the decision [src: Sect. 6.1]: blinded data; BAO on
pre-reconstruction P(k) with default settings; full shape with
velocileptors LPT, σ8-scaled ("physically motivated") bias priors and
"maximum freedom" bias, ℓ = 0, 2, no θ-cut, ω_b prior 0.02237 ± 0.00037,
k_min = 0.02 h Mpc⁻¹.

Results [src: Sects. 6, 6.1, Table 3]:

| Extra weight or cut | Tracer | χ²_sys | Largest parameter shift |
|---|---|---|---|
| no w_zfail at all (for scale) | ELG 0.8–1.1 / 1.1–1.6; QSO; LRG; BGS | 0.26 / 0.63; 0.24; < 0.04; < 0.01 | — |
| petal-6 amplifier weight | LRG | ≤ 0.03 | < 0.03σ |
| TSNR2_LRG trend, South, 0.8 < z < 0.9 | LRG | ≤ 0.04 | 0.08σ on large-scale P_0, P_2 |
| survey speed | LRG; ELG 1.1–1.6 | 0.02; 0.47 | ELG: up to 0.5σ in large-scale P_0 |
| number of exposures | ELG; QSO | 0.05; 1.9 (NGC 2.1, SGC 0.1) | QSO: 1.4σ in large-scale P_0, 0.6σ in P_2 |
| focal plane | QSO | 1.2 | scatter ≈ 0.3σ per bin, incoherent |
| mask z = 1.5 spike fibres | ELG 0.8–1.1 / 1.1–1.6 | 0.26 / 0.49 | 0.15σ on log A_s (0.8–1.1) |

Every other parameter shift is below 10% of its error; BAO α and
(h, Ω_m, log A_s) all move by at most 30% (table caption) or under 15%
(conclusions) of the error [src: Sects. 6.1, 7]. Decision: none of the
extra weights is used; only w_zfail is in the DR1 LSS catalogues [src:
Sect. 6.1]. Stated caveat: the trends peak at k < 0.03 h Mpc⁻¹, so
scale-dependent-bias f_NL, higher-order statistics or small-scale
clustering may need a different choice [src: Sects. 6.1, 7].

### Step 4. Catastrophic redshifts: characterise, model, inject
<!-- key: step-4-catastrophic-redshifts-characterise -->

DESI DR1 ELGs [src: arXiv:2405.16657, Sects. 5.1–5.2]: 0.26% of repeated
pairs have |Δv| > 1000 km s⁻¹; VI of both spectra labels the true and the
catastrophic redshift. Classes: sky residuals at 8600–8700 Å read as [O II]
(26.7%, a spike at z_catas ≈ 1.32); other sky residuals at λ > 8000 Å
(27.6%, pushing z_true < 1.1 to z_catas > 1.1); two objects in the fibre
(22.0%, mostly 0.6 < z < 0.9); no correct redshift at all (12.1%); other
line confusions, bad spectra, misclassified QSOs (11.6%). Model used for
injection (Eq. 26): pick 0.26% of mock galaxies; 76% get
z_catas = z_true + Δv_ran with |Δv_ran| drawn from a log-normal in log|Δv|,
LN(0.64, 0.25², 6.62) (Eq. 25), half positive; 24% get
z_catas ~ N(1.32, 0.006²). Stated reason for two components: random
catastrophics alone cannot reproduce the z ≈ 1.32 feature, and a generic
random part avoids over-fitting this sample. FKP weights are recomputed at
z_catas. Also run: a 1% random case ("an upper limit of the ELG
catastrophics rate in eBOSS and DESI") and removal of 1.31 < z < 1.33
(f_catas = 2.54% of the sample) [src: Sects. 5.2–5.3]. Done on 25
AbacusSummit realisations.

eBOSS DR16 quasars [src: arXiv:2007.09003, Sects. 2.2, 4.2.1]: catastrophic
rate about 1.5% (pipeline minus VI redshift > 3000 km s⁻¹ on 10,000 random
spectra); in mocks 1.5% of objects get a redshift drawn uniformly within
the box. Expected effect: dilution of the clustering, hence fσ8.

### Step 5. Redshift errors: measure from repeats, smear the mocks
<!-- key: step-5-redshift-errors-measure-from-repeats -->

- DESI DR1 ELG: repeats with |Δv| < 1000 km s⁻¹ at 0.8 < z < 1.6 follow a
  Lorentzian better than a Gaussian, L(p, w) with p = 0.03, w = 8.5 km s⁻¹
  (Eq. 27; best Gaussian N(0.06, 12.7²)); 50/95/99.5 percentiles 8.2,
  53.5, 139.0 km s⁻¹ against 20, 100, 300 km s⁻¹ for eBOSS ELGs; impact on
  clustering negligible above s = 5 h⁻¹ Mpc [src: arXiv:2405.16657,
  Sect. 5.4].
- eBOSS DR16 QSO: requirement σ_v = 300 km s⁻¹ for z < 1.5 and
  450(z − 1.5) + 300 km s⁻¹ above (Eq. 1); repeats give a double Gaussian
  (Eq. 2) with σ_1 = 150, σ_2 = 1000 km s⁻¹ and F = 4.478 [src:
  arXiv:2007.09003, Sect. 2.1]. Mocks come in four versions: no smearing,
  Gaussian, realistic (double Gaussian), realistic plus 1.5%
  catastrophics, with velocities entering as
  (1 + z_obs) = (1 + z_cos)(1 + v_los/c) [src: Sects. 4.2.1–4.2.2]. The
  RSD models (RegPT, RESPRESSO-based) and BAO fits are then run on all four
  [src: Sect. 5.3.3].

### Step 6. Slitless surveys: model interlopers in the estimator
<!-- key: step-6-slitless-surveys-model-interlopers-in -->

Euclid writes the measured correlation function of a sample with correct
galaxies (c), line interlopers (ℓ, e.g. [O III] or [S III] mistaken for
Hα) and noise interlopers (n) as the weighted sum of the three auto- and
three cross-correlations, each weighted by its fraction and random-pair
ratio (Eq. 17) [src: arXiv:2505.04688, Eq. 17]. The minimal model keeps
only the attenuated correct term,
ξ_m = (1 − f_tot)² (R_cR_c/R_mR_m) ξ_cc (Eq. 19); the second adds the
interloper autocorrelations (Eq. 20) [src: Sect. 5.2]. Tested on 1000
EuclidLargeMocks matching the DR1 area and selection [src: abstract].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

**Weight, remove or ignore a residual.** DESI removes unmodellable fibres
(1.2% of redshifts) and ignores residual trends whose fitted parameter
shifts are negligible, on the stated ground that the extra weights make no
measurable difference for BAO and full shape [src: arXiv:2405.17208,
Sects. 4, 6.1]. The cost is borne by large-scale analyses: QSO exposure
weights move the large-scale monopole by 1.4σ [src: Sect. 6].

**Threshold for "matters".** χ²_sys as an upper bound avoids fitting every
variant; but a large χ²_sys can still give small parameter shifts because
nuisance parameters and the window absorb the change: ELG catastrophic
χ²_sys reached 6.66 in Fourier space for the 1% case, with shifts no
larger than 0.2σ [src: arXiv:2405.16657, Sect. 5.3, Table 2]. In
configuration space the same cases give χ²_sys ≤ 0.42, because
catastrophics "do not move the position of the BAO peak" [src: same].

**Catastrophics: budget, cut or model.** DESI injects them into mocks and
budgets the effect (< 0.2σ for ShapeFit and full modelling) [src:
arXiv:2411.12021, Sect. 5.6]. Cutting the contaminated slice
(1.31 < z < 1.33) removes the sky-confusion spike at the cost of 2.54% of
the sample and a geometric change of the window; it raises P_ℓ at
1.1 < z < 1.6 by up to 0.3σ while catastrophics suppress it [src:
arXiv:2405.16657, Sect. 5.3]. Euclid models the dilution in the fit: the
minimal attenuation model recovers fσ8, α_∥, α_⊥ at DR1 precision with a
1–3% systematic on fσ8 depending on redshift, if f_tot is known to 10%;
with f_tot free in [0, 1] the fσ8 and bσ8 contours broaden markedly while
β stays constrained [src: arXiv:2505.04688, Sects. 6.4, 8].

**Redshift-error profile.** A single Gaussian under-describes both DESI
ELG (Lorentzian core) and eBOSS QSO (double Gaussian with a
1000 km s⁻¹ wing) errors [src: arXiv:2405.16657, Sect. 5.4;
arXiv:2007.09003, Sect. 2.1]. For eBOSS QSO the RegPT fσ8 mean was
0.3836, 0.3786, 0.3840 and 0.3746 for none, Gaussian, realistic and
catastrophic mocks (rms 0.0033 to 0.0081), α_∥ and α_⊥ moving by a few
10⁻³ [src: arXiv:2007.09003, Table 6]; the challenge recovered fσ8 to 3%
and α to 1% and set consensus systematics σ(fσ8) = 0.011,
σ(α_∥) = 0.008, σ(α_⊥) = 0.005 [src: abstract].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Bad-fibre threshold | 4σ by Monte Carlo (3 × 10⁶ draws per fibre) | DESI DR1 | arXiv:2405.17208 | Sect. 4 |
| Fibres removed | 60 of 4326; 1.2% of redshifts | DESI DR1 | arXiv:2405.17208 | Sects. 4, 7 |
| χ²_sys rule | parameter shift ≤ √χ²_sys σ; fit if ≳ 1 | DESI DR1 | arXiv:2405.17208 | Sect. 2.4 |
| Largest residual-weight χ²_sys | 1.9 (QSO, exposures) | DESI DR1 | arXiv:2405.17208 | Sect. 6 |
| Largest parameter shift from extra weights | 0.15σ on log A_s | DESI DR1 | arXiv:2405.17208 | Sect. 6.1 |
| ELG focal-plane success variation | up to 10%; centre +1% | DESI DR1 | arXiv:2405.16657 | Sect. 4.2 |
| ELG catastrophic classes | 26.7 / 27.6 / 22.0 / 12.1 / 11.6% | DESI DR1 | arXiv:2405.16657 | Sect. 5.1 |
| ELG catastrophic injection | 0.26%: 76% log-normal Δv, 24% N(1.32, 0.006²) | DESI DR1 | arXiv:2405.16657 | Eq. 26 |
| ELG catastrophic χ²_sys, Fourier, 1.1–1.6 | 1.46 (realistic), 6.66 (1% random), 4.21 (cut) | DESI DR1 mocks | arXiv:2405.16657 | Table 2 |
| ELG catastrophic parameter shifts | ≤ 0.2σ | DESI DR1 mocks | arXiv:2405.16657 | Sect. 5.3 |
| ELG redshift error | Lorentzian, w = 8.5 km s⁻¹ | DESI DR1 | arXiv:2405.16657 | Eq. 27 |
| eBOSS QSO redshift error | double Gaussian 150 / 1000 km s⁻¹, F = 4.478 | eBOSS DR16 | arXiv:2007.09003 | Eq. 2 |
| eBOSS QSO catastrophic rate | ≈ 1.5% (> 3000 km s⁻¹) | eBOSS DR16 | arXiv:2007.09003 | Sect. 2.2 |
| eBOSS QSO consensus systematic | σ(fσ8) = 0.011, σ(α_∥) = 0.008, σ(α_⊥) = 0.005 | eBOSS DR16 | arXiv:2007.09003 | abstract |
| Euclid interloper fraction assumed | ≤ 20% | Euclid DR1 forecast | arXiv:2505.04688 | Sect. 8 |
| Euclid fσ8 systematic, minimal model | 1–3% (forecast) | Euclid DR1 mocks | arXiv:2505.04688 | Sect. 8 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Sky-line confusion leaves a redshift spike.** ELG catastrophics pile
  up at z ≈ 1.32 (8600–8700 Å residuals) [src: arXiv:2405.16657,
  Sect. 5.1]; per-fibre spikes appeared at z = 1.5 [src: arXiv:2405.17208,
  Sect. 4]. Test: n(z) per fibre and per period; VI of repeat pairs.
- **Instrument features that vary in time.** A saturated feature in petal
  5 and a petal-6 amplifier instability [src: arXiv:2405.17208, Sects. 4,
  7]. Test: success rate against date, per petal.
- **Large-scale leakage.** Residual exposure, speed and focal-plane trends
  act mostly at k < 0.03 h Mpc⁻¹ [src: Sect. 7]. Test: repeat the χ²_sys
  analysis with the k range of the observable at hand (f_NL, low-k
  full shape).
- **Hemisphere-specific residual.** The QSO exposure-weight effect is in
  NGC (χ²_sys 2.1) not SGC (0.1) [src: Sect. 6]. Test: per-cap χ²_sys.
- **Contamination above design.** Euclid Q1 suggests contamination
  "significantly higher" than the 20% assumed, so the DR1 interloper
  mocks may need to be redone [src: arXiv:2505.04688, Sect. 8].
- **Reconstruction with interlopers** is not yet tested for Euclid; the
  authors defer whether the BAO template is flexible enough [src: same].
- **Dilution mistaken for low growth.** Catastrophics bias fσ8 low by
  diluting the signal (eBOSS QSO RegPT mean 0.3746 with catastrophics
  against 0.3836 without) [src: arXiv:2007.09003, Sect. 2.2, Table 6].

## Reading list
<!-- key: reading-list -->

- Method and application: Krolewski et al. 2024, arXiv:2405.17208 —
  bad-fibre Monte Carlo, residual-trend search, χ²_sys rule, decision not
  to adopt extra weights.
- Method and application: Yu et al. 2024, arXiv:2405.16657 — ELG
  focal-plane correction, catastrophic classes and injection model,
  Lorentzian redshift errors.
- Validation: Smith et al. 2020, arXiv:2007.09003 — eBOSS QSO redshift
  smearing and catastrophic mocks; how they enter the systematic budget.
- Application: Adame et al. 2024, arXiv:2411.12021 (Sect. 5.6) — how DESI
  DR1 full shape carries spectroscopic systematics.
- Forecast and method: Euclid Collaboration: Risso et al. 2025,
  arXiv:2505.04688 — interloper decomposition of ξ and the attenuation
  model.
- Context: Andrade et al. 2025, arXiv:2503.14742 (Sect. V.2) — DR2 relied
  on DR1 spectroscopic tests without re-analysis.

## Not verified
<!-- key: not-verified -->

- How DESI DR1 or DR2 models quasar redshift errors in its BAO or
  full-shape fits (only the eBOSS treatment was read).
- Tables 3–4 of arXiv:2405.16657 (parameter shifts per catastrophic case);
  only the ≤ 0.2σ summary was read.
- The Euclid Q1 contamination level (Le Brun et al. 2025, cited in
  arXiv:2505.04688; not read).
- The section holding Eq. 17 of arXiv:2505.04688 (the HTML text was read
  without reliable section boundaries before Sect. 5.2).
