# Open questions — statistics beyond the two-point function

Scope: live controversies, method debates, forecasts (labelled) and stale claims.
Snapshot: 2026-10-13


## 1. Bispectrum and N-point functions
<!-- key: bispectrum-and-n-point-functions -->

### 1.1 Does the bispectrum raise or lower σ8, and by how much does it help?
<!-- key: does-the-bispectrum-raise-or-lower-sigma8-and -->

Three DESI DR1 pipelines agree that the bispectrum monopole tightens the
amplitude, but not on the size of the gain: about 20% on ln(10¹⁰A_s)
(arXiv:2603.19356), 26% on σ8 once DR2 BAO is added (arXiv:2606.23936), about
10% on σ8 and Ω_m (arXiv:2507.13433), and 4–10% on the amplitude for combined
samples (arXiv:2610.01836). The pipelines differ in compression (ShapeFit
versus direct EFT fits), bispectrum model, priors and scale cuts. Part of
the spread is a matter of baseline: the 26% compares P_0,2,4 (k < 0.15) + B_0
with a power-spectrum-only analysis using P_0,2 to k = 0.20 and a finer
binning (arXiv:2606.23936, Sect. 3.2), so it is not the gain at fixed
power-spectrum data vector, as arXiv:2610.01836 (Sect. 6.2) points out; the
same paper finds 5% on σ8 for its combined LRG sample at fixed P_0 + P_2, and
shows that single-tracer gains (up to 20% on the amplitude) shrink when
tracers are combined (Table 3). The bispectrum scale ranges also differ:
k < 0.08 (arXiv:2507.13433), 0.12 (collaboration), 0.20 on diagonal
configurations (arXiv:2610.01836). On BOSS, the same
data gave σ8 = 0.722 +0.032/−0.036 in the window-free P + B0 analysis
(arXiv:2112.04515) and 0.794 ± 0.037 with a one-loop bispectrum
(arXiv:2206.08327); the two analyses differ in loop order, scale cuts and priors, and the
abstracts do not reconcile them.

### 1.2 Simulation-based priors
<!-- key: simulation-based-priors -->

Priors on EFT parameters learned from HOD mocks sharpen constraints
(arXiv:2507.00118; the f_NL^equil error falls from 390 to 230 in
arXiv:2512.04266 when BOSS and such priors are added [src: abstract]). The objection is that
the result then inherits the HOD family's assumptions; the sibling skill
`cosmo-galaxy-clustering` records σ8 = 0.766 ± 0.015 from such priors (Chudaykin et al. 2026, arXiv:2602.18554, abstract) against
0.842 ± 0.034 from the collaboration analysis (DESI Collaboration 2024, arXiv:2411.12022, abstract).

### 1.3 Parity violation
<!-- key: parity-violation -->

Side A: a parity-odd 4PCF excess at 7.1σ in BOSS CMASS (arXiv:2206.03625, abstract) and
4–10σ in the DESI DR1 LRG auto analysis (arXiv:2508.09133, abstract); a BAO feature in
the odd 4PCF is proposed as a decisive test (Hou, Slepian & Jamieson 2024,
arXiv:2410.05230). Side B: the excess disappears with N-body mocks
(arXiv:2401.09523), with statistics free of the 8PCF bias (arXiv:2407.03397),
in cross-patch correlations (arXiv:2508.09133), in kurto spectra
(arXiv:2604.06021), and no inflationary template fits (arXiv:2210.16320). What
decides: DESI DR2 with larger sets of high-fidelity mocks.

### 1.4 Trispectrum
<!-- key: trispectrum -->

A full-shape trispectrum pipeline now exists and is validated on simulations
(arXiv:2610.08908); the **forecast** gain for a DESI-like volume is up to 15%
on ω_cdm [src: abstract]. No data application yet.

## 2. Cosmic voids
<!-- key: cosmic-voids -->

### 2.1 Are the void AP constraints as tight as quoted?
<!-- key: are-the-void-ap-constraints-as-tight-as-quoted -->

Side A: the void–galaxy cross-correlation gives D_M/D_H more precisely than BAO
in the same data, a factor of about 3.5 in BOSS CMASS (arXiv:1904.01030, abstract), and
the combination with galaxy clustering shrinks the allowed parameter volume by
55% in eBOSS (arXiv:2008.06060, abstract). Side B: three later studies from overlapping
author lists show effects of the same order as the statistical error: the
velocity-profile mismatch (arXiv:2206.14120), the finder's response to the
fiducial cosmology (arXiv:2407.02699), and the dependence on reconstruction
(arXiv:2302.05302). No SDSS reanalysis including the finder-response correction
was found this session. What decides: a DESI analysis with the corrected
model; none was found.

