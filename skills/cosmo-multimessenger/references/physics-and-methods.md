# Physics and methods — standard sirens, fast radio bursts, lensed transients, GW × LSS

Scope: what is measured, the estimators and likelihoods in use, the conventions that differ between groups, and the public codes.
Snapshot: 2026-10-13 (deepening pass, 12–13 October; first build 2026-10-07, searches 2026-10-10)

Flags: `[src]` read this session in the cited paper; `[sec]` from a named secondary
source; `[der]` derived here. Equations without a flag are textbook definitions.

## 1. Standard sirens: the observable
<!-- key: standard-sirens-the-observable -->

### 1.1 What the waveform gives
<!-- key: what-the-waveform-gives -->

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

The idea goes back to Schutz (1986), as cited in arXiv:2212.08694 and arXiv:1807.05667. Schutz
1986 (doi:10.1038/323310a0): a neutron-star inspiral gives the absolute distance "independently
of any assumptions about the masses", and ten events within 100 Mpc "may suffice" for 3% on H0
[src: abstract, read on INSPIRE]. Holz & Hughes 2005 (arXiv:astro-ph/0504616) treat LISA massive
black-hole binaries as standard sirens with 1–10% distance accuracy, limited by pointing error
and by weak lensing [src]. Chernoff & Finn 1993 (arXiv:gr-qc/9304020) is the early treatment
with detector noise and without counterparts. Counterpart route: Dalal et al. 2006
(arXiv:astro-ph/0601275) propose short gamma-ray bursts as sirens with known redshift
(**forecast**: about 2% on H0 in one year) [src]; Nissanke et al. 2010 (arXiv:0904.1017) find
that "earlier estimates overstate how well distances can be measured", "the fundamental
limitation" being the distance–inclination degeneracy [src].

Entry points: Palmese & Mastrogiovanni 2025 (arXiv:2502.00239) and Zhao, Zhu & Lu 2026
(arXiv:2605.08595) for sirens; Glowacki & Lee 2024 (arXiv:2410.24072) and Wang et al.
2026 (arXiv:2606.22390) for FRB cosmology. All four were read at abstract level only.

### 1.2 From distance to cosmology
<!-- key: from-distance-to-cosmology -->

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
<!-- key: four-routes-to-the-redshift -->

| Route | Redshift information | Works for | First applied | Section |
|---|---|---|---|---|
| Bright siren | spectroscopic redshift of the host of an electromagnetic counterpart | BNS, NSBH; claimed for BBH in AGN discs | GW170817, arXiv:1710.05835 | §2 |
| Dark siren, galaxy catalogue | redshift distribution of the galaxies in the localisation volume | well-localised events inside a complete catalogue | arXiv:1807.05667, arXiv:1901.01540 | §3 |
| Spectral siren | features of the source-frame mass spectrum, seen redshifted | whole BBH population | arXiv:2111.03604 | §4 |
| Cross-correlation | clustering of sirens with galaxies of known redshift | large samples | arXiv:2203.03643, arXiv:2512.15380 | §6 |

Current LVK analyses combine the second and third in one hierarchical likelihood and
multiply by the GW170817 bright-siren posterior (arXiv:2509.04348, arXiv:2605.27227).

### 1.4 Modified gravitational-wave propagation
<!-- key: modified-gravitational-wave-propagation -->

If the friction term of the tensor propagation equation differs from general
relativity, the distance inferred from the GW amplitude differs from the electromagnetic
luminosity distance. The parametrisation used by the LVK and by Finke et al. 2021
(arXiv:2101.12660) and Mancarella et al. 2021 (arXiv:2112.05728) is

```
d_L^GW(z) / d_L^EM(z) = Xi_0 + (1 - Xi_0) / (1 + z)^n ,     Xi_0 = 1 in general relativity
```

