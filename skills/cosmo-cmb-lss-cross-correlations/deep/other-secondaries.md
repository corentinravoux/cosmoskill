# Other secondaries — cosmo-cmb-lss-cross-correlations dossier

Scope: how the first measurements and limits on the moving-lens effect,
anisotropic (patchy) screening, the polarised SZ remote quadrupole and
rotational kSZ are built — the estimator, filters and symmetries that
remove CMB lensing, kSZ and foregrounds, the covariance, how the amplitude
and its significance are defined, and the null tests each analysis passed —
and how to choose between stacked, quadratic and power-spectrum forms.
Snapshot: 2026-10-18.
From: Baxter 2022 Snowmass review (arXiv:2203.06795), Sect. II.2
("Polarized SZ"); SO science goals 2025 (arXiv:2503.00636), Sect. 3.4
(patchy kSZ and reionisation paragraph).

Already in L2, not repeated here: the physical origin of each effect and
the founding estimators (`physics-and-methods.md#other-secondaries`); the
measured amplitudes and limits (`results.md#other-secondaries-status`);
lensing contamination of screening as a systematic
(`systematics.md#patchy-screening-contamination-by-lensing`). The kSZ
velocity quadratic estimator, whose machinery the moving-lens and pSZ
estimators reuse, is in `deep/ksz-velocity-reconstruction.md`; the
reionisation reading of screening and patchy kSZ is in
`cosmo-reionization-21cm`.

Symbols: T_CMB mean CMB temperature; Ψ Weyl potential; v_⊥, v_r transverse
and radial velocities; v̂ reconstructed velocity; η_r, η_⊥ correlation of
true and reconstructed radial and transverse velocities; n_g^3d comoving
galaxy density; χ_* comoving distance of a snapshot; L box side (moving
lens) or multipole of a reconstructed field (screening); G, C gradient and
curl modes of a spin-1 field; b_ML, A_τ, b_q amplitudes relative to a
fiducial model; δτ optical-depth fluctuation; τ̄ mean optical depth;
f_sky sky fraction; p_0 probability of the data under the null.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. What each estimator correlates
<!-- key: step-1-what-each-estimator-correlates -->

| Effect | Estimator | Analysis read |
|---|---|---|
| Moving lens | CMB T × gradient mode of a transverse-velocity-weighted galaxy field, C_ℓ^TG | Hotinli 2026 (arXiv:2605.18938), ACT DR6 × DESI Legacy LRGs |
| Screening, stacked | sign of the large-scale CMB × small-scale map, stacked on galaxies | Coulton 2024 (arXiv:2401.13033), ACT × unWISE; Hadzhiyska 2025 (arXiv:2506.17379), ACT DR5 × DESI LRGs |
| Screening, power spectrum | TT quadratic estimator of τ(n̂), its auto-spectrum, no tracer | Kramer 2026 (arXiv:2608.27458), ACT DR6 |
| Polarised SZ | ⟨Z g V⟩ bispectrum: low-ℓ T, E (Z) × tracer g × high-ℓ E, B (V); quadratic remote-quadrupole estimator | Krywonos 2026 (arXiv:2607.16071), Planck + ACT × unWISE and CIB |
| Rotational kSZ | oriented stack along a rotation axis from satellite redshifts | Yang 2026 (arXiv:2603.14494), Planck × SDSS DR7 groups |

### Step 2. Moving lens
<!-- key: step-2-moving-lens -->

Hotinli 2026 [src: arXiv:2605.18938, Sects. II, III.1, III.3]:
1. Signal Θ_ML(θ) = −2 T_CMB ∫ dχ ∇_⊥Ψ · v_⊥ (Eq. 4).
2. Linear velocity reconstruction v̂_j(k) = i k_j U(k) δ_g(k) with
   U(k) = (faH/k² b_g) P_gg/P_gg^tot for k < k_max and zero above (Eq. 5);
   the fidelity is set by η_r and η_⊥ (Eq. 6).
3. Weight galaxies by v̂_⊥ to form the spin-1 field
   X_a(θ) = Σ_i v̂_a(x_i) δ²(θ − θ_i) (Eq. 9), split into gradient G and curl
   C modes (Eq. 10). In the squeezed limit
   ⟨T_ML X_a⟩ ∝ 𝒩 (i ℓ_a) P_gΨ(ℓ/χ_*), 𝒩 = η_⊥ n_g^3d T_CMB L/χ_* (Eq. 13):
   the moving lens appears only in C_ℓ^TG; C_ℓ^TC vanishes by parity and is a
   null test. The authors call it "the kSZ estimator with more indices".
