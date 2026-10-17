---
name: cosmo-bbn
description: Use when reviewing, planning or fact-checking big-bang nucleosynthesis — primordial D/H from quasar absorbers, Y_P from metal-poor H II regions (LBT Y_p, EMPRESS, Izotov), helium-3, Spite plateau and the lithium problem, d(p,γ)³He and d+d rates, LUNA, n_TOF, neutron lifetime bottle versus beam, PRIMAT, PArthENoPE, AlterBBN, PRyMordial, LINX, BBN prior on Ω_b h², N_eff or N_ν from BBN, lepton asymmetry, decaying relics.
---

# Big-bang nucleosynthesis — expert reference

Snapshot 2026-10-16. Numbers carry provenance flags ([src] / [sec] / [der]);
re-verify against the cited paper before a number enters a manuscript.

## File map
<!-- key: file-map -->

| Question | Load |
|---|---|
| Standard calculation, sensitivities, weak rates, τ_n, nuclear rates, codes, likelihood construction, conventions | `references/physics-and-methods.md` |
| Which group measures what (D/H, Y_P, ³He, ⁷Li), laboratories, neutron-lifetime experiments, codes, abundance compilations, next data | `references/surveys-and-data.md` |
| Abundance values, predictions, Ω_b h² from BBN, N_ν and new-physics limits, code comparison, what superseded what | `references/results.md` |
| Size of each abundance, rate, τ_n and code systematic; referee checklist | `references/systematics.md` |
| Deuterium tension, d(p,γ) dispute, τ_n anomaly, lithium, helium spread, Hubble tension, forecasts, stale claims | `references/open-questions.md` |
| Title, first author, year of a cited paper | `references/sources.tsv` |

## What an expert holds in mind
<!-- key: what-an-expert-holds-in-mind -->

- (D/H)_P = (2.527 ± 0.030) × 10⁻⁵ from seven absorbers (arXiv:1710.11129);
  (2.533 ± 0.024) × 10⁻⁵ with an eighth (arXiv:2401.12797).
- The BBN prediction error on D/H now exceeds the observational one; the
  deuterium-burning rates set it (arXiv:2011.13874, arXiv:2604.16600).
- Light-element Ω_b h² depends on the rate philosophy: 0.02236 ± 0.00034
  (PArthENoPE v3) against 0.02195 ± 0.00021 (PRIMAT rates); 0.02218 ±
  0.00055 with rates marginalised (arXiv:2401.15054).
- Ab-initio and Gaussian-process rates put the D/H prediction 1.7–2σ below
  observation at the CMB baryon density (arXiv:2011.11320,
  arXiv:2604.16600); data-driven polynomial fits find concordance
  (arXiv:2011.13874).
- Y_P = 0.2458 ± 0.0013 (LBT Y_p Project, arXiv:2601.22238) against
  0.2402 ± 0.0040 (EMPRESS XV, arXiv:2506.24050); the spread across groups
  exceeds every quoted error.
- Predicted Y_P = 0.24709 ± 0.00017 (PRIMAT, arXiv:1801.08023); τ_n
  dominates its theory error (arXiv:2303.04140).
- τ_n: bottles 879.4(6) s against beams 888.0(2.0) s (arXiv:1802.01804);
  UCNτ 877.75 s (arXiv:2106.10375); the electron-counting J-PARC beam
  agrees with bottles (arXiv:2412.19519).
- N_ν = 2.925 ± 0.082 from LBT Y_P + D/H + CMB (arXiv:2601.22239);
  N_eff = 2.990 ± 0.070 adding ACT, SPT and DESI (arXiv:2603.13226); both
  fixed one reaction network (arXiv:2609.12065).
- ⁷Li is predicted ~3.5 times the plateau (arXiv:2011.11320, Table 2); n_TOF
  closed the main nuclear routes (arXiv:1606.09420, arXiv:1803.05701).
- Any new-physics fix of lithium must keep D/H, Y_P and ³He/⁴He standard
  (arXiv:2203.11256).
- Early-time Hubble-tension models raise ω_b and clash with deuterium
  (arXiv:2604.05095, arXiv:2607.20635).

## Systematics a referee checks
<!-- key: systematics-a-referee-checks -->

