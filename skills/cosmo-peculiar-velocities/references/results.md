# Results — peculiar velocities: 2025–2026 measurements and the bulk-flow record

Scope: every published fσ8 from peculiar velocities with its provenance (§0) and the history of
that compilation (§7); the non-fσ8 output of the DESI DR1 peculiar-velocity release; the growth,
gravity and flow results found in date-sorted searches from mid-2025 to the snapshot; and the
bulk-flow record with its estimators. Snapshot: 2026-10-14

Flags: `[src]` read this session in the cited paper (abstract unless a section is named); `[sec]`
from a named secondary source; `[der]` derived, derivation stated. §0 and §7 use the flags of the
compilation they were folded from (stated there).

---

## 0. Published fσ8 from peculiar velocities
<!-- key: published-fsigma8-from-peculiar-velocities -->

Folded on 2026-10-20 from the compilation of 2026-08-12/14, in which `[src]` meant "traced to the
paper" and `[der]` "relabelled or derived, the paper does not quote fσ8".

**Codes.** `[src]`: traced to the paper (abstract, else body). `[der]`: the paper does **not**
quote fσ8 — a relabelled Ω_m^0.55σ8, β, or the midpoint of a quoted interval. `[T24]`: from Turner
(2024) Table 1, declared "no longer used — every row has now been traced to its source" yet still on
eight rows (kept as written). The compilation's count: "All 36 measurement rows are now first-hand:
32 [src], 4 [der]", 39 before four non-PV rows were removed on 2026-08-13; the second pass changed
six values (§7). `lin`: normalised to the **linear** σ8 (§0b). "re-read": checked at source on
2026-10-20. Scope: peculiar velocities only (measured distances; RSD of redshift surveys excluded,
§7). The compilation's `probe` column (not reproduced) split velocity-only analyses (24) from those
also modelling clustering / RSD (12); it did **not** mark an external density field, which every
velocity–density row uses while labelled `PV`. Ind.: mix = heterogeneous compilation, lum = galaxy
luminosity fluctuations (no direct distance). Family: `physics-and-methods.md` §0. Ordered by z_eff.

| Reference | fσ8 | z_eff | Ind. | Dataset | Family | Estimator (2026-08-13 label) | ID | Flags |
|---|---|---|---|---|---|---|---|---|
| Adams & Blake 2017 | 0.424 +0.067/−0.064 | 0.000 | FP | 6dFGS | field-level | density–velocity cross-covariance | arXiv:1706.05205 | [src] |
| Howlett et al. 2017 | 0.510 +0.090/−0.080 | 0.000 | TF | 2MTF | two-point | velocity power spectrum | arXiv:1706.05130 | [T24]; re-read |
| Johnson et al. 2014 | 0.418 ± 0.065 | 0.000 | FP+SN | 6dFGSv + low-z SNe | field-level | maximum-likelihood | arXiv:1404.3799; MNRAS 444, 3926 | [T24]; re-read, corrected (§7) |
| Ma, Branchini & Scott 2012 | 0.420 ± 0.033 | 0.000 | mix | PSCz gravity field vs peculiar velocities | vel–dens (lin) | — | arXiv:1205.4237 | |
| Lilow & Nusser 2021 | 0.367 ± 0.060 | 0.013 | mix | CF3 + 2MRS | vel–dens (lin) | constrained realisations | arXiv:2102.07291 | [src] lin; re-read |
| Boubel et al. 2024 | 0.350 ± 0.030 | 0.017 | TF | Tully-Fisher forward model | vel–dens (lin) | forward model | arXiv:2301.12648 | [src]; re-read |
| Carrick et al. 2015 | 0.401 ± 0.024 | 0.020 | mix | 2M++ | vel–dens (lin) | reconstruction | arXiv:1504.04627 | [T24] lin der |
| Davis et al. 2011 | 0.310 ± 0.040 | 0.020 | TF | SFI++ | vel–dens (lin) | reconstruction | arXiv:1011.3114 | [T24] der |
| Hollinger & Hudson 2024 | 0.362 ± 0.023 | 0.020 | mix | 2M++ (bias-corrected by 1.04) | vel–dens (lin) | reconstruction | arXiv:2312.03904; MNRAS 526, 337 | [T24] lin |
| Huterer et al. 2017 | 0.428 +0.048/−0.045 | 0.020 | SN+FP | low-z SNe + galaxy velocities | field-level | maximum-likelihood | arXiv:1611.09862; JCAP 05 (2017) 015 | [src]; re-read, corrected (§7) |
| Boruah et al. 2020 | 0.400 ± 0.017 | 0.022 | SN+TF | 465 SNe + SFI++ + 2MTF vs 2M++ | vel–dens (lin) | reconstruction | arXiv:1912.09383; MNRAS 498, 2703 | [T24] lin |
| Nusser 2017 | 0.400 ± 0.080 | 0.027 | mix | CF3 | two-point | velocity–density correlation | arXiv:1703.05324 | [T24] der |
| Nguyen et al. 2025 | 0.384 +0.094/−0.157 | 0.030 | SN | SN magnitude fluctuations × galaxies | two-point | — | arXiv:2510.07673 | |
| Qin et al. 2019 | 0.404 +0.082/−0.081 | 0.030 | TF+FP | 2MTF + 6dFGSv | two-point | momentum power spectrum | arXiv:1906.02874 | [src] |
| Said et al. 2020 | 0.338 ± 0.027 | 0.035 | FP | 6dFGS + SDSS | vel–dens (lin) | reconstruction (β → fσ8) | arXiv:2007.04993 | [src] |
| Adams & Blake 2020 | 0.384 ± 0.052 (stat) ± 0.061 (sys) | 0.045 | FP | 6dFGS | field-level | joint RSD + PV | arXiv:2004.06399 | [src] |
| Turner et al. 2023 | 0.358 ± 0.075 | 0.045 | mix | 6dFGS | two-point | velocity–density correlation | arXiv:2207.03707; MNRAS 518, 2436 | [src] |
| Dupuy et al. 2019 | 0.43 (±0.03)_obs (±0.11)_cosmic | 0.050; "<0.05" in the 2026-08-13 table | mix | CF3 | two-point | correlation | arXiv:1901.03530 | [src]; re-read |
| Courtois et al. 2023 | 0.360 ± 0.050 | 0.051 | mix | CF4 grouped | two-point | correlation function | arXiv:2211.16390; A&A 670, L15 | re-read |
| Courtois et al. 2023 | 0.300 ± 0.060 | 0.051 | SN | CF4 SNIa subset | two-point | correlation function | arXiv:2211.16390 | re-read |
| Courtois et al. 2023 | 0.380 ± 0.040 | 0.051 | mix | CF4 ungrouped | two-point | correlation function | arXiv:2211.16390 | [T24]; re-read |
| DESI Collaboration 2025, consensus | 0.4497 ± 0.0548 | 0.070 | TF+FP | DESI DR1 PV + BGS | consensus | correlated combination | arXiv:2512.03230, arXiv:2512.03231 | [src] |
| Turner et al. (DESI) 2025 | 0.391 +0.080/−0.081 | 0.070 | TF+FP | DESI DR1 PV + BGS | two-point | galaxy + momentum correlation functions | arXiv:2512.03230 | [src] |
| Lai et al. (DESI) 2025 | 0.483 +0.080/−0.043 (stat) ± 0.018 (sys) | 0.070 | TF+FP | DESI DR1 PV + BGS | field-level | maximum-likelihood fields | arXiv:2512.03229 | [src] |
| Qin et al. (DESI) 2025 | 0.440 +0.080/−0.096 | 0.070 | TF+FP | DESI DR1 PV + BGS | two-point | galaxy power spectrum | arXiv:2512.03231 | [src] |
| Franco et al. 2026 | 0.344 ± 0.105 | 0.070 | mix | CF4++ (65 331 distances) | two-point | joint real/redshift-space, Kaiser | arXiv:2605.00450 | [src] |
| Lai et al. 2023 | 0.405 +0.076/−0.071 (stat) ± 0.009 (sys) | 0.073 | FP | SDSS PV | field-level | maximum-likelihood, wide-angle + zero-point in the model | arXiv:2209.04166 | [src] |
| Lyall et al. 2024 | 0.329 +0.081/−0.083 | 0.073 | FP | 6dFGS + SDSS | two-point | correlation function | arXiv:2407.18684 | [src]; re-read |
| Qin et al. 2024 | 0.413 +0.050/−0.058 | 0.073 | FP | SDSS DR14 PV | two-point | density–momentum **cross** power spectrum | arXiv:2411.09571 | [src] |
| Feix et al. 2015 | 0.37 ± 0.13 | ~0.1 | lum | SDSS DR7, 2×10⁵ galaxies | vel–dens (lin) | galaxy **luminosity** fluctuations | arXiv:1503.05945; PRL 115, 011301 | [src] |
| Feix et al. 2017 | 0.48 ± 0.16 | ~0.1 | lum | SDSS DR13 | vel–dens (lin) | luminosity fluctuations, recalibrated photometry | arXiv:1612.07809; MNRAS 468, 1420 | [src]; re-read |
| Stahl et al. 2021 | 0.390 ± 0.022 | — | SN | DSS: 775 low-z SNe **Ia and II**, 137 via snapshot distances, vs 2M++ | vel–dens (lin) | — | arXiv:2105.05185; MNRAS 505, 2349 | [src] lin; re-read |
| Stiskalek 2026 | 0.412 ± 0.018 | — | TF+SN | 2M++; **TF + SN combined**, S₈ = 0.798 ± 0.035; FP excluded — unstable under inhomogeneous Malmquist treatment | vel–dens (lin) | — | arXiv:2509.20235; MNRAS 2026 | [src] lin |
| Turnbull et al. 2012 | 0.400 ± 0.070 | — | SN | A1 (245 SNe) vs PSCz | vel–dens (lin) | — | arXiv:1111.0631 | lin der |
| Wang et al. 2026 | 0.384 +0.116/−0.194 | — | mix | CF4 group catalogue | two-point | parallel velocity correlation function | arXiv:2604.08314 | [src] |
| Wang et al. 2026 | 0.569 +0.054/−0.060 | — | mix | CF4 | two-point | *local* growth rate, same paper — a different quantity from the row above, do not quote as "the" CF4 value | arXiv:2604.08314 | [src] |

