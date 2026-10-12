# Statistics and inference — live method debates and misconceptions

Scope: the method debates that are open in 2025–2026, with both sides cited, what would settle them, and the misconceptions that still circulate.
Snapshot: 2026-10-07

Flags: `[src]` read this session in the cited paper; `[sec]` taken from a named secondary source; `[der]` derived here, derivation stated.

## 1. Frequentist against Bayesian intervals in extended models
<!-- key: frequentist-against-bayesian-intervals-in -->

**The disagreement.** In ΛCDM, profile likelihoods and posteriors agree (Planck 2013, arXiv:1311.1657; DESI DR1 shifts below 1σ, arXiv:2508.11811). In extended models they do not: DESI DR1 full shape + BAO under w0waCDM gives shifts of 2.1σ to 6.6σ between the maximum likelihood and the posterior mean (arXiv:2508.11811) [src].

**Position A: the posterior is biased by the prior, the profile is the robust statement.** Herold et al. 2022 (arXiv:2112.12140) and Herold & Ferreira 2023 (arXiv:2210.16296) for early dark energy: the MCMC limit on `f_EDE` is a volume effect, the profile gives `f_EDE = 0.072 ± 0.036` and an H0 within 1.7σ of SH0ES. Holm et al. 2023 (arXiv:2309.04468) for BOSS: frequentist intervals show no tension with Planck. Straight et al. 2026 (arXiv:2603.25731): Bayesian limits on dark matter–proton scattering are too tight.

**Position B: the profile likelihood is not automatically valid either.** Its graphical reading needs Wilks' theorem, which fails for w0CDM with Planck and needs a boundary correction for Σm_ν (Herold et al. 2024, arXiv:2408.07700). The BOSS profile "prefers extreme values of the EFT parameters" (arXiv:2309.04468): the best fit may be unphysical. A frequentist interval says nothing about which parameter values are plausible, and a best fit in a 30-dimensional space with a noisy Boltzmann code is numerically fragile (hence the dedicated optimisers of arXiv:2312.02972 and arXiv:2401.14225).

**Position C: fix the prior, then the frameworks agree.** Bonici et al. 2026 (arXiv:2607.02498): with a Jeffreys prior on the EFT coefficients the DESI DR1 posterior encloses the MAP, and credible intervals agree with HOD-informed priors and with the profile likelihood "in both central values and degeneracy directions in the w0–wa plane". Tsedrik et al. 2025 (arXiv:2509.09562) and Pezzotta et al. 2026 (arXiv:2610.08751) reach the same end by reparameterisation and by Mpc units. Percival et al. 2022 (arXiv:2108.10402) make the same move for the covariance prior: choose the prior so that credible intervals have frequentist coverage.

**What would settle it.** More data: Holm et al. 2023 show that "the improved statistical power of future data will reconcile the constraints from frequentist and Bayesian inference". Until then the defensible practice is to publish both, with the MAP, and to state which is the headline.

**State at the snapshot.** DESI publishes Bayesian headline numbers and a separate frequentist paper (arXiv:2508.11811); the neutrino paper quotes Bayesian, Feldman–Cousins and effective-mass statements side by side (arXiv:2503.14744). No collaboration has adopted a frequentist headline for an extended model.

## 2. Bayesian evidence against delta chi2 for dynamical dark energy
<!-- key: bayesian-evidence-against-delta-chi2-for -->

**The facts.** DESI quotes the preference for w0waCDM as a `Δχ²_MAP` converted to σ with two degrees of freedom, with `Δ(DIC)` as a companion: 3.1σ and −8.7 for DESI DR2 + CMB (arXiv:2503.14738) [src]. A nested-sampling evidence on the same combination gives `ln B = −0.57 ± 0.26`, mildly favouring ΛCDM (Ong, Yallup & Handley 2025, arXiv:2511.10631; extended to seven model extensions in arXiv:2603.05472) [src].

