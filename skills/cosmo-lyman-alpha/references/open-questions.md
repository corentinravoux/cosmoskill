# Lyman-alpha forest — open questions, tensions and stale claims

Scope: live controversies with both sides cited, internal tensions between analyses, method debates, what the next data decide, labelled forecasts, and the misconceptions that still circulate.
Snapshot: 2026-10-14

Flags: `[src]` read this session in the cited paper (abstract unless a section is named); `[der]` derived here; `[sec]` secondary.

## 1. Is the small-scale linear power from the forest consistent with the CMB?
<!-- key: is-the-small-scale-linear-power-from-the-forest -->

This is the central open question of P1D cosmology, and the answer depends on the data set and on the modelling.

**The claim of tension.** Rogers & Poulin (arXiv:2311.16377) find that Planck CMB + BAO + SNe under ΛCDM are in 4.9σ tension with the eBOSS Lyα compressed likelihood in the linear power at k ~ 1 h/Mpc and z = 3, and that running α_s ~ −0.01, a 1–5% fraction of ~10⁻²⁵ eV ultra-light axions, or ~10 eV warm dark matter would alleviate it [src]. The eBOSS collaboration analysis had itself reported α_s = −0.010 ± 0.004 with Planck (arXiv:1911.09073) [src], and the BOSS DR9 analysis a "weak tension on n_s" absorbed by running (arXiv:1506.05976) [src]. The same preference for low n_s is what makes the eBOSS P1D exclude Hubble-tension-resolving early dark energy: f_EDE < 0.03 (arXiv:2303.00746) [src].

**The reanalyses of the same eBOSS DR14 data.**

- PRIYA (arXiv:2309.03943): after removing a subset of the P1D data found to be in internal tension, n_P = 1.009 (+0.027/−0.018), "in reasonable agreement with Planck, and in tension with earlier eBOSS analyses"; the amplitude is low, σ_8 = 0.733 (+0.026/−0.029) [src].
- Lyssa / lym1d (arXiv:2412.05372): slope n_Lyα = −2.369 ± 0.008 against Planck −2.363; amplitude low only through its degeneracy with the mean transmission, and "this tension disappears when imposing a well-motivated external prior on this mean transmission" [src].
- EFT (arXiv:2405.13208): σ_8 = 0.841 ± 0.017 with simulation-informed priors, "consistent with the standard cosmology" [src].
- Neutrino self-interactions: earlier eBOSS likelihoods combined with Planck preferred self-interaction; with the EFT or PRIYA likelihoods the preference disappears (arXiv:2503.15592) [src].

So four analyses of one data vector give a low slope (original), a normal slope with low amplitude (PRIYA), a normal slope with prior-dependent amplitude (Lyssa), and a normal amplitude (EFT). The disagreement is in the modelling (emulator, thermal and mean-flux priors, data cuts), not in the measurement.

**The new data.** DESI DR1 P1D gives Δ²_★ = 0.379 ± 0.032 and n_★ = −2.309 ± 0.019, and in combination with DESI BAO and Planck/ACT/SPT-3G a running α_s = 0.0014 ± 0.0041, with no preference for a non-zero value (arXiv:2601.21432) [src]. The authors close "by outlining the improvements needed to fully reach the level of confidence implied by these uncertainties" [src] — a caveat that belongs next to any quotation of these numbers.

**How the DESI paper itself reads the history** (arXiv:2601.21432, Sects. 6.2, 7.1 and 8) [src]. The DR1 result is "fully consistent" with Planck 2018 and consistent with all earlier Lyα analyses only at the 2σ level, "mostly because our n_★ uncertainties are significantly larger"; the slope error is 0.019 against 0.006 for eBOSS although DESI uses more spectra. The explanation offered: earlier analyses neglected emulator errors and used "simplified models for metal and HCD contamination … which can induce significant shifts in the inferred posteriors", and the metal and HCD models of the SDSS analyses "are strongly disfavored by DESI data". The paper also records a second external claim, by Fairbairn et al. (arXiv:2511.01612), of a 5σ tension between eBOSS P1D and the combined Planck + ACT + SPT data under ΛCDM, reduced to about 3σ with running [sec: as summarised in arXiv:2601.21432, Sect. 7.1]; the abstract of that paper states that eBOSS likelihoods with a suppression of small-scale power "can be accommodated by correlated variations of (α_s, β_s), leading to a preference for non-zero running", and proposes inflationary potentials with localised features [src].