4. Bin D_ℓ = ℓ² C_ℓ^TG with (2ℓ + 1) weights into 6 logarithmic bins over
   2500 ≤ ℓ ≤ 6000 (Eq. 22).
5. Covariance from the scatter of D_ℓ within ℓ, keeping pairs with
   |ℓ − ℓ′| ≤ Δℓ ~ 1/f_sky to absorb mask coupling (Eq. 23): f_sky ≈ 0.09
   (NGC) and 0.19 (SGC) give Δℓ = 11 and 5. A simulation-based covariance
   agrees "excellent[ly]".
6. Fit one amplitude b_ML to the binned template:
   b̂_ML = tᵀC⁻¹d / tᵀC⁻¹t, σ² = 1/tᵀC⁻¹t (Eq. 25), SNR = b̂_ML/σ (Eq. 26).
   NGC and SGC log-likelihoods are added.

**Why lensing and kSZ do not bias it** [src: Sect. III.4]. Lensing is odd
under T_pri → −T_pri with the late-time structure fixed, so its mean
contribution vanishes; the estimator is linear in T, so its covariance needs
only C_ℓ^TT. kSZ is odd under v_r → −v_r, exactly in the snapshot geometry
and approximately on the light cone. Foregrounds (tSZ, CIB, radio) have no
such symmetry. In a Quijote toy pipeline, foreground bias is "dramatically
suppressed" for ℓ ≳ k_max χ_* when the reconstruction has a hard cutoff
(k_max = 0.05 Mpc⁻¹, so ℓ_* ≈ 129 at z = 0.7), and the cross-correlation is
taken in Fourier space at ℓ ≫ ℓ_* or low-pass filtered; with true halo
velocities the contamination extends to high ℓ, which the authors give as
the reason earlier simulation studies found foregrounds an order of
magnitude above the signal [src: Sect. VI.2].

### Step 3. Screening by stacking
<!-- key: step-3-screening-by-stacking -->

**Sign estimator** (Coulton 2024) [src: arXiv:2401.13033, Sects. II.1–II.5,
III, V, VI.1]:
1. Screening replaces a fraction of line-of-sight photons by the sky mean,
   so it multiplies the primary anisotropy by (1 − δτ); δτ is 10⁻⁵–10⁻³ for
   galaxy and cluster haloes, against τ̄ ~ 5–6% (Sect. II.1).
2. On small scales the quadratic estimator reduces to a large-scale map
   times a small-scale map. Replacing the large-scale map by its **sign**
   costs a variance factor ⟨T²⟩/⟨|T|⟩² = π/2 and suppresses any foreground
   whose sign does not follow the large-scale primary CMB (tSZ, CIB, kSZ);
   the residual ISW correlation is removed by cutting ℓ ≲ 20 or subtracting
   an ISW map (Sect. II.3).
3. Filters: the low-pass map must keep the large-scale sign (transition
   above ℓ ~ 500), the high-pass map is separated from it to avoid
   correlation, both tapered; the beam and pixel window are deconvolved
   first; the output τ map loses all modes ℓ < 1600 and is re-beamed.
   Lensing bias: the first-order term vanishes if the small-scale filter is
   constant wherever the large-scale filter is non-zero (example: |L| > 1600
   with f_s constant for ℓ ≥ 950); the residual is suppressed by the ratio
   of C_ℓ^TT in the two legs (Sects. II.4, II.5).
4. 20′ × 20′ CEA cutouts with bilinear interpolation, stacked with the sign
   weight on 34 and 19 million unWISE blue and green galaxies, after removing
   objects within 6′ of SZ clusters and of SNR > 5 point sources, 10′ of map
   edges and 12′ of inpainted sources. Equal numbers of positive and
   negative weights are enforced: with O(10⁴) independent sign regions, an
   unbalanced stack would leave ~1% of the mean foreground (Sect. II.5).
