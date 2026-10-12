# Open questions — dark energy and modified gravity

Scope: live controversies about the dynamical-dark-energy signal and about
tests of gravity, with both sides cited; what the next data decide; stale
claims.

Snapshot: 2026-10-07

Flags: `[src]` read this session in the cited paper; `[sec]` from a named
secondary source; `[der]` derived here.

## 1. Is the `w0`–`wa` preference real? The critiques, one by one
<!-- key: is-the-w0-wa-preference-real-the-critiques-one -->

The collaboration numbers are in `results.md` Sections 1–3. Each subsection
below gives the objection, the reply, and the status at the snapshot.

### 1.1 Supernova-sample dependence
<!-- key: supernova-sample-dependence -->

- **Objection.** Efstathiou 2024, arXiv:2408.07175: the DR1 evidence ran from
  ~3.9σ with DES5Y to ~2.5σ with Pantheon+; supernovae common to DES5Y and
  Pantheon+ show an offset of ~0.04 mag between low and high redshift; a
  systematic of that size brings DES5Y into agreement with Planck ΛCDM [src].
- **Reply.** Vincenzi et al. 2025, arXiv:2501.06664: the offset is reproduced;
  43% of it comes from DES-SN5YR improvements in intrinsic-scatter and host
  modelling, 38% from comparing objects that carry different selection
  functions and therefore different bias corrections (20% of the supernovae
  are in common). With the Pantheon+ scatter model and host properties the
  DES-SN5YR evidence falls only from 3.9σ to 3.3σ [src].
- **What happened next.** Two real errors were then found on the supernova
  side: the Dovekie recalibration of DES (Popovic et al. 2025,
  arXiv:2511.07517) and inconsistent host masses between low and high redshift
  in Union3 and Pantheon+ (Hoyt et al. 2026, arXiv:2601.19424). The three
  samples moved towards each other, to 3.2–3.4σ (`results.md` Section 2). The
  dependence on the supernova sample, which was the strongest argument against
  the signal in 2024, is largely gone; the absolute significance settled near
  3σ, not 4σ.
- **Status.** Resolved as a discrepancy between samples; open as a common-mode
  question, because all samples share most of their low-redshift supernovae
  (`cosmo-supernovae`).

### 1.2 The low-redshift anchor
<!-- key: the-low-redshift-anchor -->

- Huang, Cai and Wang 2025, arXiv:2502.04212: within DESY5, the intercept of
  the magnitude–distance relation differs between the external low-redshift
  sample and the DES sample; correcting for it reduces the preference "to be
  less than 2σ", with or without the CMB [src].
- Notari, Redi and Tesi 2024, arXiv:2411.11685: a ~3σ preference exists
  without DESI, using DES BAO + DES5Y + Planck; the preference is driven by
  low-redshift supernovae common to DES5Y and Pantheon+; removing the common
  objects from one or the other catalogue gives 3.8σ or 2.5σ; marginalising
  over a `z < 0.1` versus `z > 0.1` magnitude offset in DES5Y weakens the
  evidence significantly [src].
- Dhawan, Popovic and Goobar 2024, arXiv:2409.18668: the dominant supernova
  systematics (calibration, progenitor and dust evolution, Milky Way
  extinction law) all shift an underlying ΛCDM towards the DESI 2024 region of
  the `w0`–`wa` plane; small calibration or dust changes produce shifts
  comparable to the reported deviation [src]. This is the reason a common-mode
  supernova systematic cannot be dismissed by the agreement of three
  compilations.
- The collaboration test: removing `z < 0.1` supernovae from DESY5 enlarges
  the errors much more than it moves the best fit (arXiv:2503.14738, figure on
  data-selection robustness) [src]. For Unite, the sibling `cosmo-supernovae`
  reports that the same cut moves the result by about 2σ (arXiv:2609.05053)
  [sec].
- **Status.** Open. No dark-energy analysis at the snapshot uses a modern,
  homogeneous low-redshift anchor; see `cosmo-supernovae` for DEBASS and ZTF.

