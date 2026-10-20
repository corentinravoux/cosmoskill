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
  SPT-3G alone: **H₀ = 66.66 ± 0.60**.
- **CMB-SPA** = SPT + ACT + Planck combined: **H₀ = 67.19 ± 0.38**,
  σ₈ = 0.8137 ± 0.0037 in the current arXiv version; the first version read
  67.24 ± 0.35 *(2026-10-08)*. SPT-3G alone is quoted as 6.2σ from SH0ES. Relative to Planck alone the joint fit shrinks σ(ωb),
  σ(ωc), σ(θs) by 50%, 17%, 22%.
- Turning point worth stating in a review: ground-based CMB now matches Planck
  in constraining power and will drive parameters from here.
- ACT DR6: lensing at 43σ; DR6 extended-model constraints in arXiv:2503.14454.

## H₀
<!-- key: h0 -->

- SH0ES: **H₀ = 73.17 ± 0.86** (HST, four anchors, arXiv:2404.08038) and
  **73.18 ± 0.88** adding JWST Cepheids and TRGB calibrations
  (arXiv:2509.01667); community Distance Network baseline **73.50 ± 0.81**
  (arXiv:2510.23823) *(2026-10-08)*. Detail: `cosmo-distance-ladder-h0`.
- JWST rejects distance-dependent HST crowding as the explanation at **8.2σ**
  (>1000 Cepheids compared).
- **Significance depends on which local anchor is used.** Quoting a σ value
  without naming both endpoints is the most common error in tension prose.

## Dark energy
<!-- key: dark-energy -->

- DESI DR2 BAO + CMB + SN prefer evolving dark energy over ΛCDM; phantom in the
  past, quintessence-like today (Quintom-B).
- Robustness study across six parameterisations with CMB (ACT+SPT+Planck) +
  DESI DR2 + DESY5/Pantheon+/Union3 (arXiv:2511.22512): preference **robust to
  parameterisation and data combination**; up to **4.2σ** (BA model,
  CMB+DESI+DESY5, w₀ = −0.785 ± 0.047).
- As published with DESI DR2 the significance was strongly SN-sample
  dependent (2.8 / 3.8 / 4.2σ for Pantheon+ / Union3 / DESY5,
  arXiv:2503.14738). After the 2025–2026 recalibrations the spread has
  closed: 3.2 / 3.4 / 3.4σ for corrected Pantheon+ / Union3.1 / DES-Dovekie
  (arXiv:2601.19424), 3.3σ for the merged Unite sample with only weak
  Bayesian evidence (arXiv:2609.05053) *(2026-10-08)*. Always name the SN
  compilation and its version next to the σ. Detail: `cosmo-supernovae`.
- The evidence is **geometric** (BAO + SN + CMB). Weak lensing does not drive
  it — which is what makes the growth-side cross-check informative.

## BAO and full-shape clustering
<!-- key: bao-and-full-shape-clustering -->

- Latest DESI BAO: DR2 (arXiv:2503.14738); full shape: still DR1
  (arXiv:2411.12021); "DR1 FS + DR2 BAO" papers mix releases
  (arXiv:2602.18761).
- BAO measure D/r_d, not H₀. DR2 alone gives **Ω_m = 0.2975 ± 0.0086**;
  DR2 + BBN gives H₀ = 68.51 ± 0.58 (arXiv:2503.14738).
- DESI DR2 BAO versus CMB in ΛCDM: 2.3σ. The errors are
  statistics-dominated: systematics add at most 9% to the α_iso error
  (arXiv:2503.14738).
- The w₀wₐ preference is 1.7σ for DESI BAO alone, 3.1σ with CMB
  (arXiv:2503.14738). DESI clustering beyond BAO has not strengthened it:
  1.4σ for DR1 FS + DR2 BAO without CMB (arXiv:2602.18761); the bispectrum
  weakens it (arXiv:2606.23936).
- Live: full-shape posteriors in extended models are prior-dominated: best
  fit and posterior mean differ by up to 6.6σ in w₀wₐCDM (arXiv:2508.11811);
  ask for the MAP. σ₈ from full shape: BOSS EFT gave 0.69–0.73
  (arXiv:1909.05277, arXiv:2112.04515); DESI DR1 gives 0.842 ± 0.034
  (arXiv:2411.12022).
