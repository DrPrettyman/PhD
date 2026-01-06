This report is a condensed summary of the author's notes so far, and
includes some preliminary results.\
For brevity's sake, the terms:

- "the autocorrelation function (ACF) of a time series"

- "the ACF of dynamical system $X$"

- "the ACF of parameter $P$"

are variously used to mean "the autocorrelation function of a time
series produced by measuring a parameter ($P$) of dynamical system $X$".

# Abstract

The project intends to create a multi-purpose tool to predict a
bifurcation or catastrophe in a dynamical system given time series data
as input. The proposed method involves analysing auto-correlation, noise
and trends in the time series.\
The case of an approaching tropical cyclone -- studying sea level
pressure and wind speed time series -- has been investigated. Results
are preliminary but do suggest that a deeper analysis may lead to a
cyclone being visible through inspection of the correlations in the time
series before it is obviously visible (i.e. pressure drops and wind
speed rises).

# Summary

## Reading Around The Problems

The project, as far as I had it in my own mind, was to investigate
indicators of regime-shift or bifurcation in a system. Here I give a few
examples:

- In (livina2011) the climate (from Pliocene to present) is modelled
  using a conceptual, stochastic potential well system. It is then
  possible to look for trends in the changes of the shape of the system.

- In (held2004) and (livina2007), **degenerate fingerprinting** is
  used to detect changes in the decay rates of fluctuations in a time
  series (using ACF[^1] and DFA[^2] resp.). It is broadly conjectured or
  accepted that a decline in the decay rate of the principal mode of a
  potential-well-style system predicates a bifurcation.

In the literature there are open problems posed, such as predicting a
future bifurcation *with a time limit* rather than retrospectively
noticing that something happened just before the bifurcation. It seems
that when an indicator or an EWS[^3] is used, and is successful --and
here we may define success as the indicator rising or falling fairly
soon before the bifurcation event takes place-- there is rarely mention
of exactly *how soon* before.\

## The Perfect Outcome

The outcome of the "perfect project" would, for me, given what I
understand the problem to be, a multi-purpose time series regime-change
predicting tool.\
This **Perfect Multi-purpose Tool** would take a time series and tell
the user whether or not the system that produced the series will undergo
a bifurcation (or, even better, any more general sort of regime change
-- see (ashwin2012)) in the near future. And, if so, how long will we
have to wait to see the change.\

# First things: Basic Ideas

## Basic Stochastic Dynamical Systems

At the start of the project I encountered the basic idea of a system
with a **double well potential**. This comes up in (livina2011). A
system such as

$$


\dot{z}(t) & = -(z^4 - 2z^2)' + \sigma(t)\eta \\
\sigma(t) & = -0.00007t+1.50045

$$

starts at time $t=0$ with a very large noise term $\sigma$ so that the
system jumps all the time between the two wells at $z = \pm 1$. As
$\sigma \rightarrow 0$ the system settles into only one of the states,
and it is unlikely to "jump out" within finite time.\
If you use some initial value for $z$ and look at a time series
$[z(t)]_t$ you could say that the system changes in its nature at the
point where "jumps" become noticeably less frequent.\
In (livina2011) some types of system changes are identified:

1.  A forced transition, where the potential function stays the same
    shape, but is moved, so that there is a trend in the time series.

2.  A noise-induced transition, where the system "jumps" from one well
    to another.

3.  A genuine bifurcation, where the shape of the potential function is
    changed.

