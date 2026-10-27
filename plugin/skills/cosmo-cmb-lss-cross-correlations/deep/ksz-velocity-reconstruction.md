# kSZ velocity reconstruction — cosmo-cmb-lss-cross-correlations dossier

Scope: how a kSZ velocity-reconstruction measurement is built (CMB filter,
quadratic estimator, noise, power-spectrum estimator, window and covariance
by surrogate fields or analytic Gaussian, fit and nuisance treatment), in
its 3D spectroscopic, 3D photometric and 2D tomographic forms, and how to
choose between them.
Snapshot: 2026-10-17.
From: Baxter 2022 Snowmass review (arXiv:2203.06795), Sect. II.2
("Cosmology with the kSZ effect").

Already in L2: origins, estimator equivalence and the b_v definition
(`physics-and-methods.md#estimators`); b_v and f_NL values
(`results.md#velocities-cosmology-from-the-large-scale-ksz`); b_fg values
and the parity-odd mitigation
(`systematics.md#ksz-foregrounds-and-map-systematics`); noise rescalings
(`systematics.md#covariance-and-noise-models`); the ELG HOD problem
(`systematics.md#ksz-the-optical-depth-degeneracy`).

Notation: arXiv:2604.04867 (3D) and arXiv:2506.21684 (2D). χ_*: distance
to the sample; K(χ) = −T_CMB σ_T n_e,0 x_e e^−τ (1+z)² (arXiv:2604.04867,
Eq. 3); P_ge: galaxy–electron spectrum; P_gg^tot, C_ℓ^tot: galaxy and CMB
totals with noise; b_ℓ: beam.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Choose the geometry
<!-- key: step-1-choose-the-geometry -->

Two families are in use.

| Family | Velocity output | Large-scale statistic | Analyses |
|---|---|---|---|
| 3D | v̂_r(x) on a 3D mesh, galaxies at their (spectroscopic or photometric) redshift | Fourier multipoles P_ℓ^gv(k), P_ℓℓ'^vv(k) | Hotinli 2025 (arXiv:2506.21657), DESI Legacy LRG photometric; Chaussidon 2026 (arXiv:2604.04867), DESI DR2 spectroscopic |
| 2D tomographic | one v̂^α(n̂) map per redshift bin α | angular C_L between bins | McCarthy 2024 (arXiv:2410.06229), McCarthy 2025 (arXiv:2511.15701), Lai 2025 (arXiv:2506.21684), Bloch 2024 (arXiv:2405.00809) |

The 3D estimator is that of Smith 2018 (arXiv:1810.13423), implemented with
surrogate fields in arXiv:2506.21657 [src: arXiv:2604.04867, Sect. III.1];
the 2D ones are listed in arXiv:2410.06229 [src: Sect. 3.1.2].

### Step 2. Filter the CMB
<!-- key: step-2-filter-the-cmb -->

The CMB enters only through a filtered map evaluated at the galaxy
positions (arXiv:2604.04867, Eqs. 20–21):

```
T̃_lm = F_l ∫ d²θ W_CMB(θ) T_CMB(θ) Y*_lm(θ)
F_l  = [P_ge^fid(l/χ_*) / P_gg^fid(l/χ_*)] × b_l / C_l^tot
```

W_CMB is a pixel weight. Both 3D analyses set it to 1 where the noise is
below 70 μK-arcmin in both 90 and 150 GHz and 0 elsewhere, and add the
Planck GAL070 Galactic mask [src: arXiv:2506.21657, Eq. 37;
arXiv:2604.04867, Sect. IV.1]. The photometric analysis sets F_l = 0 below
l_min = 2000, "to additionally suppress scales dominated by primary CMB",
and above l_max = 9000; its filters peak at l ~ 2000–4000, where the bulk of
the signal-to-noise comes from [src: arXiv:2506.21657, Sect. IV.1, Fig. 2].
The DR2 filters peak around l ~ 4000 [src: arXiv:2604.04867, Fig. 2
caption]. The 2D estimator sums ℓ_1, ℓ_2 over [300, 10000]; going below 300
changes the noise by under a percent [src: arXiv:2506.21684, Sect. 2.2].

