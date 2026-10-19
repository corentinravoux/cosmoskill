# f(R), screening and their astrophysical tests — cosmo-dark-energy-modified-gravity dossier

Scope: how a constraint on a screened fifth force is actually built in
each regime (cluster abundance with a modified mass function, galaxy
morphology with screening maps, scale-dependent growth in galaxy
clustering) and for the Vainshtein-screened nDGP model, with the choices
that set each bound, the neutrino degeneracy, and the tests that catch a
bias; for a reader about to run, compare or referee an `f(R)` or nDGP
constraint.
Snapshot: 2026-10-18.
From: Euclid 2025 review (arXiv:2512.09748), Sect. 5; DESI DR1 scale-dependent modified-gravity paper (arXiv:2604.26915).

Already in L2, not repeated here: the screening mechanisms and their
canonical references (`physics-and-methods.md#screening`); the KiDS-1000
and DESI DR1 `f(R)` analysis cards, including the DESI growth equation,
Hu–Sawicki map, flat prior on `abs(f_R0)` in [0, 10^-4] and the
nuisance reparameterisation
(`physics-and-methods.md#what-the-main-modified-gravity-analyses-did`);
the table of bounds by regime (`results.md#specific-models-and-screening`,
`open-questions.md#which-f-r-bound-is-the-bound`); the cluster-profile and
galaxy-noise caveats (`systematics.md#modified-gravity-non-linear-scales-bias-and`).
Non-linear power-spectrum predictions for `f(R)` (fitting formula, FORGE,
mgemu, e-MANTIS, ReACT) are in `deep/nonlinear-beyond-lcdm.md`; Euclid
`f(R)` and nDGP forecasts in `deep/forecasts-stage-iv.md`; cluster-count
systematics in general in `cosmo-clusters`.

Notation. `f_R = df/dR`; `f_R0` its background value today (Hu–Sawicki,
index `n`); `chi` the self-screening threshold of the Newtonian potential;
`Phi_N` a Newtonian potential (in units of `c^2`); `lambda_C` the Compton
wavelength (range) of the fifth force; `Delta G/G_N` the fractional
strength of the unscreened force; `r_c` the DGP crossover scale,
`Omega_rc = 1/(4 H0 r_c)`, and `1/sqrt(H0 r_c) = 2 sqrt(Omega_rc)`
[der: from the definition]. HMF: halo mass function.

## How it is done
<!-- key: how-it-is-done -->

### Regime 1. Cluster abundance with a modified mass function
<!-- key: regime-1-cluster-abundance-with-a-modified-mass -->

The common structure of the three analyses read (Cataneo et al. 2014,
arXiv:1412.0133; Artis et al. 2024, eRASS1, arXiv:2402.08459; Vogt et al.
2025, SPT nDGP, arXiv:2512.05819):

1. **Keep a GR-calibrated HMF and multiply it by a modified-to-GR ratio
   computed semi-analytically.**
   `n_Delta = (n^{f(R)}/n^{GR})|_ST × n_Delta|_Tinker` (arXiv:1412.0133,
   Eq. 10); eRASS1 uses the same structure with the ratio of
   Markovian multiplicity functions `f_k^{f(R)}/f_k^{GR}` of Hagstotz et
   al. 2019 applied to Tinker (arXiv:2402.08459, Eqs. 12–13, 20); SPT nDGP
   uses the ratio of Sheth–Tormen HMFs times Tinker (arXiv:2512.05819,
   Eqs. 15–18). Stated reason: N-body simulations of `f(R)` are too slow
   to sample parameter space, while the ratio "is well suited to quantify
   departure from GR" because modified gravity acts on collapse, not on
   the statistics of the field [src: arXiv:1412.0133, Sect. III;
   arXiv:2402.08459, Sect. 3.2]. In SPT nDGP the ratio is independent of
   the Sheth–Tormen form itself, which only sets the relative enhancement
   [src: arXiv:2512.05819, Sect. III.1].
