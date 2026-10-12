---
name: cosmo-clusters
description: Use when reviewing, planning or fact-checking galaxy-cluster cosmology — cluster counts, halo mass function, mass calibration (weak lensing, hydrostatic bias, CMB lensing), 1−b, richness–mass relation, projection effects, selection functions, cluster clustering, gas-mass fraction, splashback radius, cluster S8; eROSITA eRASS1, SPT, ACT, Planck SZ, DES redMaPPer, KiDS AMICO, HSC, XXL, Euclid Q1 clusters.
---

# Galaxy-cluster cosmology — expert reference

Snapshot 2026-10-07. Numbers carry provenance flags ([src] / [sec] / [der]);
re-verify against the cited paper before a number enters a manuscript.

## File map

| Question | Load |
|---|---|
| Current S8, Ω_m, w, 1−b from sample X; what it superseded | `references/results.md` |
| Cluster S8 spread, Planck mass bias, eRASS1 outlier, forecasts, stale claims | `references/open-questions.md` |
| Size of a systematic; what a referee asks | `references/systematics.md` |
| Mass function, mass definitions, likelihoods, lensing calibration, splashback, codes | `references/physics-and-methods.md` |
| Catalogue sizes, areas, lensing data, simulations, status | `references/surveys-and-data.md` |
| Title, first author, year of a cited paper | `references/sources.tsv` |

## What an expert holds in mind

- There is no single cluster S8: eRASS1 0.86 ± 0.01 (arXiv:2402.08458), DES Y3 0.864 ± 0.035 (arXiv:2503.13632), SPT 0.795 ± 0.029 (arXiv:2401.02075), Planck + DES shear 0.791 (arXiv:2509.02068), KiDS AMICO 0.74 ± 0.03 (arXiv:2507.14285).
- The eRASS1 high S8 and its growth index γ = 1.19 ± 0.21 are one feature of the data (arXiv:2410.09499); in that cosmology Planck would count 1098 clusters, not 439 (arXiv:2509.08673).
- DES Y1 clusters gave S8 = 0.65 ± 0.04, blind and wrong: lensing-model systematics (arXiv:2002.11124).
- Richness selection biases stacked lensing high by 20–60% on large scales (arXiv:2203.05416, arXiv:2002.03867).
- (1 − b) depends on its reference: 0.89 against Chandra, 0.76 against XMM, same lensing (arXiv:2402.04006). Lensing of the Planck scale gives 0.69–0.76 (arXiv:1402.2670, arXiv:1502.01883, arXiv:1904.07887); matching the Planck CMB needs 0.61 ± 0.03 (arXiv:2403.19542).
- Planck clusters are now 1.6σ from the CMB (arXiv:2509.02068); the 3.7σ of 2015 was the top of a prior-dependent range (arXiv:1502.01597).
- Simulated hydrostatic bias is 10–20% and depends on temperature weighting (arXiv:2409.07849, arXiv:2404.08539).
- Tinker 2008 is good to ≲ 5% at z = 0 and not universal (arXiv:0803.2706); baryons matter for eROSITA-like thresholds only (arXiv:1502.07357); the Euclid fit is sub-percent but halo-finder dependent (arXiv:2208.02174).
- Weak-lensing mass is biased: 5–10% for NFW fits (arXiv:1011.1681), −14.6% in Euclid-like conditions (arXiv:2409.02783). The SPT lensing systematic grows from 1% to 10% between z = 0.25 and 0.95 (arXiv:2310.12213).
- The best-constrained amplitude is not S8: SPT has σ8(Ω_m/0.3)^0.25 = 0.805 ± 0.016 (arXiv:2401.02075).
- A Poisson count likelihood underestimates errors for Rubin- or Euclid-like samples (arXiv:2210.11093).
- No counts cosmology exists from ACT DR6 (10040 clusters, arXiv:2507.21459) or SPT-3G five-year data (7190 clusters, arXiv:2607.01175).
- Splashback radii were low for optical samples (arXiv:1601.06063), not for SZ-selected ones (arXiv:1811.06081) nor KiDS AMICO (arXiv:2602.07114).

## Systematics a referee checks

1. Mass definition, mass units and the reference of any (1 − b).
2. Lensing calibration: data, redshift range, systematic floor.
3. Lensing-mass to halo-mass relation and its baryon term.
4. Selection function, purity, contaminants.
5. Optical samples: projection model, scales, richness cut, SZ or X-ray cross-check.
6. Miscentring model.
7. Mass function, neutrinos, baryons.
8. Free mass and redshift slopes; correlated scatter.
9. Sample variance in the likelihood.
10. Blinding and post-unblinding changes.
11. Exponent of the amplitude combination; CMB reference.

## Errors that recur

- Writing "clusters prefer low σ8" without naming the sample.
- Quoting DES Y1 0.65 as a measurement.
- Comparing (1 − b) values with different reference relations, or simulation b_HSE with opposite sign.
- Differencing amplitudes with exponents 0.17, 0.2, 0.25, 0.3 and 0.5.
- Calling eRASS1 all-sky: it is one hemisphere, six months (arXiv:2402.08452).
- Citing ACT cluster cosmology newer than 2013 (arXiv:1301.0816).
- Treating f_gas as a growth probe (arXiv:2111.09343).
- Quoting CMB-S4 cluster yields as upcoming (arXiv:2107.10250).
- Mixing M_sun, M_sun/h and M_sun/h70 mass limits.

## Related skills

- `cosmo-weak-lensing`: shear and redshift calibration, cosmic-shear S8.
- `cosmo-cmb-lss-cross-correlations`: tSZ and kSZ spectra, CMB lensing × galaxies.
- `cosmo-cmb`: the CMB reference of any tension.
- `cosmo-tensions-anomalies`: S8 across probes.
- `cosmo-dark-energy-modified-gravity`, `cosmo-neutrinos-dark-matter`: f(R), w, Σm_ν readings.
- `cosmo-simulations-mocks`, `cosmo-surveys-facilities`: simulations; schedules.
