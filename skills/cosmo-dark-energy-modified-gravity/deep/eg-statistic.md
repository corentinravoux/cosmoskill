# The E_G statistic — cosmo-dark-energy-modified-gravity dossier

Scope: how an `E_G` measurement is built in each of its three current
forms (CMB lensing in harmonic space, galaxy–galaxy lensing in real space,
ratio of compressed Weyl and growth observables), where `beta` comes from,
how the error of a ratio and the scale-independence test are computed, and
which choices bias the result; for a reader about to measure, forecast or
referee an `E_G` value.
Snapshot: 2026-10-18.
From: DESI DR1 E_G paper (arXiv:2507.16098); ACT DR6 E_G paper (arXiv:2405.12795).

Already in L2, not repeated here: the definition after Zhang et al. 2007,
the GR prediction `E_G = Omega_m,0/f(z)` and its modified-gravity form
`Omega_m,0 Sigma/f`, the reference values 0.401 and 0.452 at `z = 0.555`
and 0.316 (`physics-and-methods.md#the-eg-statistic`); the measured values
and their history (`results.md#eg-measurements`); the headline systematic
budgets of 2% (CMASS) and 3% (LOWZ) and the Pullen et al. low value
(`systematics.md#modified-gravity-non-linear-scales-bias-and`); the
"still worth measuring?" debate (`open-questions.md#is-eg-still-worth-measuring`).
The pseudo-`C_ell` machinery and CMB-lensing map systematics belong to
`cosmo-cmb-lss-cross-correlations`.

Notation. `beta = f/b` is the redshift-space-distortion parameter, `f` the
linear growth rate, `b` the linear galaxy bias; `C_ell^{kappa g}` the
cross-spectrum of CMB lensing convergence and galaxy overdensity,
`C_ell^{gg}` the galaxy auto-spectrum; `W_g(z) = dN/dz` the normalised
galaxy redshift distribution; `chi` comoving distance; `z_eff` an
effective redshift. Sign conventions for the potentials differ: Wenzl et
al. write the numerator as `nabla^2 (psi − phi)` (arXiv:2401.12971, Eq. 5),
Rauhut et al. as `nabla^2 (Psi + Phi)` (arXiv:2507.16098, Eq. 21); both
reduce to `Omega_m,0/f` in GR. This dossier writes each paper's
equations in its own notation.

## How it is done
<!-- key: how-it-is-done -->

### Form A. CMB lensing × galaxy clustering, harmonic space
<!-- key: form-a-cmb-lensing-x-galaxy-clustering-harmonic -->

Reference implementation: Wenzl et al. 2024, arXiv:2401.12971 (Planck
PR4 × BOSS CMASS and LOWZ), reused unchanged for ACT DR6 by Wenzl et al.
2024, arXiv:2405.12795.

1. **Spectra in the Limber approximation.** `C_ell^{kappa g}` and
   `C_ell^{gg}` are projections of `P_{nabla^2(psi−phi) g}` and `P_gg` with
   the kernels of Eqs. 15–17; the CMB lensing kernel is
   `W_kappa(z) = (3 H0^2 Omega_m,0/2c^2) (1 + z) chi(z) [1 − chi(z)/chi(z_*)]`
   (Eqs. 18–19), with `W_hat_kappa` the same without the prefactor
   [src: arXiv:2401.12971, Sect. V.1].
2. **Match the effective redshifts.** The effective redshift of a spectrum
   is the kernel-weighted mean of `z` (Eq. 21). For one galaxy sample
   `z_eff` of the cross-spectrum (Eq. 22) and of the auto-spectrum (Eq. 23)
   differ, which "would bias the E_G estimation". Each galaxy entering the
   cross-correlation is given the extra weight
   `w_x(z) = (dN/dz)/[W_hat_kappa(z) I]`, `I = ∫ dz W_g^2/W_hat_kappa`
   (Eqs. 25–26), after which
   `z_eff^{cross*} = z_eff^{auto} = z_eff^{beta}` (Eq. 28). The galaxy
   sample must otherwise be treated identically in all three measurements
   (same weights) [src: Sect. V.1]. Stated reason: earlier estimators
   corrected the mismatch with simulations and an HOD; reweighting
   removes that dependence [src: Sect. V.1].
