# Lyman-alpha forest — systematics

Scope: the canonical systematic effects of Lyα forest analyses (3D correlations and BAO/AP, P1D, tomography), each with mechanism, measured size where a paper quantifies it, standard mitigation, validation test and the reference a referee expects.
Snapshot: 2026-10-14

Flags: `[src]` read this session in the cited paper (abstract unless a section is named); `[der]` derived here; `[sec]` secondary.

The effects are grouped by where they enter: (A) from the quasar and the spectrum to the delta field, (B) astrophysical contaminants of the absorption, (C) instrument and pipeline, (D) modelling of the two-point functions, (E) simulation and emulator systematics for P1D, (F) tomography.

## A. From spectrum to delta field
<!-- key: from-spectrum-to-delta-field -->

### A1. Continuum fitting and the distortion of correlations
<!-- key: a1-continuum-fitting-and-the-distortion-of -->

- **Applies to:** both (3D: distortion of the correlation function; P1D: continuum-fitting bias).
- **Mechanism.** The unabsorbed quasar continuum is not known pixel by pixel in low-S/N survey spectra. Survey pipelines fit, per forest, a template times a low-order function, which removes the mean and slope of δ along each line of sight. This suppresses large-scale radial modes and couples every pixel of a forest to every other one, distorting the measured correlation function.
- **Size.** Power-law extrapolation or mean-spectrum continua in SDSS-like data reach no better than ~10–15% rms; mean-flux-regulated PCA reaches 8% rms at S/N ~ 2 and < 5% at S/N > 5 (Lee et al. 2012, arXiv:1108.6080) [src]. The CNN predictor LyCAN reaches a median forest-region error of 1.5% on DESI mocks and 4.1% on real COS spectra (arXiv:2405.06743) [src]. On high-resolution spectra, spline continua are biased low by < 1% at z = 2, 4% at z = 3, 12% at z = 4 (arXiv:0710.4522) [src].
- **Mitigation.** For 3D analyses: the *distortion matrix*, which applies to the model the same linear projection that the continuum fit applied to the data; in use since the final BOSS release (arXiv:1702.00176; test paper arXiv:2506.15262) [src]. For P1D: a continuum-fitting bias correction derived from synthetic spectra, needed for both FFT and QMLE (arXiv:2509.13593) [src]; QMLE additionally marginalises continuum-error modes (arXiv:2008.06421) [src]. For P3D: mode marginalisation in the optimal estimator, which removes the distortion at the cost of inflated large-scale errors (arXiv:2503.15619) [src].
- **Residual in the data.** In DR2 the best-fit model lies above the auto-correlation on average at 30 < r < 80 h⁻¹Mpc and μ < 0.95; the collaboration suspects imperfect modelling of separations < 30 h⁻¹Mpc leaking to larger separations through the continuum-fitting distortion. This is why the fit range was cut at 30 h⁻¹Mpc, and why broadband-polynomial variations are run as a check (arXiv:2503.14739, Sect. 4.2) [src].
- **Validation.** Busca et al. 2025 tested the distortion matrix on mocks: percent-level effects on the forest bias parameters may remain, but "the determination of the BAO peak position is not affected at the percent level" (arXiv:2506.15262) [src].
- **Referee expects:** arXiv:1702.00176 for the method, arXiv:2506.15262 for its test, arXiv:2306.06312 for the DESI weighting scheme.

### A2. Mean transmission and the amplitude degeneracy
<!-- key: a2-mean-transmission-and-the-amplitude -->

- **Applies to:** P1D (amplitude inference); for the 3D correlations the continuum fit absorbs F̄(z).
- **Mechanism.** The fitted continuum absorbs the mean transmitted flux F̄(z); δ is defined relative to the product C × F̄, so the absolute F̄(z) is not measured by the survey δ field. In P1D inference F̄ is nearly degenerate with the linear-power amplitude.
- **Why the survey δ cannot fix it.** The per-forest polynomial of the continuum fit absorbs the redshift evolution of F̄(z) (arXiv:2503.14739, Sect. 2.4) [src].
- **Size.** In the Lyssa reanalysis of eBOSS DR14, the amplitude goes from A_Lyα < 7.6 (95%) to 9.8 ± 1.1 when an external F̄ prior is imposed, against a Planck value of 8.79 (arXiv:2412.05372) [src]. This single choice moves the result from "in tension with Planck" to "in accordance".
- **Mitigation.** External F̄(z) from high-resolution spectra (arXiv:0710.4522), from composites without continuum fitting (arXiv:1208.2584), or from continuum prediction redward of Lyα (arXiv:2405.06743); or free F̄(z) nuisance parameters per redshift.
- **Referee expects:** a statement of which F̄ prior was used and the result without it.

### A3. Weighting of pixels
<!-- key: a3-weighting-of-pixels -->

- **Applies to:** 3D correlations.
- **Mechanism.** Pixel weights combine pipeline noise and the intrinsic forest variance. A wrong balance loses precision and, if the variance model is wrong, biases covariance estimates.
- **Size.** The DESI EDR weighting change improved the precision of the correlation function by more than 20% (arXiv:2306.06312) [src].

### A4. Blinding
<!-- key: a4-blinding -->

- **Applies to:** both.
- **Practice.** DESI DR1 BAO was developed "on a blinded dataset" (arXiv:2404.03001) [src]; the DR1 full-shape variations "were first performed blinded" (arXiv:2509.15308) [src]; the DR2 full-shape validation "was completed prior to unblinding" with quantitative requirements defined beforehand (arXiv:2607.27411) [src]; the DR1 P1D cosmology kept "cosmological parameters blinded throughout the validation process" (arXiv:2601.21432) [src].
- **Method paper.** A catalogue-level AP blinding scheme shifts each forest in wavelength after continuum fitting and changes QSO redshifts consistently; it moves the BAO peak as expected for ~5% changes in the matter content without changing posterior shapes. Metals and Lyβ limit it in the 1D correlation function (arXiv:2607.07875) [src].

## B. Astrophysical contaminants
<!-- key: astrophysical-contaminants -->

### B1. High-column-density systems (DLAs, sub-DLAs, Lyman-limit systems)
<!-- key: b1-high-column-density-systems-dlas-sub-dlas -->

