# Open questions — live controversies, internal tensions, and stale claims

Scope: the debates about the value of H0 that are unresolved in October 2026,
with both sides cited; what the next data will decide; forecasts (labelled);
and the misconceptions that still circulate, each with the paper that
corrects it.
Snapshot: 2026-10-07

Flags: `[src]` read this session in the cited paper; `[sec]` from a named
secondary source; `[der]` derived here. H0 in km/s/Mpc.

## 1. Is the local ladder value 73 or 70?

**Position A (SH0ES, H0DN).** The Cepheid-SN Ia ladder gives 73.17 ± 0.86
with four anchors (arXiv:2404.08038), 73.18 ± 0.88 with JWST Cepheids and 35
TRGB hosts (arXiv:2509.01667), and the community network gives 73.50 ± 0.81
with first-rank indicators internally consistent; removing Cepheids or TRGB
has minimal effect, and replacing SNe Ia by galaxy-based indicators changes
H0 by less than 0.1 while doubling the error `[src]` (arXiv:2510.23823).

**Position B (CCHP).** The CCHP "current best (highest precision) estimate"
is 70.39 ± 1.22 (stat) ± 1.33 (sys) ± 0.70 (sigma_SN), "based on the TRGB
method alone, with a total of 24 SN Ia calibrators from both HST and JWST
data"; it is not a JWST-only number and the JAGB does not enter it. From the
new JWST data only (10 galaxies hosting 11 SNe Ia, zero point from NGC 4258)
the same paper gives two separate values: 68.81 ± 1.79 (stat) ± 1.32 (sys)
for the TRGB and 67.80 ± 2.17 (stat) ± 1.64 (sys) for the JAGB. The abstract
calls the results "consistent with the current standard LambdaCDM model,
without the need for the inclusion of additional new physics" `[src]`
(Freedman et al. 2024, arXiv:2408.06153, abstract re-read 2026-10-08). The
programme also targets Cepheids, but that paper reports the TRGB and JAGB
only.

**Where the two actually differ.** Not in the stellar distances: TRGB and
JAGB agree with each other to better than 1% and with SH0ES Cepheid distances
at just over 1% `[src]` (arXiv:2408.06153); HST Cepheids agree with every
JWST indicator at about 0.03 mag `[src]` (arXiv:2408.11770). The difference
sits in (i) which SN Ia calibrators are in the sample and (ii) which SN
compilation and corrections form the Hubble flow.

- SH0ES reading: the CCHP JWST subsample is a low fluctuation of a small
  sample; the 11 TRGB hosts left out of the CCHP 24 give 74.1, and the
  complete N = 35 TRGB sample gives 72.1 to 73.3 ± 1.8 `[src]`
  (arXiv:2504.08921).
- CCHP reading: going from 11 to 24 calibrators moves the CSP-II based H0 by
  only 0.8 (1.4 sigma), so the JWST result is not significantly biased low,
  whereas the Pantheon+ calibration shifts by +2 (3.1 sigma), more than in
  CSP or in the Pantheon team's own SuperCal analysis `[src]` (Hoyt et al.
  2025, arXiv:2503.11769).

**What would settle it.** A common, pre-specified calibrator list with all
indicators measured in every host; a second anchor for the JWST ladders;
independent low-z SN photometry. The 2026 ladder review asks for exactly
these (arXiv:2606.26831).

**Newer CCHP lines.** A 2026 reanalysis of Milky Way Cepheids argues that
Gaia parallax errors, not metallicity, drive the PL residuals and proposes a
period-luminosity-colour calibration with 0.04 mag scatter `[src]` (Madore &
Freedman 2026, arXiv:2602.13397). The SH0ES side rejects the associated
recalibration of Gaia (arXiv:2507.15936). No H0 value from the revised
calibration was found in this session.

## 2. Does the statistical model of the ladder matter at the 2 to 3 level?

Raised in 2025 (Desmond et al., arXiv:2511.03394): implicit flat priors on
distance moduli bias H0 high; selection terms partly compensate; both should
be captured by SH0ES's simulation-based corrections but need explicit
modelling `[src]`.

- Högås & Mörtsell (2026, arXiv:2601.22215): physically motivated priors on
  all distances, Milky Way Cepheids in the joint fit, a conservative Gaia
  offset: 70.6 ± 1.0, tension reduced from 5 to 2 sigma `[src]`.
