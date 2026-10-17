# Survey simulations, selection effects and bias corrections — cosmo-supernovae dossier

Scope: how the inputs of a bias-correction simulation are measured, how
BBC turns the simulation into per-SN corrections (grid, interpolation,
dimensions, fit), how the simulation is validated against the data, what
the correction is physically made of, and how to choose between BBC,
selection functions inside a hierarchical likelihood and volume-limited
samples.
Snapshot: 2026-10-17.
From: DES-SN5YR methods (arXiv:2401.02945), Sects. III.4 and IV; Union3
(arXiv:2311.12098), Sect. IV.5; Unite (arXiv:2609.05053), Sect. 4.5; ZTF
DR2 sample simulations (arXiv:2409.04346, Sect. 5); Roman HLTDS simulation
(arXiv:2506.04402), Sect. IV.4.

Already in L2, not repeated here: the four BBC steps, the size of the
corrections, the dimensionalities, the original cell sizes and the
reference-cosmology dependence in
`physics-and-methods.md#selection-bias-bbc-and-beams`; the selection-bias
row of each compilation in `physics-and-methods.md#what-each-main-analysis-did`;
the comparison trap and its 38 % share in
`systematics.md#selection-bias-malmquist-and-its-dependence-on`; the
reference-cosmology test in
`systematics.md#reference-cosmology-in-bias-corrections`; the colour and
dust population model that the simulation draws from in
`deep/dust-intrinsic-scatter.md`.

## How it is done
<!-- key: how-it-is-done -->

Notation: `Delta mu_bias` (or `delta mu_bias`) is the mean difference
between the distance a simulated SN would be assigned and its true distance
modulus, in a cell of observables; "BiasCor" is the large simulation used to
compute it; `E_spec` is the spectroscopic selection efficiency; `S/N` the
signal-to-noise ratio.

### Step 1. Measure the instrument response with fake supernovae
<!-- key: step-1-measure-the-instrument-response-with -->

DES-SN3YR overlaid 10 000 fake SN light curves on the survey images and ran
them through the difference-imaging and scene-modelling photometry
pipelines [src: Kessler et al. 2019, arXiv:1811.02379, Sect. 4]. They give
two inputs to the catalogue-level SNANA simulation:

- **Detection efficiency versus S/N** in each filter, reaching 50 % around
  `S/N ~ 5`. The S/N is computed from the true flux and the noise model in
  the same way as in the simulation, not from measured fluxes [src:
  Sect. 7.1].
- **Flux-uncertainty scale** `Ŝ_sim`, the ratio of the RMS of
  (true − measured) flux on fakes to the same RMS in the simulation
  (Eq. 14), mapped against local surface brightness; after it, fake and
  simulated uncertainties agree within 5 % [src: Sect. 6.4]. A matching
  factor `Ŝ_SMP` rescales the data uncertainties (Eq. 15) [src].

Why fakes are not the bias correction themselves: their light-curve model is
deliberately unrealistic (no intrinsic scatter, tuned redshift
distribution), 10 000 is "more than an order of magnitude smaller" than a
BiasCor sample needs, and the result would only hold for one SN model; SNANA
is about 10^5 times faster than image-level simulation [src: Sect. 4].
Fakes are placed on at most about 1 % of galaxies per 0.05 redshift bin,
because a fake blocks real detections on its galaxy for that season [src].

### Step 2. Model the trigger and the spectroscopic selection
<!-- key: step-2-model-the-trigger-and-the-spectroscopic -->

- **Candidate logic**: two detections on separate nights within 30 days
  [src: arXiv:1811.02379, Sect. 7.1].
