# tSZ cross-correlations — cosmo-cmb-lss-cross-correlations dossier

Scope: how a tSZ × LSS measurement is turned into a physical quantity —
the bias-weighted pressure ⟨b_h P_e⟩ from galaxy × y, the gas and pressure
model and S_8 from shear × y — which statistic, model, priors, scale cuts
and covariance each analysis uses, and how to choose between a halo model,
a simulation suite and spectrum-level component separation.
Snapshot: 2026-10-17.
From: Baxter 2022 Snowmass review (arXiv:2203.06795), Sect. II.2
("Constraining baryonic feedback"); SO science goals 2025
(arXiv:2503.00636), Sect. 3.4 (tSZ paragraphs).

Already in L2: the y-map spectra, moment deprojection and the CIB stopping
rule (`physics-and-methods.md#thermal-sunyaev-zel-dovich-x-lss`,
`systematics.md#cib-dust-and-radio-leakage-in-tsz-cross`); measured
⟨b_h P_e⟩ and shear × y values and the S_8 disagreement
(`results.md#tsz-x-galaxy-positions-bias-weighted-pressure`,
`results.md#tsz-x-lensing-2`, `open-questions.md#does-the-tsz-prefer-a-low-s8`).

Symbols: y Compton parameter; P_e electron pressure; b_h linear halo bias;
dn/dM halo mass function; W_A(χ) radial kernel of field A; b_H hydrostatic
mass bias, with B = 1/(1 − b_H); r_500c, M_500c radius and mass enclosing
500 times the critical density.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Pick the statistic and what it measures
<!-- key: step-1-pick-the-statistic-and-what-it-measures -->

| Statistic | Large-scale content | Analyses read |
|---|---|---|
| Galaxy × y angular spectrum C_ℓ^gy, with C_ℓ^gg | C^gg ∝ b_g², C^gy ∝ b_g ⟨b_h P_e⟩, so the pair gives ⟨b_h P_e⟩ | Sánchez 2022 (arXiv:2210.08633), Sect. 5 |
| Clustering redshifts of intensity maps against a spectroscopic reference | dy/dz × b_y per redshift bin, with the CIB fitted in each bin's SED | Chiang 2020 (arXiv:2006.14650), Sects. II, III.2, V.2 |
| Shear × y, real space ξ_γt,y(θ) | matter–pressure spectrum weighted by the lensing kernel; σ_8, Ω_m and the gas model | Pandey 2025 (arXiv:2506.07432) |
| Shear × y, pseudo-C_ℓ | same | Tröster 2021 (arXiv:2109.04458); Wayland 2026 (arXiv:2609.31774) |

⟨b_h P_e⟩ is defined as the large-scale limit of the ratio of the
matter–pressure to the matter power spectrum (Salcido 2026,
arXiv:2605.11083, Eq. 2):

```
⟨b_h P_e⟩(z) = lim_{k→0} P_mPe(k, z) / P_mm(k, z)  =  b_y(z) P̄_e(z)
```

with b_y the y-weighted bias, and in the halo model as
⟨b_h P_e⟩ = ∫ dM (dn/dM) b_h(M) ∫ 4π r² P_e(r, M) dr
(arXiv:2210.08633, Eq. 18) [src]. In FLAMINGO the ratio is scale
independent for k < 0.03 h/Mpc, the range Salcido et al. average over, and
deviates above k > 0.1 h/Mpc from one-halo and non-linear terms [src:
arXiv:2605.11083, Sect. 2.2.1, Fig. 1]. The tomographic amplitude relates to
it by ⟨bP_e⟩ = (m_e c² (1+z)/σ_T)(dz/dχ)(dy/dz) b_y (arXiv:2006.14650,
Eq. 4); the total thermal pressure is P_th = 1.932 P_e for Y = 0.24
[src: Sect. II].

### Step 2. Measure
<!-- key: step-2-measure -->

