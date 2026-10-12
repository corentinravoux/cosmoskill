# Physics and methods — standard sirens, fast radio bursts, lensed transients, GW × LSS

Scope: what is measured, the estimators and likelihoods in use, the conventions that differ between groups, and the public codes.
Snapshot: 2026-10-07 (suite date; literature searches run 2026-10-10)

Flags: `[src]` read this session in the cited paper; `[sec]` from a named secondary
source; `[der]` derived here. Equations without a flag are textbook definitions.

## 1. Standard sirens: the observable

### 1.1 What the waveform gives

For a compact binary in the inspiral phase the two polarisation amplitudes are

```
h_+  = (4 / d_L) (G M_z / c^2)^(5/3) (pi f / c)^(2/3) (1 + cos^2 i)/2 cos(Phi)
h_x  = (4 / d_L) (G M_z / c^2)^(5/3) (pi f / c)^(2/3)  cos i          sin(Phi)
M_z  = (1 + z) M_c ,   M_c = (m1 m2)^(3/5) / (m1 + m2)^(1/5)
```

The frequency evolution `df/dt` fixes the redshifted chirp mass `M_z`, so the amplitude
gives the luminosity distance `d_L` with general relativity as the only calibrator. Three
consequences organise the whole field.

1. **No redshift.** Gravity is scale-free: there is "a perfect degeneracy between the
   source masses and redshift" (Farr et al. 2019, arXiv:1908.09084). Every method below
   is a way to obtain `z` from something else.
2. **Distance–inclination degeneracy.** The amplitude depends on `d_L` and on the
   inclination `i` together; only the ratio of the two polarisations separates them, and
   a detector network measures that ratio poorly for nearly face-on binaries. For
   GW170817 this degeneracy, and not the detector noise, dominated the first H0 error
   (arXiv:1806.10596 abstract).
3. **Absolute scale.** No distance ladder enters. The systematic floor is set by the
   detector strain calibration and the waveform model (systematics file, §3).

The idea goes back to Schutz (1986), as cited in arXiv:2212.08694 and arXiv:1807.05667.
Holz & Hughes 2005 (arXiv:astro-ph/0504616) treat LISA massive black-hole binaries as
standard sirens with 1–10% distance accuracy, limited by pointing error and by weak
lensing [src]. Chernoff & Finn 1993 (arXiv:gr-qc/9304020) is the early treatment with
detector noise and without counterparts.

Entry points: Palmese & Mastrogiovanni 2025 (arXiv:2502.00239) and Zhao, Zhu & Lu 2026
(arXiv:2605.08595) for sirens; Glowacki & Lee 2024 (arXiv:2410.24072) and Wang et al.
2026 (arXiv:2606.22390) for FRB cosmology. All four were read at abstract level only.

### 1.2 From distance to cosmology

```
d_L(z) = (1 + z) c  Int_0^z dz' / H(z')                 (flat background)
c z_obs = H0 d + v_p        (z << 1; v_p = radial peculiar velocity of the host)
```

At `z << 1` a siren measures H0 alone. At `z ~ 0.3–1`, where the binary black holes of
the current catalogues lie, it measures `H(z)` near a pivot redshift, and quoting H0
requires a background model: Pierra et al. 2025 (arXiv:2511.11795) find the GWTC-4.0
dark-siren constraint is most data-driven at `z = 0.44` and that the flat-ΛCDM H0 "is
strongly affected by the cosmological model assumption" [src]. Farr et al. 2019 and
Mancarella et al. 2021 (arXiv:2112.05728) place the pivot at `z ≈ 0.8` for design
sensitivity [src].

### 1.3 Four routes to the redshift

| Route | Redshift information | Works for | First applied | Section |
|---|---|---|---|---|
| Bright siren | spectroscopic redshift of the host of an electromagnetic counterpart | BNS, NSBH; claimed for BBH in AGN discs | GW170817, arXiv:1710.05835 | §2 |
| Dark siren, galaxy catalogue | redshift distribution of the galaxies in the localisation volume | well-localised events inside a complete catalogue | arXiv:1807.05667, arXiv:1901.01540 | §3 |
| Spectral siren | features of the source-frame mass spectrum, seen redshifted | whole BBH population | arXiv:2111.03604 | §4 |
| Cross-correlation | clustering of sirens with galaxies of known redshift | large samples | arXiv:2203.03643, arXiv:2512.15380 | §6 |

