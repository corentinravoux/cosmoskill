# Bulk flows — cosmo-peculiar-velocities dossier

Scope: how a bulk-flow amplitude and its ΛCDM probability are actually computed — the velocity
assigned to each object, the placement of objects, the weights of each estimator, the window
function, the expectation and covariance for that window, the χ² and its degrees of freedom,
the mock calibration of errors and biases — and how to choose between estimators, windows,
radii and error models.
Snapshot: 2026-10-19.
From: Turner 2024 review (arXiv:2411.19484), Sect. 5.1; Tsagas et al. 2025 review
(arXiv:2510.05340), Sects. 2.3 and 9.1–9.4.

Already in L2, not repeated here: the two definitions of a bulk flow, the r⁻² identity, the Kaiser
MLE, ηMLE and MV weight equations in `physics-and-methods.md#bulk-flow-estimators`; the record of
measured amplitudes, directions and verdicts in `results.md#distance-indicator-bulk-flows` and
`results.md#how-to-read-the-record`; the controversy in
`open-questions.md#is-the-bulk-flow-at-150-250-h-1mpc-anomalous`; the zero-point–monopole
coupling in `systematics.md#zero-point-monopole-calibration`; observer and relativistic effects in
`results.md#how-to-read-the-record`. Residual flows from velocity–density fits (V_ext) are a
different quantity: `deep/velocity-density-comparison.md`.

Notation: s_n (or S_n with noise) the radial peculiar velocity of object n; r̂_n its direction;
u_i (i = x, y, z) the estimated bulk-flow component and U_i the component an **ideal** survey
would measure; w_{i,n} the weight of object n in component i; G_nm = ⟨S_n S_m⟩ the velocity
covariance; σ_n the measurement error and σ* the 1D small-scale velocity noise; R the radius of
the ideal survey; W²_ij(k) the tensor window function; R_ij the expected covariance of the u_i.
Equations follow Peery, Watkins & Feldman 2018 (arXiv:1808.07772) and Watkins et al. 2023
(arXiv:2302.02028) for the MV method, and Nusser & Tully 2026 (arXiv:2608.14265) for shell fits.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Assign each object a velocity and an error
<!-- key: step-1-assign-each-object-a-velocity-and-an -->

Three conventions coexist, and they are not interchangeable.

- **Debiased distance, then v.** Watkins et al. 2023 compute ⟨d_est⟩ = d exp[(κσ_μ)²/2] for a
  Gaussian modulus error σ_μ, κ = ln10/5 (Eq. 6), correct to d_c = 10^{μ/5−5} exp[−(κσ_μ)²/2]
  (Eq. 7) with error σ_c ≈ κσ_μ d (Eq. 13), and take v_c = cz_mod − H0 d_c (Eq. 14) with the
  q0, j0-expanded z_mod (Eq. 15). v_c is unbiased but its errors "are not Gaussian distributed"
  [src: arXiv:2302.02028, Sect. 2]. They tested switching to the Watkins–Feldman v_f (Eq. 17) at
  large distance and it "made virtually no difference": "as long as the velocities are unbiased,
  velocity errors are able average out effectively regardless of their distribution" [src: Sect.
  5].
- **Linearised log distance.** Nusser & Tully 2026 use u_ln,i = −K_i a Δμ_i with Δμ_i = DM_i −
  DM_z,i, a = ln10/5 and K_i → cz_i at low z (Eqs. 5–6), with a diagonal error σ²_u,i = (K_i a
  eDM_i)² + σ²_floor, σ_floor = 100 km/s, the floor preventing objects with tiny reported errors
  from taking "unreasonably large weight"; all objects have cz_CMB > 4 000 km/s, so u/K is a small
  parameter [src: arXiv:2608.14265, Sect. III.1, Eq. 7].
- **The observable itself.** ηMLE (Qin et al. 2018) fits in η and avoids the v ≪ cz assumption of
  the Watkins–Feldman estimator, which "typically converges poorly" and is least accurate exactly
  for the best-measured, nearest objects [src: arXiv:1804.05520, Sect. 4.1.2].

### Step 2. Place the objects
<!-- key: step-2-place-the-objects -->

