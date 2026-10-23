# Type Ia supernova cosmology — open questions, tensions and stale claims

Scope: live controversies with both sides cited, internal tensions between
analyses, method debates, what the next data will decide (forecasts labelled),
and the misconceptions that still circulate with the paper that corrects each.
Snapshot: 2026-10-20

Flags: `[src]` read in the cited paper this session; `[sec]` from a named
secondary source; `[der]` derived here.

## 1. Is the evidence for evolving dark energy a supernova systematic?
<!-- key: is-the-evidence-for-evolving-dark-energy-a -->

This is the question that drove the field from 2024 to 2026. The physics
interpretation belongs to `cosmo-dark-energy-modified-gravity`; the
supernova side is here.

### 1.1 The case that it was (2024–2025)
<!-- key: the-case-that-it-was-2024-2025 -->

- **Sample dependence.** With DESI DR1 BAO and CMB the preference for
  `w0waCDM` was 2.5, 3.5 or 3.9 sigma for Pantheon+, Union3 or DES-SN5YR
  (DESI Collaboration 2024, arXiv:2404.03002), and 2.8, 3.8, 4.2 sigma with
  DR2 (DESI Collaboration 2025, arXiv:2503.14738) `[src]`. Three samples
  sharing most of their low-z supernovae should not differ this much for
  statistical reasons.
- **Low-z/high-z offset.** Efstathiou 2024 (arXiv:2408.07175) compared SNe
  common to DES-SN5YR and Pantheon+ and found a ~0.04 mag offset between
  low and high redshift; an offset of that order reconciles DES-SN5YR with
  Planck LCDM `[src]`.
- **The anchor drives it.** Notari, Redi & Tesi 2024 (arXiv:2411.11685):
  combining Pantheon+ and DES-SN5YR while removing common SNe from one or
  the other gives 3.8 or 2.5 sigma; the preference is driven by the low-z SNe
  common to both, which have smaller errors in DES-SN5YR `[src]`. Huang et
  al. 2025 (arXiv:2502.04212): an intercept diagnostic shows a discrepancy
  between the low-z and DES parts of DES-SN5YR, absent in Pantheon+;
  correcting it brings the preference below 2 sigma `[src]`.
- **Evidence ratio.** Ormondroyd et al. 2025 (arXiv:2509.13220): a
  low-z/high-z magnitude offset in DES-SN5YR is preferred by the Bayesian
  evidence over flexible dark energy, and removes most of the DES–DESI
  tension `[src]`.
- **Direction of known systematics.** Dhawan, Popovic & Goobar 2024
  (arXiv:2409.18668): calibration, dust and progenitor evolution, and the
  Milky Way extinction law all move `w0`–`w_a` from LCDM *toward* the DESI
  result `[src]`.

### 1.2 The case that it was not
<!-- key: the-case-that-it-was-not -->

- Vincenzi et al. 2025 (arXiv:2501.06664) reproduce the 0.04 mag offset and
  split it: 43 % from DES improvements in intrinsic-scatter and host
  modelling (inside the DES systematic budget), 38 % from comparing
  bias-corrected distances of subsets with different selection functions.
  Using the Pantheon+ scatter model and host properties, the DES-SN5YR
  preference drops only from 3.9 to 3.3 sigma `[src: abstract]`.
- DESI + CMB without any supernovae: 3.1 sigma (arXiv:2503.14738); the full
  DES combination without SNe: 2.6 sigma (DES Collaboration 2026,
  arXiv:2605.27221) `[src]`.

### 1.3 Where it stands in October 2026
<!-- key: where-it-stands-in-october-2026 -->

Both sides were partly right. Two real supernova systematics were found and
fixed, and both reduced the *spread* between samples:

1. Calibration and an extinction-law implementation error in the DES
   analysis: DES-Dovekie, 4.2 → 3.2 sigma (Popovic et al. 2025,
   arXiv:2511.07517) `[src: abstract]`.
2. Inconsistent host-mass estimates between low and high redshift: Union3.1,
   3.8 → 3.4 sigma; and the same correction applied to Pantheon+ *raises*
   it, 2.8 → 3.2 sigma (Hoyt et al. 2026, arXiv:2601.19424) `[src: abstract]`.

