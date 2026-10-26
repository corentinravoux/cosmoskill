# Delensing of B modes — cosmo-inflation-primordial dossier

Scope: how a lensing B-mode template is built (mass tracer, E-mode filter,
template formula), how it enters the r analysis (map subtraction or extra
spectral channel), how the delensing efficiency is defined and measured,
and the biases specific to delensing, with the choices current analyses
make and their stated reasons.
Snapshot: 2026-10-17.
From: SO science goals (arXiv:1808.07445), Sects. III.4.3 (delensing) and
V.1 (delensing efficiency); Achúcarro et al. 2022 review
(arXiv:2203.08128), Sect. 2.2.1.

Already in L2, not repeated here: the foundations (Knox & Song, Kesden et
al.) and the BK14 + SPTpol + Planck σ(r) gain in
`physics-and-methods.md#delensing`; the BK-SPT sizes of the CIB–φ
misestimate and polarisation-efficiency tests in
`systematics.md#b3-lensing-b-modes-and-delensing`; the SO six-SAT σ(r) at
the two reduced lensing amplitudes in `systematics.md#b11-so-six-sat-forecast-how-sigma-r-moves`.
Lensing reconstruction itself (quadratic estimators, mean field, N0/N1) is
the subject of the `cosmo-cmb` dossier `deep/lensing-reconstruction.md`;
only what delensing adds to it is here.

## How it is done
<!-- key: how-it-is-done -->

Notation: E, B the polarisation modes; κ the lensing convergence (φ the
potential); κ̂^i a tracer of κ (an internal quadratic estimator, a galaxy
density map, the cosmic infrared background CIB); ρ_L the correlation
coefficient between a tracer and the true κ at lensing multipole L;
B_t the template; A_lens the fraction of lensing B-mode power left after
delensing; l a CMB multipole.

### Step 1. Build the best mass map
<!-- key: step-1-build-the-best-mass-map -->

Tracers are co-added with weights that maximise the correlation with the
true κ (Hertig et al. 2024, arXiv:2405.01621, Eq. 12):
κ̂^comb_LM = Σ_ij (ρ⁻¹)^ij_L ρ^{jκ}_L √(C_L^{κκ}/C_L^{κ̂iκ̂i}) κ̂^i_LM,
which implies C_L^{κκ̂comb} = C_L^{κ̂combκ̂comb} = C_L^{κκ} Σ_ij ρ^{iκ}(ρ⁻¹)^{ij}ρ^{jκ}
(Eq. 13) [src: Sect. II.1.2]. Correlations between different L are
ignored; the authors state that accounting for them would not
significantly improve σ(r) in their Gaussian set-up [src: same, footnote].

Two ways of getting the weights:

- **From simulations**: SO computes them empirically from smoothed auto-
  and cross-spectra of simulated tracers, because analytic weights stop
  being optimal with a mask, inhomogeneous noise and foreground residuals
  [src: Namikawa et al. 2021, arXiv:2110.09730, Sect. II.4].
- **From smooth fits to data**: ACT DR6 fits smooth models through the
  measured tracer spectra (linear-in-z bias for each unWISE sample, a
  normalisation and a dust power law for the CIB) before computing weights,
  "to avoid biases caused by statistical fluctuations in the measured
  correlations"; the model is a smoothing device, not a physical fit
  [src: Hertig et al. 2025, arXiv:2511.21949, Sect. V].

Internal reconstruction combines ΘΘ, ΘE, EE and EB estimators; ΘB is
dropped for its low signal-to-noise [src: arXiv:2405.01621, Sect. II.1.2].
Multipole ranges in use:

| Analysis | CMB fields in the estimator | κ range in the template | External tracers | Place read |
|---|---|---|---|---|
| SO forecast pipeline | 301 ≤ l ≤ 4096; temperature 500 < l < 3000 | 20 < L < 2048 | Planck-like CIB, LSST-like galaxies | arXiv:2405.01621, Sect. II.1.2 |
| SO multitracer | — | 20 ≤ L ≤ 2048 | galaxies in six bins with edges z = 0, 0.5, 1, 2, 3, 4, 7, and CIB | arXiv:2110.09730, Sects. II.4, III.3 |
| ACT DR6 | ACT lensing map (MV or Θ-only) | 40 ≤ L ≤ 2000 (ACT), 102 ≤ L ≤ 2000 (external) | unWISE Blue and Green, Planck GNILC CIB | arXiv:2511.21949, Sect. V |

