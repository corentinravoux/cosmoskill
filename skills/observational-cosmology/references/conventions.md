# Notation, units and convention audit list

The most common real defect in a multi-topic cosmology manuscript is silent
convention drift between chapters. Check these explicitly.

## Units and h-factors

| Quantity | Common conventions | Trap |
|---|---|---|
| Distance | Mpc vs Mpc/h | mixing within one figure axis |
| Wavenumber | h/Mpc vs 1/Mpc; Lyα P1D often uses s/km | Lyα velocity units vs comoving |
| Angles | degrees (catalogues, ICRS) vs radians (code) | adapter boundaries |
| Velocity | km/s vs log-distance ratio η | PV estimator definition |
| Power spectrum | P(k) [Mpc/h]³, dimensionless Δ²(k) | factor (2π)³ Fourier convention |

State the Fourier convention once, explicitly:
P(k) defined via ⟨δ(k)δ*(k')⟩ = (2π)³ δ_D(k−k') P(k) is the usual LSS choice.

## Growth quantities

- f = dlnD/dlna; growth index γ via f ≈ Ω_m(a)^γ.
- **fσ₈** is what PV/RSD measure; σ₈ normalisation and effective redshift must
  accompany every quoted value, otherwise cross-analysis comparison is invalid.
- S₈ = σ₈ √(Ω_m/0.3) — lensing convention; do not interchange with σ₈.
- Growth-rate values quoted at different z_eff are not directly comparable.

## Redshift frames

- Heliocentric vs CMB-frame redshift: matters at the 10⁻³ level — i.e. exactly
  the PV signal. State which is used and where the conversion happens.
- Peculiar velocity sign convention (positive = receding) must be uniform.
- For Lyα: observed λ, rest-frame λ_RF, and the Lyα line convention
  (1215.67 Å) — state whether vacuum or air wavelengths.

## Estimator definitions to pin down

- **P1D**: FFT estimator vs optimal/quadratic estimator — different noise and
  resolution corrections; state which, and whether the two are cross-validated.
- **PV likelihood**: field-level (density+velocity joint covariance) vs
  compressed two-point (P_gg, P_uu, P_gu). State the inversion method and any
  regularisation.
- **Correlation function vs power spectrum**: state the Hankel convention and
  multipole definition (Legendre normalisation).
- **Covariance**: mocks vs analytic vs Gaussian approximation; number of mocks
  and any Hartlap-type correction.

## Cosmology-dependence hygiene

State once, per analysis, the **fiducial cosmology** used for:
- comoving distance conversion,
- template/linear P(k) computation (and the Boltzmann code + version),
- growth normalisation.

Then state where results are and are not sensitive to it. A jury/referee will
look for this; it is also the cleanest way to make a data-vs-model boundary
visible.

## Acronym / naming consistency

Lyman-α (not Lyman alpha / Ly-α mixed), ΛCDM, w₀wₐCDM, BAO, RSD, PV, TF/FP,
DESI/eBOSS/SDSS-IV, ZTF, LSST (survey) vs Rubin (observatory) — pick one usage
for the observatory/survey distinction and hold it.
