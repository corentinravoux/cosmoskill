# Abundance matching and SHMR fitting — cosmo-galaxy-halo-connection dossier

Scope: how a subhalo abundance-matching (SHAM) catalogue or a parametric
stellar-to-halo mass relation (SHMR) is built and fitted (choice and epoch
of the halo property, stellar mass function input, how scatter is
injected, satellites, disruption and orphans, assembly-bias extensions,
nuisance parameters and priors), what each choice was found to cost, and
how SHMRs from lensing, abundance matching and clustering compare.
Snapshot: 2026-10-21.
From: Wechsler & Tinker 2018, Sect. 2.2.1–2.2.2, 4–6; DES, HSC, COSMOS and
DESI BGS galaxy-evolution groups.

Already in L2, not repeated here: the principle and history (Vale &
Ostriker, Conroy, Behroozi 2010), the Reddick and Lehmann conclusions in one
line each, multi-epoch matching, the DES Y3 SHMR formula and the COSMOS
joint analysis in
`physics-and-methods.md#abundance-matching-and-the-stellar-to-halo-mass`;
SHMR values by survey in `results.md#stellar-to-halo-mass-relation`;
stellar-mass systematics, the scatter–slope degeneracy and how scatter is
constrained in `systematics.md#stellar-mass-and-luminosity-estimates` and
`systematics.md#scatter-slope-degeneracy`; subhalo disruption in N-body runs
(van den Bosch 2017) in
`systematics.md#satellite-distribution-velocity-bias-and-orphans`; SHAMe in
lensing fits in `physics-and-methods.md#galaxy-galaxy-lensing-with-clustering`;
the SHMR ends in `open-questions.md#the-shmr-at-the-ends`.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Choose the halo property and the epoch it is read at
<!-- key: step-1-choose-the-halo-property-and-the-epoch -->

The rank-order assignment itself is n^gal = ℛ(M*), n^halo = ℛ(𝓜), each
galaxy going to the (sub)halo of equal rank, ℛ returning ordinal ranks
(Campbell et al. 2018, arXiv:1705.06347, Eq. 2) [src: Sect. 2.1.1]. The
choice is in 𝓜. Reddick et al. 2013 test eight [src: arXiv:1207.2160,
Sect. III.2]:

| Property | Definition | What it does to satellites |
|---|---|---|
| M_0 | present mass, bound particles for subhaloes | under-estimates satellite stellar masses, because dark matter is stripped faster than stars |
| M_acc | mass when crossing the host virial radius | boosts satellites relative to centrals of equal M_0 |
| M_peak | maximum mass over the history | larger than M_acc for subhaloes stripped before infall, which starts at ~3 R_vir (Behroozi et al. 2012, as cited) |
| M_0,peak | M_0 for hosts, M_peak for subhaloes | — |
| v_max, v_acc, v_peak, v_0,peak | the same for the maximum circular velocity | v_0,peak gives the most massive satellites and the highest f_sat |

Reason given for peak or infall quantities: galaxy properties should track
potential depth, and the galaxy should keep the mass it had before
stripping [src: Sect. III.2]. At fixed M_peak, subhaloes have v_peak up to
~7% higher than hosts, attributed either to preferential disruption of
low-concentration subhaloes or to halo assembly bias; a lower-resolution
run gives the same offset [src: Sect. III.2, Fig. 2].

Interpolated proxy (Lehmann et al. 2017): v_α ≡ v_vir (v_max/v_vir)^α
(arXiv:1510.05651, Eq. 1), v_vir = (G M_vir/R_vir)^½ ∝ M_vir^⅓ (Eq. 2), so
log v_α = α log v_max + (1 − α) log v_vir (Eq. 3). v_max/v_vir is a
concentration proxy: α = 0 ranks by mass, α = 1 by v_max, and a larger α
selects more low-mass, high-concentration haloes and more subhaloes [src:
Sect. III.1]. It is evaluated at the epoch of peak mass, giving v̂_α;
reason: v_peak is "commonly set by major mergers" and haloes at their
largest circular velocities may be out of equilibrium; the rank orders by
v_peak and v_max(a_mpeak) are very similar [src: Sect. III.2]. In EAGLE
the property correlating most strongly with stellar mass is V_relax, the
highest circular velocity reached while a relaxation criterion holds
(Chaves-Montero et al. 2016, arXiv:1507.01948) [src].