Daynight ACT maps are used although their beam is worse on small scales
because they are less noisy; the photometric paper notes that daynight
temperature is less reliable at l ≳ 4000 while its filters peak around
l ~ 3000, and the DR2 paper checked that the choice does not bias the result [src: arXiv:2506.21657,
Sect. IV.1; arXiv:2604.04867, Sect. IV.1]. Masking tSZ clusters was found
unnecessary in 3D once the mean-subtraction of Step 3 is applied [src:
same]; the 2D analysis with continuity velocities masks clusters, and with
them masked the measured velocity auto-power matches the analytic N^(0)
[src: arXiv:2511.15701, Fig. 11 caption].

**Matching the two frequencies.** Both 3D analyses rescale the 150 GHz
filter by a beam ratio so that b_v^90 = b_v^150 and the 150 − 90 difference
is kSZ-free, at some loss of signal-to-noise [src: arXiv:2506.21657,
Eq. 36; arXiv:2604.04867, Eq. 39]. The two papers write the ratio the other
way round (b_l^90/b_l^150 in arXiv:2506.21657, b_l^150/b_l^90 in
arXiv:2604.04867).

Equal b_v requires b_l F_l to be equal at the two frequencies, which is the
form of arXiv:2506.21657 [der, from Eq. 25 of arXiv:2604.04867].

### Step 3. Build the velocity field
<!-- key: step-3-build-the-velocity-field -->

In 3D the estimator is a weighted sum over galaxies i in redshift bins b
(arXiv:2604.04867, Eq. 19):

```
v̂_r(x) = Σ_b Σ_{i∈b} W_i^v [T̃(θ_i) − T̃_b] δ³(x − x_i)
```

T̃_b is the weighted mean filtered temperature of the galaxies in bin b,
subtracted in 25 redshift bins "to reduce the CMB foregrounds as empirically
found" in arXiv:2506.21657; it removes only additive contributions slowly
varying in redshift and induces a radial integral constraint, which is then
modelled [src: arXiv:2604.04867, Sect. III.1]. Its mean obeys
⟨v̂_r⟩ = b_v B(x) n_v(x) v_r^true(x), with the normalisation

```
B(χ, θ) = W_CMB(θ) K(χ)/χ² ∫ d²L/(2π)² b_L F_L P_ge^fid(L/χ)      (Eq. 23)
```

evaluated at z_eff, giving B ≃ −642621, −44882 and −341092 μK⁻¹ for LRG,
ELG and QSO; B is negative by the sign convention of the kSZ term [src:
arXiv:2604.04867, Eqs. 22–24]. v̂_r is in Mpc⁻³ μK⁻¹, not dimensionless;
the units are carried through the surrogates [src: Sect. III.2].

Per-galaxy weights. DESI DR2: W = w_comp w_sys w_zfail w_FKP for both
density and velocity, with P_0 = 5 × 10⁴, 2 × 10⁴ and 3 × 10⁴ (h⁻¹Mpc)³
for LRG, ELG, QSO; the authors defer an optimal velocity weight to future
work [src: arXiv:2604.04867, Sect. IV.2, Eq. 40]. Photometric: W_i =
exp[−σ_z,i²/(α (1+z_i)²)] with α = 0.0025, which down-weights objects whose
photo-z error is large against the velocity correlation length; galaxies
with σ_z/(1+z) ~ 0.08 lose about 90% or more of their weight [src:
arXiv:2506.21657, Eq. 39, Fig. 3]. In the photometric 3D analysis the
delta functions sit at observed redshifts while the surrogate fields are
evaluated at true redshifts drawn from a deconvolved (z_obs, z_true, σ_z)
distribution [src: Sect. III.5, Eqs. 34–35].

In 2D the estimator in bin α is (arXiv:2506.21684, Eq. 8)

