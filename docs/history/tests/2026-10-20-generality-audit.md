# Generality audit — 2026-10-20

Roadmap §6.3, five steps. One agent, read-only on `skills/`, `docs/plans/`
and `README.md`; this file is the only write. The working tree was measured
as it stood on 2026-10-20, including the uncommitted wave-2 additions of
another session (three new PV dossiers, multimessenger and neutrinos-DM
files). Tags: **[M]** = measured by a command run this session (method
given); **[J]** = judgement of the auditor. Research budget used: 22 calls
(5 arXiv searches, 4 arXiv API requests for author lists, 13 paper reads,
several from the local cache), listed in steps 1, 2 and 4.

## Summary verdict

**Mostly general, with listed tilts.** The 28 domains cover the field's
structure as the community documents set it out; two areas are missing
(alternative Hubble-diagram probes, the cosmological principle). The tilts
are in the hub (its digest and worked examples favour PV and Lyα P1D), in the
depth of the owner's three domains (ranks 3, 4 and 8 of 28 by reference
words, against 16–21 for weak lensing, SNe, CMB and galaxy clustering), and
in how `flip` and two of the owner's papers are presented in PV, Lyα and
beyond-two-point. No machine paths, no personal voice.

## Step 1 — Domain list against the field

### Documents read (section structure)

| Document | What was read | Body size [M] |
|---|---|---|
| CosmoVerse white paper, arXiv:2504.01669 | full outline; words per section, §§1–5 | 180.7k words |
| Snowmass Cosmic Frontier report, arXiv:2211.09978 | outline, §§1–8 | 26.4k |
| Snowmass CF04 report (modern Universe), arXiv:2209.08049 | outline, §§1–9 | 24.4k |
| Snowmass CF05 report (cosmic dawn and before), arXiv:2209.08265 | outline, §§1–6 | — |
| Snowmass CF06 report (complementarity, facilities), arXiv:2209.08654 | outline, §§1–7 | — |
| Weinberg et al. 2013, arXiv:1201.2434 (old, used for the probe structure) | outline; words per section, §§1–9 | 125.7k |
| Huterer 2023 growth review, arXiv:2212.05003 | outline; words per section, §3 | 6.6k in §3 |

Method [M]: `fetch_paper.py <id> --outline`, then a scratch script that parses
the cached HTML with `fetch_paper.parse` and sums words under each heading,
and a second one that counts paragraphs matching topic patterns (crude:
regexes, references excluded). "Mean share" below averages three families
(CosmoVerse; the four Snowmass reports pooled; Weinberg + Huterer pooled).

### Mapping of sections onto the 28 skills

| Skill | Sections that hold the topic | Mean share of paragraphs [M] |
|---|---|---|
| cmb | CV 2.1.18, 2.3.1, 2.3.3; CF 4.1, 4.4; CF05 2.2.1; W13 2.3–2.4 | 15.8% |
| galaxy-clustering | CV 2.1.19, 2.2.3; W13 4, 7.2, 7.3; H23 3.1 | 11.8% |
| dark-energy-modified-gravity | CV 2.3.4, 4.2, 4.3; CF 3; CF04 2 | 8.7% |
| neutrinos-dark-matter | CV 2.3.5, 4.4; CF 5, 6.1 | 8.4% (inflated by "dark matter") |
| supernovae | CV 2.1.7, 2.1.9; W13 3; CF04 4.2 | 8.2% |
| inflation-primordial | CF 4; CF05 2; CV 4.5.3 | 7.5% |
| multimessenger | CV 2.1.17, 2.3.12, 5.1.4, 5.1.8; CF 3.3, 7.3; CF06 7 | 4.7% |
| clusters | CV 2.2.2; W13 6; H23 3.4 | 4.4% |
| weak-lensing | CV 2.2.1; W13 5 (largest W13 probe section, 27.7k words); H23 3.2–3.3 | 4.1% |
| simulations-mocks | CV 3.5 | 3.5% |
| reionization-21cm | CV 5.1.5, 5.1.9; CF05 4.2.1–4.2.2; CF06 6.2–6.3 | 3.3% |
| distance-ladder-h0 | CV 2.1.1–2.1.14 (31.7k words); W13 7.1 | 3.1% |
| early-universe-exotica | CF05 3; CV 4.1, 4.5.2, 4.8 | 2.7% |
| cmb-lss-cross-correlations | CV 2.2.3.a, 2.3.9; W13 7.8–7.9; CF06 5.1 | 2.6% |
| statistics-inference | CV 3.1, 3.6 | 2.6% |
| photometry-photoz | CV 2.2.1.b; CF04 4.3; W13 5.4.3 | 2.0% |
| peculiar-velocities | CV 2.1.12, 2.3.6.k, 2.3.14; H23 3.5 (1219 words, the largest §3 subsection); no W13 section | 1.8% |
| beyond-two-point | CV 2.3.11 (voids, 937 words); W13 5.2.8 | 1.5% |
| lyman-alpha | CV 2.3.8 (1032 words), 3.5.4.b; W13 7.6 (1010 words) | 1.5% |
| bbn | CV 2.3.7 (1409 words) | 1.0% |
| machine-learning | CV 3.2, 3.4 | 0.6% |
| cosmic-web | CV 2.3.9.a, g, h (superclusters) | 0.5% |
| galaxy-halo-connection | W13 4.3.2 (bias) only | 0.3% |
| surveys-facilities, data-pipelines, software-ecosystem, theory-foundations, tensions-anomalies | infrastructure or synthesis: CF04 3, 5–8; CF06 3–6; CV 3.1.5; W13 2; H23 2; CV 1–2 as a whole | — |

