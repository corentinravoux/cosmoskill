# Velocity–density comparison — cosmo-peculiar-velocities dossier

Scope: how a growth rate is obtained by comparing measured peculiar velocities with a velocity
field predicted from a redshift survey (reconstruction, bias normalisation, line-of-sight
likelihood, β → fσ8, linearisation of σ8), and how to choose between the likelihoods, the
error models and the normalisation recipes in use.
Snapshot: 2026-10-17.
From: Turner 2024 review (arXiv:2411.19484), Sect. 5.3; Cosmicflows reconstructions (Tsagas et
al. 2025, arXiv:2510.05340, Sect. 2.2.3).

Already in L2, not repeated here: the list of analyses and their fσ8 values in
`results.md#published-fsigma8-from-peculiar-velocities` and
`results.md#history-of-the-key-numbers-what-is-superseded`; the three meanings of β in
`physics-and-methods.md#conventions-units-and-where-the-community-is`; the Malmquist sizes of
Stiskalek 2025 in `systematics.md#malmquist-bias-and-the-distance-prior`; the 1.04 method bias,
the TITAN budget total and the residual-flow values in
`systematics.md#reconstruction-systematics-velocity-density` and
`results.md#residual-external-bulk-flows-from-velocity`; the 6.5 % linear/non-linear offset in
`results.md#linear-against-non-linear-sigma8`.

Notation: this file follows Carrick et al. 2015 (arXiv:1504.04627) and Stiskalek 2025
(arXiv:2509.20235). β* = f/b* with b* the bias of an L* 2M++ galaxy; u(r) the predicted
velocity for β* = 1; σ_v the residual velocity scatter in km/s (not the σ_u damping scale of the
field-level papers); V_ext a constant external dipole; d and σ_d (or μ and σ_μ) the catalogue
distance (distance modulus) and its error.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Predict the velocity from the galaxy density
<!-- key: step-1-predict-the-velocity-from-the-galaxy -->

