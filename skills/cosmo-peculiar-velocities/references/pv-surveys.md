# Peculiar-velocity surveys — distance indicators, samples, results

Compiled **2026-08-12**; §5–6 rebuilt **2026-08-14** after every fσ8 value was
traced to its own paper. **Verify before citing**: the numbers below were read
from the sources named in each row, but any number entering a manuscript should
be re-checked against the paper itself.

Anchor review: **Turner, *Cosmology with Peculiar Velocity Surveys***,
arXiv:2411.19484, a chapter for the
Elsevier *Encyclopedia of Astrophysics*. The survey descriptions come from it,
and it is the natural single citation for a manuscript paragraph introducing the
field. **Its Table 1 is not a safe source for individual values**: six disagree
with the papers, four entries are not peculiar-velocity measurements at all, and
its method column mixes fitting technique with observable — see §5 and §6.

---

## 1. Why there are exactly three indicators

A peculiar velocity needs a **redshift-independent distance**. Only three
methods deliver them in bulk over cosmological volumes.

| Indicator | Tracer | Distance error per object | Practical reach |
|---|---|---|---|
| **Tully–Fisher (TF)** | spirals; luminosity–HI linewidth | ~20 % | z ≲ 0.1 |
| **Fundamental Plane (FP)** | early types; σ–R_e–I_e | ~20 % | z ≲ 0.1 |
| **SN Ia** | standardisable candle | ~5–7 % (σ ≈ 0.1–0.15 mag) | z ≲ 0.3 |

**The controlling fact** (Turner §3): the TF/FP scatter is a constant in
*magnitude*, so the distance error is a constant *fraction* of the distance, and
the velocity error grows linearly with distance. This is why galaxy-scaling-
relation surveys stop at z ~ 0.1–0.15 no matter how many galaxies they observe,
and why **SNe Ia are the only reliable probe of the velocity field beyond
z ≈ 0.15**.

Corollary worth stating in any manuscript: TF/FP win on *number* (10⁴–10⁵
objects at ~20 % each), SNe win on *per-object precision* and reach. They are
not competing strategies; they cover different parts of the same volume.

Other indicators (TRGB, SBF, masers, JAGB, Cepheids, GW sirens) exist but are
calibration rungs, not survey-scale velocity tracers.

---

## 2. Galaxy-scaling-relation surveys (TF / FP)

Chronological, following Turner §4.

| Survey | Method | N | z | Sky | Reference |
|---|---|---|---|---|---|
| **Mark III** | TF+FP | ~3 200 | z̄ ~ 0.015 | — | Willick et al.; first uniform re-treatment of 1980s data |
| **SFI++** | TF (I-band) | ~5 000 | z̃ ~ 0.02 | most of sky above Galactic plane | Springob et al. 2007; **erratum 2009** (morphological-type correction misapplied) |
| **6dFGSv** | FP | ~9 000 (7 030 used in some analyses) | z < 0.055 | southern, \|b\| > 10° | Springob et al. 2014; Magoulas et al. 2012 |
| **2MTF** | TF | ~2 000 | z ≲ 0.03, z̃ ~ 0.016 | near-all-sky, \|b\| > 5° | Hong et al. 2019; 2MASS + ALFALFA HI |
| **SDSS PV** | FP | >34 000 | z < 0.1, z_eff ~ 0.07 | northern | Howlett et al. 2022 |
| **Cosmicflows-4** | 8 methods | 55 877 galaxies / 38 065 groups | local | both hemispheres, non-uniform | Tully et al. 2022 |

**Notes that matter.**

- **2MTF's selling point is the Galactic plane.** Optical surveys cut at
  \|b\| > 10°; 2MTF uses infrared and reaches \|b\| > 5°, recovering structure in
  the Zone of Avoidance that otherwise biases reconstructions.
- **6dFGSv and SDSS PV are complementary by construction**: south vs north,
  similar N within the 6dFGS redshift limit, but SDSS extends to z = 0.1.
- **CF4 is a compilation, not a survey.** ~35 000 FP (mostly 6dFGSv + SDSS PV)
  and ~10 000 TF (SFI++, 2MTF and others), plus SNe Ia, SNe II and SBF. It is
  heterogeneous — different groups, different calibrations — which is exactly
  why bulk-flow results derived from it are estimator- and
  calibration-sensitive. Do not treat CF4 as an independent dataset from
  6dFGSv/SDSS/SFI++/2MTF; it largely *contains* them.

