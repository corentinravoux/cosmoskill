# systematics — cosmo-inflation-primordial

Snapshot: 2026-10-14

Scope: the systematic effects that decide whether a primordial-physics claim holds — for n_s and its running, r, non-Gaussianity from the CMB and from large-scale structure, isocurvature, curvature, features and birefringence — with the size where a paper quantifies it, the standard mitigation, the validation test and the paper a referee expects. It ends with a checklist.

Flags as in the other files. CMB instrument systematics in general (beams, calibration, transfer functions) are in `cosmo-cmb`; galaxy-survey systematics in general are in `cosmo-galaxy-clustering`. This file keeps what is specific to primordial observables.

## A. Scalar spectral index and running
<!-- key: scalar-spectral-index-and-running -->

### A1. Dependence on the data combination
<!-- key: a1-dependence-on-the-data-combination -->

- **Mechanism.** n_s is degenerate with Ω_b h² within each CMB data set and with the parameters that BAO constrain; the sign of the n_s–Ω_b h² correlation differs between Planck and ACT (arXiv:2503.14452). A BAO data set in tension with the CMB in ΛCDM pulls n_s upward (arXiv:2507.12459).
- **Size.** n_s = 0.9649 ± 0.0042 for Planck 2018 (arXiv:1807.06211) [src: abstract], 0.9709 ± 0.0038 for P-ACT (arXiv:2503.14452) [src: Sect. VIII.3] and 0.974 ± 0.003 with lensing and DESI BAO (arXiv:2503.14452) [src: abstract]; CMB-SPA without BAO gives 0.9679 ± 0.0033 (arXiv:2506.20707) [src: Sect. II]. The differences between combinations are comparable to or larger than the quoted error of any one.
- **Mitigation.** Quote n_s with the combination name; give the CMB-only value beside the CMB + BAO one; state the CMB–BAO consistency (2.8σ for CMB-SPA against DESI DR2, arXiv:2506.20707) [src: abstract].
- **Validation.** Split by spectrum: P-ACT gives consistent results from either temperature or polarisation (arXiv:2503.14452) [src: abstract], so the shift is not driven by one spectrum.
- **Cite.** arXiv:2503.14452, arXiv:2507.12459.

### A2. Dependence on the cosmological model
<!-- key: a2-dependence-on-the-cosmological-model -->

- **Mechanism.** Extensions that change the damping tail or the late-time distances absorb part of the tilt.
- **Size.** With α_s, N_eff and Σm_ν free, n_s = 0.9758 ± 0.0064 (arXiv:2609.35964) [src: abstract]. With Ω_K free, n_s = 0.9667 ± 0.0041 (Planck + DESI) or 0.9692 ± 0.0035 (with ACT and SPT); with w0wa free, 0.9716 ± 0.0032 (arXiv:2607.28445) [src: abstract].
- **Mitigation.** State the model with every n_s; a model exclusion in the r–n_s plane is a statement inside ΛCDM unless shown otherwise.
- **Cite.** arXiv:2609.35964, arXiv:2607.28445.

### A3. Planck truncation, likelihood and version
<!-- key: a3-planck-truncation-likelihood-and-version -->

P-ACT keeps Planck high-ℓ data at ℓ < 1000 in TT and ℓ < 600 in TE/EE (arXiv:2503.14452) [src: Sect. VI.3]. CMB-SPA changed between arXiv versions (the values are in `results.md`, section 1); the second gives n_s = 0.9679 ± 0.0033 (arXiv:2506.20707) [src: Sect. II]. A referee asks for the arXiv version. Instrumental effects that move ACT and SPT parameters (polarised beams, leakage, calibration to Planck) are in `cosmo-cmb`.

### A4. Optical depth
<!-- key: a4-optical-depth -->

The binned primordial spectrum is constrained as e^(−2τ) P_R(k) (arXiv:2503.14454, arXiv:2609.35964); A_s inherits the τ uncertainty discussed in `cosmo-cmb`. n_s is less affected, but the amplitude of any feature or bin is quoted in that combination.

### A4b. How n_s moves with spectrum, likelihood, τ and data set (body-level)
<!-- key: a4b-how-ns-moves-with-spectrum-likelihood-tau -->

All ΛCDM, 68%, k_* = 0.05 Mpc⁻¹. <!-- num: not a value -->

| n_s | What changes | Place |
|---|---|---|
| 0.9626 ± 0.0057 | Planck 2018 TT + lowE (τ = 0.052 ± 0.008) | arXiv:1807.06211 [src: Sect. 3.1, Table 2, Eqs. 6–7] |
| 0.9650 ± 0.0061 | TT with the LFI 70 GHz low-ℓ pixel likelihood (τ = 0.072 ± 0.016) instead of SimAll | arXiv:1807.06211 [src: Sect. 3.1, Eqs. 8–9] |
| 0.980 ± 0.015; 0.967 ± 0.011; 0.969 ± 0.009 | EE + lowE; TE + lowE; TE,EE + lowE | arXiv:1807.06211 [src: Table 2, Eq. 11] |
| 0.9649 ± 0.0044 (Plik); 0.9658 ± 0.0045 (CamSpec) | high-ℓ likelihood; adding polarisation moves n_s up by about 0.5σ from TT | arXiv:1807.06211 [src: Sect. 3.1, Eq. 10] |
| 0.9655 ± 0.0062 → 0.9626 ± 0.0057 | Planck 2015 TT + lowP → 2018 TT + lowE, "mainly driven" by τ falling from 0.078 ± 0.022 to 0.052 ± 0.008 | arXiv:1807.06211 [src: Sect. 3.1] |
| 0.9657 ± 0.0040 (Planck); 0.951 ± 0.011 (SPT-3G D1); 0.9682 ± 0.0069 (ACT DR6); 0.9671 ± 0.0058 (SPT + ACT); 0.9636 ± 0.0035 (SPT + Planck); 0.9679 ± 0.0033 (CMB-SPA) | same set-up for each: T&E + lensing + PR4 τ prior | arXiv:2506.20707 [src: Table 1] |
| 0.9709 ± 0.0038 | P-ACT: the n_s–Ω_b h² correlation is positive from large scales, negative from small; combining breaks it | arXiv:2503.14452 [src: Sect. VIII.3] |

