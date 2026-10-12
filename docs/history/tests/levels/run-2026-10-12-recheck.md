# Level test — recheck of 2026-10-12

Seven questions from `docs/tests/levels/questions-recheck.md` were answered by reading the skill files by path and following each skill's "Levels and layers" section to the letter, with no source other than the files under `skills/`, the output of the layer command and the output of `skills/observational-cosmology/scripts/fetch_abstracts.py`; every file opened and every command run is recorded below.

## Preliminaries (once, before question 1)

Opened:

- `docs/tests/levels/questions-recheck.md`, lines 1–11.
- `skills/observational-cosmology/SKILL.md`: headings located with `grep -n '^#'`, then lines 8–43 ("Which skill holds what") and lines 59–93 ("Choosing the level"). The hub's own "Levels and layers" section (line 179 onwards) was not read.

Layer check, valid for questions 1–4, 6 and 7: the working directory of the session was a directory outside the repository. The existence of `.cosmoskill/` was tested with `ls -d` in that directory, in each of its parents and in the home directory: absent everywhere. `COSMOSKILL_HOME` was unset. The condition of the "Local layers" paragraph was therefore false and the layer command was not run for those six questions; their layer is `base`.

---

## Question 1 — (referee) cluster-count cosmology paper: what should be checked?

Answer:

The eleven points a referee checks on a cluster-count analysis:

1. Mass definition, mass units and the reference of any (1 − b).
2. Lensing calibration: data, redshift range, systematic floor.
3. Lensing-mass to halo-mass relation and its baryon term.
4. Selection function, purity, contaminants.
5. Optical samples: projection model, scales, richness cut, SZ or X-ray cross-check.
6. Miscentring model.
7. Mass function, neutrinos, baryons.
8. Free mass and redshift slopes; correlated scatter.
9. Sample variance in the likelihood (a Poisson count likelihood underestimates errors for Rubin- or Euclid-like samples, arXiv:2210.11093).
10. Blinding and post-unblinding changes.
11. Exponent of the amplitude combination; CMB reference.

Prose slips worth a look in the same pass: "clusters prefer low σ8" without the sample named; (1 − b) values compared across different reference relations; amplitudes differenced with different exponents (0.17 to 0.5); mass limits mixing M_sun, M_sun/h and M_sun/h70. No number is endorsed here; any value the report quotes back to the authors must first be read in the cited paper.

`[cosmoskill L1 · base · cosmo-clusters/skill#systematics-a-referee-checks]`

Level: L1 — the level table gives "the list a referee checks" as L1 content and the list is in the file; L2 would only add the size of each systematic, which was not asked, and no number is endorsed, so L4 is not triggered.

Opened:

- `skills/cosmo-clusters/SKILL.md`, lines 1–111 (whole file).
- Command: the `ls -d` layer check described in the preliminaries.

Notes:

- The file map (line 18) sends "Size of a systematic; what a referee asks" to `references/systematics.md`, while the level table says the referee list is L1. The two pull in opposite directions for exactly this question; the L1 rule was followed.
- The hub makes L4 mandatory "before endorsing a number for a manuscript, a proposal or a referee report"; the block in the domain file says only "before a number goes into a manuscript". For a referee asking for a checklist it is not stated whether the checklist itself counts; it was read as not triggering L4.
- The answer draws on two L1 sections (the checklist and "Errors that recur") but the footer takes one key.

---

## Question 2 — (outsider) latest Hubble-constant value from gravitational-wave standard sirens

Answer:

The current LIGO–Virgo–KAGRA value is H0 = 71.7 (+9.4/−7.5), in the usual H0 unit, from GWTC-5.0: 236 sources, combining the black-hole mass spectrum, the DES Y6 galaxy catalogue and GW170817 (arXiv:2605.27227). That is a precision of about 12% (derived), so it is compatible with both ends of the Hubble tension. Two things an outsider should know: the constraint is driven by features of the mass spectrum rather than by galaxies, and GW170817 is still the only siren with an electromagnetic counterpart (alone it gives 70.0 +12.0/−8.0, arXiv:1710.05835).