Linear theory gives the velocity from the mass density contrast δ,

    v(r) = (f/4π) ∫ d³r' δ(r') (r' − r)/|r' − r|³        (arXiv:1504.04627, Eq. 1)

with distances in km/s (r = HR) [src: Sect. 1]. Written with the galaxy field normalised to the
bias of an L* galaxy, δ*_g = δ_g/ψ(r), the prefactor becomes β*/4π (Eq. 9) [src: Sect. 2.4].
In h⁻¹Mpc units the H0 dependence cancels (arXiv:2509.20235, Eq. 1) [src: Sect. 2]. The
Fourier form used in simulation tests is ṽ_i(k) = −iaHf (k_i/k²) δ̃_m(k) (Turner & Blake 2023,
arXiv:2306.16664, Eq. 1), with redshift-space distortions neglected [src: Sect. 2]. The
Wiener-filter route writes the same relation as ∇·v = −fσ8 H δ̂ with δ̂ = δ_g/σ8^g(r) (Lilow &
Nusser 2021, arXiv:2102.07291, Eqs. 1–3), so that fσ8 multiplies the field directly [src:
Sect. 2.1].

The 2M++ reconstruction (Carrick et al. 2015), still the field behind most current analyses
[src: arXiv:2509.20235, Sect. 2; arXiv:1912.09383, Sect. 3.2], is built in seven steps per
iteration [src: arXiv:1504.04627, Sect. 2.5]:

1. fit a Schechter luminosity function and compute luminosity (or number) weights, Eqs. 5–6;
2. set 2MRS galaxies beyond 125 h⁻¹Mpc to zero weight; clone galaxies to fill incompleteness
   and the Zone of Avoidance (|b| < 5°, |b| < 10° near the Galactic centre, cloned from
   adjacent strips) [src: Sect. 2.1];
3. grid the weighted galaxies within 200 h⁻¹Mpc;
4. normalise δ_g to the bias of an L* galaxy and smooth with a 4 h⁻¹Mpc Gaussian;
5. predict velocities with Eq. 9;
6. turn redshifts into distances with the predicted line-of-sight velocity, using
   (1 + z_obs) = (1 + z_cos)(1 + z_pec) and H0R ≃ c[z_cos − (1 + q0)z_cos²/2] (Eqs. 2–3);
7. average the last five distance predictions per galaxy to damp oscillations in
   triple-valued regions.

Galaxies are first grouped by friends-of-friends and placed at the group redshift to suppress
fingers of God, and β* is raised "adiabatically" from 0 to 1 in steps of 0.01, in the Local
Group frame [src: same]. The procedure was found unbiased in β* on an N-body ΛCDM simulation
[src: same]; Hollinger & Hudson 2024 quote it as raising β by a factor 1.03 at 4 h⁻¹Mpc
smoothing relative to true distances, and multiply their mock β by that factor [src:
arXiv:2312.03904, Sect. 3.1.2, item 3].

The velocity field is computed once, for β* = 1, and scaled in the likelihood: "the scaling by
β* is applied only at this stage" [src: arXiv:2509.20235, Sect. 4, after Eq. 19].

### Step 2. Normalise the galaxy bias with distance
<!-- key: step-2-normalise-the-galaxy-bias-with-distance -->

In a flux-limited survey the mean luminosity, hence the bias, rises with depth. Carrick et al.
use the luminosity-dependent bias b/b* = (0.73 ± 0.07) + (0.24 ± 0.04) L/L* of Westover (2007)
and the number- or luminosity-weighted effective bias b_eff(r) = ψ(r) b* (Eqs. 7–8) [src:
arXiv:1504.04627, Sect. 2.4]. Two alternatives exist:

- Fit σ8 of the mock galaxy field in equal-volume shells with a parametric F(r) and divide δ_g
  by it; the bias of this variant is ζ† = β_norm/(f σ8,m) (Hollinger & Hudson 2024,
  arXiv:2312.03904, Eq. 11) [src: Sect. 5.2]. The Westover correction would "significantly
  over-correct" their semi-analytic mocks, which are less clustered than the real Universe;
  whether it over-corrects the data is left open [src: same].
- Estimate σ8^g(r) from the survey and divide by it before the reconstruction, so that the
  field depends on σ8 alone (arXiv:2102.07291, Eq. 2) [src: Sect. 2.1].

### Step 3. Write the likelihood along each line of sight
<!-- key: step-3-write-the-likelihood-along-each-line-of -->

The observable is the redshift; the catalogue distance enters as a prior on the true distance.
In the forward likelihood of Pike & Hudson 2005 as written by Carrick et al. [src:
arXiv:1504.04627, Sect. 4.2.2]:

    P(cz)   = ∫ dr P(cz|r) P(r)                                    (Eq. 17)
    P(cz|r) = (2πσ_v²)^{-1/2} exp{−[cz − cz_pred]²/(2σ_v²)}         (Eq. 18)
    1 + z_pred = (1 + z_cos(r, h̃)) (1 + β* u(r)/c)                  (Eq. 19)
    P(r) ∝ exp{−[r − d]²/(2σ_d²)} [1 + δ*_g(r)]                      (Eq. 21)

with h̃ a nuisance that rescales the published distances (Eq. 20) and V_ext added to the
velocity [src]. Boruah et al. 2020 rewrite the prior in distance modulus, with the volume term
r² for distances not yet corrected for homogeneous Malmquist bias (arXiv:1912.09383, Eq. 10) and
1 + z_pred = (1 + z_cos)(1 + (βv + V_ext)·r̂/c) (Eq. 7); a Gaussian instead of log-normal
distance error changes β by < 0.35σ [src: Sect. 4.2, footnote 3].

Stiskalek 2025 generalises the prior to the tracer's own bias and selection [src:
arXiv:2509.20235, Sect. 4]:

    π(r | r̂_obs, θ) = r² n(r r̂_obs, θ) f(r, θ) / Z(θ)               (Eq. 13)
    f(r, θ) = exp[−(r/R)^q]                                          (Eq. 12)
    n(r, b1) = 1 + b1 δ(r)    [quadratic variant + b2 δ², Eq. 16]     (Eq. 14)
    L(z_obs | r, θ) = N(z_obs; z_pred, sqrt(σ_v² + σ_cz²))            (Eq. 17)
    V_pec = (β* v(r) + V_ext)·r̂_obs                                  (Eq. 19)

