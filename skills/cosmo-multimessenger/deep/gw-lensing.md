# Lensing of gravitational waves — cosmo-multimessenger dossier

Scope: how lensing enters siren cosmology in its three roles (weak-lensing
noise and bias on `d_L`, strong-lensing searches and their false alarms, and
lensed-siren cosmography from a time delay with a host), with the equations,
priors and thresholds each analysis uses and the tests that catch a spurious
lensing claim or a lensing bias.
Snapshot: 2026-10-19.
From: Einstein Telescope science case (arXiv:2503.12263), Sect. 2.3.3; LISA
Cosmology Working Group (arXiv:2204.05434), Sect. 3; Birrer et al. 2025
(arXiv:2502.04472), Sect. 3; Zhao et al. 2026 (arXiv:2605.08595), Sects. 3.1.2
and 5.3.

Already in L2, not repeated here: the LVK statement that weak lensing adds a
few percent of variance per GWTC-3 siren and that strong lensing of a GWTC-3
event has probability below one percent
(`systematics.md#detector-calibration-and-waveform-systematics`); the absence
of any lensed-GW cosmological measurement
(`surveys-and-data.md#lensed-transients`); the Tamanini et al. 2016 and ET
design-study lensing terms used in forecasts and the selection-induced
multiplicative bias (`deep/next-generation-siren-forecasts.md`, Step 4);
time-delay cosmography with lensed supernovae and quasars
(`physics-and-methods.md#lensed-transients-and-time-delay-cosmography`, and
`cosmo-distance-ladder-h0`, `deep/time-delay-cosmography.md`).

## How it is done

Notation. `μ` is the (signed or absolute) magnification of an image, `κ` the
convergence, `γ` the shear, `d_L` the luminosity distance, `M_L` the
redshifted lens mass, `f` the GW frequency, `n_j` the Morse index of image
`j`, `t_j` its arrival time, `D_d`, `D_s`, `D_ds` the angular-diameter
distances to the lens (deflector), to the source and between them, `z_d`
(also `z_L`) and `z_s` (also `z_S`) the lens and source redshifts, `θ_E` the
Einstein radius, `Δφ` a Fermat-potential difference. The waveform follows the
LVK (arXiv:2512.16347, Eq. 1); the wave-optics criterion follows the LISA
Cosmology Working Group (arXiv:2204.05434, Eq. 13–15); the weak-lensing error
follows Mpetha et al. 2024 (arXiv:2402.19476, Eq. 4–11).

### Step 1. Decide which regime applies

Two numbers set the regime [src: arXiv:2204.05434, Sect. 3.1].

```
w = 8 π G M_L f = 4 π (M_L / 10^8 M☉) (f / mHz)                          (Eq. 13)
F(w) = Σ_j |μ_j|^(1/2) exp(i w Δt̃_j − i π n_j)      geometric optics, w ≫ 1 (Eq. 14)
F(w) = (w / 2π i) ∫ d²x exp(i w Δt̃(x, b))            wave optics, w ≲ 1   (Eq. 15)
```

`F = h_lensed / h_unlensed` is the amplification factor, `Δt̃_j` the delay in
units of `4 G M_L`, `x` and `b` the normalised lens-plane and source
positions. Weak lensing is `κ ≪ 1` (magnification only, hence a change of the
inferred `d_L`); strong lensing is `κ ≃ 1` (multiple images with delays).
Because GW sources are point-like, shear enters only through the
magnification [src: same, footnote 3]. For LISA sources wave optics matters
for lenses of `10^6–10^9 M☉`; LISA should see `≲ 5` strongly lensed events
in five years, mostly by `10^12 M☉` haloes where wave effects are
unimportant, while `0.1–1.6%` of its `10^5–10^6.5 M☉` binaries at `z = 4–10`
may show detectable wave-optics features [src: Sect. 3.4]. For ground-based
stellar-mass sources Dai et al. 2016 note that the relevant length is the
Schwarzschild length of the lens mass, not its physical size, and that
diffraction truncates the magnification tail above `μ ≳ 10³`
(arXiv:1605.09398) [src: Sect. II footnote 2, Sect. III].

