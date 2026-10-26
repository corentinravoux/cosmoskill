# Stochastic background and the pulsar-timing signal — cosmo-early-universe-exotica dossier

Scope: how a PTA background result is produced (per-pulsar timing and noise
model, Fourier-basis Gaussian-process likelihood, common-process models, the
Bayes factor and optimal statistic for Hellings–Downs correlations, null
distributions and their p-values), how the arrays' noise and frequency choices
differ and what each costs, and how the LVK cross-correlation limit is built.
Snapshot: 2026-10-22.
From: LISA Cosmology WG 2022 review (arXiv:2204.05434), Sects. 5.1 to 5.3; NANOGrav,
EPTA/InPTA, PPTA, CPTA, MPTA and IPTA data releases; LVK stochastic-background
searches.

Already in L2, not repeated here: amplitudes, free-γ fits and HD significances
of every array (`results.md#pulsar-timing-background-amplitude-spectrum`); LVK
limits (`results.md#ground-based-stochastic-background-limits`); systematics
(`systematics.md#pulsar-timing-noise-and-the-hellings-downs`); HD, CURN, γ
conventions (`physics-and-methods.md#the-pta-signature-and-its-statistics`);
origin debate (`open-questions.md#astrophysical-or-cosmological-origin-of-the-pta`).

## How it is done
<!-- key: how-it-is-done -->

The notation follows NANOGrav 15 yr (Agazie et al. 2023, arXiv:2306.16213,
Sect. II "The 15-year Data Set and Data Model"), whose paper sets out the most complete pipeline; the other arrays' choices are
given step by step beside it.
δt is the vector of timing residuals of one pulsar; a, b index pulsars; i, j
index Fourier frequencies f_i = i/T, with T the span from first to last
time of arrival (TOA).

### Step 1. Fit the timing model of each pulsar
<!-- key: step-1-fit-the-timing-model-of-each-pulsar -->

Each pulsar's TOAs are fitted with spin period, period derivative, sky
position, proper motion and parallax, plus five Keplerian orbital elements for
binaries and post-Keplerian terms kept when an F test favours them [src:
arXiv:2306.16213, Sect. II]. Parallax and proper motion are fitted even where
not measurable, because they produce delays at the same frequencies in every
pulsar (0.5 yr⁻¹ and 1 yr⁻¹) and could otherwise be read as a GW signal; the
cost in GWB sensitivity is minimal because those frequencies lie above the
band where the background matters [src: same]. NANOGrav adopts TT(BIPM2019)
and the JPL DE440 ephemeris, whose improved Jupiter orbit makes the ephemeris
uncertainty that affected the 11 yr search negligible [src: same]. Only the 67
pulsars with baseline ≥ 3 yr enter the background search [src: same].

Other arrays:

- **CPTA DR1** (Xu et al. 2023, arXiv:2306.16216): 57 MSPs timed with FAST
  between April 2019 and September 2022, mostly at two-week cadence, at
  1.0–1.5 GHz with the central beam of the 19-beam receiver; timing models
  in TEMPO2; J1713+0747 data after MJD 59319 dropped because of its profile
  event [src: Sect. 2].
- **MPTA** (Miles et al. 2025, arXiv:2412.01153): 83 pulsars over 4.5 yr,
  about 250,000 TOAs with a median error of 3 μs [src: abstract].
- **InPTA DR2** (Tahbildar et al. 2026, arXiv:2608.02808): 27 MSPs observed
  simultaneously in two bands with the upgraded GMRT, baseline up to 7.2 yr
  [src: abstract].
- **Five-array combination** (Yu et al. 2025, arXiv:2512.08666): public
  EPTA DR2 (10 yr), InPTA DR1, MPTA 4.5 yr, NANOGrav 15 yr and PPTA DR3, 121
  pulsars and 1,090,206 TOAs [src: main text]. A "direct combination" gives
  each pulsar one nominal timing model (one time coordinate, TDB, and one
  sky-position convention), computes one design matrix there and
  marginalises over the offsets, which avoids reconciling the arrays'
  models into a single best one; residuals come from PINT for NANOGrav TOAs
  and Tempo2 for the others [src: main text; SM Sect. A.1].

### Step 2. Model white noise
<!-- key: step-2-model-white-noise -->

White noise has three parameters per receiver/backend system: EFAC (a linear
scaling of TOA uncertainties), EQUAD (added in quadrature) and ECORR (noise
common to all sub-bands of one epoch) [src: arXiv:2306.16213, Sect. II]. They
are fitted in single-pulsar analyses and then held at their maximum a
posteriori values, summarised by a covariance C, in the array search [src:
Sect. II; Table 1 "single-pulsar analysis only"]. EPTA also fixes EFAC and
EQUAD from single-pulsar runs, and drops ECORR because with at most four
sub-band TOAs per observation no time-correlated white noise is measurable
[src: arXiv:2306.16214, Sect. 2]. CPTA instead marginalises all white- and
red-noise parameters (EFAC, EQUAD, ECORR, red and DM noise) in the
background fit, "without fixing any of them" [src: arXiv:2306.16216,
Sect. 3]. In the five-array set, NANOGrav, PPTA, MPTA and seven EPTA
backends use all three white-noise parameters; InPTA and the other EPTA
backends use EFAC and EQUAD only [src: arXiv:2512.08666, main text].

