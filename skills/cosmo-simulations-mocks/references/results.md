# Quantified results — cosmological simulations and mocks

Scope: the numbers a referee needs — code-comparison agreement, emulator and fast-method accuracy with k and z range, baryonic suppression of P(k) per suite, mock counts used by surveys.
Snapshot: 2026-10-26

## 1. Code-comparison agreement levels
<!-- key: code-comparison-agreement-levels -->

| Comparison | Set-up | Agreement | Reference, flag |
|---|---|---|---|
| Ten codes (Cosmic Code Comparison Project) | common initial conditions in small boxes | P(k) and mass function at the 10% level over wide ranges | Heitmann et al. 2007, arXiv:0706.1270 [src: abstract] |
| RAMSES, PKDGRAV3, GADGET-3 (Euclid code comparison) | one set of initial conditions (2LPT at z = 49), L = 500 Mpc/h, 2048³ particles, standard run parameters | P(k) within 1% at k ≤ 1 h/Mpc at z = 0 to 3.8, and within 3% at k ≤ 10 h/Mpc for z ≤ 1 (about 5% at z = 2, 10% at z = 3.8); largest scales within about 0.4%; reduced bispectra within less than 1% at k ≤ 2 h/Mpc | Schneider et al. 2015, arXiv:1503.05920 [src: Sects. 2.1 and 2.3, Fig. 1; bispectrum from the abstract] |
| GADGET-4, PKDGRAV3, Abacus, RAMSES on the Euclid comparison box | reruns by the code authors | P(k) within 0.4% up to k about 2 h/Mpc and 2% up to k about 10 h/Mpc at z = 0; stacked profiles of the 25 most massive haloes within a percent down to 10 kpc/h | [sec: arXiv:2112.05165, Sect. 8.5 and Fig. 24, after Springel et al. 2020] |
| Abacus on the same initial conditions | 2048³ particles, 500 Mpc/h, m_p = 1.2 × 10⁹ M_⊙/h, 10 kpc/h spline softening | good agreement with RAMSES and PKDGRAV3, "less so" with GADGET-3; halving the time step changes P(k) by less than 0.3% at k < 10 h/Mpc; linear theory reproduced to better than 0.01% on large scales | Garrison et al. 2018, arXiv:1810.02916 [src: abstract] |
| Abacus, GADGET, SWIFT (DESI N-body project) | matched phases from z = 199; 1296³, 1728³ and 2592³ particles, particle masses 6.25 × 10⁸, 2.11 × 10⁹ and 5.00 × 10⁹ M_⊙/h; compared at z = 1 and z = 2 | matter P(k) within 1% for k ≤ 10 h/Mpc (0.1% at k < 0.1 h/Mpc); between resolutions of one code 1% at k = 2 and 4% at k = 10 h/Mpc; mass functions within 1% for 10¹²–10¹³·⁵ M_⊙/h; code differences in halo clustering below the DESI statistical error for s > 20 Mpc/h in redshift space (year-5 error; year-1 error above 10 Mpc/h); 2.1 × 10⁹ M_⊙/h is converged for halo clustering at these scales | Grove et al. 2021, arXiv:2112.09138 [src: Sects. 3.2, 4.2 and 5.2] |
| GINKAKU against GADGET, PKDGRAV3, RAMSES | shared initial conditions | differences in the non-linear P(k) below about 1% after tuning accuracy parameters; inter-resolution spread of the halo mass function reduced to about 1% by the post-processing pipeline | Nishimichi et al. 2026, arXiv:2605.28581 [src] |
| Aemulus internal convergence | 1.05 Gpc/h boxes, 3.51 × 10¹⁰ M_⊙/h | statistics converged to 1% (2%) for halos with more than 500 (200) particles, for r > 200 kpc/h or k about 3 h/Mpc, z ≤ 1 | DeRose et al. 2018, arXiv:1804.05865 [src: abstract] |

Sizes with their conditions are in `systematics.md` §2. The two headline code-comparison numbers are not the same statement. Schneider et al. 2015 (1% to k = 1, 3% to k = 10; arXiv:1503.05920 [src: abstract]) compared three codes at "standard run parameters"; Grove et al. 2021 (1% to k = 10; arXiv:2112.09138 [src: abstract]) compared three other codes with settings chosen for DESI. The improvement between them reflects tuned accuracy parameters as much as better codes, as the GINKAKU paper states explicitly (arXiv:2605.28581 [src: abstract]).