### 1.3 Does the signal survive without supernovae?
<!-- key: does-the-signal-survive-without-supernovae -->

- DESI DR2 + CMB alone: 3.1σ; with only compressed early-universe CMB priors:
  2.4σ; DESI alone: 1.7σ (arXiv:2503.14738) [src].
- DES Y6 all probes + DESI DR2 BAO + CMB without supernovae: 2.6σ
  (arXiv:2605.27221) [src].
- Without the CMB: DESI DR2 + DES Y6 (low redshift only) 2.3σ
  (arXiv:2605.27221); DESI DR1 full shape + DR2 BAO 1.4σ (arXiv:2602.18761);
  with the bispectrum, within 1σ (arXiv:2606.23936) [src].
- **Reading.** No single data set shows the signal above about 2σ. The
  preference above 3σ is a property of combinations and can equally be
  described as a ΛCDM inconsistency between data sets: a mismatch in the
  matter density (`Omega_m` 0.297 from DESI against 0.317 from Planck,
  arXiv:2503.14738 [src]).
- Zaldarriaga 2026, arXiv:2606.30527: an SVD of the low-redshift distance data
  finds that the leading measurable direction is essentially `Omega_m h^2`,
  that most of the tension with the CMB resides there, and that the second
  direction, which opens in `w0wa` and is an independent test of dynamical
  dark energy, shows no significant tension [src].

### 1.4 The CMB side: lensing, optical depth, and "negative neutrino mass"
<!-- key: the-cmb-side-lensing-optical-depth-and-negative -->

The same data mismatch appears in three guises depending on the extension
fitted.

- Elbers et al. 2024, arXiv:2407.10965: with an effective neutrino mass
  allowed to be negative, Planck + ACT + DESI in ΛCDM is in 2.8–3.3σ tension
  with oscillation experiments; in `w0wa` and mirage models the mass returns
  to `0.06 (+0.15/−0.10) eV` and `0.04 (+0.15/−0.11) eV` [src].
- Jhaveri, Karwal and Hu 2025, arXiv:2504.21813: the tension "largely arises
  from the CMB lensing constraints on the calibration of the sound horizon"
  and relies on the large-angle polarisation measurement of τ; dropping these
  constraints gives `tau = 0.091 ± 0.011` in ΛCDM and brings the `w0`–`wa`
  preference below 95% CL [src].
- Sailer et al. 2025, arXiv:2504.16932: DESI versus CMB is 2.2σ in ΛCDM; `tau
  ~ 0.09` reduces the evolving-dark-energy preference from ≃3σ to ≃1.5σ;
  DESI + high-ℓ CMB + lensing gives `tau = 0.090 ± 0.012`, in ≃3–5σ tension
  with Planck low-ℓ polarisation; τ from Planck is a "single-point failure"
  for analyses that include the CMB [src].
- Counter-evidence for a high τ lives in `cosmo-cmb` and
  `cosmo-reionization-21cm` (the siblings report that reionisation data side
  with the low value).
- The CMB data set matters. The sibling `cosmo-cmb` reports the ΛCDM distance
  between CMB and DESI DR2 as 1.6σ (P-ACT), 2.8σ (CMB-SPA) or 3.7σ (SPT+ACT)
  [sec]; a `w0wa` significance inherits this spread and must name the CMB
  likelihood.
- **Status.** Open. A τ measurement independent of Planck low-ℓ EE would close
  one of the three doors.

### 1.5 Priors and parameterisation
<!-- key: priors-and-parameterisation -->

- Cortês and Liddle 2024, arXiv:2404.08056: with a pivot, the evidence is
  "concentrated in the derivative of w rather than its mean offset from −1";
  the mean equation of state matches ΛCDM in the redshift range probed (the
  "PhantomX coincidence"); conclusions "are strongly driven by the assumed
  parameter priors" [src]. The DR2 pivot values (`w_p = −1.024 ± 0.043` at
  `z_p = 0.53` for DESI + CMB, arXiv:2503.14738) show the same pattern [src].
