# Halo profiles and concentration — cosmo-galaxy-halo-connection dossier

Scope: how a halo concentration is measured in a simulation (profile fit,
enclosed mass, peak finding, circular-velocity ratio; radial range,
weighting, centre, particle minimum, relaxation cut), how NFW and Einasto
concentrations and their c(M) relations differ, how a concentration given in
one mass definition is converted to another, and how c(M), its freedom and
off-centring enter the galaxy–galaxy lensing and satellite models of current
joint fits.
Snapshot: 2026-10-19.
From: Asgari et al. 2023, Sect. 3.5-3.6; Wechsler & Tinker 2018, Sect. 2.1.

Already in L2, not repeated here: NFW and Einasto as profiles, the c(M)
relations of Bullock, Duffy (with its Table 1 coefficients), Ludlow, Child,
Diemer & Joyce and the CAMELS baryonic relation, in
`physics-and-methods.md#density-profiles-and-concentration`; concentration
scatter in the halo model (σ_ln c ~ 0.3) in
`physics-and-methods.md#the-halo-model-and-its-limits`; the size of the
profile systematics and of baryonic changes to ΔΣ in
`systematics.md#profiles-concentration-and-their-scatter` and
`systematics.md#lensing-and-clustering-systematics-in-joint-fits`; the
f_conc bracket 0.61–0.84 of the BOSS lensing comparison in
`physics-and-methods.md#galaxy-galaxy-lensing-with-clustering`; the
satellite-profile tests of satellite kinematics in `deep/satellites.md`.
Which mass function, profile and Δ_v the matter halo model uses, and the
Bullock-versus-Duffy comparison for HMcode, are in
`cosmo-theory-foundations/deep/halo-model-nonlinear.md` (Step 5); the
concentration treatment of cluster lensing masses in `cosmo-clusters`.

Symbols. r_Δ, M_Δ: radius and mass inside which the mean density is Δ times
the critical (c) or mean (m) density; vir: the Bryan & Norman overdensity.
r_s: NFW scale radius; r_−2: radius where d ln ρ/d ln r = −2 (r_s for NFW).
c_Δ = r_Δ/r_s (or r_Δ/r_−2). α: Einasto shape parameter. ν = δ_c/σ(M, z):
peak height. x_off: offset between the most bound particle and the centre of
mass, in units of the halo radius. ρ_rms: r.m.s. of ln ρ about the NFW fit.
f_h, f_s: normalisations of c(M) for the matter and satellite profiles;
f_off, R_off: fraction and Gaussian width of off-centred centrals.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Choose the halo sample: resolution and dynamical state
<!-- key: step-1-choose-the-halo-sample-resolution-and -->

The particle minimum differs by a factor of twenty between groups:

| Analysis | Minimum | Stated reason | Place read |
|---|---|---|---|
| Duffy et al. 2008 | 10⁴ particles inside r_vir; Power et al. convergence radius inside 0.05 r_vir | well-resolved fits | arXiv:0804.2486, Sect. 2.1 |
| Dutton & Macciò 2014 | 500 particles (NFW); more for Einasto | c_max ≡ R_min/ε = 29.0 (N_min/1000)^(1/3) with softening ε = 0.025 L/N, so a few hundred particles resolve c ~ 10; Einasto α and c are degenerate in poorly resolved haloes | arXiv:1402.7073, Sect. 2.4 |
| Child et al. 2018 | 2000 particles | below 2000 particles the fit and enclosed-mass concentrations of the lower-resolution run diverge from the higher-resolution run at the same mass; peak finding needs about ten times more | arXiv:1804.10199, App. B.6 |
| Diemer & Joyce 2019 | 1000 particles inside R_200c, 200 inside r_s, r_s > 6 force lengths, imposed on average through a c(M) relation | imposing them halo by halo "would lead to a biased scale radii" | arXiv:1809.07326, Sect. II.2 |

Relaxation cuts also differ, and they change the answer:

- x_off < 0.07 alone (Duffy et al., most bound particle versus FoF centre of
  mass, with x in units of r_vir: 561 of 1269 haloes relaxed at z = 0 [src:
  arXiv:0804.2486, Sect. 2.1]; Child et al., in units of R_200c: ~80% of
  haloes with ≥ 2000 particles relaxed at z = 0, falling to 45% at higher z
  [src: arXiv:1804.10199, Sect. III.1]).
- x_off < 0.07 and ρ_rms < 0.5 (Dutton & Macciò, after Macciò et al.): ~80%
  relaxed at z = 0, ~50% at z = 5 [src: arXiv:1402.7073, Sect. 2.3].
- No cut (Diemer & Joyce): unrelaxed haloes cause the upturn of c(ν) at high
  peak height, but "aggressively cutting out unrelaxed halos necessarily
  leads to a bias toward dynamically older systems and thus higher
  concentrations" [src: arXiv:1809.07326, Sect. II.2].

Unrelaxed haloes have mass far from the potential minimum, so their fitted
r_s is large and their c(M) is lower and flatter [src: arXiv:1804.10199,
Sect. III.1]. Duffy et al. relaxed haloes have A ~18% higher than the full
sample [der: L2 entry on their Table 1].

### Step 2. Choose the centre
<!-- key: step-2-choose-the-centre -->

Every analysis read centres on the most bound particle (potential minimum)
[src: arXiv:0804.2486, Sect. 2.1; arXiv:1402.7073, Sect. 2.2;
arXiv:1804.10199, App. B.3]. Against the most-connected-particle or a
density-histogram centre, relaxed haloes (centres up to 60 h⁻¹kpc apart)
change concentration by < 5%; unrelaxed low-mass haloes (centres 160 h⁻¹kpc
apart on average) by up to 20% at 2000 particles, back below 5% at high mass
[src: arXiv:1804.10199, App. B.3].

### Step 3. Measure the profile and fit it
<!-- key: step-3-measure-the-profile-and-fit-it -->

| Analysis | Bins and radial range | Fit | Place read |
|---|---|---|---|
| Duffy et al. 2008 | log bins of 0.078 dex over −1.25 ≤ log(r/r_vir) ≤ 0 | NFW (r_s, δ_c) and Einasto with α fixed to the Gao et al. α(ν); minimise the difference of log densities with equal weights; radii and masses then taken from the best-fit profile | arXiv:0804.2486, Sect. 2.1 |
| Dutton & Macciò 2014 | 50 log shells from max(0.01 r_vir, 3 softenings) to 1.2 r_vir; Poisson errors | NFW (r_−2, ρ_−2) and Einasto (r_−2, ρ_−2, α), Levenberg–Marquardt χ² | arXiv:1402.7073, Sect. 2.2 |
| Child et al. 2018 | shells inside r_200c whose outer radius encloses ≥ 100 particles | NFW differential mass profile dM/dr (Eq. 4), M_Δ and r_Δ fixed by the SO finder, Levenberg–Marquardt weighted by Poisson errors (Eq. 5) | arXiv:1804.10199, Sect. III.1 |
| Rockstar (used by Diemer & Joyce) | bound particles inside R_vir, up to 50 equal-mass bins of ≥ 15 particles | NFW, equal weights except bins within three force lengths, down-weighted by 10 | arXiv:1809.07326, Sect. II.3 |

Why Child et al. stop at r_200c and need 100 particles per shell: shells
beyond r_200 have high counts and low Poisson errors and would dominate the
fit where NFW need not hold, and the inner limit (about a tenth of the
virial radius for clusters) removes regions with numerical errors and
missing baryonic effects [src: arXiv:1804.10199, Sect. III.1]. Why Duffy et
al. fix Einasto α: they confirm α(ν) of Gao et al. on stacks of ten haloes
and adopt it, leaving two free parameters [src: arXiv:0804.2486, Sect.
2.1]; Diemer & Joyce add that α must be fixed for individual haloes because
their profiles "often allow too much freedom" [src: arXiv:1809.07326,
Sect. II.3].

