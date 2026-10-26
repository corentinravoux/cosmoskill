# Set aside from cosmo-tensions-anomalies/deep/anomaly-significance.md

Numbers run of 2026-10-23 (owner's rule: no number computed by an agent). Verbatim from the file at commit 2b5e381; line numbers of that version.

## Lines 212-217 (Choices, mask for parity: derived factor)

R^TT lower-tail probability about 1% at ℓ_max = 20–30 with the 2018 common
mask; the 2015 mask on 2018 data gives 0.3% at ℓ_max = 27; the low-ℓ
likelihood mask gives 0.2% at ℓ_max = 24, and higher-latitude sky
"diminishes the odd point parity preference" [src: arXiv:1906.02552, Sect.
6.3]. A mask change alone moves p by a factor of three to five [der: 1%
against 0.3% and 0.2%].

## Lines 222-229 (Choices, simulation set: table with the derived resolution column)

| Ensemble | Size | Content | Resolves p down to | Used by |
|---|---|---|---|---|
| FFP10 | 999 per method | signal + end-to-end noise and systematics, component-separated | ≈ 10⁻³ | Planck 2018 VII |
| Noise-free ΛCDM | 10⁸ | CMB only, Planck best fit | ≈ 10⁻⁸ | Jones et al. 2023 |
| Signal + noise mix | 10⁴ CMB × 300 noise | combinations "not completely independent" | ≈ 10⁻⁴ | Shi et al. 2022 |

[src: arXiv:1906.02552, Sect. 4; arXiv:2310.12859, Methods;
arXiv:2206.05920, Sect. II.2; resolution column der: 1/N]

## Lines 333-334 (What goes wrong: derived bound)

- A p-value below 1/N_sim quoted as a number. With 999 simulations, "<
  0.1%" is a bound [der: 1/999], and Schwarz sets the Planck floor at 0.2%.
