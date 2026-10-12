# Galaxy-cluster cosmology — systematics

Scope: the systematic effects that limit cluster cosmology, their measured size, mitigation and the reference a referee expects.
Snapshot: 2026-10-07

Cluster counts are limited by systematics, not by statistics, in every current sample. The three families are the absolute mass scale (sections 1–4), the selection (sections 5–8) and the theory and inference machinery (sections 9–11). Each subsection gives the mechanism, the size where a paper quantifies it, the usual mitigation, the validation test and the reference.

## 1. Weak-lensing mass: modelling bias and scatter

- Mechanism. A spherical profile fitted to the tangential shear of a triaxial halo embedded in large-scale structure does not return the spherical-overdensity mass.
- Size. Bias of 5–10% and intrinsic scatter of about 20% for massive clusters, up to about 30% for groups, in NFW fits to about 1e4 simulated haloes [src] (Becker & Kravtsov 2011, arXiv:1011.1681). On N-body haloes in Euclid conditions the weak-lensing mass is low by −14.6 ± 1.7 % on average for M200c > 5e13 M_sun at z < 1 in the ideal case, and by −15.5 ± 2.4 % in a realistic setting with robust source selection [src] (Euclid Collaboration 2024, arXiv:2409.02783).
- Mitigation. A simulation-calibrated relation between weak-lensing mass and halo mass, with its bias and scatter as nuisance parameters; a restricted radial range that avoids the core and the two-halo regime.
- Validation. The same estimator run on mock shear from hydrodynamical simulations; agreement between independent lensing surveys for the same clusters.
- Size in a current budget. For SPT clusters with DES Y3 lensing the systematic uncertainty of the mass calibration rises from 1% at z = 0.25 to 10% at z = 0.95, plus 2% in quadrature for baryonic effects on the lensing-mass model [src] (Bocquet et al. 2024, arXiv:2310.12213). For eRASS1 × DES Y3 the hydrodynamical modelling uncertainty dominates at z < 0.6 and the source photo-z calibration at higher lens redshift [src] (arXiv:2402.08455).

## 2. Weak-lensing mass: source redshifts, shear calibration, member contamination, blending

- Mechanism. The lensing efficiency Σ_crit depends on the source redshift distribution; cluster members scattered into the source sample dilute the shear; the dense cluster field increases blending.
- Size. Source photometric redshifts are the largest systematic of the CCCP lensing masses [src] (Hoekstra et al. 2015, arXiv:1502.01883). In the DES Y1 stacked calibration the systematic term (0.133) exceeds the statistical one (0.075) on M0 = 3.081 in units of 1e14 M_sun, for a 5.0% total [src] (McClintock et al. 2019, arXiv:1805.00039); the listed contributions are shear and photo-z errors, miscentring, member dilution, the halo–mass correlation model, triaxiality and projection effects.
- Blending at Rubin depth. In DC2 simulations a cut on a "blending entropy" S_b < 0.2 removes about 25% of objects, mostly near the magnitude limit, and substantially reduces the blending-induced bias in cluster lensing profiles and masses, and through them in σ8 [src] (Ramel et al. 2026, arXiv:2609.12158).
- Mitigation. Boost-factor or P(z)-decomposition corrections for member dilution; conservative source selection behind the cluster; the survey's own shear and redshift calibration (see `cosmo-weak-lensing`).
- Validation. Consistency of the masses of the same clusters across DES, KiDS and HSC, as done for eRASS1 (arXiv:2402.08455, arXiv:2504.01076).

## 3. Miscentring

- Mechanism. The optical or SZ centre is offset from the halo centre. The shear profile is suppressed at small radii and, for optical finders, the richness is underestimated.
- Size. About 75 ± 8 % of DES Y1 redMaPPer clusters are well centred relative to X-ray peaks; the offsets of the rest follow a Gamma distribution in normalised projected distance; miscentring causes a systematic underestimate of richness [src] (Zhang et al. 2019, arXiv:1901.07119).
- Mitigation. A two-component profile model (centred plus miscentred fraction with an offset distribution), with priors from X-ray or SZ centres; exclusion of the innermost radii.
- Validation. Comparison of optical centres with X-ray or SZ centres on the overlap sample.

## 4. Hydrostatic bias and X-ray temperature calibration

