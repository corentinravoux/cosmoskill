# FRB baryon census and halo gas — cosmo-multimessenger dossier

Scope: how the partition of diffuse baryons between the intergalactic medium
and halo gas is obtained from fast-radio-burst dispersion measures (one-point
distribution, per-sightline foreground mapping, DM–galaxy two-point
statistics, joint use with kSZ), with each analysis's definitions, model,
covariance and cuts, and the tests that catch selection and modelling biases.
Snapshot: 2026-10-17.
From: Glowacki & Lee 2024 review (arXiv:2410.24072), Sects. 3.1 and 4
(simulations, halo gas, impact on weak-lensing cosmology); FLIMFLAM and
CHIME/FRB cross-correlation programmes.

Already in L2, not repeated here: the DM budget and the Macquart relation in
`physics-and-methods.md#budget`; the three FRB likelihoods table in
`physics-and-methods.md#scatter-and-the-likelihood`; headline values of
`f_IGM`, `f_d` and halo-gas limits in `results.md` and
`open-questions.md#where-are-the-baryons-according-to-frbs`; host and Galactic
DM systematics in `systematics.md#fast-radio-bursts-host-and-milky-way-dispersion`.

## How it is done
<!-- key: how-it-is-done -->

Notation. `DM_obs` observed dispersion measure (pc cm⁻³); `DM_MW` the Milky
Way part (disc ISM plus halo); `DM_ex = DM_obs − DM_MW`; `DM_cosmic` (or
`DM_cos`) the intergalactic part, split into `DM_IGM` (gas outside haloes)
and `DM_halos` or `DM_X` (intersected haloes); `DM_host` the host part,
quoted in the rest frame; `z_s` the burst redshift; `b_⊥` impact parameter;
`f_IGM`, `f_X`, `f_cgm`, `f_icm` the fractions of all cosmic baryons in the
IGM, in intersected haloes, in the CGM of `M ≲ 10¹⁴ M☉` haloes and in
clusters; `f_d` the diffuse ionised fraction; `f_gas` the gas mass of a halo
in units of `(Ω_b/Ω_m) M_halo`.

### Step 1. Fix what "IGM" and "halo" mean
<!-- key: step-1-fix-what-igm-and-halo-mean -->

The numbers differ between papers partly because the definitions do:

| Analysis | IGM | Halo gas | Place read |
|---|---|---|---|
| Connor et al. 2024 (arXiv:2409.16952) | gas outside virialised haloes; `f_IGM ≡ Ω_IGM/Ω_b` | `f_X ≡ Ω_halos/Ω_b` at `z = 0.1`; haloes are cells with dark-matter density ≥ 57 `ρ_c`, the expected density at `R_200` | main text; Methods |
| Khrykin et al. 2024, FLIMFLAM DR1 (arXiv:2402.00505) | gas at `0 ≲ ρ/ρ̄ ≲ 10` | intersections within about the virial radius, `ρ/ρ̄ ≳ 10–100`; `f_d ≡ f_igm + f_cgm + f_icm = 1 − f_* − f_bh − f_ism` (Eq. 18) | Sects. IV, V.2 |
| Hussaini et al. 2025 (arXiv:2506.04186) | sightlines with no halo at `b_⊥ < r_vir` (`r_vir` at 200 `ρ_c`, from stellar mass via a stellar-to-halo relation) | same 57 `ρ_c` cut in the simulation used for comparison | Sects. IV.3, IV.4 |

FLIMFLAM notes that "the notation DM_igm is often used to collectively denote
both the IGM and CGM contributions", which it keeps separate [src:
arXiv:2402.00505, Sect. IV].

### Step 2a. One-point route: partition from the shape of `p(DM_ex | z)`
<!-- key: step-2a-one-point-route-partition-from-the -->

Connor et al. 2024 [src: arXiv:2409.16952, main text and Methods]:

