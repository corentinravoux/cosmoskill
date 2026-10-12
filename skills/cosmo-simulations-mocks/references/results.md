# Quantified results — cosmological simulations and mocks

Scope: the numbers a referee needs — code-comparison agreement, emulator and fast-method accuracy with k and z range, baryonic suppression of P(k) per suite, mock counts used by surveys.
Snapshot: 2026-10-07

## 1. Code-comparison agreement levels
<!-- key: code-comparison-agreement-levels -->

| Comparison | Set-up | Agreement | Reference, flag |
|---|---|---|---|
| RAMSES, PKDGRAV3, GADGET-3 (Euclid code comparison) | one set of initial conditions, standard run parameters | P(k) within 1% at k ≤ 1 h/Mpc and within 3% at k ≤ 10 h/Mpc; reduced bispectra within less than 1% at k ≤ 2 h/Mpc | Schneider et al. 2015, arXiv:1503.05920 [src] |
| Abacus on the same initial conditions | 2048³ particles, 500 Mpc/h, m_p = 1.2 × 10⁹ M_⊙/h, 10 kpc/h spline softening | good agreement with RAMSES and PKDGRAV3, "less so" with GADGET-3; halving the time step changes P(k) by less than 0.3% at k < 10 h/Mpc; linear theory reproduced to better than 0.01% on large scales | Garrison et al. 2018, arXiv:1810.02916 [src] |
| Abacus, GADGET, SWIFT (DESI N-body project) | matched phases; particle masses 6.25 × 10⁸, 2.11 × 10⁹ and 5.00 × 10⁹ M_⊙/h | matter P(k) within 1% for k ≤ 10 h/Mpc; code differences in halo clustering below the DESI statistical error for s > 20 Mpc/h in redshift space; 2.1 × 10⁹ M_⊙/h is converged for halo clustering at these scales | Grove et al. 2021, arXiv:2112.09138 [src] |
| GINKAKU against GADGET, PKDGRAV3, RAMSES | shared initial conditions | differences in the non-linear P(k) below about 1% after tuning accuracy parameters; inter-resolution spread of the halo mass function reduced to about 1% by the post-processing pipeline | Nishimichi et al. 2026, arXiv:2605.28581 [src] |
| Aemulus internal convergence | 1.05 Gpc/h boxes, 3.51 × 10¹⁰ M_⊙/h | statistics converged to 1% (2%) for halos with more than 500 (200) particles, for r > 200 kpc/h or k about 3 h/Mpc, z ≤ 1 | DeRose et al. 2018, arXiv:1804.05865 [src] |

The two headline code-comparison numbers are not the same statement. Schneider et al. 2015 (1% to k = 1, 3% to k = 10) compared three codes at "standard run parameters"; Grove et al. 2021 (1% to k = 10) compared three other codes with settings chosen for DESI. The improvement between them reflects tuned accuracy parameters as much as better codes, as the GINKAKU paper states explicitly.

Requirements derived from the Euclid comparison [src] (arXiv:1503.05920): a box of at least 0.5 Gpc/h to avoid systematic finite-volume effects on P(k), and a particle mass of at most 10⁹ M_⊙/h for 1% precision on the matter power spectrum. Covering survey volumes at that resolution needs more than a trillion particles.

## 2. Emulator accuracy
<!-- key: emulator-accuracy -->

All figures are the authors' statements about agreement with simulations of the same kind (gravity-only unless stated).

