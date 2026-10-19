# Baryon census from absorption lines — cosmo-cosmic-web dossier

Scope: how a baryon fraction is obtained from intervening absorbers (H I
Lyα, broad Lyα, O VI in the far ultraviolet; O VII and O VIII in X-rays):
the column-density integral, the ionisation, metallicity and size
corrections with their error budget, the redshift path, the detection
statistic and its look-elsewhere correction, the FUV-prior strategy, the
vetoes against Galactic, intrinsic and circumgalactic absorption, and how
"missing" is defined against Ω_b.
Snapshot: 2026-10-19.
From: Walker & Lau 2022, Sect. 4.7.

Already in L2, not repeated here: the census results and their history
(`results.md#the-baryon-census`), the controversy over the 1ES 1553+113
lines (`open-questions.md#are-the-missing-baryons-found`,
`open-questions.md#stale-claims-and-misconceptions`). Elsewhere: the FRB
partition of IGM and halo gas, in `cosmo-multimessenger`
(`deep/frb-baryon-distribution.md`); filament gas from tSZ, kSZ and X-ray
emission stacks, in `deep/filament-gas.md`.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Write the census as an integral over absorbers
<!-- key: step-1-write-the-census-as-an-integral-over -->

For an ion, the cosmological density follows from the column-density
distribution f(n) = ∂²n/∂N∂z,
Ω_ion = ρ_ion/ρ_c = (m_ion H₀ / ρ_c c) ∫ f(n) N dN, and the baryons it
traces from
Ω_WHIM,ion = Ω_ion (μ_H m_H / m_ion) / [A f_ion(T)],
where A is the element abundance relative to hydrogen, f_ion(T) the
fraction of the element in that ion and μ_H m_H the mass per hydrogen
atom (Spence et al. 2023, arXiv:2305.01587, Eqs. 1–3) [src: Sect. 5.1].
Spence et al. take μ_H = 1.3 for sub-solar gas [src: Sect. 5.1]. When
only a few absorbers exist, the integral is replaced by a sum over
sightlines, Ω_WHIM,X = (μ m_H/ρ_c) Σ_i N_H,i / Σ_i D_i, with N_H,i the
total hydrogen column of the WHIM towards source i and D_i the distance it
probes (arXiv:2305.01587, Eq. 4; Bonamente et al. 2025, arXiv:2507.21719,
Eq. 3) [src: Sect. 5.1; Sect. 3.1.1].

The FUV version used for O VI places the corrections inside the integral
(Shull, Smith & Danforth 2012, arXiv:1112.2706, Eq. 1):
Ω_b^(OVI) = [μ_b H₀ / (c ρ_cr (O/H)☉)] ∫ (dN/dz) N dN / [Z_O(N) f_OVI(N)],
with μ_b = 1.33 m_H the mean baryon mass per hydrogen nucleus including
helium and (O/H)☉ = 4.90 × 10⁻⁴ [src: Sect. III.1]. dN/dz is the number
of absorbers per unit redshift, measured as the count over the redshift
path (Step 4).

### Step 2. Choose the ionisation and metallicity correction
<!-- key: step-2-choose-the-ionisation-and-metallicity -->

**O VI.** Earlier surveys took constant f_OVI = 0.2 (its collisional-
equilibrium maximum, at log T = 5.45) and Z/Z☉ = 0.1 (arXiv:1112.2706)
[src: Sect. III.1]. From their simulations, Shull et al. fit
(Z/Z☉) f_OVI = 0.015 (N_OVI/10¹⁴ cm⁻²)^0.70 (Eq. 2), whose
column-density-weighted mean is 0.01, a factor of two below the old 0.02;
over 13.0 ≤ log N_OVI ≤ 15.0 this doubles the O VI-traced baryons [src:
Sect. III.1]. With dN/dz ∝ N^(−β), β ≈ 2.0 and γ ≈ 0.70, the integral
grows at the faint end as N_min^(−0.7) (Eq. 3), so the result "is
dominated by weak absorbers with N_OVI < 10^13.5 cm⁻²", where line
statistics are least secure [src: Sect. III.1].

