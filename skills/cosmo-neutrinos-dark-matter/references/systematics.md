# Systematics — neutrino mass, light relics and dark-matter properties from structure

Scope: what can move or fake each bound in `results.md`: the mechanism, its measured size, the standard mitigation, the validation test, and the paper a referee expects cited. Ends with the referee checklist.
Snapshot: 2026-10-16

Flags: `[src]` read in the cited paper this session; `[sec]` taken from a named secondary source; `[der]` derived here, derivation stated.

## 0. How to read this file
<!-- key: how-to-read-this-file -->

Almost every number in this domain is an upper or lower limit, and a limit moves for two different reasons: the width of the posterior changes, or its peak shifts. Most of the entries below are shifts. A limit that tightened because the preferred value moved towards the excluded side is not a gain in sensitivity, and it is the first thing to check.

The instrumental systematics of the input data are not repeated here: beams, calibration, foregrounds and low-ℓ polarisation in `cosmo-cmb`; BAO and full-shape systematics in `cosmo-galaxy-clustering`; continuum, resolution, noise and metals in `cosmo-lyman-alpha`. Part A covers the neutrino and light-relic bounds, Part B the dark-matter bounds.

# Part A — neutrino mass and N_eff

## Neutrino budgets by analysis, read in paper bodies
<!-- key: neutrino-budgets-by-analysis-read-in-paper -->

One table per analysis; the subsections below discuss each systematic across analyses. All limits 95%, ΛCDM + Σm_ν with Σm_ν > 0 unless stated.

**DESI DR2 BAO + CMB (Elbers et al. 2025, arXiv:2503.14744; baseline < 0.0642 eV, PR4 CamSpec)** [src: abstract]

| Change | Effect on Σm_ν | Place |
|---|---|---|
| High-ℓ likelihood PR3 plik / PR4 L-H | < 0.0691 / < 0.0774 eV; L-H stays broader with the oscillation splittings imposed | [src: Sect. IV.4] |
| Other ΛCDM differences between likelihoods (lower ω_b in CamSpec and L-H; weaker A_s–τ degeneracy in L-H) | "do not appear to be directly responsible" for the offsets; A_lens is the candidate driver | [src: Sect. IV.4] |
| Add Pantheon+ / Union3 / DESY5, ΛCDM | < 0.0704 / 0.0674 / 0.0744 eV, with higher Ω_m and lower H0; in ΛCDM the CMB-likelihood offsets dominate over the SN choice | [src: Sect. IV.5] |
| Same in w0waCDM, CamSpec | < 0.117 / 0.139 / 0.129 eV; here the SN choice dominates: with DESY5, < 0.129 (plik), 0.133 (CamSpec), 0.148 eV (L-H) | [src: Sect. IV.5] |
| wCDM + SNe | < 0.0653 / 0.0649 / 0.0586 eV | [src: Sect. IV.5] |
| N_eff free | < 0.0741 eV, +15%, correlation 0.18 | [src: Sect. IV.2, Eq. 19] |
| Oscillation prior instead of Σm_ν > 0 | < 0.101 eV (NO), < 0.133 eV (IO) | [src: Sect. IV.3, Eqs. 25, 27] |
| Effective mass, no boundary | −0.101 (+0.047/−0.056) eV (68%), 3.0σ below 0.059 eV as probability to exceed; CMB alone −0.11 (+0.12/−0.14) eV | [src: Sect. V.2, Eqs. 31–32] |

The SN samples are not independent: the DESY5 low-redshift (z < 0.1) sample comes from the legacy catalogues used by the others, and Pantheon+ and Union3 share a large fraction of supernovae [src: arXiv:2503.14744 Sect. IV.5].

**ACT DR6 (Calabrese et al. 2025, arXiv:2503.14454; P-ACT-LB < 0.089 eV)**

| Change | Effect | Place |
|---|---|---|
| WMAP in place of Planck (W-ACT-LB) | < 0.088 eV | [src: Sect. VI.1.1, Eq. 33] |
| BOSS BAO in place of DESI Year-1; no BAO, with SNe | < 0.13 eV; < 0.23 eV | [src: Sect. VI.1.1] |
| τ prior widened / SRoll2 removed | < 0.10 eV / < 0.19 eV | [src: Appendix G.2] |
| N_eff free | < 0.073 eV | [src: Sect. VI.1.1] |
| Theory settings at the ΛCDM best fit: Recfast against HyRec / CosmoRec | Δχ² = 0.37 / 0.49, up to O(100) away from the best fit, mostly TT at ℓ ≈ 2000; posteriors not shifted | [src: Appendix A] |
| Halofit against HMcode 2020; dark matter only against dark matter + baryons; stronger feedback | Δχ² = 0.09; 0.20; 0.39 | [src: Appendix A] |

**SPT-3G D1 (Camphuis et al. 2025, arXiv:2506.20707)**

| Change | Effect | Place |
|---|---|---|
| τ | not measured: Gaussian prior N(0.051, 0.006) from Planck; the paper notes that τ ≈ 0.09 would reconcile CMB and DESI and "regularize neutrino mass constraints" | [src: Sects. VII.1, VII.3] |
| CMB only: SPT-3G D1 / SPT+ACT / CMB-SPA | < 0.77 / 0.58 / 0.19 eV (Planck alone < 0.25 eV) | [src: Eqs. 102–104] |
| Add DESI | < 0.081 eV (SPT-3G D1), < 0.055 eV (CMB-SPA); SPT+ACT + DESI not combined (> 3σ apart in Ω_m–h r_d) | [src: Eqs. 105–106] |
| Planck at ℓ > 1000 in place of ACT | "would likely find an even tighter upper limit" because of the Planck TT lensing excess; CMB-SPA called conservative | [src: Sect. VII.4.6] |
| CMB–DESI distance in ΛCDM | 2.5σ (SPT), 3.1σ (ACT DR6 alone with ACT lensing), 2.7σ with Planck lensing and another τ prior, 3.7σ (SPT+ACT), 3.0σ (SPT+Planck), 2.8σ (CMB-SPA) | [src: Sect. VII.3] |

**Planck 2018 (arXiv:1807.06209)**

