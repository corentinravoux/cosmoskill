# Systematics — reionisation, 21 cm, line-intensity mapping

Scope: the canonical systematics, their size, mitigation and validation.
Snapshot: 2026-10-13

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

**Sizes read in the paper bodies.**

- Mechanism and residual level. The 2018 maps corrected the analogue-to-digital-converter
  non-linearity to first order (128 gain steps); the second-order effect on large signals
  leaks the temperature dipole into polarisation, at ~1 μK in the maps. SRoll2 brings the
  residual EE spectra below 2 × 10⁻² μK² at 100 and 143 GHz, "gaining an order of magnitude",
  and below 3 × 10⁻³ μK² in the 100 × 143 cross-spectrum [src: arXiv:1908.09856, Sect. 2].
- Stability of the SRoll2 value. Sky fractions of 20–60% give τ within 1σ; raising the lower
  multipole cut to ℓ_min = 5 gives no shift; removing ℓ = 5 alone moves τ by about half a σ (a
  1.2σ fluctuation in simulations); the synchrotron tracer (WMAP K, Ka or LFI 30 GHz) and the
  dust tracer (217 or 353 GHz) do not move it; low-ℓ TE alone gives 0.057 (+0.012/−0.013),
  with null-test probabilities that remain poor [src: arXiv:1908.09856, Sect. 4].

| Likelihood and data | τ (68%) | Place read |
|---|---|---|
| Planck 2018 lowE (EE, ℓ ≤ 29) alone | 0.0506 ± 0.0086 | arXiv:1807.06209, Eq. 2 |
| Planck 2018 low-ℓ TE to ℓ_max = 10 | 0.051 ± 0.015 | arXiv:1807.06209, Sect. 2.2.3 |
| Planck 2018 LFI polarisation likelihood | 0.063 ± 0.020 | arXiv:1807.06209, Sect. 2.2.3 |
| Planck 2018 TT,TE,EE + lowE | 0.0544 (+0.0070/−0.0081) | arXiv:1807.06209, Eq. 15 |
| lowE, flat prior on τ, tanh | 0.0519 (+0.0030/−0.0079) | arXiv:1807.06209, Eq. 84a |
| lowE, flat prior on τ, FlexKnot | 0.0504 (+0.0050/−0.0079) | arXiv:1807.06209, Eq. 84b |
| SRoll2 EE alone | 0.0566 (+0.0053/−0.0062) | arXiv:1908.09856, Eq. 3 |
| SRoll2 EE + Commander low-ℓ TT (A_s and τ only) | 0.0579 (+0.0056/−0.0067) | arXiv:1908.09856, Eq. 5 |
| SRoll2 EE + TT | 0.0575 (+0.0056/−0.0069) | arXiv:1908.09856, Eq. 6 |
| SRoll2 EE + TT,TE,EE | 0.0591 (+0.0054/−0.0068) | arXiv:1908.09856, Eq. 7 |
| the same + lensing + BAO | 0.0599 (+0.0054/−0.0064); z_re = 8.21 ± 0.58 | arXiv:1908.09856, Eqs. 8–9 |
| Planck 2018 maps, 100 × 143, EE: C-SimLow / momento / pydelfi | 0.0530 ± 0.0071 / 0.0507 ± 0.0063 / 0.0517 ± 0.0070 | arXiv:2103.14378, Table 3 |
| SRoll2 maps, 100 × 143, EE: C-SimLow / momento / pydelfi | 0.0582 ± 0.0057 / 0.0581 ± 0.0055 / 0.0588 ± 0.0054 | arXiv:2103.14378, Table 3 |
| SRoll2, momento, low-ℓ TTTEEE | 0.0604 ± 0.0052 | arXiv:2103.14378, Table 3 |
| SRoll2, momento EE, 100 ds1 × 100 ds2 / 143 ds1 × 143 ds2 | 0.0638 ± 0.0072 / 0.0676 ± 0.0068 | arXiv:2103.14378, Table 4 |