- DESI finished its planned survey in April 2026, full-survey results due
  2027; Euclid DR1 clustering products: mid-2027. Detail:
  `cosmo-galaxy-clustering`.

## Type Ia supernovae
<!-- key: type-ia-supernovae -->

- An unanchored SN Hubble diagram measures the shape of d_L(z) only; M and
  H₀ are degenerate (arXiv:2511.07517, arXiv:2609.05053).
- Current samples: **Unite** (2884 SNe, Pantheon+ ∪ DES, arXiv:2609.05053),
  **DES-Dovekie** (arXiv:2511.07517), **Union3.1** (arXiv:2601.19424).
  DES-SN5YR and Union3 are superseded; Pantheon+ (arXiv:2202.04077) stands
  with revised host masses. The compilations share most low-z supernovae;
  they are not independent.
- Flat-ΛCDM Ω_m from SNe alone: **0.310 (+0.012/−0.011)** Unite
  (arXiv:2609.05053), 0.330 ± 0.015 DES-Dovekie (arXiv:2511.07517),
  0.344 (+0.026/−0.025) Union3.1 (arXiv:2601.19424).
- The 2025–2026 shifts came from two fixes: Dovekie recalibration plus a
  colour-law implementation error in DES (arXiv:2511.07517), and
  inconsistent host masses between low and high redshift (arXiv:2601.19424,
  arXiv:2609.05321). Their effect on the dark-energy significance: section
  "Dark energy" above.
- Live: the low-z anchor controls the dark-energy result: cutting z < 0.1
  moves Unite by ~2σ, and no analysis yet uses a modern anchor; DEBASS, ZTF
  and TITAN are pending (arXiv:2508.10877). The residual mass step runs from
  0 to 0.17 mag depending on bias-correction dimensionality, scatter model,
  tracer and stretch linearity; its origin is disputed (arXiv:2004.10206 vs
  arXiv:2605.06799). Detail: `cosmo-supernovae`.

## Neutrino mass
<!-- key: neutrino-mass -->

- ΛCDM: **Σmν < 0.064 eV (95%)**, σ(Σmν) ≈ 0.020 eV (DESI DR2 + Planck).
- Feldman–Cousins limit 0.053 eV **breaches the oscillation floor**; with an
  effective parameter allowing negative densities the tension reaches ~3σ.
- But in w₀wₐCDM a joint DESI DR2 + CMB + DESY5 + DESY1 analysis finds
  **Σmν = 0.098 (+0.016/−0.037) eV, 2.7σ positive** (arXiv:2507.16589).
- Lesson for prose: the neutrino-mass bound is **model-dependent**, and quoting
  the ΛCDM number as "the" cosmological limit is misleading in a manuscript that
  also argues for dynamical dark energy.

## Growth, S₈, weak lensing
<!-- key: growth-s8-weak-lensing -->

- S₈ has moved up, but "converged" is too strong *(2026-10-08)*.
  KiDS-Legacy cosmic shear: 0.815 (+0.016/−0.021), 0.76σ from Planck in S8, 0.73σ in Σ8
  (arXiv:2503.19441). HSC Y3 with DESI clustering redshifts:
  0.804 (+0.019/−0.018), up from 0.769 (arXiv:2511.18134). DES Y6 3×2pt:
  0.789 ± 0.012, which is 1.8σ from the CMB in the full parameter space and
  2.6σ projected on S₈ (arXiv:2601.14559). Review: arXiv:2602.12238.
- The "S₈ tension" is reduced, not gone, and its size depends on the metric
  and on which CMB combination is the reference; treat pre-2025 statements
  about it as stale. Detail: `cosmo-weak-lensing`.
- DES Y3: cosmic shear S₈ = 0.759 (+0.025/−0.023) fiducial and
  0.772 (+0.018/−0.017) in the ΛCDM-optimised analysis (arXiv:2105.13543);
  3×2pt S₈ = 0.776 ± 0.017 (arXiv:2105.13549) *(2026-10-08)*.
- Shear ratios improve shear-only S₈ by up to 31%.

## Galaxy clusters
<!-- key: galaxy-clusters -->

- There is no single cluster S₈: **eRASS1 0.86 ± 0.01** from 5259 clusters
  (arXiv:2402.08458), DES Y3 0.864 ± 0.035 (arXiv:2503.13632), SPT
  0.795 ± 0.029 (arXiv:2401.02075), Planck + DES shear 0.791
  (arXiv:2509.02068), KiDS AMICO 0.74 ± 0.03 (arXiv:2507.14285).