### Step 2. Weak lensing as a distance error: add `σ_WL` to every siren

The per-siren distance variance used in bright-siren analyses is
(arXiv:2402.19476) [src: Eq. 4]

```
σ_dL² = σ_GW² + σ_WL² + (∂d_L/∂z)² (σ_z² + σ_vpec²)
μ = 1 / [(1 − κ)² − γ²]                                    (Eq. 6)
σ_μ² ≈ 4 σ_κ² ,   σ_WL / d_L ≈ σ_κ                          (Eq. 7, 8; shear dropped)
σ_WL / d_L = (C/2) [ (1 − (1+z)^(−β)) / β ]^α                (Eq. 11)
```

`σ_GW` is the instrumental distance error, `σ_z` the redshift error and
`σ_vpec` the peculiar-velocity term. The fitting form of Eq. 11 comes from
Hirata, Holz & Cutler 2010 (as cited) built on a 1998 magnification
distribution, and was recalibrated by Cusin & Tamanini 2021 (as cited) on
1 × 1 deg² ray-tracing simulations with `h = 0.705`, `Ω_m = 0.274`; their
coefficients are `C = 0.061`, `β = 0.264`, `α = 1.89` (Pop III seeds) and
`C = 0.096`, `β = 0.62`, `α = 2.36` (Q3 seeds) [src: Sect. IV.3]. Mpetha et al.
state that "the factor of 1/2" is "missing in" Tamanini et al. 2016
(arXiv:1601.07112), because the original expression is for
`σ(ln d_L²) = 2 σ(d_L)/d_L` [src: Sect. IV.3 and footnote 6]. Full-sky
`N_side = 16384` ray tracing (to `z = 5.3`) gives `C = 0.076`, `β = 0.344`,
`α = 2.25` without selection and `C = 0.092`, `β = 0.164`, `α = 2.09` with an
ET + 2 CE selection [src: same].

The magnification is drawn from `p(μ, z | θ)` restricted to `μ ≤ 1.75`, a
shifted log-normal, compared with full-sky simulations; detection selection
is applied by [src: Sect. IV.1, Eq. 9–10]

```
P(μ, z | θ) = C p(μ, z | θ) dN(μ, z)/dz ,   dN/dz = ∫_{ρ_lim/√μ}^∞ N(z, ρ) dρ
```

with `ρ` the signal-to-noise ratio and `ρ_lim` its threshold. The authors'
reason for cutting at `μ ≤ 1.75`: "poorly understood small-scale physics
significantly impacts the high-magnification tail" [src: Sect. IV.1]. Their
bias test (Sect. II): for each catalogue realisation, magnify every merger,
redraw distances and redshifts with the same random numbers in the lensed and
unlensed cases, fit `d_L(z)` by MCMC with `emcee`, measure the bias with the
parameter-difference method of `tensiometer`, and repeat about 300 times.

Weak lensing can also be the signal: the observed distance is
`D_L' = (1 − κ) D_L` (arXiv:2204.05434) [src: Sect. 3.2.2, Eq. 16], so the
scatter of the Hubble residuals carries `σ_8`. Forecasts: `Ω_m` and `σ_8` to
2% and 3% and H0 better than 1% from about 1 source per deg² with
spectroscopic follow-up, no external priors (arXiv:1812.02730) [src:
abstract; **forecast**]; `σ_8` to 10% from 300 ET neutron-star binaries with
counterparts, 30% from 12 LISA massive binaries (arXiv:2601.06023) [src:
abstract; **forecast**].

### Step 3. De-lens, or do not

De-lensing estimates the convergence along each siren line of sight from a
shear (and flexion) map and subtracts it. Reported gains, all **forecasts**:
30–40% on the distance error at `z = 2` with an ELT mosaic, 50% with an added
space shear map (arXiv:0907.3635) [src: abstract]; 20% (10%) at `z = 1.5`
(`z = 5`) with 100 galaxies arcmin⁻², 50% (35%) with shear and flexion from
500 galaxies arcmin⁻², up to 75% in low-convergence regions
(arXiv:1007.2468) [src: abstract]; about a factor of two at `z_s = 2.9`, but
only with an ultra-deep field for every siren, so that de-lensing is
"unlikely to be worthwhile" (arXiv:2211.15160) [src: abstract]. The most
recent of the three is the most pessimistic, and its reason is cost, not
method.