**Side A: the evidence is the consistent Bayesian answer.** The Ockham factor penalises parameters the data do not need; where the evidence does favour w0wa (with the original DES-SN5YR, `ln B = +3.32 ± 0.27`), a tension analysis traces it to a 2.95σ conflict between DESI and that supernova sample inside ΛCDM, and the preference vanishes with the recalibrated sample (`ln B = −0.30 ± 0.19`) (arXiv:2511.10631) [src]. On this reading the signal is an inter-data-set tension that two extra parameters absorb.

**Side B: the evidence is only as meaningful as the prior on w0, wa.** The CPL parameters have no physical prior; the flat ranges are conventions, and the Bayes factor moves linearly with their volume. Efstathiou 2008 (arXiv:0802.3185) argued exactly this for dark energy: for nested, poorly motivated models, parameter estimation is more informative than the evidence [src]. A `Δχ²` has a calibrated frequentist meaning that does not depend on the prior, provided Wilks' conditions hold.

**Side C: neither in-sample statistic is the right question.** Karim, Speagle & Hložek 2026 (arXiv:2609.04334) score the models on held-out redshift blocks: a modest preference for w0waCDM, supplied entirely by one BAO block (LRG2, z = 0.706), with every supernova sample consistent with zero [src]. This disagrees with Side A on which data set drives the preference, and the two analyses have not been reconciled.

**What a careful text does.** It quotes `Δχ²`, the number of extra parameters and the σ; the Bayes factor with the prior ranges; and names the supernova sample and its calibration version. It does not translate `ln B` into σ or the reverse without saying how. The physics and the full list of critiques are in `cosmo-dark-energy-modified-gravity`.

**What will decide.** A coherent signal grows as `Δχ² ∝` data volume and overtakes any fixed Ockham factor, so the two statistics converge when the effect is real; a data-set conflict does not behave this way. DESI full-survey BAO (expected 2027, per `cosmo-galaxy-clustering`) is the next test.

## 3. Which tension metric, and is "n sigma" meaningful
<!-- key: which-tension-metric-and-is-n-sigma-meaningful -->

**State of practice.** DES settled on a suite after the comparison of Lemos et al. 2021 (arXiv:2012.09554): parameter differences, eigentension and suspiciousness agree with each other on simulated and real data (about 2.3σ for DES Y1 against Planck), and the Bayes ratio does not, because of its prior-volume dependence [src]. DES Y6 quotes a full-space parameter difference, estimated with normalising flows, as the headline, with the S8 projection next to it, and uses `n_σ < 3` as its criterion for combining data sets (arXiv:2601.14559) [src]. KiDS-Legacy quotes 0.73σ against Planck in its abstract (arXiv:2503.19441); the metric behind it was not read here.

**Open points.**

- Full space or projection. 1.8σ against 2.6σ for the same DES Y6 posteriors (arXiv:2601.14559). The projection is the more sensitive test if S8 was the pre-registered question; the full-space value is the honest one if it was not. Papers rarely say which was fixed in advance.
- The reference. The CMB side has moved from Planck alone to Planck + ACT DR6 + SPT-3G, which is tighter; a survey's "tension with the CMB" changes with the reference even when its own result does not.
- Non-Gaussian posteriors. Parameter-difference estimators with normalising flows are accurate to 0.2–0.5σ (arXiv:2105.03324); the suspiciousness needs a Gaussianity assumption for its p-value.
- Correlated data. With overlapping sky (DESI and DES lensing, CMB lensing and galaxy surveys) the independent-data metrics do not apply; posterior predictive tests do, but they have their own projection effects and lose power when nuisance parameters absorb the mismatch (arXiv:2610.03447).
- Is "nσ" meaningful at all. A Gaussian-equivalent σ is a relabelling of a p-value. Beyond about 3σ it depends on the tails of the posteriors and of the likelihood, which is where the Gaussian likelihood, the Hartlap correction (arXiv:2108.10402) and kernel density estimates are least reliable.