where R and q (a depth and a sharpness of the radial incompleteness) are inferred with the
rest, n is smoothed as ½(n + sqrt(n² + τ²)) with τ = 0.01 to keep it positive (Eq. 15), and
b1 is the bias of the velocity tracer relative to 2M++, one per sample, with a uniform prior
[src]. The indicator relation is fitted in the same model: for TF a Gaussian hyperprior on the
true linewidth η_true and m_pred = μ(r) + M(η_true) (Eqs. 20–22); for FP a correlated Gaussian
hyperprior on log σ0 and log I_e and a prediction of log θ_eff (Eqs. 23–24); r and η_true are
marginalised numerically at every MCMC step [src]. Boruah et al. had introduced the joint
calibration for SNe (α, ℬ, M, σ_int) and TF (a, b, σ_int), restoring the r² term (Eq. 16) [src:
arXiv:1912.09383, Sect. 4.2.1].

### Step 4. Convert β* to fσ8 and linearise σ8
<!-- key: step-4-convert-beta-to-fsigma8-and-linearise -->

fσ8 = β* σ8*^g, with σ8*^g = ⟨σ8,g(r)/ψ(r)⟩ from counts in cells in radial shells: 0.99 ± 0.04
for 2M++, the error being the scatter between shells, "more conservative than the formal errors"
[src: arXiv:1504.04627, Sect. 4.3]. The product is a non-linear-σ8 quantity; three recipes have
been used to linearise it:

| Recipe | Used by | Result on its data | Place read |
|---|---|---|---|
| Juszkiewicz et al. 2010, Ω_m = 0.3 | Carrick 2015; Boruah 2020 | 0.427 ± 0.026 → 0.401 ± 0.024 (0.398 with Ω_m = 0.266) | arXiv:1504.04627, Sect. 4.3; arXiv:1912.09383, Sect. 5.2.1 |
| halofit, "better matches the measured particle σ8 in MDPL2" | Hollinger & Hudson 2024 | 0.398 ± 0.025 → 0.362 ± 0.023 | arXiv:2312.03904, Sect. 6.1 |
| syren-new emulator, root-finding on A_s | Stiskalek 2025 | Juszkiewicz "inaccurate at the level of 3–5 per cent" | arXiv:2509.20235, Sect. 2 |

Hollinger & Hudson state that halofit gives "a larger correction than in our previous work"
[src]. The choice of recipe therefore moves fσ8,lin by several per cent before any data
systematic.

### Step 5. Calibrate the method on mocks
<!-- key: step-5-calibrate-the-method-on-mocks -->

Hollinger & Hudson regress true halo velocities on predicted ones in 2M++-like mocks built from
semi-analytic models on MDPL2, fit β and V_ext (Eq. 7), compute σ8 of the mock galaxy field in
non-overlapping spheres, and form ζ* = (β/f)(σ8,g/σ8,m) (Eq. 8), which equals 1 for an unbiased
method [src: arXiv:2312.03904, Sect. 3.1.2]. Velocities are compared at the central galaxy of
each halo, for consistency with the grouped redshifts of the data [src: same]. The weighted
corrections are ζ† = 1.01 for each of the four Boruah et al. samples and 1.04 for the two FP
samples of Said et al.; fσ8 = β_norm/ζ† (Eq. 12) [src: Sect. 6.1].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Forward likelihood, inverse VELMOD or χ²
<!-- key: forward-likelihood-inverse-velmod-or-chi2 -->

Carrick et al. ran three on the same 2M++ field [src: arXiv:1504.04627, Sects. 4.2, 4.3,
Table 1]:

| Method | Malmquist treatment | β* (LW) |
|---|---|---|
| forward likelihood (A1 + SFI++) | homogeneous and inhomogeneous, through P(r) | 0.431 ± 0.021 |
| inverse VELMOD (SFI++ galaxies; σ_v = 150 km/s) | insensitive to inhomogeneous, homogeneous in the likelihood | 0.387 ± 0.048 |
| χ², Eq. 22 | none; "expected to be biased high" | 0.444 ± 0.026 (χ²/dof 2194/2899) |