- Per-burst likelihood `P(DM_ex | z_s, θ)`, `θ = {f_IGM, f_X, μ_host, σ_host}`,
  product over bursts, MCMC. Host DM log-normal with `μ_host` ~ U(0, 7), so
  that the median spans 0–1000 pc cm⁻³; `f_IGM`, `f_X` ~ U(0, 1) with
  `f_IGM + f_X ≤ 1`.
- Cosmic part: a bivariate log-normal `P_cos(DM_IGM, DM_X | z_s)` fitted to a
  mock survey in TNG300-1 at all redshifts, because the two terms are
  correlated (sightlines through overdensities meet more haloes) and "one
  cannot simply draw from the distributions of halo DM and IGM DM
  independently". The log-means are shifted,
  `μ_DM_IGM = μ_DM_IGM,TNG + log(f_IGM/0.827)` and
  `μ_DM_X = μ_DM_X,TNG + log(f_X/0.138)`, with the log-variances fixed at the
  simulation values.
- Why the parts separate: each has "a different redshift dependence and
  `P(DM | z_s)` distribution". The constraint comes from the "DM cliff": no burst
  beyond `z = 0.1` has `DM_ex/z_s < 800` pc cm⁻³, which a halo-dominated or
  baryons-trace-dark-matter universe would not produce.
- Model uncertainty from using one simulation: MCMC errors inflated by 30%
  "based on model mismatch resampling experiments". Cross-check without the
  partition: `f_d` from the mean cosmic DM, 0.94 ± 0.05.
