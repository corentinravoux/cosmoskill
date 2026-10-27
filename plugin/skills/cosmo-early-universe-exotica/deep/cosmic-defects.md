# Cosmic strings and domain walls: from a loop model to a Gμ limit — cosmo-early-universe-exotica dossier

Scope: how a string-tension limit or fit is produced from GW data (loop
number density from the VOS model or from the A, B, C distributions,
emission spectrum P_k or cusp/kink/kink–kink bursts, harmonic sum or burst
superposition, metastable and superstring modifications), how LVK, PTAs and
Planck set up their searches, how domain-wall spectra are parametrised, and
which modelling choice moves Gμ by orders of magnitude; the limits
themselves are in the reference files.
Snapshot: 2026-10-21.
From: LISA Cosmology WG 2022, Sect. 7 and 9.2.3; Carr et al. 2026, Sect.
II.2.2; Planck, LVK and PTA string searches.

Already in L2, not repeated here: the defect families, the Ω_GW sum and the
PTA priors in `physics-and-methods.md#cosmic-strings-and-other-defects`; the
Planck, LVK O3 and NANOGrav values and Bayes factors in
`results.md#cosmic-strings-and-defects`; the loop-distribution systematic in
`systematics.md#theory-templates-for-cosmological-backgrounds`. The PTA
likelihood is in `deep/sgwb-pta.md`; the phase-transition spectral shape
reused for domain walls in `deep/phase-transitions.md`.

## How it is done
<!-- key: how-it-is-done -->

Notation. μ is the string tension (energy per unit length) and Gμ its
dimensionless value; ℓ the invariant loop length; t cosmic time; n(ℓ, t) (or
n_l) the number density of non-self-intersecting loops per unit length and
volume; Γ the total GW power of a loop in units of Gμ²; k the harmonic
number; q the spectral index of the per-harmonic power. Two symbol clashes
to watch: NANOGrav uses α_* for the loop size at formation and Γ_d for the
monopole nucleation rate (arXiv:2306.16219, Sect. V.4), while LVK uses Γ_d
for the dimensionless decay constant that NANOGrav calls Γ
(arXiv:2101.12248, Sect. II).

### Step 1. Choose the loop number density
<!-- key: step-1-choose-the-loop-number-density -->

Two families are in use.

**Velocity-dependent one-scale (VOS) model (NANOGrav).** Loops form at time
t_* with size α_* t_*, and [src: arXiv:2306.16219, Eqs. 43–45]

n_l(ℓ, t) = ℱ C_* Θ(t − t_*) Θ(t_* − t_ini) / [α_*(α_* + ΓGμ + α̇_* t_*)
t_*⁴] (a_*/a(t))³,

with t_* = (ℓ + ΓGμ t)/(α_* + ΓGμ), C(t) = (c̃/√2) v̄/ξ³ and α(t) = α_L ξ.
ℱ = 0.1 is an efficiency factor, c̃ ≃ 0.23 the loop-chopping parameter,
α_L ≃ 0.37 the loop length in units of the correlation length L = ξt, ξ and
v̄ the dimensionless correlation length and rms velocity of long strings,
obtained by solving the VOS equations with the exact ΛCDM expansion
including the temperature dependence of g_*. Deep in radiation domination
ξ_r ≃ 0.27, v̄_r ≃ 0.66, α ≃ 0.10; with constant g_* the result "agrees very
well" with Nambu–Goto simulations [src: arXiv:2306.16219, Sect. V.4, "Model
description", text around Eqs. 43–45].

**Simulation-calibrated distributions (LVK, EPTA, multi-band analyses).**

- Model A (BOS, Blanco-Pillado–Olum–Shlaer): radiation era
  n = 0.18/[t⁴(ℓ/t + ΓGμ)^(5/2)] for ℓ/t < 0.1, with separate expressions for radiation-era
  survivors and matter-era loops (Zhang et al. 2026, arXiv:2610.02590)
  [src: Eqs. S-49 to S-51].
- Model B (LRS, Lorenz–Ringeval–Sakellariadou): power-law loop production
  with a gravitational back-reaction scale γ_c = Υ(Gμ)^(1+2χ), Υ = 20;
  C_rad ≃ 0.08, C_mat ≃ 0.016, χ_rad = 0.20, χ_mat = 0.295 [src: Sect.
  S-III.2, Eqs. S-52 to S-54]. It produces far more tiny loops than model
  A [src: arXiv:2101.12248, Sect. II].