| Emulator | Quantity | Accuracy | k range | z range | Parameters | Reference, flag |
|---|---|---|---|---|---|---|
| EuclidEmulator2 | non-linear correction to the matter power spectrum | 1% or better | 0.01–10 h/Mpc | z ≤ 3 | eight: w0waCDM + Σm_ν | arXiv:2010.11288 [src] |
| Mira-Titan IV emulator | matter power spectrum | 2–3% | "wide range" (limits not in the abstract) | n/a | eight: {ω_m, ω_b, σ_8, h, n_s, w_0, w_a, ω_ν} | arXiv:2207.12345 [src] |
| BACCO | matter power spectrum | 2% in ΛCDM, 3% with dynamical dark energy and neutrinos | 0.01–5 h/Mpc | 0 < z < 1.5 | eight | arXiv:2004.06245 [src] |
| Aemulus ν | matter power spectrum and hybrid-EFT spectra | ≤ 1% for k ≤ 1 h/Mpc; ≤ 2% for k ≤ 4 h/Mpc (matter) | as stated | 0 ≤ z ≤ 3 | wνCDM | arXiv:2303.09762 [src] |
| Dark Emulator | halo–matter cross-correlation; halo auto-correlation | better than 2%; better than 4% (CMASS-like haloes) | configuration space | 0–1.48 | flat wCDM, 101 models | arXiv:1811.09504 [src] |
| HMcode-2020 (fitted halo model, not an emulator) | matter power spectrum | RMS 2.5%; rarely above 5%; never above 16% | k < 10 h/Mpc | z < 2 | wide, including neutrinos | arXiv:2009.01858 [src] |
| BACCO baryons | ratio of baryonic to gravity-only spectrum | 1–2% | 0.01–5 h/Mpc | 0 < z < 1.5 | 15, cosmology and baryons | arXiv:2011.15018 [src] |
| FLAMINGO response | baryonic response | better than 1% | to 10 h/Mpc | z ≤ 3 | FLAMINGO feedback variations | arXiv:2410.17109 [src] |
| HMcode-2020 feedback model | baryonic response | < 1% | k < 20 h/Mpc | z < 1 | six parameters, or one | arXiv:2009.01858 [src] |
| Baryonification, 2+1 parameters | baryonic response of FLAMINGO and TNG | better than 2.5% | survey-relevant scales | survey-relevant redshifts | 3 | arXiv:2507.07892 [src] |
| LaCE, ForestFlow, PRIYA, Lyssa | Lyα P1D and P3D | see §6 | | | | |

MillenniumTNG compares its runs with these emulators as an external check (arXiv:2210.10059; no number in the abstract). EuclidEmulator2 passed a blind test against Flagship v2.0 [src] (arXiv:2010.11288).

The gravity-only emulators are quoted at 1–3% while the baryonic response at k = 1 h/Mpc is 5–10% and uncertain by a factor of two (§4). Beyond k of a few tenths h/Mpc the error budget of a matter power spectrum prediction is set by baryons, not by the emulator.

## 3. Accuracy of approximate methods
<!-- key: accuracy-of-approximate-methods -->

| Method | Statistic | Accuracy | Range | Reference, flag |
|---|---|---|---|---|
| COLA, 10 steps | halo statistics | "accurate" down to 10¹¹ M_⊙/h | 100 Mpc/h box, 5 × 10⁹ M_⊙/h particles | arXiv:1301.0322 [src] |
| ICE-COLA, 40 steps, mesh factor 3 | matter P(k) | 1% | k ≲ 1 h/Mpc, 0 < z < 1 | arXiv:1509.04685 [src] |
| same | halo mass function | 5% | M > 10¹²·⁵ M_⊙/h | arXiv:1509.04685 [src] |
| same | halo bias | 2% | k ≲ 0.7 h/Mpc | arXiv:1509.04685 [src] |
| same | redshift-space halo monopole and quadrupole | 4% | k ≲ 0.4 h/Mpc | arXiv:1509.04685 [src] |
| COLA, 20 steps, inside BORG | density field around massive local clusters | adequate; virial masses not converged | within 135 Mpc/h | arXiv:2304.09193 [src] |
| FastPM, N_s = 10, B = 2 | halo benchmarks at z = 0 | close to N_s = 40, B = 3 at one tenth of the cost | — | arXiv:1603.00476 [src] |
| Seven approximate methods (ICE-COLA, Pinocchio, PeakPatch, Halogen, Patchy, lognormal, Gaussian) against 300 N-body runs | halo power-spectrum monopole | most within 5%; quadrupole residuals sometimes larger and scale dependent | — | Blot et al. 2018, arXiv:1806.09497 [src] |
| same | variance of the multipoles | typically within 10% | — | arXiv:1806.09497 [src] |
| same | errors on growth, AP and bias parameters from the mock covariance | within 10% of the N-body covariance result | — | arXiv:1806.09497 [src] |
| EZmocks for eBOSS | two-point statistics of data against mocks | within 1σ | down to a few Mpc/h; up to k = 0.3 h/Mpc; cross-correlations discrepant in Fourier space above 0.15 h/Mpc | arXiv:2007.08997 [src] |
| GLASS | two-point statistics of clustering and lensing | percent level | full-sky shells | arXiv:2302.01942 [src] |
| CoLoRe-2LPT | Lyα bias, β, mean flux, P1D | within 10% of the DESI measurement; quasar linear bias within 5% | z > 2 | arXiv:2607.27412 [src] |
| FastPM against Abacus, GADGET, SWIFT | included in the DESI comparison | see arXiv:2112.09138 (numbers for FastPM not in the abstract) | — | arXiv:2112.09138 |

