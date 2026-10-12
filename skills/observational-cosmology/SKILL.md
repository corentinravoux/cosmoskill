---
name: observational-cosmology
description: Use when reviewing, planning, or fact-checking observational-cosmology content that spans several probes or whose probe is not yet clear — a manuscript chapter, a proposal, a tensions overview — and for notation and unit conventions, cross-probe field state, or to find which cosmo-* skill covers a topic.
---

# Observational cosmology working knowledge

## Which skill holds what

This skill is the hub of a suite. Each domain below is its own skill with
dated results, provenance flags and a bibliography checked against arXiv.
For a question inside one domain, load that skill and follow its file map;
its numbers supersede the digest in this hub.

| Topic | Skill |
|---|---|
| CMB spectra, lensing reconstruction, Planck / ACT / SPT likelihoods, τ, A_L, N_eff from the CMB | `cosmo-cmb` |
| Galaxy and quasar BAO, RSD, full shape, f_NL from clustering, estimators, DESI DR1/DR2 | `cosmo-galaxy-clustering` |
| Lyα BAO and AP, P1D, P3D, tomography, IGM, forest limits on dark matter | `cosmo-lyman-alpha` |
| Cosmic shear, 3×2pt, S8, shear and photo-z calibration, IA, baryons | `cosmo-weak-lensing` |
| SN Ia Hubble diagram, standardisation, calibration, compilations | `cosmo-supernovae` |
| H0: distance ladder, SH0ES / CCHP / H0DN, masers, time delays, inverse ladder | `cosmo-distance-ladder-h0` |
| Peculiar-velocity estimators and their equations, bulk flows, kSZ velocities, zero-point and Malmquist systematics, DESI DR1 PV and 2025–2026 results, forecasts; survey descriptions and the fσ8 table | `cosmo-peculiar-velocities` |
| Cluster counts, mass calibration and hydrostatic bias, selection, projection effects, cluster S8, gas fractions, splashback; eROSITA, SPT, ACT, Planck SZ, DES, KiDS | `cosmo-clusters` |
| CMB lensing × galaxies and quasars, lensing tomography, kSZ and gas profiles, tSZ × LSS, ISW, CIB, moving lens | `cosmo-cmb-lss-cross-correlations` |
| Bispectrum, parity-odd 4PCF, voids, density split, wavelets, lensing peaks and third-order shear, field-level inference, simulation-based inference | `cosmo-beyond-two-point` |
| n_s and running, tensor-to-scalar ratio and B modes, primordial non-Gaussianity, isocurvature, curvature, primordial features, cosmic birefringence | `cosmo-inflation-primordial` |
| Likelihoods, covariance corrections, blinding, samplers, priors and projection effects, profile likelihoods, Bayes factor against Δχ², tension metrics, Fisher limits, emulator error, SBI validation | `cosmo-statistics-inference` |
| N-body and hydrodynamical suites, fast mocks (COLA, FastPM, EZmocks), HOD and assembly bias, emulators, baryonic suppression of P(k), constrained simulations, accuracy requirements | `cosmo-simulations-mocks` |
| Facility facts: instrument, area, multiplex, release history and dates, status, next milestone, for spectroscopic, imaging, CMB, time-domain, radio, X-ray and gravitational-wave facilities | `cosmo-surveys-facilities` |
| Cross-probe synthesis: H0 and S8 tensions by endpoint and metric, CMB–BAO mismatch, cosmic dipole, large-angle CMB anomalies, JWST abundance, status of proposed resolutions | `cosmo-tensions-anomalies` |
| Reionisation history (τ, x_HI, mean free path, kSZ), 21 cm global signal and power-spectrum limits, HI and line intensity mapping, JWST early galaxies | `cosmo-reionization-21cm` |
| Standard sirens (bright, dark, spectral), host peculiar velocity, catalogue completeness, GW × LSS, fast radio bursts, lensed transients | `cosmo-multimessenger` |
| Definitions and formulae with the paper that fixes each convention: distances, r_d, σ8 and σ12, growth index, multipoles, Kaiser and streaming models, EFT ingredients, bias bases, Limber, neutrinos; which convention each survey adopts | `cosmo-theory-foundations` |
| Codes: Boltzmann solvers and forks, theory façades, samplers, perturbation-theory codes, estimators, Lyα and lensing tools, field-level codes; default units and settings, code agreement, maintenance status | `cosmo-software-ecosystem` |
| Σm_ν bounds and their model dependence, negative effective mass, mass ordering, N_eff, BBN, laboratory limits; warm, fuzzy, interacting, self-interacting, decaying dark matter | `cosmo-neutrinos-dark-matter` |
| w, w0wa, the DESI dark-energy evidence and its critiques, μ–Σ, growth index, EFT of dark energy, f(R), screening, E_G | `cosmo-dark-energy-modified-gravity` |

How the suite is built, checked and refreshed:
`references/suite-conventions.md`. Design documents and test logs are in the
`docs/` directory of the package repository.

