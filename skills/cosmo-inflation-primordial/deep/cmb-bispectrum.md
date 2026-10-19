# CMB bispectrum estimation of f_NL — cosmo-inflation-primordial dossier

Scope: how a CMB bispectrum pipeline turns cleaned T and E maps into
f_NL^local, f_NL^equil and f_NL^ortho (optimal cubic estimator and its
linear term, the KSW, binned, modal, integrated-bispectrum and learned
separable reductions, normalisation, joint fits and lensing subtraction),
how the estimators are validated against each other and on simulations,
with the pass criteria the papers state, and how to choose between them.
Snapshot: 2026-10-19.
From: Achúcarro et al. 2022 (arXiv:2203.08128), Sect. 3.2.1 (CMB
bispectrum); SO science goals (arXiv:1808.07445), Sect. VI; Planck 2018 IX
(arXiv:1905.05697).

Already in L2, not repeated here: the template definitions (Eqs. 1–3 of
Planck 2018 IX) in `physics-and-methods.md#definitions-textbook`; the
Planck 2018 data set-up (maps, masks with f_sky = 0.779/0.781, ℓ ranges,
300 FFP10 realisations, CAMB templates) in
`physics-and-methods.md#cmb-bispectrum-estimators`; the lensing–ISW sizes,
the joint lensing fit and the per-estimator Table 5 values in
`systematics.md#c1-lensing-isw-bispectrum`; the result tables and the PR4
values in `results.md#primordial-non-gaussianity-from-the-cmb`. Map-level
component separation itself is the `cosmo-cmb` dossier
`deep/component-separation.md`.

## How it is done

Notation (Planck 2018 IX, arXiv:1905.05697, Sect. 3.1): a^X_ℓm the
harmonic coefficients of map X ∈ {T, E}; b^{X1X2X3}_{ℓ1ℓ2ℓ3} the reduced
bispectrum; 𝒢 the Gaunt integral; C the full TT/TE/EE covariance including
beam and noise; f_sky the unmasked sky fraction; ℓ_max the highest
multipole used. "Fisher error" means the error predicted by the inverse
Fisher matrix of the template.

### Step 1. Write the observable and the theory template

For a rotationally invariant sky and even-parity T/E combinations,
⟨a^{X1}_{ℓ1m1} a^{X2}_{ℓ2m2} a^{X3}_{ℓ3m3}⟩ = 𝒢^{ℓ1ℓ2ℓ3}_{m1m2m3}
b^{X1X2X3}_{ℓ1ℓ2ℓ3} (Eq. 23), with 𝒢 = ∫ Y_ℓ1m1 Y_ℓ2m2 Y_ℓ3m3 d²n̂
(Eq. 24). The Gaunt integral imposes the triangle condition and, with ℓ_max,
defines a tetrahedral domain of allowed triplets [src: arXiv:1905.05697,
Sect. 3.1]. The theory template b^th is the primordial shape projected
with radiation transfer functions; Planck computes templates and the
lensing bias with CAMB at the Planck 2018 best fit [src: Sect. 3.2.2].
PolySpec writes the same projection explicitly, with 𝒯^X_ℓ(k) the transfer
functions and B_ζ the primordial bispectrum (arXiv:2511.19179, Eq. 22).

### Step 2. The optimal cubic estimator and its linear term

In the limit of small non-Gaussianity the optimal polarised estimator is
(Creminelli et al. 2006, as written in arXiv:1905.05697, Eq. 25)

f̂_NL = (1/N) Σ 𝒢 b^th { [C⁻¹a]₁ [C⁻¹a]₂ [C⁻¹a]₃ − ( (C⁻¹)₁₂ [C⁻¹a]₃ + cyclic ) },

with C the block matrix of Eq. 26 and N fixed by unit response to b^th
when f_NL = 1. The first term is cubic in the data; the second, linear in
the data, corrects the variance increase caused by the breaking of
rotational invariance by the mask and by anisotropic or correlated noise
[src: Sect. 3.1]. Because full inverse-covariance filtering is
"numerically very demanding", Planck uses the diagonal-covariance form
(Eq. 27), in which C⁻¹_ℓ is the inverse of the 2 × 2 matrix of C_ℓ^TT,
C_ℓ^TE, C_ℓ^EE (Eq. 28), and the linear term subtracts C_{ℓ1m1,ℓ2m2}
a_{ℓ3m3} and permutations. Stated reason: with diffusive inpainting as a
pre-filter this approximation "still leads to uncertainties that are very
close to optimal" [src: Sect. 3.1]. The covariance pairs in the linear
term are Monte Carlo averages over simulations; PolySpec writes the same
structure as a cubic term minus 3 ã ⟨ãã⟩ with ã an inverse-variance
filtered map (arXiv:2511.19179, Eq. 23).