The 10% on parameter errors is the number to quote when a referee asks how well an approximate-mock covariance is known. It is of the same order as the finite-mock corrections (10% on the error bar for 100 data points and 1000 mocks, according to `cosmo-statistics-inference`), so both must be stated.

## 4. Baryonic suppression of the matter power spectrum
<!-- key: baryonic-suppression-of-the-matter-power -->

The quantity is the response R(k) = P_hydro(k) / P_gravity-only(k) of the total matter power spectrum.

| Simulation or data | Suppression | Scale | Reference, flag |
|---|---|---|---|
| OWLS AGN run | 1% at k about 0.3, 10% at k about 1, 30% at k about 10 h/Mpc; cooling raises power only for k > 70 h/Mpc | z = 0 | van Daalen et al. 2011, arXiv:1104.1174 [src] |
| Horizon-AGN | less than 15% at k about 10 h/Mpc; smaller than other simulations, read by the authors as AGN feedback that is not strong enough | z = 0 | Chisari et al. 2018, arXiv:1801.08559 [src] |
| IllustrisTNG | total matter power damped by up to 20% on scales up to k about 10 h/Mpc | redshift not stated in the abstract | Springel et al. 2017, arXiv:1707.03397 [src] |
| FLAMINGO (suite paper) | halo mass function and matter power spectrum suppressed by up to about 20% | hydrodynamical against dark-matter-only | Schaye et al. 2023, arXiv:2306.04024 [src] |
| Baryonic correction model with X-ray and SZ cluster data | starts above k about 0.5 h/Mpc, maximum 10–25% around k about 2 h/Mpc | redshift not stated in the abstract | Schneider & Teyssier 2015, arXiv:1510.06034 [src] |
| FLAMINGO | stronger with lower group and cluster gas fractions, with jets instead of thermal AGN feedback, and with lower stellar masses at fixed gas fraction; cosmology dependence about 1% for k < 10 h/Mpc; the response strengthens and its minimum moves to smaller scales as redshift decreases | z ≤ 3 | Schaller et al. 2024, arXiv:2410.17109 [src] |
| Data: eROSITA gas fractions + SDSS/DESI × ACT kSZ, baryonification | 10 ± 2% at k = 1 h/Mpc; stronger than fiducial FLAMINGO and BAHAMAS | 0 < z < 1 | Siegel et al. 2025, arXiv:2512.02954 [src] |
| Data: HSC-XXL gas fractions alone (the data the fiducial simulations were calibrated to) | 5 ± 4% at k = 1 h/Mpc | 0 < z < 1 | arXiv:2512.02954 [src] |

How the suites compare with gas observations, 2024–2026:

| Test | Outcome | Reference, flag |
|---|---|---|
| DES Y3 lensing + ACT DR5 kSZ, baryonification | mean feedback more extreme than most hydrodynamical simulations; S8 = 0.823 +0.019/−0.020 | Bigwood et al. 2024, arXiv:2404.06098 [src] |
| DESI Y1 × ACT kSZ against FLAMINGO, ANTILLES, BAHAMAS, SIMBA, FABLE | fiducial feedback models disfavoured at more than 3σ; stronger-AGN variants of FLAMINGO and BAHAMAS, and SIMBA, within 2σ; kSZ amplitude predicts the P(k) suppression as well as baryon fractions do | Bigwood et al. 2025, arXiv:2510.15822 [src] |
| eROSITA X-ray + DESI × ACT kSZ + lensing against the fiducial 1 Gpc FLAMINGO | eROSITA gas fractions 2× lower than the simulation; kSZ combined more than 8σ discrepant; the strongest-expulsion variant fits | Siegel et al. 2025, arXiv:2509.10455 [src] |
| DESI DR2 BGS and LRG lensing-to-kSZ ratio (HSC Y3 shear, ACT DR6) against Illustris, IllustrisTNG, SIMBA, FLAMINGO | fiducial FLAMINGO tracks the radial gas fraction most closely; Illustris-1 and TNG300-1 bracket the data at small radii | Liu et al. 2026, arXiv:2609.22466 [src] |

