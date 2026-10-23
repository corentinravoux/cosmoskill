# Type Ia supernova cosmology — physics and methods

Scope: what a supernova Hubble diagram measures, how distances are standardised,
bias-corrected and turned into a likelihood, and which codes do it.
Snapshot: 2026-10-13

Flags: `[src]` read in the cited paper this session; `[sec]` from a named
secondary source; `[der]` derived here.

## 1. What is measured, and what it constrains
<!-- key: what-is-measured-and-what-it-constrains -->

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
<!-- key: standardisation -->

### 2.1 The Tripp relation as used today
<!-- key: the-tripp-relation-as-used-today -->

The width–luminosity relation goes back to Phillips 1993
(doi:10.1086/186970). Hamuy et al. 1996 (arXiv:astro-ph/9609059) confirmed
it on 29 Calán/Tololo SNe, with a scatter of 0.13–0.17 mag depending on the
band `[src]`. The multicolour light-curve shape method was trained on nine
SNe and gave 0.12 mag dispersion on twenty others (Riess, Press & Kirshner
1996, arXiv:astro-ph/9604143); the width–luminosity correction narrowed the
peak-magnitude dispersion of the first seven high-redshift SNe from 0.27 to
0.19 mag (Perlmutter et al. 1997, arXiv:astro-ph/9608192) `[src]`. Colour
entered as a reddening estimate from late-time `B−V` (Phillips et al. 1999,
arXiv:astro-ph/9907052) and as a second luminosity parameter beside the
decline rate, fitted jointly (Tripp & Branch 1999, arXiv:astro-ph/9904347). Current analyses use the SALT parameters and
the Tripp estimator (Tripp 1998, as cited by arXiv:2511.07517), written in
DES-Dovekie as

    mu = m_B + alpha * x1 - beta * c - M_0 - Delta_mu_bias - delta_host

with `m_B = 10.635 - 2.5 log10(x0)` `[src]`, `x1` the stretch, `c` the colour,
`Delta_mu_bias` the simulated selection-bias correction (Section 4) and
`delta_host` the host "mass step", modelled as a sigmoid

    delta_host = gamma * [1 + exp((M_star - S)/tau)]^-1 - gamma/2

with step location `S = 10^10 M_sun` in the baseline `[src: Eqs. 1–2]`
(arXiv:2511.07517). Sign convention trap: with this definition a positive
`gamma` means SNe in high-mass hosts are brighter after standardisation.

The same relation as the other analyses print it:

| Analysis | Equation as printed | Place |
|---|---|---|
| JLA | `mu = m_B* − (M_B − alpha X1 + beta C)`, with `M_B = M_B^1` below a host mass of `10^10 M_sun` and `M_B^1 + Delta_M` above; the two-parameter description is referred to Tripp 1998 | arXiv:1401.4064 `[src: Eqs. 4–5]` |
| Pantheon+ | `mu = m_B + alpha x1 − beta c − M − delta_bias + delta_host`, `m_B ≡ −2.5 log10(x0)`, same sigmoid `delta_host`; a footnote says earlier papers wrote `+delta_bias` | arXiv:2202.04077 `[src: Eqs. 1–2]` |
| DES-SN5YR | `mu_obs = m_x + alpha x1 − beta c + gamma G_host − M − Delta_mu_bias`, `G_host = +1/2` if `P > P_step`, `−1/2` otherwise; `P` is stellar mass (step at `10^10 M_sun`) or rest-frame `u−r` (step at 1) | arXiv:2401.02945 `[src: Eqs. 1–2]` |
| UNITY1.5 (Union3) | `m_B^model = −alpha x1^true + beta_B c_B^true + [beta_RL (1 − P) + beta_RH P] c_R^true − delta(0) P + M_B + mu(z)`, `P` the probability that the host behaves as a high-mass low-redshift host; latent `x1^true`, `c_B^true` (Gaussian core), `c_R^true` (exponential red tail) are marginalised for every SN | arXiv:2311.12098 `[src: Eq. 5, Sect. IV.1.1]` |
| Distance error (BBC) | `sigma_mu^2 = f(z, c, M_star) sigma_meas^2 + sigma_floor^2(z, c, M_star) + sigma_lens^2 + sigma_z^2 + sigma_vpec^2`, `sigma_floor^2 = sigma_scat^2(z, c, M_star) + sigma_gray^2`; `sigma_gray` is fitted so that the reduced `chi2` is 1 and is zero if the simulated scatter model is right | arXiv:2202.04077 `[src: Eqs. 3–4]`; arXiv:2401.02945 `[src: Eqs. 8–9]` |