**What is still open.**
- A like-for-like reanalysis of the eBOSS DR14 data vector with the DESI contaminant model and emulator-error treatment was not found this session; until it exists, the eBOSS-era tension claims rest on models that the DESI analysis argues were too simple.
- The DESI analysis fixes several things it lists as unvalidated or unmodelled: no informative IGM priors, an assumed LLS functional form strongly correlated with the cosmological parameters, no UV-fluctuation or patchy-reionisation terms, and an emulator whose error is comparable to the statistical error up to z = 2.8.
- The DESI DR1 n_★ = −2.309 ± 0.019 is less negative than the Planck-ΛCDM value quoted in the Lyssa paper for a similarly defined slope (−2.363) [src for both numbers]; the DESI paper warns that "minor differences may exist in the definition of the compressed parameters compared to other analyses", so the comparison must be made with one code.
- FFT and QMLE give forest-bias parameters that differ by 2.2σ in a simple model fit (arXiv:2505.07974) [src].
- Independent external analyses of the DESI DR1 compressed likelihood are starting to appear (N_eff < 3.41, arXiv:2609.22581) [src]; they inherit the two-parameter compression, which that paper validated to 0.15% for its sterile-neutrino model [src].

**What decides it.** DESI DR2 P1D with a second emulator on the same data; a joint 1D + 3D fit (ForestFlow already predicts 3D clustering from P1D and reproduces the DESI BAO-analysis clustering, arXiv:2607.27413 [src]); and the P3D / P× measurements, whose estimators exist (arXiv:1710.11036, arXiv:2503.15619, arXiv:2403.17294) and whose small-scale version was demonstrated on eBOSS (arXiv:2310.09116) [src].

## 2. How strong is the warm-dark-matter limit, really?
<!-- key: how-strong-is-the-warm-dark-matter-limit-really -->

- **Strong side.** m_WDM > 5.7 keV (95%) from HIRES + UVES at z = 4.2–5.0 with k_max = 0.2 s/km, marginalised over thermal history and inhomogeneous reionisation (arXiv:2309.04533) [src]; > 5.3 keV from earlier XQ-100 + HIRES/MIKE (arXiv:1702.01764) and from eBOSS + XQ-100 (arXiv:1911.09073) [src].
- **Cautious side.** > 3.1 keV with a weak preference for 4.5 keV from a 1080-simulation grid spanning photo-heating histories (arXiv:2209.14220) [src]; > 1.9 keV if cold reionisation histories are allowed, "demonstrating the level of systematic uncertainty of the Lyman-α forest method" (arXiv:1912.09397) [src]; the 5.3 keV limit of 2017 falls to 3.5 keV when temperature jumps are allowed (arXiv:1702.01764) [src]; the 5.7 keV limit falls to 4.1 keV when restricted to k_max < 0.1 s/km and earlier priors (arXiv:2309.04533) [src].
- **The physical degeneracy.** Free streaming, thermal Doppler broadening and pressure smoothing all suppress small-scale flux power. WDM suppression saturates at k ≳ 0.1 s/km because of peculiar-velocity smearing (arXiv:2209.14220) [src]. At z ≥ 5 the inferred temperatures are low, "leaving little room for additional smoothing … by free streaming of warm dark matter" (arXiv:1808.04367) [src].
- **New handle.** A first direct measurement of the pressure-smoothing scale from an acoustic feature in the small-scale P1D (λ_p ≈ 32 ± 8 ckpc at z = 4.6, arXiv:2607.19938) [src] constrains one of the degenerate quantities independently.
- **Limiting factor.** "Constraints on WDM models at high redshifts are limited by the availability of high-quality quasar spectra" (arXiv:2309.04533) [src].

A manuscript should quote a WDM limit together with its thermal-history assumption and k_max. The particle-physics interpretation (sterile-neutrino production mechanisms, mixed models) is shared with `cosmo-neutrinos-dark-matter`.

## 3. Fuzzy dark matter: which limit is current?
<!-- key: fuzzy-dark-matter-which-limit-is-current -->

Published lower limits on a pure FDM mass span a factor of ~100: 2 × 10⁻²¹ eV (20 × 10⁻²², arXiv:1703.04683), 2 × 10⁻²⁰ eV (arXiv:2007.12705), and in 2026 1.9 × 10⁻²¹ eV from P1D at z = 4.2–5.0 with a new emulator (arXiv:2606.06969) [src]. The 2026 result is ten times weaker than the 2021 one. Its authors attribute the difference to two choices: glass initial conditions for the gas in the 2021 work against offset dark-matter and gas grids in theirs, and a Gaussian-process emulator optimised for pure FDM in 2021 against their two-stage neural emulator built for the broader mixed-FDM space, "less optimized for the narrow PFDM posterior" (arXiv:2606.06969) [src: Sect. 4.1]. All three exclude the canonical 10⁻²² eV mass as all of the dark matter; mixed models with f_FDM ≲ 0.1 at 10⁻²²–10⁻²³ eV remain allowed (arXiv:2606.06969) [src].

