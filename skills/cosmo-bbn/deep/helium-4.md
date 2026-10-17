# Primordial helium-4 from metal-poor H II regions — cosmo-bbn dossier

Scope: how one H II region's He⁺/H⁺ is fitted from recombination-line
ratios (model parameters, lines used, priors, goodness-of-fit and flags),
how targets become Y_P (weighted average, York regression, intrinsic-scatter
likelihood), and which method choices separate the LBT Y_p Project, the
EMPRESS/PHLEK line and the Izotov–Thuan line.
Snapshot: 2026-10-17.
From: Cooke 2024 review, Sect. 3.2 and 6.4; LBT Y_p Project, Izotov–Thuan,
EMPRESS and Valerdi groups.

Already in L2, not repeated here: the Y_P values of every group and their
history in `results.md#primordial-helium-4`; the programmes, instruments and
sample sizes in
`surveys-and-data.md#helium-4-metal-poor-h-ii-region-programmes`; the
emissivity shift (+0.9% in y⁺), the WLS-versus-linmix comparison and the
intrinsic scatter in `systematics.md#helium-4`; the y–Y conversion trap in
`physics-and-methods.md#conventions-and-where-the-community-is-split`; the
EMPRESS–D/H incompatibility in
`open-questions.md#helium-systematics-and-neff-from-bbn`.

Notation: y⁺ = n(He⁺)/n(H⁺), y⁺⁺ = n(He⁺⁺)/n(H⁺), y = y⁺ + y⁺⁺ (number
ratio, neutral He neglected), Y the mass fraction, Y_P and y_P their
primordial (zero-metallicity) values, O/H the oxygen number ratio.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Choose targets
<!-- key: step-1-choose-targets -->

| Criterion | LBT Y_p Project | EMPRESS XV | Izotov et al. 2014 |
|---|---|---|---|
| Metallicity | O/H < 15 × 10⁻⁵, priority to O/H < 4 × 10⁻⁵ [src: arXiv:2601.22238, Sect. III] | adds extremely metal-poor galaxies (EMPGs) to 58 literature galaxies, most above 10% Z_⊙ [src: arXiv:2506.24050, Sect. II.2] | no stated cut in the passage read |
| Brightness, youth | F(Hβ) ≳ 3 × 10⁻¹⁵ erg s⁻¹ cm⁻², W(Hβ) ≳ 100 Å [src: arXiv:2601.22238, Sect. III] | — | EW(Hβ) ≥ 150 Å, O²⁺/O ≥ 0.8, σ(Y_wm)/Y_wm ≤ 3% [src: arXiv:1408.6953, Sect. 4.3] |
| Required lines | He I λ4026 at > 3σ; He I λ10830 measured [src: arXiv:2601.22238, Sect. III] | He I λ10830 in the NIR fit [src: arXiv:2506.24050, Sect. IV.3.2] | He I λ10830 [src: arXiv:1408.6953, title] |
| Chemical anomalies | log(N/O) tested, no trend, not used as a cut [src: arXiv:2601.22238, Sect. V.4] | log(N/O) > −1.0 excluded [src: arXiv:2506.24050, Sect. IV.4] | — |
| Neutral helium | radiation softness η = (O⁺/O²⁺)/(S⁺/S²⁺), sample mean 0.87, He⁰ matters for η ≳ 2 [src: arXiv:2601.22238, Sect. VII.1] | log η_rds ≲ 0.9 required, with η_rds = (S²⁺/S⁺)/(O²⁺/O⁺) (Eq. 8) [src: arXiv:2506.24050, Sect. IV.3.3] | ICF(He) within ~2% of unity [src: arXiv:1408.6953, Sect. 4.4] |

Stated reasons:

- **Low metallicity.** It "limits potential systemic error introduced by
  enrichment of He" and by an assumed linear Y–O/H relation
  [src: arXiv:2601.22238, Sect. III].
- **He I λ4026.** It is the weak line most sensitive to underlying stellar
  absorption; without it the absorption, and hence y⁺, is overestimated
  [src: arXiv:2601.22238, Sect. III].
- **He I λ10830.** It is far more sensitive to collisional excitation, hence
  to n_e, and breaks the temperature–density degeneracy
  [src: arXiv:2601.22238, Sect. III]; it reduced most y⁺ errors by ~50%
  (arXiv:1503.08146) [src: Sect. 7].
