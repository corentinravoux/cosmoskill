# Data pipelines — open questions

Scope: live method debates in pipelines, known limitations, what the next
data will decide, forecasts (labelled), and stale claims with the paper that
corrects them.
Snapshot: 2026-10-16

Flags: `[src]` abstract read this session; `[src: Sect. n]` body read;
`[sec]` named secondary source; `[der]` derived here.

## 1. Method debates
<!-- key: method-debates -->

### 1.1 Redshift fitters: fast PCA templates, physical archetypes or networks
<!-- key: redshift-fitters-fast-pca-templates-physical -->

- Side A, PCA templates. Fast and flexible; DESI Redrock met every
  survey-validation requirement with purity above 99% for all classes
  (arXiv:2209.14482) [src].
- Side B, physical models. PCA fits have no physical constraint beyond
  positive [O II] and produce false fits on spectra with calibration steps
  [src: arXiv:2209.14482, Sect. IV.13]; archetype refits cut catastrophics by
  10–30% and false positives on sky fibres by 5–40% (arXiv:2405.19288)
  [src].
- Side C, networks. QuasarNET matches expert VI on BOSS (arXiv:1808.09955)
  [src] and is a required DESI after-burner (arXiv:2503.14745) [src];
  contrastive networks for LBGs are trained on small VI samples
  (arXiv:2608.10080) [src]. The open point is how a network trained on VI
  generalises to the depth and conditions of a full survey.
- State. DESI keeps Redrock plus after-burners; the archetype refit shows
  the main pipeline is "generally robust" (arXiv:2405.19288) [src].

### 1.2 Imaging-systematics weights: regression or forward model
<!-- key: imaging-systematics-weights-regression-or -->

- Regression on maps (linear, neural network, random forest) is standard
  (arXiv:1907.11355, arXiv:2105.13540) [src], but every regression has its
  own bias and variance (arXiv:1509.08933, arXiv:2007.14499) [src], and the
  spread between methods is carried as a systematic in DES Y3
  (arXiv:2105.13540) [src].
- Forward modelling by injection captures the real pipeline: Balrog matches
  density fluctuations within 1% (arXiv:2012.12825) [src]; Obiwan validated
  the eBOSS ELG weights (arXiv:2007.08992) [src]; for DESI DR1 ELGs it
  reproduced trends only qualitatively [sec: cosmo-galaxy-clustering,
  systematics Sect. 5].
- A middle route splits the sample: property-dependent linear weights for
  DESI DR2 ELG subsamples help in ~10% of subsamples, the neural-network
  baseline remaining optimal for the full sample (arXiv:2606.18581) [src].

### 1.3 Randoms: redshifts from the data or from a model
<!-- key: randoms-redshifts-from-the-data-or-from-a-model -->

Sampling random redshifts from the data matches dN/dz exactly and nulls
radial modes; DESI states it will revisit the choice if dN/dz can be
forward-modelled [src: arXiv:2405.16593, Sect. 7.2]. Slitless surveys must
model detection anyway (arXiv:2511.20856) [src].

### 1.4 CMB map-making: filter-and-bin or unbiased maximum likelihood
<!-- key: cmb-map-making-filter-and-bin-or-unbiased -->

- Filtering with an explicit correction gives unbiased maps, but those maps
  "may not straightforwardly lead to the best constraints on the power
  spectra"; simpler map-makers that leave the filter to later steps "may
  perform equally well" (arXiv:1608.01624) [src]. SPT-3G filters and bins
  (arXiv:2603.20163) [src]; SO validates an approximate transfer-function
  route for filtered SAT maps (arXiv:2502.00946) [src].
- ACT DR6 dropped TOD filtering to keep low ℓ and solves a maximum-likelihood
  problem with model-error terms [src: arXiv:2503.14451, Sects. III.3, V.2];
  model error can still cause O(1) large-scale power loss that simulations
  without the error do not see (arXiv:2210.02243) [src].
- Half-wave-plate experiments add a third route, marginalising slow
  unpolarised signals (arXiv:2606.31720) [src].

### 1.5 Deblending: deterministic catalogues or probabilistic scenes
<!-- key: deblending-deterministic-catalogues-or -->

SCARLET leads on segmentation and reconstruction, DeepDISC on faint
recall (arXiv:2607.28475) [src]; BLISS outputs posteriors over the number
and type of sources (arXiv:2601.03422) [src]. Unrecognised blends remain
14.9–18.0% in Rubin DP1 against HST (arXiv:2610.10986) [src], and no
release yet ships a probabilistic catalogue as its main product.

### 1.6 Fibre-assignment corrections when targets outnumber fibres
<!-- key: fibre-assignment-corrections-when-targets -->

PIP weights are unbiased in principle (arXiv:1703.02070) [src] and were
produced for DESI from alternate target ledgers (arXiv:2404.03006) [src],
but in deep surveys the per-field fibre limit also erases long modes and
favours underdense regions, which needs per-field and individual weights
(arXiv:1912.06583) [src]; individual weights correct galaxy–lensing
cross-spectra to ~1% but not the auto-spectrum at k ≳ 0.2 h Mpc⁻¹
(arXiv:2110.04883) [src]. Whether PIP, the θ-cut or a modified statistic
(arXiv:1611.04635) [src] is the right default for 4MOST and PFS is open; the
DESI choice is in `cosmo-galaxy-clustering`.

### 1.7 Visual inspection as the truth table
<!-- key: visual-inspection-as-the-truth-table -->