## 4. Growth rate from the forest
<!-- key: growth-rate-from-the-forest -->

fσ8 cannot at present be measured from the 3D forest: the DESI DR1 value 0.37 (+0.055/−0.065) ± 0.033 was withheld from inference (arXiv:2509.15308) and DR2 mocks show a significant bias (arXiv:2607.27411) [src]. Routes being explored:
- field-level and EFT models that predict the full set of line-of-sight bias operators (arXiv:2309.10133, arXiv:2507.00284, arXiv:2606.26234) [src];
- simulation priors on b_η from P1D through ForestFlow, which constrain b_η f σ8 (arXiv:2607.27413) [src];
- the void–forest cross-correlation, where the quadrupole gave β = 1.21 ± 0.18 at z = 2.49 (arXiv:2203.11045) [src]; converting β to a growth rate needs the same b_η knowledge;
- cross-correlation with CMB lensing: the squeezed bispectrum between CMB lensing and P1D is detected at 4.8σ (arXiv:2405.14988), while direct lensing of the forest is not yet detected in DR1, A_L = 0.62 ± 0.33 (arXiv:2609.36949) [src].

## 5. BAO systematics at sub-percent precision
<!-- key: bao-systematics-at-sub-percent-precision -->

- **Non-linear shift.** The budget has already been revised once: 0.3% on each of α_∥, α_⊥ in the DR2 BAO paper, then 0.15% isotropic and 0.8% on the peak's AP in the DR2 full-shape paper (arXiv:2607.27410, Sect. 5.2) [src]. Two calculations give a few tenths of a percent with opposite radial sign: −0.2% radial, −0.3% transverse from EFT parameters fitted to ACCEL² (arXiv:2412.06892); +0.35% radial, ~0 transverse from AbacusSummit mocks through the DESI pipeline (arXiv:2503.13442) [src]. DESI DR2 carries a ~0.3% theory systematic for this (arXiv:2503.14739) [src]. With DR2 at 0.65% isotropic and future LBG surveys forecast at 0.4% (arXiv:2507.21852, **forecast**), the shift moves from negligible to a leading term.
- **UV background fluctuations.** A linear radiative-transfer model predicts a peak shift up to 1.2% for source bias 3 (arXiv:1402.0506) [src]; current analyses marginalise a UV term in the broadband (arXiv:2607.27411) [src]. No paper read this session reports a measured BAO shift from this effect.
- **Covariance.** Smoothed sub-sample covariance (baseline) versus unsmoothed covariance on compressed multipoles; the multipole analysis gives 0.93% isotropic precision against 0.65% for the baseline, with weaker nuisance constraints (arXiv:2603.04281, arXiv:2503.14739) [src].

## 6. Full-shape analyses: how far down in scale?
<!-- key: full-shape-analyses-how-far-down-in-scale -->

The AP gain comes from the broadband: a factor 2 (eBOSS, arXiv:2209.13942), 2.4 (DESI DR1, arXiv:2509.15308), 2 (DESI DR2, arXiv:2607.27410) over BAO alone [src]. The method debate is between
- the linear-theory-based model with empirical HCD, metal, UV and non-linear terms and a scale cut or small-scale marginalisation (the DESI baseline, validated on CoLoRe-2LPT and AbacusSummit mocks, arXiv:2607.27411) [src];
- one-loop EFT (arXiv:2309.10133, arXiv:2412.06892) and a hybrid EFT forward model (arXiv:2512.13681) [src];
- emulator-based models fed by hydrodynamical simulations (ForestFlow, arXiv:2409.05682) [src].

The field-level EFT paper states that linear-modulation models "fail at the field level even on quasi-linear scales" (arXiv:2606.26234) [src], while the DESI validation finds AP unbiased with the baseline model on hundreds of mocks (arXiv:2607.27411) [src]. These statements are compatible (a two-point AP fit can be unbiased where a field-level comparison fails) but the mocks themselves are built with approximations (2LPT, FGPA) close to the model being tested.

