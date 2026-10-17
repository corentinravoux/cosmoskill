# Hydrodynamical sub-grid calibration — cosmo-simulations-mocks dossier

Scope: how a galaxy-formation suite fixes its feedback parameters (targets,
weights, emulator, priors), how it handles resolution (strong or weak
convergence), how its variants are defined, and which observational biases in
the calibration data (hydrostatic mass, apertures, Eddington bias, selection)
it models, compared across FLAMINGO, BAHAMAS, EAGLE, IllustrisTNG, SIMBA and
CAMELS. Snapshot: 2026-10-17. From: Crain & van de Voort 2023, Sects. 2.2–2.5;
Angulo & Hahn 2021, Sect. 7.8.1.

Already in L2, not repeated here: the solvers and the founding sub-grid recipes
(`physics-and-methods.md#hydrodynamics-and-sub-grid-models`); box, particle
masses and run counts of each suite
(`physics-and-methods.md#what-the-main-suites-ran`,
`surveys-and-data.md#hydrodynamical-suites-galaxy-formation`); the spread of
the baryonic P(k) response between suites and variants, its volume convergence
and the one-parameter baryon-fraction relation
(`systematics.md#sub-grid-model-dependence`). How a lensing analysis turns
these responses into a prior or a scale cut belongs to `cosmo-weak-lensing`
(`deep/baryonic-feedback.md`).

Symbols used throughout. M_*: galaxy stellar mass; GSMF or SMF: galaxy stellar
mass function; M_500c, R_500c: mass and radius of the sphere of 500 times the
critical density; f_gas,500c: hot gas mass over M_500c inside R_500c; m_g:
initial gas (baryon) particle mass; ΔT_AGN (BAHAMAS writes ΔT_heat):
temperature jump of a thermal AGN heating event; n_heat: number of particles
heated per event; ε_f: fraction of the radiated AGN energy coupled to the gas;
f_SN, Δv_SN: FLAMINGO stellar-feedback energy fraction and target kick
velocity; f_th: EAGLE stellar-feedback energy in units of the type II supernova
energy; β_BH: logarithmic density slope of the Bondi boost factor. Hydrostatic
bias: FLAMINGO's calibration paper writes the ratio b_HSE = M_HSE/M_true (0.74
means masses 26% low, arXiv:2306.05492, Eq. 17); the later FLAMINGO bias study
writes b_HSE ≡ (M_HSE − M_true)/M_true, so the same calibration value appears
as −0.257 (arXiv:2409.07849, abstract and App. C). This file quotes each in the
paper's own convention and says which.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Decide what calibration is for
<!-- key: step-1-decide-what-calibration-is-for -->

EAGLE states the argument every later suite cites. In a self-regulated galaxy,
outflows balance inflows whatever the implemented feedback efficiency, but the
star-formation rate (or black-hole accretion rate) at which that balance is
reached, and hence the stellar (or black-hole) mass, does depend on it; since
the true efficiency is lost to numerical radiative losses and unresolved
physics, stellar and black-hole masses cannot be predicted and must be
calibrated [src: arXiv:1407.7040, Sect. 2.1]. The same argument says the amount
of star-forming gas follows the assumed star-formation law, which is why that
law is set to the observed Kennicutt–Schmidt relation rather than tuned [src:
Sect. 2.1]. The review adds the selection rule for a target: well measured on
scales the simulation resolves, and sensitive to the parameter calibrated; and
warns against reading as predictions properties closely tied to the targets
[src: arXiv:2309.17075, Sect. 2.4].

The suites then split by purpose:

- Galaxy-population suites (EAGLE, IllustrisTNG, SIMBA) calibrate on the
  stellar content of galaxies.
- Large-scale-structure suites (BAHAMAS, FLAMINGO) calibrate on the total
  baryon content of haloes, because the halo baryon fraction, dominated by hot
  gas in groups and clusters, sets how much the matter power spectrum is
  modified; BAHAMAS describes itself as the first to calibrate on massive
  haloes [src: arXiv:1603.02702, Sect. 2.2].
- Parameter-space suites (CAMELS) do not calibrate: they span four feedback
  amplitudes around the fiducial IllustrisTNG and SIMBA models [src:
  arXiv:2010.00619, Sect. III.1–III.2 and Table 1].

### Step 2. Choose the targets and the free parameters
<!-- key: step-2-choose-the-targets-and-the-free -->

