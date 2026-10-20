# Set aside on 2026-10-20 (plan item A.6)

Text taken out of the base package for balance (generality audit, correction 6).
It is kept verbatim here until phase 5 lets the owner's personal layer hold it.

## From `skills/cosmo-software-ecosystem/references/physics-and-methods.md` — §8.1 flip (key `flip`)

```
### 8.1 flip
<!-- key: flip -->

flip (Ravoux et al. 2025, arXiv:2501.16852) fits the growth rate from velocity and density fields with a Gaussian likelihood whose covariance is computed from model power spectra.
Its documentation describes three steps: build a data vector, compute a covariance, fit or forecast [src: flip docs `basicusage.md`].

- Model power spectra: matter–matter, matter–velocity-divergence and velocity-divergence spectra from `class_engine`, `cosmoprimo_engine` or `pyccl_engine`; models `linear`, `nonlinear`, `linearbel` (default, with the Bel et al. damping on the velocity terms) and `nonlinearbel`; normalisations `no_normalization`, `growth_rate`, `growth_amplitude` [src: flip docs `power_spectra.md`].
- Covariance models in `flip.covariance.analytical`: `adamsblake17`, `adamsblake17plane`, `adamsblake20`, `carreres23`, `genericzdep`, `lai22`, `ravouxcarreres`, `ravouxnoanchor25`, `ravouxqin26`, `rcrk24` [src: flip checkout, directory listing].
- Small-scale velocity damping D_u(k, σ_u) = sinc(k σ_u) applied to the velocity terms [src: flip docs `power_spectra.md`].
- Fitting: Minuit maximum likelihood, emcee MCMC, Fisher forecasts [src: flip docs `fitting.md`].
- Mandatory dependencies: numpy, scipy, matplotlib, iminuit, emcee, sympy; optional: classy, pyccl, pmesh, GPy, tensorflow, cosmoprimo [src: flip README].
- The README asks users to cite both arXiv:2501.16852 and the earlier work it builds on, Carreres et al. 2023, arXiv:2303.01198.

The paper states that the framework includes the models previously described in the literature and adds a new covariance model with wide-angle corrections (arXiv:2501.16852).
flip is "field-level" in the sense that the likelihood is written on the field values at the tracer positions; it does not sample initial conditions.

Read in the paper body (arXiv:2501.16852):

- Velocity estimators: direct velocities for simulations, a log-distance-ratio estimator for Tully–Fisher and Fundamental Plane, and SN Ia estimators, with four options for the redshift dependence J(p_i) (Watkins, low-z, higher-order Hubble law with q₀ and j₀, full with D(z) and H(z)/h) [src: Sect. 3.2, Table 2].
- Model comparison set-up: P_mm, P_mθ, P_θθ from the Bel et al. damping model with CLASS and non-linear halofit, k ∈ [0.0005, 1.0] h Mpc⁻¹, AbacusSummit cosmology, nearest-grid-point window correction with L = 10 h⁻¹ Mpc [src: Sect. 4.3].
- Numerics: some M terms (AB20, RC25) are proportional to (kσ_g)^{−9} or (kσ_g)^{−10} and suffer catastrophic cancellation in numpy at small kσ_g; flip evaluates them in arbitrary precision with mpmath [src: App. D].
- The Fisher module is the fast alternative to the likelihood, whose cost is dominated by covariance inversion [src: Sect. 5].

```

## From `skills/cosmo-multimessenger/references/physics-and-methods.md` — end of the dark-siren section, before §7 (paragraph) and the "Not verified" list (item)

```
A field-level variant grids the sirens in `d_L` space and compares the resulting density
field with a galaxy field in redshift space. The `flip` package (arXiv:2501.16852)
contains a density data vector for that purpose, `GWDensMesh` in
`flip/data_vector/gw_vectors.py` [src: public flip repository, `main` branch, class
present on 2026-10-12]. How it is built was read in a development copy and is listed
under "Not verified".

- How `GWDensMesh` builds the siren density field (per-event sky-position kernels were
  seen in a development copy of flip, not in a release).
```