### Step 4. Cross-check with non-fitting estimators
<!-- key: step-4-cross-check-with-non-fitting-estimators -->

- **Enclosed mass.** M(r_s) = M_Δ/A(c_Δ) (ln 2 − ½) (Eq. 6), solved
  iteratively; sensitive to r < r_s [src: arXiv:1804.10199, Sect. III.1].
- **Peak finding.** r_s is the maximum of the Hanning-smoothed dM/dr (Eq. 7);
  makes no assumption on the profile form [src: same].
- **Circular-velocity ratio.** V_max/V_200 (the Klypin et al. and Prada et
  al. method, as cited).

When the three Child et al. estimators disagree the profile is not NFW; they
agree on well-resolved low-redshift haloes and differ by up to 10% at z = 3
[src: arXiv:1804.10199, Sect. III.1]. c_fit is positively skewed (it can be
arbitrarily high), c_acc is close to normal [src: same].

### Step 5. Fit the c(M) relation
<!-- key: step-5-fit-the-c-m-relation -->

Diemer & Joyce fit binned median concentrations by least squares and add a
2% systematic error per bin, σ_bin = √(σ_stat² + (0.02 c_bin)²), because a
statistically well-determined median still carries fitting, binning and
numerical systematics, and low-mass bins with many haloes would otherwise
dominate [src: arXiv:1809.07326, Sect. II.3]. The scatter about the
relation is about 0.16 dex in their sample [src: same] and 0.11 dex
(log-normal) for relaxed Planck haloes in Dutton & Macciò [src:
arXiv:1402.7073, Sect. 4.1]; the two samples differ in their relaxation cut, which may account for part of the difference
[der: from the two selections in Step 1].

### Step 6. Convert to the mass definition of the analysis
<!-- key: step-6-convert-to-the-mass-definition-of-the -->

Diemer & Joyce compute c_200c and convert assuming a fixed NFW profile, as
Colossus does automatically: the conversion to c_vir and c_200m keeps 5%
accuracy up to ν ≈ 2.5 and over-estimates low-redshift concentrations by up
to 15% above it; to c_500c it over-estimates above ν = 2, by 15% at ν = 4
[src: arXiv:1809.07326, App. B]. Fitting their formula directly to c_200m
instead degrades it to 10% (ΛCDM) [src: same].

### Step 7. Put c(M) into a lensing or satellite model
<!-- key: step-7-put-c-m-into-a-lensing-or-satellite-model -->

Two architectures, with different exposure to c(M):

- **Analytic halo model (KiDS-1000).** Matter and satellite profiles are
  both untruncated NFW at the same virial mass, on the Duffy et al. c(M),
  each multiplied by a free normalisation, f_h and f_s (Eq. 15 of
  arXiv:2210.03110) [src: Sect. 2.1]. Stated reason: AGN feedback pushes
  baryons and dark matter outward, "effectively changing the concentration
  of the matter distribution", and a free concentration suffices to absorb
  baryons on the scales used [src: Sect. 1, 2.1]. Priors on f_h and f_s are
  informative and checked not to inform Ω_m and S8 [src: App. B]. Result:
  both consistent with 1, preferring lower values, f_h > 0.65 and f_s >
  0.38 (1σ lower limits) [src: Sect. 4.3].
- **Emulated halo statistics (Dark Emulator, HSC × SDSS).** The matter
  around haloes comes from the emulated halo–matter spectrum P_hm, so c(M)
  enters only through the satellite profile ũ_s (NFW with the Diemer &
  Kravtsov 2015 c(M), not free, or the emulated halo–matter profile as an
  option) (arXiv:1811.09504, App. G, Eqs. G6–G8) [src]; HSC-Y1 × SDSS
  computes ũ_s from a Colossus c(M) [src: arXiv:2111.02419, Sect. IV.1.2].
  The KiDS authors list as a drawback of dark-matter-only emulators that
  they "do not offer a simple way to accommodate for such flexibility" [src:
  arXiv:2210.03110, Sect. 2.1].
