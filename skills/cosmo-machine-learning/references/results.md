# Machine learning in cosmology — results

Scope: quantified performance of machine-learning methods in cosmology — emulator accuracy, information gains of neural summaries, challenge outcomes, robustness across simulators — with the history of the key numbers.
Snapshot: 2026-10-17

Flags: as in `physics-and-methods.md`.

## 1. Emulator accuracy
<!-- key: emulator-accuracy -->

Machine-learning-specific numbers only. Gravity-only N-body emulators
(EuclidEmulator2, BACCO, Mira-Titan, Aemulus) are compared in
`cosmo-simulations-mocks`; CosmoPower and EuclidEmulator2 error budgets in
likelihoods are in `cosmo-statistics-inference`.

| Emulator | Target | Accuracy stated | Range | Citation | Flag |
|---|---|---|---|---|---|
| CosmoPower, linear P(k) | Boltzmann-code linear matter power | 99% of test spectra within 0.1% | k in [10⁻⁵, 10] Mpc⁻¹, z in [0, 5] | arXiv:2106.03846 | [src: Sect. 3.2] |
| CosmoPower, non-linear correction | HMcode-2020 with c_min, η0 | 99% of test spectra within 0.4%; error grows for k ≳ 1 Mpc⁻¹ | same | arXiv:2106.03846 | [src: Sect. 3.2] |
| CONNECT | CLASS observables | posteriors differ from CLASS by typically 0.01–0.1σ | models tested in the paper | arXiv:2205.15726 | [src] |
| GokuNEmu (T2N-MusE) | matter power spectrum from the Goku suite | mean leave-one-out error reduced by more than five, worst-case by about eight, relative to the earlier Gaussian-process emulator | ten-parameter space | arXiv:2507.07184 | [src] |
| DarkEmulator2 | non-linear matter power spectrum | sub-percent to the particle Nyquist scale k_Ny ≃ 10 h Mpc⁻¹ for 1 h⁻¹Gpc boxes with 3000³ particles; highest-k predictions depend on resolution and shot noise | nine-parameter w0waν CDM | arXiv:2605.28596 | [src] |
| DarkEmulator2 against public emulators | ratio of non-linear P(k), 500 random cosmologies at z = 0 | EuclidEmulator2 dips by a few per cent near k ~ 1 h Mpc⁻¹ with σ8- and w0-dependent trends; BACCO agrees for k ≲ 0.1 h Mpc⁻¹ and drifts with Ω_m and σ8 at smaller scales; Mira-Titan IV shows a several-per-cent trough; Aemulus ν shows low-k excursions near w0 ≃ −1.5 that shrink at z = 0.2; Aletheia shows a percent-level offset; CsstEmulator departs by a few per cent at its highest k | overlap of each pair's parameter ranges | arXiv:2605.28596 | [src: Sect. 5.2.3] |
| PyBird-JAX | one-loop EFTofLSS P_ℓ(k) | 1.2 ms per evaluation on CPU, 0.2 ms on GPU; 3–4 orders of magnitude faster than PyBird; validated on large-volume simulations and BOSS, including cosmologies outside the training set | — | arXiv:2507.20990 | [src] |
| SPHEREx P_ℓ emulator | EFT multi-tracer multipoles | median Δχ² = 0.069; 1D best-fit shift 0.078σ; error-bar change 0.82%; 900 times faster than the SPHEREx pipeline | realistic parameter range | arXiv:2603.16003 | [src] |
| CMBolic | C_ℓ^φφ (symbolic) | mean absolute fractional error 0.27% (ΛCDM), 0.32% (with Σm_ν, w0, wa) for 2 ≤ ℓ ≤ 5500; ACT DR6 + Planck lensing run from 2 weeks to under 3 minutes | — | arXiv:2606.07745 | [src] |
| Coyote Universe | non-linear matter P(k) | the required (one per cent) accuracy from 37 models over a CMB-set prior range (wCDM) | — | arXiv:0902.0429 | [src] |

## 2. Neural summaries and field-level networks
<!-- key: neural-summaries-and-field-level-networks -->

Information gains of neural summaries over the power spectrum. Rows on
simulations are method results; rows on survey data are quoted for the
method, and the cosmological values belong to `cosmo-weak-lensing` and
`cosmo-beyond-two-point`.