Current LVK analyses combine the second and third in one hierarchical likelihood and
multiply by the GW170817 bright-siren posterior (arXiv:2509.04348, arXiv:2605.27227).

### 1.4 Modified gravitational-wave propagation

If the friction term of the tensor propagation equation differs from general
relativity, the distance inferred from the GW amplitude differs from the electromagnetic
luminosity distance. The parametrisation used by the LVK and by Finke et al. 2021
(arXiv:2101.12660) and Mancarella et al. 2021 (arXiv:2112.05728) is

```
d_L^GW(z) / d_L^EM(z) = Xi_0 + (1 - Xi_0) / (1 + z)^n ,     Xi_0 = 1 in general relativity
```

The original reference of this form was not fetched. Because sirens only measure `d_L^GW`, `Xi_0` is degenerate with
H0 and with the population model: analysing a `Xi_0 = 1.8` universe with general
relativity biases the mass scales, H0 and the merger rate (arXiv:2112.05728) [src].
Theory context belongs to `cosmo-dark-energy-modified-gravity`.

## 2. Bright sirens

### 2.1 Likelihood

The LVC 2017 measurement (arXiv:1710.05835) is the template. With `x_GW` the strain
data, `v_r` the measured recession velocity of the host group and `<v_p>` the estimated
peculiar velocity,

```
p(H0 | x_GW, v_r, <v_p>) ∝ p(H0) / N_s(H0)
     × Int  p(x_GW | d, cos i) p(v_r | d, v_p, H0) p(<v_p> | v_p) p(d) p(v_p) p(cos i)
            dd dv_p dcos i
```

`N_s(H0)` is the selection normalisation (§5). Choices that move the answer:

- **Distance prior.** Volumetric (`p(d) ∝ d^2`) or uniform in `d_L`. Yang et al. 2026
  (arXiv:2606.30504) re-ran GW170817 under both: the weighted median moves from 77.6 to
  87.6 km/s/Mpc and `P(H0 > 120)` from 0.017 to 0.159 while the binned maximum stays at
  70.5; post-hoc reweighting of the baseline samples recovers only about 17% of that
  shift because the volumetric run undersamples a low-`d_L`, high-inclination mode
  [src]. A prior study must re-sample, not reweight.
- **H0 prior.** Flat (arXiv:1710.05835) or flat-in-log (arXiv:1908.06060). The same
  event gives 70.0 (+12.0/−8.0) under the first and 68.7 (+17.5/−8.3) under the second
  convention and interval definition [src].
- **Summary statistic.** Maximum a posteriori with highest-density interval (LVC 2017,
  GWTC-3 era) or median with symmetric interval (GWTC-4.0 onwards). The posteriors are
  skewed to high H0, so the two differ by several km/s/Mpc.

### 2.2 Breaking the inclination degeneracy with electromagnetic data

| Information | How it enters | Reference |
|---|---|---|
| VLBI superluminal motion of the jet centroid | prior on viewing angle (about 20°, opening angle < 5°) [src] | arXiv:1806.09693, arXiv:1806.10596 |
| Afterglow light curve (radio, optical, X-ray, to ~3.5 yr) | joint fit of jet structure and viewing angle | arXiv:2305.19914 |
| All VLBI data fitted in the visibility plane with hydrodynamical jet models | viewing angle 16.8°–19.2°, `d_L` and H0 fitted directly [src] | arXiv:2605.11437 |
| Kilonova and gamma-ray burst with a nuclear equation-of-state prior | joint multi-messenger inference | arXiv:2002.11355 |
| Independent distance to the host (surface-brightness fluctuations) | pins `d`, hence `i ≳ 137°` [src]; no longer a ladder-free H0 | arXiv:1801.06080 |

Every row replaces a GW-only uncertainty by an astrophysical model of the jet or the
ejecta; a viewing-angle bias above about 10° gives more than 3% on H0
(arXiv:2006.02779) [src].

### 2.3 The recession velocity of the host

At 40 Mpc the peculiar velocity is of order 10% of the recession velocity
(arXiv:1710.05835, Methods) [src], so the velocity model is part of the estimator. The
approaches in the literature, in order of appearance:

| Approach | Input | Result for NGC 4993 | Reference |
|---|---|---|---|
| Gaussian-kernel average of a direct-distance catalogue | 6dFGSv Fundamental Plane, kernel 8 h⁻¹ Mpc, 10 galaxies within one kernel width [src] | `<v_p>` = 310 ± 69 km/s, error inflated to 150 km/s [sec: arXiv:1909.00587 §3.2] | arXiv:1710.05835 |
| Marginalise over the kernel scale | same kind of catalogue | a 200 km/s shift moves H0 by about 4 km/s/Mpc [src] | arXiv:1909.09609 |
| Group redshift plus several catalogues, Bayesian model averaging; likelihood written in log-distance ratio | CF3, 2MTF, 6dFGSv; several group catalogues | catalogues disagree by more than their errors | arXiv:1909.00587 |
| Reconstructed non-linear field plus virial term | BORG on 2M++ | mean 373 km/s, σ ≈ 130 km/s (82 field, 100 virial) [src] | arXiv:1909.08627 |
| Dedicated spectroscopy of the environment | DESI: 39 group members, Fundamental Plane distances | H0 = 70.9 or 73.4 depending on the velocity source [src] | arXiv:2512.08818 |
| Full covariance of the velocity field between sirens | simulations | error up to ×2 within 50 Mpc [src] | arXiv:2509.03101 |

The general Bayesian model of Howlett & Davis 2019 "works more closely with observed
quantities from redshift and peculiar velocity surveys" (log-distance ratio rather than
velocity), for the reason given in `cosmo-peculiar-velocities`: errors are Gaussian in
log-distance, not in velocity. Linear-theory reconstruction from 2M++ (Carrick et al.
2015, arXiv:1504.04627; `β* = 0.431 ± 0.021` [src]) and the BORG velocities shipped with
GLADE+ for galaxies within `z = 0.05` (arXiv:2110.06184) are the off-the-shelf options.
Stiskalek et al. 2025 (arXiv:2502.00121) rank reconstructions against direct distances
and find the non-linear BORG field best at `z ≲ 0.05` [src]; that paper names
gravitational-wave cosmology as an application. Velocity-field methods, bulk flows and
the growth-rate use of the same data are in `cosmo-peculiar-velocities`.

## 3. Dark sirens: galaxy-catalogue method

### 3.1 Principle

Each galaxy in the three-dimensional localisation volume is a candidate host. The
redshift prior along a line of sight `Ω` is

```
p(z | Ω, Λ) ∝ [ Σ_g w_g(L_g) p(z | z_g, σ_g) ]_in catalogue + [ 1 − f(z, Ω) ] p_miss(z | Λ)
w_g ∝ L_g^ε
```

`f(z, Ω)` is the completeness, `p_miss` the model for galaxies below the flux limit, and
`ε` the host-weighting exponent (`ε = 0` uniform, `ε = 1` luminosity-weighted; the
notation of arXiv:2605.27227). The information comes from structure in the galaxy
redshift distribution; a featureless `p(z)` returns the prior.

Formal references: Del Pozzo 2011 (arXiv:1108.1317) for the Bayesian formulation;
Gray et al. 2019 (arXiv:1908.06050) for the in-catalogue/out-of-catalogue split and the
mock data challenge; Gair et al. 2022 (arXiv:2212.08694) for the consolidated
derivation and for the common errors (mismodelled selection, inconsistent priors) that
produce a spurious bias.

### 3.2 Design choices that differ between analyses

| Choice | Options in use | References |
|---|---|---|
| Completion of the missing galaxies | homogeneous in comoving volume; multiplicative; clustering-informed; Gaussian process along the line of sight | arXiv:2310.08991, arXiv:2608.24992 |
| Depth actually needed | full luminosity function, or only the brightest 1% when faint galaxies cluster around bright ones | arXiv:2511.04786 |
| Host weighting | none, B, K or r-band luminosity, stellar mass, star-formation rate; fixed or inferred | arXiv:1807.05667, arXiv:2405.14818, arXiv:2608.26307, arXiv:2609.04991 |
| Galaxy redshift errors | none, Gaussian, modified Lorentzian, full photo-z PDF from a neural network | arXiv:2302.12037, arXiv:2404.16092 |
| Population model | fixed (GWTC-3 catalogue result), or inferred jointly | arXiv:2111.03604, arXiv:2308.02281 |
| Event selection | all events above a detection threshold, or the best-localised subset ("golden" and "silver" sirens) | arXiv:2111.06445, arXiv:2512.21729 |
| Redshift prior implementation | pre-computed on a pixel grid, or sampled so that host-population parameters can vary | arXiv:2609.04991 |

Two families exist: the LVK pipelines use every event above threshold with a
completeness correction; the DES/DESI-Legacy/DELVE line (arXiv:1901.01540 to
arXiv:2603.20195, results file §2.2) multiplies single-event posteriors of the
best-localised events inside a deep photometric footprint.

