# Systematics — peculiar-velocity cosmology

Scope: the systematics that decide whether a peculiar-velocity growth or flow measurement can be
trusted, each with its mechanism, its quantified size where a paper gives one, the standard
mitigation, the validation test and the reference a referee expects. Snapshot: 2026-10-07

The qualitative list by indicator (TF linewidth and inclination, FP aperture and stellar population,
SN standardisation) is in
`pv-surveys.md`
§7 and is not repeated. This file adds the numbers.

Flags as in `results.md`. "DESI DR1" means the December 2025 peculiar-velocity papers
arXiv:2512.03226 to arXiv:2512.03232.

---

## 1. Zero-point (monopole) calibration
<!-- key: zero-point-monopole-calibration -->

**Mechanism.** TF and FP relations are fitted "unanchored … under the assumption of zero bulk radial
flow", i.e. ⟨η⟩ = 0 with no redshift evolution; the physical zero-point is fixed afterwards against
external distances [src: Ross et al. 2025, arXiv:2512.03226, §4]. An error in it is a spurious
monopole in η: a radial inflow or outflow that scales with distance, and that leaks into the dipole
when sky coverage is partial.

**Sizes.**

| Survey | Zero-point and its uncertainty | Anchor | Source | Flag |
|---|---|---|---|---|
| SDSS PV | uncertainty 0.004 dex, "not including cosmic variance or the error within CosmicFlows-III itself" | CF3, cross-checked with the 2M++ predicted zero-point | Howlett et al. 2022, arXiv:2201.03112 | [src] |
| 2MTF vs 6dFGSv | relative difference < 0.02 dex | galaxies and groups in common | Qin et al. 2018, arXiv:1804.05520 | [src] |
| 2MTF vs CF3 | −0.016 ± 0.002 dex | galaxies in common | Qin et al. 2019, arXiv:1811.00822 | [src] |
| DESI DR1 FP+TF | η_zp = 0.139 ± 0.007 | 93 Pantheon+/SH0ES SN Ia distances (137 light curves) matched through galaxy groups; direct host matches are only 4 (TF) + 41 (FP) | Carr et al. 2025, arXiv:2512.03232, §5 | [src] |
| DESI DR1, value used in the field-level likelihood | σ_y = 0.005 | same paper, as quoted by Lai et al. | Lai et al. 2025, arXiv:2512.03229, §3.3 | [src] |

The 0.007 and 0.005 are both read in the arXiv sources of companion papers and differ; check which
version of the zero-point paper a given analysis used before quoting either.

**Propagation.** The zero-point uncertainty is fully correlated between all objects: DESI adds
σ²_η,zp to *every* element of the η covariance (and an extra common term for TF objects) [src:
arXiv:2512.03232, eq. "cov_mat"]. In the field-level likelihood it is marginalised analytically
(`physics-and-methods.md` §3).

**Effect on fσ8.** Small for power-spectrum statistics: "an offset in the zero-point has negligible
impact on the velocity power spectrum" in the Fisher study of Howlett, Staveley-Smith & Blake 2017
(arXiv:1609.08247) [src]. It is *not* small for velocity–density comparisons and bulk flows:

- 2MTF against 2MRS and PSCz: the residual bulk flow drops from ~250 to ~150 km/s, and β from the
  2MRS model moves into agreement with the literature, once "the monopole deviation in the velocity
  zeropoint between data and model" is subtracted (Springob et al. 2016, arXiv:1511.04849) [src].
- CF4: a zero-point **dipole** of 0.087 ± 0.019 mag in the TF W1 sample (4.1 ± 0.9 % in H0; odds
  877:1) and 0.049 ± 0.013 mag in Pantheon+ (2.3 ± 0.6 %), which a radially varying velocity dipole
  explains as "local flow features (or possibly systematics)" (Stiskalek et al. 2025,
  arXiv:2509.14997) [src]. With velocity corrections applied, the CF4 H0 anisotropy "is strongly
  reduced" (Salzano et al. 2025, arXiv:2512.02526) [src].
- CF4 internal scale: the catalogue is "compatible with" H0 = 74.6 ± 0.8 (stat) with "a large
  potential systematic error of ~3 km/s/Mpc" (Tully et al. 2023, arXiv:2209.11238); 75.0 ± 0.1 is
  the value that makes its velocities self-consistent (arXiv:2512.03168) [src]. Using another H0 to
  turn CF4 distances into velocities injects a monopole.