---

## 3. Supernova samples used for peculiar velocities

Two distinct uses, often confused:

1. **PV as signal** — SNe as velocity tracers to measure fσ8.
2. **PV as nuisance** — correcting SN redshifts for peculiar motion in
   Hubble-diagram cosmology.

| Sample | N | z | Note |
|---|---|---|---|
| **Pantheon+** | 1 701 light curves / 1 550 unique SNe, 18 subsamples | 0.001–2.26 | SALT2; strength is the low-z anchor. PVs reliable only at z < 0.02 (σ ≈ 300 km/s) |
| **Union3** | 2 087 SNe, 24 datasets | — | SALT3, Bayesian hierarchical errors; shares ~1 360 SNe with Pantheon+ |
| **DES-Y5** | 1 635 photometric + 194 low-z = 1 829 | 0.10–1.13 (+0.025–0.10) | dominates z > 0.5; too distant for PV work |
| **A2 (Boruah et al. 2020)** | 465 SN PVs | z < 0.067 | compared to 2M++ reconstruction, jointly with SFI++ and 2MTF |
| **DSS (Stahl et al. 2021)** | 775 low-z SNe Ia **and II**, 137 via snapshot distances | low-z | fσ8 = 0.390 ± 0.022 |
| **ZTF SN Ia DR2** | 994 at z < 0.06 (volume-limited); ~3 600 below z < 0.06 in the fuller sample | z < 0.06 | Rigault et al. 2025 overview; PV impact on the Hubble diagram in Carreres et al. 2025 |

**Sharing warning.** Pantheon+, Union3 and the PV compilations draw on the same
low-z SNe. Combining fσ8 measurements from two of them is not combining
independent data. State which low-z sample underlies a quoted fσ8.

---

## 4. Current and future

| Survey | Method | Expected N | z | Status |
|---|---|---|---|---|
| **DESI PV** | FP **and** TF | ~133 000 FP + ~53 000 TF (Saulder et al. 2023 targets) | z ≲ 0.15 | ongoing; spare-fibre programme, 14 000 deg² north. **First major survey measuring both FP and TF with one instrument**, TF from optical rather than HI |
| **WALLABY** | TF (HI, 21 cm) | ~17 000–40 000 PVs of ~324 000 detections (forecasts vary) | 0 < z < 0.10 | observing since 2022, 5-yr run, 14 000 deg² south, ASKAP |
| **4HS** (4MOST Hemisphere Survey) | FP | >400 000 early types | z < 0.15 | future; ~6 M redshifts over 17 000 deg², ~95 % completeness. **Largest FP sample ever planned** |
| **Taipan** | FP | ~45 000–80 000 (quoted figures differ) | z < 0.1 | southern; check current status before citing — largely superseded by 4HS |
| **ZTF** | SN Ia | ~10³ usable | z < 0.06 | ongoing, north |
| **LSST** | SN Ia | orders of magnitude more | z < 0.35 | starts 2026; ≥825 visits per southern field over 10 yr |

**Forecast headline** (Turner §6): current + future PV surveys will cover
almost the whole sky to z = 0.3 and deliver fσ8 to **≲ 3 %** — comparable to
current expansion-history precision. A combined WALLABY+Taipan forecast also
gives ~3 %.

---

## 5. Method families

Group peculiar-velocity results by **what the estimator does to the data before
fitting**, not by what optimiser it runs afterwards. Almost every analysis
maximises a likelihood somewhere, so "maximum likelihood" is not a family — it
is a fitting detail. Four families, and the boundaries are drawn from each
paper's own words:

| Family | What it does | Depends on | Rows |
|---|---|---|---|
| **Field-level likelihood-based inference** | the likelihood of the observed density and velocity *field values* is written through a model covariance and maximised or sampled; no summary statistic is measured first ("maximum likelihood fields") | the covariance model and its non-linear damping | 6 |
| **Two-point statistics** | a correlation function, power spectrum or momentum spectrum is *measured* from the data, then fitted | the estimator, its window, and the template used to fit it | 16 |
| **Velocity–density comparison, linear** | the velocity field is *predicted* from a redshift-survey density field by **linear theory** — directly, or through a Wiener filter / constrained realisation, which is still linear dynamics | an external density field, its bias, and linear theory | 13 |
| **Velocity–density comparison, particle forward model** | the same comparison, but the field is evolved from initial conditions by a **gravity solver on a particle field** (LPT, COLA, particle-mesh, N-body), reaching the mildly non-linear regime | the solver, its resolution, and the initial-condition prior | **0** |

