# Galaxy-cluster cosmology — systematics

Scope: the systematic effects that limit cluster cosmology, their measured size, mitigation and the reference a referee expects.
Snapshot: 2026-10-14

Cluster counts are limited by systematics, not by statistics, in every current sample. The three families are the absolute mass scale (sections 1–4), the selection (sections 5–8) and the theory and inference machinery (sections 9–11). Each subsection gives the mechanism, the size where a paper quantifies it, the usual mitigation, the validation test and the reference.

## 1. Weak-lensing mass: modelling bias and scatter
<!-- key: weak-lensing-mass-modelling-bias-and-scatter -->

- Mechanism. A spherical profile fitted to the tangential shear of a triaxial halo embedded in large-scale structure does not return the spherical-overdensity mass.
- Size. Bias of 5–10% and intrinsic scatter of about 20% for massive clusters, up to about 30% for groups, in NFW fits to about 1e4 simulated haloes [src] (Becker & Kravtsov 2011, arXiv:1011.1681). On N-body haloes in Euclid conditions the weak-lensing mass is low by −14.6 ± 1.7 % on average for M200c > 5e13 M_sun at z < 1 in the ideal case, and by −15.5 ± 2.4 % in a realistic setting with robust source selection [src] (Euclid Collaboration 2024, arXiv:2409.02783).
- Mitigation. A simulation-calibrated relation between weak-lensing mass and halo mass, with its bias and scatter as nuisance parameters, following the shear-library method of Grandis et al. 2021 (arXiv:2103.16212) [src]; a restricted radial range that avoids the core and the two-halo regime. In the HSC shear-selected analysis the calibrated scatter is σ_WL = 0.238 ± 0.037, and fitting down to 0.2 instead of 0.5 Mpc/h raises it by about 50% [src: Sect. 4.5.1, arXiv:2406.11970].
- Validation. The same estimator run on mock shear from hydrodynamical simulations; agreement between independent lensing surveys for the same clusters.
- Size in a current budget. For SPT clusters with DES Y3 lensing the systematic uncertainty of the mass calibration rises from 1% at z = 0.25 to 10% at z = 0.95, plus 2% in quadrature for baryonic effects on the lensing-mass model [src] (Bocquet et al. 2024, arXiv:2310.12213). For eRASS1 × DES Y3 the hydrodynamical modelling uncertainty dominates at z < 0.6 and the source photo-z calibration at higher lens redshift [src] (arXiv:2402.08455).

## 2. Weak-lensing mass: source redshifts, shear calibration, member contamination, blending
<!-- key: weak-lensing-mass-source-redshifts-shear -->

- Mechanism. The lensing efficiency Σ_crit depends on the source redshift distribution; cluster members scattered into the source sample dilute the shear; the dense cluster field increases blending.
- Size. Source photometric redshifts are the largest systematic of the CCCP lensing masses [src] (Hoekstra et al. 2015, arXiv:1502.01883). In the DES Y1 stacked calibration the systematic term (0.133) exceeds the statistical one (0.075) on M0 = 3.081 in units of 1e14 M_sun, for a 5.0% total [src] (McClintock et al. 2019, arXiv:1805.00039); the listed contributions are shear and photo-z errors, miscentring, member dilution, the halo–mass correlation model, triaxiality and projection effects.
- Blending at Rubin depth. In DC2 simulations a cut on a "blending entropy" S_b < 0.2 removes about 25% of objects, mostly near the magnitude limit, and substantially reduces the blending-induced bias in cluster lensing profiles and masses, and through them in σ8 [src] (Ramel et al. 2026, arXiv:2609.12158).
- Mitigation. Boost-factor or P(z)-decomposition corrections for member dilution; conservative source selection behind the cluster; the survey's own shear and redshift calibration (see `cosmo-weak-lensing`).
- Validation. Consistency of the masses of the same clusters across DES, KiDS and HSC, as done for eRASS1 (arXiv:2402.08455, arXiv:2504.01076).

## 3. Miscentring
<!-- key: miscentring -->

- Mechanism. The optical or SZ centre is offset from the halo centre. The shear profile is suppressed at small radii and, for optical finders, the richness is underestimated.
- Size. About 75 ± 8 % of DES Y1 redMaPPer clusters are well centred relative to X-ray peaks; the offsets of the rest follow a Gamma distribution in normalised projected distance; miscentring causes a systematic underestimate of richness [src] (Zhang et al. 2019, arXiv:1901.07119).
- Mitigation. A two-component profile model (centred plus miscentred fraction with an offset distribution), with priors from X-ray or SZ centres; exclusion of the innermost radii.
- Validation. Comparison of optical centres with X-ray or SZ centres on the overlap sample.

## 4. Hydrostatic bias and X-ray temperature calibration
<!-- key: hydrostatic-bias-and-x-ray-temperature -->

