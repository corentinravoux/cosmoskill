# Physics and methods — CMB × LSS cross-correlations

Scope: what each cross-correlation measures, the estimators and models in current use, covariance, blinding, codes and conventions.
Snapshot: 2026-10-07

Flags: `[src]` read this session in the cited paper; `[sec]` from a named secondary source; `[der]`
derived here. Equations given without a flag are textbook definitions. CMB lensing reconstruction
itself (quadratic estimators, N0/N1 biases, the lensing auto-spectrum) belongs to `cosmo-cmb`.

## 1. Why cross-correlate

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

### 2.1 Observables

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
the highest-redshift bin (arXiv:2407.04607) [src]. For broad or high-redshift samples the
magnification term is larger and the number-count slope is a calibrated input, published with the
sample (Zhou 2023, arXiv:2309.06443) [src].

### 2.2 Theory models in current use

| Model | Used by | Stated range |
|---|---|---|
| Linear theory with conservative scale cuts | Qu 2024 (arXiv:2410.10808): "a scale cut where non-linear effects are negligible" | linear regime only [src] |
| Perturbation theory, restricted to large scales | White 2021 (arXiv:2111.09898) | large scales [src] |
| Hybrid EFT (HEFT): Lagrangian bias expansion on N-body displacements, emulated | Sailer 2024 (arXiv:2407.04607, Aemulus ν emulator); Kim 2024 (arXiv:2407.04606); Sailer 2025 (arXiv:2503.24385); Rubiola 2025 (arXiv:2510.09563) | k_max = 0.6 h/Mpc in arXiv:2407.04606; ℓ_max = 600 in arXiv:2407.04607 [src] |
| Hybrid model with marginalisation over higher-order biases | Farren 2023 (arXiv:2309.05659) | validated on mocks [src] |
| One-loop Eulerian bias for P, tree-level for the bispectrum | Verdiani 2025 (arXiv:2510.17796) | k_max^P ≃ 0.2 h/Mpc, k_max^B ≃ 0.08 h/Mpc [src] |
| EFT of LSS, joint with 3D full shape and bispectrum | Ivanov 2026 (arXiv:2601.16165) | — |
| Linear bias with scale cuts, or non-linear bias | Chang 2022 (arXiv:2203.12440): two sets of scale cuts | S/N 23.9 or 25.7 [src] |

HEFT in arXiv:2407.04607 adds 16 nuisance parameters for four bins (b_2^L, b_s^L and two
counterterms per bin) to a 30-dimensional posterior [src]. That is where projection ("volume")
effects come from; see `systematics.md` §6.

### 2.3 What is quoted

- S_8 = σ_8(Ω_m/0.3)^0.5, the galaxy-lensing convention.
- S_8^× or S_8^3x2pt = σ_8(Ω_m/0.3)^0.4, the best-constrained combination of the κ–galaxy data
  (arXiv:2407.04606, arXiv:2409.02109) [src].
- σ_8, after a BAO prior fixes Ω_m.
- σ_8(z) or S_8^×(z) per bin: the growth history (arXiv:2402.05761, arXiv:2407.04606) [src].
- The amplitude at redshifts above the tracers, from the lensing auto-spectrum once the
  cross-correlations have fixed the low-redshift part: a 3.3% constraint above z = 2.4 (Farren
  2024, arXiv:2409.02109) and σ_8(z̃ = 5.1) (Embil Villagra 2025, arXiv:2507.08798) [src].

The CMB lensing auto-spectrum itself constrains a combination with exponent 0.25 (see
`cosmo-cmb`). ACT DR6 lensing alone with BAO gives σ_8 = 0.819 ± 0.015 and S_8 = 0.840 ± 0.028
(Madhavacheril 2023, arXiv:2304.05203) [src]. Four exponents (0.25, 0.4, 0.5, and 0.2 for
lensing × tSZ, §4) circulate in this domain.

### 2.4 Lensing map normalisation in cross-correlation

