# Physics and methods — CMB × LSS cross-correlations

Scope: what each cross-correlation measures, the estimators and models in current use, covariance, blinding, codes and conventions.
Snapshot: 2026-10-13

Flags: `[src]` read this session in the cited paper; `[sec]` from a named secondary source; `[der]`
derived here. Equations given without a flag are textbook definitions. CMB lensing reconstruction
itself (quadratic estimators, N0/N1 biases, the lensing auto-spectrum) belongs to `cosmo-cmb`.

## 1. Why cross-correlate
<!-- key: why-cross-correlate -->

A CMB secondary is a line-of-sight integral over all redshifts. Correlating it with a tracer of
known redshift does three things:

1. It selects the redshift slice of the integral (tomography).
2. It removes additive noise and systematics that the two maps do not share. DES uses the CMB
   lensing cross-correlations as consistency tests of its own galaxy lensing and clustering, and
   they point to problems in the redMaGiC and high-redshift MagLim samples (Abbott 2022,
   arXiv:2206.10824) [src]. For f_NL, the κ–galaxy spectrum is preferred to the galaxy
   auto-spectrum "given its stability in terms of observational systematics" (Bermejo-Climent
   2024, arXiv:2412.10279) [src].
3. It breaks degeneracies. The galaxy auto-spectrum scales as b²σ_8² and the cross-spectrum with
   lensing as bσ_8², so the pair fixes σ_8 and the bias b separately [der, linear bias on linear
   scales]. The kSZ and tSZ cross-correlations do the same for electron density and pressure.

The price is that every nuisance of the tracer (redshift distribution, magnification, bias model,
imaging systematics) enters the cosmological result. Most of the history of this field is the
history of those nuisances (`results.md` §7).

## 2. CMB lensing × galaxies and quasars
<!-- key: cmb-lensing-x-galaxies-and-quasars -->

**Origins.** The convergence map comes from a quadratic estimator: Hu 2001
(arXiv:astro-ph/0111606) builds minimum-variance estimators of the intervening mass from the six
quadratic combinations of the temperature and polarisation fields; Okamoto 2003
(arXiv:astro-ph/0301031) derives the full-sky version; the review is Lewis 2006
(arXiv:astro-ph/0601594) [src: abstract]. CMB lensing was first detected in cross-correlation: 3.4σ from
WMAP quadratic estimators × NVSS radio counts (Smith 2007, arXiv:0705.3980), then 2.5σ evidence
with SDSS LRGs, quasars and NVSS combined (Hirata 2008, arXiv:0801.0644) [src: abstract]. With ground-based
maps: SPT × optical and infrared galaxy catalogues over 17–68 deg², each at > 4σ (Bleem 2012,
arXiv:1203.4808); ACT × SDSS photometric quasars at 3.8σ (Sherwin 2012, arXiv:1207.4543) [src: abstract].
The unWISE tomography starts with Krolewski 2019 (arXiv:1909.07412): three samples at median
z ≈ 0.6, 1.1, 1.5, S/N = 79.3 over 100 < ℓ < 1000 with Planck, and the finding that
magnification bias must be included [src: abstract].

### 2.1 Observables
<!-- key: observables -->