The `delta_host` term enters Pantheon+ Eq. 1 with `+` and DES-Dovekie Eq. 1
with `−`, for the same sigmoid: check the release before applying a step by
hand. `alpha`, `beta`, `gamma` are fitted independently of cosmology, in 20
logarithmic redshift bins whose offsets absorb it and serve this fit only
`[src: Sect. III.3]` (arXiv:2401.02945), after Marriner et al. 2011
(arXiv:1107.4631), who replaced the single scatter parameter by a covariance
matrix and found `beta = 3.19 (+0.14/−0.24)` on SDSS-II, excluding the Milky
Way dust value 4.1 at 98 % `[src]`.

Measured nuisance parameters (BBC fits; error on last digit in parentheses):

| Analysis | alpha | beta | gamma (mag) | sigma_gray/int | RMS (mag) | Source |
|---|---|---|---|---|---|---|
| Pantheon+ (BS21 scatter model) | 0.148(4) | 3.09(4) | -0.003(7) | 0.00 | 0.171 | arXiv:2202.04077 Table 2 `[src]` |
| Pantheon+ (P21 scatter model) | 0.145(5) | 3.00(5) | 0.019(10) | 0.00 | 0.171 | arXiv:2202.04077 Table 2 `[src]` |
| DES-SN5YR (DES + low-z) | 0.161 ± 0.001 | 3.12 ± 0.03 | 0.038 ± 0.007 | 0.04 | — | arXiv:2401.02945 `[src: Sect. V.2]` |
| DES-Dovekie | 0.169(3) | 3.14(4) | 0.033(8) | 0.035 | 0.170 | arXiv:2511.07517 `[src: Sect. 9]` |
| Unite | 0.159(3) | 3.08(3) | 0.040(6) | 0.037 | 0.177 | arXiv:2609.05053 `[src: Sect. 6]` |
| ZTF DR2 siblings (25 pairs, cosmology-independent) | 0.228 ± 0.029 | 3.160 ± 0.191 | — | <= 0.10 (95%) | — | arXiv:2406.01434 `[src: abstract]` |
| ZTF DR2 volume-limited | broken, see below | 3.05 ± 0.06 | > 0.12 | — | 0.15 | arXiv:2405.20965, arXiv:2406.02072 `[src]` |

For bias corrections that carry no host-mass dependence (the G10 and C11
scatter models) Pantheon+ finds `gamma ~ 0.05` at 7 sigma `[src]`
(arXiv:2202.04077): the value of `gamma` is a property of the scatter model
and bias correction as much as of the data.

### 2.2 Where the linear Tripp relation is known to fail
<!-- key: where-the-linear-tripp-relation-is-known-to-fail -->

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
<!-- key: light-curve-sed-models -->

