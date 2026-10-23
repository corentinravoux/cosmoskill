# Statistics and inference — quantified facts a referee needs

Scope: sizes of covariance corrections, documented projection-effect shifts, documented differences between tension metrics and model-comparison statistics on the same data, emulator error budgets, sampler and coverage-test outcomes.
Snapshot: 2026-10-16

Flags: `[src]` read this session in the cited paper; `[sec]` taken from a named secondary source; `[der]` derived here, derivation stated.

## 1. Covariance corrections for finite mock counts
<!-- key: covariance-corrections-for-finite-mock-counts -->

### 1.1 Size of the corrections for typical mock counts
<!-- key: size-of-the-corrections-for-typical-mock-counts -->

All entries are `[der]`: computed here from the formulae read in arXiv:2108.10402 and arXiv:1312.4841 (see `physics-and-methods.md` §2.1), with `h = (n_s − 1)/(n_s − n_d − 2)`, `DS = 1 + B (n_d − n_θ)`, and `S'/S = (n_s − 1) DS / (n_s − n_d + n_θ − 1)`. The assumption is Gaussian data and independent mocks. The last column is the factor by which a naive parameter error (Gaussian likelihood with the uncorrected `S^-1`) must be multiplied.

| n_s | n_d | n_θ | Hartlap h (covariance) | 1/h (precision) | DS factor (variance) | S'/S (variance) | sqrt(S'/S) (error bar) |
|---|---|---|---|---|---|---|---|
| 100 | 20 | 5 | 1.269 | 0.788 | 1.195 | 1.408 | 1.187 |
| 200 | 50 | 5 | 1.345 | 0.744 | 1.306 | 1.688 | 1.299 |
| 600 | 50 | 5 | 1.093 | 0.915 | 1.082 | 1.170 | 1.082 |
| 1000 | 13 | 7 | 1.014 | 0.986 | 1.006 | 1.012 | 1.006 |
| 1000 | 50 | 7 | 1.054 | 0.949 | 1.045 | 1.092 | 1.045 |
| 1000 | 100 | 10 | 1.113 | 0.899 | 1.100 | 1.209 | 1.100 |
| 1000 | 200 | 10 | 1.252 | 0.799 | 1.238 | 1.529 | 1.237 |
| 1000 | 400 | 10 | 1.671 | 0.599 | 1.653 | 2.712 | 1.647 |
| 2048 | 200 | 10 | 1.109 | 0.902 | 1.103 | 1.216 | 1.103 |
| 2048 | 400 | 10 | 1.244 | 0.804 | 1.237 | 1.528 | 1.236 |
| 25000 | 5000 | 20 | 1.250 | 0.800 | 1.249 | 1.560 | 1.249 |

Reading the table: the Hartlap factor and the Dodelson–Schneider factor are of similar size and both are needed; two different numbers answer "what does it cost". (i) Against a perfectly known covariance, the scatter of the best fit grows by the Dodelson–Schneider variance factor: 1.10 for 1000 mocks and 100 points, 1.65 for 400 points, that is 5% and 29% on the error bar. (ii) Against a posterior built naively on the raw sample covariance, the error bar must be widened by the last column, which contains the Hartlap term as well: 10% and 65%. The two happen to be numerically close (DS variance 1.100 and 1.653; total error-bar factor 1.100 and 1.647), which invites quoting one for the other. A short data vector (the `n_d = 13` row, chosen as an illustration) is unaffected; a long joint data vector is not.

### 1.2 Numbers stated in the papers
<!-- key: numbers-stated-in-the-papers -->

| Statement | Value | Source | Flag |
|---|---|---|---|
| BOSS: error increase when the covariance comes from 600 mocks, "depending on how the cosmological parameters of interest are measured" | ~20% | Percival et al. 2014, arXiv:1312.4841 (abstract) | [src] |
| Parameter variance increase from a simulation covariance | factor of order `1 + N_b/N_s` | Dodelson & Schneider 2013, arXiv:1304.2593 | [src] |
| Best-fit-scatter term, "fractional increase in variance" (not error bar; Hartlap term excluded): BOSS 600 mocks, 41 bins; DLS 1000, 60; CFHTLenS 184, 24 | 7%; 6%; 13% | arXiv:1304.2593 | [src: Table 1] |
| DESI DR1 full shape: 1000 EZmocks per tracer and redshift bin, Hartlap and Percival 2014 factors, plus a larger tracer-dependent rescaling for mock realism | ~20% Fourier-space EZmock–analytic mismatch with realistic fibre assignment | DESI Collaboration 2024, arXiv:2411.12021 | [src: Sects. 5.7–5.8] |
| Realisations needed for a 5% error on a parameter error, `N_D << 100` | ≥ 200 | Taylor et al. 2013, arXiv:1212.4359 | [src: abstract] |
| Standard bootstrap, variance of ξ(s), 1–25 Mpc/h | overestimated by ~40% | Norberg et al. 2009, arXiv:0810.1885 | [src] |
| Internal covariance, Ω_m–σ8 contour volume against truth (DES 5-year forecast) | ≳ 85% | Friedrich et al. 2016, arXiv:1508.00895 | [src] |
| Corrected jackknife or bootstrap against 1000 Quijote boxes | within ~10% | Mohammad & Percival 2022, arXiv:2109.07071 | [src: abstract] |
| DES Y3: effect of the `f_sky` approximation on χ² at maximum posterior | +3.7% (Δχ² ≈ 18.9) | Friedrich et al. 2021, arXiv:2012.08568 | [src: abstract] |
| DES Y3: extra scatter of the maximum posterior from evaluating the covariance at the wrong parameters | ~3% for Ω_m and σ8, ~5% for w | arXiv:2012.08568 | [src] |
| KiDS-1000: bias of S8 from known modelling and inference systematics | ≤ 0.1σ | Joachimi et al. 2021, arXiv:2007.01844 | [src] |
| RascalC: cost of a finely binned 2PCF covariance | < 100 CPU-hours | Philcox et al. 2019, arXiv:1904.11070 | [src: abstract] |
| DESI 2024: analytic configuration-space covariance adequate for BAO; analytic Fourier-space covariance does not reproduce the mocks for full shape, hence a corrected mock covariance | qualitative | Forero-Sánchez et al. 2024, arXiv:2411.12027 | [src] |

