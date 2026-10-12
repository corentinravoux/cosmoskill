# Systematics — CMB × LSS cross-correlations

Scope: the systematic effects that have moved published results in this domain, one subsection each (mechanism, size, mitigation, validation, reference), then the referee checklist.
Snapshot: 2026-10-07

Flags: `[src]` read this session in the cited paper; `[sec]` from a named secondary source;
`[der]` derived here. "σ" shifts are in units of the statistical error of the analysis that
reports them.

Cross-correlations are often introduced as immune to systematics. They are immune to additive
contamination that the two maps do not share. They are fully exposed to anything multiplicative
(normalisation, redshift distribution, bias model) and to contamination that both maps trace,
which is the case for every extragalactic foreground.

## 1. Normalisation of the lensing map on the overlap region

**Mechanism.** A quadratic lensing estimator applied to a masked sky returns a misnormalised
convergence. The correction is a ratio of simulated spectra evaluated with the galaxy mask and
depends on the overlap region (`physics-and-methods.md` §2.4).

**Size.** Omitting it lowered S_8 by 0.6σ in unWISE × Planck (Farren 2023, arXiv:2309.05659,
appendix table) and by ΔS_8 = 0.015 (about 0.5σ) in DESI LRG × Planck PR3 (Sailer 2024,
arXiv:2407.04607, section "Planck PR3 reanalysis") [src].

**Mitigation and validation.** Monte Carlo correction per mask combination; marginalisation of
the residual normalisation uncertainty in the covariance (arXiv:2309.05659) [src].

**Referee expects.** A statement that the correction was computed for the actual overlap, and
arXiv:2309.05659 cited for the effect in cross-correlation.

## 2. Extragalactic foregrounds in the lensing reconstruction

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
below 0.2σ on A_lens (MacCrann 2023, arXiv:2304.05196) [src].

**Mitigation.** Source and cluster subtraction, profile bias-hardened estimators, CIB
deprojection with Planck high frequencies (arXiv:2304.05196); tSZ-cleaned lensing maps
(Chang 2022, arXiv:2203.12440; Shaikh 2023, arXiv:2309.04412); polarisation-only reconstruction,
now measurable at ~14σ with SPT-3G D1 × DES Y3 shear (Ouellette 2026, arXiv:2606.26223) [src].

**Validation.** Null tests between frequencies and between temperature and polarisation; two
independent sky simulations (arXiv:2304.05196); an analytic halo model of the bi- and trispectra
(CosmoBLENDER), which finds the shape of the bias for cross-correlations with low-redshift
galaxies to depend on Ω_m (Baleato Lizancos 2025, arXiv:2507.03859) [src].

**Case history.** Two Quaia analyses on Planck lensing suggested contamination of the lensing map
at z ≳ 1.5 (Alonso 2023, arXiv:2306.17748; Piccirilli 2024, arXiv:2402.05761). The ACT DR6 +
Planck PR4 analysis ran contamination and systematic null tests and finds "no evidence for
contamination in the lensing maps" (Embil Villagra 2025, arXiv:2507.08798) [src].

## 3. CIB, dust and radio leakage in tSZ cross-correlations

**Mechanism.** A Compton-y map retains CIB and radio emission, and both correlate with any
low-redshift tracer and with lensing. The sign differs: dusty and radio emission add positive
flux where the tSZ is a decrement below 217 GHz.

**Size.**
- CIB "has a substantial impact" on DES Y3 shear × y and "must be taken into account" (Gatti
  2021, arXiv:2108.01600) [src].
- For CMB lensing × y the residual CIB is "a serious systematic" because of the high CIB–κ
  correlation; the measured amplitude moves between 0.82 ± 0.21 and 0.56 ± 0.24 with the choice
  of lensing map (McCarthy 2023, arXiv:2308.16260) [src].
- For unWISE × multi-frequency maps, a model with a radio component is preferred at 9.5σ and
  11σ; without it the ACT DR6 NILC y map gives an apparent negative galaxy–tSZ correlation on
  small scales (Zhao 2026, arXiv:2606.28099) [src].
