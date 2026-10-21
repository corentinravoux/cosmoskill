# Lyα emitters as a neutral-fraction probe — cosmo-reionization-21cm dossier

Scope: how a neutral fraction is inferred from Lyα equivalent widths of
UV-selected galaxies (line measurement with JWST and from the ground,
completeness and slit loss, the post-reionisation baseline, the IGM
transmission model and the likelihood), how the narrow-band
luminosity-function route differs, and how to choose between baselines,
line profiles, simulations and summary statistics.
Snapshot: 2026-10-21.
From: SKA EoR/CD synergies chapter (Chakraborty et al. 2026,
arXiv:2606.30947), Sects. 2.2 and 4.1.2; Bernal & Kovetz 2022 review
(arXiv:2206.15377), Sect. 2.4.

Already in L2, not repeated here: the x_HI values per redshift and per
paper in `results.md#neutral-fraction-against-redshift`; the z ~ 5–6
baseline numbers and PASSAGE in `results.md#lyalpha-emitters-as-a-reionisation-probe`;
the threshold, environment and field-variance systematics in
`systematics.md#lyalpha-visibility`; the origin of the method in
`physics-and-methods.md#lyalpha-emission-from-galaxies`.

## How it is done
<!-- key: how-it-is-done -->

Notation. W (or EW) is the rest-frame Lyα equivalent width; W_obs =
W_em × T_IGM, with T_IGM the fraction of the emergent line transmitted by
the IGM (Mason et al. 2018, arXiv:1709.05356, Sect. II.1.3). The "Lyα
fraction" X_Lyα is the fraction of UV-selected galaxies with W above a
threshold (25 Å by convention, after Stark et al.; arXiv:2408.01507, Sect.
III.2). x̄_HI is the volume-averaged neutral fraction unless stated; Kundu et
al. use mass-weighted cells (arXiv:2609.40363, Sect. II.1).

### Step 1. Measure the line, or its limit, at the systemic redshift
<!-- key: step-1-measure-the-line-or-its-limit-at-the -->

JWST/NIRSpec practice, as in the public-archive sample of Tang et al. 2024
(arXiv:2408.01507, Sects. II.2 and II.5) [src]:

- Systemic redshift from rest-optical lines (Hγ, Hβ, [O III], Hα) fitted with
  Gaussians and averaged with S/N weights; 204 emission-line sources at
  6.533 < z_sys < 12.513; Lyα detected at S/N > 3 in 33 of 210.
- Grating spectra: flat (f_ν) continuum fitted at rest 1300–1400 Å, not
  below 1300 Å "to avoid potential damped Ly α absorption"; detections
  fitted with an asymmetric Gaussian; non-detections get a 3σ limit from the
  error spectrum integrated over ±1000 km/s of systemic, a window that
  "ensures we capture the entire Ly α profile".
- Prism spectra: R ~ 30 at the blue end spreads Lyα across the break, so
  the continuum is a power law at 1300–1600 Å times a Heaviside break, and
  the line is integrated over rest 1170–1270 Å (≈ 6 pixels). For 9 galaxies
  detected in both modes, EWs agree with a scatter of ~0.09 dex.
- Median 3σ EW limits: < 36 Å (grating, 85 non-detections), < 44 Å (prism,
  159 non-detections).
- A wavelength-dependent slit-loss correction assuming a point source is
  applied in the reduction (Sect. II.1).
- Lyα escape fraction from Case B with T_e = 10⁴ K: F_int(Lyα) = 8.7
  F(Hα), 25.0 F(Hβ) or 53.6 F(Hγ), dust-corrected with Balmer decrements
  (median E(B − V) = 0.01).

