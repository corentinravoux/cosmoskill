# Void–tracer cross-correlation: RSD and AP — cosmo-beyond-two-point dossier

Scope: how a void–galaxy (or void–forest) RSD and Alcock–Paczynski fit is
built step by step (where voids are found, centre and radius cut, estimator,
the model equation, where the real-space profile and dispersion come from,
how the AP scaling enters, likelihood and covariance), and how to choose
between reconstruction and redshift-space void finding, mock templates and
deprojection, the full model and the multipole-ratio estimator, mock and
jackknife covariances.
Snapshot: 2026-10-18.
From: Cai & Neyrinck 2025, Sect. 4 (redshift-space distortions around voids:
dynamical and geometric); Beyond-2pt challenge, Sect. V.7 (void–galaxy
cross-correlation); eBOSS DR16 void analyses (arXiv:2007.09013,
arXiv:2008.06060).

Already in L2, not repeated here: the two schools in one paragraph, the
founding papers and the reference SDSS analysis in outline
(`physics-and-methods.md#void-galaxy-cross-correlation-ap-and-rsd`); the
D_A H/c convention trap (same place); results and their history
(`results.md#void-galaxy-cross-correlation-ap-and-rsd`); the RSD selection
bias, the finder's AP response, the velocity-profile mismatch, mock
calibration and the systematic budgets (`systematics.md#cosmic-voids`);
the void–forest β and its meaning
(`physics-and-methods.md#voids-in-lyalpha-tomography-and-the-void-forest`).
Void finding as such is in `deep/void-finding-size-function.md`.

## How it is done
<!-- key: how-it-is-done -->

Notation. X is a void centre, x a galaxy position, r = x − X the real-space
separation and s its redshift-space image; r_∥, s_∥ are components along the
line of sight, r_⊥ = s_⊥ across it; μ_r = r_∥/r and μ_s = s_∥/s. ξ^r(r) is
the real-space void–galaxy correlation (the galaxy density profile of the
stacked void), ξ^s(s, μ) its redshift-space version, ξ̄(r) =
(3/r³)∫₀^r ξ(y) y² dy its volume average. δ(r) is the void *matter* density
profile and Δ(r) = (3/r³)∫₀^r δ(y) y² dy the mean matter contrast inside r.
v_r(r) is the mean radial galaxy velocity, σ_v∥(r) the line-of-sight velocity
dispersion, f the growth rate, b the linear bias, β = f/b, a the scale
factor, H the Hubble rate. R is the effective void radius. The notation of
arXiv:2205.06258 is followed unless stated; arXiv:2007.07895 writes the
same AP ratios q_∥, q_⊥ and ε = q_⊥/q_∥ (see Step 7).

### Step 1. Decide in which field voids are found
<!-- key: step-1-decide-in-which-field-voids-are-found -->

Two choices are in use, and the model of Step 5 is only exact for the first.

- **After RSD-removing reconstruction.** The redshift-space galaxy field is
  passed through Zeldovich reconstruction, solving
  ∇·Ψ + (f/b) ∇·[(Ψ·r̂) r̂] = −δ_g/b (arXiv:2205.06258, Eq. 3) on a 512³
  grid after Gaussian smoothing with R_s = 10 h⁻¹Mpc, and galaxies are
  shifted by −Ψ_RSD = f(Ψ·r̂)r̂ only [src: Sect. 3.1]. The result depends on
  β alone; voids are then found in this field. Stated reason: voids found in
  redshift space violate the two assumptions the model needs, a spherically
  symmetric stack and a radial, spherically symmetric outflow, because
  underdensities aligned with the line of sight look emptier and are
  preferentially selected [src: Sect. 3.1, 3.5]. Fiducial β used for the
  catalogues: 0.31 (MGS), 0.37 (BOSS), 0.35 (eBOSS); void numbers move by
  ±2% across the β grid [src: Sect. 3.2].
- **Directly in redshift space**, absorbing the selection effect in nuisance
  amplitudes (arXiv:2007.07895, Sect. 3.5) or ignoring it with the
  multipole-ratio estimator (arXiv:2007.09013, Sect. 4.1.2).

A third variant correlates voids found after reconstruction with the
*reconstructed* galaxies, so that the RSD signal is removed and only the AP
anisotropy remains (Degni et al. 2025, arXiv:2509.08884; Choices below).

