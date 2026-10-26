# cosmo-statistics-inference — deep/model-comparison.md (agent differences)

Set aside on 2026-10-24 (numbers run) before the agent-computed values were removed. Verbatim from the working tree (base commit 2b5e381). The differences, logarithms and the table row below were computed by an agent from values of arXiv:2503.14743, arXiv:2511.10631 and arXiv:2609.04334.

- Direct measurement: Karim et al. widen every prior (Table 3: `(w_0, w_a)` area 1.096 against 15.5,
  shared parameters also widened) on identical data; `ln B` moves from −0.92 to +2.36 (their sign:
  positive favours ΛCDM) on posteriors that are "indistinguishable" [src: Sect. IV.1, Table 3]. The
  logarithm of the `(w_0, w_a)` area ratio is 2.65 `[der: ln(15.5/1.096)]`, against a measured
  shift of 3.28; the shared parameters cancel between models, so the 0.6 difference is not
  explained by the text read and is left unresolved (evidence errors for these two rows not read).

- **Two evidence analyses, same DESI priors, DR2 BAO + CMB + SNe** (sign: positive favours w0wa).
  Lodha et al. (CMB as in the DESI paper): −0.66 ± 0.44, 3.03 ± 0.44, 4.88 ± 0.44 for Pantheon+,
  Union3, DESY5 [src: App. A, Table 4]. Ong et al. 2025 (Planck 2018 CamSpec, PolyChord in Cobaya,
  `w_0 ∈ [−3, 1]`, `w_a ∈ [−3, 2]`): −1.70 ± 0.26, +1.37 ± 0.27, +3.32 ± 0.27 [src: Sect. II,
  Table 1]. The two disagree by 1.0 to 1.7 in `ln B` for every compilation, beyond their quoted
  errors `[der: differences 1.04, 1.66, 1.56]`; the CMB likelihood and the `θ_MC → H_0` substitution
  differ, and no paper read reconciles them.

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| `ΔDIC − Δχ²_MAP`, w0wa, three SN samples | 3.9, 3.9, 3.8 `[der: from Table 3]` | DESI DR2 | arXiv:2503.14743 | Table 3 |

- The reason for the 1.0–1.7 difference in `ln B` between arXiv:2503.14743 and arXiv:2511.10631 with
  the same priors was not established; nor the 0.6 gap between the measured `ln B` shift and the
  logarithm of the prior-area ratio in arXiv:2609.04334.
