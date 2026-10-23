# Light-curve and SED models — cosmo-supernovae dossier

Scope: how a SALT model is trained (sample, definitions, regularisation,
error model), which phases and rest-frame wavelengths are trusted when
fitting and why, how model and training-calibration uncertainty reach the
distances, and how to choose between SALT2, SALT3, extended SALT and BayeSN.
Snapshot: 2026-10-17.
From: DES-SN5YR methods (arXiv:2401.02945), Sects. III.1 and VI.1; Union3
(arXiv:2311.12098), Sects. III.1–III.2; Unite (arXiv:2609.05053),
Sect. 4.2; ZTF DR2 light-curve modelling papers (arXiv:2409.04346,
Table 2); Scolnic & Vincenzi 2023 review (arXiv:2311.16830), Table 1.

Already in L2, not repeated here: the list of models with their training
sizes and headline scatter in `physics-and-methods.md#light-curve-sed-models`;
the SALT2 flux equation (same table); the light-curve model and cuts of each
compilation in `physics-and-methods.md#what-each-main-analysis-did`; the
training-systematic sizes and the Stage-IV training-versus-fitting forecast
in `systematics.md#light-curve-model-training`; the calibration chain in
`physics-and-methods.md#calibration-chain`.

## How it is done
<!-- key: how-it-is-done -->

Notation: `p` is rest-frame phase in days from B-band peak, `lambda` rest
wavelength; `M0(p, lambda)` the mean spectral sequence, `M1` its first
variation, `CL(lambda)` the colour law; per SN `x0` (amplitude), `x1`
(stretch), `c` (colour). The flux is
`F = x0 [M0 + x1 M1 + ...] exp[c CL(lambda)]` (Dovekie, arXiv:2506.05471,
Eq. 22, the same form as SALT2 in L2). "SALT3.X" means SALT3 trained on
sample X (arXiv:2104.07795, Sect. III.1).

### Step 1. Assemble the training sample on the analysis calibration
<!-- key: step-1-assemble-the-training-sample-on-the -->

- **K21 compilation**: 1083 SNe Ia at 0.001 ≤ z ≤ 0.850 with photometry, 380
  of them with spectra, 1207 spectra in all; heliocentric redshifts updated
  (mean change +0.0008); CSP DR3; recalibrated SFD dust map; Fragilistic
  calibration applied "to be used for analyses that calibrate their
  cosmology samples with the SuperCal-Fragilistic scheme, without
  introducing a bias from inconsistent calibrations" [src: Taylor et al.
  2023, arXiv:2301.10644, Sect. 3.1].
- **Selection**: Branch-normal SNe Ia, 1991T-like included as in SALT2; at
  least four epochs at −10 < p < 35, one at 5 < p < 20, one in each of two
  filters at −8 < p < 20, and one at −10 < p < −1; the last cut is new in
  SALT3 and removes 5 of the 420 JLA training SNe [src: arXiv:2104.07795,
  Sect. IV.4]. Host-contaminated high-z spectra were removed at 68 %
  confidence; for low-z spectra host lines are clipped but no continuum is
  subtracted; 114 Foundation and 693 kaepora spectra pass [src].
- **What cannot be calibrated**: historic surveys with too few stars get a
  20 mmag zero-point uncertainty, used only for the systematic surfaces; u
  and U are not recalibrated for lack of overlap with PS1 [src:
  arXiv:2301.10644, Sect. 3.1]. DES-SN5YR and Unite therefore drop
  observer-frame U from training "due to the challenging nature of
  calibrating the near UV ground-based data" [src: arXiv:2609.05053,
  Sect. 4.2].
- **Smaller, better-calibrated sample**: the Dovekie surface drops CfA1,
  CfA2, Calán/Tololo and "Misc. Low-z", leaving 1009 SNe and 755 spectra,
  "to restrict the sample to better understood, more modern surveys whose
  systematics are more amenable to analysis, at a modest reduction to
  statistical power" [src: arXiv:2506.05471, Sect. 5]. Unite instead keeps
  K21 without U and retrains on the Dovekie calibration (SALT3.UNITE) [src:
  arXiv:2609.05053, Sect. 4.2].

