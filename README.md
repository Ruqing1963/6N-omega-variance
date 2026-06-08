# Part XXVI — The Second Moment of ω under Twin-Centre Conditioning

*Volume III of the Arithmetic Geodynamics programme on the 6N skeleton.*

Every earlier part used **first moments** of ω_{>3}(N) (distinct prime factors > 3
of a centre N): twin centres are enriched at high ω. The **second moment** — the
Erdős–Kac variance, and how it responds to conditioning on N being a twin centre
(6N±1 both prime) — was left open. **This paper closes it empirically**, sieving all
centres up to **6N = 6×10⁸ (2,166,300 twin centres)**.

### Findings

- **Mean shift saturates.** ⟨ω⟩_twin − ⟨ω⟩_all grows but decelerates sharply,
  approaching a finite limit ≈ 0.21–0.22 (it does **not** track ln ln). It is a
  convergent small-prime sum ≈ Σ_{q>3} 2/(q(q−2)) (q=5 alone contributes 0.133).
- **Variance ratio stable:** Var_twin/Var_all = **1.104 ± 0.005**.
- **Dispersion conserved:** (Var/mean)_twin/(Var/mean)_all = **1.011 ± 0.004** across
  2.5 orders of magnitude — not a small-data fluctuation.

**Interpretation — a near-Poisson tilt.** Writing ω = Σ_q 1[q|N] (near-independent
Bernoulli(1/q)), the twin weight ∏_{q|N} q/(q−2) nudges each p_q up slightly; this
shifts the mean to a finite limit and rescales mean and variance nearly in step, so
the Erdős–Kac dispersion **survives conditioning**.

| 6N_max | ln ln | mean shift | Var ratio (twin/all) | (V/m)_all | (V/m)_twin |
|---|---|---|---|---|---|
| 1.5×10⁶ | 2.655 | +0.1710 | 1.097 | 0.2896 | 0.2916 |
| 6×10⁶ | 2.748 | +0.1845 | 1.109 | 0.3066 | 0.3117 |
| 3×10⁷ | 2.846 | +0.1995 | 1.111 | 0.3252 | 0.3303 |
| 1×10⁸ | 2.913 | +0.2085 | 1.105 | 0.3380 | 0.3414 |
| 3×10⁸ | 2.971 | +0.2120 | 1.102 | 0.3489 | 0.3518 |
| 6×10⁸ | 3.006 | +0.2149 | 1.102 | 0.3554 | 0.3585 |

### A clarification (ties off a separate thread)

The **annihilation/tiling criterion** of Part XXI (zero joint density ⟺ shifted
dead-sets cover ℤ/q) is **exactly the classical Hardy–Littlewood admissibility
condition** (inadmissible ⟺ the tuple covers ℤ/p for some prime p); e.g. {0,2,4}
covers ℤ/3, {0,2,6} does not. The annihilation lattice is the complement of the
admissible set (Erdős covering systems). Known combinatorics in new coordinates.

## Layout

```
.
├── paper/    Chen_6N_Paper26.{tex,pdf} + figures
├── figures/  fig_omega_variance.{pdf,png} · fig_omega_trend.{pdf,png}
├── data/     omega_moments_multiscale.csv
├── code/
│   ├── exp_omega_big.py            # sieve experiment to 6N=6e8 (memory-lean, multi-scale)
│   ├── fig_omega_variance_make.py  # distributions + enrichment figure
│   ├── fig_omega_trend.py          # mean-shift saturation + dispersion-conservation figure
│   └── verify_omega.py             # small-scale moments + admissibility=covering equivalence
├── CITATION.cff · .zenodo.json · LICENSE (MIT)
```

## Reproducing

```bash
pip install numpy matplotlib
python code/verify_omega.py     # fast checks (small scale + admissibility equivalence)
python code/exp_omega_big.py    # full sieve to 6N=6e8 (~600MB RAM; writes ek_*.npy + table)
python code/fig_omega_variance_make.py   # reads ek_*.npy
python code/fig_omega_trend.py
```

Expected: mean shift saturates ~0.215; variance ratio ~1.104; dispersion ratio
twin/all ~1.011.

## Scope

A new **measurement** for this programme, **not** a new theorem. It confirms (does
not supersede) classical Erdős–Kac and claims no infinitude of twins or any
constellation. Continues Part XXV (doi:10.5281/zenodo.20587516).

## License

MIT — see `LICENSE`.