**Tension as a diagnostic for model comparison.** Ong et al. 2025 (arXiv:2511.10631) use five tension metrics on a grid of data sets and models to locate the origin of a model preference. The practice of checking pairwise consistency under ΛCDM before combining, and of asking whether an extension is preferred because it reconciles two data sets, is becoming standard.

Cross-probe tension values belong to `cosmo-tensions-anomalies`; this file covers the metrics.

## 4. Simulation-based inference: validation and trust
<!-- key: simulation-based-inference-validation-and-trust -->

**Does simulation-based inference need fewer simulations than a covariance?** The early claim was O(10^3) simulations for typical problems (Alsing et al. 2019, arXiv:1903.00007). Homer et al. 2024 (arXiv:2412.02311) show that for the same number of simulations the posterior variance inflation is equal to or greater than the Dodelson–Schneider result of the Gaussian-likelihood route, and call the assumption of a smaller requirement "inaccurate"; they add that the method "knows that it does", in that the inflation appears in the posterior width rather than as hidden scatter [src]. KiDS-SBI used 18 000 realisations for a two-point analysis (arXiv:2404.15402).

**Is a coverage test enough?** No, according to Alokda et al. 2026 (arXiv:2605.00980): coverage diagnostics "probe calibration only in an averaged sense and do not constrain posterior behavior at fixed parameter value"; their f_NL posteriors pass coverage and are underconfident, with tails that differ from the likelihood-based ones even for the power spectrum, where the Gaussian likelihood is best justified [src]. TARP is proven necessary and sufficient for an accurate estimator (arXiv:2302.03026), but in the same prior-averaged sense. No fixed-θ validation standard exists yet.

**Which side is the reference?** The usual framing treats the classical Gaussian likelihood as truth and tests the learned one against it. Vinciguerra et al. 2026 (arXiv:2607.17942) find the reverse on Euclid-like mocks: the explicit likelihood fails calibration under emulator error or likelihood non-Gaussianity and the learned one does not. KiDS-SBI finds a learned likelihood close to Gaussian at fixed cosmology but wider constraints from the cosmology dependence of the covariance, which the standard analysis fixes (arXiv:2404.15402).

**Model misspecification remains the unsolved part.** Every validation above assumes the simulator is right. The practical defences (summaries stable across simulators, out-of-distribution checks, a second galaxy–halo model) are documented case by case in `cosmo-beyond-two-point`, together with the status of each data analysis; no general test exists.

**Trust threshold for a collaboration headline.** In every collaboration analysis read for this skill (DESI DR2, DES Y6, KiDS-Legacy, ACT DR6, SPT-3G D1) the headline cosmology comes from an explicit Gaussian likelihood; the simulation-based analyses of survey data (KiDS-SBI; the DES Y3 map-level analyses listed in `cosmo-beyond-two-point`) are companion results.

## 5. Priors on nuisance parameters in EFT full-shape fits
<!-- key: priors-on-nuisance-parameters-in-eft-full-shape -->

Four families of answer coexist in 2025–2026, and they do not return the same error bars.

| Approach | Claim | Objection | Reference |
|---|---|---|---|
| Wide Gaussian priors of order one on EFT coefficients ("West-coast", "East-coast") | Agnostic; perturbativity fixes the scale | Informative in practice; 1σ to 2σ projection shifts in BOSS; the two conventions disagree at 1σ on the same data | arXiv:2208.05929, arXiv:2207.14784 |
| Priors learned from HOD mocks | Restricts the nuisance space to what galaxies can produce; recovers the truth where standard priors fail | Imports the HOD model and the simulation suite into a perturbative analysis; the answer is as good as the galaxy–halo model | arXiv:2409.12937, arXiv:2402.13310 |
| Jeffreys prior or reparameterisation | Removes the volume factor without new physics input | A Jeffreys prior is data-model dependent and can leave over-broad tails (the hybrid of arXiv:2607.02498 is needed for ω_c) | arXiv:2607.02498, arXiv:2509.09562, arXiv:2610.08751 |
| No prior: profile likelihood | Prior-independent | Best fit at extreme nuisance values; validity of the interval construction | arXiv:2309.04468, arXiv:2508.11811 |

