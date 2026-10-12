# Type Ia supernova cosmology — physics and methods

Scope: what a supernova Hubble diagram measures, how distances are standardised,
bias-corrected and turned into a likelihood, and which codes do it.
Snapshot: 2026-10-07

Flags: `[src]` read in the cited paper this session; `[sec]` from a named
secondary source; `[der]` derived here.

## 1. What is measured, and what it constrains

A Type Ia supernova (SN Ia) analysis measures **relative** luminosity distances.
The observable is the distance modulus

    mu = 5 log10( d_L / 10 pc ),   d_L = (1 + z_hel) * D_M(z_HD)

where `z_hel` is the heliocentric redshift (it sets the photon energy and
arrival-rate dilution at the telescope) and `z_HD` is the "Hubble-diagram"
redshift: the CMB-frame redshift corrected for the peculiar velocity of the
host. Using the cosmological redshift alone in both factors is one of the
"common theoretical errors" listed by Davis et al. 2019 (arXiv:1907.12639),
together with adding redshifts instead of multiplying `(1+z)` factors and
using `v = cz`.

Without an external absolute calibration the SN absolute magnitude `M` is
degenerate with `H0`: an unanchored Hubble diagram constrains only the *shape*
of `d_L(z)`, that is `E(z) = H(z)/H0`. The DES-SN5YR analysis states this
explicitly and does not address `M_B` (Vincenzi et al. 2024,
arXiv:2401.02945). Consequences an analyst must hold:

- SN-only constraints are on `Omega_m` (flat LCDM), on a combination of
  `Omega_m` and `w` (flat wCDM), and almost nothing separately on `w_a`.
  Every modern SN-only `w0wa` posterior is prior-limited: DES-Dovekie finds
  `w_a = -7.5 (+3.6/-4.5)` from SNe alone with widened priors `[src]`
  (Popovic et al. 2025, arXiv:2511.07517).
- In flat wCDM the SN degeneracy in the `Omega_m`–`w` plane approximately
  follows a line of constant deceleration parameter `q0` (Camilleri et al.
  2024, arXiv:2406.05048, as restated in arXiv:2511.07517). The Unite analysis
  therefore quotes the non-degenerate combination
  `Q_H(z) = (1/2) [ Omega_m a^-3 + Omega_de (1+3w) a^-3(1+w) ]`,
  with `Q_H = -(a-ddot)/(a H0^2)`, evaluated at `z = 0.2`, and reports its
  systematics budget on `Q_H` rather than on `w` (Camilleri et al. 2026,
  arXiv:2609.05053).
- `H0` from SNe needs either the distance ladder (Cepheid/TRGB hosts; Riess et
  al. 2022, arXiv:2112.04510) or an inverse ladder (BAO + `r_d`). Both belong to
  `cosmo-distance-ladder-h0`.
- With CMB added, `w` in wCDM is pulled toward -1 almost irrespective of the
  low-redshift data; arXiv:2511.07517 flags this when quoting
  `w = -0.995 (+0.019/-0.020)` for SN+BAO+CMB and adds that the datasets are
  not mutually compatible in that model (`log S = -2.87`, 2.5 sigma) `[src]`.

Reviews (history only; neither covers post-2022 methods): Goobar &
Leibundgut 2011 (arXiv:1102.1431); Leibundgut & Sullivan 2018
(doi:10.1007/s11214-018-0491-8).

## 2. Standardisation

### 2.1 The Tripp relation as used today

The width–luminosity relation goes back to Phillips 1993
(doi:10.1086/186970). Current analyses use the SALT parameters and the Tripp
estimator (Tripp 1998, as cited by arXiv:2511.07517), written in DES-Dovekie
as

    mu = m_B + alpha * x1 - beta * c - M_0 - Delta_mu_bias - delta_host

with `m_B = 10.635 - 2.5 log10(x0)` `[src]`, `x1` the stretch, `c` the colour,
`Delta_mu_bias` the simulated selection-bias correction (Section 4) and
`delta_host` the host "mass step", modelled as a sigmoid

    delta_host = gamma * [1 + exp((M_star - S)/tau)]^-1 - gamma/2

with step location `S = 10^10 M_sun` in the baseline `[src]`
(arXiv:2511.07517). Sign convention trap: with this definition a positive
`gamma` means SNe in high-mass hosts are brighter after standardisation.