**Mitigation.** Marginalise the zero-point with its real prior width; make the bulk-flow estimator
independent of H0 by construction (the constraint Σ w cz = 0 of Peery et al. 2018,
arXiv:1808.07772); fit a monopole together with the dipole in radial shells, with the
monopole–dipole covariance (Nusser & Tully 2026, arXiv:2608.14265).

**Validation.** Calibrate two indicators on the same groups (DESI aligns TF to FP before the
external calibration [src: arXiv:2512.03232, §5]); compare the calibrated zero-point with the one
predicted by a density reconstruction [src: arXiv:2201.03112].

---

## 2. Malmquist bias and the distance prior
<!-- key: malmquist-bias-and-the-distance-prior -->

**Mechanism.** A distance with a log-normal error is combined with a non-uniform distribution of
true distances: homogeneous Malmquist bias (more volume farther away) and inhomogeneous Malmquist
bias (density structure along the line of sight). Classical treatment: Strauss & Willick 1995
(arXiv:astro-ph/9502079).

**Size — the largest quantified systematic in the field.** In the unified framework of Stiskalek
2025 (arXiv:2509.20235, §5) the inhomogeneous term is modelled through the bias b1 (and optionally
b2) of each velocity tracer relative to the 2M++ density:

| Sample | b2 preferred | Shift in S8, linear → quadratic bias | Flag |
|---|---|---|---|
| CF4 TF (two samples) | consistent with zero | not significant | [src] |
| Pantheon+ SNe | 0.36 ± 0.09 | not significant | [src] |
| SDSS FP | 1.54 ± 0.06 | 0.08 | [src] |
| 6dF FP | 0.86 ± 0.04 | 0.15 | [src] |

against a statistical uncertainty of ~0.03; the joint TF + SN result moves only from S8 = 0.798 ±
0.035 to 0.792 ± 0.035. SDSS FP and 6dF FP agree within 1.5σ under linear bias and are "driven into
3.3σ tension" under the quadratic variant. The author notes the quadratic extension "is not
self-consistent at the field level", because the velocity field is still a linear map of a linearly
biased density, and treats it "as a sensitivity test" [src: all from arXiv:2509.20235, §5]. The
corresponding fσ8 shifts per sample are quoted in the compilation (`fsigma8-pv-compilation.md`
§1) [sec].

**Why FP is exposed.** Early types live in the densest regions (largest b1), so the line-of-sight
density prior matters most for them [src: arXiv:2509.20235, §5]; and their per-object distance error
is the largest (26 % in DESI DR1, 23 % in SDSS PV) [src: arXiv:2512.03226, arXiv:2201.03112].

**Mitigation.** Work in η, never in velocity; forward-model distances with an explicit prior
(VIRBIUS, arXiv:1512.04534; Boruah et al. 2022, arXiv:2111.15535); for two-point statistics, fit the
indicator relation with the selection function inside the likelihood (the 3D-Gaussian FP fit with
1/V_max weights of arXiv:2512.03226) and validate on mocks that carry the same selection.

**Validation.** The mean vs maximum-likelihood η of each galaxy: in DESI DR1 FP the two
distributions differ by a relative zero-point of −0.10 and have σ = 0.124 vs 0.116, but individual
galaxies differ "by up to 0.56 dex in the most highly skewed cases" [src: arXiv:2512.03226, §5] —
sample statistics are safe, single-object distances are not.

---

## 3. Selection in the distance indicator
<!-- key: selection-in-the-distance-indicator -->

**Mechanism.** Magnitude, surface-brightness, linewidth or signal-to-noise cuts correlate with the
scatter of the relation, so the mean η of the selected sample is not zero and depends on redshift.

**Sizes.**

- DESI DR1 FP: variations of axis-ratio, velocity-dispersion and Δχ² cuts give "no or minimal effect
  on the resulting log-distance ratios and less than 5 % variation in σ_r²"; lowering the magnitude
  limit shifts the mean η [src: arXiv:2512.03226, §6]. Imaging: m_r(BASS/MzLS) − m_r(DECaLS) =
  −0.018 ± 0.013 mag, consistent with zero at 1.4σ, no correction applied [src].
