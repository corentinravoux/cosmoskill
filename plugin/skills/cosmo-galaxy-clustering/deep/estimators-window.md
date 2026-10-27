# Estimators, window functions, wide-angle terms and integral constraints — cosmo-galaxy-clustering dossier

Scope: how a measured two-point function is related to the model through
the survey window, wide-angle terms and integral constraints, how DESI and
its predecessors compute each piece, and which variant to choose for BAO,
full shape or f_NL.
Snapshot: 2026-10-16.
From: DESI 2024 II (arXiv:2411.12020), Sect. 10.1; Huterer 2023
(arXiv:2212.05003), Sect. 3.1.

Already in L2, not repeated here: the estimator definitions and their
foundation papers (`physics-and-methods.md#configuration-space`,
`physics-and-methods.md#fourier-space`), the one-paragraph window and
integral-constraint summary (`physics-and-methods.md#window-function-and-integral-constraints`),
the θ-cut as a fibre-assignment mitigation
(`systematics.md#fibre-assignment-and-fibre-collisions`), and the
relevance ranking by analysis (`systematics.md#window-integral-constraints-and-wide-angle-terms`).

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Measure, with a stated line of sight and normalisation
<!-- key: step-1-measure-with-a-stated-line-of-sight-and -->

**Configuration space (DESI DR1).** Landy–Szalay with the mid-point line of
sight, η̂ = (x_1 + x_2)/2; after reconstruction the numerator uses DD, DS,
SD, SS and the denominator the unshifted RR (arXiv:2411.12020, Eqs. 10–11)
[src: Sect. 10.1.1]. 200 s-bins to 200 h⁻¹ Mpc (regrouped to
4 h⁻¹ Mpc), 200 μ-bins; multipoles by a μ-sum weighted by the bin integral
of L_ℓ, so that ℓ > 0 multipoles of an isotropic signal vanish [src: same].
Random catalogues are split into data-sized chunks whose pair counts are
summed; at least 50 times the data are used (1, 8, 10, 4 random files for
BGS, LRG, ELG, QSO) [src: same].

**Fourier space (DESI DR1, arXiv:2411.12020).** FKP field F = n_D − α_R n_R (Eq. 13),
multipoles P̂_ℓ = (2ℓ+1)/(A N_k) Σ_k F_0(k) F_ℓ(−k) − N_ℓ with the
first-point line of sight (Eqs. 14, 16–17), shot noise in the monopole only
(Eq. 15) [src: Sect. 10.1.2].
Implementation details, from arXiv:2411.12020 [src: Sect. 10.1.2]:

| Setting | DESI DR1 value |
|---|---|
| Normalisation | A = (α_R/dV) Σ_i n_D,i n_R,i on cells of fixed dV^{1/3} = 10 h⁻¹ Mpc, chosen to approximate the window norm at mid-range k |
| Mass assignment | TSC, compensated by sinc(2πk_i/k_N)^p, p = 3; interlacing of order 3 |
| Boxes | 4000, 7000, 9000, 10000 h⁻¹ Mpc (BGS, LRG, ELG, QSO), 6 h⁻¹ Mpc cells, k_N ≈ 0.5 h Mpc⁻¹ |
| Randoms | all 18 files, over 100 times the data |
| Caps | NGC and SGC spectra averaged with weights A |
| Code | `pypower` (modified `nbodykit`), `pycorr` (modified Corrfunc) |

After reconstruction both A and the window are computed with the unshifted
randoms [src: same].

### Step 2. Compute the window
<!-- key: step-2-compute-the-window -->