### Step 3. Write the Gaussian-process likelihood
<!-- key: step-3-write-the-gaussian-process-likelihood -->

Residuals are a finite Gaussian process: r = δt − F c − M ε (Eq. 2), with F
the Fourier design matrix (sines and cosines at f_i), c its amplitudes, M the
timing-model design matrix and ε its coefficients, and single-pulsar log
likelihood ln p = −½ [rᵀ C⁻¹ r + ln det(2πC)] (Eq. 1) [src:
arXiv:2306.16213, Sect. II]. ε has a flat prior of infinite extent; the c of
all pulsars share a zero-mean normal prior with covariance
⟨c_ai c_bj⟩ = δ_ij (δ_ab φ_ai + Φ_ab,i) (Eq. 3), where φ_ai is the intrinsic
red noise of pulsar a and Φ_ab,i the common process. c and ε are marginalised
analytically and only the hyperparameters η are sampled [src: same].

Intrinsic red noise is a power law,
φ_ai = A_a²/(12π²) (1/T) (f_i/f_ref)^(−γ_a) f_ref⁻³ (Eq. 6), with log-uniform
A_a and uniform γ_a [src: Sect. II]. The common spectra Φ_CURN,i and Φ_HD,i
have the same form with (A_CURN, γ_CURN) or (A_HD, γ_HD) (Eqs. 7–8); "free
spectrum" models give each Φ_i its own parameter [src: same]. MPTA writes the
same likelihood and power law, f_c = 1 yr⁻¹ [src: arXiv:2412.01153, Sect.
2.1]. CPTA uses the same frequency-domain method but parametrises the
characteristic strain, A(f) = A_c (f/1 yr⁻¹)^α with α = −2/3 for SMBHBs
(γ = 3 − 2α), and S(f) = A(f)²/(12π² f³) [src: arXiv:2306.16216, Sect. 3,
Eqs. 1–2; der: γ from S ∝ f^(2α−3)].

### Step 4. Define the models compared
<!-- key: step-4-define-the-models-compared -->

| Model | Φ_ab,i | Meaning |
|---|---|---|
| IRN | 0 | intrinsic red noise only |
| CURN | δ_ab Φ_CURN,i | common spectrum, no inter-pulsar correlation |
| HD | Γ(ξ_ab) Φ_HD,i | isotropic GWB |

Source: arXiv:2306.16213, Sect. II [src]. The Hellings–Downs function is
Γ(ξ) = (3/2) x ln x − x/4 + 1/2 + δ_ab/2 with x = (1 − cos ξ)/2 (Eqs. 4–5),
ξ_ab being the angle between pulsars a and b. Monopole and dipole patterns
are fitted as alternatives (Sect. V.3). "HD13/3" fixes γ_HD = 13/3; "HDγ"
frees it.

### Step 5. Choose the frequency bins
<!-- key: step-5-choose-the-frequency-bins -->

NANOGrav uses i = 1–30 (2–59 nHz) for intrinsic noise, a range over which
pulsar noise passes from red- to white-dominated, and i = 1–14 (2–28 nHz) for
the common process, chosen as the MAP break frequency of a broken power-law
CURN fit, to limit correlation with excess white noise at higher frequencies
[src: arXiv:2306.16213, Sect. II]. EPTA uses the lowest 24 bins for DR2full
(24.7 yr) and 9 for DR2new (10.3 yr), set by the same broken-power-law method
and a free-spectrum check, and verified to be insensitive to adding bins [src:
arXiv:2306.16214, Sect. 4.1]. Across arrays the IPTA comparison lists 9, 14
and 28 GWB frequencies (EPTA, NANOGrav, PPTA), about 3–28, 2–30 and 1.7–47 nHz
[src: arXiv:2309.00693, Sect. III.1]. MPTA's free spectrum constrains only the
three lowest independent frequencies, so its frequentist analyses use 1/T to
3/T, 7.1–28.4 nHz [src: arXiv:2412.01153, Sect. 2.1]. CPTA, with T = 3.40
yr, does not fit a spectrum for the correlation search: it measures
correlations at single frequencies, mainly f = 1.5/T = 14.0 nHz, with 1/T
(9.34 nHz) and 2/T (18.7 nHz) as checks; fitting spin period and its
derivative suppresses the 1/T component, and the power-law signal is weaker
at 2/T [src: arXiv:2306.16216, Sect. 4, App. B].

### Step 6. Sample and compute Bayes factors
<!-- key: step-6-sample-and-compute-bayes-factors -->

