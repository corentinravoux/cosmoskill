# CMB primary anisotropies and lensing — systematics

Scope: the systematic effects that decide whether a CMB power-spectrum or
lensing result can be trusted, with mechanism, measured size, mitigation,
validation test and the reference a referee expects.
Snapshot: 2026-10-07

Flags: `[src]` read this session in the cited paper; `[sec]` from a named
secondary source; `[der]` derived here.

---

## 1. Temperature beams and window functions

**Mechanism.** The measured spectrum is the sky spectrum times B_ℓ². A
fractional beam error δB/B maps into 2δB/B on C_ℓ and grows with ℓ, where it
is degenerate with n_s, Ω_b h² and N_eff through the damping tail.

**Mitigation.** Beams are measured on planets (Uranus for ACT) and bright
point sources, decomposed into modes, and their uncertainty is propagated
into the covariance or sampled as nuisance parameters. ACT froze the beam
and the "leakage beam" before the first unblinding stage and allowed
pre-registered refinements before the second [src] (Louis et al. 2025,
arXiv:2503.14452, App. A).

**Validation.** Array-band and frequency null spectra, which are sensitive
to relative beam errors; consistency of parameters across arrays.

## 2. Polarised beams and temperature-to-polarisation leakage

**Mechanism.** Differential beam shape between orthogonal detectors and
optical cross-polarisation leak T into Q/U. Because TT is much larger than
TE and EE, a sub-percent leakage matters.

**Size where quantified.**

- ACT DR6 models the leakage per array with functions γ_ℓ^TE, γ_ℓ^TB
  measured on Uranus. The typical residual leakage is about 0.3%.
  Neglecting it shifts Ω_b h² by 1.7σ and n_s by 1σ and degrades TE and TB
  null tests [src] (arXiv:2503.14452, Sect. III.3.2).
- SPT-3G D1 detected quadrupolar leakage at 6σ, 6σ and 3.5σ in the 95, 150
  and 220 GHz bands, of order 1% of the signal at large scales in TE and
  reaching 1σ of the 150×150 TE error bar at small scales. It caused the
  failure of TE and EE band-power difference tests above ℓ = 3000 and
  affected TT–TE consistency. It was found after unblinding and is fitted
  at likelihood level with a prior from stacked point-source maps [src]
  (Camphuis et al. 2025, arXiv:2506.20707, Sect. IV.2.2 and App. B).
- SPT-3G D1 also introduced a sidelobe polarisation fraction β_pol per
  band, after noticing EE differences between 95 and 150 GHz on the same
  sky. The D1 data prefer β_pol ≠ 1 at 5σ within ΛCDM; without the
  correction TT and EE disagreed mainly in the n_s–Ω_b h² plane [src]
  (arXiv:2506.20707).
- A direct measurement on 100 bright point sources gives
  β_pol = 0.89 ± 0.10, 1.08 ± 0.10 and 0.90 ± 0.22 at 95, 150 and 220 GHz,
  that is, minimal sidelobe depolarisation, differing from the values
  inferred in the cosmological analysis by an effective 1.3σ. The authors
  list three explanations for the frequency-dependent residuals seen in
  the spectra: a statistical fluctuation, a need for better polarised beam
  models, or a systematic other than beam depolarisation [src] (de Haan et
  al. 2026, arXiv:2602.06334).
- Planck 2018: polarisation efficiencies of the HFI channels are corrected
  empirically, and the choice between map-based and spectrum-based
  corrections moves A_L from 1.180 ± 0.065 to 1.142 ± 0.066 and base
  parameters by up to 0.5σ in ω_b [src] (Planck Collaboration 2018,
  arXiv:1807.06209). The likelihood paper names the accuracy
  of the polarisation-efficiency modelling as the main limitation and
  estimates overall consistency between high-ℓ implementations at better
  than 0.5σ [src] (arXiv:1907.12875).
