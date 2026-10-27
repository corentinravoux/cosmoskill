# Photometric calibration and cross-calibration — cosmo-supernovae dossier

Scope: how the photometric systems of a multi-survey SN Ia sample are put
on one flux scale (internal calibration, AB tie through CALSPEC, filter
characterisation, the joint zero-point fit, the DA white-dwarf tie), how
the result is represented as uncertainties, how it is validated, and how
to choose between the Fragilistic, Dovekie and Union3 approaches.
Snapshot: 2026-10-19.
From: Union3 (arXiv:2311.12098), Sect. II.1; DES-SN5YR methods
(arXiv:2401.02945), Sect. II.4; Unite (arXiv:2609.05053), Sect. 4.1;
Scolnic & Vincenzi 2023 review (arXiv:2311.16830), Sect. 0.3
(calibration); ZTF DR2 photometry paper (arXiv:2409.04346, Table 2).

Already in L2, not repeated here: the five-stage calibration chain and its
references (`physics-and-methods.md#calibration-chain`); per-survey
zero-point errors, the factor-6 amplification, the Supercal, Fragilistic,
Dovekie, ATLAS and ZTF sizes, and the Stage-IV requirement headline
(`systematics.md#photometric-calibration-and-cross-calibration`); the
budget rows (`systematics.md#the-budget-at-a-glance`). How calibration
variants are propagated through SALT training and fitting is in
`deep/light-curve-models.md` (Step 7). Survey-internal calibration methods
(ubercal, FGCM, Gaia XP standards) are in
`cosmo-photometry-photoz/deep/photometric-calibration.md`, which leaves the
SN cross-calibration to this file.

## How it is done
<!-- key: how-it-is-done -->

Notation (Fragilistic and Dovekie): `Obs_S^b'` is the observed magnitude of
a tertiary star in filter `b'` of survey `S`; `Synth` the synthetic
magnitude of a spectrophotometric standard integrated through a passband;
`b1` the PS1 filter closest in wavelength to `b'`, and `b2 − b3` a PS1
colour; `Delta_S^b'` the zero-point offset to be fitted; `C_S^b'` the
colour slope of the transformation.

### Step 1. Calibrate each survey internally
<!-- key: step-1-calibrate-each-survey-internally -->

- **What is assumed of each dataset.** Union3 expects each group to have
  corrected detector non-linearity and to control PSF and sky effects; there
  is "no absolutely linear magnitude scale", so surveys are compared through
  their field stars, and PS1 aperture photometry is found more linear than
  PS1 PSF photometry (Currie et al., as cited) [src: arXiv:2311.12098,
  Sect. II.1.1]. Spatial uniformity of large surveys is "a subdominant
  systematic uncertainty"; the four SNLS fields are mutually consistent
  [src: Sect. II.1.2].
- **DES example.** DES images are calibrated on 17 million FGCM tertiary
  stars, with ~1 % absolute calibration and < 3 mmag all-sky uniformity;
  the AB offsets to the CALSPEC star C26202 carry ~0.011 mag uncertainty,
  while the Supercal-Fragilistic covariance gives about 6 mmag on the
  diagonal [src: arXiv:2401.02945, Sect. II.4, Table 1].

### Step 2. Tie each system to AB through CALSPEC
<!-- key: step-2-tie-each-system-to-ab-through-calspec -->

- The "best practice at present" is to observe CALSPEC spectrophotometric
  standards interspersed with the survey; CALSPEC rests on NLTE models of
  three hot DA white dwarfs [src: arXiv:2311.12098, Sect. II.1.3].
- Surveys calibrated only to the Landolt or Smith et al. catalogues get AB
  offsets by colour-transforming every CALSPEC star into the natural
  system and averaging: "Landolt/CALSPEC-14" (14 stars) and
  "Smith/CALSPEC-9" (9 stars), about 5 mmag per filter. Reason for
  averaging: star-to-star tension, rather than relying on one star such as
  BD+17 4708 [src: arXiv:2311.12098, Sect. II.1.3].

### Step 3. Characterise the passbands with stars
<!-- key: step-3-characterise-the-passbands-with-stars -->

