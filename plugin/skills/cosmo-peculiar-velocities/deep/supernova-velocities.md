# Supernova velocities — cosmo-peculiar-velocities dossier

Scope: how SN Ia magnitudes become a growth-rate constraint — Hubble residual, standardisation
fixed or fitted, residual-to-velocity conversion, the velocity-induced magnitude covariance and
its likelihood, the non-linear and intrinsic-scatter terms, redshift and host choices, selection
and contamination cuts — and how to choose between the velocity-covariance, magnitude-covariance,
correlation-function and velocity–density routes for the same supernovae.
Snapshot: 2026-10-19.
From: Turner 2024 review (arXiv:2411.19484), Sect. 3.2; Tsagas et al. 2025 review
(arXiv:2510.05340), Sect. 10.1; ZTF SN Ia DR2 peculiar-velocity paper (arXiv:2405.20409).

Already in L2, not repeated here: the SN samples and their sharing in
`surveys-and-data.md#supernova-samples-used-as-velocity-tracers`; the origin papers of the
magnitude covariance (Hui & Greene 2006, Gordon et al. 2007, Davis et al. 2011) in
`physics-and-methods.md#supernova-magnitude-covariance`; the ZTF selection, the redshift-binned
bias-correction warning and the σ_u prior shifts in
`systematics.md#sn-ia-velocities-ztf-simulations-carreres-et-al` and
`systematics.md#non-linear-velocities-and-the-damping-model`; the SN-rate inhomogeneity and the
Rubin contamination threshold in `systematics.md#selection-in-the-distance-indicator`; the
TITAN budget total in `systematics.md#reconstruction-systematics-velocity-density`; the SN
velocity–density likelihood (Boruah et al. 2020, Stahl et al. 2021, Stiskalek 2025) in
`deep/velocity-density-comparison.md`; σ8 and γ from the magnitude covariance in
`results.md#other-measurements-mid-2025-to-the-snapshot`; forecasts in
`open-questions.md#forecasts-all-rows-are-forecasts-not`. The velocity covariance as a nuisance
in Hubble-diagram fits, and BBC, light-curve models and scatter models themselves, belong to
`cosmo-supernovae`.

Notation: μ the distance modulus; m_B, x1, c the SALT peak magnitude, stretch and colour; α, β,
M (or M0, ℳ) the standardisation coefficients and absolute magnitude; σ_M (or σ_int) the
intrinsic scatter in magnitude; Δμ (or δm, Δm) the Hubble residual at the observed redshift;
z_obs, z_cos the observed and cosmological redshifts; r(z) the comoving distance and d_L the
luminosity distance; σ_v a 1D small-scale velocity dispersion in km/s; σ_u the damping scale of
the velocity covariance in h⁻¹Mpc (physics-and-methods §2).

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Standardise and form the Hubble residual
<!-- key: step-1-standardise-and-form-the-hubble-residual -->

The Tripp relation gives μ_obs,i = m_B,i − (M_B − α x1,i + β c_i) (Carreres et al. 2023,
arXiv:2303.01198, Eq. 17), and the residual is Δμ_i = μ_obs,i − μ_model(z_obs,i) (Eq. 18), with
variance σ²_μ,i = A_iᵀ C_SALT,i A_i + σ_M², A_i = (1, α, −β) (Eqs. 19–20) [src: Sect. 3.1.1]. At
z < 0.1 the residual is set by the velocity, so Ω_m cannot be fitted: Carreres et al. fix the
cosmology to the simulation input and fit only p_HD = {α, β, M0, σ_M} [src: same]. Current
practice differs on whether p_HD is refitted with the velocities:

- **Fitted jointly.** Carreres et al. let p and p_HD vary together "as one would ideally do in the
  analysis"; on 27 ZTF 6-year mocks fσ8/fσ8_fid = 0.998 ± 0.037 with mean error 0.188, and α, β,
  M0, σ_M recovered (e.g. β = 3.054 ± 0.006 vs 3.1 input) [src: arXiv:2303.01198, Sect. 4.2,
  Table 4].
- **Fixed from the full Hubble diagram, offsets marginalised.** Huterer et al. 2017 hold α = 0.14,
  β = 3.1 at their Hubble-diagram values but marginalise an extra intrinsic scatter and a
  zero-point offset, N → N + Δσ²_int I (Eq. 11) and ΔM, because "the inferred intrinsic scatter
  should be smaller, since we are now explaining some of this scatter with the peculiar velocity
  signal" [src: arXiv:1611.09862, Sects. 2.1, 3.2].
