# Systematics — CMB × LSS cross-correlations

Scope: the systematic effects that have moved published results in this domain, one subsection each (mechanism, size, mitigation, validation, reference), then the referee checklist.
Snapshot: 2026-10-13

Flags: `[src]` read this session in the cited paper; `[sec]` from a named secondary source;
`[der]` derived here. "σ" shifts are in units of the statistical error of the analysis that
reports them.

Cross-correlations are often introduced as immune to systematics. They are immune to additive
contamination that the two maps do not share. They are fully exposed to anything multiplicative
(normalisation, redshift distribution, bias model) and to contamination that both maps trace,
which is the case for every extragalactic foreground.

## 1. Normalisation of the lensing map on the overlap region
<!-- key: normalisation-of-the-lensing-map-on-the-overlap -->

**Mechanism.** A quadratic lensing estimator applied to a masked sky returns a misnormalised
convergence. The correction is a ratio of simulated spectra evaluated with the galaxy mask and
depends on the overlap region (`physics-and-methods.md`, Sect. 2.4).

**Size.** Omitting it lowered S_8 by 0.6σ in unWISE × Planck (Farren 2023, arXiv:2309.05659,
appendix table) and by ΔS_8 = 0.015 (about 0.5σ) in DESI LRG × Planck PR3 (Sailer 2024,
arXiv:2407.04607, section "Planck PR3 reanalysis") [src]. In amplitude: a nearly scale-invariant
increase of C_ℓ^κg by about 2% for unWISE × Planck PR4, with PR3 behaving alike; the dependence on
the footprint is below 1%; the ACT DR6 correction is "much larger" because of the Fourier-space
masking applied before reconstruction; with the correction, simulated spectra are recovered to
within 1% (arXiv:2309.05659) [src: App. "Lensing Monte Carlo Norm Correction"].

For ACT DR6 the two-dimensional Fourier filtering alone misnormalises the map by 10%, corrected
at map level on the full footprint; an extra transfer function is then computed on the DESI
overlap, and the two implementations of the correction (Kim 2024, arXiv:2407.04606, and
arXiv:2407.04607) agree to < 0.2σ on the lensing amplitude of each LRG bin and < 0.1σ for the
four bins together (arXiv:2407.04606) [src: Sect. 3.3].

**Mitigation and validation.** Monte Carlo correction per mask combination (480 Gaussian
simulations for Planck in arXiv:2309.05659 [src: App. I]); marginalisation of
the residual normalisation uncertainty in the covariance (arXiv:2309.05659) [src].

**Referee expects.** A statement that the correction was computed for the actual overlap, and
arXiv:2309.05659 cited for the effect in cross-correlation.

## 2. Extragalactic foregrounds in the lensing reconstruction
<!-- key: extragalactic-foregrounds-in-the-lensing -->

