# Tensions and anomalies — mundane explanations on the table

Scope: for each tension or anomaly, the mundane explanations and the paper that quantifies each.

Snapshot: 2026-10-16

Flags as in `results.md`: `[src]` read this session in the cited paper; `[sec: X]` taken from the reference files of sibling skill X (abbreviations at the top of `results.md`); `[der]` a derivation in words, without a number (no number is computed here, owner's rule of 2026-10-23). Where a row says "ID in sibling", the paper is cited with its arXiv ID in that sibling's files and is not in this skill's `sources.tsv`.

"Mundane" means: an explanation that leaves ΛCDM untouched — a systematic in one data set, an astrophysical nuisance, a statistical choice, or chance. Each row gives the mechanism, the size where a paper quantifies it, and the verdict at the snapshot: **closed** (tested and excluded as the explanation), **open** (quantified, not excluded), or **operative** (shown to have moved the number).

## 1. H0
<!-- key: h0 -->

| Explanation | Size | Verdict | Quantifying paper | Flag |
|---|---|---|---|---|
| Crowding of Cepheids in HST photometry | HST − JWST distance difference −0.01 ± 0.03 mag; crowding as the cause rejected at 8.2σ | closed | Riess et al. 2024, arXiv:2401.04773; no bias in 19 JWST hosts, arXiv:2509.01667 | [src: abstract of each] |
| Calibrator subsample and supernova compilation | CCHP TRGB 70.39 ± 1.22 (stat) ± 1.33 (sys) ± 0.70 (σ_SN) from 24 calibrators, its distances agreeing with SH0ES Cepheids "at just over the 1% level" (arXiv:2408.06153); 72.1 to 73.3 ± 1.8 for the complete 35-calibrator TRGB sample, the difference traced to 11 hosts not selected by CCHP which alone give 74.1, "2σ higher than the selected sample" (arXiv:2504.08921) [src: abstract of each] | open; the gap is in which SNe calibrate, not in the stars | arXiv:2408.06153; Li et al. 2025, arXiv:2504.08921 | [src: abstract] |
| Implicit flat priors on distance moduli | 73.0 ± 1.0 becomes 70.6 ± 1.0 with physically motivated priors on all distances and a conservative Gaia EDR3 offset, "reducing the Hubble tension from 5σ to 2σ" (arXiv:2601.22215) [src: abstract] | closed for the Milky Way step: the uniform-in-volume prior without selection biases the period–luminosity zero point by ∼0.05 mag and mis-predicts the observed parallax, magnitude and period distributions; with the SH0ES selection modelled the period–luminosity parameters agree with SH0ES at < 0.5σ (arXiv:2603.09880) [src: abstract] | arXiv:2601.22215; arXiv:2603.09880 | [src: abstract] |
| Selection of Cepheids and SNe in calibrator galaxies | shifts of −1.4, −0.2 and −1.0 km/s/Mpc from three selection terms, which "when included together ... substantially reduce the inferred tension" | open | Percival 2026, arXiv:2607.22425 | [src: abstract] |
| A single geometric anchor for the JWST ladders | both JWST ladders rest on NGC 4258; excluding Gaia parallaxes and the Magellanic-Cloud eclipsing binaries, so that NGC 4258 anchors both telescopes, SH0ES gets 72.85 ± 1.30, against 73.18 ± 0.88 with all anchors | open until a second JWST anchor exists | arXiv:2509.01667 | [src: Sect. III.2.3] |
| Local void or outflow | the SN Hubble diagram (1295 SNe) gives a 5σ bound |δ| < 27% on scales > 69 h⁻¹Mpc and is inconsistent at 4–5σ with |δ| > 20%; empirical σ_H0 = 0.60% against 0.42% expected from cosmic variance (arXiv:1901.08681) [src: abstract]. Void models fitted to Cosmicflows-4 Tully–Fisher distances prefer a void ≲ 70 Mpc, ≲ 10% of the proposed KBC size; they predict a local H0 of 72.1 (+0.9/−0.8), 70.4 ± 0.4 or 70.2 (+0.5/−0.4) for exponential, Gaussian or Maxwell–Boltzmann profiles, the last two within 3σ of the 4-anchor ladder (73.2 ± 0.9), the first at just over 1σ but disfavoured by the evidence, and the preferred models disagree with the CF4 bulk-flow curve (arXiv:2506.10518) [src: abstract] | closed as the main cause in both papers; a void reduces, does not remove, the gap in the profiles the data prefer | Kenworthy, Scolnic & Riess 2019, arXiv:1901.08681; Stiskalek, Desmond & Banik 2025, arXiv:2506.10518 | [src] |
| Local density from constrained simulations | a large-scale underdensity "at the level of ≈ 5%" in a constrained simulation to 200 Mpc (arXiv:2202.04099) [src: abstract]; "no evidence for a large local underdensity" in Manticore-Local (arXiv:2505.10682) [sec: sims] | closed: neither approaches the required size | SIBELIUS-DARK, arXiv:2202.04099; Manticore-Local, arXiv:2505.10682 | [src: abstract; sec: sims] |
| Lens mass profile (mass-sheet degeneracy) | 73.3 (+1.7/−1.8), 2.4%, from six quads with assumed profiles (Wong et al. 2020, as quoted) becomes 71.6 (+3.9/−3.3) in flat ΛCDM with Pantheon+ and the degeneracy free | operative: lensing no longer discriminates | arXiv:2506.03023 | [src: Introduction, results table] |
| Peculiar velocities of megamaser hosts | 73.9 ± 3.0 without peculiar-velocity corrections (arXiv:2001.09213); in two 2026 reanalyses with Manticore-based flows, a value "consistent with the value from the CMB" (arXiv:2608.06247) and 71.6 ± 3.7 (stat) (arXiv:2609.17684) [src: abstract of each] | operative and unresolved | Pesce et al. 2020, arXiv:2001.09213; Watkins & Feldman 2026, arXiv:2608.06247; Stiskalek & Desmond 2026, arXiv:2609.17684 | [src: abstract] |
| A Planck-specific systematic | SPT-3G D1 alone gives 66.66 ± 0.60 [sec: h0], SPT + ACT 66.59 ± 0.46 with no Planck data, and the SPT TE/EE spectra alone 66.1 ± 1.2 (4.9σ from SH0ES); SPT judges "a systematic error in the CMB data an unlikely explanation" [src: Sect. VII.2.2 of arXiv:2506.20707]; DESI DR2 BAO + BBN gives 68.51 ± 0.58 with no CMB anisotropies [src: Eq. 19 of arXiv:2503.14738] | closed | arXiv:2506.20707; arXiv:2503.14738 | [src] |
| Underestimated errors in general | treating the scatter of 163 published values (1976–2019) as the true error distribution turns a nominal 4.4σ into 2.1σ | a sociological argument, not a measurement | Lopez-Corredoira 2024, arXiv:2411.13621 | [src: abstract] |
| Supernova systematics moving the inverse ladder | known systematics shift it by less than 0.1 km/s/Mpc | closed | Popovic & Sullivan 2026, arXiv:2602.12822 | [src: abstract] |

The gap to close is the "5-sigma difference" of arXiv:2112.04510 [src: abstract]. No single quantified systematic above closes it; the open rows (calibrator selection, extragalactic selection, single anchor) are the ones a referee should ask about.

## 2. S8
<!-- key: s8 -->

| Explanation | Size | Verdict | Quantifying paper | Flag |
|---|---|---|---|---|
| Source redshift calibration | KiDS: 0.759 to 0.815; the Hellinger tension with Planck falls by 2.2σ against the most similar KiDS-1000 analysis, about two thirds of it (1.32σ) from redshift estimation and calibration and the rest from lower noise outside the KiDS-1000 footprint [src: Sect. 6 of arXiv:2503.19441]; HSC Y3: 0.769 to 0.804 with DESI clustering redshifts [sec: wl] | operative; the main driver of the old low values | arXiv:2503.19441; arXiv:2511.18134 | [src; sec: wl] |
| Shear calibration | replacing lensfit by metacalibration on KiDS-1000 gives 0.789 (+0.020/−0.024), consistent with the lensfit 0.776, and leaves the distance to Planck at 1.8σ | closed | Yoon et al. 2025, arXiv:2510.01122 | [src: abstract] |
| Intrinsic-alignment model | 0.798 (NLA) against 0.783 (TATT) on the same DES Y6 data, a 0.6σ difference in the marginal mean; against the CMB the full-space shift is 1.1σ (NLA) or 1.7σ (TATT) [src: Sect. VI.2.1, IX]; the choice of IA and baryon model moves S8 by up to 1σ [sec: wl] | open | arXiv:2602.10065 | [src] |
| IA and baryon priors from external data | DES Y3 moves to 0.832 (+0.013/−0.017), up by 1.5σ, "in closer agreement with the cosmic microwave background", with IA priors from spectroscopic measurements and a baryon model informed by X-ray and kSZ data | open; not adopted by the collaboration | Bigwood et al. 2025, arXiv:2512.04209 | [src: abstract] |
| Baryonic feedback strength | disputed: kSZ, X-ray, tSZ and the KiDS P(k) favour strong suppression, DES Y3 6×2pt weak [sec: wl, x]; KiDS-Legacy cosmic shear itself has its MAP at the lowest prior feedback amplitude, an upper limit log₁₀ T_AGN ≤ 7.71 (8.01) at 68% (95%) with Planck cosmology fixed, and excludes the most extreme FLAMINGO models above k ≈ 1 h/Mpc; P(k)-model differences stay below 10% of its constraining power [src: Sect. 6 of arXiv:2503.19441] | open | IDs in `cosmo-weak-lensing`, `cosmo-cmb-lss-cross-correlations`; arXiv:2503.19441 | [sec: wl, x; src] |
| Projection (prior-volume) effects on the point estimate | mean 0.790 against MAP 0.801 in DES Y3 + KiDS-1000, "owing to skewness in the marginal distribution and projection effects" | operative at the half-σ level | arXiv:2305.17173 | [src: abstract] |
| The CMB reference | Planck S8 0.834 ± 0.016 (PR3) to 0.819 ± 0.014 (PR4); four endpoints in use | operative | arXiv:2309.10034 | [src: Sect. 6, Eq. 17] |
| Metric and subspace | DES Y6 3×2pt: 2.6σ in S8, 2.2σ in S8–Ω_m, 1.8σ in full space; KiDS-Legacy: 0.76σ in S8, 0.73σ in Σ8 | operative | arXiv:2601.14559; arXiv:2503.19441 | [src: Sect. V.2; Sect. 7] |
| Lensing-map normalisation and redshifts in CMB-lensing tomography | the corrected lensing normalisation and the spectroscopic redshift calibration each raised the unWISE S8; unmitigated foregrounds would bias κ × unWISE low (sizes in `cosmo-cmb-lss-cross-correlations`) | operative | arXiv:2309.05659 | [sec: x] |
| Neutrino treatment and projection effects in the LRG analysis | reanalysing the Planck PR3 × DESI LRG cross-correlation: consistent neutrino masses +0.017 (∼0.5σ; the emulators lacked massive neutrinos, ΔS8 ≃ −4f_ν = −0.019 expected), the lensing normalisation correction +0.015, an informative prior on the relation of two nuisance parameters (α_a–α_x, their Eq. 7) that mitigates volume effects +0.014, the updated LRG sample −0.012; together about 1σ, from 0.725 ± 0.030 to 0.762 ± 0.023 | operative | arXiv:2407.04607 | [src: Sect. 7.2, Eq. 15] |
| Cluster mass calibration | Planck clusters at 1.6σ from the CMB with DES shear (arXiv:2509.02068); hydrostatic-bias values depend on the reference, (1 − b) = 0.89 ± 0.04 against Chandra and 0.76 ± 0.04 against XMM-Newton with the same lensing, with identical cosmology (arXiv:2402.04006) [src: abstract of each] | operative | arXiv:2509.02068; arXiv:2402.04006 | [src: abstract] |
| Selection and projection in optical clusters | richness selection biases stacked lensing high by "approximately 20 to 60 percent" on large scales (arXiv:2203.05416); DES Y1 clusters gave 0.65 ± 0.04, the discrepancy placed by the collaboration "in our modeling of the weak lensing signal" (arXiv:2002.11124) [src: abstract of each] | operative | arXiv:2203.05416; arXiv:2002.11124 | [src: abstract] |
| The gas model in tSZ cross-correlations | the same y × galaxy data are fitted with one simulation suite; ⟨b_h P_e⟩ ∝ S8^ε(z) with ε ≈ 3 over 0.1 ≤ z ≤ 1, and feedback boosts ⟨b_h P_e⟩, so the joint fit prefers low S8 with strong feedback (group-mass baryon fraction 0.10 (+0.09/−0.05) of cosmic) [src: abstract] | open | arXiv:2605.11083 | [src: abstract] |
| Prior volume in full-shape fits | low σ8 in the BOSS EFT analyses (values and IDs in `cosmo-galaxy-clustering`) against DESI DR1 full shape σ8 = 0.842 ± 0.034 (arXiv:2411.12022) [src: abstract]; frequentist intervals show no BOSS tension [sec: stat] | operative | arXiv:2411.12022; IDs in `cosmo-galaxy-clustering`, `cosmo-statistics-inference` | [src: abstract; sec] |

The high eRASS1 value (0.86 ± 0.01, arXiv:2402.08458) is the one S8 number for which no mundane downward correction has been published; its companion result, a growth index of 1.19 ± 0.21 (arXiv:2410.09499) [src: abstract of each], shows that the same data prefer less low-redshift growth when given the freedom.

## 3. A_L, tau and the CMB-BAO discrepancy
<!-- key: al-tau-and-the-cmb-bao-discrepancy -->

| Explanation | Size | Verdict | Quantifying paper | Flag |
|---|---|---|---|---|
| A_L: a feature of Planck TT at 1000 < ℓ < 2000, statistical or systematic | Plik PR3 1.180 ± 0.065 (arXiv:1807.06209 [src: Sect. 2.2.1]); CamSpec PR4 1.095 ± 0.056 and ACT DR6 1.007 ± 0.057 (arXiv:2503.14452 [src: Sect. VIII.5]); HiLLiPoP PR4 1.039 ± 0.052 (arXiv:2309.10034 [src: abstract]); SPT + ACT 1.016 (+0.048/−0.054) (arXiv:2506.20707 [src: Sect. VII.2.3]) | operative; ground data do not show the residual | arXiv:1807.06209; arXiv:2309.10034; arXiv:2503.14452; arXiv:2506.20707 | [src: as given in the size cell] |
| A_L: real excess lensing | excluded by the reconstructions: the smoothing is 2σ high relative to the Planck reconstruction (arXiv:1912.06601); the ACT + SPT + Planck reconstruction amplitude is 1.025 ± 0.017 (Qu et al. 2025, arXiv:2504.20038); the SPT-3G D1 amplitude is consistent with unity at 2% (arXiv:2608.31136) | closed | arXiv:1912.06601; arXiv:2504.20038; arXiv:2608.31136 | [src: abstract of each] |
| τ: a systematic in Planck low-ℓ EE | the BAO-preferred τ is about 5σ from Planck low-ℓ EE at face value, about 3.8σ with the prior width [src: note 72 of arXiv:2504.16932]; five reprocessings give 0.051–0.063 [sec: cmb]; ground-based CLASS × Planck gives 0.053 (+0.018/−0.019) (arXiv:2501.11904) [src: abstract] | open but disfavoured; "no evidence for systematics in the large-scale Planck data" by the authors who raised the question | arXiv:2504.16932 | [sec: cmb] |
| τ: reionisation astrophysics | Planck without low-ℓ EE + x_HI(z) from Lyα forest and damping wings at z ∼ 5–14 gives 0.0552 (+0.0019/−0.0026 stat) (+0.0075/−0.0049 sys, absorption modelling), which breaks the τ–Ω_m degeneracy and leaves a 2.4σ tension with DESI DR2 BAO | closes the high-τ door from the astrophysical side, within the absorption-modelling systematic | arXiv:2601.09644 | [src: abstract] |
| CMB–BAO: choice of CMB data | 1.6σ (P-ACT) to 3.7σ (SPT + ACT); ACT with SRoll2 τ 2.8σ, "partly driven by the τ measurement"; DESI's CMB 2.3σ, 2.0σ without CMB lensing | operative; no preferred choice | arXiv:2503.14452; arXiv:2506.20707; arXiv:2503.14738 | [src: App. H; Sect. VII.3; Sect. VI] |
| CMB–BAO: BAO systematics | the systematic error raises the total error on α_iso by 1% (BGS) to 9% (LRG3 + ELG1) and on α_AP by 0.1% (QSO) to 2% in DESI DR2 | closed at the current precision | arXiv:2503.14738 | [src: Sect. III.1] |
| CMB–BAO: lensing reconstruction | with the 2026 SPT-3G D1 lensing (amplitude unity at 2% relative to the CMB-SPA best fit) combined with CMB-SPA and DESI DR2, the "better agreement" with DESI relaxes Σm_ν to < 0.072 eV and reduces the curvature and w0wa preferences to ∼2σ | operative | arXiv:2608.31136 | [src: abstract] |
| CMB–BAO: chance | a 2–3σ difference between two data sets in one model | open; the simplest reading | — | — |

## 4. w0wa preference
<!-- key: w0wa-preference -->

| Explanation | Size | Verdict | Quantifying paper | Flag |
|---|---|---|---|---|
| Supernova photometric calibration and a colour-law implementation error | DES: 4.2σ to 3.2σ | operative | arXiv:2511.07517 | [src: abstract] |
| Inconsistent host masses between low and high redshift | Pantheon+ 2.8σ to 3.2σ; Union3 3.8σ to 3.4σ | operative; moves samples towards each other | arXiv:2601.19424 | [src: abstract] |
| Heterogeneous low-redshift anchor | an intercept offset between the external low-z and the DES supernovae within DESY5; correcting it reduces the preference "to be less than 2σ", with or without the CMB | open | Huang et al. 2025, arXiv:2502.04212 | [src: abstract] |
| Non-independence of the compilations | the samples share most low-redshift supernovae | operative; three samples are not three confirmations | — | [sec: de] |
| A ΛCDM inconsistency between data sets absorbed by two parameters | DESI DR2 against DES-SN5YR in ΛCDM: 2.95 ± 0.04σ, reduced to 1.96 ± 0.04σ with DES-Dovekie [src: abstract; Sect. III]; for DESI DR2 + CMB + supernovae ln B falls from +3.32 ± 0.27 to −0.30 ± 0.19 [src: Table 1] | operative in that analysis | arXiv:2511.10631 | [src: as given] |
| CMB lensing and τ | compressed CMB priors give 2.4σ, the CMB without lensing 2.7σ, the full CMB 3.1σ [src: Table 6 of arXiv:2503.14738]; a τ = 0.09 prior in place of Planck low-ℓ EE leaves Δχ²_MAP = −3.82, 1.4σ, against 2.8σ with τ = 0.06 [src: Sect. III.2 of arXiv:2504.16932] | open | arXiv:2503.14738; arXiv:2504.16932 | [src] |
| Statistic | 2.8σ (arXiv:2503.14738 [src: Table 6]) and ln B = −0.66 ± 0.44 (arXiv:2503.14743 [src: App. A, Table 4]) for the same DESI DR2 + CMB + Pantheon+ data | operative | arXiv:2503.14738; arXiv:2503.14743 | [src: as given] |
| Clustering beyond BAO | the DESI DR1 bispectrum weakens the preference; DESI only is within 1σ of Λ | operative | arXiv:2606.23936 | [sec: de] |
| Parameterisation | phantom crossing is preferred within CPL; in 3.2% of 1,000 mocks drawn from a non-crossing quintessence model, crossing CPL fits better than in the real data | open | Keeley et al. 2025, arXiv:2506.15091 | [src: abstract] |
| Repeated looks at accumulating data | Wilks-based σ read as if the test were done once | open | ID in sibling | [sec: de] |

## 5. Cosmic dipole
<!-- key: cosmic-dipole -->

| Explanation | Size | Verdict | Quantifying paper | Flag |
|---|---|---|---|---|
| Redshift evolution of the source population (spectral index, magnification bias, luminosity function) | the standard expression "may be inaccurate"; luminosity-function models consistent with the data give dipoles that "can disagree by more than 3σ" | disputed: the reply is that the test is "robust to such effects", because α and x need only describe sources near the flux limit; the discovering group's review concludes that "there are thus no 'theoretical systematics'" in the formula (arXiv:2505.23526) [src: Sect. IV.3] | Dalang & Bonvin 2022, arXiv:2111.03616; Guandalin et al. 2023 (abstract read, not in `sources.tsv`); von Hausegger 2024, arXiv:2404.07929 | [src] |
| Clustering dipole of the sources and mode coupling from the mask | 4.9σ becomes 3.63σ (no clustering dipole in the mocks), 3.44σ (random orientation) or 3.27σ (aligned); including an octupole in the fit shifts the dipole and inflates its variance | open; reduces, does not remove | Bashir, Chingangbam & Appleby 2025, arXiv:2511.00822 | [src: abstract] |
| Same, as assessed by the discovering group | after the ecliptic-latitude trend is removed, other large-scale power is consistent with noise, no octupole, clustering dipole "marginal" | disputed | von Hausegger et al. 2025, arXiv:2510.23769 | [src] |
| Mask leakage | the Galactic mask moves dipole power to higher multipoles, which makes the discrepancy worse, not better | closed as an explanation | arXiv:2212.07733 | [src] |
| Survey-specific count gradient (ecliptic latitude in CatWISE) | a "known trend of the quasar number counts with ecliptic latitude", accounted for before the multipole analysis | open as to completeness of the correction | arXiv:2510.23769 | [src] |
| Multi-component radio sources (overdispersed counts) | modelled with a negative-binomial likelihood; the excess remains at 3.67 ± 0.49 times the expectation | closed as an explanation | Böhme et al. 2025, arXiv:2509.16732 | [src: abstract] |
| Position-dependent sensitivity and flux calibration | the review by the discovering group: sensitivity differences (NVSS array configuration at extreme declinations, WISE confusion near the Galactic plane and ecliptic poles) are mitigated by raising the flux cut (≥ 10 mJy for radio) or by a weighting function; the CatWISE amplitude and direction stay stable with flux cut (their Fig. 5); position-dependent calibration errors persist across flux cuts and must be corrected or masked, as likely needed for VLASS below dec −15°; TGSS shows a dipole several times larger than other radio catalogues and is the data point behind the claimed frequency dependence | open as to completeness; stated by one side of the dispute | Secrest et al. 2025, arXiv:2505.23526 | [src: Sect. IV.2.1] |
| Frequency-dependent systematics in radio catalogues | amplitude rising towards low frequency in one four-survey analysis; no frequency dependence in another | open | arXiv:2010.08366; arXiv:2206.05624 | [src] |
| Eddington bias at the flux limit | forward-modelling it raises the CatWISE–Planck tension from ≈ 5.7σ to ≈ 6.7σ | closed as an explanation | Land-Strykowski et al. 2026, arXiv:2607.25703 | [src: abstract] |
| Footprint incompleteness and leakage of large-scale power | the DESI DR1 count dipole is enhanced while the redshift dipole of the quasars gives 357.95 (+55.05/−48.47) km/s | open; shows that a count excess can coexist with a normal velocity in one catalogue | Wu & Xia 2026, arXiv:2608.30914 | [src: abstract] |
| A real flow of the sources | excluded at the amplitude needed: kSZ limits at 200–2000 h⁻¹Mpc are consistent with ΛCDM | closed for a ~370 km/s flow at R ~ 1000 h⁻¹Mpc | arXiv:2605.12499 | [src: abstract] |
| Model-dependent residual | with the kinematic part fixed, the residual points 39° ± 8° away from the CMB dipole | suggests a non-kinematic component with its own direction, as expected for a systematic or a clustering term as much as for new physics [the reading is this file's, not the paper's] | arXiv:2503.02470 | [src: abstract] |

What stays unexplained: two populations with no shared objects (radio galaxies and infrared quasars) both exceed the expectation, with directions near the CMB dipole (arXiv:2206.05624) [src]. What weakens the case: the quoted significance of the single strongest catalogue ranges from 3.27σ (arXiv:2511.00822) to ≈ 6.7σ (arXiv:2607.25703) [src: abstract of each] with the null model, and the two measurements that determine the velocity without counting sources agree with the CMB velocity (arXiv:1303.5087; arXiv:2608.30914) [src: abstract of each].

## 6. Large-angle CMB anomalies
<!-- key: large-angle-cmb-anomalies -->

| Explanation | Size | Verdict | Quantifying paper | Flag |
|---|---|---|---|---|
| A posteriori selection of statistics | the joint ≤ 3 × 10⁻⁸ becomes 3σ for about 16 tests considered and 2σ for about 50 | operative; the authors list that many published tests | Guth & Namjoo 2026, arXiv:2602.10178 | [src: abstract] |
| Non-independence of the statistics | hemispherical-asymmetry and dipole-modulation statistics "cannot be considered to be independent of each other" | operative | arXiv:1906.02552 | [src] |
| Chance, tested with polarisation | about a 30% chance that a p-value dip deepens when isotropic polarisation is added; no polarisation counterpart found | open; Planck polarisation is not sensitive enough | arXiv:1906.02552 | [src: Conclusions] |
| Instrumental or processing artefact | present in WMAP and Planck and in PR3 and PR4; the lack-of-power probability does change with release (≤ 0.33% to ≤ 1.76%) | closed for the existence of the features, open for the exact p-values | arXiv:1510.07929; arXiv:2312.09989; arXiv:2406.11543 | [src: abstract of each] |
| Secondary anisotropies from the local Universe | thermal and kinetic SZ from a constrained simulation of the local 500 h⁻¹Mpc box have negligible impact on lack of correlation, quadrupole–octopole alignment and hemispherical asymmetry | closed | Jung et al. 2024, arXiv:2406.11543 | [src: abstract] |
| Cold Spot: a supervoid along the line of sight | the Planck lensing signal disfavours a void large enough, with odds 1:13 to 1:20 | closed | Owusu et al. 2023, arXiv:2211.16139 | [src: abstract] |
| Cold Spot: the Eridanus supervoid through ΛCDM ISW | accounts for about 10–20% of the temperature depression | closed as the full explanation | Kovács et al. 2022, arXiv:2112.07699 | [src: abstract] |
| Mask and component separation | p-values quoted as upper bounds over four component-separated maps | operative at the factor-of-few level in p | arXiv:2312.09989 | [src] |

The mundane explanation that cannot be excluded is cosmic variance: one sky, a handful of modes, statistics chosen after the fact. The only new information can come from large-angle polarisation and from three-dimensional tracers of the same modes.

## 7. Bulk flow
<!-- key: bulk-flow -->

All rows [sec: pv]; IDs for papers not listed in `results.md` §8 are in `cosmo-peculiar-velocities`.

| Explanation | Size | Verdict |
|---|---|---|
| Analytic minimum-variance errors underestimate the uncertainty | CF4 at 150–200 h⁻¹Mpc: errors of 28 and 36 km/s analytic (arXiv:2302.02028 [src: Sect. 7, Table 1]) against 108 km/s from mocks (arXiv:2306.11269 [src: abstract]); probability 0.00021% (arXiv:2302.02028 [src: Table 1]) to 0.11% (arXiv:2306.11269 [src: abstract]) | operative (arXiv:2302.02028; arXiv:2306.11269) |
| Window: an ideal sphere reconstructed from a sparse, anisotropic catalogue | full-range dipole deviation 2.29σ when the ΛCDM prediction is computed for the actual positions and covariances [src: abstract] | operative (arXiv:2608.14265) |
| One sub-catalogue: 6dFGS Fundamental Plane | peak-bin deviation 3.40σ, 1.56σ without 6dFGS, 3.77σ without SNe, yet the SN and 6dFGS dipoles agree within their covariance [src: abstract] | open (arXiv:2608.14265) |
| Zero-point (monopole) error leaking into the dipole | a zero-point dipole of 0.087 ± 0.019 mag in CF4 Tully–Fisher is better described by local flow structure [src: abstract] | operative (arXiv:2509.14997) |
| Neglected relativistic terms of order vz | bias "toward larger values by ∼10%" (Heinesen 2023, arXiv:2305.16084) [src: abstract] | operative, small |

## 8. JWST abundance
<!-- key: jwst-abundance -->

| Explanation | Size | Verdict | Quantifying paper | Flag |
|---|---|---|---|---|
| Photometric redshifts and masses of the first candidates | the 2022 claim was conditional: "if verified with spectroscopy" | operative: the spectroscopic FRESCO sample shows "no tension with the ΛCDM model" | arXiv:2207.12446; arXiv:2309.02492 | [src] |
| Slitless-grism redshift contamination | one of three ultra-massive objects moves from z = 5.58 to 3.2439 and from an extreme efficiency to log M_* ~ 10.6 | operative for that object | Xiao et al. 2026, arXiv:2602.03030 | [src: abstract] |
| AGN light, dust, and the lack of rest-frame near-infrared (MIRI) constraints in the stellar masses | named as the likely drivers of "earlier claims of insufficient stellar masses at z = 8" | operative according to that model comparison | Prada et al. 2026, arXiv:2604.18683 | [src] |
| Star-formation efficiency higher at early times | 2–3% of baryons converted by z = 10–12 suffices for the UV luminosity functions at 7 ≤ z ≤ 14; the three ultra-massive FRESCO galaxies would need about 50% | open as galaxy-formation physics, not as cosmology | arXiv:2604.18683; arXiv:2309.02492 | [src: abstract of each] |
| Cosmic variance of small fields, initial mass function, bursty star formation | not quantified in the papers read | open | — | — |

## 9. Tension-metric pitfalls
<!-- key: tension-metric-pitfalls -->

Worked cases. Each row is one data situation where two defensible computations give different answers.

| Pitfall | Case | The two numbers | Source | Flag |
|---|---|---|---|---|
| Unnamed reference endpoint | H0, H0DN 2025 | 5.0σ against DESI DR2 + BBN; 7.1σ against Planck + SPT + ACT | arXiv:2510.23823 | [src: abstract] |
| Unnamed reference endpoint | CMB against DESI DR2 in ΛCDM | 1.6σ (P-ACT), 2.3σ (DESI's CMB), 2.8σ (CMB-SPA), 3.7σ (SPT + ACT) | arXiv:2503.14452; arXiv:2503.14738; arXiv:2506.20707 | [src: abstract of each; Sect. VII.3 of arXiv:2506.20707 for 3.7σ] |
| Projection on the most discrepant parameter | DES Y6 3×2pt against the CMB | 2.6σ in S8; 1.8σ in the full shared space | arXiv:2601.14559 | [src: abstract] |
| Choosing the data combination after the fact | LSS against Planck 2015 | 2.55σ for the most discrepant combination; 0.76σ for the most concordant | Charnock, Battye & Moss 2017, arXiv:1703.05959 | [src: abstract] |
| Prior-volume dependence of the evidence ratio | two equal Gaussians 3σ apart | R << 1 with a flat prior on [−10, 10]; R > 1 with [−200, 200] | Lemos et al. 2021, arXiv:2012.09554 | [sec: stat] |
| Frequentist preference against Bayesian evidence | DESI DR2 + CMB + Pantheon+ | 2.8σ for w0wa (arXiv:2503.14738 [src: Table 6]); ln B = −0.66 ± 0.44, mildly for Λ (arXiv:2503.14743 [src: App. A, Table 4]) | arXiv:2503.14738; arXiv:2503.14743 | [src: as given] |
| Two evidence calculations on nominally the same data | DESI DR2 + CMB + DES-Dovekie | odds about 5:1 for w0wa; ln B = −0.30 ± 0.19 | arXiv:2511.07517; arXiv:2511.10631 | [src: abstract of each] |
| Combining data sets that disagree in the base model | DESI DR2 + DES-SN5YR | a 2.95σ ΛCDM tension between them is what the two extra parameters absorb | arXiv:2511.10631 | [src: abstract] |
| Counting correlated data as independent | three supernova compilations with a common low-z sample | 2.8, 3.8, 4.2σ before two fixes; 3.2, 3.4, 3.4σ after | arXiv:2503.14738; arXiv:2601.19424 | [src: abstract of each] |
| Local significance without a trial factor | four CMB anomaly statistics | joint p ≤ 3 × 10⁻⁸ (above 5σ); 3σ if chosen from 16 tests, 2σ from 50 | arXiv:2310.12859; arXiv:2602.10178 | [src: abstract of each] |
| Null model without the nuisance signal | CatWISE dipole | 4.9σ against mocks with shot noise and the kinematic dipole; 3.63σ, 3.44σ or 3.27σ (by clustering dipole) against mocks with clustering, radial selection and the exact mask | arXiv:2009.14826; arXiv:2511.00822 | [src: abstract of each] |
| Analytic errors against mock-calibrated errors | CF4 bulk flow | probability 0.00021%; 0.11% | arXiv:2302.02028; arXiv:2306.11269 | [src: Table 1 of arXiv:2302.02028; abstract of arXiv:2306.11269] |
| Mock covariance that lacks the data's higher-order moments | parity-odd 4PCF in BOSS | 7.1σ against Patchy mocks; 0–2.5σ with statistics free of the 8PCF bias | arXiv:2206.03625; arXiv:2407.03397 | [src: abstract of each] |
| One-sided against two-sided conversion | CatWISE dipole | p = 5 × 10⁻⁷ is quoted as 4.9σ, a one-sided conversion; a two-sided conversion of the same p gives a different σ, so the convention must be named | arXiv:2009.14826 | [src: abstract; Sect. IV] |
| Three metrics on one tension | effective Σm_ν from DESI DR2 + CMB against the oscillation minimum | 2.7σ goodness-of-fit loss, 3.0σ probability to exceed, 4.0σ parameter shift | arXiv:2503.14744 | [src: Table 4] |
| Posterior width at a physical boundary read as sensitivity | Σm_ν from DESI DR2 + CMB | marginalised σ = 0.020 eV with the 95% limit 0.0642 eV (posterior truncated at zero) against a 95% Feldman–Cousins upper limit of 0.053 eV after "correcting for the physical boundary at zero mass" | arXiv:2503.14744 | [src: abstract] |
| Bayesian limit against profile likelihood in a model with a parameter that vanishes at the ΛCDM point | early dark energy | f_EDE < 0.070 at 95% (posterior, SPT + ACT + Planck); f_EDE = 0.09 ± 0.03 and H0 = 71.0 ± 1.1 (profile, ACT DR6 + DESI DR2) | Khalife et al. 2025, arXiv:2507.23355; Poulin et al. 2025, arXiv:2505.08051 | [src: abstract of each] |
| Comparing the wrong quantity | ladder against CMB + BAO + SN | the H0 World Cup quotes the residual discrepancy in the calibrated supernova absolute magnitude M_B, with a parameter-shift statistic and a Gaussian approximation, not in H0 | arXiv:2607.13283 | [src: Fig. 2] |

General rules are in `physics-and-methods.md` Sect. 1.3; the statistical theory is in `cosmo-statistics-inference`.

## 10. What a referee checks
<!-- key: what-a-referee-checks -->

For any sentence of the form "X is in n σ tension with Y":

1. Are both data sets, with release and likelihood, named? (Planck PR3 or PR4; P-ACT or CMB-SPA; DESI DR1 or DR2; which supernova sample and calibration.)
2. Is the model stated? Every number in `results.md` is a ΛCDM statement unless marked.
3. Is the metric stated, and is it a tension between data sets or a preference between models?
4. Is it projected on one parameter or computed in the shared space? Was the parameter chosen before looking?
5. Are the two data sets independent? Check anchors, calibration, τ prior, shared supernovae, shared sky, shared mocks.
6. Is the value current? Check `results.md` Sect. 12 for what superseded it.
7. For an anomaly: was the statistic defined before the data; how many comparable statistics were tried; were the simulations of the null realistic (clustering, mask, selection, noise)?
8. For a combined constraint in an extended model: were the data sets consistent in ΛCDM before being combined, and does the extension do anything other than absorb that inconsistency?
9. Is a mundane explanation that moved the number in the past (redshift calibration, mass calibration, supernova calibration, mock realism, mass-sheet degeneracy) addressed for the new claim?
10. For a proposed resolution: does it survive BAO (Ω_m), uncalibrated supernovae (shape), ACT DR6 (damping tail), S8 and BBN at once (`open-questions.md` §2)?

## Not verified
<!-- key: not-verified -->

- Galactic extinction, stellar contamination and photometric zero-point gradients as explanations of the CatWISE dipole: not quantified in the papers read; the Colloquium review (arXiv:2505.23526) was read for flux calibration and the clustering-dipole summary only (Sect. IV.2.1, IV.3).
- The size of cosmic-variance and initial-mass-function effects on the JWST number densities.
- Whether the −1.4, −0.2, −1.0 km/s/Mpc selection shifts of the 2026 ladder reanalysis (arXiv:2607.22425) [src: abstract] add linearly; the abstract says only that together they "substantially reduce the inferred tension".
- The shift of the Unite w0wa preference when the lowest-redshift supernovae are cut (a value was given in an earlier version of this file, arXiv:2609.05053): not located in the paper in this pass.
- The sizes of the unWISE lensing-normalisation and redshift corrections (arXiv:2309.05659) and the SH0ES 2022 magnitude offset (arXiv:2112.04510): the HTML rendering of both papers was not readable in this pass.