**Photoionised Lyα forest.** The absorber is modelled as a singular
isothermal sphere n_H(r) = n₀(r/r₀)⁻² in photoionisation equilibrium,
n_HI = n_e n_H α_H^(A)(T)/Γ_H (Eq. 4), with case-A recombination
α_H^(A) ≈ 2.51 × 10⁻¹³ T_4.3^(−0.726) cm³ s⁻¹ and n_e = 1.165 n_H
(arXiv:1112.2706) [src: Sect. III.2]. Integrating gives the baryon mass
within impact parameter p,
M_b(p) = (1.09 × 10⁹ M☉) N₁₄^(1/2) Γ₋₁₄^(1/2) p₁₀₀^(5/2) T_4.3^0.363
(Eq. 6), with N_HI = 10¹⁴ N₁₄ cm⁻², Γ_H = 10⁻¹⁴ Γ₋₁₄ s⁻¹, p = 100 p₁₀₀
kpc and T = 10^4.3 T_4.3 K, and the closure parameter Ω_b^(HI) as an
integral of (dN/dz) N₁₄^(1/2) over log N_HI with prefactor 9.0 × 10⁻⁵
h₇₀⁻¹ p₁₀₀^(1/2) T_4.3^0.363 (1 + z)^0.2 / [Ω_m(1 + z)³ + Ω_Λ]^(1/2)
(Eq. 9) [src: Sect. III.2]. The photoionisation rate is taken as Γ_H(z) =
2.28 × 10⁻¹⁴ (1 + z)^4.4 s⁻¹, a fit to Haardt & Madau 2012, and p is held
constant in z [src: Sect. III.2].

**Broad Lyα absorbers (BLAs).** Lyα lines with Doppler parameter b ≥ 40
km s⁻¹, i.e. T = m_H b²/2k = 9.69 × 10⁴ K (b/40 km s⁻¹)² for pure thermal
broadening (arXiv:1112.2706) [src: App. B]. They need no metallicity
correction but do need the neutral fraction f_HI from the temperature and
ionisation state [src: Sect. IV]. The same b ≥ 40 km s⁻¹ cut defines
BLAs in current COS work (arXiv:2610.11203) [src: abstract] and serves as
an X-ray prior for log T ≥ 5 (arXiv:2305.01587) [src: Sect. 2.2].

**X-ray O VII and O VIII.** Results are quoted at an assumed abundance and
the maximum ionisation fraction: A = 0.2 solar, f_OVII = 1, f_OVIII = 0.5
(arXiv:2507.21719) [src: abstract, Sect. 4.2.1]. The authors chose the
peak values knowingly: off-peak temperatures raise the inferred density,
and "an order–of–magnitude systematic error is possible" [src: Sect.
4.2.1].

### Step 3. Propagate the parameter errors
<!-- key: step-3-propagate-the-parameter-errors -->

For the Lyα forest, the relative error on Ω_b^(HI) is the quadrature sum
of five parameter errors weighted by their exponents in Eq. 9 (1, 0.5 or
0.363): column-density distribution 15%, Γ_H ± 50%, p₁₀₀ ± 50%, T ± 30%,
H₀ ± 5% (arXiv:1112.2706) [src: App. A, Eq. 10]. Result: σ_Ω/Ω = 0.40,
hence Ω_b^(HI)/Ω_b = 0.28 ± 0.11, with 77% of the budget from Γ_H and p₁₀₀
[src: App. A]. Extending the N_HI^(−1.7) distribution from log N = 12.5 to
12.0 would raise the fraction from 28% to 31% if the slope holds [src:
App. A].

### Step 4. Measure the redshift path and dN/dz
<!-- key: step-4-measure-the-redshift-path-and-dn-dz -->

The path over which a line could have been detected is set by spectral
coverage, S/N and the rest wavelength. In the COS cluster-pair survey
(Martínez-Acosta et al. 2026, arXiv:2610.11203) [src: Sect. 3.3–3.4]:

- g(z) = Σ_k H(z − z_k^min) H(z_k^max − z) over M sightlines, with H the
  Heaviside function (Eq. 1), and Δz = ∫ g(z) dz (Eq. 2).
- Masks: flux below 50% of the continuum (against detection on top of
  strong lines) and ±200 km s⁻¹ around expected Galactic lines.
- Minimum detectable rest equivalent width per pixel, printed as
  W_r,min = 3 λ₀R/⟨S/N⟩ with R = 20,000 the COS resolution and ⟨S/N⟩ per
  resolution element; as the width of a resolution element is λ₀/R, the
  intended form is presumably 3λ₀/(R ⟨S/N⟩) [der: dimensional check].
