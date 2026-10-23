# CMB primary anisotropies and lensing — systematics

Scope: the systematic effects that decide whether a CMB power-spectrum or
lensing result can be trusted, with mechanism, measured size, mitigation,
validation test and the reference a referee expects.
Snapshot: 2026-10-14

Flags: `[src]` read this session in the cited paper; `[sec]` from a named
secondary source; `[der]` derived here.

---

## 1. Temperature beams and window functions
<!-- key: temperature-beams-and-window-functions -->

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
<!-- key: polarised-beams-and-temperature-to-polarisation -->

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
  correction TT and EE disagreed mainly in the n_s–Ω_b h² plane [src: Sect. I]
  (arXiv:2506.20707).
- A direct measurement on 100 bright point sources gives
  β_pol = 0.89 ± 0.10, 1.08 ± 0.10 and 0.90 ± 0.22 at 95, 150 and 220 GHz,
  that is, minimal sidelobe depolarisation, differing from the values
  inferred in the cosmological analysis by an effective 1.3σ. The authors
  list three explanations for the frequency-dependent residuals seen in
  the spectra: a statistical fluctuation, a need for better polarised beam
  models, or a systematic other than beam depolarisation [src: abstract] (de Haan et
  al. 2026, arXiv:2602.06334).
- Planck 2018: polarisation efficiencies of the HFI channels are corrected
  empirically, and the choice between map-based and spectrum-based
  corrections moves A_L from 1.180 ± 0.065 to 1.142 ± 0.066 and base
  parameters by up to 0.5σ in ω_b (Planck Collaboration 2018,
  arXiv:1807.06209) [src: Sect. 2.2.1]. The likelihood paper names the
  accuracy of the polarisation-efficiency modelling as the main limitation
  and estimates overall consistency between high-ℓ implementations at
  better than 0.5σ (arXiv:1907.12875) [src: abstract].
- For degree-scale B-mode work beam systematics are the dominant
  instrumental systematic of the BICEP receivers; the programme's goal is
  to hold each dominant systematic to 20% of σ(r) or less (Vergès et
  al. 2026, arXiv:2606.13942) [src: abstract].

**Referee expectation.** The leakage model, how it was measured, whether
it was in place before unblinding, and the shift in parameters with and
without it.

## 3. Absolute calibration and polarisation efficiency
<!-- key: absolute-calibration-and-polarisation-efficiency -->

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
<!-- key: time-domain-filtering-transfer-functions-ground -->

**Mechanism.** Ground experiments suppress atmospheric and ground-
synchronous signal by filtering, which removes sky modes and couples
multipoles.

**Size and mitigation.**

- ACT removes Fourier modes with |ℓ_x| < 90 and |ℓ_y| < 50 and corrects with
  a simulation-calibrated transfer matrix (800 simulations per array-band),
  neglecting ℓ–ℓ' coupling after checking that its correlation length is
  below the bin width [src: Sect. I] (arXiv:2503.14452).
- SPT estimates the filter transfer function from full time-domain
  simulations; residual uncertainty from filtering artefacts and from
  inpainting of point-source holes shifts parameters by less than 0.1σ and
  is left out of the likelihood (arXiv:2506.20707) [src: Sect. V.2,
  Sect. IV.1.1].
- For the largest scales from the ground, CLASS reports that time-domain
  filtering in maximum-likelihood map-making is correctable with a
  pixel-space transfer matrix, leaving a power deficit below 3% from
  map-making non-linearity [src] (Li et al. 2025, arXiv:2501.11904).

**Validation.** Null tests by scan direction, elevation, time and
precipitable water vapour. In ACT's suite of about 2000 nulls the lowest
PTE (0.05%) was in the elevation test, judged acceptable given the number
of tests (arXiv:2503.14452) [src: Sect. IV.1, Fig. 5 caption].

## 5. Large-scale polarisation systematics and τ
<!-- key: large-scale-polarisation-systematics-and-tau -->

**Mechanism.** The reionisation bump lies at the lowest multipoles, where 1/f noise,
far-sidelobe pickup, ADC non-linearity and Galactic foregrounds are all
largest and where only a few modes exist.