A lensing reconstruction made on a masked sky is misnormalised. Auto-spectrum analyses correct
this with Monte Carlo simulations; for a cross-correlation the correction is

```
A_ℓ^MC = C_ℓ(κ_in masked by κ mask × κ_in masked by galaxy mask) / C_ℓ(κ̂ × κ_in masked by galaxy mask)
```

and it depends on the overlap region, so it cannot be taken from the auto-spectrum analysis
(arXiv:2309.05659, appendix on the Planck reanalysis) [src]. Earlier cross-correlation papers
omitted it; restoring it raised S_8 by 0.6σ for unWISE × Planck and by 0.015 for DESI LRG × Planck
PR3 (arXiv:2309.05659, arXiv:2407.04607) [src].

### 2.5 Redshift distributions

Photometric tracers need dN/dz from outside. unWISE uses cross-correlation redshifts against
spectroscopic samples; these depend on the fiducial cosmology assumed when measuring them, which
arXiv:2309.05659 corrects for explicitly, and their uncertainty is marginalised with principal
components [src]. The DESI LRG and BGS imaging samples are calibrated directly with DESI spectra
(arXiv:2309.06443, arXiv:2407.04607) [src]. Quaia has per-object spectro-photometric redshifts
from Gaia BP/RP spectra improved with a k-nearest-neighbour model trained on SDSS (Storey-Fisher
2023, arXiv:2306.17749) [src].

### 2.6 Derived tests

- **f_NL (local).** Scale-dependent bias Δb ∝ f_NL b_φ/k², with b_φ ∝ (b − p). Analyses quote
  p = 1 and p = 1.6 side by side (arXiv:2504.20992, arXiv:2512.17865) [src]. The κ–galaxy
  spectrum is used alone or with the auto-spectrum above an ℓ_min cut (arXiv:2412.10279) [src].
- **E_G.** The ratio of a lensing cross-spectrum to a velocity (RSD) measurement of the same
  galaxies; in GR it equals Ω_m,0/f(z) and is scale independent. With ACT DR6 and BOSS it is
  consistent with GR and with scale independence (PTE > 5%), with 3–4% systematic errors
  (Wenzl 2024, arXiv:2405.12795) [src].
- **Sound-horizon-free H_0.** The shape of the lensing and galaxy spectra carries the
  matter–radiation equality scale (arXiv:2409.02109, arXiv:2506.22416, arXiv:2410.24134) [src].
- **Variance cancellation.** A third tracer can remove structure from κ before the
  cross-correlation, giving the gain of a joint analysis without modelling that tracer:
  10–20% lower variance with the CIB or LRGs on Planck data (Baleato Lizancos 2023,
  arXiv:2301.10242) [src].
- **Galaxy magnification as a growth probe.** Cross-correlating non-overlapping photometric bins
  isolates magnification; detected at 11σ for BGS × LRG (arXiv:2503.24385) [src].
- **Stacking on voids and superstructures**, compared with mock templates through an amplitude
  A_κ (Sartori 2026, arXiv:2605.19763; Hang 2021, arXiv:2105.11936) [src].

## 3. Kinematic Sunyaev–Zel'dovich effect

### 3.1 Signal

ΔT/T_CMB = −∫ dχ a σ_T n_e (v_e · n̂)/c. The signal has the blackbody spectrum of the CMB, so
frequency information cannot isolate it, and it is odd in the line-of-sight velocity, so it
averages to zero in a plain stack. Its typical size where it peaks is ~0.1 μK against ~100 μK
of primary anisotropy (as stated in Ried Guachalla 2025, arXiv:2503.19870) [src]. Every estimator
supplies the velocity sign from the galaxy survey.

Smith 2018 (arXiv:1810.13423) shows that five estimators then in use are all equivalent to the
optimal ⟨ggT⟩ bispectrum estimator and that the bispectrum carries two observables: the
small-scale galaxy–electron spectrum P_ge(k_S), which is astrophysics, and the large-scale
galaxy–velocity spectrum P_gv(k), which is cosmology [src].