DIVER (Zhu et al. 2026, arXiv:2608.19311, Sects. II.2 and II.4) [src] fits
the line with a single Gaussian and by direct summation, masking −700 to
+1400 km/s for the baseline, and takes the continuum and Hα from SED fits
to JADES photometry because grating continua are too weak. Its median 3σ
EW limits are 15.6 Å (grating) and 74.4 Å (prism), so the prism sample
cannot test a 25 Å threshold for typical galaxies [der: 74.4 > 25]. It
defines an effective visibility f_esc,Lyα^eff ≡ L_Lyα / (8.7 L_Hα,obs)
(Eq. 5), with Hα not dust-corrected, and writes it schematically as
f_Lyα^ISM T_CGM T_IGM (a_Lyα/a_Hα) 10^{0.4 A_Hα} (Eq. 6), where a is the
aperture recovery and A_Hα the Hα attenuation; slit loss and dust thus
enter the statistic by construction.

Ground-based practice (MMT/Binospec, Prieto-Lyon et al. 2025,
arXiv:2509.18302, Sect. 3.1) [src]: completeness from Monte Carlo
injection of Gaussian lines into non-detected slits, > 50% at FWHM = 100
km/s for flux ≳ 10^−17.2 erg s⁻¹ cm⁻², but ≳ 10^−16.7 for lines broader
than 500 km/s, sky lines dominating losses; slit loss from a two-exponential
surface-brightness model (0.3 kpc core with 35% of the flux, 3.8 kpc halo
with 65%) convolved with the PSF, giving 65–70% of the flux captured in a
1.7″ extraction. The pre-JWST z ~ 7 sample of Mason et al. had 68 LBGs
over 8 fields of ~50–100 arcmin², 12 detections, EW limits from injected
lines, with "a conservative minimum flux that could be measured over the
entire wavelength range" [src: arXiv:1709.05356, Sect. IV.2].

### Step 2. Fix the emergent (post-reionisation) EW distribution
<!-- key: step-2-fix-the-emergent-post-reionisation -->

Every analysis assumes the distribution emerging from the ISM and CGM does
not evolve, so that the change of the observed distribution with redshift
is due to the IGM (Mason, Sect. II.1.3; Kundu, Sect. II.2) [src]. The
forms in use:

| Analysis | Baseline sample | Form | Fitted parameters | Place read |
|---|---|---|---|---|
| Mason et al. 2018 | 127 z ~ 6 LBGs, VLT/FORS2, 63% detected | exponential + delta: p₆(W | M_UV) = (A/W_c) e^(−W/W_c) H(W) + (1 − A) δ(W) (Eq. 4) | A = 0.65 + 0.1 tanh[3(M_UV + 20.75)], W_c = 31 + 12 tanh[4(M_UV + 20.25)] Å | arXiv:1709.05356, Sect. II.1.3 |
| Tang et al. 2024 | z ~ 5 composite (ground, MUSE and DEIMOS) | log-normal in EW; μ ∈ [0, 6], σ ∈ [0.01, 3] flat | per redshift bin | arXiv:2408.01507, Sect. III.1 |
| Prieto-Lyon et al. 2025 | z ~ 5–6 galaxies, MMT/Binospec and NIRCam slitless | exponential; A ≈ 1 (no peak at zero) | EW₀ = 11.2(M_UV + 20) + 27.2 Å (Eq. 15); no dependence on β | arXiv:2509.18302, Sect. 5.2 |
| Kundu et al. 2026 | z ~ 6, −20.25 < M_UV < −18.75, from Tang et al. | log-normal (Eq. 5): e^μ = 8 (+4/−3) Å, σ = 1.85 (+0.42/−0.33) | deconvolved for the z = 6 transmission (Eq. 4) | arXiv:2609.40363, Sect. II.2, Table 1 |

In Mason's form, A absorbs both non-emitters and low-redshift interlopers
(≤ 29% if all non-detections were interlopers), assumed equally small at
z ~ 7 [src: Sect. II.1.3]. Kundu et al. deconvolve the observed z = 6
distribution for the transmission at z = 6, P_in(EW_in) = ∫ dT T P_α(T)
P₆(EW_in T) (Eq. 4), because blue-side absorption remains after
reionisation and some red-side wing persists near its end [src: Sect.
II.2]. They flag that σ in the source table is labelled dex but is the σ of
ln EW [src: Table 1 note].

