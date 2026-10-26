# Empirical, semi-analytic and hydrodynamical models — cosmo-galaxy-halo-connection dossier

Scope: how an empirical model of galaxy formation histories (UniverseMachine,
EMERGE) is parameterised and fitted (halo layer, star-formation
parameterisation, satellites and orphans, forward-modelled observational
errors, likelihood, sampler, model selection), how semi-analytic models are
tuned and what skipping the tuning costs, how a survey-like tracer sample and
its HOD are extracted from a hydrodynamical run, and how such catalogues are
used to validate an occupation-model pipeline.
Snapshot: 2026-10-21.
From: Wechsler & Tinker 2018 (arXiv:1804.03097), Sect. 2.2.4, Sect. 2.3 and
Sect. 2.4; Crain et al. 2023 review (arXiv:2309.17075).

Already in L2, not repeated here: what each model family parameterises and
its headline findings (age matching, EMERGE, UniverseMachine, SAM review,
nIFTy scatter, Crain et al.) in
`physics-and-methods.md#empirical-semi-analytic-and-hydrodynamical`; the
DESI DR1 single-mock verification (its χ² and Δχ²) in
`systematics.md#residual-redshift-space-distortions-exclusion`; the TNG300
budget of the lensing-is-low excess in
`systematics.md#assembly-bias-and-secondary-dependencies`. How a
hydrodynamical suite fixes its own feedback parameters (targets, emulators,
convergence) is in
`cosmo-simulations-mocks/deep/hydro-subgrid-calibration.md`; SHAM orphans and
disruption in `deep/abundance-matching-shmr.md`; assembly-bias diagnostics in
hydro runs (shuffling) in `deep/assembly-bias.md`.

Symbols. v_max: maximum circular velocity of a halo, max √(GM(<R)/R).
v_Mpeak: v_max at the redshift where the halo reached its peak mass M_peak.
Δv_max: ratio of current v_max to v_max one dynamical time earlier (Eq. 1 of
arXiv:1806.07893). f_Q: quenched fraction. ε: instantaneous baryon
conversion efficiency (EMERGE). a: scale factor. α_c, α_s: central and
satellite velocity-bias factors. f_ic: HOD incompleteness factor.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Choose the halo layer and keep its definitions
<!-- key: step-1-choose-the-halo-layer-and-keep-its -->

The galaxy model inherits the simulation's resolution, finder, merger trees
and mass definition.

- **UniverseMachine.** Bolshoi-Planck, 250 h⁻¹Mpc, 2048³ particles, particle
  mass 1.6 × 10⁸ h⁻¹M_⊙, force resolution 1 h⁻¹kpc, 180 snapshots equally
  spaced in log a, flat ΛCDM (h = 0.678, Ω_m = 0.307, σ8 = 0.823, n_s =
  0.96); MDPL2 (1 h⁻¹Gpc, 3840³) only for the covariance of the correlation
  functions; Rockstar haloes and Consistent Trees merger trees for both
  [src: arXiv:1806.07893, Sect. 2.1].
- **EMERGE.** Two boxes: a smaller one, run many times for the parameter
  search, and a larger one run once at the best fit to cover a wider mass
  range; the two give "identical results for the galaxy populations" [src:
  arXiv:1705.05373, Sect. 2.1]. The figure captions name 150 and 200 Mpc
  side lengths [src: captions of Figs. 4–5].
- **SAM comparison (nIFTy).** One 62.5 h⁻¹Mpc box, 270³ particles (9.31 ×
  10⁸ h⁻¹M_⊙), WMAP7, SUBFIND haloes with an FoF b = 0.2 host, objects of at
  least 20 particles, AHF MergerTree trees, and five mass definitions (M_fof,
  bound FoF mass, M_200c, M_200m, Bryan–Norman) because the 14 models each
  run with their own calibration [src: arXiv:1505.04607, Sect. 2]. SUBFIND
  host masses exclude subhaloes [src: same].

### Step 2. Parameterise star formation in haloes (empirical models)
<!-- key: step-2-parameterise-star-formation-in-haloes -->

