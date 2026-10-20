# Surveys and data — peculiar-velocity samples, release by release

Scope: the samples and releases behind every result in this skill, with the counts actually used by
the analyses, where the data are public, the status on the snapshot date, and what comes next.
Snapshot: 2026-10-07

The survey descriptions of the 2026-08 compilation (why three indicators, what each survey is, the
Cosmicflows-4 composition, the SN samples, the planned surveys) are folded into §0, §1, §4, §5 and §6;
the rest of the file gives release-level numbers read this session, the 2025–2026 releases and the
status of each programme.

Flags as in `results.md`.

---

## 0. Distance indicators: why three, and what each delivers
<!-- key: distance-indicators-why-three-and-what-each -->

Folded on 2026-10-20 from the compilation of 2026-08-12/14, in which `[src]` meant "traced to the
paper" and `[der]` "relabelled or derived, the paper does not quote fσ8".
Source of the descriptions in §0–1 and §6: the review of Turner 2024 (arXiv:2411.19484), §3, §4, §6.

A peculiar velocity needs a **redshift-independent distance**. Only three methods deliver them in
bulk over cosmological volumes.

| Indicator | Tracer | Distance error per object | Practical reach |
|---|---|---|---|
| **Tully–Fisher (TF)** | spirals; luminosity–HI linewidth | ~20 % | z ≲ 0.1 |
| **Fundamental Plane (FP)** | early types; σ–R_e–I_e | ~20 % | z ≲ 0.1 |
| **SN Ia** | standardisable candle | ~5–7 % (σ ≈ 0.1–0.15 mag) | z ≲ 0.3 |

- **The controlling fact** (Turner §3): the TF/FP scatter is a constant in *magnitude*, so the
  distance error is a constant *fraction* of the distance and the velocity error grows linearly with
  distance. Scaling-relation surveys therefore stop at z ~ 0.1–0.15 however many galaxies they
  observe, and **SNe Ia are the only reliable probe of the velocity field beyond z ≈ 0.15**.
- TF/FP win on *number* (10⁴–10⁵ objects at ~20 % each), SNe on *per-object precision* and reach:
  not competing strategies, but different parts of the same volume.
- Other indicators (TRGB, SBF, masers, JAGB, Cepheids, GW sirens) are calibration rungs, not
  survey-scale velocity tracers.

---

## 1. Past surveys — numbers as their own papers give them
<!-- key: past-surveys-numbers-as-their-own-papers-give -->

| Survey | Indicator | Sample | Sky / depth | Distance error | Reference | Flag |
|---|---|---|---|---|---|---|
| 6dFGSv | FP | 8 885 galaxies | southern hemisphere, \|b\| > 10°, z < 0.055 | 0.11 dex in log-distance, "26 % in linear distance" | Springob et al. 2014, arXiv:1409.6161; Scrimgeour et al. 2016, arXiv:1511.06930 | [src] |
| 2MTF | TF (HI + 2MASS J, H, K) | 2 018 spirals | all sky except \|b\| < 5°, within 100 h⁻¹Mpc | σ_v = 0.177 H0 d (fit of arXiv:1804.05520) | Hong et al. 2014, arXiv:1409.0287 | [src] |
| SDSS PV | FP | 34 059 early types | 7 016 deg², z ≤ 0.1 | mean 23 % | Howlett et al. 2022, arXiv:2201.03112 | [src] |
| Cosmicflows-4 | 8 methods | 55 877 galaxies in 38 065 groups | both hemispheres, anisotropic depth | — | Tully et al. 2023, arXiv:2209.11238 | [src] |
| Mark III | TF + FP | ~3 200 | z̄ ~ 0.015 | — | Willick et al.; first uniform re-treatment of 1980s data | |
| SFI++ | TF (I band) | ~5 000 | most of the sky above the Galactic plane, z̃ ~ 0.02 | — | Springob et al. 2007; **erratum 2009** (morphological-type correction misapplied) | |