The convolved multipoles are
P^conv_ℓ(k) = ∫ dk′ k′² Σ_ℓ′ W_ℓℓ′(k, k′) P_ℓ′(k′) − [Q_ℓ(k)/Q_0(0)] ∫ dk′ k′²
Σ_ℓ′ W_0ℓ′(0, k′) P_ℓ′(k′), the second term being the global integral
constraint (Beutler & McDonald 2021, arXiv:2106.06324, Eq. 1). The kernel
is a double Bessel integral over the configuration-space window multipoles
Q_L(s), which are pair counts of the weighted randoms projected on L_L(ŝ·d̂)
(Eqs. 2–3) [src: Sect. 2]. Equivalent forms: Wilson et al. 2015
(arXiv:1511.07799) derived the masked-field Hankel-transform relation in the
distant-observer limit, 10³–10⁴ times faster than earlier approaches,
with Q_q obtained by pair counting randoms [src: Sect. 7]; the DESI f_NL
paper writes the same with Wigner 3j symbols (arXiv:2411.17623, Eqs. 31–32)
[src: Sect. 4.1].

In DESI DR1 the window matrix is computed from the power spectra of the
randoms in boxes 20, 5 and 1 times the data box, concatenated, with
first-order wide-angle terms [src: arXiv:2411.12020, Sect. 10.1.2]; the
θ-cut variant uses meshes of 9, 45 and 180 h⁻¹ Gpc at 1500³, with
Δk = 3.5 × 10⁻⁵ h Mpc⁻¹, keeping in each k-bin the box with most modes, and
then Hankel-transforms to Q^(n)_p(s) [src: Pinon et al. 2024,
arXiv:2406.04804, Sect. 3.3].

### Step 3. Add wide-angle terms
<!-- key: step-3-add-wide-angle-terms -->

The single-galaxy line of sight breaks pair symmetry. Expanding
ξ(x_1, x_2) = Σ_p,n (s/d)^n ξ_p^(n)(s) L_p(d̂·ŝ) (arXiv:2411.17623, Eq. 33)
gives at n = 1 the odd terms ξ_1^(1) = −(3/5) ξ_2^(0) and
ξ_3^(1) = (3/5) ξ_2^(0) − (10/9) ξ_4^(0) (Eq. 35), each with its own window
W_ℓ^(n), which carries an extra x⁻ⁿ (Eq. 34) [src: Sect. 4.1]. Beutler &
McDonald write the n = 1 step as a matrix M (5N × 3N) that maps
(P_0, P_2, P_4) to five multipoles including P_1 and P_3, with finite-
difference derivative blocks K^{2→1}, K^{2→3}, K^{4→3}; its only
survey-specific parameter is the line-of-sight amplitude d
(arXiv:2106.06324, Eqs. 26–30) [src: Sect. 3].

### Step 4. Assemble one matrix and bin it
<!-- key: step-4-assemble-one-matrix-and-bin-it -->

P^conv = W P^true with the integral constraint absorbed:
W ≡ W − (Q/Q_0(0)) W_0ℓ′(0, k′), which is exact because the constraint is
linear in P (arXiv:2106.06324, Eqs. 20–21) [src: Sect. 2.2]. Bin-average in
both observed and theory k (Eq. 16); the BOSS/eBOSS products use
Δk_o = 0.01 and Δk_th = 0.001 h Mpc⁻¹, define W over 0 < k < 0.4 and
recommend fits over 0.01 < k < 0.3 h Mpc⁻¹, because the window couples modes
inside the fit range to modes beyond it [src: Sects. 2.1–2.2].

### Step 5. Model the integral constraints the data actually impose
<!-- key: step-5-model-the-integral-constraints-the-data -->

The FKP field integrates to zero over the survey (global IC,
arXiv:1904.08851, Eq. 3). If the radial selection is taken from the data,
by shuffled redshifts, a spline, or a binned α(r) (Eq. 4), the constraint
holds in every radial shell (Eq. 6); both are cases of one form with a
generic ε_ic(r, x) (Eqs. 7–8) [src: de Mattia & Ruhlmann-Kleider 2019,
Sects. 2.1–2.2]. Weighting randoms pixel by pixel to the data imposes an
angular IC of the same form [src: Sect. 5.2].

