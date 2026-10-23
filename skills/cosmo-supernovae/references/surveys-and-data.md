# Type Ia supernova cosmology — surveys, samples and data releases

Scope: every SN survey, compilation and data release that matters for the
Hubble diagram, in the order past, current, planned; plus the non-Ia and
lensed cross-check samples.
Snapshot: 2026-10-13

Flags: `[src]` read in the cited paper this session; `[sec]` from a named
secondary source; `[der]` derived here. Forecast rows say **forecast**.

## 1. How a cosmology sample is assembled
<!-- key: how-a-cosmology-sample-is-assembled -->

No single survey spans the redshift range. A "sample" is a high-redshift rolling
survey plus a low-redshift **anchor** (z < 0.1) from other telescopes, put on a
common photometric system (see `physics-and-methods.md` Section 9). Three
facts follow and recur throughout the literature:

1. The compilations share most of their supernovae. Pantheon+ and Union3 have
   1363 objects in common out of 1550 and 2087 `[src]` (DESI Collaboration
   2025, arXiv:2503.14738). The DES-SN5YR low-z anchor (194 SNe) is entirely
   contained in Pantheon+ `[src]` (Camilleri et al. 2026, arXiv:2609.05053).
   The three "independent" SN likelihoods used with DESI are therefore not
   independent at low redshift.
2. The anchor is the weakest part: heterogeneous instruments, targeted
   (galaxy-pre-selected) discovery in the older sets, and calibration that
   was not designed for cosmology. Pantheon already identified "modeling the
   low-redshift sample" as the main limitation (Scolnic et al. 2018,
   arXiv:1710.00845).
3. Removing z < 0.1 from Unite (687 events, 24 % of the sample) is the only
   redshift cut that moves the cosmology by ~2 sigma `[src: Sect. 9.1]`
   (arXiv:2609.05053).

## 2. Past surveys
<!-- key: past-surveys -->

| Survey | Instrument / strategy | Sample and redshift | Notes | Reference |
|---|---|---|---|---|
| High-Z Supernova Search Team | Multi-telescope search and follow-up | 16 high-z (10 new at 0.16 < z < 0.62) + 34 nearby `[src: abstract]` | Discovery of acceleration | Riess et al. 1998, arXiv:astro-ph/9805201 |
| Supernova Cosmology Project | Multi-telescope; low-z from Calán/Tololo | 42 SNe at 0.18 < z < 0.83 `[src: abstract]` | Discovery of acceleration | Perlmutter et al. 1999, arXiv:astro-ph/9812133 |
| SNLS | CFHT MegaCam, four 1 deg² fields, 4 bands (as described for the SNLS samples) | 3-year joint sample: 472 SNe = 123 low-z + 93 SDSS + 242 SNLS + 14 HST `[src: abstract]` | Introduced the systematics covariance matrix; calibration-dominated | Conley et al. 2011, arXiv:1104.1443 |
| SDSS-II SN + SNLS (JLA) | SDSS 2.5 m (0.05 < z < 0.4) + SNLS (0.2 < z < 1) + low-z | 740 SNe, 613 of them from SDSS-II and SNLS `[src: Sects. 2, 3.1]` | Joint recalibration, SALT2 retrained | Betoule et al. 2014, arXiv:1401.4064 |
| Pan-STARRS1 Medium Deep | PS1 1.8 m, griz | 365 spectroscopically confirmed; 279 used at 0.03 < z < 0.68 `[src]` | Core of Pantheon | arXiv:1710.00845 |
| Foundation | PS1, griz, untargeted follow-up of z < 0.1 SNe | DR1: 225 SNe, 180 pass cosmology cuts; intrinsic scatter 0.111 mag `[src: abstract]` | First low-z sample on a well-calibrated survey system | Foley et al. 2018, arXiv:1711.02474 |
| CfA3, CfA4, CSP-I | Dedicated low-z follow-up of mostly targeted discoveries | Together with Foundation: 194 SNe at 0.025 < z < 0.1 in the DES-SN5YR anchor `[src: Sect. 2.1]` | The "historical low-z" set | as listed in arXiv:2609.05053 |
| DES-SN | DECam on the Blanco 4 m; ten ~3 deg² fields, griz; 8 shallow fields to r ~ 23.5 per visit and 2 deep fields to 24.5; 5 seasons `[src]` | > 20 000 candidates; 7000 host redshifts (OzDES); 1635 photometric SNe Ia at 0.10 < z < 1.13 `[src]` | Largest single-survey high-z sample | Vincenzi et al. 2024, arXiv:2401.02945 |