| Suite | Calibration targets | Kept in view but not fitted | Parameters adjusted | Place read |
|---|---|---|---|---|
| EAGLE (Ref) | z = 0.1 GSMF and disc-galaxy sizes; the M_BH–M_* relation for AGN feedback (per the review) | many scaling relations as tests | f_th(Z, n_H) (Eq. 14), the accretion viscosity C_visc; ΔT_SF = 10^7.5 K and ε_f = 0.15 fixed | arXiv:1501.01311, Sect. 3 and Table 1; arXiv:2309.17075, Sect. 2.4 |
| IllustrisTNG | cosmic star-formation-rate density, z = 0 GSMF, stellar-to-halo mass relation | black-hole mass relation, halo gas fraction within R_500c, stellar sizes, used to discriminate between acceptable variants | wind velocity and energy scalings, changed by educated guesses aimed at the Illustris tensions | arXiv:1703.02970, Sect. 3.2 |
| SIMBA | GSMF; M_BH–M_* relation via the accretion efficiency | sizes and hot gas fractions, explicitly untuned | wind-velocity normalisation (1.6, from 2 in Mufasa); high-z mass-loading suppression exponent f_a | arXiv:1901.10203, Sects. 2.1, 3.1, 3.6, 3.7; arXiv:2309.17075, Sect. 2.4 |
| BAHAMAS | present-day GSMF and hot gas fractions of groups and clusters | stellar-to-halo mass relation (examined only afterwards) | stellar wind velocity, n_heat, ΔT_heat | arXiv:1603.02702, Sects. 2.2–2.4 |
| FLAMINGO | z = 0 SMF (GAMA, Driver et al. 2022) and f_gas,500c(M_500c) from X-ray and weak lensing | other galaxy, cluster and LSS data as tests | f_SN, Δv_SN, ΔT_AGN, β_BH (only the last two at low resolution) | arXiv:2306.05492, Sects. 2–3 and Table 2 |

Why each target. EAGLE takes the GSMF because it is well constrained and
reproducing it is a precondition for most uses, and it adds sizes because three
of its four GSMF-calibrated models made discs too compact through numerical
losses in dense gas [src: arXiv:1407.7040, Sect. 2.1; arXiv:1501.01311,
abstract and Sect. 3]. FLAMINGO takes the SMF for the galaxy–halo connection
needed by clustering and the gas fractions for their impact on cosmic shear
scales, the same observables as BAHAMAS [src: arXiv:2306.05492, Sect. 3]. It
prefers stellar masses to luminosity functions because at its resolution masses
are better predicted than star formation histories and dust [src: Sect. 3.1.2].

Why those parameters. In EAGLE, ΔT_AGN only weakly affects M_* above 10^11 M_⊙
but strongly affects the intracluster medium, so the GSMF is fitted with
C_visc, which sets the mass where AGN feedback takes over [src:
arXiv:1501.01311, Sect. 3]. In BAHAMAS the GSMF is insensitive to ε_f and
ΔT_heat, so n_heat (raised from 1 to 20, heating 1–3 × 10^10 M_⊙ of gas) fixes
the knee and ΔT_heat the gas fractions; a factor 30 in heated mass moves f_gas
less than 0.2 dex in ΔT_heat, because ejection is set to zeroth order by
ΔT_heat/T_vir [src: arXiv:1603.02702, Sect. 2.3 and App. A]. FLAMINGO fixes
n_heat = 1 because only the product n_heat ΔT_AGN matters and the two are
degenerate [src: arXiv:2306.05492, Sect. 2.3].

### Step 3. Bound the parameters by numerical arguments
<!-- key: step-3-bound-the-parameters-by-numerical -->

FLAMINGO sets its priors from the numerics before any fit [src:
arXiv:2306.05492, Sects. 2.1–2.3]:

- Stellar kicks are drawn with probability p_kick = 2 f_SN ΔE_SNII(t, Δt) /
  (m_ngb Δv_SN²) (Eq. 2), with m_ngb the gas mass in the kernel. Below Δv_SN =
  80 (high resolution) and 200 km/s (intermediate) the kicks lose their effect
  (overcooling or escape speed); above 400 and 800 km/s they are too rarely
  sampled, the expected number of kicks per star particle being ⟨N_kicks⟩ =
  1.85 (f_SN/0.25)(Δv_SN/400 km/s)^−2 (Eq. 3), about 2 and 0.4.
- Bondi accretion (Eq. 4) carries a boost α = max[(n_H/n_H,*)^β_BH, 1] (Eq. 5,
  after Booth & Schaye 2009, arXiv:0904.2572), n_H,* = 0.1 cm^−3, needed
  because the Bondi radius and the interstellar phases are unresolved.
- Thermal feedback is inefficient above n_H,tc = 0.25 cm^−3 (ΔT_AGN/10^7.5
  K)^{3/2} (m_g/1.09 × 10^9 M_⊙)^{−1/2} (Eq. 6, after Dalla Vecchia & Schaye
  2012, arXiv:1203.5667, their Eq. 18). Against the star-formation threshold
  this gives minima log ΔT_AGN = 6.9, 7.2, 6.2 for high, intermediate, low
  resolution; values below 10^7 K are excluded anyway because the formula
  underestimates losses there.
