# CMB survey design: detectors, noise, apertures, sky and bands — cosmo-surveys-facilities dossier

Scope: how a CMB survey is designed from detector sensitivity to map depth,
how its large-scale noise is modelled, how detectors are split across
frequency bands and between large and small apertures, how sky area,
site, scan and modulation are chosen, and what each choice costs, as read
in the Simons Observatory forecast paper, the CMB-S4 reference design, the
CMB-S4 parameter-space study, the LiteBIRD 2026 overview and the
Snowmass report.
Snapshot: 2026-10-18.
From: Snowmass CF6 (arXiv:2209.08654), Sect. 4; Simons Observatory science
goals and forecasts (arXiv:1808.07445).

Already in L2, not repeated here: the Knox band-power error, current map
depths and the LAT/SAT split in
`physics-and-methods.md#cmb-sensitivity-map-depth-resolution-and-sky`;
beams, the Planck calibration budget, scan and atmosphere, LiteBIRD's
null-map requirement in `systematics.md#cmb-experiments`; per-experiment
bands, depths and status in `surveys-and-data.md#cmb-experiments`. The SO
LAT sky-fraction trade and the SO observing-efficiency assumptions are in
`deep/survey-forecasts.md` ("Area or overlap for a CMB survey").
Likelihoods, beams in analysis and foreground cleaning are in `cosmo-cmb`;
B-mode foreground separation and delensing in `cosmo-inflation-primordial`.

Status note. CMB-S4 lost agency support on 9 July 2025
(`open-questions.md#cancelled-descoped-or-redefined-projects`). Its 2019
reference design is used here only as the most complete written
flow-down from science to detectors; its numbers are **design** values of a
project that will not be built.

Notation. NET: noise-equivalent temperature of one detector, in μK√s;
N_det: number of detectors; Y: combined yield and observing efficiency;
ΔT: survey duration; s: white map depth in μK-arcmin; N_ℓ: noise power
spectrum; ℓ_knee, α_knee: knee multipole and slope of the 1/f term;
f_sky: sky fraction; "detector-years": N_det × years of observation,
expressed in 150 GHz-equivalent detectors in CMB-S4.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Turn detectors and time into a map depth
<!-- key: step-1-turn-detectors-and-time-into-a-map-depth -->

The white-noise depth of a survey follows from the per-detector NET:

    s [μK-arcmin] = NET [μK√s] × sqrt(f_sky [arcmin²]) / sqrt(N_det × Y × ΔT [s])

(Wu et al. 2014, arXiv:1402.4108, Sect. II.1, Eq. 1), where f_sky in
arcmin² means the observed area. The authors took NET = 350 μK√s per
detector "achieved by current generation experiments" and Y = 25%
combining focal-plane yield and operating efficiency over five years
[src: Sect. II.1]. Worked example [der: Eq. 1 with these inputs]:
f_sky = 0.4 is 5.94 × 10⁷ arcmin²; 10⁴, 10⁵ and 10⁶ detectors then give
s ≈ 4.3, 1.36 and 0.43 μK-arcmin. Depth scales as 1/sqrt(N_det) and as
sqrt(area): doubling the area at fixed effort costs a factor sqrt(2) in
depth.

Two production practices replace the ideal NET:

- **SO 2018.** White levels come from array NETs that include imperfect
  yield, for a five-year survey with 20% of the time used for science
  (the realised Polarbear and ACT performance after data cuts), with the
  noise of the LAT raised to mimic discarding the 15% of map edges
  [src: arXiv:1808.07445, Sect. II.2]. Polarisation noise is √2 above the
  temperature noise because Q and U are both measured [src: Table 1 note].
- **CMB-S4 2019, "achieved performance".** Noise is scaled from BICEP/Keck
  end-to-end band-power covariances and noise spectra of several on-sky
  receiver-years, by detector count and time, with beam and NET rescaling
  between frequencies; this "automatically builds in" yield, non-uniform
  detectors, readout noise, observing inefficiency, filtering, beam
  smoothing and non-uniform coverage [src: arXiv:1907.04473, Sect. 7.A.1].
  Ideal NETs (computed at a 100 mK bath from 10-year median atmospheric
  profiles) are used only for the ratios between channels, "not to
  calculate ab-initio sensitivities" [src: same].

