# Theory foundations — convention traps and what they cost

Snapshot: 2026-10-07

Each subsection gives the mechanism, the size where a paper quantifies it, the standard mitigation, the test that reveals it, and the paper a referee expects. The formulae are in `physics-and-methods.md`; the per-analysis choices in `surveys-and-data.md`. A size flagged [der] is derived here from numbers read at source.

## 0. Sizes at a glance
<!-- key: sizes-at-a-glance -->

| Trap | Size | Flag | Section |
|---|---|---|---|
| Eisenstein–Hu r_s used as the Boltzmann r_drag | 2.75% | [src] | 3 |
| r_* used for r_drag | 1.8% | [der] | 3 |
| D_A/r_d read as D_M/r_d | factor (1+z) | [src] | 3 |
| σ8 radius over h ∈ [0.64, 0.82] | 9.8 to 12.5 Mpc | [der] | 1 |
| Priors in Mpc/h instead of Mpc, Stage-IV synthetic data | several σ against <1σ | [src], forecast setting | 1 |
| Fiducial cosmology on α_AP, DESI DR2 | 0.18% | [src] | 2 |
| (2ℓ+1) dropped from a multipole | factor 5 (ℓ = 2), 9 (ℓ = 4) | [der] | 4 |
| Pairwise against single-galaxy dispersion | factor 2 in σ² | [src] | 4 |
| σ8 of total matter against cb, Σm_ν = 0.06 eV | about 0.45% | [der] | 5 |
| Neutrinos on the cb growth rate | 0.3–2%, scale-dependent | [src] | 5 |
| f ≈ Ω^0.6 against Ω^0.55 | 6% at Ω_m = 0.3 | [der] | 6 |
| halofit against HMcode-2020 | 5–10% against 2.5% RMS stated errors; S8 biased low with halofit | [src] | 7 |
| Limber with ℓ instead of ℓ + 1/2 | O(1/ℓ) instead of O(1/ℓ²) | [src] | 8 |
| Limber for tomographic clustering, Stage IV | 1σ to more than 2σ | [src], forecast | 8 |
| Relativistic and wide-angle terms on f_NL, SPHEREx-like | about 1σ | [src], forecast | 9 |
| Tidal bias between two codes' conventions | factor 2 | [src] | 10 |
| Prior-volume projection, DESI DR1 full shape in w0waCDM | multi-σ in H0, w0, wa | [src] | 10 |

## 1. h units and the σ8 radius
<!-- key: h-units-and-the-sigma8-radius -->

- **Mechanism.** σ8 is defined in spheres of 8 h⁻¹Mpc, so its physical radius moves with h; a posterior on σ8 averages σ(R) over the radii allowed by the posterior on h (Sánchez 2020, arXiv:2002.07829, Eq. 6). Priors, scale cuts and nuisance parameters written in h⁻¹Mpc acquire the same hidden dependence.
- **Size.** Over the KiDS-Legacy prior h ∈ [0.64, 0.82] (arXiv:2503.19441) the radius runs from 9.8 to 12.5 Mpc [der]. In Sánchez's comparison, DES and Planck are "in excellent agreement" in (ω_m, σ12) while the σ8 plane shows the familiar offset; S12 = 0.815 ± 0.013 (Planck) against 0.798 ± 0.043 (DES) [src]. For template fits, the error on fσ8 "derived under a fixed h" is "significantly underestimated" [src].
- **A second channel: priors.** Pezzotta et al. 2026 (arXiv:2610.08751) show on Stage-IV synthetic data that prior-volume shifts "are largely driven by imposing priors on the model parameters defined in Mpc/h units, thereby introducing a spurious correlation with the Hubble parameter h"; in Mpc units the shifts fall "from several standard deviations to well within 1σ", including in w0waCDM (**forecast** setting) [src, abstract].
- **Mitigation.** Sample h (then units do not matter for the constraints: "using h⁻¹Mpc units or simply Mpc would lead to identical parameter constraints"); quote σ12 or state the h posterior next to σ8; for template fits use fσ12 or a rescaled amplitude (eBOSS rescaling by α_iso, DESI σ_s8).
- **Test.** Repeat the fit with h fixed to values ±10–20% apart; a robust amplitude parameter does not move.
- **Cite.** arXiv:2002.07829; Croton 2013 (arXiv:1308.4150) for h in catalogue quantities; arXiv:2610.08751.
- **Other h-unit quantities met in the papers read:** DES Y3's clustering cut R_min = 8 Mpc/h and point-mass prior 10^17 M_⊙/h (arXiv:2105.13548); DESI's counterterm prior of 12.5 h⁻²Mpc² and k range 0.02–0.20 h/Mpc (arXiv:2411.12021); Tinker masses in M_⊙/h.