- dN/dz(Δd, Δv, W_r,min) = N/Δz (Eq. 3), with Poisson errors in the
  Gehrels small-number form σ⁺ ≈ √(N + 3/4) + 1, σ⁻ ≈ √(N − 1/4), which
  the authors find to agree with jackknife variance [src: Sect. 3.4,
  footnote 11].
- The field reference is dN/dz|field ≈ N_tot/Δz_tot over 0.1 ≤ z ≤ 0.5
  (Eq. 5), not excluding the cluster-pair windows; excluding them would
  lower the field value and raise the excesses [src: Sect. 3.4, footnote
  12].

Line parameters (z, log N, b) come from Voigt fits with the non-Gaussian
COS line-spread function, and only reliability classes 'a' and 'b' are
kept, so the incidences are lower limits [src: Sect. 3.2]. Equivalent
widths scale as 12.5 mÅ N₁₃ for O VI λ1032 and 54.5 mÅ N₁₃ for Lyα, with
N₁₃ = N/10¹³ cm⁻², and O VII as 2.88 mÅ (N_OVII/10¹⁵ cm⁻²)
(arXiv:1112.2706) [src: Sect. IV].

### Step 5. Test an X-ray line: at a prior redshift
<!-- key: step-5-test-an-x-ray-line-at-a-prior-redshift -->

The FUV-prior strategy searches the X-ray spectrum only at redshifts of
secure FUV systems: O VI with both λλ1031.9, 1037.6 lines detected, or H I
Lyα with b ≥ 40 km s⁻¹ (arXiv:2305.01587) [src: Sect. 2.2]. The stated
reason: if the WHIM is multiphase, the cooler ions fix the redshift and
raise "the statistical significance and the overall credibility" of an
X-ray counterpart; EAGLE shows O VI and O VII column densities correlated
[src: Sect. 2.2].

The detection statistic is ΔC = C − C_min, the rise in the Cash statistic
when the absorber column is fixed at log N = 7 (effectively zero) [src:
Sect. 4.3.2]. Under the null, ΔC ~ χ²(1) for one free column, with
critical values 2.7, 6.6 and 8.8 at 90%, 99% and 99.7% [src: Sect. 4.3.2].
Because the column cannot be negative, the null value sits on the
boundary of parameter space, a condition of the Wilks theorem that fails;
following Protassov et al. 2002, using χ²(1) is then "often (but not
always or necessarily)" conservative [src: Sect. 4.3.2].

### Step 6. Test an X-ray line: found blind
<!-- key: step-6-test-an-x-ray-line-found-blind -->

A line found without a prior must be corrected for the number of
redshift trials (arXiv:2305.01587) [src: Sect. 4.4.1]:

1. **Simulation.** Step a model line, with the XMM-Newton RGS line-spread
   function, across 23.5–32 Å (z ≥ 0 and above the 21.6–23.5 Å Galactic
   O I–O VI region, below the source redshift) in 10 mÅ steps, reduced by
   25% for unusable detector regions to Δλ = 6.4 Å, and record the
   maximum Δχ² (≈ ΔC at ≥ 400 counts per bin) in pure-noise spectra.
2. **Binomial approximation.** N = Δλ/σ_λ independent chances, with σ_λ ≈
   50 mÅ (the RGS resolution), gives N ≈ 127; then P ≈ pN when pN ≪ 1, or
   P = Σ_{i=1}^{N} C(N, i) p^i (1 − p)^(N−i) otherwise, p being the
   single-trial p-value.

Applied to the two 2018 lines towards 1ES 1553+113: z = 0.4339 gives P =
4 × 10⁻⁵, a 4.1σ two-sided equivalent; z = 0.3551, with single-trial p =
0.017, gives P = 0.88 (binomial) or ~0.46 (simulation) [src: Sect.
4.4.1]. The first line's WHIM origin is questioned on other grounds (the
blazar likely sits in a group at z ≈ 0.433), recorded in L2.

### Step 7. Veto non-WHIM absorption, then count
<!-- key: step-7-veto-non-whim-absorption-then-count -->

The 51-source X-ray search (arXiv:2507.21719) [src: abstract; Sect. 3.2]:

- 1,224 FUV-prior systems searched; 34 possible O VII or O VIII systems
  at the 99% level (ΔC ≥ 6.6, p = 0.01, a "2.7σ" equivalent) [src:
  abstract; Sect. 3.2.5].
