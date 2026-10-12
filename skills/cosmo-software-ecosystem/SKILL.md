---
name: cosmo-software-ecosystem
description: Use when choosing, citing, comparing or debugging a cosmology code, or checking its units, defaults, version or maintenance status — CAMB, CLASS, EFTCAMB, hi_class, MGCAMB, cosmoprimo, pyccl, astropy.cosmology, Cobaya, MontePython, CosmoSIS, desilike, emcee, dynesty, PolyChord, nautilus, NumPyro, BlackJAX, velocileptors, CLASS-PT, PyBird, FOLPS, FAST-PT, pypower, pycorr, nbodykit, TreeCorr, NaMaster, Corrfunc, picca, Vega, LaCE, healpy, flip, BORG, pmwd, DISCO-DJ, CosmoPower.
---

# Cosmology software ecosystem — expert reference

Snapshot 2026-10-11. Numbers carry provenance flags ([src] / [sec] / [der]);
re-verify against the cited paper before a number enters a manuscript.
Defaults were read in named versions (camb 2.0.4, pyccl 3.3.6, cosmoprimo 1.0.0,
CLASS 3.2.3, healpy 1.19.0); re-read them for the version in use.

## File map

| Question | Load |
|---|---|
| What a code computes, its paper, repository, licence, release, users | `references/surveys-and-data.md` |
| How the members of a code family differ in method | `references/physics-and-methods.md` |
| Agreement between codes, stated accuracies, timings | `references/results.md` |
| Units, conventions and defaults that trap users; referee checklist | `references/systematics.md` |
| Maintenance status, superseded codes, debates, misconceptions | `references/open-questions.md` |

## What an expert holds in mind

- CAMB and CLASS agree at 0.01 % only for concordance ΛCDM, a shared recombination history and boosted precision (arXiv:1104.2934).
- CAMB v2 (arXiv:2607.14854) changed the defaults: unboosted runs now target 10⁻³; v1.6.6 defaults are off by 1.5 % in TT at ℓ = 3000.
- pyccl 3.3.6 still requests CAMB's v1 accuracy behaviour, so pyccl and a direct CAMB v2 call differ.
- Units split in two camps: classy and pyccl use Mpc⁻¹ and Mpc³; cosmoprimo, flip and picca use h-units; CAMB mixes both in one object.
- Default neutrinos differ: CAMB one massive eigenstate of 0.06 eV; pyccl massless, split "normal" when set; cosmoprimo and CLASS none. N_eff is 3.044 (arXiv:2012.02726) except in stored cosmologies such as astropy `Planck18` (3.046).
- "fσ8" has three code definitions (CAMB velocity–density, CLASS dσ8/dln a, scale-independent f).
- "Halofit" is eleven options in CAMB; the default is HMcode-2020 (arXiv:2009.01858), in pyccl Takahashi (arXiv:1208.2701).
- H-EFTCAMB is the official successor of EFTCAMB (arXiv:2603.01662); modified-gravity solvers agree at sub-per-cent level (arXiv:1709.09135).
- velocileptors, PyBird and FOLPSν agree to k_max ≃ 0.25 h Mpc⁻¹ at 8 (h⁻¹ Gpc)³ precision once bias freedom is matched (arXiv:2404.07272).
- MultiNest gave narrower intervals and inconsistent evidences on DES Y1; DES Y3 moved to PolyChord (arXiv:2202.08233).
- Cobaya's MCMC is a translation of CosmoMC, whose repository has been quiet since 2022; desilike binds to Cobaya, CosmoSIS and MontePython.
- picca measures, Vega models and fits (arXiv:2007.08995, arXiv:2509.15308).
- flip (arXiv:2501.16852): radians, Mpc h⁻¹, km/s, h Mpc⁻¹; engines classy, cosmoprimo, pyccl; cite also arXiv:2303.01198.
- No code paper was found for cosmoprimo, desilike, pypower or pycorr: cite the repository. They install from GitHub.

## Systematics a referee checks

- Code version and non-default precision settings.
- Units of k and P(k), value of h used.
- Neutrino mass split, N_eff, total-matter or CDM-plus-baryon field.
- Non-linear model by name; fluid or PPF dark energy (arXiv:0808.3125); recombination code.
- Sampler settings and convergence; source of any evidence.
- EFT fits: bias basis, priors, counterterm convention, k_max, infrared resummation.
- Estimators: line of sight, mesh and Nyquist, interlacing, shot noise, `bin_slop`.
- Maps: RING or NESTED, ℓ_max, monopole, polarisation convention.
- Emulators: training code, precision, parameter ranges.

## Errors that recur

- Passing a Mpc-unit P(k) to an h-unit code: a factor h³ in amplitude.
- Quoting CLASS `explanatory.ini` values as compiled defaults.
- `FlatLambdaCDM(H0, Om0)` in astropy: no radiation, no neutrinos.
- Treating astropy `Planck18` (with BAO) and cosmoprimo `DESI()` (plik TTTEEE+lowl+lowE+lensing) as the same cosmology.
- Feeding `anafast` output to `synfast` without `new=True`; passing `fwhm` in arcminutes.
- `pip install pycorr`, `pyrecon` or `lace`: unrelated PyPI packages.
- `import camb` in an environment where EFTCAMB was built.
- Citing a timing or accuracy comparison without noting it comes from one code's author.
- Calling flip and BORG the same kind of "field-level" inference.

## Related skills

- `cosmo-theory-foundations`: the conventions themselves (σ8, h-units, Fourier, bias bases).
- `cosmo-statistics-inference`: convergence, priors, evidence, sampler choice.
- `cosmo-simulations-mocks`: N-body codes, mocks, simulation emulators.
- `cosmo-galaxy-clustering`, `cosmo-lyman-alpha`, `cosmo-weak-lensing`, `cosmo-cmb`: the analyses run with these codes.
- `cosmo-beyond-two-point`, `cosmo-peculiar-velocities`: BORG and flip science.
- `cosmo-dark-energy-modified-gravity`: what the modified-gravity solvers parameterise.
