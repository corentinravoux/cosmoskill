# Results — headline measurements

Scope: current values of H0 and related parameters from standard sirens, fast radio bursts and lensed transients, the model each assumes, and the history that tells which values are superseded.
Snapshot: 2026-10-13 (deepening pass, 12–13 October; first build 2026-10-07, searches 2026-10-10)

All H0 values are in km s⁻¹ Mpc⁻¹. Every value below was read this session in the
abstract of the cited paper unless a section is named. "MAP" is maximum a posteriori
with a highest-density interval; "median" is the median with a symmetric interval;
intervals are 68% unless stated. Where the arXiv abstract and a journal version may
differ, the arXiv abstract as served on 2026-10-10 is what is quoted.

## 1. Bright siren GW170817
<!-- key: bright-siren-gw170817 -->

One event, many values: the gravitational-wave data are the same in every row. What
changes is the velocity of NGC 4993, the viewing-angle information and the priors.

| H0 | Statistic | Extra information beyond GW + host redshift | Velocity treatment | Reference | Flag |
|---|---|---|---|---|---|
| 70.0 (+12.0/−8.0) | MAP, flat-in-log prior [src: Methods]; the median with symmetric interval is 74.0 (+16.0/−8.0) [src: Extended Data Table 1] | none | 6dFGSv kernel, 150 km/s error | arXiv:1710.05835 | [src] |
| 68.7 (+17.5/−8.3) | highest-density interval, flat-in-log prior | none (GW170817-only value in the O2 paper) | — | arXiv:1908.06060 | [src] |
| 76 (+19/−13) | — | none; re-derived from public data | — | arXiv:1807.05667 | [src] |
| 68.9 (+4.7/−4.6) | — | VLBI superluminal motion and light curve | — | arXiv:1806.10596 | [src] |
| 66.8 (+13.4/−9.2) | Bayesian model average | none | several catalogues and groups | arXiv:1909.00587 | [src] |
| 64.8 (+7.3/−7.2) | Bayesian model average | radio viewing angle | several catalogues and groups | arXiv:1909.00587 | [src] |
| 68.3 (+4.6/−4.5) | — | VLBI | BORG on 2M++ plus virial term | arXiv:1909.08627 | [src] |
| 68.6 (+14.0/−8.5) | — | none | kernel scale marginalised | arXiv:1909.09609 | [src] |
| 66.2 (+4.4/−4.2) | 1σ | kilonova, gamma-ray burst, equation-of-state prior, GW190425 | — | arXiv:2002.11355 | [src] |
| 75.46 (+5.34/−5.39) | 68% credible | afterglow to about 3.5 yr (optical, X-ray, radio) | host velocity included | arXiv:2305.19914 | [src] |
| 70.9 (+6.4/−8.5) | — | — | DESI Fundamental Plane velocities of the group | arXiv:2512.08818 | [src] |
| 73.4 (+3.3/−3.9) | — | — | Cosmicflows-4 SBF velocity of NGC 4993 | arXiv:2512.08818 | [src] |
| 65.5 ± 4.4 | — | all VLBI data, visibility-plane fit, hydrodynamical jets | ensemble of corrections marginalised | arXiv:2605.11437 | [src] |

Related numbers:

- Distance: `d_L = 43.8 (+2.9/−6.9)` Mpc from the GW signal [sec: arXiv:1909.08627 §6.1];
  40.7 ± 1.4 (random) ± 1.9 (systematic) Mpc from surface-brightness fluctuations, which
  with the corrected recession velocity gives H0 = 71.9 ± 7.1, not a siren measurement
  (arXiv:1801.06080) [src]; 44.0 ± 1.6 Mpc from the 2026 VLBI fit (arXiv:2605.11437)
  [src].
- Viewing angle: about 20° (arXiv:1806.09693); 18.3°–20.3° at fixed `d_L = 40.7` Mpc and
  16.8°–19.2° with `d_L` free (arXiv:2605.11437) [src].