Requirements derived from the Euclid comparison [src: abstract] (arXiv:1503.05920): a box of at least 0.5 Gpc/h to avoid systematic finite-volume effects on P(k), and a particle mass of at most 10⁹ M_⊙/h for 1% precision on the matter power spectrum. Covering survey volumes at that resolution needs more than a trillion particles.

## 2. Emulator accuracy
<!-- key: emulator-accuracy -->

All figures are the authors' statements about agreement with simulations of the same kind (gravity-only unless stated).

| Emulator | Quantity | Accuracy | k range | z range | Parameters | Reference, flag |
|---|---|---|---|---|---|---|
| EuclidEmulator2 | non-linear correction to the matter power spectrum | 1% or better, measured on three validation cosmologies inside the ellipsoid inscribed in the parameter box [src: Sect. 8.2.1] | 0.01–10 h/Mpc | z ≤ 3 | eight: w0waCDM + Σm_ν | arXiv:2010.11288 [src] |
| Mira-Titan IV emulator | matter power spectrum | 2–3% (abstract); better than 2% on five of six test models outside the design, 2.48% for the one at the edge of the dark-energy region [src: Sect. 4.1] | "wide range" (limits not in the abstract) | 0 ≤ z ≤ 2.02 [src: Sect. 2.1] | eight: {ω_m, ω_b, σ_8, h, n_s, w_0, w_a, ω_ν} | arXiv:2207.12345 [src] |
| BACCO | matter power spectrum | 2% in ΛCDM, 3% with dynamical dark energy and neutrinos | 0.01–5 h/Mpc | 0 < z < 1.5 | eight | arXiv:2004.06245 [src] |
| Aemulus ν | matter power spectrum and hybrid-EFT spectra | ≤ 1% for k ≤ 1 h/Mpc; ≤ 2% for k ≤ 4 h/Mpc (matter) | as stated | 0 ≤ z ≤ 3 | wνCDM | arXiv:2303.09762 [src] |
| Dark Emulator | halo–matter cross-correlation; halo auto-correlation | better than 2%; better than 4% (CMASS-like haloes) | configuration space | 0–1.48 | flat wCDM, 101 models | arXiv:1811.09504 [src] |
| HMcode-2020 (fitted halo model, not an emulator) | matter power spectrum | RMS 2.5%; rarely above 5%; never above 16% | k < 10 h/Mpc | z < 2 | wide, including neutrinos | arXiv:2009.01858 [src] |
| BACCO baryons | ratio of baryonic to gravity-only spectrum | 1–2% | 0.01–5 h/Mpc | 0 < z < 1.5 | 15, cosmology and baryons | arXiv:2011.15018 [src] |
| FLAMINGO response | baryonic response | better than 1% | to 10 h/Mpc | z ≤ 3 | FLAMINGO feedback variations | arXiv:2410.17109 [src] |
| HMcode-2020 feedback model | baryonic response | < 1% | k < 20 h/Mpc | z < 1 | six parameters, or one | arXiv:2009.01858 [src] |
| Baryonification, 2+1 parameters | baryonic response of FLAMINGO and TNG | better than 2.5% | survey-relevant scales | survey-relevant redshifts | 3 | arXiv:2507.07892 [src] |
| LaCE, ForestFlow, PRIYA, Lyssa | Lyα P1D and P3D | see §6 | | | | |

Emulators against each other: EuclidEmulator2 and BACCO within about 1% at the Euclid reference cosmology and mostly within 3% over 47 cosmologies at z = 0; EuclidEmulator2 and the Mira-Titan II emulator with a scatter of about 5% over 84 cosmologies [src: Sects. 8.2.5 and 8.2.6 of arXiv:2010.11288]; EuclidEmulator2 within about 3% of a Mira-Titan ΛCDM simulation [src: Sect. 4.2.2 of arXiv:2207.12345]. MillenniumTNG compares its runs with these emulators as an external check (arXiv:2210.10059; no number in the abstract). EuclidEmulator2 passed a blind test against Flagship v2.0 [src] (arXiv:2010.11288).

