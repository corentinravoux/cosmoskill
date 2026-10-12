# Systematics — reionisation, 21 cm, line-intensity mapping

Scope: the canonical systematics, their size, mitigation and validation.
Snapshot: 2026-10-07

Each subsection gives the mechanism, the size where a paper quantifies it, the standard
mitigation, the validation test, and the paper a referee expects. Numbers carry [src], [sec] or
[der].

## 1. Optical depth from the CMB
<!-- key: optical-depth-from-the-cmb -->

**Large-scale polarisation systematics.** The Planck HFI low-ℓ maps carried residual large-scale
contamination, dominated at the lowest multipoles by a "dipole distortion" effect that the 2018
legacy release characterised but did not fully remove; the SRoll2 map-making brings it below the
noise and shrinks the τ uncertainty by ~40% [src: Pagano et al. 2019, arXiv:1908.09856]. The
first HFI-based τ came with new end-to-end simulations and a cross-check against LFI [src:
Planck Collaboration 2016, arXiv:1605.02985]. Validation: consistency between detector-set and
frequency combinations and between three likelihood constructions [src: de Belsunce et al. 2021,
arXiv:2103.14378].

**Single point of failure.** ACT, SPT and WMAP + ACT analyses all adopt the Planck τ, so an
undetected systematic there propagates to every CMB-based amplitude, neutrino-mass and
dark-energy result; Sailer et al. state that there is "no evidence for systematics in the
large-scale Planck data" [src: Sailer et al. 2025, arXiv:2504.16932].

**Model dependence.** τ inferred from EE depends on the assumed shape of x_e(z) and on how the
low-ℓ temperature deficit is treated: marginalising over inflationary-feature templates moves
the Planck 95% upper limit from 0.0696 to 0.075 [src: Jhaveri, Hu & Miranda 2026,
arXiv:2606.20795]; allowing a high-redshift flash moves the mean by 0.002 [src: Upadhyay et al.
2026, arXiv:2609.24989]. A claim that the monotonic-history assumption acts as a hidden prior on
σ₈ and Σm_ν is in arXiv:2606.27903.

Referee expects: the low-ℓ data named (Planck 2018 legacy, SRoll2, PR4), the reionisation
parametrisation, and whether τ is measured or imposed as a prior.

## 2. End of reionisation from quasar absorption
<!-- key: end-of-reionisation-from-quasar-absorption -->

**Definition dependence of dark statistics.** Dark-pixel limits depend on the binning scale and
on the definition of "dark" [src: Davies et al. 2025, arXiv:2510.25829]. Dark-gap statistics
depend on the flux threshold and bin (5% over 1 h⁻¹Mpc in arXiv:2109.06295). Mitigation: fixed,
pre-stated definitions and a second, model-dependent estimate; the 2025 dark-pixel paper finds
the two similar [src: arXiv:2510.25829].

**Two physical explanations for one statistic.** The τ_eff scatter is fitted both by residual
neutral islands and by ionising-background fluctuations with a short mean free path [src: Davies
et al. 2023, arXiv:2312.08464; Zhu et al. 2021, arXiv:2109.06295]. Lyβ dark gaps alone are
"broadly consistent" with both [src: Zhu et al. 2022, arXiv:2205.04569]. The discriminating test
is the damping wing next to troughs [src: Spina et al. 2024, arXiv:2405.12273; Zhu et al. 2024,
arXiv:2405.12275].

**Error budget of forward-modelled quantities.** The quoted errors on the mean free path,
photo-ionisation rate and neutral fraction include thermal-parameter, modelling, observational
and cosmic-variance terms [src: Gaikwad et al. 2023, arXiv:2304.02038]. Recovery tests on
simulated data return the inputs within 1σ [src: arXiv:2304.02038].

**Mean free path, direct method.** Possible biases are the overdense quasar environment,
incomplete reionisation and the proximity zone. A dedicated study with radiative-transfer
simulations finds the environment bias "minimal at z ∼ 6" and the patchiness effect not
significant, and recovers 1.49 (+0.47/−0.52) pMpc at z = 6 against 0.81 (+0.73/−0.48) pMpc at z
= 5.93 from the stack [src: Satyavolu et al. 2023, arXiv:2311.06344; Zhu et al. 2023,
arXiv:2308.04614]. Definitions of the mean free path in simulations before the end of
reionisation differ and must be matched to the measurement [src: arXiv:2311.06344].

**Simulation resolution.** The mean free path is set by kiloparsec-scale clumping that
large-volume reionisation simulations do not resolve; an emulator trained on 2 h⁻¹Mpc boxes is
one remedy [src: Tohfa et al. 2026, arXiv:2602.03923]. The imprint of reionisation on the
post-reionisation forest at z < 5 is a `cosmo-lyman-alpha` topic.