- **High EW(Hβ) and O²⁺/O.** Izotov et al. found the weighted-mean Y
  rising with decreasing EW(Hβ) and O²⁺/O, an "unphysical" trend; low
  EW(Hβ) means more underlying-galaxy light, an overestimated starburst age
  and an overestimated ICF(He) [src: arXiv:1408.6953, Sect. 4.3].
- **N/O.** Nitrogen-rich galaxies at z ~ 6 show very strong He I emission
  and may deviate chemically from primordial; relaxing the cut raises
  Y_P by only ~0.3σ [src: arXiv:2506.24050, Sect. IV.4, footnote 4].

### Step 2. Fit each region
<!-- key: step-2-fit-each-region -->

**LBT model** (Aver et al. 2026, arXiv:2601.22238) [src: Sect. II]. A
uniform Case B H II region with mean n_e and T_e, fitted by minimising

    χ² = Σ_λ [F(λ)/F(Hβ|Pγ) − (F(λ)/F(Hβ|Pγ))_meas]² / σ(λ)²     (Eq. 1)

where line fluxes are taken relative to Hβ, except He I λ10830, taken
relative to Pγ. Up to nine parameters: T_e, n_e, τ (optical depth of He I
λ3889 at line centre), C(Hβ) (reddening), a_He, a_H, a_P (underlying
stellar absorption under He, Balmer and Paschen lines), ξ (neutral-to-
ionised H fraction for collisional excitation) and y⁺. Lines: up to eight
He ratios (λλ4026, 4388, 4471, 4922, 5876, 6678, 7065 to Hβ; λ10830 to
Pγ), fifteen H ratios (Hα to H12, P8–P15) and the H8 + He I λ3889 blend:
24 ratios, 15 degrees of freedom. Best fit at the χ² minimum
("frequentist"); errors from the 1D marginalised Δχ² 68% interval, with
the MCMC used to map χ² [src: Sect. II].

Updates since the model of the team's earlier paper (their ref. [5]), with
their reasons [src: Sect. II]:

- He emissivities of Del Zanna & Storey and H emissivities of Storey &
  Sochi on finer grids; He lines change by ≲ 1% at low density except
  λ6678 [src: Sect. II.1].
- Radiative transfer from Kurichin & Ivanchik (2025), fitted over
  8000 < T_e < 22 000 K, 1 < n_e < 10 000 cm⁻³, 0 < τ < 10 to ≲ 0.1%,
  replacing the Benjamin et al. fits valid only to τ < 2, "largely
  eliminating potential extrapolation" [src: Sect. II.2].
- He I λ5016 and λ7281 removed because both are systematically low
  against Case B, which "would systematically bias the result"
  [src: Sect. II.3].
- ξ dropped below T_e = 14 000 K, where collisional excitation is
  negligible but the fit drifts to non-physical ξ [src: Sect. II.4].
- T(O III) enters as a weak prior on T(He) [src: Sect. V.3].

**EMPRESS model** (Yanagisawa et al. 2025, arXiv:2506.24050) [src:
Sect. IV.3.2]. The YMCMC code of Hsyu et al. 2020 with eight parameters
(no a_P); line ratios

    F(λ)/F(Hβ) = y⁺ [E(λ)/E(Hβ)] × [(EW(Hβ) + a_He(Hβ))/EW(Hβ)] /
                 [(EW(λ) + a_He(λ))/EW(λ)] × f_τ(λ) 10^{−f(λ)c(Hβ)}   (Eq. 6)

for He (Eq. 5 is the H analogue with the collisional factor C/R), with E
the emissivity, EW the equivalent width, f_τ the optical-depth function
and f(λ) the reddening law. Flat priors (Eq. 7): 0.06 ≤ y⁺ ≤ 0.15,
0 ≤ log n_e ≤ 3, 0 ≤ c(Hβ) ≤ 0.5, 0 ≤ a_H ≤ 10, 0 ≤ a_He ≤ 5,
0 ≤ τ_He ≤ 5, −6 ≤ log ξ ≤ −0.1; upper y⁺ bound raised to 0.15 because of
possible He overabundance at high z; 500 walkers, 1000 steps, 800 burn-in;
parameters reported as posterior medians with 16–84% ranges [src].

