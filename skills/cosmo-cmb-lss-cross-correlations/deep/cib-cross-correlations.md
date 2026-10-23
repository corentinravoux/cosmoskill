# CIB cross-correlations — cosmo-cmb-lss-cross-correlations dossier

Scope: how a CIB × CMB-lensing (or CIB × tracer) analysis is built — which
CIB map and how it was cleaned of Galactic dust, the linear CIB model and
its priors, the data vector, masks, covariance and lensing normalisation,
and how the choices differ between an f_NL measurement and a delensing
tracer. The f_NL route rests on one line of work (McCarthy, Hill,
Thornton and co-authors; no other CIB × lensing f_NL measurement found);
maps, CIB models and the delensing use have several groups, given step by
step.
Snapshot: 2026-10-22.
From: Baxter 2022 Snowmass review (arXiv:2203.06795), Sect. I (Fig. 1
probes); SO science goals 2025 (arXiv:2503.00636), Sect. 3.5 (dusty
galaxies, CIB).

Already in L2: the first CIB × lensing detections, the f_NL = 43 ± 23 and
delensing results (`physics-and-methods.md#cosmic-infrared-background`,
`results.md#cosmic-infrared-background`); the CIB as contaminant of y maps
and lensing (`systematics.md#cib-dust-and-radio-leakage-in-tsz-cross`,
`systematics.md#extragalactic-foregrounds-in-the-lensing`).

Notation follows Thornton et al. 2026 (arXiv:2605.03783). I_ν: CIB
intensity at frequency ν; j_ν(χ): comoving emissivity density, with mean
j̄_ν; b_CIB(z): linear bias of the emissivity; ρ_SFR(z): star-formation-rate
density; S_ν,eff(z): effective SED; C_ℓ^νκ: CIB × lensing convergence
spectrum; C_ℓ^νν′: CIB auto- and cross-frequency spectra; N_HI: HI column
density.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Choose the CIB map
<!-- key: step-1-choose-the-cib-map -->

Three families of Planck CIB maps are in use; which one depends on the
scales the analysis needs.

| Map | Dust removal | Unbiased range | Used for |
|---|---|---|---|
| L19 (Lenz 2019, arXiv:1905.00426) | HI4PI dust template fitted in N_side = 16 super-pixels, PR3 data, 353–857 GHz, ~25% of sky | ℓ ≳ 70 | f_NL with ℓ_min = 70 (McCarthy 2022, arXiv:2210.01049) |
| pyilc NILC with HI4PI (McCarthy 2024, arXiv:2405.13470) | HI column density as an extra "channel" with zero CIB response in a needlet ILC, NPIPE data | down to ℓ ~ 10 | f_NL with ℓ_min = 19 (arXiv:2605.03783) |
| GNILC (Planck PR2) | generalized needlet ILC using an assumed CIB power spectrum | oversubtracted on large scales, as cited in arXiv:2605.03783 | delensing tracer at 353 GHz (Hertig 2025, arXiv:2511.21949) |

All [src: abstracts; arXiv:2605.03783, Sect. III.2; arXiv:2511.21949,
Sect. III.3].

Why HI: the CIB and Galactic dust have very similar SEDs and the intrinsic
CIB SED is poorly known, so a multi-frequency ILC cannot separate them; HI
is highly correlated with Galactic dust and purely Galactic, so it suffices
to assume the CIB has no HI emission [src: arXiv:2605.03783, Sect. III.2;
arXiv:2405.13470, Sect. II.3]. The L19 dust model is
I_ν^dust = Σ_ch ε_ν^ch T_B^ch + β_ν per region, fitted with an L¹
regularisation γ on ~13 HI velocity bins (arXiv:2405.13470, Eqs. 9–10)
[src: Sects. V.1.1, V.1.4]. The NILC maps use one integrated HI map or three
velocity bins instead, because many tracers in an ILC produce "an
intolerable ILC bias" by chance correlations with the CIB; with three bins
a bias appears at ℓ ≲ 300 in validation on WebSky [src: Sect. V.1.4,
Fig. 6 caption].

