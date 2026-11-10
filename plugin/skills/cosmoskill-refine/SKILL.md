---
name: cosmoskill-refine
description: Use when the researcher asks to note something for their own work, add a paper to their layer, start or fill a dossier, override or hide a section of a cosmo-* skill, extend their layer from the recent literature (an extension run), or promote a layer entry to the package, and after a package update, to check that their layer's entries still attach to their sections. Works in Claude Code only, because it needs a persistent home directory.
---

# Refining the cosmo-* skills with a local layer

The package is the base. A researcher's additions live outside it, in a
personal layer (`~/.cosmoskill/`, or `COSMOSKILL_HOME`) or a project layer
(`.cosmoskill/` in a project directory). The format is in the package's
`docs/layers.md` and `docs/layers-v1.md`. Every command below is run, not
imitated: the scripts refuse what cannot be attached or sourced. Below,
`layers.py ...` stands for
`python3 "${CLAUDE_SKILL_DIR}"/../*observational-cosmology/scripts/layers.py ...`,
and the same for `sync_layers.py` and `promote.py`.

Add `--project` to any writing command when the researcher says "for this
project only"; with no layer yet, run `layers.py init` first.

## Choose the entry
<!-- key: choose-the-entry -->

| The researcher asks | Run |
|---|---|
| "note that ..." about one section | `layers.py note <skill> <file>#<key> "<text>"` |
| "note that ..." about the whole skill | `layers.py note <skill> general "<text>"` |
| "for me, use this value instead" | `layers.py override <skill> <file>#<key> "<text>"` |
| "I do not need this section" | `layers.py suppress <skill> <file>#<key> "<reason>"` |
| "add this paper" | `layers.py source <skill> <arXiv id> --role <role>` |
| "write this up as a dossier" | `layers.py dossier <skill> <name>`, then fill the file |

1. Find the section: open the skill's file map, search the reference file
   for the term, and take the key from the `<!-- key: ... -->` line under
   the heading. `<file>` is the reference file without `.md`, or `skill`
   for `SKILL.md`.
2. Show the researcher the base text and the entry before writing an
   override or a suppress: `layers.py resolve <skill> <file>#<key>`.
3. Write the entry in the researcher's words. An override states its value
   with its source; a suppress states its reason.
4. A paper enters a layer only through `source`, which reads title and
   author from arXiv. Never write a bibliography row from memory; a paper
   without an arXiv identifier is added by hand with `doi:<doi>`.
5. Fill a dossier from the papers read in the conversation, with the place
   each number was read; put the rest under "Not verified". Then run
   `layers.py check`: every cited paper needs a row.
6. Anything confidential goes under `<layer>/<skill>/private/`, or takes
   the line `private: yes`; it is never promoted.

## Writing good entries
<!-- key: writing-good-entries -->

Every answer in a skill reads everything `layers.py <skill>` prints, so
apply these to every entry you write, and run `layers.py check`, which
warns on the first and the third:

- A note is 1–3 lines: one fact, preference or correction. Anything longer
  is a dossier, read only when the question is on its subject.
- Attach it to the most specific section; open it with its subject
  ("τ prior:", "For KiDS S8:"), so its relevance shows without opening the
  section. One entry per subject; never two that contradict on one key.
- `general` notes apply to every question of the skill: at most three.
- The profile holds who the researcher is and their conventions, not
  content.
- A number carries its paper and the place read (a code or facility
  fact: `[doc: <page>, <date read>]`); the researcher's own
  judgement is labelled as theirs, or goes under "Not verified".
- Point to the package's sections instead of copying them: a copy goes
  stale silently when the package changes.
- Write neutrally what could serve others, so that `promote.py` can take it
  unchanged.

## Building a specialised part of a skill
<!-- key: building-a-specialised-part-of-a-skill -->

When the researcher wants their own depth on a subject the package covers
only broadly (several notes, papers and a dossier on one subject), read the
example layer in `example-layer/` of this skill first: its `profile.md`,
one `notes.md` and its dossier. Follow its shape, size and labelling: short
notes attached to keys, the papers added with `source`, one dossier in the
package's template that points to the package's sections rather than
copying them, and the researcher's own practice under "Not verified". Copy
the pattern, not the content. Then run `layers.py check` and
`sync_layers.py`.

## Extension run
<!-- key: extension-run -->

