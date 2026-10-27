# Machine learning in cosmology — open questions

Scope: live method debates, robustness controversies, what the next data and challenges will decide, and stale claims.
Snapshot: 2026-10-17

Flags: as in `physics-and-methods.md`.

## 1. How much does a network add beyond physical summaries?
<!-- key: how-much-does-a-network-add-beyond-physical -->

**The gain depends on the comparison and on noise.** On noiseless
simulated maps a CNN gave a ≈ 5 times smaller contour than the power
spectrum (arXiv:1802.01212) [src: abstract]; on survey data the gains on S8 are 16%
(KiDS-1000, arXiv:2201.07771) [src: abstract] and 5–24% (HSC Y1, arXiv:2301.01354) [src: abstract],
with larger gains on Ω_m or w. A claimed factor must name the baseline
statistic, the noise level and the scale cut.

**The loss function sets the ceiling.** MSE or MAE regression returns the
posterior mean or median, which is not a sufficient statistic; on a
controlled test it reaches 81% of the attainable figure of merit against
100% for VMIM (arXiv:2407.10877) [src: abstract]. The DES Y3 case is now
measured: on the same lensing maps a VMIM hybrid compression gives a 60%
larger FoM(Ω_m, S8, w) than the earlier MSE-trained CNN result
(arXiv:2606.11309) [src: abstract, Sect. 8.1], though the architecture
changed at the same time [src: Sect. 6.2].

Several published analyses
trained with MSE or MAE: arXiv:2407.10877 lists them in its Sect. 3
[src: Sect. 3], and its MSE list includes a 2023 analysis by Lu et al.,
which by author and year matches the HSC Y1 paper arXiv:2301.01354 [der].
The HSC Y1 paper itself states an MSE loss (arXiv:2301.01354)
[src: Eq. 32], and so does the DES Y3 C_ℓ × CNN analysis
(arXiv:2403.02314) [src: Sect. 6.2, 6.3]. Their quoted gains are then
lower bounds on what a sufficiency-trained network could extract, not the
information content of the data [der].

**A single network is not a statistic.** Sáez-Casares et al. 2026 find that
one CNN can be less informative than the power spectrum and that an
ensemble selected by posterior volume is needed (arXiv:2610.19891) [src].
How much of a reported network gain survives a change of architecture or
random seed is rarely reported; the KiDS-1000 GCNN analysis is an
exception, with three fiducial and three modified "benchmark networks"
(arXiv:2201.07771) [src: Sect. IV.6].

The field-level-inference debate with sampled initial conditions
(LEFTfield, BORG against perturbative P + B likelihoods) is in
`cosmo-beyond-two-point`; it is not a machine-learning question.

## 2. Can training on simulations be trusted on data?
<!-- key: can-training-on-simulations-be-trusted-on-data -->

**Optimistic side.** Networks trained on one hydrodynamic suite recover
Ω_m and σ8 on another from total-mass maps (arXiv:2109.10360) [src], and
graph networks on galaxy positions and velocities are robust across five
codes and finders (arXiv:2302.14101) [src]. Self-supervised encoders
pre-trained on a cheap simulator transfer to a radiative-transfer one
(arXiv:2608.26354) [src].

**The same input, opposite verdicts.** Graph networks on galaxy positions
and velocities were robust across five codes (arXiv:2302.14101) [src]; a
GNN with the same kind of input (positions and line-of-sight velocities)
fails on CAMELS-CROCODILE, mainly where the galaxy number exceeds the
training range (arXiv:2609.23982) [src: Sect. IV.1]. Robustness established
on one set of simulators does not carry to the next one.

**Sceptical side.** Robustness depends on the input: galaxy internal
properties and halo concentration break it (arXiv:2201.02202,
arXiv:2209.06843) [src]; a new sub-grid model outside the training range
makes a GNN fail and stay overconfident (arXiv:2609.23982) [src]; WST
posteriors on BOSS change with the flow architecture, which the SimBIG
authors read as misspecification (arXiv:2310.15250) [src]. All these tests
compare simulators with one another, and the spread of simulators is a
lower bound on the distance to the real Universe: CAMELS-CROCODILE
suppresses P(k) by a few per cent against up to ~27% for IllustrisTNG
at z = 0 (arXiv:2609.23982) [src: abstract].

**What would settle it.** A blind test on data from a simulator built by a
group outside the training collaboration, with the out-of-distribution
detection of the FAIR Universe challenge (arXiv:2604.14451) [src]; and a
data analysis whose neural result is compared, on the same data and scale
cuts, with an explicit-likelihood analysis (KiDS-SBI did this for a
two-point statistic, arXiv:2404.15402 [src]).