After both, the three samples give 3.2–3.4 sigma with DESI DR2 and Planck,
and the merged Unite sample gives 3.3 sigma (MAP) with a Bayesian evidence
that its authors call a "weak" preference (Camilleri et al. 2026,
arXiv:2609.05053) `[src]`. What remains open:

- **The anchor still controls the answer.** Removing z < 0.1 from Unite
  shifts the best fit by ~2 sigma `[src]`. No analysis has yet replaced the
  historical anchor by a modern one.
- **Frequentist 3 sigma vs "weak" Bayesian evidence** on the same data. The
  DES-Dovekie paper argues the two statements are consistent: with a 5 sigma
  threshold neither rejects LCDM `[src]`.
- **Systematic errors are not statistical.** The Unite authors caution that
  about half of each SN error bar is systematic, including model choices,
  and that converting it to a Gaussian significance "is prone to over
  interpretation" `[src]`.
- **Ormondroyd et al.** find that Dovekie "partially alleviates" the
  DES–DESI tension "but does not eliminate it" `[src]`.
- No independent group has yet published a critique of Unite or of the
  Union3.1 host-mass correction that this session's date-sorted searches
  found; absence of critique after one month is not confirmation.

## 2. Is the host step dust, intrinsic, or a symptom of two populations?
<!-- key: is-the-host-step-dust-intrinsic-or-a-symptom-of -->

| Position | Evidence | Reference |
|---|---|---|
| Dust: host-dependent `R_V` and reddening explain the step and the colour-dependent scatter | 11 sigma colour dependence of scatter; step dependence on colour at 4.5 sigma `[src]` | Brout & Scolnic 2021, arXiv:2004.10206 |
| Mostly intrinsic | ZTF volume-limited: no evolution of the step with colour; reddening above `c >= 0.2` is dust but the step is not `[src]` | Ginolin et al. 2024, arXiv:2406.02072 |
| Intrinsic, confirmed with a dust-aware SED model | Step `0.103 ± 0.018 mag` with dust fitted jointly; mean `R_V` equal across environments within 0.2 `[src]` | Ginolin et al. 2026, arXiv:2605.06799 |
| No dust-law difference | `R_V = 2.84 ± 0.31` in low-mass and `2.58 ± 0.23` in high-mass hosts of 157 Foundation SNe `[src: abstract]` | Thorp et al. 2021, arXiv:2102.05678 |
| Both | Intrinsic step at 3.1 sigma together with a ~2 sigma `R_V` difference `[src]` | Grayling et al. 2024, arXiv:2401.08755 |
| Two populations; the step is redundant | Low-stretch population brighter by `0.14 ± 0.03 mag` at `x1 = 0`, steeper `alpha` by `0.064 ± 0.023`, different `R_B` (3.89 ± 0.29 vs 3.08 ± 0.08) `[src: abstract]` | Wojtak et al. 2026, arXiv:2606.17802 |
| Two populations inside a cosmology analysis | Residual mass step consistent with zero for unreddened SNe; errors on cosmology shrink `[src]` | Rubin et al. 2026, arXiv:2601.19854 |
| Against two populations at high redshift | log10 Bayes factor +1.9 against, on DES-SN5YR with an SBI dust model `[src]` | Popovic et al. 2026, arXiv:2607.28725 |
| Age-driven `R_V` step | Galaxy forward model: `R_V` step with galaxy age fits best; an intrinsic age–luminosity step is mostly absorbed by `alpha` `[src]` | Wiseman et al. 2022, arXiv:2207.05583 |

Why it matters for cosmology rather than only for SN physics: the two
explanations predict different redshift evolution of the correction, and the
BBC baseline (dust) and the UNITY baseline (colour-split `beta`, now two
populations) encode different choices. The non-linear stretch relation found
by ZTF (broken `alpha`, 13.4 sigma; arXiv:2405.20965) is not yet in any
BBC cosmology analysis; UNITY has modelled non-linear standardisation since
2015 (arXiv:1507.01602).

A consequence for the distance ladder: remodelling the SH0ES SNe with two
populations and Milky-Way-like dust gives `H0 = 70.59 ± 1.15` (Wojtak &
Hjorth 2025, arXiv:2506.22150), against 73.04 ± 1.04 (Riess et al. 2022,
arXiv:2112.04510) `[src]`. This is a single-group result; see
`cosmo-distance-ladder-h0`.