Reading. Three likelihood constructions agree to 0.0007 on the SRoll2 maps and 0.0023 on the
2018 maps, and the map-making change moves τ by +0.005 to +0.007 in each [der: Table 3
rows]. Same-frequency detector-set spectra give τ higher than 100 × 143 by 1.4–2σ (143 × 143)
and less (100 × 100), "suggestive of correlated residual systematics" that partly cancel
between frequencies; the net effect on 100 × 143 is "probably at the level of a standard
deviation or less", which "depends on the fidelity of the noise and systematics simulations";
synchrotron cleaning lowers the 100 × 100 value by about 1σ [src: de Belsunce et al. 2021,
arXiv:2103.14378, Sect. 6.2 and Table 4]. On the same maps τ rises by about 0.003, half a σ,
from EE alone to the full combination [der], because high-ℓ lensing smoothing breaks the A_s
e^(−2τ) degeneracy and pulls A_s upward [src: arXiv:1908.09856, Sect. 5]. A free-form history
moves the centre by 0.0015 relative to tanh [der]. The contribution of 15 < z < 30 is τ(15,30)
< 0.018 (flat prior on it) or < 0.023 (flat prior on knots) at 95%, the values of a
corrigendum, about three times those first published [src: arXiv:1807.06209, Eqs. 85a–85b and
footnote]. Earlier disagreements between reionisation-history analyses came from different,
sometimes implicit, priors on τ [src: arXiv:1807.06209, Sect. 7.8].

Referee expects: the low-ℓ data named (Planck 2018 legacy, SRoll2, PR4), the reionisation
parametrisation, and whether τ is measured or imposed as a prior. The PR4 likelihood paper
(LoLLiPoP low-ℓ with HiLLiPoP high-ℓ) is Tristram et al. 2024, arXiv:2309.10034; its τ is not
in the abstract and is tabulated in `cosmo-cmb`.

## 2. End of reionisation from quasar absorption
<!-- key: end-of-reionisation-from-quasar-absorption -->

**Continuum reconstruction.** τ_eff = −ln⟨F/F_cont⟩ needs the unabsorbed continuum under an
almost fully absorbed forest. For XQR-30, tested on 4597 eBOSS quasars: the red-side PCA
predicts it to 0.8 (+7.8/−7.9)%, against > 13% for power-law extrapolation and 9% for the best
earlier PCA; with the shorter Keck/ESI coverage, 1.0 (+11.2/−11.3)%, about 50% larger, without
bias [src: Bosman et al. 2022, arXiv:2108.03699, Sects. 2.3 and 3.2]. A fractional continuum
error ε shifts τ_eff by ≈ ε [der: δτ_eff = δF_cont/F_cont]: 0.08 per segment, against mean
τ_eff of 2.1 at z = 5.2 and 4.7 at z = 6.0 [der: −ln of the Table 4 transmissions]. The method
matters more than its scatter: an earlier disagreement between two mean-opacity measurements
is "explained almost entirely" by power-law against linear-PCA continua, whose
wavelength-dependent biases cannot be corrected afterwards [src: arXiv:2108.03699, Sect.
4.1]. Other terms: X-Shooter and ESI spectra of six quasars differ by 1.3% with 2.3% scatter;
bootstrap (sightline-variance) errors are 5–10 times the measurement errors; damped absorbers
suppress Lyα over ≳ 5000 km/s and are removed through their metal lines [src:
arXiv:2108.03699, Sects. 3.3–3.4 and Table 4].

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
reionisation differ and must be matched to the measurement [src: arXiv:2311.06344]. Budget
of the stack: the bootstrap term is comparable to the total error at all redshifts; the
exponent ξ of the opacity–ionisation-rate relation moves the z = 5.93 value from 1.53 (ξ =
0.33) through 0.81 (0.67, nominal) to 0.30 pMpc (1.00), but the z = 5.08 value only from
10.10 to 8.74; the background ionisation rate alone contributes +0.21/−0.26 at z = 5.93 [src:
arXiv:2308.04614, Table 2 and Sect. IV.2]. Without the proximity model the z = 6 value is
too high "by a factor of two or more" [src: Becker et al. 2021, arXiv:2103.16610].

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