Mean subtraction over a patch suppresses large-scale power. The transfer
function on C_ℓ^νν is within 3% of 1 for ℓ ≳ 7, 15, 24, 40, 90, 200 at
patch scales N_side = 1, 2, 4, 8, 16, 32; the N_side = 16 choice of L19
matches its stated ℓ ≳ 70 with a small neglected loss at 70 < ℓ < 100
[src: arXiv:2405.13470, Sect. V.1.3]. The f_NL analysis uses the R_N = 1
(largest-patch) maps, at most 1% biased for ℓ ≳ 10, at the price of more
dust power on large scales [src: arXiv:2605.03783, Sect. III.2].

At 353 GHz the CMB dominates the CIB, so a NILC CMB estimate is subtracted
first [src: arXiv:2605.03783, Sect. III.2; arXiv:2405.13470, abstract].

Other maps and dust treatments:
- **GNILC** (Planck intermediate XLVIII, arXiv:1605.09387) [src]: PR2
  maps at 353, 545, 857 GHz in which Galactic dust is separated from the
  CIB by spatial (power-spectrum) information; the CIB is available over
  60% of the sky at |b| > 20°, "recommended for exploring
  cross-correlations with lensing and large-scale structure".
- **Planck 2013 XXX** (arXiv:1309.0382) [src]: the earlier Planck + IRAS
  CIB power spectra, 143–3000 GHz, on about 2240 deg², ℓ ≈ 150–2500.
- **L19 in other cross-correlations.** CIB × cosmic shear uses the L19
  maps with their 20% masks (HI threshold 2.5 × 10²⁰ cm⁻², 15′ apodisation)
  and drops ℓ < 100 because of the large-scale power loss of L19 (Jego et
  al. 2022, arXiv:2209.05472, Sect. 3.2.1) [src].
- **A CIB-free dust map instead of HI.** CIB tomography with 11 Planck,
  Herschel and IRAS maps cross-correlated with SDSS galaxies and quasars
  removes Galactic dust with CSFD (Chiang et al. 2025, arXiv:2504.05384)
  [src].

### Step 2. Choose sky regions
<!-- key: step-2-choose-sky-regions -->

Regions are defined by an HI threshold intersected with a Galactic mask:
- arXiv:2210.01049 analyses separately N_HI ≤ 1.5, 1.8, 2.0, 2.5 (in
  10²⁰ cm⁻², the unit in which arXiv:2605.03783 writes the same L19
  thresholds), whose CIB × lensing overlaps are 10.20%, 14.06%, 15.73%, 17.95% of
  the sky; the 3.0 and 4.0 maps (26.46%, 32.99%) are measured but not used
  because of large-scale dust [src: Sect. IV.5, Table 4]. The regions are
  nested, so their constraints are not independent [src: Sect. IV.7].
- arXiv:2605.03783 builds two non-overlapping regions: "Cleaner",
  N_HI < 2.5 × 10²⁰ cm⁻² within the 20% Galactic mask (f_sky = 17.9%), and
  "Dustier", the annulus up to N_HI < 4.0 × 10²⁰ within the 40% mask
  (f_sky = 15.0%); C1 apodisation of 15′ [src: Sect. III.3].
Why disjoint regions: the signal-to-noise from larger, dustier areas grows
much less than f_sky because of dust variance, and non-overlapping regions
with their covariance combine more optimally (suggested in
arXiv:2405.13470, Sect. VII.2, and done in arXiv:2605.03783) [src].

### Step 3. Model the CIB
<!-- key: step-3-model-the-cib -->

Linear model of Maniyar et al. 2018 (arXiv:1801.10146), as used in
arXiv:2605.03783, Sect. II.2.2 [src]:

```
I_ν(n̂) = ∫ dχ a(χ) j_ν(χ, n̂)                                   (Eq. 18)
P_jm(k, z, z′) = b_CIB(z) P_mm^lin(k, z, z′)                      (Eq. 20)
W^ν(χ) = a(χ) j̄_ν(χ)                                             (Eq. 21)
b_CIB(z) = b_0 + b_1 z + b_2 z²                                   (Eq. 22)
j̄_ν(z) = ρ_SFR(z) (1+z) S_ν,eff(z) χ(z)² / K,  K = 10⁻¹⁰ M_⊙ yr⁻¹ L_⊙⁻¹   (Eq. 23)
ρ_SFR(z) = α (1+z)^β / [1 + ((1+z)/γ)^δ]                          (Eq. 24)
C_ℓ^νν′ = C_ℓ,lin + C_ℓ,1h + S_νν′                                (Eq. 25)
```

