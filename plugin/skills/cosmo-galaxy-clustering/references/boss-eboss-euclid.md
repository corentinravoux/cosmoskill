# Galaxy clustering — BOSS, eBOSS and the Euclid spectroscopic survey

Scope: the final BOSS DR12 and eBOSS DR16 clustering analyses (samples,
weights, mocks, consensus values with their effective redshifts, systematic
budgets) and the plan for Euclid's spectroscopic clustering analysis
(selection, purity, nuisance model, covariance, blinding), set beside DESI
practice. DESI detail is in the other reference files; survey hardware and
release dates in `surveys-and-data.md`. Snapshot: 2026-10-20.

Flags: `[src]` read this session in the cited paper (abstract); `[src: …]`
read in the body at the place given; `[der]` derived here.

## 1. BOSS DR12: sample, weights and mocks
<!-- key: boss-dr12-sample-weights-and-mocks -->

**Sample** [src: arXiv:1607.03155, Sect. 2.2, Table 2]. LOWZ, CMASS and two
early LOWZ selections combined into one sample over 0.2 < z < 0.75, cut into
three overlapping bins. Completeness-weighted area 10,087 deg², of which
759 deg² vetoed, leaving 9329 deg².

From arXiv:1607.03155, Table 2:

| Bin | N (NGC + SGC) | V_eff [Gpc³] | V [Gpc³] |
|---|---|---|---|
| 0.2 < z < 0.5 | 604,001 | 3.7 | 6.4 |
| 0.4 < z < 0.6 | 686,370 | 4.2 | 7.3 |
| 0.5 < z < 0.75 | 594,003 | 4.1 | 12.3 |

V_eff uses P_0 = 10⁴ h⁻³ Mpc³ and h = 0.676 (arXiv:1607.03155)
[src: Table 2 caption; h = 0.676 also in Sect. 2.2].

**Weights** (Ross et al. 2017, arXiv:1607.03145) [src: Sects. 4, 4.1]:

- Close-pair (fibre-collision) and redshift-failure weights combined as
  w_z = w_cp + w_noz − 1, defined in the DR12 catalogue paper.
- Imaging: the CMASS density depends on stellar density (null-test χ² = 211
  for 10 bins, against 9.6–11.1 for the LOWZ selections, which get no stellar
  weight); the dependence varies with the fibre magnitude i_fib2 and is fitted
  as n_gal = A(i_fib2) + B(i_fib2) n_star in five i_fib2 bins. Seeing weights
  are also applied to CMASS [src: arXiv:1607.03155, Sect. 2.2].
- The simulated systematic trends "impart no bias" on BAO and have a minor
  effect on its uncertainty [src: arXiv:1607.03145, abstract]. For growth,
  four treatments of the stellar-density systematic were each applied to 200
  mocks; the resulting fσ8 values are in arXiv:1607.03145, App. D, Table 9.
- The spread of fσ8 between those treatments is small compared with the
  per-mock error in the same table; this comparison is made here [der].

**Mocks and covariance** [src: arXiv:1607.03155, Sect. 4]: 1000 MD-Patchy
(second-order LPT with stochastic halo biasing) and 1000 QPM (low-resolution
particle mesh) mocks. Final errors use MD-Patchy because its errors are
"roughly 10-15 per cent larger" and its clustering matches the data better;
NGC and SGC covariances each come from 997 mocks, three being removed for
non-Gaussian clustering; the finite-mock correction is that of Percival et
al. 2014 (arXiv:1312.4841).

## 2. BOSS DR12: systematic budget and consensus
<!-- key: boss-dr12-systematic-budget-and-consensus -->

**Systematic model** [src: arXiv:1607.03155, Sects. 7.3–7.4]:

- α (isotropic dilation): 0.003 for measurement and fitting plus 0.003 for
  galaxy-bias astrophysics, in quadrature 0.0042; ε (anisotropic warping):
  0.005, kept at that value because RSD-modelling errors could leak into ε
  through the broadband AP signal (arXiv:1607.03155) [src: Sect. 7.4].