- Self-regulation requires the time between AGN events to be shorter than the
  black-hole growth time, t_AGN/t_BH ≈ 0.98 (m_g/1.09 × 10^9 M_⊙) (n_heat
  ΔT_AGN/10^8.5 K)(m_BH/10^7 M_⊙)^−1 (Eqs. 7–9), hence ΔT_AGN ≲ 10^8.5 K at
  intermediate resolution, 8 times higher (lower) at high (low) resolution. The
  adopted flat priors are narrower than allowed (Table 2) to sample the region
  near the best fit better.

EAGLE had made the same argument to fix ΔT_SF = 10^7.5 K, and motivates f_th >
1 (asymptotic maximum 3) as compensation for numerical losses and for the
unresolved first stellar generations [src: arXiv:1501.01311, Sect. 3.1].

### Step 4. Run a training set and emulate (FLAMINGO) or iterate by hand
<!-- key: step-4-run-a-training-set-and-emulate-flamingo -->

FLAMINGO runs, per resolution, a 32-node maximin Latin hypercube of 2 ×
360³-particle boxes of 100, 200 and 400 comoving Mpc for high, intermediate and
low resolution, a compromise between cost (about 1600, 1300, 800 CPU hours per
run) and the highest cluster mass reached; a box eight times larger showed box
effects negligible [src: arXiv:2306.05492, Sect. 4.1, Table 1]. Haloes come
from VELOCIraptor at z = 0, 0.1, 0.3; stellar masses are 50 kpc 3D apertures
with the Eddington scatter of Step 5 added; the SMF is binned finer than the
data (25 or 40 bins, Poisson errors), f_gas in 20 adaptive bins of at least ten
haloes [src: Sect. 4.2]. One Gaussian process per relation maps x = (log M, θ)
to the observable with a squared-exponential kernel (Eq. 19), inputs in log
where they span decades [src: Sect. 4.3]. Emulator error is a leave-one-out
standard deviation, applied as σ_emu = |σ_crosscheck f(M, θ)| (Eq. 20) [src:
Sect. 4.4].

The others iterated by hand. IllustrisTNG ran perturbations of the model in one
(25 Mpc/h)³ box with 512³ particles, chose the phase whose halo mass function
was closest to the mean of ten, and kept the variant that relieved most of the
Illustris tensions; it declined a formal fit because a fair comparison needs
mock observations, the test box has non-negligible sample variance, and the
model is not resolution independent [src: arXiv:1703.02970, Sects. 3.1–3.2].
BAHAMAS tuned one parameter at a time in 100 Mpc/h boxes at production
resolution [src: arXiv:1603.02702, Sect. 2.3]. EAGLE calibrated four models in
50 cMpc boxes [src: arXiv:1501.01311, Table 1]. CAMELS-based work later fitted
CAMELS-TNG with neural emulators trained on about 1000 runs and implicit
likelihood inference (Jo et al. 2022, arXiv:2211.16461, abstract).

### Step 5. Model the calibration data's biases
<!-- key: step-5-model-the-calibration-data-s-biases -->

| Bias | How FLAMINGO models it | How others handle it | Place read |
|---|---|---|---|
| Eddington bias of stellar masses | lognormal scatter σ(log M_*) = min(0.070 + 0.071z, 0.3) dex added to simulated masses (Eq. 11) | not modelled in the papers read | arXiv:2306.05492, Sect. 3.1.1 |
| Systematic stellar-mass offset (population synthesis, dust) | log₁₀ M_*,obs → log₁₀ M_*,obs + log₁₀ b_*, prior log₁₀ b_* ~ N(0, 0.14) (Eqs. 12–13), mass independent because no prior exists for a mass dependence | — | Sect. 3.1.2 |
| Cosmic variance of the SMF | shift log₁₀ b_cv, prior b_cv ~ N(1, 0.06) (Eqs. 14–15) | — | Sect. 3.1.3 |
| Hydrostatic mass bias | M_500c = M_500c,HSE/b_HSE (Eq. 17), ratio convention, prior N(0.74, 0.10) combining 0.72 ± 0.08 and 0.76 ± 0.06 from X-ray versus lensing comparisons (Eq. 18); its effect on f_gas itself neglected; weak-lensing masses taken as unbiased | BAHAMAS runs a synthetic X-ray pipeline on its haloes and compares X-ray-like quantities; SIMBA compares hot gas (T > 10^5 K) within the true R_500 with the BAHAMAS compilation | Sect. 3.2.1, Eq. 23; arXiv:1603.02702, Sect. 2.4; arXiv:1901.10203, Sect. 3.7 |
| X-ray selection at low mass | cut at M_500c,HSE > 10^13.8 M_⊙, where the median f_gas stops falling, plus one point from a fit at 4 × 10^13 M_⊙ | BAHAMAS: mass-selected simulated sample, notes flux-limited samples may favour gas-rich groups | Sect. 3.2.1; arXiv:1603.02702, Sect. 2.5 |
| Redshift mismatch | X-ray sample cut to z < 0.25 (median 0.1) and matched to z = 0.1; HSC–XXL lensing sample at its median z = 0.3 with a separate emulator | — | Sects. 3.2.1–3.2.2 |
| Stellar aperture | 50 kpc 3D, chosen from mock-observation tests of EAGLE because FLAMINGO galaxies are too large to mock; 30, 50, 100 kpc differ only above about 10^11 M_⊙ | EAGLE and BAHAMAS: 30 pkpc 3D, close to a 2D Petrosian mass | Sect. 4.2 and App. A; arXiv:1407.7040, Sect. 5.1.1; arXiv:1603.02702, App. B |