One concrete lesson of DR2: the scale cut alone does not protect a full-shape fit, because the continuum-fitting distortion leaks r_∥ < 10 h⁻¹Mpc correlations to all scales and biases AP at the percent level unless marginalised (arXiv:2607.27410, Sect. 3.3) [src]. Earlier full-shape results that relied on r_min only (eBOSS, DESI DR1) predate this treatment; whether they are affected at their precision (2% and 1.6%) was not assessed in the text read here.

Effect on cosmology worth tracking: the DR2 Lyα distances agree with the Planck ΛCDM prediction and sit about 2σ from the w0waCDM prediction of CMB + DESI BAO (arXiv:2607.27410, Sect. 5.3) [src] — the Lyα point pulls against the dynamical-dark-energy solution rather than with it. In numbers, the Lyα AP Ω_m = 0.325 ± 0.018 is 1.4σ above DESI BAO and nudges DESI toward the CMB (2.4σ → 2.2σ), slightly lowering the w0wa preference (arXiv:2607.27410) [src].

## 7. P3D and P×: from estimators to cosmology
<!-- key: p3d-and-px-from-estimators-to-cosmology -->

Estimators: cross-spectrum P×(k_∥, θ) (arXiv:1710.11036); weighted FFT estimators with a window matrix that forward-models masks and pixel weights, for P1D and extended to P× (arXiv:2505.02904); FFT-average small-scale P3D (arXiv:2310.09116); pair-count spectral estimator applied to eBOSS DR16 (arXiv:2403.08241); optimal estimator with window deconvolution and mode marginalisation, flat-sky so far (arXiv:2503.15619); MAP estimator (arXiv:2403.17294); unified HMC reconstruction of P3D from ξ, P1D and P× (arXiv:2506.08198) [src]. No DESI P3D or P× cosmological measurement was found in this session's searches. A forecast for the unified reconstruction gives the P3D monopole in 25 bins over 0.07–1.8 Mpc⁻¹ at 13% average precision for DESI-like data (**forecast**, arXiv:2506.08198) [src].

## 8. Thermal history and reionisation
<!-- key: thermal-history-and-reionisation -->

- T_0(z) from different statistics agrees on a peak near z ≈ 3 (arXiv:2009.00016) but the peak redshift and height differ between P1D-based (peak 14 000 K at z ~ 3.4, arXiv:1808.04367) and multi-statistic analyses (14 750 ± 1322 K at z ≈ 3) [src].
- Late end of hydrogen reionisation (z ≤ 5.3, arXiv:2108.03699) means relic temperature fluctuations at z = 4–5, exactly where WDM limits are derived (arXiv:2109.06897) [src].
- The forest alone gives τ_e = 0.040 (+0.042/−0.018) (95%) (arXiv:2510.00107) [src]. This is relevant to the CMB τ question raised by DESI-era fits, which belongs to `cosmo-cmb` and `cosmo-reionization-21cm`.
- JWST faint quasars as He II reionisation sources are constrained by the high-z P1D (arXiv:2609.16992) [src].

- Dynamical dark energy consistent with the DESI constraints would tilt the flux power spectrum and raise IGM temperatures in hydrodynamical simulations (arXiv:2601.00767) [src]; the DESI DR1 P1D paper judges its own posterior too broad to measure the dark-energy equation of state (arXiv:2601.21432, Sect. 7) [src].

## 9. Tomography: what cosmology can it deliver?
<!-- key: tomography-what-cosmology-can-it-deliver -->

- Deep-field tomography has become a galaxy-environment and protocluster tool (LATIS, arXiv:2510.08815, arXiv:2507.10949) more than a cosmological one [src].
- Discrepancies between tracers are unexplained: IGM-selected protocluster candidates without LBG overdensity in LATIS (arXiv:2507.10949) and a galaxy protocluster without forest absorption in CLAMATO (arXiv:2303.07619) [src].
- Wide-area tomography with quasars supports void statistics: void–forest RSD at 8σ in Stripe 82 (arXiv:2203.11045) [src]. DESI's quasar density and the WEAVE-QSO forecast (≈ 16 Mpc/h smoothing, critical-point clustering at up to 4σ, **forecast**, arXiv:2201.02606) [src] define the next step; no DESI tomographic map paper was found in this session's searches.
- LBG forests (first DESI measurement, arXiv:2507.21852) are the route to both dense tomography and high-z BAO in DESI-II and Stage-5 surveys [src].

## 10. Forecasts (all labelled)
<!-- key: forecasts-all-labelled -->