- Outliers removed from the primary fit: FRB 20190520B (large local DM; it
  "biases our estimates of nuisance parameters μ_host and σ_host but only
  removes noise" from `f_IGM`, `f_X`) and FRB 20220831A (large host DM);
  reintroduced in jackknife tests.

### Step 2b. Foreground route: map each sightline
<!-- key: step-2b-foreground-route-map-each-sightline -->

FLIMFLAM DR1, 8 localised bursts [src: arXiv:2402.00505, Sects. IV–V]:

1. **Model.** `DM_model,i = DM_MW,i + DM_cosmic,i + DM_host,i` (Eq. 3) with
   `DM_cosmic = DM_igm + DM_halos` (Eq. 4).
2. **Milky Way.** NE2001 for the disc; halo 40 pc cm⁻³ with `σ_MW = 15`,
   called "a sub-dominant error component" for DR1, although published values
   span 10–111 pc cm⁻³ [src: Sect. IV.1].
3. **IGM from a density reconstruction.** `DM_igm^argo = n̄_e,bar(z̄) Σ_s
   (1 + δ^sm_m,s) l_s (1 + z_s)⁻¹` (Eq. 7), on ARGO reconstructions of the
   foreground from wide-field spectroscopy, smoothed with `R = 0.7 h⁻¹ Mpc`
   (the scale that lets dark-matter-only grids reproduce the DM_igm
   distribution of hydrodynamical runs); `n̄_e,bar` from Eq. 8 with
   `Y_He = 0.243`, `Ω_b = 0.044`; `n̄_e,igm = f_igm n̄_e,bar` (Eq. 9) at a fixed
   `z̄ ≃ 0.20`; median of 61 posterior realisations per field (Eq. 10); 15 pc cm⁻³
   added for the first 50 `h⁻¹` Mpc, which ARGO excludes [src: Sect. IV.2].
4. **Haloes from narrow-field spectroscopy.** Each foreground halo gets a
   modified-NFW gas profile, `ρ_b(r) = f_gas (Ω_b/Ω_m) ρ_0(M_halo) / [y^{1−α}
   (y_0 + y)^{2+α}]` with `y = c r/r_200` (Eq. 11), `y_0 = α = 2`, truncated at
   `r_max = r_200`; stellar masses from CIGALE, halo masses from the mean
   stellar-to-halo relation, group members replaced by their group; the halo
   DMs are integrated along the sightline at each `b_⊥` [src: Sect. IV.3].
5. **Likelihood.** Gaussian in `DM_FRB` (Eq. 15) with a per-burst variance
   summing the ARGO, halo, host and Milky Way terms in quadrature (Eq. 16);
   the unknown host part is log-normal with `σ_* = 1.23` (0.53 in log₁₀ units
   rescaled) (Eq. 17). Free: `f_igm`, `f_gas`, `⟨DM_host^unk⟩` [src: Sect. V.1].
6. **Priors** (Table 4): `f_igm` (0, 1]; `f_gas` (0, 1] or "limited" (0, 0.7]
   from SIMBA haloes in the DR1 mass range; `ln⟨DM_host^unk⟩` [0, 6]; `f_d` flat
   [0.75, 0.95] or N(0.86, 0.02) [src: Sect. V.2].

### Step 2c. Two-point route: DM against foreground galaxies
<!-- key: step-2c-two-point-route-dm-against-foreground -->

The proposal (McQuinn 2013, arXiv:1309.4451): stack sightlines by impact
parameter to foreground galaxies. The source's own DM "does not contaminate the
signal" and precise source redshifts are not needed; localisation below 0.5′
is required to place a source within `r_vir` of a `10¹²` M☉ halo at `z = 0.5`.
The maximum-likelihood stacked excess has error
`σ[Δ̂_DM] ≈ √(σ̄²_DM / (N̄ n_DM))` for `n_DM` sightlines each meeting `N̄` haloes
in the bin [src: Sect. IV].

Three implementations:

| | Hussaini et al. 2025 | Shirasaki et al. 2026 | McCarty et al. 2026 |
|---|---|---|---|
| Statistic | (i) z-score of galaxy counts in a 5 Mpc cylinder against 500 random sightlines within ±5° of latitude, Pearson test (Eq. 5); (ii) mean excess DM in annuli of `b_⊥` | `ξ̂_gd(R)` = weighted mean of `ΔDM_s` over galaxy–FRB pairs minus the same around randoms (Eq. 4) | `ξ̂_{g,δDM}(R)`, pairs minus randoms (Eq. 4); also harmonic space and a CAP-filtered optical depth (Eqs. 12–13) |
| Per-burst quantity | cosmic DM excess | `ΔDM_s = DM_obs − DM_MW − ∫ c dz n̄_e(1+z)/H` (Eq. 5); host not subtracted | `δDM` = DM minus the mean to the burst redshift (Eq. 1) |
| Galaxies | WISE-PS1-STRM and Legacy Survey; `log M_* ≥ 10`, `0.01 < z < 0.5` | 2MASS (2MRS completeness weights) | DESI BGS, 27.3 million, three stellar-mass bins |
| Foreground cut | `z_gal ≤ 0.8 z_s`; `z_s > 0.10`; `b_⊥ < 50` Mpc; 2.5° from footprint edges | `z_s ≥ z_g + 0.05` (0.1 tested: same, noisier) | ≥ 100 comoving Mpc between galaxy and burst (removes about half the pairs); galaxies at `z > 0.1` |
| Bursts | DSA-110 and ASKAP | 133 localised (component separations N1, Nbeta, Y1, Ybeta) | 153 → 130 after cuts |
| Bins | annuli | 10 log bins, 0.01–100 `h⁻¹` Mpc; 5 kept (0.01–1) | 15 log bins, 0.3–30 comoving Mpc |
| Covariance | randomised pairs and jackknife | 40 jackknife regions; 300 DM shuffles as a shot-noise floor | jackknife, k-means patches, `N_patch = 150`, Hartlap correction |
| Model | TNG300-1 ray-traced catalogue | halo model: HOD for 2MASS × TNG300 electron profiles (Eqs. 20–22) | FLAMINGO variants; halo model with BCEmu baryonification |
| Place read | arXiv:2506.04186, Sects. II, IV | arXiv:2601.21336, Sects. 2.2, 3, 4 | arXiv:2608.11296, Sects. III, IV, V |

Stated reasons for the cuts: the galaxy redshift cut removes correlation
with the host's own environment, for example a host in a cluster [src:
arXiv:2506.04186, Sect. II.2]; Shirasaki et al. select background bursts so
that host DM cannot enter and note that the earlier work "did not pay attention
to this background selection" [src: arXiv:2601.21336, Sect. 2.2]; McCarty
et al. impose 100 Mpc "to eliminate any correlation with the FRB host and its
environment" [src: arXiv:2608.11296, Sect. IV.1]. McCarty et al. exclude
`|b| < 5°`, dwarf hosts with large host DM, "low-DM" localisations whose
identification depended on their DM, and associations below 90% confidence;
two further cuts are ad hoc (one burst at `z ≈ 2`; seven southern bursts with
`δDM > 300`) [src: Sect. III.1].

