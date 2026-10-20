# Set aside on 2026-10-20 (plan item A.1)

Generality audit, correction 1: rebalance the hub skill
`observational-cosmology` to the field's weights. The text below was removed
from the hub, verbatim, under its original heading. Each removed statement
already lives in its domain skill, at the place named as
`<skill>/<file>#<key>`.

## From `skills/observational-cosmology/references/field-state-2026.md`

### Growth, S₈, weak lensing

```
- Clusters: eROSITA eRASS1, 5259 clusters, S₈ = 0.86 ± 0.01; SPT 0.795 ± 0.029.
```

Reason: replaced by the hub's new section "Galaxy clusters" (same values,
with citations). In the domain skill: `cosmo-clusters/SKILL#what-an-expert-holds-in-mind`;
the 5259 clusters in `cosmo-clusters/surveys-and-data#erosita-on-srg-x-ray-0-2-2-3-kev-detection-band`.

### Peculiar velocities

```
- DESI DR1 PV field-level: **fσ₈ = 0.483 (+0.080/−0.043) stat ± 0.018 sys**,
  BGS + FP + TF, 415 523 redshifts, 76 616 PVs (arXiv:2512.03229); consistent
  with the P(k) and ξ(r) analyses of the same data.
```

Reason: one of three DESI DR1 estimators; the hub now quotes the DR1
consensus. Lives in `cosmo-peculiar-velocities/open-questions#one-dataset-three-estimators-the-desi-dr1-spread`,
`cosmo-peculiar-velocities/results#published-fsigma8-from-peculiar-velocities` and
`cosmo-peculiar-velocities/physics-and-methods#covariance-mocks-consensus-blinding-practice`.

```
- Method trend: field-level / likelihood-based inference is displacing
  compressed two-point statistics.
```

Reason: method families and their comparison live in
`cosmo-peculiar-velocities/physics-and-methods#method-families`.

```
- **Bulk flow is contested.** Watkins et al. 2023 (arXiv:2302.02028) report
  4.81σ excess at 200 h⁻¹Mpc from CF4; the result is estimator-dependent, see
  *Evaluating bulk flow estimators for CF4* (arXiv:2306.11269). Do not cite the
  excess as established.
```

Reason: replaced in the hub by the one-line CF4 statement of the PV skill
(`cosmo-peculiar-velocities/SKILL#what-an-expert-holds-in-mind`); the full
debate, including the 4.81σ figure and the advice not to cite it as
established, is in
`cosmo-peculiar-velocities/open-questions#is-the-bulk-flow-at-150-250-h-1mpc-anomalous`.

### Lyman-α forest

```
- DESI DR1 P1D cosmology: Δ²★ = 0.379 ± 0.032, n★ = −2.309 ± 0.019 at
  0.009 s/km, z = 3; no running, α_s = 0.0014 ± 0.0041 with CMB and BAO
  (arXiv:2601.21432) *(2026-10-08)*. Detail: `cosmo-lyman-alpha`.
```

Reason: in `cosmo-lyman-alpha/SKILL#what-an-expert-holds-in-mind`,
`cosmo-lyman-alpha/results#compressed-linear-power-parameters-at-k-0-009-s`
and `cosmo-lyman-alpha/results#parameters-in-extended-models`.

```
- DR1 P1D measured with both FFT and optimal/quadratic estimators, with a
  dedicated estimator-validation paper; cross-estimator agreement is now
  standard practice.
```

Reason: in `cosmo-lyman-alpha/surveys-and-data#current-desi` and
`cosmo-lyman-alpha/physics-and-methods#estimators-2`.

```
- ACCEL² supplies the large-volume hydrodynamical calibration.
```

Reason: in `cosmo-lyman-alpha/surveys-and-data#hydrodynamical-suites`.

## From `skills/observational-cosmology/references/review-checklists.md`

Opening line, replaced by a six-list introduction:

```
Four worked lists, kept as examples of the form. They are not the suite's
```

```
**Peculiar velocities / growth rate**
- distance-indicator calibration and zero-point (SN Ia standardisation, TF/FP)
- Malmquist / selection bias, log-distance vs velocity estimator bias
- non-linear velocity dispersion σ_v, damping model
- coherent bulk flow vs survey window, correlated calibration errors
- host-galaxy dependence of SN standardisation, peculiar-velocity–redshift covariance
- fiducial cosmology dependence (fσ₈ degeneracy with σ₈, growth index γ)
```

Reason: the PV referee list is `cosmo-peculiar-velocities/SKILL#systematics-a-referee-checks`,
with sizes in `cosmo-peculiar-velocities/references/systematics.md` §10.

```
**Lyman-α forest P1D**
- continuum fitting bias, quasar spectral diversity
- resolution / pixel-window correction and its redshift dependence
- noise-power subtraction and estimator bias (FFT vs optimal/quadratic)
- DLA and BAL masking, metal contamination (SiII/SiIII), sky-line masking
- IGM thermal state degeneracy (T₀, γ, λ_P) with cosmological parameters
- simulation calibration: box size, resolution, splicing, feedback/UV background
```

Reason: the Lyα referee list is `cosmo-lyman-alpha/SKILL#systematics-a-referee-checks`,
with sizes in `cosmo-lyman-alpha/references/systematics.md`.

## From `skills/observational-cosmology/references/conventions.md`

### Estimator definitions to pin down

```
- **P1D**: FFT estimator vs optimal/quadratic estimator — different noise and
  resolution corrections; state which, and whether the two are cross-validated.
- **PV likelihood**: field-level (density+velocity joint covariance) vs
  compressed two-point (P_gg, P_uu, P_gu). State the inversion method and any
  regularisation.
```

Reason: replaced by field-wide items (shear statistic, SN light-curve model,
BAO reconstruction) and a pointer to the domain skills. P1D estimators:
`cosmo-lyman-alpha/physics-and-methods#estimators-2`; PV likelihood families:
`cosmo-peculiar-velocities/physics-and-methods#method-families`.

## From `skills/observational-cosmology/SKILL.md`

### Which skill holds what

```
| Peculiar-velocity estimators and their equations, bulk flows, kSZ velocities, zero-point and Malmquist systematics, DESI DR1 PV and 2025–2026 results, forecasts; survey descriptions and the fσ8 table | `cosmo-peculiar-velocities` |
```

Reason: shortened to the length of the other router lines; the "survey
descriptions and the fσ8 table" files were folded into the standard five
(plan A.4), see `cosmo-peculiar-velocities/references/retired-keys.tsv`.

## From `skills/observational-cosmology/references/sources.tsv`

```
Lai2025	2512.03229	Lai	2025	The DESI DR1 Peculiar Velocity Survey: growth rate measurements from the maximum likelihood fields method	results
ChavesMontero2026	2601.21432	Chaves-Montero	2026	Cosmological analysis of the DESI DR1 Lyman alpha 1D power spectrum	results
```

Reason: no longer cited in the hub. The rows remain in
`cosmo-peculiar-velocities/references/sources.tsv` and
`cosmo-lyman-alpha/references/sources.tsv`.