### Missing domains

1. **Alternative Hubble-diagram probes** [M]. CosmoVerse gives HII galaxies
   (2.1.10, 1076 words), quasars (2.1.15, 1140) and GRBs (2.1.16, 1606) their
   own sections (3822 words, 2.1% of the paper); Weinberg adds galaxy ages
   (7.11) and redshift drift (7.12). Package: 0 lines mention Risaliti, Lusso
   or a quasar Hubble diagram; 0 HII galaxies; GRBs only as GW counterparts;
   redshift drift 2 lines. Cosmic chronometers are covered (16 lines, mostly
   in distance-ladder-h0). The hub's `moresco2022` row (arXiv:2201.07241,
   "emerging probes") is cited in beyond-two-point only.
2. **Cosmological principle and inhomogeneous models** [M]. CosmoVerse 4.6
   (4969 words) and 4.5.1 (local void, 2147). Package: "cosmological
   principle / isotropy test" 5 lines, backreaction/LTB/timescape 5, local
   void/KBC 6; the dipole side sits in tensions-anomalies.
3. **Strong lensing as a probe** [J]. W13 7.10, CV 2.1.14. Present in 27 files
   (58 lines [M]) across distance-ladder-h0, neutrinos-dark-matter (one
   dossier), multimessenger; no router line names galaxy-scale strong-lens
   statistics. A router line may be enough.
4. **Out of scope by choice** [J]: laboratory dark-matter searches (43% of
   arXiv:2211.09978, §5) and high-energy particles (§§6.2, 7.2). The README
   does not state this boundary.

### Over-split or overlapping domains [J, with counts M]

- **Voids** are held in three places: beyond-two-point (3 of 10 subtopics, 3
  of 6 dossiers), cosmic-web (`voids-structures`), lyman-alpha
  (`tomography-voids`). All seven documents give voids one section or less
  (37 void paragraphs against 31 bispectrum paragraphs [M]); the package has
  660 void lines against 337 bispectrum lines [M], and no bispectrum dossier.
- **Field-level inference**: 252 lines in 13 skills, dossiers in
  beyond-two-point, peculiar-velocities and lyman-alpha [M]; 1 paragraph in
  all seven documents [M]. An emerging topic (a review exists, arXiv:2509.13435);
  one home would suffice.
- **SBI / ML / statistics**: CosmoVerse treats them as one chapter (§3,
  27.0k words); the package has three skills plus SBI dossiers in
  beyond-two-point and lyman-alpha. Overlap rather than over-split.
- Peculiar velocities and Lyα as separate domains are defensible: H23 gives
  cosmic velocities a section equal to clustering, shear and clusters; Lyα is
  a separate DESI data product.

### Names or scopes that reflect a niche [M for text, J for verdict]

- beyond-two-point trigger description lists "Lyα tomography voids" and
  "field-level inference (BORG, LEFTfield, flip)".
- lyman-alpha trigger description lists "Lyα tomography and void
  cross-correlation"; the void–forest measurement is one paper by the owner
  (arXiv:2203.11045).
