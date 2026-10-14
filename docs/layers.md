# Local layers

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
    └── deep/<name>.md      your own dossiers
```

**`profile.md`** is free text, shown to the assistant as context. Two
optional lines are read specifically:

- `home-domains: cosmo-lyman-alpha, cosmo-peculiar-velocities` names the
  skills of your own field. There the assistant may skip the orientation it
  would give an outsider. The rule "answer at the lowest level that answers"
  still holds.
- `conventions: k in h/Mpc; fiducial Planck 2018` states what every answer
  should follow.

**`<skill>/notes.md`** holds notes, one section each. The heading says which
section of the package the note attaches to:

```markdown
## results#cosmology-from-p1d
The compressed parameters are quoted with the mean-flux prior named.

## general
Skip the introduction to the estimators.
```

`results` is the file (`references/results.md`; `skill` stands for
`SKILL.md`), and `cosmology-from-p1d` is the key: the comment
`<!-- key: ... -->` under that section's heading in the package. A key does
not change when the heading is reworded, so a note stays attached across
updates of the package. `## general` attaches to the skill as a whole.

**`<skill>/sources.tsv`** lists papers the package does not cite for that
skill: your own, or those your work rests on. It has the columns of the
package's bibliography (`key, id, first_author, year, title, role`). A row is
added from arXiv, never typed from memory:

```bash
python3 skills/observational-cosmology/scripts/layers.py source cosmo-lyman-alpha <arXiv id> --role method
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
python3 skills/observational-cosmology/scripts/layers.py dossier cosmo-lyman-alpha qmle-window
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
| "note for my Lyα work that ..." | finds the section the remark is about and runs `layers.py note <skill> <file>#<key> <text>`; `general` when it concerns the whole skill |
| "add this paper to my layer" | runs `layers.py source <skill> <arXiv id> --role <role>` |
| "write up what we just worked out as a dossier" | runs `layers.py dossier <skill> <name>`, then fills the file from the papers read in the conversation, with a place for each number, and lists the rest under "Not verified" |
| "for this project only" | the same with `--project`, which writes to `.cosmoskill/` in the project |

A note is dated when written. Notes, papers and dossiers are plain files:
edit or delete them with any editor.

## How the assistant uses it

Every skill ends with a block that says: if a `.cosmoskill/` directory
exists, run `layers.py <skill>` and read what it prints. The script prints
the profile settings, the profile text, the notes, the papers and the
dossiers for that skill, project layer first, then personal. A dossier is
listed with its title and scope and read only when the question is about its
subject. An answer that draws on a layer says so, and its last line names
the layer: `[cosmoskill L3 · personal · cosmo-lyman-alpha/deep/qmle-window]`
for a dossier.

```bash
python3 skills/observational-cosmology/scripts/layers.py cosmo-lyman-alpha
python3 skills/observational-cosmology/scripts/layers.py cosmo-lyman-alpha --json
python3 skills/observational-cosmology/scripts/layers.py check
python3 skills/observational-cosmology/scripts/layers.py check --online
```

`check` lists notes attached to a key the package does not have (a typing
error, or a section the package retired), malformed rows of a `sources.tsv`,
and papers cited in a note or a dossier without a row. With `--online` it
also compares the title and first author of every row with arXiv. Run it
after updating the package.

## What a layer does not do

- A layer adds; it does not replace a value of the package. Where your
  dossier and the package disagree, the assistant gives both and says which
  is which.
- The package does not check a layer's content: a paper you added is read
  before it is quoted, like any other.
- Nothing is merged or promoted to the package.
- Keep anything confidential out of a project layer that is committed with
  the project: a layer is plain text in a directory.