Positions enter both the estimator weights and the theory covariance. Watkins et al. 2023 place
each group at an inverse-variance mean of d_c and the redshift distance d_z = cz_mod/H0 (Eq. 28,
σ_z = σ_v/H0 with σ_v ≈ 300 km/s): d_c dominates nearby, d_z far away; "the exact value chosen
for σ_v does not have a significant effect" [src: arXiv:2302.02028, Sect. 5]. Nusser & Tully place
every object at its CMB-frame redshift distance, "to reduce sensitivity to Malmquist effects
associated with noisy distance placement" [src: arXiv:2608.14265, Sect. II.2]. Whitford et al.
2023 also place galaxies at their redshifts, noting this trades Malmquist bias for selection bias,
which their selection-matched mocks are meant to capture [src: arXiv:2306.11269, Sect. 4.4].

### Step 3. Choose the target (ideal) quantity and the weights
<!-- key: step-3-choose-the-target-ideal-quantity-and-the -->

**MV.** The ideal survey for the r⁻²-weighted top-hat (L2) is realised as uniformly spread points
with "an equal number of objects per spherical shell", so that U_i = (1/N) Σ_n n̂_n,i s_n (Eq. 15);
the authors prefer this to explicit r⁻² weights because "one can achieve the same accuracy with a
much smaller ideal survey" [src: arXiv:1808.07772, Sect. 4]. The weights solve Eq. 21 (L2) with
two constraints: Σ_n w_{i,n} r̂_n,j = δ_ij (a uniform flow is recovered) and Σ_n w_{i,n} cz_n = 0,
which makes the estimate "completely independent of any uncertainty in the value of H0" because
a wrong H0 adds a phantom radial flow δv ≈ cz δH0/H0 [src: Eq. 17]. The noise enters through G_nm
= ⟨s_n s_m⟩ + δ_nm (σ*² + σ_n²) (Eq. 28), with ⟨s_n s_m⟩ and ⟨S_m U_i⟩ (Eq. 29) computed in linear
theory from a fiducial P(k) — Eisenstein & Hu with Planck 2015 parameters in arXiv:1808.07772 [src:
Sect. 4].

**Kaiser MLE and its correction.** The Kaiser estimate, written in the continuous limit (Nusser
2014 as summarised by Whitford et al.), weights each shell by w(r) n̄(r)/σ²(r) with w = 1 (Eq. 7);
it equals the volume-average bulk flow only for w(r) = σ²(r)/[n(r) r²], which the Nusser MLE
adopts (Eqs. 8–9), at the price of "requiring spherical symmetry in the survey geometry", found
"unsuitable for the CF4 dataset" [src: arXiv:2306.11269, Sects. 3.2.2, 4.4].

**Shell fits.** Nusser & Tully fit, in each radial bin, u = m (monopole), u = V_dip·r̂ (dipole),
or u = m + V_dip·r̂ (Eqs. 8–10), by weighted least squares, β̂ = A u, A = (XᵀWX)⁻¹XᵀW with W =
diag(σ_u⁻²) (Eqs. 11–12). The authors stress this is "a low-order parametrization of the
velocities sampled by a catalog, not a reconstruction of the full velocity field or a
volume-averaged flow in an ideal sphere" [src: arXiv:2608.14265, Sect. III.2]. A bin is kept only
if it has ≥ 10 objects and N_eff = (Σw)²/Σw² ≥ 10 (Eq. 2) [src: Sect. II.2].

**Prior-free forward model, in shells.** Duangchan et al. 2025 fit the four parameters (V_r,
V_X, V_Y, V_Z) to the CF4 distance moduli with a flat prior, P(π) = 1 [src: arXiv:2507.22236,
Sect. 3.1]. A single fit would sit at r_eff ≈ 75 h⁻¹Mpc (Eq. 10) against a median data distance of
155 h⁻¹Mpc, because constraints thin out and errors σ_v ≈ (ln10/5) σ_μ cz grow with distance (Eq.
9); so they fit 20 h⁻¹Mpc shells separately and volume-average them into spheres (Eq. 11). The
result is "only … a pseudo-Monte Carlo chain", and correlations between radii "cannot be
interpreted" [src: Sect. 3.3].

### Step 4. Compute the window function
<!-- key: step-4-compute-the-window-function -->

