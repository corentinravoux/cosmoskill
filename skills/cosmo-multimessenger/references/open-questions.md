# Open questions — multi-messenger cosmology

Scope: live controversies with both sides cited, method debates, what the next data decide, forecasts (labelled), and the stale claims that still circulate.
Snapshot: 2026-10-26 (light refresh of §1.7, §1.8 and the table of recurring errors; suite date 2026-10-07, literature searches run 2026-10-10)

Provenance flags as in the other files; all H0 values in km s⁻¹ Mpc⁻¹.

## 1. Live controversies
<!-- key: live-controversies -->

### 1.1 What does GW170817 say about H0?
<!-- key: what-does-gw170817-say-about-h0 -->

The gravitational-wave data alone gave the 14% precision of the first standard-siren
measurement, which cannot separate the CMB and Cepheid values; adding electromagnetic
information on the viewing angle brings it to about 7% (arXiv:2305.19914) [src: abstract],
with central values that depend on the analysis:

- low: 64.8 (+7.3/−7.2) with model-averaged velocities (arXiv:1909.00587); 65.5 ± 4.4
  with all VLBI data and hydrodynamical jets (arXiv:2605.11437); 66.2 (+4.4/−4.2) with
  kilonova and equation of state (arXiv:2002.11355) [src: abstract of each];
- middle: 68.9 (+4.7/−4.6) (arXiv:1806.10596); 68.3 (+4.6/−4.5) (arXiv:1909.08627)
  [src: abstract of each];
- high: 75.46 (+5.34/−5.39) with the afterglow to 3.5 yr (arXiv:2305.19914); 73.4
  (+3.3/−3.9) with a Cosmicflows-4 velocity for NGC 4993 (arXiv:2512.08818) [src: abstract
  of each].

All [src: abstract of each]. Two independent levers are at work: the jet model (viewing
angle) and the host velocity. The 2026 VLBI analysis lies 1.7σ from SH0ES
(arXiv:2605.11437); the 2023 afterglow analysis 1.5σ from the CMB (arXiv:2305.19914)
[src: abstract of each]. Neither is wrong on its face. A text that quotes "the" GW170817 H0
with a 4–5 error must name the jet model and the velocity model, and should not use it
as evidence for either side of the tension.

Underneath sits a prior question: the high-H0 tail of the GW-only posterior is a
property of the distance prior, not of the data (arXiv:2606.30504) [src].

### 1.2 Is the catalogue-level H0 a measurement of galaxies or of black-hole astrophysics?
<!-- key: is-the-catalogue-level-h0-a-measurement-of -->

- The LVK position in each release: the mass spectrum drives the result
  (arXiv:2111.03604 [src: abstract]; arXiv:2605.27227 [src: Sect. IV.1]). In GWTC-3 only GW190814 was informative
  through the catalogue.
- Bera et al. 2020 (arXiv:2007.04271) go further: without explicit use of clustering,
  "the inference of H0 from real data is expected to be prior-dominated".
- Against this, the best-localised-event analyses with deep photometric catalogues
  claim genuine catalogue information: about 20% from 8 events (arXiv:2111.06445),
  improved to (+12.0/−11.0) on 78.2 with 17 events and luminosity weighting
  (arXiv:2603.20195) [src: abstract of each]; and the GWTC-5.0 analysis reports a gain
  from DES Y6 with luminosity weighting (arXiv:2605.27227) [src: Sect. IV.1].
- The first cross-correlation detection, 5.9σ from two events (arXiv:2512.15380)
  [src: abstract],
  shows that clustering information exists in the data, concentrated in GW190814.

Open point: the share of the GWTC-5.0 constraint that comes from galaxies. The paper
gives it as a percentage improvement over the spectral-only posterior, different for
the two pipelines; the numbers are macros in the source and were not recovered.

### 1.3 Does the black-hole mass spectrum evolve with redshift, and does it matter yet?
<!-- key: does-the-black-hole-mass-spectrum-evolve-with -->

