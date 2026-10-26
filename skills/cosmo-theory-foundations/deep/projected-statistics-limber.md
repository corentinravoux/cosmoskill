# Angular power spectra, Limber and non-Limber projection — cosmo-theory-foundations dossier

Scope: how an angular spectrum and its real-space transforms are computed for
clustering, shear, CMB lensing and magnification (kernels, spin prefactors,
units), which variant of the Limber approximation each analysis uses and what
each variant costs, how the three tested non-Limber algorithms work and how
they compare in speed and accuracy, and which approximations bias a Stage-IV
3×2pt fit.
Snapshot: 2026-10-17.
From: Huterer 2023 review (arXiv:2212.05003), Sects. 3.2–3.3; DES Y3 3×2pt
modelling (arXiv:2105.13548), Sect. III.

Already in L2, not repeated here: the LoVerde–Afshordi series (arXiv:0809.5112), its
convergence criteria and the worked case of a σ_z = 0.01 bin; the DES Y3
non-Limber formula for clustering (Eqs. 29–34) and its Limber Eq. 16
(`physics-and-methods.md#limber-approximation-and-angular-power-spectra`);
the Fang et al. LSST Y1 numbers and the headline sizes of Kitching,
Kilbinger and Zhang (`results.md#limber-approximation`,
`systematics.md#limber-and-flat-sky-approximations`). Magnification and
relativistic terms in the counts: `deep/relativistic-wide-angle.md`.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Write every tracer in one form
<!-- key: step-1-write-every-tracer-in-one-form -->

The N5K challenge writes the full spectrum as a triple integral
[src: Leonard et al. 2023, arXiv:2212.04291, Eqs. 1–3]:

C_ℓ^ij = (2/π) ∫∫∫ dχ1 dχ2 dk k² P_ij(k, χ1, χ2) Δ_ℓ^i(k, χ1) Δ_ℓ^j(k, χ2),
Δ_ℓ^i(k, χ) = f_ℓ^i K_i(χ) j_ℓ^(m_i)(kχ),

with j_ℓ^(m) = j_ℓ, j_ℓ', j_ℓ'' or j_ℓ/x² for m = 0, 1, 2, −2. The two tracers
of the challenge [src: Eqs. 7–8]:

| Tracer | f_ℓ | m | K(χ) |
|---|---|---|---|
| Number counts | 1 | 0 | H(z) p_i(z) b_g(z) |
| Weak lensing | sqrt[(ℓ+2)!/(ℓ−2)!] | −2 | (3H0²Ω_m/2a) χ ∫_z^∞ dz' p_i(z') [χ(z') − χ]/χ(z') |

The same kernels as other analyses write them, c = 1 throughout where the
paper says so:

| Kernel | Form | Source |
|---|---|---|
| DES lens efficiency | W^i_κ,g(χ) = (3Ω_m H0²/2c²) ∫_χ^∞ dχ' n^i_g(χ') (χ/a(χ)) (χ' − χ)/χ' | arXiv:2105.13548, Eq. 5 [src] |
| CMB lensing | W_κ(z) = (3/2)Ω_m H0²(1+z) χ(χ_* − χ)/χ_*, Ω_m including neutrinos non-relativistic at low z | ACT DR6 × unWISE, arXiv:2309.05659, Sect. 8.1.2 [src: LaTeX] |
| Galaxies | W_g(z) = H(z) dN/dz | same [src] |
| Magnification | W_μ(z) = (5s_μ − 2)(3/2)Ω_m H0²(1+z) ∫_χ^χ_* dχ' [χ(χ' − χ)/χ'] H(z') dN/dz', s_μ ≡ d log10 N/dm | same [src] |

