# Two-point statistics and estimators — cosmo-weak-lensing dossier

Scope: how ξ±, COSEBIs, band powers and pseudo-Cℓ are measured and
predicted in practice (fine binning, bin averaging, weight functions,
mode coupling, noise bias, binning schemes), how scale cuts are set in each
statistic and carried from one to another, and how large a difference
between two statistics on the same catalogue is expected and how that
expectation is computed.
Snapshot: 2026-10-18.
From: Pantos 2026 review (arXiv:2602.12238), Sect. 4.1; KiDS-Legacy key
papers (arXiv:2503.19441, arXiv:2503.19442); HSC Y3 real- and
harmonic-space pair (arXiv:2304.00702, arXiv:2304.00701).

Already in L2, not repeated here: the table of statistics with their
reference papers, the KiDS-Legacy definitions of E_n and C_E,l and its
reason for keeping ξ± out of the primary analysis, the HSC real-space E/B
split, the BNT transform (`physics-and-methods.md#two-point-statistics`);
the estimators with m or ⟨R⟩ (`physics-and-methods.md#estimators`); the
statistic, scale range and covariance of each main analysis
(`physics-and-methods.md#what-each-main-analysis-did`); the B-mode tests of
each survey with their PTEs (`systematics.md#psf-modelling-and-leakage`);
the HSC Y1 Cℓ/ξ± and UNIONS Cℓ/ξ± values
(`results.md#history-of-the-key-numbers`). How baryon contamination sets
small-scale cuts is treated in `deep/baryonic-feedback.md`; this dossier
takes the cuts from the statistic's side.

Symbols. ξ±(θ): shear correlation functions at separation θ; C_EE, C_BB:
E- and B-mode angular power spectra; E_n, B_n: COSEBI modes n = 1, 2, …
over [θ_min, θ_max]; T±n(θ): COSEBI filters; W_n(ℓ): their Hankel
transforms; C_E,l: band power l over [ℓ_lo,l, ℓ_up,l]; T(θ): apodised
selection function of the band powers (unrelated to T±n); g±^l: band-power
filters; M_ℓℓ': mode-coupling matrix of a mask; L: a multipole bin (band)
with weights ω_L^ℓ; F_Lℓ: band-power window; N_L: shape-noise bias;
k_{>α}(ℓ): wavenumber below which a fraction α of C_ℓ accumulates; σ(ΔS8):
scatter of the difference of S8 point estimates between two statistics
measured on the same noise realisation.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Measure ξ± finely, whatever statistic is fitted
<!-- key: step-1-measure-xi-finely-whatever-statistic-is -->

COSEBIs and band powers are linear transforms of ξ±, so every KiDS
statistic starts from finely binned ξ±. KiDS-1000 needed a million linear θ
bins for COSEBIs in KV450 and reached the same accuracy, better than
0.03%, with 4000 logarithmic bins once it adopted log-COSEBIs; band powers
need 300 log bins over 0.5′–300′, "extended on either side to allow for the
apodisation", for better than per-cent accuracy (Asgari et al. 2020,
arXiv:2007.15633) [src: Sects. 2.2–2.3]. KiDS-Legacy measures 1000 log bins
over 2′–300′ with TreeCorr 4.2.3 and bin_slop = 1.5, the galaxy weights
being the recalibrated shape weights times the redshift "gold" weights
(Wright et al. 2025, arXiv:2503.19441) [src: Sect. 2.5.1]. The range
0.5′–300′ in KiDS-1000 was set "based on the extent of the survey and its
resolution" [src: arXiv:2007.15633, Sect. 2.4].

### Step 2. Predict ξ± over the measured bin, not at a point
<!-- key: step-2-predict-xi-over-the-measured-bin-not-at -->