Survey weight is the quantity that adds linearly: CMB-S4 defines it as
2A/N² for a Q/U map of noise N over effective area A, "linear in detector
count and run time" [src: arXiv:1907.04473, Table 2-4 note]. Check
[der]: the 95 GHz ultra-deep entry (weight 14.1 × 10⁶ μK⁻², 0.78
μK-arcmin) implies A ≈ 1190 deg², 2.9% of the sky, as designed; the
deep-wide 95 GHz temperature entry (26.3 × 10⁶ μK⁻², 2.0 μK-arcmin) gives
A ≈ 29,200 deg² if the temperature weight is A/N², matching the quoted
f_sky^noise of 71% (29,000 deg²) [src: Sect. 7.3].

### Step 2. Add the large-scale noise
<!-- key: step-2-add-the-large-scale-noise -->

Ground surveys are not white on large scales. SO models every telescope
and band as

    N_ℓ = N_red (ℓ/ℓ_knee)^α_knee + N_white

[src: arXiv:1808.07445, Sect. II.2, Eq. 1], with parameters taken from
earlier experiments:

- **SAT polarisation.** N_red = N_white; ℓ_knee ≈ 50 with α_knee from
  −3.0 to −2.4 at 93 GHz reproduces the B-mode errors of QUIET, BICEP2/Keck
  and ABS; the knee "accounts for both the 1/f noise and the loss of modes
  due to filtering" and agrees with Polarbear using a rotating half-wave
  plate; ℓ_knee = 50 is the pessimistic and 25 the optimistic case,
  scaled to other bands through precipitable-water-vapour fluctuations,
  assuming a scan speed twice that of ABS and QUIET [src: same, Table 2].
- **LAT polarisation.** N_red = N_white, ℓ_knee = 700, α_knee = −1.4, from
  ACTPol at 150 GHz and Polarbear without a rotating half-wave plate
  [src: same].
- **LAT temperature.** ℓ_knee = 1000, α_knee = −3.5, N_red = 1800 μK²s at
  90 GHz and 12,000 μK²s at 145 GHz measured on ACTPol; extrapolated to
  other bands with an atmospheric model; divided by the number of optics
  tubes per band (each tube taken as an independent atmospheric
  realisation below the tube separation, ℓ ≈ 50) and by a further factor
  2 for the larger field per tube; the two bands of one tube are given a
  correlation coefficient of 0.9 because "the same water vapor provides
  the 1/f noise at all frequencies" [src: same].
- **SAT temperature** is not modelled: the SATs are not used for
  temperature science, already measured by WMAP and Planck [src: same].

The scan speed enters because the atmosphere must be frozen: turbulence
at about 1 km drifting at 10 m/s moves at 0.6°/s on the sky, so the CMB-S4
LAT was specified at 3° (1.5°) per second in azimuth (elevation), about
1°/s on the sky, with 2 s turnarounds on scans of a few tens of seconds
[src: arXiv:1907.04473, Sect. 15.1, Table 4-11].

### Step 3. Split the survey by science driver
<!-- key: step-3-split-the-survey-by-science-driver -->

CMB-S4's flow-down shows why the survey splits in two [src:
arXiv:1907.04473, Sect. 7.1]:

- **Light relics (N_eff)** constrain mostly through TE, whose error is
  sample-variance dominated, so the driver is area: a deep and wide field
  of f_sky ≈ 0.7.
- **Primordial gravitational waves (r)** depend on BB, whose sample
  variance is small and reducible by delensing, while foregrounds are
  bright relative to the signal, so the driver is depth on the cleanest
  small patch: an ultra-deep field of f_sky ≈ 0.03.

The same split appears in SO's damping-tail study: at noise above
4 μK-arcmin, N_eff depends strongly on f_sky; σ(N_eff) degrades by 40%
from f_sky = 0.4 to 0.1; resolution finer than 2–3′ does not help much at
fixed other specifications; 5 μK-arcmin over 40% of the sky with < 3′ at
145 GHz reaches σ(N_eff) = 0.06 (**forecast**) [src: arXiv:1808.07445,
Sect. IV.1.1].

