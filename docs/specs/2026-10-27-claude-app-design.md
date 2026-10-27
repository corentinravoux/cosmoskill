# cosmoskill in the Claude app — design

Written 2026-10-27. One source tree, one GitHub repository, two hosts: Claude
Code and the Claude app (web, Desktop, Cowork), both installing the plugin
from `.claude-plugin/marketplace.json`.

## Why

The app installs plugins from a GitHub marketplace (Personnaliser → Plugins →
Ajouter → Ajouter une place de marché → Ajouter à partir d'un référentiel).
A test install on 2026-10-27 showed what breaks there; nothing else needs to
change. A per-skill ZIP edition (proposed in outside feedback) is not needed:
the plugin route keeps the whole tree.

## Facts measured in the app (2026-10-27)

- Skills live at `/mnt/skills/plugins/cosmoskill:<skill>/`: each folder name
  carries the plugin prefix, so the hub is `cosmoskill:observational-cosmology`.
  `deep/`, `references/` and the hub's `scripts/` are all present.
- `${CLAUDE_SKILL_DIR}` reaches the model literally; the environment variable
  is empty in the shell.
- The sandbox network allows package registries, GitHub and
  `api.anthropic.com` only. `arxiv.org`, `export.arxiv.org` and
  `ar5iv.labs.arxiv.org` fail with a DNS error (`Name or service not known`).
  `fetch_paper.py` then retries with sleeps (about 75 s) before failing.
- No web fetch or web search tool in a chat unless the user turns web search
  on for it.
- Skills need code execution (Paramètres → Capacités → « Créer et modifier des
  fichiers »; on Team/Enterprise, the owner's « Politique » tab).

## Goals

1. Every script path in every `SKILL.md` resolves in Claude Code (routes A,
   B, C of the README) and in the app.
2. L4 degrades cleanly: script, then a web tool, then "L4 required, not
   done". Never paper content from memory.
3. A network that cannot reach arXiv costs seconds, not minutes.
4. The README tells an app user what to switch on, and a Claude Code user how
   not to load the skills twice.

## Non-goals

- No second edition, no build step, no ZIP per skill.
- No layers in the app: `layers.py`, `promote.py`, `sync_layers.py` and
  `cosmoskill-refine` stay Claude Code features. The layers paragraph is
  already conditional on a `.cosmoskill/` directory, which the app lacks.
- No change to content (L1–L3), keys, numbers or bibliographies.
- `docs/agent-brief*.md` and `docs/layers.md` are maintainer documents for
  Claude Code; their paths stay.

## Decisions

- Path form: `"${CLAUDE_SKILL_DIR}"/../*observational-cosmology/scripts/<script>`.
  The glob sits outside the quotes so that the shell expands it; it matches
  `observational-cosmology` and `cosmoskill:observational-cosmology`.
- One sentence tells the model that `${CLAUDE_SKILL_DIR}` is the folder of
  the `SKILL.md` and that, if it is unexpanded, it writes that path in its
  place.
- Unreachable network = the URL error's reason is a DNS failure
  (`socket.gaierror`), a refused connection, `ENETUNREACH`/`EHOSTUNREACH`,
  or HTTP 403 (what an egress proxy answers for a blocked host).
  Then the scripts stop at once with exit code 3 and a message naming the web
  fallback. Timeouts, HTTP 429/503 and other errors keep today's retries.
- Release 1.0.1, the owner pushes and tags on GitHub.