- Patel, Chakraborty and Amendola 2024, arXiv:2407.06586: the Bayesian
  comparison depends on the prior range, in particular the lower bound of the
  dark-energy parameters (title and abstract snippet only; no number
  extracted) [src].
- Toomey et al. 2025, arXiv:2509.13318: priors on (`w0`, `wa`) learned by a
  normalising flow from two quintessence models reduce the Planck + DESI
  tension with Λ from ~3.1σ to ~1.3σ; "uniform priors ... can actually bias
  inferences toward unphysical parameter regions" [src].
- **Reply.** Herold and Karwal 2025, arXiv:2506.12004: profile-likelihood
  (frequentist) constraints on `w0`, `wa` are "in excellent agreement with the
  Bayesian constraints" for DESI + Planck + lensing + Pantheon+ or DESY5; the
  `Omega_m` profiles show internal inconsistencies under Λ that disappear in
  `w0wa` [src]. The collaboration significances are themselves `Delta chi2` at
  the posterior maximum, not posterior volumes (arXiv:2503.14738) [src].
- **Reading.** For BAO + CMB + SN the prior objection affects Bayesian
  evidences and theory-informed analyses, not the `Delta chi2`. For full-shape
  clustering it is a different and much larger problem (`systematics.md`
Section 5).
- Lodha et al. 2025, arXiv:2503.14743: other parameterisations, binned `w(z)`
  and Gaussian-process reconstructions give consistent trends [src].
- Non-parametric caveat: Kim, Mota and Tamosiunas 2026, arXiv:2607.28918,
  apply an anytime-valid e-process to the DR1→DR2 BAO sequence. For an
  alternative aligned with the DR2-preferred direction the running evidence
  reaches 33.97 (illustrative 5% threshold: 20); removing the LRG2 redshift
  bin reduces it to 0.49; allowing any of the seven bins to carry the excess,
  the signal does not survive a look-elsewhere correction; they call it "a
  fragile, single-bin, specification-dependent signal" [src]. This is a
  BAO-only statement.

### 1.6 Physical versus effective models: phantom crossing
<!-- key: physical-versus-effective-models-phantom -->

- **The claim.** In CPL the best fit crosses `w = −1` near `z ≃ 0.4`
  (arXiv:2503.14738) [src]. Rippentrop, Ishak and Gonzalez 2026,
  arXiv:2608.25278, choose the redshift that maximises the departure from −1
  and obtain 3.01–3.22σ for `w < −1` before the crossing and 3.30–3.55σ for
  `w > −1` after it, within CPL [src].
- **The constraint from theory.** Lewis and Chamberlain 2024,
  arXiv:2412.13894: the null energy condition imposes inequalities on `D_H`,
  `D_M`, `D_V` and `F_AP` relative to ΛCDM once `theta_*` is fixed; the DESI
  DR2 tension "arises primarily in directions that are inconsistent with the
  null-energy condition, so ΛCDM is favoured by current acoustic scale
  measurements unless the null-energy condition is violated" [src]. A single
  minimally coupled scalar field (quintessence) therefore cannot reproduce the
  BAO + CMB part of the signal.
- **Can a non-crossing model fake it?** Keeley, Shafieloo and Matthewson 2025,
  arXiv:2506.15091: in 1,000 mocks drawn from an algebraic-quintessence
  fiducial, CPL with a phantom crossing beats the real-data `chi2` improvement
  in 3.2% of cases [src]. Roughly a 2σ statement: the crossing is preferred,
  not established.
- **Thawing quintessence.** DESI's own test gives `Delta chi2` of −2.9 to
  −13.2 for algebraic thawing against −10.7 to −21.0 for `w0wa`
  (arXiv:2503.14743) [src]. Shlivko 2025, arXiv:2512.20832, finds thawing
  quintessence "consistently preferred over a cosmological constant" for DESI
  DR2 + Planck + ACT with any supernova compilation including DES-Dovekie, not
  sensitive to the prior but "contingent on the inclusion of supernovae"
  [src]. The two statements are compatible: thawing beats Λ when supernovae
  are included, and CPL beats thawing.