CCL writes each tracer as a transfer function against the primordial
curvature spectrum, C_ℓ^ab = 4π ∫ (dk/k) 𝒫_Φ(k) Δ_ℓ^a Δ_ℓ^b [src: Chisari et
al. 2019, arXiv:1812.05995, Eq. 21]: density Δ^D = ∫ dz p_z b T_δ j_ℓ(kχ)
(Eq. 22); RSD Δ^RSD = ∫ dz (1+z) p_z T_θ j_ℓ''(kχ)/H (Eq. 25); magnification
Δ^M = −ℓ(ℓ+1) ∫ (dz/H) W^M T_φ+ψ j_ℓ(kχ) with
W^M = ∫_z^∞ dz' p_z(z') [(2 − 5s)/2] r(χ' − χ)/[r(χ') r(χ)] (Eqs. 26–27);
shear Δ^L = −(1/2) sqrt[(ℓ+2)!/(ℓ−2)!] ∫ (dz/H) W^L T_φ+ψ j_ℓ (Eqs. 28–29);
CMB lensing Δ^κ = −[ℓ(ℓ+1)/2] ∫₀^χ_* (dz/H) r(χ_* − χ)/[r(χ) r(χ_*)] T_φ+ψ
(Eq. 31) [src]. T_δ here is the ratio to the primordial Φ, not the
Eisenstein–Hu normalised T(k) (Eqs. 23–24), and the ΛCDM relation
T_δ = −(1+z)T_θ/(H f) = −k² T_φ+ψ/[3H0²Ω_m(1+z)] (Eq. 32) is assumed [src].

Two assumptions sit under all of these. The unequal-time spectrum is taken
as the geometric mean P_ij(k, χ1, χ2) = sqrt[P_ij(k, χ1) P_ij(k, χ2)]
(arXiv:2212.04291, Eq. 4; CCL's factorisable form, arXiv:1812.05995,
Sect. II.4.1) [src]. The Poisson equation ∇²Φ ≈ (3/2)H0²Ω_m a⁻¹δ_m holds,
which "breaks down" for very light massive neutrinos, modified gravity or
non-trivial dark matter or dark energy [src: arXiv:2212.04291, Eq. 6].

### Step 2. Apply Limber where it is safe
<!-- key: step-2-apply-limber-where-it-is-safe -->

Limber replaces j_ℓ(x) ≈ sqrt[π/(2ℓ+1)] δ_D(ℓ + 1/2 − x), or equivalently
uses ∫ dk k² j_ℓ(kχ1) j_ℓ(kχ2) = 2δ(χ1 − χ2)/(πχ1χ2) [src: arXiv:2212.04291,
Eqs. 9–10; same form in CCL Eq. 73]. CCL then computes
C_ℓ^ab = [2/(2ℓ+1)] ∫ dk P_δ(k, z_ℓ) Δ̃_ℓ^a Δ̃_ℓ^b with χ_ℓ = (ℓ + 1/2)/k and
Δ̃^D = p_z b H at z_ℓ, a Limber RSD term
Δ̃^RSD = [(1+8ℓ)/(2ℓ+1)²] p_z f H(z_ℓ) − [4/(2ℓ+3)] sqrt[(2ℓ+1)/(2ℓ+3)] p_z f H(z_ℓ+1),
and Δ̃^M = 3Ω_M,0 H0² [ℓ(ℓ+1)/k²] [(1+z_ℓ)/χ_ℓ] W^M(z_ℓ)
[src: arXiv:1812.05995, Eqs. 74–77]. Limber is least accurate at small ℓ,
when neither tracer is lensing, and "particularly" for cross-correlations of
different clustering bins [src: arXiv:2212.04291, Sect. 2.2].

### Step 3. Get the spin prefactor right (shear)
<!-- key: step-3-get-the-spin-prefactor-right-shear -->

On the sphere the shear coefficients are ₂γ_ℓm = (1/2) ł(ℓ, 2) ψ_ℓm with
ł(ℓ, s) = sqrt[(ℓ+s)!/(ℓ−s)!] [src: Kilbinger et al. 2017, arXiv:1702.05301,
Eqs. 18–19], so C^γ = (1/4) ł²(ℓ, 2) C^ψ (Eq. 21), with C^ψ built from
𝒜 = (3/2)Ω_m(H0/c)² and the lensing efficiency q_i (Eqs. 10–11). The
convergence differs: C^κ = [ℓ(ℓ+1)/((ℓ−1)(ℓ+2))] C^γ, larger by 10% at ℓ = 4,
1% at ℓ = 14, < 0.1% for ℓ > 45 [src: Eq. 24]. In flat sky ł(ℓ, 2) is
replaced by ℓ² (Eq. 29) [src].

