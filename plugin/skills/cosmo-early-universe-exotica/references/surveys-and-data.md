# Early-Universe exotica — surveys and data

Scope: the pulsar-timing arrays and their data releases, ground-based and planned gravitational-wave detectors as stochastic-background probes, microlensing surveys behind primordial-black-hole limits, absolute-spectrum CMB instruments, and the CMB and gamma-ray data used for the other limits. Past, current, planned.
Snapshot: 2026-10-26

Flags as in `physics-and-methods.md`.

## 1. Pulsar-timing arrays
<!-- key: pulsar-timing-arrays -->

The 2023 releases were coordinated (June 2023); the International Pulsar
Timing Array (IPTA) compares and combines them. "First evidence" from the
major arrays is at the ~2–4σ level (arXiv:2412.01153) [src].

| Array | Data set | Pulsars, span | Telescopes | Headline (abstract) | Citation | Flag |
|---|---|---|---|---|---|---|
| NANOGrav | 15 yr data set (2023) | 67 pulsars in the GWB analysis; 16.03 yr | Arecibo, GBT, VLA | HD-correlated background, p ≈ 10⁻³ (Bayes-factor null) and 5 × 10⁻⁵–1.9 × 10⁻⁴ (frequentist) | arXiv:2306.16213 | [src: Sect. VI] |
| EPTA + InPTA | EPTA DR2 (24.7 yr full; 10.3 yr "new" subset), InPTA DR1 for ten common pulsars | 25 pulsars | European telescopes; uGMRT for InPTA | Bayes factor 60, false-alarm 0.1% for the 10.3 yr subset | arXiv:2306.16214 | [src: abstract] |
| PPTA | DR3 | 30 pulsars, 18 yr | Parkes (Murriyang) | HD significance p ≲ 0.02 (~2σ); signal strength time-dependent | arXiv:2306.16215 | [src: abstract] |
| CPTA | DR1 | — (FAST observations) | FAST | 4.6σ HD around 14 nHz with the discrete-frequency method | arXiv:2306.16216 | [src: abstract] |
| MPTA | 4.5 yr data release | 83 pulsars, ~250,000 arrival times, median error 3 μs | MeerKAT | HD 3–3.4σ in one noise model, insignificant in others | arXiv:2412.01153 | [src: abstract] |
| InPTA | DR2 | 27 pulsars, up to 7.2 yr, two bands | uGMRT | CURN Bayes factor 2.5; HD consistent with zero; A_GWB < 3.4 × 10⁻¹⁴ at γ = 13/3 | arXiv:2608.02808 | [src: abstract] |
| IPTA | comparison of 2023 results | all five arrays | — | GWB parameters agree within 1σ across arrays; DR3 combination in preparation | arXiv:2309.00693 | [src] |
| Independent combination | public data of five PTAs | 121 pulsars | — | consistent with non-zero amplitude, below 5σ; reconstructed correlation matches HD | arXiv:2512.08666 | [src: abstract] |

The InPTA DR2 paper estimates that a baseline of at least 10 yr is needed
before its data start to recover the common red noise (arXiv:2608.02808) [src: abstract]. The IPTA comparison found that "extending" each array with pulsars it
does not time improves the amplitude constraint and the HD signal-to-noise
ratio, the logic of IPTA DR3 (arXiv:2309.00693) [src]. The independent
five-array analysis is not a collaboration release: it merges per-pulsar
models by "direct combination" instead of choosing a single timing model
(arXiv:2512.08666) [src].

### 1.1 Low-frequency radio support and what comes next
<!-- key: low-frequency-radio-support-and-what-comes-next -->

- EPTA DR2low adds LOFAR (100–200 MHz) and NenuFAR (30–90 MHz) data to
  the EPTA + InPTA DR2new+ set for 12 pulsars over ~11 yr. Red noise is
  then required in 10 of 12 pulsars instead of 5, an extra chromatic term
  appears in eight, and unmodelled solar-wind delays near conjunction are
  absorbed into the dispersion measure (Iraci et al. 2025,
  arXiv:2510.04639) [src: abstract]. The noise model of a pulsar thus depends on the
  frequency coverage of the data, which feeds directly into the background
  inference.
- InPTA DR2 single-pulsar noise analysis of 27 pulsars: pulsars with baselines ≲ 2.5 yr show Gaussian
  residuals and (one exception) no red noise; 4 of 15 longer-baseline pulsars keep significant
  non-Gaussian residuals, which "may require more advanced methods" (Nobleson et al. 2025, arXiv:2512.20455) [src: abstract].
