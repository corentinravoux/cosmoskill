---
name: cosmo-theory-foundations
description: Use when checking, deriving or reviewing a theory convention behind a cosmological analysis — distance definitions (D_M, D_H, D_V, D_A), r_d versus r_s, sound-horizon fitting formulae, theta_MC, sigma8 versus sigma12 or sigma_s8, h^-1 Mpc units, growth rate and growth index, Fourier and multipole normalisation, Kaiser formula, fingers of God, streaming model, EFTofLSS counterterms, bias bases, halo model, Limber, wide-angle or relativistic terms, massive-neutrino treatment.
---

# Theory foundations — expert reference

Snapshot 2026-10-07. Numbers carry provenance flags ([src] / [sec] / [der]);
re-verify against the cited paper before a number enters a manuscript.

Read first: hub file `observational-cosmology/references/conventions.md`.

## File map

| Question | Load |
|---|---|
| Definitions and formulae, with the paper and equation that fix each convention | `references/physics-and-methods.md` |
| Which convention Planck, ACT, BOSS/eBOSS, DESI, DES, KiDS adopt | `references/surveys-and-data.md` |
| Size and validity range of each approximation; what superseded what | `references/results.md` |
| Convention traps, sizes at a glance, worked cases, referee checklist | `references/systematics.md` |
| Split conventions, method debates, misconceptions | `references/open-questions.md` |
| Bibliography with roles | `references/sources.tsv` |

## What an expert holds in mind

- BAO alone give Ω_m and h r_d (101.54 ± 0.73 Mpc in DESI DR2), never H0; DESI's r_d = 147.05 Mpc × (ω_b/0.02236)^−0.13 (ω_bc/0.1432)^−0.23 (N_eff/3.04)^−0.1 assumes standard pre-recombination physics (arXiv:2503.14738).
- Three "sound horizons": r_drag = 147.09 Mpc, r_* = 144.43 Mpc (arXiv:1807.06209); the Eisenstein–Hu formula value is 2.75% above the Boltzmann r_drag (arXiv:1303.5076). Calibrated fits reach 0.021% (arXiv:1411.1074).
- D_H is c/H0 in Hogg (arXiv:astro-ph/9905116) and c/H(z) in BAO papers; BAO use D_M, not D_A; Ω_k > 0 is open.
- θ_MC is a CosmoMC approximation to θ_*, not the acoustic angle (arXiv:1303.5076).
- σ8: 8 h⁻¹Mpc, linear, z = 0. Planck uses total matter (arXiv:1303.5076); DESI DR1 full shape "excluding neutrinos" (arXiv:2411.12021).
- The radius moves with h; σ12 removes this, and a template fit measures fσ12 (arXiv:2002.07829). DESI quotes fσ_s8 tied to r_d^fid; eBOSS rescaled σ8 by α_iso (arXiv:2007.08991).
- γ = 0.55 is the ΛCDM value: γ = 0.55 + 0.05[1 + w(z=1)], good to 0.05–0.2% on the growth factor (arXiv:astro-ph/0507263, abstract). Neutrinos make growth scale-dependent at 0.3–2% (arXiv:1708.01154).
- Multipoles carry (2ℓ+1), the Hankel pair i^ℓ; Kaiser multipoles are 1 + 2β/3 + β²/5, 4β/3 + 4β²/7, 8β²/35 (arXiv:astro-ph/9708102).
- The fingers-of-God σ is a pairwise dispersion, √2 above the single-galaxy one (arXiv:astro-ph/9708102); in the EFT it is a counterterm whose amplitude and sign cannot be predicted (arXiv:1909.05277).
- Bias bases differ: co-evolution tidal bias is −2/7 or −4/7 times (b1 − 1); Lagrangian b1 is Eulerian b1 − 1 (arXiv:2404.07272).
- Limber needs k = (ℓ + 1/2)/χ, error O(1/ℓ²) (arXiv:0809.5112); safe for shear, not for tomographic clustering (arXiv:1911.11947, arXiv:2606.23781).
- ΔP/P ≃ −8 f_ν holds only at fixed ω_m on small linear scales (arXiv:astro-ph/0603494); bias and growth belong to the cb field (arXiv:1311.1212).
- Non-linear fits: revised halofit 5–10% (arXiv:1208.2701), HMcode-2020 2.5% RMS (arXiv:2009.01858); halofit biases S8 low (arXiv:2503.19441).
- Prior-volume shifts in full-shape fits reach several σ in extended models (arXiv:2607.02498) and are largely tied to priors in Mpc/h (arXiv:2610.08751).

## Systematics a referee checks

Units of every length, prior and scale cut; field, redshift and h behind σ8;
template or full modelling behind fσ8; D_M or D_A, source of r_d, N_eff; θ_MC
or θ_*; neutrino splitting and field; exact growth or Ω_m^γ; multipole
normalisation; non-linear prescription and range; Limber per probe;
line-of-sight definition; bias basis, counterterms, priors; MAP against mean;
fiducial cosmology. Details: `references/systematics.md` §12.

## Errors that recur

- Converting a BAO result with r_* or an Eisenstein–Hu r_s.
- Reading D_A/r_d as D_M/r_d, or r_s/D_V as D_V/r_d.
- Comparing σ8 or S8 across different fields, neutrino treatments, exponents (0.5, 0.58, 0.4) or h posteriors.
- Plotting BOSS fσ8, DESI fσ_s8 and velocity fσ8 as one quantity.
- Calling γ = 0.55 "general relativity", or using Ω^0.6.
- Comparing tidal-bias or counterterm values between codes.
- Using k = ℓ/χ, or Limber for narrow clustering bins.
- Quoting −8 f_ν without what is held fixed.
- Copying a formula with a printed slip (k_osc "110 h/Mpc" in arXiv:1909.05277); mixing 93.04, 93.14, 93.2 eV or N_eff 3.046 and 3.044.

## Related skills

- `observational-cosmology`: hub, conventions audit list.
- `cosmo-galaxy-clustering`: BAO tables, full-shape results, estimators.
- `cosmo-peculiar-velocities`: velocity statistics, σ_u.
- `cosmo-weak-lensing`: S8 values, shear projections, baryons.
- `cosmo-dark-energy-modified-gravity`: γ and μ–Σ measurements.
- `cosmo-neutrinos-dark-matter`, `cosmo-cmb`, `cosmo-distance-ladder-h0`: Σm_ν and N_eff; CMB parameters; r_d-based H0.
- `cosmo-simulations-mocks`, `cosmo-statistics-inference`, `cosmo-software-ecosystem`: emulator accuracy; projection effects; code versions.
