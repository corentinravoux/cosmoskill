<!-- Produced by the Plan agent on 2026-10-12 from docs/specs/2026-10-12-general-levelled-package-design.md. Tags: [V] verified by the planner, [I] inferred. Not yet reviewed by the owner. -->

# Part 1 — Roadmap for cosmoskill 2

> **Scope decisions taken after this roadmap was written (2026-10-12).**
> The package holds general knowledge with a checked link to each source; a
> number is verified on demand by reading the linked paper. The claims table
> and verification grades of phase 3 are dropped, with the re-reading
> campaign they implied. The package is kept private for testing: no install
> validation, no continuous integration, no lint for single-user content.
> Kept from the tooling: the bibliography checker, the paper reader, the
> layer script, and the three upkeep tools for section keys and level blocks.
> Phases 1 and 2 are done. What remains of phase 3 is even coverage; phases 4
> to 7 stand, without the parts that depended on claims.

Tags: **[V]** verified this session (file read, command run, documentation page fetched); **[I]** inferred. Units: a *run* is one research agent (350–500k tokens); a *test* is one files-only run (about 200k); a *window* holds about five runs.

## 0. Findings that change the starting point

1. **The repository is committed and public.** One commit `a63e54b "first version"` exists, `main` equals `origin/main`, and github.com/corentinravoux/cosmoskill is public with no LICENSE [V: `git log`, `git status`, page fetched]. Only `docs/specs/` is untracked [V]. The personal content is therefore already published, unlicensed. Phase 1 corrects a public repository, and the licence decision is urgent.
2. **The design's "40 skill files" is not reproduced.** 39 files contain "the author", but 47 of those 59 lines mean a paper's authors [V]. Content tied to one person or machine sits in 20 files (37 lines), plus the provenance vocabulary of `cosmo-software-ecosystem` [V]. Inventory in Part 2.
3. **The hub is outside the checker.** It has no `sources.tsv`; `field-state-2026.md` cites 25 arXiv IDs [V]. The two hub peculiar-velocity files cite 48 distinct IDs as links or bare numbers, which the checker's regex does not see [V].

## 1. Claude Code facts

Sources: [S] https://code.claude.com/docs/en/skills · [M] https://code.claude.com/docs/en/plugins/manifest-reference (fetched as `/plugins-reference`) · [R] https://code.claude.com/docs/en/plugins/marketplace-reference · [C] https://code.claude.com/docs/en/plugin-marketplaces · [L] https://code.claude.com/docs/en/plugins/loading · [H] https://code.claude.com/docs/en/plugins/host-marketplace · [P] https://code.claude.com/docs/en/plugins/create · [I] https://code.claude.com/docs/en/plugins/install · [A] https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview

