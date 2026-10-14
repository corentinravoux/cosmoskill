# Field state — observational cosmology, mid-2026

Cross-domain digest. First written **2026-08-06**; lines marked *(2026-10-08)*
were corrected or added on that date from the sources named. **The `cosmo-*`
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
  KiDS-Legacy cosmic shear: 0.815 (+0.016/−0.021), 0.73σ from Planck
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
- Clusters: eROSITA eRASS1, 5259 clusters, S₈ = 0.86 ± 0.01; SPT 0.795 ± 0.029.

## Peculiar velocities
<!-- key: peculiar-velocities -->

- DESI DR1 PV field-level: **fσ₈ = 0.483 (+0.080/−0.043) stat ± 0.018 sys**,
  BGS + FP + TF, 415 523 redshifts, 76 616 PVs (arXiv:2512.03229); consistent
  with the P(k) and ξ(r) analyses of the same data.
- Method trend: field-level / likelihood-based inference is displacing
  compressed two-point statistics.
- **Bulk flow is contested.** Watkins et al. 2023 (arXiv:2302.02028) report
  4.81σ excess at 200 h⁻¹Mpc from CF4; the result is estimator-dependent, see
  *Evaluating bulk flow estimators for CF4* (arXiv:2306.11269). Do not cite the
  excess as established.

## Lyman-α forest
<!-- key: lyman-alpha-forest -->

- DESI DR2 Lyα BAO at **0.65%** (arXiv:2503.14739); AP from the full shape at
  **1%** at z_eff = 2.33, twice as tight as BAO from the same data, giving
  D_H/r_d = 8.600 ± 0.066 and D_M/r_d = 39.32 ± 0.33 (arXiv:2607.27410).
- DESI DR1 P1D cosmology: Δ²★ = 0.379 ± 0.032, n★ = −2.309 ± 0.019 at
  0.009 s/km, z = 3; no running, α_s = 0.0014 ± 0.0041 with CMB and BAO
  (arXiv:2601.21432) *(2026-10-08)*. Detail: `cosmo-lyman-alpha`.
- DR1 P1D measured with both FFT and optimal/quadratic estimators, with a
  dedicated estimator-validation paper; cross-estimator agreement is now
  standard practice.
- ACCEL² supplies the large-volume hydrodynamical calibration.

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