### Step 3. Turn the signal into gas physics
<!-- key: step-3-turn-the-signal-into-gas-physics -->

- **Halo model with simulated profiles** (Shirasaki et al.). Electron profiles
  are stacked in 35 bins of `11 < log M_500 < 14.5` and 30 radial bins of
  `0.01 < r/r_500 < 10` from TNG300-1 at `z = 0`, ignoring star-forming cells,
  which makes the TNG prediction a lower limit on the electron density; the
  null detection then sets `M_cut > 10¹²` M☉ (95%, `Δχ² = 4` over
  `0.01 < R < 0.2 h⁻¹` Mpc, where the boost factor is unity) in a
  `tanh(M/M_cut)` suppression of the gas mass [src: arXiv:2601.21336,
  Sects. 4.2, 5.2].
- **Simulation suite, amplitude-matched** (McCarty et al.). FLAMINGO predictions
  are scaled by an amplitude `A` fitted analytically on the last 7 bins
  (≳ 4 Mpc), which carry amplitude but "little information about feedback
  physics", and the feedback variants are then compared; `A` is close to 1 in
  every mass bin. Caveat in the paper: residual differences such as the mean
  halo mass of the sample are degenerate with feedback strength [src:
  arXiv:2608.11296, Sect. V.1].
- **Baryonification** (McCarty et al.). Free `log₁₀ M_c` ∈ [11, 15], `θ_ej` ∈
  [2, 8], `η` ∈ [0.05, 0.4]; `(μ, γ, δ)` fixed to (1.0, 2.5, 7.0); no free
  two-halo amplitude because it "tends to produce unphysical fits", the two-halo
  term being set by the well-known BGS bias [src: Sect. V.2]. The resulting
  power-spectrum suppression is an extrapolation: the measurement fixes the gas
  profile of this galaxy sample and baryonification generalises it to the
  `10¹²–10¹⁵` M☉ range that sets the total suppression [src: Sect. VI.1].
- **Comparison with kSZ.** DM converts to optical depth; the CAP-filtered
  `τ̂_FRB` (Eq. 13) is directly comparable to stacked kSZ, and is used to break
  the kSZ degeneracy between `τ` and `r/σ_v` (velocity reconstruction) or to
  constrain the velocity bias `b_v` [src: arXiv:2608.11296, Sects. II, IV.3].
  The kSZ side is in `cosmo-cmb-lss-cross-correlations`.

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### One-point, foreground or two-point
<!-- key: one-point-foreground-or-two-point -->