1. D/H sample (7, 8 or 13 systems), continuum and interloper treatment.
2. Y_P sample, weighted average or regression, emissivities, He I 10830.
3. Spite-plateau T_eff scale and depletion assumptions.
4. d(p,γ)³He, d(d,n)³He, d(d,p)t evaluation; rates marginalised or not.
5. Code and version; N_eff assumed in tabulated Y_P.
6. τ_n adopted and beam–bottle spread.
7. N_ν versus N_eff baseline.
8. BBN-only, CMB-only and joint results separated; compressed or full BBN likelihood.

## Errors that recur
<!-- key: errors-that-recur -->

- Quoting a "BBN prior" on ω_b without code, rate set and abundances.
- Calling the D/H–CMB offset a tension or a concordance without saying
  which deuterium-burning rates were used.
- Mixing N_ν (baseline 3) from BBN with N_eff (baseline 3.044) from the CMB.
- Comparing a regression Y_P with a weighted-average Y_P as if equivalent.
- Citing Izotov et al. 2014 (Y_P = 0.2551, N_eff = 3.58) as current.
- Treating the neutron-lifetime puzzle as evidence for dark decays.
- Combining a low EMPRESS Y_P with D/H at ΔN_eff = 0 without noting the
  incompatibility (arXiv:2401.15054, Sect. 4.3).

## Related skills
<!-- key: related-skills -->

- `cosmo-neutrinos-dark-matter`: synthesis of N_eff and neutrino-mass bounds.
- `cosmo-galaxy-clustering`, `cosmo-distance-ladder-h0`: how BAO uses the
  BBN prior to calibrate r_d; BAO + BBN H0.
- `cosmo-cmb`: Y_P and N_eff from the damping tail; CMB Ω_b h².
- `cosmo-tensions-anomalies`: Hubble tension status.
- `cosmo-early-universe-exotica`: phase transitions, primordial black holes,
  varying constants beyond BBN limits.
- `cosmo-statistics-inference`: tension metrics, marginalisation.

<!-- cosmoskill:block:start — generated by tools/sync_blocks.py, do not edit by hand -->
## Levels and layers
<!-- key: levels-and-layers -->

Answer at the lowest level that answers the question, then stop.

| Level | Read | Holds |
|---|---|---|
| L1 | this file only | the headline values, the state of the domain, the list a referee checks, the errors that recur |
| L2 | one file of `references/` | what this file does not hold: other values, their history, the size of each systematic, methods, releases |
| L3 | one dossier of `deep/` | none in this skill yet: say so and answer at L2 |
| L4 | the cited paper itself | what L1 to L3 quote; required before a number goes into a manuscript, a proposal or a referee report, and when two statements of the skills disagree |

Sizes, in thousands of tokens: L1 2k; open 3k; methods 5k; results 6k; surveys 4k; systematics 4k.

- L2: when the file map names several files, search them for the term
  before reading, and read only the passage.
- L4 starts from the L2 entry: its citation and flag say where to look. Read
  the paper with
  `python3 "${CLAUDE_SKILL_DIR}/../observational-cosmology/scripts/fetch_paper.py" <arXiv id>`
  (`--abstract`, `--outline`, `--section`, `--grep`), or with any tool that
  gives the paper. If it cannot be read, say that L4 was required and not
  done.
- A formula of the skill may be applied to the asker's numbers; label the
  result as derived.

Local layers: if a directory `.cosmoskill/` exists in the working directory,
in one of its parents, or in the home directory, or if `COSMOSKILL_HOME` is
set, run
`python3 "${CLAUDE_SKILL_DIR}/../observational-cosmology/scripts/layers.py" cosmo-bbn`
and read what it prints before answering. A note applies when its subject is
the question's; you need not open the section it is attached to. Say which
statements come from a local layer.

End the answer with one line, `<file>` being `skill` for this file or the
name of the reference file without extension:
`[cosmoskill L<level> · <base, personal, project, or several joined by +> · cosmo-bbn/<file>#<key>]`
The key is the comment under the heading of the section used; leave `#<key>`
out if you did not read that heading. At L4, put the paper and the place
read instead: `arXiv:<id>, <abstract or section>`.
<!-- cosmoskill:block:end -->