- fσ8: 0.024, 0.015, 0.009 for the low, middle and high bin, the maximum of
  the MD-Patchy bias and the high-resolution mock estimate (method in
  `rsd-modelling.md`, Sect. 7) (arXiv:1607.03155) [src: Sects. 7.3–7.4;
  values as the systematic errors of Table 7].
- Systematics correlated between redshift bins with coefficient 0.75: a
  common mode carrying 0.87 of the total plus independent parts of 0.50;
  "the variance of the common mode is 10-fold larger than the variance of
  the two other modes" (arXiv:1607.03155) [src: Sect. 7.4].
- The baryon–dark-matter relative velocity is excluded from the budget; a
  0.3% rms limit on its BAO shift is cited from the DR12 three-point
  function, and adding it to the template moves α by at most 0.3σ
  (arXiv:1607.03155) [src: Sect. 7.4].

**Consensus values** (BAO+FS, statistical then systematic error;
r_d,fid = 147.78 Mpc) [src: arXiv:1607.03155, Table 7]:

| z_eff | D_M (r_d,fid/r_d) [Mpc] | H (r_d/r_d,fid) [km/s/Mpc] | fσ8 |
|---|---|---|---|
| 0.38 | 1518 ± 20 ± 11 | 81.5 ± 1.7 ± 0.9 | 0.497 ± 0.039 ± 0.024 |
| 0.51 | 1977 ± 23 ± 14 | 90.5 ± 1.7 ± 1.0 | 0.458 ± 0.035 ± 0.015 |
| 0.61 | 2283 ± 28 ± 16 | 97.3 ± 1.8 ± 1.1 | 0.436 ± 0.034 ± 0.009 |

- Full-shape-only consensus fσ8: 0.502 ± 0.041 ± 0.024, 0.459 ± 0.037 ±
  0.015, 0.419 ± 0.036 ± 0.009 (arXiv:1607.03155) [src: Table 7].
- D_V(0.38, 0.51, 0.61) = (1477 ± 16, 1877 ± 19, 2140 ± 22) Mpc × (r_d/r_d,fid),
  i.e. 1.1%, 1.0%, 1.0% (arXiv:1607.03155) [src: Sect. 8.2, Eqs. 21–23].
- Aggregate precision across the three bins, systematics included: 1.0% on
  the transverse scale, 1.6% radial, 0.8% on D_V, 5.7% on fσ8
  (arXiv:1607.03155) [src: Sect. 8.2].
- Table 8 gives the 9 × 9 covariance and precision matrices; the on-line
  files carry full precision [src: Table 8 caption].
- H(0.51) is 90.5 ± 1.7 ± 1.0 in Table 7 but 90.4 in the Table 8 mean
  column; quote Table 7 and the likelihood files (arXiv:1607.03155)
  [src: Tables 7–8].

## 3. eBOSS DR16: samples, weights and the SDSS compilation
<!-- key: eboss-dr16-samples-weights-and-the-sdss -->

**Spectroscopic completeness** (Ross et al. 2020, arXiv:2007.09000)
[src: Sect. 5.3, Eqs. 2–4]:

- Close pairs: an unobserved target in a collision group with an observed
  one; its weight is shared among the good observations of the group,
  w_cp = (N_cp + N_z + N_badclass + N_star)/(N_z + N_badclass + N_star).
  This "provides unbiased transverse clustering on large-scales in
  configuration space", but radial clustering is biased and "the issues are
  more severe in Fourier space"; the catalogues provide w_cp and leave the
  residual to each analysis, with PIP weights as the unbiased alternative
  (Mohammad et al. 2020, arXiv:2007.09005; see `systematics.md`, Sect. 4).
- Redshift failures: weights from fitted trends of redshift efficiency with
  the squared i-band spectrograph signal-to-noise and with fibre ID (position
  on the CCD and on the plate). LRG efficiency depends more strongly on
  signal-to-noise than quasar efficiency, because LRG redshifts rest on
  absorption features.