The gravity-only emulators are quoted at 1% (EuclidEmulator2, arXiv:2010.11288) and 2–3% (Mira-Titan IV, arXiv:2207.12345) [src: abstract of each], while the baryonic response at k = 1 h/Mpc is 10 ± 2% from kSZ and eROSITA but 5 ± 4% from the HSC-XXL gas fractions (arXiv:2512.02954 [src: abstract]; §4). Beyond k of a few tenths h/Mpc the error budget of a matter power spectrum prediction is set by baryons, not by the emulator.

## 3. Accuracy of approximate methods
<!-- key: accuracy-of-approximate-methods -->

| Method | Statistic | Accuracy | Range | Reference, flag |
|---|---|---|---|---|
| COLA, 10 steps | halo statistics | "accurate" down to 10¹¹ M_⊙/h | 100 Mpc/h box, 5 × 10⁹ M_⊙/h particles | arXiv:1301.0322 [src: abstract] |
| ICE-COLA, 40 steps, mesh factor 3 | matter P(k) | 1% | k ≲ 1 h/Mpc, 0 < z < 1 | arXiv:1509.04685 [src: abstract] |
| same | halo mass function | 5% | M > 10¹²·⁵ M_⊙/h | arXiv:1509.04685 [src: abstract] |
| same | halo bias | 2% | k ≲ 0.7 h/Mpc | arXiv:1509.04685 [src: abstract] |
| same | redshift-space halo monopole and quadrupole | 4% | k ≲ 0.4 h/Mpc | arXiv:1509.04685 [src: abstract] |
| COLA, 20 steps, inside BORG | density field around massive local clusters | adequate; virial masses not converged | within 135 Mpc/h | arXiv:2304.09193 [src: abstract] |
| FastPM, N_s = 10, B = 2 | halo benchmarks at z = 0 | close to N_s = 40, B = 3 at one tenth of the cost | — | arXiv:1603.00476 [src: abstract] |
| Seven approximate methods (ICE-COLA, Pinocchio, PeakPatch, Halogen, Patchy, lognormal, Gaussian) against 300 N-body runs | halo power-spectrum monopole | most within 5%; quadrupole residuals sometimes larger and scale dependent | — | Blot et al. 2018, arXiv:1806.09497 [src: Sect. 1] |
| same | variance of the multipoles | typically within 10% | — | arXiv:1806.09497 [src: abstract] |
| same | errors on growth, AP and bias parameters from the mock covariance | within 10% of the N-body covariance result | — | arXiv:1806.09497 [src: abstract] |
| EZmocks for eBOSS | two-point statistics of data against mocks | within 1σ | down to a few Mpc/h; up to k = 0.3 h/Mpc; cross-correlations discrepant in Fourier space above 0.15 h/Mpc | arXiv:2007.08997 [src: abstract] |
| GLASS | two-point statistics of clustering and lensing | percent level | full-sky shells | arXiv:2302.01942 [src] |
| CoLoRe-2LPT | Lyα bias, β, mean flux, P1D | within 10% of the DESI measurement; quasar linear bias within 5% | z > 2 | arXiv:2607.27412 [src: abstract] |
| FastPM against Abacus, GADGET, SWIFT | matter P(k) | departs at the 1% level | k > 0.5 h/Mpc, z = 1 and 2; force-mesh factor 2, 46 steps | arXiv:2112.09138 [src: Sects. 3.1.4 and 5.2] |
| EZmocks, original method | halo P(k) and ξ against N-body; bispectrum | 1%; 20% | k ≤ 0.55 h/Mpc, r ≥ 10 Mpc/h | arXiv:1409.1124 [src: abstract] |
| PATCHY | halo P(k), real and redshift space | about 2% | k ≲ 1 h/Mpc, z = 0.577, CMASS-like density | arXiv:1307.3285 [src: abstract] |
| L-PICOLA | matter P(k); reduced bispectrum | 2%; 5% | z = 0, BAO and RSD scales | arXiv:1506.03737 [src] |
| COLA, 10 steps (WiggleZ mocks) | velocity power spectrum | no systematic error for k < 0.15 h/Mpc; 3% for k < 0.2 h/Mpc | 10¹² M_⊙ haloes | arXiv:1507.05329 [src: abstract] |
| PINOCCHIO | halo mass function | better than 10% | haloes of at least 30–50 particles | arXiv:astro-ph/0109323 [src: abstract] |
| nIFTy comparison | quadrupole of ξ and P(k) | 1% only for the semi-N-body method | r < 25 Mpc/h, k > 0.15 h/Mpc | arXiv:1412.7729 [src: abstract] |
| Seven approximate methods, correlation-function covariance | parameter errors | within 5% (lower mass threshold), 10% (higher); up to 20% depending on how the halo sample is matched | z = 1 | Lippich et al. 2018, arXiv:1806.09477 [src: abstract] |
| Same, power-spectrum covariance, body | parameter errors | 5% for most methods on cosmological parameters; 10% for all but lognormal; test resolution 4–5% | periodic boxes, z = 1, 300 mocks per method | arXiv:1806.09497 [src: Sect. 6] |
| Same, bispectrum covariance | errors on bias parameters | within 10% except methods calibrated on two-point statistics only | — | Colavincenzo et al. 2018, arXiv:1806.09499 [src: abstract] |
| sCOLA light-cones, tiled with an LPT buffer and second-order boundary potential, against GADGET-4 (3.84 Gpc/h box, 3840³ particles) | matter P(k); velocity-divergence P(k); equilateral bispectrum | 1%; 1.5%; 2%; no visible discontinuity at tile boundaries; 1300 CPU hours, a factor 2600 below the GADGET-4 run | up to k ≃ 0.4 h/Mpc | Aubin et al. 2026, arXiv:2610.26639 [src: abstract] |
| DESI DR1 EZmock covariance against a data-tuned analytic one | variance | too small by 10–40% depending on the sample; corrected by rescaling | configuration space | arXiv:2411.12027 [src: Sect. 4] |