Share of the continuum in the error budget. On 1000 mock spectra the median 1σ precision on
⟨x_HI⟩ is ~15% with a perfectly known continuum and ~28% with the continuum modelled and
marginalised (~0.55 and ~0.80 dex on the lifetime): the continuum contributes about as much
as the intrinsic stochasticity of neutral patches and ionisation fronts. That analysis models
the whole spectrum, proximity zone included, and corrects its posteriors for coverage, which
earlier pipelines did not test [src: Hennawi et al. 2024, arXiv:2406.12070, Sect. 5.7,
quoting its companion paper]. The first PCA predictor reaches 6–12% precision with ≲ 1% bias
on its training set [src: Davies et al. 2018, arXiv:1801.07679]. The covariance-matrix method
of the XQR-30 analysis underestimated the Lyα + N V profile by ~10% between 1215 and 1230 Å,
inside the window (1218–1230 Å) where the wing is fitted, for X-Shooter and BOSS spectra
alike; the bias was measured on two samples of 30 unabsorbed quasars at 3.5 < z < 4.5 and
calibrated out [src: arXiv:2404.12585, Sects. 3.3–3.4]. Dense absorbers near the quasar "can
imitate" the IGM wing [src: arXiv:2404.12585, Sect. 2.2], the caveat of Miralda-Escudé 1998,
arXiv:astro-ph/9708253.

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
- Sizes in SPT-3G D1, read in the HTML rendering of the first arXiv version, whose headline
  values (D_3000^kSZ = 1.98 ± 0.87 μK², Δ⁵⁰z < 4.2, Δ⁹⁰z < 7.0) differ from the current
  abstract (1.75 ± 0.86 μK², < 3.8, < 6.1): they show the model dependence, not final values.
  (i) Templates: with free CIB and tSZ–CIB shapes but fixed SZ templates, D_3000^kSZ = 1.74 ±
  0.64 or 2.89 ± 0.87 μK² for two template sets; SZ shapes scaled as ℓ^α bring them within
  0.5σ. More tSZ–CIB correlation means less tSZ and more kSZ power. (ii) Late-time
  subtraction: patchy = total − 1.65 (σ₈/0.8)^4.46 μK², that is 1.76 μK² at σ₈ = 0.812 or 1.35
  μK² at 0.77, a ~25% change that lengthens the duration limit by ~1. (iii) Conversion:
  D_3000^p-kSZ = 2.03 [(1 + z_re)/11 − 0.12] (Δ⁵⁰z/1.05)^0.51 μK² (semi-analytic) or 1.75
  (z_re/8.0)^1.4 (Δ⁹⁰z/4.0)^0.75 μK² (AMBER), with z_re fixed to 7.68 and a uniform prior on
  the duration; the two "are not directly comparable". The Agora template fit gives only
  Δ⁵⁰z < 11 [src: Chaubal et al. 2026, arXiv:2601.20551, Sects. 7, 8.1.1 and 8.1.4, Eqs.
  18–20]. The first SPT limit already moved from ≤ 2.1 to ≤ 4.9 μK² (95%), and Δz from ≤ 4.4
  to ≤ 7.9, when the tSZ–CIB correlation was freed [src: Zahn et al. 2012, arXiv:1111.6386].
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

| Pipeline | Step that can remove or bias signal | Size | How measured | Place read |
|---|---|---|---|---|
| PAPER-64 (2015) | empirical inverse-covariance weighting with fringe-rate filtering | loss "previously found to be < 2%" was "underestimated by a factor of > 1000"; bootstrap errors too small by ~2 in mK | injection into data; a signal-only simulation misses the data–signal correlation, "which can be large and negative" | arXiv:1810.05175, Sect. V |
| HERA 2021, Band 1 (Band 2) | absolute calibration bias; cross-coupling filter; LST averaging; redundant averaging | 9% (8%); 3% (1%); 1% (1%); 1% (1%) of power | validation simulations and data | arXiv:2108.02263, Table 2 |
| HERA 2022, z = 10.4 / 7.9 | absolute calibration; crosstalk subtraction; coherent time averaging; redundant-baseline averaging; total | ≲ 0% / ≲ 0%; 2.4% / 3.3%; 1.2% / 1.5%; 1.9% / 2.4%; 5.5% / 7.2% | noise-free simulations of a known signal; non-redundancy from the data | arXiv:2210.04912, Table 2 |
| LOFAR 2025 | Gaussian-process foreground removal | injected power recovered more than 2σ low in 1, 0 and 4 of 100 cases at z ≈ 8.3, 9.1, 10.1 (GRIZZLY-like signals); 4, 1 and 11 for 21cmFAST signals, outside the kernel's training set | 25 spectrum shapes at 0.25, 0.5, 1 and 2 times the noise power, injected just before the regression | arXiv:2503.05576, Sect. 5.3 |
| LOFAR 2025 | flux scale | one calibrator known to 5% | — | arXiv:2503.05576, Sect. 5.1 |