- For stacked tSZ on DESI LRG and BGS, dust and radio emission dominate the tSZ signal at and
  below the ~2′ aperture, while large-scale (R > 4′) CIB contamination is less significant (Moore
  2026, arXiv:2609.08939) [src].
- KiDS-1000 × y was found "insensitive to the CIB", with intrinsic alignments a small but
  significant contribution (Tröster 2021, arXiv:2109.04458) [src]. The statements differ because
  the y maps, scales and source redshifts differ; none transfers to another analysis.

**Mitigation.** CIB deprojection in the ILC; moment deprojection against a wrong CIB spectrum
(arXiv:2308.16260); fitting tSZ, CIB and radio jointly at the level of the multi-frequency
cross-spectra, with the CIB spectral parameters calibrated externally and marginalised (Wayland
2026, arXiv:2609.31774; arXiv:2606.28099; La Posta 2026, arXiv:2603.04269) [src].

**Validation.** Repeat the measurement with at least two differently cleaned y maps; show the
result against the CIB spectral index and with radio sources masked.

## 4. Redshift distribution of photometric tracers

**Mechanism.** At fixed data, a tracer placed at lower redshift has a larger C_ℓ^gg and a smaller
overlap with the lensing kernel, so the fit compensates by raising S_8 (arXiv:2309.05659) [src].

**Size.** Adding spectroscopic data to the unWISE cross-correlation redshifts raised S_8 by
0.8σ, the largest single term of the reanalysis; the Blue-sample dN/dz changed by 0.74σ and
Green by 0.14σ. Switching to a principal-component marginalisation of dN/dz moved S_8 by −0.2σ
and widened the posterior by ~15% (arXiv:2309.05659, appendix table) [src]. In galaxy lensing the
same class of error drove the old low S_8 values [sec: `cosmo-weak-lensing` SKILL.md].

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

**Mechanism.** Lensing by foreground matter changes the observed number counts with a
coefficient (5 s_μ − 2) and correlates directly with κ.

**Size.** Below 1% of C_ℓ^gg and up to ≃ 10% of C_ℓ^κg in the highest DESI LRG bin
(arXiv:2407.04607, section "From 3D to 2D") [src]. Those bins are narrow; the size for broad or
quasar samples was not read this session.

**Mitigation.** Measure s_μ on the actual selection; arXiv:2309.06443 publishes the coefficients
for the LRG samples [src]. Sailer 2025 (arXiv:2503.24385) turns the
effect into a signal, with a finite-difference calibration of the slope, and assigns a systematic
error of ±0.050 on σ_8, larger than its statistical error of ±0.047 [src].

## 6. Bias model, scale cuts and projection effects

**Mechanism.** A flexible bias model has many weakly constrained parameters. Marginal means of
cosmological parameters then shift away from the best fit ("volume effect"), in a direction that
depends on priors.

**Size.** In the first DESI LRG × Planck analysis the mean S_8 (0.725) sat about 1σ below its own
best fit (0.751); a prior tying the two counterterms moved the mean by +0.014 while the best fit
moved by 0.005. With the new priors and ℓ_max = 600, tests on a noiseless model prediction give
shifts below σ/3 in every configuration and at most σ/10 for the baseline (arXiv:2407.04607,
sections "Volume effect estimation" and "Planck PR3 reanalysis") [src].

**Related slips.**
- Inconsistent neutrino mass between the power-spectrum emulator and the rest of the likelihood:
  ΔS_8 ≃ −4 f_ν = −0.019 for Σm_ν = 0.06 eV, observed as −0.017 (arXiv:2407.04607) [src].
- Constraints that come from the broadband shape of the auto-spectrum, not from the lensing
  amplitude: the low Ω_m = 0.245 ± 0.024 of the 2MASS/WISE analysis is "driven by the broadband
  shape of the galaxy auto-correlation, and may be affected by theoretical uncertainties in the
  HEFT power spectrum templates" (Rubiola 2025, arXiv:2510.09563) [src].
- Linear or non-linear bias changes the usable scales and the result only slightly in DES Y3:
  S_8 = 0.736 against 0.734 (arXiv:2203.12440) [src].

**Mitigation and validation.** Quote the best fit beside the mean; fit a noiseless synthetic data
vector; show a linear-theory fit on restricted scales (arXiv:2407.04607) [src]; fit N-body mocks.