- ZTF SN Ia simulations (Carreres et al. 2023, arXiv:2303.01198): the selected sample is unbiased
  only to z < 0.06, where the 6-year forecast is a 19 % fσ8 error; the selection is "mostly a
  magnitude cut", and M_0 is recovered ~0.01 mag low [src: abstract and §5]. A sharp cut in z_obs is
  itself an asymmetric cut in velocity [src: §5].
- Rubin SN Ia (**forecast**, Rosselli et al. 2025, arXiv:2507.00157): photometric classification is
  tolerable — "for contamination fractions below ~2 %, the measurement remains unbiased" [src].
- SN-rate inhomogeneity: the ZTF DR2 volume-limited sample shows a SN Ia excess at z ≃ 0.02–0.04
  rejected as a uniform-rate fluctuation at 12.2σ, with local rate enhancements of 3–8 in clusters;
  "the SN Ia rate is not a linear tracer of the underlying matter density" (Lordet et al. 2026,
  arXiv:2604.12714) [src]. A velocity tracer that over-samples clusters over-weights virialised
  motions.

**Mitigation and validation.** End-to-end mocks with the survey selection (675 for DESI DR1,
arXiv:2512.03228; 2 048 for SDSS PV, arXiv:2201.03112); a redshift cut where the sample stops being
complete.

---

## 4. Environment-dependent residuals of the scaling relations
<!-- key: environment-dependent-residuals-of-the-scaling -->

**Mechanism.** If the residual of the TF or FP relation correlates with environment, the "velocity"
field acquires a spurious correlation with density that no random-scatter model reproduces.

**Sizes.**

- SDSS PV: "a significant trend between group richness and mean surface brightness", removed with
  separate FP fits per richness bin [src: arXiv:2201.03112].
- DESI DR1 FP: an excess of small-scale clustering of η led to the correction ⟨η_group⟩ − ⟨η_field⟩
  = −0.0145 log10(N_group) for N_group < 71, −0.0268 otherwise (χ²/dof = 16.3/16); groups built from
  pairs within r⊥ < 1.75 and r∥ < 8.5 h⁻¹Mpc; the trend has the same sign as in SDSS and "roughly
  half" the amplitude [src: arXiv:2512.03226, §4]. Even after it, the momentum power spectrum is
  enhanced at k > 0.1 h Mpc⁻¹ and is fitted only below that [src: arXiv:2512.03231].
- DESI DR1 TF: "excess correlation" between TF velocities at z > 0.05, seen by all three estimators
  and not reproduced by the mocks ("systematics not captured by the mocks, such as the environmental
  dependence"); all TF velocities at z > 0.05 were removed, leaving 2 929 of 6 806 [src:
  arXiv:2512.03229, arXiv:2512.03230]. Fits by indicator (correlation-function analysis, same BGS
  density): BGS + FP 0.440 +0.064/−0.061; BGS + TF(z < 0.05) 0.261 +0.130/−0.101; BGS + TF(z < 0.10)
  0.320 +0.141/−0.109 [src: arXiv:2512.03230, results table].
- Simulation evidence: in Millennium-TNG, TF- and FP-inferred velocities give reliable two-point
  statistics only "on scales larger than ~10 h⁻¹Mpc"; below that, residuals correlated with
  structural properties, star-formation history and environment produce "spurious correlations with
  the galaxy density field"; adding SFR, gas mass and stellar mass to the relations mitigates it,
  mostly for late types (Dumerchat et al. 2026, arXiv:2602.23033) [src].

**Mitigation.** Scale cuts (24 h⁻¹Mpc lower bound in configuration space, k ≤ 0.1 for the momentum
spectrum, in DESI DR1); environment terms in the relation; splitting by indicator as a null test.

---

## 5. Non-linear velocities and the damping model
<!-- key: non-linear-velocities-and-the-damping-model -->

**Mechanism.** The empirical D_u = sinc(kσ_u) absorbs redshift-space displacement of the tracers and
non-linear motions; σ_u is degenerate with fσ8.

**Sizes.**

