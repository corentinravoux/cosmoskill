<!-- Produced by the Plan agent on 2026-10-12 from docs/specs/2026-10-12-general-levelled-package-design.md. Tags: [V] verified by the planner, [I] inferred. Not yet reviewed by the owner. -->

# Part 2 — Phase 1 implementation plan

Starting state [V]: `main` at `a63e54b`, equal to `origin/main`, public; `docs/specs/` untracked; 22 skills, 132 Markdown files, 21 `sources.tsv` files with 2,382 rows; `~/.cache/cosmo-skill-verify/arxiv.json` holds all 1,901 distinct arXiv IDs of those bibliographies; the owner's machine loads the skills through per-skill symlinks in `~/.claude/skills/`.

Rules for the whole phase:
- No research agent.
- No number, error bar, redshift, flag or existing `sources.tsv` row changes.
- A statement whose only support is a private source is removed, never replaced from memory. Each removal is logged verbatim in `docs/tests/phase1-log.md`.
- No commit, push or tag without the owner's request.

## Inventory (all counts measured by grep on the working tree)

| Kind | Where | Count |
|---|---|---|
| K1 absolute path `/home/<user>/…` | five reference files of `cosmo-peculiar-velocities` (pointers to the hub PV files) | 6 lines |
| K2 `~/Software`, `~/Documents` | hub `SKILL.md` 2; `suite-conventions.md` 7; PV `SKILL.md`, `results.md`, `surveys-and-data.md` 1 each; multimessenger `physics-and-methods.md` 1 (a private report) | 13 lines |
| K3 owner's packages by name | `growth_review`: 11 lines in 8 files (hub `SKILL.md`, `pv-surveys.md`, `fsigma8-pv-compilation.md`, `suite-conventions.md`, PV `SKILL.md`, `results.md`, `surveys-and-data.md`, galaxy-clustering `results.md`). `oneuniverse`: 2 lines (software `systematics.md`). `lyapower`, `lelantos`, `lyavoid`, `p1desi`: lyman-alpha `physics-and-methods.md` 186, 254; simulations-mocks `physics-and-methods.md` 87 | 16 lines |
| K4 "the author's …" meaning the owner | software-ecosystem `systematics.md` 7, 31, 179; `physics-and-methods.md` 7; `surveys-and-data.md` 118; `open-questions.md` 160. lyman-alpha 186, 254. multimessenger `physics-and-methods.md` 266, `open-questions.md` 141. tensions `physics-and-methods.md` 390 | 11 lines |
| K5 private tooling | `claude_config/install.sh` (`suite-conventions.md` 84); arXiv MCP watch procedure (66–69, 87); "local code read" (multimessenger `physics-and-methods.md` 278) | 6 lines |
| K6 environment-bound provenance | software-ecosystem, 5 files: "installed" 64, "checkout" 33, "context7" 19 occurrences; definitions at line 7 of `physics-and-methods.md`, `systematics.md`, `results.md`; development branches `4most_test` (picca), `mesh_improvements` (flip) | — |
| K7 voice and stale text | `fsigma8-pv-compilation.md`: first person at lines 3 and 84; its section 6 describes `fsigma8_pv_data.txt` and `validate_fsigma8.py`, which its own header says were deleted | — |
| K8 dependence on the hub PV files | "hub" 34 times in the six PV files; 3 lines in hub `SKILL.md`. The two files cite 48 distinct IDs; 10 have no row in the PV bibliography: 1011.3114, 1204.4725, 1205.4237, 1503.05945, 1606.03092, 1612.07809, 1703.05324, 1801.04969, 1901.03530, 2211.16390 | — |
| K9 tailoring without a string | hub description names PV and fσ8; hub checklists cover PV, Lyα P1D, dipole and BAO only; "at the defence" (hub 169); persona at `docs/agent-brief.md` line 6 | — |
| K10 docs and README | `/home/<user>`: 6 lines (agent-brief 2, plan 1, green-wave1 2, green-wave2 1). `~/Software`: 8 (README 2, design 1, plan 2, gate-log 2, green-wave34 1). `claude_config` or `claude_env`: 13. README: author's install script, MCP watch, `growth_review` | — |

Strict total under `skills/`: 37 lines in 20 files (K1–K5 overlap). Not personal, left alone: 47 "the authors" lines; 14 bibliography rows with Ravoux as first author in 6 skills; public identifiers such as `ravouxcarreres`.