**Imaging weights** [src: arXiv:2007.09000, Sect. 5.5, Eq. 13, Table 5]:
w_sys = [A_sys + C_sys · P]⁻¹ from a multivariate linear regression of
projected density on HEALPix maps (N_side = 512 for imaging, 256 for stars),
separately for NGC and SGC: quasars against g-band depth, E(B−V), i-band sky
and i-band PSF; LRGs against stellar density, E(B−V), sky and PSF. The airmass
trend disappears although airmass is not regressed, because it enters through
depth.

**Combined SDSS measurements** (eBOSS Collaboration 2021); Gaussian
approximations, correlations ignored. From arXiv:2007.08991 [src: Table 3]:

| Sample | z range | N | z_eff | V_eff [Gpc³] | BAO only | fσ8 (RSD only) | BAO+RSD |
|---|---|---|---|---|---|---|---|
| MGS | 0.07–0.2 | 63,163 | 0.15 | 0.24 | D_V/r_d = 4.47 ± 0.17 | 0.53 ± 0.16 | D_V/r_d = 4.51 ± 0.14 |
| BOSS galaxies | 0.2–0.5 | 604,001 | 0.38 | 3.7 | D_M/r_d = 10.23 ± 0.17, D_H/r_d = 25.00 ± 0.76 | 0.500 ± 0.047 | 10.27 ± 0.15, 24.89 ± 0.58, fσ8 = 0.497 ± 0.045 |
| BOSS galaxies | 0.4–0.6 | 686,370 | 0.51 | 4.2 | 13.36 ± 0.21, 22.33 ± 0.58 | 0.455 ± 0.039 | 13.38 ± 0.18, 22.43 ± 0.48, fσ8 = 0.459 ± 0.038 |
| eBOSS LRG | 0.6–1.0 | 377,458 | 0.70 | 2.7 | 17.86 ± 0.33, 19.33 ± 0.53 | 0.448 ± 0.043 | 17.65 ± 0.30, 19.78 ± 0.46, fσ8 = 0.473 ± 0.041 |
| eBOSS ELG | 0.6–1.1 | 173,736 | 0.85 | 0.6 | D_V/r_d = 18.33 (+0.57, −0.62) | 0.315 ± 0.095 | 19.5 ± 1.0, 19.6 ± 2.1, fσ8 = 0.315 ± 0.095 |
| eBOSS QSO | 0.8–2.2 | 343,708 | 1.48 | 0.6 | 30.69 ± 0.80, 13.26 ± 0.55 | 0.462 ± 0.045 | 30.21 ± 0.79, 13.23 ± 0.47, fσ8 = 0.462 ± 0.045 |

BAO+RSD columns give D_M/r_d, D_H/r_d, fσ8. The Lyα columns of the same
table belong to `cosmo-lyman-alpha`.

- The eBOSS LRG sample adds the z > 0.6 tail of BOSS DR12 over the full
  9376 deg² BOSS footprint to 174,816 eBOSS LRGs, "more than doubles" the
  sample and lowers z_eff slightly [src: arXiv:2007.08991, Sect. III.1].
- 6dFGS and WiggleZ are left out of the SDSS compilation: 6dFGS adds about
  16% on the MGS result, WiggleZ has under 10% of the CMASS effective volume,
  and the overlap would complicate the covariance (arXiv:2007.08991)
  [src: Sect. III.1].
- Small differences between companion papers: the quasar consensus is
  D_M/r_d = 30.22 ± 0.79, D_H/r_d = 13.26 ± 0.47, fσ8 = 0.464 ± 0.045 in Hou
  et al. (arXiv:2007.08998, abstract) and 30.21 ± 0.79, 13.23 ± 0.47,
  0.462 ± 0.045 in Neveux et al. (arXiv:2007.08999, abstract, which prints
  D_H/r_drag = "3.23 ± 0.47", a typographical slip) and in Table 3 of
  arXiv:2007.08991 [src]. The ELG configuration-space BAO is
  D_V/r_d = 18.23 ± 0.58 (Raichoor et al., arXiv:2007.09007) against 18.33
  in Table 3, which is the Fourier-space value of de Mattia et al.
  (arXiv:2007.09008) [src]. Cite the compilation table, and say so.