5. Covariance from 150 Gaussian simulations of the NILC map with a tiled
   noise model; strong radial correlations from the high-pass filter. Check:
   the per-galaxy scatter gives diagonal elements within ~35% (Sect. V).
6. Validation: Websky and Agora maps with all foregrounds and no screening
   give zero; with injected screening they return the filtered input; 40
   lensed "backlight" simulations at halo positions give zero, which also
   bounds the mean field (Sects. III.2, III.3).
7. Significance: χ² against the null; a projected beta profile with β = 0.86
   fixed because of the θ_0–β degeneracy, beam-convolved and filtered like
   the data; Δχ² = 5 against null; AIC −0.93 (blue) and 4.0 (green); F-test
   p = 0.25 and 1.0. The best fit (τ_0 = 1.9 × 10⁻⁴, θ_0 = 1.2′) differs from
   the 1D posterior means (Sect. VI.1).

**Variant on DESI LRGs** (Hadzhiyska 2025) [src: arXiv:2506.17379,
Sects. III.1, III.3, IV.1, IV.2, IV.4]: high-pass f_ℓ^hi = 0 below 2350,
1 above 2500 (Eq. 5); low-pass f_ℓ^lo = 1 below 2000, 0 above 2150 (Eq. 6);
the sign is taken at the galaxy pixel; galaxies are kept only where
abs(T^lo) > 40 μK, because a small large-scale amplitude can have its sign set
by foregrounds; positive and negative weights are balanced. CMB lensing,
estimated by lensing a Gaussian CMB with AbacusSummit convergence and
stacking on light-cone haloes of mean log M ≈ 13.3 (M⊙/h), makes up about two
thirds of the stacked screening signal; with it, the screening and kSZ
optical depths agree. The kSZ side uses v_rms = 300 km/s and r = 0.25 for
the photometric sample. The 95% bound is A + Nσ_A with N = 1.64, A = 0.54,
σ_A = 0.61, against a mean τ ≈ 1.6 × 10⁻⁴ for the model. The CAP filter
cannot be used for screening because large-scale CMB leaks in; after
high-pass filtering, profiles with high, low and no feedback look alike,
so the information is in the amplitude.

### Step 4. Screening as a power spectrum
<!-- key: step-4-screening-as-a-power-spectrum -->

Kramer 2026 [src: arXiv:2608.27458, Sects. V.1, V.4.2, VI.1, VII.1]:
- TT quadratic estimator in the Hu–Okamoto form, the pipeline reproducing
  the DR6 lensing bandpowers; polarisation not used because of its noise.
  CMB range 600 ≤ ℓ ≤ 3000: ℓ_min follows the DR6 power-spectrum analysis,
  ℓ_max is where foregrounds overtake the CMB.
- Bandpowers over 100 < L^τ < 3000; L_min = 100 because of a large mean
  field; above ℓ_CMB,max the N⁰ noise rises sharply.
- Lensing: no bias hardening; the leakage N_L^{leak,τφ} is computed
  analytically from the response of the τ estimator to the lensing coupling
  ("an inefficient lensing estimator"), agreeing with simulations, and a
  secondary N¹ term is subtracted.
- Amplitude of an AMBER reionisation template (z_mid = 8, Δz = 4, A_z = 3,
  M_min = 10⁸ M⊙, l_mfp = 3 Mpc/h): A_τ = 180 ± 157, < 450 at 95%; null PTE
  0.68 for 21 dof; DR6 noise is ~1000 times the fiducial signal.
- Residual foregrounds from Websky, processed like the data (bispectrum and
  trispectrum terms): ΔA_τ = 0.33σ for the baseline coadd, 0.24–1.4σ across
  frequency choices, largest at 90 GHz; lowering ℓ_max reduces it at a cost
  in sensitivity.

### Step 5. Polarised SZ (remote quadrupole)
<!-- key: step-5-polarised-sz-remote-quadrupole -->

Krywonos 2026 [src: arXiv:2607.16071, Sects. 3, 4.1, 5.4, 5.5, 6]:
1. pSZ is the product of the optical depth (correlated with tracers) and the
   remote quadrupole (correlated with the local low-ℓ T and E); the optimal
   bispectrum amplitude estimator decomposes into a quadratic estimator of
   the remote quadrupole, by analogy with kSZ.
