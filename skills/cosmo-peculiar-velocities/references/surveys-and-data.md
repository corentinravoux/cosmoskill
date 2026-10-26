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

Folded on 2026-10-20 from the compilation of 2026-08-12/14, in which `src` meant "traced to the
paper" and `der` "relabelled or derived, the paper does not quote fσ8".
Source of the descriptions in §0–1 and §6: the review of Turner 2024 (arXiv:2411.19484), §3, §4, §6.

A peculiar velocity needs a **redshift-independent distance**. Only three methods deliver them in
bulk over cosmological volumes.

| Indicator | Tracer | Distance error per object | Practical reach |
|---|---|---|---|
| **Tully–Fisher (TF)** | spirals; luminosity–HI linewidth | ~20 % (scatter "around 0.35-0.40 mag") [src: arXiv:2411.19484, Sect. 3.1] | z < 0.15 for both scaling relations [src: arXiv:2411.19484, Sect. 4] |
| **Fundamental Plane (FP)** | early types; σ–R_e–I_e | ~20 % (intrinsic scatter "around 0.1 dex") [src: arXiv:2411.19484, Sect. 3.1] | as TF |
| **SN Ia** | standardisable candle | smaller per object than TF or FP (no figure read) | "the most relevant" SNe Ia for PV work are at z < 0.3 [src: arXiv:2411.19484, Sect. 6.2] |

- **The controlling fact** (Turner 2024, arXiv:2411.19484, Sect. 4): the TF/FP scatter is a
  constant in *magnitude*, so the distance error is proportional to the distance and the velocity
  error grows linearly with distance. Scaling-relation surveys are therefore "restricted to the
  local universe (z < 0.15)" however many galaxies they observe, and "SNe Ia are the only reliable
  method by which we can probe the peculiar velocity field directly beyond redshifts of z ∼ 0.15"
  [src: arXiv:2411.19484, Sects. 4 and 6.2].
- TF/FP win on *number* (the catalogues of §1–2), SNe on *per-object precision* and reach: not
  competing strategies, but different parts of the same volume.
- Other indicators (TRGB, SBF, masers, JAGB, Cepheids, GW sirens) are calibration rungs, not
  survey-scale velocity tracers.

---

## 1. Past surveys — numbers as their own papers give them
<!-- key: past-surveys-numbers-as-their-own-papers-give -->

| Survey | Indicator | Sample | Sky / depth | Distance error | Reference | Flag |
|---|---|---|---|---|---|---|
| 6dFGSv | FP | 8 885 galaxies | southern hemisphere, \|b\| > 10°, z < 0.055 | 0.11 dex in log-distance, "26 % in linear distance" | Springob et al. 2014, arXiv:1409.6161; Scrimgeour et al. 2016, arXiv:1511.06930 | [src: abstract of both; \|b\| > 10° from arXiv:1511.06930, abstract] |
| 2MTF | TF (HI + 2MASS J, H, K) | 2 018 spirals | all sky except \|b\| < 5°, within 100 h⁻¹Mpc | — | Hong et al. 2014, arXiv:1409.0287 | [src: abstract] |
| SDSS PV | FP | 34 059 early types | 7 016 deg², z ≤ 0.1 | mean 23 % | Howlett et al. 2022, arXiv:2201.03112 | [src: abstract] |
| Cosmicflows-4 | 8 methods | 55 877 galaxies in 38 065 groups | both hemispheres, anisotropic depth | — | Tully et al. 2023, arXiv:2209.11238 | [src: abstract] |
| Mark III | TF + FP | ~3 200 | z̄ ~ 0.015 | — | Willick et al.; first uniform re-treatment of 1980s data | [sec: Turner 2024, arXiv:2411.19484, Sect. 4] |
| SFI++ | TF (I band) | ~5 000 | — | — | Springob et al. 2007; **erratum 2009** (morphological-type correction misapplied) | [sec: arXiv:2411.19484, Sect. 4, for the sample] |