S_ν,eff comes from Herschel data; ρ_SFR follows the Madau–Dickinson form;
f_NL enters as Δb added to b_CIB [src: same]. The one-halo term is
precomputed and fixed, being nearly scale independent and degenerate with
the shot noise S_νν′, which is free [src: same]. Measured spectra are
compared through C^νκ_theory = A_ℓ b_ℓ p_ℓ f_ν C^νκ and
C^νν′_theory = b_ℓ² p_ℓ² f_ν f_ν′ C^νν′ (Eqs. 26–27), with a 5′ beam b_ℓ,
the N_side 2048 pixel window p_ℓ, calibration factors f_ν that also absorb
colour corrections, and the Monte Carlo lensing normalisation A_ℓ [src:
Sect. II.3].

Why the model is linear: Maniyar et al. fitted only ℓ ≤ 600, where the
two-halo term is > 90% of the CIB power; CIB × lensing was then available
for ℓ = 163–1937 [src: arXiv:1801.10146, Sect. 2.3.1]. C^νφ ∝ b_eff and
C^νν ∝ b_eff², so the lensing cross-spectrum partly breaks the degeneracy
between the bias evolution and ρ_SFR [src: Sect. 2.2, Eq. 9]. The fitted
bias is an emissivity-weighted effective bias, not the bias of the haloes
that dominate the star formation (Eqs. 13–14); it rises from ~0.8 at z = 0
to ~8 at z = 4 [src: Sect. 4.2, abstract].

Other CIB models, fitted to other data:
- Planck 2013 XXX fitted two models to all auto- and cross-spectra: the
  linear model with an emissivity-weighted mean bias (the one above) and a
  halo/subhalo model with a parametrised L_IR–mass relation; star
  formation is well constrained to z ~ 2, beyond which the SED uncertainty
  dominates [src: arXiv:1309.0382].
- A four-parameter halo model linking halo mass accretion to star
  formation fits Planck and Herschel spectra jointly for the first time,
  log₁₀M_max = 12.94 ± 0.02, but finds the large-scale Planck and Herschel
  data "not fully compatible" with the Herschel ℓ > 3000 data (Maniyar et
  al. 2020, arXiv:2006.16329) [src].
- Halo-based SFR models fitted to CIB × tracer spectra instead of CIB
  auto-spectra: CIB × DES and KiDS shear, η = 0.445 +0.055/−0.11,
  log₁₀(M_1/M⊙) = 12.17 ± 0.25 [src: arXiv:2209.05472]; CIB × KiDS galaxies
  (43σ), η_max = 0.41 +0.09/−0.14 at log₁₀M_peak = 12.14 ± 0.36 (Yan et
  al. 2022, arXiv:2204.01649) [src]; CIB × unWISE (194σ, 100 < ℓ < 2000),
  three halo models constrained consistently, T_0 = 21.14 +1.02/−1.34 K
  against the Planck 24.4 ± 1.9 K (Yan et al. 2023, arXiv:2310.10848)
  [src]; tomography with SDSS, 60σ on the evolving CIB spectrum over
  0 < z < 4, the bias–intensity degeneracy broken with the FIRAS + Planck
  monopole [src: arXiv:2504.05384].

A simpler kernel serves a delensing tracer: a single modified-blackbody
SED with T_d = 34 K, β = α = 2, and a Gaussian emissivity in redshift
around z_c ~ 2 with σ_z = 2 (arXiv:2511.21949, Eqs. 22–24); its fitted
parameters are not interpreted [src: Sects. II.3, V].

### Step 4. Choose the data vector
<!-- key: step-4-choose-the-data-vector -->

arXiv:2605.03783 [src: Sect. III.4, Eqs. 28–29]:
- Bin edges 19, 27, 40, 58, 85, 124, 180, 263, 380, 420, 460, 500, 540, 580,
  620: logarithmic at low ℓ, Δℓ = 40 from ℓ = 380.