## 2. Fiducial cosmology and the Alcock–Paczynski rescaling
<!-- key: fiducial-cosmology-and-the-alcock-paczynski -->

- **Mechanism.** Redshifts are turned into distances with a fixed catalogue cosmology; the model is distorted by q_∥ = D_H/D_H^fid, q_⊥ = D_M/D_M^fid, with a volume prefactor D²_A,fid H_true/(D²_A,true H_fid) (arXiv:1909.05277, appendix). A template fit adds a second fiducial dependence: the template shape, its one-loop terms and its amplitude.
- **Size.** DESI assigns the fiducial cosmology a systematic on α_AP of 0.1% in DR1 and 0.18% in DR2, the increase coming from adding an evolving-dark-energy case to the test (arXiv:2503.14738; method in Pérez-Fernández et al. 2024, arXiv:2406.06085) [src]. In eBOSS, fσ8 built from the rescaled σ8 depends on the template at a level "significantly smaller than the statistical errors", with 2% marked as the reference deviation in its mock test (arXiv:2007.08991, Appendix A) [src].
- **Where it bites.** Compressed parameters: in ShapeFit and standard compression the one-loop terms are computed in the fiducial cosmology (arXiv:2411.12021); fσ_s8 is exact "at first-order of perturbation theory" only. Euclid preparation finds that "using a 'wrong' template can also introduce an additional scatter, although with smaller amplitude" than the scatter already present with the right one (arXiv:2603.13148) [src, abstract].
- **Mitigation.** Full modelling with the AP mapping; for BAO, ratios to r_d^fid and a quoted systematic; for compressed growth, the rescaled amplitude.
- **Test.** Refit with two or more catalogue cosmologies (DESI does, arXiv:2406.06085); check that the forgotten-prefactor error is absent by recovering the input on a mock with a deliberately wrong grid cosmology.
- **Cite.** arXiv:2406.06085; arXiv:2106.07641 (ShapeFit); arXiv:2007.08991.

## 3. r_d definition and code dependence
<!-- key: rd-definition-and-code-dependence -->

- **Mechanism.** Three different numbers are called "the sound horizon": r_* at last scattering, r_drag from a Boltzmann code, and the Eisenstein–Hu fitting-formula value.
- **Size.** Fitting formula against CAMB: 2.75% (arXiv:1303.5076) [src]; conventions "differ at the 1-2% level" (arXiv:1411.1074) [src]; r_drag against r_*: 147.09 against 144.43 Mpc, 1.8% (arXiv:1807.06209) [src, ratio der]. Against these, DESI DR2 measures h r_d to 0.7% [der: 0.73/101.54].
- **Related traps.** D_A/r_d against D_M/r_d, "differing by a factor (1+z)", and the inverse ratio r_s/D_V of older papers (arXiv:1411.1074; arXiv:1303.5076). N_eff = 3.046 or 3.044 and the pivot 3.04 of DESI's formula: 0.013% on r_d [der]. The drag redshift quoted as 1020 (eBOSS) or 1060 (DESI).
- **Model dependence.** Every r_d formula assumes "standard pre-recombination physics" (arXiv:2503.14738); one extra relativistic species lowers r_d by about 3.2%, Σm_ν = 0.5 eV by 0.26% (arXiv:1411.1074) [src]. An H0 from BAO + BBN inherits the assumption; BAO alone give h r_d.
- **Mitigation.** Quote D/r_d; state the code or formula that gives r_d; never convert an old r_s/D_V without the 1.0275 factor.
- **Test.** Recompute r_d for the paper's own best fit with a Boltzmann code and compare.
- **Cite.** arXiv:1411.1074; arXiv:astro-ph/9709112; arXiv:1303.5076, Sect. 5.2; Brieden, Gil-Marín & Verde 2023 (arXiv:2212.04522) for the power-law form.

