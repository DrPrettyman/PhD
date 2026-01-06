# Detecting crossovers in the power spectrum using tipping point indicators

## crossovers in power spectra

The power spectrum scaling exponent indicator, developed in this chapter
in the context of detecting and predicting tipping points,

To create a time series with a clear crossover in the power spectrum we
take the sum of a Gaussian white noise series $\eta_t$ and red noise
(random walk) series $W_t$ defined by the relation
$W_t = W_{t-1} + \zeta_t$, where $\zeta_t$ are a Gaussian white noise
series independent of $\eta_t$. Thus the terms of the series are given
by $$
    
    z(t) = \sum_{\tau=0}^t \zeta_\tau + \mu\eta_t
$$ Where $\mu$ is a parameter modifying the variance of
the white noise terms $\eta_t$. Due to the linearity of the Fourier
transform we are able to calculate the power spectrum $S_z(f)$ of this
series given that we know already $$
    
    S_{\mu\eta}(f) = \left| \mu\hat{\eta}(f) \right|^2 = \mu^2
$$ since $\hat{\eta}(f)=1$, and $$
    
    S_{W}(f) = \left| \hat{W}(f) \right|^2 = \left|\frac{1}{2\pi f}\right|^2 = \frac{1}{4\pi^2}f^{-2}.
$$ Combining the two series we have $$
    S_z(f) &=& \left| \hat{z}(f) \right|^2\\
    &=& \left| \hat{W}(f) + \mu\hat{\eta}(f) \right|^2\\
    &=& \left| \frac{1}{2\pi f} + \mu\right|^2\\
    
    &=& \frac{1}{4\pi^2}f^{-2} + \frac{\mu}{2\pi}f^{-1} + \mu^2.
$$