Row notes. Hollinger & Hudson: 2023 in the 2026-08-13 table (MNRAS 526, 337), 2024 in the
2026-08-12 one; resolved to arXiv:2312.03904, *Cosmological parameters estimated from velocity–
density comparisons: calibrating 2M++*, the value theirs after correcting a reconstruction bias of
1.04 ± 0.01. Lai et al. 2023 is a measurement on the SDSS PV catalogue, not a mock. Dupuy et al.:
0.430 ± 0.114 in the 2026-08-12 table [der: √(0.03² + 0.11²) = 0.114]; Turner gives ± 0.140 (§7).
The 2026-08-13 table had only the ungrouped Courtois value. Feix: z_eff = 0.100 in the 2026-08-12
table. Turnbull, Ma et al. and Nguyen et al. are only in the 2026-08-12 table, with no code. DESI
DR1: 415 523 redshifts + 76 616 PVs, z_eff = 0.07, three estimators on **one dataset** (§1).

**Reading this table.**

- **Rows are not independent.** 6dFGSv, SDSS PV, SFI++, 2MTF, 2M++ and the low-z SNe recur across
  most of them, and CF3/CF4/CF4++ *contain* several. Never average it, and never present it as a
  set of independent constraints.
- **The four DESI DR1 rows are three estimators on one dataset plus their correlated consensus.**
  Quote the consensus; how far the 0.391–0.483 spread measures method systematics is discussed in
  `open-questions.md` §4.
- **`der` rows are circular in a test of gravity.** Carrick et al. measure Ω_m^0.55σ8, Nusser 2017
  quotes an interval on the same combination, Davis et al.'s value follows from β (Turnbull et al.
  is also flagged `der`). Calling any of them fσ8 assumes f = Ω_m^0.55, i.e. assumes GR. Exclude
  them from any growth-index or modified-gravity fit.
- **A linear template biases correlation-function results low.** Tonegawa et al. 2024
  (arXiv:2309.14457; MNRAS 529, 4787) recover fσ8 = 0.361 with a linear template against 0.376 with
  perturbation theory on the same HR4 N-body mocks — 5.2 % below the fiducial value. Many two-point
  rows here use a linear template.
- **Range and errors** (compilation's statement): 0.31 to 0.51 over 0 < z_eff < 0.08, where ΛCDM
  predicts a nearly flat fσ8 ≈ 0.45, the scatter being method and systematics, not cosmology [der,
  2026-10-20: as merged here, 0.300 (Courtois SN subset) to 0.569 (Wang local rate), z_eff to ~0.1].
  Errors run 0.017 to 0.19, a factor of ten; the tightest (Boruah 2020, 0.017; Stiskalek 2026,
  0.018; Hollinger & Hudson 2024, 0.023) are reconstruction analyses, which import an external
  density field and its systematics; correlation-function and power-spectrum errors are typically
  0.05–0.12.

### 0a. Effective redshift genuinely absent
<!-- key: effective-redshift-genuinely-absent -->

Folded on 2026-10-20 from the compilation of 2026-08-12/14, in which `[src]` meant "traced to the
paper" and `[der]` "relabelled or derived, the paper does not quote fσ8".

Five rows have no effective redshift by the authors' own choice, not a gap (re-verified paper by
paper on 2026-08-14):

- **Stiskalek 2026** — Table 1 prints "—" in the z_eff column for the Joint TFR+SNe row (the one
  quoted), in both the fiducial and the robustness block; the individual samples carry one (CF4
  TFR W1 0.017, CF4 TFR i 0.022, Pantheon+ 0.026, 6dF FP 0.035, SDSS FP 0.037). The caption
  defines it as "the mean CMB redshift of each sample", so one *could* be formed; he declines to.
- **Turnbull et al. 2012** — "a characteristic or uncertainty-weighted depth of 58 h⁻¹ Mpc"; no
  redshift. **Stahl et al. 2021** — sample cut at z < 0.07, depth ≈ 30 h⁻¹ Mpc, with the warning
  "each peculiar-velocity catalogue will have its own characteristic depth … and comparisons should
  only be made at comparable depths."
- **Wang et al. 2026** (two rows) — framed in survey depth (h⁻¹Mpc); CF4's depth is anisotropic,
  "the depth of northern sky (z∼0.1) is two times of the depth of southern sky (z∼0.05)".

Stiskalek's Fig. 4 plots literature points at sample mean redshifts he computes: **his**
assignments, not the original authors'.

### 0b. Linear against non-linear σ8
<!-- key: linear-against-non-linear-sigma8 -->

