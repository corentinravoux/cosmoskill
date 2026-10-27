# Rubric for reviewing cosmology prose

Scope: what to look for when reviewing a chapter, a paper or a proposal
section, and how to report it. Domain-specific lists are in each domain
skill.

## Red flags when reviewing cosmology prose
<!-- key: red-flags-when-reviewing-cosmology-prose -->

- σ significances quoted without stating the model comparison and datasets.
- fσ₈ compared across analyses without matching σ₈ normalisation or effective z.
- "tension" language used for <3σ without a caveat.
- Simulation-calibrated results presented without stating the simulation suite,
  resolution, and the range of validity in k or scale.
- Forecast numbers (Fisher) presented next to measurements without labelling.

## Conceptual slips that recur in cosmology prose
<!-- key: conceptual-slips-that-recur-in-cosmology-prose -->

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
  whose value (0.5) is a convention, not a measurement. <!-- num: not a value -->
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
<!-- key: using-the-checklists-without-generating-false -->

The lists above match on topic; a defect matches on *claim*. Before reporting an
item, quote the sentence in the manuscript that commits the error. If no sentence
can be quoted, there is no finding — the topic merely appears.

Two cases that look identical to a keyword search and are not:
- a parameter named as something a probe is *sensitive to* (a table cell, a list
  of constrained quantities) versus a numerical *bound* being asserted;
- a fiducial value assumed for modelling (Σmν = 0.06 eV in a composition list)
  versus a measurement being quoted.
Neither of the first kind is a claim, and neither can be wrong. <!-- num: not a value -->

## Calibrate the finding to the section's register
<!-- key: calibrate-the-finding-to-the-section-s-register -->

An overview bullet, a methods section and a results section carry different
burdens of proof. A tensions overview exists to convey which discrepancies are
serious and roughly how serious; it does not owe the reader a mechanism, a
second citation, or a significance quoted to two decimals. Before writing a
finding, ask what the section is *for* — then propose the smallest change that
fixes it. Often that is one qualifier, not a sentence.

A number quoted faithfully from a review that was current when the author wrote
is not an error. The only legitimate concern is whether it will still read as
current at submission, and a hedge fixes that without a rewrite.
