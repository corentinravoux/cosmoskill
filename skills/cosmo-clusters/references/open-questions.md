# Galaxy-cluster cosmology — open questions

Scope: live disagreements, method debates, forecasts and stale claims.
Snapshot: 2026-10-07

## 1. Do clusters see a low S8, a high S8, or neither?
<!-- key: do-clusters-see-a-low-s8-a-high-s8-or-neither -->

Current ΛCDM values of S8 = σ8 (Ω_m/0.3)^0.5 from independent cluster samples (all [src] in `results.md`):

| Sample | Selection | S8 | Citation |
|---|---|---|---|
| eRASS1 | X-ray | 0.86 ± 0.01 | arXiv:2402.08458 |
| DES Y3 redMaPPer | optical | 0.864 ± 0.035 | arXiv:2503.13632 |
| SDSS redMaPPer + HSC Y3 lensing | optical | 0.816 +0.041/−0.039 | arXiv:2309.13025 |
| SPT (SZ + ECS + 500d) + DES Y3 + HST | SZ | 0.795 ± 0.029 | arXiv:2401.02075 |
| Planck PSZ2 + DES + Chandra + BAO, constant bias | SZ | 0.791 +0.023/−0.021 | arXiv:2509.02068 |
| KiDS-1000 AMICO | optical | 0.74 ± 0.03 | arXiv:2507.14285 |
| XXL C1 + HSC Y3 (simulation-based inference) | X-ray | 0.867 ± 0.063 | arXiv:2602.11989 |
| HSC shear-selected | lensing | 0.993 +0.084/−0.126 | arXiv:2406.11970 |

The spread among cluster samples is larger than the spread between clusters and any other probe. The extremes, eRASS1 and KiDS AMICO, differ by 0.12, or about 3.8σ if the errors are Gaussian and independent [der: 0.12 / sqrt(0.01² + 0.03²)]; they are not fully independent, since eRASS1 uses KiDS-1000 among its lensing data. Planck clusters and eRASS1 differ by 2.9σ according to the Planck × DES authors [src, arXiv:2509.02068].

For orientation, the sibling skills give KiDS-Legacy cosmic shear at 0.815 +0.016/−0.021 and DES Y6 3×2pt at 0.789 ± 0.012 [sec, `cosmo-weak-lensing` SKILL.md], and a primary-CMB σ8 of 0.8137 ± 0.0037 from the SPT + ACT + Planck combination [sec, `cosmo-cmb` SKILL.md]. SPT and Planck clusters sit with DES; DES Y3 clusters and eRASS1 sit above every lensing value.

There is therefore no single "cluster S8" and no cluster S8 tension in one direction. The summary is that the spread between cluster analyses, about ±0.05 [der: half the range 0.74–0.86, shear-selected sample excluded], exceeds the statistical error of the best of them, 0.01.

## 2. eRASS1: the outlier with the smallest error
<!-- key: erass1-the-outlier-with-the-smallest-error -->

- For: the largest sample (5259 clusters [src]), lensing calibration from three surveys, a selection function from simulated skies (arXiv:2402.08458, arXiv:2402.08457).
- Against, from inside the collaboration: with one extra low-redshift degree of freedom in the growth, the same data give a growth index γ = 1.19 ± 0.21, in tension with 0.55, and S8 "recovers the value inferred by cosmic shear studies" [src] (Artis et al. 2024, arXiv:2410.09499). The high S8 and the suppressed late growth are the same feature of the data seen through two models.
- Against, from outside: in the eROSITA best-fit cosmology the Planck cosmology sample would contain 1098 clusters against 439 observed, and the predicted tSZ power spectrum is "two times higher at all scales" than measured; fitting only the bias gives (1 − b) = 0.630 ± 0.034 [src] (Aymerich et al. 2025, arXiv:2509.08673). In the SPT cosmology the same test gives 498 clusters and (1 − b) = 0.790 ± 0.070.
- What would decide it: a deeper eROSITA sample with the same pipeline; an independent analysis of the public eRASS1 catalogue; SPT-3G counts over the 1279 clusters in common (arXiv:2607.01175).