- Mechanism. Hydrostatic masses miss non-thermal pressure (bulk motion, turbulence) and depend on the temperature estimate. Scaling relations calibrated on them carry the bias into the counts.
- First simulation estimate. Mock Chandra analyses of simulated clusters: hydrostatic mass biased low by about 5–20% through the virial region, gas mass accurate to < 6% [src] (Nagai, Vikhlinin & Kravtsov 2007, arXiv:astro-ph/0609247).
- Size from simulations. Median hydrostatic bias of about −0.1 at group scale to −0.2 at cluster scale in FLAMINGO, with scatter of about 0.1 at M500c ~ 1e14 M_sun [src] (Braspenning et al. 2025, arXiv:2409.07849). For M500c > 7.5e14 M_sun at z = 0 the bias is 0.22 ± 0.01 with X-ray spectroscopic-like temperatures and −0.05 ± 0.01 with SZ y-weighted temperatures [src] (Kay et al. 2024, arXiv:2404.08539): much of the "hydrostatic" bias is a temperature-weighting effect.
- Size from data. Non-thermal pressure of about 6% at R500 and 10% at R200 in X-COP; the universal gas fraction with the Planck mass calibration implies 1 − b = 0.85 ± 0.05 [src] (Eckert et al. 2019, arXiv:1805.00034).
- Instrument calibration. The same lensing data give 1 − b = 0.89 ± 0.04 against a Chandra-calibrated Y_SZ–M relation and 0.76 ± 0.04 against the XMM one [src] (arXiv:2402.04006). The cosmology from the counts is identical; only the label "bias" moves.
- Mass and redshift dependence. Weighing the Giants found evidence at 95% confidence for a mass dependence of M_Planck/M_WtG [src] (arXiv:1402.2670); a Planck + SPT fit finds the bias increasing towards high redshift and low mass (arXiv:2112.03606); ACT × DES Y3 finds (1 − b) decreasing with redshift with power-law index −1.8 +0.5/−0.6 [src] (arXiv:2512.18935); gas-fraction data give 3.8σ evidence for redshift dependence that is "entirely dependent on the cluster sample" [src] (Wicker et al. 2023, arXiv:2204.12823).
- Mitigation. Calibrate the mass scale with lensing and treat X-ray quantities as low-scatter proxies only; free mass and redshift trends of the relation.
- Validation. Relaxed clusters at r2500, where lensing and hydrostatic masses agree: 0.96 ± 9% (stat) ± 9% (sys) [src] (Applegate et al. 2016, arXiv:1509.02162).

## 5. X-ray selection
<!-- key: x-ray-selection -->

- Mechanism. Detection depends on surface brightness, hence on core state, morphology, exposure, background and point-source contamination, not on mass alone.
- Evidence. PSZ2 revealed "a population of low-redshift X-ray under-luminous clusters" almost absent from ROSAT-selected samples [src] (arXiv:1502.01598). X-ray and SZ selections do not pick the same population.
- Mitigation. Selection functions from end-to-end simulated skies, as for eRASS1 (Clerc et al. 2024, arXiv:2402.08457); optical confirmation to control purity (eRASS1 cosmology sample at about 95% purity [src], arXiv:2402.08452); a mixture model for residual contaminants.
- Validation. Cross-matching with SZ and optical catalogues: 1279 SPT-3G clusters match eRASS1 [src] (arXiv:2607.01175); 321 AMICO KiDS-1000 clusters match the eRASS1 primary sample [src] (arXiv:2507.14338).

## 6. SZ selection: astrophysical contamination
<!-- key: sz-selection-astrophysical-contamination -->

- Dust. At z > 1 the tSZ signal is reduced by 17.4 +3.1/−2.9 % at 150 GHz and 3.7 ± 0.7 % at 95 GHz; the SPT-Deep catalogue from dust-nulled maps is consistent with the nominal one, which the authors attribute to the 220 GHz band [src] (arXiv:2503.17271). In SPT-3G five-year data the 220 GHz increment is about 17 times larger at z ~ 1.5 than at z ~ 0.25, with only weak evidence for correlated synchrotron emission [src] (arXiv:2607.01175).
- Radio sources. Median reduction of ξ by 0.032, about 0.8% of the ξ = 4 threshold; about 7% of candidates have a predicted Δξ > 1 [src] (arXiv:2311.07512).
- Relativistic corrections and CIB in Planck. Relativistic corrections change the tSZ amplitude by 5–10% but not the signal-to-noise; the cluster-correlated CIB has a negligible effect on the Planck tSZ observables [src] (arXiv:2408.06189).
- Purity. PSZ2 purity lower limit 83% [src] (arXiv:1502.01598); SPT-3G candidates more than 82% pure at ξ > 4 and more than 99% at ξ ≥ 5 [src] (arXiv:2607.01175).
- Mitigation. Multi-frequency matched filters with deprojection; optical confirmation; a ξ or S/N threshold at which purity is high.
- Validation. Catalogues rebuilt from dust-nulled or CIB-deprojected maps.

## 7. Orientation and triaxiality in the selection
<!-- key: orientation-and-triaxiality-in-the-selection -->