The compilation: 15 data sets (12 hydrostatic, 3 lensing); the hydrostatic ones
give 581 objects, 533 after averaging duplicates, 310 after the redshift cut,
rescaled to the simulation cosmology with M_500c ∝ h^−1 and f_gas ∝ h^−1.5,
then reduced to medians in eight logarithmic mass bins between 10^13.8 and
10^15 M_⊙ with bootstrap errors [src: arXiv:2306.05492, Sect. 3.2.1 and Table
4]. The lensing data enter as two points of the HSC–XXL power-law fit,
f_gas,500c = 0.054 ± 0.010 at 10^13.5 M_⊙ and 0.106 ± 0.023 at 10^14.5 M_⊙, two
because a two-parameter fit sampled at more masses gives correlated points;
only the lower one fits in the 100 and 200 Mpc boxes [src: Sect. 3.2.2].

### Step 6. Write the likelihood and weight the targets
<!-- key: step-6-write-the-likelihood-and-weight-the -->

Per mass bin, FLAMINGO uses Gaussian terms whose variance adds the data and
emulator errors (Eq. 21 for the SMF, Eq. 23 for X-ray gas fractions, with the
emulator evaluated at M_500c,obs/b_HSE), so that the fit cannot over-fit the
emulator [src: arXiv:2306.05492, Sect. 5]. The total (Eq. 24) averages each
data set over its bins and gives the SMF and the mean of the two gas-fraction
sets equal weight; without that the far better-measured SMF would drive the
fit, while the baryon fractions are what drives the power-spectrum suppression
[src: Sect. 5]. Flat priors stay inside the hypercube to avoid extrapolation;
sampling is emcee with 500 burn-in steps [src: Sect. 5].

### Step 7. Fit the biases once, then each resolution
<!-- key: step-7-fit-the-biases-once-then-each-resolution -->

The three bias parameters are fitted at intermediate resolution only and held
fixed for the other two, since they describe the data, not the model [src:
arXiv:2306.05492, Sect. 6.3]. Their posteriors equal their priors (log₁₀ b_* =
0.06 ± 0.11, b_cv = 0.98 ± 0.06, b_HSE = 0.74 ± 0.09): the fit does not
constrain them, and b_HSE is what lets the X-ray and lensing gas fractions be
fitted together [src: Sect. 6.2 and Table 7]. The one strong degeneracy is β_BH
against b_* [src: Sect. 6.2].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Strong or weak convergence
<!-- key: strong-or-weak-convergence -->

Definitions (EAGLE): strong convergence means results do not change with
resolution at fixed sub-grid parameters; weak convergence means they agree
after recalibration [src: arXiv:1407.7040, Sect. 2.2].

- Weak (EAGLE, FLAMINGO, BAHAMAS's high-resolution check). Buys: the sub-grid
  scale moves with the resolution, and feedback can depend on the local gas
  state. Assumes: calibration is needed anyway. The paper also argues that a
  fixed parameter set is not a fixed physical model, since the energy, mass and
  number of feedback events change with particle mass and time step [src:
  arXiv:1407.7040, Sect. 2.2]. Costs: one calibration per resolution, and
  differences between resolutions can no longer test numerics.
- Strong (IllustrisTNG). Buys, per its authors: truncation errors can in
  principle be reduced arbitrarily, numerical and physical limits are
  separated, tuning is simpler, and the method converges at high enough
  resolution [src: arXiv:1703.02970, App. A]. Costs: stellar masses and star
  formation rates rise with resolution, so TNG300 (8 times coarser in mass than
  TNG100) is multiplied by a correction function from TNG100 against TNG100-2
  ("rTNG300"), TNG100 resolution being the model's target [src:
  arXiv:1707.03406, Sect. 3.3]. The FLAMINGO paper adds that TNG300 and
  MillenniumTNG fit the calibration data less well for this reason [sec:
  arXiv:2306.04024, Sect. 1].