### Step 4. Choose the patch size for r
<!-- key: step-4-choose-the-patch-size-for-r -->

The semi-analytic optimum for r = 0 is formally below 1% of the sky; CMB-S4
chose about 3% because cut-sky E/B separation "heavily disfavors" patches
below about 1%, because a 1% field would need more than 80% removal of
the lensing B-mode rms, because foreground amplitude and complexity grow
with area, and because several ~1% patches give reproducibility
[src: arXiv:1907.04473, Sects. 7.2, 7.A.1]. A wider "Pole Wide" survey of
about 7% and SATs in Chile were kept as options if r ≳ 0.01 [src:
Sect. 7.2].

For SO, the SAT field of view and scan strategy give a broad, graded
coverage of effective area about 4000 deg²; on 1000 simulations each,
this window gave errors equal to or smaller than a compact circular mask
of the same hits for 30 ≲ ℓ ≲ 300, close to mode counting
σ(C_ℓ) = (C_ℓ + N_ℓ)/sqrt((ℓ + 1/2) f_sky^eff Δℓ), with
f_sky^eff = ⟨N_hits⟩²/⟨N_hits²⟩ = 0.19 for noise-dominated maps (0.1 for
signal-dominated maps) [src: arXiv:1808.07445, Sect. III.4.1]. The
conclusion: the coverage set by scan and field of view is sub-dominant for
SO's r constraint, absent foreground systematics [src: same].

### Step 5. Allocate detectors to bands and to delensing
<!-- key: step-5-allocate-detectors-to-bands-and-to -->

- **CMB-S4.** For f_sky = 0.03, σ(r) = 5 × 10⁻⁴ needs 1.8 × 10⁶
  150 GHz-equivalent detector-years (1.2 × 10⁶ with optimistic
  foregrounds), about 30% of it for delensing, leaving a 30% rms lensing
  residual (about 10% in power) (**design**) [src: arXiv:1907.04473,
  Sects. 7.2, 7.A.1]. The eight SAT channels span the four atmospheric
  windows; each window was split as far as possible while keeping each
  per-detector NET within 10–15% of a full-window detector [src:
  Sect. 7.A.1]. Mapping detectors into real dichroic optics tubes moved the
  allocation away from the optimum and raised the degree-scale effort to
  1.5 × 10⁶ detector-years for a combined weight of 38 × 10⁶ μK⁻² [src:
  Sect. 7.2].
- **Why a 20 GHz channel on the LAT.** An early forecast iteration showed
  synchrotron residual biases; a 20 GHz SAT channel lacked sensitivity at
  ℓ ≳ 100 for lack of resolution, so it moved to the delensing LAT [src:
  Sects. 7.2, 7.A.1].
- **Why the foreground bands at all.** Unmodelled dust biases r at 150 GHz
  by two orders of magnitude above the CMB-S4 target; each foreground needs
  at least one channel, and several if it varies across the field [src:
  Sect. 7.2].
- **SO low-frequency time.** σ(r) is broadly optimal with about one year of
  the 27/39 GHz tube in an MF SAT, at the expense of 93/145 GHz [src:
  arXiv:1808.07445, Sect. III.4.3]. The SAT resolution (≤ 90′) does not
  limit r because the constraint sits at ℓ ≤ 100–150 [src: same, Fig. 14
  caption].
- **Deep-wide bands** are driven by clusters, not by N_eff, which "does not
  require a heavy amount of foreground cleaning" [src: arXiv:1907.04473,
  Sect. 7.3].

### Step 6. Set the aperture and the telescope type
<!-- key: step-6-set-the-aperture-and-the-telescope-type -->