### Step 2. Define centre and radius
<!-- key: step-2-define-centre-and-radius -->

- REVOLVER (ZOBOV-based) on the reconstructed field; centre = the centre of
  the largest empty sphere inscribed in the void (Nadathur & Hotchkiss 2015),
  chosen because the linear outflow model describes the mean flow around it
  better than around other centres [src: arXiv:2205.06258, Sect. 3.2].
- VIDE (ZOBOV-based) in redshift space; centre = volume-weighted barycentre,
  X = Σ x_i V_i / Σ V_i, and R = [(3/4π) Σ V_i]^{1/3}
  (arXiv:2007.07895, Eqs. 37–38). Stated reasons: the barycentre is
  constrained by the boundary, where the AP information is, and is robust to
  discreteness noise and to the motion of single tracers [src: Sect. 3.2].
- eBOSS DR16 tested barycentre against circumcentre (four lowest-density
  cells): about 4% change in β at the true cosmology, and a significant
  deviation when the fiducial Ω_m is wrong, so the barycentre was kept and
  no systematic assigned [src: arXiv:2007.09013, Sect. 4.5.6].

### Step 3. Select voids
<!-- key: step-3-select-voids -->

| Analysis | Cut | Stated reason | Place |
|---|---|---|---|
| SDSS six bins | keep voids above the median radius of each catalogue: R_cut = 40 (MGS), 47–49 h⁻¹Mpc (BOSS, eBOSS), about half of each sample kept | "following previous works"; the cut varies by ±3% with the mock or β | arXiv:2205.06258, Sect. 3.2, Table 1 |
| BOSS deprojection | R > N_s [(4π/3) n(z)]^{-1/3} with N_s = 4, giving R > 34.9 h⁻¹Mpc, 5952 voids before the cut | purity against Poisson voids; also removes voids misidentified through RSD | arXiv:2007.07895, Eq. 39, Sect. 3.2 |
| eBOSS DR16 | at least five galaxies; no edge flag; centre + R (or farthest member) inside the redshift limits | buffer particles create spurious voids near boundaries | arXiv:2007.09013, Sect. 3.2 |
| Reconstructed-space test | no cut | small voids carry most of the statistical power; cuts are "somewhat arbitrary" | arXiv:2509.08884, Sect. 3.4 |

### Step 4. Measure the cross-correlation
<!-- key: step-4-measure-the-cross-correlation -->

- Landy–Szalay with void randoms. 30 bins in s and 80 in μ up to
  s = 120 h⁻¹Mpc; galaxy randoms 50 times the data; *void* randoms drawn
  from the stacked void catalogues of 250 mocks, because voids avoid the
  survey edges and their n(z) differs from the galaxies'. Galaxies carry the
  survey systematic weights, voids unit weight; caps are summed after a
  check that they agree, a comparison the authors found useful to catch bugs
  in reconstruction or void finding [src: arXiv:2205.06258, Sect. 3.4,
  Eq. 5]. ξ^r is estimated with the reconstructed galaxies, ξ^s with the
  original redshift-space positions; both depend on β through the voids.
- Hamaus estimator, ξ^s = ⟨X, x⟩/(⟨X⟩⟨x⟩) − ⟨X, x_r⟩/(⟨X⟩⟨x_r⟩)
  (arXiv:2007.07895, Eq. 40), a limiting case of Landy–Szalay. Multipoles
  are obtained by weighting pairs with Legendre polynomials, without μ
  bins, which the authors prefer at small s and μ → 1 where binning is
  coarse. Separations are in units of each void's R ("stacking"), so that
  the compensation walls of voids of different size add at s = R; without
  this the wall at s = R is smeared out, which hurts the AP test
  [src: Sect. 3.3, 4.3.3].

### Step 5. Write the model
<!-- key: step-5-write-the-model -->

The general relation, exact if void–galaxy pairs are conserved
(arXiv:2205.06258, Eq. 11, the model of Nadathur & Percival):

  1 + ξ^s(s, μ_s) = ∫ [1 + ξ^r(r)] [1 + v_r/(raH) + (r v_r′ − v_r)/(raH) μ_r²]^{-1} P(ṽ, r) dṽ,