- Achieving strong convergence by design (decoupled winds, cooling switched
  off, feedback scaled with dark-matter velocity dispersion) costs the
  hydrodynamic coupling of winds and adds parameters that can themselves depend
  on resolution [src: arXiv:1407.7040, Sect. 2.2; arXiv:2309.17075, Sect. 2.5].

What the comparisons found. EAGLE's strong test (8 times better mass, 2 times
better spatial resolution in 25 cMpc) raised the GSMF by up to 0.4 dex near
10^9 M_⊙; Illustris's model, built for strong convergence, did about as badly;
the recalibrated run (Recal-L025N0752, ΔT_AGN = 10^9 K instead of 10^8.5 K,
changed f_th density dependence and C_visc, mean f_th 1.07 against 1.06) agrees
within 0.2 dex above 2 × 10^8 M_⊙ [src: arXiv:1407.7040, Sect. 5.1.2]. BAHAMAS,
holding the physical feedback scales fixed (n_heat × 8, seeding at 800 instead
of 100 FoF particles, 384 SPH neighbours), finds stellar and baryon fractions
within about 10% above M_200 = 10^13 M_⊙ but stellar masses up to 40% higher
below 10^12 M_⊙; a weak test (mass loading 2 → 6, lower seeding mass) restores
the stellar fractions and the gas fractions above 10^13 M_⊙, but not those at
10^12–10^12.5 M_⊙ [src: arXiv:1603.02702, App. C]. FLAMINGO's high-resolution
fit needs about twice the stellar energy and half the kick velocity, and β_BH =
0.038 against 0.514, because higher densities are resolved; it reads equally
good fits at three resolutions as weak convergence [src: arXiv:2306.05492,
Sect. 6.3]. TNG reports stellar masses consistent between L25n256 and L25n512
only in haloes above about 2 × 10^12 M_⊙ (50,000 resolution elements) and halo
gas fractions stable at all masses [src: arXiv:1703.02970, App. A]. SIMBA,
otherwise fixed, tunes its high-z mass-loading exponent per resolution (f_a = 2
at its 100 Mpc/h resolution, 1.5 at 8 times finer mass) and calls its high-z
stellar growth "tuned rather than predictive" [src: arXiv:1901.10203, Sect.
2.1].

Even low-resolution FLAMINGO needed more than parameter changes: a lower
star-formation threshold, 10^7 instead of 10^5 M_⊙ seeds and no stellar
feedback, which makes its best-fit values hard to compare with the others [src:
arXiv:2306.05492, Sects. 2, 2.2 and 6.3].

### Emulator fit or hand tuning
<!-- key: emulator-fit-or-hand-tuning -->

The emulator route gives a posterior, an explicit weight per target and an
emulator error in the likelihood, at the price of 32 extra runs per resolution
and per AGN model [src: arXiv:2306.05492, Sects. 4–5 and 6.4]. Hand tuning
(TNG, BAHAMAS, EAGLE) is cheaper and avoids fitting to noise in a small box,
which is TNG's stated reason [src: arXiv:1703.02970, Sect. 3.2], but yields one
point without uncertainty; BAHAMAS writes that it does not claim a unique
solution [src: arXiv:1603.02702, Sect. 2.5]. Implicit-likelihood inference on
CAMELS recovers emulated targets to 0.17% (SFRD) and 0.4% (SMFs) and shows that
the SFRD alone leaves parameters degenerate [src: arXiv:2211.16461, abstract];
fitted to observed SMFs, it leaves about 0.3 dex too few massive galaxies, a
limit of the model or of its six-parameter space [src: Sect. VI.4.1].

### Defining a variant
<!-- key: defining-a-variant -->