For an estimator u_i = Σ_n w_{i,n} S_n, the tensor angle-averaged window is

    W²_ij(k) = Σ_{n,m} w_{i,n} w_{j,m} f_nm(k)                                          (Eq. 30)
    f_nm(k)  = ∫ d²k̂/(4π) (r̂_n·k̂)(r̂_m·k̂) exp[i k k̂·(r_n − r_m)]                         (Eq. 31)

[src: arXiv:2302.02028, Sect. 6; same as arXiv:1808.07772, Eq. 33]. Its diagonal shows which
scales contribute; comparing it with the window of the ideal survey shows how far the data can go.
The diagnostic used: CF3 tracks the ideal r⁻² window to R ≈ 150 h⁻¹Mpc, beyond which "the central
peak … has reached a minimum width and has ceased to track the window function of the ideal
survey"; CF4 tracks it to ≈ 200 h⁻¹Mpc [src: arXiv:1808.07772, Sect. 6, Fig. 4;
arXiv:2302.02028, Sect. 7].

For a survey-weighted estimator (MLE family) the window is built from randoms instead. Qin et al.
2018 draw 50 × N_gal random points with the survey's sky and redshift distribution, weight them by
1/(σ²(r) + σ*²), and sum W(k) = Σ_l w_l exp[i (k/√3)(x_l + y_l + z_l)] / Σ_l w_l (Eq. 25), because
a hemispherical, Galactic-plane-masked, error-weighted sample is "more complicated than a sphere or
Gaussian whose outer radius is equal to the bulk flow depth" [src: arXiv:1804.05520, Sect. 6.2].

### Step 5. Expectation, covariance and χ²
<!-- key: step-5-expectation-covariance-and-chi2 -->

In linear theory the expected covariance of the estimate is

    R_ij = ⟨u_i u_j⟩ = (H0² Ω_m^1.1 / 2π²) ∫ dk P(k) W²_ij(k)          (arXiv:2302.02028, Eq. 32)

independent of H0 when distances are in h⁻¹Mpc; then χ² = Σ u_i R⁻¹_ij u_j over three components,
and the probability is the χ²(3 dof) tail [src: arXiv:2302.02028, Sect. 6, Eqs. 32–33;
arXiv:1808.07772, Eq. 35]. The **expectation** quoted beside the amplitude is the rms amplitude
implied by R_ij (139 and 120 km/s at R = 150 and 200 h⁻¹Mpc for CF4) [src:
arXiv:2302.02028, Table 1]. The amplitude errors in the CF4 table "include both the theoretical
difference between the estimate and the bulk flow from an ideal survey and the measurement
noise"; the plotted error bars are measurement noise alone [src: Sect. 7, Table 1, Fig. 7]. The
scalar version used for MLE estimates is σ_B² = (H0² f²/2π²) ∫ W²(k) P(k) dk with f = Ω_m^0.55
(Eq. 24), with Gaussian W = exp(−k²R²/2) or top-hat W = 3(sin kR − kR cos kR)/(kR)³ only as
idealisations [src: arXiv:1804.05520, Sect. 6.2].

The shell fits propagate the linear radial-velocity covariance S_ij = Ψ⊥(s)(r̂_i·r̂_j) + [Ψ∥ −
Ψ⊥](r̂_i·ŝ)(r̂_j·ŝ) (Eq. 16), computed from the z = 0 linear P(k), through the same operator:
C_cv = A S Aᵀ, C_pred = C_meas + C_cv (Eq. 18), with cross-bin blocks A_b S^{bb′} A_b′ᵀ (Eq. 19)
and catalogue-difference covariance C_Δ = C^aa_pred + C^bb_pred − C^ab_cv − C^ba_cv (Eq. 21). The
test statistic is Q = θ̂ᵀC_θ⁻¹θ̂ against χ²_k with k = 1 (monopole), 3 (dipole) or 4 (both) per bin,
times N_bin for the global tests; the marginal tests integrate over the omitted parameters rather
than fixing them, and a small p "is not the probability that ΛCDM is false"; p is converted to
N_σ = Φ⁻¹(1 − p/2) [src: arXiv:2608.14265, Sects. IV.2–IV.3, Eqs. 16–24].

### Step 6. Calibrate errors and biases on mocks
<!-- key: step-6-calibrate-errors-and-biases-on-mocks -->

