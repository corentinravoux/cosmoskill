# Covariance, likelihood and blinding — cosmo-supernovae dossier

Scope: how the statistical and systematic distance covariances of an SN Ia
Hubble diagram are assembled (sample freezing, duplicates, weights,
binning, photometric samples), how the absolute magnitude is removed from
the likelihood, which samplers, priors and significance conventions the
current analyses use and why, and what blinding and unblinding criteria
they apply.
Snapshot: 2026-10-19.
From: DES-SN5YR methods (arXiv:2401.02945), Sects. III.6 and VII; Union3
(arXiv:2311.12098), Sect. V.1; Unite (arXiv:2609.05053), Sects. 4.9, 5.2,
6 and 8.

Already in L2, not repeated here: the Gaussian likelihood and the Pantheon+
form of `C_syst` (`physics-and-methods.md#covariance-and-likelihood-practice`),
the gain from unbinning and the Pantheon+ unbinned and binned values of
`sigma_w` (same section), the one-at-a-time budget conventions and the per-analysis
budgets (`systematics.md#the-budget-at-a-glance` and its subsections), the
FoM definitions and the Union3 compressed-product prior issue (same
`physics-and-methods.md` section), and the list of what each analysis hid
(`physics-and-methods.md#blinding-practice`).

## How it is done
<!-- key: how-it-is-done -->

Notation: `mu_i` is the bias-corrected distance modulus of light curve `i`,
`C_stat` and `C_syst` the statistical and systematic covariances,
`Delta mu_S^i` the change of `mu_i` when systematic `S` is switched on,
`W_S` (or `sigma_psi`) its scale, `M` the SN absolute magnitude, and
`𝓜` the magnitude–`H0` combination that an unanchored fit can constrain.

### Step 1. Freeze one sample for every variant
<!-- key: step-1-freeze-one-sample-for-every-variant -->

- An unbinned covariance needs the same SNe in the baseline and in every
  systematic variant. "Fluctuations of the sample of light curves that pass
  the sample quality cuts ... for different systematics result in an
  ill-defined covariance matrix" [src: arXiv:2202.04077, Sect. II.2].
- Pantheon+ therefore applies light-curve quality cuts on the baseline
  values only, and runs BBC twice: once to find the < 1 % of SNe for which
  no bias correction can be computed in some variant, then on the common
  set; this gives the 1701 light curves [src: arXiv:2202.04077, Sect. II.2].