Folded on 2026-10-20 from the compilation of 2026-08-12/14, in which `src` meant "traced to the
paper" and `der` "relabelled or derived, the paper does not quote fσ8". The last two rows come from it (chronological in Turner 2024, arXiv:2411.19484, Sect. 4: Mark III,
SFI++, 6dFGSv, 2MTF, SDSS PV, CF4). That section gives 6dFGSv as "almost 9000" early types; 2MTF
as "around 2000 galaxies out to a redshift of ∼0.03 and a median redshift of ∼0.016", in a final
release of 2019; SDSS PV as reaching z = 0.1 with "an effective redshift of z ∼ 0.07" [src:
arXiv:2411.19484, Sect. 4]. The rows above, read in the survey papers, differ in the 2MTF
reference year (Hong et al. 2014) and the CF4 year (2023).

Notes.

- **2MTF's selling point is the Galactic plane.** 6dFGSv covers |b| > 10° (arXiv:1511.06930,
  abstract); 2MTF uses the infrared and covers the whole sky apart from |b| < 5° (arXiv:1409.0287,
  abstract), recovering structure in the Zone of Avoidance that otherwise biases reconstructions.
- **6dFGSv and SDSS PV are complementary by construction**: south against north, similar N within
  the 6dFGS redshift limit, but SDSS extends to z = 0.1 [src: arXiv:2411.19484, Sect. 4].
- **CF4 is a compilation, not a survey**: FP (mostly 6dFGSv + SDSS PV) and TF (SFI++, 2MTF and
  others) distances, plus SNe Ia, SNe II and SBF, from different groups with different
  calibrations — which is why bulk flows derived from it are estimator- and calibration-sensitive.
  It largely *contains* 6dFGSv, SDSS PV, SFI++ and 2MTF and is not independent of them. (The CF4
  paper's own merging counts, 42 254 FP and 12 395 TF galaxies, are in `systematics.md` §9b, read in
  arXiv:2209.11238, Sect. X.1.)

- 6dFGSv velocities are delivered as **probability distributions** at the redshift-space position of
  each galaxy, from a Bayesian FP fit [src: arXiv:1409.6161]. The mean of η corresponds to the
  median of v [src: arXiv:1804.05520, §3, citing Scrimgeour et al.].
- SDSS PV ships 2 048 mocks with the survey selection and a group-richness correction; its
  zero-point is tied to Cosmicflows-3 [src: arXiv:2201.03112, abstract]. It is the sample behind three rows of
  the fσ8 table of `results.md` §0.
- Cosmicflows-4 absolute scale: Cepheids, TRGB and the NGC 4258 maser; the assembly "is compatible
  with" H0 = 74.6 ± 0.8 (stat), "large potential systematic error of ~3 km/s/Mpc" [src:
  arXiv:2209.11238]. [src: abstract]

---

## 2. Cosmicflows-4++ and its derivatives (2025–2026)
<!-- key: cosmicflows-4-and-its-derivatives-2025-2026 -->

| Release | Content | Reference | Flag |
|---|---|---|---|
| CF4++ | CF4 plus first-release velocities from WALLABY (655), FAST (4 796) and DESI (4 191); catalogue and reconstructed density and velocity fields **publicly released** | Courtois et al. 2025, arXiv:2502.01308 | [src: abstract] |
| CF4++ as used for clustering | 65 331 galaxy distances, out to z = 0.1 | Franco, Courtois & Bernui 2026, arXiv:2605.00450 | [src: abstract] |
| CF4++ZOA | 65 518 CF4++ distances + 8 283 new redshifts at \|b\| ≤ 10° (2 176 from MeerKAT HI, covering the innermost 3°-wide strip of the southern Zone of Avoidance) | Hollinger et al. 2026, arXiv:2603.09339 | [src: abstract] |