**Izotov–Thuan route** (arXiv:1408.6953) [src: Sect. 3.4]. Monte Carlo
over T_e(He⁺), N_e(He⁺) in 10–600 cm⁻³ and τ(λ3889) in 0–5, minimising the
scatter of single-line abundances about their weighted mean,
χ² = Σ_i (y⁺_i − y⁺_wm)²/σ²(y⁺_i) (Eq. 5), with y⁺_wm the inverse-variance
mean (Eq. 6). T_e(He⁺) is tied to T_e(O III) through a CLOUDY-calibrated
relation (Eq. 9) varied within ±5%, or set equal to it. Total
y = ICF(He)(y⁺ + y²⁺) and Y = 4y(1 − Z)/(1 + 4y) with Z = B × O/H,
B = 8.64 A(O) − 47.44, A(O) = 12 + log O/H (Eqs. 7–8).

### Step 3. Screen the fits
<!-- key: step-3-screen-the-fits -->

- **LBT: χ² at 95%.** For 15 degrees of freedom χ² < 25.0; 7 of 54 targets
  fail (three expected from noise alone), several showing [Fe V] λ4227,
  i.e. ionisation not from massive stars [src: arXiv:2601.22238, Sect. IV,
  Table 1].
- **LBT: flags on the 47 survivors.** τ > 10 (outside the radiative-transfer
  fit domain; one target, τ = 13.25); a_He > 0.5 Å (two targets; an earlier
  paper of the team used 1.0 Å, but the LBT sample's mean a_He is 0.266 Å against
  0.522 Å in the older HeBCD data); T(He) diverging from T(O III) and
  T(S III); residual ΔY plotted against every model parameter and against
  W(Hβ), n_e(S II), O⁺/O, η and χ²/dof, with no further trend found
  [src: Sects. V.1–V.5]. 41 targets remain.
- **EMPRESS/PHLEK: 2σ line criterion.** All detected He I and H I lines
  reproduced within 2σ; 11 of 27 EMPRESS galaxies pass, and relaxing the
  criterion "only marginally affects" Y_P [src: arXiv:2506.24050,
  Sect. IV.3.2]. With the N/O and η cuts, 9 galaxies are added to 58
  literature ones, 67 in all [src: Sect. IV.5].

### Step 4. From targets to Y_P
<!-- key: step-4-from-targets-to-yp -->

**Weighted average (LBT primary).** Inverse-variance mean
Ȳ ± σ̄ = Σw_iY_i/Σw_i ± (Σw_i)^{−1/2}, w_i = 1/σ_i² (Eqs. G1–G2), error
multiplied by S when S² = Σw_i(Ȳ − Y_i)²/(N − 1) > 1, the Particle Data
Group procedure (Eqs. G3–G4) [src: arXiv:2601.22238, App. G]. On the 15
unflagged targets with O/H < 4 × 10⁻⁵: y_P = 0.08146 ± 0.00058 (Eq. 2),
S = 1.15, converted by Y_P = 4y_P/(1 + 4y_P) (Eq. 3) to
0.2458 ± 0.0013 (Eq. 4) [src: Sect. VII.2]. The stated justification is
that Y_P does not require the slope when the metallicity baseline is
short, and the running mean ⟨Y⟩ shows no systematic rise with the O/H
cut [src: Sect. VII.2].

**York regression (LBT secondary).** Weighted least squares with errors on
both y and O/H, York's method, weights w_i = w_Xi w_Yi/(w_Xi + b²w_Yi)
and S² = Σw_i(a + bX_i − Y_i)²/(N − 2) (Eqs. G5–G6) [src: App. G]. On 41
targets, y_P = 0.08117 ± 0.00096, slope Δy/Δ(O/H) = 14 ± 12, S = 1.70
(Eqs. 5–6) [src: Sect. VII.3]. Regressing y rather than Y removes the Z
dependence, as advocated by Hsyu et al. [src: Sect. VII.3]. linmix
(Bayesian, errors on both axes, intrinsic scatter, median of 10 000
chains) is the third estimator [src: App. G].

