# Limits and systematics — cosmological simulations and mocks

Scope: where simulations and mocks stop being trustworthy — resolution, box size, sub-grid dependence, galaxy–halo assumptions, covariance from approximate mocks.
Snapshot: 2026-10-13

## 1. Resolution and box-size effects
<!-- key: resolution-and-box-size-effects -->

**Mechanism.** Finite particle mass suppresses small-scale power and makes low-mass halos unreliable; a finite box removes modes longer than L, which biases the growth of the modes that are kept (finite-volume effect) and removes their contribution to the covariance (super-sample covariance).

**Size.**
- Matter power spectrum: 1% precision needs m_p ≤ 10⁹ M_⊙/h and L ≥ 0.5 Gpc/h [src] (Schneider et al. 2015, arXiv:1503.05920).
  - Box size, at fixed particle mass of about 10¹⁰ M_⊙/h, against a 1024 Mpc/h reference at z = 0: a 128 Mpc/h box underestimates P(k) by more than 10%; 256 Mpc/h is accurate to 5% overall (1% at k > 1 h/Mpc); 512 Mpc/h differs by about 1% or less at all wavenumbers. Hence L ≥ 500 Mpc/h against systematic finite-volume effects [src: Sect. 3.2 and Fig. 4, left, of arXiv:1503.05920].
  - Sample variance is a separate requirement: sub-percent statistical error at wavenumber k needs L ≳ 250/k, that is 2.5 Gpc/h for k = 0.1 h/Mpc [src: Eq. 5]; over the whole range of their figure it would need about 12 Gpc/h [src: Sect. 3.2].
  - Mass resolution, in a 512 Mpc/h box against a 2048³ reference: runs with 256³, 512³ and 1024³ particles lose more than 1% of power above k = 0.25, 1 and 4 h/Mpc. The wavenumber up to which a run is accurate to 1% is k_max = k_sn/3, with k_sn the wavenumber where the shot noise (L/N)³ is 1% of P(k); half the particle Nyquist wavenumber, the older rule, does not reproduce the runs [src: Sect. 3.2]. The resulting requirement is m_p ≤ 10⁹ M_⊙/h for 1% up to k = 10 h/Mpc, relaxed to about 8 × 10¹⁰ M_⊙/h for k ≤ 1 h/Mpc [src: Sect. 3.2]. The physical reason: haloes below 10¹¹ M_⊙/h contribute negligibly to P(k), and 10⁹ M_⊙/h particles resolve them with about 100 particles [src: Sect. 3.2].
  - Consequence drawn by the paper: a 4 Gpc/h survey box at that resolution needs 16,000³, four trillion, particles [src: Sect. 3.2], the particle number of Flagship 2.
- Halo statistics: converged to 1% only for halos with more than 500 particles, 2% for more than 200; the dominant uncertainty is the particle loading [src] (DeRose et al. 2018, arXiv:1804.05865). In the body: runs with eight times more particles show the mass function within 1% for haloes of 500 particles or more, the deficit below that depending to good approximation on the particle number alone, as −exp[−(log₁₀N_part − 0.25)/0.557] [src: Sect. IV.2.5 and Eq. 8]; to higher order it depends on the local slope of the mass function, and only above about 1000 particles is it below 1% for all slopes, hence larger errors at high redshift [src: Sect. IV.2.5]. Starting at z = 99 instead of the fiducial z = 49 (2LPT) moves the mass function by more than 1% below M_200b = 10¹³ M_⊙/h, and P(k) near k = 4 h/Mpc at z = 0 at about the 1σ level of the test [src: Sect. IV.2.1]. Against (5 Gpc/h)³ boxes no finite-box effect is seen beyond sample variance [src: Sect. IV.2.6]. The suite treats the halo finder and its settings as part of the mass definition [src: Sect. V]. A mock that populates halos of 20 to 50 particles is outside every published convergence statement. Flagship 2 keeps haloes down to 10 particles and corrects their masses by abundance matching, its mass function being incomplete below about 300 particles [src: Sect. 4.2 of arXiv:2405.13495].
- Halo clustering for DESI: 2.1 × 10⁹ M_⊙/h is sufficient for s > 20 Mpc/h in redshift space [src: abstract] (Grove et al. 2021, arXiv:2112.09138). The statement is limited to those scales; small-scale HOD fits are not covered by it.
- Missing long modes: truncating the initial spectrum at a fraction of the box lowers the two-point function and the number of the most massive haloes and leaves concentrations unchanged, while the median spin falls by about 50% [src] (Power & Knebe 2005, arXiv:astro-ph/0512281). Finite-volume effects are substantial below (500 Mpc/h)³ and negligible above about 1 Gpc/h: the average matter P(k) differs by less than 0.1% between 1 and 4 Gpc/h boxes, no measurable difference is expected in the halo mass function, and covariances scale with volume up to a small super-sample correction, so that boxes of 1–1.5 Gpc/h suffice for most survey requirements [src] (Klypin & Prada 2018, arXiv:1809.03637). The review quotes a box of at least 1000 Mpc/h for percent-level convergence of P(k) and of covariance matrices at z = 0 [sec: arXiv:2112.05165, Sect. 8.1].
- Poorly resolved haloes: the abundance of haloes with fewer than about 100 particles is overestimated, because halo finders take upward fluctuations for objects; the rate of convergence depends on the finder, the force accuracy and the softening [sec: arXiv:2112.05165, Sect. 8.1]. Friends-of-friends masses depend on mass resolution in a way that cannot be corrected in general, because substructure, which depends on redshift and cosmology, enters [src] (More et al. 2011, arXiv:1103.0005). Substructure is not recovered reliably below 30–40 particles by most finders, 10–20 by phase-space finders [src] (Knebe et al. 2011, arXiv:1104.0949).
- Halo definition: the spherical-overdensity mass function is calibrated to ≲ 5% at z = 0 and the amplitude of the "universal" function falls by 20–50% between z = 0 and 2.5 depending on the mass definition [src] (Tinker et al. 2008, arXiv:0803.2706); a halo mass in a mock means nothing without its definition.
- Weak-lensing maps built by tiling a small box: Tokiwa et al. 2025 (arXiv:2511.20423, abstract) compare 3750 Mpc/h boxes with tiled 625 Mpc/h boxes for higher-order lensing statistics and covariances, separating the replication effect from the missing super-sample modes. Their quantitative results were not read (snippet only).