- **Applies to:** both.
- **Mechanism.** Systems with log N_HI > 17 (LLS) up to log N_HI > 20.2–20.3 (DLA) add broad damped Voigt wings. They trace halos (higher bias) and their wings suppress radial modes, which imprints a scale-dependent bias on the forest power spectrum (arXiv:2506.13005, arXiv:1711.06275) [src]. The first BOSS 3D measurement already attributed a low β to HCDs and metals (arXiv:1104.5244) [src]. Foundations: in P1D, damping wings add large-scale power and ignoring them underestimates the slope of the linear power (McDonald et al. 2005, arXiv:astro-ph/0407378) [src]; in 3D, HCDs add noise, raise the measured density bias and lower β_α, with correction formulae in terms of the mean effective optical depth and host-halo bias of the HCDs (Font-Ribera & Miralda-Escudé 2012, arXiv:1205.2018) [src].
- **Mitigation.** (i) Identify and mask DLAs, and correct the wings: CNN catalogue for eBOSS DR16 (arXiv:2107.09612), Gaussian-process catalogue for DR16Q (arXiv:2103.10964), and for DESI DR2 a combination of a template-fitting "DLA Toolkit", a CNN and a GP finder (arXiv:2503.14740) [src]. (ii) Model the unmasked remainder in the correlation function: the Voigt model (linearly biased HCDs convolved with Voigt profiles, integrated over the column-density distribution) of Rogers et al. 2018, recommended over top-hat approximations and valid to |k| < 1 h/Mpc (arXiv:1711.06275) [src]; tested on DESI-type mocks by Tan et al. 2025, who find it performs comparably to the ad hoc models of published analyses and stress that the HCD content and bias of real data are uncertain (arXiv:2506.13005) [src].
- **Size of finder imperfection.** DESI DR2 combined catalogue: about 85% pure and 79% complete for log N_HI > 20.3 in S/N > 2 spectra without BALs; the Toolkit alone 80% pure, 79% complete (arXiv:2503.14740) [src]. eBOSS DR16 CNN: > 90% completeness and purity for 20.1 ≤ log N_HI ≤ 22 in bright forests (arXiv:2107.09612) [src].
- **For P1D (DESI DR1).** Marginalising over LLS contamination inflates the errors on the compressed parameters by about 50%; the LLS parameters are strongly correlated with (Δ²_★, n_★), and the paper calls it "concerning that possible small deviations from the assumed functional form for LLS contamination could induce noticeable variations in the inferred parameters"; external priors on the LLS abundance would help (arXiv:2601.21432, Sects. 6.2 and 8) [src]. DLAs are identified by three finders, then modelled and masked (same paper, Sect. 2.1) [src].
- **For P1D (high resolution).** Small-scale P1D at k > 0.045 s/km is more sensitive to LLS contamination; a sample biased toward HCDs (archival KODIAQ-SQUAD) pushes the inferred primordial amplitude high (arXiv:2509.18271) [src]. McDonald et al. 2005 already found that damping wings raise the inferred slope of the linear power (arXiv:astro-ph/0407377) [src].
- **Where the gas sits (simulation).** In TNG50 at z ≃ 3, DLAs give way to sub-DLAs at impact parameter b ≈ 0.11 R_200c, sub-DLAs to LLSs at 0.3, LLSs to forest at 0.5; a single Voigt component recovers the column of damped systems but not of LLSs (arXiv:2609.19235) [src].
- **Validation.** Compare DLA-masking strategies on mocks and data (arXiv:2503.14741) [src]; fits with and without the HCD term; marginalisation over unidentified HCDs in the BAO error (already in arXiv:1702.00176 [src]).

### B2. Metal absorption
<!-- key: b2-metal-absorption -->

- **Applies to:** both (3D: displaced spurious peaks, Si II 1260 near the BAO scale; P1D: Si III and Si II oscillations and additive power).
- **Mechanism.** Absorption by other transitions at different redshift appears at the same observed wavelength. In 3D it produces spurious correlations displaced along the line of sight by the wavelength ratio; in P1D it adds oscillations (Si III–Lyα) and a smooth additive power from metals redward lines.
- **History.** McDonald et al. 2006 found "clear evidence for SiIII correlations with the Ly-alpha forest" and that "metals contribute significantly to the total power and have to be subtracted properly" (arXiv:astro-ph/0405013) [src].
- **Mitigation.** P1D: subtract the power measured in side bands redward of the Lyα emission line, and fit the Si III (and Si II) oscillation; DESI used red-side spectra for metal and noise-calibration systematics (arXiv:2306.06316) [src] and the 1D correlation function for new insight into metals (arXiv:2505.07974) [src]. High resolution: identify and mask narrow metal lines and restrict to k < 0.1 s/km, where the effect is "completely mitigated" (arXiv:1709.07354) [src]. 3D: include metal–Lyα and metal–QSO correlation templates in the model; DESI measured the auto-correlation of the transmission in low-z quasars where no Lyα forest exists and interpreted it with two components, pipeline noise and Si IV and C IV auto-correlations (arXiv:2404.03003) [src].
- **Size.** Metal contribution to the mean absorption ~6–9% at z = 3, decreasing with redshift as stated (arXiv:0710.4522) [src]. In 3D at z = 2.33, Si III(1207) and Si II(1190, 1193, 1260) produce spurious peaks at |Δr_∥| ≈ 21, 59, 52 and 104 h⁻¹Mpc; the last sits close to the BAO scale along the line of sight. DR2 best-fit metal biases are of order −3 to −7 × 10⁻³ for the silicon lines and −18.6 ± 4.9 × 10⁻³ for the effective C IV term, which is prior-dominated (arXiv:2503.14739, Sect. 3.2 and Appendix A) [src]. In the DR1 P1D cosmology, marginalising over Si II–Si II contamination alone inflates the compressed-parameter errors by about 20% (arXiv:2601.21432, Sect. 6.2) [src].
- **Si II–Si II.** The Si II–Si II line pair is "robustly detected" in the DESI DR1 1D correlation function and produces an oscillation that no cosmological, IGM or HCD parameter can mimic; its parameters are only weakly correlated with cosmology, but omitting it shifts the result (arXiv:2601.21432, Sect. 8) [src]. The DESI side band is 1268–1380 Å; lines below about 1300 Å overlap the forest and cannot be removed this way (same paper, Sect. 2.1) [src].
- **Turned into signal.** The C IV forest × QSO correlation gives a 3.0% BAO measurement at z_eff = 1.92 in DESI DR2 (arXiv:2601.08103) [src]. The Si III–Lyα correlation is visible in the 1D bispectrum (arXiv:2410.09150) [src].

### B3. Broad absorption line quasars
<!-- key: b3-broad-absorption-line-quasars -->

- **Applies to:** both (quantified here for BAO; for P1D the BAL mask also enters through C4).
- **Mechanism.** BAL troughs, blueshifted by up to ~0.1c, fall in the forest region and mimic absorption; BALs also perturb the quasar redshift.
- **Size.** 12–16% of quasars show BALs and were excluded in earlier analyses (arXiv:2111.09439) [src].
- **Mitigation.** Mask the expected trough locations and keep the quasar: this "returns over 95% of the pathlength" lost by exclusion (arXiv:2111.09439) [src]. DESI DR1 baseline: mask all pixels associated with all BAL features in the forest region; alternative strategies and finder incompleteness do not change the BAO result (arXiv:2405.09737) [src].

### B4. Fluctuations of the ionising background and the proximity effect
<!-- key: b4-fluctuations-of-the-ionising-background-and -->