ACT-only parameters rest on the Planck Sroll2 large-scale EE for τ; with DESI DR2 the best-fit τ is 1.3σ above the Sroll2 mean (1.1σ with DR1), and ACT + Sroll2 differs from DESI DR2 by 2.8σ in the Ω_m–h r_d plane, against 1.6σ for P-ACT (arXiv:2503.14452) [src: App. H]. ACT varies 14 foreground parameters with Gaussian priors on Galactic dust amplitudes, and polarisation efficiencies uniform in [0.9, 1.1]; CMB-only and multi-frequency likelihoods agree within 0.1σ (arXiv:2503.14452) [src: Sect. VII.2, Table 3; Sect. VIII.1]. With a free polarisation efficiency the EE-only error on Ω_c h² roughly doubles [src: Sect. VIII.1].

### A5. Running from the Lyα forest
<!-- key: a5-running-from-the-lyalpha-forest -->

- **Mechanism.** The P1D slope depends on the modelling of the intergalactic medium, metals, high-column-density systems and the emulator; an error in the slope is read as running.
- **Size.** eBOSS P1D + Planck gave −0.010 ± 0.004, which its authors call a slight (3σ) preference for negative running (arXiv:1911.09073) [src: abstract]; P-ACT alone excludes that value at more than 3σ (arXiv:2503.14454) [src: Sect. IV.1]; DESI DR1 P1D, which marginalises more systematics, gives 0.0014 ± 0.0041 with CMB and BAO (arXiv:2601.21432) [src: abstract].
- **Mitigation and detail.** `cosmo-lyman-alpha`.

## B. Tensor-to-scalar ratio
<!-- key: tensor-to-scalar-ratio -->

### B1. Polarised Galactic dust
<!-- key: b1-polarised-galactic-dust -->

- **Mechanism.** Polarised dust emission is the main B-mode foreground at high frequency; if the dust spectral index β_d varies across the sky, the ℓ dependence of the dust spectrum changes with frequency and can mimic a tensor signal.
- **Size.** For SO, a low-order moment expansion leaves a bias of up to r ≈ 0.03 when the spatial dispersion is σ(β_d) ≈ 0.3, the most extreme case considered but still allowed by data; the bias is driven by correlations between β_d and the dust amplitude (arXiv:2508.00073) [src: abstract]. It is far above the SO forecast σ(r) = 1.2 × 10⁻³ (arXiv:2512.15833) [src: abstract].
- **Body-level (SO SATs, arXiv:2508.00073)** [src: Sect. IV.2, Fig. 9]: with realistic PySM d10 dust and s5 synchrotron, the fiducial BBPower pipeline is biased even at zero dust dispersion, from synchrotron decorrelation (spatially varying β_s); a second-order moment in β_s removes it. With growing β_d dispersion (spatial or along the line of sight) the fiducial bias rises to r ≈ 0.1; the moment pipeline stays consistent with r = 0 at low dispersion but is still biased for x_βd ≳ 1.0 (spatial) or ≳ 1.2 (line of sight). T_d variations bias r less. A covariance from Gaussian power-law simulations without decorrelation is "known to be incorrect" and gives χ²/dof = 1.7 at zero dust dispersion; an angular template plus a covariance with decorrelation brings r back in line for the x_βd = 1.6 case.
- **Mitigation.** Multi-frequency parametric fits with a free dust spectral index (BK18: no external prior on it, 220 GHz as the dust lever arm, arXiv:2110.00483 [src: abstract]); moment expansions and "extended parametric methods" (arXiv:2508.00073).
- **Validation.** Recovery of r = 0 on simulations with several dust models of increasing complexity; stability of r when frequencies are dropped.
- **History a referee remembers.** The BICEP2 B-mode excess was reanalysed jointly with Planck data; the joint analysis gave r_0.05 < 0.12 (arXiv:1502.00612) [src: abstract].
- **Cite.** arXiv:1502.00612, arXiv:2110.00483, arXiv:2508.00073.

### B2. Synchrotron
<!-- key: b2-synchrotron -->

Low-frequency channels constrain it: the WMAP and Planck maps from 23 GHz upward in BK18 (arXiv:2110.00483) and the 27 and 39 GHz SO bands (arXiv:1808.07445). In BK18 synchrotron is not detected (A_sync,23 < 1.4 μK², 95%), and the WMAP 23/33 GHz and LFI 30/44 GHz bands pull A_sync in opposite directions: dropping WMAP makes it peak at zero, dropping LFI well above zero (arXiv:2110.00483) [src: App. E.2]. A residual for r below the BK18 noise follows from Table 2 there (section B9).

### B3. Lensing B modes and delensing
<!-- key: b3-lensing-b-modes-and-delensing -->

