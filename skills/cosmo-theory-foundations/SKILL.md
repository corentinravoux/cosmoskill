---
name: cosmo-theory-foundations
description: Use when checking, deriving or reviewing a theory convention behind a cosmological analysis — distance definitions (D_M, D_H, D_V, D_A), r_d versus r_s, sound-horizon fitting formulae, theta_MC, sigma8 versus sigma12 or sigma_s8, h^-1 Mpc units, growth rate and growth index, Fourier and multipole normalisation, Kaiser formula, fingers of God, streaming model, EFTofLSS counterterms, bias bases, halo model, Limber, wide-angle or relativistic terms, massive-neutrino treatment.
---

# Theory foundations — expert reference

Snapshot 2026-10-15. Flags [src] / [sec] / [der]; re-verify at source before
a number enters a manuscript.

Read first: `observational-cosmology/references/conventions.md`.

## File map
<!-- key: file-map -->

| Question | Load |
|---|---|
| Definitions and formulae, with the paper and equation fixing each | `references/physics-and-methods.md` |
| Conventions of Planck, ACT, BOSS/eBOSS, DESI, DES, KiDS | `references/surveys-and-data.md` |
| Accuracy of each approximation; what superseded what | `references/results.md` |
| Convention traps and their sizes, worked cases, referee checklist | `references/systematics.md` |
| Split conventions, method debates, misconceptions | `references/open-questions.md` |
| Bibliography with roles | `references/sources.tsv` |
| Relativistic counts, magnification and evolution bias, two-population dipole | `deep/relativistic-wide-angle.md` |
| Computing C_ℓ: kernels, spin prefactors, Limber variants, non-Limber codes | `deep/projected-statistics-limber.md` |
| Building halofit or HMcode-2020; halo-model normalisation; neutrinos | `deep/halo-model-nonlinear.md` |

## What an expert holds in mind
<!-- key: what-an-expert-holds-in-mind -->

- BAO alone give Ω_m and h r_d (101.54 ± 0.73 Mpc in DESI DR2), never H0; DESI's r_d = 147.05 Mpc × (ω_b/0.02236)^−0.13 (ω_bc/0.1432)^−0.23 (N_eff/3.04)^−0.1 assumes standard pre-recombination physics (arXiv:2503.14738).
- Three "sound horizons": r_drag = 147.09 Mpc, r_* = 144.43 Mpc (arXiv:1807.06209); Eisenstein–Hu r_s is 2.75% above Boltzmann r_drag (arXiv:1303.5076). Calibrated fits reach 0.021% (arXiv:1411.1074).
- D_H is c/H0 in Hogg (arXiv:astro-ph/9905116) and c/H(z) in BAO papers; BAO use D_M, not D_A; Ω_k > 0 is open.
- θ_MC is a CosmoMC approximation to θ_*, not the acoustic angle (arXiv:1303.5076).
- σ8: 8 h⁻¹Mpc, linear, z = 0. Planck uses total matter (arXiv:1303.5076); DESI DR1 full shape "excluding neutrinos" (arXiv:2411.12021).
- The radius moves with h; σ12 removes this, and a template fit measures fσ12 (arXiv:2002.07829). DESI quotes fσ_s8 tied to r_d^fid; eBOSS rescaled σ8 by α_iso (arXiv:2007.08991).
- γ = 0.55 is the ΛCDM value: γ = 0.55 + 0.05[1 + w(z=1)], 0.05% on the growth factor for Λ, 0.4–0.5% for w = −0.5 or −1.5 (arXiv:astro-ph/0507263, Sect. V.1). Neutrinos make growth scale-dependent at 0.3–2% (arXiv:1708.01154).
- Multipoles carry (2ℓ+1), the Hankel pair i^ℓ; Kaiser multipoles are 1 + 2β/3 + β²/5, 4β/3 + 4β²/7, 8β²/35 (arXiv:astro-ph/9708102).
- Fingers-of-God σ is pairwise, √2 above the single-galaxy one (arXiv:astro-ph/9708102); in the EFT a counterterm of unpredictable amplitude and sign (arXiv:1909.05277).
- Bias bases differ: co-evolution tidal bias is −2/7 or −4/7 times (b1 − 1); Lagrangian b1 is Eulerian b1 − 1 (arXiv:2404.07272).
- Limber needs k = (ℓ + 1/2)/χ, error O(1/ℓ²), ~1% only above ℓ ≈ 5χ/σ_χ for one bin (arXiv:0809.5112); safe for shear, not for tomographic clustering (arXiv:1911.11947, arXiv:2606.23781).
- ΔP/P ≃ −8 f_ν holds only at fixed ω_m on small linear scales (arXiv:astro-ph/0603494); bias and growth belong to the cb field (arXiv:1311.1212).
- Non-linear fits: revised halofit 5–10% (arXiv:1208.2701); on common emulator nodes 5.0% RMS against 2.5% for HMcode-2020 (arXiv:2009.01858); halofit biases S8 low (arXiv:2503.19441).
- Full-shape prior-volume shifts reach several σ in extended models (arXiv:2607.02498), largely from priors in Mpc/h (arXiv:2610.08751).