Measured nuisance parameters (BBC fits; error on last digit in parentheses):

| Analysis | alpha | beta | gamma (mag) | sigma_gray/int | RMS (mag) | Source |
|---|---|---|---|---|---|---|
| Pantheon+ (BS21 scatter model) | 0.148(4) | 3.09(4) | -0.003(7) | 0.00 | 0.171 | arXiv:2202.04077 Table 2 `[src]` |
| Pantheon+ (P21 scatter model) | 0.145(5) | 3.00(5) | 0.019(10) | 0.00 | 0.171 | arXiv:2202.04077 Table 2 `[src]` |
| DES-SN5YR (DES + low-z) | 0.161 ± 0.001 | 3.12 ± 0.03 | 0.038 ± 0.007 | 0.04 | — | arXiv:2401.02945 `[src]` |
| DES-Dovekie | 0.169(3) | 3.14(4) | 0.033(8) | 0.035 | 0.170 | arXiv:2511.07517 `[src]` |
| Unite | 0.159(3) | 3.08(3) | 0.040(6) | 0.037 | 0.177 | arXiv:2609.05053 `[src]` |
| ZTF DR2 siblings (25 pairs, cosmology-independent) | 0.228 ± 0.029 | 3.160 ± 0.191 | — | <= 0.10 (95%) | — | arXiv:2406.01434 `[src]` |
| ZTF DR2 volume-limited | broken, see below | 3.05 ± 0.06 | > 0.12 | — | 0.15 | arXiv:2405.20965, arXiv:2406.02072 `[src]` |

For bias corrections that carry no host-mass dependence (the G10 and C11
scatter models) Pantheon+ finds `gamma ~ 0.05` at 7 sigma `[src]`
(arXiv:2202.04077): the value of `gamma` is a property of the scatter model
and bias correction as much as of the data.

### 2.2 Where the linear Tripp relation is known to fail

- **Stretch is not linear.** ZTF DR2 (volume-limited, z < 0.06, nearly 1000
  SNe) rejects a single `alpha` at 13.4 sigma; a broken relation gives
  `alpha_low = 0.27 ± 0.01` below `x1 = -0.48 ± 0.08` and
  `alpha_high = 0.08 ± 0.01` above `[src]` (Ginolin et al. 2024,
  arXiv:2405.20965). Because the mix of low- and high-stretch SNe drifts with
  redshift (Nicolas et al. 2021, arXiv:2005.09441), a single linear `alpha`
  is effectively redshift dependent.
- **Colour mixes dust and intrinsic colour.** Brout & Scolnic 2021
  (arXiv:2004.10206) model `c` as intrinsic colour plus dust reddening with a
  distribution of `R_V` that differs with host mass; `beta` is then an
  effective quantity. DES-SN5YR treats `beta` as "the observed, effective
  beta" and sets `beta_true = 2.87` in bias-correction simulations `[src]`
  (arXiv:2401.02945).
- **Two populations.** Wojtak & Hjorth (arXiv:2506.22150; Wojtak, Hallgren &
  Hjorth 2026, arXiv:2606.17802) and UNITY1.8 (Rubin et al. 2026,
  arXiv:2601.19854) fit two overlapping populations with different stretch
  and colour distributions and different standardisation relations.

### 2.3 Light-curve / SED models

| Model | Reference | Key facts |
|---|---|---|
| SALT2 | Guy et al. 2007, arXiv:astro-ph/0701828 | Empirical spectral sequence with a colour law; rest-frame 2500–8000 Å `[src]`. Retrained for Pantheon+ with the Fragilistic calibration (arXiv:2112.03864). |
| SALT3 (K21) | Kenworthy et al. 2021, arXiv:2104.07795 | Trained on 1083 SNe with 1207 spectra; 2000–11000 Å; public training code (SALTshaker); SALT2.4 vs SALT3.K21 distance shift between low and high z of 2 ± 14 mmag `[src]`. |
| SALT3.DES5YR | Taylor et al. 2023, arXiv:2301.10644 | SALT2 and SALT3 trained on the same 1083 SNe; model-choice systematic `Delta w = +0.001 ± 0.005` (SN+CMB) `[src]`. |
| SALT3.DOV | arXiv:2506.05471, arXiv:2511.07517 | Retrained on the Dovekie calibration, with many legacy-survey SNe cut from the training sample. |
| BayeSN | Mandel et al. 2022, arXiv:2008.07538 | Hierarchical Bayesian SED model, optical to NIR (0.35–1.8 µm), dust and intrinsic components separated; trained on 79 SNe; total Hubble RMS 0.10 mag with NIR vs 0.14 mag for SALT2/SNooPy on the same sample `[src]`. |
| BayeSN G26 | Grayling et al. 2026, arXiv:2606.19429 | Trained on the SALT cosmology training sample with cross-calibration parameters inside the training; on DES-SN5YR at z < 0.7, sigma_NMAD 0.164 mag vs 0.185 mag for SALT3.Dovekie, without bias corrections `[src]`. Described by its authors as a step toward an end-to-end BayeSN cosmology analysis, not yet one. |