with s_∥ = r_∥ + v_∥/(aH) (Eq. 7), ṽ = v_∥ − v_r μ_r the incoherent
velocity, and P(ṽ, r) a zero-mean Gaussian of width σ_v∥(r) (Eq. 12). The
outflow is the linear-continuity form v_r(r) = −(1/3) f a H r Δ(r) (Eq. 13),
with Δ the *non-linear* enclosed contrast [src: Sect. 3.5, footnote 5].
Pair conservation holds by construction when the same voids serve for ξ^r
and ξ^s; spherical symmetry needs a void selection without orientation
bias, hence Step 1 [src: Sect. 3.5]. Eq. 11 gives results very close to
the Gaussian streaming model once a bug in an earlier GSM implementation was
fixed [src: footnote 4]. It is evaluated directly, without expansion in Δ.

Linear versions. Dropping second order in δ and Δ but keeping the products
ξ^r δ and ξ^r Δ (not small inside a void, where ξ^r ≈ −1):

  ξ^s(s, μ) = ξ^r(r) + (f/3) Δ(r)[1 + ξ^r(r)] + f μ² [δ(r) − Δ(r)][1 + ξ^r(r)],
  r = s [1 + (f/3) Δ(s) μ²]   (arXiv:1712.07575, Eqs. 14–15).

The Jacobian terms squash the void along the line of sight and dominate near
the walls; the coordinate shift stretches it where ξ^r is steepest; together
they make the quadrupole change sign inside the void [src: Sect. 3.1]. With
a velocity dispersion the model becomes the convolution of Eq. 25 of the
same paper, still linear in all senses [src: Sect. 3.4].

With the linear-bias substitution ξ^r = bδ inside voids, f → β and
Δ → ξ̄^r (arXiv:1712.07575, Eqs. 17–18; arXiv:2007.07895, Eqs. 31–32). At
linear order only ℓ = 0, 2 survive:

  ξ^s_0 = (1 + β/3) ξ(r),  ξ^s_2 = (2β/3)[ξ(r) − ξ̄(r)]   (arXiv:2007.07895, Eqs. 34–35),

which gives the profile-free relation ξ^s_0 − ξ̄^s_0 = ξ^s_2 (3 + β)/(2β)
(Eq. 36), valid only at ε = 1. The eBOSS DR16 analysis fits exactly this,
minimising ε(β) = ξ_2 − (ξ_0 − ξ̄_0) 2β/(3 + β) (arXiv:2007.09013, Eq. 24);
its stated advantage is that it needs almost no knowledge of the real-space
profile or of the velocity distribution [src: Sect. 4.1.2].

The BOSS deprojection model adds two nuisance amplitudes:

  ξ^s(s) = 𝓜 { ξ(r) + (1/3)(f/b) ξ̄(r) + (f/b) 𝓠 μ_r² [ξ(r) − ξ̄(r)] }   (arXiv:2007.07895, Eq. 44),

with r_∥ = s_∥/[1 − (1/3)(f/b) 𝓜 ξ̄(r)], solved by iteration from
Δ(s) (5 iterations suffice) [src: Eq. 26, Sect. 2.3, 3.5]. 𝓜 absorbs
deprojection inaccuracy and Poisson-void dilution of the monopole, 𝓠
selection effects of redshift-space voids such as fingers of God at void
walls; priors uniform in [−10, 10] [src: Sect. 3.5]. A later form with
modified coefficients, ξ^s = 𝓜{ξ + βξ̄ + 2𝓠βμ²[ξ − ξ̄]}, is attributed to
Hamaus et al. 2022 in arXiv:2509.08884 (Eq. 17); the Hamaus 2022 paper was
not read.

Lyα forest. With δ_F = b_δ δ + b_η η_∥ + δ_N, η_∥ the line-of-sight velocity
gradient, and the same linear outflow,
ξ(r, μ) = b_δ δ_v + b_η f [δ̄_v/3 + (δ_v − δ̄_v) μ²] (arXiv:2203.11045,
App. A, Eq. 10), hence ξ_2 = [2β/(3 + β)](ξ_0 − ξ̄_0) with β = b_η f/b_δ
(Eq. 11), formally the galaxy relation with a different β.

### Step 6. Supply the real-space ingredients
<!-- key: step-6-supply-the-real-space-ingredients -->

Eq. 11 maps ξ^r to ξ^s; ξ^r, Δ and σ_v∥ must come from somewhere.