**History of the mitigation.** SRoll2 fits higher-order terms of the HFI
ADC non-linearity that the 2018 release treated to first order, bringing
the residual "below the detector noise level" in simulations (Delouis
et al. 2019, arXiv:1901.11386) [src: abstract]; the associated τ analysis
says the dipole-distortion systematic is brought below the noise and the τ
uncertainty is reduced by about 40% relative to 2018 (Pagano et al. 2019,
arXiv:1908.09856) [src: abstract]. NPIPE lowers noise and systematics at
essentially all scales and finds τ robust to data and sky cuts
(arXiv:2007.04997) [src: abstract]. Different likelihood constructions on
the same SRoll2 maps agree and move τ by about 0.5σ, mostly through the
joint treatment of temperature and polarisation (de Belsunce et al. 2021,
arXiv:2103.14378) [src: abstract].

**Independent checks.** CLASS × Planck gives 0.053 (+0.018/−0.019), the
first ground-based attempt (arXiv:2501.11904) [src: abstract].
Reionisation-history data (Lyα forest, damping wings, dark pixels)
combined with CMB data that exclude low-ℓ EE return τ = 0.0552
(+0.0019/−0.0026 stat) (+0.0075/−0.0049 sys) (Kageura et al. 2026,
arXiv:2601.09644) and 0.067 ± 0.011 (Montero-Camacho & Mao 2026,
arXiv:2607.26373) [src: abstract].

**Modelling dependence.** The standard analysis assumes a step-like
(tanh) reionisation and slow-roll primordial spectra. Relaxing the
reionisation model, or treating the low-ℓ temperature deficit as a
physical feature, raises the allowed τ: the Planck 95% upper limit moves
from 0.0696 to 0.075 (Jhaveri et al. 2025, arXiv:2504.21813; 2026,
arXiv:2606.20795) [src: abstract].

**Referee expectation.** Name the low-ℓ EE likelihood or τ prior; state
that ACT, SPT and DESI+CMB results all inherit it; cite Sailer et al. 2025
(arXiv:2504.16932) when discussing what a τ shift would do.

## 6. Extragalactic foregrounds in temperature
<!-- key: extragalactic-foregrounds-in-temperature -->

**Mechanism.** Above ℓ ≈ 2000 the TT spectrum is dominated by the CIB,
radio sources, tSZ and kSZ, which are correlated with each other (tSZ–CIB)
and frequency dependent.

**Size.** The ACT DR6 foreground paper finds that ΛCDM and ΛCDM+N_eff
parameters move by less than 0.5σ under all tested template changes and
model extensions, while some foreground parameters move more; it also
shows recovery of input cosmology from non-Gaussian, correlated sky
simulations built independently of the fitted model (Beringue et al.
2025, arXiv:2506.06274) [src: abstract]. SPT-3G D1 finds that the inferred tSZ and kSZ
power depends on the tSZ–CIB correlation model and, less, on the assumed
angular shapes [src] (Chaubal et al. 2026, arXiv:2601.20551). ACT DR6
detects a tilt of the SZ spectrum relative to its baseline template [src]
(arXiv:2503.14452).

**Mitigation.** Multi-frequency fit with templates (Dunkley et al. 2013,
arXiv:1301.0776); point-source masking with flux cuts; restricting TT to
ℓ ≤ 3000 (SPT) while using TE and EE to 4000, since polarised foregrounds
are much weaker (arXiv:2506.20707) [src: Sect. IV.4].

**Validation.** Frequency-split parameter consistency. SPT orders its
frequency spectra to expose foreground mis-modelling and notes a trend in
Ω_b h² and n_s across TT frequencies that remains consistent with the null
hypothesis [src] (arXiv:2506.20707).

## 7. Galactic foregrounds and B modes
<!-- key: galactic-foregrounds-and-b-modes -->

**Mechanism.** Polarised dust and synchrotron exceed the primordial B-mode
signal everywhere on the sky at the levels now probed.

**History.** The joint BICEP2/Keck–Planck analysis found strong evidence
for dust and no significant tensor signal, r_0.05 < 0.12
(arXiv:1502.00612) [src: abstract]. BK18 fits a seven-parameter foreground
model without an external prior on the dust spectral index, with 220 GHz
maps whose signal-to-noise on dust exceeds that of Planck 353 GHz
(arXiv:2110.00483) [src: abstract]. Planck 2018 measures mean polarised
indices β_d = 1.55 ± 0.05 and β_s = −3.1 ± 0.1 (arXiv:1807.06208) [src:
abstract].

**For TT/TE/EE.** Galactic dust is a minor term at high latitude and is
fitted with an amplitude per spectrum type.

**Lensing B modes** are now a comparable limitation: the SPT-3G D1 lensing
template built with a profile-hardened estimator and a CIB tracer keeps
foreground-induced bias below 10% of the statistical error on the template
power in simulations (Nakato et al. 2026, arXiv:2608.06343) [src: abstract].