The LVK writes it as Eq. (11) of arXiv:2605.27227, with both parameters positive, and attributes
it to Belgacem et al. 2018 (arXiv:1805.08731) [src: Sect. II.4.2], who introduce `(Xi_0, n)` as
the analogue of `(w0, wa)` and argue that in generic modified gravity the propagation effect
dominates over that of `w_DE(z)`, "even in theories where the speed of gravity is equal to c"
[src: abstract]. The ratio tends to 1 at low redshift and to `Xi_0` at high redshift, on the
assumption that the departure from general relativity is tied to the late emergence of dark
energy; the form "is an assumption", and it is "imperfectly behaved" because `n → 0` also gives
general relativity [src: same section]. A second parametrisation, through the running of the
Planck mass `α_M` with amplitude `c_M` (`c_M = 0` in general relativity), is fitted alongside
[src: Sect. IV.2]. In the data both are strongly correlated with the low-redshift slope `γ` of
the merger rate, because a change of `d_L^GW(z)` and a change of the rate evolution alter the
observed redshift distribution in the same way [src: Sect. IV.2]. Because sirens only measure
`d_L^GW`, `Xi_0` is degenerate with H0 and with the population model: analysing a `Xi_0 = 1.8`
universe with general relativity biases the mass scales, H0 and the merger rate
(arXiv:2112.05728) [src]. The GW speed is a separate test: the (+1.74 ± 0.05) s between GW170817
and GRB 170817A bounds `(c_g − c)/c` to between −3 × 10⁻¹⁵ and +7 × 10⁻¹⁶ (arXiv:1710.05834)
[src], which disfavours dark-energy models with a variable GW speed, the covariant Galileon
among them (Ezquiaga & Zumalacárregui 2017, arXiv:1710.05901) [src]. Theory context belongs to
`cosmo-dark-energy-modified-gravity`.

## 2. Bright sirens
<!-- key: bright-sirens -->

### 2.1 Likelihood
<!-- key: likelihood -->

The LVC 2017 measurement (arXiv:1710.05835) is the template. With `x_GW` the strain
data, `v_r` the measured recession velocity of the host group and `<v_p>` the estimated
peculiar velocity,

```
p(H0 | x_GW, v_r, <v_p>) ∝ p(H0) / N_s(H0)
     × Int  p(x_GW | d, cos i) p(v_r | d, v_p, H0) p(<v_p> | v_p) p(d) p(v_p) p(cos i)
            dd dv_p dcos i
```

This is Eq. (7) of the Methods; `N_s(H0)` is the selection normalisation (Eq. 8; §5), constant
in H0 when the prior is set on `d` and detection depends on `d` only; a volumetric prior on
redshift gives `N_s ∝ H0³`, which cancels [src: Methods, Eq. 10–12]. Canonical priors: `p(d) ∝
d²`, `p(H0) ∝ 1/H0`, flat in `cos i` and in `v_p` on [−1000, 1000] km/s; Gaussian velocity
likelihoods with `v_r = 3327 ± 72` and `<v_p> = 310 ± 150` km/s [src: Methods]. Choices that
move the answer:

- **Distance prior.** Volumetric (`p(d) ∝ d^2`) or uniform in `d_L`. Yang et al. 2026
  (arXiv:2606.30504) re-ran GW170817 under both: the weighted median moves from 77.6 to
  87.6 km/s/Mpc and `P(H0 > 120)` from 0.017 to 0.159 while the binned maximum stays at
  70.5; post-hoc reweighting of the baseline samples recovers only about 17% of that
  shift because the volumetric run undersamples a low-`d_L`, high-inclination mode
  [src]. A prior study must re-sample, not reweight.
- **H0 prior.** Flat-in-log, `p(H0) ∝ 1/H0`, in LVC 2017 (arXiv:1710.05835) [src: Methods] and
  in the O2 paper (arXiv:1908.06060); flat in the LVK papers from GWTC-3 (§5). The same event
  gives 70.0 (+12.0/−8.0) in the first and 68.7 (+17.5/−8.3) in the second [src, abstracts]; the
  two share the prior form, and what else differs between them was not read. A prior flat in `z`
  instead of `p(d) ∝ d²`: systematics file, §2.