| Forecast | Value | Assumptions | Citation |
|---|---|---|---|
| LBG-forest BAO | 0.4% isotropic, 1.3% AP; 0.6% AP with full shape | 5000 deg², 1000 LBGs per deg², S/N as in the DESI pilot | arXiv:2507.21852 |
| P1D EFT compression | 10% on Δ²_p, 2.0% on n_p at k_p = 0.7 Mpc⁻¹ | DESI DR1 P1D, conservative per-bin EFT parameters | arXiv:2604.09407 |
| WDM from reionisation relics | m_WDM > 5.0 keV (DESI-like), 7.1 keV with SKA | relic model, DESI-like covariance | arXiv:2605.26518 |
| P1D precision | percent level with 5-year DESI in the absence of systematics | QMLE on synthetic spectra | arXiv:2008.06421 |
| Lyα BAO survey design | 1.4% on radial and transverse scales | 2000 deg², ~40 QSOs per deg², the 2007 design study | arXiv:astro-ph/0607122 |
| eBOSS full-shape AP | ~2% on D_M/D_H against 4% from BAO | eBOSS DR16 mocks | arXiv:2209.12931 |

The 2007 forecast is worth keeping in view: a 1.4% target has become a 0.65% measurement (arXiv:2503.14739) [src].

## 10b. What the next data decide
<!-- key: what-the-next-data-decide -->

| Question | Deciding measurement | Status of the tool |
|---|---|---|
| Is the P1D slope consistent with the CMB at the eBOSS-claimed precision? | DESI DR2 P1D with emulator errors reduced by a larger simulation suite, and a second emulator on the same data vector | emulator error is comparable to the statistical error up to z = 2.8 in DR1 (arXiv:2601.21432) |
| Can the thermal and mean-flux degeneracies be broken internally? | joint fit of survey P1D with high-resolution P1D | proposed, needs an emulator extended in k (arXiv:2601.21432); XQ-100 shown to constrain thermal nuisance parameters (arXiv:2509.18271) |
| Is the LLS contamination model adequate? | external priors on LLS abundance; halo-centred forward models | first simulation characterisation (arXiv:2609.19235); Voigt model tests (arXiv:2506.13005) |
| Sign and size of the BAO shift | EFT fits to data; larger hydrodynamical boxes | ACCEL² (640 h⁻¹Mpc) detects BAO but barely its damping (arXiv:2407.04473) |
| Can f be measured at z > 2? | field-level or EFT full-shape analyses validated on hydrodynamical mocks; forest × LBG cross-correlations in DESI-II | models exist (arXiv:2606.26234); the data-level fσ8 is biased on current mocks (arXiv:2607.27411) |
| Does the Lyα AP point keep pulling toward ΛCDM? | DESI DR3 full shape | DR2: agreement with Planck ΛCDM, ~2σ from the CMB + BAO w0waCDM prediction (arXiv:2607.27410) |
| How warm can dark matter be? | more high-S/N z > 4 spectra; direct pressure-smoothing measurements | sample-limited (arXiv:2309.04533); λ_p proof of concept (arXiv:2607.19938) |
| Are 3D small scales usable? | P× and P3D on DESI data | estimators ready (arXiv:1710.11036, arXiv:2505.02904, arXiv:2503.15619); no data measurement found |

## 11. Misconceptions and stale claims
<!-- key: misconceptions-and-stale-claims -->

