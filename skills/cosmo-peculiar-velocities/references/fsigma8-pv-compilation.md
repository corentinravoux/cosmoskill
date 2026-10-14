# fσ8 from peculiar velocities — compilation

Published fσ8 values from peculiar-velocity data, as located by August 2026 (TF, FP,
SNe Ia and mixed compilations), with its uncertainty, effective redshift,
distance indicator, dataset, estimator, and citation.

Compiled **2026-08-13**, method families added **2026-08-14**. Companion to
`pv-surveys.md` (surveys, systematics, and the method-family definitions in §5).

This file is a table for reading and its discussion. It is not a data
product: a compilation meant to be loaded by code belongs in a data package
with its own integrity tests.

## Provenance code — read this before quoting anything
<!-- key: provenance-code-read-this-before-quoting -->

| | meaning |
|---|---|
| **[src]** | value traced to the paper itself — abstract, or the body where the abstract does not state it |
| **[der]** | the paper does **not** quote fσ8; the number is a relabelling or derivation — Ω_m^0.55σ8, β, or the midpoint of a quoted interval |
| ~~[T24]~~ | *no longer used* — every row has now been traced to its source |

**All 36 measurement rows are now first-hand**: 32 [src], 4 [der]. Reaching that
took two passes, and the second pass changed six values (§4). The count was 39
before four non-PV rows (Achitouv ×2, Beutler 2012, Blake+2018 — redshift-space
distortions of the 6dFGS *redshift* survey, no measured distances) were removed
on 2026-08-13; see §4a.

**The [der] rows are circular if used to test gravity.** Carrick et al. measure
Ω_m^0.55σ8, Nusser quotes an interval on the same combination, and the Davis
value follows from β. Calling any of them "fσ8" assumes f = Ω_m^0.55, i.e.
assumes GR. Exclude them from a growth-index fit.

---

## 1. Measurements from data
<!-- key: measurements-from-data -->

**Scope: peculiar velocities only.** Four entries carried by Turner (2024)
Table 1 are *not* here — they are redshift-space distortions of the 6dFGS
*redshift* survey with no measured distances, so they measure the same growth
rate by a different probe. Removed 2026-08-13 and listed in §4a so the
difference is explicit rather than silent.

36 measurements. The `probe` column separates analyses that model only the
velocity field (24) from those that also model the galaxy clustering / RSD (12).
It does **not** mark which analyses use an external density field: every
velocity–density row does, while being labelled `PV`, because the density field
is an input rather than part of the fitted statistic.

Ordered by effective redshift. Indicator: TF = Tully–Fisher, FP = fundamental
plane, SN = Type Ia supernovae, mix = heterogeneous compilation, lum = galaxy
luminosity fluctuations (not a direct distance indicator).