| Statement | Value | Source | Flag |
|---|---|---|---|
| σ_u from N-body | ≈ 13 h⁻¹Mpc at z = 0 (valid to k ≤ 0.2 h Mpc⁻¹) | arXiv:1312.1022 | [src] |
| σ_u measured on 2MTF | 6.75 +1.74/−6.75 h⁻¹Mpc | Howlett et al. 2017, as quoted in arXiv:2303.01198, §6 | [sec] |
| σ_u preferred by SDSS PV mocks | within 19–23 h⁻¹Mpc | Lai et al. 2023, as quoted in arXiv:2303.01198, §6 | [sec] |
| fσ8 variation for σ_u in 13–15 h⁻¹Mpc | < ~2 % | arXiv:2303.01198, §6 | [src] |
| Systematic from fixing σ_u, DESI DR1 | ±0.018 on fσ8, ~30 % of the statistical error | arXiv:2512.03229 | [src] |
| Systematic quoted for SDSS PV (field-level, same finite-difference method per arXiv:2512.03229) | ±0.009 | arXiv:2209.04166 | [src] |
| Systematic quoted for the 6dFGS joint RSD+PV fit (source of the term not read) | ±0.061, larger than the statistical ±0.052 | arXiv:2004.06399 | [src] |
| Linear instead of non-linear P_θθ in the velocity covariance | fσ8 biased by (−2.7 ± 0.06) % on 27 ZTF mocks | arXiv:2303.01198, §6 | [src] |
| Linear template for velocity correlation functions | 5.2 % low on HR4 mocks | Tonegawa et al. 2024, arXiv:2309.14457, as reported in `fsigma8-pv-compilation.md` | [sec] |

The three "preferred" σ_u values span a factor of three. A result that fixes σ_u must show the
fσ8(σ_u) slope; a result that samples it must show the prior.

**Mitigation.** Sample σ_u with interpolated covariances (flip, arXiv:2501.16852); perturbative or
emulated models (arXiv:2508.00066, arXiv:2602.03382); a density cut on grid cells [src:
arXiv:2512.03229].

---

## 6. Reconstruction systematics (velocity–density comparison)
<!-- key: reconstruction-systematics-velocity-density -->

- Bias of the method itself on 2M++-like mocks: fσ8 high by 1.04 ± 0.01; cosmic variance of the
  volume ~5 %; predicted-velocity error 170 km/s (Hollinger & Hudson 2024, arXiv:2312.03904) [src].
- Stochasticity of the reconstructed velocity biases the model velocity; in lognormal tests the
  correction is "significant" in some scenarios (Turner & Blake 2023, arXiv:2306.16664) [src].
- Budget for SNe against a 2M++-like reconstruction (**simulated** TITAN): σ_sys = 0.023 = SN 0.017
  ⊕ reconstruction 0.016; "the assumed intrinsic scatter model is the largest single systematic
  contribution" and can shift fσ8 low through red SNe (Dixon et al. 2026, arXiv:2606.14962) [src].
- Dominant *statistical* term of the tightest results is not the velocities but the galaxy field:
  "the uncertainty dominated by the variance of the 2M++ galaxy field" (σ8 of the galaxies) [src:
  arXiv:2509.20235].
- σ8 normalisation: these analyses return the **linear** σ8; the offset to the non-linear convention
  is 6.5 % in Carrick et al. 2015 (`fsigma8-pv-compilation.md` §4b) [sec].
- External flow: a residual dipole of 159 ± 23 to 171 ± 11 km/s is fitted as a free "V_ext"
  (`results.md` §3b); Watkins et al. 2025 (arXiv:2512.03168) argue it "increases monotonically with
  scale", against the usual assumption of a spatially uniform external flow [src].

---

## 7. Wide-angle and geometry
<!-- key: wide-angle-and-geometry -->

Momentum statistics deviate strongly from the plane-parallel limit at low redshift ("deviations from
the plane-parallel limit are large"), and "even multipoles in the cross-correlation between density
and momentum are non-zero regardless of the choice of line of sight" (Castorina & White 2020,
arXiv:1911.08353) [src]. Field-level covariances must therefore be wide-angle (L22 and RC25 models,
`physics-and-methods.md` §3); the plane-parallel AB20 model "breaks for large-area surveys at low
redshift" [src: arXiv:2501.16852]. For correlation functions the survey geometry enters the
definition of ψ1, ψ2 themselves.