## 3. The Planck mass bias: which number, and is there still a tension?
<!-- key: the-planck-mass-bias-which-number-and-is-there -->

| Statement | (1 − b) | Citation | Flag |
|---|---|---|---|
| Needed to reconcile Planck counts with Planck primary CMB in the Planck model | 0.61 ± 0.03 (Planck sample); "about 40%" bias in 2013 | arXiv:2403.19542, arXiv:1303.5080 | [src] |
| Lensing calibrations of the XMM-based Planck scale | 0.688 ± 0.072; 0.76 ± 0.05 ± 0.06; 0.71 ± 0.10 (CMB lensing); 0.73 +0.10/−0.11; 0.72 ± 0.11 | arXiv:1402.2670, arXiv:1502.01883, arXiv:1904.07887, arXiv:2606.17984, arXiv:2606.24142 | [src] |
| Clustering of Planck clusters | 0.62 +0.14/−0.11 | arXiv:2302.14074 | [src] |
| Simulations and X-ray thermodynamics | 0.8–0.9 | arXiv:2409.07849, arXiv:1805.00034 | [src] |
| Planck + DES shear profiles, relative to a Chandra-calibrated relation | 0.844 +0.055/−0.062, with a 1.6σ difference from the CMB | arXiv:2509.02068 | [src] |

Reading. The lensing values cluster at 0.70–0.75, between the simulation expectation and the value the 2013–2015 CMB comparison required. The 2025 Planck × DES analysis reports only a 1.6σ difference from the CMB. Two things changed between 2015 and 2025: the mass calibration (lensing instead of a prior on hydrostatic bias) and the CMB reference itself. The 3.7σ of Planck 2015 was the upper end of a range that started at "a little over one standard deviation", depending on the (1 − b) prior [src, arXiv:1502.01597].

Still open: X-COP gas fractions exclude the low bias "at high significance, unless the most massive halos are missing a substantial fraction of their baryons" [src, arXiv:1805.00034]; whether the bias depends on mass and redshift (index −1.8 +0.5/−0.6 in redshift for ACT [src, arXiv:2512.18935]; α_SZ = 1.49 against 1.8 [src, arXiv:2112.03606]); and whether a redshift trend in (1 − b) is a property of clusters or of the lensing calibration at high redshift, where the lensing systematic grows to 10% at z = 0.95 [src, arXiv:2310.12213].

## 4. Has the optical selection problem been solved?
<!-- key: has-the-optical-selection-problem-been-solved -->

- Evidence that it has: DES Y3, with a cluster-based multiprobe data vector, finds S8 = 0.864 ± 0.035 and, with 3×2pt, 0.811 +0.022/−0.020 with a probability-to-exceed of 0.6 against Planck [src, arXiv:2503.13632]. The simulation-based reanalysis of DES Y1 moves Ω_m from 0.179 to 0.254 and σ8 to 0.826 [src, arXiv:2510.25706]. SDSS redMaPPer with HSC Y3 lensing gives 0.816 [src, arXiv:2309.13025].
- Evidence that it has not: KiDS-1000 AMICO finds S8 = 0.74 ± 0.03 and Ω_m = 0.22 ± 0.02, 2.8σ from Planck [src, arXiv:2507.14285], with an explicit projection-effect term. The reanalysed DES Y1 is still 2.58σ from Planck, now through a low Ω_m [src, arXiv:2510.25706]. DES Y3 × SPT cross-matching finds redshift trends that the projection-effect simulations do not capture (arXiv:2502.12914). The same anisotropic-boost model gave 0.718 with SDSS lensing and 0.816 with HSC lensing (arXiv:2112.09059, arXiv:2309.13025).
- The position of the two camps: one calibrates richness by lensing with a forward model of the finder; the other holds that low-richness optical clusters need a multi-wavelength anchor, because the richness–mass slope from SZ cross-calibration is B ≈ 1 against B ≈ 0.75 from optical-only calibration [src, arXiv:2101.04984].
- What decides it: DES Y6 clusters with 3×2pt (strategy in arXiv:2503.13631), Euclid DR1 with its CosmoPostProcess correction (arXiv:2605.02723), and SZ cross-matches at lower richness from SPT-3G.