![[] Scaling crossover in the
power spectrum of the sum of red and white noise series. Showing the
power spectrum of the series $z(t)$ (solid black line, see
eqn. [\[eqn:crossoverfunction\]](#eqn:crossoverfunction)
) imposed over the periodogram (blue).
Also showing the power spectrum of white and red noise (dashed black
lines) and their periodograms (grey and red resp.). The crossover occurs
at $f=10^{-3/2}$ (see
eqn. [\[eqn:crossoverfrequency\]](#eqn:crossoverfrequency)
). ](crossover1){#fig:crossover1
width="\\linewidth"}

In figure [1](#fig:crossover1)
 the power spectra of white noise $\mu\eta_t$
and red noise $W_t$, given by
equations [\[eqn:powerspectrum_white\]](#eqn:powerspectrum_white)

and [\[eqn:powerspectrum_red\]](#eqn:powerspectrum_red)
 respectively, are shown (dashed
lines) imposed over the periodograms of computed instances of these
series (shown in grey and red respectively). In this case the value
$$
    \mu = \frac{10^{3/2}}{2\pi}
$$ has been chosen so that the intersection of the two
curves, given by
equations [\[eqn:powerspectrum_white\]](#eqn:powerspectrum_white)

and [\[eqn:powerspectrum_red\]](#eqn:powerspectrum_red)
 is given by $$

    
     \frac{1}{4\pi^2}f^{-2} &= \mu^2,\\
     \frac{1}{2\pi}f^{-1} &= \mu,\\
     \frac{1}{2\pi}f^{-1} &= \frac{10^{3/2}}{2\pi},\\
     f &= 10^{-3/2},
     
$$ Which is the midpoint of the values $f=0.01$ and $f=0.1$
on the logarithmic scale. In
figure [1](#fig:crossover1)
 we also see the power spectrum of the
function $z(t)$, given by
equation [\[eqn:powerspectrum_cross\]](#eqn:powerspectrum_cross)
 (solid line), and the periodogram
of an instance of the time series (shown in blue). This time series is
simply the sum of the white noise and red noise series. We note that the
periodogram of $z$ entirely overlaps the periodogram of the red noise
series $W$ for small values of $f$, and overlaps the periodogram of the
white noise series $\eta$ for large values of $f$.

## Applying the PS indicator

The power spectrum of $z(t)$, given by
equation [\[eqn:powerspectrum_cross\]](#eqn:powerspectrum_cross)
, does not exhibit simple power-law
scaling, since there is no value $\xi$ for which $$
    S_z(cf) = c^\xi S_z(f).
$$ and so the power spectrum is not simply a straight line
in the log-log plot (figure [1](#fig:crossover1)
). However, this does not mean that there is
not value in applying the Power Spectrum Indicator, which simply fits a
straight line to the periodogram to obtain a single value $\xi$. When
applying the PS indicator to dynamical systems with tipping behaviour it
is not the exact value of the indicator that is of interest but the
change in the value over time as the indicator is applied in a sliding
window on the time series. In particular we are concerned with the
detection of critical slowing down in the time before a tipping point is
reached which is characterised by an increase in the autocorrelation
scaling exponent, or a "reddening" of the power spectrum as the return
time around a stable state increases.

![[] Power spectrum indicator of
the sum of white noise and red noise series with decreasing white noise
component. Panel **a**: The time series $z(t)$ (blue, left $y$-axis) and
the standard deviation $\mu$ of the white noise component (red, right
$y$-axis). Dashed black show times at which the crossover point is at
the lower end, the centre, and the upped end of the frequency range in
which the PS indicator is measured. Panel **b**: The PS indicator in a
sliding window $1\%$ of the length of the time series. Panels **c**:
Depictions of the periodograms of $z(t)$ when the crossover point is at
the lower end, the centre, and the upped end of the measured frequency
range (panels c1, c2, c3 resp.). The power spectrum (black) and the
linear fit to the periodogram (red) and also shown.
](crossover2_decrease){#fig:crossover2 width="\\linewidth"}

In figure [2](#fig:crossover2)
a we have plotted the series $z(t)$ given by
equation [\[eqn:crossoverfunction\]](#eqn:crossoverfunction)
, the sum of a red noise and a white
noise series with scaling crossover (blue line, left $y$-axis). In this
case the value of the parameter $\mu$ changes with time and is described
by the function $$
    \mu(t) = 10-10\tanh(t-6),
$$ so that $\mu\rightarrow20$ as $t\rightarrow-\infty$ and
$\mu\rightarrow0$ as $t\rightarrow\infty$. This function is plotted
alongside the time series in
figure [2](#fig:crossover2)
a (red line, right $y$-axis). We note that
the value of $f$ at which the crossover occurs in the power spectrum is
given by $$
    f_\text{c} = \frac{1}{2\pi\mu},
$$ (see
equation [\[eqn:crossoverfrequency\]](#eqn:crossoverfrequency)
) and therefore varies with the value
of $\mu$. For this experiment, when applying the PS indicator, we have
chosen to estimate the slope of the periodogram in the frequency range
$10^{-2}\leq f \leq 10^{-1}$. For large values of $\mu$, i.e.
$\mu>100/2\pi\approx15.9$ we have $f_\text{c}<0.01$ and so the crossover
point lies outside of the measurement range, in which case the PS
indicator will have a value similar to that of white noise (zero) since
the red noise aspect of the periodogram is not measured. Similarly, for
$\mu<10/2\pi\approx1.59$ we have $f_\text{c}>0.1$ and in this case only
the red noise aspect of the periodogram is measured. The times at which
these two values of $\mu$ occur, which are the times that the crossover
point enters and then leaves the measured frequency range, are marked by
vertical dashed lines on
figure [2](#fig:crossover2)
a. The centre dashed line marks the point in
time at which $\mu = 10^{3/2}/2\pi\approx5.03$, when the crossover point
appears directly in the centre of the measured frequency range in the
logarithmic scale (see
equation [\[eqn:crossoverfrequency\]](#eqn:crossoverfrequency)
).

In figure [2](#fig:crossover2)
b the PS indicator is plotted in a sliding
window of length $10^4$ points, which is $1\%$ of the length of the time
series, $N=10^6$. The three dashed vertical lines are continued from
figure [2](#fig:crossover2)
a and show the times at which the crossover
point enters, is in the centre of, and leaves the frequency range in
which the PS indicator is measured. We note that the PS indicator rises
correspondingly as the value of $\mu$ decreases, that is, as the
variance of the white noise component of the system decreases, leaving
only the red noise component as $\mu\rightarrow0$, the "redness" of the
data increases. Thus, we are able to detect an increasing reddening of
time series using the PS indicator, even when there is no simple
power-law scaling due to the presence of a crossover.

In figure [2](#fig:crossover2)
c1, c2 and c3 three periodograms are shown,
these are periodograms of a time series $z(t)$ of length $10^5$ with a
constant value of $\mu$. The three values if $\mu$ used are the values
marked in figure [2](#fig:crossover2)
a with dashed lines, at which points the
crossover is at the lower end (panel c1), the centre (panel c2), and the
upper end (panel c3) of the measured frequency range. Also shown over
the three periodograms are the PS indicator estimation (red line) and
the analytically calculated power spectrum (black curve) in
equation [\[eqn:powerspectrum_cross\]](#eqn:powerspectrum_cross)
. This power spectrum in each case
is a smooth curve, not the union of two lines depicted in
figure [1](#fig:crossover1)
, and the PS indicator is still influenced by
the decreasing "red" part of the power spectrum a short time before the
crossover point enters the range $10^{-2}\leq f \leq 10^{-1}$, and
similarly the periodogram is still influenced by the flat "white" part
of the spectrum for a short time after the crossover point leaves this
range. In figure [2](#fig:crossover2)
c1 we see the influence of the red noise when
the crossover point is precisely at the lower bound of the range,
although the white noise is still dominant. The PS indicator for this
value of $\mu$ is $0.36$; this value is closer to zero for even larger
values of $\mu$ where the red noise has a much smaller variance than the
white noise and has far less influence on the shape of the periodogram.

## Crossover detection in the AR(1) model

The example of the previous section, the sum of a red noise process and
a white noise process, was chosen for its clearly visible power spectrum
crossover. We now look at the discrete AR(1) process $x_t$ defined by
the equation $$
    x_t = \mu x_{t-1} + \eta_t
$$ where $\eta_t$ is a Gaussian white noise process with
variance $\sigma^2$ and $\mu$ is a parameter which, in this experiment,
is in the range $0\leq \mu \leq 1$. For $\mu=0$ this is a pure Gaussian
white noise process while for $\mu=1$ this is a random walk (red noise).
As $\mu$ increases from $0$ to $1$ as a function of time we expect to
see this noise process become 'redder': developing long-term memory,
which is not present in a white noise signal, and therefore developing
properties similar to those of the random walk. Of course the lag-1
autocorrelation function will increase with $\mu$, but in this example
we inspect the power spectrum, which is given by $$


    S_x(f) &= \frac{\sigma^2}{\left|1-\mu e^{-2\pi i f}\right|^2},\\
    &= \frac{\sigma^2}{1+ \mu^2 - 2\mu\cos(2\pi f)},

$$ \[CITE Von Storch 2002\]. The derivation of this equation
assumes that $\mu$ is constant over time whereas we are interested in
cases where $\mu$ is increasing (or otherwise changing). However, we are
only interested in the shape of the power spectrum in time windows which
are short relative to the whole time series, so that we can track the
changing shape, and we assume $\mu$ is constant within each window. That
is, we assume $\mu$ changes slowly relative to AR(1) process.

For the purposes of tipping point analysis we are interested in the
*Power Spectrum Scaling Exponent* which we define as the value $\beta$
such that the power spectrum satisfies the scaling relationship
$$
    S_x(f) \sim f^{-\beta}.
$$ For power spectra where $\beta$ exists, that is, where
there is a global power-law scaling relationship, the value can be
obtained by taking the negative value of the gradient of the log-log
plot. Given a time series, we can estimate the value $\beta$ by
measuring the negative gradient of the log-log plot of the periodogram.
For time series of processes whose power spectra do not satisfy a
power-law scaling relationship, and therefore no single number $\beta$
exists, we are still able to measure the gradient of the power spectrum
at a particular value of $f$ (or averaged over a range of values). We
refer to this specific exponent $\beta_f$ as the *Power Spectrum
Exponent*, although it is not a scaling exponent in the sense that the
power spectrum actually satisfies a power-law scaling relationship.

In the case of the AR(1) process we calculate the specific PS exponent
$\beta_f$ as the negative gradient of the log-log plot of the power
spectrum, which we obtain by differentiating $\log[S_x(f)]$ with respect
to $\log f$: $$
    
    \beta_f := \text{PS exponent} &= -\frac{d}{d(\log f)}\log[S_x(f)],\\
    &= -\frac{d}{d(\log f)}\log\left[\frac{\sigma^2}{1+ \mu^2 - 2\mu\cos(2\pi f)}\right],\\
    &= -\frac{d}{du} \log\left[\frac{\sigma^2}{1+\mu^2-2\mu\cos(2\pi 10^u)}\right],\\
    &= \frac{d}{du} \log\left[1+\mu^2-2\mu\cos(2\pi 10^u)\right],\\
    &= \frac{1}{\ln(10)}\cdot\frac{4\pi \mu \ln(10) 10^u \sin(2\pi 10^u)}{1+\mu^2-2\mu\cos(2\pi 10^u)},\\
    &= \frac{4\pi \mu f \sin(2\pi f)}{1+\mu^2-2\mu\cos(2\pi f)},
    
$$ where we have used the substitution $u = \log_{10}(f)$ to
simplify the calculation. This gradient may then be evaluated at a
particular value of $f$ (or, rather, in the case of the periodogram,
estimated by a linear fit in a particular range of $f$ values). What we
refer to as the *Power Spectrum Indicator* is the value of this PS
exponent as a function of time, $$

    B_f(t):=~\text{PS indicator} = \frac{4\pi \mu f \sin(2\pi f)}{1+\mu^2-2\mu\cos(2\pi f)},
$$ where the $t$ dependence comes from the fact that
$\mu = \mu(t)$ is a function of time. We are now able to take the $t$
derivative: $$
\frac{d}{dt}B_f(t) = \frac{4\pi f \sin(2\pi f)\dot\mu(1-\mu^2)}{1+\mu^2-2\mu\cos(2\pi f)}.
$$ Equating this to zero, assuming $\mu(t)$ is not a
constant function ($\dot\mu \neq 0$), we find the maximum value of the
PS indicator occurs when $\mu=1$ when the AR(1) process is a random
walk, at which point the PS indicator has the value $$

\max[B_f] = \frac{2\pi f \sin(2\pi f)}{1-\cos(2\pi f)} ~~\xrightarrow[f\rightarrow 0]{}~ 2.
$$ For larger values of $f$ this maximum indicator value
is not close to the maximal value of 2. For $f = 0.1$ we have
$\max[B_{0.1}] = 1.93$, whereas for $f = 0.38$ already the value is
significantly less: $\max[B_{0.38}] = 1$. In cases where the PS
indicator is being estimated using a noisy periodogram it is essential
that the increase in the indicator value as critical slowing down occurs
(that is, as $\mu$ increases from 0 to 1) is easily observable. For this
reason, when we estimate the PS scaling exponent, a frequency
$\log(f)\leq -1$ should be used in order to be able to observe the
largest increase in the PS indicator.

![[] (**a**) The
power spectrum of the AR(1) process (see
eqn. [\[eqn:AR1process_powerspectrum\]](#eqn:AR1process_powerspectrum)
) is plotted on a log-log scale
for various values of the parameter $\mu$. Note the 'white-noise' (flat)
part of the power spectrum for small $f$ and the 'red-noise' (negative
gradient) part for large $f$. (**b**) The PS indicator (see
eqn. [\[eqn:AR1_psindicator\]](#eqn:AR1_psindicator)
) is plotted as a function of $f$ for
the same $\mu$ values. ](AR1_powerspectrum){#fig:AR1_powerspectrum
width="\\linewidth"}

In figure [3](#fig:AR1_powerspectrum)
 the power spectrum of the AR(1)
process is plotted (panel **a**) for parameter value $\mu = 0.9$. We
note that for small values of $f$ ($\log f<-2.5$) the "white noise"
(flat) aspect of the power spectrum is visible whilst for larger values
($\log f\approx -1$) we observe a "red noise" (gradient $= -2$) feature,
and there is a crossover which occurs at approximately $\log f= -2$. We
also note that, similar to the example in
figure [2](#fig:crossover2)
, this crossover point a value of $f$
dependent on the parameter $\mu$: also plotted are the power spectra for
$\mu = 0.7,~ 0.8,~ 0.999$. In
figure [3](#fig:AR1_powerspectrum)
b the PS exponent $B_f$ is plotted as
a function of $\log f$ for the same (fixed) values of $\mu$. We are able
to see the white noise part of the power spectrum ($\log f<-2.5$) where
$B_f=0$ and the peak ($B_f\approx 2$), which occurs at
$\log f\approx -1$ for $\mu = 0.9$, corresponding to the
negative-gradient 'red noise' aspect of the power spectrum in panel
**a**. This plot also allows us to visualise the observation made in
equation [\[eqn:maximumPSindicator_AR1\]](#eqn:maximumPSindicator_AR1)
 that for large values of $f$
($\log f > -1$) the PS indicator does not reach a value close to the
maximum value of 2, even for $\mu$ close to 1.

![[] The
PS indicator is plotted as a function of $\mu$ for various values of
$f$. Note that for larger $f$ the PS indicator has a maximum value $<2$
while for smaller $f$ the indicator shows the characteristic increasing
('reddening') trend only in the $\mu>0.9$
range.](PSexponent_changingmu){#fig:PSexponent_changingmu
width="\\linewidth"}

In figure [4](#fig:PSexponent_changingmu)
 we plot the PS indicator
(equation [\[eqn:AR1_psindicator\]](#eqn:AR1_psindicator)
) as a function of $\mu$ rather than as
a function of time, which is equivalent to the assumption $\mu(t)=t$.
The PS indicator increases, as expected, as $\mu$ increases from 0 to 1.
We note that for very small values of $f$ ($\log f<-2$) the indicator
value is close to zero until the point $\mu=0.9$ when it increases very
steeply. This effect can also been seen in
figure [3](#fig:AR1_powerspectrum)
b where we observe that even at
$\mu=0.9$ the indicator is zero for small $f$, whereas for $\mu = 0.999$
the indicator is $\approx 2$ over the whole range $-3<\log f<-1$. For
larger $f$ it is possible to see the increasing trend in the indicator
over the whole series of increasing $\mu$. For this reason, when one
wishes to detect a 'reddening' of noise due to critical slowing down,
which is modelled as an AR(1) process \[CITE Scheffer\], the most
obvious trend will be visible when measuring the PS scaling exponent
using a frequency $\log f\geq-2$. We note, however, that this will not
be true if a relatively high base-level PS indicator ($B_f>0.5$) is
observed for $\log f=-2$, implying an AR(1) parameter $\mu>0.9$. In this
case it may be more instructive to observe whether there is a steep
increase in the indicator as $\mu$ increases between 0.9 and 1; this is
clearly visible for $\log f=-3$ but not for $\log f=-1$.

In practical applications where only short time series are available and
the power spectrum is approximated by the fast Fourier transform
periodogram, there may be very few data available in the lower
frequencies due to the logarithmic scale. In these cases it may not be
possible to reasonably estimate the PS exponent for small values of $f$
and so the frequencies used will be informed by the length of the time
series. In table [1](#tab:AR1_frequencyrange)
 we have enumerated the number of
data points in different frequency ranges having obtained the fast
Fourier transform periodogram from a time series of $10^4$, $10^3$ and
$10^2$ points. When using very short time series, say $100$ points, it
is already impossible to estimate the gradient of the periodogram for
frequencies $\log f<-2$ because there are simply not enough data to
perform a linear fit. However, in the range $-2\leq\log f\leq-1$ it is
at least possible, with 10 points available, although we note that this
will likely give a very noisy PS indicator and longer time series or
large ensembles would be preferred.

+:------------------------:+:----------:+:----------:+:----------:+
| Frequency range          | Number of data in range              |
|                          +------------+------------+------------+
|                          | $N=10^{4}$ | $N=10^{3}$ | $N=10^{2}$ |
+--------------------------+------------+------------+------------+
| $-3.5\leq\log f\leq-2.5$ | 28         | 3          | 0          |
+--------------------------+------------+------------+------------+
| $-3\leq\log f\leq-2$     | 91         | 10         | 1          |
+--------------------------+------------+------------+------------+
| $-2.5\leq\log f\leq-1.5$ | 285        | 28         | 3          |
+--------------------------+------------+------------+------------+
| $-2\leq\log f\leq-1$     | 901        | 91         | 10         |
+--------------------------+------------+------------+------------+
| $-1.5\leq\log f\leq-0.5$ | 2846       | 285        | 28         |
+--------------------------+------------+------------+------------+

: The fast Fourier transform periodogram is obtained for time series of
length $10^4$, $10^3$ and $10^2$ and the number of data in various
frequency ranges is recorded. For time series of length $10^2$ there are
not sufficient data to estimate the PS scaling exponent for $\log f<-2$.

Taking all of these factors into account, we conclude that using a
frequency range $-2\leq\log f\leq-1$ in which to measure the PS scaling
exponent will give the most clearly observable increase in the PS
indicator during critical slowing down. At the higher end of this range
we begin to observe the sudden drop in the maximum exponent value; at
the lower end of the range there exist the dual problems of almost no
increase for parameter values below $\mu=0.9$, and an insufficient
number of data for estimation when dealing with short time series.
