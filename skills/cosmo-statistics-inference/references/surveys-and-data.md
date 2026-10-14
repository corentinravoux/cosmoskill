# Statistics and inference — how each collaboration does it

Scope: the statistical practice (likelihood, covariance, blinding, sampler, point estimate, tension metric, model comparison) of the major collaborations in their latest analyses, with citations. The measurements themselves are in the probe skills.
Snapshot: 2026-10-14

Flags: `[src]` read this session in the cited paper; `[sec]` taken from a named secondary source; `[der]` derived here, derivation stated. Unless a row says otherwise, every entry of §1 is `[src]` from the paper named in its last column.

## 1. Summary table
<!-- key: summary-table -->

| Analysis | Likelihood and covariance | Blinding | Sampler and convergence | Point estimate quoted | Tension metric | Model comparison | Source |
|---|---|---|---|---|---|---|---|
| DESI DR2 BAO cosmology (2025) | BAO distances with their covariance; for DR1, RascalC analytic covariance for BAO and corrected EZmock covariance for full shape (arXiv:2411.12027) | catalogue-level redshift shifts, same prescription as DR1 with a new random seed; unblinded December 2024 | Metropolis–Hastings in Cobaya with CAMB; `R − 1 < 0.01` or effective sample size ≳ 10^3 | mean ± σ, or 68% minimal credible interval if asymmetric; limits at 68% except Σm_ν at 95%; best fit with `iminuit` | not read at source here (see `cosmo-galaxy-clustering` for the values) | `Δχ²_MAP` converted to σ with 2 degrees of freedom; `Δ(DIC)` | arXiv:2503.14738 |
| DESI DR1 full shape, frequentist companion (2025) | same data and likelihood as the Bayesian analysis | as DR1 | "standard profile likelihood method" | maximum likelihood with 1σ confidence intervals | shifts against the posterior mean | — | arXiv:2508.11811 |
| DESI DR2 neutrinos (2025) | BAO + CMB | as DR2 | as DR2 | Bayesian 95% limit, Feldman–Cousins 95% limit, effective mass allowed negative | tension with oscillation lower limits by frequentist and Bayesian methods | — | arXiv:2503.14744 |
| DES Y6 3×2pt (2026) | Gaussian; analytic CosmoCov covariance with Gaussian and non-Gaussian terms, recomputed at the blind MAP cosmology | three levels: shear catalogue, data vector, cosmology | Nautilus, 10 000 live points, 16 networks; MAP by Powell optimiser from the 20 best samples | marginal posterior; MAP and projected joint highest posterior density (PJ-HPD) shown to flag volume effects | parameter-difference probability with normalising flows (`tensiometer`), `n_σ = sqrt(2) erf^-1(Δ)`; data sets combined only if `n_σ < 3` | for wCDM: posterior of `w`, and `Δχ²` likelihood-ratio test with 1 degree of freedom | arXiv:2601.14559 |
| DES Y3 3×2pt (2021–2023) | Gaussian; analytic halo-model covariance (arXiv:2012.08568) | data-vector transformation (arXiv:1911.05929) | PolyChord, after the comparison of arXiv:2202.08233 | — | suite of arXiv:2012.09554; posterior predictive tests (arXiv:2011.03410) | — | papers cited in the row |
| KiDS-Legacy cosmic shear (2025) | Gaussian; analytic OneCovariance (Gaussian, non-Gaussian, super-sample, shear-calibration terms), tested against GLASS mocks | three shape catalogues, one true, the others shifted by up to ±2σ in S8 | Nautilus inside CosmoSIS; MAP by adaptive Nelder–Mead | three in parallel: marginal mean ± σ; marginal mode + highest posterior density interval (headline); MAP + PJ-HPD | 0.73σ against Planck (metric not read at source here) | — | arXiv:2503.19441 |
| KiDS-1000 SBI (2024) | learned likelihood, 18 000 forward simulations | — | sequential neural likelihood estimation | marginal mean | — | — | arXiv:2404.15402 |
| ACT DR6 power spectra (2025) | multi-frequency likelihood and a foreground-marginalised CMB-only likelihood; analytic pseudo-spectrum covariance with a Monte Carlo correction from 1640 simulations, plus beam, leakage-beam and non-Gaussian lensing terms | two phases, with pre-registered criteria and dated unblinding | Cobaya MCMC, `R − 1 < 0.01` | marginal posterior | ΛCDM parameters of P-ACT and DESI DR2 agree at 1.6σ | — | arXiv:2503.14452 |
| SPT-3G D1 T/TE/EE (2025) | not read at source here | maps and spectra "validated through blind and unblind tests" | not read at source here | marginal posterior | 2.8σ between CMB (SPT + ACT + Planck) and DESI DR2 BAO in ΛCDM, in the Ω_m–h r_d plane | "CMB data alone show no evidence for physics beyond ΛCDM" | arXiv:2506.20707 |
| Planck 2013 frequentist cross-check | Planck 2013 likelihood | — | Minuit minimiser | profile-likelihood intervals; Feldman–Cousins for Σm_ν | — | — | arXiv:1311.1657 |
| Euclid preparation (forecast) | Fisher matrix, validated between independent codes | — | — | forecast | — | figure of merit | arXiv:1910.09273 |