---

## 8. Sample variance, mocks and the covariance
<!-- key: sample-variance-mocks-and-the-covariance -->

- Low-z volumes are small: cosmic variance on fσ8 from the 2M++ volume is ~5 % [src:
  arXiv:2312.03904]; Dupuy et al. split their CF3 error into ±0.03 observational and ±0.11 cosmic
  [sec: `fsigma8-pv-compilation.md`].
- Mocks drawn from finite boxes under-predict large-scale velocity correlations: with a 1 h⁻¹Gpc box
  the halo velocity correlation is suppressed relative to linear theory; fitting with k_min = 0
  biases fσ8 "significantly" when bin correlations are ignored; marginalising over k_min restores
  it; the suppression grows with halo mass (Chuang et al. 2026, arXiv:2602.04485) [src].
- Bulk-flow errors from analytic estimators are "typically underestimated" relative to
  mock-calibrated ones (arXiv:2306.11269) [src].
- Observer position: a Local-Group-like observer changes the bulk flow by ~20 % at R ≤ 50 h⁻¹Mpc
  (arXiv:1802.03391) [src].
- Coherent velocities correlate SN magnitudes: neglecting the velocity covariance shifts H0 by about
  1.0 km/s/Mpc in ZTF DR2 simulations and underestimates its error (Carreres et al. 2025,
  arXiv:2405.20409); the zero-point error of a low-z anchor is underestimated by a factor ~2
  (arXiv:astro-ph/0512159); H0 errors from nearby sirens can double (Blake & Turner 2025,
  arXiv:2509.03101) [src]. Group-averaged redshifts recover ~135–145 km/s of scatter (Peterson et
  al. 2024, arXiv:2408.14560) [src]. These belong to `cosmo-supernovae` and
  `cosmo-distance-ladder-h0`.

---

## 9. Model and convention systematics
<!-- key: model-and-convention-systematics -->

- Velocity estimator: v = cz − H0 D overestimates by ~100 km/s at z ~ 0.04 (arXiv:1405.0105) [src];
  the estimators that drop the "−1" term of the full expression underestimate velocities
  increasingly with redshift [src: arXiv:2303.01198, appendix].
- Velocity bias: neglecting it "has the potential to bias constraints on the growth rate by over 5σ"
  for next-generation surveys (**forecast**, arXiv:1609.08247) [src].
- FLRW modelling of magnitude fluctuations: against full numerical relativity the growth-rate offset
  at z ≲ 0.2 is "sub-dominant to the statistical error of current datasets" (Nguyen, Blake &
  Macpherson 2026, arXiv:2606.18437) [src].
- Fit-range dependence: in the DESI DR1 correlation-function analysis fσ8 trends with the lower
  bound of the fit range, within the statistical error [src: arXiv:2512.03230, §5].

---

## 10. What a referee checks in a results section
<!-- key: what-a-referee-checks-in-a-results-section -->

1. Is the fit in log-distance (or magnitude) space, and which velocity estimator
   was used if velocities appear?
2. Zero-point: anchor, uncertainty, and whether it is marginalised or fixed.
   For a flow measurement: is the monopole fitted with the dipole?
3. Malmquist treatment, and the shift of the result under an alternative one —
   mandatory for FP samples.
4. Results split by indicator (FP / TF / SN) on the same density field.
5. σ_u (or the non-linear model): fixed or sampled, value, prior, and the
   induced systematic on fσ8.
6. Scale cuts in k or r, and the trend of fσ8 with them.
7. Wide-angle treatment for any survey covering thousands of square degrees at
   z < 0.1.
8. Mocks: number, selection realism, box size against the largest fitted scale;
   whether the quoted error is the mock scatter or the posterior width.
9. σ8 convention (linear vs non-linear) and effective redshift; whether fσ8 is
   measured or derived from β or Ω_m^0.55 σ8.
10. For a bulk flow: estimator, window, depth, the ΛCDM expectation for the
    *same* window, and mock-calibrated errors.
11. Shared data: which rows of `fsigma8-pv-compilation.md` use the same galaxies.
12. For kSZ velocities: the optical-depth or b_v degeneracy and the external
    information that breaks it.
