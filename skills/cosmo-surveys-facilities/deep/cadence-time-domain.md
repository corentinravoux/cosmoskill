# Cadence design for time-domain cosmology surveys — cosmo-surveys-facilities dossier

Scope: how the cadence of a supernova-cosmology survey is specified,
simulated and scored (light-curve quality cuts, signal-to-noise and
redshift-limit metrics, deep-field budgets, filter pairing, gaps and season
length, spectroscopic follow-up), and what each design choice costs, as
read in the Rubin cadence-optimisation papers, the DESC deep-drilling
studies, the Roman time-allocation report and the ZTF scheduler paper.
Snapshot: 2026-10-18.
From: Bianco et al. 2022, Sects. IV–V (survey simulations, Survey Cadence
Optimization Committee); Roman Observations Time Allocation Committee
(arXiv:2505.10574).

Already in L2, not repeated here: the cadence table of the main surveys and
the three factors found by Lochner et al. in
`physics-and-methods.md#cadence-and-time-domain-strategy`; ZTF detector
effects and cross-survey calibration in `systematics.md#time-domain-surveys`;
the Roman HLTDS tier areas in
`surveys-and-data.md#roman-2-4-m-space-telescope-l2-slitless`. The rolling
cadence and its cost to static science are in
`deep/footprint-tiling-depth.md` ("Rolling cadence against uniform depth").
Supernova light-curve fitting, selection-bias corrections and photometric
classification as analyses are in `cosmo-supernovae`.

Notation. SNR_b is the light-curve signal-to-noise ratio in band b summed
over epochs; σ_c the uncertainty on the SALT2 colour c; z_lim (Rubin wide
survey) or z_complete (deep fields) the redshift up to which SNe Ia pass the
quality cuts; N_visits the number of 30 s visits per night and per field;
"budget" the fraction of all survey visits given to a programme.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Fix what a usable light curve is
<!-- key: step-1-fix-what-a-usable-light-curve-is -->

A cadence is judged by the number of supernovae whose light curves pass
cuts tied to the distance error, so the cuts come first.

- **Colour error drives the distance error.** With the SALT2 distance
  modulus μ = m_B + α x₁ − β c − M (Gris et al. 2022, arXiv:2205.07651,
  Eq. 1; x₁ the stretch, c the colour, α, β, M global parameters), β > 3
  and α ≈ 0.16 make the colour term β σ_c dominate the σ_μ budget; with an
  intrinsic scatter of 0.12–0.14 mag, colour errors above about 0.04 add
  significantly, hence the requirement σ_c ≲ 0.04 that defines a
  "well-measured" SN Ia [src: arXiv:2205.07651, Sect. II.1].
- **σ_c maps onto a minimum SNR per band.** For a medium SN Ia with daily
  sampling, σ_c ≤ 0.04 is equivalent to SNR_i ≥ 59, SNR_z ≥ 39 and
  SNR_y ≥ 20 [src: Sect. II.1, Fig. 2 caption], with
  SNR_b = sqrt(Σ_i (f_i^b/σ_i^b)²) summed over light-curve points
  [src: Eq. 3]. The wide-survey proxy of Lochner et al. uses SNR_g > 30,
  SNR_r > 40, SNR_i > 30, SNR_z > 20, which it calls equivalent to
  σ_c ≤ 0.04 [src: arXiv:2104.05676, Sect. V.1.2]. The two sets differ
  because they describe different redshift ranges (the deep-field set
  is for high-z SNe whose rest-frame optical has moved to izy).
- **Sampling cuts.** The DESC requirements in use in 2022 keep grizy
  points with SNR > 1 whose rest-frame mean wavelength lies in
  380–700 nm, at phases (t − t_peak)/(1 + z) between −20 and +60 days, and
  ask for at least 3 points before peak, at least 8 after, at least one at
  phase ≤ 10 and at least one at phase ≥ 20 (as printed), plus
  σ_c < 0.04 [src: arXiv:2210.15690, App. D, Eqs. D1–D2].

### Step 2. Simulate the survey and score it with metrics
<!-- key: step-2-simulate-the-survey-and-score-it-with -->

- **Simulator and metric framework.** Rubin's Operations Simulator (OpSim)
  with the Feature Based Scheduler produces ten-year pointing histories
  with weather, seeing and sky brightness; runs are released in "families"
  that vary one axis (footprint, WFD time fraction, filter distribution);
  the Metric Analysis Framework (MAF) computes science metrics on them
  [src: arXiv:2108.01683, Sect. II]. After the 2018 white-paper call, 173
  OpSim runs were released (v1.5 to v1.7.1) [src: Sect. IV.1].