- **Summary statistic.** Maximum a posteriori with highest-density interval (LVC 2017, GWTC-3
  era) or median with symmetric interval (GWTC-4.0 onwards). The posteriors are skewed to high
  H0, so the two differ by several km/s/Mpc: 70.0 (+12.0/−8.0) against 74.0 (+16.0/−8.0) for the
  same LVC 2017 posterior (arXiv:1710.05835) [src: Extended Data Table 1].

### 2.2 Breaking the inclination degeneracy with electromagnetic data
<!-- key: breaking-the-inclination-degeneracy-with -->

| Information | How it enters | Reference |
|---|---|---|
| VLBI superluminal motion of the jet centroid | prior on viewing angle (about 20°, opening angle < 5°) [src]; the GW posterior `p(d, θ_obs | x_GW)` is the prior of the light-curve and centroid fit, and the resulting `p(d | x_GW, x_VLBI, x_LC)` enters the LVC 2017 velocity likelihood unchanged [src: 1806.10596 Methods §0.2, Eq. 5–7] | arXiv:1806.09693, arXiv:1806.10596 |
| Afterglow light curve (radio, optical, X-ray, to ~3.5 yr) | joint fit of jet structure and viewing angle | arXiv:2305.19914 |
| All VLBI data fitted in the visibility plane with hydrodynamical jet models | viewing angle 16.8°–19.2°, `d_L` and H0 fitted directly [src] | arXiv:2605.11437 |
| Kilonova and gamma-ray burst with a nuclear equation-of-state prior | joint multi-messenger inference | arXiv:2002.11355 |
| Independent distance to the host (surface-brightness fluctuations) | pins `d`, hence `i ≳ 137°` [src]; no longer a ladder-free H0 | arXiv:1801.06080 |

Every row replaces a GW-only uncertainty by an astrophysical model of the jet or the
ejecta; a viewing-angle bias above about 10° gives more than 3% on H0
(arXiv:2006.02779) [src].

### 2.3 The recession velocity of the host
<!-- key: the-recession-velocity-of-the-host -->

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
<!-- key: dark-sirens-galaxy-catalogue-method -->

### 3.1 Principle
<!-- key: principle -->

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

As written by the LVK (arXiv:2605.27227, with the out-of-catalogue term in arXiv:2509.04348):

```
p(z | Ω) ∝ ψ(z | Λ) / (1 + z) × [ dN_eff,cat / dz dΩ + dN_eff,out / dz dΩ ]     [src: 2605.27227 Eq. 2]
w_j = | L_j / L* |^ε = 10^(−0.4 ε (M_j − M*))                                    [src: 2605.27227 Eq. 3]
dN_eff,out / dz dΩ = (dV_c / dz dΩ) φ* Int_{x_thr}^{x_max} x^(α+ε) e^(−x) dx    [src: 2509.04348 Eq. 13]
x_thr = 10^(0.4 [M* − M_thr(z, m_thr(Ω))])
```

`ψ(z)` is the merger-rate evolution and `1/(1+z)` converts source to observer time. The sky is
cut in HEALPix pixels (`nside = 128` in GWTC-5.0); in each pixel the galaxies brighter than the
pixel's median apparent magnitude `m_thr(Ω)` are kept, each contributing a Gaussian in redshift,
and `ε` is fixed to 0 or 1, not fitted (arXiv:2605.27227) [src: Sect. II.2, III.2]. The
out-of-catalogue term assumes missing galaxies uniform in comoving volume and isotropic, with a
redshift-independent Schechter function and a step-function selection at `m_thr`; it "is
independent of H0" (arXiv:2509.04348) [src: Sect. II.2, Eq. 12–13]. With `ε = 0` an arbitrarily
faint luminosity cut-off makes the out-of-catalogue term dominate the prior, which is one reason
luminosity weighting is the fiducial choice [src: same section]. The two LVK pipelines differ
here: the completeness correction of `icarogw` depends on all Schechter parameters, including
the galaxy number density, while that of `gwcosmo` does not (arXiv:2605.27227) [src: Sect.
II.2].

