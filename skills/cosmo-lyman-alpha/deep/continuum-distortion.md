# Continuum fitting and the distortion matrix — cosmo-lyman-alpha dossier

Scope: how the picca continuum fit is run step by step, why the measured δ
field is re-projected, how the distortion matrix is computed and approximated,
which alternatives (fitted broadbands, mode de-weighting, mode marginalisation,
small-scale template marginalisation) exist and what each costs, and which
tests show that the treatment is adequate for BAO and for the full shape.
Snapshot: 2026-10-16.
From: Chaves-Montero et al. 2026 review (arXiv:2605.22489), Sect. 0.4.1;
DESI 2024 IV Lyα BAO (arXiv:2404.03001), Sects. 2.5 and 4.3.

Already in L2, not repeated here: the definition of δ and the DESI continuum
model (`physics-and-methods.md#definition`); the projector η and the pixel
weights as written in DESI DR1, with γ_α = 2.9 and η_LSS = 7.5
(`physics-and-methods.md#estimators`); the alternative per-object continuum
methods (PCA, LyCAN, composites, splines) and their accuracies
(`physics-and-methods.md#alternative-continuum-methods`); the size, mitigation
and referee expectations (`systematics.md#a1-continuum-fitting-and-the-distortion-of`);
the small-scale leakage and its marginalisation as a covariance update
(`systematics.md#d1b-leakage-of-small-scales-through-the`,
`physics-and-methods.md#full-shape-and-alcock-paczynski`).

Notation: q a quasar (one forest), λ an observed wavelength, Λ ≡ log λ, f the
observed flux, F̄C_q the product of mean transmission and continuum, δ^t the
true transmission fluctuation, δ^m the measured one, δ^mp the projected
measured field, w a pixel weight, A or M a bin of the measured correlation
function in (r_⊥, r_∥), A′ or N a bin of the undistorted model. This follows
Busca et al. 2025 (arXiv:2506.15262); DESI DR1 writes δ̃ for the projected
field and η for the projector (arXiv:2404.03001, Eqs. 7–8).

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Fit F̄C_q per forest, iteratively, with a fitted variance model
<!-- key: step-1-fit-fcq-per-forest-iteratively-with-a -->

The model is F̄C_q(λ) = C̄(λ_RF)(a_q + b_q (Λ − Λ_min)/(Λ_max − Λ_min))
(arXiv:2306.06312, Eq. 4), with C̄(λ_RF) a universal rest-frame shape and
(a_q, b_q) an amplitude and tilt per forest. F̄ and C_q are not separated
because "they are not needed separately in our analysis" [src: Sect. 3.3].
(a_q, b_q) maximise 2 ln L = −Σ_i [f_i − F̄C_q]²/σ_q² − Σ_i ln σ_q² (Eq. 5);
the ln σ² term is kept because σ_q depends on (a_q, b_q) [src: same].

The flux variance is modelled as σ_q²/(F̄C_q)² = η(λ) σ̃²_pip,q + σ²_LSS(λ)
(arXiv:2306.06312, Eq. 6), with σ̃_pip,q = σ_pip,q/F̄C_q the pipeline noise in
units of the expected flux, η(λ) a correction to the pipeline noise (written
η_pip in the DR1 BAO paper) and σ²_LSS the intrinsic variance of the forest
[src: Sect. 3.3]. The iteration, as listed in the EDR catalogue paper [src:
Sect. 3.3]:

1. Start from C̄ = 1, η = 1, σ²_LSS = 0.1.
2. Fit (a_q, b_q) for every forest with Eq. 5.
3. Compute δ_q(λ).
4. Fit η(λ) and σ²_LSS(λ): bin δ_q in 20 wavelength bins × 100 bins of
   σ̃_pip (2000 cells), take the variance in each cell, fit Eq. 7 at each
   wavelength; cells with fewer than 100 pixels are discarded; if a fit fails
   the previous values are kept.
5. Recompute C̄(λ_RF) as the weighted mean of the expected fluxes at fixed
   λ_RF.