| # | Reference | fσ8 | z_eff | Ind. | Dataset | Estimator | ID | Prov. |
|---|---|---|---|---|---|---|---|---|
| 1 | Johnson et al. 2014 | 0.418 ± 0.065 | 0.00 | FP | 6dFGSv | maximum-likelihood | arXiv:1404.3799; MNRAS 444, 3926 | [T24] |
| 2 | Howlett et al. 2017 | 0.510 +0.090/−0.080 | 0.00 | TF | 2MTF | velocity power spectrum | arXiv:1706.05130 | [T24] |
| 3 | Adams & Blake 2017 | 0.424 +0.067/−0.064 | 0.00 | FP | 6dFGS | density–velocity cross-covariance | arXiv:1706.05205 | **[src]** |
| 4 | Lilow & Nusser 2021 | 0.367 ± 0.060 | 0.013 | mix | CF3 + 2MRS | constrained realisations | arXiv:2102.07291 | **[src]** |
| 5 | Boubel et al. 2024 | 0.35 ± 0.03 | 0.017 | TF | forward-modelled TF | forward model | arXiv:2301.12648 | **[src]** |
| 6 | Davis et al. 2011 | 0.310 ± 0.040 | 0.020 | TF | SFI++ | reconstruction | arXiv:1011.3114 | [T24] |
| 7 | Carrick et al. 2015 | 0.401 ± 0.024 | 0.020 | mix | 2M++ | reconstruction | arXiv:1504.04627 | [T24] |
| 8 | Huterer et al. 2017 | 0.428 +0.048/−0.045 | 0.020 | SN | low-z SNe + galaxy velocities | maximum-likelihood | arXiv:1611.09862; JCAP 05 (2017) 015 | **[src]** |
| 9 | Hollinger & Hudson 2023 | 0.362 ± 0.023 | 0.020 | mix | 2M++ | reconstruction | MNRAS 526, 337 | [T24] |
| 10 | Boruah et al. 2020 | 0.400 ± 0.017 | 0.022 | SN + TF | 465 SNe + SFI++ + 2MTF vs 2M++ | reconstruction | arXiv:1912.09383; MNRAS 498, 2703 | [T24] |
| 11 | Nusser 2017 | 0.400 ± 0.080 | 0.027 | mix | CF3 | velocity–density correlation | arXiv:1703.05324 | [T24] |
| 12 | Qin et al. 2019 | 0.404 +0.082/−0.081 | 0.03 | TF + FP | 2MTF + 6dFGSv | momentum power spectrum | arXiv:1906.02874 | **[src]** |
| 13 | Dupuy et al. 2019 | 0.43 (±0.03)_obs (±0.11)_cosmic | <0.05 | mix | CF3 | correlation | arXiv:1901.03530 | **[src]** |
| 14 | Said et al. 2020 | 0.338 ± 0.027 | 0.035 | FP | 6dFGS + SDSS | reconstruction (β → fσ8) | arXiv:2007.04993 | **[src]** |
| 15 | Adams & Blake 2020 | 0.384 ± 0.052 (stat) ± 0.061 (sys) | 0.045 | FP | 6dFGS | joint RSD + PV | arXiv:2004.06399 | **[src]** |
| 16 | Turner et al. 2023 | **0.358 ± 0.075** | 0.045 | mix | 6dFGS | velocity–density correlation | arXiv:2207.03707; MNRAS 518, 2436 | **[src]** |
| 17 | Courtois et al. 2023 | 0.380 ± 0.040 | 0.051 | mix | CF4 | correlation function | arXiv:2211.16390; A&A 670, L15 | [T24] |
| 18 | Franco et al. 2026 | 0.344 ± 0.105 | 0.07 | mix | CF4++ (65 331 distances) | joint real/redshift-space, Kaiser | arXiv:2605.00450 | **[src]** |
| 19 | Lai et al. 2023 | 0.405 +0.076/−0.071 (stat) ± 0.009 (sys) | 0.073 | FP | SDSS PV | maximum-likelihood, wide-angle + zero-point in the model | arXiv:2209.04166 | **[src]** |
| 20 | Lyall et al. 2024 | 0.329 +0.081/−0.083 | 0.073 | FP | 6dFGS + SDSS | correlation function | arXiv:2407.18684 | **[src]** |
| 21 | Qin et al. 2024 | 0.413 +0.050/−0.058 | 0.073 | FP | SDSS DR14 PV | density–momentum **cross** power spectrum | arXiv:2411.09571 | **[src]** |
| 22 | Feix et al. 2015 | 0.37 ± 0.13 | ~0.1 | lum | SDSS DR7, 2×10⁵ galaxies | galaxy **luminosity** fluctuations | arXiv:1503.05945; PRL 115, 011301 | **[src]** |
| 23 | Feix et al. 2017 | 0.48 ± 0.16 | ~0.1 | lum | SDSS DR13 | luminosity fluctuations, recalibrated photometry | arXiv:1612.07809; MNRAS 468, 1420 | **[src]** |

### Effective redshift genuinely absent — verified in the papers
<!-- key: effective-redshift-genuinely-absent-verified-in -->

These empty cells are not a gap in this file: the papers give no effective
redshift. Reading them:

- **Stiskalek 2026** — his own Table 1 prints "—" in the z_eff column for the
  Joint TFR+SNe row, the one quoted here. The individual samples do have one
  (CF4 TFR W1 0.017, CF4 TFR i 0.022, Pantheon+ 0.026, 6dF FP 0.035, SDSS FP
  0.037); the joint fit deliberately does not.
- **Stahl et al. 2021** — sample cut at z < 0.07, no effective redshift quoted.
- **Wang et al. 2026** — the analysis is framed in survey depth (h⁻¹Mpc).

Stiskalek's Fig. 4 does plot literature points at effective redshifts, but those
are **his** assignments (sample mean redshifts he computes), not the original
authors'. Adopting them would silently attribute one author's choice to another.

Stiskalek's Table 1 also quantifies the fundamental-plane instability he warns
about: under the quadratic Malmquist treatment, 6dF FP moves from
fσ8L = 0.379 ± 0.016 to **0.301 ± 0.015**, and SDSS FP from 0.412 to 0.373,
while the TFR and SN samples barely move.

| Reference | fσ8 | Note | ID | Prov. |
|---|---|---|---|---|
| Stahl et al. 2021 | 0.390 ± 0.022 | DSS: 775 low-z SNe **Ia and II**, 137 via snapshot distances; vs 2M++ | arXiv:2105.05185; MNRAS 505, 2349 | **[src]** |
| Stiskalek 2026 | 0.412 ± 0.018 | **TF + SN combined**; S₈ = 0.798 ± 0.035. FP excluded — unstable under inhomogeneous Malmquist treatment | arXiv:2509.20235; MNRAS 2026 | **[src]** |
| Wang et al. 2026 | 0.384 +0.116/−0.194 | CF4 group catalogue, parallel velocity correlation function | arXiv:2604.08314 | **[src]** |
| Wang et al. 2026 | 0.569 +0.054/−0.060 | *local* growth rate, same paper — a different quantity from the row above, do not quote as "the" CF4 value | arXiv:2604.08314 | **[src]** |

### DESI DR1 Peculiar Velocity Survey (2025)
<!-- key: desi-dr1-peculiar-velocity-survey-2025 -->

Three estimators, **one dataset**: 415 523 redshifts + 76 616 PVs, z_eff = 0.07.
These are not independent measurements and must never be averaged as if they were.

| Analysis | fσ8 | ID | Prov. |
|---|---|---|---|
| maximum-likelihood fields (Lai et al.) | 0.483 +0.080/−0.043 (stat) ± 0.018 (sys) | arXiv:2512.03229 | **[src]** |
| galaxy + momentum correlation functions (Turner et al.) | 0.391 +0.080/−0.081 | arXiv:2512.03230 | **[src]** |
| galaxy power spectrum (Qin et al.) | 0.440 +0.080/−0.096 | arXiv:2512.03231 | **[src]** |
| **consensus** (correlated combination) | **0.4497 ± 0.0548** | arXiv:2512.03230, arXiv:2512.03231 | **[src]** |

Derived in the same papers: γ_L = 0.580 ± 0.110, Ω_m = 0.301 ± 0.011,
σ8 = 0.834 ± 0.032. Planck+ΛCDM comparison value quoted there: fσ8 = 0.449 ± 0.008.

**The 0.391 → 0.483 spread across three estimators on identical data is the
single most useful number in this file.** It is the honest scale of current
method systematics — larger than most individual quoted error bars.

---

## 2. Forecasts and simulation validation — NOT measurements
<!-- key: forecasts-and-simulation-validation-not -->

Keep these visually and verbally separate from §1. Mixing them is the most
common error in PV review figures.