- For degree-scale B-mode work beam systematics are the dominant
  instrumental systematic of the BICEP receivers; the programme's goal is
  to hold each dominant systematic to 20% of σ(r) or less [src] (Vergès et
  al. 2026, arXiv:2606.13942).

**Referee expectation.** The leakage model, how it was measured, whether
it was in place before unblinding, and the shift in parameters with and
without it.

## 3. Absolute calibration and polarisation efficiency

**Mechanism.** A calibration error rescales C_ℓ and is degenerate with
A_s e^(−2τ). A polarisation-efficiency error rescales TE by one power and EE
by two.

**Practice.** ACT and SPT calibrate against Planck on their own footprints,
so the overall amplitude is not independent of Planck (arXiv:2503.14452,
arXiv:2506.20707). SPT checks that agreement with Planck holds at 0.4σ with
and without the amplitude parameter [src]. For ACT EE alone, freeing the
polarisation efficiency in [0.9, 1.1] roughly doubles the error on Ω_c h²
and H₀ [src] (arXiv:2503.14452, Sect. VIII.1).

**Consequence.** σ₈ from "ACT alone" or "SPT alone" inherits Planck's
calibration and Planck's τ. Only the shape parameters are independent.

## 4. Time-domain filtering, transfer functions, ground and atmosphere

**Mechanism.** Ground experiments suppress atmospheric and ground-
synchronous signal by filtering, which removes sky modes and couples
multipoles.

**Size and mitigation.**

- ACT removes Fourier modes with |ℓ_x| < 90 and |ℓ_y| < 50 and corrects with
  a simulation-calibrated transfer matrix (800 simulations per array-band),
  neglecting ℓ–ℓ' coupling after checking that its correlation length is
  below the bin width [src] (arXiv:2503.14452).
- SPT estimates the filter transfer function from full time-domain
  simulations; residual uncertainty from filtering artefacts and from
  inpainting of point-source holes shifts parameters by less than 0.1σ and
  is left out of the likelihood [src] (arXiv:2506.20707).
- For the largest scales from the ground, CLASS reports that time-domain
  filtering in maximum-likelihood map-making is correctable with a
  pixel-space transfer matrix, leaving a power deficit below 3% from
  map-making non-linearity [src] (Li et al. 2025, arXiv:2501.11904).

**Validation.** Null tests by scan direction, elevation, time and
precipitable water vapour. In ACT's suite of about 2000 nulls the lowest
PTE (0.05%) was in the elevation test, judged acceptable given the number
of tests [src] (arXiv:2503.14452).

## 5. Large-scale polarisation systematics and τ

**Mechanism.** The reionisation bump lies at ℓ ≲ 20, where 1/f noise,
far-sidelobe pickup, ADC non-linearity and Galactic foregrounds are all
largest and where only a few modes exist.

**History of the mitigation.** SRoll2 fits higher-order terms of the HFI
ADC non-linearity that the 2018 release treated to first order, bringing
the residual "below the detector noise level" in simulations [src] (Delouis
et al. 2019, arXiv:1901.11386); the associated τ analysis says the dipole-
distortion systematic is brought below the noise and the τ uncertainty is
reduced by about 40% relative to 2018 [src] (Pagano et al. 2019,
arXiv:1908.09856). NPIPE lowers noise and systematics at essentially all
scales and finds τ robust to data and sky cuts [src] (arXiv:2007.04997).
Different likelihood constructions on the same SRoll2 maps agree and move
τ by about 0.5σ, mostly through the joint treatment of temperature and
polarisation [src] (de Belsunce et al. 2021, arXiv:2103.14378).

**Independent checks.** CLASS × Planck gives 0.053 (+0.018/−0.019), the
first ground-based attempt [src] (arXiv:2501.11904); its error is three
times the Planck one (0.018/0.006) [der]. Reionisation-history data (Lyα forest, damping wings,
dark pixels) combined with CMB data that exclude low-ℓ EE return τ near
0.055–0.067 [src] (Kageura et al. 2026, arXiv:2601.09644; Montero-Camacho &
Mao 2026, arXiv:2607.26373).

