# RED against GREEN — wave 2

2026-10-09. `baseline-wave2.md` is the memory-only sheet (no tools, no skill);
`green-wave2.md` is the same twelve questions answered from the six wave-2
skill files only. Reference values are those read at source during the gates
(`gate-log.md`).

## What the baseline got wrong or could not know

| Q | Baseline (memory) | At source | Kind of failure |
|---|---|---|---|
| 1 | DESI DR1 PV counts "roughly 7×10⁴ FP and 7×10³ TF"; no arXiv IDs | 73 686 FP and 2 929 TF after the z > 0.05 TF cut (arXiv:2512.03230, body); IDs 2512.03228–03232 | missing detail that changes the reading (the result is FP) |
| 2 | no 2026 reanalysis; "my belief … but this is a guess" | Nusser & Tully 2026: 2.3σ overall, a window-dependent 3.4σ feature (arXiv:2608.14265) | after the cutoff |
| 3 | DES Y6 all-probes w0wa attributed to arXiv:2601.14559, "I recall 3.2σ" | that ID is the 3×2pt paper; the dark-energy combination is arXiv:2605.27221, 3.0σ with DESI DR2 and the CMB, 2.6σ without supernovae | wrong ID and value |
| 4 | only one E_G value, the ACT one | two current values at z = 0.555: 0.36 with Planck lensing (arXiv:2401.12971), 0.31 with ACT DR6 (arXiv:2405.12795); a 2026 KiDS-based measurement (arXiv:2604.24631) | partial |
| 6 | JUNO: 59-day result, "no mass-ordering determination yet" | 207-day result, normal ordering at ≥ 2.1σ, Bayes factor 10.18 (arXiv:2609.37895) | after the cutoff |
| 8 | KiDS AMICO KiDS-1000 "S8 ≈ 0.86 ± 0.03" | S8 = 0.74 ± 0.03; 0.86 is σ8 (arXiv:2507.14285) | σ8 taken for S8 |
| 8 | Planck PSZ2 reanalysis attributed to arXiv:2402.04006, S8 ≈ 0.78 | arXiv:2509.02068, S8 = 0.791 (+0.023/−0.021), (1 − b) = 0.844 | wrong paper |
| 10 | no DESI DR2 kSZ numbers; b_v from an earlier paper only | velocity–galaxy cross-correlation at 17.0σ (LRG), 20.8σ cumulative (arXiv:2604.04867); lensing/kSZ ratio favouring fiducial FLAMINGO (arXiv:2609.22466) | after the cutoff |
| 11 | DESI bispectrum "leaves the w0wa preference essentially unchanged or mildly stronger" | it weakens it: 2.8σ with the CMB (arXiv:2606.23936) | wrong direction |
| 12 | DES Y3 map-level SBI from an earlier paper only | S8 = 0.808 ± 0.017 in wCDM (arXiv:2606.11309) | after the cutoff |

Right from memory: the three DESI PV estimator values and the consensus; the
DESI DR2 neutrino limits; KATRIN; the warm-dark-matter limits; eRASS1 and SPT
cluster S8; the unWISE and DESI LRG lensing-tomography values.

One point to the baseline: it recalled Σmν < 0.043 eV from Wang et al. 2024,
which the skill's "tightest limit, 0.049 eV" contradicted. The paper exists
(arXiv:2405.03368) and says what the baseline said; the skill was wrong to
use a superlative and has been corrected.

**Reading.** Wave 2 shows the same pattern as wave 1, more strongly, because
these domains moved more in 2026: results after the cutoff, wrong attribution
of a real ID, one quantity taken for another (σ8 for S8), and one wrong
direction of an effect. No invented papers.

## What the skills delivered

Eleven of twelve questions fully answered from the files, one partial (the GR
prediction for the 2026 E_G). No wrong-file navigation.

## Conflicts and gaps found by GREEN, and what was done

| Found | Action |
|---|---|
| kSZ b_v range stated three ways (0.2–0.45, 0.3–0.45, 0.23–0.39) across two skills | one statement, 0.2–0.45, with the four source values named; coordinator edit |
| E_G at z = 0.555: 0.36 in one skill, 0.31 / 0.34 in another | not a conflict: Planck-based and ACT-based measurements (arXiv:2401.12971, arXiv:2405.12795). The dark-energy skill now carries both |
| "Tightest neutrino limit 0.049 eV" | superlative removed; arXiv:2405.03368 added |
| Error bars of the three DESI PV estimators only in the hub | added to `cosmo-peculiar-velocities/references/results.md` from the abstracts |
| DESI TF clustering sample 6 807 against 6 806 | left as is; two papers of the set, not re-read |
| Not in the skills: b_v for DESI DR2 ELGs and quasars; power-spectrum-only w0wa significances with the CMB; LiFT central values; SimBIG P_ℓ values; GR prediction for the 2026 E_G | left as declared gaps |

Checker after the edits: all six wave-2 skills exit 0. The coordinator's own
first edit introduced a citation without a bibliography row; the checker
caught it.