- Stiskalek et al. (2026, arXiv:2603.09880, with SH0ES co-authors): the same
  prior without the selection function mis-predicts the observed parallax,
  magnitude and period distributions; with selection, the SH0ES calibration
  is recovered within 0.5 sigma and the claimed shift is "unjustified"
  `[src]`.
- Percival (2026, arXiv:2607.22425): a likelihood for truncated selection in
  correlated observables finds 1.3 to 2.3 sigma evidence for residual
  selection in calibrator-galaxy Cepheids and shifts of -1.4, -0.2 and -1.0
  that together "substantially reduce" the tension `[src]`.
- Stiskalek et al. (2025, arXiv:2509.09665): a Cepheid-only two-rung ladder
  with explicit selection and a field-level velocity model gives 71.1 ± 1.4;
  other selection assumptions raise it by up to one sigma `[src]`. It is
  2.7 sigma from the CMB value `[der]` (against 67.24 ± 0.35; the paper
  states 2.8).

**Why it is unresolved.** The SH0ES hosts were chosen over three decades
without a single documented rule (arXiv:2204.10866), so the selection model
is itself a prior. The Milky Way step is settled in favour of SH0ES by
arXiv:2603.09880; the extragalactic step (Percival's parameter) is not.

## 3. Is the tension "ladder versus everything else"?

**Claim.** Among 88 sound-horizon-free measurements, 30 ladder-based ones
average 72.73 ± 0.39 and 58 others 69.37 ± 0.34, a 6.5 sigma split (3.9 sigma
at least after correlations); measurements that assume LCDM give the lowest
values (67.61 ± 0.96) `[src]` (Pantos & Perivolaropoulos 2026,
arXiv:2601.00650).

**Counter-evidence.**

- One-step and SN-free routes that return high values: SBF 73.8 ± 2.4 total
  (arXiv:2502.15935), SNe II by spectral modelling 74.9 ± 1.9 (stat)
  (arXiv:2411.04968), megamasers 73.9 ± 3.0 (arXiv:2001.09213, now
  contested), single-lens TDCOSMO values of 73 to 74 (arXiv:2604.14145,
  arXiv:2608.27566).
- Averages of heterogeneous published values inherit their correlations and
  selection; a Bayesian jackknife over 16 measurements finds many grouping
  scenarios with similar evidence and only disfavours "no measurement is
  biased" `[src]` (Hughes et al. 2025, arXiv:2511.19341).
- BAO + BBN is 4.5 sigma from SH0ES without any CMB anisotropy data `[src]`
  (arXiv:2503.14738), and the equality-scale H0 (66.7 to 67.9) is still 2.2
  to 3.0 sigma from SH0ES `[src]` (arXiv:2411.16677): the low camp does not
  rest on one probe either.

**Honest summary.** Routes with errors below 2 split cleanly (ladder high;
CMB, BAO + BBN, inverse ladder low). Routes with errors of 3 to 5 (lensing,
masers, sirens) are compatible with both, and their central values have moved
with modelling choices.

## 4. Megamasers: 73.9, 71.6 or 67?

The 2020 MCP value of 73.9 ± 3.0 used a fixed 250 km/s velocity noise and no
flow correction (arXiv:2001.09213). Two 2026 reanalyses with
constrained-simulation velocity fields disagree:

- Watkins & Feldman (arXiv:2608.06247): 66.9 ± 2.5 to 68.8 ± 2.6 depending on
  the assumed velocity noise, consistent with the CMB and more than 2 sigma
  below the ladder; they argue earlier results were biased by peculiar
  velocities `[src]`.
- Stiskalek & Desmond (arXiv:2609.17684): 71.6 ± 3.7 from five galaxies
  refitted at the spot-catalogue level with a distance prior and selection;
  velocity corrections lower H0 by 1.6 to 2.1 `[src]`.

Both lower the 2020 value; they differ on by how much. With six objects the
outcome hinges on the velocity model of each host and on the error assigned to
it. Do not cite megamasers as support for either camp without naming the
analysis.

## 5. Time-delay cosmography after the mass-sheet reckoning

Kochanek (2020, arXiv:1911.05083) argued that no lensing H0 is more accurate
than ~10% because the convergence at the Einstein radius is unconstrained.
TDCOSMO accepted the degeneracy and constrains it with kinematics: 71.6
(+3.9/-3.3) from 8 lenses, 4.6% with external lenses (arXiv:2506.03023). A
2026 study lists kinematic systematics of several per cent in sigma^2 from
the PSF, the anisotropy model and the light-versus-mass profile, each
comparable to the target precision `[src]` (arXiv:2602.03934).

Open points: whether SLACS and SL2S deflectors share the population of the
time-delay lenses (arXiv:2007.02941); whether lambda_int differs from 1
(1.12 +0.05/-0.06 in one system, arXiv:2604.14145); the status of cluster
lenses, where three lensed SNe give 64.8 to 75.7 with errors of 4 to 11
(arXiv:2305.06367, arXiv:2403.18902, arXiv:2509.12301).

**Forecast.** 3.3% with resolved kinematics of the 7 original lenses, 2.5%
adding 50 non-time-delay lenses, 1.5% and 1.2% with 40 time-delay and 200
other lenses, all without profile assumptions (Birrer & Treu 2021,
arXiv:2008.06157) `[src]`.

## 6. Coma and the Fundamental Plane

The DESI FP relation fixes H0 times D_Coma. With D_Coma = 98.5 ± 2.2 Mpc from
SNe Ia on the HST ladder, H0 = 76.5 ± 2.2; the Planck value requires
111.8 ± 1.8 Mpc, 4.6 sigma beyond the direct measures, and independent
routes (Key Project FP with Cepheids, JWST TRGB, HST SBF) all give less than
100 Mpc `[src]` (Scolnic et al. 2025, arXiv:2409.14546). The argument recasts
the tension as a statement about one well-studied distance. Weak points a
referee will raise: every Coma distance quoted traces back to the same
anchors; the FP zero point from one cluster carries its peculiar velocity and
the FP's environmental dependence; the DESI DR1 follow-up with a group
catalogue gives 73.7 ± 1.1 once calibrated on SH0ES SNe (arXiv:2512.03232).

## 7. A local void or outflow

**For.** Near-infrared luminosity density rises by ~1.5 beyond z ~ 0.07,
suggesting a ~300 Mpc under-density (Keenan et al. 2013, arXiv:1304.2884)
`[src]`. Taken at face value (density contrast 0.46 ± 0.06 between 40 and 300
Mpc) such a void could account for the tension but is itself in 6.04 sigma
tension with LCDM, which motivated a MOND-based cosmology (Haslbauer et al.
2020, arXiv:2009.11292) `[src]`. A 2026 perspective connects the void to
low-redshift BAO deviations and predicts convergence to the CMB value at
z > 0.2 (Banik et al. 2026, arXiv:2602.03928) `[src]`.

**Against.** The SN Ia Hubble diagram at 0.023 < z < 0.15 shows no step and
excludes contrasts above 27% on > 69 Mpc/h scales at 5 sigma
(arXiv:1901.08681); LCDM sample variance is 0.31 (arXiv:1706.09723); flow
corrections raise rather than lower H0 (arXiv:2110.03487). Fitting void
profiles to Cosmicflows-4 Tully-Fisher distances at the field level prefers a
void smaller than 70 Mpc, under 10% of the proposed size; the profiles give
local H0 of 72.1 (+0.9/-0.8), 70.4 ± 0.4 or 70.2 (+0.5/-0.4), the first being
disfavoured by the evidence, and the predicted bulk flows disagree with
Cosmicflows-4 `[src]` (Stiskalek et al. 2025, arXiv:2506.10518). The
Manticore-Local reconstruction finds no large local under-density `[src]`
(arXiv:2505.10682). The 2026 decade review states that a local void "has
long been ruled out as a significant contribution" `[src]` (Cai & Wang 2026,
arXiv:2606.20434).