Reasons given: the lower CMB cut at 301 removes the overlap between the B
modes in the EB estimator and the B modes to be delensed (Step 6); the
temperature range avoids atmospheric noise and extragalactic foregrounds
[src: arXiv:2405.01621, Sect. II.1.2]; L < 40 is removed because the mean
field exceeds the reconstructed signal there; external tracers start at
L = 102 because of Galactic dust at low L [src: arXiv:2511.21949,
Sect. V]. Which tracer matters where: internal reconstruction dominates for
L < 250, the CIB and galaxies for 250 < L < 1000 at SO LAT noise [src:
arXiv:2405.01621, Sect. II.1.2]; in the SO multitracer forecast LSST
galaxies contribute most, CMB lensing and CIB similarly [src:
arXiv:2110.09730, Sect. III.3].

### Step 2. Filter the E modes
<!-- key: step-2-filter-the-e-modes -->

Diagonal Wiener filter Ê^WF_lm = C_l^EE/(C_l^EE + N_l^EE) Ê_lm
(arXiv:2405.01621, Eq. 7; arXiv:2511.21949, Eq. 28). ACT takes N_l^EE from
map splits and keeps 100 ≤ l ≤ 2048, the lower bound set by its Fourier-
space filter [src: arXiv:2511.21949, Sects. II.4, V]. The full inverse-
variance (C⁻¹) filter solved by conjugate gradients, with infinite noise in
unobserved pixels, combines LAT and SAT maps optimally
(arXiv:2110.09730, Eq. 18); it raises the E-mode correlation with the
truth by 5–10% over the diagonal filter, and adding SAT E modes removes
more than 5% more lensing power [src: Sect. III.3]. Both 2024–2025
pipelines use the diagonal filter: SO to save CPU and to keep SAT
foreground residuals and systematics out of the template; ACT because its
noise is fairly uniform [src: arXiv:2405.01621, Sect. II.1.2;
arXiv:2511.21949, Sect. II.4].

### Step 3. Form the template
<!-- key: step-3-form-the-template -->

Gradient-order template from the filtered, lensed E modes
(arXiv:2110.09730, Eq. 17; flat-sky Eq. 25):
B^temp_l = ∫ d²l′/(2π)² W(l, l′) Ê^WF_l′ κ̂^comb_{l−l′}, with
W(l, l′) = 2 [l′·(l−l′)/|l−l′|²] sin 2(ψ_l − ψ_l′) (Eq. 24).

Why lensed E and gradient order: with lensed E modes new cancellations at
next-to-leading order allow a delensing floor as low as O(1)% of the
original power, while a gradient-order template from unlensed or delensed
E, or a non-perturbative remapping of lensed E, leaves a floor of O(10)%;
the gradient-order template also wins with noisy E and φ [src:
Baleato Lizancos et al. 2020, arXiv:2010.14286, abstract]. SO states its
first-order template is indistinguishable from optimal remapping until
residuals reach O(1)% [src: arXiv:2110.09730, Sect. II.5].

BICEP/Keck–SPTpol used a map-space "undeflect-and-difference" template
instead. Its extra noise comes from undeflecting Q/U maps that contain B
noise; nulling B before undeflecting reduces it, but by a fractionally
small amount for l < 500 in that data set [src: arXiv:2011.08163, App. A].

### Step 4. Use the template
<!-- key: step-4-use-the-template -->

**Map subtraction.** B^del = B̂ − α_l B^temp with α_l = C_l^{BB,cross}/C_l^{BB,temp}
minimising the variance (arXiv:2110.09730, Eqs. 19–20), so that
C_l^{BB,del} = Ĉ_l^BB [1 − (C_l^{BB,cross})²/(Ĉ_l^BB C_l^{BB,temp})] (Eq. 21).

