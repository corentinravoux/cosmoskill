# Data pipelines — results

Scope: measured pipeline performance — redshift success rates, purities,
catastrophic-failure fractions, sky-subtraction residuals, astrometric and PSF
residuals, deblending and completeness figures, map-making transfer
functions — with the dataset and citation for each, and what superseded what.
Snapshot: 2026-10-16

Flags: `[src]` abstract read this session; `[src: Sect. n]`, `[src: Table n]`
body read; `[sec]` named secondary source; `[der]` derived here.

## 1. Spectroscopic redshift performance
<!-- key: spectroscopic-redshift-performance -->

| Survey, sample | Success or completeness | Purity, catastrophics | Precision | Source |
|---|---|---|---|---|
| BOSS CMASS (DR9) | 98.7% automated classification; 95.4% confirmed galaxies | ~0.2% of confident redshifts wrong | statistical errors underestimated by 1.19–1.34 for galaxies, 2 for quasars (repeats) | arXiv:1207.7326 [src] |
| eBOSS LRG, redmonster (early data) | 90.5% | meets eBOSS requirement | reported errors overestimated by ~54% | arXiv:1607.02432 [src] |
| eBOSS DR16Q | 99.8% complete | 0.3–1.3% contamination | — | arXiv:2007.09001 [src] |
| GAMA autoz | — | — | median 33 km/s | arXiv:1404.2626 [src] |
| BOSS quasars, QuasarNET | 99.52% complete | 99.51% pure; line-confusion failures < 0.2% | — | arXiv:1808.09955 [src] |
| DESI SV, BGS Faint (180 s) | 98.5% | 99.5% | 99.7% within 0.001(1+z) of GAMA | arXiv:2209.14482 [src: Sect. IV.13] |
| DESI SV, LRG (1000 s, Δχ² > 15, z < 1.5) | 98.9% | 99.8% | — | arXiv:2209.14482 [src: Sect. IV.13] |
| DESI LRG main | 98.9% confident after bright-star veto | 0.2% catastrophic; 0.5% stars | — | arXiv:2208.08515 [src] |
| DESI SV, ELG | lower: many targets lack bright lines or fall out of range | > 99.4% | — | arXiv:2209.14482 [src: Sect. IV.13] |
| DESI SV, QSO (Redrock + Mg II + QuasarNET) | 98.0 ± 0.4% | 99.5 ± 0.4% | — | arXiv:2209.14482 [src: Sect. IV.13] |
| DESI SV QSO VI | modified pipeline 94% vs standard 86% of VI quasars | ~99% within 3000 km/s | ~100 km/s precision, ~70 km/s accuracy | arXiv:2208.08517 [src] |
| DESI SV galaxies VI | — | > 99% | ~10 km/s BGS and ELG, ~40 km/s LRG | arXiv:2208.08516 [src] |
| DESI DR1 summary | — | outliers ≤ 0.3% BGS/LRG/ELG; 0.7% QSO z < 2.1; 1.8% QSO z > 2.1 | 10 km/s BGS, ELG; 50 km/s LRG; 20–125 km/s QSO | arXiv:2503.14745 [src: Table 6] |
| DESI archetype refit vs Redrock | 0.5–0.8% higher success and purity for galaxies | catastrophics −10 to −30% on SV tiles; false positives on sky fibres −5 to −40% | — | arXiv:2405.19288 [src] |
| Euclid Q1 SPE (0.9 < z < 1.8, tuned cuts) | 89% | bias < 3×10⁻⁵ in Δz/(1+z) vs DESI | ~10⁻³ | arXiv:2503.15308 [src] |

DESI DR1 also lists wavelength precision 0.025 Å, sky-subtraction
systematics < 1% and spectrophotometric calibration 6–10%
[src: arXiv:2503.14745, Table 6]. DR2 success rates per tracer (BGS 98.8%,
LRG 99.0%, ELG 73.9%, QSO 68.0%) are quoted in `cosmo-galaxy-clustering`
from the DESI DR2 BAO paper [sec: cosmo-galaxy-clustering, systematics Sect. 6].

**Truth tables.** Success and purity are defined against visual inspection
(VI) of deep co-adds: DESI inspected ~2500 BGS, 3500 LRG and 10,000 ELG
spectra (Lan et al. 2023, arXiv:2208.08516) [src] and the quasar survey
(Alexander et al. 2023, arXiv:2208.08517) [src]; eBOSS DR16Q carries VI
for 320,161 spectra (Lyke et al. 2020, arXiv:2007.09001) [src]. Networks
for the next tracers are trained on such VI samples (arXiv:2608.10080) [src].