- Velocities: group recession velocity 3327 ± 72 km/s in the CMB frame [sec:
  arXiv:1909.08627 §6.1]; peculiar velocity 310 ± 69 km/s from 6dFGSv, adopted with
  150 km/s [sec: arXiv:1909.00587 §3.2]; 373 km/s mean with total σ ≈ 130 km/s from BORG
  (arXiv:1909.08627 §6.1) [src]. Hubble-flow velocity 3327 − 310 = 3017 km/s [der].
- Prior dependence: under a uniform-in-`d_L` prior the weighted median is 87.6 instead
  of 77.6 while the mode stays at 70.5 (arXiv:2606.30504) [src].

Reading the table: the six values that use jet or afterglow information lie between
64.8 and 75.5 with quoted errors of 4 to 7 [der: range of the rows above]. The same
data therefore support both a Planck-like and a SH0ES-like value depending on the jet
model, and no single row is "the" GW170817 result. Gourdji et al. 2026 place their peak
0.5σ from Planck and 1.7σ from SH0ES; Palmese et al. 2023 are within 1σ of the
Cepheid-anchored value and 1.5σ of the CMB value [src, both abstracts].

Candidate bright sirens that are not established:

| Event | Assumption | H0 | Model | Reference |
|---|---|---|---|---|
| GW190521 | ZTF19abanrhr (`z = 0.438`) is the counterpart | 50.4 (+28.1/−19.5), 62.2 (+29.5/−19.7), 43.1 (+24.6/−11.4) for three waveform models | flat ΛCDM, Ω_m marginalised | arXiv:2009.14199 |
| GW190521 | same | 48 (+24/−10) | flat wCDM | arXiv:2009.14057 |
| GW190521 + GW170817 with VLBI | same | 67.6 (+4.3/−4.2) | flat ΛCDM | arXiv:2009.14199 |
| 13 BBH with claimed AGN-flare hosts | all 13 associations real | 70.50 (+3.37/−2.89) (stat) ± 1.56 (cal) | — | arXiv:2607.03672 |

The last row is the tightest siren number in the literature and is conditional on
associations that the LVK analyses do not use.

## 2. Dark sirens and catalogue-level H0
<!-- key: dark-sirens-and-catalogue-level-h0 -->

### 2.1 LVK collaboration results (flat ΛCDM)
<!-- key: lvk-collaboration-results-flat-lambdacdm -->

| Catalogue | Events used | H0 | What is combined | Reference | Flag |
|---|---|---|---|---|---|
| O1–O2 | BBH with galaxy catalogues (DES for GW170814), plus GW170817 | 68.7 (+17.0/−7.8) (flat-in-log prior, highest-density) | catalogue + bright | arXiv:1908.06060 | [src] |
| GWTC-3 | 47 | 68 (+12/−7) (arXiv abstract) | spectral + bright | arXiv:2111.03604 | [src] |
| GWTC-3 | 47 | 68 (+8/−6) | GLADE+ catalogue, **fixed** population, + bright | arXiv:2111.03604 | [src] |
| GWTC-4.0 | 142 of 218 | 75.4 (+12.8/−9.1); 90%: (+24.5/−13.3) (median; arXiv abstract) | spectral + GLADE+ + bright | arXiv:2509.04348 | [src] |
| GWTC-5.0 | 236 | 71.7 (+9.4/−7.5) (median) | spectral + DES Y6 catalogue with luminosity weighting + bright | arXiv:2605.27227 | [src] |

Notes.

- GWTC-5.0 is the current collaboration value. Its uncertainty is 22.0% smaller than
  that of GWTC-4.0 [src]. Fractional half-width: (9.4 + 7.5)/2/71.7 = 11.8%; for
  GWTC-4.0, (12.8 + 9.1)/2/75.4 = 14.5%; for GW170817 alone in 2017, 14% [der for the
  first two; src for the third, arXiv:2305.19914].