The Lyα fraction implied by Prieto-Lyon at M_UV = −19.5 is 45 ± 5%,
against 35 ± 7% from Tang et al. 2024a, as quoted there [src:
arXiv:2509.18302, Sect. 5.2].

### Step 3. Model the transmission through the IGM
<!-- key: step-3-model-the-transmission-through-the -->

The common structure (Mason et al. 2018, Eqs. 5–6):
τ_IGM(z, v) = τ_D(z, v) + τ_HII(z, v), and
T_IGM(x̄_HI, M_h, Δv) = ∫₀^∞ dv J_α(Δv, M_h, v) e^(−τ_IGM), where τ_D is the
damping-wing optical depth of neutral patches, τ_HII the resonant opacity
of infalling and residual gas in the local H II region, J_α the emergent
line profile and Δv its velocity offset from systemic [src]. Choices of
each analysis:

| Ingredient | Mason et al. 2018 | Tang et al. 2024 | Kundu et al. 2026 |
|---|---|---|---|
| τ_HII | e^(−τ_HII) = H(v − v_circ): all flux below the circular velocity absorbed | same, τ_HII = ∞ at v ≤ v_c (M_UV = −19 → zero transmission below 140 km/s) | blue side of systemic fully absorbed, infall neglected |
| Line profile | Δv log-normal in halo mass (Eqs. 1–2), m = 0.32 ± 0.07, c = 2.48 ± 0.03, σ_v = 0.24 ± 0.02 from 158 z ~ 2–3 galaxies | z ~ 5 composite, peak Δv ≃ 230 km/s, FWHM ≃ 300 km/s | Gaussian centred at 2 v_out (shell back-scattering), σ_v = v_circ, v_out = a v_circ with a = 0 or 1 (Eqs. 6–7) |
| Neutral gas | EoS 21cmFASTv2, 1.6 Gpc, 1024³, "Faint Galaxies" (ζ = 20), x̄_HI = 0.01–0.95 in steps ~0.02 | bubble radius R_b drawn from 21cmFAST distributions ("gradual" model), x_HI = 1 outside the bubble | THESAN-1 RMHD, 95.5 cMpc, 2100³ particles, mass-weighted x_HI on 512³ grids |
| τ_D | along thousands of sightlines to haloes of 10¹⁰–10¹² M_⊙ | integral of x_HI n_H σ_α from z_s to z_reion ≃ 5.3 (Mason & Gronke form) | cell sum of Miralda-Escudé expression (Eqs. 9–11) to z = 5.5 |
| Place read | arXiv:1709.05356, Sects. II.1.1, II.2, III.1 | arXiv:2408.01507, Sect. IV.2 | arXiv:2609.40363, Sects. II.1, II.3 |

Kundu's transmission is T_α = ∫₀^∞ dν L_ν e^(−τ_DW) / ∫ dν L_ν (Eq. 8), so
T_α → ½ without outflows when τ_DW → 0: half the Gaussian is blue of
systemic [src: Sect. II.3.2]. The Gunn–Peterson depth used there is τ_GP =
3.8 × 10⁵ [(1 + z_s)/7]^{3/2} [Ω_b h²/0.0223] [Ω_m h²/0.142]^{−1/2}
[(1 − Y)/0.76] (Eq. 10) [src]. Mason's reason for a halo-mass rather than
UV-magnitude relation for Δv: galaxies of equal M_UV at different
redshifts have different masses, and Δv ∝ M_h^0.32 tracks the circular
velocity v_c ∝ M_h^{1/3} [src: Sect. II.1.1]. Tang's reason for ignoring
infall in its conclusions: at the sample's M_UV and with z ~ 5 offsets,
infall does not drive the decline [src: Sect. IV.2].

### Step 4. Build the likelihood and sample
<!-- key: step-4-build-the-likelihood-and-sample -->

