---
name: cosmo-inflation-primordial
description: Use when reviewing, planning or fact-checking inflation and primordial-physics claims — spectral index n_s and running, the ACT DR6 n_s shift, Starobinsky or α-attractor viability, tensor-to-scalar ratio r, B modes (BICEP/Keck BK18, SPT-3G, Simons Observatory, LiteBIRD), delensing, primordial non-Gaussianity f_NL (Planck bispectrum, scale-dependent bias, b_φ, DESI, SPHEREx, Euclid), isocurvature, spatial curvature Ω_K, primordial features, cosmic birefringence.
---

# Inflation and primordial physics — expert reference

Snapshot 2026-10-14. Numbers carry provenance flags ([src] / [sec] / [der]);
re-verify against the cited paper before a number enters a manuscript.

## File map
<!-- key: file-map -->

| Question | Load |
|---|---|
| Values and history: n_s, running, r, f_NL, isocurvature, Ω_K, features, β | `references/results.md` |
| Definitions, slow roll, estimators, likelihoods, blinding, codes, conventions | `references/physics-and-methods.md` |
| B-mode experiments, CMB combinations, f_NL samples, SPHEREx, Euclid | `references/surveys-and-data.md` |
| Systematic sizes; referee checklist | `references/systematics.md` |
| n_s debate, b_φ, curvature, birefringence, forecasts, stale claims | `references/open-questions.md` |
| Dust and synchrotron cleaning for r | `deep/bmode-foreground-separation.md` |
| Delensing templates for r | `deep/delensing.md` |
| Galaxy-bispectrum f_NL: model, priors, cuts | `deep/lss-bispectrum-png.md` |
| CMB bispectrum estimators, validation | `deep/cmb-bispectrum.md` |
| BB likelihood for r: purification, windows, null tests | `deep/tensor-bmode-likelihood.md` |
| Slow-roll fits, reheating priors, model evidences | `deep/slow-roll-model-comparison.md` |
| Bibliography with roles | `references/sources.tsv` |

## What an expert holds in mind
<!-- key: what-an-expert-holds-in-mind -->

- n_s (ΛCDM): 0.9649 ± 0.0042 (Planck 2018, arXiv:1807.06211), 0.9679 ± 0.0033 (CMB-SPA, arXiv:2506.20707), 0.974 ± 0.003 (P-ACT-LB, with DESI BAO; arXiv:2503.14452).
- 0.974 partly reflects the CMB–BAO tension (arXiv:2507.12459): with Ω_K or w0wa free, n_s is 0.967–0.972 (arXiv:2607.28445); with α_s, N_eff, Σm_ν free its error doubles (arXiv:2609.35964).
- Starobinsky: 2σ edge of P-ACT-LB + BK18 for N = 50–60, in ΛCDM (arXiv:2503.14454); refined predictions stay within 2σ for N ≳ 58 (arXiv:2504.20757).
- Running: 0.0062 ± 0.0052 (arXiv:2503.14454); eBOSS Lyα −0.010 ± 0.004 is superseded (arXiv:2601.21432).
- r_0.05 < 0.036 at 95%, σ(r) = 0.009 (BK18, arXiv:2110.00483) remains the tightest; SPT-3G alone gives r < 0.25 (arXiv:2505.02827); 0.032 (arXiv:2112.07961) and 0.038 (ACT) reuse it.
- Forecasts: SO with six SATs, σ(r) = 1.2 (1.4) × 10⁻³ with 70% (50%) delensing (arXiv:2512.15833); LiteBIRD after reformation, δr < 0.002 (arXiv:2607.25285).
- CMB f_NL: local −0.9 ± 5.1, equilateral −26 ± 47, orthogonal −38 ± 24 (Planck 2018, arXiv:1905.05697); PR4: −0.1 ± 5.0, 6 ± 46, −8 ± 21 (arXiv:2504.00884).
- Galaxy surveys measure f_NL·b_φ. DESI DR1: −3.6 ± 9 (quasar p = 1.6) or +3.5 (p = 1) (arXiv:2411.17623); one BOSS data vector: σ = 16–226 (arXiv:2205.05673). ±4.1 (CMB + DESI) is an external bispectrum reanalysis (arXiv:2512.04266).
- SPHEREx launched 11 March 2025; Δf_NL < 0.5 is required, assuming universality (arXiv:2511.02985). Euclid forecasts 2.2 (arXiv:2507.15819).
- Isocurvature: Planck β_iso(k = 0.002 Mpc⁻¹) < 2.5% for CDI, < 0.1% if fully correlated (arXiv:1807.06211).
- Ω_K < 0 is closed. Planck-alone −0.044 +0.018/−0.015 is the A_L feature (arXiv:1807.06209); DESI DR2 + CMB: +0.0023 ± 0.0011 (arXiv:2503.14738).
- Features: amplitudes below 2% (arXiv:2606.28310); a 3σ DESI fixed-cosmology feature vanishes with cosmology free (arXiv:2610.10530).
- Birefringence: β = 0.342° +0.094/−0.091 (WMAP + Planck, arXiv:2205.13962), 0.215° ± 0.074° (ACT, arXiv:2509.13654), 0.277° ± 0.057° jointly, 4.8σ; no detection claimed (arXiv:2608.06480).