**Galaxy × y** (arXiv:2210.08633) [src: Sects. 3.2, 4.1, 4.2]:
- Maps: galaxy overdensity per tomographic bin, HEALPix N_side = 2048, with
  imaging-systematics weight maps; y maps downgraded to the same N_side.
  SPT-SZ + Planck minimum-variance y in the South (fiducial), Planck MILCA
  (10′ beam, 40% Galactic and point-source masks) in the North.
- Estimator: NaMaster pseudo-C_ℓ; 14 logarithmic bandpowers with edges 150,
  195, 254, 332, 433, 564, 736, 959, 1251, 1631, 2126, 2772, 3614, 4712,
  6142.
- Covariance: jackknife on 75 (South) and 92 (North) k-means patches, with
  the Hartlap factor (N_JK − N_band − 2)/(N_JK − 1) (Eq. 26); it exceeds the
  analytic covariance by up to 20%. Reason: to capture spatial variation
  "beyond the analytical model". Because of the jackknife, ℓ < 150 is cut:
  the patches are smaller than those modes.

**Shear × y, real space** (arXiv:2506.07432): ξ_γt,y in 20 logarithmic
bins from 2.5′ to 250′ (see L2) modelled through the Hankel transform
ξ_γt,y(θ) = ∫ dℓ ℓ/2π J_2(ℓθ) C_κy(ℓ) (Eq. 10) [src: Sect. II.2.2]. The
covariance is Gaussian plus the one-halo connected non-Gaussian term,
without super-sample covariance, because tSZ cross-correlations are
dominated by Poisson fluctuations of massive haloes; the non-Gaussian part
is ~10%; it is computed at the best fit of a first run [src: Sect. II.3.1].

**Shear × y, harmonic space** (arXiv:2109.04458) [src: Sect. 2.3]:
shear maps at N_side 2048 with lensfit weights as masks; ellipticities
divided by (1 + m); 12 logarithmic bins in 51 ≤ ℓ ≤ 2952, of which only
100 ≤ ℓ ≤ 1500 are used, because the KiDS-1000 shear methodology was
validated only there; the full range would add ~10% in signal-to-noise.
Cross-spectra are computed on each map's own mask, not on the overlap.

**Clustering-based tomography** (arXiv:2006.14650) [src: Sect. III.2]:
cross-correlate each Planck and IRAS intensity map with SDSS spectroscopic
references in redshift bins; w̄_TR(z_i) = (dT/dz) b_T b_R w̄_DM (Eq. 8),
with b_R from the reference auto-correlation and w̄_DM from Halofit; the
angular range corresponds to fixed projected separations with
r_p,max = 8 Mpc. The bins are quasi-independent because the references are
spectroscopic [src: Sect. V.3.3].

### Step 3. Model
<!-- key: step-3-model -->

**Halo model for galaxy × y** (arXiv:2210.08633, Sects. 2.1–2.4) [src]:
- P_uv = P^1h + P^2h, with P^1h = ∫ dM (dn/dM) ⟨U V⟩ and
  P^2h = ⟨b_h U⟩⟨b_h V⟩ P_L (Eqs. 4–7); Tinker 2010 mass function.
- The one-to-two-halo transition is corrected by multiplying by
  R(k) = P_HaloFit/P_HaloModel (Eqs. 8–9).
- Pressure: GNFW, P_e(r) = P_* p(r/r_500c), p(x) = (c_P x)^−γ
  [1 + (c_P x)^α]^((γ−β)/α) (Eqs. 15–16), with (α, β, γ, c_P) =
  (1.33, 4.13, 0.31, 1.81) and
  P_* = P_0 (1.65 eV cm⁻³) h_70^(8/3) [h_70 (1 − b_H) M_500c / 3 × 10¹⁴ M_⊙]^0.79,
  P_0 = 6.41 (Eq. 17).
