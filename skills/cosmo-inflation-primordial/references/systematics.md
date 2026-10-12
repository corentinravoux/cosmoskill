# systematics — cosmo-inflation-primordial

Snapshot: 2026-10-07

Scope: the systematic effects that decide whether a primordial-physics claim holds — for n_s and its running, r, non-Gaussianity from the CMB and from large-scale structure, isocurvature, curvature, features and birefringence — with the size where a paper quantifies it, the standard mitigation, the validation test and the paper a referee expects. It ends with a checklist.

Flags as in the other files. CMB instrument systematics in general (beams, calibration, transfer functions) are in `cosmo-cmb`; galaxy-survey systematics in general are in `cosmo-galaxy-clustering`. This file keeps what is specific to primordial observables.

## A. Scalar spectral index and running
<!-- key: scalar-spectral-index-and-running -->

### A1. Dependence on the data combination
<!-- key: a1-dependence-on-the-data-combination -->

- **Mechanism.** n_s is degenerate with Ω_b h² within each CMB data set and with the parameters that BAO constrain; the sign of the n_s–Ω_b h² correlation differs between Planck and ACT (arXiv:2503.14452). A BAO data set in tension with the CMB in ΛCDM pulls n_s upward (arXiv:2507.12459).
- **Size.** +0.0060 from Planck 2018 to P-ACT, then +0.003 more with lensing and DESI BAO [der, from `results.md` section 1]; CMB-SPA without BAO gives 0.9679 ± 0.0033 (arXiv:2506.20707). The spread between combinations, 0.965 to 0.974, is two to three times the quoted error of any one.
- **Mitigation.** Quote n_s with the combination name; give the CMB-only value beside the CMB + BAO one; state the CMB–BAO consistency (2.8σ for CMB-SPA against DESI DR2, arXiv:2506.20707).
- **Validation.** Split by spectrum: P-ACT gives 0.9730 ± 0.0055 (TT), 0.974 ± 0.014 (TE), 0.976 ± 0.012 (EE) (arXiv:2503.14452) [src], so the shift is not driven by one spectrum.
- **Cite.** arXiv:2503.14452, arXiv:2507.12459.

### A2. Dependence on the cosmological model
<!-- key: a2-dependence-on-the-cosmological-model -->

- **Mechanism.** Extensions that change the damping tail or the late-time distances absorb part of the tilt.
- **Size.** With α_s, N_eff and Σm_ν free, n_s = 0.9758 ± 0.0064: the error doubles (arXiv:2609.35964) [src]. With Ω_K or w0wa free, n_s falls to 0.967–0.972 (arXiv:2607.28445) [src].
- **Mitigation.** State the model with every n_s; a model exclusion in the r–n_s plane is a statement inside ΛCDM unless shown otherwise.
- **Cite.** arXiv:2609.35964, arXiv:2607.28445.

### A3. Planck truncation, likelihood and version
<!-- key: a3-planck-truncation-likelihood-and-version -->

P-ACT removes Planck multipoles above 1000 (TT) and 600 (TE, EE) (arXiv:2503.14452). CMB-SPA changed between arXiv versions: n_s = 0.9684 ± 0.0030 in the first, 0.9679 ± 0.0033 in the second (arXiv:2506.20707) [src]. A referee asks for the arXiv version. Instrumental effects that move ACT and SPT parameters (polarised beams, leakage, calibration to Planck) are in `cosmo-cmb`.

### A4. Optical depth
<!-- key: a4-optical-depth -->

The binned primordial spectrum is constrained as e^(−2τ) P_R(k) (arXiv:2503.14454, arXiv:2609.35964); A_s inherits the τ uncertainty discussed in `cosmo-cmb`. n_s is less affected, but the amplitude of any feature or bin is quoted in that combination.

### A5. Running from the Lyα forest
<!-- key: a5-running-from-the-lyalpha-forest -->

- **Mechanism.** The P1D slope depends on the modelling of the intergalactic medium, metals, high-column-density systems and the emulator; an error in the slope is read as running.
- **Size.** eBOSS P1D + Planck gave −0.010 ± 0.004, a 2.5σ negative running [der: 0.010/0.004] (arXiv:1911.09073, via arXiv:2503.14454); P-ACT alone excludes that value at more than 3σ (arXiv:2503.14454); DESI DR1 P1D, which marginalises more systematics, gives 0.0014 ± 0.0041 with CMB and BAO (arXiv:2601.21432).
- **Mitigation and detail.** `cosmo-lyman-alpha`.

