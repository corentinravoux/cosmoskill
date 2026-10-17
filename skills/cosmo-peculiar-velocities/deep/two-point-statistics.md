# Velocity and momentum two-point statistics — cosmo-peculiar-velocities dossier

Scope: how density–momentum power spectra and ψ1, ψ2 correlation functions are measured and
modelled in current analyses — field definitions, optimal weights, shot noise, window and
geometry factors, the one-loop model and its velocity-dispersion nuisances — and how to choose
between weights, templates, parameter sets and likelihoods.
Snapshot: 2026-10-17.
From: Turner 2024 review (arXiv:2411.19484), Sect. 5.2; DESI DR1 PV correlation-function and
power-spectrum papers (arXiv:2512.03230, arXiv:2512.03231).

Already in L2, not repeated here: the momentum estimator F^p, its shot noise and linear limit,
the η → v conversion and the DESI DR1 data vector, k ranges and the k^p ≤ 0.1 cut in
`physics-and-methods.md#momentum-power-spectrum`; the ψ estimators in η, the α_vv rescaling, the
24–120 h⁻¹Mpc fit range and its reason in
`physics-and-methods.md#velocity-and-momentum-correlation-functions`; priors, likelihoods,
mock validation and the FP group systematic in
`systematics.md#desi-dr1-density-and-momentum-power-spectra-qin` and
`systematics.md#desi-dr1-galaxy-and-momentum-correlation`; SDSS PV power-spectrum likelihood
(Box–Cox, Sellentin–Heavens) in `systematics.md#sdss-pv-growth-rate-field-level-lai-et-al-2023`;
wide-angle effects in `systematics.md#wide-angle-and-geometry`.

Notation: p = (1 + δ)v is the line-of-sight momentum; P^δ, P^p, P^δp the density, momentum
and cross spectra and P_ℓ their multipoles; ⟨v²⟩ the per-object velocity variance (errors plus
non-linear scatter); P_FKP the characteristic amplitude in an FKP-type weight; ψ1, ψ2 the
radial velocity correlations of Gorski; A(r), B(r) the survey-geometry factors that mix Ψ∥ and
Ψ⊥; σ_vT, σ_vS two velocity-dispersion nuisances of the one-loop model. Symbols follow Qin et al.
2025 (arXiv:2512.03231) for spectra and Turner et al. 2025 (arXiv:2512.03230) for correlation
functions.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Choose momentum rather than velocity
<!-- key: step-1-choose-momentum-rather-than-velocity -->

DESI DR1 measures the momentum spectrum because "our measurements are limited to locations where
galaxies (and thus mass) are present": an empty region records zero velocity "due to the
absence of tracers", not because v = 0 [src: arXiv:2512.03231, Sect. 3.1]. The alternatives are
rejected with reasons: a reconstructed velocity field "is inherently dependent on cosmological
assumptions"; a Voronoi tessellation "introduces complications in the Fourier space" [src:
same]. The (1 + δ) factor brings non-linear terms that the model must carry (Step 4). Tonegawa
et al. make the same point for ψ: the observable is density-weighted, so a density–velocity term
contributes at order δ_L⁴, with sign opposite to the linear term, "which has often been
neglected" [src: arXiv:2309.14457, abstract].

### Step 2. Build the fields and their weights
<!-- key: step-2-build-the-fields-and-their-weights -->

Density and momentum fields from Qin et al. 2025 [src: arXiv:2512.03231, Sects. 3.1, 3.3]:

    F^δ(r) = w_δ(r)[n_δ(r) − α n_s(r)]/A_δ,   A_δ² = ∫ w_δ² n̄_δ² d³r     (Eqs. 6–7)
    F^p(r) = w_p(r) n_p(r) v(r)/A_p,           A_p² = ∫ w_p² n̄_p² d³r     (Eqs. 8–9)
    w_δ = 1/[1 + n̄_δ P^δ_FKP]                                             (Eq. 25)
    w_p = 1/[⟨v²(r)⟩ + n̄_p P^p_FKP]                                       (Eq. 26)