Every success and purity number for DESI is relative to VI of deep co-adds
of a few thousand to ten thousand spectra per class (arXiv:2208.08516,
arXiv:2208.08517) [src]; eBOSS inspected 320,161 quasar spectra
(arXiv:2007.09001) [src]. VI found spurious pipeline features as well as
redshift errors (arXiv:2208.08516) [src]. The limits are the size of the
inspected samples, their depth relative to the main survey, and the
dependence of new networks on them (arXiv:2608.10080) [src].

## 1b. Known tensions between pipelines and releases
<!-- key: known-tensions-between-pipelines-and-releases -->

- DES Y3 excluded the g band from lensing because its PSF models were not
  accurate enough; Y6 restored it with colour-dependent Piff models
  (arXiv:2501.05781) [src].
- In Rubin DP1 the production extendedness classification and DeepDISC
  agree within ~1 percentage point on a common sample (97.4% vs 98.5%),
  but DeepDISC labels more faint sources as stars and independent labels
  favour the random forest in most disagreements (arXiv:2610.10986) [src].
- ACT DR6 mapmaker transfer function from pure simulations disagreed with
  the one measured against Planck until model error was traced
  [src: arXiv:2503.14451, Sect. V.2].
- The HSC SDSS-heritage deblender performs adequately in most of the survey
  but fails in most cluster cores, which matter for HSC science
  [src: arXiv:1705.06766, Sect. 4.8.3].
- Planck 2018 end-to-end simulations differ from the data at the
  few-percent level after component separation (arXiv:1807.06208) [src].

## 1c. Forecasts
<!-- key: forecasts -->

- LSST full depth (**forecast**): ~62% of detected galaxies blended at the
  1% flux level and N_eff lowered by ~18%, to at most 39.4 arcmin⁻² in r
  (arXiv:2103.02078) [src].
- LSST-like photometric clustering (**forecast**): an anisotropic n(z)
  biases σ8 low by 1.7σ and Ω_m high by 1.4σ if a global n(z) is used
  (arXiv:2609.15542) [src].
- DESI fibre assignment (**forecast**, mocks): after three or more passes
  the BAO errors match those of a randomly sampled survey
  (arXiv:1805.00951) [src].

## 2. What the next data will decide
<!-- key: what-the-next-data-will-decide -->

- Euclid DR1: whether automated NISP redshifts can be made reliable as the
  extracted sample deepens; in Q1 under 10% of spectra allow a redshift
  [src: arXiv:2503.15302, Sect. 9], and 89% success needs tuned cuts
  (arXiv:2503.15308) [src].
- Rubin LSSTCam: global astrometric calibration, differential chromatic
  refraction (not corrected in DP1) and PSF size bias (both Piff variants
  underestimate it in DP1) [src: arXiv:2603.23786, Sects. IV.3.2, V.2, V.3].
- DESI DR2 and beyond: whether PIP weights become usable for the fits, and
  whether DES-region ELGs need separate treatment for all statistics
  (arXiv:2606.18581) [src]; the PIP question is tracked in
  `cosmo-galaxy-clustering`.
- 4MOST and PFS: the first full-scale tests of assignment corrections when
  targets outnumber fibres (arXiv:1912.06583, arXiv:2110.04883) [src].
- Simons Observatory: the first on-sky test of half-wave-plate map-makers
  and automated daily reduction at its data volume (arXiv:2406.10905,
  arXiv:2606.31720) [src].

## 3. Stale claims and misconceptions
<!-- key: stale-claims-and-misconceptions -->

| Claim that still circulates | Correction |
|---|---|
| Fibre spectrographs cannot sky-subtract well enough for faint targets | Cross-beam switching and dual stare reach < 1% (arXiv:1609.06142) [src]; PCA reaches the Poisson regime over long integrations (arXiv:1007.0648) [src] |
| Averaging the samples in each pixel is a good enough CMB map | It generally destroys information for total-power detectors (arXiv:astro-ph/9611130) [src] |
| End-to-end simulations validate a map-maker | Not if they omit the model error; ACT DR6 converged in simulations and was biased on data (arXiv:2210.02243; arXiv:2503.14451, Sect. V.2) [src] |
| Pipeline redshift errors can be used as given | BOSS underestimates by 1.19–2 (arXiv:1207.7326) [src]; redmonster overestimates by ~54% (arXiv:1607.02432) [src] |
| The Euclid Q1 redshift catalogue is a cosmology sample | Every H_E < 22.5 source gets a redshift; under 10% of spectra allow one [src: arXiv:2503.15302, Sect. 9] |
| DESI DR1 spectral variances are exact | Flux-calibration variance is underestimated, up to a factor 5 at S/N ~ 100 per pixel [src: arXiv:2503.14745, App. E] |
| DESI DR1 v0 redshift catalogues are final | FIBERMAP metadata errors (e.g. STD_FIBER_RA wrong for ~17% of targets) are fixed only in zcatalog v1 [src: arXiv:2503.14745, App. E] |
| Template subtraction removes imaging systematics without bias | Biased in its original form; basic mode projection is unbiased (arXiv:1509.08933) [src] |
| The co-add PSF can be modelled from stars on the co-add | Dithers make it discontinuous; HSC combines input PSF models instead [src: arXiv:1705.06766, Sect. 3.3.1] |
| A survey-design area or density is a delivered one | Legacy Surveys' ~14,000 deg² is the design (arXiv:1804.08657) [src]; current areas are in `cosmo-surveys-facilities` |

## Not verified
<!-- key: not-verified -->

- Whether PIP weights entered the DESI DR2 fits: not read here; see `cosmo-galaxy-clustering`.
- Simons Observatory first-light map quality: no paper read.