| Change | Effect | Place |
|---|---|---|
| TT+lowE → TT,TE,EE+lowE | < 0.54 → < 0.26 eV | [src: Eqs. 56a–b] |
| Add lensing reconstruction | < 0.44 eV (TT), < 0.24 eV (TT,TE,EE) | [src: Eqs. 57a–b] |
| CamSpec in place of Plik | < 0.38 eV, < 0.27 eV with lensing: weaker because CamSpec prefers less A_L, and "for small masses the constraint is largely determined by the lensing effect" | [src: Eqs. 58a–b, Sect. 7.5.1] |
| Lensing reconstruction + BAO + θ_MC only | < 0.60 eV, almost independent of the A_L excess in the spectra | [src: Eq. 59] |
| TT+lowE + BAO, no lensing | < 0.16 eV | [src: Eq. 60a] |
| Low-ℓ polarisation history | TT-only limit 0.72 eV (2015, lowP) → 0.59 eV (SimLow) → 0.54 eV (lowE): a tighter τ restricts A_s through C_ℓ ∝ A_s e^(−2τ) | [src: Sect. 7.5.1] |

## 1. The positivity prior and the three error bars
<!-- key: the-positivity-prior-and-the-three-error-bars -->

- **Mechanism.** The posterior of Σm_ν in ΛCDM peaks at the prior edge Σm_ν = 0. The 95% limit then measures how fast the likelihood falls from the edge, and the marginal error is that of a truncated distribution.
- **Size.** For DESI DR2 BAO + CMB the same data give σ = 0.020 eV (Bayesian, Σm_ν > 0), σ = 0.043 eV (parabola fitted to the profile likelihood, minimum at −0.036 eV) and σ = 0.053 eV (posterior of the effective signed mass, 2.6 times the first) (Elbers et al. 2025, arXiv:2503.14744 [src]). A prior floor at the oscillation minimum raises the DR2 limit from 0.0642 eV to 0.105 eV (normal) or 0.135 eV (inverted); for DR1 the same change moved 0.072 eV to 0.113 eV (arXiv:2503.14744, arXiv:2404.03002 [src]).
- **Mitigation.** Quote the limit together with a boundary-free statement: the profile-likelihood parabola with a Feldman–Cousins limit, or the effective-mass posterior.
- **Validation.** Bayesian and frequentist limits agree within about 10% when both are built for Σm_ν ≥ 0 (Naredo-Tuero et al. 2024, arXiv:2407.13831 [src]); in DESI DR2 the Feldman–Cousins limit is 0.01 eV below the Bayesian one in ΛCDM and 0.01 eV above it in w0waCDM (arXiv:2503.14744 [src]). Agreement of the limits does not remove the boundary effect; it shows the two constructions truncate alike.
- **Referee citation.** arXiv:2503.14744 §5; arXiv:2407.13831.

## 2. Optical depth τ
<!-- key: optical-depth-tau -->

- **Mechanism.** The primary CMB measures A_s e^(−2τ) precisely. A larger τ means a larger A_s and a larger predicted lensing amplitude, which leaves room for neutrino suppression; τ itself comes almost entirely from Planck large-scale polarisation (arXiv:2503.14744 §5.2.1 [src]). ACT and SPT take τ from Planck, so no current CMB + BAO neutrino limit is independent of it [sec: `cosmo-cmb`].
- **Size, from the collaborations' own tests.**

| Test | Result | Citation | Flag |
|---|---|---|---|
| DESI DR2 + CMB, τ fixed at 0.067 or 0.074 (about 2σ or 3σ above 0.054 ± 0.007) | tension of the effective mass with oscillations falls from 3σ to 2.3σ or 1.7σ | arXiv:2503.14744 §5.2.1 | [src] |
| Same, large-scale polarisation excluded | tension "could be explained as a ∼2σ statistical fluctuation" | arXiv:2503.14744 §5.2.1 | [src] |
| P-ACT-LB, prior widened to τ = 0.057 ± 0.012 | Σm_ν < 0.089 eV becomes < 0.10 eV: "minimal impact" | Calabrese et al. 2025, arXiv:2503.14454 appendix | [src] |
| P-ACT-LB, SRoll2 removed | Σm_ν < 0.19 eV; τ = 0.081 ± 0.016 is then measured from lensing in the spectra | arXiv:2503.14454 appendix | [src] |
| No low-ℓ EE, DESI BAO + high-ℓ CMB + lensing | τ = 0.090 ± 0.012; w0wa preference from about 3σ to 1.4σ (Δχ²_MAP = −3.82) [src: Sect. III.2] | Sailer et al. 2025, arXiv:2504.16932 | [src] |
| No low-ℓ EE, no lensing constraints | τ = 0.091 ± 0.011; neutrino tension at 0.06 eV removed | Jhaveri, Karwal & Hu 2025, arXiv:2504.21813 | [src: abstract] |
| Imposed prior τ = 0.11 ± 0.006 | Σm_ν = 0.10 (+0.04/−0.05) eV | Sullivan, de Belsunce & Ivanov 2026, arXiv:2606.30903 | [src: abstract] |

- **What the size means.** Widening the error on τ does almost nothing; the central value has to move. A shift to about 0.09 is 3–5σ from Planck low-ℓ polarisation (arXiv:2504.16932 [src]), and Planck reprocessings give 0.051–0.063 with σ ≈ 0.006 [sec: `cosmo-cmb`]. DESI adds that τ cannot be the whole explanation, because at fixed neutrino mass a larger τ raises the CMB-preferred H0 r_d only slightly (arXiv:2503.14744 §5.2.1 [src]).
- **Mitigation.** Name the low-ℓ EE likelihood or the τ prior. Show the limit with the prior widened and with low-ℓ EE removed.
- **Validation.** Independent reionisation-history constraints; they side with the low value [sec: `cosmo-cmb`, which holds the papers; `cosmo-reionization-21cm`].
- **Referee citation.** arXiv:2504.16932, arXiv:2504.21813, and the collaboration test used (arXiv:2503.14744 §5.2.1 or the ACT appendix).

## 3. Excess lensing-like smoothing and the choice of Planck likelihood
<!-- key: excess-lensing-like-smoothing-and-the-choice-of -->