**UniverseMachine** [src: arXiv:1806.07893, Sect. 3.1–3.2]. The SFR
distribution at fixed v_Mpeak and z is a sum of two log-normals, quenched and
star-forming (Eq. 2). The star-forming median is a double power law plus a
Gaussian in v = v_Mpeak/V (Eqs. 4–5), each parameter with a z = 0 value and
terms in (1 − a), ln(1 + z) and z (Eqs. 6–11). σ_SF = min(σ_SF,0 + (1 −
a)σ_SF,1, 0.3 dex) (Eq. 3); the quenched population is fixed at a median sSFR
of 10⁻¹¹·⁸ yr⁻¹ and 0.36 dex scatter, because "as long as SFR_SF ≫ SFR_Q,
the exact value of SFR_Q does not impact galaxy stellar masses or colours".
f_Q rises from Q_min to 1 as an error function of log v_Mpeak (Eqs. 12–15).
Assembly enters by rank: at fixed v_Mpeak and z, a halo's SFR percentile is
C_SF = C(r_c C⁻¹(C_Δvmax) + √(1 − r_c²) R) (Eq. 18), with C the unit Gaussian
cumulative distribution, R a unit normal and r_c(v_Mpeak) the rank
correlation between Δv_max and SFR (Eqs. 16–17). The random term R(t) sums
short- and long-timescale components, because without long-timescale
correlation the UVJ-quenched galaxies cannot be produced [src: Sect. 3.2].
Reasons for the variables: peak v_max "better matches galaxy clustering"
and avoids pseudo-evolution, but transient peaks after mergers led to using
v_max at the epoch of peak mass; Δv_max rather than accretion rate or
concentration because those are not robustly measured for satellites by
halo finders, whereas the v_max history is [src: Sect. 3.1].

**EMERGE** [src: arXiv:1705.05373, Sect. 3.1–3.2]. The SFR is the halo's
baryonic growth rate times ε(M, z) = 2ε_N [(M/M_1)^(−β) + (M/M_1)^γ]⁻¹
(Eq. 5), the double power law of Moster et al. 2010 applied to the
instantaneous rather than integrated efficiency, chosen because the
instantaneous efficiencies predicted by multi-epoch abundance matching
follow that shape at every redshift. Satellites follow "delayed-then-rapid"
quenching: after the halo passes its peak mass the SFR is held at its value
at t_peak for τ = t_dyn τ₀ (m*/10¹⁰ M_⊙)^(−τ_s) (Eq. 13), then set to zero.
Mergers send a fraction f_esc of satellite stars to the intracluster mass
(Eq. 15). Each observable set is chosen to constrain mostly one parameter
group: SMFs to z = 8 for M₀ and M_z, the cosmic SFR density to z = 11 for
ε₀ and ε_z, sSFRs for the slopes, the low-z massive SMF for f_esc, quenched
fractions to z = 4 for τ₀ and τ_s, small-scale w_p for the stripping
parameter f_s [src: Sect. 3.3].

### Step 3. Decide what happens to satellites and orphans
<!-- key: step-3-decide-what-happens-to-satellites-and -->

- **UniverseMachine.** A satellite survives until v_max/v_Mpeak falls below
  T_merge, which rises from T_merge,300 to T_merge,1000 as an error function
  of the host's log v_Mpeak centred at 2.75 (Eq. 20); disrupted stars merge
  into the central if the subhalo was last seen within f_merge R_vir,host,
  otherwise join the intrahalo light [src: arXiv:1806.07893, Sect. 3.3].
  Subhaloes lost by the finder before reaching T_merge are integrated in the
  host's NFW potential with a softened force, GM(<r)/(r + 0.1 R_vir)²
  (Eq. 32), leapfrog with 10 sub-steps per snapshot; no mass loss while
  infalling and ṁ = −1.18 (m/t_dyn)(m/M)^0.07 after pericentre (Eqs. 34–35);
  d log v_max/d log m = 0.3 − 0.4 m/(m + m_i) (Eq. 36); < 1% highly unbound
  satellites are removed [src: App. B.2].
- **EMERGE.** Orphans keep the orbit of the last snapshot and merge after a
  dynamical-friction time; their mean distance shrinks as √(1 − Δt/t_df)
  and they are placed randomly on a sphere of that radius [src:
  arXiv:1705.05373, Sect. 3.2.3].
- **SAMs.** Most keep galaxies whose subhalo was lost; teams freeze, integrate
  or tag a dark-matter particle for their positions, which nIFTy could not
  compare because particle data were not supplied [src: arXiv:1505.04607,
  Sect. 3.3].

### Step 4. Forward-model the observational errors
<!-- key: step-4-forward-model-the-observational-errors -->

UniverseMachine applies them to the model, not the data [src:
arXiv:1806.07893, Sect. 3.5]:

- a redshift-dependent offset between observed and true stellar mass, μ =
  μ₀ + μ_a(1 − a) (Eq. 25), with prior widths 0.14 and 0.24 dex, plus an
  SFR-only offset κ exp(−(z − 2)²/2) (Eq. 26), prior width 0.24 dex, for the
  tension between observed sSFRs and SMF evolution that peaks at z = 2
  [src: arXiv:1806.07893, Sect. 3.5];