- **Large aperture** for resolution: the CMB-S4 LAT needed < 1.5′ at
  150 GHz, a few μK-arcmin at 95 and 150 GHz over about 70% of the sky, and
  bands to at least 270 GHz; hence a 5.5 m effective aperture (physical
  about 6 m to reduce spillover), surface error < 37 μm rms for 80% Strehl
  at 1 mm, pointing knowledge < 5″ rms so that pointing-induced E→B mixing
  does not limit r, emissivity < 0.01 [src: arXiv:1907.04473, Sect. 15.1,
  Table 4-11]. Stage-3 LATs hold about 10⁴ detectors; a wide-field design
  holds about 10⁵, so three LATs suffice [src: same].
- **Small aperture** for large scales: aperture-filling calibrators and
  cryogenic modulators, stable fully cryogenic optics, compact mounts with
  boresight rotation, and suppressed sidelobes; "only small-aperture
  telescopes have demonstrated sufficient performance in degree-scale
  B-mode measurements" [src: Sect. 17.1]. SO reached the same conclusion:
  the LAT gives resolution, the SATs a larger field and better control of
  the atmosphere on large scales [src: arXiv:1808.07445, Sect. II.1].
- **Sidelobes** dominate systematic errors through ground, Galaxy, Sun and
  Moon pickup, which calls for an offset optical design, low edge
  illumination, small panel gaps, large clearances and shields [src:
  arXiv:1907.04473, Sect. 15.1].
- **Residual systematics budget.** Simulations required noise-like additive
  residuals ≲ 10% of the noise for a bias ≲ 10⁻⁴ on r, a level Stage-3
  experiments achieve, so "Stage-3 technology is sufficient; we just need
  more of it" [src: Sect. 8].

### Step 7. Pick the site and the scan
<!-- key: step-7-pick-the-site-and-the-scan -->

- **Sites.** The Atacama site at 23° S sees more than 80% of the sky,
  allowing the 70% wide survey; the South Pole suits deep integration on a
  small patch [src: arXiv:1907.04473, Sect. 14.1]. Median precipitable
  water vapour used in forecasts: 0.5 mm at the Pole, 1.0 mm in the
  Atacama [src: Sect. 7.A.1, Fig. 7-67 caption].
- **Minimum elevation and Galactic plane.** Lower minimum elevations open
  more sky at an air-mass noise penalty; scanning around the Galaxy
  "anti-apodised" the maps through turnaround time, so the design scans
  through it and chooses the Galactic cut after the fact; a 30° minimum
  elevation and a 13–14% Galactic cut leave about 62% for N_eff [src:
  Sect. 7.3].
- **Modulation.** A continuously rotating half-wave plate at the sky side
  of all lenses modulates the large-scale atmosphere and removes
  instrumental polarisation from the optics behind it, reducing T→P leakage
  and polarised sidelobes; CMB-S4 planned one only for SATs in Chile at
  85 GHz and above, because the Chilean atmosphere is less stable [src:
  Sect. 17.4]; SO puts one in every SAT [src: arXiv:1808.07445,
  Sect. II.1].
- **Space.** LiteBIRD combines spin, precession and anti-Sun control at
  L2; study values are a 37.5° precession angle, 57.5° spin angle, spin
  0.05 rpm with a polarisation modulator and 0.3 rpm without, precession
  period 1–10 h, optimised for thermal and cryogenic feasibility "while
  maintaining sufficient cross-linking", which controls large-scale
  polarisation systematics [src: arXiv:2607.25285, Sect. 3.5]. Its band
  NETs are derived from the feasibility of foreground removal, and the
  12-band choice is to be consolidated in Phase A [src: Sect. 2.3].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Wide-shallow against narrow-deep
<!-- key: wide-shallow-against-narrow-deep -->

Wide wins for any sample-variance-limited spectrum (TE for N_eff, lensing,
clusters); narrow-deep wins for BB at r ≈ 0, until cut-sky and delensing
limits bite below about 1% (Steps 3–4). Wu et al. found σ(r)
foreground-limited, with the optimal f_sky moving higher when
foregrounds are high, while σ(N_eff), the DETF FoM and σ(p_ann) are not
sample-variance limited and gain from detectors (**forecast**) [src:
arXiv:1402.4108, Sect. VII].

### More detectors against a smaller beam
<!-- key: more-detectors-against-a-smaller-beam -->