## Systematics a referee checks
<!-- key: systematics-a-referee-checks -->

Units of lengths, priors, scale cuts; field, redshift, h behind σ8; template
or full modelling behind fσ8; D_M or D_A, r_d source, N_eff; θ_MC or θ_*;
neutrino splitting and field; exact growth or Ω_m^γ; multipole normalisation;
non-linear prescription and range; Limber per probe; line of sight; bias
basis, counterterms, priors; MAP or mean; fiducial cosmology.
`references/systematics.md` §12.

## Errors that recur
<!-- key: errors-that-recur -->

- Converting a BAO result with r_* or an Eisenstein–Hu r_s.
- Reading D_A/r_d as D_M/r_d, or r_s/D_V as D_V/r_d.
- Comparing σ8 or S8 across fields, neutrino treatments, exponents (0.5, 0.58, 0.4) or h posteriors.
- Plotting BOSS fσ8, DESI fσ_s8 and velocity fσ8 as one quantity.
- Calling γ = 0.55 "general relativity", or using Ω^0.6.
- Comparing tidal-bias or counterterm values between codes.
- Using k = ℓ/χ, or Limber for narrow clustering bins.
- Quoting −8 f_ν without what is held fixed.
- Copying a printed slip (k_osc "110 h/Mpc", (b1 + fμ)² in Eq. A.1 of arXiv:1909.05277); mixing 93.04, 93.14, 93.2 eV or N_eff 3.046 and 3.044.

## Related skills
<!-- key: related-skills -->

- `observational-cosmology`: hub, conventions audit list.
- `cosmo-galaxy-clustering`: BAO tables, full-shape results, estimators.
- `cosmo-peculiar-velocities`: velocity statistics, σ_u.
- `cosmo-weak-lensing`: S8 values, shear projections, baryons.
- `cosmo-dark-energy-modified-gravity`: γ and μ–Σ measurements.
- `cosmo-neutrinos-dark-matter`, `cosmo-cmb`, `cosmo-distance-ladder-h0`: Σm_ν, N_eff; CMB parameters; r_d-based H0.
- `cosmo-simulations-mocks`, `cosmo-statistics-inference`, `cosmo-software-ecosystem`: emulator accuracy; projection effects; code versions.

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

Sizes, in thousands of tokens: L1 3k; open 7k; methods 18k; results 7k; surveys 9k; systematics 9k; deep/halo-model-nonlinear 6k; deep/projected-statistics-limber 6k; deep/relativistic-wide-angle 7k.

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
`python3 "${CLAUDE_SKILL_DIR}/../observational-cosmology/scripts/layers.py" cosmo-theory-foundations`
and read what it prints before answering. A note applies when its subject is
the question's; you need not open the section it is attached to. Say which
statements come from a local layer.

End the answer with one line, `<file>` being `skill` for this file or the
name of the reference file without extension:
`[cosmoskill L<level> · <base, personal, project, or several joined by +> · cosmo-theory-foundations/<file>#<key>]`
The key is the comment under the heading of the section used; leave `#<key>`
out if you did not read that heading. At L4, put the paper and the place
read instead: `arXiv:<id>, <abstract or section>`.
<!-- cosmoskill:block:end -->