3. **Estimator.**
   `E_G^ell(z_eff) ≈ Gamma(z_eff) C_ell^{kappa g*}/(beta C_ell^{gg})`
   with `Gamma(z_eff) = (2 c H(z_eff)/3 H0^2) ∫ dz W_g^2(z)/W_hat_kappa(z)`
   (Eqs. 35–36), the only approximation being that `H(z)` varies slowly
   across the sample (Eqs. 33–34) [src: Sect. V.2].
4. **Magnification correction.** `Gamma → Gamma_ell = Gamma C_alpha^ell`
   with `C_alpha^ell = (C^{kappa g*}/C^{kappa g*,mag})(C^{gg,mag}/C^{gg})`
   (Eqs. 41–42), computed at the fiducial cosmology from measured
   magnification slopes `alpha` (LOWZ `2.47 ± 0.11`; CMASS
   `alpha(z) = 2.71 + 8.78 (z − 0.55)`, Eq. 40). The correction lowers
   `E_G` for any sample with `alpha > 1` [src: Sect. V.3.3].
5. **`beta` from a re-done RSD fit.** The BOSS DR12 power-spectrum
   multipoles and window matrices are refitted with the LPT model of
   velocileptors to `k_max = 0.2 h/Mpc`, with `f sigma8` and `b sigma8`
   free, `alpha_parallel, alpha_perp` free, and the linear spectrum and
   `sigma8(z)` fixed at Planck values; `beta = f sigma8/(b sigma8)` is
   derived per chain sample. Stated reasons: to use updated theory and to
   keep the cross-covariance of `f sigma8` and `b sigma8`, which the
   published results omit; `sigma8` is fixed because freeing it with
   BOSS signal-to-noise "can lead to undesirable parameter-volume
   effects" [src: Sect. VI.7]. The full pdf of `beta` enters `E_G`, and
   `beta` is assumed uncorrelated with the angular spectra because it
   comes from the 3D clustering [src: Sect. VII.1].
6. **Bandpowers and scale cuts.** NaMaster pseudo-`C_ell` (Eq. 44); all
   computations on `ell` in [2, 3071]; analysis on 11 log-spaced bins with
   edges [48, 59, 71, 87, 106, 129, 157, 191, 233, 283, 345, 420]; `ell_max`
   set by `k = 0.2 Mpc^-1` (≈ 30 Mpc comoving): 420 for CMASS, 233 for LOWZ
   (first 8 bins); `ell_min = 48` to avoid galaxy-map foregrounds
   correlating with lensing [src: Sect. VI.1].
7. **Covariance.** Sample covariance of 480 correlated simulated
   realisations of the lensing map and of the galaxy map with and without
   the cross-correlation weight (Eq. 52), Hartlap-corrected; checked
   against an analytic Gaussian covariance and a jackknife. Jackknife
   errors pass if on average 10–20% larger than the baseline with no
   outlier above 50% (found: about 20%, 0–50%) [src: Sect. VI.3]. For ACT:
   400 realisations; correlation between `C^{kappa g}` and `C^{gg}` in the
   same bin about 33% (CMASS) and 28% (LOWZ), falling at small scales
   [src: arXiv:2405.12795, Sect. VI.1.1].
8. **The ratio pdf, not Gaussian propagation.** The spectra are taken as
   correlated Gaussians and the pdf of their ratio is computed exactly,
   then divided by the `beta` pdf; the median is the estimate and the
   central 68.27% the interval [src: arXiv:2401.12971, Sect. VII.1].
9. **Two tests.** Consistency with GR:
   `PTE_GR = 1 − 2 |0.5 − P(E_G < E_G^GR)|` (Eq. 66), with the pdf
   convolved with the uncertainty of `E_G^GR` [src: Sect. VII.2]. Scale
   independence: minimum over a constant of a `chi^2` distance (Eq. 67),
   compared with a `chi^2` with `N_bins − 1` degrees of freedom,
   `PTE_scale-indep = P(chi^2 > chi^2_min)` (Eq. 69); `< 0.05` flags
   scale dependence, or an underestimated covariance, or a scale-dependent
   systematic. The `chi^2`-minimising constant is biased and is used only
   for the test [src: Sect. VII.3].

### Form B. Galaxy–galaxy lensing × projected clustering, real space
<!-- key: form-b-galaxy-galaxy-lensing-x-projected -->

