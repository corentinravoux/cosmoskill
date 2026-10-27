# Anthropic directory listing Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Clear the four directory warnings and the two file holds, so that a version of cosmoskill is scanned without a policy hold and the listing gets an icon; release 1.0.3.

**Architecture:** The directory scans the *plugin folder*, the folder that holds `.claude-plugin/plugin.json`, and today that is the repository root: `docs/`, `tests/`, `tools/` and `releases/` are scanned with the skills. Move the plugin into `plugin/` (manifest, `skills/`, a short README, LICENSE, icon) and keep the development material at the root, outside the scan. The marketplace at the root points to `./plugin`, so installs in Claude Code and the Claude app keep the same skill names.

**Tech Stack:** Python 3 standard library (tools, tests with unittest/pytest), Pillow for the icon script only (in `tools/`, outside the plugin), git.

**Spec:** the directory's validation report (owner, 2026-10-27, four warnings quoted below) and https://claude.com/docs/plugins/pre-submission-checklist.md. No design doc; the requirements are in Global Constraints.

## What triggers each warning (measured on 213d4b8)

| # | Warning | Cause found | Cleared by |
|---|---|---|---|
| 1 | readable source instead of binaries or install-time downloads | `tests/fixtures/layers/empty/.keep` (empty file, not text); maybe `npx` in README | Task 1 (tests leave the plugin folder) |
| 2 | reads a credential and sends data | `docs/plans/2026-10-16-benchmark-plan.md` (`CLAUDE_CONFIG_DIR=$HOME/.claude-alt`, OAuth) next to the arXiv calls of the scripts; unrelated | Task 1 (docs leave the plugin folder) |
| 3 | no icon | missing `.claude-plugin/icon.png` | Task 3 |
| 4 | a launcher to ship as a script | `npx skills add …` in `README.md`; `pip install` lines in skill content are documentation | Task 2 (plugin README has no launcher); the skill lines stay |
| — | 578 files > 512; `docs/history/tests/gate-log.md`, `releases/1.0.0.tsv` > 256 KiB | development material | Task 1 (`plugin/` holds 419 + 5 files, largest 92 KB) |

The causes of 1 and 2 are inferred: the report does not name files. Task 4 re-validates and checks.

## Global Constraints

- Plugin folder `plugin/`: only `.claude-plugin/`, `skills/`, `README.md`, `LICENSE`; ≤ 512 files; every non-image file < 256 KiB; no empty file, no symlink, no binary except `.claude-plugin/icon.png`.
- Icon: square PNG, 512 to 2048 px a side, < 2 MB, at `plugin/.claude-plugin/icon.png`. The portal takes it **once**, at the first save or submit: the owner approves the image and the owner must not save a submission before it is pushed.
- Plugin `README.md`: ≥ 40 words outside code blocks; says what the scripts run and contact (arXiv hosts, cache paths); contains no `npx`, `uvx`, `pipx`, `pip install`, `curl`.
- Skill names, keys and content unchanged; `${CLAUDE_SKILL_DIR}` glob paths unchanged (they are sibling-relative).
- Standard library only in `plugin/`; Pillow only in `tools/make_icon.py`.
- Git: commit on `main`, push to `main`, no branch, no tag (owner tags on GitHub). Version 1.0.3 (1.1 is reserved for the benchmark).

## Review Focus

1. An existing Claude Code install updated after the move: `/plugin` must still list `cosmoskill:cosmo-cmb` etc., not lose the plugin because the marketplace `source` changed.
2. `tools/make_release_manifest.py --from <pre-move ref>` must compare `skills/` at that ref with `plugin/skills/` now, not report every section added and retired. Test in Task 1.
3. `tools/check_keys.py --against <pre-move ref>` (same issue, `git ls-tree … skills`). Test in Task 1.
4. People who linked `cosmoskill/skills/*` into `~/.claude/skills`: their links break on `git pull`. CHANGELOG and README say to relink from `plugin/skills/*`.
5. skills.sh: `npx skills add` must still find 30 skills through the root `marketplace.json` (or its recursive fallback). Checked in Task 4.

---

### Task 1: Move the plugin into `plugin/`

