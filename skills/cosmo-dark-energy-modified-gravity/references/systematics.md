# Systematics — dark energy and modified gravity

Scope: what can fake or hide a departure from Λ or from general relativity at
the level of the combined analysis; the probe-level systematics are in the
sibling skills and are summarised only where they decide the dark-energy
result.

Snapshot: 2026-10-07

Flags: `[src]` read this session in the cited paper; `[sec]` from a named
secondary source; `[der]` derived here.

## 0. How to read this file
<!-- key: how-to-read-this-file -->

A dark-energy or modified-gravity claim is a statement about a combination of
data sets. Its systematics are of three kinds:

1. A systematic inside one probe that moves the relative distance or amplitude
   between low and high redshift (Sections 1–4).
2. An inference artefact: priors, parameterisation, choice of statistic,
   repeated testing (Sections 5–8).
3. A modelling limit specific to tests of gravity (Sections 9–12).

For the signal under discussion in 2024–2026 the sizes are: BAO + CMB +
supernovae prefer `w0wa` at 3.0–3.4σ (`results.md` Sections 2 and 9). A
systematic that removes about 1.5σ from this makes it unremarkable. Several
candidates of that size are documented below.

## 1. Supernova relative calibration between low and high redshift
<!-- key: supernova-relative-calibration-between-low-and -->

- **Mechanism.** The `w0wa` signal from supernovae is a difference in distance
  modulus between the `z < 0.1` anchor sample, observed by many historical
  surveys, and the homogeneous high-redshift sample. Any zero-point,
  colour-law, selection or host-correction error that differs between the two
  mimics evolution in `w`. The direction is not random: Dhawan, Popovic and
  Goobar 2024, arXiv:2409.18668, find that "all the dominant systematic errors
  shift the dark energy inference towards the DESI 2024 results from an
  underlying ΛCDM cosmology" [src].
- **Size.** The DESY5 low-redshift points sit at `mu − mu_fid ≈ 0.03` mag
  against 0.01 mag for Pantheon+ (arXiv:2503.14738) [src]. An offset of ~0.04
  mag between low and high redshift in common supernovae (Efstathiou 2024,
  arXiv:2408.07175) [src], of which 43% is modelling improvements and 38%
  different selection functions (Vincenzi et al. 2025, arXiv:2501.06664)
  [src]. The Dovekie recalibration and colour-law fix changed `Omega_m` by
  −0.022 and the significance from 4.2σ to 3.2σ (Popovic et al. 2025,
  arXiv:2511.07517) [src]. Inconsistent host masses produced a > 0.03 mag
  discrepancy between the Union3 and Pantheon+ low-redshift means, reduced to
  0.01 mag after correction (Hoyt et al. 2026, arXiv:2601.19424) [src].
- **Mitigation.** Recalibration on a common photometric system; consistent
  host properties across redshift; a single combined sample with one set of
  bias corrections (Unite, arXiv:2609.05053) [src]. Details:
  `cosmo-supernovae`.
- **Validation test.** Drop `z < 0.1` supernovae and refit: the DESI DR2 test
  shows much larger errors and a small shift of the best fit
  (arXiv:2503.14738) [src]. Marginalise over a free magnitude offset between
  the low- and high-redshift subsamples (Notari, Redi and Tesi 2024,
  arXiv:2411.11685) [src]. Compare intercepts of the magnitude–distance
  relation between subsamples (Huang, Cai and Wang 2025, arXiv:2502.04212)
  [src].
- **Referee expects.** arXiv:2408.07175, arXiv:2501.06664, arXiv:2511.07517,
  arXiv:2601.19424.

## 2. Non-independence of the supernova compilations
<!-- key: non-independence-of-the-supernova-compilations -->

- **Mechanism.** Pantheon+, Union3 and the DES samples share most of their
  low-redshift supernovae; 20% of the supernovae are common to Pantheon+ and
  DES-SN5YR (arXiv:2501.06664) [src]. Agreement among them does not test a
  common-mode error in the anchor.
- **Size.** Removing the common objects from one catalogue or the other
  changes the exclusion of ΛCDM between 3.8σ and 2.5σ (arXiv:2411.11685,
  DR1-era data) [src].
- **Mitigation and test.** Use one compilation per fit; never multiply
  significances; prefer the combined Unite sample when the question is the
  joint constraint.