2. **Compute the collapse threshold in the modified theory.**
   - Cataneo et al.: `delta_c = A [1 − B log10(1 + (Omega_m^-1 − 1)/(1 + z)^3)]`
     with (A, B) = (1.6865, 0.0123) for GR and (1.7063, 0.0136) for `f(R)`,
     the latter for forces enhanced by 4/3 everywhere (Eq. 12); the
     virial overdensity ratio is fixed to 74/94 (Eq. 13). The 4/3 values
     underestimate the effect for `abs(f_R0) ≳ 10^-5`, so the limits are
     conservative; the ratio is set to 1 wherever it falls below 1, which
     acts as a screening "much more efficient than the one predicted by
     simulations" [src: Sect. III].
   - eRASS1: mass- and redshift-dependent threshold
     `delta_c^{f(R)} = delta_c^GR × Delta(f_R0, M, z)` (Eqs. 17–19), a fit to
     spherical collapse with chameleon screening, `n = 1` frozen "for
     consistency with the HMF calibration" [src: Sects. 3.1–3.2].
   - SPT nDGP: `delta_c` and `Delta_vir` from the full spherical-collapse
     equation with the nDGP force (Eqs. 13–14); linear growth rescaled by
     `D^{nDGP}/D^{ΛCDM}` (Eq. 12); the semi-analytic ratio is then
     corrected against 49 BRIDGE N-body cosmologies by
     `R_BRIDGE/R_SAM = q~ (1/sqrt(H0 r_c) − 0.1)(z − 0.8) + 1` with
     `q~ = 0.06` (Eq. 19), which cuts the model–simulation variance by 26%
     [src: Sect. III.1]. The BRIDGE runs have massless neutrinos, so the
     calibration does not cover neutrino effects [src: same].
3. **Mass definitions.** HMFs calibrated at `M_200m` or `M_vir` are
   converted to the survey's `M_500c` or `M_200c` with an NFW profile and
   a concentration relation (Duffy et al. for eRASS1; `c_200 = 4` fixed in
   Cataneo et al., "negligible effect" for `c_200 ≳ 3`), neglecting `f(R)`
   effects inside the virial radius [src: arXiv:2402.08459, Sect. 3.2;
   arXiv:1412.0133, Sect. III].
4. **HMF uncertainty.** eRASS1 multiplies the HMF by
   `(s ln(M/10^14 M_sun) + q)` with `q ~ N(1, 0.5)`, `s ~ N(0, 0.5)`
   (Eq. 21), because GR HMFs differ by up to 10% between simulations and
   finders and its `f(R)` model differs from that of Cataneo et al. by up
   to 20% [src: Sect. 3.2].
5. **Mass calibration from lensing, kept in GR.** All three calibrate the
   observable–mass relation with weak lensing modelled as in GR. Reasons
   read: in `f(R)` the lensing mass equals the GR one up to effects of
   order `f_R0` (Schmidt 2010, cited) and geodesics change by
   `≲ 10^-4` [src: arXiv:1412.0133, Sect. IV.1; arXiv:2402.08459,
   Sect. 3.3]; in nDGP the lensing potential is unmodified (Eq. 9) and
   profile changes are "minor" [src: arXiv:2512.05819, Sects. III, IV.2].
   eRASS1 adds a screening argument: haloes above `10^{p_2} h^-1 M_sun`,
   `p_2 = 1.50 (log abs(f_R0) − log(1 + z)) + 21.6` (Eq. 32, after Mitchell
   et al. 2018), are fully screened; at `log abs(f_R0) = −5.25`, 95.4% of
   the sample lies above the screening mass [src: Sect. 3.3]. The ratio of
   lensing to X-ray (dynamical) masses is itself a fifth-force probe, but
   in Cataneo et al. it was "completely degenerate" with instrumental and
   astrophysical uncertainties [src: arXiv:1412.0133, Sect. IV.1].
6. **External data.** Cataneo et al. combine with CMB and gas-mass
   fractions; eRASS1 uses cluster abundance alone with no cosmological
   priors; SPT nDGP combines with Planck PR4 primary CMB because clusters
   alone cannot constrain the nDGP parameter (degeneracy with `A_s` and
   `Omega_m`) [src: arXiv:1412.0133, Sect. IV; arXiv:2402.08459, Sect. 5.2;
   arXiv:2512.05819, Sect. V.1].

### Regime 2. Galaxy morphology with screening maps
<!-- key: regime-2-galaxy-morphology-with-screening-maps -->