## 2. DESI
<!-- key: desi -->

**Inference** (arXiv:2503.14738, §5) [src]. Cobaya with Metropolis–Hastings sampling and CAMB. BAO-only fits sample Ω_m and `h r_d`; with a BBN prior, H0 and ω_b; with the full CMB likelihood, the six base parameters with `θ_MC`. Convergence: Gelman–Rubin `R − 1 < 0.01`, or an effective sample size of ≳ 10^3, whichever takes longer. Summaries with `getdist`. The best fit and its χ² come from `iminuit` started at the MAP of each chain. For combinations with the DES Y3 3×2pt likelihood, the best fit uses the CosmoSIS implementation and the chains are combined as weighted `CombineHarvesterFlow` chains.

**Model comparison** [src]. `Δχ²_MAP` between the MAP points of the two models, including non-uniform priors; frequentist significance for two extra parameters; `Δ(DIC)` with the rule of thumb −5 strong, −10 decisive. Table in `results.md` §4.1. DESI states that for BAO alone the w0wa posteriors "are cut off by the priors, so the marginalized means and limits ... are prior-dependent", and that with the compressed CMB prior the posterior "is still bounded by the `wa > −3` prior".

**Blinding** [src]. Catalogue level, "using the same prescription as was applied to DR1" (Andrade et al. 2024, arXiv:2404.07282, built on Brieden et al. 2020, arXiv:2006.10857) "but with a new random seed"; validation tests on blinded catalogues; "once these tests were passed and the pipeline frozen, the blinding was removed" in December 2024. A Lyα-specific Alcock–Paczynski blinding was published in 2026 (arXiv:2607.07875).

**Covariance** (DESI 2024, arXiv:2411.12027) [src]. The analytic configuration-space covariance (RascalC, arXiv:1904.11070) is the fiducial choice for BAO because it adapts to the measured clustering; the analytic Fourier-space covariance failed the comparison for full shape, "which motivates the use of a corrected mock covariance" from EZmocks. The DR1 full-shape paper gives it: every element of the 1000-EZmock covariance is rescaled by a tracer-dependent factor calibrated on the data-tuned RascalC matrix, then the Hartlap and Percival 2014 factors are applied (arXiv:2411.12021) [src: Sects. 5.7–5.8]. For joint full shape and post-reconstruction BAO, an analytic cross-covariance was validated in 2026 (arXiv:2602.12343).

**Frequentist companions.** A profile-likelihood analysis of DR1 full shape (arXiv:2508.11811), a Feldman–Cousins limit and an effective-mass analysis for neutrinos (arXiv:2503.14744), and a reparameterisation and Jeffreys-prior reanalysis (arXiv:2607.02498). DESI is the collaboration that has gone furthest in publishing both statistical frameworks on the same data.

**External Bayesian reanalyses.** Evidence and tension grid with PolyChord (arXiv:2511.10631, arXiv:2603.05472); out-of-sample scoring (arXiv:2609.04334).

## 3. DES
<!-- key: des -->

**Year 6 3×2pt** (DES Collaboration 2026, arXiv:2601.14559, §4 and appendices) [src].