- Mechanism. A halo elongated along the line of sight has a higher projected signal in SZ, optical richness and lensing alike, so it is more likely to be selected and its lensing mass is biased high.
- Size. For the Planck-selected CHEX-MATE sample the induced lensing-mass bias is 0–4%, largest at low mass [src] (Saxena et al. 2025, arXiv:2505.23005).
- Mitigation. Correlated scatter between the selection observable and the lensing mass in the population model.

## 8. Optical selection: projection effects and lensing selection bias
<!-- key: optical-selection-projection-effects-and -->

This is the systematic that produced the wrong DES Y1 result (S8 = 0.65 ± 0.04, arXiv:2002.11124).

- Mechanism. Photometric cluster finders count galaxies in a cylinder that is tens of Mpc deep. Haloes embedded in filaments or elongated along the line of sight gain richness, so a richness-selected sample is enriched in them. Their stacked lensing and clustering signals are boosted anisotropically on large scales relative to a mass-selected sample of the same mean mass.
- How the estimate grew. The redMaPPer paper put the incidence of projection effects at ≤ 5% [src] (Rykoff et al. 2014, arXiv:1303.3562). The empirical model of Costanzi et al. 2019 (arXiv:1807.07072) found that marginalising over a lognormal richness–mass relation only, without projection effects, biases S8 by 0.05, more than twice the posterior uncertainty of a DES Y1-like analysis [src]. DES Y1 then found the selection effect on stacked lensing masses to be 20–30% [src: Sect. III.3, arXiv:2002.11124].
- Size in simulations. Lensing and clustering boosted on large scales by up to factors of 1.2 and 1.4; about 30% of the sample, the clusters in filaments aligned with the line of sight, causes the boost [src] (Sunayama et al. 2020, arXiv:2002.03867). For redMaPPer in the Buzzard simulations, residuals of richness and lensing are positively correlated at fixed mass, and the selection bias of ΔΣ is 20–60% on large scales, from spurious members within ±20–60 Mpc/h along the line of sight [src] (Wu et al. 2022, arXiv:2203.05416). The Euclid framework finds an enhancement of the stacked profile that peaks near 1 Mpc/h with amplitude 20–40% depending on richness and redshift, with baryons changing it by about 2% beyond 0.3 Mpc/h [src] (Euclid Collaboration 2026, arXiv:2605.02723).
- Size in data. Projection effects contribute about 16% of the weighted richness for the lowest-richness SDSS redMaPPer clusters, with a steeper richness dependence than the models then in use [src] (Myles et al. 2021, arXiv:2011.07070). SPT-SZ confirms 207 of 1005 DES Y1 redMaPPer clusters at λ > 40; the unconfirmed population exceeds 12% at λ = 40 and extrapolates to more than 22% at λ = 20 (97.5 percentile limits) [src] (Grandis et al. 2021, arXiv:2101.04984).
- Mitigation, in order of appearance. A richness cut (λ ≥ 30 "significantly reduces the tension", arXiv:2002.11124); an external multi-wavelength mass anchor (arXiv:2010.13800); an anisotropic-boost forward model (arXiv:2112.09059, arXiv:2309.13025); a multiprobe data vector of cluster abundances, cluster cross-correlations and galaxy clustering, on large scales only in DES Y1 (arXiv:2010.01138) and extended in DES Y3 (arXiv:2503.13632); a simulation-based forward model of the cluster finder with counts-in-cylinders selection (arXiv:2510.25706).
- Validation. Cross-matching with SZ or X-ray samples (arXiv:2502.12914, which rules out significant contamination by unvirialised objects at high richness in DES Y3 but finds redshift trends that projection-effect simulations do not capture); spectroscopic membership (arXiv:2011.07070).
- The warning in the record. The anisotropic-boost model applied to SDSS with SDSS lensing gave S8 = 0.718 +0.024/−0.021, which its authors call "clearly inconsistent" with other probes (arXiv:2112.09059); the same model with HSC Y3 lensing gave 0.816 +0.041/−0.039 (arXiv:2309.13025). A model of the projection effect is not a guarantee.

## 9. Halo mass function and bias
<!-- key: halo-mass-function-and-bias -->

- Non-universality. The amplitude of the "universal" f(σ) falls by 20–50% from z = 0 to 2.5 depending on the mass definition [src] (Tinker et al. 2008, arXiv:0803.2706). A fit that ignores this introduces false cosmological sensitivity (arXiv:1502.07357).
- Calibration accuracy. Tinker 2008 is accurate to ≲ 5% at z = 0 [src]; replacing it by the Magneticum DM-only fit shifts a Planck-like result by Δσ8 ≈ 0.02 [src] (Bocquet et al. 2016, arXiv:1502.07357), which is comparable to current statistical errors. The Euclid calibration is sub-percent over the models tested, and names the halo finder as the remaining effect that can bias inference [src] (arXiv:2208.02174).
- Baryons. Negligible for SPT-like and Planck-like samples; for an eROSITA-like sample neglecting them biases Ω_m low by about 0.01 [src] (arXiv:1502.07357). The effect vanishes for M200m ≳ 1e14 M_sun and at z ~ 2.
- Halo bias. The Tinker 2010 fit has about 6% scatter, and the bias of FoF haloes is about 10% below that of Δ = 200 haloes [src] (arXiv:1001.3162). A clustering-based mass calibration inherits this.
- Mitigation. Marginalise over mass-function uncertainty (arXiv:2507.14285); use fits or emulators calibrated for massive neutrinos and for the halo definition actually used.