At 25–75% f_sky, 10⁴ → 10⁵ detectors improves σ(N_eff) by about 30% (and
again for 10⁵ → 10⁶), while each arcminute of beam gains about 10%; the
DETF FoM (CMB + BAO + H₀) gains more than a factor 2 per decade of
detectors (**forecast**) [src: arXiv:1402.4108, Sect. VII]. The CMB-S4
light-relics design "hits" its target, so an increase in noise or beam can
only be traded against a decrease in the other [src: arXiv:1907.04473,
Sect. 7.3].

### Half-wave plate or not
<!-- key: half-wave-plate-or-not -->

With a rotating plate, SO assumes SAT ℓ_knee = 25–50; the LAT without one
is modelled with ℓ_knee = 700 in polarisation [src: arXiv:1808.07445,
Sect. II.2]. The cost is a cryogenic mechanism near the aperture (sapphire
stack at 45 K, superconducting magnetic bearing in the CMB-S4 design) [src:
arXiv:1907.04473, Sect. 17.4]; in space, dropping it forces a faster spin
(0.3 rpm against 0.05) [src: arXiv:2607.25285, Sect. 3.5].

### Pole or Chile
<!-- key: pole-or-chile -->

The Pole gives continuous access to one clean patch and a more stable
atmosphere (no plate planned there in CMB-S4); Chile gives the wide sky
but needs modulation for degree scales [src: arXiv:1907.04473, Sects.
14.1, 17.4]. The SPT-3G noise knees at ℓ = 128 and 182 limit its own r
constraint (`cosmo-inflation-primordial`, systematics file) [sec:
cosmo-inflation-primordial].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Ideal per-detector NET (2014) | 350 μK√s; Y = 25%; 5 yr | CMB-S4 study | arXiv:1402.4108 | Sect. II.1 |
| Science fraction of time | 20% over 5 yr; 15% LAT edges cut | SO 2018 | arXiv:1808.07445 | Sect. II.2 |
| SAT ℓ_knee (pol.) | 50 pessimistic, 25 optimistic at 93/145 GHz; 30 at 27/39; 70, 100 at 225, 280 (pessimistic) | SO 2018 | arXiv:1808.07445 | Table 2 |
| LAT ℓ_knee | 700 (pol., α = −1.4); 1000 (temp., α = −3.5) | SO 2018 | arXiv:1808.07445 | Sect. II.2 |
| LAT N_red (temp.) | 230 (93 GHz), 1500 (145 GHz) μK²s after tube scaling | SO 2018 | arXiv:1808.07445 | Table 2 |
| SAT effective area | ~4000 deg²; f_sky^eff 0.19 (noise), 0.1 (signal) | SO 2018 | arXiv:1808.07445 | Sect. III.4.1 |
| N_eff driver | f_sky ≥ 0.4, 5 μK-arcmin, < 3′ for σ = 0.06 (**forecast**) | SO 2018 | arXiv:1808.07445 | Sect. IV.1.1 |
| Ultra-deep effort | 1.8 × 10⁶ det-yr (optimal), 1.5 × 10⁶ degree-scale in design; 38 × 10⁶ μK⁻² | CMB-S4 (**design**) | arXiv:1907.04473 | Sects. 7.2, 7.A.1 |
| Ultra-deep Q/U depth | 0.78 (95 GHz), 1.2 (145 GHz) μK-arcmin | CMB-S4 (**design**) | arXiv:1907.04473 | Table 2-4 |
| Delensing survey depth | 0.68 (95), 0.96 (145) μK-arcmin; 2.3′, 1.5′ | CMB-S4 (**design**) | arXiv:1907.04473 | Table 2-5 |
| Deep-wide depth | 2.0 μK-arcmin T at 95/145 GHz; 71% f_sky^noise; 62% after Galactic cut | CMB-S4 (**design**) | arXiv:1907.04473 | Sect. 7.3, Table 2-6 |
| Additive residual budget | ≲ 10% of noise for ≲ 10⁻⁴ bias on r | CMB-S4 | arXiv:1907.04473 | Sect. 8 |
| LAT design | 5.5 m effective; < 37 μm rms; < 5″ pointing; 3°/s az | CMB-S4 (**design**) | arXiv:1907.04473 | Table 4-11 |
| Detector count | ~500k total, ~250k for the wide survey | CMB-S4 (**design**) | arXiv:1907.04473 | Sects. 8, 15.1 |
| SO MF SAT delivered | ~9400 biased TES per SAT (80% yield); combined NET 2.4 (90 GHz), 3.2 (150 GHz) μK√s | SO commissioning | arXiv:2609.26938 | abstract |
| LiteBIRD scan | 37.5° precession, 57.5° spin, 0.05 or 0.3 rpm | LiteBIRD (**design**) | arXiv:2607.25285 | Sect. 3.5 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Ab-initio NETs.** Forecasts built from ideal NETs omit yield, cuts,
  filtering and coverage; CMB-S4 used them only for channel ratios for this
  reason [src: arXiv:1907.04473, Sect. 7.A.1]. Test: is the noise anchored
  to achieved on-sky performance, and what efficiency is assumed (SO: 20%
  [src: arXiv:1808.07445, Sect. II.2])?