- Vetoes: Galactic lines and absorption intrinsic to the source [src:
  Sect. 3.2.1–3.2.2 titles]; any
  known galaxy within 1 Mpc on the sky and ±1,000 km s⁻¹ (Δz ≈ ±0.0034)
  of the absorber, as a circumgalactic-medium (CGM) test, e.g. galaxies at
  0.12 Mpc and 50 kpc remove systems [src: Sect. 3.2.3]; low-count spectra
  where ΔC is unreliable [src: Sect. 3.2.4 title].
- Survivors: 7 O VII and 8 O VIII systems; the largest ΔC = 17.9 (p = 2.3
  × 10⁻⁵, "4.2σ") [src: Sect. 3.2.5].
- Double counting: two FUV priors at z = 0.18759 and 0.18775 are not
  resolvable in X-rays (dropping one changes Ω by 0.8%); an O VII and an
  O VIII line at the same z = 0.0902 towards 3C 273 may be one phase [src:
  Sect. 4.2.4].
- Non-detections enter through EAGLE: the probability p_j =
  P(N_OVII > N⁺_OVII | N_OVI) that a sightline with a given O VI (or H I)
  column holds O VII above the upper limit N⁺ (arXiv:2305.01587, Eq. 6)
  [src: Sect. 5.2.1].

### Step 8. State Ω_b and what "missing" means
<!-- key: step-8-state-omegab-and-what-missing-means -->

The reference is Ω_b ≈ 0.05 from BBN deuterium, the CMB and FRBs
(arXiv:2507.21719) [src: Sect. 4.1]. The FUV surveys find "approximately
one half of the expected baryons" in the lower-temperature WHIM, and the
"growing consensus" places the rest in its X-ray-bright, higher-temperature
part [src: Sect. 4.1]. Shull et al. state their census as fractions of
the total, Ω_b^(i)/Ω_b^(tot), with an unaccounted 29 ± 13% [src: Sect. IV
of arXiv:1112.2706]. A census figure is thus defined by (i) the Ω_b it is
divided by, (ii) the components counted as observed, and (iii) the
overlap correction between them (Step 9).

### Step 9. Combine phases without double counting
<!-- key: step-9-combine-phases-without-double-counting -->

Shull et al. combine O VI (17 ± 4%) and BLA (14 ± 7%) into 25 ± 8% for the
WHIM at 5 ≤ log T ≤ 6, an overlap of about a quarter, after the 20–40%
overlap correction between BLA and O VI absorbers of Danforth et al. 2010
[src: App. B of arXiv:1112.2706]. They note a possible, undetermined
overlap of photoionised O VI with the Lyα forest [src: App. B]. The BLA
fraction itself differs by survey: dN/dz = 30 ± 4 (b = 40–150 km s⁻¹, log
N_HI ≥ 13.2, seven sightlines) against 18 ± 11 (seven STIS sightlines),
hence the adopted 14 ± 7% with an inflated error [src: App. B].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Constant or column-dependent ionisation correction
<!-- key: constant-or-column-dependent-ionisation -->

Constant f_OVI (Z/Z☉) = 0.02 gives O VI fractions of 7.2 ± 0.8% (to 30
mÅ) and 8.6 ± 0.7% (to 10 mÅ) from the 111-absorber STIS reanalysis; the
simulation-based N-dependent correction doubles them, to the adopted 17 ±
4% with a systematic inflation (arXiv:1112.2706) [src: Sect. III.1]. The
cost of the second route is model dependence on the simulation's
metallicity field.

### Prior-driven or blind X-ray search
<!-- key: prior-driven-or-blind-x-ray-search -->

Priors remove most redshift trials and raise credibility, but restrict
the census to gas with a detected FUV counterpart and to the redshifts of
those systems (arXiv:2305.01587) [src: Sect. 2.2]. Blind searches need
the look-elsewhere correction of Step 6: a ΔC that is highly significant at
one redshift can be a 46–88% fluctuation once ~127 trials are counted
[src: Sect. 4.4.1].

### Significance threshold for the census
<!-- key: significance-threshold-for-the-census -->

With the 99% threshold, Ω_WHIM,X/Ω_b = 0.83 (+3.99/−0.62) from O VII and
0.79 (+3.08/−0.50) from O VIII (68% level) (arXiv:2507.21719) [src:
abstract]. Excluding uncertain systems: 0.82 (+3.98/−0.62) and 0.68
(+3.04/−0.46); keeping only ΔC ≥ 9 ("3σ"): 0.56 (+1.83/−0.41) and 0.11
(+0.05/−0.04), the O VIII value falling because the two largest-column
systems drop out [src: Sect. 4.2.5, Eqs. 11–12].