Formal references: Schutz 1986 (doi:10.1038/323310a0) for the idea of statistical redshifts from
the galaxies in the localisation volume [sec: cited for both the siren idea and the catalogue
method in arXiv:2605.27227 Sect. I]; MacLeod & Hogan 2008 (arXiv:0712.0618) for a worked
estimator on SDSS mocks, in which "each galaxy in a LISA error volume contributes linearly to
the log likelihood for the source redshift" [src]; Del Pozzo 2011 (arXiv:1108.1317) for the
Bayesian formulation; Gray et al. 2019 (arXiv:1908.06050) for the in-catalogue/out-of-catalogue
split and the mock data challenge; Gair et al. 2022 (arXiv:2212.08694) for the consolidated
derivation and for the common errors (mismodelled selection, inconsistent priors) that produce a
spurious bias.

### 3.2 Design choices that differ between analyses
<!-- key: design-choices-that-differ-between-analyses -->

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
<!-- key: dark-sirens-spectral-population-method -->

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
- The three LVK models, all "superpositions of truncated Gaussian and power-law distributions"
  and all taken as redshift-independent (arXiv:2605.27227) [src: Sect. II.3]:

  | Model | Covers | Content | Parameters |
  |---|---|---|---|
  | Multi-peak (MLTP in the paper) | BBH only | one power law with a smooth low-mass cut-off and two Gaussian peaks; `m2` from a power law in mass ratio (Eq. 4) | 11 |
  | FullPop-4.0 (fiducial) | BNS, NSBH and BBH | a low-mass power law for neutron-star objects, a second power law with two Gaussian peaks for black holes, a dip at the junction for the mass gap; `m2` from the same spectrum with a pairing function (Eq. 5) | 19 |
  | FullPop 3 Peaks | same | FullPop-4.0 plus a third Gaussian peak, first used in arXiv:2601.03257 | not stated in the section read |

  The single-peak Power Law + Peak model of GWTC-3 and GWTC-4.0 was dropped in GWTC-5.0 as "more
  strongly disfavored" [src: Sect. II.3]. The merger rate `ψ(z)` follows a Madau–Dickinson form
  with parameters `(γ, κ, z_p)`, `ψ ∝ (1+z)^γ` at `z << z_p` [src: Sect. II.3]. Spins are
  isotropic with uniform magnitudes unless a spin model is named.
- Why a full-population model helps: in GWTC-4.0, moving from a BBH-only model to FullPop-4.0
  tightened the dark-siren H0 by about 56% and 51% (relative to the single-peak and multi-peak
  models) with only 5 additional candidates, "explained by the inclusion of further
  characteristic scales in the mass spectrum, related to the mass gap" (arXiv:2509.04348) [src:
  Sect. IV.1].

The method assumes the features do not move with redshift, or that their motion is
modelled. That assumption is the dominant systematic (systematics file, §5).

## 5. Hierarchical likelihood and selection function
<!-- key: hierarchical-likelihood-and-selection-function -->

All dark-siren analyses use the inhomogeneous-Poisson population likelihood

```
L({x_i} | Λ) ∝ Π_i [ Int L(x_i | θ) p_pop(θ | Λ) dθ ] / ξ(Λ)^N
ξ(Λ) = Int p_det(θ) p_pop(θ | Λ) dθ
```

with `Λ` holding H0, Ω_m, the mass, spin and rate-evolution parameters and, when used, `Xi_0`.
`ξ(Λ)` is the detectable fraction, estimated from injection campaigns. The derivation is Mandel,
Farr & Gair 2018 (arXiv:1809.02063); general treatment of selection in hierarchical models is in
`cosmo-statistics-inference`.

As the LVK writes it, in detector-frame parameters `θ_det ∋ {m1_det, m2_det, D_L^GW}` and
source-frame parameters `θ ∋ {m1, m2, z}` (arXiv:2605.27227) [src: Eq. 1]:

```
p({d_i} | Λ) ∝ ξ(Λ)^(−N_det) Π_i Int dθ_det,i  [ p(θ_det,i | d_i) / π_PE(θ_det,i) ]
                                               × | dθ_det,i / dθ_i |^(−1) p_pop(θ_i | Λ)
```