- **Applies to:** 3D correlations (large-scale shape, BAO and full shape).
- **Mechanism.** The H I fraction depends on the local photo-ionisation rate; sources cluster, so Γ fluctuates on scales comparable to the mean free path. This makes b_δ and β scale dependent while keeping the product b_δ β fixed, and adds a shot-noise term from rare bright sources (Gontcho A Gontcho et al. 2014, arXiv:1404.7425) [src]. On scales beyond the mean free path the H I density anti-correlates with matter (Pontzen 2014, arXiv:1402.0506) [src].
- **Size.** Distortion of the correlation-function shape around the BAO peak, with the peak position shifting "only by 1.2 percent for a mean source bias of b_j = 3" in a linear radiative-transfer calculation (arXiv:1402.0506) [src]. This number predates DESI precision (0.65% isotropic) and is an upper-end model, not a measured shift.
- **Mitigation.** A UV-fluctuation term in the 3D model; BOSS DR12 marginalised over it (arXiv:1702.00176) [src]; the DESI DR2 full-shape analysis marginalises over the impact of UV background fluctuations (arXiv:2607.27411) [src].
- **Detected in DR2.** During the DR2 full-shape validation the scale-dependent UV bias was detected at ~3σ to ~5σ depending on the model setup and added to the baseline; b_Γ = 0.143 ± 0.047 at z_eff = 2.33 against a prediction of ≃ 0.13 at z = 2.25 from arXiv:1404.7425; it improves the fit but does not change AP significantly; source shot noise and He II reionisation terms gave no significant improvement (arXiv:2607.27410 [src: Sect. III.4]; arXiv:2607.27411 [src: Sect. III.4]). It does destabilise fσ8 (G7).
- **At z > 5** the fluctuations are large: homogeneous-UVB models are excluded at z ≥ 5.4 (arXiv:2108.03699) [src].

### B5. Relics of patchy reionisation
<!-- key: b5-relics-of-patchy-reionisation -->

- **Applies to:** both (sizes given for the 3D power and for P1D).
- **Mechanism.** Regions that reionised at different times keep different temperatures and pressure-smoothing for a long time, adding large-scale power correlated with the reionisation topology.
- **Size.** Deviation of the 3D power at k = 0.14 Mpc⁻¹ of 19–36% at z = 4, decreasing to 2.0–4.1% at z = 2; for P1D 3.3–6.5% at z = 4 and 0.35–0.75% at z = 2 (Montero-Camacho et al. 2019, arXiv:1902.02892) [src]. At 4.2 ≤ z ≤ 5: P1D suppressed by ~10% at k ~ 0.1 s/km and enhanced by 10–50% at k < 0.03 s/km relative to homogeneous-UVB models; no significant bias on thermal parameters at 10% measurement errors, ~1σ shifts at 5% errors (Molaro et al. 2022, arXiv:2109.06897) [src].
- **Mitigation.** Simulation-based correction templates (arXiv:2109.06897; suite arXiv:2207.13098); patchy H and He reionisation parameters in the emulator (arXiv:2306.05471); marginalisation over inhomogeneous reionisation in WDM fits (arXiv:2309.04533) [src].
- **Opportunity.** The same relics carry dark-matter information on large scales (**forecast**, arXiv:2605.26518) [src].

### B6. Helium reionisation
<!-- key: b6-helium-reionisation -->

- **Applies to:** P1D.
- **Mechanism.** He II reionisation at z ~ 3 heats the gas and flattens the temperature–density relation; patchy He II reionisation "imprints an excess in the 1D flux power spectrum on large scales" (arXiv:2306.05471) [src].
- **Evidence.** T_0 peak of 14 750 ± 1322 K and γ minimum of 1.225 ± 0.120 at z ≈ 3 (arXiv:2009.00016) [src]; UVB models reproduce it only with non-equilibrium evolution and photo-heating rates reduced by a factor ~0.7–0.8 (same) [src].
- **Consequence for P1D cosmology.** The thermal nuisance parameters are not smooth power laws through z ~ 3; PRIYA chains on eBOSS alone prefer a low level of He II heating and shift n_P when IGM temperature data are added (arXiv:2309.03943) [src].

## C. Instrument and pipeline
<!-- key: instrument-and-pipeline -->

### C1. Spectral resolution
<!-- key: c1-spectral-resolution -->

- **Applies to:** P1D.
- **Mechanism.** P1D is divided by the squared resolution window; an error δR/R on the resolution produces a k-dependent multiplicative error that grows as k².
- **Size.** DESI DR1: CCD image simulations of 675,000 quasars reveal biases at the highest k "corresponding to a resolution error of a few percent"; this sets the systematic budget, and no correction is derived because the simulation fidelity is insufficient (arXiv:2509.13593) [src]. XQ-100 has "large resolution corrections" and is therefore estimated separately from HIRES/UVES (arXiv:2108.10870) [src].
- **Scale cut that follows.** DESI DR1 cosmology uses k_∥ < 0.5π/R_z with R_z the pixel width in velocity units for 0.8 Å pixels, i.e. about 0.026–0.041 s/km over z = 2.2–4.2 [der, see `results.md` §3], and k_∥ > 10⁻³ s/km because of continuum-fitting errors (arXiv:2601.21432, Sect. 2.1) [src].
- **Mitigation and validation.** Per-pixel resolution matrix from the pipeline, validated with 2D image simulations of raw DESI exposures processed through the pipeline (arXiv:2306.06316) [src]; restrict k_max; marginalise a resolution nuisance per redshift bin in the cosmological fit.

### C2. Noise power
<!-- key: c2-noise-power -->

- **Applies to:** P1D.
- **Mechanism.** In low-S/N spectra the noise power is comparable to the signal at high k; a misestimated pipeline variance biases P1D additively.
- **History.** BOSS DR9 required "a novel treatment" of the noise level (arXiv:1306.5896) [src].
- **S/N cut as mitigation.** Restricting to forests with mean S/N > 3 per pixel instead of > 1 reduces the DR1 systematic errors by a factor 2.7 at the price of 25% larger statistical errors (arXiv:2601.21432, Sect. 2.1) [src].
- **Mitigation.** The cross-exposure estimator, which correlates independent exposures of the same quasar and "eliminates the need to model the pipeline noise" (arXiv:2505.07974; also used in the FFT measurement, arXiv:2505.09493) [src]; side-band calibration of the noise (arXiv:2306.06316) [src].

### C3. Correlated pipeline noise in 3D
<!-- key: c3-correlated-pipeline-noise-in-3d -->

- **Applies to:** 3D correlations.
- **Mechanism.** Sky-background subtraction and spectro-photometric calibration use fibres of the same exposure and spectrograph, so their errors are correlated between quasars observed together.
- **Size and form.** "An excess signal caused by the sky background subtraction noise is present in the lyman-alpha auto-correlation in the first line-of-sight separation bin" (Guy et al. 2025, arXiv:2404.03003) [src].
- **Mitigation.** A simple model term for sky-subtraction and calibration noise, isolated with synthetic data (arXiv:2404.03003) [src]; in DR2 a single amplitude a_noise for noise correlated between fibres of the same focal-plane petal, measured at 10⁴ a_noise = 2.20 ± 0.15 (arXiv:2503.14739, Appendix A) [src]; in eBOSS, modelling of "instrumental correlations" was one of the main improvements of DR16 (arXiv:2007.08995) [src]. DESI has an atmospheric dispersion corrector and bench-mounted spectrographs in a climate-controlled room, which improve spectro-photometric calibration, sky subtraction and wavelength calibration relative to SDSS (arXiv:2503.14739, Sect. 6.3) [src].