Inverse VELMOD predicts the linewidth from the magnitude and is chosen over forward VELMOD
because SFI++ is a compilation whose selection is hard to model, and inverse fits depend only
weakly on it [src: Sect. 4.2.1, Eqs. 11–16]. Boruah et al. keep χ² only as a goodness-of-fit
diagnostic: its slope "is biased high due to inhomogeneous Malmquist bias" [src:
arXiv:1912.09383, Sect. 5.1.1].

### Evaluate the predicted velocity at the redshift or at a sampled distance
<!-- key: evaluate-the-predicted-velocity-at-the-redshift -->

- Lilow & Nusser evaluate v_r at the redshift distance s = d_com(z_obs), not at the distance
  inferred from μ, "to minimize the spatial Malmquist bias effect", and compare distance moduli
  through μ ≈ μ(z_obs) − η(z_obs) v_r (Eqs. 23–24, with η here a magnitude-per-velocity factor,
  not the log-distance ratio) [src: arXiv:2102.07291, Sect. 2.6].
- Boubel et al. 2024 query a redshift-space version of the field at each observed redshift. Stiskalek
  calls this a "partial" forward model, whose factorisation p(z_obs, z_cos) = p(z_cos|z_obs)
  p(z_obs) puts a prior on observed data; the correct treatment is a likelihood for z_obs and a
  prior on z_cos, which carries inhomogeneous Malmquist bias [src: arXiv:2509.20235, Sect. 6,
  Eq. 28].
- Sampling the real-space distance and integrating over it (Eqs. 17–21 of arXiv:1504.04627;
  Eq. 13 of arXiv:2509.20235) handles triple-valued regions; Carrick et al. give that as the
  reason their β* is insensitive to misplaced galaxies [src: arXiv:1504.04627, Sect. 5.1].

### Tracer bias b1 fixed to 1 or free
<!-- key: tracer-bias-b1-fixed-to-1-or-free -->

A prior P(r) ∝ r²[1 + δ_g(r)] (Said et al. 2020, Eq. 23, as read by Stiskalek) fixes b1 = 1.
All samples of Stiskalek 2025 prefer b1 significantly different from 1, and β* and b1 are
degenerate: fixing b1 below the preferred range raises β*; for SDSS FP, b1 = 1 drives β* to
~0.51, i.e. in the direction opposite to the low fσ8 Said et al. report, so b1 alone does not
explain it [src: arXiv:2509.20235, Sect. 6, Fig. 7 text]. Other differences named there: the
1/S_n likelihood weighting for selection in Said et al., "without clear justification from first
principles", against selection parameters inferred jointly; and the FP likelihood written in θ_eff
rather than log θ_eff [src].

### σ_v fixed or free
<!-- key: sigmav-fixed-or-free -->

Carrick et al. and Boruah et al. fix σ_v = 150 km/s from N-body tests [src: arXiv:1504.04627,
Sect. 5.1; arXiv:1912.09383, Sect. 4.1]; Boruah et al. state that fitting it "does not change
the results" [src: Sect. 4.1], but find in simulated SNe a degeneracy
σ_v ≈ [137 + 220(σ_int/0.08 − 1)] km/s, so fitting σ_v and σ_int together "can result in
significant bias" [src: App. A, Fig. 14 caption]. Stiskalek uses a Maxwell–Boltzmann prior
with ⟨σ_v⟩ ≈ 200 km/s (scale a = 125 km/s), with negligible effect [src: arXiv:2509.20235,
Sect. 4]. Dixon et al. 2026 leave σ_v free with a flat prior [src: arXiv:2606.14962, Sect.
IV.2, Eq. 11].

### Diagonal errors or the full covariance of the reconstruction
<!-- key: diagonal-errors-or-the-full-covariance-of-the -->