Details of r analyses belong to `cosmo-inflation-primordial`.

## 8. Foregrounds in lensing reconstruction
<!-- key: foregrounds-in-lensing-reconstruction -->

**Mechanism.** tSZ, CIB and point sources are non-Gaussian and correlated
with the lensing field; they bias the temperature quadratic estimator
through their trispectrum and their bispectrum with κ.

**Size and mitigation.** For ACT DR6, source and cluster finding and
subtraction plus a profile bias-hardened estimator reduce the bias on
A_lens to below 0.2σ; a CIB-deprojected variant using Planck high-frequency
data performs similarly and agrees on the data; other frequency-cleaned
options either cost too much noise or are biased (MacCrann et al.
2023, arXiv:2304.05196) [src: abstract]. Methods: bias hardening (Namikawa et al. 2012,
arXiv:1209.0091), gradient cleaning (Madhavacheril & Hill 2018,
arXiv:1802.08230), polarisation-only reconstruction (Ge et al. 2024,
arXiv:2411.06000).

**Validation.** Two independent sky simulations; frequency-difference
nulls at map and band-power level; consistency between estimators with
different foreground immunity (arXiv:2304.05196, arXiv:2608.06343).
Planck 2018 restricts its likelihood to 8 ≤ L ≤ 400 because higher L shows
marginal evidence for null-test failures in the lensing curl and frequency
consistency (arXiv:1807.06210) [src: Sect. 3.2].
SPT-3G 2018 quotes its amplitude "excluding instrumental and astrophysical
systematic uncertainties" and marginalises a foreground bias template in
its parameter fits [src] (Pan et al. 2023, arXiv:2308.11608).

## 9. Lensing-related modelling of the primary spectra
<!-- key: lensing-related-modelling-of-the-primary-spectra -->

- **Non-linear growth and baryons.** At ℓ ≳ 3000 the lensed spectra depend
  on C_L^κκ at scales affected by non-linear evolution and feedback.
  Forecast biases for a CMB-S4-like survey reach 1.6σ on H₀ and 1.2σ on
  N_eff; removing TT above ℓ = 3000 or marginalising feedback parameters
  mitigates them (forecast) (McCarthy et al. 2021, arXiv:2103.05582) [src:
  abstract].
  ACT DR6 uses a dark-matter-only non-linear model without feedback [src]
  (Calabrese et al. 2025, arXiv:2503.14454). SPT detects non-linear
  evolution in the lensing spectrum at more than 3σ [src]
  (arXiv:2411.06000).
- **Super-sample lensing.** Modes larger than the survey dilate the
  acoustic scale coherently. It should be included for surveys with less
  than 10% of the sky that measure the damping tail at ℓ ≳ 1500; omitted,
  it produces apparently conflicting θ values (Manzotti et al. 2014,
  arXiv:1401.7992) [src: abstract]. SPT-3G D1 samples the mean convergence κ of the field
  as a nuisance parameter [src] (arXiv:2506.20707). Tristram et al. 2023
  checked it is negligible for Planck's sky fraction [src]
  (arXiv:2309.10034).
- **Aberration.** Our velocity (β = 0.00123) shifts multipoles on a partial
  sky by ΔL/L ≈ β⟨cos θ⟩; ignored, it biases θ* at the 0.01% level,
  comparable to Planck's uncertainty (Jeong et al. 2013,
  arXiv:1309.2285) [src: abstract]. ACT corrects for it with 300
  simulations (arXiv:2503.14452) [src: Sect. III.3.3].

## 10. Covariance accuracy
<!-- key: covariance-accuracy -->

Analytic pseudo-C_ℓ covariances are approximate on small or inhomogeneous
footprints. Earlier fast approximations are good to about 5% on the SPT-3G
footprint for wide bins and an improved one to 1% (Camphuis et al.
2022, arXiv:2204.13721) [src: abstract]. The ACT DR6 prescription agrees
with simulations to 3% (16% for the earlier prescription) and to 1% after
a simulation-based correction (Atkins et al. 2024, arXiv:2412.07068) [src:
abstract]. Lensing analyses use simulation covariances with a Hartlap
correction (792 simulations for ACT DR6) (Qu et al. 2023,
arXiv:2304.05202) [src: Sect. V.11].

## 11. Theory-code accuracy
<!-- key: theory-code-accuracy -->

Default Boltzmann precision settings are not sufficient for DR6-class data
(arXiv:2103.05582). ACT DR6 and SPT-3G D1 share the same increased
accuracy settings, and emulators are trained on high-precision spectra
[src] (arXiv:2506.20707). The helium abundance from different BBN codes
has negligible impact on the primary spectra, but the N_eff assumed in the
BBN table (3.044 versus 3.046) must be made consistent [src]
(arXiv:2503.14454).