- The spectral-only and catalogue-only GWTC-5.0 posteriors are "now tighter than" the
  GW170817 bright-siren posterior, and the dark-siren analysis "excludes the tail of
  high H0 values" of the bright siren (arXiv:2605.27227 §4.1) [src]. The values, read
  in the HTML rendering on 2026-10-12 [src: Sect. IV.1, Table 3]: spectral only 70.1
  (+15.1/−13.3); dark sirens with DES `r` band and luminosity weighting 68.8
  (+14.2/−13.2); GW170817 as bright siren, recomputed with the same population and
  injections, 79.1 (+27.6/−12.4); combined 71.7 (+9.4/−7.5), 90%: (+17.7/−11.4). With
  the other mass models the combined value is 73.1 (+12.3/−8.6) (multi-peak, BBH only)
  and 72.3 (+9.0/−7.4) (FullPop 3 Peaks, mildly preferred by the Bayes factors but not
  adopted, for continuity with GWTC-4.0). All with `Ω_m = 0.3065` fixed and H0 on
  U(10, 200).
- The galaxy catalogue improves the GWTC-5.0 spectral constraint by 3.5% (DES) or 2.8%
  (GLADE+); against GWTC-4.0 the spectral result improved by 14.6% and the GLADE+
  dark-siren result by 13.2% (arXiv:2605.27227) [src: Sect. IV.1, V.1].
- GWTC-4.0 in two versions: the body read on 2026-10-12 (ar5iv rendering) gives 76.6
  (+13.0/−9.5) combined, 81.6 (+21.5/−15.9) dark only, 76.4 (+23.0/−18.1) spectral only
  and 78.4 (+25.7/−12.0) for GW170817 [src: Sect. IV.1], while the table above quotes
  the arXiv abstract read on 2026-10-10. The rendering is of an earlier version of the
  paper; quote the version you cite.
- The GWTC-3 improvements were 17% (spectral) and 42% (catalogue) over GWTC-1 [src].
- In every release the collaboration states that the mass-spectrum features, not the
  galaxy catalogue, drive the constraint (systematics file, §5).
- Against the Hubble tension: the gap between the local and CMB values in
  `cosmo-distance-ladder-h0` is about 6; the GWTC-5.0 half-width is about 8.5 [der].
  The result is consistent with both.

### 2.2 External analyses of the same catalogues
<!-- key: external-analyses-of-the-same-catalogues -->