**Mitigation.** Resolution corrections applied in post-processing (EuclidEmulator2 provides one, arXiv:2010.11288); several box sizes spliced (Mira-Titan combines 111 high-resolution runs with 1776 low-resolution runs and perturbation theory, arXiv:2207.12345); a separate large-volume, low-resolution set for the covariance.

**Validation test a referee expects.** A convergence test at fixed phases with at least one higher resolution, for the statistic actually used, on the scales actually used.

## 2. Initial-condition and time-stepping errors
<!-- key: initial-condition-and-time-stepping-errors -->

**Mechanism.** Truncated LPT leaves transients that decay slowly; particle discreteness adds errors that grow from early starts; coarse global time steps (the regime of fast particle-mesh codes) lose small-scale power.

**Size.** Zel'dovich starts at z_i = 49 lose about 2, 4 and 8% of non-linear power at z = 0, 1, 3 and 5% of the halo abundance at 10¹⁵ M_⊙/h [src] (arXiv:astro-ph/0606505). In the Euclid comparison paper, with 1024³ particles in 512 Mpc/h and PKDGRAV3: the difference between Zel'dovich and 2LPT initial conditions is sub-percent and confined to k > 1 h/Mpc in the initial conditions themselves, but by z = 0 it has grown and reaches down to k about 0.1 h/Mpc; a Zel'dovich start needs z_i ≳ 200 for percent accuracy at z = 0, while the rule that the starting redshift should not exceed fifty times the redshift of typical halo formation (Reed et al. 2013, as quoted there) gives z_i ≲ 100 for such boxes; the paper concludes that 2LPT should be used consistently [src: Sect. 3.1 and Fig. 3 of arXiv:1503.05920]. Late-start 3LPT reaches 1% on P(k) and the bispectrum up to the particle Nyquist frequency [src] (arXiv:2008.09588). Halving the Abacus time step changes P(k) by less than 0.3% at k < 10 h/Mpc [src] (arXiv:1810.02916).

**Order against starting redshift, from the figure of Michaux et al. reproduced in the review.** With starting redshifts of 11.5, 24, 49, 99 and 199 and a reference started with 3LPT at z = 24 on a face-centred-cubic lattice with four times the particles: 1LPT underestimates the power spectrum and the equilateral bispectrum on intermediate and small scales, a higher starting redshift reduces this only partly, raising the LPT order improves it much more, and 3LPT started as late as z = 11.5 agrees with the reference at the sub-percent level for k ≲ 2 h/Mpc at z = 0 and z = 1, for both statistics [sec: arXiv:2112.05165, Sect. 8.3 and Fig. 23]. Early starts are not free: tree forces are least accurate when the density is nearly uniform [sec: arXiv:2112.05165, Sects. 5.4.1 and 8.3].

**A measured case in a production suite.** Quijote starts all runs at z = 127, with 2LPT for massless-neutrino models and the Zel'dovich approximation for massive-neutrino ones. On 100 matched pairs of the fiducial model (512³ particles in 1 Gpc/h): the matter P(k) differs by less than 1.5% in real space at all redshifts and by less than 0.5% in redshift space; the power spectrum of haloes above 3.2 × 10¹³ M_⊙/h by about 1% or less at low redshift, more at higher redshift, with little scale dependence; the halo bispectrum at z = 0 to k = 0.5 h/Mpc by around 10% in redshift space and slightly more in real space. The authors recommend taking neutrino-mass derivatives against the Zel'dovich version of the fiducial runs [src: Sect. V.1 and Fig. 13 of arXiv:1909.05273].

**Order against starting redshift, read in Michaux et al. 2020 (arXiv:2008.09588).** Set-up: L = 1 Gpc/h, 1024³ particles on a simple cubic lattice (m_p = 8.04 × 10¹⁰ M_⊙/h), L-GADGET-3; reference with 3LPT at z = 24 on a face-centred-cubic lattice with 4 × 1024³ particles sampling the same modes [src: Sect. 4.1 and Table 2].
- Matter P(k) at z = 3: 3LPT from z = 11.5 is accurate to 1% for k ≲ k_Ny/2; 2LPT and 3LPT from z = 24 and 49 for k ≲ k_Ny/4 and k_Ny/5; Zel'dovich runs from z = 49, 99 or 199 only to about k_Ny/10 [src: Sect. 5.2.2 and Fig. 7].
- Matter P(k) at z = 0 and 1: 3LPT from z = 11.5 is accurate up to the particle Nyquist wavenumber at z = 1 and beyond it at z = 0, as are 2LPT and 3LPT from z = 24 at z = 0. A Zel'dovich start, even at z = 199, is accurate only for k ≲ k_Ny/8 at z = 0 and k_Ny/9 at z = 1: it converges very slowly with earlier starts, and to the discrete solution, not the fluid one [src: Sect. 5.2.2].
- The authors' estimate for two production set-ups: runs started at z = 200 with the Zel'dovich approximation (the first Euclid Flagship run and the runs of the first EuclidEmulator, as they describe them) "could be systematically biased low by about 4%" at k about 4 h/Mpc, and runs started at z = 49 with 2LPT (the BACCO runs) by 1.5% on the same scales [src: Sect. 5.2.2]. The estimate is made at the resolution of their test and is not a measurement on those suites.
- Bispectrum: more sensitive than P(k). At z = 1 percent-level agreement to small scales was not reached with 2LPT at this resolution; 3LPT gives sub-percent errors on the equilateral bispectrum at z = 0 up to the Nyquist wavenumber; the Zel'dovich approximation "should not be used for precision studies" [src: Fig. 9].
- Halo mass function: at z = 0 the high-mass end converges to 1% for all initial conditions, but the earliest starts are low by more than 5% at about 100 particles per halo whatever the LPT order, and Zel'dovich from z = 49 is low by 2–3% even at high masses; at z = 1 Zel'dovich runs are low by at least 5% at all masses; at z = 3 they have more than 20% fewer haloes at fixed mass, 2LPT from z = 24 or 49 is 10–15% low and 3LPT about 10% low [src: Sect. 5.4.2 and Fig. 11].
- Discreteness alone (simple cubic against the oversampled lattice, same LPT order): with a start at z = 49 the power near the Nyquist wavenumber is low by about 8% at z = 3 and 3% at z = 1; with a start at z = 11.5 by at most about 2%, 1% and 0.4% at z = 3, 1 and 0. The suppression does not depend on the LPT order and peaks at intermediate redshift, before haloes dominate those scales [src: Sect. 5.2.1 and Fig. 6].
- The errors grow with the order of the statistic (kurtosis more than skewness, bispectrum more than power spectrum) and are largest at high redshift; the optimal starting redshift depends on the mass resolution and is earlier at higher resolution [src: Sect. 6].