- The best-constrained amplitude is not S₈: SPT has
  σ₈(Ω_m/0.3)^0.25 = 0.805 ± 0.016 (arXiv:2401.02075).
- The eRASS1 high S₈ and its growth index γ = 1.19 ± 0.21 are one feature of
  the data (arXiv:2410.09499); in that cosmology Planck would count 1098
  clusters, not 439 (arXiv:2509.08673).
- Live: mass calibration. (1 − b) depends on its reference: 0.89 against
  Chandra, 0.76 against XMM, same lensing (arXiv:2402.04006); matching the
  Planck CMB needs 0.61 ± 0.03 (arXiv:2403.19542). Planck clusters are now
  1.6σ from the CMB (arXiv:2509.02068). Richness selection biases stacked
  lensing high by 20–60% on large scales (arXiv:2203.05416, arXiv:2002.03867).
- No counts cosmology exists from ACT DR6 (10040 clusters, arXiv:2507.21459)
  or SPT-3G five-year data (7190 clusters, arXiv:2607.01175). Detail:
  `cosmo-clusters`.

## CMB × LSS cross-correlations
<!-- key: cmb-x-lss-cross-correlations -->

- CMB lensing × galaxies: unWISE × ACT DR6 + Planck gives
  **S₈ = 0.810 ± 0.015**, consistent with primary CMB, superseding
  0.784 ± 0.015 (arXiv:2309.05659, arXiv:2105.03421); DESI LRG × ACT DR6 +
  Planck PR4 gives 0.775 (+0.019/−0.022), 1.6–2.2σ low (arXiv:2407.04607).
- kSZ, DESI DR2 × ACT DR6: stacking at 18σ (arXiv:2604.19744), velocity
  reconstruction at 20.8σ (arXiv:2604.04867). kSZ measures τ × v; no kSZ fσ₈
  exists.
- Live: feedback strength is disputed. Strong: > 8σ from fiducial FLAMINGO
  (arXiv:2509.10455); 10 ± 2% suppression at k = 1 h/Mpc (arXiv:2512.02954).
  Weak: 6×2pt (arXiv:2510.25596).
- tSZ-based S₈ values disagree: 0.811 (+0.015/−0.012) (arXiv:2506.07432),
  0.72 ± 0.03 (arXiv:2605.11083).
- No DES Y6, Euclid or DESI DR2 × CMB-lensing cosmology was found (search of
  2026-10-09). Detail: `cosmo-cmb-lss-cross-correlations`.

## Inflation and primordial physics
<!-- key: inflation-and-primordial-physics -->

- n_s (ΛCDM): 0.9649 ± 0.0042 (Planck 2018, arXiv:1807.06211),
  0.9679 ± 0.0033 (CMB-SPA, arXiv:2506.20707), **0.974 ± 0.003** (P-ACT-LB,
  with DESI BAO; arXiv:2503.14452).
- Live: 0.974 partly reflects the CMB–BAO tension (arXiv:2507.12459): with
  Ω_K or w₀wₐ free, n_s is 0.967–0.972 (arXiv:2607.28445). Starobinsky sits
  at the 2σ edge of P-ACT-LB + BK18 for N = 50–60, in ΛCDM
  (arXiv:2503.14454).
- r_0.05 < 0.036 at 95% (BK18, arXiv:2110.00483) remains the tightest.
  Forecasts: SO σ(r) = 1.2 (1.4) × 10⁻³ with 70% (50%) delensing
  (arXiv:2512.15833); LiteBIRD δr < 0.002 (arXiv:2607.25285).
- f_NL: CMB local −0.9 ± 5.1 (Planck 2018, arXiv:1905.05697), −0.1 ± 5.0 in
  PR4 (arXiv:2504.00884). Galaxy surveys measure f_NL·b_φ: DESI DR1 −3.6 ± 9
  (quasar p = 1.6) or +3.5 (p = 1) (arXiv:2411.17623).
- Ω_K: DESI DR2 + CMB gives +0.0023 ± 0.0011 (arXiv:2503.14738); the
  Planck-alone closed value is the A_L feature (arXiv:1807.06209).
  Birefringence: 0.277° ± 0.057° jointly, 4.8σ, no detection claimed
  (arXiv:2608.06480). Detail: `cosmo-inflation-primordial`.

