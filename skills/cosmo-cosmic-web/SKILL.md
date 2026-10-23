---
name: cosmo-cosmic-web
description: Use when reviewing, planning or fact-checking cosmic-web work — T-web, V-web, NEXUS, DisPerSE, Bisous, ORIGAMI, filament, wall, node and void catalogues, mass or volume fractions, connectivity, galaxy properties versus web environment, tidal anisotropy, spin flip and spin–filament alignment (SAMI, MaNGA), WHIM and filament gas from tSZ, kSZ, eROSITA or radio, missing baryons, FRB baryon census, superclusters, protoclusters, web reconstructions from galaxies, Cosmicflows or Lyα tomography.
---

# Cosmic web — expert reference

Snapshot 2026-10-16. Numbers carry provenance flags ([src] / [sec] / [der]);
re-verify against the cited paper before a number enters a manuscript.

## File map
<!-- key: file-map -->

| Question | Load |
|---|---|
| Formation, finders, environment variables, spin theory, filament-gas methods, reconstructions, codes | `references/physics-and-methods.md` |
| Catalogues (CAVITY, DESI, Cosmicflows); X-ray, SZ, radio, FRB, protocluster data; simulations | `references/surveys-and-data.md` |
| Web fractions, filament statistics, environment, spins, filament gas, baryon census, protoclusters, history | `references/results.md` |
| Finder, threshold, redshift-space, confounding, alignment, stacking, reconstruction systematics; referee checklist | `references/systematics.md` |
| Missing baryons, web versus halo mass, spin transition, finder choice, protocluster abundance, stale claims | `references/open-questions.md` |
| Cited-paper metadata | `references/sources.tsv` |
| Spin–filament alignment measurement | `deep/spin-alignments.md` |
| Webs from galaxy surveys; finder agreement | `deep/web-classification.md` |
| Filament-gas stacks: errors, contamination, models | `deep/filament-gas.md` |
| Protocluster selection and masses; supercluster definitions | `deep/protoclusters-superclusters.md` |
| Environment trends at fixed density, halo mass | `deep/environment.md` |
| Absorption-line baryon census | `deep/missing-baryons.md` |

## What an expert holds in mind
<!-- key: what-an-expert-holds-in-mind -->

- Web fractions belong to finders: across twelve methods on one
  simulation, filament mass spans ~10–60%, void volume ~40–90%
  (arXiv:1705.03021, Sect. 5.3).
- Hessian thresholds are conventions: λ_th = 0.2 (T-web), 0.44 (V-web), 0
  (Cosmicflows V-web); a constant-volume threshold is
  proposed (arXiv:1705.03021, arXiv:2606.13538, arXiv:2412.09531).
- DESI void volume fractions span ~6–16% (DR1 T-web) to ~59% (EDR ASTRA,
  tuned to GAMA) (arXiv:2604.02463, arXiv:2604.01456).
- Connectivity: ~6.1 neighbours per node in 3D Gaussian fields, rising with
  peak height and halo mass (arXiv:1803.11477); confirmed over three decades
  of mass in MDPL2 (arXiv:2607.14785).
- At fixed stellar mass, galaxies redden toward filaments (arXiv:1710.02676);
  at fixed local density the SDSS filament–field difference vanishes
  (arXiv:2409.09028), and a halo-mass-only mock reproduces the δ₈–α₅ trends
  (arXiv:1801.04878).
- Halo spin flip: parallel to filaments at low mass, perpendicular at high
  mass; 5 × 10¹¹ h⁻¹M☉ with NEXUS, scaling with filament diameter
  (arXiv:1805.00033).
- SAMI stellar spin transition at log M* = 10.4–10.9
  (arXiv:1909.12371), tied to bulge mass (arXiv:2208.10767); the first MaNGA
  study found none (arXiv:1902.09797).
- Filament X-ray: 9σ total, 5.4σ WHIM after ~40% contamination, eRASS:4,
  7817 SDSS filaments, log T = 6.84 (arXiv:2406.00105, abstract).
- Filament tSZ: 5.3σ between LRG pairs (arXiv:1709.05024), 4.4σ along
  30–100 Mpc filaments (arXiv:1911.09706); oriented ACT DR6 multipoles at
  8–10σ (arXiv:2409.04535).
- FRBs give Ω_b h₇₀ = 0.051 ± 0.006 and f_IGM = 0.76 (+0.10/−0.11)
  (arXiv:2409.16952, abstract); the phase partition is statistical.
- O VII "missing baryons" lines (arXiv:1806.08395) re-analysed: one is
  noise, one possibly intrinsic (arXiv:2305.01587, Sect. 4.4).
- JWST "too many protoclusters" disappears with consistent mass apertures;
  64% of candidates are likely proto-groups (arXiv:2605.28930).