- **Taken from the published compilation.** Crisman et al. 2026 use the BBC-corrected Pantheon+,
  DES-Y5 and DES-Dovekie distance moduli directly and "do not fit the light-curve parameters α,
  β and γ"; Nguyen et al. 2025 use the Pantheon+ moduli and subtract the ensemble mean of δm,
  "effectively fitting for the absolute magnitude M − 5 log10 h" [src: arXiv:2604.06361, Sect.
  2.1; arXiv:2510.07673, Sect. 3.3].
- **Inside a BBC simulation.** Dixon et al. 2026 (TITAN simulations) fit α, β, γ (mass step), ℳ
  with redshift-binned distances in BBC "to break the degeneracy between nuisance parameter
  estimation and the cosmological model", with a lensing error 0.055z and **no** velocity term in
  the distance errors, since the forward likelihood models it [src: arXiv:2606.14962, Sect. IV.1,
  Eq. 5].

### Step 2. Convert residuals to velocities, or keep magnitudes
<!-- key: step-2-convert-residuals-to-velocities-or-keep -->

To first order in v/c (Hui & Greene 2006, Eq. 15, as derived in App. A.1),

    v̂_i = −(ln10 c/5) [ (1 + z_i) c / (H(z_i) r(z_i)) − 1 ]⁻¹ Δμ_i                       (Eq. 21)
    σ_v̂ ≃ 1400 (z/0.1)(σ_μ/0.1) km/s                             (arXiv:2303.01198, Eq. 23)

[src: arXiv:2303.01198, Sect. 3.1.2]. z_i should be z_cos; using z_obs is "only a second order
approximation", biased for nearby fast objects; the paper compares four variants (v̂1–v̂4, the
last being Watkins–Feldman) and keeps Eq. 21 as "the least biased"; all biases are < ~5 % for v ~
300 km/s, and the Ω_m dependence of the prefactor is negligible [src: Sect. 3.1.2, App. A.2–A.3].
The variant v̂2 = −(ln10 c/5) H r/(1 + z) Δμ (Eq. 49) is the one used by Howlett et al. 2017,
Huterer et al. 2017 and Lai et al. 2023 [src: App. A.2].

The magnitude route writes the same physics as δm = α(z) v_r with

    α(z) = (5 / c ln10) [ 1 − c (1 + z)² / (H(z) D_L(z)) ]                               (Eq. 12)

[src: arXiv:2510.07673, Sect. 2.2]. Since D_L = (1 + z) r, c(1 + z)²/(H D_L) = (1 + z)c/(H r), so
Eq. 12 is the inverse of the prefactor of Eq. 21 [der: algebra on the two equations]. Crisman et
al. carry the curvature generalisation, the bracket becoming 1 − (1 + z)² 𝒞_k(χ)/(H d_L) with 𝒞_k
= cosh[H0 sqrt(Ω_k) χ] (Eq. 4) [src: arXiv:2604.06361, Sect. 2.1].

Which quantity is Gaussian decides the likelihood. Huterer et al. model SNe as Gaussian in the
magnification μ = −2[10^{Δm/5} − 1] (Eq. 9), not in Δm, because below z = 0.01 "the signal,
expected to be Gaussian in μ, is therefore not Gaussian in magnitude", while for 6dFGS galaxies,
whose ~27 % errors are near-Gaussian in log distance and > 99 % of which lie at z > 0.01, they
stay Gaussian in log distance [src: arXiv:1611.09862, Sect. 3.2]. Carreres et al. check that their
v̂ are Gaussian (App. A.4) [src: arXiv:2303.01198, Sect. 3.2.4].

### Step 3. Build the covariance
<!-- key: step-3-build-the-covariance -->

**Velocity space** (Carreres et al. 2023):

    C_ij = C^vv_ij(fσ8, σ_u) + [σ_v² + σ²_v̂,i(p_HD)] δ_ij                                 (Eq. 38)

with the linear C^vv of physics-and-methods §3 and parameters p = {fσ8, σ_v, σ_u}; maximised with
iminuit (Hesse or Minos errors), checked against emcee [src: Sects. 3.2.4, 3.3]. With estimated
velocities σ_u is unconstrained and drifts high with fσ8, so a Gaussian prior centred on 15
h⁻¹Mpc with 50 % width is imposed; with true velocities σ_u = 14.6 ± 0.5 is recovered [src: arXiv:2303.01198,
Sect. 4.2].