- It matters in principle: up to 3σ with 2000 events (arXiv:2312.11627); about 1.5σ in a
  blinded challenge at O4 sensitivity (arXiv:2412.14244); the second blinded challenge
  concludes that the spectrum must be known "at all relevant redshifts" to better than
  the statistical error (arXiv:2604.26273) [src: abstract of each].
- It does not show in the data yet: no compelling evidence in GWTC-4.0, and the model-
  form systematic is larger than the evolution systematic (arXiv:2605.20112); the
  independent model is favoured in GWTC-5.0 (arXiv:2609.25662); a redshift-dependent
  pair-instability scale fitted to GWTC-3 was not favoured by Bayes factors
  (arXiv:2204.13495).
- A subtlety from the 2026 analysis: fitting an evolving model to a non-evolving truth
  shifts H0 low by itself (arXiv:2605.20112) [src]. Flexibility is not free.

Both sides agree that the answer changes with sensitivity. The practical rule today:
quote the shift between mass-model families as a systematic.

### 1.4 Binary black holes with claimed counterparts
<!-- key: binary-black-holes-with-claimed-counterparts -->

GW190521 with the flare ZTF19abanrhr gives H0 = 50.4, 62.2 or 43.1 depending on the
waveform (arXiv:2009.14199) and 48 (+24/−10) in wCDM (arXiv:2009.14057) [src: abstract
of each]. A 2026
analysis of 13 black-hole mergers associated with active galactic nuclei reaches 4.4%,
70.50 (+3.37/−2.89) ± 1.56 (arXiv:2607.03672) [src: abstract]. The associations are the
assumption; the LVK cosmology papers treat GW170817 as "the only confidently identified
bright siren available" (arXiv:2605.27227) [src: Sect. IV.1]. A chance-coincidence analysis of
the 13 associations was not read here.

### 1.5 Is the galaxy-catalogue method biased?
<!-- key: is-the-galaxy-catalogue-method-biased -->

A claimed bias on mock data (Trott & Huterer 2021) was answered by Gair et al. 2022
(arXiv:2212.08694): unbiased when selection effects and priors are implemented
consistently. Real residual biases are documented from host weighting
(arXiv:2405.14818), features in photometric `n(z)` (arXiv:2602.04766) and completion
schemes (arXiv:2310.08991). The method is unbiased in principle and fragile in
practice.

### 1.6 Where are the baryons, according to FRBs?
<!-- key: where-are-the-baryons-according-to-frbs -->

- `f_igm = 0.59 (+0.11/−0.10)` from eight sightlines with foreground mapping
  (arXiv:2402.00505); `f_IGM = 0.76 (+0.10/−0.11)` (arXiv:2409.16952); `≥ 0.69` at 95%
  (arXiv:2506.04186); more than 90% in all diffuse gas (arXiv:2506.03536) [src: abstract
  of each]. The definitions differ (results file, Sect. 4.1), and the last is sensitive to the assumed
  Milky Way halo and host distributions.
- Halo gas: hot-gas fraction below about 10% of the cosmic fraction in `10^12–13 M☉`
  haloes, IllustrisTNG-300 too gas-rich (arXiv:2601.21336); no-feedback models
  disfavoured at about 9σ and agreement with kSZ (arXiv:2608.11296) [src: abstract of each]. Strong feedback is
  the common conclusion; its amplitude in the units a weak-lensing analysis needs is
  not settled. See `cosmo-weak-lensing` and `cosmo-cmb-lss-cross-correlations`.

### 1.7 Can FRBs measure H0?
<!-- key: can-frbs-measure-h0 -->

Published values differ by more than their quoted errors (results file, Sect. 4.3). The
statistical uncertainty "below 2.8%" of Xu et al. 2025 (arXiv:2507.18946) [src: abstract]
is not the total error, by the authors' own list of systematics. The structural limit is
the degeneracy with `Ω_b h² f_d` (physics file, Sect. 7.2): an FRB H0 is
an inverse-distance-ladder-like statement conditional on the baryon density, and is
not independent of early-universe physics unless something breaks the degeneracy
(gravitational-wave distances, arXiv:2508.14434, **forecast**). BAO break it in data:
120 localised bursts with DESI DR2 BAO give H0 = 71.4 (+2.2/−2.5) and
`Ω_b` = 0.0503 (+0.0025/−0.0021) without a CMB or BBN prior, and 68.8 ± 1.0 when the DM
distributions follow IllustrisTNG with the diffuse-gas fraction fixed; the authors name
extragalactic DM modelling as the dominant systematic (arXiv:2610.15536) [src: abstract].