**Cross-spectral.** The template is an extra "frequency channel": its
auto-spectrum and its cross-spectra with every frequency map enter the
multi-frequency likelihood with the foreground model [src:
arXiv:2110.09730, Sect. II.6; arXiv:2011.08163, Sect. II.2]. This
requires simulations of the template's signal and noise to (1) debias its
auto-spectrum, (2) predict the expectation values of the new spectra,
(3) build their covariance with the other bandpowers [src:
arXiv:2011.08163, Sect. II.2]. In BK-SPT the template auto-spectrum is
written as four terms (Eq. 10), and its noise bias, ⟨(n_QU ∗ (s_φ + n_φ))²⟩ +
⟨(s_QU ∗ n_φ)²⟩, is estimated from simulations and subtracted (Eq. 11); the
usual BICEP/Keck observing matrix does not apply to the template, so its
spectra are rescaled by the ratio of input lensing C_l^BB to the mean of
signal-only simulations [src: same].

**Equivalence.** For an ideal survey with negligible foreground residuals,
C^{BtB}_l = C^{BtBt}_l (arXiv:2405.01621, Eqs. 14–15), hence the subtracted
map has C_l^{BB,del} = C_l^BB − C_l^{BtBt} + N_l (Eq. 21), and the Fisher
information on r from the 2×2 spectral matrix (Eqs. 23–24) is identical to
that of the subtracted map (Eq. 22) [src: Sect. III]. The argument holds
on a cut sky if all maps share the same pixel weighting [src: same]. On
SO-like simulations, foreground cleaning applied to maps whose lensing
power was reduced by 65% gave the same σ(r) as cross-spectral delensing
[src: Sect. VI.3]. Reasons to prefer the cross-spectral route on the
ground: filtering against atmosphere is easier to handle in harmonic
space, and data splits give the noise spectrum [src: Sect. III]; ACT adds
that map-level subtraction is more sensitive to masking, filtering and
beam systematics [src: arXiv:2511.21949, Sect. II.4].

### Step 5. Define and measure the efficiency
<!-- key: step-5-define-and-measure-the-efficiency -->

With C^{BtB} = C^{BtBt}, the residual is C_l^{BB,del} ≈ C_l^{B̃B̃} − C_l^{BtBt}
(arXiv:2511.21949, Eq. 32) and the multipole-averaged residual fraction is
A_lens = mean over l of [1 − C_l^{BtBt}/C_l^{B̃B̃}] (Eq. 33), so that
C_l^{BB,del} ≈ A_lens C_l^{BB,lens} [src: Sect. II.4]. SO uses the general
form A_lens = 1 − mean[(C_l^{BtB})²/(C_l^BB C_l^{BtBt})] (arXiv:2405.01621,
Eq. 32). "Delensing efficiency" is 1 − A_lens.

On noise-dominated data, ACT measures the effect through the
noise-cancelling difference ΔC_l^BB = C_l^{BtBt} − 2C_l^{B̂Bt} (Eq. 44) and
fits an amplitude to the predicted ΔC_l: A_ΔC = 0.95 ± 0.05 over
100 ≤ l ≤ 1500, a detection of delensing at signal-to-noise 19.7 [src:
arXiv:2511.21949, Sect. VI.2, Eq. 45].

### Step 6. Weight the pixels
<!-- key: step-6-weight-the-pixels -->

For pseudo-C_l on an inhomogeneous patch, SO derives
w_i ∝ 1/(C_l^i + N_l^i) (arXiv:2405.01621, Eq. 31), applied as
w_i ∝ 1/(σ²_i,res + σ²_i,noise) (Eq. 25), with the lensing residual
σ²_res = A_lens × (5 μK·arcmin)² and σ²_noise = σ²_white/N_i^hit
(Eq. 33). Hit-count weighting is suboptimal for SO "as the residual
lensing variance surpasses the central white noise variance of the
mid-frequency SAT channels"; uniform weighting needs aggressive
apodisation [src: Sect. IV]. The same weights go on all SAT channels and
on the template, as the equivalence requires [src: same].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Which tracers
<!-- key: which-tracers -->

- **Internal only (iterative).** The CMB-S4 pipeline reconstructs κ
  iteratively from high-resolution maps and removes 92–93% of the lensing
  B-mode variance, compatible with σ(r) ≃ 5 × 10⁻⁴ (**forecast**)
  [src: Belkner et al. 2023, arXiv:2310.06729, abstract]. CMB-S4 is no
  longer funded (`surveys-and-data.md#planned`); the method stays relevant
  for SO and later.