### Step 2. Choose the stellar mass function that is matched
<!-- key: step-2-choose-the-stellar-mass-function-that-is -->

Reddick et al. match to the exact stellar mass function of the
volume-limited sample rather than a literature fit, "for consistency with
the group catalog", because conditional mass functions are sensitive to
this input [src: arXiv:1207.2160, Sect. III.2]. The SHMR codes fit the
SMF with explicit nuisance terms: log₁₀(M*,meas/M*,true) = μ + κ
log₁₀(M*,true/M_0), M_0 = 10^11.3 M_⊙ (Behroozi et al. 2010,
arXiv:1001.0015, Eq. 1), μ Gaussian with 0.25 dex width (SPS ≈ 0.1, dust ≈
0.1, star-formation history ≈ 0.2 dex, κ term ≤ 0.1 dex, in quadrature), κ
Gaussian of width 0.10 about 0 [src: Sect. III.1.1]. Higher-order error
models were rejected because no priors exist for them and loose priors
would fit "bumps and wiggles" from statistical and sample-variance errors
[src: same].

### Step 3. Inject scatter
<!-- key: step-3-inject-scatter -->

Observed SMF = intrinsic SMF ∘ P_s ∘ P, with P_s the scatter of M* at fixed
halo mass and P the measurement error at fixed true M* (arXiv:1001.0015,
Eq. 17). Three implementations:

1. **Iterative deconvolution** (Behroozi et al. 2010, as used by Reddick):
   match with zero scatter, add log-normal scatter, re-estimate the
   intrinsic SMF from the difference between observed and scattered SMFs,
   repeat until the scattered output matches the observed SMF. It cannot
   keep the SMF steep above the characteristic mass for very large
   scatter; Reddick et al. judge this harmless because scatter above ~0.3
   dex is excluded for massive galaxies [src: arXiv:1207.2160, Sect.
   III.2, Fig. 3].
2. **Noisy re-ranking**: add scatter to the stellar masses, re-rank, iterate
   to the desired scatter (Hearin et al. 2013, as cited) [src:
   arXiv:1705.06347, Sect. 2.1.1].
3. **Draw from a predetermined list** so the SMF is reproduced exactly
   (Trujillo-Gomez et al. 2011, as cited); the scatter is then not
   log-normal and is skewed in large haloes [src: arXiv:1207.2160, Sect.
   III.2].

Direct deconvolution was not used by Behroozi et al. to compute
uncertainties, for four stated reasons: it amplifies statistical bumps,
depends on how the SMF is extrapolated beyond the data, becomes harder when
the error kernel varies with redshift, and returns only a
redshift-averaged relation [src: arXiv:1001.0015, Sect. III.4.2]. Reddick
et al. include no stellar-mass measurement error, so their scatter is the
sum of intrinsic and measurement scatter [src: arXiv:1207.2160, Sect.
III.2]. Campbell et al. add no scatter, since it mainly lowers clustering
above M* = 10¹¹ h⁻²M_⊙ [src: arXiv:1705.06347, Sect. 2.1.1].

### Step 4. Decide what happens to satellites
<!-- key: step-4-decide-what-happens-to-satellites -->