- **Main SN metric.** On HEALPix pixels of N_side = 64 (0.8 deg²), with
  E(B − V) > 0.25 masked and only griz used, the metric computes
  z_lim = max(z | LC(z) fulfils requirements) and
  N(z < z_lim) = δΩ_pix ∫₀^{z_lim} [ΔT_step/(1+z)] R(z) dV(z), with R(z)
  the SN Ia volumetric rate and ΔT_step the simulated window of peak dates
  [src: arXiv:2104.05676, Sect. V.1.1, Eqs. 3–4]. Full light-curve
  simulation over 18,000 deg² is too slow, hence the pixel approach
  [src: same].
- **Fast proxies.** In the background-limited regime the per-visit error
  follows from the 5σ limiting flux f_{i|5}, and the cadence enters as the
  number of observations per time bin δ_b:
  f_{|5} ⟨δ_b⟩^{−1/2} = 5 sqrt(ΔT) sqrt(Σ_i (f_i^b)²)/SNR_b
  [src: Sect. V.1.2, Eq. 6]. The left side holds the strategy (depth times
  cadence), the right side the supernova; SNR_rate is the fraction of a
  season in which SNR_b(t) reaches its value for median depth and cadence
  [src: same].
- **Transient-discovery weighting (ZTF).** The ZTF scheduler maximises the
  number of exposures per night weighted by the volume each probes,
  V = 10^{0.6(m_lim − 21)}, with m_lim the limiting magnitude
  [src: arXiv:1905.02209, Sect. III, Eq. 1]; a greedy variant uses the
  volumetric speed V̇ ∝ 10^{0.6 m_lim}/(t_exp + t_OH) [src: Eq. 2].
  Cadence and scientific priority are deliberately left out of the metric
  and imposed as constraints of the integer-programming optimisation,
  because "these concerns have no general quantitative relationship to our
  objective function" [src: Sect. III].
- **Combining metrics.** Rubin compares strategies across science areas on
  radar plots (visits per pointing, NEO fraction, galaxy and star counts,
  number of SNe Ia, a 3×2pt figure of merit) [src: arXiv:2108.01683,
  Sect. IV.1, Fig. 5]; the Survey Cadence Optimization Committee (SCOC),
  formed in 2020, advises the Operations Director and remains a standing
  committee through operations [src: Sect. V.1].

### Step 3. Respect the floor set by the requirements document
<!-- key: step-3-respect-the-floor-set-by-the -->

The LSST SRD fixes only a few numbers: at least 15,000 deg² (18,000 by
design) covered uniformly; the sum over bands of the median number of
visits not below 750 (design 825); and at least 1000 deg² (design 2000)
with nearly uniform sampling on 40 s to 30 min [src: arXiv:2104.05676,
Sect. II.2]. A second visit per night within 15–40 min is required for
asteroid detection [src: Sect. VII.1]. Bianco et al. stress that the SRD
"intentionally places minimal quantitative constraints on the observing
strategy", leaving the distribution of visits within a year, between
filters, and the definition of a visit open, and that 10–20% of the time
remains for deep drilling fields (DDFs) and minisurveys [src:
arXiv:2108.01683, Sect. V.1]. Two strategies compliant with the SRD can
differ "even in core features" such as the inter-night gap distribution
[src: Sect. II, Fig. 2 caption].

### Step 4. Design the deep fields as a budget problem
<!-- key: step-4-design-the-deep-fields-as-a-budget -->

For the DDFs the free parameters are the number of fields, the number and
length of seasons, the cadence, the filter allocation and the total
budget [src: arXiv:2205.07651, Sect. III]. The budget is

    DD_budget = N_visits^DD / (N_visits^DD + N_visits^non-DD),
    N_visits^DD = Σ_fields Σ_seasons N_visits,night × seaslen / cad

[src: arXiv:2205.07651, Eqs. 5–6], with N_visits^non-DD = 2,122,176 visits taken from LSST
simulations [src: Sect. III]. Read off the budget contours: for 180-day
seasons, ten seasons per field and a one-day cadence, a 3–15% budget allows
7 to 42 visits per night; with two seasons per field it allows 36 to 208
[src: Fig. 4 caption].