## 3. Damping wings
<!-- key: damping-wings -->

**Quasars.** Error sources: the stochastic distribution of neutral patches, the effect of the
quasar's own ionising radiation (lifetime), the unknown intrinsic spectrum, and spectral noise
[src: Hennawi et al. 2024, arXiv:2406.12070]. Size: for single objects the posterior on ⟨x_HI⟩
is ±0.2–0.26 wide even after marginalising the lifetime over 10³–10⁸ yr [src: Davies et al.
2018, arXiv:1802.06066]. Sample selection matters: 23 of the 42 XQR-30 quasars survive quality
control [src: Greig et al. 2024, arXiv:2404.12585]. Validation: coverage of the credible
contours on 100 mock spectra [src: arXiv:2406.12070].

**Galaxies.** A local damped Lyα absorber and the IGM wing are degenerate at prism resolution.
Tests with low-redshift spectra degraded to JWST quality recover the absorber column density
with an rms error of order 1 dex at R ~ 100; x_HI is "poorly constrained" and does not improve
substantially at R ~ 1000; column densities are underestimated when Lyα emission is present
[src: Huberty et al. 2025, arXiv:2501.13899]. Mitigation in the measurements: templates from z ~
2–5 galaxies that include galactic and circumgalactic absorption and Lyα emission, and stacks
matched in UV magnitude and slope [src: Umeda et al. 2025, arXiv:2504.04683]. The resulting x_HI
intervals are wide (for example 0.65 +0.27/−0.35 at z ~ 7).

**Topology prior.** All x_HI values assume an inside-out topology from a simulation. Bubble
radii inferred from galaxies exceed analytic cosmic-average expectations by up to a few dex
[src: Umeda et al. 2023, arXiv:2306.00487].

## 4. Lyα visibility
<!-- key: lyalpha-visibility -->

- Intrinsic line properties. The z ~ 5–6 lines are broader and more offset (median 258 km/s)
  than the z ~ 2 templates used before JWST, which raises the predicted transmission through
  neutral gas and lowers inferred neutral fractions [src: Prieto-Lyon et al. 2025,
  arXiv:2509.18302].
- Environment. In the DIVER sample strong emitters lie farther from overdensities; near the z ~
  5.2 GOODS-N overdensity fewer than 15% of galaxies show strong Lyα. This is opposite to the
  simplest inside-out expectation and points to circumgalactic or local opacity [src: Zhu et al.
  2026, arXiv:2608.19311].
- Field-to-field variance. Four PASSAGE pointings contain {3, 1, 0, 0} emitters [src: Runnholm
  et al. 2025, arXiv:2502.19174].
- Threshold dependence. The same data give different ⟨x_HI⟩ for EW > 25 Å and EW > 10 Å (0.38
  against 0.52 at z ~ 7) [src: Kundu et al. 2026, arXiv:2609.40363].

## 5. Kinetic SZ
<!-- key: kinetic-sz -->

- Component separation. The inferred SZ powers "are dependent on the detailed modeling of the
  thermal SZ–CIB correlation, and to a lesser extent on the assumed angular dependence of the SZ
  spectra" [src: Chaubal et al. 2026, arXiv:2601.20551].
- Late-time kSZ. Duration limits assume a level of homogeneous kSZ; the ACT limit Δz < 4.4 is
  the conservative case of a minimal low-redshift contribution, and other assumptions tighten it
  [src: Beringue et al. 2025, arXiv:2506.06274].
- Simulation dependence. SPT-3G quotes two limits from two models (semi-analytic and AMBER) with
  two duration definitions [src: arXiv:2601.20551].
- Trispectrum. The measured four-point signal is dominated by lensing and foregrounds, estimated
  with the Agora simulations [src: Raghunathan et al. 2024, arXiv:2403.02337].

## 6. 21 cm interferometry at z > 6
<!-- key: 21-cm-interferometry-at-z-6 -->

**Signal loss.** Foreground suppression can remove cosmological signal and produce upper limits
that are too low. Two documented cases: GMRT, where a sliding spectral average subtracted from
the data overlapped the modes used for the limit; and PAPER-64, where inverse-covariance
weighting with a covariance estimated from few independent time samples (made worse by
fringe-rate filtering) biased the power low [sec: Liu & Shaw 2019, arXiv:1907.08211, section
12.5; src: Cheng et al. 2018, arXiv:1810.05175]. Because cleaned data are not a linear function
of the input, simulating the signal alone through the pipeline is not sufficient; injection into
real data is used but is hard to interpret [sec: arXiv:1907.08211, section 12.5]. Mitigation:
estimators with minimal inherent loss and an explicit loss budget (HERA, arXiv:2108.02263),
signal-injection tests (LOFAR, arXiv:2503.05576), a bias correction where suppression is found
(LOFAR 3C196, arXiv:2504.18534).

