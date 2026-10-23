# Open questions — peculiar velocities

Scope: live controversies with both sides cited, internal tensions between analyses of the same
data, method debates, forecasts (labelled), what the next data decide, and the stale claims that
still circulate. Snapshot: 2026-10-14

The two controversies of the 2026-08 compilation (FP against TF and SNe; the contested bulk flow)
are merged into §1 and §3; its reading of the fσ8 table and its open gaps are in §4 and §11. Flags
as in `results.md`.

---

## 1. Is the bulk flow at 150–250 h⁻¹Mpc anomalous?
<!-- key: is-the-bulk-flow-at-150-250-h-1mpc-anomalous -->

Folded in part on 2026-10-20 from the compilation of 2026-08-12/14, in which `[src]` meant "traced
to the paper" and `[der]` "relabelled or derived, the paper does not quote fσ8": that compilation
records the CF4 result as a 4.81σ excess at 200 h⁻¹Mpc, estimator-dependent (arXiv:2306.11269), and
advises against citing the excess as established.

**For an anomaly.**

- Watkins et al. 2023 (arXiv:2302.02028): MV top-hat flow of 387 ± 28 km/s at 150 h⁻¹Mpc and 419 ±
  36 at 200 h⁻¹Mpc in CF4, against expectations of 139 and 120; probabilities 0.023 % and 0.00021 %
  [src: Table 1].
- Whitford, Howlett & Davis 2023 (arXiv:2306.11269): confirm the amplitude with mock-calibrated
  errors, 428 ± 108 km/s at 173 h⁻¹Mpc, probability 0.11 % [src: abstract].
- Duangchan et al. 2025 (arXiv:2507.22236): a forward model with no ΛCDM prior on the velocity field
  finds "a 3σ tension … around 140 Mpc/h and 240 Mpc/h" [src: abstract].
- Watkins, Clark & Feldman 2025 (arXiv:2512.03168): the flow is "dominated by sources beyond 200
  Mpc/h", with the external part rising with scale [src: abstract].
- Courtois et al. 2025 (arXiv:2502.01308): no dynamical homogeneity scale within 200–300 h⁻¹Mpc in
  CF4++; their bulk flow at 150 h⁻¹Mpc is 315 ± 40 km/s [src: abstract].

**Against.**

- Nusser & Tully 2026 (arXiv:2608.14265): monopole + dipole in six radial bins to 300 h⁻¹Mpc, with
  the ΛCDM prediction computed for the actual positions, weights and covariances. The full CF4
  sample is "broadly consistent with ΛCDM" (dipole deviation 2.29σ, joint 2.36σ). The excess is
  **localised** at 120–160 h⁻¹Mpc (|V_dip| = 628 ± 82 km/s, 3.40σ), concentrated towards negative
  supergalactic X, and "depends strongly on the survey window": removing 6dFGS lowers the deviation
  to 1.56σ, removing SNe raises it to 3.77σ; TF and 6dFGS favour larger dipoles, SDSS and SNe
  smaller ones [src: abstract].
- Stiskalek, Desmond & Lavaux 2025 (arXiv:2509.14997): a general bulk-flow curve from TF and SN
  samples at z < 0.05 is "fully consistent with expectations from the standard cosmological model"
  [src].
- Do et al. 2026 (arXiv:2606.17142): SN Ia flows of ~100–400 km/s within z ≲ 0.1, "all consistent
  with the predictions of ΛCDM", with the spread between two estimators, two distance estimators and
  two wavelength regimes presented as the systematic [src: abstract].
- Dressler & Monson 2026 (arXiv:2604.02470): 5 % SBF distances show a ~1000 km/s infall over a
  steradian converging to zero at ~70 Mpc, "at odds with reports of comparable amplitude bulk flows
  on scales of hundreds of Mpc" [src: abstract].
- kSZ: no flow in Planck clusters (< 254 km/s at 95 % CL, arXiv:1303.5090); upper limits at 200–2000
  h⁻¹Mpc consistent with ΛCDM (arXiv:2605.12499) [src].