- **Mechanism.** Lensing B modes add sample variance to r and, if the template is biased, a bias.
- **Size.** Delensing BK14 improved σ(r) by about 10% against 26% for a perfect template (arXiv:2011.08163) [src: abstract]. SO assumes 70% removal for its headline forecast (arXiv:2512.15833) [src: abstract].
- **Mitigation.** A lensing template from CMB polarisation plus a mass tracer (CIB, later internal reconstruction), included in the likelihood as a pseudo-frequency map.
- **Validation.** Simulations in which the tracer is correlated with foregrounds; comparison of the template cross-spectrum with the expected lensing BB.
- **Body-level sizes (BK14 + lensing template, arXiv:2011.08163).** σ(r) 0.024 → 0.022 in the six-parameter search of 499 simulations (0.026 → 0.023 in eight dimensions) [src: Sect. VI.1]. A misestimate of the CIB–φ cross-spectrum by half the patch-to-patch scatter biases r by 0.2σ [src: Sect. IV.2]; a 1.7% low polarisation efficiency of the input SPTpol Q/U maps gives a negligible bias [src: Sect. IV.2]. The template needs E modes at higher ℓ than the BICEP beam resolves, hence the SPTpol and Planck maps [src: Sect. III.1.3].
- **Cite.** arXiv:2011.08163.

### B4. Temperature-to-polarisation leakage from beam mismatch
<!-- key: b4-temperature-to-polarisation-leakage-from -->

- **Mechanism.** Differences between the beams of paired orthogonal detectors convert the temperature anisotropy into spurious polarisation.
- **Size.** For BICEP3 at 95 GHz over 2016–2024 the residual after extended deprojection is equivalent to r = (1.12 ± 0.06) × 10⁻³, down from (4.5 ± 0.7) × 10⁻³ with standard deprojection; preliminary (arXiv:2608.25016) [src: abstract]. The standard-deprojection residual is not small against the BK18 σ(r) = 0.009 (arXiv:2110.00483) [src: abstract], so it cannot be ignored at the BK24 depth.
- **Mitigation.** Deprojection of beam-difference templates built from the temperature map; far-field beam maps.
- **Cite.** arXiv:2608.25016.

### B5. Beam chromaticity and bandpass
<!-- key: b5-beam-chromaticity-and-bandpass -->

For the SO SATs, the variation of the beam inside each band biases r by 0.02σ and the dust amplitude A_d by up to 0.77σ; all biases stay below 1σ, also with bandpass-shape uncertainty (arXiv:2503.01791) [src: abstract]. The effect matters for the foreground parameters more than for r.

### B6. Low-frequency noise and filtering
<!-- key: b6-low-frequency-noise-and-filtering -->

Atmospheric and instrumental 1/f noise sets the lowest usable multipole. SPT-3G has noise knees at ℓ = 128 (95 GHz) and 182 (150 GHz), which is why its r limit is 0.25 despite deep maps (arXiv:2505.02827) [src: abstract]. The SO forecast assumes ℓ_knee = 50 (arXiv:2512.15833) [src: abstract]; the forecast is conditional on reaching it.

### B7. Statistical construction and priors
<!-- key: b7-statistical-construction-and-priors -->

Feldman–Cousins versus Bayesian limits differ by almost a factor of two for SPIDER (0.11 against 0.19, arXiv:2103.13334) [src: abstract]. Freeing ΛCDM parameters and adding Planck low-ℓ polarisation moves 0.036 to 0.032 on the same B-mode data (arXiv:2112.07961) [src: abstract; Sect. I for 0.036]; a different n_s moves it to 0.038 (arXiv:2503.14454) [src: Sect. IV.4]. None of these is new B-mode information.

### B8. Model of the tensor spectrum
<!-- key: b8-model-of-the-tensor-spectrum -->

Limits assume a nearly scale-invariant inflationary spectrum with n_t fixed: BK18 fixes n_t = 0 (arXiv:2110.00483) [src: main text, likelihood paragraph], Planck 2018 and ACT DR6 impose the consistency relation n_t = −r/8 (arXiv:1807.06211 [src: Sect. 3.5]; arXiv:2503.14454 [src: Sect. IV.4]); at the present limit the difference is negligible. Causal post-inflationary sources have a different spectrum and their limit, r_ect < 0.0077, is not comparable (arXiv:2601.20958).

### B9. BK18 budget as read in the paper body
<!-- key: b9-bk18-budget-as-read-in-the-paper-body -->

BICEP/Keck 2021, arXiv:2110.00483. Baseline: r_0.05 = 0.014 +0.010/−0.011 (r_0.05 < 0.036, 95%), A_d,353 = 4.4 +0.8/−0.7 μK², A_sync,23 < 1.4 μK² (95%), β_d = 1.49 +0.13/−0.12; lensing BB fixed to the Planck 2018 ΛCDM prediction [src: main text, results paragraph]. [src: Sect. "pacs"]

| Item | Baseline treatment or size | Effect on r | Place |
|---|---|---|---|
| Dust SED | modified black body, T_d = 19.6 K, β_d free (no prior); amplitude at 353 GHz, ℓ = 80 | dropping the old prior β_d = 1.59 ± 0.11 changes r "very little" | [src: main text; App. E.1] |
| Dust spatial spectrum | D_ℓ ∝ ℓ^α_d, uniform −1 < α_d < 0 | — | [src: main text] |
| Synchrotron | power law, Gaussian prior β_s = −3.1 ± 0.3 at 23 GHz; uniform −1 < α_s < 0; dust–sync correlation ε | not detected: removing it raises −2 log L by 1.5 on data against 2.5 in simulations | [src: main text; App. E.2, Table 1] |
| Dust decorrelation Δ_d | not in baseline (biasing: in BK15 sims without decorrelation, 72% of r curves peaked at zero when freed) | freeing it shifts r down slightly; Δ_d peaks at 1 | [src: App. E.2] |
| Lensing amplitude | A_L^BB = 1.03 +0.08/−0.09 if freed | r "hardly changes" | [src: App. E.2] |
| Third-party dust skies (PySM 1–3, MHD, MKD, Vansyngel) | σ(r) 0.009–0.012 | bias ≤ 0.1σ without decorrelation parameter; decorrelated Gaussian sky refit without Δ_d: +2.1σ | [src: App. E.4, Table 2] |
| T→P leakage from beam mismatch | Δr = (1.5 ± 1.1) × 10⁻³ (BK15: 2.7 ± 1.9) | subdominant to σ(r) = 0.009 | [src: App. F.1] |
| Other additive (EMI, magnetic, thermal, ghosts) | r < 10⁻⁴ each; satellite-uplink EMI r < 1.7 × 10⁻³ (95%) | negligible | [src: App. F.2] |
| Polarised point sources | upward bias 1–3 × 10⁻³ (estimate) | not corrected | [src: App. F.2] |
| Noise-bias × deprojection filtering | downward bias 2 × 10⁻³ (preliminary) | not corrected | [src: App. F.2] |
| Bandpass centre (2% Gaussian prior per band) | shift of the 95% limit 3 × 10⁻⁵ | negligible | [src: App. F.3] |