## 2. Spectral extraction and sky subtraction performance
<!-- key: spectral-extraction-and-sky-subtraction -->

| Pipeline | Quantity | Value | Source |
|---|---|---|---|
| DESI | sky-fibre residuals vs noise model, continuum | consistent with expected noise | arXiv:2209.14482 [src: Sect. IV.7.5] |
| DESI | excess noise on the brightest sky lines (1000 s dark exposures) | 1–3% of the sky level | arXiv:2209.14482 [src: Sect. IV.7.5] |
| DESI | flux calibration, residuals of 9854 DA white-dwarf fits, b arm | within ±2% above ~3700 Å; a ~6% step below ~3700 Å; r and z arms offset by about −1% | arXiv:2209.14482 [src: Sect. IV.9.4] |
| LAMOST DR3+ | sky residual, emission lines and continuum | ~3% each, down to 1.5% on lines in dark time; wavelength calibration ~4.5 km/s | arXiv:1705.02079 [src] |
| LAMOST | PCA after master-sky subtraction | removes a further 25% of the OH residual | arXiv:1705.02079 [src] |
| AAOmega | long-exposure limit of standard sky subtraction | systematic floor reached after 4–10 h | arXiv:1007.0648 [src] |
| FLAMES test | cross-beam switching, dual stare | accuracy and precision < 1% | arXiv:1609.06142 [src] |

## 3. Imaging pipeline performance
<!-- key: imaging-pipeline-performance -->

| Survey, release | Quantity | Value | Source |
|---|---|---|---|
| DECam | single-exposure astrometric solution | 3–6 mas on the focal plane, plus atmosphere (7 mas RMS after Gaia interpolation, 30 s) | arXiv:1703.01679 [src] |
| Euclid Q1 VIS | absolute astrometry vs Gaia | 5 mas | arXiv:2503.15303 [src] |
| Euclid Q1 VIS | image-to-image photometric scatter; FWHM; stack depth | < 0.8%; 0.16″; I_E = 25.6 (10σ, 1.3″ apertures) | arXiv:2503.15303 [src] |
| Rubin DP1 | separation repeatability at 5′ (AM1) | approaching the 10 mas design requirement | arXiv:2603.23786 [src: Sect. V.3] |
| Rubin DP1 | PSF FWHM median / best | ~1.14″ / ~0.58″ | arXiv:2603.23786 [src] |
| Rubin DP1 | ECDFS 5σ point-source co-add depth | u 24.55, g 26.18, r 25.96, i 25.71, z 25.07, y 23.1 | arXiv:2603.23786 [src] |
| Rubin DP1 | detection completeness | 50% at i ≈ 25.83 (vs Hubble Legacy Field); below 90% at i ≈ 23.5 (vs Euclid Q1) | arXiv:2603.23786 [src: Sect. V.6] |
| DES Y3 Gold | photometric uniformity; star–galaxy separation | < 3 mmag; > 98% efficiency, > 99% purity for galaxies at 19 < i < 22.5 | arXiv:2011.03407 [src] |
| KiDS DR4 | 5σ 2″ depth u, g, r, i; r seeing | 24.23, 25.12, 25.02, 23.68; 0.70″ | arXiv:1902.11265 [src] |
| KiDS DR5 | area; median r depth | 1347 deg²; 24.8 (5σ), seeing 0.7″ | arXiv:2503.19439 [src] |
| DECam brighter-fatter | size growth with flux | up to 2% over full dynamic range | arXiv:1402.0725 [src] |

## 3b. Target composition, detection and classification
<!-- key: target-composition-detection-and-classification -->