**Files:**
- Move: `skills/` → `plugin/skills/`; `.claude-plugin/plugin.json` → `plugin/.claude-plugin/plugin.json` (`git mv`)
- Copy: `LICENSE` → `plugin/LICENSE`
- Modify: `.claude-plugin/marketplace.json` (`"source": "./plugin"`)
- Modify: `tools/{assign_keys,check_keys,check_numbers,locate_numbers,make_release_manifest,refresh_status,sync_blocks}.py`, `tests/*.py` (every `ROOT / "skills"`), `plugin/skills/observational-cosmology/scripts/promote.py:137` (printed command)
- Create: `tools/layout.py`, `tests/test_layout.py`
- Test: `tests/test_layout.py`, `tests/test_release_manifest.py`, `tests/test_keys_and_blocks.py`

**Interfaces:**
- Produces: `tools/layout.py` with `PLUGIN = "plugin"`, `SKILLS = "plugin/skills"` (repo-relative strings) and `skills_dir_at(repo: Path, ref: str | None) -> str`: `"plugin/skills"`, or `"skills"` when `ref` names a commit without `plugin/skills` (pre-move). Every tool and test takes the skills path from here; temporary test repos build `plugin/skills/`.

- [ ] **Step 1: Write the failing tests** in `tests/test_layout.py`:
  - `test_plugin_folder_holds_only_the_plugin`: top entries of `git ls-files plugin` ⊆ `{".claude-plugin", "skills", "README.md", "LICENSE"}` and include `.claude-plugin`, `skills`, `LICENSE` (Task 2 adds `test_plugin_readme_exists`).
  - `test_plugin_folder_within_directory_limits`: `git ls-files plugin` count ≤ 512; every file other than `icon.png` is non-empty, decodes as UTF-8 and is < 262144 bytes; no symlink.
  - `test_marketplace_points_to_plugin`: `marketplace.json` plugin `source == "./plugin"`; `plugin/.claude-plugin/plugin.json` exists; no `plugin.json` at the root.
  - `test_license_copies_identical`: `plugin/LICENSE` bytes == `LICENSE` bytes.
  - In `tests/test_release_manifest.py`, `test_manifest_across_the_move`: temp repo, commit A with `skills/cosmo-x/...`, commit B with the same tree under `plugin/skills/`; manifest `--from A` has 0 added, 0 retired.
  - In `tests/test_keys_and_blocks.py`, `test_check_keys_against_pre_move_ref`: same two commits; `check_keys --against A` reports 0 problems.
- [ ] **Step 2: Run** `python3 -m pytest -q tests/test_layout.py tests/test_release_manifest.py tests/test_keys_and_blocks.py`. Expected: the new tests FAIL (`plugin/` missing, or `layout` not importable).
- [ ] **Step 3: Move and repoint.** `git mv` as listed; write `tools/layout.py`; replace each `"skills"` path in tools and tests with `layout.SKILLS` (tests: `ROOT / layout.SKILLS`); `make_release_manifest` and `check_keys` call `skills_dir_at` for the `--from` / `--against` ref; `promote.py` prints `verify_sources.py plugin/skills/<skill>` and `tests/test_promote.py:74` expects that. `layers.py` is unchanged (it finds the skills from its own path).
- [ ] **Step 4: Run** `python3 -m pytest -q` and `python3 tools/sync_blocks.py --check`, `python3 tools/check_keys.py`, `python3 tools/check_numbers.py`. Expected: all pass (98 + 6 tests), 0 stale blocks, 0 key problems.
- [ ] **Step 5: Commit** `layout: the plugin moves to plugin/; development material stays outside the directory scan`.

### Task 2: READMEs and contributor paths

**Files:**
- Create: `plugin/README.md`
- Modify: `README.md` (clone/link section, layout line, "What it runs and contacts" moves to the plugin README and is linked), `CONTRIBUTING.md:13,49,60` (paths)
- Test: `tests/test_layout.py`