- a mass- or sSFR-dependent offset is not used, because the tight SMF errors
  would make the sampler use it to fit the SMF shape ("overfitting") and the
  sSFR-dependent one is degenerate with sample variance;
- random stellar-mass errors σ_SM,obs = min(σ_SM,0 + σ_SM,z z, 0.3 dex)
  (Eq. 27) for Eddington bias; SFR scatter such that intrinsic plus
  observed main-sequence scatter is 0.3 dex (Eq. 28) [src: arXiv:1806.07893,
  Sect. 3.5];
- volume-weighting over each observable's redshift range (Eq. 29),
  redshift-space distortions from halo velocities, and 30 km/s of combined
  velocity bias and redshift error; PRIMUS grism redshifts with σ_z/(1 + z) =
  0.0033 [src: arXiv:1806.07893, Sect. 3.5];
- a universal Chabrier IMF, as in all the compared data.

### Step 5. Write the likelihood and sample
<!-- key: step-5-write-the-likelihood-and-sample -->

| Model | Data and likelihood | Search and sampler | Cost and convergence | Place read |
|---|---|---|---|---|
| UniverseMachine | SMFs, sSFRs, cosmic SFR, quenched fractions, UV luminosity functions, UV–stellar mass, IRX–UV, auto- and cross-correlations by star-formation class, central quenching vs environment; exp(−χ²/2) with covariances where available | hybrid adaptive-Metropolis and stretch-move MCMC, 100 walkers, ~500 000 steps; best fit by gradient descent from the mean of the last 400 steps | 400 000 CPU hours; chains run for 10 autocorrelation times; each walker spreads one model over 144 processors, ~1.5 CPU hours (36 s wall clock) per point; 1069 data points, 44 parameters, naive reduced χ² 0.36 | arXiv:1806.07893, Sect. 3.1, 4.1, App. F |
| EMERGE | log SMF, log cosmic SFR density, log sSFR, f_q, w_p; χ² = Δᵀ C⁻¹ Δ, diagonal C where no full matrix is published (Eqs. 17–21) | "Hybrid" optimiser (simulated annealing, MCMC and particle-swarm elements): 14 sets of 30 walkers × 2000 steps, all reaching the same minimum; then an affine-invariant ensemble sampler, 10 ensembles of 100 walkers started around the best fit | 11 free parameters in the final model (Table 6) | arXiv:1705.05373, Sect. 3.3–3.4 |

UniverseMachine convolves the mock analytically with the observational
errors and weights galaxies by their probability of entering each bin, to
reduce sampling noise in the χ² surface; this costs time per evaluation but
makes gradient-based best-fit searches and a Fisher-matrix starting guess
possible [src: arXiv:1806.07893, App. F].

### Step 6. Select the model
<!-- key: step-6-select-the-model -->

EMERGE compares six nested variants by information criteria and Bayesian
evidence [src: arXiv:1705.05373, App. A.3]: a redshift-dependent efficiency
(M_z, ε_z) beats a constant one by a log Bayes factor of 418; letting the
low-mass slope evolve gains 1.6; letting the high-mass slope evolve as well
loses 12.5 (penalised, no better fit); a stellar-mass-dependent quenching
time gains 75.8 over the same model without it, by fitting the quenched
fractions and small-scale clustering of low-mass galaxies.

### Step 7. Tune a SAM, or deliberately not
<!-- key: step-7-tune-a-sam-or-deliberately-not -->

Shark tunes its free parameters primarily to the stellar mass function and
keeps the stellar-to-halo relation, HI and H₂ mass functions and
metallicities out of the tuning so that they test the model [src:
arXiv:1807.11180, Sect. 5.2, 5.3, 5.6]. The choice of SMF propagates: tuned
to the Wright et al. 2017 SMF, Shark's centrals at M_halo ≈ 10¹⁵ M_⊙ are
1.4–8.5 times (16th–84th percentiles) more massive than in Moster et al.
2013, whose relation was calibrated on the steeper-ended Li & White 2009
SMF [src: Sect. 5.2]. nIFTy ran 14 models "as is" to show the importance of
calibration; the raw scatter in the SMF "reduces considerably" when each
model uses its preferred merger trees, halo mass definition and IMF [src:
arXiv:1505.04607, Sect. 3.4].

### Step 8. Extract a survey-like tracer and its HOD from a hydro run
<!-- key: step-8-extract-a-survey-like-tracer-and-its-hod -->

