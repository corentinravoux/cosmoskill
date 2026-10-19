# Satellites, group catalogues and satellite kinematics — cosmo-galaxy-halo-connection dossier

Scope: how centrals and satellites are separated in a redshift survey (the
halo-based and self-calibrated group finders, their purity and completeness,
their failure modes), how satellite kinematics is measured and modelled
(selection cones, interlopers, Jeans modelling, anisotropy, radial profile),
how velocity bias is measured from small-scale redshift-space clustering,
and how fibre collisions are handled in each; what each choice was found to
cost.
Snapshot: 2026-10-19.
From: Wechsler & Tinker 2018, Sect. 3.3, 5.5-5.6, 6.2.

Already in L2, not repeated here: the satellite results (CMASS velocity
bias 0.22 and 0.86, DESI QSO α_c, DESI ELG strict conformity, DESI DR1 BGS
satellite slopes and quenched fractions, KiDS-1000 sub-Poisson variance) in
`results.md#satellites`; the DESI DR1 BGS group catalogue facts (size,
~0.2 dex mass errors, lost-galaxy redshifts correct ~50% of the time) in
`surveys-and-data.md#group-and-cluster-catalogues`; the sizes of the
satellite-profile, velocity-bias, orphan and disruption systematics,
including the Basilisk S8 profile test, in
`systematics.md#satellite-distribution-velocity-bias-and-orphans`; why group
and HOD satellite fractions of DESI BGS disagree in
`systematics.md#scatter-slope-degeneracy`. The AbacusHOD velocity
parameters (α_vel,c, α_vel,s) and the placement of centrals and satellites
in simulation-based HODs are in `deep/hod-clf.md` (Step 1 and "Central
position and satellite tracers"); orphans and subhalo disruption in SHAM in
`deep/abundance-matching-shmr.md`; PIP weights as a clustering estimator in
`cosmo-galaxy-clustering`.

Symbols. Primary / secondary: a galaxy selected as a central / satellite
(they may not be true ones). Impurity: a primary that is not a true
central. Interloper: a secondary that is not in the primary's halo. ΔV:
line-of-sight velocity difference of a secondary relative to its primary.
R_p: projected separation. σ_200: satellite velocity dispersion in units of
200 km/s. β: velocity anisotropy, β = 1 − σ_t²/(2σ_r²) with σ_t, σ_r the
tangential and radial dispersions. n_sat(r|M): number-density profile of
satellites in a halo of mass M. 𝓡 = c_vir/c_sat: ratio of halo to satellite
concentration. γ: inner logarithmic slope of n_sat. f_sat: satellite
fraction. α_c, α_s: central and satellite velocity-bias factors.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Decide how centrals and satellites are identified
<!-- key: step-1-decide-how-centrals-and-satellites-are -->

Two routes are in use: a group finder that partitions the whole sample into
groups and gives each a halo mass, or a local isolation criterion that
selects only primary–secondary pairs for kinematics. The second keeps only
systems it can use and never assigns a mass to the rest.

**Halo-based group finder (Yang et al. 2007, arXiv:0707.4640).** Five steps
[src: Sect. III.1]:

1. Potential centres from a friends-of-friends pass with very small linking
   lengths, ℓ_z = 0.3 along the line of sight and ℓ_p = 0.05 transverse, in
   units of the mean galaxy separation; every unlinked galaxy is also a
   tentative centre.
2. A characteristic luminosity L_19.5, the completeness-weighted sum of
   member luminosities brighter than ⁰·¹M_r − 5 log h = −19.5 (Eq. 3),
   corrected for members lost below the flux limit at z > 0.09 (Eq. 4).
3. A halo mass from a mass-to-light ratio (500 h M_⊙/L_⊙ at the first
   iteration, then the relation from the previous iteration), and from it
   r_180 (Eq. 5) and a line-of-sight dispersion σ = 397.9 km/s (M_h/10¹⁴
   h⁻¹M_⊙)^0.3214 (Eq. 6). Haloes are defined at overdensity 180.
4. Membership from the redshift-space density contrast P_M(R, Δz) = (H₀/c)
   Σ(R)/ρ̄ p(Δz) (Eq. 7), with Σ the projected NFW profile (Eqs. 8–10) and
   p(Δz) a Gaussian of width σ (Eq. 11); a galaxy joins a group if P_M ≥ B
   = 10, the group with the largest P_M if several qualify; two groups
   merge if all members of one belong to the other.
5. Iterate from step 2 until memberships stop changing.

The final masses come from rank-matching L_19.5 (or total stellar mass) to
a halo mass function in volume-complete group subsamples (three redshift
limits, Table 2), interpolated for the others, down to 10^11.6 h⁻¹M_⊙ [src:
Sect. III.5]. The stated reason for not using dynamical masses: most groups
have a few members, which makes velocity-dispersion masses "extremely
unreliable" [src: Sect. III.5]. The background level B was tuned on a mock
to maximise the mean of f_c(1 − f_i) (definitions in Step 4) [src: Sect.
III.2].

**Self-calibrated group finder (DESI DR1 BGS, arXiv:2610.20919).** The same
skeleton, with three changes [src: Sect. IV.1]:

- Haloes are M_200m with NFW profiles on a mean c(M) relation (Eqs. 2–3);
  each step inverse-abundance-matches a weighted group luminosity w_cen w_f
  L_grp to the halo mass function at z = 0 (Eq. 4), in redshift bins of
  width 0.05 with 1/V_max weighting; w_f(z) = 10^(0.561 (z/0.311)^2.077)
  restores satellite light lost below the flux limit (Eqs. 5–6) and moves
  masses by only a few per cent.
- Luminosity rather than stellar mass is matched because luminosity has the
  lower uncertainty and the weights can absorb the lower luminosity of
  quiescent galaxies at fixed stellar mass [src: footnote 5].
- A neighbour becomes a satellite if P_sat = 1 − [1 + P_proj P_z /
  B_sat,c(L)]⁻¹ > 0.5 (Eq. 7), with P_proj the projected NFW density and
  P_z a Gaussian in cΔz (Eqs. 8–11). The threshold B_sat,c = β_0,c +
  β_L,c (log L − 9.5) (Eq. 12) and the central weight log w_cen,c, an error
  function of log L (Eq. 13), each take separate quiescent and star-forming
  parameters: ten in all.

The ten parameters are calibrated, not tuned by hand [src: Sect. IV.2]:
run the finder to |Δf_sat| < 0.001 (typically 4–5 iterations), tabulate the
mean occupation of volume-limited subsamples, populate the z = 0
Bolshoi-Planck halo catalogue with Poisson satellites, compute w_p with
Corrfunc, and add a χ² on the ratio of quiescent to star-forming total
satellite luminosity L_sat in bins of central luminosity: χ²_tot = Σ over 14
w_p samples + χ²_Lsat (Eq. 14), explored with emcee for 200 000 iterations.
The final catalogue runs 10 iterations, converged to |Δf_sat| < 3 × 10⁻⁵.
The B_sat parameters are constrained by the one-halo-scale clustering, the
w_cen parameters mostly by L_sat [src: Sect. IV.1].

**Isolation criteria for kinematics.** A primary is the brightest galaxy in
a cylinder (More et al. 2011) or a cone frustum (Basilisk) around it;
secondaries are fainter galaxies in a smaller one. Sizes scale with σ_200,
itself fitted iteratively as a function of the primary's luminosity or
stellar mass: R_h = 0.8 σ_200 h⁻¹Mpc, ΔV_h = 1000 σ_200 km/s, R_s = 0.15
σ_200 h⁻¹Mpc, ΔV_s = 4000 km/s in More et al. (arXiv:1003.3203, Eq. 3) [src:
Sect. 3.1]; R_ap^pri = 0.6 σ_200, R_ap^sec = 0.15 σ_200 h⁻¹Mpc and ΔV^pri =
ΔV^sec = 1000 σ_200 km/s with log σ_200 = 0.04 + 0.48 log L_10 + 0.05 (log
L_10)², capped at σ_200 = 4, in Basilisk (arXiv:2409.03105, Eq. 1); the
radii are about 1.65 and 0.4 virial radii [src: Sect. 2.1]. The reason for
scaling: brighter primaries live in larger haloes, and mass-scaled
selection gives "much lower interloper fractions" than fixed cylinders in
mock tests [src: arXiv:1003.3203, Sect. 3.1].

### Step 2. Correct for spectroscopic incompleteness at small separations
<!-- key: step-2-correct-for-spectroscopic-incompleteness -->

Fibre collisions remove close pairs, which are exactly the one-halo pairs.

| Analysis | Treatment | Reason or test | Place read |
|---|---|---|---|
| SDSS satellite kinematics (Basilisk) | primaries removed where spectroscopic completeness < 0.8 or where < 80% of the secondary cone lies in the footprint (w_app from ~5 × 10⁴ random points); collided galaxies get the nearest neighbour's redshift during primary selection only, then all collided primaries and secondaries are removed; R_p < 55″ excluded | ~65% of SDSS galaxies with a neighbour within 55″ lack a redshift | arXiv:2409.03105, Sect. 2.2, 6.4 |
| BOSS CMASS velocity bias | Guo et al. 2012 correction: split into collision-free and potentially collided populations, the latter's contribution estimated from resolved pairs in tile overlaps | collision scale ~0.4 h⁻¹Mpc at z ~ 0.5; ~7% of CMASS galaxies collided | arXiv:1407.4811, Sect. 2.1, 3.2, App. A |
| DESI One-Percent LRG/QSO | pairwise-inverse-probability weights from 128 fibre-assignment realisations plus angular up-weighting (PIP+ANG) | stated unbiased down to 0.1 h⁻¹Mpc (Mohammad et al. 2020, as cited) | arXiv:2306.06314, Sect. 2 |
| DESI One-Percent ELG | same weights, and the sample cut to 0.2–1.5° from each rosette centre (−12%, 215 000 left); clustering below twice the mean seeing is lost to blending | weights then matter only below ~1 h⁻¹Mpc; imaging and redshift-failure weights negligible on small scales | arXiv:2306.06319, Sect. 2.2 |
| DESI DR1 BGS groups | lost galaxies (no fibre or Δχ² < 40) get a redshift before group finding by a hybrid nearest-neighbour (HNN) scheme mixing neighbour redshifts and photometric redshifts | photo-z alone (σ = 0.012 + 0.031 z) is within 0.005 of the truth only ~33% of the time, which suppresses f_sat; pure nearest neighbour over-estimates f_sat | arXiv:2610.20919, App. A.2–A.3 |

The DESI group finder deliberately leaves its algorithm unchanged and
treats lost galaxies as a pre-processing step, unlike the photometric
group finding it cites, which widens the redshift-space Gaussian and lowers
B_sat [src: arXiv:2610.20919, App. A.2]. Its choice criterion is stated:
"We prioritize minimizing biases over maximizing correct redshifts" [src:
App. A.3].

### Step 3. Measure the kinematic statistic
<!-- key: step-3-measure-the-kinematic-statistic -->

**Stacked dispersions (More et al. 2011).** Satellites are binned by the
central's luminosity or stellar mass, and P(ΔV) is fitted by two Gaussians
plus a constant (the constant absorbs interlopers) (Eq. 4); the dispersion
is σ² = (a₁σ₁³ + a₂σ₂³)/(a₁σ₁ + a₂σ₂) − σ_err² (Eq. 5), with σ_err = √2 ×
35 ≈ 49.5 km/s for SDSS redshift errors, and errors from 1000 Poisson
realisations of the histogram [src: Sect. 3.2]. Two weightings are
measured: satellite-weighted (each satellite counts once) and host-weighted
(weight 1/N_sat). The reason: σ_sat alone cannot separate the mean
mass–luminosity relation from its scatter, since different relations with
different scatter give the same σ_sat; the two weightings are equal only for
zero scatter, so their difference measures it [src: Sect. 3.2].

**Forward model of individual pairs (Basilisk).** No stacking: the
likelihood of every secondary's (ΔV, R_p) is computed given the CLF, which
handles mass mixing; the number of secondaries per primary and the
luminosity function enter as further data [src: arXiv:2409.03105, Sect. 3,
4.2].

### Step 4. Model satellites, interlopers and the halo
<!-- key: step-4-model-satellites-interlopers-and-the-halo -->

**Satellites.** Both approaches treat satellites as tracers in a spherical
NFW halo with a fixed c(M) (Macciò et al. 2007 in More et al.; Diemer &
Kravtsov 2015 in Basilisk), the central at rest at the centre, and the
satellite profile a generalised NFW, n_sat ∝ (r/𝓡r_s)^(−γ) (1 +
r/𝓡r_s)^(γ−3) (arXiv:1003.3203, Eq. 10) [src: Sect. 3.3.1; arXiv:2409.03105,
Sect. 4.2.4]. More et al. fix (γ, 𝓡) = (0, 2) from their earlier SDSS
analysis, assume Poisson satellite numbers and isotropic orbits, and average
the Jeans radial dispersion (Eq. 14) over the aperture (Eqs. 12, 16) [src:
Sect. 3.3.1]. Basilisk adds:

- a constant anisotropy β fitted to the data, entering the projected
  dispersion (Eq. 41) and, through the fourth-order Jeans equation, the
  line-of-sight kurtosis (Eqs. 43–44); the line-of-sight distribution is a
  generalised Gaussian rather than a Gaussian, because "there is no a priori
  reason why the LOSVD should be Gaussian" and its shape carries the
  anisotropy [src: Sect. 4.2.4];
- splashback galaxies, by extending the satellite integrals to r_sp = f_sp
  r_vir with f_sp = 2; f_sp ≳ 1.5 recovers β without bias on mocks, f_sp = 1
  biases β weakly, f_sp = 3 gives indistinguishable posteriors [src: Sect.
  4.2.5];
- interlopers as a background term proportional to the comoving volume of
  each velocity slice of the cone (Eq. 50), which rises with ΔV because the
  back of a cone is larger, plus an infalling Gaussian whose amplitude and
  width are measured per primary from "tertiary" galaxies at 0.6–0.9 σ_200
  h⁻¹Mpc (Eq. 49) [src: Sect. 4.2.5]. A Kaiser-model infall term was tried
  and "did not yield sufficiently accurate results"; the uniform interloper
  model of the first Basilisk paper over-estimated satellite numbers and
  biased the satellite CLF parameters in larger samples [src: same].

**Radial profile.** Basilisk pre-computes arrays at fixed (γ, 𝓡), so the
profile is scanned on a 15 × 15 grid of (γ, log 𝓡) with one chain per node
and the likelihoods combined [src: App. C]. On SDSS the best fit is (γ, 𝓡)
= (0.94, 1.7), satellites tracing the dark matter, (1, 1), are excluded at
more than 5σ, and γ and 𝓡 are degenerate along a ridge; the CLF parameters
are "very robust" to moderate moves along it [src: App. C]. On a mock with
satellites in subhaloes the true profile is (0.0, 2.6) and Basilisk returns
(0.0, 2.5) [src: Sect. 5.2].

### Step 5. Velocity bias from small-scale redshift-space clustering
<!-- key: step-5-velocity-bias-from-small-scale-redshift -->

Guo et al. 2015 (arXiv:1407.4811) populate SO haloes of a simulation with a
Zheng et al. 2007 HOD (Eqs. 8–9), centrals at the potential minimum and
satellites on random dark-matter particles, which keeps halo shapes [src:
Sect. 2.2.2]. Velocities: the central gets a Gaussian line-of-sight
velocity of width σ_c = α_c σ_v relative to the halo core (Eq. 10);
satellites v_s − v_h = α_s (v_p − v_h) (Eq. 11), so σ_s = α_s σ_v; no
velocity bias means α_c = 0, α_s = 1. A 30 km/s Gaussian redshift error,
measured from repeat observations, is added to every galaxy. Predictions
are tabulated for α_c ∈ [0, 1] and α_s ∈ [0, 2] in steps of 0.1 and
interpolated; seven free parameters [src: same]. The data vector is w_p,
ξ₀, ξ₂ and ξ₄ in 0.2-dex bins centred from 0.13 to 51.5 h⁻¹Mpc, π_max = 100
h⁻¹Mpc, Δμ = 0.05 [src: Sect. 2.1]. The same parameterisation, with α_c
restricted to non-negative values, is the AbacusHOD one (`deep/hod-clf.md`).

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Group finder or isolation criterion
<!-- key: group-finder-or-isolation-criterion -->

A group finder returns every galaxy's classification and a mass for every
group, which non-parametric HODs, red fractions and conformity need; it
pays with three coupled error types that Campbell et al. 2015
(arXiv:1505.04798) separate [src: Sect. 3.1, 6]:

- **Membership.** "Fracturing" splits one halo's galaxies into several
  groups (satellites become centrals, masses fall); "fusing" merges galaxies
  of several haloes into one group (centrals become satellites, masses
  rise).
- **Central designation.** The brightest member is called the central. Even
  with perfect membership about 10% of groups at 10¹³ M_⊙ have a satellite
  as brightest galaxy in their mock, and phase-space studies they cite find
  the brightest member is a satellite in ~25% (Milky-Way-mass) to ~40%
  (cluster) of haloes [sec: van den Bosch et al. 2005 and Skibba et al. 2011,
  as cited in Sect. 3.1.2 of arXiv:1505.04798].
- **Mass.** Abundance-matched group masses inherit both errors.

Isolation criteria avoid fusing by design but keep impurities: about 5% with
the earlier Basilisk selection, which biased the inferred scatter of the
mass–luminosity relation by more than 3σ once the sample was eight times
larger; the tightened cones remove most "Type-II" impurities (neither
central nor brightest satellite), while "Type-I" impurities (a satellite
brighter than its central) are forward-modelled [src: arXiv:2409.03105,
App. A].

### Which group finder
<!-- key: which-group-finder -->

On one age-matching mock with conformity, run through three finders tuned
to it, f_sat(L) is over-estimated by the Berlind et al. finder (fusing, a
transition ratio T_sat ≃ 1.75), less so by the Yang et al. finder, and
recovered by the Tinker et al. finder except at high luminosity, where
central inversion dominates [src: arXiv:1505.04798, Sect. 4.3]. All three
recover the first moment of the HOD for the full sample and the CLF, but
the central red fraction poorly; all recover a true one-halo conformity
signal and all induce a smaller spurious one in a shuffled mock without
conformity [src: Sect. 4.6, 6]. Their recommendation: model the group
finder errors through the halo transition probability or forward-model
the group finding on mocks [src: Sect. 6]. f_sat(L) is also "sensitive to
the halo definition applied when tuning a group finder" [src: Sect. 6].

### Hand-tuned or self-calibrated
<!-- key: hand-tuned-or-self-calibrated -->

Yang et al. tune one background level on a CLF mock [src:
arXiv:0707.4640, Sect. III.2]; the self-calibrated finder fits ten colour-
and luminosity-dependent parameters to the sample's own w_p and L_sat
[src: arXiv:2610.20919, Sect. IV.2]. The cost of the latter is that the
calibration itself assumes a halo catalogue (Bolshoi-Planck), Poisson
satellites and a cosmology; its authors found low sensitivity to cosmology
in earlier tests but advise more extensive tests before cosmological use
[src: Sect. IV.1].

### Stacked dispersions or full forward model
<!-- key: stacked-dispersions-or-full-forward-model -->

Stacking with two weightings separates mean relation and scatter only
through the sw/hw difference [src: arXiv:1003.3203, Sect. 3.2]. The forward
model uses each pair, models mass mixing, interlopers, splashback and
selection, and constrains β: SDSS gives β = 0.29 (+0.05, −0.04), radially
anisotropic, consistent with but tighter than β = 0.26 ± 0.09 from an
analysis without mass mixing and with fewer pairs [src: arXiv:2409.03105,
Sect. 6.4]. A mass-dependent β(M) model shows a weak trend toward more
radial orbits at low mass, which the authors warn may be a radial
dependence in disguise, because the 55″ cut removes a different fraction of
the virial radius at each mass [src: Sect. 6.4].

### Fixed or fitted satellite profile
<!-- key: fixed-or-fitted-satellite-profile -->

More et al. fix a cored profile (0, 2) [src: arXiv:1003.3203, Sect.
3.3.1]; Basilisk II fits (0.94, 1.7) on SDSS kinematics [src:
arXiv:2409.03105, App. C]; the later Basilisk cosmology analysis prefers γ
= 1, 𝓡 ≈ 2.2 and finds that the profile choice moves (Ω_m, σ8) by up to
~5σ (`systematics.md#satellite-distribution-velocity-bias-and-orphans`). The
halo parameters are robust to the profile in Basilisk II, the cosmological
parameters are not in its successor [der: comparison of App. C of
arXiv:2409.03105 with the L2 entry on arXiv:2512.14889].

### Which statistic for velocity bias
<!-- key: which-statistic-for-velocity-bias -->

On CMASS, ξ₀ + ξ₂ gives weak velocity-bias constraints, adding ξ₄ tightens
them (it picks up finer finger-of-God structure), and adding w_p tightens
them further by excluding regions of the occupation parameters; ξ₀ + ξ₂ +
ξ₄ alone gives a significantly smaller α_s than with w_p, because the
small-scale w_p shape is itself sensitive to satellite velocities in
massive haloes [src: arXiv:1407.4811, Sect. 3.2]. α_c is set mainly by
scales above ~1 h⁻¹Mpc (two-halo central pairs), α_s by the one-halo
finger-of-God regime [src: same].

### SO or FoF haloes, and where the centre is
<!-- key: so-or-fof-haloes-and-where-the-centre-is -->

Guo et al. prefer SO haloes because FoF haloes are bridged; with the
potential minimum as centre in both, the central velocity bias is
insensitive to the halo definition [src: arXiv:1407.4811, Sect. 3.2]. The
group finders assume Δ = 180 (Yang) or 200m (DESI): their masses and f_sat
are tied to that choice [src: arXiv:0707.4640, Sect. III.1;
arXiv:2610.20919, Sect. IV.1].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| FoF seed linking lengths | ℓ_z = 0.3, ℓ_p = 0.05 (mean separations) | SDSS DR4 groups | arXiv:0707.4640 | Sect. III.1 |
| Membership threshold | B = 10 | SDSS DR4 groups | arXiv:0707.4640 | Sect. III.1 |
| Group completeness | > 90% of groups f_c > 0.6; 80% f_c > 0.8; f_c = 1 for ~95% (low mass) to ~60% (clusters) | SDSS DR4 mock | arXiv:0707.4640 | Sect. III.2 |
| Group contamination | ~65% of groups f_i = 0; ~85% f_i ≤ 0.5 | SDSS DR4 mock | arXiv:0707.4640 | Sect. III.2 |
| Lowest assigned group mass | 10^11.6 h⁻¹M_⊙ | SDSS DR4 groups | arXiv:0707.4640 | Sect. III.5 |
| Calibrated parameters | 10 (4 B_sat, 6 w_cen) | DESI DR1 BGS SCGF | arXiv:2610.20919 | Sect. IV.1 |
| Calibration data | 14 w_p samples + L_sat ratio; 200 000 emcee iterations | DESI DR1 BGS SCGF | arXiv:2610.20919 | Sect. IV.2, Eq. 14 |
| Lost-galaxy test sample | truth 106 965 targets, 124 deg², 97.9% complete; test 78.4% complete | DESI SV3 vs DR2-internal | arXiv:2610.20919 | App. A.2 |
| Classification after HNN | satellites purity 82.3%, completeness 81.2%; centrals 94.1%, 94.5% (against SV3, not mocks) | DESI DR1 BGS | arXiv:2610.20919 | App. A.3 |
| Central inversion, perfect membership | ~10% at 10¹³ M_⊙ | age-matching mock | arXiv:1505.04798 | Sect. 3.1.2 |
| Selection cones | R_pri = 0.6, R_sec = 0.15 σ_200 h⁻¹Mpc; ΔV = 1000 σ_200 km/s | Basilisk II | arXiv:2409.03105 | Sect. 2.1 |
| Selection cylinders | R_h = 0.8, R_s = 0.15 σ_200 h⁻¹Mpc; ΔV_h = 1000 σ_200, ΔV_s = 4000 km/s | SDSS, More et al. | arXiv:1003.3203 | Sect. 3.1 |
| Sample sizes | 3949 centrals, 6213 satellites (luminosity-stacked, all) | SDSS, More et al. | arXiv:1003.3203 | Table 1 |
| Velocity error | σ_err = 49.5 km/s on ΔV (35 km/s per galaxy) | SDSS | arXiv:1003.3203 | Sect. 3.2 |
| Velocity error | 30 km/s per galaxy | BOSS CMASS | arXiv:1407.4811 | Sect. 2.2.2 |
| Fibre-collision angle; collided fraction | 55″; ~65% of galaxies with a neighbour inside it lack a redshift | SDSS | arXiv:2409.03105 | Sect. 2.2 |
| Fibre-collision scale; collided fraction | ~0.4 h⁻¹Mpc at z ~ 0.5; ~7% (2.1% in the ancillary test region) | BOSS CMASS | arXiv:1407.4811 | Sect. 3.2, App. A |
| Splashback extent of satellites | f_sp = 2 (unbiased β for f_sp ≳ 1.5) | Basilisk II | arXiv:2409.03105 | Sect. 4.2.5 |
| Orbital anisotropy | β = 0.29 (+0.05, −0.04) | SDSS, Basilisk II | arXiv:2409.03105 | Sect. 6.4 |
| Satellite profile | (γ, 𝓡) = (0.94, 1.7); DM-tracing (1, 1) excluded at > 5σ | SDSS, Basilisk II | arXiv:2409.03105 | App. C |
| Impurities, earlier selection | ~5%; scatter biased > 3σ for an 8× larger sample | Basilisk mocks | arXiv:2409.03105 | App. A |
| Velocity-bias tables | α_c ∈ [0, 1], α_s ∈ [0, 2], step 0.1 | BOSS CMASS | arXiv:1407.4811 | Sect. 2.2.2 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Group-catalogue statistics read as halo statistics.** Fusing,
  fracturing and central inversion equalise the properties of red and blue
  sub-populations and can create a one-halo conformity signal where there
  is none [src: arXiv:1505.04798, Sect. 4.6, 6]. Test: run the same finder
  on a mock with and without the effect (the shuffled mock of that paper);
  compare in group space, not halo space.
- **Group masses used where they were not validated.** Typical error ~0.2
  dex, larger for groups without satellites, lost centrals, footprint edges
  and unrelaxed rich clusters; high-redshift BGS groups are mostly bright
  isolated centrals [src: arXiv:2610.20919, Sect. VI.2]. Test: the same
  statistic on mock group catalogues processed identically.
- **Lost galaxies dropped or given photo-z.** Dropping them lowers f_sat
  (they sit in dense regions); photo-z placement lowers it too; plain
  nearest-neighbour raises it [src: arXiv:2610.20919, App. A.3]. Test: a
  high-completeness truth region against the incomplete footprint (the
  SV3 test).
- **Fibre-collision correction untested.** Test: refit on a collision-free
  subset (complete sectors, ~1/4 of the CMASS area) and without r_p, s < 0.5
  h⁻¹Mpc; in CMASS neither changed the velocity bias substantially [src:
  arXiv:1407.4811, Sect. 3.2]. A targeted ancillary sample reproduced w_p
  and the multipoles within errors [src: App. A].
- **Kinematics with a uniform interloper background.** Over-counts
  satellites and biases the satellite CLF in large samples [src:
  arXiv:2409.03105, Sect. 4.2.5]. Test: fit the tertiary-galaxy velocity
  distribution, which matches the interlopers' in mocks [src: Fig. 4
  caption].