| Prescription | Rule | Analysis | Place read |
|---|---|---|---|
| Accretion mass, current SMF | subhaloes matched on M_acc to today's SMF, so satellites keep growing like centrals of their M_acc | Behroozi 2010 fiducial | arXiv:1001.0015, Sect. III.3.2 |
| Frozen at infall | M* = m(M_inf, z_inf) for subhaloes (Eq. 9): no stripping, no star formation after infall | Moster 2013 MEAM | arXiv:1205.5807, Sect. 3.2 |
| Disruption cut | galaxy removed when M_0 < μ_cut M_peak; μ_cut = 0–0.15 explored; 0.1 removes ~4% of subhaloes | Reddick 2013 | arXiv:1207.2160, Sect. III.2 |
| Disruption cut | M_sub < f_s M_peak (after Moster et al. 2018), because V_peak never decreases while stellar mass can be stripped | SHAMe | arXiv:2012.06596, Sect. 3.2, Eq. 2 |
| Orphans | most-bound particle of a lost subhalo tracked until t_dyn = 1.17 t_merge d_host² V_host (M_host/10¹³ h⁻¹M_⊙)^½ / [G ln(M_host/M_sub + 1) M_sub], t_merge free; the mass factor added to fit satellite numbers in massive haloes | SHAMe | arXiv:2012.06596, Sect. 3.1, Eq. 1 |

### Step 5. Optionally add assembly bias
<!-- key: step-5-optionally-add-assembly-bias -->

- Through the proxy: α of v̂_α sets the concentration dependence and so the
  assembly bias of the catalogue [src: arXiv:1510.05651, Sect. III.5,
  III.1].
- Through the scatter: SHAMe correlates the scatter at fixed V_peak with
  each subhalo's large-scale bias (Paranjape et al. 2018 estimator, as
  cited), separately for centrals (A_c) and satellites (A_s), each in [−1,
  1], conserving the satellite fraction at all densities; maximum and
  minimum settings differ by about a factor three in large-scale
  clustering (Contreras et al. 2020a, Fig. 8, as cited) [src:
  arXiv:2012.06596, Sect. 4].

### Step 6. Fit
<!-- key: step-6-fit -->

- **Grid over (scatter, μ_cut), mocks through the observational pipeline.**
  At every grid point the abundance-matched snapshot is turned into a light-cone, fibre
  collisions are added and the group finder is run, so the conditional SMF
  is compared like for like; 25 realisations per point give a shot-noise
  variance added to the covariance diagonal; observables are averaged over
  the nine neighbouring grid points to smooth outliers; the log M* > 9.8
  threshold and one CSMF host-mass bin [12.6, 12.9] are excluded [src:
  arXiv:1207.2160, Sects. III.2, VI.1].
- **Several thresholds combined.** Lehmann et al. treat the four luminosity
  thresholds as independent, an approximation they state and judge small
  [src: arXiv:1510.05651, Sect. IV.2].
- **SMF only, many epochs.** MEAM populates all haloes and subhaloes at
  every redshift with an SMF, with parameters log M_1(z) and N(z) quadratic
  in z and β(z), γ(z) power laws in (1 + z) (arXiv:1205.5807, Eqs. 5–8);
  likelihood ℒ = exp(−χ²_r) with χ²_r the bin-averaged and then
  redshift-averaged squared deviation of log Φ (Eqs. 4, 10) [src: Sects.
  3.1–3.2]. This normalisation differs from exp(−χ²/2) summed over bins
  and changes the width of the posterior [der: from Eqs. 4 and 10].
- **Parametric SHMR inside an HOD, with lensing.** DES Y3 writes the central
  occupation of a stellar-mass threshold as ⟨N_c⟩ = (f_cen/2)[1 +
  erf((log f_SHMR(M_h) − log M*^t)/σ_log M*)] (arXiv:2506.22367, Eq. 2),
  bins as differences of thresholds (Eqs. 3–4), satellites f_sat [(M_h −
  κM_min)/M_sat]^α_sat exp(−M_cut/M_h) with M_sat and M_cut power laws of
  M_min ≡ f_SHMR⁻¹(M*^t) (Eqs. 5–7), Poisson satellites (Eq. 9), and samples
  with MultiNest on a Hartlap-corrected Gaussian likelihood (Eq. 44) [src:
  Sects. 2.2, 6]. σ_log M* converts to halo-mass scatter by σ_log M* /
  σ_log M_h = d log M*/d log M_h [src: Sect. 2.2].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### V_peak or M_peak
<!-- key: vpeak-or-mpeak -->