### B10. SPT-3G 2019–2020 BB budget as read
<!-- key: b10-spt-3g-2019-2020-bb-budget-as-read -->

Zebrowski et al. 2025, arXiv:2505.02827: eight-component model, uniform prior r > 0, lensing BB fixed to Planck ΛCDM [src: Sect. VI.1].

| Item | Treatment or size | Effect on r | Place |
|---|---|---|---|
| Dust | modified black body, T = 19.6 K; uniform β_d ∈ [0, 3]; D_ℓ = A(ℓ/80)^α with α ∈ [−1.2, −0.2] | r anti-correlated with A_dust | [src: Sect. VI.1, Eq. 7; Sect. VII.1] |
| Fitted dust, BK18 mask | A_150,ℓ=80 = 0.013 +0.006/−0.004, α = −0.73 ± 0.29, β = 2.2 ± 0.5; agrees with BK18 at about 1σ | r < 0.25, σ(r) = 0.067, PTE 42% | [src: Table 4] |
| Same, 1500 deg² mask | A = 0.037 ± 0.009, β = 1.67 ± 0.26 | r < 0.25, σ(r) = 0.068, PTE 3.0% | [src: Table 4] |
| Radio Poisson | D_ℓ ∝ (ℓ/500)², S_ν ∝ ν^−0.75, positive amplitude | marginalised | [src: Sect. VI.1, Eq. 8] |
| Synchrotron | omitted: WMAP 23 GHz extrapolated to 95 GHz gives 1.5 × 10⁻⁵ μK² in the first bin, 300 times below its error | — | [src: Sect. VI.1] |
| Polarisation angle | global rotation minimising TB and EB: Δψ = 0.008, 0.007, −0.006 rad at 95, 150, 220 GHz | self-calibration, so no constant β measurable | [src: Sect. IV.2, Eq. 1] |
| Calibration | three calibration terms in the fit | marginalised | [src: Sect. VI.1] |

### B11. SO six-SAT forecast: how σ(r) moves (**forecast**)
<!-- key: b11-so-six-sat-forecast-how-sigma-r-moves -->

Simons Observatory 2025, arXiv:2512.15833, 10³ σ(r) at 68% after 10 years, without / with foreground frequency decorrelation (moment expansion) [src: Sect. 3.2, Table 2].

| 1/f noise | Delensing | 10³ σ(r) | Nominal three-SAT SO, 5 yr, A_lens = 0.5 |
|---|---|---|---|
| pessimistic | A_lens = 0.5 | 1.2 / 1.4 | 2.7 / 3.1 |
| pessimistic | A_lens = 0.3 (70%) | 1.0 / 1.2 | — |
| optimistic | A_lens = 0.5 | 0.9 / 1.1 | 1.9 / 2.5 |
| optimistic | A_lens = 0.3 | 0.7 / 0.9 | — |

Decorrelation degrades σ(r) by about 20%, the pessimistic 1/f model by about 30%, and going from 50% to 70% delensing improves it by 20% after 10 years. The paper's own fiducial is the most conservative case, σ(r) = 1.4 × 10⁻³ (pessimistic 1/f, 50% delensing, decorrelation); the 1.2 × 10⁻³ of the abstract assumes 70% delensing (arXiv:2512.15833) [src: Sect. 3.2].

## C. Non-Gaussianity from the CMB
<!-- key: non-gaussianity-from-the-cmb -->

### C1. Lensing–ISW bispectrum
<!-- key: c1-lensing-isw-bispectrum -->

The correlation between lensing and the ISW effect produces a squeezed bispectrum that biases f_NL^local if it is not subtracted. Planck 2018 detects it at 3.5σ (arXiv:1905.05697) [src]. In polarisation the lensing–reionisation E-mode correlation plays the same role; the template amplitude f_NL^lens is 1 in ΛCDM [src: Sect. 4.1, Eq. 37].

Planck 2018 sizes, SMICA, 68% (arXiv:1905.05697, Table 5 and Sect. 5.1, as given per row):

| Quantity | Value | Place |
|---|---|---|
| f_NL^local T, KSW: not subtracted → lensing subtracted | 6.7 ± 5.6 → −0.5 ± 5.6 | [src: Table 5] |
| f_NL^local T+E, KSW: not subtracted → subtracted | 4.1 ± 5.1 → −0.9 ± 5.1 | [src: Table 5] |
| f_NL^local T+E, subtracted, by estimator | KSW −0.9 ± 5.1; Binned −2.5 ± 5.0; Modal 1 −0.1 ± 4.7; Modal 2 −2.0 ± 5.0 | [src: Table 5] |
| f_NL^ortho T+E, not subtracted → subtracted (KSW) | −46 ± 23 → −37 ± 23 | [src: Table 5] |
| f_NL^equil T+E (KSW) | −17 ± 47 → −18 ± 47 (lensing bias negligible) | [src: Table 5] |
| E only (KSW, subtracted) | local 47 ± 28, equilateral 169 ± 161, orthogonal −208 ± 86 | [src: Table 5] |
| Joint fit instead of subtraction (Binned, SMICA) | T: f_NL^local = 2.7 ± 5.7 with f_NL^lens = 0.60 ± 0.34; T+E: −1.7 ± 5.2 with 0.82 ± 0.27 | [src: Sect. 5.1] |
| f_NL^lens from the tSZ-cleaned SMICA T (+E) map | Binned 0.83 ± 0.35 (0.90 ± 0.28); Modal 1 0.90 ± 0.34 (1.03 ± 0.27) | [src: Table 2] |