- `results.md`, Sect. 1.3, keeps the per-paper values.

## 4. eBOSS DR16: systematic treatment
<!-- key: eboss-dr16-systematic-treatment -->

- **Modelling.** N-body mock challenges per tracer, with blind mocks in
  rescaled cosmologies; numbers in `rsd-modelling.md`, Sects. 6–7. "All
  galaxy and quasar tracers used both blind and non-blind mocks to assess
  their modeling systematic errors", and HOD variations were included [src:
  arXiv:2007.08991, Sect. III.1].
- **Blind mocks for quasars.** OuterRim halo catalogues rescaled to new
  cosmologies (Mead & Peacock method: positions, masses and velocities
  rescaled so that σ(R, z) matches the target), analysed with the OuterRim
  cosmology as fiducial [src: arXiv:2007.09003, Sects. 4.3–4.3.2].
- **Fiducial cosmology.** Template rescaled by α before fixing the σ8
  normalisation for galaxies; weak dependence on α_iso in Nseries mocks, with
  a 2% band marked in Fig. 15 [src: arXiv:2007.08991, App. A].
- **LRG budget** [src: arXiv:2007.08993, Table 10]: σ_sys on (α_⊥, α_∥, fσ8)
  = (0.013, 0.018, 0.024) CLPT-GS, (0.012, 0.017, 0.023) TNS, (0.012, 0.013,
  0.024) P_ℓ; observational effects are the largest single term (0.017–0.018
  on fσ8); all systematics are added in quadrature to the diagonal of the
  covariance.
- **Quasar redshift errors.** The survey requirement models redshift
  smearing as a Gaussian of rms 300 km/s below z = 1.5, rising as
  450(z − 1.5) + 300 km/s above; duplicate observations show wider tails,
  better fitted by two Gaussians [src: arXiv:2007.09003, Sect. 2.1, Eq. 1].
  Total quasar systematics: one third of the statistical error [src:
  arXiv:2007.08999, abstract].
- **ELG angular systematics.** The configuration-space ELG analysis models a
  radial integral constraint and uses an estimator that cancels angular modes
  [src: arXiv:2007.09009, abstract]; the Fourier analysis models the
  integral constraints from photometric variations inferred from the data
  [src: arXiv:2007.09008, abstract]. The full ELG data show only a 1.4σ
  preference for a BAO feature [src: arXiv:2007.09008].

## 5. Euclid spectroscopic survey: selection and data products
<!-- key: euclid-spectroscopic-survey-selection-and-data -->

Euclid Collaboration: Mellier et al. 2025 (arXiv:2405.13491):

- Target: luminous emission-line galaxies at 0.9 < z < 1.8 with Hα flux above
  the nominal limit 2 × 10⁻¹⁶ erg cm⁻² s⁻¹, from slitless spectroscopy with
  the NISP red grism; the catalogue is selected to maximise number density
  "while keeping the fraction of spurious redshift measurements under
  control" (arXiv:2405.13491) [src: Sect. 7.7.1; flux limit in Sect. 4.1]. The red grism range was chosen to be
  complementary to ground-based surveys, DESI targeting mainly lower
  redshifts "with significant overlap" [src: Sect. 2.1].
- Purity and completeness are measured on the Euclid Deep Fields; blue-grism
  exposures there give a reference sample of at least 120,000 galaxies with
  99% redshift purity and 99% completeness (arXiv:2405.13491)
  [src: Sects. 4.3.3, 7.7.1, 3.5.3].
- Redshifts: the z PDF may use priors favouring the strongest lines or the
  known Hα-emitter redshift distribution; the empirical prior gives the best
  purity and completeness [src: Sect. 7.5.2].
- Selection function: a random catalogue built by forward modelling from the
  noise level of the NISP exposures and approximate end-to-end simulations of
  the spectroscopic pipeline [src: Sect. 7.7.1]. The detection-model random
  of Monaco et al. 2025 (arXiv:2511.20856) is in `systematics.md`, Sect. 6.