**Discreteness near the Nyquist wavenumber.** Without a correction for the growing modes of the particle lattice, 1% accuracy on P(k) is reached only down to k_Nyquist/4 with 2LPT, and down to k_Nyquist/13 with first-order initial conditions; with the rescaling of Garrison et al. it reaches k_Nyquist [src] (arXiv:1605.02333).

**Agreement between codes, and its dependence on redshift and on settings.** Euclid comparison (RAMSES, PKDGRAV3, GADGET-3; one set of 2LPT initial conditions at z = 49; L = 500 Mpc/h, 2048³ particles; "standard" run parameters: RAMSES refined to 2 kpc/h, PKDGRAV3 softening 0.02 of the mean particle separation with opening angle 0.7, GADGET-3 softening 10 kpc/h with a 2048³ mesh) [src: Sect. 2.1 of arXiv:1503.05920]:
- P(k) within 1% for k ≤ 1 h/Mpc at all redshifts measured (z = 0, 1, 2, 3.8); within 3% for 1 < k < 10 h/Mpc at z ≤ 1; about 5% at z = 2 and 10% at z = 3.8, where the adaptive-mesh code resolves the small haloes that dominate the signal less well than the tree codes [src: Sect. 2.3 and Fig. 1].
- On the largest scales the maximum difference is about 0.4%, against about 3% and 2% in the 2008 and 2010 comparisons of Heitmann et al.; the systematic offset of more than 10% at k about 10 h/Mpc between mesh and tree codes seen in 2008 has disappeared [src: Sect. 2.3]. The 2008 project itself quotes agreement at the 10% level for P(k) and the mass function (Heitmann et al. 2007, arXiv:0706.1270) [src].
- Varying the mesh size of GADGET-3 and the time-step criterion of all three codes changes P(k) at the sub-percent level below k about 10 h/Mpc, less than the differences between codes [src: Sect. 2.3 and Appendix A]. The paper warns that parameters cannot be tuned for agreement, since the codes could converge to the wrong answer.
- Later reruns of the same initial conditions with Abacus, L-GADGET-3 and GADGET-4 bring four codes within 0.4% up to k about 2 h/Mpc and within 2% up to k about 10 h/Mpc at z = 0, and the stacked density profiles of the 25 most massive haloes within a percent down to 10 kpc/h; the original GADGET-3 run is now thought to have had poorer time integration or force accuracy [sec: arXiv:2112.05165, Sect. 8.5 and Fig. 24].
- DESI comparison (Abacus, GADGET-2, SWIFT and the quasi-N-body FastPM, from identical Panphasia initial conditions at z = 199, at three resolutions of 1296³, 1728³ and 2592³ particles, compared at z = 1 and z = 2, not at z = 0) [src: Sects. 3.2 and 5.2 of arXiv:2112.09138]:
  - between the three N-body codes at fixed resolution: P(k) within 0.1% at k < 0.1 h/Mpc, below 1% at k = 2 h/Mpc and within 1% at k = 10 h/Mpc, at all three resolutions and both redshifts [src: Fig. 4 and Sect. 5.2];
  - between resolutions of one code: within 1% at k = 2 h/Mpc and within 4% at k = 10 h/Mpc; one step in resolution lowers the power by up to 2% at k = 10 h/Mpc [src: Fig. 3 and Sect. 5.2]. Resolution therefore moves P(k) more than the choice of code;
  - FastPM, run with force-mesh factor B = 2 and 46 steps linear in the scale factor, departs from the N-body codes at the 1% level for k > 0.5 h/Mpc [src: Sects. 3.1.4 and 5.2];
  - the comparison exposed an error of about 0.5% in the large-scale growth of SWIFT, since corrected; rescaling the initial spectrum by the linear growth factor did not reproduce the large-scale simulated power at sub-percent level, whereas 2LPT evolved to low redshift did [src: Sect. 3.2];
  - haloes (ROCKSTAR): matched-halo properties within 1% between codes above 10¹³ M_⊙/h; mass functions within 1% between codes for 10¹² to 10¹³·⁵ M_⊙/h at z = 1 and within 10% up to 10¹⁴·⁵ M_⊙/h; the effect of resolution is larger than that of the code, the medium (low) resolution departing from the high one by more than 1% below 10¹² (10¹²·⁵) M_⊙/h [src: Sect. 4.2, Figs. 9 and 10];
  - halo clustering for mass limits of 10¹¹ and 10¹¹·⁵ M_⊙/h, which bracket the expected minimum host mass of DESI emission-line galaxies: all codes agree within the expected DESI year-1 uncertainty above 10 Mpc/h and within the year-5 uncertainty above 20 Mpc/h; the medium resolution agrees with the high one above 20 Mpc/h; the authors conclude that "one should be more careful choosing simulation resolution than choosing the N-body code" and draw no conclusion on the fitness of a run for a given DESI analysis [src: Sect. 5.2].