The two CF4++ counts (65 331 and 65 518) are both as printed in the cited abstracts (arXiv:2605.00450,
arXiv:2603.09339; the 4 191 DESI objects below are from the arXiv:2502.01308 abstract); the difference
is not explained there. CF4++ is still a compilation: every caution of §1 about CF4
applies, and its DESI component is an early subset (4 191 objects), not the DR1 catalogue.

Results obtained from it in the same period: bulk flow of 315 ± 40 km/s at 150 h⁻¹Mpc and "the
dynamical scale of homogeneity is not yet reached in the interval [200–300] Mpc/h"
(arXiv:2502.01308) [src: abstract]; the Vela mass (`results.md` §2).

---

## 3. DESI Peculiar Velocity Survey
<!-- key: desi-peculiar-velocity-survey -->

A secondary-target programme of DESI, FP and TF with one instrument and one photometric system
(Legacy Surveys DR9).

| Stage | Date | Content | Reference | Flag |
|---|---|---|---|---|
| Target selection | 2023-02 | 373 533 early-type and 118 637 late-type targets in the 5-year footprint; predicted yield ~133 000 FP + ~53 000 TF velocities over 14 000 deg² | Saulder et al. 2023, arXiv:2302.13760 | [src: Sect. "Résumé"] |
| Survey validation / EDR, FP | 2024-08 | 6 698 unique early types observed, 4 267 with velocity-dispersion error < 10 %; FP zero-point from the Coma SBF distance; H0 = 76.05 ± 0.35 (stat) ± 0.49 (syst FP), ± 4.86 ("statistical due to calibration"), the term that dominates | Said et al. 2025, arXiv:2408.13842 | [src: abstract] |
| EDR, TF | 2025-07 | rotation at 0.33 R26 for 1 163 spirals (1 136 + 27 dwarfs); slope −7.96 ± 0.13 AB mag from 41 Coma spirals, scatter 1.07 ± 0.02 mag; public distance catalogue | Douglass et al. 2025, arXiv:2507.11765 | [src: abstract] |
| DR1 FP catalogue | 2025-12 | 98 292 unique early types, z < 0.1, 26 % distances | Ross et al. 2025, arXiv:2512.03226 | [src: abstract] |
| DR1 TF catalogue | 2025-12 | 10 262 spirals, rotation at 0.4 R26; 6 807 in the clustering catalogue | Douglass et al. 2025, arXiv:2512.03227 | [src: abstract] |
| DR1 mocks | 2025-12 | 675 realisations with BGS density, FP, TF and SN Ia samples | Bautista et al. 2025, arXiv:2512.03228 | [src: abstract] |
| DR1 zero-point | 2025-12 | η_zp = 0.139 ± 0.007 from SH0ES/Pantheon+ SNe via groups | Carr et al. 2025, arXiv:2512.03232 | [src: Sect. V.5] |

**From catalogue to cosmology sample.** The counts shrink at each step, and the growth-rate papers
do not all quote the same one [src: first row, abstract of arXiv:2512.03226 and of arXiv:2512.03227; other rows, arXiv:2512.03230, Sects. 2.2.1–2.2.2, and arXiv:2512.03229, abstract and Sect. 2.1]:

| Step | FP | TF |
|---|---|---|
| Catalogue | 98 292 | 10 262 |
| Clustering sample, 0.01 < z < 0.1 | 73 822 | 6 806 |
| After removing TF at z > 0.05 | — | 2 934 |
| After the 4σ cut on η | 73 686 | 2 929 |
| Velocities in the fit | 76 615 (correlation functions) / 76 616 (field-level) | |

together with 415 523 BGS redshifts; z_eff = 0.07 is "the mean redshift of all galaxies across the
clustering and velocity samples" [src: arXiv:2512.03230, Sect. 2.2.2]. Mean η uncertainty: 0.12 (FP),
0.11 (TF) [src: arXiv:2512.03229, Sect. 2.1]. "Over 90%" of the velocities are FP [src:
arXiv:2512.03229, Sect. 2.1], so DR1 is, in practice, an FP measurement.