## 10. Form of the scaling relation: scatter, evolution, mass dependence
<!-- key: form-of-the-scaling-relation-scatter-evolution -->

- Mechanism. Counts constrain the product of mass function and scaling relation. A wrong functional form (constant bias, self-similar evolution, lognormal scatter) is absorbed by cosmological parameters.
- Size. With a constant bias the Planck × DES analysis gives S8 = 0.791 +0.023/−0.021 and Ω_m = 0.312; with a mass-dependent bias 0.814 +0.019/−0.020 and 0.353 +0.025/−0.031 [src] (arXiv:2509.02068). With self-similar evolution the Chandra–Planck analysis gives S8 = 0.78 ± 0.02, with fitted evolution 0.81 ± 0.02 [src] (arXiv:2402.04006). A redshift-evolution parameter β = 0.86 ± 0.07 can replace w = −0.82 ± 0.07 in the Planck + ACT counts [src] (arXiv:2403.19542): evolution of the relation and dark energy are degenerate.
- Scatter. The richness–mass scatter is not lognormal in DES Y3 × SPT (arXiv:2502.12914); the intrinsic scatter of log λ*–log M200 in KiDS AMICO is 0.05 ± 0.02 [src] (arXiv:2507.14285).
- Mitigation. Free slopes in mass and redshift, correlated scatter, and a mass calibration that spans the redshift range of the counts.

## 11. Likelihood, covariance, photometric redshifts
<!-- key: likelihood-covariance-photometric-redshifts -->

- Sample variance. Neglected by a pure Poisson likelihood, which "always underestimates the errors" for Rubin- or Euclid-like samples [src] (Payerne et al. 2023, arXiv:2210.11093); the framework is Hu & Kravtsov 2003 (arXiv:astro-ph/0203169). Super-sample covariance is in the KiDS AMICO list of marginalised effects (arXiv:2507.14285).
- Photometric redshifts of clusters. In Euclid-like mocks they broaden posteriors by 20–30%; neglecting redshift-space distortions in cluster clustering can bias the constraints [src] (Fumagalli et al. 2025, arXiv:2510.13509).
- Inference machinery. Simulation-based inference adds its own error term: 3% from neural-network stochasticity in the XXL analysis [src] (arXiv:2602.11989).
- Parameter-space effects. The best-constrained combination is not S8; quoting S8 inflates the error and moves the point estimate along the degeneracy (arXiv:2401.02075, arXiv:2406.11970).

## 12. Systematics list of a recent analysis
<!-- key: systematics-list-of-a-recent-analysis -->

The KiDS-1000 AMICO analysis marginalises over: impurities of the background and cluster samples, biases in cluster redshift and richness, projection effects, halo orientation, miscentring, truncation, correlated matter, shear multiplicative bias, baryons, geometric distortion, mass-function uncertainty and super-sample covariance [src] (Lesci et al. 2025, arXiv:2507.14285). It is a usable template for what a counts-plus-lensing paper should list.

## 13. Mass-calibration and selection budgets, analysis by analysis
<!-- key: mass-calibration-and-selection-budgets-analysis -->

One table per analysis, read in the paper body; the place read is in the flag. A plain `[src]` elsewhere in this file means the abstract.

### eRASS1 cosmology (Ghirardini et al. 2024, arXiv:2402.08458) and its DES Y3 calibration (Grandis et al. 2024, arXiv:2402.08455)
<!-- key: erass1-cosmology-ghirardini-et-al-2024-arxiv -->