- Against fitting functions and emulators of the time: the revised HALOFIT agrees with the simulations to better than 5% on all scales and redshifts measured; the Coyote emulator to about 3% at z = 0 and 5% at z = 1, the simulations giving more power at k ≳ 1 h/Mpc, partly because the emulator was calibrated on GADGET runs [src: Sect. 3.3 and Fig. 5 of arXiv:1503.05920].

**Referee check.** The LPT order and starting redshift are stated; a simulation older than 2006 started with the Zel'dovich approximation is not a percent-level reference at z > 1.

## 3. Sub-grid model dependence
<!-- key: sub-grid-model-dependence -->

**Mechanism.** Feedback recipes are calibrated on a few observables; anything not calibrated is a prediction that differs between suites. Gas expelled from groups lowers the total matter power spectrum at k ≳ 0.3 h/Mpc.

**Size.** From 1% at k about 0.3 to 30% at k about 10 h/Mpc in the OWLS AGN run [src] (arXiv:1104.1174); less than 15% at k about 10 in Horizon-AGN [src] (arXiv:1801.08559); up to 20% in IllustrisTNG [src] (arXiv:1707.03397). The spread between suites at k = 1 h/Mpc is therefore of the same order as the effect. Side by side in one homogenised comparison (fiducial BAHAMAS, OWLS AGN, EAGLE, Illustris, TNG100, TNG300, Horizon-AGN, all with stellar and AGN feedback): every run suppresses the total matter power over 1 < k < 20 h/Mpc, by 10–30% at k = 10 h/Mpc, with a cross-over to enhancement between k = 20 and 100 h/Mpc; Illustris is the strongest on 0.1 < k < 10 h/Mpc because its radio-mode feedback empties groups; TNG100 (75 Mpc/h) and TNG300 (205 Mpc/h) agree with each other for k < 10 h/Mpc and with Horizon-AGN once a large-scale offset of about 0.7% in the latter is removed; MassiveBlack-II suppresses only at k ≲ 2 h/Mpc. The authors state that the runs "certainly do not agree at the level required for Stage IV weak lensing surveys" [src: Sect. 3.8 and Fig. 14 of arXiv:1906.00968]. Earlier, without AGN feedback, the effect was 1% or less at 1 < k < 10 h/Mpc with a boost at k about 20 h/Mpc (arXiv:astro-ph/0512426) [src]. Data-driven estimates give 10 ± 2% at k = 1 h/Mpc with kSZ and eROSITA, 5 ± 4% with the older X-ray sample [src] (arXiv:2512.02954).

**The one-parameter relation.** With f̃ the mean baryon fraction inside R_500c of haloes of M_500c = 6 × 10¹³ to 2 × 10¹⁴ M_⊙ in units of Ω_b/Ω_m [src: Eq. 4 of arXiv:1906.00968], the fractional change of the z = 0 matter power at k = 0.5 h/Mpc follows −exp(−5.990 f̃ − 0.5107) within 1% for the cosmo-OWLS and BAHAMAS runs in 400 Mpc/h boxes and for EAGLE, Illustris, TNG100, TNG300 and Horizon-AGN; the suppression is monotonic in f̃ at least for k ≲ 3 h/Mpc [src: Sect. 3.9, Figs. 15 and 16]. The baryon fraction is used instead of the gas fraction because overcooling also lowers the gas fraction without removing mass from the halo.

**What the FLAMINGO suite paper states about the spread (z = 0)** [src: Sect. 8, Figs. 22 and 23 of arXiv:2306.04024]:
- The response is converged with box size between 1 and 2.8 Gpc. With resolution, the runs with baryon particle masses of 10¹⁰ and 10⁹ M_⊙ depart from the 10⁸ M_⊙ run by more than 1% above k = 3 and k = 20 h/Mpc.
- Lower cluster gas fractions give stronger suppression; uncertainties in the stellar mass function matter only for k ≳ 10 h/Mpc; jet feedback gives a different scale dependence at fixed gas fraction, stronger on larger scales.
- The variants calibrated to gas fractions shifted by ±2σ are not safe upper and lower limits: fiducial BAHAMAS, whose gas fractions are close to fiducial FLAMINGO, predicts a suppression as strong as the −4σ or even −8σ variants depending on k. Gas and star fractions inside R_500c do not fully fix the suppression; the distance to which gas is displaced also enters.
- MillenniumTNG, EAGLE, IllustrisTNG and Horizon-AGN predict very small suppression because their cluster baryon fractions are higher than observed; some cosmo-OWLS models and Illustris predict much stronger suppression because theirs are too low.
- The van Daalen et al. relation between P_hydro/P_DMO at k = 1 h/Mpc and the mean baryon fraction of 10¹⁴ M_⊙ haloes holds for nearly all simulations to about 0.01 in the ratio, also at k = 0.5 and 2 h/Mpc; deviations are larger at k = 10 h/Mpc. Illustris and SIMBA are the outliers, perhaps because of their boxes of about 100 Mpc. The paper stresses that the absolute error on the ratio is what matters: on scales k < 1 h/Mpc P_hydro is only a few percent below P_DMO.
- The cosmology dependence is small in the four variations run, none of which changes the cosmic baryon fraction much.