| Route | Needs | Buys | Costs | Place read |
|---|---|---|---|---|
| One-point shape | localised bursts, a simulated `P_cos(DM_IGM, DM_X)` | uses every burst; `f_IGM` and `f_X` at once | tied to one simulation's log-variances (30% error inflation); host model enters | arXiv:2409.16952, Methods |
| Foreground mapping | wide- and narrow-field spectroscopy per field | per-sightline `DM_igm` and `DM_halos`; separates the host (`⟨DM_host^unk⟩ ≈ 70` in every prior case) | 8 sightlines; `f_gas` weakly constrained, degenerate with `f_igm` through the `f_d` prior; halo extent fixed | arXiv:2402.00505, Sects. IV.3, VI |
| Two-point | many bursts behind a galaxy survey | insensitive to host and Milky Way DM; mass-binned profiles | few pairs at small `R`; DM selection can bias it (below) | arXiv:2601.21336; arXiv:2608.11296, Sect. VI.4 |
| IGM-only subsample | complete galaxy catalogue to `M_* = 10¹⁰` M☉, cluster catalogues | direct `f_IGM` | a lower limit: halo-free sightlines also cross less IGM | arXiv:2506.04186, Sect. IV.4 |

### Halo gas profile and extent
<!-- key: halo-gas-profile-and-extent -->

The mNFW form with `α = y_0 = 2` "is designed to mimic gas profiles in the
multi-phase CGM"; distinguishing radial profiles would "likely require future
samples of hundreds of localized FRBs", so mNFW is "a useful ansatz" [src:
arXiv:2410.24072, Sect. 4.2]. FLIMFLAM fixed `r_max = r_200`; extending profiles
to `2 r_200` "can double" `DM_halos`, but DR1 had too little power to fit the
extent [src: arXiv:2402.00505, Sect. IV.3]. The alternatives used in two-point
work are tabulated simulation profiles (TNG300) and baryonification (above).

### Prior on `f_gas` and `f_d`
<!-- key: prior-on-fgas-and-fd -->

In FLIMFLAM, moving from flat to Gaussian `f_d` changes results at the ~1%
level; the limited `f_gas` prior moves `f_gas` from 0.55 (+0.26/−0.29) to 0.44
(+0.18/−0.24) and `f_igm` from 0.59 to 0.63 (+0.09/−0.07) along the degeneracy;
the `f_igm`–`f_gas` degeneracy is "primarily set by the prior constraints on
the total amount of diffuse baryons" [src: arXiv:2402.00505, Sect. VI].

### Covariance for a sparse two-point measurement
<!-- key: covariance-for-a-sparse-two-point-measurement -->

