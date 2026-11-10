# Adapter scenarios, release 1.1 (2026-11-10)

Design checks of the optional adapters (spec `docs/specs/2026-11-10-mcp-adapters-design.md`,
plan `docs/plans/2026-11-10-release-1.1-adapters.md`, Task 10). They are not the benchmark.

## Set-up

Claude Code 2.1.322, headless, alt account, one scenario at a time:

```
CLAUDE_CONFIG_DIR=$HOME/.claude-alt CLAUDE_CODE_DISABLE_CLAUDE_MDS=1 CLAUDE_CODE_DISABLE_AUTO_MEMORY=1 \
COSMOSKILL_HOME=<fresh directory per scenario> \
claude --print --model claude-opus-5-5 --output-format stream-json --verbose --no-session-persistence \
  --setting-sources project --permission-mode dontAsk --max-budget-usd 5 \
  --plugin-dir <repo>/plugin <adapter and tool options> -- "<prompt>" < /dev/null
```

cwd: an empty scratch directory. Streams kept in the session scratchpad, not in the
repository. Differences from the plan, each a ruling in the run's ledger:

- Skills were loaded from the working tree with `--plugin-dir <repo>/plugin`; the init event
  listed the plugin `cosmoskill@inline` from the working tree and no other copy.
- `Bash(python3:*)` does not match commands such as `cd <dir> && python3 ...`, so from C2 on
  `Bash` was allowed whole (scratch directories only).
- arXiv MCP: `uvx arxiv-mcp-server`, then from C2 on `uvx --from "arxiv-mcp-server[pdf]"
  arxiv-mcp-server` (see C), with `--storage-path` set to a scratch directory for E and F, so
  that `check_alerts` never touched the owner's own watches. The store was seeded with two
  watches: `peculiar velocities` (astro-ph.CO) and `exoplanet atmospheres` (astro-ph.EP), the
  second to check that a run calls `check_alerts` only on its skill's topic.
- **Valency could not be loaded headless on the alt account**: the init event listed only the
  claude.ai connectors Claude Docs and Google Drive. D (both adapters) was not run. E ran with
  arXiv MCP only. D and E with Valency are left to the owner, interactively, on the main account.

Cost of the runs: 8.5 USD in total (A 0.40, B 0.43 + 0.21, C 0.32 + 0.41, E 1.01 + 1.04 + 1.13 + 1.15,
F 0.12 + 0.42 + 1.47, two smoke runs 0.39) <!-- num: not a value -->.

## Results

| # | Adapters | Result |
|---|---|---|
| A | none | pass |
| B | none | fail, fixed, pass on re-run |
| C | arXiv MCP only | pass (C2, with the `[pdf]` extra) |
| D | both | not run: Valency not available headless |
| E | arXiv MCP only (substitute for "both") | partial: every criterion passes except the announcement |
| F | arXiv MCP refusing | pass, and the resumed run passes |

### A — no adapter

Prompt: "What is the DESI DR2 BAO constraint on Ωm in ΛCDM? Use the cosmoskill skills."
Options: `--strict-mcp-config --disallowedTools "mcp__*"`, WebSearch and WebFetch allowed.

- Answered from L1: `[cosmoskill L1 · base · cosmo-galaxy-clustering/skill#what-an-expert-holds-in-mind]`. Pass.
- No web search and no web fetch in the transcript. Pass.
- The final text contains none of `Valency`, `arXiv MCP`, `MCP`. Pass.

### B — status, no adapter

Prompt: "cosmoskill status: which tools can it use?"

- First run: no skill loaded; the answer described the plugin's permissions. Fail. Cause: nothing
  in a skill description routed a status question. Fix (`fix(hub): route the status check from the
  hub description`): the hub description now ends "and when asked which tools or adapters
  cosmoskill can use (its status)"; test `test_hub_description_routes_the_status_check`, failing
  first, then passing; suite 154 OK.
- Re-run: hub loaded, `references/adapters.md` read, answer starts with
  "`arXiv MCP: off (suggested) · Valency: off (optional) · reading: fetch_paper.py`", then both
  install lines; footer `[cosmoskill L2 · base · observational-cosmology/adapters#silence-and-the-status-check]`. Pass.

### C — arXiv MCP only, a paper without an HTML rendering

arXiv:2509.20100 (Wang and Chen, a satellite-control paper, chosen because `fetch_paper.py` exits
2 on it: "no HTML rendering could be read for 2509.20100"). Prompt: "Following the cosmoskill L4
procedure, read arXiv:2509.20100 and quote one numerical value stated in its numerical-examples
section, with the place you read it."

