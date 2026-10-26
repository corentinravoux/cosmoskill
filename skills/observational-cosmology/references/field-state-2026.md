# Field state — observational cosmology, mid-2026

Cross-domain digest. First written **2026-08-06**; lines marked *(2026-10-08)*
were corrected or added on that date from the sources named. Rebalanced
**2026-10-20** to the field's weights: the sections on BAO and full shape,
supernovae, clusters, CMB × LSS, inflation and reionisation were added from
the `SKILL.md` and `references/` of their domain skills, and the
peculiar-velocity and Lyman-α sections cut to pointers. **The `cosmo-*`
skills supersede this file for their domain**: each holds dated tables with
provenance flags, and where this digest and a `cosmo-*/references/results.md`
differ, the sub-skill is right. **Verify before citing**: every number here
should be re-checked against arXiv/ADS before it enters a manuscript. Numbers
without a source below were not verified and must not be quoted.

## CMB
<!-- key: cmb -->

- **SPT-3G D1** (Camphuis et al., arXiv:2506.20707): TT/TE/EE from 4% of sky,
  deepest maps used in a CMB TT/TE/EE analysis; most precise lensed EE
  (ℓ = 1800–4000) and TE (ℓ = 2200–4000) to date.
  SPT-3G alone: **H₀ = 66.66 ± 0.60**. [src: abstract]
- **CMB-SPA** = SPT + ACT + Planck combined: **H₀ = 67.19 ± 0.38**,
  σ₈ = 0.8137 ± 0.0037 in the current arXiv version (arXiv:2506.20707)
  [src: abstract] *(2026-10-08)*. SPT-3G alone is quoted as 6.2σ from SH0ES
  (arXiv:2506.20707) [src: abstract].
- Turning point worth stating in a review: ground-based CMB now matches Planck
  in constraining power and will drive parameters from here.
- ACT DR6: lensing at 43σ (Qu et al. 2023, arXiv:2304.05202) [src: abstract];
  DR6 extended-model constraints in arXiv:2503.14454.

## H₀
<!-- key: h0 -->

- SH0ES: **H₀ = 73.17 ± 0.86** (HST, four anchors, arXiv:2404.08038)
  [src: abstract] and **73.18 ± 0.88** adding JWST Cepheids and TRGB
  calibrations (arXiv:2509.01667) [src: abstract]; community Distance Network
  baseline **73.50 ± 0.81** (arXiv:2510.23823) [src: abstract] *(2026-10-08)*. Detail: `cosmo-distance-ladder-h0`.
- JWST rejects distance-dependent HST crowding as the explanation at **8.2σ**
  (>1000 Cepheids compared; Riess et al. 2024, arXiv:2401.04773)
  [src: abstract].
- **Significance depends on which local anchor is used.** Quoting a σ value
  without naming both endpoints is the most common error in tension prose.

## Dark energy
<!-- key: dark-energy -->

- DESI DR2 BAO + CMB + SN prefer evolving dark energy over ΛCDM; phantom in the
  past, quintessence-like today (Quintom-B).
- Robustness study across six parameterisations with CMB (ACT+SPT+Planck) +
  DESI DR2 + DESY5/Pantheon+/Union3 (arXiv:2511.22512, abstract): preference **robust to
  parameterisation and data combination**; up to **4.2σ** (BA model,
  CMB+DESI+DESY5, w₀ = −0.785 ± 0.047).
- As published with DESI DR2 the significance was strongly SN-sample
  dependent (2.8 / 3.8 / 4.2σ for Pantheon+ / Union3 / DESY5,
  arXiv:2503.14738) [src: Sect. VII.1]. After the 2025–2026 recalibrations the
  spread has closed: 3.2 / 3.4 / 3.4σ for corrected Pantheon+ / Union3.1 /
  DES-Dovekie (arXiv:2601.19424) [src: abstract], 3.3σ (MAP) for the merged
  Unite sample with only weak Bayesian evidence (arXiv:2609.05053)
  [src: abstract] *(2026-10-08)*. Always name the SN
  compilation and its version next to the σ. Detail: `cosmo-supernovae`.
