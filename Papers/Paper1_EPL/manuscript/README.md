# A Novel Scaling Indicator of Early Warning Signals Helps Anticipate Tropical Cyclones

**Authors:** J. Prettyman, T. Kuna, V. Livina

**Published in:** EPL (Europhysics Letters)

## Code

The MATLAB code for reproducing the figures and analysis is available at:
[MatlabCodePhD/Projects/Paper1_EPL](https://github.com/DrPrettyman/MatlabCodePhD/tree/main/Projects/Paper1_EPL)

## Abstract

This paper introduces a novel power spectrum (PS) scaling indicator for detecting early warning signals (EWS) of tipping points in dynamical systems. Tipping events, modelled as the decay of critical modes approaching bifurcation, are characterised by increased return times to stable equilibria (critical slowing down). The temporal scaling properties of time series can detect this critical slowing down.

## Key Contributions

- **Novel PS-indicator**: A new early warning signal based on the power-law decay rate of the power spectrum, complementing existing ACF(1) and DFA indicators
- **Analytical foundation**: The PS scaling exponent is related to ACF and DFA exponents via the relationship: α = (1+β)/2 = 1 - γ/2
- **Application to tropical cyclones**: Demonstrates the PS-indicator can detect EWS in real geophysical data where ACF(1) fails

## Methods

Three scaling indicators are compared:
1. **ACF(1)-indicator**: Lag-1 autocorrelation function
2. **DFA-indicator**: Detrended fluctuation analysis scaling exponent
3. **PS-indicator**: Power spectrum scaling exponent (novel contribution)

## Experiments

1. **Artificial data**: Time series with linearly increasing scaling exponent (β from 0 to 2)
2. **Model data**: Pitchfork bifurcation system (100 runs averaged)
3. **Tropical cyclone data**: Sea-level pressure from 14 category 4-5 cyclones at landfall (HadISD2005 dataset)

## Key Findings

- The PS-indicator behaves similarly to ACF(1) and DFA indicators on idealised systems
- For tropical cyclone data, the PS-indicator shows an increasing trend ~50 hours before minimum pressure, providing a useful EWS where ACF(1) fails
- Window size sensitivity is important, particularly due to ~12-hour tidal oscillations in pressure data

## Files

- `eplformat_v13.tex` - Main manuscript LaTeX source
- `bibliography_v2.bib` - References
- `figures/` - Figures (fig1-5 as EPS files)
- `epl2.cls` - EPL journal class file
