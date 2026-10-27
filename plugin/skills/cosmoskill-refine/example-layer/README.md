# cosmoskill local layer

A layer holds, per skill of the package, three things.

**Notes**, in `<skill>/notes.md`, one section each:

    ## results#the-cmb-reference-values
    Quote every S8 difference against both CMB references named here.

    ## general
    I work on shear calibration: skip its introduction.

The heading names the section of the package the note attaches to, as
`<file>#<key>`, where the key is the comment under that section's heading in
the package. `## general` attaches to the skill as a whole.

**Papers**, in `<skill>/sources.tsv`: your own papers and the ones you rely
on that the package does not cite. Same columns as the package's
bibliography. Add a row with `layers.py source <skill> <arXiv id> --role
<role>`: title and author then come from arXiv.

**Dossiers**, in `<skill>/deep/<name>.md`: a subject you know in more depth
than the package holds. Start one with `layers.py dossier <skill> <name>`.

`layers.py check` lists what no longer attaches after an update of the
package.