KiDS-1000 does not evaluate ξ± at an effective θ, since "this
approximation can result in biases": the theory is integrated over each
bin weighted by the number of pairs N_pair measured on the data, which
"includes all survey effects" [src: arXiv:2007.15633, Sect. 2.1]. DES Y3
uses the full-sky form ξ±^{ij}(θ) = Σ_ℓ (2ℓ+1)/(2π ℓ²(ℓ+1)²) [G⁺_{ℓ,2}(cos θ)
± G⁻_{ℓ,2}(cos θ)] [C_EE ± C_BB], the G functions built from Legendre
polynomials and averaged over angular bins (Secco et al. 2021,
arXiv:2105.13544) [src: Eq. 11]. KiDS-Legacy writes the flat-sky Hankel
form [src: arXiv:2503.19441, Eq. 15]. Writing ξ± as ∫ d ln k 𝒫(k) (Eqs.
12–13 of arXiv:2105.13544) shows which k each angle receives; after the DES
Y3 cuts, at about 2.5′ in ξ+ and 30′ in ξ−, "only a relatively small
contribution" comes from k > 1 h/Mpc [src: Fig. 4 caption].

### Step 3. COSEBIs
<!-- key: step-3-cosebis -->

E_n = ½ ∫_{θmin}^{θmax} dθ θ [T+n ξ+ + T−n ξ−], B_n with the minus sign
(arXiv:2007.15633) [src: Eq. 7]; predicted as E_n = ∫ dℓ ℓ/(2π) C_EE W_n
with W_n = ∫ dθ θ T+n J0(ℓθ) = ∫ dθ θ T−n J4(ℓθ) [src: Eqs. 8–9]. Two
families exist, linear and logarithmic; the filter of mode n has n + 1
roots; KiDS uses log-COSEBIs because "the first few n-modes are sufficient
to essentially capture the full cosmological information" [src: Sect.
2.2]. Number of modes: five in KiDS-1000; six in KiDS-Legacy because, "with
our increased constraining power, and larger redshift baseline", mode 6
improves S8, while modes 7–20 return identical constraints; W_n makes the
integrand "practically zero outside 10 ≲ ℓ ≲ 10³", so the ℓ integral can
be truncated (arXiv:2503.19441) [src: Sect. 2.5.2, Eqs. 16–18]. The
covariance follows Asgari et al. 2020 with updated N_pair and σ_ε, plus the
in-survey non-Gaussian term, negligible in effect (arXiv:2007.15633) [src:
Sect. 2.2].

### Step 4. Band powers
<!-- key: step-4-band-powers -->

C_E/B,l = (π/𝒩_l) ∫ dθ θ T(θ) [ξ+ g+^l ± ξ− g−^l], with 𝒩_l = ln ℓ_up,l
− ln ℓ_lo,l so that the band traces ℓ²C(ℓ) at its logarithmic centre
(arXiv:2007.15633) [src: Eqs. 10–11]. The θ integral must be truncated, so
a top hat in ℓ is impossible; the apodisation in T(θ) softens the edges to
"reduce the ringing" [src: Sect. 2.3]. The prediction uses windows W^l_EE
= W^l_BB and W^l_EB = W^l_BE built from T, g±, J0 and J4 [src: Eqs.
12–13]; they "are no longer top hat functions", and the cross windows make
E and B leak into each other. KiDS uses eight log bands over 100 ≤ ℓ ≤ 1500
[src: Sect. 2.3]; KiDS-Legacy keeps them and changes the edge treatment of
T(θ), so that its windows "initially go to zero within their desired ℓ
ranges" (arXiv:2503.19441) [src: Sect. 2.5.3, Fig. 1 caption]. The mixing
grows for narrower bands and for a smaller θ range [src: Sect. 2.5.3].

### Step 5. Pseudo-Cℓ
<!-- key: step-5-pseudo-cell -->

The masked spin-2 field has ⟨C̃_ℓ⟩ = Σ_ℓ' M_ℓℓ' C_ℓ' including E↔B
leakage; the binned estimator inverts the binned coupling matrix,
Ĉ_L = Σ_L' (M⁻¹)_LL' C̃_L', and the data must be compared with Σ_ℓ F_Lℓ C_ℓ,
F_Lℓ = Σ_L' (M⁻¹)_LL' Σ_{ℓ'∈L'} ω^{ℓ'}_{L'} M_ℓ'ℓ, because masking, binning
and decoupling "are generally not permutable" (Doux et al. 2022,
arXiv:2203.07128) [src: Eqs. 10–15]. Choices made by the two pseudo-Cℓ
analyses read here:

- **Maps.** DES Y3: HEALPix N_side = 1024, ellipticities corrected first
  (mean subtracted, divided by the response), weighted galaxy counts as the
  mask, "a close approximation to inverse-variance masks" [src: Sect. 3.1].
  HSC Y3: six fields mapped separately in the flat-sky approximation, 1′ ×
  1′ Plate Carrée pixels with the projection centred on each field (33–120
  deg²), spectra co-added with inverse-variance weights (Dalal et al. 2023,
  arXiv:2304.00701) [src: Sects. III, IV.1].
- **Binning.** DES Y3: 32 square-root-spaced bins over 8 ≤ ℓ ≤ 2048, as a
  balance between linear bins (too coarse at high ℓ) and logarithmic ones
  (too coarse at low ℓ) [src: arXiv:2203.07128, Sect. 3.1]. HSC Y3: 17
  bins over 100–15800, roughly logarithmic with linear spacing at low ℓ;
  spectra and coupling matrices are computed to high ℓ "to correctly
  account for mode coupling between smaller scale modes and those we use"
  [src: arXiv:2304.00701, Sects. III, IV.1].
- **Noise bias.** Subtracted from auto-spectra only, estimated analytically
  as Ñ_L = Ω_pix ⟨Σ_{i∈p} w_i² (e₁² + e₂²)/2⟩_p, the average running over
  all pixels including empty ones outside the footprint
  (arXiv:2203.07128) [src: Eq. 16]; it agrees with the mean over random
  rotations of the galaxies and is preferred for being noiseless [src:
  Sect. 3.1]; HSC quotes agreement to about 3% for its ℓ range
  (arXiv:2304.00701) [src: Eq. 20, Sect. III].
- **No E/B purification**, because the B-mode signal is subdominant and
  purification would need an apodised mask, which on a mask "speckled with
  empty pixels" would "significantly decrease the effective survey area"
  (arXiv:2203.07128) [src: Sect. 3.1].
- The windows F_Lℓ "extend beyond the top-hat ones, with some negative
  terms, especially for small multipoles below ℓ ≲ 200" [src:
  arXiv:2203.07128, Sect. 3.1].

### Step 6. Set the scale cuts in each statistic
<!-- key: step-6-set-the-scale-cuts-in-each-statistic -->

- **Δχ² per bin pair (DES Y3 harmonic).** Compare a Halofit vector with
  one rescaled by the OWLS-AGN suppression; keep multipoles while each of
  the 10 bin pairs has Δχ²_ab < Δχ²/N_pair with Δχ² = 1 (equivalently a
  global Δχ² ≈ 0.34, the pairs being correlated), validated by requiring
  the fiducial maximum posterior to lie inside the 2D region of the
  contaminated posterior: 119 of 320 points; with shear ratios, Δχ² = 0.5,
  102 points; ℓ_max falls between about 200 and 400 except bin 1–1
  (arXiv:2203.07128) [src: Sect. 3.5.1]. The paper notes that HSC Y1 and
  KiDS-450 used redshift-independent ℓ_max = 1900 and 1300 [src].
- **k_max cut.** Find ℓ_max where k_{>α}(ℓ) = k_max, with ∫^{ln k_{>α}}
  d ln k |d ln X / d ln k| = α, α = 0.95, X = C_ℓ, ξ+ or ξ−; the absolute
  value matters for ξ+, which receives negative contributions (Doux et al.
  2020, arXiv:2011.06469) [src: Sect. 3, Eq. 17]; k_max from 1 to 5 h/Mpc,
  5 being where Halofit errors exceed 10% [src: Sect. 3]; one k_max for
  all pairs, "in practice limited by the low redshift bin"
  (arXiv:2203.07128) [src: Sect. 3.5.2, Eq. 28].
- **Model-sufficiency in the S8–Ωm plane (HSC Y3 harmonic).** Require
  √(d Σ⁻¹ dᵀ) < 0.3 for d = (ΔS8, ΔΩm) of the MAP on contaminated noiseless
  vectors, with Σ the posterior covariance of the fiducial data run; the
  MAP is taken as the best of 50 Powell minimisations from different
  starting points (about 20 suffice), to separate model bias from
  projection effects (arXiv:2304.00701) [src: Sect. V.2.1, Eq. 35].
  Large scales: ℓ < 300 is cut for excess B modes [src: Sect. IV.1].