**Status.** Minority position, still published. The decisive data are direct
distances and velocities at 100 to 300 Mpc (DESI PV, WALLABY); see
`cosmo-peculiar-velocities`.

## 8. Theory status (summary; details in sibling skills)

**Late-time fixes do not work, by construction.** The ladder constrains M_B;
any smooth late-time change of H(z) is bounded by BAO + uncalibrated SNe
(Efstathiou 2021, arXiv:2103.08723). A model that fits SH0ES, DESI BAO and
SNe needs either a step in M_B at z ~ 0.01 or a violation of distance duality
`[src]` (Bansal & Huterer 2026, arXiv:2602.06293). The inverse ladder cannot
be moved to 73 by SN systematics: known systematics shift it by less than
0.1, and the required d mu / dz = 0.2 mag would give Omega_M = 0.23, 10 sigma
from other probes `[src]` (Popovic & Sullivan 2026, arXiv:2602.12822). The
DESI preference for evolving dark energy (2.8 to 4.2 sigma with SNe as
published in arXiv:2503.14738; revised since by supernova recalibrations, see
`cosmo-supernovae`) does not change this (Efstathiou 2026, arXiv:2607.29562)
`[src]`.

**Early-time fixes are constrained but alive.**

- ACT DR6 finds no evidence for early dark energy, extra radiation, varying
  constants, primordial magnetic fields or modified recombination; models
  built to raise H0 are "not favored" `[src]` (Calabrese et al. 2025,
  arXiv:2503.14454).