- **Problem.** Laboratory or published passbands may not describe the
  survey-mode response. The gold standard is a scan with a light source
  referenced to a calibrated detector, but scattered light still prevents
  precise inter-filter use [src: arXiv:2311.12098, Sect. II.1.4].
- **Union3** shifts the natural-system passbands of low-z datasets with
  unmeasured or evolving passbands "until the observed color terms match
  synthetic color terms", synthesising colour terms from the Pickles, NGSL
  v2 and STIS low-resolution libraries and averaging the shifts, which
  "generally agree to a few angstroms" between libraries [src:
  arXiv:2311.12098, Sect. II.1.4]. The table of that section runs from a
  few Å to −180 Å (LOSS K1 I) [src: Sect. II.1.4].
- **Dovekie** regresses, for each filter, the synthetic difference
  `Synth_PS1^b1 − Synth_S^b'` on the synthetic PS1 colour (Eq. 4), and the
  observed difference on the observed colour with up to three 3-sigma
  clipping iterations (Eq. 5). The colour is PS1 `g − i`, or `g − r` for the
  bluest filter of each survey, because `g − i` spans more colour without
  the noisier `z` band [src: arXiv:2506.05471, Sect. 3.2.1]. Gaia
  spectrophotometry integrated through the passbands gives a second
  regression (Eq. 6) [src: Sect. 3.2.2].
- **Why simulations are needed**: "linear regression on data with noise in
  the independent variable, outliers, and/or cuts on the data is a biased
  estimator"; simulated tertiary stars built from the NGSL or CALSPEC
  library (Eq. 10) give the bias `Delta_C` and scatter `varsigma` of the
  slope difference [src: Sect. 3.3, Sect. 3.2.3].
- **Fit of the shift** (arXiv:2506.05471, Eq. 9): passbands are shifted, `f_new(lambda) =
  f_old(lambda − lambda_shift)` (Eq. 7), from −50 to +50 Å; the PS1 and Gaia
  likelihoods are summed with a zero-centred 50 Å prior; Gaia is ignored in
  `g` bands because of known discrepancies between Gaia spectra and PS1 and
  DES `g`; a filter is shifted when the determinations disagree with the
  nominal passband by 3 sigma or more, and the posterior width gives the
  1-sigma filter uncertainty [src: Sect. 3.2.3].
- **Unit errors.** A second modification weights the passband by
  `(lambda_eff / lambda)^X`, `X = ±1` (Eq. 8), for passbands whose files
  appear to mix energy- and photon-counting units [src: Sect. 3.2.3];
  applied with `X = −1` to all CfA4 filters, believed supplied in
  energy-counting units [src: Sect. 8.1, Table 1].

### Step 4. Fit all zero-point offsets jointly
<!-- key: step-4-fit-all-zero-point-offsets-jointly -->

- **Fragilistic** (Eq. 4–5): for stars common to PS1 and survey `S`,
  `Obs_PS1^b1 − Obs_S^b' = (Synth_PS1^b1 + Delta_PS1^b1) − (Synth_S^b' +
  Delta_S^b') + C_S^b' × [(Obs_PS1^b2 + Delta_PS1^b2) − (Obs_PS1^b3 +
  Delta_PS1^b3)]`; 105 filters, 4 of them PS1 `griz`, so 101 equations
  and 105 parameters, with degeneracies broken by priors; minimised with
  emcee to obtain the covariance [src: arXiv:2112.03864, Sect. III.1].
  Priors: 0.00 ± 0.01 mag for PS1/Foundation, DES, SDSS and SNLS, none for
  other samples "to ensure that the calibration solution is primarily
  determined by the more modern all sky surveys", and 0.02 mag on the PS1
  public catalogue (fixed in Supercal) "to facilitate covariance between all
  of the surveys"; survey weights `W_S` (KAIT 1–4 each 1/4) for systems
  recalibrated over time; error floors 0.005 (modern) and 0.01 mag (other
  low-z; 0.02 for CNIa0.02, which had no tertiary stars) [src: Sect.
  III.1]. Colour slopes are fixed to the synthetic ones where data and
  synthetic agree [src].