The size of the stake is documented in `cosmo-galaxy-clustering`: with simulation-based priors the full-shape σ8 moves well away from the value obtained with conservative priors. The physics of the models is there; the statistical point here is that "the full-shape constraint" on an extended model is not a single number until the nuisance prior is named.

## 6. Covariance: mocks, analytic, or neither
<!-- key: covariance-mocks-analytic-or-neither -->

**The trade.** Mocks contain survey realism (geometry, fibre assignment, imaging systematics, non-Gaussian terms) and pay for it with Wishart noise that scales with the data-vector length. Analytic covariances are noise-free and cheap to iterate, and pay with missing terms. The two errors are of different kinds: the first is quantified by known formulae (`results.md` §1.1), the second only by comparison with mocks.

**Where each collaboration stands** (`surveys-and-data.md`). Lensing and 3×2pt: analytic, validated on mocks (DES Y6, KiDS-Legacy). CMB spectra: analytic with a Monte Carlo correction from about 1600 simulations (ACT DR6). BAO: semi-analytic, calibrated on the data (DESI). Full shape: mocks with a correction, because the analytic Fourier-space covariance failed validation (arXiv:2411.12027).

**Open points.**

- Longer data vectors. Joint multi-tracer full shape with bispectrum, or 3×2pt with many tomographic bins, pushes `n_d` into the hundreds or thousands; with 1000 mocks the error inflation reaches tens of per cent (`results.md` §1.1). Compression, denoising and analytic covariances are the three exits, and each has a known failure: compression at a wrong fiducial point, denoised matrices with too-small errors in configuration space (arXiv:2604.13851), analytic matrices without survey realism.
- Which correction. The 2022 matching-prior posterior (arXiv:2108.10402) is the most complete treatment; whether current survey pipelines use it, the 2014 factors, or the Hartlap factor alone was not established here for the 2025–2026 analyses.
- Tails. A Hartlap-corrected Gaussian underestimates tail probabilities relative to the t-distribution (arXiv:2108.10402); tension statements live in the tails.
- Cosmology dependence. Fixed (and iterated) covariance is the rule for Gaussian likelihoods (arXiv:1204.4724); KiDS-SBI finds that letting the forward model carry the cosmology dependence widens the constraints (arXiv:2404.15402). Both statements are correct; they concern different likelihoods.
- Simulation-based inference does not remove the problem (arXiv:2412.02311).
- Fully analytic cross-covariances between statistics of the same galaxies are becoming available (arXiv:2602.12343), which removes one of the reasons for mock-based joint covariances.

## 7. Emulators and differentiable pipelines in the likelihood
<!-- key: emulators-and-differentiable-pipelines-in-the -->

**What is settled.** Emulating a Boltzmann code is a solved engineering problem at current precision: errors below 0.4% and posterior differences below sampling noise (arXiv:2106.03846), and KiDS-Legacy runs its headline analysis on an emulated `P(k)` (arXiv:2503.19441) [src].

**What is not.**

- Propagation of emulator error. The common practice is to show that the error is small and then ignore it. A Bayesian propagation exists (arXiv:2205.11587) but its adoption in survey analyses was not found here. Vinciguerra et al. 2026 (arXiv:2607.17942) show that emulator inaccuracy can miscalibrate an explicit likelihood for Euclid-like data.
- Emulators of simulations inherit the simulations. A 1% dark-matter-only emulator (arXiv:2010.11288) moves the error budget to baryonic feedback and to the galaxy–halo connection, where the "emulator error" is a modelling choice and not an interpolation residual. The probe skills document the resulting disagreements.
- Extended models. Training sets cover ΛCDM and a few extensions with hard parameter boxes; posteriors that reach the box edge are a recurrent symptom (`cosmo-beyond-two-point`).
- Gradient-based and GPU inference. Differentiable emulators enable NUTS and GPU nested sampling, with reported gains of orders of magnitude in wall-clock time and a 39-dimensional Bayes factor in two days on one GPU (arXiv:2509.13307) [src]. Whether evidences from such pipelines are as reliable as CPU nested sampling in the tails is tested in that paper for one case.
- Emulating the likelihood or the posterior directly (learned proposals, flows for combining probes) puts a density estimator inside the inference; DES Y6 combines independent probes through normalising flows (arXiv:2601.14559) [src]. The accuracy of such flows for tension estimates is 0.2σ to 0.5σ (arXiv:2105.03324).

