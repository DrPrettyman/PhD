# Power Spectrum Scaling as a Measure of Critical Slowing Down and Precursor to Tipping Points in Dynamical Systems

**Authors:** Joshua Prettyman, Tobia Kuna, Valerie Livina

**Published in:** Environmental Research Letters (IOP Publishing)

## Code

The MATLAB code for reproducing the figures and analysis is available at:
[MatlabCodePhD/Projects/Paper3_ERL](https://github.com/joshuaprettyman/MatlabCodePhD/tree/main/Projects/Paper3_ERL)

## Abstract

This paper provides an analytical justification for using the power spectrum (PS) scaling exponent as a tipping point indicator, based on the mathematical formulation of critical slowing down (CSD). The usefulness of the PS indicator is assessed when the power spectrum does not exhibit true power-law scaling, or changes over time. The method is shown to be robust against trends and oscillations in time series, making it suitable for studying resilience in ecological and geophysical systems with periodic oscillations.

## Key Contributions

- **Analytical foundation for PS indicator**: Derives the PS indicator directly from the AR(1) model of critical slowing down
- **Optimal frequency range**: Determines the best frequency range (10^-2 to 10^-1) for PS exponent estimation
- **Robustness analysis**: Demonstrates PS indicator resilience to trends and periodic oscillations where ACF1 and DFA fail
- **Non-scaling power spectra**: Shows PS indicator remains useful even when true power-law scaling doesn't exist

## Theory

The AR(1) process models critical slowing down:
```
z(t_{n+1}) = exp(-κΔt) z(t_n) + ση_n
```

The PS indicator is derived from the AR(1) power spectrum:
```
S_z(f) = σ² / (1 + μ² - 2μcos(2πf))
```

Key result: The PS indicator increases from 0 to 2 as the AR parameter μ increases from 0 to 1 (approaching the tipping point).

## Key Findings

1. **Frequency range**: Optimal estimation in range -2 ≤ log(f) ≤ -1, corresponding to time scales 10 ≤ s ≤ 100
2. **Crossover behaviour**: PS indicator detects "reddening" even when power spectrum has crossover (no true scaling)
3. **Trend robustness**: For time series length N ≥ 10³, PS indicator is unaffected by parabolic trends (unlike ACF1)
4. **Periodicity robustness**: PS indicator unchanged by superimposed sine waves, while ACF1 and DFA are significantly affected
5. **GISP2 application**: Confirms CSD in ice-core data prior to Bølling warming event, consistent with previous DFA results

## Sensitivity Analysis

| Condition | ACF1 | DFA | PS |
|-----------|------|-----|-----|
| Pure AR(1) | Best | Good | Good |
| With parabolic trend | Poor | Poor | Good (N≥10³) |
| With periodic oscillations | Poor | Poor | Excellent |

## Files

- `jPrettyman_ERL_clean.tex` - Main manuscript LaTeX source
- `jPrettyman_ERL_highlighting.tex` - Version with revision highlights
- `bibliography_prettyman.bib` - References
- `figures/` - Figures (c2fig07-19, GISP_fig09 as EPS files)
- `iopart.cls` - IOP journal class file