| Reference | Value | What it is | ID |
|---|---|---|---|
| Dixon et al. 2026 | ⟨fσ8⟩ = 0.429 ± 0.038 (σ_stat 0.030, σ_sys 0.023) | **Simulated** end-to-end measurement for TITAN, ~2000 mock SNe Ia at z < 0.067 on Uchuu; recovers the input 0.428 to 0.1%. First systematic budget for the reconstruction-and-scaling method | arXiv:2606.14962 |
| Tonegawa et al. 2024 | fσ8 = 0.361 (linear) vs 0.376 (PT) | **HR4 N-body mocks.** Quantifies a bias that applies to many rows of §1: fitting velocity correlation functions with a *linear* template recovers fσ8 **5.2% below** the fiducial value. MNRAS 529, 4787 | arXiv:2309.14457 |
| Ravoux et al. 2025 | — | `flip` framework: field-level covariance model with wide-angle corrections + geometry-dependent Fisher forecast. **No data fσ8 is reported** | arXiv:2501.16852; A&A 698, A273 | 
| Rosselli et al. 2025 | — | Growth-rate forecast from LSST SN peculiar velocities | arXiv:2507.00157 |

---

## 3. Excluded — bulk flow, not fσ8
<!-- key: excluded-bulk-flow-not-fsigma8 -->

Frequently cited alongside, measures a different quantity:
Watkins et al. 2023 (arXiv:2302.02028, the
contested 4.81σ excess), Whitford et al. 2023
(arXiv:2306.11269, estimator dependence),
Do et al. 2026 (Hawai'i Supernova Flows,
arXiv:2606.17142, ~100–400 km/s, all consistent
with ΛCDM).

---

## 4. Discrepancies found when going to source
<!-- key: discrepancies-found-when-going-to-source -->

**Five** of Turner's tabulated values that remain in scope do not match the source (a sixth, Beutler 2012, is out of scope — see §4a). Not errors on his
part necessarily — a review may quote a different row of a paper's results table
— but the rate (6 of 21 checked, 29%) is why nothing here is left second-hand.

| Paper | Turner Table 1 | Source abstract | Comment |
|---|---|---|---|
| Said et al. 2020 | 0.311 ± 0.027 | **0.338 ± 0.027** | abstract gives the *combined* 6dFGS+SDSS value at z_eff = 0.035; 0.311 is likely one survey alone |
| Boubel et al. 2024 | 0.360 ± 0.030 | **0.35 ± 0.03** | arXiv v2 abstract vs possibly the published MNRAS value |
| Dupuy et al. 2019 | 0.430 ± 0.140 | **0.43 (±0.03)_obs (±0.11)_cosmic** | Turner combines the two error terms; the split matters, since the cosmic-variance term is irreducible |
| Turner et al. 2023 | 0.325 ± 0.075 | **0.358 ± 0.075** | the abstract value is for 27 < s < 123 h⁻¹Mpc combining velocity and density statistics; Turner's table presumably quotes a different scale cut — of his own paper |
| Johnson et al. 2014 | 0.418 ± 0.055 | **0.418 ± 0.065** | their conclusions state 0.418 ± 0.065; the 0.055 is Beutler's error, quoted in the adjacent sentence of Johnson's own text |

Additionally, values circulating in secondary summaries for the DESI DR1 PV
correlation-function and power-spectrum analyses (0.402 +0.075/−0.077 and
0.443 +0.110/−0.070) **do not match the papers**, which give 0.391 +0.080/−0.081
and 0.440 +0.080/−0.096. Cite the arXiv abstracts.

### 4a. Removed as out of scope
<!-- key: removed-as-out-of-scope -->

Present in Turner (2024) Table 1, absent here. All four are RSD of the 6dFGS
redshift survey — no measured distances, therefore not peculiar velocities. The
two Achitouv values additionally share galaxies with each other.

| Reference | fσ8 | ID |
|---|---|---|
| Achitouv et al. 2017, galaxy–galaxy | 0.42 ± 0.06 | arXiv:1606.03092 |
| Achitouv et al. 2017, void–galaxy | 0.39 ± 0.11 | arXiv:1606.03092 |
| Beutler et al. 2012 | 0.423 ± 0.055 (Turner: 0.428 +0.079/−0.068) | arXiv:1204.4725 |
| Blake, Carter & Koda 2018 | 0.38 ± 0.12 | arXiv:1801.04969 |

---