- **Mechanism.** Planck temperature spectra show more peak smoothing than ΛCDM predicts, parameterised by A_lens. Neutrino mass reduces lensing, so excess smoothing pushes Σm_ν towards and below zero. DESI describes the related signature as an oscillatory feature in the small-scale temperature spectrum that ΛCDM with positive masses does not account for and that is degenerate with A_lens (arXiv:2503.14744 §5.2.1 [src]). A_lens rescales the smoothing of the spectra only; it is not the amplitude of the lensing reconstruction [sec: `cosmo-cmb`].
- **Size.** With DESI DR2 BAO: Σm_ν < 0.0691 eV (PR3 plik), < 0.0642 eV (PR4 CamSpec), < 0.0774 eV (PR4 LoLLiPoP–HiLLiPoP). plik had A_lens > 1 at more than 2σ, CamSpec reduced it, and the L-H value is consistent with unity; CamSpec is nonetheless the tightest because it uses more PR4 data (arXiv:2503.14744 §4.4 [src]). The effective-mass tension is weaker with L-H but present with all three (§5.2.1 [src]). The A_lens values themselves (1.180 ± 0.065 for PR3 Plik, 1.039 ± 0.052 for PR4 HiLLiPoP, 1.007 ± 0.057 for ACT DR6) are in `cosmo-cmb` [sec].
- **The opposing readings.** ACT finds that replacing Planck by WMAP changes nothing (< 0.088 against < 0.089 eV) and concludes, with reference to an independent decomposition, that once CMB lensing and BAO are included the spectra are sub-dominant and the excess smoothing is not the main driver (arXiv:2503.14454 §6.1.1 [src]). Cozzumbo et al. 2025 (arXiv:2511.01967) give the lensing sector two free amplitudes, one for peak smoothing and one for the reconstruction, and obtain an effective mass of −0.018 (+0.085/−0.089) eV with no tension [src]. Both can hold: the limit is robust to the Planck smoothing excess, while the significance of the negative preference is not robust to freeing the lensing amplitudes, because the width grows to about 0.087 eV, 1.6 times the DESI DR2 effective-mass width, and the centre moves to −0.018 eV [der: 0.087/0.053; the two data combinations are not identical].
- **Mitigation.** State the Planck likelihood and release. Repeat the fit with a PR4 likelihood, and with A_lens marginalised if the claim is a tension.
- **Validation.** The route that uses only primary CMB with A_lens marginalised plus the reconstructed lensing spectrum, without any late-time distance data, gives Σm_ν < 0.41 eV (Qu et al. 2026, arXiv:2607.24742 [src]). That is the size of the bound when both the geometric channel and the smoothing are removed.
- **Referee citation.** arXiv:2503.14744 §4.4; arXiv:2511.01967; arXiv:2607.24742.

## 4. The BAO data and the CMB–BAO mismatch
<!-- key: the-bao-data-and-the-cmb-bao-mismatch -->

- **Mechanism.** The tight limits are geometric. BAO fix Ω_m; the CMB fixes ω_b and ω_cdm; DESI distances are smaller than CMB data allow in ΛCDM with positive masses, a discrepancy in H0 r_d, and at fixed θ* a lower neutrino mass compensates it (arXiv:2503.14744 §5.2.1 [src]; Loverde & Weiner 2024, arXiv:2410.00090). With the effective mass fixed at −0.11 eV the CMB alone gives H0 = 68.96 ± 0.49 km/s/Mpc and matches DESI (arXiv:2503.14744 §5.2.1 [src]).
- **Size.** Same CMB and lensing data, different distance data: < 0.089 eV with DESI DR1, < 0.13 eV with BOSS BAO, < 0.23 eV with supernovae and no BAO (arXiv:2503.14454 §6.1.1 [src]). ACT states that its exclusion of the inverted ordering "strongly depends on the use of DESI BAO data".
- **Shift versus information.** Adding CMB lensing to DR1 BAO + CMB narrows the profile width by 0.023 eV and moves the minimum by +0.020 eV; adding the DR1 full shape changes the width by 0.003 eV and lowers the limit through a shift towards negative values (arXiv:2503.14744 §5.1 [src]).
- **Mitigation.** Quote the consistency of the CMB and BAO data sets in the model being fitted before combining them. The CMB–DESI DR2 distance in ΛCDM is 2.3σ in the DESI paper [sec: `cosmo-galaxy-clustering`] and 1.6σ, 2.8σ or 3.7σ for P-ACT, CMB-SPA or SPT+ACT [sec: `cosmo-cmb`].
- **Validation.** A limit with a second BAO data set, or without BAO.
- **Referee citation.** arXiv:2503.14744 §5.2.1; arXiv:2410.00090.

## 5. The dark-energy model and the supernova sample
<!-- key: the-dark-energy-model-and-the-supernova-sample -->

- **Mechanism.** Neutrino mass and the late-time expansion history both change the distance to last scattering at fixed physical densities. A model that absorbs the BAO–CMB mismatch elsewhere releases the pressure on Σm_ν.
- **Size.** DESI DR2 BAO + CMB: < 0.0642 eV (ΛCDM), < 0.0851 eV (wCDM), < 0.163 eV (w0waCDM). With supernovae the w0waCDM limit is 0.117, 0.139 or 0.129 eV for Pantheon+, Union3 or DESY5, while in wCDM supernovae tighten the limit to 0.0586–0.0653 eV (arXiv:2503.14744 Table 2 [src]). The effective mass in w0waCDM is 0.06 (+0.15/−0.10) eV (Elbers et al. 2024, arXiv:2407.10965 [src]).
- **Mitigation.** State the model with the limit; in a text that also argues for evolving dark energy, quote the w0waCDM limit. A dark-energy-independent construction gives < 0.152 eV, stable under binned and cubic w(a) (arXiv:2607.24742 [src: abstract]).
- **Validation.** Limits with each supernova compilation. The compilations were recalibrated in 2025–2026 (`cosmo-supernovae`); the neutrino limits in the DESI table predate those revisions and have not been recomputed in a paper read here.
- **Referee citation.** arXiv:2503.14744 Table 2; arXiv:2407.10965.

## 6. Full-shape analyses: nuisance priors and external reanalyses
<!-- key: full-shape-analyses-nuisance-priors-and -->

- **Mechanism.** The scale-dependent suppression is degenerate with galaxy bias and EFT counterterms; in extended models the marginal posterior depends on the prior volume of those parameters.
- **Size.** In the DESI analysis the DR1 full shape adds almost no width (0.003 eV) (arXiv:2503.14744 [src]). The tightest published numbers, < 0.049 eV in ΛCDM and < 0.077 eV in w0waCDM, come from an external reanalysis that adds the bispectrum and cross-correlations (Ivanov et al. 2026, arXiv:2601.16165 [src]); its authors state the w0waCDM limit is 37% tighter than background data alone.
- **Mitigation and validation.** Ask for the profile likelihood or the best fit next to the posterior, and for the mock validation of the prior choice. `cosmo-galaxy-clustering` documents how large the offset between best fit and posterior mean becomes in extended models.
- **Referee citation.** arXiv:2503.14744 §2.8 and §5.1; arXiv:2601.16165.