- peculiar-velocities router line ends "survey descriptions and the fσ8
  table", pointing to two files that only this domain has (step 3).

## Step 2 — Subtopic lists

Method [M]: scratch script over all 28 `subtopics.tsv`. A row is
**R** if its `from` names a review/white paper/roadmap, or cites an id whose
`sources.tsv` role is `review`, or names a review row's first author and year;
**C** if it cites only collaboration or working-group papers; **P** otherwise.

| Result | Rows |
|---|---|
| R review-backed | 254 of 319 (80%) |
| C collaboration / WG papers only | 59 |
| P individual papers only | 6 (cosmic-web 3 and data-pipelines 2 are method-comparison or pipeline papers: Libeskind 2018, Guy 2023, Bosch 2018; software-ecosystem 1) |

Per owner-near domain [M]: peculiar-velocities 11 R / 1 C (Turner 2024,
arXiv:2411.19484, and Tsagas 2025, arXiv:2510.05340); lyman-alpha 5 R / 6 C;
galaxy-clustering 7 R / 5 C; beyond-two-point 5 R / 5 C. Lowest R fractions:
data-pipelines 1/11, lyman-alpha 5/11, beyond-two-point 5/10.

Flags:
- **lyman-alpha `tomography-voids`** [M]: `from` = "Tomography survey groups
  (CLAMATO, arXiv:1710.02894; Stripe 82 eBOSS map, arXiv:2004.01448)" — one
  of two sources is the owner's paper, and no review is cited.
- **lyman-alpha anchor review** [M]: the only recent review cited,
  arXiv:2605.22489, is a machine-learning book chapter (outline: §0.4 data
  reduction = continuum fitting and Voigt decomposition; §0.6 inference).
  `p1d-estimation` cites its "Sect. 0.4", which contains no estimator
  section; the rest of that row is the DESI P1D papers (arXiv:2505.09493,
  first author the owner, and arXiv:2505.07974). McQuinn 2016
  (arXiv:1512.00086) is in `sources.tsv` as a review but in no `from`.
- **galaxy-clustering** [M]: 5 systematics subtopics come from one paper,
  DESI 2024 II (arXiv:2411.12020). One collaboration's list [J: acceptable
  as a working-group list, but no BOSS/eBOSS or Euclid list beside it].
- **software-ecosystem `differentiable-field-level-codes`** [M]: names flip
  first; neither cited source names it (`fetch_paper.py 2605.23839 --grep flip`:
  0 paragraphs; the Snowmass CompF paper arXiv:2203.07347 predates flip).
- PV subtopics are review-backed: Turner 2024 has §5.1–5.4 matching
  `bulk-flows`, `two-point-statistics`, `velocity-density-comparison`,
  `field-level-likelihood` [M, outline read].

## Step 3 — Depth against the owner's areas

Method [M]: scratch `depth.py`: `sources.tsv` rows; occurrences of `[src`
(both `[src]` and `[src: …]`) in `references/*.md` + `deep/*.md`; dossier
count and lines; words (`split()`) in `references/*.md` and in `deep/*.md`;
`arXiv:` citations in references, deep and SKILL.md.