## Systematics a referee checks
<!-- key: systematics-a-referee-checks -->

1. Finder, tracer, smoothing, threshold; a second finder or threshold
   range.
2. Matching in stellar mass and local density or halo mass; centrals and
   satellites; node proximity.
3. Redshift-space and photometric-redshift effects through the same pipeline
   on mocks.
4. Spin tracer (stellar, gas, shape), 2D or 3D, selection and significance
   estimator.
5. Filament-gas masking, background, halo/AGN contamination, null tests.
6. Gas profile model and metallicity behind T and δ.
7. Baryon fraction reference Ω_b and the definition of "missing".
8. Protocluster mass aperture and descendant criterion.
9. Reconstruction: posterior ensemble, survey edges.

## Errors that recur
<!-- key: errors-that-recur -->

- Quoting a web fraction without finder, smoothing and threshold.
- Reading a stellar-mass-matched environmental trend as a tidal effect.
- Saying spins "align with filaments" without the mass dependence.
- Calling stacked filament X-rays pure WHIM; stacks see its hot, dense end.
- Citing arXiv:1806.08395 as settling the baryon census.
- Mixing Codis et al. 2012 and NEXUS spin-flip masses as one number.
- Using a galaxy void as a matter void without dynamical evidence.

## Related skills
<!-- key: related-skills -->

- `cosmo-beyond-two-point`: void and density-split cosmology, void size
  function, topological summaries as statistics.
- `cosmo-lyman-alpha`: tomography surveys, maps, forest-selected
  protoclusters.
- `cosmo-simulations-mocks`: constrained simulations of the local web
  (CLUES, BORG, Manticore, Hamlet-PM).
- `cosmo-weak-lensing`: intrinsic alignments as a shear systematic.
- `cosmo-cmb-lss-cross-correlations`: kSZ, tSZ and gas profiles for
  feedback and cosmology.
- `cosmo-galaxy-halo-connection`: assembly bias and conformity in occupation
  models.
- `cosmo-peculiar-velocities`: Cosmicflows data, bulk flows.
- `cosmo-multimessenger`: FRB dispersion measure as a cosmological probe.

<!-- cosmoskill:block:start — generated by tools/sync_blocks.py, do not edit by hand -->
## Levels and layers
<!-- key: levels-and-layers -->

Answer at the lowest level that answers the question, then stop.

| Level | Read | Holds |
|---|---|---|
| L1 | this file only | the headline values, the state of the domain, the list a referee checks, the errors that recur |
| L2 | one file of `references/` | what this file does not hold: other values, their history, the size of each systematic, methods, releases |
| L3 | one dossier of `deep/` | how a result is obtained and how to choose a method |
| L4 | the cited paper itself | what L1 to L3 quote; required before a number goes into a manuscript, a proposal or a referee report, and when two statements of the skills disagree |

Sizes, in thousands of tokens: L1 3k; open 4k; methods 7k; results 9k; surveys 4k; systematics 4k; deep/environment 7k; deep/filament-gas 8k; deep/missing-baryons 6k; deep/protoclusters-superclusters 8k; deep/spin-alignments 8k; deep/web-classification 9k.

- L2: when the file map names several files, search them for the term
  before reading, and read only the passage.
- L4 starts from the L2 entry: its citation and flag say where to look. Read
  the paper with
  `python3 "${CLAUDE_SKILL_DIR}/../observational-cosmology/scripts/fetch_paper.py" <arXiv id>`
  (`--abstract`, `--outline`, `--section`, `--grep`), or with any tool that
  gives the paper. If it cannot be read, say that L4 was required and not
  done.
- Quote a number only with its paper and the place it was read, as the
  skill gives them; the skill holds no number of its own making. A formula
  may be applied to the asker's numbers; label the result as derived.

Local layers: if a directory `.cosmoskill/` exists in the working directory,
in one of its parents, or in the home directory, or if `COSMOSKILL_HOME` is
set, run
`python3 "${CLAUDE_SKILL_DIR}/../observational-cosmology/scripts/layers.py" cosmo-cosmic-web`
and read what it prints before answering. A note applies when its subject is
the question's; you need not open the section it is attached to. An
override replaces its base section for this researcher: use it, and quote
the base value beside it, both labelled. A suppressed section is left out
and named as suppressed; use it only when the question asks for that
section's own content, and then say that the layer hides it. Say which
statements come from a local layer.

End the answer with one line, `<file>` being `skill` for this file or the
name of the reference file without extension:
`[cosmoskill L<level> · <base, personal, project, or several joined by +> · cosmo-cosmic-web/<file>#<key>]`
The key is the comment under the heading of the section used; leave `#<key>`
out if you did not read that heading. At L4, put the paper and the place
read instead: `arXiv:<id>, <abstract or section>`.
<!-- cosmoskill:block:end -->