Mason et al. forward-model 10⁶ galaxies per halo and x̄_HI, giving
p(W | x̄_HI, M_UV) = A f(W, x̄_HI) H(W) + (1 − A) δ(W) (Eq. 13), with f a
Gaussian kernel density estimate [src: Sect. III.1]. For a detection with
Gaussian error σ_i the likelihood is the convolution of Eq. 10; for a
non-detection, the integral below the limit (Eq. 11); the prior on x̄_HI
is uniform on [0, 1] (Eq. 9) [src: Sect. III]. Δv is marginalised; if it is
measured, a narrower posterior follows [src: Sect. III.1]. Tang et al. use
the same product of per-galaxy terms with p(EW | x_HI) = p_z~5(EW/T_IGM)
and emcee; because NIRSpec has no OH sky lines, a non-detection is
p(x < x_3σ) [src: arXiv:2408.01507, Sects. III.1, IV.2]. Kundu et al.
model the fraction of galaxies above EW thresholds per M_UV bin, from
Eq. 3, rather than individual EWs [src: arXiv:2609.40363, Sect. II.2].

In joint analyses, one Lyα-emitter clustering estimate (x̄_HI = 0.3 ± 0.2
at z = 6.6) enters as a contaminated upper limit, and published x̄_HI
PDFs from emitter fractions enter as spline priors on x̄_HI(z) [src:
Sims et al. 2025, arXiv:2504.09725, Sect. 3.4.3, Eq. 21; Sect. 3.4.4,
Eq. 22].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Which baseline
<!-- key: which-baseline -->

- **z ~ 6 or z ~ 5.** Mason uses z ~ 6 and assumes the Universe fully
  ionised there [src: arXiv:1709.05356, Sect. II.2]; with a late end of
  reionisation (`results.md#end-of-reionisation-from-the-lyalpha-forest`)
  that assumption leaks residual neutral gas into the baseline. Tang uses
  z ~ 5 "at which the IGM damping wing attenuation is expected to be
  minimal" [src: Chen et al. 2025, arXiv:2505.24080, Sect. V.2]; Kundu
  keeps z ~ 6 but removes the z = 6 transmission by Eq. 4 [src].
- **Exponential or log-normal.** Tang finds the choice does not change the
  fractions significantly [src: arXiv:2408.01507, Sect. III.1]. Kundu
  finds the exponential (Mason) model gives Lyα fractions higher by
  ≈ 0.1–0.2 at z ≲ 8, still inside the observed errors [src:
  arXiv:2609.40363, Sect. III.6].
- **EW distribution or bright-end luminosity function.** Kundu attributes
  its better agreement with data, relative to an earlier THESAN analysis,
  to calibrating on the EW distribution rather than on narrow-band LAE
  luminosity functions at L_α ~ 10^42.5–10^43.8 erg/s: those reach only
  EW ≥ 113 Å at M_UV = −18.75 and EW ≥ 28 Å at −20.25, against medians of
  10 ± 2 Å and 16 ± 3 Å at M_UV = −19.5 and −18.5 [src: Sect. III.7]. The
  earlier model gave a median EW of ~70 Å at M_UV = −18.5 [src].

### Line profile and velocity offset
<!-- key: line-profile-and-velocity-offset -->

The z ~ 5–6 lines are broader, and offsets at z > 5 lie above the
pre-JWST predictions [src: arXiv:2509.18302, Sect. 6.2]. Broader lines put
more flux at red velocities, where the wing is weaker [src]. Three z > 6
sources lie above the FWHM–Δv relation (Δv ≳ 2 FWHM), possibly because the
IGM already removes flux near line centre [src]. In Kundu's tests, a
double-peaked profile with outflows gives fractions between the a = 0 and
a = 1 Gaussian cases, so the calibration, not the profile, drives its
differences from earlier work [src: arXiv:2609.40363, Sect. III.7].

### Simulation and topology
<!-- key: simulation-and-topology -->