- IPTA DR3, the full combination in which pulsars timed by several arrays
  are merged, is announced in arXiv:2309.00693 as the next step [src]; no
  IPTA DR3 background result was found with an arXiv identifier at the
  snapshot (see "Not verified").

## 2. Ground-based and space interferometers as background probes
<!-- key: ground-based-and-space-interferometers-as -->

| Data | Observing runs | Band dominating the limit | Citation | Flag |
|---|---|---|---|---|
| LIGO–Virgo O3 (+ O1, O2) | to 2020 | 20–76.6 Hz for a flat spectrum | arXiv:2101.12130 | [src: abstract] |
| LVK O1–O4a | to the end of O4a | — | arXiv:2508.20721 | [src] |
| LVK O1 to 1 April 2025 (within O4) | adds O4 data, re-processes earlier O4 data with new frequency-domain cuts for non-stationary spectral lines | — | arXiv:2608.23477 | [src] |

LISA will survey the 0.1 mHz – 1 Hz band; its definition-phase summary is
the "Red Book" (Colpi et al. 2024, arXiv:2402.07571) [src: abstract], and its
cosmology programme — phase transitions, strings, inflation, PBHs,
non-standard pre-BBN histories — is the LISA Cosmology Working Group review
(arXiv:2204.05434) [src: outline]. LISA as a facility belongs to
`cosmo-surveys-facilities`, standard sirens to `cosmo-multimessenger`. The
LVK O4 limits re-process earlier O4 data with frequency-domain cuts against
non-stationary spectral features, and verify that correlated magnetic noise
(Schumann resonances) stays below sensitivity (arXiv:2608.23477;
arXiv:2101.12130) [src].

### 2.1 Bands and sensitivities
<!-- key: bands-and-sensitivities -->

| Instrument | Band | Sensitivity statement | Citation | Flag |
|---|---|---|---|---|
| NANOGrav 15 yr | f_i = i/T, T = 16.03 yr (arXiv:2306.16213, Sect. II); bin 2 at f₂ = 3.95 nHz (arXiv:2306.16213, Fig. 6 caption) | minimum noise characteristic strain 7 × 10⁻¹⁵ at 5 nHz (arXiv:2306.16218, abstract) | arXiv:2306.16213; arXiv:2306.16218 | [src: Sect. II, Fig. 6 caption; abstract] |
| PTAs in general | 10⁻⁹ – 10⁻⁶ Hz | — | arXiv:2204.05434 | [src: Sect. 5.1.3] |
| LVK O3 | 20–76.6 Hz (α = 0), 20–90.6 Hz (α = 2/3), 20–291.6 Hz (α = 3), 99% of sensitivity | — | arXiv:2101.12130 | [src: abstract] |
| LISA | 0.1 mHz – 1 Hz | — | arXiv:2402.07571 | [src: abstract] |
| Binary pulsars, Earth–Moon resonances | ~1 μHz | Ω_GW ≳ 6 × 10⁻⁶ excluded; ≳ 5 × 10⁻⁹ by the late 2030s (**forecast**) | arXiv:2204.05434 | [src: Sect. 5.1.3] |
| CMB B modes (Planck + BICEP/Keck) | f = 7.7 × 10⁻¹⁷ Hz | Ω_GW h² < 1.5 × 10⁻¹⁶ from r < 0.036 | arXiv:2204.05434 | [src: Sect. 5.1.3] |

## 3. Microlensing surveys for compact objects
<!-- key: microlensing-surveys-for-compact-objects -->

| Survey | Targets | Data behind the limit | Citation | Flag |
|---|---|---|---|---|
| MACHO | Magellanic Clouds | claimed halo lens population; disputed by EROS and OGLE | cited via arXiv:2601.06024 and arXiv:2509.05400 | [src] |
| EROS-2 | LMC and SMC | 33 × 10⁶ stars monitored 6.7 yr; bright-star subsample of 7 × 10⁶ over 84 deg² (LMC) and 9 deg² (SMC) | arXiv:astro-ph/0607207 | [src: abstract] |
| Subaru/HSC | M31 | one 7 h night at 2 min cadence | arXiv:1701.02151 | [src] |
| OGLE (bulge) | Galactic bulge | 2622 events over 5 yr | arXiv:1901.07120 | [src: abstract] |
| OGLE (LMC, 20 yr) | LMC | ~80 million stars over 20 yr | arXiv:2403.02386 | [src: abstract] |
| OGLE (high cadence) | LMC and SMC centres | ~35 million stars, October 2022 – May 2024 | arXiv:2410.06251 | [src: abstract] |