### Step 2. Fix the model definitions and resolution
<!-- key: step-2-fix-the-model-definitions-and-resolution -->

SALT3 removes the scale degeneracies with seven definitions [src:
arXiv:2104.07795, Sect. II.1]: `m_B^peak = 10.5` for `x0 = 1`; zero B-band
flux of `M1` at peak; `x1` of the training sample with mean 0 and standard
deviation 1; `c` with mean 0; `CL(4300 Å) = 0` and `CL(5430 Å) = −1`; no
correlation between `x1` and `c` in the training sample. Only the last
differs from SALT2, which instead fixes the V-band flux of `M1` at peak to
zero; the reason given is that a dust-like colour term "does not depend on
the processes associated with light-curve stretch", and uncorrelated
parameters ease population inference [src]. Consequence stated by the
authors: `alpha` depends on the training demographics and on this
definition, and "has no useful comparison across models" [src:
Sect. III.1].

| | SALT2 | SALT3 | Place read |
|---|---|---|---|
| Model range | 2000–9200 Å, −20 to +50 d | 2000–11 000 Å, −20 to +50 d | arXiv:2301.10644, Sect. 2.2 |
| Flux basis (cubic B-splines) | 14 phase (~5 d) × 100 wavelength (~72 Å) | 20 phase (~3 d) × 127 wavelength (~72 Å) | same |
| Colour law | polynomial, `N_CL = 4`, fitted 2800–7000 Å | `N_CL = 5`, 2800–8000 Å | arXiv:2301.10644, Table 1 |
| Outside the polynomial range | linear extrapolation | linear extrapolation | same |
| In-sample variance | out-of-sample variance scaled by an "error snake" to give `chi2_nu = 1` | fitted separately by maximum likelihood | arXiv:2104.07795, Sect. II.2 |

The colour law is `CL_p = alpha_cl lambda_r + sum_i cl_i lambda_r^(i+2)`,
`alpha_cl = 1 − sum cl_i`, in reduced wavelength
`lambda_r = (lambda − lambda_B)/(lambda_V − lambda_B)` with
`lambda_B = 4302.57 Å`, `lambda_V = 5428.55 Å` [src: arXiv:2301.10644,
Colour Laws]. Unite describes the same ranges as central passband ranges of
2800–7000 Å (SALT2) and 2800–8000 Å (SALT3) [src: arXiv:2609.05053,
Sect. 4.2]; these are the colour-law polynomial ranges, not the model
ranges.

### Step 3. Write the error model
<!-- key: step-3-write-the-error-model -->

SALT3 separates "in-sample variance" (population diversity a one-parameter
model cannot capture; the authors cite 3–5 SED parameters plus colour as
needed) from "out-of-sample variance" (finite training data) [src:
arXiv:2104.07795, Sect. II.2]:

- a diagonal flux variance built from `sigma_M0`, `sigma_M1` and their
  correlation, zeroth-order B-splines in phase and wavelength (Eq. 3);
- a "colour scatter" `k(lambda)`, the exponential of a fourth-order
  polynomial, fully correlated between points in the same band and zero
  between bands (Eq. 4), "similar to chromatic models of intrinsic scatter
  like those of Guy et al." [src].

Table 2 lists 72 coefficients each for `sigma_M0`, `sigma_M1` and their
correlation and 4 for the colour scatter [src]; the text gives 8 wavelength
by 12 phase basis functions and Table 1 gives 9 phase by 5 wavelength, an
internal inconsistency of the paper.

### Step 4. Train
<!-- key: step-4-train -->

`chi2_Total = chi2_Phot + A_Spec chi2_Spec + chi2_Constraints + chi2_Reg`
(arXiv:2104.07795, Eq. 10) [src: Sect. II.5]:

- Photometry enters with the model covariance added to the measurement
  errors (Eq. 11), the model reddened by Milky Way `E(B−V)`.
- Spectra are down-weighted by `A_Spec = 0.75` so that spectra and
  photometry contribute about equally, "to reduce the sensitivity of the
  training to unknown systematic errors in the spectral data" (Table 1).
  Each spectrum is multiplied by a smooth recalibration
  `exp(sum y_i lambda^i / i!)` and the colour law is removed from the
  spectral model (Eq. 5), so that mis-calibrated spectra do not bias `CL`
  [src: Sect. II.3].
- Regularisation penalises phase gradients, wavelength gradients and
  non-separability ("dyadic") of `M0` and `M1`, each weighted by
  `1/N_eff`, the binned density of spectra (Eqs. 7–9); weights are tuned
  so the terms "do not contribute significantly to the total χ²", because
  regularisation can over-smooth [src: Sect. II.4].
- The fit alternates Levenberg–Marquardt on flux and nuisance parameters
  with an iMinuit fit of the error model (Eq. 14). The colour scatter is
  held at zero during this stage, since a non-zero value "results in biased
  flux surfaces due to the regularization procedure"; it is fitted last
  with `CL` free. Out-of-sample variance comes from the inverse Hessian
  with regularisation suppressed by a factor 100 [src: Sect. II.5].
- Cost on K21: about 25 minutes per iteration, about 25 iterations, and
  about 4 hours for 80 error-model iterations [src].

### Step 5. Validate on held-out SNe
<!-- key: step-5-validate-on-held-out-sne -->

K21 is split at random into K21train and K21valid (541 SNe each). Metrics:
RMS of Hubble residuals and `Diff(Delta_z mu)`, the change between models of
the mean distance at 0.4 < z < 0.6 minus that at 0.01 < z < 0.2 (Eq. 17);
selection biases are taken as common to the two models and not corrected
[src: arXiv:2104.07795, Sect. III.1]. Result: `sigma_int` higher by
0.01 mag, consistent RMS, `Diff` consistent with zero at the mmag level
[src: Sect. V.1]. The full-K21 model lowers the Foundation RMS from 0.144
to 0.125 mag by using its i and z bands; two extra usable filters improve
the RMS by about 10 % [src: Sect. V.2.1].

### Step 6. Fit the light curves inside the trusted range
<!-- key: step-6-fit-the-light-curves-inside-the-trusted -->

- **Wavelength rule.** A filter is used if its rest-frame central
  wavelength falls inside a range narrower than the model range, because
  the whole bandpass must be inside the SED [src: arXiv:2301.10644,
  Sect. 4.2]. Taylor et al. use 3000–8000 Å: the 2000–3000 Å end has
  limited training data, and 3000 Å keeps at least 50 % of a filter in the
  well-constrained region; 8000 Å keeps about one filter width from the
  SALT2 end at 9200 Å; SALT3 alone could go to about 8700 Å [src]. The
  Dovekie surface has a nominal range of 3500–8800 Å [src:
  arXiv:2506.05471, Sect. 5].
- **Phase rule (Union3).** From 98 well-sampled SNe truncated on a grid,
  requiring a mean distance change ≲ 0.03 mag and NMAD ≲ 0.1 mag: first
  phase ≤ +2, last ≥ +8 and span ≥ 10 d, or first ≤ +6, last ≥ +17 and
  span ≥ 15 d [src: arXiv:2311.12098, Sect. III.2.1]. ZTF finds −10 to
  +40 d optimal, the fit robust to the window (x1 scatter about its
  typical error of 0.2; `c` and `m_B` changes below 30 % of their errors),
  with the model failing before −10 d "where the training critically lacks
  statistics" [src: arXiv:2406.02073, abstract and Sect. 5.1].