- Projection: Limber, C_ℓ^AB = ∫ dχ W_A W_B/χ² P_AB(k = (ℓ+½)/χ) (Eq. 22),
  with W_g = (H/c) n_g(z) and W_y = (σ_T/m_e c²)/(1+z) (Eqs. 20–21),
  justified for ℓ > 150; model spectra multiplied by the HEALPix window and
  by the Gaussian beam of the y map.
- Photo-z: shift Δz_i and stretch σ_z,i per bin (Eq. 23) with DES Gaussian
  priors.
- HOD: M_min = M_0 free U(10, 16) in log₁₀, σ_lnM = 0.15 fixed, M'_1 free,
  α_s U(0, 3), f_c = 1, satellites in an NFW with scale β_g truncated at
  β_max (Table 2, Eq. 14).

**Two regimes, fitted separately** (arXiv:2210.08633, Sect. 4.3) [src]:
1. Large scales, k_max = 0.7 Mpc⁻¹, ℓ_max,i = k_max χ(z̄_i) − ½ (864 to
   2320 over the six bins), b_H ~ U(0, 1), GNFW shape fixed to the Planck
   values "to make a fair comparison with other studies".
2. Small scales to k_max = 2.5 Mpc⁻¹, with the HOD fixed from step 1, free
   α ~ U(0.3, 4), β ~ U(0.2, 10), c_P ~ U(0.1, 5), γ = 0.31 fixed because
   the data are insensitive to it.
Why two: the one-to-two-halo transition of C^gg could not be modelled
coherently across both. Beyond k = 2.5 the model fails and small-scale
clustering systematics are less well corrected.

**Gas model coupled to matter, for shear × y** (arXiv:2506.07432,
Sect. II.2.1) [src]:
- Total halo mass conserved and split into central galaxy, gas and
  collisionless matter.
- ρ_gas(r) ∝ [1 + r/(θ_co r_200c)]^−β_gas [1 + (r/(θ_ej r_200c))^γ_gas]^−((δ_gas−β_gas)/γ_gas)
  (Eq. 1), normalised to f_gas M_tot with f_gas = Ω_b/Ω_m − f_star.
- Fixed γ_gas = 2.0, δ_gas = 7.0, θ_co = 0.05, "as the parameter space is
  substantially degenerate"; these defaults fit ANTILLES haloes of
  13.0 < log M < 14.5 at 0 < z < 1.
- θ_ej = θ_ej,0 (M_200c/M_*,ej)^ν_M (1+z)^ν_z with log₁₀ M_*,ej = 16
  (Eq. 2); β_gas = 3 (M/M_c)^μ_β / [1 + (M/M_c)^μ_β] with log₁₀ M_c = 13.75
  (Eq. 3).
- Pressure from hydrostatic equilibrium; non-thermal fraction
  R_nt = α_nt f(z) (r/r_200c)^n_nt with n_nt = 0.3 (Eq. 4); P_e =
  2(X_H + 1)/(5X_H + 3) P_th with X_H = 0.76.
- Transition regime: matter spectra multiplied by
  P_mm^halofit/P_mm^tot,nfw; for matter × pressure the one- and two-halo
  terms are combined as [(P^1h)^α_κy + (P^2h)^α_κy]^(1/α_κy), with
  α_κy free, because pressure has different exclusion effects from matter
  [src: Sect. II.2.2].
- Linear spectrum from an analytic approximation (better than 2% for these
  projected fields) to stay inside JAX [src: same].

**HMx for shear × y** (arXiv:2109.04458, Sect. 3.1) [src]: a halo model
fitted to BAHAMAS spectra, in which every gas parameter is tied to one
feedback parameter log₁₀(T_AGN/K); pressure–matter spectra are reproduced at
the 15% level for z < 2 and k ≲ 7 h/Mpc and matter–matter at 2%. HMx
predicts ratios to the gravity-only spectrum, which are more robust than
absolute spectra as cosmology varies.