Desmond and Ferreira 2020, arXiv:2009.08743:

1. **Signal.** In an unscreened galaxy, gas and dark matter feel the fifth
   force but main-sequence stars self-screen (`chi ~ f_R0 ≲ 10^-6`), so
   the HI centroid moves from the optical centroid until the halo's
   restoring force balances the missing force on the stars:
   `G_N M(r_*)/r_*^2 = a_5 Delta G/G_N` (Eq. 14); the displaced disk
   develops a U-shaped warp `z(x) ≃ −a_5,z (Delta G/G_N^2) abs(x)^3/M(x)`
   (Eq. 15), summarised by `w_1` (Eq. 16) [src: Sect. III.1].
2. **Screening map.** A galaxy is screened if
   `abs(Phi_ext) + abs(Phi_in) > chi`, with `chi = (3/2) f_R0` in `f(R)` and
   self-screening `Phi_in = −V_vir^2` from abundance matching; the external
   potential and the fifth-force field `a_5` are sourced only by
   unscreened mass within `4 lambda_C`, from a halo catalogue plus a
   BORG-reconstructed density field. The map reaches 290 Mpc (2M++
   completeness), so with `lambda_C,max = 8 Mpc` test galaxies are kept to
   250 Mpc [src: Sect. IV.1.4].
3. **Likelihood.** For each galaxy and each of 21 `lambda_C` values in
   0.3–8 Mpc, 1000 Monte Carlo realisations of `r_*` and `w_1` at
   `Delta G/G_N = 1` are fitted with a Gaussian mixture (2–25 components,
   chosen by BIC), then rescaled with `Delta G/G_N`; each galaxy enters as
   `(1 − f_i)` screened plus `f_i` unscreened (Eqs. 30–31), with `f_i` the
   unscreened fraction of realisations [src: Sect. IV.3].
4. **Astrophysical noise.** Each term is convolved with a Gaussian of width
   `sigma_i`: proportional to distance for gas–star offsets (angular
   resolution of the Arecibo beam), constant for warps, both free and
   marginalised; chosen by BIC among constant, distance-dependent and both
   [src: Sect. IV.3]. Only disks with `b/a = 0.15` are used because `w_1`
   correlated with axis ratio "in a way that was difficult to model"
   [src: same]. Sampling with emcee, about 30 walkers, chains ≥ 50
   autocorrelation lengths [src: same].

### Regime 3. Scale-dependent growth in the galaxy power spectrum
<!-- key: regime-3-scale-dependent-growth-in-the-galaxy -->

Additions to the L2 card for Gonzalez et al. 2026, arXiv:2604.26915:

- **`k_max = 0.17` rather than 0.2 h/Mpc.** DESI found 0.2 optimal for
  the GR EFT analysis; the authors cut lower so that the screening
  non-linearities are "well accounted for by the EFT counterterms". Using
  0.2 would tighten the `f_R0` bound by 35%, and "most of the constraining
  power on the fifth-force scale comes from wavenumbers higher than"
  0.17 [src: Sect. 5, "Consistency and validation"].
- **`n` free.** `n = 1.41 ± 0.52` (full shape), `1.30 ± 0.51` (with BAO),
  supporting `n = 1`; a small degeneracy with `f_R0` relaxes the bound on
  the mediator mass [src: same].
- **Per-bin consistency.** Fits per DESI redshift bin agree; a bump away
  from zero in LRG1 is absent in neighbouring bins and shows no trend
  [src: same].
- **External data.** BBN, a wide `n_s` prior, compressed CMB
  (`theta_*`, `omega_b`, `omega_bc`, Eqs. 18–19) with a Planck `n_s`
  prior; DES-Y5 supernovae "as an illustrative comparison case rather
  than as a preferred baseline", with Dovekie, Pantheon+ and Union3
  explored [src: Sect. 3.2].

### Vainshtein screening: nDGP
<!-- key: vainshtein-screening-ndgp -->

- **Theory as fitted.** Normal-branch DGP with a dark-energy component
  tuned so that `H(a)` is ΛCDM; otherwise the bound on `r_c` "is
  dominated by geometric probes rather than the growth of structure".
  Sub-horizon, the brane-bending mode gives
  `nabla^2 Phi = 4 pi (1 + 1/(3 beta)) G delta rho` and an unmodified lensing
  potential (Eqs. 8–9), with `beta(a)` of Eq. 7: scale-independent linear
  growth, Vainshtein screening in dense regions
  [src: arXiv:2512.05819, Sect. III].
