# Limits and systematics — cosmological simulations and mocks

Scope: where simulations and mocks stop being trustworthy — resolution, box size, sub-grid dependence, galaxy–halo assumptions, covariance from approximate mocks.
Snapshot: 2026-10-07

## 1. Resolution and box-size effects

**Mechanism.** Finite particle mass suppresses small-scale power and makes low-mass halos unreliable; a finite box removes modes longer than L, which biases the growth of the modes that are kept (finite-volume effect) and removes their contribution to the covariance (super-sample covariance).

**Size.**
- Matter power spectrum: 1% precision needs m_p ≤ 10⁹ M_⊙/h and L ≥ 0.5 Gpc/h [src] (Schneider et al. 2015, arXiv:1503.05920).
- Halo statistics: converged to 1% only for halos with more than 500 particles, 2% for more than 200; the dominant uncertainty is the particle loading [src] (DeRose et al. 2018, arXiv:1804.05865). A mock that populates halos of 20 to 50 particles is outside every published convergence statement.
- Halo clustering for DESI: 2.1 × 10⁹ M_⊙/h is sufficient for s > 20 Mpc/h in redshift space [src] (Grove et al. 2021, arXiv:2112.09138). The statement is limited to those scales; small-scale HOD fits are not covered by it.
- Weak-lensing maps built by tiling a small box: Tokiwa et al. 2025 (arXiv:2511.20423) compare 3750 Mpc/h boxes with tiled 625 Mpc/h boxes for higher-order lensing statistics and covariances, separating the replication effect from the missing super-sample modes. Their quantitative results were not read (snippet only).

**Mitigation.** Resolution corrections applied in post-processing (EuclidEmulator2 provides one, arXiv:2010.11288); several box sizes spliced (Mira-Titan combines 111 high-resolution runs with 1776 low-resolution runs and perturbation theory, arXiv:2207.12345); a separate large-volume, low-resolution set for the covariance.

**Validation test a referee expects.** A convergence test at fixed phases with at least one higher resolution, for the statistic actually used, on the scales actually used.

## 2. Initial-condition and time-stepping errors

**Mechanism.** Truncated LPT leaves transients that decay slowly; particle discreteness adds errors that grow from early starts; coarse global time steps (the regime of fast particle-mesh codes) lose small-scale power.

**Size.** Zel'dovich starts at z_i = 49 lose about 2, 4 and 8% of non-linear power at z = 0, 1, 3 and 5% of the halo abundance at 10¹⁵ M_⊙/h [src] (arXiv:astro-ph/0606505). Late-start 3LPT reaches 1% on P(k) and the bispectrum up to the particle Nyquist frequency [src] (arXiv:2008.09588). Halving the Abacus time step changes P(k) by less than 0.3% at k < 10 h/Mpc [src] (arXiv:1810.02916).

**Referee check.** The LPT order and starting redshift are stated; a simulation older than 2006 started with the Zel'dovich approximation is not a percent-level reference at z > 1.

## 3. Sub-grid model dependence

**Mechanism.** Feedback recipes are calibrated on a few observables; anything not calibrated is a prediction that differs between suites. Gas expelled from groups lowers the total matter power spectrum at k ≳ 0.3 h/Mpc.

**Size.** From 1% at k about 0.3 to 30% at k about 10 h/Mpc in the OWLS AGN run [src] (arXiv:1104.1174); less than 15% at k about 10 in Horizon-AGN [src] (arXiv:1801.08559); up to 20% in IllustrisTNG [src] (arXiv:1707.03397). The spread between suites at k = 1 h/Mpc is therefore of the same order as the effect. Data-driven estimates give 10 ± 2% at k = 1 h/Mpc with kSZ and eROSITA, 5 ± 4% with the older X-ray sample [src] (arXiv:2512.02954).

**Secondary effects.**
- Volume: the baryonic response is converged only above (200 Mpc)³ [src] (arXiv:2410.17109); the Horizon-AGN result is sensitive to the presence of its most massive haloes [src] (arXiv:1801.08559).
- Initial conditions: differences between the initial conditions of a hydrodynamical run and its gravity-only twin can produce a 1% offset in large-scale power that is not a baryonic effect [src] (arXiv:1906.00968).
- Back-reaction: the dark matter itself moves by up to a few percent [src] (arXiv:1801.08559).
- Redshift: the evolution is non-monotonic between z = 0 and 5 in Horizon-AGN [src] (arXiv:1801.08559); a single-redshift calibration does not transfer.
- Calibration data: the fiducial FLAMINGO and BAHAMAS runs were calibrated to pre-eROSITA X-ray gas fractions; eROSITA fractions are 2× lower [src] (arXiv:2509.10455).

**Mitigation.** Scale cuts; a parametrised response (baryonification, HMcode, SP(k)) marginalised with or without an external gas prior; a set of bracketing simulations rather than one.