| Sample or code | Quantity | Value | Source |
|---|---|---|---|
| DESI QSO main selection, VI of deep SV co-adds | composition | 71% quasars, 16% galaxies, 6% stars, 7% inconclusive | arXiv:2208.08511 [src] |
| DESI QSO selection | quasars per deg² delivered | > 200, including 60 at z > 2.1; 20% above requirement | arXiv:2208.08511 [src] |
| DESI ELG main | reliable redshifts | > 400 deg⁻² in each of 0.6 < z < 1.1 and 1.1 < z < 1.6 | arXiv:2208.08513 [src] |
| DESI BGS | redshift success, no strong dependence on conditions (**forecast** from SV) | > 95% | arXiv:2208.08512 [src] |
| eBOSS LRG targets | secure redshifts in SDSS-quality spectra | ≥ 89% | arXiv:1508.04478 [src] |
| BOSS quasar targets | confirmed quasars | ~51.5% | arXiv:1207.7326 [src] |
| DES Y6 Gold | star–galaxy efficiency, contamination (17.5 < i < 22.5) | 98.6%, 0.8% | arXiv:2501.05739 [src] |
| DeepDISC on Rubin DP1, after fine-tuning | galaxy and star completeness, class-aware matching | 84.2% and 49.1% (from 40.2% and 13%) | arXiv:2610.10986 [src] |
| DeepDISC vs production random forest | classification accuracy on a common sample | 97.4% vs 98.5% | arXiv:2610.10986 [src] |

## 4. CMB map-making performance
<!-- key: cmb-map-making-performance -->

| Experiment | Quantity | Value | Source |
|---|---|---|---|
| ACT DR6 | sky area; median combined depth | 19,000 deg²; 10 μK arcmin | arXiv:2503.14451 [src] |
| SPT-3G D1 Main field (2019–2020) | white noise, I, at 95/150/220 GHz | 5.4, 4.4, 16.2 μK arcmin (Q/U 8.4, 6.6, 25.8) over 4% of the sky | arXiv:2603.20163 [src] |
| Planck HFI 2018 | Solar dipole amplitude uncertainty; direction | < 0.35 μK absolute (~10⁻⁴); within 1′ | arXiv:1807.06207 [src] |
| Planck HFI 2018 | calibration bias from the main systematic | measured and corrected at the 10⁻⁴ level | arXiv:1807.06207 [src] |
| Planck NPIPE | Solar dipole; τ from large-scale polarisation | 3366.6 ± 2.7 μK; τ = 0.051 ± 0.006 (ΛCDM) | arXiv:2007.04997 [src] |
| Planck SRoll2 | systematic residuals at large scales | well below detector noise, per end-to-end simulations | arXiv:1901.11386 [src] |
| Planck 2018 component-separated maps | end-to-end simulations vs data | relative biases at the few-percent level | Planck 2018 IV, arXiv:1807.06208 [src] |

## 5. Catalogue completeness and systematics weights
<!-- key: catalogue-completeness-and-systematics-weights -->

| Survey, sample | Quantity | Value | Source |
|---|---|---|---|
| SDSS plates | target sampling rate; non-colliding targets; fibre efficiency | > 92%; > 99%; > 90% | arXiv:astro-ph/0105535 [src] |
| eBOSS DR16 LRG | redshift success; catastrophic (Δz > 1000 km/s) | 98%; < 1% | arXiv:2007.09000 [src] |
| eBOSS DR16 QSO | redshift success; catastrophic (Δz > 3000 km/s) | 95%; 2% | arXiv:2007.09000 [src] |
| eBOSS DR16 QSO | χ²/dof of density vs imaging depth, before → after weights | 776/10 → 6/8 | arXiv:2007.09000 [src] |
| eBOSS QSO CORE (design) | area where a linear imaging model recovers the angular distribution | 96.7% NGC, 76.7% SGC | arXiv:1508.04472 [src] |
| DESI LRG | stellar contamination; imaging robustness | 0.5%; "highly robust against imaging systematics" | arXiv:2208.08515 [src] |
| DESI BGS | stellar contamination; fibre-assignment efficiency (Bright, **forecast** from SV and simulations) | < 1%; > 80% | arXiv:2208.08512 [src] |
| DESI DR1 | bad fibres removed from LSS catalogues | 60 | arXiv:2405.16593 [src: Sect. 4.2] |
| DES Y3 lenses | bias from the decontamination procedure on mocks | ≤ 0.5σ in (Ω_m, b) | arXiv:2105.13540 [src] |
| DES Y3 Balrog | match of injected-object density fluctuations to data | within 1% | arXiv:2012.12825 [src] |
| DES SV Balrog | suppression of variable-selection effects using injections as randoms | ≥ 100× | arXiv:1507.08336 [src] |
| DESI DR2 ELG | subsample-wise linear weights improve on the fiducial NN weights | in ~10% of subsamples; fiducial optimal for the full sample | Hagen et al. 2026, arXiv:2606.18581 [src] |
| PFS-like deep survey | per-field and individual-inverse-probability weights | ξ recovered to < 1% above 10 h⁻¹ Mpc | arXiv:1912.06583 [src] |