**A simulation suite instead of a model** (arXiv:2609.31774, Sect. III.4)
[src]: the measured C^γy is compared with FLAMINGO matter–pressure spectra
through the Limber integral, with one free rescaling amplitude A_γtSZ. The
stated reason: this avoids "most of the inaccuracies and approximations
associated with the halo model" and inherits the simulations' calibration
to stellar mass functions and X-ray gas fractions; the cost is a limited
set of models. The released spectra are in comoving pressure and must be
multiplied by (1+z)³ [src: footnote 4].

### Step 4. Priors and nuisances of a shear × y fit
<!-- key: step-4-priors-and-nuisances-of-a-shear-x-y-fit -->

DES Y3 shear + shear × ACT DR6 y (arXiv:2506.07432, Table 1) [src]:

| Group | Parameter | Prior |
|---|---|---|
| Gas | θ_ej,0; ν_θej^z; ν_θej^M; μ_β | U[1, 6]; U[−3, 3]; U[−1, 1]; U[0.01, 1.5] |
| Non-thermal pressure | α_nt | U[0, 0.5] |
| Transition | α_κy | U[0.8, 1.2] |
| Cosmology | Ω_m; Ω_b; h; n_s; σ_8 | U[0.1, 0.5]; U[0.03, 0.07]; U[0.5, 0.9]; U[0.8, 1.2]; U[0.6, 1.0] |
| IA (NLA) | A_IA; η_IA | U[−5, 5]; U[−5, 5], z_0 = 0.62 |
| Shear calibration | m¹…m⁴ | N(−0.0063, 0.0091), N(−0.0198, 0.0078), N(−0.024, 0.0076), N(−0.037, 0.0076) |
| Source photo-z | Δ_z¹…Δ_z⁴ | N(0, 0.018), N(0, 0.015), N(0, 0.011), N(0, 0.017) |

The θ_ej,0 prior keeps ejected gas within 6 R_200c for log₁₀ M_200c ~ 16,
"expected even in high baryonic feedback simulations"; μ_β > 0 is
physically expected [src: Sect. II.2.1]. Changing the ranges of the
unconstrained parameters does not change the cosmological conclusions
[src: App. C].

Scale cuts: the whole 2.5′–250′ range is used, because the model includes
feedback; the DES Y3 shear-only analysis had cut small scales and lost
signal-to-noise from 40 to 27 [src: Sect. II.2.3]. One exception: below
10′ in the two lowest source bins of shear × y, where NLA underestimates
the intrinsic-alignment signal against a halo model of IA [src: same].
KiDS × y keeps A_IA free and η_IA fixed; IA is "small but significant",
comparable in relative size to its role in cosmic shear [src:
arXiv:2109.04458, Sect. 3.4.2].

Sampling: NUTS (numpyro), 64 chains, 8000 warm-up and 8000 samples each,
R − 1 < 0.01, about 6 hours on four H100 GPUs; checked against nested
sampling [src: arXiv:2506.07432, Sect. II.3.2].

### Step 5. Read the amplitude
<!-- key: step-5-read-the-amplitude -->

The shear × tSZ signal scales approximately as σ_8⁵ Ω_m, so KiDS × y
quotes Σ_8^0.2 = σ_8 (Ω_m/0.3)^0.2 (arXiv:2109.04458, Sect. 4) [src]. That
is the origin of the 0.2 exponent listed in L2. Halo-model scalings of
⟨b_h P_e⟩ are steep: ∝ (σ_8 Ω_m^0.81 h^0.67)^3.14 at z = 0, as cited
in arXiv:2605.11083 [src: Sect. 3.1]; in FLAMINGO, Planck cosmology gives
10–15% more ⟨b_h P_e⟩ than the fiducial, and Σm_ν = 0.24 eV about 7%
less than Planck [src: same].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Map-level y or spectrum-level separation
<!-- key: map-level-y-or-spectrum-level-separation -->