The TNG300 procedure for DESI-like galaxies (arXiv:2202.12911):

1. TNG300-1 (205 h⁻¹Mpc, 2500³ dark-matter particles and gas cells) and its
   dark-matter-only twin, at z = 0.8 [src: arXiv:2202.12911, Sect. 2.1].
2. Colours with FSPS (MILES library, MIST isochrones) from the star-formation
   history of star particles within 30 kpc, split at 30 Myr into a young part
   (nebular emission) and an old part (stellar continuum); dust optical depth
   τ_v = γ (Z_gas/Z_⊙)^α Σ̃*^β (Eq. 1) with (α, β, γ) = (−0.6, 0.2, 0.4)
   "roughly tuned" to z ~ 0 relations and not formally optimised [src:
   arXiv:2202.12911, Sect. 2.2].
3. The DESI LRG (Eqs. 2–3) and ELG (Eqs. 4–6) colour cuts on magnitudes
   shifted by δm, with δm chosen to reach the DESI target density of 5 ×
   10⁻⁴ h³Mpc⁻³: δm = −0.4 gives 4608 LRGs, δm = +0.6 gives 4998 ELGs [src:
   arXiv:2202.12911, Sects. 2.3.1–2.3.2].
4. Each galaxy's host matched to the dark-matter-only run through TNG's
   bijective subhalo map, by position and mass where it is missing; halo mass
   M_200c; centre at the potential minimum [src: Sect. 2.4].
5. Occupations, satellite counts, radial and velocity distributions measured
   per mass bin and compared to the baseline HOD forms [src: Sect. 3]. The
   halo velocity dispersion is approximated by that of the largest subhalo
   divided by 1.23, since that subhalo over-estimates it by (23 ± 3)% with no
   significant mass dependence on 800 test haloes [src: arXiv:2202.12911,
   Sect. 3.4].

Other suites, one line each:

- **FLAMINGO** (Contreras et al. 2024): 1906.8 h⁻¹Mpc box, 2 × 5040³
  particles (3.85 × 10⁹ and 7.29 × 10⁸ h⁻¹M_⊙ for dark matter and initial
  gas), partially fixed initial conditions; at z = 0.4 a BOSS-like
  incomplete red colour–magnitude selection (~3.16 × 10⁻⁴ h³Mpc⁻³) and a
  DESI BGS-like sample complete in M_r (10⁻³ h³Mpc⁻³); 681 h⁻¹Mpc boxes with
  other feedback variants for the BGS-like sample only [src:
  arXiv:2407.18912, Sects. 2.1–2.2].
- **Illustris and EAGLE** (Beltz-Mohrmann et al. 2020): two luminosity-
  threshold samples per run; a five-parameter HOD fitted to each hydro run
  and applied to its dark-matter-only twin; compared on w_p, ξ(s), group
  multiplicity and counts-in-cells [src: arXiv:1908.11448, abstract, Sect. 4
  headings].
- **EAGLE, SHAM** (Chaves-Montero et al. 2016): V_relax, the peak circular
  velocity while a relaxation criterion holds, correlates best with M_⋆
  [src: arXiv:1507.01948, abstract].
- **EAGLE, sizes** (Desmond et al. 2017): galaxy size correlates only
  weakly with halo mass, concentration and spin at fixed M_⋆ [src:
  arXiv:1612.01029, abstract].
- **Magneticum** (Ragagnin et al. 2021): HODEmu, a Gaussian-process
  emulator of the satellite N_s–M relation (normalisation A, slope β,
  scatter σ) over 15 cosmologies and 4 redshifts in 0 < z < 0.5 [src:
  arXiv:2110.05498, abstract].
- **MillenniumTNG** (Contreras et al. 2025): satellites matched between
  hydro and dark-matter-only runs through merger trees, giving position and
  velocity offsets versus mass and radius [src: arXiv:2512.04080,
  abstract].
- **SIMBA and TNG**: shuffling and environment-dependent HODs in
  `deep/assembly-bias.md` (arXiv:2511.01441).

### Step 9. Use an empirical-model mock to validate an HOD pipeline
<!-- key: step-9-use-an-empirical-model-mock-to-validate -->

The DESI DR1 full-scale analysis transfers the diffsky galaxy–halo model,
run on SMDPL, to the UNIT simulations with GalSampler, using halo mass and
concentration and a host-centric phase-space model; the LRG-like z = 0.5 mock
is observed in the distant-observer approximation along three axes, with a
jackknife covariance from 125 parts of each of two UNIT boxes; the pipeline
then fits it with AbacusSummit templates [src: arXiv:2512.15962, Sect.
III.4]. The outcome is in L2.