- DES-SN5YR, DES-Dovekie and Unite use the same rule ("common to all
  variants" among their cuts, in L2).

### Step 2. Build the statistical covariance
<!-- key: step-2-build-the-statistical-covariance -->

- Pantheon+ (Eq. 5): the diagonal is the full distance error `sigma_mu^2`
  of each light curve; for two light curves of the same SN from different
  surveys the off-diagonal element is
  `sigma_floor^2 + sigma_lens^2 + sigma_z^2 + sigma_vpec^2`, i.e. every
  noise term except the light-curve measurement itself [src:
  arXiv:2202.04077, Sect. II.2, Eq. 5].
- DES-SN5YR's `C_stat` is diagonal [src: arXiv:2401.02945, Sect. III.6].
  Unite, which inherits the Pantheon+ duplicates, adds off-diagonal terms
  following Pantheon+ and replaces `sigma_lens = 0.055 z` by the per-SN
  error of its lensing estimator, dominated by the foreground photo-z
  uncertainty [src: arXiv:2609.05053, Sect. 4.9].
- What counts as statistical: terms whose effect "could be simply reduced
  by increasing the SN sample size". A statistical term can still be
  correlated between SNe (the SN-model uncertainty is the example given),
  so `C_stat` is not always diagonal [src: arXiv:1104.1443, Sect. IV.1].

### Step 3. Build the systematic covariance
<!-- key: step-3-build-the-systematic-covariance -->

Two forms are in use.

- **Derivative form** (Conley et al. 2011, Eq. 6; Pantheon+, Eq. 7):
  `C_syst,ij = sum_k (d m_mod,i/d S_k)(d m_mod,j/d S_k)(Delta S_k)^2`,
  summed over the `K` systematics with sizes `Delta S_k` [src:
  arXiv:1104.1443, Sect. IV.1, Eq. 6]. Pantheon+ assumes linearity between
  `Delta mu_psi` and `psi` to compute the derivative [src:
  arXiv:2202.04077, Sect. II.2].
- **Difference form** (DES-SN5YR Eq. 11, DES-Dovekie Eq. 9):
  `C_syst^ij = sum_S Delta mu_obs,S^i Delta mu_obs,S^j W_S^2`, with `W_S`
  "the scale of the systematic" [src: arXiv:2401.02945, Sect. III.6,
  Eq. 11], set to 1 unless stated [src: arXiv:2511.07517, Sect. 4.1, Eq. 9].
- **Redshift systematics** need a model term: Pantheon+ defines
  `Delta mu_psi^i = mu_psi^i − mu_BASE^i − (mu_ref(z_psi) − mu_ref(z_BASE))`
  with `mu_ref` flat LCDM (`Omega_M = 0.3`), so that a redshift shift is
  turned into a distance change at fixed cosmology [src: arXiv:2202.04077,
  Eq. 6]. The text names the same term `mu_ref` and then `mu_mod`.
- **Weights for ensembles.** Unite's Table 4 gives a "Size" per variant:
  1/10 for each of 10 SALT3 + calibration realisations, 1/4 for each of
  three P23 dust realisations and for the BS21 parameters, 1/3 for the
  Milky Way colour law, 1/10 for each of 10 host-mass realisations, and
  1/6 for the `Delta z = 10^-4` shift, whose note says the scaling makes
  `sqrt(1/6) × 10^-4 ≈ 4 × 10^-5` [src: arXiv:2609.05053, Table 4].
- **Reading of the "Size" column** [der]: the note implies that "Size" is
  the variance weight `W_S^2`, so that an ensemble of `n` equally weighted
  draws sums to one unit of variance, which is the rule DES-Dovekie
  restored (one weight per SALT surface, L2).
- **Effects that are not smooth**, such as contamination removing an SN
  from the sample: Conley et al. estimate them in redshift bins, then
  reproject onto individual SNe the bin-wide, fully correlated uncertainty
  that reproduces the bin-mean effect [src: arXiv:1104.1443, Sect. IV.1].
- **Inversion.** With a diagonal part and low-rank off-diagonal pieces,
  Conley et al. invert with the Sherman–Morrison–Woodbury formula in `N^2`
  steps [src: Sect. IV.1].
- **What enters Unite's `C_syst`** is the DES-SN5YR list with three
  changes: the BEAMS contamination variants are replaced by a probability
  cut; the `P21(u−r)` dust variant is dropped because it "fails to
  adequately describe the Hubble residuals" (alone it gives `delta w =
  0.048` in DES-SN5YR and 0.029 in DES-Dovekie, with no effect on
  `sigma_w,syst`); and the ±0.2 mag spectroscopic-efficiency shift is
  extended from DES to SDSS, SNLS and PS1MD [src: arXiv:2609.05053,
  Sect. 4.9].

### Step 4. Decide binned, unbinned or rebinned
<!-- key: step-4-decide-binned-unbinned-or-rebinned -->

- **Binned** (Brout, Hinton & Scolnic 2021, Eqs. 5–6): `<z>_bin` is the
  error-weighted mean redshift and
  `<mu>_bin = <mu^i − mu_fid^i> + mu_fid(<z>_bin)`, with
  `mu_fid` = flat `w = −1`, `Omega_M = 0.3` [src: arXiv:2012.05900,
  Sect. II.2].
- **Why unbinned is better**: a covariance-matrix fit and a fit with an
  explicit "self-calibrating" scale `S_sys` per systematic (Eqs. 11–12,
  Gaussian prior of the same width, `Omega_M = 0.3 ± 0.01`) agree with
  each other in both binned and unbinned form, but the unbinned data
  "always produces equal or better constraints"; binning removes the
  ability of the data to constrain systematics that depend on anything
  other than redshift, and the gain grows with sample size [src:
  arXiv:2012.05900, Sects. II.4, V]. Redshift smoothing, as in JLA,
  "would remove any color-dependence" and behaves like binning [src:
  Sect. V].
- **Photometric samples.** BHS21 note that only binned BBC distances had "a
  robust, frequentist meaning" with BEAMS probabilities and simulated
  core-collapse distributions [src: arXiv:2012.05900, Sect. V]. Kessler,
  Vincenzi & Armstrong 2023 unbin after the BBC fit: per event
  `sigma_mu,unbin,i = S_zeta sigma_mu,i / sqrt(P_B(Ia),i)` (Eq. 10), where
  `P_B(Ia),i = P_Ia D_Ia / [P_Ia D_Ia + (1 − P_Ia) D_CC]` (Eq. 9) and
  `S_zeta` is chosen so that the weighted error in each redshift bin
  equals the BBC error on that bin's offset (Eqs. 7–8). `S_zeta` is "a few
  percent greater than 1", and the authors call Eq. 8 "an ad hoc
  assumption" without rigorous derivation [src: arXiv:2306.05819,
  Sect. III]. Check: the weighted mean Hubble residual per bin must be zero
  (Eq. 11) [src].
- **Rebinned**: weighted means in cells of `{z, x1, c}` (Eqs. 12–13) keep
  the self-calibration at lower cost; on 50 simulated DES + low-z samples
  with core-collapse and peculiar contaminants, unbinned and rebinned give
  similar uncertainty and no evidence for a `w` bias [src: arXiv:2306.05819,
  abstract, Sect. III]. The Roman forecast cell numbers are in
  `deep/selection-bias-corrections.md`.

### Step 5. Write the distance model and remove M
<!-- key: step-5-write-the-distance-model-and-remove-m -->

- Distance model as printed (Unite Eqs. 2–5): `mu_theory = 5 log10[D_L /
  1 Mpc] + 25`, `D_L(z_obs, z) = (1 + z_obs) R_0 S_k(chi(z))`, with `z_obs`
  heliocentric, `z` cosmological, `R_0 = c / (H0 sqrt|Omega_K|)` [src:
  arXiv:2609.05053, Sect. 3.1]. DES-Dovekie writes the integral over
  `z_CMB` and the prefactor `(1 + z_obs)`, which "captures the effect of
  beaming due to peculiar velocity of both the Sun and the SN Ia" [src:
  arXiv:2511.07517, Sect. 4.1, Eqs. 5–7].
- **Analytic marginalisation over 𝓜.** With a flat prior,
  `chi2_marg = a + log(e / 2 pi) − b^2 / e` (Eq. 7), where
  `a = Delta m^T C^-1 Delta m`, `b = Delta m^T C^-1 1`, `e = 1^T C^-1 1`
  and `Delta m` omits `𝓜`; the determinant of `C` does not appear. A
  two-`𝓜` version (split by host mass) is Eq. 8, with
  `𝓜_1 = (bf − cd)/g`, `𝓜_2 = (ce − bd)/g` [src: arXiv:1104.1443,
  Appendix C]. Unite follows the same treatment, citing Goliath et al.
  2001, Appendix A.1, and combines `M` and `H0` "into a single parameter
  that we analytically marginalise over" [src: arXiv:2609.05053,
  Sect. 3.1]. DES-Dovekie marginalises over
  `𝓜 = M_0 + 5 log10(c / H0)` [src: arXiv:2511.07517, Sect. 4.1].
- **Union3** writes `𝓜_B ≡ M_B − 5 log10(H0 / 70 km/s/Mpc)` and uses the
  constant `5 log10[c / ((70 km/s/Mpc)(10 pc))] = 43.15861` (Eqs. A4–A6),
  with a prior `𝓜_B ~ N(−19, 0.3^2)` "for h = 0.7" [src:
  arXiv:2311.12098, Appendix A, Appendix B].
- **Anchored form** (Pantheon+ Eqs. 14–15): for SNe in Cepheid hosts the
  residual is `mu_i − mu_i^Cepheid`, elsewhere `mu_i − mu_model(z_i)`, and
  the SH0ES Cepheid covariance is added to the SN covariance [src:
  arXiv:2202.04077, Sect. II.3]. Unite releases both anchored and
  unanchored forms (L2).

### Step 6. Sample, and say how
<!-- key: step-6-sample-and-say-how -->

- Pantheon+: PolyChord in CosmoSIS, 250 live points, 30 repeats, evidence
  tolerance 0.1, giving 1000–3000 independent samples; SN-only results
  checked with CosmoMC and with SNANA's grid fitter [src:
  arXiv:2202.04077, Sect. II.3].
- DES-Dovekie and Unite: CosmoSIS with Nautilus, which also returns
  `log Z` [src: arXiv:2511.07517, Sect. 4.1; arXiv:2609.05053,
  Sect. 8.2]. Nautilus gives no error on `log Z`; DES-Dovekie estimates
  `sigma(log Z) ~ 0.2` from other samplers, settings and seeds [src:
  arXiv:2511.07517, Sect. 4.3].
- For the 25 validation simulations DES-Dovekie uses SNANA's `wfit` with a
  CMB `R`-shift prior instead of the full Planck likelihood, "to avoid
  excessive CPU consumption" [src: arXiv:2511.07517, Sect. 6.2].
- Union3's frequentist contours use `Delta chi2` = 2.296, 6.180, 11.829 for
  68.3, 95.4 and 99.7 % in two parameters, profiling the others, with an
  adaptive-refinement contour code [src: arXiv:2311.12098, Sect. V.3].

### Step 7. Compress, if releasing distances
<!-- key: step-7-compress-if-releasing-distances -->

Union3 releases "spline-interpolated distance moduli": additive
perturbations from flat LCDM (`Omega_m = 0.3`) at 22 non-zero nodes (steps
of 0.05 to z = 0.8, then 0.1 or every 10 SNe), interpolated by a
second-order spline fixed to zero at z = 0, with median and covariance
from 500 000 posterior samples. The check: `exp(−chi2/2)` from the spline
product, with `Delta 𝓜_B` absorbing the magnitude shift (Eq. 22), matches
the density of the direct UNITY1.5 wCDM posterior samples "even out into
the tails" [src: arXiv:2311.12098, Sect. V.2.1]. The reason given for
releasing it: most users "would prefer distance moduli as a function of
redshift with a covariance matrix" [src]. Its SN `chi2` has 22 − `N_fit`
degrees of freedom, not 2087 [src: Table 5 note]. Node priors are
`N(0, 1^2)` around the `Omega_m = 0.3` distances [src: Appendix B].

### Step 8. Compare models
<!-- key: step-8-compare-models -->

- **Frequentist**: Wilks' theorem on `Delta chi2_ML` with one (wCDM) or two
  (`w0w_a`CDM) extra degrees of freedom, converted to `n sigma` with
  Eq. 10; "strictly only approximate for real data, as terms of
  O(1/sqrt N)" are neglected [src: arXiv:2511.07517, Sect. 4.3]. Unite
  quotes both `Delta chi2_MAP` (3.3 sigma) and `Delta chi2_ML` (3.1 sigma)
  for Unite + BAO + CMB [src: arXiv:2609.05053, Sect. 8.2, Eq. 11].
- **Bayesian**: `log R = Delta log Z`, read on the Trotta 2008 scale [src:
  arXiv:2511.07517, Sect. 4.3; arXiv:2609.05053, Sect. 8.2]. DES-Dovekie's
  argument for quoting both: preference is driven by `Delta chi2` in both
  cases, and the difference lies in the complexity penalty [src:
  arXiv:2511.07517, Sect. 4.3].
- **Priors for the evidence** (DES-Dovekie): `H0` in (0.55, 0.91) [as
  printed, i.e. `h`], `w0 ~ U(−3, −0.4)`, `w_a ~ U(−3, 2)`,
  `Omega_k` in (−0.15, 0.15), `Omega_m` in (0.1, 0.5), `w0 + w_a < 0`;
  reasons: `Omega_m > 0.5` "is inconsistent with a wide range of other
  galaxy surveys", the `w0` upper bound avoids confusing dark energy with
  curvature or matter, the `Omega_k` range saves compute, and
  `w0 + w_a < 0` ensures matter domination; SN-only constraints that hit
  these bounds are quoted on broadened priors while the evidence keeps
  them [src: arXiv:2511.07517, Sect. 4.3].
- **Tension before combination**: Suspiciousness, `ln S = ln R − ln I`,
  prior-independent unlike `R`; `ln S < −5` strong, −5 to −2.5 moderate
  [src: arXiv:2609.05053, Sect. 8.1].

### Step 9. Blind, validate, unblind
<!-- key: step-9-blind-validate-unblind -->

- **Hide**: Pantheon+ hides the binned BBC residuals and shifts the
  CosmoSIS chains by unknown values [src: arXiv:2202.04077, Sect. II.3].
  Union3 fits separate absolute magnitudes per sample at flat LCDM
  `Omega_m = 0.3` and removes the differences; the choice of models and
  external data was also made blind [src: arXiv:2311.12098, Sect. I].
- **Criteria (DES-Dovekie, following DES-SN5YR)**: (i) reproduce the
  DES-SN5YR cosmology with the current code, with a flag restoring the
  Fitzpatrick 1999 bug and the old calibration weight, so that changes come
  only from the listed differences; (ii) recover the input cosmology of 25
  simulated samples (flat LCDM), fitted with a CMB prior in wCDM and
  `w0w_a`CDM; (iii) data–simulation reduced `chi2` between 0.7 and 3.0 for
  `z, x1, c, m_B, M_star, mu − mu_model` and the redshift and host-mass
  evolution of `x1` and `c` [src: arXiv:2511.07517, Sect. 6.3]. Recovered
  on average: `w = −0.9986 ± 0.0045`, `Omega_m = 0.316 ± 0.001`; and
  `w0 = −1.0027 ± 0.0223`, `w_a = −0.0325 ± 0.1015`, for input flat LCDM
  `Omega_m = 0.315` [src: Sect. 6.2].
- **Calibration checks carried with them**: 100 simulated tertiary-star
  catalogues with random offsets recovered within 1 sigma; tertiary stars
  doubled; DES `g − r` shift consistent between white-dwarf and
  tertiary-star solutions; equal or smaller Hubble scatter [src:
  arXiv:2511.07517, Sect. 6.3].
- **Unite**: 25 realisations at `Omega_m = 0.315`; mean biases
  `0.002 ± 0.002` (flat LCDM), `0.005 ± 0.010` and `w − w_true = 0.01 ±
  0.03` (flat wCDM); reduced `chi2` criterion 0.7–3.0 per survey, HST
  exempt for small numbers [src: arXiv:2609.05053, Sect. 5.2].
- **Coverage**: DES-SN5YR cites a test on 150 simulated DES-SN samples in
  which Bayesian contours and approximate Neyman intervals agree "at the
  > 95 % level" [sec: arXiv:2401.02945, Sect. VII.2, reporting Armstrong et
  al.].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Covariance matrix or quadrature sum
<!-- key: covariance-matrix-or-quadrature-sum -->

The "quadrature method" (shift each parameter, add shifts in quadrature)
cannot be reused by others in a new parameter space without refitting
every term, and ignoring the correlations it hides "not only
underestimates the uncertainties, but can lead to biased results"; this is
why Conley et al. moved to `C_syst` [src: arXiv:1104.1443, Sect. IV.1].
The one-at-a-time rows printed today are diagnostics of the full matrix,
not a quadrature budget (L2).

### Covariance matrix or explicit nuisance scales
<!-- key: covariance-matrix-or-explicit-nuisance-scales -->

BHS21 find the two equivalent when both are unbinned [src:
arXiv:2012.05900, Sect. V]. UNITY samples every systematic as a parameter;
Union3 notes that the Pantheon+ 2-sigma contour in `Omega_m`–`Omega_Lambda`
has 48 % of the area of its own, although about 97 % of
Pantheon+ SNe were considered for Union3, and that even with all small
systematic terms fixed to zero UNITY's contour is comparable to Pantheon+:
"UNITY1.5 assesses uncertainties much more conservatively" [src:
arXiv:2311.12098, Sect. V.2.1, Fig. 26 caption]. The authors call for a
comparison on the same inputs [src].

### Fit α and β with cosmology, or fix them
<!-- key: fit-alpha-and-beta-with-cosmology-or-fix-them -->

Conley et al. find correlation coefficients of about 0.2 between
`alpha, beta` and `Omega_m, w`; holding them fixed in `C_syst` biases them
and shrinks the inner contour by ~40 % on SNLS3 [src: arXiv:1104.1443,
Sect. IV.6]. They also warn against replacing marginalisation over `𝓜`
by its best-fit value `b/e` when `alpha` and `beta` are fitted in the same
likelihood, because `chi2` values at different `alpha, beta` stop being
comparable [src: Appendix C]. BBC sidesteps this by fitting `alpha, beta,
gamma` first in redshift bins (L2); the warning applies to anyone writing a
joint likelihood on light-curve parameters.

### Binned, unbinned or rebinned
<!-- key: binned-unbinned-or-rebinned -->

Unbinned costs an `N × N` inversion (1701 for Pantheon+, 2884 for Unite)
and a frozen sample; binned loses self-calibration of colour-, stretch- or
host-dependent systematics; rebinning in `{z, x1, c}` keeps most of the
gain [src: arXiv:2012.05900, Sect. V; arXiv:2306.05819, Sect. III]. BHS21
suggest the binned LSST and Roman systematic forecasts of their time be
redone, noting that inverting matrices of > 100 000 SNe is costly [src:
arXiv:2012.05900, Sect. V].

### BEAMS variants or a probability cut
<!-- key: beams-variants-or-a-probability-cut -->

Unite drops the BEAMS contamination variants from `C_syst` and applies a
"conservative" `P_Ia` cut instead [src: arXiv:2609.05053, Sect. 4.9]; the
cost is fewer SNe, the gain one fewer simulated population in the matrix.

### Budget on w or on a non-degenerate combination
<!-- key: budget-on-w-or-on-a-non-degenerate-combination -->

Unite presents its budget on `Q_H(z = 0.2)`, "similar to how S8 summarises
the constraints in the sigma8–Omega_m plane", with `Omega_m` and `w`
budgets only as figures [src: arXiv:2609.05053, Appendix A]. Budgets on
`w` from DES and Pantheon+ are therefore not directly comparable with
Unite's.

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| SNe lost for missing bias correction in some variant | < 1 % | Pantheon+ | arXiv:2202.04077 | Sect. II.2 |
| `mu_ref` for redshift systematics | flat LCDM, `Omega_M = 0.3` | Pantheon+ | arXiv:2202.04077 | Eq. 6 |
| Variance weights | 1/10 (SALT3 + calibration, host masses), 1/4 (dust), 1/3 (MW colour law), 1/6 (redshift shift) | Unite | arXiv:2609.05053 | Table 4 |
| Duplicate-SN term after reimplementation | `sigma_QH` 0.002 → 0.003; `Delta Q_H` 0.004 → 0.005 | Unite | arXiv:2609.05053 | Sect. 5.2 |
| `S_zeta` in photometric unbinning | a few percent above 1 | BBC simulations | arXiv:2306.05819 | Sect. III |
| Simulated samples for unbinning test | 50, ~2000 events each | DES-like | arXiv:2306.05819 | abstract |
| Magnitude constant at h = 0.7 | 43.15861 | Union3 | arXiv:2311.12098 | Eq. A5 |
| Prior on `𝓜_B` | `N(−19, 0.3^2)` | Union3 | arXiv:2311.12098 | Appendix B |
| Spline nodes | 22, Δz = 0.05 to 0.8 then 0.1 | Union3 | arXiv:2311.12098 | Sect. V.2.1 |
| PolyChord settings | 250 live points, 30 repeats, tolerance 0.1 | Pantheon+ | arXiv:2202.04077 | Sect. II.3 |
| `sigma(log Z)` | ~0.2 | DES-Dovekie | arXiv:2511.07517 | Sect. 4.3 |
| Evidence priors | `h` (0.55, 0.91); `w0` (−3, −0.4); `w_a` (−3, 2); `Omega_k` (−0.15, 0.15); `Omega_m` (0.1, 0.5) | DES-Dovekie | arXiv:2511.07517 | Sect. 4.3 |
| Suspiciousness thresholds | strong < −5; moderate −5 to −2.5 | Unite | arXiv:2609.05053 | Sect. 8.1 |
| Data–simulation reduced `chi2` window | 0.7–3.0 | DES-Dovekie, Unite | arXiv:2511.07517; arXiv:2609.05053 | Sect. 6.3; Sect. 5.2 |
| Validation simulations | 25 | DES-Dovekie, Unite | arXiv:2511.07517; arXiv:2609.05053 | Sect. 6.2; Sect. 5.2 |
| Coverage test | 150 realisations, > 95 % agreement | DES-SN5YR | arXiv:2401.02945 | Sect. VII.2 `[sec]` |
| Effect of fixing α, β in `C_syst` | inner contour ~40 % too small | SNLS3 | arXiv:1104.1443 | Sect. IV.6 |
| Union3 post-unblinding prior-bound test | `Omega_m` −0.007 (~1/4 sigma) | Union3 | arXiv:2311.12098 | Appendix B |
| Unite largest post-unblinding shift | 0.3 sigma (SN-only flat LCDM) | Unite | arXiv:2609.05053 | Sect. 5.2 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Sample changes between variants.** The matrix is ill-defined; seen as a
  non-positive-definite or noisy `C_syst`. Test: identical SN lists in
  every variant [src: arXiv:2202.04077, Sect. II.2].
- **Duplicates inherited inconsistently.** Unite's first version kept the
  Pantheon+ off-diagonal entries; the dedicated implementation raised the
  duplicate term from 0.002 to 0.003 on `sigma_QH` [src: arXiv:2609.05053,
  Sect. 5.2].
- **Wrong ensemble weights.** The DES-SN5YR calibration weight error (L2)
  is the case; check that the weights of each ensemble sum to one unit of
  variance.
- **Redshift systematics without the model term** of Pantheon+ Eq. 6: a
  redshift shift then enters as zero distance change.
- **Unbinned photometric samples without the BEAMS factor**: the event
  errors must be inflated by `1/sqrt(P_B(Ia))` and rescaled by `S_zeta`;
  the weighted residual per bin must vanish [src: arXiv:2306.05819,
  Eqs. 10–11].
- **Fixing α and β, or plugging in the best-fit 𝓜, in a joint fit**:
  biased parameters and errors [src: arXiv:1104.1443, Sect. IV.6,
  Appendix C].
- **Prior-limited SN-only `w0w_a` fits** quoted as measurements;
  DES-Dovekie quotes such cases on broadened priors [src:
  arXiv:2511.07517, Sect. 4.3]. Unite adds that SN posteriors in `w0`–`w_a`
  are non-Gaussian with a "strong hook" near `w_a = 0`, so projection
  effects are expected [src: arXiv:2609.05053, Sect. 8.2].
- **Wilks applied as exact**: it is approximate at `O(1/sqrt N)` [src:
  arXiv:2511.07517, footnote 12].
- **Reading the Union3 spline errors as per-node independent errors**: part
  of the covariance is common to all nodes and degenerate with `𝓜_B`,
  which inflates the displayed errors [src: arXiv:2311.12098, Fig. 25
  caption].
- **Errors found only after unblinding.** Unite's per-survey residuals
  showed a ~2 sigma SNLS offset, traced to the omitted radial dependence of
  the SNLS filters (Regnault et al. 2009) and reduced to ~0.9 sigma; a
  hidden `chi2/dof` selection on high-S/N low-z data had removed five
  calibrator light curves [src: arXiv:2609.05053, Sect. 5.2]. Per-survey
  residuals belong among the pre-unblinding tests.
- **The `w(z)` form.** The HTML rendering of Pantheon+ Sect. II.3 prints
  `w = w0 + w_a (1+z)` [src: arXiv:2202.04077, Sect. II.3], whereas Union3
  and DES-Dovekie print `w = w0 + w_a (1 − a)` [src: arXiv:2311.12098,
  Sect. V.3; arXiv:2511.07517, Eq. 4]. Not resolved here; check the
  journal version before reusing the Pantheon+ expression.

## Reading list
<!-- key: reading-list -->

- Conley et al. 2011, arXiv:1104.1443 — foundation: Sect. IV.1 for the
  systematics covariance, IV.6 for the cost of shortcuts, Appendix C for
  analytic marginalisation over `𝓜`.
- Goliath et al. 2001, arXiv:astro-ph/0104009 — foundation: the
  marginalisation that Conley et al. and Unite cite (not read here).
- Brout, Hinton & Scolnic 2021, arXiv:2012.05900 — method: why unbinned
  matrices self-calibrate, Sects. II.2–II.4 and V.
- Kessler, Vincenzi & Armstrong 2023, arXiv:2306.05819 — method:
  unbinning and rebinning for photometric samples, Sect. III.
- Brout et al. 2022, arXiv:2202.04077 — application: Sects. II.2–II.3 for
  duplicates, frozen sample, redshift systematics, anchored likelihood and
  blinding.
- Vincenzi et al. 2024, arXiv:2401.02945 — application: Sect. III.6 and
  VII.2 for the difference form and the coverage test.
- Popovic et al. 2025, arXiv:2511.07517 — application: Sects. 4.1, 4.3, 6.2
  and 6.3 for priors, significance conventions and unblinding criteria.
- Camilleri et al. 2026, arXiv:2609.05053 — application: Sects. 3.1, 4.9,
  5.2 and 8 for weights, duplicates, post-unblinding changes and tension
  metrics.
- Rubin et al. 2023, arXiv:2311.12098 — method and critique: the spline
  compression and its check (Sect. V.2.1), and the claim that BBC
  uncertainties are smaller than UNITY's on overlapping data.

## Not verified
<!-- key: not-verified -->

- Goliath et al. 2001, Appendix A.1, not read; the marginalisation formula
  above is the Conley et al. version.
- The Armstrong et al. coverage paper behind the DES-SN5YR "> 95 %"
  statement (arXiv:2401.02945, Sect. VII.2) was not identified or read.
- The chain-shifting blinding formalism cited by Pantheon+ (its
  reference 49) was not identified. <!-- num: not a value -->
- Handley & Lemos 2019 (Suspiciousness) and Trotta 2008 (evidence scale)
  were not read; their use is quoted from Unite and DES-Dovekie.
- Whether Pantheon+'s printed `w(z)` is a rendering or a paper error.
