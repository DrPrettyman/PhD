# Overview

The project intends to create a multi-purpose tool to predict a tipping
point (critical transition) in a dynamical system, specifically a
geophysical system, given time series data as input, both in
one-dimensional systems and in higher dimensions.

# Introduction to tipping points

This project is concerned with tipping points, or critical transitions
(lenton2008; @scheffer2009), in dynamical systems, and methods that
enable us to predict these. (livina2011) identifies three types of
system changes which may be the cause of a tipping event:

1.  A forced transition, where the potential function stays the same
    shape, but is moved, so that there is a trend (or possibly a sudden
    jump) in the time series.

2.  A noise-induced transition, where the system shifts from one stable
    state to another due to a large initial perturbation.

3.  A genuine bifurcation, where the shape of the potential function is
    changed.

Given a set of time series data (e.g. a measurement variable of a
physical system or computational model) where a transition or
bifurcation has occurred, we wish to detect an Early Warning Signal
(EWS), which should be measurable before the tipping point. This EWS can
then be used to predict future tipping points.

The authors of (livina2011) study a system such as $$


\dot{z}(t) & = -(z^4 - 2z^2)' + \sigma(t)\eta \\
\sigma(t) & = -0.00007t+1.50045

$$ where a double-well-potential system effectively becomes a
single-well system as the noise term becomes so small that it is
practically impossible for the system to change state. Note that the
noise term $\sigma(t)\eta$ is integrated over $t$. In section
[4.2](#sec_pitchforkdata)
 we study a system with a genuine
'pitchfork' bifurcation, we also note the test of EWS on artificial data
made from the concatenation of several short time series with different
noise structures (livina2012). Thus, there are many possible time
series on which the EWS may be tested.

# Analytical derivation of one-dimensional EWS

(dakos2008) lists several EWS techniques which have been attempted:
analysis of spectral properties (kleinen2003), degenerate
fingerprinting (held2004) and a modification of Detrended Fluctuation
Analysis (DFA) (livina2007).

A key concept involved in these methods is that of resilience or
recovery rates (scheffer2001; @dakos2012), that is, how quickly the
system returns to the stable state having received a small perturbation.
The theory states that the recovery rate will slow down as the system
approaches a bifurcation point (scheffer2009), known as critical
slowing down. As an example we take the system in equation
[\[fork_system\]](#fork_system)
: $$
\dot{z}(t) & = -\frac{\partial}{\partial z}(z^4 + \left(3-t\right)z^2) + \eta_t

$$ where $\eta_t$ are independent and Gaussian. This system
is trapped within a single well of attraction (at $z=0$) for $t\leq 3$,
at $t=3$ a bifurcation occurs creating a double well potential system
for $t>3$. The shape of the potential at $t=0$, $t=2$ and $t=3$ is shown
in figure [1](#three_shapes)
. Intuitively, the system will take longer to
return to the $z=0$ equilibrium, following a small perturbation, as the
sides of the potential well become less steep. The hypothesis is that
this critical slowing down will be seen in a wide variety of dynamical
systems approaching a bifurcation.


![](../../notes/images/three_potential_function_shapes.png)
Showing the shape of the system potential of the system in
equation 
[fork_system] at 
t = 0, 2, 3. The sides of the
potential well become less steep as the system approaches the
bifurcation.


(vannes2007) test this hypothesis with a number of ecological models
and find that the intensity of the critical slowing down effect is
linearly, or almost linearly, related to the distance from the tipping
point in all cases.

## Degenerate fingerprinting: autocorrelation

The use of autocorrelation as an EWS is justified by modelling a
dynamical system using a one-dimensional autoregressive system:
$$
y_{n+1} = e^{\kappa\Delta t}y_{n} + \eta_n
$$ (held2004; @scheffer2009). Where $\eta_n$ are independent
and Gaussian, the state $y_n=0$ is the equilibrium. The system returns
to equilibrium exponentially with rate $\kappa$ (the decay rate). If we
simulate critical slowing down by decreasing $\kappa$, the
autocorrelation coefficient $\alpha \equiv e^{\kappa\Delta t}$
increases, $\alpha\xrightarrow[\kappa\rightarrow 0]{}1$. It is also
shown that as the autocorrelation increases so does the variance, thus
detecting an increase in variance provides another EWS.

(held2004) use this observation to argue that in a multi-dimensional
system one should project onto the first EOF (the basis vector for which
the variance of the system is maximised) as this is the one-dimensional
basis in which the rise in autocorrelation (and also variance) will
occur. We note that the basis in which the variance is maximimal may not
be the same as the basis in which the variance is increasing. At least,
this is not immediately obvious a priori and may be wanting further
investigation. An investigation of this is an ongoing project. In some
dynamical systems it may be that while autocorrelation rises before a
tipping point, variance does not (gsell2016), this property may also
provide fruitful investigation.

The autocorrelation of a one-dimensional time series
$X=\{x_k\}_{k=1}^{N}$ is estimated using the autocorrelation function
(ACF) formula: $$

\text{ACF}_{l}(X) = \frac{1}{(N-l)\sigma^2}\sum_{j=1}^{N-l}(x_{j}-\mu)(x_{j+l} - \mu)
$$ (held2004), where $l$ is the lag and $\mu$ and $\sigma$
are the mean and standard deviation of the series, it is likely in
applications that $\mu$ and $\sigma$ are also estimated from the data,
using the standard formulae. Other measures of autocorrelation such as
the Mann-Kendall coefficient may be used (yue2002).

The rise in ACF --the "fingerprint" of the bifurcation-- is detected by
calculating the ACF of a segment of the time series, say
$\{X_i\}_{i=m-k}^{m}$, then sliding this window by one point ($m-k+1$ to
$m+1$) and calculating the ACF of this new time series segment.

As an exercise, say $$
x_n &= \phi x_{n-1} + \eta_n\\
&= \phi^n x_0 + \sum_{i=0}^n \phi^i\eta_{n-i}
$$ then from the ACF$_l$ formula
[\[eqn_ACF_formula\]](#eqn_ACF_formula)
 we have $$
\text{ACF}_{l}(X) =& \frac{1}{(N-l)\sigma^2}\sum_{j=1}^{N-l}\left[x_jx_{j+l} - \mu x_j - \mu x_{j+l} + \mu^2\right]\\
=& \frac{1}{(N-l)\sigma^2}\sum_{j=1}^{N-l}x_jx_{j+l}\\
&+ \frac{-\mu}{(N-l)\sigma^2}\sum_{j=1}^{N-l}(x_j + x_{j+l})\\
&+ \mu^2/\sigma^2
$$ Concentrate on the first part, $$
\sum_{j=1}^{N-l}x_jx_{j+l} = \sum \phi^{2j+l}x_0^2 + \phi^jx_0p_{j+l} + \phi^{j+l}x_0p_{j} + p_{j}p_{j+l}
$$

And so on. This is done elsewhere.

The real problem is knowing which lag to use. possibly it would be a
good idea to use a combination of many lags to create a function such as
$$
F(X) = \text{ACF}_1(X) + \frac{1}{2}\text{ACF}_2(X) + \frac{1}{3}\text{ACF}_3(X) + \dots
$$ but this is just a guess. What would it mean to combine
the differently lagged functions?\
How does the lag relate to the supposed Critical Slowing Down (CSD)? We
know that the classic stationary-system example predicts a shift from
short-term memory (white noise) to long-term memory (AR(1) process) as
the bifurcation is approached. We want to detect this. Possibly we
should measure the relative sizes of small-lag and large-lag ACF values,
such as $$
F(X) = \frac{\text{ACF}_1(X)}{\text{ACF}_2(X)} + \frac{\text{ACF}_2(X)}{\text{ACF}_3(X)} + \frac{\text{ACF}_3(X)}{\text{ACF}_4(X)} + \dots,
$$ but again, this is a guess for now.

Say we have an AR(1) process and an AR(2) process described by
$$
X_1: ~~x_n &= \phi_1 x_{n-1} + \eta\\
\text{and~~} X_2: ~~x_n &= \phi_1 x_{n-1} + \phi_2 x_{n-2} + \eta
$$ resp.. We can calculate the ACF of each using different
lags, $$
&ACF_1(X_1) = \phi_1 &&ACF_2(X_1) = \phi_1^2\\
&ACF_1(X_2) = \frac{\phi_1}{1-\phi_2} &&ACF_2(X_2) = \frac{\phi_1^2}{1-\phi_2}+\phi_2,
$$ note that these are expected values. In fact we find that
this is quite simple: $$
ACF_l(X_1) &= \phi_1^l\\
ACF_l(X_2) &= \phi_1 ACF_{l-1}(X_2) + \phi_2 ACF_{l-2}(X_2)\\
\text{even~~} ACF_{l}(X_k) &= \sum_{j=1}^l ACF_{j}(X_k)
$$ probably there's a way to formulate a closed form that has
already been done.

Anyway, the original motivation for using ACF was the idea that we have
a ball in a potential well, moving around with random noise, as the well
gets shallower the perturbations get larger and therefore the ball takes
longer to return to the bottom of the well. These longer return times
imply an increase in ACF$_1$.

So with this in mind, maybe let's model it with an actual well-potential
system. Does this imply that we should take higher-laged ACF into
account?

## DFA

Detrended Fluctuation Analysis (kantelhardt2001) is used by
(livina2007) as an EWS, similarly to autocorrelation. Taking time
series data $X$ of length $N$, the DFA method involves calculating $Y$,
the cumulative sum of $X$, splitting this into $\lfloor N/s \rfloor$
non-overlapping segments $Y_{(j)}$ and in each segment 'detrending' by
subtracting an order-$n$ polynomial fit $p_n(Y_{(j)})$: $$
y_i &= \sum_{k=0}^{i}x_k~~i=0,\dots,N\\
Y_{(j)} &= \{ y_{js}, y_{js+1}, \dots, y_{(j+1)s-1}  \}~~j=0,\dots,\left\lfloor \frac{N}{s} \right\rfloor-1\\
\overline{Y}_{(j)} &= Y_{(j)} - p_n(Y_{(j)})
$$ Given these detrended segments $\overline{Y}_{(j)}$, the
formula in equation [\[DFA\]](#DFA)
 gives the $s$-dependent fluctuation coefficient
$F^{(n)}(s)$: $$
F^{(n)}(s) = \sqrt{ \frac{1}{\lfloor N/s \rfloor} \sum_{j=0}^{\lfloor N/s \rfloor-1} \text{Var}(\overline{Y}_{(j)})}.

$$ Using the relation $F^{(n)}(s) \propto s^{\alpha_n}$, we
can perform the algorithm with many values of $s$ to arrive confidently
at a value for $\alpha_n$. This value, which we will call
$\text{DFA}_n(X)$, is used as an EWS in the same way as the ACF
coefficient. In fact, (kantelhardt2001) plots $F(s)/\sqrt{s}$ over $s$.
There is also a modified DFA method mentioned.

## Power Spectrum

Spectral properties of the time series may also be used as indicators
(kleinen2003), in particular the scaling exponent of the power
spectrum. The use of spectral properties as an EWS will be useful when
the tipping point is associated with a change in the structure of the
noise, or the stationary system becoming non-stationary. However, a
shift from a dominance of short-scale memory to long-scale memory, seen
in the measurement of the power spectrum scaling exponent (PSE), will be
associated with a rise in autocorrelation, and so in this respect the
PSE and the ACF are related.

# Scaling indicators, noise and ARIMA models

## Scaling exponents

We note that scaling indicators such as ACF, DFA and the PS exponent
only capture so much information about a time series. These methods are
effectively attempting to fit a model to the data. In particular, using
the ACF(1) indicator is an attempt to model the time series as an AR(1)
process, it is not necessarily effective if the structure of the noise
is significantly different from an AR(1) process.

See Taqqu papers on FARIMA models. G.E. Box is obviously a good source
(BoxJenkinsBook). Also, see (govindan2003) on estimation of power-law
exponents using ACF and DFA. Also, see (makse1996) for generating
long-range correlated data.

## ARMA Models

Notes taken from (BoxJenkinsBook). The ARMA process could be given by:
$$
\Phi(B)\tilde{z}_t = \Theta(B)a_t
$$ where $\Phi$ and $\Theta$ are polynomial operators of
degree $p$ and $q$ resp., recall $B$ is the backward shift operator. For
a simple AR1 process we might have something like
$\Phi(B) = 1 - \frac{1}{2}B$ and $\Theta(B)=1$, the process then being
defined by $$
z_t = \frac{1}{2}z_{t-1} + a_t.
$$ For a simple MA2 process we might have, for example,
$\Phi(B) = 1B$ and $\Theta(B)=1 - \theta_1B - \theta_2B^2$, the process
then being defined by $$
z_t = a_t - \theta_1 a_{t-1} - \theta_2 a_{t-2},
$$ or something like that. To ensure stationarity the roots
of $\Phi(B)=0$ must lie *outside* the unit circle. If they lie *inside*
then the whole thing blows up. If they lie *on the circle* we get the
good kind of non-stationary process that can model stuff. Maybe $\Phi$
has *lots* of roots, in which case we might want for some of them to be
on the circle and the rest outside. (When I say on the circle I mean
$=1$ for the moment, wait until chapter 9 says Mr. Box). Thus (cf root
= 1) we can write an ARIMA process in the form: $$
\Phi(B)(1-B)^d z_t = \Theta(B)a_t,

$$ this defines an ARIMA$(p,d,q)$ process where $p$ and $q$
are the orders of $\Phi$ and $\Theta$ as before and now we have $d$ as
well.

The general ARIMA process in Eqn.
[\[generalARIMA\]](#generalARIMA)
 can be also expressed as: $$
z_t &= a_t + \psi_1 a_{t-1} + \psi_2 a_{t-2} + \psi_3 a_{t-3} + ...\\
&=  \Psi(B)a_t
$$ Because $z_t$ is in terms of $\{z_\tau\}_{\tau<t}$ and
$\{a_t, a_{t-1}, ...\}$ but $z_{t-1}$ is in terms of
$\{z_\tau\}_{\tau<t-1}$ and $\{a_{t-1}, a_{t-1}, ...\}$, etc. so $z_t$
can be written in terms of $\{a_{t-j}\}_{j=0}^\infty$. This may be no
good if you don't have an infinite white noise series, so instead use a
truncated form, which is given in (BoxJenkinsBook)(section 4.2.2).

We can also have an "inverted form" of the model where we do the
opposite to above and represent $z_t$ in terms of
$\{z_t-j\}_{j=1}^\infty$ and a single random shock $a_t$, but we don't
really need the $t$ subscript: $$
\pi(B)z_t &= \left(1-\sum_{j=1}^\infty \pi_j B^j\right) z_t = a_t\\
&\Rightarrow z_t = \sum_{j=1}^\infty \pi_j z_{t-j} + a_t
$$ In a model, where $\Phi$ and $\Theta$ have been defined,
we can substitute the above $\pi(B)z_t=a_t$ into Eqn.
[\[generalARIMA\]](#generalARIMA)
 to get: $$
\Phi(B)(1-B)^d = \Theta(B)\pi(B)
$$ and equate coefficients of $B$ to get the values of the
$\pi_j$.

## FARIMA

You can simulate Brownian motion using the *Random Midpoint Displacement
Method* (PeitgenBook) which is given here:

1.  set $X(0) = 0$ and $X(1) = \texttt{randn}$

2.  set $X(\frac{1}{2}) = \frac{X(0)+X(1)}{2}+D_1\texttt{randn}$

3.  set $X(\frac{1}{4}) = \frac{X(0)+X(1/2)}{2}+D_2\texttt{randn}$ and
    $X(\frac{3}{4}) = \frac{X(1/2)+X(1)}{2}+D_2\texttt{randn}$

4.  etceteras

$\texttt{randn} \sim N(0,1)$ and the $D$'s are scaling factors
calculated such that the Brownian motion is self similar. For *Regular*
Brownian motion with Hurst exponent $H=0.5$ such that if we zoom in on
the Brownian timeseries by a factor of $2$ in the time direction and a
factor of $2^H = \sqrt{2}$ in the amplitude, we also see regular
Brownian motion. In this case we can note that $X(1) \sim N(0,1)$ so if
we zoom in we want $$
\sqrt{2}X(\frac{1}{2}) \sim N(0,1).
$$ That is, we want $$
\text{Var}\left(2^H X(\frac{1}{2})\right) &= 2^{2H} \text{Var}\left(X(\frac{1}{2})\right) \\
&= 2^{2H}\text{Var}\left(  \frac{X(0)+X(1)}{2}+D_1\texttt{randn} \right) \\
&= 2^{2H}\left[ \text{Var}\left(  \frac{X(1)}{2} \right) +  \text{Var}\left(D_1\texttt{randn} \right) \right]\\
&=  2^{2H}\left[ \frac{1}{4}\text{Var}\left(  X(1) \right) + D_1^2 \text{Var}\left(\texttt{randn} \right) \right]\\
& =  2^{2H}\left( \frac{1}{4} + D_1^2 \right)
$$ to be equal to $1$. Thus $$
D_1 = \sqrt{\frac{1}{2^{2H}} - \frac{1}{4} }
$$ We also find that $$
D_{k} = \frac{D_{k-1}}{2^H}
$$ for all $k>1$. So that's that. My understanding is that
if we just take the lag-1 difference of our Brownian series we get
Gaussian White Noise, in particular we get *fractional* Gaussian noise
if we start with *fractional* Brownian motion (that is we have
$H\neq 1/2$).

If we take the term-wise difference of the fractional Brownian walk we
get fractional Gaussian noise (FGN).

# Comparison of one-dimensional EWS methods

(livina2012) compare the performance ACF and DFA degenerate
fingerprinting methods on artificial data. The potential analysis method
(livina2011) is also used for comparison. The ACF and DFA methods are
tested of an artificial time series produced by concatenating several
series of increasingly correlated noise, from pure white noise to
Brownian motion. This is an example of a time series which experiences a
rise in autocorrelation simultaneously with a decrease in variance.

## Application to artificial data

## Model with a pitchfork bifurcation

Here we study the pitchfork bifurcation seen in the model of equation
[\[fork_system\]](#fork_system)
. The equation used here is on a different time
scale: $$
\dot{z}(t) & = -\frac{\partial}{\partial z}\left(z^4 + \left(3-\frac{t}{200}\right)z^2\right) + \eta_t

$$ so that the bifurcation occurs at $t=600$. Figure
[2](#pitchfork_plot)
shows 100 instances of this model plotted together. The noise is
sufficiently large that the two branches are not distinguishable until
at least $t=650$.

![[] 100 instances of the model
in equation [\[pitchfork\]](#pitchfork)
.](figures/one_and_many_timeseries.png){#pitchfork_plot


In figure [3](#ACF_all) we
plot the ACF$_1$ statistic (calculated using a 200-point sliding window)
for the 100 instances. We can clearly see a increasing trend in the mean
(dashed line), visible even at around $t=400$, but this is not so clear
for any individual time series. For example, in model run number 80
(picked out in black) there is an increasing trend very early ($t=250$
to $400$) but this is followed by a decreasing trend, before the
expected rise at $t=500$. Figure [4](#comparison)
 shows the mean, for all 100 time series, of the
ACF, DFA and PSE indicators. All show the expected rising trend before
the bifurcation, but we must note that in measurements of geophysical
systems it is not always possible to run 100 experiments in order to get
a useful EWS.

![[] The ACF lag-1 estimator is calculated for
100 model runs upto the point of bifurcation ($t=600$).
](figures/one_and_many_ACF.png)

![[] A comparison of the three
autocorrelation indicators discussed. In each case the indicators are
calculated for all 100 series, using a widow of 200 points, and then the
mean of all is taken as in Figure [3](#ACF_all)
. The scaling exponent and DFA coefficient have been
scaled linearly to fit on the same
axis.](figures/method_comparison.png)

# Application to real data

## Tropical Cyclones

We apply the one-dimensional EWS methods to sea-level pressure data time
series, it would also be good to apply these methods to some other,
similar data for comparison. (dakos2012) compare the results of
applying an ACF method to various geophysical time series of where
dramatic shifts can be seen. These methods are also used in biological
and palaeoclimate data (scheffer2001; @livina2011).