## Tasks, in order

**T0. Baseline.** Touches `docs/tests/phase1-log.md` and `tools/numeric_fingerprint.py` (new; prints per file the set of distinct tokens matching `\d[\d.,]*`).
- `git switch -c phase-1-generalise`.
- Record `verify_sources.py --offline skills/cosmo-*` (expect 21 lines, 0 problems) and the fingerprint of every file under `skills/`.
- Proof: the log holds both outputs.
- Do not touch anything else.

**T1. Lint, red first.** New: `tools/lint_generic.py`, `tools/lint-patterns.txt`, `tests/test_lint.py`, `tests/fixtures/lint/`.
- Patterns: `/home/`, `/Users/`, `~/Software`, `~/Documents`, `<packages>/`, `claude_config`, `claude_env`, `\second Claude home`, `install\.sh`, `growth_review`, `oneuniverse`, `author's (environment|own|project|report|compilation|\`)`, `the author's$`, `local code read`, `hdr-writing`, `manuscript-review`, `claude-mem`, first-person `\bI (said|could|found)\b`.
- Scope: `skills/`, `README.md`, `.claude-plugin/`, `docs/`, `tools/`. `docs/history/` is exempt from the name patterns, not from the path patterns.
- Allowlist: the repository URL in `README.md` and the two JSON files; `~/.claude/`, `~/.cache/`, `~/.cosmoskill/` in README and docs.
- Proof: the unit test passes (a fixture with each pattern exits 1, a clean fixture exits 0). On the untouched tree the lint reports every K1–K5 line; the count goes in the log.
- Do not write patterns that match `the authors`, `Ravoux et al`, or `ravoux[a-z]` identifiers.

**T2. Fold the hub PV files.** Touches the two files, the six PV files, PV `sources.tsv`.
1. `git mv` both files from `skills/observational-cosmology/references/` to `skills/cosmo-peculiar-velocities/references/`, names kept.
2. Citation form only: `[2501.16852](https://arxiv.org/abs/2501.16852)` and `[arXiv:…](…)` become `arXiv:2501.16852`; bare IDs in the `arXiv` column of the section 6 table get the prefix.
3. Add ten rows for the IDs of K8. Title and first author come from `fetch_abstracts.py <ids>`, the year from the ID, the role from the table the paper sits in (measurement: `results`; forecast section: `forecast`).
4. Replace the six absolute pointer lines and the 34 "hub" mentions by the local file names. PV `SKILL.md` lines 11–13 become two file-map rows.
5. In `fsigma8-pv-compilation.md`: make lines 3 and 84 impersonal; delete stale section 6. Do not reconcile its "35 rows" with the header's "36": the deletion removes the conflict.
6. All `growth_review` sentences (K3) collapse into one line in `fsigma8-pv-compilation.md`. Its wording waits for the owner's decision. Machine paths go in every case.
- Proof: `verify_sources.py skills/cosmo-peculiar-velocities` prints `150 sources, 0 problem(s) [arXiv-checked]` [I: 140 + 10]. The fingerprints of the two moved files equal those of T0, minus the logged section. `grep -rn "hub" skills/cosmo-peculiar-velocities` returns only "`observational-cosmology`: hub" in Related skills.
- If the checker reports an ID not found, correct it from the paper and log it.
- Do not touch any value, error, redshift or flag in the tables, nor the 140 existing rows.

**T3. Hub.** Touches hub `SKILL.md`, `suite-conventions.md`, new `references/review-checklists.md`, new `references/sources.tsv`.
- `SKILL.md`: remove "peculiar-velocity surveys and the fσ8 compilation" from the description; remove the parenthesis in the PV router row; remove the PV and `growth_review` paragraphs under "Hub files"; replace `<docs>/` by the repository URL; "at the defence" becomes "at submission".
- Move the four checklists unchanged to `review-checklists.md`, with one sentence saying each domain skill holds its own list.
- Add the script location as `${CLAUDE_SKILL_DIR}/scripts/`.
- `suite-conventions.md`: commands relative to the hub skill directory (`scripts/verify_sources.py ../cosmo-<domain>`); refresh procedure through public means (`fetch_abstracts.py`, date-sorted arXiv listing), MCP named as optional; "Adding a domain" without `install.sh`; "Where data lives" restated as the design's non-goal; the contract reads "five standard reference files plus topical files listed in the file map".
- `sources.tsv` for `field-state-2026.md`: 23 rows copied verbatim from the domain bibliographies, 2 fetched [V: 25 IDs, 23 already present].
- Proof: `verify_sources.py skills/observational-cosmology` prints 25 sources, 0 problems. A question about PV surveys triggers the PV skill in T10.
- Do not touch `conventions.md` or the numbers of `field-state-2026.md`.