- **Live spectroscopic confirmation** cannot be simulated (eight
  telescopes, weather, classification, some human decisions), so
  `E_spec` is empirical: the data/simulation ratio of the peak i-band
  magnitude, simulated with `E_spec = 1`, fitted with a sigmoid
  `E_spec = s0 [1 + exp(s1 i_peak − s2)]^-1` (Eq. 17) by emcee with Poisson
  errors; its normalisation is arbitrary for the bias [src: Sect. 7.1]. The
  fit needs stretch and colour populations that themselves need `E_spec`;
  rather than iterate, external populations are used, whose dependence on
  `E_spec` was shown to be negligible [src].
- **Low-redshift samples**: either magnitude limited, with one `E_spec` in
  peak B magnitude (a one-sided Gaussian), or volume limited, with
  populations made redshift dependent (`x1 → x1 + 25 z`, `c → c − 1 z`); the
  second is carried as a systematic and called conservative because "there
  is no physical motivation for this redshift dependence" [src: Sect. 7.2].
  DES-SN5YR states that targeted low-z surveys' selection "can only be
  inferred fudging simulations to match the data" [src: arXiv:2401.02945,
  App. A].
- **Host-redshift selection (photometric samples)**: the main selection in
  DES-SN5YR is the need for a host spectroscopic redshift; its efficiency is
  modelled against total host magnitude, and a 0.2 mag shift of that curve
  is a systematic [src: arXiv:2401.02945, Sect. VI.4.3]. Hosts are drawn
  from a deep-coadd catalogue with SOM photometric redshifts; a shallower
  catalogue is the systematic variant [src: Sects. IV.4, VI.4.2].

### Step 3. Generate the populations
<!-- key: step-3-generate-the-populations -->

Stretch and colour parent populations are fitted so that the simulated
distributions after selection match the data. Popovic et al. 2021 use an
asymmetric generalised normal (Eq. 4; shape `n = 3` for `x1`, `n = 2` for
`c`) for high-z surveys and a double Gaussian for the double-peaked low-z
and Foundation stretch distributions (Eq. 5) [src: arXiv:2102.01776,
Sect. IV.1]. The fit uses a migration matrix from a simulation with flat true
`x1` and `c`, giving the probability that a true value in bin `i` is
measured in bin `j` after selection, noise and scatter, and minimises the
data–prediction χ² (Eqs. 6–7) [src]. The colour, dust and scatter model is
the subject of `deep/dust-intrinsic-scatter.md`.

### Step 4. Compute the correction on a grid
<!-- key: step-4-compute-the-correction-on-a-grid -->

| Version | Corrected quantity | Grid | BiasCor size | Source |
|---|---|---|---|---|
| BBC5D (2017) | each of `m_B`, `x1`, `c` (Eq. 11) | `{z, x1, c}` cells 0.05, 0.50, 0.05; `alpha_SIM ± 0.04`, `beta_SIM ± 0.4` on a 2 × 2 grid | 500 000 after cuts | arXiv:1610.04677, Sect. V.2 |
| DES-SN3YR | same | α {0.10, 0.24}; β {2.7, 3.5} (G10) or {3.3, 4.3} (C11) | 1.3 × 10^6 | arXiv:1811.02379, Sect. 9 |
| BBC7D | same, plus a host shift | adds `theta = ±0.06` and discrete `M*` bins | | arXiv:2102.01776, Sect. V.2 |
| BBC4D ("BBC-BS20") | the distance (Eqs. 14–15) | `{z, x1, c, M*}`; no α, β grid | | arXiv:2102.01776, Sect. V.3 |

Rules in the 2017 implementation [src: arXiv:1610.04677, Sect. V.2]:
corrections are `sigma_mu^-2`-weighted averages in each cell, interpolated
linearly; a cell needs at least 3 events and an event at least 3 valid
cells, or it is rejected, which also removes contaminants; the simulation
extends beyond the last data redshift (to 1.15 for data to 1.10) so the top
bin is interpolated, not extrapolated. Shallow and deep fields, 1 mag apart
in depth, get separate corrections [src: Sect. V.1].

Reasons for each step up:

- **7D**: `gamma` fitted with 5D corrections is biased when `c` and `x1`
  correlate with host mass. A shift `+theta` is added to a random half of
  the BiasCor and `−theta` to the other, and each event's host term is
  interpolated between them (Eq. 12); `M*` is binned, not interpolated,
  "to avoid interpolating across the luminosity step" [src:
  arXiv:2102.01776, Sect. V.2].
- **4D**: BBC5D cannot handle a dust model, which has a colour-dependent
  scatter, two colour slopes (`beta_SN`, `R_V`) and intrinsic quantities
  that differ from SALT `c` and `beta`. The α, β grid is dropped "because the
  BS20 simulations are forward-modeled and result in BBC-fitted α and β that
  are in agreement with that of the data", and `theta` is dropped because
  the model predicts the step [src: Sect. V.3]. With 5D and SALT2 the
  distance and parameter forms agree [src]. The effective `beta_true =
  2.87` used with a dust model is in L2.

### Step 5. Fit the bias-corrected Hubble diagram
<!-- key: step-5-fit-the-bias-corrected-hubble-diagram -->

Each event's likelihood is the BEAMS mixture
`L_i = [P_Ia/P_tot] D_Ia + [S_CC (1 − P_Ia)/P_tot] D_CC` (arXiv:1610.04677,
Eqs. 6–7), with `D_Ia` a normalised Gaussian in the Hubble residual (Eq. 8)
and `D_CC` a map from contaminant simulations (Eq. 9); the Gaussian
normalisation "cannot be arbitrarily removed", which is why corrections are
needed in the first place [src: Sect. V.1]. Flat priors: `alpha` [0.02,
0.30], `beta` [1, 6], `S_CC` [−0.1, 5], bin offsets [−5, 5] (Table 3) [src].
The fit returns distance offsets in redshift bins at a fixed reference
cosmology; cosmology is then fitted to them (Eq. 15; 22 bins in the 2017
tests) [src: Sect. V.6]. Roman forecasts use 45 bins with width
proportional to `(1+z)^2`, an unbinned diagram, and a "rebinned" one of 4
stretch × 8 colour × 45 redshift cells (919 non-empty on average) to keep
unbinned self-calibration at lower cost [src: arXiv:2506.04402,
Sect. IV.4]. For host photometric redshifts BBC computes the true distance
at the measured redshift, valid only if the host `z_phot` PDF is well
modelled [src].

### Step 6. Validate the simulation against the data
<!-- key: step-6-validate-the-simulation-against-the-data -->

- **Distributions**: DES-SN3YR compared peak magnitude (forced to match by
  construction of `E_spec`), redshift, Milky Way extinction, cadence gaps,
  maximum S/N per band and host surface brightness; agreement is good except
  a simulated excess at S/N > 100 and poor agreement for hosts fainter than
  24 mag arcsec^-2, where `Ŝ_sim → 1` limits the impact [src:
  arXiv:1811.02379, Sect. 8]. Only `E_spec` and the populations are tuned;
  all other inputs are measured [src].
- **Pass criterion**: a reduced χ² between 0.7 and 3.0 per survey for
  redshift, SALT parameters and host mass, HST excepted for its small
  numbers [src: arXiv:2609.05053, Sect. 5.2, following DES-SN5YR and
  DES-Dovekie].
- **Per-survey Hubble residuals** after unblinding found, in Unite, a 2σ
  SNLS offset traced to a position-dependent filter transmission not
  modelled (reduced to 0.9σ once included) and an unintended χ²/dof cut on
  high-S/N low-z data (five calibrator light curves recovered) [src:
  Sect. 5.2].
- **Coverage and cosmology recovery** on simulated samples: see L2.

## What the correction is made of
<!-- key: what-the-correction-is-made-of -->

Kessler et al. decompose the bias for red DES events (`c > 0.06`), where it
reaches about 0.4 mag at the highest redshift [src: arXiv:1811.02379,
Sect. 9]:

1. No intrinsic scatter, only `x0` fitted: about 0.01 mag, because only the
   two trigger detections are selected and the other few dozen epochs are
   unbiased.
2. G10 scatter, only `x0` fitted: about 0.1 mag, since selection prefers
   positive brightness fluctuations correlated across epochs and bands.
3. All three parameters fitted: much larger, "mainly because of the bias in
   fitted color"; measured-minus-true colour RMS is about 0.5 of the true
   colour spread, 0.7 at z > 0.5.

Their conclusion: the bias "is primarily associated with intrinsic scatter
and light-curve fitting", not with Malmquist bias in the narrow sense [src].
Averaged over colour it is zero at low redshift and about 0.05 mag at high
redshift, model dependent; changing α from 0.10 to 0.24 moves it by up to
0.03 mag, changing β by about 1 by up to 0.01 mag [src].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Correcting fitted parameters or the distance (1D)
<!-- key: correcting-fitted-parameters-or-the-distance-1d -->

With the correct α and β in the simulation, a redshift-only correction of
the distance works as well as BBC5D with 9 % larger uncertainty; with the
biased values a χ² fit returns (α = 0.15, β = 3.0 against true 0.14, 3.2)
it gives a `w` bias of 0.016 ± 0.004 [src: arXiv:1610.04677,
Sect. VIII.2]. The authors locate the problem in correcting `mu` with
predetermined α, β rather than in the dimensionality [src]. The DES-SN3YR
step changed from 0.040 to 0.066 mag between 5D and 1D (L2).

### Simulated corrections (BBC) or a selection function in the likelihood
<!-- key: simulated-corrections-bbc-or-a-selection -->

- **UNITY1.5**: an error-function probability of selection in observer-
  frame magnitude, with each survey's depth marginalised (following Steve)
  rather than fixed; observer magnitudes are mapped to affine combinations
  of `m_B` and `c` per redshift, e.g. for SNLS `m_i = m_B − 0.8` at
  z = 0.8 and `m_i = m_B − 0.5 + 1.0 c` at z = 1.1 [src: arXiv:2311.12098,
  Sect. IV.5]. The fitted DES depths come out shallower than their priors
  "because both are limited by the depth of spectroscopic selection"; prior
  widths do not drive the cosmology [src].
- **Steve**: the selected-data likelihood
  `P(S|data,θ) P(data|θ) / ∫ P(S|D,θ) P(D|θ) dD` (arXiv:1811.02381, Eq. 11)
  has a denominator the authors could not evaluate tractably in all
  parameters ("a brief dismissal of many months of struggle"); they reduce
  it to apparent magnitude and redshift (Eq. 13), replace the skewed colour
  population by a Gaussian with the skew-normal mean and variance (dropping
  skewness "resulted in highly biased population recovery"), and fit an
  error function (or a skew normal for saturated or combined low-z samples)
  to SNANA efficiency ratios, inflating their errors until χ²_red = 1 to get
  a covariance used as a prior [src: Sect. IV.4.5]. What this misses,
  stated: variation of the selection function with cosmology or
  spectroscopic efficiency [src].
- The cost of BBC in return is its reliance on one simulated population and
  reference cosmology (L2), which is what these approaches marginalise.

### Avoid the correction: volume-limited samples
<!-- key: avoid-the-correction-volume-limited-samples -->

ZTF DR2 compares, by Kolmogorov–Smirnov tests on simulations, input and
post-selection stretch and colour distributions as a function of redshift
limit; they agree within 3σ to `z_lim ≈ 0.07`, colour diverging beyond
0.05; the adopted limit `z ≤ 0.06` gives about 1000 SNe [src:
arXiv:2409.04650, Sect. 5.2 and abstract]. This works only at low redshift
and discards most of the sample; it is used for standardisation studies, not
for a Hubble diagram over redshift.

### Same SN, two selection functions
<!-- key: same-sn-two-selection-functions -->