## 4. Dark sirens: spectral (population) method

The detector measures `m_det = (1 + z) m_src`. If the source-frame mass spectrum has a
feature at a known or self-calibrated scale, the observed position of that feature as a
function of `d_L` traces `z(d_L)`.

- Origin: Taylor, Gair & Mandel 2011 (arXiv:1108.5161) with the narrow neutron-star mass
  function; Farr et al. 2019 (arXiv:1908.09084) with the pair-instability cutoff near
  45 M☉.
- "Spectral sirens": Ezquiaga & Holz 2022 (arXiv:2202.08240) argue for using the whole
  spectrum and list five features (both edges of the pair-instability gap, both edges of
  the neutron-star–black-hole gap, the minimum neutron-star mass) [src].
- Features seen in data: a peak near 10 M☉ and a change of slope near 35 M☉ in GWTC-5.0
  (arXiv:2605.27226) [src]; peaks near 9 and 32 M☉ and a roll-off above 46 M☉ in O3, the
  32 M☉ peak correlating most strongly with H0 (arXiv:2410.07416) [src]; a further scale
  at 63.3 ± 4.8 M☉ claimed in GWTC-4.0 (arXiv:2601.03257) [src].
- Mass models: parametric families (the LVK fiducial in GWTC-5.0 is called FullPop-4.0,
  with a three-peak variant and a BBH-only multi-peak model; arXiv:2605.27227 §4.1),
  non-parametric (arXiv:2404.02210), and normalising flows trained on population-synthesis
  catalogues (arXiv:2603.15332).

The method assumes the features do not move with redshift, or that their motion is
modelled. That assumption is the dominant systematic (systematics file, §5).

## 5. Hierarchical likelihood and selection function

All dark-siren analyses use the inhomogeneous-Poisson population likelihood

```
L({x_i} | Λ) ∝ Π_i [ Int L(x_i | θ) p_pop(θ | Λ) dθ ] / ξ(Λ)^N
ξ(Λ) = Int p_det(θ) p_pop(θ | Λ) dθ
```

with `Λ` holding H0, Ω_m, the mass, spin and rate-evolution parameters and, when used,
`Xi_0`. `ξ(Λ)` is the detectable fraction, estimated from injection campaigns. The
derivation is Mandel, Farr & Gair 2018 (arXiv:1809.02063); general treatment of
selection in hierarchical models is in `cosmo-statistics-inference`. Points specific to
sirens:

- `ξ` depends on H0, because the detection horizon in `d_L` is fixed while the
  population is specified in `z`. Dropping this term is the classic source of bias
  (arXiv:2212.08694).
- For bright sirens the electromagnetic selection (is the counterpart found?) enters as
  well (arXiv:1908.06050, arXiv:2006.02779).
- Bright and dark sirens come from one underlying population; a self-consistent joint
  framework is given by Colombo et al. 2026 (arXiv:2609.12053), who find that treating
  them as independent does not bias H0 in the next runs but biases the low-mass end of
  the mass spectrum [src].
- Priors in use for H0: uniform on [20, 140] (DES-line papers), uniform on [10, 220]
  (arXiv:1807.05667), uniform on (10, 200) (arXiv:2605.27227, Table of §4.1) [src].
  Combining posteriors from different papers requires dividing out each prior.
- Blinding: LVK H0 analyses are not blinded. Blinded mock data challenges exist for the
  spectral method (arXiv:2412.14244, arXiv:2604.26273). Lensed-supernova measurements are
  blinded (§8).

## 6. Siren × large-scale-structure cross-correlation

Sirens trace the matter field with a bias `b_GW`. Their angular positions in shells of
`d_L` correlate with galaxies in shells of `z` only where the two shells overlap in
physical space, so the correlation is maximal on the true `d_L(z)` relation.

- Proposal with lensing magnification included: Oguri 2016 (arXiv:1603.02356).
- Three-dimensional formulation with `b_GW(z)` as nuisance: Mukherjee et al. 2020
  (arXiv:2007.02943); first application to GWTC-3 with 2MPZ and WISE×SuperCOSMOS
  (arXiv:2203.03643).
- Insensitivity to catalogue incompleteness: Bera et al. 2020 (arXiv:2007.04271), who
  also argue that an analysis that does not use clustering explicitly is
  prior-dominated.