**Calibration against an incomplete sky model.** End-to-end simulations show that sky-based,
per-frequency antenna calibration contaminates otherwise clean power-spectrum modes for
realistic catalogue completeness; the requirement is a joint one on catalogue precision and on
the spectral smoothness of the antennas [src: Barry et al. 2016, arXiv:1603.00607].

**Instrument chromaticity: reflections, cross-coupling, mutual coupling.** HERA Phase I shows
systematics attributed to RFI, cable sub-reflections or cross-coupling, suppressed to a dynamic
range of ~10⁹ relative to the peak foreground power [src: HERA Collaboration 2021,
arXiv:2108.02263]. In Phase II mutual coupling is the dominant systematic and removes the modes
k = 0.35–0.55 [src: HERA Collaboration 2025, arXiv:2511.21289].

**Excess variance.** LOFAR limits sit above thermal noise; the 2025 reprocessing attributes the
remainder to distant-source residuals, beam-model errors and low-level RFI [src: Mertens et al.
2025, arXiv:2503.05576]. NenuFAR reduced its excess variance 50-fold by changing field and
pipeline, and finds it largely incoherent between nights at z = 20.3, so it should integrate
down [src: Munshi et al. 2025, arXiv:2507.10533]. The 3C196 field shows an excess of different
behaviour from the NCP, suggesting residual foregrounds [src: Ceccotti et al. 2025,
arXiv:2504.18534].

**Non-Gaussian leakage.** Foreground leakage makes the distribution of power estimates
non-Gaussian; fitting only the Gaussian component tightens the MWA limit at z = 6.5 from (30.2
mK)² to (23.0 mK)² [src: Trott et al. 2025, arXiv:2508.04164]. A referee will ask how the
Gaussian component is isolated without removing signal.

**Wedge leakage.** Section 5.1 of `physics-and-methods.md`.

## 7. Global 21 cm signal
<!-- key: global-21-cm-signal -->

- Foreground-model degeneracy. The EDGES polynomial foreground fit implies unphysical foreground
  parameters, and other signal shapes fit the same data [src: Hills et al. 2018,
  arXiv:1805.01421].
- Instrumental structure. A ground-plane resonance model fits the public spectrum with a smaller
  rms residual (20.8 mK) than the EDGES model (24.5 mK); the public EDGES spectrum had no noise
  level, so standard goodness-of-fit statistics could not be computed [src: Bradley et al. 2018,
  arXiv:1810.09015].
- Calibration and noise model. Data models with a detailed noise model and calibration-error
  terms are decisively preferred, and then the evidence for a signal is not strong [src: Sims &
  Pober 2019, arXiv:1910.03165].
- Beam chromaticity. The beam couples spatial foreground structure into the spectrum; EDGES
  corrects with beam factors, and the corresponding data model is validated on simulations [src:
  Sims et al. 2025, arXiv:2506.20042].
- Validation standard: an independent instrument. SARAS 3 is the only one so far [src: Singh et
  al. 2021, arXiv:2112.06778].

## 8. Post-reionisation HI intensity mapping
<!-- key: post-reionisation-hi-intensity-mapping -->

**Signal loss in blind foreground cleaning.** Aggressive cleaning biases the largest scales by
more than 50%; a transfer function built by injecting mock signal into the data reconstructs the
power to sub-percent accuracy in simulations, and mocks wrong by up to ±100% in fiducial
parameters bias recovered values by less than 5% [src: Cunnington et al. 2023,
arXiv:2302.07034]. The 2026 MeerKLASS auto-spectrum marginalises the loss in the fit [src:
MeerKLASS Collaboration 2026, arXiv:2610.12158].

**Additive systematics in auto-correlation.** MeerKLASS subset auto-spectra show excess power
from unresolved systematics; the detection rests on cross-spectra between observationally
independent subsets (split by scan and by dish), which pass the null and robustness tests [src:
arXiv:2610.12158; arXiv:2606.25955, section 3]. CHIME needed new RFI masking, achromatic
beamforming and filtering before time averaging to reach an auto-detection [src: CHIME
Collaboration 2025, arXiv:2511.19620].

**Foreground residuals in cross-correlation.** They do not bias a cross-correlation but inflate
its variance: in CHIME × Lyα the residuals are ~6–10 times the thermal noise in the correlation
function [src: CHIME Collaboration 2023, arXiv:2309.04404].