**Likelihood with intrinsic scatter (EMPRESS).** Linear model
y = y_P + [dy/d(O/H)] (O/H) (Eq. 9), maximising

    log L = −½ Σ_i [ (y_i − a(O/H)_i − b)² / s_i² + log s_i² ],
    s_i² = σ_yi² + a² σ_(O/H)i² + σ_int²                         (Eq. 10)

with a the slope, b = y_P and σ_int the intrinsic scatter, by MCMC: y_P =
0.0790 ± 0.0017, slope 0.00067 (+0.00017/−0.00016), σ_int = 0.0010
(+0.0010/−0.0007) (Eqs. 11–13), Y_P = 0.2402 ± 0.0040 (Eq. 15)
[src: arXiv:2506.24050, Sect. V.1].

**Regression in Y with Z (Aver 2015, Izotov 2014).** Aver et al. 2015
regress Y with Z = 20(O/H) [src: arXiv:1503.08146, Sect. 6, footnote 1];
Izotov et al. 2014 regress with their B(A(O)) relation and add a
Monte-Carlo systematic of 0.0019 to the 0.0010 statistical error
[src: arXiv:1408.6953, Sects. 3.4, 4.4].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Best fit or posterior median
<!-- key: best-fit-or-posterior-median -->

The LBT team uses the χ² minimum; Hsyu et al., and EMPRESS after them,
use posterior medians. For parameters bounded at zero (n_e, a_He, τ) whose
best fit is near zero, the chain is truncated with a tail to high values,
so the median sits "significantly higher than the best-fit", sometimes
with an interval that excludes the best fit [src: arXiv:2601.22232,
App. A]. Measured on EMPRESS data: maximum-likelihood parameters give
Y_P = 0.2404 (+0.0039/−0.0034) (Eq. 27) against 0.2402 ± 0.0040 with
medians, "in good agreement" [src: arXiv:2506.24050, Sect. V.1].

### Positive-only or signed nuisance priors
<!-- key: positive-only-or-signed-nuisance-priors -->

Matsumoto et al. (EMPRESS VIII) let c(Hβ), a_H, a_He and τ_He go
negative, arguing that true values near zero scatter to negative best
fits and that positive-only priors bias medians upward
[src: arXiv:2506.24050, Sect. V.1; arXiv:2601.22232, App. A]. In EMPRESS
XV, signed priors give Y_P = 0.2355 (+0.0034/−0.0035) (Eq. 23) against
0.2402 fiducial, attributed to the y⁺–a_He correlation; the fiducial keeps
positive priors [src: arXiv:2506.24050, Sect. V.1]. The LBT team keeps
positive priors with maximum likelihood instead [src: arXiv:2601.22232,
App. A].

### Average or regression; how far to extrapolate
<!-- key: average-or-regression-how-far-to-extrapolate -->

- LBT: weighted average 0.2458 ± 0.0013 (15 targets, O/H < 4 × 10⁻⁵);
  extending to O/H < 8 × 10⁻⁵ (33 targets) gives 0.2464 ± 0.0013 with
  S = 1.76, so doubling the sample does not shrink the error because of
  dispersion [src: arXiv:2601.22238, Sect. VII.2]. The slope rests on
  8 of 41 points above O/H = 8 × 10⁻⁵; without them it is 15 ± 36
  [src: Sect. VII.3].
- Bias of averaging if enrichment is real: for ΔY/Δ(O/H) = 46 the
  average over O/H < 4 × 10⁻⁵ would be high by ~0.0009, below the error
  [src: Sect. VII.2].
- EMPRESS, EMPGs only: slope fixed at Hsyu's 0.00054 gives
  Y_P = 0.2383 (+0.0058/−0.0043); slope zero gives 0.2422
  (+0.0060/−0.0042); σ_int rises to 0.0035–0.0043, i.e. EMPGs scatter
  more than metal-poor galaxies [src: arXiv:2506.24050, Sect. V.1,
  Eqs. 28–33].
- Aver 2015 on the Izotov et al. data: 15 qualifying objects give
  0.2449 ± 0.0040 (slope 79 ± 43); with three flagged objects 0.2424 ±
  0.0034; mean of qualifying points 0.2515 ± 0.0017; regression without
  the T(O III) prior on 12 objects 0.2379 ± 0.0050 [src:
  arXiv:1503.08146, Sect. 6].

### Same data, different analysis
<!-- key: same-data-different-analysis -->