`[cosmoskill L1 · base · cosmo-multimessenger/skill#what-an-expert-holds-in-mind]`

Level: L1 — the headline value with its citation is a bullet of the file; nothing in the question asks for the history or the table of other siren values (L2), and the number is not going into a manuscript (L4).

Opened:

- `skills/cosmo-multimessenger/SKILL.md`, lines 1–136 (whole file).
- No command (layer condition false, see preliminaries).

Notes:

- Skill choice: `cosmo-distance-ladder-h0` lists standard sirens in its description, so two skills fit. The hub table (sirens in the `cosmo-multimessenger` row only) and the rule "one probe's value: that probe's skill" settled it.
- The L1 bullet gives H0 without its unit (km/s/Mpc is nowhere in the file). For an outsider this is a gap; the unit was not supplied from memory.
- The bullet carries a `[der]` flag ("About 12% [der]"), whereas the hub states that "the `SKILL.md` bullets carry citations only" and that flags are in the reference files.
- "Latest" is slightly ambiguous at L1: the file also lists a 2026 jet-informed GW170817 value (65.5 ± 4.4, arXiv:2605.11437). "Errors that recur" warns against presenting one jet-informed value as "the" result, which was enough to choose the LVK value without opening `references/results.md`.

---

## Question 3 — (analyst of the same probe) wavenumber and redshift ranges of the DESI DR1 P1D, per estimator

Answer:

| | QMLE (arXiv:2505.07974, Sect. 4.1) | FFT (arXiv:2505.09493, Sects. 3.2, 4.1, 7) |
|---|---|---|
| Unit | s/km | Å⁻¹ |
| Redshift | Δz = 0.2 bins estimated from z = 2.0 to 4.6, first and last removed: z = 2.2–4.4 [der]; cross-exposure estimate only to z = 3.8 | Δz = 0.2 bins from z_min = 2.1, none above z = 4.2: bins z = 2.2–4.2 [der] |
| Wavenumber, measured | 60 linear bins of 5 × 10⁻⁴ s/km, then 25 logarithmic bins of Δlog k = 0.01: band edges to 0.030, then to 0.053 s/km [der, assuming the linear bins start at k = 0 and a base-10 logarithm] | k_min = 0.0468 Å⁻¹ to k_max = 2.0 Å⁻¹ |
| Wavenumber, recommended | 10⁻³ s/km < k < 0.5π/R_z, i.e. k_max = 0.0255 s/km at z = 2.2, 0.0318 at z = 3.0, 0.0414 at z = 4.2 [der]; these are the cuts of the cosmology paper | 2.0 Å⁻¹ is 0.0260 s/km at z = 2.2 and 0.0422 s/km at z = 4.2 [der], so the two k_max conventions agree |

One open point: the cosmology paper (arXiv:2601.21432, Sect. 2.1) quotes 11 bins, z = 2.2–4.2, for the P1D, while the QMLE binning as described gives bins up to 4.4. The reference file flags this as not resolved; the z = 4.4 bin should be checked in arXiv:2505.07974 before it is relied on. The end points marked [der] are computed from the stated binning, not quoted by the papers.

`[cosmoskill L2 · base · cosmo-lyman-alpha/results#the-one-dimensional-flux-power-spectrum]`

Level: L2 — the `SKILL.md` says only that DESI measures P1D with both FFT and QMLE, with no range, so L1 cannot answer; one passage of one reference file holds both estimators' ranges; there is no `deep/` dossier (L3) and nothing is being endorsed for a manuscript (L4).

Opened:

- `skills/cosmo-lyman-alpha/SKILL.md`, lines 1–99 (whole file).
- Command: `grep -n -E 'QMLE|FFT'` on `skills/cosmo-lyman-alpha/references/physics-and-methods.md`, `surveys-and-data.md` and `results.md` (output cut to 260 characters per line), because the file map names three files that could hold the answer.
- Command: `grep -n -E '^#|<!-- key'` on `skills/cosmo-lyman-alpha/references/results.md`, to find the heading and key of the passage.
- `skills/cosmo-lyman-alpha/references/results.md`, lines 150–181.
- No layer command (condition false).