- **Dovekie** (Eqs. 14–21): with slopes fixed, 52 offsets (4 of them PS1)
  are sampled with NUTS from
  `log p(Delta) = log L_WD + log L_Tertiary + log pi_Prior` (Eq. 14); the
  prior is a zero-mean normal per survey (Eq. 15). The white-dwarf term
  (Eqs. 16–18) compares catalogue photometry of DA WDs in PS1, DES and
  SDSS with synthetic magnitudes averaged over SED realisations, using the
  mean modelling covariance over all standards, "effectively assuming a
  high degree of correlation between all standards" because systematics
  below HST precision may be shared; catalogue errors are inflated by
  fitted parameters because they are "underestimated" [src:
  arXiv:2506.05471, Sect. 3.4.2]. The tertiary term (Eq. 21) is a mixture
  over the NGSL and CALSPEC libraries with equal weights, and each filter
  has covariance `sigma_S^2 I + f_S^2 1`, i.e. a per-survey error floor
  `f_S` fully correlated between that filter's stars, included as a
  systematic on the filter transformation [src: Sect. 3.4.3]. SOUSA and
  LOSS are not in the fiducial solution [src: Sect. 3.4].
- **Unite** reruns the public Dovekie code with LOSS1, LOSS2 and SOUSA
  added, excludes CfA1, CfA2 and HST (HST CALSPEC "define the absolute flux
  calibration"), and finds zero points of common surveys highly consistent
  with Dovekie [src: arXiv:2609.05053, Sect. 4.1].

### Step 5. Tie the network to faint DA white dwarfs
<!-- key: step-5-tie-the-network-to-faint-da-white-dwarfs -->

- 32 faint all-sky DA WDs (`16.5 < V < 19.5`) and three CALSPEC primaries
  are modelled hierarchically from 912 Å to 32 µm, inferring HST WFC3
  zero points together with `log g`, `T_eff`, `A_V`, `R_V`; residuals
  < 0.004 mag RMS on average [src: arXiv:2412.08809, abstract].
- Likelihood (Eq. 4): Student-t in each HST band with zero point `Z_X`,
  per-cycle offset `Delta Z_X^c`, excess dispersion and a count-rate
  non-linearity term in F160W only; the network is tied to the 2020
  CALSPEC system by fixing the F475W magnitudes of G191B2B, GD153 and GD71
  [src: Sect. 3.2]. Synthetic magnitudes are photon-weighted integrals
  against the AB spectrum (Eq. 3) [src].
- Against DES DR2 (seven WDs) the residual bias is 12–13 mmag in `g, r, i`
  and 4 mmag in `z`; it depends on the CALSPEC version, and the residuals
  shrink "dramatically" if the 2014 CALSPEC system used by the surveys is
  adopted instead (Gaia G: −1 mmag) [src: arXiv:2412.08809, Sect. 4.4].
  The authors keep the 2020 system as "more accurate" and ask surveys to
  adopt it [src].

### Step 6. Represent the uncertainty
<!-- key: step-6-represent-the-uncertainty -->

- **Filter uncertainties.** Dovekie derives them from the shift posteriors
  and finds them larger than the ~6 Å historically assumed for modern AB
  surveys, growing to the red: DES `griz` 5, 5, 10, 30 Å against 6 Å each in
  Fragilistic; CSP `BVgri` 8, 10, 10, 15, 20 Å against 7, 3, 8, 4, 2 Å
  [src: arXiv:2506.05471, Table 2, Sect. 8.1].
- **Zero points.** Low-z surveys keep a 0.01 mag error floor and are
  "entirely error-floor dominated"; surveys with DA WDs observed improve
  by a factor 2 [src: arXiv:2506.05471, Sect. 8.2].
- **CALSPEC.** Union3 rejects a single slope in wavelength because the
  history of CALSPEC changes "poorly" matches one (as assumed in Betoule et
  al.), and adopts uncertainties relative to 5000–6000 Å of 10 mmag
  (3000–4000 Å), 5 mmag (4000–5000 Å), 2 mmag (6000–8000 Å), 5 mmag above
  8000 Å, plus 5 mmag above 10 000 Å, uncorrelated [src:
  arXiv:2311.12098, Sect. IV.4.3]. The BBC analyses carry 5 mmag per
  7000 Å (L2).
- **Passbands in UNITY.** Each passband uncertainty is an effective-
  wavelength uncertainty only; derivatives come from warping each passband
  by `exp(lambda / 1 µm)` and refitting [src: Sect. IV.4.2]. Zero-point,
  passband and CALSPEC terms enter as nuisance parameters `Delta sys` with
  derivatives on `{m_B, x1, c}` (Eq. 10), equivalent to the covariance
  approach (Eq. 11) for linear systematics and Gaussian priors [src:
  Sect. IV.4].

### Step 7. Validate
<!-- key: step-7-validate -->

- **Injected offsets.** Dovekie recovers random zero-point offsets in 100
  simulated tertiary-star sets with no bias above 1 sigma in any filter
  [src: arXiv:2506.05471, Sect. 4.2].
- **Per-survey Hubble residuals.** Fragilistic compares weighted mean
  residuals per survey at 0.01 < z < 0.4, cutting at 0.4 "to eliminate
  sensitivity to cosmological signals": `chi2/N_dof = 17.6/17`, 11.1/11
  for the Supercal subset; CSP stood out and received an extra systematic
  [src: arXiv:2112.03864, Sect. V.1].
- **SNe in common between instruments** (Union3, Eq. 3):
  `mu_ij ~ Student-t(mu_i + Delta mu_j, sigma_j, 7)` for 250 SNe observed
  by at least two groups in at least two bands, with `x1` and peak date
  fixed from a joint fit so that cuts cannot move SNe in or out. CfA2,
  CfA3, CfA4 and LOSS agree with each other but are offset from Swope;
  Foundation, LCO and SDSS show the largest dispersion; offsets are
  consistent with the assigned zero-point and passband uncertainties [src:
  arXiv:2311.12098, Sect. III.3].
- **Unblinding checks carried by DES-Dovekie** (doubled tertiary stars,
  agreement of white-dwarf and tertiary-star `g − r`, equal or smaller
  Hubble scatter) are listed in `deep/covariance-likelihood-blinding.md`.

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Shift the reference or shift the others
<!-- key: shift-the-reference-or-shift-the-others -->

Fragilistic found PS1 `g` slopes discrepant at > 3 sigma with SDSS `g`
(+5 sigma), SNLS `g` (+5.5) and the CfA1, CfA3S, CfA4p1, KAIT and SOUSA
`B` bands (+3.5 to +9 sigma), and shifted
PS1 `g` by +30 Å "to bring all into better agreement" [src:
arXiv:2112.03864, Sect. III.1]. Dovekie undoes that shift, choosing "to
preserve the band passes of the reference survey and modify other surveys
as necessary"; this explains most of its filter changes except CfA4 [src:
arXiv:2506.05471, Sects. 4.1, 8.1]. Cost: about seventeen modified filters,
including +30 Å on all SNLS bands [src: Table 1].