### Step 4. Search for strongly lensed pairs (the LVK workflow)

The lensed waveform of image `j` is (arXiv:2512.16347) [src: Sect. III.1,
Eq. 1]

```
h̃_L^j(f; θ, φ_j) = √μ_j  h̃_U(f; θ)  exp(−2 i π f t_j + i π n_j sign(f)) ,
n_j ∈ {0, 0.5, 1}  for type I (minimum), II (saddle), III (maximum) images
```

`θ` holds the binary parameters. Images share the frequency evolution; the
type-II phase is detectable only with precession, higher multipoles or
eccentricity [src: same]; for a non-precessing equal-mass quasi-circular
binary it amounts to a `π/4` shift of the coalescence phase
(arXiv:2204.05434) [src: Sect. 3.3].

The GWTC-4.0 (O4a) search is tiered by cost [src: arXiv:2512.16347, Sect.
III.1.1, IV.1]:

1. **Data.** 84 new O4a binary-black-hole candidates with false-alarm rate
   below 1 yr⁻¹; earlier runs are not paired with O4a, for cost and because
   the gap between runs is longer than expected galaxy-lens delays [src:
   Sect. II].
2. **Tier 1** on all 3486 pairs: Posterior Overlap (consistency of
   detector-frame masses, spins and sky position, `B_U^L`, times a prior
   ratio `R_U^L` from the expected galaxy-lens delay distribution) and
   Phazap (phase of the `ℓ = m = 2` mode at 40 Hz, arrival times between
   detectors, phase evolution). A false-positive probability (FPP) is the
   fraction of unlensed background pairs with a higher ranking statistic;
   FPP < 1% in either method passes. 105 pairs passed (5 in both, 33 Posterior
   Overlap only, 67 Phazap only).