The point of the transfer is that the galaxy model is not the one being
fitted, so the test probes model misspecification [der: from the
construction just described].

On FLAMINGO, an emulator (GalaxyEmu-Planck) of a 13-parameter HOD and of
SHAMe is fitted to w_p, ξ_0,2 and ΔΣ (> 1 h⁻¹Mpc, to avoid baryonic
effects) and then predicts k-NN, counts-in-cylinders, void probability and
assembly-bias statistics: the HOD performs comparably on clustering and
lensing, SHAMe better on higher-order statistics, notably assembly bias,
and two HOD parameters can be dropped without loss [src: arXiv:2407.18912,
abstract, Sect. 3.3 headings]. SHAMe needs both assembly-bias parameters;
without them the predicted small-scale lensing is too high, "in the same
direction as the lensing-is-low signal" [src: Sect. 5]. FLAMINGO is also
the validation volume for a joint cluster-lensing, galaxy-clustering and
cross-correlation model, which improves the σ8–Ω_m figure of merit 15-fold
over clusters alone [src: arXiv:2601.16353, abstract].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Empirical model, SAM or hydrodynamical run
<!-- key: empirical-model-sam-or-hydrodynamical-run -->

The empirical models fit their parameters to data with a likelihood and
report posteriors (Step 5); the price is per-model cost (400 k CPU hours
for UniverseMachine, arXiv:1806.07893, Sect. 4.1) and phenomenological forms. SAMs carry physical
prescriptions but are tuned to a few targets, and the halo layer changes
their outputs at the tuning level (Step 7). Hydrodynamical runs give
correlated galaxy and gas properties in one volume, but in a single
cosmology and box: 205 h⁻¹Mpc for TNG300 (arXiv:2202.12911) [src:
Sect. 2.1], hence tracer samples of a few thousand galaxies, against
1906.8 h⁻¹Mpc for FLAMINGO (arXiv:2407.18912) [src: Sect. 2.1] (Step 8).

### Which hydrodynamical suite
<!-- key: which-hydrodynamical-suite -->

The suites disagree where feedback acts, so a result from one is not a
property of hydrodynamics:

- **Halo mass function.** Both Illustris and EAGLE shift haloes to lower
  masses, but differently: Illustris is below its dark-matter-only HMF
  above 10¹² h⁻¹M_⊙ and above it at lower masses, EAGLE below at all masses
  under 10¹⁴ h⁻¹M_⊙ [src: arXiv:1908.11448, Sect. 6]. A hydro-fitted HOD
  on the dark-matter-only twin therefore over-predicts n_g; after an HMF
  correction it reproduces all statistics for the bright sample, while the
  faint sample also needs spatial, velocity and assembly-bias terms [src:
  abstract].
- **Satellite abundance.** The N_s–M normalisation and slope depend
  weakly on Ω_m and Ω_b, which "can explain some discrepancies" between
  the satellite HODs of Magneticum, Illustris and BAHAMAS; the dependence
  differs between full-physics, dark-matter-only and non-radiative runs
  [src: arXiv:2110.05498, abstract].
- **Assembly bias.** ~10% at z = 0 in TNG, nearly zero in SIMBA (see
  `deep/assembly-bias.md`); TNG and the Santa Cruz SAM agree on two-point
  clustering and assembly-bias signatures but differ in low-mass occupancy
  and in a TNG gas–environment correlation absent from the SAM [src:
  arXiv:2108.00006, abstract]. In EAGLE assembly bias changes clustering
  by 20% and a V_relax SHAM captures it to within 15% [src:
  arXiv:1507.01948, abstract].
- **Baryons against selection.** In MTNG, hydro satellites sit 3–4% closer
  to halo centres and move more slowly than in the dark-matter-only run,
  changing clustering by 10–20% at 0.1 h⁻¹Mpc (1–3σ at DESI-like errors);
  this is smaller than the change from galaxy selection [src:
  arXiv:2512.04080, abstract].
- **Environment.** In FLAMINGO the HMF, halo bias, SHMR, CSMF and c–M
  relation depend on environment; ignoring it biases the SHMR and f_sat in
  density-split lensing HOD fits [src: arXiv:2610.23997, abstract].

### Which halo property
<!-- key: which-halo-property -->

UniverseMachine uses v_Mpeak for potential-well depth and Δv_max for
assembly (reasons in Step 2). EMERGE uses halo mass and growth rate with a
time-since-peak-mass satellite rule; UniverseMachine states that such
time-since-accretion schemes "cannot capture orbit-dependent effects" [src:
arXiv:1806.07893, Sect. 3.1].