All rows [src]. The withdrawn PAPER-64 limit was (22.4 mK)² at z = 8.4 [src: Ali et al. 2015,
arXiv:1502.06016] against (200 mK)² at z = 8.37 in the re-analysis, a factor ~80 in power
[der: (200/22.4)²]. The HERA corrections are flat in k and independent of the signal model.
The 9% bias came from a logarithmic linearisation of gain amplitudes on low signal-to-noise
visibilities and was found during pipeline validation; in 2022 it is below 1% in the gains,
of opposite sign, and left uncorrected as the conservative choice [src: arXiv:2108.02263,
Sect. III.11; arXiv:2210.04912, Sect. III.3.6]. The LOFAR worst cases have a flat spectrum or
a large-scale upturn, close in frequency coherence to the mode-mixing component.

**Calibration against an incomplete sky model.** End-to-end simulations show that sky-based,
per-frequency antenna calibration contaminates otherwise clean power-spectrum modes for
realistic catalogue completeness; the requirement is a joint one on catalogue precision and on
the spectral smoothness of the antennas [src: Barry et al. 2016, arXiv:1603.00607].

**Instrument chromaticity: reflections, cross-coupling, mutual coupling.** HERA Phase I shows
systematics attributed to RFI, cable sub-reflections or cross-coupling, suppressed to a dynamic
range of ~10⁹ relative to the peak foreground power [src: HERA Collaboration 2021,
arXiv:2108.02263]. The dynamic range is 10⁹ in power relative to the
peak foreground emission; the data are noise limited for k ≥ 0.5 h Mpc⁻¹ and show residual
systematics below [src: arXiv:2108.02263, Sects. I and VI]. Crosstalk is modelled as
autocorrelation power leaking into cross-correlations and removed only inside |f_max| = 0.024
mHz (|b_E-W|/1 m) − 0.28 mHz of zero fringe rate, so as not to remove sky signal [src:
arXiv:2210.04912, Sect. III.1, Eq. 3]. In Phase II mutual coupling, "the reflection or
re-emission of sky signal by one antenna into another", is the dominant systematic and
removes the modes k = 0.35–0.55 [src: HERA Collaboration 2025, arXiv:2511.21289]. It is
stronger than in Phase I because the Vivaldi feeds are more sensitive towards the horizon
and hang above the dish without the cage of the Phase I dipoles; cable reflections were
pushed beyond ≳ 2700 ns by fibre links. It is modelled as delayed, down-weighted copies of
the other baselines sharing an antenna, gives an "X" pattern in fringe-rate–delay space that
is filtered in the time domain, and inpainting and flagging models reserve 500–750 ns in
delay for it. Foregrounds outshine the signal "by up to four orders of magnitude" [src:
arXiv:2511.21289, Sects. I, III.6, III.8.4 and III.9.1].

**Excess variance.** LOFAR limits sit above thermal noise; the 2025 reprocessing attributes the
remainder to distant-source residuals, beam-model errors and low-level RFI [src: Mertens et al.
2025, arXiv:2503.05576]. In detail: Cas A and Cygnus A in the far sidelobes, where deep nulls
and beam-model errors defeat a spectrally smooth direction-dependent calibration; calibrating
source clusters beyond the first null, which "may in some circumstances do more harm than
good"; and broadband low-level RFI at high k_∥; direction-independent calibration errors are
no longer thought significant [src: arXiv:2503.05576, Sect. 6.2]. In the 2020 analysis the
excess had a spectral coherence of 0.25–0.45 MHz and was partially correlated between nights
[src: Mertens et al. 2020, arXiv:2002.07196]. NenuFAR reduced its excess variance 50-fold by changing field and
pipeline, and finds it largely incoherent between nights at z = 20.3, so it should integrate
down [src: Munshi et al. 2025, arXiv:2507.10533]. The 3C196 field shows an excess of different
behaviour from the NCP, suggesting residual foregrounds [src: Ceccotti et al. 2025,
arXiv:2504.18534].