3. **Tier 2**, Fast-GOLUM: joint likelihood built from the first image's
   samples, with priors U(0.1, 50) on relative magnification,
   `[t_ij − 0.2, t_ij + 0.2]` s on the delay and {0, 0.5, 1, 1.5} on the Morse
   difference, "chosen to cover a broad range of astrophysical lensing
   scenarios"; pass if `log10 C_U^L > 0`, `C_U^L = p(d1, d2 | L) / [p(d1 | U)
   p(d2 | U)]`. 55 of 105 discarded, 50 kept.
4. **Tier 3**, Hanabi: full joint parameter estimation, the evidence
   reweighted by the GWTC-4.0 population, a singular-isothermal-sphere (SIS)
   lens population and selection effects, giving the strong-lensing Bayes
   factor. No pair prefers lensing, for three merger-rate models
   (Madau–Dickinson, `R_min(z)`, `R_max(z)`); all 50 pairs have
   `p_astro^pair > 0.9` [src: Sect. IV.1.3].
5. **Sub-threshold counterparts**: PyCBC with a single template (aligned-spin
   projection of the maximum-posterior waveform) and TESLA-X on GstLAL with a
   targeted bank, both with SEOBNRv4, vetoing triggers whose 90% sky area does
   not overlap the target [src: Sect. III.1.2].
6. **Background**: 254 unlensed injections into real O4a data, because lensed
   models "have extra degrees of freedom" and can win on non-Gaussian noise
   [src: Sect. III.3].

The full O3 search used the same families (sub-threshold searches, parameter
overlap, spectrogram similarity, joint Bayesian analysis with selection and
astrophysical priors, type-II phase and point-mass distortions) and found no
significant evidence (arXiv:2304.08393) [src: abstract].

### Step 5. Turn a non-detection into rates and a high-redshift bound

Rates relative to unlensed detections are simulated with SIS lenses, the SDSS
velocity-dispersion function (`σ_vd = 10–350` km/s) for galaxies, the Tinker
halo mass function (`10^14–10^16 M☉`) for clusters, the GWTC-4.0 population,
and a two-detector SNR above 8 applied to the fainter image (`R_D`, both
detected) or the brighter (`R_S`) [src: arXiv:2512.16347, Sect. VII.1]. The
non-detection removes merger-rate histories that would have produced lensed
pairs; the resulting bound on the high-redshift BBH rate is "comparable to"
that from the absence of a stochastic background, with a different redshift
weighting [src: Sect. VII.2]. The stochastic-background side is in
`cosmo-early-universe-exotica`, `deep/sgwb-pta.md`.

### Step 6. Lensed-siren cosmography (forecast only)

With an electromagnetic host the delay gives the time-delay distance
(arXiv:1703.04151) [src: Eq. 1–2]

```
Δt_ij = D_Δt (1 + z_d) / c × Δφ_ij ,   D_Δt = D_d D_s / D_ds
```

Liao et al. keep `(1 + z_d)` outside `D_Δt`; the L2 file and TDCOSMO include
it in `D_Δt`. Three errors enter: the delay, the Fermat potential, and the
line of sight (1% level) [src: same]. Two routes exist:

- **Bright lensed siren.** The kilonova identifies the lensed host; an image
  of the host without the transient constrains the lens. Liao et al. find a
  Fermat-potential error of about 0.6% against about 3% for lensed quasars,
  and 0.37% on H0 from 10 systems with `Ω_M = 0.3` fixed, against 1.5% for
  the same number of lensed quasars; 0.68% for flat ΛCDM in the abstract
  [src: Results; abstract]. **forecast**.
- **Dark lensed siren.** A quadruple image localises the host among the
  lensed galaxies in the GW area. Hannuksela et al. 2020 rank candidate lenses
  by GW and electromagnetic consistency, model the 11 best with `lenstronomy`
  on simulated HST images, and get one to five candidates; with a lens model
  they place the binary in one of two sub-arcsecond regions, about 10⁹ times
  smaller than the initial `~4 deg²`, and obtain H0 = 68 (+8/−6) (median,
  symmetric 68%) in flat ΛCDM with `Ω_M` fixed, mainly from the time-delay
  distance, secondarily from the four sirens with an assumed 20% scatter
  between model and true magnification (arXiv:2004.13811) [src: Sect. 4, 5].
  **forecast**. Third-generation networks: three or more images reduce the
  typical area to about 0.01 deg² and give `≲ 1%` on H0 in two years or more,
  even with stellar-mass BBH alone (arXiv:2510.12470) [src: abstract].
  **forecast**.

Without a host neither route works: "sky localisation of dark sirens without
an EM counterpart will be very poor and far beyond the astrometric
requirement", with an exception only for "extremely simple" lenses such as a
point mass (arXiv:2502.04472) [src: Sect. 3.2 and footnote 1].

## Choices and what they cost

### Weak-lensing term: which `σ_WL(z)`

| Choice | Assumes | Cost | Used by |
|---|---|---|---|
| Tamanini et al. 2016 form, coefficient 0.066 | 1 × 1 deg² dark-matter-only rays | factor 2 too large according to arXiv:2402.19476 [src: Sect. IV.3] | LISA forecasts (next-generation dossier) |
| `0.05 z` | linear in `z` | no cosmology dependence | ET design study (next-generation dossier) |
| Eq. 11 with full-sky coefficients | `N_side = 16384`, `z ≤ 5.3`, old cosmology `h = 0.7`, `Ω_m = 0.279` | resolution-dependent width (Fig. 3) | arXiv:2402.19476 |
| Amplitude of `σ_WL` free, fitted with cosmology | enough events | weaker cosmology | arXiv:2402.19476 [src: Sect. VI, Eq. 12] |
| No term | — | biased above `z ≈ 0.5` | some forecasts (next-generation dossier) |

Why the simulation matters: a small box misses superclusters and voids
(high `ℓ_min`), coarse resolution cuts `ℓ_max`; both narrow `p(μ)`; dark-matter
only versus feedback changes it again, IllustrisTNG and MilleniumTNG giving a
narrower `p(μ, z)` [src: arXiv:2402.19476, Sect. IV.3].

### Treat the magnification as noise, as a nuisance, or as data

Adding `σ_WL` treats lensing as noise; the bias study shows that this is
unbiased only if `σ_WL` is right (Step 2). Fitting its amplitude makes it a
nuisance. Using the residual scatter makes it data and gives `σ_8` (Step 2).
For spectral sirens there is no `σ_WL` term in the LVK likelihood: the GWTC-3
paper ignores lensing (L2). The bias it would cause is through the
mass–redshift degeneracy of Dai et al. (arXiv:1605.09398) [src: Eq. 1, 5]

```
M̃ (1 + z̃) = M (1 + z) ,    d_L(z̃) = d_L(z) / √μ
```

so a magnified low-mass, high-redshift merger is read as a heavier, nearer
one; strong magnification `μ ≳ 3` makes a heavy tail of apparently massive
mergers that may dominate the intrinsically massive population in some
formation models [src: abstract]. This is the same mass-scale lever that
spectral sirens use for H0 (`systematics.md#population-mass-spectrum-mis-specification`).
Ray tracing finds `⟨μ⟩` stays at unity below about 3 Gpc for LIGO–Virgo
detections, with 0.5–1% scatter, and a bias beyond (arXiv:2012.08381) [src:
abstract].