- Hollinger & Hudson 2024 (arXiv:2312.03904): the residual flows of velocity–density comparisons are
  "not in conflict" with ΛCDM [src].

**Where the disagreement actually sits.** Not in the amplitude of the CF4 dipole (387 ± 28, 428 ±
108 and 315 ± 40 differ by less than 2σ [der]) but in (i) the error model — analytic MV errors
against mock-calibrated ones; (ii) the window — a top-hat sphere reconstructed by MV weights against
the survey's own radial bins; (iii) the 6dFGS FP component of CF4, whose zero-point and Malmquist
treatment are independently in question (§3). Heinesen 2023 (arXiv:2305.16084) adds that neglected
relativistic terms of order vz bias recent estimates "toward larger values by ~10 %" [src].

**What decides it.** A homogeneous southern FP sample (4HS) replacing 6dFGS in the 120–160 h⁻¹Mpc
shell; DESI PV at the same depth in the north with a single zero-point; selection-matched mocks,
which Nusser & Tully 2026 name as the missing test.

---

## 2. "Peculiar velocities grow faster in general relativity"
<!-- key: peculiar-velocities-grow-faster-in-general -->

- Claim: in the 1+3 covariant treatment the peculiar flux gravitates, giving linear growth v ∝ t in
  place of the Newtonian v ∝ t^(1/3), which "could explain the reported fast and deep bulk flows"
  (Pastén & Tsagas 2026, arXiv:2601.21741; review in Tsagas, Perivolaropoulos & Asvesta 2025,
  arXiv:2510.05340) [src].
- Rebuttal: "When the covariant equations are applied consistently, the 1+3 approach reproduces
  exactly the standard perturbative result"; the stronger growth comes from "an inconsistent
  treatment of the coupled covariant system, in which terms constrained by the field equations are
  treated as if they were independent sources" (Clarkson & Maartens 2026, arXiv:2603.14511) [src].
- Reply: Tsagas 2026 (arXiv:2603.28377) maintains that the quasi-Newtonian approach is "effectively
  Newtonian" [src].

Status: unresolved in print. No observational peculiar-velocity analysis uses the modified growth
law; standard linear theory is the working assumption of every result in this skill, and full-GR
simulations find FLRW modelling adequate at z ≲ 0.2 (arXiv:2606.18437) [src].

---

## 3. Which distance indicator can be trusted?
<!-- key: which-distance-indicator-can-be-trusted -->

Two results point in opposite directions.

- **FP low, TF and SN concordant** (velocity–density comparison against 2M++): TF + SN give S8 =
  0.798 ± 0.035; FP samples shift by 0.08 (SDSS) and 0.15 (6dF) in S8 under a quadratic Malmquist
  term and end in 3.3σ mutual tension (Stiskalek 2025, arXiv:2509.20235) [src].
  Folded on 2026-10-20 from the compilation of 2026-08-12/14, in which `[src]` meant "traced to the
  paper" and `[der]` "relabelled or derived, the paper does not quote fσ8": it calls this the first consistent Bayesian analysis of all three indicator classes in one framework
  against 2M++, with fσ8 = 0.412 ± 0.018 from TF + SNe, concordant with the CMB; its conclusion: low-z
  PV data do *not* reinforce the early-vs-late S₈ tension, and FP systematics deserve scrutiny —
  which matters for the whole programme, since FP dominates the object counts of CF4, SDSS PV and
  4HS. The earlier FP
  result, S8 = 0.637 ± 0.054, "more than 3σ" from Planck (Said et al. 2020, arXiv:2007.04993), is of
  this type [src].
- **TF low, FP concordant** (DESI DR1 correlation functions on one density field): BGS + FP gives
  0.440 +0.064/−0.061; BGS + TF(z < 0.05) gives 0.261 +0.130/−0.101; and TF at z > 0.05 shows an
  unexplained excess correlation and was discarded (arXiv:2512.03230) [src].

