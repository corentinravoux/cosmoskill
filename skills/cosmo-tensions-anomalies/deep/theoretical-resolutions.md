# Theoretical resolutions — cosmo-tensions-anomalies dossier

Scope: how a proposed resolution of the H0 tension is tested against all
data at once and judged — which data set plays the baseline and which the
local datum, why the ladder enters as a prior on M_B rather than on H0,
which residual-tension and model-preference metrics and thresholds are
used, how the S8, CMB–BAO, BBN and neutrino-mass constraints are brought
in, and how far each data choice moves the verdict.
Snapshot: 2026-10-22.
From: CosmoVerse white paper (arXiv:2504.01669), Sect. 4; Abdalla et al.
2022 (arXiv:2203.06142), Sect. VII. Peers of the Schöneberg et al.
comparisons: Khalife et al. 2023, Di Valentino et al. 2021; critiques by
Knox & Millea, Efstathiou, Benevento et al., Vagnozzi; the 2020 EDE–LSS
exchange.

Already in L2 or in sibling skills, not repeated here: the groups E, M,
R, L, E + L and the no-go arguments in outline
(`physics-and-methods.md#theoretical-resolutions-of-the-h0-tension`); the
equations of Δ_Gauss, Δ_DMAP, Δ_shift (`physics-and-methods.md#definitions`);
the World Cup verdict per group and the EDE limits
(`open-questions.md#the-2026-systematic-comparison`,
`open-questions.md#early-dark-energy-where-the-limits-come-from`,
`open-questions.md#what-a-viable-resolution-must-pass`). Model physics:
`cosmo-early-universe-exotica`; profile likelihoods:
`cosmo-statistics-inference` (`deep/profile-likelihoods.md`); the CMB–DESI
distance: `deep/cmb-bao-mismatch.md`.

Notation. M_B is the standardised SN Ia absolute magnitude; A the
baseline data (CMB + BAO + uncalibrated SNe), B the local datum (H0 or
M_B) [src: arXiv:2607.13283, Sect. III]. χ²_min = −2 ln L_max. AIC =
χ²_min + 2 N_param (Eq. 21), ΔAIC = model − ΛCDM (Eq. 22); ln BF = ln Z_M1
− ln Z_M2, Z the evidence (Eqs. 23–24). Q_MPCL is the parameter-shift
statistic under another name [src: Sect. III.1.3; arXiv:2507.23355, Sect.
II]. f_EDE is the maximal EDE energy fraction; θ_s the acoustic angle;
r_s*, r_d the sound horizon at last scattering and drag; S8 = σ8
(Ω_m/0.3)^0.5. "World Cup" = arXiv:2607.13283; "Olympics" =
arXiv:2107.10291.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Ask two questions, not one
<!-- key: step-1-ask-two-questions-not-one -->

Success has two parts: how far the model reduces the tension, and how
good its combined fit is compared with ΛCDM [src: arXiv:2607.13283, Sect.
III]; the Olympics splits the first into a ladder-free posterior test and
a goodness-of-fit test [src: arXiv:2107.10291, Sect. 2]. Why both: ΛCDM
with Ω_cdm h² fixed to 0.11 centres H0 at 71.84 ± 0.16 (Planck 2018 +
lensing + BAO) and passes a Gaussian test at 1.0σ, with Δχ² ≈ 106 against
ΛCDM [src: same section, criterion 1, fn. 8]. Phenomenological emergent
dark energy (no ΛCDM limit) looks good on tension; its generalisation
GPEDE, which contains ΛCDM, passes no test [src: same section].
Khalife et al. add the second side to the first question: a model that
lowers the tension by widening the H0 posterior "without actually
predicting a larger value" is "not excluded" but does not solve it [src:
arXiv:2312.09814, Sect. 4.3]; the review of Di Valentino et al. makes the
same point [src: arXiv:2103.01183, abstract].

### Step 2. Fix the baseline data A
<!-- key: step-2-fix-the-baseline-data-a -->

World Cup baseline [src: arXiv:2607.13283, Sect. IV.1]:

- CMB: Planck PR4 (NPIPE) with CamSpec v12.7 at ℓ > 30, Commander TT and
  SRoll2 EE at ℓ < 30; ACT DR6 and SPT-3G D1 "lite" likelihoods in
  `candl`; CamSpec cut to ℓ < 1000 in TT, TE and ℓ < 600 in EE "to avoid
  double-counting" with the ground data. Lensing: SPT-3G 2-yr and ACT DR6
  (ACT + Planck variant) [src: arXiv:2607.13283, Sect. IV.1].
- BAO: DESI DR2, all tracers from 0.1 < z < 4.2 [src: arXiv:2607.13283, Sect. IV.1].
- SNe: Pantheon+, uncalibrated, 0.01 < z < 2.3 [src: arXiv:2607.13283, Sect. IV.1].
- Reference model: ΛCDM with free Σm_ν [src: Sect. IV.2].