**Modelling dependence.** The standard analysis assumes a step-like
(tanh) reionisation and slow-roll primordial spectra. Relaxing the
reionisation model, or treating the low-ℓ temperature deficit as a
physical feature, raises the allowed τ: the Planck 95% upper limit moves
from 0.0696 to 0.075 [src] (Jhaveri et al. 2025, arXiv:2504.21813; 2026,
arXiv:2606.20795).

**Referee expectation.** Name the low-ℓ EE likelihood or τ prior; state
that ACT, SPT and DESI+CMB results all inherit it; cite Sailer et al. 2025
(arXiv:2504.16932) when discussing what a τ shift would do.

## 6. Extragalactic foregrounds in temperature

**Mechanism.** Above ℓ ≈ 2000 the TT spectrum is dominated by the CIB,
radio sources, tSZ and kSZ, which are correlated with each other (tSZ–CIB)
and frequency dependent.

**Size.** The ACT DR6 foreground paper finds that ΛCDM and ΛCDM+N_eff
parameters move by less than 0.5σ under all tested template changes and
model extensions, while some foreground parameters move more; it also
shows recovery of input cosmology from non-Gaussian, correlated sky
simulations built independently of the fitted model [src] (Beringue et al.
2025, arXiv:2506.06274). SPT-3G D1 finds that the inferred tSZ and kSZ
power depends on the tSZ–CIB correlation model and, less, on the assumed
angular shapes [src] (Chaubal et al. 2026, arXiv:2601.20551). ACT DR6
detects a tilt of the SZ spectrum relative to its baseline template [src]
(arXiv:2503.14452).

**Mitigation.** Multi-frequency fit with templates (Dunkley et al. 2013,
arXiv:1301.0776); point-source masking with flux cuts; restricting TT to
ℓ ≤ 3000 (SPT) while using TE and EE to 4000, since polarised foregrounds
are much weaker [src] (arXiv:2506.20707).

**Validation.** Frequency-split parameter consistency. SPT orders its
frequency spectra to expose foreground mis-modelling and notes a trend in
Ω_b h² and n_s across TT frequencies that remains consistent with the null
hypothesis [src] (arXiv:2506.20707).

## 7. Galactic foregrounds and B modes

**Mechanism.** Polarised dust and synchrotron exceed the primordial B-mode
signal everywhere on the sky at the levels now probed.

**History.** The joint BICEP2/Keck–Planck analysis found strong evidence
for dust and no significant tensor signal, r_0.05 < 0.12 [src]
(arXiv:1502.00612). BK18 fits a seven-parameter foreground model without
an external prior on the dust spectral index, with 220 GHz maps whose
signal-to-noise on dust exceeds that of Planck 353 GHz [src]
(arXiv:2110.00483). Planck 2018 measures mean polarised indices
β_d = 1.55 ± 0.05 and β_s = −3.1 ± 0.1 [src] (arXiv:1807.06208).

**For TT/TE/EE.** Galactic dust is a minor term at high latitude and is
fitted with an amplitude per spectrum type.

**Lensing B modes** are now a comparable limitation: the SPT-3G D1 lensing
template built with a profile-hardened estimator and a CIB tracer keeps
foreground-induced bias below 10% of the statistical error on the template
power in simulations [src] (Nakato et al. 2026, arXiv:2608.06343).

Details of r analyses belong to `cosmo-inflation-primordial`.

## 8. Foregrounds in lensing reconstruction

**Mechanism.** tSZ, CIB and point sources are non-Gaussian and correlated
with the lensing field; they bias the temperature quadratic estimator
through their trispectrum and their bispectrum with κ.