| Model | Reference | Key facts |
|---|---|---|
| SALT | Guy et al. 2005, arXiv:astro-ph/0506583 | First version: luminosity modelled against phase, wavelength, one shape and one colour parameter, trained on nearby SNe; distances from rest-frame U and B alone with 0.16 ± 0.05 mag dispersion `[src: abstract]`. |
| SALT2 | Guy et al. 2007, arXiv:astro-ph/0701828 | Flux model `F(p, lambda) = x0 [M0(p, lambda) + x1 M1(p, lambda) + ...] exp[c CL(lambda)]`, with `p` the phase, `M0` the mean spectral sequence, `M1` its first variation, `CL` the mean colour law and `c = (B−V)_max − <B−V>`; equivalent to a principal-component decomposition apart from the colour term `[src: Eq. 1, Sect. 2]`. Rest-frame 2500–8000 Å `[src]`. Retrained for Pantheon+ with the Fragilistic calibration (arXiv:2112.03864). |
| SALT3 (K21) | Kenworthy et al. 2021, arXiv:2104.07795 | Trained on 1083 SNe with 1207 spectra; 2000–11000 Å; public training code (SALTshaker); SALT2.4 vs SALT3.K21 distance shift between low and high z of 2 ± 14 mmag `[src: abstract]`. |
| SALT3.DES5YR | Taylor et al. 2023, arXiv:2301.10644 | SALT2 and SALT3 trained on the same 1083 SNe; model-choice systematic `Delta w = +0.001 ± 0.005` (SN+CMB) `[src: abstract]`. |
| SALT3.DOV | arXiv:2506.05471, arXiv:2511.07517 | Retrained on the Dovekie calibration, with many legacy-survey SNe cut from the training sample. |
| MLCS2k2, SNooPy | Jha et al. 2007, arXiv:astro-ph/0612666; Burns et al. 2011, arXiv:1010.4040 | Non-SALT fitters. MLCS2k2: 133 nearby SNe, intrinsic dispersion below 7 % in distance, separate intrinsic colour and dust `[src]`. SNooPy: uBVgriYJH templates from 24 CSP SNe `[src]`. |
| BayeSN | Mandel et al. 2022, arXiv:2008.07538 | Hierarchical Bayesian SED model, optical to NIR (0.35–1.8 µm), dust and intrinsic components separated; trained on 79 SNe; total Hubble RMS 0.10 mag with NIR vs 0.14 mag for SALT2/SNooPy on the same sample `[src: abstract]`. |
| BayeSN G26 | Grayling et al. 2026, arXiv:2606.19429 | Trained on the SALT cosmology training sample with cross-calibration parameters inside the training; on DES-SN5YR at z < 0.7, sigma_NMAD 0.164 mag vs 0.185 mag for SALT3.Dovekie, without bias corrections `[src: abstract]`. Described by its authors as a step toward an end-to-end BayeSN cosmology analysis, not yet one. |

Calibration and model training are coupled: Brout et al. 2022
(arXiv:2112.03864) retrain SALT2 on the new calibration and find that the
change of model plus the change of light-curve calibration shifts distances by
`d mu/dz = 0.04 mag` over 0 < z < 1 `[src]`. An analysis that recalibrates
photometry without retraining the model is not self-consistent.

## 3. Intrinsic scatter and dust models
<!-- key: intrinsic-scatter-and-dust-models -->

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
<!-- key: selection-bias-bbc-and-beams -->

A flux-limited survey preferentially keeps bright, blue, slow-declining events
near its limit. The standard treatment is "BEAMS with Bias Corrections" (BBC;
Kessler & Scolnic 2017, arXiv:1610.04677), implemented in SNANA (Kessler et
al. 2009, arXiv:0908.4280):

1. Simulate the survey at catalogue level (cadence, PSF, sky noise, zero
   points, detection and spectroscopic-selection efficiency; Kessler et al.
   2019, arXiv:1811.02379) with an assumed population and scatter model.
   The parent stretch and colour populations are themselves fitted: Scolnic
   & Kessler 2016 (arXiv:1603.01559) found Hubble-residual biases up to 0.3
   mag against colour (10 sigma) in 920 SNe when they are ignored `[src]`.
2. Fit the simulated light curves exactly as the data, and compute

       Delta_mu_bias = m_B + alpha_true x1 - beta_true c - M0_true - mu_true

   averaged in cells. Dimensionality matters: "1D" corrects in redshift only,
   "5D" in `{z, x1, c, alpha, beta}`, and the current "4D" in
   `{z, c, x1, log10 M_star}` after Popovic et al. 2021 (arXiv:2102.01776),
   which is required once the scatter model depends on host mass.
3. Fit `alpha, beta, gamma, sigma_gray` and distances independently of
   cosmology.
4. Fit cosmology to the bias-corrected Hubble diagram with a covariance matrix.

Simulated selection corrections predate BBC: for SNLS3, Perrett et al. 2010
(arXiv:1006.2254) found Malmquist and spectroscopic-sampling effects from
z ~ 0.6, with a clear shift of the mean magnitude above z = 0.75 `[src]`.
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