## 3. Compilations and their status
<!-- key: compilations-and-their-status -->

| Compilation | Year | Content | Method | Status on 2026-10-07 | Reference |
|---|---|---|---|---|---|
| Union and its 2012 extension | 2008, 2012 | 414 SNe reduced to 307 by cuts `[src]`; the 2012 analysis adds 14 HST cluster SNe, ten beyond z = 1 `[src]` | One blind procedure for heterogeneous subsamples, with outlier rejection | Superseded; ancestors of Union3 | Kowalski et al. 2008, arXiv:0804.4142; Suzuki et al. 2012, arXiv:1105.3470 |
| JLA | 2014 | 740 SNe, SDSS-II + SNLS3 + low-z + HST | SALT2, binned-smoothed covariance | Superseded | arXiv:1401.4064 |
| Pantheon | 2018 | 1048 SNe, 0.01 < z < 2.3 `[src: abstract]` | SALT2 + BBC, Supercal | Superseded by Pantheon+ | arXiv:1710.00845 |
| DES-SN3YR | 2019 | 207 DES (spectroscopic) + 122 low-z = 329 `[src: abstract]` | SALT2 + BBC | Superseded | Abbott et al. (DES) 2019, arXiv:1811.02374 |
| Pantheon+ | 2022 | 1701 light curves of 1550 SNe from 18 surveys, 0.001 < z < 2.26 `[src]`; includes the SH0ES calibrators | SALT2 (retrained), BBC, Fragilistic, unbinned covariance | Still the standard for distance-ladder `H0`; its host masses and calibration are updated in Unite | Scolnic et al. 2022, arXiv:2112.03863; Brout et al. 2022, arXiv:2202.04077 |
| Union3 | 2023 | 2087 SNe from 24 datasets `[src]` | SALT3 + UNITY1.5 | Superseded by Union3.1 | Rubin et al. 2023, arXiv:2311.12098 |
| DES-SN5YR (= DESY5) | 2024 | 1635 DES photometric (0.10 < z < 1.13) + 194 low-z (0.025 < z < 0.10), "for a total of 1829 SNe" (Sect. 2.1) `[src]` | SALT3 + BBC, SuperNNova, BEAMS | Superseded by DES-Dovekie | DES Collaboration 2024, arXiv:2401.02929 |
| DES-Dovekie | 2025 | 1623 DES + 197 low-z = 1820 `[src: Sect. 8.2, Table 5]`; effective N = 1684 `[src]` | Dovekie calibration, SALT3.DOV, corrected colour-law implementation | Current DES SN sample | Popovic et al. 2025, arXiv:2511.07517 |
| Union3.1 | 2026 | ~2000 SNe of Union3 with host properties remeasured from DESI Legacy Imaging Surveys photometry with Prospector `[src]` | UNITY1.7 `[src: arXiv:2601.19424 Sect. VI]`; two-population variant UNITY1.8 | Current Union sample | Hoyt et al. 2026, arXiv:2601.19424; Rubin et al. 2026, arXiv:2601.19854 |
| Unite | 2026 | 2884 likely SNe Ia: Pantheon+ plus DES, Dovekie calibration, host masses remeasured for > 98 % `[src]` | SALT3 + BBC; delensing term by default | Newest and largest; arXiv v2 of September 2026, journal status not checked | arXiv:2609.05053; Lee et al. 2026, arXiv:2609.05321 |