- **Season length.** Observability (20° ≤ altitude ≤ 86.5°, airmass ≤ 1.5)
  shortens the season from 275–200 to 150–100 days as N_visits grows from 1
  to 400; seasons of at least six months are needed to collect at least 80%
  of the SNe Ia of the northernmost fields, and time dilation shortens the
  effective season at high z because SNe at the season edges have poor
  light curves [src: arXiv:2205.07651, Sect. III].
- **Cadence.** "A regular cadence of observation (∼ 3 days max)" and few
  gaps longer than 10 days [src: arXiv:2205.07651, Sect. III].
- **Depth per night for a target completeness.** At one-day cadence and
  180-day seasons, z_complete = 0.80, 0.75, 0.70 need 149, 108 and 81
  visits per night (g/r/i/z/y = 2/9/62/56/20, 2/9/44/38/15, 2/9/33/31/6),
  at a cost of 1.3%, 0.9% and 0.7% of the survey per season
  [src: arXiv:2405.10781, Sect. 2.2.3, Table 3]. With a 5–7% DDF budget it
  is "impossible" to observe five fields for ten years at
  z_complete ≳ 0.75 [src: same].
- **Fields.** COSMOS, ELAIS-S1, XMM-LSS and CDF-S (chosen in 2012) plus the
  Euclid Deep Field South; DESC asked for southern deep-field coverage
  contemporaneous with Euclid and Roman [src: arXiv:2205.07651, Sect. III,
  Table 1]. The SCOC phase-2 recommendation: 5–7% budget, five DDFs for ten
  years, EDFS at half the exposure time over about twice the area, and
  COSMOS brought to ten-year depth within three years, for early photo-z
  calibration and low-surface-brightness science [src: arXiv:2405.10781,
  Sect. 2.1].

### Step 5. Plan the redshifts with the cadence
<!-- key: step-5-plan-the-redshifts-with-the-cadence -->

A photometric sample needs host redshifts, and the follow-up programme is
part of the design.

- The deep-field optimisation assumed about 2500 host redshifts from
  4MOST/TiDES after five years for the southern fields (CDF-S, ELAIS-S1,
  Euclid/Roman) and about 20,000 PFS spectra after ten years for the
  equatorial ones, the PFS plan covering 5 deg² (four fields of view) per
  equatorial field for about 12,000 redshifts [src: arXiv:2205.07651,
  Sect. VIII]. Only half of the well-measured sample has a host spectrum
  under the PFS plan; full use within three years would need about 800 PFS
  redshifts a year with eight fields of view per equatorial field
  [src: Sect. X, item 3].
- TiDES itself forecasts classification of transients to r = 22.5, up to
  30,000 live-transient spectra to z ~ 0.5 and up to 50,000 host redshifts
  to z ~ 1 over five years of 4MOST (**forecast**) [src: arXiv:1903.02476,
  abstract].
- Why spectroscopy rather than photo-z: an LSST minimal target of
  σ_z ≈ 0.02(1 + z_phot) gives a distance-modulus error above 0.10 mag, so
  photo-z SNe add little; the authors recommend designing for
  spectroscopic hosts and treating photo-z SNe as a bonus
  [src: arXiv:2205.07651, Sect. X, item 4].

### Step 6. Design a space time-domain tier around a target S/N
<!-- key: step-6-design-a-space-time-domain-tier-around-a -->

The Roman HLTDS shows the same logic with different levers. The committee
needed "at least two tiers" to cover 0.5 < z < 2.5 with four or five
filters for rest-frame optical and near-infrared colours, and chose
exposure times and cadences "to accumulate a fixed (on average) S/N at the
target redshifts" [src: arXiv:2505.10574, Sect. III.2]. The core
component (two years mid-mission) images a wide tier of 10.68 deg² (north,
ELAIS-N1) plus 7.59 deg² (south, EDFS) in RZYJH with alternating RZY and
RJH sequences every ~5 days, aiming at peak S/N = 20 at z ~ 0.9, and a deep
tier of 1.97 + 4.5 deg² in ZYJHF aiming at S/N = 20 at z ~ 1.7; prism
tiers of 4.5 and 0.56 deg² in the south at ~5-day cadence with 900 s and
3600 s exposures provide redshifts and classification; the core
component takes 158 days [src: Sect. III.2]. "Good" SNe Ia (cumulative
S/N > 40) are expected to number about 7500 (wide) and 6800 (deep)
(**forecast**) [src: same]. A 15-day pilot (eight visits at 20-day cadence)
collects templates, reference prism data and the z > 1 rate; a 7-day
extended component visits the deep tier every ~120 days over the mission
[src: same].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Visit pairs in the same filter or in different filters
<!-- key: visit-pairs-in-the-same-filter-or-in-different -->