- **Internal quadratic + external.** SO forecast 65% (baseline) and 70%
  (goal) removal in the SAT–LAT overlap, about 30–35% residual depending on
  scale, close to the isotropic-survey value; σ(r) = 0.0015 with the
  template against 0.003 without, for 50 ≤ l ≤ 200, foregrounds ignored
  (**forecast**) [src: arXiv:2110.09730, Sects. III.3–III.4].
- **What data achieve today.** ACT DR6 lensing + unWISE + Planck CIB:
  tracer correlation 55–85% with κ for L ≤ 2000; 39% of lensing power
  removed at 100 ≤ l ≤ 1500 on ACT B modes and 47% at 30 ≤ l ≤ 300 on
  Planck B modes, over 23% of the sky [src: arXiv:2511.21949, abstract].
  The 39% is 19% below the 48% possible with ideal E modes; "the fidelity
  of the lensing map is now the most important factor", where E-mode noise
  limited earlier Planck-based work [src: Sect. VI.2].
- **CIB alone (first demonstration).** On BK14 a perfect template would
  have cut σ(r) by only 26% (0.024 → 0.018), because lensing was
  subdominant to foregrounds and noise at that depth [src:
  arXiv:2011.08163, Sect. IV.1].
- **Early SO estimate.** Internal delensing with the LAT on 40% of the
  sky: A_lens = 0.71 (baseline; 0.80 with more pessimistic foreground
  cleaning); A_lens ≈ 0.5 was expected from external tracers, hence
  external delensing was named the primary path and internal delensing the
  cross-check [src: arXiv:1808.07445, Sect. V.1, Eq. 15].

### Internal-delensing bias: model it or cut it
<!-- key: internal-delensing-bias-model-it-or-cut-it -->

If the B modes in the EB (or any B-dependent) estimator overlap with the B
modes being delensed, the delensed spectrum is suppressed beyond the
removal of lensing; its variance also drops [src: Baleato Lizancos et al.
2020, arXiv:2007.01622, abstract]. In their SO-like configuration the bias
is about 80% of the signal power of the unbiased delensed spectrum, and
the variance of the biased spectrum is about 65% of the unbiased one with
l_cut = 300 [src: Sect. 4.2]. The bias multiplies the primordial power and
suppresses it more than lensing and noise, so modelling it loses
signal-to-noise on r, more so when separate surveys provide the
reconstruction and the large-scale B modes [src: Sect. 8]. The bias is
local in l, so excluding from the reconstruction every B mode at the
scales to be delensed removes it at little cost; this is "preferable over
an approach where the bias is modelled" and is the authors'
recommendation for quadratic and likelihood-based reconstructions alike
[src: Sect. 8]. SO adopts l ≥ 301 for this reason [src: arXiv:2405.01621,
Sect. II.1.2].

In data the bias is seen: with the full MV ACT lensing map the template ×
ACT B cross-spectrum shows an excess from l ≥ 600, exactly the minimum
multipole of the CMB fields used in the reconstruction; it comes from
correlated noise and disappears in simulations with independent noise.
It can make residuals "deceptively mimic near-perfect delensing". ACT
therefore uses the Θ-only reconstruction when delensing ACT B modes, at a
loss of efficiency; for future searches the stated best route is to
restrict the EB estimator to l > 300 [src: arXiv:2511.21949, App. C].
Using B modes and template from different instruments (SAT versus LAT)
also reduces it [src: same].

### Template order
<!-- key: template-order -->

Gradient order with lensed E (recommended) against non-perturbative
remapping or unlensed E: O(1)% against O(10)% residual floors (Step 3)
[src: arXiv:2010.14286, abstract].

### Delensing inside foreground cleaning
<!-- key: delensing-inside-foreground-cleaning -->

