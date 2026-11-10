# Adapters: tools beyond the skills

Read this file only for an outward task: a question that asks for papers
newer than a skill's sweep date, for the papers that cite a given paper, or
for papers not on arXiv; a paper that `fetch_paper.py` cannot read; an
extension run of `cosmoskill-refine`; or a status request. A question that
the levels answer does not open it.

Two MCP servers are adapters of the suite: arXiv MCP (`arxiv-mcp-server`)
and Valency. Both are optional. Without them the suite works as it always
has, and an answer never mentions them.

## Detecting the adapters
<!-- key: detecting-the-adapters -->

An adapter is present when its tools are among your tools, loaded or
deferred (in Claude Code a deferred tool is listed by name only and loaded
on demand with ToolSearch). The prefix of a tool's name changes from one
install to another: match on the part after the last `__`.

- arXiv MCP: `search_papers`, `read_paper`, `download_paper`,
  `get_paper_latex`, `get_paper_latex_section`, `search_paper_text`,
  `citation_graph`, `watch_topic`, `check_alerts`.
- Valency: `semantic_search_papers`, `search_by_title`, `get_citing_papers`,
  `find_similar_papers`, `get_paper_by_id`, `filter_by_date_range`.

arXiv MCP's `semantic_search` searches only the papers already downloaded
to this machine; it is not used to find papers.

## Routes by task
<!-- key: routes-by-task -->

Each row is tried from left to right. A tool that is absent, or that
refuses (see "Refusals"), is skipped.

| Task | 1st | 2nd | 3rd | Last |
|---|---|---|---|---|
| Find papers on a topic | Valency `semantic_search_papers` | arXiv MCP `search_papers` | web search | the skills alone, stating the skill's sweep date |
| Papers of the last days | arXiv MCP `search_papers` (live) | Valency (a few days behind arXiv) | web search | the skills, saying that nothing after the sweep date was searched |
| Who cites a paper | Valency `get_citing_papers` | arXiv MCP `citation_graph` | web search | none: say it was not found |
| What a paper cites | arXiv MCP `citation_graph` | its bibliography, read with `fetch_paper.py` | | |
| Papers not on arXiv | Valency | web search | | |
| Read a paper, day-to-day (L4) | `fetch_paper.py` | arXiv MCP `get_paper_latex` or `read_paper` | web tool | "L4 required and not done" |
| Read a paper, extension mode | arXiv MCP `get_paper_latex_section`, `get_paper_latex` or `read_paper` | `fetch_paper.py` | web tool | the entry goes under "Not verified" |
| New papers on a topic | arXiv MCP `check_alerts` on the researcher's existing watches for the skill's topics | Valency `filter_by_date_range` or a date-filtered search | | |

Rules that go with the table:

- **No adapter at all: the suite behaves as before.** The web-search column
  is used only after an adapter of the same row was tried. A researcher with
  no adapter gets no new web search; the L4 row keeps its web-tool fallback.
- **What starts an outward route in an answer:** only a question that asks
  for papers, for citations, or for what is new. A question whose subject
  may have moved since the snapshot (for example "the current value of H0")
  is answered from the levels, with the skill's sweep date, as before.
- **Watches.** Never call `watch_topic` without the researcher's explicit
  agreement in this conversation. Call `check_alerts` only with a topic of
  the skill at hand, never without a topic: each call advances the watch's
  cursor, so the papers returned for a topic are not returned again.
- **Identifiers** are compared without their version: `2501.16852v2` and
  `2501.16852` are the same paper. A bibliography row never carries a
  version.

## When both are present
<!-- key: when-both-are-present -->

- Valency finds and ranks; arXiv MCP and `fetch_paper.py` read.
- Deduplicate results on the arXiv identifier without its version.
- When the two disagree on a version, a date or a title, the live arXiv
  record holds.
- Search both in parallel only for an exhaustive sweep of an extension run.
  Otherwise the first tool of the row that is present answers.

## Refusals
<!-- key: refusals -->

A refusal is any failure of a tool call: a rate limit, a timeout, an
authentication error, a server that is down.

- A refusing tool is skipped, and the next tool of the row is tried.
- In an answer, a tool that refused counts as absent until the answer is
  given. Do not retry it: arXiv MCP already retries with backoff.
- In an extension run, follow "Extension run" in `cosmoskill-refine`: the run
  stops, and resumes later, only when a step has no working tool left.
- arXiv MCP's `citation_graph` calls Semantic Scholar. Without a
  `SEMANTIC_SCHOLAR_API_KEY` in the server's environment it reaches the rate
  limit quickly and answers `status=rate_limited`. That is expected: treat
  it as a refusal, not as an error to report.
- A paper that arXiv holds only as PDF has no LaTeX source, and arXiv MCP
  reads it only when the server was installed with its PDF extra
  (`arxiv-mcp-server[pdf]`); its error says so. Treat it as a refusal.

## Day-to-day budget
<!-- key: day-to-day-budget -->

An answer that takes an outward route stays small.

- Valency: `include_abstract=false` and `limit` 10 <!-- num: not a value -->
  results. Read the abstract of a hit only when its title makes it a
  candidate.
- Do not download or read a full paper unless the question needs its
  content.
- An abstract served by Valency or by a search hit is a lead, not a source.
  For an arXiv paper, read the abstract again from arXiv
  (`fetch_paper.py --abstract <id> <id> ...`, several identifiers in one
  call) before citing it as `[src: abstract]`. For a paper not on arXiv,
  cite the Valency record as `[sec: Valency record, <id>]` until the paper
  itself is read.
- A result of any adapter enters an answer with the flag of the place where
  it was read, as every other statement of the suite does.

## Silence and the status check
<!-- key: silence-and-the-status-check -->

An answer never names an adapter that is not among your tools, never says
that one is missing, and never suggests installing one. The state of the
adapters is shown only when the researcher asks which tools or adapters
cosmoskill can use (for example "cosmoskill status"), and at the start of
an extension run. Give it as one line:

`arXiv MCP: on|off (suggested) · Valency: on|off (optional) · reading: fetch_paper.py[ + arXiv MCP]`

Then, for each adapter that is off, its install line:

- arXiv MCP, in Claude Code: `claude plugin marketplace add blazickjp/arxiv-mcp-server`,
  then `claude plugin install arxiv-mcp-server@arxiv-mcp`; in any other MCP
  host, the stdio server `arxiv-mcp-server`, as its README describes. It does not run in the
  Claude app, which takes no local server. [doc: github.com/blazickjp/arxiv-mcp-server README, 2026-11-10]
- Valency: a Valency account, then, in Claude Code,
  `claude plugin marketplace add valency-oss/valency-connectors --scope user`,
  `claude plugin install valency@valency-claude-plugin --scope user` and
  `claude mcp login plugin:valency:valency`; in the Claude app, connect
  Valency as an MCP connector of your Claude account. [doc: github.com/valency-oss/valency-connectors README, 2026-11-10]

## What each adapter sends
<!-- key: what-each-adapter-sends -->

The suite's scripts send only arXiv identifiers, to arXiv. The adapters send
more, each to its own service:

- arXiv MCP: search queries and paper identifiers go to arXiv;
  `citation_graph` sends paper identifiers to Semantic Scholar.
- Valency: search queries and paper identifiers go to Valency, under the
  researcher's account.