## 3. Interpretability
<!-- key: interpretability -->

**Is a black box acceptable for a cosmological parameter?** Saliency
studies can say where a lensing CNN looks (negative-κ regions in noiseless
maps, peaks with noise; arXiv:2007.06529) [src], but not which physical
process it relies on, which is what a robustness argument needs. Two
answers are being developed: networks whose summaries are physically
parametrised and so readable (neural marks, arXiv:2606.11295) [src], and
symbolic replacement of networks, which generalised out of distribution
better than the GNN it was distilled from (arXiv:2006.11287) [src].
Symbolic emulators of P_L(k) (0.2% RMS fractional error, arXiv:2311.15865,
abstract) and C_ℓ^φφ (mean absolute fractional error 0.27% in the ΛCDM
subspace and 0.32% over the extended parameter space, arXiv:2606.07745,
abstract) match neural ones on smooth targets; whether
the approach scales to high-dimensional or field-level targets is open.

**Symbolic regression as model discovery.** Exhaustive symbolic regression
finds ~40 functions describing H(z) from chronometers and Pantheon+ more
economically than the Friedmann equation (arXiv:2211.11461) [src: abstract]. The
authors' reading is that the low-z data do not uniquely prefer the
standard expansion history; it is not evidence against ΛCDM.

## 3b. Foundation models and self-supervised encoders
<!-- key: foundation-models-and-self-supervised-encoders -->

**The claim.** A large encoder pre-trained without labels on cheap
simulations or survey data gives summaries that transfer across simulators
and tasks. SKATR, a Vision Transformer pre-trained with a joint-embedding
objective on 67 325 semi-numerical 21cmFAST light-cones [src: Sect. 2.1], is applied frozen
to hydrodynamical Loreli II light-cones and gives the most precise and
best-calibrated posteriors of the comparison while needing 2.6 times fewer
radiative-transfer simulations than the supervised in-domain baseline
(arXiv:2608.26354) [src: abstract].

**The caution.** The DESC white paper accepts foundation models and
LLM-driven agents only "coupled with rigorous evaluation and governance"
(arXiv:2601.14235) [src]. No cosmological parameter from survey data
obtained through a foundation-model encoder was found in this session.

## 3c. Emulators: neural, Gaussian-process or symbolic?
<!-- key: emulators-neural-gaussian-process-or-symbolic -->

Early emulators interpolated tens of simulations (37 for the Coyote
Universe, arXiv:0902.0429) [src: abstract]. Gaussian processes "struggle with scalability in
sample size and dimensionality", and a neural multi-fidelity emulator beat
the earlier Gaussian process by more than five in mean error on the same
suite (arXiv:2507.07184) [src]. Symbolic emulators are competitive for
smooth one-dimensional targets and remain analytic
(arXiv:2311.15865, arXiv:2606.07745) [src]. For multi-tracer EFT
multipoles, emulating the loop kernels from a spline of the linear P(k)
removes the dependence on a fixed cosmological model (arXiv:2507.20990)
[src]. The open question is not accuracy at the training cosmology but
behaviour at the edge of the training box, for example for the w0wa region
preferred by recent BAO data; the sibling `cosmo-simulations-mocks` lists
this as unchecked for the gravity-only emulators.

## 4. What the next data will decide
<!-- key: what-the-next-data-will-decide -->

- **DES Y3 map-level weak lensing + clustering SBI.** The analysis design
  forecasts 2–3 times the Ω_m–S8 figure of merit of its two-point baseline
  (**forecast**, arXiv:2511.04681) [src: abstract]; the data analysis is announced as
  forthcoming in that paper. A date-sorted arXiv search from November 2025
  (run 2026-10-16) returned no combined-probe data paper, but a DES Y3
  lensing-only map-level analysis with VMIM hybrid statistics appeared in
  June 2026, S8 = 0.808 ± 0.017 in wCDM (arXiv:2606.11309, abstract), with DES Y6 announced next
  (arXiv:2606.11309) [src].
- **FAIR Universe challenge results.** The challenge tests inference with
  a limited training set and out-of-distribution detection on HSC-like
  maps (arXiv:2604.14451) [src]; the organisers' results paper was not
  found. One entrant reports first place in the public phase and in one of
  three final leaderboards (score 11.70, ±1σ coverage 0.70) with a CNN
  ensemble whose outputs feed a likelihood calibrated on the training
  grid, and notes that it degrades substantially off-grid; the organisers'
  own neural baselines detected some out-of-distribution categories worse
  than the power spectrum (arXiv:2604.09621 [src: Sect. 4];
  arXiv:2604.14451 [src: Sect. 5.2.3]).