| Data | Method | H0 | Reference |
|---|---|---|---|
| GW170817 without its counterpart | catalogue, galaxies above 0.01 L*_B, flat prior [10, 220] | 76 (+48/−23) | arXiv:1807.05667 |
| GW170814 + DES Y3 | catalogue, prior [20, 140] | 75.2 (+39.5/−32.4) | arXiv:1901.01540 |
| GWTC-2 + GLADE | catalogue, dark only | 67.3 (+27.6/−17.9) | arXiv:2101.12660 |
| GWTC-2 + GLADE + GW170817 | catalogue + bright | 72.2 (+13.9/−7.5) | arXiv:2101.12660 |
| 8 dark sirens + DESI Legacy | catalogue, prior [20, 140] | 79.8 (+19.1/−12.8); with GW170817 72.77 (+11.0/−7.55) | arXiv:2111.06445 |
| GWTC-3 + GLADE+ | joint population and catalogue (`gwcosmo`) | 69 (+12/−7) (MAP) | arXiv:2308.02281 |
| 10 well-localised O3 dark sirens (DECam photometry) | catalogue | 76.00 (+17.64/−13.45) | arXiv:2310.13695 |
| 15 dark sirens (5 from O4a) + DESI Legacy | catalogue | 70.4 (+13.6/−11.7); with GW170817 and jet 68.0 (+4.4/−3.8) | arXiv:2404.16092 |
| 17 dark sirens (7 from O4a) + DESI Legacy | catalogue, r-band weighting | 78.2 (+12.0/−11.0); unweighted 78.8 (+14.6/−12.2); with GW170817, jet and velocity correction 69.9 (+4.1/−4.0) | arXiv:2603.20195 |
| GWTC-4.0 (142 events) | spectral, new full-spectrum model | 78.8 (+19.0/−15.3) | arXiv:2601.03257 |
| GWTC-4.0 (142 events) | catalogue + spectral | 82.5 (+16.8/−14.3) | arXiv:2601.03257 |
| GWTC-4.0 + DES Y6 Gold | `gwcosmo`, `0.05 < z < 0.50` | 71.7 (+22.7/−18.3); with GW170817 73.1 (+11.9/−8.5) | arXiv:2602.04766 |
| GWTC-4.0 + DES Y3 3×2pt + GW170817 with jet | joint | 67.9 (+4.4/−4.3); 9.9% without the jet | arXiv:2601.04774 |
| GWTC-4.0 | normalising-flow population trained on synthetic catalogues | 71.62 (+4.04/−4.00) | arXiv:2603.15332 |
| GWTC-5.0 (235 BBH) | spectral, independent mass and redshift | 74.3 (+13.7/−19.6) | arXiv:2609.25662 |
| GWTC-5.0 subset | `gwcosmo` with host weighting inferred | 71.9 (+9.1/−7.5) (median) | arXiv:2609.04991 |
| GWTC-4.0 (137 dark sirens) | non-parametric `H(z)` | `H(0.44)` = 92.3 (+29.9/−36.6) | arXiv:2511.11795 |
| GWTC-4.0 (142) + TDCOSMO-2025 | distance sum rule | 83.78 (+12.53/−10.23); 75.42 (+3.74/−4.66) with the H0LiCOW lens treatment | arXiv:2606.03634 |

How to read the tight rows.

- Every value near ±4 comes from GW170817 with a jet prior; the dark sirens add about
  11% (arXiv:2603.20195) [src].
- The ±4.0 of the normalising-flow analysis is conditional on the astrophysical
  prescriptions of the training catalogues; the same paper shows H0 degenerate with the
  fraction of dynamically formed binaries (about 35% for a Planck cosmology, about 25%
  for SH0ES) (arXiv:2603.15332) [src].
- Dark-siren-only values without a bright siren have half-widths of about 12 to 23
  [der: mean of the upper and lower errors of the rows above].

### 2.3 Modified gravitational-wave propagation
<!-- key: modified-gravitational-wave-propagation -->

| Data | `Xi_0` (1 in general relativity) | Reference |
|---|---|---|
| GWTC-2 dark sirens + GLADE | 2.1 (+3.2/−1.2) | arXiv:2101.12660 |
| GWTC-2, if ZTF19abanrhr is the GW190521 counterpart | 1.8 (+0.9/−0.6) | arXiv:2101.12660 |
| GWTC-3 spectral | 1.2 ± 0.7 (flat prior); 1.0 (+0.4/−0.8) (prior uniform in log) | arXiv:2112.05728 |
| GWTC-4.0 | 1.4 (+1.0/−0.4); 90%: (+2.8/−0.6) | arXiv:2509.04348 |
| GWTC-5.0, spectral, FullPop-4.0 | 1.1 (+0.6/−0.3) with H0 on U(10, 120); 1.0 (+0.3/−0.2) with H0 on U(65, 77); `c_M` = −0.4 (+1.6/−1.3) and −0.1 (+1.0/−0.8) [src: Sect. IV.2]; 35.7% and 50% tighter than GWTC-4.0 [src: Sect. V.1] | arXiv:2605.27227 |
| GWTC-4.0, as printed in the ar5iv rendering (earlier version) | 1.2 (+0.8/−0.4); 90%: (+2.4/−0.5) [src: abstract of that rendering] | arXiv:2509.04348 |