Excluded on purpose: transverse (angular) BAO from SDSS, because they "may
suffer from radial mode leakage" or bin smearing and do not carry the full
DESI constraining power; the authors note that the stronger performance
of the sign-switching cosmological constant in some papers is enhanced
by those data [src: Sect. IV.2, "Notable differences"]. (Olympics: Planck
2018 + BOSS DR12, MGS, 6dFGS BAO + Pantheon [src: arXiv:2107.10291, Sect.
2]. Khalife et al. 2023: Planck TT, TE, EE + lowE + lensing, SPT-3G 2018,
BAO 6dFGS + DR7 + DR12 + DR16, Pantheon; SH0ES as a Gaussian on H0, 73.29
± 0.9 [src: arXiv:2312.09814, Sects. 2, 4.3].)

### Step 3. Enter the ladder as a prior on M_B
<!-- key: step-3-enter-the-ladder-as-a-prior-on-mb -->

The World Cup uses M_B = −19.253 ± 0.027 from SH0ES; combined with the full
Pantheon+ range it gives H0 = 73.26 ± 0.98, against 73.04 ± 1.04 in the
SH0ES paper, the difference being that SH0ES restricts to z < 0.15 and
fixes q0 = −0.55 [src: arXiv:2607.13283, Sect. IV.1 and fn. 8]. The
Olympics used M_b = −19.2435 ± 0.0373 when supernovae are in the data and
H0 = 73.2 ± 1.3 when they are not [src: arXiv:2107.10291, Sect. 2].

Why M_B and not H0. The ladder "calibrate[s] the intrinsic magnitude of
supernovae at redshifts of 0.02–0.15"; the H0 then has to be derived from
the supernovae within the model's own expansion history [src:
arXiv:2107.10291, Sect. 2]. Camarena & Marra give three reasons: no double
counting of low-redshift SNe, no reliance on cosmography with q0 fixed to
−0.55, and the calibration information on M_B is not thrown away, which
otherwise "bias[es] both model selection and parameter constraints" [src:
arXiv:2101.08641, abstract; the two χ²_tot differ only in the last
term, Eqs. 14–15].

How much it matters, worked case: a "hockey-stick" dark energy with a
phantom transition at 0.01 ≤ z_t ≤ 0.1. With the H0 prior its best fit has
w_x ≈ −14, H0 = 72.5 (0.5σ from SH0ES) and Δχ² = −10.7 against wCDM, but
its M_B is 4.9σ from the local calibration; with the M_B prior the best
fit returns to H0 = 69.3 (3.0σ) and Δχ² = +3.5 [src: arXiv:2101.08641,
Table 3]. For wCDM itself the two priors give nearly the same posterior
[src: Sect. 5]. The Olympics "checked explicitly that using a SH0ES
likelihood on H0 rather than M_b incorrectly yields more favorable results
for these late-time models"; for early-time models the choice is
"effectively irrelevant" [src: arXiv:2107.10291, Sect. 2].

Earlier statements by other groups. Benevento, Hu & Raveri: transitions
at z ≪ 0.1 reach the SH0ES 74.03 ± 1.42 with a CMB + BAO fit as good as
ΛCDM's, but with the SH0ES calibration transferred to Pantheon H0 falls
to 69.17 ± 1.09 [src: arXiv:2002.11707, abstract]. Efstathiou: an H0
prior is "a huge and lossy compression" that discards the SN Hubble-
diagram shape; carry one M_B for Cepheid hosts and one for distant SNe,
a candidate needing overlapping posteriors, valid also for changes at z
≲ 0.05 [src: arXiv:2103.08723, Sect. 3]. Forward side: fitting the
expansion history to Pantheon instead of fixing q0 raises the
three-anchor H0 from 74.1 ± 1.3 to 74.8–75.0 ± 1.3, M_B unchanged near
−19.21 [src: Table 2].

Double-counting caveat. Bansal & Huterer state that applying −19.253 ±
0.027 together with the full Pantheon+ sample "effectively double-counts
the SNe in the range 0.01 < z < 0.15" and gives artificially tight
contours; they use the full Pantheon+SH0ES likelihood instead, and quote
an inflated prior M = −19.243 ± 0.032 from a "de-marginalization" by
Camarena and Marra that reproduces it [src: arXiv:2602.06293, App. A,
Eq. 22, Fig. 5]. The World Cup combines the −19.253 ± 0.027 prior with
Pantheon+ over 0.01 < z < 2.3 [src: arXiv:2607.13283, Sect. IV.1]; Sect.
IV.1 does not say whether the overlap was corrected.

The M_B tension "also incorporates ... the calibration mismatch between
BAO and SNeIa data": ΛCDM 5.6σ in M_B against 4.3σ in H0 (Δ_shift) [src:
arXiv:2607.13283, Tables 3, 4 and caption].

### Step 4. Measure the residual tension (question 1)
<!-- key: step-4-measure-the-residual-tension-question-1 -->

A = CMB + BAO + SN without the local datum; B = the M_B (or H0) prior
[src: arXiv:2607.13283, Sect. III]. Three numbers per model:

- Δ_Gauss on the single parameter, kept "for reference" because it misses
  long tails [src: Sect. III.1.1].
- Δ_DMAP = sqrt(χ²_min,A+B − χ²_min,A − χ²_min,B) (Eq. 17), with
  χ²_min,SH0ES = 0 for a one-parameter prior [src: arXiv:2107.10291, Sect.
  2, criterion 2]. It uses likelihoods only "and not the prior bounds"
  [src: arXiv:2607.13283, Sect. III.1.2]. The σ are the Gaussian
  equivalent of the probability to exceed for χ² with one degree of
  freedom [src: arXiv:2507.23355, Sect. II, fn. 4].