- **Galaxy clustering.** Piga et al. 2022, arXiv:2211.12523, fit BOSS DR12
  with the one-loop EFTofLSS; on synthetic and simulated data the
  posteriors are biased by the `Omega_rc`–`A_s` degeneracy, so `A_s` is
  fixed to the Planck value; `Omega_rc ≲ 0.65` (95%) with a flat prior on
  `log10 Omega_rc`, a bound that "depends strongly on the prior", and
  `≲ 0.2` from a Bayes-factor-based bound [src: abstract].
- **Clusters + CMB.** SPT (1005 clusters, `0.25 < z < 1.78`, DES Y3 lensing
  for 688, HST for 39) cannot constrain the nDGP parameter alone; Planck
  PR4 alone gives `1/sqrt(H0 r_c) < 1.62` (95%), the joint fit `< 1.41`
  (95%) with massive neutrinos [src: arXiv:2512.05819, abstract; Sects.
  V.1–V.2]. The PR4 limit depends on the Planck data set and likelihood
  [src: Sect. V.2].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Conservative or simulation-calibrated mass function
<!-- key: conservative-or-simulation-calibrated-mass -->

Cataneo et al. deliberately chose a threshold that underestimates the HMF
enhancement for `abs(f_R0) ≳ 10^-5` and a ratio floor that over-screens,
so their limit is conservative; they warn that entering
`abs(f_R0) ≲ 10^-5` needs a validated chameleon model [src:
arXiv:1412.0133, Sect. III]. eRASS1's mass-dependent threshold models
screening but carries a 20% model difference and free HMF amplitude and
slope priors [src: arXiv:2402.08459, Sect. 3.2]. SPT nDGP calibrates its
semi-analytic ratio on simulations, with a one-parameter correction
because simulation shot noise precludes a richer fit [src:
arXiv:2512.05819, Sect. III.1].

### Neutrinos: degenerate in one regime, not in another
<!-- key: neutrinos-degenerate-in-one-regime-not-in -->

In cluster counts massive neutrinos raise the collapse barrier: for
`Sum m_nu = 0.3 eV` the barrier is indistinguishable from GR at
`log abs(f_R0) = −5` (Hagstotz et al. 2019, as cited); freeing the mass
relaxes the eRASS1 limit from −4.31 to −4.12 [src: arXiv:2402.08459,
Sect. 5.2]. In DESI DR1 full shape at `k_max = 0.17 h/Mpc` the degeneracy
is small: `Sum m_nu < 0.533 eV` (GR) against `< 0.589 eV` (MG), about 10%
looser, and `f_R0 < 2.60 × 10^-5` with free neutrino mass against
`2.52 × 10^-5` without, 3% [src: arXiv:2604.26915, Sect. 6, Eqs. 22–24].
A paper quoting an `f(R)` bound should say whether `Sum m_nu` was free.

### Cosmological or astrophysical regime
<!-- key: cosmological-or-astrophysical-regime -->

The galaxy-morphology analysis assumes ΛCDM for cosmology because
`f_R0 ≈ 10^-8` has "only minute effect" on expansion and growth, "what
makes astrophysical tests of screened fifth forces far more powerful than
cosmological ones" [src: arXiv:2009.08743, Sect. VI.1]. Its costs are
the restoring-force model (inner slope `beta` varied 0–1.5: at most a
factor 2 on `Delta G/G_N`) and the noise model (both noise terms instead
of one: at most 50%) [src: Sects. IV.3, VI.1]. Cluster abundance needs no
galaxy-formation model but is limited to `abs(f_R0) ≳ 10^-5`, where
massive clusters are not screened [src: arXiv:2402.08459, Sect. 3.1:
screening of massive clusters for `abs(f_R0) < 10^-5`, since `Phi_N ~ 10^-5`].

### Prior on the model parameter
<!-- key: prior-on-the-model-parameter -->