- **Modified gravity reading.** Ye et al. 2024, arXiv:2407.15832: a
  non-parametric reconstruction in Horndeski gravity implies that "gravity
  should be nonminimally coupled" to give a stable phantom crossing [src]. Pan
  and Ye 2025, arXiv:2503.19898, claim "the first 3σ evidence for non-minimal
  coupling" from DESI DR2 + CMB + SN in an EFT reconstruction [src]. Wen et
  al. 2026, arXiv:2609.40176: a one-parameter "cosmic glitch" model gives
  `G_cosmo/G_N = 0.9920 ± 0.0025` (3.3σ) from Planck + ACT + SPT + DESI DR2
  [src]. These are re-descriptions of the same background mismatch; none adds
  independent data. The perturbation-level tests that could separate them are
  in `results.md` Section 6 and do not show a departure from general
  relativity.
- **Status.** Open. The crossing is a feature of the best-fit CPL line; its
  significance as a physical statement is about 2–3.5σ depending on the test,
  and it disappears if the low-redshift supernova offset or the CMB lensing/τ
  inputs move.

### 1.7 Statistics of repeated looks
<!-- key: statistics-of-repeated-looks -->

Kim et al. (arXiv:2607.28918) point out that Wilks-based σ values are read as
if the test were done once, while DR1, DR2, DR3 are successive looks at
accumulating data; they recommend reporting an anytime-valid e-value with its
test specification alongside σ [src]. No collaboration paper does so at the
snapshot.

## 2. Modified gravity: live questions
<!-- key: modified-gravity-live-questions -->

### 2.1 Is there any perturbation-level anomaly at all?
<!-- key: is-there-any-perturbation-level-anomaly-at-all -->

- **No, in collaboration analyses.** DESI DR1 full shape + CMB + DES Y3 +
  DESY5: `mu0 = 0.05 ± 0.22`, `Sigma0 = 0.008 ± 0.045`, binned parameters all
  consistent with GR (Ishak et al. 2024, arXiv:2411.12026). DES Y3 + external:
  `Sigma0 = 0.04 ± 0.05` (DES Collaboration 2022, arXiv:2207.05766). ACT DR6:
  growth as predicted by GR (Calabrese et al. 2025, arXiv:2503.14454). `E_G`
  from Planck × BOSS and from DESI DR1 × KiDS/DES/HSC consistent with GR
  (Wenzl et al. 2024, arXiv:2401.12971; Rauhut et al. 2025, arXiv:2507.16098)
  [src].
- **Yes, in some external analyses.** `Sigma0 = 0.149 ± 0.051` (3.0σ) with
  KiDS-Legacy and Planck + ACT + SPT (Du et al. 2026, arXiv:2602.03110);
  growth index `gamma = 0.633 (+0.025/−0.024)` (3.7σ) (Nguyen, Huterer and Wen
  2023, arXiv:2302.01331); a "mild yet consistent indication for c_B > 0" in
  DESI's own α-basis fit (arXiv:2411.12026) [src].
- **Common thread.** Each positive result leans on the CMB lensing amplitude:
  the Σ0 result is attributed by its authors to large-scale CMB lensing; the
  Planck part of the γ result trades against curvature, as the PR3 smoothing
  anomaly does; DESI shows the PR3 Σ0 tension vanishes with PR4 likelihoods.
  The question reduces to whether the CMB lensing amplitude is anomalous,
  which is a `cosmo-cmb` question.
- **Status.** No confirmed departure from GR. The γ result has not been
  re-derived with PR4 likelihoods and DESI data in any paper read this
  session.

### 2.2 Does modified gravity explain the DESI signal?
<!-- key: does-modified-gravity-explain-the-desi-signal -->