## 3. BAO: which bins carry the signal
<!-- key: bao-which-bins-carry-the-signal -->

- **Mechanism.** DESI BAO errors are statistics-dominated (sibling
  `cosmo-galaxy-clustering` [sec]), so the concern is not a known systematic
  but a statistical fluctuation or an unknown effect in a few bins.
- **Size.** In DR1 the preference was "primarily driven by the two LRG samples
  at z_eff = 0.51 and z_eff = 0.71"; replacing DESI at `z < 0.8` by SDSS BAO
  returned parameters consistent with ΛCDM (Chudaykin and Kunz 2024,
  arXiv:2407.02558) [src]. For the DR1→DR2 sequence, an e-process analysis
  finds the evidence "concentrated almost entirely in the LRG2 redshift bin";
  without it the e-value falls from 33.97 to 0.49 (Kim, Mota and Tamosiunas
  2026, arXiv:2607.28918) [src].
- **Counter-evidence.** The DR2 measurements are "consistent with DESI DR1 and
  SDSS" (arXiv:2503.14738, abstract) [src]; the sibling
  `cosmo-galaxy-clustering` gives the SDSS–DESI difference at `z ≈ 0.7` as
  about 2.6σ in DR2 [sec].
- **Validation test.** Leave-one-bin-out fits; replacement of DESI bins by
  SDSS; consistency of `D_M/D_H` (which is independent of `r_d`) with the
  fitted model.
- **Lyman-α.** The DR2 Lyα full-shape distances agree with Planck ΛCDM and sit
  about 2σ from the CMB + BAO `w0waCDM` prediction (sibling
  `cosmo-lyman-alpha`, citing the 2026 DESI Lyα full-shape paper [sec]). A
  `w0wa` best fit must be checked at `z = 2.33` as well as at `z < 1`.

## 4. The CMB input
<!-- key: the-cmb-input -->

- **Which information is used.** DESI + compressed (`theta_*`, `omega_b`,
  `omega_bc`) priors: 2.4σ; + primary CMB without lensing: 2.7σ; + lensing:
  3.1σ (arXiv:2503.14738) [src]. The lensing likelihood adds 0.4σ without
  moving the posterior.
- **Which likelihood.** CamSpec and Plik agree; PR4 LoLLiPoP–HiLLiPoP shifts
  the DESI + CMB + DESY5 contour by ~0.1σ (arXiv:2503.14738) [src]. For
  modified gravity the choice matters much more (Section 10).
- **Which experiment.** The ΛCDM distance between CMB and DESI DR2 is 1.6σ,
  2.8σ or 3.7σ for P-ACT, CMB-SPA and SPT+ACT (sibling `cosmo-cmb` [sec]).
- **Optical depth.** τ is taken from Planck low-ℓ polarisation in essentially
  every analysis. `tau ~ 0.09` reduces the `w0wa` preference from ≃3σ to ≃1.5σ
  (Sailer et al. 2025, arXiv:2504.16932) [src]; dropping the lensing and low-ℓ
  polarisation constraints brings the preference below 95% CL (Jhaveri, Karwal
  and Hu 2025, arXiv:2504.21813) [src].
- **Compression accuracy.** Compressed likelihoods are validated per model
  space; a compression built for ΛCDM is not automatically valid in `w0waCDM`
  with free neutrino mass (Srivastav, Bansal and Huterer 2026,
  arXiv:2606.18455, provide five separate compressions) [src].
- **Validation test.** Repeat the fit with compressed priors, with and without
  lensing, with a τ prior widened or replaced, and with at least two CMB data
  sets.

## 5. Prior-volume (projection) effects
<!-- key: prior-volume-projection-effects -->

- **Mechanism.** When the data do not constrain all directions, marginal
  posteriors are pulled towards regions of large prior volume, away from the
  best fit. Full-shape clustering with EFT nuisance parameters is the worst
  case.
- **Size.** DESI DR1 full shape + BAO in `w0waCDM`: shifts between the
  maximum-likelihood estimate and the Bayesian posterior mean of 2.1σ, 4.1σ,
  6.5σ, 6.3σ and 6.6σ for `sigma8`, `H0`, `Omega_m`, `w0`, `wa`; under ΛCDM
  the shifts are below 1σ (Morawetz et al. 2025, arXiv:2508.11811) [src]. The
  frequentist intervals are "significantly shifted relative to the Bayesian
  credible intervals for the w0waCDM model, unless supernovae data are
  included" [src].
