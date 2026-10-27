# cosmoskill in the Claude app — implementation plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** The same repository installs and works as a plugin in Claude Code and in the Claude app; release 1.0.1.

**Architecture:** Three changes to the single source. The scripts stop at once when arXiv cannot be reached. The generated "Levels and layers" block (and the few hand-written lines like it) uses a path that tolerates the app's `cosmoskill:` folder prefix and an unexpanded `${CLAUDE_SKILL_DIR}`, and states the L4 fallback order. The README and manifests describe both hosts.

**Tech Stack:** Python ≥ 3.9 standard library, `unittest` run through `pytest`, bash glob expansion.

**Spec:** `docs/specs/2026-10-27-claude-app-design.md`

## Global Constraints

- Scripts: standard library only, Python 3.9+.
- No change to L1–L3 content, section keys, numbers, bibliographies.
- Blocks are never edited by hand: edit `tools/templates/fixed-block.md`, then run `python3 tools/sync_blocks.py`.
- Path form, verbatim: `"${CLAUDE_SKILL_DIR}"/../*observational-cosmology/scripts/<script>.py`
- Exit code 3 means "arXiv cannot be reached from this machine"; 2 keeps its meaning (API unreachable after retries or rate-limited).
- The owner pushes and makes the GitHub release; the executor commits and tags locally only after the owner approves the plan.
- Gates of each task are appended to `docs/history/tests/gate-log.md` under a heading `### Claude app support (1.0.1)`.

## Review Focus

1. Hub skill turned off in the app (glob matches nothing): bash leaves the pattern literal and `python3` fails with "No such file or directory". Expected: the model says L4 was required and not done. Covered by the block copy ("if the script cannot run"), and by `test_unmatched_glob_fails_loudly` in Task 2.
2. Claude Code path with a space (route C clone in a folder with a space): the quoted part must keep it whole. Covered by the temporary directory name `with space` in Task 2's resolution test.
3. An egress proxy that answers HTTP 403 instead of failing DNS: treated as unreachable, no retry. Test `test_proxy_403_is_unreachable` in Task 1.
4. A real slow or rate-limited arXiv (timeout, 429, 503) must still retry as today. Test `test_a_timeout_still_retries` in Task 1.
5. Researchers with layer entries attached to `levels-and-layers`: its fingerprint changes in every skill, so `sync_layers.py` reports those entries after the update. Named in the CHANGELOG entry (Task 3); `releases/1.0.1.tsv` lists the change.

---

### Task 1: Stop at once when arXiv cannot be reached

**Files:**
- Modify: `skills/observational-cosmology/scripts/verify_sources.py` (add `unreachable`, use it in `query`, lines 133–152)
- Modify: `skills/observational-cosmology/scripts/fetch_paper.py` (import `unreachable`; use it in `download`, lines 117–148, and `abstracts`, lines 151–167)
- Test: `tests/test_network.py` (new)

**Interfaces:**
- Produces: `verify_sources.unreachable(error: BaseException) -> bool`. True when `error` is `urllib.error.HTTPError` with code 403, or `urllib.error.URLError` whose `reason` is `socket.gaierror`, `ConnectionRefusedError`, or an `OSError` with `errno` in `{errno.ENETUNREACH, errno.EHOSTUNREACH}`. False otherwise (timeouts included).
- Produces: exit code 3 from `fetch_paper.py` (`abstracts` returns 3; `download` raises `SystemExit(3)`) and from `verify_sources.py` (`query` raises `SystemExit(3)`), each after one stderr message.
- `fetch_paper.py` imports it the way `layers.py` does: `sys.path.insert(0, str(Path(__file__).resolve().parent))`, then `from verify_sources import unreachable`.

- [ ] **Step 1: Write the failing tests** in `tests/test_network.py`, loading both scripts with `importlib` as `tests/test_fetch_paper.py` does. Raise errors from a patched `module.urllib.request.urlopen`; record `module.time.sleep` calls with `unittest.mock.patch.object`; point `fetch_paper.CACHE` at a temporary directory.

