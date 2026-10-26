# Notation, units and convention audit list

The most common real defect in a multi-topic cosmology manuscript is silent
convention drift between chapters. Check these explicitly.

Snapshot: 2026-10-20 (estimator list widened to the large probe families).

## Units and h-factors
<!-- key: units-and-h-factors -->

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
<!-- key: growth-quantities -->

- f = dlnD/dlna; growth index γ via f ≈ Ω_m(a)^γ.
- **fσ₈** is what PV/RSD measure; σ₈ normalisation and effective redshift must
  accompany every quoted value, otherwise cross-analysis comparison is invalid.
- S₈ = σ₈ √(Ω_m/0.3) — lensing convention; do not interchange with σ₈.
- Growth-rate values quoted at different z_eff are not directly comparable.

## Redshift frames
<!-- key: redshift-frames -->

- Heliocentric vs CMB-frame redshift: the difference is of the size of the PV
  signal itself. State which is used and where the conversion happens.
- Peculiar velocity sign convention (positive = receding) must be uniform.
- For Lyα: observed λ, rest-frame λ_RF, and the Lyα line convention
  (1215.67 Å) — state whether vacuum or air wavelengths.

## Estimator definitions to pin down
<!-- key: estimator-definitions-to-pin-down -->

- **Shear two-point statistic**: ξ±, COSEBIs, band powers or pseudo-C_ℓ.
  ξ± mixes E and B modes and all ℓ (Schneider et al. 2002,
  arXiv:astro-ph/0206182); COSEBIs separate E and B exactly over a finite
  [θ_min, θ_max] (Schneider et al. 2010, arXiv:1002.2136); pseudo-C_ℓ needs
  noise-bias subtraction and the mode-coupling matrix of the mask (Hivon et
  al. 2002, arXiv:astro-ph/0105302). State which, and the scale range: in a
  B-mode validation, scale cuts did not translate between statistics
  (arXiv:2604.03227).
- **SN light-curve model and standardisation**: the model and its training
  (SALT2, SALT3 and their retrainings, or BayeSN) and the calibration it was
  trained on; current analyses use the Tripp estimator,
  μ = m_B + α x1 − β c − M_0 − Δμ_bias − δ_host as written in DES-Dovekie
  (arXiv:2511.07517). Calibration and model training are coupled; small
  zero-point shifts are amplified up to sixfold in distance
  (arXiv:2112.03864, arXiv:2506.05471).
- **BAO reconstruction**: algorithm and convention. DESI uses the iterative
  FFT algorithm (Burden et al. 2015, arXiv:1504.02591) in the RecSym
  convention (randoms shifted with the same redshift-space displacement, RSD
  kept), against RecIso in BOSS and eBOSS; state the smoothing scale and the
  assumed (b, f) (arXiv:2404.03000).
- **Correlation function vs power spectrum**: state the Hankel convention and
  multipole definition (Legendre normalisation).
- **Covariance**: mocks vs analytic vs Gaussian approximation; number of mocks
  and any Hartlap-type correction.
- Domain estimators (Lyα P1D, peculiar-velocity likelihoods, kSZ, cluster
  counts and others): the `physics-and-methods.md` of the domain skill.

## Cosmology-dependence hygiene
<!-- key: cosmology-dependence-hygiene -->

State once, per analysis, the **fiducial cosmology** used for:
- comoving distance conversion,
- template/linear P(k) computation (and the Boltzmann code + version),
- growth normalisation.

Then state where results are and are not sensitive to it. A jury/referee will
look for this; it is also the cleanest way to make a data-vs-model boundary
visible.

## Acronym / naming consistency
<!-- key: acronym-naming-consistency -->

Lyman-α (not Lyman alpha / Ly-α mixed), ΛCDM, w₀wₐCDM, BAO, RSD, PV, TF/FP,
DESI/eBOSS/SDSS-IV, ZTF, LSST (survey) vs Rubin (observatory) — pick one usage
for the observatory/survey distinction and hold it.