### 1.3 Non-Gaussian likelihood and parameter-dependent covariance: documented sizes
<!-- key: non-gaussian-likelihood-and-parameter-dependent -->

| Case | Effect | Source | Flag |
|---|---|---|---|
| BOSS power-spectrum multipoles, Gaussian against mock-estimated likelihood | fσ8 shifts by −0.44σ, other parameters not significantly | Hahn et al. 2019, arXiv:1803.06348 | [src] |
| Group multiplicity function, same test | `log M_1` and α shift by +0.43σ and −0.51σ, broaden by 42% and 66% | arXiv:1803.06348 | [src: abstract] |
| Shear correlation functions, 100 deg² mocks | no significant bias in 1D posteriors of Ω_m, σ8 | Lin et al. 2020, arXiv:1905.03779 | [src: abstract] |
| PCA compression of the shear data vector in the same work | dimension reduced by a factor ~5 with most of the information kept | arXiv:1905.03779 | [src] |
| Parameter-dependent covariance in 3×2pt, survey under 1% of the sky | bias up to O(10%) of the statistical error | Kodwani et al. 2019, arXiv:1811.11584 | [src] |
| CMB: validity of the Hamimeche–Lewis approximation | ℓ ≳ 30 | Hamimeche & Lewis 2008, arXiv:0801.0554 | [src] |

## 2. Projection (prior-volume) effects — documented shifts
<!-- key: projection-prior-volume-effects-documented -->

Shifts are between the posterior mean and the best fit (maximum likelihood or MAP), in units of the posterior σ, as each paper states them.

| Data and model | Shift | Other numbers | Source | Flag |
|---|---|---|---|---|
| BOSS full shape, EFTofLSS, ΛCDM, "West-coast" prior (PyBird) | up to 1σ | PyBird and CLASS-PT results agree only at the 1σ level on the same data | Simon et al. 2023, arXiv:2208.05929 | [src] |
| Same, "East-coast" prior (CLASS-PT) | up to 2σ | best fits of the two priors consistent at ~1σ, ~0.5σ with doubled prior widths | arXiv:2208.05929 | [src] |
| BOSS (eBOSS) full shape, ΛCDM, profile against posterior | up to 1.0σ (1.6σ) | frequentist intervals wider by factors up to 1.9 (1.6); Planck constraints unchanged | Holm et al. 2023, arXiv:2309.04468 | [src: abstract] |
| DESI DR1 full shape + BAO, ΛCDM: σ8, H0, Ω_m | 0.8σ, 0.3σ, 0.7σ | frequentist: σ8 = 0.863 (+0.048/−0.040), H0 = 68.96 (+0.81/−0.80), Ω_m = 0.3034 ± 0.0110 | Morawetz et al. 2025, arXiv:2508.11811 | [src: abstract] |
| DESI DR1 full shape + BAO, w0waCDM: σ8, H0, Ω_m, w0, wa | 2.1σ, 4.1σ, 6.5σ, 6.3σ, 6.6σ | frequentist: σ8 = 0.782 (+0.060/−0.036), H0 = 63.7 (+4.2/−2.0), Ω_m = 0.378 (+0.024/−0.047), w0 = −0.16 (+0.10/−0.50), wa = −3.0 (+1.7, lower bound not given) | arXiv:2508.11811 | [src: abstract] |
| DESI DR1 full shape, w0waCDM, with supernovae | intervals no longer significantly shifted | qualitative | arXiv:2508.11811 | [src] |
| DESI DR1 full shape + BBN + n_s, baseline priors | "multi-σ" in H0, w0, wa | Jeffreys prior brings the MAP inside the 68% region | Bonici et al. 2026, arXiv:2607.02498 | [src] |
| Stage-IV synthetic clustering, w0waCDM, Mpc/h against Mpc priors | from "several standard deviations" to "well within 1σ" | mock data | Pezzotta et al. 2026, arXiv:2610.08751 | [src] |
| DES Y3 + KiDS-1000 cosmic shear, ΛCDM, S8 | mean 0.790 (+0.018/−0.014) against MAP 0.801 | 1.7σ from Planck | DES & KiDS 2023, arXiv:2305.17173 | [src: abstract] |
| BOSS full shape, wCDM, CMB-free | w = −1.17 (+0.12/−0.11); nuisance priors "informative", broadening them shifts the contours | — | Carrilho et al. 2023, arXiv:2207.14784 | [src: abstract] |
| LSS only (BOSS DR12 full shape + BAO + DES Y3 3×2pt), w0waCDM, reparameterised | w0 = −0.72 ± 0.21, wa = −0.91 (+0.78/−0.64) | MAP inside the marginal interval | Tsedrik et al. 2025, arXiv:2509.09562 | [src: abstract] |