## 8. Blinding of extended-model results
<!-- key: blinding-of-extended-model-results -->

**The gap.** Blinding schemes are designed and validated for the baseline observable in the baseline model: the BAO peak position and RSD amplitude for DESI (arXiv:2404.07282), the 3×2pt data vector under ΛCDM and wCDM for DES (arXiv:1911.05929, arXiv:2601.14559). The results that attract most attention are extended-model fits and combinations with external data, which are usually run after the baseline is unblinded.

**Points under discussion.**

- A catalogue-level shift hides the distance scale and the growth rate; it does not by itself hide a preference for `w0`, `wa` once several redshift bins and external data sets are combined, unless the choice of combinations and priors was frozen beforehand. Which of the DESI DR2 dark-energy combinations were pre-specified was not read here.
- External data are public and unblinded. A combined analysis can be blind only to the new data, and the choice of which external data set is the headline (the supernova compilation, the CMB likelihood) is an analysis choice with a documented effect of 2.8σ to 4.2σ (arXiv:2503.14738).
- Blinding against diagnosis. KiDS-Legacy reports that its scheme impeded the diagnosis of systematics (arXiv:2503.19441); ACT DR6 moved one validation test to after unblinding because "actual data were needed to make further progress" (arXiv:2503.14452); DES Y6 needed three blind iterations and dropped a lens bin without finding the cause (arXiv:2601.14559). The alternative, unblinding to investigate, costs credibility. The current answer is a written plan that states in advance what happens when a test fails.
- Reanalyses of public data, which now produce many of the statistical critiques, are not blind by construction.
- Tooling for Stage IV: data-vector blinding with encryption for Rubin (arXiv:2604.18111); a Lyα forest scheme for DESI (arXiv:2607.07875).

## 9. What the next data will decide
<!-- key: what-the-next-data-will-decide -->

| Question | What decides it | When (from the sibling skills) |
|---|---|---|
| Is the w0wa preference a coherent signal or a data-set conflict | `Δχ²` grows with data volume for a signal and overtakes a fixed Ockham factor; the out-of-sample score should spread over redshift blocks instead of sitting in one | DESI full-survey results, expected 2027 |
| Do frequentist and Bayesian full-shape constraints converge | larger volume reduces projection effects (arXiv:2309.04468) | DESI DR2 and full-survey full shape |
| Can simulation-based inference carry a headline result | a fixed-parameter validation standard and a misspecification test accepted by a collaboration | Stage-IV first analyses |
| Is the Gaussian likelihood adequate for Stage-IV two-point data | calibration tests of the explicit likelihood (arXiv:2607.17942, arXiv:2012.06267) on survey-realistic mocks | Euclid DR1, Rubin first-year analyses |
| How many mocks, or none | analytic cross-covariances and denoising validated on joint data vectors | ongoing |

Forecast statements about the statistical reach of future surveys (figures of merit, σ(Σm_ν)) are in the probe skills and are Fisher-based unless stated otherwise; §10 of `physics-and-methods.md` lists what that implies.

## 10. Misconceptions and stale claims
<!-- key: misconceptions-and-stale-claims -->