- **For.** A stable phantom crossing needs more than a minimally coupled
  scalar; non-minimal coupling provides it (Ye et al. 2024, arXiv:2407.15832;
  Pan and Ye 2025, arXiv:2503.19898, "3σ evidence for non-minimal coupling")
  [src]. In DR1 the Horndeski fit was as good as CPL: 2.4σ against 2.5σ from
  ΛCDM (Chudaykin and Kunz 2024, arXiv:2407.02558) [src].
- **Against.** These fits use the same background data and reach the same
  significance as CPL; the perturbation data that would distinguish them pull
  back to GR: "the inclusion of cosmic shear and CMB lensing data
  significantly shifts the constraints towards GR" (Rebouças et al. 2026,
  arXiv:2606.00411) [src]; DESI finds `mu0`, `Sigma0` consistent with GR in a
  `w0wa` background while still preferring `w0 > −1`, `wa < 0`
  (arXiv:2411.12026) [src].
- **Competing re-descriptions.** Interacting dark energy at 3–5σ, robust to
  DES-Dovekie, matching or exceeding CPL with the same number of parameters
  (Li et al. 2026, arXiv:2601.07361) [src]; a cosmological gravitational
  constant 0.8% below Newton's at 3.3σ (Wen et al. 2026, arXiv:2609.40176)
  [src]. The review of Li et al. 2026, arXiv:2606.21826, lists interacting
  dark energy, non-minimally coupled gravity and non-standard dark matter as
  producing the same effective departure from `w = −1` at the background level
  [src].
- **What would decide.** A perturbation-level prediction that differs between
  models: scale-dependent growth, `Sigma ≠ 1`, a specific ISW or lensing
  signature. Li et al. (arXiv:2601.07361) say so explicitly: future
  weak-lensing and clustering measurements are necessary to distinguish the
  paradigms [src].

### 2.3 What is left of scalar–tensor dark energy after GW170817
<!-- key: what-is-left-of-scalar-tensor-dark-energy-after -->

Settled: the luminal speed of gravitational waves at LIGO frequencies removes
quartic and quintic Horndeski terms as drivers of acceleration (Ezquiaga and
Zumalacárregui 2017, arXiv:1710.05901; Creminelli and Vernizzi 2017,
arXiv:1710.05877; Baker et al. 2017, arXiv:1710.06394) [src]. Open: whether
the surviving conformally coupled models can produce the DESI-like background
without violating local tests, which requires screening
(`physics-and-methods.md` Section 5), and whether the EFT used for cosmology
is valid at the frequency of the gravitational-wave measurement (not re-read
this session; see "Not verified").

### 2.4 Which `f(R)` bound is "the" bound
<!-- key: which-f-r-bound-is-the-bound -->

| Regime | Bound on `abs(f_R0)` | Source |
|---|---|---|
| Galaxy morphology | `< 1.4 × 10^-8` | Desmond and Ferreira 2020, arXiv:2009.08743 [src] |
| Cluster abundance | `< 10^-4.79` | Cataneo et al. 2014, arXiv:1412.0133 [src] |
| Cluster lensing + kinematics | `≲ (2–5) × 10^-5` | Pizzuti et al. 2026, arXiv:2604.23631 [src] |
| Galaxy power spectrum, DESI DR1 | `< 10^-4.59` | Gonzalez et al. 2026, arXiv:2604.26915 [src] |

Desmond and Ferreira state that their bound forces "practically all
astrophysical" objects to be screened (the abstract was read up to that
point), and their title calls astrophysically relevant Hu–Sawicki `f(R)` ruled
out [src]. Cosmological analyses keep quoting 10^-5-level bounds because they
are independent of galaxy-formation modelling. Both are correct statements
about different assumptions; a paper should say which it relies on.

### 2.5 Is `E_G` still worth measuring?
<!-- key: is-eg-still-worth-measuring -->

For: it is model-agnostic and uses linear scales only (Leonard et al. 2025,
arXiv:2511.19194) [src]. Against: its GR prediction needs `Omega_m,0` from
elsewhere, its bias cancellation is approximate, and a joint μ–Σ fit uses the
same data with a proper likelihood. Current practice is to publish both
(arXiv:2507.16098; Zhang et al. 2026, arXiv:2604.24631) [src].