| Setting | Gain stated | Data | Citation | Flag |
|---|---|---|---|---|
| CNN on noiseless convergence maps, 96 cosmologies, 1 arcmin smoothing | Ω_m–σ8 contour area ≈ 5 times smaller than the power spectrum, ≈ 4 times smaller than peaks | simulations | Gupta et al. 2018, arXiv:1802.01212 | [src] |
| Loss-function test on a differentiable log-normal LSST-Y10 simulator, HMC ground truth | VMIM summaries reach 100% of the full-field Ω_c–σ8 figure of merit; MSE summaries 81% | simulations | Lanzieri et al. 2024, arXiv:2407.10877 | [src] |
| IMNN on Gaussian and log-normal fields | saturates the analytically known field information; SBI recovers the field-level posterior nearly losslessly | simulations | Makinen et al. 2021, arXiv:2107.07405 | [src] |
| CNN on CAMELS total-mass maps, tested on the other sub-grid model | Ω_m to ±4%, σ8 to ±2.5% | simulations, (25 h⁻¹Mpc)² maps | arXiv:2109.10360 | [src] |
| KiDS-1000 GCNN versus spherical power spectrum, GPABC | S8 = 0.79 ± 0.05 against 0.78 ± 0.06; 16% improvement; baryons widen S8 by about 10%; almost one million CosmoGrid mocks | data | Fluri et al. 2022, arXiv:2201.07771 | [src] |
| Same, without baryon treatment; and with a post-unblinding GPABC smoothing scale | S8 = 0.77 (+0.04/−0.05) (GCNN) against 0.76 ± 0.05 (power spectrum), a 14% gain; "GCNN optimized" S8 = 0.79 (+0.04/−0.05), ~11% tighter than the fiducial GCNN | data | arXiv:2201.07771 | [src: Sect. VI] |
| HSC Y1 CNN versus power spectrum | 5–24% smaller S8 error; 2.5–3.0 times smaller Ω_m error; with four baryon parameters S8 = 0.819 (+0.034/−0.024) | data | Lu et al. 2023, arXiv:2301.01354 | [src] |
| DES Y3 power spectrum + CNN map-level, wCDM | more than a factor of two on (Ω_DE, w) over the power spectrum; Gower Street suite of 791 full-sky PKDGRAV runs, over 3000 mock data sets | data | Jeffrey et al. 2024, arXiv:2403.02314 | [src] |
| KiDS-1000 GCNN on the mean of 400 CosmoGrid benchmark mocks | network constraints on average only ~10% tighter than the power spectrum, against ~30% in an earlier higher-resolution study; attributed to the scale cut (ℓ_max ~ 1500) and the conservative GPABC scale h = 0.4 | simulations | arXiv:2201.07771 | [src: Sect. V] |
| HSC Y1 CNN, eight extra architectures (n_block 5–15, n_ch 32–96) | statistical error on S8 0.0349–0.0355 and on Ω_m 0.0756–0.0782 across architectures at 4′ smoothing; 2′ smoothing gives 0.0338 and 0.0696 | mock catalogues | arXiv:2301.01354 | [src: Sect. VII.1, Table 6] |
| DES Y3 hybrid statistics (VMIM), wCDM | S8 = 0.808 ± 0.017, Ω_m = 0.325 ± 0.024, w < −0.766; FoM(Ω_m, S8, w) = 29 444 against 18 430 for the MSE C_ℓ × CNN and 10 344 for ξ± reanalysed with the same priors | data | Williamson et al. 2026, arXiv:2606.11309 | [src: Table 3] |
| KiDS-Legacy-like mocks, multi-fidelity field-level SBI | calibrated posteriors from 60 N-body simulations; at least an order of magnitude lower simulation cost | simulations | arXiv:2606.23346 | [src] |
| Same, high-fidelity-only CNN | beyond-two-point information extracted after ~200 Gower Street simulations, FoM 2–3 times the bandpower-only model; acceptable calibration for N ≥ 100 | simulations | arXiv:2606.23346 | [src: Sect. 4.2.1] |
| VMIM against MSE and MAE summaries | FoM(Ω_c, σ8) × 1.24 and × 1.1; w0 shifted to −1.13 (MSE), −1.16 (MAE), −0.73 (GNLL) against −1.01 for the HMC truth | simulations | arXiv:2407.10877 | [src: Sect. 6.3, Tables 4–5] |

## 3. Neural density estimation on data
<!-- key: neural-density-estimation-on-data -->

Method-level outcomes; the cosmological values belong to the probe skills.