- **Conversion between spaces.** ℓ ≈ π/θ with the geometric mean of the
  ξ+ and ξ− cuts, ℓ_max = π/√(θ⁺_min θ⁻_min), "preserves signal-to-noise"
  better than either alone (arXiv:2011.06469) [src: Sect. 3]; it is the
  conversion that correlates worst (next section). KiDS-1000 keeps its
  ξ− cut at 4′ and uses the full 0.5′–300′ range for COSEBIs and band
  powers (arXiv:2007.15633) [src: Sect. 2.4].

### Step 7. Compute the expected difference before comparing statistics
<!-- key: step-7-compute-the-expected-difference-before -->

KiDS-1000 builds the cross-covariance of COSEBIs, band powers and ξ± from
the Salmo simulations, draws 100 joint noise realisations around a theory
vector, runs the full pipeline on each statistic, and compares the
distribution of ΔS8 with the mean posterior width (arXiv:2007.15633) [src:
App. B.1]. DES uses importance sampling on Gaussian mocks of a DES Y3-like
survey (arXiv:2011.06469) [src: Sects. 5–6]. UNIONS runs both pipelines on
350 GLASS lognormal mocks (Guerrini et al. 2026, arXiv:2605.13543) [src:
Sect. 5.3]. The test statistic is the fraction of mocks with |ΔS8| above
the observed one.

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

| Statistic | Assumes | Buys | Costs | Used by |
|---|---|---|---|---|
| ξ± | none beyond the estimator | simplest; no mask correction; in KiDS-1000 mocks the smallest bias of the marginal S8 but also the tightest distribution, so a similar bias relative to its width [src: arXiv:2007.15633, App. B.1] | E/B mixed; substantial sensitivity to ℓ > 1500; ξ+ reaches ℓ < 10, where the large-θ ξ± distribution "deviates from a Gaussian" in Salmo mocks [src: arXiv:2007.15633, Sect. 2.4] | DES, HSC, UNIONS |
| COSEBIs (log) | finite [θ_min, θ_max] defines the modes | exact E/B split within the range; 5–6 numbers per pair; Gaussian-like distribution [src: Sect. 2.4] | fine ξ± binning; the S8 exponent 0.5 is "not perpendicular" to the COSEBI degeneracy, widening its S8 distribution [src: App. B.1] | KiDS-1000, KiDS-Legacy |
| Band powers | apodisation acceptable | control of the ℓ range | E/B leakage; widest S8 distribution of the three in KiDS-1000 mocks [src: App. B.1] | KiDS-1000, KiDS-Legacy |
| Pseudo-Cℓ | mask coupling computed exactly; flat sky per field (HSC) | direct link to the theory spectrum; cuts in ℓ | noise-bias subtraction; window functions with negative lobes; no purification | HSC Y3, DES Y3, UNIONS, KiDS-Legacy BNT |

What comparisons on one catalogue found:

- **KiDS-1000, three statistics.** ΔS8 between any two is "only 20–30%
  tighter than" the mean single-statistic width, so "we do not expect to
  find perfect agreement"; the observed 0.4σ between COSEBIs and ξ± is
  expected. The cross-correlation is largest between ξ− and band powers or
  COSEBIs; small-scale ξ± is unused by the others (arXiv:2007.15633) [src:
  App. B.1].
- **DES Y3-like mocks, Cℓ against ξ±.** σ(ΔS8) and the Pearson correlation
  r of the posterior means depend on how the cuts are matched: no cuts
  0.006, r = 0.79; ℓ ≈ π/θ 0.011, r = 0.68; k_max = 3 h/Mpc 0.008, r =
  0.83; baryon χ² 0.014, r = 0.66; with the published HSC Y1 cuts r is about
  10% (arXiv:2011.06469) [src: Table 3, Sects. 6.1, 6.3]. For k_max from 5
  down to 1 h/Mpc, σ(ΔS8) grows from 0.0049 to 0.019 and r falls from 89% to
  56% [src: Sect. 6.1]. All systematics tested push the harmonic σ8 higher
  than the real-space one, but by less than the observed HSC and KiDS-450
  differences [src: Sect. 6.3].
- **DES Y3 data.** Cℓ gives S8 higher by ΔS8 = 0.031 without shear ratios
  and 0.025 with them, against an expected σ(ΔS8) ≈ 0.02; best-constrained
  exponents α = 0.595 (Cℓ) and 0.552 (ξ±), 0.598 and 0.586 with shear
  ratios (arXiv:2203.07128) [src: Sect. 6.4].