- C_ℓ^νκ on both regions with all bins; C_ℓ^νν′ (six frequency pairs of
  353, 545, 857 GHz) on the Cleaner region only and only in the last three
  bins, 500 ≤ ℓ < 620. Auto-spectra use half-mission splits to remove noise
  bias.
- Why so little auto-spectrum: dust left at low ℓ "could be misinterpreted
  as scale-dependent bias, providing erroneous constraining power on
  f_NL"; the auto-spectra are kept only to break degeneracies between the
  bias, its evolution and the SFRD parameters. The Dustier region still
  shows dust at 500 ≤ ℓ ≤ 600, hence its auto-spectra are dropped.
- Why C^νκ can go to ℓ_min = 19: Galactic dust adds noise but no bias to a
  cross-spectrum with lensing. The leading bias would be a
  ⟨D_low-ℓ D_high-ℓ D_high-ℓ⟩ dust bispectrum through the quadratic
  estimator, expected negligible because dust power is small at the
  high ℓ of the SMICA-based PR4 reconstruction.

The earlier analysis used C^νκ for 70 ≤ ℓ ≤ 430 and both C^νκ and C^νν′ for
430 ≤ ℓ ≤ 610, never above 610 because the model is linear [src:
arXiv:2210.01049, Sect. IV.2, Eq. 29].

### Step 5. Priors
<!-- key: step-5-priors -->

arXiv:2605.03783, Table 1 and Sect. IV.2 [src]:

| Parameter | Prior | Reason given |
|---|---|---|
| f_NL | U(−1000, 1000) | uninformative |
| b_0 | N(0.83, 0.11) | present-day b_I σ_8 constraint converted with a σ_8 measurement |
| b_1, b_2 | U(0, 200); b_CIB > 0 at all z | physicality |
| log₁₀α, β, log₁₀γ, δ | U(−100, 100), U(−10, 10), U(−50, 50), U(−10, 10) | uninformative |
| S_νν′ | flat over the 1σ range of a counts model, widened by 20% | absorbs the one-halo term, ≲ 20% of S_νν′ |
| f_353, f_545, f_857 | N(1, 0.05) | calibration and colour correction |
| ν Ī_ν at 353–3000 GHz | split-normal priors, e.g. 0.46 +0.04/−0.05 nW m⁻² sr⁻¹ at 353 GHz | galaxy number counts, collated by Maniyar et al. |

Fiducial values are the Maniyar et al. 2018 best fit [src: Sect. IV.2].

### Step 6. Covariance and lensing normalisation
<!-- key: step-6-covariance-and-lensing-normalisation -->

- 480 Gaussian simulations built on the NPIPE lensing simulations: CIB
  realisations correlated with κ at the fiducial C^νκ, plus Gaussian dust
  with inter-frequency correlations but uncorrelated with the CIB, scaled so
  that CIB + dust reproduces the measured C^νν′; masked like the data;
  Hartlap factor (n − p − 2)/(n − 1) (Eq. 31) [src: arXiv:2605.03783,
  Sect. IV.1].
- The fiducial model of the simulations is itself a maximum-likelihood fit
  with an analytic covariance [src: same].
- A_ℓ = ⟨Ĉ_ℓ^{ν_mask κ̂_mask}⟩ / C_ℓ,theory^νκ (Eq. 32) from the same
  simulations, per region [src: Sect. IV.3].
- arXiv:2210.01049 derived the f_NL error from the scatter of best fits over
  200 Gaussian simulations, checking that their mean is ~0, alongside MCMC
  [src: Sect. IV.7].

For a delensing co-add, the mode-coupling matrix of spectra involving the
ACT lensing map uses the square of the ACT mask, with a simulation-based
transfer function f_L^κ = ⟨C_L^{κ̂ACT κ}⟩/C_L^κκ (arXiv:2511.21949,
Eq. 42) [src: Sect. V].

### Step 7. Use the CIB as a lensing tracer instead
<!-- key: step-7-use-the-cib-as-a-lensing-tracer-instead -->