On SO-like simulations with the cross-spectral moment pipeline
(`deep/bmode-foreground-separation.md`), delensing with a 65%-efficient
template lowers σ(r) by 37% (d0s0), 31% (d1s1) and 27% (dmsm) at r = 0; the
moment parameters widen the posteriors and reduce the relative gain. With
r = 0.01 and d0s0, σ(r) goes from 2.2 × 10⁻³ to 1.5 × 10⁻³ (32%) [src:
arXiv:2405.01621, Sect. VI.3]. Gaussian and Hamimeche–Lewis likelihoods
agree for the SO patch; for BICEP/Keck-size patches the authors state a
non-Gaussian approximation is needed, especially at low l [src:
Sect. II.3].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Residual lensing power, SO SAT–LAT overlap | ≈ 30–35%; 65% (baseline), 70% (goal) removed | SO multitracer (**forecast**) | arXiv:2110.09730 | Sect. III.3 |
| σ(r) with / without template | 0.0015 / 0.003 (50 ≤ l ≤ 200, no foregrounds) | SO (**forecast**) | arXiv:2110.09730 | Sect. III.4 |
| σ(r) gain with cleaning | 37%, 31%, 27% (d0s0, d1s1, dmsm) | SO (**forecast**) | arXiv:2405.01621 | Sect. VI.3 |
| Template suppression from Wiener filtering | cross/auto ≈ 0.7 at 50 ≤ l ≤ 190 | SO | arXiv:2110.09730 | Sect. III.3 |
| Internal A_lens, LAT on 40% of sky | 0.71 (0.80 pessimistic cleaning) | SO 2019 (**forecast**) | arXiv:1808.07445 | Eq. 15 |
| Iterative internal delensing | 92–93% of lensing variance removed; σ(r) ≃ 5 × 10⁻⁴ | CMB-S4 (**forecast**) | arXiv:2310.06729 | abstract |
| Data: removed lensing power | 39% (ACT B, 100 ≤ l ≤ 1500), 47% (Planck B, 30 ≤ l ≤ 300) | ACT DR6 + unWISE + CIB | arXiv:2511.21949 | abstract |
| Data: tracer correlation | 55–85%, L ≤ 2000 | ACT DR6 | arXiv:2511.21949 | abstract |
| Data: amplitude of ΔC_l | 0.95 ± 0.05, SNR 19.7 | ACT DR6 | arXiv:2511.21949 | Eq. 45 |
| Data: cross/auto equivalence | A_× = 0.97 ± 0.02, χ²/dof 1.1 for 34 dof, PTE 0.32 | ACT DR6 | arXiv:2511.21949 | Eq. 49 |
| Perfect-template ceiling, BK14 | σ(r) 0.024 → 0.018 (26%) | BK-SPT | arXiv:2011.08163 | Sect. IV.1 |
| Perfect-template validation | |Δr| ≲ 0.002 between unlensed skies and lensed skies + perfect template | BK-SPT | arXiv:2011.08163 | Sect. IV.1 |
| Internal-delensing bias | ≈ 80% of signal power; variance ≈ 65% of unbiased (l_cut = 300) | SO-like | arXiv:2007.01622 | Sect. 4.2 |
| Template floors | O(1)% (gradient order, lensed E); O(10)% otherwise | theory | arXiv:2010.14286 | abstract |
| Pixel-weight lensing term | A_lens × (5 μK·arcmin)² | SO | arXiv:2405.01621 | Sect. IV |
| ACT bandpower width | ΔL = 100 (tracers), Δl = 40 (template × B), 10° apodisation | ACT DR6 | arXiv:2511.21949 | Sect. V |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Internal-delensing bias read as efficiency.** Shows up as a template ×
  B cross-spectrum excess starting at the minimum multipole of the
  reconstruction (ACT: l ≥ 600) and as residuals near zero. Test: compare
  the template auto-spectrum with its cross-spectrum with the data; they
  must agree for an unbiased template (ACT: A_× = 0.97 ± 0.02); rerun with
  independent noise in simulations [src: arXiv:2511.21949, Sect. VI.3,
  App. C]. Remedy: excise overlapping B modes [src: arXiv:2007.01622,
  Sect. 8].
- **Dust in the CIB or in the E modes.** Higher-point functions ⟨BEI⟩_c and
  ⟨EIEI⟩_c bias the delensed spectrum; small against statistical errors
  for ground-based experiments, possibly significant for space-based ones
  on very large scales, and mitigated by multi-frequency cleaning [src:
  arXiv:2102.01045, abstract]. These terms affect the auto- and cross-
  spectra differently, so the auto/cross equivalence test catches them
  [src: arXiv:2511.21949, Sect. VI.3].