### C4. Masking (sky lines, DLAs, BALs) in Fourier space
<!-- key: c4-masking-sky-lines-dlas-bals-in-fourier-space -->

- **Applies to:** P1D (FFT estimator).
- **Mechanism.** Masked pixels convolve the FFT power with the mask window.
- **Consequence.** The DESI DR1 cosmological analysis uses the QMLE measurement "since these are not affected by masking systematics like FFT-based estimates" (arXiv:2601.21432, Sect. 2.1) [src].
- **Mitigation.** Masking-bias correction for the FFT estimator derived from 20 synthetic realisations (arXiv:2509.13593) [src]; QMLE handles masks by construction (arXiv:2008.06421) [src]; high-resolution pipelines correct "the bias induced by masking missing data, DLAs, and metal absorption lines" (arXiv:1709.07354) [src].

### C5. Quasar redshift errors
<!-- key: c5-quasar-redshift-errors -->

- **Applies to:** 3D correlations (mainly the Lyα × QSO cross-correlation).
- **Mechanism.** Broad emission lines give redshift errors of a few hundred km/s. Random errors smear the cross-correlation and the BAO peak radially; errors correlated with the emission-line shapes leak into the mean continuum and create a spurious correlation at small transverse separation (Youles et al. 2022, arXiv:2205.06648) [src]. A systematic offset shifts the cross-correlation along the line of sight.
- **Size.** In DESI early data the offset grew with redshift because the redshift templates mis-modelled the Lyα optical depth; new templates changed Δr_∥ from −1.94 ± 0.15 h⁻¹Mpc to −0.08 ± 0.04 h⁻¹Mpc, that is from −205 ± 15 km/s to −9.0 ± 4.0 km/s (Bault et al. 2025, arXiv:2402.18009) [src]. BAO peak position changes from random errors are negligible (arXiv:2205.06648) [src].
- **In the DR2 fit.** Δr_∥ = 0.53 ± 0.18 h⁻¹Mpc and σ_v = 3.18 ± 0.64 h⁻¹Mpc (arXiv:2503.14739, Appendix A) [src].
- **Mitigation.** A free Δr_∥ and a velocity-dispersion (finger-of-god-like) damping in the cross-correlation model (the marginalisation over "the non-linear velocity of quasars" in arXiv:1708.02225 [src]); improved templates; dedicated study in the DR2 validation (arXiv:2503.14741) [src].
- **Diagnostic.** The forest × galaxy cross-correlation measures redshift dispersion and offsets of galaxy samples (arXiv:2507.21852, arXiv:2509.07453) [src].

## D. Modelling of the 3D two-point functions
<!-- key: modelling-of-the-3d-two-point-functions -->

### D1. Non-linear BAO broadening and shift
<!-- key: d1-non-linear-bao-broadening-and-shift -->

- **Applies to:** 3D correlations (BAO).
- **Mechanism.** Non-linear growth and bulk flows damp the BAO feature anisotropically and shift its position at the sub-percent level.
- **Size.** From one-loop EFT parameters measured in ACCEL²: theoretical error budget of −0.2% (radial) and −0.3% (transverse) at z = 2, i.e. −0.3% isotropic and 0.1% anisotropic; for the cross-correlation −0.2% and −0.1% (arXiv:2412.06892) [src]. From AbacusSummit Lyα mocks with the DESI fitter: Δα_∥ = 0.35% at 3σ and no transverse shift for the auto-correlation; cross-correlation Δα_⊥ ~ −0.25% at 2σ (arXiv:2503.13442) [src]. The two studies agree on the size (a few tenths of a percent) and not on the sign of the radial shift.
- **Mitigation.** DESI DR2 added a theoretical systematic term Δα_∥ = Δα_⊥ = 0.3%, uncorrelated, to the covariance of the BAO parameters, rather than applying a correction, because the three available studies "have not converged on either the exact magnitude nor on the direction of the shift, and all three only detect the shift at about the ~3σ level"; the paper notes that an ALPT-based FGPA study found a 1% isotropic shift and the EFT study ~0.2% (auto) and ~0.1% (cross) at z = 2.33, and that the dependence of the EFT bias parameters on He II reionisation and UV fluctuations is unquantified (arXiv:2503.14739, Sect. 6.1) [src]. No reconstruction is applied to the Lyα field. A one-loop EFT model recovers unshifted BAO parameters (arXiv:2503.13442) [src].
- **Revised budget in the DR2 full-shape analysis.** Δα_p = 0.15% on the isotropic BAO scale and Δφ_p = 0.8% on the AP of the peak, because AbacusSummit and CoLoRe-2LPT mocks agree on a larger effect in the AP direction; the shift is at most about a third of the DR2 BAO statistical error and is not applied as a correction since EFT predictions from AbacusSummit mocks and from hydrodynamical simulations still disagree on its direction (arXiv:2607.27410, Sect. 5.2) [src].
- **Mocks.** Lognormal mocks do not broaden the peak; the DR1 validation named this as the top priority for the next mocks (arXiv:2404.03004) [src]; CoLoRe-QL (arXiv:2503.14741) and CoLoRe-2LPT (arXiv:2607.27412) address it [src]. In a hydrodynamical box (ACCEL², 640 h⁻¹Mpc) the BAO is clearly detected and its damping only marginally (arXiv:2407.04473) [src].

### D1b. Leakage of small scales through the distortion matrix
<!-- key: d1b-leakage-of-small-scales-through-the -->

- **Applies to:** 3D correlations (AP and full shape; BAO fit range).
- **Mechanism.** The continuum-fit projection mixes line-of-sight separations; undistorted correlations at r_∥ < 10 h⁻¹Mpc contribute to the distorted correlation at all separations, including those kept by a scale cut.
- **Size.** Percent-level bias on the Lyα AP parameter if ignored (arXiv:2607.27410, Sect. 3.3) [src]; for comparison the DR2 AP error is 1.0–1.1%.
- **Mitigation.** Analytic marginalisation of one amplitude per small-scale model bin (402 amplitudes in DR2), implemented as a covariance update (same section) [src].
- **Earlier symptom.** The broadband mismatch at 30–80 h⁻¹Mpc in the DR2 BAO fit was attributed to this effect (arXiv:2503.14739, Sect. 4.2) [src].

### D2. Small-scale non-linearity in full-shape fits
<!-- key: d2-small-scale-non-linearity-in-full-shape-fits -->

