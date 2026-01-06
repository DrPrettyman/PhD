# notes from discussion with Tobias

In (williamson2015) the aim (so far as the 1D ODE is concerned) is to
estimate the parameter $a$ assuming that a system is described by an
equation $$
x_{n+1} = ax_n + c + \varepsilon\eta
$$ where $a$, $c$, $\varepsilon$ are parameters and $\eta$
is guassian noise. For this they propose $$
a = \frac{E(x_{n+1}x_n) - \mu^2}{E(x_n^2)-\mu^2}
$$ where $\{x\}_n$ is a time series, which probably means
$$
a = \frac{\overline{x_{n+1}x_n} - \overline{x_n}^2}{\overline{x_n^2} - \overline{x_n}^2}
$$ and is just the lag-1 autocorrelation of the series.
Tobias reckons there must be a better way to estimate $a$, and also $c$
and $\varepsilon$. look into maximun likelyhood estimation, also see
(BoxJenkinsBook).\
Also, in (williamson2015) the first 2D system considered doesn't have
an attracting point, it has concentric stable orbits and so a solution
does not get "very close" to the fixed point, depending on your
definition of 'very close'. To linearise about this fixed point is
therefore not good form. It would certainly be a good idea to try the
method with more examples, I already tried this with the Lorenz
butterfly attractor.\
Tobias talked about this $x_{n+1} = ax_n + c + \varepsilon\eta$ system
and how it would be good to estimate $a$, $c$, $\varepsilon$ from this
system if $a$ is slowly changing, rather that jumping. In particular,
you cannot predict that $a$ will change in the future but can you say
with confidence that $a$ is changing? then you can predict that it will
continue to change.\
We also discussed the double-well potential system. my notes follow:

- More frequent changes of state, or a change of state where one has not
  been seen before, may be an early warning signal for a change to a
  single-state system. i.e. might imply that the centre "hump" is
  getting lower and easier to jump over.

- Or maybe the opposite, if you can see that the shape of the well is
  changing to a one-state system (e.g. you may see that the variance is
  increasing or that the data is more skewed as one side of the well
  gets less steep) then you may predict that a jump will happen soon.

# notes from discussion with Valerie

Valerie recommends using the method in (williamson2015) on some real
data. Preferably mslp, sst or wind-speed data before and during a
hurricane. either use two or three of these variables at a chosen grid
point and use this (williamson2015) parameter estimation method which
"attempts" to linearise the underlying meteorological dynamical system
by looking at the 2/3D time series data.\
Alternatively, try to take several grid points around the hurricane area
and examine, say, mslp at every point, these give you a high dimensional
system. It is unclear how this would work, but I suggest using Principle
Component Analysis (PCA) to reduce the dimension of the system, then you
have a, say, 3D system to look at. Or, use PCA dimension reduction for
mslp to get a 1D system in this variable and also for wind-speed/sst so
you have a 2/3D system which hopefully captures much of the variance in
the whole region.
