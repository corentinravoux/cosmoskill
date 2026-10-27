# CMB survey design: detectors, noise, apertures, sky and bands — cosmo-surveys-facilities dossier

Scope: how a CMB survey is designed from detector sensitivity to map depth,
how its large-scale noise is modelled, how detectors are split across
frequency bands and between large and small apertures, how sky area,
site, scan and modulation are chosen, and what each choice costs, as read
in the design and forecast papers of the Simons Observatory (2018, 2025),
CMB-S4 (2019 reference design, 2020 r forecast), the South Pole programme
(SPT-3G+, BICEP/Keck and BICEP Array), ACT DR6, CMB-HD, LiteBIRD (2022,
2026) and the Snowmass report.
Snapshot: 2026-10-22.
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

Status, as the sources give it:

| Project | Status | Source |
|---|---|---|
| CMB-S4 | DOE and NSF "can no longer support" it (9 July 2025); orderly shutdown. Its 2019 design and 2020 r forecast are used here only as the most complete written flow-down; their numbers are **design** values of a project that will not be built | cmb-s4.org, read in `cosmo-cmb` [sec: cosmo-cmb] |
| South Pole Observatory | coordinated observing and analysis programme of SPT and BICEP: SPT-3G+ (installation early 2029, six-year survey) delenses BICEP Array; goal σ(r) ~ 0.001 with data through 2034 | arXiv:2608.20236, abstract, Sect. 2.2 [src] |
| BICEP Array | 30/40 and 150 GHz receivers observing for several years; 220/270 GHz at 7 of 12 modules, to be filled before the 2027 season | arXiv:2608.25015, abstract [src] |
| Simons Observatory | LAT upgrade (30,000 new detectors, doubled mapping speed) complete by 2028, survey to 2034; SATs from three to six by 2027, survey to 2035 | arXiv:2503.00636, abstract, App. A; arXiv:2512.15833, abstract [src] |
| LiteBIRD | reformed 2024–2026 | `open-questions.md#cancelled-descoped-or-redefined-projects` |
| CMB-HD | "a proposed millimeter-wave survey" (Snowmass 2021 white paper) | arXiv:2203.05728, abstract [src] |

Notation. NET: noise-equivalent temperature of one detector, in μK√s;
N_det: number of detectors; Y: combined yield and observing efficiency;
ΔT: survey duration; s: white map depth in μK-arcmin; N_ℓ: noise power
spectrum; ℓ_knee, α_knee: knee multipole and slope of the 1/f term;
f_sky: sky fraction; "detector-years": N_det × years of observation,
expressed in 150 GHz-equivalent detectors in CMB-S4. <!-- num: not a value -->

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
[src: Sect. II.1]. In Eq. 1 depth scales as 1/sqrt(N_det) and as
sqrt(area): doubling the area at fixed effort costs a factor sqrt(2) in
depth.

Production practices that replace the ideal NET:

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
- **SO 2025 (enhanced LAT and SATs).** Same detector NETs and 20%
  efficiency as 2018, now for 3 years with the nominal LAT tubes (1 LF,
  4 MF, 2 UHF) then 6 years with the full receiver (1 LF, 8 MF, 4 UHF),
  over f_sky = 0.61 instead of 0.47 [src: arXiv:2503.00636, App. A].
  "Baseline" NETs are the requirements, "goal" the expected performance;
  pre-deployment MF tubes are consistent with goal [src: same, Table 5].
  The SAT depths now include inhomogeneous noise and are quoted in
  polarisation, √2 above the 2018 temperature convention [src:
  arXiv:2512.15833, Table 1 note].
- **CMB-HD, scaling from SO.** Its depths need the SO goal noise divided
  by 8; with noise ∝ 1/sqrt(N_det t_obs), SO's 30,000 detectors over
  5 years become 1.3 million over 7.5 years (1.6 million with a
  280/350 GHz channel), at the same 20% efficiency, called likely
  pessimistic since ACT and Polarbear reached 17–30%, and 80% yield
  [src: arXiv:2203.05728, Sect. 9.3].