## 7. Assumptions about the neutrino background itself
<!-- key: assumptions-about-the-neutrino-background-itself -->

- **Mechanism.** The conversion from energy density to mass assumes three species with a Fermi–Dirac distribution at the standard temperature, stable over the age of the Universe.
- **Size.** Photon injection after neutrino decoupling changes the Planck + lensing + DESI limit from 0.0691 eV to 0.0652 eV (decay to photons only) or 0.0710 eV (photons and dark radiation); the shift is at most 0.004 eV for fixed splittings; a free neutrino-to-photon temperature ratio gives 0.0724 eV. The neutrino temperature and Σm_ν are positively correlated, so a lower radiation density worsens the tension (Figueroa, Sobotka & Erickcek 2026, arXiv:2609.15970 [src]). With N_eff free the DESI DR2 limit is 0.0741 eV with correlation 0.18 (arXiv:2503.14744 [src]); ACT finds 0.073 eV (arXiv:2503.14454 §6.1.1 [src]).
- **What is not covered.** ACT notes that neutrinos that decay, or whose mean momentum exceeds the thermal value, could still be compatible with the inverted-ordering band (arXiv:2503.14454 §6.1.1 [src]). Decaying dark matter relaxes the bound to about 1 eV only if perturbation data are ignored; the full Planck likelihood with lensing restores ≲ 0.079 eV (Montandon et al. 2026, arXiv:2603.03284 [src]).
- **Convention trap.** ACT fixes 0.06 eV in a single massive state as its baseline and uses three massive species when the mass varies (arXiv:2503.14454 [src]). The number of massive states changes the limit at the level at which results are now compared.
- **Referee citation.** arXiv:2609.15970.

## 8. Mass-ordering statements
<!-- key: mass-ordering-statements -->

- **Mechanism.** The Bayes factor between orderings is the ratio of prior volume left by an upper limit that sits between the two minimum masses; it depends on the prior measure on the masses as much as on the data.
- **Size.** K = 10 for DESI DR2 + CMB + NuFIT 6.0 with the CamSpec likelihood, 6 with L-H and 8 with plik; Δχ² = 4.6 (arXiv:2503.14744 [src]). Other prior constructions give 46.5 (Jiang et al. 2024, arXiv:2407.18047) and more than 460 in ΛCDM or more than 40 in extensions, with the prior measure changing K by a factor of about 10 (Jimenez et al. 2026, arXiv:2606.18987) [src].
- **Mitigation.** Give the prior on the masses, the frequentist Δχ², and the result in w0waCDM. Oscillation data alone fit both orderings almost equally well unless the Super-Kamiokande atmospheric table is added (Esteban et al. 2024, arXiv:2410.05380 [src]).
- **Validation.** The laboratory: JUNO with accelerator constraints favours normal ordering at ≥ 2.1σ, Bayes factor 10.18 (JUNO Collaboration 2026, arXiv:2609.37895 [src: abstract]).

## 9. N_eff
<!-- key: neff -->

| Systematic | Mechanism | Size | Citation | Flag |
|---|---|---|---|---|
| Which CMB data | ACT prefers "somewhat less damping than the Planck best-fit model" | 2.60 (+0.21/−0.29) for ACT alone, 2.73 ± 0.14 for P-ACT, against 3.18 (+0.29/−0.33) for SPT-3G D1 | arXiv:2503.14454 §6.1.1; Camphuis et al. 2025, arXiv:2506.20707 | [src] |
| Adding BAO | BAO prefer larger H0 r_d and smaller Ω_m, which N_eff absorbs | P-ACT 2.73 → P-ACT-LB 2.86 (DR1) → 2.92 ± 0.12 (DR2); DESI DR2 + Planck 3.23 ± 0.18; SPT + DESI 3.53 ± 0.23 | arXiv:2503.14454; arXiv:2503.14744; arXiv:2506.20707 | [src] |
| One-sided prior | fitting only ΔN_eff ≥ 0 | the 95% limit is 0.17 for P-ACT-LB but 0.14 for P-ACT: lensing and BAO relax it by moving the posterior up | arXiv:2503.14454 §6.1.1 | [src] |
| Primordial spectrum | a power law is assumed | self-interacting dark radiation: N_idr < 0.134 becomes ΔN_eff < 0.58 with running and running-of-running free | Garny, Niedermann & Sloth 2026, arXiv:2604.26541 | [src] |
| Free-streaming or fluid | only free-streaming radiation produces the phase shift | separate parameters N_eff and N_idr | Bashinsky & Seljak 2003, arXiv:astro-ph/0310198 | [src] |
| Helium | the damping tail is degenerate with Y_P | BBN consistency imposed, or Y_P freed | arXiv:astro-ph/0310198 | [src] |
| Epoch | BBN and CMB measure radiation at different times | −0.708 < N_ν^CMB − N_ν^BBN < 0.328 | Yeh et al. 2022, arXiv:2207.13133 | [src: abstract] |

A low N_eff cannot be attributed to photon heating at late times: raising the photon energy density by the 12% (P-ACT) or 6% (P-ACT-LB) needed would produce spectral distortions μ = 0.16 or y = 0.03 (0.09 or 0.02), excluded by COBE/FIRAS; only injection at 2 × 10⁶ < z < 10⁹ escapes (arXiv:2503.14454 §6.1.1 [src]). Do not combine CMB and BAO for N_eff without stating their mutual consistency in ΛCDM + N_eff [sec: `cosmo-cmb`].

## 10. BBN inputs
<!-- key: bbn-inputs -->