| Claim that circulates | What is correct | Corrected by |
|---|---|---|
| "The Hartlap factor corrects for the finite number of mocks." | It removes the bias of the precision matrix only. The scatter of the best fit (Dodelson–Schneider) and the bias of the likelihood width need separate factors, or the t-distribution posterior with a matching prior. | arXiv:1304.2593, arXiv:1312.4841, arXiv:2108.10402 |
| "With N mocks greater than the number of data points the covariance is fine." | That is the condition for invertibility. Precision needs `n_s` well above `n_d`: with `n_s = 1000` and `n_d = 400` the scatter of the best fit grows by 29% in error bar (variance factor 1.65), and a posterior built on the raw sample covariance must be widened by 65%. | arXiv:1212.4359; `results.md` §1.1 |
| "Simulation-based inference needs fewer simulations than a covariance matrix." | The variance inflation is at least the Dodelson–Schneider one for the same number of simulations. | arXiv:2412.02311 |
| "The posterior passed a coverage test, so it is validated." | Coverage is a prior average; posteriors can pass and be underconfident with wrong tails. | arXiv:2605.00980 |
| "`sqrt(Δχ²)` is the significance." | Only for one extra parameter. For w0wa, DESI uses two degrees of freedom: `Δχ² = 12.5` is 3.1σ, not 3.5σ. | arXiv:2503.14738 |
| "A 3σ `Δχ²` preference means the Bayesian evidence favours the model." | For DESI DR2 + Planck the same data give 3.1σ and `ln B = −0.57 ± 0.26`. | arXiv:2511.10631 |
| "The Bayes ratio R > 1 shows that two data sets agree." | `R` scales with the prior volume; widening a flat prior turns a 3σ discrepancy into "agreement". | arXiv:1902.04029, arXiv:2012.09554 |
| "The tension is nσ" without metric or reference. | DES Y6 against the CMB is 1.8σ or 2.6σ depending on the subspace; CMB against DESI DR2 is quoted as 1.6σ, 2.3σ or 2.8σ by three collaborations with three CMB combinations. | arXiv:2601.14559, arXiv:2503.14452, arXiv:2506.20707 |
| "The posterior mean is the best-fitting value." | In extended models the two differ by up to 6.6σ (DESI DR1 full shape, w0waCDM). | arXiv:2508.11811 |
| "A shift of the full-shape posterior relative to Planck is a tension in the data." | For BOSS it was largely a prior-volume effect; frequentist intervals show no tension. | arXiv:2208.05929, arXiv:2309.04468 |
| "Profile likelihoods are prior-free, hence always safe." | The graphical `Δχ²` interval needs Wilks' conditions, which fail near boundaries and are in doubt for `w0` with Planck; the best fit can sit at extreme nuisance values. | arXiv:2408.07700, arXiv:2309.04468 |
| "The upper limit on the neutrino mass measures the sensitivity." | Near a boundary the truncated-posterior width (0.020 eV for DESI DR2 + CMB) is not the sensitivity; boundary-free statements are needed. | arXiv:2503.14744; `cosmo-neutrinos-dark-matter` |
| "MultiNest and PolyChord are interchangeable." | On the DES Y1 likelihood MultiNest gave inconsistent evidences and narrower intervals. | arXiv:2202.08233 |
| "`R − 1 < 0.01` guarantees convergence." | The classical statistic fails for heavy tails and unequal chain variances; it says nothing about tail quantiles. | arXiv:1903.08008 |
| "A parameter-dependent covariance in the Gaussian likelihood is more accurate." | It adds artificial information; keep the covariance fixed and iterate. | arXiv:1204.4724 |
| "The Fisher forecast is the expected error bar." | For `w0`–`wa` from geometrical probes it is too small by 30%–70%, and it contains no projection effect. | arXiv:1205.3984 |
| "The emulator is accurate to 1%, so theory error is negligible." | The figure is against dark-matter-only simulations inside the training box; emulator error can miscalibrate a Gaussian likelihood. | arXiv:2010.11288, arXiv:2607.17942 |
| "The jackknife gives the covariance." | Without correction it is biased in a scale-dependent way; an internal 2σ can be anything from 1σ to 3σ. | arXiv:0810.1885, arXiv:2109.07071 |
| "The analysis was blind." | Ask at which level, with which unblinding criteria, and what changed afterwards; three collaborations document non-trivial events at unblinding. | arXiv:2601.14559, arXiv:2503.14452, arXiv:2503.19441 |
| "Three supernova samples confirm the result." | They share objects and calibration and give 2.8σ to 4.2σ with the same BAO and CMB; the spread is an analysis-choice effect. | arXiv:2503.14738; `cosmo-supernovae` |