**T4. Domain skills, K3–K6.**
- lyman-alpha 186: delete the sentence. Line 254 and simulations-mocks 87: keep as a neutral list of public implementations only if `curl -sI https://github.com/<owner>/<name>` returns 200 for each; otherwise delete.
- multimessenger `physics-and-methods.md` 265–267: drop the private `[sec]` flag; keep the sentence as `[src]` only if `fetch_abstracts.py 2512.15380` shows it in the abstract, else move it to "Not verified". Lines 276–280: delete the report path; keep the `GWDensMesh` sentence only if the file exists on the default branch of the public flip repository, cited by repository and version.
- multimessenger `open-questions.md` 139–143: retitle, delete the sentence about the report, keep the cited bullets.
- tensions 390: delete the clause quoting the private compilation; the "not read at source" item stays.
- software-ecosystem: redefine the three words in the three header lines. "installed": read in the released package at the stated version. "checkout": read in the public source repository at the stated tag, branch or commit. "context7": read in the library documentation on 2026-10-11. Delete `systematics.md` 31, the `oneuniverse` parenthesis of 179 (the RING/NESTED advice stays) and `open-questions.md` 160. Reword `surveys-and-data.md` 118. List facts read on development branches under "Not verified" as "development branch, not a release".
- Proof: lint exits 0 on `skills/`; `verify_sources.py --offline skills/*/` reports 0 problems; fingerprints differ from T0 only on logged removals.
- Do not touch the 116 provenance tags themselves or any value.

**T5. Docs.**
- `git mv` `docs/design.md`, `docs/plan.md` and `docs/tests/` under `docs/history/`. Add `docs/history/README.md`: record of the October 2026 single-user build, superseded by `docs/specs/`.
- Replace the 14 absolute or `<repo>/` paths in docs by repository-relative ones.
- `docs/agent-brief.md`: line 6 becomes "a professional cosmologist"; relative paths; MCP tool names kept as one option, with the public fallbacks named.
- Proof: the lint exits 0 on `docs/`.
- Do not touch the rules of the brief, nor any table or value in the test logs.

**T6. Packaging and README.**
- `.claude-plugin/plugin.json`: version `0.2.0`; `license` once decided.
- New `.claude-plugin/marketplace.json` with `name`, `owner`, and one entry `{"name": "cosmoskill", "source": "./"}`; no `version` in the entry.
- Delete the root symlink `scripts`: one canonical path, and it breaks on Windows clones.
- LICENSE files once decided.
- README, route A: `/plugin marketplace add corentinravoux/cosmoskill`, `/plugin install cosmoskill@<marketplace>`, update with `claude plugin update`; skills named `cosmoskill:cosmo-…`.
- README, route B: `git clone … ~/.claude/skills/cosmoskill`; same names; `git pull`.
- README, route C: clone anywhere and link each `skills/*/` into `~/.claude/skills/`; bare names; `git pull`.
- README also says: install by one route only. The table is recomputed (hub row without PV, hub 25 sources, PV 150). The author-machine paragraphs go. The limits section gains the list of the design's section 1.
- Proof: `claude plugin validate . --strict` passes; the lint exits 0.
- Do not touch the "What to trust" section, except additions.

**T7. Checker tests, snapshot, structure check.** New: `tests/test_verify_sources.py`, `tests/fixtures/skills/`, `tools/make_arxiv_snapshot.py`, `tests/fixtures/arxiv-snapshot.json`, `tools/check_structure.py`.
- Fixtures: one good skill, and one each for wrong title, wrong first author, citation without row, row never cited, bad header, duplicate key. Each is asserted on output and exit status, with a fixture cache passed through `XDG_CACHE_HOME`, so no network.
- The snapshot holds title and first author for every arXiv ID in any `sources.tsv`, written from the local cache. The checker reads only `authors[0]` [V].
- `check_structure.py` fails when a skill directory name differs from `name`; when a description exceeds 1,024 characters or does not start with "Use when"; when a file named in a file map is missing; when a sibling skill named in "Related skills" does not exist; when a README count differs from the row count.
- Proof: `python3 -m unittest discover -s tests` passes; each script exits 1 on its broken fixture.
- Do not change the checker's matching logic or thresholds.