### Assumed temperature
<!-- key: assumed-temperature -->

At 0.2 solar, the O VII-based Ω_WHIM,X/Ω_b is 0.84 at log T = 6.0, 1.62 at
6.3, 11.27 at 6.5 and 3623 at 7.0, because f_OVII falls from log f =
−0.01 to −3.64 in collisional ionisation equilibrium; for O VIII it is
45.04, 0.95, 1.24 and 25.33 at log T = 6.0, 6.3, 6.5, 7.0 [src: Table 4
of arXiv:2507.21719]. A census quoted at one temperature therefore needs
the temperature or a line ratio from two ions of one element [src: Sect.
4.2.1; Sect. 5.1 of arXiv:2305.01587].

### One sightline or many
<!-- key: one-sightline-or-many -->

Tilton et al. 2012 used 44 sightlines (Lyα path Δz = 5.38, O VI 6.1) and
Danforth et al. 2016 82 (Lyα Δz ≈ 20, O VI 14.5), whereas the 1ES
1553+113 analysis rests on one sightline with seven prior redshifts, each
with ~30% chance of an X-ray detection; a short path with a detection
"can overestimate" the WHIM density, and a path about ten times longer is
needed to challenge the WHIM hypothesis with upper limits
(arXiv:2305.01587) [src: Sect. 5.4.4].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| (Z/Z☉) f_OVI | 0.015 (N/10¹⁴)^0.70; weighted mean 0.01 (old 0.02) | simulations | arXiv:1112.2706 | Eq. 2, Sect. III.1 |
| O VI integration range | 13.0 ≤ log N_OVI ≤ 15.0 | STIS/COS | arXiv:1112.2706 | Sect. III.1 |
| O VI line frequency | dN/dz ≈ 22.2 (+3.2/−2.4) to 30 mÅ, β = 2.075 ± 0.119 | 111 O VI absorbers | arXiv:1112.2706 | Sect. III.1 |
| H I column slope | β = 1.68 ± 0.03 | Tilton et al. survey | arXiv:1112.2706 | App. A |
| Γ_H(z) | 2.28 × 10⁻¹⁴ (1 + z)^4.4 s⁻¹ | Haardt & Madau fit | arXiv:1112.2706 | Sect. III.2 |
| Lyα forest error | σ_Ω/Ω = 0.40; 77% from Γ_H and p | error propagation | arXiv:1112.2706 | App. A |
| BLA definition | b ≥ 40 km s⁻¹ (T = 9.69 × 10⁴ K b₄₀²) | FUV | arXiv:1112.2706; arXiv:2610.11203 | App. B; abstract |
| O VI + BLA combined | 25 ± 8% (≈ 1/4 overlap) | census | arXiv:1112.2706 | App. B |
| ΔC critical values | 2.7, 6.6, 8.8 (90, 99, 99.7%) | χ²(1) | arXiv:2305.01587 | Sect. 4.3.2 |
| Redshift trials | Δλ = 6.4 Å, σ_λ ≈ 50 mÅ, N ≈ 127 | RGS | arXiv:2305.01587 | Sect. 4.4.1 |
| X-ray sample | 51 sources, 1,224 priors, 34 at 99%, 7 O VII + 8 O VIII kept | XMM, Chandra | arXiv:2507.21719 | abstract |
| CGM veto | galaxy within 1 Mpc and ±1,000 km s⁻¹ | SDSS and literature | arXiv:2507.21719 | Sect. 3.2.3 |
| Survey windows | Δv = ±1,000 km s⁻¹, Δd ≤ 3 Mpc of cluster-pair axis | COS, 10 sightlines | arXiv:2610.11203 | Sect. 3.2 |
| Mask | flux < 50% of continuum; ±200 km s⁻¹ around Galactic lines | COS | arXiv:2610.11203 | Sect. 3.3 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Faint-end extrapolation.** O VI baryons are dominated by N_OVI <
  10^13.5 cm⁻², where some FUSE/STIS lines are "unconfirmed with high-S/N
  data" in COS (arXiv:1112.2706) [src: Sect. III.1, IV]. Test: quote Ω for
  two N_min values; require S/N ≥ 30 for weak-line surveys [src: Sect. IV].