## 3. Siren × galaxy cross-correlation results
<!-- key: siren-x-galaxy-cross-correlation-results -->

| Data | Result | Reference |
|---|---|---|
| 8 well-localised GWTC-3 dark sirens × 2MPZ and WISE×SuperCOSMOS, + GW170817 | H0 = 75.4 (+11/−6) (median, equal-tailed), after marginalising Ω_m and the GW bias; "mostly driven by the bright siren", the dark-only posterior is uninformative | arXiv:2203.03643 |
| 2 GWTC-3 events × GLADE+ (Peak Sirens) | cross-correlation peak detected at 5.9σ, of which GW190814 alone gives 3.4σ | arXiv:2512.15380 |
| same, adding GW170817 without its redshift | H0 = 67 (+18/−15); `b_gw < 4.3` at 95% | arXiv:2512.15380 |

No cross-correlation analysis of GWTC-4.0 or GWTC-5.0 was found in the date-sorted
search of 2026-10-10.

## 4. Fast radio bursts: baryons and H0
<!-- key: fast-radio-bursts-baryons-and-h0 -->

### 4.1 Baryon census
<!-- key: baryon-census -->

| Quantity | Value | Sample | Reference | Flag |
|---|---|---|---|---|
| `Ω_b` | 0.051 (+0.021/−0.025) `h70⁻¹` (95%) | first arcsecond-localised sample | arXiv:2005.13161 | [src] |
| `Ω_b h70` | 0.051 ± 0.006 | DSA-110 and literature sample | arXiv:2409.16952 | [src] |
| `f_IGM` | 0.76 (+0.10/−0.11) | same | arXiv:2409.16952 | [src] |
| `f_igm` | 0.59 (+0.11/−0.10) | 8 FLIMFLAM sightlines with foreground spectroscopy | arXiv:2402.00505 | [src] |
| `f_gas` in haloes of `10^10`–`10^13 M☉` | 0.55 (+0.26/−0.29) | same | arXiv:2402.00505 | [src] |
| `f_IGM` | ≥ 0.69 (95%) | 61 localised, sightlines without intervening haloes | arXiv:2506.04186 | [src] |
| `f_d` (all diffuse gas) | > 0.9 for a constant model | 124 localised | arXiv:2506.03536 | [src] |
| mean rest-frame `DM_host` | 90 (+29/−19) pc cm⁻³ | FLIMFLAM | arXiv:2402.00505 | [src] |
| median `DM_host` | 186 (+59/−48) pc cm⁻³ (the abstract prints the unit as km/s/Mpc) | ASKAP + Parkes, H0 prior 67–74 | arXiv:2208.00819 | [src] |
| fluctuation parameter | `log10 F > −0.89` (3σ) | 78 bursts, 21 localised | arXiv:2305.07022 | [src] |

The three `f_IGM`-type numbers do not measure the same thing: Khrykin et al. separate
halo gas using foreground galaxy maps, Connor et al. partition by a population model,
and Liu et al. quote all diffuse gas. Macquart et al. state that their baryon density
is consistent with the CMB and nucleosynthesis values.

### 4.2 Feedback from DM cross-correlations
<!-- key: feedback-from-dm-cross-correlations -->

| Result | Reference |
|---|---|
| DM correlates with foreground galaxy density, `p = 1.76 × 10⁻⁵`; stacked excess DM out to megaparsec scales at about 3σ | arXiv:2506.04186 |
| DM × 2MASS galaxies with 133 localised bursts: null at `0.01 < R < 1 h⁻¹ Mpc`; hot-gas fraction in `10^12–13 M☉` haloes below about 10% of the cosmic baryon fraction; IllustrisTNG-300 too gas-rich | arXiv:2601.21336 |
| DM × DESI Legacy Bright Galaxy Sample with 130 localised bursts: 6.5σ detection; a no-feedback model disfavoured at about 9σ; agreement with kSZ profiles; first joint FRB + kSZ attempt at `fσ8` | arXiv:2608.11296 |
| M31 halo: excess DM of 5.9–59.6 pc cm⁻³ (inner) and 25.7–64.6 pc cm⁻³ (outer) from 171 sightlines against 684 controls, CHIME Catalog 2 | arXiv:2602.23749 |