## Reionisation and 21 cm
<!-- key: reionisation-and-21-cm -->

- τ from Planck low-ℓ polarisation: 0.051–0.063, σ ≈ 0.005–0.009
  (arXiv:1807.06209, arXiv:1908.09856, arXiv:2103.14378). The value
  0.090 ± 0.012 is CMB + DESI without low-ℓ EE, not a measurement
  (arXiv:2504.16932); reionisation probes in place of low-ℓ EE give
  τ = 0.067 ± 0.011 (arXiv:2607.26373).
- Reionisation ends late: dark gaps persist to z ≃ 5.3 (arXiv:2109.06295);
  x_HI = 0.19 ± 0.07 at z = 5.6 (arXiv:2405.12273). Its duration from the
  kSZ: SPT-3G D1 Δz(25–75%) < 3.8 (arXiv:2601.20551).
- No 21 cm power spectrum is detected at z > 6. Deepest limit: HERA Phase I
  **Δ² ≤ 457 mK²** at 95% confidence (z = 7.9, k = 0.34 h/Mpc;
  arXiv:2210.04912).
- Live: EDGES (78 MHz, 0.5 K; arXiv:1810.05912) is unconfirmed; SARAS 3
  rejects its profile at 95.3% (arXiv:2112.06778). HI intensity mapping has
  auto-spectra (CHIME, 12.5σ at z ~ 1; arXiv:2511.19620) but no BAO.
- JWST: ΛCDM models fit luminosity functions to z = 14 (arXiv:2604.18683).
  Detail: `cosmo-reionization-21cm`.

## Peculiar velocities
<!-- key: peculiar-velocities -->

- DESI DR1 PV consensus: fσ₈(z = 0.07) = 0.4497 ± 0.0548, from three
  estimators (0.391, 0.440, 0.483) (arXiv:2512.03228, arXiv:2512.03230).
- CF4 bulk flow: 387 ± 28 km/s at 150 h⁻¹Mpc (arXiv:2302.02028); with mock
  errors the probability is 0.11% (arXiv:2306.11269). Detail:
  `cosmo-peculiar-velocities`.

## Lyman-α forest
<!-- key: lyman-alpha-forest -->

- DESI DR2 Lyα BAO at **0.65%** (arXiv:2503.14739); AP from the full shape at
  **1%** at z_eff = 2.33, twice as tight as BAO from the same data, giving
  D_H/r_d = 8.600 ± 0.066 and D_M/r_d = 39.32 ± 0.33 (arXiv:2607.27410).
  P1D, IGM and forest limits on dark matter: `cosmo-lyman-alpha`.

## Isotropy
<!-- key: isotropy -->

- CatWISE quasar number-count dipole: amplitude **2.7×** the kinematic
  expectation, 4.9–5.7σ (arXiv:2212.07733). Contested on ecliptic-latitude
  selection grounds (arXiv:2511.00822).

## Facility timeline (verified 2026-08)
<!-- key: facility-timeline-verified-2026-08 -->

| Facility | Status |
|---|---|
| **CMB-S4** | **cancelled** — DOE and NSF withdrew support 9 July 2025 |
| Simons Observatory | commissioning / early observing |
| LiteBIRD | JAXA L-class; reformed after the 2024 Mission Definition Review to a single telescope with 12 bands, δr < 0.002 (arXiv:2607.25285) *(2026-10-08)*; launch under revision JFY2032 → JFY2036 |
| Rubin LSST | survey began **30 June 2026** |
| Roman | launch **30 Aug 2026**, science ops early 2027 |
| Euclid | Q1 (March 2025) released; DR1-Foundation planned 12 Nov 2026; full DR1 with clustering and lensing products mid-2027 |
| 4MOST | first light **18 Oct 2025** (ESO announcement of 22 Oct 2025) |
| Subaru PFS | first light **22 Mar 2025**, SSP under way |
| SPHEREx | launched **11 Mar 2025**, first all-sky map Dec 2025 |
| DESI | DR2 released 2025; DR3 BAO expected 2027 |
| MUST | 6.5 m Stage-V, Lenghu; completion ~2029–30, survey in the 2030s |