Reference implementation: Rauhut et al. 2025, arXiv:2507.16098 (BOSS DR12
and DESI DR1 lenses × KiDS-1000, DES Y3, HSC sources), estimator of Reyes
et al. 2010.

1. **Observables.** Differential surface density `Delta Sigma(R)` from
   tangential shear (dsigma; DESI and mocks: 15 log bins in
   `0.08 < R < 80 h^-1 Mpc`; BOSS: 10 log bins in 0.5–50 for comparison
   with earlier work) and projected clustering `w_p(R) = ∫ xi_gg(R, Pi) dPi`
   (Corrfunc) [src: Sects. 4.2, 4.5; Eq. 17].
2. **Annular statistics.** To remove one-halo scales below `R_0`:
   `Upsilon_gm(R, R_0) = (2/R^2) ∫_{R_0}^{R} R' Sigma dR' − Sigma(R) + (R_0^2/R^2) Sigma(R_0)`
   (Eq. 18), in practice `Upsilon_gm = Delta Sigma(R) − (R_0/R)^2 Delta Sigma(R_0)`
   with `Delta Sigma(R_0)` interpolated (Eq. 38); `Upsilon_gg` the same on
   `rho_c w_p` (Eq. 19). Origin of the annular form: Mandelbaum et al. 2010
   and Baldauf et al. 2010 [src: Sect. 2.4]. PIP weights are not needed
   because only `R > R_0` is used [src: Sect. 4.5].
3. **Direct estimator.** `E_G(R, z) = Upsilon_gm/(beta Upsilon_gg)`
   (Eqs. 23, 43); linear bias and `sigma8` cancel since
   `beta ∝ 1/b`, `Upsilon_gm ∝ b sigma8^2`, `Upsilon_gg ∝ b^2 sigma8^2`,
   but `Omega_m` does not [src: Sect. 2.5]. Fractional errors add in
   quadrature (Eq. 44), the three pieces assumed uncorrelated because the
   lensing overlap is a small part of the clustering area; the `R` bins
   are then compressed to one value per lens bin with optimal weights
   [src: Sect. 4.7].
4. **Maximum-likelihood estimator.** Because a ratio of noisy quantities
   "may result in a biased or non-Gaussian result", a joint fit of
   `Upsilon_gm = A_E b_L Upsilon_gm(R; b_L, b_NL)` and
   `Upsilon_gg(R; b_L, b_NL)` with `delta_g = b_L delta + b_NL delta^2/2`
   (Eqs. 45–46), cosmology fixed; then `E_G(z) = Omega_m A_E/beta`. The
   `b_L` factor decorrelates `A_E` from bias. Method of Blake et al. 2020,
   Sect. 8.3 [sec: as described in arXiv:2507.16098, Sect. 4.8]. The bias
   model is valid only above the virial radius [src: Sect. 4.8].
5. **`R_0` from mocks.** In Buzzard mocks with `beta = f_fid/b_L`, the ML
   estimate was computed for `R_0 = 1, 2, 3, 4 h^-1 Mpc`; 3 recovers
   `Omega_m/f` and the mean deviation is zero to 2%; the threshold may
   differ in modified gravity because the mocks are GR [src: Sect. 5].
6. **`beta`.** BOSS: narrow-slice RSD values of Zheng et al. 2019; DESI:
   the DR1 full-shape chains converted sample by sample to `f/b_L`; LRG
   bins [0.4, 0.6], [0.6, 0.8], [0.8, 1.1] give
   `0.445 ± 0.074, 0.448 ± 0.064, 0.378 ± 0.059`; for BGS only the full
   `0.1 < z < 0.4` value `0.380 ± 0.103` exists and is applied to every
   BGS sub-bin [src: Sects. 6.1–6.2].
7. **Astrophysical terms.** `Delta Sigma = Delta Sigma_GGL + Delta Sigma_IA + Delta Sigma_mag`
   (Eq. 30), IA from NLA with `A_IA = 0.5`, `eta = 0`, lens magnification
   with `alpha_l = 2`; switching both off moves `E_G(z)` by 0.1σ on
   average [src: Sect. 2.6].
8. **Scale dependence.** `E_G(R, z_i) = A_i [1 + alpha log10 R]` (Eq. 47),
   GR at `alpha = 0`, after Blake et al. 2020 [src: Sect. 4.9].

### Form C. Ratio of compressed Weyl and growth observables
<!-- key: form-c-ratio-of-compressed-weyl-and-growth -->