- Models C-1, C-2: hybrids with free slope; C-1 follows A in the radiation
  era and B in the matter era, C-2 the reverse; parameters (c_rad, χ_rad,
  c_mat, χ_mat) = (0.15, 0.45, 0.019, 0.295) for C-1 and (0.019, 0.20,
  0.003, 0.45) for C-2, γ_∞ = 0.1 [src: arXiv:2610.02590, Sect. S-III.3].
  LVK quotes (χ_rad, χ_mat) = (0.45, 0.295) and (0.2, 0.45) [src:
  arXiv:2101.12248, Sect. V].

Why both: the simulations assume intercommutation probability 1 and differ
in their treatment of small loops, where gravitational back-reaction (not
simulated) matters [src: arXiv:2306.16227, Sect. 4.2.1].

### Step 2. Choose the emission spectrum of a loop
<!-- key: step-2-choose-the-emission-spectrum-of-a-loop -->

**Harmonic form (NANOGrav).** A loop radiates at f = 2k/ℓ with power P_k =
(Γ/ζ(q)) k^(−q), so that Σ P_k = Γ; Γ = 50 "as suggested by numerical
simulations" [src: arXiv:2306.16219, Eq. 41]. Templates [src: Sect. V.4]:
stable-c, cusps only, q = 4/3; stable-k, kinks only, q = 5/3; stable-m,
all power in the fundamental mode, P_1 = Γ; stable-n, numerically computed
spectra including cusps and kinks, q ≈ 4/3 for k ≳ 100 and up to q ~ 1.5
near k ~ 10. Sum to k_max = 10⁵ "which ensures good convergence".

**Burst form (LVK).** Cusps, kinks and kink–kink collisions emit strain h_i
= A_i f^(−q_i), q_c = 4/3, q_k = 5/3, q_kk = 2, with A_i = g_1,i Gμ ℓ^(2−q_i)/
[(1+z)^(q_i−1) r(z)] and g_1,c ≈ 0.85, g_1,k ≈ 0.29, g_1,kk ≈ 0.10 [src:
arXiv:2101.12248, Eqs. 1–2]. Emission is beamed within θ_m = (g_2 f(1+z)ℓ)^
(−1/3), g_2 = √3/4, required < 1 [src: Eq. 3]. The burst rate per loop size
and volume is (2/ℓ) N_i n(ℓ, t) Δ_i (1+z)⁻¹ with beaming fraction Δ_i =
(θ_m/2)^(3(2−q_i)) [src: Eq. 4]; N_c, N_k are the numbers of cusps and
kinks per oscillation, N_kk ≈ N_k²/4. Γ follows from N_c, N_k [src: Eq. 8];
LVK fixes N_c = 1 and scans N_k = 1–200, the upper end motivated by
simulations favouring Γ ~ 50 [src: Sect. II]. EPTA writes the same Γ =
N_cΓ^c + N_kΓ^k + (N_k²/4)Γ^kk and uses either N_c = 2, N_k = 0 (Γ = 57) or
N_c = 1 with N_k uniform in [1, 200] [src: arXiv:2306.16227, Eqs. 17–18].

### Step 3. Sum over loops and history
<!-- key: step-3-sum-over-loops-and-history -->

NANOGrav: Ω_GW(f) = (8π/3H₀²)(Gμ)² Σ_k P_k ℐ_k(f), ℐ_k(f) = (2k/f)
∫ dt (a/a₀)⁵ n_l((2k/f)(a/a₀), t) [src: arXiv:2306.16219, Eqs. 40, 42].
LVK: Ω_GW(f) = (4π²/3H₀²) f³ Σ_i ∫dz ∫dℓ h_i² d²R_i/(dz dℓ) [src:
arXiv:2101.12248, Eq. 10]. EPTA writes the harmonic form summed over cusp,
kink and kink–kink contributions with ΛCDM H(z) from Planck 2018 [src:
arXiv:2306.16227, Eq. 19].

The two forms are discrete and continuous representations of the same
radiation and agree on the scale-invariant plateau; they diverge on the
rising low-frequency branch, where the first harmonics dominate (Zhang et
al. 2026, arXiv:2610.02590) [src: abstract]. At PTA frequencies the
spectrum is dominated by large loops formed near and after matter–radiation
equality; at ground-based frequencies by loops formed in the radiation era
[src: arXiv:2306.16227, Sect. 4.2.1; arXiv:2101.12248, Sect. V].