No random catalogue is subtracted from F^p because the mean velocity is zero, so subtracting it
"would be equivalent to subtracting zero" [src: Sect. 3.1]. The momentum weight is the
variance-minimising weight of Howlett 2019 in the Gaussian, distant-observer limit (arXiv:1906.02875,
Eqs. 40–41), checked by a full functional derivation [src: Sect. 5]; it is "not necessarily the
optimum choice" with non-Gaussian contributions or for parameter constraints, and P_FKP values
are instead chosen by maximising the Fisher information on fσ8 [src: same]. ⟨v²⟩ is
(ln10 c z σ_η/(1 + z))² + 300² km² s⁻² per object, and the value of the non-linear term has
"minimal impact" (arXiv:2512.03231, Eq. 59, App. A) [src].

Configuration-space weights (Turner et al. 2025) [src: arXiv:2512.03230, Sect. 3.2.2]:

    W_g,i = κ_i/(1 + n_i P_gg),                P_gg = 10⁴ h⁻³Mpc³          (Eq. 21)
    W_η,i = 1/(σ²_η,i/α_i + α_i n_i P_v),       P_v = 10¹⁰ h⁻³Mpc³ km² s⁻²   (Eq. 22)

with κ_i the completeness weight and α_i the velocity-to-η conversion factor (their Eq. 20),
W_η taken from Turner et al. 2023.

| Constant | Power spectra (Qin 2025) | Correlation functions (Turner 2025) | Place read |
|---|---|---|---|
| density P_FKP | 1 600 h⁻³Mpc³ | 10⁴ h⁻³Mpc³ | arXiv:2512.03231 Sect. 3.3; arXiv:2512.03230 Eq. 21 |
| momentum P_FKP | 5 × 10⁹ h⁻³Mpc³ km² s⁻² | 10¹⁰ h⁻³Mpc³ km² s⁻² | same; Eq. 22 |

The two DESI DR1 companion analyses therefore weight the same galaxies differently: a concrete
case of the "different analysis choices" to which the mock paper attributes the low
cross-estimator correlations (`results.md#desi-dr1-peculiar-velocity-survey-arxiv-2025-12`).

### Step 3. Estimate multipoles or pair correlations
<!-- key: step-3-estimate-multipoles-or-pair-correlations -->

**Power spectra** [src: arXiv:2512.03231, Sects. 3.2, 3.4]. Yamamoto-type estimators
P_ℓ = |F F*_ℓ| − 𝒩_ℓ (Eqs. 13–14), with 𝒩^p_ℓ containing ⟨v²⟩ (Eq. 16). The cross spectrum is
imaginary: P^δp_ℓ = ½ Im{|F^p F^δ*_ℓ| − |F^δ F^p*_ℓ|} − 𝒩^δp_ℓ (Eq. 17), because invariance
under δ → −δ, v → −v gives P^δp_ℓ = −P^δp*_ℓ (App. B); its shot noise uses min{n̄_δ, n̄_p} and
⟨v⟩ and arises only from galaxies common to both samples (Eq. 18). Shot noise is ignored for
ℓ > 0 [src]. Galaxies go on a 2 h⁻¹Mpc grid in an 800 h⁻¹Mpc box, each Fourier mode is divided by
the cell sinc (Eq. 27), and modes are limited by K_Ny = min(π/L_i) (Eq. 28) [src].

**Correlation functions** [src: arXiv:2512.03230, Sects. 3.1.1, 3.2.3, 3.2.5]. ψ̂1, ψ̂2 are
weighted DD pair sums of η_a η_b with cos θ_ab and cos θ_a cos θ_b (Eqs. 23–24); the cross
correlation subtracts a random–data term, which "acts to reduce the variance … by accounting
for edge effects", analogous to Landy–Szalay (Eq. 32), and is rescaled to velocity units by
α_gv (Eq. 33) [src]. The model is built with the sample's own geometry:

    ψ1(r) = A(r) Ψ∥(r) + [1 − A(r)] Ψ⊥(r),  ψ2(r) = B(r) Ψ∥ + [1 − B(r)] Ψ⊥    (Eqs. 6–7)
    A(r) = Σ W_a W_b cos θ_ab cos θ_a cos θ_b / Σ W_a W_b cos² θ_ab           (Eq. 12)
    B(r) = Σ W_a W_b cos² θ_a cos² θ_b / Σ W_a W_b cos θ_a cos θ_b cos θ_ab   (Eq. 13)