**Secondary effects.**
- Volume: the baryonic response is converged only above (200 Mpc)³ [src] (arXiv:2410.17109). In the body: with the fiducial FLAMINGO model in boxes of 50 Mpc to 2.8 Gpc, the response at z = 0 and z = 1 is within 1% of the largest box up to k about 10 h/Mpc for sides above 200 Mpc; 400 Mpc boxes are not converged to 0.5% even at k about 1 h/Mpc, and the deviation is larger at higher redshift, where the rare massive haloes are missing. The authors caution that responses from Illustris, EAGLE, Horizon-AGN, SIMBA and CAMELS, all in volumes of (100 Mpc)³ or less, are "likely not converged" and, if the sign is the same as in FLAMINGO, overestimate the response at k < 4 h/Mpc, whereas the TNG300 response is converged, as MillenniumTNG confirms [src: Sect. 2.3, Fig. 1 and Sect. 5 of arXiv:2410.17109]; the Horizon-AGN result is sensitive to the presence of its most massive haloes [src] (arXiv:1801.08559).
- Initial conditions: differences between the initial conditions of a hydrodynamical run and its gravity-only twin can produce a 1% offset in large-scale power that is not a baryonic effect [src] (arXiv:1906.00968).
- Back-reaction: the dark matter itself moves by up to a few percent [src] (arXiv:1801.08559).
- Redshift: the evolution is non-monotonic between z = 0 and 5 in Horizon-AGN [src] (arXiv:1801.08559); a single-redshift calibration does not transfer. In FLAMINGO the response strengthens with time: its minimum moves from k = 6 h/Mpc at z = 2 to 10 h/Mpc at z = 0 and the onset from k about 1 to about 0.1 h/Mpc; for the gas-fraction variations at z = 0 the minimum stays at k = 8–10 h/Mpc, so that the gas fraction changes the depth more than the range of scales; stronger-feedback models evolve more between z = 1 and 0 [src: Sects. 3.2, 4.1.1 and 4.2 of arXiv:2410.17109].
- One parameter is not enough: fed with the baryon fractions of the FLAMINGO runs, the SP(k) model built on ANTILLES does not reproduce their response, which the FLAMINGO authors read as the need for more than one parameter [src: Sect. 5 and Fig. 12 of arXiv:2410.17109]; the same follows from the jet runs and from the BAHAMAS comparison above.
- Reach of the FLAMINGO family: its emulator, built on nine models over k = 10⁻¹·⁵ to 10¹·⁵ h/Mpc and z ≤ 3, covers almost all published responses; the −8σ thermal and jet variants resemble the cosmo-OWLS runs with ΔT_AGN = 10⁸·³ and 10⁸·⁵ K often used as a strong-feedback reference; Illustris and the strongest cosmo-OWLS run are outside its reach, and below −8σ the response saturates (an extrapolation of the emulator) [src: Sects. 4.1.1 and 4.4.1 of arXiv:2410.17109].
- Cosmology: for two feedback models rerun in a low-S₈ cosmology the response differs from the fiducial-cosmology emulator by less than 1% at k < 10 h/Mpc; larger differences, up to a few percent at k = 10 h/Mpc, are expected for cosmologies that change the mass–concentration relation more, and a dependence on Ω_b/Ω_m is expected and untested [src: Sect. 4.3 of arXiv:2410.17109].
- Calibration data: the fiducial FLAMINGO and BAHAMAS runs were calibrated to pre-eROSITA X-ray gas fractions; eROSITA fractions are 2× lower [src] (arXiv:2509.10455).

**Mitigation.** Scale cuts; a parametrised response (baryonification, HMcode, SP(k)) marginalised with or without an external gas prior; a set of bracketing simulations rather than one.

**Validation test a referee expects.** The analysis is repeated with at least two simulations that bracket the plausible range (not two runs of one sub-grid family), and the paper states which variant, not only which suite, was used.

## 4. HOD assumptions and assembly bias
<!-- key: hod-assumptions-and-assembly-bias -->

**Mechanism.** A mock galaxy catalogue is a gravity-only halo catalogue plus an occupation model. If occupation depends on halo properties other than mass that also correlate with clustering (assembly bias), or if satellites do not follow the assumed profile and velocity distribution, the mock clustering is wrong in a way that a mass-only HOD fit absorbs into its parameters.

**Size.**
- The mass-only HOD underpredicts the real-space correlation function of TNG300 galaxies by about 15% at 1 < r < 20 Mpc/h [src] (arXiv:1911.02610).
- DESI DR1 BAO: an HOD-dependent shift of 0.19% in α_AP (configuration space, 3.3σ detection) between the vanilla, baseline and extended LRG models on the 25 AbacusSummit boxes; no 3σ detection in the other cases, for which a conservative estimate is adopted [src: abstract] (arXiv:2404.03008).
- DESI DR1 full shape: parameter shifts across HOD models are often above 20% of the statistical uncertainty; a systematic covariance C_HOD and a prior-related diagonal term are added to the statistical covariance [src] (arXiv:2411.12023).
- Fast mocks inherit the galaxy–halo model of their calibration set: the DESI EZmocks are tuned to AbacusSummit HOD mocks [src] (arXiv:2411.12027).

**Mitigation.** Extended HODs with assembly-bias, velocity-bias and satellite-profile parameters; tests on a second galaxy model of a different kind (SHAM, a semi-analytic model or a hydrodynamical simulation); a systematic covariance term.

**Validation test a referee expects.** Recovery of the input cosmology on mocks built with a galaxy model different from the one in the fit, at the scales of the fit; the halo particle number of the least massive hosts (500 particles for 1% in arXiv:1804.05865). [src: abstract]

**What remains open.** All data analyses with density-split, wavelet and similar statistics use AbacusSummit with an HOD (`cosmo-beyond-two-point`); a 2026 paper titled "Bounding the Effect of HOD Assumptions on Small-Scale Clustering Constraints" was found by the date-sorted search and not read.

## 5. Covariance from approximate mocks
<!-- key: covariance-from-approximate-mocks -->

**Mechanism.** A sample covariance needs N_mocks much larger than the data-vector length, which forces approximate dynamics. The approximation changes the non-Gaussian part of the covariance (the trispectrum and super-sample terms), the shot noise through the bias or halo-assignment model, and the survey realism (fibre assignment, systematics weights).