**Primary-beam structure.** The MeerKLASS stacked spectrum carries an oscillation at the
frequency of the MeerKAT primary-beam ripple, fitted at 17.90 (+6.53/−4.27) MHz, and its
amplitude is degenerate with the HI density, which biases the inferred HI mass low [src:
Cunnington et al. 2026, arXiv:2606.25955, section 3]. For HIRAX, feed-placement precision is the
item not yet within requirement [src: Studer et al. 2026, arXiv:2607.26972].

**Astrophysical degeneracies.** Ω_HI, b_HI and r are not separated by one amplitude. CHIME's
stacking amplitude is limited by modelling at non-linear scales and is sensitive to the redshift
bias of the optical tracer (Δv = −66 ± 20 km/s for eBOSS quasars) [src: CHIME Collaboration
2022, arXiv:2202.01242]. The stacked signal in a single-dish map is broadened by clustering and
by the beam, and needs forward modelling [src: arXiv:2606.25955, section 3].

## 9. Line-intensity mapping
<!-- key: line-intensity-mapping -->

- Filtering and transfer functions. Time-domain filtering that removes atmospheric 1/f noise
  also removes large-scale signal: the CCAT filter-and-bin transfer function is below 20% at k ≲
  0.1 Mpc⁻¹ [src: Dev et al. 2026, arXiv:2607.20404].
- Instrument systematics in the power spectrum. COMAP moved from feed–feed to feed-group
  cross-spectra for robustness and reports 312 difference-map null tests consistent with noise
  [src: Stutzer et al. 2024, arXiv:2406.07511].
- Stacking attenuation. Redshift (velocity) uncertainty of the catalogue, pipeline signal loss,
  cosmic variance and interloper emission all enter the COMAP quasar stack interpretation [src:
  Dunne et al. 2025, arXiv:2510.23568].
- Model uncertainty. Shot noise is uncertain by factors of 2–5 through star-formation burstiness
  [src: Kovetz et al. 2026, arXiv:2605.13967].

## 10. JWST abundances and the photon budget
<!-- key: jwst-abundances-and-the-photon-budget -->

- Candidate against confirmed. The baryon-budget argument was made with photometric candidates
  [src: Boylan-Kolchin 2022, arXiv:2208.01611]. Later work attributes the early excess stellar
  masses to AGN contamination, dust attenuation and missing mid-infrared constraints [src: Prada
  et al. 2026, arXiv:2604.18683].
- Small fields. The z ~ 14–15 number density rests on ~350 arcmin² and carries an uncertainty of
  a factor of several (182 +329/−105 times the model) [src: Naidu et al. 2025,
  arXiv:2505.11263].
- Sample selection in ξ_ion. A stellar-mass-complete sample gives a significantly milder
  evolution of ξ_ion with redshift and UV magnitude than previously reported [src: Simmonds et
  al. 2024, arXiv:2409.01286].
- Escape fraction. It is never measured directly at z > 6; every budget relies on low-redshift
  calibrations or spectral modelling [src: Giovinazzo et al. 2026, arXiv:2607.22834; Muñoz et
  al. 2024, arXiv:2404.07250].

## Referee checklist
<!-- key: referee-checklist -->

1. τ: which low-ℓ likelihood; which reionisation parametrisation; measured or prior.
2. x_HI values: volume- or mass-weighted; which topology simulation; upper limit, lower limit or
   measurement; 1σ or 2σ.
3. Dark pixels and gaps: binning scale and flux threshold stated.
4. Damping wings: continuum model, lifetime prior, local-absorber treatment, spectral
   resolution.
5. Mean free path: proper or comoving units; proximity-zone correction; definition in the
   comparison simulation.
6. kSZ duration: definition of Δz; late-time template; tSZ–CIB model.
7. 21 cm limits: confidence level, k and z of the quoted bin, integration time, signal-loss
   test, thermal-noise comparison, calibration strategy.
8. 21 cm limits: no ranking of experiments across different k without a model.
9. Global signal: foreground model order, beam correction, calibration terms in the data model,
   independent confirmation.
10. HI intensity mapping: cross, stack or auto; which parameter combination; transfer-function
    construction; null tests between independent subsets.
11. LIM: transfer function, interloper treatment, null tests, model used to turn a limit into a
    statement about galaxies.
12. JWST abundance claims: spectroscopic or photometric; survey area; comparison made to the
    halo baryon limit or to a galaxy-formation model.

## Not verified
<!-- key: not-verified -->

- Ionospheric effects, polarisation leakage and RFI excision have dedicated sections in
  arXiv:1907.08211 that were not read; no size is quoted here.
- The systematics budget of the XQR-30 flux measurements (continuum reconstruction, zero-level,
  sky subtraction) was not read in the body of any paper.
- The original PAPER-64 limit before retraction and the size of its signal loss were not read.
- The HERA mutual-coupling model and its validation were not read beyond the abstract.