**Magnitude space** (Huterer et al. 2017):

    S_ij = (5/ln10)² [(1 + z_i)²/(H(z_i) d_L(z_i))] [(1 + z_j)²/(H(z_j) d_L(z_j))] ξ_ij      (Eq. 4)
    ξ_ij = (dD_i/dτ)(dD_j/dτ) ∫ dk/(2π²) P(k) Σ_ℓ (2ℓ + 1) j′_ℓ(kχ_i) j′_ℓ(kχ_j) [P_ℓ(n̂_i·n̂_j) − δ_ℓ0]  (Eq. 5)
    L(A) ∝ |C|^{-1/2} exp(−½ Δmᵀ C⁻¹ Δm),   C = A S + N                                  (Eq. 6)

with A = 1 in the fiducial ΛCDM and A = 0 for noise only; ℓ_max = 20 unless cos θ > 0.95, where
200 is used; the halofit non-linear P(k) because objects at z ≲ 0.01 with small separations
"contribute appreciably"; O(10⁸) elements for O(10⁴) objects took "about 12 hours on a modern
24-core desktop" [src: arXiv:1611.09862, Sects. 3–3.2]. Crisman et al. split C = C^PV(λ_c) +
C^nonlin(σ_v) + C^cat (Eq. 2), with C^nonlin_ii = [5σ_v/(z ln10)]² (Eq. 5) and σ_v free; the
Pantheon+ and DES-Dovekie covariances already contain an effective ~240 km/s velocity term,
which they **remove** "to avoid any potential double counting" and replace with their own; the
residual vector and the covariance are recomputed at every step [src: arXiv:2604.06361, Sect.
2.1]. Letting σ_v differ between z < 0.05 and 0.05 < z < 0.1 did not shift the parameters and was
disfavoured by BIC [src: same].

**Correlation functions** (Nguyen et al. 2025): the auto-correlation of δm and its
cross-correlation with DESI BGS galaxies are measured and fitted, the δm–velocity map of Eq. 11
turning velocity correlation models into magnitude ones; the fit is validated on 675 Abacus
realisations with and without SN selection [src: arXiv:2510.07673, Sects. 2.2, 6.2].

### Step 4. Choose the redshift range and the sample
<!-- key: step-4-choose-the-redshift-range-and-the-sample -->

- **Upper limit from selection.** In ZTF simulations Hubble residuals are biased beyond z ~ 0.06,
  reaching Δμ ≃ −0.13 at z ~ 0.12, which "simply translates to a fake outflow"; the cut z_obs <
  0.06 keeps the bias below ~−0.01 mag (⟨N⟩ ~ 1 660 SNe) [src: arXiv:2303.01198, Sects. 4.1–4.2].
  The true velocities are not biased: selection is "mostly a magnitude cut" [src: Sect. 4.1].
  For LSST the analogous window is 0.02 < z < 0.14, the maximum velocity bias ~70 km/s, "almost one
  order of magnitude smaller than the PV measurement error" [src: arXiv:2507.00157, Sect. 4.1].
- **Lower limit.** A sharp z_obs cut is asymmetric in velocity (more high-z_cos objects with
  negative v enter the bin), giving a small positive residual at z_obs = 0.02 that z_cos removes
  [src: arXiv:2303.01198, Sect. 4.1]; the LSST simulation sees "a large reverse Malmquist bias for
  z < 0.02, due to saturation" and cuts there also to stay in the Hubble flow [src:
  arXiv:2507.00157, Sect. 4.1]. Huterer et al. instead keep z < 0.01, where the signal-to-noise is
  largest, which is why they move to the magnification likelihood [src: arXiv:1611.09862, Sect.
  3.2].
- **Where the information saturates.** Crisman et al. stop at z = 0.1 (Pantheon+, 628 SNe) and
  0.2 (DES-Y5, 243; DES-Dovekie, 245), having "explicitly tested" that the velocity information
  saturates below these limits [src: arXiv:2604.06361, Sect. 2.1]; Huterer et al. find constraints
  "negligibly improve after z_max ≃ 0.05" [src: arXiv:1611.09862, Sect. 4.1]. Nguyen et al. use 510
  unique Pantheon+ SNe at z < 0.1, z_eff = 0.03 as the mean SN redshift [src: arXiv:2510.07673,
  Sect. 3.3]; the difference from Crisman's 628 is not explained in either text read.