6. Repeat; five iterations give stable estimates.

eBOSS DR16 ran the same loop "until stable values are obtained after about
five iterations", separately for the Lyα and Lyβ regions (arXiv:2007.08995)
[src: Sect. II.4]. BOSS DR12 used ten iterations, with stability of ~10⁻⁴ on
C̄ and F̄, and a likelihood that convolved an assumed transmission PDF D(F, z)
with Gaussian noise ("method 2", log-normal D) or a narrow Gaussian D
("method 1", which yields only the product C_qF̄) (arXiv:1702.00176, Eqs. 3–5)
[src: Sect. 4.1]. The F̄(z) it returns depends on D and "should therefore not
be considered as a measurement of the mean absorption" [src: same]; that is
the origin of the statement in `systematics.md#a2-mean-transmission-and-the-amplitude`.

DESI performs the fit "in each of the analysed regions independently", so a
quasar can carry up to three (a_q, b_q) pairs (Lyα regions A and B, and the
C III calibration region) (arXiv:2404.03001) [src: Sect. 2.5].

### Step 2. Discard forests the fit cannot handle
<!-- key: step-2-discard-forests-the-fit-cannot-handle -->

- A region is discarded when the fitted F̄C_q is negative in at least one
  pixel (arXiv:2404.03001) [src: Sect. 2.5].
- Forests need at least 150 pixels of 0.8 Å, because short forests produce
  the long tail of large |b_q/a_q| where "fitting the real continuum of the
  quasar is difficult" (arXiv:2306.06312) [src: Sect. 4.3]. 150 × 0.8 Å =
  120 Å [der], which is the "forests shorter than 120 Å discarded" of the DR2
  paper quoted in `physics-and-methods.md#definition`: the same cut in
  different units.

### Step 3. Project the measured field
<!-- key: step-3-project-the-measured-field -->

Because (a_q, b_q) are fitted on the forest itself, δ^m at one pixel mixes all
true δ^t of the same forest. In a flat-spectrum toy with unit weights,
δ^m = δ^t + n/f_0 − ε − ε(δ^t + n/f_0) + O(ε²), where ε is the weighted mean
fluctuation of the forest with a Λ-dependent factor (arXiv:2506.15262,
Eqs. 5–6); for DESI 0.8 Å pixels a forest has N ≈ 600 pixels and the rms of ε
at completed-survey noise is of order 0.05 [src: Sect. 2].

The pipeline then removes the weighted mean and slope exactly:
δ^mp_qλ = Σ_λ′ η_qλλ′ δ^m_qλ′ with
η_qλλ′ = δ^K_λλ′ − (w_qλ′/W_q)[1 + Λ_qλ Λ_qλ′ / mean(Λ²_qλ)]
(arXiv:2506.15262, Eq. 7), W_q = Σ_λ w_qλ. The reason for projecting rather
than using δ^m: if δ^m − δ^t = A_q0 + A_q1 Λ_qλ (Eq. 8), the projection
cancels both terms and δ^mp = δ^tp (Eq. 9), so the correlations of the
projected measured field equal those of the projected true field, which can be
computed from a model [src: Sect. 2]. In DESI DR1 the projection is built with
the correlation weights w rather than the continuum-fit weights w^cont; to
first order this makes η_ij the full relation between δ̃ and δ^t, so η^cont is
never needed (arXiv:2404.03001, Eq. 8) [src: Sect. 3.1].

BOSS DR12 introduced this explicit subtraction "to simplify this effect and
facilitate its correction"; it also nearly removed the difference between its
two continuum methods, to 0.056 of the rms uncertainty per bin
(arXiv:1702.00176, Eq. 7) [src: Sect. 4.1].

For the cross-correlation, eBOSS DR16 also subtracts the weighted mean δ per
observed-wavelength bin after projection (arXiv:2007.08995, Eq. 8), because
the projection lets that mean drift from zero; the step "ensures that the
cross-correlation approaches zero at large scale, whatever the redshift
distribution of the quasars" [src: Sect. II.4]. On mocks the true δ^t in front
of quasars has a non-zero mean of ≈ 7 × 10⁻⁴, which must be subtracted for the
same reason before correlating the true field (arXiv:2506.15262) [src: Sect. 4].