Grimm, Bonvin and Tutusaus 2024, arXiv:2403.13709, define
`E_G(z) = (𝓗(z)/𝓗0)^2 (1 + z)^-1 J_hat(z)/f_hat(z)` (Eq. 3), where
`f_hat = f sigma8` from RSD and `J_hat` is the amplitude of the Weyl
potential measured from DES Y3 galaxy–galaxy lensing and clustering
assuming GR only at a high reference redshift `z_*`; without the
`𝓗` prefactor the GR value would be `Omega_m(z)/f(z)` [src: Sect. II].
The two observables come from different surveys and redshifts, so
`f_hat` is reconstructed at the four DES MagLim redshifts from 22
literature values (`0.001 ≤ z ≤ 1.944`) by cubic splines with the four
values as free parameters; Gaussian processes were rejected because the
result was dominated by the hyperparameter prior, and four knots were
chosen by the AIC [src: Sect. II, Table 1]. Precision 6.0–11.3% at four
redshifts, at most 1.6σ from GR [src: abstract]. Zhang et al. 2026,
arXiv:2604.24631, apply the same ratio (their Eq. 19) to KiDS-1000 ×
BOSS/2dFLenS, evaluated per posterior sample; `sigma8(z)` cancels in
`J_hat/f_hat`, which is why `E_G` remains a "No-Prior" GR test when `J_hat`
and `f_hat` separately cannot be compared with GR [src: Sect. 2.2]; they
set `z_* = 5` [src: Sect. 2.1].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Lensing source: CMB or galaxies
<!-- key: lensing-source-cmb-or-galaxies -->

CMB lensing gives one source plane, harmonic-space cuts in `k`, and no
intrinsic alignments; galaxy lensing gives tomography and smaller
scales but needs `R_0`, IA and magnification modelling. Leonard,
Ferreira and Heymans 2015, arXiv:1510.04287, note that scale-dependent
bias is worse in the real-space statistic "than it would be in the case
of the original Fourier-space statistic, in which case truncation at a
particular value of `k` could eliminate all effects" [src: Sect. 5].

### Direct ratio or maximum likelihood (real space)
<!-- key: direct-ratio-or-maximum-likelihood-real-space -->

In Buzzard mocks the direct estimator of Eq. 43 is "consistently biased
low", which the authors attribute to the ratio of noisy quantities, not
to non-linear bias (earlier simulation studies found a smaller low bias
of that origin); the ML estimator is unbiased to 2% at `R_0 = 3 h^-1 Mpc`
[src: arXiv:2507.16098, Sect. 5]. Use the ML values for the headline;
Rauhut et al. list ML values in their Table 3.

### Full ratio pdf or Gaussian propagation (harmonic space)
<!-- key: full-ratio-pdf-or-gaussian-propagation-harmonic -->

For a Planck + CMASS-like covariance at the fiducial cosmology, the pdf of
the estimator is skewed: mean 2.0% high, mode 3.6% low, median within
0.2% of the input. Gaussian propagation underestimates the upper 1σ error
by 12% (0.060 against 0.068) and overestimates the lower by 11% (0.060
against 0.054); at 2σ the upper error is 24% low (0.121 against 0.16)
[src: arXiv:2401.12971, Sect. VII.1]. Consequence: a low `E_G` quoted with
Gaussian errors overstates its tension with GR. Scaling the theory
`C^{kappa g}` by 0.7 reproduces the 2.6σ of Pullen et al. under Gaussian
statistics [src: same]. In the ACT analysis, assuming Gaussianity moves
the values but not the conclusion [src: arXiv:2405.12795, Sect. VI.3].
The scale-independence test calibrated on 480 simulations and on 100,000
Gaussian draws follows the `chi^2` with `N_bins − 1` d.o.f.; `PTE_GR` on
the simulations is flat [src: arXiv:2401.12971, Sects. VII.2–VII.3].

### Reweighting or simulation-based redshift correction
<!-- key: reweighting-or-simulation-based-redshift -->

Without the cross-correlation weight the estimator carries "a
scale-dependent bias of multiple percent, depending on dN/dz"
[src: arXiv:2401.12971, Sect. V.2]; with it, the residual approximation
error `|S_Gamma − 1| < 0.3%` on all scales, against a few percent for the
Pullen et al. estimator, which needed an N-body + HOD correction
[src: Sect. V.3.1]. The weight also changes the shot noise; with FKP
weights the net effect for BOSS was a variance decrease [src: Sect. V.2].