## 3. Does progenitor age evolution bias the Hubble diagram?
<!-- key: does-progenitor-age-evolution-bias-the-hubble -->

- **Yes, strongly**: Kang et al. 2020 (arXiv:1912.04903), a correlation of
  standardised luminosity with population age in early-type hosts at 99.5 %
  confidence `[src]`; Lee et al. 2022 (arXiv:2107.06288); Son et al. 2025
  (arXiv:2510.13121), who conclude that SNe + BAO + CMB are > 9 sigma from
  LCDM and that the universe is not currently accelerating; Chung et al.
  2026 (arXiv:2605.21586) defend the correction against the rebuttal.
- **No**: Rose et al. 2020 (arXiv:2002.12382); Wiseman et al. 2026
  (arXiv:2601.13785); Murakami et al. 2026 (arXiv:2604.16597), who bound the
  redshift-dependent bias at `-0.007 (+0.012/-0.014) mag` `[src]`.

Judgment for prose: the "non-accelerating universe" conclusion comes from one
group, relies on applying a host-age slope without the host-mass correction
and on equating host age with progenitor age, and is contradicted by two
independent samples. It is not a mainstream result and should not be cited
as an established challenge to acceleration. The underlying question — how
much of the environmental dependence is age, and whether mass is an adequate
proxy as redshift increases — is legitimately open (Rigault et al. 2020,
arXiv:1806.03849), and matters most for Roman at z > 1.

## 4. Which inference framework: BBC, hierarchical Bayes, or SBI?
<!-- key: which-inference-framework-bbc-hierarchical -->

- BBC separates standardisation, bias correction and cosmology; it is
  frequentist in its nuisance parameters (they are fitted, not
  marginalised, as arXiv:2511.07517 notes) and depends on simulated
  populations.
- Hierarchical models (UNITY, Steve, BAHAMAS) marginalise populations and
  selection jointly, but selection enters through analytic approximations;
  Steve showed a `w` bias that depends on the scatter model (Hinton et al.
  2019, arXiv:1811.02381).
- SBI (FlowSN, arXiv:2603.11165; CIGaRS, arXiv:2508.15899) learns the
  selection-affected likelihood from the same simulations BBC uses. No SBI
  cosmology result on real data was found in this session's searches.

The decisive test is announced, not done: UNITY on the Unite sample
(arXiv:2609.05053). Until then, differences between Union3.1 and
Unite/DES-Dovekie mix data and method.

## 5. Is there a calibration floor?
<!-- key: is-there-a-calibration-floor -->

Current cross-calibration reaches the few-mmag level per band, but small
shifts are amplified up to six-fold in distance (Popovic et al. 2025,
arXiv:2506.05471). **Forecast** (Anumba et al. 2026, arXiv:2604.19746): for
Rubin and Roman, 5 mmag and 5 Å errors cost about half the FoM, and the
effect is nearly degenerate with cosmology so that the data cannot
self-calibrate it. Joint training of the SED model and the cross-calibration
(Grayling et al. 2026, arXiv:2606.19429) is one proposed way to add
constraint from the supernovae themselves. Whether absolute flux standards
(DA white dwarfs) can be pushed to the required level is not settled.

## 6. Tensions between analyses that a reader should know
<!-- key: tensions-between-analyses-that-a-reader-should -->

- **Unite vs its parents.** Unite prefers `Omega_m = 0.310`, lower than
  DES-Dovekie (0.330) and Pantheon+ (0.334), although it is built from them
  `[src]` (arXiv:2609.05053). The authors attribute this to the combined
  0.023 <= z <= 0.85 range and to reanalysis choices; the low-z/high-z
  offset between Unite and Pantheon+ on common SNe is −0.0199 mag, mostly
  host masses and dust parameters `[src]`.
- **Siblings.** DES siblings suggest at least half the intrinsic scatter is
  not host-driven (Scolnic et al. 2020, arXiv:2002.00974); ZTF siblings show
  a much smaller scatter between siblings than in the Hubble residuals
  (Dhawan et al. 2024, arXiv:2406.01434).
- **`alpha` from siblings and from broken fits** (0.22–0.27 for low-stretch
  SNe) vs the single `alpha ~ 0.16` of cosmology fits.