The nDGP BOSS bound moves from 0.65 to 0.2 in `Omega_rc` between a
log-flat-prior credible limit and a Bayes-factor-based limit [src:
arXiv:2211.12523, abstract]; the DESI `f(R)` bound is quoted with a flat
prior on `abs(f_R0)`, a log prior shifting results low (L2 card). For
one-sided parameters near a boundary, quote the prior with the limit.

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| eRASS1 `log10 abs(f_R0)` (95%), massless ν | < −4.31 (abstract, Eq. 50); Table 2 prints < −5.12 | clusters only, no priors | arXiv:2402.08459 | abstract; Sect. 5.2, Table 2 |
| Same, `Sum m_nu` free | < −4.12; `Sum m_nu < 0.44 eV` (text), < 0.39 eV (Table 2) | — | arXiv:2402.08459 | Sect. 5.2, Eqs. 51–52; Table 2 |
| eRASS1 cosmology with `f(R)` | `Omega_m = 0.28 ± 0.02`, `sigma8 = 0.89 ± 0.04`, `S8 = 0.85 ± 0.04` | — | arXiv:2402.08459 | Eq. 49 |
| HMF systematic priors | `q ~ N(1, 0.5)`, `s ~ N(0, 0.5)` | eRASS1 | arXiv:2402.08459 | Eq. 21 |
| Cluster sample, Cataneo et al. | 224 clusters (BCS, REFLEX, Bright MACS), 94 with follow-up, 50 with lensing masses | — | arXiv:1412.0133 | Sect. IV.1 |
| Collapse threshold parameters | GR (1.6865, 0.0123); `f(R)` (1.7063, 0.0136); `Delta_vir` ratio 74/94 | — | arXiv:1412.0133 | Eqs. 12–13 |
| nDGP HMF correction | `q~ = 0.06`; variance 0.0073 → 0.0058 | 49 BRIDGE cosmologies | arXiv:2512.05819 | Sect. III.1, Eq. 19 |
| nDGP, Planck PR4 / + SPT clusters | `1/sqrt(H0 r_c) < 1.62` / `< 1.41` (95%) | massive ν for the joint | arXiv:2512.05819 | Eq. 31; abstract |
| Same in `Omega_rc` | < 0.66 / < 0.50 | — | [der: `Omega_rc = (x/2)^2`] | — |
| nDGP, BOSS DR12 EFT | `Omega_rc ≲ 0.65` (log prior), `≲ 0.2` (Bayes-factor bound), `A_s` fixed to Planck | — | arXiv:2211.12523 | abstract |
| SPT nDGP effect on `sigma8` | error +58%, `Omega_m` error +7%, relative to νΛCDM | clusters + WL | arXiv:2512.05819 | Sect. V.1 |
| Galaxy morphology range | `lambda_C` 0.3–8 Mpc; `chi` 1.3 × 10^-8 to 9.4 × 10^-6 | — | arXiv:2009.08743 | Table 1 |
| Restoring-force and noise systematics | ≤ ×2 (`beta` 0–1.5); ≤ 50% (noise model) | — | arXiv:2009.08743 | Sects. VI.1, IV.3 |
| DESI `k_max` | 0.17 h/Mpc baseline; 0.2 gives a 35% tighter `f_R0` bound | DR1 full shape | arXiv:2604.26915 | Sect. 5 |
| DESI ν degeneracy | `Sum m_nu < 0.533` (GR), `< 0.589 eV` (MG); `f_R0 < 2.60 × 10^-5` vs `2.52 × 10^-5` | DESI FS + BAO + BBN + `n_s10` | arXiv:2604.26915 | Eqs. 22–24 |
| Free Hu–Sawicki index | `n = 1.41 ± 0.52` (FS), `1.30 ± 0.51` (FS + BAO) | — | arXiv:2604.26915 | Sect. 5 |

The eRASS1 abstract and Eq. 50 give −4.31 while Table 2 of the same
version gives −5.12 for the massless case; the sibling `cosmo-clusters`
quotes −4.31. Until the discrepancy is resolved at source, quote −4.31
with the section and note the table value.

## What goes wrong
<!-- key: what-goes-wrong -->