| Skill | Rows | [src flags | Dossier lines | Ref words | Rank (ref words) |
|---|---|---|---|---|---|
| simulations-mocks | 245 | 816 | 2505 | 33,736 | 1 |
| statistics-inference | 134 | 768 | 1959 | 30,427 | 2 |
| **lyman-alpha** | 202 | **939 (1st)** | 2228 | **29,740** | **3** |
| **peculiar-velocities** | 166 | 770 | 1983 | **28,103** | **4** |
| neutrinos-dark-matter | 148 | 853 | 2344 | 27,653 | 5 |
| theory-foundations | 123 | 587 | 1978 | 26,217 | 6 |
| tensions-anomalies | 141 | 660 | 2625 | 25,432 | 7 |
| **beyond-two-point** | 237 (3rd) | 649 | 2131 | 25,271 | **8** |
| inflation-primordial | 155 | 683 | 2367 | 24,224 | 9 |
| reionization-21cm | 214 | 864 | 2223 | 24,224 | 10 |
| software-ecosystem | 120 | 640 | 2284 | 23,979 | 11 |
| cmb-lss-cross-correlations | 181 | 834 | 2289 | 23,421 | 12 |
| dark-energy-modified-gravity | 155 | 823 | 2208 | 22,146 | 13 |
| clusters | 138 | 822 | 2250 | 21,455 | 14 |
| multimessenger | 169 | 647 | 2189 | 21,197 | 15 |
| weak-lensing | 239 | 930 | 2030 | 20,853 | 16 |
| distance-ladder-h0 | 144 | 855 | 2139 | 19,972 | 17 |
| supernovae | 169 | 763 | 2333 | 19,911 | 18 |
| cmb | 131 | 845 | 2321 | 19,822 | 19 |
| surveys-facilities | 142 | 754 | 2332 | 19,087 | 20 |
| **galaxy-clustering** | 163 | 717 | 2155 | **17,796** | **21** |
| galaxy-halo-connection | 139 | 766 | 2245 | 16,844 | 22 |
| machine-learning | 134 | 797 | 2037 | 16,740 | 23 |
| photometry-photoz | 123 | 771 | 2347 | 14,783 | 24 |
| early-universe-exotica | 114 | 783 | 2241 | 13,834 | 25 |
| cosmic-web | 120 | 761 | 2430 | 13,588 | 26 |
| data-pipelines | 117 | 810 | 2411 | 12,108 | 27 |
| bbn | 102 | 721 | 2193 | 11,127 | 28 |
| median | 143 | — | 2243 | 21,326 | — |

Every skill has six dossiers (1,959–2,625 lines); deep words are flat
(18.7k–24.6k). Depth differences sit in `references/`.

Field weight against depth [M for numbers; ratio = share of package
reference words ÷ mean paragraph share in the documents]:

| Skill | Share of ref words | Field share | Ratio |
|---|---|---|---|
| lyman-alpha | 4.9% | 1.5% | 3.3 |
| beyond-two-point | 4.2% | 1.5% | 2.8 |
| peculiar-velocities | 4.7% | 1.8% | 2.6 |
| cosmic-web (control, not owner) | 2.3% | 0.5% | 4.6 |
| bbn (control) | 1.8% | 1.0% | 1.8 |
| weak-lensing | 3.5% | 4.1% (22% in W13) | 0.85 |
| supernovae | 3.3% | 8.2% | 0.40 |
| galaxy-clustering | 2.9% | 11.8% | 0.25 |
| cmb | 3.3% | 15.8% | 0.21 |

Findings:
- **[M] PV is the only skill with seven reference files**: `pv-surveys.md`
  (3,910 words) and `fsigma8-pv-compilation.md` (2,820), compiled
  2026-08-13/14 for the early hub, kept "author-vetted" and untouched since
  (gate-log, 2026-10-08 and 2026-10-19 entries). They are 24% of its
  reference words.
- **[J] Owner areas too deep relative to the major probes.** The equal
  template (six dossiers each) already favours small topics, and cosmic web
  shows that this is not owner-specific. But among probe skills the owner's
  three are the deepest by reference words and Lyα has the most `[src`
  flags, while the two probes the documents weigh most for late-time
  cosmology are near the bottom.
- **[J] Galaxy clustering and CMB too thin.** Galaxy clustering: rank 21 of 28
  in reference words, 5 systematics subtopics from one paper, no dossier on
  RSD modelling as such; CMB: rank 19.
- **[M] Inside skills.** lyman-alpha: 260 P1D lines against 190 BAO lines,
  two P1D dossiers, no dossier on 3D/BAO modelling (gate-log shows dossiers
  were chosen by an L2-gap audit, which explains it). The documents give Lyα
  BAO 21 paragraphs and P1D 11 [M]. beyond-two-point: 414 void lines against
  80 bispectrum lines; 3 void dossiers, 0 bispectrum dossiers.

## Step 4 — Within-skill balance

Method [M]: scratch `cites.py` counts `arXiv:<id>` occurrences in
`references/*.md` + `deep/*.md`, maps ids to `sources.tsv` first_author;
author lists of all 1,233 rows of the seven domains fetched from the arXiv
API (4 requests) to find the owner on author lists. "Small team" = 15
authors or fewer.

### Top ten cited papers (citations, share of the skill's citations)

| Skill (citations) | Top ten |
|---|---|
| peculiar-velocities (1070) | Lai 2025 2512.03229 61 (5.7%); Turner 2025 2512.03230 45; Qin 2025 2512.03231 44; Howlett 2022 2201.03112 38; Carrick 2015 1504.04627 34; Ross 2025 2512.03226 32; Stiskalek 2025 2509.20235 31; Carreres 2023 2303.01198 29; **Ravoux 2025 2501.16852 25**; Dixon 2026 2606.14962 24 |
| lyman-alpha (1396) | Chaves-Montero 2026 2601.21432 73 (5.2%); DESI 2025 2503.14739 55; DESI 2026 2607.27410 39; Busca 2025 2506.15262 32; DESI 2024 2404.03001 32; Karaçaylı 2025 2505.07974 32; **Ravoux 2020 2004.01448 32**; Fernandez 2024 2309.03943 31; **Ravoux 2025 2505.09493 31**; Karaçaylı 2025 2509.13593 28 |
| galaxy-clustering (913) | Adame 2024 2411.12021 80 (8.8%); DESI 2025 2503.14738 58; DESI 2024 2404.03000 40; Andrade 2025 2503.14742 32; Bianchi 2024 2411.12025 32; Chaussidon 2024 2411.17623 31; DESI 2024 2404.03002 28; Paillas 2024 2404.03005 24; Chen 2024 2402.14070 22; DESI 2024 2411.12020 21 |
| beyond-two-point (1247) | Beyond-2pt 2024 2405.02252 86 (6.9%); Contarini 2022 2212.03873 47; Williamson 2026 2606.11309 42; Woodfinden 2022 2205.06258 30; Hamaus 2020 2007.07895 30; Liu 2025 2501.01698 30; Contarini 2022 2205.11525 26; Paillas 2023 2309.16541 23; Jeffrey 2024 2403.02314 23; Sartori 2024 2412.02761 22 |
| weak-lensing (control, 1163) | Wright 2025 2503.19441 77 (6.6%); DES 2026 2601.14559 61; DES 2026 2602.10065 47; Li 2023 2304.00702 37; Asgari 2020 2007.15633 34; Amon 2021 2105.13543 25; Giannini 2026 2601.15175 24; Yamamoto 2025 2501.05665 23; Dalal 2023 2304.00701 20; Bigwood 2025 2512.04209 18 |
| cmb (control, 1006) | Camphuis 2025 2506.20707 116 (11.5%); Louis 2025 2503.14452 75; Planck 2019 1907.12875 65; Qu 2023 2304.05202 52; Omori 2026 2608.31136 51; Tristram 2023 2309.10034 44; Planck 2018 1807.06209 37; Calabrese 2025 2503.14454 36; Pagano 2019 1908.09856 26; Naess 2025 2503.14451 23 |
| supernovae (control, 1000) | Camilleri 2026 2609.05053 94 (9.4%); Popovic 2025 2511.07517 67; Vincenzi 2024 2401.02945 65; Rubin 2023 2311.12098 55; Brout 2022 2202.04077 37; Popovic 2025 2506.05471 37; Kessler 2025 2506.04402 27; Mitra 2025 2512.06319 26; Popovic 2021 2112.04456 24; Kessler 2018 1811.02379 22 |

No single paper exceeds 6% in the owner-near skills (controls: up to 11.5%).
Collaboration concentration [M]: DESI-collaboration first authors 18.6% of
galaxy-clustering citations, 9.5% of lyman-alpha; Planck 15.7% of cmb.

### The owner's share [M]

| Skill | Owner first author: rows, citations | Owner on any author list | Owner rank among individuals (small-team citations) |
|---|---|---|---|
| peculiar-velocities | 2 rows, 47 (4.4%) | 7 rows, 6.9% | 25 of 281 |
| lyman-alpha | 4 rows, 79 (5.7%; 4th first author) | 42 rows, 48.6% (DESI papers) | **4 of 312** (6.2%) |
| beyond-two-point | 5 rows, 21 (1.7%) | 5 rows | 62 of 404 |
| galaxy-clustering | 0 | 15 rows, 30.9% (DESI papers) | not ranked |
| software-ecosystem | 1 row, 8 (1.0%) | — | — |
| weak-lensing, cmb, supernovae | 0, 0, 1 (0.1%) | 0, 2, 3 rows | — |

Dossier level [M]: the owner's paper is the most cited in
`lyman-alpha/deep/tomography-voids.md` (23 of 83, 27.7%; CLAMATO 16) and in
`lyman-alpha/deep/p1d-estimation.md` (21 of 81, 25.9%, beside the two QMLE
papers 19 and 16 — balanced); the owner's two papers are 2nd and 3rd in
`peculiar-velocities/deep/field-level-likelihood.md` (17 + 10 of 79, 34%;
the simulation forecast arXiv:2609.34508 outranks every DESI paper but Lai
2025). `supernova-velocities.md`: Carreres 2023 first (18 of 77); the owner
is not on its arXiv author list.

### "Default" phrasing [M: grep for "the standard", "the default", "by default",
"recommended", "preferred", "state of the art" near flip / field-level /
FFT / tomography / voids in seven skills]