The final numbers are KSW on SMICA, chosen for stability across releases; the T-only lensing amplitude is low in all maps, possibly from an ISW–tSZ–tSZ bispectrum anti-correlated with the lensing shape [src: Sects. 4.1, 5.1]. Point-source contamination of the primordial shapes is negligible [src: Sect. 5.1].

### C2. Foreground and point-source bispectra
<!-- key: c2-foreground-and-point-source-bispectra -->

Unclustered point sources and the CIB have their own bispectra, fitted jointly (arXiv:2504.00884). Validation: stability across component-separation methods and consistency with Minkowski functionals (arXiv:1502.01592).

### C3. Fidelity of the simulations
<!-- key: c3-fidelity-of-the-simulations -->

Errors and the linear term come from simulations. Planck 2015 polarisation results were labelled preliminary because the simulated noise did not match the data (arXiv:1502.01592); PR4 simulations have a systematically low lensing bispectrum, shown to be harmless (arXiv:2504.00884).

### C4. Template dependence and look-elsewhere
<!-- key: c4-template-dependence-and-look-elsewhere -->

A null result for three templates is not a null result for all shapes; scans over oscillatory or collider templates need a look-elsewhere correction (2.4σ after correction, arXiv:2511.17500). [src: abstract]

## D. Non-Gaussianity from large-scale structure
<!-- key: non-gaussianity-from-large-scale-structure -->

### D1. The response b_φ
<!-- key: d1-the-response-bphi -->

- **Mechanism.** The signal is f_NL · b_φ; b_φ depends on how the tracer was selected, not only on its linear bias.
- **Size.** For the same BOSS data, the strongest bound is f_NL = 16 ± 16 and the loosest 230 ± 226 as the b_φ(b_1) relation is changed (arXiv:2205.05673) [src: abstract], and σ(f_NL) is 19, 44 or 165 for the highest-concentration third, all, or the lowest-concentration third of haloes (arXiv:2209.07251) [src: abstract]. For DESI DR1 the central value moves from −3.6 to +3.5 between p = 1.6 and p = 1 for quasars (arXiv:2411.17623) [src: abstract]; Quaia also depends on the assumed response (arXiv:2504.20992).
- **Mitigation.** Simulation-based priors on p for the selected sample (p̄ ≃ 1.4 for DESI-like quasars in IllustrisTNG, checked against CAMELS; arXiv:2602.12357 [src: abstract]); reporting f_NL for more than one p.
- **Warning.** Marginalising b_φ with a wide prior is not conservative: it biases f_NL through projection effects (arXiv:2205.05673).
- **Cite.** arXiv:0805.3580, arXiv:2205.05673, arXiv:2209.07251, arXiv:2602.12357.

### D2. Large-scale imaging systematics
<!-- key: d2-large-scale-imaging-systematics -->

- **Mechanism.** Stellar density, extinction, depth and seeing modulate the target density on the same scales as the 1/k² signal; excess large-scale power mimics a non-zero f_NL, and over-correction removes signal.
- **Size.** For eBOSS DR16 the optimal analysis improved the error by 10% where a Fisher forecast predicted more, which its authors read as "still unknown systematic effects in the data" (arXiv:2309.15814) [src: abstract]. SPHEREx allocates δn/n < 0.2% rms per dex to spurious clustering to reach Δf_NL < 0.5 (arXiv:2511.02985) [src: Sect. III.2].
- **Mitigation.** Regression or neural-network weights against imaging templates (arXiv:2106.13725); an angular integral-constraint term in the window to account for the modes removed by the weights (arXiv:2411.17623); cross-correlation between tracers (arXiv:2604.05213) or with CMB lensing (arXiv:2512.17865), which do not share these systematics.
- **Validation.** Mocks that reproduce the target selection with contamination injected and removed (EZmocks, arXiv:2106.13725); blinded validation (arXiv:2411.17623); the spectroscopic DESI quasar auto-spectrum shows no excess large-scale power, unlike photometric quasar samples (arXiv:2512.17865).

### D2b. DESI DR1 LRG + QSO budget as read
<!-- key: d2b-desi-dr1-lrg-qso-budget-as-read -->

Chaussidon et al. 2024, arXiv:2411.17623. Model: P(k, μ) with b_1 + b_φ f_NL/T_Φ→δ(k) + f μ², a Lorentzian damping Σ_s and residual shot noise, monopole and quadrupole (Eqs. 2–6); b_φ = 2δ_c(b_1 − p), δ_c = 1.686, p = 1 (LRG), p = 1.6 (QSO, "all the quasars have a recent merger history which it is not known") (Eq. 7); fit either f_NL or the product b_φ f_NL [src: Sect. 2; Sect. 4.2.1].