From the 45 H II regions with λ10830, Izotov et al. keep 28 and find
0.2551 ± 0.0022; Aver et al. find 0.2449 ± 0.0040 from the same
observations, and attribute the difference "both to differences in
determining the helium abundances for individual objects and in how the
samples are defined" [src: arXiv:1503.08146, Sect. 6]. Izotov et al.
themselves get 0.2540 ± 0.0008 from 62 regions with only a density cut
(N_e ≤ 200 cm⁻³) [src: arXiv:1408.6953, Sect. 4.3].

### Qualification test
<!-- key: qualification-test -->

χ² at 95% (LBT) is stricter than "all lines within 2σ" (PHLEK, EMPRESS);
the LBT team expects the latter to admit more objects and lower the
quoted error, effect on Y_P unknown [src: arXiv:2601.22232, App. A]. They
also note that 38 of Hsyu's 54 Sample-1 galaxies, all from SDSS, lack
λ10830 [src: same].

### Atomic data
<!-- key: atomic-data -->

- LBT: the emissivity update raised y⁺ by ~0.9% on average (see L2); the
  radiative-transfer update lowered best-fit τ and marginally lowered y⁺
  for targets with non-negligible τ; 15 targets have τ < 0.1 and are
  unaffected [src: arXiv:2601.22238, Sect. VI.3].
- EMPRESS: CHIANTI collision strengths instead of the default lower Y_P by
  0.0017, to 0.2385 (+0.0037/−0.0031) (Eq. 19), comparable to a quoted
  ±0.0015 systematic from H I collisional excitation [src:
  arXiv:2506.24050, Sect. V.1].
- Izotov et al.: 1% emissivity, 0.25% ICF and 0.5% non-recombination
  H-line uncertainties give ≤ 0.75% (0.0019) in Y_P [src:
  arXiv:1408.6953, Sect. 4.4].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Line ratios and parameters | 24 ratios, 9 parameters, 15 d.o.f. | LBT IV | arXiv:2601.22238 | Sect. II |