In the Limber approximation, as written in Sailer 2024 (arXiv:2407.04607, section "From 3D to
2D") [src]:

```
C_ℓ^gg = ∫ dχ/χ² { [W^g]² P_gg(k,z) + 2 W^g W^μ P_gm(k,z) + [W^μ]² P_mm(k,z) }
C_ℓ^κg = ∫ dχ/χ²  W^κ { W^g P_gm(k,z) + W^μ P_mm(k,z) },        k = (ℓ + 1/2)/χ

W^g(χ) = H(z) φ(z)                                   φ ∝ dN/dz, ∫ φ dz = 1
W^κ(χ) = (3/2) Ω_m H_0² (1+z) χ (χ_* − χ)/χ_*          χ_* = distance to last scattering
W^μ(χ) = (5 s_μ − 2) (3/2) Ω_m H_0² (1+z) ∫_z^∞ dz' χ(z) [χ(z') − χ(z)]/χ(z') φ(z')
```

s_μ is the slope of the cumulative number counts at the magnitude limit. The same paper evaluates
P_gg and P_gm at a single effective redshift per bin,
z_eff = ∫ dχ z [W^g]²/χ² / ∫ dχ [W^g]²/χ², which it finds accurate to sub-percent for its narrow
LRG bins; beyond-Limber corrections are dominated by redshift-space distortions at ℓ ≲ 75 [src].

Sizes for the DESI LRG bins: magnification is below 1% of C_ℓ^gg and at most ≃ 10% of C_ℓ^κg, in
the highest-redshift bin (arXiv:2407.04607) [src: Sect. 4.5]. For broad or high-redshift samples the
magnification term is larger and the number-count slope is a calibrated input, published with the
sample (Zhou 2023, arXiv:2309.06443) [src].

The Limber approximation (Limber 1953, doi:10.1086/145672 [sec: title and year from Crossref,
paper not read]) is the leading term of a series in 1/(ℓ + 1/2): its error is O(1/ℓ²), and a
second-order term brings it to O(1/ℓ⁴), which matters for narrow redshift bins (LoVerde 2008,
arXiv:0809.5112) [src]. Magnification of number counts was detected at 8σ in the SDSS
galaxy–quasar cross-correlation, with the change of sign expected from the slope of the quasar
counts (Scranton 2005, arXiv:astro-ph/0504510) [src]. For a sample with a complex or implicit
selection the standard slope estimate may not apply, and the bias is calibrated on the selection
itself (von Wietersheim-Kramsta 2021, arXiv:2101.05261) [src].

### 2.2 Theory models in current use
<!-- key: theory-models-in-current-use -->

| Model | Used by | Stated range |
|---|---|---|
| Linear theory with conservative scale cuts | Qu 2024 (arXiv:2410.10808): "a scale cut where non-linear effects are negligible" | linear regime only [src] |
| Perturbation theory, restricted to large scales | White 2021 (arXiv:2111.09898) | large scales [src] |
| Hybrid EFT (HEFT): Lagrangian bias expansion on N-body displacements, emulated | Sailer 2024 (arXiv:2407.04607, Aemulus ν emulator); Kim 2024 (arXiv:2407.04606); Sailer 2025 (arXiv:2503.24385); Rubiola 2025 (arXiv:2510.09563) | k_max = 0.6 h/Mpc in arXiv:2407.04606 [src: abstract]; 79 ≤ ℓ < 600 for the galaxy auto-spectra in arXiv:2407.04607 [src: Sect. 6.6] |
| Hybrid model with marginalisation over higher-order biases | Farren 2023 (arXiv:2309.05659) | validated on mocks [src] |
| One-loop Eulerian bias for P, tree-level for the bispectrum | Verdiani 2025 (arXiv:2510.17796) | k_max^P ≃ 0.2 h/Mpc, k_max^B ≃ 0.08 h/Mpc [src: abstract] |
| EFT of LSS, joint with 3D full shape and bispectrum | Ivanov 2026 (arXiv:2601.16165) | — |
| Linear bias with scale cuts, or non-linear bias | Chang 2022 (arXiv:2203.12440): two sets of scale cuts | S/N 23.9 or 25.7 [src: abstract] |

HEFT in arXiv:2407.04607 adds 16 nuisance parameters for four bins (b_2^L, b_s^L and two
counterterms per bin) to a 30-dimensional posterior [src]. That is where projection ("volume")
effects come from; see `systematics.md` §6. The hybrid model is that of Kokron 2021
(arXiv:2101.11014): N-body dynamics with an analytic Lagrangian bias expansion, emulated with
Aemulus over 0 ≤ z ≤ 2 [src]; arXiv:2407.04607 takes from it the sub-percent accuracy to
k = 0.6 h/Mpc for haloes of LRG mass [src: Sect. 5.1].

### 2.3 What is quoted
<!-- key: what-is-quoted -->

- S_8 = σ_8(Ω_m/0.3)^0.5, the galaxy-lensing convention.
- S_8^× or S_8^3x2pt = σ_8(Ω_m/0.3)^0.4, the best-constrained combination of the κ–galaxy data
  (arXiv:2407.04606, arXiv:2409.02109) [src: abstract].
- σ_8, after a BAO prior fixes Ω_m.
- σ_8(z) or S_8^×(z) per bin: the growth history (arXiv:2402.05761, arXiv:2407.04606) [src].
- The amplitude at redshifts above the tracers, from the lensing auto-spectrum once the
  cross-correlations have fixed the low-redshift part: a 3.3% constraint above z = 2.4 (Farren
  2024, arXiv:2409.02109) and σ_8(z̃ = 5.1) (Embil Villagra 2025, arXiv:2507.08798) [src: abstract].

The CMB lensing auto-spectrum itself constrains S_8^CMBL ≡ σ_8(Ω_m/0.3)^0.25 (arXiv:2304.05203,
Sect. I and footnote 2; see `cosmo-cmb`). ACT DR6 lensing alone with BAO gives σ_8 = 0.819 ± 0.015 and S_8 = 0.840 ± 0.028
(Madhavacheril 2023, arXiv:2304.05203) [src: abstract]. Four exponents (this one, the two above, and
the one of lensing × tSZ in `#thermal-sunyaev-zel-dovich-x-lss`) circulate in this domain.

### 2.4 Lensing map normalisation in cross-correlation
<!-- key: lensing-map-normalisation-in-cross-correlation -->

A lensing reconstruction made on a masked sky is misnormalised. Auto-spectrum analyses correct
this with Monte Carlo simulations; for a cross-correlation the correction is

```
A_ℓ^MC = C_ℓ(κ_in masked by κ mask × κ_in masked by galaxy mask) / C_ℓ(κ̂ × κ_in masked by galaxy mask)
```

and it depends on the overlap region, so it cannot be taken from the auto-spectrum analysis
(arXiv:2309.05659, appendix on the Planck reanalysis) [src]. In practice the footprint
dependence is below 1% for Planck × unWISE, where the correction itself is about 2%
[src: App. "Lensing Monte Carlo Norm Correction"]; sizes are in `systematics.md` §1. Earlier cross-correlation papers
omitted it; restoring it raised S_8 by 0.6σ for unWISE × Planck and by 0.015 for DESI LRG × Planck
PR3 (arXiv:2309.05659, arXiv:2407.04607) [src].

### 2.5 Redshift distributions
<!-- key: redshift-distributions -->

Photometric tracers need dN/dz from outside. unWISE uses cross-correlation redshifts against
spectroscopic samples; these depend on the fiducial cosmology assumed when measuring them, which
arXiv:2309.05659 corrects for explicitly, and their uncertainty is marginalised with principal
components [src]. The DESI LRG and BGS imaging samples are calibrated directly with DESI spectra
(arXiv:2309.06443, arXiv:2407.04607) [src]. Quaia has per-object spectro-photometric redshifts
from Gaia BP/RP spectra improved with a k-nearest-neighbour model trained on SDSS (Storey-Fisher
2023, arXiv:2306.17749) [src].

### 2.6 Derived tests
<!-- key: derived-tests -->

- **f_NL (local).** Scale-dependent bias Δb ∝ f_NL b_φ/k², with b_φ ∝ (b − p). Analyses quote
  p = 1 and p = 1.6 side by side (arXiv:2504.20992, arXiv:2512.17865) [src: abstract]. The κ–galaxy
  spectrum is used alone or with the auto-spectrum above an ℓ_min cut (arXiv:2412.10279) [src: abstract].
- **E_G.** The ratio of a lensing cross-spectrum to a velocity (RSD) measurement of the same
  galaxies; in GR it equals Ω_m,0/f(z) and is scale independent. With ACT DR6 and BOSS it is
  consistent with GR and with scale independence (PTE > 5%), with 3–4% systematic errors
  (Wenzl 2024, arXiv:2405.12795) [src: abstract]. Proposed by Zhang 2007 (arXiv:0704.1932) as the ratio
  of the Laplacian of the Newtonian potentials to the peculiar-velocity divergence; first
  measured with galaxy–galaxy lensing, E_G = 0.39 ± 0.06 on tens of Mpc (Reyes 2010,
  arXiv:1003.2185); the CMB-lensing estimator, from C_ℓ^κg, C_ℓ^gg and β, is Pullen 2014
  (arXiv:1412.4454); its first use, Planck × CMASS, gave E_G(z = 0.57) = 0.243 ± 0.060 (stat)
  ± 0.013 (sys), 2.6σ below GR, the deviation lying above 80 Mpc/h (Pullen 2015,
  arXiv:1511.04457) [src: abstract].
- **Sound-horizon-free H_0.** The shape of the lensing and galaxy spectra carries the
  matter–radiation equality scale (arXiv:2409.02109, arXiv:2506.22416, arXiv:2410.24134) [src].
- **Variance cancellation.** A third tracer can remove structure from κ before the
  cross-correlation, giving the gain of a joint analysis without modelling that tracer:
  10–20% lower variance with the CIB or LRGs on Planck data (Baleato Lizancos 2023,
  arXiv:2301.10242) [src: abstract].
- **Galaxy magnification as a growth probe.** Cross-correlating non-overlapping photometric bins
  isolates magnification; detected at 11σ for BGS × LRG (arXiv:2503.24385) [src: abstract].
- **Stacking on voids and superstructures**, compared with mock templates through an amplitude
  A_κ (Sartori 2026, arXiv:2605.19763; Hang 2021, arXiv:2105.11936) [src].

### 2.7 What the main analyses did
<!-- key: what-the-main-analyses-did -->

Columns: Farren 2023, arXiv:2309.05659 (left), and Sailer 2024, arXiv:2407.04607 (right); the place read is given in each cell.

| | unWISE × ACT DR6 (arXiv:2309.05659) | DESI LRG × PR4 + ACT DR6 (arXiv:2407.04607) |
|---|---|---|
| Estimator | pseudo-C_ℓ (MASTER: Hivon 2001, arXiv:astro-ph/0105302) with NaMaster (Alonso 2018, arXiv:1809.09603), HEALPix nside 2048; the mode-coupling mask for κ is the square of the ACT mask, accurate to better than 1%, with a simulated transfer function for the residual [src: Sect. 4] | NaMaster mask-deconvolved bandpowers, edges linear in √ℓ; 9 (Planck κg), 8 (ACT κg) and 7 (gg) bandpowers per bin [src: Sect. 3] |
| Range | κg 50 ≤ ℓ ≤ 400; gg 100 ≤ ℓ ≤ 400 [src: Sect. 4] | 20 or 44 ≤ ℓ < 600 (κg), 79 ≤ ℓ < 600 (gg) [src: Sect. 5.1] |
| Model | HMCode matter spectrum plus higher-order Lagrangian (CLEFT) terms; per sample: linear bias, offsets to the fiducial evolution of the quadratic and shear biases, s_μ, shot noise [src: Sect. 8.1.5] | HEFT with the Aemulus ν emulator; per bin: b_1^L, b_2^L, b_s^L, s_μ, shot noise, counterterms α_a, α_x [src: Sect. 5.2] |
| Cosmology priors | Ω_m in [0.01, 0.95], ln(10¹⁰A_s) in [1, 4]; fixed n_s = 0.9665, Ω_b h² = 0.02242, Ω_m h³ = 0.09635 (proxy for θ_MC), Σm_ν = 0.06 eV [src: Sect. 9.3, table] | ln(10¹⁰A_s) in U(2, 4), Ω_c h² in U(0.08, 0.16); fixed n_s = 0.9649, Ω_b h² = 0.02236, Ω_m h³ = 0.09633, Σm_ν = 0.06 eV [src: Sect. 5.2] |
| Nuisance priors | b_1 flat; c_2,L, c_s,L Gaussian; log₁₀ P_shot Gaussian of width 0.2; s_μ 10%; three (Blue) and five (Green) dN/dz principal-component coefficients with skew-normal priors [src: Sect. 9.3, table] | b_1^L U(0, 3); b_2^L U(−5, 5); b_s^L N(0, 1); shot noise 30%; s_μ ± 0.1; α_a N(0, 50) h⁻²Mpc²; α_x tied to α_a through ε ~ N(0, 2) h⁻²Mpc² [src: Sect. 5.2, table] |
| Covariance | 400 Gaussian simulations with Hartlap factor; analytic blocks between the two samples [src: Sect. 6] | analytic Gaussian (NaMaster) as a cross-check of the companion paper's hybrid covariance; neighbouring bandpowers correlated by at most 4% [src: Sect. 3] |
| Blinding | parameters blinded, spectra not; model must recover N-body inputs within 0.5σ; null tests pass at PTE > 0.05; consistency runs with random offsets added to the parameters; scales and priors frozen before unblinding [src: Sect. 9.1] | ACT cross-spectrum and ACT-derived parameters blinded until cuts, priors, null tests and mock fits were final; no fiducial choice changed after unblinding [src: Sect. 7.1] |

Two analyses built differently:

| Analysis | Estimator and range | Blinding |
|---|---|---|
| DES Y3 × SPT + Planck (arXiv:2203.12440) | real space with TreeCorr, 2.5′ < θ < 250′; ⟨δ_g κ⟩ with a random-catalogue term subtracted, ⟨γ_t κ⟩ divided by the metacalibration response [src: Sect. 4] | shear catalogue multiplied by a secret factor, then data vectors shifted; unblinding required the systematics tests and posterior-predictive p-values above 0.01 for the fit and for the consistency of the SPT + Planck and Planck-only patches [src: Sect. 5] |
| E_G, ACT DR6 × BOSS (arXiv:2405.12795) | C_ℓ^κg reweighted to the effective redshift of C_ℓ^gg and β (a percent-level, scale-dependent error otherwise); the non-Gaussian distribution of the ratio is kept [src: Sect. 6.3] | analysis choices fixed before unblinding, sensitivity tests run afterwards [src: Sect. 6.3] |

## 3. Kinematic Sunyaev–Zel'dovich effect
<!-- key: kinematic-sunyaev-zel-dovich-effect -->

### 3.1 Signal
<!-- key: signal -->

ΔT/T_CMB = −∫ dχ a σ_T n_e (v_e · n̂)/c. The signal has the blackbody spectrum of the CMB, so
frequency information cannot isolate it, and it is odd in the line-of-sight velocity, so it
averages to zero in a plain stack. Its typical size where it peaks is ~0.1 μK against ~100 μK
of primary anisotropy (as stated in Ried Guachalla 2025, arXiv:2503.19870) [src: Sect. IV.2]. Every estimator
supplies the velocity sign from the galaxy survey.

**Origins.** The effect is that of Sunyaev 1980 (doi:10.1093/mnras/190.3.413 [sec: title and year
from Crossref, paper not read]). Reviews of the SZ effects: Birkinshaw 1998
(arXiv:astro-ph/9808050), Carlstrom 2002 (arXiv:astro-ph/0208192), Mroczkowski 2018
(arXiv:1811.02310) [src].

Smith 2018 (arXiv:1810.13423) shows that five estimators then in use are all equivalent to the
optimal ⟨ggT⟩ bispectrum estimator and that the bispectrum carries two observables: the
small-scale galaxy–electron spectrum P_ge(k_S), which is astrophysics, and the large-scale
galaxy–velocity spectrum P_gv(k), which is cosmology [src].

### 3.2 Estimators
<!-- key: estimators -->

| Estimator | Needs | Returns | Reference |
|---|---|---|---|
| Pairwise | positions and redshifts of groups; aperture photometry | mean pairwise momentum ∝ τ̄ × pairwise velocity v_12(r) | Hand 2012, arXiv:1203.4219; Calafut 2021, arXiv:2101.08374 [src] |
| Velocity-weighted stacking | a 3D velocity reconstruction | stacked profile ∝ τ(R); gas density profile | Schaan 2015, arXiv:1510.06442; Schaan 2020, arXiv:2009.05557 [src] |
| Hybrid stacking | spectroscopic velocities interpolated to photometric objects | same, with the photometric number density | Mallaby-Kay 2023, arXiv:2305.06792 [src] |
| Projected field | no redshifts; cleaned CMB map, filtered and squared, × projected galaxies | A_kSZ², sensitive to f_b f_free | Hill 2016, arXiv:1603.01608; Kusiak 2021, arXiv:2102.01068 [src] |
| Velocity reconstruction | quadratic estimator in small-scale T × small-scale δ_g | large-scale radial velocity map, up to the bias b_v | McCarthy 2024, arXiv:2410.06229; Chaussidon 2026, arXiv:2604.04867 [src] |
| Harmonic-space momentum template | velocity-weighted galaxy template × T | P_ge bandpowers, nearly uncorrelated | Qu 2026, arXiv:2604.19744; Hotinli 2026, arXiv:2609.17676 [src] |

Where each estimator comes from [src, abstracts]:

| Estimator | Proposed in |
|---|---|
| Pairwise | Ferreira 1998 (arXiv:astro-ph/9812456): the mean pairwise velocity v_12 estimated from line-of-sight velocities, sensitive to σ_8² Ω^0.6. With Planck: 1.8–2.5σ on foreground-cleaned maps around SDSS central galaxies at z ≈ 0.1 (Planck Collaboration 2015, arXiv:1504.03339) [src: abstract] |
| Velocity-weighted template | Ho 2009 (arXiv:0903.2845): reconstructed velocity field × galaxy field as a kSZ template |
| Projected field | Doré 2003 (arXiv:astro-ph/0309337): kSZ × cosmic shear, strength scaling roughly as σ_8⁷; DeDeo 2005 (arXiv:astro-ph/0511060): tomographic galaxy counts; Ferraro 2016 (arXiv:1605.02722): squared filtered map × projected tracers, **forecast** S/N ≈ 3 (Planck), 120 (Advanced ACTPol), > 150 (Stage IV) with WISE, statistical errors only [src: abstract] |
| Velocity reconstruction ("kSZ tomography") | Terrana 2016 (arXiv:1610.06919) and Deutsch 2017 (arXiv:1707.08129): the statistically anisotropic part of the CMB–tracer correlation encodes the CMB dipole seen by the electrons; Cayuso 2021 (arXiv:2111.11526): quadratic estimators for the radial (kSZ) and transverse (moving lens) velocity |

**Stacking, as implemented for DESI × ACT** (arXiv:2503.19870, section "Methodology") [src].
Velocities come from the linearised continuity equation with the redshift-space term,
∇·v + (f/b) ∇·[(v·n̂) n̂] = −aHf δ_g/b, solved as in BAO reconstruction (v = aHf ψ); the paper
reuses the DESI Y1 BAO reconstruction displacements (smoothing 15 h⁻¹Mpc, b = 2.0) after removing
the RecSym (1 + f) factor. The compensated aperture photometry (CAP) filter is

```
𝒯(R) = ∫_0^R d²θ δT(θ) − ∫_R^{√2 R} d²θ δT(θ)

T̂_kSZ(R) = −(1/r) (σ_v^rec/c) Σ_i 𝒯_i(R) (v_i^rec/c) / Σ_i (v_i^rec/c)²
```

where r is the correlation coefficient between true and reconstructed velocities, taken as 0.65
for a DESI-like spectroscopic sample from earlier simulation work, with a ~2% uncertainty that
the paper neglects [sec: as quoted in arXiv:2503.19870]. The CAP output approximates the
cumulative gas profile as R grows. The covariance comes from 10,000 bootstrap resamplings of the
catalogue, and S/N = sqrt(χ²_null − χ²_best-fit) [src]. The photometric analysis uses the same
filter (its Eq. for W_θd) in nine apertures from 1′ to 6′, about 0.4–2.9 Mpc over its four bins,
the uniform-mean estimator above with r from mocks, the ThumbStack pipeline and 10,000 bootstrap
resamplings (arXiv:2407.07152) [src: Sect. 3.2].

**Velocity reconstruction** (arXiv:2604.04867, section "kSZ Velocity Bias") [src]. The estimator
obeys ⟨v̂_r(x)⟩ = b_v B(x) n_v(x) v_r^true(x), with

```
b_v(χ) = ∫ d²L b_L F_L P_ge^true(L/χ) / ∫ d²L b_L F_L P_ge^fid(L/χ)
```

so b_v = 1 only if the fiducial small-scale galaxy–electron spectrum is right. The LRG fit of
the P_gv dipole has four parameters (f_NL, b_v at 90 and 150 GHz, a damping Σ_v), reaches
k_min = 0.0014 Mpc⁻¹, and gives SNR = 17.05 with χ² = 37.76 for 52 degrees of freedom; P_vv adds
three noise-rescaling parameters [src: Sect. 5.2, table of LRG fits]. The integral is
dominated by small scales, b_v is effectively constant on the scales analysed, and it is
marginalised as a free amplitude. The fiducial P_ge in that paper is a halo model (hmvec) with an
abundance-matching HOD and the Battaglia AGN electron profile, in which the baryon fraction
reaches the cosmic value at the virial radius [src]. "b_v", "A" (arXiv:2506.21684) and "A_kSZ²"
(arXiv:2102.01068) are all amplitudes relative to a fiducial gas model and are comparable only if
the fiducial models are the same.

**Pairwise, as written in arXiv:2511.23417** [src: Sect. III.2, III.3, Eqs. 8–10, 14].

```
p̂_kSZ(r) = − Σ_{i<j} (ΔT_i − ΔT_j) c_ij / Σ_{i<j} c_ij²,   c_ij = r̂_ij · (r̂_i + r̂_j)/2
V(r,z) = −(2/3) f(z) H(z) r/(1+z) × ξ̄_h(r,z)/[1 + ξ_h(r,z)],   p̂_th = −(T_CMB/c) τ̄ V(r,z)
```

ΔT is aperture photometry minus its mean, so the fitted depth is an attenuated τ̄_AP. Bins are
10 Mpc wide from 5 to 145 Mpc plus four wider ones to 355 Mpc; r < 20 Mpc is dropped because
the linear V fails there; the covariance is a bootstrap with 1000 iterations, the jackknife
overestimating it.

**Pairwise.** The amplitude is turned into a mass-averaged optical depth by comparing the measured
curve with the linear-theory pairwise velocity of a fixed cosmology (arXiv:2101.08374,
arXiv:2511.23417) [src], or with a pairwise velocity measured from reconstructed, machine-learnt
velocities (Gong 2026, arXiv:2609.36355) [src].

**Projected field.** Needs foreground-cleaned maps, because nothing cancels tSZ or dust, and a
marginalisation over the CMB lensing contribution to the same statistic (arXiv:2102.01068) [src].

### 3.3 From a kSZ profile to a feedback statement
<!-- key: from-a-ksz-profile-to-a-feedback-statement -->

1. Convert the stacked signal to an electron profile around galaxies (CAP or harmonic bandpowers).
2. Assign host halo masses. The cross-spectrum "does not itself measure" them
   (arXiv:2609.17676) [src]. Current practice: CMB lensing of the same galaxies (Hadzhiyska 2025,
   arXiv:2507.14136), galaxy–galaxy lensing (Bigwood 2025, arXiv:2510.15822; Siegel 2025,
   arXiv:2509.10455), an HOD with its uncertainty (arXiv:2604.19744), or the lensing-to-kSZ ratio
   with one ΔΣ-type filter applied to both, which yields f_gas(R) without a profile model (Liu
   2026, arXiv:2609.22466) [src].
3. Compare with hydrodynamical simulations selected like the data, or fit a gas model
   (baryonification, GNFW) and propagate to the matter power suppression (Bigwood 2024,
   arXiv:2404.06098; Siegel 2025, arXiv:2512.02954) [src].

Combining kSZ (density) with tSZ (pressure) of the same objects gives the electron temperature,
measured to 20% for CMASS (arXiv:2009.05557), and the feedback energetics (Amodeo 2020,
arXiv:2009.05558) [src: abstract]. Stacked tSZ with a ȳ–τ̄ relation gives optical depths that can be
checked against the pairwise kSZ values (Moore 2026, arXiv:2609.08939) [src: abstract].

### 3.4 Cosmology from the large-scale velocity field
<!-- key: cosmology-from-the-large-scale-velocity-field -->

The reconstructed velocity traces the matter field without galaxy bias, so v × g cancels sample
variance for the scale-dependent bias and constrains f_NL (arXiv:2511.15701, arXiv:2604.04867)
[src]. Pairwise velocities test the force law (Gallardo 2026, arXiv:2604.14327) [src]. Growth
(fσ_8) is not obtained: the amplitude is degenerate with τ or b_v. The velocity side of this is
developed in `cosmo-peculiar-velocities`.

Proposals to break the degeneracy: a low-scatter relation between optical depth and tSZ signal
within an aperture, found in hydrodynamical simulations with a sub-grid systematic below 10%
(Battaglia 2016, arXiv:1607.02442); fast radio bursts (Madhavacheril 2019, arXiv:1901.02418)
[src: abstract]. What the cosmology programme promised: growth rate to sub-1% out to z ≈ 1 from kSZ cluster
velocities and reconstructed velocities (Alonso 2016, arXiv:1604.01382, **forecast**); f_NL from
the unbiased large-scale velocity field (Münchmeyer 2018, arXiv:1810.13424, **forecast**) [src: abstract].

## 4. Thermal Sunyaev–Zel'dovich × LSS
<!-- key: thermal-sunyaev-zel-dovich-x-lss -->

y = (σ_T/m_e c²) ∫ P_e dl, with a known non-blackbody spectrum, so a Compton-y map can be built by
component separation.

**Origins.** The effect: Sunyaev 1970 (doi:10.1007/BF00653471 [sec: title and year from Crossref,
paper not read]). Halo model: Komatsu 2002 (arXiv:astro-ph/0205468) predicts the tSZ C_ℓ from a
universal gas profile and the halo mass function with no free parameter; C_ℓ ∝ σ_8⁷ (Ω_b h)²,
dominated by 20–40% of the virial radius [src: abstract]. Pressure profiles behind the models: the
universal profile of 33 REXCESS clusters of 10¹⁴–10¹⁵ M⊙ (Arnaud 2009, arXiv:0910.1234) and
profiles from SPH simulations (Battaglia 2011, arXiv:1109.3711) [src: abstract]. y maps: the first all-sky
map, from the Planck 100–857 GHz channels (Planck Collaboration 2013, arXiv:1303.5081); the 2015
maps, from 30–857 GHz (Planck Collaboration 2015, arXiv:1502.01596) [src: abstract]. First tSZ × CMB
lensing: 6.2σ with a Planck ILC y map, σ_8(Ω_m/0.282)^0.26 = 0.824 ± 0.029 (Hill 2013,
arXiv:1312.4525); stacking and cross-correlation of y with groups: Vikram 2016
(arXiv:1608.04160) [src: abstract].

The cross-correlations in use:

| Statistic | Constrains | Reference |
|---|---|---|
| galaxies × y, large scales | bias-weighted mean electron pressure ⟨b_h P_e⟩(z), in meV cm⁻³ | Pandey 2019, arXiv:1904.13347; Sánchez 2022, arXiv:2210.08633 [src] |
| spectroscopic reference × multi-frequency intensity maps | ⟨bP_e⟩ to z ~ 1 with uncorrelated bins; the thermal history; a mass bias B = 1.27 (1 − b = 0.79) for the Planck universal pressure profile | Chiang 2020, arXiv:2006.14650 [src: abstract] |
| galaxies × multi-frequency maps, tSZ and CIB fitted together | ⟨bP_e⟩ and ⟨bρ_SFR⟩ jointly | La Posta 2026, arXiv:2603.04269 [src] |
| shear × y | pressure profile, feedback, and cosmology through σ_8(Ω_m/0.3)^0.2 | Van Waerbeke 2013, arXiv:1310.5721; Tröster 2021, arXiv:2109.04458; Gatti 2021, arXiv:2108.01600; Pandey 2025, arXiv:2506.07432 [src: abstract] |
| CMB lensing × y | intermediate-mass (10¹³–10¹⁴ h⁻¹M⊙), z ≲ 1.5 gas | McCarthy 2023, arXiv:2308.16260 [src: abstract] |
| stacked y on groups and clusters | integrated pressure; ȳ–τ̄ relation | arXiv:2609.08939 [src] |

In the FLAMINGO simulations ⟨b_h P_e⟩ ∝ S_8^ε with ε ≈ 3 over 0.1 ≤ z ≤ 1, and stronger feedback
raises ⟨b_h P_e⟩, opposite to its effect on small-scale gas fractions (Salcido 2026,
arXiv:2605.11083) [src: abstract]. The statistic is therefore a steep but feedback-degenerate amplitude
probe.

The (1 − b) of arXiv:2006.14650 is defined against the Planck pressure profile; the comparison
with cluster-count values, which depend on the reference mass, is in `cosmo-clusters`.

Component separation choices that matter here: needlet ILC with CIB deprojection; moment
deprojection, which protects against a wrong CIB spectral shape (arXiv:2308.16260) [src]; and
fitting the components at the level of the multi-frequency cross-spectra instead of the map
(Wayland 2026, arXiv:2609.31774; Zhao 2026, arXiv:2606.28099) [src]. As written in
arXiv:2506.07432 [src: App. "Impact of systematics"], the tSZ spectrum is f_ν = x coth(x/2) − 4
with x = hν/k_B T_CMB; the deprojected CIB is a modified blackbody
g_ν ∝ (ν/ν_0)^(3+β) / [exp(hν/k_B T_CIB) − 1] × (dB/dT at T_CMB)⁻¹, and the moment component is
the same expression multiplied by ln(ν/ν_0). That analysis measures ξ_γt,y with treecorr in 20
logarithmic bins from 2.5′ to 250′, with Gaussian priors on the redshift shifts Δz and shear
calibrations m of the four source bins [src: Sect. 2.1].

## 5. Integrated Sachs–Wolfe effect
<!-- key: integrated-sachs-wolfe-effect -->

ΔT/T = 2 ∫ dη ∂Φ/∂η (in units with c = 1): a decaying potential, as under dark energy, leaves a
positive correlation between temperature and overdensity on large angular scales. It is detectable
only in cross-correlation, and the signal-to-noise is bounded by cosmic variance of the primary
CMB: the highest significance among the works cited here is 4.7–5.0σ, from five catalogues in
redshift bins (Stölzner 2017, arXiv:1710.03238) [src: abstract].

**Origins.** Sachs 1967 (doi:10.1086/148982) and Rees 1968 (doi:10.1038/217511a0) [sec: titles
and years from Crossref, papers not read]. Crittenden 1995 (arXiv:astro-ph/9510072) proposed the
cross-correlation: with a cosmological constant a significant part of the large-scale anisotropy
arises at z < 1 from evolving potentials, "an effect first noted by Rees and Sciama", and
correlates with tracers of the local matter density [src: abstract]. First reported correlations: WMAP ×
HEAO-1 hard X-ray background at 2.5–3.0σ and × NVSS at 2–2.5σ (Boughn 2003,
arXiv:astro-ph/0305001) [src: abstract]. WMAP-era combinations: ~4.5σ (Giannantonio 2008, arXiv:0801.4380);
a tomographic likelihood over z ~ 0.1–2.5 with b(z) dN/dz fitted per sample (Ho 2008,
arXiv:0801.0642) [src: abstract]. Review: Nishizawa 2014 (arXiv:1404.5102) [src: abstract].

Three approaches:

1. Angular cross-spectrum C_ℓ^Tg with a tracer bias fixed beforehand, summarised by A_ISW
   (Krolewski 2021, arXiv:2110.13959; Ghodsi Yengejeh 2026, arXiv:2607.22461) [src]. The bias
   comes from the CMB lensing cross-spectrum for unWISE (arXiv:2110.13959, Sect. 3.1.2), from
   an earlier lensing-tomography fit for Quaia (arXiv:2607.22461, Sect. 2.2), and from the
   tracer auto-spectrum in Stölzner 2017 (arXiv:1710.03238, Sect. VII.1) [src].
   As written in arXiv:2110.13959 [src: Sect. 2]: (ΔT/T)_ISW = −2 ∫ dχ e^−τ Φ̇, and
   C_ℓ^Tg = (2/π) ∫ k² dk P(k) K_ℓ^Φ̇(k) K_ℓ^g(k), with K_ℓ^g = ∫ dz b(z) (dN/dz) D(z) j_ℓ[kχ(z)]
   and K_ℓ^Φ̇ = (3 Ω_m H_0²/k²) ∫ dz d[(1+z)D(z)]/dz j_ℓ[kχ(z)]; a magnification term with
   coefficient (5s − 2) is added. The template is binned like the data and scaled by A_ISW.
2. Stacking or matched filtering on catalogued voids and superclusters (Nadathur 2016,
   arXiv:1608.08638; Kovács 2018, arXiv:1811.07812) [src: abstract]. The matched filter has an expected S/N
   comparable to the full cross-correlation and avoids the a posteriori bias of tuned stacking
   filters (arXiv:1608.08638) [src: abstract]. The stacking line starts with Granett 2008
   (arXiv:0805.3695): 9.6 ± 2.2 μK, above 4σ, on SDSS LRG supervoids and superclusters [src: abstract].
3. The ISW–lensing bispectrum, internal to the CMB: ≈ 3σ in Planck 2015 (Planck Collaboration
   2015, arXiv:1502.01595) [src].

## 6. Cosmic infrared background
<!-- key: cosmic-infrared-background -->

The CIB is unresolved dusty-galaxy emission; it overlaps strongly in redshift with the CMB lensing
kernel. Uses: a lensing tracer for delensing, co-added with galaxies and the internal
reconstruction (Hertig 2025, arXiv:2511.21949); f_NL from CIB × κ, which avoids the Galactic dust
that contaminates the CIB auto-spectrum on large scales (Thornton 2026, arXiv:2605.03783);
star-formation history through tomographic cross-correlation (arXiv:2603.04269) [src]. It is also
the principal contaminant of y-maps and of temperature-based lensing reconstruction
(`systematics.md` §2–3).

**Origins.** Song 2002 (arXiv:astro-ph/0209001) computed the far-infrared background × lensing
potential correlation with a halo model [src: abstract]. First detections, both in 2013: Planck, with a
peak significance of 42σ at 545 GHz, a correlation as high as 80% and a host-halo mass scale
log₁₀(M/M⊙) = 10.5 ± 0.6 (Planck Collaboration 2013, arXiv:1303.5078); SPT 150 GHz convergence ×
Herschel/SPIRE over 90 deg², 6.7–8.8σ per band, bias 1.3–1.8 (Holder 2013, arXiv:1303.5048)
[src: abstract]. Delensing with the CIB: Sherwin 2015 (arXiv:1502.05356) [src: abstract].

## 7. Other secondaries
<!-- key: other-secondaries -->

| Effect | Physical origin | How it is extracted |
|---|---|---|
| Moving lens | transverse motion of a potential; dipole pattern aligned with the transverse velocity | reconstructed transverse velocities × T, Fourier-space estimator with separated scales (Hotinli 2026, arXiv:2605.18938) [src] |
| Patchy / anisotropic screening | Thomson scattering damps primary anisotropy by e^−τ(n̂) | stacking, or a statistical-anisotropy estimator; strongly contaminated by lensing (arXiv:2506.17379; Kramer 2026, arXiv:2608.27458) [src] |
| Rotational kSZ | gas rotation in haloes; temperature dipole across the rotation axis | oriented stacking with the axis from satellite redshift dipoles (Yang 2026, arXiv:2603.14494) [src] |
| Polarised SZ | scattering of the local CMB quadrupole ("remote quadrupole") | CMB–CMB–galaxy bispectrum (Krywonos 2026, arXiv:2607.16071) [src] |

Origins. Moving lens: Birkinshaw 1983 (doi:10.1038/302315a0, "A test for transverse motions of
clusters of galaxies" [sec: Crossref, not read]); the large-scale transverse-velocity estimator
from temperature × overdensity is Hotinli 2018 (arXiv:1812.03167); a pairwise transverse-velocity
estimator built on the dipolar signature is Yasini 2018 (arXiv:1812.04241) [src]. Screening:
Dvorkin 2008 (arXiv:0812.1566) built the quadratic estimator of τ(n̂) for patchy reionisation;
late-time screening × unWISE with ACT + Planck is not significantly detected, the null being
consistent at 1.7σ (blue) and 0.016σ (green), τ̄ < 0.033 arcmin² (blue) and < 0.057 (green) within
a 6′ disk at 95% (Coulton 2024, arXiv:2401.13033); the "temperature inversion" and "signed"
estimators trade optimality for robustness to lensing and foregrounds (Schutt 2024,
arXiv:2401.13040, whose abstract calls the companion result a "first detection") [src].

## 8. Covariance, likelihood, point estimates
<!-- key: covariance-likelihood-point-estimates -->

- Bandpower likelihoods are Gaussian. arXiv:2309.05659 uses simulations for both the power
  spectrum recovery and the covariance, and marginalises an uncertainty on the lensing
  normalisation in the covariance [src, section titles]. A cross-covariance between tomographic
  samples that share sky must be included: neglecting it shifted S_8 by 0.3σ in that analysis
  [src, section "Post-unblinding Changes"].
- Stacking analyses use bootstrap over objects (10,000 resamplings in arXiv:2503.19870) [src].
  Bootstrap underestimates the velocity-reconstruction noise for dense samples: the fitted noise
  rescalings for DESI LRGs are 1.13 and 1.09 at 90 and 150 GHz, and 1.29 for the cross
  (arXiv:2604.04867, table of LRG fits) [src].
- Velocity-reconstruction analyses calibrate normalisation and covariance with "surrogate fields"
  that propagate mask, light-cone evolution and weights (arXiv:2604.04867, arXiv:2609.17676) [src].
- Posterior means can sit far from best fits when many bias parameters are poorly constrained.
  arXiv:2407.04607 always reports the best fit next to the mean for that reason [src].

## 9. Blinding
<!-- key: blinding -->

Blinded: unWISE × ACT DR6 (arXiv:2309.05659), DESI LRG × ACT DR6 (arXiv:2407.04606,
arXiv:2407.04607), DES Y3 × ACT DR4 (Marques 2023, arXiv:2306.17268), E_G with ACT DR6 × BOSS
(arXiv:2405.12795) [src]. Not blinded, stated as such: DESI LRG f_NL (arXiv:2412.10279) [src].
arXiv:2309.05659 documents its post-unblinding changes: the baseline S_8 moved by −0.1σ
(ΔS_8 = −0.002), from a mode-coupling and transfer-function correction (+0.2σ), a neglected
cross-covariance between the two samples (−0.3σ), and a bias-evolution bug whose fix widened the
error by 5% [src]. The kSZ gas-profile papers read for this file do not state a blinding scheme in
their abstracts; treat them as unblinded unless the paper says otherwise. A text search of the
bodies (2026-10-13) finds no blinding of the kSZ measurement in arXiv:2407.07152,
arXiv:2503.19870 or arXiv:2604.19744; in arXiv:2604.04867 the DESI DR2 galaxy power spectrum was
still blinded and is left out, and the linear bias is fixed from the galaxy monopole without
propagating its error to f_NL [src: Sect. 1 and Sect. 5.4].

## 10. Codes and public products
<!-- key: codes-and-public-products -->

| Code or product | Purpose | Where stated |
|---|---|---|
| ThumbStack | CAP stacking for kSZ and tSZ | arXiv:2009.05557; github.com/EmmanuelSchaan/ThumbStack [src] |
| pyrecon (MultiGrid) | reconstruction displacements, reused for velocities | arXiv:2503.19870; github.com/cosmodesi/pyrecon [src] |
| hmvec | halo model for the fiducial P_ge | arXiv:2604.04867 [src] |
| glasz | joint kSZ + galaxy–galaxy lensing model | Sunseri 2025, arXiv:2505.20413; github.com/James11222/glasz [src] |
| CosmoBLENDER | halo-model foreground biases to lensing auto, cross and delensing | Baleato Lizancos 2025, arXiv:2507.03859 [src] |
| Aemulus ν HEFT emulator, velocileptors, CLASS | theory for κ × galaxies | arXiv:2407.04607 [src] |
| WebSky | extragalactic foreground simulations for bias tests | arXiv:2309.05659 [src] |
| ACT DR6 lensing maps | κ alm, mask, filter, noise; 400 simulations at NERSC | LAMBDA, `surveys-and-data.md` §2 |
| Quaia catalogue and selection function | zenodo.org/records/10403370 | arXiv:2306.17749 [src] |

## 11. Conventions and where the community is split
<!-- key: conventions-and-where-the-community-is-split -->

- **Exponent of the amplitude combination**: 0.5, 0.4, 0.25, 0.2 (§2.3, §4). Compare like with
  like or convert with the Ω_m posterior.
- **Mean or best fit**: the two differed by ~1σ in the first DESI LRG analysis
  (`systematics.md` §6).
- **Scale cuts or bias model**: linear-only (arXiv:2410.10808) against HEFT to k = 0.6 h/Mpc
  (arXiv:2407.04606); arXiv:2407.04607 reports "excellent agreement" between its HEFT fit and a
  linear-theory fit on a restricted range of scales [src: abstract].
- **f_NL response p**: 1 or 1.6.
- **Detection significance**: "S/N" from Δχ² against a best-fit template, "rejection of the null",
  and amplitude over error are three numbers; arXiv:2305.06792 quotes 4.8σ and 5.1σ for the same
  data [src: abstract].
- **kSZ amplitude names**: τ̄, A_kSZ², A, b_v (§3.2).
- **"kinetic" and "kinematic"** SZ are the same effect; both spellings appear in titles.
- **Template amplitudes**: A_ISW, A_κ and b_ML are ratios to a ΛCDM or halo-model template whose
  cosmology and construction must be named; ⟨bP_e⟩ is quoted in meV cm⁻³ (arXiv:2210.08633) [src].