- **Component-separated y map.** Deprojecting a contaminant raises the map
  variance and needs its SED a priori; a wrong SED leaves an uninterpretable
  residual (arXiv:2609.31774, Sect. II.3) [src]. MILCA uses CIB templates,
  but "as the CIB-induced bias decreases, the noise level increases", and
  the CIB is not fully correlated across frequencies [src:
  arXiv:2210.08633, Sect. 3.2.2].
- **Spectrum-level (MLBR).** Model each frequency map as
  m_ν = S_ν^tSZ y + S̄_ν^CIB c + Ñ_ν, cross every map with the shear, and
  solve C̄ = Σ_c Sᵀ Σ⁻¹ d with Σ_c = (Sᵀ Σ⁻¹ S)⁻¹ (arXiv:2609.31774,
  Eqs. 10, 16–18) [src]. The CIB SED is averaged over each lensing kernel
  (Eq. 14) and its parameters are marginalised. Robustness tests: a free
  tilt δβ per bin (found 0.15 ± 0.11, −0.10 ± 0.09, −0.15 ± 0.07,
  −0.05 ± 0.05), a radio component with β_PS = −3 or −2, two CIB
  components per kernel; within the SED range allowed by the external
  infrared spectra U(z) the changes are a small fraction of the errors [src: Sect. III.2, Table 3].
- **Per-redshift SED fit.** The clustering-based method fits tSZ and a
  modified blackbody CIB at each redshift, keeping redshift information that
  "would otherwise be lost in any map-level component separation"; points
  above 4600 GHz rest frame are dropped to avoid mid-infrared emission
  [src: arXiv:2006.14650, Sect. V.2].
- **A scalar CIB leak.** y_obs = y_true + α_CIB I_CIB with the 545 GHz map
  and α_CIB = (2.3 ± 6.6) × 10⁻⁷ MJy⁻¹ sr; the authors call it simplistic
  (frequency-independent, spatially constant) but sufficient because the
  CIB proved negligible for KiDS × y [src: arXiv:2109.04458, Sect. 3.4.3,
  Eqs. 9–10].

### How much the CIB moves ⟨b_h P_e⟩
<!-- key: how-much-the-cib-moves-bh-pe -->

On the same DES Y3 galaxies (arXiv:2210.08633, Sect. 4.5, Table 4) [src]:
the predicted CIB leakage into C^gy is below 1% (median) for the SPT-SZ +
Planck minimum-variance map; with MILCA it is significant in the last three
bins and dominant in the last two. In those two bins b_H moves from
0.59 +0.08/−0.09 and 0.64 +0.08/−0.09 (raw MILCA) to 0.11 +0.07/−0.06 and 0.07 +0.08/−0.05 after subtracting a
predicted CIB map, in line with 0.10 for SPT-SZ + Planck. The leakage was
predicted by scaling the 353 GHz CIB map of Lenz et al. to each channel
with a CIB SED and passing it through the ILC weights (Eqs. 29–31). The
corrected MILCA values are kept as a cross-check only, not combined,
"given the size of the systematic CIB correction". Bins 4 and 5
(z̄ = 0.89, 0.97) are not part of the fiducial sample [src: Table 4
caption]. Other tests: deprojecting two reddening maps moves (1 − b_H) by
≤ 0.23σ; masking NVSS sources above 1 mJy at 1.4 GHz by ≤ 0.15σ, the MILCA
source-mask threshold being ~200 mJy at 143 GHz against ~6 mJy at 150 GHz
for SPT-SZ [src: Sect. 4.5].

### Halo model, physical gas model, or simulations
<!-- key: halo-model-physical-gas-model-or-simulations -->

| Approach | Buys | Costs | Used by |
|---|---|---|---|
| GNFW with free (1 − b_H) | comparison with cluster literature; ⟨b_h P_e⟩ per bin | one-to-two-halo transition must be patched (R(k)); HOD needed for C^gg | arXiv:2210.08633 |
| HMx, one T_AGN | gas and matter coupled; feedback and cosmology together | calibrated to one simulation family; 15% accuracy on pressure spectra | arXiv:2109.04458 |
| Baryonification-type gas + hydrostatic pressure | joint fit of shear and shear × y to all scales; P(k) suppression | six free gas, pressure and transition parameters, several slopes fixed | arXiv:2506.07432 |
| FLAMINGO spectra, free amplitude | no halo-model approximations | discrete set of models | arXiv:2609.31774 |

