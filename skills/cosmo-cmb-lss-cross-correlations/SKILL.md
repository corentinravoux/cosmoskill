---
name: cosmo-cmb-lss-cross-correlations
description: Use when reviewing, planning or fact-checking cross-correlations of CMB secondaries with large-scale structure — CMB lensing × galaxies or quasars (unWISE, DESI LRG, DESI Legacy, Quaia), lensing tomography S8 or σ8(z), 5×2pt/6×2pt, kSZ (pairwise, stacking, projected-field, velocity reconstruction, b_v, ACT × DESI gas profiles, baryonic feedback), tSZ × galaxies or shear, Compton-y, ISW, CIB, moving lens, patchy screening, f_NL or E_G from CMB lensing.
---

# CMB × LSS cross-correlations — expert reference

Snapshot 2026-10-13. Numbers carry provenance flags ([src] / [sec] / [der]);
re-verify against the cited paper before a number enters a manuscript.

## File map
<!-- key: file-map -->

| Question | Load |
|---|---|
| S8, σ8(z), f_NL, E_G, kSZ, tSZ, ISW values; what superseded what | `references/results.md` |
| Low-z growth, feedback strength, tSZ S8, ISW excess, forecasts, stale claims | `references/open-questions.md` |
| Systematic sizes; referee checklist | `references/systematics.md` |
| Limber kernels, kSZ estimators, b_v, models, blinding, codes, conventions | `references/physics-and-methods.md` |
| Lensing maps, tracers, samples, shared data, status | `references/surveys-and-data.md` |
| kSZ velocity reconstruction: filters, estimator, surrogates, fit | `deep/ksz-velocity-reconstruction.md` |
| Galaxy or shear × y → ⟨bP_e⟩, gas model, S8 | `deep/tsz-cross-correlations.md` |
| CIB × lensing for f_NL or delensing: maps, dust, model, priors | `deep/cib-cross-correlations.md` |
| kSZ stack → gas profile: forward model, GNFW, simulations, ratio | `deep/ksz-gas-profiles.md` |
| ISW: bias, covariance, significance, matched filter | `deep/isw.md` |
| Moving lens, screening, pSZ, rotational kSZ: estimators, nulls | `deep/other-secondaries.md` |
| Bibliography | `references/sources.tsv` |

## What an expert holds in mind
<!-- key: what-an-expert-holds-in-mind -->

- unWISE × ACT DR6 + Planck: S8 = 0.810 ± 0.015, consistent with primary CMB, supersedes 0.784 ± 0.015 (arXiv:2309.05659, arXiv:2105.03421) [src: abstract].
- DESI LRG × ACT DR6 + Planck PR4: S8 = 0.775 +0.019/−0.022, 1.6–2.2σ low; supersedes 0.73 ± 0.03 (arXiv:2407.04607, arXiv:2111.09898). LRG papers share one sample (arXiv:2407.04606, arXiv:2510.17796) [src: abstract].
- Both rose ~1σ for known reasons: lensing normalisation +0.6σ, redshifts +0.8σ (arXiv:2309.05659, App. I.1 table); neutrino consistency +0.017, projection effect +0.014 (arXiv:2407.04607, Sect. 7.2).
- Unmitigated foregrounds bias κ × unWISE Blue by −4.2σ; profile hardening leaves 0.04σ (arXiv:2309.05659, Sect. 7.3). Polarisation-only lensing × shear: 14σ (arXiv:2606.26223, abstract).
- Quaia "contamination" of Planck lensing: not confirmed with ACT DR6 (arXiv:2507.08798); DESI DR1 quasars: high σ8 = 0.929 +0.059/−0.074 (arXiv:2506.22416) [src: abstract].
- kSZ estimators: one ⟨ggT⟩ bispectrum, two observables P_ge, P_gv (arXiv:1810.13423). DESI DR2 × ACT DR6: stacking 18σ (arXiv:2604.19744), velocity reconstruction 20.8σ (arXiv:2604.04867) [src: abstract].
- kSZ measures τ × v. b_v = 0.233 ± 0.020 at 150 GHz (DR2 LRG, arXiv:2604.04867, Sect. V.2 table) or 0.33 ± 0.03 (arXiv:2511.15701, abstract), relative to fiducial gas-plus-HOD. No kSZ fσ8 exists.
- Feedback disputed. Strong: > 8σ from fiducial FLAMINGO (arXiv:2509.10455); 10 ± 2% suppression, k = 1 h/Mpc (arXiv:2512.02954). Weak: 6×2pt (arXiv:2510.25596); lensing/kSZ ratio tracks fiducial FLAMINGO (arXiv:2609.22466). Non-linear velocities: 10–20% stack bias (arXiv:2607.23339) [src: abstract].
- tSZ-based S8 values disagree: 0.811 +0.015/−0.012 (arXiv:2506.07432), 0.72 ± 0.03 (arXiv:2605.11083) [src: abstract].
- ISW: A = 0.96 ± 0.30 (unWISE, arXiv:2110.13959), 1.69 ± 0.61 (Quaia, arXiv:2607.22461). Supervoid excess (arXiv:1811.07812): not reproduced with matched mocks (arXiv:2105.11936) [src: abstract].
- f_NL: Quaia −20.5 +19.0/−18.1 for p = 1 (arXiv:2504.20992), CIB × κ 43 ± 23 (arXiv:2605.03783), kSZ 15.9 +34.6/−34.4 (arXiv:2604.04867) [src: abstract].
- Moving lens detected, 4.8σ (arXiv:2605.18938); patchy screening, polarised SZ undetected (arXiv:2608.27458, arXiv:2607.16071) [src: abstract].
- No DES Y6, Euclid or DESI DR2 × CMB-lensing cosmology found (search 2026-10-09). Latest DES: Y3 shear × SPT-3G D1, S8 = 0.833 +0.047/−0.061 (arXiv:2606.26223, abstract).

