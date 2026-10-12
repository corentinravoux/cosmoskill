# Local layers, version 0

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
    └── notes.md
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

## How the assistant uses it

Every skill ends with a block that says: if a `.cosmoskill/` directory
exists, run `layers.py <skill>` and read what it prints. The script prints
the profile settings, the profile text and the notes for that skill, project
layer first, then personal. An answer that draws on a note says so, and its
last line names the layer.

```bash
python3 skills/observational-cosmology/scripts/layers.py cosmo-lyman-alpha
python3 skills/observational-cosmology/scripts/layers.py cosmo-lyman-alpha --json
python3 skills/observational-cosmology/scripts/layers.py check
```

`check` lists notes attached to a key the package does not have: a typing
error, or a section the package retired. Run it after updating the package.

## What version 0 does not do

- A note adds context; it does not replace a value of the package. Recording
  a number of your own, with its source and a checked bibliography row, is
  the structured layer planned for a later version.
- Nothing is merged or promoted to the package.
- Keep anything confidential out of a project layer that is committed with
  the project: a layer is plain text in a directory.
