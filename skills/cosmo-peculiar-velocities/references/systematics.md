# Systematics — peculiar-velocity cosmology

Scope: the systematics that decide whether a peculiar-velocity growth or flow measurement can be
trusted, each with its mechanism, its quantified size where a paper gives one, the standard
mitigation, the validation test and the reference a referee expects. Snapshot: 2026-10-14

§0 gives the qualitative list by indicator; §1–9 add the numbers.

Flags as in `results.md`. "DESI DR1" means the December 2025 peculiar-velocity papers
arXiv:2512.03226 to arXiv:2512.03232.

---

## 0. Systematics by indicator — the qualitative list
<!-- key: systematics-by-indicator-the-qualitative-list -->

Folded on 2026-10-20 from the compilation of 2026-08-12/14, in which `[src]` meant "traced to the
paper" and `[der]` "relabelled or derived, the paper does not quote fσ8".

**Common to all.** Malmquist / selection bias, homogeneous vs inhomogeneous — the single largest
source of disagreement between analyses (§2); log-distance vs velocity estimator bias (the
ratio-of-distances estimator is biased; use log-distance ratios, §9); zero-point calibration, fully
degenerate with a monopole flow (§1); non-linear velocity dispersion σ_v and the damping model (§5);
coherent bulk flow × survey window; fiducial-cosmology dependence and the fσ8–σ8–γ degeneracies.

**TF-specific.** Inclination corrections, HI linewidth definition (W₅₀ vs W₂₀), extinction,
morphological-type corrections (the SFI++ erratum came from exactly this), HI self-absorption.

**FP-specific.** Aperture correction on σ, stellar-population and environmental dependence of the
plane (§4), surface-brightness selection, plane evolution with z.