- **Applies to:** 3D correlations (full shape, P3D).
- **Mechanism.** The linear (Kaiser-like) model with empirical non-linear corrections fails below a scale that depends on the statistic.
- **Practice.** eBOSS full shape used r_min = 25 h⁻¹Mpc (arXiv:2209.12931) [src]; DESI DR2 analytically marginalises the undistorted model below r_min = 30 (auto) and 40 h⁻¹Mpc (cross) and fixes the Arinyo non-linear parameters to ForestFlow values calibrated on the DESI DR1 P1D (arXiv:2607.27411 [src: Sects. III.4, III.5]; arXiv:2607.27413) [src]. The Arinyo-i-Prats et al. fitting function describes hydrodynamical P3D to better than 5% up to k = 10 h/Mpc (arXiv:2205.00962) [src]; the one-loop EFT to below 2% up to k = 2 h/Mpc in ACCEL² (arXiv:2412.06892) and sub-percent to k = 3 h/Mpc at z = 2.8 in Sherwood (arXiv:2309.10133) [src].
- **Warning.** "Phenomenological flux power spectrum models, based on modulations of the linear-theory power spectrum, fail at the field level even on quasi-linear scales" (arXiv:2606.26234) [src]. The Kaiser approximation for Lyα × QSO differs from N-body mock measurements at small scales (arXiv:2305.08899) [src].

### D3. Growth rate from the forest
<!-- key: d3-growth-rate-from-the-forest -->

- **Applies to:** 3D correlations (full shape).
- **Finding.** fσ8 from the forest full shape fails validation: DESI DR1 measured it but did not use it "due to difficulties in its validation with mocks" (arXiv:2509.15308) [src]; in DR2 "mock studies reveal a significant bias in the inferred growth-rate parameter fσ8, leading us to exclude this measurement" (arXiv:2607.27411) [src]. Any text that quotes a Lyα fσ8 as a cosmological constraint contradicts the collaboration's own assessment.
- **Reason, in brief.** The forest's velocity-gradient bias b_η is a free parameter not fixed by a conservation law as for galaxies, so β does not give f directly; f enters only through b_η f σ8 (parameter combinations as in arXiv:2607.27413) [src].

### D4. Covariance matrix
<!-- key: d4-covariance-matrix -->

- **Applies to:** 3D correlations.
- **Practice.** Estimated from the data over HEALPix pixels, with the cross-covariance between the four correlation functions included since DESI (arXiv:2503.14739, Sects. 4 and 6.3) [src]; the DR2 baseline smooths it, and the multipole analysis shows that compressing to monopole and quadrupole gives a positive-definite covariance without smoothing, with finite-sample debiasing corrections (arXiv:2603.04281) [src]. Population tests on mocks check that BAO errors are well calibrated (arXiv:2404.03004, arXiv:2607.19619) [src]. eBOSS P3D used LyaCoLoRe mocks for the covariance (arXiv:2403.08241) [src].

## E. Simulation and emulator systematics for P1D inference
<!-- key: simulation-and-emulator-systematics-for-p1d -->

**Applies to:** P1D.

| Effect | Size | Citation | Flag |
|---|---|---|---|
| Resolution convergence | 20 h⁻¹kpc cells for 1% in flux statistics up to k = 10 h/Mpc (Nyx) | arXiv:1406.6361 | [src] |
| Box size / missing modes | L > 40 h⁻¹Mpc for sub-percent error | arXiv:1406.6361 | [src] |
| Splicing of boxes | accurate at the 10% level | arXiv:1406.6361 | [src] |
| Large-scale mode convergence of P3D (β) | controlled by resolution through mode coupling, not by box size | arXiv:2407.04473 | [src] |
| Eulerian vs SPH | ≲ 1% in P1D after tessellation-based density reconstruction; SPH kernels bias flux statistics, worst at z ~ 5 | arXiv:2207.05023 | [src] |
| Emulator interpolation | ≲ 1% (PRIYA); sub-percent (LaCE neural network, k_∥ = 0.1–4 Mpc⁻¹, z = 2–4.5); 1.5% for P1D and 3% for P3D (ForestFlow) | arXiv:2309.03943, arXiv:2305.19064, arXiv:2409.05682 | [src] |
| Galaxy-formation model dependence | training on IllustrisTNG and testing on SIMBA gives ~10% positive bias on σ_8 in an SBI test | arXiv:2603.13011 | [src] |
| UVB treatment | canonical UVB tables reionise and heat the IGM too early (z ~ 15) | arXiv:1607.04218 | [src] |
| Continuum-placement correction on high-resolution data | "uncertain", needed to match the flux PDF and power, particularly at z > 4 | arXiv:1605.03462 | [src] |

Emulator error is now part of the likelihood: in DESI DR1 it degrades the Δ²_★ and n_★ precision by 30% and 19%, and accounting for it inflates the compressed-parameter errors by about 25% relative to analyses that ignore it; earlier SDSS analyses did not include it (arXiv:2601.21432, Sects. 6.2 and 8) [src].

Thermal-history priors remain the dominant model dependence of WDM limits: 5.3 keV versus 3.5 keV with or without temperature jumps (arXiv:1702.01764) and 1.9 keV for deliberately cold histories (arXiv:1912.09397) [src]. Iršič et al. 2024 argue that this dependence has diminished thanks to independent thermal measurements and that the leading small-scale modelling systematics are now peculiar-velocity structure and inhomogeneous reionisation (arXiv:2309.04533) [src].

## F. Tomography-specific
<!-- key: tomography-specific -->

**Applies to:** neither the 3D correlations nor P1D: tomographic maps and void cross-correlations only.

- **Sightline sparsity and noise.** The map resolution is tied to the mean transverse sightline separation: 13 h⁻¹Mpc for 37 QSOs per deg² (arXiv:2004.01448) [src], 2.5 h⁻¹Mpc for CLAMATO (arXiv:1710.02894) [src]. Sparsity introduces systematics in critical-point statistics, especially in cross-correlations of points of mixed signature (arXiv:2201.02606) [src].
- **Void finder calibration.** Thresholds are calibrated on hydrodynamical simulations so that IGM voids correspond to matter voids (arXiv:1710.02612) [src]; purity and completeness must be quoted from mock observations with the same sightline sampling and noise (arXiv:2004.01448) [src].
- **The tomographic effect in void cross-correlations.** Because pixels lie along parallel lines of sight, the void–forest cross-correlation has an anisotropy of purely geometric origin that the RSD model has to include (arXiv:2203.11045) [src].
- **Breakdown of the transmission–density relation.** A galaxy protocluster at z = 2.30 shows no significant absorption in CLAMATO (arXiv:2303.07619) [src], and LATIS finds strong absorption without LBG overdensities (arXiv:2507.10949) [src]: tomographic maps are not unbiased density maps in the most extreme environments.

## G. Systematic budgets of the main analyses (paper bodies)
<!-- key: systematic-budgets-of-the-main-analyses-paper -->

One table per analysis; each entry gives the place read. "σ/3" is the DESI threshold: a shift below a third of the statistical error of the data set needs no further action.

### G1. DESI DR2 Lyα BAO (arXiv:2503.14739; mocks arXiv:2503.14741)
<!-- key: g1-desi-dr2-lyalpha-bao-arxiv-2503-14739-mocks -->