- **Theoretical error instead of a free parameter (BOSS × lensing).** The
  matter NFW concentration inside P_hm is rescaled by f_conc = 0.84, 0.61
  and 1.26, from the best fit and 1σ range of GAMA groups, with the HOD held
  at its fitted posterior: clustering is unchanged and the one-halo lensing
  falls; the change of halo masses that feedback would also cause (and hence
  of the two-halo term) is not included [src: arXiv:2202.07440, Sect. 4.1].

**Off-centring.** A fraction f_off of centrals is displaced with a Gaussian
of width R_off, through the Fourier kernel H_off(k) = 1 − f_off + f_off
exp[−(kR_off)²/2] multiplying the central term of P_gm (arXiv:1811.09504,
Eqs. G7–G8) [src]. HSC-Y1 × SDSS leaves it out of the baseline and adds two
parameters per lens sample in an extended model; cosmological constraints
are "robust against these variants" [src: arXiv:2111.02419, Sect. IV.1.2,
App. G]; mock tests recover S8 within 0.5σ for off-centred centrals "except
for extreme cases" [src: Sect. IV.1.2].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### NFW fit, Einasto fit or V_max ratio
<!-- key: nfw-fit-einasto-fit-or-vmax-ratio -->

At z = 0 V_max/V_200 and NFW fits agree within statistical errors; at higher
redshift and mass V_max gives concentrations up to 15% higher, because any
perturbation scatters V_max upward and V_max/V_200 approaches 1 near c_200 ≃
2.2, so errors are amplified for the low concentrations of massive and
high-z haloes; the V_max method even gives a positive c(M) slope at z = 3
[src: arXiv:1402.7073, Sect. 3.1.1, Fig. 6 caption]. NFW and Einasto
concentrations differ by up to ~15%, with a mass trend that makes the
Einasto c(M) steeper and faster-evolving [src: Sect. 3.1.2]. Diemer & Joyce
quote agreement to about 10% or better [src: arXiv:1809.07326, Sect. II.3].
The Einasto α is ≃ 0.16 for 10¹² h⁻¹M_⊙ at low z and ≃ 0.25 at z ~ 4,
rising steeply above 10¹⁴ h⁻¹M_⊙; α = 0.0095 ν² + 0.155 removes the redshift
dependence (Eq. 17, Gao et al. form) [src: arXiv:1402.7073, Sect. 6.2].

### Relaxed-only or full sample
<!-- key: relaxed-only-or-full-sample -->

Relaxed-only relations are higher; a full sample keeps the high-ν upturn
from unrelaxed haloes [src: arXiv:1809.07326, Sect. II.2;
arXiv:1804.10199, Sect. III.1]. Which one a galaxy–halo model needs depends
on whether its haloes are selected for relaxation: survey hosts are not
[der].

### Which c(M), and in which cosmology
<!-- key: which-c-m-and-in-which-cosmology -->

A WMAP-era relation in a Planck-cosmology analysis is low: relaxed Planck
concentrations are ~20% higher than WMAP5 ones and close to WMAP1, log₁₀ c_200
= 0.905 − 0.101 log₁₀(M_200/10¹² h⁻¹M_⊙) (Eq. 8) and log₁₀ c_vir = 1.025 −
0.097 log₁₀(M_vir/10¹² h⁻¹M_⊙) (Eq. 9) [src: arXiv:1402.7073, Sect. 4.1].
The Duffy et al. relation, fitted in WMAP5, is the base of the KiDS-1000
halo model, with f_h free [src: arXiv:2210.03110, Sect. 2.1] [der: the f_h
posterior absorbs both baryons and any cosmology mismatch of the relation].
Recent models disagree among themselves: Diemer & Joyce differ from Correa
et al. and Ludlow et al. models by up to 20%, the latter describing only
relaxed haloes (no upturn), and from Bolshoi/MultiDark Rockstar data by
about 10% at low and high mass [src: arXiv:1809.07326, Sect. IV.2, Fig. 6
caption].