## 5. Hydrostatic bias: are simulations and lensing in conflict?
<!-- key: hydrostatic-bias-are-simulations-and-lensing-in -->

Simulations give a median bias of 10–20% (arXiv:2409.07849); lensing of SZ-selected samples gives 25–30% against the XMM-based scale. Part of the gap is not hydrodynamics: the X-ray spectroscopic-like temperature alone gives 0.22 ± 0.01 in FLAMINGO where the SZ-weighted temperature gives −0.05 ± 0.01 [src, arXiv:2404.08539], and the Chandra–XMM calibration difference moves (1 − b) from 0.76 to 0.89 [src, arXiv:2402.04006]. Whether what remains requires new physics in the intracluster medium is open. Direct measurements of gas motions would settle it; no such result was fetched this session.

## 6. Splashback: a ΛCDM test or a selection test?
<!-- key: splashback-a-lambdacdm-test-or-a-selection-test -->

Optically selected clusters gave splashback radii smaller than N-body predictions, which the authors judged unlikely to come solely from dynamical friction or cluster-finding systematics (arXiv:1601.06063). SZ-selected clusters agree with simulations and redMaPPer clusters are about 2σ low in the same analysis [src, arXiv:1811.06081]; the 2026 KiDS-1000 AMICO measurement from lensing and from the cluster–galaxy correlation agrees with ΛCDM [src, arXiv:2602.07114]. The current reading is that the early discrepancy was selection. Open points: precision is 10–14% per stack, too coarse for the accretion-rate or modified-gravity tests proposed; and the 6.6σ assembly-bias signal of arXiv:1601.06063 rests on a split by mean projected member distance, whose sensitivity to projection effects was not checked this session (see "Not verified").

Date-sorted leads not read (2025–2026, titles only): splashback of RASS-MCMF clusters with DES Y3; MaDCoWS2 splashback radii to z = 1.65; relation between accretion shocks and splashback radii.

## 7. Method debates
<!-- key: method-debates -->

- How much does clustering add? More than 300% in figure of merit for Euclid-like optical samples [arXiv:2510.13509, **forecast**], but 2–8% on σ(w) for future SZ samples with current mass-relation priors, vanishing if the priors tighten by a factor of two [arXiv:2510.14464, **forecast**]. The answer depends on the assumed external mass calibration; a forecast that does not state it is not usable.
- Poisson, Gaussian or simulation-based likelihood (arXiv:2210.11093, arXiv:2602.11989).
- Mass function: fitting function, emulator, or hydrodynamical calibration; the halo-finder dependence is unresolved at the level Euclid needs (arXiv:2208.02174).
- Constant or mass-dependent bias: the choice moves Ω_m from 0.312 to 0.353 in the same data [src, arXiv:2509.02068].
- Reporting: best-constrained combination with a survey-specific exponent, or S8. Both should be given.
- Extended models from counts. SPT finds w = −1.45 ± 0.31 alone and −1.34 +0.22/−0.15 with Planck, 2.2σ from −1 [src, arXiv:2401.02075]; with DES 3×2pt the departure is 1.7σ [src, arXiv:2412.07765]. eRASS1 finds w = −1.12 ± 0.12 [src, arXiv:2402.08458]. Counts are degenerate between w and the redshift evolution of the scaling relation (arXiv:2403.19542), so these are not evidence for phantom dark energy; the wider discussion is in `cosmo-dark-energy-modified-gravity`.
- Early dark energy from eRASS1: f_EDE < 0.3 from counts alone; the 3.2σ preference (f_EDE = 0.10 +0.04/−0.03, H0 = 71.4 ± 1.4) appears only with CMB, BAO and CMB lensing, and uses the 0.1 < z < 0.45 subsample [src, arXiv:2609.07834].