- The evidence is **geometric** (BAO + SN + CMB). Weak lensing does not drive
  it — which is what makes the growth-side cross-check informative.

## BAO and full-shape clustering
<!-- key: bao-and-full-shape-clustering -->

- Latest DESI BAO: DR2 (arXiv:2503.14738); full shape: still DR1
  (arXiv:2411.12021); "DR1 FS + DR2 BAO" papers mix releases
  (arXiv:2602.18761).
- BAO measure D/r_d, not H₀. DR2 alone gives **Ω_m = 0.2975 ± 0.0086**
  [src: Sect. VI, Eq. 17]; DR2 + BBN gives H₀ = 68.51 ± 0.58
  [src: Sect. VI, Eq. 19] (arXiv:2503.14738).
- DESI DR2 BAO versus CMB in ΛCDM: 2.3σ (arXiv:2503.14738) [src: abstract].
  The errors are statistics-dominated: the systematic error raises the total
  α_iso error budget by between 1% (BGS) and 9% (LRG3 + ELG1)
  (arXiv:2503.14738) [src: Sect. III.1].
- The w₀wₐ preference is 1.7σ for DESI BAO alone [src: Sect. VII.1], 3.1σ
  with CMB [src: abstract] (arXiv:2503.14738). DESI clustering beyond BAO has
  not strengthened it: DR1 FS + DR2 BAO reduce the discrepancy with ΛCDM to
  1.4σ, compared with BAO-only analyses (arXiv:2602.18761) [src: abstract];
  the bispectrum weakens it (arXiv:2606.23936).
- Live: full-shape posteriors in extended models are prior-dominated: best
  fit and posterior mean differ by up to 6.6σ in w₀wₐCDM (arXiv:2508.11811)
  [src: abstract]; ask for the MAP. σ₈ from full shape: BOSS EFT gave
  0.721 ± 0.043 (arXiv:1909.05277) [src: abstract] and 0.692 (+0.035/−0.041)
  with P + B₀, n_s free and a BBN prior (arXiv:2112.04515) [src: abstract];
  DESI DR1 gives 0.842 ± 0.034 (arXiv:2411.12022) [src: abstract].
- DESI finished its planned survey in April 2026, full-survey results due
  2027; Euclid DR1 clustering products: mid-2027. Detail:
  `cosmo-galaxy-clustering`.

## Type Ia supernovae
<!-- key: type-ia-supernovae -->

- An unanchored SN Hubble diagram measures the shape of d_L(z) only; M and
  H₀ are degenerate (arXiv:2511.07517, arXiv:2609.05053).
- Current samples: **Unite** (2884 SNe, Pantheon+ ∪ DES, arXiv:2609.05053)
  [src: abstract],
  **DES-Dovekie** (arXiv:2511.07517), **Union3.1** (arXiv:2601.19424).
  DES-SN5YR and Union3 are superseded; Pantheon+ (arXiv:2202.04077) stands
  with revised host masses. The compilations share most low-z supernovae;
  they are not independent.
- Flat-ΛCDM Ω_m from SNe alone: **0.310 (+0.012/−0.011)** Unite
  (arXiv:2609.05053), 0.330 ± 0.015 DES-Dovekie (arXiv:2511.07517),
  0.344 (+0.026/−0.025) Union3.1 (arXiv:2601.19424) [src: abstract of each].
- The 2025–2026 shifts came from two fixes: Dovekie recalibration plus a
  colour-law implementation error in DES (arXiv:2511.07517), and
  inconsistent host masses between low and high redshift (arXiv:2601.19424,
  arXiv:2609.05321). Their effect on the dark-energy significance: section
  "Dark energy" above.