Mason uses the "Faint Galaxies" run only, because morphology information
is "mostly smeared out" for galaxies spread over Δz ≳ 0.1; sensitivity
returns with Δz ~ 0.01 samples [src: arXiv:1709.05356, Sect. II.2]. The
cost: the inference is conditional on one topology and one ζ. Kundu's
THESAN box is 95.5 cMpc, below the ≥ 100 Mpc that Mason says is needed to
model fluctuations on tens of Mpc [src: arXiv:1709.05356, Sect. II.2;
arXiv:2609.40363, Sect. II.1]; Kundu wraps sightlines periodically, so
bubble "sizes" can exceed the box length [src: Sect. II.4]. Its bubble size
is a one-dimensional skewer length to the first cell with x_HI > 0.5, not
a spherical radius [src].

### Individual EWs, fractions, or the upper envelope
<!-- key: individual-ews-fractions-or-the-upper-envelope -->

- Full EW likelihood (Mason, Tang): uses limits and detections jointly.
- Fractions above a threshold (Kundu): simpler to compare across papers,
  but threshold-dependent (`systematics.md#lyalpha-visibility`).
- Upper envelope (DIVER): the 95th percentile T₉₅ of f_esc,Lyα^eff,
  calibrated on simulations as p95(f_esc,IGM) = max[0, 1 − A⟨x_HI⟩²] with
  A = 0.886 (Eq. 15); since non-IGM attenuation can only lower the
  envelope, inverting gives a ceiling on ⟨x_HI⟩ (Eq. 16) [src:
  arXiv:2608.19311, Sect. V]. The quadratic form is motivated by Poisson
  encounters with neutral structures (Eqs. 10–13) and the authors "caution
  that it may not be a general law" [src]. Unlike dark pixels, the ceiling
  needs a simulation calibration [src].

### Luminosity function instead of equivalent widths
<!-- key: luminosity-function-instead-of-equivalent-widths -->

Narrow-band surveys select emitters by line flux and compare the Lyα
luminosity function (LF) with a post-reionisation reference; two routes:
- **Density ratio (LAGER).** T(6.9)/T(5.7) = (ρ_Lyα ratio)/(ρ_UV ratio)
  (Eq. 8), assuming unchanged ISM and stellar populations over 200 Myr:
  0.63 (+0.13/−0.15) over 0.63 ± 0.09 gives 1.0 (+0.26/−0.28) [src:
  arXiv:2105.12191, Sect. VIII.1.3]. The conversion is model dependent:
  from T > 0.72 (1σ), three McQuinn radiative-transfer models give
  x_HI < 0.16, 0.33, 0.11, a volume test < 0.04 and analytic bubble models
  < 0.16; the paper adopts x_HI < 0.33 at z = 6.9 [src: Sect. VIII.1.4, Table 4].
- **Forward model (SILVERRUSH).** 21cmFAST maps of one scenario at x_HI =
  0–0.975 laid on the density field; UV LF turned into a Lyα LF with a
  z ~ 6 EW distribution; damping wings along sightlines; 100 sub-volumes of
  Δz = 0.1; fit only log L_α = 42.4–43.4 (resolution below, AGN above
  43.5); Gaussian likelihood, uniform prior. Result: x_HI < 0.05 at z = 5.7,
  0.15 (+0.10/−0.08), 0.18 (+0.14/−0.12), 0.75 (+0.09/−0.13) at 6.6, 7.0,
  7.3; clustering gives 0.06 and 0.21 at 5.7 and 6.6 [src: arXiv:2411.15495, Sect. V.4].
- **Systematics.** LFs at one redshift differ by factors ~2 between
  surveys; EW limits (0–48 Å on a common spectrum) explain up to ~1.6 in
  density; veto-band masking (~15–40% of area, ~9% for the z = 5.7
  reference) lowers φ* if ignored [src: arXiv:2105.12191, Sects.
  VIII.1–VIII.1.2]. Cosmic variance sets a floor Δx_HI ~ 0.2 at x_HI = 0.3
  for a 2 deg², Δz = 0.5 survey; only many independent fields reduce it
  [src: arXiv:2305.04949]. The bright end (L > 10^43.4 erg/s) does not
  evolve from z = 5.7 to 6.6, read as bubbles around luminous emitters
  [src: arXiv:2506.13854].