### Step 4. Add metastability or reduced intercommutation
<!-- key: step-4-add-metastability-or-reduced -->

- **Metastable strings** (NANOGrav): n_l^meta = Θ(t_s − t_*) E(ℓ, t) n_l,
  with t_s = Γ_d^(−1/2), Γ_d = (μ/2π) e^(−πκ) the monopole nucleation rate
  per unit length and time, √κ = m_GUT/μ^(1/2) ~ Λ_GUT/Λ_U(1), and E = exp{−Γ_d
  [ℓ(t − t_*) + ½ΓGμ(t − t_*)²]} [src: arXiv:2306.16219, Eqs. 46–50]. The
  prior √κ ∈ [7, 9.5] is narrow because √κ ≫ 10 is indistinguishable from
  stable strings and √κ ~ 1 gives no PTA signal [src: Sect. V.4]. meta-l
  keeps loops only (monopoles with unconfined flux radiate gauge bosons);
  meta-ls adds segments with q = 1 [src: Sect. V.4].
- **Superstrings**: Ω_GW → Ω_GW/P with intercommutation probability P,
  log₁₀ P ∈ [−3, 0]; called "standard practice" in the absence of
  simulations, which would need to run up to 10³ times longer [src: Eq.
  52 and text].

### Step 5. Search and set the limit
<!-- key: step-5-search-and-set-the-limit -->

- **LVK stochastic.** Cross-correlation spectra O1–O3; the 95% excluded
  region in (Gμ, N_k) with N_c = 1 [src: arXiv:2101.12248, Sect. V].
- **LVK bursts.** Matched filter with the power-law waveforms, coincidence
  in at least two detectors, ranking by a likelihood ratio; 273.5 days of
  O3 coincident data; background from 300 time shifts (225 yr); loudest-
  event threshold log₁₀ Λ ≃ 15.0 (cusps), 15.1 (kinks) and 15.1 (kink–kink
  collisions); efficiencies from injections [src: arXiv:2101.12248, Sect.
  III]. The burst limits are weaker than the stochastic ones except
  for model C-1 with N_k > 70 [src: Sect. V].
- **PTA.** NANOGrav and EPTA fit the template with per-pulsar noise; EPTA
  uses its hierarchical likelihood on 25 pulsars of DR2new [src:
  arXiv:2306.16227, Sect. 4.2.2]. NANOGrav quotes two kinds of upper limit
  when SMBHBs are added: the K-ratio bound (likelihood ratio to SMBHB-only
  falls below 1/10) and the 95% highest-posterior-density interval, with
  a special rule when the HPD threshold meets the low-Gμ plateau [src:
  arXiv:2306.16219, Sect. V.4, footnote 6]. It also overlays the CMB string
  bound and its own LVK bound Ω_GW ≤ 1.7 × 10⁻⁸ at 25 Hz [src: Eq. 24,
  Fig. 10 caption].