| # | What the documentation says [V] | Src | Consequence |
|---|---|---|---|
| 1 | Skills load from `~/.claude/skills/<name>/`, from `.claude/skills/` (start directory up to repository root), from `<plugin>/skills/<name>/`, and from managed settings. | S | Three install routes exist. |
| 2 | Same name: enterprise over personal, personal over project. A plugin skill and any other skill both load; plugin skills are namespaced `plugin:skill`. | S | Harness precedence cannot give "project, then personal, then base". Plugin plus link install lists every skill twice. |
| 3 | Frontmatter fields are all optional: `name`, `description`, `when_to_use`, `allowed-tools`, `disallowed-tools`, `model`, `effort`, `context`, `agent`, `background`, `hooks`, `paths`, `shell`, `user-invocable`, `disable-model-invocation`, `arguments`, `argument-hint`, `metadata`, `license`. Unknown fields are ignored silently. Agent Skills limits: name 64 characters, description 1,024. | S, A | Current skills use `name` and `description` only; descriptions are 356–494 characters [V, measured]. |
| 4 | `` !`cmd` `` and ```` ```! ```` blocks run before the content reaches the model. A failing command aborts the invocation. Outside auto mode a command not allowed by permission rules aborts too, unless pre-approved in `allowed-tools`. `disableSkillShellExecution` replaces the output. | S | Dynamic context exists, but it makes Python and permissions a load-time dependency. |
| 5 | `${CLAUDE_SKILL_DIR}` is the skill's own directory, substituted in the Markdown body and in `allowed-tools` Bash rules; `${CLAUDE_PROJECT_DIR}` likewise. `${CLAUDE_PLUGIN_ROOT}` and `${CLAUDE_PLUGIN_DATA}` exist in plugin skills only. None is exported to Bash-tool commands. Skills may bundle scripts. | S, M | Portable self-reference exists; it replaces every absolute path. |
| 6 | The listing always holds every name. Descriptions are dropped, least-invoked first, beyond a budget of 1% of the context window; per-skill cap 1,536 characters. | S | The 22 descriptions total 10,118 characters [V]. Descriptions cannot be the only router. |
| 7 | Skill content is not re-read. After compaction the first 5,000 tokens of each skill are kept, 25,000 combined. | S | `SKILL.md` plus the fixed block must stay under 5,000 tokens. |
| 8 | The manifest is optional; `name` is the only required key. A `version` there pins users until the string changes. | M, L | The present `"version": "0.1.0"` [V] blocks updates unless bumped. |
| 9 | `.claude-plugin/marketplace.json` needs `name`, `owner`, `plugins`; each entry needs `name` and `source`. `"."` means the marketplace root. Relative sources resolve only for git or local marketplaces. | R, C | One repository can be both marketplace and plugin. |
| 10 | Install: `/plugin marketplace add owner/repo`, then `/plugin install name@marketplace` (or `claude plugin install`). Update: `claude plugin update name@marketplace`. Auto-update is off for third-party marketplaces. Version: manifest, then entry, then commit SHA. | I, H, L | Updates need a user action and a version change. |
| 11 | Marketplace plugins are copied to `~/.claude/plugins/cache/…/<version>/`; files outside the plugin are not copied; symlinks inside it are kept. | L, H | All shipped files must live inside the repository tree. |
| 12 | A folder with `.claude-plugin/plugin.json` under `~/.claude/skills/` loads in place as `name@skills-dir`, skills prefixed. | P, L | Cloning into `~/.claude/skills/cosmoskill` is a route; `git pull` updates it. |
| 13 | `${CLAUDE_PLUGIN_DATA}` is `~/.claude/plugins/data/<id>/`, kept across updates, deleted on uninstall. `userConfig` values (types include `directory`) go to `pluginConfigs` in `settings.json`; `${user_config.KEY}` is substituted in skill content; the dialog appears only on `/plugin` install. | M, P | Neither can hold a personal layer safely or under every route. |
| 14 | `claude plugin validate <path> --strict` checks manifest and skill frontmatter. | M, P | Acceptance check; local, not CI. |

Could not confirm: the unit behind "1% of the context window"; whether symlinked skill directories are officially supported (they work on the owner's machine [V]); whether substitutions apply in supporting files (the pages say "skill content"; I assume not [I]); whether `claude plugin validate` runs without login; how the model resolves a bare sibling name such as `cosmo-cmb` when the listing shows `cosmoskill:cosmo-cmb`.

## 2. Design changes recommended

1. **§5, layers are data, not skills.** State it. Fact 2 forbids using skill precedence for the order, so `layers.py` stays the mechanism.
2. **§5, keep the instruction form.** Do not inject `layers.py` with `` !`…` `` in domain skills: a missing `python3` or an unapproved command would abort a base skill (fact 4). Make the block conditional on `~/.cosmoskill/` or `./.cosmoskill/` existing. Try injection in Phase 2 for the hub and `cosmoskill-refine` only.
3. **§5–6, paths.** `SKILL.md` writes `${CLAUDE_SKILL_DIR}/…`; shipped scripts stay in `skills/observational-cosmology/scripts/`, the one place reachable under all routes; reference files use paths relative to the skill.
4. **§5, location.** Personal layer at `$COSMOSKILL_HOME`, default `~/.cosmoskill`. Not the plugin data directory, not `userConfig` (fact 13).
5. **§7, routes and names.** Three routes; skills are `cosmo-x` when linked and `cosmoskill:cosmo-x` under both plugin routes; install by one route only. A release bumps `version` in `plugin.json` only.
6. **§4, routing.** The hub's first sentence carries the routing; Phase 2 shortens descriptions against a trigger test (fact 6).
7. **§8, section keys move to Phase 2.** A v0 note attached by heading text would be orphaned when Phase 3 assigns keys, at the first base update. That contradicts aim 3. Assigning section keys needs no research.
8. **§8, split Phase 6.** 6a: missing domains. 6b: L3 for the rest, continuing after 1.0 (cost below).
9. **§8, subtopic lists belong to Phase 3.** Per-subtopic budgets need them before L3 does.

## 3. Phases

### Phase 1 — Generalise what exists
**Goal.** Remove everything tied to one person or machine and bring all content, hub included, under the checker. Make it installable by three routes and checked on every push.
**Work packages, all no research agent.** 1.1 lint script and tests. 1.2 fold the two hub PV files into `cosmo-peculiar-velocities`. 1.3 hub and domain text edits. 1.4 packaging, README, licences. 1.5 checker tests, snapshot, CI. 1.6 clean-account test (1 test).
**Deliverables.** Part 2 lists them.
**Hands on.** `tools/lint_generic.py`, `tools/check_structure.py`, `tools/clean_account.sh`, CI workflow, hub `sources.tsv`, route and naming rules, generalised `docs/agent-brief.md`.
**Acceptance.** Checklist in Part 2.
**Estimate.** 0 runs, 1 test; at most 1 window.
**Risks.** A number altered while moving 640 lines: move with `git mv`, edit citation form and pointer sentences only, compare numeric tokens before and after. Bare sibling names unresolved under the namespace: tested; fallback is one sentence in the hub. CI red from arXiv throttling: the push job uses a committed snapshot.
**Owner decisions.** Licences block the LICENSE files, the `license` field and the tag. The name blocks the marketplace name and the tag; a later rename breaks namespaces. The fσ8 pointer blocks one sentence.

### Phase 2 — Level router, section keys, layers v0
**Goal.** One fixed block in every skill tells the assistant how to choose a level and where personal notes are. Every attachable section gets a permanent key.
**Work packages, all no research agent.**
- 2.1 Keys: `<!-- key: skill:file:slug -->` under each `##` and `###`; `tools/assign_keys.py`; `tools/check_keys.py --against <tag>`; `references/retired-keys.tsv`.
- 2.2 Level rules in the hub; `tools/templates/fixed-block.md`; `tools/sync_blocks.py` writes it between markers; a "Levels" table per `SKILL.md` with measured tokens (`tools/measure_levels.py`).
- 2.3 `skills/observational-cosmology/scripts/layers.py`; `docs/layers-v0.md` (formats of `profile.md`, `notes.md`).
- 2.4 Shortened descriptions.
- 2.5 Question sets `docs/tests/levels/questions-<viewpoint>.md` from four viewpoints (outsider, same-probe analyst, other-probe analyst, referee), each question with expected level, file and token ceiling, written from the files.
- 2.6 Tests (3).
**Needs.** Phase 1 lint, CI, clean-account harness.
**Hands on.** Key format and stability check. `layers.py <skill> [--json]`: exits 0 always, prints existing layer files and profile settings. Answer footer `[cosmoskill L<n> · <layer> · <skill>/<file>#<key>]`.
**Acceptance.** (a) At least 80% of questions answered at the expected level with tokens of files read under the ceiling, measured from the transcript. (b) L1 questions answered without opening a reference file. (c) With a fixture layer, the note attached to a key appears labelled `personal`; with no layer directory, no command runs. (d) `check_keys.py` fails on a removed key; `sync_blocks.py --check` fails on a differing block. (e) Clean account: no listing-budget warning in the `--debug` log.
**Estimate.** 0 runs, 3 tests; 1 window.
**Risks.** Escalation to L2 by habit, because the file map invites loading: the block states a stop rule and test (a) measures it.
**Owner decisions.** Footer wording.