The last two rows disagree on whether fiducial FLAMINGO is excluded. This is the live debate recorded in `open-questions.md` §1.1; the sibling skills `cosmo-weak-lensing` and `cosmo-cmb-lss-cross-correlations` quote the same four papers with the same numbers.

What controls the suppression: the mean baryon fraction of groups predicts the z = 0 effect to 1% for k < 1 h/Mpc across OWLS, cosmo-OWLS and BAHAMAS [src] (arXiv:1906.00968), and to about the percent level for k ≲ 10 h/Mpc and z ≤ 3 across ANTILLES [src] (arXiv:2305.09710). Differences in group baryon fractions explain the quantitative disagreement between older predictions [src] (arXiv:1906.00968).

## 5. Mock counts used by surveys
<!-- key: mock-counts-used-by-surveys -->

| Analysis | Covariance source | Mock count | Reference, flag |
|---|---|---|---|
| eBOSS DR16 BAO and RSD | EZmock sample covariance | 1000 per tracer | arXiv:2007.08997 [src] |
| DESI DR1 BAO | analytic (RascalC, configuration space) as the fiducial choice, validated against EZmocks | 1000 EZmocks per Galactic cap | arXiv:2411.12027 [src] |
| DESI DR1 full shape | EZmock sample covariance with a correction, because the analytic Fourier-space covariance did not reproduce the expected measurements | 1000 per cap | arXiv:2411.12027 [src] |
| DESI DR1 systematic tests | AbacusSummit HOD mocks | 25 boxes | arXiv:2404.03008 [src] |
| DESI DR1 peculiar velocities | DESI-PV mocks | 675 | arXiv:2512.03228 [src] |
| Euclid | no cosmological analysis published at the snapshot [sec: `cosmo-weak-lensing` and `cosmo-galaxy-clustering` SKILL.md]; the reference mock is one Flagship 2 light-cone | 1 | arXiv:2405.13495 [src] |

Two points about these counts. The DESI BAO covariance is not a mock covariance: the mocks validate an analytic one. And the DESI EZmocks are calibrated on AbacusSummit HOD mocks, which are calibrated on the one-percent survey, so the chain from data to covariance has two fitted layers [src] (arXiv:2411.12027).

With N_mocks = 1000 and a data vector of 100 points the error bar inflates by 10%, with 400 points by 65%; this is the sibling skill's number (`cosmo-statistics-inference`, from arXiv IDs cited there) and it was not re-derived here [sec: cosmo-statistics-inference SKILL.md].

## 6. Lyα simulation accuracy
<!-- key: lyalpha-simulation-accuracy -->

| Statement | Number | Conditions | Reference, flag |
|---|---|---|---|
| Resolution for converged flux statistics | 20 kpc/h cells for 1% | Nyx, to k = 10 h/Mpc, 2 ≤ z ≤ 4 | arXiv:1406.6361 [src] |
| Box size | L > 40 Mpc/h for sub-percent missing-mode error | Nyx | arXiv:1406.6361 [src] |
| Splicing accuracy | 10% level on P1D | Nyx test | arXiv:1406.6361 [src] |
| Eulerian versus SPH | ≲ 1% in P1D | Nyx versus CRK-HACC with tessellated density; the SPH-kernel density biases flux statistics, most at z about 5 | arXiv:2207.05023 [src] |
| AGN feedback on P1D | suppression at all scales, growing to low z; neglect shifts σ_8 by 2% and n_s by 1% (twice the then-current error on n_s) | Horizon-AGN series, z = 4.25–2.0 | arXiv:2002.02822 [src] |
| LaCE | sub-percent, k_∥ = 0.1–4 Mpc⁻¹, z = 2–4.5; percent level to 8 Mpc⁻¹ | includes unseen ΛCDM extensions | arXiv:2305.19064 [src] |
| ForestFlow | 3% on P3D to k = 5 Mpc⁻¹; 1.5% on P1D to k_∥ = 4 Mpc⁻¹ | z = 2–4.5 | arXiv:2409.05682 [src] |
| PRIYA | interpolation error < 1%; percent-level convergence, z = 5.4–2.2 | 120 Mpc/h boxes | arXiv:2306.05471 [src] |
| Lyssa | sub-percent convergence of P1D per run | 4096³ cells in 120 Mpc | arXiv:2412.05372 [src] |
| Lyssa on eBOSS DR14 | A_Lyα < 7.6 (95%), n_Lyα = −2.369 ± 0.008; Planck best fit A_Lyα = 8.79, n_Lyα = −2.363; with a mean-transmission prior A_Lyα = 9.8 ± 1.1 | the low amplitude is driven by the mean-flux degeneracy | arXiv:2412.05372 [src] |