Taking the two nightly visits in the same filter is more efficient but
"severely degrades the overall cadence"; transient metrics fall
"dramatically" while static science barely changes [src:
arXiv:2104.05676, Sect. VI.5, Fig. 12]. Different-filter pairs have been
the simulation default since the 2018 call and are one of DESC's
"strongest recommendations" [src: Sects. VI.5, VII.1].

### One 30 s exposure or two 15 s snaps
<!-- key: one-30-s-exposure-or-two-15-s-snaps -->

Two snaps help reject cosmic rays; a single 30 s exposure gains about 7%
efficiency and improves cosmology metrics by up to 20%; its only drawback
for SNe is saturation at z < 0.05 [src: arXiv:2104.05676, Sect. VII.1,
Fig. 13]. The choice was left to commissioning [src: Sect. VI.5].

### Which filters get the cadence
<!-- key: which-filters-get-the-cadence -->

Filter allocation and moon-driven filter swaps make the cadence differ
between bands; for SNe the redder bands matter most, riz need high cadence
and u does not [src: arXiv:2104.05676, Sects. VI.6, VII.1, Fig. 15]. For
the DDFs, swapping u and y with the Moon phase yields more high-z SNe and
should be the default filter-load strategy, according to the authors
[src: arXiv:2405.10781, Sect. 6]. The authors' recommended relief for the
wide survey is to relax the veto on blue bands near full Moon or raise the
nightly visit density by covering less area, aiming at 2–3 days in g, r, i
[src: arXiv:2104.05676, Sect. V.1.4].

### Gaps, weather and conditions
<!-- key: gaps-weather-and-conditions -->

"The cadence of observations is by far the most important parameter for
SNe Ia science, before observing conditions": a pointing in poor
conditions is better than none, and gaps over ~10 days harm the size and
depth of the sample [src: arXiv:2104.05676, Sect. V.1.4]. Weather scenarios
change transient metrics by up to 150% against a small effect on static
metrics, so fields missed by weather should be revisited as soon as
possible [src: Sect. VI.7, Fig. 17]. In the deep-field simulations, large
inter-night gaps cut the SN Ia sample by up to 30%, and large translational
dithers shrink the high-cadence area; the authors ask for a scheduler with
a nightly gap-recovery mechanism [src: arXiv:2205.07651, Sect. X, item 1].

### Season length
<!-- key: season-length -->

Metrics are fairly insensitive to season length as long as it stays near
the baseline; shorter seasons degrade SNe and strong lensing; some
high-airmass visits lengthen seasons cheaply [src: arXiv:2104.05676,
Sect. VI.6, Fig. 16].

### Deep universal, deep rolling or intensive deep rolling
<!-- key: deep-universal-deep-rolling-or-intensive-deep -->

- **Deep Universal (DU):** all DDFs every season at the same depth. Cannot
  reach z_complete ≥ 0.6–0.65 within the budget because z- and y-band
  visits are too few [src: arXiv:2205.07651, Sect. VII.3].
- **Deep Rolling (DR):** ultra-deep and deep classes, each field observed
  for two seasons [src: Sect. VIII].
- **Intensive Deep Rolling (IDR):** two ultra-deep equatorial fields
  (COSMOS, XMM-LSS) to z_complete ~ 0.8 plus one deep field to ~0.6,
  observed every night with about 130 visits per night, achievable in a few
  years [src: arXiv:2205.07651, Sect. X, item 2].
- **Result on equal budget.** At 5%, σ_w ≈ 1.3–1.4% for IDR against
  σ_w ≥ 2% for DU; DU collects about 1.8 times more well-measured SNe but
  IDR has 45% of its SNe at z ≥ 0.8 against 22% for DU, and the N(z) shape,
  not the count, decides σ_w [src: arXiv:2205.07651, Sects. VII.3, VIII,
  Fig. 11 caption]
  (**forecast**). Going from 5% to 8% budget lowers σ_w by 20–25%; σ_w ≈
  1.1% needs 8% (DR) or 15% (DU) [src: Sect. VII.3]. The equatorial choice
  for the ultra-deep fields follows from host spectroscopy: PFS is "the only
  survey able to provide a significant number of spectra" at
  0.7 < z < 1.1 [src: Sect. X, item 3].