Details worth remembering:

- **Pantheon+ vs DES overlap.** Pantheon+ contains the DES-SN3YR
  spectroscopic sample (203 SNe); 145 of these are also in DES-SN5YR. Unite
  keeps the 145 DES-SN5YR versions because the two samples have different
  selection functions `[src: Sect. 2.3]` (arXiv:2609.05053).
- **Common objects across analyses.** Unite and DES-Dovekie share 1555 SNe
  (182 at z < 0.1); Unite and Pantheon+ share 1375 (642 at z < 0.1) `[src]`
  (arXiv:2609.05053).
- **What changed in DES-Dovekie** (arXiv:2511.07517, Section 5): (i) the
  Fitzpatrick 1999 colour law in SNANA had been a polynomial expansion around
  `R_V = 3.1`; replacing it by the full law changes simulated bias
  corrections at the ~0.01 mag level; (ii) Dovekie cross-calibration instead
  of Fragilistic, with zero points that "notably differ for DES"; (iii)
  retrained SALT3; (iv) regenerated bias-correction simulations; (v) a
  weighting error (0.3 instead of 1/sqrt(9) = 0.33 on nine calibration
  variants) that had made DES-SN5YR underestimate its photometric systematic
  by ~20 %; (vi) the `sigma_x1` cut moved from 1.0 to 1.15 `[src]`.
- **What changed in Union3.1** (arXiv:2601.19424): host masses of z < 0.1 SNe
  in Union3 had been overestimated on average, and those of z < 0.15 SNe in
  Pantheon+ underestimated; after correction the two compilations' mean
  low-redshift distance moduli agree to 0.01 mag instead of differing by
  > 0.03 mag `[src]`.

## 4. Current surveys and releases
<!-- key: current-surveys-and-releases -->

| Survey | Instrument / strategy | Release and size | Cosmology status | Reference |
|---|---|---|---|---|
| ZTF SN Ia DR2 | Palomar 48-inch, 47 deg² field, g r i, untargeted; SEDm classification | 3628 spectroscopically classified SNe Ia at z < 0.3, discovered March 2018 – December 2020; 2667 pass light-curve cuts; volume-limited subsample of nearly 1000 at z < 0.06; 5138 spectra; Hubble scatter 0.15 mag `[src]` | **Not usable for cosmological parameters.** The overview states the photometric accuracy "is not yet suited for cosmological parameter inference, which will follow as DR2.5" | Rigault et al. 2024, arXiv:2409.04346 |
| ZTF scene-modelling reprocessing | Scene-modelling photometry | Stellar repeatability better than 1 %; a flux-dependent PSF distortion ("pocket effect") gives non-linearities of a few percent and affects all ZTF light-curve releases; SMP vs forced photometry: colour shift 10 mmag, absolute calibration shift 90 mmag `[src]` | Reprocessing "in progress" in September 2025. No DR2.5 release paper was found by arXiv and INSPIRE title and abstract searches on 2026-10-07 | Lacroix et al. 2025, arXiv:2509.04073 |
| DEBASS | DECam imaging of low-z SNe, WiFeS host spectroscopy; same instrument as DES | > 400 spectroscopically confirmed SNe Ia at 0.01 < z < 0.08 (2021 to mid-2025); early release of 77 SNe in the DES footprint; MAD of residuals ~0.10 mag before bias corrections `[src]` | Preliminary; intended to replace the historical DES anchor | Sherman et al. 2025, arXiv:2508.10878; Acevedo et al. 2025, arXiv:2508.10877 |
| TITAN (ATLAS) | Four ATLAS telescopes, all sky | > 10 000 spectroscopically confirmed SNe Ia observed by ATLAS, "thousands" cosmology-grade; calibration paper finds initial offsets ~40 mmag vs DES Y6 stars, reduced to an estimated 5–10 mmag systematic `[src]` | Calibration and host papers out; no Hubble-diagram cosmology found in this session's searches | Marlin et al. 2025, arXiv:2512.21903; Murakami et al. 2026, arXiv:2604.16597 |
| Young Supernova Experiment | PS1 griz + ZTF gr | DR1: 1975 transients observed from 24 November 2019 to 20 December 2021, redshifts to ~0.5; a photometric classifier labels 1048 of 1483 unclassified events as SNe Ia `[src]`. Named by the Unite authors among the low-z samples "expected to produce new low-z results in the near future" `[sec, arXiv:2609.05053]` | No cosmology sample found | Aleo et al. 2023, arXiv:2211.07128 |
| JWST high-z SNe Ia | NIRCam / NIRSpec | Spectroscopically confirmed SNe Ia at z > 2: SN 2023adsy and SN 2023aeax (z = 2.15); the latter's distance agrees with LCDM at ~0.1 sigma; "no definitive evolution" `[src: abstract]` | Evolution test, not a cosmology sample | Pierel et al. 2024, arXiv:2411.11953 |

