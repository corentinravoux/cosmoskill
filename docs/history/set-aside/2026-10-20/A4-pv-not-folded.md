# A.4 — text of the two PV hub files not folded into the standard five

Plan item A.4 of `docs/plans/2026-10-20-plan.md`. Sources:
`skills/cosmo-peculiar-velocities/references/pv-surveys.md` and
`skills/cosmo-peculiar-velocities/references/fsigma8-pv-compilation.md`, deleted on 2026-10-20
after their content was folded into `physics-and-methods.md`, `surveys-and-data.md`, `results.md`,
`systematics.md` and `open-questions.md` of that skill. Verbatim copies of both files:
`A4-pv-surveys.original.md` and `A4-fsigma8-pv-compilation.original.md` in this directory. The map
from every old section key to the section that now holds it is
`skills/cosmo-peculiar-velocities/references/retired-keys.tsv`.

Below, under the original headings, is everything that was not folded, verbatim, with the reason.
Statements not listed here are in the skill.

---

## pv-surveys.md

### Preamble

> **Verify before citing**: the numbers below were read from the sources named in each row, but
> any number entering a manuscript should be re-checked against the paper itself.

Not folded: the same rule is stated for the whole skill in its `SKILL.md` (L4 is required before a
number goes into a manuscript).

> and it is the natural single citation for a manuscript paragraph introducing the field.

Not folded: manuscript writing advice. The review itself (Turner 2024, arXiv:2411.19484) is cited
as the source of the survey descriptions in `surveys-and-data.md` §0.

### 1. Why there are exactly three indicators

> Corollary worth stating in any manuscript:

Not folded: writing advice; the corollary itself is in `surveys-and-data.md` §0.

### 5. Method families

> Nothing is lost by keeping the two axes apart.

> Two consequences to watch for:

> take that wording over any review's classification.

Not folded: editorial remarks without content of their own. The two axes, the two consequences
(Howlett et al. 2017; Adams & Blake 2017 as origin of the method) and the fact that Lai et al. 2023
and the DESI analysis name the method in their abstracts are in `physics-and-methods.md` §0.

### 6. Published fσ8 measurements from peculiar velocities

> Discussion companion: `fsigma8-pv-compilation.md`.

Not folded: pointer to a deleted file (the companion is merged into the same section).

Carried over in a different notation (recorded here for the conservation check, not a loss): the
rows "Feix et al. 2015 | 0.370 ± 0.130" and "Feix et al. 2017 | 0.480 ± 0.160" are the rows
0.37 ± 0.13 and 0.48 ± 0.16 of `results.md` §0 (same values, written as in the 2026-08-13
table), and "CF4++ (65331 distances)" is written "65 331" there.

### 9. Writing rules for PV sections

Not folded: manuscript writing guidance in the owner's voice, not referee-checkable facts. Each
fact a rule rests on is in the skill: z_eff range and the σ8 convention in `results.md` §0, §0a,
§0b; method families and their failure modes in `physics-and-methods.md` §0; CF4 as a compilation
in `surveys-and-data.md` §1; forecasts against measurements in `results.md` §0c and
`open-questions.md` §8; "forward model" and linear dynamics in `physics-and-methods.md` §5 and
`open-questions.md` §10; the `der` rows in `results.md` §0.

> - Never write "the peculiar velocity survey X measures fσ8" without the
>   **effective redshift** — the compilation above spans z_eff = 0 to 0.1 and the
>   values are not comparable across it.
> - Name the **method family** (§5), not just "maximum likelihood": that names the
>   optimiser, which nearly every analysis in the table uses. The DESI DR1 spread
>   across three estimators on identical data shows why the family matters.
> - State the **σ8 normalisation** when quoting a velocity–density comparison.
>   Six results in the table are fσ8_lin, and the offset is 6.5%.
> - When quoting CF4-based results, say that CF4 is a compilation containing the
>   other samples — otherwise the reader counts the same galaxies twice.
> - Distinguish **forecast** from **measurement** explicitly; much of the recent
>   PV literature is forecasts (LSST, 4HS, WALLABY).
> - The families have different failure modes and are not interchangeable:
>   field-level inference stands on its covariance model, two-point statistics on
>   the estimator and its fitting template, velocity–density comparison on an
>   external density field and on linear theory. Say which one a number came from.
> - Never let "forward model" imply non-linear dynamics. Four papers in the table
>   forward-model the *distance indicator* against a linear-theory field; no
>   published fσ8 comes from a particle-evolving forward model at all (§5).
> - Do not quote a `der` row (Carrick 2015, Davis 2011, Nusser 2017) in a
>   modified-gravity context: those papers measure Ωm^0.55·σ8 or β, and reading
>   them as fσ8 assumes the answer.

---

## fsigma8-pv-compilation.md

### Preamble

> Compiled **2026-08-13**, method families added **2026-08-14**. Companion to
> `pv-surveys.md` (surveys, systematics, and the method-family definitions in §5).
>
> This file is a table for reading and its discussion. It is not a data
> product: a compilation meant to be loaded by code belongs in a data package
> with its own integrity tests.

Not folded: the dates are kept in the fold line of every receiving section ("the compilation of
2026-08-12/14"); the pointer is to a deleted file; the data-product remark is the owner's workflow
note about a separate data package, not part of the skill.

### 1. Measurements from data — DESI DR1 Peculiar Velocity Survey (2025)

> is the
> single most useful number in this file.

Not folded: a ranking of the file's own content. The statement it introduces (the 0.391 → 0.483
spread as the scale of method systematics) is in `open-questions.md` §4, beside the papers'
opposite reading.

### 2. Forecasts and simulation validation — NOT measurements

> Keep these visually and verbally separate from §1. Mixing them is the most
> common error in PV review figures.

Not folded: figure-making advice, and the second sentence is an unsourced judgment. The separation
itself is kept: forecasts and simulations are a section of their own, `results.md` §0c.

### 4b. Linear vs non-linear σ8 — verified 2026-08-13

> turned up a normalisation split that no review flags and that this file previously hid.

Not folded: framing about the file's own history; the split is in `results.md` §0b.

> Column `sigma8_norm` in the data file records this per row.

Not folded: refers to the owner's data file outside the package. The convention is recorded per
row in the `lin` flag of `results.md` §0.