- **SDSS groups + clustering.** Only v_peak fits the conditional SMF and
  w_p together; best fit μ_cut = 0.03 and 0.20 dex scatter; clustering, the
  central CSMF and the satellite CSMF each require scatter < 0.25 dex
  [src: arXiv:1207.2160, Sect. VI.1, Fig. 8].
- **Interpolation.** Combining four SDSS thresholds on DarkSky-400, α =
  0.57 (+0.20, −0.27) and scatter 0.17 (+0.03, −0.05) dex; α = 0 (M_peak-
  like), α = 1 (v_peak-like) and zero scatter are each excluded at p <
  0.001; the v̂_1.0 model with 0.22 dex gives χ²/dof = 8.9, 2.5, 1.9, 1.8 for
  M_r < −20.5, −21, −21.5, −22 [src: arXiv:1510.05651, Sect. IV.2, Fig. 9].
  Four 250 h⁻¹Mpc boxes with different cosmologies, codes and initial
  conditions give overlapping p = 0.05 contours [src: Sect. IV.3].
- **The crisis.** M_peak-based models under-predict clustering below 1
  h⁻¹Mpc because they make too few satellites: rank-order v_peak gives f_sat
  approaching ~30% at 10^9.5 h⁻²M_⊙, the mass-based models stay below ~24%,
  and small-scale clustering tracks f_sat nearly one to one [src:
  arXiv:1705.06347, Sect. 4.1]. Yet the M_peak model's f_sat agrees with an
  SDSS group catalogue, and a non-evolving M*–V_peak relation forms
  galaxies too early; no published SHAM fits z = 0 w_p, the evolving SMF
  and uses only extant subhaloes [src: Sects. 4.1, 9].
- **Hydro test.** In EAGLE, SHAM on V_relax recovers real-space clustering
  within errors above 2 Mpc for 8.77 < log M* < 10.77, over-predicts it by
  30% below 2 Mpc for the lowest mass bin through too many satellites in
  massive haloes, and recovers redshift-space clustering at all masses and
  separations; assembly bias changes EAGLE clustering by 20%, captured by
  V_relax to within 15% [src: arXiv:1507.01948, abstract]. In TNG300 the
  mean M*–V_peak relation is almost identical for centrals and satellites,
  while M_peak shows a larger central–satellite difference [src:
  arXiv:2012.06596, Sect. 2.3].

### Orphans, disruption or resolution
<!-- key: orphans-disruption-or-resolution -->

- **Resolution sets the satellite count.** SHAM on TNG300-1-Dark matches the
  densest TNG sample but over-predicts clustering at lower densities;
  TNG300-3-Dark matches the sparsest but under-predicts the densest; the
  errors reach large scales in the quadrupole and hexadecapole [src:
  arXiv:2012.06596, Sect. 2.3]. With orphans and disruption, SHAMe
  reproduces w_p and ξ_0,2,4 of TNG300 stellar-mass samples at n = 10⁻²,
  3.16 × 10⁻³ and 10⁻³ h³Mpc⁻³ on a simulation of 64 times lower
  resolution, and the HOD, assembly bias and kNN-CDFs that were not fitted
  agree "almost perfectly" [src: Sect. 8].
- **Lower-resolution runs lose v_peak satellites first.** The same model on
  Consuelo (8 h⁻¹kpc softening) and Esmeralda (15 h⁻¹kpc) loses satellites
  with M* > 10.5 against Bolshoi (1 h⁻¹kpc), lowering f_sat and small-scale
  clustering [src: arXiv:1207.2160, App. B].
- **Two readings of missing subhaloes.** Campbell et al. find "no empirical
  evidence of sufficiently massive missing sub-haloes" at Bolshoi
  resolution (m_p = 1.35 × 10⁸ h⁻¹M_⊙) and call the motivation for orphans
  "lacking" [src: arXiv:1705.06347, Sect. 9], whereas van den Bosch 2017
  attributes ~80% of Bolshoi subhalo disruption to numerics (L2,
  `systematics.md#satellite-distribution-velocity-bias-and-orphans`). The
  orphan profile matters: orphans on the dark-matter profile cluster more
  than orphans on the subhalo profile [src: arXiv:1705.06347, Fig. 12].