Qualification from the paper bodies (2026-10-13). The finder-response paper
itself states that arXiv:2008.06060, arXiv:2007.09013 and arXiv:2205.06258
"correctly accounted for this bias" through their fiducial-cosmology
systematic term (arXiv:2407.02699, Sect. 6); in those budgets the term is
0.8% on α_⊥/α_∥ for Ω_m = 0.35 against 0.286 (arXiv:2008.06060, Sect. 6.2)
and a scatter of 0.0061 against statistical errors of 0.019–0.052
(arXiv:2205.06258, Table 3). The bias pulls ε towards 1, that is towards
the fiducial model, so it matters most for a test of a cosmology far from
the fiducial one. The 2019 BOSS CMASS result (arXiv:1904.01030) is not in
that list. A second, separate dispute is whether reconstruction is needed at
all (arXiv:2007.07895, Sect. 4.3.1, against arXiv:1805.09349).

### 2.2 Calibrated or calibration-free
<!-- key: calibrated-or-calibration-free -->

The two BOSS results from one paper, f/b = 0.540 ± 0.091 and 0.347 ± 0.023,
show how much of the constraining power can come from the mocks
(arXiv:2007.07895, abstract). A referee should ask which is quoted.

### 2.3 The w < −1 pull
<!-- key: the-w-1-pull -->

Voids plus galaxies in SDSS give w = −1.50 +0.43/−0.28 and Ω_m = 0.391 in wCDM
(arXiv:2303.06143, abstract); the VSF gives w = −1.1 ± 0.2 (arXiv:2212.03873, abstract) and
−1.263 +0.329/−0.396 (arXiv:2501.07817, abstract). None is significant; they should not
be cited as support for phantom dark energy.

### 2.4 Growth from the void–forest cross-correlation
<!-- key: growth-from-the-void-forest-cross-correlation -->

The first measurement gives the forest β around voids at z = 2.49
(arXiv:2203.11045, abstract). Open: whether a growth-rate constraint can be extracted,
given that forest RSD in the auto- and cross-correlations fail mock validation
for fσ8 (recorded in `cosmo-lyman-alpha`). A void–Lyα RSD Letter by the same
author is in preparation and is not citable.

### 2.5 Forecasts (all **forecast**)
<!-- key: forecasts-all-forecast -->

| Probe | Forecast | Reference |
|---|---|---|
| Euclid void–galaxy CCF with reconstruction | D_M/D_H to about 0.3%, fσ8 to 5–8% in each of four bins, ΔΩ_m = ±0.0028, w to 6% | arXiv:2302.05302, abstract |
| Euclid VSF | w to better than 10%; FoM(w0, wa) = 17 with only Σm_ν additionally free | arXiv:2205.11525, abstract |
| Euclid photometric void clustering × lensing | cross-correlation improves constraints by 10–15%, FoM by 10% to 25% | Bonici et al. 2023, arXiv:2206.14211, abstract |
| Void lensing for Σm_ν; voids for ultra-light axions | simulation studies, no number read | Xu et al. 2026, arXiv:2603.09278; London et al. 2026, arXiv:2602.22990 |

### 2.6 Stale or fragile claims
<!-- key: stale-or-fragile-claims -->

- "Voids give a 1% AP measurement free of systematic errors": see §2.1.
- "Void lensing is low": resolved for DESI Legacy LRG voids by matched mocks,
  A_κ = 1.016 ± 0.054 (arXiv:2412.02761; proceedings summary Sartori 2026,
  arXiv:2605.19763).
- A claimed sign change of the ISW effect in voids at z < 0.03 (Hansen et al.
  2025, arXiv:2506.08832, abstract) is a single-group result with an amplitude an order
  of magnitude above the ΛCDM expectation; treat as unconfirmed.

## 3. Alternative statistics and their validation
<!-- key: alternative-statistics-and-their-validation -->

### 3.1 Are the factor 2–6 gains real?
<!-- key: are-the-factor-2-6-gains-real -->