## B. Tensor-to-scalar ratio
<!-- key: tensor-to-scalar-ratio -->

### B1. Polarised Galactic dust
<!-- key: b1-polarised-galactic-dust -->

- **Mechanism.** Polarised dust emission is the main B-mode foreground at high frequency; if the dust spectral index β_d varies across the sky, the ℓ dependence of the dust spectrum changes with frequency and can mimic a tensor signal.
- **Size.** For SO, a low-order moment expansion leaves a bias of up to r ≈ 0.03 when the spatial dispersion is σ(β_d) ≈ 0.3, the most extreme case considered but still allowed by data; the bias is driven by correlations between β_d and the dust amplitude (arXiv:2508.00073) [src]. That is 25 times the SO forecast σ(r) = 1.2 × 10⁻³ [der].
- **Mitigation.** Multi-frequency parametric fits with a free dust spectral index (BK18: no external prior on it, 220 GHz as the dust lever arm, arXiv:2110.00483); moment expansions and "extended parametric methods" (arXiv:2508.00073).
- **Validation.** Recovery of r = 0 on simulations with several dust models of increasing complexity; stability of r when frequencies are dropped.
- **History a referee remembers.** The BICEP2 B-mode excess was reanalysed jointly with Planck data; the joint analysis gave r_0.05 < 0.12 (arXiv:1502.00612).
- **Cite.** arXiv:1502.00612, arXiv:2110.00483, arXiv:2508.00073.

### B2. Synchrotron
<!-- key: b2-synchrotron -->

Low-frequency channels constrain it: the WMAP and Planck maps from 23 GHz upward in BK18 (arXiv:2110.00483) and the 27 and 39 GHz SO bands (arXiv:1808.07445). No quantified residual was read this session.

### B3. Lensing B modes and delensing
<!-- key: b3-lensing-b-modes-and-delensing -->

- **Mechanism.** Lensing B modes add sample variance to r and, if the template is biased, a bias.
- **Size.** Delensing BK14 improved σ(r) by about 10% against 26% for a perfect template (arXiv:2011.08163) [src]. SO assumes 70% removal for its headline forecast (arXiv:2512.15833) [src].
- **Mitigation.** A lensing template from CMB polarisation plus a mass tracer (CIB, later internal reconstruction), included in the likelihood as a pseudo-frequency map.
- **Validation.** Simulations in which the tracer is correlated with foregrounds; comparison of the template cross-spectrum with the expected lensing BB.
- **Cite.** arXiv:2011.08163.

### B4. Temperature-to-polarisation leakage from beam mismatch
<!-- key: b4-temperature-to-polarisation-leakage-from -->

- **Mechanism.** Differences between the beams of paired orthogonal detectors convert the temperature anisotropy into spurious polarisation.
- **Size.** For BICEP3 at 95 GHz over 2016–2024 the residual after extended deprojection is equivalent to r = (1.12 ± 0.06) × 10⁻³, down from (4.5 ± 0.7) × 10⁻³ with standard deprojection; preliminary (arXiv:2608.25016) [src]. The standard-deprojection residual is half of the BK18 σ(r) = 0.009 [der], so it cannot be ignored at the BK24 depth.
- **Mitigation.** Deprojection of beam-difference templates built from the temperature map; far-field beam maps.
- **Cite.** arXiv:2608.25016.

### B5. Beam chromaticity and bandpass
<!-- key: b5-beam-chromaticity-and-bandpass -->

For the SO SATs, the variation of the beam inside each band biases r by 0.02σ and the dust amplitude A_d by up to 0.77σ; all biases stay below 1σ, also with bandpass-shape uncertainty (arXiv:2503.01791) [src]. The effect matters for the foreground parameters more than for r.

### B6. Low-frequency noise and filtering
<!-- key: b6-low-frequency-noise-and-filtering -->

Atmospheric and instrumental 1/f noise sets the lowest usable multipole. SPT-3G has noise knees at ℓ = 128 (95 GHz) and 182 (150 GHz), which is why its r limit is 0.25 despite deep maps (arXiv:2505.02827) [src]. The SO forecast assumes ℓ_knee = 50 (arXiv:2512.15833) [src]; the forecast is conditional on reaching it.

### B7. Statistical construction and priors
<!-- key: b7-statistical-construction-and-priors -->