A 1% emulator error is an interpolation error inside the training set. It says nothing about physics absent from the simulations (patchy reionisation, AGN feedback), which the rows above show to be at the percent level or more.

## 7. Constrained simulations: quantified results
<!-- key: constrained-simulations-quantified-results -->

| Quantity | Value | Context | Reference, flag |
|---|---|---|---|
| Reduction of cell-to-cell scatter in constrained runs | factor 2–3 at 5 Mpc/h | CLUES, inner region | arXiv:1510.04900 [src] |
| Scatter between simulated and reconstructed velocity fields | 104 ± 4 km/s | CLUES | arXiv:1510.04900 [src] |
| Smallest scale of accurate 2LPT BORG reconstruction | about 6 Mpc/h | SDSS DR7-like mock | arXiv:1203.3639 [src] |
| Number of COLA steps adequate for the density field around local clusters | 20 (virial masses still unconverged) | within 135 Mpc/h | arXiv:2304.09193 [src] |
| Local underdensity | about 5% relative to the mean | SIBELIUS-DARK, to 200 Mpc | arXiv:2202.04099 [src] |
| Local underdensity | "no evidence for a large local underdensity" | Manticore-Local | arXiv:2505.10682 [src] |
| Cluster counterparts | 14, each within 1°, detected at 2–4σ across the posterior | Manticore-Local | arXiv:2505.10682 [src] |
| Reconstructed volume and resolution | (4 Gpc/h)³ to z about 0.7 at about 4 Mpc/h | Manticore-Deep | arXiv:2606.10020 [src] |
| CMB-lensing cross-correlation of the reconstruction | 7.4σ (Planck PR3) | Manticore-Deep | arXiv:2606.10020 [src] |
| kSZ from reconstructed velocities | 3.5σ, 64,750 clusters, Planck 217 GHz | Manticore-Deep | arXiv:2606.10020 [src] |
| Constrained ensemble from velocities | 100 runs, 512³ in (500 Mpc/h)³, Cosmicflows-4 to 160 Mpc/h | Hamlet-PM | arXiv:2602.03699 [src] |
| S8 from density–velocity cross-correlation with a linear reconstruction | 0.793 ± 0.035; in agreement with weak lensing and Planck, in strong disagreement with some peculiar-velocity studies | validation framework for velocity reconstructions | arXiv:2502.00121 [src] |
| Differentiable particle mesh | 6 steps for percent-level P(k) at k about 0.2 h/Mpc, 512³, a few seconds on GPU | DISCO-DJ | arXiv:2510.05206 [src] |
| Lyα-tomography reconstruction | r = 0.95 on deformation-tensor eigenvalues | TARDIS, 30 m-class mock data | arXiv:1903.09049 [src] |

The two local-density statements come from different inferences on overlapping data and are not reconciled in the abstracts read; see `open-questions.md` §1.6. The S8 value is a by-product of a validation paper and uses linear theory; current peculiar-velocity growth measurements are in `cosmo-peculiar-velocities`.


## 8. History of the key numbers
<!-- key: history-of-the-key-numbers -->

Each line gives the sequence in time, so that a reader can tell which statement is the current one.

**Agreement between N-body codes on the matter power spectrum.**
- 2016: 1% to k = 1 h/Mpc and 3% to k = 10 h/Mpc, three codes at standard settings (arXiv:1503.05920).
- 2019: Abacus on the same initial conditions; time-step convergence below 0.3% to k = 10 h/Mpc (arXiv:1810.02916).
- 2022: 1% to k = 10 h/Mpc for Abacus, GADGET and SWIFT with DESI settings (arXiv:2112.09138). This is the figure to quote today, with its condition.
- 2026: below about 1% for a fourth code family after tuning (arXiv:2605.28581).