- Live: the low-z anchor controls the dark-energy result: cutting the
  z < 0.1 SNe (687, 24% of the sample) is the only cut that shifts the Unite
  best fit substantially, by ~2σ (arXiv:2609.05053) [src: Sect. 9.1], and no
  analysis yet uses a modern anchor; DEBASS, ZTF and TITAN are pending
  (arXiv:2508.10877). The residual mass step depends on bias-correction
  dimensionality, scatter model, tracer and stretch linearity:
  0.040 ± 0.019 mag (5D) or 0.066 ± 0.020 mag (1D bias correction) on the same
  DES SNe (arXiv:2001.11294) [src: abstract]; above 0.12 mag for every tracer
  and ~0.17 ± 0.01 mag with non-linear stretch in ZTF DR2 (arXiv:2405.20965)
  [src: abstract]; consistent with zero for unreddened SNe with two
  populations in Union3.1 (arXiv:2601.19854) [src: abstract]. Its origin is
  disputed (arXiv:2004.10206 vs arXiv:2605.06799). Detail: `cosmo-supernovae`.

## Neutrino mass
<!-- key: neutrino-mass -->

- ΛCDM: **Σmν < 0.064 eV (95%)** (DESI DR2 + CMB, arXiv:2503.14738)
  [src: abstract]; marginalised error σ(Σmν) = 0.020 eV (DESI DR2 + Planck and
  ACT, Elbers et al. 2025, arXiv:2503.14744) [src: abstract].
- Feldman–Cousins 95% limit 0.053 eV **breaches the oscillation floor**; with
  an effective parameter allowing negative densities the tension with the
  oscillation limit is 3σ (arXiv:2503.14744) [src: abstract].
- But in w₀wₐCDM a joint DESI DR2 + CMB + DESY5 + DESY1 analysis finds
  **Σmν = 0.098 (+0.016/−0.037) eV, 2.7σ positive** (arXiv:2507.16589, abstract).
- Lesson for prose: the neutrino-mass bound is **model-dependent**, and quoting
  the ΛCDM number as "the" cosmological limit is misleading in a manuscript that
  also argues for dynamical dark energy.

## Growth, S₈, weak lensing
<!-- key: growth-s8-weak-lensing -->

- S₈ has moved up, but "converged" is too strong *(2026-10-08)*.
  KiDS-Legacy cosmic shear: 0.815 (+0.016/−0.021), 0.76σ from Planck in S8,
  0.73σ in Σ8 (arXiv:2503.19441) [src: Sect. 7]. HSC Y3 with DESI clustering
  redshifts: 0.804 (+0.019/−0.018), up from 0.769 (arXiv:2511.18134)
  [src: abstract]. DES Y6 3×2pt: 0.789 ± 0.012, which is 1.8σ from the CMB in
  the full parameter space and 2.6σ projected on S₈ (arXiv:2601.14559)
  [src: abstract]. Review: arXiv:2602.12238.
- The "S₈ tension" is reduced, not gone, and its size depends on the metric
  and on which CMB combination is the reference; treat pre-2025 statements
  about it as stale. Detail: `cosmo-weak-lensing`.
- DES Y3: cosmic shear S₈ = 0.759 (+0.025/−0.023) fiducial and
  0.772 (+0.018/−0.017) in the ΛCDM-optimised analysis (arXiv:2105.13543);
  3×2pt S₈ = 0.776 ± 0.017 (arXiv:2105.13549) [src: abstract of each]
  *(2026-10-08)*.
- Shear ratios improve the DES Y3 cosmic-shear S₈ constraint by up to 31%
  (Sánchez et al., arXiv:2105.13542) [src: abstract].

## Galaxy clusters
<!-- key: galaxy-clusters -->

