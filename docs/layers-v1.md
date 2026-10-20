# Layers v1 — overlay by section key

Status: design of plan item B (`docs/plans/2026-10-20-plan.md`), 2026-10-20.
It extends `docs/layers.md`; a layer written for v0 still works unchanged.

The roadmap of 2026-10-12 designed phase 5 around a claims table. That
table was dropped; v1 is built on what the package already has: frozen
section keys (`<!-- key: slug -->`, checked by `tools/check_keys.py`) and the
list of retired keys (`references/retired-keys.tsv`).

## 1. What a layer entry can do

An entry in `<layer>/<skill>/notes.md` attaches to one section of the base,
named `<file>#<key>`, or to the skill (`general`). It has one of three modes:

| Mode | Effect on an answer | Typical use |
|---|---|---|
| `add` (default) | the base section holds; the entry is read with it | a convention, a caveat, the group's baseline choice |
| `override` | the entry replaces the base section *for this researcher*; an answer quotes both, labelled | a value the researcher re-derived, a newer result the base lacks |
| `suppress` | the base section is skipped for this researcher; its heading and the reason stay visible | an introduction the researcher does not need |

An override never changes what the package says: the base value is always
shown beside it, and the answer says which one it used.

### Format

```markdown
## results#optical-depth-tau
mode: override
base: 3f2a9c1d7e0b
Our baseline is the PR4 LoLLiPoP value; quote it first.
```

- The first lines after the heading may be `mode:`, `base:` and `private:`,
  in any order; the text follows.
- No `mode:` line means `add`: every v0 note is an `add` entry.
- `base:` is the fingerprint of the base section when the entry was
  written: the first 12 hex digits of the SHA-256 of the section's text
  (heading line to the next heading of the same or a higher level, key line
  and trailing blank lines excluded, whitespace at line ends removed). The
  writing commands set it; nobody types it.
- `private: yes` marks an entry that is never promoted to the base.
  Everything under a directory named `private/` inside a layer is private
  too (`<layer>/<skill>/private/notes.md`, `.../private/deep/<name>.md`,
  `.../private/sources.tsv`); these files are read like the others.

### Precedence

Project layer, then personal layer, then base. When both layers override
the same section, the project entry is the effective one; both are shown.
A `suppress` in one layer and an `override` in another: the override wins
(something is said, not hidden).

## 2. Commands

All in the hub's `scripts/` directory, standard library only.

| Command | Does |
|---|---|
| `layers.py note <skill> <file>#<key> <text>` | as in v0, now stamps `base:` |
| `layers.py override <skill> <file>#<key> <text>` | writes an `override` entry, stamped |
| `layers.py suppress <skill> <file>#<key> <reason>` | writes a `suppress` entry, stamped |
| `layers.py resolve <skill> <file>[#<key>] [--json]` | prints the effective text: each base section, with every entry that applies, labelled by layer and mode |
| `sync_layers.py [--stamp <skill>/<file>#<key> \| --stamp-all] [--follow]` | reports every entry whose base section changed, moved or disappeared since it was written |
| `promote.py <skill> source <id> \| dossier <name> \| note <file>#<key>` | moves a layer entry into the package's working tree for the owner to review and commit |

`COSMOSKILL_BASE` (a `skills/` directory) replaces the package's own
`skills/` as the base, for tests and for checking a layer against another
checkout of the package.

### `resolve`

For each section of the file (or the one named): the base heading and key;
then, if an entry applies,

- `add`: the base text, then `[<layer> note] <text>`;
- `override`: `[base] <text>` then `[<layer> override — effective for this
  researcher] <text>`;
- `suppress`: `[suppressed by the <layer> layer: <reason>]` in place of the
  base text.

Sections without an entry are printed as they are. With `--json`, one
object per section: `file, key, heading, base_text, entries[]`.

### `sync_layers.py`

For each entry of every layer found (project, personal):

| Status | Meaning | Exit |
|---|---|---|
| `ok` | key present, fingerprint unchanged | 0 |
| `unstamped` | a v0 note without `base:` | 0 (reported) |
| `changed` | key present, base text changed since the entry was written | 2; **3 if the entry is an override** |
| `moved` | key listed in `retired-keys.tsv` with a `replaced_by` | 2; 3 for an override |
| `retired` | key retired with no replacement | 2; 3 for an override |
| `missing` | key absent and not listed as retired | 2; 3 for an override |

The exit status is the highest found; 1 is kept for a malformed layer. A
`changed` override is the case that must never pass silently: the
researcher's value may now be the older of the two.

`--stamp` re-stamps one entry after the researcher has reviewed it;
`--stamp-all` re-stamps every `ok`, `unstamped` and `changed` entry.
`--follow` rewrites the heading of each `moved` entry to its `replaced_by`
and stamps it. Neither touches an entry that is `retired` or `missing`.

### `promote.py`

Writes into the package's working tree; never commits.

- `source <id>`: the row must have a public identifier (arXiv or DOI) and
  match arXiv when online; it is appended to the skill's
  `references/sources.tsv`.
- `dossier <name>`: copied to `skills/<skill>/deep/<name>.md`. Refused when
  the dossier is private, when a cited identifier has no row in the base
  (unless `--with-sources` promotes the layer's rows with it), when a
  dossier of that name exists, or when `Scope:` or `Snapshot:` is missing.
  Prints the file-map row and the `subtopics.tsv` row to add, and the
  checks to run.
- `note <file>#<key>`: a note cannot be merged into prose automatically; it
  is written as a proposal, `docs/proposals/<date>_<skill>_<file>_<key>.md`,
  holding the base section, the entry and its mode, for the owner to fold
  in by hand.

Every refusal exits non-zero and writes nothing. The layer entry is kept;
`--remove` deletes it after a successful promotion.

## 3. Release manifest

`tools/make_release_manifest.py --from <ref> [--to <ref>] --version <v>`
writes `releases/<v>.tsv` with columns `skill, file, key, change,
replaced_by, fingerprint`; `change` is `added`, `changed`, `retired` or
`moved`, computed with the same fingerprint as the layers. It tells a
researcher, before updating, which of their entries `sync_layers.py` will
report.

## 4. Skill `cosmoskill-refine`

A workflow skill, triggered when the researcher asks to note, add a paper,
start a dossier, override or hide a section, or after an update of the
package. It runs the commands above, shows `sync_layers.py` reports one
entry at a time, and never writes a bibliography row from memory.

## 5. What answers do with the modes

The block every `SKILL.md` ends with (generated from
`tools/templates/fixed-block.md`) adds: an `override` is quoted with the base
value beside it, both labelled; a `suppress` is honoured unless the question
is about that section itself. The footer is unchanged
(`base+personal`, `base+project`).

## 6. Tests

On fixture layers in `tests/fixtures/layers/` and a fixture base in
`tests/fixtures/base/` (selected with `COSMOSKILL_BASE`):

1. v0 notes still load and resolve as `add`.
2. `resolve` prints base and override, both labelled; `suppress` hides the
   base text and keeps the reason.
3. Base moved forward (one section reworded, one key retired with a
   replacement, one removed): every entry resolves or is reported;
   `sync_layers.py` exits 3 and names the key of the changed override.
4. `--follow` re-attaches the moved entry; `--stamp` clears `changed`.
5. `promote.py` on a private entry, or on a dossier citing an identifier
   with no row, exits non-zero and writes nothing.
6. The release manifest lists the reworded, retired and moved keys.

Plus one answering test with an override (as in
`docs/history/tests/levels/run-2026-10-17-layers.md`).