**Mechanism.** tSZ clusters and CIB galaxies in the temperature map produce a lensing-like
signal in the quadratic estimator. Because they trace the same structure as the galaxies, the
term ⟨Q(T_fg, T_fg) g⟩ biases the cross-correlation (arXiv:2309.05659, section "Simulation Based
Test for Extragalactic Foregrounds") [src].

**Size.** On WebSky simulations with unWISE-like galaxies, a reconstruction without bias
hardening is biased by −4.2σ (Blue) and −3.1σ (Green) in the cross-correlation amplitude; the
baseline with frequency co-adds and geometric profile hardening leaves |ΔA/σ| ≃ 0.04, and
deprojecting the CIB in addition brings no further gain. Polarisation carries about 30% of the
weight in the minimum-variance map, so the temperature-only test is an upper limit
(arXiv:2309.05659) [src]. For the ACT DR6 lensing auto-spectrum the same mitigation leaves a bias
below 0.2σ on A_lens (MacCrann 2023, arXiv:2304.05196) [src]. In that paper's table, for the
baseline range L ≤ 763: ΔA_lens = −0.0042 (WebSky) and −0.00088 (the second simulation) for the
minimum-variance estimator, error 0.023, that is −0.18σ and −0.04σ; temperature only, −0.012 and
−0.0024 for an error of 0.037 (−0.31σ and −0.06σ). The fractional bias on C_L^κκ stays within 2%
to L ≈ 500, and without profile hardening both cluster-model and source subtraction are needed
to reach the few-percent level (arXiv:2304.05196) [src: Sect. "Baseline Analysis", table of
A_lens biases]. For DESI LRGs, WebSky foreground-only reconstructions crossed with HOD-populated
mock LRGs give amplitude shifts of order 0.1σ or less in each of the four bins, temperature
only (arXiv:2407.04606) [src: Sect. 4.1].

Two more tracer-specific tests. BOSS CMASS- and LOWZ-like samples on WebSky: 0.1–0.2σ without
mitigation, below 0.02σ with the bias-hardened ACT DR6 estimator (Wenzl 2024, arXiv:2405.12795)
[src: Sect. 5.2.3, figure caption]. DES Y3 × SPT + Planck: the tSZ-cleaned lensing map lets the
fit use small scales that the Y1 analysis had to drop; the signal-to-noise of the fiducial
δ_g κ + γ_t κ vector is 34.8 without cuts, 23.9 with linear-bias cuts, 25.7 with non-linear-bias
cuts (arXiv:2203.12440) [src: Sect. 4, table of signal-to-noise].

**Estimators behind the mitigation** [src: abstract of each]. Bias hardening (Namikawa 2012,
arXiv:1209.0091); source hardening against point-source trispectra (Osborne 2013,
arXiv:1310.7547); profile hardening, in which all temperature foregrounds are treated as sources
of one profile (Sailer 2020, arXiv:2007.04325); a foreground-cleaned gradient leg (Madhavacheril
2018, arXiv:1802.08230); shear-only reconstruction (Schaan 2018, arXiv:1804.06403). Before
mitigation: percent-level bias on the lensing power needs masking of sources above 1 mJy at
150 GHz and clusters above 10¹⁴ M⊙, and ℓ_max ~ 2500 in the reconstruction (van Engelen 2013,
arXiv:1310.7023).

**Mitigation.** Source and cluster subtraction, profile bias-hardened estimators, CIB
deprojection with Planck high frequencies (arXiv:2304.05196); tSZ-cleaned lensing maps
(Chang 2022, arXiv:2203.12440; Shaikh 2023, arXiv:2309.04412); polarisation-only reconstruction,
now measurable at ~14σ with SPT-3G D1 × DES Y3 shear (Ouellette 2026, arXiv:2606.26223) [src: abstract].

**Null tests on data.** unWISE × ACT DR6 runs 28 null tests on C_ℓ^κg for its two samples and
finds four with PTE < 0.05 and none below 0.01, all for the Blue sample: minimum variance against
temperature-only, temperature-only against polarisation-only, minimum variance against
CIB-deprojected, and minimum variance against polarisation-only on the 40% Galactic mask. More
than four failures occur in 11% of 400 Gaussian simulations; the second and fourth tests are 77%
and 32% correlated with the first; the CIB-deprojected map uses a different mask
(arXiv:2309.05659) [src: Sect. 7.1].

**Validation.** Null tests between frequencies and between temperature and polarisation; two
independent sky simulations (arXiv:2304.05196); an analytic halo model of the bi- and trispectra
(CosmoBLENDER), which finds the shape of the bias for cross-correlations with low-redshift
galaxies to depend on Ω_m (Baleato Lizancos 2025, arXiv:2507.03859) [src].

**Case history.** Two Quaia analyses on Planck lensing suggested contamination of the lensing map
at z ≳ 1.5 (Alonso 2023, arXiv:2306.17748; Piccirilli 2024, arXiv:2402.05761). The ACT DR6 +
Planck PR4 analysis ran contamination and systematic null tests and finds "no evidence for
contamination in the lensing maps" (Embil Villagra 2025, arXiv:2507.08798) [src]. In detail:
18 null tests (polarisation-only, temperature-only, CIB-deprojected, 90 against 150 GHz, 40%
mask, curl), none with PTE < 0.05, and a Kolmogorov–Smirnov PTE of 0.43 for their distribution;
WebSky biases "well below 0.1" σ in both bins; the paper adds that the possible Planck
contamination "was found not to impact cosmological constraints" [src: Sect. V.1, V.2, Table 2].
For the DESI Legacy samples the WebSky bias is −0.01σ with the baseline and −0.19, −0.18, −0.07σ
without profile hardening (arXiv:2410.10808) [src: Sect. V.3].

## 3. CIB, dust and radio leakage in tSZ cross-correlations
<!-- key: cib-dust-and-radio-leakage-in-tsz-cross -->

**Mechanism.** A Compton-y map retains CIB and radio emission, and both correlate with any
low-redshift tracer and with lensing. The sign differs: dusty and radio emission add positive
flux where the tSZ is a decrement, below the tSZ null frequency.

**Size.**
- CIB "has a substantial impact" on DES Y3 shear × y and "must be taken into account" (Gatti
  2021, arXiv:2108.01600) [src].
- In numbers, for DES Y3 shear × Planck y: deprojecting a CIB modified blackbody (24 K, β = 1.2)
  changes the signal by χ² = 4, 12, 55 and 110 for 8 degrees of freedom in source bins 1 to 4,
  against 4, 8, 14 and 9 for the ACT map; masking radio sources changes the Planck measurement
  by χ² = 34 for 32; the cross-shear null gives 84/68 (Planck) and 93/80 (ACT); Planck and ACT
  measurements agree at 60/44. β = 1.6 fails to describe the data. The difference covariance is
  a jackknife restricted to θ < 40′ (arXiv:2108.01600) [src: Sect. 4.3, table of tests].
- For DES Y3 shear × ACT DR6 + Planck y: changing β in a β-only deprojection has "a significant
  impact", mostly on the two highest-redshift bins; deprojecting in addition the first moment of
  the spectrum with respect to β makes the measurement robust to β. The fiducial map assumes
  β = 1.7 and T_CIB = 10.70 K, has a 1.6′ beam, and covers f_sky = 0.087 with DES. Masking the
  ~20,000 point sources with 3′ holes changes the measurement slightly at high redshift; unresolved
  radio sources are left to future work; the CIB is not perfectly correlated between channels,
  so some leakage can remain (arXiv:2506.07432) [src: App. "Impact of systematics"; Sect. 2.1].
- For CMB lensing × y the residual CIB is "a serious systematic" because of the high CIB–κ
  correlation; the measured amplitude moves between 0.82 ± 0.21 and 0.56 ± 0.24 with the choice
  of lensing map (McCarthy 2023, arXiv:2308.16260) [src: abstract].
- For unWISE × multi-frequency maps, a model with a radio component is preferred at 9.5σ and
  11σ; without it the ACT DR6 NILC y map gives an apparent negative galaxy–tSZ correlation on
  small scales (Zhao 2026, arXiv:2606.28099) [src: abstract].
- For stacked tSZ on DESI LRG and BGS, dust and radio emission dominate the tSZ signal at and
  below the ~2′ aperture, while large-scale (R > 4′) CIB contamination is less significant (Moore
  2026, arXiv:2609.08939) [src].
- KiDS-1000 × y was found "insensitive to the CIB", with intrinsic alignments a small but
  significant contribution (Tröster 2021, arXiv:2109.04458) [src]. The statements differ because
  the y maps, scales and source redshifts differ; none transfers to another analysis.

- In the Planck y maps the residuals are thermal dust on large scales (the major contaminant at
  ℓ < 60 in 2013) and CIB and point sources on small scales (Planck Collaboration 2013,
  arXiv:1303.5081; Planck Collaboration 2015, arXiv:1502.01596) [src: abstract]. The tSZ–CIB correlation is
  detected in Planck data: stacked on clusters, the infrared emission is about 50% more extended
  than the tSZ signal (Planck Collaboration 2015, arXiv:1509.06555) [src: abstract].

**Mitigation.** CIB deprojection in the ILC; moment deprojection against a wrong CIB spectrum
(arXiv:2308.16260); fitting tSZ, CIB and radio jointly at the level of the multi-frequency
cross-spectra, with the CIB spectral parameters calibrated externally and marginalised (Wayland
2026, arXiv:2609.31774; arXiv:2606.28099; La Posta 2026, arXiv:2603.04269) [src].

**A stopping rule** (arXiv:2308.16260) [src: Sect. V.2, summary; Sect. IV.1]. Deproject the CIB
for several assumed spectra; if C_ℓ^yκ is not stable, add the δβ moment, then the δT moment, and
so on until it is. With the standard Planck frequency coverage stability comes only with both
moments; without 545 GHz, with δβ alone. The ISW–κ correlation is dominant or comparable to
tSZ–κ up to ℓ ~ 100–200, so the primary CMB is deprojected as well, on the first five needlet
scales.

**Validation.** Repeat the measurement with at least two differently cleaned y maps; show the
result against the CIB spectral index and with radio sources masked.

## 4. Redshift distribution of photometric tracers
<!-- key: redshift-distribution-of-photometric-tracers -->

**Mechanism.** At fixed data, a tracer placed at lower redshift has a larger C_ℓ^gg and a smaller
overlap with the lensing kernel, so the fit compensates by raising S_8 (arXiv:2309.05659) [src].

**Size.** Adding spectroscopic data to the unWISE cross-correlation redshifts raised S_8 by
0.8σ, the largest single term of the reanalysis; the Blue-sample dN/dz changed by 0.74σ and
Green by 0.14σ. Switching to a principal-component marginalisation of dN/dz moved S_8 by −0.2σ
and widened the posterior by ~15% (arXiv:2309.05659) [src: App. I, Table 10]. In galaxy lensing the
same class of error drove the old low S_8 values [sec: `cosmo-weak-lensing` SKILL.md].

**How the marginalisation is built** (arXiv:2309.05659) [src: Sect. 8.2]. 1000 Gaussian
realisations of the cross-correlation redshift estimate, spline-interpolated with a positivity
constraint; principal components of their difference from the best fit, kept up to 90% of the
variance (3 for Blue, 5 for Green), with skew-normal priors fitted to the coefficients. With 99%
of the variance (6 and 9 components) the mean parameters do not move and the error on S_8^×
grows by 2% (Blue) and 14% (Green). The positivity constraint and the dependence of C_ℓ^gg on
the square of the noisy distribution give a noise bias of up to 5% on some components of
C_ℓ^gg, corrected separately. The cross-match distribution, which enters only the bias-free
terms, is taken without error.

**Mitigation.** Direct spectroscopic calibration where it exists (DESI spectra for the Legacy LRG
and BGS samples: Zhou 2023, arXiv:2309.06443); marginalisation with a data-driven basis; an
explicit correction for the fiducial cosmology used in cross-correlation redshifts
(arXiv:2309.05659) [src].

**Validation.** Galaxy cross-spectra between bins; consistency of σ_8 between samples at
different redshift (arXiv:2309.05659) [src].

**Stacking analogue.** Void-lensing and ISW templates need mocks with the same photometric
redshift error and sparseness as the data; the "lensing-is-low" void signal disappears once the
Buzzard templates are recalibrated with DESI spectra (Sartori 2026, arXiv:2605.19763) [src].

## 5. Magnification bias
<!-- key: magnification-bias -->

**Mechanism.** Lensing by foreground matter changes the observed number counts with a
coefficient (5 s_μ − 2) and correlates directly with κ.

**Size.** Below 1% of C_ℓ^gg and up to ≃ 10% of C_ℓ^κg in the highest DESI LRG bin
(arXiv:2407.04607, section "From 3D to 2D") [src]. Those bins are narrow. For the broad unWISE
samples: below 1% of C_ℓ^κg for Blue and about 6% for Green; up to 5% of C_ℓ^gg for Green on large
scales; dropping the magnification terms moves S_8 by −0.2σ (arXiv:2309.05659) [src: Sect. 8.1.5].

**Priors in use.** Gaussian, centred on the measured slope: 10% wide for unWISE, s_μ =
0.455 ± 0.0455 (Blue) and 0.653 ± 0.0653 (Green) (arXiv:2309.05659) [src: Sect. 9.3, table of
priors]; width 0.1 for the DESI LRG bins, about ten times the Poisson error of the measured
slopes (arXiv:2407.04607) [src: Sect. 5.2]. In E_G the magnification correction is 2–3% for
CMASS and negligible for LOWZ (arXiv:2405.12795) [src: Sect. 6.3].

**Mitigation.** Measure s_μ on the actual selection; arXiv:2309.06443 publishes the coefficients
for the LRG samples [src]. Sailer 2025 (arXiv:2503.24385) turns the
effect into a signal, with a finite-difference calibration of the slope, and assigns a systematic
error of ±0.050 on σ_8, larger than its statistical error of ±0.047 [src]. The ±0.050 is the
shift from beyond-linear biasing: a synthetic vector with realistic non-linear bias, fitted with
the linear-bias magnification likelihood, returns σ_8 = 0.762 ± 0.052 for a true 0.82, of which
−0.015 is a volume effect. Evolution of s_μ inside the source bins moves σ_8 by −0.002
[src: Sect. III.2].

## 6. Bias model, scale cuts and projection effects
<!-- key: bias-model-scale-cuts-and-projection-effects -->

**Mechanism.** A flexible bias model has many weakly constrained parameters. Marginal means of
cosmological parameters then shift away from the best fit ("volume effect"), in a direction that
depends on priors.

**Size.** In the first DESI LRG × Planck analysis the mean S_8 (0.725) sat about 1σ below its own
best fit (0.751); a prior tying the two counterterms moved the mean by +0.014 while the best fit
moved by 0.005. With the new priors and ℓ_max = 600, tests on a noiseless model prediction give
shifts below σ/3 in every configuration and at most σ/10 for the baseline (arXiv:2407.04607,
sections "Volume effect estimation" and "Planck PR3 reanalysis") [src].

**Scale cuts and how they were set.**

| Analysis | κg range | gg range | Set by |
|---|---|---|---|
| unWISE × ACT DR6 (arXiv:2309.05659) [src: Sect. 4] | 50 ≤ ℓ ≤ 400 | 100 ≤ ℓ ≤ 400 | ℓ_min by systematics tests and the lensing mean field, ℓ_max by unbiased parameter recovery on mocks; fixed before unblinding |
| DESI LRG, HEFT (arXiv:2407.04607) [src: Sect. 5.1, table of scale cuts] | 20 ≤ ℓ < 600 (Planck), 44 ≤ ℓ < 600 (ACT) | 79 ≤ ℓ < 600 | ℓ_min where beyond-Limber corrections are below 1%; ACT mean field exceeds the signal at ℓ ≲ 30; ℓ_max ≃ χ(z_min) × 0.6 h/Mpc for the first bin |
| DESI Legacy galaxies × ACT DR6, linear bias (Qu 2024, arXiv:2410.10808) [src: Sect. III.1] | 50 ≤ ℓ ≤ 154, 221, 283 (k_max = 0.15, 0.16, 0.17 h/Mpc) | same | ℓ_max where the non-linear part of P_mm reaches 10% of the linear one; a tighter cut moves S_8 by 0.03σ, linear against non-linear modelling by 0.19σ (PR3 reanalysis) |
| Quaia × ACT DR6, linear bias (arXiv:2507.08798) [src: Sect. IV.1] | 32 ≤ ℓ ≤ 316 (bin 1), 526 (bin 2) | same | first bandpower dropped for systematics and the mean field; k_max = 0.15 h/Mpc at the mean redshift of the bin |
| DESI LRG, linear theory (arXiv:2407.04607) [src: Sect. 5.1] | ℓ_max = 178, 243, 243 for bins 2–4; bin 1 dropped | same | ℓ_max ≃ χ(z_eff) × 0.1 h/Mpc, where linear and non-linear P_mm differ by ≤ 1.5% |

In the unWISE analysis the higher-order bias terms are at most 7% (Blue) and 5% (Green) of
C_ℓ^gg and at most 2% of C_ℓ^κg; dropping them all moves S_8 by ≃ 0.1σ. The in-range
signal-to-noise is 40 (Blue) and 51 (Green), against 67 and 74 for 20 ≤ ℓ ≤ 3000: the scale cut
costs about a third of the available signal (arXiv:2309.05659) [src: Sect. 4, Sect. 8.1.5].

**Related slips.**
- Inconsistent neutrino mass between the power-spectrum emulator and the rest of the likelihood:
  ΔS_8 ≃ −4 f_ν = −0.019 for Σm_ν = 0.06 eV, observed as −0.017 (arXiv:2407.04607) [src: Sect. 7.2].
- Constraints that come from the broadband shape of the auto-spectrum, not from the lensing
  amplitude: the low Ω_m = 0.245 ± 0.024 of the 2MASS/WISE analysis is "driven by the broadband
  shape of the galaxy auto-correlation, and may be affected by theoretical uncertainties in the
  HEFT power spectrum templates" (Rubiola 2025, arXiv:2510.09563) [src: abstract].
- Linear or non-linear bias changes the usable scales and the result only slightly in DES Y3:
  S_8 = 0.736 against 0.734 (arXiv:2203.12440) [src: abstract].

**Mitigation and validation.** Quote the best fit beside the mean; fit a noiseless synthetic data
vector; show a linear-theory fit on restricted scales (arXiv:2407.04607) [src]; fit N-body mocks.

## 7. Imaging systematics and large-scale power of the tracer
<!-- key: imaging-systematics-and-large-scale-power-of -->

**Mechanism.** Stellar density, depth and extinction modulate the observed galaxy density. The
auto-spectrum gains spurious large-scale power. The cross-spectrum with κ is not protected
either: weights change the effective sample, and in the unWISE case below it was C_ℓ^κg that
moved.

**Size.** Introducing systematics weights for unWISE raised S_8 by 0.4σ in the reanalysis of
unWISE × Planck (arXiv:2309.05659, App. I.1 table), mostly through a higher C_ℓ^κg for the Blue
sample at nearly unchanged C_ℓ^gg [src]; in the ACT DR6 analysis the weights changed S_8 by
ΔS_8 = 0.006 (~0.3σ) [src: arXiv:2309.05659, Sect. 3.1.3]. For f_NL the
effect is the leading one: the DESI LRG analysis uses a neural-network weight scheme and an
ℓ_min cut on the auto-spectrum, and states that the cross-spectrum is the more stable of the two
(Bermejo-Climent 2024, arXiv:2412.10279) [src]. The spectroscopic DESI quasar sample is free of
the excess large-scale power seen in photometric quasar auto-spectra (Chiarenza 2025,
arXiv:2512.17865) [src]. CatNorth needs a machine-learnt selection function to remove a
large-scale excess (Qin 2026, arXiv:2603.09457) [src].

**Validation.** Splits by imaging footprint, Galactic cap, declination, extinction and stellar
density, each of which is a subsection of arXiv:2407.04607 [src, section titles].

## 8. kSZ: the optical-depth degeneracy
<!-- key: ksz-the-optical-depth-degeneracy -->

**Mechanism.** Every kSZ statistic is a product of an electron column (τ, P_ge) and a velocity.
Cosmology from the velocity needs τ; gas physics from τ needs the velocity.

**Consequences.**
- Pairwise kSZ constrains H_0 f σ_8² only "assuming that an estimate of the optical depth and
  galaxy bias of the sample exists" (Hadzhiyska 2025, arXiv:2510.14135) [src].
- Velocity reconstruction returns b_v × v; b_v absorbs the mismatch between true and fiducial
  P_ge and is marginalised (Chaussidon 2026, arXiv:2604.04867) [src]. Measured values are well
  below one: b_v = 0.229 ± 0.022 (90 GHz) and 0.233 ± 0.020 (150 GHz) for DESI DR2 LRGs
  (arXiv:2604.04867, Sect. V.2 table), 0.33 ± 0.03 for photometric LRGs (McCarthy 2025,
  arXiv:2511.15701, abstract), A = 0.42 ± 0.042 (Lai 2025, arXiv:2506.21684, abstract) [src].
- A low b_v is evidence about gas only if the galaxy side of the fiducial P_ge is right. For DESI
  ELGs the abundance-matching HOD gives a linear bias of ~2.3 instead of ~1.3 and so biases b_v
  low (arXiv:2604.04867, section "Lower kSZ signal than expected") [src].

**Model dependence of a pairwise τ̄.** The depth is the measured momentum divided by a
linear-theory pairwise velocity at a fixed cosmology: moving the minimum separation from 20 to
30 or 40 Mpc shifts τ̄_AP by < 3%, for non-linear corrections of a few to 10% in that range. For
the L36 sample of DESI DR1 LRGs, τ̄_AP = (0.36 ± 0.05), (0.42 ± 0.06) and (0.46 ± 0.05) × 10⁻⁴ on
the total-frequency, 150 GHz and ILC maps (arXiv:2511.23417) [src: Sect. III.3, Table 2].

**Mitigation.** External τ from tSZ through a ȳ–τ̄ relation (Moore 2026, arXiv:2609.08939), from
simulations, or from machine learning trained on simulations (Gong 2025, arXiv:2511.23417);
f_NL analyses that use only the scale dependence and marginalise the amplitude [src].

## 9. kSZ: velocity reconstruction errors
<!-- key: ksz-velocity-reconstruction-errors -->

**Mechanism.** The stacking weight is a reconstructed velocity, correlated with the truth by a
coefficient r < 1; the estimator divides by r.

**Size.** r = 0.65 for a DESI-like spectroscopic sample, with an uncertainty equivalent to ~2% of
the signal that the DESI Y1 analysis neglects [sec: simulation result as quoted in Ried Guachalla
2025, arXiv:2503.19870, Sect. IV.2]. When the stacking velocity retains non-linear information or is affected
by redshift-space distortions, non-linear terms suppress the stacked signal by 10–20%, a 1–2σ
effect for current data, weakly dependent on feedback (Ondaro-Mallea 2026, arXiv:2607.23339)
[src: abstract]. Periodic boundary conditions in the reconstruction produce a skewed tail at the edges of
the redshift range: 49 and 25 galaxies beyond ±5σ_v = 1,150 km/s in DESI Y1, without effect on
the result (arXiv:2503.19870) [src: Sect. IV.1].

**r is degenerate with the gas amplitude.** The estimator scales as r n_e σ_gas σ_rec, so an
error on r is an error on the profile amplitude. r = 0.65 is a light-cone average over the DESI
LRG redshift range; it is expected to be lower at low redshift (non-linear growth), and to vary
with satellite fraction (f_sat ≈ 0.12 for LRGs at z = 0.5; fingers of God and miscentring),
fibre-assignment incompleteness and bias evolution when the sample is split
(Qu 2026, arXiv:2604.19744) [src: Sect. 3.2.1].

**Photometric redshifts.** Velocities from photometric redshifts were first used for stacking in
Hadzhiyska 2024 (arXiv:2407.07152); the photometric and spectroscopic LRG profiles are
consistent, with comparable statistical power (arXiv:2503.19870) [src]. Size of the
degradation: r = 0.3 for σ_z/(1 + z) = 2%, against 0.65 spectroscopic [sec: simulation value as
quoted in arXiv:2407.07152]. On AbacusSummit light-cone mocks with 2% redshift noise and
redshift-space distortions, the profile corrected by 1/r recovers the input optical-depth
profile, and r shows no scale dependence (0.1σ) (arXiv:2407.07152) [src: App. "Effect of
photometric noise and recovery of the true τ"]. The loss of signal-to-noise is made up by about
four times more galaxies [sec: simulation studies as quoted in arXiv:2503.19870, Sect. 5.6]: the
photometric Main LRG sample reaches S/N = 9.1 with 3,118,161 galaxies, and its profile differs
from the spectroscopic one by Δχ² = 9.8 for 9 degrees of freedom; the highest photometric S/N
needs outlier removal and a cut σ(z) < 0.05 (arXiv:2503.19870) [src: Sect. 5.6].

**Mitigation.** Calibrate r on mocks with the survey geometry; use the same velocity estimator in
the simulation prediction as in the data (arXiv:2607.23339) [src].

## 10. kSZ: foregrounds and map systematics
<!-- key: ksz-foregrounds-and-map-systematics -->

**Mechanism.** tSZ, CIB and radio emission are correlated with the galaxies but not with the sign
of their velocity, so a velocity-weighted stack cancels them on average. Quadratic velocity
reconstruction does not enjoy the same cancellation.

**Size and evidence.**
- tSZ leakage into a velocity-weighted stack: the cancellation is only approximate because the
  tSZ signal scales as M^(5/3) and a few massive clusters dominate it. For BOSS × ACT DR5 it is
  below 10% of the kSZ signal and of the noise after rejecting galaxies above
  5.5 × 10¹¹ M⊙ in stellar mass (halo mass 10¹⁴ M⊙): 1,399 of 312,708 (CMASS K), 8,617 of
  368,701 (CMASS M) and 11,013 of 145,714 (LOWZ K) galaxies. Doppler-boosted dust is
  smaller than the dust emission by v/c ~ 10⁻³ and neglected; the pipeline is tested to
  sub-percent accuracy on simulated maps (Schaan 2020, arXiv:2009.05557) [src: Sect. 4.5].
- Dust in the tSZ stack of the same galaxies: the fiducial y map deprojects a modified blackbody
  with T_dust = 24 K and β = 1.2; a second method models the 90 and 150 GHz stacks with Herschel
  H-ATLAS data over 161 deg²; the two recover the same tSZ profile; both assume one dust
  spectrum for all galaxies (arXiv:2009.05557) [src: Sect. 4.4].
- DESI Y1 × ACT DR6 stack: 1000 shuffles of the velocities give no signal, and the profile from
  the tSZ- and dust-deprojected map differs from the fiducial one by less than the statistical
  error (arXiv:2503.19870) [src: App. "Systematic checks/Null tests"]. DR2 harmonic space:
  random-velocity templates give PTE = 0.182, 0.993, 0.211 and 0.197 for three redshift slices
  and the full sample (arXiv:2604.19744) [src: Sect. 4.1].
- Velocity reconstruction: a foreground term ∝ b_fg δ_m in the reconstructed velocity gives a
  monopole in P_gv that leaks into the dipole through the window. For DESI DR2 LRGs the monopole
  is detected at SNR ≃ 45, with b_fg = 1.83 × 10⁻³ (90 GHz) and 1.11 × 10⁻³ (150 GHz); the ratio
  1.65 matches the tSZ scaling of 1.68, so tSZ dominates. For ELGs and quasars the monopole has
  SNR ≃ 1.7 and 1.8 and the leakage is negligible (arXiv:2604.04867) [src: Sect. 5.1, table].
- Direct v^kSZ × galaxy spectra show "signs of foreground contamination" confined to
  equal-redshift spectra, while v^kSZ × continuity-equation velocity shows none (arXiv:2511.15701)
  [src].
- A parity-odd combination of tomographic velocity–galaxy spectra cancels the foreground term
  under the Limber approximation without loss of signal-to-noise; applied to ACT DR6 × DESI
  Legacy data the fit improves "dramatically" (Embil Villagra 2026, arXiv:2603.28746) [src].
- With spectroscopic redshifts the foreground contribution can be modelled and has "a negligible
  impact" (arXiv:2604.04867) [src].
- The f_gas ratio analysis finds a mild North/South Galactic cap discrepancy in one LRG bin and
  applies a simulation-calibrated correction for ACT beam suppression (Liu 2026, arXiv:2609.22466)
  [src].
- In the group-stacking analysis, CIB effects are subdominant to the kSZ signal in the ACT channel
  used (Roper 2025, arXiv:2510.12553) [src].

**Validation.** The same measurement on co-added 150 GHz and 98 GHz maps and a component-separated map
(Calafut 2021, arXiv:2101.08374), or on 150 GHz, total-frequency and ILC maps (arXiv:2511.23417); frequency-difference nulls, 26 of them in Hotinli 2026
(arXiv:2609.17676); two experiments with independent optics and beams, ACT and SPT-3G, agreeing
to 0.7σ channel by channel (arXiv:2609.17676) [src: abstract].

## 11. kSZ and tSZ: host haloes, satellites and miscentring
<!-- key: ksz-and-tsz-host-haloes-satellites-and -->

**Mechanism.** A stacked profile is an average over the halo-mass distribution of the sample,
including satellites and miscentred galaxies. Comparing with a simulation requires the same
selection.

**Size.** Ignoring baryons in a galaxy–galaxy lensing fit biases the halo mass low by ~20%
(Sunseri 2025, arXiv:2505.20413) [src: abstract]. The simulation comparison of Bigwood 2025
(arXiv:2510.15822) fixes the mass selection with galaxy–galaxy lensing and includes cosmic
variance, miscentring and satellites [src: abstract]. Independent CMB-lensing masses exist for the DESI
samples (Hadzhiyska 2025, arXiv:2507.14136) [src: abstract].

A large offset of the galaxies from the centres of the gas profiles, or a significant satellite
fraction in more massive haloes, would artificially extend the observed profile; the stacks also
contain a two-halo term (arXiv:2009.05557) [src: Sect. 4.5]. In the simulation comparison of
arXiv:2510.15822, stellar-mass selections contain ~10–30% satellites depending on mass bin and
simulation; at fixed mean halo mass a centrals-only selection gives a larger kSZ amplitude in
FLAMINGO, SIMBA, BAHAMAS and FABLE; shifting the filter centre by up to the 0.5′ ACT pixel has a
negligible effect on the inner profile [src: Sect. 3.5, 3.6]. No number for the change of the
profile under miscentring was read.

**Why it matters.** The same DESI × ACT data are read as disfavouring fiducial FLAMINGO at > 8σ
(Siegel 2025, arXiv:2509.10455) and as tracked most closely by fiducial FLAMINGO (arXiv:2609.22466)
under different treatments of mass and filtering; see `open-questions.md` §2.

## 12. Patchy screening: contamination by lensing
<!-- key: patchy-screening-contamination-by-lensing -->

The stacked screening estimator returns a ~4.1σ signal that exceeds what the kSZ-measured gas
implies; N-body tests show that CMB lensing dominates it (Hadzhiyska 2025, arXiv:2506.17379)
[src]. The power-spectrum estimator on ACT DR6 shows foreground contamination at one frequency
(Kramer 2026, arXiv:2608.27458) [src]. A screening "detection" needs a lensing-hardened estimator,
an explicit subtraction, or filters shown on lensed simulations to cancel the leading lensing term:
the ACT × unWISE sign estimator removes τ modes below ℓ = 1600 and finds no lensing bias on 40
lensed simulations (Coulton 2024, arXiv:2401.13033, Sects. II.4, III.3) [src].

## 13. ISW: cosmic variance, selection of structures and mocks
<!-- key: isw-cosmic-variance-selection-of-structures-and -->

**Mechanism.** The total signal-to-noise is a few, so the result is sensitive to the selection of
structures and to choices made after looking at the data.

**Evidence.** Stacks on selected supervoids give A_ISW ≈ 4–5 (Kovács 2018, arXiv:1811.07812);
a matched filter without a posteriori choices on BOSS structures gives 1.64 ± 0.53 (Nadathur
2016, arXiv:1608.08638); stacks on DESI Legacy superstructures with matched mocks give
−0.10 ± 0.69 for voids (Hang 2021, arXiv:2105.11936) [src: abstract].

**Significance against the expected signal** (unWISE × Planck, Krolewski 2021,
arXiv:2110.13959) [src: Sect. 5.1, table of systematics tests]. Per sample A_ISW = 0.73 ± 0.34
(2.1σ, Blue), 1.00 ± 0.39 (2.6σ, Green), 1.14 ± 0.52 (2.2σ, Red); combined 3.2σ with covariances
from 300 FFP10 simulations; χ² = 10.4 for 15 degrees of freedom at A_ISW = 1. A signal of
A_ISW = 1 would be seen at 2.9σ in Blue, and at 3.7σ without the excess large-scale power of the
Blue auto-spectrum; the ℓ_min = 7 cut costs ~20% of the signal-to-noise and ℓ_max = 100 less
than 2%. Across CMB maps the Blue amplitude ranges from 0.66 (SEVEM 70 GHz) to 0.87 (SEVEM
217 GHz), with 0.83 for the SZ-free SMICA map, all within the 0.34 error. The b dN/dz
uncertainty moves A_ISW by 0.025, 0.011 and 0.018. Magnification contributes substantially to
C_ℓ^Tg for the Green and Red samples [src: Sect. 2].

**Mitigation.** Fix the catalogue and the filter before measuring; build mocks with the data's
number density, bias and photometric-redshift error; report the full cross-correlation next to
the stack. The cross-spectrum approach needs the tracer bias, redshift distribution and
magnification, with the same failure modes as §4–7.

## 14. Covariance and noise models
<!-- key: covariance-and-noise-models -->

- A cross-covariance between tomographic samples was missing in one blinded analysis until after
  unblinding (−0.3σ on S_8; arXiv:2309.05659) [src: Sect. 9.2].
- Sizes of the correlations in that analysis: C_ℓ^gg with C_ℓ^κg at the same ℓ up to 60%;
  different ℓ ≤ 10%; C_ℓ^κg of the two samples 40–60%; ACT and Planck lensing reconstructions
  ≲ 30%, but the two κg spectra up to 50% and the two gg spectra up to 60% because the galaxies
  are the same. Hartlap factors 0.96 (one sample) and 0.93 (two) for 400 simulations and 13
  bandpowers; an independent set of 400 changes the signal-to-noise by ≲ 5%
  (arXiv:2309.05659) [src: Sect. 6].
- Bootstrap over objects underestimates velocity-reconstruction noise for dense samples: the
  fitted noise rescalings for DESI LRGs are 1.13 (90 GHz), 1.09 (150 GHz) and 1.29 (90 × 150)
  (arXiv:2604.04867) [src: Sect. V.2, table of LRG fits].
- kSZ and secondary power from spectra alone depend on the assumed tSZ–CIB correlation (Chaubal
  2026, arXiv:2601.20551) [src].

## 15. Shared data
<!-- key: shared-data -->

ACT and Planck lensing maps, DESI Legacy targets and DESI spectroscopy recur across the papers of
this domain (`surveys-and-data.md` §5). Agreement between two results built on the same maps
tests the modelling, not the data.

## 16. What a referee checks in a results section
<!-- key: what-a-referee-checks-in-a-results-section -->

Lensing × galaxies:
1. Which lensing maps (Planck PR3 or PR4, ACT DR4 or DR6, SPT-SZ or SPT-3G), and whether the
   Monte Carlo normalisation was computed on the overlap.
2. Foreground mitigation of the lensing map and the simulated residual bias for this tracer.
3. Source of dN/dz, how its uncertainty is marginalised, and the shift under an alternative.
4. Magnification coefficient: measured how, with what prior.
5. Bias model, k_max or ℓ_max, validation on mocks, and best fit beside the mean.
6. Imaging-systematics weights and the splits by footprint.
7. Exponent of the quoted amplitude; the CMB reference of any quoted tension.
8. Blinding and the list of post-unblinding changes.
9. Covariance between bins and between the ACT and Planck cross-spectra.

kSZ and tSZ:
10. Estimator family, velocity source, and the value of r or its mock calibration.
11. Fiducial P_ge (electron profile and HOD) behind any b_v or amplitude.
12. Host halo mass: lensing-calibrated or assumed; satellites and miscentring in the simulation
    comparison.
13. Consistency across frequencies and across cleaned maps; treatment of CIB, dust and radio.
14. Which simulation, which variant, and whether the amplitude was left free.
15. For a matter-power suppression: the gas model that maps profiles to P(k), and the k quoted.

ISW, voids and other stacks:
16. A priori definition of the catalogue and filter; mocks matched in density and redshift error.
17. The cosmology of the template behind A_ISW or A_κ.

All:
18. Overlap of the data with earlier results quoted as independent confirmation.