Priors (NANOGrav, Table 1 of arXiv:2306.16213) [src: App. B]: EFAC uniform
[0, 10]; log₁₀ EQUAD and log₁₀ ECORR uniform [−8.5, −5] (s); log₁₀ A_red
uniform [−20, −11]; γ_red uniform [0, 7]; common amplitude log₁₀ A uniform
[−18, −14] at γ = 13/3 and [−18, −11] with γ free; γ uniform [0, 7]; free
spectrum log₁₀ ρ_i uniform [−18, −8] (s²). Convergence requires Gelman–Rubin
R̂ < 1.01 for all parameters (PTMCMC sampler) [src: App. B]. CPTA samples with
parallel tempering at ten temperatures, log A_c uniform in [−18, −13] and α
in [−1.8, 1.5]; the lower α edge follows from requiring a finite RMS after
the spin fit (α > −2), moved up to avoid numerical singularities [src:
arXiv:2306.16216, Sect. 3].

Model comparison uses four tools [src: arXiv:2306.16213, App. B]:

- **Thermodynamic integration**: ln p(d|H) = ∫₀¹ ⟨ln p(d|θ)⟩_β dβ over
  parallel-tempered chains (Eq. B1).
- **Savage–Dickey ratio** for nested models (a parameter frozen at zero).
- **Product-space sampling** for disjoint models such as HD against CURN: a
  model-index parameter switches the likelihood, and the Bayes factor is the
  ratio of the time spent in each model. EPTA uses the same method [src:
  arXiv:2306.16214, Sect. 3.1].
- **Reweighting**: sample the cheap CURN posterior and reweight to HD; the
  mean weight is the HD/CURN Bayes factor.

Bayes-factor errors come from bootstrap resampling of the chains [src:
arXiv:2306.16213, App. B]. MPTA uses Savage–Dickey [src: arXiv:2412.01153,
Sect. 2.1]. On the five-array set, ln BF(HD/CURN) = 10.18 ± 0.13, i.e.
BF = 26,000 ± 3,000, which the authors put at "two orders-of-magnitude
larger" than NANOGrav's ≈ 200 and at ≈ 4.5σ by √(2 ln BF) [src:
arXiv:2512.08666, main text].

### Step 7. Compute the optimal statistic
<!-- key: step-7-compute-the-optimal-statistic -->

For each pair, ρ_ab = δt_aᵀ P_a⁻¹ Φ̃_ab P_b⁻¹ δt_b / Tr(P_a⁻¹ Φ̃_ab P_b⁻¹ Φ̃_ba)
(Eq. 9), where P_a = ⟨δt_a δt_aᵀ⟩ is the total auto-covariance and Φ̃_ab the
cross-covariance normalised so that Φ_ab = A² Γ(ξ_ab) Φ̃_ab [src:
arXiv:2306.16213, Sect. IV]. ρ_ab has mean A²Γ(ξ_ab) and variance σ_ab² ≈
(Tr …)⁻¹, too large for one pair to be useful. The estimator is the weighted
template fit Â² = Σ ρ_ab Γ_ab/σ_ab² / Σ Γ_ab²/σ_ab² (Eq. 10), and
S/N = Σ ρ_ab Γ_ab/σ_ab² / [Σ Γ_ab²/σ_ab²]^½ (Eq. 11) [src: same]. Because P_a
depends on noise hyperparameters, the statistic is evaluated at the MAP or,
better, averaged over the CURN posterior ("noise-marginalised", Vigeland et
al. 2018, arXiv:1805.12188), which gives more accurate amplitudes [src: same].
The distribution of Â² is only approximately normal, so this S/N is not a
σ level [src: same]. NANOGrav finds S/N = 5 ± 1 (CURNγ noise) and 4 ± 1
(CURN13/3), with 14 frequencies and very weak dependence on that number [src:
Sect. IV].

Peers:

- **CPTA: a correlation-coefficient statistic.** All residuals are fitted
  with the timing models and a common sinusoid at f; the per-pulsar phases
  φ_i give c_ij = cos(φ_i − φ_j), and the significance against constant
  correlation is the Jenet et al. 2005 statistic 𝒮 (Eq. 6), a normalised
  correlation between c_ij and the HD values with a Gaussian null for many
  pulsars (Eq. 8) [src: arXiv:2306.16216, Sect. 4]. Uses cross-correlations
  only, so it is "immune" to a common uncorrelated signal and removes a
  clock monopole; bounding c_ij in [−1, 1] makes it not optimal but less
  sensitive to a few dominant pulsars [src: same]. It gives no amplitude, so
  MPTA states CPTA cannot be compared with it directly [src:
  arXiv:2412.01153, Sect. 4.3].
- **MPTA**: noise-marginalised OS on three frequencies, the Savage–Dickey
  BF, and the PPTA pseudo-Bayesian pairwise analysis between the two [src:
  arXiv:2412.01153, Sect. 2.1]. PPTA did not use an OS in its latest search
  and quotes the pairwise amplitude [src: same, Sect. 4.3].