- **UNIONS-3500, non-tomographic.** 0.60σ if the two results are treated
  as independent; 2.18σ (p = 1.5 × 10⁻², ±0.2σ from mock counting) once
  their correlation is estimated on 350 mocks; the harmonic result is
  insensitive to its cuts, the configuration-space S8 rises to the
  harmonic value when scales down to 5′ are included, and localised B
  modes in configuration space are the stated candidate
  (arXiv:2605.13543) [src: Sect. 5.3].
- **HSC Y3.** With "coordinated analysis choices" the two papers report
  "excellent agreement" (arXiv:2304.00701) [src: Sect. VI.1].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| ξ± fine binning for COSEBIs | 4000 log bins, < 0.03% accuracy (formerly 10⁶ linear bins) | KiDS-1000 | arXiv:2007.15633 | Sect. 2.2 |
| ξ± fine binning for band powers | 300 log bins over 0.5′–300′, extended for apodisation | KiDS-1000 | arXiv:2007.15633 | Sect. 2.3 |
| ξ± fine binning | 1000 log bins, 2′–300′, TreeCorr bin_slop 1.5 | KiDS-Legacy | arXiv:2503.19441 | Sect. 2.5.1 |
| COSEBI modes | 5 (KiDS-1000); 6, with 7–20 adding nothing (KiDS-Legacy) | KiDS | arXiv:2007.15633; arXiv:2503.19441 | Sect. 2.2; Sect. 2.5.2 |
| COSEBI ℓ support | 10 ≲ ℓ ≲ 10³ | KiDS-Legacy | arXiv:2503.19441 | Sect. 2.5.2 |
| ξ± ℓ support | ξ+ 1 ≲ ℓ ≲ 10⁴; ξ− 10 ≲ ℓ ≲ 10⁵ | KiDS-Legacy | arXiv:2503.19441 | Sect. 2.5.1 |
| Band powers | 8 log bands, 100–1500 | KiDS-1000, KiDS-Legacy | arXiv:2007.15633 | Sect. 2.3 |
| Pseudo-Cℓ binning | 32 √ℓ-spaced bins, 8–2048, N_side 1024 (pixel ≈ 11.8 arcmin²) | DES Y3 | arXiv:2203.07128 | Sect. 3.1 |
| Pseudo-Cℓ binning | 17 bins, 100–15800; used 300 < ℓ < 1800 (6 bins); S/N 26.4 | HSC Y3 | arXiv:2304.00701 | Sects. III, IV.1 |
| DES Y3 harmonic cuts | 119 / 320 points (Δχ² = 1); 102 with shear ratios (Δχ² = 0.5) | DES Y3 | arXiv:2203.07128 | Sect. 3.5.1 |
| k_max cut | α = 0.95, k_max 1–5 h/Mpc; ℓ_max ≈ 1600 for bin 4 at k_max = 5 | DES Y3 | arXiv:2203.07128 | Sect. 3.5.2 |
| Model-sufficiency threshold | 0.3σ_2D on the MAP; cosmo-OWLS fails (0.57σ_2D) at ℓ_max = 1800 | HSC Y3 | arXiv:2304.00701 | Sect. V.2.1, Tables 2–3 |
| Expected ΔS8 between statistics | 20–30% below the mean σ(S8) | KiDS-1000 | arXiv:2007.15633 | App. B.1 |
| σ(ΔS8), Cℓ vs ξ± | 0.006–0.014 by cut choice; r 0.66–0.83 (≈ 0.10 with HSC Y1 cuts) | DES Y3-like mocks | arXiv:2011.06469 | Table 3, Sect. 6.3 |
| Observed ΔS8, Cℓ − ξ± | 0.031 (0.025 with shear ratios) | DES Y3 | arXiv:2203.07128 | Sect. 6.4 |
| Observed ΔS8, config − harmonic | 0.06; 2.18σ with correlation, 0.60σ without | UNIONS-3500 | arXiv:2605.13543 | Sect. 5.3 |
| Harmonic-space goodness of fit | χ² = 55.38 against 50 noisy mocks, p = 0.42 | HSC Y3 | arXiv:2304.00701 | Sect. VI.1 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Comparing two statistics as if independent.** UNIONS shows the size of
  the error: 0.60σ naive against 2.18σ with the correlation from mocks
  (arXiv:2605.13543) [src: Sect. 5.3]. Test: joint mocks, both pipelines,
  distribution of ΔS8.