DES Y6 3×2pt measured its own projection effects with a noiseless data vector at the MAP, analysed with the data pipeline and covariance (arXiv:2601.14559, appendix on prior-volume effects) [src]. Pulls are (truth − mean)/σ.

| Parameter | 3×2pt ΛCDM | 2×2pt | Shear, TATT | Shear, NLA | 3×2pt non-linear bias | 3×2pt wCDM | 3×2pt wCDM, non-linear bias |
|---|---|---|---|---|---|---|---|
| S8 | +0.17 | +0.23 | +0.10 | −0.07 | +0.50 | +0.43 | +0.83 |
| Ω_m | −0.32 | −0.37 | −0.14 | −0.31 | −0.64 | −0.05 | −0.15 |
| σ8 | +0.26 | +0.33 | +0.06 | +0.17 | +0.65 | +0.22 | +0.54 |
| w | — | — | — | — | — | +0.40 | +0.63 |

With an earlier synthetic data vector the same test gave shifts above 0.5σ in all parameters of interest, "often exceeding 1σ", to the point that `ΔS8` could no longer be used as a scale-cut validation metric for 2×2pt and 3×2pt; stricter scale cuts sometimes increased the shifts, because less data means more projection [src].

The DESI w0waCDM line is the largest documented projection effect in a collaboration analysis: 6.6σ in `wa` between the maximum likelihood and the posterior mean of the same data. It agrees with the figure quoted in `cosmo-galaxy-clustering`.

Cost of the mitigations: 320 000 mock catalogues from 10 000 HOD parameter sets on 32 boxes for the HOD-informed prior (Zhang et al. 2024, arXiv:2409.12937) [src]; 10 500 HOD mocks for the simulation-based prior of Ivanov et al. 2024 (arXiv:2402.13310), which shrinks the bias-parameter posterior volume by an order of magnitude and improves single-field f_NL constraints by about 40% [src]; analytic marginalisation cuts sampling time by a factor 3–10 (Hadzhiyska et al. 2023, arXiv:2301.11895) [src].

## 3. Profile likelihood against posterior on the same data
<!-- key: profile-likelihood-against-posterior-on-the -->

| Parameter, data, model | Frequentist | Bayesian | Source | Flag |
|---|---|---|---|---|
| ΛCDM parameters, Planck 2013 | profile likelihood with Minuit | "excellent" agreement | Planck intermediate XVI, arXiv:1311.1657 | [src] |
| Σm_ν, Planck 2013 CMB + lensing + BAO | < 0.26 eV (95% CL) | "very similar" with Feldman–Cousins | arXiv:1311.1657 | [src] |
| Σm_ν, Planck 2018 + ACT lensing + DESI (2024), ΛCDM | profile limits agree with the posterior at the ~10% level | < 0.072 eV (95%) | Naredo-Tuero et al. 2024, arXiv:2407.13831 | [src] |
| Σm_ν, same with HiLLiPoP and without the DESI z = 0.7 bin | — | < 0.11 eV (95%) | arXiv:2407.13831 | [src: abstract] |
| Σm_ν, DESI DR2 BAO + CMB, ΛCDM | < 0.053 eV (95%, Feldman–Cousins) | < 0.0642 eV (95%), marginalised σ = 0.020 eV | Elbers et al. 2025, arXiv:2503.14744 | [src: abstract] |
| Early dark energy fraction, Planck + BOSS full shape | f_EDE = 0.072 ± 0.036 (68% CL) | MCMC limits affected by volume effects (values not transcribed here) | Herold et al. 2022, arXiv:2112.12140 | [src: abstract] |
| Early dark energy, Planck + BOSS | f_EDE = 0.087 ± 0.037, H0 = 70.57 ± 1.36 km/s/Mpc; H0 within 1.7σ of SH0ES for all data sets tried | — | Herold & Ferreira 2023, arXiv:2210.16296 | [src: abstract] |
| Tensor-to-scalar ratio, Planck PR4 + BK18 + lensing + BAO | r < 0.037 (95% CL) | r < 0.038 (flat prior on r) | Campeti & Komatsu 2022, arXiv:2205.05617 | [src: abstract] |
| Dark matter–proton scattering, Planck 2018 | prior-independent limits | "the Bayesian method consistently overestimates the constraints on the cross section" | Straight et al. 2026, arXiv:2603.25731 | [src] |
| Wilks, likelihood integration and Feldman–Cousins on non-Gaussian chains | agree within 10% near the Gaussian regime | — | Barua et al. 2025, arXiv:2508.10633 | [src] |