- **Achieved depths to anchor against.** BICEP/Keck through 2018: Q/U
  2.8, 2.8, 8.8 μK-arcmin at 95, 150, 220 GHz over ≈ 600 deg² (95 GHz)
  and ≈ 400 deg² [src: arXiv:2110.00483, abstract]. SPT on one telescope:
  SPT-SZ 2500 deg² at 36/16/62 μK-arcmin (95/150/220 GHz, temperature),
  SPTpol 500 deg² at 5.9/13.5, SPT-3G 1500 deg² expected 2.2/1.9/6.7 with
  data to 2028; SPT-3G+ aims at 0.7 μK-arcmin at 90 and 150 GHz on
  800 deg² with nearly ten times SPT-3G's mapping speed [src:
  arXiv:2608.20236, Sect. 1], 0.5 μK-arcmin combined [src: abstract].

Survey weight is the quantity that adds linearly: CMB-S4 defines it as
2A/N² for a Q/U map of noise N over effective area A, "linear in detector
count and run time" [src: arXiv:1907.04473, Table 2-4 note].

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
  assuming a scan speed twice that of ABS and QUIET [src: arXiv:1808.07445,
  Sect. II.2, Table 2].
- **LAT polarisation.** N_red = N_white, ℓ_knee = 700, α_knee = −1.4, from
  ACTPol at 150 GHz and Polarbear without a rotating half-wave plate
  [src: arXiv:1808.07445, Sect. II.2].
- **LAT temperature.** ℓ_knee = 1000, α_knee = −3.5, N_red = 1800 μK²s at
  90 GHz and 12,000 μK²s at 145 GHz measured on ACTPol (arXiv:1808.07445)
  [src: Sect. II.2]; extrapolated to
  other bands with an atmospheric model; divided by the number of optics
  tubes per band (each tube taken as an independent atmospheric
  realisation below the tube separation, ℓ ≈ 50) and by a further factor
  2 for the larger field per tube; the two bands of one tube are given a
  correlation coefficient of 0.9 because "the same water vapor provides
  the 1/f noise at all frequencies" [src: same].
- **SAT temperature** is not modelled: the SATs are not used for
  temperature science, already measured by WMAP and Planck [src: same].
- **What "ℓ_knee" meant in 2018.** SO 2025 states that the 2018 values
  "would have been better called a reference multipole, ℓ_ref", scaled by
  N_red, not the multipole where red and white noise are equal; the two
  relate by N_red/ℓ_ref^α = σ²/ℓ_knee^α [src: arXiv:2503.00636, App. A,
  footnote 12]. For point sources SO 2025 uses true knees from ACT data:
  α = −3.5, ℓ_knee = 500, 500, 2100, 3000, 3800, 3800 at 27–280 GHz
  [src: same]. The SAT forecasts of 2025 keep ℓ_knee = 50 (pessimistic)
  and 25 (optimistic) [src: arXiv:2512.15833, Sect. 3.1].
- **Measured knees (ACT, SPT, Planck).** ACT DR6 maps follow
  N_ℓ ≈ σ²[1 + (ℓ/ℓ_knee)^α], α ≈ −3, ℓ_knee ≈ 2100/3000/3800 at
  f090/f150/f220 in temperature and typically 300–640 in polarisation by
  array; by ℓ = 0.1 ℓ_knee the atmospheric power is ≈ 1000 times the white
  level [src: arXiv:2503.14451, Sect. V.1]. The same paper quotes SPT at
  ℓ_knee = 1200/1900/2100 (T) and 200 (E), slope closer to −4, at a site
  with typically a third of ACT's PWV, and Planck at ℓ_knee ~ 50, slope
  closer to −1 [src: same, footnote 23].

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
  of f_sky ≈ 0.7 (arXiv:1907.04473) [src: Sect. 7.1].
- **Primordial gravitational waves (r)** depend on BB, whose sample
  variance is small and reducible by delensing, while foregrounds are
  bright relative to the signal, so the driver is depth on the cleanest
  small patch: an ultra-deep field of f_sky ≈ 0.03 (arXiv:1907.04473)
  [src: Sect. 7.2].

The same split appears in SO's damping-tail study: at noise above
4 μK-arcmin, N_eff depends strongly on f_sky; σ(N_eff) degrades by 40%
from f_sky = 0.4 to 0.1; resolution finer than 2–3′ does not help much at
fixed other specifications; 5 μK-arcmin over 40% of the sky with < 3′ at
145 GHz reaches σ(N_eff) = 0.06 (**forecast**) [src: arXiv:1808.07445,
Sect. IV.1.1].