DESI DR1 f_NL implements them as window corrections
W → W − W^RIC − W^AIC (arXiv:2411.17623, Eq. 46) [src: Sect. 5.2.3]:

- W^RIC_ℓℓ′ = (W_ℓp / (W_00)_00) f_pq W_qℓ′ with
  f_pq = A_pq exp[−(k_n² + k_m²)/σ²_pq] (Eqs. 39–40), A and σ fitted on
  EZmocks with and without shuffling. This is multiplicative, unlike the
  additive mock-difference corrections of earlier work, and so does not
  depend on the spectrum it was estimated on [src: Sect. 4.4].
- W^AIC: same form, fitted on 30 uncontaminated EZmocks to which the
  imaging-weight scheme is applied; it is purely geometric, so it does not
  measure the efficiency of the weights (arXiv:2411.17623) [src: Sect. 5.2.2].
- The global IC is negligible there [src: Sect. 4.4].

### Step 6. If the window is non-compact, rotate it
<!-- key: step-6-if-the-window-is-non-compact-rotate-it -->

The θ-cut and veto masks make W strongly non-diagonal, so a naive
convolution would need theory at k′ > 0.5 h Mpc⁻¹ [src:
arXiv:2411.12020, Sect. 10.1.2]. Pinon et al. transform
d′ = M d − s m_o, W′ = M W − m_o m_tᵀ, C′ = M C Mᵀ (arXiv:2406.04804,
Eqs. 43–45), which leaves χ² unchanged for invertible M once s is
marginalised (Eqs. 40–42) [src: Sect. 5.1]. M, m_o, m_t minimise a loss
that rewards a compact W′, a near-diagonal C′ and an unchanged
normalisation (Eqs. 46–52, with α = 5, β = 10); m_t is initialised to zero
below k_t = 0.2 h Mpc⁻¹ [src: same]. DESI fits s on complete Abacus
cut-sky mocks, takes a Gaussian prior with mean and width equal to that
best fit, and marginalises it analytically by adding m_o s² m_oᵀ to C′; the
residual is below one fifth of the DR1 errors [src: arXiv:2411.12020,
Sect. 10.1.2, Fig. 12].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Line of sight
<!-- key: line-of-sight -->

| Choice | Where used | Cost |
|---|---|---|
| Mid-point | DESI ξ [src: arXiv:2411.12020, Sect. 10.1.1] | pair counts, no FFT speed |
| First/end point | DESI P(k) and FFT estimators [src: Sect. 10.1.2] | wide-angle terms and odd multipoles must be modelled |
| Two-ℓ (bipolar) generalisation of Yamamoto | proposed; optimal on ultra-large scales | FFT-evaluable exact window with a finite number of terms (Sailer et al. 2026, arXiv:2607.05513, abstract) |

In Gaussian simulations of a 19.7 h⁻¹ Gpc box the (2,2) estimator doubles
the signal-to-noise of the first two bandpowers relative to the Yamamoto
hexadecapole; mean bias of the finite window at most 2.8σ over 256
realisations (≈ 0.2σ for one) [src: arXiv:2607.05513, Sect. 5.3].

### Convolve the model, deconvolve the data, or estimate without a window
<!-- key: convolve-the-model-deconvolve-the-data-or -->

- **Convolve the model** (DESI, BOSS, eBOSS): no constraint on binning.
- **Deconvolve the data** by inverting W: same BAO likelihood as the
  standard analysis on 6dFGS, BOSS and eBOSS, but needs a square window
  matrix and hence coarse theory bins [src: arXiv:2106.06324, Sect. 7].
- **Window-free quadratic estimators** (ML or FKP-weighted): unwindowed
  bandpowers with a near-diagonal covariance, free of leading gridding,
  binning and non-Poisson shot-noise effects, and of integral constraints
  unless the first k-bin is used; on a BOSS chunk, parameters compatible
  with the standard route and no gain in constraining power [src: Philcox
  2021, arXiv:2012.09389, Sect. VI]. Critique: super-survey modes are
  expected to affect it, and the IC impact on it should be checked [src:
  Nakano et al. 2026, arXiv:2606.29735, Sect. 6].