The fitting technique is recorded separately: forward likelihood (Boruah 2020,
Stahl 2021), forward model (Boubel 2024), hierarchical Bayes (Stiskalek 2026,
Ma+2012), MCMC, χ². Nothing is lost by keeping the two axes apart.

**No published fσ8 comes from a particle-evolving forward model.** Every
velocity–density comparison in §6 predicts the velocity field with *linear*
dynamics. The analyses that do evolve a particle field publish reconstructions,
Bayesian evidences and cosmographies — checked 2026-08-14, none quotes fσ8:

| Paper | arXiv | why not a row |
|---|---|---|
| Graziani et al. 2019 | arXiv:1901.01818 | hierarchical Bayesian forward model of CF3, but "assumes the ΛCDM model within the linear regime" |
| Boruah, Lavaux & Hudson 2022 | arXiv:2111.15535 | "a forward-modelled velocity field reconstruction algorithm"; forward-models the distance data and Malmquist bias, reports no fσ8 |
| Valade et al. 2026 | arXiv:2602.03699 | "The dynamics are integrated with a particle-mesh gravity solver, thus probing the mildly non-linear regime" on CF4 — the clearest particle-evolving analysis, and it reports no fσ8 |
| Manticore-Local | arXiv:2505.10682 | BORG with a nonlinear gravitational solver on 2M++; Bayesian evidence comparisons, not a growth rate |

This is an open niche, not a settled question: the machinery exists on the
reconstruction side and has not been closed into a growth-rate measurement.

**"Forward model" does not imply non-linear dynamics.** In Boubel 2024,
Stiskalek 2026, Boruah 2020 and Stahl 2021 the thing being forward-modelled is
the **distance indicator** — the Tully-Fisher relation, the Malmquist bias, the
standardisation — while the velocity field is still the 2M++ linear-theory
prediction. Stiskalek's own abstract is explicit: "jointly calibrates each
distance indicator and a *linear theory* reconstruction". Likewise
"constrained realisations" (Lilow & Nusser 2021) is a Wiener filter in spherical
Fourier-Bessel space: a reconstruction, but with linear dynamics.

**Turner (2024) Table 1 conflates them** — it lists "maximum-likelihood" beside
"power spectrum" and "correlation function", i.e. one fitting label among three
observable labels. Two consequences to watch for:

- **Howlett+2017 is grouped with the maximum-likelihood analyses there, and the
  paper is not one**: it is "suitable for measuring the velocity power
  spectrum", i.e. an estimator applied and then fitted.
- **Adams & Blake 2017 is the origin of the field-level method**, per Lai+2023:
  "In the development of the maximum likelihood fields method, Adams & Blake
  (2017) were the first to simultaneously model...".

Lai+2023 and the DESI maximum-likelihood-fields analysis both name the method in
their own abstracts; take that wording over any review's classification.

---

## 6. Published fσ8 measurements from peculiar velocities

Every value traced to its own paper (no row transcribed from a review), ordered
by effective redshift. `lin` marks a result normalised to the **linear** σ8;
`der` marks a paper that never quotes fσ8 at all.