### 1.8 Lensed supernovae: low or high?
<!-- key: lensed-supernovae-low-or-high -->

Refsdal gives 64.8 (eight models) or 66.6 (two models) (arXiv:2305.06367) and 66.0 ± 4.3
on re-modelling (arXiv:2509.09979); Encore 66.9 (+11.2/−8.1) (arXiv:2509.12301); H0pe
75.7 (+8.1/−5.5) (arXiv:2403.18902); SN 2025wny 70.8 (+8.2/−6.1) (arXiv:2608.28427)
[src: abstract of each]. Adding the host surface brightness to the Refsdal cluster model
gives 65.0 (+2.0/−1.8), a 3.0% uncertainty "given our cluster total mass
parameterization", which is held fixed (arXiv:2610.12595) [src: abstract].

They are consistent with each other and with both ends of the tension [der: comparison
of the values above]. The open question is whether
cluster mass models can be trusted at the level of their quoted spread; the galaxy-
scale system and the standard-candle magnification test are the two ways forward.

### 1.9 Are bright sirens still the main route?
<!-- key: are-bright-sirens-still-the-main-route -->

The 2017–2018 forecasts assumed tens of binary neutron stars with counterparts. None
has followed GW170817, and the rate estimates have come down (arXiv:2609.12053). The
same paper argues that a few bright sirens remain essential because they break the
H0–Ω_m degeneracy of dark sirens, or that dark sirens need an external Ω_m prior.

## 2. Method debates
<!-- key: method-debates -->

| Question | Positions | References |
|---|---|---|
| Completion of an incomplete catalogue | homogeneous; multiplicative; clustering-informed; Gaussian process; bright galaxies only | arXiv:2310.08991, arXiv:2608.24992, arXiv:2511.04786 |
| Host weighting | fix to luminosity in one band; or infer the exponent | arXiv:2405.14818, arXiv:2608.26307, arXiv:2609.04991 |
| All events or the best-localised | hierarchical analysis of everything above threshold; or golden/silver subsets with dedicated spectroscopy | arXiv:2605.27227, arXiv:2512.21729, arXiv:2607.17284 |
| Mass model | parametric families; non-parametric; trained on population synthesis | arXiv:2605.27227, arXiv:2404.02210, arXiv:2603.15332 |
| Catalogue method or cross-correlation | host-by-host likelihood; or two-point statistics with a free bias | arXiv:2212.08694, arXiv:2007.04271, arXiv:2512.15380 |
| Peculiar velocity of a host | smoothed direct distances; reconstruction from the galaxy density; both with covariance | arXiv:1909.00587, arXiv:1909.08627, arXiv:2509.03101 |
| Statistic to quote | MAP with highest-density interval; or median with symmetric interval | arXiv:1710.05835, arXiv:2509.04348 |
| FRB likelihood | localised bursts with `p(DM | z)`; or survey forward model with unlocalised bursts | arXiv:2507.18946, arXiv:2208.00819 |
| Bright and dark sirens | independent posteriors multiplied; or one population model | arXiv:2609.12053 |

### 2.1 Tracer choice for a field-level siren H0
<!-- key: tracer-choice-for-a-field-level-siren-h0 -->

Which tracer field to compare with a siren field in `d_L` is not settled in the
literature read here. What the cited papers establish:

- H0 comes from the position of the cross-correlation peak in `(z, d_L)`
  (arXiv:2512.15380). Whether that removes the need for an unbiased tracer of the
  matter field is an inference, not a statement of that paper.
- Every published dark-siren or cross-correlation H0 found in this session uses galaxy
  catalogues (results file, §2 and §3).