Folded on 2026-10-20 from the compilation of 2026-08-12/14, in which `[src]` meant "traced to the
paper" and `[der]` "relabelled or derived, the paper does not quote fσ8". The last two rows come from it (chronological in Turner §4: Mark III, SFI++, 6dFGSv, 2MTF,
SDSS PV, CF4). It gives the other four as: 6dFGSv ~9 000 FP (7 030 used in some analyses), z <
0.055, southern, |b| > 10°, Springob et al. 2014 and Magoulas et al. 2012; 2MTF ~2 000, z ≲ 0.03
(z̃ ~ 0.016), near-all-sky |b| > 5°, 2MASS + ALFALFA HI, "Hong et al. 2019"; SDSS PV > 34 000,
z < 0.1, z_eff ~ 0.07, northern; CF4 "Tully et al. 2022", "local". The rows above, read in the
papers, differ in the 2MTF reference year (Hong et al. 2014) and the CF4 year (2023).

Notes.

- **2MTF's selling point is the Galactic plane.** Optical surveys cut at |b| > 10°; 2MTF uses the
  infrared and reaches |b| > 5°, recovering structure in the Zone of Avoidance that otherwise biases
  reconstructions.
- **6dFGSv and SDSS PV are complementary by construction**: south against north, similar N within
  the 6dFGS redshift limit, but SDSS extends to z = 0.1.
- **CF4 is a compilation, not a survey**: ~35 000 FP (mostly 6dFGSv + SDSS PV) and ~10 000 TF
  (SFI++, 2MTF and others), plus SNe Ia, SNe II and SBF, from different groups with different
  calibrations — which is why bulk flows derived from it are estimator- and calibration-sensitive.
  It largely *contains* 6dFGSv, SDSS PV, SFI++ and 2MTF and is not independent of them. (The CF4
  paper's own merging counts, 42 254 FP and 12 395 TF galaxies, are in `systematics.md` §9b.)

- 6dFGSv velocities are delivered as **probability distributions** at the redshift-space position of
  each galaxy, from a Bayesian FP fit [src: arXiv:1409.6161]. The mean of η corresponds to the
  median of v [src: arXiv:1804.05520, §3, citing Scrimgeour et al.].
- SDSS PV ships 2 048 mocks with the survey selection and a group-richness correction; its
  zero-point is tied to Cosmicflows-3 [src: arXiv:2201.03112]. It is the sample behind three rows of
  the fσ8 table of `results.md` §0.
- Cosmicflows-4 absolute scale: Cepheids, TRGB and the NGC 4258 maser; the assembly "is compatible
  with" H0 = 74.6 ± 0.8 (stat), "large potential systematic error of ~3 km/s/Mpc" [src:
  arXiv:2209.11238].

---

## 2. Cosmicflows-4++ and its derivatives (2025–2026)
<!-- key: cosmicflows-4-and-its-derivatives-2025-2026 -->

| Release | Content | Reference | Flag |
|---|---|---|---|
| CF4++ | CF4 plus first-release velocities from WALLABY (655), FAST (4 796) and DESI (4 191); catalogue and reconstructed density and velocity fields **publicly released** | Courtois et al. 2025, arXiv:2502.01308 | [src] |
| CF4++ as used for clustering | 65 331 galaxy distances, out to z = 0.1 | Franco, Courtois & Bernui 2026, arXiv:2605.00450 | [src] |
| CF4++ZOA | 65 518 CF4++ distances + 8 283 new redshifts at \|b\| ≤ 10° (2 176 from MeerKAT HI, covering the innermost 3°-wide strip of the southern Zone of Avoidance) | Hollinger et al. 2026, arXiv:2603.09339 | [src] |

The two CF4++ counts (65 331 and 65 518) are both as printed in the cited abstracts; the difference
is not explained there. CF4++ is still a compilation: every caution of §1 about CF4
applies, and its DESI component is an early subset (4 191 objects), not the DR1 catalogue.

Results obtained from it in the same period: bulk flow of 315 ± 40 km/s at 150 h⁻¹Mpc and "the
dynamical scale of homogeneity is not yet reached in the interval [200–300] Mpc/h"
(arXiv:2502.01308) [src]; the Vela mass (`results.md` §2).