| Ingredient | Reconstruction school (arXiv:2205.06258) | Deprojection school (arXiv:2007.07895) |
|---|---|---|
| ξ^r(r) | mean ⟨ξ̂^r⟩ of 250 MGS or Patchy mocks after reconstruction. Reason: ξ̂^r from the data is noisier and correlated with the measured ξ^s; ignoring that correlation gave an artificially low χ² and biased parameters [src: arXiv:2205.06258, Sect. 3.5] | inverse Abel transform of the projected ξ^s_p(s_⊥) of the data, ξ(r) = −(1/π)∫_r^∞ (dξ^s_p/ds_⊥) ds_⊥/√(s_⊥² − r²) (Eq. 27), projection to s_∥ = ±3R [src: Sect. 3.6]. Reason: no assumption on cosmology or structure formation [src: abstract]. Model uncertainty from the measured ξ_p is neglected in the covariance [src: Sect. 3.7] |
| Δ(r) | template from BigMD galaxy voids and dark matter at z_ref = 0.1, 0.32 or 0.52, scaled as Δ(r; z) = [σ8(z)/σ8^BigMD(z_ref)] Δ^fid(r; z_ref) (Eq. 15), a scaling verified on simulations with other σ8. Reason: the linear-bias prescription "is often a poor approximation" and biased earlier fits [src: arXiv:2205.06258, Sect. 3.5] | linear bias, ξ = bδ (Eq. 29), justified by simulations and lensing for large voids [src: Sect. 2.3] |
| σ_v∥(r) | BigMD template shape, free asymptotic amplitude σ_v [src: Sect. 3.5] | none: the linear model has no dispersion |
| Free parameters | fσ8, β (through reconstruction), α_⊥/α_∥, σ_v [src: Sect. 3.6] | f/b, ε, 𝓜, 𝓠 [src: Sect. 3.6] |

Why the linear bias fails inside voids: on mocks, ξ^r/b differs from the true
δ by about 25% within the void radius, in a scale-dependent way, because
void finding selects regions where the stochastic term of δ_g = bδ + ε is
negative; ξ^r/b then overestimates the void depth and the wall height, even
for b = 1. The effect is smaller if ξ^r is measured with a denser tracer than
the one used to find voids [src: arXiv:1712.07575, Sect. 3.2].

An alternative fitting form for δ(r) is the HSW profile,
δ(r) = δ_c [1 − (r/r_s)^α]/[1 + (r/R)^β] (arXiv:2007.07895, Eq. 28; there β
is a slope, not f/b), with δ_c, r_s, α, β free; Patchy voids are matched by
(r_s/R, δ_c, α, β) ≈ (0.82, −0.36, 1.6, 9.1) with b = 2.2 [src: Sect. 3.6].

### Step 7. Put in the AP scaling
<!-- key: step-7-put-in-the-ap-scaling -->

α_⊥ = D_M/D_M^fid, α_∥ = D_H/D_H^fid (arXiv:2205.06258, Eq. 16) and
ξ^s(s_⊥, s_∥) = ξ^{s,fid}(α_⊥ s_⊥^fid, α_∥ s_∥^fid) (Eq. 17). The input
functions ξ̂^r, Δ and σ_v∥ are rescaled so that the apparent void size
changes as r → α_⊥^{2/3} α_∥^{1/3} r; the absolute void size is therefore
not a ruler and only α_⊥/α_∥ is constrained [src: Sect. 3.5]. In the
deprojection notation, R = q_∥^{1/3} q_⊥^{2/3} R′, so that s/R and μ_s depend
only on ε = q_⊥/q_∥ (arXiv:2007.07895, Eqs. 13–16), with q_∥ the ratio of
true to fiducial H⁻¹ and q_⊥ of D_A (comoving) [src: Sect. 2.2].

### Step 8. Likelihood and covariance
<!-- key: step-8-likelihood-and-covariance -->