Kilbinger et al. (arXiv:1702.05301) combine prefactor p(ℓ) and Limber argument ν(ℓ) in
P^γ_L1 = p(ℓ) 𝒜² ∫ dχ q_i q_j a⁻² P_m(ν(ℓ)/χ; χ) [src: Eq. 43] and compare
seven variants with the full spherical projection, CFHTLenS n(z), flat ΛCDM
(Table 1; "ℓ_0.1" and "ℓ_0.01" are the multipoles beyond which the error is
below 10% and 1% as the text uses them; the caption prints "ℓ ≤ ℓ_x"; arXiv:1702.05301, Table 1) [src]:

| ID | p(ℓ) | ν(ℓ) | ℓ_0.1 | ℓ_0.01 | Used by (as stated) |
|---|---|---|---|---|---|
| L1Fl | 1 | ℓ | 4 | 60 | pre-2014 CFHTLenS, DLS |
| ExtL1Fl | ℓ⁴/(ℓ+1/2)⁴ | ℓ + 1/2 | 20 | 200 | "should not be used" |
| ExtL1FlHyb | 1 | ℓ + 1/2 | 4 | 10 | post-2014 CFHTLenS, DES-SV, KiDS |
| ExtL1Sph | ł²(ℓ,2)/(ℓ+1/2)⁴ | ℓ + 1/2 | 3 | 12 | — |
| ExtL2Fl | ℓ⁴/(ℓ+1/2)⁴ | ℓ + 1/2 | 19 | 200 | — |
| ExtL2FlHyb | 1 | ℓ + 1/2 | 5 | 16 | best flat-sky |
| ExtL2Sph | ł²(ℓ,2)/(ℓ+1/2)⁴ | ℓ + 1/2 | 2 | 5 | best |

Why the "hybrid" beats the "extended flat" case: the spherical prefactor
expands as 1 − 5/(2ℓ²) + O(ℓ⁻³), the flat extended one as 1 − 2/ℓ + 5/(2ℓ²)
+ O(ℓ⁻³), farther from the truth than p = 1 [src: Eqs. 45–46].

### Step 4. Second-order Limber, where first order fails
<!-- key: step-4-second-order-limber-where-first-order -->

C_ℓ = F_ℓ ∫ (dχ/χ) K̃_i K̃_j P_ij(ν/χ, z){1 + ν⁻²[(χ²/2)(K̃_i''/K̃_i +
K̃_j''/K̃_j) + (χ³/6)(K̃_i'''/K̃_i + K̃_j'''/K̃_j)]}, K̃ ≡ K/sqrt(χ), primes
d/dχ [src: arXiv:2212.04291, Eq. 12, which prints K̃_j''/K̃_j in the χ³ bracket
where the symmetry with K̃_i''' requires K̃_j''']. LoVerde & Afshordi set
F_ℓ = 1 (spin 0); Kilbinger et al. give the spin-2 case [src: Sect. 2.2.1].
The series "is not a convergent series over all ℓ", and higher orders in a
divergent range "can and will lead to worse results" [src]. The second-order
term always adds power; in the flat hybrid case, which already overestimates,
it makes things worse [src: arXiv:1702.05301, Sect. 4.1].

### Step 5. Non-Limber where the kernels are narrow
<!-- key: step-5-non-limber-where-the-kernels-are-narrow -->

The three methods of the N5K challenge [src: arXiv:2212.04291, Sect. 4]:

- **matter (FFTLog, two Bessel functions; arXiv:2212.04291).** Expand P in complex power laws
  f(x) = Σ c_n x^(ν_n), ν_n = 2πi n/N + η (Eq. 17); integrals of power laws
  times two Bessel functions are hypergeometric functions, tabulated once;
  C_ℓ = Σ_n ∫₀¹ dt I_ℓ(ν_n, t)[f_n(t) + t^(ν_n−2) f_n(1/t)] (Eq. 18);
  N ≈ 100 suffices; handles scale-dependent bias directly [src].
- **FKEM (CosmoLike).** Split P_δ(k, z1, z2) = D(χ1)D(χ2)P_lin(k, 0) +
  [P_δ − P_lin] (Eq. 19): the linear part becomes single-Bessel FFTLog
  transforms, the non-linear residual goes into Limber with "only sub-percent
  errors on large scales" (Eq. 20). Assumes scale-independent linear growth
  [src: Sect. 4.2].
- **Levin.** Turns the oscillatory integral ∫ dχ h(χ, k) j_ℓ(kχ),
  h = K_i sqrt(P_ij)(kχ)^(m_i), into a linear differential system solved on
  collocation points (Eqs. 25–28) [src: Sect. 4.3].