- **Type-II impurities.** Low-luminosity primaries with high-dispersion
  secondaries inflate the inferred scatter [src: arXiv:2409.03105, App. A].
  Test: plot primaries of a mock in the (M_h, L) plane and count those
  beyond 4σ_c from the input relation.
- **Selection bias read as the mass–luminosity relation.** Brighter
  primaries have larger cones and more luminosity range above the
  secondary limit, so primaries with secondaries are biased bright at fixed
  mass; the raw median L(M) of selected primaries does not equal the input
  relation [src: arXiv:2409.03105, Sect. 5.2]. Test: forward-model the
  selection, as Basilisk does, instead of averaging selected systems.
- **Anisotropy and radius confused.** With a fixed angular cut, a radial
  dependence of β can appear as a mass dependence [src: arXiv:2409.03105,
  Sect. 6.4].
- **Satellite velocity bias without w_p.** Redshift-space multipoles alone
  give a lower α_s on CMASS [src: arXiv:1407.4811, Sect. 3.2]. Test: fit
  with and without w_p and ξ₄.
- **Validation criterion.** Basilisk's pass criterion is recovery of the
  input CLF from 10^11.5 to 10¹⁵ h⁻¹M_⊙ and of the subhalo-like profile on
  a mock whose satellites sit in subhaloes [src: arXiv:2409.03105, Sect.
  5.2, Fig. 9 caption].