| Route | Suite | What is held | What it buys | What it costs | Place read |
|---|---|---|---|---|---|
| Shift one sub-grid parameter | EAGLE (WeakFB, StrongFB: f_th × 0.5, 2; AGNdT8, AGNdT9); BAHAMAS (ΔT_heat ± 0.2 dex) | all other parameters | clean attribution to one process | the variant may no longer fit the calibration data; the shift has no observational meaning | arXiv:1501.01311, Table 1; [sec: arXiv:2306.05492, Sect. 6.4] |
| Shift the calibration data, refit all parameters | FLAMINGO: f_gas +2σ, −2σ, −4σ, −8σ; M_* −1σ (0.14 dex); M_* −1σ with f_gas −4σ | the other target (SMF kept fitted) | a variant labelled by observables, less dependent on the sub-grid model | needs the emulator; σ is a bootstrap error on a median, about five times smaller than the object-to-object scatter | arXiv:2306.05492, Sects. 6.2, 6.4 |
| Same data, other feedback implementation | FLAMINGO jets (fiducial data and f_gas −4σ), new 32-run hypercube; EAGLE's four GSMF-calibrated models | the calibration targets | tests what the targets do not pin down | one hypercube per implementation | arXiv:2306.05492, Sects. 2.3.1, 6.4; arXiv:1501.01311, Sect. 3.1 |
| Span amplitudes without calibration | CAMELS: A_SN1, A_AGN1 in [0.25, 4], A_SN2, A_AGN2 in [0.5, 2], with Ω_m, σ_8 | the functional form of the TNG or SIMBA model | marginalisation over feedback for learning | most points fit no data; 25 Mpc/h boxes | arXiv:2010.00619, Table 1, Sect. III.3.1 |

FLAMINGO shifts all gas-fraction points coherently by Nσ because it takes the
errors to be mostly systematic and correlated, and uses steps of 2σ rather than
1σ because the cluster-to-cluster scatter far exceeds the bootstrap error [src:
arXiv:2306.05492, Sect. 6.4]. Across the thermal variants ΔT_AGN moves only
from 10^7.71 (+2σ) to 10^8.40 K (−8σ), the gas fraction being mostly a function
of it [src: Table 8]. The CAMELS amplitudes multiply different things in the
two models (TNG: wind energy per unit SFR, wind speed, kinetic-mode energy,
burstiness; SIMBA: mass loading, wind speed, momentum flux, jet speed), so
equal values do not mean equal physics, and CAMELS-SIMBA drops SIMBA's cap of
wind energy at the supernova energy [src: arXiv:2010.00619, Table 1, Sect.
III.2].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Calibration boxes (high, intermediate, low resolution) | 100, 200, 400 cMpc, 2 × 360³ particles; m_g = 1.34 × 10^8, 1.07 × 10^9, 8.56 × 10^9 M_⊙ | FLAMINGO | arXiv:2306.05492 | Table 1 |
| Priors f_SN; Δv_SN [km/s]; log ΔT_AGN [K]; β_BH | high: [0.2, 0.9]; [80, 400]; [7.7, 8.9]; [0, 0.9]. intermediate: [0, 0.5]; [200, 800]; [7.5, 8.5]; [0.1, 0.9]. low: —; —; [7, 9.5]; [0, 3] | FLAMINGO | arXiv:2306.05492 | Table 2 |
| Best fit f_SN, Δv_SN, log ΔT_AGN, β_BH | high 0.524, 259, 8.07, 0.038; intermediate 0.238, 562, 7.95, 0.514; low —, —, 8.29, 0.373 | FLAMINGO | arXiv:2306.05492 | Table 2 |
| Emulator leave-one-out error, log SMF / f_gas(z = 0.1) / f_gas(z = 0.3) | high 2.7 / 8.9 / 7.9%; intermediate 2.2 / 7.5 / 6.7%; low 1.5 / 4.8 / 4.2%; jet 1.9 / 7.1 / 6.1% | FLAMINGO | arXiv:2306.05492 | Table 6 |
| Emulator against a rerun at the variant parameters | SMF about 1% (jet f_gas −4σ about 5%); f_gas within about 10%, most within 5% | FLAMINGO variants | arXiv:2306.05492 | Sect. 6.4 |
| Fitted mass ranges, intermediate resolution | SMF 10^9.92–10^11.50 M_⊙; f_gas 10^13.50–10^14.36 M_⊙ | FLAMINGO | arXiv:2306.05492 | Table 3 |
| Reduced χ² of the calibration fit | 1.15 (high), 1.23 (intermediate), 0.95 (low) | FLAMINGO | arXiv:2306.05492 | Sects. 6.2–6.3 |
| Fitted biases (ratio convention) | log₁₀ b_* = 0.026, b_cv = 0.995, b_HSE = 0.743 | FLAMINGO | arXiv:2306.05492 | Table 7 |
| Hydrostatic bias predicted by fiducial FLAMINGO (difference convention) | median −0.1 (groups) to −0.2 (clusters) in true mass, nearly flat in hydrostatic mass; minimum scatter about 0.1 at M_500c ~ 10^14 M_⊙ | FLAMINGO bias study | arXiv:2409.07849 | abstract |
| Refit with that mass-dependent bias | f_SN 0.228, Δv_SN 584 km/s, ΔT_AGN 10^7.85 K, β_BH 0.522, between fiducial and f_gas +2σ | FLAMINGO bias study | arXiv:2409.07849 | App. C, Table 1 |
| BAHAMAS against cosmo-OWLS AGN 8.0 | wind 300 vs 600 km/s; n_heat 20 vs 1; ΔT_heat 10^7.8 vs 10^8.0 K; ε_f = 0.15, mass loading 2 unchanged | BAHAMAS | arXiv:1603.02702 | Table 1 |
| EAGLE calibrated models | four, in 50 cMpc, 752³ per species; GSMF matched to < 0.31 dex | EAGLE | arXiv:1501.01311 | Table 1, Fig. 2 caption |
| EAGLE weak-convergence agreement | < 0.2 dex above 2 × 10^8 M_⊙ (100 star particles) | EAGLE | arXiv:1407.7040 | Sect. 5.1.2 |
| TNG calibration box | 25 Mpc/h, 512³ dark-matter particles and gas cells, about 1500 galaxies with ≥ 100 star particles, 9 haloes above 10^13 M_⊙ | IllustrisTNG | arXiv:1703.02970 | Sect. 3.1 |
| CAMELS amplitude ranges | A_SN1, A_AGN1 ∈ [0.25, 4]; A_SN2, A_AGN2 ∈ [0.5, 2]; Ω_m ∈ [0.1, 0.5]; σ_8 ∈ [0.6, 1.0]; 1000-run Latin hypercube per model | CAMELS | arXiv:2010.00619 | Table 1, Sect. III.3.1 |
| eROSITA group gas fraction | f_gas,500 = 4.32 ± 0.42% at M_500 = 2.54 × 10^13 M_⊙ (25 eRASS1 groups) | eROSITA × 2MRS | arXiv:2608.17735 | abstract |