## 7. Imaging systematics and large-scale power of the tracer

**Mechanism.** Stellar density, depth and extinction modulate the observed galaxy density. The
auto-spectrum gains spurious large-scale power. The cross-spectrum with κ is not protected
either: weights change the effective sample, and in the unWISE case below it was C_ℓ^κg that
moved.

**Size.** Introducing systematics weights for unWISE raised S_8 by 0.4σ, mostly through a higher
C_ℓ^κg for the Blue sample at nearly unchanged C_ℓ^gg (arXiv:2309.05659) [src]. For f_NL the
effect is the leading one: the DESI LRG analysis uses a neural-network weight scheme and an
ℓ_min cut on the auto-spectrum, and states that the cross-spectrum is the more stable of the two
(Bermejo-Climent 2024, arXiv:2412.10279) [src]. The spectroscopic DESI quasar sample is free of
the excess large-scale power seen in photometric quasar auto-spectra (Chiarenza 2025,
arXiv:2512.17865) [src]. CatNorth needs a machine-learnt selection function to remove a
large-scale excess (Qin 2026, arXiv:2603.09457) [src].

**Validation.** Splits by imaging footprint, Galactic cap, declination, extinction and stellar
density, each of which is a subsection of arXiv:2407.04607 [src, section titles].

## 8. kSZ: the optical-depth degeneracy

**Mechanism.** Every kSZ statistic is a product of an electron column (τ, P_ge) and a velocity.
Cosmology from the velocity needs τ; gas physics from τ needs the velocity.

**Consequences.**
- Pairwise kSZ constrains H_0 f σ_8² only "assuming that an estimate of the optical depth and
  galaxy bias of the sample exists" (Hadzhiyska 2025, arXiv:2510.14135) [src].
- Velocity reconstruction returns b_v × v; b_v absorbs the mismatch between true and fiducial
  P_ge and is marginalised (Chaussidon 2026, arXiv:2604.04867) [src]. Measured values are well
  below one: b_v = 0.229 ± 0.022 (90 GHz) and 0.233 ± 0.020 (150 GHz) for DESI DR2 LRGs
  (arXiv:2604.04867, table of LRG fits), 0.33 ± 0.03 for photometric LRGs (McCarthy 2025,
  arXiv:2511.15701), A = 0.39 ± 0.04 (Lai 2025, arXiv:2506.21684) [src].
- A low b_v is evidence about gas only if the galaxy side of the fiducial P_ge is right. For DESI
  ELGs the abundance-matching HOD gives a linear bias of ~2.3 instead of ~1.3 and so biases b_v
  low (arXiv:2604.04867, section "Lower kSZ signal than expected") [src].

**Mitigation.** External τ from tSZ through a ȳ–τ̄ relation (Moore 2026, arXiv:2609.08939), from
simulations, or from machine learning trained on simulations (Gong 2025, arXiv:2511.23417);
f_NL analyses that use only the scale dependence and marginalise the amplitude [src].

## 9. kSZ: velocity reconstruction errors

**Mechanism.** The stacking weight is a reconstructed velocity, correlated with the truth by a
coefficient r < 1; the estimator divides by r.

**Size.** r = 0.65 for a DESI-like spectroscopic sample, with an uncertainty equivalent to ~2% of
the signal that the DESI Y1 analysis neglects [sec: simulation result as quoted in Ried Guachalla
2025, arXiv:2503.19870]. When the stacking velocity retains non-linear information or is affected
by redshift-space distortions, non-linear terms suppress the stacked signal by 10–20%, a 1–2σ
effect for current data, weakly dependent on feedback (Ondaro-Mallea 2026, arXiv:2607.23339)
[src]. Periodic boundary conditions in the reconstruction produce a skewed tail at the edges of
the redshift range: 49 and 25 galaxies beyond ±5σ_v = 1,150 km/s in DESI Y1, without effect on
the result (arXiv:2503.19870) [src].

**Photometric redshifts.** Velocities from photometric redshifts were first used for stacking in
Hadzhiyska 2024 (arXiv:2407.07152); the photometric and spectroscopic LRG profiles are
consistent, with comparable statistical power (arXiv:2503.19870) [src].