summed over data pairs in each separation bin with the same weights as the estimator [src]. ψ1
and ψ2 "contain all of the information within the 3D velocity tensor" for an irrotational field
[src: Sect. 3.1.1]. For simulation boxes A and B are "very close to 1/3 and 3/5 irrespective of
scales" (arXiv:2309.14457, Sect. 4) [src]; a survey's values depart from these, which is why the
geometry must be recomputed for each sample.

### Step 4. Model: one-loop spectra with shared nuisances
<!-- key: step-4-model-one-loop-spectra-with-shared -->

DESI DR1 uses the redshift-space one-loop models of Vlah et al. and Okumura et al. [src:
arXiv:2512.03231, Sect. 4.1]:

    P^δ(k,μ)  = P00 + μ²(2P01 + P02 + P11) + μ⁴(P03 + P04 + P12 + P13 + ¼P22)   (Eq. 29)
    P^p(k,μ)  = (aH)²/k² [P11 + μ²(2P12 + 3P13 + P22)]                        (Eq. 30)
    P^δp(k,μ) = (aH/k) μ [P01 + P02 + P11
                + μ²(3/2 P03 + 2P04 + 3/2 P12 + 2P13 + ½P22)]                   (Eq. 31)

Eq. 31 corrects "minor inaccuracies" of the Okumura et al. cross-spectrum expression, following
Chen et al. 2025, and therefore also of the SDSS PV analysis [src]. The P_mn terms are
generalised to density and momentum samples from different surveys, with separate biases for
each (Eqs. 35–43), giving 13 parameters in all [src: Sects. 4.2, 5.1]. The only stated
assumption of Eqs. 29–31 is the local plane-parallel approximation; they "do not presuppose the
ΛCDM paradigm" beyond E(z), D(a) and P_L [src: Sect. 4.1].

**What σ_vT and σ_vS are.** Howlett 2019 found that a single free σ_v "leads to significant biases
in the recovered values of fσ8", and replaced it, following Vlah et al. (2012), by two: σ_v,1 in
P02, P12, P22, P04 and the vector part of P13, and σ_v,2 in P03 and the scalar part of P13
(arXiv:1906.02875, App. A.1) [src]. Qin 2025 calls them σ_vT and σ_vS with exactly these
assignments (Table 1) [src: arXiv:2512.03231, Sect. 4.2]. Both are dispersions entering as
k²σ² damping-like terms inside the loop expansion, not the σ_u of field-level fits.

**Parameter reduction.** Mock tests reduce 13 parameters to five, fσ8, b1σ8, b2σ8, σ_vT, σ_vS,
shared between density and momentum, because "these models don't [respond] equally to every
parameter" (App. E) [src: arXiv:2512.03231, Sect. 5.1]. b_s and b_3nl can be fixed by the local
Lagrangian relations b_s = −(4/7)(b1 − 1), b_3nl = (32/315)(b1 − 1) (Eq. 46) [src]. In Howlett
2019 the linear power spectrum is fixed to the mock cosmology (σ8 = 0.815), the combinations
b1σ8, b2σ8, fσ8 are fitted, and "the systematic effects of fixing σ8 can be absorbed into the
nuisance terms" [src: arXiv:1906.02875, App. A.1].

**From spectra to ψ.** Turner 2025 sets P_v(k) = 3 P^0_pp(k), the factor 3 being the monopole of
(aHfμ/k)² P_L (Eqs. 10–11), and uses the one-loop momentum monopole from the Qin et al. code as
the velocity spectrum; the cross dipole is ξ^1_gu = (1/2π²) ∫ dk k P^1_gp j1(kr) (Eq. 16); the
octopole is dropped as too weak [src: arXiv:2512.03230, Sects. 3.1.1, 3.1.3]. The transforms use
FFTLog in cosmoprimo with power-law extrapolation beyond k ≈ 0.4 h Mpc⁻¹ and an exp(−k²a²)
damping with a = 1 h⁻¹Mpc to suppress ringing, which "does not affect any of the parameter fits"
[src]. Qin 2025 notes that the momentum correlation equals the velocity correlation only on
linear scales, so the ψ model "can be converted from the model of momentum power spectrum
approximately" [src: arXiv:2512.03231, Sect. 4.1].

