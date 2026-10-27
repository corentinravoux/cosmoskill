# Systematics checklists for reviewing a results section

Snapshot: 2026-10-20. Six worked lists, one per large probe family, kept as
examples of the form and drawn from the referee lists of the domain skills
named under each. They are not the suite's coverage: every domain skill
carries its own list under "Systematics a referee checks", with the size of
each effect in its `references/systematics.md`.

**Weak lensing / 3×2pt** (`cosmo-weak-lensing/systematics#what-a-referee-checks-in-a-lensing-results`)
- redshift calibration: two independent methods, agreement per bin, propagation
- shear calibration m per bin, including its blending-induced redshift dependence
- PSF leakage; B-mode null tests in more than one statistic
- intrinsic-alignment model and priors; shift of S₈ under the alternative model
- baryons: scale cuts (and the simulation that set them) or a model and its prior
- covariance construction, goodness of fit; blinding level and post-unblinding changes
- projection effects on the marginal S₈ (mean against MAP); CMB data set and tension metric

**CMB power spectra and lensing** (`cosmo-cmb/systematics#what-a-referee-checks-in-a-cmb-results-section`)
- Planck likelihood, low-ℓ EE likelihood or τ prior, Planck truncation when combined
- whether "CMB" includes lensing reconstruction, and which one
- multipole ranges per spectrum and frequency, fixed before unblinding or not
- beams, temperature-to-polarisation leakage, polarisation efficiency and calibration
- foreground-template and frequency-split robustness; null-test suite and PTEs
- Boltzmann accuracy, non-linear lensing model, recombination code, N_eff and neutrino-mass convention
- for lensing: N⁰/N¹ subtraction, foreground-mitigation estimator, L range
- consistency claims between experiments that share sky, calibration and τ

**Type Ia supernovae** (`cosmo-supernovae/systematics#what-a-referee-checks-in-a-results-section`)
- exact sample and version, number of SNe, redshift range, low-z cut
- one calibration solution for calibration, model training, light-curve fits and bias simulations
- scatter and dust model in the bias corrections, and their dimensionality
- systematics budget per source, its convention, unbinned covariance
- α, β, γ, σ_int and their redshift-dependent variants; host-mass step location and tracer
- stability under low-z cut, anchor-survey removal, classifier and P_Ia cut
- samples that share supernovae treated as independent (they are not)

**BAO / full shape** (`cosmo-galaxy-clustering/systematics#what-a-referee-checks-in-a-results-section`)
- D/r_d (or α) with z_eff and the fiducial cosmology stated
- pre- or post-reconstruction; reconstruction efficiency and convention, fiducial-cosmology template dependence
- scale cuts and multipoles, and when they were chosen
- imaging systematics weights, fibre assignment/collisions
- broadband/marginalisation choices, prior sensitivity in EFT/full-shape fits, MAP beside posterior means
- covariance estimation (mock count, Hartlap-type corrections)
- for f_NL: the b_φ assumption next to the number

**Cluster counts** (`cosmo-clusters/systematics#what-a-referee-checks-in-a-results-section`)
- mass definition, mass units, and the reference of any (1 − b)
- absolute mass calibration: lensing data, redshift range, systematic floor
- weak-lensing-mass to halo-mass relation and its baryon term
- selection function, purity, contaminants; for optical samples the projection model
- mass function, neutrinos, baryons; free mass and redshift slopes of the scaling relation
- exponent of the quoted amplitude combination and the CMB data set of a tension

**Isotropy / dipole tests**
- flux-limit and depth systematics across the sky, differential completeness
- kinematic aberration + Doppler boost modelling (spectral index, count slope)
- masking, Galactic plane cuts, and their effect on low-ℓ modes
- redshift frame and evolution mixing into an apparent dipole
- look-elsewhere / posterior-volume effects in significance quoting

Peculiar velocities, the Lyman-α forest and the other domains: the list under
"Systematics a referee checks" in the domain's `SKILL.md`.
