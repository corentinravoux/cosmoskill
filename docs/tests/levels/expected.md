# Level test — expected behaviour

Written from the skill files on 2026-10-12, before the first run. "Files"
are the files the answer should need; opening more is a failure of the stop
rule for L1 questions and a cost for the others.

| Q | Skill | Level | Files | What must be there |
|---|---|---|---|---|
| 1 | cosmo-weak-lensing | L1 | SKILL.md | reduced, not gone; depends on metric and CMB reference |
| 2 | cosmo-lyman-alpha | L1 | SKILL.md | DR2 BAO values; full-shape distances as current best |
| 3 | cosmo-cmb-lss-cross-correlations (or cosmo-peculiar-velocities) | L1 | SKILL.md | no: it measures τ × v; no kSZ fσ8 exists |
| 4 | cosmo-cmb (or cosmo-surveys-facilities) | L1 | SKILL.md | cancelled, 9 July 2025 |
| 5 | cosmo-clusters | L1 | SKILL.md | the referee list of the skill |
| 6 | cosmo-multimessenger | L1 | SKILL.md | 71.7 (+9.4/−7.5), GWTC-5.0 |
| 7 | cosmo-lyman-alpha | L2 | results.md | ranges per estimator; the unresolved 4.4 against 4.2 |
| 8 | cosmo-statistics-inference | L2 | results.md | both readings: 24 % widening, 11 % scatter |
| 9 | cosmo-surveys-facilities (or weak-lensing, galaxy-clustering) | L2 | surveys-and-data.md or results.md | 24 June 2026 |
| 10 | cosmo-distance-ladder-h0 | L2 | results.md | 73.994 ± 0.697 |
| 11 | cosmo-reionization-21cm | L2 | results.md | the Phase II limit with its k and z |
| 12 | cosmo-supernovae | L2 | results.md | 1550 supernovae; 0.334 ± 0.018 |
| 13 | cosmo-statistics-inference | L3 asked, none exists | physics-and-methods.md and/or results.md | says there is no dossier, answers at L2 |
| 14 | cosmo-lyman-alpha | L4 required | SKILL.md, possibly results.md | says the number must be re-read in arXiv:2503.14739; notes that ± 0.101 combines the statistical and systematic errors |
| 15 | cosmo-lyman-alpha | L2 | results.md, plus the layer | uses the note marked FIXTURE-NOTE-7Q, labelled personal; no estimator introduction |
| 16 | cosmo-tensions-anomalies (or cosmo-distance-ladder-h0) | L1 | SKILL.md | 4.4σ to 7.1σ depending on the early endpoint |

Pass: at least 13 of 16 at the expected level with the expected content; no
reference file opened for questions 1 to 6 and 16; question 15 names the
personal layer; every answer ends with the footer line.

## Recheck (`questions-recheck.md`), written before the run

| Q | Skill | Level | What must be there |
|---|---|---|---|
| 1 | cosmo-clusters | L1 | the referee list; no reference file opened |
| 2 | cosmo-multimessenger | L1 | 71.7 (+9.4/−7.5); no reference file opened |
| 3 | cosmo-lyman-alpha | L2 | ranges per estimator; footer of the form `cosmo-lyman-alpha/results#<key>` |
| 4 | cosmo-lyman-alpha | L4, done | the abstract of arXiv:2503.14739 read with the package script; 8.632 ± 0.098 ± 0.026 confirmed; ± 0.101 identified as the combined error |
| 5 | cosmo-lyman-alpha | L1 | the personal note applied and labelled, layers joined in the footer, no reference file opened |
| 6 | cosmo-surveys-facilities | L1 | cancelled, 9 July 2025 |
| 7 | cosmo-statistics-inference | L2 | the formula with its source, the 300-point case worked out and labelled as derived |

Pass: seven of seven, and the list of instructions that did not work no
longer contains the items rewritten after the first run.