- **Five-array set**: OS, a Neyman–Pearson statistic (NP) and a robust NP
  (NPMV), with noise-marginalised p-values; none reaches 5σ; the OS gives
  ≈ 4.3σ against the ≈ 3.2σ the authors attribute to NANOGrav [src:
  arXiv:2512.08666, Table 3 and text].

### Step 8. Build the null distribution
<!-- key: step-8-build-the-null-distribution -->

Two proxies keep each pulsar's noise and destroy the HD signature [src:
arXiv:2306.16213, Sect. III, App. F; arXiv:2306.16214, Sect. 4.3]:

- **Phase shifts** (Taylor et al. 2017, as cited): random phases in [0, 2π]
  added to the common-process Fourier components. Tests "no inter-pulsar
  correlations".
- **Sky scrambles** (Cornish & Sampson 2016, as cited): pulsars given random
  sky positions. Tests "correlations present but independent of angle".
  Scrambled overlap reduction functions must be nearly orthogonal to the true
  one and to each other, by the match M̄ = Σ Γ_ab Γ′_ab / √(Σ Γ² Σ Γ′²)
  (Eq. F1); NANOGrav uses M̄ < 0.1 against the true ORF and < 0.17 between
  scrambles [src: arXiv:2306.16213, App. F].

Model-based alternatives are simulations of CURN data and the analytic
generalised χ² distribution of Hazboun et al. 2023 (as cited) [src:
arXiv:2306.16213, Sect. IV]. CPTA applies both proxies to 𝒮: phase shifts
reproduce the Gaussian null because 𝒮 does not depend on amplitude; sky
scrambles (3,000 realisations at M = 0.1, 0.3, 0.5; 100,000 at M = 1, no
significant dependence on M) leave a tail for 𝒮 ≥ 2 and overestimate the
p-value, since a scrambled sky still carries a shuffled HD correlation
[src: arXiv:2306.16216, App. C]. The authors add that a statistic that
involves the amplitude (OS, likelihood ratio, Bayes factor) can lead to
different conclusions [src: same].

### Step 9. Cross-checks
<!-- key: step-9-cross-checks -->

- Spline reconstruction of Γ(ξ) with seven knots (0°, 25°, 49.2°, 82.5°,
  121.8°, 150°, 180°), placed at the HD end points, zero crossings and
  minimum [src: arXiv:2306.16213, Sect. III].
- Binned ρ_ab (15 bins of equal pair number) with χ² = 8.1 against HD,
  p = 0.75 from HD simulations; error bars include the ⟨ρ_ab ρ_cd⟩ covariance
  induced by the signal, without which spreads are 20–40% smaller [src:
  arXiv:2306.16213, Sect. IV].
- Dropout factors per pulsar; leave-one-out posterior predictive likelihood
  (Eq. 13) giving a pseudo Bayes factor of 1400 for HD13/3 over CURN13/3;
  S/N growth with time slices and pulsar number; Arecibo-only and GBT-only
  data sets [src: arXiv:2306.16213, Sect. V.4].
- Alternative DM model (Sect. V.1); ephemeris model BayesEphem (EPTA, Sect. 4.4.2).

### LVK: the cross-correlation route
<!-- key: lvk-the-cross-correlation-route -->

For detectors I, J the statistic is Ĉ^IJ(f) = (2/T) Re[s̃_I* s̃_J]/(γ_IJ S₀)
(arXiv:2101.12130, Eq. 2), with γ_IJ the normalised overlap reduction
function, S₀ = 3H₀²/(10π²f³), and ⟨Ĉ⟩ = Ω_GW(f); its variance is σ_IJ² ≈
P_I P_J /(2TΔf γ_IJ² S₀²) (Eq. 3) [src: Sect. II.1]. Ω_GW is computed with
H₀ = 67.9 km s⁻¹ Mpc⁻¹ (Planck 2015) [src: Sect. II]. Frequencies are combined
with weights w(f) = Ω_GW(f)/Ω_GW(f_ref), f_ref = 25 Hz (Eqs. 4–5), baselines
and earlier runs by inverse variance (Eq. 7), and parameters estimated with a
Gaussian likelihood in Ĉ_k (Sect. II.3) [src]. Only cross-correlations are
used, because detector noise spectra are not known well enough to subtract
from auto-correlations [src: Sect. II.2]. Correlations between baselines enter
at O(Ω²) and are neglected [src: Sect. II.3].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Dispersion-measure model: DMX or Gaussian process
<!-- key: dispersion-measure-model-dmx-or-gaussian-process -->

- **DMX** (NANOGrav baseline): a piecewise-constant DM per group of
  observations, about every 6 days, inside the timing model [src:
  arXiv:2309.00693, Sect. III.1]. Kept as standard so results compare
  directly with the 12.5 yr analysis [src: arXiv:2306.16213, Sect. V.1].
  Cost: a broadband loss of GW sensitivity at low and high frequencies [src:
  Mingarelli et al. 2026 review, arXiv:2603.13643, Sect. 9].