## Reading list
<!-- key: reading-list -->

- Method, group finder: Yang et al. 2007, arXiv:0707.4640 — the
  halo-based algorithm, completeness/contamination/purity definitions,
  rank-ordered group masses.
- Method, current group finder: Williams et al. 2026, arXiv:2610.20919 —
  self-calibration on w_p and L_sat, lost-galaxy treatment, usage advice.
- Critique: Campbell et al. 2015, arXiv:1505.04798 — failure modes of three
  finders on one mock; spurious conformity; forward-model group finding.
- Method, kinematics: More et al. 2011, arXiv:1003.3203 — scaled
  cylinders, satellite- and host-weighted dispersions, isotropic Jeans
  model.
- Method, kinematics: Mitra et al. 2024, arXiv:2409.03105 — Basilisk II:
  cones, interloper model from tertiaries, splashback, kurtosis and β,
  profile scan, impurities.
- Method, velocity bias: Guo et al. 2015, arXiv:1407.4811 — α_c, α_s
  tables, statistic combinations, fibre-collision tests.
- Application: Yuan et al. 2024, arXiv:2306.06314, and Rocher et al. 2023,
  arXiv:2306.06319 — PIP+ANG weights and rosette cuts in DESI small-scale
  HOD fits.

## Not verified
<!-- key: not-verified -->

- The Tinker et al. and Berlind et al. group finders, the first Basilisk
  paper and Lange et al. 2019, Guo et al. 2012 (fibre-collision method),
  Mohammad et al. 2020 (PIP accuracy), Wojtak & Mamon 2013 and the
  self-calibrated finder's Papers I and II are cited in the papers read; not
  read, no identifiers recorded.
- The c(M) relation and the halo mass function used by the DESI DR1
  group finder are cited there by reference number only ([54], [81]); their
  identity was not checked.
- The purity and completeness of the DESI DR1 group finder on mocks (Paper
  I) were not read; the numbers above compare with the SV3 truth catalogue
  only.