- **Where it does not matter.** For BAO + CMB + supernovae, profile
  likelihoods and posteriors agree (Herold and Karwal 2025, arXiv:2506.12004)
  [src].
- **Mitigations.** ShapeFit compression, which "inherently mitigates the prior
  volume effects" (arXiv:2602.18761) [src]; reparameterising the EFT nuisance
  parameters so that "the actual posterior maximum values are within the
  marginalised credible interval" (Tsedrik, Carrilho and Moretti 2025,
  arXiv:2509.09562) [src]; simulation-based priors on the EFT parameters (Chen
  and Ivanov 2025, arXiv:2507.00118) [src]; profile likelihoods.
- **Validation test.** Report the MAP next to the posterior mean; fit
  noiseless synthetic data at a known cosmology and check that the truth is
  recovered inside 1σ.
- **Modified gravity.** For Hu–Sawicki `f(R)` in DESI DR1 full shape, `f_R0`
  "is largely orthogonal to the cosmological parameters ... such that no
  additional projection effects relative to the GR case are introduced"
  (arXiv:2604.26915) [src].

## 6. Priors on the dark-energy parameters themselves
<!-- key: priors-on-the-dark-energy-parameters-themselves -->

- **Mechanism.** Uniform priors on (`w0`, `wa`) give equal weight to regions
  no physical model populates; the Bayes factor scales inversely with the
  prior volume.
- **Size.** Reversing the DR2 + CMB + DESY5 Bayes factor needs priors wider by
  more than 10 in each parameter (arXiv:2503.14743) [src]. Theory-informed
  priors from quintessence reduce the Planck + DESI tension with Λ from ~3.1σ
  to ~1.3σ (Toomey et al. 2025, arXiv:2509.13318) [src]. With priors on
  Padé-`w` parameters, thawing quintessence is still preferred over Λ when
  supernovae are included, "not sensitive to our choice of prior" (Shlivko
  2025, arXiv:2512.20832) [src]. See also Patel, Chakraborty and Amendola
  2024, arXiv:2407.06586.
- **Hard prior edges.** The DESI BAO-only and BAO + CMB-prior posteriors are
  cut by `wa > −3`; their means and limits are prior-dependent
  (arXiv:2503.14738) [src]. Supernova-only `wa` values of large magnitude are
  the same effect (`cosmo-supernovae`).
- **Reading.** A theory-informed prior that excludes `w < −1` answers the
  question "is quintessence preferred to Λ"; it cannot answer "is Λ rejected".
  State which question is asked.

## 7. Parameterisation artefacts
<!-- key: parameterisation-artefacts -->

- CPL forces a crossing of −1 once `theta_*` and `Omega_m` are fixed and `w0 >
  −1` (arXiv:2503.14738) [src].
- Data generated from a non-crossing (algebraic quintessence) model yield a
  CPL crossing with a `chi2` gain exceeding the observed one in 3.2% of 1,000
  mocks (Keeley, Shafieloo and Matthewson 2025, arXiv:2506.15091) [src].
- The evidence is in the slope, not in the offset: `w_p` is 0.6σ (DESI + CMB)
  and 1.9σ (with DESY5) from −1 [der: (−1.024 + 1)/0.043 and (−0.954 +
  1)/0.024, values from arXiv:2503.14738]; the argument is due to Cortês and
  Liddle 2024, arXiv:2404.08056 [src].
- High-order polynomial expansions and high-redshift cut-offs of `w(z)` "can
  be pathological" (Linder 2007, arXiv:0708.0024) [src].
- Choosing the redshift at which the departure from −1 is maximal (Rippentrop,
  Ishak and Gonzalez 2026, arXiv:2608.25278) raises the quoted σ by
  construction; it is a statement within CPL [src].
- **Validation test.** Fit at least one class that cannot cross −1 and one
  non-parametric reconstruction, and quote `Delta chi2` for each (as in
  arXiv:2503.14743).

## 8. Repeated looks and choice of test
<!-- key: repeated-looks-and-choice-of-test -->

- Wilks-based σ values assume one test. DESI has been tested against Λ at DR1
  and DR2 and will be again; with seven BAO bins and several supernova samples
  the number of implicit trials is larger still. Kim et al. (arXiv:2607.28918)
  find that with a look-elsewhere correction over the seven bins the BAO-only
  signal does not survive [src].
