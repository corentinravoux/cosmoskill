# Baryonic-feedback mitigation — cosmo-weak-lensing dossier

Scope: how a cosmic-shear analysis protects S8 from baryonic suppression of
the matter power spectrum (validated scale cuts, a halo-model feedback
parameter, baryonification emulators, a phenomenological amplitude, choice
of statistic, k-space nulling), how each is set up step by step, and how to
choose between them.
Snapshot: 2026-10-17.
From: Pantos 2026 review (arXiv:2602.12238), Sects. 4.1.1 and 7.4; DES Y6
analysis framework (arXiv:2601.14859), Sects. III.1 and VI.

Already in L2, not repeated here: the feedback model, prior, scale-cut rule
and S8 shift of each main analysis, the external gas-probe results and the
"non-linear solution" debate (`systematics.md#baryonic-feedback`); the
feedback-parameter conventions (`physics-and-methods.md#conventions-that-split-the-community`);
the per-analysis method table (`physics-and-methods.md#what-each-main-analysis-did`);
baryon results (`results.md`).

Symbols. P_m(k, z): matter power spectrum; P_hydro/P_DM: ratio of a
hydrodynamical to a dark-matter-only spectrum, applied as a response; S(k):
the same ratio from a baryonification model; T_AGN: sub-grid AGN heating
temperature of BAHAMAS, the single HMcode-2020 feedback parameter, written
Θ_AGN = log₁₀(T_AGN/K) by DES; M_c: halo mass below which haloes have lost
half their gas (baryonification); f_b = Ω_b/Ω_m; σ_2D: a shift expressed in
units of the 2D (Ω_m, S8) posterior width; Δχ²: χ² difference between a
contaminated and a baseline synthetic data vector over the covariance.

## How it is done
<!-- key: how-it-is-done -->

### Route A. Scale cuts validated on contaminated synthetic data
<!-- key: route-a-scale-cuts-validated-on-contaminated -->

The DES procedure, as written for Y3 and refined for Y6:

1. **Choose the contamination that brackets reality.** DES Y3 used one
   pessimistic case, OWLS-AGN, judged "an adequate upper limit": more extreme
   than BAHAMAS but below Illustris, which "is known be too extreme in its
   radio-mode AGN feedback, and underpredicts the amount of baryons in galaxy
   groups" (arXiv:2105.13548, Sect. V.1.1) [src]. DES Y6 brackets from both
   sides: gravity-only (EuclidEmulator2) and BAHAMAS-8.0 ("hi AGN"), each
   applied to the EuclidEmulator2 spectrum as
   P_m = (P_hydro/P_DM) P_m^Eemu (arXiv:2601.14859, Eq. 14) [src: Sect.
   III.1]. The reason for the two-sided bracket: the fiducial model already
   contains moderate feedback, and the suppression is asymmetric [src:
   Sect. III.1].
2. **Translate a Δχ² threshold into θ_min per bin pair.** Y3: choose
   Δχ²_thr and set θ_min,± for each of the 20 shear functions so that each
   carries less than Δχ²_thr/20 (arXiv:2105.13548, Sect. V.1.3) [src]. Y6:
   θ_min per pair such that max[χ²(base, max), χ²(base, min)] < Δχ²
   (arXiv:2601.14859, Eq. 31) [src: Sect. VI.1].
3. **Run chains on the contaminated vectors and iterate.** Y6 explores Δχ²
   in [0.1, 5] and accepts the largest value giving ΔS8 < 0.5σ; the
   validation of cosmic-shear and 2×2pt cuts cost 1.75 million CPU-hours
   [src: arXiv:2601.14859, Sect. VI.1, Fig. 7 caption]. Y3 adopted
   (R_min,w, R_min,γt, Δχ²_thr) = (8 Mpc/h, 6 Mpc/h, 0.5) (Eq. 39) [src:
   Sect. V.1.3 of arXiv:2105.13548].
