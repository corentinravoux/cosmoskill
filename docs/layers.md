# Local layers

This page describes layers for the researcher. The full specification of
entry modes, stamps, `sync_layers.py`, `promote.py` and the release manifest
is `docs/layers-v1.md`; a layer written for v0 still works unchanged.

The package is the base layer. A researcher adds to it without editing it,
in two places:

| Layer | Where | For |
|---|---|---|
| personal | `~/.cosmoskill/`, or the directory named by `COSMOSKILL_HOME` | what holds for you in every project |
| project | `.cosmoskill/` in a project directory, found from any subdirectory | what holds for one paper or proposal |

Create one with the hub's script, here written from the repository root:

```bash
python3 skills/observational-cosmology/scripts/layers.py init            # personal
python3 skills/observational-cosmology/scripts/layers.py init --project  # in the current directory
```

## What a layer holds

```
.cosmoskill/
├── profile.md
└── <skill>/
    ├── notes.md            notes attached to sections of the package
    ├── sources.tsv         your own papers, and those you rely on
    ├── deep/<name>.md      your own dossiers
    └── private/            the same three, never promoted to the package
```

**`profile.md`** is free text, shown to the assistant as context. Two
optional lines are read specifically:

- `home-domains: cosmo-weak-lensing, cosmo-cmb-lss-cross-correlations` names the
  skills of your own field. There the assistant may skip the orientation it
  would give an outsider. The rule "answer at the lowest level that answers"
  still holds.
- `conventions: k in h/Mpc; fiducial Planck 2018` states what every answer
  should follow.

**`<skill>/notes.md`** holds notes, one section each. The heading says which
section of the package the note attaches to:

```markdown
## results#the-cmb-reference-values
Quote every S8 difference against both CMB references named here.

## general
Skip the introduction to shear estimators.
```

`results` is the file (`references/results.md`; `skill` stands for
`SKILL.md`), and `the-cmb-reference-values` is the key: the comment
`<!-- key: ... -->` under that section's heading in the package. A key does
not change when the heading is reworded, so a note stays attached across
updates of the package. `## general` attaches to the skill as a whole.

A note adds to its section. Two other modes act on the section itself, for
you only:

```markdown
## results#optical-depth-tau
mode: override
base: 3f2a9c1d7e0b
Our baseline is the low-ell reanalysis value; quote it first.

## physics-and-methods#what-is-measured-and-why-it-constrains-cosmology
mode: suppress
base: 8c01d2e4f9a7
I know the basics of cluster counts.
```

- `override`: your text replaces the section for you. An answer still
  quotes the package's value beside yours, both labelled, and says which
  one it used.
- `suppress`: the section is skipped, unless the question is about it; its
  heading and your reason stay visible.
- `base:` is the fingerprint of the section when the entry was written. The
  commands write it; it tells `sync_layers.py` when the section has changed
  under your entry.
- `private: yes`, or a file under `<skill>/private/`, marks what is never
  promoted to the package.

**`<skill>/sources.tsv`** lists papers the package does not cite for that
skill: your own, or those your work rests on. It has the columns of the
package's bibliography (`key, id, first_author, year, title, role`). A row is
added from arXiv, never typed from memory:

```bash
python3 skills/observational-cosmology/scripts/layers.py source cosmo-supernovae <arXiv id> --role method
```

The script takes the title and the first author from arXiv, derives a key,
and writes nothing if arXiv cannot be reached or if the package already
cites the paper. Roles are those of the package: foundation, review, method,
data, results, systematics, forecast, code, critique. A paper without an
arXiv identifier is added by hand, with `doi:<doi>` in the `id` column.

**`<skill>/deep/<name>.md`** is a dossier: a subject you know in more depth
than the package holds, written once so that the assistant does not have to
be told again. Start one from the template:

```bash
python3 skills/observational-cosmology/scripts/layers.py dossier cosmo-clusters richness-mass-calibration
```

The template has a scope line, then sections for the method, the choices and
their cost, the numbers with the place each was read, what goes wrong, a
reading list and what is not verified. Papers cited in a dossier or in a
note need a row, in the layer or in the package.

## Adding to a layer in a conversation

Nothing here needs a script run by hand: ask the assistant. It uses the
commands below, which refuse what cannot be attached or sourced.

| Request | What the assistant does |
|---|---|
| "note, for my cluster work, that ..." | finds the section the remark is about and runs `layers.py note <skill> <file>#<key> <text>`; `general` when it concerns the whole skill |
| "for me, use this value of τ instead" | shows the section with `layers.py resolve`, then runs `layers.py override <skill> <file>#<key> <text>` |
| "I do not need the introduction to shear estimators" | runs `layers.py suppress <skill> <file>#<key> <reason>` |
| "add this paper to my layer" | runs `layers.py source <skill> <arXiv id> --role <role>` |
| "write up what we just worked out as a dossier" | runs `layers.py dossier <skill> <name>`, then fills the file from the papers read in the conversation, with a place for each number, and lists the rest under "Not verified" |
| "for this project only" | the same with `--project`, which writes to `.cosmoskill/` in the project |

A note is dated and stamped when written. Notes, papers and dossiers are
plain files: edit or delete them with any editor. The `cosmoskill-refine`
skill gives the assistant this workflow.

## Writing good entries

A layer is read on every question of the skills it touches, so how it is
written decides what it costs and whether it is used.