- **Knee assumed, not measured.** A forecast is conditional on its ℓ_knee;
  SO used 25 and 50 for the SATs [src: Table 2]. Test: compare with the
  knee measured by the same telescope type at the same site.
- **Atmosphere scaled as white noise.** Atmospheric noise is spatially
  correlated and does not average down with detector number, and two bands
  of one tube share it [src: Sect. II.2]. Test: inter-band correlation in
  the noise model.
- **f_sky without weighting.** The effective sky fraction depends on the
  hit distribution and on whether maps are noise- or signal-dominated
  (0.19 against 0.1 for the same SO hit map) [src: Sect. III.4.1].
- **Optimal band allocation that cannot be built.** Real dichroic tubes
  force a departure that raised the CMB-S4 effort from the optimum [src:
  arXiv:1907.04473, Sect. 7.2].
- **Avoiding the Galaxy.** Scan turnarounds at the Galactic boundary pile
  up coverage at map edges [src: Sect. 7.3].
- **Design treated as plan.** CMB-S4 numbers describe a cancelled project;
  LiteBIRD's 12 bands and NETs are not yet consolidated
  [src: arXiv:2607.25285, Sect. 2.3].

## Reading list
<!-- key: reading-list -->

- Foundation: Knox 1995, arXiv:astro-ph/9504054 — mode counting and the
  value of resolution (read in L2; body not renderable here).
- Method: Wu et al. 2014, arXiv:1402.4108 — NET-to-depth relation and the
  detector, beam and sky-fraction grid.
- Method: Simons Observatory 2018, arXiv:1808.07445 — the ℓ_knee noise
  model, scan-strategy test, damping-tail requirements.
- Application: CMB-S4 Collaboration 2019, arXiv:1907.04473 — full
  flow-down: two-tier survey, detector-years, band split, LAT and SAT
  drivers, sites, half-wave plates.
- Application: LiteBIRD Collaboration 2026, arXiv:2607.25285 — space scan
  parameters and band requirements after the reformation.
- Critique: Harrington et al. 2026, arXiv:2609.26938 — delivered SO SAT
  NETs against the baseline targets.
- Review: Flaugher et al. 2022, arXiv:2209.08654 — the Stage-4 and CMB-HD
  concepts in the Snowmass report.

## Not verified
<!-- key: not-verified -->

- The SO companion instrument paper with detector NETs (cited as in
  preparation in arXiv:1808.07445, Sect. II.2).
- The CMB-S4 optimisation reference ([561] in arXiv:1907.04473) and its
  Fig. 7-70 per-channel optimum.
- The SO SAT expansion forecast (arXiv:2512.15833) and enhanced LAT paper
  (arXiv:2503.00636) bodies: their detector counts are in L2 [sec: CMB].
- The temperature survey-weight definition (A/N²) is inferred from the
  CMB-S4 table, not stated in the sections read.
- SPT-3G and BICEP Array design papers; Planck and WMAP scan-strategy
  papers.