- **Nuclear rates.** The baryon density from D/H depends on the deuterium-burning rates: ab-initio theoretical rates favour lower Ω_b h², experimental rates higher. Marginalising over rates gives Ω_b h² = 0.02218 ± 0.00055 (Schöneberg 2024, arXiv:2401.15054 [src]), four times the error of the 0.02236 ± 0.00014 obtained with BBN + CMB and N_ν = 3 (Yeh et al. 2026, arXiv:2601.22239 [src]) [der: 0.00055/0.00014].
- **Helium.** The predicted Y_P = 0.24709 ± 0.00017 (Pitrou et al. 2018, arXiv:1801.08023) is far more precise than the measured 0.2458 ± 0.0013 (arXiv:2601.22239) [src]; N_ν from BBN is limited by the observational helium systematics, which this session did not research.
- **Convention.** N_ν with baseline 3 in BBN papers, N_eff with baseline 3.044 in CMB papers (arXiv:2207.13133 [src: Sect. 1]).
- **Referee expectation.** A "BBN prior" names the code and the rate compilation.

# Part B — dark-matter properties

## Dark-matter budgets by analysis, read in paper bodies
<!-- key: dark-matter-budgets-by-analysis-read-in-paper -->

**Lyα forest, HIRES + UVES, z = 4.2–5.0 (Iršič et al. 2023, arXiv:2309.04533; baseline m_WDM > 5.7 keV, 95%)** [src: abstract]

| Change | Effect | Place |
|---|---|---|
| Thermal model | 12 thermal histories (end of reionisation z = 5.35–7.41; T0(z = 4.6) ≈ 6400–14600 K) crossed with m_WDM = 2, 3, 4 keV, σ8 and n_s: 144 Sherwood simulations, linear-interpolation emulator (error ≤ 1.2% at high k and z) | [src: Sect. III, Table 1, Sect. III.1] |
| Simulation-envelope thermal prior → Gaussian T0 prior (1000 K) from independent measurements | > 5.85 keV; 3σ and 5σ exclusions 3.75 and 3.21 keV (baseline 3.73 and 3.18 keV) | [src: Sects. IV.2, IV.4] |
| k_max = 0.2 → < 0.1 s/km, same thermal treatment | > 4.09 keV; u0 (pressure smoothing) no longer constrained; earlier HIRES/MIKE with k_max = 0.088 s/km and a wide thermal prior gave about 2.1 keV | [src: Sect. IV.9] |
| Inhomogeneous reionisation | tabulated Sherwood-Relics correction applied; large-scale enhancement lies at k < 5 × 10⁻³ s/km, outside the data; small-scale thermal and pressure effects may cancel | [src: Sect. IV.7] |
| Goodness of fit | χ² = 40.7 for 34 d.o.f.; 20.4 for 20 at k < 0.1 s/km; all three redshift bins lie above the model at k > 0.1 s/km, "a possible shortcoming of the model on the smallest scales" | [src: Sect. IV.2] |

**Lyα forest, Boera et al. spectra, 4.2 ≤ z ≤ 5.0 (Villasenor et al. 2022, arXiv:2209.14220; > 3.1 keV, 95%)**

| Item | What was done or found | Place |
|---|---|---|
| Thermal-history family | 1080 simulations (25 h⁻¹ Mpc, 2 × 1024³) over m_WDM and three transformations of a fiducial UV background: Γ_i(z) → β Γ_i(z − Δz), 𝓗_i(z) → β α_E 𝓗_i(z − Δz); β sets the mean flux, α_E the temperature, Δz the timing of reionisation (about 200 Myr span) | [src: Sect. 3.3] |
| Helium | He II photorates fixed: He II reheating matters only at z < 4 | [src: Sect. 3.3] |
| Uniform UV background replaced by a patchy-reionisation correction (10–15% small-scale suppression at k ≈ 0.1 s/km) | limit > 3.8 keV, peak 7.1 keV, ΛCDM inside the 95% interval; but χ² rises from 38.3 to 46.4, so the uniform case is kept as the main result | [src: Sect. 5.6] |
| Baseline peak | maximum likelihood at 4.5 keV, χ² = 38.3, against 40.9 for the ΛCDM best fit | [src: Sect. 5.6] |

Both Lyα analyses correct for inhomogeneous reionisation with different simulation-based prescriptions; here the correction moves the likelihood to higher masses and worsens the fit. Compare §11.

**Strong lensing, JWST, 28 quads with arcs (Gilman et al. 2025, arXiv:2511.07513)**

| Change | Effect on m_hm (Bayes factor 10:1) | Place |
|---|---|---|
| Σ_sub prior log-uniform over a factor 100 | m_hm < 10^8.6 M⊙ (about 3.0 keV with Eq. 18 [der]) | [src: Sect. VII] |
| Σ_sub prior from Galacticus / N-body | < 10^7.4 / 10^7.2 M⊙ (6.5 / 7.4 keV) | [src: Sect. VI.2] |
| Arcs omitted | 0.4–0.5 dex weaker | [src: Sect. VI.2] |
| Subhalo structure evaluated at infall rather than z = 0 | subhaloes denser by a factor 10–200; changes the meaning of Σ_sub relative to earlier work | [src: Sect. VII.1] |
| Source size | Gaussian emission region, FWHM uniform in 1–10 pc (warm dust) or 20–80 pc (narrow-line region) | [src: Sect. V.4] |
| Macromodel | elliptical power law + external shear + m = 1, 3, 4 multipoles with free amplitudes and orientations; luminous satellites as SIS; earlier WDM lensing studies had no or fewer angular degrees of freedom | [src: Sects. V.1, VII.1, Table 2] |
| Prior on m_hm | log10 m_hm uniform on [4, 10] | [src: Sect. III table] |

**Lensing flux ratios + Milky Way satellites, joint (Nadler et al. 2021, arXiv:2101.07810; > 9.7 keV, 95%)**

| Change | M_hm limit (95% / 20:1) | m_WDM (95% / 20:1) | Place |
|---|---|---|---|
| Fiducial: baryonic subhalo disruption equally efficient in the Milky Way and in lenses (q = 1) | 10^7.0 / 10^7.4 M⊙ | 9.7 / 7.4 keV | [src: Sect. 6.1 table] |
| Disruption twice as efficient in the Milky Way (q = 0.5) / in lenses (q = 2) | 10^7.1 / 10^7.6; 10^6.9 / 10^7.3 M⊙ | 9.1 / 6.4; 10.4 / 7.9 keV | [src: Sect. 6.1 table] |
| Product of the one-dimensional M_hm posteriors instead of the joint (Σ_sub, M_hm) combination | 10^7.2 / 10^7.7 M⊙ | 8.4 / 6.0 keV | [src: Sect. 6.1 table] |
| Criterion | 95% limits depend on the arbitrary lower edge of the M_hm prior; 20:1 likelihood ratios less so; log prior on M_hm adopted | — | [src: Sect. 6.1] |