- **Multi-band.** Joint ln ℒ = ln ℒ_PTA + ln ℒ_LVK, sampling (Gμ, N_c, N_k)
  with log-uniform Gμ ∈ [10⁻¹⁸, 10⁻⁶], N_c ∈ [0, 3], N_k ∈ [1, 10], plus
  SMBHB (NANOGrav's bivariate Gaussian) and a compact-binary background
  with index 2/3 for LVK O1–O4a; PTA likelihood refitted from the public
  HD free-spectrum posteriors [src: arXiv:2610.02590, Sect. "Bayesian
  inference", Eqs. 7–11].
- **CMB (Planck 2013).** The string spectrum is added uncorrelated to the
  adiabatic one with amplitude f₁₀ (string fraction at ℓ = 10) as a
  seventh parameter in COSMOMC, Planck + WMAP polarisation, optionally ACT
  and SPT high-ℓ data; the six ΛCDM parameters are not significantly
  affected and the strongest correlation is with Ω_b h² (and N_eff, Y_He
  for Abelian–Higgs strings) [src: arXiv:1303.5085, Sect. 3, Table 3].

### Domain walls
<!-- key: domain-walls -->

NANOGrav: h²Ω_GW = (3/32π) 𝒟 ε̃ α_*² 𝒮(f/f_p), with 𝒟 the dilution factor
of the phase-transition section, ε̃ = 0.7 from simulations, α_* the wall
energy fraction at the decay temperature T_* [src: arXiv:2306.16219, Eqs.
54–55], peak f_p = 1.14 nHz (10.75/g_*,s)^(1/3)(g_*/10.75)^(1/2)(T_*/10
MeV) [src: Eq. 56], and the broken power law with a = 3 fixed by causality
and b ∈ [0.5, 1], c ∈ [0.3, 3] [src: Eq. 57]. Decay into dark radiation
(dw-dr) is parametrised by ΔN_eff ≃ 0.62 (10.75/g_*)^(1/3)(g_*,s/g_*)(α_*/
0.1), prior up to 0.39 [src: Eq. 58]; decay into Standard-Model particles
(dw-sm) requires T_* ≳ 2.7 MeV from BBN and α_* < 0.3 [src: Sect. V.5].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Loop distribution
<!-- key: loop-distribution -->

The largest single choice. LVK O3 stochastic exclusions: model A Gμ ≳ (9.6 ×
10⁻⁹ – 10⁻⁶), B ≳ (4.0–6.3) × 10⁻¹⁵, C-1 ≳ (2.1–4.5) × 10⁻¹⁵, C-2 ≳
(4.2–7.0) × 10⁻¹⁵, the ranges spanning N_k [src: arXiv:2101.12248, Sect.
V]. The C-1 exclusion holds "aside from a small region where N_k ≳ 180",
which the stochastic analysis leaves open [src: same]. With model A the
strongest limit came from PTAs (Gμ ≳ 10⁻¹⁰); with B
and C-1 from LVK; with C-2 the CMB is almost as strong as LVK [src: Sect.
V]. In the 2026 multi-band analysis only model A can explain the PTA signal
without violating LVK; B, C-1 and C-2 are capped by LVK about 4.6 orders of
magnitude below their PTA-only bounds [src: arXiv:2610.02590, "Constraints"
paragraph]. EPTA, with BOS (= A) and LRS (= B) and Γ = 57, finds log₁₀ Gμ =
−10.07 (+0.47/−0.36) and −10.63 (+0.24/−0.22) (90%) from strings alone, and
< −9.77 and < −10.44 (95% quantile) with SMBHBs [src: arXiv:2306.16227,
Sect. 4.2.2].

### Harmonic or burst spectrum
<!-- key: harmonic-or-burst-spectrum -->

Where the detector sits on the rising branch (models B, C at LVK), the
harmonic sum gives more amplitude and strengthens the LVK limit by 25%, 21%
and 31% (B, C-1, C-2); on the plateau (model A at LVK) the two converge to
~9%, the residual coming from the g_* tilt across the QCD transition [src:
arXiv:2610.02590, "Constraints" paragraph]. For model A with NANOGrav the
harmonic limit is 1.4 × 10⁻¹⁰ against 3.4 × 10⁻¹⁰ in the burst form [src:
Table S-1].

### Fixed or free kink and cusp numbers
<!-- key: fixed-or-free-kink-and-cusp-numbers -->

Fixing N_c = 1 and scanning N_k (LVK, EPTA case ii) gives a band of limits;
marginalising over N_c, N_k (multi-band) folds this into one limit. In
model A many kinks or cusps weaken the LVK constraint, in B and C the
bounds are insensitive to N_c [src: arXiv:2101.12248, Sect. V]. EPTA finds
the N_k posterior nearly uninformative and degenerate with Gμ [src:
arXiv:2306.16227, Sect. 4.2.2].

### VOS model or simulation-calibrated distribution
<!-- key: vos-model-or-simulation-calibrated-distribution -->

The VOS route lets NANOGrav include the exact g_*(T) history; it is
calibrated to agree with Nambu–Goto simulations at constant g_* [src:
arXiv:2306.16219, Sect. V.4]. Its four stable templates differ only in P_k;
for fixed Gμ stable-m gives the strongest nanohertz signal, then stable-k,
stable-n, stable-c, which orders their posteriors [src: Sect. V.4].

### Nambu–Goto or field-theory strings
<!-- key: nambu-goto-or-field-theory-strings -->

Both PTA analyses use Nambu–Goto loops; NANOGrav calls the relation to
Abelian–Higgs strings "the subject of ongoing research" [src:
arXiv:2306.16219, Sect. V.4]. Field-theory simulations find that network
loops decay quickly, lifetime 0.14 ± 0.04 of their initial length, through
a non-linear channel much stronger than gravitational radiation, so "one
cannot use the Nambu-Goto model to derive robust constraints on the tension
of field theory strings"; the proposed parameter is the fraction f_NG of
Nambu–Goto-like loops, f_NG < 0.1 at 95% (Hindmarsh et al. 2021,
arXiv:2103.16248) [src: abstract]. A NANOGrav-compatible Abelian–Higgs
network then needs Gμ f_NG^2.6 ≳ 3.2 × 10⁻¹³ (95%), and diffuse γ-ray
limits require most of the network energy to go into dark matter or dark
radiation (Hindmarsh & Kume 2022, arXiv:2210.06178) [src: abstract]. On
the CMB side Planck already brackets the issue: Nambu–Goto Gμ < 1.5 × 10⁻⁷
against Abelian–Higgs < 3.2 × 10⁻⁷ (Planck + WP) [src: arXiv:1303.5085,
Table 2].

### Segments in metastable networks
<!-- key: segments-in-metastable-networks -->

NANOGrav's meta-ls, where segments dominate the signal in the highest-
posterior region, gives a Bayes factor of 21.3 against 13.4 for loops only
[src: arXiv:2306.16219, Sect. V.4]. A 2025 study argues that thermal
fluctuations on segments damp the monopole oscillations, so the segment
contribution is negligible in realistic situations (Chitose et al. 2025,
arXiv:2507.12386) [src: abstract]; under that reading meta-l is the
relevant template.

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| VOS calibration | ℱ = 0.1; c̃ ≃ 0.23; α_L ≃ 0.37; ξ_r ≃ 0.27, v̄_r ≃ 0.66, α ≃ 0.10 | NANOGrav | arXiv:2306.16219 | Sect. V.4 |
| Loop power | Γ = 50; k_max = 10⁵ | NANOGrav | arXiv:2306.16219 | Sect. V.4 |
| Metastable prior | √κ ∈ [7.0, 9.5]; data prefer √κ ~ 8, log₁₀ Gμ ~ −(7…4) | NANOGrav 15 yr | arXiv:2306.16219 | Sect. V.4 |
| Stable-string limits with SMBHB | K-ratio log₁₀ Gμ < −9.67, −9.87, −10.10, −9.71; 95% HPDI < −9.88, −10.04, −10.26, −9.90 (c, k, m, n) | NANOGrav 15 yr | arXiv:2306.16219 | Sect. V.4 |
| Superstring Bayes factor | 46 ± 2 (alone), 37 ± 2 (with SMBHB) | NANOGrav 15 yr | arXiv:2306.16219 | Sect. V.4 |
| Burst constants | g_1,c ≈ 0.85, g_1,k ≈ 0.29, g_1,kk ≈ 0.10; g_2 = √3/4 | LVK | arXiv:2101.12248 | Sect. II |
| Burst search | 273.5 d; 300 time shifts, 225 yr background | LVK O3 | arXiv:2101.12248 | Sect. III |
| Model B parameters | Υ = 20; C_rad ≃ 0.08, C_mat ≃ 0.016; χ_rad = 0.20, χ_mat = 0.295 | multi-band | arXiv:2610.02590 | Sect. S-III.2 |
| Multi-band limits (harmonic, 95%) | A: 1.3 × 10⁻¹⁰ (joint, PTA-dominated); B, C-1, C-2: 2.0, 1.1, 2.5 × 10⁻¹⁵ (LVK) | NANOGrav 15 yr + LVK O1–O4a | arXiv:2610.02590 | Eqs. 12–13, Table S-1 |
| Model A strings + SMBHB vs SMBHB | Bayes factor 1.00 (harmonic), 0.91 (burst); EPTA 1.32, 1.30 | multi-band | arXiv:2610.02590 | "Constraints"; Sect. S-V.1 |
| EPTA string fits | log₁₀ Gμ = −10.07 (+0.47/−0.36) BOS, −10.63 (+0.24/−0.22) LRS (90%) | EPTA DR2new | arXiv:2306.16227 | Sect. 4.2.2 |
| Planck f₁₀ | < 0.015 (NG), < 0.028 (AH), Planck + WP | Planck 2013 | arXiv:1303.5085 | Table 2 |
| Domain walls | ε̃ = 0.7; ΔN_eff prior up to 0.39; dw-sm T_* ≳ 2.7 MeV, α_* < 0.3 | NANOGrav | arXiv:2306.16219 | Sect. V.5 |
| Field-theory loops | lifetime 0.14 ± 0.04 ℓ_init; f_NG < 0.1 (95%) | Abelian–Higgs simulations | arXiv:2103.16248 | abstract |

## What goes wrong
<!-- key: what-goes-wrong -->

- **A Gμ limit quoted without its loop model.** Shows up as limits that
  differ by six orders of magnitude between papers [src: arXiv:2101.12248,
  Sect. V]. Test: name the distribution (A/BOS, B/LRS, C, VOS) and N_c,
  N_k or Γ.
- **Nambu–Goto limits applied to field-theory strings.** Test: state f_NG
  or restrict the claim to Nambu–Goto loops [src: arXiv:2103.16248].
- **Harmonic and burst spectra mixed across bands.** On the rising branch
  they differ by tens of per cent in the limit [src: arXiv:2610.02590].
  Test: use one formalism for a joint fit.
- **Stable strings "fitting" the PTA signal.** Large Gμ gives a spectrum
  too flat, small Gμ too weak; stable strings give γ ≲ 4 only for log₁₀ A ≲
  −15.0 [src: arXiv:2306.16219, Sect. V.4]; EPTA DR2new likewise finds the
  predicted spectrum steeper than the data [src: arXiv:2306.16227, Sect.
  4.2.2]. Test: report Bayes factors and the K-ratio region, not only a
  posterior peak.
- **Metastable or superstring fits without the LVK band.** Fits at large
  Gμ must be checked against the LVK limit and the CMB string bound, which
  NANOGrav overlays [src: arXiv:2306.16219, Fig. 10 caption]. Test: joint
  PTA + LVK likelihood [src: arXiv:2610.02590].
- **Superstrings by 1/P rescaling.** A placeholder for missing simulations
  [src: arXiv:2306.16219, Sect. V.4]. Test: flag the result as template-
  limited.
- **Segment-dominated metastable signal.** Contested [src:
  arXiv:2507.12386]. Test: report meta-l alongside meta-ls.
- **HPD interval on a plateau.** Sampling noise in the plateau creates
  spurious disjoint intervals [src: arXiv:2306.16219, footnote 6]. Test:
  quote the K-ratio bound, which is likelihood-based and prior-robust.
- **Domain walls decaying into dark radiation without the N_eff bound.**
  Test: cap ΔN_eff in the prior, as NANOGrav does [src: Sect. V.5].

## Reading list
<!-- key: reading-list -->

- Method and application: Afzal et al. 2023, arXiv:2306.16219 — VOS loop
  density, P_k templates, metastable and superstring modifications, domain
  walls, K-ratio and HPD limits (Sects. V.4–V.5).
- Method and application: LVK 2021, arXiv:2101.12248 — burst waveforms,
  beaming, models A, B, C, burst and stochastic limits.
- Method and comparison: Zhang et al. 2026, arXiv:2610.02590 — loop
  distributions written out, harmonic versus burst, joint PTA + LVK fit.
- Application: Antoniadis et al. 2023, arXiv:2306.16227 — BOS and LRS on
  EPTA DR2new, Γ from N_c and N_k (Sect. 4.2).
- Foundation: Blanco-Pillado et al. 2014, arXiv:1309.6637 — loop number
  density from Nambu–Goto simulations.
- Application: Planck 2013 XXV, arXiv:1303.5085 — f₁₀ template fit and the
  NG/AH bracket (Sect. 3).
- Critique: Hindmarsh et al. 2021, arXiv:2103.16248; Hindmarsh & Kume 2022,
  arXiv:2210.06178 — field-theory loop decay and f_NG (abstracts).
- Critique: Chitose et al. 2025, arXiv:2507.12386 — segment emission
  (abstract).
- Model: Buchmüller et al. 2020, arXiv:2009.10649 — metastable strings from
  B−L breaking.

## Not verified
<!-- key: not-verified -->

- The burst-to-harmonic correspondence formulae of arXiv:2610.02590
  (Sect. S-II) and its PTA refitting method were not read.
- NANOGrav's domain-wall results (Sect. V.5 results) and segment number
  densities (its Appendix) were not read.
- The Planck 2013 bispectrum, wavelet and Minkowski-functional pipelines
  (Sect. 4) were not read beyond L2.
- No PPTA, CPTA, MPTA or LVK O4 string-specific analysis was read.
- Bodies of arXiv:2103.16248, arXiv:2210.06178 and arXiv:2507.12386 were not
  read; only abstracts.