The DES events in Pantheon+ are the 207 brightest, spectroscopically
confirmed; DES-SN5YR keeps 1635 photometrically classified events with host
redshifts. Applying both selections to one DES-like simulation ten times the
data reproduces the observed ~0.02 mag difference in bias corrections at
z > 0.1 to 5 mmag; at z < 0.1 the selections and corrections coincide [src:
arXiv:2501.06664, Sect. 5]. Separately, model updates shifted all
DES-SN5YR corrections by a constant 0.04 mag relative to Pantheon+, with no
effect on cosmology [src: Sect. 4.1].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Fakes overlaid on images | 10 000 | DES-SN3YR | arXiv:1811.02379 | Sect. 4 |
| Detection efficiency | 50 % at S/N ~ 5 | DES-SN3YR | arXiv:1811.02379 | Sect. 7.1 |
| Flux-error agreement after `Ŝ_sim` | within 5 % | DES-SN3YR | arXiv:1811.02379 | Sect. 6.4 |
| Simulation vs image-level speed | ~10^5 | SNANA | arXiv:1811.02379 | Sect. 4 |
| Trigger | 2 detections, separate nights, within 30 d | DES-SN | arXiv:1811.02379 | Sect. 7.1 |
| Volume-limited low-z variant | `x1 → x1 + 25 z`, `c → c − 1 z` | DES-SN3YR systematic | arXiv:1811.02379 | Sect. 7.2 |
| Host-redshift efficiency shift | 0.2 mag | DES-SN5YR systematic | arXiv:2401.02945 | Sect. VI.4.3 |
| BiasCor sizes | 5 × 10^5 (2017 tests); 1.3 × 10^6 (DES-SN3YR) | | arXiv:1610.04677; arXiv:1811.02379 | Sect. V.2; Sect. 9 |
| Cell rules | ≥ 3 events per cell, ≥ 3 cells per event | BBC | arXiv:1610.04677 | Sect. V.2 |
| Host shift in 7D | `theta = ±0.06`; ~0.02 mag at high z | BBC7D | arXiv:2102.01776 | Sect. V.2 |
| BBC priors | α [0.02, 0.30], β [1, 6], `S_CC` [−0.1, 5] | BBC | arXiv:1610.04677 | Table 3 |
| Redshift bins | 22 (2017 tests); 45 ∝ (1+z)^2 (Roman) | | arXiv:1610.04677; arXiv:2506.04402 | Sect. V.6; Sect. IV.4 |
| Rebinned diagram | 4 × 8 × 45, 919 non-empty | Roman forecast | arXiv:2506.04402 | Sect. IV.4 |
| Bias components (red events, high z) | 0.01 → ~0.1 → ~0.4 mag | DES-SN3YR sims | arXiv:1811.02379 | Sect. 9 |
| Colour error / colour spread | ~0.5; 0.7 at z > 0.5 | DES-SN3YR sims | arXiv:1811.02379 | Sect. 9 |
| 1D vs 5D | +9 % error; `w` bias 0.016 ± 0.004 with wrong α, β | simulations | arXiv:1610.04677 | Sect. VIII.2 |
| Data–simulation criterion | reduced χ² 0.7–3.0 per survey | Unite, DES | arXiv:2609.05053 | Sect. 5.2 |
| Volume limit | `z ≤ 0.06`, ~1000 SNe | ZTF DR2 | arXiv:2409.04650 | Sect. 5.2 |
| Bias-correction difference, two DES selections | ~0.02 mag at z > 0.1; sims match to 5 mmag | Pantheon+ vs DES-SN5YR | arXiv:2501.06664 | Sect. 5 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Circular `E_spec` and populations.** Each needs the other; DES-SN3YR
  breaks the loop with external populations [src: arXiv:1811.02379,
  Sect. 7.1]. Test: vary `E_spec` and refit populations.