On the same kind of data the approaches give opposite S_8 readings (see
L2). One difference is visible in the papers: arXiv:2506.07432 fits a free
gas model and finds reduced pressure in haloes below 10¹⁴ M_⊙/h (see L2),
whereas arXiv:2609.31774 can lower the amplitude only through S_8 or the
discrete FLAMINGO feedback variants [der: comparison of the two model
sets]. Against fiducial
FLAMINGO the measured amplitude is A_γtSZ = 0.598 ± 0.015 (30 < ℓ ≤ 2000);
the strongest-feedback low-S_8 run gives 0.949 ± 0.024 [src:
arXiv:2609.31774, Table 4].

### Compiling ⟨b_h P_e⟩ across surveys
<!-- key: compiling-bh-pe-across-surveys -->

The S_8 = 0.72 ± 0.03 of L2 comes from 42 compiled measurements at z < 1
treated as independent, although all use Planck y maps; no FLAMINGO variant
reaches a reduced χ² below 2.92 (fiducial 4.87), and neighbouring bins
differ by more than statistical fluctuations allow, "suggesting the
presence of residual systematics and/or underestimated uncertainties"
[src: arXiv:2605.11083, Sect. 3.1, Table 3]. A reader should treat that
S_8 as a statement about the compilation.

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Linear-regime average for ⟨b_h P_e⟩ | k < 0.03 h/Mpc | FLAMINGO | arXiv:2605.11083 | Sect. 2.2.1 |
| Galaxy × y large-scale cut | k_max = 0.7 Mpc⁻¹; ℓ ≥ 150 | DES Y3 × SPT + Planck | arXiv:2210.08633 | Sect. 4.3 |
| Galaxy × y small-scale cut | k_max = 2.5 Mpc⁻¹ | same | arXiv:2210.08633 | Sect. 4.3 |
| Jackknife regions | 75 (South), 92 (North) | same | arXiv:2210.08633 | Sect. 4.2 |
| Jackknife against analytic covariance | larger by ≤ 20% | same | arXiv:2210.08633 | Sect. 4.2 |
| GNFW shape (Planck 2013) | (α, β, γ, c_P) = (1.33, 4.13, 0.31, 1.81); P_0 = 6.41 | same | arXiv:2210.08633 | Sect. 2.3 |
| CIB leakage into C^gy | median < 1% (SPT-SZ + Planck); dominant in bins 4–5 (MILCA) | same | arXiv:2210.08633 | Sect. 4.5 |
| Shear × y range | 2.5′–250′, except < 10′ removed in source bins 1–2 | DES Y3 × ACT DR6 | arXiv:2506.07432 | Sect. II.2.3 |
| cNG covariance share | ~10% | same | arXiv:2506.07432 | Sect. II.3.1 |
| Fixed gas slopes | γ_gas = 2.0, δ_gas = 7.0, θ_co = 0.05 | same | arXiv:2506.07432 | Sect. II.2.1 |
| KiDS × y multipoles | 100 ≤ ℓ ≤ 1500 (8 bins) | KiDS-1000 × Planck, ACT | arXiv:2109.04458 | Sect. 2.3 |
| HMx accuracy | 15% (pressure × matter), 2% (matter) | BAHAMAS | arXiv:2109.04458 | Sect. 3.1 |
| Shear × tSZ scaling | ∝ σ_8⁵ Ω_m | KiDS-1000 | arXiv:2109.04458 | Sect. 4 |
| Σ_8^0.2 | 0.723 +0.046/−0.032 (MILCA) | KiDS-1000 × Planck | arXiv:2109.04458 | Eq. 11 |
| A_γtSZ against fiducial FLAMINGO | 0.598 ± 0.015; LS8: 0.854 ± 0.022 | DES × Planck frequency maps | arXiv:2609.31774 | Table 4 |
| Clustering-redshift scale | r_p,max = 8 Mpc | SDSS × Planck, IRAS | arXiv:2006.14650 | Sect. III.2 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **CIB in the y map.** Shows up as ⟨b_h P_e⟩ or b_H that drift with
  redshift and with the map. Test: predict y^CIB = wᵀ x^CIB through the ILC
  weights and cross it with the tracer [src: arXiv:2210.08633, Eqs. 29–31];
  compare a minimum-variance and a CIB-nulled map; fit a δβ tilt per bin
  [src: arXiv:2609.31774, Sect. III.2].