- Mechanism. Hydrostatic masses miss non-thermal pressure (bulk motion, turbulence) and depend on the temperature estimate. Scaling relations calibrated on them carry the bias into the counts.
- Size from simulations. Median hydrostatic bias of about −0.1 at group scale to −0.2 at cluster scale in FLAMINGO, with scatter of about 0.1 at M500c ~ 1e14 M_sun [src] (Braspenning et al. 2025, arXiv:2409.07849). For M500c > 7.5e14 M_sun at z = 0 the bias is 0.22 ± 0.01 with X-ray spectroscopic-like temperatures and −0.05 ± 0.01 with SZ y-weighted temperatures [src] (Kay et al. 2024, arXiv:2404.08539): much of the "hydrostatic" bias is a temperature-weighting effect.
- Size from data. Non-thermal pressure of about 6% at R500 and 10% at R200 in X-COP; the universal gas fraction with the Planck mass calibration implies 1 − b = 0.85 ± 0.05 [src] (Eckert et al. 2019, arXiv:1805.00034).
- Instrument calibration. The same lensing data give 1 − b = 0.89 ± 0.04 against a Chandra-calibrated Y_SZ–M relation and 0.76 ± 0.04 against the XMM one [src] (arXiv:2402.04006). The cosmology from the counts is identical; only the label "bias" moves.
- Mass and redshift dependence. Weighing the Giants found evidence at 95% confidence for a mass dependence of M_Planck/M_WtG [src] (arXiv:1402.2670); a Planck + SPT fit finds the bias increasing towards high redshift and low mass (arXiv:2112.03606); ACT × DES Y3 finds (1 − b) decreasing with redshift with power-law index −1.8 +0.5/−0.6 [src] (arXiv:2512.18935); gas-fraction data give 3.8σ evidence for redshift dependence that is "entirely dependent on the cluster sample" [src] (Wicker et al. 2023, arXiv:2204.12823).
- Mitigation. Calibrate the mass scale with lensing and treat X-ray quantities as low-scatter proxies only; free mass and redshift trends of the relation.
- Validation. Relaxed clusters at r2500, where lensing and hydrostatic masses agree: 0.96 ± 9% (stat) ± 9% (sys) [src] (Applegate et al. 2016, arXiv:1509.02162).

## 5. X-ray selection

- Mechanism. Detection depends on surface brightness, hence on core state, morphology, exposure, background and point-source contamination, not on mass alone.
- Evidence. PSZ2 revealed "a population of low-redshift X-ray under-luminous clusters" almost absent from ROSAT-selected samples [src] (arXiv:1502.01598). X-ray and SZ selections do not pick the same population.
- Mitigation. Selection functions from end-to-end simulated skies, as for eRASS1 (Clerc et al. 2024, arXiv:2402.08457); optical confirmation to control purity (eRASS1 cosmology sample at about 95% purity [src], arXiv:2402.08452); a mixture model for residual contaminants.
- Validation. Cross-matching with SZ and optical catalogues: 1279 SPT-3G clusters match eRASS1 [src] (arXiv:2607.01175); 321 AMICO KiDS-1000 clusters match the eRASS1 primary sample [src] (arXiv:2507.14338).

## 6. SZ selection: astrophysical contamination

- Dust. At z > 1 the tSZ signal is reduced by 17.4 +3.1/−2.9 % at 150 GHz and 3.7 ± 0.7 % at 95 GHz; the SPT-Deep catalogue from dust-nulled maps is consistent with the nominal one, which the authors attribute to the 220 GHz band [src] (arXiv:2503.17271). In SPT-3G five-year data the 220 GHz increment is about 17 times larger at z ~ 1.5 than at z ~ 0.25, with only weak evidence for correlated synchrotron emission [src] (arXiv:2607.01175).
- Radio sources. Median reduction of ξ by 0.032, about 0.8% of the ξ = 4 threshold; about 7% of candidates have a predicted Δξ > 1 [src] (arXiv:2311.07512).
- Relativistic corrections and CIB in Planck. Relativistic corrections change the tSZ amplitude by 5–10% but not the signal-to-noise; the cluster-correlated CIB has a negligible effect on the Planck tSZ observables [src] (arXiv:2408.06189).
- Purity. PSZ2 purity lower limit 83% [src] (arXiv:1502.01598); SPT-3G candidates more than 82% pure at ξ > 4 and more than 99% at ξ ≥ 5 [src] (arXiv:2607.01175).
- Mitigation. Multi-frequency matched filters with deprojection; optical confirmation; a ξ or S/N threshold at which purity is high.
- Validation. Catalogues rebuilt from dust-nulled or CIB-deprojected maps.

## 7. Orientation and triaxiality in the selection