### Phase 3 — Contract v2 and even L2
**Goal.** Every headline number gets a claims row with a visible grade. Every domain meets one source rule, with classic references filled by rule.
**Work packages.**
- 3.1 no research agent: `docs/contract-v2.md` (claims schema, grades, flag-to-grade mapping, `references/subtopics.tsv`, source rule per subtopic, band as a floor).
- 3.2 no research agent: checker v2, fixtures, `docs/agent-brief-v2.md`.
- 3.3 no research agent: `tools/extract_claims.py` proposes rows from the "What an expert holds in mind" bullets and the current tables of `results.md`; `tools/grade_from_abstract.py` grades C, `verified_by=machine`, any value found verbatim in the arXiv abstract.
- 3.4 research agent, 2 runs, 450k tokens and 80 tool calls each: the two pilot domains. Subtopic list from two recent reviews and the collaborations' working-group lists; foundations pass; re-read at the locator of every headline number not machine-matched. Then re-estimate 3.5.
- 3.5 research agent, 19–28 runs: the other 19 domains, one at a time, gated in waves of five.
- 3.6 tests (5): per wave, checker, coordinator re-read of five random A/B claims per domain, one regression run on the existing 38 questions.
**Needs.** Keys. **Hands on.** Schema, grades, `subtopics.tsv`, brief v2, claim keys.
**Acceptance.** (a) `tools/check_headline_coverage.py`: every number in every L1 bullet maps to a graded row. (b) Checker v2 fails fixtures with a missing grade, a dangling source key, a duplicate key, a grade A without table or equation locator. (c) One mismatch in five re-read claims returns the domain to repair. (d) Every subtopic meets the source rule. (e) Regression answers unchanged or better. (f) No released key lost.
**Estimate.** 21–30 runs, 5 tests; 5–7 windows, fixed after 3.4.
**Risks.** Cost: pilot-first measurement, machine grading, hard budgets. Values differing between arXiv versions (67.24 became 67.19 in the first baseline [V]): the schema records the version read. Agents damaging verified prose: brief v2 allows edits to the TSV files and marked lines only.
**Owner decisions.** Pilot domains (they go first); grade threshold.