Side A: three statistics on BOSS CMASS (DSC, WST, MFs) return σ8 and fσ8
consistent with each other and with Planck, with errors 2–6 times smaller than
the two-point function in the same pipeline (arXiv:2309.16541,
arXiv:2310.16116, arXiv:2501.01698), and several passed a parameter-masked
challenge (arXiv:2405.02252). Side B: the three share one sample, one
simulation suite and one galaxy–halo family, so their agreement is not
independent confirmation; the challenge mocks were themselves HOD mocks and
the challenge paper states that it does not validate the error bars; the
SimBIG analysis, tested against a different N-body code, halo finder and
occupation model, found σ8 not robust at small scales (arXiv:2310.15250); DESI multiplets show the standard HOD failing on a
higher-order statistic (arXiv:2511.15354). Missing: a DESI application of any
of them, and a blinded data analysis. Neither was found this session.

### 3.2 Which statistic?
<!-- key: which-statistic -->

No ranking exists. The Beyond-2pt paper declines to give one because priors,
scale cuts and volumes differ (arXiv:2405.02252). Its summary does say
that, with θ_* fixed, density split, EFT P + B and the hybrid-EFT power
spectrum give similar errors on Ω_m, "implying that ... the bulk of the
information comes from quasi-linear (BAO) scales", and that the tightest σ8
errors come from kNN and the hybrid-EFT emulator (Sect. II.1). For neutrino mass, the
marked power spectrum's advantage over P + B disappears at realistic tracer
density (arXiv:2411.14377).

### 3.3 What a second round of the challenge needs
<!-- key: what-a-second-round-of-the-challenge-needs -->

Stated or implied by arXiv:2405.02252: observational systematics (the first
round had none), non-HOD galaxy models, a test of error-bar calibration, and
field-level inference in redshift space with free cosmology (it took part only
in real space with σ8 free).

## 4. Higher-order weak lensing
<!-- key: higher-order-weak-lensing -->

### 4.1 Does third-order shear sharpen or reopen the S8 tension?
<!-- key: does-third-order-shear-sharpen-or-reopen-the-s8 -->

KiDS-Legacy 2+3-point: within 1σ of Planck (arXiv:2606.12389, abstract). DES Y3
2+3-point: 2.3σ (arXiv:2508.14018, abstract). HSC Y3 2+3-point: 3.2σ, an increase over
its two-point result (arXiv:2508.14019, abstract). The three use the same statistic and
closely related pipelines (two share authors). The spread therefore reflects
the underlying catalogues and redshift calibrations, which for HSC Y3 have
since been revised (see `cosmo-weak-lensing`). No HSC Y3 2+3-point reanalysis
with the revised redshifts was found.

### 4.2 How much information is there beyond two-point?
<!-- key: how-much-information-is-there-beyond-two-point -->

Data-based figures of merit: +80% to +111% for 2+3-point in the Ω_m–S8 plane
(arXiv:2508.14019, arXiv:2508.14018), more than double in KiDS-Legacy
(arXiv:2606.12389), +70% to +90% for SBI with several statistics
(arXiv:2405.10881), almost a factor 3 in (Ω_m, S8, w) for the hybrid analysis
(arXiv:2606.11309). The gain is mostly in Ω_m, by breaking the Ω_m–σ8
degeneracy; S8 itself improves modestly (about 25% in HSC Y1,
arXiv:2409.01301).

### 4.3 Is the baryon robustness real?
<!-- key: is-the-baryon-robustness-real -->

HSC Y1 finds differences ≤ 0.5σ down to 2′, "or it is canceled by other
scale-dependent systematics" (arXiv:2403.03807, abstract). That caveat is the open
question for Stage IV, where the statistical error will be several times
smaller.

### 4.4 What the next data decide
<!-- key: what-the-next-data-decide -->

DES Y6 higher-order analyses are announced (arXiv:2606.11309). Stage-IV
status and dates are in `cosmo-weak-lensing`.

## 5. Field-level inference
<!-- key: field-level-inference -->

### 5.1 How much information lies beyond the power spectrum and bispectrum?
<!-- key: how-much-information-lies-beyond-the-power -->

Side A (LEFTfield group). On identical modes of simulated halos, sampling the
initial conditions improves σ8 by factors 3.5–5.2 over a simulation-based
P + B analysis at k_max = 0.10–0.12 h Mpc⁻¹ (arXiv:2403.03220, abstract); in redshift
space for a DESI-LRG-like sample the amplitude is twice as precise, up to
three times in extended models (arXiv:2609.16719, abstract); a controlled toy model
shows the loss of fixed summaries growing with non-linearity and with falling
noise (arXiv:2606.18227); for f_NL^loc the gain is about 1.3
(arXiv:2603.20855, abstract).