| Analysis | Estimator | Outcome | Citation | Flag |
|---|---|---|---|---|
| KiDS-1000 cosmic shear pseudo-C_ℓ | NLE (DELFI, six-MAF ensemble), 18 000 realisations | S8 = 0.731 ± 0.033; PTE 0.42; neglecting variable depth and PSF anisotropy overestimates S8 by ~5% | von Wietersheim-Kramsta et al. 2024, arXiv:2404.15402 | [src] |
| Same, noiseless mock (truth S8 = 0.756) | NLE against a fixed-covariance Gaussian likelihood | S8 = 0.743 (+0.034/−0.031) against 0.733 (+0.034/−0.024); with noise 0.762 (+0.032/−0.027) against 0.744 (+0.031/−0.022) | arXiv:2404.15402 | [src: Sect. 8] |
| Stage-IV 3×2pt mock, 50 parameters | marginal NRE | posteriors in excellent agreement with nautilus at two orders of magnitude fewer CPU-hours | arXiv:2609.24946 | [src] |
| DES 5-year SN Ia population (dust and intrinsic scatter) | NPE for posteriors, NRE for model comparison, seven models | log₁₀ Bayes factor +1.9 against two high-z SN Ia populations; ΔR_V = 0.8; robust to abs(Δw) < 0.10 | Popovic et al. 2026, arXiv:2607.28725 | [src] |
| SO-SAT-like B modes, NILC + cross-spectra compression | NPE with flows | r = (1.09 ± 0.27) × 10⁻² for input 0.01, f_sky = 0.21, on the PySM d12 foreground model while trained on a semi-analytic one | Duivenvoorden et al. 2025, arXiv:2512.16869 | [src] |
| 100 simulated galaxy-scale strong lenses | NRE with post hoc population-level coverage calibration | median fractional uncertainty 22.8% on w and 2.9% on Ω_m (ΛCDM truth) | Jarugula et al. 2026, arXiv:2608.23534 | [src] |

## 4. Generative-model fidelity
<!-- key: generative-model-fidelity -->

| Model | Target | Fidelity stated | Citation | Flag |
|---|---|---|---|---|
| GAN, 2D N-body slices | cosmic web, 500 Mpc boxes | P(k) within 1–2% for 0.06 < k < 0.4 | arXiv:1801.09070 | [src] |
| Conditional flow matching | lensing convergence maps | < 1% basic, < 5% higher-order statistics (GAN benchmark < 10%, < 20%) | arXiv:2605.23114 | [src] |
| Cosmo-FOLD latent diffusion | TNG300-2 dark matter and gas temperature | P(k) within 10% for k ≤ 5 h Mpc⁻¹; bispectrum reproduced with positional encodings | arXiv:2601.14377 | [src] |
| Stochastic interpolants and GLOW, field-level initial conditions | posterior of a 32³ field | mean-field P(k) within 10%; variance-field P(k) off by up to ~30% | arXiv:2606.10023 | [src: Sect. 5.2] |

## 5. Challenge outcomes and classifier performance
<!-- key: challenge-outcomes-and-classifier-performance -->