### Phase 4 — L3 pilot
**Goal.** Two domains get one dossier per subtopic that answers what L2 cannot. The pilot fixes the dossier contract and the cost per dossier.
**Work packages.**
- 4.1 no research agent: `docs/contract-l3.md`, `docs/agent-brief-l3.md`; template for `deep/<subtopic>.md` (scope, derivations with equation locators, body-level table citing claim keys, method variants, reading list by role, not verified); 5–15k tokens.
- 4.2 no research agent, with a human: 12 specialist questions per domain, written before the dossiers from `subtopics.tsv`.
- 4.3 research agent, 6–10 runs: two or three dossiers per run.
- 4.4 tests (4–6): memory-only baseline, L2-only run, L3 run.
- 4.5 human review against a rubric.
**Needs.** Phase 3 on the pilot domains only. **Hands on.** L3 contract, brief, measured cost per dossier.
**Acceptance.** (a) The L3 run answers at least 10 of 12 with locators, including at least 4 the L2-only run failed. (b) Every dossier number is a claims row graded A or B. (c) The reviewer marks no paragraph "textbook, uncited". (d) Sizes in band; an L3 question loads one dossier.
**Estimate.** 6–10 runs, 4–6 tests; 2–3 windows.
**Risks.** Dossiers restating L2: test (a). Subtopics mirroring the owner's interests: the list records its review source.
**Owner decisions.** Pilot domains; reviewer.

### Phase 5 — Layers v1 and refine workflows
**Goal.** Structured layers add or override claims by key. A base update never silently changes or orphans a refinement.
**Work packages, all no research agent.** 5.1 overlay semantics in `docs/layers-v1.md`. 5.2 `layers.py resolve`, `sync_layers.py`, `promote.py` in the hub scripts directory; `tools/make_release_manifest.py` writing `releases/<version>.tsv` (added, changed, superseded, retired keys); fixtures in `tests/fixtures/layers/`. 5.3 `skills/cosmoskill-refine/`. 5.4 tests (2).
**Needs.** Claims schema, keys, L3 contract; not the Phase 3 research. **Hands on.** Release manifest and contribution format.
**Acceptance.** (a) Fixture layer with the base moved one tag forward: every note and override resolves or is reported. (b) A base row changed under an override: `sync_layers.py` exits 3 and names the key. (c) `promote.py` on an entry under `private/` or without a public identifier exits non-zero and writes nothing. (d) A claim added by the workflow passes the checker with a locator. (e) An answer using an override shows both values, labelled.
**Estimate.** 0 runs, 2 tests; at most 1 window.
**Risks.** Hand-edited TSV: the same checker runs on layers.
**Owner decisions.** Whether project layers are committed in paper repositories by default.