This is the choice that sets the error bar. Blake & Turner 2024 (arXiv:2408.05660) compare, on
400 Gaussian realisations, the power-spectrum method with the reconstruction-and-scaling
method, the latter with χ² = wᵀC⁻¹w, w_n = u(x_n) − α(x_n)(β/β_fid) v(x_n) (Eqs. 30–31) [src:
Sect. 3.3]. C_mn contains the auto- and cross-correlations of the true and reconstructed
velocities plus noise (Eq. 32); it reduces to noise alone only with no velocity bias (α = 1), no
smoothing, uniform selection and infinite tracer density [src]. The off-diagonal terms "are
typically not included" in Eq. 22 of Carrick et al., Eq. 26 of Said et al. and Eq. 9 of Boruah
et al. [src]. Result: with noise-only errors the scatter of best fits is "significantly larger
than the mean error", and the quoted fractional error does not shrink with the volume of the
velocity sample; with the full covariance the errors match the power-spectrum method and a
Fisher forecast [src: Sect. 4]. The authors offer this as "a potential explanation of the
difference between the growth rate errors previously reported by the two methods" and stress
that their test omits windows, distance-dependent errors, RSD and non-linear bias [src: Sect. 5].

Two partial answers exist. The 2M++ analyses bootstrap both the density and the velocity
catalogues, and find that each contributes "essentially equal amounts" to the error [src:
arXiv:1504.04627, Sect. 4.3]. The calibrated mocks give 5 % mock-to-mock scatter on fσ8 from the
finite 2M++ volume (4 % in Carrick et al. from shells), "the dominant source of error"; combining
six sub-samples needs an extra term because their β differ by more than their measurement
errors, which the authors attribute to sample variance [src: arXiv:2312.03904, Sect. 6.1]. The
three combinations agree: β = 0.390 ± 0.024 (error inflated to χ² = dof), 0.402 ± 0.022
(jackknife over surveys), 0.402 ± 0.023 (mock covariance) [src]. On TITAN-like mocks, Dixon et
al. find no under-estimate of errors and attribute the difference with Blake & Turner to a tuned
smoothing scale and a catalogue that samples the density well below 4 h⁻¹Mpc [src:
arXiv:2606.14962, Sect. VI.1].

### Correcting the model velocity for its own stochasticity
<!-- key: correcting-the-model-velocity-for-its-own -->

The mean true velocity at fixed predicted velocity v is ū = (r σ_u/σ_v) v (Turner & Blake 2023,
arXiv:2306.16664, Eq. 3), with σ_u², σ_v², σ_uv² the true, reconstructed and cross variances
(Eqs. 4–6; here σ_u and σ_v are velocity rms values in that paper's notation, not damping
scales), r = σ_uv²/(σ_u σ_v), and D(k) = exp(−k²λ²/2) the smoothing kernel [src: Sect. 2]. On 400
lognormal boxes, fitting f with v_mod = v is biased for λ = 5, 10 and 20 h⁻¹Mpc, while
v_mod = (rσ_u/σ_v)v is unbiased [src: Sect. 3, Fig. 4 text]. The 2M++ papers instead calibrate
the end-to-end bias on mocks (ζ*, ζ†).

### Smoothing scale
<!-- key: smoothing-scale -->

4 h⁻¹Mpc was chosen as "the best compromise" between scatter of predicted against simulated
velocities and an unbiased slope [src: arXiv:1504.04627, Sect. 2.3]. In TITAN mocks, 3 and 5
h⁻¹Mpc variants shift fσ8 by 0.002 ± 0.012 [src: arXiv:2606.14962, Table 2].

### Wiener filter and constrained realisations instead of direct smoothing
<!-- key: wiener-filter-and-constrained-realisations -->