## What goes wrong
<!-- key: what-goes-wrong -->

- **A calibrated quantity quoted as a prediction.** EAGLE warns that which
  observables are independent of the targets is "not always unambiguous" [src:
  arXiv:1407.7040, Sect. 2.1]; reproducing the GSMF does not guarantee
  realistic group and cluster baryon fractions, and at M_halo = 10^12 M_⊙ the
  circumgalactic gas fraction is about 0.2 in EAGLE but above 0.5 in
  IllustrisTNG, both calibrated on stellar masses [src: arXiv:2309.17075, Sect.
  5.4]. Test: list the targets and the quantities kept in view (Step 2 table)
  before calling an agreement a success.
- **A hydrostatic bias that is not the simulation's.** FLAMINGO calibrated with
  one constant bias, −0.257 in the difference convention; its own mock X-ray
  analysis gives a smaller bias at every hydrostatic mass, that bias depends on
  the feedback variant (median difference about 0.1 between f_gas −8σ and +2σ),
  and most of it comes from X-ray weighting rather than true departures from
  equilibrium above 10^13 M_⊙ [src: arXiv:2409.07849, App. C, Sects. 3.3–3.4].
  Refitting moves the model about halfway to the +2σ variant [src: App. C,
  Table 1]. Test: compare like with like, either by a synthetic X-ray pipeline
  as in BAHAMAS or by a bias fitted jointly with lensing masses.
- **Calibration data superseded.** The fiducial FLAMINGO gas fractions are
  pre-eROSITA, mostly without selection corrections; eROSITA fractions with
  lensing-calibrated masses are about two times lower, and kSZ profiles
  disagree with fiducial FLAMINGO at more than 8σ [src: arXiv:2509.10455,
  abstract and Sects. III, VI.1]. A second eROSITA analysis of 25 optically
  identified groups finds fiducial FLAMINGO and BAHAMAS closest and the
  strong-feedback variants in 2.5–8.0σ tension [src: arXiv:2608.17735,
  abstract]. The two eROSITA results disagree on which variant fits; a referee
  asks which data set calibrated the variant used.
- **Bootstrap errors used as the width of the variant grid.** The FLAMINGO σ is
  a bootstrap error on a median; the paper itself notes error bars about five
  times smaller than the scatter and that a 200 or 400 Mpc box never reaches
  the f_gas plateau above 10^15 M_⊙ [src: arXiv:2306.05492, Sect. 6.2]. The +2σ
  and −2σ variants are therefore not 95% bounds of anything physical.
- **Aperture mismatch at the massive end.** Apertures matter above about 10^11
  M_⊙ in EAGLE and FLAMINGO and above 10^10.7 M_⊙ in BAHAMAS; a
  Sérsic-plus-exponential fit adds up to 0.2 dex, which a 100 kpc aperture
  reproduces [src: arXiv:1407.7040, Sect. 5.1.1; arXiv:2306.05492, App. A;
  arXiv:1603.02702, App. B]. FLAMINGO fits the SMF only below 10^11.5 M_⊙,
  partly for this reason [src: arXiv:2306.05492, Sect. 3.1]. Test: state the
  aperture with every stellar mass.