```
v̂^α_lm = N_ℓ^vv,α Σ (−1)^{m+1} Γ^α_{ℓ1ℓ2ℓ} (ℓ1 ℓ2 ℓ; m1 m2 −m) a_ℓ1m1 δ^α_g,ℓ2m2 / (C_ℓ1^TT C_ℓ2^gg,α)
Γ^α_{ℓ1ℓ2ℓ} = sqrt[(2ℓ1+1)(2ℓ2+1)(2ℓ+1)/4π] (ℓ1 ℓ2 ℓ; 0 0 0) C_ℓ2^τg,α          (Eq. 9)
1/N_ℓ^vv,α = (1/(2ℓ+1)) Σ_{ℓ1ℓ2} (Γ^α)² / (C̃_ℓ1^TT C̃_ℓ2^gg,α)                    (Eq. 13)
```

computed in pixel space as v^α(n̂) = −N^vv,α a′(n̂) δ′_g^α(n̂) with
inverse-variance-filtered maps at N_side = 4096 (Eqs. 11–12); C̃^TT and
C̃^gg are measured on the data with pseudo-C_ℓ [src: Sect. 2.2]. The
projected velocity is a redshift-weighted integral of v_r, accurate "to
within a few percent" with the galaxy dN/dχ of the bin as weight
(arXiv:2410.06229, Eqs. 14–15) [src]. The optical-depth bias is then one
parameter per bin, or one overall (arXiv:2511.15701, Eq. 20):

```
b_v^α ≃ Σ_ℓ (2ℓ+1) C_ℓ^τg_α [C_ℓ^τg_α]^true / (C_ℓ^TT C_ℓ^gαgα)  ÷  Σ_ℓ (2ℓ+1) (C_ℓ^τg_α)² / (C_ℓ^TT C_ℓ^gαgα)
```

### Step 4. Predict the noise
<!-- key: step-4-predict-the-noise -->

The leading reconstruction noise, called the kSZ N^(0) bias by analogy with
CMB lensing, tends to a constant on large scales (Giri & Smith 2020,
arXiv:2010.07193, Eq. 27):

```
N^(0)_vr(k_L → 0) = (χ_*⁴/K_*²) [ ∫ d²l/(2π)² P_ge(l/χ_*)² / (P_gg(l/χ_*) C_l^tot) ]⁻¹
```

It is proportional (arXiv:2010.07193) to C_l^tot on kSZ scales (l ~ 5000), so it falls as the
CMB noise falls [src: Sect. VI.4]. In 100 Quijote simulations the true noise
was larger, consistent with a factor 2–3 increase, explained by an
N^(3/2) term from a six-point halo-model calculation; N^(1) is negligible
[src: Sects. V.2, VI.4]. N^(3/2) does not depend on CMB noise, so it grows
in relative importance with deeper CMB data or denser galaxy samples; the
authors expect it to be small for DESI with Simons Observatory and possibly
important for Rubin or CMB noise ≲ 1 μK-arcmin [src: Sect. VI.4]. Their
simulations used 0.5 μK-arcmin, 1′ beam and DESI-like galaxies [src: same].

### Step 5. Measure the large-scale spectra
<!-- key: step-5-measure-the-large-scale-spectra -->

3D (arXiv:2604.04867, Eqs. 28–32). With a spin-ℓ Fourier transform 𝓕_ℓ
(Eq. 28, ε = i for odd ℓ), v_r = 𝓕_1[faH δ_m/k] (Eq. 30) and

```
P̂_ℓ^gv(k)    = (2ℓ+1)/𝒩_gv ∫ dΩ_k/4π 𝓕_0[δ̂_g](k) 𝓕_ℓ[v̂_r](−k)                 (Eq. 31)
P̂_ℓℓ'^vv(k)  = (2ℓ+1)(2ℓ'+1)/𝒩_vv ∫ dΩ_k/4π 𝓕_ℓ[v̂_r](k) 𝓕_ℓ'[v̂_r](−k)        (Eq. 32)
```