Calibration and model training are coupled: Brout et al. 2022
(arXiv:2112.03864) retrain SALT2 on the new calibration and find that the
change of model plus the change of light-curve calibration shifts distances by
`d mu/dz = 0.04 mag` over 0 < z < 1 `[src]`. An analysis that recalibrates
photometry without retraining the model is not self-consistent.

## 3. Intrinsic scatter and dust models

After standardisation the Hubble residual scatter is 0.15–0.18 mag in current
samples (table above). How the unexplained part is modelled changes the bias
corrections and therefore the cosmology.

| Name | Reference | Content |
|---|---|---|
| Coherent ("gray") scatter | — | One achromatic `sigma_int` added in quadrature. Shown to be inadequate: Kessler et al. 2013 (arXiv:1209.2482) require wavelength-dependent scatter and find that wrong model uncertainties bias distances by up to ~0.05 mag with redshift `[src]`. |
| G10 / C11 | evaluated in arXiv:1209.2482 | Two spectral-variation scatter models (mostly achromatic vs mostly chromatic); the pre-2021 pair of systematics variants. |
| BS21 dust model | arXiv:2004.10206 | Intrinsic colour weakly tied to luminosity plus dust with a wide `R_V` distribution depending on host mass; explains the colour dependence of Hubble scatter (11 sigma detection) and of the mass step; replacing earlier colour models shifts `w` by up to 0.04 `[src]`. |
| P21/P23 (Dust2Dust) | Popovic et al. 2023, arXiv:2112.04456 | Forward-model fit of 4 intrinsic-colour and 8 dust parameters with selection re-weighting; propagated uncertainty `sigma_w = 0.005`, `sigma_H0 = 0.145 km/s/Mpc` `[src]`. Baseline of Pantheon+, DES-SN5YR, DES-Dovekie and Unite. |
| W22 age model | Wiseman et al. 2022, arXiv:2207.05583 | Galaxy-driven forward model tracing progenitor age; an `R_V` step with galaxy age matches the data best; used as a systematic variant ("Model SN age"). |
| Stjörnumál | Popovic et al. 2026, arXiv:2607.28725 | Simulation-based-inference successor to Dust2Dust; on DES-SN5YR finds a smaller `Delta R_V = 0.8` between host-mass bins than earlier SALT-based fits and evidence against two populations at high redshift (log10 Bayes factor +1.9) `[src]`. |

BBC lets a residual `gamma` float even with a dust model, "to test for any
residual brightness step that is not explained by our dust model"
(arXiv:2401.02945). It is non-zero at > 5 sigma in DES-SN5YR `[src]`.

## 4. Selection bias: BBC and BEAMS

A flux-limited survey preferentially keeps bright, blue, slow-declining events
near its limit. The standard treatment is "BEAMS with Bias Corrections" (BBC;
Kessler & Scolnic 2017, arXiv:1610.04677), implemented in SNANA (Kessler et
al. 2009, arXiv:0908.4280):

1. Simulate the survey at catalogue level (cadence, PSF, sky noise, zero
   points, detection and spectroscopic-selection efficiency; Kessler et al.
   2019, arXiv:1811.02379) with an assumed population and scatter model.