- Where velocities enter, they are reconstructed from the galaxy density field
  (arXiv:1909.08627) or taken from direct-distance catalogues for one host
  (arXiv:1710.05835, arXiv:1909.00587).
- Velocity covariance matters within 50 Mpc (arXiv:2509.03101) [src: abstract], and the non-linear BORG
  reconstruction is the best-performing field at `z ≲ 0.05` (arXiv:2502.00121).

Not verified here: the supernova sample sizes, the Manticore-Local depth and the
Hamlet-PM comparison quoted in that report.

## 3. What the next data decide
<!-- key: what-the-next-data-decide -->

| Data | Expected | Decides |
|---|---|---|
| LVK run IR1, six months, targeting a mid-January 2027 start [doc: https://www.aei.mpg.de/gwastronomy, 2026-10-26] | more events at O4-like sensitivity; a neutron-star merger with a counterpart would be the second bright siren | whether GW170817-based conclusions survive a second event |
| O4c data (2025-01-28 to 2025-11-18 [der]) in a future catalogue | the last part of O4 is not in GWTC-5.0 | spectral-siren precision; evolution of the mass spectrum |
| O5, no date ("Plans and timeline for the fifth observing run (O5) are in discussion") [doc: https://www.aei.mpg.de/gwastronomy, 2026-10-26] | — | the regime where population systematics dominate (arXiv:2312.11627) |
| Deep spectroscopy of siren localisation volumes | redshifts to `r ≈ 19` for the best events (arXiv:2607.17284) | whether catalogue information overtakes spectral information |
| Larger localised FRB samples; DSA with about `10^5` bursts (**forecast**, arXiv:2608.30943) | DM two-point statistics | feedback amplitude; `p(DM | z)` shape |
| Fourth image of SN Requiem, "within a few years" (arXiv:2509.12301) | decade-long delay baseline | a precise cluster-lens H0 |
| Further galaxy-scale lensed supernovae | delays of days to weeks | lens-model dependence against cluster systems |

## 4. Forecasts
<!-- key: forecasts -->

Every row is a **forecast**, not a measurement.

| Claim | Assumptions | Reference |
|---|---|---|
| H0 to about 2% within five years and 1% within a decade | LIGO–Virgo at design, counterparts for binary neutron stars | arXiv:1712.06531 |
| About 50 binary neutron stars arbitrate the tension | bright sirens | arXiv:1802.03404 [src: abstract] |
| 15 more GW170817-like events with radio imaging, against 50–100 without | jet-informed inclination | arXiv:1806.10596 [src: abstract] |
| 4.4% with about 250 binary neutron stars and a 50%-complete catalogue | simplified universe, O2-like sensitivity | arXiv:1908.06050 [src: abstract] |
| H0 to ±10% with about 100 events | neutron-star mass function narrower than 0.04 M☉ | arXiv:1108.5161 [src: abstract] |
| `H(z)` to 6.1% at `z ≈ 0.8` after one year at design, 2.9% after five | fixed pair-instability scale | arXiv:1908.09084 [src: abstract] |
| `H(z)` better than 10% at `z ≲ 1` in a year (2G); ≲ 1% at `z ≳ 2` in a month (3G) | full mass spectrum | arXiv:2202.08240 [src: abstract] |
| 5.8% on H0 and 6.4% on `H(0.9)` from 1000 events | non-parametric mass model | arXiv:2404.02210 [src: abstract] |
| H0 about 20%, `H(z)` about 7% at `z ≈ 0.8`, `Xi_0` about 10% in five years | LIGO–Virgo design, population method | arXiv:2112.05728 [src: abstract] |
| Percent-level H0 from the best 100 black-hole binaries of O5 | complete spectroscopic catalogue | arXiv:2312.05302 [src: abstract] |
| 0.98% (median) from ten events in one year; 2.63% with the A+ network | A# network with LIGO-India, spectroscopy to `r ≈ 19` | arXiv:2607.17284 [src: abstract] |
| A few percent from golden and silver sirens in one year | A# network, HETDEX-depth spectroscopy at `z < 0.2` | arXiv:2512.21729 |
| Less than 10% (2%) at 90% from 50 (500) black-hole binaries | cross-correlation, fully incomplete catalogue | arXiv:2007.04271 [src: abstract] |
| Percent level needs `σ_dL = 0.1 d_L` and at least 5000 dark sirens | tomographic cross-correlation | arXiv:2510.19931 [src: abstract] |
| `σ(H0) ≈ 1` with about 90 low-redshift bright sirens, or about 20 with BAO | Einstein Telescope; information saturates above `z ≈ 1` | arXiv:2607.20413 [src: abstract] |
| Sub-percent `H(z)` over more than 10 billion years | next-generation networks, all siren classes combined | arXiv:2402.03120 [src: abstract] |
| Waveform and calibration accuracy must scale as `O(ρ⁻²)` | golden dark sirens, next generation | arXiv:2602.14898 |
| Competitive H0 and `w0` | LISA extreme-mass-ratio inspirals and massive binaries combined | arXiv:2603.23612 |
| 1.3% on H0 from about 200 GW190521-like events | counterparts in AGN discs are real | arXiv:2009.14199 [src: abstract] |
| H0 to ±2.5 from 100 localised FRBs | upgraded ASKAP search | arXiv:2208.00819 [src: abstract] |
| H0 to about 2.6% from about 100 localised FRBs; 1% from a few hundred | scatter models as assumed | arXiv:2108.00581, arXiv:2104.04538 [src: abstract of each] |
| H0 to ±6 in one year | FRBs with Einstein Telescope distances | arXiv:2508.14434 |
| Photometric redshifts cost up to an order of magnitude | sirens with galaxy catalogues in the 2040s | arXiv:2512.18369 |

Track record: the 2017 forecast of 2% in five years (arXiv:1712.06531) [src: abstract]
has not been met (collaboration values in the results file, Sect. 6.1) because the
assumed counterparts did not occur. The FRB forecasts of 2021–2022 (about 2.6% from
about 100 localised bursts, arXiv:2108.00581; ±2.5 km/s/Mpc from 100 mock bursts,
arXiv:2208.00819) can be compared with the 2025 analysis of 95 bursts, whose
uncertainty "below 2.8%" is statistical only (arXiv:2507.18946) [src: abstract of each]
and whose central value differs from other FRB analyses by more than that. Forecasts in this field have been limited by event rates and by systematics that the
forecast did not contain.

Einstein Telescope science and configurations are in arXiv:2503.12263; that paper was
read at abstract level only and no cosmological number is taken from it.

## 5. Misconceptions and stale claims
<!-- key: misconceptions-and-stale-claims -->

| Claim | Why it is wrong or stale | Corrected by |
|---|---|---|
| "Standard sirens give H0 = 70 (+12/−8)." | That is GW170817 alone in 2017. The collaboration value is 71.7 (+9.4/−7.5) from GWTC-5.0. | arXiv:1710.05835, arXiv:2605.27227 [src: abstract of each] |
| "The LVK dark-siren result is 68 (+8/−6)." | GWTC-3 with a fixed population; the joint analysis gives 69 (+12/−7), and two releases have followed. | arXiv:2111.03604, arXiv:2308.02281 [src: abstract of each]; arXiv:2605.27227 |
| Quoting a GWTC-4.0 H0 from memory. | The arXiv abstract read on 2026-10-10 gives 75.4 (+12.8/−9.1); check the version cited, and prefer GWTC-5.0. | arXiv:2509.04348 [src: abstract] |
| "GW170817 with the jet gives 68.9 ± 4.7, a 7% measurement." | One of several jet-informed values that differ by more than their errors: 68.9 (+4.7/−4.6) (arXiv:1806.10596), 65.5 ± 4.4 (arXiv:2605.11437), 75.46 (+5.34/−5.39) (arXiv:2305.19914). | arXiv:1806.10596, arXiv:2605.11437, arXiv:2305.19914 [src: abstract of each] |
| "Sirens are free of astrophysical assumptions." | True of the distance. The redshift of a dark siren comes from the mass spectrum or from a host model. | arXiv:2103.14663, arXiv:2312.11627 |
| "Sirens need no cosmological model." | True at `z << 1`. The dark-siren constraint peaks at `z ≈ 0.44`; H0 is an extrapolation under a background model. | arXiv:2511.11795 |
| "The dark-siren method uses a galaxy catalogue complete to the detection horizon." | GLADE+ is complete to 47 Mpc. | arXiv:2110.06184 [src: abstract] |
| "The catalogue method is intrinsically biased." | Not when selection effects are treated consistently. | arXiv:2212.08694 |
| "Peculiar-velocity errors average out with more sirens." | Nearby hosts share bulk flows; covariance can double the error within 50 Mpc. | arXiv:2509.03101 [src: abstract] |
| "The peculiar velocity of NGC 4993 is 310 ± 150 km/s." | One estimate (arXiv:1710.05835 [src: Methods, Sect. "Finding the Hubble velocity of NGC 4993"]); BORG gives 373 with σ ≈ 130 (arXiv:1909.08627 [src: Sect. 6.1]), and direct-distance catalogues disagree beyond their errors (arXiv:1909.00587 [src: Sect. 3.2]). | arXiv:1710.05835, arXiv:1909.08627, arXiv:1909.00587 |
| "GWTC-5.0 has 267 events." | 390 candidates; 267 in the population analysis; 236 in cosmology. | arXiv:2605.27225, arXiv:2605.27226, arXiv:2605.27227 [src: abstract of each] |
| "O5 starts in 2027." | "Plans and timeline for the fifth observing run (O5) are in discussion"; a six-month run IR1 targets a mid-January 2027 start. | AEI page [doc: https://www.aei.mpg.de/gwastronomy, 2026-10-26] |
| "2% from sirens within five years." | A 2017 forecast, conditional on counterparts that did not occur. | arXiv:1712.06531 |
| "FRBs give an independent H0." | Conditional on `Ω_b h²` and on the diffuse baryon fraction. | arXiv:2508.14434 |
| "FRBs measure H0 to under 3%." | Statistical error only ("below 2.8%"); other analyses differ from it by more than that (results file, Sect. 4.3). | arXiv:2507.18946 [src: abstract] |
| "`f_IGM ≈ 0.8` is measured." | 0.59, 0.76, ≥ 0.69 and "more than 90%" under different definitions and samples. | arXiv:2402.00505, arXiv:2409.16952, arXiv:2506.04186, arXiv:2506.03536 [src: abstract of each] |
| "The DM scatter at fixed redshift is log-normal." | Not a good match to ray-traced simulations. | arXiv:2507.07090 |
| "Only two lensed supernovae have given H0." | Four by August 2026: Refsdal, H0pe, Encore (the third, arXiv:2509.12301), SN 2025wny (arXiv:2608.28427). | arXiv:2509.12301, arXiv:2608.28427 [src: abstract of each] |
| "Time-delay cosmography gives 73.3 with 2.4%." | That is H0LiCOW with assumed lens profiles (arXiv:1907.04869); with the mass-sheet degeneracy free, 71.6 (+3.9/−3.3) for TDCOSMO-2025 and 71.1 (+2.4/−2.3) for TDCOSMO-2026, which supersedes it. | arXiv:1907.04869, arXiv:2506.03023, arXiv:2610.14881 [src: abstract of each]; `cosmo-distance-ladder-h0` |
| "Modified GW propagation is excluded." | `Xi_0 = 1.4 (+1.0/−0.4)` in GWTC-4.0: consistent with 1, weakly constrained. | arXiv:2509.04348 |

## Not verified
<!-- key: not-verified -->

- Lensed gravitational waves: LVK searches and their results were not read; only 2026
  forecast titles were seen.
- Lensed FRBs as a time-delay probe: not researched.
- Gravitational-wave × HI intensity-mapping and × SKAO forecasts appeared in the 2026
  search (titles only).
- The statistical significance of the 13 AGN associations of arXiv:2607.03672 [src: abstract for the count].
- Whether a third-party reanalysis of the GWTC-5.0 catalogue contribution exists.
- Milestones of the Einstein Telescope, Cosmic Explorer and LISA.