- **Light-curve cuts.** Huterer et al.: x1 < 3, σ_x1 < 1, c < 0.3, σ_c < 0.1, fit probability >
  10⁻³, σ_t0 < 2 days, then a 4σ Hubble-diagram clip [src: arXiv:1611.09862, Sect. 2.1]. TITAN: −3
  < x1 < 3, −0.3 < c < 0.3, σ_x1 < 1, σ_t0 < 1 day, σ_c < 0.1 [src: arXiv:2606.14962, Sect. IV.1].

### Step 5. Assign the redshift
<!-- key: step-5-assign-the-redshift -->

The host redshift is assumed external and exact in the ZTF and LSST simulations [src:
arXiv:2303.01198, Sect. 2.6]. For LSST the fraction of SNe with a host spectroscopic redshift is
modelled as R_host(z) = R_spectro(z) × R_SN(z) for DESI BGS, 4MOST CRS-BG and 4HS (Eq. 3) [src:
arXiv:2507.00157, Sect. 2.4.1]. Replacing the host redshift by a group mean removes virial motion:
on 173 Pantheon+ hosts with AAT group redshifts, the Hubble-residual standard deviation falls from
0.324 to 0.285 mag (δ = sqrt(STD²_indiv − STD²_group) = 0.155 mag, Eq. 2), and from 0.513 to 0.407
mag for large groups at z < 0.018; groups include pairs, the mean is unweighted [src:
arXiv:2408.14560, Sects. III.2.1, V.2]. A group redshift is not a velocity-free redshift: it keeps
the group's own coherent motion, which is the signal.

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Velocity-covariance, magnitude-covariance, correlation-function or velocity–density route
<!-- key: velocity-covariance-magnitude-covariance -->

| Route | Fits | Assumes | Cost | Analysis |
|---|---|---|---|---|
| Velocity covariance | fσ8, σ_v, σ_u (+ p_HD) | linearised Δμ → v, Gaussian v̂ | dense N × N matrix; σ_u needs a prior | arXiv:2303.01198 |
| Magnitude covariance | A (or σ8, γ, Ω_k with CMB) + σ_v or Δσ_int, ΔM | ΛCDM shape of P(k); no conversion to v | 10⁸ elements for 10⁴ objects (arXiv:1611.09862, Sect. 3.1); parameters other than fσ8 need a cosmology | arXiv:1611.09862; arXiv:2604.06361 |
| Correlation functions (× galaxies) | fσ8 from δm auto and δm–galaxy cross | mock covariance, linear α(z) | needs a galaxy sample on the same sky and mocks | arXiv:2510.07673 |
| Velocity–density | β (→ fσ8) | a reconstruction and linear theory | reconstruction systematics | arXiv:2606.14962; `deep/velocity-density-comparison.md` |

The magnitude route quotes A, σ8 or γ, not fσ8 directly: Crisman et al. "quote σ8 and γ, never
fσ8" (L2). The correlation-function route is the only one of the four with a measured
**cross** with galaxies, a quantity that vanishes if δm is pure noise [der: δm uncorrelated
with galaxies when it carries no velocity].

### Likelihood Gaussian in magnitude or in magnification
<!-- key: likelihood-gaussian-in-magnitude-or-in -->

On Supercal SNe to z = 0.1, a likelihood Gaussian in magnitude instead of magnification shifts
the peak of A to 0.71, by −0.07 or ~0.3σ, with an unchanged error; restricted to z > 0.01 the two
give "nearly identical" posteriors [src: arXiv:1611.09862, Sect. 4.1]. The choice therefore
matters only when the lowest-redshift SNe are kept.

### σ_v fixed in the published covariance, or free
<!-- key: sigmav-fixed-in-the-published-covariance-or-free -->

A compilation covariance with a fixed ~240 km/s velocity term and a likelihood that adds its own
σ_v count the same scatter twice; Crisman et al. remove the fixed term [src: arXiv:2604.06361,
Sect. 2.1]. Carreres et al. fit σ_v; Huterer et al. absorb it in Δσ²_int [src: arXiv:2303.01198,
Sect. 3.2.4; arXiv:1611.09862, Sect. 3.2].