Side B (perturbative-likelihood group). With an analytic P + B (+ T)
likelihood the errors match the field-level ones on large scales; the
trispectrum adds 20–30%; the discrepancy is attributed to the likelihood-free
P + B baselines being too weak, not to the field-level errors being too small
(arXiv:2507.05378; 20–30% read in the abstract). With cosmology free, field-level errors are "comparable"
to P + B (arXiv:2509.09673).

State of play: both sides agree on the field-level error bars and disagree on
the P + B error bars. Note that the redshift-space gain of arXiv:2609.16719
uses a Fisher forecast for P + B. Neither side has applied the method to
survey data.

### 5.2 Has field-level inference delivered cosmology from data?
<!-- key: has-field-level-inference-delivered-cosmology -->

With sampled initial conditions: no parameter constraint was found; the data
products are fields (arXiv:1806.11117, arXiv:1909.06396, arXiv:2505.10682,
arXiv:2602.02363). In the Beyond-2pt challenge it took part only in real space
with σ8 as the single free parameter (arXiv:2405.02252). With neural
compression: yes, on 10% of BOSS (arXiv:2310.15256; the 10% is read in the abstract of the companion paper arXiv:2310.15243). With a Gaussian
likelihood: yes, for fσ8 from velocities (`cosmo-peculiar-velocities`).

### 5.3 Local-Universe implications
<!-- key: local-universe-implications -->

Manticore-Local finds "no evidence for a large local underdensity"
(arXiv:2505.10682). This bears on local-void explanations of the Hubble
tension, treated in `cosmo-distance-ladder-h0`.

### 5.4 Neural BAO reconstruction
<!-- key: neural-bao-reconstruction -->

LiFT claims an effective-volume gain of 1.2–2.0 on DESI DR1 LRGs
(arXiv:2609.14862). Open: whether a collaboration will adopt a learned
reconstruction in a blinded BAO analysis, and how its theory-systematic budget
compares with the 0.1–0.2% of standard reconstruction (figure from
`cosmo-galaxy-clustering` [sec]).

## 6. Simulation-based inference
<!-- key: simulation-based-inference -->

- **Not yet on DESI.** No SBI analysis of DESI galaxy clustering was found in
  date-sorted searches. The SimBIG papers contain forecasts for DESI, PFS and
  Euclid (arXiv:2310.15246); the abstract gives no number.
- **Promise against delivery.** The marked power spectrum went from a
  forecast factor above 2 (matter, Fisher; arXiv:2001.11024, abstract) to 1.2 on σ8 only
  (galaxies, data; arXiv:2404.04228, abstract) and to no advantage over P + B at BOSS
  density in an analytic study (arXiv:2411.14377).
- **Halo finder dependence** of the bispectrum σ8 (arXiv:2309.15071) has no
  agreed mitigation.

## 7. Misconceptions and stale claims
<!-- key: misconceptions-and-stale-claims -->

| Claim still seen | Correction | Reference |
|---|---|---|
| "Parity violation detected at 7σ in BOSS" | The excess is against Patchy mocks; 1.4σ with N-body mocks, 0–2.5σ with 8PCF-free statistics, null in cross-patch and compressed analyses | arXiv:2401.09523 (abstract), arXiv:2407.03397 (abstract), arXiv:2508.09133, arXiv:2604.06021 |
| "The BOSS bispectrum shows γ 2.7σ from GR" | A 2016 result with Planck 2015; DESI DR1 P + B gives μ0 = 0.12 ± 0.49 (Sect. 4.2.6; the arXiv listing abstract gives ± 0.51), consistent with GR | arXiv:1606.00439 (abstract), arXiv:2606.23936 |
| "The bispectrum strengthens the DESI dark-energy signal" | It shifts DESI-only w0wa towards Λ and weakens the evidence relative to P alone | arXiv:2606.23936 |
| "Voids give a 1% AP distance free of systematics" | Finder response to AP, velocity-profile mismatch and reconstruction dependence were quantified afterwards; the later SDSS analyses carry a fiducial-cosmology term that the finder-response paper judges adequate | arXiv:2407.02699, arXiv:2206.14120 |
| "Void lensing is low compared with ΛCDM" | A_κ = 1.016 ± 0.054 with matched mocks | arXiv:2412.02761, abstract |
| "The marked power spectrum gives a 4σ neutrino-mass detection" | Fisher forecast for matter in 1 (h⁻¹Gpc)³; on BOSS data the gain is 1.2× on σ8 only | arXiv:2001.11024, arXiv:2404.04228 (abstract) |
| "Higher-order statistics passed a blind challenge, so their errors are validated" | The challenge tested bias of the mean on HOD mocks and says explicitly that it does not validate uncertainties | arXiv:2405.02252 |
| "Field-level inference gives 3–5 times better σ8" | True against an SBI P + B baseline on simulated rest-frame halos; disputed against an analytic P + B (+ T) likelihood; no data application | arXiv:2403.03220, arXiv:2507.05378, arXiv:2509.09673 |
| "BORG measures cosmological parameters from 2M++ or BOSS" | The papers report reconstructed fields and quote no cosmological parameter | arXiv:1806.11117, arXiv:1909.06396 |
| "HSC Y3 third-order shear confirms a 3σ S8 tension" | Predates the HSC Y3 redshift recalibration recorded in `cosmo-weak-lensing`; KiDS-Legacy 2+3-point is within 1σ of Planck | arXiv:2508.14019, arXiv:2606.12389 |
| "w < −0.8 from DES Y3 map-level inference favours w ≈ −1" | One-sided limit w < −0.80 (abstract) against a prior edge at w = −1 (Sect. 4.2) | arXiv:2403.02314 |
| "The void–forest β = 1.21 is a growth-rate measurement" | It is the forest RSD parameter around voids | arXiv:2203.11045, abstract |

