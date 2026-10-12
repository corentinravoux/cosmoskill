# RED against GREEN — waves 3 and 4

2026-10-12. `baseline-wave34.md` is the memory-only sheet (no tools, no
skill); `green-wave34.md` is the same fourteen questions answered from the
nine wave-3 and wave-4 skill files only.

## What the baseline got wrong or could not know

| Q | Baseline (memory) | In the skills, from source | Kind of failure |
|---|---|---|---|
| 3 | joint birefringence angle "my own inverse-variance estimate", about 4.5–4.7σ | published joint analysis: β = 0.277° ± 0.057°, 4.8σ, 3.5σ with dust mitigation (arXiv:2608.06480) | after the cutoff |
| 7 | Manticore-Local "finds only a modest local underdensity, of order 5 %" | "no evidence for a large local underdensity" (arXiv:2505.10682); the 5 % is SIBELIUS-DARK; extension to SDSS/BOSS unknown to the baseline: (4 h⁻¹Gpc)³ at about 4 Mpc/h (arXiv:2606.10020) | attribution; after the cutoff |
| 8 | Euclid DR1 "21 October 2026"; eROSITA DR2 "eRASS1–4" | DR1-Foundation 12 November 2026, DR1 mid-2027; eROSITA DR2 holds catalogues of three passes (arXiv:2607.27772) | stale schedule; wrong content |
| 9 | clustering-aware mocks "roughly 3σ" (guess); DESI redshift dipole unknown | 3.63σ and 3.44σ (arXiv:2511.00822); v ≈ 358 km/s (arXiv:2608.30914) | missed; after the cutoff |
| 10 | reassessment of the joint CMB-anomaly claim "I do not recall the paper" | about 3σ after look-elsewhere correction (arXiv:2602.10178) | missed |
| 10, 1 | CMB-SPA H0 = 67.24 ± 0.35; n_s = 0.9684 ± 0.0030 | 67.19 ± 0.38; 0.9679 ± 0.0033 in the current arXiv version | first-version values |
| 11 | MWA limit "(30–43 mK)²" from a 2020 paper; MeerKLASS auto-spectrum unknown | (23.0 mK)² (arXiv:2508.04164); MeerKLASS at z = 0.42 (arXiv:2610.12158) | stale; after the cutoff |
| 12 | latest LVK value "GWTC-4.0, 76.6 (+13.0/−9.5)" | GWTC-5.0: 71.7 (+9.4/−7.5), 236 sources, DES Y6 catalogue (arXiv:2605.27227); the GWTC-4.0 abstract reads 75.4 (+12.8/−9.1) | missed a pre-cutoff paper; value differs |
| 14 | CAMB v2: "I do not reliably remember"; EFTCAMB successor: "not sure one exists" | arXiv:2607.14854; H-EFTCAMB, "the official successor" (arXiv:2603.01662) | after the cutoff; missed |

Right from memory: Planck and PR4 f_NL, the DESI f_NL and its assumption,
BK18 and the SPT-3G r limit, the DESI DR2 + CMB Bayes factor, the code
comparison and COLA accuracies, GLADE+ completeness, the Limber error, flip's
units.

## A point to the baseline: an error in a skill

Question 5. The baseline evaluated the Dodelson–Schneider formula and gave 5 %
and 28 % on the error bar for 100 and 400 data points with 1000 mocks. The
skill said "10 % on the error bar … 65 %". Recomputed by the coordinator: the
Dodelson–Schneider variance factors are 1.100 and 1.653 (5 % and 29 % on the
error bar); the skill's 10 % and 65 % are the last column of its own table,
the widening to apply to a posterior built on the raw sample covariance,
Hartlap term included (factors 1.100 and 1.647). Two different quantities
that happen to be numerically close. The skill's sentence was ambiguous to the
point of being wrong as read; four passages now state both. (The coordinator's
first correction replaced one reading by the other and was itself redone.)

## What the skills delivered

Fourteen of fourteen questions answered from the files; two answers followed
an explicit pointer to `cosmo-cmb`. No wrong-file navigation.

## Conflicts and gaps found by GREEN, and what was done

| Found | Action |
|---|---|
| τ from Planck low-ℓ: 0.054–0.063 (reionisation skill) against 0.051–0.063 (tensions, CMB skills) | the lower end is NPIPE, 0.051 ± 0.006 (arXiv:2007.04997), tabulated `[src]` in `cosmo-cmb`; the reionisation skill now gives the full range and says where the lowest value comes from |
| CHIME auto-spectrum: "not found" in the facilities file, 12.5σ in its own SKILL.md and in the reionisation skill | facilities entry corrected, item removed from its "Not verified" list |
| "BK18 is the latest B-mode measurement" against SPT-3G r < 0.25 (2025) in the same skill | wording changed to "tightest"; the SPT-3G limit named as not competitive |
| MWA limit quoted as (23.0 mK)² in one place and 470 mK² in another | both polarisations of the same paper; SKILL.md now gives both |
| Facilities file sent the reader to "Sect. 2.7" for the Euclid calendar; 2.7 is UNIONS | pointer corrected |
| Euclid DR2: June 2029 (ESA) against March 2029 (IPAC) | documented in the files as a disagreement between two official pages; no edit |
| Not in the skills: constant A of the Percival 2014 factor; Planck 2018 r_drag for other data combinations; Planck z_drag | left as declared gaps |

Offline consistency check after the edits: clean on the five skills touched.
The arXiv API was rate-limiting at the time; the rows added were copied from
sibling bibliographies already verified.