An extension run searches the literature after a skill's sweep date, reads
what it finds, and proposes entries for the researcher's layer. It costs
many tokens. It starts only when the researcher asks (for example "refine
my peculiar-velocities layer from the recent literature", "look for what
appeared since the snapshot"). Never start one on your own, and never
because an alert arrived. The tools and their order are in
`references/adapters.md` of the hub
(`"${CLAUDE_SKILL_DIR}"/../*observational-cosmology/references/adapters.md`);
read it first.

1. **Announce it.** Say that this is an extension run, give the status line
   of `adapters.md`, and give the start date printed by
   `layers.py sweep <skill>` (the latest of the skill's snapshot, the
   package's sweep record and the layer's own).
2. **Resume or start.** Run `layers.py progress <skill>`. If it prints
   `paused run:`, resume from that file: do not search again for what its
   candidates already hold. Otherwise it creates the file; fill `Adapters:`.
3. **Gather candidates** newer than the start date. If the researcher has
   arXiv MCP watches, call `check_alerts` only with the topics of this
   skill, and write what it returns under "Alerts read" of the progress
   file at once. Never call `watch_topic` without the researcher's
   agreement in this conversation. With Valency, search the skill's
   subjects and call `get_citing_papers` on its key sources (the papers
   cited in the bullets of "What an expert holds in mind"). Write every
   candidate to the "Candidates" table with its `Found via` (`valency`,
   `arxiv-mcp` or `web`) and the status `found`.
4. **Rank** the candidates against the skill's dossiers and reference
   sections, and drop those that add nothing (status `skipped`, with the
   reason).
5. **Read** the relevant ones with the extension reading row of
   `adapters.md` (arXiv MCP first, then `fetch_paper.py`); set the status
   to `read`. A Valency abstract is a lead; follow the abstract rule of
   `adapters.md`.
6. **Propose one entry at a time** and wait for the researcher's answer
   (status `proposed`, then `accepted` or `rejected`). Any kind may be
   proposed: a `source`, a `note`, dossier content, an `override`. Show an
   override beside the base value it replaces, with both sources. Write an
   accepted entry with the usual commands and `--via <how it was found>`:
   `layers.py source <skill> <id> --role <role> --via valency`,
   `layers.py note ... --via arxiv-mcp`. A paper with no arXiv identifier
   goes into the layer's `sources.tsv` by hand with `doi:<doi>`, then
   `layers.py found <skill> doi:<doi> --via <v>` records how it was found.
   Every statement carries its `[src: <place>]`.
7. **Refusals.** When a tool refuses, try the next tool of its row. When a
   step has no working tool left (for example, no reader can open a
   candidate), stop: write `Stopped:` (the service that refused, the time,
   when to retry) and the list under `## Left to do` in the progress file,
   tell the researcher, and end the run. Write no entry from a partial
   check. The next run on the same skill resumes from the file.
8. **Finish.** Run `layers.py sweep <skill> --record --to <today>
   --adapters <the ones used>`, then `layers.py check`, then
   `layers.py progress <skill> --clear`.

For the package's owner, this same run on the owner's personal layer is how
the base is strengthened: then `promote.py <skill> source`, `dossier`,
`note` and `sweep`, and the proposals are folded in by hand. The cycle is
in the hub's `references/suite-conventions.md`, "Strengthening the base with
an extension run".

## After an update of the package
<!-- key: after-an-update-of-the-package -->

Run `sync_layers.py` and go through what it reports one entry
at a time, with the researcher:

| Status | Do |
|---|---|
| `ok`, `unstamped` | nothing; after review, `--stamp-all` stamps the unstamped |
| `changed` | show `layers.py resolve` for the section; the researcher keeps, edits or deletes the entry; then `--stamp <skill>/<file>#<key>` |
| `changed` override (exit 3) | the same, first: the researcher's value may now be older than the base |
| `moved` | `--follow` re-attaches it to the replacement; then resolve it as `changed` |
| `retired`, `missing` | the section is gone: the researcher moves the entry to another key or deletes it |

Do not stamp an entry the researcher has not reviewed.

## Promote to the package
<!-- key: promote-to-the-package -->

Only the package's owner promotes, in a clone of the package:
`promote.py <skill> source <id> | dossier <name> | note <file>#<key>`.
It writes into the working tree and never commits; a note becomes a
proposal under `docs/proposals/` to fold in by hand. Private entries and
rows without a public identifier are refused. Run the checks it prints.