Roles of the new anchors:

- DEBASS vs Foundation: median distance offset `0.016 ± 0.019 mag`; a
  different calibration solution moves it by `-0.015 ± 0.019 mag`; tertiary
  stars of DEBASS, DES and PS1 agree at the 10 mmag level `[src: abstract]`
  (arXiv:2508.10877). **Forecast** (same paper): replacing the historical
  anchor by > 400 DEBASS SNe improves the statistical errors on `w0` and
  `w_a` by 30 % and 24 %, raises the FoM by up to 60 %, and allows an
  `f sigma8` measurement at the 25 % level.
- Foundation vs older low-z: Foundation Hubble residuals are fainter than the
  pre-existing low-z residuals by `0.046 ± 0.027 mag` (stat+sys) `[src]`
  (Jones et al. 2019, arXiv:1811.09286). This 2019 number is the historical
  precedent of the 2024–2025 "low-z offset" debate.

## 5. Planned and starting facilities
<!-- key: planned-and-starting-facilities -->

| Facility | Status | SN programme | Numbers | Source |
|---|---|---|---|---|
| Rubin LSST | 10-year survey began 30 June 2026 `[sec, Rubin/SLAC and CMU announcements found by web search]` | Wide-Fast-Deep plus Deep Drilling Fields; fully photometric analysis with host photo-z | **Forecast**: a simulated DDF sample of ~6000 events with a spectroscopic low-z WFD sample gives FoM ~150, against 54 quoted for DES-SN5YR; small but significant biases remain in the pipeline `[src: abstract]` | Mitra et al. 2025, arXiv:2512.06319 |
| Rubin + DESI follow-up | Proposal | DESI tiles re-prioritised on Rubin alerts, starting 2027 | **Forecast**: 7500 near-peak spectra in one year; a volume-limited subset of 2300 SNe Ia at z < 0.3 added to current data pushes the tension with LCDM beyond 5 sigma *if current best-fit values persist* `[src: Sect. IV.2.5]` | Truong et al. 2026, arXiv:2604.18859 |
| Roman | Launched 30 August 2026; in commissioning `[sec, NASA mission page read 2026-10-07]` | High-Latitude Time-Domain Survey (HLTDS): wide imaging 18.3 deg² and deep imaging 6.5 deg², northern and southern fields, core component ~2 years with filter subsets every 5 days, ~6 months of observing time in total `[sec, NASA HLTDS page]` | **Forecast**: 10 000 Roman SNe Ia after cuts, combined with 4400 from LSST, give a FoM "well above" the mission requirement of 326, with SALT-training systematics not included `[src]` | Kessler et al. 2025, arXiv:2506.04402 |
| Roman (earlier reference design) | Superseded by the HLTDS definition | Two tiers, ~19 deg² (z up to 1) and ~5 deg² (z up to 1.7) | **Forecast**: ~12 000 SNe Ia, ~5000 at z > 1 `[src]` | Rose et al. 2021, arXiv:2111.03081 |