- **Misestimated tracer spectra.** Wrongly shaped lensing residuals can be
  mistaken for a primordial signal [src: arXiv:2110.09730, Sect. IV].
  Test: check that the co-added tracer's cross-spectrum with the internal
  reconstruction equals the fiducial C_L^κκ, as the weights imply (ACT
  Eq. 48, Fig. 11) [src: arXiv:2511.21949, Sect. VI.3]. Size for the CIB in
  BK-SPT is in L2 (`systematics.md#b3-lensing-b-modes-and-delensing`).
- **Galaxy bias and non-linearity.** Treating the galaxy field as Gaussian
  and knowing only its linear bias gives a bias on r well within the
  statistical error even for a cosmic-variance-limited case with
  Rubin-like galaxies [src: Wang et al. 2025, arXiv:2507.04666, abstract].
- **Mean field and filtering.** Mean field dominates the internal
  reconstruction at L < 40 in ACT; Fourier-space filtering suppresses E and
  B power and needs transfer functions from simulations; the mask for
  spectra involving a quadratic estimator is the square of the CMB mask
  [src: arXiv:2511.21949, Sect. V].
- **Template statistics not described by simulations** (dust leaking into
  the template, low-l Planck residuals, non-Gaussian dust in the CIB). Test
  used by BK-SPT: spectrum-difference tests between baseline and varied l
  (Q/U) and L (CIB) ranges, with χ²_sys and χ_sys against simulated
  differences (Eqs. 17–18, Table 1) [src: arXiv:2011.08163, Sect. V].
- **Validating the pseudo-channel likelihood.** BK-SPT checks that lensed
  skies with a perfect template recover the same r as unlensed skies,
  realisation by realisation [src: arXiv:2011.08163, Sect. IV.1].
- **Weights tuned on r = 0.** SO keeps the r = 0 pixel weights for r = 0.01
  input, since r is unknown on real data [src: arXiv:2405.01621,
  Sect. VI.3].

## Reading list
<!-- key: reading-list -->

- Foundation: Knox & Song 2002, arXiv:astro-ph/0202286, and Kesden et al.
  2002, arXiv:astro-ph/0202434 (in L2) — why lensing sets a floor.
- Method: Namikawa et al. 2021, arXiv:2110.09730 — multitracer co-addition,
  C⁻¹ E filter, template formula, cross-spectral use, tracer-spectrum
  uncertainty.
- Method: Hertig et al. 2024, arXiv:2405.01621 — equivalence of map and
  cross-spectral delensing, optimal pixel weights, delensing inside the
  moment foreground pipeline.
- Method: Baleato Lizancos et al. 2020, arXiv:2007.01622 — internal-
  delensing bias and why to cut, not model, it.
- Method: Baleato Lizancos et al. 2020, arXiv:2010.14286 — which template
  to build.
- Application: BICEP/Keck and SPTpol 2021, arXiv:2011.08163 — first
  delensed r; template as pseudo-band; null tests.
- Application: Hertig et al. 2025, arXiv:2511.21949 — ACT DR6 template on
  data; efficiency definition; auto/cross test; internal bias in data.
- Forecast: Belkner et al. 2023, arXiv:2310.06729 — iterative internal
  delensing.
- Critique: Baleato Lizancos et al. 2021, arXiv:2102.01045 — foreground
  higher-point functions in CIB delensing.
- Critique: Wang et al. 2025, arXiv:2507.04666 — galaxy bias for galaxy-
  based delensing.

## Not verified
<!-- key: not-verified -->

- The body of arXiv:2310.06729 (iterative estimator, foreground models,
  per-set efficiencies): abstract only.
- The bodies of arXiv:2010.14286, arXiv:2102.01045 and arXiv:2507.04666:
  abstracts only.
- LiteBIRD multitracer delensing (Namikawa et al.) and SPT-3G or
  BICEP/Keck delensing beyond BK14: titles seen in a search, not read.
- The ACT DR6 excess-residual numbers when tracers are removed (Sect. VI.2,
  cut in the reading).