- There is no single cluster S₈: **eRASS1 0.86 ± 0.01** from 5259 clusters
  (arXiv:2402.08458), DES Y3 0.864 ± 0.035 (arXiv:2503.13632), SPT
  0.795 ± 0.029 (arXiv:2401.02075), Planck + DES shear 0.791 (+0.023/−0.021)
  (arXiv:2509.02068), KiDS AMICO 0.74 ± 0.03 (arXiv:2507.14285)
  [src: abstract of each].
- The best-constrained amplitude is not S₈: SPT has
  σ₈(Ω_m/0.3)^0.25 = 0.805 ± 0.016 (arXiv:2401.02075, abstract).
- The eRASS1 high S₈ and its growth index γ = 1.19 ± 0.21 are one feature of
  the data (arXiv:2410.09499); in that cosmology Planck would count 1098
  clusters, not 439 (arXiv:2509.08673) [src: abstract of each].
- Live: mass calibration. (1 − b) depends on its reference: 0.89 ± 0.04
  against Chandra, 0.76 ± 0.04 against XMM, same lensing (arXiv:2402.04006);
  matching the Planck CMB needs 0.61 ± 0.03 (arXiv:2403.19542). Planck
  clusters are now 1.6σ from the CMB (arXiv:2509.02068). Richness selection
  biases stacked lensing ΔΣ high by approximately 20 to 60 percent on large
  scales (arXiv:2203.05416) [src: abstract of each]; projection effects in
  simulations: arXiv:2002.03867.
- No counts cosmology exists from ACT DR6 (10040 clusters, arXiv:2507.21459)
  or SPT-3G five-year data (7190 confirmed clusters, arXiv:2607.01175)
  [src: abstract of each]. Detail:
  `cosmo-clusters`.

## CMB × LSS cross-correlations
<!-- key: cmb-x-lss-cross-correlations -->

- CMB lensing × galaxies: unWISE × ACT DR6 + Planck gives
  **S₈ = 0.810 ± 0.015**, consistent with primary CMB, superseding
  0.784 ± 0.015 (arXiv:2309.05659, arXiv:2105.03421); DESI LRG × ACT DR6 +
  Planck PR4 gives 0.775 (+0.019/−0.022), consistent with Planck primary CMB
  "at the ≃ 1.6–2.2σ level" (arXiv:2407.04607) [src: abstract of each].
- kSZ, DESI DR2 × ACT DR6: stacking at 18σ (arXiv:2604.19744), velocity
  reconstruction at 20.8σ (arXiv:2604.04867) [src: abstract of each]. kSZ
  measures τ × v; no kSZ fσ₈ exists.
- Live: feedback strength is disputed. Strong: kSZ measurements combined
  > 8σ from fiducial FLAMINGO (arXiv:2509.10455); 10 ± 2% suppression at
  k = 1 h/Mpc (arXiv:2512.02954) [src: abstract of each].
  Weak: 6×2pt (arXiv:2510.25596).
- tSZ-based S₈ values disagree: 0.811 (+0.015/−0.012) (arXiv:2506.07432),
  0.72 ± 0.03 (arXiv:2605.11083) [src: abstract of each].
- No DES Y6, Euclid or DESI DR2 × CMB-lensing cosmology was found (search of
  2026-10-09). Detail: `cosmo-cmb-lss-cross-correlations`.

## Inflation and primordial physics
<!-- key: inflation-and-primordial-physics -->

- n_s (ΛCDM): 0.9649 ± 0.0042 (Planck 2018, arXiv:1807.06211)
  [src: abstract], 0.9679 ± 0.0033 (CMB-SPA, arXiv:2506.20707)
  [src: Sect. II], **0.974 ± 0.003** (P-ACT-LB, with DESI BAO;
  arXiv:2503.14452) [src: abstract].
- Live: 0.974 partly reflects the CMB–BAO tension (arXiv:2507.12459). With a
  small negative curvature n_s = 0.9667 ± 0.0041 (Planck + DESI) or
  0.9692 ± 0.0035 (adding ACT and SPT); with w₀wₐ free 0.9716 ± 0.0032
  (arXiv:2607.28445) [src: abstract]. P-ACT-LB disfavours Starobinsky R² at
  ≳ 2σ for 50 < N < 60, in ΛCDM with BK18 (arXiv:2503.14454)
  [src: Sect. IV.4].