- **DMGP** (EPTA, PPTA): a power-law Gaussian process with ν⁻² basis, up to
  i = 100, plus a deterministic solar-wind model; smaller prior volume and
  more precise DM series, at higher computing cost and with the need to model
  the time covariance correctly [src: arXiv:2306.16213, Sect. V.1;
  arXiv:2603.13643, Sect. 9].
- **Same data, both models**: in NANOGrav only two pulsars (J1713+0747,
  J1600−3053) change noticeably; DMGP shifts γ_CURN upwards, closer to 13/3,
  while the HD significance is unchanged [src: arXiv:2306.16213, Sect. V.1,
  Fig. 5]. The fitted γ is therefore partly a noise-model output.
- **Combined data**: the five-array analysis adopts DMGP for every pulsar,
  on the argument that red and DM noise are intrinsic to the pulsar and the
  interstellar medium and must be the same across arrays; it notes that
  NANOGrav and InPTA use DMX [src: arXiv:2512.08666, main text].

### Per-pulsar noise: fixed recipe or model selection
<!-- key: per-pulsar-noise-fixed-recipe-or-model-selection -->

NANOGrav gives every pulsar red noise with 30 frequencies [src:
arXiv:2309.00693, Sect. III.1]. EPTA selects for each pulsar among red noise,
DM and scattering (chromatic indices 0, 2, 4) and the number of Fourier
components by Bayes factor, from 10 up to nearly 150 frequencies, dropping red
noise where none is detected [src: arXiv:2306.16214, Sect. 2;
arXiv:2309.00693, Sect. III.1]. PPTA caps red noise at 1/(240 d), adds a
high-frequency achromatic term up to 1/(30 d) for some pulsars, scattering
(ν⁻⁴) for seven, band noise below 960 MHz and system noise for five [src:
arXiv:2309.00693, Sect. III.1]. Customised models were one of the two
corrections that, with hierarchical priors, turned the pre-2020 upper limits
into detections at A ~ 2–3 × 10⁻¹⁵, according to the 2026 review [src:
arXiv:2603.13643, Sect. 3]. In a standardised re-analysis the arrays'
CURN amplitudes agree, but some long-baseline pulsars (J1744−1134,
J1600−3053, J1857+0943) still get dropout factors that disagree between
arrays [src: arXiv:2309.00693, Sect. IV.3].

CPTA compares all 16 combinations of EQUAD, ECORR, red and DM noise (each on
or off) per pulsar and keeps the one of highest evidence, with four
independent noise pipelines (TEMPONEST, ENTERPRISE, FORTYTWO, 42++) giving
consistent results [src: arXiv:2306.16216, Sect. 2]. MPTA runs three
models: DATA (390 free parameters, the noise processes selected per pulsar),
ER (532, extra achromatic red noise wherever DATA lacks it, against
sub-threshold misspecification) and ALT (530, ER without the steep red
process of J2129−5721, constrained only in its lowest bin with γ > 10 and
degenerate with the common signal) [src: arXiv:2412.01153, Sect. 2.3,
Table 1]. Depending on these choices the HD correlations are 3–3.4σ or
insignificant, which the authors relate to many of the most precise MPTA
pulsars being close together on the sky and dominating the statistics [src:
abstract]. The OS amplitude is sensitive to the noise model, while the
Bayesian HD assessments are not [src: Sect. 4.3].

### Red-noise priors
<!-- key: red-noise-priors -->

The 2026 review summarises two results it cites (Hazboun et al. 2020;
Goncharov et al. 2022): uniform priors on red-noise amplitude let per-pulsar
noise absorb common power, biasing GWB limits low, and fitting pulsars one at
a time before the common search lets power leak in either direction [src:
arXiv:2603.13643, Sect. 3]. PPTA states that over-broad priors create
spurious support for CURN; it restricts each pulsar's prior to the central
99.7% single-pulsar interval widened by −2/+1 in log₁₀ A and ±0.5 in γ, and
lifts the common-amplitude floor from −20 to −18 because the data are
insensitive below log₁₀ A ≈ −16.5 [src: arXiv:2306.16215, Sect. II.1.1].
The Savage–Dickey Bayes factor for the common process then drops from
log₁₀ B = 6.8 to 4.8 while the amplitude, log₁₀ A = −14.69 ± 0.05, does not
move [src: Sect. III.1].

### Bayes factor or optimal statistic
<!-- key: bayes-factor-or-optimal-statistic -->

The Bayes factor uses the full likelihood but each phase-shifted realisation
costs a full run: NANOGrav computed 5,000 Bayesian phase shifts against
400,000 for the optimal statistic [src: arXiv:2306.16213, Fig. 3 caption].
The optimal statistic is fast and frequentist but needs the noise posterior
from a Bayesian CURN run [src: arXiv:2306.16214, Sect. 3.2]. Same data,
NANOGrav: p = 10⁻³ (BF, phase shifts) and p = 1.6 × 10⁻³ (BF, sky
scrambles) against p = 5 × 10⁻⁵ (OS, phase shifts), 1.8 × 10⁻⁴ (OS,
simulations), 1.9 × 10⁻⁴ (OS, generalised χ²) and < 10⁻⁴ (OS, sky
scrambles) [src: Sects. III–IV, App. F]. The BF also depends on how many
bins enter Φ: 200 with 14 frequencies, 1000 with 5 [src: Sect. III]. CPTA
warns that its BF(HD/dipole) = 66 is not decisive: the Bayesian comparison
includes autocorrelation terms that its frequentist 𝒮 omits, and simulations
(Zic et al. 2022) and its toy model (App. A) show the limits of Bayes factors
here; with 𝒮 alone, dipole (4.1) and HD (4.6) cannot be told apart [src:
arXiv:2306.16216, Sect. 4].