- **Fit loop (Union3, sncosmo).** Window −15 to +45 d around a first peak
  estimate; model uncertainties set to zero, then updated and refitted 3–5
  times; the peak date iterated to convergence [src: arXiv:2311.12098,
  Sect. III.1]. For about 2 % of SNe with single-date ≳ 5σ outliers, a
  two-component flux likelihood (99 % nominal, 1 % five times broader) is
  used [src]. A derivative test (sum over zero points of `dm_B/dzp` equal to
  1 within 0.2) rejects 101 SNe with poor coverage or poor model match
  [src].
- **Redshift fixed.** With host redshifts of `sigma_z ~ 10^-4`, the
  redshift is fixed in the fit [src: arXiv:2511.07517, Sect. 3.1].

### Step 7. Propagate calibration through training and fitting together
<!-- key: step-7-propagate-calibration-through-training -->

- **Ensemble of surfaces (BBC analyses).** Zero-point and mean-wavelength
  shifts are drawn from the cross-calibration covariance, the training
  sample is recalibrated, SALT is retrained, and each surface is used with
  its matching bandpasses to refit the light curves; calibration and model
  uncertainty are thus propagated "simultaneously ... and not decoupled as
  in most previous SN cosmological analyses" [src: arXiv:2401.02945,
  Sect. VI.1]. Taylor et al. trained nine such surfaces [src:
  arXiv:2301.10644, Sect. 3.3]; Dovekie trains nine and weights each
  `sigma_k = 1/3` so that the quadrature sum is one (Eq. 23) [src:
  arXiv:2506.05471, Sect. 5.1]. The DES-SN5YR text says "ten mock
  realizations" [src: arXiv:2401.02945, Sect. VI.1]; the weighting error
  found later is in L2.
- **Validation-based (Union3).** Fitting rest-frame UB alone against UBVR on
  SNLS, SDSS and CSP1 shows no slope or offset, so the SALT3 rest-frame U
  is calibrated to about 0.01 mag relative to BVR [src: arXiv:2311.12098,
  Sect. III.2.2]. Union3 adopts correlated 0.01 mag uncertainties for rest
  bands bluer than 4000 Å and redder than 7000 Å, plus 0.03 mag below
  3400 Å, after ten retrainings with 0.01 mag zero-point perturbations gave
  consistent values [src: Sect. IV.4.4]. The reason for preferring
  validation: for SALT2-4 with JLA and for the original SALT3 the test
  shows "biases in excess of those expected from propagating training
  calibration uncertainties" [src].
- **Derivatives from model fluxes.** Per-SN zero-point derivatives are
  biased by Eddington bias (a SN that fluctuates faint in rest U looks
  redder, is pushed brighter, and has a derivative closer to zero). Union3
  computes them on model light curves with `M_B = −19.1`, `x1 = 0`, `c = 0`
  instead of smoothing in redshift, which would lose self-calibration [src:
  Sect. III.1].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### SALT2 or SALT3
<!-- key: salt2-or-salt3 -->

- **Same training, same calibration (K21, Fragilistic), DES-SN3YR data**:
  309 SNe pass with SALT2.FRAG and 322 with SALT3.FRAG, Hubble scatter 0.152
  and 0.151 mag; SALT3 has larger model uncertainties, which lowers the
  reduced χ² of high-S/N low-z light curves and changes who passes the
  fit-probability cut [src: arXiv:2301.10644, Sect. 4.3]. The systematic
  from the framework is `Delta w = +0.001 ± 0.005` with a CMB-like prior;
  SN-only and common-subset fits give |Δw| ≈ 0.03, consistent with zero
  within their errors; fitting only the common subset is "not recommended
  due to the complications it introduces in the bias correction process"
  [src: Discussion].
- **What the number excludes**: changes of training sample, calibration
  and fitting wavelength range [src]. Sensitivity to calibration differs:
  the SALT2.JLA `M0` moves by at least 5 % below about 3000 Å and above
  about 7400 Å across systematic surfaces, the FRAG surfaces by at most
  about 2.5 % above 3000 Å, SALT3 least [src: Sect. 3.3].