2. The amplitude b_q is the ratio of true to model C̄_ℓ^τg, the analogue of
   b_v: b_q = 1 means the gas model is right (Sect. 4.1). The quadrupole
   window W_q is the same as in kSZ velocity reconstruction with that tracer.
3. Templates of the remote quadrupole from inpainted Commander T and E,
   ℓ = 2–20, conditioned with ΛCDM spectra (Eq. 29).
4. Filters: tracer a_ℓm × C̄_ℓ^τg/C_ℓ^gg with a top-hat passband (without it
   the low-ℓ variance disagrees with the analytic noise N_q); polarisation
   E, B divided by B_ℓ C_ℓ, with a 5′ Gaussian B_ℓ; CIB point-source flux cuts
   (0.035, 0.10, 0.18 MJy/sr at 353, 545, 857 GHz) adjusted until N_q matches
   the reconstruction spectra; reference scale ℓ̄ = 200.
5. Validation on 1500 noise-only, signal-plus-noise and signal-only
   simulations at N_side = 1024.
6. Sensitivity peaks at ℓ ~ O(100), the two-halo regime, so pSZ carries
   little gas-profile information and is less suppressed by feedback than
   kSZ (Sect. 5.4). CIB 353 GHz gives ~4 times lower noise than unWISE;
   ACT 220 GHz ~10 times higher noise, a systematics check (Sect. 6).

### Step 6. Rotational kSZ
<!-- key: step-6-rotational-ksz -->

Yang 2026 [src: arXiv:2603.14494, Sects. 3.2, 3.3, 5.1, 5.3]:
1. Groups above a mass threshold in SDSS DR7 (2966 of 291,659) matched to
   haloes of a constrained simulation (2472 matched).
2. Axis: satellites with M_* < 10^10.5 h⁻¹M⊙ within r_vir and Δz = 0.004
   (~12 h⁻¹Mpc); for each trial angle a sinusoidal rotation curve is fitted
   to binned velocities; the angle maximising the amplitude defines the
   axis (method of Manolopoulou and Plionis 2017).
3. Selection fixed in advance: χ²/dof < 1, χ²_r/dof > 1 against a randomised
   curve, χ²/χ²_r < 0.4; 134 groups, mean log M_vir 14.19 (data), ⟨z⟩ = 0.066.
   The criteria are kept "unchanged" to avoid a look-elsewhere effect.
4. Planck map high-passed above 110′ (ℓ ~ 100); 4° × 4° patches rescaled by
   r_vir, rotated to the axis, weighted by N_sat v_rot; the Planck common
   mask applied.
5. Statistic: mean temperature difference between right and left
   half-disks of radius r_vir, ΔT = 25.5 μK (data), 12.8 μK (simulation).
6. Noise: 10,000 random rotations of the group positions on the real map
   (σ = 10.7 μK) or 10,000 Gaussian CMB + noise maps with Δ_T = 3.1 μK-arcmin
   (σ = 9.3 μK); 2.3σ or 2.7σ, the authors quoting the conservative 2.3σ.

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Screening: quadratic, sign, or hardened estimator
<!-- key: screening-quadratic-sign-or-hardened-estimator -->

The full quadratic estimator is optimal but its foreground and lensing
biases "are much larger than the signal"; hardening and component
separation suppress them at a noise cost and are not yet shown sufficient
(arXiv:2401.13033, Sect. II.3) [src]. The sign estimator pays π/2 in
variance for foreground immunity; lensing is then handled by filter choice
and validated on lensed simulations (same paper, Sects. II.4, III.3).
The power-spectrum analysis keeps the full estimator and subtracts an
analytic lensing leakage instead of hardening (arXiv:2608.27458,
Sect. V.4.2) [src]. With the filter edges of arXiv:2506.17379
(Eqs. 5–6), lensing was two thirds of the stacked signal [src]; the two
stacking papers use different filters and their lensing conclusions are
not reconciled in the parts read.

### Stacking or power spectrum
<!-- key: stacking-or-power-spectrum -->

A tracer-based stack targets late-time screening around known haloes; the
tracer-free power spectrum targets reionisation and is ~1000 times above
the fiducial signal in noise (arXiv:2608.27458, Sect. VI.1) [src].

### Moving lens: reconstructed velocities with a hard cutoff
<!-- key: moving-lens-reconstructed-velocities-with-a -->