- Data products: selected catalogue and randoms, reconstructed versions
  (Zel'dovich or least-action), 2PCF in both configuration and Fourier space
  ("it is important to measure them in both spaces"), the first five
  Legendre multipoles of the 2PCF, and the three-point function [src: Sect. 7.7.1].
- Status: no Euclid spectroscopic clustering measurement on data at the
  snapshot; releases in `surveys-and-data.md`, Sect. 2.2.

## 6. Euclid spectroscopic analysis: model, nuisance, covariance, blinding
<!-- key: euclid-spectroscopic-analysis-model-nuisance -->

**Performance-verification set-up** [src: arXiv:2405.13491, Sect. 8.1.1,
Table 5]: P_0, P_2, P_4 in four bins (0.9–1.1, 1.1–1.3, 1.3–1.5, 1.5–1.8;
mean z = 1, 1.2, 1.4, 1.65), k_max = 0.3 h Mpc⁻¹, chosen "to alleviate
so-called projection effects". Spectroscopic nuisance parameters per bin:
b_1 U(1, 3), b_2 U(−5, 5), a shot-noise parameter U(−1, 2), counterterms
c_0, c_2, c_4 fixed, and a "purity factor (assuming Poisson distributed
interlopers)" with fiducial values 0.195, 0.204, 0.306, 0.121 and a Gaussian
prior of width 0.01.

**Likelihood model (CLOE)** (Euclid Collaboration: Cardone et al. 2025,
arXiv:2510.09118) [src: Sects. 4.1–4.2, Eqs. 88–103]:

- The linear Kaiser form is not used; the model is based on the EFTofLSS,
  projected on Legendre multipoles with the AP rescaling and the volume
  factor (q_⊥² q_∥)⁻¹.
- Redshift errors: P × exp[−k²μ²σ_r²] with σ_r = c σ_err/H and a constant
  σ_err = 0.002, "the expected performance of the NISP spectrograph",
  computed in the fiducial cosmology (arXiv:2510.09118) [src: Sect. 4.2].
- Random outliers (line interlopers and noise interlopers) damp the power by
  (1 − f_out)², f_out = 1 − purity, constant within each bin; interlopers
  with their own clustering are left to "forthcoming work". The interloper
  cross-correlation model and its size are in
  `deep/spectroscopic-systematics.md` (Risso et al. 2025, arXiv:2505.04688).
- As printed, Eq. 90 integrates from −1 to −1; Eq. 94 has the intended
  −1 to 1 [src: Eqs. 90, 94].

**Covariance** [src: arXiv:2405.13491, Sect. 8.1.2]: Gaussian likelihood;
spectroscopic clustering treated as independent of the photometric 3×2pt
(shown "a reasonable approach for a Euclid-like mission"); covariance
evaluated at the fiducial model only; the survey footprint entered only
through f_sky. Euclid's semi-analytic covariance for BAO is in
`deep/bao-reconstruction-fitting.md` (arXiv:2605.03446).

**Blinding** [src: arXiv:2405.13491, Sect. 8.2.4]:

- The first 500 deg² are analysed unblinded; they are 1/30 of the final
  sample, so with variance scaling as inverse volume their error is 5.5 times
  larger (arXiv:2405.13491) [src: Sect. 8.2.4], "equivalent to blinding the signal at the 5.5σ level"; pipeline
  revisions are applied retrospectively only to this sample until DR1.
- For DR1, blinding is applied to derived statistics, not raw data: the
  two-point data products (ξ and P multipoles) are shifted by the expected
  difference between the Planck 2018 best-fit flat ΛCDM model and one drawn
  within 3σ, following the DES approach but with independent shifts for
  clustering and lensing, so that differences between probes are also blind.
- Contrast with DESI, which blinds the catalogue (`physics-and-methods.md`,
  Sect. 5), and with eBOSS, which blinded its modelling tests through blind
  mocks (Sect. 4).