Notes:

- Three file-map rows fit (estimators in methods, releases in surveys, "current values, fit details" in results). The instruction "search them for the term before reading" resolved it, but the search output itself shows fragments of the two files that were then not read; "read only the passage" cannot be strictly true once a search has been run across files.
- The passage needed for the key (heading at line 150) and the passage holding the answer (lines 160–161 and 167–180) are separated by table rows for other surveys; 32 lines were read where about 17 held the answer.
- L4 is required "when two files disagree". Here the disagreement (upper redshift 4.4 against 4.2) is inside one file, between two cited papers, and the file itself says it was not resolved. Whether that triggers L4 is not stated; it was read as not triggering, and the open point was passed on to the asker.

---

## Question 4 — (author) "DESI DR2 measures D_H/r_d = 8.632 ± 0.101 from the Lyα forest": can it be submitted like that?

Answer:

The number is right, the sentence needs three repairs, and one check is still owed.

- Verified in the abstract of arXiv:2503.14739 (DESI DR2 Results I): D_H(z_eff)/r_d = 8.632 ± 0.098 ± 0.026, statistical then theoretical systematic, at z_eff = 2.33. The draft's ± 0.101 is the two added in quadrature (√(0.098² + 0.026²) = 0.1014, derived). The suite's reference file records 8.632 ± 0.101 as the stat + sys value the paper gives in its Sect. 6.2 and recommends for model testing; that section was not read. **L4 was required and was done on the abstract only**: the combined error must be read in Sect. 6.2 of the paper before submission.
- Say what the error is: "± 0.101 (stat + sys)", or quote it split as the abstract does.
- Give z_eff = 2.33 and the citation.
- "From the Lyα forest" is loose: the measurement combines the forest auto-correlation with the forest × quasar cross-correlation, and is BAO only. Label it "BAO-only", because the DR2 full-shape analysis gives a different and tighter pair (D_H/r_d = 8.600 ± 0.066, arXiv:2607.27410), with a correlation of opposite sign; mixing the two pairs is a known slip. If D_M/r_d is quoted alongside, its partner is 38.99 ± 0.53 with ρ = −0.431.

`[cosmoskill L4 · base · cosmo-lyman-alpha/results#bao-and-alcock-paczynski-at-z-2-3-current-values]`

Level: L4 — the number is going into a manuscript, for which L4 is mandatory; L1 already holds the value, but a skill file "is never the verification". L4 was reached through the L2 entry as instructed, and completed only as far as the abstract.

Opened:

- `skills/cosmo-lyman-alpha/SKILL.md`: not reopened; lines 1–99 had been read in full for question 3.
- Command: `grep -n -E '8\.632'` on `skills/cosmo-lyman-alpha/references/*.md`, and `grep -n -E '^#|<!-- key'` on `results.md` for the heading.
- `skills/cosmo-lyman-alpha/references/results.md`, lines 8–25.
- Command: `python3 skills/observational-cosmology/scripts/fetch_abstracts.py --help` (the directory `skills/observational-cosmology/scripts/` was listed first).
- Command: `python3 skills/observational-cosmology/scripts/fetch_abstracts.py 2503.14739`.
- No layer command (condition false).

Notes:

- The block in the domain file says "L4: the cited paper itself" and names no tool. The tool is named only in the hub, as `${CLAUDE_SKILL_DIR}/scripts/fetch_abstracts.py`, a path that is right only when the hub is the skill being read; from a domain skill it is `${CLAUDE_SKILL_DIR}/../observational-cosmology/scripts/fetch_abstracts.py`, which no file says.
- The hub's "the body through any tool that gives the paper" could not be followed: no such tool belongs to the package, and the rules of this test allow none. The quantity the draft actually quotes (± 0.101) is not in the abstract, so the one tool the suite provides could not complete the L4 check for this number.
- "L4 starts from the L2 entry" forces a reference-file read although value and citation are both at L1. Here the read paid for itself (it says the combined error is in Sect. 6.2), but the rule does add a step.
- The footer has no form for L4: no `<file>#<key>` designates the paper, and "L4 done on the abstract only" cannot be expressed. The key of the L2 entry was used.