- Frequentist σ, DIC, and Bayes factor can disagree in sign for the same data
  (Pantheon+ with DR2: 2.8σ, `Delta DIC = −6.8`, `ln B = −0.66 ± 0.44`;
  arXiv:2503.14738, arXiv:2503.14743) [src].
- **Referee expects.** The statistic named, the number of extra parameters,
  the prior ranges, and both a frequentist and a Bayesian number.

## 9. Combining data sets that disagree
<!-- key: combining-data-sets-that-disagree -->

- Under ΛCDM, DESI BAO and the CMB differ at 2.3σ (arXiv:2503.14738) [src];
  all DES probes and the CMB at 2.8σ (arXiv:2601.14559) [src]; under constant
  `w`, Unite finds "strong evidence of tension between CMB measurements and
  the combined BAO and supernova datasets" (arXiv:2609.05053) [src].
- A model with two more parameters that absorbs a 2–3σ inter-data-set
  difference will be preferred at 2–3σ. The preference and the tension are one
  fact, not two.
- **Mitigation.** Quantify consistency under each model before combining
  (Raveri and Hu 2018, arXiv:1806.04649; Handley and Lemos 2019,
  arXiv:1902.04029); the metrics themselves belong to
  `cosmo-statistics-inference`.
- **Alternative absorbers of the same mismatch.** Negative effective neutrino
  mass (Elbers et al. 2024, arXiv:2407.10965), higher τ (arXiv:2504.16932),
  interacting dark energy at 3–5σ (Li et al. 2026, arXiv:2601.07361),
  non-minimal coupling at 3σ (Pan and Ye 2025, arXiv:2503.19898), a weaker
  cosmological gravitational constant at 3.3σ (Wen et al. 2026,
  arXiv:2609.40176) [src]. That five unrelated one- or two-parameter
  extensions each reach about 3σ on the same data is the signature of a
  data-set mismatch, not of five discoveries.

## 10. Modified gravity: degeneracy with the CMB lensing amplitude
<!-- key: modified-gravity-degeneracy-with-the-cmb -->

- **Mechanism.** Σ rescales the lensing potential, so it absorbs any excess or
  deficit of lensing smoothing in the CMB power spectra, exactly as the
  phenomenological `A_L` does.
- **Size.** The Planck PR3 tension of Σ0 with GR disappears with the PR4
  LoLLiPoP + HiLLiPoP likelihoods (Ishak et al. 2024, arXiv:2411.12026) [src].
  A 2026 analysis with KiDS-Legacy and Planck + ACT + SPT finds `Sigma0 =
  0.149 ± 0.051` (3.0σ) and attributes it to "higher amplitudes in the
  large-scale CMB lensing measurements" (Du et al. 2026, arXiv:2602.03110)
  [src]. The growth-index excess of Nguyen, Huterer and Wen 2023,
  arXiv:2302.01331, is partly the same Planck feature: in Planck data it
  "offsets the preference for nonzero curvature" [src].
- **Mitigation.** Run with at least two CMB likelihoods and with and without
  lensing reconstruction; report Σ0 with `A_L` free as a diagnostic. The `A_L`
  history is in `cosmo-cmb`.

## 11. Modified gravity: dependence on the background and on the functional form
<!-- key: modified-gravity-dependence-on-the-background -->

- **Background.** In DESI DR1, `mu0` moves from 0.05 ± 0.22 (ΛCDM background)
  to −0.24 (+0.32/−0.28) (`w0wa` background) with the same data; Σ0 is stable
  (arXiv:2411.12026) [src]. A modified-gravity constraint is conditional on
  the expansion history assumed.
- **Functional form.** A time dependence proportional to `Omega_DE(a)` is
  insensitive to modifications at `z > 1`. Pan and Ye (arXiv:2503.19898) argue
  that the common EFT parameterisations are too rigid and that the data
  constrain a quadratic expansion [src]. Rebouças et al. 2026,
  arXiv:2606.00411, find deviations from GR that vanish when a cosmological
  constant is assumed and shift towards GR when cosmic shear and CMB lensing
  are added [src].