The 10% on parameter errors (arXiv:1806.09497 [src: abstract]) is the number to quote when a referee asks how well an approximate-mock covariance is known in a periodic box; on a real survey the one measured case, DESI DR1, needed a rescaling of 10 to 40% (arXiv:2411.12027 [src: Sect. 4]; last row). It must be stated together with the finite-mock correction to the error bar, whose size is in `cosmo-statistics-inference`.

## 4. Baryonic suppression of the matter power spectrum
<!-- key: baryonic-suppression-of-the-matter-power -->

The quantity is the response R(k) = P_hydro(k) / P_gravity-only(k) of the total matter power spectrum.

| Simulation or data | Suppression | Scale | Reference, flag |
|---|---|---|---|
| OWLS AGN run | 1% at k about 0.3, 10% at k about 1, 30% at k about 10 h/Mpc; cooling raises power only for k > 70 h/Mpc | z = 0 | van Daalen et al. 2011, arXiv:1104.1174 [src: abstract] |
| Non-radiative and cooling-plus-star-formation runs, no AGN | suppression of at most 1% at 1 < k < 10 h/Mpc; boost of 2% and 10% at k about 20 h/Mpc | not stated | Jing et al. 2005, arXiv:astro-ph/0512426 [src: abstract] |
| Homogenised comparison of BAHAMAS, OWLS AGN, EAGLE, Illustris, TNG100, TNG300, Horizon-AGN | all suppress over 1 < k < 20 h/Mpc, by 10–30% at k = 10 h/Mpc; cross-over between k = 20 and 100 h/Mpc | z = 0 | van Daalen et al. 2019, arXiv:1906.00968 [src: Sect. 3.8, Fig. 14] |
| FLAMINGO, where the minimum sits | k = 8–10 h/Mpc at z = 0 for all gas-fraction variations; k = 6 h/Mpc at z = 2 for the fiducial model | z = 0–2 | arXiv:2410.17109 [src: Sects. 3.2 and 4.1.1] |
| CAMELS Latin hypercubes | P_hydro/P_Nbody reaches about 50% at k about 10 h/Mpc in strong-feedback runs | z = 0, 25 Mpc/h boxes | arXiv:2010.00619 [src: Sect. IV.1.3] |
| Horizon-AGN | less than 15% at k about 10 h/Mpc; smaller than other simulations, read by the authors as AGN feedback that is not strong enough | z = 0 | Chisari et al. 2018, arXiv:1801.08559 [src: abstract] |
| IllustrisTNG | total matter power damped by up to 20% on scales up to k about 10 h/Mpc | redshift not stated in the abstract | Springel et al. 2017, arXiv:1707.03397 [src] |
| FLAMINGO (suite paper) | halo mass function and matter power spectrum suppressed by up to about 20% | hydrodynamical against dark-matter-only | Schaye et al. 2023, arXiv:2306.04024 [src: abstract] |
| Baryonic correction model with X-ray and SZ cluster data | starts above k about 0.5 h/Mpc, maximum 10–25% around k about 2 h/Mpc | redshift not stated in the abstract | Schneider & Teyssier 2015, arXiv:1510.06034 [src] |
| FLAMINGO | stronger with lower group and cluster gas fractions, with jets instead of thermal AGN feedback, and with lower stellar masses at fixed gas fraction; cosmology dependence about 1% for k < 10 h/Mpc; the response strengthens and its minimum moves to smaller scales as redshift decreases | z ≤ 3 | Schaller et al. 2024, arXiv:2410.17109 [src: abstract] |
| Data: eROSITA gas fractions + SDSS/DESI × ACT kSZ, baryonification | 10 ± 2% at k = 1 h/Mpc; stronger than fiducial FLAMINGO and BAHAMAS | 0 < z < 1 | Siegel et al. 2025, arXiv:2512.02954 [src: abstract] |
| Data: HSC-XXL gas fractions alone (the data the fiducial simulations were calibrated to) | 5 ± 4% at k = 1 h/Mpc | 0 < z < 1 | arXiv:2512.02954 [src] |