### Pair search: overlap statistics or joint parameter estimation

Posterior overlap and phase consistency are cheap and run on all `N(N−1)/2`
pairs; joint parameter estimation is the only step that includes population
and selection, and is run on 50 of 3486 pairs (Step 4). The two tier-1
methods flagged largely different pairs (5 in common of 105), which is why
either one passing is enough [src: arXiv:2512.16347, Sect. IV.1.1].

### Bright or dark lensed siren

The bright route needs a counterpart and gives a precise host image; the
dark route needs a quadruple and a lens catalogue in the GW area, and its
host test (below) uses an H0 prior. Birrer et al. add that ms timing makes
small-Einstein-radius (about 0.5″) galaxy lenses usable, which optical
delays below a day cannot exploit [src: arXiv:2502.04472, Sect. 3.3].

## Numbers

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| O4a pairs examined; after tier 1; after tier 2 | 3486; 105; 50 | GWTC-4.0 | arXiv:2512.16347 | Sect. IV.1 |
| Tier-1 threshold | FPP < 1% | GWTC-4.0 | arXiv:2512.16347 | Sect. III.1.1 |
| Unlensed background | 254 injections in O4a data | GWTC-4.0 | arXiv:2512.16347 | Sect. III.3 |
| Relative lensed-double rates, Power-Law model (median) | `R_D` 18.1 × 10⁻⁴, `R_S` 24.5 × 10⁻⁴ (first column pair); 5.4 × 10⁻⁴, 7.6 × 10⁻⁴ (second pair) | GWTC-4.0 | arXiv:2512.16347 | Table 7 |
| Same, Power-Law + Peak with SGWB limit (90%) | 3.2–9.9, 5.0–13.5 (first pair); 0.9–3.8, 2.1–5.1 (second pair), × 10⁻⁴ | GWTC-4.0 | arXiv:2512.16347 | Table 7 |
| GW231123 point-lens `log10 B` | 3.8 (IMRPhenomXPHM-SpinTaylor), 1.5 (NRSur7dq4), 0.1 (IMRPhenomXO4a); 0.62 Hanford, 2.64 Livingston | GWTC-4.0 | arXiv:2512.16347 | Table 2, Sect. VI.1 |
| GW231123 redshifted lens mass | 911 (+504/−292) M☉ (XPHM-ST) | GWTC-4.0 | arXiv:2512.16347 | Sect. VI.1 |
| Chance-coincidence FAP per pair | chirp mass ~9%, sky ~1%, phase ~10%; combined ~10⁻⁴ | mock catalogue | arXiv:2201.04619 | abstract |
| Lensing rate at design (for the false-alarm argument) | `≲ 10⁻³` | mock | arXiv:2201.04619 | abstract |
| Weak-lensing bias spread on H0 | 0.25 km s⁻¹ Mpc⁻¹ (3G BNS), 5 (LISA SMBHB) | bright sirens | arXiv:2402.19476 | Sect. VI |
| Probability of > 1σ (> 2σ) bias, BNS, too-narrow `p(μ)` | 54% (19%) | bright sirens | arXiv:2402.19476 | Sect. VI |
| Knowledge needed to model `p(μ)` | H0 to 2, `Ω_m` to 0.02, `σ_8` to 0.07 | bright sirens | arXiv:2402.19476 | Sect. VI |
| Astrometry for < 5% on H0 | 0.6 mas for 1″ separation and 1-day delay | lensed transient | arXiv:2502.04472 | Sect. 3.2, Eq. 6 |
| H0 floor from GW timing | `≲ 10` m s⁻¹ Mpc⁻¹ for delays `≳` hours | lensed GW | arXiv:2502.04472 | Sect. 3.1 |
| Lens-prior-only H0 error, quad with `θ_E = 0.5″` | about 12% | mock | arXiv:2502.04472 | Sect. 4.1 |
| ET detections and lensed events per year | 10⁴–10⁵; 50–100 lensed | **forecast** | arXiv:1703.04151 | abstract |