## 4. Fourier and multipole normalisation
<!-- key: fourier-and-multipole-normalisation -->

- **Mechanism.** Factors that differ silently between codes: (2π)³ in P(k); the (2ℓ+1) of the multipoles; the i^ℓ of the Hankel pair; the sign of the Fourier exponent; P(k) against Δ²(k) = k³P/(2π²).
- **Size.** Each is a factor, not a per cent: 5 on the quadrupole, 9 on the hexadecapole if (2ℓ+1) is dropped [der]; a sign on ξ_2 if i^ℓ is ignored ("a negative quadrupole" of ξ "corresponds to … a positive quadrupole" of P, arXiv:astro-ph/9708102) [src].
- **Velocity dispersion.** The σ of the damping models is a pairwise 1D dispersion, "2^(1/2) larger than a random 1-dimensional single-point (galaxy) dispersion" (arXiv:astro-ph/9708102, Sect. 7.2): a factor 2 in σ² between conventions. It is expressed as a length (velocity over Hubble rate) in most clustering papers and in km/s in velocity papers (`cosmo-peculiar-velocities` lists the mix of σ_u in h⁻¹Mpc with σ_v in km/s among recurring errors).
- **Printed slips exist.** arXiv:1909.05277 prints the BAO scale k_osc as "~110 h/Mpc" and writes the next-to-leading counterterm with opposite signs in main text and appendix; arXiv:astro-ph/0603494 prints the −8 f_ν relation for the ratio of spectra rather than its fractional change. Re-deriving from a paper requires checking dimensions.
- **Mitigation and test.** State the convention once (hub conventions file); validate a new code by reproducing the Kaiser multipoles (1 + 2β/3 + β²/5, 4β/3 + 4β²/7, 8β²/35) from a linear input.
- **Cite.** arXiv:astro-ph/9708102; arXiv:1909.05277 for the modern statement of both conventions.

## 5. Which matter field: cb versus total matter
<!-- key: which-matter-field-cb-versus-total-matter -->

- **Mechanism.** With massive neutrinos there are two matter fields. Haloes, bias and the redshift-space growth rate follow CDM+baryons; lensing and the Planck σ8 follow total matter.
- **Size.** If neutrinos are unclustered at 8 h⁻¹Mpc, σ8 of total matter is below the cb value by about f_ν: 0.45% for Σm_ν = 0.06 eV [der, `results.md` section 8]. Planck defines σ8 on "total matter (baryons + CDM + massive neutrinos)" (arXiv:1303.5076); DESI DR1 full shape "excluding neutrinos" (arXiv:2411.12021) [src]. The neutrino effect on the cb growth rate is 0.3–2% over k = 0.01–0.5 h/Mpc for M_ν ≤ 0.15 eV (arXiv:1708.01154) [src].
- **Consequences if the wrong field is used.** Bias becomes scale-dependent and the mass function loses universality (arXiv:1311.1212; arXiv:1311.0866); a velocity bias appears between haloes and total matter (arXiv:1708.01154); original halofit over-predicts the neutrino suppression by 10% of its size at k ~ 1 h/Mpc (arXiv:1109.4416) [src].
- **Related convention.** Ω_m includes massive neutrinos in Planck and DESI ("when they are non-relativistic"); ω_bc or ω_cb does not, and it is the latter that enters r_d. The neutrino sector itself differs: one state of 0.06 eV, three degenerate states, or Σm_ν fixed; and the eV-to-ω_ν constant is 93.04, 93.14 or 93.2 depending on the paper.
- **Mitigation and test.** State the field for σ8, f and the template; with Σm_ν varied, check that the growth rate fed to the RSD model is the cb one; compare a chain with one massive state against three degenerate.
- **Cite.** arXiv:1311.1212; arXiv:1708.01154; arXiv:astro-ph/0603494.