| Item | What the paper does | Flag |
|---|---|---|
| Mass function | Tinker 2008, chosen for its simple form; Tinker 2010 or Despali 2016 lower σ8 from 0.88 ± 0.02 to 0.86 ± 0.02, Ω_m unchanged; "does not yet limit our cosmological constraints" | [src: Sect. 7.2, 2402.08458] |
| Count-rate–mass relation | lognormal scatter σ_X, prior U(0.05, 2); normalisation, mass slope, redshift evolution of slope and normalisation all free (uniform priors); luminosity-distance and scale-factor evolution fixed to −2 and 2 | [src: Table 1, 2402.08458] |
| Richness–mass relation | normalisation, slope, two redshift terms, scatter free; correlation with count rate ρ in U(−0.9, 0.9); richness noise Poisson in its Gaussian limit; selection cut λ̂ > 3 lowers completeness by 1.1% | [src: Table 1, Sect. 4.3, 2402.08458] |
| WL bias model | ⟨ln(M_WL/M0)⟩ = b_l + b_M ln(M/M0), ln σ²_WL = s_l + s_M ln(M/M0), M0 = 2e14 M_sun, calibrated on TNG300 haloes with M200c > 3e13 M_sun/h at z = 0.24, 0.42, 0.64, 0.95 (three projections each) | [src: Sect. 4.1, Eq. 35, 2402.08455] |
| WL bias value and its uncertainty | b_WL from −0.05 to −0.1; uncertainty from ~1000 re-runs varying source n(z), richness–mass, member contamination, miscentring and shear bias, plus 2% hydro-modelling uncertainty; compressed into two principal components A_WL, B_WL with N(0, 1) priors; the highest-redshift bias is dominated by the Σ_crit uncertainty from photo-z | [src: Sect. 4.5, 2402.08455; Table 1, 2402.08458] |
| Shear and photo-z term | fractional uncertainty of the mean lensing efficiency from 0.55% at z_cl = 0.1 to 4.3% at z_cl = 0.8 | [src: Sect. 3.3.2, 2402.08455] |
| Miscentring | X-ray-to-halo offsets from the eROSITA simulated twin, Rayleigh + Gamma mixture (Eq. 26); extraction model: NFW with a core at the effective miscentring radius (Eq. 29) | [src: Sects. 4.2.2, 4.3, 2402.08455] |
| Contaminants | mixture model with AGN fraction U(0, 0.1) and random-source fraction U(0, 0.15) | [src: Table 1, 2402.08458] |
| Cluster redshifts | relative error N-truncated (0.0050, 0.0011); bias b_z N(1.005, 0.037); catastrophic fraction TN(0.0013, 0.0010) | [src: Table 1, 2402.08458] |
| Cosmology priors | Ω_m U(0.05, 0.95); H0 N(67.77, 0.6), with a distance-ladder or flat prior checked to make no difference; Ω_b U(0.046, 0.052); n_s U(0.92, 1.0) | [src: Sect. 4.6, Table 1, 2402.08458] |

### SPT clusters with DES Y3 and HST lensing (Bocquet et al. 2024, arXiv:2310.12213 and arXiv:2401.02075)
<!-- key: spt-clusters-with-des-y3-and-hst-lensing -->

| Item | What the paper does | Flag |
|---|---|---|
| M_WL–M_halo relation | calibrated on Magneticum hydro/gravity-only pairs: 9798 mass maps of 3266 haloes with M200c > 1.56e14 M_sun/h, projection depth ±20 Mpc/h; the link to gravity-only masses lets a gravity-only mass function (Tinker 2008 is the one cited) be used | [src: Sect. V.2.1, 2310.12213] |
| Baryonic uncertainty | repeated on TNG (1431 maps of 477 haloes); differences Δb_WL = 0.02, Δb_WL,M = 0.018, Δs_WL = 0.25, Δs_WL,M = 0.59, added in quadrature | [src: Eq. 39, 2310.12213] |
| Budget by source | bias uncertainty dominated by baryons at low z and by photo-z (⟨Σ_crit⁻¹⟩) beyond z ≈ 0.45; finite simulation sample, miscentring, member contamination and shear calibration together ~1% up to z ~ 0.8; eight variants (SPT or optical centres, BPZ or DNF, R_min = 0.5 or 0.8 Mpc/h) | [src: Sects. V.2.1–V.2.2, 2310.12213] |
| Radial range | only scales beyond 500 kpc/h, larger than typical SPT centre offsets | [src: Sect. V.2.2, 2310.12213] |
| Priors in the cosmology fit | bias and scatter modulated by N(0, 1) parameters; b_WL,M N(1.029, 0.006²); s_WL,M N(−0.226, 0.040²); SZ and richness relations uninformative, scatter > 0.05; correlation coefficients U(−0.5, 0.5); Ω_b h² and n_s Planck Gaussians; h N(0.70, 0.05²); Σm_ν U(0, 0.6) eV | [src: Table 1, 2401.02075] |
| Multi-observable model | lognormal scatter in ζ, M_WL, λ with full covariance (Eqs. 46–47) | [src: Sect. VII.1, 2310.12213] |
| Mass function uncertainty | 3.5% in amplitude and 2% in slope marginalised as a test; no shifts, so neglected thereafter | [src: Sect. IV.2.3, 2401.02075] |
| Sample and purity | ξ > 5, z > 0.25, ≳ 95% pure after follow-up; DES covers 73% of the area | [src: Sect. II.1, 2401.02075] |

### DES Y1 redMaPPer counts and stacked lensing (DES Collaboration 2020, arXiv:2002.11124)
<!-- key: des-y1-redmapper-counts-and-stacked-lensing-des -->

Sizes are uncertainties on the amplitude of the mass–richness relation, mostly from Table 6 of McClintock et al. 2019 (arXiv:1805.00039) as the paper restates them.