4. **Set the threshold from a budget.** Y6: the sum of all systematics must
   stay below 1σ; a minor systematic gets 0.3σ, so that ten in quadrature
   give at most 1σ; a major or coupled one (baryons with non-linear growth)
   gets 0.5σ [src: arXiv:2601.14859, Sect. VI.2]. For cosmic shear the
   metric is the shift of the marginal mean of S8, found more stringent than
   the 2D shift [src: Sect. VI.2].
5. **Re-derive the cuts per model setup.** DES Y6 derived separate cuts for
   NLA and TATT, "since this procedure is sensitive to the uncertainty of our
   constraints on S8": 178 + 89 points for NLA, 183 + 99 for TATT, of 400
   [src: arXiv:2602.10065, Sect. IV.3]. DES Y3 instead imposed one set of
   cuts on all probe combinations and models "to enable model comparisons
   based on the same data points" [src: arXiv:2105.13548, Sect. V.1.3].

Why not a theory-error covariance instead: it requires a model of the
distribution of the model error, "much more difficult to validate than the
choice of one pessimistic contamination realization" [src: arXiv:2105.13548,
Sect. V.1].

Why DES Y6 fixed Θ_AGN = 7.7 inside the cut data: once the
feedback-sensitive scales are removed the data do not constrain it; sampling
it would add a poorly constrained parameter, enhance projection effects, and
make the prior feed back into the scale-cut definition [src:
arXiv:2601.14859, Sect. III.1]. Why HMcode-2020 over the alternatives:
EuclidEmulator2 is sub-per-cent accurate but calibrated on a parameter space
narrower than DES Y6 needs; Halofit deviates by 5–10% on non-linear scales
and has no baryonic extension [src: Sect. III.1].

### Route B. A halo-model feedback parameter (HMcode-2020)
<!-- key: route-b-a-halo-model-feedback-parameter-hmcode -->

The six-parameter model modifies the halo model three ways [src: Mead et
al. 2020, arXiv:2009.01858, Sect. 6.1]: a lower concentration through B
(gravity-only B = 4); a central stellar term f_* (0 < f_* < Ω_b/Ω_m); and
gas expulsion,
f_g(M) = (Ω_b/Ω_m − f_*) (M/M_b)^β / [1 + (M/M_b)^β] (Eq. 24), haloes below
M_b having lost more than half their gas; the NFW window becomes
W̃ = [Ω_c/Ω_m + f_g(M)] W + f_* M/ρ̄ (Eq. 25). Gravity-only is recovered for
B → 4, M_b → 0, f_* → 0 [src: Sect. 6.4].

The single-parameter model fits all six linearly in θ = log₁₀(T_AGN/10^7.8 K)
to three BAHAMAS runs (7.6, 7.8, 8.0), with β = 2 fixed (Table 5); it
follows the simulated response to "within a couple of per cent" [src: Sect.
6.3]. Two facts a practitioner must hold [src: Sects. 6.3–6.4]:

- It "has no limit in which the 'gravity only' result is recovered".
- The recommended prior is 7.6 < log₁₀T_AGN < 8.0 (the BAHAMAS range that
  reproduces observed halo gas fractions), or 7.6–8.3 to include cosmo-OWLS;
  cosmo-OWLS AGN 8.7 is matched by an effective 8.3.

The priors analyses use extend beyond the fitted range: KiDS-Legacy
[7.3, 8.3] (L2), described in its model section as T_AGN ∈ [7.1, 8.3]
(arXiv:2503.19441, Sect. 2.3) [src]; DES Y6 free-Θ_AGN variant [7.2, 9.0]
(L2). KiDS-Legacy reads 7.3 as "consistent with dark-matter only" [src:
Sect. 5.2.7]; that is an extrapolation of the BAHAMAS fit, since the model
paper states that no value recovers gravity-only. KiDS-Legacy's reason for
not using the alternatives (FLAMINGO emulators, SP(k), baryonification):
they "were published over the course of the analysis" or were not
implemented in its CosmoSIS framework [src: Sect. 2.3].