### Intrinsic-scatter model in the bias correction
<!-- key: intrinsic-scatter-model-in-the-bias-correction -->

With TITAN "data" simulated under each model and BS21 bias corrections, fσ8 is recovered within
0.1 % for BS21 but is −2.1 % (0.7σ of the mean) for G10 and −6.4 % (2.2σ) for C11, mock scatter
0.031–0.035; C11 "predicts a color distribution that becomes intrinsically more skewed at redder
colors, mimicking the effect of gravitationally induced velocities"; a c < 0.2 cut before the
BiasCor stage reduces the C11 offset to −4.6 % [src: arXiv:2606.14962, Sect. V.3]. The authors
regard the G10 and C11 results as "overly conservative", since DES finds both models fit worse
[src: same]. Other SN variants in their budget: the mass-step location shifted by 0.2 dex to
log M* = 10.2, and the ATLAS efficiency curve shifted by 0.2 mag [src: Sect. IV.4.1].

### Spectroscopic or photometric typing
<!-- key: spectroscopic-or-photometric-typing -->

Above ~2 % contamination the Gaussian velocity likelihood breaks, the residual and velocity pulls
become skewed, and some realisations return fσ8 ~ 0; the photometrically typed sample loses SNe
Ia through classifier efficiency and so has a larger error than the pure sample [src:
arXiv:2507.00157, Sect. 5].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Velocity error per SN | ≃ 1400 (z/0.1)(σ_μ/0.1) km/s | ZTF simulation | arXiv:2303.01198 | Eq. 23 |
| Estimator bias | < ~5 % at v ~ 300 km/s; larger at z < 0.02 | ZTF simulation | arXiv:2303.01198 | Sect. 3.1.2, App. A.2 |
| σ_u prior | Gaussian, centre 15 h⁻¹Mpc, width 50 % | ZTF simulation | arXiv:2303.01198 | Sect. 4.2 |
| Joint p + p_HD fit | fσ8/fid = 0.998 ± 0.037, mean error 0.188 (27 mocks, 0.02 < z < 0.06) | ZTF 6-year simulation (**forecast**) | arXiv:2303.01198 | Table 4 |
| True-velocity floor | mean error 0.100, fσ8/fid = 0.991 ± 0.016 | same | arXiv:2303.01198 | Sect. 4.2 |
| Fixed-p_HD fit with σ_u prior | 1.036 ± 0.031, mean error 0.185 | same | arXiv:2303.01198 | Sect. 4.2 |
| Selection-free redshift range | z < 0.06 (ZTF); 0.02 < z < 0.14 (LSST) | simulations | arXiv:2303.01198; arXiv:2507.00157 | Sect. 4.2; Sect. 4.1 |
| Multipole cut in ξ_ij | ℓ_max = 20 (cos θ < 0.95), 200 otherwise | Supercal + 6dFGS | arXiv:1611.09862 | Sect. 3.1 |
| Covariance cost | ~12 h on 24 cores for O(10⁴) objects | same | arXiv:1611.09862 | Sect. 3.1 |
| Magnitude-vs-magnification shift | ΔA = −0.07 (~0.3σ) | Supercal | arXiv:1611.09862 | Sect. 4.1 |
| Fixed velocity term in compilations | ~240 km/s (Pantheon+, DES-Dovekie; none in DES-Y5) | — | arXiv:2604.06361 | Sect. 2.1 |
| Sample sizes for PV fits | 628 (Pantheon+, z < 0.1), 243 (DES-Y5), 245 (DES-Dovekie, z < 0.2); 510 unique Pantheon+ at z < 0.1 | — | arXiv:2604.06361; arXiv:2510.07673 | Sect. 2.1; Sect. 3.3 |
| SN selection effect on fσ8 | mean shifts 0.027, 0.016, 0.0064 for limits m = 16.0, 16.5, 17.0 | 675 Abacus mocks | arXiv:2510.07673 | Sect. 6.2 |
| Group vs host redshift | Hubble-residual STD 0.324 → 0.285 mag (173 SNe) | Pantheon+ hosts, AAT groups | arXiv:2408.14560 | Sect. V.2 |
| Hubble-diagram scatter in TITAN mocks | ~0.17 mag, all scatter models | simulation | arXiv:2606.14962 | Sect. IV.1 |
| Scatter-model sensitivity | −2.1 % (G10), −6.4 % (C11), −4.6 % with c < 0.2 | TITAN simulation | arXiv:2606.14962 | Sect. V.3 |
| Contamination threshold | ~2 % | LSST simulation (**forecast**) | arXiv:2507.00157 | Sect. 5 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Selection read as a flow.** A magnitude-limited, spectroscopically typed sample develops a
  negative Hubble residual with redshift that the velocity estimator turns into an outflow;
  test: residuals of mocks against z_obs and z_cos, and fσ8 against z_max [src:
  arXiv:2303.01198, Sect. 4.1, Fig. 9].