In the original BBC each fitted parameter is corrected, `mu* = (m_B − d_mB) +
alpha (x1 − d_x1) − beta (c − d_c) − M0`, by interpolation in
`{z, x1, c, alpha, beta}` over 500 000 simulated events (cells of 0.05, 0.50,
0.05 in `z`, `x1`, `c`); the event likelihood adds a contaminant term with a
free scale `S_CC` `[src: Eqs. 6 and 11, Sect. V.2]` (arXiv:1610.04677). The
bias term as printed for the 4D scheme is `Delta_mu_bias = m_x + alpha_true x1
− beta_true c + gamma_true G_host + M_B_true − mu_true` `[src: Eq. 7]`
(arXiv:2401.02945); with a dust-based simulation `beta_true` is not defined
and an effective value is assumed. A wrong (intrinsic) `beta` was used there
in Pantheon+ and corrected before DES-SN5YR `[src: Sect. 4.5]` (arXiv:2609.05053).

Bias corrections assume a reference cosmology: with `w_ref = −1` the `w` bias
is −0.003(4), −0.017(4), −0.044(4) for true `w` = −1, −0.9, −0.8
`[src: Table 4]` (arXiv:1610.04677). Camilleri et al. 2024 (arXiv:2406.05048)
show that a reference `Omega_m` wrong by ~0.2 gives a bias below the
statistical error, directed along the SN degeneracy, and give a procedure to
reduce it; this is the paper to cite when fitting non-standard models to a
public bias-corrected Hubble diagram.

**BEAMS** (Kunz, Bassett & Hlozek 2007, arXiv:astro-ph/0611004) replaces a
hard classification by a mixture likelihood weighted by each object's
probability of being a SN Ia; `N` objects of mean purity `P` constrain like
`N P` confirmed SNe Ia. Applied to data: 792 SDSS-II photometric SNe
with host redshifts, contour area in (`Omega_m`, `Omega_Lambda`) three times
smaller than with the 297 confirmed ones `[src]` (Hlozek et al. 2012,
arXiv:1111.5328). The effective DES-Dovekie sample size is 1684, the
sum of BEAMS probabilities `[src]` (arXiv:2511.07517). In DES the
likelihood is `prod_i (L_Ia,i + L_CC,i)` with `L_Ia = P_Ia D_Ia` and `L_CC =
(1 − P_Ia) D_CC`, the contaminant term `D_CC` being taken from core-collapse
simulations `[src: Eqs. 3–5]` (arXiv:2401.02945).

### 4.1 What each main analysis did
<!-- key: what-each-main-analysis-did -->