---

## Question 5 — (analyst of the same probe, personal layer) what to keep in mind when quoting compressed P1D parameters

Answer:

- Name the pivot and its unit. DESI DR1 quotes Δ²_★ = 0.379 ± 0.032 and n_★ = −2.309 ± 0.019 at k = 0.009 s/km, z = 3 (arXiv:2601.21432). Other papers use Mpc⁻¹ pivots. Personal layer: this researcher's convention is k in s/km for P1D.
- Name the definition. (Δ²_★, n_★), (A_Lyα, n_Lyα) and (A_P, n_P) are different pairs; values are not comparable across papers until both pivot and definition match.
- Name the mean-flux prior next to the parameters. Personal layer (note FIXTURE-NOTE-7Q): in this group the compressed parameters are always quoted with the mean-flux prior named beside them. Base: the amplitude is degenerate with the mean flux (arXiv:2412.05372), and one eBOSS data vector gave σ8 = 0.733 or 0.841 depending on the analysis.
- Do not compare error bars across generations as like for like: the DR1 slope error is three times the eBOSS one because LLS, Si II–Si II and emulator errors are now marginalised.
- Say which sample: 62,807 spectra at S/N > 3 for cosmology, not the more than 300,000 quasars measured.

The introduction to the estimators is skipped (personal layer: home domain).

`[cosmoskill L1 · base+personal · cosmo-lyman-alpha/skill#errors-that-recur]`

Level: L1 — the cautions are in "Errors that recur" and the headline bullets of the file, and the layer note applies without opening the section it is attached to; L2 (`references/results.md`, §4) would add the table of compressed values, which was not asked.

Opened:

- `skills/cosmo-lyman-alpha/SKILL.md`: not reopened; lines 1–99 had been read in full for question 3.
- Command, run from the repository root with `COSMOSKILL_HOME` pointing at `tests/fixtures/layers/home`: `python3 skills/cosmo-lyman-alpha/../observational-cosmology/scripts/layers.py cosmo-lyman-alpha` (exit status 0). Its output was read in full: the personal profile (home domain `cosmo-lyman-alpha`; conventions "k in s/km for P1D; distances in Mpc/h elsewhere"), one note on `cosmo-lyman-alpha/results#cosmology-from-p1d` (FIXTURE-NOTE-7Q) and one note on `cosmo-lyman-alpha/general` ("Skip the introduction to the FFT and QMLE estimators").
- No reference file.

Notes:

- The layer instructions worked as written: the note attached to `results#cosmology-from-p1d` was applied without opening that section, as the block allows.
- The footer does not say how a layer note attached to a section that was not read should appear: the `<file>#<key>` slot names the base section used (`skill#errors-that-recur`), and the note's own anchor (`results#cosmology-from-p1d`) has no place. A reader of the footer alone would not know where the personal statement came from.
- "Several joined by +" does not say whether `base` is listed when a layer adds to it, nor in which order; `base+personal` was written.
- It is not stated whether profile lines (home domain, conventions) count as "statements from a local layer" to be attributed, or only the notes. Both were attributed.
- The note on `general` concerns the estimators, not the question's subject; under "a note applies when its subject is the question's" it was applied only as an omission.
- Two L1 sections were used and the footer takes one key.

---

## Question 6 — (outsider) is CMB-S4 still going ahead?

Answer:

No. CMB-S4 was cancelled on 9 July 2025, and quoting it as "the plan" is now a recurring error. The ground-based programme that continues is the Simons Observatory (no public data yet); in space, LiteBIRD is now a single telescope with launch in Japanese fiscal year 2036 (arXiv:2607.25285).

`[cosmoskill L1 · base · cosmo-surveys-facilities/skill#what-an-expert-holds-in-mind]`

