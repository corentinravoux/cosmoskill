# Optional MCP adapters: arXiv MCP and Valency

Date: 2026-11-10. Status: design, approved for planning once reviewed.
Base: cosmoskill 1.0.4 (`6f2e38d`).

## Intent

cosmoskill gives expert knowledge from a frozen snapshot (26 October 2026).
Two MCP servers can extend what it reaches outside itself:

- **arXiv MCP** (`arxiv-mcp-server`, local stdio server run by `uvx`): live
  arXiv search, PDF and LaTeX reading, search inside a paper, topic watches,
  and a citation graph through Semantic Scholar.
- **Valency** (remote connector, per-user account): a large indexed corpus
  (about 47M papers over 9 sources, arXiv included, up to a few days behind
  arXiv), semantic search over the whole corpus, forward citations from
  OpenAlex, author and trend analytics, journal and PubMed coverage.

The goal is to let cosmoskill use them when they are present, as **optional
adapters that switch off silently when absent**. The main gain is not in
day-to-day answers but in the maintenance loop: strengthening the base
(owner) and growing personal layers (every user) with `cosmoskill-refine`.

## Goals

1. When an adapter is present, cosmoskill uses it for the tasks where it is
   better than what cosmoskill has today, in a fixed order of preference.
2. When an adapter is absent or refuses (rate limit, error), cosmoskill
   behaves exactly as 1.0.4 does, and says nothing about the missing tool
   in its answers.
3. Day-to-day answers stay as cheap as today.
4. `cosmoskill-refine` gains an extension mode that uses both adapters to
   find, read and propose new material for a layer, on request only.
5. Any user can connect both adapters cleanly; arXiv MCP is marked as
   suggested, Valency as optional.

## Non-goals

- No bundling: neither server ships inside the plugin (no `.mcp.json` in
  cosmoskill). Reasons: it would force `uv` on every user, duplicate the
  server for users who already have arXiv MCP, complicate the Anthropic
  directory review, and do nothing in the Claude app.
- No automation: no scheduled runs, no hook, no alert that starts a run.
  Extension runs start only when the user asks.
- No benchmark work in this project. The benchmark plan
  (`docs/plans/2026-10-16-benchmark-plan.md`) stays as it is; adapter arms
  are added later, outside this design.
- No change to levels 1 to 3 beyond the per-skill sweep record (D9), none
  to the citation flags or to the `sources.tsv` columns, and none to the
  layer format beyond per-entry provenance, the user's sweep dates and the
  run's progress state (D8, D7).

## Anti-goals (a failure even if it works)

- A tool result treated as a source. A Valency abstract or an arXiv MCP
  search hit is a lead; `[src: <place>]` still means the paper was read at
  that place.
- An answer that gets more expensive by default because a tool is present.
- A user without Valency or arXiv MCP who gets a visibly weaker or noisier
  skill: nagging, error messages, or text about tools they do not have.
- A dossier or layer entry written with silent holes because a call was
  refused.

## Constraints

- Hosts: Claude Code (both adapters possible), Claude app (Valency possible
  as a connector, arXiv MCP not: local servers do not run there), other
  agents through `npx skills` (whatever MCP tools they expose).
- Tool names differ between installs. Here arXiv MCP tools are
  `mcp__plugin_arxiv-mcp-server_arxiv__<tool>` and Valency tools
  `mcp__claude_ai_Valency__<tool>`; elsewhere the prefix changes. In Claude
  Code the tools can also be deferred: listed by name only, loaded on demand
  with ToolSearch. Detection must therefore work on the **tool's own name**
  (the part after the prefix), among available or deferred tools:
  - arXiv MCP: `search_papers`, `read_paper`, `get_paper_latex`,
    `get_paper_latex_section`, `search_paper_text`, `citation_graph`,
    `watch_topic`, `check_alerts` (server 0.8.1).
  - Valency: `semantic_search_papers`, `search_by_title`,
    `get_citing_papers`, `find_similar_papers`, `get_paper_by_id`.
- arXiv MCP's `semantic_search` searches only papers already downloaded and
  needs the `[pro]` extra: not used for discovery.