**Validation test a referee expects.** The analysis is repeated with at least two simulations that bracket the plausible range (not two runs of one sub-grid family), and the paper states which variant, not only which suite, was used.

## 4. HOD assumptions and assembly bias

**Mechanism.** A mock galaxy catalogue is a gravity-only halo catalogue plus an occupation model. If occupation depends on halo properties other than mass that also correlate with clustering (assembly bias), or if satellites do not follow the assumed profile and velocity distribution, the mock clustering is wrong in a way that a mass-only HOD fit absorbs into its parameters.

**Size.**
- The mass-only HOD underpredicts the real-space correlation function of TNG300 galaxies by about 15% at 1 < r < 20 Mpc/h [src] (arXiv:1911.02610).
- DESI DR1 BAO: an HOD-dependent shift of 0.19% in α_AP (configuration space, 3.3σ detection) between the vanilla, baseline and extended LRG models on the 25 AbacusSummit boxes; no 3σ detection in the other cases, for which a conservative estimate is adopted [src] (arXiv:2404.03008).
- DESI DR1 full shape: parameter shifts across HOD models are often above 20% of the statistical uncertainty; a systematic covariance C_HOD and a prior-related diagonal term are added to the statistical covariance [src] (arXiv:2411.12023).
- Fast mocks inherit the galaxy–halo model of their calibration set: the DESI EZmocks are tuned to AbacusSummit HOD mocks [src] (arXiv:2411.12027).

**Mitigation.** Extended HODs with assembly-bias, velocity-bias and satellite-profile parameters; tests on a second galaxy model of a different kind (SHAM, a semi-analytic model or a hydrodynamical simulation); a systematic covariance term.

**Validation test a referee expects.** Recovery of the input cosmology on mocks built with a galaxy model different from the one in the fit, at the scales of the fit; the halo particle number of the least massive hosts (500 particles for 1% in arXiv:1804.05865).

**What remains open.** All data analyses with density-split, wavelet and similar statistics use AbacusSummit with an HOD (`cosmo-beyond-two-point`); a 2026 paper titled "Bounding the Effect of HOD Assumptions on Small-Scale Clustering Constraints" was found by the date-sorted search and not read.

## 5. Covariance from approximate mocks

**Mechanism.** A sample covariance needs N_mocks much larger than the data-vector length, which forces approximate dynamics. The approximation changes the non-Gaussian part of the covariance (the trispectrum and super-sample terms), the shot noise through the bias or halo-assignment model, and the survey realism (fibre assignment, systematics weights).

**Size.**
- Against 300 N-body simulations, seven approximate methods reproduce the variance of the power-spectrum multipoles typically within 10%, and give parameter errors within 10% of the N-body covariance [src] (Blot et al. 2018, arXiv:1806.09497). Methods whose clustering amplitude is calibrated only on two-point statistics are the exceptions for the bispectrum covariance, according to the companion bispectrum paper of the same project (abstract read; not in the source list).
- DESI DR1: the analytic configuration-space covariance performs satisfactorily for BAO, but the analytic Fourier-space covariance does not reproduce the expected full-shape measurements, hence a corrected mock covariance for the full shape [src] (Forero-Sánchez et al. 2024, arXiv:2411.12027).
- The shot noise of approximate fibre assignment differs from the real algorithm; the DESI EZmocks use a fast fibre-assignment emulator [src] (arXiv:2411.12027).
- Box replication misestimates cosmic variance; the DESI EZmocks use (6 Gpc/h)³ boxes to avoid it [src] (arXiv:2411.12027), whereas the Flagship 2 full-sky light-cone replicates a 3600 Mpc/h box [src] (arXiv:2405.13495).
- A fixed-amplitude ("fixed and paired") suite has suppressed variance by construction and cannot provide a covariance (arXiv:1603.05253, arXiv:1811.02111).

**Mitigation.** Validate the mock covariance against an analytic one and against a small N-body set; rescale; add systematic covariance terms.

**Validation test a referee expects.** The calibration reference of the mocks, the number of mocks against the length of the data vector, the correction factors applied (see `cosmo-statistics-inference`), and a comparison with an independent covariance estimate.

## 6. Lyα-specific simulation limits

**Resolution and box size pull in opposite directions.** A cell of 20 kpc/h and a box above 40 Mpc/h are the minimum for 1% flux statistics [src] (arXiv:1406.6361); BAO and P3D on large scales need boxes far larger than hydrodynamics can afford at that resolution. The standard escapes are splicing, accurate to about 10% on P1D [src] (arXiv:1406.6361), and emulating a small set of bias and shape parameters that are then attached to linear theory (ForestFlow, arXiv:2409.05682).