Feldman–Cousins versus Bayesian limits differ by almost a factor of two for SPIDER (0.11 against 0.19, arXiv:2103.13334). Freeing ΛCDM parameters and adding Planck low-ℓ polarisation moves 0.036 to 0.032 on the same B-mode data (arXiv:2112.07961); a different n_s moves it to 0.038 (arXiv:2503.14454). None of these is new B-mode information.

### B8. Model of the tensor spectrum
<!-- key: b8-model-of-the-tensor-spectrum -->

Limits assume a nearly scale-invariant inflationary spectrum with n_t fixed by the consistency relation. Causal post-inflationary sources have a different spectrum and their limit, r_ect < 0.0077, is not comparable (arXiv:2601.20958).

## C. Non-Gaussianity from the CMB
<!-- key: non-gaussianity-from-the-cmb -->

### C1. Lensing–ISW bispectrum
<!-- key: c1-lensing-isw-bispectrum -->

The correlation between lensing and the ISW effect produces a squeezed bispectrum that biases f_NL^local if it is not subtracted. Planck 2018 detects it at 3.5σ (arXiv:1905.05697) [src]. The size of the bias on f_NL^local was not read this session.

### C2. Foreground and point-source bispectra
<!-- key: c2-foreground-and-point-source-bispectra -->

Unclustered point sources and the CIB have their own bispectra, fitted jointly (arXiv:2504.00884). Validation: stability across component-separation methods and consistency with Minkowski functionals (arXiv:1502.01592).

### C3. Fidelity of the simulations
<!-- key: c3-fidelity-of-the-simulations -->

Errors and the linear term come from simulations. Planck 2015 polarisation results were labelled preliminary because the simulated noise did not match the data (arXiv:1502.01592); PR4 simulations have a systematically low lensing bispectrum, shown to be harmless (arXiv:2504.00884).

### C4. Template dependence and look-elsewhere
<!-- key: c4-template-dependence-and-look-elsewhere -->

A null result for three templates is not a null result for all shapes; scans over oscillatory or collider templates need a look-elsewhere correction (2.4σ after correction, arXiv:2511.17500).

## D. Non-Gaussianity from large-scale structure
<!-- key: non-gaussianity-from-large-scale-structure -->

### D1. The response b_φ
<!-- key: d1-the-response-bphi -->

- **Mechanism.** The signal is f_NL · b_φ; b_φ depends on how the tracer was selected, not only on its linear bias.
- **Size.** For the same BOSS data, σ(f_NL) runs from 16 to 226 with the b_φ(b_1) relation (arXiv:2205.05673) [src], and is 19, 44 or 165 for the highest-concentration third, all, or the lowest-concentration third of haloes (arXiv:2209.07251) [src]. For DESI DR1 the central value moves from −3.6 to +3.5 between p = 1.6 and p = 1 for quasars (arXiv:2411.17623) [src]; for Quaia the error grows from 19 to 26 (arXiv:2504.20992) [src].
- **Mitigation.** Simulation-based priors on p for the selected sample (p̄ ≈ 1.4 for DESI-like quasars in IllustrisTNG, checked against CAMELS; arXiv:2602.12357); reporting f_NL for more than one p.
- **Warning.** Marginalising b_φ with a wide prior is not conservative: it biases f_NL through projection effects (arXiv:2205.05673).
- **Cite.** arXiv:0805.3580, arXiv:2205.05673, arXiv:2209.07251, arXiv:2602.12357.

### D2. Large-scale imaging systematics
<!-- key: d2-large-scale-imaging-systematics -->

- **Mechanism.** Stellar density, extinction, depth and seeing modulate the target density on the same scales as the 1/k² signal; excess large-scale power mimics a non-zero f_NL, and over-correction removes signal.
- **Size.** For eBOSS DR16 the optimal analysis improved the error by 10% where a Fisher forecast predicted more, which its authors read as "still unknown systematic effects in the data" (arXiv:2309.15814) [src]. SPHEREx allocates δn/n < 0.2% rms per dex to spurious clustering to reach Δf_NL < 0.5 (arXiv:2511.02985) [src].
- **Mitigation.** Regression or neural-network weights against imaging templates (arXiv:2106.13725); an angular integral-constraint term in the window to account for the modes removed by the weights (arXiv:2411.17623); cross-correlation between tracers (arXiv:2604.05213) or with CMB lensing (arXiv:2512.17865), which do not share these systematics.
- **Validation.** Mocks that reproduce the target selection with contamination injected and removed (EZmocks, arXiv:2106.13725); blinded validation (arXiv:2411.17623); the spectroscopic DESI quasar auto-spectrum shows no excess large-scale power, unlike photometric quasar samples (arXiv:2512.17865).