| | Pantheon+ (arXiv:2202.04077) | DES-SN5YR (arXiv:2401.02945) | DES-Dovekie (arXiv:2511.07517) | Union3 and Union3.1 (arXiv:2311.12098; arXiv:2601.19424) | Unite (arXiv:2609.05053) |
|---|---|---|---|---|---|
| Light-curve model | SALT2-B22, retrained on Fragilistic, fitted in SNANA `[src: Sect. II.1]` | SALT3.DES5YR: K21 training set, Fragilistic, observer-frame U band removed `[src: arXiv:2609.05053 Sect. 4.2]` | SALT3.DOV, retrained on Dovekie with many legacy-survey SNe cut `[src: Sect. 3.1]` | SALT3, Taylor et al. version, in SNCosmo `[src: Sect. III.1]` | SALT3.UNITE: K21 training set without U band, Dovekie calibration `[src: Sect. 4.2]` |
| Sample | 1701 light curves of 1550 SNe, 0.001 < z < 2.26 `[src]` | 3868 → 1829 (194 low-z + 1635 DES; 1499 DES with `P_Ia > 0.5`) `[src: Table 4]` | 3991 → 1820 (197 low-z + 1623 DES) `[src: Table 5]` | 2711 → 2087 `[src: Table 1]` | 5271 → 2884 `[src: Table 3]` |
| Cuts | an epoch before 5 rest-frame days after peak, peak-date error < 2 d, `abs(x1) < 3`, `abs(c) < 0.3`, `sigma_x1 < 1.5`, valid bias correction (10 light curves lost), present in all 40 systematic variants (60 lost), Chauvenet `[src: arXiv:2112.03863 Sect. II.2]`; 151 SNe observed by several surveys, all but one at z < 0.1, agree to 0.102 mag against 0.218 ± 0.011 for random pairs `[src: arXiv:2112.03863 Sect. III.2]` | `abs(x1) < 3`, `abs(c) < 0.3`, `sigma_x1 < 1`, `sigma_tpeak < 2 d`, fit probability > 0.001, detected host with its own redshift, Chauvenet, valid bias correction, common to all variants `[src: Table 4]` | same with `sigma_x1 < 1.15` `[src: Table 5]` | five points in two filters, `abs(x1) + sigma_x1 < 5`, `abs(c) < 0.3`, `sigma_c < 0.2`, Milky Way `E(B−V) < 0.3`, known peculiar events out `[src: Sect. III.2.3]` | DES-SN5YR cuts with `sigma_x1 < 1.15`, Milky Way `E(B−V) < 0.2`, `P_Ia(SCONE) > 0.8` `[src: Table 3]` |
| Low redshift | no cut in the sample; `z > 0.01` in cosmology fits without SH0ES `[src: Fig. 16 caption]`; `sigma_vpec = 240 km/s` `[src: Sect. III.1.3]` | CfA3, CfA4, CSP DR3, Foundation at `z > 0.025`; 1 % error floor on their photometry (2 % for Foundation z band) `[src: Sect. II.2]` | same samples, `z > 0.025` `[src: Sect. 2.2]` | `z_CMB > 0.01`; linear-theory velocity covariance at `z_CMB < 0.1` sampled with the rest `[src: Table 1, Sect. IV.4.5]` | no redshift cut `[src: Table 3]`; the volumetric redshift bias at z < 0.01 is modelled in the bias correction, and a cut at 0.01 changes nothing `[src: Sect. C.2]` |
| Selection bias | BBC: 4D cells for BS21/P21, 7D for G10/C11 `[src: Table 5]` | BBC4D in `{z, x1, c, log M_star}`, `beta_true = 2.87` `[src: Sect. III.4]` | BBC4D `[src: Eq. 3]` | no correction term: error-function selection in observer-frame magnitude, survey depths marginalised `[src: Sect. IV.5]` | BBC version 4 `[src: Sect. 4.5]` |
| Scatter model | BS21 dust parameters; `x1` populations of Popovic et al. 2021 `[src: Sect. III.3.2]` | BS21 framework with forward-modelled parameters (P21, later called P23) `[src: arXiv:2609.05053 Sect. 4.3]` | P23 `[src: Sect. 3.2]` | per-dataset unexplained dispersion, shared between `m_B`, `x1`, `c` by sampled fractions `[src: Sect. IV.3]` | P23, not refitted `[src: Sect. 4.3]` |
| Non-Ia | none: probability set to 0 `[src: Sect. II.1]` | BEAMS with SuperNNova `[src: Sect. III.3]` | as DES-SN5YR | outlier mixture, fitted fraction `[src: Sect. IV.6]` | probability cut, no BEAMS variants `[src: Sect. 4.9]` |
| Covariance | `C_stat` with off-diagonal terms for duplicated SNe `[src: Eq. 5]` plus unbinned `C_syst` `[src: Eq. 7]` | diagonal `C_stat` plus unbinned `C_syst = sum_S Delta_mu_S^i Delta_mu_S^j W_S^2` `[src: Eq. 11]` | as DES-SN5YR | none: calibration, selection and population parameters are sampled; UNITY1.7 in Union3.1 fixes an outlier prior and fits the step location, `10.115 (+0.044/−0.053)` `[src: arXiv:2601.19424 Sect. VI, Table 3]` | `C_stat` with duplicates; lensing term from a per-SN estimator `[src: Sect. 4.9]` |
| Validation and blinding | binned residuals hidden and chains shifted `[src: Sect. II.3]`; 20 simulated samples give `w = −1.012 ± 0.011` (BS21) and `−0.983 ± 0.015` (G10) for input −1 `[src: Sect. III.3.4]` | 25 simulated samples; results unblinded in arXiv:2401.02929 `[src: Sect. VII.1]` | reproduce DES-SN5YR with the old errors restored; 25 simulations; data–simulation reduced `chi2` in 0.7–3.0 `[src: Sect. 6.3]` | per-sample magnitudes at fixed cosmology; 100 simulated realisations `[src: Sect. IV.7.1]` | 25 simulations: `Omega_m` bias `0.002 ± 0.002` (flat LCDM), `w` bias `0.01 ± 0.03`; four changes after unblinding, largest shift 0.3 sigma `[src: Sect. 5.2]` |