**SPH sampling of voids.** The forest at z about 5 comes from low-density gas that SPH samples poorly; the kernel-based density biases flux statistics, and agreement with a grid code at the 1% level required a tessellation-based density [src] (arXiv:2207.05023). A referee should ask how the density was reconstructed in any SPH-based forest prediction at z > 4.

**Thermal and ionisation history.** The choice of UV background changes the mean flux by 10–15% at z = 2 and by a factor 2 at z = 4 [src] (arXiv:1406.6361). Rescaling the optical depth hides this but ties the recovered amplitude to the assumed mean flux: with the same eBOSS data the Lyssa emulator gives A_Lyα < 7.6 without a mean-transmission prior and 9.8 ± 1.1 with one [src] (arXiv:2412.05372).

**Patchy reionisation relics.** Temperature fluctuations seeded by inhomogeneous reionisation persist and add large-scale P1D power at z > 4 [src] (arXiv:2207.13098); patchy helium reionisation does the same at lower redshift [src] (arXiv:2306.05471). A suite with homogeneous reionisation cannot absorb this except through other parameters.

**Galaxy formation.** AGN feedback is not negligible for P1D: 2% on σ_8 and 1% on n_s if ignored [src] (arXiv:2002.02822). Only suites with a galaxy-formation model contain a realistic DLA population (PRIYA, arXiv:2306.05471); the others mask or model DLAs separately.

**Continuum placement.** Comparing a simulation with data needs a correction for continuum-placement bias, uncertain above z = 4 [src] (arXiv:1605.03462).

**Synthetic spectra are not hydrodynamical.** BAO mocks built from Gaussian or lognormal skewers reproduce the BAO signal and the linear biases (arXiv:1912.02763); they are not valid tests of small-scale or broadband physics. The sibling skill records that fσ8 from the forest fails mock validation.

## 7. Constrained-simulation limits

**Constraint scale.** Information from the data reaches down to a scale set by tracer density, noise and the forward model: about 6 Mpc/h for 2LPT BORG on SDSS-like data [src] (arXiv:1203.3639), about 4 Mpc/h for Manticore-Deep [src] (arXiv:2606.10020), a few tens of megaparsecs for velocity-constrained realisations [src] (arXiv:1510.04900). Everything below it in a resimulation is a random draw. A claim about an individual galaxy-scale object in a constrained run is a claim about the prior.

**Dynamics inside the sampler.** Few-step solvers are accurate for the large-scale field and not for halo interiors: 20 COLA steps do not give converged virial masses [src] (arXiv:2304.09193). The remedy is posterior resimulation; a paper that reads masses directly from the inference-resolution field should be questioned.

**Data model.** Galaxy bias, selection and noise are inferred jointly; the result depends on the bias model; the Manticore-Local abstract lists "a refined galaxy bias model" and "physics-informed priors" among its ingredients (arXiv:2505.10682). The Hamlet-PM paper states that its systematic biases "still need to be addressed" (arXiv:2602.03699). Velocity-based methods depend instead on distance errors and their lognormal bias.

**Dependence on the tracer.** Reconstructions from galaxy positions (2M++) and from peculiar velocities (Cosmicflows) use different data with different systematics; agreement between them is a test, and the validation framework of arXiv:2502.00121 finds that the non-linear BORG reconstruction outperforms linear-theory ones against direct distance tracers.

**Point estimate versus ensemble.** A single constrained simulation is one sample. Statements about named objects need their frequency across the posterior ensemble (Manticore-Local quotes 2–4σ detections of its cluster counterparts across the ensemble, arXiv:2505.10682).

**Assumed cosmology.** The prior and the forward model fix the cosmological parameters; consistency tests of the posterior with ΛCDM (power spectrum, halo mass function) check the inference, they do not test ΛCDM independently.

**Validation a referee expects.** Posterior-predictive tests; a comparison with data excluded from the inference (velocities, tSZ, kSZ, CMB lensing); the number of posterior samples; the resolution of the inference and of the resimulation stated separately.


## 8. Emulator and surrogate limits

**Mechanism.** An emulator returns a smooth interpolation with no warning when it is asked for a point its training set does not support, or for physics its simulations do not contain.

**Size.**
- Interpolation error: 1% (EuclidEmulator2), 2–3% (Mira-Titan IV, BACCO), 2.5% RMS and up to 16% (HMcode-2020) [src] (arXiv:2010.11288, arXiv:2207.12345, arXiv:2004.06245, arXiv:2009.01858). These are not interchangeable at Stage-IV precision.
- Simulation error underneath: 1% between codes only with tuned settings (§1 of `results.md`).
- Missing physics: every gravity-only emulator needs a baryonic response on top, whose own emulators are accurate to 1–2.5% with respect to simulations that disagree with each other by more than that (arXiv:2011.15018, arXiv:2507.07892, arXiv:2410.17109).
- Cosmology dependence of the baryonic response: about 1% for k < 10 h/Mpc in FLAMINGO, over a limited set of cosmologies; the authors ask for a wider range before the result is taken as general [src] (arXiv:2410.17109).
- Residual resolution effects: EuclidEmulator2 corrects for them after emulation [src] (arXiv:2010.11288); an emulator without such a correction inherits the resolution bias of its training runs.