**Mitigation.** Calibrate r on mocks with the survey geometry; use the same velocity estimator in
the simulation prediction as in the data (arXiv:2607.23339) [src].

## 10. kSZ: foregrounds and map systematics

**Mechanism.** tSZ, CIB and radio emission are correlated with the galaxies but not with the sign
of their velocity, so a velocity-weighted stack cancels them on average. Quadratic velocity
reconstruction does not enjoy the same cancellation.

**Size and evidence.**
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

**Validation.** The same measurement on 150 GHz, 90/98 GHz and ILC maps (Calafut 2021,
arXiv:2101.08374; arXiv:2511.23417); frequency-difference nulls, 26 of them in Hotinli 2026
(arXiv:2609.17676); two experiments with independent optics and beams, ACT and SPT-3G, agreeing
to 0.7σ channel by channel (arXiv:2609.17676) [src].

## 11. kSZ and tSZ: host haloes, satellites and miscentring

**Mechanism.** A stacked profile is an average over the halo-mass distribution of the sample,
including satellites and miscentred galaxies. Comparing with a simulation requires the same
selection.

**Size.** Ignoring baryons in a galaxy–galaxy lensing fit biases the halo mass low by ~20%
(Sunseri 2025, arXiv:2505.20413) [src]. The simulation comparison of Bigwood 2025
(arXiv:2510.15822) fixes the mass selection with galaxy–galaxy lensing and includes cosmic
variance, miscentring and satellites [src]. Independent CMB-lensing masses exist for the DESI
samples (Hadzhiyska 2025, arXiv:2507.14136) [src].

**Why it matters.** The same DESI × ACT data are read as disfavouring fiducial FLAMINGO at > 8σ
(Siegel 2025, arXiv:2509.10455) and as tracked most closely by fiducial FLAMINGO (arXiv:2609.22466)
under different treatments of mass and filtering; see `open-questions.md` §2.

## 12. Patchy screening: contamination by lensing

The stacked screening estimator returns a ~4.1σ signal that exceeds what the kSZ-measured gas
implies; N-body tests show that CMB lensing dominates it (Hadzhiyska 2025, arXiv:2506.17379)
[src]. The power-spectrum estimator on ACT DR6 shows foreground contamination at one frequency
(Kramer 2026, arXiv:2608.27458) [src]. A screening "detection" needs a lensing-hardened estimator
or an explicit subtraction.

## 13. ISW: cosmic variance, selection of structures and mocks

**Mechanism.** The total signal-to-noise is a few, so the result is sensitive to the selection of
structures and to choices made after looking at the data.

**Evidence.** Stacks on selected supervoids give A_ISW ≈ 4–5 (Kovács 2018, arXiv:1811.07812);
a matched filter without a posteriori choices on BOSS structures gives 1.64 ± 0.53 (Nadathur
2016, arXiv:1608.08638); stacks on DESI Legacy superstructures with matched mocks give
−0.10 ± 0.69 for voids (Hang 2021, arXiv:2105.11936) [src].

**Mitigation.** Fix the catalogue and the filter before measuring; build mocks with the data's
number density, bias and photometric-redshift error; report the full cross-correlation next to
the stack. The cross-spectrum approach needs the tracer bias, redshift distribution and
magnification, with the same failure modes as §4–7.

## 14. Covariance and noise models

- A cross-covariance between tomographic samples was missing in one blinded analysis until after
  unblinding (−0.3σ on S_8; arXiv:2309.05659) [src].
- Bootstrap over objects underestimates velocity-reconstruction noise for dense samples: the
  fitted noise rescalings for DESI LRGs are 1.13 (90 GHz), 1.09 (150 GHz) and 1.29 (90 × 150)
  (arXiv:2604.04867, table of LRG fits) [src].
- kSZ and secondary power from spectra alone depend on the assumed tSZ–CIB correlation (Chaubal
  2026, arXiv:2601.20551) [src].

## 15. Shared data

ACT and Planck lensing maps, DESI Legacy targets and DESI spectroscopy recur across the papers of
this domain (`surveys-and-data.md` §5). Agreement between two results built on the same maps
tests the modelling, not the data.

## 16. What a referee checks in a results section

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