### Route C. Baryonification emulators
<!-- key: route-c-baryonification-emulators -->

Foundation: displace particles of a dark-matter-only simulation so that
haloes follow profiles of hot gas, ejected gas, central stars and
adiabatically relaxed dark matter; the ejected gas fraction sets the
amplitude of the suppression and the ejection radius its scale (Schneider &
Teyssier 2015, arXiv:1510.06034) [src: Abstract].

| | BCemu (Giri & Schneider 2021, arXiv:2108.08863) | BACCO (Aricò et al. 2020, arXiv:2011.15018) |
|---|---|---|
| Parameters | log M_c ∈ [11, 15], μ ∈ [0, 2], θ_ej ∈ [2, 8], γ ∈ [1, 4], δ ∈ [3, 11], η, η_δ ∈ [0.05, 0.4] [src: Table 1] | log M_c ∈ [9, 15], log η, log β, log M_1,z0,cen, log M_inn, log θ_inn, log θ_out [src: Sect. 3.1, Eq. 2] |
| Cosmology | through f_b only, f_b ∈ [0.10, 0.25], because suppression is insensitive to other parameters [src: Sect. 2.2.1] | full emulator: σ8 ∈ [0.73, 0.9], Ω_m ∈ [0.23, 0.4], plus Ω_b, n_s, h, M_ν, w0, wa [src: Sect. 3.1, Eq. 1] |
| Training | 2700 baryonified Pkdgrav3 runs, 512³ in (256 h⁻¹ Mpc)³, 0.03 ≲ k ≲ 12.5 h Mpc⁻¹ [src: Sect. 2.2.1] | 10,000-point Latin hypercube over 15 parameters on rescaled simulations [src: Sect. 3.1] |
| Reduced models | 5 parameters (δ = 7, η = 0.2): ≈ 1% except z = 2; 3 (γ = 2.5, μ = 1): < 1.5% to k ≈ 10 at z ≤ 1; 1 (θ_ej = 3.5, η_δ = 0.2): ≈ 5% below k ≈ 8, valid only for k < 2 h Mpc⁻¹ [src: Sect. 5] | 1 parameter (M_c) fits BAHAMAS to 2% at z = 0, most others 2–3%, a few extreme cases above 6% [src: Sect. 5.2] |

The two groups disagree on how cosmology enters. BACCO finds baryonic and
cosmological effects "not independent", mainly through Ω_m and Ω_b (largely
removed at fixed Ω_b/Ω_m = 0.13), then σ8 at 2–3% through the mass function
[src: arXiv:2011.15018, Sect. 4]. BCemu keeps only f_b, citing earlier
studies [src: arXiv:2108.08863, Sect. 2.2.1]. Cost of the f_b-only design in
practice: in the DES Y3 blue-sample reanalysis the emulator fails outside
0.1 < f_b < 0.25, so values Ω_m ≳ 0.7 are never sampled and the effective
Ω_m prior peaks near 0.3 [src: arXiv:2512.04209, App. A, Fig. 5]. Cost of
BACCO's design: its cosmology box (Ω_m ∈ [0.23, 0.4], σ8 ∈ [0.73, 0.9]) is
narrower than typical lensing priors.

### Route D. One phenomenological amplitude
<!-- key: route-d-one-phenomenological-amplitude -->

P_m = P_m^L + A_mod (P_m^NL − P_m^L), with P^NL from HMcode-2020 without
feedback (Amon & Efstathiou 2022, arXiv:2206.11794, Eq. 6) [src: Sect.
3.2]. With the cosmology fixed to Planck, KiDS-1000 ξ± give A_mod =
0.69 ± 0.06, an underestimate because the Planck errors are neglected; S8 and
A_mod are strongly degenerate when both are free [src: Sect. 3.2]. The model
is "purely phenomenological": the suppression could be feedback or a dark-
matter property [src: Sect. 3.2]. DES Y6 uses it as a robustness variant
with A_mod ∈ [0.5, 1.5] (L2).