### Field average or structure by structure
<!-- key: field-average-or-structure-by-structure -->

In the EGS, 26 ± 10% of z = 6.5–8 galaxies have EW > 25 Å, twice the
other three fields, with no downturn from z ~ 6 [src: arXiv:2408.01507,
Sect. III.4]. Chen et al. infer a mean transmission per overdensity with
a flat prior on T ∈ [0, 1] against the z ~ 5 log-normal (μ = 2.38, σ =
1.63): T = 0.52 (+0.28/−0.22) and 0.55 (+0.23/−0.22) for the z ≃ 7.2
GOODS-S and z ≃ 7.1 GOODS-N structures, against T = 0.61 expected for R_ion
= 2 pMpc [src: arXiv:2505.24080, Sect. V.2]. Overdensities are bins of
dz = 0.2 (≈ 6–8 pMpc) at least 3 times the median count of FRESCO [O III]
emitters above 2 × 10⁻¹⁸ erg s⁻¹ cm⁻² Å⁻¹, which selects mostly M_UV <
−19.7 galaxies in an "on" mode of star formation [src: Sect. IV.1]. The EGS
z = 7.0–7.6 region, 10 emitters with 3 above 100 Å, needs 2–3 bubbles of
R ~ 2–4 pMpc or one of R ≳ 12 pMpc, "extremely rarely seen in standard
reionization simulations" [src: Sect. V.2, Fig. 11 caption].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Lyα fraction (EW > 25 Å) | 30 ± 7% (z ~ 5), 24 (+10/−9)% (z ~ 6), 18 (+7/−6)% (z = 6.5–8), 8 (+9/−6)% (z = 8–10), 0 (+14/−0)% (z = 10–13.3) | JWST archive | arXiv:2408.01507 | Sect. III.2 |
| EW > 50 Å, > 100 Å at z = 6.5–8 | 9 (+5/−4)%, 4 (+3/−2)% | same | arXiv:2408.01507 | Sect. III.2 |
| x̄_HI | 0.48 (+0.15/−0.22) (z = 6.5–8); 0.81 (+0.12/−0.24) (8–10); 0.89 (+0.08/−0.21) (10–13.3) | same | arXiv:2408.01507 | Sect. IV.2 |
| Ground to NIRSpec MSA flux | NIRSpec ≃ 0.8 × ground (1.5″ apertures) | Tang et al. | arXiv:2408.01507 | Sect. III.2 |
| Average Lyα slit loss, NIRSpec vs FORS2 at z ≃ 6 | 35 ± 10% (as quoted) | DIVER | arXiv:2608.19311 | Sect. II.4 |
| Median 3σ EW limits | 36 Å grating, 44 Å prism (Tang); 15.6 Å grating, 74.4 Å prism (DIVER) | JWST | arXiv:2408.01507; arXiv:2608.19311 | Sect. II.5; Sect. II.4 |
| Prism vs grating EW scatter | ~0.09 dex (9 objects) | Tang et al. | arXiv:2408.01507 | Sect. II.5 |
| Slit capture, Binospec | 65–70% in 1.7″ | Prieto-Lyon et al. | arXiv:2509.18302 | Sect. 3.1.2 |
| Completeness, Binospec | > 50% at ≳ 10^−17.2 (FWHM 100 km/s) or ≳ 10^−16.7 erg s⁻¹ cm⁻² (> 500 km/s) | same | arXiv:2509.18302 | Sect. 3.1.1 |
| Lyα fraction at M_UV = −19.5, z ~ 5–6 | 45 ± 5% (vs 35 ± 7% Tang 2024a) | same | arXiv:2509.18302 | Sect. 5.2 |
| Δv–M_h relation | m = 0.32 ± 0.07, c = 2.48 ± 0.03, σ_v = 0.24 ± 0.02 | Mason et al. | arXiv:1709.05356 | Eqs. 1–2 |
| Cosmic variance of the z ~ 7 sample | ~6% in the Lyα optical depth (as quoted) | Mason et al. | arXiv:1709.05356 | Sect. IV.2 |
| Envelope calibration | A = 0.886 | DIVER | arXiv:2608.19311 | Eq. 15 |
| Mean transmission in overdensities | 0.52, 0.55 (R_ion = 2 pMpc → 0.61) | Chen et al. | arXiv:2505.24080 | Sect. V.2 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Aperture mismatch between baseline and target.** Ground and NIRSpec
  fluxes differ by a factor ≈ 0.8 [src: arXiv:2408.01507, Sect. III.2];
  DIVER applies no slit-loss correction and pairs grating Lyα with SED Hα
  from different apertures, keeping only a uniform relative scale [src:
  arXiv:2608.19311, Sect. II.4]. Test: rescale the baseline to the target
  aperture and propagate the factor's error.