Whitford et al. 2023 run each estimator on 512 CF4 mocks (L-PICOLA, with the SDSS, 6dFGSv and
CF4 TF selections stacked around one observer) and find the analytic errors too small: the Peery
MVE reduced χ² falls from 6.51 at R = 69 to 3.39 at R ≥ 276 h⁻¹Mpc (Table 2), and 4.48 at 173
h⁻¹Mpc after bias correction; the estimators return an **underestimate** of the expected moment
[src: arXiv:2306.11269, Sects. 2.4.2, 4.3.2]. They then (i) correct the bias from the mock
regression and (ii) rescale the measurement-error covariance C_ij → βC_ij so that the mock reduced
χ² is 1, cosmic variance untouched [src: Sect. 5.1]. Their recommendation: estimators "always need
to be applied to realistic mocks before applying them to estimate the bulk flow of a real dataset
and compare the results to theory" [src: Sect. 4.4]. Duangchan et al. use 64 mocks to derive an
additive (Δ) and a multiplicative (R) correction per shell and component, apply each of the 64
corrections to sample their variance, and find R suited to the bulk flow, Δ to the radial flow
[src: arXiv:2507.22236, Sect. 4.3, Eqs. 12–13].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Gaussian or r⁻² ideal window (MV)
<!-- key: gaussian-or-r-2-ideal-window-mv -->

Gaussian weights w(r) = A exp[−r²/(R/3)²] (Eq. 34, R scaled by 3 to give a central peak of the
same width) were introduced "to smooth the sharp edge" of a top-hat; r⁻² weights do better,
"almost eliminating the side-lobe", so the flow is "only sensitive to velocity modes at or above
the scale of the survey" [src: arXiv:1808.07772, Sect. 6, Fig. 3]. The choice moves the verdict
on the same CF3 data at R = 150 h⁻¹Mpc: Gaussian 252 km/s against an expectation of 166, χ² = 6.92,
p = 7.4 %; r⁻² 282 km/s against 128, χ² = 9.59, p = 2.2 % [src: Table 1]. The authors note it is
"surprising" that the Gaussian amplitudes are smaller although the expectation is larger [src:
Sect. 6].

### MV against Kaiser MLE on the same data
<!-- key: mv-against-kaiser-mle-on-the-same-data -->

On CF4 with mock-calibrated errors (Whitford et al. 2023, arXiv:2306.11269, Table 3, supergalactic components):

| Estimator | |B| raw → bias-corrected (km/s) | Effective depth | P(>χ²) raw → corrected | Mock ΛCDM ⟨|B|⟩ |
|---|---|---|---|---|
| Kaiser MLE | 302 ± 164 → 408 ± 165 | 49 h⁻¹Mpc | 32.7 % → 10.1 % | 130 ± 54 → 196 ± 82 |
| Peery MVE | 357 ± 104 → 428 ± 108 | 173 h⁻¹Mpc | 0.71 % → 0.11 % | 128 ± 59 → 194 ± 86 |

Bracketed values in the paper, without the error rescaling, give 0.06 % (raw) and 0.002 %
(corrected) for the MVE [src: arXiv:2306.11269, Table 3].

Reading [der]: the Kaiser MLE has a
much shallower error-weighted depth than the MVE whatever data it is given, so the two do not test
the same scale; and the MVE probability changes by more than an order of magnitude between unscaled
and mock-scaled errors.

The Kaiser MLE is also exposed to a global zero-point (Whitford et al. 2023, arXiv:2306.11269):
shifting every η by ±0.031 (about 5 km/s/Mpc in H0) moves the Kaiser components by "upward of 100 km s⁻¹", most along the SDSS cone, and
asymmetrically because a constant shift in η is not a constant shift in v; the Peery MVE "remains
unbiased", as its cz constraint predicts [src: Sect. 4.3.3].

### Sphere estimators or radial shells
<!-- key: sphere-estimators-or-radial-shells -->

A sphere estimate at R mixes all shells inside R with correlated errors; "estimates of the bulk
flow components at different R … have highly correlated errors" [src: arXiv:1808.07772, Sect. 6].
Shells isolate where a signal sits and carry an explicit cross-bin covariance, and fitting the
monopole jointly gives the monopole–dipole covariance (L2). They cost the comparability with the
volume-average definition [src: arXiv:2608.14265, Sect. III.2]. On CF4 the two pictures differ: a
"2.29σ" full-range dipole deviation and a localised 3.40σ feature in the shell analysis (L2),
against χ² probabilities of 0.023 % and 0.00021 % for the MV spheres [src: arXiv:2302.02028,
Table 1].