### Route E. Choose a statistic or a kernel less sensitive to small scales
<!-- key: route-e-choose-a-statistic-or-a-kernel-less -->

- **COSEBIs.** "Fairly insensitive to the amplitude of the non-linear matter
  power spectrum at high k", which allowed smaller scales and a 20% gain on
  S8 and Ω_m in KV450 + DES Y1 (Asgari et al. 2019, arXiv:1910.05336) [src:
  Abstract]. KiDS-Legacy's 2′ lower limit comes from the joint DES + KiDS
  analysis, which found it optimal for baryon mitigation with E_n/B_n
  [src: arXiv:2503.19441, Sect. 5.2.7].
- **BNT k-cuts.** Removing k ≥ 0.33 Mpc⁻¹ from KiDS-Legacy pseudo-Cℓ gives
  S8 = 0.798 ± 0.045, within 0.1σ of the no-cut result, when the Gaussian
  covariance is computed from the theory vector; with the covariance from the
  observed vector the same cut gives 0.717 ± 0.047, and k-cut scans show a
  scale trend up to 1.80σ that mocks attribute to the interplay of
  covariance prescription and data vector (Gu et al. 2026, arXiv:2607.04384)
  [src: Abstract].

### Route F. Calibrate the feedback model with gas observations
<!-- key: route-f-calibrate-the-feedback-model-with-gas -->

The DES Y3 blue-sample reanalysis puts correlated priors from X-ray gas
fractions and kSZ profiles on BCemu parameters; numbers in L2. The
mechanism behind such calibrations: the suppression is set by the mean
baryon fraction of haloes, to near per-cent level for k ≲ 10 h Mpc⁻¹ and
z ≤ 3 across 400 ANTILLES simulations, with group-mass haloes
(10¹³–10¹⁴ M⊙) dominating on cosmic-shear scales (Salcido et al. 2023,
arXiv:2305.09710) [src: Abstract].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

| Route | Assumes | Buys | Costs | Who |
|---|---|---|---|---|
| Scale cuts with one-sided contamination | the chosen simulation bounds reality | no extra parameters | result tied to the bounding simulation; information discarded | DES Y3, HSC Y3 (L2) |
| Two-sided cuts around a fixed moderate model | the truth lies between gravity-only and BAHAMAS-8 | keeps slightly smaller scales | 0.7σ (Illustris-1) to ≈ 1.5σ ("more extreme") bias if feedback is stronger | DES Y6 |
| HMcode-2020 T_AGN free | BAHAMAS-like feedback family | marginalises with one parameter | no gravity-only limit; priors extrapolate beyond 7.6–8.0 | KiDS-Legacy, joint DES + KiDS |
| Baryonification emulator | profile parametrisation, emulator range | links to gas observables | 5–7 parameters, or 1 with 5% error; cosmology range restrictions | DES Y3 reanalyses |
| A_mod | one shape for the suppression | model-agnostic test | no physical meaning; degenerate with S8 | robustness tests |
| COSEBIs / BNT | the kernel localises scales | small-scale information or targeted nulling | BNT result depends on covariance prescription | KiDS |

Results when two routes were compared on the same data are in L2 (DES Y6
free Θ_AGN or A_mod; KiDS-Legacy smaller scales; joint DES + KiDS
dark-matter-only). Three items not there:

- **How the validating simulation sets the residual.** DES Y6 cosmic shear
  states that, by design, BAHAMAS-8 biases S8 low by 0.5σ and Illustris-1
  by 0.7σ under its cuts, and kept the cuts because the true amplitude is
  still debated [src: arXiv:2602.10065, Sect. IV.3]. The DES Y6 framework
  paper states that "more extreme scenarios induce shifts in S8 of at most
  ∼ 1.5σ under our fiducial cuts", reduced when Θ_AGN is marginalised [src:
  arXiv:2601.14859, Sect. III.1]. The two numbers refer to different sets of
  simulations, not named alike in the two papers.