### Scatter implementation
<!-- key: scatter-implementation -->

Deconvolution keeps a log-normal scatter but fails for broad scatter at the
steep end; list-drawing reproduces the SMF exactly with a skewed scatter;
"it is not yet clear whether these alternatives can be distinguished by
existing data" [src: arXiv:1207.2160, Sect. III.2]. Ignoring scatter at
fixed halo mass over-predicts M* in 10^14.25 M_⊙ haloes by 0.13–0.19 dex;
ignoring measurement scatter adds 0.12 dex at z = 1 [src: arXiv:1001.0015,
Sect. IV.3.7].

### Functional form of the SHMR
<!-- key: functional-form-of-the-shmr -->

Behroozi et al. reject power laws at the high-mass end: the fitted slope
depends on the survey's number-density limit, creating artificial
redshift evolution, and averages over a slope that keeps increasing, so it
under-estimates M_h at high M* [src: arXiv:1001.0015, Sect. III.4.3]. Their
inverse form is log₁₀M_h(M*) = log₁₀M_1 + β log₁₀(M*/M*,0) +
(M*/M*,0)^δ / [1 + (M*/M*,0)^(−γ)] − ½ (Eq. 21), with typical z = 0 values δ
= 0.5–0.6 and γ = 1.3–1.7, and each parameter linear in scale factor (Eq.
22) [src]. The total systematic budget is dominated by stellar-mass
offsets, ~0.25 dex at all redshifts, against 0.02–0.12 dex (z = 0) and
0.07–0.16 dex (z = 1) for all other sources together [src: Sect. IV.3.7].
DES Y3 instead embeds the Kravtsov et al. 2018 form (L2) in an HOD, with
SHMR priors "informed by Kravtsov et al. (2018)" [src: arXiv:2506.22367,
Sect. 6].

### SHAM or SHMR-in-HOD
<!-- key: sham-or-shmr-in-hod -->

SHAM predicts satellite numbers and positions from the simulation, so
f_sat is an output and depends on resolution, the property and the orphan
model (sections above). An SHMR-in-HOD frees them: DES Y3 decouples the
satellite HOD from the central one through (B_sat, β_sat, B_cut, β_cut) "to
give the model additional freedom in order to fit the more complex data"
[src: arXiv:2506.22367, Sect. 2.2]. Group-catalogue and HOD satellite
fractions of DESI BGS disagree (L2, `results.md#satellites`), so the two
routes do not give the same f_sat on the same data.

## SHMRs from lensing, abundance matching and clustering compared
<!-- key: shmrs-from-lensing-abundance-matching-and -->

- **Where they agree.** Abundance matching, HOD, CLF, X-ray clusters and
  lensing-plus-clustering models show "remarkable consistency on the general
  outlines" of the local SHMR [src: arXiv:1804.03097, Sect. 6.1]. COSMOS
  lensing + clustering + SMF agrees broadly with matching and satellite
  kinematics, and Behroozi-style matching on its SMFs recovers its pivot
  masses, with "subtle differences" unexplained [src: arXiv:1104.0928,
  Sects. V.4, V.5.5]. DES Y3 (w(θ) + γ_t) agrees with the Behroozi 2013 and
  Moster 2013 matching at low mass and with the SDSS lensing + clustering
  iHOD [src: arXiv:2506.22367, Sect. 7.1.1].
- **Where they differ, and why.** Above log M_h^cen ≳ 12 DES Y3 is in
  tension with that matching and agrees with Kravtsov et al. [src: same],
  who find earlier SHMRs underestimate BCG masses by ~2–4 because SDSS
  photometry misses outer profiles; with improved photometry matching
  agrees with M*,BCG ∝ M₅₀₀^(0.34 ± 0.11) [src: arXiv:1401.7329, Sect.
  III.1]. The review names massive-end stellar masses (sky subtraction
  first, then outer profiles, ICL, IMF) as the largest discrepancy between
  methods [src: arXiv:1804.03097, Sects. 6.1, 6.5.1]. HSC lensing finds M_h
  varying by up to 0.4 dex at fixed total M*, with the inner 10 kpc mass:
  one SHMR is incomplete there [src: arXiv:1811.01139].