δ̂_g is the FKP field and 𝒩 an FKP-type normalisation from the randoms
[src: Sect. III.4]. Because velocities are sampled at galaxies, Eq. 31 is
formally the galaxy–momentum spectrum, equal to P^gv on linear scales [src:
same]. The authors use P̂_11^vv rather than the monopole: μ-weighting is the
optimal way to extract the μ dependence (Tegmark et al. 1997, as cited) and
reduces foreground impact [src: Sect. III.4, App. E]. On the same LRG data
the monopole version gives SNR 1.51 against 3.11 [src: App. E, Table 10].
Mesh: 10 Mpc cells in DR2; 15 Mpc with 3000 Mpc padding against
periodic-boundary artefacts in arXiv:2506.21657 [src: Sect. III.5.4;
Sect. IV.2].

2D. Angular cross-spectra of v̂^α with the galaxy overdensity or with a
continuity-equation velocity in bin β, for all bin pairs. arXiv:2511.15701
uses 4 or 16 bins and four bandpowers between L_min = 6 and L_max = 53 [src:
Sect. 2.2.1, Table 2]; arXiv:2506.21684 uses 20 bins of Δz = 0.03 over
0.4 < z < 1.0 and a QML estimator on N_side = 32 maps for the large scales
[src: Sect. 2.1.2].

### Step 6. Model
<!-- key: step-6-model -->

Linear theory in redshift space (arXiv:2604.04867, Eqs. 10–17):

```
v_r^s(k, μ) = b_v (i f a H μ / k) D_v(k, Σ_v) δ_m(k),    D_v = sinc(k Σ_v)
P_1^gv = (b_1 + 3f/5) b_v (i f a H / k) P_lin(k)
P_3^gv = (2/5) b_v (i f² a H / k) P_lin(k)
P_0^vv = −(1/5) b_v² (f a H / k)² P_lin(k)
```

With primordial non-Gaussianity (arXiv:2604.04867) b_1 → b_1 + b_Φ f_NL / T_Φ→δ(k, z) (Eq. 6),
b_Φ = 2δ_c (b_1 − p), δ_c = 1.686, p = 1.0 for LRG and ELG and 1.4 for
quasars; the authors note that p for LRGs and ELGs needs further study
[src: Sect. II.3, Eq. 9]. The window is not applied as a matrix: model and
covariance are forward-modelled through the survey with surrogate fields
(Step 7) [src: Sect. II.5].

The 2D analysis with continuity velocities needs a simulation-calibrated
transfer function T_L for the continuity reconstruction, v^cont = T v^true
+ n, because a high correlation coefficient does not guarantee an unbiased
cross-power and a low one does not preclude it (arXiv:2511.15701, Eqs.
36–40) [src: Sect. 5.2.1]. T_L is calibrated for every bin pair with the
survey geometry [src: same].

### Step 7. Window and covariance: surrogate fields
<!-- key: step-7-window-and-covariance-surrogate-fields -->

A surrogate is a Gaussian field with the linear matter power spectrum,
scaled by the growth factor, "painted" onto the randoms, with a noise term;
it is not a mock catalogue (arXiv:2604.04867, Sect. III.5.1) [src]. Each
parameter multiplies its own basis field (Eqs. 33–36): for galaxies b_1,
f, b_Φ f_NL and shot noise s_n; for each frequency b_fg, b_v D_v and the
reconstruction noise s_nv. The noise field takes the real filtered ACT map
at a random subset of N_g randoms, the same subset for both frequencies, so
that common noise is kept [src: Sect. III.5.3, Eq. 38]. The mean over
surrogates is the model, their scatter the covariance; the basis spectra are
precomputed so that a likelihood call is a linear combination [src:
Sect. III.5.1]. Because random redshifts are drawn from the data and the
mean is subtracted in 25 bins, each surrogate component is mean-subtracted
in the same 25 bins to reproduce the radial integral constraint [src:
Sect. III.5.3]. Why surrogates: an inexpensive, parameter-dependent
covariance that includes geometry and window "without requiring large
ensembles of realistic simulations"; valid at k < 0.07 Mpc⁻¹ where
higher-order terms are negligible [src: Sect. III.5.1]. Masks, wide angles
and the global integral constraint come for free; the angular integral
constraint is not treated because P_gg at large scales is not used [src:
Sect. III.5.3].