## 3. Method debates
<!-- key: method-debates -->

- **Frequentist versus Bayesian headline.** The collaborations quote `Delta
  chi2` → σ; critics quote evidences with theory priors (Toomey et al. 2025,
  arXiv:2509.13318) [src]. Herold and Karwal 2025, arXiv:2506.12004, show the
  two agree on the parameter constraints for BAO + CMB + SN [src]; they do not
  agree on model preference when the supernova sample is Pantheon+
  (`results.md` Section 4).
- **Is CPL adequate?** DESI: two parameters suffice (Lodha et al. 2025,
  arXiv:2503.14743) [src]. Wolf and Ferreira 2023, arXiv:2310.07482:
  phenomenological prescriptions cannot identify the microphysics [src]. Wolf
  et al. 2024, arXiv:2408.17318: mapping thawing quintessence onto (`w0`,
  `wa`) shows it is only marginally consistent with the data [src].
- **Full-shape information.** Adding BOSS or DESI full-shape data has weakened
  the preference in three analyses (Chen and Ivanov 2025, arXiv:2507.00118;
  Forero-Sánchez et al. 2026, arXiv:2602.18761 and arXiv:2606.23936) and
  strengthened it in one (Lu and Simon 2025, arXiv:2511.10616) [src]. The
  analyses differ in priors, compression and supernova sample; no
  like-for-like comparison was found.
- **Compressed versus full CMB.** Compression isolates the early-universe
  anchor and removes lensing; the significance is lower by 0.7σ in DESI DR2
  (2.4σ against 3.1σ, arXiv:2503.14738) [src]. Which is "the" BAO + CMB number
  depends on whether CMB lensing is trusted at that level.
- **One sample or three.** With Unite available, quoting three supernova
  variants is no longer necessary; but Unite inherits the anchor of both
  parents (Camilleri et al. 2026, arXiv:2609.05053) [src].

## 4. What the next data will decide
<!-- key: what-the-next-data-will-decide -->

| Question | Deciding data | Expected | Flag |
|---|---|---|---|
| Does the BAO + CMB preference grow with volume? | DESI full-survey BAO | 2027 | [sec] `surveys-and-data.md` Section 5 |
| Is the low-redshift supernova offset real? | a homogeneous modern anchor | pending | [sec] `cosmo-supernovae` |
| Is the CMB side a τ or lensing problem? | independent τ; lensing from ACT/SPT/SO | see `cosmo-cmb` | [sec] |
| Does growth agree with the `w0wa` background in GR? | DESI DR2 full shape; Euclid DR1 | 2027 | [sec] |
| Is `Sigma0 > 0` a CMB-lensing artefact? | Euclid and Rubin lensing without CMB lensing | 2027 onward | — |
| Thawing versus phantom crossing | `sigma(wa)` several times smaller than today | Stage-IV combination | [der] `surveys-and-data.md` Section 5 |

Forecasts (all labelled **forecast**): Euclid figure of merit raised by at
least a factor of three by probe cross-correlations (arXiv:1910.09273); LSST ×
DESI `E_G` able to reject GR for some models (arXiv:2511.19194); supernova
systematics able to move `w0`–`wa` by several error ellipses in future
compilations (Dhawan, Popovic and Goobar 2024, arXiv:2409.18668) [src].

## 5. Misconceptions and stale claims
<!-- key: misconceptions-and-stale-claims -->