```python
DNS = urllib.error.URLError(socket.gaierror(-2, "Name or service not known"))

def test_dns_failure_is_unreachable(self):
    self.assertTrue(verify.unreachable(DNS))
def test_proxy_403_is_unreachable(self):
    self.assertTrue(verify.unreachable(urllib.error.HTTPError("u", 403, "Forbidden", {}, None)))
def test_timeout_is_not_unreachable(self):
    self.assertFalse(verify.unreachable(TimeoutError()))
    self.assertFalse(verify.unreachable(urllib.error.URLError(TimeoutError())))
def test_abstracts_stop_at_once_without_network(self):
    # urlopen raises DNS
    self.assertEqual(fetch.abstracts(["1807.06209"]), 3)
    self.assertEqual(sleeps, [])
    self.assertIn("https://arxiv.org/abs/1807.06209", stderr)
def test_download_stops_at_once_without_network(self):
    with self.assertRaises(SystemExit) as caught:
        fetch.download("1807.06209", refresh=True)
    self.assertEqual(caught.exception.code, 3)
    self.assertEqual(sleeps, [])
def test_query_stops_at_once_without_network(self):
    with self.assertRaises(SystemExit) as caught:
        verify.query(["1807.06209"])
    self.assertEqual(caught.exception.code, 3)
    self.assertEqual(sleeps, [])
def test_a_timeout_still_retries(self):
    # fetch.ATTEMPTS patched to 1; urlopen raises TimeoutError
    self.assertEqual(fetch.abstracts(["1807.06209"]), 2)
    self.assertEqual(len(sleeps), 3)   # range(ATTEMPTS + 2)
```

- [ ] **Step 2: Run them to see them fail**

Run: `python3 -m pytest tests/test_network.py -q`
Expected: FAIL, `AttributeError: module 'verify_sources' has no attribute 'unreachable'`.

- [ ] **Step 3: Implement `unreachable`** in `verify_sources.py` (add `import errno`, `import socket`). In `query`, before the backoff: if `unreachable(error)`, print the message below and `raise SystemExit(3)`.

Message, `verify_sources.py`:
`arXiv cannot be reached from this machine ({error}); do not retry. Use --offline for the local checks only.`

- [ ] **Step 4: Use it in `fetch_paper.py`.** In `download`, catch `HTTPError` 403 and `URLError` through `unreachable` before the existing handlers; on the first unreachable source, try the next source without sleeping; if every source is unreachable, print the message and `raise SystemExit(3)`. In `abstracts`, on the first unreachable error print the message and `return 3`.

Message, `fetch_paper.py`, one line per identifier:
`arXiv cannot be reached from this machine ({error}); do not retry. Read https://arxiv.org/abs/{id} with a web tool if you have one; otherwise say that L4 was required and not done.`

- [ ] **Step 5: Run the tests to see them pass**

Run: `python3 -m pytest -q`
Expected: 90 passed (83 existing + 7 new).

- [ ] **Step 6: Commit**

```bash
git add tests/test_network.py skills/observational-cosmology/scripts/verify_sources.py skills/observational-cosmology/scripts/fetch_paper.py
git commit -m "scripts: stop at once when arXiv cannot be reached (exit 3)"
```

---

### Task 2: Paths and the L4 fallback that work in both hosts

**Files:**
- Modify: `tools/templates/fixed-block.md` (the L4 bullet and the layers command)
- Regenerate: the block of all 29 skills with references (`python3 tools/sync_blocks.py`)
- Modify: `skills/observational-cosmology/SKILL.md` lines 69–74 (script list) and 100–104 (the "L4 is mandatory" bullet)
- Modify: `skills/cosmoskill-refine/SKILL.md` line 14
- Test: `tests/test_script_paths.py` (new)

**Interfaces:**
- Consumes: exit code 3 and its message from Task 1 (the block copy names it as "reports that arXiv cannot be reached").