2. Fit the simulated light curves exactly as the data, and compute

       Delta_mu_bias = m_B + alpha_true x1 - beta_true c - M0_true - mu_true

   averaged in cells. Dimensionality matters: "1D" corrects in redshift only,
   "5D" in `{z, x1, c, alpha, beta}`, and the current "4D" in
   `{z, c, x1, log10 M_star}` after Popovic et al. 2021 (arXiv:2102.01776),
   which is required once the scatter model depends on host mass.
3. Fit `alpha, beta, gamma, sigma_gray` and distances independently of
   cosmology.
4. Fit cosmology to the bias-corrected Hubble diagram with a covariance matrix.

Sizes: redshift-binned distance biases reach 0.05 mag across the low-z and
DES-SN samples, and up to 0.4 mag for individual events of extreme colour
`[src]` (arXiv:1811.02379). BBC recovered `alpha` and `beta` to 1% and gave a
`w` bias of `0.006 ± 0.002` on 900 000 simulated SNe `[src]`
(arXiv:1610.04677). Ignoring SN–host correlations in the correction biased
`gamma` by ~0.02 mag and `w` by ~0.02; the 4D treatment reduces these to
0.004 mag and 0.006–0.010 `[src]` (arXiv:2102.01776). The measured mass step
depends on the correction: DES-SN3YR finds `gamma = 0.040 ± 0.019` (5D) but
`0.066 ± 0.020` (1D) on the same data `[src]` (Smith et al. 2020,
arXiv:2001.11294).

Bias corrections assume a reference cosmology. Camilleri et al. 2024
(arXiv:2406.05048) show that a reference `Omega_m` wrong by ~0.2 gives a bias
below the statistical error, directed along the SN degeneracy, and give a
procedure to reduce it; this is the paper to cite when fitting non-standard
models to a public bias-corrected Hubble diagram.

**BEAMS** (Kunz, Bassett & Hlozek 2007, arXiv:astro-ph/0611004) replaces a
hard classification by a mixture likelihood weighted by each object's
probability of being a SN Ia; `N` objects of mean purity `P` constrain like
`N P` confirmed SNe Ia. The effective DES-Dovekie sample size is 1684, the
sum of BEAMS probabilities `[src]` (arXiv:2511.07517).

## 5. Hierarchical Bayesian and simulation-based alternatives

| Framework | Reference | Notes |
|---|---|---|
| BAHAMAS | Shariff et al. 2016, arXiv:1510.05954 | Hierarchical model on SALT2 parameters. On the 740 JLA SNe with Planck it gave `Omega_m = 0.399 ± 0.027` and `w = -0.910 ± 0.045` (flat wCDM), 2.8 sigma and 1.6 sigma from the standard analysis, a mass step of 0.055 ± 0.022 mag and `sigma_res = 0.104 ± 0.005` `[src]`. No selection-effect modelling at that stage. |
| UNITY | Rubin et al. 2015, arXiv:1507.01602; UNITY1.5 in arXiv:2311.12098; UNITY1.8 in arXiv:2601.19854 | Outliers, selection effects, non-linear standardisation, unexplained dispersion and calibration in one posterior. Separate `beta` for blue SNe and for red SNe in low- and high-mass hosts. Used for Union3 and Union3.1. |
| Steve | Hinton et al. 2019, arXiv:1811.02381 | Hierarchical model with simulation-characterised selection; `w` bias below 0.03 on average on 60 000 simulated SNe, dependent on the intrinsic-scatter model `[src]`. Cross-check in DES-SN3YR. |
| Two-population BHM | arXiv:2606.17802 | SALT2 parameters plus host mass and colour as a mixture of two SN and two host populations. |
| FlowSN | Boyd et al. 2026, arXiv:2603.11165 | Normalising flow learns the selected-SN likelihood from simulations, used inside a hierarchical model with HMC; on LSST-like SNANA simulations the `w0` posterior is an order of magnitude less biased than "conventional techniques" `[src]`. Simulation result only. |
| CIGaRS | Karchev et al. 2025, arXiv:2508.15899 | Joint SBI of SN and host photometry, progenitor age and metallicity dependence, delay-time distribution and cosmology; demonstrated on ~16 000 mock SNe to z = 0.9 `[src]`. Simulation result only. |

Published cosmology from data comes from BBC (Pantheon, Pantheon+, DES,
Unite) and UNITY (Union3, Union3.1). Two pipelines on overlapping data are
the field's main robustness test; UNITY on Unite is announced as future work
(arXiv:2609.05053).