**TF follow-up.** Siwakoti et al. 2026 (arXiv:2608.26459) test the single-fibre rotation measurement
against integral-field data for 215 galaxies: ~28 % have photometric–kinematic position-angle
misalignments > 10°; median distance bias ≈ +1.98 Mpc; they recommend a global fractional
uncertainty of ≈ 3.5 % for DESI TF distances (≈ 1 % for aligned, up to ≈ 10 % for strongly
misaligned systems) [src: abstract]. This is an added systematic term, small beside the 0.466 mag
intrinsic scatter of the DR1 TF relation (arXiv:2512.03227, abstract), but coherent with galaxy
morphology.

**Public data and status.**

- DESI DR1 spectra and redshifts: public since 19 March 2025; EDR since 13 June 2023 [sec:
  data.desi.lbl.gov/doc/releases, read 2026-10-08].
- DR1 PV measurements and likelihood products: Zenodo record 17672675 and the power-spectrum code at
  github.com/FeiQin-cosmologist/Galaxy_Power_Spectrum [src: arXiv:2512.03231, data availability]. [src: Sect. "Data availability"]
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
| ZTF SN Ia DR2 | 3 628 spectroscopically classified SNe Ia at z < 0.3 (March 2018 – December 2020); 2 667 pass light-curve cuts; "nearly a thousand" in the volume-limited z < 0.06 sample | public, but "the photometric accuracy of the DR2 is not yet suited for cosmological parameter inference", deferred to "DR2.5" | Rigault et al. 2025, arXiv:2409.04346 | [src: abstract] |
| ZTF, growth rate | simulations only: 19 % on fσ8 from 6 years at z < 0.06, velocities alone; 10 % (σ = +0.047/−0.048) when combined with DESI DR3 BGS density — both **forecasts** | **no fσ8 from ZTF data found** in date-sorted searches up to 2026-10-08 | Carreres et al. 2023, arXiv:2303.01198; Ravoux et al. 2026, arXiv:2609.34508 | [src: abstract of each] |
| TITAN (ATLAS) | ~2 000 SNe Ia at z < 0.067 expected; end-to-end simulated measurement only | data analysis not published | Dixon et al. 2026, arXiv:2606.14962 | [src: abstract] |
| Hawai'i Supernova Flows | optical + NIR SN Ia distances; bulk flow within z ≲ 0.1 | published | Do et al. 2026, arXiv:2606.17142 | [src: abstract] |
| WHALES | SNe Ia in and around superclusters; first two seasons on Shapley (0.02 < z < 0.06): 12 likely SNe Ia, 8 spectroscopically confirmed | initial data release | Acevedo et al. 2025, arXiv:2510.26731 | [src: abstract] |
| Rubin LSST | **forecast**: 10 % on fσ8 over 0.02 < z < 0.14 in the most realistic scenario | 10-year survey began 30 June 2026 [sec: `cosmo-supernovae` surveys file] | Rosselli et al. 2025, arXiv:2507.00157 | [src: abstract] |

**The compilation's SN table.** Folded on 2026-10-20 from the compilation of 2026-08-12/14, in which `src` meant "traced to the
paper" and `der` "relabelled or derived, the paper does not quote fσ8".
Two distinct uses, often confused: **PV as signal** (SNe as velocity tracers, to measure fσ8) and
**PV as nuisance** (correcting SN redshifts for peculiar motion in Hubble-diagram cosmology).

From Turner 2024 (arXiv:2411.19484, Sect. 3.2, and Sect. 6.2 for ZTF) unless a row names another paper and place:

| Sample | N | z | Note |
|---|---|---|---|
| Pantheon+ | 1 701 light curves / 1 550 unique SNe, 18 subsamples | 0.001–2.26 | SALT2; strength is the low-z anchor |
| Union3 | 2 087 SNe, 24 datasets | — | SALT3, Bayesian hierarchical errors; shares ~1 360 SNe with Pantheon+ |
| DES-Y5 | 1 635 photometric + 194 low-z = 1 829 | 0.10–1.13 (+0.025–0.10) | dominates z > 0.5; too distant for PV work |
| A2 (Boruah et al. 2020) | 465 SN PVs | z < 0.067 | compared to the 2M++ reconstruction, jointly with SFI++ and 2MTF (arXiv:1912.09383, abstract) |
| DSS (Stahl et al. 2021) | 775 low-z SNe Ia **and II**, 137 via snapshot distances | low z | fσ8 = 0.390 ± 0.022 (arXiv:2105.05185, abstract) |
| ZTF SN Ia DR2 | "around 3600 supernovae below z<0.06" in current ZTF datasets (Sect. 6.2) | z < 0.06 | Rigault et al. 2025 overview; PV impact on the Hubble diagram in Carreres et al. 2025 |

Turner's "around 3600 supernovae below z<0.06" (arXiv:2411.19484, Sect. 6.2) does not match the DR2
overview, which gives 3 628 SNe Ia at z < 0.3 and "nearly a thousand" in the volume-limited z < 0.06
sample (arXiv:2409.04346, abstract). **Sharing**: Pantheon+, Union3 and
the PV compilations draw on the same low-z SNe, so combining fσ8 from two of them is not combining
independent data; state which low-z sample underlies a quoted fσ8.

---

## 5. HI Tully–Fisher surveys
<!-- key: hi-tully-fisher-surveys -->

| Survey | Content | Status | Reference | Flag |
|---|---|---|---|---|
| WALLABY pilot, phase 1 | 614 HI spectra in four fields, 472 usable, 251 sufficiently inclined; TF distances with W1; cluster distances to 5–10 % | published | Courtois et al. 2023, arXiv:2210.12498 | [src: abstract] |
| WALLABY pilot, phase 2 (PDR2) | 180 deg², three more fields; TF from 0.8 to 3.4 μm, including the 4HS target photometry | published | Mould et al. 2024, arXiv:2406.10877 | [src: abstract] |
| WALLABY full survey | 132 footprints observed by 31 December 2025, "around 11.5 %" complete; "almost 6 000" full-survey detections released internally; public release of the first tranche under discussion | observing | [sec: WALLABY newsletter, wallaby-survey.org, February 2026, read 2026-10-08] | [sec] |
| FAST | 4 796 velocities in CF4++ | first release ingested | arXiv:2502.01308 | [src: abstract] |
| SKAO | **forecast** chapter for TF surveys with SKA-Mid AA* and AA4 | planned | Mayor et al. 2026, arXiv:2606.26001 | [src] |

Expected size of WALLABY: arXiv:2210.12498 expects it "to detect around half a million galaxies with
a mean redshift of z = 0.05" and suggests "that about 200,000 Tully-Fisher distances might result
from the survey"; arXiv:2406.10877 speaks of "the full WALLABY survey of 200,000 galaxies" [src:
abstract of each]. The 2026-08 compilation (folded on 2026-10-20) gave further PV and detection
counts that no paper read here states; they are not reproduced. WALLABY is an HI (21 cm) TF survey of
the southern sky with ASKAP.

---

## 6. Next: 4HS, DESI DR2/DR3, Rubin, kSZ
<!-- key: next-4hs-desi-dr2-dr3-rubin-ksz -->