CMB-HD derives all its requirements from two targets, dark matter on
small scales and new light species, "since there are no science targets
that pull the requirements in opposing directions": the widest sky from
the ground (about 50%, preferred once kSZ foregrounds are included),
0.5 μK-arcmin in temperature (0.7 in polarisation) in a combined
90/150 GHz channel for a 5σ test of suppressed small-scale power, which
also gives σ(N_eff) = 0.014, σ(f_NL^local) = 0.26 and σ(r) = 0.005
(**forecast**) [src: arXiv:2203.05728, Sect. 9.1]. It does not re-image
the scales SO measures to sample variance (ℓ = 30–3000 in T, 30–2000 in
E), so its largest scales are ℓ ~ 1000 in temperature and ℓ ~ 100 in
polarisation [src: same]. Its parameter forecast, with ℓ = 30–20,000,
residual foregrounds, delensed peaks and DESI BAO, gives σ(n_s) = 0.0013
and σ(N_eff) = 0.014 (**forecast**) [src: arXiv:2309.03021, abstract].

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

Peers on the same question:

- **CMB-S4 2020, realistic hit maps.** The idealised circular patch "is
  not actually achievable"; from the Pole coverage can be concentrated on
  a compact region, from Chile Earth's rotation spreads it, and a large
  SAT field of view sets a minimum field and a strong edge taper [src:
  arXiv:2008.12619, Sect. VII.1]. Effective sky fractions (signal/noise,
  %, inverse-variance weights): Pole deep 1.9/2.9, Pole wide 4.3/6.5,
  Chile deep 2.4/3.4, Chile full 5.9/18; BICEP2/Keck 1.0/1.3 and BICEP3
  1.9/2.7 [src: Table 5]. The Pole strategy "is always favored in the
  limit of small r", because sensitivity can be concentrated more deeply,
  and the smaller survey makes the delensing requirement more stringent
  [src: Sect. VII.3].
- **SO 2025 SATs.** About 10% of the sky, f_sky = ⟨N_hits²⟩²/⟨N_hits⁴⟩
  ≈ 0.10 for signal and ⟨N_hits⟩²/⟨N_hits²⟩ ≈ 0.18 for noise; the
  updated scan strategy changes σ(r) by less than 10% [src:
  arXiv:2512.15833, Sect. 3.1].
- **SPT-3G+.** The 800 deg² field was chosen to overlap fully the
  BICEP/Keck patch, so that one site observes one patch continuously and
  the large-aperture lensing map delenses the small-aperture maps [src:
  arXiv:2608.20236, Sect. 2.2].

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
  arXiv:1907.04473, Sects. 7.2, 7.A.1].
- **Why the foreground bands at all.** Unmodelled dust biases r at 150 GHz
  by two orders of magnitude above the CMB-S4 target; each foreground needs
  at least one channel, and several if it varies across the field [src:
  arXiv:1907.04473, Sect. 7.2].
- **SO low-frequency time.** σ(r) is broadly optimal with about one year of
  the 27/39 GHz tube in an MF SAT, at the expense of 93/145 GHz [src:
  arXiv:1808.07445, Sect. III.4.3]. The SAT resolution (≤ 90′) does not
  limit r because the constraint sits at ℓ ≤ 100–150 [src: same, Fig. 14
  caption].
- **Deep-wide bands** are driven by clusters, not by N_eff, which "does not
  require a heavy amount of foreground cleaning" [src: arXiv:1907.04473,
  Sect. 7.3].
- **SO SAT expansion.** The LF receiver gets its own platform instead of
  replacing an MF receiver for one year; two further MF SATs (12,040
  detectors each) double the 93/145 GHz mapping speed, for 61,852 SAT
  detectors in all [src: arXiv:2512.15833, Sect. 2]. Delensing is
  bracketed by A_lens = 0.5 (external tracers) and 0.3 (internal, with an
  extended LAT campaign); nominal SO is expected to reach A_lens = 0.35
  [src: Sect. 3.1].
- **BICEP Array.** Four 550 mm refractors at 30/40, 95, 150 and
  220/270 GHz, more than 30,000 detectors [src: arXiv:1808.00568,
  abstract]; finishing the 220/270 GHz receiver is "a top priority"
  because the science goals need its dust cleaning [src: arXiv:2608.25015,
  abstract]. Delensing comes from SPT (Step 4).
- **LiteBIRD.** δr must be reached without delensing by external data
  [src: arXiv:2202.02773, Sect. 3.2]; its statistical requirement
  carries sub-requirements on dust, synchrotron, CO separation, the number
  of bands and the frequency range, fixed by simulation [src: Sect. 3.3].

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
  more of it" [src: arXiv:1907.04473, Sect. 8].