The combined lensing estimate is (arXiv:2511.21949, Eqs. 25, 27)

```
κ̂^comb_LM = Σ_ij (ρ_L⁻¹)^ij ρ_L^{κ̂^j κ} sqrt(C_L^κκ / C_L^{κ̂^i κ̂^i}) κ̂^i_LM
ρ_L^{κ κ̂^i} = C_L^{κ κ̂^i} / sqrt(C_L^κκ C_L^{κ̂^i κ̂^i})
```

with ρ_L the matrix of correlation coefficients among tracers [src:
Sect. II.3]. Smooth models are fitted to the measured cross-spectra before
computing weights, "to avoid biases caused by statistical fluctuations";
external tracers enter only at 102 ≤ L ≤ 2000 because of Galactic dust at
low L [src: Sect. V]. The smooth-template weighting was already the
practice of the Planck CIB + Planck κ + WISE multitracer maps (Yu et al.
2017, arXiv:1705.02332) [src]. Simulated tracers are Gaussian fields
g = A_L κ + u with A_L = C_L^gκ/C_L^κκ, extended to several tracers by a
Cholesky decomposition (Eqs. 35–39) [src: Sect. IV.2].

The CIB as a delensing tracer, by other experiments:

| Analysis | Tracer and data | Result | Source |
|---|---|---|---|
| Sherwin & Schmittfull 2015 (**forecast**) | Planck 545 GHz CIB | removes > half the lensing B power; σ(r) better by up to ≈ 2.2, ≈ 4 with a ≈ 3 μK′ lensing reconstruction; CIB-spectrum uncertainty harmless below a few thousand deg² | arXiv:1502.05356 [src] |
| Larsen et al. 2016 | Planck 545 + 857 GHz, temperature | peak sharpening at 16σ, A_delens = 1.12 ± 0.07 | arXiv:1607.05733 [src] |
| Manzotti et al. 2017 | Herschel 500 μm, SPTpol 90 deg² | B power −28% at 300 < ℓ < 2300; no-delensing rejected at 6.9σ; limited by tracer noise | arXiv:1701.04396 [src] |
| Yu et al. 2017 | Planck CIB + Planck κ + WISE | delensing factor 43 ± 1% (f_sky = 0.43), 48 ± 1% (0.11); maps public | arXiv:1705.02332 [src] |
| BICEP/Keck 2020 | Planck CIB, SPT + BK + Planck E | σ(r) 0.024 → 0.022 in simulations (26% with a perfect template); r_0.05 < 0.090 → < 0.082 | arXiv:2011.08163 [src] |
| Nakato et al. 2026 | SPT-3G 2019–20 + Planck CIB | profile-hardened GMV + CIB: foreground bias < 10% of σ; A_lens^res ≃ 0.48 over 20 ≤ ℓ ≤ 200 | arXiv:2608.06343 [src] |

Hertig et al. and Nakato et al. each call their template "the highest
delensing efficiency" to date, on different sky areas and multipole
ranges (lensing power removed: 39% for ACT DR6 B modes at
100 ≤ ℓ ≤ 1500 and 47% for Planck at 30 ≤ ℓ ≤ 300, over 23% of the sky,
against A_lens^res ≃ 0.48 at 20 ≤ ℓ ≤ 200 on the SPT-3G field) [src: arXiv:2511.21949;
arXiv:2608.06343].

CIB × CMB lensing as a lensing measurement: ACTPol × Planck CIB detects
polarisation lensing at 4.5σ (9.1σ with temperature) on 206 deg² and the
first CIB × κ at ℓ > 2000, A = 1.02 +0.12/−0.18 (stat.) ± 0.06 (syst.)
against the Planck fit (van Engelen et al. 2014, arXiv:1412.0626) [src];
POLARBEAR × Herschel gives 4.0σ evidence for polarisation lensing and
2.3σ for lensing B modes (arXiv:1312.6645) [src].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Which map, for which scales
<!-- key: which-map-for-which-scales -->