### Same sample or two independent observables
<!-- key: same-sample-or-two-independent-observables -->

Forms A and B need lensing, clustering and RSD on one galaxy sample with
identical weights (Sect. V.1 of arXiv:2401.12971). Form C combines
bias-free observables from different surveys, at the price of
reconstructing `f_hat` at the lensing redshifts and of assuming GR at
`z_*` [src: arXiv:2403.13709, Sect. II]; Grimm et al. present it as "a
novel approach ... with improved precision" [src: abstract]. Its
`J_hat` values were obtained "using CMB priors and standard scale cuts"
[src: Table 2 caption], so the independence from early-universe
information is not complete.

### Source of `Omega_m,0` and the nonlinear-bias correction
<!-- key: source-of-omegam-0-and-the-nonlinear-bias -->

Leonard et al. 2025, arXiv:2511.19194 (LSST DESC), simulate a
posterior-predictive test of GR with LSST sources and DESI LRG lenses,
restricted to `r_p ≥ 5 Mpc/h`: draw `Omega_m` from its prior, fit a
constant (reject GR if the `chi^2` fails), fit `Omega_m^fit` under GR,
draw replicated `E_G = Omega_m^fit/f`, and reject GR if the measured
constant lies outside the central 95% of the replicated values
[src: Sect. V.1]. The `Omega_m` prior decides the power (table below).
They also correct for nonlinear bias with
`C_b(r_p) = Omega_m Upsilon_gg/(b_1 Upsilon_gm)` computed from a fitted
LPT bias model (Eqs. 51–52) and propagate its uncertainty (Eq. 53); with
the correction no `E_G(r_p)` point needs cutting, whereas without it
"a large number of small-scale data points" fail the linear-scale
criterion [src: Sects. IV.3–IV.4]. The priors they test are GR-derived;
they recommend an `Omega_m` prior from analyses with extra gravitational
freedom for real data [src: Sect. V.2].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| `ell` range, CMB lensing × CMASS / LOWZ | 48 ≤ ℓ < 420 (11 bins) / first 8 bins (ℓ_max 233) | Planck PR4 × BOSS | arXiv:2401.12971 | Sect. VI.1 |
| Physical cut behind `ell_max` | `k = 0.2 Mpc^-1`, ≈ 30 Mpc comoving | same | arXiv:2401.12971 | Sect. VI.1 |
| Number of simulations for covariance | 480 (Planck); 400 (ACT) | — | arXiv:2401.12971; arXiv:2405.12795 | Sect. VI.3; Sect. VI.1.1 |
| `beta`, CMASS / LOWZ | 0.371 (+0.042/−0.055) / 0.338 (+0.058/−0.081) | velocileptors refit, `k_max = 0.2 h/Mpc` | arXiv:2401.12971 | Sect. VI.7 |
| `f sigma8`, `b sigma8` (CMASS) | 0.443 ± 0.048, 1.202 (+0.060/−0.034) | same | arXiv:2401.12971 | Sect. VI.7 |
| Estimator approximation error | `|S_Gamma − 1| < 0.3%` | — | arXiv:2401.12971 | Sect. V.3.1 |
| Bias evolution within sample | ≤ 1% (CMASS), ≤ 2% (LOWZ), from slopes `db/dz` 1.6 and 1.8 | — | arXiv:2401.12971 | Sect. V.3.2 |
| Magnification correction | 2–3% (CMASS), < 0.1% (LOWZ); its uncertainty ≤ 0.2% | — | arXiv:2401.12971 | Sect. V.3.3 |
| Lensing–galaxy overlap | ACT DR6 covers 34% of CMASS, 37% of LOWZ | — | arXiv:2405.12795 | Sect. VI.1.2 |
| Bias difference overlap vs full | `Delta b/b = (−0.9 ± 0.9)%` CMASS, `(0.8 ± 1.3)%` LOWZ; < 2.7%, < 3.4% at 95% | — | arXiv:2405.12795 | Sect. VI.1.2 |
| Statistical error of `E_G` | ~18% (ACT + CMASS), ~26% (ACT + LOWZ) | — | arXiv:2405.12795 | Sect. VI.1.2 |
| Scale independence, ACT + Planck + CMASS | `PTE_scale-indep = 0.53`; `PTE_GR = 0.31` | — | arXiv:2405.12795 | Sect. VI.4 |
| `R_0` | 3 h^-1 Mpc (tested 1–4); earlier works 1.5 | DESI DR1 × KiDS/DES/HSC; Reyes, Blake | arXiv:2507.16098; arXiv:1510.04287 | Sect. 5; Sect. 3.4 |
| Mock recovery | mean deviation consistent with zero to 2% (ML, `R_0 = 3`) | Buzzard | arXiv:2507.16098 | Sect. 5 |
| `beta`, DESI DR1 LRG bins | 0.445 ± 0.074, 0.448 ± 0.064, 0.378 ± 0.059; BGS 0.380 ± 0.103 | DR1 full-shape chains | arXiv:2507.16098 | Sect. 6.2 |
| `E_G(z)`, DESI DR1 × HSC-Y3, ML | 0.381 ± 0.070 (`z = 0.5`), 0.345 ± 0.055 (0.7), 0.352 ± 0.068 (0.95) | — | arXiv:2507.16098 | Table 3 |
| Scale-dependence slope `alpha` | 0.04 ± 0.14 (BOSS), −0.05 ± 0.09 (DESI); 0.17 ± 0.26 in Blake et al. 2020 | — | arXiv:2507.16098 | Sect. 6.4 |
| `E_G` from `J_hat/f_hat` | 0.447 ± 0.027 (`z = 0.295`), 0.378 ± 0.026 (0.467), 0.396 ± 0.033 (0.626) | DES Y3 `J_hat` + RSD compilation | arXiv:2403.13709 | Table 2 |
| GR rejection rate, LSST Y1 + DESI (**forecast**) | `f_R0 = 10^-4`: 0.023 (`sigma(Omega_m) = 0.03`, DES Y3-like) vs 0.924 (0.0084, Planck-like); nDGP `Omega_rc = 0.5`: 0.017 vs 0.559 | — | arXiv:2511.19194 | Table 1 |
| Same, LSST Y10 + DESI (**forecast**) | `f_R0 = 10^-4`: 0.021 vs 0.925 | — | arXiv:2511.19194 | Table 2 |
| `E_G` reach on μ, Σ (**forecast**) | ≈ 20% 1σ on `mu_bar_0`, `Sigma_0` from SKA2 + LSST, one redshift bin | — | arXiv:1510.04287 | Sect. 5 |