Shirasaki et al. keep only bins where the jackknife error exceeds the
DM-shuffle error, because jackknife cannot represent scales larger than its
regions and shuffles give a robust shot-noise floor [src: arXiv:2601.21336,
Sect. 3.1]. McCarty et al. use 150 patches, many more than bins but each larger
than the largest scale; halving or doubling `N_patch` changes the SNR of the
`log M_* > 10` bin by about 1σ either way [src: arXiv:2608.11296, Sect. IV.1].
Bins are strongly correlated because each burst enters many pairs and bins
[src: arXiv:2608.11296, Sect. VI.1; arXiv:2506.04186, Sect. II.2].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| TNG300 reference partition | `f_IGM` = 0.827, `f_X` = 0.138 | Connor | arXiv:2409.16952 | Methods |
| DM cliff | no burst at `z > 0.1` with `DM_ex/z < 800` pc cm⁻³ | Connor | arXiv:2409.16952 | main text |
| Host DM | `μ_host` = 4.90 (+0.18/−0.20), `σ_host` = 0.53 (+0.16/−0.14); median 130 (+25/−23) pc cm⁻³ rest frame | Connor | arXiv:2409.16952 | main text |
| Massive-halo share (X-ray, SZ synthesis) | ICM 3.75 ± 0.5%; groups `10^12.7–10^14` M☉ 5.4 ± 1.0% | Connor | arXiv:2409.16952 | main text |
| Model-mismatch inflation | 30% on MCMC errors | Connor | arXiv:2409.16952 | main text |
| ARGO smoothing; realisations | `R = 0.7 h⁻¹` Mpc; 61 | FLIMFLAM DR1 | arXiv:2402.00505 | Sect. IV.2 |
| Milky Way halo | 40 ± 15 pc cm⁻³ | FLIMFLAM DR1 | arXiv:2402.00505 | Sect. IV.1 |
| Halo masses probed | mostly `10^11–10^12.5` M☉ | FLIMFLAM DR1 | arXiv:2402.00505 | Sect. IV.3 |
| CGM share | `f_cgm` = 0.20 (+0.10/−0.11) for `10^11–10^13` M☉ | FLIMFLAM DR1 | arXiv:2402.00505 | Sect. VI |
| Feedback reading | `f_igm ≈ 0.59` no feedback, ≈ 0.70 stellar, 0.85–0.87 AGN jets (SIMBA); jets disfavoured at 2σ | FLIMFLAM DR1 | arXiv:2402.00505 | Sect. VI |
| Pairs | 339 at `R < 0.1`, 2224 at `R < 1 h⁻¹` Mpc | 2MASS × 133 FRBs | arXiv:2601.21336 | Sect. 3.1 |
| Detection | `(S/N)²` = 9.44, 8.44, 11.8, 10.4 for 5 d.o.f. (p = 0.092–0.037): null | same | arXiv:2601.21336 | Sect. 3.3 |
| Gas suppression scale | `M_cut > 1 × 10¹²` M☉ (95%) | same | arXiv:2601.21336 | Sect. 5.2 |
| IGM-only subsample | 15 bursts at `z > 0.15`; `σ_MW = 0.1 DM_MW`, `σ_MWhalo = 15`, `σ_host ≈ 100/(1+z_s)`, `σ_X` = 10% | Hussaini | arXiv:2506.04186 | Sect. IV.4 |
| Mock survey power | 40 bursts give a moderate stacked detection in TNG300 | Hussaini | arXiv:2506.04186 | Sect. IV.3 |
| BCEmu priors | `log M_c` [11, 15], `θ_ej` [2, 8], `η` [0.05, 0.4] | McCarty | arXiv:2608.11296 | Sect. V.2 |
| Stacking forecast (2013) | localisation < 0.5′; `σ̄_DM = 200` pc cm⁻³ assumed; 10² sightlines sensitive to a top-hat to `r_vir`, 10³ to `2 r_vir`; **forecast** | McQuinn | arXiv:1309.4451 | Sect. IV |

## What goes wrong
<!-- key: what-goes-wrong -->

- **DM-dependent selection.** For 3000 simulated bursts at `0.3 ≤ z ≤ 0.4`
  in IllustrisTNG, the angular DM–galaxy cross-correlation is robust to host
  DM, optical follow-up selection and CHIME-like DM and scattering selection,
  but removing the 10% most dispersed bursts in a redshift shell biases the
  amplitude "by over 50%" at about 0.1° (Mpc scales) [src: Cheng et al. 2025,
  arXiv:2506.03258, abstract]. McCarty et al. quote the same study for a sharp
  600 pc cm⁻³ cut biasing by a factor of 2 or more, and cannot model the
  selection of their heterogeneous sample [src: arXiv:2608.11296,
  Sect. VI.4]. Test: rerun with and without high-`δDM` bursts (McCarty et al.
  find the amplitude unchanged when the seven cut bursts are restored, with
  more noise [src: same]).
- **Selection in the one-point route.** Redshift- and DM-dependent selection
  alter `p(DM, z)` but barely `p(DM_ex | z)`: biases ≲ 0.8σ for 10² bursts,
  possibly > 3σ for 10⁴ [src: Sharma et al. 2025, arXiv:2511.16850,
  abstract].
- **Scattering near galaxies and host misidentification.** The boost factor
  `B(R)` (Eq. 6), pairs around galaxies over pairs around randoms, flags both:
  `B > 1` for bursts physically associated with foreground galaxies, `B < 1`
  for bursts lost to pulse broadening in dense environments. It is unity at
  `R ≲ 0.1 h⁻¹` Mpc and departs moderately at `R ≳ 0.3` in the 2MASS analysis
  [src: arXiv:2601.21336, Sect. 3.2].