The 2D analyses use instead an analytic Gaussian (Knox) covariance with
NaMaster mask decoupling and all inter-bin terms (arXiv:2511.15701,
Eq. 15), validated by redshift-shuffled nulls (Table 2) [src: Sect. 3.3];
or 6800 null simulations (arXiv:2410.06229, Sect. 5.3) [src].

### Step 8. Fit
<!-- key: step-8-fit -->

In DR2 [src: arXiv:2604.04867, Sects. III.5.2, IV.2, V.1, V.2]:

1. Fit (arXiv:2604.04867, Sects. III.5.2, IV.2, V.1, V.2) b_fg^90 and b_fg^150 to the P_0^gv monopole, then fix them; their
   leakage into the dipole stays below ~10% of the statistical errors for
   LRGs.
2. Fit (arXiv:2604.04867, Sects. III.5.2, IV.2, V.1, V.2) P_11^vv to get the three noise rescalings s_nv^90, s_nv^150,
   s_nv^90×150 (the last models the 90–150 cross-covariance).
3. Fit (arXiv:2604.04867, Sects. III.5.2, IV.2, V.1, V.2) the P_1^gv dipoles of both frequencies, alone or with P_11^vv.
   Free: f_NL, b_v^90, b_v^150, Σ_v (and Σ_v^vv with P^vv). Fixed: f to its
   fiducial value, b_1 from the separately measured P_gg amplitude, Σ_g = 0.
   The reason: without P_gg, P^gv alone has degeneracies among b_1, f and
   b_v and between Σ_g and Σ_v.
4. The covariance is evaluated once at the fiducial values of Table 4,
   obtained by iterating on the data, because inversion dominates the cost.
5. NGC and SGC spectra (arXiv:2604.04867, Sects. III.5.2, IV.2, V.1, V.2) are combined as P = w_1 P_NGC + (1 − w_1) P_SGC,
   w_1 the ratio of normalisations (0.57–0.59); NGC carries ~60% of the
   constraining power.

Hartlap and Percival factors are applied; enough surrogates are drawn that
the combined correction is ~5% (4500 for LRG, 2000 for ELG and QSO); the
Percival factor is left out when computing χ² and PTE [src: Sect. III.5.1,
Table 2]. The photometric 3D analysis fits only {f_NL, b_v} with k_max =
0.018 Mpc⁻¹ and fixed b_g = 2.2, because P_gv alone constrains only b_g b_v
and (b_g − 1) b_v f_NL [src: arXiv:2506.21657, Sect. V.3].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### 3D or 2D tomographic
<!-- key: 3d-or-2d-tomographic -->

- **3D** uses the radial information of each galaxy, gives Fourier
  multipoles that separate foreground (even ℓ) from velocity (odd ℓ), and
  reaches k_min = 0.0014 Mpc⁻¹ [src: arXiv:2604.04867, Sect. III.3,
  Table 1]. It needs a 3D window model (surrogates) and, with photometric
  data, a model of the photo-z scatter [src: arXiv:2506.21657, Sect. III.5].
- **2D** works with HEALPix maps and standard pseudo-C_ℓ or QML tools,
  needs only per-bin dN/dz, and has one b_v^α per bin (16 parameters in
  arXiv:2511.15701) [src: Sects. 2.2.1, 4.1.2]. The projection kernel of
  each bin is approximated by the galaxy dN/dχ to a few percent
  (arXiv:2410.06229, Sect. 3.1.2) [src].
- No paper read here compares both on the same data. The DR2 paper defers
  the comparison with the photometric 3D analysis to a paper in preparation
  [src: arXiv:2604.04867, Sect. V.5].

### Spectroscopic or photometric galaxies
<!-- key: spectroscopic-or-photometric-galaxies -->