| Item | Treatment | Size, as % of σ_stat (LRG / QSO) | Place |
|---|---|---|---|
| Scale range | k_min = 0.003 h Mpc⁻¹ (QSO), raised to 0.006 for LRG because of an uncorrected residual systematic; k_max = 0.08 h Mpc⁻¹ | — | [src: Sect. 4.2.1; App. A.2] |
| Imaging weights w_sys | linear or random-forest regression at HEALPix level (regressis) on 12 maps: Gaia stellar density, HI, two E(B−V) differences, PSF and galaxy depths, seeing | 22% / 38% (spread of f_NL across weight choices; 0.22σ and 0.38σ) | [src: Sect. 5.1.1; Sect. 6.3, Table 11] |
| Geometry (window, wide angle) | validated on 1000 EZmocks | 34% / 26% | [src: Table 11] |
| Radial integral constraint | in the window | 6% / 20% | [src: Table 11] |
| Angular integral constraint (modes removed by w_sys) | in the window | 6% / 6% | [src: Table 11] |
| Total, in quadrature | neglected in the quoted errors | +8% / +12% on the error | [src: Sect. 6.3, Eq. 52] |

Imaging weights remain "the most important source of the systematics" [src: Sect. 6.3].

### D2c. eBOSS DR16 quasar budget as read
<!-- key: d2c-eboss-dr16-quasar-budget-as-read -->

Mueller et al. 2021, arXiv:2106.13725: 0.8 < z < 2.2, monopole to k = 0.121 h Mpc⁻¹ in 63 bins of Δk ≈ 0.019 h Mpc⁻¹, NGC and SGC with separate bias, shot-noise and velocity-dispersion nuisances, p = 1.6 by default [src: Table 1]. All 68% unless stated [src: Sect. 8.1 and its table; Sect. 8.3].

| Variation | f_NL | Place |
|---|---|---|
| Baseline: neural-network imaging weights (Gaia stellar template), redshift + FKP weights (P_0 = 20,000 h⁻³ Mpc³, z_eff 1.51 → 1.82) | −33 < f_NL < 10 (95%: −51 to 28); maximum likelihood −12 | [src: Sect. 8.1] |
| Linear imaging weights (BAO default) | −50 < f_NL < 10; maximum likelihood −26; "not robust" | [src: Sect. 8.1, table] |
| No optimal weights (NN) | −28 < f_NL < 31: optimal weights tighten by 37% | [src: Sect. 8.1] |
| Linear weights without optimal weights | maximum likelihood shifts by almost 4σ, a sign of low-redshift contamination | [src: Sect. 8.1] |
| p = 1 instead of 1.6 | −18 < f_NL < 11; same maximum likelihood, error 80% tighter; σ ranges 14–21 with p | [src: Sect. 8.1] |
| Over-subtraction by the weights, from contaminated mocks | Δf_NL = −12, i.e. f_NL = 0 ± 21 (stat.) ± 12 (sys.); not applied | [src: Sect. 8.3] |

Any weighting removes large-scale modes and pushes f_NL negative [src: Sect. 8.3].

### D2d. Quaia (photometric quasars × Planck lensing) as read
<!-- key: d2d-quaia-photometric-quasars-x-planck-lensing -->

Fabbian et al. 2025, arXiv:2504.20992, 68%, p_φ = 1 unless stated [src: Sect. 3.3; Sect. 4.2, Eqs. 37–40 and the table of analysis settings].

| Variation | f_NL |
|---|---|
| Fiducial: C_ℓ^gg (ℓ > 15) + C_ℓ^κg (ℓ ≥ 2), systematics deprojected | −20.5 +19.0/−18.1 |
| p_φ = 1.6 | −28.7 +26.1/−24.6 |
| C_ℓ^κg only (p_φ = 1; 1.6) | −13.8 +26.7/−25.0; −15.6 +42.3/−34.8 |
| C_ℓ^gg only | −61.8 +37.0/−35.6 |
| No deprojection of imaging templates | −13.5 +19.0/−18.7 |
| ℓ_min^gg = 10 | −17.7 ± 19 |
| ℓ_min^κg = 4; 10 | −29.0 ± 20; −38.2 ± 24 |
| G < 20 sub-sample | −12.1 +27.2/−25.0 |

The ℓ ≤ 15 cut of the auto-spectrum comes from simulations: bins whose shift under deprojection has PTE < 5% against systematics-free simulations are removed (ℓ = 6 has PTE < 1%); no κg bin fails, and the quasar dipole must be deprojected (Y_10, Y_1±1) to avoid leakage through the mask (arXiv:2504.20992) [src: Sect. 3.3, Fig. 7].

### D2e. DESI DR1 quasars × Planck PR4 lensing as read
<!-- key: d2e-desi-dr1-quasars-x-planck-pr4-lensing-as -->

Chiarenza et al. 2025, arXiv:2512.17865, baseline p = 1.6, three bins over 0.8 < z < 3.5, 68% [src: Sects. 5.2, 7.3–7.4, Tables 9–10].

| Variation | f_NL |
|---|---|
| Baseline (regressis linear weights) | 2 +28/−34 |
| Third bin (2.5 < z < 3.5) dropped: its ℓ = 6.5 bin is > 2σ off and its bias amplitude ≈ 3σ from 1 | −15 +29/−35 (0.5σ shift, same error) |
| Constant bias per bin; linearly interpolated b(z) | −3 +28/−35; 2 +28/−33 |
| A_s and n_s free with Planck 2018 Gaussian priors | 1 +33/−36 |

Neural-network weights are not used because their over-correction of large-scale modes is "particularly severe"; the residual mode removal of the two linear schemes is measured on 500 systematics-free lognormal mocks (GLASS) of the DR1 footprint and corrected (arXiv:2512.17865) [src: Sect. 5.2].

### D3. Window function and integral constraints
<!-- key: d3-window-function-and-integral-constraints -->

Estimating the mean density and the radial selection from the data removes large-scale modes. DESI corrects the window for the radial integral constraint (arXiv:2411.17623). An error here is degenerate with f_NL.

### D4. Redshift errors and tomographic bin mismatch
<!-- key: d4-redshift-errors-and-tomographic-bin-mismatch -->