**Stellar streams GD-1 and Pal 5 (Banik et al. 2019, arXiv:1911.02663; > 3.6 keV)**

| Change | Effect | Place |
|---|---|---|
| GD-1 alone | > 4.6 keV; Pal 5 has a weak preference for small masses | [src: Sect. 4.1] |
| Inner-Galaxy WDM subhalo suppression | for 3.3 keV, simulations with tides find subhaloes 3 times (10⁷–10⁸ M⊙) and 1.75 times (10⁸–10⁹ M⊙) more abundant than the standard fit; refitted as γ = 1.5, β = 0.7 instead of 2.7, 0.99 | [src: Sect. 3.1] |
| Amplitude and survival fraction | fully degenerate with streams alone; marginalised; slope varied in [−1.95, −1.85] | [src: Sect. 4.1] |
| Posterior shape | plateaus above about 10 keV | [src: Sect. 4.1] |

## 11. Lyman-α forest: the thermal history
<!-- key: lyman-alpha-forest-the-thermal-history -->

- **Mechanism.** Free streaming, thermal Doppler broadening and pressure smoothing all remove small-scale flux power; the last depends on the whole heating history, not on the temperature at the redshift observed [sec: `cosmo-lyman-alpha`].
- **Size.** The same class of z > 4 high-resolution data gives, for a thermal relic:

| Thermal-history assumption | m_WDM limit | Citation | Flag |
|---|---|---|---|
| T(z) a power law | > 5.3 keV | Iršič et al. 2017, arXiv:1702.01764 | [src] |
| temperature jumps up to 5000 K allowed | > 3.5 keV | arXiv:1702.01764 | [src: abstract] |
| wide range of histories, 1080 simulations | > 3.1 keV | Villasenor et al. 2022, arXiv:2209.14220 | [src: abstract] |
| coldest reionisation histories allowed by data | > 1.9 keV | Garzilli et al. 2019, arXiv:1912.09397 | [src] |
| histories wide enough that a warm intergalactic medium fits the cutoff | no limit | Garzilli, Boyarsky & Ruchayskiy 2015, arXiv:1510.07006 | [src] |
| thermal history and inhomogeneous reionisation marginalised, k_max = 0.2 s/km | > 5.7 keV | Iršič et al. 2023, arXiv:2309.04533 | [src: abstract] |
| same, k_max < 0.1 s/km and earlier priors | > 4.1 keV | arXiv:2309.04533 | [src: abstract] |

- **Mitigation.** Marginalise over a thermal-history family wide enough to include late and cold reionisation; include inhomogeneous reionisation; use independent temperature measurements as priors and say so.
- **Validation.** Stability of the limit under k_max cuts and under dropping redshift bins.
- **For fuzzy dark matter** the same dependence gives > 20 × 10⁻²² eV with temperature jumps against > 37.5 × 10⁻²² eV for a power law (Iršič et al. 2017, arXiv:1703.04683 [src]), and published limits from comparable data span 1.9 × 10⁻²¹ to 2 × 10⁻²⁰ eV (Liu, Gong & Zhou 2026, arXiv:2606.06969; Rogers & Peiris 2020, arXiv:2007.12705 [src]).
- **Referee citation.** arXiv:1912.09397 and arXiv:2309.04533 together.

## 12. From a cutoff scale to a particle mass
<!-- key: from-a-cutoff-scale-to-a-particle-mass -->

- **Production mechanism.** One data set: > 0.55 keV for a thermal relic, > 2.0 keV for a sterile neutrino (Viel et al. 2005, arXiv:astro-ph/0501562 [src]). The 7.1 keV sterile neutrino is excluded by structure formation only for lepton asymmetries L6 > 10 (Enzi et al. 2020, arXiv:2010.13802 [src]).
- **Half-mode conversion.** M_hm = 10^7.8 M⊙ is quoted as 5.2 keV (Gilman et al. 2019, arXiv:1908.06983) and as 5.6 keV (Keeley et al. 2025, arXiv:2511.07765); 10^7.4 M⊙ as 6.5 keV (Gilman et al. 2025, arXiv:2511.07513) and as 7.4 keV (Nadler et al. 2021, arXiv:2101.07810) [src]. The difference is the transfer-function fit, the cosmology and M⊙ against M⊙/h. A 0.9 keV spread from the conversion alone is as large as the differences between probes [der: 7.4 − 6.5].
- **Confidence level.** 95% limits, 20:1 posterior-odds limits and 10:1 Bayes-factor limits coexist: 6.20 keV at 95% is 5.75 keV at 20:1 (Liu, Gong & Liao 2025, arXiv:2512.01361 [src]); the joint analysis of Enzi et al. gives 6.048 keV at 95% and 2.552 keV with a likelihood-ratio 1/20 criterion (arXiv:2010.13802 [src]).
- **Other models.** Matching the half-mode scale overestimates the constraint for dark matter–neutrino scattering (Mosbech et al. 2026, arXiv:2607.15020 [src]); for ultralight fields the mapping depends on the field power spectrum (Nadler et al. 2026, arXiv:2605.15371 [src]).
- **Mitigation.** Compare limits in M_hm with one unit convention, or recompute the mass with one relation; state the criterion.

## 13. Milky Way satellite counts
<!-- key: milky-way-satellite-counts -->

Source for this section: the supplement of Nadler et al. 2020 (arXiv:2008.00022 [src]).

- **Host halo.** The model rests on two dark-matter-only zoom-in simulations with virial masses 1.57 × 10¹² and 1.26 × 10¹² M⊙, chosen for a Gaia-Enceladus-like merger and a realistic LMC analogue. The Milky Way mass is marginalised and is "the most important nuisance parameter governing the SHMF" for such hosts.
- **The LMC.** Hosts without a realistic LMC analogue under-predict the satellites in the DES footprint, and an analysis using them "would yield biased (and more stringent) dark matter constraints". The small number of suitable simulations is named as the main limitation.
- **Subhalo disruption.** The simulated hosts are less concentrated than the real, baryon-contracted Milky Way halo, which may change the disruption efficiency beyond the disk-disruption term that is modelled and marginalised.
- **Galaxy–halo connection.** Eight parameters: slope and scatter of the luminosity–V_peak relation; amplitude, scatter and slope of the size relation; the occupation fraction; the disk-disruption efficiency. A cutoff in the subhalo mass function is partly degenerate with a cutoff in galaxy occupation.
- **Selection.** Detection probabilities as a function of luminosity, size, distance and sky position enter a Poisson likelihood in surface-brightness bins.
- **Validation.** Consistency of the inferred galaxy–halo connection with hydrodynamical simulations; the joint Milky Way + M31 analysis gives 6.20 keV against 6.5 keV for the Milky Way alone (arXiv:2512.01361, arXiv:2008.00022 [src]).
- **Referee citation.** arXiv:2008.00022 and the census papers it builds on, which this session did not fetch.