- Reconstruction school: data vector (ξ^s_0, ξ^s_2), n_d = 60 points
  (30 radial bins per multipole); the hexadecapole is left out because it
  adds little at current precision [src: arXiv:2205.06258, Sect. 3.6].
  Covariance from 1000 mocks, held fixed with cosmology, with the
  Percival et al. 2021 posterior [1 + χ²/(n_s − 1)]^{−m/2},
  m = n_θ + 2 + [n_s − 1 + B(n_d − n_θ)]/[1 + B(n_d − n_θ)],
  B = (n_s − n_d − 2)/[(n_s − n_d − 1)(n_s − n_d − 4)], n_θ = 4
  (Eqs. 18–22). β enters the data vector, so measurements are precomputed
  on a fine β grid; the likelihood is evaluated at the two bracketing grid
  points and interpolated linearly. Interpolating the correlation functions
  instead averaged noise and lowered χ² between grid points [src: Sect. 3.6].
- Deprojection school: covariance by delete-one-void jackknife over the
  N_v voids, scaled by (N_v − 1); reason: voids are mutually exclusive
  patches, the method uses the data only and needs no model assumption, and
  it agrees with mock covariances for large N_v [src: arXiv:2007.07895,
  Sect. 3.3]. Data vector ξ^s(s_∥, s_⊥) in 18² bins (multipoles ℓ = 0, 2, 4
  give consistent results); Gaussian likelihood sampled with emcee
  [src: Sect. 3.4, 3.6].
- eBOSS DR16: residual ε(β) of Step 5, about 20 bins per sample, 1000
  EZmocks, Hartlap factor (below 2% on the errors), MINUIT [src:
  arXiv:2007.09013, Sect. 4.2].

### Step 9. Validate
<!-- key: step-9-validate -->

Model on N-body mocks (Nseries, OuterRim), fiducial-cosmology reruns, and the
systematic terms of `systematics.md#response-of-the-void-finder-to-the-fiducial`.
For the deprojection model on 30 Patchy mocks: χ²_red = 1.86 at the power
of 30 surveys, f/b and ε recovered within 68%, 𝓜 above unity by about 14%
(attributed to over-dispersion in Patchy), strong 𝓜–f/b anticorrelation
broken by the monopole [src: arXiv:2007.07895, Sect. 3.6].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Reconstruction before finding, or voids in redshift space
<!-- key: reconstruction-before-finding-or-voids-in -->

Reconstruction makes the model assumptions true by construction but costs a
reconstruction per β and a dependence on reconstruction efficiency (L2). The
deprojection school keeps redshift-space voids and pays two nuisance
parameters; its calibration-free errors are four times those of its
mock-calibrated variant (L2). A finder-level study with a spherical finder
shows why the redshift-space route needs care: the one-to-one map between
real- and redshift-space voids is affected by a tracer-RSD expansion of
radii, an AP volume change, an off-centring of void centres along the line
of sight from void motions (X̃ = X + V(1 + z)/H, arXiv:2107.01314, Eq. 9),
and an ellipticity selection; the expansion and AP corrections of radii are
the most important model change, and the Gaussian streaming model stays
robust once all effects are included [src: Sect. 6]. The same paper calls
reconstruction "computationally expensive, quite redundant" and wasteful of
the information in redshift-space void systematics [src: Sect. 6].

### Reconstructed voids with reconstructed galaxies (AP only)
<!-- key: reconstructed-voids-with-reconstructed-galaxies -->

On 100 Quijote halo boxes (1 h⁻¹Gpc, z = 0.5, FoF halos above
10¹³ h⁻¹M_⊙, n ≈ 4 × 10⁻⁴ h³Mpc⁻³, β = 0.41), VIDE voids in reconstructed
space give ε = 0.995 ± 0.011 against 1.005 ± 0.015 in redshift space, an
improvement factor I = 1.3 at the error of one box; model Eq. 17 of that
paper with 𝓠 fixed to 1 in reconstructed space; χ²_ν = 1.15 against 1.31
[src: arXiv:2509.08884, Sect. 3.1, 4.2, 5.1]. The gain holds as small voids
are removed (I ≈ 1.25–1.35) and no bias in ε appears in the joint fit, but in
a few single boxes ε deviates when all voids are kept, which disappears
above 3 mean tracer separations (13 h⁻¹Mpc there) [src: Sect. 5.2].
Covariance: delete-one jackknife per box, checked against the mock-to-mock
covariance [src: Sect. 4.3]. This gives AP only; growth is lost with the RSD.

### Mock templates or data-driven profile
<!-- key: mock-templates-or-data-driven-profile -->