Pattern: where the model is well constrained and no boundary is involved (ΛCDM, r with a flat prior), the two frameworks agree to a few per cent. They separate in three situations: a boundary (Σm_ν), a parameter that switches off a sector (f_EDE, an interaction cross-section), and many weakly constrained nuisance parameters (EFT full shape, §2).

## 4. Model comparison — evidence against delta chi2 on the same data
<!-- key: model-comparison-evidence-against-delta-chi2-on -->

### 4.1 DESI DR2: Δχ², significance and ΔDIC for w0waCDM against ΛCDM
<!-- key: desi-dr2-chi2-significance-and-dic-for-w0wacdm -->

The Δχ² table of §7.1 of DESI Collaboration 2025 (arXiv:2503.14738), transcribed [src]. `Δχ²_MAP` is w0waCDM minus ΛCDM; the significance assumes 2 extra parameters; `Δ(DIC) = DIC_w0wa − DIC_ΛCDM`. The supernova rows use the compilations as they stood in March 2025 and are superseded for the supernova samples (see `cosmo-supernovae` and `cosmo-dark-energy-modified-gravity`); they are kept here because they are the reference case for the statistics.

| Data | Δχ²_MAP | Significance | Δ(DIC) |
|---|---|---|---|
| DESI | −4.7 | 1.7σ | −0.8 |
| DESI + (θ*, ω_b, ω_bc) from CMB | −8.0 | 2.4σ | −4.4 |
| DESI + CMB (no lensing) | −9.7 | 2.7σ | −5.9 |
| DESI + CMB | −12.5 | 3.1σ | −8.7 |
| DESI + Pantheon+ | −4.9 | 1.7σ | −0.7 |
| DESI + Union3 | −10.1 | 2.7σ | −6.0 |
| DESI + DESY5 | −13.6 | 3.3σ | −9.3 |
| DESI + DESY3 (3×2pt) | −7.3 | 2.2σ | −2.8 |
| DESI + DESY3 (3×2pt) + DESY5 | −13.8 | 3.3σ | −9.1 |
| DESI + CMB + Pantheon+ | −10.7 | 2.8σ | −6.8 |
| DESI + CMB + Union3 | −17.4 | 3.8σ | −13.5 |
| DESI + CMB + DESY5 | −21.0 | 4.2σ | −17.2 |

Checks `[der]`: every significance is reproduced by `p = exp(−abs(Δχ²)/2)` and the two-sided Gaussian equivalent. `Δ(DIC) − Δχ²_MAP` lies between 3.6 and 4.7 in every row, that is about twice the two extra parameters, as expected when both are constrained by the data.

### 4.2 The same data under the Bayesian evidence
<!-- key: the-same-data-under-the-bayesian-evidence -->

| Data, w0waCDM against ΛCDM | Δχ² route | Evidence route | Source | Flag |
|---|---|---|---|---|
| DESI DR2 BAO + Planck CMB | 3.1σ | `ln B = −0.57 ± 0.26`, modestly favouring ΛCDM | Ong, Yallup & Handley 2025, arXiv:2511.10631 | [src] |
| + DES-SN5YR (original calibration) | 4.2σ | `ln B = +3.32 ± 0.27`, quoted as 3.07 ± 0.10σ | arXiv:2511.10631; arXiv:2603.05472 | [src] |
| + DES-Dovekie (recalibrated) | (see `cosmo-dark-energy-modified-gravity`) | `ln B = −0.30 ± 0.19` | arXiv:2511.10631 | [src] |
| + Pantheon+ | 2.8σ | `ln B = −0.66 ± 0.44` | DESI extended dark-energy paper, Lodha et al. 2025, arXiv:2503.14743 | [sec: `cosmo-dark-energy-modified-gravity` SKILL.md; the abstract of arXiv:2503.14743 does not give it] |
| Out-of-sample score, DESI DR2 BAO + CMB + supernovae | — | "modest preferences" for w0waCDM in ΔELPD, supplied entirely by one BAO block, LRG2 at z = 0.706; all supernova samples consistent with zero | Karim et al. 2026, arXiv:2609.04334 | [src: abstract] |

Where the Bayesian preference comes from, according to arXiv:2511.10631 [src: Sect. III]: a 2.95 ± 0.04σ tension between DESI DR2 and DES-SN5YR within ΛCDM, reduced to 1.96 ± 0.04σ with DES-Dovekie. The extended model is preferred "precisely because its additional parameters act to resolve this specific dataset conflict".