## 12. Correlated data and common inputs when combining experiments
<!-- key: correlated-data-and-common-inputs-when -->

- ACT and Planck overlap on the sky. P-ACT avoids double counting by
  cutting Planck at ℓ < 1000 (TT) and ℓ < 600 (TE, EE) instead of modelling
  the cross-covariance; ACT estimates that a full treatment would improve
  σ(N_eff) by less than 5% [src: Sect. IV.1] (arXiv:2503.14452).
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
  deviation occurs in 9% [src: abstract] (Planck Collaboration 2016,
  arXiv:1608.02487).

## 13. Post-unblinding changes
<!-- key: post-unblinding-changes -->

Both 2025 ground analyses changed their pipelines after unblinding: ACT
raised the polarisation ℓ_min (arXiv:2503.14452, App. B); SPT added two
instrumental models and updated its foreground model (arXiv:2506.20707,
App. B). Both document the changes and their motivation by cosmology-
independent tests. A reader should treat the documented change log as
part of the result.

## 14. Polarisation angle
<!-- key: polarisation-angle -->

A global angle miscalibration rotates E into B and generates EB and TB. It
is degenerate with cosmic birefringence unless the angle is calibrated
independently or solved jointly using Galactic foregrounds. The ACT DR6
birefringence analysis uses priors from the optics model and marginalises
residual intensity-to-polarisation leakage, and states that unexplained
systematics in the ACT data prevent strong cosmological conclusions [src]
(Diego-Palazuelos & Komatsu 2025, arXiv:2509.13654).

## 15. Nuisance priors and test sizes by analysis
<!-- key: nuisance-priors-and-test-sizes-by-analysis -->

Read in the paper bodies; one table per analysis. "Shift" is the change of
the posterior mean in units of its σ, for the data combination named.

### ACT DR6 power spectra (Louis et al. 2025, arXiv:2503.14452)
<!-- key: act-dr6-power-spectra-louis-et-al-2025-arxiv -->

From arXiv:2503.14452:

| Item | Prior or size | Place |
|---|---|---|
| Foreground model | 15 parameters, 14 free (9 TT, 2 TE, 2 EE, one radio index common to all); β_p ≡ β_c; wide non-negative uniform priors on amplitudes | [src: Sect. VII.2, Table 3] |
| Galactic dust amplitudes at ℓ = 500, 150 GHz (data) | Gaussian: TT 7.95 ± 0.32, TE 0.42 ± 0.03, EE 0.168 ± 0.017 μK², from Planck 353–143 GHz | [src: Table 3, Sect. VI.1.2] |
| tSZ–CIB correlation ξ | uniform 0 ≤ ξ ≤ 0.2 on data | [src: Table 3] |
| Dipole calibration (Planck) | 1 ± 0.003 | [src: Table 4] |
| Per-array gain calibration | 1 ± 0.0016 to 1 ± 0.0024 (f090/f150), 1 ± 0.013 (PA4 f220); twice the measured error | [src: Sect. VI.1.5, Table 4] |
| Polarisation efficiency, four array-bands | uniform 0.9 < p < 1.1 | [src: Sect. VII.2, Table 4] |
| Bandpass shifts, five array-bands | Gaussian 0 ± 1.0 to 1.3 GHz, 0 ± 3.6 GHz for PA4 f220; measured with a Fourier-transform spectrometer | [src: Sect. VI.1.4, Table 4] |
| Beam chromaticity | neglecting it shifts foreground parameters by up to 1σ; added after unblinding | [src: Sect. VI.1.4, App. B] |
| tSZ shape α_tSZ | −0.6 ± 0.2 (P-ACT), non-zero at 3σ; the only foreground extension that moves cosmology at the 0.5σ level; 10% correlated with Ω_b h² and n_s | [src: Sect. VIII.6, Eq. 48] |
| Free CIB SEDs (β_c ≠ β_p) | moves SZ amplitudes by about 1σ | [src: Sect. VIII.6, Table 7] |
| Polarised dust slope free, or dust prior removed | n_s and Ω_b h² (ACT alone) shift by 0.2–0.3σ, others < 0.1σ | [src: Sect. VIII.6] |
| f090 versus f150 parameters | largest single shifts 1.4σ (Ω_c h²), 1.3σ (n_s); 5-parameter PTE 50% (TT/TE/EE), 53% (TE/EE); 0.8% and 1.7% with the pre-unblinding settings | [src: Sect. VII.3.2, Eqs. 34–35] |
| Post-unblinding changes | cosmology shifts come from the raised polarisation ℓ_min (mainly n_s) and α_tSZ; 4-pass maps and final covariance negligible | [src: App. B] |
| Planck polarisation efficiency | Planck fixes it from TT in ΛCDM; freeing it does not broaden P-ACT EE posteriors | [src: App. G.3] |