| Claim still in circulation | Why it is wrong or stale | Corrected by |
|---|---|---|
| "DESI finds evolving dark energy at 4.2σ" | Value with DES-SN5YR before recalibration; now 3.2–3.4σ | arXiv:2511.07517, arXiv:2601.19424 |
| "DESI alone shows dynamical dark energy" | DESI BAO alone: 1.7σ, prior-limited | arXiv:2503.14738 |
| "The signal depends on which supernova sample is used" | True in 2024–2025; the three samples now agree at 3.2–3.4σ | arXiv:2601.19424 |
| "Pantheon+ shows no preference" | Not after the host-mass correction (3.2σ) | arXiv:2601.19424 |
| "Three supernova samples confirm it independently" | They share most low-redshift supernovae | arXiv:2501.06664, arXiv:2411.11685 |
| "The data prefer `w` different from −1" | `w_p` is within 2σ of −1; the preference is for a slope | arXiv:2404.08056, arXiv:2503.14738 |
| "The data prefer thawing quintessence" | `w ≥ −1` models fit worse than CPL; the BAO + CMB tension lies in NEC-violating directions | arXiv:2503.14743, arXiv:2412.13894 |
| "Phantom crossing is detected" | Preferred within CPL; 3.2% of non-crossing mocks imitate it | arXiv:2506.15091 |
| "Evolving dark energy eases the Hubble tension" | `w0waCDM` lowers `H0` | arXiv:2503.14738 |
| "The Bayesian evidence is strong" | `ln B` from −0.66 to 4.88 by sample in DR2; "weak" after the supernova revisions | arXiv:2503.14743, arXiv:2511.07517, arXiv:2609.05053 |
| "Full-shape clustering confirms it" | DESI DR1 FS + DR2 BAO: 1.4σ; bispectrum weakens it | arXiv:2602.18761, arXiv:2606.23936 |
| "Planck shows Σ0 > 0 / modified gravity" | PR3 artefact; gone with PR4 likelihoods | arXiv:2411.12026 |
| "E_G is low at large scales" | 2015 CMASS value; calibrated estimator agrees with GR | arXiv:2401.12971 |
| "GW170817 killed modified gravity" | It removed non-conformal Horndeski couplings; conformal coupling and screening models remain | arXiv:1710.05877 |
| "f(R) is constrained to 10^-5" (as the best bound) | Galaxy-scale bound is 1.4 × 10^-8 | arXiv:2009.08743 |
| "Negative neutrino mass is a separate anomaly" | Same CMB–BAO mismatch as `w0wa`; `w0wa` restores positive mass | arXiv:2407.10965 |
| "Interacting dark energy / non-minimal coupling is detected at 3–5σ" | Re-description of the same background mismatch; lensing data pull to GR | arXiv:2606.00411 |

## 6. Not verified this session
<!-- key: not-verified-this-session -->

- The DESI DR1 full-shape value of the growth index γ, and any post-PR4 update
  of the Nguyen et al. growth-suppression result.
- Numerical Planck 2018 values of μ0 and Σ0; only their qualitative status
  (tension in PR3, removed with PR4 likelihoods) was read, in
  arXiv:2411.12026.
- The prior ranges on `w0` and `wa` in the DESI analyses beyond the `wa > −3`
  edge.
- The definitions of the calibrated-thawing, emergent and mirage one-parameter
  relations (the equations are in arXiv:2405.13588 and arXiv:2503.14743; only
  their names, parameter counts and fit statistics were read).
- Thresholds of the Jeffreys scale as used by each paper; only the DESI
  wording ("moderate ≤ 2.5", "strong ≤ 5") was read.
- Which named Horndeski models survive GW170817, and the argument that the
  cosmological EFT may not apply at LIGO frequencies.
- Vainshtein-screened model constraints (nDGP, Galileons): no number was read.
- Early dark energy, which belongs to `cosmo-tensions-anomalies` and
  `cosmo-distance-ladder-h0`, was not researched.
- DES Y6 and KiDS-Legacy collaboration constraints on μ–Σ: none found by title
  search; the KiDS-Legacy number in `results.md` is from an external analysis.
- Any DESI DR2 full-shape or DR3 result: none exists at the snapshot according
  to the sibling `cosmo-galaxy-clustering`.
- Euclid and DESI release dates come from web pages returned by a search, not
  from collaboration papers.
- The abstract of arXiv:2511.07517 was first read through a summarising fetch
  and then verbatim through the arXiv API; the Unite sensitivity to the `z <
  0.1` cut is quoted from the sibling `cosmo-supernovae`, not from
  arXiv:2609.05053 itself.