## Hub files

- `references/field-state-2026.md`: cross-probe digest and facility timeline.
  Each domain skill supersedes it for its own domain.
- `references/conventions.md`: notation, units, estimator definitions to pin
  down.
- `references/review-checklists.md`: four worked systematics checklists for
  reviewing a results section. Every domain skill carries its own list under
  "Systematics a referee checks".
- `${CLAUDE_SKILL_DIR}/scripts/verify_sources.py <skill directory>`: checks
  every cited arXiv identifier of a skill against arXiv.
- `${CLAUDE_SKILL_DIR}/scripts/fetch_abstracts.py <arXiv ids>`: prints what a
  cited paper's abstract says.

## How to use this in review

1. **Date-check every claim.** Results move fast; a "latest" statement written in
   2025 is often stale. Cross-check numbers against the reference file, and if
   the number matters, verify against arXiv/ADS before endorsing it.
2. **Never invent numbers.** Central values, error bars, significances and paper
   numbers must come from a fetched source or the author. If unverified, say so.
3. **Check the probe-specific systematics list** when reviewing a results
   section — each domain skill gives the set a referee will look for.
4. **Check consistency of conventions** — h-factors, σ₈ vs S₈ vs fσ₈, redshift
   frame (heliocentric/CMB), RA/Dec units, k in h/Mpc vs 1/Mpc, ξ(r) vs P(k)
   Fourier convention. Silent convention drift between chapters is the most
   common real error in a multi-topic manuscript.

## Red flags when reviewing cosmology prose

- σ significances quoted without stating the model comparison and datasets.
- fσ₈ compared across analyses without matching σ₈ normalisation or effective z.
- "tension" language used for <3σ without a caveat.
- Simulation-calibrated results presented without stating the simulation suite,
  resolution, and the range of validity in k or scale.
- Forecast numbers (Fisher) presented next to measurements without labelling.

## Conceptual slips that recur in cosmology prose

Check these when reviewing a chapter; each is a real error, not a style point.

- **"Standard candle" for SNe Ia.** They are *standardisable*: the width–luminosity
  and colour corrections are what make them usable, and an intrinsic scatter
  remains afterwards. Same for "standard ruler" applied to BAO without saying the
  ruler is calibrated by the sound horizon at the drag epoch.
- **Which parameter a probe constrains.** The CMB constrains ωb and ωc (physical
  densities) directly; Ωm and H₀ come out through θ*. Writing that the CMB
  "measures Ωm" skips the step a referee will ask about.
- **tSZ vs kSZ.** tSZ = inverse Compton off hot electrons, a spectral distortion
  independent of cluster velocity; kSZ = Doppler from the cluster's bulk motion.
  Only kSZ carries a peculiar velocity.
- **ISW.** The effect is a *temperature* shift from a time-varying potential, not
  a spectral distortion; it is sensitive to the decay of potentials, hence to Λ
  and curvature.
- **σ₈ vs S₈ vs fσ₈.** Distinct quantities with distinct degeneracy directions.
  fσ₈ values at different z_eff are not comparable; S₈ carries an Ωm exponent
  whose value (0.5) is a convention, not a measurement.
- **Growth rate in modified gravity.** f is scale-dependent in f(R) and in most
  screened models, so a single fσ₈(z) curve is an effective quantity at the
  8 h⁻¹Mpc scale, not the ΛCDM growth rate.
- **Tension significances.** Always name both endpoints and both datasets. A σ
  computed against Planck 2018 differs from one computed against CMB-SPA.
- **Model dependence of limits.** Σmν bounds, in particular, move by a factor of
  a few between ΛCDM and w₀wₐCDM. Quote the model with the number.
- **Forecast vs measurement.** Fisher forecasts and real constraints must be
  visually and verbally distinguished when they appear in the same table.

## Using the checklists without generating false positives

The lists above match on topic; a defect matches on *claim*. Before reporting an
item, quote the sentence in the manuscript that commits the error. If no sentence
can be quoted, there is no finding — the topic merely appears.

Two cases that look identical to a keyword search and are not:
- a parameter named as something a probe is *sensitive to* (a table cell, a list
  of constrained quantities) versus a numerical *bound* being asserted;
- a fiducial value assumed for modelling (Σmν = 0.06 eV in a composition list)
  versus a measurement being quoted.
Neither of the first kind is a claim, and neither can be wrong.

## Calibrate the finding to the section's register

An overview bullet, a methods section and a results section carry different
burdens of proof. A tensions overview exists to convey which discrepancies are
serious and roughly how serious; it does not owe the reader a mechanism, a
second citation, or a significance quoted to two decimals. Before writing a
finding, ask what the section is *for* — then propose the smallest change that
fixes it. Often that is one qualifier, not a sentence.

A number quoted faithfully from a review that was current when the author wrote
is not an error. The only legitimate concern is whether it will still read as
current at submission, and a hedge fixes that without a rewrite.