- **f_NL needs the largest scales.** The scale-dependent bias goes as 1/k²,
  so the ℓ_min = 70 of L19 was "a severe hindrance"; a Fisher forecast with
  the same maps cleaned to ℓ_min = 10 gave σ(f_NL) ~ 4 from cross-correlation
  alone, and better than ~2 adding the CIB auto-spectrum, both stated as
  optimistic because dust variance is neglected [src: arXiv:2210.01049,
  Sect. VI.2]. Moving to the NILC maps with ℓ_min = 19 and two disjoint
  regions halved σ(f_NL), from 40 for the best earlier region to 23,
  "driven mostly by new maps that are unbiased to larger angular scales, as
  well as a more optimal treatment of additional sky area" [src:
  arXiv:2605.03783, Sect. V.1]. An earlier **forecast** puts the CIB
  auto-spectrum itself at |f_NL| < 1 for future space missions, provided
  enough frequency channels, high ones such as 857 GHz included, clean the
  dust (Tucci et al. 2016, arXiv:1606.02323) [src]; the data analyses
  above keep the auto-spectrum out of the low ℓ for fear of dust (Step 4).
- **Delensing needs intermediate scales.** The NILC maps were less
  correlated with CMB lensing than GNILC in the relevant multipoles, because
  they keep large-scale CIB power at the cost of more dust at intermediate
  and small scales; 545 and 857 GHz were not added because they are strongly
  correlated with 353 GHz [src: arXiv:2511.21949, Sect. III.3].

### One frequency or three
<!-- key: one-frequency-or-three -->

With a single frequency in C^νκ the f_NL constraint is "far reduced";
adding a second frequency narrows it mostly by breaking degeneracies with
nuisance parameters; dropping 545 GHz changes almost nothing [src:
arXiv:2605.03783, Sect. V.4]. A diagonal covariance inflates the f_NL
posterior by ~80% against the full one, which the authors attribute either
to inter-frequency correlations cleaning residual dust or to their removing
low-redshift information [src: same].

### Bias parametrisation
<!-- key: bias-parametrisation -->

Δb ∝ f_NL (b^G − 1) (Eq. 33), so the bias evolution matters. A quadratic
b_CIB(z) risks over-specifying the bias where the data have no sensitivity.
Piecewise linear (nodes at z = 0, 1, 4, 7): same width, central value
~0.5σ lower. Piecewise constant with 4 or 5 bins: similar widths; the
5-bin case shifts by ~0.1σ [src: arXiv:2605.03783, Sect. V.2]. The b_0
prior is kept in all cases.

### CIB as ISW tracer
<!-- key: cib-as-isw-tracer -->