For a SPHEREx-like photometric analysis, galaxies assigned to the wrong redshift bin produce apparent tensions of 3–6σ on f_NL^local and 9–12σ on the bias; a scattering-matrix formalism removes the bias in simulations (Saraf and Parkinson 2024, arXiv:2412.03078) [src: abstract].

### D5. Bias parameters and scale cuts in bispectrum analyses
<!-- key: d5-bias-parameters-and-scale-cuts-in-bispectrum -->

Equilateral and orthogonal constraints depend on the priors of the non-linear bias parameters: 940 ± 600 with everything free against 260 ± 300 with quadratic bias and cosmology fixed (arXiv:2201.07238) [src: abstract]; simulation-based priors tighten DESI + BOSS to 200 ± 230 (arXiv:2512.04266) [src: abstract]. A referee asks for the scale cuts, the validation on simulations with known f_NL, and the result without the informative priors.

### D6. Covariance approximations in forecasts
<!-- key: d6-covariance-approximations-in-forecasts -->

The SPHEREx forecast omits the non-Gaussian covariance and the power spectrum–bispectrum covariance, worth "tens of percent" (arXiv:2511.02985). Euclid's σ(f_NL^local) = 2.2 assumes universality and k_max = 0.15 h Mpc⁻¹ (arXiv:2507.15819) [src: abstract].

### D7. Relativistic and wide-angle effects
<!-- key: d7-relativistic-and-wide-angle-effects -->

General-relativistic and wide-angle terms contribute on the same large scales as the f_NL signal. No quantified result was read this session; listed under "Not verified".

### D8. Cluster counts
<!-- key: d8-cluster-counts -->

The ACT cluster f_NL depends on the mass calibration: the analysis finds a 16.4% residual mass bias "heavily informed by our adopted priors", with negligible effect on f_NL at the present error (arXiv:2602.03917) [src: abstract].

## E. Isocurvature
<!-- key: isocurvature -->

- **Prior-volume effects.** With a flat prior on the isocurvature tilt, an unconstrained amplitude leaves a large volume at extreme tilts; Planck and ACT sample amplitudes at two scales instead (arXiv:2503.14454).
- **Correlation with n_s.** The scale-invariant CDI limit weakens from 0.9 to 1.1 (× 10⁻¹⁰) when ACT is added because n_s rises (arXiv:2503.14454) [src]. Isocurvature limits inherit the data-combination dependence of section A1.
- **Lensing-like smoothing.** Compensated isocurvature produces extra smoothing at high ℓ, like A_L (arXiv:1807.06211); the Planck 68% interval Δ²_rms = 0.0037 +0.0016/−0.0021 (arXiv:1807.06211) [src: Sect. 9.5; Sect. 11] is not a detection.
- **Non-linear modelling.** HMCode can fail for blue-tilted spectra (arXiv:2503.14454).

## F. Spatial curvature
<!-- key: spatial-curvature -->

- **A_L and likelihood.** The Planck-only preference for Ω_K < 0 has the same origin as A_L > 1 and changes with the likelihood (−0.044 +0.018/−0.015 with Plik, −0.037 +0.019/−0.014 with CamSpec, TT,TE,EE + lowE; arXiv:1807.06209) [src: Sect. 7.3]. Quote release and likelihood.
- **Combining discordant data.** Planck alone and BAO were in 2.5 to 3σ tension in the curved model (arXiv:1908.09139) [src: abstract]; combining them hides that. The same holds today for CMB and DESI in ΛCDM.
- **Model dependence at late times.** Ω_K from BAO and supernovae depends on the dark-energy model: an open preference in ΛCDM, Ω_K = 0.049 ± 0.037, disappears in extended models (arXiv:2604.23492) [src: abstract]; with w0wa free DESI + CMB + SNe give 10³Ω_K = 1.1 ± 1.3 (Pantheon+), 0.6 ± 1.3 (Union3) and 0.8 ± 1.3 (DESY5) (arXiv:2503.14738) [src: Table 5 (Sect. VI)].
- **Supernova sample.** The late-time open preference ranges from 2σ to 5σ with the supernova compilation (arXiv:2512.19565).

## G. Primordial features
<!-- key: primordial-features -->

- **Look-elsewhere.** Local Δχ² of −10 to −15 corresponds to at most 2.6σ globally (arXiv:2605.30236) [src: abstract].
- **Fixed cosmology.** A 3σ logarithmic feature in DESI DR1 at fixed Planck cosmology disappears when the cosmology is varied (arXiv:2610.10530).
- **Likelihood version.** Planck PR3 hints shrink with PR4 CamSpec (arXiv:2605.30236).
- **BAO degeneracy and non-linear damping.** Frequencies near the BAO one are poorly constrained; the damping must be modelled consistently (arXiv:1906.08758, arXiv:2610.10530).
- **Binning.** Binned likelihoods erase high-frequency oscillations (arXiv:2605.30236).

## H. Cosmic birefringence
<!-- key: cosmic-birefringence -->

