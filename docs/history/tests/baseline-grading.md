# RED against GREEN — wave 1

2026-10-08. `baseline.md` is the memory-only sheet (no tools, no skill, model
cutoff June 2026); `green-wave1.md` is the same twelve questions answered from
the six wave-1 skill files only. Reference values are the ones read at source
during the coordinator gates (`gate-log.md`).

## What the baseline got wrong or could not know

| Q | Baseline (memory) | At source | Kind of failure |
|---|---|---|---|
| 1, 8 | SN-dependent w0wa preference 2.8 / 3.8 / 4.2σ given as current, with Dovekie lowering DESY5 to 3.2σ | 3.2 / 3.4 / 3.4σ for Pantheon+ / Union3.1 / DES-Dovekie (arXiv:2601.19424); Unite 3.3σ (arXiv:2609.05053, September 2026) | stale; two of three samples missing, Unite after the cutoff |
| 2 | BAO-only Lyα distances given as the current best | DR2 full shape supersedes them: D_H/r_d = 8.600 ± 0.066, D_M/r_d = 39.32 ± 0.33 (arXiv:2607.27410, July 2026) | after the cutoff |
| 3 | "No P1D cosmology" implied; k ranges "low confidence" | DR1 P1D cosmology published (arXiv:2601.21432) | missed a pre-cutoff paper |
| 5 | CMB-SPA H0 = 67.24 ± 0.35 | 67.19 ± 0.38 in the current arXiv version (arXiv:2506.20707 v2) | first-version value |
| 10 | CCHP "preprint combination of TRGB, JAGB and Cepheids 69.96 ± 1.05 ± 1.12" | not in the current abstract of arXiv:2408.06153, which gives TRGB-alone 70.39 and JWST-only TRGB and JAGB values | unverifiable recollection of an earlier version |
| 10 | SH0ES latest = 73.17 ± 0.86 (2024) | 73.18 ± 0.88 with JWST Cepheids and TRGB (arXiv:2509.01667) | missed a pre-cutoff paper |
| 11 | Euclid DR1 "scheduled for 21 October 2026" | DR1-Foundation 12 November 2026, complete DR1 mid-2027 (ESA timeline of 15 June 2026, as cited in the skills) | stale schedule |
| 12 | "Jarvis+ 2011.03408" for PSF modelling | arXiv:2011.03408 is Gatti et al., the DES Y3 shape catalogue | wrong attribution of a real ID |

What it got right: all 34 arXiv IDs it cited exist; DESI DR2 BAO, ACT DR6,
SPT-3G D1, DES Y6 3×2pt, KiDS-Legacy, Pantheon+ and Union3 headline numbers
match the sources; DES-Dovekie ID and Ωm correct.

**Reading.** On this question set the memory-only failure is not invention.
It is staleness (results after the cutoff, schedule slips, values that changed
between arXiv versions), papers missed inside the training window, and the
absence of any signal telling a correct value from a superseded one. That is
the failure the skills are built against: dated values, provenance flags,
explicit "superseded by" history.

## What the skills delivered

Eight of twelve questions fully answered from the files, the remaining four
answered with a declared gap; no conflict between skills; no wrong-file
navigation. Every stale baseline item above is correct in the GREEN sheet
except the day of the Euclid Q1 release, which the files did not hold.

## Gaps found by GREEN, sent to a repair pass

- Lyα: k and z ranges of the four DESI P1D measurement papers; systematics not
  split between 3D correlations and P1D.
- CMB: ACT DR6-alone H0 and n_s from ACT's own table.
- H0: the 70.39 value described as TRGB-alone in one file and as TRGB + JAGB in
  another (the abstract says TRGB alone); CCHP Cepheid result; anchors of the
  73.18 row.
- Euclid: day of Q1, completeness of the release list.
- Galaxy clustering: quotes 2.8–4.2σ without saying the values were revised.
- Supernovae: the DES-SN5YR total not printed.
- Weak lensing: three referee-checklist items without a reference.

The repair pass edits the files from primary sources and reruns the checker;
its result is appended to `gate-log.md`.