- **On ZTF data**, SALT3 (sncosmo v2.0) describes the second maximum
  slightly better than SALT2 but overestimates early fluxes in all bands
  and underestimates r near peak more strongly [src: arXiv:2406.02073,
  Sect. 4.5].

### Model change or zero-point change
<!-- key: model-change-or-zero-point-change -->

On a Pantheon+-like sample, replacing only the SALT model (same zero points)
shifts `w` by 0.037 and replacing only the zero points (same model) by
0.0429; together they account for nearly all of the 0.078 shift between the
Pantheon+ and Dovekie calibration solutions [src: arXiv:2506.05471,
Sect. 6.1]. This is the measured size of "calibration enters twice".

### One colour parameter or more
<!-- key: one-colour-parameter-or-more -->

- ZTF residuals show phase-dependent offsets for blue SNe (−0.11 < c <
  −0.03) that red SNe do not show, which a phase-independent `CL` cannot
  produce; the authors infer a missing phase-dependent intrinsic colour term
  and ask that "SN Ia cosmology must include a SALT2 retraining" [src:
  arXiv:2406.02073, Sect. 4.3.1 and abstract]. No host-dependent residual
  features are found [src: abstract].
- SALT3+ adds a parameter `x2`, trained on ZTF DR2 plus the SALT3
  compilation: the extra variation is mostly phase-dependent g−r and r−i
  colour linked to the i-band secondary maximum; SALT3 absorbs it into `c`;
  neglecting `x2` leaves a Hubble-residual trend of 0.039 ± 0.005 mag, but
  "no evidence of a bias in current cosmological measurements" [src:
  arXiv:2502.09713, abstract].
- Three bands are needed: with g and r only, ZTF colours change by less
  than 0.01, but a third band is required to test calibration, to test a
  second colour term and to classify [src: arXiv:2406.02073, Sect. 5.2].

### SALT with Tripp, or BayeSN
<!-- key: salt-with-tripp-or-bayesn -->

| | SALT + Tripp | BayeSN |
|---|---|---|
| Model | `M0`, `M1`, one colour law for dust and intrinsic colour together | log-SED = template + `W0` + `theta_1 W1` + residual GP + `A_V xi(lambda; R_V)` with the Fitzpatrick law (arXiv:2008.07538, Eqs. 9–12) |
| Population | none in training; distances from `m_B, x1, c` by Tripp | `theta ~ N(0,1)`, `delta M ~ N(0, sigma_0^2)`, `A_V` exponential with mean `tau_A`, one global `R_V ~ U(1,5)` (Sect. 2.5) |
| Distance | after the fit, from summary statistics | sampled jointly with the latent parameters, marginalised over dust and residuals (Sect. 2.8) |
| Wavelength | optical | 0.35–1.8 µm in the 2022 model (Sect. 1.1) |
| Cosmology in training | none | distance prior from a fiducial cosmology; G26 applies it only at z < 0.08, flat above, to avoid circularity (arXiv:2606.19429, Sect. 2.3) |
| Calibration | ensemble of retrained surfaces | per-filter `Delta lambda_T` and `Delta m_T` sampled inside the model with Dovekie priors (arXiv:2606.19429, Eqs. 3–5) |
| Bias corrections | SNANA BBC | not yet in SNANA (arXiv:2606.19429, Sect. 5) |