- **Rubin alert stream.** Classifiers and anomaly detectors tuned on
  ELAsTiCC and ZTF meet real LSST alerts; the Fink authors note that the
  transition "will require significant adaptation" (arXiv:2404.08798)
  [src]. A first identification and classification of transients in Rubin
  DP1 (LSSTComCam, three fields) found eight new and three known likely
  supernovae among 369 644 difference-image objects; Superphot+, trained
  on ZTF g and r photometry and applied to redshift-matched LSSTComCam
  bands, gave four SNe IIn against expected class fractions, only two
  classifications above 95% confidence, and anomaly scores flagging all
  but one light curve as unlike ZTF, so the authors classified none
  (Freeburn et al. 2025, arXiv:2507.22864) [src: abstract, Sect. IV.2,
  Table 4].
- **Photometric SN Ia cosmology with ML classification.** The ELAsTiCC-based
  DESC study forecasts a w0wa FoM of about 150 with ~6000 events and
  reports small but significant biases (**forecast**, arXiv:2512.06319)
  [src: abstract].
- **Simulation budgets.** Multi-fidelity training (60 N-body runs suffice
  in a KiDS-Legacy mock according to the abstract, while the body places
  reliable posterior widths at N ~ 100–120; arXiv:2606.23346 [src;
  Sect. 4.2.1]) decides whether
  field-level SBI is affordable at Stage-IV fidelity.

## 5. Misconceptions and stale claims
<!-- key: misconceptions-and-stale-claims -->

| Claim | Correction | Reference |
|---|---|---|
| "A neural summary extracts all the information." | Only if trained for sufficiency; MSE summaries reached 81% of the attainable figure of merit in a controlled test | arXiv:2407.10877, abstract |
| "A CNN gives 5 times tighter lensing constraints than the power spectrum." | Noiseless simulated maps; on survey data the S8 gains are 16% (KiDS-1000) and 5–24% (HSC Y1) | arXiv:1802.01212, arXiv:2201.07771, arXiv:2301.01354, each abstract |
| "The emulator is accurate to 0.4%, so the model is accurate to 0.4%." | The figure is the residual against the training code (HMcode, CLASS); physics absent from it is not covered | arXiv:2106.03846, abstract, Sect. 3.2 |
| "Neural posteriors are calibrated if the network is trained well." | All benchmarked SBI algorithms can be overconfident; finite budgets are the critical problem | arXiv:2110.06581, arXiv:2605.10719 |
| "A network robust to two CAMELS sub-grid models is robust to the real Universe." | Robustness is input-dependent and fails on a new model outside the training range | arXiv:2609.23982, arXiv:2201.02202 |
| "Cosmology from a single galaxy measures Ω_m to 10%." | Within one simulation model; not robust to the sub-grid physics, with dramatic failures on a fraction of galaxies across codes | arXiv:2201.02202 (abstract), arXiv:2304.06084 |
| "Generative models reproduce the posterior if they match mean and power spectrum." | The variance-field power spectrum can be up to ~30% off while the mean matches | arXiv:2606.10023, Sects. 5.2, 6.1 |
| "PLAsTiCC log-loss 0.468 was the winning score." | That is the flat-weight metric of the Avocado paper; the official weighted metric of the winner was 0.685 | arXiv:1907.04690 (abstract), arXiv:2012.12392 (Fig. 7 caption) |
| "ESR shows the data disfavour the Friedmann equation." | It shows the data do not uniquely prefer it | arXiv:2211.11461 |

## 6. Not verified
<!-- key: not-verified -->

- The FAIR Universe organisers' results paper (announced for NeurIPS 2026
  in arXiv:2604.09621, Sect. 4); only the winning entry and the baselines
  were read.
- Whether any 2025–2026 collaboration headline (DES Y6, KiDS-Legacy, DESI
  DR2, Euclid) used a neural summary or an emulator other than for the
  linear and non-linear matter power spectrum; the siblings record the
  headline likelihoods as explicit.
- Closed 2026-10-16: the KiDS-SBI and DES Y3 (C_ℓ × CNN, hybrid) blinding
  protocols were read; they are summarised in `systematics.md` §6.
- Closed 2026-10-17: the Rubin DP1 transient classification paper
  (arXiv:2507.22864) was read; see §4.