---

## 3. DESI Peculiar Velocity Survey
<!-- key: desi-peculiar-velocity-survey -->

A secondary-target programme of DESI, FP and TF with one instrument and one photometric system
(Legacy Surveys DR9).

| Stage | Date | Content | Reference | Flag |
|---|---|---|---|---|
| Target selection | 2023-02 | 373 533 early-type and 118 637 late-type targets in the 5-year footprint; predicted yield ~133 000 FP + ~53 000 TF velocities over 14 000 deg² | Saulder et al. 2023, arXiv:2302.13760 | [src] |
| Survey validation / EDR, FP | 2024-08 | 6 698 unique early types observed, 4 267 with velocity-dispersion error < 10 %; FP zero-point from the Coma SBF distance; H0 = 76.05 ± 0.35 (stat) ± 0.49 (syst FP), plus a third term of ± 4.86 that dominates | Said et al. 2025, arXiv:2408.13842 | [src] |
| EDR, TF | 2025-07 | rotation at 0.33 R26 for 1 163 spirals (1 136 + 27 dwarfs); slope −7.96 ± 0.13 AB mag from 41 Coma spirals, scatter 1.07 ± 0.02 mag; public distance catalogue | Douglass et al. 2025, arXiv:2507.11765 | [src] |
| DR1 FP catalogue | 2025-12 | 98 292 unique early types, z < 0.1, 26 % distances | Ross et al. 2025, arXiv:2512.03226 | [src] |
| DR1 TF catalogue | 2025-12 | 10 262 spirals, rotation at 0.4 R26; 6 807 in the clustering catalogue | Douglass et al. 2025, arXiv:2512.03227 | [src] |
| DR1 mocks | 2025-12 | 675 realisations with BGS density, FP, TF and SN Ia samples | Bautista et al. 2025, arXiv:2512.03228 | [src] |
| DR1 zero-point | 2025-12 | η_zp = 0.139 ± 0.007 from SH0ES/Pantheon+ SNe via groups | Carr et al. 2025, arXiv:2512.03232 | [src] |

**From catalogue to cosmology sample.** The counts shrink at each step, and the growth-rate papers
do not all quote the same one [src: arXiv:2512.03229 §2, arXiv:2512.03230 §2]:

| Step | FP | TF |
|---|---|---|
| Catalogue | 98 292 | 10 262 |
| Clustering sample, 0.01 < z < 0.1 | 73 822 | 6 806 |
| After removing TF at z > 0.05 | — | 2 934 |
| After the 4σ cut on η | 73 686 | 2 929 |
| Velocities in the fit | 76 615 (correlation functions) / 76 616 (field-level) | |

together with 415 523 BGS redshifts; z_eff = 0.07 is "the mean redshift of all galaxies across the
clustering and velocity samples" [src: arXiv:2512.03230]. Mean η uncertainty: 0.12 (FP), 0.11 (TF)
[src: arXiv:2512.03229]. "Over 90 %" of the velocities are FP [src: arXiv:2512.03229], so DR1 is, in
practice, an FP measurement.

**TF follow-up.** Siwakoti et al. 2026 (arXiv:2608.26459) test the single-fibre rotation measurement
against integral-field data for 215 galaxies: ~28 % have photometric–kinematic position-angle
misalignments > 10°; median distance bias ≈ +1.98 Mpc; they recommend a global fractional
uncertainty of ≈ 3.5 % for DESI TF distances (≈ 1 % for aligned, up to ≈ 10 % for strongly
misaligned systems) [src]. This is an added systematic term, small beside the 0.466 mag intrinsic
scatter, but coherent with galaxy morphology.

**Public data and status.**

- DESI DR1 spectra and redshifts: public since 19 March 2025; EDR since 13 June 2023 [sec:
  data.desi.lbl.gov/doc/releases, read 2026-10-08].