### Laboratory passbands or star-derived ones
<!-- key: laboratory-passbands-or-star-derived-ones -->

Dovekie concludes that laboratory filter measurements "do not appear to
accurately predict the colour responses" of tertiary standards, citing a
CSP-B shift nearly ten times the nominal < 8 Å uncertainty, and attributes
such shifts to survey-mode conditions [src: arXiv:2506.05471, Sect. 8.1].
DES, with four times as many stars as SDSS, SNLS and PS1, gains no
significant filter precision, so star statistics and repeatability set the
limit [src]. For finished surveys (CfA3, SNLS), which SALT training needs,
no new stars can be taken [src].

### Tertiary stars alone or with white dwarfs
<!-- key: tertiary-stars-alone-or-with-white-dwarfs -->

White dwarfs halve the zero-point error of the surveys that observed them
[src: arXiv:2506.05471, Sect. 8.2], at the price of tying to the 2020
CALSPEC system, against which older survey calibrations show 4–13 mmag
residuals [src: arXiv:2412.08809, Sect. 4.4].

### Covariance ensemble or nuisance parameters
<!-- key: covariance-ensemble-or-nuisance-parameters -->

BBC analyses draw surfaces from the cross-calibration covariance and
retrain (light-curve dossier, Step 7); UNITY samples each zero point,
passband and CALSPEC term and reports how much the data shrink their
posteriors ("partial self calibration") [src: arXiv:2311.12098,
Sect. IV.4]. The internal DES offsets were replaced by Fragilistic ones
because the low-z samples share that solution, it gives covariance between
DECam and low-z filters, it generates correlated realisations, and it uses
more external data; the change is a ~5 mmag `g − z` colour correction [src:
arXiv:2401.02945, Sect. II.4].