| Classifier, task | Performance stated | Training/test data | Citation | Flag |
|---|---|---|---|---|
| Avocado, PLAsTiCC blinded phase | best of 1094 entries; flat-weight log-loss 0.468; SN Ia AUC 0.957 | PLAsTiCC | arXiv:1907.04690 | [src] |
| PLAsTiCC top three, official metric | 0.68503, 0.69933, 0.70016 | PLAsTiCC | arXiv:2012.12392 | [src: Sect. 3.4] |
| SuperNNova, Ia versus non-Ia | 96.92 ± 0.09% without redshift; 99.55 ± 0.06% with host redshift; > 86.4% two days before maximum without redshift | realistic simulations with survey detection | arXiv:1901.06384 | [src] |
| SCONE, Ia versus non-Ia | 99.73 ± 0.26% in distribution; 98.18 ± 0.3% for 6-way typing; out-of-distribution performance lower | PLAsTiCC unblinded test subset | arXiv:2106.04370 | [src] |
| SCONE, trained on the spectroscopic subset, tested on the full sample | accuracy 80.61 ± 1.75%, purity 81.86 ± 2.22%, efficiency 80.06 ± 1.31%, AUC 0.855 | PLAsTiCC | arXiv:2106.04370 | [src: Table 5] |
| ELAsTiCC-based DESC SN Ia simulation, SCONE + BBC, wCDM with CMB prior, 25 realisations | mean w bias 0.0225 ± 0.0037 (binned), 0.0126 ± 0.0038 (unbinned), 0.0256 ± 0.0032 (rebinned), stat only, for σ_w ≈ 0.020; absent with a perfect classifier | simulated LSST DDF | arXiv:2512.06319 | [src: Table 7, Sect. IV.4] |
| Beyond-2pt parameter-masked challenge, redshift-space mocks (mean of 10, errors of one box) | every team (density split, two kNN variants, EFT P + B, BACCO P, SBI P + B) recovered the masked Ω_m and σ8 within 1σ; SBI P + B trained on (1 h⁻¹Gpc)³ against a (2 h⁻¹Gpc)³ covariance for the others, and was wider on Ω_m, attributed to trimming the largest scales; a BACCO σ8 bias was traced after unmasking to hexadecapole emulation error | HOD mocks | arXiv:2405.02252 | [src: Sect. II.1, Table 1] |
| FAIR Universe WL challenge, Phase-1 baselines (score of Eq. 4: Gaussian KL term plus a 10³-weighted MSE penalty) | power spectrum + MCMC 4.58, CNN + MCMC 8.68, CNN direct prediction 8.52 on the public test set | HSC-Y3-like maps | Dai et al. 2026, arXiv:2604.14451 | [src: Sect. 4.1, 5.1.4] |
| FAIR Universe, Phase-2 baselines (mean TPR over 100 log-spaced FPRs in [0.001, 0.05]) | power spectrum χ² 0.214, CNN χ² 0.105, autoencoder 0.131; random 0.013: the neural baselines detect some out-of-distribution categories worse than the power spectrum | same | arXiv:2604.14451 | [src: Sect. 4.2, 5.2.3] |
| FAIR Universe, Phase-1 winner (Cmbagent agents with human redirection) | score 11.70, normalised MSE 0.10, ±1σ coverage 0.70; first in the public phase and in one of three final leaderboards (unseen maps at training cosmologies); Inception CNN ensembles with D4 test-time augmentation, CNN outputs used as summaries in a Gaussian likelihood calibrated on the training grid; degrades "substantially" off-grid in sparse regions | same | Borrett et al. 2026, arXiv:2604.09621 | [src: Sect. 3.5, 4, Tables 1, 3] |
| ORACLE, 19-way | top-level precision 0.96 at 1 day, > 0.99 at 64 days; 0.83 for 19 classes at 1024 days | ~0.5 M ELAsTiCC events | arXiv:2501.01496 | [src] |
| QuasarNET on BOSS | purity 99.51 ± 0.03%, completeness 99.52 ± 0.03%; catastrophic line confusion < 0.2%; BAL recognition 98.0 ± 0.4% | BOSS spectra | arXiv:1808.09955 | [src] |

## 6. Robustness across simulators
<!-- key: robustness-across-simulators -->

Summary of the cross-simulator tests listed in `systematics.md` §1: the
tests that passed used inputs on which the simulators compared agree
(positions and velocities of haloes or galaxies, total-mass maps), while
those that failed leaned on galaxy internal properties, halo
concentration, or small-scale clustering below k ~ 0.3 h Mpc⁻¹
(arXiv:2302.14101, arXiv:2209.06843, arXiv:2201.02202, arXiv:2310.15250)
[src]. The rule is not sufficient: a positions-and-velocities GNN failed on
CAMELS-CROCODILE (arXiv:2609.23982) [src: Sect. IV.1]. The measured failures are a
~10% σ8 bias for Lyα P1D across CAMELS models (arXiv:2603.13011) [src] and
a complete failure with overconfidence when a GNN meets a new galaxy
formation model outside its training range (arXiv:2609.23982) [src].

## 7. History of the key numbers
<!-- key: history-of-the-key-numbers -->

**Emulator accuracy on the matter power spectrum.**
- 2009: one-per-cent accuracy from 37 wCDM models (Coyote,
  arXiv:0902.0429) [src].
- 2021: 0.4% (99th percentile) for a neural emulator of Boltzmann and
  HMcode output, k ≤ 10 Mpc⁻¹, z ≤ 5, from 1.8 × 10⁵ training spectra
  (CosmoPower, arXiv:2106.03846) [src: Sect. 3.2].
- 2023: a symbolic expression reaches 0.2% RMS on the linear P(k)
  (arXiv:2311.15865) [src].
- 2025: neural multi-fidelity emulation cuts the mean error by more than
  five relative to the earlier Gaussian process on the same suite
  (arXiv:2507.07184) [src].