### Step 6. Transform to real space on the sphere
<!-- key: step-6-transform-to-real-space-on-the-sphere -->

DES Y3 uses curved-sky sums with bin-averaged polynomials [src:
arXiv:2105.13548, Eqs. 17–20]: w^i(θ) = Σ_ℓ [(2ℓ+1)/4π] P_ℓ(cos θ) C^ii(ℓ);
γ_t^ij = Σ_ℓ (2ℓ+1)/[4π ℓ(ℓ+1)] P_ℓ²(cos θ) C^ij_δE(ℓ);
ξ±^ij = Σ_ℓ (2ℓ+1)/[2π ℓ²(ℓ+1)²][G⁺_ℓ,2 ± G⁻_ℓ,2](C^ij_EE ± C^ij_BB); each
P_ℓ replaced by its average over [θ_min, θ_max],
[P_ℓ+1 − P_ℓ−1]/[(2ℓ+1)(cos θ_max − cos θ_min)] (Eq. 20). The flat-sky
alternative is the Hankel pair ξ+ = (1/2π) ∫ dℓ ℓ J_0(ℓθ) P^γ, ξ− with J_4
(arXiv:1702.05301, Eq. 47), against the spherical
ξ± = (1/4π) Σ_ℓ≥2 (2ℓ+1) C^γ d^ℓ_2,±2(θ) with reduced Wigner matrices (Eq. 48)
[src]. Kilbinger et al. note that ł(ℓ, 2) extends to non-integer ℓ, so a
spherical C_ℓ can be fed to a fast Hankel transform [src: Sect. 4.2].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Limber or non-Limber, per probe
<!-- key: limber-or-non-limber-per-probe -->

On the LSST Y10 3×2pt set-up (10 clustering, 5 shear bins; σ_z = 0.03(1+z)
lenses, 0.05(1+z) sources) [src: arXiv:2212.04291, Sect. 3.1]:

- Clustering auto- and adjacent-bin spectra: Limber is off by "a few ten
  per-cent" at low ℓ; all three non-Limber codes bring this to sub-per-cent
  [src: Sect. 5.1].
- Clustering × shear and shear × shear: differences from Limber "a few % of
  the uncertainties at most" [src: Sect. 5.1].
- Even at 200 ≤ ℓ ≤ 1000 (arXiv:2212.04291) first-order Limber failed the accuracy target for
  clustering autocorrelations because of their tiny LSST Y10 errors; the
  winning entry used second-order Limber there [src: Sect. 3.3].
- Broad tracers: for unWISE × ACT DR6 lensing the leading beyond-Limber
  contribution (from RSD) is below 0.1% on all scales used, so Limber is kept
  [src: arXiv:2309.05659, Sect. 8.1.2 footnote].

### Which non-Limber code
<!-- key: which-non-limber-code -->

From arXiv:2212.04291, Sect. 5.1 (run times) and the sections named in the Source column:

| Method | Time, LSST Y10 3×2pt, 64 cores | Strength | Weakness | Source |
|---|---|---|---|---|
| FKEM | 0.437 s | fastest at the target accuracy and across bin numbers | needs a separable linear spectrum: scale-dependent growth or PNG need extra work; parallelises poorly above a fraction of a node; fiducial precision settings failed for narrow bins | arXiv:2212.04291, Sects. 5.1, 5.2.3, 6 |
| matter | 2.00 s | best ℓ ≤ 200 accuracy for narrow bins; run time grows least with spectra count | slower | same |
| Levin | 4.53 s | no factorisation needed | accuracy degrades "dramatically" at half bin width | same |
| CCL Limber | 0.0445 s | — | fails the accuracy target | same |

Target accuracy (arXiv:2212.04291): Δχ² ≈ 0.2 for ℓ < 200, from an original Δχ² ≤ 1 over
2 ≤ ℓ ≤ 2000 chosen because Δχ² = 1 "could in principle correspond to an
erroneous 1σ detection" [src: Sect. 3.3]. Run times exclude
cosmology-independent precomputation [src: Sect. 5.1].

### Flat or spherical shear; Hankel or spherical transform
<!-- key: flat-or-spherical-shear-hankel-or-spherical -->

