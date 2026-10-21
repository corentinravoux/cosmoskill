---
name: cosmo-surveys-facilities
description: Use when checking, citing or planning around a survey or facility fact — instrument, aperture, field of view, fibres, sky area, depth, data-release date, public access, status or next milestone — for SDSS-V, DESI, DESI-II, PFS, 4MOST, WEAVE, MOONS, Euclid, Roman, SPHEREx, MUST, Spec-S5, WST, MSE, DES, KiDS, HSC, Legacy Surveys, UNIONS, Rubin LSST, CSST, Planck, ACT, SPT, Simons Observatory, LiteBIRD, CMB-S4, ZTF, CHIME, MeerKAT, SKA, eROSITA, LIGO-Virgo-KAGRA.
---

# Surveys and facilities — expert reference

Snapshot 2026-10-14. Numbers carry provenance flags ([src] / [sec] / [der]);
re-verify against the cited paper before a number enters a manuscript.
Facts flagged `[sec: GC|WL|CMB|SN|CL]` come from the named sibling skill.

## File map
<!-- key: file-map -->

| Question | Load |
|---|---|
| Facility, releases, next step | `references/surveys-and-data.md` |
| Release dates, public data, milestones | `references/results.md` |
| Etendue, multiplex, nP, depth conventions, completeness, fibre assignment, cadence | `references/physics-and-methods.md` |
| Systematic created by each hardware or strategy choice; skill treating it | `references/systematics.md` |
| Slips, cancellations, sibling disagreements, stale claims | `references/open-questions.md` |
| Footprint, tiling, passes, uniform depth | `deep/footprint-tiling-depth.md` |
| Science goal to survey and instrument requirements | `deep/requirements-flowdown.md` |
| Forecasting a survey's reach and validating it | `deep/survey-forecasts.md` |
| Scoring a time-domain cadence: Rubin, deep fields, Roman | `deep/cadence-time-domain.md` |
| Detectors to CMB map depth; noise knees, bands, apertures, sites | `deep/cmb-survey-design.md` |
| Overlaps, shared ground data, joint processing between surveys | `deep/cross-survey-coordination.md` |

## What an expert holds in mind
<!-- key: what-an-expert-holds-in-mind -->

- DESI finished its planned survey in April 2026 and observes through 2028;
  public spectra stop at DR1 (19 March 2025), DR2 being BAO likelihoods only
  (arXiv:2205.10939, arXiv:2503.14745).
- Euclid has three public releases and no cosmology product. DR1-Foundation
  is due 12 November 2026, DR1 mid-2027, DR2 June 2029, DR3 October 2031,
  all tentative (arXiv:2405.13493, arXiv:2405.13492).
- Rubin's ten-year survey began 30 June 2026; Early DP2 came on 27 July
  2026; DR1 will use the first year of data (arXiv:0805.2366).
- Roman launched 30 August 2026 and is in commissioning; its surveys are
  the community-defined ones, not the 2021 reference (arXiv:2505.10574).
- SDSS DR20 (30 July 2026) is current. SDSS-V has no clustering programme;
  eBOSS closed in DR16 (arXiv:2507.06989, arXiv:2112.02026).
- 4MOST (first light 18 October 2025, 2436 fibres), WEAVE and MOONS (first
  observations announced 3 September 2026) are on sky without a confirmed
  main-survey start (arXiv:1903.02464, arXiv:2212.03981, arXiv:2009.00628).
- CMB-S4 was cancelled on 9 July 2025. LiteBIRD is now one telescope, launch
  JFY2036 (arXiv:2607.25285). The Simons Observatory has no public data.
- eROSITA DR2 (31 July 2026) holds catalogues of three all-sky passes of
  the German half; eight were planned (arXiv:2607.27772, arXiv:2010.03477).
- Legacy Surveys DR11 covers about 22,700 deg²; the 14,000 deg² figure is
  the design (arXiv:1804.08657).
- Stage-V spectroscopy: MUST reports construction (arXiv:2605.10102);
  Spec-S5, WST and MSE are designs (arXiv:2608.07927, arXiv:2403.05398,
  arXiv:2503.15553).
- 21 cm cosmology had only cross-correlation detections (arXiv:2202.01242,
  arXiv:2606.25955) until the CHIME auto-spectrum, 12.5σ at z ~ 1
  (arXiv:2511.19620; `cosmo-reionization-21cm`); CHORD's full array is due
  in 2028 (arXiv:2607.09374).