- **Mismatched cuts inflate the scatter.** With HSC Y1 cuts the two
  statistics correlate at about 10% on DES Y3-like mocks, so differences
  of 0.5–1σ like those of HSC Y1 and KiDS-450 are not anomalous
  (arXiv:2011.06469) [src: Sect. 6.3]. Test: match cuts by k_max before
  comparing.
- **Point estimates near a prior edge.** In KiDS-1000 the ξ± contour sits
  along the degeneracy at high σ8 and low Ωm, touching the prior; many of
  the 100 mocks do the same for one statistic or another, and a contour cut
  by a hard prior "will appear as a tighter constraint", as for A_bary with
  band powers (arXiv:2007.15633) [src: App. B.1]. Test: mocks with the same
  priors.
- **Effective-θ theory.** Evaluating ξ± at a bin centre instead of
  integrating with N_pair can bias the fit (arXiv:2007.15633) [src: Sect.
  2.1].
- **ξ+ at large θ non-Gaussian.** Visible in the Salmo distribution of
  ξ±(θ); in KiDS-1000 the affected bins had a negligible effect, tested by
  a reduced range [src: arXiv:2007.15633, Sect. 2.4].
- **A cut that passes for one simulation fails for another.** HSC Y3
  passes OWLS-AGN, Illustris, Horizon-AGN, EAGLE and EuclidEmulator but not
  cosmo-OWLS, and its dark-matter-only CosmicEmu test is worse at ℓ_max =
  1800 than at 2200, attributed to large-scale differences between HMCode
  and CosmicEmu (arXiv:2304.00701) [src: Sect. V.2.1, Table 3].
- **Mask-related noise-bias errors.** The analytic Ñ_L assumes the average
  over all pixels of the map, empty ones included; the random-rotation
  estimate is the cross-check (arXiv:2203.07128) [src: Sect. 3.1].
- **B modes localised in one space.** The UNIONS candidate for its
  configuration–harmonic difference; B-mode tests must therefore pass in
  each statistic used (`systematics.md#psf-modelling-and-leakage`).

## Reading list
<!-- key: reading-list -->

- Foundation: Schneider et al. 2010, arXiv:1002.2136 — COSEBIs (cited here
  through the KiDS papers).
- Method: Asgari et al. 2020, arXiv:2007.15633 — the three statistics on
  one catalogue, fine binning, the expected ΔS8 from joint mocks (App. B.1).
- Method: Doux et al. 2020, arXiv:2011.06469 — how to match scale cuts in
  ℓ and θ, and σ(ΔS8) for each matching.
- Method: Doux et al. 2022, arXiv:2203.07128 — pseudo-Cℓ pipeline choices
  (binning, noise, no purification) and harmonic cuts for DES Y3.
- Application: Dalal et al. 2023, arXiv:2304.00701 — field-by-field
  flat-sky pseudo-Cℓ and the MAP-based model-sufficiency test.
- Application: Wright et al. 2025, arXiv:2503.19441 — KiDS-Legacy COSEBIs
  (six modes) and band powers with the new T(θ) edges.
- Application: Secco et al. 2021, arXiv:2105.13544 — curved-sky,
  bin-averaged ξ± model and its k sensitivity.
- Critique: Guerrini et al. 2026, arXiv:2605.13543 — a 2.18σ
  configuration–harmonic difference once correlations are counted.

## Not verified
<!-- key: not-verified -->

- Joachimi et al. 2021 (arXiv:2007.01844) Eqs. 22–23 for T(θ) and g±^l,
  and Appendix C of arXiv:2503.19441 for the new band-power edges: not
  read.
- Louca & Sellentin 2020 on the Gaussianity of the COSEBI likelihood,
  Asgari & Schneider 2015 on band-power leakage, Nicola et al. 2021 on
  pseudo-Cℓ for HSC: cited through the papers above, not read.
- The DES Y1 harmonic-space compatibility study (Camacho et al. 2021) was
  seen only in a search listing; its numbers are not used.
- Whether the UNIONS 2.18σ uses the posterior mean or another point
  estimate.