### Orphans: kept, and how many
<!-- key: orphans-kept-and-how-many -->

Orphans fix the resolution loss of subhaloes but can overshoot. In
UniverseMachine clusters found with a mock redMaPPer finder, the orphan
fraction falls from ~60% at projected separations 0.1–0.3 h⁻¹Mpc to ~20% at
0.7–0.9 h⁻¹Mpc; it is marginally consistent with weak-lensing upper limits
from satellites of SDSS redMaPPer clusters within 0.3 h⁻¹Mpc and
"substantially" violates them beyond [src: arXiv:2312.04847, Abstract,
Sect. 5]. The authors attribute it to premature loss of Rockstar subhaloes
and the orbit-independent average mass loss, and suggest using satellite
lensing as a constraint in the fit [src: Sect. 5]. In nIFTy the model-to-
model spread in galaxies per halo above 10¹³ h⁻¹M_⊙ is about an order of
magnitude and comes mainly from the treatment of orphans, though non-orphan
differences remain [src: arXiv:1505.04607, Sect. 6.4].

### Colour-cut or stellar-mass selection in a hydro run
<!-- key: colour-cut-or-stellar-mass-selection-in-a-hydro -->

At the DESI LRG density, a stellar-mass-ranked sample "recovers largely the
same properties" as the colour-selected one: α_c ≈ 0.15, α_s ≈ 1, radial
bias toward large radii in low-mass haloes (attributed to FoF
over-linking); its centrals prefer high-concentration haloes more weakly,
because mass selection admits more star-forming galaxies [src:
arXiv:2202.12911, Sect. 4.1].

### What hydro runs say about the HOD assumptions
<!-- key: what-hydro-runs-say-about-the-hod-assumptions -->

- Velocity bias of DESI-like LRGs in TNG300: α_c = 0.137 ± 0.007, α_s =
  0.92 ± 0.05 with α_s = 0.8, 0.9, 1.05 in three rising mass bins; both
  within ~1σ of BOSS LRG fits [src: arXiv:2202.12911, Sect. 3.4]. ELG
  centrals ~0.15 [src: Fig. 10 caption].
- Satellite occupation: mean equals variance for LRGs across all masses
  (Poisson); for ELGs a hint of super-Poisson at the highest masses, not
  significant [src: Sect. 3.2]. Compare the sub-Poisson preference of
  KiDS-1000 data in `systematics.md#occupation-statistics-and-the-central-condition`.
- Baseline forms reproduce the measured TNG occupations "reasonably well",
  e.g. log M_cut = 12.7, log M_1 = 13.6, σ = 0.2, α = 1.15, κ = 0.08, f_ic =
  0.8 for LRGs (a curve chosen by eye, not a fit) [src: arXiv:2202.12911,
  Fig. 2 caption, Sect. 3.1].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Halo layer | Bolshoi-Planck 250 h⁻¹Mpc, 2048³, 1.6 × 10⁸ h⁻¹M_⊙, 180 snapshots; Rockstar + Consistent Trees | UniverseMachine | arXiv:1806.07893 | Sect. 2.1 |