Folded on 2026-10-20 from the compilation of 2026-08-12/14 (verified there on 2026-08-13 by
reading all 35 papers rather than their abstracts), in which `[src]` meant "traced to the paper"
and `[der]` "relabelled or derived, the paper does not quote fσ8".

**Six rows report fσ8 with the *linear* σ8** (fσ8,lin or fσ8_L): Carrick et al. 2015, Lilow &
Nusser 2021, Hollinger & Hudson 2024, Boruah et al. 2020, Stahl et al. 2021, Stiskalek 2026
(Turnbull et al. 2012 is also flagged `lin` in the 2026-08-12 table). All are velocity–density
comparisons, which predict the velocity field from linear theory; the other rows write plain fσ8.
**The offset exceeds several error bars**: Carrick et al. quote fσ8,lin = 0.401 ± 0.024 (the value
tabulated here and by Turner) and fσ8 = 0.427 ± 0.026 with the non-linear σ8, 6.5 % apart. Six of
35 rows sit on the lower convention, including three of the four tightest errors (Boruah 0.017,
Stiskalek 0.018, Hollinger & Hudson 0.023): plotted against Planck's fσ8 without the convention,
they bias the low end downward — the points that drive any claim of tension.

### 0c. Forecasts and simulation validation — not measurements
<!-- key: forecasts-and-simulation-validation-not -->

Folded on 2026-10-20 from the compilation of 2026-08-12/14, in which `[src]` meant "traced to the
paper" and `[der]` "relabelled or derived, the paper does not quote fσ8".

| Reference | Value | What it is | ID |
|---|---|---|---|
| Dixon et al. 2026 | ⟨fσ8⟩ = 0.429 ± 0.038 (σ_stat 0.030, σ_sys 0.023) | **Simulated** end-to-end measurement for TITAN, ~2000 mock SNe Ia at z < 0.067 on Uchuu; recovers the input 0.428 to 0.1 %. First systematic budget for the reconstruction-and-scaling method | arXiv:2606.14962 |
| Tonegawa et al. 2024 | fσ8 = 0.361 (linear) vs 0.376 (PT) | HR4 N-body mocks; the linear-template bias of the reading notes above | arXiv:2309.14457 |
| Ravoux et al. 2025 | — | `flip` framework: field-level covariance model with wide-angle corrections + geometry-dependent Fisher forecast. No data fσ8 is reported | arXiv:2501.16852; A&A 698, A273 |
| Rosselli et al. 2025 | — | Growth-rate forecast from LSST SN peculiar velocities (10 %, `surveys-and-data.md` §4) | arXiv:2507.00157 |

**Excluded as bulk flows, not fσ8**, though often cited alongside: Watkins et al. 2023
(arXiv:2302.02028), Whitford et al. 2023 (arXiv:2306.11269), Do et al. 2026 (Hawai'i Supernova
Flows, arXiv:2606.17142); see §3. Crisman, Quartin & Rebouças 2026 (arXiv:2604.06361; Phys. Dark
Univ. 53, 102391): in scope, but quotes σ8 and γ, not fσ8 (§2). Pike & Hudson 2005: β_K = 0.49 ±
0.04 and σ8(Ω_m/0.3)^0.6 = 0.91 ± 0.12 (0.85 ± 0.05 with IRAS); fσ8 would need a value of Ω_m and
the GR growth index, one assumption beyond the `der` rows, and no such conversion is published.

---

## 1. DESI DR1 Peculiar Velocity Survey (arXiv 2025-12-02)
<!-- key: desi-dr1-peculiar-velocity-survey-arxiv-2025-12 -->

Seven companion papers. The three fσ8 values and the consensus are also in §0; the rows below
are what it does not carry. The DESI DR1 summary of the 2026-08 compilation is merged here (folded
on 2026-10-20 from the compilation of 2026-08-12/14, in which `[src]` meant "traced to the paper"
and `[der]` "relabelled or derived, the paper does not quote fσ8"): one dataset, three estimators,
"not independent measurements and must never be averaged as if they were".

| Quantity | Value | Paper | Flag |
|---|---|---|---|
| FP catalogue size | 98 292 unique early-type galaxies, z < 0.1 | Ross et al. 2025, arXiv:2512.03226 | [src] |
| FP distance precision | 26 % random error per galaxy | arXiv:2512.03226 | [src] |
| TF catalogue size | 10 262 spirals, rotation measured at 0.4 R26; 6 807 in the clustering catalogue | Douglass et al. 2025, arXiv:2512.03227 | [src] |
| TF relation | slope −7.22 ± 0.01 AB mag (r band), intrinsic scatter 0.466 ± 0.001 AB mag, calibrated in bins Δz = 0.005 over 0.03 < z < 0.1 | arXiv:2512.03227 | [src] |
| Sample entering the field-level fit | 415 523 redshifts + 76 616 velocities | Lai et al. 2025, arXiv:2512.03229 | [src] |
| Mocks | 675 realisations, used by all three estimators and for the cross-method correlations | Bautista et al. 2025, arXiv:2512.03228 | [src] |
| Consensus fσ8(z_eff = 0.07) | 0.4497 ± 0.0548 | Turner et al. 2025, arXiv:2512.03230 | [src] |
| Correlation functions | 0.391 (+0.080/−0.081) | Turner et al. 2025, arXiv:2512.03230 abstract | [src] |
| Power spectra | 0.440 (+0.080/−0.096) | Qin et al. 2025, arXiv:2512.03231 abstract | [src] |
| Maximum-likelihood fields | 0.483 (+0.080/−0.043) stat ± 0.018 sys | Lai et al. 2025, arXiv:2512.03229 abstract | [src] |
| Planck+ΛCDM value quoted for comparison | 0.449 ± 0.008 | arXiv:2512.03229 | [src] |
| Growth index, consensus + DESI DR1 full shape | γ_L = 0.580 ± 0.110 | arXiv:2512.03230; Qin et al. 2025, arXiv:2512.03231 | [src] |
| Ω_m, σ8 from the same joint fit | 0.301 ± 0.011, 0.834 ± 0.032 | arXiv:2512.03231 | [src] |
| H0, FP+TF zero-point tied to SH0ES/Pantheon+ SNe Ia | 73.7 ± 0.06 (stat) ± 1.1 (syst) km/s/Mpc | Carr et al. 2025, arXiv:2512.03232 | [src] |

**How the consensus is built** (arXiv:2512.03228, §9) [src]. Each estimator is run on the 675 mocks;
the scatter of the best fits and their Pearson correlations are

| | field-level (MLE) | power spectra | correlation functions |
|---|---|---|---|
| mean ± scatter on mocks (fiducial 0.462) | 0.461 ± 0.059 | 0.439 ± 0.054 | 0.478 ± 0.079 |
| correlation with MLE | — | (38.8 ± 3.4) % | (27.3 ± 5.6) % |
| correlation with power spectra | | — | (29.0 ± 4.3) % |