**Size.**
- Against 300 N-body simulations, seven approximate methods reproduce the variance of the power-spectrum multipoles typically within 10%, and give parameter errors within 10% of the N-body covariance [src: Sect. 1] (Blot et al. 2018, arXiv:1806.09497). Methods whose clustering amplitude is calibrated only on two-point statistics are the exceptions for the bispectrum covariance (next items).
- What that comparison is, read in the body [src: Sects. 2.1, 5.2 and 6 of arXiv:1806.09497]: halo power-spectrum multipoles at z = 1 in periodic boxes; reference of 300 Minerva runs (GADGET-3, 1000³ particles in 1500 Mpc/h, 2.67 × 10¹¹ M_⊙/h, 2LPT at z = 63, SUBFIND haloes); 300 realisations per approximate method on the same initial conditions; two halo samples, of bias about 2.6 at 2 × 10⁻⁴ h³/Mpc³ and about 3.4 at 5.5 × 10⁻⁵ h³/Mpc³, defined in each method by abundance matching; parameters {α_∥, α_⊥, fσ_8, b_1, b_2, γ_3⁻}.
  - Variance of the multipoles: within 10% for all methods in both samples except the monopole of Halogen (20–30%) and of the lognormal mocks, whose excess grows with bin width, the sign of too large a non-Gaussian term; ICE-COLA and PeakPatch average about 3% in the sparser sample; quadrupole 5–10%, hexadecapole within 5% except Pinocchio and Patchy at 9% [src: Sect. 5.2 and Fig. 4].
  - Parameters: the covariance source does not bias the cosmological parameters, recovered within 1% of the input, with biases of a few percent on poorly constrained nuisance parameters. Errors on cosmological parameters agree with the N-body ones at the 5% level or better for all methods except Halogen (one AP parameter) and Pinocchio (sparser sample); 10% is reached by all methods on all parameters except the lognormal mocks. The volume of the 1σ ellipsoid in {α_∥, α_⊥, fσ_8} is within 10% except for ICE-COLA and lognormal in the denser sample and Pinocchio in the sparser [src: Sect. 6].
  - Resolution of the test itself: with 300 mocks and matched initial conditions the error on an error ratio is about 4–5%, so differences below that are not measured [src: Sect. 6].
  - The Gaussian covariance with a non-linear power spectrum does as well as the mocks in this set-up, which the authors attribute to periodic boxes where the two-point term dominates; a survey window, where it would not, is not tested. The performance is slightly worse for the more massive sample [src: Sect. 6].
- The same comparison in configuration space: all seven methods recover the mean parameter values obtained with the N-body covariance; parameter uncertainties agree within 5% for the lower mass threshold and 10% for the higher; they can differ by up to 20% depending on whether the approximate halo sample is matched to the N-body one in mass, in number density or in clustering amplitude; no method clearly outperforms the others [src] (Lippich et al. 2018, arXiv:1806.09477).
- Bispectrum: with 300 realisations per method and matched initial conditions, most methods give errors on linear and non-linear bias within 10% of the N-body ones; the exceptions are the methods whose clustering amplitude is calibrated on two-point statistics only [src: Sect. 1] (Colavincenzo et al. 2018, arXiv:1806.09499).
- Two-point statistics of the mocks themselves, as stated by the method papers against N-body references: EZmocks 1% on P(k) to k = 0.55 h/Mpc and 20% on the bispectrum (arXiv:1409.1124); PATCHY 2% to k about 1 h/Mpc at z = 0.577 (arXiv:1307.3285); HALOGEN 2% on ξ at 10–50 Mpc/h and 15% near 100 Mpc/h (arXiv:1412.5228); L-PICOLA 2% on the matter P(k) and 5% on the reduced bispectrum at z = 0 (arXiv:1506.03737); PINOCCHIO 10% on the mass function (arXiv:astro-ph/0109323) [src]. In the nIFTy comparison only the semi-N-body method reached 1% on the quadrupole at r < 25 Mpc/h or k > 0.15 h/Mpc (arXiv:1412.7729) [src]. These are monopole-dominated statements: the quadrupole is where the effective-bias methods are weakest.
- DESI DR1: the analytic configuration-space covariance performs satisfactorily for BAO, but the analytic Fourier-space covariance does not reproduce the expected full-shape measurements, hence a corrected mock covariance for the full shape [src] (Forero-Sánchez et al. 2024, arXiv:2411.12027).
- DESI DR1, sizes read in the body [src: Sects. 4 and 5 of arXiv:2411.12027]: on the data, configuration-space BAO fits with the EZmock covariance return uncertainties about 10% smaller, and poor goodness of fit, compared with the RascalC covariance tuned on the data, although mock-tuned RascalC and mock sample covariances agree with each other; the authors conclude that the mocks differ from the data in ways that matter for the covariance (three- and four-point clustering, the fast fibre-assignment emulation). The full-shape analysis therefore uses the EZmock covariance multiplied by a sample-specific factor, the inverse of the mean reduced χ² between the two covariances [src: Eq. 22], of 10 to 40% depending on the sample. In Fourier space the analytic and mock covariances differ by about 10% element by element, with biases on parameter errors and χ² of up to 12% in ShapeFit and direct fits, against about 7% on errors and under 3% on goodness of fit for full-shape fits in configuration space.
- The shot noise of approximate fibre assignment differs from the real algorithm; the DESI EZmocks use a fast fibre-assignment emulator [src] (arXiv:2411.12027).
- Box replication misestimates cosmic variance; the DESI EZmocks use (6 Gpc/h)³ boxes to avoid it [src] (arXiv:2411.12027), whereas the Flagship 2 full-sky light-cone replicates a 3600 Mpc/h box [src] (arXiv:2405.13495).
- A fixed-amplitude ("fixed and paired") suite has suppressed variance by construction and cannot provide a covariance (arXiv:1603.05253, arXiv:1811.02111).

**Mitigation.** Validate the mock covariance against an analytic one and against a small N-body set; rescale; add systematic covariance terms.

**Validation test a referee expects.** The calibration reference of the mocks, the number of mocks against the length of the data vector, the correction factors applied (see `cosmo-statistics-inference`), and a comparison with an independent covariance estimate.

## 6. Lyα-specific simulation limits
<!-- key: lyalpha-specific-simulation-limits -->

**Resolution and box size pull in opposite directions.** A cell of 20 kpc/h and a box above 40 Mpc/h are the minimum for 1% flux statistics [src] (arXiv:1406.6361); BAO and P3D on large scales need boxes far larger than hydrodynamics can afford at that resolution. The standard escapes are splicing, accurate to about 10% on P1D [src] (arXiv:1406.6361), and emulating a small set of bias and shape parameters that are then attached to linear theory (ForestFlow, arXiv:2409.05682).