A brute-force sum over all triplets scales as ℓ_max⁵ and is "completely
unfeasible" [src: arXiv:1905.05697, Sect. 3.1]. The estimators below differ
only in how they avoid it.

### Step 3a. KSW: factorise the template

KSW filters the data into two maps on a grid of comoving distances r:
A(r, n̂) = Σ α_ℓ(r) b_ℓ a_ℓm Y_ℓm / 𝒞_ℓ and B(r, n̂) = Σ β_ℓ(r) b_ℓ a_ℓm
Y_ℓm / 𝒞_ℓ (Komatsu, Spergel and Wandelt 2005, arXiv:astro-ph/0305189,
Eqs. 7–8), with b_ℓ the beam, 𝒞_ℓ = C_ℓ b_ℓ² + noise, and β_ℓ(r) =
(2/π) ∫ k² dk P(k) g_Tℓ(k) j_ℓ(kr) (Eq. 6), g_Tℓ the radiation transfer
function and P the potential power spectrum; B is a Wiener-filtered map of
the primordial potential. The cubic statistic S_prim = 4π ∫ r² dr ∫
(d²n̂/4π) A B² (Eq. 9) equals the inverse-variance-weighted sum of
observed × theoretical bispectra over ℓ1 ≤ ℓ2 ≤ ℓ3 (Eq. 10), and f_NL
follows from S_prim ≃ f_NL Σ (ℬ^prim)²/(𝒞𝒞𝒞) (Eq. 14). Cost: N^(3/2)
per harmonic transform times about 100 radial points, against N^(5/2) for
the full bispectrum [src: astro-ph/0305189, Sect. III.1]. KSW applies to
templates that are, or are well approximated by, sums of products of
one-dimensional functions — the local, equilateral and orthogonal shapes
[src: arXiv:1905.05697, Sect. 3.1.1]. The skew-C_ℓ variant first builds a
"bispectrum-related power spectrum" whose shape-dependent slope helps
separate several non-Gaussian components [src: same].

Running non-Gaussianity: the equilateral running f_NL → f*_NL[(k1+k2+k3)/
(3k_piv)]^{n_NG} (Eq. 29) is not separable; Planck makes it separable with a
Schwinger parametrisation (Eq. 30) rather than with the geometric-mean form
(Eq. 31), because the former "behaves better numerically" while the two
are strongly correlated [src: Sect. 3.1.2]. n_NG itself is not fitted by
template; KSW estimates f*_NL on a grid of n_NG and the posterior of n_NG
is built analytically, with a flat prior on f*_NL whose meaning depends on
the pivot [src: same].

### Step 3b. Binned estimator: coarse-grain in ℓ

Starting point: the ideal full-sky estimator f̂_NL = ⟨b^th, b^obs⟩ /
⟨b^th, b^th⟩ (Bucher et al. 2010, arXiv:0911.1642, Eq. 21), with the inner
product ⟨b^A, b^B⟩ = Σ_{ℓ1≤ℓ2≤ℓ3} b^A b^B / Var[b^obs] (Eq. 22); ⟨b^th,
b^th⟩ is the total (S/N)² of the template. A non-ideal template
b^templ loses optimality by the factor Var(non-ideal)/Var(ideal) =
1/cos²θ (Eq. 30), θ being the angle between the two templates in that
inner product [src: arXiv:0911.1642, Sect. 2.4]. Binning: partition ℓ into
M bins I_A (Eq. 31), sum the bispectrum within each bin triplet (Eq. 32);
the implied template (Eq. 33) satisfies ⟨b^binned, b^th⟩ = ⟨b^binned,
b^binned⟩ (Eq. 34), so cos²θ measures the loss [src: Sect. 2.5]. The
stated physical reason binning is cheap: the bispectrum varies on the
acoustic period Δℓ ≈ 200 and the damping scale ℓ_damp ≈ 400, not on Δℓ = 1
[src: Sect. 2.4].