### 3.2 Estimators

| Estimator | Needs | Returns | Reference |
|---|---|---|---|
| Pairwise | positions and redshifts of groups; aperture photometry | mean pairwise momentum ∝ τ̄ × pairwise velocity v_12(r) | Hand 2012, arXiv:1203.4219; Calafut 2021, arXiv:2101.08374 [src] |
| Velocity-weighted stacking | a 3D velocity reconstruction | stacked profile ∝ τ(R); gas density profile | Schaan 2015, arXiv:1510.06442; Schaan 2020, arXiv:2009.05557 [src] |
| Hybrid stacking | spectroscopic velocities interpolated to photometric objects | same, with the photometric number density | Mallaby-Kay 2023, arXiv:2305.06792 [src] |
| Projected field | no redshifts; cleaned CMB map, filtered and squared, × projected galaxies | A_kSZ², sensitive to f_b f_free | Hill 2016, arXiv:1603.01608; Kusiak 2021, arXiv:2102.01068 [src] |
| Velocity reconstruction | quadratic estimator in small-scale T × small-scale δ_g | large-scale radial velocity map, up to the bias b_v | McCarthy 2024, arXiv:2410.06229; Chaussidon 2026, arXiv:2604.04867 [src] |
| Harmonic-space momentum template | velocity-weighted galaxy template × T | P_ge bandpowers, nearly uncorrelated | Qu 2026, arXiv:2604.19744; Hotinli 2026, arXiv:2609.17676 [src] |

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
catalogue, and S/N = sqrt(χ²_null − χ²_best-fit) [src].

**Velocity reconstruction** (arXiv:2604.04867, section "kSZ Velocity Bias") [src]. The estimator
obeys ⟨v̂_r(x)⟩ = b_v B(x) n_v(x) v_r^true(x), with

```
b_v(χ) = ∫ d²L b_L F_L P_ge^true(L/χ) / ∫ d²L b_L F_L P_ge^fid(L/χ)
```

so b_v = 1 only if the fiducial small-scale galaxy–electron spectrum is right. The integral is
dominated by small scales, b_v is effectively constant on the scales analysed, and it is
marginalised as a free amplitude. The fiducial P_ge in that paper is a halo model (hmvec) with an
abundance-matching HOD and the Battaglia AGN electron profile, in which the baryon fraction
reaches the cosmic value at the virial radius [src]. "b_v", "A" (arXiv:2506.21684) and "A_kSZ²"
(arXiv:2102.01068) are all amplitudes relative to a fiducial gas model and are comparable only if
the fiducial models are the same.

**Pairwise.** The amplitude is turned into a mass-averaged optical depth by comparing the measured
curve with the linear-theory pairwise velocity of a fixed cosmology (arXiv:2101.08374,
arXiv:2511.23417) [src], or with a pairwise velocity measured from reconstructed, machine-learnt
velocities (Gong 2026, arXiv:2609.36355) [src].

**Projected field.** Needs foreground-cleaned maps, because nothing cancels tSZ or dust, and a
marginalisation over the CMB lensing contribution to the same statistic (arXiv:2102.01068) [src].

### 3.3 From a kSZ profile to a feedback statement

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
arXiv:2009.05558) [src]. Stacked tSZ with a ȳ–τ̄ relation gives optical depths that can be
checked against the pairwise kSZ values (Moore 2026, arXiv:2609.08939) [src].

### 3.4 Cosmology from the large-scale velocity field

The reconstructed velocity traces the matter field without galaxy bias, so v × g cancels sample
variance for the scale-dependent bias and constrains f_NL (arXiv:2511.15701, arXiv:2604.04867)
[src]. Pairwise velocities test the force law (Gallardo 2026, arXiv:2604.14327) [src]. Growth
(fσ_8) is not obtained: the amplitude is degenerate with τ or b_v. The velocity side of this is
developed in `cosmo-peculiar-velocities`.