No sentence presents an owner method as the default. Framing that does
privilege it, found by reading the flip and surname contexts:

1. `cosmo-supernovae/references/physics-and-methods.md:394–396`: "the
   likelihood framework for that is the one of Ravoux et al. 2025" —
   privileged: one framework presented as the framework.
2. `cosmo-peculiar-velocities/references/physics-and-methods.md:23`: the
   log-distance ratio η, a quantity older than the paper, is defined with a
   citation to arXiv:2501.16852 first; Johnson et al. 2014 follows.
3. same file, lines 60–61, 135, 157: two of six velocity estimators are
   labelled "(flip)"; "The flip framework … writes any model as"; "Named
   covariance models (as flip labels them)", including the owner's RC25.
   The general formalism is presented through one code.
4. `cosmo-beyond-two-point/references/physics-and-methods.md:467–469`: the
   Gaussian field-level likelihood is "what `flip` implements"; the method
   (Johnson 2014, Adams & Blake 2017/2020, Lai 2023) is attributed through
   the code. `results.md` §5.4 is titled "Gaussian field-level likelihood
   (flip)" and holds only the owner's forecast and Fisher result.
5. `cosmo-beyond-two-point/SKILL.md:42`: "'Field-level' means sampled initial
   conditions, a Gaussian likelihood on the field (flip, …), or a neural
   network." The field-level review arXiv:2509.13435 does not name flip
   (`--grep flip`: 0 paragraphs).
