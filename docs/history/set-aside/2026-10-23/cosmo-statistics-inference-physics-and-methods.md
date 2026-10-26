# cosmo-statistics-inference — references/physics-and-methods.md, Sects. 5.2 and 8.2 (agent conversions)

Set aside on 2026-10-24 (numbers run) before the agent-computed values were removed. Verbatim from the working tree (base commit 2b5e381). The threshold table was computed by an agent from the χ² survival function, and the sentences below it convert values with formulae; none of these numbers is read in a paper. The file now keeps the formulae and the values stated in arXiv:2503.14738 and arXiv:2607.28918.

- The statistics literature defines split-`R̂ = sqrt(var⁺/W)` with `var⁺ = (N − 1) W/N + B/N`, `B` and `W` the between- and within-chain variances over `M` half-chains of `N` draws (Vehtari et al. 2021, arXiv:1903.08008) [src: Eqs. 1–4]. Recommended practice: rank-normalised, folded `R̂ < 1.01`, "much tighter than the one recommended by Gelman and Rubin (1992)" (1.1); at least four chains; rank-normalised bulk and tail effective sample size above 400 [src: Sect. 2]. A cosmology `R − 1 < 0.01` is roughly `R̂ < 1.005`, not `R̂ < 1.01` `[der: for one parameter and large N, Lewis's D ≈ B/(N W) ≈ R̂² − 1 ≈ 2(R̂ − 1); ignores the eigenvalue maximum and chain splitting]`.

DESI DR2 (DESI Collaboration 2025, arXiv:2503.14738) finds the best fit with `iminuit` started from the MAP of each chain, defines `Δχ²_MAP` as "twice the difference in the negative log posteriors at the maximum posterior points for each model", and converts it to "the corresponding (frequentist) significance levels given 2 extra free parameters" [src]. The conversion is `p = exp(−Δχ²/2)` for two degrees of freedom, then the two-sided Gaussian equivalent `[der]`; it reproduces the published column (`Δχ² = −12.5` gives 3.10σ, `−21.0` gives 4.19σ; full table in `results.md` §4).

Thresholds `[der, from the χ² survival function]`:

| nσ (two-sided) | p | Δχ², 1 dof | 2 dof | 3 dof | 4 dof |
|---|---|---|---|---|---|
| 1 | 0.317 | 1.00 | 2.30 | 3.53 | 4.72 |
| 2 | 0.0455 | 4.00 | 6.18 | 8.02 | 9.72 |
| 3 | 2.70e-3 | 9.00 | 11.83 | 14.16 | 16.25 |
| 4 | 6.33e-5 | 16.00 | 19.33 | 22.06 | 24.50 |
| 5 | 5.73e-7 | 25.00 | 28.74 | 31.81 | 34.56 |

Conditions for the conversion to hold: nested models, the simpler model in the interior of the larger one's parameter space, Gaussian asymptotics, no parameter that becomes unidentified under the null. `sqrt(Δχ²)` is the significance only for one extra parameter; applying it to w0wa would turn 3.1σ into 3.5σ `[der]`.