- **30 m for CMB-HD.** Lensing by structures at k ~ 10 h Mpc⁻¹ seen at
  z ~ 2 needs ℓ ~ 35,000, about 15″ at 150 GHz, hence a 30 m dish, which
  foreground cleaning (sources above 0.03 mJy, the CIB) also requires
  above 100 GHz; two off-axis crossed Dragone telescopes [src:
  arXiv:2203.05728, Sects. 9.1, 9.3, abstract].
- **Upgrading an existing large aperture.** SPT-3G+ on the 10 m SPT:
  6020 dichroic pixels (24,080 TES detectors) at 90/150 GHz, 100 mK
  dilution refrigerator, microwave SQUID multiplexing, a 4° field split
  into 14 optics tubes [src: arXiv:2608.20236, abstract]; SPT-3G had a
  1.88° field [src: Sect. 1].
- **Detector and readout choice in a small aperture.** The two new SO MF
  SATs use kinetic inductance detectors with RFSoC readout instead of TES
  and SMuRF, "much simpler to read out", and a two-lens instead of a
  three-lens design; forecasts assume equal KID and TES performance [src:
  arXiv:2512.15833, Sect. 2].

### Step 7. Pick the site and the scan
<!-- key: step-7-pick-the-site-and-the-scan -->

- **Sites.** The Atacama site at 23° S sees more than 80% of the sky,
  allowing the 70% wide survey; the South Pole suits deep integration on a
  small patch [src: arXiv:1907.04473, Sect. 14.1]. Median precipitable
  water vapour used in forecasts: 0.5 mm at the Pole, 1.0 mm in the
  Atacama [src: Sect. 7.A.1, Fig. 7-67 caption].
  CMB-HD chooses Cerro Toco because an instrument there sees the required
  50% of the sky while one at the Pole sees less than half of that, and a
  dry site minimises the detector count [src: arXiv:2203.05728,
  Sect. 9.3]. The SPT site has typically a third of ACT's PWV [src:
  arXiv:2503.14451, footnote 23].
- **Reuse of infrastructure.** The three added SO SATs sit on the former
  ACT and Polarbear/Simons Array sites, reusing the ACT ground screen [src:
  arXiv:2512.15833, Sect. 2].
- **Minimum elevation and Galactic plane.** Lower minimum elevations open
  more sky at an air-mass noise penalty; scanning around the Galaxy
  "anti-apodised" the maps through turnaround time, so the design scans
  through it and chooses the Galactic cut after the fact; a 30° minimum
  elevation and a 13–14% Galactic cut leave about 62% for N_eff [src:
  arXiv:1907.04473, Sect. 7.3].
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
For r, the CMB-S4 2020 forecast found the Pole favoured at small r, with
the crossover depending on assumptions, and inflated the foregrounds of the
shallower Chilean region by a factor 3 [src: arXiv:2008.12619,
Sect. VII.3]. For a half-sky survey, CMB-HD found the Pole short of sky
(Step 7). The two current r programmes split the same way: the SO SATs in
Chile with a half-wave plate on about 10% of the sky [src:
arXiv:2512.15833, Sect. 3.1], SPO on one ~800 deg² patch at the Pole [src:
arXiv:2608.20236, Sect. 2.2].

### Who forecasts what for r
<!-- key: who-forecasts-what-for-r -->