How the suites compare with gas observations, 2024–2026:

| Test | Outcome | Reference, flag |
|---|---|---|
| DES Y3 lensing + ACT DR5 kSZ, baryonification | mean feedback more extreme than most hydrodynamical simulations; S8 = 0.823 +0.019/−0.020 | Bigwood et al. 2024, arXiv:2404.06098 [src: abstract] |
| DESI Y1 × ACT kSZ against FLAMINGO, ANTILLES, BAHAMAS, SIMBA, FABLE | fiducial feedback models disfavoured at more than 3σ; stronger-AGN variants of FLAMINGO and BAHAMAS, and SIMBA, within 2σ; kSZ amplitude predicts the P(k) suppression as well as baryon fractions do | Bigwood et al. 2025, arXiv:2510.15822 [src] |
| eROSITA X-ray + DESI × ACT kSZ + lensing against the fiducial 1 Gpc FLAMINGO | eROSITA gas fractions 2× lower than the simulation; kSZ combined more than 8σ discrepant; the strongest-expulsion variant fits | Siegel et al. 2025, arXiv:2509.10455 [src] |
| DESI DR2 BGS and LRG lensing-to-kSZ ratio (HSC Y3 shear, ACT DR6) against Illustris, IllustrisTNG, SIMBA, FLAMINGO | fiducial FLAMINGO tracks the radial gas fraction most closely; Illustris-1 and TNG300-1 bracket the data at small radii | Liu et al. 2026, arXiv:2609.22466 [src] |

The last two rows disagree on whether fiducial FLAMINGO is excluded. This is the live debate recorded in `open-questions.md` §1.1; the sibling skills `cosmo-weak-lensing` and `cosmo-cmb-lss-cross-correlations` quote the same four papers with the same numbers.

What controls the suppression: the mean baryon fraction of groups predicts the z = 0 effect to 1% for k < 1 h/Mpc across OWLS, cosmo-OWLS and BAHAMAS [src: abstract] (arXiv:1906.00968; the fitted relation and its limits are in `systematics.md` §3), and to about the percent level for k ≲ 10 h/Mpc and z ≤ 3 across ANTILLES [src: abstract] (arXiv:2305.09710). Differences in group baryon fractions explain the quantitative disagreement between older predictions [src: abstract] (arXiv:1906.00968).

## 5. Mock counts used by surveys
<!-- key: mock-counts-used-by-surveys -->

| Analysis | Covariance source | Mock count | Reference, flag |
|---|---|---|---|
| eBOSS DR16 BAO and RSD | EZmock sample covariance | 1000 per tracer | arXiv:2007.08997 [src: abstract] |
| DESI DR1 BAO | analytic (RascalC, configuration space) as the fiducial choice, validated against EZmocks | 1000 EZmocks per Galactic cap | arXiv:2411.12027 [src: Sect. 2.1] |
| DESI DR1 full shape | EZmock sample covariance with a correction, because the analytic Fourier-space covariance did not reproduce the expected measurements | 1000 per cap | arXiv:2411.12027 [src: Sect. 2.1] |
| DESI DR1 systematic tests | AbacusSummit HOD mocks | 25 boxes | arXiv:2404.03008 [src: abstract] |
| DESI DR1 peculiar velocities | DESI-PV mocks | 675 | arXiv:2512.03228 [src: abstract] |
| Euclid | no cosmological analysis published at the snapshot [sec: `cosmo-weak-lensing` and `cosmo-galaxy-clustering` SKILL.md]; the reference mock is one Flagship 2 light-cone | 1 | arXiv:2405.13495 [src] |