### Step 4. Compute the distortion matrix
<!-- key: step-4-compute-the-distortion-matrix -->

Replacing δ^t δ^t products by the undistorted model gives
ξ_A = Σ_A′ D_AA′ ξ^at_A′(z_0) with
D^auto_AA′ = W_A⁻¹ Σ_{(qλ,q′λ′)∈A} w_qλ w_q′λ′ Σ_{(qλ″,q′λ‴)∈A′} η_qλλ″ η_q′λ′λ‴ f^auto_A′(λ″, λ‴, z_0)
(arXiv:2506.15262, Eqs. 14–15), with f^auto = ((1+z″)/(1+z_0))^(γ_α−1)
((1+z‴)/(1+z_0))^(γ_α−1), γ_α = 2.9 (Eq. 16), and for the cross-correlation
Eq. 17 with f^cross carrying γ_Q = 1.44 for the quasars (Eq. 18) [src: Sect. 3].
The function f is the DR2 addition; BOSS, eBOSS and DESI DR1 used f = 1
(Eqs. 19–21), which assumes that the pairs entering A′ through the mixing are
representative of the pairs that measure ξ_A′ [src: Sect. 6].

Settings and the authors' reasons:

| Setting | Value | Reason given | Place read |
|---|---|---|---|
| Data bins | 4 h⁻¹Mpc, 0–200 h⁻¹Mpc in r_⊥ and r_∥ (2500 bins, auto) | — | arXiv:2404.03001, Sect. 3.1 |
| Model bins | 2 h⁻¹Mpc | improvement over eBOSS | arXiv:2404.03001, Sect. 4.3 |
| Model r_∥ range | to 300 h⁻¹Mpc (eBOSS: 200) | DESI forests are ~400 h⁻¹Mpc long, so measured correlations mix with much larger separations; distortions had not converged for r_∥ > 150 h⁻¹Mpc | arXiv:2506.15262, Sect. 3 |
| Pairs used | 1% of the Lyα pixels | the computation is "computationally intensive"; doubling to 2% does not change BAO | arXiv:2404.03001, Sects. 4.3, 6.4 |
| Redshift evolution | included from DR2 | improves the fit to mocks; Δχ² = −4 on data; negligible BAO change | arXiv:2503.14739, Sect. III.1 |
| Pixel width | 0.8 Å for the fit; DR2 re-bins the fitted δ by three pixels to 2.4 Å | — | arXiv:2404.03001, Sect. 2.5; arXiv:2503.14739, App. B |

Structure: diagonal elements are very near unity; off-diagonal elements
vanish unless r_⊥A ≈ r_⊥A′ (neighbouring forests are nearly parallel), where
they are a few percent. Small off-diagonal terms do not mean a small
distortion, because they multiply correlations much larger than the diagonal
one (arXiv:2506.15262) [src: Sect. 3]. The distortion is largest at small r_⊥;
at small r_⊥ and large r_∥ the measured correlation falls below the true one
because the mixing subtracts part of the large positive small-r_∥
correlations [src: Sect. 2].

### Step 5. Distort the model, then fit
<!-- key: step-5-distort-the-model-then-fit -->