Mock templates (Step 6) inject the mocks' cosmology and galaxy model into
Δ and σ_v, scaled only by σ8; the deprojected profile carries the data's
noise and is not propagated in the covariance; linear bias is quick but
wrong by about 25% inside the void radius (Step 6). The quantified cost of
the linear-bias, multipole-ratio route on N-body mocks: β biased by
0.037 ± 0.007 (Nseries LRG, fiducial 0.41), 0.057 ± 0.005 (OuterRim ELG,
0.686) and 0.160 ± 0.004 (OuterRim QSO, 0.401), about 9%, 8% and 40%,
which eBOSS adopted as systematics [src: arXiv:2007.09013, Sect. 4.5.4,
Table 5]. The reconstruction school's use of BigMD templates explicitly
avoids this prescription [src: arXiv:2205.06258, Sect. 3.5].

### Mock covariance or void jackknife
<!-- key: mock-covariance-or-void-jackknife -->

Mock covariances need a mock pipeline repeated per β (1000 mocks); jackknife
over voids is free and data-based but assumes voids are independent, valid
for separations up to the void extent rather than inter-void scales
[src: arXiv:2007.07895, Sect. 3.3]. Both schools report agreement with
the other method on mocks (same place; arXiv:2509.08884, App. A.2).

### Full model or ratio estimator
<!-- key: full-model-or-ratio-estimator -->

The full Eq. 11 needs ξ^r, Δ and σ_v and gives fσ8 directly through the σ8
scaling of Δ; the ratio estimator needs nothing but returns β, turned into
fσ8 with an external bias (`systematics.md#bias-conversion`).

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Reconstruction grid, smoothing | 512³, R_s = 10 h⁻¹Mpc | SDSS six bins | arXiv:2205.06258 | Sect. 3.1 |
| Void numbers before / after median cut | 517/258, 1009/504, 1596/798, 2526/1263, 3830/1915, 4706/2341 | MGS, LOWZ ×2, CMASS ×2, eBOSS | arXiv:2205.06258 | Table 1 |
| Fitted range, bins | s ≤ 120 h⁻¹Mpc; 30 s × 80 μ bins; n_d = 60 | SDSS six bins | arXiv:2205.06258 | Sect. 3.3, 3.4, 3.6 |
| Randoms | 50 × data, void randoms from 250 mocks | SDSS six bins | arXiv:2205.06258 | Sect. 3.4 |
| Purity cut | N_s = 4, R > 34.9 h⁻¹Mpc | BOSS deprojection | arXiv:2007.07895 | Eq. 39 |
| Bins | 18² (2D), 25 radial × 3 multipoles; innermost bin dropped | BOSS deprojection | arXiv:2007.07895 | Sect. 3.6 |
| Nuisance priors | f/b, ε, 𝓜, 𝓠 uniform in [−10, 10] | BOSS deprojection | arXiv:2007.07895 | Sect. 3.5 |
| Linear bias of the sample | b = 1.85 (data), 2.20 (Patchy) | BOSS combined | arXiv:2007.07895 | Sect. 3.1 |
| Linear-bias error inside voids | about 25% within R | MD mocks | arXiv:1712.07575 | Sect. 3.2 |
| Ratio-estimator bias on N-body | 9%, 8%, 40% (LRG, ELG, QSO) | eBOSS DR16 | arXiv:2007.09013 | Table 5 |
| Centre definition | 4% on β (barycentre vs circumcentre) | eBOSS DR16 | arXiv:2007.09013 | Sect. 4.5.6 |
| AP gain from reconstructed space | σ(ε) 0.015 → 0.011, I = 1.3 | Quijote halos | arXiv:2509.08884 | Sect. 5.1 |
| Priors (reconstructed-space test) | ε ∈ [0, 2], β ∈ [−1, 1], 𝓜, 𝓠 ∈ [−10, 10] | Quijote halos | arXiv:2509.08884 | Sect. 4.2 |
| Lyα void position resolution | σ_∥ = 3.9, σ_⊥ = 5.1 h⁻¹Mpc; stack axis ratio 1.33 | eBOSS Stripe 82 mocks | arXiv:2203.11045 | App. B.1 |
| Lyα void centre offset towards sightlines | D ≈ 2.5 h⁻¹Mpc | same | arXiv:2203.11045 | App. B.2 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Voids found in redshift space with a model that assumes real-space
  voids.** Shows as an extra quadrupole inside the void radius. Test: rerun
  on mocks with voids found in real space or after reconstruction
  (arXiv:1712.07575, Sect. 3.1; arXiv:2205.06258, Sect. 3.5).
