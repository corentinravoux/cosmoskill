# Relativistic projection effects, magnification and wide-angle terms — cosmo-theory-foundations dossier

Scope: how the observed number-count fluctuation is written with the sample
selection made explicit (magnification and evolution bias), in which gauge the
bias is defined, how the coefficients are measured for a real sample, how the
terms are computed in the angular spectrum and in the correlation function, how
the relativistic dipole of two populations is isolated, and what neglecting
each term costs.
Snapshot: 2026-10-17.
From: Ivanov 2026 lecture notes (arXiv:2607.28314), Sect. 6.1; DES Y3
magnification modelling (arXiv:2105.13548, Sect. II); BOSS DR12 wide-angle
analysis (arXiv:1810.05051).

Already in L2, not repeated here: the Bonvin–Durrer expression without
selection effects and the name of each term
(`physics-and-methods.md#relativistic-and-wide-angle-terms`); the DES Y3
δ_g,μ = C_g κ_g form; the BOSS DR12 wide-angle sizes
(`systematics.md#wide-angle-relativistic-and-line-of-sight`); the threshold
Θ ≳ 30° and the SPHEREx f_NL headline (`results.md#wide-angle-and-relativistic-terms`).
The estimator side of wide-angle terms (line of sight, window, odd multipoles
through the window) is in `cosmo-galaxy-clustering/deep/estimators-window.md`;
the magnification term of photometric 3×2pt in modified gravity in
`cosmo-dark-energy-modified-gravity/deep/nonlinear-beyond-lcdm.md`.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Write the count for the sample actually selected
<!-- key: step-1-write-the-count-for-the-sample-actually -->

The L2 expression counts all sources. A flux- or magnitude-limited sample adds
terms set by the slope of the luminosity function. Challinor & Lewis 2011
(arXiv:1105.5292) work in the conformal-Newtonian gauge with
ds² = a²(η)[(1+2ψ)dη² − (1−2φ)δ_ij dx^i dx^j] [src: Eq. 6], so ψ is the
temporal and φ the spatial potential, η conformal time, ℋ = a'/a, χ comoving
distance, v the Newtonian-gauge velocity, κ the convergence. For all sources
with m < m_*, "neglecting only local terms" [src: Sect. IV, Eq. 37]:

Δ_N(n̂, z, m < m_*) = δ_N(L > L̄_s*) − (1/ℋ) n̂·∂v/∂χ + (5s − 2)[κ − (1/χ) ∫^η_A (φ + ψ) dη]
 + [(2 − 5s)/(ℋχ) + 5s − ∂ln[a³N̄(L > L̄_s*)]/(ℋ∂η) + ℋ̇/ℋ²][ψ + ∫^η_A (φ̇ + ψ̇) dη − n̂·v] + (1/ℋ) φ̇ + ψ + (5s − 2) φ,

with the local count slope

s(z, m_*) ≡ ∂log10 N̄(z, m < m_*)/∂m_* = n̄_s(η, ln L̄_s*)/[2.5 N̄(η, L > L̄_s*)] [src: Eq. 38],

N̄ the background density of sources brighter than the threshold, and "no
line-of-sight scattering" assumed [src: Sect. IV].

The same result in the notation of the CLASSgal paper (Di Dio et al. 2013,
arXiv:1307.1459), which the Euclid papers copy, with Bardeen potentials Ψ
(temporal) and Φ (spatial), primes for conformal-time derivatives, r_S the
comoving distance to the source, sources seen "in direction −n" [src: Sect. 2]:

Δ^(N)(n, z, m_*) = D_g(L > L̄_*) + (1 + 5s)Φ + Ψ + (1/ℋ)[Φ' + ∂_r(V·n)]
 + (ℋ'/ℋ² + (2 − 5s)/(r_S ℋ) + 5s − f^N_evo)(Ψ + V·n + ∫₀^r_S dr (Φ' + Ψ'))
 + [(2 − 5s)/(2r_S)] ∫₀^r_S dr [2 − ((r_S − r)/r) Δ_Ω](Φ + Ψ) [src: Eq. 10],

with f^N_evo = ∂ln[a³ N̄(z, L > L̄_*)]/(ℋ ∂τ_S) and s as in Eq. 11, identical to
Challinor & Lewis Eq. 38 [src: Eqs. 10–12]. Two remarks from the source: the
dominant RSD term "does not depend on luminosity nor evolution", while the
lensing term does ("the so called magnification bias") [src: Sect. 2]; and
with s = 0, f_evo = 0 Eq. 10 reduces to the all-source Eq. 8 [src].

Three equivalent ways of writing the magnification amplitude:

| Symbol | Definition | Lensing coefficient | Paper |
|---|---|---|---|
| s | ∂log10 N̄/∂m_* | 5s − 2 (multiplies κ) | arXiv:1105.5292, Eqs. 37–38; arXiv:1307.1459, Eq. 11 |
| α | 2.5 d log N_μ(m)/dm, N_μ the lensed cumulative count | 2(α − 1) | DES, arXiv:2209.09782, Eqs. 13–14 |
| C = C_area + C_sample | C_area = −2; C_sample the response of the selected number to κ | C | DES, arXiv:2209.09782, Eq. 12 |
| 𝒬 | −d ln n̄_g(> L_min)/d ln L_min | −2(1 − 𝒬) | Lukens & Jeong 2026, arXiv:2608.18334, Eqs. 3.26, 3.29 |

Hence 5s − 2 = 2(α − 1) = C = 2(𝒬 − 1), i.e. α = 𝒬 = 5s/2 when "log" is
log10 [der: CLASSgal states ∂ln N̄/∂ln L = −(5/2)s, arXiv:1307.1459, Sect. 2].
Magnification vanishes at s = 2/5 [src: arXiv:2311.03168, footnote 12].

### Step 2. Put the bias in the right gauge
<!-- key: step-2-put-the-bias-in-the-right-gauge -->

- **Comoving/synchronous.** Challinor & Lewis take δ_n^syn = b δ_m^syn,
  "since it is the comoving perturbation … that enters directly into the
  Poisson equation", and convert: δ_n = b δ_m^syn + [d ln(a³n̄_s)/dη − 3ℋ] v/k
  [src: arXiv:1105.5292, Eq. 31]. CLASSgal does the same through
  D_g = D − 3(ℋV/k + Φ) [src: arXiv:1307.1459, Eq. 13], replacing D_g by
  bD + (f^N_evo − 3)ℋV/k − 3Φ, justified because "galaxies and dark matter
  follow the same velocity field" [src: Sect. 2].
- **Synchronous-comoving throughout.** Lukens & Jeong write the whole count in
  that gauge, metric a²{−dτ² + [(1 + 2D)δ_ij + 2E_ij]dx^i dx^j} [src: Eq. 3.24],
  observed contrast b_g δ_m + b_e δz − (1/aH)∂²_∥E' + 2(1 − 𝒬)φ − φ'/(aH) − …
  − 2(1 − 𝒬)κ [src: Eq. 3.26], with GR closure ∇²φ = −a²H²[f + (3/2)Ω_m]δ,
  ∇²E' = −aHfδ, ∇²E'' = −a²H²[(3/2)Ω_m − f]δ [src: Eqs. 3.34–3.36].
- **What Challinor & Lewis reject.** Yoo et al.'s linear bias in the
  zero-redshift-perturbation gauge: bias "is physically due to the local
  physics of structure formation, and nothing to do with how we observe it"
  [src: arXiv:1105.5292, Sect. III].
- **When it matters.** Gauge differences are O(ℋ²/k²) (Bonvin, Hui &
  Gaztañaga 2014, arXiv:1309.1321, footnote to Eq. 28); the Newtonian–synchronous
  difference becomes important for k ≪ 0.01 Mpc⁻¹ [src: arXiv:1105.5292, Fig. 1
  caption].

### Step 3. Measure the magnification coefficient of the sample
<!-- key: step-3-measure-the-magnification-coefficient-of -->

- **Magnitude-limited mock (Euclid spectroscopic).** Cumulative counts at m_*
  and m_* ± 0.04 in each of 13 bins, logarithmic derivative by Eq. 5, variance
  from 100 jackknife regions; s grows with z because a fixed apparent limit
  is a brighter intrinsic limit at high z [src: arXiv:2311.03168, Sect. 3.2].
  Convenience fit s(z) = 1.231 − 1.746z + 1.810z² − 0.505z³ (and b(z)) for
  that binning only; "we do not use these fits" in the calculations
  [src: App. B, Eqs. 27–29].
- **Real photometric selection (DES Y3).** Balrog image simulations re-run
  with a constant magnification δμ = 1.02 (δκ ~ 0.01), large enough to move
  enough objects across thresholds, small enough that κ² terms are ~10⁻⁴
  [src: arXiv:2209.09782, Sect. 5.1]; statistical error from Eq. 25; a
  systematic from the difference between flux-perturbation estimates on data
  and on Balrog [src: Sect. 5.4]. The Balrog values are smaller than the
  flux-only ones, especially at 0.3 ≲ z ≲ 0.6, attributed to selection on
  size (star–galaxy separation) and photometric systematics [src: Sect. 5.4].
- Why simulation: "galaxy selection can be complex in detail (i.e. not simply
  a threshold in total galaxy flux)" [src: Sect. 2.1].

### Step 4. Decide the evolution bias
<!-- key: step-4-decide-the-evolution-bias -->

- Definitions: f_evo(z) = d ln(a³n̄_S)/(ℋ dτ_S) = −(1+z) d/dz ln[n̄_S/(1+z)³]
  (arXiv:1307.1459, Sect. 2) and b_e = d ln(a³n̄_g)/d ln a (arXiv:2608.18334,
  Eq. 3.8) [src]. CLASSgal sets f_evo = 0 by default "since f_evo(z) is very
  uncertain" [src: Sect. 2].
- With a universal mass function, b_e = δ_c f (b_g − 1), δ_c = 1.686
  [src: arXiv:2608.18334, Eqs. 3.8–3.9]; Lukens & Jeong instead derive b_e and
  𝒬 from the WISE luminosity function for their forecast [src: Sect. 5.5].
- Consistency check: for the total counts (W ∝ n̄) the velocity terms
  integrate to −∫ dη (1+z) n̄ n̂·v̇, of order v rather than kv/ℋ, so all
  source-velocity terms must be kept together, "since these nearly cancel"; the
  near cancellation "is a useful numerical consistency check"
  [src: arXiv:1105.5292, Sect. V.1, Eqs. 45–47].

### Step 5. Compute the statistic
<!-- key: step-5-compute-the-statistic -->

- **Angular spectrum.** C_ℓ(z1, z2) = 4π ∫ (dk/k) 𝒫(k) Δ_ℓ(z1, k) Δ_ℓ(z2, k)
  [src: arXiv:1307.1459, Eq. 17], 𝒫 the primordial spectrum and Δ_ℓ the
  transfer function of Eq. 18: j_ℓ times density and potential terms, j_ℓ' and
  j_ℓ'' times velocity (the Kaiser term is the one ∝ j_ℓ'' k/ℋ), and a
  line-of-sight integral for lensing and ISW-like terms [src: Eq. 18]. The
  code was valid for K = 0 only at release [src: Sect. 2]. CAMB sources is the
  Challinor–Lewis implementation (camb.info/sources) [src: arXiv:1105.5292,
  Sect. I]. PowerFull extends the 2-FAST FFTLog algorithm to the full
  relativistic C_ℓ with local f_NL [src: arXiv:2608.18334, Sect. 4].
- **Correlation function, spectroscopic.** Euclid models the multipoles of
  ξ with coffe; C_ℓ would need "more than 1000 bins" at δz ≲ 10⁻³ and has
  large auto-spectrum shot noise; the curved-sky local terms follow Szalay et
  al. 1998 and Szapudi 2004, the integrated (lensing) terms need the method of
  Tansella et al. 2018 [src: arXiv:2311.03168, Sect. 2.1–2.2]. Magnification
  in a power-spectrum estimator "requires non-trivial extensions" [src:
  Sect. 2.2].
- Local monopole and dipole terms are dropped for consistency (arXiv:1307.1459,
  Sect. 2); the observer-velocity dipole is 3n̂·v_oA − n̂·v_oA (1/ℋ) d ln n̄/dz
  and vanishes in the CMB frame [src: arXiv:1105.5292, Eq. 29]; Lukens & Jeong
  use ℓ_min = 2 for that reason [src: Sect. 5.5].

### Step 6. Isolate the relativistic dipole with two populations
<!-- key: step-6-isolate-the-relativistic-dipole-with-two -->

Bonvin, Hui & Gaztañaga keep terms to order ℋ/k [src: arXiv:1309.1321,
Eq. 28]. For a bright (B) and a faint (F) population at separation d, lowest
order in d/r, flat background [src: Eq. 47]:

ξ^rel(r, d, β) = [2A/(9Ω_m²π²)] (ℋ/ℋ0) D1² f {ν1(d) P1(cos β)[(ℋ̇/ℋ² + 2/(rℋ))(b_B − b_F) + (1/(rℋ) − 1)(5(s_B b_B − s_F b_F) + 3(s_B − s_F) f)] + ν3(d) P3(cos β) 2(1 − 1/(rℋ))(s_B − s_F) f},

with ν_ℓ(d) = ∫ (dk/k)(k/H0)³(kη0)^(n_s−1) T²(k) j_ℓ(kd), f = d ln D1/d ln a
[src: Eq. 48]. It is antisymmetric and vanishes when b_B = b_F and s_B = s_F:
"it is essential to have two distinct populations"; with s ≠ 0 an octupole
appears [src: Sect. III.1]. Relativistic contributions to even multipoles are
suppressed by ℋ/k and by d/r; the dipole has no d/r suppression [src].

Contamination and its removal [src: Sect. IV.1–IV.2.1]: standard plus lensing
dipoles contaminate the relativistic one by 47% at d = 50 h⁻¹Mpc for z_B =
0.25, 83% at z_B = 2. The wide-angle part is removed model-independently by
measuring the quadrupoles of B and F separately: their difference,
−[2A/(9π²Ω_m²)](4/3)(b_B − b_F) D1² f μ2(d) P2(cos β) [src: Eq. 66], times
3d/(10r) equals the wide-angle dipole term; the residual contamination falls to
5%, 9%, 15%, 29% at z_B = 0.25, 0.5, 1, 2. The same correction, with opposite
sign, applies to the octupole [src].

### Step 7. Wide-angle terms in the even multipoles
<!-- key: step-7-wide-angle-terms-in-the-even-multipoles -->

Castorina & White 2018 (arXiv:1709.09730) use the bisector line of sight and
x ≡ s/d (s pair separation, d distance to the pair) [src: Sect. 2.1, Eq. 12]:

- L_ℓ(cos θ/2) ≃ 1 − x² ℓ(ℓ+1)[1 − μ²]/16 [src: Eq. 14]: geometric
  corrections start at O(x²); x ≃ 0.045 for a BAO-scale pair at z = 1 [src].
- Plane-parallel limit, written with f only and with ξ_ℓ^(n)(s, d) =
  ∫ k² dk/(2π²) (kd)^(−n) P(k) j_ℓ(ks) without i^ℓ: ξ_2^pp = ξ_2^(0)(−(4/3)f −
  (4/7)f²) [src: Eqs. 17–18 and footnote 3]. The minus sign is the missing i^ℓ,
  not a physical difference from Hamilton's multipoles (L2 section 7).
- Geometric O(x²) terms (Eq. 19), e.g. ξ_0 ∋ −(4f²/45)x² ξ_0^(0) −
  [f(9+f)/45]x² ξ_2^(0); selection-function terms for a uniform sample
  (α(s) = 2) start at O(x) and enter only ℓ = 0, 2, e.g. ξ_0 ∋ (4f²/3)ξ_0^(2)
  + (2/3)f(1−f)x ξ_1^(1) [src: Eq. 20].
- The two partly cancel for a uniform sample, "an accidental cancellation";
  for full-shape modelling at 1% accuracy wide-angle terms "can be safely
  neglected"; at the BAO scale, out-of-phase leakage from ℓ' ≠ ℓ reaches "the
  percent level or even larger" at low redshift, best handled inside the
  template [src: Sect. 2.1].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Full relativistic, Newtonian or Kaiser model
<!-- key: full-relativistic-newtonian-or-kaiser-model -->

For SPHEREx-like f_NL (Fisher, five samples, ℓ_max = 250, Planck priors on
n_s, α_s, A_s; **forecast**): neglecting relativistic terms shifts f_NL by
⟨Δf_NL⟩ ≃ 1.3 σ, of order unity in absolute terms, plateauing beyond ℓ ~ 100
because the Doppler and potential terms and local PNG all carry inverse
powers of k; dropping only the extra Doppler term ("Newtonian") is
"negligible by comparison" [src: arXiv:2608.18334, Sect. 5.5]. Caveat stated:
small parameter space, b_φ from universality [src]. For even multipoles on
sub-Hubble scales the large-scale relativistic terms "do not significantly
impact" the analysis; Euclid omits them and keeps magnification [src:
arXiv:2311.03168, Sect. 2.1, footnote 1, which also notes that Eq. 4 assumes
the Euler equation but not Einstein's equations].

### Magnification: model, template or neglect
<!-- key: magnification-model-template-or-neglect -->

| Analysis | Neglecting magnification | Including it | Source |
|---|---|---|---|
| Euclid photometric clustering (**forecast**) | shifts up to 1.6σ; 3×2pt up to 6σ | 1σ errors on Ω_m, w0, wa reduced 20–35% (clustering alone); no gain in 3×2pt | arXiv:2110.05435 [src, abstract] |
| Euclid spectroscopic ξ_ℓ (**forecast**) | ΛCDM shifts 0.4–0.7σ; w0waCDM < 0.5σ; growth rate up to 1.2σ in the highest bin | S/N of the magnification term 0.50, 0.92, 1.52, 2.50 at z̄ = 1.00, 1.20, 1.40, 1.65 (ℓ_m = 4) | arXiv:2311.03168 [src: abstract, Table 3] |
| Euclid spectroscopic, template method | — | template computed at cosmologies ±1σ from the fiducial: shifts ≤ 0.08σ (ΛCDM), ≤ 0.11σ on f̃_i | arXiv:2311.03168 [src: Sect. 5.4, Tables 6–8] |

The template "does not encode any cosmological information" and keeps the
growth-rate analysis model-independent, at the price of the lensing
information, "not very significant" [src: arXiv:2311.03168, Sect. 5.4].

### Magnification coefficient: fixed, Gaussian or free
<!-- key: magnification-coefficient-fixed-gaussian-or-free -->

DES Y3 tested C_sample fixed to Balrog, C_sample = 2 (no magnification), a
Gaussian prior of the Balrog statistical width, and flat priors [src:
arXiv:2209.09782, Sect. 6]. Adding the cross-clustering between lens bins
"significantly improves the constraints on lens magnification parameters and
allows uninformative priors … without any loss of constraining power or prior
volume concerns" [src: abstract]. Magnification is "a significant systematic
for the MagLim sample" [src: abstract]; it dominates widely separated bin
pairs (e.g. bins 1 × 6) and high-z lens–source pairs [src: Sect. 6].

### Bias gauge
<!-- key: bias-gauge -->

Challinor & Lewis find a "significantly smaller difference" between full and
"standard" results (Eq. 49: Δ_std = bδ_m^syn − (1/ℋ)n̂·∂v/∂χ − (2 − 5s)κ) than
Yoo et al., mainly from the bias treatment, but still "several percent on the
largest scales" and more for the CMB cross-correlation [src:
arXiv:1105.5292, Sect. V.2]. Replacing δ_N^syn by the Newtonian δ_N gives a
change "significantly larger than the difference between the standard and full
results" [src: Fig. 5 caption].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Lensing coefficient | 5s − 2 = 2(α − 1) = C; null at s = 2/5 | all | arXiv:1105.5292; arXiv:2209.09782; arXiv:2311.03168 | Eqs. 37; 12–13; fn. 12 |
| C_sample, DES MagLim (Balrog) | 2.43, 2.30, 3.75, 3.94, 3.56, 4.96 (six bins, 0.2 < z < 1.05) | DES Y3 | arXiv:2209.09782 | Table 1 |
| C_sample, DES redMaGiC (Balrog) | 2.63, −1.04, 0.67, 4.50, 3.93 (0.15 < z < 0.9) | DES Y3 | arXiv:2209.09782 | Table 2 |
| Balrog magnification step | δμ = 1.02, κ² terms ~10⁻⁴ | DES Y3 | arXiv:2209.09782 | Sect. 5.1 |
| s(z) fit | 1.231 − 1.746z + 1.810z² − 0.505z³ | Euclid spec., Flagship | arXiv:2311.03168 | Eqs. 28–29 |
| s step for the derivative | ± 0.04 mag, 100 jackknives | Euclid spec. | arXiv:2311.03168 | Sect. 3.2 |
| Universal-mass-function b_e | δ_c f (b_g − 1), δ_c = 1.686 | PowerFull | arXiv:2608.18334 | Eq. 3.9 |
| f_NL shift without relativistic terms (**forecast**) | 1.3σ at ℓ_max = 250 | SPHEREx-like | arXiv:2608.18334 | Sect. 5.5 |
| Dipole contamination before / after wide-angle correction | 47% → 5% (z = 0.25), 83% → 29% (z = 2), d = 50 h⁻¹Mpc | linear theory | arXiv:1309.1321 | Sect. IV.1–IV.2.1 |
| Lensing share of ξ_4 for one population | 5% at d ≳ 100, 35% at d ≳ 200 h⁻¹Mpc; < 1% of ξ_0, ξ_2 | linear theory | arXiv:1309.1321 | Sect. IV.1 |
| Wide-angle parameter | x = s/d ≃ 0.045, BAO pair at z = 1 | — | arXiv:1709.09730 | Sect. 2.1 |
| Dipole detection in mocks (**forecast**) | 4σ and 3σ in the two lowest bins, ≈ 6σ total, signal below 30 h⁻¹Mpc | Euclid Flagship | arXiv:2410.06268 | abstract |
| Dipole detection in data | 2.7σ (shell estimator), 2.8σ (dipole), ~10 h⁻¹Mpc; varies by 0.5σ with choices | BOSS DR12 CMASS | arXiv:1709.07855 | abstract |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Sign of the Doppler term.** Challinor & Lewis use n̂ as the line-of-sight
  direction and write −n̂·v; CLASSgal sees sources "in direction −n" and
  writes +V·n (arXiv:1105.5292, Eq. 37; arXiv:1307.1459, Eq. 10) [der: same
  physics]. Test: reproduce the sign of the relativistic dipole for b_B > b_F,
  positive in arXiv:1309.1321, Sect. IV.1 ("stronger for faint galaxies behind
  the bright galaxy").
- **log10 against ln.** s is per magnitude in log10; 𝒬 and α per ln L or per
  magnitude with 2.5: mixing them changes the lensing amplitude by a factor
  of order 2.5 [der from the definitions above].
- **Flux-only slope for a complex selection.** DES Balrog C_sample is smaller
  than the flux-only estimate, and negative in redMaGiC bin 2 [src:
  arXiv:2209.09782, Table 2, Sect. 5.4]. Test: an image-simulation response.
- **Magnification parameters absorbing other systematics.** The posterior
  C_sample of MagLim bin 3 lies far above every estimate, and bin 6 is ~3σ low;
  the authors ascribe this to other systematics [src: Sect. 8.3]. Test:
  cross-clustering between lens bins, which the baseline did not use.
- **Inconsistent evolution and RSD terms.** "Much larger differences can be
  obtained" than the true relativistic correction [src: arXiv:1105.5292,
  Sect. V.2]. Test: for W ∝ n̄, the velocity terms must nearly cancel
  (Eq. 47).