- Δ_shift (Eqs. 18–20) with `tensiometer`; it "naturally penaliz[es] more
  complex models" but carries posterior-volume and projection effects
  [src: arXiv:2607.13283, Sect. III.1.3].

DMAP supersedes the Gaussian tension in the Olympics; they differ by ≲
10% except for EDE and NEDE [src: arXiv:2107.10291, Sect. 2, fn. 9].
Khalife et al. use the exact form, Q_MPCL: q = probability of the
smallest credible interval of P(δ) (difference of the two posteriors)
containing δ = 0, n = √2 erf⁻¹(q) (Eqs. 5–7); for Gaussian posteriors
Q_MPCL = Q_DMAP = Δ_GT. Q_MPCL carries priors and volume effects, Q_DMAP
only best fits, so both are reported [src: arXiv:2312.09814, Sect. 4.3].

### Step 5. Measure the model preference (question 2)
<!-- key: step-5-measure-the-model-preference-question-2 -->

ΔAIC and ln BF on the combined fit A + B, against ΛCDM [src:
arXiv:2607.13283, Sects. III.2.1–III.2.2]. Evidence from `MCEvidence`; quoted
errors 0.00–0.51, but thinning tests suggest "closer to ± 0.5" [src:
Table 6 caption]; BF "depends explicitly on the adopted parameter priors"
[src: Sect. III.2.2].

The Olympics' warnings on AIC: the 2N penalty "can be circumvented by
simply fixing model parameters to their best-fit", and ΔAIC does not say
whether the gain comes from H0 or from fitting other data (Planck) better;
hence it is read with a tension metric [src: arXiv:2107.10291, Sect.
2, criterion 3].

### Step 6. Apply thresholds and select
<!-- key: step-6-apply-thresholds-and-select -->

| Comparison | Tension threshold | Preference threshold | Stated reason |
|---|---|---|---|
| Olympics | Δ_Gauss or Δ_DMAP ≤ 3σ | ΔAIC ≤ −6.91 | 3σ so that models failing it stay excluded if systematics are revised "slightly but not drastically"; −6.91 from exp(−ΔAIC/2) = 10^1.5, "weak preference" on Jeffreys' scale [src: arXiv:2107.10291, Sect. 2] |
| World Cup | cells < 3.5σ highlighted (not a cut) | −ΔAIC > 10 or ln BF > 3, on the fit with the M_B prior | "a significant improvement in the combined fit" [src: arXiv:2607.13283, Sect. III.3; Tables 2–4] |
| Khalife et al. 2023 | Q_MPCL or Q_DMAP ≤ 3σ, either, "agnostic" between them | ΔAIC with and without SH0ES, computed only for Q_MPCL ≤ 4σ | 3σ so that revised systematics could bring a model below 2σ [src: arXiv:2312.09814, Sect. 2] |
| SPT-3G D1 EDE | Q_MPCL ≤ 3σ and Q_DMAP ≤ 3σ | ΔAIC ≤ −6.91, on data without SH0ES | to ask "is there SH0ES-independent evidence for the AEDE model?" [src: arXiv:2507.23355, Sect. II] |

Olympics medals: bronze for passing DMAP or AIC, silver for both, gold
for also passing the Gaussian tension without the ladder prior; a model
whose combined Δχ² is worse than ΛCDM is excluded [src:
arXiv:2107.10291, Sect. 2]. World Cup finalists are tested in their
simplest form (flat, Λ) to limit computing cost, with the curved
varying-m_e model, the Olympics "gold medal winner", added for reference
and WZDR added as a "wild card" for group R [src: arXiv:2607.13283, Sect.
IV.7].

### Step 7. Knockout: bring in the other probes one at a time
<!-- key: step-7-knockout-bring-in-the-other-probes-one -->

World Cup tests on the finalists [src: arXiv:2607.13283, Sect. V.1]:

- Planck to ℓ = 1800/1050/600 (TT/TE/EE), where Planck and ACT have
  "roughly similar constraining power", with CamSpec or plik.
- DES Y5 Dovekie SNe in place of Pantheon+ (no M_B tension computed,
  because the calibration differs [src: Table 10 caption]).
- S8 = 0.789 ± 0.012 from DES Y6 3×2pt as a Gaussian likelihood on the
  ΛCDM-derived S8, "for simplicity" [src: arXiv:2607.13283, Sect. V.6].
- BBN: `PRyMordial` grid in (Ω_b h², ΔN_eff or m_e^early/m_e^late),
  PArthENoPE or PRIMAT rates, against the D/H and Y_p of the Numbers
  table; EMG and thawing gravity excluded (gravity modified at BBN) [src:
  Sects. V.1, V.7].
- Σm_ν ≥ 58 meV, because lower values are in > 2σ tension with
  oscillation data even for normal ordering [src: arXiv:2607.13283, Sect. V.4; Fig. 18
  caption has "60 eV"].
- Baryonic feedback: marginalising over T_AGN of HMcode 2020, since the
  lensed damping tail depends on non-linear lensing [src: Sect. V.5].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Prior on M_B or on H0