### D3. Window function and integral constraints
<!-- key: d3-window-function-and-integral-constraints -->

Estimating the mean density and the radial selection from the data removes large-scale modes. DESI corrects the window for the radial integral constraint (arXiv:2411.17623). An error here is degenerate with f_NL.

### D4. Redshift errors and tomographic bin mismatch
<!-- key: d4-redshift-errors-and-tomographic-bin-mismatch -->

For a SPHEREx-like photometric analysis, galaxies assigned to the wrong redshift bin produce apparent tensions of 3–6σ on f_NL^local and 9–12σ on the bias; a scattering-matrix formalism removes the bias in simulations (Saraf and Parkinson 2024, arXiv:2412.03078) [src].

### D5. Bias parameters and scale cuts in bispectrum analyses
<!-- key: d5-bias-parameters-and-scale-cuts-in-bispectrum -->

Equilateral and orthogonal constraints depend on the priors of the non-linear bias parameters: 940 ± 600 with everything free against 260 ± 300 with quadratic bias and cosmology fixed (arXiv:2201.07238) [src]; simulation-based priors tighten DESI + BOSS to 200 ± 230 (arXiv:2512.04266) [src]. A referee asks for the scale cuts, the validation on simulations with known f_NL, and the result without the informative priors.

### D6. Covariance approximations in forecasts
<!-- key: d6-covariance-approximations-in-forecasts -->

The SPHEREx forecast omits the non-Gaussian covariance and the power spectrum–bispectrum covariance, worth "tens of percent" (arXiv:2511.02985). Euclid's σ(f_NL^local) = 2.2 assumes universality and k_max = 0.15 h Mpc⁻¹ (arXiv:2507.15819).

### D7. Relativistic and wide-angle effects
<!-- key: d7-relativistic-and-wide-angle-effects -->

General-relativistic and wide-angle terms contribute on the same large scales as the f_NL signal. No quantified result was read this session; listed under "Not verified".

### D8. Cluster counts
<!-- key: d8-cluster-counts -->

The ACT cluster f_NL depends on the mass calibration: the analysis finds a 16.4% residual mass bias "heavily informed by our adopted priors", with negligible effect on f_NL at the present error (arXiv:2602.03917) [src].

## E. Isocurvature
<!-- key: isocurvature -->

- **Prior-volume effects.** With a flat prior on the isocurvature tilt, an unconstrained amplitude leaves a large volume at extreme tilts; Planck and ACT sample amplitudes at two scales instead (arXiv:2503.14454).
- **Correlation with n_s.** The scale-invariant CDI limit weakens from 0.9 to 1.1 (× 10⁻¹⁰) when ACT is added because n_s rises (arXiv:2503.14454) [src]. Isocurvature limits inherit the data-combination dependence of section A1.
- **Lensing-like smoothing.** Compensated isocurvature produces extra smoothing at high ℓ (arXiv:1807.06211), so it responds to the same peak-smoothing preference as A_L [der: inference from the mechanism]; the 68% interval 0.0037 +0.0016/−0.0021 is not a detection.
- **Non-linear modelling.** HMCode can fail for blue-tilted spectra (arXiv:2503.14454).

## F. Spatial curvature
<!-- key: spatial-curvature -->

- **A_L and likelihood.** The Planck-only preference for Ω_K < 0 has the same origin as A_L > 1 and changes by about 0.5σ with the polarisation likelihood (−0.044 with Plik, −0.037 with CamSpec; arXiv:1807.06209) [src]. Quote release and likelihood.
- **Combining discordant data.** Planck alone and BAO were in 2.5–3σ tension in the curved model (arXiv:1908.09139); combining them hides that. The same holds today for CMB and DESI in ΛCDM.
- **Model dependence at late times.** Ω_K from BAO and supernovae depends on the dark-energy model: an open preference in ΛCDM disappears in extended models (arXiv:2604.23492); with w0wa free DESI + CMB + SNe give (0.6–1.1) × 10⁻³ ± 1.3 × 10⁻³ (arXiv:2503.14738).
- **Supernova sample.** The late-time open preference ranges from 2σ to 5σ with the supernova compilation (arXiv:2512.19565).