- **Limits too shallow for the threshold.** A 74 Å prism limit says nothing
  about EW > 25 Å (`#numbers`). Test: use the full likelihood with
  per-object limits, or restrict to the grating sample.
- **Redshift window and interlopers.** Pre-JWST samples needed the line in
  the observed window; ~48% of one lensed subsample could lie above it,
  checked by excluding it [src: arXiv:1709.05356, Sect. IV.2]. Systemic
  JWST redshifts remove this.
- **AGN among emitters.** In Abell 2744, 3 of the 4 z ≃ 7–8 emitters appear
  to be broad-line AGN [src: arXiv:2408.01507, Sect. III.4]. Test: remove
  AGN before the fit.
- **Environment.** Strong emitters avoid overdensities in DIVER and
  cluster in the EGS; both depart from a uniform screen
  (`systematics.md#lyalpha-visibility`; arXiv:2505.24080, Sect. V.2). Test:
  fit field by field (Tang Table 3 does this).
- **Assumed non-evolving emergent distribution.** If dust falls with
  redshift, the emitted EW rises and the inferred suppression is
  underestimated [src: arXiv:1709.05356, Sect. II.1.3].
- **Infall treatment.** A step at v_circ removes all flux below ~140 km/s
  for M_UV = −19 [src: arXiv:2408.01507, Sect. IV.2]; Kundu neglects
  red-side infall [src: arXiv:2609.40363, Sect. II.3.2]. Report which.
- **Table units.** σ of a log-normal labelled dex but defined on ln EW
  [src: arXiv:2609.40363, Table 1 note].

## Reading list
<!-- key: reading-list -->

- Method: Mason et al. 2018, arXiv:1709.05356 — forward-modelled EW
  likelihood with non-detections; Δv–halo-mass relation.
- Application: Tang et al. 2024, arXiv:2408.01507 — JWST/NIRSpec
  measurement recipe (grating and prism), log-normal fit, x̄_HI to z = 13.
- Data: Prieto-Lyon et al. 2025, arXiv:2509.18302 — z ~ 5–6 baseline,
  completeness and slit-loss modelling, line widths and offsets.
- Application: Kundu et al. 2026, arXiv:2609.40363 — THESAN transmission,
  deconvolved baseline, threshold and calibration tests.
- Application: Chen et al. 2025, arXiv:2505.24080 — transmission per
  overdensity, bubble sizes.
- Critique: Zhu et al. 2026, arXiv:2608.19311 — effective visibility,
  environment, upper-envelope ceilings.
- Application: Sims et al. 2025, arXiv:2504.09725 — how emitter results
  enter a joint likelihood.

## Not verified
<!-- key: not-verified -->

- Luminosity-function route: the SILVERRUSH IV (Konno et al.) z = 5.7 and
  6.6 LFs used as references, the McQuinn et al. models and the HEROES
  method sections were not read; the clustering route only as far as
  arXiv:2411.15495, Sect. V.4.
- Lu et al. bubble-size distributions and Mason & Gronke transmission
  integral (used by arXiv:2408.01507) were not read.
- The 35 ± 10% slit loss is quoted by arXiv:2608.19311 from Napolitano et
  al.; that paper was not read and no identifier is recorded.
- Kundu et al. results sections III.1–III.5 were not read beyond what L2
  holds.
