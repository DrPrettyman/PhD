# Python EWS Analysis

Python implementation of Early Warning Signal (EWS) detection techniques developed during the PhD project.

Thesis: [University of Reading repository](http://centaur.reading.ac.uk/98364/1/23022044_Prettyman_Thesis_Joshua%20Prettyman.pdf)

## Modules

### tippingpoints/

Core analysis library with reusable functions:

| Module | Description |
|--------|-------------|
| `scaling_methods` | Sliding-window ACF, DFA, and PSE indicators for detecting critical slowing down |
| `noise_methods` | Stochastic process generators (white noise, random walks, AR(1), AR(63)) |
| `numerical_methods` | SDE integrators (Euler-Maruyama, Milstein) |
| `timeseries` | `TimeSeries` class wrapping indicator calculations and plotting |

### thesisfigures/

Code to reproduce specific figures and tables from the thesis:

| Module | Description |
|--------|-------------|
| `figures_c1` | Chapter 1 figures |
| `figures_c2` | Chapter 2 figures |
| `plot_helper` | `ThesisPlot` class for standardized thesis-style plots |

### Usage

```python
from tippingpoints import scaling_methods

# Calculate sliding-window power spectrum exponent
t, pse = scaling_methods.pse_sliding(t, z)

# Calculate sliding-window DFA exponent
t, dfa = scaling_methods.dfa_sliding(t, z)

# Calculate sliding-window lag-1 autocorrelation
t, acf = scaling_methods.acf_sliding(t, z)
```

Or use the `TimeSeries` class:

```python
from tippingpoints.timeseries import TimeSeries

ts = TimeSeries(z, t)
ts.set_pse_indicator()
ts.plot_indicator()
```

## Documentation

Sphinx documentation source is in `docs/source/`. To build:

```bash
cd docs
make html
# Open build/html/index.html
```

## Dependencies

- Python 3.9+
- NumPy
- Matplotlib