### ΛCDM prior in the weights, or none
<!-- key: lambdacdm-prior-in-the-weights-or-none -->

MV weights and Wiener-filter reconstructions use a fiducial P(k); Whitford et al. note that for
"small or noisy samples" the prior of a Wiener filter "can dominate the underlying signal", making
the comparison with ΛCDM "somewhat circular" [src: arXiv:2306.11269, Sect. 3.1]. Duangchan et al.
remove the prior but need simulation-based corrections: on CF4 the corrected amplitude peaks at
350 km/s at ~140 h⁻¹Mpc, "well within the 3σ scatter of the ΛCDM model", the uncorrected one
exceeds 600 km/s at 240 h⁻¹Mpc, and the V_X component leaves the ΛCDM 3σ range at ~140 h⁻¹Mpc,
reaching more than 4σ (corrected) at 240 h⁻¹Mpc [src: arXiv:2507.22236, Sect. 5.2]. Their Fig. 9
assumes H0 = 75.9 km/s/Mpc [src: Fig. 9 caption].

### Velocity estimator inside the flow
<!-- key: velocity-estimator-inside-the-flow -->

Qin et al. 2018 compare three estimators on the same data — dMLE (velocities from distances),
wMLE (Watkins–Feldman velocities) and ηMLE — and find on 6dFGSv mocks a bias in B_z (the
equatorial pole) that persists with wMLE and with an MV estimator at 70 h⁻¹Mpc (B_z = −421 ± 66
km/s), concluding it is not the estimator but "some aspect of the 6dFGSv survey and selection
function", plausibly "the hemispherical nature of the 6dFGSv data combined with a zero-point
offset"; recomputing the mock f_n removes it [src: arXiv:1804.05520, Sect. 5.3, App. C]. The
paper gives B_z-revised values in App. C (Tables 4–5): 311.9 ± 26.7 km/s at a depth of 38.9
h⁻¹Mpc for the combined sample.

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| σ* in the MV covariance | velocity noise for "small-scale motions not included in the linear model" (value not read) | MV | arXiv:1808.07772 | Eq. 28 |
| σ_v for distance placement | ≈ 300 km/s, insensitive | CF4 MV | arXiv:2302.02028 | Sect. 5 |
| Velocity floor | 100 km/s, independent per object | CF4 shells | arXiv:2608.14265 | Eq. 7 |
| Minimum cz | > 4 000 km/s for every fitted object | CF4 shells | arXiv:2608.14265 | Sect. III.1 |
| Bin acceptance | ≥ 10 objects and N_eff ≥ 10 | CF4 shells | arXiv:2608.14265 | Eq. 2 |
| Maximum reliable R (window test) | ≈ 150 (CF3), ≈ 200 h⁻¹Mpc (CF4) | MV | arXiv:1808.07772; arXiv:2302.02028 | Sect. 6; Sect. 7 |
| Theory P(k) | Eisenstein & Hu, Planck 2015 (σ8 = 0.8159, Ω_m = 0.3089) | MV on CF3 | arXiv:1808.07772 | Sect. 4 |
| Theory P(k) | z = 0 linear, Planck 2018 (Ω_m = 0.3111, σ8 = 0.8102) | CF4 shells | arXiv:2608.14265 | Sect. II.2 |
| Mock count | 512 (CF4); 64 (prior-free); 2 × 8 (2MTF + 6dFGSv) | — | arXiv:2306.11269; arXiv:2507.22236; arXiv:1804.05520 | Sects. 4.3, 4.3, 5.3 |
| Peery MVE reduced χ² on mocks | 6.51 (R = 69) → 3.39 (R ≥ 276 h⁻¹Mpc) | CF4 | arXiv:2306.11269 | Table 2 |
| Window randoms | 50 × the galaxy count | 2MTF + 6dFGSv | arXiv:1804.05520 | Sect. 6.2 |
| Effective depth of a single forward fit | ≈ 75 h⁻¹Mpc vs median distance 155 h⁻¹Mpc | CF4 | arXiv:2507.22236 | Eq. 10 |
| Shell width | 20 h⁻¹Mpc | CF4 prior-free | arXiv:2507.22236 | Sect. 3.3 |
| Zero-point test | ±0.031 in η ≈ 5 km/s/Mpc in H0; Kaiser shifts > 100 km/s, MVE unbiased | CF4 mocks | arXiv:2306.11269 | Sect. 4.3.3 |
| 2MTF + 6dFGSv sky imbalance | ~5:1 south to north | combined sample | arXiv:1804.05520 | Sect. 5.3 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **The data window stops tracking the ideal one.** Beyond that R, "bulk flow estimates on these
  scales will seem to change more slowly with radius than the actual bulk flow"; test by
  overplotting W²_ii of data and ideal survey [src: arXiv:2302.02028, Sect. 7].