- "Peak Sirens": find the peak of the 3D angular cross-spectrum `C_ℓ(z, D_L)` between
  galaxy redshifts and siren luminosity distances; H0 follows from the position of the
  peak, and the same measurement bounds the gravitational-wave bias [src]. First
  detection on data: de Matos et al. 2025 (arXiv:2512.15380).
- Joint analysis with a 3×2pt data vector: Andrade-Oliveira et al. 2026
  (arXiv:2601.04774).
- Requirements for a percent-level H0 (forecast): `σ_dL = 0.1 d_L`, at least 5000 dark
  sirens and good localisation (arXiv:2510.19931) [src].

A field-level variant grids the sirens in `d_L` space and compares the resulting density
field with a galaxy field in redshift space. The `flip` package (arXiv:2501.16852)
contains a density data vector for that purpose, `GWDensMesh` in
`flip/data_vector/gw_vectors.py` [src: public flip repository, `main` branch, class
present on 2026-10-12]. How it is built was read in a development copy and is listed
under "Not verified".

## 7. Fast radio bursts: dispersion measure–redshift relation

### 7.1 Budget

```
DM_obs = DM_MW,ISM + DM_MW,halo + DM_cosmic(z) + DM_host / (1 + z)

<DM_cosmic>(z) = (3 c H0 Ω_b / 8 π G m_p) Int_0^z  f_d(z') χ_e(z') (1 + z') / E(z') dz'
χ_e = Y_H + Y_He / 2   (≈ 7/8 after helium reionisation)
```

`f_d` is the fraction of baryons in diffuse ionised gas (written `f_IGM` when halo gas
is counted separately). The mean relation is called the Macquart relation after
Macquart et al. 2020 (arXiv:2005.13161). Earlier formulations: Deng & Zhang 2013
(arXiv:1401.0059) for `Ω_b f_IGM`; McQuinn 2013 (arXiv:1309.4451) for the probability
distribution of `DM(z)` and its sensitivity to where halo baryons sit.

### 7.2 What is degenerate with what

`<DM_cosmic> ∝ Ω_b H0 f_d`. Written with the physical baryon density,
`<DM_cosmic> ∝ (Ω_b h²) f_d / h` [der: `Ω_b H0 = (Ω_b h²) × 100 / h`]. An H0 from FRBs
therefore requires an external `Ω_b h²` (nucleosynthesis or CMB) and an assumed `f_d`;
conversely a baryon census requires H0. Jahns-Schindler & Spitler 2025
(arXiv:2508.14434) state the degeneracy and propose FRBs with gravitational-wave
distances to break it without early-universe priors. A higher H0 predicts a lower DM at
fixed `z`.

### 7.3 Scatter and the likelihood

The scatter of `DM_cosmic` at fixed `z` is non-Gaussian, skewed to high DM by
intersected haloes. Two descriptions are in use:

- the one-parameter form `σ_DM = F z^(−0.5)` with fluctuation parameter `F` (Baptista
  et al. 2023, arXiv:2305.07022); `F` is degenerate with H0 [src];
- distributions measured in hydrodynamical simulations. Konietzka et al. 2025
  (arXiv:2507.07090) show that sparse snapshot sampling in earlier IllustrisTNG work
  misestimated the standard deviation and higher moments of `p(DM | z)` by more than
  50% and that the log-normal form is a poor match [src].

`DM_host` is modelled as a distribution, log-normal in most analyses, whose median
and width are fitted (arXiv:2208.00819). The Milky Way halo term is taken from models:
50–80 pc cm⁻³ to 200 kpc (Prochaska & Zheng 2019, arXiv:1901.11051) [src].

Two likelihood styles exist. The first fits localised bursts only, `p(DM | z)`
(arXiv:2104.04538, arXiv:2108.00581, arXiv:2507.18946). The second forward-models the
survey — luminosity function, beam shape, burst width, population evolution — and fits
`p(z, DM)` of localised and unlocalised bursts together (James et al. 2022,
arXiv:2208.00819; the `zDM` code). The second style returns larger H0 errors because it
marginalises over the energy function and `DM_host` [src]. Unlocalised bursts alone
constrain H0 weakly through the shape of the DM distribution (arXiv:2604.03769).

### 7.4 Beyond the mean relation

- Foreground mapping: spectroscopy of galaxies in front of each burst separates the
  intergalactic and circumgalactic terms (FLIMFLAM, arXiv:2402.00505).