| Claim still seen | Status | Correcting source |
|---|---|---|
| "Lyα BAO is in 2–2.5σ tension with Planck ΛCDM." | Stale. True for BOSS DR11/DR12 (arXiv:1404.1801, arXiv:1708.02225); 1.5σ at eBOSS DR16. | arXiv:2007.08995 |
| "The Lyα forest prefers negative running of the spectral index." | Stale as a general statement: it is the eBOSS-era result (α_s = −0.010 ± 0.004); DESI DR1 + CMB + BAO gives 0.0014 ± 0.0041. | arXiv:2601.21432 |
| "The forest measures σ_8 / the eBOSS forest shows a low σ_8." | Model dependent: 0.733 (PRIYA), 0.841 (EFT) from the same data; amplitude is degenerate with the mean transmission. | arXiv:2309.03943, arXiv:2405.13208, arXiv:2412.05372 |
| "The forest gives fσ8 at z = 2.3." | Not validated; excluded by DESI in DR1 and DR2. | arXiv:2509.15308, arXiv:2607.27411 |
| "The Lyα BAO has no systematic error budget." | Since DR2 a theory systematic (~0.3%) is included. | arXiv:2503.14739 |
| "Lyα gives m_WDM > 5.3 keV" quoted without conditions. | Depends on thermal-history priors (3.5 keV with temperature jumps; 1.9 keV for cold histories); the latest strong bound is 5.7 keV. | arXiv:1702.01764, arXiv:1912.09397, arXiv:2309.04533 |
| "The Lyα forest alone tightly constrains Σm_ν." | Alone it gives ~1 eV (1.1 eV, 0.8 eV); the power comes from combination with CMB. DESI DR1 P1D moves the CMB-SPA + DESI BAO limit only from 55.1 to 53.7 meV. | arXiv:1410.7244, arXiv:1702.03314, arXiv:2601.21432 |
| "The latest Lyα BAO is DESI DR1 (2% on H)." | Superseded by DR2 (1.1% radial, 0.65% isotropic) and by the DR2 full-shape AP (1%). | arXiv:2503.14739, arXiv:2607.27410 |
| "The forest has no bias parameters, unlike galaxies." | An argument of the 1998 inversion method (arXiv:astro-ph/9708018); 3D analyses fit b and β and P1D needs thermal and mean-flux nuisance parameters. | arXiv:1104.5244, arXiv:1506.04519 |
| "Lyα BAO needs quasars." | LBG forests give a consistent auto-correlation; C IV forest gives BAO at z = 1.92. | arXiv:2507.21852, arXiv:2601.08103 |

## 12. Internal tensions between analyses — quick list
<!-- key: internal-tensions-between-analyses-quick-list -->

- **Lyα bias from auto versus cross (DESI DR2).** b_α = −0.1488 ± 0.0020, β_α = 1.365 ± 0.032 from the auto-correlations alone; b_α = −0.099 ± 0.021, β_α = 1.98 ± 0.35 from the cross-correlations alone; combined −0.1352 ± 0.0073 and 1.445 ± 0.064 (arXiv:2503.14739, Appendix A) [src]. The paper treats these as nuisance parameters that are not expected to agree exactly.
- **Bias from P1D-level fits versus 3D fits.** The QMLE fit b_F(z) = −0.218 × ((1+z)/4)^2.96 gives −0.127 at z = 2.33 [der: (3.33/4)^2.96 = 0.581], against −0.135 to −0.149 from the 3D fits above. The P1D-level model is called "simplistic" by its authors, and FFT and QMLE differ by 2.2σ in it (arXiv:2505.07974) [src].
- **AP at z = 2.33.** D_M/D_H = 4.518 ± 0.095 (DR2 BAO), 4.525 ± 0.071 (DR1 full shape), 4.572 ± 0.046 (DR2 full shape), fiducial 4.548 [der: 39.1879/8.6172] (arXiv:2503.14739, arXiv:2509.15308, arXiv:2607.27410) [src]. All mutually consistent.
- **Lyα-only H_0 with a BBN prior, flat ΛCDM.** 63.2 ± 2.5 (eBOSS), 68.3 ± 1.6 (DESI DR1 full shape + DR2 BAO), 66.5 ± 1.3 (DESI DR2) (arXiv:2209.13942, arXiv:2509.15308, arXiv:2607.27410) [src].
- **Ω_m from Lyα AP alone.** 0.36 (+0.03/−0.04) (eBOSS) and 0.325 ± 0.018 (DESI DR2), both above the DESI BAO value (arXiv:2209.13942, arXiv:2607.27410) [src].
- **Compressed P1D parameters.** Slope errors of 0.006–0.007 (eBOSS analyses) against 0.019 (DESI DR1) for a larger sample: the difference is the treatment of contaminants and emulator error, not the data (arXiv:2601.21432) [src].
- **Thermal peak.** 14 000 K at z ~ 3.4 (arXiv:1808.04367) against 14 750 ± 1322 K at z ≈ 3 (arXiv:2009.00016) [src].
- **Dark-matter bounds.** WDM from 1.9 to 5.7 keV and FDM from 1.9 × 10⁻²¹ to 2 × 10⁻²⁰ eV depending on data, k_max and thermal priors (§§2–3).

## 13. Not verified
<!-- key: not-verified -->

- Closed 2026-10-14: the reason the 2026 FDM limit is weaker is now in §3 (authors' explanation, not an independent test).
- A like-for-like cosmological reanalysis of eBOSS DR14 with the DESI DR1 model.
- Any DESI DR2 P1D measurement or DESI P3D/P× measurement on data (none found by date-sorted search).
- Any DESI-based tomographic map publication (none found by search).
