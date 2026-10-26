# Changelog

Each release names the commit it was cut from. The detail of every step,
with the checks run and the statements compared at source, is in
`docs/history/tests/gate-log.md`; the plans that set each step are in
`docs/plans/`.

## 1.0.0 — 2026-10-26

First stable release. The content is the same shape as 0.3.0, but grown,
balanced across domains and brought under a mechanical rule for numbers.

### Content

- 28 domain skills and the hub. Seven domains added after 0.3.0:
  `cosmo-photometry-photoz`, `cosmo-galaxy-halo-connection`,
  `cosmo-data-pipelines`, `cosmo-bbn`, `cosmo-machine-learning`,
  `cosmo-cosmic-web`, `cosmo-early-universe-exotica`. Alternative distance
  probes, the cosmological principle and strong-lens statistics added as
  sections of existing skills.
- Level 3: six specialist dossiers in every domain skill (168), each chosen
  where the reference files answered fewest practitioner questions (two
  rounds of gap audit), then about 40 rebalanced so that no method, group
  or dataset dominates a subject.
- Generality: the package follows the field's own weights, not its
  owner's research; content that was specific to the owner's work moved to
  the owner's personal layer.
- Light literature refresh to 2026-10-26: one date-sorted search per
  section of every `results.md` since its snapshot; dossiers keep their own
  snapshot dates.

### The numbers rule

- Every number names its paper (`arXiv:` or `doi:`) and the place it was
  read (section, table, equation, figure, footnote or abstract); no number
  is computed by an agent (owner, 2026-10-23). About 5,400 statements were
  brought under the rule, skill by skill, each run gated with statements
  compared at source.
- Code facts and facts from official pages carry `[doc: <URL, path or
  installed package>, <date read>]`; a `[doc]` fact goes stale two years
  after its read date. A `[src]` or `[sec]` flag names a paper only.
- Numbers that are not values (names, notation, pointers) carry
  `<!-- num: not a value -->` or are recognised by tested rules of the
  checker (catalogue names, lines named by wavelength, confidence levels,
  "21 cm").
- `tools/check_numbers.py` enforces all of this; `tests/test_numbers.py`
  requires zero statements without paper and place, zero derived numbers,
  zero stale or old-style flags.
- Restored from a source read at the place: the Δχ² thresholds (PDG Review
  of Particle Physics 2024, Table 40.2) and the P-ACT n_s by spectrum
  (arXiv:2503.14452, Table 6).

### Layers

- Layers v1 (`docs/layers-v1.md`): notes, overrides and suppressions
  stamped with the fingerprint of the section they attach to;
  `sync_layers.py` reports entries whose section changed, moved or was
  retired; `promote.py` moves an entry into the package; the
  `cosmoskill-refine` skill drives them in a conversation; an example layer
  in `skills/cosmoskill-refine/example-layer/`.

### Tools and tests

- New: `tools/check_numbers.py`, `tools/locate_numbers.py`,
  `tools/refresh_status.py` (what a refresh should cover: snapshot ages,
  `[doc]` facts going stale), `tools/make_release_manifest.py`.
- `SKILL.md` has no word limit.
- Tests: 30 at 0.3.0, 83 at 1.0.0.

### Not in this release

- A benchmark with outside questions, answered blind and graded by people,
  is planned for 1.1 or 1.2. The level-3 tests of `docs/history/tests/levels/`
  are self-tests and are not evidence of quality.

## 0.3.0 — 2026-10-12 (`43eace2`)

- Levels L1 to L4: a generated block at the end of every `SKILL.md` gives
  the levels and the measured size of each; the answer names the level and
  the section it used.
- A permanent key under every section heading; `tools/assign_keys.py`,
  `tools/check_keys.py`, `tools/sync_blocks.py`.
- Free-text personal and project layers (`~/.cosmoskill/`, `layers.py`).
- `fetch_paper.py` reads a paper's abstract, outline, one section, or the
  lines around a term.
- Tooling trimmed to what answering and updating need.

## 0.2.0 — 2026-10-12 (`448cac5`)

- First public version: the hub and 21 domain skills, made general (no
  personal paths or content), MIT licence, plugin and marketplace
  manifests, `verify_sources.py` checking every cited identifier against
  arXiv.

## 0.1.0 — 2026-10-07 to 2026-10-12

- First build, one research agent per domain, before packaging (not
  released).