- DR1 PV measurements and likelihood products: Zenodo record 17672675 and the power-spectrum code at
  github.com/FeiQin-cosmologist/Galaxy_Power_Spectrum [src: arXiv:2512.03231, data availability].
- DESI DR2 (three years of data): the release page lists no public DR2; only the DR2 BAO cosmology
  chains are out [sec: same page]. **No DR2 peculiar-velocity paper was found** in date-sorted arXiv
  searches up to 2026-10-08. The DR1 field-level paper calls its mock study "a preparation for the
  DR2 data release, which will contain more Tully-Fisher galaxies" [src: arXiv:2512.03229].

---

## 4. Supernova samples used as velocity tracers
<!-- key: supernova-samples-used-as-velocity-tracers -->

Sample definitions, calibration and release status of the SN compilations are in `cosmo-supernovae`
(`references/surveys-and-data.md`). Velocity-specific facts:

| Sample | Velocity use | Status on the snapshot date | Reference | Flag |
|---|---|---|---|---|
| Pantheon+ (low z) | SN magnitude × DESI BGS correlations; σ8 and γ from the magnitude covariance; zero-point anchor of DESI DR1 PV | public | arXiv:2510.07673, arXiv:2604.06361, arXiv:2512.03232 | [src] |
| ZTF SN Ia DR2 | 3 628 spectroscopically classified SNe Ia at z < 0.3 (March 2018 – December 2020); 2 667 pass light-curve cuts; "nearly a thousand" in the volume-limited z < 0.06 sample | public, but "the photometric accuracy of the DR2 is not yet suited for cosmological parameter inference", deferred to "DR2.5" | Rigault et al. 2025, arXiv:2409.04346 | [src] |
| ZTF, growth rate | simulations only: 19 % on fσ8 from 6 years at z < 0.06, velocities alone; 10 % (σ = +0.047/−0.048) when combined with DESI DR3 BGS density — both **forecasts** | **no fσ8 from ZTF data found** in date-sorted searches up to 2026-10-08 | Carreres et al. 2023, arXiv:2303.01198; Ravoux et al. 2026, arXiv:2609.34508 | [src] |
| TITAN (ATLAS) | ~2 000 SNe Ia at z < 0.067 expected; end-to-end simulated measurement only | data analysis not published | Dixon et al. 2026, arXiv:2606.14962 | [src] |
| Hawai'i Supernova Flows | optical + NIR SN Ia distances; bulk flow within z ≲ 0.1 | published | Do et al. 2026, arXiv:2606.17142 | [src] |
| WHALES | SNe Ia in and around superclusters; first two seasons on Shapley (0.02 < z < 0.06): 12 likely SNe Ia, 8 spectroscopically confirmed | initial data release | Acevedo et al. 2025, arXiv:2510.26731 | [src] |
| Rubin LSST | **forecast**: 10 % on fσ8 over 0.02 < z < 0.14 in the most realistic scenario | 10-year survey began 30 June 2026 [sec: `cosmo-supernovae` surveys file] | Rosselli et al. 2025, arXiv:2507.00157 | [src] |

**The compilation's SN table.** Folded on 2026-10-20 from the compilation of 2026-08-12/14, in which `[src]` meant "traced to the
paper" and `[der]` "relabelled or derived, the paper does not quote fσ8".
Two distinct uses, often confused: **PV as signal** (SNe as velocity tracers, to measure fσ8) and
**PV as nuisance** (correcting SN redshifts for peculiar motion in Hubble-diagram cosmology).