- SPT-3G: f_EDE < 0.12 (SPT alone), < 0.070 (SPT + ACT + Planck) at 95%,
  tension 3.6 sigma; adding DESI gives f_EDE = 0.055 (+0.024/-0.047) and
  2.6 sigma, driven by the CMB-DESI discrepancy in LCDM `[src]` (Khalife et
  al. 2025, arXiv:2507.23355).
- A profile-likelihood analysis with ACT DR6 + DESI DR2 gives f_EDE = 0.09 ±
  0.03 and H0 = 71.0 ± 1.1, residual tension ~2 sigma, and stresses
  prior-volume effects in the Bayesian limits `[src]` (Poulin et al. 2025,
  arXiv:2505.08051). Review of the model class: Poulin et al. 2023,
  arXiv:2302.09032.
- SPT + ACT + Planck + DESI show mild preferences for modified recombination
  or a varying electron mass in a non-flat universe `[src]`
  (arXiv:2506.20707).
- Structural limits: reducing r_d alone conflicts with BAO or weak lensing
  (arXiv:2010.04158); r_d-free H0 estimates stay low (arXiv:2411.16677),
  though with r_d free and newer data one finds 70.0 ± 1.7
  (arXiv:2509.16202).

Model catalogues and rankings: arXiv:2107.10291 and arXiv:2504.01669; go to
`cosmo-tensions-anomalies` and `cosmo-dark-energy-modified-gravity`.

## 9. Were the errors ever right?

A historical analysis of 163 H0 values from 1976 to 2019 finds a chi^2 of 580
about the weighted mean and concludes that published errors are generically
underestimated, recalibrating a nominal 4.4 sigma to 2.1 sigma and
attributing the attention to "groupthink" `[src]` (Lopez-Corredoira 2024,
arXiv:2411.13621). The answer of the field is procedural rather than
rhetorical: JWST cross-checks of the photometry (arXiv:2401.04773),
leave-one-out variants and an independent community pipeline
(arXiv:2510.23823). Cite the critique when discussing sociology; it is not a
measurement.

## 10. What the next data will decide

| Question | Data | When | Flag |
|---|---|---|---|
| Gaia zero point and the MW anchor | Gaia DR4 | 2 December 2026 | [src] ESA page |
| Calibrator sample variance; JAGB standardisation | more JWST hosts; spectroscopic purity surveys (arXiv:2609.25412) | ongoing | [src] |
| Time-delay H0 at ~3% without profile assumptions | TDCOSMO-2026 hierarchical analysis | announced (arXiv:2608.27566) | [src] |
| Third rung without SNe at 1% | DESI PV calibrated directly on Cepheids / TRGB | later DESI releases (arXiv:2512.03232) | [src] |
| Two-rung ladders | TRGB beyond cz ~ 1000 km/s and better local reconstructions (arXiv:2609.29996) | open | [src] |
| r_d-free early H0 | completed DESI + SO-like lensing: sigma(H0) ~ 0.67, **forecast** (arXiv:2509.16202) | late 2020s | [src] |

## 11. Stale or wrong claims that still circulate