**SPH sampling of voids.** The forest at z about 5 comes from low-density gas that SPH samples poorly; the kernel-based density biases flux statistics, and agreement with a grid code at the 1% level required a tessellation-based density [src] (arXiv:2207.05023). A referee should ask how the density was reconstructed in any SPH-based forest prediction at z > 4.

**Thermal and ionisation history.** The choice of UV background changes the mean flux by 10–15% at z = 2 and by a factor 2 at z = 4 [src] (arXiv:1406.6361). Rescaling the optical depth hides this but ties the recovered amplitude to the assumed mean flux: with the same eBOSS data the Lyssa emulator gives A_Lyα < 7.6 without a mean-transmission prior and 9.8 ± 1.1 with one [src] (arXiv:2412.05372).

**Patchy reionisation relics.** Temperature fluctuations seeded by inhomogeneous reionisation persist and add large-scale P1D power at z > 4 [src] (arXiv:2207.13098); patchy helium reionisation does the same at lower redshift [src] (arXiv:2306.05471). A suite with homogeneous reionisation cannot absorb this except through other parameters.

**Galaxy formation.** AGN feedback is not negligible for P1D: 2% on σ_8 and 1% on n_s if ignored [src] (arXiv:2002.02822). Only suites with a galaxy-formation model contain a realistic DLA population (PRIYA, arXiv:2306.05471); the others mask or model DLAs separately.

**Continuum placement.** Comparing a simulation with data needs a correction for continuum-placement bias, uncertain above z = 4 [src] (arXiv:1605.03462).

**Synthetic spectra are not hydrodynamical.** BAO mocks built from Gaussian or lognormal skewers reproduce the BAO signal and the linear biases (arXiv:1912.02763); they are not valid tests of small-scale or broadband physics. The sibling skill records that fσ8 from the forest fails mock validation.

## 7. Constrained-simulation limits
<!-- key: constrained-simulation-limits -->

**Constraint scale.** Information from the data reaches down to a scale set by tracer density, noise and the forward model: about 6 Mpc/h for 2LPT BORG on SDSS-like data [src] (arXiv:1203.3639), about 4 Mpc/h for Manticore-Deep [src] (arXiv:2606.10020), a few tens of megaparsecs for velocity-constrained realisations [src] (arXiv:1510.04900). Everything below it in a resimulation is a random draw. A claim about an individual galaxy-scale object in a constrained run is a claim about the prior.

**Dynamics inside the sampler.** Few-step solvers are accurate for the large-scale field and not for halo interiors: 20 COLA steps do not give converged virial masses [src] (arXiv:2304.09193). The remedy is posterior resimulation; a paper that reads masses directly from the inference-resolution field should be questioned.

**Data model.** Galaxy bias, selection and noise are inferred jointly; the result depends on the bias model; the Manticore-Local abstract lists "a refined galaxy bias model" and "physics-informed priors" among its ingredients (arXiv:2505.10682). The Hamlet-PM paper states that its systematic biases "still need to be addressed" (arXiv:2602.03699). Velocity-based methods depend instead on distance errors and their lognormal bias.

**Dependence on the tracer.** Reconstructions from galaxy positions (2M++) and from peculiar velocities (Cosmicflows) use different data with different systematics; agreement between them is a test, and the validation framework of arXiv:2502.00121 finds that the non-linear BORG reconstruction outperforms linear-theory ones against direct distance tracers.

**Point estimate versus ensemble.** A single constrained simulation is one sample. Statements about named objects need their frequency across the posterior ensemble (Manticore-Local quotes 2–4σ detections of its cluster counterparts across the ensemble, arXiv:2505.10682).

**Assumed cosmology.** The prior and the forward model fix the cosmological parameters; consistency tests of the posterior with ΛCDM (power spectrum, halo mass function) check the inference, they do not test ΛCDM independently.

**Validation a referee expects.** Posterior-predictive tests; a comparison with data excluded from the inference (velocities, tSZ, kSZ, CMB lensing); the number of posterior samples; the resolution of the inference and of the resimulation stated separately.


## 8. Emulator and surrogate limits
<!-- key: emulator-and-surrogate-limits -->

**Mechanism.** An emulator returns a smooth interpolation with no warning when it is asked for a point its training set does not support, or for physics its simulations do not contain.