The hard k_max separates the large-scale velocity from small-scale
foreground physics and is what makes the foreground bias small; it also
discards velocity modes above k_max (arXiv:2605.18938, Sect. VI.2) [src].

### pSZ tracer
<!-- key: psz-tracer -->

CIB maps give lower reconstruction noise than unWISE but carry Galactic dust
correlated with dust in the polarisation maps; with CIB, use 90–150 GHz CMB
channels (arXiv:2607.16071, Sect. 6) [src].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Moving-lens ℓ range | 6 log bins, 2500 ≤ ℓ ≤ 6000 | ACT DR6 × DESI-LS LRG | arXiv:2605.18938 | Sect. III.3 |
| Covariance coupling width | Δℓ = 11 (NGC, f_sky ≈ 0.09), 5 (SGC, 0.19) | same | arXiv:2605.18938 | Sect. III.3 |
| Reconstruction cutoff | k_max = 0.05 Mpc⁻¹; ℓ_* ≈ 129 at z = 0.7 | same | arXiv:2605.18938 | Sect. VI.2 |
| Null tests | 25 per sample, all p_0 > 0.05 | same | arXiv:2605.18938 | Sect. V.3 |
| 150 − 90 GHz null | b_ML = −0.19 ± 0.38 (main), +0.12 ± 0.39 (extended) | same | arXiv:2605.18938 | Sect. V.3 |
| 220 GHz-based differences | +2.02 to +2.28, errors 1.25–1.30 (1.6–1.8σ) | same | arXiv:2605.18938 | Sect. V.3 |
| 220 GHz single-frequency amplitude | 3.08 ± 1.29 | same | arXiv:2605.18938 | Sect. VI.1 |
| CIB prediction from Planck 545 GHz | Δb_ML = 0.00 ± 0.10 at 150 GHz (measured 1.06 ± 0.27) | same, GAL060 mask, 2000 ≤ ℓ ≤ 5000 | arXiv:2605.18938 | Sect. VI.1 |
| Sign-estimator variance cost | π/2 | ACT × unWISE | arXiv:2401.13033 | Sect. II.3 |
| τ-map high-pass | ℓ < 1600 removed | same | arXiv:2401.13033 | Sect. II.5 |
| Galaxies stacked | 34 M (blue), 19 M (green) | same | arXiv:2401.13033 | Sect. II.5 |
| Covariance simulations | 150 | same | arXiv:2401.13033 | Sect. V |
| Beta-profile slope | β = 0.86 fixed | same | arXiv:2401.13033 | Sect. VI.1 |
| Filter edges | low-pass 2000–2150; high-pass 2350–2500 | ACT DR5 × DESI LRG | arXiv:2506.17379 | Eqs. 5–6 |
| Large-scale amplitude cut | abs(T^lo) > 40 μK | same | arXiv:2506.17379 | Sect. III.3 |
| Lensing share of the stacked screening signal | ~2/3 | same | arXiv:2506.17379 | Sect. IV.1 |
| kSZ / screening significance | 7.2σ / 4.1σ; χ² 52.5 / 29.9 for 9 dof | same | arXiv:2506.17379 | Sect. IV.1 |
| Screening spectrum ranges | ℓ_CMB 600–3000; L^τ 100–3000 | ACT DR6 | arXiv:2608.27458 | Sects. V.1, VI.1 |
| Foreground bias on A_τ | 0.33σ (baseline); 0.24–1.4σ by frequency | same | arXiv:2608.27458 | Sect. VII.1 |
| pSZ templates | Commander ℓ = 2–20; ℓ̄ = 200 | Planck + ACT × unWISE, CIB | arXiv:2607.16071 | Sect. 5.5 |
| pSZ validation | 1500 simulations per type | same | arXiv:2607.16071 | Sect. 5.5 |
| pSZ forecast | σ(b_q) = 0.769, LiteBIRD × CIB 353 GHz (**forecast**) | same | arXiv:2607.16071 | Sect. 5.4 |
| rkSZ sample | 134 fast-rotating groups, ⟨z⟩ = 0.066 | Planck × SDSS DR7 | arXiv:2603.14494 | Sect. 3.3 |
| rkSZ noise | 10.7 μK (rotations), 9.3 μK (Gaussian) | same | arXiv:2603.14494 | Sect. 5.3.2 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Lensing in screening.** Odd-parity arguments do not protect a
  screening estimator; check with lensed simulations at the tracer
  positions (40 backlight maps in arXiv:2401.13033, Sect. III.3) or model
  the leakage (arXiv:2608.27458) [src]. An unexplained excess over the
  kSZ-implied τ is the symptom (arXiv:2506.17379, Sect. IV.1) [src].