All four are [src]. The first three use localised samples of similar size and reach
different detection levels on different scales and tracers; they agree on strong
feedback.

### 4.3 H0 from the dispersion measure–redshift relation
<!-- key: h0-from-the-dispersion-measure-redshift-relation -->

| H0 | Sample | Method | Reference | Flag |
|---|---|---|---|---|
| 62.3 ± 9.1 | 9 localised | `p(DM | z)` with scatter model | arXiv:2104.04538 | [src] |
| 64.67 (+5.62/−4.66) | 14 localised | scatter distributions from simulations (arXiv abstract) | arXiv:2108.00581 | [src] |
| 73 (+12/−8) | 16 localised + 60 unlocalised | survey forward model (`zDM`) | arXiv:2208.00819 | [src] |
| 85.3 (+9.4/−8.1) | 21 localised + 57 unlocalised | as above, with `F` free | arXiv:2305.07022 | [src] |
| 71.28 (+1.90/−2.08) | 95 of 117 localised | `p(DM | z)`, statistical error only | arXiv:2507.18946 | [src] |
| 69 (+17/−15) | 2124 unlocalised (CHIME Catalog 2) | DM distribution only | arXiv:2604.03769 | [src] |

Each needs an external baryon density (physics file, §7.2); the prior used is not in
every abstract. The values span 62 to 85 while the
smallest quoted error is 2 [der]: the scatter between analyses measures the modelling
systematics (host and halo DM, scatter model, selection), which Xu et al. 2025 list
themselves. No FRB H0 is at present a competitive or independent arbiter of the
tension.

## 5. Lensed transients and time delays (pointer)
<!-- key: lensed-transients-and-time-delays-pointer -->

| Object | H0 | Notes | Reference | Flag |
|---|---|---|---|---|
| SN Refsdal | 64.8 (+4.4/−4.3) | eight cluster models, blinded | arXiv:2305.06367 | [src] |
| SN Refsdal | 66.6 (+4.1/−3.3) | the two models most consistent with the observations | arXiv:2305.06367 | [src] |
| SN Refsdal, re-modelled | 66.0 ± 4.3 | four mass models, new MUSE and JWST redshifts | arXiv:2509.09979 | [src] |
| SN H0pe | 71.8 (+9.2/−8.1) | seven lens models, time delays only (arXiv abstract) | arXiv:2403.18902 | [src] |
| SN H0pe | 75.7 (+8.1/−5.5) | models weighted by the absolute magnifications (arXiv abstract) | arXiv:2403.18902 | [src] |
| SN Encore | 66.9 (+11.2/−8.1) | seven lens models, double-blind | arXiv:2509.12301 | [src] |
| SN 2025wny | 80.5 (+26.4/−16.7) | photometric delays only | arXiv:2608.28427 | [src] |
| SN 2025wny | 70.8 (+8.2/−6.1) | photometric + spectroscopic delays | arXiv:2608.28427 | [src] |
| TDCOSMO-2025 (8 lensed quasars) | 71.6 (+3.9/−3.3) | flat ΛCDM, Ω_m from Pantheon+, mass-sheet degeneracy free, blinded | arXiv:2506.03023 | [src] |

The TDCOSMO value agrees with the one in `cosmo-distance-ladder-h0`, where the history
of lensed-quasar results is kept. All lensed-supernova values assume flat ΛCDM with
fixed or weakly varied matter density (not stated in every abstract; check the paper).
The four supernovae are mutually consistent within their errors [der: comparison of the
rows].

## 6. History of the key numbers
<!-- key: history-of-the-key-numbers -->