The paper comments that these "are lower than expected" — Fourier- and configuration-space growth
rates were correlated at 84 % in eBOSS — and attributes it to "different analysis choices, scale
ranges and model parametrization for each method, or the lower overall signal-to-noise ratio". The
combination follows the BOSS consensus method (code `Gacomb`), needs symmetric Gaussian errors ("we
use half of the confidence interval for each measurement"), takes the field-level statistical error
"scaled up based on results from mocks" with its systematic added in quadrature, and "has a Gaussian
posterior by construction".

Reading notes.

- The field-level and correlation-function abstracts call the three analyses consistent within 1σ
  [src: arXiv:2512.03229, arXiv:2512.03230, arXiv:2512.03231].
- The correlation-function paper quotes its companions as 0.482 +0.049/−0.026 (field-level, before
  the ×1.64 error inflation of arXiv:2512.03229 Sect. 5) and 0.443 +0.113/−0.070 (power spectra),
  not the abstract values above, which were re-read on arXiv on 2026-10-14 [src: arXiv:2512.03230,
  Sect. 4.3.5; abstracts of arXiv:2512.03229, arXiv:2512.03231]. Quote the abstracts.
- In mock units the largest pairwise difference, field-level minus correlation functions = 0.092, is
  1.1σ; the other two are 0.7σ and 0.6σ [der: σ_diff² = σ_a² + σ_b² − 2ρσ_aσ_b with the mock
  scatters and correlations of the table above, giving 0.085, 0.063, 0.082]. The spread is therefore
  what the mocks predict for three weakly correlated estimators, not evidence of a method systematic
  by itself.
- Journals [sec: INSPIRE records read 2026-10-08]: Lai et al. in JCAP, Turner et al. in Open J.
  Astrophys., Qin et al. in A&A, Carr et al. in ApJ, all dated 2026; the files of this skill
  cite them by their 2025 arXiv year.
- The H0 number is a *calibration transfer*, not an independent H0: the DESI sample supplies the
  Hubble-flow rung, the absolute scale comes from SH0ES supernovae (baseline) or SBF. Its
  statistical error (0.06) is negligible beside the 1.1 systematic, which carries the uncertainty of
  the SN distance ladder it is tied to [src: arXiv:2512.03232]. The topic belongs to
  `cosmo-distance-ladder-h0`.

---

## 2. Other measurements, mid-2025 to the snapshot
<!-- key: other-measurements-mid-2025-to-the-snapshot -->

Rows already in the fσ8 table of §0 are marked "in table"; they are listed so the 2025–2026 picture is
complete in one place, with the model each assumes.

| Result | Value | Data | Model / method | Citation | Flag |
|---|---|---|---|---|---|
| fσ8 and S8, TF + SN Ia (in table) | fσ8 = 0.412 ± 0.018 (linear σ8), S8 = 0.798 ± 0.035 | CF4 TF, Pantheon+ SNe vs 2M++ | hierarchical forward model of each indicator against a linear-theory reconstruction; flat ΛCDM, f monotonic in Ω_m | Stiskalek 2025, arXiv:2509.20235 (MNRAS 2026; "Stiskalek 2026" in §0) | [src] |
| fσ8 from SN magnitude × galaxy correlations (in table) | 0.384 +0.094/−0.157 at z = 0.03 | Pantheon+ × DESI DR1 BGS, z < 0.1 | auto- and cross-correlation functions, N-body covariance | Nguyen et al. 2025, arXiv:2510.07673 | [src] |
| σ8 from SN magnitudes alone | 0.73 ± 0.22 (Pantheon+); 0.70 +0.31/−0.38 (DES-Y5); 1.02 +0.38/−0.45 (DES-Dovekie) | SN velocity-induced magnitude covariance | flat ΛCDM | Crisman, Quartin & Rebouças 2026, arXiv:2604.06361 | [src] |
| Growth index, SN + Planck PR4, free Ω_k | γ = 0.519 +0.061/−0.099 (Pantheon+); 0.500 +0.054/−0.098 (DES-Y5); 0.525 +0.074/−0.073 (DES-Dovekie) | same | ΛCDM + γ + Ω_k | arXiv:2604.06361 | [src] |
| Curvature in the same fit | Ω_k = −0.011 ± 0.006 (Pantheon+), flatness excluded at 2.0σ; 2.6σ (DES-Y5); 1.8σ (DES-Dovekie) | same | ΛCDM + γ + Ω_k | arXiv:2604.06361 | [src] |
| β from CF4 against the internal (r < 200 h⁻¹Mpc) predicted field | β = 0.31 ± 0.01 | CF4 | linear velocity–density comparison with weighted averages | Watkins, Clark & Feldman 2025, arXiv:2512.03168 | [src] |
| H0 for which CF4 velocities are self-consistent | 75.0 ± 0.1 km/s/Mpc (a catalogue scale, not a cosmological H0) | CF4 | same | arXiv:2512.03168 | [src] |
| fσ8, CF4 groups, parallel velocity correlation (in table) | 0.384 +0.116/−0.194; "local" 0.569 +0.054/−0.060 | CF4 groups | ψ∥ estimator, MCMC | Wang et al. 2026, arXiv:2604.08314 | [src] |
| fσ8, CF4++ real- vs redshift-space clustering (in table) | 0.344 ± 0.105 at z = 0.07 | 65 331 CF4++ distances | Kaiser enhancement of ξ; **not** a velocity statistic | Franco, Courtois & Bernui 2026, arXiv:2605.00450 | [src] |
| "BAO" scale in the same paper | 132 ± 8 h⁻¹Mpc (real space), 139 ± 7 h⁻¹Mpc (redshift space) | same | empirical fit | arXiv:2605.00450 | [src] |
| Great Attractor infall from SBF | flow over ~1 sr peaking at ~1000 km/s, converging to zero at D ≈ 70 Mpc; 66 galaxies, 5 % distances | Magellan/FourStar H-band SBF, 2000 < V < 5000 km/s | kinematic | Dressler & Monson 2026, arXiv:2604.02470 | [src] |
| Vela supercluster mass | 33.8 × 10¹⁶ M_⊙, radius 70 h⁻¹Mpc, distance 189 h⁻¹Mpc | 65 518 CF4++ distances + 8 283 new ZoA redshifts (2 176 MeerKAT HI) | hybrid redshift + velocity reconstruction | Hollinger et al. 2026, arXiv:2603.09339 | [src] |
| H0 from GW170817 with DESI FP group velocities | 70.9 +6.4/−8.5 km/s/Mpc (FP); 73.4 +3.3/−3.9 (CF4 SBF velocity of NGC 4993) | 39 group galaxies | standard siren + group peculiar velocity | Amsellem et al. 2025, arXiv:2512.08818 | [src] |

Reading notes.

- The Franco et al. value sits in that table but is an RSD-type measurement (ratio of redshift-
  to real-space clustering), made possible because CF4++ gives real-space positions. It does not use
  the velocity two-point function and should not be grouped with it [src: arXiv:2605.00450].
- The β = 0.31 ± 0.01 of Watkins et al. has an error bar several times smaller than any fσ8 in the
  table of §0. The abstract does not say what the error includes; a fit against a fixed predicted
  field does not carry the variance of the density field, which dominates the error of Stiskalek
  2025 ("uncertainty dominated by the variance of the 2M++ galaxy field") [src: arXiv:2512.03168,
  arXiv:2509.20235].
- Crisman et al. quote σ8 and γ, never fσ8; a conversion would assume Ω_m and the background model.
  Leave it out of an fσ8 plot [src: arXiv:2604.06361].

---

## 3. The bulk-flow record
<!-- key: the-bulk-flow-record -->

A bulk flow is only defined together with its **window** (top-hat sphere, Gaussian, the survey's own
weights) and its **estimator**; the estimators and their defining equations are in
`physics-and-methods.md` §6. Amplitudes at different depths or with different windows are not
comparable, and the ΛCDM expectation must be computed for the same window. All directions are
Galactic.

### 3a. Distance-indicator bulk flows
<!-- key: distance-indicator-bulk-flows -->

| Reference | Data | Estimator, window | Depth | Amplitude (km/s) | Direction (l, b) | Paper's verdict vs ΛCDM | Flag |
|---|---|---|---|---|---|---|---|
| Watkins, Feldman & Hudson 2009, arXiv:0809.4041 | compilation of all major surveys | MV, Gaussian | 50 h⁻¹Mpc | 407 | (287°, 8°) | excluded at >98 % for WMAP5 (predicted 1D rms ~110 km/s) | [src] |
| Feldman, Watkins & Hudson 2010, arXiv:0911.5516 | 4 536 velocities | MV + shear + octupole | ~100 h⁻¹Mpc | 416 ± 78 | (282° ± 11°, 6° ± 6°) | "disagreement … at a high confidence level" | [src] |
| Nusser & Davis 2011, arXiv:1101.1650 | SFI++ TF | ACE (all-space constrained estimate), top-hat | 40 h⁻¹Mpc | 333 ± 38 | (276°, 14°) | consistent | [src] |
| same | same | same | 100 h⁻¹Mpc | 257 ± 44 | (279°, 10°) | consistent | [src] |
| Turnbull et al. 2012, arXiv:1111.0631 | 245 SNe Ia ("First Amendment") | MV | — | 249 ± 76 | (319° ± 18°, 7° ± 14°) | consistent | [src] |
| Feindt et al. 2013, arXiv:1310.4184 | 117 SNfactory SNe + Union2 | dipole fit in redshift shells | 0.06 < z < 0.1 | < 240 (68 % CL, along the CMB dipole) | — | contradicts a large "dark flow" | [src] |
| Hong et al. 2014, arXiv:1409.0287 | 2MTF, 2 018 spirals | χ² with Gaussian filter | 20 / 30 / 40 h⁻¹Mpc | 310.9 ± 33.9 / 280.8 ± 25.0 / 292.3 ± 27.8 | "similar to previous" | consistent at 1σ | [src] |
| Hoffman, Courtois & Tully 2015, arXiv:1503.05422 | Cosmicflows-2 | Wiener filter + constrained realisations, top-hat | 50 (150) h⁻¹Mpc | 250 ± 21 (239 ± 38) | — | consistent with the ΛCDM prior, which the method requires as a prerequisite; cosmic variance 126 (60) km/s | [src] |
| Scrimgeour et al. 2016, arXiv:1511.06930 | 6dFGSv, ~10⁴ FP | MV, hemisphere | 50 h⁻¹Mpc | 248 ± 58 | (318° ± 20°, 40° ± 13°) | consistent | [src] |
| same | same | same | 70 h⁻¹Mpc | 243 ± 58 | same | consistent | [src] |
| Qin et al. 2018, arXiv:1804.05520 | 2MTF + 6dFGSv, 10 904 galaxies | ηMLE (log-distance likelihood) | 40 h⁻¹Mpc | 288 ± 24 | (296° ± 6°, 21° ± 5°) | consistent | [src] |
| Qin et al. 2019, arXiv:1811.00822 | 2MTF + CF3 | ηMLE | 37 h⁻¹Mpc | 259 ± 15 | (300° ± 4°, 23° ± 3°) | consistent; shear 1.7 ± 0.4 h km/s/Mpc | [src] |
| Peery, Watkins & Feldman 2018, arXiv:1808.07772 | CF3 | improved MV, top-hat, H0-independent | 150 h⁻¹Mpc | 282 km/s (r⁻² weights; 252 with Gaussian weights) | — | ΛCDM expectation 128 (166); χ²(3 dof) = 9.59 (6.92), probability 2.2 % (7.4 %) | [src: Table 1] |
| Qin 2021, arXiv:2105.04800 | 2MTF | estimator on Gaussianised velocities | 30 h⁻¹Mpc | 332 ± 27 | (293° ± 5°, 13° ± 4°) | consistent | [src] |
| Watkins et al. 2023, arXiv:2302.02028 | CF4 | MV, top-hat | 150 h⁻¹Mpc | 387 ± 28 (ΛCDM expectation 139) | (297° ± 4°, −6° ± 3°) | χ² = 19.34 for 3 d.o.f., probability 0.023 % | [src: Table 1] |
| same | same | same | 200 h⁻¹Mpc | 419 ± 36 (ΛCDM expectation 120) | (298° ± 5°, −8° ± 4°) | χ² = 29.13 for 3 d.o.f., probability 0.00021 % | [src: Table 1] |
| Whitford, Howlett & Davis 2023, arXiv:2306.11269 | CF4 | Kaiser MLE | 49 h⁻¹Mpc | 408 ± 165 | towards the Great Attractor region | "reasonable agreement" | [src] |
| same | same | MVE, mock-calibrated errors | 173 h⁻¹Mpc | 428 ± 108 | same | 0.11 % probability of a larger χ² | [src] |
| Lopes et al. 2024, arXiv:2405.11077 | Pantheon+ SNe, 0.015 ≤ z ≤ 0.06 | directional H0 dipole | 102.83 ± 10.2 Mpc | 132.14 ± 109.3 | (326.1° ± 11.2°, 27.8° ± 11.2°) | dipole in H0 at > 99.9 % CL; the velocity itself is 1.2σ from zero [der: 132.14/109.3] | [src] |
| Courtois et al. 2025, arXiv:2502.01308 | CF4++ (CF4 + first WALLABY, FAST, DESI velocities) | not stated in the abstract | 150 h⁻¹Mpc | 315 ± 40 | — | homogeneity scale "not yet reached" within 200–300 h⁻¹Mpc | [src] |
| Duangchan et al. 2025, arXiv:2507.22236 | CF4 | forward model with no cosmological prior on the field, simulation-based correction from 64 mocks | ~140 and ~240 h⁻¹Mpc | (in body) | — | 3σ tension at both depths | [src] |
| Stiskalek, Desmond & Lavaux 2025, arXiv:2509.14997 | CF4 TF W1, 2MTF, SFI++, Pantheon+, z < 0.05 | forward model, radially varying velocity dipole | bulk-flow *curve* | — | — | "fully consistent with expectations from the standard cosmological model" | [src] |
| Watkins, Clark & Feldman 2025, arXiv:2512.03168 | CF4 | MV split into internal (< 200 h⁻¹Mpc) and external parts | to 200 h⁻¹Mpc | — | — | flow "dominated by sources beyond 200 Mpc/h", external part *rising* with scale | [src] |
| Nusser & Tully 2026, arXiv:2608.14265 | CF4 and each constituent catalogue | monopole + dipole in six radial bins, log-distance estimator, ΛCDM prediction for the actual positions and covariances | to 300 h⁻¹Mpc; peak bin 120–160 h⁻¹Mpc | 628 ± 82 (dipole of that bin) | towards negative supergalactic X | full range 2.29σ (dipole), 2.36σ (joint); peak bin 3.40σ, 1.56σ without 6dFGS, 3.77σ without SNe | [src] |
| Do et al. 2026, arXiv:2606.17142 | Hawai'i Supernova Flows SNe Ia, optical and NIR | two estimators × two distance estimators × two wavelength regimes | z ≲ 0.1 | ~100 to 400 depending on the choice | — | "all consistent with the predictions of ΛCDM" | [src] |

### 3b. Residual ("external") bulk flows from velocity–density comparison
<!-- key: residual-external-bulk-flows-from-velocity -->

These are a different quantity: the dipole left after subtracting the flow predicted from a
redshift-survey density field, attributed to sources outside the survey volume. They are not
comparable to §3a amplitudes.

| Reference | Density field | Residual flow (km/s) | Direction (l, b) | Flag |
|---|---|---|---|---|
| Turnbull et al. 2012, arXiv:1111.0631 | PSCz | 150 ± 43 not accounted for | — | [src] |
| Carrick et al. 2015, arXiv:1504.04627 | 2M++ (200 h⁻¹Mpc) | 159 ± 23, preferred at 5.1σ | (304° ± 11°, 6° ± 13°) | [src] |
| Springob et al. 2016, arXiv:1511.04849 | 2MRS, PSCz | ~250, falling to ~150 once the monopole zero-point offset between data and model is removed | — | [src] |
| Boruah, Hudson & Lavaux 2020, arXiv:1912.09383 | 2M++ | 171 ± 11 | (301° ± 4°, 0° ± 3°) | [src] |

Carrick et al. also give the *predicted* flow of a 50 h⁻¹Mpc Gaussian window, 230 ± 30 km/s towards
(293° ± 8°, 14° ± 10°), and a predicted Local Group velocity from the 2M++ volume alone of 540 ± 40
km/s towards (268° ± 4°, 38° ± 6°), 10° from the CMB dipole [src: arXiv:1504.04627].

### 3c. kSZ bulk flows
<!-- key: ksz-bulk-flows -->

| Reference | Data | Result | Flag |
|---|---|---|---|
| Kashlinsky et al. 2010, arXiv:0910.4958 | WMAP5 + >1 000 X-ray clusters | flow "consistent with approximately constant velocity out to at least 800 Mpc" (the "dark flow" claim, so named in arXiv:1310.4184) | [src] |
| Planck Collaboration 2014, arXiv:1303.5090 | Planck + MCXC clusters, mean z = 0.18 | no bulk flow detected; blind-search upper limit 254 km/s (95 % CL); kSZ monopole 72 ± 60 km/s; cluster radial rms < 800 km/s (95 % CL) against a linear ΛCDM value near 230 km/s at z = 0.15 | [src] |
| Gandhi et al. 2026, arXiv:2605.12499 | kSZ velocity reconstruction, WISE×SuperCOSMOS and unWISE with Planck, six bins over 0.1 ≲ z ≲ 1.5 | upper limits at 200 ≲ R ≲ 2000 h⁻¹Mpc "fully consistent with the ΛCDM bulk flow expectation"; "strong tension" with reading the CatWISE quasar dipole as a ~370 km/s flow at R ~ 1000 h⁻¹Mpc | [src] |

### 3d. How to read the record
<!-- key: how-to-read-the-record -->

- **Every tension claim in the table comes from the minimum-variance estimator applied to a
  heterogeneous compilation** — the 2009–2010 composite, then CF3 and CF4 (arXiv:0809.4041,
  arXiv:0911.5516, arXiv:1808.07772, arXiv:2302.02028) — plus the prior-free forward model of
  arXiv:2507.22236 on CF4. Every single-survey measurement at 30–70 h⁻¹Mpc in the table is reported
  as consistent with ΛCDM.
- **The significance of the CF4 excess fell by more than an order of magnitude in probability when
  the errors were calibrated on mocks**: 0.00021 % at 200 h⁻¹Mpc in Table 1 of arXiv:2302.02028
  ("less than 0.003 %" in its abstract) against 0.11 % at 173 h⁻¹Mpc (arXiv:2306.11269), because
  "the uncertainty assigned to the bulk flows from these estimators is typically underestimated"
  [src: arXiv:2306.11269]. The amplitude itself was confirmed.
- **Monopole and dipole are coupled.** Removing a monopole zero-point offset lowered the 2MTF
  residual flow from ~250 to ~150 km/s [src: arXiv:1511.04849]; a zero-point dipole of 0.087 ± 0.019
  mag in CF4 TF (odds 877:1) is better described as local flow structure than as anisotropic
  expansion [src: arXiv:2509.14997]. See `systematics.md` §1.
- **Which sub-catalogue carries the excess.** In CF4 "TFR and 6dFGS favor larger dipoles, while SDSS
  and SN favor smaller ones"; the localised 120–160 h⁻¹Mpc feature "depends strongly on the survey
  window" [src: arXiv:2608.14265].
- **Relativistic terms.** Corrections of order vz (gravitational redshift, time evolution of the
  field) bias recent estimates "toward larger values by ~10 %" according to Heinesen 2023
  (arXiv:2305.16084) [src].
- **The observer matters.** For a Local-Group-like observer the measured bulk flow differs from that
  of a random observer by up to ~20 % at R ≤ 50 h⁻¹Mpc, comparable to sample variance; sparse
  sampling, velocity errors and radial incompleteness each bias it by more than 10 % at R ≤ 100
  h⁻¹Mpc [src: arXiv:1802.03391].

---

## 4. Velocities from the kSZ effect (2025–2026)
<!-- key: velocities-from-the-ksz-effect-2025-2026 -->

The kSZ effect gives τ × v. Three estimators, with what each returns and what it is degenerate with:

| Estimator | What it returns | Degeneracy | Reference result |
|---|---|---|---|
| Pairwise kSZ | mean pairwise momentum of halo pairs vs separation | mean optical depth τ̄; the combination constrained is H0 f σ8² once τ̄ and bias are supplied | 9.3σ with 913 286 DESI DR1 LRGs × ACT DR6 + Planck (Gong et al. 2025, arXiv:2511.23417); 5σ at z ~ 0.3 with DESI DR1 BGS (Hadzhiyska et al. 2025, arXiv:2510.14135) [src] |
| Velocity-weighted stacking | gas profile around galaxies, using an *external* reconstructed velocity as the weight | accuracy of the reconstructed velocity | non-linear terms suppress the signal by 10–20 % when the stacking velocity keeps non-linear information or RSD (Ondaro-Mallea et al. 2026, arXiv:2607.23339) [src] |
| kSZ velocity reconstruction (kSZ tomography) | large-scale radial velocity modes from the anisotropy of the small-scale kSZ–galaxy correlation | velocity bias b_v (the "optical-depth degeneracy"), an overall amplitude | galaxy–velocity cross-spectrum at 17.0σ (LRG), 8.3σ (ELG), 6.8σ (QSO), first velocity auto-spectrum at 3.1σ, 20.8σ cumulative with DESI DR2 × ACT DR6 (Chaussidon et al. 2026, arXiv:2604.04867) [src] |

Facts that matter for a peculiar-velocity reader.

- **b_v is measured well below 1.** 0.45 +0.06/−0.05 (Hotinli et al. 2025, arXiv:2506.21657, DESI-LS
  × ACT DR5); A = 0.39 ± 0.04 (Lai, Kvasiuk & Münchmeyer 2025, arXiv:2506.21684, QML estimator, ACT
  DR6 × DESI-LS DR9); 0.33 ± 0.03 (McCarthy et al. 2025, arXiv:2511.15701, against the
  continuity-equation velocity of photometric LRGs) [src]. The amplitude of the velocity field is
  therefore **not** measurable by kSZ alone: fσ8 from kSZ needs an external τ. The published
  cosmological constraints from kSZ velocity reconstruction are on f_NL, through scale-dependent
  bias, not on fσ8.
- If the suppression of galaxy–electron power implied by b_v < 1 persists, the forecast f_NL gains
  from kSZ tomography "can change appreciably" (Tishue, Shiveshwarkar & Holder 2025,
  arXiv:2510.25821) [src].
- kSZ velocity reconstruction already has "lower noise on a per-mode basis than the galaxy
  auto-correlation on the largest scales" (arXiv:2604.04867) [src]: it is a large-scale-mode probe,
  complementary to distance-indicator velocities, which are a z < 0.1 probe.
- Reconstructed (not kSZ) velocities used as stacking weights are now also machine-learned: Gong et
  al. 2026 (arXiv:2609.36355) reach SNR 14.2 on the optical depth with a Transformer-reconstructed
  velocity field of DESI DR2 LRGs at z = 0.55 and 0.8 [src].

Measurements, all model-dependent through the electron profile; none is an fσ8.

| Result | Value | Data | Citation | Flag |
|---|---|---|---|---|
| Pairwise kSZ detection | 9.3σ | 913 286 DESI DR1 LRGs × ACT DR6 + Planck | arXiv:2511.23417 | [src] |
| Pairwise kSZ at low z | 5σ at z ~ 0.3 (θ_ap = 3.3′, log M⋆ > 11); constrains H0 f σ8² given τ̄ and bias | 1.6 M DESI DR1 BGS galaxies × ACT DR6 | arXiv:2510.14135 | [src] |
| Force-law index from pairwise kSZ | g ∝ 1/rⁿ with n = 2.1 ± 0.3 over 30–230 Mpc | ACT × SDSS | Gallardo et al. 2026, arXiv:2604.14327 | [src] |
| Galaxy clustering + pairwise kSZ spectrum | H0 = 70.82 +4.94/−5.01, Ω_m = 0.290 +0.092/−0.068, w0 = −1.038 +0.245/−0.437, lg τ̄ = −4.24 ± 0.10 (w0CDM) | ACT DR6 × CMASS | Li & Zheng 2025, arXiv:2510.27227 | [src] |
| kSZ velocity reconstruction, f_NL | −39 +40/−33; b_v = 0.45 +0.06/−0.05; 11.7σ | ACT DR5 × DESI-LS LRGs | arXiv:2506.21657 | [src] |
| same, QML estimator | A = 0.39 ± 0.04; 11.7σ | ACT DR6 × DESI-LS DR9 | arXiv:2506.21684 | [src] |
| kSZ × continuity-equation velocity, f_NL | −180 +61/−86 (67 % CL), consistent with zero at 95 %; b_v = 0.33 ± 0.03 (11σ) | ACT DR6 × DESI-LS LRGs | arXiv:2511.15701 | [src] |
| Spectroscopic velocity reconstruction, f_NL | 15.9 +34.6/−34.4 (68 % CL); 20.8σ cumulative kSZ detection | DESI DR2 LRG, ELG, QSO × ACT DR6 | arXiv:2604.04867 | [src] |
| Bulk flow to Gpc scales | upper limits, consistent with ΛCDM (see §3c) | Planck × WISE×SuperCOSMOS, unWISE | arXiv:2605.12499 | [src] |

History of the kSZ-velocity f_NL: −39 +40/−33 (June 2025) → −180 +61/−86 (Nov 2025, 2D photometric)
→ 15.9 +34.6/−34.4 (April 2026, spectroscopic DR2, "the tightest constraint to date derived from the
velocity field") [src: arXiv:2506.21657, arXiv:2511.15701, arXiv:2604.04867].

---

## 5. Tests of gravity and scale dependence
<!-- key: tests-of-gravity-and-scale-dependence -->

| Test | Result | Data, method | Model | Citation | Flag |
|---|---|---|---|---|---|
| Scale-dependent growth | fσ8(k, z=0) in bins Δk ~ 0.03 h Mpc⁻¹ to ~35 % each, including scales > 300 h⁻¹Mpc; no scale dependence; ~15 % combined | 6dFGSv + low-z SNe, field-level, velocity only | bias-independent | Johnson et al. 2014, arXiv:1404.3799 | [src] |
| Growth index from the bulk flow | γ = 0.495 ± 0.096 (σ8 = 0.8, Ω_m = 0.266 fixed); DGP excluded at > 99 % | SFI++ bulk flow | ΛCDM + γ | Nusser & Davis 2011, arXiv:1101.1650 | [src] |
| f(R) from the bulk flow | f_R0 must be ≤ 10⁻⁴ (10⁻³ overpredicts the 2MTF flow at 20–50 h⁻¹Mpc) | ECOSMOG simulations vs 2MTF | f(R) gravity | Seiler & Parkinson 2016, arXiv:1607.01837 | [src] |
| S8 under GR and DGP | S8 = 0.637 ± 0.054 (γ = 6/11) and 0.741 ± 0.062 (γ = 11/16); > 3σ from Planck | 6dFGS + SDSS FP vs 2M++ | Ω_m = 0.315 ± 0.007 prior | Said et al. 2020, arXiv:2007.04993 | [src] |
| nDGP and f(R) from two-point functions | r_c H0/c > 6.987 and −log10|f_R0| > 4.703 (2σ), "significantly affected by the prior" | 6dFGS + SDSS PV correlation functions | nDGP, Hu–Sawicki f(R) | Lyall et al. 2024, arXiv:2407.18684 | [src] |
| Growth index, DESI | γ_L = 0.580 ± 0.110 | DESI DR1 PV consensus + DESI DR1 full shape | ΛCDM + γ | arXiv:2512.03230 | [src] |
| Growth index, SN velocities + CMB | γ = 0.519 +0.061/−0.099 (Pantheon+) | SN magnitude covariance + Planck PR4 | ΛCDM + γ + Ω_k | arXiv:2604.06361 | [src] |
| Force law | n = 2.1 ± 0.3 | pairwise kSZ | g ∝ r⁻ⁿ | arXiv:2604.14327 | [src] |

Reading notes.

- The Said et al. S8 "tension" is an FP-versus-2M++ result, the configuration that Stiskalek 2025
  finds unstable under the Malmquist treatment; the same framework with TF + SNe gives S8 = 0.798 ±
  0.035, concordant with Planck [src: arXiv:2509.20235]. Do not quote arXiv:2007.04993 as evidence
  for suppressed growth without that caveat.
- Bulk-flow tests of gravity are degenerate with observer position: an enhancement of the growth
  rate by ~15 % is mimicked by Local-Group-like observer selection [src: arXiv:1802.03391].
- The DESI γ_L comes from a joint fit of the consensus low-redshift growth rate with the DESI DR1
  full-shape clustering data; the velocity sample contributes one 12.2 % point at z = 0.07 [src:
  arXiv:2512.03230].
- Forecast, not measurement: a kSZ-velocity analogue of E_G (the V̂_G estimator, galaxy × CMB
  lensing over galaxy × kSZ-reconstructed velocity) is predicted to reach S/N ~ 20–55 for ACT/SO ×
  DESI at z ≈ 0.73, 1.33, 1.84 [src: arXiv:2510.27605] — **forecast**.

---

## 6. History of the key numbers — what is superseded, and by what
<!-- key: history-of-the-key-numbers-what-is-superseded -->

| Quantity | Sequence | Status |
|---|---|---|
| Largest homogeneous FP sample | 6dFGSv 8 885 (arXiv:1409.6161) → SDSS PV 34 059 (arXiv:2201.03112) → DESI DR1 98 292 (arXiv:2512.03226) | DESI DR1 current; 6dFGSv is southern, SDSS PV and DESI are northern |
| fσ8 from a single homogeneous survey with density + velocity | 6dFGS 0.384 ± 0.052 ± 0.061 (arXiv:2004.06399) → SDSS PV 0.405 +0.076/−0.071 ± 0.009 (arXiv:2209.04166) → DESI DR1 consensus 0.450 ± 0.055 (arXiv:2512.03230) | not superseding each other: different volumes. DESI DR1 field-level alone is "about 30 % tighter" than SDSS PV [src: arXiv:2512.03229] |
| fσ8 from velocity–density comparison with 2M++ | 0.401 ± 0.024 (arXiv:1504.04627, as Ω_m^0.55 σ8,lin) → 0.400 ± 0.017 (arXiv:1912.09383) → 0.338 ± 0.027 with FP (arXiv:2007.04993) → 0.362 ± 0.023 after mock calibration (arXiv:2312.03904) → 0.412 ± 0.018, TF + SN only (arXiv:2509.20235) | all use the same density field; the last fits the three indicator classes in one framework and quotes the TF + SN combination |
| CF4 bulk flow at 150–200 h⁻¹Mpc | 387 ± 28 and 419 ± 36, analytic MV errors (arXiv:2302.02028) → 428 ± 108 at 173 h⁻¹Mpc, mock errors (arXiv:2306.11269) → 315 ± 40 at 150 h⁻¹Mpc in CF4++ (arXiv:2502.01308) → shell analysis, localised 3.4σ feature (arXiv:2608.14265) | amplitude stable; quoted significance fell from 0.00021 % to a 2.3σ full-range deviation |
| "Dark flow" | constant flow to ≥ 800 Mpc from WMAP kSZ (arXiv:0910.4958) → not detected, < 254 km/s (arXiv:1303.5090) → Gpc-scale limits consistent with ΛCDM (arXiv:2605.12499) | superseded |
| MV flow of the 2009–2010 compilation | 407 km/s in a 50 h⁻¹Mpc Gaussian window (arXiv:0809.4041), 416 ± 78 at ~100 h⁻¹Mpc (arXiv:0911.5516) → 257 ± 44 at 100 h⁻¹Mpc from SFI++ alone (arXiv:1101.1650) and single-survey values of 240–330 at 30–70 h⁻¹Mpc | the 2009–2010 compilation values are not reproduced by single homogeneous surveys at smaller depth; they are not directly comparable |
| DESI PV Hubble-flow H0 | 76.05 ± 0.35 ± 0.49 plus a ± 4.86 term, Coma SBF anchor, EDR (arXiv:2408.13842) → 73.7 ± 0.06 ± 1.1, SN Ia anchor, DR1 (arXiv:2512.03232) | DR1 supersedes EDR |
| kSZ-velocity f_NL | −39 +40/−33 → −180 +61/−86 → 15.9 +34.6/−34.4 (§4) | DESI DR2 × ACT DR6 current |

## 7. History of the fσ8 compilation: values corrected or removed at source
<!-- key: history-of-the-fsigma8-compilation-values -->

Folded on 2026-10-20 from the compilation of 2026-08-12/14, in which `[src]` meant "traced to the
paper" and `[der]` "relabelled or derived, the paper does not quote fσ8".

The compilation started from Turner, *Cosmology with Peculiar Velocity Surveys* (arXiv:2411.19484,
an Elsevier *Encyclopedia of Astrophysics* chapter; survey descriptions in `surveys-and-data.md`
§0–1). **Its Table 1 is not a safe source for individual values** (checked 2026-08-13): six values
disagree with the papers — five in scope, below, and Beutler 2012, out of scope — four entries are
not peculiar-velocity measurements, and its method column mixes fitting technique with observable
(`physics-and-methods.md` §0). A review may quote a different row of a paper's results table, so
this need not be an error of the review; the rate was 6 of 21 checked, 29 %.

| Paper | Turner Table 1 | Source | Comment |
|---|---|---|---|
| Said et al. 2020 | 0.311 ± 0.027 | **0.338 ± 0.027** (abstract) | the abstract gives the *combined* 6dFGS+SDSS value at z_eff = 0.035; 0.311 is likely one survey alone |
| Boubel et al. 2024 | 0.360 ± 0.030 | **0.35 ± 0.03** (abstract) | arXiv v2 abstract vs possibly the published MNRAS value |
| Dupuy et al. 2019 | 0.430 ± 0.140 | **0.43 (±0.03)_obs (±0.11)_cosmic** (abstract) | Turner combines the two error terms; the split matters, since the cosmic-variance term is irreducible |
| Turner et al. 2023 | 0.325 ± 0.075 | **0.358 ± 0.075** (abstract) | the abstract value is for 27 < s < 123 h⁻¹Mpc combining velocity and density statistics; the table presumably quotes a different scale cut of the same paper |
| Johnson et al. 2014 | 0.418 ± 0.055 | **0.418 ± 0.065** (conclusions) | 0.055 is Beutler's error, quoted in the adjacent sentence of Johnson's own text |

Values circulating in secondary summaries for the DESI DR1 PV correlation-function and
power-spectrum analyses (0.402 +0.075/−0.077 and 0.443 +0.110/−0.070) do not match the papers,
which give 0.391 +0.080/−0.081 and 0.440 +0.080/−0.096; cite the arXiv abstracts. (The
correlation-function paper itself quotes its power-spectrum companion as 0.443 +0.113/−0.070, §1.)

**Removed as out of scope** on 2026-08-13: present in Turner (2024) Table 1, absent from §0. All
four are redshift-space distortions of the 6dFGS *redshift* survey — no measured distances,
therefore not peculiar velocities; they measure the same growth rate by a different probe. The two
Achitouv values also share galaxies with each other.

| Reference | fσ8 | ID |
|---|---|---|
| Achitouv et al. 2017, galaxy–galaxy | 0.42 ± 0.06 | arXiv:1606.03092 |
| Achitouv et al. 2017, void–galaxy | 0.39 ± 0.11 | arXiv:1606.03092 |
| Beutler et al. 2012 | 0.423 ± 0.055 (Turner: 0.428 +0.079/−0.068) | arXiv:1204.4725 |
| Blake, Carter & Koda 2018 | 0.38 ± 0.12 | arXiv:1801.04969 |

**Corrected on 2026-10-20** while re-reading ten values (all ten values matched): Johnson et al.
2014's 0.418 ± 0.065 is the 6dFGSv **+ SNe** fit; 6dFGSv alone gives 0.428 +0.079/−0.068 and the
SNe alone 0.417 +0.097/−0.084 [src: arXiv:1404.3799, Sect. 5.4 and Table 3] — the indicator, given
as FP with dataset 6dFGSv in both 2026-08 tables, is now FP+SN. The 6dFGSv-alone value is the
number listed above as Turner's entry for Beutler 2012 [der: equality of the numbers only].
Huterer et al. 2017's 0.428 is for the Supercal SNe Ia and the 6dFGS FP distances "combined
appropriately" [src: arXiv:1611.09862, abstract] — indicator given as SN, now SN+FP.

## Not verified in this file
<!-- key: not-verified-in-this-file -->

- Amplitude of the Duangchan et al. 2025 bulk flow (abstract gives only a 3σ tension at ~140 and
  240 h⁻¹Mpc); the Peery et al. 2018 amplitude is now in §3a.
- The estimator behind the Courtois et al. 2025 bulk flow (abstract only).
- Any DESI DR2 peculiar-velocity result: none found up to 2026-10-08.
- §0, §0a–c, §7 and the merged sentence of §1: folded from the 2026-08 compilation, not re-read, except ten values
  re-read on 2026-10-20 (rows marked "re-read"; Johnson 2014 in Sect. 5.4 and 6, the others in the
  abstract), all matching, two indicator labels corrected (§7). Not re-read: the uncoded rows (Ma
  2012, Nguyen 2025, Turnbull 2012) and Tonegawa's 5.2 % (not in its abstract).