Level: L1 — the status and its date are a bullet of the file, which answers a yes-or-no question; the circumstances of the cancellation (L2, `references/open-questions.md`) were not asked, and there is no paper to go to for L4.

Opened:

- `skills/cosmo-surveys-facilities/SKILL.md`, lines 1–130 (whole file).
- No command (layer condition false).

Notes:

- Skill choice was unambiguous here: the hub rule "a date, a release or the status of an instrument: `cosmo-surveys-facilities`" overrides `cosmo-cmb`.
- The L1 bullet gives the cancellation with no citation and no flag, and says nothing on who cancelled or why. An outsider is likely to ask next; the file map row "Slips, cancellations … → `references/open-questions.md`" invites the read. It was not made, because L1 answers the question as put.

---

## Question 7 — (analyst) covariance from 1000 mocks, 300 data points, 10 parameters: by how much must the error bars be widened?

Answer:

With n_s = 1000, n_d = 300, n_θ = 10, all values below derived from the formulae of Percival et al. 2022 (arXiv:2108.10402):

- Hartlap factor h = (n_s − 1)/(n_s − n_d − 2) = 999/698 = 1.431.
- B = (n_s − n_d − 2)/[(n_s − n_d − 1)(n_s − n_d − 4)] = 1.435 × 10⁻³; Dodelson–Schneider variance factor 1 + B(n_d − n_θ) = 1.416 (arXiv:1304.2593).
- Covariance to use in χ²: S′ = (n_s − 1)[1 + B(n_d − n_θ)]/(n_s − n_d + n_θ − 1) × S = 1.995 S.

So, in error bar:

- starting from the raw sample covariance S: widen by 41% (√1.995 = 1.413), Hartlap term included;
- if the Hartlap factor is already applied (covariance hS): a further 18% (√(1.995/1.431) = 1.181);
- for reference, the scatter of the best fit against a perfectly known covariance grows by 19% (√1.416 = 1.190).

"Hartlap-corrected" alone is therefore not the full treatment. These numbers are worked out here, not quoted from a paper; the formulae should be checked in arXiv:2108.10402 before the factor is written into a manuscript.

`[cosmoskill L2 · base · cosmo-statistics-inference/physics-and-methods#sample-covariance-from-mocks-and-its-corrections]`

Level: L2 — L1 gives the factors for 100 and 400 data points only, not for 300, so it cannot answer; the formula is in one reference passage and, per the hub, a derivation with no dossier is answered at L2 by applying the formula and labelling the result as derived; L4 was not triggered because nothing is yet being put into a manuscript.

Opened:

- `skills/cosmo-statistics-inference/SKILL.md`, lines 1–113 (whole file).
- Command: `grep -n -E 'Dodelson|Percival|Hartlap'` on `skills/cosmo-statistics-inference/references/physics-and-methods.md` and `results.md` (output cut to 230 characters per line), with `grep -n -E '^#|<!-- key'` on `physics-and-methods.md`.
- Command: `grep -n -E '^\| *1000 *\|'` and `grep -n -E '^#|<!-- key'` on `skills/cosmo-statistics-inference/references/results.md`, to see whether the table of corrections had a row for 300 data points (it has rows for 13, 50, 100, 200 and 400 only).
- `skills/cosmo-statistics-inference/references/physics-and-methods.md`, lines 27–51.
- Command: a one-line `python3 -c` evaluation of h, B, the Dodelson–Schneider factor and S′/S for (1000, 300, 10).
- No layer command (condition false).

Notes:

- Two reference files fit: the file map sends "a method, its formula" to `physics-and-methods.md` and "sizes of corrections" to `results.md`. L2 is "one file". The table of `results.md` has no row for 300 points, so the formula file was read; but the sentence that says which of the factors answers "what does it cost" is in `results.md` (§1.1, the paragraph after the table), which stayed unread except for the fragments shown by the search. The "further 18%" over a Hartlap-corrected covariance is a ratio formed here, not one a file gives.
- The rule that allows working a formula out for the asker's numbers ("Applying a formula") is in the hub only; the block in the domain file is silent on it. Without the hub, an assistant at L2 would not know whether to compute or to quote the two neighbouring rows.
- The L1 bullet is hard to read on one point: "widened by 10% and 65%" follows a parenthesis that gives variance factors, and does not say error bar or variance. The table rows seen in the search output (1.100 and 1.647 under "sqrt(S'/S) (error bar)") show it is the error bar. An L1-only reader could take it either way.
- L1 almost answers by interpolation (300 lies between the tabulated 200 and 400 of the reference table, and between the 100 and 400 of the bullet); the levels do not say whether an interpolated L1 answer is acceptable. It was read as not acceptable.

---

## Instructions that did not work

Could not be followed as written:

1. **Reading the body of the paper at L4** (hub, "Choosing the level": "the body through any tool that gives the paper"). The package supplies an abstract fetcher only. In question 4 the quantity to verify (± 0.101, Sect. 6.2 of arXiv:2503.14739) is not in the abstract, so L4 stopped short and had to be declared "required and not done" for that part.
2. **The path of the abstract fetcher.** It is given only in the hub, as `${CLAUDE_SKILL_DIR}/scripts/fetch_abstracts.py`, which resolves only when the hub is the skill in hand. The "Levels and layers" block of every domain skill sends the reader to "the cited paper itself" and names no tool and no path.
3. **The footer at L4.** The form `<skill>/<file>#<key>` has no value for "the paper", and no way to say that L4 was partial. The key of the L2 entry was used.
4. **The footer for a layer note.** A note attached to a section that the block says need not be opened (`results#cosmology-from-p1d`, question 5) cannot be cited in the footer, whose single `<file>#<key>` slot holds the base section used.

Ambiguous:

5. **When to run the layer command.** The reader must first establish whether `.cosmoskill/` exists "in the working directory, in one of its parents, or in the home directory", for which no command is given, while `layers.py` presumably performs that search itself. "Working directory" is also unclear in a harness whose working directory is not the repository and is reset between commands. Running the command unconditionally would be simpler to state.
6. **The layer slot of the footer.** "Several joined by +" does not say whether `base` is listed with a layer, nor the order; and it is not said whether profile lines count as layer statements to attribute.
7. **The L4 trigger "when two files disagree".** It does not cover a disagreement inside one file or between two cited papers (question 3, z = 4.4 against 4.2).
8. **The L4 trigger by context.** The hub says manuscript, proposal or referee report; the domain block says manuscript only. A referee asking for a checklist (question 1) falls between the two.
9. **"One file of `references/`" at L2.** In question 7 the formula and the reading of the correction factors sit in two files; in question 3 three file-map rows fit. The search-first rule picks the file, but the search output leaks lines of the files that are then not read, so "read only the passage" holds only loosely.
10. **File-map rows that point to L2 for L1 content.** `cosmo-clusters` sends "what a referee asks" to `references/systematics.md`; `cosmo-multimessenger` and `cosmo-statistics-inference` end their L1 checklist with "Details: `references/systematics.md` §…"; `cosmo-surveys-facilities` sends "cancellations" to `references/open-questions.md`. Each pushes towards opening a file that the level rule says is not needed.
11. **Flags at L1.** The hub says the `SKILL.md` bullets carry citations only; every domain `SKILL.md` opens with "Numbers carry provenance flags", and `skills/cosmo-multimessenger/SKILL.md` line 29 carries a `[der]`.
12. **One key for several sections.** Questions 1 and 5 used two L1 sections; the footer takes one.
13. **"Applying a formula" is in the hub only.** A domain skill read on its own does not say that a value absent from L1 and from the tables may be computed at L2 and labelled as derived.
14. **File names in the sizes line.** "open", "methods", "surveys" in "Sizes, in thousands of tokens" are not the names the footer asks for (`open-questions`, `physics-and-methods`, `surveys-and-data`).

Content gaps met on the way (not instructions): the siren H0 at L1 has no unit; the CMB-S4 cancellation at L1 has no citation; the "10% and 65%" of the statistics L1 bullet does not say error bar or variance.