### Free normalisation, theoretical error or emulator
<!-- key: free-normalisation-theoretical-error-or-emulator -->

Free f_h, f_s (KiDS-1000) keeps small scales and pays with two weakly
constrained parameters; the theoretical-error route (Amon et al.) keeps the
model fixed and widens the budget; the emulator route (HSC) has no handle on
baryons in the matter profile and relies on scale cuts [src:
arXiv:2210.03110, Sect. 2.1, 4.1; arXiv:2202.07440, Sect. 4.1;
arXiv:2111.02419, Sect. IV.1.2]. KiDS states that HSC's more conservative
scale cuts arise from that concern [src: arXiv:2210.03110, Sect. 4.1].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Minimum particles | 10⁴ (Duffy); 500 (Dutton & Macciò, NFW); 2000 (Child); 1000 in R_200c + 200 in r_s (Diemer & Joyce) | — | arXiv:0804.2486; arXiv:1402.7073; arXiv:1804.10199; arXiv:1809.07326 | Sect. 2.1; 2.4; App. B.6; II.2 |
| Maximum measurable c | 29.0 (N_min/1000)^(1/3) for ε = 0.025 L/N | Dutton & Macciò | arXiv:1402.7073 | Sect. 2.4 |
| Relaxation cut | x_off < 0.07 (and ρ_rms < 0.5) | Duffy; Child; Dutton & Macciò | arXiv:0804.2486; arXiv:1804.10199; arXiv:1402.7073 | Sect. 2.1; III.1; 2.3 |
| Relaxed fraction | ~80% at z = 0; ~50% at z = 5 | Dutton & Macciò | arXiv:1402.7073 | Sect. 2.3 |
| Radial fit range | −1.25 ≤ log(r/r_vir) ≤ 0 (Duffy); 0.01–1.2 r_vir (Dutton & Macciò) | — | arXiv:0804.2486; arXiv:1402.7073 | Sect. 2.1; 2.2 |
| Centre choice effect | < 5% relaxed; up to 20% unrelaxed at 2000 particles | Child | arXiv:1804.10199 | App. B.3 |
| Estimator spread | up to 10% at z = 3 (fit, enclosed mass, peak) | Child | arXiv:1804.10199 | Sect. III.1 |
| V_max vs NFW | V_max up to 15% higher at high z and mass | Dutton & Macciò | arXiv:1402.7073 | Sect. 3.1.1 |
| NFW vs Einasto | within ~15% | Dutton & Macciò | arXiv:1402.7073 | Sect. 3.1.2 |
| Einasto α(ν) | 0.0095 ν² + 0.155 | Gao form, confirmed | arXiv:1402.7073 | Eq. 17 |
| Planck c–M | log₁₀ c_200 = 0.905 − 0.101 log₁₀(M_200/10¹² h⁻¹M_⊙) | relaxed, > 500 particles | arXiv:1402.7073 | Eq. 8 |
| Planck vs WMAP5 | ~20% higher | relaxed | arXiv:1402.7073 | Sect. 4.1 |
| Scatter | 0.11 dex (relaxed); ~0.16 dex (all) | — | arXiv:1402.7073; arXiv:1809.07326 | Sect. 4.1; II.3 |
| Per-bin systematic | 2% of c | Diemer & Joyce | arXiv:1809.07326 | Sect. II.3 |
| NFW conversion error | ≤ 5% to vir, 200m up to ν ≈ 2.5; up to 15% beyond, and for 500c at ν = 4 | Diemer & Joyce | arXiv:1809.07326 | App. B |
| c(M) normalisations | f_h > 0.65, f_s > 0.38 (1σ lower limits) | KiDS-1000 | arXiv:2210.03110 | Sect. 4.3 |
| f_conc tested | 0.84, 0.61, 1.26 | BOSS × lensing | arXiv:2202.07440 | Sect. 4.1 |
| Off-centring parameters | 2 per lens sample (f_off, R_off) | HSC-Y1 × SDSS extended model | arXiv:2111.02419 | Sect. IV.2, App. G |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Concentrations from too few particles.** Fit and enclosed-mass values
  diverge below ~2000 particles; peak finding needs ~10 times more [src:
  arXiv:1804.10199, App. B.6]. Test: compare two resolutions at fixed mass.