| Sample | N | z | Note |
|---|---|---|---|
| Pantheon+ | 1 701 light curves / 1 550 unique SNe, 18 subsamples | 0.001–2.26 | SALT2; strength is the low-z anchor. PVs reliable only at z < 0.02 (σ ≈ 300 km/s) |
| Union3 | 2 087 SNe, 24 datasets | — | SALT3, Bayesian hierarchical errors; shares ~1 360 SNe with Pantheon+ |
| DES-Y5 | 1 635 photometric + 194 low-z = 1 829 | 0.10–1.13 (+0.025–0.10) | dominates z > 0.5; too distant for PV work |
| A2 (Boruah et al. 2020) | 465 SN PVs | z < 0.067 | compared to the 2M++ reconstruction, jointly with SFI++ and 2MTF |
| DSS (Stahl et al. 2021) | 775 low-z SNe Ia **and II**, 137 via snapshot distances | low z | fσ8 = 0.390 ± 0.022 |
| ZTF SN Ia DR2 | 994 at z < 0.06 (volume-limited); "~3 600 below z < 0.06 in the fuller sample" | z < 0.06 | Rigault et al. 2025 overview; PV impact on the Hubble diagram in Carreres et al. 2025 |

The compilation's "~3 600 below z < 0.06" disagrees with the 3 628 SNe Ia at z < 0.3 of the DR2
abstract in the table above; its 994 fits "nearly a thousand". **Sharing**: Pantheon+, Union3 and
the PV compilations draw on the same low-z SNe, so combining fσ8 from two of them is not combining
independent data; state which low-z sample underlies a quoted fσ8.

---

## 5. HI Tully–Fisher surveys
<!-- key: hi-tully-fisher-surveys -->

| Survey | Content | Status | Reference | Flag |
|---|---|---|---|---|
| WALLABY pilot, phase 1 | 614 HI spectra in four fields, 472 usable, 251 sufficiently inclined; TF distances with W1; cluster distances to 5–10 % | published | Courtois et al. 2023, arXiv:2210.12498 | [src] |
| WALLABY pilot, phase 2 (PDR2) | 180 deg², three more fields; TF from 0.8 to 3.4 μm, including the 4HS target photometry | published | Mould et al. 2024, arXiv:2406.10877 | [src] |
| WALLABY full survey | 132 footprints observed by 31 December 2025, "around 11.5 %" complete; "almost 6 000" full-survey detections released internally; public release of the first tranche under discussion | observing | [sec: WALLABY newsletter, wallaby-survey.org, February 2026, read 2026-10-08] | [sec] |
| FAST | 4 796 velocities in CF4++ | first release ingested | arXiv:2502.01308 | [src] |
| SKAO | **forecast** chapter for TF surveys with SKA-Mid AA* and AA4 | planned | Mayor et al. 2026, arXiv:2606.26001 | [src] |

The expected size of WALLABY is quoted inconsistently by its own papers: "around half a million
galaxies with a mean redshift of z = 0.05" in arXiv:2210.12498, "200,000 galaxies" for the
full-survey TF programme in arXiv:2406.10877 [src]. Folded on 2026-10-20 from the compilation of 2026-08-12/14, in which `[src]` meant "traced to the
paper" and `[der]` "relabelled or derived, the paper does not quote fσ8". It gives WALLABY as HI (21 cm)
TF, ~17 000–40 000 PVs of ~324 000 detections ("forecasts vary"), 0 < z < 0.10, observing since
2022, a 5-year run over 14 000 deg² of the southern sky with ASKAP.

---

## 6. Next: 4HS, DESI DR2/DR3, Rubin, kSZ
<!-- key: next-4hs-desi-dr2-dr3-rubin-ksz -->

| Programme | What it adds | Status on the snapshot date | Flag |
|---|---|---|---|
| 4MOST Hemisphere Survey (4HS) | southern FP sample, > 400 000 early types at z < 0.15 (numbers below) | 4MOST first light in October 2025; "Verification, Commissioning, and Survey Validation"; "expected start of full science operations in Q2 2026" — the page had not been updated beyond that statement when read | [sec: 4most.eu home page, read 2026-10-08] |
| DESI PV DR2 | three years of data; more TF | not public; no paper | [sec: DESI release page] |
| DESI DR3 BGS × ZTF 6-year SNe | field-level density × velocity | **forecast** only (arXiv:2609.34508) | [src] |
| Rubin LSST SNe Ia | velocities to z ~ 0.14 and beyond | survey started 30 June 2026 | [sec: `cosmo-supernovae`] |
| kSZ velocity reconstruction | large-scale radial modes at z ~ 0.5–2 | ACT DR6 × DESI DR2 published (arXiv:2604.04867); Simons Observatory next (belongs to `cosmo-cmb-lss-cross-correlations`) | [src] |
| Gravitational-wave sirens as distance tracers | **forecast**: ~3 % on fσ8 from Einstein Telescope neutron-star mergers at z ≲ 0.2 after 10 years, with DESI and TAIPAN densities | concept | Palmese & Kim 2021, arXiv:2005.04325 [src] |