<!-- key: prior-on-mb-or-on-h0 -->

M_B is required for late-time models and costs the SN-overlap handling;
H0 is harmless for early-time models and wCDM (Step 3). SPT-3G D1 quotes
its EDE tension in H0 against SH0ES 73.17 ± 0.86 [src: arXiv:2507.23355,
Sects. I, II].

### Frequentist or Bayesian residual tension: the early dark energy dispute
<!-- key: frequentist-or-bayesian-residual-tension-the -->

Both sides, same model class:

- Bayesian, collaboration: f_EDE < 0.070 (95%) and 3.6σ from SPT + ACT +
  Planck; with DESI, Q_MPCL = 2.6σ and Q_DMAP = 2.4σ for CMB-SPA + DESI,
  2.9σ when Pantheon+ is added; Δχ² = −8.5 but ΔAIC = −2.5 without SH0ES,
  "no strong statistical evidence" [src: arXiv:2507.23355, abstract,
  Sect. IV.2]. The authors state the prior-volume problem themselves: as
  f_EDE → 0 a large range of θ_i and z_c reproduces ΛCDM and pulls the
  chain there, and a z_c prior above recombination raises f_EDE without
  raising H0 [src: Sect. II].
- Profile likelihood: f_EDE = 0.09 ± 0.03 and H0 = 71.0 ± 1.1 from
  Planck (ℓ < 1000) + ACT DR6 + lensing + Pantheon+ + DESI DR2, intervals
  by the Neyman construction, Δχ² < 1 (3.84) for 68% (95%); f_EDE > 0 at
  about 2.5σ where the Bayesian analysis gives only an upper limit [src:
  arXiv:2505.08051, Sect. VI and abstract]. The authors call the Bayesian
  penalty "a perfectly valid concern (the region of parameter space that
  can address the tension is small)" but "an important caveat" [src:
  Sect. VI].
- World Cup EDE: Δ_DMAP 2.51σ, Δ_shift 2.6σ (H0), 3.0σ (M_B) [src:
  arXiv:2607.13283, Tables 2–4]; Olympics: tails took EDE and EMG from
  3.1–3.7σ (Gaussian) to 1.6–2.3σ (DMAP) [src: arXiv:2107.10291, Sect. 2].
  Khalife et al. 2023: EDE Q_MPCL 3.7σ, Q_DMAP 2.7σ [src:
  arXiv:2312.09814, Table 1].
- 2020 round, BOSS full shape [src: abstract of each]. Against: EDE at 3σ with
  SH0ES and without most LSS, below 2σ with LSS, weaker with physical
  field priors (Hill et al., arXiv:2003.07355); EFT BOSS gives f_EDE <
  0.072 (95%), H0 = 68.54 (+0.52/−0.95), f_EDE < 0.053 with photometric
  LSS, and "refute[s] claims" that MCMC without SH0ES misleads (Ivanov et
  al., arXiv:2006.11235); EDE and Rock 'n' Roll degeneracies are "well
  broken" by full shape (D'Amico et al., arXiv:2006.12420). For: the limits
  are "a consequence of their choice of priors"; EFT-LSS + CMB + SNe
  allow f_ede = 0.09, H0 = 71 at Δχ² = 0.12 against ΛCDM, the extra power
  tracing to a BOSS–Planck A_s difference already in ΛCDM (Smith et al.,
  arXiv:2009.10740).

### Model preference with or without the local datum
<!-- key: model-preference-with-or-without-the-local-datum -->

With M_B: EDE −ΔAIC = 23.4, ln BF = 10.51 [src: arXiv:2607.13283,
Tables 5, 6]. Without SH0ES: EDE Δχ² = −7.0 against −35.4 with SH0ES, on
P-ACT + lensing + BAO + SN [src: arXiv:2505.08051, Sect. V]; ΔAIC = −2.5
for CMB-SPA + DESI [src: arXiv:2507.23355, Sect. IV.2]. The first asks
whether the model fits all data including the ladder, the second whether
data other than the ladder ask for it; quote which. Khalife et al.: ΔAIC
without SH0ES positive for all eleven models (EDE Δχ² = −4.6, ΔAIC =
+1.4); with SH0ES ≈ 6² − n² for a tension cut from 6σ to nσ, so "nothing
in the data" is fit better than in ΛCDM "except the SH0ES likelihood
itself" [src: arXiv:2312.09814, Sect. 2, Table 1].

### Which CMB data
<!-- key: which-cmb-data -->

- Removing ACT (primary and lensing): group R falls from about 5σ to
  3–3.5σ, varying m_e from about 4σ to 3.6σ; groups L, E + L stay near
  5.5σ. The authors attribute it to ACT's "slight preference for higher
  power at high ℓ": extra radiation lowers the damping tail, EDE raises it,
  varying m_e "sits in between" [src: arXiv:2607.13283, Sect. IV.5].
- Extended CamSpec: ± 0.4σ at most; extended plik: about −0.5σ almost
  everywhere, −1.1σ for curved varying m_e [src: arXiv:2607.13283, Sect. V.2].
- ACT DR6 across all its extended models: 66.1 < H0 < 71.0 (68%), lower
  end from neutrino self-interactions, upper end from EDE [src:
  arXiv:2503.14454, Sect. VIII.2].