- **Polarisation-angle calibration.** EB measures α + β. Planck's raw angle uncertainty is the systematic that the Minami–Komatsu method removes (arXiv:2011.11254); ACT relies on optics-model priors, and its result is conditional on them (arXiv:2509.13654, arXiv:2608.06480). Target for hardware calibration: 0.08° for the SO SATs (**forecast**, arXiv:2606.11300) [src: abstract].
- **Intrinsic EB of Galactic dust.** The foreground-based calibration assumes the foreground EB is known. β decreases as the Galactic mask grows (arXiv:2201.07682); a dust-robust variant of the ACT + Planck analysis gives 3.5σ instead of 4.8σ (arXiv:2608.06480) [src]. Body-level, Planck PR4 (arXiv:2201.07682) [src: Sects. V–VI]: β = 0.30° ± 0.11° at f_sky = 0.93; dropping one channel gives 0.34 ± 0.12 (no 100 GHz), 0.38 ± 0.12 (no 143), 0.27 ± 0.13 (no 217), 0.08 ± 0.21 (no 353), so the 353 GHz cross-spectra carry most of the signal. A dust EB acts as an effective angle γ_ℓ, so foreground calibration returns β − γ; with r^TB,dust ≈ 0.05 and a filament–field misalignment ψ_dust ≈ 5°, γ ≲ 0.7° for f_sky ≈ 0.7 (Eq. 1). The filament model C_ℓ^EB,dust = A_ℓ C_ℓ^EE,dust sin(4ψ_ℓ^dust), with A_ℓ free in four ℓ bins over 51–1490 (Eq. 2), brings β back to positive values for all masks. Known instrumental systematics in the NPIPE simulations shift β by −0.009° ± 0.003°, negligible against 0.11° [src: Sect. IV].
- **Intensity-to-polarisation leakage.** Marginalised in the ACT analysis (arXiv:2509.13654).
- **Omitted systematic in a quoted error.** 0.30 ± 0.05 excludes the angle systematic (arXiv:2507.16714, abstract).
- **Self-calibrated experiments.** BICEP/Keck constrains only β(ℓ) variations (arXiv:2603.06812). SPT-3G likewise rotates its maps to null TB and EB (section B10).

### H1. ACT DR6 birefringence: miscalibration-angle treatment as read
<!-- key: h1-act-dr6-birefringence-miscalibration-angle -->

Diego-Palazuelos and Komatsu 2025, arXiv:2509.13654. Five array-bands, each with its own α_i and a zero-mean Gaussian prior from the ACT optics model; EB and TB jointly, ℓ from 600–1000 (by band) to 7525; dust EB and TB neglected because at ℓ ≥ 600 behind the extended Planck 70% mask the spectra are CMB- and noise-dominated and the method does not use foregrounds to break α + β [src: Sect. III, Eq. 1, Table 1].

| Variation | β (deg, 68%) | Place |
|---|---|---|
| Fit of ψ_i = α_i + β only (EB, four bands): weighted mean | 0.192 ± 0.032 (ACT team: 0.20 ± 0.03 before systematic errors, 0.20 ± 0.08 with the optics calibration error) | [src: Sect. IV; Sect. I] |
| Independent priors on α_i | 0.204 ± 0.058 | [src: Table 2] |
| 90% correlated priors within an optics tube (PA) | 0.212 ± 0.072 | [src: Table 2] |
| 90% correlated per frequency | 0.212 ± 0.072 | [src: Table 2] |
| Same three, with residual I→P leakage γ_i marginalised | 0.208 ± 0.059; 0.215 ± 0.074 (headline); 0.216 ± 0.073 | [src: Sect. V, Table 3] |

Fitted |γ_i| ≤ 0.08%, against the 0.3% leakage correction already applied to the maps; marginalising γ shifts α_i by ≤ 0.21σ and β by ≤ 0.07σ (arXiv:2509.13654) [src: Sect. V]. Dropping off-diagonal covariance shifts best fits by ≤ 0.01°; the data tighten α_i over the optics prior by 20–37% for PA5 and PA6 [src: Sect. IV]. An unexplained PA5 f150 − f090 angle difference of 0.21° ± 0.09° is why the prior choice matters [src: Sect. IV].

### H2. ACT + Planck joint birefringence: how β moves (as read)
<!-- key: h2-act-planck-joint-birefringence-how-beta -->

Eskilt 2026, arXiv:2608.06480, 68%, in degrees [src: Sect. III].

| Subset or variation | β | Calibrates α by |
|---|---|---|
| ACT × ACT (EB only, no TB, diagonal covariance) | 0.207 ± 0.073 | ACT optics priors |
| Planck × Planck, nearly full sky, filamentary dust-EB model | 0.387 ± 0.094 (1.5σ from ACT-only) | Galactic foregrounds |
| ACT × Planck (600 < ℓ < 2000) | 0.178 ± 0.078 (2.3σ) | ACT priors, about 3 times tighter than the HFI ones |
| Joint baseline | 0.277 ± 0.057 (4.8σ) | both |
| Planck on a 30% Galactic cut (f_sky = 0.62), ℓ > 600, without 30, 44, 353 GHz ("dust-robust") | 0.236 ± 0.067 (3.5σ) | mostly ACT priors |
| No Planck α priors (HFI ones are pre-flight) | 0.280 ± 0.059 | ACT priors + foregrounds |
| No α priors at all | 0.442 ± 0.098 | foregrounds only |

Joint χ² = 89.1 for 73 degrees of freedom (PTE 9.7%); ACT × ACT alone has PTE 0.1%, partly from a poor fit near ℓ ≈ 1800–1900 already noted by the ACT team. Planck prefers α + β ≈ 0.30°, ACT ≈ 0.20° (arXiv:2608.06480) [src: Sect. III].

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

- Quantified synchrotron residuals for r beyond BK18 (closed for BK18 in section B9).
- Relativistic and wide-angle contributions to the large-scale power spectrum in f_NL analyses (only titles of 2025–2026 papers were seen).
- Stellar-contamination requirements for SPHEREx beyond the δn/n allocation.
- BICEP/Keck gain and ground-pickup budgets, and the BK18 polarisation-angle procedure (the BK18 additive and bandpass budget is now in section B9).
- The estimator dependence of the PR4 f_NL reanalysis (arXiv:2504.00884 has no HTML rendering; not read).
- E-to-B leakage from partial sky and filtering in ground-based B-mode analyses: no paper read.
- Systematics of the Planck low-ℓ polarisation that enter r < 0.032 (arXiv:2112.07961) [src: abstract].