### Step 5. Convolve with the window
<!-- key: step-5-convolve-with-the-window -->

The model multipoles are mixed by a matrix W (P^c = W·P, Eq. 47) built from randoms (Eqs.
48–51); for the cross spectrum A² → A_p A_δ and the kernel is the average of the two mixed
density/momentum terms (Eqs. 52–53) [src: arXiv:2512.03231, Sect. 4.3]. Settings: randoms on a
140³ grid in a 700 h⁻¹Mpc box "to get a grid without empty voxels"; theory multipoles to
ℓ_max = 4, because off-diagonal blocks of W are non-zero and odd/even multipoles leak into each
other, with negligible change for other ℓ_max; theory on k′ ∈ [0, 0.4075] h Mpc⁻¹ in 300 bins,
wider than the measured k ∈ [0, 0.3] [src]. In configuration space the window enters through
A(r), B(r) and the RD term of Eq. 32 instead (Step 3).

### Step 6. Fit
<!-- key: step-6-fit -->

The likelihood, priors, scale ranges and mock validation are in L2. Two practices from the
method papers: Howlett 2019 subtracts the observer's bulk flow (Kaiser MLE) before measuring
P^p; this lowers the large-scale monopole and its variance at k < 0.05 h Mpc⁻¹, leaves fσ8
unchanged and "marginally" improves its error, with the integral-constraint correction applied
but no further correction for forcing ⟨v⟩ = 0 [src: arXiv:1906.02875, Sect. 6.2]. Without PV
errors the momentum multipoles are close to log-normal; with errors they become "much more
Gaussian", with residual skewness on large scales; no fσ8 bias was found for 6dFGSv, but the small
2MTF volume produced a non-Gaussianity that biased fσ8 [src: Sect. 6.3], the motivation for the
Box–Cox transform of the SDSS PV analysis [src: arXiv:2411.09571, Sect. V.1].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Linear template or perturbation theory
<!-- key: linear-template-or-perturbation-theory -->

On Quijote dark matter and HR4 galaxies, fitting ψ1 and ψ2 over [r_min, 90] h⁻¹Mpc [src:
arXiv:2309.14457, Sects. 4–5]:

| r_min [h⁻¹Mpc] | Linear template | PT to δ_L⁴ with density–velocity term | Fiducial |
|---|---|---|---|
| 21 (Quijote) | 0.398 | 0.447 | 0.446 |
| 33 (Quijote) | 0.418 | 0.445 | 0.446 |
| 21 (HR4 galaxies) | 0.361 +0.024/−0.030 | 0.376 +0.025/−0.031 | 0.381 |

Linear theory "overpredicts the velocity power spectrum, demanding that fσ8 is smaller to
compensate"; both non-linear and density–velocity terms are negative and each contributes 5–10 %
at r = 10–20 h⁻¹Mpc; linear theory is "approximately valid" for r_min ~ 50 h⁻¹Mpc; for a
(500 h⁻¹Mpc)³ survey the shift is ~10 % at r_min = 20, comparable to the forecast error [src].
The PT template needs bσ8 (fixed in that study at 0.834 and 1.111) because the density–velocity
term scales as fσ8 bσ8 [src: Sect. 4]. A gridded, volume-weighted analysis (Adams & Blake 2017b)
avoids the ⟨δv⟩ term at the cost of losing scales below the grid [src: Sect. 5]. DESI DR1 uses
one-loop spectra for both its two-point analyses (Step 4).

### Which multipoles
<!-- key: which-multipoles -->