- **Stricter cuts need not reduce the shift.** Because of projection
  effects, smaller Δχ² does not systematically reduce ΔS8, even in the
  best-constrained direction S8(α = 0.636) [src: arXiv:2601.14859, Fig. 8
  caption].
- **Post-unblinding scale choices.** The DES Y3 "ΛCDM-optimised" cuts were
  obtained by removing the points with the largest Δχ² contribution until
  Δχ² = 1, give σ_2D = 0.1 for shear, do not pass validation in wCDM, and
  "were introduced after unblinding" [src: arXiv:2105.13548, Sect. V.1.3].
  The same cuts were adopted by the joint DES + KiDS analysis (L2), so a
  reader should know they were not part of the Y3 blind plan.

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Y3 scale-cut parameters | R_min,w = 8, R_min,γt = 6 Mpc/h, Δχ²_thr = 0.5 shared over 20 ξ± | DES Y3 | arXiv:2105.13548 | Eq. 39 |
| Y3 residual bias, Illustris at fiducial cuts | 0.23σ_2D shear, 0.50σ_2D 3×2pt | DES Y3 | arXiv:2105.13548 | Sect. V.1.3 |
| Y3 wCDM residuals | 0.1, 0.16, 0.05 σ_2D (2×2, 3×2, 3×2 + Planck) | DES Y3 | arXiv:2105.13548 | Sect. V.1.3 |
| Y6 Δχ² search range | [0.1, 5] | DES Y6 | arXiv:2601.14859 | Fig. 7 caption |
| Y6 thresholds | 0.3σ minor, 0.5σ major or coupled | DES Y6 | arXiv:2601.14859 | Sect. VI.2 |
| Y6 validation cost | 1.75 million CPU-hours | DES Y6 | arXiv:2601.14859 | Sect. VI.1 |
| Y6 fiducial feedback | Θ_AGN = 7.7, fixed | DES Y6 | arXiv:2601.14859 | Sect. III.1 |
| Halofit error | 5–10% on non-linear scales | DES Y6 comparison | arXiv:2601.14859 | Sect. III.1 |
| HMcode-2020 calibrated T_AGN range | 7.6–8.0 (BAHAMAS); to 8.3 with cosmo-OWLS | HMcode-2020 | arXiv:2009.01858 | Sect. 6.4, Table 6 |
| HMcode-2020 one-parameter accuracy | within a couple of per cent of BAHAMAS | HMcode-2020 | arXiv:2009.01858 | Sect. 6.3 |
| BCemu f_b range | 0.10–0.25 | BCemu | arXiv:2108.08863 | Table 1 |
| BACCO one-parameter fit | 2% (BAHAMAS, z = 0); > 6% for a few extremes | BACCO | arXiv:2011.15018 | Sect. 5.2 |
| BACCO cosmology–baryon coupling via σ8 | 2–3% | BACCO | arXiv:2011.15018 | Sect. 4 |
| A_mod with Planck cosmology | 0.69 ± 0.06 | KiDS-1000 ξ± | arXiv:2206.11794 | Eq. 7 |
| COSEBIs gain | 20% on S8, Ω_m | KV450 + DES Y1 | arXiv:1910.05336 | Abstract |
| BNT k-cut | k ≥ 0.33 Mpc⁻¹ removed; S8 = 0.798 ± 0.045 or 0.717 ± 0.047 by covariance choice | KiDS-Legacy | arXiv:2607.04384 | Abstract |
| Baryonification suppression from clusters | above k ∼ 0.5 h Mpc⁻¹, 10–25% near k ∼ 2 h Mpc⁻¹ | early estimate | arXiv:1510.06034 | Abstract |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Bounding simulation too weak.** If the true suppression exceeds the
  bracket, S8 is biased low by 0.7σ (Illustris-1) in DES Y6 [src:
  arXiv:2602.10065, Sect. IV.3]. Test: analyse synthetic data from stronger
  simulations with the fiducial cuts; free the feedback parameter.