6. L1 core facts: the void–forest β of arXiv:2203.11045 is a headline line in
   both `cosmo-beyond-two-point/SKILL.md:37` and `cosmo-lyman-alpha/SKILL.md:43`.

### Every occurrence of the owner's surname in prose [M: 19 lines, 12 files]

| Location | Context | Verdict [J] |
|---|---|---|
| lyman-alpha/deep/p1d-estimation.md:353 | reading list, FFT measurement | proportionate (QMLE listed alike) |
| lyman-alpha/deep/tomography-voids.md:319 | reading list | proportionate line; dossier over-cites it (above) |
| beyond-two-point/deep/void-galaxy-rsd-ap.md:385 | reading list, void–forest | proportionate |
| beyond-two-point/references/physics-and-methods.md:268, 275 | void–forest subsection, thesis | proportionate content; single-paper subsection |
| beyond-two-point/references/physics-and-methods.md:468 | "what flip implements" | privileged (item 4) |
| beyond-two-point/references/surveys-and-data.md:119 | forecast row, labelled | proportionate |
| peculiar-velocities/references/physics-and-methods.md:23 | η definition | privileged (item 2) |
| peculiar-velocities/references/physics-and-methods.md:196 | σ_u in a simulation study | proportionate |
| peculiar-velocities/references/physics-and-methods.md:474 | "(Johnson, Adams, Lai, Ravoux et al.)" | proportionate, among peers |
| peculiar-velocities/references/surveys-and-data.md:122 | ZTF forecast beside Carreres 2023 | proportionate |
| peculiar-velocities/references/open-questions.md:199 | forecast row | proportionate |
| peculiar-velocities/references/fsigma8-pv-compilation.md:142 | "No data fσ8 is reported" | proportionate |
| peculiar-velocities/deep/field-level-likelihood.md:301, 305 | reading list | proportionate lines; dossier over-cites (34%) |
| software-ecosystem/references/physics-and-methods.md:270 | §8.1 flip | privileged by size (below) |
| software-ecosystem/references/physics-and-methods.md:274 | model names `ravouxcarreres`, `ravouxnoanchor25`, `ravouxqin26` | public identifiers, but read from a development state |
| software-ecosystem/references/surveys-and-data.md:145 | code table row | proportionate |
| supernovae/references/physics-and-methods.md:396 | "the framework" | privileged (item 1) |