- **CMB vs SN + BAO in wCDM**: "strong evidence of tension" within constant
  `w`, relieved by `w(a)` `[src]` (arXiv:2609.05053). Whether that is
  evidence for evolution or for a mismatch elsewhere is the question of
  `cosmo-tensions-anomalies`.

## 7. What the next data will decide
<!-- key: what-the-next-data-will-decide -->

| Question | Data | Expectation | Source |
|---|---|---|---|
| Does the dark-energy preference survive a modern anchor? | DEBASS (> 400 SNe on DECam) replacing the historical DES anchor | **Forecast**: −30 % and −24 % on the `w0`, `w_a` statistical errors, FoM up to +60 % | Acevedo et al. 2025, arXiv:2508.10877 |
| Same, northern sky | ZTF DR2.5 with scene-modelling photometry | Not released as of this snapshot; the pocket-effect correction is the gating item | Lacroix et al. 2025, arXiv:2509.04073 |
| Same, all sky | TITAN (ATLAS) | Calibration at the 5–10 mmag level claimed; cosmology pending | Marlin et al. 2025, arXiv:2512.21903 |
| Can a year of targeted spectroscopy settle it? | Rubin alerts + DESI | **Forecast**: > 5 sigma if the current best fit is true | Truong et al. 2026, arXiv:2604.18859 |
| Is a fully photometric (photo-z) Hubble diagram unbiased? | Rubin DDF | **Forecast**: FoM ~150 from ~6000 events, with residual biases to fix | Mitra et al. 2025, arXiv:2512.06319 |
| Evolution at z > 1 | Roman HLTDS (launched August 2026) | **Forecast**: 10 000 SNe Ia, FoM above 326 without model-training systematics | Kessler et al. 2025, arXiv:2506.04402 |
| BBC vs UNITY on identical data | Unite | Announced | arXiv:2609.05053 |

## 8. Misconceptions and stale claims
<!-- key: misconceptions-and-stale-claims -->

| Claim still seen | Status | Correction |
|---|---|---|
| "DESI + CMB + DESY5 prefers evolving dark energy at 4.2 sigma." | Stale since November 2025 | 3.2 sigma with DES-Dovekie (arXiv:2511.07517); 3.4 sigma in the Hoyt et al. re-run (arXiv:2601.19424) |
| "Pantheon+ shows the weakest preference (2.8 sigma), so the signal is driven by DES." | Stale | With consistent host masses Pantheon+ gives 3.2 sigma (arXiv:2601.19424); 3.4 → 4.0 sigma for the Pantheon+ subsample of Unite when its masses are remeasured (arXiv:2609.05321) |
| "The three SN samples are independent confirmations." | Wrong | 1363 SNe common to Pantheon+ and Union3; the DES anchor is a subset of Pantheon+ (arXiv:2503.14738; arXiv:2609.05053) |
| "Supernovae alone prefer evolving dark energy." | Wrong | SN-only posteriors are consistent with `w_a = 0`; the SN contribution is `w0 > -1` at ~2 sigma, and the `w_a` signal appears only with BAO and CMB (arXiv:2609.05053; arXiv:2511.07517) |
| "`Omega_m = 0.352` from DES supernovae." | Superseded | 0.330 ± 0.015 (arXiv:2511.07517) |
| "Union3 gives `Omega_m = 0.356`." | Superseded | 0.344 (+0.026/−0.025), Union3.1 (arXiv:2601.19424) |
| "DES-SN5YR is statistics-dominated, so systematics cannot matter." | Misleading | Its photometric systematic had been underestimated by ~20 % through a weighting error, and calibration alone later moved the result by one sigma (arXiv:2511.07517) |
| "ZTF DR2 provides a 3600-SN low-z Hubble diagram for cosmology." | Wrong | The release paper states the photometry is not suited for cosmological inference; a sensor non-linearity was found later (arXiv:2409.04346; arXiv:2509.04073) |
| "The mass step is 0.06 mag." | Under-specified | 0.00 to 0.17 mag depending on bias-correction model, tracer and stretch linearity (`results.md` Section 3.3) |
| "The mass step is explained by dust." | Contested | See Section 2; arXiv:2605.06799 against, arXiv:2004.10206 for |
| "Age-corrected supernovae show the universe is not accelerating." | Fringe, rebutted | arXiv:2601.13785; arXiv:2604.16597 |
| "Photometric classification is the limiting systematic of DES." | Wrong | Less than 10 % of the systematic budget (arXiv:2401.02945) |
| "The low-z/high-z offset between DES and Pantheon+ proves a DES error." | Half right | 38 % of it is a selection-function artefact of the comparison (arXiv:2501.06664); the remainder led to real corrections on *both* sides (arXiv:2511.07517; arXiv:2601.19424) |
| "Recalibration of SNe could resolve the Hubble tension." | Not supported | The 2025–2026 corrections change `H0` by ~0.2 km/s/Mpc (Roy Choudhury 2026, arXiv:2607.24443); calibration contributes < 0.2 km/s/Mpc (arXiv:2112.03864) |
| "FoM values are comparable between papers." | Wrong | Two definitions differing by a factor 19.4 are in use (arXiv:2311.12098 vs arXiv:2609.05053) |
| "JLA / Pantheon are fine for a quick fit." | Obsolete | Superseded twice over in calibration, scatter model and covariance treatment (arXiv:2202.04077) |