### SPT-3G D1 T&E (Camphuis et al. 2025, arXiv:2506.20707)
<!-- key: spt-3g-d1-t-e-camphuis-et-al-2025-arxiv-2506 -->

From arXiv:2506.20707:

| Item | Prior or size | Place |
|---|---|---|
| External temperature calibration (to Planck) | N(1.0, 0.0036); posterior 1.0002 ± 0.0036 | [src: App. D, Table 9] |
| Polarisation efficiency, relative calibrations | uniform U(0.8, 1.2) in the full likelihood; Gaussian "subset priors" from Planck (e.g. E_cal N(1.0, 0.0095)) only for subsets; posterior E_cal 1.0095 ± 0.0051 | [src: Table 9] |
| Temperature beam | nine eigenmode amplitudes, standard-normal priors; broadening the priors ×100 shifts n_s by < 0.5σ, all others < 0.2σ; ×5 broadening < 0.1σ | [src: App. D] |
| Quadrupolar T→P leakage ε₂ | Gaussian priors from maps: −0.0065 ± 0.0011 (95), −0.012 ± 0.0021 (150), −0.023 ± 0.0066 (220 GHz); left free, < 3σ from the map prior | [src: Table 9, App. D] |
| Sidelobe polarisation fraction β_pol | uniform U(0, 1); posteriors 0.48 (+0.13/−0.12), 0.62 (+0.17/−0.15), 0.62 ± 0.15 at 95, 150, 220 GHz | [src: Table 9] |
| Foregrounds | Galactic dust priors from Planck maps on the field; Poisson amplitudes U(0, 200) μK² per cross-frequency; CIB clustering index N(0.53, 0.1); Agora tSZ and kSZ templates (AGN heating 10⁸ K); tSZ–CIB and 95 GHz CIB clustering marginalised in the covariance | [src: Sect. V.2.2] |
| Foreground variations (CIB prior, Agora CIB or CIB+tSZ templates, extended model) | all cosmological shifts < 0.2σ (Fisher estimate) | [src: App. E.2] |
| Inter-frequency parameter tests | 15 tests, pass threshold PTE 0.05/15 = 0.0033; all pass | [src: Sect. VI.4, Table 2] |
| Effect of the post-unblinding models | at unblinding TE parameters failed every consistency test with TT and EE; the Ω_b h² shift came from T→P leakage, the n_s shift from leakage and the sidelobe model | [src: App. B.4] |

### Planck 2018 Plik high-ℓ likelihood (Planck Collaboration 2019, arXiv:1907.12875)
<!-- key: planck-2018-plik-high-ell-likelihood-planck -->

From arXiv:1907.12875 unless a row names another paper:

| Item | Prior or size | Place |
|---|---|---|
| Absolute map calibration y_cal | Gaussian 1 ± 0.0025 | [src: Table 16] |
| TT inter-frequency calibration | c_100 = 1.0002 ± 0.0007, c_217 = 0.99805 ± 0.00065 | [src: Table 16] |
| Polarisation efficiency (EE) | fixed corrections c_EE = 1.021, 0.966, 1.04 at 100, 143, 217 GHz, set from the TT ΛCDM best fit; they lower χ² by 50; the EE-versus-TE test of these corrections fails at 2σ | [src: Table 16, Sect. 5.2] |
| Map-based versus spectrum-based efficiency model | minor in ΛCDM (Δχ² = 10); about 0.5σ on some parameters of extended models | [src: Sect. 5.2, Sect. 3.7] |
| T→P beam leakage | fixed template, the dominant systematic in TE; with other processing it lowers TE χ² by about 74; TE inter-frequency PTE still 0.9% | [src: Sect. 3.4, Sect. 5.2] |
| Foregrounds, TT | Poisson amplitudes [0, 400] μK²; CIB [0, 200]; tSZ, kSZ [0, 10] with joint prior D^kSZ + 1.6 D^tSZ = 9.5 ± 3 μK²; ξ ∈ [0, 1]; dust at ℓ = 200, e.g. 8.6 ± 2 (100) to 91.9 ± 20 μK² (217) | [src: Table 16] |
| Foregrounds, TE and EE | TE dust Gaussian priors from 353 GHz (0.13 ± 0.042 to 1.938 ± 0.54 μK² at ℓ = 500); EE dust amplitudes fixed (0.040–0.70 μK²) | [src: Table 16] |
| EE correlated-noise template | from FFP10; ignoring it biases ω_b by 0.25σ (EE alone) | [src: Sect. 5.2] |
| Simulations | n_s bias 0.1σ (TT) from the Gaussian approximation at low ℓ; 0.16σ possible on n_s from TE alone | [src: Sect. 5.2] |
| Lifting nuisance priors | ΛCDM shifts < 0.5σ (largest on ln 10¹⁰A_s); ΛCDM+A_L < 0.4σ; N_eff 1.1σ, which is 1.8σ_exp for a data subset | [src: Sect. 3.8] |
| Plik versus CamSpec (TT,TE,EE) | most ΛCDM parameters within 0.5σ (TT alone 0.2σ); A_L differs by 0.7σ, Ω_K by 0.5σ; for Ω_K the Δχ² = 11 preference falls to 5.2 with spectrum-based efficiencies (CamSpec: 4.3) | [src: arXiv:1807.06209, Sect. 2.2.5] |