| Item | Size or treatment | Flag |
|---|---|---|
| Multiplicative shear bias | 1.7% Gaussian, fully correlated across bins | [src: Sect. III.3] |
| Source photo-z bias | 2.6% Gaussian, fully correlated | [src: Sect. III.3] |
| Miscentring | ≤ 1%, forward-modelled with priors from X-ray centres | [src: Sect. III.3] |
| Halo–mass correlation (modelling) | 2% Gaussian, simulation-calibrated | [src: Sect. III.3] |
| Selection-effect bias (triaxiality, projection) | simulation correction lowers lensing masses by ≈ 20–30%, richness- and redshift-dependent; taken as uncertain at half its amplitude, ≈ 13% on mass, ≈ 60% of the final mass error budget; adopted after unblinding (Appendix D) | [src: Sect. III.3] |
| Mass function | Tinker; deviations characterised with simulations; no baryonic term for the mass function or the lensing masses (concentration free per bin) | [src: Sect. IV.1] |
| Richness model | P(λ_true \| M) = Poisson convolved with Gaussian scatter of fixed relative width; projection effects forward-modelled in the counts with no nuisance parameter | [src: Sect. IV.1] |
| Count covariance | Poisson, sample variance, miscentring; no covariance between counts and lensing masses | [src: Sect. IV.1] |
| Projection-model systematic | half the parameter shift between the fiducial model and random-point injection | [src: Appendix B] |
| What the calibration paper had assumed | triaxiality factor 0.96 ± 0.02 times projection factor 1.02 ± 0.02, combined 0.98 ± 0.03, constant in richness and redshift; boost factor ≈ 2% on ΔΣ at R = 1 Mpc; miscentring posteriors equal the priors (McClintock et al. 2019, arXiv:1805.00039) | [src: Sects. 5.4.2, 5.6, 1805.00039] |

The contrast between the last row and the selection-effect row is the DES Y1 lesson in numbers: an analytic orientation-plus-projection correction of −2 ± 3% was replaced after unblinding by a simulation correction of −20 to −30%.

### DES Y3 redMaPPer, counts + lensing + clustering (DES Collaboration 2025, arXiv:2503.13632)
<!-- key: des-y3-redmapper-counts-lensing-clustering-des -->

| Item | Size or treatment | Flag |
|---|---|---|
| Data vector | 16491 clusters, 3 redshift bins in 0.2 < z < 0.65 × 4 richness bins from λ = 20 (counts S/N 94.5); cluster shear γ_c (404 points, S/N 31.8), w_cc (149, S/N 18.8), w_cg (124, S/N 39.6), Maglim w_gg (31, S/N 52.5) after scale cuts | [src: Sect. III.1] |
| Richness–mass and selection | lognormal richness–mass relation (four parameters) plus an empirical, scale-dependent model of redMaPPer selection effects (Sect. C5 of To et al. 2025, arXiv:2503.13631) | [src: Sect. III.2] |
| Cluster lensing | linear transformation of ΔΣ that localises the signal; scale cuts set by non-linear bias and non-linear matter modelling | [src: Sect. III.2] |
| Shared 3×2pt nuisances | TATT intrinsic alignments, photo-z shifts (and stretch for Maglim), multiplicative shear bias, point-mass marginalisation; HMCode2020 matter power spectrum | [src: Sect. III.2] |
| Prior-volume effects | 2D Ω_m–S8 constraint biased by < 0.3 of the statistical uncertainty in noiseless simulated analyses | [src: Sect. III.2] |
| Emulator | LINNA, validated to LSST-Y10 precision | [src: Sect. III.2] |
| Blinding | parameter-level only (the 3×2pt data were already unblinded): cosmological shifts up to 5σ, mass–observable and galaxy-bias shifts up to 2σ; χ² not blinded | [src: Sect. IV.1] |

### KiDS-1000 AMICO counts + stacked lensing (Lesci et al. 2025, arXiv:2507.14285)
<!-- key: kids-1000-amico-counts-stacked-lensing-lesci-et -->