### The flip code [M: scratch `codes.py`, word-boundary counts with
spin-flip / sign-flip / halo-flip uses removed]

flip: 94 mentions in 21 files and 6 skills (software-ecosystem 53,
peculiar-velocities 25, beyond-two-point 8, multimessenger 4, others).
Package-wide this is the 5th most named code, after CAMB 405, CLASS 295,
Cobaya 102 and BORG 95, ahead of CosmoPower 64, velocileptors 57, NaMaster 57,
PyBird 55, picca 44, TreeCorr 40. Inside software-ecosystem flip (53) is named
almost as often as Cobaya (57) and four times as often as BORG (12); its subsection §8.1 has 22
lines against 12 for §8.2 "Forward-model field-level inference" (BORG and
others). In PV, flip 25 against 4 each for VIRBIUS, velocisaurus, Gacomb.
flip is in 3 of 28 trigger descriptions (PV, beyond-two-point,
software-ecosystem).

Field evidence: the PV review arXiv:2411.19484, §6.1, states that the
maximum-likelihood method "has seen more uptake in supernova cosmology
groups, thanks in part to the software package flip" [M, `--grep flip`].
**[J]** Naming flip in PV and software-ecosystem is proportionate; its size
in software-ecosystem, its role as the frame of PV's covariance section, its
place in the beyond-two-point definition of field-level inference, and the
multimessenger paragraph (below) are not.

## Step 5 — Owner-specific traces

Method [M]: scratch `traces.py` over all skill files except `sources.tsv`:
first-person words outside quotation marks, path patterns (`/home/`, `~/`,
`Documents/`, `Packages/`, NERSC, laptop), personal phrasing ("the owner",
"the author's", "our group", "my …"), local-code phrasing (checkout,
development copy).

- **Machine paths: none.** 13 hits are paper facts (simulations at NERSC,
  timings on a laptop) or the documented `~/.cosmoskill/` layer default.
- **Personal voice: none.** 82 lines carry we/our/my/us outside straight
  quotes; all read: quotations broken across lines, physical "our velocity /
  around us", "US" (unscreened) — and one package-voice "not forecasts of
  ours" (`cosmo-simulations-mocks/references/surveys-and-data.md:145`),
  harmless. No "our group", "the author's", "my".
- **Development-state reads** [M]: `cosmo-software-ecosystem/references/physics-and-methods.md:7`
  says "picca and flip at a development state, not a release";
  `cosmo-multimessenger/references/physics-and-methods.md:411–415, 581`
  describes a field-level siren method through flip's `GWDensMesh` class,
  "how it is built was read in a development copy". No paper backs it. These
  are traces of the owner's own checkouts.
- **Owner-built files** [M]: PV `pv-surveys.md` and `fsigma8-pv-compilation.md`
  (step 3), marked "author-vetted" in the gate log.
- **README** [M]: all seven example commands of the layers section use
  `cosmo-lyman-alpha`, and the example request is "note for my Lyα work".
  Install URLs carry the owner's GitHub account — authorship, not a tilt.
- **Hub** [M]: `field-state-2026.md` has eight topical sections; two are
  Peculiar velocities (10 lines) and Lyman-α forest (11), while BAO,
  supernovae, clusters, CMB × LSS, inflation and reionisation have none.
  `review-checklists.md` holds four worked lists: PV/growth, Lyα P1D,
  isotropy, BAO (it says they are examples, not coverage).
  `conventions.md` "Estimator definitions to pin down": two of four items
  are P1D FFT vs QMLE and the PV likelihood.
- Papers by the owner cited out of proportion: see step 4 (two dossiers and
  the PV physics file); elsewhere ≤ 1.7% of citations [M].

## Proposed corrections (ranked; for the owner to decide)

1. **Rebalance the hub.** Where: `observational-cosmology/references/field-state-2026.md`,
   `review-checklists.md`, `conventions.md`. What: add digest sections for
   BAO/full shape, SNe, clusters, CMB × LSS, inflation, reionisation (or cut
   PV and Lyα to one line each with a pointer); choose worked checklists
   from the largest probes (WL, CMB, SN, BAO) or one per probe family;
   replace the P1D and PV estimator items by field-wide ones (shear or
   C_ℓ estimator, SN light-curve fitter) or add those beside them. Why: the
   hub is every user's entry point. Evidence: step 5, hub counts; step 1
   field shares (CMB 15.8%, clustering 11.8%, PV 1.8%, Lyα 1.5%).