DESI DR1 fits [P^δ_0, P^δ_2, P^p_0, P^δp_1]; other multipoles "are found to be close to zero and
exhibit high noise levels" [src: arXiv:2512.03231, Sect. 5.1]. Howlett 2019 measured P^p_0 and
P^p_2 robustly on its mocks and did not use higher ones, "completely noise-dominated" [src:
arXiv:1906.02875, Sect. 6.1]. In configuration space the cross octopole is dropped [src:
arXiv:2512.03230, Sect. 3.1.3].

### P_FKP and the effective depth
<!-- key: pfkp-and-the-effective-depth -->

Raising P^p_FKP shifts weight to distant objects (more volume, larger velocity errors); lowering
it favours nearby objects with small errors; the tested values were 2 × 10⁸, 10⁹ and 5 × 10⁹
km² s⁻² h⁻³Mpc³ and unweighted; the choice changes "the relative errors on different scales",
not the mean measurement [src: arXiv:1906.02875, Sect. 6.1, Figs. 7–9 text]. Velocity errors
raise the diagonal of the momentum covariance "by up to an order of magnitude" while keeping the
off-diagonal terms, so the correlation matrix becomes much more diagonal [src: Fig. 10 caption].

### Power spectra, correlation functions or reconstruction
<!-- key: power-spectra-correlation-functions-or -->

On 400 Gaussian realisations, the power-spectrum method with Fisher-forecast errors and the
reconstruction-and-scaling method with full covariance agree; the latter with noise-only errors
under-estimates the error (Blake & Turner 2024, arXiv:2408.05660, Sects. 4–5) [src]; see
`deep/velocity-density-comparison.md`. Between the DESI DR1 power spectra and correlation
functions, the mock correlation is 29 % (L2).

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Momentum shot-noise variance | ⟨v²⟩ = (ln10 c z σ_η/(1+z))² + 300² km² s⁻² | DESI DR1 P(k) | arXiv:2512.03231 | Eq. 59 |
| Density / momentum P_FKP | 1 600 h⁻³Mpc³ / 5 × 10⁹ h⁻³Mpc³ km² s⁻² | DESI DR1 P(k) | arXiv:2512.03231 | Sect. 3.3 |
| Density / momentum weight constants | 10⁴ h⁻³Mpc³ / 10¹⁰ h⁻³Mpc³ km² s⁻² | DESI DR1 ξ | arXiv:2512.03230 | Eqs. 21–22 |
| Fourier grid | 2 h⁻¹Mpc cells, 800 h⁻¹Mpc box | DESI DR1 P(k) | arXiv:2512.03231 | Sect. 3.4 |
| Window grid | 140³ in 700 h⁻¹Mpc; ℓ_max = 4; k′ ≤ 0.4075 in 300 bins | DESI DR1 P(k) | arXiv:2512.03231 | Sect. 4.3 |
| Model parameters | 13 in full; 5 fitted | DESI DR1 P(k), ξ | arXiv:2512.03231 | Sect. 5.1 |
| Lagrangian relations | b_s = −4/7 (b1 − 1), b_3nl = 32/315 (b1 − 1) | one-loop model | arXiv:2512.03231 | Eq. 46 |
| FFTLog regularisation | extrapolation beyond k ≈ 0.4; exp(−k²a²), a = 1 h⁻¹Mpc | DESI DR1 ξ | arXiv:2512.03230 | Sect. 3.1.1 |
| ψ bins | 6 h⁻¹Mpc over 0–150 h⁻¹Mpc | DESI DR1 ξ | arXiv:2512.03230 | Sect. 3.2.3 |
| A, B in a box | ≈ 1/3, 3/5 | Quijote, HR4 | arXiv:2309.14457 | Sect. 4 |
| Linear-template bias | ~10 % at r_min = 20 for (500 h⁻¹Mpc)³; valid at r_min ~ 50 | Quijote, HR4 | arXiv:2309.14457 | abstract; Sect. 5 |
| PV vs cosmic error at r_min = 21 | +0.020/−0.027 (PV), +0.013/−0.015 (cosmic), linear | HR4 | arXiv:2309.14457 | Sect. 4 |
| Bulk-flow removal | affects k < 0.05 h Mpc⁻¹; fσ8 unchanged | mocks | arXiv:1906.02875 | Sect. 6.2 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Linear template at small r_min.** fσ8 low by 5–10 % below ~50 h⁻¹Mpc [src: arXiv:2309.14457,
  Sect. 5]. Test: r_min scan against a PT template on mocks.