| Item | Size or treatment | Flag |
|---|---|---|
| Shear calibration | σ_m = 0.02 on the multiplicative bias, added to the profile covariance as σ² g_k g_l | [src: Eq. 44] |
| Source redshifts | σ_SOM = 0.01 for the first two cluster-redshift bins, 0.04 for the last | [src: Eq. 44] |
| Orientation + projection | 4% residual on mass, hence σ_OP = 0.03 on the profile through Γ = d ln ΔΣ/d ln M ≃ 0.7; justified by orientation and projection biases cancelling in KiDS-DR3 AMICO (3% residual) and by the redMaPPer factor 0.98 ± 0.03 | [src: Sect. 5.4, Eqs. 44–46] |
| Mass function | Tinker 2008 times a bias factor B_HMF = s log(M200m/M*) + q (log M* = 13.8) with a 2D Gaussian prior following Costanzi et al. 2019, mean (s, q) = (0.037, 1.008); M200c converted to M200m with a mass-conversion model | [src: Sect. 5.1, Eq. 19; Sect. 5.4] |
| Richness–mass relation | lognormal, mean α + β log(M/M_piv) + γ log(H(z)/H(z_piv)), M_piv = 1e14 M_sun/h, z_piv = 0.4, λ*_piv = 50; all four parameters uniform | [src: Eqs. 20–21, Sect. 5.4] |
| Profile model | concentration amplitude free, mass and redshift slopes fixed to Duffy et al. 2008 values (−0.084, −0.47); truncation F_t N(3, 0.5) | [src: Sect. 5.4] |
| Miscentring | f_off N(0.3, 0.1), f_off > 0; σ_off U(0, 0.5) Mpc/h | [src: Sect. 5.4] |
| Count likelihood | Poisson convolved with Gaussian super-sample modes (Lima & Hu 2004); lensing Gaussian with bootstrap + systematic covariance | [src: Eqs. 39–44] |
| Cosmology priors | Ω_cdm and A_s uniform; Ω_b and n_s Gaussian on Planck 2018 means with widths of 5σ; h N(0.7, 0.03) | [src: Sect. 5.4] |
| Blinding | two altered completeness functions: S8 = 0.72, 0.73, 0.74 for original and blind versions (tests without SSC) | [src: Appendix B, Table 3] |

### HSC Y3 shear-selected clusters (Chiu et al. 2024, arXiv:2406.11970)
<!-- key: hsc-y3-shear-selected-clusters-chiu-et-al-2024 -->

Read from the LaTeX source; no HTML rendering was available.

| Item | Size or treatment | Flag |
|---|---|---|
| WL mass bias model | ln b_WL = ln A_WL + B_WL ln(M/M_piv) + γ_WL ln((1+z)/(1+z_piv)), calibrated for HSC lensing of X-ray clusters on Magneticum following the Grandis et al. method; baryonic uncertainty from DM-only versus hydro runs | [src: Sect. 4.5, Eq. for M_WL–M–z] |
| Mass- and redshift-dependent priors | A_WL = 0.903 ± 0.030, B_WL = −0.057 ± 0.022, γ_WL = −0.474 ± 0.062, σ_WL = 0.238 ± 0.037 at M_piv = 2.89e14 M_sun/h (M200c), z_piv = 0.6 | [src: Sect. 4.5.1] |
| Constant-bias alternative | A_WL N(0.99, 0.05²), from CAMIRA richness-inferred masses with three richness–mass calibrations | [src: Sect. 4.5.2] |
| Source-selection difference | ≲ 3% for z_cl ≲ 0.7 between the calibration's and this work's source cuts | [src: Sect. 4.5.1] |
| Inner radii | including R ≳ 0.2 instead of ≳ 0.5 Mpc/h raises the WL scatter by ≈ 50% (citing Grandis et al. 2021) | [src: Sect. 4.5.1] |
| Blinding | three shape catalogues with blinded multiplicative bias (offsets in {−0.1, …, 0.1}); selection functions recomputed by injection for each | [src: Sect. 4.7] |

### Planck 2015 SZ counts (Planck Collaboration 2015 XXIV, arXiv:1502.01597)
<!-- key: planck-2015-sz-counts-planck-collaboration-2015 -->

| Item | Size or treatment | Flag |
|---|---|---|
| Y–M relation | E^−β(z) [D_A² Ȳ500 / 1e-4 Mpc²] = Y* (h/0.7)^(−2+α) [(1 − b) M500 / 6e14 M_sun]^α; from X-ray hydrostatic masses of the 2013 analysis, with M_X = (1 − b) M500 and b constant in mass and redshift | [src: Sect. 3.2, Eq. 7] |
| Scaling priors | log Y* = −0.19 ± 0.02; α = 1.79 ± 0.08 (free in the N(z, q) fit); β = 0.66 ± 0.50, fixed to its central value; σ_lnY = 0.173 ± 0.023 | [src: Table 1] |
| Mass-scale priors | WtG 1 − b = 0.688 ± 0.072; CCCP 0.780 ± 0.092 (baseline; stat 0.07 and sys 0.06 in quadrature); CMB lensing 1/(1 − b) = 0.99 ± 0.19; 2013 baseline 0.8 in [0.7, 1] | [src: Sect. 4.3, Table 2] |
| Mass function | Tinker 2008 baseline; Watson et al. 2013 shifts results by about 1σ to higher Ω_m and lower σ8 along the degeneracy, increasing the tension | [src: Appendix A.2] |
| Detection | matched filters over six bands with the Arnaud et al. 2010 universal pressure profile as template, θ500 from 1 to 35 arcmin | [src: Sect. 2] |
| Sample variance | neglected: bins assumed uncorrelated, justified by the high masses (Hu & Kravtsov 2003) | [src: Sect. 5.1] |