Forecasts quoted side by side, each under its own assumptions
(**forecast**): SO with six SATs to 2035, σ_r = 1.2 × 10⁻³ (ℓ_knee = 50,
moderately complex foregrounds, 70% delensing), 7 × 10⁻⁴ optimistic,
about 2.5 times better than the original three-SAT, five-year plan [src:
arXiv:2512.15833, abstract]; SPO σ(r) ~ 0.001 through 2034 [src:
arXiv:2608.20236, Sect. 2.2]; BICEP Array alone, σ(r) ~ 0.003 in the 2018
design, "depending on the level of delensing" [src: arXiv:1808.00568,
abstract], ~0.001 by 2034 in 2026 [src: arXiv:2608.25015, abstract];
LiteBIRD 2022 requirement δr < 10⁻³ total [src: arXiv:2202.02773,
Table 1]; CMB-HD σ(r) = 0.005 [src: arXiv:2203.05728, Sect. 9.1]. The
achieved reference is BICEP/Keck through 2018, σ(r) = 0.009 [src:
arXiv:2110.00483, abstract]. SPT-3G+ quotes SO's 10-year prediction as
0.0014 [src: arXiv:2608.20236, Sect. 2.2], where the SO SAT paper gives
1.2 × 10⁻³ (baseline) [src: arXiv:2512.15833, abstract]; cite the SO
paper for SO's number.

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
| SO LAT survey 2025 | 3 yr nominal + 6 yr full receiver; f_sky 0.61; 20% efficiency | SO 2025 | arXiv:2503.00636 | App. A |
| SO LAT NET per tube | baseline 10.8 (93), 13.4 (145) μK√s; goal 7.8, 8.4 | SO 2025 | arXiv:2503.00636 | Table 5 |
| SO SAT expansion | 6 SATs, 61,852 det; MF pol. depth 1.7/2.1 (baseline), 1.2/1.4 (goal) μK-arcmin; to 2035 | SO 2025 | arXiv:2512.15833 | Table 1 |
| SO SAT f_sky | 0.10 (signal), 0.18 (noise) | SO 2025 | arXiv:2512.15833 | Sect. 3.1 |
| Measured ℓ_knee, T | 2100/3000/3800 at f090/f150/f220; pol. 300–640; α ≈ −3 | ACT DR6 | arXiv:2503.14451 | Sect. V.1 |
| Measured ℓ_knee, as quoted | SPT 1200/1900/2100 (T), 200 (E), slope ~ −4; Planck ~50 | ACT DR6 | arXiv:2503.14451 | footnote 23 |
| Achieved Q/U depth | 2.8, 2.8, 8.8 μK-arcmin (95/150/220), ≈ 600/400 deg² | BICEP/Keck BK18 | arXiv:2110.00483 | abstract |
| SPT surveys (T depth) | SPT-3G 1500 deg² 2.2/1.9/6.7 expected; SPT-3G+ 800 deg², 0.7 at 90 and 150 GHz | SPT | arXiv:2608.20236 | Sect. 1 |
| SPT-3G+ receiver | 24,080 det, 4° field, 14 tubes, from 2029, 6 yr | SPT (**design**) | arXiv:2608.20236 | abstract |
| BICEP Array | 4 × 550 mm, 30/40–270 GHz, > 30,000 det | BICEP/Keck (**design**) | arXiv:1808.00568 | abstract |
| CMB-S4 r-survey f_sky | Pole deep 1.9/2.9%, Chile full 5.9/18% (signal/noise) | CMB-S4 2020 (**design**) | arXiv:2008.12619 | Table 5 |
| CMB-HD | 0.5 μK-arcmin T, 15″ at 150 GHz, 20,000 deg², 7.5 yr, 2 × 30 m, 1.6 × 10⁶ det | CMB-HD (proposal) | arXiv:2203.05728 | abstract, Sect. 9.3 |
| LiteBIRD 2022 sensitivity | 2.2 μK-arcmin total, 15 bands, 3 telescopes, 3 yr (pre-reformation) | LiteBIRD (**design**) | arXiv:2202.02773 | abstract |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Ab-initio NETs.** Forecasts built from ideal NETs omit yield, cuts,
  filtering and coverage; CMB-S4 used them only for channel ratios for this
  reason [src: arXiv:1907.04473, Sect. 7.A.1]. Test: is the noise anchored
  to achieved on-sky performance, and what efficiency is assumed (SO: 20%
  [src: arXiv:1808.07445, Sect. II.2])?
- **Knee assumed, not measured, or defined differently.** A forecast is
  conditional on its ℓ_knee; SO used 25 and 50 for the SATs [src:
  Table 2]. The SO 2018 LAT values are reference multipoles scaled by
  N_red, the ACT and SO 2025 point-source values true knees [src:
  arXiv:2503.00636, App. A, footnote 12]. Test: which definition, and
  compare with the knee measured by the same telescope type at the same
  site (Step 2).
- **Atmosphere scaled as white noise.** Atmospheric noise is spatially
  correlated and does not average down with detector number, and two bands
  of one tube share it [src: Sect. II.2]. Test: inter-band correlation in
  the noise model.
- **f_sky without weighting, or under another definition.** The
  effective sky fraction depends on the hit distribution and on whether
  maps are noise- or signal-dominated (0.19 against 0.1 for the same SO
  hit map) [src: arXiv:1808.07445, Sect. III.4.1]. SO 2025 uses
  ⟨N_hits²⟩²/⟨N_hits⁴⟩ for signal [src: arXiv:2512.15833, Sect. 3.1];
  CMB-S4 2020 builds signal, noise and cross fractions from analysis
  weights [src: arXiv:2008.12619, Eqs. 9–11]. Compare only under one
  definition.
