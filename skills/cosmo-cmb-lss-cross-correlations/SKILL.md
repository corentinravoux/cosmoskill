---
name: cosmo-cmb-lss-cross-correlations
description: Use when reviewing, planning or fact-checking cross-correlations of CMB secondaries with large-scale structure — CMB lensing × galaxies or quasars (unWISE, DESI LRG, DESI Legacy, Quaia), lensing tomography S8 or σ8(z), 5×2pt/6×2pt, kSZ (pairwise, stacking, projected-field, velocity reconstruction, b_v, ACT × DESI gas profiles, baryonic feedback), tSZ × galaxies or shear, Compton-y, ISW, CIB, moving lens, patchy screening, f_NL or E_G from CMB lensing.
---

# CMB × LSS cross-correlations — expert reference

Snapshot 2026-10-07. Numbers carry provenance flags ([src] / [sec] / [der]);
re-verify against the cited paper before a number enters a manuscript.

## File map

| Question | Load |
|---|---|
| Current S8, σ8(z), f_NL, E_G, kSZ, tSZ, ISW values; what superseded what | `references/results.md` |
| Low-z growth, feedback strength, tSZ S8, ISW excess, forecasts, stale claims | `references/open-questions.md` |
| Size of a systematic; referee checklist | `references/systematics.md` |
| Limber kernels, kSZ estimators, b_v, models, blinding, codes, conventions | `references/physics-and-methods.md` |
| Lensing maps, tracers, sample sizes, shared data, status | `references/surveys-and-data.md` |
| Bibliography | `references/sources.tsv` |

## What an expert holds in mind

- unWISE × ACT DR6 + Planck: S8 = 0.810 ± 0.015, consistent with the primary CMB; supersedes 0.784 ± 0.015 (arXiv:2309.05659, arXiv:2105.03421).
- DESI LRG × ACT DR6 + Planck PR4: S8 = 0.775 +0.019/−0.022, 1.6–2.2σ low; supersedes 0.73 ± 0.03 (arXiv:2407.04607, arXiv:2111.09898). The LRG papers share one sample (arXiv:2407.04606, arXiv:2510.17796).
- Both old values rose ~1σ for identified reasons: lensing normalisation +0.6σ, redshifts +0.8σ (arXiv:2309.05659); neutrino consistency +0.017, projection effect +0.014 (arXiv:2407.04607).
- Unmitigated foregrounds bias κ × unWISE by −4.2σ; profile hardening leaves 0.04σ (arXiv:2309.05659). Polarisation-only lensing × shear is measured at 14σ (arXiv:2606.26223).
- Quaia "contamination" of Planck lensing is not confirmed with ACT DR6 (arXiv:2507.08798); DESI DR1 quasars give a high σ8 = 0.929 +0.059/−0.074 (arXiv:2506.22416).
- kSZ estimators are one ⟨ggT⟩ bispectrum with two observables, P_ge and P_gv (arXiv:1810.13423). DESI DR2 × ACT DR6: stacking at 18σ (arXiv:2604.19744), velocity reconstruction at 20.8σ (arXiv:2604.04867).
- kSZ measures τ × v. b_v = 0.23 ± 0.02 (DR2 LRG, arXiv:2604.04867) or 0.33 ± 0.03 (arXiv:2511.15701), relative to a fiducial gas-plus-HOD model. No kSZ fσ8 exists.
- Feedback is disputed. Strong: > 8σ from fiducial FLAMINGO (arXiv:2509.10455); 10 ± 2% suppression at k = 1 h/Mpc (arXiv:2512.02954). Not strong: 6×2pt (arXiv:2510.25596); a lensing/kSZ ratio tracked by fiducial FLAMINGO (arXiv:2609.22466). Non-linear velocities bias stacks by 10–20% (arXiv:2607.23339).
- tSZ-based S8 values disagree: 0.811 +0.015/−0.012 (arXiv:2506.07432), 0.72 ± 0.03 (arXiv:2605.11083).
- ISW: A = 0.96 ± 0.30 (unWISE, arXiv:2110.13959), 1.69 ± 0.61 (Quaia, arXiv:2607.22461). The supervoid excess (arXiv:1811.07812) is not reproduced with matched mocks (arXiv:2105.11936).
- f_NL errors are 20–35: Quaia −20.5 +19.0/−18.1 for p = 1 (arXiv:2504.20992), CIB × κ 43 ± 23 (arXiv:2605.03783), kSZ 15.9 +34.6/−34.4 (arXiv:2604.04867).
- Moving lens: first detection, 4.8σ (arXiv:2605.18938). Patchy screening and polarised SZ: undetected (arXiv:2608.27458, arXiv:2607.16071).
- No DES Y6, Euclid or DESI DR2 × CMB lensing cosmology was found (search of 2026-10-09). Latest DES: Y3 shear × SPT-3G D1, S8 = 0.833 +0.047/−0.061 (arXiv:2606.26223).

## Systematics a referee checks

1. Lensing maps; Monte Carlo normalisation on the overlap.
2. Foreground mitigation of κ and its simulated residual.
3. dN/dz source and marginalisation; magnification coefficient.
4. Bias model, scale cuts, best fit beside the mean.
5. Imaging weights and footprint splits.
6. kSZ: velocity source and r; fiducial P_ge; host halo mass.
7. tSZ: CIB, dust and radio leakage.
8. Simulation variant behind a feedback statement; free amplitude or not.
9. Stacks: a priori catalogue, matched mocks.
10. Blinding, post-unblinding changes, shared data.

## Errors that recur

- Quoting 0.784 or 0.73 as the lensing-tomography S8.
- Comparing amplitudes with exponents 0.5, 0.4, 0.25 and 0.2.
- Calling cross-correlations immune to systematics.
- Treating ACT + Planck lensing, or the DESI LRG analyses, as independent.
- Reading b_v ≈ 0.3 as a missing-baryon fraction, or kSZ as a growth measurement.
- Writing that DESI × ACT kSZ "rules out TNG" from the Y1 paper (PTE 0.045, free amplitude; arXiv:2503.19870).
- Citing 6×2pt (0.792) as cross-correlation; cross-only gave 0.736 (arXiv:2206.10824, arXiv:2203.12440).
- Comparing f_NL values with different p.
- Assuming one "ACT DR6" footprint: 9400 deg² for lensing, 19,000 for temperature (arXiv:2304.05203, arXiv:2511.23417).
- Citing CMB-S4 forecasts as upcoming.

## Related skills

- `cosmo-cmb`: lensing reconstruction and auto-spectrum, experiment status.
- `cosmo-weak-lensing`: galaxy-lensing S8, baryon models.
- `cosmo-peculiar-velocities`: velocities and growth.
- `cosmo-clusters`: cluster tSZ, hydrostatic bias.
- `cosmo-galaxy-clustering`, `cosmo-inflation-primordial`: DESI samples; f_NL, delensing.
- `cosmo-dark-energy-modified-gravity`, `cosmo-tensions-anomalies`: E_G, ISW; S8 across probes.