## 5. Hierarchical Bayesian and simulation-based alternatives
<!-- key: hierarchical-bayesian-and-simulation-based -->

| Framework | Reference | Notes |
|---|---|---|
| Hierarchical model on SALT-II fits | March et al. 2011, arXiv:1102.3237 | On simulations: tighter constraints than the `chi2` method more than 90 % of the time, statistical bias reduced by a factor 2–3, and a posterior for the intrinsic dispersion (`0.13 ± 0.01 mag` on the data of the time) `[src]`. An earlier hierarchical framework, for near-infrared light curves with Gibbs sampling, is Mandel et al. 2009 (arXiv:0908.0536): intrinsic `sigma(M_H) = 0.11 ± 0.03 mag` `[src]`. |
| BAHAMAS | Shariff et al. 2016, arXiv:1510.05954 | Hierarchical model on SALT2 parameters. On the 740 JLA SNe with Planck it gave `Omega_m = 0.399 ± 0.027` and `w = -0.910 ± 0.045` (flat wCDM), 2.8 sigma and 1.6 sigma from the standard analysis, a mass step of 0.055 ± 0.022 mag and `sigma_res = 0.104 ± 0.005` `[src: abstract]`. No selection-effect modelling at that stage. |
| UNITY | Rubin et al. 2015, arXiv:1507.01602; UNITY1.5 in arXiv:2311.12098; UNITY1.8 in arXiv:2601.19854 | Outliers, selection effects, non-linear standardisation, unexplained dispersion and calibration in one posterior. Separate `beta` for blue SNe and for red SNe in low- and high-mass hosts. Used for Union3 (UNITY1.5) and Union3.1 (UNITY1.7 `[src: arXiv:2601.19424 Sect. VI]`). |
| Steve | Hinton et al. 2019, arXiv:1811.02381 | Hierarchical model with simulation-characterised selection; `w` bias below 0.03 on average on 60 000 simulated SNe, dependent on the intrinsic-scatter model `[src: abstract]`. Cross-check in DES-SN3YR. |
| Two-population BHM | arXiv:2606.17802 | SALT2 parameters plus host mass and colour as a mixture of two SN and two host populations. |
| FlowSN | Boyd et al. 2026, arXiv:2603.11165 | Normalising flow learns the selected-SN likelihood from simulations, used inside a hierarchical model with HMC; on LSST-like SNANA simulations the `w0` posterior is an order of magnitude less biased than "conventional techniques" `[src]`. Simulation result only. |
| CIGaRS | Karchev et al. 2025, arXiv:2508.15899 | Joint SBI of SN and host photometry, progenitor age and metallicity dependence, delay-time distribution and cosmology; demonstrated on ~16 000 mock SNe to z = 0.9 `[src: abstract]`. Simulation result only. |

Published cosmology from data comes from BBC (Pantheon, Pantheon+, DES,
Unite) and UNITY (Union3, Union3.1). Two pipelines on overlapping data are
the field's main robustness test; UNITY on Unite is announced as future work
(arXiv:2609.05053).

## 6. Photometric classification
<!-- key: photometric-classification -->

DES-SN5YR is the first flagship result with photometrically classified SNe
and host-galaxy spectroscopic redshifts (DES Collaboration 2024,
arXiv:2401.02929). Ingredients:

- **Benchmark**: the Supernova Photometric Classification Challenge, a
  simulated DES-like mix of Ia, Ibc and II with a confirmed training subset;
  13 entries from 10 groups, all performing better on the training subset
  than on the unconfirmed sample `[src]` (Kessler et al. 2010,
  arXiv:1008.1024). Lochner et al. 2016 (arXiv:1603.00882) compared feature
  extractions and learning algorithms on it.