### Phase shifts or sky scrambles
<!-- key: phase-shifts-or-sky-scrambles -->

On EPTA DR2new the OS p-value is 0.002 with phase shifts and 0.008 with all
sky scrambles (simulated target data); simulations give 0.006 and the
generalised χ² 0.003 at S/N = 3.5; EPTA adopts p ≈ 0.004 [src:
arXiv:2306.16214, Sect. 4.3]. Sky scrambles and phase shifts disagree in the
high-S/N tail for DR2new and agree in the low-S/N regime (DR2full) [src:
same]. Tighter match thresholds reduce the number of scrambles (NANOGrav:
6,043 at M̄ < 0.1, 1,534 at M̄ < 0.08, against 10,000 at 0.17) without
changing the null distribution noticeably [src: arXiv:2306.16213, App. F].
Di Marco et al. 2023 find that sky scrambles saturate after O(10)
quasi-independent realisations (|M| < 0.1) and phase shifts after O(100),
so the ≳ 5σ tail of the null cannot be estimated reliably this way [src:
arXiv:2305.04464].

### Full or recent data
<!-- key: full-or-recent-data -->

EPTA analyses its 24.7 yr set and the 10.3 yr set from wide-band backends
only. Phase-shift p-values of the HD/CURN Bayes factor are 0.04 (BF 4) and
0.0005 (BF 60) [src: arXiv:2306.16214, Sect. 4.3]; Sect. 6 of the same
paper quotes 0.001 for DR2new. Ignoring the lowest bin of DR2full brings the
two free spectra into agreement; with γ fixed at 13/3 both give log₁₀ A ≈
−14.61 [src: Sect. 6]. The 10.3 yr span is close to Jupiter's ~12 yr orbit,
so adding BayesEphem lowers the DR2new HD Bayes factor from about 60 to 17
[src: Sect. 4.4.2].

InPTA DR2 (7.2 yr at most) finds a broad CURN posterior, a Savage–Dickey
BF of 2.5 and OS S/N consistent with zero for monopole, dipole and HD, and
needs at least a 10 yr baseline in simulations to start recovering the
common signal [src: arXiv:2608.02808, abstract]. MPTA notes that PPTA's
amplitude grows across its time slices, which could affect short data sets
such as its own [src: arXiv:2412.01153, Sect. 4.3].

Amplitudes as MPTA lists them, its own at γ = 13/3 [src: arXiv:2412.01153,
Sect. 4.3]: MPTA log₁₀ A = −14.32 (+0.07/−0.08) (OS) or −14.39 ± 0.11 (Bayesian,
γ window 0.1); EPTA+InPTA −14.48 (+0.08/−0.11) (OS, recent 9 yr, largest of
its versions, fixed index); NANOGrav −14.62 (+0.11/−0.12) (Bayesian; no OS amplitude
reported); PPTA −14.69 ± 0.05 (pairwise). MPTA is "larger in amplitude than
all values reported by other PTAs", overlaps EPTA+InPTA, is 2.5σ from PPTA,
and 1.2σ from PPTA's latest 6 yr slice, −14.57 (+0.11/−0.13).

### Reference frequency
<!-- key: reference-frequency -->

The strong A–γ correlation at f_ref = 1 yr⁻¹ is a parametrisation artefact
that largely disappears at f_ref = (10 yr)⁻¹ [src: arXiv:2306.16213, Sect.
III]; amplitudes at different γ compare only at a common f_ref.

### LVK: amplitude prior and data cuts
<!-- key: lvk-amplitude-prior-and-data-cuts -->