Bin choice: a divisional scheme with split parameters optimised on a grid
to maximise cos²θ, for ℓ_max = 2000 and Planck 100 GHz noise; 64 bins give
cos²θ = 0.993, a 0.7% variance increase, against 1999 multipoles [src:
Sect. 5.2, Table 2]. Planck 2018 uses 57 bins with boundaries 2, 4, 10, 18,
30, 40, 53, 71, 99, 126, 154, 211, …, 1897, 2001, 2091, 2240, 2500, fixed in
2015 "by minimizing the increase in the theoretical variance for the
primordial shapes due to the binning" [src: arXiv:1905.05697, Sect.
3.2.2]. Data and theory bispectra are binned and stored separately and
combined only in the final sum, so new shapes need no rerun of the maps,
the binned data bispectrum is a non-parametric product, and ℓ dependence
comes "for free" by dropping bins [src: Sect. 3.1.4]. The 2018 change: the
average of the squared Gaussian maps entering the linear term is
precomputed, an order-of-magnitude speed-up for 300 simulations [src:
same].

### Step 3c. Modal estimator: expand on separable modes

The shape function S(k1, k2, k3) is expanded on orthonormal polynomials
R_n of the tetrahedral domain, S = Σ α^R_n R_n with α^R_n = ⟨R_n, S⟩
(Fergusson et al. 2010, arXiv:0912.5516, Eqs. 81–82), and
transformed back to separable products Q_n through a triangular matrix λ
(Eqs. 85–86) so that a KSW-type fast sum applies; Parseval's theorem
(Eq. 84) makes the overlap of two shapes the dot product of their mode
vectors. Convergence is quantified by the correlation of the partial sum
with the target: better than 98% with 6 modes for primordial equilateral
and DBI shapes and 98% with 15 modes for their CMB bispectra at ℓ_max = 500;
the CMB expansion converges more slowly because it must follow the
acoustic peaks [src: arXiv:0912.5516, Sect. III.4, Fig. 9]. The data "mode
spectrum" is theory-independent: f_NL for any shape follows by correlating
its theoretical mode vector with the data one, which is why modal methods
suit scans of many models, and the modes give a smoothed model-independent
bispectrum reconstruction [src: arXiv:1905.05697, Sect. 3.1.3].

Planck 2018 runs two modal pipelines [src: Sect. 3.2.2]:

- Modal 1 expands TTT, EEE, TTE and EET separately, writes the normalisation
  in separable form and implements Eq. 27 directly; basis: 600 polynomial
  modes plus radial modes from the KSW expansion of the three standard
  templates "to speed up convergence for these shapes". Used for the three
  standard shapes and most validation tests.
- Modal 2 first orthogonalises T and E into uncorrelated coefficients and
  constrains the resulting bispectra independently; it cannot estimate EEE
  directly. Basis: 2000 polynomial modes plus a Sachs–Wolfe local template
  "to improve efficiency in the squeezed limit". Used for shapes with large
  parameter spaces such as oscillatory bispectra.

High-frequency oscillatory shapes beyond the reach of the modal and binned
bases use two dedicated estimators [src: same].

### Step 3d. Integrated bispectrum (PR4 reanalysis, temperature only)

The sky is divided into equal patches and the estimator is the average
over patches of (patch mean) × (patch power spectrum), minus a linear term
built from the same product with simulated patch spectra (Jung et al.
2025, arXiv:2504.00884, Sect. 2.3, first two equations). The theory
expectation is a sum over the bispectrum weighted by 3j and 6j symbols and
the patch window w_ℓ; the patches have w_ℓ = 1 for ℓ ≤ 10 and 0 otherwise,
so "we probe only the squeezed limit"; the covariance follows from the
weakly non-Gaussian approximation [src: Sect. 2.3]. The estimator is used
for T and for f_NL^local and the lensing amplitude only [src: Sect. 6,
table of simulation averages].

### Step 3e. Learned separable basis (non-separable models)

PolySpec fits a separable ansatz Σ_n w_n α_n β_n γ_n to a numerically
computed shape and evaluates the estimator in O(ℓ_max² log ℓ_max) as a
radial integral of products of filtered maps U[ã, f](r) (arXiv:2511.19179,
Eqs. 24–25), with the normalisation 𝓕 computed by Monte Carlo (Eq. 26)
and an idealised Fisher matrix by Gauss–Legendre quadrature (Eqs. 27–29)
[src: Sect. V.1]. Validation on Planck PR4: the learned representation of
the local (equilateral) shape has a 2D cosine of 99.93% (99.81%) with the
true template, and gives f_NL^neural = 2.9 ± 5.2 against f_NL^loc = 2.9 ±
5.0 (9 ± 48 against 8 ± 48); full and cyclic permutation sets agree within
0.1σ [src: Sect. V.3].