**T8. Continuous integration.** New: `.github/workflows/check.yml`.
- On push and pull request, Python 3.12, standard library only: the lint, the structure check, the unit tests, `verify_sources.py --offline skills/*/`.
- Then the snapshot-backed full check: copy the snapshot to `$RUNNER_TEMP/c/cosmo-skill-verify/arxiv.json` and run the checker with `XDG_CACHE_HOME=$RUNNER_TEMP/c`. The network is used only for IDs absent from the snapshot [V: cached IDs are never queried].
- Weekly `schedule` and `workflow_dispatch`: the same command with an empty cache, `timeout-minutes: 90`.
- Proof: after the owner pushes a scratch branch, a deliberately wrong title turns the push job red and reverting it turns it green.
- Do not query arXiv for every ID on each push. Do not put `claude plugin validate` in CI: unauthenticated use was not confirmed.
- Action version tags were not checked this session.

**T9. Local verification.** No file changes except the log. Run:
- the lint;
- the structure check;
- the unit tests;
- `verify_sources.py skills/*/` online (expect 22 lines, 0 problems);
- `grep -rIE '/home/|~/Software|~/Documents' skills README.md .claude-plugin docs` (expect nothing);
- `claude plugin validate . --strict`;
- the fingerprint comparison.

**T10. Clean-account test.** New: `tools/clean_account.sh`, `docs/tests/phase1-clean-account.md`.
- It needs a commit on the branch, made at the owner's request, and the owner's login in a fresh configuration directory: `CLAUDE_CONFIG_DIR=$(mktemp -d)/.claude`, then a clone of the branch.
- Route A from the local clone: `claude plugin marketplace add <clone>`, `claude plugin install cosmoskill@<marketplace>`; `claude plugin details cosmoskill` must list 22 skills.
- Routes B and C, each in its own configuration directory: a `-p` prompt asking for all skill names containing "cosmo" must return 22.
- One files-only run of eight fixed questions, web tools disallowed, under route A:
  - the DESI DR1 PV question of the wave-2 set;
  - one row of the moved fσ8 table with its `der` flag;
  - one routing question to the hub;
  - one question crossing two skills;
  - one software-defaults question;
  - three taken from the existing sets.
- Pass: answers equal the files and the earlier green sheets; each names skill and file; no forbidden string in the output; no file read outside the clone; no listing-budget warning in the `--debug` log.
- A marketplace added from a local path loads in place [V], so the cached-copy path is confirmed only after the owner pushes: repeat route A from GitHub then.

**T11. Hand-over.** Report to the owner the diff summary, the removal log and the open decisions. The owner commits, pushes and tags.

## Acceptance checklist

- [ ] The lint exits 0 on the tree, and exits 1 on its fixture.
- [ ] No match for `/home/`, `~/Software`, `~/Documents` anywhere outside `.git`.
- [ ] The checker passes online on 22 skills, hub included; the unit tests show it fails on each defect kind.
- [ ] The two PV files live in `cosmo-peculiar-velocities`; their 48 IDs are in checked form with rows; numeric fingerprints unchanged apart from logged removals.
- [ ] `claude plugin validate . --strict` passes; the structure check passes.
- [ ] CI is green on the branch and red on a planted error.
- [ ] Clean account: 22 skills load under each of the three routes; eight of eight questions pass; route A repeated from GitHub after the push.
- [ ] README states the routes, the naming difference and the limits.
- [ ] Open until the owner decides: LICENSE files and `license` field; package and marketplace name; the fσ8 pointer line.

### Critical Files for Implementation
- <skills>/observational-cosmology/SKILL.md
- <skills>/observational-cosmology/references/fsigma8-pv-compilation.md
- <skills>/cosmo-peculiar-velocities/references/sources.tsv
- <skills>/observational-cosmology/scripts/verify_sources.py
- <repo>/README.md