### Planck + ACT counts reanalysis (Lee et al. 2024, arXiv:2403.19542)
<!-- key: planck-act-counts-reanalysis-lee-et-al-2024 -->

| Item | Size or treatment | Flag |
|---|---|---|
| ACT sample | 59 clusters of the 182-cluster 2018 ACTPol catalogue at SNR_2.4 > 5.6, 987.5 deg², 148 GHz only (spatial, not spectral, selection) | [src: Sect. 2.2] |
| Planck sample | the 439-cluster MMF3 cosmology sample | [src: Sect. 2.2, Fig. 2 caption] |
| Mass-bias priors | CCCP + MENeaCS 1 − b = 0.84 ± 0.04 (61 Planck clusters) and Planck CMB lensing 0.71 ± 0.10, replacing the 2015 priors; the bias is assumed a weak function of mass and redshift; an Eddington-bias correction is noted to lower the CCCP and WtG values | [src: Sect. 3.1] |

### Planck PSZ2 × DES Y3 shear × Chandra (Aymerich et al. 2025, arXiv:2509.02068)
<!-- key: planck-psz2-x-des-y3-shear-x-chandra-aymerich -->

| Item | Size or treatment | Flag |
|---|---|---|
| Lensing sample | 93 PSZ2 cosmology clusters inside the DES Y3 footprint (4143 deg², 5–6 sources per arcmin²); selected only by sky position, hence taken as representative | [src: Sect. 2.3] |
| Y–M relation | calibrated on Chandra Y_X masses with a Malmquist-bias correction: E^−2/3 D_A² Y_SZ / Y_piv = 10^(−0.29 ± 0.01) (M_H/M_piv)^(1.70 ± 0.1); its parameters sampled within these Gaussian priors | [src: Sect. 3.3, Eq. 5; Sect. 6.1] |
| M_WL–M relation | lognormal, ⟨ln(M_WL/M_p)⟩ = b(z) + b_M ln(M/M_p), M_p = 2e14 M_sun, calibrated on synthetic shear profiles after Grandis et al. 2024; four N(0, 1) nuisance parameters | [src: Sect. 4.2.3, Eqs. 24–25] |
| Analysis variants | BCG, SZ or MCMF centres; bpz or dnf for member contamination; inner bin 0.5 or 0.8 Mpc/h (baseline: BCG, bpz, 0.8) | [src: Sect. 4.2.3, Table 2] |
| Bias and priors | (1 − b) and its mass and redshift evolution flat; Ω_b h² N(0.0218, 0.0012) from BBN; n_s N(0.965, 0.004); BOSS DR12 BAO for H0 | [src: Sect. 6.1, Table 3] |
| Mass function | Tinker 2008 | [src: Sect. 5.1] |

### ACT DR5 × DES Y3 lensing (Shin et al. 2025, arXiv:2512.18935)
<!-- key: act-dr5-x-des-y3-lensing-shin-et-al-2025-arxiv -->

| Item | Size or treatment | Flag |
|---|---|---|
| Bias model | 1/(1 − b) = A_mass (M_SZ/3e14 M_sun)^η ((1 + z)/1.45)^ζ, or a constant; M_SZ from the Hilton et al. 2021 relation with σ_lnM fixed at 0.2 (freeing it does not change 1 − b) | [src: Sect. 4.3, Eq. 20] |
| Source photo-z | shift Δz_s sampled from DES Y3: mean 0 (0), σ 0.011 (0.017) for source bins 3 (4) | [src: Sect. 4.5.1] |
| Shear calibration | m sampled from DES Y3: −0.024 (−0.037) ± 0.008 for bins 3 (4); cluster lensing cannot self-calibrate either term | [src: Sect. 4.5.2] |
| Miscentring | BCG centres, McClintock et al. 2019 model | [src: Sect. 4.5.3] |
| Member dilution | boost factor "typically a factor of 1–2 in central regions", strongly dependent on source selection; measured by P(z) decomposition and fitted | [src: Sect. 3.4] |

## What a referee checks in a results section
<!-- key: what-a-referee-checks-in-a-results-section -->

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
<!-- key: not-verified -->

- Contamination of CMB-lensing cluster mass estimators by the cluster's own tSZ and kSZ signal: quantified since in `deep/cmb-cluster-lensing.md` (2026-10-18), from arXiv:1705.00411, arXiv:2305.06326, arXiv:2404.02153 and arXiv:2402.18346.
- The cross-calibration of eROSITA temperatures with Chandra and XMM-Newton: the corresponding paper was not read beyond its title. (The eRASS1 contaminant priors are now in section 13; the member-dilution size is given for DES Y1 and ACT × DES there.)
- The numerical values of the SPT M_WL–M_halo parameters (Table 4 of arXiv:2310.12213): the table cells did not render.
- The priors of the DES Y3 cluster analysis (its Table 2) and its mass function: the table did not render and the sections read do not name the mass function.
- Cluster-finder photometric-redshift performance for HSC shear-selected clusters.