Stage-IV calibration requirement (**forecast**, Anumba et al. 2026,
arXiv:2604.19746): zero-point shifts of 5 mmag and filter-wavelength shifts
of 5 Å reduce the FoM by ~50 % when propagated through light-curve fitting
and by ~13 % when applied only in model training; the fitting-stage effect is
smooth in redshift, nearly degenerate with cosmology, and cannot be
self-calibrated `[src]`.

## 6. Public data locations
<!-- key: public-data-locations -->

| Product | Location | Stated in |
|---|---|---|
| Pantheon+ distances, covariance, bias-correction simulations | `pantheonplussh0es.github.io` | arXiv:2202.04077 |
| DES-SN5YR light curves, Hubble diagram, ancillary data | <https://github.com/des-science/DES-SN5YR>; 31 636 difference-imaging and 19 706 scene-modelling light curves `[src]` | Sánchez et al. 2024, arXiv:2406.05046 |
| Dovekie cross-calibration | <https://github.com/bap37/Dovekie/> | arXiv:2506.05471 |
| Union3 distances, light-curve fits, UNITY1.5 | "released to the community" | arXiv:2311.12098 |
| Unite | Public likelihood code, in anchored and unanchored forms | arXiv:2609.05053 |
| ZTF SN Ia DR2 | Light curves, spectra, host properties, Python access tool | arXiv:2409.04346 |
| SALT3 training code and data | <https://saltshaker.readthedocs.io> | arXiv:2104.07795 |

DESI ships the Pantheon+, Union3 and DESY5 likelihoods inside its inference
framework and reports all three rather than choosing (arXiv:2503.14738).
Anyone repeating that exercise after 2025 should use DES-Dovekie, Union3.1
and either the corrected Pantheon+ or Unite.

## 7. Cross-check samples (not SN Ia light-curve standardisation)
<!-- key: cross-check-samples-not-sn-ia-light-curve -->

### 7.1 Type II supernovae
<!-- key: type-ii-supernovae -->

| Method | Sample | Result (model) | Reference |
|---|---|---|---|
| Standardised candle method, Cepheid/TRGB/geometric calibrators | 13 calibrator SNe II | `H0 = 75.4 (+3.8/-3.7) km/s/Mpc`, statistical only; systematic estimate 1.5 `[src]` | de Jaeger et al. 2022, arXiv:2203.08974 |
| Tailored expanding photosphere method (radiative-transfer emulator), no distance ladder | 10 SNe II at 0.01 < z < 0.04, literature data | `H0 = 74.9 ± 1.9 km/s/Mpc` (stat) `[src: abstract]` | Vogl et al. 2024, arXiv:2411.04968 |
| Hierarchical Bayesian SCM with an H-alpha term, SNfactory spectrophotometry | Hubble-flow SNe II-P | Scatter reduced from 0.28 to 0.18 mag; `H0 = 70.6 (+4.5/-4.3) km/s/Mpc` (stat only) `[src: abstract]` | Holas et al. 2026, arXiv:2609.39804 |

The standardised candle method goes back to Hamuy & Pinto 2002
(arXiv:astro-ph/0201279): plateau luminosity correlates with ejecta
velocity, which cuts the Hubble-diagram scatter from ~1 mag to 0.4 (V) and
0.3 (I) mag, and to 0.2 mag for eight objects in the Hubble flow `[src]`.
The expanding photosphere method, which needs no calibrator, goes back to
Kirshner & Kwan 1974 (doi:10.1086/153123), who assumed blackbody emission
for two SNe; dilution factors from non-LTE models came later
`[sec, arXiv:2411.04968 Sect. 1]`.
These are `H0` cross-checks that replace SNe Ia in the ladder or bypass it;
the interpretation belongs to `cosmo-distance-ladder-h0`.

### 7.2 Strongly lensed supernovae
<!-- key: strongly-lensed-supernovae -->