## 7. Systematics treatment across collaborations
<!-- key: systematics-treatment-across-collaborations -->

| Item | BOSS DR12 | eBOSS DR16 | DESI DR1/DR2 | Euclid (planned) |
|---|---|---|---|---|
| Fibre or slit incompleteness | w_cp close-pair weights (arXiv:1607.03145) | w_cp; PIP + angular up-weighting tested (arXiv:2007.09000, arXiv:2007.09005) | θ-cut + window, PIP in tests (`systematics.md` Sect. 4) | slitless: no fibres; detection-probability randoms (arXiv:2405.13491) |
| Imaging | stellar density and seeing weights for CMASS, seeing for LOWZE3 | linear multi-map regression | linear, SYSNet, random forest; polynomial template | detection limit modulated by observing conditions; randoms forward-modelled from NISP noise (arXiv:2405.13491, Sect. 7.7.1) |
| Redshift failures | w_noz | S/N- and fibre-ID-dependent weights | success-rate modelling (`systematics.md` Sect. 6) | purity and completeness from Deep Fields; purity parameter in the fit |
| Model systematic | MD-Patchy bias and high-resolution challenge | N-body challenges with blind mocks | Abacus-based theory and HOD budget | EFT model with k_max = 0.3 (arXiv:2405.13491, Sect. 8.1.1), scale cuts for projection effects |
| Covariance | MD-Patchy (997 per cap in the consensus; arXiv:1607.03155, Sect. 4), Percival factor | EZmocks per tracer (not read here) | EZmocks (FS), RascalC (BAO) | analytic Gaussian (SPV) |
| Blinding | none described | blind mocks only | catalogue-level shifts | unblinded first 500 deg², then data-vector shifts (arXiv:2405.13491, Sect. 8.2.4) |

Sources for the BOSS, eBOSS and Euclid columns are Sects. 1–6 of this file;
the DESI column summarises `systematics.md` and `physics-and-methods.md`.
The eBOSS covariance entry and the absence of catalogue blinding in BOSS are
stated as not found in the sections read, not as verified absences.

## 8. What the BOSS–eBOSS experience implies for Euclid and DESI
<!-- key: what-the-boss-eboss-experience-implies -->

- Systematics comparable to the statistical error are not new: in eBOSS LRG
  they exceeded half the statistical error for every parameter [src:
  arXiv:2007.08993, Sect. 4.2.5]; in BOSS DR12 the fσ8 systematic was up to
  0.6σ of the mock scatter in the low bin [src: arXiv:1607.03155, Sect. 7.1].
- Consensus of several methods reduced both statistical error and bias on
  high-fidelity mocks [src: arXiv:1607.03155, Sect. 8.2, Fig. 9].
- Compressed fσ8 depends on the template and the fiducial cosmology; eBOSS
  recommended fitting the multipoles directly for DESI and Euclid [src:
  arXiv:2007.08991, App. A]; DESI DR1 did so with full modelling
  (`physics-and-methods.md`, Sect. 3), Euclid plans to with CLOE.
- In Weinberg et al.'s assessment, BAO is "a relatively easy" measurement
  because a systematic must have a sharp preferred scale to shift the peak,
  while broadband clustering needs "a factor of more than ten better
  accuracy" [src: arXiv:1201.2434, Sect. 4.5.1]; the same review names
  photometric miscalibration, redshift failures and fibre collisions as the
  measurement systematics and angular templates or mode projection as the
  remedies [src: Sect. 4.5.1].

## Not verified
<!-- key: not-verified -->

- The eBOSS covariance mocks (EZmocks per tracer) and their number: the
  sections read do not state them.
- Whether any BOSS DR12 analysis used catalogue or data-vector blinding: not
  found in the sections read.
- The Euclid DR1 spectroscopic sample size and the expected fσ8 precision per
  bin: not read (see `open-questions.md`, Sect. 11, for the forecast papers).
- CLOE paper 6 (systematic uncertainties, Euclid Collaboration 2025) was
  found by search but not read.