| Programme | What it adds | Status on the snapshot date | Flag |
|---|---|---|---|
| 4MOST Hemisphere Survey (4HS) | southern FP sample, > 400 000 early types at z < 0.15 (arXiv:2411.19484, Sect. 6.2; numbers below) | 4MOST first light in October 2025; "Verification, Commissioning, and Survey Validation"; "expected start of full science operations in Q2 2026" — the page had not been updated beyond that statement when read | [sec: 4most.eu home page, read 2026-10-08] |
| DESI PV DR2 | three years of data; more TF | not public; no paper | [sec: DESI release page] |
| DESI DR3 BGS × ZTF 6-year SNe | field-level density × velocity | **forecast** only (arXiv:2609.34508) | [src] |
| Rubin LSST SNe Ia | **forecast** fσ8 precision quoted over 0.02 < z < 0.14 (arXiv:2507.00157, abstract) | survey started 30 June 2026 | [sec: `cosmo-supernovae`] |
| kSZ velocity reconstruction | large-scale radial velocity modes from DESI LRGs, ELGs and QSOs | ACT DR6 × DESI DR2 published (arXiv:2604.04867, abstract); Simons Observatory next (belongs to `cosmo-cmb-lss-cross-correlations`) | [src] |
| Gravitational-wave sirens as distance tracers | **forecast**: ~3 % on fσ8 from Einstein Telescope neutron-star mergers at z ≲ 0.2 after 10 years, with DESI and TAIPAN densities | concept | Palmese & Kim 2021, arXiv:2005.04325 [src: abstract] |

**The compilation's table of current and future surveys.** Folded on 2026-10-20 from the compilation of 2026-08-12/14, in which `src` meant "traced to the
paper" and `der` "relabelled or derived, the paper does not quote fσ8". Re-read on 2026-10-23: each row names its source.

| Survey | Method | Expected N | z | Status |
|---|---|---|---|---|
| DESI PV | FP **and** TF | ~133 000 FP + ~53 000 TF predicted measurements (Saulder et al. 2023, arXiv:2302.13760, abstract) | z < 0.15 (same) | ongoing; spare-fibre programme, 14 000 deg² north (same). First major survey measuring both FP and TF with one instrument, TF from optical rather than HI (§3) |
| WALLABY | TF (HI) | "about 200,000 Tully-Fisher distances might result" (arXiv:2210.12498, abstract) | mean z = 0.05 of the detections (same) | observing, southern, ASKAP (§5) |
| 4HS | FP | > 400 000 early types | z < 0.15 | future; about six million redshifts over 17 000 deg², ~95 % completeness. Largest FP sample ever planned [sec: Turner 2024, arXiv:2411.19484, Sect. 6.2] |
| Taipan | FP | — (the forecast sizes in the compilation were not re-read) | — | southern; check current status before citing — largely superseded by 4HS |
| ZTF | SN Ia | "nearly a thousand" in the volume-limited DR2 sample (arXiv:2409.04346, abstract) | z < 0.06 (same) | ongoing, north |
| LSST | SN Ia | orders of magnitude more, to z < 0.35; each southern field imaged at least 825 times over 10 years [sec: arXiv:2411.19484, Sect. 6.2] | z < 0.35 | starts 2026 |

**Forecast headline** (Turner 2024, arXiv:2411.19484, Sect. 6.2): current and future PV surveys will
cover almost the whole sky to z = 0.3 and deliver fσ8 to **≲ 3 %**, comparable to current
expansion-history precision; its Sect. 2.1 attributes forecasts "of order ≲ 3%" to Koda et al. 2014
and Howlett et al. 2017a — both **forecasts**. Taipan, which several forecasts
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

- The compilation figures of §0, §1, §4 and §6 were re-read on 2026-10-23 in Turner 2024
  (arXiv:2411.19484) and the survey abstracts; those not found there were removed: the SN Ia
  per-object distance error, the SFI++ sky coverage and median redshift, the 6dFGSv analysis subsample, the CF4 FP and TF totals, the Taipan sample size, the WALLABY PV and detection
  counts, the Pantheon+ redshift limit for reliable PVs, the ZTF "994" and the 2MTF σ_v fit.
- 4HS sample sizes and footprint: as given by Turner 2024, Sect. 6.2 (secondary), not read in a 4HS
  paper.
- ZTF "DR2.5": no release paper found; see `cosmo-supernovae`.

- Whether the WALLABY full survey has made a public release since February 2026.