The DESI × HSC row is one of three source surveys; KiDS and DES give
different values in the same bins (e.g. 0.335 ± 0.068 and 0.253 ± 0.055
at `z = 0.5`) [src: arXiv:2507.16098, Table 3]. Quote the source survey.

## What goes wrong
<!-- key: what-goes-wrong -->

| Failure | How it shows | Test or fix | Source |
|---|---|---|---|
| `z_eff` of cross and auto spectra differ | scale-dependent percent-level bias | reweight the cross-correlation sample (Eq. 25); same weights elsewhere | arXiv:2401.12971, Sects. V.1–V.2 |
| Bias evolves within the redshift bin | `beta` and `C^{gg}` no longer cancel `b`; bias `S_b` (Eq. 38) | estimate from per-slice bias fits; narrower bins if comparable to errors; a bias trend cancelling a gravity deviation is not caught | arXiv:2401.12971, Sect. V.3.2 |
| Magnification ignored | `E_G` high by 2–3% for CMASS-like samples | `C_alpha^ell` from measured `alpha` | arXiv:2401.12971, Sect. V.3.3 |
| Lensing overlap is a biased sub-area | `C^{kappa g}` on the overlap, `beta C^{gg}` on the full sample | ratio of `C^{gg}` overlap/full, `Delta b/b = sqrt(A_Ratio) − 1` (Eq. 44) | arXiv:2405.12795, Sect. VI.1.2 |
| Gaussian error on a ratio | upper error too small, tension overstated | ratio pdf; report median and central 68.27% | arXiv:2401.12971, Sect. VII.1 |
| Direct ratio in real space | low bias in mocks | ML fit with `A_E` | arXiv:2507.16098, Sects. 4.8, 5 |
| Scale-dependent (nonlinear) bias | `E_G(R)` depressed at small `R`; does not cancel since `beta` carries only linear bias | raise `R_0` is insufficient for futuristic data; model `b(k)` or apply `C_b(r_p)` | arXiv:1510.04287, Sects. 3.3–3.4; arXiv:2511.19194, Sect. IV.4 |
| Short projection length `P` in `w_p` | `E_G(R)` lowered, more at large `R` (negative `xi` lost, RSD not cancelled); significant for SKA2 + LSST-like errors | predict with the `P` actually used; balance against noise | arXiv:1510.04287, Sect. 3.2 |
| `Omega_m,0` prior from GR fits | test power depends on the prior width; circularity | posterior-predictive test; prior from extended-gravity analyses | arXiv:2511.19194, Sect. V.2 |
| `R_0` chosen in GR mocks | non-linear threshold may move in modified gravity | state it; vary `R_0` | arXiv:2507.16098, Sect. 5 |
| Screening invisible | `E_G` cancels non-linear matter clustering under linear bias, so screening signatures are suppressed | do not use `E_G` as a screening test | arXiv:2511.19194, Sect. IV.1 |