**Non-Gaussian leakage.** Foreground leakage makes the distribution of power estimates
non-Gaussian; fitting only the Gaussian component tightens the MWA limit at z = 6.5 from (30.2
mK)² to (23.0 mK)² [src: Trott et al. 2025, arXiv:2508.04164]. A referee will ask how the
Gaussian component is isolated without removing signal.

**Ionosphere and polarisation leakage.** The ionosphere absorbs (smoothly, hence benign),
refracts source positions, scintillates and Faraday-rotates polarised emission. The rotation
angle scales as λ², so polarised foregrounds acquire a rapidly oscillating spectrum, and
where the instrument leaks polarisation into Stokes I the result is a spectrally unsmooth
foreground. Refraction is handled in direction-dependent calibration on catalogued sources
[sec: Liu & Shaw 2019, arXiv:1907.08211, sections VI.3 and XII.3]. MWA corrects offsets for
the 1,000 brightest sources only and selects data with an ionospheric-activity metric [src:
arXiv:2505.09097, Sect. III.3; Trott et al. 2020, arXiv:2002.02575]. No size is quoted here.

**Wedge leakage.** Section 5.1 of `physics-and-methods.md`. A buffer beyond the horizon is
always added: HERA moved it from 200 ns to 300 ns between its two analyses (section 5.4
there).

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
- Why it is hard in principle. One antenna gives one spectrum, with few degrees of freedom to
  separate signal from foregrounds; a slow reionisation step is as smooth as the foregrounds,
  so experiments at reionisation frequencies can only exclude rapid transitions and most now
  target the non-monotonic Cosmic Dawn trough. Thermal noise is not the limit: with ~1 MHz
  channels it falls below the signal in less than a day [sec: arXiv:1907.08211, section XV.2].
- Dynamic range. A signal of ~10 mK against Galactic synchrotron above 100 K [src: Bowman &
  Rogers 2010, arXiv:1209.1117]; the 50–100 MHz band constrains the first stars only if
  "systematic temperature residuals can be controlled to less than 1 mK" and the foregrounds
  follow low-order polynomials [src: Pritchard & Loeb 2010, arXiv:1005.4057].
- Beam factor, as defined. Each of 72 sidereal-time spectra is divided by G_beam(ν) = ∫ T_sky(Ω,
  ν_ref) B(Ω, ν) dΩ / ∫ T_sky(Ω, ν_ref) B(Ω, ν_ref) dΩ, with ν_ref = 75 MHz, T_sky the 408 MHz
  Haslam map scaled with index −2.5 and B an electromagnetic simulation of the beam. It is
  exact only if the sky structure over 50–100 MHz equals that at 75 MHz and at 408 MHz and the
  beam is known "to high precision" [src: Sims & Pober 2019, arXiv:1910.03165, Sect. 2.1.1,
  Eqs. 3–4; Murray et al. 2026, arXiv:2605.16643, Sect. V.7, Eq. 35].
- Its size. In the EDGES cross-checks the fitted trough depth ranges from 370 mK (no beam
  correction, full band) to 670 mK (one of two simulated beam models), a comparison in which
  no other model component was allowed to change [src: arXiv:1910.03165, Sect. 2.1.3]. In the
  2026 re-processing, with the legacy beam factor and flags injected the open pipeline
  reproduces the published spectrum to "much better than 1 mK"; a beam factor recomputed on a
  fine sidereal-time grid changes the residuals to a five-term log-polynomial foreground by "a
  couple of mK"; other assignments of sidereal times change the spectrum by a few K, mostly
  absorbed by the foreground fit, leaving differences below 20 mK; a bug of the legacy code
  exceeds the numerical differences between pipelines [src: arXiv:2605.16643, Sect. VIII.3].
  For scale, the claimed profile is 0.5 K deep.