- **Missing rare systems at small separation.** With few pairs at small `R`,
  a sample can miss the rare massive haloes that dominate the signal and be
  biased low; offered as a possible cause of a dip in two bins [src:
  arXiv:2608.11296, Sect. VI.4].
- **Simulated variance of `p(DM | z)`.** Ray-tracing with redshift gaps between
  snapshots misestimates the DM variance, though means are about right [src:
  arXiv:2409.16952, Methods]; L2 gives the size from Konietzka et al. 2025.
- **Star-forming gas in simulated profiles.** Ignoring it gives a lower limit
  on the electron density; the TNG prediction already exceeds the data at
  small scales [src: arXiv:2601.21336, Sect. 4.2].
- **Photometric redshifts.** Scatter galaxy positions, more harmful for
  stacking in `b_⊥` than for cylinder counts [src: arXiv:2506.04186,
  Sect. V.3]; they change the inferred `r` "at the level of a few percent"
  [src: arXiv:2608.11296, Sect. VI.4].
- **Incomplete foreground catalogues.** Undetected low-mass haloes contaminate
  an "IGM-only" sample; Hussaini et al. carry a 10% `σ_X` term and restrict to
  `M_* > 10¹⁰` M☉ [src: arXiv:2506.04186, Sect. IV.4].
- **Validation suite used.** Jackknife on bursts and DSA-110-only subsample
  (Connor); flat or Gaussian `f_d` and limited `f_gas` priors (FLIMFLAM);
  `Δz` = 0.05 and 0.1, four DM component separations, boost factor
  (Shirasaki); `N_patch` variation, FLAMINGO amplitude on large scales
  (McCarty); TNG300 mock with matched sample size (Hussaini) [src: places
  above].

## Reading list
<!-- key: reading-list -->

- Foundation: McQuinn 2013, arXiv:1309.4451, Sect. IV — the stacking estimator
  and its error; why host DM drops out.
- Review: Glowacki & Lee 2024, arXiv:2410.24072, Sect. 4 — mNFW, `f_gas`
  convention, link to baryonic effects in weak lensing.
- Method/application: Connor et al. 2024, arXiv:2409.16952 — bivariate
  IGM–halo DM distribution calibrated on TNG300, DM cliff.
- Application: Khrykin et al. 2024, arXiv:2402.00505 — per-sightline foreground
  mapping with ARGO and mNFW haloes; prior sensitivity.
- Application: Hussaini et al. 2025, arXiv:2506.04186 — galaxy-count and
  impact-parameter correlations; IGM-only subsample.
- Application: Shirasaki et al. 2026, arXiv:2601.21336 — background selection,
  boost factor, null detection turned into a gas–halo limit.
- Application: McCarty et al. 2026, arXiv:2608.11296 — mass-binned DESI BGS
  cross-correlation, baryonification fit, CAP filter against kSZ.
- Critique: Cheng et al. 2025, arXiv:2506.03258 — selection biases in
  DM–galaxy cross-correlations.
- Critique: Sharma et al. 2025, arXiv:2511.16850 — selection effects on the
  conditional `p(DM_ex | z)`.

## Not verified
<!-- key: not-verified -->

- Table 1 of arXiv:2608.11296 (SNR per mass bin, significance against NFW,
  BCEmu posteriors) did not render as text; the headline significance is in
  L2 from the abstract.
- The body of Cheng et al. 2025 (arXiv:2506.03258) and of Sharma et al. 2025
  (arXiv:2511.16850) was not read; only their abstracts.
- The component-separation likelihood that produced the four DM estimates
  (Takahashi et al. 2025, cited by arXiv:2601.21336) was not read; no
  identifier recorded.
- The SIMBA baryon-fraction study used for the FLIMFLAM `f_gas` prior
  (Khrykin et al. 2024b) was not read.
- The value of `f_IGM ≥ 0.69` from the IGM-only subsample (L2) was not re-read
  in the body here.