They are not contradictory — different estimators, different TF samples (HI linewidths in CF4,
single-fibre optical rotation at 0.4 R26 in DESI), and the DESI TF error bar is large — but neither
supports a blanket statement about an indicator. Common ground: environment-correlated residuals
exist in both relations (group-richness trend in SDSS and DESI FP; Millennium-TNG, arXiv:2602.23033)
[src: Sect. A.2].

Open: whether the DESI FP group trend is physical or photometric ("the difference in amplitude works
against" a physical origin, arXiv:2512.03226); the cause of the TF excess at z > 0.05; whether the
position-angle systematic of arXiv:2608.26459 contributes [src].

---

## 4. One dataset, three estimators: the DESI DR1 spread
<!-- key: one-dataset-three-estimators-the-desi-dr1-spread -->

0.391 (correlation functions), 0.440 (power spectra), 0.483 (field-level) on the same catalogue,
consensus 0.4497 ± 0.0548 with correlations from 675 mocks [src: arXiv:2512.03229, arXiv:2512.03230,
arXiv:2512.03231].

- The papers' reading: mutually consistent within 1σ, and "the improvement when combining the
  methods is appreciable, given that the different methods access different underlying scales with
  different weights" [src: arXiv:2512.03230].
- The opposite reading (2026-08 compilation; folded on 2026-10-20 from the compilation of
  2026-08-12/14, in which `[src]` meant "traced to the paper" and `[der]` "relabelled or derived,
  the paper does not quote fσ8"): the 0.391 → 0.483 spread on identical data is the honest scale of
  current method systematics, larger than most individual quoted error bars, and it tracks the
  method family — the field-level estimator high, the two two-point estimators lower; more widely,
  reconstruction methods cluster low (0.31–0.40) and velocity-statistics methods scatter wider and
  higher, "a real methodological split", visible in the DESI DR1 triplet [der, 2026-10-20: the
  velocity–density rows of `results.md` §0 run from 0.310 to 0.480 once Feix 2017 is counted, and
  0.310–0.420 without the luminosity rows].

The mocks settle part of it. The three estimators are correlated at only 27–39 % on the 675 mocks
("lower than expected"; 84 % between Fourier and configuration space in eBOSS), and with those
correlations the largest observed difference (field-level minus correlation functions) is 1.1σ [src:
arXiv:2512.03228, §9; der: see `results.md` §1]. So the DR1 spread alone does not demonstrate a
method systematic. What it does show is that the three estimators weight different scales and carry
different nuisance models, to the point of being nearly independent on the same galaxies — which is
why combining them gains information, and why agreement between them is a weaker cross-check than it
looks. The field-level posterior is strongly asymmetric (+0.080/−0.043) while the consensus is
Gaussian "by construction", built from half-widths.

Related internal inconsistency: the Planck ΛCDM value at z = 0.07 is quoted as 0.449 ± 0.008 in
arXiv:2512.03229 and as 0.446 in arXiv:2512.03230 [src].

---

## 5. The non-linear velocity model
<!-- key: the-non-linear-velocity-model -->

- The sinc damping is empirical and its scale is not agreed: ≈ 13 h⁻¹Mpc from N-body
  (arXiv:1312.1022), 6.75 from 2MTF data, 19–23 from SDSS PV mocks (values quoted in
  arXiv:2303.01198) [src, sec].
- Field-level analyses fix it for memory reasons and carry the cost as a systematic (0.018 in DESI
  DR1) that "could potentially exceed the statistical uncertainty" in future releases
  (arXiv:2512.03229) [src].
- Three replacements are on the table: interpolated covariances over (σ_g, σ_u) in flip
  (arXiv:2501.16852), written "to lay the foundations for a nonlinear extension of the
  likelihood-based method at the field level"; 1-loop EFT with velocity-specific IR resummation
  (arXiv:2508.00066); HOD emulators (arXiv:2602.03382), where realistic velocity errors and
  small-scale systematics erase much of the gain: 3.8 % on fσ8 with velocities against 4.7 % from
  clustering alone in a ZTF + DESI-like setting (**forecast**) [src].
- Limit set by galaxy physics: TF/FP velocities are unreliable below ~10 h⁻¹Mpc whatever the
  dynamical model (arXiv:2602.23033) [src].

---

## 6. Local H0 anisotropy and the local void
<!-- key: local-h0-anisotropy-and-the-local-void -->

- Dipoles in H0 from CF4 and Pantheon+ are detected at high odds as *zero-point* dipoles but are
  better described by flow structure (arXiv:2509.14997), and shrink once velocity corrections are
  applied (arXiv:2512.02526) [src].
- Local-void solutions to the Hubble tension predict outflows and a rising bulk-flow curve
  (Mazurenko et al. 2024, arXiv:2311.17988: "qualitative agreement" with the CF4 flow) [src].
  Fitting such profiles to CF4 TF distances with a field-level forward model prefers "a void size of
  less than 70 Mpc", under 10 % of the size required, with a predicted local H0 of 70.2–72.1
  km/s/Mpc depending on the profile (Stiskalek, Desmond & Banik 2025, arXiv:2506.10518) [src]. This
  belongs to `cosmo-distance-ladder-h0` and `cosmo-tensions-anomalies`.

---

## 7. Does low-z growth support an S8 or growth tension?
<!-- key: does-low-z-growth-support-an-s8-or-growth -->

- Against: fσ8(z = 0.07) = 0.450 ± 0.055 equals the Planck ΛCDM prediction (DESI DR1); TF + SN S8 =
  0.798 ± 0.035 (arXiv:2509.20235); γ_L = 0.580 ± 0.110 (DESI) and γ ≈ 0.50–0.53 from SN velocities
  + CMB (arXiv:2604.06361) [src].
- For: FP-based velocity–density comparisons (arXiv:2007.04993) [src].
- Verdict in the literature as of the snapshot: no support, with FP systematics as the stated reason
  for the earlier signal. A 12 % measurement cannot settle a tension of a few per cent; see
  `cosmo-weak-lensing` for the lensing side.

---

## 8. Forecasts — all rows are forecasts, not measurements
<!-- key: forecasts-all-rows-are-forecasts-not -->

| Survey or combination | Forecast | Method | Citation | Flag |
|---|---|---|---|---|
| TAIPAN + WALLABY/WNSHS | ~3 % on fσ8 at z ~ 0.025; velocities improve the constraint by ~40 % over density alone; factor ~2 if all modes to k = 0.2 h Mpc⁻¹ are used | Fisher | Koda et al. 2014, arXiv:1312.1022 | [src: abstract] |
| same, combined surveys | ~3 %; adding 2MTF (~2 000 galaxies) to 6dFGS improves fσ8 by ~20 % | Fisher | arXiv:1609.08247 | [src] |
| DESI PV + BGS, full survey | 4 % statistical at z < 0.15, "over two times better" than BGS redshifts alone | Fisher | Saulder et al. 2023, arXiv:2302.13760 | [src] |
| DESI PV vs BGS RSD | uncertainty reduced "by a factor of approximately 2.5 at redshift 0.1" | — | Said et al. 2025, arXiv:2408.13842 | [src: abstract] |
| ZTF SNe, 6 years, z < 0.06 | 19 % | mocks + maximum likelihood | arXiv:2303.01198 | [src] |
| ZTF 6-year SNe + DESI DR3 BGS | σ(fσ8) = +0.047/−0.048, a 10 % error; up to 50 % reduction from adding the density | field-level on dedicated simulation | Ravoux et al. 2026, arXiv:2609.34508 | [src: abstract] |
| ZTF + LSST SNe | 5 % on fD "by 2027" | analytical | Graziani et al. 2020, arXiv:2001.09095 | [src] |
| LSST SNe, 5 years, SN data alone | σ(σ8) = 0.17, or 0.09 with 20 % completeness | exact likelihood + Fisher | Garcia et al. 2020, arXiv:1905.00746 | [src: abstract] |
| LSST SNe, realistic simulation | 10 % over 0.02 < z < 0.14; < 18 % in each of three bins | mocks + maximum likelihood | arXiv:2507.00157 | [src: abstract] |
| LSST + DESI SNe with high-z RSD | σ(γ) ≈ 0.02 | Fisher | Kim & Linder 2020, arXiv:1911.09121 | [src] |
| LSST + 4MOST, 6×2pt | area in (σ8, γ) shrinks "by more than half" against clustering alone | Fisher | Quartin et al. 2022, arXiv:2111.05185 | [src] |
| Next-generation SN surveys × galaxies | "a further order of magnitude" on fσ8 over the Pantheon+ × BGS result | N-body scaling | arXiv:2510.07673 | [src] |
| Einstein Telescope sirens + DESI/TAIPAN | ~3 % on fσ8, σ(γ) ≲ 0.04 | Fisher | arXiv:2005.04325 | [src] |
| Neutrino mass with velocities | Σm_ν ≈ 0.14 eV (68 %) attainable without Planck; marginal gain with Planck | Fisher | Whitford, Howlett & Davis 2022, arXiv:2112.10302 | [src: abstract] |
| V̂_G (kSZ velocity × CMB lensing) | S/N ~ 20–55 for ACT/SO × DESI | forecast | arXiv:2510.27605 | [src] |
| Whole programme | ≲ 3 % on fσ8 to z = 0.3 | review statement | Turner 2024, arXiv:2411.19484, via the 2026-08 compilation (`surveys-and-data.md` §6) | [sec] |

Reading the table.

- The 2014–2020 forecasts assumed Taipan and used volume Fisher matrices. A survey-geometry Fisher
  forecast is "30 % closer to a full likelihood-based estimation than a standard volume Fisher
  forecast" (arXiv:2501.16852) [src]: volume forecasts are optimistic.
- Measured against forecast: DESI DR1, with about 41 % of the predicted final velocity sample [der:
  76 615 / 186 000] and almost only FP, reaches 12.2 % (arXiv:2512.03230) against 4 % forecast for
  the full survey [src]. The forecast did not include the TF loss at z > 0.05, the k ≤ 0.1 cut on
  the momentum spectrum, or the σ_u systematic.
- The 2020 statement that ZTF and LSST reach 5 % "by 2027" has no measurement behind it one year
  before that date: no fσ8 from ZTF data was found (`surveys-and-data.md` §4).

---

## 9. What the next data decide
<!-- key: what-the-next-data-decide -->

| Question | Data | When |
|---|---|---|
| Is the TF excess at z > 0.05 a systematic of single-fibre rotation? | DESI DR2 TF, integral-field comparison (arXiv:2608.26459) | DR2 analyses; no date published |
| Does the estimator spread shrink with volume? | DESI DR2/DR3 with the three estimators | same |
| Is the 120–160 h⁻¹Mpc dipole a 6dFGS artefact? | 4HS FP in the south | after 4MOST science operations start |
| First fσ8 from a homogeneous SN sample | ZTF DR2.5, TITAN, then Rubin | not released on the snapshot date |
| Closing a particle-evolving forward model into fσ8 | Hamlet-PM (arXiv:2602.03699), Manticore-type inference | open niche: the machinery exists on the reconstruction side and has not been closed into a growth-rate measurement (`physics-and-methods.md` §0, §5) |
| Non-linear field-level likelihood | flip extensions, EFT or emulator covariances | method work in progress |
| b_v and the electron profile | SO × DESI, tSZ-informed τ | belongs to `cosmo-cmb-lss-cross-correlations` |

---

## 10. Stale or wrong claims still in circulation
<!-- key: stale-or-wrong-claims-still-in-circulation -->

| Claim | Correction | Source |
|---|---|---|
| "CF4 shows a 4.8σ (or 5σ) bulk flow" | With mock-calibrated errors the probability at ~173 h⁻¹Mpc is 0.11 %; a shell analysis gives 2.3σ over the full range and a localised 3.4σ feature that depends on the 6dFGS component | arXiv:2306.11269, arXiv:2608.14265 |
| "Bulk-flow measurements disagree with each other" | The amplitudes agree; the windows, depths and error models differ. Quote window and depth with every number | `results.md` §3 |
| "Peculiar velocities show the S8 tension at low z" | True only of FP-based velocity–density comparisons; TF + SN and DESI DR1 agree with Planck | arXiv:2509.20235, arXiv:2512.03230 |
| "DESI DR1 PV combines FP and TF" | 73 686 FP against 2 929 TF velocities after cuts; TF at z > 0.05 was removed | arXiv:2512.03230 |
| "The DESI PV survey measures H0 = 73.7" | It transfers the SH0ES calibration to a Hubble-flow sample; the 1.1 systematic is the ladder's | arXiv:2512.03232 |
| "v = cz − H0 d" for velocities at z > 0.03 | ~100 km/s too high at z ~ 0.04; use the log-distance estimators | arXiv:1405.0105, arXiv:1411.6665 |
| "The zero-point does not matter for growth" | Negligible for the velocity power spectrum, decisive for β and residual flows (250 → 150 km/s in 2MTF) | arXiv:1609.08247, arXiv:1511.04849 |
| "ZTF has measured fσ8" | Only simulations and forecasts are published | arXiv:2303.01198, arXiv:2609.34508 |
| "kSZ measures the velocity field amplitude" | It measures τ × v; b_v ≈ 0.1–0.45 against halo-model profiles, depending on sample and fiducial model (0.10–0.15 for DESI DR2 emission-line galaxies, 0.2–0.45 for luminous red galaxies; values in `cosmo-cmb-lss-cross-correlations`, `results.md`) | arXiv:2511.15701, arXiv:2506.21657, arXiv:2604.04867 |
| "GR predicts faster growth of peculiar velocities than Newtonian theory" | Disputed; the standard result is recovered when the covariant system is solved consistently | arXiv:2603.14511 |
| "The Franco et al. CF4++ fσ8 is a velocity measurement" | It is a real- vs redshift-space clustering ratio | arXiv:2605.00450 |
| "Forward model means non-linear dynamics" | In Boubel 2024, Stiskalek 2025, Boruah 2020 and Stahl 2021 the indicator is forward-modelled, the field is linear | `physics-and-methods.md` §5 |

## 11. Gaps left open by the fσ8 compilation
<!-- key: gaps-left-open-by-the-fsigma8-compilation -->

Folded on 2026-10-20 from the compilation of 2026-08-12/14, in which `[src]` meant "traced to the
paper" and `[der]` "relabelled or derived, the paper does not quote fσ8".

- **Distance indicator for the 13 rows marked "mix"** (count of the 2026-08-13 table). Cosmicflows-
  based analyses blend TF, FP and SNe in proportions that change between catalogue versions, so a
  clean TF/FP/SN split of the compilation is not currently possible.
- **The [der] rows** (three named in the compilation: Carrick, Nusser, Davis; Turnbull also carries
  the flag) would be better replaced by the quantity the papers actually measure (Ω_m^0.55σ8 for
  Carrick and Nusser, β for Davis), with the GR conversion applied at plot time and visible.
- **Crisman, Quartin & Rebouças 2026**, *Joint curvature and growth rate measurements with supernova
  peculiar velocities and the CMB* (arXiv:2604.06361): in scope, no fσ8 extracted, since the abstract
  quotes σ8 and γ (`results.md` §2).
- **Feix and Nguyen use the same physics** — growth from correlated magnitude scatter, of galaxies
  in one case, of SNe in the other. Both are classed `probe=PV` but the indicator column separates
  them (`lum` vs `SN`), which is arguably inconsistent.

## Not verified
<!-- key: not-verified -->

- Bulk-flow amplitude of Duangchan et al. 2025 (only the significance was read); Peery et al. 2018:
  282 km/s at 150 h⁻¹Mpc, r⁻² weights, 2.2 % probability in ΛCDM [src: arXiv:1808.07772, Table 1].
- Whether a published rebuttal to Nusser & Tully 2026 or to Whitford et al. 2023 by the MV authors
  exists beyond arXiv:2512.03168.
- Any Taipan status after the note in `surveys-and-data.md` §6.
- The folded passages of §1, §3, §4 and §11: from the 2026-08 compilation, not re-read.