- **Linear bias inside voids.** Biases β, most for sparse or high-bias
  tracers (40% for eBOSS quasars). Test: N-body mocks with the true f/b,
  as in arXiv:2007.09013, Table 5.
- **Spurious (Poisson) voids** have a null quadrupole and a weaker monopole,
  so they dilute both (arXiv:2509.08884, Sect. 2.4, citing earlier work);
  𝓜 is meant to absorb this. Test: vary the radius cut and watch ε and β.
- **Real-space profile measured on the data and treated as exact.** Gives
  χ² too low and biased parameters unless the correlation with ξ^s enters
  the covariance [src: arXiv:2205.06258, Sect. 3.5].
- **Interpolating correlation functions across the β grid** smooths noise
  and creates artificial χ² minima between grid points; interpolate the
  likelihood instead [src: arXiv:2205.06258, Sect. 3.6].
- **Void centre motion and ellipticity**: off-centring and ellipticity-RSD
  distort ξ even with corrected radii [src: arXiv:2107.01314, Sect. 6].
- **Disagreement between galactic caps** in ξ^s flags bugs in
  reconstruction or finding [src: arXiv:2205.06258, footnote 3].
- **Lyα tomography voids.** The map resolution is anisotropic and void
  centres are pulled towards the nearest sightline. In a toy model with
  input β = 1 these raise the ratio estimate to 1.25 and 1.11; subtracting
  the quadrupole of shuffled sightline data, which keeps both effects,
  brings both back to 1.03 [src: arXiv:2203.11045, App. B.1, B.2]. The
  shuffling correction is therefore part of the estimator, not an option.
- **Finder response to the fiducial cosmology** pulls ε towards 1; see
  `systematics.md#response-of-the-void-finder-to-the-fiducial`.

## Reading list
<!-- key: reading-list -->

- Review: Cai & Neyrinck 2025, arXiv:2503.22532 — Sect. 4: linear and
  streaming models, the two ways of recovering the real-space profile.
- Foundation: Nadathur & Percival 2017, arXiv:1712.07575 — derivation of the
  model, why ξδ terms stay, why linear bias fails inside voids, dispersion.
- Method and application: Woodfinden et al. 2022, arXiv:2205.06258 —
  complete reconstruction pipeline: void randoms, BigMD templates, AP
  rescaling, β grid, Percival likelihood.
- Method and application: Hamaus et al. 2020, arXiv:2007.07895 — deprojection,
  𝓜 and 𝓠, jackknife covariance, calibrated against free results.
- Application: Aubert et al. 2022, arXiv:2007.09013 — multipole-ratio
  estimator on three eBOSS tracers and its N-body bias.
- Method: Degni et al. 2025, arXiv:2509.08884 — AP from voids and galaxies
  both in reconstructed space; keeps small voids.
- Critique: Correa et al. 2022, arXiv:2107.01314 — expansion, AP volume,
  off-centring and ellipticity effects of redshift-space voids.
- Application: Ravoux et al. 2022, arXiv:2203.11045 — void–forest model and
  the tomographic corrections (appendices).

## Not verified
<!-- key: not-verified -->

- The main text of arXiv:2203.11045 (the "tomographic effect" fit, scale
  range, mocks): only the appendices have an HTML rendering; numbers above
  come from the appendices.
- Hamaus et al. 2022 (Euclid void–galaxy forecast with the modified
  coefficients of the 𝓜–𝓠 model), Nadathur & Hotchkiss 2015 (empty-sphere
  centre), Paillas et al. 2021 corrections to the outflow model, Schuster
  et al. 2023 on the validity of linear continuity: cited through the papers
  read, not read, no identifiers recorded.
- How arXiv:2008.06060 and arXiv:1904.01030 calibrate σ_v and the
  void-centre velocity: L2 summarises; bodies not re-read here.
- No DESI void–galaxy RSD or AP analysis was found in two date-sorted
  searches from 2025-06-01 (one returned arXiv:2509.08884, the other a
  modified-gravity model paper, not read).