- **Cohesive strategy with other probes.** When photo-z training and weak
  lensing requirements are added, the best designs are deep rolling with
  deep fields at ~3-night cadence and 30–40 visits per night, and
  ultra-deep fields at ≲ 2 nights and 80–100 visits per night for three to
  four seasons; all requirements together need about 8.5% of the survey,
  against the 7% SCOC maximum [src: arXiv:2405.10781, Sect. 6].

### Rolling the wide survey
<!-- key: rolling-the-wide-survey -->

The rolling cadence raises the footprint weight of the active region by
90%; it only mildly improves overall classification, but in the active
region about 50% of SNe Ia pass the light-curve requirements against about
20% in the background region, up to a factor 2.7 more usable SNe Ia
[src: arXiv:2210.15690, Sect. V]. A three-visits-per-night variant
("presto-color") gives shorter, sparser light curves: early classification
and full-light-curve classification pull in opposite directions
[src: same]. The static-science cost of rolling is in
`deep/footprint-tiling-depth.md`.

### Multi-programme scheduling
<!-- key: multi-programme-scheduling -->

ZTF runs several programmes with strict independence of their observations
and time balance, from a fixed field grid [src: arXiv:1905.02209, Sect. II].
Its public Northern Sky Survey (δ ≥ −31°, |b| > 7°) observes each field
every third night once in g and once in r, at least 30 min apart to
separate transients from moving objects, with 85% of public time (34% of
telescope time); the Galactic plane gets two visits per night with 15% of
public time [src: Sect. VI.1]. The PTF greedy scheduler with ad-hoc weights
"proved unpredictable and prone to long slews", which motivated the
integer-programming approach once readout fell from 40 s to 8 s
[src: Sect. II].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Well-measured SN Ia | σ_c ≲ 0.04 | DESC | arXiv:2205.07651 | Sect. II.1 |
| Equivalent SNR, deep | SNR_i ≥ 59, SNR_z ≥ 39, SNR_y ≥ 20 | DESC DDF | arXiv:2205.07651 | Fig. 2 caption |
| Equivalent SNR, wide proxy | g > 30, r > 40, i > 30, z > 20 | DESC WFD | arXiv:2104.05676 | Sect. V.1.2 |
| Sampling cuts | ≥ 3 pre-peak, ≥ 8 post-peak, phase window −20 to +60 d, 380–700 nm rest frame | DESC | arXiv:2210.15690 | App. D |
| Metric pixels | N_side = 64 (0.8 deg²); E(B−V) > 0.25 masked | DESC | arXiv:2104.05676 | Sect. V.1.1 |
| OpSim runs evaluated | 173 (v1.5–v1.7.1) | Rubin | arXiv:2108.01683 | Sect. IV.1 |
| SRD visits | ≥ 750, design 825 summed over bands | LSST SRD | arXiv:2104.05676 | Sect. II.2 |
| Time left for DDFs and minisurveys | 10–20% | Rubin | arXiv:2108.01683 | Sect. V.1 |
| SCOC DDF budget | 5–7%, five fields, ten years | SCOC phase 2 | arXiv:2405.10781 | Sect. 2.1 |
| Visits per night for z_complete 0.80 / 0.75 / 0.70 | 149 / 108 / 81 at 1-day cadence | DESC DDF | arXiv:2405.10781 | Table 3 |
| Budget needed for all DESC DDF requirements | ~8.5% | DESC | arXiv:2405.10781 | Sect. 6 |
| σ_w at 5% budget | 1.3–1.4% (IDR), ≥ 2% (DU) (**forecast**) | DESC | arXiv:2205.07651 | Sect. VII.3 |
| Guaranteed FoM of IDR then DU with 8% | ≥ 150 (**forecast**) | DESC | arXiv:2205.07651 | Sect. X |
| Same-filter pairs | transient metrics degraded "dramatically" | DESC | arXiv:2104.05676 | Fig. 12 |
| 1 × 30 s against 2 × 15 s | ~7% efficiency; metrics up to +20% | DESC | arXiv:2104.05676 | Sect. VII.1 |
| Weather effect on transient metrics | up to 150% | DESC | arXiv:2104.05676 | Fig. 17 caption |
| Usable SNe Ia, rolling active vs background | ~50% vs ~20% | DESC | arXiv:2210.15690 | Sect. V |
| HLTDS core | 158 days; wide imaging tier 10.68 deg² (North) and 7.59 deg² (South), deep imaging tier 1.97 and 4.5 deg²; "about 18 deg2" wide and "about 6.5 deg2" deep in Sect. II | Roman | arXiv:2505.10574 | Sect. III.2; Sect. II |
| HLTDS good SNe Ia | ~7500 wide, ~6800 deep (**forecast**) | Roman | arXiv:2505.10574 | Sect. III.2 |
| TiDES | ≤ 50,000 host redshifts to z ~ 1 in 5 yr (**forecast**) | 4MOST | arXiv:1903.02476 | abstract |
| ZTF public cadence | 3 nights, g + r, ≥ 30 min apart | ZTF | arXiv:1905.02209 | Sect. VI.1 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Median gap hides the tail.** The median inter-night gap gives "an
  incomplete picture as the tails of the distribution ... can be quite
  broad" [src: arXiv:2104.05676, Sect. VI.6]. Test: the per-band gap
  distribution and the fraction of gaps over 10 days, not the median.