**Size and mitigation.** For ACT DR6, source and cluster finding and
subtraction plus a profile bias-hardened estimator reduce the bias on
A_lens to below 0.2σ; a CIB-deprojected variant using Planck high-frequency
data performs similarly and agrees on the data; other frequency-cleaned
options either cost too much noise or are biased [src] (MacCrann et al.
2023, arXiv:2304.05196). Methods: bias hardening (Namikawa et al. 2012,
arXiv:1209.0091), gradient cleaning (Madhavacheril & Hill 2018,
arXiv:1802.08230), polarisation-only reconstruction (Ge et al. 2024,
arXiv:2411.06000).

**Validation.** Two independent sky simulations; frequency-difference
nulls at map and band-power level; consistency between estimators with
different foreground immunity (arXiv:2304.05196, arXiv:2608.06343).
Planck 2018 restricts its likelihood to 8 ≤ L ≤ 400 because higher L shows
some evidence of a curl-test failure [src] (arXiv:1807.06209).
SPT-3G 2018 quotes its amplitude "excluding instrumental and astrophysical
systematic uncertainties" and marginalises a foreground bias template in
its parameter fits [src] (Pan et al. 2023, arXiv:2308.11608).

## 9. Lensing-related modelling of the primary spectra

- **Non-linear growth and baryons.** At ℓ ≳ 3000 the lensed spectra depend
  on C_L^κκ at scales affected by non-linear evolution and feedback.
  Forecast biases for a CMB-S4-like survey reach 1.6σ on H₀ and 1.2σ on
  N_eff; removing TT above ℓ = 3000 or marginalising feedback parameters
  mitigates them (forecast) [src] (McCarthy et al. 2021, arXiv:2103.05582).
  ACT DR6 uses a dark-matter-only non-linear model without feedback [src]
  (Calabrese et al. 2025, arXiv:2503.14454). SPT detects non-linear
  evolution in the lensing spectrum at more than 3σ [src]
  (arXiv:2411.06000).
- **Super-sample lensing.** Modes larger than the survey dilate the
  acoustic scale coherently. It should be included for surveys with less
  than 10% of the sky that measure the damping tail at ℓ ≳ 1500; omitted,
  it produces apparently conflicting θ values [src] (Manzotti et al. 2014,
  arXiv:1401.7992). SPT-3G D1 samples the mean convergence κ of the field
  as a nuisance parameter [src] (arXiv:2506.20707). Tristram et al. 2023
  checked it is negligible for Planck's sky fraction [src]
  (arXiv:2309.10034).
- **Aberration.** Our velocity (β = 0.00123) shifts multipoles on a partial
  sky by ΔL/L ≈ β⟨cos θ⟩; ignored, it biases θ* at the 0.01% level,
  comparable to Planck's uncertainty [src] (Jeong et al. 2013,
  arXiv:1309.2285). ACT corrects for it with 300 simulations [src]
  (arXiv:2503.14452).

## 10. Covariance accuracy

Analytic pseudo-C_ℓ covariances are approximate on small or inhomogeneous
footprints. Earlier fast approximations are good to about 5% on the SPT-3G
footprint for wide bins and an improved one to 1% [src] (Camphuis et al.
2022, arXiv:2204.13721). The ACT DR6 prescription agrees with simulations
to 3% (16% for the earlier prescription) and to 1% after a simulation-
based correction [src] (Atkins et al. 2024, arXiv:2412.07068). Lensing
analyses use simulation covariances with a Hartlap correction (792
simulations for ACT DR6) [src] (Qu et al. 2023, arXiv:2304.05202).

## 11. Theory-code accuracy

Default Boltzmann precision settings are not sufficient for DR6-class data
(arXiv:2103.05582). ACT DR6 and SPT-3G D1 share the same increased
accuracy settings, and emulators are trained on high-precision spectra
[src] (arXiv:2506.20707). The helium abundance from different BBN codes
has negligible impact on the primary spectra, but the N_eff assumed in the
BBN table (3.044 versus 3.046) must be made consistent [src]
(arXiv:2503.14454).