## Systematics a referee checks
<!-- key: systematics-a-referee-checks -->

- n_s: CMB combination, arXiv version, BAO, model.
- r: dust complexity (bias up to 0.03, arXiv:2508.00073), beam leakage (10⁻³, arXiv:2608.25016), point sources (1–3 × 10⁻³, arXiv:2110.00483), delensing, ℓ_knee.
- CMB f_NL: lensing–ISW subtraction (+5 on local), simulations.
- Galaxy f_NL: b_φ prior, imaging weights, integral constraints; bispectrum bias priors.
- Ω_K: likelihood, discordant data, dark-energy model.
- Features: global significance, varied cosmology.
- Birefringence: angle calibration, dust EB.

## Errors that recur
<!-- key: errors-that-recur -->

- "ACT measured n_s = 0.974": P-ACT gives 0.9709 ± 0.0038.
- "Starobinsky is excluded", without model, N and data.
- r < 0.032 taken as newer B-mode data than r < 0.036.
- r_ect < 0.0077 (causal sources, arXiv:2601.20958) quoted as inflationary.
- Citing CMB-S4 or pre-reformation LiteBIRD targets.
- f_NL = 0.8 ± 5.0 (2015, preliminary) as Planck's result.
- Giving a galaxy f_NL without p.
- "Planck shows a closed universe"; "negative curvature" for Ω_K < 0.
- "Birefringence detected"; 0.30° ± 0.05° omits the angle systematic (arXiv:2507.16714).
- BICEP/Keck is blind to a constant β (arXiv:2603.06812).

## Related skills
<!-- key: related-skills -->

- `cosmo-cmb`: likelihoods, τ, A_L, instruments.
- `cosmo-galaxy-clustering`, `cosmo-beyond-two-point`: DESI samples, bispectrum, EFT.
- `cosmo-cmb-lss-cross-correlations`: f_NL from lensing or kSZ.
- `cosmo-lyman-alpha`: P1D behind the running.
- `cosmo-dark-energy-modified-gravity`, `cosmo-neutrinos-dark-matter`: w0wa; axions.
- `cosmo-tensions-anomalies`, `cosmo-theory-foundations`: CMB–BAO tension; inflationary theory.

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

Sizes, in thousands of tokens: L1 3k; open 7k; methods 11k; results 12k; surveys 5k; systematics 12k; deep/bmode-foreground-separation 7k; deep/cmb-bispectrum 8k; deep/delensing 7k; deep/lss-bispectrum-png 7k; deep/slow-roll-model-comparison 6k; deep/tensor-bmode-likelihood 7k.

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
`python3 "${CLAUDE_SKILL_DIR}/../observational-cosmology/scripts/layers.py" cosmo-inflation-primordial`
and read what it prints before answering. A note applies when its subject is
the question's; you need not open the section it is attached to. An
override replaces its base section for this researcher: use it, and quote
the base value beside it, both labelled. A suppressed section is left out
and named as suppressed; use it only when the question asks for that
section's own content, and then say that the layer hides it. Say which
statements come from a local layer.

End the answer with one line, `<file>` being `skill` for this file or the
name of the reference file without extension:
`[cosmoskill L<level> · <base, personal, project, or several joined by +> · cosmo-inflation-primordial/<file>#<key>]`
The key is the comment under the heading of the section used; leave `#<key>`
out if you did not read that heading. At L4, put the paper and the place
read instead: `arXiv:<id>, <abstract or section>`.
<!-- cosmoskill:block:end -->