- Likelihood: Gaussian in the concatenated `w(θ)`, `γ_t(θ)`, `ξ±(θ)` vector, in CosmoSIS.
- Covariance: analytic, CosmoCov, Gaussian and non-Gaussian contributions, validated for Y3 (arXiv:2012.08568). The signal uses HMCode2020 while the covariance keeps Halofit, a mismatch of ≲ 2.5% in individual elements with negligible effect on errors. Point-mass terms and observing-condition weights are marginalised analytically by modifying the inverse covariance. The covariance is first computed at a fiducial cosmology and recomputed at the blind MAP before unblinding.
- Sampler: Nautilus (arXiv:2306.16923) with `n_live = 10 000` and 16 networks. This replaces the PolyChord of Y3 (arXiv:2202.08233).
- Combining probes: normalising-flow density estimates of each posterior (`tensiometer`), which allow independent probes to be combined without rerunning chains.
- Goodness of fit and internal consistency: posterior predictive distribution, compressed to `Δ_PPD`, with a pre-set threshold `Δ_PPD > 0.01` (method paper arXiv:2610.03447); χ² at the MAP defined as `−2 ln[L π_G]_max`, so that Gaussian priors count; effective number of parameters `N_eff = N_sampled − Tr(C_P C_π^-1)`.
- Point estimates: the MAP is found by a Powell optimiser started from the 20 highest-posterior samples; the PJ-HPD interval (from the KiDS-1000 methodology, arXiv:2007.01844) is shown next to the marginal to flag projection effects. "For our fiducial results, we only quote parameters that are not shifted significantly by prior-volume effects."
- Tension: parameter-difference probability (arXiv:1806.04649, arXiv:2105.03324), reported as an effective number of σ; `n_σ < 3` is the criterion for combining data sets. Headline numbers are full-parameter tensions; 1D or 2D values are quoted "when needed".
- Model comparison (wCDM): the size of `abs(−1 − w)` against `σ(w)`, and a `Δχ²` likelihood-ratio test with one degree of freedom.
- Blinding: three levels. Catalogue: ellipticities rescaled by a blind factor `0.9 < f < 1.1` until the catalogue null tests pass. Data vector: the transformation of arXiv:1911.05929; "we do not run chains on the blinded data vectors". Cosmology: chains run with parameter values hidden; `Δ_PPD` thresholds, `χ²/ν`, and nuisance posteriors against their priors are checked; the covariance is recomputed at the blind MAP; then the parameters are revealed.
- What happened at unblinding: "several PPD tests failed, and the posterior for one of the n(z) modes of lens bin 2 was pushing strongly against its prior"; the cause was not found, and all data involving lens bin 2 were dropped; "the decision-making process was outlined in advance by a detailed analysis plan, which prevented any post hoc decisions".
- Projection effects: a pre-agreed test with a noiseless data vector at the MAP, and a pre-agreed rule that parameters shifted by more than 1σ would not be highlighted (`results.md` §2).

**Year 3 and earlier.** The method papers remain the references: covariance (arXiv:2012.08568), sampler comparison (arXiv:2202.08233), blinding (arXiv:1911.05929), tension metrics (arXiv:2012.09554), posterior predictive tests (arXiv:2011.03410), non-Gaussian parameter shifts (arXiv:2105.03324). The joint DES Y3 + KiDS-1000 analysis documents what must be harmonised before two surveys are combined (arXiv:2305.17173).

## 4. KiDS
<!-- key: kids -->

**KiDS-Legacy cosmic shear** (Wright et al. 2025, arXiv:2503.19441) [src].