| Reference | fσ8 | family | ind. | dataset | z_eff | arXiv | flags |
|---|---|---|---|---|---|---|---|
| Adams & Blake 2017 | 0.424 +0.067/−0.064 | field-level | FP | 6dFGS | 0.000 | arXiv:1706.05205 |  |
| Howlett et al. 2017 | 0.510 +0.090/−0.080 | two-point | TF | 2MTF | 0.000 | arXiv:1706.05130 |  |
| Johnson et al. 2014 | 0.418 ± 0.065 | field-level | FP | 6dFGSv | 0.000 | arXiv:1404.3799 |  |
| Ma, Branchini & Scott 2012 | 0.420 ± 0.033 | vel–dens (lin) | mix | PSCz gravity field vs peculiar velocities | 0.000 | arXiv:1205.4237 |  |
| Lilow & Nusser 2021 | 0.367 ± 0.060 | vel–dens (lin) | mix | CF3+2MRS | 0.013 | arXiv:2102.07291 | lin |
| Boubel et al. 2024 | 0.350 ± 0.030 | vel–dens (lin) | TF | Tully-Fisher forward model | 0.017 | arXiv:2301.12648 |  |
| Carrick et al. 2015 | 0.401 ± 0.024 | vel–dens (lin) | mix | 2M++ | 0.020 | arXiv:1504.04627 | lin der |
| Davis et al. 2011 | 0.310 ± 0.040 | vel–dens (lin) | TF | SFI++ | 0.020 | arXiv:1011.3114 | der |
| Hollinger & Hudson 2024 | 0.362 ± 0.023 | vel–dens (lin) | mix | 2M++ (bias-corrected by 1.04) | 0.020 | arXiv:2312.03904 | lin |
| Huterer et al. 2017 | 0.428 +0.048/−0.045 | field-level | SN | low-z SNe + galaxy velocities | 0.020 | arXiv:1611.09862 |  |
| Boruah et al. 2020 | 0.400 ± 0.017 | vel–dens (lin) | SN+TF | 465 SNe + SFI++ + 2MTF vs 2M++ | 0.022 | arXiv:1912.09383 | lin |
| Nusser 2017 | 0.400 ± 0.080 | two-point | mix | CF3 | 0.027 | arXiv:1703.05324 | der |
| Nguyen et al. 2025 | 0.384 +0.094/−0.157 | two-point | SN | SN magnitude fluctuations x galaxies | 0.030 | arXiv:2510.07673 |  |
| Qin et al. 2019 | 0.404 +0.082/−0.081 | two-point | TF+FP | 2MTF + 6dFGSv | 0.030 | arXiv:1906.02874 |  |
| Said et al. 2020 | 0.338 ± 0.027 | vel–dens (lin) | FP | 6dFGS + SDSS | 0.035 | arXiv:2007.04993 |  |
| Adams & Blake 2020 | 0.384 ± 0.052 ±0.061ₛ | field-level | FP | 6dFGS | 0.045 | arXiv:2004.06399 |  |
| Turner et al. 2023 | 0.358 ± 0.075 | two-point | mix | 6dFGS | 0.045 | arXiv:2207.03707 |  |
| Dupuy et al. 2019 | 0.430 ± 0.114 | two-point | mix | CF3 | 0.050 | arXiv:1901.03530 |  |
| Courtois et al. 2023 | 0.360 ± 0.050 | two-point | mix | CF4 grouped | 0.051 | arXiv:2211.16390 |  |
| Courtois et al. 2023 | 0.300 ± 0.060 | two-point | SN | CF4 SNIa subset | 0.051 | arXiv:2211.16390 |  |
| Courtois et al. 2023 | 0.380 ± 0.040 | two-point | mix | CF4 ungrouped | 0.051 | arXiv:2211.16390 |  |
| DESI Collaboration 2025 | 0.450 ± 0.055 | consensus | TF+FP | DESI DR1 PV + BGS | 0.070 | arXiv:2512.03230 |  |
| Turner et al. (DESI) 2025 | 0.391 +0.080/−0.081 | two-point | TF+FP | DESI DR1 PV + BGS | 0.070 | arXiv:2512.03230 |  |
| Lai et al. (DESI) 2025 | 0.483 +0.080/−0.043 ±0.018ₛ | field-level | TF+FP | DESI DR1 PV + BGS | 0.070 | arXiv:2512.03229 |  |
| Qin et al. (DESI) 2025 | 0.440 +0.080/−0.096 | two-point | TF+FP | DESI DR1 PV + BGS | 0.070 | arXiv:2512.03231 |  |
| Franco et al. 2026 | 0.344 ± 0.105 | two-point | mix | CF4++ (65331 distances) | 0.070 | arXiv:2605.00450 |  |
| Lai et al. 2023 | 0.405 +0.076/−0.071 ±0.009ₛ | field-level | FP | SDSS PV | 0.073 | arXiv:2209.04166 |  |
| Lyall et al. 2024 | 0.329 +0.081/−0.083 | two-point | FP | 6dFGS + SDSS | 0.073 | arXiv:2407.18684 |  |
| Qin et al. 2024 | 0.413 +0.050/−0.058 | two-point | FP | SDSS DR14 PV | 0.073 | arXiv:2411.09571 |  |
| Feix et al. 2015 | 0.370 ± 0.130 | vel–dens (lin) | lum | SDSS DR7 (2e5 galaxies) | 0.100 | arXiv:1503.05945 |  |
| Feix et al. 2017 | 0.480 ± 0.160 | vel–dens (lin) | lum | SDSS DR13 | 0.100 | arXiv:1612.07809 |  |
| Stahl et al. 2021 | 0.390 ± 0.022 | vel–dens (lin) | SN | DSS: 775 low-z SNe Ia+II vs 2M++ | — | arXiv:2105.05185 | lin |
| Stiskalek 2026 | 0.412 ± 0.018 | vel–dens (lin) | TF+SN | 2M++ (FP excluded) | — | arXiv:2509.20235 | lin |
| Turnbull et al. 2012 | 0.400 ± 0.070 | vel–dens (lin) | SN | A1 (245 SNe) vs PSCz | — | arXiv:1111.0631 | lin der |
| Wang et al. 2026 | 0.384 +0.116/−0.194 | two-point | mix | CF4 groups | — | arXiv:2604.08314 |  |
| Wang et al. 2026 | 0.569 +0.054/−0.060 | two-point | mix | CF4 | — | arXiv:2604.08314 |  |