**Baryonic suppression at k = 1 h/Mpc, z = 0.**
- 2011: 10% in the OWLS AGN run (arXiv:1104.1174), the result that made baryons a cosmological systematic.
- 2015: 10–25% maximum near k about 2 h/Mpc from the baryonic correction model with cluster gas data (arXiv:1510.06034).
- 2018: weaker in Horizon-AGN (less than 15% even at k about 10) and up to 20% by k about 10 in IllustrisTNG (arXiv:1801.08559, arXiv:1707.03397).
- 2020: the spread is explained by the baryon fraction of groups (arXiv:1906.00968).
- 2023–2025: FLAMINGO, calibrated to pre-eROSITA gas fractions, up to about 20% in its suite paper; its strongest-feedback variants match lensing-based analyses but are in strong tension with the X-ray gas fractions used for the calibration [src] (arXiv:2306.04024, arXiv:2410.17109).
- 2025: data-driven 10 ± 2% from kSZ and eROSITA, against 5 ± 4% from the older X-ray sample (arXiv:2512.02954). Current, and disputed (arXiv:2609.22466).

**Gravity-only emulator accuracy.**
- 2019–2021: 2–4% for halo statistics (arXiv:1811.09504); 2–3% for BACCO to k = 5 h/Mpc (arXiv:2004.06245); 1% for EuclidEmulator2 to k = 10 h/Mpc (arXiv:2010.11288).
- 2023: 2–3% for the final Mira-Titan emulator over eight parameters (arXiv:2207.12345); 1% to k = 1 h/Mpc for Aemulus ν (arXiv:2303.09762).
- 2026: a nine-parameter emulator of the Dark Quest II programme reports sub-percent accuracy to the particle Nyquist scale (abstract read; outside the source list).

**Covariance mocks for spectroscopic surveys.**
- eBOSS DR16: 1000 EZmocks per tracer (arXiv:2007.08997).
- DESI DR1: 1000 EZmocks per Galactic cap, used directly for the full shape and as validation of an analytic covariance for BAO (arXiv:2411.12027).
- DESI DR1 peculiar velocities: 675 (arXiv:2512.03228).

**Lyα forest simulations.**
- 2015: 20 kpc/h and 40 Mpc/h requirements; splicing good to 10% (arXiv:1406.6361).
- 2017: Sherwood, up to 160 Mpc/h (arXiv:1605.03462).
- 2020: AGN feedback worth 2% on σ_8 (arXiv:2002.02822).
- 2023: grid and particle codes agree to 1% in P1D with a tessellated density (arXiv:2207.05023); PRIYA with patchy reionisation (arXiv:2306.05471); Sherwood-Relics (arXiv:2207.13098).
- 2023–2025: emulators at the sub-percent to 3% level (arXiv:2305.19064, arXiv:2409.05682, arXiv:2412.05372).
- 2026: 2LPT-based synthetic spectra replace lognormal ones for the DESI DR2 full-shape validation (arXiv:2607.27412).

**Constrained simulations.**
- 2013: 2LPT field-level inference, about 6 Mpc/h (arXiv:1203.3639).
- 2016: velocity-constrained realisations to 150 Mpc/h (arXiv:1510.04900).
- 2019: particle-mesh dynamics inside the sampler, 2M++ (arXiv:1806.11117).
- 2022: SIBELIUS-DARK to 200 Mpc with public catalogues (arXiv:2202.04099).
- 2024: posterior resimulation established as the route to halo masses (arXiv:2304.09193).
- 2025: Manticore-Local, a posterior ensemble validated on velocities (arXiv:2505.10682, arXiv:2502.00121).
- 2026: Manticore-Deep over (4 Gpc/h)³ (arXiv:2606.10020); forward modelling from Cosmicflows-4 velocities (arXiv:2602.03699).

## Not verified
<!-- key: not-verified -->

- k and z limits of the Mira-Titan IV emulator (the abstract says "wide range").
- Numerical accuracy of FastPM in the DESI code comparison (arXiv:2112.09138 abstract gives none).
- Mock counts behind the DES and Euclid covariances, and the DES choice of an analytic covariance: a DES Y3 covariance paper was read this session but lies outside the source list; see `cosmo-weak-lensing` and `cosmo-statistics-inference`.
- The BOSS MultiDark-Patchy count (12,288 DR12 light-cones in the abstract read) is outside the source list.
- Number of CoLoRe-2LPT realisations used for DESI DR2.
- Quantitative results of arXiv:2511.20423 on box replication.
- The sub-percent figure of the 2026 Dark Quest II emulator, the 2% of a 2025 COLA-based w0wa emulator against EuclidEmulator2, and the percent-level field-level emulator inside BORG were read in abstracts of papers outside the source list.
- Baryonic suppression in EAGLE, BAHAMAS, SIMBA and MillenniumTNG individually: no number was read at source for these four.