### Normalisation A
<!-- key: normalisation-a -->

Beutler & McDonald fix A so that Q_0(s → 0) = 1, A = ∫ n̄_w² dx (Eq. 4); the
traditional random-sum with n̄(z) meets this only to about 10%. If data and
window share the same A the likelihood is unaffected ("essentially
cosmetic"); if they do not, P is biased in amplitude [src: arXiv:2106.06324,
Sect. 2]. DESI uses a fixed-cell A chosen to approximate the window norm at
mid-range k, with `pypower` modified for this definition [src:
arXiv:2411.12020, Sect. 10.1.2]. A BOSS "window function
normalization issue" is named as excluding one public measurement set from
comparisons [src: Simon et al. 2023, arXiv:2208.05929, Sect. IV.3].

### How many wide-angle orders
<!-- key: how-many-wide-angle-orders -->

On BOSS DR12 low-z NGC, in linear Kaiser theory [src: Beutler, Castorina &
Zhang 2019, arXiv:1810.05051, Sects. 3.4.1, 4]:

- The quadrupole leaks about 10% into the monopole at large scales; n = 1
  dipole and octopole terms add about 2% (arXiv:1810.05051) [src: Sect. 3.4.1].
- Ignoring n = 1, 2 biases the FFT quadrupole by 20% at large scales and the
  hexadecapole by more than 100% at k = 0.003 h Mpc⁻¹ (arXiv:1810.05051)
  [src: Sect. 3.4.1].
- Including n = 2 lowers the large-scale monopole by 3%.
- Window plus wide-angle terms reach up to 5% of the even-multipole errors;
  no significant effect on BAO or RSD for BOSS.

DESI DR1 keeps n ≤ 1 [src: arXiv:2411.12020, Sect. 10.1.2;
arXiv:2411.17623, Sect. 4.1].

### Random redshifts and the radial IC
<!-- key: random-redshifts-and-the-radial-ic -->

- Binned (δr = 2 h⁻¹ Mpc) and shuffled schemes give nearly the same spectra,
  so the binned-scheme model can stand for shuffling; both remove power
  along the line of sight, mostly in P_2 and P_4, and the effect grows when
  imposed on separate chunks (6 chunks of CMASS) [src: arXiv:1904.08851,
  Sect. 4.3].
- For DESI DR1 f_NL, uncorrected shuffling biases f_NL by 1σ [src:
  arXiv:2411.17623, Sect. 4.4].
- Alternative: predict the radial selection from first principles and
  marginalise over unknowns [src: arXiv:1904.08851, Sect. 6].

### Imaging weights and the angular IC
<!-- key: imaging-weights-and-the-angular-ic -->

On CMASS-like mocks with a pixelated scheme at nside = 64 (≈ 0.84 deg²),
modelling the angular IC recovers α_∥, α_⊥, fσ8 on uncontaminated mocks at
the cost of 22% larger fσ8 errors; on contaminated mocks, ignoring the
systematics gives Δα_∥ = 0.043, Δα_⊥ = −0.037, Δfσ8 = −0.17, while the
angular IC brings fσ8 within about 20% of the single-mock error [src:
arXiv:1904.08851, Sect. 5.2, Table 2]. In DESI DR1 the AIC from linear
weights is about 0.4σ on f_NL and is corrected; for random-forest weights
the correction is slightly worse [src: arXiv:2411.17623, Sect. 5.2.2].

### Weights: FKP or optimal (OQE)
<!-- key: weights-fkp-or-optimal-oqe -->