**Reading this table**

- **Rows are not independent.** 6dFGSv, SDSS PV, SFI++, 2MTF and 2M++ recur
  across most of them, and CF3/CF4/CF4++ *contain* several. Never average it,
  and never present it as a set of independent constraints.
- **The four DESI DR1 rows are three estimators on one dataset plus their
  correlated consensus.** Quote the consensus. The 0.391–0.483 spread across
  identical data is the honest measure of current method systematics — and note
  that the spread tracks the method family: the field-level estimator is high,
  the two two-point estimators lower.
- **`lin` vs plain fσ8 is not a rounding difference.** Carrick et al. quote both
  for the same data: fσ8_lin = 0.401 ± 0.024 against fσ8 = 0.427 ± 0.026, a 6.5%
  offset, larger than several error bars in the table. All six `lin` rows are
  velocity–density comparisons, which predict the velocity field from linear
  theory and so naturally constrain the linear normalisation.
- **`der` rows are circular in a test of gravity.** Carrick+2015 measures
  Ωm^0.55·σ8, Nusser 2017 quotes an interval on the same combination, Davis+2011's
  value follows from β. Calling any of them fσ8 assumes f = Ωm^0.55, i.e. assumes
  GR. Exclude them from any growth-index or modified-gravity fit.
- **A linear template biases correlation-function results low.** Tonegawa+2024
  (MNRAS 529, 4787) recover fσ8 = 0.361 with a linear template against 0.376
  with perturbation theory on the same HR4 mocks — 5.2% low. Many two-point rows
  here use a linear template.

**Six values in Turner (2024) Table 1 disagree with the source**, checked
2026-08-13: Said 2020 (0.338, not 0.311), Boubel 2024, Dupuy 2019, Turner 2023
(0.358, not 0.325), Beutler 2012, and Johnson 2014 (error 0.065, not 0.055 —
0.055 is Beutler's error, quoted in the adjacent sentence of Johnson's own text).

**Four entries carried by Turner Table 1 are not peculiar-velocity measurements
and are excluded here**: Achitouv+2017 galaxy–galaxy and void–galaxy,
Beutler+2012, and Blake, Carter & Koda 2018. All four are redshift-space
distortions of the 6dFGS *redshift* survey, with no measured distances.

**Five rows have no effective redshift, and that is the authors' own choice**,
not a gap — re-verified paper by paper 2026-08-14:

- **Stiskalek 2026** — Table 1 prints "−" in the z_eff column for the Joint
  TFR+SNe row, in both the fiducial and the robustness block, while the
  individual samples carry one (CF4 TFR W1 0.017, CF4 TFR i 0.022, Pantheon+
  0.026, 6dF FP 0.035, SDSS FP 0.037). The caption defines it as "the mean CMB
  redshift of each sample", so one *could* be formed for the joint fit; he
  declines to.
- **Turnbull et al. 2012** — localises A1 by "a characteristic or
  uncertainty-weighted depth of 58 h⁻¹ Mpc"; no redshift is quoted.
- **Stahl et al. 2021** — same convention, depth ≈ 30 h⁻¹ Mpc, with an explicit
  warning: "each peculiar-velocity catalogue will have its own characteristic
  depth … and comparisons should only be made at comparable depths."