`π_PE` is the parameter-estimation prior, which is divided out; the Jacobian carries the
source-to-detector-frame change, and with it H0; the total number of mergers is marginalised
with a prior `∝ 1/N` [src: Sect. II.1]. How the two pipelines evaluate it (arXiv:2509.04348)
[src: Appendix A]:

| Step | `icarogw` | `gwcosmo` |
|---|---|---|
| Per-event integral | Monte Carlo sum over posterior samples (Eq. A3); requires an effective sample size `n_eff,PE > 10` (Eq. A5) | samples re-weighted by `p_pop / π_PE` (Eq. A6), then a one-dimensional kernel density estimate in redshift per sky pixel (Eq. A7), integrated against the catalogue prior (Eq. A8) |
| Known weakness | sampling variance of the Monte Carlo sum | "susceptible to systematic uncertainties if re-weighted sample sizes are too small" |
| Selection term `ξ` | both: re-weighting of an injection campaign that passed the same detection threshold as the catalogue (Eq. A9), with `n_eff,inj > 4 N_obs` | |

The thresholds are data-dependent and "effectively modify the likelihood surface"; raising
`n_eff,PE` to 50, removing it, requiring `n_eff,inj > 2000`, or using `var(ln L) < 1` (Eq. A10)
instead changed the GWTC-4.0 H0 negligibly, a conclusion the paper restricts to its own models
and warns may fail for "highly-peaked integrands, such as those resulting from extreme
luminosity-weighting schemes" [src: Sect. IV.3]. The detection threshold of the cosmology sample
is a false-alarm rate below 0.25 yr⁻¹ in at least one search pipeline (arXiv:2605.27227) [src:
Sect. III.1].

Combining the two codes: GWTC-4.0 quotes "an equal-weighted mixture of samples (50% from each
pipeline)", so that the result carries the residual difference between the two numerical
implementations (arXiv:2509.04348) [src: Sect. IV]. On the same GWTC-5.0 events the two codes
agree on H0 but not on how much the catalogue adds: 2% for `icarogw`, 8% for `gwcosmo`, 3.5% for
the mixture (arXiv:2605.27227) [src: Sect. IV.1].

Points specific to sirens:

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
- Fixed background: the LVK ΛCDM results fix `Ω_m = 0.3065` and `w0 = −1`, because rebuilding
  the catalogue redshift prior for each `Ω_m` is too costly; a spectral-only run with `Ω_m` free
  on U(0, 1) returns the prior and leaves H0 almost unchanged (arXiv:2605.27227) [src: Sect.
  IV.1, Appendix E].
- Modified-gravity runs use narrower H0 priors, U(10, 120) or U(65, 77), with `Xi_0` on U(0.435,
  10) and `n` on U(0.1, 10): a wider H0 prior would send sources beyond `z ≈ 10`, outside the
  redshift priors and the stable range of the selection integral (arXiv:2605.27227) [src: Sect.
  IV.2].
- Electromagnetic selection is not in the LVK likelihood: "our pipelines fully account for GW
  selection effects, they do not yet model the EM detection probability", which is why GW170817
  is removed from the dark-siren sample and its posterior multiplied in afterwards
  (arXiv:2605.27227) [src: Sect. V.2].
- Blinding: LVK H0 analyses are not blinded. Blinded mock data challenges exist for the
  spectral method (arXiv:2412.14244, arXiv:2604.26273). Lensed-supernova measurements are
  blinded (§8).

## 6. Siren × large-scale-structure cross-correlation
<!-- key: siren-x-large-scale-structure-cross-correlation -->

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
- Not a cross-correlation, though sometimes listed with them: Andrade-Oliveira et al. 2026
  (arXiv:2601.04774) multiply the DES Y3 3×2pt posterior by the LVK spectral-siren posterior,
  assuming independence, and chose spectral rather than catalogue sirens to avoid a covariance
  through shared galaxy catalogues [src: Sect. 3.4].
- Requirements for a percent-level H0 (forecast): `σ_dL = 0.1 d_L`, at least 5000 dark
  sirens and good localisation (arXiv:2510.19931) [src].