- Primordial running α_s, β_s (Eq. 25 of arXiv:2607.13283): ΛCDM + α_s +
  β_s gives α_s = 0.0122 ± 0.0057; group R reaches 3.5σ only with α_s and
  β_s far from zero [src: Sect. IV.6, Table 9].

### Which BAO
<!-- key: which-bao -->

Replacing DESI by BOSS lowers H0 by 1–1.5 km/s/Mpc in many ACT extended
models [src: arXiv:2503.14454, Sect. VIII.2]. BAO "have the strongest
impact on constraints for all model classes": they fix Ω_m = 0.2995 ±
0.0035 in ΛCDM "and nearly the same for all other models" [src:
arXiv:2607.13283, Sect. IV.2]. Without BAO, groups R, M and E allow
broader, higher Ω_m and looser neutrino-mass bounds [src: same section].

### Which supernovae
<!-- key: which-supernovae -->

DES Y5 gave Ω_m = 0.352 ± 0.017, Pantheon+ 0.334 ± 0.018, DES Dovekie
0.330 ± 0.015 in ΛCDM; group M models raise H0 by lowering Ω_m and are the
ones SNe constrain. Swapping in Dovekie moves varying m_e from 69.10
(+0.71/−0.68) to 68.97 ± 0.65, 0.2σ more tension [src: arXiv:2607.13283,
Sect. V.3].

### Extended base model
<!-- key: extended-base-model -->

With w0wa, EDE Δ_DMAP goes 2.51σ → 3.24σ; with Ω_k, varying m_e goes
4.25σ → 3.54σ [src: arXiv:2607.13283, Table 2].

## How the other tensions enter the judgement
<!-- key: how-the-other-tensions-enter-the-judgement -->

### CMB–BAO mismatch
<!-- key: cmb-bao-mismatch -->

Before combining CMB with DESI in EDE, SPT-3G D1 checks their consistency
in the Ω_m–h r_d plane with a 3σ threshold: 1.5σ, 2.8σ, 2.5σ for SPT-3G
D1, SPT + ACT, CMB-SPA in EDE against 2.3σ, 3.7σ, 2.8σ in ΛCDM. With DESI
the EDE fraction departs from zero at 1.6σ, 2.8σ, 1.2σ, which the authors
call "another manifestation of the discrepancy that currently exists
between CMB and DESI BAO data in ΛCDM"; f_EDE of roughly 4–10% makes the
CMB and DESI regions overlap in [Ω_m, Ω_m(h r_d/147.1 Mpc)²] [src:
arXiv:2507.23355, Sect. IV.2, Fig. 2]. The profile-likelihood side reads
the same fact as support: the EDE cosmology that fits SH0ES predicts a
larger H0 r_s and a slightly smaller Ω_m "in good agreement with DESI",
because ω_c rises to keep the CMB fit [src: arXiv:2505.08051, Sect. V].
The World Cup states the general version: models easing H0 have a
negative H0–Ω_m correlation, so DESI's low Ω_m helps them [src:
arXiv:2607.13283, Sect. IV.2].

Cost on the supernova side: in EDE Ω_m = 0.2949 ± 0.0034, 2.1σ from
Pantheon+ and 3.1σ from DES Y5, so "EDE cannot fully remove the
preference for dynamical dark energy" in CMB + BAO + SN [src:
arXiv:2505.08051, Sect. V]. Against this, with EDE included a
quintessence-like w0 + wa ≥ −1 is consistent at 1σ with Planck + ACT +
SPT + DESI + Pantheon+ + SH0ES, Δχ² ≲ −14 against w0waCDM without EDE
[src: arXiv:2511.16606, abstract].

### S8
<!-- key: s8 -->

The EDE-specific form: the EDE fit to CMB + SH0ES has 10% more matter
power at k = 1 h/Mpc and a higher σ8, which LSS data penalise [src:
arXiv:2003.07355, abstract].

The structural argument [src: arXiv:2010.04158, main text, Eqs. 1–2,
Figs. 1–2]: θ* = r*/D(z*) and θ⊥^BAO = r_d/D(z_obs) define lines in the
r_d–H0 plane with different slopes because z* ≫ z_obs; with r_d =
1.0184 r* fixed, CMB, BAO and SH0ES meet only at Ω_m h² ≈ 0.167 (Planck
ΛCDM: 0.143 ± 0.001); at that matter density S8 is pushed up against DES
and KiDS. Low-Ω_m h² solutions fail BAO; high-Ω_m h² solutions fail weak
lensing. Changes in n_s are "small" in the models surveyed. The argument
assumes no new physics after recombination.

Measured in the World Cup [src: arXiv:2607.13283, Sect. V.6]: with the
DES Y6 S8 prior the M_B tension of group E rises by up to 0.7σ (0.3σ in
H0); WZDR is unchanged; varying m_e improves by 0.3σ and its curved
version by 1.4σ, to 2.7σ, because group M lowers Ω_m and so S8 at fixed
σ8. The authors expect KiDS-Legacy (S8 = 0.815 +0.016/−0.021) instead
"would lead to constraints closer to the baseline" [src: fn. 11]. In
ACT DR6 no extended model moves the CMB S8 down toward cosmic shear, and
the comparison is to be taken "with a grain of salt" because a late-time
S8 inferred under ΛCDM changes in the new model [src: arXiv:2503.14454,
Sect. VIII.2]. Running leaves S8 at 0.826 against 0.829 (average error
0.007) [src: arXiv:2607.13283, Sect. IV.6].