| Failure | How it shows | Test or fix | Source |
|---|---|---|---|
| GR HMF uncertainty mistaken for a fifth force | enhanced counts at high mass | free HMF amplitude and slope; compare HMF models | arXiv:2402.08459, Sect. 3.2 |
| Semi-analytic HMF ratio off | ~10% scatter against simulations | calibrate on MG N-body runs (BRIDGE) | arXiv:2512.05819, Sect. III.1 |
| Neutrino mass fixed | `f(R)` limit too tight in clusters | free `Sum m_nu` | arXiv:2402.08459, Sect. 5.2 |
| Degeneracy with `A_s` or `sigma8` | biased posteriors on synthetic data (BOSS nDGP); unconstrained nDGP from clusters alone | fix `A_s` or add CMB; validate on mocks | arXiv:2211.12523; arXiv:2512.05819, Sect. V.1 |
| Lensing–dynamical mass difference ignored | mass calibration biased if the fifth force acts on the dynamics | calibrate masses with lensing; check screening mass | arXiv:1412.0133, Sect. III footnote and IV.1; arXiv:2402.08459, Sect. 3.3 |
| Over-efficient screening in the model | limits too loose but conservative | state it; validate chameleon modelling before using `abs(f_R0) < 10^-5` | arXiv:1412.0133, Sect. III |
| Screening at high `k` in clustering | bias if `k_max` too high | lower `k_max`; per-bin fits; free `n` | arXiv:2604.26915, Sect. 5 |
| Astrophysical noise in morphology | spurious offsets or warps | free noise terms; random-forest feature test; hydrodynamical mocks (Horizon-AGN, TNG) | arXiv:2009.08743, Sects. IV.3, VI.1 |
| Incomplete density field in the screening map | wrong screening classification at large distance | cut the test sample 5 `lambda_C,max` inside the map edge | arXiv:2009.08743, Sect. IV.1.4 |
| MG calibration without neutrinos | HMF correction does not cover νΛCDM | flag; extend simulations | arXiv:2512.05819, Sect. III.1 |

Referee checks specific to this dossier: which HMF ratio and which
collapse threshold; the mass definition conversion; whether lensing
masses are assumed GR and why; whether `Sum m_nu` is free; the prior on
`f_R0` or `Omega_rc`; for clustering, `k_max` and its justification; for
morphology, the screening-map extent and the noise model; for nDGP, the
background (ΛCDM-matched or not).

## Reading list
<!-- key: reading-list -->

- Method, clusters: Cataneo et al. 2014, arXiv:1412.0133 — modified-to-GR
  HMF ratio, conservative threshold, lensing-calibrated masses.
- Application, clusters: Artis et al. 2024, arXiv:2402.08459 — eRASS1,
  mass-dependent threshold, screening mass, neutrino degeneracy.
- Application, Vainshtein: Vogt et al. 2025, arXiv:2512.05819 — nDGP HMF
  with BRIDGE correction, SPT + Planck PR4.
- Application, galaxy clustering: Piga et al. 2022, arXiv:2211.12523 —
  BOSS EFT nDGP, `A_s` degeneracy, prior dependence.
- Application, galaxies: Desmond and Ferreira 2020, arXiv:2009.08743 —
  screening maps, gas–star offsets and warps, noise model.
- Application, scale-dependent growth: Gonzalez et al. 2026,
  arXiv:2604.26915 — `k_max`, free `n`, neutrino test.
- Foundation: Hu and Sawicki 2007, arXiv:0705.1158; Khoury and Weltman
  2003, arXiv:astro-ph/0309300 (in L2).
- Non-linear spectra and forecasts: `deep/nonlinear-beyond-lcdm.md`,
  `deep/forecasts-stage-iv.md`.

## Not verified
<!-- key: not-verified -->

- Hagstotz et al. 2019 (the eRASS1 HMF formalism) and Mitchell et al. 2018
  (screening mass): described only as eRASS1 cites them.
- The source of the eRASS1 Table 2 / text discrepancy (−5.12 against
  −4.31; 0.39 against 0.44 eV); a later arXiv version may correct one.
- The BOSS nDGP pipeline body (scale cuts, priors) beyond the abstract.
- Vainshtein constraints on cubic or quartic Galileons and on other
  named Horndeski models (JBD, K-mouflage) were not read.
- Cluster lensing-versus-kinematics tests (arXiv:2604.23631) beyond L2.