Spectroscopic redshifts allow an explicit foreground model with "a
negligible impact" and P^vv detection; ELGs and quasars become usable
(arXiv:2604.04867, abstract) [src]. Photometric samples bring volume and
number: 3,958,201 DESI Legacy LRGs over 3442 deg² in the North-only 3D
analysis, against 2,870,615 DR2 LRGs over ~5500 deg² [src:
arXiv:2506.21657, Sect. IV.2; arXiv:2604.04867, Table 3]. The cost is
radial resolution: the photometric 3D fit stops at k_max = 0.018 Mpc⁻¹
against 0.07 for P^gv with spectra [src: arXiv:2506.21657, Sect. V.3;
arXiv:2604.04867, Table 1]. The photometric analysis dropped the Galactic
South because DES-processed imaging produced visible artefacts and
systematics in the analysis [src: arXiv:2506.21657, Sect. IV.2].

### What the reconstructed velocity is crossed with
<!-- key: what-the-reconstructed-velocity-is-crossed-with -->

| Partner field | What it adds | Cost | Analysis |
|---|---|---|---|
| Galaxy overdensity (P^gv, C^vg) | the f_NL scale dependence through b_Φ | b_1 must come from P_gg; equal-z 2D spectra show foreground signs (see L2) | arXiv:2604.04867; arXiv:2506.21684; arXiv:2511.15701 |
| External velocity template (BOSS) | a test of the velocity itself | a separate survey; one amplitude A = 0.638 ± 0.17, 3.8σ | arXiv:2410.06229, Sect. 5.3 [src] |
| Continuity-equation velocity | no foreground signs seen | simulation-calibrated T_L for every bin pair | arXiv:2511.15701, Sect. 5.2 [src] |
| Itself (P^vv) | cosmic-variance-limited cross-check; −23% on σ(f_NL) for DR2 LRG | noise-dominated; 3.1σ | arXiv:2604.04867, Sect. V.2 [src] |

Why P^vv helps f_NL although it carries no f_NL: it constrains b_v and so
breaks the b_v–f_NL degeneracy of P^gv, and makes the posteriors more
Gaussian [src: arXiv:2604.04867, Sect. V.2, Fig. 7 caption].

### Fiducial P_ge and the meaning of b_v
<!-- key: fiducial-pge-and-the-meaning-of-bv -->

All the analyses read here take P_ge^fid from a halo model (hmvec) with the
Battaglia "AGN" gas profile and an abundance-matching HOD [src:
arXiv:2506.21657, Sect. V.3; arXiv:2604.04867, Sect. V.5]. The fiducial is
not very sensitive to the assumed galaxy density: d log P_ge^fid / d log
n_g ≈ 0.3 [src: arXiv:2506.21657, Sect. V.3]. b_v depends on the CMB
data (through C_ℓ^TT) and on the binning and C_ℓ^gg of the galaxy survey,
so "care should therefore be taken when comparing the measurement of b_v
from different data combinations and analysis choices" [src:
arXiv:2511.15701, Sect. 4.1.2]. A growth measurement is out of reach until
b_v is known: cosmology from these spectra is limited to scale-dependent
effects such as f_NL [src: same]. Giri & Smith note a way out: with RSD
included, the μ⁰ and μ² terms of ⟨g v_r⟩ constrain f/b_g without b_v
(proposed in their ref. [77], not read) [src: arXiv:2010.07193, Sect. VIII].

### Which CMB map and which foreground treatment
<!-- key: which-cmb-map-and-which-foreground-treatment -->

- Lensing and the moving lens cannot bias ⟨v̂_r⟩ by symmetry: lensing is odd
  under T_prim → −T_prim, the moving lens under reversal of the transverse
  velocity; tSZ and CIB are even under radial reflection, which is exact in
  a snapshot but only approximate on a light cone [src: arXiv:2604.04867,
  Sect. III.3; arXiv:2010.07193, Sect. VIII]. What survives is the b_fg δ_m
  term, removed by modelling (spectroscopic) or mean subtraction and
  cluster masking.
- With Planck and unWISE the dominant contaminant was a coupling between
  the CIB and large-scale galaxy-survey systematics; the authors develop a
  method to minimise it (Bloch 2024, arXiv:2405.00809) [src].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| CMB filter range | l = 2000–9000; peak 2000–4000 | DESI LS × ACT DR5, 3D | arXiv:2506.21657 | Sect. IV.1 |