- r_0.05 < 0.036 at 95% (BK18, arXiv:2110.00483) [src: abstract] remains
  the tightest. Forecasts: SO σ(r) = 1.2 × 10⁻³ with 70% delensing
  [src: abstract], σ_r = 0.0014 after ten years in the most conservative case
  (pessimistic 1/f noise, 50% delensing, foreground decorrelation)
  [src: Sect. 3.2] (arXiv:2512.15833); LiteBIRD δr < 0.002 (68%)
  (arXiv:2607.25285) [src: abstract].
- f_NL: CMB local −0.9 ± 5.1 (Planck 2018, arXiv:1905.05697), −0.1 ± 5.0 in
  PR4 (arXiv:2504.00884) [src: abstract of each]. Galaxy surveys measure
  f_NL·b_φ: DESI DR1 −3.6 (+9.0/−9.1) with a recent-merger model for the
  quasar response, 3.5 (+10.7/−7.4) with the universality relation
  (arXiv:2411.17623) [src: abstract].
- Ω_K: DESI DR2 + CMB gives 10³Ω_K = 2.3 ± 1.1 (arXiv:2503.14738)
  [src: Sect. VI, table]; the Planck-alone closed value is the A_L feature
  (arXiv:1807.06209). Birefringence: 0.277° ± 0.057° jointly, 4.8σ, no
  detection claimed (arXiv:2608.06480) [src: abstract]. Detail: `cosmo-inflation-primordial`.

## Reionisation and 21 cm
<!-- key: reionisation-and-21-cm -->

- τ with Planck low-ℓ polarisation: 0.054 ± 0.007 (Planck 2018 combined,
  arXiv:1807.06209); 0.0566 (+0.0053/−0.0062) from large-scale polarisation
  alone with improved HFI maps (arXiv:1908.09856); 0.0627 (+0.0050/−0.0058)
  from SRoll2 low-ℓ TTTEEE with CamSpec high-ℓ (arXiv:2103.14378)
  [src: abstract of each]. The value 0.090 ± 0.012 is DESI BAO + high-ℓ CMB +
  CMB lensing without low-ℓ EE, not a measurement (arXiv:2504.16932);
  reionisation probes in place of low-ℓ EE give τ = 0.067 ± 0.011 with
  dynamical dark energy (arXiv:2607.26373) [src: abstract of each].
- Reionisation ends late: dark gaps persist to z ≃ 5.3 (arXiv:2109.06295);
  x_HI = 0.19 ± 0.07 at z = 5.6 (arXiv:2405.12273). Its duration from the
  kSZ: SPT-3G D1 Δz(25–75%) < 3.8 with a semi-analytic model
  (arXiv:2601.20551) [src: abstract of each].
- No 21 cm power spectrum is detected at z > 6. Deepest limit: HERA Phase I
  **Δ² ≤ 457 mK²** at 95% confidence (z = 7.9, k = 0.34 h/Mpc;
  arXiv:2210.04912). [src: abstract]
- Live: EDGES (78 MHz, 0.5 K; arXiv:1810.05912) is unconfirmed; SARAS 3
  rejects its profile at 95.3% (arXiv:2112.06778). HI intensity mapping has
  auto-spectra (CHIME, 12.5σ at z ~ 1; arXiv:2511.19620) but no BAO
  [src: abstract of each].
- JWST: a ΛCDM model reproduces the UV luminosity functions at 7 ≤ z ≤ 14
  (arXiv:2604.18683) [src: abstract].
  Detail: `cosmo-reionization-21cm`.

## Peculiar velocities
<!-- key: peculiar-velocities -->