### Step 4. Normalise, fit jointly or subtract the lensing bias

With F_ab = ⟨B^a, B^b⟩ the Fisher matrix of templates a, b, the expected
variance of a single-shape f_NL is 1/F_aa, multiplied by 1/f_sky on a
masked sky. A contaminant of known amplitude f_NL^(2) biases shape 1 by
f_NL^(1),(2) = −(F_12/F_11) f_NL^(2); this is how the lensing bispectrum,
whose amplitude is 1, is subtracted. If the contaminant amplitude is
unknown, the joint estimator f̂^a = Σ_b (F⁻¹)_ab ⟨B̂, B^b⟩ is used and
the error becomes (F⁻¹)_aa [src: arXiv:2504.00884, Sect. 3.2]. In the
binned estimator the inner product includes the inverse of the T/E
covariance V of each bin triplet [src: same]. Planck quotes the three
primordial shapes "independent" (single-shape fits) after lensing
subtraction for its headline numbers (the L2 table); in the 2015
simulations a joint T+E binned fit of a local-only input gave local 11.5 ±
6.4, equilateral −7.5 ± 51, orthogonal −0.4 ± 29, illustrating the
template correlations [src: arXiv:1502.01592, Sect. 5.2].

### Step 5. Errors and linear term from simulations

Planck 2018: 300 FFP10 noise realisations through each component-
separation pipeline, 160 for the modal pipelines "to speed up the
computation", whose convergence with 160 maps was tested in earlier
releases [src: arXiv:1905.05697, Sect. 3.2.2]. PR4 reanalysis: 600 SEVEM
CMB + noise simulations [src: arXiv:2504.00884, Sect. 4]. PolySpec on PR4:
100 simulations for the linear term and a further 400 for the variance
[src: arXiv:2511.19179, Sect. V.3].

### Step 6. Validate

The Planck sequence, in the order the papers run it:

1. Estimator agreement map by map on 49 foreground-free simulations with
   lensing–ISW and no primordial signal, in three stages (beam only; plus
   anisotropic noise; plus a mask leaving 79% (T) and 76% (P) of the sky).
   Criterion as stated: "the typical discrepancy between the bispectrum
   estimators, even in this most realistic case, is less than about a
   third of the uncertainty on f_NL" [src: arXiv:1502.01592, Sect. 5.1,
   Tables 5–7].
2. Unbiasedness on 100 T + E simulations with f_NL^local = 12 and no
   lensing–ISW, with beam, noise and mask: all four estimators recover the
   input, errors "very close to the Fisher errors" (Fisher local: 5.8 T,
   26 E, 5.0 T+E) except Modal 1 E-only, which had too few maps in the
   linear term [src: Sect. 5.2, Table 8].
3. Component-separation pairs on data: for each of six method pairs and
   each shape, Δf_NL on data divided by σ_Δ, the scatter of the same
   difference over 160 foreground-free FFP10 simulations processed by each
   pipeline. Because six pairs are compared, the benchmark is the fraction
   of simulations in which any pair exceeds 1, 2 or 3σ_Δ (Table 17: about
   2/3, 13–19%, and 0–2.5%), and the maximum over simulations, 2.9–3.7.
   Data values up to about 3 are "not particularly unusual" [src:
   arXiv:1905.05697, Sect. 6.1.1, Tables 16–17].
4. Bispectrum-level consistency: mode-by-mode and bin-by-bin correlation of
   the reconstructed bispectra between cleaning methods [src: Sects. 6.1.2,
   6.6].
5. Noise mismatch: extra Gaussian noise with the data − simulation noise
   spectrum added to simulations while the estimator is calibrated on the
   originals; the map-by-map scatter has σ_Δ ≈ σ_fNL/10 and the errors do
   not change. The stated reason it cannot bias: "as long as the noise is
   Gaussian, noise mismatches of this kind cannot bias the estimators" [src:
   Sect. 6.2].
6. Mask: union of the 2018 and 2015 masks (f_sky = 0.72) and polarisation
   masks grown by 20 or 40 pixels, with differences judged against the
   scatter of 150 simulations analysed with both masks [src: Sect. 6.4,
   Tables 22–23].