- **Synchronous δ rescaled with D.** The Newtonian-gauge δ_n grows more slowly
  on large scales because of the ℋḊ velocity term; rescaling it with the
  synchronous growth factor is incorrect [src: arXiv:1105.5292, Fig. 1
  caption].
- **Linear dipole model at small separation.** The dipole turns over near
  20 h⁻¹Mpc in N-body, absent from linear predictions, captured by a
  non-perturbative model whose key ingredient is the pairwise potential
  difference (Dam & Bonvin 2025, arXiv:2506.22431) [src, abstract]; in the
  Euclid mocks the small-scale signal is dominated by the non-linear potential
  (arXiv:2410.06268) [src, abstract].
- **Even-multipole contamination misread.** Lensing reaches 35% of ξ_4 at
  200 h⁻¹Mpc while staying below 1% of ξ_0, ξ_2 (arXiv:1309.1321): the
  hexadecapole is the first even multipole to check.
- **i^ℓ convention.** Castorina & White's ξ_ℓ^(n) omit i^ℓ (footnote 3), so
  their plane-parallel quadrupole carries a minus sign.

## Reading list
<!-- key: reading-list -->

- Foundation: Challinor & Lewis 2011, arXiv:1105.5292 — counts with flux
  limit (Eq. 37), bias gauge (Eq. 31), total-count cancellation (Eq. 47).