## 6. Photometric classification

DES-SN5YR is the first flagship result with photometrically classified SNe
and host-galaxy spectroscopic redshifts (DES Collaboration 2024,
arXiv:2401.02929). Ingredients:

- **SuperNNova** (Möller & de Boissière 2019, arXiv:1901.06384): recurrent
  network on light curves; Ia vs non-Ia accuracy 96.92 ± 0.09 % without
  redshift and 99.55 ± 0.06 % with redshift on simulations `[src]`.
- **Contamination budget** (Vincenzi et al. 2023, arXiv:2111.10382): after
  SuperNNova, contamination 0.8–3.5 % and efficiency 97.7–99.5 % depending on
  the non-Ia models; `w` bias < 0.008 and `sigma_w,syst <= 0.004` against an
  expected `sigma_w,stat = 0.039` `[src]`.
- The light-curve fit and the requirement of a valid bias correction already
  act as classifiers: SALT3 fitting and quality cuts reduce non-Ia from ~40 %
  to ~11 % before any classifier `[src]` (arXiv:2401.02945).
- **Host association**: the directional-light-radius method mismatches 1.7 %
  of simulated SNe, giving `Delta w = 0.0013 ± 0.0026` (Qu et al. 2024,
  arXiv:2307.13696) `[src]`.

Unite additionally applies a cut `P_Ia > 0.8` to the DES events `[src]`
(arXiv:2609.05053).

## 7. Covariance and likelihood practice

The cosmology likelihood is Gaussian in distance-modulus residuals,

    chi2 = Delta_mu^T (C_stat + C_syst)^-1 Delta_mu ,

with `Delta_mu_i = mu_i - mu_model(z_i)` and, for an unanchored fit, the
offset `M` (equivalently `H0`) marginalised.

- `C_stat` is diagonal apart from duplicated SNe (same SN observed by several
  surveys) and includes light-curve fit errors, a lensing term
  (`sigma_lens = 0.055 z` in Pantheon+), a redshift term and a
  peculiar-velocity term (`sigma_vpec = 240 km/s` in Pantheon+) `[src]`
  (Brout et al. 2022, arXiv:2202.04077).
- `C_syst` follows Conley et al. 2011 (arXiv:1104.1443), who introduced the
  systematics covariance matrix including the effect of systematics on the
  light-curve model. For each systematic `psi` the whole analysis is rerun and

      C_syst,ij = sum_psi (d Delta_mu_i / d S_psi) (d Delta_mu_j / d S_psi) sigma_psi^2

  (arXiv:2202.04077, Eq. 7). For Pantheon+ this is a 1701 × 1701 matrix.
- **Binned vs unbinned.** JLA, Pantheon and DES-SN3YR used redshift-binned or
  smoothed matrices. Brout, Hinton & Scolnic 2021 (arXiv:2012.05900) show
  that an unbinned matrix lets the data self-calibrate systematics and
  shrinks the systematic error by ~1.5; in Pantheon+ the total systematic on
  `w` is 0.019 unbinned and 0.029 binned in 20 bins `[src]`
  (arXiv:2202.04077). Kessler, Vincenzi & Armstrong 2023 (arXiv:2306.05819)
  extend this to photometric samples through BBC, with a rebinning in
  redshift, colour and stretch to keep the matrix tractable.
- **Budgets are not additive.** DES-SN5YR and DES-Dovekie evaluate each
  systematic alone ("leave-one-out" on the uncertainty, "add-one-in" on the
  shift); the quadrature sum exceeds the total because correlations cancel
  inside the full matrix (arXiv:2401.02945; arXiv:2511.07517). Do not sum the
  rows of those tables.

**Model-comparison conventions** differ between papers and are a recurring
source of confusion:

- DESI quotes a frequentist significance from `Delta chi2_MAP` between
  `w0waCDM` and LCDM (2 extra parameters) (DESI Collaboration 2025,
  arXiv:2503.14738). DES-Dovekie quotes the same statistic (`Delta chi2 =
  -13.5`, 3.2 sigma) *and* the Bayesian evidence (`Delta log Z = -1.7`, odds
  ~5:1, "weak") for the same data `[src]` (arXiv:2511.07517). Unite quotes
  both the MAP-based (3.3 sigma) and maximum-likelihood-based (3.1 sigma)
  numbers `[src]` (arXiv:2609.05053).