Lilow & Nusser apply a Wiener filter in a spherical Fourier–Bessel basis to 2MRS and draw
constrained realisations from lognormal, Poisson-sampled fields; they cite Keselman & Nusser
(2017) that on scales ≳ 5 h⁻¹Mpc non-linear dynamical reconstructions are compatible with
linear theory on realistic redshift catalogues, the gain being offset by selection, shot noise
and fingers of God [src: arXiv:2102.07291, Sect. 8.2]. Their likelihood of Δμ includes a
covariance C_Δμ (Eq. 26) and free (fσ8, B_ext, h_obs) [src: Sect. 2.6].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Smoothing | 4 h⁻¹Mpc Gaussian | 2M++ | arXiv:1504.04627 | Sect. 2.3 |
| Reconstruction volume | 200 h⁻¹Mpc; 2MRS weight 0 beyond 125 | 2M++ | arXiv:1504.04627 | Sect. 2.5 |
| Field grid | 256³ in a 400 h⁻¹Mpc box | 2M++ | arXiv:2509.20235 | Sect. 2 |
| Bias–luminosity relation | b/b* = 0.73 + 0.24 L/L* | Westover 2007, used by 2M++ | arXiv:1504.04627 | Sect. 2.4 |
| σ8*^g | 0.99 ± 0.04 | 2M++ | arXiv:1504.04627 | Sect. 4.3 |
| σ_v | 150 km/s fixed; ⟨σ_v⟩ ≈ 200 prior | Carrick, Boruah; Stiskalek | arXiv:1504.04627; arXiv:2509.20235 | Sect. 5.1; Sect. 4 |
| Kaiser rocket fix | β* changes by 3 % | 2M++ | arXiv:1504.04627 | Sect. 5.1 |
| V_ext preference | Δχ² = 34 for 3 dof, 5.1σ | 2M++ | arXiv:1504.04627 | Sect. 4.3 |
| Reconstruction β factor | 1.03 at 4 h⁻¹Mpc | 2M++ mocks | arXiv:2312.03904 | Sect. 3.1.2 |
| ζ† per sample | 1.01 (A2, SFI field, SFI groups, 2MTF); 1.04 (6dF FP, SDSS FP) | 2M++ mocks | arXiv:2312.03904 | Sect. 6.1 |
| Cosmic variance on fσ8 | 5 % (mocks), 4 % (shells) | 2M++ | arXiv:2312.03904 | Sect. 6.1 |
| Edge effect | within 20 h⁻¹Mpc of the boundary: σ_v +~75 km/s, β biased 20–30 % (as cited) | 2M++ mocks | arXiv:2606.14962 | Sect. VI.1 |
| Linear P instead of non-linear | predicted rms velocity −1.2 % | 2M++ mocks | arXiv:2312.03904 | Sect. 6.1 |
| real/redshift-space σ8^g | ~1.1 (redshift space higher) | 2MRS mocks | arXiv:2102.07291 | Sect. 8.4 |
| TITAN SN systematics | intrinsic-scatter model: C11 −0.014 ± 0.007, G10 −0.005 ± 0.005; σ_sys^SN 0.017 | TITAN mocks | arXiv:2606.14962 | Sect. V.2, Table 2 |
| TITAN reconstruction systematics | smoothing 0.012, depth K < 12.7 0.007, boundary 190→180 h⁻¹Mpc 0.008 (−0.008 shift); σ_sys^recon 0.016 | TITAN mocks | arXiv:2606.14962 | Table 2 |
| Line-of-sight upper limit | R = 200 h⁻¹Mpc; σ8,g within 190 | TITAN mocks | arXiv:2606.14962 | Sect. IV.2, IV.4.2 |
| Intrinsic-scatter bias, C11 vs BS21 | −0.028 (−6.4 %); −0.019 (−4.6 %) with c < 0.2 | TITAN mocks | arXiv:2606.14962 | Sect. VI.1 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Inhomogeneous Malmquist bias left in.** A χ² or point-estimate comparison at the catalogue
  distance biases β high [src: arXiv:1504.04627, Sect. 4.2.3; arXiv:1912.09383, Sect. 5.1.1].
  Test: compare χ² and forward-likelihood β on the same data (Table 1 of arXiv:1504.04627 shows
  0.444 against 0.431).
- **Tracer bias fixed at 1.** Shows as a β* that moves when b1 is freed; test: scan b1 (Fig. 7
  of arXiv:2509.20235) and compare linear and quadratic n(r) [src: Sects. 4, 6].
- **Error bar without the field's sample variance.** Symptom: the fractional error does not
  grow when the velocity sample shrinks. Test: mock-to-mock scatter against the mean quoted
  error, or the full covariance of Eq. 32 of arXiv:2408.05660 [src: Sect. 4].