## 4. Thermal Sunyaev–Zel'dovich × LSS

y = (σ_T/m_e c²) ∫ P_e dl, with a known non-blackbody spectrum, so a Compton-y map can be built by
component separation. The cross-correlations in use:

| Statistic | Constrains | Reference |
|---|---|---|
| galaxies × y, large scales | bias-weighted mean electron pressure ⟨b_h P_e⟩(z), in meV cm⁻³ | Pandey 2019, arXiv:1904.13347; Sánchez 2022, arXiv:2210.08633 [src] |
| spectroscopic reference × multi-frequency intensity maps | ⟨bP_e⟩ to z ~ 1 with uncorrelated bins; the thermal history; a mass bias B = 1.27 (1 − b = 0.79) for the Planck universal pressure profile | Chiang 2020, arXiv:2006.14650 [src] |
| galaxies × multi-frequency maps, tSZ and CIB fitted together | ⟨bP_e⟩ and ⟨bρ_SFR⟩ jointly | La Posta 2026, arXiv:2603.04269 [src] |
| shear × y | pressure profile, feedback, and cosmology through σ_8(Ω_m/0.3)^0.2 | Van Waerbeke 2013, arXiv:1310.5721; Tröster 2021, arXiv:2109.04458; Gatti 2021, arXiv:2108.01600; Pandey 2025, arXiv:2506.07432 [src] |
| CMB lensing × y | intermediate-mass (10¹³–10¹⁴ h⁻¹M⊙), z ≲ 1.5 gas | McCarthy 2023, arXiv:2308.16260 [src] |
| stacked y on groups and clusters | integrated pressure; ȳ–τ̄ relation | arXiv:2609.08939 [src] |

In the FLAMINGO simulations ⟨b_h P_e⟩ ∝ S_8^ε with ε ≈ 3 over 0.1 ≤ z ≤ 1, and stronger feedback
raises ⟨b_h P_e⟩, opposite to its effect on small-scale gas fractions (Salcido 2026,
arXiv:2605.11083) [src]. The statistic is therefore a steep but feedback-degenerate amplitude
probe.

The (1 − b) of arXiv:2006.14650 is defined against the Planck pressure profile; the comparison
with cluster-count values, which depend on the reference mass, is in `cosmo-clusters`.

Component separation choices that matter here: needlet ILC with CIB deprojection; moment
deprojection, which protects against a wrong CIB spectral shape (arXiv:2308.16260) [src]; and
fitting the components at the level of the multi-frequency cross-spectra instead of the map
(Wayland 2026, arXiv:2609.31774; Zhao 2026, arXiv:2606.28099) [src].

## 5. Integrated Sachs–Wolfe effect

ΔT/T = 2 ∫ dη ∂Φ/∂η (in units with c = 1): a decaying potential, as under dark energy, leaves a
positive correlation between temperature and overdensity on large angular scales. It is detectable
only in cross-correlation, and the signal-to-noise is bounded by cosmic variance of the primary
CMB: the highest significance among the works cited here is 4.7–5.0σ, from five catalogues in
redshift bins (Stölzner 2017, arXiv:1710.03238) [src].

Three approaches:

1. Angular cross-spectrum C_ℓ^Tg with a bias fixed by the tracer auto-spectrum, summarised by
   A_ISW (Krolewski 2021, arXiv:2110.13959; Ghodsi Yengejeh 2026, arXiv:2607.22461) [src].
2. Stacking or matched filtering on catalogued voids and superclusters (Nadathur 2016,
   arXiv:1608.08638; Kovács 2018, arXiv:1811.07812) [src]. The matched filter has an expected S/N
   comparable to the full cross-correlation and avoids the a posteriori bias of tuned stacking
   filters (arXiv:1608.08638) [src].
3. The ISW–lensing bispectrum, internal to the CMB: ≈ 3σ in Planck 2015 (Planck Collaboration
   2015, arXiv:1502.01595) [src].