## 6. Growth-rate approximations used outside their range
<!-- key: growth-rate-approximations-used-outside-their -->

- **Mechanism.** f = Ω_m(z)^γ with γ = 0.55 is a ΛCDM fit, used as if it were general relativity. Linder's own formula has γ = 0.55 + 0.05[1 + w(z=1)] (arXiv:astro-ph/0507263).
- **Size.** Within its range the formula is good to 0.05–0.2% on the growth factor [src: abstract of arXiv:astro-ph/0507263; an earlier draft of this file read 0.05–0.5%, which the abstract does not support]; the exponent 0.6 of older work differs by 6% in f at Ω_m = 0.3 [der]; a DGP model and a quintessence model with the same expansion differ by 7% in growth today [src]. With neutrinos, growth is scale-dependent at the 0.3–2% level (arXiv:1708.01154), larger than the fit error.
- **Definitions that coincide only for scale-independent growth.** f × σ8; Planck's [σ8^(vd)]²/σ8^(dd) (arXiv:1807.06209, Eq. 27); eBOSS's f = ∂ln σ8/∂ln a (arXiv:2007.08991, Eq. 19).
- **Where it bites.** A γ constraint that mixes fσ8 points defined differently, or that uses a ΛCDM-fixed Ω_m(z) while fitting γ; a "growth suppression" inferred against a 0.55 baseline in a model with w ≠ −1.
- **Mitigation and test.** Solve the growth equation; keep the index as a parametrisation of deviations, not as the baseline calculation; show the result with the exact ΛCDM growth as a null test.
- **Cite.** arXiv:astro-ph/0507263; arXiv:astro-ph/0701317; values in `cosmo-dark-energy-modified-gravity`.

## 7. Non-linear prescription outside its calibration
<!-- key: non-linear-prescription-outside-its-calibration -->

- **Mechanism.** halofit and HMcode are fits to finite simulation sets; their quoted accuracies hold only within those sets.
- **Size.** 5–10% (revised halofit), ≃5% (HMcode 2015), RMS 2.5% with a 16% worst case (HMcode-2020), each to k ~ 10 h/Mpc and z ≤ 2–3 [src, `results.md` section 4]. KiDS-Legacy reports that halofit "tends to overestimate power for lower values of S8, resulting in an underestimated S8 value", and that HMCode2020 gives "a slightly higher S8" than HMCode2015 (arXiv:2503.19441) [src]; Planck 2018 itself moved from Takahashi halofit to HMcode for CMB lensing (arXiv:1807.06209).
- **Range violations in practice.** KiDS-Legacy notes that its priors on h²Ω_m extend beyond the range over which HMcode was fitted (arXiv:2503.19441); dynamical dark energy lies outside the training range of most emulators (arXiv:2511.13826).
- **Baryons.** DES Y3 removes them by scale cuts with a gravity-only model (arXiv:2105.13548); KiDS-Legacy marginalises a feedback parameter. The two S8 values are conditional on different treatments (`cosmo-weak-lensing`).
- **Mitigation and test.** Compare against an emulator on the scales used (DES does); rerun with the alternative prescription and report the shift; state k and z ranges of the calibration.
- **Cite.** arXiv:1208.2701; arXiv:2009.01858; arXiv:1109.4416.

## 8. Limber and flat-sky approximations
<!-- key: limber-and-flat-sky-approximations -->

- **Mechanism.** Limber replaces two Bessel functions by a delta function; it fails when the radial kernels are narrow or barely overlap (arXiv:0809.5112). Writing k = ℓ/χ instead of (ℓ + 1/2)/χ degrades the error from O(1/ℓ²) to O(1/ℓ).
- **Size.** Cosmic shear: >1% at ℓ < 40 with flat sky and Hankel approximations combined (arXiv:1611.04954); negligible for CFHTLenS-class parameters (arXiv:1702.05301; arXiv:1704.01054). Clustering: "significant biases" at LSST Y1 or DES Y6 precision (arXiv:1911.11947); 1σ to more than 2σ for Roman and Rubin (arXiv:2606.23781, **forecast**).
- **Mitigation.** Non-Limber integration with RSD and magnification for clustering (arXiv:2105.13548); second-order Limber for shear.
- **Test.** Compare the C_ℓ with a non-Limber code (the N5K comparison, arXiv:2212.04291) for the narrowest bin.
- **Cite.** arXiv:0809.5112; arXiv:1911.11947.