### Primordial spectrum and BBN
<!-- key: primordial-spectrum-and-bbn -->

EDE solutions reaching H0 ∼ 73 shift n_s toward unity, |n_s − 1| ≃
O(0.001), with ACT DR6 and SPT-3G D1 [src: arXiv:2509.11902, abstract].

With PArthENoPE rates the M_B tension rises by 0.5σ "uniformly"; with
PRIMAT, deuterium pushes Ω_b h² lower (about 2σ from Planck ΛCDM) and
group E, whose degeneracies favour higher Ω_b h², rises further: +0.7σ
for NEDE, others about +0.4σ [src: arXiv:2607.13283, Sect. V.7].

### Neutrino mass
<!-- key: neutrino-mass -->

In varying m_e, H0, Σm_ν and m_e^early/m_e^late rise together without
changing the CMB spectra at first order; Σm_ν < 123 meV with BAO, < 291
meV without [src: arXiv:2607.13283, Sect. IV.2]. With Σm_ν ≥ 58 meV the
curved varying-m_e model drops by 1.4σ to 2.9σ; others move ≤ 0.2σ [src:
Sect. V.4].

### Late-time models: the two walls in numbers
<!-- key: late-time-models-the-two-walls-in-numbers -->

Earlier form: BOSS BAO + uncalibrated Pantheon, five-node spline H(z),
zero curvature, give β_BAO ≡ c/(r_s^drag H0) = 29.54 ± 0.406, tying H0 to
r_s without ΛCDM [src: arXiv:1908.03663, Sect. III]; Knox & Millea call
a faster expansion in the decade of scale factor before recombination
"the least unlikely" [src: abstract]. Late escapes: H(z) wiggles cost
many new degrees of freedom and sit at the three BOSS redshifts, which
"might invalidate" the BAO compression; distance-duality violation would
need supernova "axion brightening" [src: Sects. IV.1.1–IV.1.2]. A
dynamics-free inverse ladder gives the same verdict [src:
arXiv:2103.08723, abstract]. Other side: from seven hints (old-object
ages, r_s–H0 degeneracy directions, chronometers, low-z "descending
trends", early ISW, uncalibrated Ω_m, equality-scale H0) early-time
physics "alone will always fall short"; early plus late non-local plus
local new physics is needed [src: Vagnozzi, arXiv:2308.16628, abstract].

Normalisation wall: BAO measure r_d H0 (Eqs. 2–4 of arXiv:2607.21244);
late-time models cannot change r_d. Shape wall [src: arXiv:2607.21244,
Sect. II]: θ_s = r_s* H0 / I with I = ∫₀^{z*} dz/E(z) (Eqs. 5–6), so at
fixed θ_s and r_s*, δH0/H0 ≃ δI/I (Eq. 8). Split I = I_< + I_> at z_max ≈
2.3 (Eq. 9) with weights f_< ≃ 0.41, f_> ≃ 0.59 in Planck ΛCDM (Eqs.
10–11). Required: δH0/H0 ≃ 0.093 for H0DN 73.50 ± 0.81 against CMB
67.24 ± 0.35. Measured, Gaussian-process reconstruction of E(z) from
unanchored SNe ± BAO, integrating each realisation separately:
(δH0/H0)_< < 0.8% (Union3 + DESI) to 0.38% (DES Y5 Dovekie + DESI) at 95%
(Eq. 18); total δH0/H0 < 2.07% (conservative, ΛCDM-guided I_>) or <
3.67% (permissive, wCDM-guided), the latter leaving ≈ 4.3σ [src: Sect.
V, Table 2]. The pointwise ≈ 5% freedom in E(z) does not translate into
5% in H0 because pointwise quantiles do not belong to one realisation
[src: Sect. V].

Calibration route [src: arXiv:2602.06293, Sect. IV, Table 3]: on DESI
DR2 + CMB + Pantheon+SH0ES, a step in H at low z gains Δχ² ≈ −2 (z_t =
0.013), w0wa Δχ² = −5, Ω_K −10; a step in M_B at z_t ≈ 0.013 gains
Δχ² ≈ −40 but "effectively simply removes the SH0ES measurements"; a
non-minimally coupled scalar with a smoothly varying M_B gains −27
[src: Sects. V–VI]; the table of App. A lists H0 = 71.78 for it [src:
App. A]. Broken distance duality is "a radical ... departure".

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| M_B prior | −19.253 ± 0.027 | World Cup | arXiv:2607.13283 | Sect. IV.1 |
| H0 from that prior + full Pantheon+ | 73.26 ± 0.98 | World Cup | arXiv:2607.13283 | Sect. IV.1 |
| De-marginalised M prior | −19.243 ± 0.032 | Bansal & Huterer, attributed to Camarena & Marra | arXiv:2602.06293 | App. A, Eq. 22 |
| ΛCDM Δ_DMAP, baseline | 5.41σ | World Cup | arXiv:2607.13283 | Table 2 |
| ΛCDM Δ_shift in H0 / M_B | 4.3σ / 5.6σ | World Cup | arXiv:2607.13283 | Tables 3, 4 |
| NEDE: Δ_shift H0 / M_B | 2.2σ / 2.7σ | World Cup | arXiv:2607.13283 | Tables 3, 4 |
| 4-parameter recombination: Δχ², ln BF | −17.78, −0.17 | World Cup | arXiv:2607.13283 | Tables 5, 6 |
| ln BF error, realistic | ± 0.5 | World Cup | arXiv:2607.13283 | Table 6 caption |
| Ω_m from BAO, ΛCDM | 0.2995 ± 0.0035 | World Cup | arXiv:2607.13283 | Sect. IV.2 |
| S8 prior in knockout | 0.789 ± 0.012 (DES Y6) | World Cup | arXiv:2607.13283 | Sect. V.1 |
| BBN data | D/H = (2.527 ± 0.030) × 10⁻⁵; Y_p = 0.2458 ± 0.0013 | World Cup | arXiv:2607.13283 | Sect. V.1 |
| Shift from S8 prior | group E up to +0.7σ (M_B); curved m_e −1.4σ | World Cup | arXiv:2607.13283 | Sect. V.6 |
| Shift from BBN | +0.5σ (PArthENoPE); +0.4 to +0.7σ (PRIMAT) | World Cup | arXiv:2607.13283 | Sect. V.7 |
| Shift without ACT | group R 5σ → 3–3.5σ | World Cup | arXiv:2607.13283 | Sect. IV.5 |
| Σm_ν, varying m_e | < 123 meV (with BAO), < 291 meV (without) | World Cup | arXiv:2607.13283 | Sect. IV.2 |
| H0 range across ACT extended models | 66.1–71.0 (68%) | ACT DR6 | arXiv:2503.14454 | Sect. VIII.2 |
| EDE profile intervals | f_EDE = 0.09 ± 0.03; H0 = 71.0 ± 1.1 | Poulin et al. | arXiv:2505.08051 | Sect. VI |
| EDE Δχ² without / with SH0ES | −7.0 / −35.4; Q_DMAP 2.0σ | Poulin et al. | arXiv:2505.08051 | Sect. V |
| EDE, CMB-SPA + DESI | Q_MPCL 2.6σ (2.9σ + Pantheon+), Q_DMAP 2.4σ, ΔAIC −2.5 | SPT-3G | arXiv:2507.23355 | Sect. IV.2 |
| Hockey-stick, H0 vs M_B prior | Δχ² −10.7 vs +3.5 | Camarena & Marra | arXiv:2101.08641 | Table 3 |
| Required δH0/H0 | ≃ 0.093 | Sabogal et al. | arXiv:2607.21244 | Sect. II |
| Allowed δH0/H0 (95%) | < 2.07% conservative; < 3.67% permissive | Sabogal et al. | arXiv:2607.21244 | Table 2 |
| M_B step at z ≈ 0.013 | Δχ² ≈ −40 | Bansal & Huterer | arXiv:2602.06293 | Sect. IV |
| ΛCDM tension, Planck + SPT-3G 2018 + BAO + SN vs SH0ES | Q_MPCL 6.0σ, Q_DMAP 5.8σ | Khalife et al. | arXiv:2312.09814 | Table 1 |
| m_e + Ω_K (+ Σm_ν) | Q_MPCL 2.9σ (1.5σ), Q_DMAP 3.1σ (3.0σ); H0 = 68.20 (69.75 +1.85/−2.93) | Khalife et al. | arXiv:2312.09814 | Table 1 |
| EDE, without / with SH0ES | ΔAIC +1.4 / −25.1 | Khalife et al. | arXiv:2312.09814 | Table 1 |
| m_e Q_MPCL, same SH0ES likelihood as the Olympics | 2.9 → 3.2σ on adding SPT-3G 2018 and eBOSS DR16 | Khalife et al. | arXiv:2312.09814 | Sect. 2, fn. 7 |
| Late DE transition: H0 prior vs calibration transferred to SNe | 74.03 ± 1.42 reached vs 69.17 ± 1.09 | Benevento et al. | arXiv:2002.11707 | abstract |
| β_BAO = c/(r_s^drag H0), BOSS + Pantheon, spline H(z) | 29.54 ± 0.406 | Knox & Millea | arXiv:1908.03663 | Sect. III |
| EDE with EFT BOSS (no SH0ES) | f_EDE < 0.072 (95%); H0 = 68.54 (+0.52/−0.95) | Ivanov et al. | arXiv:2006.11235 | abstract |
| EDE, EFT-LSS + CMB + SNe, other priors | f_ede = 0.09, H0 = 71, Δχ² = 0.12 vs ΛCDM | Smith et al. | arXiv:2009.10740 | abstract |

## What goes wrong
<!-- key: what-goes-wrong -->

- A late-time model tested with an H0 prior: H0 looks resolved while the
  best-fit M_B sits 4.9σ from the Cepheid value (arXiv:2101.08641, Table
  3). Test: refit with the M_B prior or the calibrated SN likelihood and
  plot M_B,i = m_B,i − μ(z_i).
- M_B prior on top of the full SN sample double-counts 0.01 < z < 0.15
  (arXiv:2602.06293, App. A). Test: compare with the full Pantheon+SH0ES
  likelihood.
- Tension metric alone: a model without a ΛCDM limit or with a parameter
  fixed by hand passes it with a bad fit; AIC alone can be gamed by fixing
  parameters (arXiv:2107.10291, Sect. 2). Test: report Δχ² ≤ 0, N_param,
  and both a tension and a preference metric.
- Bayesian limit or Δ_shift alone for a model whose ΛCDM limit fills a
  large prior volume (EDE). Test: Δ_DMAP or a profile likelihood beside it
  (arXiv:2505.08051, Sect. VI; arXiv:2507.23355, Sect. II).
- ln BF differences below about 0.5 read as meaningful (arXiv:2607.13283,
  Table 6 caption).
- A preference that comes from the CMB–DESI mismatch read as support for
  the H0 mechanism. Test: CMB–BAO consistency in the model before
  combining (arXiv:2507.23355, Sect. IV.2); rerun with BOSS BAO
  (arXiv:2503.14454, Sect. VIII.2).
- A model's CMB S8 compared with a lensing S8 derived under ΛCDM. Test:
  derive the late-time S8 in the model or state the approximation
  (arXiv:2503.14454, Sect. VIII.2; arXiv:2607.13283, Sect. V.6).
- Planck-only verdicts on radiation models: ACT moves group R by about
  2σ (arXiv:2607.13283, Sect. IV.5). Test: with and without ACT, and with
  extended Planck multipoles.
- Transverse SDSS BAO used for late-time models (arXiv:2607.13283, Sect.
  IV.2); pointwise E(z) bands read as H0 freedom (arXiv:2607.21244, V).
- BBN left out for groups E, M, R: it costs 0.4–0.7σ, with a rate-code
  dependence (arXiv:2607.13283, Sect. V.7).

## Reading list
<!-- key: reading-list -->

- Method, current: Schöneberg et al. 2026, arXiv:2607.13283 — Sects. III,
  IV.1, V; Tables 2–6.
- Method, first version: Schöneberg et al. 2021, arXiv:2107.10291 — Sect. 2.
- Foundation of the M_B prior: Camarena & Marra 2021, arXiv:2101.08641 —
  Sect. 5, Table 3.
- Critique of late-time models: Bansal & Huterer 2026, arXiv:2602.06293 —
  Sect. IV, App. A; Sabogal et al. 2026, arXiv:2607.21244 — Sects. II, V.
- Early-time limit with S8: Jedamzik, Pogosian & Zhao 2021,
  arXiv:2010.04158.
- Collaboration tests: ACT DR6, arXiv:2503.14454 — Sect. VIII.2; SPT-3G D1
  EDE, Khalife et al. 2025, arXiv:2507.23355 — Sects. II, IV.2.
- The other side on EDE: Poulin et al. 2025, arXiv:2505.08051 — Sects. V–VI.
- Side effects on n_s and w0wa: Peng et al. 2025, arXiv:2509.11902; Wang
  & Piao 2025, arXiv:2511.16606 (abstracts).
- Other comparisons: Khalife et al. 2023, arXiv:2312.09814 (Sects. 2,
  4.3); review Di Valentino et al. 2021, arXiv:2103.01183.
- Where solutions can live: Knox & Millea 2019, arXiv:1908.03663 (Sects.
  III–IV); Vagnozzi 2023, arXiv:2308.16628 (opinion); calibration tests
  of late models: Benevento et al. 2020, arXiv:2002.11707; Efstathiou
  2021, arXiv:2103.08723 (Sect. 3).
- EDE and LSS, both sides: Hill et al. 2020, arXiv:2003.07355; Ivanov et
  al. 2020, arXiv:2006.11235; D'Amico et al. 2020, arXiv:2006.12420;
  Smith et al. 2020, arXiv:2009.10740 (abstracts).

## Not verified
<!-- key: not-verified -->

- Bodies of arXiv:2509.11902 and arXiv:2511.16606 (abstracts only).
- The Camarena–Marra paper behind M = −19.243 ± 0.032 (ref. [85] of
  arXiv:2602.06293): not identified or read. [src: App. A]
- Whether the World Cup corrects the SH0ES–Pantheon+ overlap at 0.01 < z
  < 0.15: not stated in Sect. IV.1 of arXiv:2607.13283; other sections not searched.
- Olympics Table 1 (rendered as a CSV include) and its Tests C and D;
  World Cup Table 10 and Appendix C (text summaries only).
- Efstathiou 2026 (arXiv:2607.29562): not reread. Efstathiou 2021 read
  at Sect. 3 only.
- Khalife et al. 2023 Sects. 5.3–5.6 (per-model detail, S8 update) not
  read; the four EDE–LSS papers of 2020 read at abstract level only.
- No paper read here compares S8-oriented models (decaying dark matter,
  interacting dark energy) across all data; the Olympics notes only that
  the dark radiation–dark matter models lower S8 (arXiv:2107.10291, Sect. 2).
- CosmoVerse Sect. 4 and Abdalla et al. Sect. VII (`from`): not reread.