- **Bias normalisation copied from another sample.** The Westover curve over-corrects the
  semi-analytic mocks; ζ† is near 1 only after normalising with each mock's own σ8(r) [src:
  arXiv:2312.03904, Sect. 5.2]. Test: recover ζ = 1 in shells, excluding the survey edges.
- **Edges and Zone of Avoidance.** ζ† deviates at 125 and 200 h⁻¹Mpc, the two survey depths
  [src: arXiv:2312.03904, Sect. 5.2]; Carrick et al. check high-latitude galaxies (b > 50°) and
  find no shift beyond the random errors [src: arXiv:1504.04627, Sect. 5.1].
- **Kaiser rocket.** Reconstructing in the Local Group frame misplaces galaxies along the LG
  motion; the "Kaiser fix" (Eq. 23, r_K = 1 000 km/s) moves β* by 3 % [src: arXiv:1504.04627,
  Sect. 5.1].
- **Linearisation recipe unstated.** Juszkiewicz, halofit and an emulator give different
  fσ8,lin from one β* (Step 4). Test: quote fσ8 with the non-linear σ8 as well.
- **σ_v and σ_int fitted together for SNe.** Degenerate; can bias both [src: arXiv:1912.09383,
  App. A].
- **SN intrinsic-scatter model.** Pushes fσ8 low through red SNe [src: arXiv:2606.14962, Sect.
  VI.1]. Test: rerun with another model and with a colour cut.
- **Correlated SN systematics in a product likelihood.** The hybrid likelihood (Eqs. 12–16 of
  arXiv:2606.14962) keeps the line-of-sight integrals and adds the off-diagonal part of C_sys;
  its difference term vanishes for uncorrelated SNe [src: Sect. IV.3].

## Reading list
<!-- key: reading-list -->

- Method, the reconstruction: Carrick et al. 2015, arXiv:1504.04627 — iterative 2M++
  reconstruction, three likelihoods compared, σ8*^g, Kaiser fix.
- Method: Boruah, Hudson & Lavaux 2020, arXiv:1912.09383 — forward likelihood in μ, joint
  calibration of SN and TF parameters, σ_v–σ_int degeneracy.
- Method: Stiskalek 2025, arXiv:2509.20235 — tracer bias b1, phenomenological selection, FP in
  log θ_eff, critique of Said 2020 and Boubel 2024.
- Calibration: Hollinger & Hudson 2024, arXiv:2312.03904 — ζ*, ζ†, cosmic variance, halofit
  linearisation.
- Method, alternative: Lilow & Nusser 2021, arXiv:2102.07291 — Wiener filter and constrained
  realisations, comparison in μ at the redshift distance, fσ8 against β.
- Critique: Turner & Blake 2023, arXiv:2306.16664 — stochasticity of the reconstruction and the
  (rσ_u/σ_v) correction.
- Critique: Blake & Turner 2024, arXiv:2408.05660 — diagonal errors under-estimate the error;
  equivalence with the power-spectrum method once the covariance is complete.
- Validation: Dixon et al. 2026, arXiv:2606.14962 — end-to-end SN budget, hybrid likelihood
  with correlated systematics.

## Not verified
<!-- key: not-verified -->

- Pike & Hudson 2005 (arXiv:astro-ph/0511012), where the forward likelihood is introduced, and
  Juszkiewicz et al. 2010 and Westover 2007: cited here through arXiv:1504.04627, bodies not read.
- Said et al. 2020 (arXiv:2007.04993) and Boubel et al. 2024 (arXiv:2301.12648): their
  likelihoods are described here only as Stiskalek 2025 (Sect. 6) reads them.
- The size of the fσ8 bias of the uncorrected reconstruction in arXiv:2306.16664 (Fig. 4, not
  readable as text) and the error ratios of arXiv:2408.05660 (Figs. 4–5).
- Hollinger & Hudson 2021 ("HH21"), the earlier idealised-mock calibration: no identifier read.
- The Appendix A N-body tests of arXiv:1504.04627 (smoothing and σ_v) were not read.