## 8. What the next data will decide
<!-- key: what-the-next-data-will-decide -->

- DESI DR2 full shape with the bispectrum: whether the amplitude gain (from 4% in arXiv:2610.01836 to 26% in arXiv:2606.23936, both abstract, depending on pipeline) converges between pipelines.
- DESI DR2 parity-odd 4PCF with cross-patch statistics and N-body mock sets.
- A DESI or Euclid void–galaxy analysis with the AP-response correction:
  whether the 0.3% **forecast** on D_M/D_H (arXiv:2302.05302, abstract) survives.
- DES Y6 higher-order lensing (arXiv:2606.11309) and an HSC Y3 2+3-point
  rerun with revised redshifts.
- A field-level or SBI cosmology from DESI galaxy clustering: none exists.
- A second Beyond-2pt round with systematics and non-HOD galaxies.

## Not verified
<!-- key: not-verified -->

Items looked for and not found, or known to exist but not read this session.
None of them should be asserted from this skill.

- A DESI DR1 or DR2 void–galaxy AP/RSD cosmology paper (two searches, none
  found).
- Any kNN cosmological constraint from survey data.
- An SBI or field-level cosmological-parameter analysis of DESI galaxy
  clustering.
- Explicit (initial-condition sampling) field-level lensing on survey data.
- (Closed 2026-10-13, abstracts only.) DES Y3 peaks (arXiv:2110.10135),
  KiDS-1000 density split (arXiv:2208.02171) and 2+3-point
  (arXiv:2309.08602), HSC Y1 PDF and peaks (arXiv:2304.05928,
  arXiv:2308.10866), Euclid HOWLS (arXiv:2301.12890): see `results.md` §4.
  The values of the KiDS-1000 2+3-point analysis were not read.
- Void ISW stacking results from DES, and the supervoid literature.
- The SimBIG skew-spectra numbers. (The first SimBIG power-spectrum paper,
  arXiv:2211.00723, and the AbacusSummit, CosmoGrid and PT Challenge
  reference papers were read in abstract on 2026-10-13.)
- The SDSS-II bispectrum measurements. (Foundational bispectrum papers and
  the IRAS and 2dFGRS measurements were added on 2026-10-13, from abstracts:
  `physics-and-methods.md` §1.1.)
- Blinding status of each individual data analysis: read for
  arXiv:2503.09714, arXiv:2606.12389, arXiv:2606.11309 and arXiv:2508.14018
  (`physics-and-methods.md` §7.1); not read for the void, density-split,
  wavelet and Minkowski-functional analyses.
- Numbers behind "biases in the recovered parameters" for the void-finder AP
  response (arXiv:2407.02699): Sect. 5.1 and 6 give the direction (towards
  ε = 1) and the dependence on the finder, shown in figures; no number is
  quoted in the text read.
- (Closed 2026-10-13.) arXiv:2508.14019 uses the original HSC Y3 redshift
  distributions with flat priors on the shifts of the two high-redshift
  bins, not DESI clustering redshifts (Sect. II.1.2, IV.2.2; see
  `results.md` §4).
- The Lyα forest compressed bispectrum (arXiv:2510.23597) and the DES Y3
  lensing-plus-clustering map-level design paper (arXiv:2511.04681): only the
  first lines of the abstracts were read.