| Claim | Why it is wrong or stale | Correcting paper |
|---|---|---|
| "Cepheid crowding in HST photometry may explain the tension." | JWST: -0.01 ± 0.03 mag, rejected at 8.2 sigma; no bias in 19 hosts | arXiv:2401.04773; arXiv:2509.01667 |
| "JWST found H0 = 69, so the tension is gone." | CCHP's result is 70.39 with a total error of 1.94; the distances agree with SH0ES at ~1%; the difference is the SN calibrator subsample | arXiv:2408.06153; arXiv:2408.11770; arXiv:2504.08921 |
| "The TRGB gives 69.8." | That is the 2021 CCHP HST value; other TRGB analyses give 72 to 73, and none of 108 CATS variants is below 71.6 | arXiv:2106.15656; arXiv:2304.06693; arXiv:2504.08921 |
| "Lensing gives 73.3 at 2.4%, 5.3 sigma with the ladder." | Assumed power-law or composite profiles; with the mass-sheet degeneracy free the result is 71.6 (+3.9/-3.3) | arXiv:1907.04869; arXiv:2007.02941; arXiv:2506.03023 |
| "Megamasers independently confirm 73.9." | No flow correction in that value; 2026 reanalyses give 66.9 to 71.6 | arXiv:2608.06247; arXiv:2609.17684 |
| "The tension is 4.4 sigma" (or "5 sigma") with no qualifier. | 4.4 is the 2019 figure and 5.0 the 2022 one against Planck 2018; today's figure runs from 4.4 to 7.1 for the SH0ES and H0DN values depending on the early-Universe endpoint | arXiv:1903.07603; arXiv:2112.04510; `results.md` Section 5 |
| "Planck is the outlier." | SPT-3G alone gives 66.66 ± 0.60; BAO + BBN gives 68.51 ± 0.58 with no CMB anisotropies | arXiv:2506.20707; arXiv:2503.14738 |
| "SH0ES and CCHP are independent measurements." | Same anchor (NGC 4258) for the JWST work, overlapping SN hosts, overlapping low-z SNe | arXiv:2408.11770 |
| "DESI's 73.7 from peculiar velocities is an independent H0." | Its zero point is the SH0ES / Pantheon+ SN Ia calibration | arXiv:2512.03232 |
| "Dynamical dark energy (DESI) relieves the H0 tension." | The ladder-CMB mismatch is in M_B and is insensitive to the late expansion history | arXiv:2607.29562; arXiv:2103.08723 |
| "A late-time transition or phantom dark energy can raise H0." | Requires a step in M_B at z ~ 0.01 or broken distance duality | arXiv:2602.06293 |
| "We live in a void that explains it." | Direct distances limit the void to < 70 Mpc; SN Hubble diagram shows no step | arXiv:2506.10518; arXiv:1901.08681 |
| "The Cepheid metallicity term could shift H0 by per cents." | Anchors and hosts have similar metallicity; gamma matters for dwarf-galaxy distances, not for H0 | arXiv:2507.15936 |
| "A volume prior lowers H0 to 70.6, so the tension is statistical." | Without the selection term the model fails posterior predictive checks; with it the SH0ES zero point is recovered | arXiv:2603.09880 |
| "Use the SH0ES H0 as a Gaussian prior in a cosmological fit." | Double counts low-z SNe and fixes q0; use the M_B calibration | arXiv:2103.08723 |
| "Standard sirens already weigh in." | 75.4 (+12.8/-9.1) from GWTC-4.0 | arXiv:2509.04348 |

## Not verified

- An H0 value from the CCHP with the 2026 revised Milky Way Cepheid
  calibration; the CCHP JWST Cepheid result. A date-sorted arXiv search on
  2026-10-08 (author Freedman, abstract "Hubble constant" or Cepheid(s),
  2025-01-01 to 2026-10-08) returned four papers, none of which reports a
  CCHP Cepheid-based or combined H0: the latest CCHP H0 values found remain
  those of arXiv:2408.06153 and arXiv:2503.11769. The search matches author
  and abstract words only, so a paper with other wording would be missed.
- The H0 preferred by CMB + BAO in w0waCDM, and whether it is lower than in
  LCDM.
- The M_B prior values to use in place of an H0 prior (the paper proposing
  them, read this session, is not in `sources.tsv`).
- Claims of anisotropy or redshift evolution ("running") of H0: several 2025-
  2026 preprints were seen in searches and not read.
- Whether a TDCOSMO-2026 or SH0ES-2026 milestone paper has appeared after
  1 October 2026.