## 8. What the next data will decide
<!-- key: what-the-next-data-will-decide -->

| Data | Status on 2026-10-07 | What it tests | Citation |
|---|---|---|---|
| SPT-3G Main five-year counts | catalogue of 7190 confirmed clusters and a clustering measurement published; no counts cosmology found | SPT 2024 result with about seven times the sample [der: 7190/1005]; eRASS1 cross-check | arXiv:2607.01175, arXiv:2610.08947 |
| ACT DR6 counts | catalogue of 10040 clusters published; only an f_NL analysis found | independent SZ counts with DES, HSC and KiDS lensing | arXiv:2507.21459, arXiv:2602.03917 |
| DES Y6 clusters + 3×2pt | modelling strategy validated on mocks; no result found | optical selection at full DES depth | arXiv:2503.13631 |
| Euclid DR1 clusters | Q1 workflow validation only (426 clusters in 63 deg²) | optical counts and clustering with space-based lensing | arXiv:2503.19196 |
| eROSITA beyond eRASS1 | no deeper cosmology found | whether the high S8 persists | arXiv:2609.07834 |
| HSC shear-selected, optically confirmed sample | 129 clusters in the cosmology analysis | a gravity-only selection | arXiv:2406.11970 |
| Rubin LSST | survey began 30 June 2026 [sec, `cosmo-weak-lensing` SKILL.md]; cluster-lensing blending study on DC2 | deep stacked lensing for all southern samples | arXiv:2609.12158 |
| SPT-3G+ | receiver installation planned for early 2029 | high-redshift SZ clusters | arXiv:2608.20236 |

## 9. Forecasts
<!-- key: forecasts -->

Every row is a **forecast**.

| Experiment | Forecast | Assumptions | Citation | Flag |
|---|---|---|---|---|
| Euclid photometric clusters | Δw0 = 0.03, Δwa = 0.2 with free curvature, figure of merit 291; with Planck Δw0 = 0.02, Δwa = 0.07, figure of merit 802; Δf_NL ~ 6.6; Δγ = 0.02; ΔΩ_ν = 0.0013 | Fisher matrix, 2015; depends on knowledge of the observable–mass relation, which the abstract calls "crucial" | Sartoris et al. 2016, arXiv:1505.02165 | [src] |
| Euclid counts + clustering | photo-z broaden posteriors by 20–30%; clustering raises the figure of merit by more than 300% | 1000 Euclid-like mock catalogues | arXiv:2510.13509 | [src] |
| CMB-S4 wide and deep | 75000 clusters over f_sky = 50% and 14000 over 3%; about 1350 at z ≥ 2; σ(w0) ≲ 1%; 2.5–4.5σ detection of Σm_ν with CMB-cluster lensing calibration; CMB-HD three times more clusters | 2021 experiment configuration. CMB-S4 lost DOE and NSF support on 9 July 2025 [sec, `cosmo-cmb` SKILL.md], so these numbers describe a design, not a scheduled survey | Raghunathan et al. 2022, arXiv:2107.10250 | [src] |
| Future SZ samples, 33000–140000 clusters | clustering improves σ(w) by 1.023–1.079 and σ(Ω_m) by 1.068–1.145; with weak priors, the mass slope and redshift evolution of the relation improve by 1.389 ± 0.041 and 1.340 ± 0.039 | three prior levels on the mass–observable relation | Zhan & Reichardt 2025, arXiv:2510.14464 | [src] |
| eROSITA-like sample | neglecting baryons in the mass function biases Ω_m low by about 0.01, comparable to the expected uncertainty | idealised survey, Magneticum | arXiv:1502.07357 | [src] |
| Rubin- or Euclid-like counts | Gaussian likelihood sufficient; little gain from many mass–redshift bins | 1000 PINOCCHIO catalogues, ideal setup | arXiv:2210.11093 | [src] |

The Sartoris forecast of ΔΣm_ν = 0.01 (as written in the abstract, units of eV presumably) predates the DES Y1 lesson and assumes a mass calibration that no optical survey has yet demonstrated.