Validation suite of the harmonic-space analyses: input recovery on
correlated simulations; jackknife errors 10–20% above the baseline with
no outlier above 50%; North–South consistency; full map against lensing
overlap; flat `PTE` distributions on the simulations; analysis choices
fixed before unblinding and sensitivity tests run afterwards (covariance
type, North or South only, overlap-only `C^{gg}`, no magnification
correction, no reweighting, Gaussian errors) [src: arXiv:2401.12971,
Sects. VI.3, VII; arXiv:2405.12795, Sect. VI.3]. The ACT paper also runs
misaligned-map, 90–150 GHz, CIB-deprojection and Websky foreground tests
(section titles read; details in `cosmo-cmb-lss-cross-correlations`).

Referee checks specific to `E_G`: which form (A, B or C) and which
estimator (direct or ML); `z_eff` matching; where `beta` comes from and
whether its full pdf is used; magnification and bias-evolution terms;
how the error of the ratio was computed; the scale-independence test
and its calibration; the source and width of `Omega_m,0`; the lensing
survey named when several give different values.

## Reading list
<!-- key: reading-list -->

- Foundation: Zhang et al. 2007, arXiv:0704.1932 — definition (read in L2).
- Foundation, real space: Reyes et al. 2010, arXiv:1003.2185 — the
  `Upsilon`-based estimator.
- Method, harmonic space: Wenzl et al. 2024, arXiv:2401.12971 — reweighting,
  `Gamma`, magnification, ratio pdf, PTE tests; the template for CMB lensing.
- Application: Wenzl et al. 2024, arXiv:2405.12795 — ACT DR6, overlap-bias
  test, ACT + Planck combination.
- Application, real space: Rauhut et al. 2025, arXiv:2507.16098 — DESI DR1
  × three lensing surveys, ML estimator, `R_0` from mocks, `beta` from
  full-shape chains.
- Method, alternative form: Grimm, Bonvin and Tutusaus 2024,
  arXiv:2403.13709 — `E_G` from `J_hat/f_hat`; Zhang et al. 2026,
  arXiv:2604.24631, for its application to KiDS-1000.
- Critique: Leonard, Ferreira and Heymans 2015, arXiv:1510.04287 —
  projection length, scale-dependent bias, `R_0`.
- Forecast and test design: Leonard et al. 2025, arXiv:2511.19194 —
  posterior-predictive test, `Omega_m` prior, nonlinear-bias correction.
- Method background: Blake et al. 2020, arXiv:2005.14351 — origin of the ML
  estimator and of the `alpha log10 R` test (cited through
  arXiv:2507.16098; body not read).

## Not verified
<!-- key: not-verified -->

- The body of Blake et al. 2020 (arXiv:2005.14351) and of Pullen et al.'s
  2014 harmonic-space estimator paper (cited in the sibling
  `cosmo-cmb-lss-cross-correlations`); their methods are described here
  only as Rauhut et al. and Wenzl et al. report them.
- The full systematic budget of arXiv:2401.12971 summing to 2% and 3%: only
  the components above (0.3%, bias evolution, magnification) were read;
  the remaining items were not traced.
- The historical values in arXiv:2604.24631, Table 1 (Blake 2016, Amon
  2018, Alam 2016) were not read in their own papers.
- ACT null-test pass criteria (only section titles read).