- **SuperNNova** (Möller & de Boissière 2019, arXiv:1901.06384): recurrent
  network on light curves; Ia vs non-Ia accuracy 96.92 ± 0.09 % without
  redshift and 99.55 ± 0.06 % with redshift on simulations `[src: abstract]`.
- **Contamination budget** (Vincenzi et al. 2023, arXiv:2111.10382): after
  SuperNNova, contamination 0.8–3.5 % and efficiency 97.7–99.5 % depending on
  the non-Ia models; `w` bias < 0.008 and `sigma_w,syst <= 0.004` against an
  expected `sigma_w,stat = 0.039` `[src: abstract]`.
- The light-curve fit and the requirement of a valid bias correction already
  act as classifiers: SALT3 fitting and quality cuts reduce non-Ia from ~40 %
  to ~11 % before any classifier `[src]` (arXiv:2401.02945).
- **Host association**: the directional-light-radius method mismatches 1.7 %
  of simulated SNe, giving `Delta w = 0.0013 ± 0.0026` (Qu et al. 2024,
  arXiv:2307.13696) `[src]`.

The DES photometric sample itself (SuperNNova ensembles, more than 98 %
accuracy on simulations): 1863 SNe Ia, 1484 cosmology-grade at 0.07 < z <
1.14 `[src]` (Möller et al. 2022, arXiv:2201.11142). Unite additionally
applies a cut `P_Ia > 0.8` to the DES events, with probabilities from SCONE
`[src: Table 3]` (arXiv:2609.05053), a convolutional network on
wavelength–time flux images that needs no redshift (Qu et al. 2021,
arXiv:2106.04370).

## 7. Covariance and likelihood practice
<!-- key: covariance-and-likelihood-practice -->

The cosmology likelihood is Gaussian in distance-modulus residuals,

    chi2 = Delta_mu^T (C_stat + C_syst)^-1 Delta_mu ,

with `Delta_mu_i = mu_i - mu_model(z_i)` and, for an unanchored fit, the
offset `M` (equivalently `H0`) marginalised.

- `C_stat` is diagonal apart from duplicated SNe (same SN observed by several
  surveys) and includes light-curve fit errors, a lensing term
  (`sigma_lens = 0.055 z` in Pantheon+), a redshift term and a
  peculiar-velocity term (`sigma_vpec = 240 km/s` in Pantheon+)
  `[src: Eqs. 3 and 5, Sect. III.1.3]` (Brout et al. 2022, arXiv:2202.04077).
  The `0.055 z` term is attributed to Jönsson et al. 2010 (arXiv:1002.1374)
  `[sec, arXiv:2202.04077 Sect. II.1]`; Holz & Linder 2005
  (arXiv:astro-ph/0412173) showed that lensing cuts the effective number of
  SNe threefold at z = 1.5 for a 10 % intrinsic flux dispersion `[src]`.
  Unite replaces `0.055 z` by the error of a per-SN lensing estimator, and
  notes that the simulated lensing distributions used before had a scatter
  about 30 % too low `[src: Sects. 4.7, 4.9]` (arXiv:2609.05053).
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
  posterior carries a prior with structure in `Omega_m`–`w0`–`w_a`; with a
  flat prior it shifts, not significantly, and the effect on the DESI 2024
  fits is "inconsequential" `[src]` (Kim 2024, arXiv:2412.14181).

## 8. Redshifts and peculiar-velocity corrections
<!-- key: redshifts-and-peculiar-velocity-corrections -->

The use of SNe as velocity tracers (growth rate, bulk flow) belongs to
`cosmo-peculiar-velocities`, which describes the likelihood frameworks used
for it. Here peculiar velocities are a nuisance.

- **Frame.** Heliocentric redshifts are converted to the CMB frame with the
  exact multiplicative formula, then corrected for the host peculiar velocity
  predicted from a density-field reconstruction. Carr et al. 2022
  (arXiv:2112.01471) reviewed 2821 SN redshifts for Pantheon+, fixing 5
  wrong or missing heliocentric corrections, 44 wrong or missing coordinates
  and 1200 missing uncertainties; the net effect is `Delta H0 = -0.11
  km/s/Mpc` and `Delta w = -0.001` `[src]`.