| Item | Size or practice | Place read |
|---|---|---|
| Validation threshold | recover α_∥ = α_⊥ = 1 within σ_DR2/3, i.e. 0.0038 (α_∥) and 0.0045 (α_⊥); larger biases "must be investigated, corrected, or incorporated into the systematic errors" | arXiv:2503.14741 [src: Sect. IV.1, Fig. 6 caption] |
| Mock suite | 300 CoLoRe-QL (input power with smoothed BAO peak, mimicking non-linear broadening) + 100 Saclay mocks; DR1 used 100 LyaCoLoRe + 50 Saclay | arXiv:2503.14739 [src: Sect. V.1] |
| Bias on stacked mocks, Δα_∥ | −0.0042 ± 0.0006 (CoLoRe-QL), −0.0074 ± 0.0010 (Saclay), −0.0052 ± 0.0005 (combined 400), "near the threshold" | arXiv:2503.14741 [src: Table 1] |
| Bias on stacked mocks, Δα_⊥ | 0.0005 ± 0.0008, 0.0031 ± 0.0012, 0.0012 ± 0.0006 (same order) | arXiv:2503.14741 [src: Table 1] |
| Bias on α_iso = α_⊥^(9/20) α_∥^(11/20) and φ = α_⊥/α_∥ | −0.0023 ± 0.0003 and 0.0065 ± 0.0010 (combined) | arXiv:2503.14741 [src: Table 1] |
| Origin of the α_∥ bias | quasar redshift errors smear the weak broad emission lines of the mean continuum during continuum fitting, creating spurious correlations; absent in raw mocks without continuum fitting and much reduced when redshift errors are added after continuum fitting; the mock implementation is "the most extreme version of this effect" | arXiv:2503.14739 [src: Sect. V.1]; arXiv:2503.14741 [src: Sect. IV.1] |
| Per-mock fits | 400 individual fits: residuals Δα/σ_α consistent with a unit Gaussian; χ² distribution higher than expected, attributed to the model at small scales, not to the covariance (better than with the DR1 mocks) | arXiv:2503.14741 [src: Sect. IV.2, Figs. 7–8] |
| Close-pair test | removing quasar–pixel pairs with θ < 20 arcmin and Δv < 4000 km/s mitigates the mock bias; on data the shift is within σ/3 | arXiv:2503.14739 [src: Sects. V.1, V.2] |
| Data splits | auto vs cross, region A vs B, North vs South imaging, high vs low S/N (split at S/N = 4.25 in 1420–1480 Å, chosen for equal BAO errors): all consistent | arXiv:2503.14739 [src: Sect. V.2, Fig. 10] |
| Analysis variations | DR1 configuration (r_min = 10), broadband polynomials, close-pair removal, free non-linear broadening instead of the LPT value: all shifts < σ/3; tests passed before unblinding and rerun after | arXiv:2503.14739 [src: Sect. V.2, Fig. 11] |
| Theory systematic added | 0.3% on each of α_∥, α_⊥ (non-linear shift; see D1) | arXiv:2503.14739 [src: Sect. VI.1] |
| Further variations (App. B) | estimation of δ (no C III recalibration, η_pip = 1, η_LSS = 3.5, 2.4 Å pixels); data cuts (λ_obs, λ_RF, z_QSO < 3.78, > 50 pixels, DLA mask only at S/N_red > 3, weak BALs only, no sharp-line mask); distortion matrix (to 200 h⁻¹Mpc, 2% of data, 4 h⁻¹Mpc bins, no redshift evolution); rebinning of δ: all within σ/3 except "only quasar targets", whose shift matches its larger change of sample size | arXiv:2503.14739 [src: App. B, Fig. 13] |

### G2. DESI DR1 Lyα BAO (arXiv:2404.03001)
<!-- key: g2-desi-dr1-lyalpha-bao-arxiv-2404-03001 -->

| Item | Size or practice | Place read |
|---|---|---|
| Blinding | correlation functions blinded by an additive correction mimicking a BAO shift; catalogue-level blinding rejected because sky lines and absorption lines close to Lyα made it hard to apply robustly | [src: Sect. 6.1] |
| Mock threshold | stacked-mock bias below one third of the blinded statistical error, ~0.005 (α_∥) and ~0.007 (α_⊥) | [src: Sect. 6.2.3] |
| Largest mock offset | Δα_∥ = −0.003 ± 0.0014, Δα_⊥ = +0.004 ± 0.0018 (100 LyaCoLoRe mocks); the two mock suites differ at the same level, so no correction | [src: Sect. 6.5] |
| Systematic adopted | a conservative 0.5% would raise the total α_∥ (α_⊥) error by 3% (2%) in quadrature; judged negligible, so **only statistical errors are reported** | [src: Sect. 6.5] |
| Broadband terms | move the best fit by less than a tenth of the statistical error | [src: Sect. 6.5] |
| Shifts beyond σ/3 | "only quasar targets" and "weak BALs" (data 11% and 8% less constraining, expected fluctuations 0.28σ and 0.33σ); an alternative quasar-redshift estimator masking λ < Lyα (rms Δz 443 km/s above z = 2, ~4.2 h⁻¹Mpc in pair separations, 2% of pixels moved across the rest-frame cuts) gives Δα_∥ = 0.001, Δα_⊥ = −0.013, against bootstrap fluctuations of 0.007 and 0.009 (1000 HEALPix bootstraps): judged statistical | [src: Appendix E] |
| Cross-covariance between the four functions | ignoring it underestimates the BAO errors by 10% | [src: Sect. 3.3] |
| Covariance validation | per mock, compressed BAO residual δ_α/σ_α with δ_α = (∂M ᵀC⁻¹∂M)⁻¹ ∂M ᵀC⁻¹ R and σ_α = (∂M ᵀC⁻¹∂M)^(−1/2) (Eqs. 14–15): rms 0.96 ± 0.05 (α_∥), 0.99 ± 0.06 (α_⊥) on LyaCoLoRe, 1.07 ± 0.07, 1.03 ± 0.07 on Saclay; 10% larger without the cross-covariance | [src: Sect. 6.2.2] |
| Error calibration | data BAO errors larger than in the DR1 mocks, which lack non-linear broadening of the peak; checked with 1000 Monte Carlo realisations of the data covariance | [src: Sect. 6.2.4, Fig. 9] |
| Priors on contaminants (Table 5) | informative only for b_CIV(eff) ~ N(−24.3, 1.5) ×10⁻³ and β_HCD ~ N(0.5, 0.09); all others uniform; best fits ×10³: Si II(1190) −4.50 ± 0.64, Si II(1193) −3.05 ± 0.63, Si II(1260) −4.02 ± 0.62, Si III(1207) −9.79 ± 0.68; b_HCD = −0.0563 (+0.0045/−0.0036), L_HCD = 6.51 h⁻¹Mpc; Δr_∥ = 0.066 ± 0.058 h⁻¹Mpc, σ_z = 3.67 ± 0.14 h⁻¹Mpc; ξ_0^TP = 0.395 ± 0.051; 10⁴ a_noise = 3.54 ± 0.16 | [src: Appendix B, Table 5] |
| Correlation with nuisance parameters | BAO parameters "not strongly correlated with any of the nuisance parameters" | [src: Appendix B, Fig. 14] |

### G3. eBOSS DR16 Lyα BAO (arXiv:2007.08995)
<!-- key: g3-eboss-dr16-lyalpha-bao-arxiv-2007-08995 -->