The CIB × CMB temperature (ISW) signal has a forecast S/N of 4.2–5.6 on 70%
of the sky without residual dust; with a 10% dust residual in the CIB power
spectra it "drops drastically", and keeping the S/N loss below 10% on 40%
of the sky needs dust cleaned to the 0.01% level of the power spectrum; on
the 11% GASS field no ISW signal was detected (Maniyar 2019,
arXiv:1809.04551) [src: abstract]. This is the ISW counterpart of the
dust problem above.

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| ℓ_min for C^νκ | 19 (NILC maps); 70 (L19 maps) | Planck PR4 κ × CIB | arXiv:2605.03783; arXiv:2210.01049 | Sect. III.2; Sect. VI.2 |
| ℓ range for C^νν′ | 500–620 (Cleaner only); 430–610 earlier | same | arXiv:2605.03783; arXiv:2210.01049 | Sect. III.4; Sect. IV.2 |
| Linear-model limit | ℓ ≤ 600, two-halo term > 90% | Planck CIB | arXiv:1801.10146 | Sect. 2.3.1 |
| Map bias of NILC CIB | ≤ 1% for ℓ ≳ 10 (R_N = 1) | NPIPE × HI4PI | arXiv:2605.03783 | Sect. III.2 |
| Mean-subtraction transfer | > 0.97 for ℓ ≳ 7–200 (N_side 1–32) | WebSky test | arXiv:2405.13470 | Sect. V.1.3 |
| Sky fractions | 17.9% (Cleaner), 15.0% (Dustier) | same | arXiv:2605.03783 | Sect. III.3 |
| Simulations for covariance | 480 (current); 200 for the error (earlier) | same | arXiv:2605.03783; arXiv:2210.01049 | Sect. IV.1; Sect. IV.7 |
| b_0 prior | N(0.83, 0.11) | same | arXiv:2605.03783 | Table 1 |
| Calibration priors | N(1, 0.05) per frequency | same | arXiv:2605.03783 | Table 1 |
| One-halo fraction of shot noise | ≲ 20% | same | arXiv:2605.03783 | Sect. IV.2.3 |
| Region contribution | σ(f_NL) = 27 (Cleaner); ~15% better with Dustier | same | arXiv:2605.03783 | Sect. V.1 |
| Cleaner–Dustier null | p = 0.37 for 42 degrees of freedom | same | arXiv:2605.03783 | Eq. 37 |
| Diagonal-covariance penalty | σ(f_NL) larger by ~80% | same | arXiv:2605.03783 | Sect. V.4 |
| Earlier result | −87 < f_NL < 19; σ ≈ 41 | L19 maps | arXiv:2210.01049 | abstract |
| Delensing tracer range | 102 ≤ L ≤ 2000 (external tracers) | ACT DR6 + unWISE + CIB | arXiv:2511.21949 | Sect. V |
| Delensing CIB kernel | T_d = 34 K, β = α = 2, z_c ~ 2, σ_z = 2 | same | arXiv:2511.21949 | Sect. II.3 |
| Effective CIB bias | ~0.8 (z = 0) to ~8 (z = 4) | Planck | arXiv:1801.10146 | abstract |
| GNILC CIB sky | 60% at abs(b) > 20° | Planck PR2 | arXiv:1605.09387 | abstract |
| CIB × shear model | η = 0.445 +0.055/−0.11; log₁₀M_1 = 12.17 ± 0.25 | Planck L19 × DES, KiDS | arXiv:2209.05472 | abstract |
| CIB × galaxies significance | 43σ (KiDS); 194σ (unWISE); 60σ (SDSS tomography) | Planck × tracers | arXiv:2204.01649; arXiv:2310.10848; arXiv:2504.05384 | abstracts |
| CIB × ACTPol κ amplitude | A = 1.02 +0.12/−0.18 ± 0.06 | ACTPol × Planck | arXiv:1412.0626 | abstract |
| CIB delensing on data | A_delens = 1.12 ± 0.07 (T); B −28% (SPTpol); 43–48% (multitracer); A_lens^res ≃ 0.48 (SPT-3G) | various | arXiv:1607.05733; arXiv:1701.04396; arXiv:1705.02332; arXiv:2608.06343 | abstracts |
| BK r with CIB delensing | r_0.05 < 0.090 → < 0.082 | BICEP/Keck 2014 | arXiv:2011.08163 | abstract |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Galactic dust read as f_NL.** Low-ℓ dust power in the CIB auto-spectrum
  mimics scale-dependent bias. Test: compare maps cleaned with different
  patch sizes (R_N = 1 against 16); keep auto-spectra only at ℓ ≳ 500
  [src: arXiv:2605.03783, Sect. III.2, Fig. 1].
- **A dust bispectrum biasing C^νκ.** Would scale as 2^(3/2)–5^(3/2) more in
  the Dustier region, where C^νν′ is 2 times higher below ℓ ~ 100 and 5 times
  near ℓ ~ 20. Tests: f_NL stable as ℓ_min rises (Fig. 9); difference
  vector Cleaner − Dustier with Cov(Δ) = C^Cl + C^Du − 2C^Cl,Du, p = 0.37
  [src: arXiv:2605.03783, Sect. V.3, Eqs. 34–37].
- **ILC bias from too many HI tracers.** Chance correlations remove CIB.
  Test: inject WebSky CIB into the data and cross the output with the input
  [src: arXiv:2405.13470, Sect. V.1.4, Fig. 6].
- **CMB template subtraction at 353 GHz** could oversubtract CIB; the map
  paper assesses it on simulations and finds it not large enough [src:
  arXiv:2605.03783, Sect. III.2 footnote; arXiv:2405.13470, Sect. IV.2
  title].
- **Over-constrained bias evolution.** Test: piecewise bias models [src:
  arXiv:2605.03783, Sect. V.2].