- Foundation/code: Di Dio et al. 2013, arXiv:1307.1459 — CLASSgal transfer
  function Eq. 18, f_evo and s conventions.
- Method: Bonvin, Hui & Gaztañaga 2014, arXiv:1309.1321 — two-population
  dipole, wide-angle correction by quadrupole differences.
- Method: Castorina & White 2018, arXiv:1709.09730 — O(x) and O(x²)
  wide-angle terms with selection function.
- Application: Elvin-Poole et al. 2022, arXiv:2209.09782 — C_sample from
  image simulations, prior choices, cross-bin clustering.
- Application: Euclid Collaboration 2023, arXiv:2311.03168 — s(z) from
  mocks, magnification in ξ_ℓ, template method.
- Forecast: Lepori et al. 2021, arXiv:2110.05435 — magnification in
  photometric clustering and 3×2pt.
- Forecast: Lukens & Jeong 2026, arXiv:2608.18334 — synchronous-comoving
  count, b_e and 𝒬, f_NL shift.
- Test: Alam et al. 2017, arXiv:1709.07855 — first measured asymmetry, BOSS
  CMASS. Lepori et al. 2024, arXiv:2410.06268 — dipole detectability in Euclid
  mocks.
- Critique: Dam & Bonvin 2025, arXiv:2506.22431 — non-linear dipole.

## Not verified
<!-- key: not-verified -->

- The coefficients R_1 to R_6 of arXiv:1309.1321 (App. B) and its standard
  dipole Eq. 52: not read.
- Yoo, Fitzpatrick & Zaldarriaga 2009 and Jeong, Schmidt & Hirata 2012 bodies:
  not read; the gauge debate is given from Challinor & Lewis's side and from
  the O(ℋ²/k²) statement of arXiv:1309.1321.
- The flux limit and sample of the Euclid s(z) fit, and the per-bin values of
  Table 2 of arXiv:2311.03168: not read.
- Whether the f in b_e = δ_c f(b_g − 1) (arXiv:2608.18334, Eq. 3.9) is the
  growth rate or a different factor: the equation was read, its symbol list
  was not.
- How current CAMB and CLASS releases expose s and the evolution bias: no
  code documentation read.