- **Simulated weather too kind.** Optimistic weather inflates transient
  metrics by up to 150% [src: arXiv:2104.05676, Sect. VI.7]. Test: rerun with the realistic
  cloud threshold.
- **Count instead of N(z).** A strategy with more SNe can give a worse σ_w
  if its redshift completeness is low [src: arXiv:2205.07651, Sect. VIII].
  Test: compare σ_w or the FoM, not N_SN.
- **No host redshifts.** A deep-field forecast that assumes every SN has a
  spectroscopic host overstates the result; only half the sample has one
  under the PFS plan [src: Sect. X]. Test: tie the forecast to a named
  follow-up programme and its fibre hours.
- **Classification ignored.** The 2022 DESC metric has no classification
  term [src: arXiv:2104.05676, Sect. V.1.1]; classification depends on
  light-curve length, gaps and points near peak [src: arXiv:2210.15690,
  Sect. V]. Test: a classifier run on the simulated cadence.
- **DDF dithers.** Large translational dithers lower the depth of the
  deep fields; DESC asks for dithers "as small as possible" there
  [src: arXiv:2104.05676, Sect. VII.1; arXiv:2205.07651, Sect. X].
- **Simplified simulations.** The DDF designs were made with "a relatively
  basic simulation" of sky brightness, clouds and dithering and need
  validation with the scheduler [src: arXiv:2405.10781, Sect. 6].
- **Design is not delivery.** The SCOC re-evaluates the strategy during
  operations [src: arXiv:2108.01683, Sect. V.1]; quote the cadence of the
  release analysed, not of a white paper.

## Reading list
<!-- key: reading-list -->

- Review: Bianco et al. 2022, arXiv:2108.01683 — OpSim, MAF, the
  white-paper calls and the SCOC process.
- Method: Lochner et al. 2022, arXiv:2104.05676 — DESC metrics for every
  probe; visit pairs, exposure time, gaps, seasons, weather.
- Method: Gris et al. 2022, arXiv:2205.07651 — SN Ia requirements, budget
  equations and deep-rolling designs with host spectroscopy.
- Application: Gris et al. 2024, arXiv:2405.10781 — DDF strategy meeting
  photo-z, weak-lensing and SN requirements together.
- Critique: Alves et al. 2022, arXiv:2210.15690 — cadence against
  photometric classification; the updated light-curve cuts.
- Application: Roman Observations Time Allocation Committee 2025,
  arXiv:2505.10574 — HLTDS tiers, components and the reasons given.
- Method: Bellm et al. 2019, arXiv:1905.02209 — volumetric metric and
  integer-programming scheduler of ZTF.
- Application: Swann et al. 2019, arXiv:1903.02476 — TiDES live-transient
  and host-redshift follow-up for LSST.
- Critique: Leistedt et al. 2025, arXiv:2512.16478 — rolling cadence
  against uniform static depth.

## Not verified
<!-- key: not-verified -->

- The adopted Rubin baseline as of the survey start (version, rolling
  parameters, whether visits are 1 × 30 s or 2 × 15 s), and the SCOC
  phase-3 recommendations: not found on arXiv in the searches made.
- The Roman HLTDS Definition Committee report (Appendix C.2 of
  arXiv:2505.10574 is not rendered); the reasons for the field choice
  beyond the continuous-viewing-zone and roll-angle constraints read in
  Sect. III.2.
- Whether the "phase ≤ 10" cut of arXiv:2210.15690, App. D, is meant
  as ≤ −10 (the rendering prints ≤ 10).
- DES-SN and ZTF SN Ia field cadences as delivered; ATLAS and YSE cadence
  design papers beyond their abstracts (L2).
- The current TiDES strategy and Rubin–4MOST coordination after 4MOST
  first light.
