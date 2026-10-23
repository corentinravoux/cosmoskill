# R10 set-aside — cosmo-peculiar-velocities/references/physics-and-methods.md §0

Run R10 of step 4 (docs/plans/2026-10-21-plan.md), 2026-10-22. Verbatim copy of §0 "Method families"
(lines 11-36) before R10 rewrote it to set the classifications of the reviews and comparison papers side
by side. The classification by data compression below is the package owner's; R10 keeps it in the base as
one of the classifications (the one the fσ8 table of results.md §0 uses), condensed.

## 0. Method families
<!-- key: method-families -->

Folded on 2026-10-20 from the compilation of 2026-08-12/14, in which `[src]` meant "traced to the
paper" and `[der]` "relabelled or derived, the paper does not quote fσ8".
Grouped by **what the estimator does to the data before fitting**, not by the optimiser: almost
every analysis maximises a likelihood, so "maximum likelihood" is a fitting detail, not a family.
Boundaries follow each paper's own words; "Rows" counts rows of the fσ8 table (`results.md` §0).

| Family | What it does | Depends on | Rows | Here |
|---|---|---|---|---|
| Field-level likelihood-based inference | the likelihood of the observed density and velocity *field values* is written through a model covariance and maximised or sampled; no summary statistic is measured first ("maximum likelihood fields") | the covariance model and its non-linear damping | 6 | §3 |
| Two-point statistics | a correlation function, power or momentum spectrum is *measured*, then fitted | the estimator, its window, the fitting template | 16 | §4 |
| Velocity–density comparison, linear | the velocity field is *predicted* from a redshift-survey density field by **linear theory** — directly, or through a Wiener filter / constrained realisation, still linear dynamics | an external density field, its bias, linear theory | 13 | §5 |
| Velocity–density comparison, particle forward model | the same, with the field evolved from initial conditions by a **gravity solver on a particle field** (LPT, COLA, particle-mesh, N-body), mildly non-linear | the solver, its resolution, the initial-condition prior | **0** | §5 |

The fitting technique is a separate axis: forward likelihood (Boruah 2020, Stahl 2021), forward
model (Boubel 2024), hierarchical Bayes (Stiskalek 2026, Ma+2012), MCMC, χ². The families fail
differently: on the covariance model; on the estimator and template; on the external density field
and linear theory. Turner (2024) Table 1 puts "maximum-likelihood" beside "power spectrum" and
"correlation function" (a fitting label among observables) and groups Howlett+2017 with the
maximum-likelihood analyses, though it measures and fits the velocity power spectrum (its abstract
finds the Watkins & Feldman estimator "suitable for measuring the velocity power spectrum") [src:
arXiv:1706.05130, abstract]. Per Lai+2023, "In the development of the maximum likelihood fields
method, Adams & Blake (2017) were the first to simultaneously model..."; Lai+2023 (arXiv:2209.04166)
and the DESI analysis (arXiv:2512.03229) name the method in their own abstracts.