LVK reports log-uniform amplitude priors as headline (natural for a scale
parameter, more sensitive to small signals), with a lower bound Ω_ref ≥ 10⁻¹³
on which the limit depends mildly, and gives the more conservative uniform-prior
limits as well [src: arXiv:2101.12130, Sect. IV.1]. In O3, glitch gating
zeroed 0.4% (Hanford) and 1% (Livingston) of the data; without it the
non-stationarity cut (σ varying by > 20% between segments) would have
removed more than half of the 192 s segments [src: Sects. III.2–III.3].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Pulsars, span | 67 (≥ 3 yr), T = 16.03 yr | NANOGrav 15 yr | arXiv:2306.16213 | Sect. II |
| Red-noise bins | i = 1–30 (2–59 nHz) | NANOGrav | arXiv:2306.16213 | Sect. II |
| Common-process bins | 14 (2–28 nHz); EPTA 24/9; PPTA 28 | NANOGrav, EPTA, PPTA | arXiv:2306.16213; arXiv:2306.16214; arXiv:2309.00693 | Sect. II; Sect. 4.1; Sect. III.1 |
| Common amplitude prior | log₁₀ A ∈ [−18, −14] (γ = 13/3), [−18, −11] (free) | NANOGrav | arXiv:2306.16213 | Table 1 |
| Red-noise priors | log₁₀ A ∈ [−20, −11], γ ∈ [0, 7] | NANOGrav | arXiv:2306.16213 | Table 1 |
| Convergence | R̂ < 1.01 | NANOGrav | arXiv:2306.16213 | App. B |
| BF(HD/CURN) | 200 (14 bins) – 1000 (5 bins) | NANOGrav | arXiv:2306.16213 | Sect. III |
| Phase shifts | 5,000 (BF), 400,000 (OS) | NANOGrav | arXiv:2306.16213 | Fig. 3 |
| OS S/N | 5 ± 1 (CURNγ), 4 ± 1 (CURN13/3) | NANOGrav | arXiv:2306.16213 | Sect. IV |
| Sky-scramble match | M̄ < 0.1 (vs true), < 0.17 (mutual); 10,000 generated, 5,000 used | NANOGrav | arXiv:2306.16213 | App. F |
| Pseudo Bayes factor | 1400 (HD13/3 vs CURN13/3), ~3σ from 40 simulations | NANOGrav | arXiv:2306.16213 | Sect. V.4 |
| Split telescopes | OS S/N 2.9 (Arecibo), 3.3 (GBT) | NANOGrav | arXiv:2306.16213 | Sect. V.4 |
| EPTA OS p-value | ≈ 0.004 (DR2new) | EPTA | arXiv:2306.16214 | Sect. 4.3 |
| BayesEphem effect | BF 60 → 17 (DR2new) | EPTA | arXiv:2306.16214 | Sect. 4.4.2 |
| PPTA early-data limit | A < 1.2 × 10⁻¹⁵ (95%, first 9 yr) against 2.0 ± 0.2 × 10⁻¹⁵ full | PPTA DR3 | arXiv:2306.16215 | Sect. III.4 |
| Null saturation | O(10) sky scrambles, O(100) phase shifts | simulations | arXiv:2305.04464 | abstract |
| CPTA DR1 | 57 MSPs, T = 3.40 yr; log A_c = −14.4 (+1.0/−2.8) free α, −14.7 (+0.9/−1.9) at α = −2/3 (95%) | CPTA | arXiv:2306.16216 | Sects. 2–3 |
| CPTA HD statistic | 𝒮 = 4.6 at 1.5/T (p = 4 × 10⁻⁶); 2.4, 2.3 at 1/T, 2/T; dipole 4.1; BF(HD/dipole) = 66 | CPTA | arXiv:2306.16216 | Sect. 4 |
| MPTA OS amplitude | log₁₀ A = −14.12 (+0.04/−0.05) (fixed-parameter common signal; abstract: α = −0.26), −14.32 (+0.07/−0.08) (13/3) | MPTA DATA model | arXiv:2412.01153 | Sect. 4.3; abstract |
| MPTA HD significance | 3–3.4σ or insignificant, by noise model | MPTA | arXiv:2412.01153 | abstract |
| InPTA DR2 | 27 MSPs, ≤ 7.2 yr; A_GWB < 3.4 × 10⁻¹⁴ (95%, γ = 13/3); BF(CURN) 2.5 | InPTA | arXiv:2608.02808 | abstract |
| Five-array set | 121 pulsars, 1,090,206 TOAs; BF(HD/CURN) = 26,000 ± 3,000; OS ≈ 4.3σ | EPTA, InPTA, MPTA, NANOGrav, PPTA | arXiv:2512.08666 | main text, Table 3 |
| LVK O3 livetime lost | 17.9% (HL), 22.1% (HV), 21.9% (LV) | O3 isotropic | arXiv:2101.12130 | Sect. III.2 |
| LVK band removed | 13.3% (HL), 21.5% (HV), 18.9% (LV); below 300 Hz 3.2, 9.3, 5.9% | O3 isotropic | arXiv:2101.12130 | Sect. III.2 |
| LVK spectrum fit | χ²/dof = 0.98 after cuts | O3 isotropic | arXiv:2101.12130 | Sect. IV.1 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Spurious common process.** Simulated arrays with no common signal give
  CURN Bayes factors above 10⁵ under a wide range of noise prescriptions,
  depending strongly on the red-noise priors; a CURN detection is "not a
  reliable precursor" to a GWB detection [src: Zic et al. 2022,
  arXiv:2207.12237]. Test: rest the claim on HD correlations, and check that
  the CURN Bayes factor is stable under prior changes, as PPTA did [src:
  arXiv:2306.16215, Sect. III.1].