7. ℓ_min and ℓ_max scans with the binned estimator: T stable by ℓ = 2000,
   E by ℓ = 1500, which justifies the lower ℓ_max of KSW and modal [src:
   Sect. 6.5].
8. Thermal dust and tSZ tests [src: Sect. 6.3, summarised in Sect. 6.6].

## Choices and what they cost

### Which estimator

| Estimator | Assumes | Buys | Costs | Used by |
|---|---|---|---|---|
| KSW / skew-C_ℓ | separable template | fastest; final Planck numbers; running via Schwinger trick | one template per run; no reconstruction | Planck 2013–2018 headline (KSW on SMICA) [src: arXiv:1905.05697, Sects. 3.1.1, 5.1 via L2] |
| Binned | smooth bispectrum in ℓ | shapes added without rerunning maps; ℓ dependence; binned reconstruction; contaminant-adjustable weights | binning loss (0.7% variance at 64 bins); misses rapid oscillations | Planck validation, mask and ℓ tests; PR4 reanalysis [src: arXiv:0911.1642, Table 2; arXiv:1905.05697, Sects. 3.1.4, 6.4–6.5; arXiv:2504.00884] |
| Modal | convergent polynomial expansion | any shape, including non-separable; scans of many models; smoothed reconstruction | convergence must be checked per shape; slower for squeezed and oscillatory shapes without extra modes | Planck Modal 1 (standard shapes, validation) and Modal 2 (oscillatory) [src: arXiv:1905.05697, Sect. 3.2.2] |
| Integrated bispectrum | squeezed limit only (patch scales ℓ ≤ 10) | simple; independent of the other codes | T only; local and lensing shapes only | PR4 reanalysis [src: arXiv:2504.00884, Sect. 2.3] |
| Learned separable basis | separable ansatz fits the shape | numerically computed (collider) shapes with KSW-level cost | must be checked against known shapes (99.8–99.9% cosines) | PR4 collider search [src: arXiv:2511.19179, Sect. V.3] |

When the four Planck estimators were run on the same simulations with
noise and mask, the differences to KSW for T+E local were −1.0 ± 1.7
(binned), −0.3 ± 1.7 (Modal 1) and −0.6 ± 1.3 (Modal 2), against σ(f_NL) ≈
5 [src: arXiv:1502.01592, Table 7]. Planck's reason for running several:
cross-validation, plus applications only some estimators allow —
reconstruction in different domains, characterisation of spurious
components, direction-dependent signals [src: arXiv:1905.05697, Sect.
3.1].

### Full inverse-covariance filter or diagonal approximation

The exact estimator needs C⁻¹ on the masked, anisotropic-noise sky;
Planck uses the diagonal C_ℓ⁻¹ after diffusive inpainting and states that
the errors stay near optimal [src: arXiv:1905.05697, Sect. 3.1]. The
inpainting (fill the mask with the mean, then replace each masked pixel by
the mean of its neighbours, 2000 iterations) is the same as in 2013 and
2015 [src: Sect. 3.2.2]. The PR4 reanalysis gives the reason in more
detail: inpainting removes the lack of small-scale power inside the mask
and the edge discontinuity, both of which "would bleed into the unmasked
region of the map during the filtering process in harmonic space" [src:
arXiv:2504.00884, Sect. 4]. PolySpec instead filters with the total
signal-plus-noise spectrum from half-mission maps, "matching the official
Planck analyses" [src: arXiv:2511.19179, Sect. V.3].

### Multipole range

- T to 2000 (KSW, modal) or 2500 (binned): no effect, since 2000 < ℓ ≤ 2500
  is noise-dominated [src: arXiv:1905.05697, Sect. 3.2.2].
- E from ℓ = 4: with ℓ = 2, 3 the simulations showed a small local bias,
  larger errors and larger inter-estimator discrepancies, attributed to
  non-Gaussian polarisation noise at very low ℓ; the cut was made "a
  priori, before looking at the data" [src: same]. In 2015 the polarisation
  ℓ_min was 40 [src: Sect. 6.5].
- Binned only: TEE configurations with the temperature mode in [2, 3] are
  removed because with them the errors are "much larger than the optimal
  Fisher errors"; why only this estimator needs it is "not clear" [src:
  Sect. 3.2.2].

### Which cleaned map