- **Redshift-binned bias corrections.** Shifting a whole shell creates fake correlations (L2).
  TITAN uses a one-dimensional, redshift-dependent correction and notes that x1- and c-dependent
  corrections could reduce the C11 bias [src: arXiv:2606.14962, Sect. V.3].
- **Double-counted small-scale velocities.** A compilation's fixed velocity error plus a fitted
  σ_v [src: arXiv:2604.06361, Sect. 2.1].
- **Red, skewed colours mimicking velocities.** Scatter models with a skewed red tail bias fσ8
  low; test by simulating data under each model, not only varying the bias-correction model
  [src: arXiv:2606.14962, Sect. V.3].
- **Errors that ignore the velocity covariance.** In LSST mocks the scatter of residuals across
  realisations exceeds the mean error at z < 0.1 when the PV covariance is left out [src:
  arXiv:2507.00157, Sect. 4.1].
- **Contaminants.** Above ~2 % the likelihood fails [src: arXiv:2507.00157, Sect. 5].
- **Coherent calibration errors.** SN velocities are coherent on the sky, so the analysis is
  "more sensitive to biases in individual SNe or subsamples located in particular regions of the
  sky than the usual isotropic analysis", which is why the Supercal recalibration and bias
  corrections "will have some impact on inferences of A" [src: arXiv:1611.09862, Sect. 2.1]. Test: vary z_max and the
  low-z subsample, as Huterer et al. do, and check stability of A [src: Sect. 4.1].
- **Shared supernovae.** DES-Y5 and Pantheon+ overlap at low z, and DES-Y5 has "clumped
  patches" at the DES deep fields [src: arXiv:2604.06361, Sect. 2.1]; results from the two are not
  independent (L2).

## Reading list
<!-- key: reading-list -->

- Turner 2024, arXiv:2411.19484, Sect. 3.2 — review: SNe Ia as velocity tracers.
- Huterer et al. 2017, arXiv:1611.09862, Sects. 3–4 — method: magnitude-space covariance,
  amplitude A, magnification likelihood, nuisance marginalisation.
- Carreres et al. 2023, arXiv:2303.01198, Sects. 3–4 and App. A — method: velocity-space
  likelihood on realistic ZTF simulations, estimator comparison, selection.
- Crisman, Quartin & Rebouças 2026, arXiv:2604.06361, Sect. 2.1 — application: current
  compilations, σ_v treatment, curvature-generalised covariance.
- Nguyen et al. 2025, arXiv:2510.07673, Sects. 2–3, 6 — application: SN magnitude × galaxy
  correlation functions with mock validation.
- Rosselli et al. 2025, arXiv:2507.00157, Sects. 2.4, 4–5 — forecast: LSST host redshifts,
  redshift window, contamination.
- Dixon et al. 2026, arXiv:2606.14962, Sects. IV–V — critique: SN modelling systematics, the
  intrinsic-scatter model as the leading term.
- Peterson et al. 2024, arXiv:2408.14560, Sects. III, V — method: group-averaged redshifts.

## Not verified
<!-- key: not-verified -->

- Carreres et al. 2025 (arXiv:2405.20409, ZTF DR2 peculiar velocities on the Hubble diagram), the
  subtopic's named source: not re-read for this dossier; its numbers in L2 stand.
- Hui & Greene 2006 and Gordon et al. 2007 bodies; the HSS paper cited by Huterer et al. for the
  full-sky window approximation.
- The Nguyen et al. correlation-function estimators and their fitted scales (Sects. 5, 7): not
  read; only the δm–v relation, the sample and the selection test.
- The Tsagas et al. 2025 review Sect. 10.1.
- The reason why the two papers quote different numbers of Pantheon+ SNe at low redshift (light
  curves against unique SNe is a possible but unchecked explanation).