### Where a calibration error bites: training or fitting
<!-- key: where-a-calibration-error-bites-training-or -->

On simulated LSST and Roman samples with 5 mmag zero-point and 5 Å
wavelength perturbations, errors applied only in SALT training cost 7–14 %
of the FoM, while errors in light-curve fitting (Fit or Train+Fit) cost
about half; the fitting-stage distance residuals are well described by a
quadratic in redshift and so "cannot be self-calibrated" [src:
arXiv:2604.19746, Sect. III.3, Table 5]. Most sensitive single filters
(Fit): LSST `r` zero point, ~19 % FoM loss; Roman F106 and F129 up to
12 %; Roman wavelength shifts < 4 % [src]. **Forecast.** The authors flag
non-linear FoM behaviour at some shift amplitudes as not understood [src].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Filters / equations / parameters | 105 / 101 / 105 | Fragilistic | arXiv:2112.03864 | Sect. III.1 |
| Zero-point priors | 0.01 mag modern surveys; 0.02 mag PS1; none others | Fragilistic | arXiv:2112.03864 | Sect. III.1 |
| Error floors | 0.005 (modern), 0.01 (low-z), 0.02 (CNIa0.02) | Fragilistic | arXiv:2112.03864 | Sect. III.1 |
| Offsets sampled | 52, NUTS | Dovekie | arXiv:2506.05471 | Sect. 3.4 |
| Filter-shift scan and prior | −50 to +50 Å; 50 Å Gaussian | Dovekie | arXiv:2506.05471 | Sect. 3.2.3 |
| Shift threshold | ≥ 3 sigma slope disagreement | Dovekie | arXiv:2506.05471 | Sect. 3.2.3 |
| PS1 `g` shift | +30 Å (Fragilistic), removed (Dovekie) | both | arXiv:2112.03864; arXiv:2506.05471 | Sect. III.1; Sect. 4.1 |
| SNLS `griz` shift | +30 Å | Dovekie | arXiv:2506.05471 | Table 1 |
| DES `griz` filter uncertainty | 5, 5, 10, 30 Å (Fragilistic 6 Å each) | Dovekie | arXiv:2506.05471 | Table 2 |
| Low-z zero-point floor | 0.01 mag | Dovekie | arXiv:2506.05471 | Sect. 8.2 |
| Landolt/Smith AB offsets | ~5 mmag per filter (14 and 9 CALSPEC stars) | Union3 | arXiv:2311.12098 | Sect. II.1.3 |
| CALSPEC uncertainty model | 10 / 5 / 2 / 5 (+5) mmag by wavelength range | Union3 | arXiv:2311.12098 | Sect. IV.4.3 |
| SNe in common used for offsets | 250 | Union3 | arXiv:2311.12098 | Sect. III.3 |
| DA WD network | 32 faint + 3 CALSPEC; < 0.004 mag RMS | Boyd et al. | arXiv:2412.08809 | abstract |
| WD residuals vs DES DR2 | 12–13 mmag `gri`, 4 mmag `z` | Boyd et al. | arXiv:2412.08809 | Sect. 4.4 |
| DES FGCM | 17 million stars, < 3 mmag uniformity | DES-SN5YR | arXiv:2401.02945 | Sect. II.4 |
| ATLAS calibration total after correction | 0.005 (orange), 0.009 mag (cyan) | TITAN | arXiv:2512.21903 | Table 4 |
| Stage-IV FoM retained (Train / Fit / Train+Fit, LR, random) | 0.868 / 0.532 / 0.485 (**forecast**) | LSST + Roman | arXiv:2604.19746 | Table 5 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Unit mislabelling of passbands** (energy vs photon counting): seen as
  colour slopes that no wavelength shift fixes; Dovekie's Eq. 8 test [src:
  arXiv:2506.05471, Sect. 8.1].