Planck 2018 keeps SMICA, citing its stability across releases and the
component-separation tests, with "a slight preference for SMICA and NILC";
it adds that this preference applies to non-Gaussianity only [src:
arXiv:1905.05697, Sects. 6.1.1, 6.6]. The PR4 reanalysis uses SEVEM, which
"removes the large NG contamination due to several galactic foregrounds",
and checks on 300 PR3 simulations that SEVEM and SMICA give the same
simulation averages to well within the errors [src: arXiv:2504.00884,
Sects. 4, 6]. So the PR3 and PR4 headline values in L2 come from different
cleaning methods as well as different estimators.

### Subtracting lensing with theory or with the simulation average

The PR4 simulations have a lensing amplitude below 1 (binned T+E 0.939 ±
0.009 over 600 maps), traced back to the input CMB simulations rather than
to NPIPE or SEVEM. Subtracting the averaged simulation bispectrum instead
of the theoretical lensing bias moves the PR4 binned T+E values to −0.6 ±
5.0 (local), 5 ± 46 (equilateral), −9 ± 21 (orthogonal), shifts an order
of magnitude below 1σ; random 100-map subsets show the local f_NL and its
error uncorrelated with the subset's lensing amplitude [src:
arXiv:2504.00884, Sect. 6, Tables "simulations" and "png2", figure on
local–ISW correlations]. The expected lensing bias on T-only local f_NL in
that set-up is 4.3 [src: same, figure caption].

## Numbers

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Brute-force scaling | ℓ_max⁵ | Planck 2018 | arXiv:1905.05697 | Sect. 3.1 |
| KSW scaling | N^(3/2) × ~100 radial points (full: N^(5/2)) | KSW | arXiv:astro-ph/0305189 | Sect. III.1 |
| Binning loss | cos²θ = 0.608, 0.846, 0.925, 0.974, 0.993 for 4, 8, 16, 32, 64 bins (ℓ_max = 2000) | Bucher et al. | arXiv:0911.1642 | Table 2 |
| Planck binning | 57 bins, 2 to 2500 | Planck 2015, 2018 | arXiv:1905.05697 | Sect. 3.2.2 |
| Modal bases | Modal 1: 600 polynomial + KSW radial modes; Modal 2: 2000 polynomial + SW local | Planck 2018 | arXiv:1905.05697 | Sect. 3.2.2 |
| Modal convergence | > 98% with 6 modes (primordial), 15 modes (CMB, ℓ_max = 500) | Fergusson et al. | arXiv:0912.5516 | Sect. III.4 |
| Inpainting | 2000 diffusive iterations | Planck 2013–2018, PR4 | arXiv:1905.05697 | Sect. 3.2.2 |
| Simulations | 300 FFP10 (160 modal); 600 PR4; 100 + 400 (PolySpec) | — | arXiv:1905.05697; arXiv:2504.00884; arXiv:2511.19179 | Sects. 3.2.2; 4; V.3 |
| Noise mismatch | 3% (T, ℓ ≈ 2000), ~1% (E); σ_Δ ≈ σ_fNL/10 | Planck 2018 | arXiv:1905.05697 | Sect. 6.2 |
| Estimator agreement | < 1/3 σ_fNL with noise and mask | Planck 2015 sims | arXiv:1502.01592 | Sect. 5.1 |
| Fisher errors, local | 5.8 (T), 26 (E), 5.0 (T+E) | Planck 2015 sims | arXiv:1502.01592 | Sect. 5.2 |
| Multiplicity benchmark | any pair > 3σ_Δ in 0–2.5% of sims; max 2.9–3.7 | Planck 2018 | arXiv:1905.05697 | Table 17 |
| Largest data discrepancy | SMICA − Commander, T-only orthogonal: Δ = −43, Δ/σ_Δ = −10.0 (≈ 1σ_fNL) | Planck 2018 | arXiv:1905.05697 | Table 16, Sect. 6.1.1 |
| Mask test | union mask f_sky = 0.72: equilateral T shift −49 ± 24 (≈ 2/3 σ_fNL); 13.3% of sims have a > 2σ_Δ shift | Planck 2018 | arXiv:1905.05697 | Sect. 6.4, Table 22 |
| PR4 simulation means (binned T+E) | local 0.02 ± 0.20, equil 1.1 ± 1.9, ortho 1.0 ± 0.9, lensing 0.939 ± 0.009 | PR4 | arXiv:2504.00884 | Sect. 6, table of simulation averages |
| Integrated-bispectrum patches | w_ℓ = 1 for ℓ ≤ 10 | PR4 | arXiv:2504.00884 | Sect. 2.3 |