Two points about these counts. The DESI BAO covariance is not a mock covariance: the mocks validate an analytic one. And the DESI EZmocks are calibrated on AbacusSummit HOD mocks, which are calibrated on the one-percent survey, so the chain from data to covariance has two fitted layers [src] (arXiv:2411.12027).

At fixed number of mocks the finite-mock inflation of the error bar grows with the length of the data vector; the correction factors and their papers are in `cosmo-statistics-inference` and are not repeated here.

## 6. Lyα simulation accuracy
<!-- key: lyalpha-simulation-accuracy -->

| Statement | Number | Conditions | Reference, flag |
|---|---|---|---|
| Resolution for converged flux statistics | 20 kpc/h cells for 1% | Nyx, to k = 10 h/Mpc, 2 ≤ z ≤ 4 | arXiv:1406.6361 [src: abstract] |
| Box size | L > 40 Mpc/h for sub-percent missing-mode error | Nyx | arXiv:1406.6361 [src: abstract] |
| Splicing accuracy | 10% level on P1D | Nyx test | arXiv:1406.6361 [src: abstract] |
| Eulerian versus SPH | ≲ 1% in P1D | Nyx versus CRK-HACC with tessellated density; the SPH-kernel density biases flux statistics, most at z about 5 | arXiv:2207.05023 [src] |
| AGN feedback on P1D | suppression at all scales, growing to low z; neglect shifts σ_8 by 2% and n_s by 1% (twice the then-current error on n_s) | Horizon-AGN series, z = 4.25–2.0 | arXiv:2002.02822 [src: abstract] |
| LaCE | sub-percent, k_∥ = 0.1–4 Mpc⁻¹, z = 2–4.5; percent level to 8 Mpc⁻¹ | includes unseen ΛCDM extensions | arXiv:2305.19064 [src: abstract] |
| ForestFlow | 3% on P3D to k = 5 Mpc⁻¹; 1.5% on P1D to k_∥ = 4 Mpc⁻¹ | z = 2–4.5 | arXiv:2409.05682 [src: abstract] |
| PRIYA | interpolation error < 1%; percent-level convergence, z = 5.4–2.2 | 120 Mpc/h boxes | arXiv:2306.05471 [src: abstract] |
| Lyssa | sub-percent convergence of P1D per run | 4096³ cells in 120 Mpc | arXiv:2412.05372 [src: abstract] |
| Lyssa on eBOSS DR14 | A_Lyα < 7.6 (95%), n_Lyα = −2.369 ± 0.008; Planck best fit A_Lyα = 8.79, n_Lyα = −2.363; with a mean-transmission prior A_Lyα = 9.8 ± 1.1 | the low amplitude is driven by the mean-flux degeneracy | arXiv:2412.05372 [src: abstract] |

A 1% emulator error is an interpolation error inside the training set. It says nothing about physics absent from the simulations (patchy reionisation, AGN feedback), which the rows above show to be at the percent level or more.

## 7. Constrained simulations: quantified results
<!-- key: constrained-simulations-quantified-results -->