## 12. Correlated data and common inputs when combining experiments

- ACT and Planck overlap on the sky. P-ACT avoids double counting by
  cutting Planck at ℓ < 1000 (TT) and ℓ < 600 (TE, EE) instead of modelling
  the cross-covariance; ACT estimates that a full treatment would improve
  σ(N_eff) by less than 5% [src] (arXiv:2503.14452).
- SPT does not quote a consistency statistic between SPT+ACT and Planck
  for A_2pt because the ACT data are significantly correlated with Planck
  [src] (arXiv:2506.20707).
- All ground results share Planck's calibration and Planck's τ (Sections 3
  and 5).
- The three lensing reconstructions were combined with their overlap
  modelled in Qu et al. 2025 (arXiv:2504.20038).
- Shifts between a data set and its subset are expected to be larger than
  naive intuition; Planck's ℓ < 800 versus ℓ > 800 parameter shifts are
  exceeded in 15% of simulations (χ²) and a 2.2σ single-parameter
  deviation occurs in 9% [src] (Planck Collaboration 2016,
  arXiv:1608.02487).

## 13. Post-unblinding changes

Both 2025 ground analyses changed their pipelines after unblinding: ACT
raised the polarisation ℓ_min (arXiv:2503.14452, App. B); SPT added two
instrumental models and updated its foreground model (arXiv:2506.20707,
App. B). Both document the changes and their motivation by cosmology-
independent tests. A reader should treat the documented change log as
part of the result.

## 14. Polarisation angle

A global angle miscalibration rotates E into B and generates EB and TB. It
is degenerate with cosmic birefringence unless the angle is calibrated
independently or solved jointly using Galactic foregrounds. The ACT DR6
birefringence analysis uses priors from the optics model and marginalises
residual intensity-to-polarisation leakage, and states that unexplained
systematics in the ACT data prevent strong cosmological conclusions [src]
(Diego-Palazuelos & Komatsu 2025, arXiv:2509.13654).

---

## What a referee checks in a CMB results section

1. Which Planck likelihood (Plik PR3, CamSpec PR3/PR4, HiLLiPoP PR4) and
   which low-ℓ EE likelihood or τ prior; whether Planck was truncated when
   combined with ACT.
2. Whether "CMB" includes lensing reconstruction, and which one.
3. Multipole ranges per spectrum and frequency, and whether they were
   fixed before unblinding.
4. Beam, leakage and polarisation-efficiency treatment; parameter shifts
   with and without each correction.
5. Foreground-model robustness: template variations and frequency-split
   consistency, with the size of the induced parameter shifts.
6. Null-test suite: number of tests, PTE distribution, treatment of
   correlated tests, and what was cut as a result.
7. Covariance construction and its validation against simulations.
8. Boltzmann-code accuracy settings, non-linear lensing model, recombination
   code, N_eff value assumed, neutrino-mass convention.
9. For lensing: N⁰ and N¹ subtraction method, foreground-mitigation
   estimator, L range, fiducial model for the quoted amplitude.
10. Significance statements: both endpoints named, model stated, and the
    arXiv version of the number (the CMB-SPA and ACT Σm_ν values changed
    between versions).
11. Whether a claimed consistency between experiments accounts for shared
    sky, shared calibration and shared τ.

## Not verified

- The NPIPE low-ℓ polarisation transfer function and its handling in
  LoLLiPoP were not read this session.
- The ACT DR6 beam paper and the SPT-3G D1 beam description were not read
  directly; beam statements above come from the power-spectrum papers.
- Atmospheric-noise characterisation at the South Pole (a 2026 BICEP/Keck
  paper exists) was not read.
- Bandpass uncertainties: ACT DR6 samples five bandpass-shift parameters
  [src] (arXiv:2503.14452); their priors and impact were not read.