| 2D estimator range | ℓ_1, ℓ_2 ∈ [300, 10000], N_side 4096 | DESI LS × ACT DR6, QML | arXiv:2506.21684 | Sect. 2.2 |
| k range, P^gv | 0.0014–0.07 Mpc⁻¹; Δk 0.0014 (k < 0.01), 0.0028 above; 28 bins | DESI DR2 | arXiv:2604.04867 | Table 1 |
| k range, P^vv | 0.0014–0.05 Mpc⁻¹; 21 bins | DESI DR2 | arXiv:2604.04867 | Table 1 |
| Data vector | 56 (P^gv, two frequencies), 63 (P^vv, three combinations) | DESI DR2 LRG | arXiv:2604.04867 | Sect. III.4 |
| k_max, photometric 3D | 0.018 Mpc⁻¹, 9 bandpowers per frequency | DESI LS | arXiv:2506.21657 | Sect. V.3 |
| 2D bandpowers | 4, 6 ≤ L ≤ 53; 4 or 16 bins | DESI LS × ACT DR6 | arXiv:2511.15701 | Table 2 |
| Surrogates | 4500 (LRG), 2000 (ELG, QSO); Hartlap + Percival ≈ 5% | DESI DR2 | arXiv:2604.04867 | Sect. III.5.1, Table 2 |
| Normalisation B | −642621 (LRG), −44882 (ELG), −341092 (QSO) μK⁻¹ | DESI DR2 | arXiv:2604.04867 | Eq. 24 |
| Fiducial b_1, p | 2.1, 1 (LRG); 1.3, 1 (ELG); 2.48, 1.4 (QSO) | DESI DR2 | arXiv:2604.04867 | Table 4 |
| Foreground leakage into dipole | < ~10% of statistical errors (LRG) | DESI DR2 | arXiv:2604.04867 | Sect. V.1 |
| P^vv gain on f_NL | −23% on σ(f_NL) | DESI DR2 LRG | arXiv:2604.04867 | Sect. V.2 |
| P_11^vv against P_00^vv | SNR 3.11 against 1.51 | DESI DR2 LRG | arXiv:2604.04867 | App. E, Table 10 |
| Photometric 3D result | SNR 11.7; f_NL = −39 +40/−33; b_v = 0.45 +0.06/−0.05 | DESI LS × ACT DR5 | arXiv:2506.21657 | Sect. V.3 |
| Template cross | A = 0.638 ± 0.17; Δχ² = 14.06; 3.7σ (sims), 3.9σ (analytic) | DESI LS × ACT DR6 × BOSS | arXiv:2410.06229 | Sect. 5.3 |
| Noise excess over N^(0) in N-body | factor ~2–3, explained by N^(3/2) | Quijote, 0.5 μK-arcmin | arXiv:2010.07193 | Sects. V.2, VI.4 |
| b_v scale dependence | 1 on large scales; ≈ 2.4 at k = 0.1 Mpc⁻¹; constant for k ≲ 0.01 | Quijote | arXiv:2010.07193 | Sect. V.2 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Noise underestimated by the surrogate bootstrap.** For dense samples
  (LRGs, where 1/n̄ is small against C_ℓ^gg) s_nv > 1; not seen for ELGs
  and quasars; a block bootstrap is suggested [src: arXiv:2604.04867,
  Sect. V.2]. Test: fit s_nv on P^vv and propagate it to the covariance.
- **Higher-order noise.** N^(0) alone underpredicts the noise in N-body by
  a factor 2–3 [src: arXiv:2010.07193, Sect. V.2]. Test: compare the
  measured velocity auto-power with N^(0), as in arXiv:2511.15701, Fig. 11.
- **Foreground monopole leaking into the dipole** through the window [src:
  arXiv:2604.04867, Sect. III.3]. Test: fit the P_0^gv monopole; check that
  b_fg^90/b_fg^150 follows the tSZ ratio; residual sign opposite to tSZ on the
  largest scales, possibly dust or ISW, is left unmodelled [src: Sect. V.1].