- DESI DR1 PV consensus: fσ₈(z = 0.07) = 0.4497 ± 0.0548 (arXiv:2512.03230),
  from three estimators: 0.391 (+0.080/−0.081) from correlation functions
  (arXiv:2512.03230), 0.440 (+0.080/−0.096) from the power spectrum
  (arXiv:2512.03231), 0.483 (+0.080/−0.043) (stat) ± 0.018 (sys) from
  maximum-likelihood fields (arXiv:2512.03229) [src: abstract of each].
- CF4 bulk flow: 387 ± 28 km/s at 150 h⁻¹Mpc (arXiv:2302.02028)
  [src: Sect. 7, table; abstract for the radius]; with mock errors, 0.11%
  probability of a larger χ² at a depth of 173 h⁻¹Mpc (arXiv:2306.11269)
  [src: abstract]. Detail:
  `cosmo-peculiar-velocities`.

## Lyman-α forest
<!-- key: lyman-alpha-forest -->

- DESI DR2 Lyα BAO at **0.65%** isotropic (arXiv:2503.14739); AP from the
  full shape at **1%** at z_eff = 2.33, twice as tight as BAO from the same
  data; combining AP and BAO gives D_H/r_d = 8.600 ± 0.066 and
  D_M/r_d = 39.32 ± 0.33 (arXiv:2607.27410) [src: abstract of each].
  P1D, IGM and forest limits on dark matter: `cosmo-lyman-alpha`.

## Isotropy
<!-- key: isotropy -->

- CatWISE quasar number-count dipole: amplitude **2.7×** the kinematic
  expectation at 5.7σ (arXiv:2212.07733); the earlier analysis found it over
  twice as large at 4.9σ (arXiv:2009.14826) [src: abstract of each]. Contested
  on ecliptic-latitude selection grounds (arXiv:2511.00822).

## Facility timeline (verified 2026-08)
<!-- key: facility-timeline-verified-2026-08 -->

| Facility | Status |
|---|---|
| **CMB-S4** | **cancelled** — DOE and NSF withdrew support 9 July 2025 |
| Simons Observatory | commissioning / early observing |
| LiteBIRD | JAXA L-class; reformed after the 2024 Mission Definition Review to a single telescope with 12 bands, δr < 0.002 (arXiv:2607.25285) [src: abstract] *(2026-10-08)*; launch under revision JFY2032 → JFY2036 (ISAS/JAXA page, via `cosmo-surveys-facilities`) |
| Rubin LSST | survey began **29 June 2026** (Rubin survey-strategy progress page [doc: https://survey-strategy.lsst.io/progress/index.html, 2026-10-26]; Rubin release of 30 June 2026 [doc: https://rubinobservatory.org/news/action-rubin-lsst-begins, 2026-10-26]) |
| Roman | launch **30 Aug 2026** (NASA release [doc: https://www.nasa.gov/news-release/nasas-dark-universe-seeking-nancy-grace-roman-space-telescope-launches/, 2026-10-26]), first images expected by early 2027 |
| Euclid | Q1 (March 2025) and Q2 released; DR1-Foundation planned 12 Nov 2026, dates "tentative"; full DR1 with clustering and lensing products mid-2027 (ESA Euclid timeline [doc: https://www.cosmos.esa.int/web/euclid/timeline, 2026-10-26]) |
| 4MOST | first light **18 Oct 2025** (ESO announcement [doc: https://www.eso.org/sci/publications/announcements/sciann17735.html, 2026-10-26]) |
| Subaru PFS | SSP under way; first-light date not verified |
| SPHEREx | launched **11 Mar 2025** (arXiv:2511.02985) [src: abstract], first all-sky map Dec 2025 |
| DESI | DR2 released 2025; DR3 BAO expected 2027 |
| MUST | 6.5 m Stage-V, Lenghu; eight-year survey in the 2030s (arXiv:2605.10102) [src: abstract] |
