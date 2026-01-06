# Tobias' notes after our discussion (also with Jochen)

- rank test, using change in rank, compare with average rank, proper
  treatment of change size.

- hypothesis test, trend, no trend

- biased by a prior knowledge of finiteness of time horizon

- condition study using the knowledge of the event time

- rank test for $X_{t+1}-X_{t}$ or square of this

- $\chi^2$ is not asymptotically stable

- use better trend statistics in a window for smaller window

- How large the window has to be?

- to get rid of oscillation subtract all harmonics!

- what is the noise?

# Email from Valerie

Here is the list of small (hopefully, useful) exercises that could
provide you with a number of functions that you could use later in your
time series analysis.

\- write a function that plots power spectrum (PS) of input time series
and allows you to pick by mouse the points between which you would like
to estimate the scaling exponent; plot in the same figure the fitting
line and typed value of the exponent

\- do the same for DFA (for example, use the c-code from physionet.org
that calculates DFA curve, which is then plotted by Matlab): figure of
the curve, mouse-picked points for estimating range, plotted fit line
and typed values of the exponent

\- write as functions the codes for estimation of ACF, PS, and DFA
exponent, with inputs such as time series itself, window size, range of
estimation (for DFA and PS) and how many points to skip for sliding
window

\- code for a contour plot of Kendall coefficients (trend estimation in
the input indicator curve) for aggregated data with varying window of
aggregation versus window length

\- write a function that generates a power-low correlated noise of
prescribed length and correlation exponent (transformation in the
Fourier domain).

\- code that builds a stochastic model with correlated noise (from the
previous exercise) and low-frequency variability similar to the observed
in the real data

\- apply the analysis to the simulated data (of the previous exercise),
as you did with real data.

# Finding the noise in the signal

To find the "colour of noise" we look at the scaling exponent of the
power spectrum of a signal.\
Question: Is it useful to "detrend" the signal first?\
I say, no. Because what appears to be a trend may be due to noise, and
there is no way of knowing. The 12-hourly oscillations certainly seem
super-imposed onto the signal, they may be due to tidal or temperature
phenomena and is is reasonable to remove them. However, other trends are
surely due to noise. Except, I suppose, just before the cyclone appears
(which is the area we are interested in), when trends may be imposed by
the cyclone. It is probably preferable anyway to view these trends as an
alteration to the "colour" of the noise, and this alteration will be our
early warning signal. But then everything is "noise" before you know
what causing it, I suppose. Except for genuine quantum randomness\...