A field-level variant grids the sirens in `d_L` space and compares the resulting density
field with a galaxy field in redshift space. The `flip` package (arXiv:2501.16852)
contains a density data vector for that purpose, `GWDensMesh` in
`flip/data_vector/gw_vectors.py` [src: public flip repository, `main` branch, class
present on 2026-10-12]. How it is built was read in a development copy and is listed
under "Not verified".

## 7. Fast radio bursts: dispersion measure–redshift relation
<!-- key: fast-radio-bursts-dispersion-measure-redshift -->

### 7.1 Budget
<!-- key: budget -->

```
DM_obs = DM_MW,ISM + DM_MW,halo + DM_cosmic(z) + DM_host / (1 + z)

<DM_cosmic>(z) = (3 c H0 Ω_b / 8 π G m_p) Int_0^z  f_d(z') χ_e(z') (1 + z') / E(z') dz'
χ_e = Y_H + Y_He / 2   (≈ 7/8 after helium reionisation)
```

`f_d` is the fraction of baryons in diffuse ionised gas (written `f_IGM` when halo gas is
counted separately). The mean relation is called the Macquart relation after Macquart et al.
2020 (arXiv:2005.13161), who write it as [src: Eq. 2]

```
<DM_cosmic> = Int_0^z_FRB  c n_e(z) dz / [ H0 (1+z)^2 sqrt(Ω_m (1+z)^3 + Ω_Λ) ]
n_e = f_d(z) ρ_b(z) (1 − Y_He/2) / m_p ,   ρ_b(z) = Ω_b ρ_c,0 (1+z)^3 ,   Y_He = 0.25
```

with `f_d(z)` from a census of stars, remnants (30% of the stellar mass) and neutral gas
(`M_ISM/M_* = 0.38`), uncertain to below 6% on `Ω_b h70` [src: Methods §0.4]; `f_d(z = 0) =
0.844` (arXiv:2208.00819) [src: Sect. 7.2]. Numerically, `<DM_cos> ≈ 1085 z f_d (Ω_b h70 /
0.04703)` pc cm⁻³ at `z ≲ 1` (arXiv:2409.16952) [src]. Earlier formulations: Inoue 2004
(arXiv:astro-ph/0309364), written for the radio dispersion of gamma-ray bursts and cited for the
mean relation by arXiv:2208.00819 [src: Sect. 2.1]; Deng & Zhang 2013 (arXiv:1401.0059) for `Ω_b
f_IGM`; McQuinn 2013 (arXiv:1309.4451) for the probability distribution of `DM(z)` and its
sensitivity to where halo baryons sit.

### 7.2 What is degenerate with what
<!-- key: what-is-degenerate-with-what -->

`<DM_cosmic> ∝ Ω_b H0 f_d`. Written with the physical baryon density,
`<DM_cosmic> ∝ (Ω_b h²) f_d / h` [der: `Ω_b H0 = (Ω_b h²) × 100 / h`]. An H0 from FRBs
therefore requires an external `Ω_b h²` (nucleosynthesis or CMB) and an assumed `f_d`;
conversely a baryon census requires H0. Jahns-Schindler & Spitler 2025
(arXiv:2508.14434) state the degeneracy and propose FRBs with gravitational-wave
distances to break it without early-universe priors. A higher H0 predicts a lower DM at
fixed `z`.

### 7.3 Scatter and the likelihood
<!-- key: scatter-and-the-likelihood -->

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

The likelihoods as their papers write them:

| Analysis | Likelihood | Fixed | Fitted | Place read |
|---|---|---|---|---|
| Macquart et al. 2020, `Ω_b h70` | product over bursts of the convolution of `p_host` (log-normal, Eq. 3, rest frame, `(1+z)⁻¹` applied) with `p_cosmic(Δ) = A Δ^(−β) exp[−(Δ^(−α) − C0)² / (2 α² σ_DM²)]`, `Δ = DM_cosmic / <DM_cosmic>`, `α = β = 3` (Eq. 4), on `DM − DM_MW,ISM − DM_MW,halo` (Eq. 6) | `Ω_Λ = 0.691`; `DM_MW,halo = 50`, `DM_MW,ISM = 30` pc cm⁻³ | `Ω_b h70`, `F` (with `σ_DM = F z^(−0.5)`), host median `e^μ` on 20–200 pc cm⁻³, `σ_host` on 0.2–2.0 | arXiv:2005.13161 [src: Methods §0.5] |
| James et al. 2022, H0 | forward model of `P(z, DM, SNR)` per survey; `<DM_cosmic> ∝ Ω_b H0` (Eq. 9), and with `Ω_b h²` fixed `<DM_cosmic> ∝ 1/H0` (Eq. 10) | `Ω_b h² = 0.02242`, `f_d(z)`, `F = 0.32`, `DM_halo = 50`, NE2001 | H0, host `μ_host` and `σ_host`, luminosity function, evolution | arXiv:2208.00819 [src: Sect. 2.1, 7.2] |
| Connor et al. 2024, baryon partition | per-burst `P(DM_ex | z_s, θ)` with `p(DM | z)` taken from a simulation, product over bursts, MCMC; cross-check with a Gaussian likelihood on the mean (Eq. 4, 7) | `Ω_b h70` for the partition, or `f_d` for `Ω_b h70` | `θ = {f_IGM, f_X, μ_host, σ_host}`, `f_X` being the share in intersected haloes | arXiv:2409.16952 [src: main text, Methods] |

Two likelihood styles exist. The first fits localised bursts only, `p(DM | z)`
(arXiv:2104.04538, arXiv:2108.00581, arXiv:2507.18946). The second forward-models the
survey — luminosity function, beam shape, burst width, population evolution — and fits
`p(z, DM)` of localised and unlocalised bursts together (James et al. 2022,
arXiv:2208.00819; the `zDM` code). The second style returns larger H0 errors because it
marginalises over the energy function and `DM_host` [src]. Unlocalised bursts alone
constrain H0 weakly through the shape of the DM distribution (arXiv:2604.03769).

### 7.4 Beyond the mean relation
<!-- key: beyond-the-mean-relation -->

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
<!-- key: lensed-transients-and-time-delay-cosmography -->

```
Δt_ij = (D_Δt / c) [ φ(θ_i) − φ(θ_j) ] ,   D_Δt = (1 + z_d) D_d D_s / D_ds ∝ 1 / H0
```

`φ` is the Fermat potential. The method is due to Refsdal 1964 (doi:10.1093/mnras/128.4.307)
[sec: cited as its origin in arXiv:2506.03023 Sect. 2.1; title confirmed on Crossref, text not
read]. A transient gives a time delay in one season instead of a decade of quasar monitoring,
and a Type Ia supernova gives in addition its absolute magnification, which breaks the
mass-sheet degeneracy that limits lensed quasars. The practice so far:

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

How the delay becomes H0 in the main analyses:

| Analysis | Step from delay and lens model to H0 | Place read |
|---|---|---|
| SN Refsdal | the convergence map `κ` that fits the image positions does not depend on H0, so delays predicted at H0 = 70, Ω_M = 0.3 are rescaled as 1/H0; the measured SX–S1 delay of 376.0 (+5.6/−5.5) days is compared with each model, the likelihood being a Gaussian mixture built on 1000 simulated light curves that include subhaloes and stars. H0 = 73.04 would need 333.8 days | arXiv:2305.06367 [src: main text, Supplementary "Rescaling time-delay predictions"] |
| SN H0pe | per model, `p(H0 | LC) ∝ P(H0) P(M_l) ∫ P(O | M_l; H0) P(O | LC) dO` (Eq. 4), then a weighted sum over the seven models (Eq. 5), on the assumption that their systematics are not independent; with two delays the models are in effect weighted by how well they match the ratio of the delays, with absolute magnifications by how well they match those | arXiv:2403.18902 [src: Sect. VII.1] |
| SN Encore | one delay only; each team gives samples of its mass model at a fixed cosmology, delays are rescaled for random H0 draws and weighted by the time-delay likelihood, then each model by the maximum likelihood of the same 23 image positions (Eq. 1); a BIC weighting was tried and dropped | arXiv:2509.12301 [src: Sect. VI.3] |
| SN 2025wny | galaxy-scale lens model combined with delays; the result depends on the radial profile assumed (systematics file, §8) | arXiv:2608.28427 [src: Sect. VI.2] |
| Mass-sheet transform | `κ_λ = λ κ + (1 − λ)` leaves image positions and flux ratios unchanged and rescales `Δt → λ Δt` and `μ → μ/λ²`, so `H0 ∝ λ` | arXiv:2506.03023 [src: Sect. 3.1, Eq. 5–7]; arXiv:2403.18902 [src: Sect. X.3] |