- Statistics: COSEBIs (fiducial) and band powers, over 2 to 300 arcmin; `ξ±` in an appendix.
- Likelihood: Gaussian. Theory `P(k)` from a CosmoPower emulator (arXiv:2106.03846) trained on CAMB and HMCode2020.
- Covariance: analytic, OneCovariance, `C = C_G + C_NG + C_SSC + C_mult`, the last term carrying the multiplicative shear-bias uncertainty; `C_G` split into sample-variance, shot-noise and mixed terms, the shot-noise term computed from the weighted pair counts and the survey variance from the mask. Agreement with GLASS mocks within 10% at large separations and below 5% under 0.5 degrees. An iterated covariance is one of the listed analysis variations.
- Sampler: Nautilus within CosmoSIS, chosen for "superior efficiency, robustness of uncertainties, and accurate evidence estimation".
- Point estimates, three reported side by side for the fiducial COSEBIs: marginal mean ± σ, 0.813 ± 0.018; marginal mode with highest posterior density interval, 0.815 (+0.016/−0.021), which is the headline; MAP with PJ-HPD, 0.811 (+0.022/−0.015). The MAP uses an adaptive Nelder–Mead algorithm.
- Goodness of fit: χ² = 127.8 for 120.5 effective degrees of freedom (probability to exceed 0.307) for COSEBIs, 151.0 for 162.5 (0.731) for band powers.
- Internal consistency: COSEBIs and band powers differ by 0.55σ in S8, attributed to a degeneracy direction with exponent 0.58 to 0.60 rather than 0.5; the paper therefore prefers `Σ8`. Translated posterior distributions are shown against the data vector. A companion paper holds the full suite of consistency tests.
- Blinding: three realisations of the shape catalogue, one true and two with induced shape differences giving up to ±2σ in S8, analysed in parallel until the manuscript had passed internal review; "only the discussion and conclusion sections [were] written after unblinding". The authors note that this scheme "effectively hampered the diagnosis of subtle systematic effects", because shape catalogues could not be compared directly with earlier ones without unblinding.
- Post-unblinding changes are listed in a dedicated appendix.

**KiDS-1000.** Methodology paper with the covariance validation against more than 20 000 mocks, the revised degrees of freedom and the MAP + PJ-HPD estimator (arXiv:2007.01844); covariance blinding scheme (arXiv:1910.08533); simulation-based reanalysis (arXiv:2404.15402).

## 5. HSC
<!-- key: hsc -->

The statistical practice of the HSC Year 3 analyses was not read at source in this session. The S8 values, the recalibration with DESI clustering redshifts and the blinding level are in `cosmo-weak-lensing`. Listed under "Not verified".

## 6. ACT
<!-- key: act -->

**DR6 power spectra and ΛCDM parameters** (Louis et al. 2025, arXiv:2503.14452) [src].

- Covariance, built from several terms: (1) analytic pseudo-spectrum covariance for noise and a Gaussian signal; (2) a Monte Carlo correction for inhomogeneous, stripy noise and for the ground-pickup filter, from an ensemble of 1640 simulations; (3) beam covariance from planet observations; (4) leakage-beam uncertainty from 10 000 simulated realisations; (5) non-Gaussian lensing terms, both the off-diagonal correlations induced by lensing modes and the lensing super-sample variance; further non-Gaussian foreground terms are listed in the paper (the list was truncated in the fetch). Leakage-beam uncertainty is a significant part of the TE error on large scales; the additional terms affect the EE error only mildly, reaching up to 15% at ℓ = 800; non-Gaussian tSZ and radio-source terms matter for TT at 90 GHz on small scales.
- Likelihoods: a multi-frequency likelihood with 15 foreground parameters (14 free) and 15 instrument parameters (6 calibrations with Gaussian priors, 4 polarisation efficiencies with flat priors in 0.9 to 1.1, 5 bandpass shifts with Gaussian priors), and a CMB-only likelihood. The default combination with Planck uses a multipole cut per data set instead of an ACT–Planck covariance.
- Sampling: Cobaya MCMC, theory to `ℓ_max = 9000`, `R − 1 < 0.01`, flat priors on the six ΛCDM parameters.
- Blinding in two phases. Phase 1: spectra may be plotted, but no parameters are fitted and no comparison with theory is made; polarisation spectra are not compared with Planck. Requirements before unblinding: analysis choices frozen; about 2000 null-test probabilities to exceed with a distribution consistent with expectation and no excess outside 1% to 99%. Unblinded 7 December 2023. Phase 2: comparison of TE and EE with Planck; recovery of ΛCDM and ΛCDM + N_eff parameters on Gaussian simulations to within 0.2σ; all products frozen. Unblinded 18 April 2024.
- Deviations from the plan are numbered and justified in the paper. The most instructive: a realistic non-Gaussian simulation initially gave 3σ shifts in some ΛCDM parameters because its foregrounds were more complex than the model; the team proceeded to unblind with a pre-stated rule (marginalise over an extra foreground parameter if a model extension moves cosmological parameters by more than 0.5σ), and recovered consistent parameters after unblinding with an additional tSZ shape parameter.
- Consistency statement: ΛCDM parameters agree between P-ACT and DESI DR2 at 1.6σ.

