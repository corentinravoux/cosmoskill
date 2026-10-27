# Changelog

Each release names the commit it was cut from. The detail of every step,
with the checks run and the statements compared at source, is in
`docs/history/tests/gate-log.md`; the plans that set each step are in
`docs/plans/`.

## 1.0.1 — 2026-10-27

Claude app support. The same repository installs as a plugin in Claude Code
and in the Claude app (web, Desktop, Cowork); content unchanged. Plan:
`docs/plans/2026-10-27-claude-app.md`.

- **README rewritten** around the two hosts: install in the app and in
  Claude Code, a table of what each host can do, how L4 reaches arXiv in the
  app, and how not to load the skills twice when Claude Code syncs the
  account's plugins. Shorter: 199 lines instead of 318.
- **Script paths.** Every skill calls the hub's scripts as
  `"${CLAUDE_SKILL_DIR}"/../*observational-cosmology/scripts/…`: the glob
  finds the hub whether or not its folder carries the app's plugin prefix
  (`cosmoskill:observational-cosmology`), and the skill says what
  `${CLAUDE_SKILL_DIR}` means when it reaches the model unexpanded.
- **L4 fallback order:** the script; a web tool on `arxiv.org/abs/<id>` when
  the script cannot reach arXiv; otherwise "L4 required, not done", never the
  paper's content from memory.
- **Scripts:** `fetch_paper.py` and `verify_sources.py` stop at once, with
  exit code 3 and that advice, when the machine has no route to arXiv (failed
  name lookup, refused connection, unreachable network, a proxy's 403 over
  HTTP or HTTPS). Timeouts and rate limits are retried as before. The hub's
  script lines now start with `python3` (the scripts are not executable).
  14 tests added (97).
- `cosmoskill-refine` is marked Claude Code only.
- **For layer users:** `levels-and-layers` changed in every skill, and the
  hub's `hub-files` and `choosing-the-level`; `sync_layers.py` reports entries
  attached to them (`releases/1.0.1.tsv`).

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
  section of every `results.md` since its snapshot, and citation checks on
  the papers behind the headline values; about 95 paper additions over the 28
  skills (some papers enter several), each run gated with statements
  compared at source. Headline
  values that moved: H0 from time delays (TDCOSMO-2026, arXiv:2610.14781,
  superseding TDCOSMO-2025) and from standard sirens (GWTC-5.0,
  arXiv:2605.27227, superseding GWTC-4.0); the scale independence of
  "lensing is low" (now scale-dependent with DECADE, arXiv:2610.23828); the
  LVK sub-solar PBH limit (O4, arXiv:2610.19329). The other reference files
  and the dossiers keep their own snapshot dates.
- `releases/1.0.0.tsv`: the section keys added, changed, moved or retired
  since 0.3.0, for `sync_layers.py`.

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