- **Feedback parameter outside its calibration.** HMcode-2020 priors that go
  below 7.6 or above 8.3 extrapolate the BAHAMAS fit, and no value recovers
  gravity-only [src: arXiv:2009.01858, Sects. 6.3–6.4]. Test: run a
  gravity-only (B = 4, M_b = 0, f_* = 0) variant explicitly.
- **Emulator boundaries acting as priors.** BCemu's f_b range shapes the Ω_m
  prior [src: arXiv:2512.04209, App. A]; BACCO's cosmology box is narrower
  than lensing priors [src: arXiv:2011.15018, Sect. 3.1]. Test: plot the
  effective prior by sampling the prior through the likelihood.
- **Validation blind to projection effects.** Tightening cuts may not shrink
  shifts [src: arXiv:2601.14859, Fig. 8]. Test: validate on the
  best-constrained direction and report MAP as well as mean.
- **Smaller scales reopen other systematics.** KiDS-Legacy's 0.5′ extension
  makes the B-mode test fail again (p < 0.01) [src: arXiv:2503.19441, Sect.
  5.2.7]. Test: repeat null tests with each scale range.
- **Covariance built from the observed data vector.** Moves the BNT-cut S8
  by about 0.08 [src: arXiv:2607.04384, Abstract]. Test: theory-vector
  Gaussian covariance, iterated.
- **Scale choices made after unblinding.** DES Y3 optimised cuts [src:
  arXiv:2105.13548, Sect. V.1.3]. Test: state which cuts were in the blind
  plan.
- **Reading a phenomenological suppression as feedback.** A_mod can equally
  be a dark-matter effect [src: arXiv:2206.11794, Sect. 3.2]; for the
  simulation side of the argument see FLAMINGO (McCarthy et al. 2023,
  arXiv:2309.07959) and L2.

## Reading list
<!-- key: reading-list -->

- Foundation: Schneider & Teyssier 2015, arXiv:1510.06034 — baryonic
  correction model.
- Method: Mead et al. 2020, arXiv:2009.01858 — HMcode-2020 feedback model,
  one-parameter form, recommended priors.
- Method: Giri & Schneider 2021, arXiv:2108.08863 — BCemu, parameter ranges,
  reduced models.
- Method: Aricò et al. 2020, arXiv:2011.15018 — BACCO emulator; baryon–
  cosmology coupling.
- Method: Salcido et al. 2023, arXiv:2305.09710 — suppression from halo
  baryon fractions.
- Application: Krause et al. 2021, arXiv:2105.13548 — the DES scale-cut
  procedure and its reasons.
- Application: Sanchez-Cid et al. 2026, arXiv:2601.14859 — two-sided
  bracketing, thresholds, Θ_AGN fixed.
- Application: Wright et al. 2025, arXiv:2503.19441 — model-based route with
  COSEBIs.
- Test: Asgari et al. 2019, arXiv:1910.05336 — COSEBIs and high-k
  insensitivity.
- Test: Gu et al. 2026, arXiv:2607.04384 — BNT k-cuts as mitigation and
  diagnostic.
- Critique: Amon & Efstathiou 2022, arXiv:2206.11794 — a stronger
  suppression as an alternative to low S8.
- Critique: McCarthy et al. 2023, arXiv:2309.07959 — FLAMINGO feedback
  variations against the lensing data.

## Not verified
<!-- key: not-verified -->

- Which simulations the DES Y6 framework calls "more extreme scenarios"
  (the ≈ 1.5σ statement): not named in the paragraph read.
- The BCemu and BACCO emulator accuracies in their test sets (Sects.
  2.2.3 and 3.4): not read.
- FLAMINGO and SP(k) emulators as used in a lensing likelihood: no analysis
  using them was read.
- The theory-error-covariance route for baryons (cited in arXiv:2105.13548,
  Sect. V.1, footnote): not read.