| Fit size | 1069 data points, 44 parameters, reduced χ² 0.36 | UniverseMachine | arXiv:1806.07893 | Sect. 4.1 |
| Sampling | 100 walkers, ~5 × 10⁵ steps, 4 × 10⁵ CPU h, 10 autocorrelation times | UniverseMachine | arXiv:1806.07893 | Sect. 4.1 |
| Quenched population | median sSFR 10⁻¹¹·⁸ yr⁻¹, scatter 0.36 dex (fixed) | UniverseMachine | arXiv:1806.07893 | Sect. 3.2 |
| Star-forming scatter cap | 0.3 dex | UniverseMachine | arXiv:1806.07893 | Eq. 3 |
| Stellar-mass offset priors | 0.14 (μ₀), 0.24 (μ_a, κ) dex | UniverseMachine | arXiv:1806.07893 | Sect. 3.5 |
| Redshift error + velocity bias | 30 km/s | UniverseMachine | arXiv:1806.07893 | Sect. 3.5 |
| Orphan force softening | 0.1 R_vir; 10 sub-steps per snapshot | UniverseMachine | arXiv:1806.07893 | App. B.2 |
| Orphan fraction in clusters | ~60% (0.1–0.3) to ~20% (0.7–0.9 h⁻¹Mpc) | UniverseMachine, mock redMaPPer | arXiv:2312.04847 | Sect. 5 |
| Optimiser | 14 × 30 walkers × 2000 steps; then 10 × 100 walkers | EMERGE | arXiv:1705.05373 | Sect. 3.4 |
| Log Bayes factors | 418 (model 2 vs 1), 1.6 (3 vs 2), 12.5 (3 vs 4), 75.8 (5 vs 3) | EMERGE | arXiv:1705.05373 | App. A.3 |
| Final parameters | 11, e.g. f_esc = 0.388, τ₀ = 4.282, τ_s = 0.363 | EMERGE | arXiv:1705.05373 | Table 6 |
| SAM comparison box | 62.5 h⁻¹Mpc, 270³, 20-particle minimum, 5 mass definitions | nIFTy | arXiv:1505.04607 | Sect. 2 |
| Central mass at 10¹⁵ M_⊙ vs Moster 2013 | 1.4–8.5 times higher | Shark | arXiv:1807.11180 | Sect. 5.2 |
| DESI-like tracer counts | 4608 LRGs (δm = −0.4), 4998 ELGs (δm = +0.6) at 5 × 10⁻⁴ h³Mpc⁻³ | TNG300, z = 0.8 | arXiv:2202.12911 | Sect. 2.3 |
| Dust parameters | (α, β, γ) = (−0.6, 0.2, 0.4) | TNG300 colours | arXiv:2202.12911 | Sect. 2.2 |
| Subhalo-dispersion correction | divide by 1.23 ((23 ± 3)% over-estimate) | TNG300 | arXiv:2202.12911 | Sect. 3.4 |
| LRG velocity bias | α_c = 0.137 ± 0.007; α_s = 0.92 ± 0.05 | TNG300 | arXiv:2202.12911 | Sect. 3.4 |
| Validation mock covariance | 125 jackknife parts × 2 UNIT boxes | DESI DR1 | arXiv:2512.15962 | Sect. III.4 |
| Hydro box | 1906.8 h⁻¹Mpc, 2 × 5040³, m_DM 3.85 × 10⁹ h⁻¹M_⊙ | FLAMINGO | arXiv:2407.18912 | Sect. 2.1 |
| Survey-like densities | BOSS-like ~3.16 × 10⁻⁴, BGS-like 10⁻³ h³Mpc⁻³ at z = 0.4 | FLAMINGO | arXiv:2407.18912 | Sect. 2.2 |
| HOD complexity | 13 parameters; 2 removable without loss | FLAMINGO validation | arXiv:2407.18912 | abstract |
| Satellite offsets | 3–4% closer; 10–20% in clustering at 0.1 h⁻¹Mpc | MTNG | arXiv:2512.04080 | abstract |
| SHAM in EAGLE | 30% too much clustering < 2 Mpc at 8.77 < log M_⋆ < 9.77; assembly bias 20%, captured to 15% | EAGLE | arXiv:1507.01948 | abstract |
| Satellite emulator | 15 cosmologies × 4 redshifts | Magneticum | arXiv:2110.05498 | abstract |
| Joint cluster + galaxy model | figure of merit × 15 | FLAMINGO | arXiv:2601.16353 | abstract |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Orphan excess.** An empirical model can fit SMFs and clustering while
  over-predicting orphans in cluster outskirts [src: arXiv:2312.04847, Sect.
  5]. Test: compare the model's orphan fraction versus projected radius, after
  running the same cluster finder, with satellite-lensing limits.
- **Halo layer changed under a tuned model.** SAM outputs scatter widely when
  run on trees and mass definitions they were not tuned on [src:
  arXiv:1505.04607, Sect. 3.4]. Test: rerun with the model's preferred mass
  definition and IMF before comparing; retune when the halo layer changes.
- **Systematic offsets absorbing shape.** A free mass-dependent stellar-mass
  offset lets the fit chase the SMF shape [src: arXiv:1806.07893, Sect.
  3.5]. Test: keep offsets redshift-dependent only, with priors from
  population-synthesis studies, as UniverseMachine does.
- **Noisy χ² from stochastic mocks.** One random realisation per call makes
  the χ² surface noisy [src: arXiv:1806.07893, App. F]. Remedy: analytic
  convolution with observational errors and probability-weighted bins.
- **Calibration targets reused as tests.** Shark lists which observables
  were and were not used in tuning [src: arXiv:1807.11180, Sect. 5]. Test:
  check that a claimed success is on an untuned observable.
- **Tracer selection by mass instead of colour.** Changes the central
  assembly-bias signal (weaker concentration preference) though not the
  velocity bias [src: arXiv:2202.12911, Sect. 4.1]. Test: repeat with
  colour cuts at the survey density.