Rubin LSST, Roman and X-ray timing (NICER and successors) are the next
microlensing and X-ray-lensing data; the X-ray route is named by Carr et al.
for the asteroid window (arXiv:2601.06024) [src: Sect. V].

## 4. Absolute-spectrum CMB instruments
<!-- key: absolute-spectrum-cmb-instruments -->

| Instrument | Status | Design and target | Citation | Flag |
|---|---|---|---|---|
| COBE/FIRAS | past (data from the early 1990s) | absolute spectrophotometer; RMS deviations < 50 ppm of the peak | Fixsen et al. 1996, arXiv:astro-ph/9605054 | [src: Sect. 6.1, Sect. 8] |
| FIRAS reanalysis (μ map) | 2022 | first μ map from a spectrometer; cross-correlated with Planck T and polarisation | arXiv:2206.02762 | [src] |
| TMS (Tenerife Microwave Spectrometer) | ground, 10–20 GHz | optical system described | arXiv:2111.15364 | [src: abstract] |
| COSMO | ground (Antarctica) | multi-mode antennas; part of the TMS + COSMO + BISOU combination | arXiv:2406.09349 | [src] |
| BISOU | balloon concept | pathfinder of a space mission; 5σ y-distortion measurement achievable (**forecast**) | Maffei et al. 2021, arXiv:2111.00246 | [src] |
| PIXIE | Explorer-class concept | single cryogenic Fourier-transform spectrometer against an external blackbody; 300 channels, 28 GHz – 6 THz, 2.65° beams, ~200 Jy/sr per beam; > 1000 × FIRAS sensitivity (**forecast**) | Kogut et al. 2024, arXiv:2405.20403 (original concept arXiv:1105.2044) | [src: abstract] |
| PIXIE, Super-PIXIE in the Voyage 2050 paper | concepts | σ(y) ≃ 3.4 × 10⁻⁹, σ(μ) ≃ 3 × 10⁻⁸ (PIXIE); σ(y) ≃ 1.6 × 10⁻⁹, σ(μ) ≃ 7.7 × 10⁻⁹ (Super-PIXIE), with foregrounds (**forecast**) | arXiv:1909.01593 | [src: Sect. 1.2] |
| FOSSIL | proposed space mission | ~three orders of magnitude better than FIRAS; would detect the ΛCDM μ (**forecast**) | arXiv:2609.16194 | [src] |

Cyr et al. state that TMS, COSMO and BISOU together "will provide the first
discovery of a monopole y-type distortion within the coming decade" (**forecast**; arXiv:2609.16194) [src: abstract]. The original PIXIE concept was aimed
primarily at B-mode polarisation, r < 10⁻³ at 5σ (arXiv:1105.2044) [src: abstract];
the 2024 design adds the spectrum, τ and line intensity mapping
(arXiv:2405.20403) [src].

## 5. CMB anisotropy data used for exotica
<!-- key: cmb-anisotropy-data-used-for-exotica -->

## 6. Gamma-ray and other data
<!-- key: gamma-ray-and-other-data -->

## 7. Status at a glance
<!-- key: status-at-a-glance -->

| Probe | Past | Current (snapshot) | Planned |
|---|---|---|---|
| nHz background | pre-2023 PTA upper limits | five arrays with 2–4σ HD evidence; combinations below 5σ | IPTA DR3; longer InPTA and MPTA baselines |
| LVK-band background | O1–O3 limits | O4 limits to April 2025; CBC foreground predicted within a factor of a few | further O4/O5 runs |
| mHz background | — | — | LISA |
| Compact-object microlensing | MACHO, EROS-2 | OGLE LMC (twenty years), OGLE high-cadence, Subaru/HSC | X-ray-pulsar lensing (asteroid window) |
| Spectral distortions | COBE/FIRAS | FIRAS reanalyses | TMS, COSMO, BISOU; PIXIE, FOSSIL concepts |
| Recombination physics | Planck | ACT DR6, SPT-3G D1 | — |

Each row draws on the tables above; no new number is introduced.

## Not verified
<!-- key: not-verified -->

- IPTA DR3: a paper titled "From a Rumble to a Roar: The International
  Pulsar Timing Array's Third Data Release" appears in INSPIRE without an
  arXiv identifier; its content was not read.
- NANOGrav, EPTA, PPTA and CPTA releases after 2023 (beyond the 2025 EPTA
  DR2low and PPTA DR3 continuous-wave papers) were not searched in full.
- The LISA launch date and adoption status were not read; see
  `cosmo-surveys-facilities`.
- The exact Planck multipole cut inside P-ACT.
- Release dates and status of TMS, COSMO and BISOU beyond what their
  instrument papers state.
<!-- key: not-verified -->