- **A resolution change without recalibration or correction.** Using TNG300 or
  CAMELS galaxy properties at face value: TNG300 needs the rTNG300 correction
  [src: arXiv:1707.03406, Sect. 3.3]; CAMELS is at about TNG100-2 resolution,
  and its rescaling to TNG100 itself depends on the feedback parameters, so it
  is valid only near the fiducial point [src: arXiv:2211.16461, Sects. II.4,
  VI.5.1].
- **Stochastic noise in small calibration boxes.** Differences seeded by
  sub-grid randomness grow into significant differences even for well resolved
  galaxies; the review recommends several seeds when small volumes are used for
  calibration [src: arXiv:2309.17075, Sect. 2.5]. TNG cites the sample variance
  of its 25 Mpc/h box as a reason not to fit [src: arXiv:1703.02970, Sect.
  3.2].
- **Hidden implementation differences between calibration and production.**
  FLAMINGO reports a zero-metallicity star-formation bug in intermediate
  resolution, a black-hole repositioning change applied only at high and low
  resolution, which significantly strengthened the quenching of massive
  galaxies at high resolution, and jet calibration runs with jets along the box
  z-axis; the first and last are judged to have small effects [src:
  arXiv:2306.05492, Sects. 2, 2.2, 6.4]. Test: check the errata of the
  calibration paper before attributing a feature to physics.

Validation as the papers state it: equal-quality fits (reduced χ²) at each
resolution and a rerun at the best-fit parameters reproducing the emulator
within its error [src: arXiv:2306.05492, Sects. 6.2–6.4]; weak and strong
convergence tests in a smaller box at two resolutions sharing the large modes
[src: arXiv:1407.7040, Sect. 5.1.2; arXiv:1603.02702, App. C].

## Reading list
<!-- key: reading-list -->

- Foundation: Schaye et al. 2015, arXiv:1407.7040, Sects. 2.1–2.2 — why
  feedback must be calibrated; strong versus weak convergence.
- Method: Kugel et al. 2023, arXiv:2306.05492 — emulator calibration with bias
  parameters, priors from numerics, data-shift variants.
- Method: Crain et al. 2015, arXiv:1501.01311, Sect. 3 — choosing targets; four
  calibrated stellar-feedback models; one-parameter variations.
- Application: McCarthy et al. 2017, arXiv:1603.02702, Sect. 2 and App. A, C —
  calibrating on halo baryon content by hand; fixed-scale convergence.
- Application: Pillepich et al. 2018, arXiv:1703.02970, Sect. 3.2 and App. A —
  the case for hand tuning and strong convergence.
- Application: Pillepich et al. 2017, arXiv:1707.03406, Sect. 3.3 — the rTNG300
  resolution correction.
- Application: Davé et al. 2019, arXiv:1901.10203, Sects. 2.1, 3.7 — what SIMBA
  tuned and what it left as prediction.
- Method: Villaescusa-Navarro et al. 2021, arXiv:2010.00619, Table 1 — feedback
  amplitudes as a parameter space.
- Method: Jo et al. 2022, arXiv:2211.16461 — likelihood-free calibration on
  CAMELS and its resolution caveat.
- Critique: Braspenning et al. 2024, arXiv:2409.07849, App. C — the hydrostatic
  bias assumed in calibration against the simulated one.
- Critique: Siegel et al. 2025, arXiv:2509.10455, Sect. VI.1, and Khalil et al.
  2026, arXiv:2608.17735 — eROSITA gas fractions against the calibration data,
  with opposite verdicts on the variants.
- Review: Crain & van de Voort 2023, arXiv:2309.17075, Sects. 2.4–2.5.

## Not verified
<!-- key: not-verified -->

- MillenniumTNG, Horizon-AGN and Magneticum calibration choices: not read. The
  review states Horizon-AGN's stellar feedback was not calibrated but taken
  from Starburst99 and its AGN feedback set by the M_BH–M_* relation [sec:
  arXiv:2309.17075, Sect. 2.4].
- The BAHAMAS strong and weak AGN variants (ΔT_heat ± 0.2 dex) are quoted from
  the FLAMINGO papers; McCarthy et al. 2018 was not read.
- The later CAMELS extensions to 28 parameters (seen in a search by title only)
  and to 35 parameters (arXiv:2606.10038, in L2): how their parameter ranges
  were chosen was not read.
- The functional form of the rTNG300 correction (Eq. 3 and App. A of
  arXiv:1707.03406) and the stellar-mass rescaling of Jo et al. (their App. A):
  not read.
- The detailed eROSITA selection treatment in arXiv:2608.17735 and why its
  verdict differs from arXiv:2509.10455: only its abstract was read.
- Ludlow-type tests of spurious collisional heating as a limit on convergence:
  not researched.