- Dataset compatibility is checked with the Suspiciousness statistic
  `log S = log R - log I` before combining (arXiv:2511.07517).
- **Figure of merit.** Unite uses `FoM = 1/sqrt(det Cov(w0, wa))` and
  reports 315 `[src]` (arXiv:2609.05053). Union3 uses the original DETF
  definition, the inverse area of the 95.4 % contour, which is smaller by a
  factor `6.18 pi = 19.4` `[src]` (Rubin et al. 2023, arXiv:2311.12098).
  Never compare FoM values across papers without checking which one is meant.
- Compressed products are not likelihood-equivalent to the full sample unless
  shown to be; the public Union3 "spline-interpolated distance moduli"
  posterior carries a non-flat prior (see "Not verified").

## 8. Redshifts and peculiar-velocity corrections

The use of SNe as velocity tracers (growth rate, bulk flow) belongs to
`cosmo-peculiar-velocities`; the likelihood framework for that is the one of
Ravoux et al. 2025 (arXiv:2501.16852). Here peculiar velocities are a
nuisance.

- **Frame.** Heliocentric redshifts are converted to the CMB frame with the
  exact multiplicative formula, then corrected for the host peculiar velocity
  predicted from a density-field reconstruction. Carr et al. 2022
  (arXiv:2112.01471) reviewed 2821 SN redshifts for Pantheon+, fixing 5
  wrong or missing heliocentric corrections, 44 wrong or missing coordinates
  and 1200 missing uncertainties; the net effect is `Delta H0 = -0.11
  km/s/Mpc` and `Delta w = -0.001` `[src]`.
- **Flow model.** Peterson et al. 2022 (arXiv:2110.03487), with 584 low-z
  SNe, find the best reduction of Hubble scatter from combining
  coherent-flow corrections (2M++ based) with galaxy-group averaging (0.167
  to 0.157 mag relative scatter); the correction raises `H0` by ~0.4 km/s/Mpc
  relative to raw CMB-frame redshifts; residual systematics are 0.06–0.11
  km/s/Mpc in `H0` and 0.02–0.03 in `w` `[src]`.
- **Correlated velocities.** Davis et al. 2011 (arXiv:1012.2912) introduced
  the velocity covariance matrix, which down-weights nearby SNe as "a
  graduated version of the usual sharp low-redshift cut"; ignoring the CMB
  dipole correction shifts `w` by ~0.04, and ignoring coherent velocities by
  ~2 % `[src]`.
- **Low-redshift cut.** DES-SN5YR and DES-Dovekie keep only `z > 0.025`;
  Unite removes this cut so that the same Hubble diagram can be anchored for
  `H0`, and tests cuts at `z > 0.0233` and `z > 0.1` `[src]`
  (arXiv:2609.05053). A redshift systematic of `Delta z = 10^-4` (scaled by
  `sqrt(1/6)`) is carried in the Unite budget `[src]`.

## 9. Calibration chain

1. **Flux scale**: HST CALSPEC standards; a 2020 CALSPEC update changed the
   fundamental calibration by of order 1.5 % over 4000 Å `[src]`
   (arXiv:2112.03864). The CALSPEC uncertainty carried in DES-SN5YR and
   Unite is 5 mmag per 7000 Å `[src]` (arXiv:2401.02945; arXiv:2609.05053).
2. **Per-survey tertiary stars** observed with each SN instrument.
3. **Cross-calibration** of all systems against a uniform all-sky stellar
   catalogue: Supercal (Scolnic et al. 2015, arXiv:1508.05361) used
   Pan-STARRS1; Fragilistic (arXiv:2112.03864) solves 25 systems and 105
   filters simultaneously and outputs a calibration covariance; Dovekie
   (Popovic et al. 2025, arXiv:2506.05471) is the open-source successor,
   using PS1 and Gaia, fitting filter-transmission shifts with uncertainties
   for the first time, and adding faint DA white dwarfs as an absolute tie.
4. **DA white-dwarf network**: faint all-sky DA white dwarfs with modelled
   SEDs tied to the CALSPEC primaries (Axelrod et al. 2023,
   doi:10.3847/1538-4357/acd333).