## 9. Wide-angle, relativistic and line-of-sight definition
<!-- key: wide-angle-relativistic-and-line-of-sight -->

- **Mechanism.** The plane-parallel Kaiser formula assumes one line of sight per pair. FFT estimators take the direction to one galaxy; this generates odd multipoles that couple to the window (arXiv:1810.05051). On horizon scales the observed counts contain Doppler, potential and lensing terms (arXiv:1105.5280).
- **Size.** Geometry, non-linearity and radial selection together change large-scale RSD "at the level of 20 per cent" in SDSS-II LRG mocks (arXiv:1102.1014) [src]; wide-angle corrections are "non-negligible for opening angles Θ ≳ 30°" (arXiv:2608.19039) [src]; neglecting relativistic and wide-angle terms shifts f_NL by about 1σ in a SPHEREx-like **forecast** (arXiv:2608.18334).
- **Selection function.** The radial operator carries a term in α(r) = ∂ln[r² n̄(r)]/∂ln r (arXiv:astro-ph/9708102), so wide-angle corrections depend on the radial selection, not on geometry alone (arXiv:1709.09730).
- **Mitigation.** Model the odd multipoles or include the wide-angle terms in the window (arXiv:1810.05051); for f_NL use a full-sky or two-ℓ estimator (arXiv:2607.05513); state the magnification coefficient of each sample (arXiv:2105.13548).
- **Test.** Measure the dipole; compare the low-k quadrupole with a wide-angle-aware model.
- **Cite.** arXiv:astro-ph/9712007; arXiv:1709.09730; arXiv:1810.05051.

## 10. Bias-basis, counterterm and prior conventions
<!-- key: bias-basis-counterterm-and-prior-conventions -->