**Size.**
- Interpolation error: 1% (EuclidEmulator2), 2–3% (Mira-Titan IV, BACCO), 2.5% RMS and up to 16% (HMcode-2020) [src] (arXiv:2010.11288, arXiv:2207.12345, arXiv:2004.06245, arXiv:2009.01858). These are not interchangeable at Stage-IV precision.
- What "1%" rests on for EuclidEmulator2: training runs with 3000³ particles at 3 particles per Mpc/h per dimension (smallest resolved mass about 3.3 × 10⁹ M_⊙/h, Nyquist wavenumber about 9.4 h/Mpc), paired-and-fixed, started with first-order LPT at z = 99 [src: Sects. 3.3 and 4.5 of arXiv:2010.11288]; a cosmology-independent correction factor then rescales the result to the resolution of 8 particles per Mpc/h (about 1.7 × 10⁸ M_⊙/h), and without it the emulator is 2% low on non-linear scales against Flagship 2 [src: Sect. 5.3 and Fig. 11]. The validation set is three cosmologies, all inside the ellipsoid inscribed in the parameter box: the error is well below 1% for k ≤ 10 h/Mpc and z ≤ 3 there, the authors expect it to exceed 1% outside that ellipsoid, and expect the total error at k ≳ 5 h/Mpc to be dominated by the simulations, not the emulation [src: Sect. 8.2.1].
- Emulator against emulator: EuclidEmulator2 and BACCO agree at the percent level at the Euclid reference cosmology for z ≤ 1.5, BACCO being lower on small scales because its runs have the lower resolution without correction, and mostly within 3% over 47 cosmologies at z = 0; against the Mira-Titan II emulator the standard deviation over 84 cosmologies is about 5% at z = 0, with a few much poorer cases [src: Sects. 8.2.5 and 8.2.6 of arXiv:2010.11288]. The spread between emulators is the practical measure of the theory error, and it is larger than any single quoted accuracy.
- Mira-Titan IV: 111 models over 0.12 ≤ ω_m ≤ 0.155, 0.0215 ≤ ω_b ≤ 0.0235, 0.7 ≤ σ_8 ≤ 0.9, 0.55 ≤ h ≤ 0.85, 0.85 ≤ n_s ≤ 1.05, −1.3 ≤ w_0 ≤ −0.7, −1.73 ≤ w_a ≤ 1.28 with w_0 + w_a ≤ −0.0081, 0 ≤ ω_ν ≤ 0.01, and 0 ≤ z ≤ 2.02 [src: Sect. 2.1 and Eq. 1 of arXiv:2207.12345]. Tested on six simulations outside the design: better than 2% for five, at or below 1% for the ΛCDM one, 2.48% at high k for the model at the edge of the (w_0, w_a) region; leave-one-out errors around or below 2%; the 36-model predecessor is at 3–6% on the same tests [src: Sect. 4.1 and Figs. 7–9]. Only the ΛCDM test model falls inside the narrower box of EuclidEmulator2, which is within about 3% of that simulation in the worst case [src: Sect. 4.2.2]. An emulator error therefore depends on where in its box it is asked, and is largest at the edges.
- History of the quoted accuracies: HALOFIT revised, 5% for k ≤ 1 h/Mpc and 10% for 1 ≤ k ≤ 10 h/Mpc (arXiv:1208.2701); Coyote, 1% to k about 1 h/Mpc for wCDM (arXiv:0912.4490); Mira-Titan II, about 4% over eight parameters (arXiv:1705.03388) [src].
- Simulation error underneath: 1% between codes only with tuned settings (§1 of `results.md`).
- Missing physics: every gravity-only emulator needs a baryonic response on top, whose own emulators are accurate to 1–2.5% with respect to simulations that disagree with each other by more than that (arXiv:2011.15018, arXiv:2507.07892, arXiv:2410.17109).
- Cosmology dependence of the baryonic response: about 1% for k < 10 h/Mpc in FLAMINGO, over a limited set of cosmologies; the authors ask for a wider range before the result is taken as general [src] (arXiv:2410.17109).
- Residual resolution effects: EuclidEmulator2 corrects for them after emulation [src] (arXiv:2010.11288); an emulator without such a correction inherits the resolution bias of its training runs.

**Mitigation.** Compare two emulators built on different codes; keep the posterior away from the design boundary or report when it is not; propagate the quoted error into the likelihood (`cosmo-statistics-inference`).

**Referee check.** The emulator version, its parameter box, and the position of the best fit inside it.

## 9. Light-cone and survey-realism limits
<!-- key: light-cone-and-survey-realism-limits -->

- Pseudo-light-cones made of a few snapshots carry no redshift evolution inside a bin; the DESI DR1 EZmocks are built this way [src] (arXiv:2411.12027).
- Box replication repeats structure along the line of sight and across the sky; Flagship 2 replicates a 3600 Mpc/h box to reach z = 3 over the full sky, while its galaxy catalogue covers one octant [src: Sect. 2.1] (arXiv:2405.13495).
- A mock is as realistic as the observational effects applied to it. The eBOSS EZmocks include photometric and spectroscopic systematics [src] (arXiv:2007.08997); the DESI DR1 EZmocks include an emulated fibre assignment [src] (arXiv:2411.12027); effects not applied cannot be validated on the mocks.
- Mocks calibrated on the data they are used to validate (eBOSS EZmocks, arXiv:2007.08997) reproduce the clustering by construction; agreement between data and mocks is then not a test.
- Synthetic Lyα spectra reproduce DESI statistics within 10%, not at the precision of the measurement [src] (arXiv:2607.27412).

## 10. Neutrino and modified-gravity simulation limits
<!-- key: neutrino-and-modified-gravity-simulation-limits -->

- Neutrino implementations agree at the sub-percent level on common initial data [src] (arXiv:2211.12457); the eleven N-body implementations compared are "not all independent".
- Modified-gravity codes agree to 1% on the ratio to ΛCDM up to k about 5–10 h/Mpc for three models [src] (arXiv:1506.06384); the absolute spectrum carries the usual gravity-only error, and baryons are not included.
- The quasi-static approximation was tested for the symmetron model only [src] (arXiv:1506.06384).
- Emulators cover neutrino mass up to the largest value simulated (0.5 eV in Aemulus ν, arXiv:2303.09762).

## What a referee checks
<!-- key: what-a-referee-checks -->

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
<!-- key: not-verified -->

- Quantitative size of box-replication and super-sample effects on lensing statistics (arXiv:2511.20423, snippet only). The only replication figure read is the bias of less than 10% near the correlation length in MoMaF light-cones (arXiv:astro-ph/0309305, abstract).
- Effect of the halo finder on a galaxy mock or on a fitted cosmology: the finder comparison (arXiv:1104.0949) and the mass-function papers were read in abstract; no paper read here propagates the choice of finder to HOD or cosmological parameters.
- Body of Crocce et al. 2006 (arXiv:astro-ph/0606505) and of the COLA, ICE-COLA and FastPM papers: abstracts only; the step-number dependence of their accuracy is not tabulated here.
- Emulator errors of BACCO, Aemulus ν and Dark Emulator: as stated in their abstracts; only EuclidEmulator2 and Mira-Titan IV were read in the body.
- The size of the transient from first-order initial conditions in the Flagship 2 and EuclidEmulator2 runs themselves: no measurement was found.
- Accuracy of ray-tracing and of the Born approximation in lensing light-cones: no source was read.
- Emulator error propagation into a likelihood: treated in `cosmo-statistics-inference`, not re-read here.
- Sensitivity of Local Group analogues to unconstrained small-scale modes: abstract read during the first build, outside the source list.
- Fuzzy and self-interacting dark-matter solvers: not researched.