| Quantity | Value | Context | Reference, flag |
|---|---|---|---|
| Reduction of cell-to-cell scatter in constrained runs | factor 2–3 at 5 Mpc/h | CLUES, inner region | arXiv:1510.04900 [src] |
| Scatter between simulated and reconstructed velocity fields | 104 ± 4 km/s | CLUES | arXiv:1510.04900 [src: abstract] |
| Smallest scale of accurate 2LPT BORG reconstruction | about 6 Mpc/h | SDSS DR7-like mock | arXiv:1203.3639 [src] |
| Number of COLA steps adequate for the density field around local clusters | 20 (virial masses still unconverged) | within 135 Mpc/h | arXiv:2304.09193 [src: abstract] |
| Local underdensity | about 5% relative to the mean | SIBELIUS-DARK, to 200 Mpc | arXiv:2202.04099 [src: abstract] |
| Local underdensity | "no evidence for a large local underdensity" | Manticore-Local | arXiv:2505.10682 [src] |
| Cluster counterparts | 14, each within 1°, detected at 2–4σ across the posterior | Manticore-Local | arXiv:2505.10682 [src: abstract; Sect. 3.4.2] |
| Reconstructed volume and resolution | (4 Gpc/h)³ to z about 0.7 at about 4 Mpc/h | Manticore-Deep | arXiv:2606.10020 [src: abstract] |
| CMB-lensing cross-correlation of the reconstruction | 7.4σ (Planck PR3) | Manticore-Deep | arXiv:2606.10020 [src: abstract] |
| kSZ from reconstructed velocities | 3.5σ, 64,750 clusters, Planck 217 GHz | Manticore-Deep | arXiv:2606.10020 [src: abstract] |
| Constrained ensemble from velocities | 100 runs, 512³ in (500 Mpc/h)³, Cosmicflows-4 to 160 Mpc/h | Hamlet-PM | arXiv:2602.03699 [src: abstract] |
| S8 from density–velocity cross-correlation with a linear reconstruction | 0.793 ± 0.035; in agreement with weak lensing and Planck, in strong disagreement with some peculiar-velocity studies | validation framework for velocity reconstructions | arXiv:2502.00121 [src: abstract] |
| Differentiable particle mesh | 6 steps for percent-level P(k) at k about 0.2 h/Mpc, 512³, a few seconds on GPU | DISCO-DJ | arXiv:2510.05206 [src: abstract] |
| Lyα-tomography reconstruction | r = 0.95 on deformation-tensor eigenvalues | TARDIS, 30 m-class mock data | arXiv:1903.09049 [src: abstract] |

The two local-density statements come from different inferences on overlapping data and are not reconciled in the abstracts read; see `open-questions.md` §1.6. The S8 value is a by-product of a validation paper and uses linear theory; current peculiar-velocity growth measurements are in `cosmo-peculiar-velocities`.


## 8. History of the key numbers
<!-- key: history-of-the-key-numbers -->

Each line gives the sequence in time, so that a reader can tell which statement is the current one.

**Agreement between N-body codes on the matter power spectrum.**
- 2008: 10% between ten codes (arXiv:0706.1270); differences of more than 10% at k about 10 h/Mpc between mesh and tree codes, as recalled in arXiv:1503.05920, Sect. 2.3.
- 2016: 1% to k = 1 h/Mpc and 3% to k = 10 h/Mpc, three codes at standard settings (arXiv:1503.05920 [src: abstract]).
- 2019: Abacus on the same initial conditions; time-step convergence below 0.3% to k = 10 h/Mpc (arXiv:1810.02916 [src: abstract]).
- 2022: 1% to k = 10 h/Mpc for Abacus, GADGET and SWIFT with DESI settings (arXiv:2112.09138, abstract). This is the figure to quote today, with its condition.
- 2026: below about 1% for a fourth code family after tuning (arXiv:2605.28581).

**Baryonic suppression at k = 1 h/Mpc, z = 0.**
- 2011: 10% in the OWLS AGN run (arXiv:1104.1174 [src: abstract]), the result that made baryons a cosmological systematic.
- 2015: 10–25% maximum near k about 2 h/Mpc from the baryonic correction model with cluster gas data (arXiv:1510.06034 [src: abstract]).
- 2018: weaker in Horizon-AGN (less than 15% even at k about 10) and up to 20% by k about 10 in IllustrisTNG (arXiv:1801.08559, arXiv:1707.03397 [src: abstract of each]).
- 2020: the spread is explained by the baryon fraction of groups (arXiv:1906.00968).
- 2023–2025: FLAMINGO, calibrated to pre-eROSITA gas fractions, up to about 20% in its suite paper; its strongest-feedback variants match lensing-based analyses but are in strong tension with the X-ray gas fractions used for the calibration [src: abstract] (arXiv:2306.04024, arXiv:2410.17109).
- 2025: data-driven 10 ± 2% from kSZ and eROSITA, against 5 ± 4% from the older X-ray sample (arXiv:2512.02954). Current, and disputed (arXiv:2609.22466 [src: abstract of each]).