- **Mechanism.** The same physics is parametrised differently in each one-loop code; priors that are "wide" in one basis are informative in another; weakly constrained nuisance parameters shift marginal posteriors.
- **Size of the convention differences.** Co-evolution tidal bias: −(2/7)(b1^E − 1) in velocileptors EPT, −(4/7)(b1^E − 1) in FOLPSν (arXiv:2404.07272, Eqs. 3.15–3.16) [src], a factor 2 in the number called tidal bias. Linear bias: Lagrangian b1 against Eulerian 1 + b1. Counterterms: k²P_Zel against k²P_lin; two multipole coefficients against three μ-dependent ones (arXiv:1909.05277).
- **Size of the prior effect.** In DESI DR1 full shape with BBN and an n_s constraint, baseline priors give "multi-σ projection" in H0, w0 and wa, removed by a Jeffreys prior (Bonici et al. 2026, arXiv:2607.02498) [src]. DES Y3 states that on noiseless synthetic data "the marginalized parameter posteriors may appear biased from the input parameter values due to parameter volume effects … while the maximum a posteriori point … recovers the input parameter values", and that these effects "decrease as the data's constraining power increases and are thus not a systematic bias"; DES therefore reports the MAP in parentheses next to the mean (arXiv:2105.13548, Eq. 36) [src]. KiDS-Legacy reports three point estimates of S8 for the same chain, 0.813, 0.815 and 0.811 (arXiv:2503.19441) [src]: a spread of 0.2σ there, larger in extended models (`cosmo-galaxy-clustering`).
- **Mitigation.** Sample bias with σ8 attached (DESI: (1 + b1)σ8, b2σ8², b_sσ8²); drop the hexadecapole; priors in Mpc (arXiv:2610.08751); report MAP or profile likelihood next to the marginal mean.
- **Test.** Fit noiseless synthetic data generated at the best fit (DESI's choice of pipeline was made on such data); fit one code's synthetic data with another (arXiv:2404.07272).
- **Cite.** arXiv:2404.07272; arXiv:2607.02498; arXiv:0902.0991; arXiv:1402.5916; statistical treatment in `cosmo-statistics-inference`.

## 11. Three worked cases
<!-- key: three-worked-cases -->

**Reading an old BAO number.** A 2010–2012 paper quotes r_s/D_V. Its r_s is the Eisenstein–Hu value. To compare with a Boltzmann-based model, either multiply the model r_drag by 1.0275 as Planck 2013 did, or divide the datum's r_s by it; then invert to D_V/r_d. If the paper quotes D_A/r_s, multiply by (1+z) for D_M. Skipping the first step is a 2.75% error, four times the 0.7% precision of DESI DR2 on h r_d [der].

**Comparing two σ8 values.** Planck 2018: σ8 = 0.8111 ± 0.0060, total matter, one 0.06 eV state. DESI DR1 full shape: σ8 "excluding neutrinos", fiducial value 0.811355. The definitions differ by about 0.45% in amplitude for that neutrino mass [der], against a Planck error of 0.7% and DESI full-shape errors several times larger (`cosmo-galaxy-clustering`). Harmless today; not harmless when a Stage-IV σ8 reaches the Planck precision. The DESI text gives its fiducial 0.811355 as the Planck chain mean, which is Planck's total-matter number to four digits; which field that particular value refers to was not resolved here.

**Putting fσ8 points on one plot.** BOSS and eBOSS points are template-fit fσ8 with σ8 rescaled by α_iso (galaxies); DESI DR1 points are fσ_s8 under r_d = r_d^fid; Planck's prediction curve is [σ8^(vd)]²/σ8^(dd) for total matter; peculiar-velocity points come from a different estimator at z < 0.1. The plot is legitimate as a display with these caveats stated; a γ fit to it needs each point's definition, covariance and fiducial cosmology (`cosmo-peculiar-velocities`, `cosmo-dark-energy-modified-gravity`).

## 12. What a referee checks
<!-- key: what-a-referee-checks -->

1. Units: is every length, wavenumber, mass, prior width and scale cut in Mpc or in h⁻¹Mpc, and which h?
2. σ8: field (total or cb), redshift, linear, and the h posterior or a σ12 next to it; for S8, the exponent (0.5, 0.58, 0.4 for S12).
3. fσ8: full modelling or template fit; if template, fixed h and template cosmology, rescaling applied (α_iso, σ_s8), and the definition of f.
4. Distances: D_M or D_A; D_H(z) or c/H0; ratio to r_d or absolute; sign convention of Ω_K.
5. r_d: Boltzmann value or which formula; N_eff; the pre-recombination assumption stated wherever H0 is quoted.
6. CMB priors: θ_MC or θ_*; r_* or r_drag.
7. Neutrinos: Σm_ν fixed or varied, splitting, N_eff, the eV conversion; which field in bias and growth.
8. Growth model: exact solution or Ω_m^γ; the γ baseline for the assumed w; scale dependence.
9. Fourier and multipole conventions; pairwise or single-galaxy dispersion; units of σ.
10. Non-linear prescription and its calibrated range; treatment of baryons.
11. Limber or not, per probe and per bin; ℓ + 1/2; flat sky.
12. Line-of-sight definition, odd multipoles, magnification coefficients, on large scales.
13. Bias basis, counterterm form, priors and their units; MAP against marginal mean.
14. Fiducial cosmology of the catalogue and of the template; the systematic assigned to it.
15. Code and version for the linear spectrum; whether a formula from a paper was re-derived or copied.

## Not verified
<!-- key: not-verified -->

- No paper read this session quantifies the bias from a dropped AP volume prefactor or from a wrong multipole normalisation: these are stated as factors, not measured.
- The size of the cb-versus-total σ8 difference is a derivation; a Boltzmann-code value was not read. Whether DESI's fiducial σ8 = 0.811355 is a cb or a total-matter number was not resolved.
- The quantitative effect of the θ_MC-versus-θ_* confusion on a BAO + CMB-prior fit was not found.
- Systematics from the choice of pair line of sight in DESI's own power-spectrum estimator were not read.