| χ² cut | 95% CL; χ² < 25.0 for 15 d.o.f.; 47 of 54 pass | LBT IV | arXiv:2601.22238 | Sect. IV |
| Flags | τ > 10; a_He > 0.5 Å; T(He) vs T(O III), T(S III) | LBT IV | arXiv:2601.22238 | Sects. V.1–V.3 |
| ξ fitted only above | T_e = 14 000 K | LBT IV | arXiv:2601.22238 | Sect. II.4 |
| Radiative-transfer fit domain | 0 < τ < 10, n_e < 10⁴ cm⁻³, 8000–22 000 K | LBT IV (KI25) | arXiv:2601.22238 | Sect. II.2 |
| Mean y⁺ error | 2.3% (LBT) against 4.0% (team's pre-LBT dataset) | LBT IV | arXiv:2601.22238 | Sect. VI.1 |
| S factor | 1.15 (15 targets); 1.76 (33); 1.70 (regression, 41) | LBT IV | arXiv:2601.22238 | Sects. VII.2–VII.3 |
| Averaging bias for ΔY/Δ(O/H) = 46 | ~0.0009 | LBT IV | arXiv:2601.22238 | Sect. VII.2 |
| YMCMC priors | 0.06 ≤ y⁺ ≤ 0.15; 0 ≤ a_He ≤ 5; 0 ≤ τ_He ≤ 5; −6 ≤ log ξ ≤ −0.1 | EMPRESS XV | arXiv:2506.24050 | Eq. 7 |
| Sample cuts | log(N/O) ≤ −1.0; log η_rds ≲ 0.9; all lines within 2σ | EMPRESS XV | arXiv:2506.24050 | Sects. IV.3–IV.5 |
| Signed-prior shift | Y_P 0.2402 → 0.2355 | EMPRESS XV | arXiv:2506.24050 | Eqs. 15, 23 |
| Collision-strength shift | −0.0017 in Y_P | EMPRESS XV | arXiv:2506.24050 | Eq. 19 |
| Intrinsic scatter | σ_int = 0.0010 (+0.0010/−0.0007) in y | EMPRESS XV | arXiv:2506.24050 | Eq. 13 |
| Selection | EW(Hβ) ≥ 150 Å, O²⁺/O ≥ 0.8, σ(Y)/Y ≤ 3% | Izotov 2014 | arXiv:1408.6953 | Sect. 4.3 |
| Systematic in Y_P | 0.0019 (≤ 0.75%) | Izotov 2014 | arXiv:1408.6953 | Sect. 4.4 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Extrapolating the radiative-transfer correction.** High-τ targets
  sit outside the fit domain and showed signs of an upward Y bias; flag
  τ > 10 [src: arXiv:2601.22238, Sect. V.1]. Test: residual ΔY against τ.
- **Overestimated underlying absorption.** Without He I λ4026, a_He and y⁺
  come out high [src: arXiv:2601.22238, Sect. III]. Test: require λ4026;
  plot ΔY against a_He.
- **Temperature–density degeneracy.** Optical lines alone leave it open;
  He I λ10830 breaks it [src: arXiv:1503.08146, Sect. 7;
  arXiv:2506.24050, Sect. IV.3.2]. Scaling a separately observed λ10830
  to the optical spectrum can add bias; simultaneous optical and NIR
  spectra were recommended [src: arXiv:1503.08146, Sect. 7].
- **Biased lines.** He I λ5016 and λ7281 fall below Case B; including them
  biases y⁺ [src: arXiv:2601.22238, Sect. II.3].
- **Non-physical neutral fraction.** At low T_e, ξ runs away; drop it
  below 14 000 K [src: arXiv:2601.22238, Sect. II.4]. In YMCMC the
  posterior of log ξ plateaus below −3 without affecting other parameters
  [src: arXiv:2506.24050, Sect. IV.3.2].
- **Sample-driven slope.** A slope fixed by a few high-O/H points; test by
  dropping them [src: arXiv:2601.22238, Sect. VII.3].
- **Unphysical sample trends.** Weighted-mean Y rising with falling EW(Hβ)
  or O²⁺/O signals an overestimated ICF [src: arXiv:1408.6953, Sect. 4.3].
- **Many low-quality points.** They shrink the formal error of the mean
  artificially; apply the S factor [src: arXiv:2601.22238, App. G].
- **Dropping the T(O III) prior.** The Aver 2015 regression fell to
  0.2379 ± 0.0050 without it, which "raises some questions regarding
  possible systematic errors" [src: arXiv:1503.08146, Sect. 6].
- **Validation.** Expected χ² failure count (3 of 54 at 95%) against
  observed (7) [src: arXiv:2601.22238, Sect. IV]; mean ⟨Y⟩ stable against
  the O/H cut [src: Sect. VII.2].

## Reading list
<!-- key: reading-list -->

- Method: Skillman et al. 2026 (LBT I), arXiv:2601.22232 — project design;
  App. A compares the LBT and PHLEK/EMPRESS methods.
- Application: Aver et al. 2026 (LBT IV), arXiv:2601.22238 — full current
  model, χ² cut, flags, weighted average and York regression.
- Application: Yanagisawa et al. 2025 (EMPRESS XV), arXiv:2506.24050 —
  YMCMC priors, N/O and softness cuts, intrinsic-scatter likelihood,
  prior and atomic-data tests.
- Application: Izotov, Thuan & Guseva 2014, arXiv:1408.6953 — Monte Carlo
  route, EW(Hβ) and excitation cuts, systematic budget.
- Critique: Aver, Olive & Skillman 2015, arXiv:1503.08146 — re-analysis of
  the Izotov data, λ10830 effect, regression variants.
- Method: Hsyu et al. 2020, arXiv:2005.12290 — YMCMC and regression in y.
- Review: Cooke 2024, arXiv:2409.06015 — context.

## Not verified
<!-- key: not-verified -->

- The Kurichin & Ivanchik 2025 radiative-transfer paper, the Del Zanna &
  Storey and Storey & Sochi emissivity papers, and the Méndez-Delgado
  study of He I λ5016 and λ7281: cited through arXiv:2601.22238, not read,
  no identifier recorded.
- Hsyu et al. 2020 (arXiv:2005.12290): its YMCMC description was read only
  through arXiv:2506.24050 and arXiv:2601.22232, not in its own body.
- LBT Y_p Project II (MODS spectra) and VI (N/O): not found or not read.
- Valerdi et al. and the Ioffe SDSS analyses: their per-target methods were
  not read for this dossier.