The BayeSN authors give as reasons the poorly constrained residual-scatter
models of SALT (Δw ~ 0.04 between them), the confusion of dust and
intrinsic colour in one colour law, and the lack of NIR coverage [src:
arXiv:2008.07538, Sect. 1.1]. In G26 the supernovae tighten the zero-point
priors, mostly in red filters, and several filter shifts move by more than
5σ (CfA3K V +72.7 ± 5.5 Å, CfA3K r +53.4 ± 8.6 Å, among others) [src:
arXiv:2606.19429, Sect. 4.3, Table 3]. Milky Way extinction is recomputed at
each proposed filter shift: a 50 Å shift of g at `E(B−V) = 0.05` changes
extinction by about 3 mmag, comparable to Dovekie zero-point errors [src:
Sect. 2.2.2]. On DES-SN5YR at z < 0.7, without bias corrections, `sigma_NMAD`
is 0.164 mag for G26 against 0.185 for SALT3.Dovekie [src: Sect. 5].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| K21 training sample | 1083 SNe, 380 with spectra, 1207 spectra, 0.001 ≤ z ≤ 0.850 | SALT3 | arXiv:2301.10644 | Sect. 3.1 |
| Dovekie training sample | 1009 SNe, 755 spectra | SALT3.DOV | arXiv:2506.05471 | Sect. 5 |
| Uncalibratable historic zero points | 20 mmag (systematic surfaces only) | SALT.FRAG | arXiv:2301.10644 | Sect. 3.1 |
| Spectral suppression | `A_Spec = 0.75` | SALT3.K21 | arXiv:2104.07795 | Table 1 |
| Regularisation weights | phase 1000, wave 10 000, dyadic 1000 | SALT3.K21 | arXiv:2104.07795 | Table 1 |
| Error-model parameters | 72 + 72 + 72 + 4 (colour scatter) | SALT3 | arXiv:2104.07795 | Table 2 |
| Trusted fitting range | 3000–8000 Å central wavelength; SALT3 up to ~8700 Å | SALT.FRAG | arXiv:2301.10644 | Sect. 4.2 |
| Dovekie nominal range | 3500–8800 Å | SALT3.DOV | arXiv:2506.05471 | Sect. 5 |
| Phase coverage | first ≤ +2, last ≥ +8, span ≥ 10 d (or ≤ +6, ≥ +17, ≥ 15 d) | Union3 | arXiv:2311.12098 | Sect. III.2.1 |
| Optimal phase window | −10 to +40 d | ZTF DR2 | arXiv:2406.02073 | abstract |
| SALT rest-U calibration | ~0.01 mag vs BVR; +0.03 mag below 3400 Å | Union3 | arXiv:2311.12098 | Sects. III.2.2, IV.4.4 |
| SALT2 vs SALT3 | `Delta w = +0.001 ± 0.005` (SN + CMB) | DES-SN3YR | arXiv:2301.10644 | Discussion |
| Model-only / zero-point-only shift | `Delta w` 0.037 / 0.0429 (total 0.078) | Pantheon+-like | arXiv:2506.05471 | Sect. 6.1 |
| Systematic surfaces and weight | 9, `sigma_k = 1/3` | Dovekie | arXiv:2506.05471 | Eq. 23 |
| `M0` variation across surfaces | within 0.025 (Dovekie); ≤ ~2.5 % above 3000 Å (FRAG) | | arXiv:2506.05471; arXiv:2301.10644 | Sect. 5.1; Sect. 3.3 |
| `x2` residual trend | 0.039 ± 0.005 mag | SALT3+ on ZTF | arXiv:2502.09713 | abstract |
| BayeSN vs SALT3.Dovekie scatter | 0.164 vs 0.185 mag NMAD, no bias correction, z < 0.7 | DES-SN5YR | arXiv:2606.19429 | Sect. 5 |
| BayeSN low-z distance prior | z < 0.08, `sigma_pec = 150 km/s` | G26 | arXiv:2606.19429 | Sect. 2.3 |
| Foundation RMS, SALT2.JLA → SALT3.K21 | 0.144 → 0.125 mag | | arXiv:2104.07795 | Sect. V.2.1 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Training and fitting on different calibrations.** Biases distances;
  the reason K21 was recalibrated with Fragilistic [src: arXiv:2301.10644,
  Sect. 3.1] and SALT3.DOV and SALT3.UNITE were retrained. Test: check that
  the surface, the light-curve zero points and the bias-correction
  simulations share one solution.
- **Bands used outside the trusted range.** The blue end (2000–3000 Å) has
  little training data [src: arXiv:2301.10644, Sect. 4.2]; validation shows
  SALT biases beyond the propagated training errors for SALT2-4 and the
  first SALT3 [src: arXiv:2311.12098, Sect. IV.4.4]. Test: the UB versus
  UBVR comparison of Union3, Sect. III.2.2.
