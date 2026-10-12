# Results — peculiar velocities: 2025–2026 measurements and the bulk-flow record

Scope: what the fσ8 compilation does not hold — the non-fσ8 output of the DESI DR1 peculiar-velocity
release, the growth, gravity and flow results found in date-sorted searches from mid-2025 to the
snapshot, and the bulk-flow record with its estimators. Snapshot: 2026-10-07

**The historical fσ8 table is not repeated here.** It lives, row by row and traced to source, in
`pv-surveys.md` (§6) and is discussed in `fsigma8-pv-compilation.md`; nothing here duplicates it.

Flags: `[src]` read this session in the cited paper (abstract unless a section is named); `[sec]`
from a named secondary source; `[der]` derived, derivation stated.

---

## 1. DESI DR1 Peculiar Velocity Survey (arXiv 2025-12-02)
<!-- key: desi-dr1-peculiar-velocity-survey-arxiv-2025-12 -->

Seven companion papers. The three fσ8 values and the consensus are in that table; the rows below
are what it does not carry.

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

- The three estimators give 0.391 (correlation functions), 0.440 (power spectra) and 0.483
  (maximum-likelihood fields) on the same catalogue; the field-level and correlation-function
  abstracts call the other analyses consistent within 1σ [src: arXiv:2512.03229, arXiv:2512.03230,
  arXiv:2512.03231].
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

Rows already in the fσ8 table of `pv-surveys.md` are marked "in table"; they are listed so the 2025–2026 picture is
complete in one place, with the model each assumes.

| Result | Value | Data | Model / method | Citation | Flag |
|---|---|---|---|---|---|
| fσ8 and S8, TF + SN Ia (in table) | fσ8 = 0.412 ± 0.018 (linear σ8), S8 = 0.798 ± 0.035 | CF4 TF, Pantheon+ SNe vs 2M++ | hierarchical forward model of each indicator against a linear-theory reconstruction; flat ΛCDM, f monotonic in Ω_m | Stiskalek 2025, arXiv:2509.20235 (MNRAS 2026; "Stiskalek 2026" in the hub file) | [src] |
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
  table of `pv-surveys.md`. The abstract does not say what the error includes; a fit against a fixed predicted
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
| Peery, Watkins & Feldman 2018, arXiv:1808.07772 | CF3 | improved MV, top-hat, H0-independent | 150 h⁻¹Mpc | (amplitude in body) | — | ~2 % chance of a flow this large | [src] |
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

## Not verified in this file
<!-- key: not-verified-in-this-file -->

- Amplitudes of the Peery et al. 2018 and Duangchan et al. 2025 bulk flows (only significances
  read).
- The estimator behind the Courtois et al. 2025 bulk flow (abstract only).
- Any DESI DR2 peculiar-velocity result: none found up to 2026-10-08.
- fσ8 values of the table in `pv-surveys.md` were not re-read this session except those quoted above from
  abstracts.