- **Foreground sign leakage.** If the large-scale amplitude is small,
  foregrounds can set its sign: cut on abs(T^lo) (arXiv:2506.17379) [src];
  balance positive and negative weights, otherwise ~1% of the mean
  foreground remains (arXiv:2401.13033, Sect. II.5) [src].
- **ISW in the large-scale leg** of the screening estimator: remove ℓ ≲ 20
  or subtract an ISW map (arXiv:2401.13033, Sect. II.3) [src].
- **Moving lens with true velocities.** Simulation studies that used true
  halo velocities without a cutoff found foreground contamination larger
  than the signal; the pass criterion is a hard k_max and ℓ ≫ k_max χ_*
  (arXiv:2605.18938, Sect. VI.2) [src].
- **Moving-lens null suite.** Curl mode (parity), three frequency
  differences, NGC − SGC, each on three footprints; pass at p_0 > 0.05. The
  220 GHz channels are the weakest point, tested against Planck 353/545 GHz
  with a modified blackbody (β_d = 1.7, T_d = 10.7 K) and a GAL060 mask
  (arXiv:2605.18938, Sects. V.3, VI.1) [src].
- **Screening power spectrum.** Websky residuals give up to 1.4σ at 90 GHz;
  a single-frequency consistency test shows the 90 GHz contamination
  (arXiv:2608.27458, Sect. VII.1) [src].
- **pSZ.** Excess low-ℓ power with CIB tracers that grows with CMB frequency
  means dust correlated between maps; anisotropy from bright CIB sources
  breaks the agreement between N_q and the reconstruction spectra
  (arXiv:2607.16071, Sects. 5.5, 6) [src]. Test: reconstruction spectra
  against the analytic noise, frequency by frequency.
- **Rotational kSZ.** Redshift-space tilts of the satellite distribution and
  interlopers bias rotation amplitudes by up to tens of percent, so the
  simulation comparison is done in redshift space; a merger-like split of
  the simulation shows no change; the result applies to the selected
  fast-rotating groups only (arXiv:2603.14494, Sects. 3.2, 3.3) [src].

## Reading list
<!-- key: reading-list -->

- Foundation: Hotinli 2018, arXiv:1812.03167 — transverse velocities from
  the moving lens (in L2).
- Foundation: Dvorkin 2008, arXiv:0812.1566 — quadratic estimator of τ(n̂)
  (in L2).
- Method: Coulton 2024, arXiv:2401.13033 — sign estimator, lensing-safe
  filters, foreground and lensing validation, null significance.
- Application: Hotinli 2026, arXiv:2605.18938 — moving-lens estimator,
  symmetry arguments, empirical covariance, 25 null tests, CIB check.
- Critique: Hadzhiyska 2025, arXiv:2506.17379 — lensing dominates a stacked
  screening signal; kSZ–screening comparison.
- Application: Kramer 2026, arXiv:2608.27458 — screening power spectrum,
  analytic lensing leakage, foreground budget.
- Method: Krywonos 2026, arXiv:2607.16071 — pSZ bispectrum, b_q,
  remote-quadrupole templates, tracer choice.
- Application: Yang 2026, arXiv:2603.14494 — oriented stacking with
  pre-registered selection; two noise estimates.

## Not verified
<!-- key: not-verified -->

- The curved-sky moving-lens pipeline and its surrogate normalisation
  (arXiv:2605.18938, Sect. III.2 and App. A) and the fiducial P_gΨ.
- The exact low- and high-pass filter formulas of arXiv:2401.13033 (the
  equations were not rendered); only their stated criteria are given.
- The companion paper on lensing bias in real-space screening estimators
  cited by arXiv:2506.17379 (its ref. [91]) and the "temperature inversion"
  estimator of arXiv:2401.13040 beyond L2.
- The pSZ constraints themselves (Sect. 8 of arXiv:2607.16071) beyond the
  L2 values.