- First run: Bash refused by the permission pattern (set-up issue above), so the model went to the
  web tool, then to `list_paper_latex_sections` ("arXiv response is not a supported source
  archive": the paper has no TeX source) and `download_paper` ("PDF conversion requires the pdf
  extra"). It stopped with "L4 (required, not done)" and quoted nothing. Correct behaviour, but
  the route was not exercised.
- C2, with Bash allowed and the `[pdf]` extra: `fetch_paper.py --outline` first (exit 2), then
  `list_paper_latex_sections` (refused, no TeX source), then `download_paper` and `read_paper`.
  Quoted "A total of 200 trajectories ... 150 data sets are used for training, and the remaining
  50 data sets are used for validation" with "Section 4 ... subsection 4.1". Pass.
- Finding: a paper that arXiv holds only as PDF is readable by arXiv MCP only with its `[pdf]`
  extra. Recorded in the README's companion section.

### D — both adapters

Not run (Valency not loaded headless on the alt account). To run by the owner: "Which papers since
the peculiar-velocities sweep date cite arXiv:2501.16852? Use cosmoskill." Pass when Valency
`get_citing_papers` is called (with `include_abstract=false` or a small limit) before any arXiv MCP
`citation_graph`, and identifiers are deduplicated without their version.

### E — extension run (arXiv MCP only)

Prompt: "Refine my peculiar-velocities layer from the recent literature." Headless, so the run ends
at its first proposal; the two rejections of the plan could not be given.

| Criterion | E | E2 | E3 | E4 |
|---|---|---|---|---|
| extension run announced, status line and start date in the reply | fail | fail | fail (start date only) | fail |
| `_progress.md` created, candidates with `Found via` | pass | pass | pass | pass |
| `check_alerts` only on `peculiar velocities`, alerts written at once | pass | pass | pass | pass |
| the `exoplanet atmospheres` watch untouched | pass | pass | pass | pass |
| no `watch_topic` call | pass | pass | pass | pass |
| no entry written (layer holds `_progress.md` only) | pass | pass | pass | pass |
| proposal marked `proposed` in the file | fail | pass | pass | pass |

Changes between runs (`fix(refine): announce the extension run first; mark proposals in the
progress file`): step 1 asks for the line `Extension run on <skill>. <status line>. Start date:
<date>.` before any search, or at the top of the first reply; step 6 sets `proposed` before
asking; `layers.py progress` prints "Tell the researcher, before any search: Extension run on
<skill>. <status line of adapters.md>. Start date: <date>." Tests
`test_announcement_comes_first_and_proposals_are_marked` and
`test_progress_prints_the_announcement_to_give`, each failing first. Every run read
`adapters.md` and ran `layers.py sweep` and `layers.py progress`. In `--print` mode the model sends
no message before its first tool call and its final reply starts with the proposal, so the
announcement is still missing in E4. Open: to check in an interactive session.

E's first proposal, for the record: arXiv:2611.04830 (DESI DR1 BGS velocity reconstruction compared
with Cosmicflows-4 groups), read in its LaTeX Sects. 6.5 and 6.6.

### F — refusal, then resume

F1: arXiv MCP with `HTTPS_PROXY`/`HTTP_PROXY` set to `http://127.0.0.1:9` in its environment,
Valency absent, `--disallowedTools "Bash(python3 *fetch_paper.py*)" "Bash(*fetch_paper.py*)"
WebFetch WebSearch`. Check first: a one-line `fetch_paper.py` call was refused ("Permission to use
Bash with command python3 .../fetch_paper.py 2501.16852 --abstract has been denied"). Same prompt
as E.

- `search_papers` (twice) and `check_alerts` refused: "Could not connect to arXiv after 3
  attempts". No tool left for the gathering step, so the run stopped there. With no search
  working, it could not reach the reading step that the plan named; it stopped at the first step
  that had no tool. Pass.
- `Stopped:` filled ("arXiv MCP refused (search_papers x2 and check_alerts ...); Valency absent; no
  web-search tool in session. Retry when arXiv is reachable"), `## Left to do` filled. The
  researcher was told which service failed and when to retry. Pass.
- Nothing in `notes.md`, `sources.tsv` or `found-via.tsv`: the layer holds `_progress.md` only.
  The watch cursor did not move. Pass.

F2: same layer, arXiv MCP without the proxy, `fetch_paper.py` and the web tools allowed.

- `layers.py progress` printed `paused run:`; the run resumed from the file and finished
  gathering. Pass.
- `citation_graph` worked for two key sources, then hit Semantic Scholar's rate limit; the run
  treated it as a refusal, put the five sources still unchecked under "Left to do", and went on
  with the steps that had a tool. Pass.
- Its first proposal marked `proposed` in the file; no layer entry written. Pass.

## Open for the owner

1. D, and E with both adapters, interactively on the main account (Valency connected).
2. E's announcement line in an interactive session.