- **ψ model built with the wrong geometry.** A(r), B(r) must use the data weights and pairs
  (Eqs. 12–13 of arXiv:2512.03230); the box values 1/3, 3/5 do not apply to a survey. Test:
  recompute A, B with each weight change.
- **Labels of Ψ∥ and Ψ⊥.** As printed, the DESI DR1 correlation-function paper attaches
  [j0 − 2j1/(kr)] to Ψ⊥ and j1/(kr) to Ψ∥ (arXiv:2512.03230, Eqs. 8–9), the opposite of the
  assignment written in arXiv:2604.08314 and quoted in
  `physics-and-methods.md#velocity-and-momentum-correlation-functions`. Check the convention of
  the code against a linear-theory limit before mixing formulae from the two papers.
- **Cross-spectrum algebra.** The Okumura et al. expression carried "minor inaccuracies",
  inherited by the SDSS PV paper; use Eq. 31 of arXiv:2512.03231 [src: Sect. 4.1].
- **One σ_v for all terms.** Biases fσ8; use σ_vT and σ_vS [src: arXiv:1906.02875, App. A.1].
- **Window truncated at low ℓ.** Off-diagonal W blocks mix multipoles; include ℓ ≤ 4 even when
  fitting fewer [src: arXiv:2512.03231, Sect. 4.3].
- **Non-Gaussian momentum spectra in small volumes.** Biased fσ8 in 2MTF [src: arXiv:1906.02875,
  Sect. 6.3]. Test: skewness and kurtosis of mock P_ℓ per k bin against Gaussian draws (their
  Fig. 12 procedure); transform (Box–Cox) or use a t-likelihood.
- **Environment-correlated η.** The FP group trend enhances P^p above k ≈ 0.1 h Mpc⁻¹ (L2); test:
  k^p_max scan and split by group richness.
- **Plane-parallel model at low z.** Eqs. 29–31 assume the local plane-parallel approximation
  [src: arXiv:2512.03231, Sect. 4.1]; wide-angle sizes are in L2.

## Reading list
<!-- key: reading-list -->

- Foundation: Gorski 1988 (doi:10.1086/185255) and Gorski et al. 1989 (doi:10.1086/167771) — ψ1,
  ψ2 (not read here; see Not verified).
- Method: Howlett 2019, arXiv:1906.02875 — momentum estimator, optimal weight, σ_v,1/σ_v,2,
  bulk-flow removal, Gaussianity tests.
- Method: Qin et al. 2024, arXiv:2411.09571 — density–momentum cross spectrum on SDSS PV;
  Box–Cox likelihood.
- Application: Qin et al. 2025, arXiv:2512.03231 — corrected cross-spectrum model for distinct
  surveys, window matrix, parameter reduction.
- Application: Turner et al. 2025, arXiv:2512.03230 — weighted ψ1, ψ2 and cross estimators,
  A(r), B(r), P_v = 3P^0_pp.
- Critique: Tonegawa et al. 2024, arXiv:2309.14457 — linear template and density weighting bias
  fσ8 low.
- Critique: Blake & Turner 2024, arXiv:2408.05660 — equivalence of power-spectrum and complete
  reconstruction errors.

## Not verified
<!-- key: not-verified -->

- Gorski 1988, Gorski et al. 1989 and Turner et al. 2023 (arXiv:2207.03707, origin of W_η) were
  not read in the body.
- Appendix E of arXiv:2512.03231 (the tests that reduce 13 parameters to five) and Section 7 of
  arXiv:1906.02875 (Fisher-optimised P_FKP) were not read.
- Which of the two Ψ∥/Ψ⊥ labellings the released codes follow was not checked.
- Whether "modes that exceed the Nyquist frequency" in arXiv:2512.03231, Sect. 3.4, means the
  modes kept are below K_Ny (as Eq. 28 suggests) was not resolved; the sentence is as printed.