- **Optimal band allocation that cannot be built.** Real dichroic tubes
  force a departure that raised the CMB-S4 effort from the optimum [src:
  arXiv:1907.04473, Sect. 7.2].
- **Avoiding the Galaxy.** Scan turnarounds at the Galactic boundary pile
  up coverage at map edges [src: Sect. 7.3].
- **Design treated as plan.** CMB-S4 numbers describe a cancelled project;
  LiteBIRD's 12 bands and NETs are not yet consolidated
  [src: arXiv:2607.25285, Sect. 2.3].
- **Polarisation or temperature depth.** SO 2018 tables give temperature
  depths, SO 2025 SAT tables polarisation (√2 higher) [src:
  arXiv:2512.15833, Table 1 note].
- **One collaboration's forecast quoted by another.** SPT-3G+ quotes 0.0014
  for SO (arXiv:2608.20236) [src: Sect. 2.2], the SO paper 1.2 × 10⁻³
  (arXiv:2512.15833) [src: abstract] (Who forecasts what for r).

## Reading list
<!-- key: reading-list -->

| Role | Paper | What for |
|---|---|---|
| Foundation | Knox 1995, arXiv:astro-ph/9504054 | mode counting and the value of resolution (read in L2; body not renderable here) |
| Method | Wu et al. 2014, arXiv:1402.4108 | NET-to-depth relation; detector, beam and sky-fraction grid |
| Method | Simons Observatory 2018, arXiv:1808.07445 | the ℓ_knee noise model, scan-strategy test, damping-tail requirements |
| Method | Simons Observatory 2025, arXiv:2503.00636, App. A | updated LAT survey, NETs, ℓ_ref against ℓ_knee |
| Method | Simons Observatory 2025, arXiv:2512.15833, Sects. 2, 3.1 | SAT expansion, f_sky definitions, delensing brackets |
| Method | CMB-S4 Collaboration 2020, arXiv:2008.12619, Sect. VII | realistic hit maps, Pole against Chile for r |
| Application | CMB-S4 Collaboration 2019, arXiv:1907.04473 | full flow-down: two-tier survey, detector-years, band split, LAT and SAT drivers, sites, half-wave plates |
| Application | Natoli et al. 2026, arXiv:2608.20236 | SPT-3G+ and the South Pole Observatory |
| Application | Hui et al. 2018, arXiv:1808.00568; Steiger et al. 2026, arXiv:2608.25015 | BICEP Array design and status |
| Application | CMB-HD Collaboration 2022, arXiv:2203.05728, Sect. 9; MacInnis et al. 2023, arXiv:2309.03021 | requirements derived by scaling SO; parameter forecasts |
| Application | LiteBIRD Collaboration 2022, arXiv:2202.02773, Sects. 3.2–3.3 | the pre-reformation requirement tree |
| Application | LiteBIRD Collaboration 2026, arXiv:2607.25285 | space scan parameters and band requirements after the reformation |
| Data | BICEP/Keck 2021, arXiv:2110.00483 | achieved depth and σ(r) |
| Data | Naess et al. 2025, arXiv:2503.14451, Sect. V.1 | measured atmospheric knees (ACT, with SPT and Planck quoted) |
| Critique | Harrington et al. 2026, arXiv:2609.26938 | delivered SO SAT NETs against the baseline targets |
| Review | Flaugher et al. 2022, arXiv:2209.08654 | the Stage-4 and CMB-HD concepts in the Snowmass report |

## Not verified
<!-- key: not-verified -->

- The SO companion instrument paper with detector NETs (cited as in
  preparation in arXiv:1808.07445, Sect. II.2).
- The CMB-S4 optimisation reference ([561] in arXiv:1907.04473) and its
  Fig. 7-70 per-channel optimum.
- The temperature survey-weight definition (A/N²) is inferred from the
  CMB-S4 table, not stated in the sections read.
- SPT-3G receiver design (Sobrin et al. 2018, arXiv:1809.00032), the
  bodies of the BICEP Array papers and of the Snowmass 2021 CMB-S4 white
  paper (abstracts only; its post-2019 design changes are not given);
  Planck and WMAP scan-strategy papers. No paper of the South Pole
  Observatory as such was found; it is described from the SPT-3G+ paper.
