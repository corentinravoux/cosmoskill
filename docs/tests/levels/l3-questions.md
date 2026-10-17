# Level test — L3 pilot questions

Twenty-four specialist questions, twelve per pilot skill, for roadmap work
package 4.4. Written on 2026-10-16 from each skill's `references/subtopics.tsv`
and from the roadmap's description of L3 ("how a result is derived and how to
choose between methods"), **before any file under `deep/` was opened and
before the two `SKILL.md` files were read**. Only the subtopic keys and titles
of the two `subtopics.tsv` files, and the list of dossier file names, were
known when they were written.

Each question is one a practitioner preparing or refereeing an analysis would
ask; none is answered by a single headline number. Per skill, questions 1–8
fall on the three dossier subtopics; questions 9–12 fall on other subtopics
and are controls, where L3 should not help.

## cosmo-galaxy-clustering

Dossier subtopics: `bao-reconstruction-fitting` (G1–G3), `full-shape-modelling`
(G4–G6), `estimators-window` (G7–G8).

- **G1** (referee, BAO) The paper reconstructs with one displacement convention
  and fits the post-reconstruction multipoles. What is the difference between
  the RecIso and RecSym conventions, which one did DESI adopt, and what does
  the choice change in the post-reconstruction quadrupole and in the damping
  parameters of the fit template?
- **G2** (analyst, BAO) How is the BAO fit template built — wiggle/no-wiggle
  split, anisotropic damping Σ_∥ and Σ_⊥ (and Σ_s), broadband terms — and how
  did DESI choose between a polynomial broadband and a spline-based one, and
  which priors does it put on the damping parameters?
- **G3** (referee, BAO) How is the BAO systematic error budget built — theory
  and modelling, choice of fiducial cosmology, galaxy–halo connection — what
  method sets each term, and how large is each relative to the statistical
  error?
- **G4** (analyst, full shape) Full modelling against ShapeFit compression:
  which parameters does each sample, what information does compression lose,
  under which conditions do the two agree, and which did DESI DR1 adopt as
  baseline and why?
- **G5** (analyst, full shape) How is k_max chosen for a one-loop EFT fit, and
  how is the choice validated on simulations — on which mocks and with which
  criterion on the parameter bias?
- **G6** (referee, full shape) How are the counterterms and stochastic terms
  parametrised and what priors are put on them; how does the choice of bias
  basis and of priors (physical versus Eulerian, analytic marginalisation)
  produce projection effects, and how did DESI handle them?
- **G7** (analyst, estimators) How is the survey window applied to the theory
  for a FKP/Yamamoto power-spectrum estimator — how is the window matrix
  computed, and how are the wide-angle terms included?
- **G8** (referee, estimators) What are the global and radial integral
  constraints, when does each matter (for instance shuffled versus sampled
  random redshifts), how are they corrected, and what sets the size and
  number of random catalogues for the Landy–Szalay estimator?
- **G9** (control, `rsd-growth`) How is fσ8 extracted from the redshift-space
  multipoles in a template fit, how is the f–b degeneracy broken, and what does
  the Alcock–Paczynski effect add?
- **G10** (control, `fibre-assignment`) PIP weights, individual inverse
  probability weights or nearest-neighbour upweighting: how does one choose,
  and what is the θ-cut used for in DESI DR1?
- **G11** (control, `primordial-non-gaussianity`) How is f_NL obtained from
  scale-dependent bias, how is the response b_φ (the parameter p) chosen, and
  how are imaging systematics on large scales handled?
- **G12** (control, `imaging-systematics`) Linear regression against
  neural-network target-density weights: how does one choose, and how is
  over-correction of large-scale power tested?

## cosmo-statistics-inference

Dossier subtopics: `covariance-estimation` (S1–S3), `profile-likelihoods`
(S4–S6), `tension-metrics` (S7–S8).

- **S1** (analyst, covariance) Hartlap de-biasing of the inverse covariance or
  the Sellentin–Heavens t-distribution likelihood: what does each correct,
  when should one be used rather than the other, and how do the resulting
  posteriors differ?
- **S2** (analyst, covariance) How is the inflation of parameter errors due
  to covariance noise derived (Dodelson–Schneider, Percival et al.), and how
  does one choose the number of mocks for a target precision on the error
  bars?
- **S3** (referee, covariance) Mock-based, analytic or semi-analytic, or
  internal (jackknife) covariance: how does one choose, and how is an analytic
  covariance validated against mocks — which tests, which pass criterion?
- **S4** (analyst, profile likelihood) How is a profile likelihood built in
  practice for a cosmological model with many nuisance parameters (optimiser,
  restarts, profiling over nuisances), and how is the interval read from it?
- **S5** (referee, profile likelihood) Near a physical boundary (Σm_ν ≥ 0,
  f_EDE ≥ 0), how should the interval be built — Feldman–Cousins, a boundary
  correction, or the naive Δχ² = 1 rule — and when do they differ?
- **S6** (referee, profile likelihood) When do the profile likelihood and the
  marginal posterior disagree, and how does one decide which summary to
  report; what did the early-dark-energy case show?
- **S7** (analyst, tension metrics) Which tension metric to use — parameter
  difference, suspiciousness, Bayes ratio R, goodness-of-fit degradation,
  eigentension — how is each computed, and which depend on the prior?
- **S8** (referee, tension metrics) How is a tension metric converted to an
  "n σ" statement, and how does one handle non-Gaussian posteriors (for
  instance a parameter-difference distribution estimated from samples)?
- **S9** (control, `samplers-convergence`) Metropolis–Hastings, nested
  sampling or NUTS for a 30–50-parameter cosmology fit: how does one choose,
  and which convergence criterion is adequate?
- **S10** (control, `model-comparison`) Bayes factor, Δχ² or an information
  criterion for a w0wa preference: how does one choose, and how are the
  Jeffreys-scale and "σ-equivalent" statements derived?
- **S11** (control, `priors-projection-effects`) How does one test an
  analysis for projection effects (MAP against posterior mean, prior-only
  chains, profiles), and how should constraints be reported?
- **S12** (control, `simulation-based-inference`) How is a neural posterior
  estimator validated (coverage, SBC, TARP) before its result is used for
  cosmology?