DESI DR1 per-tracer assignment completeness and the size of the residual
imaging and fibre-assignment effects on BAO and full shape are in
`cosmo-galaxy-clustering` (systematics, Sects. 4–5).

## 5b. Source-injection results
<!-- key: source-injection-results -->

| Programme | Scale | What it measured | Source |
|---|---|---|---|
| Balrog (DES SV) | introduced | injections as randoms; DES–COSMOS amplitude 1.00 ± 0.09 over 0.004° < θ < 0.2° | arXiv:1507.08336 [src] |
| Balrog (DES Y3) | ~30 million galaxies from Deep Field models on 20% of the footprint | density fluctuations with observing conditions matched within 1%; colours calibrated to ~1–8 mmag; size-overestimate–linked magnitude biases near neighbours | Everett et al. 2022, arXiv:2012.12825 [src] |
| Balrog (DES Y6) | 146 million injections over the full 5000 deg² | percent-level accuracy of object properties; SSI and data catalogues agree, including their correlations with survey properties | Anbajagane et al. 2025, arXiv:2501.05683 [src] |
| Obiwan (Legacy Surveys) | eBOSS ELG portion | 3D clustering consistent with the map-based weights, validating the eBOSS ELG catalogue | Kong et al. 2020, arXiv:2007.08992 [src] |
| Rubin DP1 | 12 patches of ECDFS with DC2 stars and galaxies | completeness and misclassification versus magnitude | arXiv:2603.23786 [src: Sect. V.6] |

## 6. History: what superseded what
<!-- key: history-what-superseded-what -->

| Stage | Earlier | Superseded by | Source |
|---|---|---|---|
| SDSS redshift fitter | BOSS DR9 PCA pipeline (arXiv:1207.7326) | eBOSS redmonster for LRGs (arXiv:1607.02432), then Redrock for eBOSS final cosmology and DESI | arXiv:2209.14482 [src: Sect. V] |
| DESI quasar templates | BOSS templates from a few hundred spectra | two eigenspectrum sets by redshift range in DR1 | arXiv:2305.10426 [src]; arXiv:2503.14745 [src: Sect. III.1.3] |
| DESI reduction | Fuji (EDR), Guadalupe | Iron (DR1): throughput modelled against positioner location for sky subtraction | arXiv:2503.14745 [src: Sect. III.1.3] |
| DESI DR1 catalogues | zcatalog v0 | zcatalog v1 (metadata fixes) | arXiv:2503.14745 [src: App. E] |
| DES PSF | Y1 | Y3 Piff (arXiv:2011.03409), then Y6 colour-dependent Piff with g band | arXiv:2501.05781 [src] |
| DES photometric data set | Y3 Gold, uniformity < 3 mmag, ~390M objects | Y6 Gold, < 2 mmag, 669M objects | arXiv:2011.03407, arXiv:2501.05739 [src] |
| DES injection | Balrog on 20% of Y3 | Balrog on the full Y6 footprint, 146M injections | arXiv:2012.12825, arXiv:2501.05683 [src] |
| KiDS imaging | DR4, 1006 deg² | DR5, 1347 deg², i band re-observed | arXiv:1902.11265, arXiv:2503.19439 [src] |
| HSC sky subtraction | earlier PDRs | PDR3: small-scale sky subtraction before detection | arXiv:2108.13045 [src] |
| HSC deblender | SDSS-heritage templates | SCARLET | arXiv:1705.06766 [src: Sect. 4.8.3]; arXiv:1802.10157 [src] |
| Planck HFI maps | 2015 release (polarisation problems) | 2018 Legacy, then SRoll2 and NPIPE | arXiv:1807.06207, arXiv:1901.11386, arXiv:2007.04997 [src] |
| ACT map-making | DR4 with TOD filtering | DR6 without TOD filtering, ground pickup removed in map space | arXiv:2503.14451 [src: Sect. V.2] |
| Euclid spectroscopy | pre-launch pipelines | Q1 early versions; DR1 pending | arXiv:2503.15302 [src] |

## Not verified
<!-- key: not-verified -->

- DESI DR2 redshift success per tracer: secondary only (from `cosmo-galaxy-clustering`).
- Rubin DP1 PSF residual values of Table 5 beyond the observed means not read.
- HSC blended-object fraction not read.
- 4MOST and PFS on-sky redshift success: not available.