- Spectrum: all variants agree with the full spherical projection to < 1%
  above ℓ = 100, most to < 0.1%; ExtL2Sph is 15 times faster than the full
  projection (first 18 ℓ) and an order of magnitude below Euclid-like
  cosmic variance at all ℓ [src: arXiv:1702.05301, Sect. 4.1].
- Correlation function (arXiv:1702.05301): the flat Hankel transform is accurate to "better than
  5 (0.2) percent for ξ+ (ξ−)"; ExtL2Sph with the spherical transform is
  "well below one (0.03) percent" for θ < 300 arcmin [src: Sect. 4.2]. The
  abstract summarises the Hankel error as "below two percent"; the body
  figures are larger for ξ+.
- Parameters: negligible for CFHTLenS [src: abstract].

### RSD and the non-linear spectrum in angular clustering
<!-- key: rsd-and-the-non-linear-spectrum-in-angular -->

Zhang et al. 2026 (arXiv:2606.23781) take non-Limber clustering with RSD and
EuclidEmulator2 (HMCode beyond k = 10 h/Mpc) as baseline [src: Sect. 2.2.3]
and switch one approximation at a time (**forecast**) (arXiv:2606.23781) [src: Table 4]:

| Scenario | Δχ², DES-Y3 | Δχ², Rubin harmonic | Bias in (Ω_m, S8), Roman real / harmonic | Rubin real / harmonic |
|---|---|---|---|---|
| Limber | 9.15 | 71.42 | 0.73σ / 0.75σ | 1.79σ / 1.97σ |
| no RSD | 8.90 | 87.09 | 0.70σ / 0.75σ | 2.05σ / 2.31σ |
| HMCode | 0.93 | 6.03 | 0.61σ / 0.56σ | 0.98σ / 1.24σ |
| all three | 12.29 | 79.44 | 0.96σ / 1.12σ | 2.76σ / 3.12σ |

The Limber and no-RSD effects (arXiv:2606.23781) are similar because Limber "strongly
suppresses" the RSD contribution, so RSD is the dominant one; RSD barely
affects γ_t, whose k_∥ ≈ 0 under Limber [src: Sect. 5.3]. Limber errors sit
on large scales that scale cuts keep, hence a larger bias in harmonic space
[src]. The baseline itself is offset from the input by 0.07–0.25σ, their
projection-effect level [src]. CosmoLike and CCL agree to Δχ² = 0.167
(Roman real, 3×2pt, no cuts) [src: Sect. 5.1].

### Magnification coefficient in CMB-lensing cross-correlations
<!-- key: magnification-coefficient-in-cmb-lensing-cross -->

ACT DR6 × unWISE measures s_μ by perturbing the photometry and re-selecting,
then marginalises with a 10% Gaussian prior because s_μ is defined on the
true population and varies with depth by about 5% [src: arXiv:2309.05659,
Sect. 8.1.2]. Observed spectra: C^gg + 2C^gμ + C^μμ and C^κg + C^κμ [src].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| C^κ/C^γ − 1 | 10% (ℓ = 4), 1% (ℓ = 14), < 0.1% (ℓ > 45) | full sky | arXiv:1702.05301 | Eq. 24 |
| Limber variants, ℓ for 1% error | 60 (L1Fl), 10 (ExtL1FlHyb), 5 (ExtL2Sph) | CFHTLenS n(z) | arXiv:1702.05301 | Table 1 |
| Hankel against spherical ξ± | < 5% (ξ+), < 0.2% (ξ−) | CFHTLenS | arXiv:1702.05301 | Sect. 4.2 |
| N5K accuracy target | Δχ² ≈ 0.2 at ℓ < 200 | LSST Y10 | arXiv:2212.04291 | Sect. 3.3 |
| N5K run times | 0.437 s (FKEM), 2.00 s (matter), 4.53 s (Levin), 0.0445 s (Limber) | LSST Y10, 64 cores | arXiv:2212.04291 | Sect. 5.1 |
| FFTLog terms | N ≈ 100 | matter | arXiv:2212.04291 | Sect. 4.1 |
| Limber error, clustering autos at low ℓ | a few tens of per cent | LSST Y10 | arXiv:2212.04291 | Sect. 5.1 |
| Beyond-Limber RSD | < 0.1% | unWISE × ACT DR6 | arXiv:2309.05659 | Sect. 8.1.2 |
| s_μ prior | 10% Gaussian (depth variation ~5%) | unWISE × ACT DR6 | arXiv:2309.05659 | Sect. 8.1.2 |
| (Ω_m, S8) bias from Limber (**forecast**) | 0.73–0.75σ Roman; 1.79–1.97σ Rubin | 3×2pt | arXiv:2606.23781 | Table 4 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **ν = ℓ with a flat prefactor ℓ⁴/(ℓ+1/2)⁴.** O(ℓ⁻¹) convergence, 10% only
  at ℓ > 20 (arXiv:1702.05301, Table 1). Kilbinger et al. also record that the
  "+0.5" was missing from the printed Limber equation of two cosmic-shear
  papers although their analyses used it [src: Sect. 4.1, footnote 4]: read
  the code, not the printed equation.