The fitter multiplies the physical model by D before comparing with data
(arXiv:2007.08995) [src: Sect. III.5]. In full-shape fits DESI DR2 adds one
free amplitude per undistorted bin T at r < r_min. Writing these amplitudes
as a vector a (the paper calls them η, not to be confused with the projector)
and their templates Δ̂_MT = Σ_N D_MN Δ_NT, with Δ_NT = 1 when the fine model
bin N lies in the coarse bin T, the marginalised χ² uses
C̃ = C + Δ̂ S Δ̂ᵀ (arXiv:2607.27410, Eqs. 16–17), with S the prior covariance
of the amplitudes; their best-fit values are recovered at the end by Eq. 18
[src: Sect. III.3]. "We add as many templates … as there are data bins at
r < r_min" and keep those bins in the χ², so no degrees of freedom are added
[src: same]. One consequence: after this marginalisation the data lost
sensitivity to the six Arinyo non-linear parameters, which were then fixed
to ForestFlow values from the DESI DR1 P1D (q_1 = 0.303, q_2 = 0.267,
k_v = 0.576, a_v = 0.443, b_v = 1.66, k_p = 11.062), with no significant
effect on values or errors [src: Sect. III.2.1].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### How to absorb the continuum-fitting distortion
<!-- key: how-to-absorb-the-continuum-fitting-distortion -->

| Approach | Used by | What it assumes | Cost | Place read |
|---|---|---|---|---|
| Additive power law in r and μ, 12 free parameters | BOSS DR9–DR11 auto (Busca 2013, Delubac 2015) | distortion is smooth | 12 nuisance parameters; no physical link to the fit | arXiv:1702.00176, Sect. 4.3 [sec] |
| Multiplicative k_∥ suppression tending to 0 for k_∥ ≲ 2π/L, L ~ 380 h⁻¹Mpc, tuned on simulations to one parameter | Blomqvist 2015 cross-correlation | distortion acts on radial modes only | simulation tuning | arXiv:1702.00176, Sect. 4.3 [sec] |
| De-weight the linear modes of each forest in the covariance | Slosar et al. 2013 | δ^m − δ^t is linear in Λ | — | arXiv:1702.00176, Sect. 4.3 [sec] |
| Distortion matrix on the model, no free parameter | BOSS DR12 onwards, eBOSS DR16, DESI | same linearity; template errors and noise uncorrelated between forests; higher-order terms negligible | O(N_pairs) computation, sub-sampled; leaks small scales into all scales | arXiv:1702.00176, Sect. 4.3; arXiv:2506.15262, Sect. 2 |
| Marginalise continuum modes inside an optimal estimator | optimal P3D estimator (mocks) | n_C = 2 modes (mean, tilt) per forest | errors ×35 at k = 2.1 × 10⁻² Mpc⁻¹, ×7 at 3.3 × 10⁻² Mpc⁻¹, +30% on average for k ≳ 5 × 10⁻² Mpc⁻¹; correlations between multipoles extend to Δℓ = 8 | arXiv:2503.15619, Sects. 3.4, 4.1.3 |

BOSS DR12 chose the matrix to avoid free parameters: "we do not introduce
free parameters to account for the effects of continuum-fitting"
(arXiv:1702.00176) [src: Sect. 4.3]. The optimal estimator chose
marginalisation because the projected modes otherwise suppress the monopole on
large scales, boost the quadrupole on all scales and create spurious ℓ ≥ 6
power, which "makes theoretical modeling difficult"; with marginalisation the
ℓ = 6 distortion is completely removed on Gaussian simulations
(arXiv:2503.15619) [src: Sect. 4.2.2]. Its authors note that the continuum fit
also introduces higher-order correlations that they do not address [src:
same], and that the mode templates could be adapted to machine-learned
continua [src: Sect. 4.1.3].

### Original or redshift-dependent matrix
<!-- key: original-or-redshift-dependent-matrix -->

On ten completed-survey LyaCoLoRe mocks the redshift-dependent matrix performs
better than the original for μ > 0.95; both share a residual at large positive
r_∥ in the cross-correlation, which the authors attribute possibly to the
300 h⁻¹Mpc truncation (arXiv:2506.15262) [src: Sects. 4, 6]. DESI DR2 found
no measurable BAO difference between the two (arXiv:2506.15262 [src: Sect. 6];
arXiv:2503.14739 [src: Sect. III.1]). In the DR2 data-validation tests,
"dmat model z-indep", "dmat r_∥ < 200", "dmat 2%" and "dmat dr = 4" are the
four distortion-matrix variations run (arXiv:2503.14739) [src: App. B].