**Milky Way + M31 satellites (Liu, Gong & Liao 2025, arXiv:2512.01361; > 6.20 keV, 95%)** [src: abstract]

| Item | What was done or found | Place |
|---|---|---|
| Hosts | 45 dark-matter-only Milky Way-mass zoom-ins (1.18–1.57 × 10¹² M⊙), subhaloes resolved to V_max ≈ 9 km/s, V_peak > 10 km/s; two Milky Way analogues (1.26, 1.57 × 10¹²) and two M31 hosts (1.19, 1.35 × 10¹²) | [src: Sect. IV.2] |
| Completeness | DES and PS1 detection probabilities from machine-learning classifiers in M_V, distance, r_1/2 and sky position; satellites within 300 kpc and r_1/2 > 10 pc; M31 from PAndAS with an analytic selection function, 30–300 kpc, r_1/2 > 63 pc; 58 satellites in all | [src: Sect. III] |
| Disruption | one parameter 𝓑 for baryonic subhalo disruption among eight galaxy–halo parameters | [src: Sect. IV.3] |
| M31 mass prior | the larger prior gives > 6.07 keV (5.61 keV at 20:1), against 6.20 (5.75) | [src: Sect. V.2, Eqs. 20–21] |
| Gain from M31 | few percent; about 10% overall relative to the Milky Way alone, which the paper quotes as 5.9 keV from an earlier Nadler et al. analysis | [src: Sect. V.2]; [sec] for 5.9 keV |
| Criterion | M_hm < 3.23 × 10⁷ M⊙ (95%) and < 4.23 × 10⁷ M⊙ (20:1) | [src: Sect. V.2] |

## 14. Strong-lensing flux ratios and arcs
<!-- key: strong-lensing-flux-ratios-and-arcs -->

Source for the priors: Gilman et al. 2025 §4.3 (arXiv:2511.07513 [src]).

- **Subhalo abundance.** The amplitude of the subhalo mass function Σ_sub is degenerate with the half-mode mass: fewer subhaloes from tides look like fewer subhaloes from free streaming. The CDM prediction is uncertain: the Symphony N-body simulations predict a bound mass function about 50% below the Galacticus semi-analytic model in the inner host. The two priors are log10 Σ_sub/kpc⁻² = −0.8 ± 0.2 (Galacticus) and −1.0 ± 0.2 (N-body), and the 0.2 dex between them is taken as the representative systematic.
- **Size.** That choice moves the limit from 5.6 to 6.4 keV with flux ratios alone (arXiv:2511.07765) and from 6.5 to 7.4 keV with arcs (arXiv:2511.07513, arXiv:2606.05277) [src]. The lower abundance gives the stronger limit.
- **Tidal model.** The mean bound mass fraction is 0.05 for a 10¹³ M⊙ host at z = 0.5, with a further 15% suppression from the central galaxy; both are model inputs.
- **Robust inputs.** The line-of-sight halo mass function amplitude is varied by ±10% around Sheth–Tormen and the subhalo slope within −1.95 to −1.85; the host mass has a prior log10 m_host/M⊙ = 13.3 ± 0.3; haloes are rendered down to 10⁶ M⊙; the M_hm prior is log-uniform over 10⁴–10¹⁰ M⊙. A Bayes-factor or posterior-odds limit depends on that range, since models below about 10⁵ M⊙ are indistinguishable from CDM in the analysis.
- **Lens model.** Smooth-model angular structure (m = 1, 3, 4 multipoles), source size, luminous satellites and globular clusters can imitate or hide substructure (arXiv:2511.07765 [src]). Imaging of the arcs breaks the Σ_sub–M_hm covariance and gains 0.4 dex (arXiv:2511.07513 [src]).
- **Validation.** The measured CDM subhalo abundance compared with both predictions; limits quoted for both priors.
- **Referee citation.** arXiv:2511.07765, arXiv:2511.07513.

## 15. Stellar streams, luminosity functions, dwarf kinematics
<!-- key: stellar-streams-luminosity-functions-dwarf -->

| Probe | Dominant systematic | Size where quantified | Citation | Flag |
|---|---|---|---|---|
| GD-1, Pal 5 density | normalisation and slope of the subhalo mass function in the inner Galaxy, tidal disruption | 3.6 keV from streams alone, 6.2 keV only with satellite counts | Banik et al. 2019, arXiv:1911.02663 | [src: abstract] |
| Ultraviolet luminosity functions | star-formation efficiency and its scatter are degenerate with a delay in halo formation | ≥ 3.2 keV after marginalisation, weaker than the headline Lyα, satellite and lensing limits | Liu, Shan & Zhang 2024, arXiv:2404.13596 | [src] |
| Same, dark matter–proton scattering | as above | for n = 0 within an order of magnitude of the Lyα and satellite limits | Lazare et al. 2025, arXiv:2510.10757 | [src] |
| Dwarf sizes and dispersions (fuzzy dark matter) | heating by granules assumes the soliton–halo structure and no other heating or cooling history | > 3 × 10⁻¹⁹ eV at 99%, 15 to 150 times the other limits [der: against 2 × 10⁻²⁰ and 2 × 10⁻²¹ eV] | Dalal & Kravtsov 2022, arXiv:2203.05750 | [src] |
| Leo II kinematics | wavefunction reconstruction; independent of cosmology and production | > 2.2 × 10⁻²¹ eV | Zimmermann et al. 2024, arXiv:2405.20374 | [src] |
| One VLBI arc | a single lens; smooth-lens and source model | ≤ 4.4 × 10⁻²¹ eV excluded at 20:1 | Powell et al. 2023, arXiv:2302.10941 | [src] |

## 16. Combined small-scale limits
<!-- key: combined-small-scale-limits -->