- **Analytic errors too small.** Mock reduced χ² of 3–6 for the MVE on CF4 [src:
  arXiv:2306.11269, Table 2]. Test: run the estimator on selection-matched mocks and quote both
  scaled and unscaled probabilities.
- **Estimator bias on realistic fields.** Kaiser and Watkins estimators recover a constant flow
  but "may not measure the bulk flow moment with the same accuracy and precision for realistic
  mocks"; with highly non-linear velocities every estimator tested is biased [src:
  arXiv:2306.11269, Sect. 4.4].
- **Survey geometry in the ΛCDM prediction.** Under-sampling (fewer than ~500 velocities)
  increases the variance so that a measured flow must be compared with mocks, not with the
  analytic expectation (Andersen et al. 2016, as reported) [src: arXiv:2306.11269, Sect. 3.1].
- **Correlations left out of the covariance.** The shell analysis neglects shared calibration
  errors, repeated distances and overlap between catalogues; its catalogue rows "must therefore
  not be combined as independent measurements", and its p-values are not corrected for the number
  of bins and catalogues inspected [src: arXiv:2608.14265, Sect. VIII.1].
- **The covariance is unconditioned.** It represents random ΛCDM realisations, "not conditioned
  on the known density distribution in our local Universe", evaluated at z = 0 [src: same].
- **Hemispheric samples.** A zero-point fitted to a one-hemisphere sample leaks into the polar
  dipole (`deep/distance-indicators.md`, Step 6), seen as the 6dFGSv B_z bias [src:
  arXiv:1804.05520, App. C].

## Reading list
<!-- key: reading-list -->

- Turner 2024, arXiv:2411.19484, Sect. 5.1 — review: definitions and the history of the record.
- Peery, Watkins & Feldman 2018, arXiv:1808.07772, Sects. 3–6 — method: r⁻² MV estimator,
  H0-independence constraint, window functions, Gaussian vs r⁻² comparison.
- Watkins et al. 2023, arXiv:2302.02028, Sects. 2, 5–7 — application: debiased velocities, object
  placement, the CF4 χ² and its error budget.
- Whitford, Howlett & Davis 2023, arXiv:2306.11269, Sects. 3–5 — critique: four estimators on
  selection-matched mocks, error rescaling, zero-point sensitivity.
- Qin et al. 2018, arXiv:1804.05520, Sects. 4–6 and App. C — method: ηMLE, survey window from
  randoms, hemispheric bias.
- Nusser & Tully 2026, arXiv:2608.14265, Sects. II–IV and VIII — method: monopole + dipole shells
  with propagated ΛCDM covariance and catalogue differences.
- Duangchan et al. 2025, arXiv:2507.22236, Sects. 3–5 — alternative: prior-free shell forward
  model with simulation-based corrections.

## Not verified
<!-- key: not-verified -->

- Watkins, Feldman & Hudson 2009 (arXiv:0809.4041) and Feldman et al. 2010 (arXiv:0911.5516)
  bodies: the radius of the original Gaussian ideal window and the shear and octupole
  terms were not read here.
- Nusser 2014 (arXiv:1405.6271) and Nusser 2016 (arXiv:1508.03860) bodies: the Nusser MLE is
  described through arXiv:2306.11269 only. Andersen et al. 2016, Agarwal et al. 2012, Macaulay et
  al. 2011–2012: seen as citations only.
- The numerical value of σ* adopted by Peery et al. 2018 and Watkins et al. 2023.
- The form of K_i in Nusser & Tully 2026 (their App. A) and of Ψ∥, Ψ⊥ (their App. B).
- The Tsagas et al. 2025 review sections named in `subtopics.tsv`.