## 7. SPT
<!-- key: spt -->

**SPT-3G D1** (Camphuis et al. 2025, arXiv:2506.20707) [src, abstract and summary section]. The maps and power spectra "have been validated through blind and unblind tests". Quoted consistency statements: H0 from SPT-3G alone is 6.2σ from SH0ES; the three-experiment CMB combination differs from DESI DR2 BAO at 2.8σ in ΛCDM, in the Ω_m–h r_d plane; "CMB data alone show no evidence for physics beyond ΛCDM", while CMB + BAO gives 2–3σ shifts in curvature, lensing amplitude or the dark-energy equation of state. The likelihood, covariance and sampler sections of the paper were not accessible through the section tool and are listed under "Not verified".

## 8. Planck
<!-- key: planck -->

- Likelihood form: at high multipoles, approximations of the Hamimeche–Lewis type are valid for ℓ ≳ 30; below that, exact or simulation-based low-ℓ likelihoods are needed (arXiv:0801.0554) [src for the general statement]. The Planck 2018 and PR4 likelihood products (Plik, CamSpec, HiLLiPoP, SRoll2) are described in `cosmo-cmb`.
- Frequentist cross-check: Planck intermediate results XVI (arXiv:1311.1657) [src]: profile likelihoods with Minuit agree with the Bayesian results; Feldman–Cousins for the neutrino mass; frequentist limit Σm_ν < 0.26 eV (95% CL) from CMB + lensing + BAO in 2013.
- The Planck likelihood remains the test bed for statistical method papers: profile-likelihood validity (arXiv:2408.07700, with `Plik_lite`), emulator validation (arXiv:2106.03846), prior-volume effects in extended models (arXiv:2203.16285, arXiv:2603.25731).

## 9. Euclid preparation
<!-- key: euclid-preparation -->

No Euclid cosmological inference exists at the snapshot (see `cosmo-weak-lensing` and `cosmo-galaxy-clustering` for release dates). The statistical groundwork that was read here:

- Forecasts: Fisher matrices validated across independent implementations, with "optimistic" and "pessimistic" settings (Euclid Collaboration 2020, arXiv:1910.09273) [src]. These are forecasts.
- Non-linear theory: EuclidEmulator2, 1% to k = 10 h/Mpc for dark-matter-only (arXiv:2010.11288) [src].
- Covariance: the linear-construction method for cluster clustering, up to 20 times faster than a sample covariance (Lindholm et al. 2026, arXiv:2603.10735) [src]; rotational-invariant and non-linear shrinkage estimators benchmarked for clustering (arXiv:2604.13851).
- Likelihood form: a Gaussian pseudo-C_ℓ likelihood is sufficient for a Euclid-like 3×2pt analysis (arXiv:2012.06267) [src]; on Euclid-like shear mocks an explicit Gaussian likelihood on compressed correlation functions can be miscalibrated where a learned likelihood is not (arXiv:2607.17942) [src]. The second is not a Euclid Collaboration paper.
- Prior-volume effects in Stage-IV clustering: Mpc units and σ12 (arXiv:2610.08751) [src].

For Rubin LSST, the blinding tool is Smokescreen (arXiv:2604.18111) [src]; the inference framework is in `cosmo-software-ecosystem`.

## 10. Other analyses used as method references
<!-- key: other-analyses-used-as-method-references -->

| Analysis | Why it is cited | Source |
|---|---|---|
| BOSS DR9–DR11 | the covariance-error corrections were derived for it; 600 mocks gave about 20% extra error | arXiv:1312.4841 |
| BOSS full shape, two EFT pipelines | the reference case for prior dependence | arXiv:2208.05929, arXiv:2309.04468 |
| DES Y1 3×2pt | test bed for tension metrics, samplers and posterior predictive tests | arXiv:2012.09554, arXiv:2202.08233, arXiv:2011.03410 |
| CFHTLenS and KiDS-450 | non-Gaussian likelihood diagnostics; covariance blinding | arXiv:1707.04488, arXiv:1910.08533 |

## 11. Convergence of practice, as seen in the 2025–2026 papers
<!-- key: convergence-of-practice-as-seen-in-the-2025 -->