- LVK's O4 ended 18 November 2025; GWTC-5.0 has 267 mergers in its
  population analysis (arXiv:2605.27226) and 236 sources in its cosmology
  analysis (arXiv:2605.27227; `cosmo-multimessenger`); O5 has no date.
- A design number is not a delivered number: check release, area and
  passes before quoting.

## Systematics a referee checks
<!-- key: systematics-a-referee-checks -->

- Fibre-assignment incompleteness and its correction (PIP weights, θ-cut):
  arXiv:1703.02070, arXiv:2411.12025.
- Redshift success by tracer and its focal-plane dependence, against the
  design requirement (DESI: > 90–95% per pointing, arXiv:2205.10939).
- Imaging depth variations and the north/south photometric boundary of the
  targeting imaging.
- Photometric calibration uniformity (arXiv:astro-ph/0703454,
  arXiv:1706.01542).
- Slitless line confusion; CMB beams and scan strategy; 21 cm beam
  knowledge (arXiv:1401.2095).

## Errors that recur
<!-- key: errors-that-recur -->

- Dating a data release by its first cosmology paper.
- Quoting CMB-S4, the 2022 LiteBIRD design or the 2000 deg² Roman HLSS as
  the plan.
- Calling DESI DR2 or Euclid DR1 public.
- Comparing depths across surveys without the S/N and aperture convention.
- Quoting a GW candidate count without its threshold (arXiv:2605.27226).
- Comparing figures of merit computed with different priors.
- Treating ZTF SN Ia DR2 as a cosmology sample (arXiv:2409.04346).
- Using a pre-2026 start date for Rubin, Roman, 4MOST, MOONS or CSST.

## Related skills
<!-- key: related-skills -->

Sample sizes, estimators and results live in the probe skills:
`cosmo-galaxy-clustering`, `cosmo-lyman-alpha`, `cosmo-weak-lensing`,
`cosmo-cmb`, `cosmo-supernovae`, `cosmo-clusters`,
`cosmo-peculiar-velocities`, `cosmo-reionization-21cm`,
`cosmo-multimessenger`. Figure-of-merit conventions:
`cosmo-dark-energy-modified-gravity`, `cosmo-statistics-inference`. Mocks
that mimic a survey: `cosmo-simulations-mocks`. Hub:
`observational-cosmology`.

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

Sizes, in thousands of tokens: L1 3k; open 5k; methods 7k; results 5k; surveys 13k; systematics 7k; deep/cadence-time-domain 7k; deep/cmb-survey-design 7k; deep/cross-survey-coordination 8k; deep/footprint-tiling-depth 8k; deep/requirements-flowdown 6k; deep/survey-forecasts 6k.

- L2: when the file map names several files, search them for the term
  before reading, and read only the passage.
- L4 starts from the L2 entry: its citation and flag say where to look. Read
  the paper with
  `python3 "${CLAUDE_SKILL_DIR}/../observational-cosmology/scripts/fetch_paper.py" <arXiv id>`
  (`--abstract`, `--outline`, `--section`, `--grep`), or with any tool that
  gives the paper. If it cannot be read, say that L4 was required and not
  done.
- A formula of the skill may be applied to the asker's numbers; label the
  result as derived.

Local layers: if a directory `.cosmoskill/` exists in the working directory,
in one of its parents, or in the home directory, or if `COSMOSKILL_HOME` is
set, run
`python3 "${CLAUDE_SKILL_DIR}/../observational-cosmology/scripts/layers.py" cosmo-surveys-facilities`
and read what it prints before answering. A note applies when its subject is
the question's; you need not open the section it is attached to. An
override replaces its base section for this researcher: use it, and quote
the base value beside it, both labelled. A suppressed section is left out
and named as suppressed; use it only when the question asks for that
section's own content, and then say that the layer hides it. Say which
statements come from a local layer.

End the answer with one line, `<file>` being `skill` for this file or the
name of the reference file without extension:
`[cosmoskill L<level> · <base, personal, project, or several joined by +> · cosmo-surveys-facilities/<file>#<key>]`
The key is the comment under the heading of the section used; leave `#<key>`
out if you did not read that heading. At L4, put the paper and the place
read instead: `arXiv:<id>, <abstract or section>`.
<!-- cosmoskill:block:end -->