- **Wang et al. 2026** — framed in survey depth throughout, and CF4's depth is
  anisotropic: "the depth of northern sky (z∼0.1) is two times of the depth of
  southern sky (z∼0.05)". A single z_eff would be meaningless.

Stiskalek's Fig. 4 plots literature points at sample mean redshifts he computes
himself; those are his assignments, not the original authors'.

**Pike & Hudson 2005 is not in the table.** It reports β_K = 0.49 ± 0.04 and
σ8(Ωm/0.3)^0.6 = 0.91 ± 0.12 (0.85 ± 0.05 with IRAS) — an Ωm exponent of 0.6,
normalised by 0.3. Converting to fσ8 needs both a value of Ωm and the GR growth
index, one assumption beyond what the `der` rows already carry, and no such
conversion is published.

Discussion companion: `fsigma8-pv-compilation.md`.

---

## 7. Systematics, by indicator

**Common to all**
- Malmquist / selection bias — homogeneous vs inhomogeneous; the single largest
  source of disagreement between analyses.
- log-distance vs velocity estimator bias (the ratio-of-distances estimator is
  biased; use log-distance ratios).
- Zero-point calibration, which is fully degenerate with a monopole flow.
- Non-linear velocity dispersion σ_v and the damping model.
- Coherent bulk flow × survey window.
- Fiducial-cosmology dependence and the fσ8–σ8–γ degeneracies.

**TF-specific** — inclination corrections, HI linewidth definition (W₅₀ vs W₂₀),
extinction, morphological-type corrections (the SFI++ erratum came from exactly
this), HI self-absorption.

**FP-specific** — aperture correction on σ, stellar-population and environmental
dependence of the plane, surface-brightness selection, plane evolution with z.

**SN-specific** — SALT2 vs SALT3 standardisation, host-mass step, intrinsic
scatter model, photometric vs spectroscopic classification, and — for PV work
specifically — the peculiar-velocity correction applied *to build the sample*,
which is circular if the same reconstruction is later used as the model.

---

## 8. Two live controversies

**FP disagrees with TF and SNe.** Stiskalek et al. (2026, MNRAS,
arXiv:2509.20235) run the first consistent
Bayesian analysis of all three indicator classes in one framework against 2M++.
TF + SNe give S₈ = 0.798 ± 0.035, fσ8 = 0.412 ± 0.018, **concordant with the
CMB**; the FP results are unstable under the Malmquist-bias treatment and give
systematically lower S₈. Conclusion to carry: low-z PV data do *not* reinforce
the early-vs-late S₈ tension, and FP systematics deserve scrutiny. Since FP
dominates the object counts of CF4, SDSS PV and 4HS, this matters for the whole
programme.

**The bulk flow is contested.** Watkins et al. 2023
(arXiv:2302.02028) report a 4.81σ excess at
200 h⁻¹Mpc from CF4; the result is estimator-dependent
(arXiv:2306.11269). Do not cite the excess
as established.

---

## 9. Writing rules for PV sections

- Never write "the peculiar velocity survey X measures fσ8" without the
  **effective redshift** — the compilation above spans z_eff = 0 to 0.1 and the
  values are not comparable across it.
- Name the **method family** (§5), not just "maximum likelihood": that names the
  optimiser, which nearly every analysis in the table uses. The DESI DR1 spread
  across three estimators on identical data shows why the family matters.
- State the **σ8 normalisation** when quoting a velocity–density comparison.
  Six results in the table are fσ8_lin, and the offset is 6.5%.
- When quoting CF4-based results, say that CF4 is a compilation containing the
  other samples — otherwise the reader counts the same galaxies twice.
- Distinguish **forecast** from **measurement** explicitly; much of the recent
  PV literature is forecasts (LSST, 4HS, WALLABY).
- The families have different failure modes and are not interchangeable:
  field-level inference stands on its covariance model, two-point statistics on
  the estimator and its fitting template, velocity–density comparison on an
  external density field and on linear theory. Say which one a number came from.
- Never let "forward model" imply non-linear dynamics. Four papers in the table
  forward-model the *distance indicator* against a linear-theory field; no
  published fσ8 comes from a particle-evolving forward model at all (§5).
- Do not quote a `der` row (Carrick 2015, Davis 2011, Nusser 2017) in a
  modified-gravity context: those papers measure Ωm^0.55·σ8 or β, and reading
  them as fσ8 assumes the answer.