- **Mask-induced lensing misnormalisation.** Test: A_ℓ per region from
  simulations [src: arXiv:2605.03783, Sect. IV.3].
- **Nested regions combined as independent.** The earlier HI thresholds are
  subsets of one another [src: arXiv:2210.01049, Sect. IV.7].
- **Fitting tracer weights to noisy spectra.** Biases the co-added lensing
  map; fit smooth models first [src: arXiv:2511.21949, Sect. V;
  arXiv:1705.02332].
- **Foreground bias in the CMB-lensing leg of a template.** Test:
  reconstruction variants with different foreground immunity (standard
  and profile-hardened GMV, polarisation only) on Agora simulations [src:
  arXiv:2608.06343].
- **Large-scale power loss of L19 in other cross-correlations.** Test or
  cut: ℓ ≥ 100 [src: arXiv:2209.05472, Sect. 3.2.1].
- **Inconsistent CIB data sets in the model fit.** Large-scale Planck and
  Herschel against Herschel ℓ > 3000 [src: arXiv:2006.16329].

## Reading list
<!-- key: reading-list -->

- Foundation: Planck Collaboration 2013 XVIII, arXiv:1303.5078 — first
  CIB × lensing (in L2).
- Method: Maniyar et al. 2018, arXiv:1801.10146 — linear CIB model, SFRD,
  effective bias; the model all f_NL analyses use.
- Data: Lenz et al. 2019, arXiv:1905.00426 — HI-cleaned CIB maps unbiased
  at ℓ ≳ 70.
- Data/method: McCarthy 2024, arXiv:2405.13470 — HI as an ILC channel;
  transfer function of mean subtraction; ILC bias.
- Application: McCarthy et al. 2022, arXiv:2210.01049 — first
  cross-correlation-only CIB f_NL; ℓ_min forecast.
- Application: Thornton et al. 2026, arXiv:2605.03783 — current f_NL
  pipeline: regions, data vector, priors, simulations, null tests.
- Application: Hertig et al. 2025, arXiv:2511.21949 — CIB in a co-added
  delensing tracer; GNILC against NILC.
- Critique: Maniyar et al. 2019, arXiv:1809.04551 — dust requirement for
  CIB × ISW.
- Data: Planck intermediate XLVIII, arXiv:1605.09387 (GNILC maps); Planck
  2013 XXX, arXiv:1309.0382 (CIB spectra, linear and halo models).
- Models from other data: Maniyar et al. 2020, arXiv:2006.16329; Jego et
  al. 2022, arXiv:2209.05472; Yan et al. 2022, arXiv:2204.01649 and 2023,
  arXiv:2310.10848; Chiang et al. 2025, arXiv:2504.05384.
- Forecast: Tucci et al. 2016, arXiv:1606.02323 (f_NL from the CIB
  auto-spectrum); Sherwin & Schmittfull 2015, arXiv:1502.05356 (CIB
  delensing).
- Delensing and lensing on data: Larsen et al. 2016, arXiv:1607.05733;
  Manzotti et al. 2017, arXiv:1701.04396; Yu et al. 2017,
  arXiv:1705.02332; BICEP/Keck 2020, arXiv:2011.08163; Nakato et al.
  2026, arXiv:2608.06343; van Engelen et al. 2014, arXiv:1412.0626;
  POLARBEAR 2013, arXiv:1312.6645.

## Not verified
<!-- key: not-verified -->

- The GNILC large-scale oversubtraction: stated in arXiv:2605.03783 with a
  citation; the cited evidence was not read.
- The Herschel-based effective SEDs S_ν,eff(z) and the shot-noise model
  behind the S_νν′ priors: references not read.
- CIB × galaxy cross-correlations used for star-formation history
  (arXiv:2603.04269, in L2) and the CIB halo models compared in
  arXiv:2405.13470, Figs. 15–16: not read in body. The CIB models of
  Shang et al. 2012 and HerMES (Viero et al. 2013): titles seen only.
- The bodies of the delensing papers in the peer table (abstracts only),
  and the scattering-transform dust–CIB separation (Sinha et al. 2026,
  title only).
- The sizes of A_ℓ for the two regions (arXiv:2605.03783, App. A): figure
  only.