- **Stability priors.** Ghost and gradient conditions remove part of the EFT
  parameter space and produce one-sided posteriors (arXiv:1312.5742 for the
  conditions) [src]. A "preference" that sits against a stability boundary is
  a prior effect until shown otherwise; the DESI `c_B > 0` indication is
  flagged by its authors as needing "further study to determine whether this
  is due to systematics or new physics" (arXiv:2411.12026) [src].
- **Neutrinos.** Massive neutrinos suppress growth and are degenerate with
  `mu < 1` and with `f_R0`; the DESI `f(R)` analysis studies this degeneracy
  explicitly (arXiv:2604.26915) [src].

## 12. Modified gravity: non-linear scales, bias and astrophysics
<!-- key: modified-gravity-non-linear-scales-bias-and -->

- **Non-linear modelling.** Weak-lensing tests are "limited by the absence of
  nonlinear predictions that are reliable at our required precision" (DES
  Collaboration 2022, arXiv:2207.05766) [src]; scale cuts remove most of the
  signal-to-noise. KiDS-1000 cosmic shear leaves `f_R0` unconstrained even
  with a fully non-linear model (Tröster et al. 2020, arXiv:2010.16416) [src].
  Screening makes the non-linear regime model-specific.
- **`E_G`.** (i) Mismatched effective redshifts between lensing, clustering
  and RSD pieces; (ii) non-Gaussian error of a ratio; (iii) residual
  systematic budget of 2% (CMASS) and 3% (LOWZ) in the calibrated estimator
  (Wenzl et al. 2024, arXiv:2401.12971) [src]; (iv) dependence of the GR
  prediction on `Omega_m,0` and the need for a careful bias treatment (Leonard
  et al. 2025, arXiv:2511.19194) [src]. The 2.6σ low value of Pullen et al.
  2015, arXiv:1511.04457, arose only at scales above 80 Mpc/h [src] and is not
  reproduced by the calibrated estimator.
- **Cluster tests of screening.** Results depend on the assumed mass profile:
  NFW and Hernquist give agreement with GR, a Burkert profile (disfavoured by
  lensing) gives a ~2σ departure; dynamically disturbed clusters drive part of
  it (Pizzuti et al. 2026, arXiv:2604.23631) [src]. Cluster abundance needs
  the mass calibration and the modified halo mass function (Cataneo et al.
  2014, arXiv:1412.0133) [src].
- **Galaxy-scale tests.** Astrophysical noise in gas–star offsets and warps is
  marginalised with an empirical model, and data-quality cuts matter (Desmond
  and Ferreira 2020, arXiv:2009.08743) [src].
- **Distance ladder.** Environment-dependent screening must be modelled per
  host galaxy (potential, acceleration, curvature); the result is a null
  (Högås et al. 2025, arXiv:2512.14814) [src].

## 13. What a referee checks in a dark-energy or modified-gravity results section
<!-- key: what-a-referee-checks-in-a-dark-energy-or -->

1. Which supernova sample and which calibration version (pre- or post-Dovekie,
   Union3 or Union3.1, Pantheon+ with original or corrected host masses,
   Unite).
2. Which CMB: experiment, likelihood, lensing included or not, τ prior.
3. Which DESI release for BAO and for full shape, and whether DR1 full shape
   and DR2 BAO are combined with their cross-covariance.
4. The statistic behind every "σ": `Delta chi2_MAP` with stated degrees of
   freedom, or a Bayes factor with stated priors; never one presented as the
   other.
5. MAP or profile-likelihood values next to posterior means whenever
   full-shape data or weakly constrained parameters are involved.
6. A test without the `z < 0.1` supernovae, and a test without supernovae at
   all.
7. Consistency of the data sets under the base model, quantified, before the
   extended-model preference is quoted.
8. For a phantom-crossing claim: a fit of a non-crossing class and its `Delta
   chi2`; a statement of whether the claim is within CPL.
9. For `mu`, `Sigma`: the convention (GR = 0 or 1), the time dependence, the
   background assumed, the scale cuts, the CMB lensing likelihood.
10. For `f(R)` or other screened models: the regime probed (linear
    cosmological, cluster, galactic) and the non-linear prescription.
11. For `E_G`: the source of `Omega_m,0`, the effective-redshift treatment,
    the scale range.
12. For EFT or Horndeski fits: the stability conditions imposed and whether
    the posterior is prior-bounded.
13. No claim that an alternative model "explains DESI" without a
    perturbation-level prediction that distinguishes it from CPL.