### 6.1 LVK H0 with sirens
<!-- key: lvk-h0-with-sirens -->

| Year | Value | Status |
|---|---|---|
| 2017 | 70.0 (+12.0/−8.0), GW170817 alone | superseded as "the siren H0"; still the reference single-event posterior |
| 2019 | 68.7 (+17.0/−7.8), O1–O2 | superseded; different prior and interval |
| 2021 | 68 (+12/−7) spectral, 68 (+8/−6) catalogue with fixed population, GWTC-3 | the 68 (+8/−6) is not robust: fixed population |
| 2023 | 69 (+12/−7), GWTC-3 with joint population (`gwcosmo`) | supersedes the fixed-population GWTC-3 value |
| 2025 | 75.4 (+12.8/−9.1), GWTC-4.0 | superseded |
| 2026 | 71.7 (+9.4/−7.5), GWTC-5.0 | current |

The central value has moved by less than 1σ between releases while the method changed
each time (prior, statistic, population treatment, catalogue). The precision has gone
from 14% to 12% in nine years [der, §2.1], against a 2017 **forecast** of about 2%
within five years (arXiv:1712.06531) that assumed a steady supply of binary neutron
stars with counterparts.

### 6.2 GW170817 with electromagnetic inclination
<!-- key: gw170817-with-electromagnetic-inclination -->

68.9 (2018, arXiv:1806.10596) → 68.3 with BORG velocities (2019, arXiv:1909.08627) →
64.8 with model-averaged velocities (2019, arXiv:1909.00587) → 66.2 with kilonova and
equation of state (2020, arXiv:2002.11355) → 75.46 with the late afterglow (2023,
arXiv:2305.19914) → 65.5 with all VLBI data (2026, arXiv:2605.11437). None supersedes
the others; they are alternative jet and velocity models.

### 6.3 FRB baryon density
<!-- key: frb-baryon-density -->

`Ω_b h70 = 0.051` with a 95% interval of +0.021/−0.025 (2020) → 0.051 ± 0.006 at 68%
(2024) [src; arXiv:2005.13161, arXiv:2409.16952]. The central value did not move; for a
Gaussian the 1σ error roughly halved [der: 0.023/2 ≈ 0.012 against 0.006].

### 6.4 Agreement with sibling skills
<!-- key: agreement-with-sibling-skills -->

- `cosmo-distance-ladder-h0`: TDCOSMO-2025 71.6 (+3.9/−3.3) — same value read here.
- `cosmo-surveys-facilities`: O4 ended 18 November 2025 — confirmed by the LVK
  announcement; "GWTC-5.0 has 267 mergers" — 267 is the population-analysis sample, the
  catalogue holds 390 candidates (surveys file, §1.2); "O5 has no date" — confirmed, with
  the addition that a six-month run IR1 is planned from November 2026.

## Not verified
<!-- key: not-verified -->

- Closed on 2026-10-12: the GWTC-5.0 spectral-only, catalogue-only and bright-only H0
  values and its `Xi_0` constraint are now in §2.1 and §2.3. Still open: which version
  of arXiv:2509.04348 the journal printed.
- Whether the arXiv abstracts of arXiv:2509.04348, arXiv:2111.03604, arXiv:1806.10596,
  arXiv:2108.00581 and arXiv:2403.18902 carry the same numbers as their journal
  versions. Values different from those above circulate for each of these papers;
  quote the version you cite.
- The matter-density prior of each lensed-supernova analysis. Read on 2026-10-13 for
  SN Refsdal only: delays predicted at H0 = 70 and Ω_M = 0.3 and rescaled, with an
  effect of varying Ω_M of at most about 0.7 (arXiv:2305.06367) [src: Supplementary].
- The Ω_m and `w0` constraints from sirens beyond those in the GW190521 rows.
- H0 values from SN Zwicky or iPTF16geu, if any exist.