- **Wrong ionisation phase.** O VI also arises in photoionised gas below
  10⁵ K, so not every O VI absorber is WHIM (arXiv:2610.11203) [src: Sect.
  5.4]. Test: require a BLA or a second ion; report the result with the
  phase split.
- **Fake BLAs.** Noise and blends of narrow components mimic broad,
  shallow lines [src: Sect. 5.4 of arXiv:2610.11203]. Test: high S/N and
  component analysis; compare the BLA excess with the narrow-Lyα excess,
  which CGM contamination affects alike [src: Sect. 5.4].
- **CGM counted as IGM.** Sightlines through filaments meet more galaxy
  haloes (arXiv:2610.11203) [src: Sect. 5.4]. Test: galaxy veto within 1
  Mpc and ±1,000 km s⁻¹ (arXiv:2507.21719) [src: Sect. 3.2.3]. The X-ray
  data are insensitive to density, so WHIM and warm CGM at log T = 5–7 are
  not separated by the lines themselves [src: Sect. 4.2.6].
- **Uncorrected trials.** A serendipitous line quoted with its single-trial
  p (arXiv:2305.01587) [src: Sect. 4.4.1]. Test: Step 6.
- **Boundary of parameter space.** Positive-only columns break the χ²
  asymptotics of ΔC [src: Sect. 4.3.2 of arXiv:2305.01587]; calibrate with
  simulations when the result is close to threshold.
- **Temperature and abundance unknown.** An order-of-magnitude systematic
  (arXiv:2507.21719) [src: Sect. 4.2.1, Table 4]. Report Ω as a function
  of f_ion and A, as the authors do.
- **Double counting.** Unresolved FUV priors at nearby z, or O VII and O
  VIII from one phase (arXiv:2507.21719) [src: Sect. 4.2.4]; O VI–BLA
  overlap (arXiv:1112.2706) [src: App. B].
- **Small path.** A single sightline is not a fair sample
  (arXiv:2305.01587) [src: Sect. 5.4.4].
- **Filament association asserted, not tested.** Of the X-ray systems,
  13 lie in the SDSS volume; four likely detections sit within 5 Mpc of a
  filament spine, while six likely detections have no filament that can
  reasonably give their column (arXiv:2507.21719) [src: Sect. 4.3.3]. A
  "WHIM in filaments" claim needs this cross-match on a stated filament
  catalogue.

## Reading list
<!-- key: reading-list -->

- Foundation: Shull, Smith & Danforth 2012, arXiv:1112.2706 — O VI and
  Lyα census equations, simulation-based corrections, error budget, BLA
  overlap (Sect. III, App. A–B).
- Critique: Spence et al. 2023, arXiv:2305.01587 — FUV priors, ΔC
  statistic and its boundary problem, redshift-trial correction, Ω_WHIM,X
  formalism with EAGLE (Sect. 2.2, 4.3–4.4, 5).
- Application: Bonamente et al. 2025, arXiv:2507.21719 — 51-source X-ray
  census, vetoes, threshold and temperature systematics, filament
  cross-match (Sect. 3–4).
- Application: Martínez-Acosta et al. 2026, arXiv:2610.11203 — BLA and O VI
  incidence near cluster pairs: g(z), masks, dN/dz errors, field reference
  (Sect. 3, 5.4).
- Claim: Nicastro et al. 2018, arXiv:1806.08395 — the two O VII absorbers
  (abstract only read this session).
- Forecast: Fisher et al. 2026, arXiv:2605.26907 — NewAthena X-IFU count
  requirements for 3σ and 5σ O VII detections (abstract).
- Review: Walker & Lau 2022, arXiv:2202.07056 — the WHIM as the expected
  reservoir (Sect. 4.7, in L2).

## Not verified
<!-- key: not-verified -->

- Danforth et al. 2016 (HST/COS IGM survey) and Tilton et al. 2012 were not
  found by search; their sightline counts and paths are as quoted by
  arXiv:2305.01587, Sect. 5.4.4.
- The body of arXiv:1806.08395 has no HTML rendering and the PDF could not
  be read; its search method, significance and Ω estimate were not read at
  source.
- Paper I of the 51-source X-ray series (the line search itself) was not
  read; its selection is as summarised in arXiv:2507.21719.
- The NewAthena count requirements (arXiv:2605.26907) were not read beyond
  the abstract, which gives no numbers.
- The results section of arXiv:2610.11203 (the BLA and O VI excesses with
  their significance) was not re-read; the L2 entry gives them from the
  abstract.