**The compilation's table of current and future surveys.** Folded on 2026-10-20 from the compilation of 2026-08-12/14, in which `[src]` meant "traced to the
paper" and `[der]` "relabelled or derived, the paper does not quote fσ8".

| Survey | Method | Expected N | z | Status |
|---|---|---|---|---|
| DESI PV | FP **and** TF | ~133 000 FP + ~53 000 TF (Saulder et al. 2023 targets) | z ≲ 0.15 | ongoing; spare-fibre programme, 14 000 deg² north. First major survey measuring both FP and TF with one instrument, TF from optical rather than HI (§3) |
| WALLABY | TF (HI) | ~17 000–40 000 PVs (§5) | 0 < z < 0.10 | observing since 2022, southern, ASKAP |
| 4HS | FP | > 400 000 early types | z < 0.15 | future; ~6 M redshifts over 17 000 deg², ~95 % completeness. Largest FP sample ever planned |
| Taipan | FP | ~45 000–80 000 (quoted figures differ) | z < 0.1 | southern; check current status before citing — largely superseded by 4HS |
| ZTF | SN Ia | ~10³ usable | z < 0.06 | ongoing, north |
| LSST | SN Ia | orders of magnitude more | z < 0.35 | starts 2026; ≥ 825 visits per southern field over 10 yr |

**Forecast headline** (Turner §6): current and future PV surveys will cover almost the whole sky to
z = 0.3 and deliver fσ8 to **≲ 3 %**, comparable to current expansion-history precision; a combined
WALLABY + Taipan forecast also gives ~3 % — both **forecasts**. Taipan, which several forecasts
above assume, should not be cited as a coming survey without checking its status.

---

## 7. Public codes and data products
<!-- key: public-codes-and-data-products -->

| Product | What | Reference | Flag |
|---|---|---|---|
| `flip` | field-level covariance and likelihood, wide-angle, JAX; Fisher forecasts; docs at flip.readthedocs.io | arXiv:2501.16852 | [src] |
| `velocisaurus` | EFT predictions of redshift-space velocity statistics (github.com/sfschen/velocisaurus) | arXiv:2508.00066 | [src] |
| Galaxy_Power_Spectrum (CosmPSPy) | density and momentum power-spectrum estimators, models, window convolution | arXiv:2512.03231 | [src] |
| Gacomb | consensus combination of correlated measurements, used for the DESI DR1 consensus (github.com/TyannDB/Gacomb) | arXiv:2512.03230 | [src] |
| VIRBIUS | Bayesian joint reconstruction of distances and velocity field | arXiv:1512.04534 | [src] |
| Iskay2 | pairwise kSZ signal-extraction pipeline | Gallardo et al. 2025, arXiv:2510.20715 | [src: title] |
| CF4++ fields | catalogue and reconstructed density and velocity fields | arXiv:2502.01308 | [src] |

## Not verified in this file
<!-- key: not-verified-in-this-file -->

- 4HS sample sizes and footprint: from the 2026-08 compilation (§6), not re-read.
- §0, §1 (Mark III and SFI++ rows, the compilation's survey figures, the notes), §4 (the
  compilation's SN table), §5 (WALLABY expected size) and §6 (the compilation's table and forecast
  headline): folded from the 2026-08 compilation, not re-read.
- ZTF "DR2.5": no release paper found; see `cosmo-supernovae`.
- The label of the ± 4.86 term in the DESI EDR FP H0 (the abstract was read truncated at that
  point).
- Whether the WALLABY full survey has made a public release since February 2026.