- arXiv MCP `citation_graph` calls Semantic Scholar. Without a key
  (`SEMANTIC_SCHOLAR_API_KEY` in the server's environment) it is rate
  limited quickly and returns `status=rate_limited`. A free key exists
  (https://www.semanticscholar.org/product/api#api-key).
- Scripts stay standard-library Python; the adapters are used by the model
  through its tools, not by the scripts.
- The suite's existing rules hold: the release process, fingerprints in
  `releases/`, `CHANGELOG.md`, `docs/history/tests/gate-log.md`, and the git
  flow (straight to `main`, never tag).

## Decisions taken with the owner

### D1. Valency: essential for the owner, optional for users

Valency is the owner's main tool for strengthening the base. For users it is
optional but must connect cleanly and give its full benefit when present
(full adapter in the user-facing skills, not a one-line mention). If the
service disappears, users lose nothing; only the owner's maintenance loop
needs a replacement.

### D2. arXiv MCP: not bundled, marked as suggested

The README gets a "Suggested companions" section: arXiv MCP marked
**suggested**, Valency marked **optional**, each with its one-line install,
what it adds, and what it contacts. The Semantic Scholar key gets one line
there: recommended for heavy `cosmoskill-refine` use, optional otherwise.

### D3. Two modes with different budgets

**Day-to-day mode** is what cosmoskill already does (hub `SKILL.md`,
"Choosing the level"): lowest level that answers, L2 passages only, L4 with
`fetch_paper.py --grep/--section/--outline`. The adapters add only:

- at L4, arXiv MCP after `fetch_paper.py` fails (paper without HTML
  rendering, exit 2), before the web-tool fallback;
- routes for outward tasks that have none today (newer than the snapshot,
  citations, papers not on arXiv), with small calls: Valency with
  `include_abstract=false` and about 10 results, abstracts read only for the
  promising hits; no full-paper download unless the question requires it.

**Extension mode** is `cosmoskill-refine` building a layer (or the base, for
the owner). Thorough, token cost accepted: arXiv MCP first for reading (full
LaTeX, section by section), Valency for broad sweeps and citing papers,
arXiv MCP alerts as one of the inputs. The agent says it is entering this
mode before a long run.

### D4. Order of preference per task

Each row is tried left to right; an absent or refusing tool is skipped.

| Task | 1st | 2nd | 3rd | Last |
|---|---|---|---|---|
| Find papers on a topic | Valency semantic search | arXiv MCP `search_papers` | web search | the skills alone, stating the snapshot date |
| Papers of the last days | arXiv MCP (live) | Valency (lags) | web search | the snapshot, said explicitly |
| Who cites a paper | Valency `get_citing_papers` | arXiv MCP `citation_graph` | web search | none |
| What a paper cites | arXiv MCP `citation_graph` | its bibliography through `fetch_paper.py` | | |
| Papers not on arXiv | Valency | web search | | |
| Read a paper, day-to-day (L4) | `fetch_paper.py` | arXiv MCP (PDF, LaTeX) | web tool | "L4 required and not done" |
| Read a paper, extension mode | arXiv MCP | `fetch_paper.py` | web tool | entry under "Not verified" |
| New papers on a topic | arXiv MCP `check_alerts` on the user's existing watches | Valency date-filtered search | | |

Rules that go with the table (builder-check answers, author's calls):

- **No adapter at all: behaviour identical to 1.0.4.** The web-search column
  is used only after an adapter of the row was tried; a user with no
  adapter gets no new web searches. The L4 row keeps its 1.0.4 web-tool
  fallback.
- **What triggers an outward route in day-to-day mode:** only a question
  that explicitly asks for papers, citations, or what is new. A question
  whose subject may have moved since the snapshot (for example "current
  H0") is answered from the levels, with the date of the skill's last
  sweep (D9), as today.
- **Watches:** an extension run never creates a watch (`watch_topic`)
  without the user's explicit agreement in that conversation. `check_alerts`
  advances each watch's cursor, so it is called only with the topics of the
  skill being refined, never without a topic; the papers it returns are
  written to the run's progress state at once, so a stop cannot lose them.

### D5. When both are present

- Valency finds and ranks; arXiv MCP and `fetch_paper.py` read.
- Results are deduplicated on the arXiv identifier without version (Valency
  returns `2501.16852v2`).
- On a disagreement of metadata (version, date, title), live arXiv wins.
- Parallel search on both only for an exhaustive sweep (extension mode);
  otherwise the first present tool answers.

### D6. Silence in answers

An absent adapter is never mentioned in an answer, as with the thcosmoskill
bridge in 1.0.4. The adapters' state is shown only:

- when the user asks for it (a status check: "arXiv MCP: on · Valency: off ·
  reading: `fetch_paper.py`"), with the install hint for a suggested
  adapter that is off;
- at the start of an extension run, so the user knows what the run can
  reach.

(The trigger wording of the status check is the builder's call; see below.)

### D7. Rate limits

- Day-to-day: a refusing tool counts as absent for the rest of the answer;
  no retry loop (arXiv MCP already retries with backoff).
- Extension mode: a refusal is any failure of a tool (rate limit, timeout,
  authentication, server down). A refusing tool is skipped and the next
  tool of the D4 row is tried, as in day-to-day mode. The run **stops and
  resumes later** only when a step has no working tool left (for example:
  no reader can open a candidate paper). It then saves its progress in the
  layer (what was found, read and proposed, and what is left), tells the
  user which service refused and when to retry, and the next run on the
  same scope resumes from there. No entry is written from a partial check.
  (Author's call, from the owner's rule "stop and resume later" and the
  anti-goal "no silent holes": skipping to a working tool leaves no hole.)

### D8. Extension run, on request only

1. The user asks (for example "refine my peculiar-velocities layer").
2. `cosmoskill-refine` shows the adapters' state and enters extension mode.
3. It gathers candidates newer than the later of the skill's sweep date
   (D9) and the user's own last sweep of that skill (kept in the layer):
   arXiv MCP alerts on the skill's topics if the user has watches, Valency
   search, and citing papers of the skill's key sources.
4. It ranks them against the existing dossiers and reference sections.
5. It reads the relevant ones (D4, extension row).
6. It proposes entries one at a time for the user to accept. Any kind of
   entry may be proposed (`source`, `note`, dossier content, `override`); an
   override is shown beside the base value it replaces, with both sources.
   Each entry carries its `[src: <place>]` and, in the layer, its
   provenance ("found via Valency", "found via arXiv MCP", "found via web
   search"). Accepted entries are written with the existing `layers.py`
   commands; a paper without an arXiv identifier enters with `doi:<doi>` as
   today.
7. At the end, the run records in the layer the date up to which the skill
   was swept and with which adapters.

Abstracts (author's call): an abstract served by Valency is a lead. For an
arXiv paper the abstract is read again from arXiv
(`fetch_paper.py --abstract`, several identifiers in one call) before it
earns `[src: abstract]`. For a paper not on arXiv, the Valency record
(journal or PubMed abstract) is cited as `[sec: Valency record, <id>]` until
the paper itself is read.

### D9. Owner route and the base's sweep record

**Route (owner's decision): A.** The owner strengthens the base by running
`cosmoskill-refine` in extension mode on their own personal layer, then
moving entries into the base with `promote.py` and folding the proposals in
by hand through the existing "Refreshing a domain" cycle of
`suite-conventions.md`. One flow serves the owner and the users, and every
maintenance run exercises the personal-layer machinery. Only this flow is
wired to the adapters; the refresh cycle keeps its step 2 as it is.

**What the base keeps (owner's decision): a per-skill sweep record, no
per-source provenance.** Each domain skill states the date up to which it
was swept and with which adapters (for example "swept with Valency and arXiv
MCP up to 2026-11-10"). `sources.tsv` does not change: provenance stays in
the owner's layer. The sweep record is used to:

- start users' extension runs from that date instead of the global snapshot
  date, so they cost fewer tokens;
- let answers say how current a skill is ("current to <date>") instead of
  the global snapshot date.

A skill never swept keeps the global snapshot date (26 October 2026).

### D10. Contacts

`plugin/README.md` ("What it runs and contacts") and the README state, per
adapter, what leaves the machine: with Valency, search queries and paper
identifiers go to Valency; with arXiv MCP, queries and identifiers go to
arXiv, and `citation_graph` sends identifiers to Semantic Scholar. The
existing sentence "Only arXiv identifiers are sent" is qualified: it stays
true for the scripts, not for the adapters.

## What changes, by file (expected)

- `plugin/skills/observational-cosmology/SKILL.md`: an adapters section
  (detection, D4 table, D5, D6, D7 day-to-day), the L4 paragraph extended
  with the arXiv MCP step.
- Every domain `SKILL.md` that repeats the L4 instruction: the same step,
  kept to one line, pointing to the hub section.
- `plugin/skills/cosmoskill-refine/SKILL.md`: extension mode (D3, D7, D8).
- `README.md`, `plugin/README.md`: suggested companions (D2), host table,
  contacts (D10).
- `references/suite-conventions.md`: the owner's route A (D9) and how a
  sweep record is updated when proposals are folded in.
- Each domain skill: its sweep record (D9), read by answers and by
  extension runs.
- `layers.py` / layer format: the user's per-skill sweep date, the run's
  progress state, and per-entry provenance (D8). `sources.tsv` columns do
  not change.
- `CHANGELOG.md`, `releases/`, version bump, gate log: as for any release.

## Left to the builder

- Wording of the adapters section and of the status-check trigger.
- Where and in what format the resume state of an extension run is stored
  (inside the layer, readable by the user, ignored by `layers.py check`).
- How per-entry provenance is recorded in the layer (D8), without changing
  the `sources.tsv` columns; it must survive `sync_layers.py`.
- Where and in what format the base's sweep record lives (a line in each
  domain `SKILL.md`, a reference section, or one file for the suite), and
  whether `promote.py` updates it or the owner does by hand; it must be
  covered by the release fingerprints.
- The exact size limits of day-to-day calls.
- How to test: at least one run per host type with no adapter (behaviour
  identical to 1.0.4), one with arXiv MCP only, one with both, and one with
  a forced rate limit in extension mode. These are checks of the design,
  not the benchmark.
- Version number of the release.
