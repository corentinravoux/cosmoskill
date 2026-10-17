# Personal-layer answering test — 2026-10-17

Question: does an assistant reading the package files use a personal layer
when it applies, leave it out when it does not, and label its answer?

Set-up. A throwaway personal layer in a temporary directory, selected with
`COSMOSKILL_HOME`: a profile (`home-domains: cosmo-cmb`; convention "quote
every optical-depth value with its likelihood name"), one note attached to
`cosmo-cmb/results#optical-depth-tau` (a marked fixture sentence: the group
takes the PR4 LoLLiPoP value as its baseline), and one personal dossier
`cosmo-cmb/deep/test-tau-pipeline` describing a fictitious pipeline, marked as
a fixture. One subagent answered four questions from the package files only,
starting at the hub and following each `SKILL.md`, including its level block.

| # | Question | Expected | Result |
|---|---|---|---|
| 1 | Current Planck τ from large-scale polarisation | note and convention applied; footer names the personal layer | pass: baseline named as coming from the personal layer, every value with its likelihood, `[cosmoskill L2 · base+personal · cosmo-cmb/results#optical-depth-tau]` |
| 2 | How the researcher's TAUFIX pipeline fits τ | answered from the personal dossier at L3, flagged as such | pass: four points from the dossier, its fixture status stated, `[cosmoskill L3 · personal · cosmo-cmb/deep/test-tau-pipeline]` |
| 3 | DESI DR2 LRG D_M/r_d at z_eff = 0.51 | no layer content (other domain) | pass: `layers.py` run, profile only, `base` footer |
| 4 | ACT DR6 n_s | no layer content (the τ note does not apply) | pass on the layer; see below |

Finding outside the layer. The hub routes n_s to `cosmo-inflation-primordial`,
whose table lacks the ACT DR6-alone value; the answer came from `cosmo-cmb`,
which holds it. Fix: a pointer sentence in the inflation `results.md` naming
where the per-experiment CMB values are (no number repeated, one owner).

Cost: one subagent, about 100k tokens, 17 tool calls.