**Gravity-only emulator accuracy.**
- 2003–2012: fitting functions, HALOFIT (arXiv:astro-ph/0207664) and its revision at 5% for k ≤ 1 h/Mpc and 10% for 1 ≤ k ≤ 10 h/Mpc (arXiv:1208.2701 [src: abstract of each]).
- 2009–2010: Coyote emulator, 1% to k about 1 h/Mpc over wCDM (arXiv:0912.4490).
- 2017: Mira-Titan II, about 4% over eight parameters (arXiv:1705.03388).
- 2019–2021: better than 2% for the halo–matter cross-correlation and 4% for the halo auto-correlation (arXiv:1811.09504); 2% in ΛCDM and 3% with dynamical dark energy and massive neutrinos for BACCO to k = 5 h/Mpc (arXiv:2004.06245); 1% for EuclidEmulator2 to k = 10 h/Mpc (arXiv:2010.11288 [src: abstract of each]).
- 2023: 2–3% for the final Mira-Titan emulator over eight parameters (arXiv:2207.12345); 1% to k = 1 h/Mpc for Aemulus ν (arXiv:2303.09762).
- 2026: a nine-parameter emulator of the Dark Quest II programme reports sub-percent accuracy to the particle Nyquist scale (abstract read; outside the source list).

**Covariance mocks for spectroscopic surveys.**
- BOSS DR9: 600 PTHalos mocks (arXiv:1203.6609). BOSS DR12: 12,288 MultiDark-Patchy light-cones (arXiv:1509.06400 [src: abstract of each]).
- eBOSS DR16: 1000 EZmocks per tracer (arXiv:2007.08997, abstract).
- DESI DR1: 1000 EZmocks per Galactic cap, used directly for the full shape and as validation of an analytic covariance for BAO (arXiv:2411.12027, Sect. 2.1).
- DESI DR1 peculiar velocities: 675 (arXiv:2512.03228, abstract).

**Lyα forest simulations.**
- 2015: 20 kpc/h and 40 Mpc/h requirements; splicing good to 10% (arXiv:1406.6361 [src: abstract]).
- 2017: Sherwood, up to 160 Mpc/h (arXiv:1605.03462, abstract).
- 2020: AGN feedback worth 2% on σ_8 (arXiv:2002.02822).
- 2023: grid and particle codes agree to 1% in P1D with a tessellated density (arXiv:2207.05023); PRIYA with patchy reionisation (arXiv:2306.05471); Sherwood-Relics (arXiv:2207.13098).
- 2023–2025: emulators at the sub-percent to 3% level (arXiv:2305.19064, arXiv:2409.05682, arXiv:2412.05372).
- 2026: 2LPT-based synthetic spectra replace lognormal ones for the DESI DR2 full-shape validation (arXiv:2607.27412).

**Constrained simulations.**
- 2013: 2LPT field-level inference, about 6 Mpc/h (arXiv:1203.3639).
- 2016: velocity-constrained realisations to 150 Mpc/h (arXiv:1510.04900, abstract).
- 2019: particle-mesh dynamics inside the sampler, 2M++ (arXiv:1806.11117).
- 2022: SIBELIUS-DARK to 200 Mpc with public catalogues (arXiv:2202.04099, abstract).
- 2024: posterior resimulation established as the route to halo masses (arXiv:2304.09193).
- 2025: Manticore-Local, a posterior ensemble validated on velocities (arXiv:2505.10682, arXiv:2502.00121).
- 2026: Manticore-Deep over (4 Gpc/h)³ (arXiv:2606.10020); forward modelling from Cosmicflows-4 velocities (arXiv:2602.03699).

## Not verified
<!-- key: not-verified -->

- k limits of the Mira-Titan IV emulator: not found in the sections read (the abstract says "wide range"); its redshift range is now in §2.
- Mock counts behind the DES and Euclid covariances, and the DES choice of an analytic covariance: a DES Y3 covariance paper was read during the first build but lies outside the source list; see `cosmo-weak-lensing` and `cosmo-statistics-inference`.
- Number of CoLoRe-2LPT realisations used for DESI DR2.
- Quantitative results of arXiv:2511.20423 on box replication.
- The sub-percent figure of the 2026 Dark Quest II emulator, the 2% of a 2025 COLA-based w0wa emulator against EuclidEmulator2, and the percent-level field-level emulator inside BORG were read in abstracts of papers outside the source list.
- Baryonic suppression at k = 1 h/Mpc in EAGLE, BAHAMAS, SIMBA and MillenniumTNG individually: only their ordering was read (arXiv:2306.04024, Sect. 8; arXiv:1906.00968, Sect. 3.8), not a number for each.
- The per-sample values of the DESI DR1 covariance rescaling (the paper refers to two companion papers for them).
