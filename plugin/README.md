# cosmoskill

Observational-cosmology skills for Claude Code and the Claude app: one hub
skill (`observational-cosmology`) and 28 domain skills (`cosmo-*`).

Ask Claude about a measurement, a survey or a method, and the skills give it
the current values, where each comes from, what a referee checks, and which
statements still in circulation are out of date. Every number names the paper
and the place it was read: when it matters, Claude reads the paper again
rather than trusting the skill. Literature snapshot: 26 October 2026.

## How it answers

Claude answers at the shallowest level that answers the question, and says
which one it used:

| Level | Claude reads | Enough for |
|---|---|---|
| L1 | the skill's `SKILL.md` | where a domain stands, the headline values, what to watch for |
| L2 | one reference file | another value, its history, a systematic, a referee point |
| L3 | a dossier in `deep/` | how a result is obtained, which method to choose |
| L4 | the cited paper | a number about to go into a manuscript, a proposal or a referee report |

## Install

In the Claude app (paid plan): **Customize → Plugins → Add → Add marketplace →
Add from a repository**, enter `corentinravoux/cosmoskill`, install
**cosmoskill**, and turn on **Settings → Capabilities → Create and edit
files**. Turn on web search in a chat to let Claude read the cited papers.

In Claude Code:

```
/plugin marketplace add corentinravoux/cosmoskill
/plugin install cosmoskill@cosmoskill
```

## What each host can do

| | Claude Code | Claude app |
|---|---|---|
| Skills, reference files, dossiers (levels 1–3) | yes | yes |
| Read the cited paper (level 4) | yes, with `fetch_paper.py` | with web search on; or `fetch_paper.py` if `arxiv.org`, `export.arxiv.org` and `ar5iv.labs.arxiv.org` are allowed domains |
| Personal and project layers, `cosmoskill-refine` | yes | no: the app starts each chat with an empty disk |

## What it runs and contacts

The skills are text. The scripts in the hub skill's `observational-cosmology/scripts/`
(Python standard library only, readable source, nothing downloaded at install)
run only when Claude calls them:

- `fetch_paper.py` downloads a cited paper's abstract or text from
  `export.arxiv.org`, `arxiv.org` and `ar5iv.labs.arxiv.org`, and caches it
  in `~/.cache/cosmo-skill-verify/papers/`.
- `verify_sources.py` asks `export.arxiv.org` for the title and first author
  of arXiv identifiers, cached in `~/.cache/cosmo-skill-verify/arxiv.json`;
  `--offline` contacts nothing.
- `layers.py`, `sync_layers.py` and `promote.py` read and write layer files in
  `~/.cosmoskill/` (or `$COSMOSKILL_HOME`) and `.cosmoskill/`; adding a paper
  to a layer asks `export.arxiv.org` for its title and author.

Only arXiv identifiers are sent. No personal data, credentials or usage data
leave the machine.

## More

Domains, trust notes, layers and maintenance: the repository,
https://github.com/corentinravoux/cosmoskill. Licence: MIT (`LICENSE`).