- Foreground model order. A log-polynomial of 3rd to 5th order recovers the signal in
  simulations, "with the specific order required dependent on instrumental details";
  ionospheric absorption adds a roughly quadratic term; in the EDGES analysis the same
  five-term polynomial is also meant to absorb residual calibration structure, which is the
  point of contention [src: arXiv:1910.03165, Sect. 2.3.2]. Forms in use: x^β log^k x
  ("LinLog") and a linearised physical model with ionospheric terms, {x^β, x^β log x, x^β
  log² x, x^(β−2), x^(−2)} [src: arXiv:2605.16643, Sect. IV.1, Eqs. 10–11].
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

How the correction is built and why it is debated. The transfer function is the ratio of the
cross-power of cleaned injected mocks to that of the uncleaned ones, over 100 mocks cleaned
together with the real data [src: Cunnington et al. 2022, arXiv:2206.01579, Sect. 4.3, Eqs.
19–20]. Loss grows with the number of modes removed and is worst at small k_∥; after 30 modes
the 2022 auto-power still exceeded a mock with the same cleaning, "indicating that residual
RFI, foregrounds, and other systematics are present" [src: arXiv:2206.01579, Sect. 5.1]. The
correction is "numerically equivalent to a renormalisation of the power spectrum estimator",
but cleaning also mixes modes, and treating that as loss can bias the correlations between k
bins on large scales; hence the fitted damping (k / h Mpc⁻¹)^β of 2026 [src: arXiv:2610.12158,
Sects. 7.3 and 11.4]. Foregrounds exceed the signal by ~10³ in the GBT maps [src: Switzer et
al. 2013, arXiv:1304.3712] and by 10³–10⁵ for CHIME [src: arXiv:2202.01242, Sect. IV.5].

**Mask–gain coupling in interferometers.** A frequency-dependent RFI mask with a 1% gain
difference between two days makes the average of two smooth spectra non-smooth and leaks
foregrounds to high delay; CHIME filters each 9.94 s integration before averaging and drops
those with more than 2% of samples missing [src: CHIME Collaboration 2025, arXiv:2511.19620,
Sect. III.2.3]. Its systematic on A²_HI is ± 0.61 on 3.55, about 17%, against a statistical
error of +27/−37% [der from src: arXiv:2511.19620, Sect. VI.2.3].

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
- Form of the correction. COMAP divides the measured spectrum by T(k) = T_f T_b T_p T_ν
  (filter, beam, pixel window, channel window); the filter term comes from simulations, and
  the uncertainty is divided by the same T, "becoming large whenever the transfer function
  T(k) becomes small" [src: Stutzer et al. 2024, arXiv:2406.07511, Sect. 4, Eqs. 18–20]. An
  end-to-end signal-injection test is given in its Appendix D (not read).
- Interlopers for CO(1–0) at z = 2–3: "very few, if any", apart from a ~10% contamination by
  CO(2–1) from z = 6–8 [src: arXiv:2406.07511, Sect. 2.1, footnote].
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

- Ionospheric effects and polarisation leakage are described from arXiv:1907.08211 without a
  size; its RFI section was not read.
- The bodies of arXiv:1810.05912, arXiv:1805.01421 and arXiv:2112.06778 could not be read (no
  usable HTML rendering): the number of foreground terms, the beam correction and the
  residual levels of the EDGES and SARAS 3 analyses are known here only through abstracts and
  through arXiv:2605.16643.
- The Planck 2016 HFI low-ℓ paper (arXiv:1605.02985) was not read beyond its abstract.
- XQR-30 flux measurements: continuum and instrument terms are now read (section 2); the
  zero-level and sky-subtraction errors were not.
- The HERA Phase II mutual-coupling model is described from the paper's own summary; the
  dedicated modelling papers it cites were not read.
- The LOFAR bias correction on the 3C196 field (arXiv:2504.18534) and the NenuFAR and
  PAPER re-analysis signal-loss treatments were not read in the paper bodies.