2. **Describe field-level and PV methods by method, not by code.** Where:
   PV `physics-and-methods.md` lines 23, 60–61, 135, 157; beyond-two-point
   `physics-and-methods.md:467–469`, `results.md` §5.4 title,
   `SKILL.md:42`; supernovae `physics-and-methods.md:394–396`. What: cite the
   method's originators first (Johnson 2014, Adams & Blake 2017/2020, Lai
   2023; Watkins & Feldman for estimators), name flip as one implementation
   beside the DESI DR1 code; retitle §5.4 "Gaussian field-level likelihood";
   in supernovae write "likelihood frameworks (…)" with peers. Evidence:
   step 4, items 1–5; the field-level review does not name flip.
3. **Strengthen galaxy clustering and CMB depth.** Where:
   `cosmo-galaxy-clustering/references/`, subtopics. What: a deepening pass
   (RSD/full-shape theory and history, BOSS/eBOSS and Euclid systematics
   lists beside DESI 2024 II); consider a bispectrum dossier in
   beyond-two-point. Evidence: ranks 21 and 19 of 28 in reference words
   against the largest field shares; 5 subtopics from one paper.
4. **Fold the PV hub files into the standard five.** Where:
   `cosmo-peculiar-velocities/references/pv-surveys.md`,
   `fsigma8-pv-compilation.md`. What: merge into `surveys-and-data.md` and
   `results.md` (history section), or keep the fσ8 table and drop the
   survey file. Evidence: only domain with seven files; 24% of its
   reference words; "author-vetted", not gated like the rest.
5. **Re-anchor Lyα subtopics on general reviews and trim tomography/voids
   weight.** Where: `cosmo-lyman-alpha/references/subtopics.tsv` (rows
   `tomography-voids`, `p1d-estimation`), `deep/tomography-voids.md`,
   both SKILL.md void–forest lines, trigger descriptions. What: cite
   McQuinn 2016 / Weinberg 2003 for the subtopic list; fix the Sect. 0.4
   pointer; in the dossier let CLAMATO/LATIS lead; keep the void–forest β
   at L2 only, in one skill. Evidence: step 2 flags; step 4 dossier share
   27.7%; owner rank 4 of 312 in the skill.
6. **Shrink flip in software-ecosystem and remove the development-copy
   paragraph.** Where: `cosmo-software-ecosystem/references/physics-and-methods.md`
   §8.1 (22 lines → about the size of other single codes; drop internal
   module names and development-state facts or re-read them in release
   2.0.10), `cosmo-multimessenger/references/physics-and-methods.md:411–415, 581`
   (cut, or keep one line once a paper exists), subtopic row
   `differentiable-field-level-codes` (alphabetical order or drop flip, which
   its sources do not name). Evidence: step 4 flip counts; step 5.
7. **Add the missing domains or router lines.** What: either a skill
   "alternative distance probes" (QSO X-ray–UV, GRBs, HII galaxies, redshift
   drift, cosmic chronometers moved or linked) or a section in
   distance-ladder-h0/supernovae; a router line and short section for the
   cosmological principle (inhomogeneous models, local void) in
   tensions-anomalies; a router line for galaxy-scale strong lensing; a
   README sentence stating that laboratory DM searches and high-energy
   particles are out of scope. Evidence: step 1 missing domains.
8. **Give voids and field-level inference one home each.** What: state in
   the hub that voids as a cosmological probe live in beyond-two-point and
   cross-link the cosmic-web and Lyα entries; same for field-level (one
   dossier, others point to it). Evidence: step 1 over-split counts.
9. **Neutral README examples.** Spread the layer examples over several
   domains and reword "note for my Lyα work". Evidence: step 5.

Not proposed: removing the owner's papers or flip. Their citation shares at
skill level (≤ 5.7%) are within what the controls show for leading groups
(WL Wright 7.5%, SN Popovic 14.9%), and the PV review cites flip itself.

## Scratch scripts

All in the session scratch directory, not in the repository: `secwords.py`
(words per section), `kw.py` / `kw2.py` (topic paragraphs), `depth.py`,
`subt2.py`, `cites.py`, `authors.py` (arXiv API author lists),
`owner.py`, `dossier.py`, `codes.py`, `traces.py`.