### Planck PR4 CamSpec (Rosenberg et al. 2022, arXiv:2205.10869)
<!-- key: planck-pr4-camspec-rosenberg-et-al-2022-arxiv -->

From arXiv:2205.10869:

| Item | What was done | Place |
|---|---|---|
| TT calibration | factor per spectrum relative to 143×143 over 50 ≤ ℓ ≤ 500 (cosmic variance removed by differencing), read as beam-transfer errors | [src: Sect. 3.4.1, Eq. 2] |
| Effective polarisation efficiencies | one factor per TE or EE spectrum fitted to the CamSpec TT ΛCDM best fit and divided out before coaddition (spectrum-based); TE-predicted EE factors track the measured ones; overall c_TE, c_EE remain likelihood parameters | [src: Sect. 3.4.2, Eq. 3] |
| T→P leakage from beam mismatch | QuickPol off-diagonal beam-matrix correction applied to TE, negligible for EE; checked with TE "triplets" sharing a polarisation map | [src: Sect. 3.4.3, Eq. 4] |

### ACT DR6 lensing (Qu et al. 2023, arXiv:2304.05202; MacCrann et al. 2023, arXiv:2304.05196)
<!-- key: act-dr6-lensing-qu-et-al-2023-arxiv-2304-05202 -->

ΔA_lens over the baseline 40 ≤ L ≤ 763, MV estimator (polarisation-only
MVPol in brackets); conservative models are upper limits. Rows from
arXiv:2304.05202 (Table 3, Sect. V) unless they name arXiv:2304.05196.

| Item | Size | Place |
|---|---|---|
| Miscalibration | 0.0043, 0.18σ (MVPol 0.09σ) | [src: 2304.05202, Table 3] |
| Beam uncertainty | 0.0011, 0.05σ | [src: Table 3] |
| T→P leakage, Uranus beam model / constant (conservative) | −0.01σ / −0.19σ (MVPol −0.18σ) | [src: Table 3] |
| Polarisation efficiency lowered by 1σ, fully correlated | −0.0090, −0.37σ (MVPol −0.38σ) | [src: Table 3] |
| Polarisation angle rotated by −0.16° | ≤ 0.01σ | [src: Table 3] |
| Fiducial CMB spectra in the normalisation (ACT DR4+WMAP instead of Planck) | A_lens moves 0.23σ; spectrum uncertainty added to the lensing-alone covariance (+3% on band-power errors; σ(S₈^CMBL) 0.021 → 0.022) | [src: 2304.05202, Sect. V.10] |
| Mean field | exceeds the signal near L ~ 20; one reason for L_min = 40 | [src: Sect. V.9] |
| Extragalactic foregrounds, baseline (source and cluster subtraction + profile hardening) | ΔA_lens^MV −0.0042 (websky), −0.0009 (S10) against σ = 0.023, i.e. −0.18σ and −0.04σ; TT-only −0.31σ and −0.06σ; < 0.3σ up to L_max = 1300 | [src: 2304.05196, Sect. V.1, Table 1] |
| CIB-deprojected variant with Planck | ΔA_lens^MV −0.0032 (websky), −0.0013 (S10) | [src: 2304.05196, Table 1] |
| tSZ-deprojected + point-source hardening | MV error 0.041–0.042 instead of 0.023 | [src: 2304.05196, Table 1] |