- Mechanism. A halo elongated along the line of sight has a higher projected signal in SZ, optical richness and lensing alike, so it is more likely to be selected and its lensing mass is biased high.
- Size. For the Planck-selected CHEX-MATE sample the induced lensing-mass bias is 0–4%, largest at low mass [src] (Saxena et al. 2025, arXiv:2505.23005).
- Mitigation. Correlated scatter between the selection observable and the lensing mass in the population model.

## 8. Optical selection: projection effects and lensing selection bias

This is the systematic that produced the wrong DES Y1 result (S8 = 0.65 ± 0.04, arXiv:2002.11124).

- Mechanism. Photometric cluster finders count galaxies in a cylinder that is tens of Mpc deep. Haloes embedded in filaments or elongated along the line of sight gain richness, so a richness-selected sample is enriched in them. Their stacked lensing and clustering signals are boosted anisotropically on large scales relative to a mass-selected sample of the same mean mass.
- Size in simulations. Lensing and clustering boosted on large scales by up to factors of 1.2 and 1.4; about 30% of the sample, the clusters in filaments aligned with the line of sight, causes the boost [src] (Sunayama et al. 2020, arXiv:2002.03867). For redMaPPer in the Buzzard simulations, residuals of richness and lensing are positively correlated at fixed mass, and the selection bias of ΔΣ is 20–60% on large scales, from spurious members within ±20–60 Mpc/h along the line of sight [src] (Wu et al. 2022, arXiv:2203.05416). The Euclid framework finds an enhancement of the stacked profile that peaks near 1 Mpc/h with amplitude 20–40% depending on richness and redshift, with baryons changing it by about 2% beyond 0.3 Mpc/h [src] (Euclid Collaboration 2026, arXiv:2605.02723).
- Size in data. Projection effects contribute about 16% of the weighted richness for the lowest-richness SDSS redMaPPer clusters, with a steeper richness dependence than the models then in use [src] (Myles et al. 2021, arXiv:2011.07070). SPT-SZ confirms 207 of 1005 DES Y1 redMaPPer clusters at λ > 40; the unconfirmed population exceeds 12% at λ = 40 and extrapolates to more than 22% at λ = 20 (97.5 percentile limits) [src] (Grandis et al. 2021, arXiv:2101.04984).
- Mitigation, in order of appearance. A richness cut (λ ≥ 30 "significantly reduces the tension", arXiv:2002.11124); an external multi-wavelength mass anchor (arXiv:2010.13800); an anisotropic-boost forward model (arXiv:2112.09059, arXiv:2309.13025); a multiprobe data vector of cluster abundances, cluster cross-correlations and galaxy clustering, on large scales only in DES Y1 (arXiv:2010.01138) and extended in DES Y3 (arXiv:2503.13632); a simulation-based forward model of the cluster finder with counts-in-cylinders selection (arXiv:2510.25706).
- Validation. Cross-matching with SZ or X-ray samples (arXiv:2502.12914, which rules out significant contamination by unvirialised objects at high richness in DES Y3 but finds redshift trends that projection-effect simulations do not capture); spectroscopic membership (arXiv:2011.07070).
- The warning in the record. The anisotropic-boost model applied to SDSS with SDSS lensing gave S8 = 0.718 +0.024/−0.021, which its authors call "clearly inconsistent" with other probes (arXiv:2112.09059); the same model with HSC Y3 lensing gave 0.816 +0.041/−0.039 (arXiv:2309.13025). A model of the projection effect is not a guarantee.

## 9. Halo mass function and bias

- Non-universality. The amplitude of the "universal" f(σ) falls by 20–50% from z = 0 to 2.5 depending on the mass definition [src] (Tinker et al. 2008, arXiv:0803.2706). A fit that ignores this introduces false cosmological sensitivity (arXiv:1502.07357).
- Calibration accuracy. Tinker 2008 is accurate to ≲ 5% at z = 0 [src]; replacing it by the Magneticum DM-only fit shifts a Planck-like result by Δσ8 ≈ 0.02 [src] (Bocquet et al. 2016, arXiv:1502.07357), which is comparable to current statistical errors. The Euclid calibration is sub-percent over the models tested, and names the halo finder as the remaining effect that can bias inference [src] (arXiv:2208.02174).
- Baryons. Negligible for SPT-like and Planck-like samples; for an eROSITA-like sample neglecting them biases Ω_m low by about 0.01 [src] (arXiv:1502.07357). The effect vanishes for M200m ≳ 1e14 M_sun and at z ~ 2.
- Halo bias. The Tinker 2010 fit has about 6% scatter, and the bias of FoF haloes is about 10% below that of Δ = 200 haloes [src] (arXiv:1001.3162). A clustering-based mass calibration inherits this.
- Mitigation. Marginalise over mass-function uncertainty (arXiv:2507.14285); use fits or emulators calibrated for massive neutrinos and for the halo definition actually used.