## Not verified
<!-- key: not-verified -->

- Whether any 2025–2026 collaboration analysis uses the matching-prior t-distribution of arXiv:2108.10402 in production.
- Which DESI DR2 extended-model combinations were fixed before unblinding.
- The reply of the DESI collaboration to the Bayesian-evidence reanalyses, and any reconciliation between arXiv:2511.10631 (the supernova sample drives the preference) and arXiv:2609.04334 (one BAO block drives it).
- Later papers on the early-dark-energy profile likelihood with ACT DR6 or SPT-3G data were not searched.
- Bayesian model averaging, hierarchical models for supernova and distance-ladder inference (BEAMS, UNITY, BayeSN), Gaussian-process reconstruction and its priors, and cross-validation beyond arXiv:2609.04334 are outside what was researched; see `cosmo-supernovae` and `cosmo-distance-ladder-h0` for the hierarchical models.
- Field-level inference raises its own statistical questions (noise model, sampling in 10^6 dimensions, validation of the posterior on the initial conditions); they are covered in `cosmo-beyond-two-point` and were not researched here.
- Recent papers found by the date-sorted searches (from 2025-06-01) after the 100-source cap was reached. They are listed by title only, were not read beyond the title, and are leads for an update:
  - Euclid Collaboration (Gouyou Beauchamps et al.), "Euclid preparation. CII. Non-Gaussianity of 2-pt statistics likelihood: Parameter inference with a non-Gaussian likelihood in Fourier and configuration space" (April 2026). Directly relevant to §1 and §4 of the methods and systematics files and to the Euclid section.
  - Pyne, Joachimi, Gordon & Lin, "A guide to choosing data compression methods for cosmological inference" (September 2026).
  - Sugiyama & Park, "Data Compression with Noise Suppression for Inference under Noisy Covariance" (August 2025).
  - Guth & Namjoo, "Statistical isotropy of the universe and the look-elsewhere effect" (February 2026).
  - Šarčević, van der Wild & Trendafilova, "DerivKit: stable numerical derivatives bridging Fisher forecasts and MCMC" (February 2026).
  - Rogozenski et al. (LSST DESC), "Fisher Forecasting for the DESC with Augur" (August 2026).
  - Dhawalikar, Paranjape & Alam, "Stabilizing simulation-based cosmological Fisher forecasts" (June 2025).
  - Xu et al., "Impact of non-Gaussian likelihood on cosmological constraints from the thermal Sunyaev–Zel'dovich power spectrum: a simulation-based inference analysis" (June 2026); its abstract, read this session, reports that for multipoles below 1000 the Gaussian likelihood gives unbiased cosmological constraints for a Planck-like analysis.
  - Pierre et al., "Mitigating Model Misspecification in Simulation-Based Inference for Galaxy Clustering" (July 2025), and Tirapongprasert & Ho, "Don't Cut Corners: How Training Outside the Prior Makes Simulation-Based Inference More Robust" (August 2026); abstracts read, not cited for lack of source slots.
  - Bonici et al., "Effort: a fast and differentiable emulator for the Effective Field Theory of the Large Scale Structure of the Universe" (January 2025); abstract read: posteriors from Effort with Hamiltonian Monte Carlo agree with PyBird with Metropolis–Hastings within Monte Carlo noise.
  - Ormondroyd et al., "Dynamic or Systematic? Bayesian model selection between dark energy and supernova biases" (September 2025); abstract read: a magnitude offset between low- and high-redshift supernovae is favoured by the evidence over a flexible dark-energy model.