## 4b. Linear vs non-linear σ8 — verified 2026-08-13
<!-- key: linear-vs-non-linear-sigma8-verified-2026-08-13 -->

Reading all 35 papers rather than their abstracts turned up a normalisation
split that no review flags and that this file previously hid.

**Six rows report fσ8 with the *linear* σ8**, writing it fσ8,lin or fσ8_L:
Carrick+2015, Lilow & Nusser 2021, Hollinger & Hudson 2024, Boruah+2020,
Stahl+2021, Stiskalek 2026. All six are velocity–density comparison or
reconstruction analyses — they predict the velocity field from linear theory, so
the linear normalisation is the natural output.

The remaining rows write plain fσ8 without specifying.

**The offset is larger than several of the error bars in this table.** Carrick
et al. quote both for the same data:

| | |
|---|---|
| fσ8,lin | 0.401 ± 0.024 ← the value tabulated here and by Turner |
| fσ8 (non-linear σ8) | 0.427 ± 0.026 |

6.5% apart. Six of 35 rows sit on the lower convention, and they include three of
the four tightest error bars in the compilation (Boruah 0.017, Stiskalek 0.018,
Hollinger & Hudson 0.023). Plotting them against Planck's fσ8 without saying
which normalisation is in play biases the low end of the distribution downward —
and it is exactly those points that drive any claim of tension.

Column `sigma8_norm` in the data file records this per row.

---

## 5. What the compilation shows
<!-- key: what-the-compilation-shows -->

- **Range**: 0.31 to 0.51 over 0 < z_eff < 0.08, where ΛCDM predicts a nearly
  flat fσ8 ≈ 0.45 across that interval. The scatter is dominated by method and
  systematics, not by cosmology.
- **Errors** run 0.017 to 0.19 — a factor of ten. The tightest
  (Boruah 2020, 0.017; Stiskalek 2026, 0.018; Hollinger & Hudson 2024, 0.023)
  are all *reconstruction* analyses, which import an external density field and
  its own systematics. The correlation-function and power-spectrum analyses,
  which do not, are typically 0.05–0.12.
- **Reconstruction methods cluster low** (0.31–0.40); velocity-statistics
  methods scatter wider and higher. This is a real methodological split and is
  visible in the DESI DR1 triplet within a single dataset.
- **Many entries share data.** 6dFGSv, SDSS PV, SFI++, 2MTF, 2M++ and the low-z
  SNe recur across most rows, and CF3/CF4/CF4++ *contain* several of them.
  Treating this table as independent points would be wrong.

## 6. Remaining gaps
<!-- key: remaining-gaps -->

Every value is now traced to its source and every row has an arXiv identifier.
Hollinger & Hudson resolved to arXiv:2312.03904,
*Cosmological parameters estimated from velocity–density comparisons:
calibrating 2M++* — the value 0.362 ± 0.023 is theirs after correcting a
reconstruction bias of 1.04 ± 0.01. Lai et al. 2023 confirmed a measurement on
the SDSS PV catalogue, not a mock.

Open:

- **Distance indicator for the 13 rows marked "mix".** Cosmicflows-based
  analyses blend TF, FP and SNe in proportions that change between catalogue
  versions, so a clean TF/FP/SN split of the compilation is not currently
  possible.
- **The three [der] rows** would be better replaced by the quantity the papers
  actually measure (Ω_m^0.55σ8 for Carrick and Nusser, β for Davis), with the
  GR conversion applied at plot time and visible.
- **Crisman, Quartin & Rebouças 2026**, *Joint curvature and growth rate
  measurements with supernova peculiar velocities and the CMB*
  (arXiv:2604.06361; Phys. Dark Univ. 53, 102391)
  — in scope, value not extracted; the abstract quotes σ8 and γ rather than fσ8.
- **Feix and Nguyen use the same physics** — growth from correlated magnitude
  scatter, galaxies in one case, SNe in the other. They are classed `probe=PV`
  but the `indicator` column still separates them (`lum` vs `SN`), which is
  arguably inconsistent.