Lensed quasars and the mass-sheet degeneracy: `cosmo-distance-ladder-h0`. Supernova
standardisation: `cosmo-supernovae`. Lensed gravitational waves and lensed FRBs have
no cosmological measurement yet.

## 9. Codes and pipelines
<!-- key: codes-and-pipelines -->

| Code | Purpose | Reference |
|---|---|---|
| `gwcosmo` | LVK pipeline: catalogue and spectral sirens, joint population inference; sampled redshift prior and host-weighting inference in the 2026 version; version 3.0.0 in GWTC-4.0 [src: 2509.04348, software statement]; kernel-density evaluation of the per-event term (§5) | arXiv:1908.06050, arXiv:2308.02281, arXiv:2609.04991 |
| `icarogw` 2.0 | LVK pipeline: population, cosmology and modified propagation, CPU/GPU; about two orders of magnitude faster above 100 events [src]; version 2.0.3 in GWTC-4.0 [src: 2509.04348, software statement]; Monte Carlo evaluation (§5) | arXiv:2305.17973 |
| `CHIMERA` | joint population and catalogue analysis, built for spectroscopic catalogues | arXiv:2312.05302 |
| `DarkSirensStat` | catalogue method with completeness studies, released with the GWTC-2 analysis | arXiv:2101.12660 |
| `zDM` (+ PATH) | forward model of `p(z, DM)` with survey selection; probabilistic host association | arXiv:2208.00819, arXiv:2609.04765 |
| `FRBs` repository | halo and cosmic DM models (`github.com/FRBs`, named in the abstract) | arXiv:1901.11051 |
| IllustrisTNG DM catalogues | more than 20 public ray-traced DM catalogues [src] | arXiv:2507.07090 |
| `flip` | field-level covariance likelihood; `GWDensMesh` density vector for sirens | arXiv:2501.16852 |

## Conventions and community splits
<!-- key: conventions-and-community-splits -->

- H0 in km s⁻¹ Mpc⁻¹; `d_L` in Mpc (no `h`); DM in pc cm⁻³; viewing angle as inclination
  `i` (0°–180°) or as angle from the jet axis (0°–90°): 137° and 43° are one geometry.
- Summary statistic (MAP + highest-density, or median + symmetric) and H0 prior (flat
  or flat-in-log, ranges in §5) differ between papers.
- "Dark siren" means catalogue method in some papers and any siren without counterpart
  in others; the GWTC-5.0 paper uses "spectral" and "dark" for the two cases.
- A fixed-population H0 is not comparable with a marginalised one (arXiv:2605.27227 §4.1).
- FRB baryon fraction: `f_IGM` (excluding halo gas) or `f_d` (all diffuse ionised gas).

## Not verified
<!-- key: not-verified -->

- Closed on 2026-10-13: the abstract of Schutz (1986) was read on INSPIRE and its DOI confirmed
  on Crossref. The text of Refsdal (1964) was not read.
- The equations of the FullPop-4.0 and multi-peak mass models (Appendix A of arXiv:2605.27227,
  Appendix C of arXiv:2509.04348) and their prior ranges; §4 gives their content as described in
  Sect. II.3 only.
- GausSN (named in arXiv:2608.28427) and the cluster-lens modelling codes.
- How `GWDensMesh` builds the siren density field (per-event sky-position kernels were
  seen in a development copy of flip, not in a release).