- **Early points.** Before −10 d the models fail for lack of training data,
  SALT3 more than SALT2 on ZTF [src: arXiv:2406.02073, abstract and
  Sect. 4.5]. Test: residuals by phase bin; restrict the window.
- **Per-SN calibration derivatives.** Eddington bias correlates derivative
  and Hubble residual and biases the cosmology [src: arXiv:2311.12098,
  Sect. III.1]. Test: simulated-data recovery, as in Union3 Sect. IV.7.1.
- **Wrong weight on systematic surfaces.** With nine surfaces the weight is
  1/3 (arXiv:2506.05471, Eq. 23); a different count in the text and the
  weights used is a red flag (L2 records the 0.3 weight of DES-SN5YR).
- **Comparing `alpha` between models.** Meaningless because `x1` is
  defined relative to each training sample [src: arXiv:2104.07795,
  Sect. III.1].
- **`m_B` zero points differ.** SALT3 defines `m_B^peak = 10.5` at `x0 = 1`
  [src: arXiv:2104.07795, Sect. II.1]; DES-Dovekie writes
  `m_B = 10.635 − 2.5 log10(x0)` [src: arXiv:2511.07517, Sect. 3.1];
  Pantheon+ writes `m_B ≡ −2.5 log10(x0)` (L2). The constant is absorbed in
  `M`, but `m_B` columns from different releases cannot be mixed.
- **Colour absorbing other variability.** SALT3 fits put the `x2`
  variation into `c`, making colours less informative [src:
  arXiv:2502.09713, abstract]; blue SNe show phase-dependent colour
  residuals [src: arXiv:2406.02073, Sect. 4.3.1]. Test: residuals split by
  colour and phase.
- **Distances compared without bias corrections.** The G26 comparison is
  made that way, with a z < 0.7 cut "to mitigate Malmquist bias" [src:
  arXiv:2606.19429, Sect. 5]; it is a scatter comparison, not a cosmology
  result.

## Reading list
<!-- key: reading-list -->

- Foundation: Kenworthy et al. 2021, arXiv:2104.07795 — SALT3 definitions,
  error model, regularisation, training procedure and validation metrics.
- Method: Taylor et al. 2023, arXiv:2301.10644 — SALT2 against SALT3 on the
  same data; trusted wavelength range; systematic surfaces.
- Method: Popovic et al. 2025, arXiv:2506.05471 — Dovekie retraining,
  surface weights, model-versus-zero-point split of `Delta w`.
- Application: Rubin et al. 2023, arXiv:2311.12098 — phase and wavelength
  validation, robust fitting, calibration derivatives without Eddington
  bias.
- Application: Vincenzi et al. 2024, arXiv:2401.02945 — joint propagation
  of calibration and model.
- Critique: Rigault et al. 2024, arXiv:2406.02073 — where SALT fails on
  3000 ZTF light curves. [src: abstract]
- Critique/extension: Kenworthy et al. 2025, arXiv:2502.09713 — SALT3+ and
  the `x2` term.
- Alternative: Mandel et al. 2022, arXiv:2008.07538 — BayeSN model and
  priors.
- Alternative: Grayling et al. 2026, arXiv:2606.19429 — BayeSN with
  in-model cross-calibration and a test on DES-SN5YR.

## Not verified
<!-- key: not-verified -->

- Guy et al. 2007 and 2010 (SALT2 training and error snake), Mosher et al.
  2014 (JLA training systematics) and the SALTshaker update cited by
  Dovekie as Kenworthy et al. (2025) and "Whimbrel" (in prep.): not read.
- The SALT2 basis-function count: Taylor et al. give 14 × 100; Kenworthy et
  al., Table 1, give 11 × 97 for the JLA training; not resolved.
- SALT3.UNITE training details beyond Unite Sect. 4.2.