- **Convergence for shear.** C^κ is not C^γ at low ℓ (Eq. 24); a code that
  uses one for the other errs by 10% at ℓ = 4 (arXiv:1702.05301, Eq. 24).
- **Second-order Limber over a divergent range.** Makes results worse
  (arXiv:2212.04291, Sect. 2.2.1); in the flat hybrid case it worsens an
  overestimate (arXiv:1702.05301, Sect. 4.1).
- **FKEM outside its factorisation.** Scale-dependent growth (massive
  neutrinos, modified gravity) or PNG breaks Eq. 19 (arXiv:2212.04291,
  Sects. 4.2, 6). Test: compare with matter or Levin, which do not factorise.
- **Precision settings tuned on the fiducial binning.** FKEM's settings
  "failed dramatically" for narrower bins until doubled (arXiv:2212.04291,
  Sect. 5.2.3). Test: rerun at half and quarter bin width.
- **Limber RSD read as "RSD included".** In Limber, RSD is strongly
  suppressed (arXiv:2606.23781, Sect. 5.3); turning RSD on without non-Limber
  integration does not capture the effect the Δχ² table measures.
- **Unbinned real-space prediction.** DES averages P_ℓ over each θ bin
  (arXiv:2105.13548, Eq. 20); a point evaluation at bin centres is a different
  model.
- **Code differences below the noise.** CosmoLike against CCL gives
  Δχ² ≈ 0.1–0.2 for Roman 3×2pt (arXiv:2606.23781, Sect. 5.1); a smaller
  approximation effect cannot be claimed from one code.
- **Validity of ΛCDM transfer relations.** CCL ties T_θ and T_φ+ψ to T_δ
  (Eq. 32) and did not support RSD with massive neutrinos at release
  (arXiv:1812.05995, Sect. II.4.1).

## Reading list
<!-- key: reading-list -->

- Foundation: LoVerde & Afshordi 2008, arXiv:0809.5112 — the series and its
  convergence (in L2).
- Method: Kilbinger et al. 2017, arXiv:1702.05301 — spin prefactors, seven
  Limber variants, Hankel against spherical ξ±.
- Method: Leonard et al. 2023, arXiv:2212.04291 — matter, FKEM, Levin compared
  at LSST Y10 accuracy.
- Method: Fang et al. 2020, arXiv:1911.11947 — FKEM with RSD and
  magnification (in L2).
- Code: Chisari et al. 2019, arXiv:1812.05995 — CCL transfer functions and
  Limber RSD and magnification terms.
- Application: Krause et al. 2021, arXiv:2105.13548 — DES Y3 kernels,
  curved-sky bin-averaged transforms.
- Application: Farren et al. 2023, arXiv:2309.05659 — CMB lensing and
  magnification kernels, s_μ prior.
- Critique: Zhang et al. 2026, arXiv:2606.23781 — Limber, RSD and non-linear
  spectrum biases for Roman and Rubin.

## Not verified
<!-- key: not-verified -->

- G±_ℓ,2 of the DES ξ± sums: defined in Eq. 4.19 of a reference of
  arXiv:2105.13548, not read.
- Kitching et al. 2017 (arXiv:1611.04954) body: only the abstract-level
  statements of L2 are available; their exact replacement of the Hankel step
  was not read.
- Accuracy of Limber for CMB lensing × narrow spectroscopic bins: not found;
  the < 0.1% statement is for unWISE's broad samples (arXiv:2309.05659, Sect. 8.1.2 footnote).
- Angpow (CCL's beyond-Limber option): named in arXiv:1812.05995, Sect.
  III.3.2, not read.