It seems that the example in Eqn.
[\[noise_wells\]](#noise_wells)
 is of the third type, fundamentally, since it
is indistingushable from a constant-noise system where the thing changes
shape so that the wells become deeper and steeper, something like Eqn.
[\[steeper_wells\]](#steeper_wells)
, the values of $\alpha$ and $\sigma$ can be
determined to give the same dynamics as the decreasing-noise system.

$$

\dot{z}(t) & = -\alpha t(z^4 - 2z^2)' + \sigma\eta
$$

It is often the case, when looking at this sort of things, that examples
will be of a different nature -- where the number of wells increases or
decreases.

## Basic Ways of Predicting

There is an idea encountered in several papers (e.g. (held2004),
(livina2007)) that the autocorrelation function of a time series can
provide an early warning signal for changes to the underlying dynamical
system. Possibly the change in autocorrelation will be easily
perceptible before it becomes obvious from simply looking at the time
series that there is a change.\
It is also worth studying other functions of the time series, whether
related to the ACF or not, which may make obvious information otherwise
hidden in the noise. Indeed the nature of the noise itself may well
change as the system changes, although it is impossible to decide what
is noise and what is signal when dealing with physical systems.

### Finger printing -- ACF

The first example of a EWS indicator studied is that of ACF, the
auto-correlation function. In (held2004) the ACF (lag-1) is calculated
in a sliding window. An increase in the ACF signal indicates that a
bifurcation is happening. With something like the system in Eqn.
[\[noise_wells\]](#noise_wells)
 this is certainly the case, because the data
becomes less noisey, more correlated, when it stops jumping about all
the time. The rising trend is clearly visible long before the decrease
in noise is obvious.

### Finger printing -- DFA

(livina2007) introduces Detrended Fluctuation Analysis, which is
discussed in detail in (kantelhardt2001). The idea is similar to the
auto-correlation method in (held2004). The method will produce, for a
time series input, a number $\alpha$ which is the "bifurcation
indicator".\
The analysis requires a five-step method:

1.  Determine the "profile" $Y$, which is the cumulative sum of the time
    series.

2.  Divide the profile $Y$ into non-overlapping segments of length $s$,
    there will be $\lfloor N/s \rfloor$ such segments

3.  In each segment, detrend the profile by subtracting the order-$n$
    polynomial fit. This gives the *detrended* profile $Y_s$.

4.  In each segment, calculate the variance of $Y_s$, call this $F_s$.
    Then calculate
    $$F^{(n)}(s) = \sqrt{ \frac{1}{\lfloor N/s \rfloor} \sum F_s}$$

5.  (kantelhardt2001) states that $F^{(n)}(s) \propto s^\alpha$. Thus,
    we do the above four steps for a range of $s$ values, then fit an
    exponential to get a value for $\alpha$.

### Mann-Kendall coefficient

The Mann-Kendall coefficient $S$, of a single time series, is a measure
of auto-correlation.

$$
S = \sum_{i = 1}^{n-1} \sum_{j = i+1}^{n} \text{sign}(x_j - x_i)
$$

The coefficient may be useful in identifying trends in the data
((yue2002)).

### Potential Analysis

In (livina2011) the system producing the time series is modelled by
estimating the shape of its potential function. Observing a trend in the
shape-changing of the potential gives you some predictive power. For
example, if it appears that the sides of the well are getting steeper,
you may suggest that they will continue to get steeper, and make jumps
less likely. This is like suggesting that a dice has become weighted
because it has produced a long run of sixes, and thus predicting that it
will only ever roll sixes again.

## Modelling

Modelling a system may be very useful. I mean a stochastic, abstract
model, not a fluid-dynamics physical model.\
We can progress a particle along a trajectory, with some constraint,
such as the double-well model in Eqn.
[\[steeper_wells\]](#steeper_wells)
. A vital part of the model is the noise term,
since without noise there would be predictability, and Epicurus tells us
that the universe is inherently unpredictable. But what kind of noise?
Is there more to noise than mere white noise? Ah ha! There is so much
more! One can do all kinds of things to a boring white-noise signal.
Using the basic signal you can create an AR(1) process, an MA(1)
process. You can combine the methods to make an ARMA process, or even an
ARIMA, or FARIMA process. You can shift the Fourier transform of the
white-noise signal then Inverse transform to get pink, red, purple
noise. You can sum it up to get Brownian Motion, then you mess about and
get Fractional Brownian Motion.\
There are many variations but how can you parametrise a general FARIMA
process? It is surely not possible! The best you can do is to identify
the colour of the noise by fitting an exponential to its power-spectrum
signal.

# Tropical Cyclones - Ideas

Tropical cyclones are a good example of something happening. Looking at
the sea-level pressure in one location, all is fairly constant, then
suddenly there is a drop.\
Maybe this drop in pressure can be predicted from only the pressure time
series. One would expect that there might be a build up of correlations
before the event. The reason for thinking so is that the cyclone
*approaches*, rather than suddenly appearing from nowhere. In fact, any
sort of physical event is likely to share this feature.\
It is possibly not unreasonable to expect that an indication that the
event is approaching is detectable before the event is detected. That
is, that the outcome of a sophisticated analysis of the data will reveal
something such as "indicator $\beta$ becoming greater than $0.95$"
before it is possible to say "the pressure has decreased more than would
be expected by random chance, indicating that a storm system is close
by."\
The analogy to a double well potential two-state system is not at all
obvious here, as it is in the hot-Earth/ice-age example in
(livina2011). It fact this may not provide any analogy at all. However,
the time series look superficially similar, and this is also true of
many economic and physical systems where sudden catastrophe occurs.

## Things to look for

Armed with only a very basic idea about cyclones, I will proceed.\
The cyclone is very big. If a butterfly can affect the weather on China
then it stands to reason that a cyclone will affect the weather of
things a few hundred kilometres away. However, whereas the wings of the
butterfly will only add a very small noise term, the cyclone will surely
add something much larger, especially to things that are close. Maybe it
will add a white-noise term, maybe it will add some other noise, maybe
it will add a deterministic trend (other than the very-steep-drop trend
that happens when the cyclone has already arrived).\

### Options - Which cyclones?

So we have some options. First, we have the option of where to look
(geographically):

1.  Do we look at a large area with many data points, possibly
    artificially gridded, and combine?

2.  Do we look at individual weather stations with raw data?

3.  Do we look only at stations that are within distance $d$ of the
    centre of the cyclone? What is $d$?

4.  Do we look at only places where a category 5 cyclone occurred?

5.  Do we look at points in the ocean, on the coast, or inland?

6.  Do we look at many cyclones in one area (for example, East-coast
    USA)? Or at many examples across the world? The dynamics of Asian
    cyclones formed in the Pacific may be different from USA cyclones
    (called hurricanes).

Of course, our choices may affect the conclusions. In fact, they will
very surely affect the conclusions.\

### Options - Which data?

We also have the option, which data to use?

1.  Do we look at data spread over an area, or from one station?

2.  Do we look at pressure, wind-speed, wind-direction, rain-fall, etc.?

3.  Do we look at on field, or do we look at e.g. pressure and
    wind-speed, or many fields?

4.  If we look at many fields, how do we combine them?

## Using multi-dimension time series

It is probably a good idea to look for signals in the multi-dimensional
data which combines **slp**[^4], wind-speed, and possibly other fields.
All the time series combined will provide more information that just
slp.\
However, it will become nonsensical to look at every possible field.
Even with two or three or four it will be difficult to identify what we
want to look for, and many of the fields may be strongly correlated.\
So we have two tasks:

1.  Decide which fields to use, or how to distil many time series into a
    manageable number (for example, using PCA[^5]).

2.  Decide how to analyse the multi-dimension (hopefully just 2D). What
    to look for? How to detect a change point in many dimensions?

# Tropical Cyclones - Investigation

## Data

For this investigation, the HadISD dataset was used. The time series for
the slp data is taken from a single station, as close as possible to the
center of the cyclone at the point that the cyclone 'makes landfall'.
The **annoying oscillations** were also removed from the slp time
series.

## First inspection

The first thing was to get some slp data from an area where a large
cyclone had occurred. One of the very largest cyclones of recent years
is Hurricane Katrina (USA, 2005). The 1D time series of pressure data
was given the sliding-window ACF lag-1 treatment, which gave a
convincing picture of the ACF rising significantly about two days before
the large drop in pressure occurred (when Katrina passed through the
location), and reaching a peak value just before the drop. This is a
similar picture to over sliding ACF studies of time series, e.g.
(held2004).\
Then I looked at Hurricane Andrew. Andrew formed in the Atlantic and
passed over the Caribbean at it's peak intensity, unlike Katrina which
formed in the Caribbean and was at it's strongest over the southern USA.
Andrew does the opposite to Katrina: the ACF signal *decreases*
significantly over exactly the same time periods that it *rises* for
Katrina. Several other storms have been analysed in the same way, but
none show such obvious increases or decreases as Katrina and Andrew.
Some rise, some fall and some show very little change.\



   Caribbean    Atlantic
  ----------- -------------
    Katrina      Andrew
     Rita         Floyd
    Charley    Frances (?)

Most tropical cyclones happen in disparate places and under different
circumstances, it is therefore difficult to classify them. A subset of
the cyclones occur in or near the Caribbean sea and have had an effect
on the southern USA. These may be classified according to their paths.
Those that start in the Caribbean all travel west then north or
north-east and land in Louisiana or the west coast of Florida. Those
that start in the mid-Atlantic all travel north-west and land in Florida
or (occasionally) further up the US east coast.\
The most useful way to classify the cyclones will probably be by whether
they are at or past their peak intensity at the moment they land on the
coast.

## The annoying oscillations

In the HadISD dataset the slp data (for any location, any time of year)
has very clear 12-hourly oscillations. These, I expect, are to do with
the moon, since tides also come in 12-hour cycles. How to get rid of
these? Maybe by **de-seasonalising**, i.e.

$$
x_i \longrightarrow x_i - \text{mean}\left( [x_{i+12k}]_{k = 0, \pm 1, ...} \right)
$$

but this is not such a great method. In fact this method may create or
remove trends in the data, if the oscillations are 24-hour or 120-hour.\
If we continue to use these data, it will be important to agree a
reasonable method of detecting and removing these oscillation, because
they will significantly impose upon the correlation structure.

## Aggregating the time series

Following (citation) we have experimented with aggregating the
time series. That is, to aggregate $k$ data points we replace the series
$[x_i]_1^N$ with the series $[y_i]_1^{\lfloor N/k \rfloor}$ where

$$
y_i = \sum_{j=1}^k x_{k(i-1)+j}
$$

Since this makes the series $k$-times shorter, we have much less data to
work with. Accordingly, when calculating in a given window we must
reduce the length of the window in terms of the number of data points to
keep the window the same length in terms of actual time.\
This technique somewhat amplifies the affect of applying the ACF
fingerprinting method, but does not change the conclusion. Aggregating
in this way will not give us any new information, but may make it easier
to spot a pattern in the autocorrelation.

# Results

So far, some preliminary results have been obtained. The data from the
HadISD data set have been used, selecting times and locations to
correspond with certain large tropical cyclones, listed in section
[4.2](#first-inspection)
.\

## Simply looking into the auto-correlation

The ACF lag-1 of the sea-level pressure is calculated in a sliding
window of 120-240 points. In some cases we see an expected rise
((livina2007)) in the value just before the cyclone event, however in
other cases the value does not rise, see figure
[1](#Charlie_and_Andrew)
. It is not sensible to draw any
conclusions regarding the use of the ACF as an early warning signal. The
DFA method yields very similar results.\

![slp data for hurricanes Charlie and Andrew (left) and the ACF of this
data measured in a 240-point sliding window. Contrast the rising ACF for
Charlie with the steep decrease for
Andrew.](../images/CharlieandAndrew.png){#Charlie_and_Andrew


Despite this discouragement, the autocorrelation does appear to be
worthy of further study. The sliding ACF (as shown in figure
[1](#Charlie_and_Andrew)
) was calculated for many cyclones and
for many windows of data where no cyclone occurred (or occurred shortly
afterwards). In the cyclone time series, the ACF had much larger
variances and lower means than in the control. Therefore, the ACF does
in some way give an indication of whether a cyclone may be approaching.

## Measuring the noise

The time series is treated as a noise signal and the 'colour' is
calculated using a fit to obtain the scaling exponent of the power
spectrum. We have not speculated on the usefulness of the result, but
there appears to be a small increase in the scaling exponent which
begins $\approx 50$hours before the cyclone is visible in the time
series. This is present in most, but not all, cases and is indeed the
case in the mean.

# Other Ideas and suggestions

Besides the work done to obtain the results shown in section
[5](#results), there have been
attempts to follow other paths.

## Multi-dimensional tool

There was a suggestion to use gridded data, possibly from a reanalysis,
and then to develop a tool to analyse this multi-dimensional data. There
was also a suggestion to use more than one parameter, we have so far
only looked at sea-level pressure, but wind-speed, precipitation,
wind-direction and other data is readily available.\
In (williamson2015), a technique is developed to detect a bifurcation
in a system given two or three time series (i.e. the $x$, $y$ and $z$
components of the Lorenz 96 attractor). The method introduces a 2 or
3-dimensional version of the basic ACF estimator, which is an
$n\times n$ matrix (for $n$ dimensions), and then attempt to identify a
trend in the eigenvalues. It is unclear, however, what this matrix is an
estimator for, and whether it is a good one.\
The method used in (williamson2015) was implemented and used on the
real data for Hurricane Katrina, with both slp and wind-speed as inputs.
The results did not appear to tell us anything. This method may also
require significant work if it to work with *non-idealised* systems. It
is also not obvious to what extent the definition of a "coupled system"
is analogous to the atmosphere, or which atmospheric components one
would have to look at to appreciate the analogy.\
PCA[^6] was used to condense the gridded data in to a 1-D time series.
This approach appeared potentially useful and should be tested further.
PCA was also used to condense the slp/wind-speed system into a 1-D time
series, this was done for four different cyclone data sets. However,
this did not give any useful insight since nearly all the variation
($>90\%$) in the 2-D series was contained in the slp data anyway. It was
concluded that more of an insight into the physical system is needed to
determine which fields may be useful, but this method will potentially
be very useful.

# What next for the Cyclone project?

There are several important decisions facing the project, and several
tasks to complete:

- More than one dimension of the data must be taken into account.

- A multi-dimensional approach taking data from dispersed (possibly
  gridded) locations must be agreed upon.

- A stochastic model of the system is required.

- We must decide which cyclones to study, and which fields of the data
  to look at.

- We must decide what we are asking of our method (i.e. what is the null
  hypothesis)

## Making a model

There is a need to build a stochastic model of the approaching-cyclone
time series. This will probably be an ARMA model, but will have to be
parametrised somehow by studying the few cases of real cyclone data that
have been collected.\
The suggestion is to use the model to generate many time series, and
then to see if they realistically represent the system. Once the model
is tuned in this way, we may begin to decide which parameters are
important, and then examine whether these fields can provide a basis for
an early warning signal.

## The significance of the Null Hypothesis

We must decide what question we want to ask of our method:

1.  Will there be a cyclone?

2.  Will there be a cyclone in the next \[three days\]?

3.  Given that we know there will be a cyclone in the next \[ten days\],
    will there be a cyclone in the next \[three days\]?

4.  Given that we know there will be a cyclone in the next \[ten days\],
    when will the event happen?

[^1]: Auto Correlation Function

[^2]: Detrended Fluctuation Analysis

[^3]: Early Warning Signal

[^4]: Sea-level pressure

[^5]: Principal Component Analysis, also called EOF Analysis, because of
    the term "Empirical Orthogonal Functions".

[^6]: Principal Component Analysis