## 10. Form of the scaling relation: scatter, evolution, mass dependence

- Mechanism. Counts constrain the product of mass function and scaling relation. A wrong functional form (constant bias, self-similar evolution, lognormal scatter) is absorbed by cosmological parameters.
- Size. With a constant bias the Planck × DES analysis gives S8 = 0.791 +0.023/−0.021 and Ω_m = 0.312; with a mass-dependent bias 0.814 +0.019/−0.020 and 0.353 +0.025/−0.031 [src] (arXiv:2509.02068). With self-similar evolution the Chandra–Planck analysis gives S8 = 0.78 ± 0.02, with fitted evolution 0.81 ± 0.02 [src] (arXiv:2402.04006). A redshift-evolution parameter β = 0.86 ± 0.07 can replace w = −0.82 ± 0.07 in the Planck + ACT counts [src] (arXiv:2403.19542): evolution of the relation and dark energy are degenerate.
- Scatter. The richness–mass scatter is not lognormal in DES Y3 × SPT (arXiv:2502.12914); the intrinsic scatter of log λ*–log M200 in KiDS AMICO is 0.05 ± 0.02 [src] (arXiv:2507.14285).
- Mitigation. Free slopes in mass and redshift, correlated scatter, and a mass calibration that spans the redshift range of the counts.

## 11. Likelihood, covariance, photometric redshifts

- Sample variance. Neglected by a pure Poisson likelihood, which "always underestimates the errors" for Rubin- or Euclid-like samples [src] (Payerne et al. 2023, arXiv:2210.11093); the framework is Hu & Kravtsov 2003 (arXiv:astro-ph/0203169). Super-sample covariance is in the KiDS AMICO list of marginalised effects (arXiv:2507.14285).
- Photometric redshifts of clusters. In Euclid-like mocks they broaden posteriors by 20–30%; neglecting redshift-space distortions in cluster clustering can bias the constraints [src] (Fumagalli et al. 2025, arXiv:2510.13509).
- Inference machinery. Simulation-based inference adds its own error term: 3% from neural-network stochasticity in the XXL analysis [src] (arXiv:2602.11989).
- Parameter-space effects. The best-constrained combination is not S8; quoting S8 inflates the error and moves the point estimate along the degeneracy (arXiv:2401.02075, arXiv:2406.11970).

## 12. Systematics list of a recent analysis

The KiDS-1000 AMICO analysis marginalises over: impurities of the background and cluster samples, biases in cluster redshift and richness, projection effects, halo orientation, miscentring, truncation, correlated matter, shear multiplicative bias, baryons, geometric distortion, mass-function uncertainty and super-sample covariance [src] (Lesci et al. 2025, arXiv:2507.14285). It is a usable template for what a counts-plus-lensing paper should list.

## What a referee checks in a results section

1. The mass definition, the units of mass (h, h70 or none) and the reference of any quoted (1 − b).
2. The absolute mass calibration: which lensing data, over which redshift range relative to the counts, with which systematic floor.
3. The weak-lensing-mass to halo-mass relation: the simulations it was calibrated on, and the baryon term.
4. The selection function: how it was built, the purity, and the treatment of contaminants.
5. For optical samples: the projection-effect model, the scales used, the richness threshold, and a test against an SZ or X-ray sample.
6. Miscentring model and its prior.
7. The mass function and its uncertainty; massive neutrinos; baryons for low-mass samples.
8. The functional form of the scaling relation: free mass and redshift slopes, correlated scatter.
9. The count likelihood and whether sample variance is included.
10. Blinding and post-unblinding changes.
11. The exponent of the quoted amplitude combination and the CMB data set used for a tension.
12. Goodness of fit of the counts and of the lensing profiles separately.

## Not verified

- The size of the member-dilution (boost-factor) correction in any specific analysis.
- Contamination of CMB-lensing cluster mass estimators by the cluster's own tSZ and kSZ signal: no paper quantifying it was fetched.
- The eRASS1 treatment of contaminants (AGN, random sources) in the mixture model, and the cross-calibration of eROSITA temperatures with Chandra and XMM-Newton: the corresponding papers were not read beyond their titles.
- Cluster-finder photometric-redshift performance for HSC shear-selected clusters.