- **Scatter.** Abundance alone cannot fix it: BOSS bias 0.18 dex (log M_h =
  12.7–13.7), SDSS clustering + lensing 0.22 (+0.02/−0.01) at 10¹² and
  0.18 ± 0.01 at 10¹⁴ M_⊙, groups with SHAM mocks 0.20 ± 0.02, X-ray
  clusters 0.17 (14–15), all including measurement scatter [sec:
  arXiv:1804.03097, Sect. 6.2; 0.17 also in arXiv:1401.7329, Sect. III.1].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Best SHAM | v_peak, μ_cut = 0.03, scatter 0.20 dex | SDSS DR7, Bolshoi | arXiv:1207.2160 | Sect. VI.1 |
| Scatter bound | < 0.25 dex from each of w_p, central and satellite CSMF | SDSS DR7 | arXiv:1207.2160 | Sect. VI.1 |
| μ_cut | 0.1 removes ~4% of subhaloes | Bolshoi | arXiv:1207.2160 | Sect. III.2 |
| Realisations per grid point | 25 | SDSS DR7 | arXiv:1207.2160 | Sect. VI.1 |
| v_peak offset | subhaloes up to ~7% above hosts at fixed M_peak | Bolshoi | arXiv:1207.2160 | Sect. III.2 |
| Interpolation | α = 0.57 (+0.20, −0.27); scatter 0.17 (+0.03, −0.05) dex | SDSS, DarkSky-400 | arXiv:1510.05651 | Sect. IV.2 |
| v_max-only χ²/dof | 8.9, 2.5, 1.9, 1.8 (four thresholds) | SDSS | arXiv:1510.05651 | Fig. 9 |
| Satellite fraction | ~30% (v_peak) vs < ~24% (mass-based) at 10^9.5 h⁻²M_⊙ | Bolshoi SHAMs | arXiv:1705.06347 | Sect. 4.1 |
| EAGLE test | small-scale over-prediction 30%; assembly bias 20%, captured within 15% | EAGLE | arXiv:1507.01948 | abstract |
| SHAMe resolution | fits TNG300 with a 64× lower-resolution run | TNG300 | arXiv:2012.06596 | Sect. 8 |
| Assembly-bias range | factor ~3 in large-scale clustering (A = ±1), as cited | SHAMe | arXiv:2012.06596 | Sect. 4 |
| SMF systematic prior | μ: 0.25 dex Gaussian; κ: N(0, 0.10) | Behroozi 2010 | arXiv:1001.0015 | Sect. III.1.1 |
| Scatter neglect | +0.13–0.19 dex in M* at 10^14.25 M_⊙ | Behroozi 2010 | arXiv:1001.0015 | Sect. IV.3.7 |
| Typical high-mass shape | δ = 0.5–0.6, γ = 1.3–1.7 (z = 0) | Behroozi 2010 | arXiv:1001.0015 | Sect. III.4.3 |
| DES Y3 HOD priors | σ_log M* U[0.01, 0.5]; α_sat U[0.5, 3]; κ U[0, 5]; B_sat U[0, 20]; β_sat U[0.1, 2]; B_cut U[0, 15]; β_cut U[−0.5, 2]; f_cen = f_sat = 1 | DES Y3 | arXiv:2506.22367 | Table 2 |
| DES Y3 SHMR priors | log M_1 U[11, 13]; log ε U[−2, −1]; α U[−3, −1]; γ U[0, 1]; δ U[3, 6] | DES Y3 | arXiv:2506.22367 | Table 2 |
| DES Y3 nuisances | κ_c U[0.1, 1.3]; α_lmag U[1, 3]; Δlog M* U[−0.15, 0.15]; Δz_ℓ N(0, 0.1), second entry a variance per the caption; Σ_ℓ U[0.8, 1.3] | DES Y3 | arXiv:2506.22367 | Table 2, Sect. 6 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Satellite deficit read as a failed galaxy–halo relation.** Small-scale
  clustering too low under M_peak SHAM tracks f_sat [src: arXiv:1705.06347,
  Sect. 4.1]. Test: compare f_sat with a group catalogue processed like the
  data (arXiv:1207.2160, Sect. VI.1) before changing the proxy.
