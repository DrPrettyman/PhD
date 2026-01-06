# Overview

A model of the sea level pressure profile in the vicinity of a hurricane
is presented. The model is based on (holland1980) but is modified so
that the pressure is modelled at a fixed point in space as a function of
time, rather than at a fixed time as a function of the distance from the
hurricane centre. We are therefore able to model the effect on sea level
pressure (at a weather station for example) of an approaching hurricane.

Possibly we will explore the following paths:

1.  Adding time dependency to the Holland1980 model generally (replacing
    $r$-radial distance, with $d(t)$-distance at time $t$), and also to
    the various model parameters (ambient pressure, central pressure).

2.  Adding some stochasticity to these parameters.

# Holland1980 Hurricane model

(holland1980) presents a model of the wind ($V_g$) and pressure ($p$)
profiles in hurricanes: $$
p(r) &= p_c + (p_n-p_c)\exp\left( \frac{-A}{r^B} \right)\\
V_g(r) &= \left[ AB\frac{p}{\rho r^B} + r^2f^2 \right]^{1/2} - \frac{rf}{2},
$$ where $p_c$ and $p_n$ are the central and ambient
pressures, $\rho$ is the density of air (assumed constant at 1.15kg
m$^{-3}$) $A$ and $B$ are parameters to be determined, $f$ is the
Coriolis parameter, and $r$ is the radial distance from the centre of
the hurricane. Holland fits this model to three Australian hurricanes:
Tracy (December 1974), Joan (December 1975) and Kerry (February 1979).
The values of the fitted parameters $A$ and $B$ are given in table
[1](#table1), these are
obtained by fitting to scarce observations, especially observations of
maximum wind speed $V_m$ given by $$
V_m = \left(\frac{B(p_n-p_c)}{\rho e}\right)^{1/2}
$$ and occurring at a radius $R_w = A^{1/B}$.

  Hurricane    $A$    $B$
  ----------- ------ ------
  Tracy        23.0   1.5
  Joan         49.5   1.05
  Kerry        225    1.4

  : Values of fitted parameters in three hurricanes (holland1980)

# Modified model (time dependent)

We consider a fixed point at distance $d(t)$ from the hurricane centre
at time $t$. In our model equations we can simply replace $r$ with
$d(t)$ to introduce a time dependence. We therefore want to estimate the
function $d$. If the hurricane moves in a straight line towards the
fixed point with a speed of $v$kmph we will have simply
$$
d:t\mapsto -(vt),
$$ where the hurricane centre reaches the point at time
$t=0$ and 1 hour before that is called $t=-1$. We can generalise this to
a hurricane moving in a straight line at $v$kmph, not necessarily
directly towards the fixed point, in this case we have
$$
d:t\mapsto \sqrt{d_0^2 + (vt)^2},
$$ where $d_0$ is the distance of the closest approach to
the point, which happens at time $t=0$. But hurricanes rarely move in
straight lines, say we decide that the hurricane moves along a circular
arc of radius $R$km, with speed $v$kmph, then the distance is given by
$$
d(t) = \sqrt{(R\pm d_0)^2 + R^2 - 2R(R \pm d_0)\cos\left(\frac{-vt}{R}\right)}
$$ where the sign in the $(R\pm d_0)$ terms is + when the
weather station lies outside of the circle, and $-$ when it lies inside.

and we might also want to add some noise to this. We might also
introduce a time-dependent speed $v(t)$.

## Central pressure

The central pressure $p_c$ can obviously change over time, generally
decreasing at first, then increasing. We might model this as a simple
piecewise linear trend decreasing from the ambient pressure at the time
when the hurricane forms $p_n(t_s)$, to the central pressure at its
minimum point $p_c(t_\text{min})$ then incresing again to the the
central pressure at time $t=0$ ($p_c(0)$): $$
p_c:t\mapsto \left\{
\begin{array}{ll}
      \frac{p_n(t_s)-p_c(t_\text{min})}{t_s-t_\text{min}}(t-t_s)+p_n(t_s) & t \leq t_\text{min} \\
      \frac{p_c(t_\text{min})-p_c(0)}{t_\text{min}}t + p_c(0) & t \geq t_\text{min} \\
\end{array} 
\right.
$$ Or, we might model each piecewise component as a
parabolic trend, something like $$
p_c(t) = \frac{p_c(0)-p_c(t_\text{min})}{t_\text{min}^2} t^2 - 2\frac{p_c(0)-p_c(t_\text{min})}{t_\text{min}} t + p_c(0).
$$ But, possibly it is best to fit a polynomial to some
representative data. In any case, we can also note that the ambient
pressure $p_n$ should be time dependent. At least there should be some
12-hourly oscillations, as we can observe in the data, and we should
also add some noise to this term. The density of air ($\rho$) can
probably be assumed constant, as can the Coriolis parameter, which is
not a large term anyway. The values of the parameters $A,B$, which are
determined by the maximum wind speed and the radius at which this
occurs, will obviously change as the hurricane evolves, but this is
already pretty complicated so lets just ignore that.

## Ambient pressure

To investigate the ambient pressure, at each station, we look at the sea
level pressure during a 100-day period ending 10 days before the
cyclone. The mean pressures during this period for all the American
stations are in the range \[1014.3,1017.6\] with a mean of 1016.1hPa
over all the stations. The non-American stations had mean pressures
outside this range, between 1003 and 1010. These are station numbers: 23
(Philippines, Zeb and Megi), 24 (India, Hudhud) and 26 (Japan, Flo). It
might be a good idea to restrict the analysis to a single region (such
as American north Atlantic hurricanes).

All time-series show a definite 12-hourly oscillation (we can see from
the power spectrum), and the mean amplitude of the wave is found for
each series - all lie in the range \[1.43, 1.76\] and the mean value is
1.60. Besides a daily fluctuation, the pressure can also vary by at
least 10hPa over the course of 100 days, it would be a good idea to
impose some additional fluctuations - either a lower-frequency sine
wave, or some red noise - to model this. A reasonable function for the
ambient pressure might therefore be: $$
p_n(t) = 1016.1 + 1.6\sin\left(\frac{2\pi t}{12}\right) + \gamma W(t),
$$ where $W(t)$ is Brownian motion and $\gamma$ is a
constant to be determined.