For DESI QSO mocks, f_NL differs by about −6 (mean −5.8) between FKP and
OQE weights, a real bias between schemes that vanishes when b_1 is fixed;
about 0.5σ for DR1, larger than the error for the full survey; on data a
low-redshift QSO residual makes OQE weights necessary (Δf_NL ≈ 20) [src:
arXiv:2411.17623, Sect. 4.3].

### Hard θ-cut or apodised cut
<!-- key: hard-theta-cut-or-apodised-cut -->

A Tukey-apodised transverse cut (Λ = 2.1 h⁻¹ Mpc) must extend to about
30 h⁻¹ Mpc before the Fourier window vanishes above k_t ≈ 0.3–0.4 h Mpc⁻¹,
discarding scales far larger than the cut; this is why DESI rotates the
window instead [src: arXiv:2406.04804, App. C].

### Analytic window and IC or light-cone mocks
<!-- key: analytic-window-and-ic-or-light-cone-mocks -->

On BOSS-like linear light-cone mocks the analytic window-plus-IC treatment
loses accuracy at k ≲ k_eq and becomes invalid with PNG, because
super-survey modes enter the IC through the data-derived selection; the
proposed alternative is to forward-model the measured spectrum with
light-cone mocks [src: arXiv:2606.29735, abstract, Sect. 6]. The size of
the resulting bias on f_NL is left for later work [src].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| P(k) cell / k_N | 6 h⁻¹ Mpc / ≈ 0.5 h Mpc⁻¹ | DESI DR1 | arXiv:2411.12020 | Sect. 10.1.2 |
| Normalisation cell | dV^{1/3} = 10 h⁻¹ Mpc | DESI DR1 | arXiv:2411.12020 | Sect. 10.1.2 |
| Window boxes | 20×, 5×, 1× data box | DESI DR1 | arXiv:2411.12020 | Sect. 10.1.2 |
| θ-cut window meshes | 9, 45, 180 h⁻¹ Gpc; 1500³; Δk = 3.5 × 10⁻⁵ | DESI DR1 ELG | arXiv:2406.04804 | Sect. 3.3 |
| θ-cut | θ < 0.05° removed from all pair terms | DESI DR1 | arXiv:2411.12020 | Sect. 10.1.1 |
| Rotation residual | < 1/5 of DR1 errors | DESI DR1 LRG3 | arXiv:2411.12020 | Sect. 10.1.2 |
| Window k-range / fit range | 0–0.4 / 0.01–0.3 h Mpc⁻¹ | BOSS, eBOSS, 6dFGS products | arXiv:2106.06324 | Sect. 2.2 |
| Δk_o / Δk_th | 0.01 / 0.001 h Mpc⁻¹ | same | arXiv:2106.06324 | Sect. 2.2 |
| Traditional A error | ≈ 10% on Q_0(0) = 1 | SDSS-era | arXiv:2106.06324 | Sect. 2 |
| Odd-multipole detection | 9.0σ (low z), 8.7σ (high z) | BOSS DR12 | arXiv:1810.05051 | Sect. 3.6.3 |
| Wide-angle (n > 0) detection | 6.0σ, 6.4σ | BOSS DR12 | arXiv:1810.05051 | Sect. 3.6.3 |
| Fit range of that test | 0.008 < k < 0.096 h Mpc⁻¹, 5 multipoles | BOSS DR12 | arXiv:1810.05051 | Sect. 4 |
| Angular-IC error cost | +22% on fσ8 | CMASS mocks | arXiv:1904.08851 | Sect. 5.2 |
| RIC bias if ignored | 1σ on f_NL | DESI DR1 mocks | arXiv:2411.17623 | Sect. 4.4 |
| AIC bias (linear weights) | ≈ 0.4σ on f_NL | DESI DR1 mocks | arXiv:2411.17623 | Sect. 5.2.2 |
| FKP − OQE f_NL (QSO) | ≈ −6 on mocks; ≈ 20 on data | DESI DR1 | arXiv:2411.17623 | Sect. 4.3 |
| Two-ℓ estimator gain | ×2 S/N, first two bandpowers | Gaussian sims | arXiv:2607.05513 | Sect. 5.3 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Window and data normalised differently.** Amplitude offset that mimics
  bias or σ8. Test: compute A once from Q_0(s → 0) and use it for both
  [src: arXiv:2106.06324, Sect. 2].