- **Keep notes to 1–3 lines.** `layers.py <skill>` prints every note of the
  skill before each answer; a long note is paid for on every question. Put
  longer content in a dossier: it is listed by title and scope and read only
  when the question is on its subject. `layers.py check` warns on a note of
  more than four lines.
- **Attach to the most specific section, and open with the subject.** A
  note is applied when its subject is the question's, without opening the
  section it is attached to; "τ prior: ..." is recognised, "Note: ..." is
  not. One entry per subject: two contradicting entries on one key leave
  the answer to choose.
- **Few `general` notes.** They apply to every question of the skill;
  `check` warns above three.
- **Choose the mode by what you mean.** A note adds without contradicting.
  An override says the package's value is not the one you use; give your
  value with its paper and place read, since the answer quotes it beside
  the package's. A suppress hides a section you never need; give the reason.
  A dossier holds your own method depth, in the package's template.
- **The profile is for who you are and your conventions**, not for content:
  it is printed in every skill.
- **Source like the package.** A number carries its paper and the place
  read; add papers with `layers.py source`, never by hand; your own
  judgement is labelled as yours or goes under "Not verified".
- **Point to the package rather than copying it.** A copied passage goes
  stale silently when the package changes; a pointer to `<file>#<key>`
  stays right, and `sync_layers.py` reports when the section moves.
- **Write an override after reading the current base** with
  `layers.py resolve`, so that its stamp means something when
  `sync_layers.py` later says `changed`.
- **Keep confidential content private** (`private/` or `private: yes`), and
  write the rest neutrally, so that `promote.py` can move it into the
  package unchanged.

A complete example, built with `layers.py` and kept valid by a test, is in
`skills/cosmoskill-refine/example-layer/`: a profile, notes of each mode
(including a `general` and a private one) on three skills, a paper row and a
short dossier that points to the package. The `cosmoskill-refine` skill
reads it before building a specialised part of a skill in a researcher's
layer.

## How the assistant uses it

Every skill ends with a block that says: if a `.cosmoskill/` directory
exists, run `layers.py <skill>` and read what it prints. The script prints
the profile settings, the profile text, the notes, the papers and the
dossiers for that skill, project layer first, then personal. A dossier is
listed with its title and scope and read only when the question is about its
subject. An answer that draws on a layer says so, and its last line names
the layer: `[cosmoskill L3 · personal · cosmo-clusters/deep/richness-mass-calibration]`
for a dossier.

```bash
python3 skills/observational-cosmology/scripts/layers.py cosmo-weak-lensing
python3 skills/observational-cosmology/scripts/layers.py cosmo-weak-lensing --json
python3 skills/observational-cosmology/scripts/layers.py resolve cosmo-cmb results#optical-depth-tau
python3 skills/observational-cosmology/scripts/layers.py check
python3 skills/observational-cosmology/scripts/layers.py check --online
```

`resolve` prints a file of the package, or one section, with every entry
that applies, labelled by layer and mode: `[base]` and `[personal override —
effective for this researcher]`, `[suppressed by the project layer: ...]`,
`[personal note] ...`. When both layers override a section, the project
entry is the effective one; an override in one layer wins over a suppress in
the other. `--json` gives one object per section.

`check` lists notes attached to a key the package does not have (a typing
error, or a section the package retired), malformed entries and rows, and
papers cited in a note or a dossier without a row. With `--online` it also
compares the title and first author of every row with arXiv.

## After updating the package

```bash
python3 skills/observational-cosmology/scripts/sync_layers.py
python3 skills/observational-cosmology/scripts/sync_layers.py --follow
python3 skills/observational-cosmology/scripts/sync_layers.py --stamp cosmo-cmb/results#optical-depth-tau
python3 skills/observational-cosmology/scripts/sync_layers.py --stamp-all
```

`sync_layers.py` gives each entry a status: `ok`, `unstamped` (a note
written before stamps), `changed` (the section was edited since the entry
was written), `moved` (the key was retired with a replacement, listed in
the skill's `references/retired-keys.tsv`), `retired` (no replacement) or
`missing`. It exits 0 when all are `ok` or `unstamped`, 2 when an entry
needs review, 3 when that entry is an override (your value may now be the
older one), and 1 for a malformed layer. Read the section again with
`resolve`, edit your entry if needed, then `--stamp` it; `--follow`
re-attaches moved entries to their replacement. Retired and missing
entries are left to you. A release of the package can ship
`releases/<version>.tsv` (written by `tools/make_release_manifest.py`),
which lists the keys added, changed, moved or retired, so you can see what
`sync_layers.py` will report before updating.

## Promoting to the package

The package's owner can move an entry into the package with
`promote.py <skill> source <id> | dossier <name> | note <file>#<key>`. It
writes into the working tree and never commits: a paper is appended to the
skill's bibliography (with a public identifier only), a dossier is copied to
`deep/`, and a note becomes a proposal in `docs/proposals/` to fold in by
hand. Private entries, rows without an arXiv or DOI identifier, and
dossiers citing a paper without a row are refused, and nothing is written.

## What a layer does not do

- A layer does not change what the package says. Even an override is
  shown beside the package's value; where your dossier and the package
  disagree, the assistant gives both and says which is which.
- The package does not check a layer's content: a paper you added is read
  before it is quoted, like any other.
- Nothing is merged into the package automatically: `promote.py` only
  prepares the change, for the owner to review and commit.
- Keep anything confidential out of a project layer that is committed with
  the project: a layer is plain text in a directory.