- **Non-independence.** Joint limits reuse the same satellite census and earlier lensing posteriors. The 9.7 keV of Nadler et al. 2021 (arXiv:2101.07810) combines the satellite analysis with the 2019 eight-lens posterior and reports a 30% gain over either; it has not been redone with the JWST sample in a paper found here. The stream + satellite limit of 6.2 keV and the Lyα + lensing + satellite limit of 6.048 keV use overlapping satellite information (arXiv:1911.02663, arXiv:2010.13802 [src]).
- **Shared theory.** The subhalo mass function and its tidal evolution enter satellites, streams and lensing alike; an error there is common-mode, and agreement between these three probes is weaker evidence than it looks. The Lyα forest (thermal history), the luminosity functions (star-formation efficiency) and dwarf kinematics have unrelated systematics.
- **Mitigation.** Quote each probe's own limit next to the combination.

## 17. Interacting and self-interacting dark matter
<!-- key: interacting-and-self-interacting-dark-matter -->

- **Scale probed.** CMB limits and satellite limits on the same dark matter–baryon cross section differ by orders of magnitude because satellites probe smaller scales (Nadler et al. 2019, arXiv:1904.10000 [src]); state the probe with the cross section, and the velocity index n.
- **Self-interaction, mergers.** The offset method depends more on how the centroids are measured than on the initial conditions, and early Bullet Cluster limits were overstated (Robertson, Massey & Eke 2016, arXiv:1605.04307 [src]). The ensemble offset is 5.8 ± 8.2 kpc (Harvey et al. 2015, arXiv:1503.07675 [src]).
- **Self-interaction, profiles.** Jeans modelling assumes equilibrium and a baryon model; with core collapse included about 1/6 of SPARC galaxies admit both a core-growth and a core-collapse solution, giving an L-shaped degeneracy between σ0 and the velocity scale (Jia et al. 2026, arXiv:2601.17118 [src]).
- **Velocity.** σ/m of 0.5 ± 0.2 cm²/g in groups and 0.19 ± 0.09 cm²/g in clusters refer to different velocities (Sagunski et al. 2020, arXiv:2006.12515 [src: abstract]); a limit without its velocity cannot be compared with another.

## 18. Sub-component axions, decays, the X-ray line
<!-- key: sub-component-axions-decays-the-x-ray-line -->

- **Axion hints from one data set.** A 2.7σ preference at 10⁻²⁶ eV in BOSS alone (Rogers et al. 2023, arXiv:2301.08361), a mild preference in the DESI luminous red galaxies that vanishes with the CMB (Verdiani et al. 2026, arXiv:2607.11876), and a 2.1σ preference at 10⁻²⁴·⁵ eV in ACT lensing driven by a few points (Laguë et al. 2026, arXiv:2606.06410) [src]. None survives combination; all depend on the non-linear model of the non-cold component.
- **Decays.** Bayesian and profile-likelihood 68% regions differ strongly for two-body decays because of prior volume (Montandon et al. 2025, arXiv:2505.20193 [src]); the "best fit" lifetime of 120 Gyr with a 1.2% kick exists only with an S8 prior (Simon et al. 2022, arXiv:2203.07440 [src]).
- **3.5 keV line.** The blank-sky exclusion depends on the background model: the limit relaxes by a factor of about 20, or by more than an order of magnitude, under the alternatives proposed in two comments (arXiv:2004.06170, arXiv:2004.06601, on Dessert, Rodd & Safdi 2018, arXiv:1812.06976 [src]).

## 19. What a referee checks in a results section
<!-- key: what-a-referee-checks-in-a-results-section -->

Neutrino mass and N_eff:

1. The model (ΛCDM, wCDM, w0waCDM) and the number of massive states are stated with the limit.
2. The Planck release and high-ℓ likelihood, the lensing data, the BAO release and the supernova sample are named.
3. The low-ℓ EE likelihood or τ prior is named, and the limit is shown with the prior widened or removed.
4. A boundary-free statement accompanies the Bayesian limit: profile parabola, Feldman–Cousins limit or effective mass. The quoted σ is identified as truncated or not.
5. An "improved" limit is decomposed into a change of width and a shift.
6. The consistency of CMB and BAO in the fitted model is quoted before they are combined.
7. A tension with oscillations names the metric and the oscillation fit; an ordering preference names the mass prior and gives Δχ².
8. Collaboration results are distinguished from external reanalyses.
9. N_eff: free-streaming or fluid; Y_P treatment; one-sided or two-sided; primordial-spectrum assumption; standard value 3.044.
10. A BBN prior names code and rates.

Dark matter:

11. Thermal relic or another production mechanism; fraction of the dark matter.
12. The half-mode mass, its unit convention and the conversion used; 95%, 20:1 or 10:1.
13. Lyα: thermal-history family, treatment of reionisation, k_max, redshift range.
14. Satellites: host-halo selection and LMC analogue, Milky Way mass, disruption model, selection function.
15. Lensing: subhalo-abundance prior and result under the alternative, multipoles, source size, line-of-sight haloes, M_hm prior range.
16. Combined limits: which posteriors are reused and what they share.
17. Fuzzy dark matter: which probe, and for the dwarf-heating limit its dynamical assumptions.
18. Self-interaction: the velocity; for mergers the centroid method; for profiles core growth against core collapse.
19. Interacting dark matter: dedicated simulations or a half-mode mapping.
20. A hint from one data set is shown against the combination.

## Not verified
<!-- key: not-verified -->

- Observational systematics of the primordial helium determination (LBT Y_p Project) were not researched.
- Stream analyses: Sects. 3.1 and 4.1 of arXiv:1911.02663 were read (Part B budget table); its treatment of baryonic substructures (Sect. 2.3) and stream progenitor modelling were not.
- The effect on the limit of the alternative inner-Galaxy subhalo suppression (γ = 1.5, β = 0.7) in arXiv:1911.02663 was not read. [src: Sect. 3.1]
- Effect of the source-size and multipole priors on the JWST limits: priors read (arXiv:2511.07513 Sects. V.1, V.4), no ablation found in the sections read.
- Blinding practice of the small-scale dark-matter analyses was not read.
- The decomposition of the neutrino bound that ACT cites for the statement that excess smoothing is not the primary driver was not fetched; the statement is quoted from ACT.
- The effect of the 2025–2026 supernova recalibrations on the w0waCDM neutrino limits was not found in any paper read here.