- **Non-stationary amplitude.** PPTA's first 9 yr limit lies at the 99.8th
  percentile below the full-data amplitude; the collaboration cannot yet
  rule out a non-astrophysical origin [src: arXiv:2306.16215, Sect. III.4].
  Test: sliding-window amplitudes with all pulsars and fixed noise models.
- **Chromatic events read as noise.** If the two J1713+0747 events are not
  modelled, white noise is overestimated [src: arXiv:2306.16213, Sect. V.1];
  unmodelled scattering is absorbed by the DM model and leaks into the
  achromatic channel [src: arXiv:2603.13643, Sect. 9]. Test: deterministic
  dip models with free chromatic index; multi-band or low-frequency data.
- **Solar wind as a correlated signal.** Solar-wind DM is correlated between
  pulsars at similar elongation, a spatially correlated chromatic noise to be
  separated from the GWB [src: arXiv:2603.13643, Sect. 9].
- **Ephemeris absorbed by short data.** A span near Jupiter's period
  degrades ephemeris separation [src: arXiv:2306.16214, Sect. 4.4.2]. Test:
  BayesEphem on and off.
- **Over-reading the p-value tail.** Too few independent scrambles to probe
  ≳ 5σ [src: arXiv:2305.04464]; the OS S/N is not a σ level [src:
  arXiv:2306.16213, Sect. IV]. Test: compare phase shifts, sky scrambles,
  simulations and the generalised χ², as EPTA did.
- **Low-frequency bin driving γ.** The lowest bins have few contributing
  pulsars and the largest weight; EPTA's DR2full γ steepens because of its
  lowest bin [src: arXiv:2306.16214, Sect. 6]. Test: refit without the lowest
  bin; free-spectrum comparison between data subsets.
- **Pulsars that disfavour the signal.** NANOGrav finds three negative HD
  dropout factors; possible causes are noise fluctuations, chromatic
  mismodelling or the pulsar term of the GWB itself [src: arXiv:2306.16213,
  Sect. V.4].
- **LVK correlated noise.** Coherent instrumental lines (1 Hz harmonics
  Hanford–Virgo, a 33.2 Hz line from beating calibration lines) and magnetic
  correlations; frequency notching by coherence (Eq. 10), and a joint
  GWB + magnetic fit [src: arXiv:2101.12130, Sects. III.2, IV.3].

## Reading list
<!-- key: reading-list -->

- Method and application: Agazie et al. 2023, arXiv:2306.16213 — likelihood,
  priors, model comparison, optimal statistic, null tests, validation suite.
- Application: Antoniadis et al. 2023, arXiv:2306.16214 — customised noise
  models, full against recent data, comparison of null-distribution methods.
- Application: Reardon et al. 2023, arXiv:2306.16215 — prior construction,
  factorised likelihood, time dependence of the amplitude.
- Comparison: IPTA 2023, arXiv:2309.00693 — the arrays' noise and frequency
  choices side by side; standardised re-analysis.
- Application: Xu et al. 2023, arXiv:2306.16216 — CPTA single-frequency
  correlation statistic, 16-model noise selection (Sect. 2), scramble tails.
- Application: Miles et al. 2025, arXiv:2412.01153 — MPTA noise-model
  dependence of HD significance; amplitudes of all arrays compared.
- Application: Tahbildar et al. 2026, arXiv:2608.02808 — InPTA DR2 upper limit.
- Combination: Yu et al. 2025, arXiv:2512.08666 — direct combination of five
  arrays' public data.
- Method: Vigeland et al. 2018, arXiv:1805.12188 — noise-marginalised optimal
  statistic.
- Critique: Zic et al. 2022, arXiv:2207.12237 — spurious common-spectrum
  detections and their prior dependence.
- Critique: Di Marco et al. 2023, arXiv:2305.04464 — limits of sky scrambles
  and phase shifts for background estimation.
- Review: Mingarelli et al. 2026, arXiv:2603.13643 — noise-model history and
  chromatic noise.
- Method: LVK 2021, arXiv:2101.12130 — cross-correlation estimator, data
  quality, priors for ground-based limits.

## Not verified
<!-- key: not-verified -->

- Hazboun et al. 2020 (red-noise priors), Goncharov et al. 2022 (spin noise
  covariant with the common process), Hazboun et al. 2023 (generalised χ²),
  Taylor et al. 2017 (phase shifts) and Cornish & Sampson 2016 (sky
  scrambles): known here only through the papers above; no identifier
  recorded.
- CPTA's noise-model paper (Chen et al., in prep. as cited) and its App. A
  toy model; MPTA's noise paper (Miles et al. 2024, as cited); the body of
  InPTA DR2 (abstract only); the five-array Table 3 column headings beyond
  the caption (the values quoted are the text's).
- The IPTA "standardised noise model" itself (arXiv:2309.00693, Sect. III.2)
  and the Lite, FrankenStat and Gibbs combination methods of
  arXiv:2603.13643, Sect. 10 were not read.
- The full Vigeland et al. abstract was not read beyond the title and the
  use NANOGrav makes of it.