### Phase 6 — Coverage
**Goal.** 6a adds the seven missing domains at L2 under contract v2. 6b extends L3 to the remaining domains.
**Work packages.**
- 6.1 no research agent: `docs/scopes-v2.md` (boundaries: photo-z against weak lensing, galaxy–halo against simulations, BBN against neutrinos, cosmic web and machine learning against beyond-two-point and statistics), router rows, descriptions within the listing budget.
- 6.2 research agent, 10–12 runs: seven domains at about 1.5 runs each.
- 6.3 tests (3): baseline and files-only run on a new question set.
- 6.4 research agent: L3 for 26 domains, about 8 dossiers each at 2–3 per run: 70–100 runs.
**Acceptance.** 6a: Phase 3 tests on the new domains; the hub routes one question per new domain correctly; no listing-budget warning. 6b, per domain: Phase 4 tests (a), (b), (d).
**Estimate.** 6a: 10–12 runs, 3 tests; 3 windows. 6b: 14–20 windows.
**Risks.** 6b dominates the programme: 1.0 ships without it. Contradictory numbers across overlapping skills: one claim key per number, siblings cite the key.
**Owner decisions.** Order of 6b by a neutral rule; whether some new domains merge into existing skills.

### Phase 7 — Release 1.0
**Work packages.** 7.1 no research agent: `CHANGELOG.md` from the manifests, `CONTRIBUTING.md`, `.github/ISSUE_TEMPLATE/number-error.yml` (contradicting source and locator required), `docs/refresh.md`, `scripts/new_since.py` (arXiv API by category and date). 7.2 research agent, 8–9 runs: refresh of 28 domains with the public procedure, since the October 2026 snapshot will be months old. 7.3 tests (5): all question sets on a clean account installed from GitHub. 7.4 no research agent: `claude plugin validate . --strict`, version bump.
**Acceptance.** (a) A session with public tools only finds the papers on a control list the owner prepares for two domains. (b) All question sets pass on the clean install. (c) Upgrade from the previous tag with a fixture layer passes the Phase 5 tests.
**Estimate.** 8–9 runs, 5 tests; 3 windows.
**Owner decisions.** Version policy; maintainers.

| Phase | Runs | Tests | Windows |
|---|---|---|---|
| 1 | 0 | 1 | ≤ 1 |
| 2 | 0 | 3 | 1 |
| 3 | 21–30 | 5 | 5–7 |
| 4 | 6–10 | 4–6 | 2–3 |
| 5 | 0 | 2 | ≤ 1 |
| 6a | 10–12 | 3 | 3 |
| 7 | 8–9 | 5 | 3 |
| To 1.0 | 45–61 | 23–25 | 16–19 |
| 6b | 70–100 | — | 14–20 |

## 4. Dependencies and the shortest path

```
P1 → P2 (keys, block, layers v0) → P3.1–3.3 (schema, checker)
                                      ├→ P3.4 pilot domains → P4 (L3 pilot)
                                      ├→ P5 (needs schema and L3 contract only)
                                      └→ P3.5 other 19 domains → P6a → P7 → 1.0
                                                                  P6b continues in 1.x
```

The design's order holds, with three adjustments: section keys in Phase 2; pilot domains first inside Phase 3, so Phase 4 does not wait for the other 19; Phase 6 split.

**Shortest honest release.** Phase 1 plus the licence and name decisions, tagged 0.2.0, in under one window. Its README states: L1 and L2 only, numbers verified by sample and often at abstract level, snapshot October 2026, uneven depth, seven domains absent, no layers. Since the repository is already public, this is a correction, not a launch.

## 5. Where the design is weak

- **Claims schema.** No columns for asymmetric errors, statistical and systematic split, one-sided limits and confidence level, units, effective redshift, the arXiv version read, or who verified (agent, machine, human). Vector results such as BAO tables and non-numeric claims have no form.
- **Flags and grades.** The mapping from `[src]`, `[sec]`, `[der]` to A–D is undefined; a derived number has no grade rule.
- **Key stability.** Nothing says who mints keys, how a rename is recorded, or what a base update may do. Proposed: a retired-keys registry and a CI check against the last tag.
- **Neutral L3 subtopics.** "Recent reviews and working groups" names no selection rule, count band or audit trail. Proposed: `subtopics.tsv` with the source of each entry.
- **Override semantics.** Add, override and suppress are not separated; the reader's view of a disagreement is unspecified (propose: both values, labelled). The profile's "default level" conflicts with "start at the lowest level".
- **Conflict detection.** It needs the base row's hash stored in the layer when the override is written, and a machine-readable release manifest. Neither is in the design.
- **L4 has no shipped tool beyond abstracts.** `fetch_abstracts.py` reads abstracts only [V]; "L4 is mandatory" needs a public way to read a section and a definition of L4 offline.
- **Source band against "caps never delete".** Weak lensing has 192 sources and Lyα 172 [V]; a band can only be a floor.
- **"No textbook-level filler"** is a human judgement with no rubric or named reviewer.