- **Flow model.** Peterson et al. 2022 (arXiv:2110.03487), with 584 low-z
  SNe, find the best reduction of Hubble scatter from combining
  coherent-flow corrections (2M++ based: Carrick et al. 2015,
  arXiv:1504.04627, density field within 200 Mpc/h and an external bulk flow
  of `159 ± 23 km/s`) with galaxy-group averaging (0.167
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
<!-- key: calibration-chain -->

1. **Flux scale**: HST CALSPEC standards; a 2020 CALSPEC update changed the
   fundamental calibration by of order 1.5 % over 4000 Å `[src]`
   (arXiv:2112.03864). The CALSPEC uncertainty carried in DES-SN5YR and
   Unite is 5 mmag per 7000 Å `[src]` (arXiv:2401.02945; arXiv:2609.05053).
   CALSPEC rests on pure-hydrogen white-dwarf models; relative fluxes of the
   primary standards are accurate to 1 % from the visible to 2.5 µm (Bohlin
   et al. 2014, arXiv:1406.1707), and the 2020 models of G191-B2B, GD153
   and GD71 agree to 1 % from 1500 Å to 30 µm (Bohlin et al. 2020,
   arXiv:2005.10945) `[src]`.
2. **Per-survey tertiary stars** observed with each SN instrument. Worked
   examples: the SNLS calibration (Regnault et al. 2009, arXiv:0908.3808:
   response maps from dithered stellar fields, position-dependent passbands)
   and its joint SNLS–SDSS version with three transfer paths from the HST
   standards (Betoule et al. 2013, arXiv:1212.4864).
3. **Cross-calibration** of all systems against a uniform all-sky stellar
   catalogue: Supercal (Scolnic et al. 2015, arXiv:1508.05361) used
   Pan-STARRS1; Fragilistic (arXiv:2112.03864) solves 25 systems and 105
   filters simultaneously and outputs a calibration covariance; Dovekie
   (Popovic et al. 2025, arXiv:2506.05471) is the open-source successor,
   using PS1 and Gaia, fitting filter-transmission shifts with uncertainties
   for the first time, and adding faint DA white dwarfs as an absolute tie.
4. **DA white-dwarf network**: faint all-sky DA white dwarfs with modelled
   SEDs tied to the CALSPEC primaries (Axelrod et al. 2023,
   doi:10.3847/1538-4357/acd333); 32 are modelled jointly with three CALSPEC
   stars to < 0.004 mag RMS `[src]` (Boyd et al. 2025, arXiv:2412.08809).
5. **Propagation**: calibration variants are propagated *simultaneously*
   through model retraining and light-curve fitting (10 covariance
   realisations of SALT3 surfaces and zero points in Unite `[src]`,
   arXiv:2609.05053).

## 10. Blinding practice
<!-- key: blinding-practice -->

- JLA: the SNLS–SDSS inter-calibration was "performed blindly with respect to
  the cosmology analysis" (Betoule et al. 2014, arXiv:1401.4064).
- Pantheon+: the binned distance residuals from BBC were hidden and the
  CosmoSIS chains shifted by unknown values `[src: Sect. II.3]`
  (arXiv:2202.04077).
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
<!-- key: public-codes-and-pipelines -->

| Code | What it does | Reference |
|---|---|---|
| SNANA | Survey simulation, light-curve fitting, BBC, fast cosmology fitter (`wfit`) | arXiv:0908.4280; arXiv:1610.04677 |
| Pippin | "A pipeline for supernova cosmology" (title confirmed on Crossref; paper not read); the pipeline manager named in arXiv:2511.07517 | Hinton & Brout 2020, doi:10.21105/joss.02122 `[sec, reference list of arXiv:2202.04077]` |
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
<!-- key: conventions-and-where-the-community-is-split -->

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
<!-- key: not-verified -->

- Tripp 1998 (A&A 331, 815) has no arXiv version and no DOI on Crossref; it
  is cited through arXiv:2511.07517, and Tripp & Branch 1999 was read instead. [src: Sect. "References"]