Table 7 is described as "computed for galaxy- and cluster-scale lenses
separately"; the header row naming which column pair is which was not in the
text read, so the pairs are not labelled here.

## What goes wrong

- **False lensing pairs grow as `N²`.** The number of random pairs grows as
  `N²` while lensed events grow as `N`; with simple overlap criteria false
  alarms dominate at design sensitivity "even when selecting the highest SNR
  pairs", and raising the SNR threshold shrinks the lensed sample as
  `~1/SNR³` (arXiv:2201.04619) [src: abstract]. A later study argues that
  improved parameter precision "will efficiently weed out false alarms" and
  places a first confident detection in O5 (arXiv:2510.23238) [src: abstract;
  **forecast**]. Test: an FPP from an unlensed background in real noise, and
  a Bayes factor that includes population and selection (Step 4).
- **Waveform systematics mimic lensing.** For GW231123 the point-lens Bayes
  factor falls from `10^3.8` to `10^0.1` as the waveform changes, and "the
  favoring of lensing decreases for waveform models more favored by the data";
  extra lens freedom can absorb waveform–data mismatch [src:
  arXiv:2512.16347, Sect. VI.1]. Tests: several waveform families,
  single-detector runs (Hanford and Livingston), and noise studies [src:
  Sect. VI.1, VI.6].
- **`H0` from a lens redshift alone.** Huang et al. 2023 claim 0.3–2% on H0
  from one lensed TianQin event with the lens redshift as the only
  electromagnetic input (arXiv:2304.10435) [src: abstract]. Poon &
  Hannuksela 2026 show that with a point lens the measured delay and the two
  effective distances `d_L/√|μ|` fix `y`, `μ±`, `d_L` and `M_L`, leaving two
  equations (their Eq. 3) for three unknowns `(η_L, z_S, H0)`; for `z_L = 0.5`,
  `M_L = 10^12 M☉`, `(5 kpc, 1, 67.66)` and `(4.73 kpc, 1.5, 111.45)` give the
  same `d_L = 6776` Mpc and `y = 0.372`. The general form is the similarity
  transformation degeneracy: lens modelling fixes only dimensionless
  parameters, `y`, `T* = (1 + z_L)/c × D_L D_S / D_LS × θ_E²` and `d_L`;
  besides `z_L`, either `z_S` or `θ_E` is needed, and with a mass sheet H0 "may
  remain unresolvable" (arXiv:2608.28765) [src: main text, Eq. 1–3, footnote
  2]. Test: check that the Fisher matrix and the sampler agree; an MCMC that
  "resolves" a degeneracy the Fisher matrix shows is suspect [src: same].
- **Mass-sheet degeneracy survives.** It is "also present when using lensed
  GWs"; a neutron-star merger is standardisable only to about 10%, so many
  events are needed to use magnifications, and microlensing still affects
  them; in the interference and wave-optics regimes a single waveform can
  break it (arXiv:2502.04472) [src: Sect. 3.4]. The ms-delay forecast of
  about 10% on H0 without astrometry omits the mass sheet (Sect. 4.2).