- **Randoms' redshifts from the data, no RIC in the model.** Lost
  line-of-sight power in P_2, P_4; for f_NL a 1σ bias [src:
  arXiv:1904.08851, Sect. 4.3; arXiv:2411.17623, Sect. 4.4]. Test: mocks
  with true and shuffled randoms through the same pipeline.
- **Imaging weights without an AIC.** Large-scale power suppressed; the
  weights look more efficient than they are [src: arXiv:2411.17623,
  Sect. 5.2.2]. Test: apply the weighting to uncontaminated mocks.
- **Wide-angle terms omitted with an end-point line of sight.** Quadrupole
  and hexadecapole biased at large scales [src: arXiv:1810.05051,
  Sect. 3.4.1]. Null test: fit the measured dipole and octopole; they
  should be explained by window plus wide-angle terms alone, as on BOSS
  [src: Sect. 4].
- **Window truncated in k′.** Theory needed beyond its validity; caught by
  inspecting W columns at high k_t or by rotating as DESI does [src:
  arXiv:2411.12020, Sect. 10.1.2].
- **Window from too few randoms or one box.** Loss of resolution at low k or
  aliasing at high k; DESI concatenates several boxes [src:
  arXiv:2406.04804, Sect. 3.3].
- **Analytic IC on ultra-large scales.** Inaccurate at k ≲ k_eq, invalid
  with PNG [src: arXiv:2606.29735, abstract]. Test: light-cone mocks with
  the data's selection-estimation step.
- **Weighting-scheme bias in f_NL.** FKP against OQE differences that grow
  with volume [src: arXiv:2411.17623, Sect. 4.3]. Test: fit individual
  mocks with both and look at the mean of the difference.

## Reading list
<!-- key: reading-list -->

- Foundation: Wilson et al. 2015, arXiv:1511.07799 — masked multipoles by
  Hankel transforms; Q_q from pair counts.
- Foundation: de Mattia & Ruhlmann-Kleider 2019, arXiv:1904.08851 — global,
  radial and angular integral constraints in one formalism.
- Method: Beutler, Castorina & Zhang 2019, arXiv:1810.05051 — wide-angle
  terms with the window; size per multipole; odd-multipole null test.
- Method: Beutler & McDonald 2021, arXiv:2106.06324 — window and wide-angle
  matrices, normalisation, deconvolution; public BOSS/eBOSS/6dFGS products.
- Application: DESI 2024 II, arXiv:2411.12020 — DESI estimator settings,
  window computation and rotation.
- Method: Pinon et al. 2024, arXiv:2406.04804 — θ-cut windows and the
  rotation that makes them compact.
- Application: Chaussidon et al. 2024, arXiv:2411.17623 — RIC and AIC as
  window corrections for f_NL.
- Alternative: Philcox 2021, arXiv:2012.09389 — window-free quadratic
  estimators.
- Alternative: Sailer et al. 2026, arXiv:2607.05513 — optimal wide-angle
  estimator with an exact finite window.
- Critique: Nakano et al. 2026, arXiv:2606.29735 — analytic window and IC
  fail at k ≲ k_eq with PNG.

## Not verified
<!-- key: not-verified -->

- The C^(n)_ℓℓ′L coefficients (App. B of arXiv:2106.06324) and the
  normalisation ratios of its Table 7.
- Window treatment in Euclid preparation papers (not read).
- Whether DESI DR2 analyses change the window or IC treatment (no DR2
  full-shape or f_NL method paper read).
- The quantitative f_NL bias promised by arXiv:2606.29735 (left to future
  work by the authors).