| Object | Type, redshift | H0 (km/s/Mpc) | Reference |
|---|---|---|---|
| SN Refsdal | Cluster-lensed core-collapse SN | `64.8 (+4.4/-4.3)` from eight lens models; `66.6 (+4.1/-3.3)` from the two best `[src]` | Kelly et al. 2023, arXiv:2305.06367 |
| SN H0pe | SN Ia, z = 1.78, cluster lens, JWST | `75.7 (+8.1/-5.5)` using the SN Ia magnification to weight lens models; `71.8 (+9.2/-8.1)` without `[src: abstract]` | Pascale et al. 2024, arXiv:2403.18902 |
| SN Encore | SN Ia, z = 1.95, cluster lens, JWST | `66.9 (+11.2/-8.1)` `[src: abstract]`; a second lensed SN ("Requiem") in the same host has a further image expected within a few years | Pierel et al. 2025, arXiv:2509.12301 |
| SN 2025wny | Superluminous SN-I, z = 2.015, galaxy-scale lens | `66.7 (+7.6/-6.3)` for isothermal profiles; `70.8 (+8.2/-6.1)` with free density slopes `[src: abstract]` | Mörtsell et al. 2026, arXiv:2608.28430 |

Discovery papers: four images of one supernova around a z = 0.54 galaxy of
the cluster MACS J1149.6+2223, host at z = 1.49, a later appearance
elsewhere in the cluster predicted (Kelly et al. 2015,
arXiv:1411.6009, which credits the idea to Refsdal 1964,
doi:10.1093/mnras/128.4.307 `[sec]`); iPTF16geu, a multiply imaged SN Ia
at z = 0.409, four images, magnified more than fifty times by a galaxy
(Goobar et al. 2017, arXiv:1611.00014) `[src]`.
Review: Suyu et al. 2024 (arXiv:2301.07729). All four values assume flat
LCDM-like distance ratios and are dominated by lens-model uncertainty; none
discriminates between 67 and 73. Detail in `cosmo-distance-ladder-h0` and
`cosmo-multimessenger`.

### 7.3 Siblings
<!-- key: siblings -->

Two or more SNe Ia in one host test standardisation without a cosmological
model. Burns et al. 2020 (arXiv:2004.13069), from 12 galaxies hosting two or
more SNe Ia, find distances consistent to 3 % once observational errors are
accounted for `[src]`. One ZTF pair 0.6 kpc apart, differing by 2 mag at
peak, gives `beta = 3.5 ± 0.3` independently of cosmology and of selection
`[src]` (Biswas et al. 2021, arXiv:2103.16978). DES: 8 galaxies with two likely SNe Ia; apart from stretch, siblings
agree no better than random pairs, and at 2.8 sigma at least half of the
intrinsic scatter does not come from shared host properties `[src]` (Scolnic
et al. 2020, arXiv:2002.00974). ZTF DR2: 25 pairs give `alpha = 0.218 ±
0.055`, `beta = 3.084 ± 0.312` allowing diversity, a sibling intrinsic scatter
`<= 0.10 mag` (95 %) against `0.22 ± 0.04` from Hubble residuals of the same
objects, and an `alpha` higher than the cosmological-sample value by 2.5–3.5
sigma, driven by low-stretch pairs `[src]` (Dhawan et al. 2024,
arXiv:2406.01434). The two results pull in different directions on how much
scatter is host-driven; the samples are small.

## Not verified
<!-- key: not-verified -->

- The SNLS five-year cosmology sample: no publication was searched for or
  found in this session.
- Rubin: the survey start date and Data Preview contents come from
  announcements and a Rubin technical note located by web search, not from a
  refereed paper; no Rubin SN Ia cosmology or SN data-release paper was found.
- ZTF "DR2.5": collaboration slides located by web search describe ~3800 SNe
  with scene-modelling light curves and an earlier target date; they are not
  a release and are not used above.
- YSE and TITAN cosmology-sample sizes; the CfA3, CfA4 and CSP data papers
  were not re-read for individual counts.
- Roman HLTDS expected SN counts by redshift: only the simulation papers
  above were read.