- DM–galaxy cross-correlation and stacking on foreground haloes: arXiv:2506.04186,
  arXiv:2601.21336, arXiv:2608.11296. These constrain the gas profile around haloes and
  therefore baryonic feedback; the suppression of the matter power spectrum that follows
  is treated in `cosmo-simulations-mocks` and `cosmo-weak-lensing`.
- Combination with the kinematic Sunyaev–Zel'dovich effect to break the optical-depth
  degeneracy (arXiv:2608.11296); the kSZ side is in `cosmo-cmb-lss-cross-correlations`.
- Host association is probabilistic (the PATH formalism); a combined `zDM` + PATH
  framework for uncertain associations is in arXiv:2609.04765.

## 8. Lensed transients and time-delay cosmography (pointer)

```
Δt_ij = (D_Δt / c) [ φ(θ_i) − φ(θ_j) ] ,   D_Δt = (1 + z_d) D_d D_s / D_ds ∝ 1 / H0
```

`φ` is the Fermat potential. A transient gives a time delay in one season instead of a
decade of quasar monitoring, and a Type Ia supernova gives in addition its absolute
magnification, which breaks the mass-sheet degeneracy that limits lensed quasars. The
practice so far:

- Cluster lenses (SN Refsdal, SN H0pe, SN Encore): the delay is compared with the
  predictions of several independently built cluster mass models, weighted by how well
  each reproduces the observables; the spread between models limits the precision
  (arXiv:2305.06367, arXiv:2403.18902, arXiv:2509.12301).
- Use of the standard candle: in SN H0pe the models are weighted by agreement with the
  absolute magnifications (arXiv:2403.18902).
- Galaxy-scale lens: SN 2025wny, delays from light curves and from the time evolution
  of spectral features (arXiv:2608.28427).
- Blinding is standard: blinded analysis for Refsdal, live unblinding for H0pe,
  double-blind for Encore [src: the three abstracts].

Lensed quasars and the mass-sheet degeneracy: `cosmo-distance-ladder-h0`. Supernova
standardisation: `cosmo-supernovae`. Lensed gravitational waves and lensed FRBs have
no cosmological measurement yet.

## 9. Codes and pipelines

| Code | Purpose | Reference |
|---|---|---|
| `gwcosmo` | LVK pipeline: catalogue and spectral sirens, joint population inference; sampled redshift prior and host-weighting inference in the 2026 version | arXiv:1908.06050, arXiv:2308.02281, arXiv:2609.04991 |
| `icarogw` 2.0 | LVK pipeline: population, cosmology and modified propagation, CPU/GPU; about two orders of magnitude faster above 100 events [src] | arXiv:2305.17973 |
| `CHIMERA` | joint population and catalogue analysis, built for spectroscopic catalogues | arXiv:2312.05302 |
| `DarkSirensStat` | catalogue method with completeness studies, released with the GWTC-2 analysis | arXiv:2101.12660 |
| `zDM` (+ PATH) | forward model of `p(z, DM)` with survey selection; probabilistic host association | arXiv:2208.00819, arXiv:2609.04765 |
| `FRBs` repository | halo and cosmic DM models (`github.com/FRBs`, named in the abstract) | arXiv:1901.11051 |
| IllustrisTNG DM catalogues | more than 20 public ray-traced DM catalogues [src] | arXiv:2507.07090 |
| `flip` | field-level covariance likelihood; `GWDensMesh` density vector for sirens | arXiv:2501.16852 |

## Conventions and community splits

- H0 in km s⁻¹ Mpc⁻¹; `d_L` in Mpc (no `h`); DM in pc cm⁻³; viewing angle as inclination
  `i` (0°–180°) or as angle from the jet axis (0°–90°): 137° and 43° are one geometry.
- Summary statistic (MAP + highest-density, or median + symmetric) and H0 prior (flat
  or flat-in-log, ranges in §5) differ between papers.
- "Dark siren" means catalogue method in some papers and any siren without counterpart
  in others; the GWTC-5.0 paper uses "spectral" and "dark" for the two cases.
- A fixed-population H0 is not comparable with a marginalised one (arXiv:2605.27227 §4.1).
- FRB baryon fraction: `f_IGM` (excluding halo gas) or `f_d` (all diffuse ionised gas).

## Not verified

- The original reference for the `(Xi_0, n)` parametrisation; Schutz (1986) itself.
- The functional forms of the FullPop-4.0 and multi-peak mass models.
- GausSN (named in arXiv:2608.28427) and the cluster-lens modelling codes.
- How `GWDensMesh` builds the siren density field (per-event sky-position kernels were
  seen in a development copy of flip, not in a release).
