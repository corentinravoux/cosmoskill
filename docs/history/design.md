# Observational-cosmology skill suite — design

Date: 2026-10-07. Status: in execution (the author asked for an immediate start;
this document records the design so that it can be corrected afterwards).

## 1. Request, as understood

> Create a new, extensive skill for observational cosmology, with sub-skills,
> always based on data from the literature, giving a good view of the field to
> be used as expert knowledge. Long-term task; use the new MCP servers and
> plugins; plan with superpowers or use sub-agents.

**Stated by the author:** extensive; sub-skills; literature-based; expert-level
view of the field; long-term; use sub-agents and the new tooling.

**Assumptions (correct me):**

1. The existing `observational-cosmology` skill is kept and becomes the **hub**:
   its review rubric and checklists are tested material and stay where other
   skills (`manuscript-review`, `hdr-writing`) expect them.
2. "Sub-skills" are **real skills** (`cosmo-<domain>/SKILL.md`), each
   discoverable on its own description, not reference files buried in the hub.
3. "Based on data from literature" means: every statement beyond textbook
   definitions carries an arXiv ID or DOI, every number carries a provenance
   flag, and nothing is written from model memory.
4. The suite covers the whole field, not only the author's own probes
   (Lyα, peculiar velocities), because its purpose is expert breadth.
5. Machine-readable compilations stay in `<packages>/growth_review`; the suite
   holds discussion and pointers, never a second copy of a data table.

## 2. Approaches considered

| | Approach | Verdict |
|---|---|---|
| A | Hub skill + one real skill per domain, fixed file contract, machine-checked bibliography | **chosen** |
| B | One skill, many reference files | one description cannot trigger on 21 domains; the hub would have to be loaded for every cosmology question |
| C | A plugin with its own marketplace entry | packaging overhead with no benefit for a single-user config repository |

## 3. Architecture

As packaged on 2026-10-12 (until then the skills lived under
`claude_config/claude/skills/` and these documents under
`claude_config/reports/research/2026-10-07_cosmo-skill-suite/`):

```
<repo>/
├── README.md
├── .claude-plugin/plugin.json        manifest, for installation as a plugin
├── skills/
│   ├── observational-cosmology/      hub: router, review rubric, cross-domain conventions
│   │   ├── SKILL.md
│   │   ├── references/               digest, conventions, PV files, suite-conventions.md
│   │   └── scripts/                  verify_sources.py, fetch_abstracts.py
│   └── cosmo-<domain>/               one per domain (21)
│       ├── SKILL.md                  triggers, file map, core facts, checklists
│       └── references/
│           ├── physics-and-methods.md    observables, estimators, models, codes
│           ├── surveys-and-data.md       experiments, releases, sample sizes, status
│           ├── results.md                dated headline results with provenance
│           ├── systematics.md            canonical systematics and mitigations
│           ├── open-questions.md         controversies, tensions, forecasts (labelled)
│           └── sources.tsv               key, id, first_author, year, title, role
├── scripts -> skills/observational-cosmology/scripts
└── docs/                             design.md, plan.md, agent-brief.md, tests/
```

`claude_config/install.sh` links every `skills/*/` directory that holds a
`SKILL.md` into `~/.claude/skills/` and `the second Claude home/skills/`.

## 4. Literature-grounding contract

- **Citation form in prose:** `arXiv:2503.14738` or `doi:10.xxxx/yyyy`, so a
  regular expression finds every citation.
- **Every cited ID has a row in `sources.tsv`.** `verify_sources.py` checks
  each arXiv ID against the arXiv API (the paper exists, the title matches, the
  first author matches) and reports orphan citations in either direction.
- **Provenance flags on numbers** (same vocabulary as the existing
  fσ8 compilation):
  - `[src]` — read in the paper itself (abstract or body) during the session;
  - `[sec]` — taken from a named secondary source (review, later paper);
  - `[der]` — derived, with the derivation and its assumption stated.
  A number with no flag is a defect.
- **Snapshot date** at the top of every `results.md` and `surveys-and-data.md`.
- **Forecasts** are labelled as forecasts wherever they appear.

## 5. Domains

Twenty-one sub-skills in four waves; scope per domain is in `plan.md`.

Wave 1: `cosmo-cmb`, `cosmo-galaxy-clustering`, `cosmo-lyman-alpha`,
`cosmo-weak-lensing`, `cosmo-supernovae`, `cosmo-distance-ladder-h0`.
Wave 2: `cosmo-peculiar-velocities`, `cosmo-clusters`,
`cosmo-cmb-lss-cross-correlations`, `cosmo-beyond-two-point`,
`cosmo-dark-energy-modified-gravity`, `cosmo-neutrinos-dark-matter`.
Wave 3: `cosmo-inflation-primordial`, `cosmo-tensions-anomalies`,
`cosmo-surveys-facilities`, `cosmo-statistics-inference`,
`cosmo-simulations-mocks`.
Wave 4: `cosmo-reionization-21cm`, `cosmo-multimessenger`,
`cosmo-software-ecosystem`, `cosmo-theory-foundations`.

## 6. Testing (writing-skills, reference-skill form)

- **RED:** a fresh agent answers a fixed question set from memory, with no
  tools and no skill. Expected failures: invented arXiv IDs, values stale by a
  data release, missing post-cutoff results. Saved in `tests/baseline.md`.
- **GREEN:** a fresh agent answers the same set using only the skill files.
  Pass = each answer matches the verified source and names the file it came
  from; a wrong or missing answer is a gap to fix in the reference.
- **Mechanical gate:** `verify_sources.py` exits 0 for the sub-skill.
- Each wave is gated before the next is launched.

## 7. Maintenance

The field moves monthly. Each domain gets an arXiv topic watch (arXiv MCP
`watch_topic`); a refresh session runs `check_alerts`, updates `results.md`
and `sources.tsv`, bumps the snapshot date, and re-runs the checker. The
procedure is written in the hub's `references/suite-conventions.md`.

## 8. Out of scope

- No ghost-writing of manuscript prose (the `hdr-writing` rule is unaffected).
- No new data tables duplicating `growth_review`.
- No commit or push without an explicit request.