## G. Primordial features
<!-- key: primordial-features -->

- **Look-elsewhere.** Local Δχ² of −10 to −15 corresponds to at most 2.6σ globally (arXiv:2605.30236).
- **Fixed cosmology.** A 3σ logarithmic feature in DESI DR1 at fixed Planck cosmology disappears when the cosmology is varied (arXiv:2610.10530).
- **Likelihood version.** Planck PR3 hints shrink with PR4 CamSpec (arXiv:2605.30236).
- **BAO degeneracy and non-linear damping.** Frequencies near the BAO one are poorly constrained; the damping must be modelled consistently (arXiv:1906.08758, arXiv:2610.10530).
- **Binning.** Binned likelihoods erase high-frequency oscillations (arXiv:2605.30236).

## H. Cosmic birefringence
<!-- key: cosmic-birefringence -->

- **Polarisation-angle calibration.** EB measures α + β. Planck's raw angle uncertainty is the systematic that the Minami–Komatsu method removes (arXiv:2011.11254); ACT relies on optics-model priors, and its result is conditional on them (arXiv:2509.13654, arXiv:2608.06480). Target for hardware calibration: 0.08° for the SO SATs (**forecast**, arXiv:2606.11300).
- **Intrinsic EB of Galactic dust.** The foreground-based calibration assumes the foreground EB is known. β decreases as the Galactic mask grows (arXiv:2201.07682); a dust-robust variant of the ACT + Planck analysis gives 3.5σ instead of 4.8σ (arXiv:2608.06480) [src].
- **Intensity-to-polarisation leakage.** Marginalised in the ACT analysis (arXiv:2509.13654).
- **Omitted systematic in a quoted error.** 0.30 ± 0.05 excludes the angle systematic (arXiv:2507.16714).
- **Self-calibrated experiments.** BICEP/Keck constrains only β(ℓ) variations (arXiv:2603.06812).

## I. Checklist for a referee
<!-- key: checklist-for-a-referee -->

1. n_s, α_s: which CMB combination by name, which arXiv version, BAO included or not, which model; is the CMB–BAO tension stated?
2. Any claim that a model (Starobinsky, Higgs, α-attractor) is "excluded": at what confidence, for what N and reheating assumption, in which cosmological model?
3. r: pivot scale; 95% limit construction; which B-mode data (almost always BK18); what was added to them; foreground model and dust prior; delensed or not.
4. r forecasts: assumed ℓ_knee, delensing fraction, foreground complexity, f_sky, mission configuration (pre- or post-reformation LiteBIRD; SO with three or six SATs).
5. f_NL from the CMB: release (2015, 2018, PR4), T or T + E, estimator, lensing–ISW subtraction.
6. f_NL from galaxies: value of p or the b_φ prior for each tracer; imaging-systematics treatment; integral constraints; blinding; result for a second p.
7. f_NL from the bispectrum: bias priors, scale cuts, fixed or free cosmology, validation on simulations with non-zero f_NL.
8. A combined CMB + LSS f_NL: is the LSS part conditional on b_φ?
9. Isocurvature: which mode, correlated or not, at which k, which definition (β_iso, α_non-adi, or P_II amplitude).
10. Ω_K: sign convention; CMB only or with BAO; release and likelihood; dark-energy model.
11. Features: global significance; cosmology varied; unbinned likelihood; frequency range searched.
12. Birefringence: how the polarisation angle was calibrated; dust EB model; whether the quoted error includes the angle systematic; the authors' own caveat.
13. Every forecast labelled as such and attached to a survey configuration that still exists.

## J. Not verified
<!-- key: not-verified -->

- The bias on f_NL^local from the lensing–ISW bispectrum if it is not subtracted.
- Quantified synchrotron residuals for r.
- Relativistic and wide-angle contributions to the large-scale power spectrum in f_NL analyses (only titles of 2025–2026 papers were seen).
- Stellar-contamination requirements for SPHEREx beyond the δn/n allocation.
- BICEP/Keck systematics budgets other than beam leakage (polarisation-angle, gain, ground pickup).
- E-to-B leakage from partial sky and filtering in ground-based B-mode analyses: no paper read.
- Systematics of the Planck low-ℓ polarisation that enter r < 0.032.