## 6. Cosmic infrared background

The CIB is unresolved dusty-galaxy emission; it overlaps strongly in redshift with the CMB lensing
kernel. Uses: a lensing tracer for delensing, co-added with galaxies and the internal
reconstruction (Hertig 2025, arXiv:2511.21949); f_NL from CIB × κ, which avoids the Galactic dust
that contaminates the CIB auto-spectrum on large scales (Thornton 2026, arXiv:2605.03783);
star-formation history through tomographic cross-correlation (arXiv:2603.04269) [src]. It is also
the principal contaminant of y-maps and of temperature-based lensing reconstruction
(`systematics.md` §2–3).

## 7. Other secondaries

| Effect | Physical origin | How it is extracted |
|---|---|---|
| Moving lens | transverse motion of a potential; dipole pattern aligned with the transverse velocity | reconstructed transverse velocities × T, Fourier-space estimator with separated scales (Hotinli 2026, arXiv:2605.18938) [src] |
| Patchy / anisotropic screening | Thomson scattering damps primary anisotropy by e^−τ(n̂) | stacking, or a statistical-anisotropy estimator; strongly contaminated by lensing (arXiv:2506.17379; Kramer 2026, arXiv:2608.27458) [src] |
| Rotational kSZ | gas rotation in haloes; temperature dipole across the rotation axis | oriented stacking with the axis from satellite redshift dipoles (Yang 2026, arXiv:2603.14494) [src] |
| Polarised SZ | scattering of the local CMB quadrupole ("remote quadrupole") | CMB–CMB–galaxy bispectrum (Krywonos 2026, arXiv:2607.16071) [src] |

## 8. Covariance, likelihood, point estimates

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

Blinded: unWISE × ACT DR6 (arXiv:2309.05659), DESI LRG × ACT DR6 (arXiv:2407.04606,
arXiv:2407.04607), DES Y3 × ACT DR4 (Marques 2023, arXiv:2306.17268), E_G with ACT DR6 × BOSS
(arXiv:2405.12795) [src]. Not blinded, stated as such: DESI LRG f_NL (arXiv:2412.10279) [src].
arXiv:2309.05659 documents its post-unblinding changes: the baseline S_8 moved by −0.1σ
(ΔS_8 = −0.002), from a mode-coupling and transfer-function correction (+0.2σ), a neglected
cross-covariance between the two samples (−0.3σ), and a bias-evolution bug whose fix widened the
error by 5% [src]. The kSZ gas-profile papers read for this file do not state a blinding scheme in
their abstracts; treat them as unblinded unless the paper says otherwise.

## 10. Codes and public products

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

- **Exponent of the amplitude combination**: 0.5, 0.4, 0.25, 0.2 (§2.3, §4). Compare like with
  like or convert with the Ω_m posterior.
- **Mean or best fit**: the two differed by ~1σ in the first DESI LRG analysis
  (`systematics.md` §6).
- **Scale cuts or bias model**: linear-only (arXiv:2410.10808) against HEFT to k = 0.6 h/Mpc
  (arXiv:2407.04606); arXiv:2407.04607 reports "excellent agreement" between its HEFT fit and a
  linear-theory fit on a restricted range of scales [src].
- **f_NL response p**: 1 or 1.6.
- **Detection significance**: "S/N" from Δχ² against a best-fit template, "rejection of the null",
  and amplitude over error are three numbers; arXiv:2305.06792 quotes 4.8σ and 5.1σ for the same
  data [src].
- **kSZ amplitude names**: τ̄, A_kSZ², A, b_v (§3.2).
- **"kinetic" and "kinematic"** SZ are the same effect; both spellings appear in titles.
- **Template amplitudes**: A_ISW, A_κ and b_ML are ratios to a ΛCDM or halo-model template whose
  cosmology and construction must be named; ⟨bP_e⟩ is quoted in meV cm⁻³ (arXiv:2210.08633) [src].