- [ ] **Step 1: Write the failing tests** in `tests/test_script_paths.py`.

```python
def test_no_file_uses_the_unprefixed_sibling_path(self):
    # every skills/*/SKILL.md and skills/observational-cosmology/references/*.md
    self.assertNotIn("/../observational-cosmology/", text)
def test_every_block_states_the_unexpanded_rule(self):
    # every SKILL.md that has a generated block
    self.assertIn("reaches you unexpanded", block)
def test_the_path_resolves_with_and_without_the_plugin_prefix(self):
    # for prefix in ("", "cosmoskill:"), under a temporary dir named "with space":
    # make <prefix>cosmo-cmb/ and <prefix>observational-cosmology/scripts/fetch_paper.py,
    # take the fetch_paper.py command from the real skills/cosmo-cmb/SKILL.md,
    # replace ${CLAUDE_SKILL_DIR} by the temporary <prefix>cosmo-cmb path,
    # run: bash -c 'ls -d <path expression>'
    self.assertEqual(result.returncode, 0)
    self.assertTrue(result.stdout.strip().endswith("scripts/fetch_paper.py"))
def test_unmatched_glob_fails_loudly(self):
    # same, with no hub folder: bash -c 'python3 <path expression> --help'
    self.assertNotEqual(result.returncode, 0)
```

- [ ] **Step 2: Run them to see them fail**

Run: `python3 -m pytest tests/test_script_paths.py -q`
Expected: FAIL on the first two tests (old path, sentence absent); the resolution test fails for the `cosmoskill:` prefix.

- [ ] **Step 3: Edit `tools/templates/fixed-block.md`.** Replace the L4 bullet by this copy, verbatim:

```markdown
- L4 starts from the L2 entry: its citation and flag say where to look. Read
  the paper with
  `python3 "${CLAUDE_SKILL_DIR}"/../*observational-cosmology/scripts/fetch_paper.py <arXiv id>`
  (`--abstract`, `--outline`, `--section`, `--grep`). `${CLAUDE_SKILL_DIR}` is
  the folder of this file; if it reaches you unexpanded, write that folder's
  path in its place. If the script cannot run, or reports that arXiv cannot
  be reached, do not run it again: read `https://arxiv.org/abs/<id>` or
  `https://arxiv.org/html/<id>` with a web tool if you have one. If the paper
  cannot be read, say that L4 was required and not done; never give its
  content from memory.
```

In the "Local layers" paragraph, change the command to
`python3 "${CLAUDE_SKILL_DIR}"/../*observational-cosmology/scripts/layers.py {skill}`.

- [ ] **Step 4: Regenerate the blocks**

Run: `python3 tools/sync_blocks.py && python3 tools/sync_blocks.py --check`
Expected: 29 blocks written; then exit 0, 0 stale.

- [ ] **Step 5: Hand edits.**
  - Hub `SKILL.md`, before the line `- ${CLAUDE_SKILL_DIR}/scripts/verify_sources.py ...` (69), add the line: `` In the lines below, `${CLAUDE_SKILL_DIR}` is the folder of this file; if it reaches you unexpanded, write that folder's path in its place. ``
  - Hub `SKILL.md`, "L4 is mandatory" bullet (100–104): replace "or with any tool that gives the paper. If it cannot be read, say that L4 was required and not done" by the fallback of Step 3 ("If the script cannot run … never give its content from memory").
  - `cosmoskill-refine/SKILL.md` line 14: the path form of the Global Constraints, with `layers.py`.

- [ ] **Step 6: Run every gate**

Run: `python3 -m pytest -q && python3 tools/check_keys.py && python3 tools/check_numbers.py && claude plugin validate .`
Expected: 94 passed; 0 key problems; check_numbers 0 without paper and place, 0 derived (as at 1.0.0); validate passes.

- [ ] **Step 7: Commit**

```bash
git add tools/templates/fixed-block.md skills tests/test_script_paths.py
git commit -m "skills: script paths and L4 fallback that work in Claude Code and the Claude app"
```

---

### Task 3: README, manifests, release 1.0.1, check in the app

**Files:**
- Modify: `README.md` "## Installing" (lines 223–258)
- Modify: `.claude-plugin/plugin.json` (`"version": "1.0.1"`), `.claude-plugin/marketplace.json` (description)
- Modify: `skills/cosmoskill-refine/SKILL.md` (description)
- Modify: `CHANGELOG.md`, `docs/history/tests/gate-log.md`
- Create: `releases/1.0.1.tsv` (generated)

- [ ] **Step 1: README.** Change "Three routes" to "Four routes"; keep A–C; add route D after C:
  - **D. In the Claude app (web, Desktop, Cowork), paid plan.** Personnaliser (Customize) → Plugins → Ajouter (Add) → Ajouter une place de marché (Add marketplace) → Ajouter à partir d'un référentiel (Add from a repository) → `corentinravoux/cosmoskill` → install `cosmoskill`. Requires code execution: Paramètres → Capacités → « Créer et modifier des fichiers » (Settings → Capabilities → Create and edit files); on a Team or Enterprise account, the owner enables it under Organization settings → Plugins & skills → Policy.
  - L4 in the app: the sandbox cannot reach arXiv by default. Either turn on web search in the chat, or have the allowed domains extended with `arxiv.org`, `export.arxiv.org`, `ar5iv.labs.arxiv.org`. Without either, the skills answer at L1–L3 and say when L4 was required.
  - Not in the app: layers and `cosmoskill-refine` (no persistent home directory).
  - Both hosts on one account: Claude Code 2.1.273+ also loads the plugins of the Claude account it is signed in with. Use route D or route A, not both; or keep route A and set `"syncClaudeAiSkills": false` in Claude Code's settings.
- [ ] **Step 2: Manifests and refine.** `marketplace.json` description: "Observational-cosmology reference skills for Claude Code and the Claude app: …" (rest unchanged). `plugin.json` version `1.0.1`. `cosmoskill-refine` description: append " Claude Code only: needs a persistent home directory."
- [ ] **Step 3: Release manifest**

Run: `python3 tools/make_release_manifest.py --from v1.0.0 --version 1.0.1`
Expected: `releases/1.0.1.tsv`; changes only `levels-and-layers` (29 rows, `changed`) and the hub section that holds the script list and L4 bullet; no `retired`.

- [ ] **Step 4: CHANGELOG** `## 1.0.1 — <date>`: Claude app support (route D); script paths tolerate the `cosmoskill:` prefix and an unexpanded `${CLAUDE_SKILL_DIR}`; L4 fallback order; scripts exit 3 at once without network; `levels-and-layers` changed in every skill, so `sync_layers.py` reports layer entries attached to it.
- [ ] **Step 5: Gates again** (Task 2 Step 6 command) and log them in `gate-log.md`.
- [ ] **Step 6: Commit and tag locally**

```bash
git add README.md CHANGELOG.md .claude-plugin skills/cosmoskill-refine/SKILL.md releases/1.0.1.tsv docs
git commit -m "cosmoskill 1.0.1: Claude app support"
git tag -a v1.0.1 -m "cosmoskill 1.0.1"
```

- [ ] **Step 7: Owner** pushes `main`, `v1.0.0` and `v1.0.1`, then updates the plugin in the app (Personnaliser → Plugins → cosmoskill → update) and in Claude Code (`claude plugin update cosmoskill@cosmoskill`).
- [ ] **Step 8: Check in the app.** New chat, same test prompt as on 2026-10-27, plus: "Use cosmo-cmb: what is the Planck 2018 H0, and read it at L4." Expected: the hub's scripts found through the glob; `fetch_paper.py` exits 3 at once with the message (no 75 s wait); with web search off, the answer names L4 as required and not done; with web search on, the abstract of 1807.06209 is read. Log the result in `gate-log.md`.