- Sampler: both Stage-III lensing collaborations moved to Nautilus for their final analyses (arXiv:2601.14559, arXiv:2503.19441); the CMB and BAO analyses use Metropolis–Hastings in Cobaya with `R − 1 < 0.01` (arXiv:2503.14738, arXiv:2503.14452).
- Covariance: analytic for lensing and 3×2pt (CosmoCov, OneCovariance), validated on mocks; analytic with Monte Carlo corrections for CMB spectra; semi-analytic for BAO; mock-based with corrections for full shape.
- Point estimates: lensing papers now report the MAP with a projected interval next to the marginal, and DES pre-registers which parameters may be highlighted given projection effects.
- Blinding: every analysis in §1 from 2025–2026 is blind at some level, and the two that give the most detail (DES Y6, ACT DR6) publish the pre-registered criteria and the deviations from them.
- Model comparison: `Δχ²` likelihood-ratio tests converted to σ are the collaboration standard (DESI with 2 degrees of freedom, DES with 1 for wCDM); evidences are computed mostly by external groups.

## 12. Priors side by side: DES Y6 3×2pt and KiDS-Legacy cosmic shear
<!-- key: priors-side-by-side-des-y6-3x2pt-and-kids -->

Both tables were read at source (arXiv:2601.14559, table of fiducial values and priors; arXiv:2503.19441, table of fiducial prior ranges) [src]. Brackets are flat priors.

| Quantity | DES Y6 3×2pt | KiDS-Legacy |
|---|---|---|
| Amplitude parameter sampled | `A_s × 10^9` in [0.5, 5] | S8 in [0.5, 1.0] |
| Matter density | Ω_m in [0.1, 0.6] | `Ω_c h²` in [0.051, 0.255] |
| Baryon density | Ω_b in [0.03, 0.07] | `Ω_b h²` in [0.019, 0.026] |
| h | [0.58, 0.8] | [0.64, 0.82] |
| n_s | [0.93, 1.00] | [0.84, 1.10] |
| Neutrino mass | free, m_ν in [0.06, 0.6] eV | fixed, Σm_ν = 0.06 eV |
| Dark energy | w in [−2, −1/3] when varied | w0 = −1, wa = 0 fixed |
| Baryonic feedback | `Θ_AGN = 7.7` fixed, with scale cuts set by a `Δχ²` threshold | `log10(T_AGN/K)` in [7.3, 8.3], marginalised |
| Intrinsic alignments | TATT: `A_1` in [−1, 3], `A_2` in [−3, 3], redshift indices with Gaussian priors | mass- and type-dependent NLA with a multivariate Gaussian prior informed by direct measurements |
| Shear calibration | Gaussian priors per bin, sampled | propagated through an extra covariance term |
| Redshift calibration | amplitudes of n(z) modes, Gaussian priors | correlated Gaussian prior on mean shifts |
| Statistic and likelihood | `ξ±`, `γ_t`, `w(θ)`; Gaussian | COSEBIs, band powers; Gaussian |

Consequences for comparison. The two surveys sample different amplitude parameters with flat priors (A_s against S8), so the implied prior on S8 differs; they treat the neutrino mass differently, which moves S8 at fixed data; and they handle baryons by cuts in one case and by marginalisation in the other. A difference between their S8 values is therefore not purely a difference between data sets. The joint DES Y3 + KiDS-1000 analysis exists because of this (arXiv:2305.17173); no equivalent joint analysis of DES Y6 and KiDS-Legacy was found in this session.

## Not verified
<!-- key: not-verified -->

- HSC Year 3: covariance, sampler, blinding and tension metric were not read at source.
- SPT-3G D1: likelihood form, covariance construction, sampler and the details of the blinding.
- Planck 2018 and PR4 likelihood papers: not fetched; only the 2013 profile-likelihood paper and the Hamimeche–Lewis method paper were read.
- KiDS-Legacy: the metric behind the quoted 0.73σ, and the content of the companion consistency paper.
- DESI DR2: the tension metric used for the BAO-against-CMB comparison and the covariance used for DR2 (the statements above are for the 2024 analysis).
- DES Y6: the cosmic-shear and 2×2pt companion papers and the methods paper were not read; the statements above come from the 3×2pt paper.
- Euclid: no Euclid Collaboration paper on the inference pipeline, likelihood code or blinding strategy was fetched.