- 2026: sub-percent to the particle Nyquist scale over nine parameters
  including w0, wa and neutrinos (arXiv:2605.28596) [src].
What changed is the target (from gravity-only spectra to multi-tracer EFT
multipoles and field-level outputs) more than the headline per cent.

**Neural summaries of weak-lensing maps.**
- 2018: ≈ 5 times smaller contour than the power spectrum, noiseless
  simulations (arXiv:1802.01212) [src].
- 2022: 16% on S8 on KiDS-1000 data (arXiv:2201.07771) [src].
- 2023: 5–24% on S8 and 2.5–3 times on Ω_m on HSC Y1 (arXiv:2301.01354)
  [src].
- 2024: more than a factor of two on (Ω_DE, w) on DES Y3
  (arXiv:2403.02314) [src].
- 2024: the loss function caps the gain (MSE 81% of the full-field figure
  of merit, arXiv:2407.10877) [src].
- 2026: on the same DES Y3 lensing data and maps, a VMIM hybrid
  compression raises FoM(Ω_m, S8, w) by 60% over the MSE C_ℓ × CNN and by
  almost three over the two-point analysis (arXiv:2606.11309)
  [src: abstract, Table 3].
- 2025: 2–3 times the Ω_m–S8 figure of merit for DES Y3 lensing +
  clustering maps (**forecast**, arXiv:2511.04681) [src].
The survey-data gains on the S8 error (16%; 5–24%) are much smaller than
the noiseless-simulation factor of ≈ 5 in contour area; the quantities
differ (error against area), so the comparison is qualitative [der].

**Simulation budgets for neural density estimation.**
- 2019: O(10³) simulations or fewer for typical problems
  (arXiv:1903.00007) [src].
- 2024: 18 000 realisations for KiDS-SBI, with the loss converged after
  5000 (arXiv:2404.15402) [src: Sect. 5.4].
- 2024: over 3000 DES Y3 mocks from 791 full-sky runs (arXiv:2403.02314)
  [src].
- 2025: over one million map-level mocks for the DES Y3 lensing +
  clustering design (arXiv:2511.04681) [src].
- 2026: 60 high-fidelity N-body runs with multi-fidelity training for a
  KiDS-Legacy-like field-level analysis (arXiv:2606.23346) [src].
The sibling `cosmo-statistics-inference` records why the 2019 figure does
not mean fewer simulations than a covariance matrix.

**Transient classification.**
- 2018–2019: PLAsTiCC, best flat-weight log-loss 0.468, SN Ia AUC 0.957
  (arXiv:1907.04690) [src].
- 2019–2021: RNN and CNN classifiers above 96–99% binary accuracy in
  distribution (arXiv:1901.06384, arXiv:2106.04370) [src], with
  degraded out-of-distribution performance.
- 2025: real-time hierarchical classification from 1 day of photometry
  after first detection plus host context, on ELAsTiCC (arXiv:2501.01496)
  [src].

**Robustness across simulators.**
- 2021: total-mass maps transfer between IllustrisTNG and SIMBA
  (arXiv:2109.10360) [src].
- 2022–2023: galaxy properties do not transfer (arXiv:2201.02202,
  arXiv:2304.06084) [src]; halo and galaxy positions and velocities do
  (arXiv:2209.06843, arXiv:2302.14101) [src].
- 2026: Lyα P1D shows a ~10% σ8 bias across models (arXiv:2603.13011)
  [src]; a GNN fails on CAMELS-CROCODILE outside its training range
  (arXiv:2609.23982) [src].

## 8. Not verified
<!-- key: not-verified -->

- Emulator accuracy tables for Lyα, HOD and baryonic-feedback emulators
  (see `cosmo-lyman-alpha`, `cosmo-galaxy-halo-connection`,
  `cosmo-simulations-mocks`).
- Quantitative per-cent figures for the DarkEmulator2 cross-comparison
  beyond those in Sect. 5.2.3 (figures not read).
- Closed 2026-10-16: PyBird-Emu accuracy in σ is in `systematics.md` §3
  (95% of residuals below 0.1σ to k = 0.2 h Mpc⁻¹, arXiv:2507.20990,
  Sect. 2.2).
- FAIR Universe organisers' results paper (only the baselines,
  arXiv:2604.14451, and the winning entry, arXiv:2604.09621, were read).
- ELAsTiCC challenge-level results: an INSPIRE search for "ELAsTiCC"
  (2026-10-17) returned eight papers that use the data and none that
  describes the challenge itself.