| Item | Size or practice | Place read |
|---|---|---|
| Mock validation design | 10 realisations of four contamination levels (raw; + continuum + noise; + metals; + HCDs + quasar redshift errors) for each of the four correlation functions; 90 more for two levels, to test biases ten times below the statistical error | [src: Sect. V.4] |
| Mean α on mocks, all four functions combined | raw 1.009 / 0.995; + continuum + noise 1.005 / 0.992; + metals 1.010 / 0.989; + HCDs + σ_v 1.005 / 0.998 (α_∥ / α_⊥, mean σ 0.019 / 0.023 at the last level) | [src: Table 4] |
| β_Lyα on mocks, all four functions combined | 1.628 (raw) → 1.553 (+ continuum + noise) → 1.464 (+ HCDs + σ_v): contaminants bias β, not α | [src: Table 4] |
| ρ(α_∥, α_⊥) on mocks | −0.572 (auto), −0.470 (cross), −0.615 (auto Lyβ), −0.347 (cross Lyβ); zero between different functions | [src: Table 5] |
| HCD masking | DLAs with log N_HI > 20.3 masked in data; in mocks, input HCDs above 20.3 corrected and pixels with > 20% absorption masked; detected versus input DLA parameters give "nearly identical results" | [src: Sect. V.4] |
| Alternative analyses | BAO stable once metals are in the model, also with broadband polynomials; bias parameters change with HCD and broadband terms; other quasar-redshift estimators move the cross-correlation BAO by ≤ 0.5σ; distortion matrix to 300 h⁻¹Mpc or on a finer grid has no important effect; only the two-redshift-bin split differs by ~1σ, as expected for independent samples | [src: Appendix D] |
| Errors reported | statistical only (abstract; see `results.md`) | [src] |

### G4. DESI DR1 P1D, FFT estimator (arXiv:2505.09493)
<!-- key: g4-desi-dr1-p1d-fft-estimator-arxiv-2505-09493 -->

Budget per (k, z) bin, all terms added in quadrature; P1D is then "dominated by systematic errors for most redshifts and wavenumbers", the statistical errors having dropped by a factor 2.6–3 relative to EDR [src: Sect. 6.2, Fig. 11].

| Term | Treatment and size | Place read |
|---|---|---|
| Noise level | removed from the budget: the cross-exposure estimator measures the noise from the data | [src: Sect. 6.2] |
| Resolution damping | σ = 2 k² Δλ σ_Δλ P1D, with a conservative 1% absolute error on the effective resolution Δλ (PSF stability) | [src: Sect. 6.2] |
| Resolution correction | multiplicative correction A_res from image simulations; error 30% of |A_res − 1| | [src: Sect. 6.2] |
| Metals | side-band (SB1) power subtracted via a fit; error equal to the statistical error of the side-band power | [src: Sect. 6.2] |
| Continuum fitting | multiplicative correction A_cont from DR1-like mocks; 30% relative error | [src: Sect. 6.2] |
| Masking (DLA, BAL with AI > 0, sky lines) | multiplicative corrections A_dla, A_bal, A_line; 30% relative error, 6% for BAL masking | [src: Sect. 6.2] |
| Undetected DLAs | ratio of masked to unmasked P1D fitted with the Rogers et al. 2018 form; 20% finder incompleteness assumed | [src: Sect. 6.2] |
| Undetected BALs | same method, 15% incompleteness | [src: Sect. 6.2] |
| Why 30% | the standard deviation of a uniform 0–100% shift of a correction; called "very conservative"; mock-to-mock scatter judged too small | [src: Sect. 6.2] |
| Correlations between k bins | not modelled in the measurement paper; deferred to the inference | [src: Sect. 6.2] |

### G5. DESI DR1 P1D, optimal (QMLE) estimator (arXiv:2505.07974)
<!-- key: g5-desi-dr1-p1d-optimal-qmle-estimator-arxiv -->

Five major systematics, budget shown per redshift bin after the continuum correction [src: Sect. 4.4, Fig. 4].

| Term | Treatment and size | Place read |
|---|---|---|
| DLAs | largest systematic on large scales; catalogue completeness and purity ~85%; error from a fit (Eq. 7) to the ratio of unmasked to masked P1D; a high-confidence catalogue gives results "entirely consistent" with the baseline | [src: Sect. 4.4.1, Fig. 5] |
| BALs | catalogue completeness ~80% at S/N > 2.5; unmasked-BAL effect ten times smaller than for DLAs; error for 20% incompleteness | [src: Sect. 4.4.2] |
| Continuum fitting | ≲ 1% bias on all scales, detected only on the stack of 20 DR1 mocks up to z = 3.8; corrected, 30% of the correction kept as a correlated error; tabulated as 10³ b_cont = a + b x with x = k/(0.009 s/km), e.g. 6.768 − 0.699x (z = 2.2), 6.206 − 0.101x (z = 3.0), 10.825 + 0.172x (z = 3.6), 7.599 − 0.059x (z = 3.8) | [src: Sect. 4.4.3; App. B, Table 3] |
| Resolution | image simulations of ~675,000 z > 2.3 quasars (150 tiles) find resolution biases b_res ≈ 1.5%, dominating at k ≳ 0.01 s/km; error b_res × 2k²R_z² P1D; for a fit, a free b_res with Gaussian prior σ = 1.5% | [src: Sect. 4.4.4] |
| Noise | pipeline-variance calibration errors that differ between CCD amplifiers; budget from 20 one-amplifier-removed jackknifes; a feature at k = 0.009 s/km follows a fixed 9.6 Å oscillation traced to CCD zero images | [src: Sect. 4.4.5, Fig. 6] |
| Cross-exposure version (xQMLE) | all terms except noise | [src: Fig. 4 caption] |

### G6. DESI DR1 Lyα full shape (arXiv:2509.15308)
<!-- key: g6-desi-dr1-lyalpha-full-shape-arxiv-2509-15308 -->

| Item | Size or practice | Place read |
|---|---|---|
| Blinding | random offsets added to φ_s and f inside the likelihood (σ = 0.02 from eBOSS for φ_s; forecast σ_f = 0.14); actual offsets −0.020 and +0.02; baseline choices and validation fixed blind | [src: Sect. II.4] |
| Mocks | the DR1 BAO suite: 100 LyaCoLoRe + 50 Saclay lognormal mocks; mock model drops sky residuals, C IV, transverse proximity and BAO broadening (absent from the mocks) and adds two smoothing parameters | [src: Sect. IV.1] |
| Scale cuts from mocks | scales below 20 h⁻¹Mpc bias φ_f by more than 2σ in both suites; fσ8 biased with cross-correlation scales below 35 h⁻¹Mpc (LyaCoLoRe); Saclay mocks consistent at 2σ only with both functions above 50 h⁻¹Mpc, through larger errors rather than a smaller shift | [src: Sect. IV.1] |
| Decision | taken before unblinding: only AP fully validated; fσ8 shown but not used, because the two mock suites disagree and the RSD of the cross-correlation relies on the auto-correlation calibration | [src: Sects. II.4, V] |

### G7. DESI DR2 Lyα full shape (arXiv:2607.27411, arXiv:2607.27410)
<!-- key: g7-desi-dr2-lyalpha-full-shape-arxiv-2607-27411 -->