**Mitigation.** Compare two emulators built on different codes; keep the posterior away from the design boundary or report when it is not; propagate the quoted error into the likelihood (`cosmo-statistics-inference`).

**Referee check.** The emulator version, its parameter box, and the position of the best fit inside it.

## 9. Light-cone and survey-realism limits

- Pseudo-light-cones made of a few snapshots carry no redshift evolution inside a bin; the DESI DR1 EZmocks are built this way [src] (arXiv:2411.12027).
- Box replication repeats structure along the line of sight and across the sky; Flagship 2 replicates a 3600 Mpc/h box to reach z = 3 over the full sky, while its galaxy catalogue covers one octant [src] (arXiv:2405.13495).
- A mock is as realistic as the observational effects applied to it. The eBOSS EZmocks include photometric and spectroscopic systematics [src] (arXiv:2007.08997); the DESI DR1 EZmocks include an emulated fibre assignment [src] (arXiv:2411.12027); effects not applied cannot be validated on the mocks.
- Mocks calibrated on the data they are used to validate (eBOSS EZmocks, arXiv:2007.08997) reproduce the clustering by construction; agreement between data and mocks is then not a test.
- Synthetic Lyα spectra reproduce DESI statistics within 10%, not at the precision of the measurement [src] (arXiv:2607.27412).

## 10. Neutrino and modified-gravity simulation limits

- Neutrino implementations agree at the sub-percent level on common initial data [src] (arXiv:2211.12457); the eleven N-body implementations compared are "not all independent".
- Modified-gravity codes agree to 1% on the ratio to ΛCDM up to k about 5–10 h/Mpc for three models [src] (arXiv:1506.06384); the absolute spectrum carries the usual gravity-only error, and baryons are not included.
- The quasi-static approximation was tested for the symmetron model only [src] (arXiv:1506.06384).
- Emulators cover neutrino mass up to the largest value simulated (0.5 eV in Aemulus ν, arXiv:2303.09762).

## What a referee checks

For any paper that uses a simulation or a mock set:

1. Code, box size, particle number and particle mass are stated, and the particle mass is compared with the requirement of the statistic (10⁹ M_⊙/h for 1% on P(k); 500 particles per halo for 1% on halo statistics).
2. Initial conditions: LPT order and starting redshift.
3. Convergence is shown for the statistic used, on the scales used, not inherited from a different statistic.
4. For fast particle-mesh mocks: number of steps, force-mesh factor, starting redshift, and the N-body reference they were validated against.
5. For hydrodynamical results: the suite and the variant; what the sub-grid model was calibrated to; whether the observable in question was part of the calibration.
6. For a baryonic correction: which simulations bracket the prior, and whether an external gas observable (X-ray, kSZ, tSZ) constrains it.
7. For an emulator: parameter range, k and z range, quoted error and whether it is propagated; whether the fit sits near the edge of the design.
8. For galaxy mocks: the occupation model, the test with a different galaxy model, and the least massive host halo in particles.
9. For a mock covariance: number of mocks against data-vector length, the correction applied, the calibration reference of the mocks, and whether fixed-amplitude boxes were (wrongly) used.
10. For light-cones: box replication, snapshot spacing, and which observational effects were applied to the mocks and which were not.
11. For Lyα predictions: cell size or particle load against the 20 kpc/h requirement, box size, treatment of the mean flux, thermal-history parametrisation, splicing, reionisation model, and for SPH the density estimator.
12. For a constrained simulation: data used, constraint scale, forward-model accuracy, posterior ensemble size, and validation on independent data.
13. For any "simulation X is ruled out" statement: like-for-like selection (halo mass from lensing, satellites, miscentring), as in arXiv:2510.15822, and whether an amplitude was left free.

## Not verified

- Quantitative size of box-replication and super-sample effects on lensing statistics (arXiv:2511.20423, snippet only).
- Halo-finder dependence (friends-of-friends, spherical overdensity, ROCKSTAR, CompaSO) and its effect on mocks: no source was read.
- Accuracy of ray-tracing and of the Born approximation in lensing light-cones: no source was read.
- Bispectrum covariance from approximate mocks: the companion paper of arXiv:1806.09497 was read in abstract only and is outside the source list.
- Emulator error propagation into a likelihood: treated in `cosmo-statistics-inference`, not re-read here.
- Sensitivity of Local Group analogues to unconstrained small-scale modes: abstract read, outside the source list.
- Fuzzy and self-interacting dark-matter solvers: not researched.