- **Radial integral constraint from the mean subtraction.** Unmodelled, it
  biases the spectrum [src: arXiv:2604.04867, Sect. III.1]. Test:
  mean-subtract every surrogate component in the same bins.
- **Imaging systematics** in a photometric sample. Test: large-scale P_gg
  excess; restrict the footprint (Galactic North only in arXiv:2506.21657,
  Sect. IV.2). With spectra, the P^gv dipole showed no large-scale excess
  for any tracer [src: arXiv:2604.04867, Sect. IV.2].
- **Photo-z outliers.** Adding the σ_z weight brought the reduced χ² of the
  QML galaxy–velocity spectra from 1.5 to 1.02 [src: arXiv:2506.21684,
  Sect. 2.1.2, footnote].
- **Continuity velocity mistaken for an unbiased template.** Test: calibrate
  T_L on simulations with the survey geometry and compare C^cont,cont
  between data and simulations [src: arXiv:2511.15701, Sect. 5.2.1].

Null tests and their pass criteria as stated:

| Test | Criterion | Analysis |
|---|---|---|
| 150 − 90 GHz dipole (beam-matched) | consistent with zero; PTE 0.69 (daynight), 0.996 (night) to k = 0.018 | arXiv:2506.21657, Sect. V.4; arXiv:2604.04867, App. C |
| CMB map rotated by 4° in declination | PTE > 0.05 with b_v = 0 for 90, 150, 150−90 and joint | arXiv:2506.21657, Table 2 |
| Shuffled small-scale galaxy redshifts | χ² to zero acceptable (PTE 0.33–0.86) | arXiv:2511.15701, Table 2 |
| NGC against SGC | no point in tension; data-vector and likelihood combinations agree | arXiv:2604.04867, App. B |
| Null simulations for the template cross | 2 of 6800 exceed the measured Δχ² | arXiv:2410.06229, Sect. 5.3 |

## Reading list
<!-- key: reading-list -->

- Foundation: Smith et al. 2018, arXiv:1810.13423 — estimator in the
  snapshot geometry; the bispectrum view.
- Foundation: Deutsch et al. 2017, arXiv:1707.08129 — remote dipole field
  reconstruction.
- Method: Cayuso et al. 2021, arXiv:2111.11526 — harmonic-space quadratic
  estimators.
- Critique: Giri & Smith 2020, arXiv:2010.07193 — N-body test; N^(3/2)
  noise; b_v scale dependence; symmetry arguments against foreground bias.
- Application: Bloch 2024, arXiv:2405.00809 — Planck × unWISE; CIB coupled
  to galaxy systematics.
- Application: McCarthy et al. 2024, arXiv:2410.06229 — first ACT
  detection, 2D, cross with BOSS velocity template.
- Method/application: Hotinli et al. 2025, arXiv:2506.21657 — 3D pipeline,
  surrogate fields, photo-z treatment, null tests.
- Application: Lai et al. 2025, arXiv:2506.21684 — 2D tomographic QML.
- Application: McCarthy et al. 2025, arXiv:2511.15701 — continuity
  velocities, T_L calibration, Knox covariance.
- Application: Chaussidon et al. 2026, arXiv:2604.04867 — spectroscopic 3D,
  foreground monopole, P^vv, fit order.

## Not verified
<!-- key: not-verified -->

- The N^(3/2) expression (arXiv:2010.07193, Eq. 81): located, not copied.
- Scale independence of b_v^α at L < 200 in Cayuso et al. 2023: quoted from
  arXiv:2511.15701, footnote 9; not read at source.
- Howlett 2019 (optimal velocity weights), Tegmark et al. 1997
  (μ-weighting) and the MAP velocity estimator of arXiv:2506.21684,
  footnote 6: cited, not read.
- The RSD route to f/b_g without b_v (ref. [77] of arXiv:2010.07193): not
  identified.
- The 3D spectroscopic against photometric comparison (in preparation).