- **Unmodelled inefficiency on bright hosts.** Subtraction artefacts lower
  detection efficiency on bright galaxies more than Poisson noise predicts;
  the simulation models the extra scatter but not the inefficiency, and
  fakes show it does not affect the two-detection trigger for nearby SNe Ia
  [src: arXiv:1811.02379, Sect. 7.1]. A survey with fewer epochs should
  recheck this.
- **Unknown low-z selection.** Targeted searches are neither magnitude nor
  volume limited; both are run [src: arXiv:1811.02379, Sect. 7.2], and the
  choice remains tuned to the data [src: arXiv:2401.02945, App. A].
- **Hidden cuts and missing instrument features.** An unintended χ²/dof cut
  on bright low-z light curves and a missing position-dependent SNLS filter
  curve were found only after unblinding, through per-survey residuals
  [src: arXiv:2609.05053, Sect. 5.2]. Test: per-survey residual plot before
  unblinding.
- **Interpolation limits.** `theta` must exceed the host shift for the 7D
  interpolation to be valid, and the top redshift bin needs simulated events
  beyond it [src: arXiv:2102.01776, Sect. V.2; arXiv:1610.04677,
  Sect. V.2]. Events without three valid cells are dropped; count them.
- **Host photometric redshifts.** BBC is reliable only if the host `z_phot`
  PDF is modelled correctly, which simulations cannot test [src:
  arXiv:2506.04402, Sect. IV.4].
- **Selection function simplified in hierarchical models.** Steve reduces
  selection to magnitude and redshift and does not vary it with cosmology
  [src: arXiv:1811.02381, Sect. IV.4.5]; UNITY assumes an error function per
  survey [src: arXiv:2311.12098, Sect. IV.5].
- **Comparing corrected distances object by object.** Different selections
  give different corrections for the same SN [src: arXiv:2501.06664,
  Sect. 5]; compare bias-corrected binned means instead.
- **Constant offsets read as physics.** A uniform 0.04 mag change in
  corrections between releases is absorbed by `M` [src: arXiv:2501.06664,
  Sect. 4.1].

## Reading list
<!-- key: reading-list -->

- Foundation: Kessler & Scolnic 2017, arXiv:1610.04677 — the BBC
  likelihood, grid rules and the 1D-versus-5D test.
- Method: Kessler et al. 2019, arXiv:1811.02379 — fakes, trigger, `E_spec`,
  noise scale, data–simulation comparisons, what the bias is made of.
- Method: Popovic et al. 2021, arXiv:2102.01776 — host-dependent
  populations, 7D and 4D corrections.
- Application: Vincenzi et al. 2024, arXiv:2401.02945 — BBC4D with a dust
  model, host-redshift selection, validation.
- Application: Camilleri et al. 2026, arXiv:2609.05053 — pass criteria and
  what per-survey residuals caught.
- Alternative: Rubin et al. 2023, arXiv:2311.12098 — selection function in
  observer-frame magnitude inside UNITY.
- Alternative: Hinton et al. 2019, arXiv:1811.02381 — selection in a
  hierarchical likelihood and its approximations.
- Alternative: Amenouche et al. 2024, arXiv:2409.04650 — defining a
  volume-limited sample.
- Critique: Vincenzi et al. 2025, arXiv:2501.06664 — selection-dependent
  corrections of the same SN.
- Forecast: Kessler et al. 2025, arXiv:2506.04402 — BBC for a photometric
  Roman sample.

## Not verified
<!-- key: not-verified -->

- Scolnic & Kessler 2016 (SK16) population method, D'Andrea et al. 2018
  (DES spectroscopic targeting) and the DES host-redshift efficiency paper
  cited by DES-SN5YR as Vincenzi et al.: named in the papers read, not read.
- Armstrong et al. (coverage of BBC contours) and Kessler et al. 2023
  (unbinned BBC for photometric samples): see L2; not reread.
- The BBC4D cell sizes used in Pantheon+ and DES-SN5YR were not found in the
  sections read.