5. **Propagation**: calibration variants are propagated *simultaneously*
   through model retraining and light-curve fitting (10 covariance
   realisations of SALT3 surfaces and zero points in Unite `[src]`,
   arXiv:2609.05053).

## 10. Blinding practice

- JLA: the SNLS–SDSS inter-calibration was "performed blindly with respect to
  the cosmology analysis" (Betoule et al. 2014, arXiv:1401.4064).
- UNITY was validated on simulations before being run on data (arXiv:1507.01602).
- Union3: per-sample absolute magnitudes were fitted with the cosmology fixed
  to flat LCDM (`Omega_m = 0.3`) and the per-sample differences removed, so
  cosmological constraints stayed hidden; the choice of models and external
  datasets was also made blind (arXiv:2311.12098). A prior-bound oversight
  found after unblinding was reported and left unchanged (effect on
  `Omega_m` about 0.007).
- DES-SN5YR, DES-Dovekie and Unite: analysis validated on simulations and
  pre-registered unblinding criteria (arXiv:2401.02945; arXiv:2511.07517
  Section 6.3; arXiv:2609.05053 Section 5.2).
- Lensed-SN `H0` measurements are blinded by construction: Refsdal (Kelly et
  al. 2023, arXiv:2305.06367), SN H0pe with a live unblinding (Pascale et al.
  2024, arXiv:2403.18902), SN Encore double-blind (Pierel et al. 2025,
  arXiv:2509.12301).

A reanalysis of an already-unblinded sample (DES-Dovekie, Union3.1, Unite)
cannot be blind in the same sense; DES-Dovekie first reproduces DES-SN5YR.

## 11. Public codes and pipelines

| Code | What it does | Reference |
|---|---|---|
| SNANA | Survey simulation, light-curve fitting, BBC, fast cosmology fitter (`wfit`) | arXiv:0908.4280; arXiv:1610.04677 |
| SALTshaker / SALT3 | Public SALT training code and model; integrated in sncosmo and SNANA | arXiv:2104.07795 |
| BayeSN | GPU hierarchical SED model, <https://github.com/bayesn/bayesn> | arXiv:2008.07538; Grayling et al. 2024, arXiv:2401.08755 |
| UNITY | Unified Bayesian framework (released with Union3) | arXiv:1507.01602; arXiv:2311.12098 |
| Steve | Hierarchical model with simulated selection | arXiv:1811.02381 |
| SuperNNova | Photometric classifier | arXiv:1901.06384 |
| Dovekie | Cross-calibration, <https://github.com/bap37/Dovekie/> | arXiv:2506.05471 |
| Dust2Dust / Stjörnumál | Dust and intrinsic-colour population inference | arXiv:2112.04456; arXiv:2607.28725 |
| FlowSN | SBI likelihood for selection effects | arXiv:2603.11165 |
| CosmoSIS + Nautilus | Sampling and evidence in Unite | as used in arXiv:2609.05053 |

## 12. Conventions and where the community is split

- **Sample names.** "DES-SN5YR", "DESY5", "DES5Y": the same 2024 sample;
  "DES-Dovekie" (2025) supersedes it. "Union3.1" (2026) supersedes "Union3".
  "Unite" (2026) is Pantheon+ plus DES on the Dovekie calibration.
- **Counting.** Pantheon+ is 1701 light curves of 1550 distinct SNe
  (arXiv:2112.03863). DES-SN5YR is 1635 DES events plus 194 low-z, of which
  1499 DES events have `P_Ia > 0.5` (arXiv:2609.05053).
- **Mass-step sign and location**: step at 10^10 M_sun in BBC analyses;
  10^10.2 is a Unite systematic variant.
- **Host property**: global mass (BBC, UNITY) vs local colour or sSFR (ZTF,
  SNfactory); see `systematics.md`.
- BBC vs hierarchical vs SBI, and dust vs intrinsic step: `open-questions.md`.

## Not verified

- Tripp 1998 and Fitzpatrick 1999 are cited only through arXiv:2511.07517.
- The non-flat prior of the public Union3 spline posterior comes from an
  abstract read this session (A. G. Kim 2024), not listed in `sources.tsv`.
- Pippin (DES pipeline manager, named in arXiv:2511.07517): paper not fetched.
- The low-redshift cut of the Pantheon+ cosmology fit was not located.