- **Resolution-dependent results.** The same parameters give different
  clustering on different boxes [src: arXiv:1207.2160, App. B;
  arXiv:2012.06596, Sect. 2.3]. Test: rerun on a lower-resolution box, or
  include orphans and check convergence across resolutions.
- **Scatter at the high-mass end.** Deconvolution cannot keep the bright
  end for scatter ≳ 0.3 dex [src: arXiv:1207.2160, Fig. 3]. Test: compare
  the output SMF with the input at the bright end.
- **Intrinsic and measured scatter mixed.** Without a measurement-error
  kernel the fitted scatter includes it [src: arXiv:1207.2160, Sect.
  III.2]; Behroozi et al. convolve both (Eq. 17). Test: state which
  kernels were applied before comparing scatters.
- **Group-catalogue comparisons without the group finder.** Test: run mocks
  through fibre collisions and the same finder, as Reddick et al. do.
- **Likelihood normalisation.** exp(−χ²_r) with averaged χ² (MEAM) and
  Gaussian likelihoods give different error bars on the same SMF [der: from
  arXiv:1205.5807, Eqs. 4, 10]. Test: check the likelihood before
  comparing SHMR uncertainties across papers.
- **Satellite rule.** Satellites growing after infall (current SMF on
  M_acc) and satellites frozen at infall give different relations
  [src: arXiv:1001.0015, Sect. III.3.2; arXiv:1205.5807, Sect. 3.2]. Test:
  report which rule was used.
- **Fixed central–satellite equality.** SHAM assigns M* without regard to
  host mass or central status; EAGLE shows both assumptions are not quite
  satisfied [src: arXiv:1507.01948, abstract].

## Reading list
<!-- key: reading-list -->

- Method: Reddick et al. 2013, arXiv:1207.2160 — eight proxies, deconvolved
  scatter, μ_cut disruption, mocks through the group finder, resolution.
- Method: Lehmann et al. 2017, arXiv:1510.05651 — v_α interpolation, epoch
  of peak mass, joint α–scatter constraint.
- Method: Behroozi et al. 2010, arXiv:1001.0015 — stellar-mass nuisance
  model, deconvolution limits, SHMR functional form, error budget.
- Method: Moster et al. 2013, arXiv:1205.5807 — multi-epoch matching,
  satellites frozen at infall, likelihood.
- Method: Contreras et al. 2020, arXiv:2012.06596 — SHAMe orphans,
  disruption and assembly-bias parameters; resolution convergence.
- Application: Zacharegkas et al. 2025, arXiv:2506.22367 — SHMR inside an
  HOD with lensing, priors and nuisances.
- Critique: Campbell et al. 2018, arXiv:1705.06347 — the M_peak clustering
  crisis and three remedies.
- Critique: Chaves-Montero et al. 2016, arXiv:1507.01948 — SHAM tested
  against EAGLE.

## Not verified
<!-- key: not-verified -->

- Hearin et al. 2013 (re-ranking scatter), Trujillo-Gomez et al. 2011
  (list-drawing), Contreras et al. 2020a (assembly-bias implementation,
  factor three), Moster et al. 2018 (disruption rule), Guo & White 2014
  (orphans in SHAM) and Paranjape et al. 2018: cited in the papers read,
  not read, no identifiers recorded.
- The SHM functional form of Moster et al. 2013 (its Eq. 2) was not read;
  only its parameter names and redshift dependence (Eqs. 5–8).
- SHMR comparison: arXiv:1811.01139 read in its abstract only; the
  numerical gap between the DES Y3 and matching SHMRs above 10¹² M_⊙, and
  KiDS lensing SHMRs, were not read.
- The orphan fractions needed by each SHAM model in arXiv:1705.06347,
  Fig. 11, and its Appendix C completeness fit were not read as text.