| Item | Size or practice | Place read |
|---|---|---|
| Mocks | 400 CoLoRe-2LPT realisations (stack); AbacusSummit mocks as a cross-check; mocks lack UV fluctuations, C IV, sky residuals and proximity effect, so these terms are removed from the mock model | arXiv:2607.27411 [src: Sect. IV.2] |
| Threshold | one third of the DR2 statistical error, ~0.38% on φ_s for the adopted cuts | arXiv:2607.27411 [src: Sect. IV.2] |
| Scale cuts | φ_s within threshold for r_min ≥ 25 h⁻¹Mpc (auto) and ≥ 40 h⁻¹Mpc (cross) on CoLoRe-2LPT; AbacusSummit converges for r_min ≥ 30 jointly; adopted 30 (auto) and 40 (cross) | arXiv:2607.27411 [src: Sect. IV.2, Fig. 2] |
| Kaiser vs Arinyo small-scale terms | no significant difference on mocks; Arinyo q_1 consistent with zero | arXiv:2607.27411 [src: Sect. IV.2] |
| Mock biases | α_p and φ_s consistent with truth; φ_p biased by 0.6% at ~5σ on the stack, same sign and size as AbacusSummit, within threshold | arXiv:2607.27411 [src: Sect. VI.1] |
| fσ8 | 10% bias at ≫ 5σ on mocks, not removed by any reasonable model or scale-cut change; data error from the fitter ~40% larger than mock errors; unstable under modelling of α_s, proximity effect and UV fluctuations → de-scoped | arXiv:2607.27411 [src: Sects. IV.3, VI.1, App. C.1] |
| Population test | pulls of α_p, φ_p, φ_s close to a unit Gaussian (φ_p slightly shifted); fitter (Gaussian-approximated) errors slightly underestimate the RMS of best fits | arXiv:2607.27411 [src: Sect. IV.3, Fig. 6] |
| Consequence for the BAO budget | the non-linear shift is mainly anisotropic, so the full-shape paper replaces the isotropic 0.3% by Δα_p = 0.15% and Δφ_p = 0.8% (see D1) | arXiv:2607.27411 [src: Sect. VI.1]; arXiv:2607.27410 [src: Sect. 5.2] |

### G8. DESI DR1 P1D cosmology (arXiv:2601.21432)
<!-- key: g8-desi-dr1-p1d-cosmology-arxiv-2601-21432 -->

Contaminants are modelled multiplicatively on the emulator's Lyα-only P1D: P1D^cont = [(1 + C_Lyα–SiIII + C_Lyα–SiII + C_SiII–SiIII) C_HCD P1D^emu + C_SiII–SiII] C_res (Eq. 13); per redshift 8 metal, 5 HCD, 1 resolution and 6 emulator parameters, 20 in all; the model is evaluated on a k grid eight times finer and rebinned so that metal oscillations are not smoothed [src: Sect. 4.4].

| Term | Model and size | Place read |
|---|---|---|
| HCDs | four classes after Rogers et al. 2018 (LLS 1.6 × 10¹⁷–10¹⁹, sub-DLA 10¹⁹–2 × 10²⁰, small DLA 2 × 10²⁰–10²¹, large DLA > 10²¹ cm⁻²); C_HCD = 1 + f_norm + Σ f_i [a_i(z) e^(b_i(z) k_∥) − 1]⁻² with a, b fixed to Rogers et al. and f_i free; the DESI finder is ≃ 70% complete above 2 × 10²⁰ cm⁻² at S/N > 2, so LLSs, sub-DLAs and missed DLAs remain | [src: Sect. 4.2, Eq. 11] |
| Resolution | marginalised instead of put in the covariance: C_res = 1 + 2 f_res R_z² k_∥², one f_res per redshift (to absorb e.g. the blue–red channel transition), expected bias a few per cent | [src: Sect. 4.3, Eq. 12] |
| Effect on the errors | LLS, Si II–Si II and emulator errors inflate the compressed-parameter errors by ~50%, 20%, 25% (see B1, B2, E) | [src: Sects. 6.2, 8] |

## Referee checklist for a Lyα results section
<!-- key: referee-checklist-for-a-lyalpha-results-section -->

The two lists are separate because the systematics differ; the "Applies to"
tag of each subsection above says which list it feeds. Tomography (section F)
is in neither.

### 3D correlations (BAO, AP, full shape)
<!-- key: 3d-correlations-bao-ap-full-shape -->

1. Which estimator (pair-count ξ, multipoles, P3D), and was it cross-checked against a second one?
2. Continuum method and how its distortion is modelled (distortion matrix, mode marginalisation) (A1, D1b).
3. DLA and BAL treatment: finder, purity/completeness, masking threshold, residual HCD model (B1, B3).
4. Metals: metal templates in the correlation model (B2).
5. Correlated sky-subtraction and calibration noise between fibres (C3).
6. Quasar redshift errors: Δr_∥ and dispersion parameters in the cross-correlation (C5).
7. Non-linear effects: BAO-shift systematic term; r_min or small-scale marginalisation for full shape (D1, D1b, D2).
8. UV fluctuations and reionisation relics: included, marginalised, or argued negligible at the redshift and scale used (B4, B5).
9. Covariance: source (sub-sampling, mocks, analytic), smoothing, finite-sample corrections (D4).
10. Validation on mocks that contain the effect being marginalised (HCDs, metals, BAO broadening, redshift errors), with the number of realisations.
11. Blinding: what was blinded and when it was lifted (A4).
12. No fσ8 claim from the forest unless the mock bias is addressed (D3).

### P1D
<!-- key: p1d -->

1. Which estimator (FFT, QMLE), and was it cross-checked against the other?
2. Continuum method and its bias correction from synthetic spectra (A1).
3. Mean-flux treatment: free, or which external prior; result with and without (A2).
4. DLA and BAL treatment: finder, purity/completeness, masking, and the model for residual HCDs and LLSs (B1, B3, C4).
5. Metals: side-band subtraction and Si III/Si II terms (B2).
6. Resolution and noise: how validated (image simulations, cross-exposure), and the k_max that follows (C1, C2).
7. Masking correction for an FFT estimator (C4).
8. Reionisation relics and the He II thermal history: included, marginalised, or argued negligible at the redshift and scale used (B5, B6).
9. Covariance: source, regularisation, correlations between redshift bins.
10. Validation on synthetic spectra and image simulations, with the number of realisations.
11. Blinding: what was blinded and when it was lifted (A4).
12. For P1D cosmology: emulator, simulation suite, thermal-history parameterisation and priors, and whether the result holds with a second emulator (E).

## Not verified
<!-- key: not-verified -->

- Per-redshift numerical systematic budgets of the DESI DR1 P1D measurements: both papers show them as figures (FFT Fig. 11, QMLE Fig. 4), not tables; only the rules and the continuum-bias table were read.
- The blinding method of the DESI DR2 BAO analysis (the paper states that tests were passed before unblinding but the method was not found in the passages read).
- The Lorentzian form of the cross-correlation damping X_NL as an equation (not rendered in the DR1 full-shape HTML).