## 10. Misconceptions and stale claims
<!-- key: misconceptions-and-stale-claims -->

| Claim still met | Why it is wrong or stale | Correcting paper |
|---|---|---|
| "Cluster counts give a low σ8, like weak lensing." | True of Planck 2013–2015 and KiDS AMICO; false of eRASS1 (0.86 ± 0.01) and DES Y3 (0.864 ± 0.035). | arXiv:2402.08458, arXiv:2503.13632 |
| "Planck clusters are in 3–4σ tension with the CMB." | 3.7σ was the extreme of a prior-dependent range in 2015. Planck × DES in 2025: 1.6σ. | arXiv:1502.01597, arXiv:2509.02068 |
| "Reconciling Planck needs 1 − b ≈ 0.6, which simulations exclude, so new physics." | 0.6 is specific to the Planck XMM-based relation and the Planck model; lensing gives 0.70–0.75; X-ray calibration accounts for part of the gap. | arXiv:2402.04006, arXiv:2403.19542 |
| "(1 − b) = 0.84 from Planck × DES contradicts the lensing value of 0.7." | Different reference relation (Chandra against XMM). | arXiv:2509.02068 |
| "DES Y1 clusters measured S8 = 0.65." | The collaboration attributed it to systematics in the lensing model; it is superseded. | arXiv:2002.11124, arXiv:2503.13632, arXiv:2510.25706 |
| "The halo mass function is universal and known to a per cent." | Tinker 2008: ≲ 5% at z = 0, amplitude evolves by 20–50% to z = 2.5. | arXiv:0803.2706 |
| "Baryons do not matter for cluster counts." | True for SPT-like and Planck-like masses, not for eROSITA-like thresholds. | arXiv:1502.07357 |
| "Splashback radii are smaller than ΛCDM predicts." | Optical selection; SZ-selected and recent lensing results agree with ΛCDM. | arXiv:1811.06081, arXiv:2602.07114 |
| "eROSITA cluster cosmology uses the all-sky survey." | eRASS1 is the first six months, western Galactic hemisphere, 12791 deg² for the cosmology sample. | arXiv:2402.08452 |
| "ACT and SPT-3G cluster cosmology." | The last ACT counts cosmology is from 2013 (15 + 7 clusters). No ΛCDM analysis of ACT DR5 or DR6 or SPT-3G counts was found. | arXiv:1301.0816, arXiv:2607.01175 |
| "f_gas constrains growth." | It is a distance and Ω_b/Ω_m probe. | arXiv:2111.09343 |
| "Euclid Q1 delivered a cluster cosmology sample." | 426 clusters in 63 deg², a workflow validation. | arXiv:2503.19196 |
| "CMB-S4 will deliver 75000 clusters." | A 2021 design forecast for an experiment that has lost agency support [sec, `cosmo-cmb` SKILL.md]. | arXiv:2107.10250 |
| "SPT clusters prefer phantom dark energy." | 2.2σ with Planck, 1.7σ with DES 3×2pt and Planck; degenerate with scaling-relation evolution. | arXiv:2401.02075, arXiv:2412.07765 |
| "A blind analysis is a validated analysis." | DES Y1 was blind. | arXiv:2002.11124 |

## Not verified
<!-- key: not-verified -->

- Whether the member-distance split behind the 2016 cluster assembly-bias detection is contaminated by projection effects: the later literature on this was not fetched.
- Any eROSITA cosmology from eRASS:4 or eRASS:5 depth, and the release plan of the German consortium: not found; not searched on collaboration pages.
- Simons Observatory cluster forecasts and catalogues: a date-sorted search returned none.
- A CMB-lensing cluster mass calibration dated after June 2025: a date-sorted search returned none.
- Direct X-ray measurements of gas motions in clusters and their implication for non-thermal pressure.
- Kinetic SZ and tSZ power-spectrum constraints related to clusters: see `cosmo-cmb-lss-cross-correlations`.
- The Euclid DR1 date and content for clusters: see `cosmo-weak-lensing` and `cosmo-surveys-facilities`.