### Variance model: keep or drop the ε term
<!-- key: variance-model-keep-or-drop-the-term -->

eBOSS DR16 added ε(λ)/σ̃²_pip,q to the variance, for "the observed increase of
variance, at high SNR, most probably due to quasar-to-quasar spectral
diversity"; it is significant for ≈ 10⁻⁴ of the pixels, and η(λ) ranged from
1.04 at 360 nm to 1.20 at 580 nm (arXiv:2007.08995, Eq. 4) [src: Sect. II.4].
DESI dropped ε because even in the top 5% S/N quasars its contribution is
minimal; the authors plan a rest-frame continuum-variance term σ²_C(λ_RF)
instead (arXiv:2306.06312, Eq. 10) [src: App. A.2]. Re-adding ε ("ε free") is
one of the DR1 BAO robustness variations (arXiv:2404.03001) [src: Sect. 6.4.1].
In DESI EDR the fitted η deviates from 1 by ~2% (EDR+M2) and up to ~7.5%
(EDR), the latter from poorer pipeline variances early in survey validation
(arXiv:2306.06312) [src: Sect. 3.3].

### Weights in the projection and the correlation
<!-- key: weights-in-the-projection-and-the-correlation -->

The weight w = 1/(η σ̃²_pip + σ²_mod σ²_LSS) interpolates between noise-only
weighting (small σ²_mod) and equal weights at fixed redshift (large σ²_mod)
(arXiv:2306.06312, Eq. 8). At 0.8 Å pixels the optimum is near 7–8, giving 25%
smaller auto-correlation errors (20% in the caption of the paper's Fig. 10)
and 10% smaller cross-correlation errors; at 2.4 Å pixels the optimum is 3.1
and the auto gain only 8% [src: Sect. 4.1]. This is the ">20%" of
`systematics.md#a3-weighting-of-pixels`. σ²_mod is the parameter DESI DR1 calls
η_LSS (arXiv:2404.03001, footnote 9) [src: Sect. 3.1]. Because the same w
enters η, changing the weights changes D; the variations η_LSS = 3.5 and
Δλ = 2.4 Å (with η_LSS = 3.1) are run on DR1 and DR2 (arXiv:2404.03001
[src: Sect. 6.4.1]; arXiv:2503.14739 [src: App. B]).

### Same-spectrograph pairs: drop them or keep and model them
<!-- key: same-spectrograph-pairs-drop-them-or-keep-and -->

BOSS DR12 rejected same-spectrograph pairs at small r_∥ to avoid the sky-
subtraction excess. eBOSS DR16 kept them because the continuum fit spreads the
r_∥ = 0 excess into "a smooth distortion of the correlation function for all
r_∥", which rejecting the pairs did not remove; keeping them lets the fit
determine its amplitude. The spurious r_∥ = 0 correlation reaches ≈ 20% of the
physical one at r_⊥ ≈ 50 h⁻¹Mpc; it is smooth elsewhere and does not affect
BAO but does affect the Lyα bias parameters (arXiv:2007.08995) [src:
Sects. III.2, IV.5]. DESI keeps this logic with one amplitude a_noise
(`systematics.md#c3-correlated-pipeline-noise-in-3d`).

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Iterations of the continuum fit | 5 | DESI EDR, eBOSS DR16 | arXiv:2306.06312; arXiv:2007.08995 | Sect. 3.3; Sect. II.4 |
| Iterations, stability | 10, ~10⁻⁴ | BOSS DR12 | arXiv:1702.00176 | Sect. 4.1 |
| Variance-fit grid | 20 λ × 100 σ̃_pip bins; cells < 100 pixels dropped | DESI EDR | arXiv:2306.06312 | Sect. 3.3 |
| Minimum forest length | 150 pixels of 0.8 Å (= 120 Å [der]) | DESI | arXiv:2306.06312 | Sect. 4.3 |
| Pixels per forest | N ≈ 600 | DESI | arXiv:2506.15262 | Sect. 2 |
| rms of mixing term ε | ~0.05 | DESI completed survey | arXiv:2506.15262 | Sect. 2 |
| Same-forest correlation ε δ^t | ~1% | DESI | arXiv:2506.15262 | Sect. 2 |
| Typical forest length | ~400 h⁻¹Mpc (DESI); ~380 h⁻¹Mpc (BOSS) | — | arXiv:2506.15262; arXiv:1702.00176 | Sect. 3; Sect. 4.3 |
| D off-diagonal size | a few percent, only for r_⊥A ≈ r_⊥A′ | DESI mocks | arXiv:2506.15262 | Sect. 3 |
| Pairs used for D | 1% (2% as variation) | DESI DR1, DR2 | arXiv:2404.03001 | Sect. 4.3 |
| γ_α, γ_Q in D | 2.9, 1.44 | DESI DR2 | arXiv:2506.15262 | Eqs. 16, 18 |
| γ_α range tested | 2.5–3.4: small effect | mocks | arXiv:2506.15262 | Sect. 4 |
| β_Lyα, standard vs true continuum | 1.452 ± 0.005 vs 1.528 ± 0.004 (auto); ≈ 4% low | 10 DESI Y5 mocks | arXiv:2506.15262 | Table 1 |
| b(1 + 0.7β), standard vs true | 0.2762 vs 0.2774 (auto): sub-percent | same | arXiv:2506.15262 | Table 1 |
| 0.6α_∥ + 0.4α_⊥ | 0.9998 ± 0.0013 (standard, auto) | same | arXiv:2506.15262 | Table 1 |
| 0.4(α_∥−1) − 0.6(α_⊥−1) | 0.0060 ± 0.0036 (standard, auto), ≈ 1.7σ, read as a fluctuation | same | arXiv:2506.15262 | Sect. 5, Table 1 |
| Spurious mean δ^t in front of quasars | ≈ 7 × 10⁻⁴ | mocks | arXiv:2506.15262 | Sect. 4 |
| Δχ² from z-evolution in D | −4 | DESI DR2 data | arXiv:2503.14739 | Sect. III.1 |
| Optimal σ²_mod (η_LSS) | 7–8 at 0.8 Å (7.5 adopted); 3.1 at 2.4 Å | DESI EDR | arXiv:2306.06312 | Sect. 4.1 |
| Sky-noise excess at r_∥ = 0 | ≈ 20% of ξ at r_⊥ ≈ 50 h⁻¹Mpc | eBOSS DR16 | arXiv:2007.08995 | Sect. IV.5 |
| Error inflation from mode marginalisation | ×35, ×7, +30% (see above) | optimal P3D, mocks | arXiv:2503.15619 | Sect. 4.1.3 |

The Busca et al. Table 1 values are means of ten mocks with errors equal to
the dispersion divided by √10, fitted over 10 < r < 180 h⁻¹Mpc with b_Q fixed
to 4.04 for the cross-correlation [src: Sect. 5]. The "true continuum" column
uses the true δ^t with D set to unity.

## What goes wrong
<!-- key: what-goes-wrong -->

- **Short forests.** Large |b_q/a_q| and poor fits; caught by the
  distribution of b_q/a_q and removed by the 150-pixel cut (arXiv:2306.06312)
  [src: Sect. 4.3].
- **Negative expected flux.** The fit is unphysical; the region is dropped
  (arXiv:2404.03001) [src: Sect. 2.5]. Report the number lost (its Table 1).
- **Non-linear continuum errors.** Quasar diversity that is not linear in Λ
  breaks Eq. 8 of Busca et al.; the method then relies on template errors
  being "local astrophysical effects" uncorrelated between forests
  (arXiv:2506.15262) [src: Sect. 2]. Test: mocks with realistic continua
  (simqso with emission-line diversity) where δ^t is known [src: Sect. 4].
- **Truncated or coarse matrix.** Residuals at large positive r_∥ in the
  cross-correlation, possibly from truncation at 300 h⁻¹Mpc; the authors
  propose extending |r_∥|, narrower bins and independent redshift bins
  (arXiv:2506.15262) [src: Sects. 4, 7]. Test: the four "dmat" variations
  of DR2.
- **Wrong redshift evolution in D.** Measurable on mocks for γ_α in 2.5–3.4,
  small; "more precise measurements of … γ_α are necessary" to quantify it on
  data (arXiv:2506.15262) [src: Sects. 4, 7].
- **Bias parameters read at face value.** The distortion treatment leaves a
  ≈ 4% low β on mocks while BAO is unaffected [src: Table 1]; an analysis
  that uses β (full shape, cross-checks of b_η) should state this.
- **Scale cut taken to remove small scales.** Through D, r_∥ < 10 h⁻¹Mpc
  of the model reaches all data bins; marginalise the undistorted small-scale
  bins (arXiv:2607.27410) [src: Sect. III.3].
- **Correlated pipeline noise.** Through the continuum fit an r_∥ = 0 excess
  becomes a smooth distortion everywhere; dropping the pairs does not cure it
  (arXiv:2007.08995) [src: Sect. IV.5].
- **Contaminants absent from the test mocks.** The Busca et al. tests use
  mocks without metals or HCDs and call for repeating them with both, and for
  more study of quasar-redshift errors (arXiv:2506.15262) [src: Sects. 4, 7].

Validation used in DESI DR1: BAO shifts under variations of the δ estimation
(no C III calibration, η_pip = 1, ε free, η_LSS = 3.5, Δλ = 2.4 Å) and of the
pixel selection, against a threshold of σ/3; shifts slightly beyond it from
adding or removing pixels are attributed to statistical fluctuations
(arXiv:2404.03001) [src: Sect. 6.4.1].

## Reading list
<!-- key: reading-list -->

- Foundation: Bautista et al. 2017, arXiv:1702.00176 — the explicit mean and
  slope subtraction, the distortion matrix, and the earlier alternatives it
  replaced (Sects. 4.1, 4.3).
- Application: du Mas des Bourboux et al. 2020, arXiv:2007.08995 — the
  variance model with ε, the per-wavelength mean subtraction for the
  cross-correlation, sky-noise and distortion together (Sects. II.4, III.5, IV.5).
- Method: Ramírez-Pérez et al. 2024, arXiv:2306.06312 — the DESI iteration
  step by step, the weight optimisation, the dropped ε term (Sects. 3.3, 4, A.2).
- Application: DESI 2024 IV, arXiv:2404.03001 — DESI DR1 settings and
  δ-estimation robustness variations (Sects. 2.5, 3.1, 4.3, 6.4.1).
- Application: DESI DR2 BAO, arXiv:2503.14739 — redshift-dependent matrix and
  its variations (Sect. III.1, App. B).
- Test: Busca et al. 2025, arXiv:2506.15262 — why the projection works, the
  matrix structure, quantitative mock test, open improvements.
- Alternative: Karaçaylı et al. 2025, arXiv:2503.15619 — continuum modes
  marginalised inside an optimal P3D estimator, and the cost in errors.
- Critique and remedy: DESI DR2 full shape, arXiv:2607.27410 — small-scale
  leakage through D and template marginalisation (Sect. III.3).

## Not verified
<!-- key: not-verified -->

- The functional form fitted for η(λ) and σ²_LSS(λ) in Eq. 7 of
  arXiv:2306.06312 (as printed, the χ²-like expression lacks a square; not
  checked against the PDF).
- How the Lyβ-region forest enters the DESI distortion matrices (only the
  Lyα(A) × Lyα(B) data vector was seen).
- The size of the percent-level AP bias from small-scale leakage (App. A of
  arXiv:2607.27410, not read).
- Whether any DESI analysis uses a machine-learned continuum (LyCAN,
  arXiv:2405.06743) in place of the picca fit; no such analysis was read.
- The original Busca 2013, Delubac 2015 and Blomqvist 2015 descriptions,
  known here only through arXiv:1702.00176.