- **Host identification uses an H0 prior.** The Bayes factor that ranks
  candidate hosts requires `H0^Δt` and `H0^dL` to fall in U(60, 80) against a
  wide alternative U(0, 1000) (arXiv:2004.13811) [src: App. A.5, Eq. 14–16].
  An H0 measured on hosts selected this way is conditioned on the prior range.
- **Missing or wrong `σ_WL`.** "Any cosmological analysis using binary mergers
  at `z ≳ 0.5` not including a weak lensing term has a high probability of
  being biased by more than 1σ"; generating `σ_WL` with too-low `h` and `Ω_m`
  raises the probability of a > 1σ bias by 1.5–3 times; a `p(μ)` broader than
  the small-area simulations raises it by 3 (BNS) or 10 (SMBHB)
  (arXiv:2402.19476) [src: Sect. VI]. Canevarolo & Chisari find, for an ET
  bright-siren scenario, a lensing bias "comparable to or greater than the
  expected statistical uncertainty", varying between catalogue realisations
  (arXiv:2310.12764) [src: abstract]. Test: repeat with several realisations
  and with `σ_WL` from at least two simulations.
- **Selection shifts `⟨μ⟩`.** With detection selection "flux conservation is
  no longer enforced" and the bias is multiplicative and does not average
  down (arXiv:2204.05434) [src: Sect. 3.2.1]; Eq. 9–10 of arXiv:2402.19476 is
  the correction.
- **Morse phase taken for a waveform error, or missed.** Type-II images near
  threshold "might be missed with standard template bank searches"
  (arXiv:2204.05434) [src: Sect. 3.3]; the LVK runs a dedicated type-II search
  [src: arXiv:2512.16347, Sect. III.2.1].

## Reading list

- Foundation, regimes: LISA Cosmology Working Group 2022, arXiv:2204.05434,
  Sect. 3 — `w`, `F(w)`, Morse phases, weak lensing as noise and as signal.
- Foundation, population bias: Dai, Venumadhav & Sigurdson 2016,
  arXiv:1605.09398 — the magnification–mass–redshift degeneracy (Eq. 1, 5).
- Method, weak-lensing error: Mpetha et al. 2024, arXiv:2402.19476 — `σ_WL`
  fitting form, the factor 1/2, the bias test.
- Method, search: LVK GWTC-4.0 lensing, arXiv:2512.16347 — the tiered
  workflow, priors, thresholds, rates, GW231123.
- Application, earlier run: LVK full O3, arXiv:2304.08393 — the same families
  of searches, no evidence.
- Method, cosmography: Liao et al. 2017, arXiv:1703.04151 — lensed siren +
  host gives `D_Δt`.
- Method, dark lensed siren: Hannuksela et al. 2020, arXiv:2004.13811 — host
  identification and H0 without a counterpart.
- Review: Birrer et al. 2025, arXiv:2502.04472, Sects. 3–4 — timing,
  astrometry, mass sheet.
- Critique, false alarms: Çalışkan et al. 2022, arXiv:2201.04619; reply in
  spirit: Barsode et al. 2025, arXiv:2510.23238.
- Critique, degeneracy: Poon & Hannuksela 2026, arXiv:2608.28765, on Huang et
  al. 2023, arXiv:2304.10435.
- Critique, de-lensing: Wu et al. 2022, arXiv:2211.15160.

## Not verified

- The ET science case Sect. 2.3.3 (arXiv:2503.12263) and Zhao et al. 2026
  Sects. 3.1.2 and 5.3 (arXiv:2605.08595) were not read for this dossier.
- Hirata, Holz & Cutler 2010 and Cusin & Tamanini 2021 were not fetched; they
  are quoted as cited in arXiv:2402.19476.
- The column labels of Table 7 of arXiv:2512.16347 (galaxy or cluster lenses).
- The earlier paper on the similarity transformation degeneracy cited by
  arXiv:2608.28765 (its ref. [2]) was not identified.
- The O1–O3a lensing searches and the O3 rate numbers (arXiv:2304.08393 read
  at abstract level only).
- Lensed FRBs and lensed GRBs as timing sources (mentioned in arXiv:2502.04472
  Sect. 3.1) were not researched.
- The Bilby likelihood issue referred to in arXiv:2512.16347 Sect. IV.1.1.