### Planck 2018 lensing (Planck Collaboration 2018, arXiv:1807.06210)
<!-- key: planck-2018-lensing-planck-collaboration-2018 -->

From arXiv:1807.06210:

| Item | What was done or found | Place |
|---|---|---|
| CIB bias, temperature-only | 2% negative bias at 217 GHz on 8 ≤ L ≤ 400 from the LSS bispectrum; an order of magnitude smaller after SMICA cleaning; sub-percent with tSZ-deprojected SMICA weights; curl negligible | [src: Sect. 4.5, Fig. 23] |
| Foreground simulations | residual extragalactic power is Gaussian in the baseline simulations; correlated non-Gaussian PSM simulations used as a test | [src: Sect. 4.5] |
| N¹ | subtracted analytically in the FFP10 fiducial model, model dependence corrected perturbatively in the likelihood; realisation-dependent and simulation-based N¹ tested | [src: Sect. 4.8, Eq. 78] |

### SPT-3G D1 lensing (Omori et al. 2026, arXiv:2608.31136)
<!-- key: spt-3g-d1-lensing-omori-et-al-2026-arxiv-2608 -->

From arXiv:2608.31136:

| Item | What was done or found | Place |
|---|---|---|
| Foreground and instrument model | not subtracted as fixed biases: an emulator trained on Agora simulations and on pipeline reruns with varied instrumental parameters rescales the model band powers, sampled jointly with cosmology | [src: Sect. VI.2.3, Eq. 40] |
| Foreground bias, baseline GMV | ≲ 10% of the signal at L ≤ 1000 from difference spectra; corrected GMV versus PP, cross-ILC and tSZ-deprojected PTE 0.80, 0.46, 0.06; a high-L trend tested by dropping the last two bins | [src: Sect. V.3.3] |
| Temperature ℓ_max 3000 versus 3500 | consistent; extra foreground bias small against difference variance | [src: Sect. V.3.3] |
| End-to-end Agora test, σ₈Ω_m^0.25 on 10 patches | mean z = −0.25 ± 0.32, χ² = 2.8/10 (patches not fully independent) | [src: Sect. VI.3.1] |
| Post-unblinding change | polarised-beam normalisation moved from ℓ = 800 to a physical small-scale normalisation, changing P_cal | [src: Sect. V.4] |

### Combined CMB analyses (SPT+ACT, CMB-SPA, ACT+SPT+Planck lensing)
<!-- key: combined-cmb-analyses-spt-act-cmb-spa-act-spt -->

From arXiv:2506.20707 unless a row names another paper:

| Item | What was done or found | Place |
|---|---|---|
| CMB-SPA composition | Planck PR3 Plik T&E + low-ℓ TT, Planck PR4 φφ, ACT DR6 (ACT-lite) with the P-ACT multipole cuts, SPT-3G D1 T&E + MUSE φφ; τ prior N(0.051, 0.006) | [src: arXiv:2506.20707, Sect. VII.1] |
| Correlations | SPT assumed uncorrelated with ACT and Planck (small overlap); Planck–ACT correlation reduced by the P-ACT cuts, not modelled | [src: Sect. VII.1] |
| SPT-3G D1 versus Planck, versus ACT DR6 (ΛCDM, five parameters) | 0.4σ and 1.1σ; without the amplitude A_s e^(−2τ): 0.4σ and 1.4σ | [src: Sect. VII.2.2] |
| Joint lensing likelihood | Gaussian in ACT DR6, Planck PR4 and SPT-3G MUSE band powers; ACT–Planck cross-covariance from 480 FFP10 simulations on the ACT footprint; ACT–SPT ≲ 15% and Planck–SPT ≲ 10% correlation | [src: arXiv:2504.20038, Sect. III, App. VII.1] |

### Large-scale polarisation and τ (Planck 2018 lowE, PR4 LoLLiPoP)
<!-- key: large-scale-polarisation-and-tau-planck-2018 -->

From arXiv:1807.06209 unless a row names another paper:

| Item | What was done or found | Place |
|---|---|---|
| lowE (SimAll) | 100×143 GHz QML cross-spectrum, ℓ = 2–29, maps cleaned with LFI 30 GHz and HFI 353 GHz templates; likelihood from 300 end-to-end simulations, off-diagonal correlations ignored | [src: arXiv:1807.06209, Sect. 2.2.3] |
| lowE alone | τ = 0.0506 ± 0.0086 (with low-ℓ TT, other parameters fixed); half a sigma below the 2016 HFI value 0.055 ± 0.009, driven by removing the last 1000 scanning rings, higher simulation variance and the 30 GHz tracer | [src: Eq. 2, Sect. 2.2.3] |
| Low-ℓ TE | excluded: excess variance at ℓ = 5 and ℓ = 18–19 not understood; TE to ℓ = 10 gives τ = 0.051 ± 0.015 | [src: Sect. 2.2.3] |
| LFI 70 GHz alternative | τ = 0.063 ± 0.020 | [src: Sect. 2.2.3] |
| SRoll2 EE likelihood (used by ACT DR6) | same SimAll-type construction on 100×143 EE, ℓ = 2–29, 500 signal maps per τ on a 101-point grid with 10⁹A_s e^(−2τ) = 1.875 fixed; τ = 0.0566 (+0.0053/−0.0062) on 50% of the sky; masks of 20–60% agree within 1σ (simulations: within 1.3σ); stable to ℓ_min = 5 | [src: arXiv:1908.09856, Sect. 4, Eqs. 2–3] |
| PR4 LoLLiPoP | Commander-cleaned detset cross-spectra, QML at N_side 16 on 50% of the sky, corrected by the PR4 transfer function; Hamimeche–Lewis variable change adapted to cross-spectra; covariance from PR4 simulations with Sellentin–Heavens marginalisation; foreground model fixed in the simulations, so foreground-model error is not included | [src: arXiv:2309.10034, Sects. 3.1, 4] |

### Planck PR4 HiLLiPoP V4.2 (Tristram et al. 2023, arXiv:2309.10034)
<!-- key: planck-pr4-hillipop-v4-2-tristram-et-al-2023 -->

From arXiv:2309.10034:

| Item | Prior or size | Place |
|---|---|---|
| Absolute calibration A_Planck | N(1.0000, 0.0025), from the orbital dipole | [src: Sect. 5.3, Table 7] |
| Five map inter-calibrations (143A fixed) | uniform [0.9, 1.1]; recovered 1.001–1.004 with σ 0.006–0.008 | [src: Sect. 8, Table 7] |
| Polarisation efficiencies | fixed at 1, 1, 0.975 (100, 143, 217 GHz); fitted values 0.972–1.016 at ±0.010–0.014, the 217 GHz maps about 2σ from unity; fixing costs Δχ² = 36 for 29 758 points and does not move ΛCDM or foreground parameters | [src: Sect. 8, Eqs. 29–34] |
| Beams and leakage | QuickPol window functions including leakage; beam uncertainty and sub-pixel effect neglected as small | [src: Sect. 5.3] |
| Dust | rescalings c_dust^T, c_dust^P with prior 1.0 ± 0.1 (fit 1.08 ± 0.03, 1.20 ± 0.03); indices β^T = 1.51 ± 0.01, β^P = 1.59 ± 0.02 (Gaussian) | [src: Table 7] |
| Extragalactic | radio, IR [0, 150]; CIB [0, 20]; tSZ, kSZ [0, 50] μK² at ℓ = 3000, 143 GHz; ξ ∈ [−1, 1]; β_CIB 1.75 ± 0.06; β_radio fixed −0.8 | [src: Table 7] |
| Galactic mask (baseline XXL masks 20%, 30%, 45% at 100, 143, 217 GHz) | masking 5% or 10% more changes χ² by < 100 for 29 758 points | [src: Sect. 9] |
| PR4 versus PR3 (TT,TE,EE) | Ω_c h² −1.0σ, n_s +0.75σ, H₀ +0.6σ, S₈ −0.9σ; errors 10–20% smaller; CamSpec PR4 agrees within 1σ | [src: Sect. 9, Table 4] |

---

## What a referee checks in a CMB results section
<!-- key: what-a-referee-checks-in-a-cmb-results-section -->

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
<!-- key: not-verified -->

- The NPIPE low-ℓ polarisation transfer function: LoLLiPoP corrects for
  it (Sect. 15 of this file) [src: arXiv:2309.10034, Sect. 3.1]; its size was not
  read.
- The ACT DR6 beam paper was not read; ACT beam statements come from the
  power-spectrum paper. The SPT-3G D1 beam treatment (nine eigenmodes from
  AGN and Saturn observations) was read in arXiv:2506.20707, Sect. V.2.1;
  the dedicated beam paper was not.
- Atmospheric-noise characterisation at the South Pole (a 2026 BICEP/Keck
  paper exists) was not read.
- Bandpass uncertainties: closed, priors now in Sect. 15 of this file (ACT DR6). The
  impact of the bandpass shifts on cosmological parameters alone was not
  found stated separately.