- **Biased colour slopes** from noisy independent variables and clipping;
  caught only with simulated stars [src: Sect. 3.3].
- **Underestimated catalogue errors** of standards; fitted inflation
  parameters [src: Sect. 3.4.2].
- **Gaia in `g`**: discrepant with PS1 and DES, excluded [src: Sect. 3.2.3].
- **Chromatic, time-dependent instrument response.** ATLAS shows a
  colour-dependent residual of about 0.005–0.045 mag over the SN `g − i`
  range, worsening with time on one camera, corrected by shifting the
  passbands; the cyan chromatic term falls from 0.029 to 0.005 mag [src:
  arXiv:2512.21903, Sects. VI.1, VI.3, Table 4].
- **Position-dependent passbands.** The SNLS radial filter dependence
  (Regnault et al. 2009) was omitted in Unite until a ~2 sigma per-survey
  residual exposed it [src: arXiv:2609.05053, Sect. 5.2].
- **Mixed CALSPEC versions** between the WD network (2020) and survey
  calibrations (2014 or older): 4–13 mmag residuals [src:
  arXiv:2412.08809, Sect. 4.4].
- **Treating finished low-z surveys as improvable**: their floor is fixed
  by archival stars [src: arXiv:2506.05471, Sect. 8.1].
- **Internal inconsistency to note.** Dovekie's Table 1 lists CSP-B at
  +50 Å and CfA3K-B at +70 Å, while its text gives CfA3K-V −30 Å (Sect.
  4.1) and CSP-B 70 Å (Sect. 8.1) [src: arXiv:2506.05471]. Unresolved; use
  the released filter files.

## Reading list
<!-- key: reading-list -->

- Scolnic et al. 2015, arXiv:1508.05361 — foundation: Supercal, the PS1-based
  cross-calibration (L2 sizes).
- Brout et al. 2022, arXiv:2112.03864 — method: Sect. III.1 for the joint
  fit, priors, weights and floors; Sect. V.1 for the per-survey residual
  test.
- Popovic et al. 2025, arXiv:2506.05471 — method: Sects. 3.2–3.4 for filter
  characterisation, simulations and the three-term posterior; Sect. 8 for
  the limits of the tertiary-star method.
- Boyd et al. 2025, arXiv:2412.08809 — method: the DA white-dwarf network
  and its CALSPEC-version dependence.
- Rubin et al. 2023, arXiv:2311.12098 — alternative: Sect. II.1 for
  calibration principles, III.3 for the common-SN test, IV.4 for nuisance
  treatment and the CALSPEC uncertainty model.
- Vincenzi et al. 2024, arXiv:2401.02945 — application: Sect. II.4, why a
  survey adopts the cross-calibration over its own AB offsets.
- Marlin et al. 2025, arXiv:2512.21903 — application: calibrating a new
  all-sky anchor (ATLAS) and its chromatic term.
- Anumba et al. 2026, arXiv:2604.19746 — critique / forecast: why
  fitting-stage calibration errors cannot self-calibrate.

## Not verified
<!-- key: not-verified -->

- Dovekie Eq. 3 (survey colour transformations) and its Table 8 of priors
  were not read.
- The Scolnic & Vincenzi 2023 review and the ZTF DR2 Table 2 named in the
  `From` line were not read for this dossier.
- Currie et al. (PS1 linearity), Krisciunas et al. 2020 (CSP passbands),
  Axelrod et al. 2023 and Narayan et al. 2019 are quoted through the papers
  above.
- The FGCM method (Burke et al.) is not read here; see the photometry
  sibling.