- **Approximate halo velocity dispersion.** Using the largest subhalo's
  dispersion biases α_c and α_s by 23% unless corrected [src:
  arXiv:2202.12911, Sect. 3.4].
- **Untuned dust in mock colours.** The TNG dust model was only roughly
  tuned [src: arXiv:2202.12911, Sect. 2.2]; selections near colour
  boundaries inherit it [der].
- **One suite taken as "the" hydro answer.** Illustris and EAGLE change
  the HMF differently [src: arXiv:1908.11448, Sect. 6]; SIMBA and TNG
  disagree on assembly bias at z = 0 (arXiv:2511.01441). Test: repeat on a
  second suite, or on feedback variants of one (FLAMINGO's 681 h⁻¹Mpc
  boxes, arXiv:2407.18912, Sect. 2.1).
- **Hydro-fitted HOD on a dark-matter-only HMF.** Over-predicts the number
  density unless the HMF is corrected [src: arXiv:1908.11448, abstract].
- **Validation on one mock.** The DESI DR1 test used a single LRG-like
  sample and calls for more, notably for BGS [src: arXiv:2512.15962, Sect.
  III.4].

## Reading list
<!-- key: reading-list -->

- Method, empirical: Behroozi et al. 2019, arXiv:1806.07893 — UniverseMachine
  parameterisation, observational-systematics model, orphan tracking,
  sampler and cost.
- Method, empirical: Moster et al. 2018, arXiv:1705.05373 — EMERGE
  efficiency, satellite quenching, Hybrid optimiser, Bayes-factor model
  selection.
- Critique: Kumar et al. 2023, arXiv:2312.04847 — orphan over-abundance
  in UniverseMachine against satellite lensing.
- Comparison: Knebe et al. 2015, arXiv:1505.04607 — 14 models (abstract)
  on one halo layer without retuning; orphans drive the occupation spread.
- Method, SAM: Lagos et al. 2018, arXiv:1807.11180 — what Shark tunes and
  what it keeps as tests.
- Application, hydro: Yuan et al. 2022, arXiv:2202.12911 — DESI-like
  colour selection in TNG300, HOD, Poisson test, velocity bias.
- Comparison, hydro: Beltz-Mohrmann et al. 2020, arXiv:1908.11448 — HOD
  fitted in Illustris and EAGLE, transferred to their dark-matter twins.
- Validation, hydro: Contreras et al. 2024, arXiv:2407.18912 — FLAMINGO
  BOSS- and BGS-like samples, HOD against SHAMe on higher-order statistics.
- Application, hydro: Chaves-Montero et al. 2016, arXiv:1507.01948 (EAGLE
  SHAM); Desmond et al. 2017, arXiv:1612.01029 (EAGLE sizes); Ragagnin et
  al. 2021, arXiv:2110.05498 (Magneticum satellites); Contreras et al.
  2025, arXiv:2512.04080 (MTNG satellites); Martín Girardi et al. 2026,
  arXiv:2610.23997 (FLAMINGO environment); Cao et al. 2026,
  arXiv:2601.16353 (FLAMINGO clusters + galaxies).
- Comparison, hydro vs SAM: Hadzhiyska et al. 2021, arXiv:2108.00006.
- Application, validation: Lange et al. 2025, arXiv:2512.15962 — GalSampler
  transfer of an empirical model as a misspecification test.
- Review: Somerville & Davé 2015, arXiv:1412.2712; Crain & van de Voort
  2023, arXiv:2309.17075 (see L2).

## Not verified
<!-- key: not-verified -->

- Henriques et al. 2015 (arXiv:1410.0365) has no HTML rendering: its MCMC
  calibration of the Munich SAM was not read.
- Diffsky, GalSampler (Hearin et al. 2020), the TNG colour model of
  Hadzhiyska et al. 2021 and the UniverseMachine DR1 high-z predictions were
  not read.
- A date-sorted arXiv search for 2025–2026 empirical-model papers was
  rate-limited; an INSPIRE query returned no 2025–2026 empirical
  galaxy–halo model paper beyond those listed, so newer models may exist.
- The hydro-suite additions of 2026-10-21 rest on abstracts, except
  arXiv:2407.18912 (Sects. 2.1, 2.2, 5) and arXiv:1908.11448 (Sect. 6).
  No galaxy–halo connection paper on Astrid was found by abstract search.
- The EMERGE box side lengths come from figure captions, not from the
  simulation section, which was cut by the rendering.