The lesson for a referee: for DESI + CMB the three in-sample statistics read 3.1σ, `Δ(DIC) = −8.7` ("strong" on DESI's own scale) and `ln B = −0.57` (mildly against). None of them is an error; they answer different questions with different treatment of the prior volume of `w0`, `wa`.

## 5. Tension metrics on the same data
<!-- key: tension-metrics-on-the-same-data -->

| Comparison, model | Metric | Value | Source | Flag |
|---|---|---|---|---|
| DES Y1 3×2pt against Planck, ΛCDM | parameter differences, eigentension, suspiciousness (mutually similar) | ~2.3σ | Lemos et al. 2021, arXiv:2012.09554 | [src] |
| Same | Bayes ratio | "inconsistent with the rest due to its dependence on the prior volume" | arXiv:2012.09554 | [src] |
| Same | Bayes ratio with narrower priors | drops below unity; "DES and Planck are, in a Bayesian sense, incompatible under ΛCDM" | Handley & Lemos 2019, arXiv:1902.04029 | [src] |
| Planck against SH0ES, DES Y1, SDSS BAO | suspiciousness | strong, moderate, no tension | arXiv:1902.04029 | [src] |
| Simulated DES Y1 against Planck, Ω_m shifted by 1.5 marginal σ (a-priori 2.3σ), ΛCDM | Bayes ratio; eigentension; GoF loss; parameter difference (MCMC/update); suspiciousness | `log R = −0.4 ± 0.6` ("no evidence"); 3.3σ; 3.0σ; 2.8σ/2.7σ; 2.9 ± 0.4σ | Lemos et al. 2021, arXiv:2012.09554 | [src: Table 3] |
| Same, Ω_m shifted by 2 marginal σ (a-priori 3.8σ) | same order | `log R = −4.8 ± 0.6`; 4.1σ; 3.9σ; 3.4σ/3.6σ; 4.1 ± 0.6σ | arXiv:2012.09554 | [src: Table 3] |
| Toy case: two equal Gaussians 3σ apart | Bayes ratio, flat prior [−10, 10] against [−200, 200] | `R << 1` against `R > 1` | arXiv:2012.09554, figure 4 | [src] |
| DES Y6 3×2pt against Planck 2018 + ACT DR6 + SPT-3G DR1, ΛCDM | full-space parameter difference | 1.8σ | DES Collaboration 2026, arXiv:2601.14559 | [src] |
| Same | projected on S8 | 2.6σ | arXiv:2601.14559 | [src] |
| All DES probes (3×2pt, SNe, BAO, clusters) against CMB | parameter difference | 2.8σ | arXiv:2601.14559 | [src] |
| DES 3×2pt + DESI DR2 BAO + DES SNe + SPT clusters against CMB | parameter difference | 2.3σ | arXiv:2601.14559 | [src] |
| LSS combinations against Planck 2015 + Pol + BAO | method of Battye, Charnock & Moss | 2.55σ for the most discrepant LSS combination, 0.76σ for the most concordant | Charnock, Battye & Moss 2017, arXiv:1703.05959 | [src: abstract] |
| DES Y3 + KiDS-1000 shear against Planck | as quoted | 1.7σ | arXiv:2305.17173 | [src] |
| DESI DR2 against DES-SN5YR, ΛCDM | five metrics, combined statement | 2.95 ± 0.04σ; 1.96 ± 0.04σ with DES-Dovekie | Ong et al. 2025, arXiv:2511.10631 | [src: Sect. III] |
| DES Y1 internal consistency | posterior predictive p-value | 0.046; 0.10 after removing about 1.5% of the data vector | Doux et al. 2021, arXiv:2011.03410 | [src: abstract] |
| Accuracy of non-Gaussian parameter-shift estimators | benchmark | within 0.2σ generally, 0.5σ in difficult cases | Raveri & Doux 2021, arXiv:2105.03324 | [src: abstract] |
| KiDS-Legacy cosmic shear against Planck | Hellinger distance: 0.73σ in Σ8 (the abstract's figure), 0.76σ in S8 [src: Sect. 7] | 0.73σ / 0.76σ | Wright et al. 2025, arXiv:2503.19441 | [src] |
| CMB against DESI DR2 BAO, ΛCDM | as quoted by each collaboration | 1.6σ (P-ACT), 2.8σ (SPT-3G + ACT + Planck, Ω_m–h r_d plane) | arXiv:2503.14452, arXiv:2506.20707 | [src] |

Two readings of the table. First, the DES Y6 pair (1.8σ and 2.6σ on the same posteriors) shows that projecting on the best-measured combination raises the figure; the full-space number is the one that accounts for the look at several parameters. Second, the quoted lensing tensions do not share a reference: KiDS compares with Planck alone, DES Y6 with a three-experiment CMB combination (noted in `cosmo-weak-lensing`).

## 6. Samplers — documented accuracy and cost
<!-- key: samplers-documented-accuracy-and-cost -->

| Statement | Value | Source | Flag |
|---|---|---|---|
| MultiNest against PolyChord on the DES Y1 likelihood | inconsistent evidence estimates and "somewhat narrower" credible intervals from MultiNest | Lemos et al. 2023, arXiv:2202.08233 | [src] |
| PolyChord against Metropolis–Hastings, same likelihood | good agreement | arXiv:2202.08233 | [src] |
| DESI DR2 convergence criterion | Gelman–Rubin `R − 1 < 0.01` or effective sample size ≳ 10^3, whichever is longer | arXiv:2503.14738 | [src] |
| nautilus against emcee, dynesty, UltraNest, pocoMC | sampling efficiency higher, "often by more than an order of magnitude" | Lange 2023, arXiv:2306.16923 | [src] |
| GPU nested sampling, 39-dimensional shear analysis, ΛCDM against w0wa | Bayes factors in 2 days on one A100 GPU; a further factor 4 from interpolating the matter power spectrum | Lovick et al. 2025, arXiv:2509.13307 | [src] |
| Cobaya overhead per posterior evaluation | sub-millisecond | Torrado & Lewis 2021, arXiv:2005.05290 | [src] |
| Analytic marginalisation of calibratable nuisance parameters | sampling time reduced by a factor 3–10 | arXiv:2301.11895 | [src] |

## 7. Emulator error budgets
<!-- key: emulator-error-budgets -->

| Emulator | Quantity | Stated accuracy | Range | Source | Flag |
|---|---|---|---|---|---|
| CosmoPower | linear and non-linear matter power spectrum (Boltzmann-code output) | emulation error < 0.4% | k in [10^-5, 10] Mpc^-1, z in [0, 5] | Spurio Mancini et al. 2022, arXiv:2106.03846 | [src] |
| CosmoPower | CMB TT, TE, EE and lensing potential spectra | error ≲ 10% of the expected Simons Observatory shot noise | 5σ region around the Planck best fit | arXiv:2106.03846 | [src] |
| CosmoPower | speed-up of the full inference pipeline | up to O(10^4) | — | arXiv:2106.03846 | [src] |
| EuclidEmulator2 | non-linear correction to the matter power spectrum | 1% or better against high-resolution dark-matter-only simulations | 0.01 ≤ k ≤ 10 h/Mpc, z ≤ 3, w0waCDM + Σm_ν (8 parameters) | Euclid Collaboration 2021, arXiv:2010.11288 | [src] |
| EuclidEmulator2 | training set | over 250 simulations, 3000³ particles, 1 (Gpc/h)³, paired-and-fixed | — | arXiv:2010.11288 | [src: abstract] |

These are interpolation accuracies against the training-type calculation. They are not the accuracy of the prediction against the real Universe: a 1% dark-matter-only emulator says nothing about baryonic feedback at k of a few h/Mpc.

## 8. Simulation-based inference — coverage and validation outcomes
<!-- key: simulation-based-inference-coverage-and -->

| Analysis | Outcome | Source | Flag |
|---|---|---|---|
| Density-estimation likelihood-free inference, typical cosmological problems | high-fidelity posteriors with O(10^3) simulations or fewer | Alsing et al. 2019, arXiv:1903.00007 | [src] |
| Benchmark of neural posterior, ratio and likelihood estimation and approximate Bayesian computation | every algorithm "can yield overconfident posterior approximations"; ensembles are more reliable | Hermans et al. 2022, arXiv:2110.06581 | [src] |
| Gaussian linear model, neural posterior and likelihood estimation with normalising flows | posterior variance inflated by at least the Dodelson–Schneider amount for the same number of simulations; the true contour is recovered "given enough simulations" | Homer et al. 2024, arXiv:2412.02311 | [src] |
| KiDS-1000 cosmic shear pseudo-C_ℓ, 18 000 realisations, ΛCDM | S8 = 0.731 ± 0.033; probability-to-exceed 0.42; learnt likelihood approximately Gaussian at fixed cosmology; constraints wider than with a Gaussian likelihood because of the cosmology dependence of the covariance | von Wietersheim-Kramsta et al. 2024, arXiv:2404.15402 | [src] |
| Same: neglecting variable depth and PSF anisotropy in the forward model | S8 overestimated by ~5% | arXiv:2404.15402 | [src] |
| f_NL from halo fields, 1000 realisations, ratio estimation against likelihood-based inference | means and skewness agree; variance agrees on average only; kurtosis differs; for P + B the learned posteriors are "often underconfident ... despite passing coverage tests" | Alokda et al. 2026, arXiv:2605.00980 | [src: abstract] |
| Euclid-like Gaussian shear mocks, explicit Gaussian likelihood against learned likelihood, TARP | the explicit likelihood is "strongly miscalibrated under emulation inaccuracies or likelihood non-Gaussianity"; constraints differ by up to a factor of two from the map-level network with the explicit likelihood, about 30% with the learned one | Vinciguerra et al. 2026, arXiv:2607.17942 | [src] |
| Beyond-2pt mock challenge | tests the bias of the mean on HOD mocks; states that it does not validate error bars | [sec: `cosmo-beyond-two-point` SKILL.md] | [sec] |

The KiDS-SBI value of S8 belongs to the KiDS-1000 data and calibration, superseded by KiDS-Legacy (see `cosmo-weak-lensing`); it is quoted here for the method.

## 9. Fisher forecasts against full posteriors
<!-- key: fisher-forecasts-against-full-posteriors -->

| Case | Fisher against sampled posterior | Source | Flag |
|---|---|---|---|
| Purely geometrical probes (supernovae, BAO), `w0`–`wa`, Stage-III and Stage-IV | Fisher underestimates marginalised errors by 30%–70% | Wolz et al. 2012, arXiv:1205.3984 | [src] |
| Probes including structure growth (weak lensing), same study | contours agree; errors change at the 5% level | arXiv:1205.3984 | [src] |
| Euclid, cross-correlations between probes (forecast) | may increase the dark-energy figure of merit "by at least a factor of three" | Euclid Collaboration 2020, arXiv:1910.09273 | [src], forecast |
| Compression: MOPED with parameter-dependent noise | errors increase "by a very modest factor" | Heavens et al. 2000, arXiv:astro-ph/9911102 | [src] |

The first line is the relevant one for w0wa from BAO and supernovae: the posterior is strongly non-elliptical along the `w0`–`wa` degeneracy, so a Fisher forecast of the figure of merit for geometrical probes alone is optimistic by a large factor.

## 10. Blinding — documented outcomes
<!-- key: blinding-documented-outcomes -->

| Statement | Value | Source | Flag |
|---|---|---|---|
| DESI DR1 catalogue blinding: change of analysis choices between blinded and unblinded data | none needed for BAO and RSD | Andrade et al. 2024, arXiv:2404.07282 | [src] |
| DESI Lyα Alcock–Paczynski blinding: size of the hidden shift | BAO peak moved as for a change of about 5% in matter content, posterior shapes unchanged | Perez-Sanchez et al. 2026, arXiv:2607.07875 | [src] |
| DES data-vector blinding: effect on internal consistency | no significant degradation of `χ²` between data and best-fit model on simulated DES Y3 data; `χ²` is conserved more precisely as experiments become more precise | Muir et al. 2020, arXiv:1911.05929 | [src] |
| Covariance blinding on KiDS-450 | the cosmic-shear tension with Planck "could easily be induced by a mischaracterization of correlations between ξ− at the highest redshift and all lower redshifts" (an illustration, with no direct evidence that the KiDS-450 covariance is biased) | Sellentin 2020, arXiv:1910.08533 | [src] |

## 11. Look-elsewhere corrections — documented cases
<!-- key: look-elsewhere-corrections-documented-cases -->

No collaboration analysis found in this session quotes a trial-factor-corrected global significance for a headline cosmological result. The documented cases are of the complementary kind: a local significance that changed when the analysis freedom was removed or the null was simulated.

| Case | Local figure | After calibration or change of choice | Source | Flag |
|---|---|---|---|---|
| w0wa preference with DESI DR2 + CMB, by supernova compilation | 2.8σ, 3.8σ, 4.2σ | three values from one BAO + CMB data set; the spread is an analysis-choice effect | arXiv:2503.14738 | [src: Sect. VII] |
| Same preference, out-of-sample, by redshift block | — | supplied by a single BAO block (LRG2, z = 0.706) | arXiv:2609.04334 | [src: abstract] |
| LSS against Planck, choice of LSS combination | 2.55σ (most discrepant) | 0.76σ (most concordant) | arXiv:1703.05959 | [src: abstract] |
| DES Y6 against CMB, choice of projection | 2.6σ in S8 | 1.8σ in the full space | arXiv:2601.14559 | [src: abstract] |
| Parity-odd four-point function | 7.1σ against one mock suite | 1.4σ with N-body mocks | [sec: `cosmo-beyond-two-point` SKILL.md] | [sec] |
| Phantom crossing within CPL | "preferred" | 3.2% of non-crossing mocks imitate it | [sec: `cosmo-dark-energy-modified-gravity` SKILL.md] | [sec] |

## 12. History of the key numbers
<!-- key: history-of-the-key-numbers -->

### 12.1 Covariance corrections
<!-- key: covariance-corrections -->

| Year | Step | What it superseded | Source |
|---|---|---|---|
| 2007 | unbiased precision matrix (Hartlap factor) | the plain inverse of the sample covariance | arXiv:astro-ph/0608064 |
| 2013 | noise of the precision matrix propagates to parameter scatter, `1 + B (n_d − n_θ)`; requirements on the number of mocks | the Hartlap factor used alone | arXiv:1304.2593, arXiv:1212.4359 |
| 2014 | `m_1` rescaling of the parameter covariance read from the likelihood | separate, inconsistent corrections | arXiv:1312.4841 |
| 2016 | marginalisation over the true covariance: multivariate t-distribution | Gaussian likelihood with a debiased precision | arXiv:1511.05969 |
| 2022 | frequentist-matching prior; `S'` as the Gaussian approximation | the independence-Jeffreys prior of 2016, which omits the best-fit scatter | arXiv:2108.10402 |
| 2024 | the same inflation exists in simulation-based inference | the belief that learned likelihoods escape it | arXiv:2412.02311 |
| 2026 | rotational-invariant and non-linear shrinkage estimators tested for clustering | — (not yet adopted by a survey analysis read here) | arXiv:2604.13851 |

A text that says "we apply the Hartlap correction" and nothing else is using the 2007 state of the art.

### 12.2 Significance of evolving dark energy, by statistic
<!-- key: significance-of-evolving-dark-energy-by -->

| Date | Data | Statistic | Value | Source |
|---|---|---|---|---|
| March 2025 | DESI DR2 BAO + CMB | `Δχ²_MAP`, 2 dof | 3.1σ | arXiv:2503.14738 |
| March 2025 | + Pantheon+ / Union3 / DESY5 | same | 2.8σ / 3.8σ / 4.2σ | arXiv:2503.14738 |
| November 2025 | DESI DR2 BAO + Planck | Bayes factor | `ln B = −0.57 ± 0.26` | arXiv:2511.10631 |
| November 2025 | + DES-SN5YR / DES-Dovekie | Bayes factor | `+3.32 ± 0.27` / `−0.30 ± 0.19` | arXiv:2511.10631 |
| September 2026 | DESI DR2 BAO + CMB + supernovae | out-of-sample ΔELPD | modest, from one BAO block | arXiv:2609.04334 |

The later frequentist values with recalibrated supernovae are in `cosmo-dark-energy-modified-gravity`; this table tracks the statistic, not the data.

### 12.3 Lensing against the CMB, by metric
<!-- key: lensing-against-the-cmb-by-metric -->

| Date | Comparison | Value | Metric | Source |
|---|---|---|---|---|
| 2017 | LSS against Planck 2015 | 0.76σ to 2.55σ | depends on the LSS combination | arXiv:1703.05959 |
| 2020 | DES Y1 3×2pt against Planck | ~2.3σ | parameter differences, suspiciousness, eigentension | arXiv:2012.09554 |
| 2023 | DES Y3 + KiDS-1000 shear against Planck | 1.7σ | as quoted | arXiv:2305.17173 |
| 2024 | KiDS-1000 SBI against CMB | 2.9σ | as quoted | arXiv:2404.15402 |
| 2025 | KiDS-Legacy against Planck | 0.73σ (Σ8), 0.76σ (S8) | Hellinger distance, Sect. 7 | arXiv:2503.19441 |
| 2026 | DES Y6 3×2pt against Planck + ACT + SPT | 1.8σ full space, 2.6σ in S8 | parameter difference, normalising flows | arXiv:2601.14559 |

The entries are not comparable with each other without the metric and the CMB reference; the S8 values behind them are in `cosmo-weak-lensing`.

### 12.4 CMB against DESI DR2 BAO in ΛCDM: three published figures
<!-- key: cmb-against-desi-dr2-bao-in-lambdacdm-three -->

| Quoted by | CMB data | Value | Space | Source | Flag |
|---|---|---|---|---|---|
| ACT | P-ACT | 1.6σ | Ω_m–h r_d plane, Gaussian separation in 2D | arXiv:2503.14452 | [src: App. H] |
| SPT | SPT-3G + ACT DR6 + Planck | 2.8σ | Ω_m–h r_d plane | arXiv:2506.20707 | [src] |
| DESI | CMB as defined in the DESI paper | 2.3σ | — | [sec: `cosmo-galaxy-clustering` SKILL.md, citing arXiv:2503.14738] | [sec] |

Three numbers for what a text would call "the CMB–BAO tension". The ACT and SPT figures are computed in the same Ω_m–h r_d plane and differ by CMB combination (ACT-L alone against DESI DR2 is 2.8σ, arXiv:2503.14452 [src: App. H]); the space behind the DESI figure was not read.

## Not verified
<!-- key: not-verified -->

- The constant `A` of the Percival 2014 `m_1` factor was not transcribed (it is defined in the paper's eq. AB); the table of §1.1 uses the exact 2022 expression instead.
- The Bayesian (MCMC) limits on the early-dark-energy fraction that the profile-likelihood papers argue against were not read; only the frequentist values are quoted.
- `ln B = −0.66 ± 0.44` for DESI DR2 + CMB + Pantheon+ is taken from a sibling skill, not from the paper body.
- No quantified emulator error budget for a Lyα, HOD or baryonic-feedback emulator was collected here; see the probe skills.
- No trial-factor-corrected global significance for a cosmological anomaly was found; §11 lists spreads between analysis choices instead.
- The number of simulations needed for simulation-based inference as a function of summary dimension (beyond the statements of arXiv:1903.00007 and arXiv:2412.02311) was not quantified.
- DESI DR1 full shape uses 1000 EZmocks with Hartlap and Percival 2014 factors (§1.2); the data-vector length per tracer and the DR2 practice were not read, so §1.1 gives generic cases.