- **Relaxation cut not stated.** Changes the amplitude and the high-mass
  shape of c(M) [src: arXiv:1809.07326, Sect. II.2]. Test: report both
  samples, or state which one the model's haloes resemble.
- **Method mixed across papers.** V_max-based and fit-based relations
  differ by up to 15% at high z and mass [src: arXiv:1402.7073, Sect.
  3.1.1]; Einasto versus NFW by up to ~15% [src: Sect. 3.1.2]. Test:
  compare like with like before calling two relations discrepant.
- **Converting at high peak height.** The fixed-NFW conversion is good to
  5% only up to ν ≈ 2.5 [src: arXiv:1809.07326, App. B]. Test: for cluster
  hosts, use a relation calibrated in the target definition.
- **WMAP-era relation in a Planck analysis.** ~20% low [src:
  arXiv:1402.7073, Sect. 4.1]. Test: free normalisation, or a
  cosmology-dependent model.
- **f_conc changed without the halo mass.** Rescaling concentration alone
  leaves the two-halo term at dark-matter-only masses [src:
  arXiv:2202.07440, Sect. 4.1].
- **Off-centring ignored.** Lowers ΔΣ inside R_off; HSC finds S8 robust
  except in extreme mock cases [src: arXiv:2111.02419, Sect. IV.1.2]. Test:
  refit with (f_off, R_off) free.
- **Skewed c_fit distributions.** Means of fitted concentrations are pulled
  by an unbounded tail [src: arXiv:1804.10199, Sect. III.1]. Use medians or
  enclosed-mass estimates.

## Reading list
<!-- key: reading-list -->

- Method, measurement: Child et al. 2018, arXiv:1804.10199 — three
  estimators, shell selection, centring and particle-number tests.
- Method, NFW vs Einasto vs V_max: Dutton & Macciò 2014, arXiv:1402.7073 —
  fitting set-up, relaxation criteria, Planck c(M), α(ν), resolution bound.
- Method, model: Diemer & Joyce 2019, arXiv:1809.07326 — no relaxation cut
  and why, per-bin systematic, conversion accuracy between definitions.
- Foundation of the common power law: Duffy et al. 2008, arXiv:0804.2486 —
  fitting range, relaxed sample.
- Application, analytic lensing model: Dvornik et al. 2023,
  arXiv:2210.03110 — f_h and f_s as the baryon handle.
- Application, emulator: Nishimichi et al. 2019, arXiv:1811.09504 —
  where c(M) enters (satellites only) and the off-centring kernel.
- Critique, theoretical error: Amon et al. 2023, arXiv:2202.07440 —
  concentration rescaling as a baryon bracket and its omission of mass
  changes.

## Not verified
<!-- key: not-verified -->

- Prada et al. 2012 and Klypin et al. (V_max-based concentrations), Gao et
  al. 2008 (α(ν)), Hu & Kravtsov 2003 (definition conversion), Diemer &
  Kravtsov 2015, Correa et al. 2015 and Debackere et al. 2020/2021 (baryons
  and concentration) are cited in the papers read; not read here.
- The priors on f_h and f_s in KiDS-1000 (its App. B table) and the
  numerical α(ν) of Duffy et al.'s Fig. 1 legend were not read.
- No 2025–2026 concentration-measurement paper was searched for in this
  run (budget kept for the bodies above).