## What goes wrong

- **Unsubtracted lensing–ISW.** Biases local f_NL by about 5 (L2). Test:
  detect the lensing amplitude in the same run and check it against 1; the
  PR4 simulations themselves miss it by 6–10% (above), so check the data
  with both theory and simulation-average subtraction.
- **Linear term from too few or mismatched simulations.** Shows up as
  errors above Fisher: Modal 1 E-only in 2015 [src: arXiv:1502.01592, Sect.
  5.2]. Test: compare simulation errors with Fisher errors; repeat with
  random subsets of simulations, as PR4 does with 100-map subsets [src:
  arXiv:2504.00884, Sect. 6].
- **Non-Gaussian low-ℓ polarisation noise.** Biases local f_NL in
  simulations when E at ℓ = 2, 3 is kept [src: arXiv:1905.05697, Sect.
  3.2.2]. Test: ℓ_min scan on simulations before unblinding.
- **Foreground residuals in one cleaned map.** Shows up as a pair
  difference larger than its simulation scatter; judge it against the
  multiplicity-corrected benchmark, not against 1σ [src: Sect. 6.1.1].
- **Simulation noise model mismatch.** Cannot bias a cubic statistic with
  Gaussian noise but can degrade the linear term; test by injecting the
  noise difference [src: Sect. 6.2].
- **Template mis-specification for non-separable shapes.** Test: cosine
  between the separable approximation and the target including mask, beam
  and noise (PolySpec reports 99.8–99.9% for known shapes) [src:
  arXiv:2511.19179, Sect. V.3]; for modal, the convergence correlation of
  the partial sum [src: arXiv:0912.5516, Sect. III.4].
- **Treating shapes as independent when they correlate.** Local, equi-
  lateral and orthogonal templates overlap, so an injected local signal
  leaks into the others in single-shape fits [src: arXiv:1502.01592, Sect.
  5.2]; quote whether values are single-shape or joint.
- **Running f_NL pivot.** A flat prior on f*_NL at one pivot is not flat at
  another, and without a detection the fit can favour particular n_NG [src:
  arXiv:1905.05697, Sect. 3.1.2].

## Reading list

- Foundation: Komatsu, Spergel and Wandelt 2005, arXiv:astro-ph/0305189 —
  the A and B filtered maps and the fast cubic statistic (Eqs. 6–14).
- Method: Bucher et al. 2010, arXiv:0911.1642 — inner
  product, cos²θ loss, binning (Eqs. 21–34, Table 2).
- Method: Fergusson et al. 2010, arXiv:0912.5516 — modal
  expansion and its convergence (Sect. III.4).
- Application: Planck 2015 XVII, arXiv:1502.01592 — estimator agreement
  and unbiasedness tests (Sects. 5.1–5.2, Tables 5–8).
- Application: Planck 2018 IX, arXiv:1905.05697 — estimators (Sect. 3.1),
  settings (Sect. 3.2.2), validation suite (Sect. 6).
- Application: Jung et al. 2025, arXiv:2504.00884 — PR4 with binned and
  integrated estimators, joint-fit and bias formulae (Sect. 3.2), the low
  lensing amplitude in simulations (Sect. 6).
- Method and test: Philcox, Zhong and Sirletti 2025, arXiv:2511.19179 —
  learned separable basis, PolySpec estimator (Eqs. 23–29), validation
  against standard templates on PR4.

## Not verified

- The definition of the KSW filter α_ℓ(r) (Sect. II of
  arXiv:astro-ph/0305189) was not copied; only β_ℓ(r) was read.
- Bucher et al. 2016 (the full binned-estimator paper cited by Planck),
  Fergusson 2014 (the Modal 2 T/E orthogonalisation), Shiraishi et al.
  2019 (Modal 1 polarisation), Smith et al. 2009 and Elsner & Wandelt 2012
  (full C⁻¹ filtering), Munshi & Heavens 2010 (skew-C_ℓ) and Becker &
  Huterer 2012 (running likelihood): cited inside Planck 2018 IX, not read.
- The PR4 reanalysis was read from its LaTeX source, which carries no
  equation numbers; places are given by section. Its multipole ranges and
  the number of simulations used for its linear term were not read.
- SO bispectrum forecasts (arXiv:1808.07445, Sect. VI): not read.
