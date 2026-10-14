# Phase 2 — level router, section keys, layers v0: plan

From `2026-10-12-cosmoskill2-roadmap.md`, phase 2, with the specification's
revisions 7 (section keys now) and 3 (no load-time command). No research
agent. One files-only test run at the end.

## Deliverables

| | File | What |
|---|---|---|
| 1 | `tools/assign_keys.py` | adds `<!-- key: slug -->` under every `##` and `###` of the skills; idempotent, never changes an existing key |
| 2 | `tools/check_keys.py` | every heading keyed, keys unique per file, well-formed; `--against <git ref>`: no key of that ref lost unless listed in `references/retired-keys.tsv` |
| 3 | `tools/templates/fixed-block.md`, `tools/sync_blocks.py` | one generated "Levels and layers" block at the end of every `SKILL.md`, with the measured size of each level; `--check` fails on a stale block |
| 4 | hub `SKILL.md` | the level rules in full: how a question maps to a level, when to escalate, the answer footer |
| 5 | `skills/observational-cosmology/scripts/layers.py` | finds the project layer (`./.cosmoskill/`, searched upward) and the personal layer (`$COSMOSKILL_HOME`, default `~/.cosmoskill/`), prints profile and notes for a skill; `init`, `check` |
| 6 | `docs/layers-v0.md` | format of `profile.md` and `notes.md`, and what v0 does not do |
| 7 | `tests/` | unit tests for 1, 2, 3, 5, each with a case that fails |
| 8 | `docs/tests/levels/questions.md` | questions from four viewpoints, each with expected level and file |
| 9 | — | dropped: the checks are run by hand in the update cycle; the package is kept private for testing, without continuous integration |

## Decisions taken here

- **Key.** A slug frozen at assignment, written `<file-stem>#<slug>` inside a
  skill and `<skill>/<file-stem>#<slug>` across skills. It is derived from the
  heading once and does not follow later rewording of the heading.
- **Levels on disk.** L1 `SKILL.md`; L2 `references/*.md`; L3 `deep/*.md`,
  absent in every skill for now; L4 the paper.
- **Notes attach to keys**, not to heading text, so a later rewording or
  reordering of the base does not orphan them. `layers.py check` reports a
  note whose key the base no longer has.
- **Profile.** Free text plus two optional lines: `home-domains:` (skills
  where the researcher is a specialist: orientation may be skipped, the
  lowest-level rule still holds for everything else) and `conventions:`.
- **Answer footer.** `[cosmoskill L<n> · <layer> · <skill>/<file>#<key>]`.
  Wording is the maintainer's to change in the template.
- **Not in this phase.** Shortening the skill descriptions: it changes what
  triggers a skill and can only be judged with the command-line client's
  listing diagnostics, which were not available. Structured layers (claims,
  sources, overrides, sync, promote) are phase 5.

## Acceptance

1. `check_keys.py` passes; it fails on a heading without a key, a duplicate,
   and, with `--against`, on a removed key.
2. `sync_blocks.py --check` passes; it fails after a block is edited by hand.
3. With a fixture layer, `layers.py <skill>` prints the note and its layer;
   with no layer it prints nothing and exits 0; `layers.py check` reports a
   note on a key the base does not have.
4. Lint, structure check, bibliography check and all unit tests pass.
5. Files-only test on `docs/tests/levels/questions.md`: at least 80 % of
   questions answered at the expected level; no L1 question opens a
   reference file; the fixture note is found and labelled as personal.