- [ ] **Step 1: Write the failing tests:**
  - `test_plugin_readme_exists`: `plugin/README.md` is tracked.
  - `test_plugin_readme_long_enough`: words outside fenced code in `plugin/README.md` ≥ 40.
  - `test_plugin_readme_discloses_network`: contains `export.arxiv.org`, `arxiv.org`, `ar5iv.labs.arxiv.org`, `~/.cache/cosmo-skill-verify`.
  - `test_plugin_readme_has_no_launcher`: none of `npx `, `uvx `, `pipx `, `pip install`, `curl ` appears.
  - `test_root_readme_links_plugin_skills`: root `README.md` contains `cosmoskill/plugin/skills/*/` and not `cosmoskill/skills/*/`.
- [ ] **Step 2: Run** `python3 -m pytest -q tests/test_layout.py`. Expected: the five FAIL.
- [ ] **Step 3: Write.** `plugin/README.md` (about 60 lines): what the skills do (two sentences from the root README), the level table, install in the app and in Claude Code (no launcher), what each host can do, "What it runs and contacts" (moved from the root README), licence, link to the repository for the rest. Root README: drop the "clone into `~/.claude/skills/cosmoskill`" variant (it needs `skills/` at the root), link loop over `cosmoskill/plugin/skills/*/`, one line "The plugin is in `plugin/`; the rest of the repository is for maintainers"; the `npx skills add` section stays (outside the plugin folder).
- [ ] **Step 4: Run** `python3 -m pytest -q`. Expected: all pass.
- [ ] **Step 5: Commit** `docs: plugin README for the directory; README and CONTRIBUTING follow plugin/`.

### Task 3: Icon

**Files:**
- Create: `tools/make_icon.py`, `plugin/.claude-plugin/icon.png`
- Test: `tests/test_layout.py`

- [ ] **Step 1: Write the failing test** `test_icon_meets_directory_rules`: read the PNG header with the standard library (`struct` on the IHDR chunk): signature `\x89PNG`, width == height, 512 ≤ width ≤ 2048, file size < 2 000 000 bytes.
- [ ] **Step 2: Run** it. Expected: FAIL (file missing).
- [ ] **Step 3: `tools/make_icon.py`** writes a 1024 × 1024 PNG with Pillow, deterministic. Draft design (owner decides): deep-navy background `#0b1d3a`; a white circle outline (the sky); inside it one blue and one red dot moving apart (blueshift and redshift, a peculiar-velocity motif); no text (unreadable at 64 px).
- [ ] **Step 4: Owner check.** Show the PNG; adjust until approved. The portal keeps the first icon it sees: do not push before approval, and the owner does not save a submission before the push.
- [ ] **Step 5: Run** `python3 -m pytest -q`; commit `plugin: listing icon (tools/make_icon.py)`.

### Task 4: Release 1.0.3, checks, push

**Files:**
- Modify: `plugin/.claude-plugin/plugin.json` (`"version": "1.0.3"`), `README.md` (version line), `CHANGELOG.md`
- Create: `releases/1.0.3.tsv` (generated)

- [ ] **Step 1:** `python3 tools/make_release_manifest.py --from 213d4b8 --version 1.0.3`. Expected: 0 added, 0 changed, 0 moved, 0 retired (Review Focus 2 on real data).
- [ ] **Step 2:** CHANGELOG 1.0.3: layout moved to `plugin/`, why (directory scan), linked-skill users relink from `plugin/skills/*`, icon, plugin README; tests count.
- [ ] **Step 3: Checks.** `python3 -m pytest -q` (all pass); `claude plugin validate ./plugin` and `claude plugin validate .` (both `✔ Validation passed`; binary at `~/.vscode/extensions/anthropic.claude-code-*/resources/native-binary/claude`); in the scratchpad, `npx -y skills@latest add <repo path> --list` finds 30 skills. Review Focus 1: in a temporary `CLAUDE_CONFIG_DIR`, add the repo as a local marketplace, install, and list the skills: 30, named `cosmoskill:<skill>`.
- [ ] **Step 4: Commit and push** to `main`: `cosmoskill 1.0.3: plugin in plugin/ for the directory scan; icon; plugin README`.
- [ ] **Step 5: Owner, in the portal.** If a submission was already saved with the plugin path empty, delete the draft (its folder cannot be changed). **Submit new → Plugin bundle**, repository `corentinravoux/cosmoskill`, **Plugin path `plugin`**, branch `main` → **Validate**. Expected: warnings 1–4 and the file holds gone; any finding left is pasted back with the file it names.