## Systematics a referee checks
<!-- key: systematics-a-referee-checks -->

1. Lensing maps; Monte Carlo normalisation on overlap.
2. κ foreground mitigation; simulated residual.
3. dN/dz source, marginalisation; magnification coefficient.
4. Bias model, scale cuts, best fit beside mean.
5. Imaging weights and footprint splits.
6. kSZ: velocity source, r; fiducial P_ge; halo mass.
7. tSZ: CIB, dust and radio leakage.
8. Feedback claims: simulation variant; free amplitude or not.
9. Stacks: a priori catalogue, matched mocks.
10. Blinding, post-unblinding changes, shared data.

## Errors that recur
<!-- key: errors-that-recur -->

- Quoting the superseded 0.784 (arXiv:2105.03421) or 0.73 (arXiv:2111.09898) as lensing-tomography S8 [src: abstract].
- Mixing amplitude exponents 0.5, 0.4, 0.25, 0.2 (arXiv:2105.03421, arXiv:2407.04606, arXiv:2304.05203 Sect. I, arXiv:2109.04458) [src: abstract].
- Calling cross-correlations immune to systematics.
- Treating ACT + Planck lensing, or DESI LRG analyses, as independent.
- Reading b_v = 0.33 ± 0.03 (arXiv:2511.15701) [src: abstract] as missing baryons, or kSZ as growth.
- Claiming DESI Y1 × ACT kSZ "rules out TNG" (PTE 0.045, free amplitude; arXiv:2503.19870). [src: abstract]
- Citing 6×2pt (0.792) as cross-correlation; cross-only gave 0.736 (arXiv:2206.10824, arXiv:2203.12440) [src: abstract].
- Comparing f_NL with different p.
- Assuming one ACT DR6 footprint: 9400 deg² lensing, 19,000 temperature (arXiv:2304.05203, arXiv:2511.23417) [src: abstract].
- Citing CMB-S4 forecasts as upcoming.

## Related skills
<!-- key: related-skills -->

- `cosmo-cmb`: lensing reconstruction, auto-spectrum, experiments.
- `cosmo-weak-lensing`: galaxy-lensing S8, baryon models.
- `cosmo-peculiar-velocities`: velocities, growth.
- `cosmo-clusters`: cluster tSZ, hydrostatic bias.
- `cosmo-galaxy-clustering`, `cosmo-inflation-primordial`: DESI samples; f_NL, delensing.
- `cosmo-dark-energy-modified-gravity`, `cosmo-tensions-anomalies`: E_G, ISW; S8 across probes.

<!-- cosmoskill:block:start — generated by tools/sync_blocks.py, do not edit by hand -->
## Levels and layers
<!-- key: levels-and-layers -->

Answer at the lowest level that answers the question, then stop.

| Level | Read | Holds |
|---|---|---|
| L1 | this file only | the headline values, the state of the domain, the list a referee checks, the errors that recur |
| L2 | one file of `references/` | what this file does not hold: other values, their history, the size of each systematic, methods, releases |
| L3 | one dossier of `deep/` | how a result is obtained and how to choose a method |
| L4 | the cited paper itself | what L1 to L3 quote; required before a number goes into a manuscript, a proposal or a referee report, and when two statements of the skills disagree |

Sizes, in thousands of tokens: L1 3k; open 7k; methods 12k; results 12k; surveys 6k; systematics 11k; deep/cib-cross-correlations 8k; deep/isw 7k; deep/ksz-gas-profiles 11k; deep/ksz-velocity-reconstruction 8k; deep/other-secondaries 7k; deep/tsz-cross-correlations 7k.

- L2: when the file map names several files, search them for the term
  before reading, and read only the passage.
- L4 starts from the L2 entry: its citation and flag say where to look. Read
  the paper with
  `python3 "${CLAUDE_SKILL_DIR}/../observational-cosmology/scripts/fetch_paper.py" <arXiv id>`
  (`--abstract`, `--outline`, `--section`, `--grep`), or with any tool that
  gives the paper. If it cannot be read, say that L4 was required and not
  done.
- Quote a number only with its paper and the place it was read, or, for a
  code or facility fact, its `[doc]` page and read date, as the skill gives
  them; the skill holds no number of its own making. A formula
  may be applied to the asker's numbers; label the result as derived.

Local layers: if a directory `.cosmoskill/` exists in the working directory,
in one of its parents, or in the home directory, or if `COSMOSKILL_HOME` is
set, run
`python3 "${CLAUDE_SKILL_DIR}/../observational-cosmology/scripts/layers.py" cosmo-cmb-lss-cross-correlations`
and read what it prints before answering. A note applies when its subject is
the question's; you need not open the section it is attached to. An
override replaces its base section for this researcher: use it, and quote
the base value beside it, both labelled. A suppressed section is left out
and named as suppressed; use it only when the question asks for that
section's own content, and then say that the layer hides it. Say which
statements come from a local layer.

End the answer with one line, `<file>` being `skill` for this file or the
name of the reference file without extension:
`[cosmoskill L<level> · <base, personal, project, or several joined by +> · cosmo-cmb-lss-cross-correlations/<file>#<key>]`
The key is the comment under the heading of the section used; leave `#<key>`
out if you did not read that heading. At L4, put the paper and the place
read instead: `arXiv:<id>, <abstract or section>`.
<!-- cosmoskill:block:end -->