## 9. Hubble diagrams beyond SNe Ia: what quasars and GRBs add at z > 2
<!-- key: hubble-diagrams-beyond-sne-ia-what-quasars-and -->

SN Ia samples thin out near z ~ 2; quasars (X-ray–UV relation), gamma-ray
bursts and HII galaxies reach z ~ 7 and beyond. None is a physically
standardised candle: each is an empirical correlation whose normalisation is
degenerate with H0 and with the SN M_B. Details, samples and numbers are in
`cosmo-distance-ladder-h0`, `references/alternative-distance-probes.md`.

**Dependence on SN calibration.** The quasar Hubble diagram is put on an
absolute scale by cross-calibration on SNe Ia in the common redshift range
(Lusso et al. 2020, arXiv:2008.08586) `[sec: alternative-distance-probes.md
§2.1]`. GRB relations are calibrated by interpolating the SN Ia distance
modulus at each burst redshift (Liang et al. 2008, arXiv:0802.4262) `[src]`,
in 2025 on Pantheon+ (Huang et al. 2025, arXiv:2506.08929) `[src]`. The
high-z points therefore inherit the SN calibration and its systematics; they
add only the extrapolation in redshift, plus their own evolution and
selection effects.

**Reading a claimed departure from ΛCDM.** The quasar diagram agrees with SNe
and ΛCDM below z ~ 1.4 and deviates above at ~4σ according to its authors
(Risaliti & Lusso 2019, arXiv:1811.02590) `[src]`, who argue against a
redshift-dependent systematic (arXiv:2008.08586) `[src]`. Critiques: the
deviation comes from a cosmographic expansion that fails beyond z ~ 2
(Yang et al. 2020, arXiv:1911.01681) `[src]`; the full sample is not
standardisable, only z ≲ 1.5–1.7 subsets are (Khadka & Ratra 2020,
arXiv:2012.09291) `[src]`, with the SDSS–4XMM sub-sample as main cause
(arXiv:2107.07600) `[src]`; rising Ω_m with effective redshift is expected
in flat-ΛCDM fits (Ó Colgáin et al. 2022, arXiv:2203.10558) `[src]`. eROSITA
quasar samples confirm the relation but do not yet constrain cosmology
(Sacchi et al. 2025, arXiv:2508.00732) `[src]`. HII galaxies to z ~ 14 are
consistent with flat ΛCDM (Chávez et al. 2026, arXiv:2607.14254) `[src]`.
Checks before accepting such a claim against the SN Ia diagram: is the
departure present where SNe and the probe overlap (it is not, for quasars);
direct model fit or cosmographic series; relation parameters fitted jointly
and stable across redshift bins and models; which sub-samples carry the
high-z points.

## Not verified
<!-- key: not-verified -->

- Whether any published analysis combines DESI DR2 with Unite using exactly
  the DESI external data; and any DESI DR3 result.
- Responses to the Unite and Union3.1 papers after September 2026.
- Claims of anisotropy or dipoles in SN samples (several 2025–2026 preprints
  appeared in searches) are outside this file; see
  `cosmo-tensions-anomalies`.