- **Radio sources.** Test: extra NVSS mask [src: arXiv:2210.08633,
  Sect. 4.5]; a radio component in the mixing matrix
  [src: arXiv:2609.31774, Eq. 20]; masking ACT point and extended sources,
  to which the DES × ACT cosmology is robust [src: arXiv:2506.07432,
  App. C].
- **Galactic dust.** Test: deproject reddening templates; shifts ≤ 0.23σ
  [src: arXiv:2210.08633, Sect. 4.5].
- **Halo-model transition.** C^gg excess not described by the one-halo term
  from ℓ ~ 3000 (θ ~ 3.6′), consistent with small-scale clustering
  systematics [src: arXiv:2210.08633, Sect. 5]. Test: fit regimes
  separately; free transition parameter α_κy [src: arXiv:2506.07432,
  Sect. II.2.2].
- **Intrinsic alignments in shear × y.** Strongest where tSZ weights massive
  haloes; NLA fails below 10′ at low source redshift [src:
  arXiv:2506.07432, Sect. II.2.3].
- **Jackknife covariance on large scales.** Inaccurate when the mode exceeds
  the patch: drop ℓ < 150 [src: arXiv:2210.08633, Sect. 4.3].
- **Compilations treated as independent.** Shared y maps; reduced χ² 3–6
  against smooth models [src: arXiv:2605.11083, Sect. 3.1].
- **Pressure units from simulations.** FLAMINGO releases comoving pressure
  [src: arXiv:2609.31774, footnote 4].

## Reading list
<!-- key: reading-list -->

- Foundation: Komatsu 2002, arXiv:astro-ph/0205468 — halo-model tSZ
  spectrum (in L2).
- Foundation: Arnaud 2009, arXiv:0910.1234 — universal pressure profile
  (in L2).
- Method: Chiang 2020, arXiv:2006.14650 — clustering-based tSZ tomography;
  per-redshift SED fit.
- Application: Sánchez 2022, arXiv:2210.08633 — galaxy × y halo model, two
  regimes, jackknife, CIB leakage test.
- Application: Tröster 2021, arXiv:2109.04458 — KiDS × y with HMx; the 0.2
  exponent; scalar CIB model.
- Application: Pandey 2025, arXiv:2506.07432 — coupled gas model, priors,
  covariance, NUTS.
- Method: Wayland 2026, arXiv:2609.31774 — spectrum-level component
  separation; FLAMINGO amplitude.
- Critique: Salcido 2026, arXiv:2605.11083 — ⟨b_h P_e⟩ definition, its
  cosmology and feedback dependence, limits of the compilation.

## Not verified
<!-- key: not-verified -->

- The HOD parameter ρ_gy and β_max priors of arXiv:2210.08633, Table 2:
  their definitions (Koukoufilippas et al. 2020) were not read.
- The halo-model scaling of Chen et al. 2024: quoted from arXiv:2605.11083.
- The ACT DR6 y map construction used in arXiv:2506.07432 beyond the
  parameters in L2.
- Gatti 2021 and Pandey 2019 modelling sections (only L2 statements).