**SN-specific.** SALT2 vs SALT3 standardisation, host-mass step, intrinsic-scatter model,
photometric vs spectroscopic classification, and — for PV work — the peculiar-velocity correction
applied *to build the sample*, which is circular if the same reconstruction is later the model.

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
(arXiv:astro-ph/9502079); Monte Carlo study inside the POTENT method paper, Dekel, Bertschinger &
Faber 1990 (doi:10.1086/169418) [src: abstract]; the inverse-TF route that avoids it when no
selection is made on linewidth, Nusser & Davis 1994 (arXiv:astro-ph/9407100) [src: abstract].

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
biased density, and treats it "as a sensitivity test" [src: all from arXiv:2509.20235, §5]. In fσ8
(his Table 1): 6dF FP moves from fσ8L = 0.379 ± 0.016 to **0.301 ± 0.015** under the quadratic
treatment, SDSS FP from 0.412 to 0.373, while the TFR and SN samples barely move [sec: Table 1 as
read for the 2026-08 compilation; folded on 2026-10-20 from the compilation of 2026-08-12/14, in
which `[src]` meant "traced to the paper" and `[der]` "relabelled or derived, the paper does not
quote fσ8"].

**Why FP is exposed.** Early types live in the densest regions (largest b1), so the line-of-sight
density prior matters most for them [src: arXiv:2509.20235, §5]; and their per-object distance error
is the largest (26 % in DESI DR1, 23 % in SDSS PV) [src: arXiv:2512.03226, arXiv:2201.03112].

**Mitigation.** Work in η where the method allows (the DESI DR1 momentum spectrum converts η to v first, arXiv:2512.03231 eq. 57); forward-model distances with an explicit prior
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
| σ_u measured on 2MTF | 6.75 +1.74/−6.75 h⁻¹Mpc | Howlett et al. 2017, as quoted in arXiv:2303.01198, Sect. 5.1 | [sec] |
| σ_u preferred by SDSS PV mocks | 19–23 h⁻¹Mpc tested, 21 or 22 adopted (the paper uses both) | Lai et al. 2023, arXiv:2209.04166 | [src: Sect. 5.3, 6.1] |
| fσ8 variation for σ_u in 13–15 h⁻¹Mpc | < ~2 %; −9 % to +6 % for a Gaussian prior centred anywhere in 5–25 h⁻¹Mpc (width 10); insensitive to the prior width | arXiv:2303.01198 | [src: Sect. 5.1, Fig. 12] |
| Systematic from fixing σ_u, DESI DR1 | ±0.018 on fσ8, ~30 % of the statistical error; mock-mean slope 0.018 per h⁻¹Mpc around σ_u = 16 | arXiv:2512.03229 | [src: Table 1] |
| Systematic quoted for SDSS PV (field-level, central finite difference, δσ_u = 1 h⁻¹Mpc) | ±0.009 | arXiv:2209.04166 | [src: Sect. 6.1, eqs. 45–47] |
| Systematic quoted for the 6dFGS joint RSD+PV fit | ±0.061, larger than the statistical ±0.052; σ_u contributes only 1.09 × 10⁻³ — the term is the redshift-dependent bias α_b (6.06 × 10⁻²); k_max 1.69 × 10⁻³, σ_g 2.84 × 10⁻³ | arXiv:2004.06399 | [src: Table 5, Sect. 5.1.1] |
| Linear instead of non-linear P_θθ in the velocity covariance | fσ8 biased by (−2.7 ± 0.06) % on 27 ZTF mocks, because linear P overestimates small-scale power and hence the variance | arXiv:2303.01198 | [src: Sect. 5.2] |
| Linear template for velocity correlation functions | 5.2 % low on HR4 mocks | Tonegawa et al. 2024, arXiv:2309.14457, as reported in the 2026-08 compilation (`results.md` §0) | [sec] |

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
  is 6.5 % in Carrick et al. 2015 (`results.md` §0b) [sec].
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
  [sec: 2026-08 compilation, `results.md` §0].
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

## 9b. Budgets read analysis by analysis
<!-- key: budgets-read-analysis-by-analysis -->

One table per analysis, read in the body this session; the place read is in each flag. fσ8 values
are at the paper's z_eff (0.07 for DESI DR1) and against the paper's own fiducial.

### DESI DR1, maximum-likelihood fields (Lai et al. 2025, arXiv:2512.03229)
<!-- key: desi-dr1-maximum-likelihood-fields-lai-et-al -->

| Item | What the paper did or found | Flag |
|---|---|---|
| Free parameters and priors | fσ8 ∈ [0, 1], bσ8 ∈ [0, 3], σ_v ∈ [1, 2000] km/s, b_add σ8 ∈ [0, 10], σ_g ∈ [0, 10] h⁻¹Mpc, all flat; σ_u fixed; k_max not free (unlike Adams & Blake 2020) | [src: Sect. 4.1] |
| σ_u slope on the 675 combined mocks | mean fσ8 = 0.442, 0.460, 0.478 for σ_u = 15, 16, 17 h⁻¹Mpc (fiducial 0.462); 16 chosen; systematic by finite difference, ± 0.018 | [src: Table 1, Sect. 4.4.2] |
| Covariance validation | mean Hessian error 0.036 against mock scatter 0.059 (fiducial cuts; 0.066 before them); attributed to the 20 h⁻¹Mpc gridding and the finite k-range removing sample variance; the data error is inflated by 0.059/0.036 ≈ 1.64, following Sugiyama et al. 2023 | [src: Sect. 4.4.2, Sect. 5] |
| Statistical error before and after inflation | 0.483 +0.049/−0.026 → +0.080/−0.043; total relative error 13 % with the systematic | [src: Table 6, Sect. 5] |
| TF alone vs FP alone (velocity only, 20 h⁻¹Mpc grid, σ_u = 10) | TF 0.85 ± 0.11 (all z), 0.64 +0.12/−0.21 (z < 0.05); FP 0.520 ± 0.054 (3σ cut) | [src: Tables 2, 3] |
| Fitting choices (grid 20 vs 30, σ_u 0 vs 10, 3σ vs 4σ cut) | shifts "much smaller than the uncertainty"; all-data fiducial 0.483 vs 0.453 +0.048/−0.053 with a 30 h⁻¹Mpc grid | [src: Tables 4, 6] |
| Density-cell cut | δ_g > 10 removes 6 of ~6 000 cells (20 h⁻¹Mpc grid); δ_g > 2 removes 41 of 2 023 (30 h⁻¹Mpc grid) | [src: App. B] |
| Comparison with GR | fiducial 1.3σ above fσ8 = 0.444 statistically, ~1σ with the systematic | [src: Fig. 10 caption] |

### DESI DR1, density and momentum power spectra (Qin et al. 2025, arXiv:2512.03231)
<!-- key: desi-dr1-density-and-momentum-power-spectra-qin -->

| Item | What the paper did or found | Flag |
|---|---|---|
| Model and nuisances | 1-loop model with 13 parameters, reduced to 5 on mocks: fσ8 ∈ (0, 1.5], b1σ8 ∈ [0, 3], b2σ8 ∈ [−5, 5], σ²_vT, σ²_vS ∈ (0, 350²], flat; b1, b2 and the dispersions shared by density and momentum | [src: Sect. 5.1] |
| Likelihood and covariance | 675 mocks; Sellentin–Heavens t-distribution (eq. 54) instead of a Hartlap-corrected χ²; data vector [P^δ_0, P^δ_2, P^p_0, P^δp_1], k ∈ [0.025, 0.3] h Mpc⁻¹ in 0.009 bins | [src: Sect. 5.1] |
| Mock validation | mock-mean fit 0.468 +0.061/−0.043 against fiducial 0.466 at z = 0.2; P^p_2 left out as noise-dominated | [src: Sect. 5.2] |
| FP group systematic | data P^p rises above the 675 FP mocks from k = 0.05 and strongly at 0.1 h Mpc⁻¹; fσ8 jumps from ~0.4 to ~0.6 when k^p_max reaches 0.125; cause traced to more negative η in large groups (as in SDSS PV); k^p_max = 0.1 adopted, k_max = 0.3 kept for P^δ and P^δp | [src: Sect. 6.1, Fig. 10] |

### DESI DR1, galaxy and momentum correlation functions (Turner et al. 2025, arXiv:2512.03230)
<!-- key: desi-dr1-galaxy-and-momentum-correlation -->

| Item | What the paper did or found | Flag |
|---|---|---|
| Parameters and priors | same five as the power spectra; table prints σ²_vT, σ²_vS ~ U(0, 350) in (h⁻¹Mpc)², not 350² | [src: Table 1, Sect. 3.3] |
| Covariance | 675 mocks, 80 × 80 (five statistics × 16 bins, 24–120 h⁻¹Mpc), Hartlap factor (eq. 35); emcee | [src: Sect. 3.3, Fig. 3] |
| Mock validation | 300 AbacusSummit mocks: mean error ≈ 15.6 %, scatter of best fits ≈ 13.8 % (the Fig. 5 caption swaps the two labels); mock mean 0.484 +0.077/−0.073 against 0.462 | [src: Sect. 4.2] |
| Companion values as this paper quotes them | MLE 0.482 +0.049/−0.026 (+0.018 sys), power spectra 0.443 +0.113/−0.070 — not the abstract values of arXiv:2512.03229 (0.483 +0.080/−0.043) and arXiv:2512.03231 (0.440 +0.080/−0.096); consensus 0.4497 ± 0.0548 (12.2 %) by the Sánchez et al. 2017 method | [src: Sect. 4.3.5] |
| External comparison | Planck ΛCDM fσ8(0.07) = 0.446 (0.449 in arXiv:2512.03229); DESI BGS full shape 0.38 ± 0.09 at z = 0.295, consistent at 1σ | [src: Sect. 4.3.5] |

### DESI DR1 catalogues and zero-point (arXiv:2512.03226, arXiv:2512.03227, arXiv:2512.03232)
<!-- key: desi-dr1-catalogues-and-zero-point-arxiv-2512 -->

| Item | What the paper did or found | Flag |
|---|---|---|
| FP fit | 3D-Gaussian likelihood (eq. 12), 8 parameters with flat priors (a ∈ [1.0, 1.8], b ∈ [−1.5, −0.5], σ1 ∈ [0.01, 0.12] …); iterative p < 0.01 clipping, 6 iterations, 1 534 outliers removed, 96 758 calibrators | [src: 2512.03226 Sect. 5.2.1, Table 2] |
| FP Malmquist and selection | magnitude and redshift cuts "accounted for to the best of our ability" in the f_n and S_n terms of eq. 12, then tested by varying analysis choices | [src: 2512.03226 Sect. 6.1] |
| FP scatter in velocity | ~20 % intrinsic scatter, i.e. errors ~0.2 cz, ~6 000 km/s at z = 0.1; lower cut z = 0.0033 (cz ≈ 1 000 km/s) | [src: 2512.03226 Sect. 2] |
| FP aperture and evolution | fiducial α = −0.06 ± 0.03 and Q = 1.1 ± 0.4, chosen so that the mean η is flat over 0.04 < z < 0.09; α has the stronger effect on the η–z tilt | [src: 2512.03226 Sect. 6.1.1, Figs. 13–14] |
| FP against CF4 | 13 112 common galaxies: μ_DESI = 0.987 ± 0.005 μ_CF4 + 0.48 +0.20/−0.18; divergence below μ ≈ 33 (z ~ 0.01), removed from the clustering sample | [src: 2512.03226 Sect. 6.2] |
| TF calibration | 4 050 galaxies, 14 bins of Δz = 0.005 over 0.03–0.1, common slope, one intercept per bin, HyperFit (eq. 17); slope −7.22 ± 0.01, scatter 0.466 ± 0.001 mag (0.41 and 0.49 in earlier calibrations) | [src: 2512.03227 Sect. IV.3] |
| TF against CF4 | 299 common galaxies (96 in the cosmology sample): DESI larger by 0.21 ± 0.71 mag in μ, read as a zero-point offset | [src: 2512.03227 Sect. VI.1] |
| Zero-point | η_zp = 0.139 ± 0.007 from the covariance-weighted mean difference to Pantheon+ in common groups, z < 0.01 excluded; groups hosting SNe vs all: K–S p = 0.05, mean difference consistent with zero but subtracted | [src: 2512.03232 Sect. V.5, Fig. 8] |
| H0 systematic budget | weighted scatter of the tests (grouping, FP, TF, redshifts, zero-pointing) 0.29 km/s/Mpc (0.49 for the EDR FP); 1.1 with the SH0ES/Pantheon+ covariance taken as a floor; SBF and other calibrators have diagonal covariances only, so their floors are "likely underestimated" | [src: 2512.03232 Sect. VI.1.6, VI.2] |

### DESI DR1 mocks (Bautista et al. 2025, arXiv:2512.03228)
<!-- key: desi-dr1-mocks-bautista-et-al-2025-arxiv-2512 -->

| Item | What the paper did or found | Flag |
|---|---|---|
| Construction | 25 AbacusSummit 2 h⁻¹Gpc boxes × 27 sub-volumes = 675 cut-sky mocks, observer at each centre, DR1 masks; neighbouring sub-volumes correlated below 1.6 % (from Carreres et al. 2023b); 1 + z_obs = (1 + z_cos)(1 + z_v) | [src: Sect. 3.3, eq. 1] |
| FP η skewness | the per-galaxy Malmquist correction pushes large-error galaxies to negative η; the inverse-variance mean stays unbiased; mocks and data are Gaussianised | [src: Sect. 5.4] |
| TF mocks | downsampled to ~10 000 galaxies and refitted with the data's cuts; η_mock = [μ(z_obs) − μ_mock]/5 (eqs. 12–14) | [src: Sect. 6.3] |
| Known mismatches | z = 0.2 snapshot, HOD fitted over another redshift range, residual data systematics; the mocks enter the data analysis only through the covariance | [src: Sect. 10] |

### SDSS PV catalogue (Howlett et al. 2022, arXiv:2201.03112)
<!-- key: sdss-pv-catalogue-howlett-et-al-2022-arxiv-2201 -->

| Item | What the paper did or found | Flag |
|---|---|---|
| FP fit | 34 059 galaxies; a = 1.274 ± 0.027, b = −0.841 ± 0.009; scatters σ1 = 0.0537, σ2 = 0.335, σ3 = 0.219; including the ~20 % rejected objects shifts the plane | [src: Table 2, Sect. 4.3] |
| Selection (Malmquist) correction | analytic f_n per galaxy and per trial distance (eq. 21), the 3D Gaussian integrated within 10.0 ≤ m_r ≤ 17.0 and s > log 70; it up-weights larger distances for incompleteness and for volume; evaluated on 1 001 trial η per galaxy | [src: Sect. 5.1] |
| Validation on 2 048 mocks | measured − true η unbiased in every redshift bin, "no evidence that our pipeline is introducing spurious flows"; an η–absolute-magnitude trend is expected from the geometry of the fit (η ∝ r + 0.841 i) and not corrected | [src: Sect. 5.2, Fig. 10] |
| Group richness | η decreases with the richness of the Tempel et al. 2017 group; not removed by forcing η flat in magnitude; corrected by separate fits per richness bin | [src: Sect. 5.3] |
| Zero-point | 294 galaxies in common with CF3 (285 with FP distances; 90 % at z < 0.05), two lenticulars with TF distances dropped (0.1σ change); relative uncertainty 0.004 dex without cosmic variance or the CF3 error; bulk flow therefore correlated with CF3's; checked against 2M++ | [src: Sect. 5.4, 5.5] |
| Final precision | mean η error 0.1 dex, ~23 % in distance (26 % for 6dFGSv) | [src: Sect. 5.5] |

### SDSS PV growth rate: field-level (Lai et al. 2023, arXiv:2209.04166) and power spectra (Qin et al. 2024, arXiv:2411.09571)
<!-- key: sdss-pv-growth-rate-field-level-lai-et-al-2023 -->

| Item | What the paper did or found | Flag |
|---|---|---|
| Field-level priors | fσ8 ∈ [0, 1], bσ8 ∈ [0, 3], σ_v ∈ [0, 5000] km/s, b_add σ8 ∈ [0, 10], flat; σ_u fixed (and σ_g fixed in the fit without Taylor expansion) | [src: 2209.04166 Sect. 5.1, 6.1] |
| σ_u on mocks | best fσ8 rises with σ_u; values 19–23 h⁻¹Mpc tested against fiducial 0.432; above the ~13 of Koda et al., attributed to the larger subhalo masses of the SDSS mocks; Sect. 5.3 picks 21, Sect. 6.1 and Fig. 11 use 22 | [src: 2209.04166 Sect. 5.3, 6.1] |
| Systematic budget | σ²_s = (∂ψ/∂s)² δs² by central finite difference (eqs. 45–47), δσ_u = 1 h⁻¹Mpc → 0.009; added in quadrature over fixed parameters | [src: 2209.04166 Sect. 6.1] |
| Field-level result | fσ8 = 0.405 +0.076/−0.071 at z_eff = 0.073, k_max = 0.15, δ_g > 20 cut; b_add σ8 = 1.550, > 20σ from zero, "so we must include it"; σ_v = 400 ± 260 km/s | [src: 2209.04166 Fig. 11] |
| Power spectra: likelihood | 2 048 mocks; Box–Cox Gaussianisation per k-bin (eq. 44), then the Sellentin–Heavens t-likelihood (eq. 46); five parameters fσ8, b1σ8, b2σ8, b3nlσ8, σ²_v | [src: 2411.09571 Sect. V.1] |
| Power spectra: result | fσ8 = 0.413 +0.050/−0.058 at z_eff = 0.073 from P^δ_0, P^p_0, P^δp_1; χ²/dof = 72.9/79; GR + Planck prediction 0.448 | [src: 2411.09571 Sect. VI.1, Table 2] |
| Same data, two methods | 0.405 (field-level) and 0.413 (power spectra) on SDSS PV, both at z_eff = 0.073; no joint mock correlation published in either paper | [src: as above] |

### Cosmicflows-4 (Tully et al. 2023, arXiv:2209.11238)
<!-- key: cosmicflows-4-tully-et-al-2023-arxiv-2209-11238 -->

| Item | What the paper did or found | Flag |
|---|---|---|
| Merging | five methods bundled into groups (42 254 FP galaxies → 27 701 groups; 12 395 TF → 10 189; 425 SBF → 227; 1 008 SN Ia hosts → 945; 94 SN II); zero-points fitted jointly by MCMC with grouped SNe Ia as reference; before merging the SN Ia scale was internally consistent with H0 ~ 71 and TF with ~75 | [src: Sect. X.1, Fig. 16] |
| Absolute scale | TRGB and Cepheid (CPLR) matches, both grounded on the NGC 4258 maser (7.576 Mpc, 1.5 %) and the LMC (49.59 kpc, 1 %); Rizzi vs Freedman TRGB scales differ by −0.028 ± 0.035 mag on 12 galaxies | [src: Sect. X.2] |
| Systematics beyond the calibrators | 20–25 % per object means 3 000–7 500 km/s at 0.05–0.1c; "selection biases at the level of only a few percent can have several hundred kilometers per second effects"; the test used is constancy of the Hubble parameter with redshift | [src: Sect. X.3] |
| 6dFGSv Malmquist recalibration | the PDF normalisation with the original J < 13.65 limit gives a Hubble parameter rising at low z in 128 mocks; iterating to J < 13.38 flattens it and reduces the bias of the η-MLE bulk flow | [src: Sect. IV.1, Figs. 4–5] |

### 6dFGSv: field-level fits (Johnson et al. 2014, arXiv:1404.3799; Adams & Blake 2020, arXiv:2004.06399)
<!-- key: 6dfgsv-field-level-fits-johnson-et-al-2014 -->

| Item | What the paper did or found | Flag |
|---|---|---|
| Sample | 8 896 early types, cz < 16 120 km/s (CMB frame), σ0 ≥ 112 km/s, S/N > 5 Å⁻¹, mean distance error 26 % | [src: 1404.3799 Sect. 2.1] |
| Zero-point | the origin of a spurious monopole; an offset y with Gaussian prior σ_y (eq. 32) is marginalised analytically following Bridle et al. 2002 — the scheme later used by SDSS PV and DESI DR1 | [src: 1404.3799 Sect. 3.6] |
| Non-linear velocities | velocities depart from linearity at larger scales than the density; the diagonal (cosmic-variance) terms carry small-scale power, so the field is gridded (method of Abate et al. 2008), which also shrinks the matrix | [src: 1404.3799 Sect. 3.5] |
| Systematic budget, joint RSD + PV | finite-difference terms on fσ8 (Table 5): k_max 1.69 × 10⁻³, σ_g 2.84 × 10⁻³, σ_u 1.09 × 10⁻³, redshift-dependent bias α_b 6.06 × 10⁻²; total ± 0.061 against ± 0.052 statistical; α_b also dominates β (4.84 × 10⁻²) | [src: 2004.06399 Sect. 5.1.1, Table 5] |
| Cosmology dependence | refit with WMAP5, Planck 2015 (fiducial) and Planck 2018 parameters, mainly through the shape of P_mm, P_θθ, P_mθ | [src: 2004.06399 Sect. 5.1.2] |

### SN Ia velocities, ZTF simulations (Carreres et al. 2023, arXiv:2303.01198) — simulation, not a measurement
<!-- key: sn-ia-velocities-ztf-simulations-carreres-et-al -->

| Item | What the paper did or found | Flag |
|---|---|---|
| Fit | fσ8, σ_v and σ_u by maximum likelihood (iminuit, Hesse/Minos errors), checked against emcee | [src: Sect. 3.3] |
| σ_u | Gaussian prior rather than a fixed value; shifts in §5 above | [src: Sect. 5.1] |
| Selection beyond z = 0.06 | the cut keeps ⟨N⟩ ~ 1 660 SNe, half the typed sample; above it the fσ8 bias grows to ~180 % at z = 0.12; a redshift-binned bias correction (Betoule et al. 2014, Kessler & Scolnic 2017) "will shift the velocity of an entire redshift shell", creating fake correlations | [src: Sect. 5.4] |

### TF, FP and SNe against 2M++ (Stiskalek 2025, arXiv:2509.20235)
<!-- key: tf-fp-and-sne-against-2m-stiskalek-2025-arxiv -->

| Item | What the paper did or found | Flag |
|---|---|---|
| Selection | phenomenological radial prior of Lavaux 2016 with a depth R and a sharpness q fitted per sample, checked against the CF4 TF W1 redshift distribution | [src: Sect. 4] |
| Inhomogeneous Malmquist | prior ∝ r² n(r, b1) with n from the 2M++ field, a free b1 per sample (uniform prior), density clipped at τ = 0.01; quadratic variant with b2 ~ N(0, 1) as a robustness test (sizes in §2) | [src: Sect. 4] |
| Velocity model | linear-theory 2M++ velocity scaled by β*, plus a constant external dipole V_ext and a Gaussian residual dispersion σ_v | [src: Sect. 4, eq. 17] |

### Same data, different methods
<!-- key: same-data-different-methods -->

- DESI DR1, one catalogue at z_eff = 0.07: correlation functions 0.391, power spectra 0.440,
  field-level 0.483; mock correlations 27–39 % (`results.md` §1). The three use different error
  constructions: Hartlap χ², Sellentin–Heavens t-likelihood, Hessian errors inflated × 1.64; and
  different scale limits: 24 h⁻¹Mpc, k^p ≤ 0.1, a 20 h⁻¹Mpc grid (tables above).
- SDSS PV at z_eff = 0.073: field-level 0.405 +0.076/−0.071 and power spectra 0.413 +0.050/−0.058,
  with no published correlation between them (table above).
- TF against FP within DESI DR1: the TF-only field-level fit is 0.85 ± 0.11 against 0.520 ± 0.054
  for FP (velocities only, Tables 2–3 of arXiv:2512.03229); all three methods cut TF at z > 0.05.

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
11. Shared data: which rows of the fσ8 table (`results.md` §0) use the same galaxies.
12. For kSZ velocities: the optical-depth or b_v degeneracy and the external
    information that breaks it.

## Not verified in this file
<!-- key: not-verified-in-this-file -->

- §0, and the Stiskalek fσ8 shifts of §2: folded from the 2026-08 compilation, not re-read.
- The individual terms behind the 0.29 km/s/Mpc DESI DR1 zero-point systematic (its Fig. 10).
- Systematic budgets of the 2MTF velocity power spectrum (arXiv:1706.05130), of the 6dFGS
  correlation functions (arXiv:2207.03707), and of the SN velocity–density fits (arXiv:1912.09383,
  arXiv:2105.05185): not read in the body.
