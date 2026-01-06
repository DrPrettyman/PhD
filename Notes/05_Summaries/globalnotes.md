# Meetings with Valerie and Tobias

## 9$^{th}$ of Septemper 2015

We discussed 'Degenerate Fingerprinting' which gives an 'Early Warning
Signal'. The jist is that there is a change in the autocorrelation of a
time series when approaching a bifurcation. The autocorrelation ought to
decrease with increasing lag and the rate of this decrease is greater
when there is less memory in the series. In a completely memory-less
series the lag-1 autocorrelation is $\approx 0$. We expect that the
autocorrelation will increase if the series is about to change, this is
the 'early warning signal'.\
We did not discuss 'Potential Analysis' in details.\
I have written a note to myself: "The power spectrum is the Fourier
transform of the autocorrelation".\
We have agreed that I will:

- Write up everything each Friday that I have done that week. The
  write-up should be as if to explain to Tobias what Valerie has
  explained to me or what I have learnt otherwise.

- Send this to Tobias and Valerie.

- Go to NPL sometime and register there.

- Download and use xmgrace for plots.

- Use CITRIX to access my desktop at NPL remotely (after registering at
  NPL.

- Ask questions frequently.

## email from Valerie 29/09/2015

1.  For generating long-range correlated data, see for instance
    (makse1996).

2.  Also read about AR, ARMA and FARIMA models. Taqqu et al papers on
    FARIMA are good.

3.  This paper by Govindan et al may be useful in terms of estimation of
    power-law exponents using ACF and DFA: (govindan2003).

4.  As an exercise, generate artificial data as a sum of sine wave with
    period 365 (like daily geophysical data) and noise (first white,
    then red with exponent, let's say, 0.7). Apply deseasonalising to
    remove the periodicity by subtracting average "annual" cycle and
    estimate the exponent from the fluctuations using ACF and DFA.

## Meeting with Valerie at NPL (Tuesday 06/10/2015)

1.  Discussed Detrended Frequency Analysis (DFA). I have read
    (govindan2003), Valerie also recommends (kantelhardt2001) which
    has a more step-by-step explanation of DFA. DFA is used to estimate
    the exponent $\alpha$ of a signal.

2.  Discussed Power Spectrum (PS) and the Discrete Fourier Transform
    (DFT - `fft` in MatLab). The PS is the modulus of the Fourier
    coefficients ($\{\sqrt{c_i c_i^*}\}_i$ where the $c_i$ are the
    complex coefficients). The PS of a signal is used to estimate the
    exponent $\beta$: $\beta$ is the slope of the PS.

    - **Note:** See Numerical Recipes (www.nr.com) for discussion on how
      things like `fft` are coded. Also note that MatLab may store the
      Fourier transform in a way which must be considered when trying to
      code something such as the coloured noise generation.

3.  DFA, PS and ACF estimate the same things. To be precise, they
    estimate $\alpha$, $\beta$, $\gamma$ resp. but these three are
    related as follows: $$
    \alpha = 1 - \frac{1}{\gamma} & & \alpha = \frac{1+\beta}{2}
    
    $$

4.  Discussed coloured noise. I have been generating either pure white
    noise or a random walk. These are examples of coloured noise with
    exponents 0.5 and 1.5 resp.. Additionally, one may have noise with
    any other exponent, 0.7 for example. The DFA estimates the exponent
    $\alpha$.

    - One may create coloured noise (see (makse1996)), the principal
      being that you take white noise, the PS of which has slope $0$,
      thus yields $\beta =0$ when doing Power Spectrum Analysis (Thus
      $\alpha=0.5$, see equation
      [\[exponent_relationships\]](#exponent_relationships)
      reference="exponent_relationships"})

    - You tilt the white noise DFT in the Fourier domain (complex plane)
      to change the exponent of the PS (e.g. random walk has
      $\alpha = 1.5$).

    - You perform the inverse FT (`ifft`) to get a noise signal.

5.  Valerie also sends me the paper (livina2011book).

6.  Aims:

    - Predicting [when]{.underline} a tipping point will happen, with
      uncertainty.

    - Classifying tipping points, see (ashwin2012).

7.  Also discussed:

    - direction of the PhD: Ecological themes, for example Savannah
      $\leftrightarrow$ Forest system and tipping points

    - Should discuss courses to take, and find out course requirements
      from Reading. Maybe MAGIC courses can be viewed from afar.

    - **Note for Matlab use:** use `x = (1:1000)’;` instead of
      `x = 1:1000;` - the apostrophe is the transpose to give a column
      vector.

## Note from Valerie on DFA

\
Well you wouldn't want $s<7$. I suppose it depends on the data, but at
$1/4$ of the series you won't get too much detrending. I guess you don't
want to detrend it too much though, you might detrend out the
correlations that you want to observe. I guess seasonal rainfall data
doesn't have too many $10^{th}$ order polynomial trends. If you use
$s =7$ and then use $6^{th}$ order fit, you will fit the points exactly
and get rid of all your data. What is the point of DFA anyway? Should we
maybe just use a linear fit in each segment, or quadratic?

# Models

## Double-well potential model

### Decreasing Noise

This week I have installed MatLab and have tried to re-familiarise
myself with it. I have tried to reproduce Figure 3 (a) in Valerie's
paper *Changing climate states and stability: from Pliocene to present,
2011*, which is shown in Figure [2.1](#Figure3a)
. The data is artificially generated with a
double-well potential given by $$
U(z) = z^4 - 2z^2
$$ and has added time-dependent noise so that the system is
defined by $$
\dot{z}(t) = -(z^4 - 2z^2)' + \sigma(t)\eta,
$$ where $\eta$ is Gaussian noise and
$\sigma(t)= -0.00007t+1.50045$ so that the noise level decreases from
$1.5$ to $0.1$ as $t$ goes from $1$ to $20 000$. The field $\dot{z}(t)$
is plotted (using MatLab) for a few values of $t$ in Figure
[2.2](#vectorField). The
noise-less system has stable 'wells' at $z=\pm 1$ and a not-stable
stationary point at $z=0$.\


![](../images/Figure3a.png)




![](../images/vectorField.png)



So I don't understand where Figure [2.1](#Figure3a)
 comes from because rather than the noise-level
decreasing it appears that the potential wells are moving closer to zero
(and the noise is also decreasing, on closer inspection).\
I used the system $$
\dot{z}(t) = -(z^4 - 2z^2)' + \sigma(t)\eta,
$$ to plot the signal $z$ shown in Figure
[2.3](#signal), which makes
more sense because the wells stay at $\pm 1$ but the noise level
decreases. When the noise level is too small the signal stays in just
one of the wells because it can't get out.\


![](../images/signalPlot1.png)



Anyway, I have also tried to write a MatLab script that calculates the
autocorrelation in a sliding window, but I'm getting a little confused,
the MatLab I knew back in second year has been replaced by python and
C++ since then. MatLab handles lists, arrays and structures in a strange
way I have decided, but I'll get used to it.

### Parabolic trend

I have also tried to reproduce Figure 3 (b) in Valerie's paper *Changing
climate states and stability: from Pliocene to present, 2011*, which is
shown in Figure [2.4](#Figure3b)
. The figure is stated to be produced by the system
$$
\dot{z}(t) & = -(z^4 - 2z^2)' + F(t) + \sigma\eta \\
F(t) & = (5\times 10^{-9}) t^2
$$ In the paper it says "a deterministic forcing with a
parabolic trend varying from 0 to 2 is added to the dynamical equation,
driving the mean value of the time series." but what is shown in Figure
[2.4](#Figure3b) is the
parabolic trend $F(t)$ added to the time series, not added to the
dynamical equation. The system given by the equation changes from a
double-well to a single well potential at the point when
$$F(t) > \min_{z\in [-1,0]}\left\{-(z^4 - 2z^2)'\right\} = \frac{1}{\sqrt{3}},$$
that is, $t \geq 10746$. An example series has been produced in Figure
[2.5](#forcing). At $t=0$,
$F(t)\approx 0$ the stable positions of the system are at
$z\in \{-1,0,1\}$ which is the solution to $-(z^4 - 2z^2)'=0$. When
$F(t)=2$ the (single) stable position is at $z=1.19$ which is the
solution to $-(z^4 - 2z^2)'+2=0$. So the time series does not show the
dramatic parabolic trend shown in Figure
[2.4](#Figure3b), but rather
the stable position at $z=1$ increases to $z=1.19$.\
Or maybe I have completely failed to see something here, please let me
know.


![](../images/Figure3b.png)




![](../images/deterministic_forcing.png)




## ARIMA models

Autoregressive Integrated Moving Average Process.

### Notes taken from (BoxJenkinsBook)

The ARMA process could be given by: $$
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
well.\
The operator $(1-B)$ we denote by $\nabla$. $$
z_t &= (1, 4, 9, 16, 25, 36)\\
\nabla z_t &= (z_2 - z_1, z_3 - z_2, ...)\\
&= (3, 5, 7, 9, 11)\\
\nabla^2 z_t &= (z_3 - 2z_2 +z_1, z_4 - 2z_3 +z_2, ...)\\
&=  (2, 2, 2, 2) 
$$

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
truncated form, which is given in (BoxJenkinsBook)(section 4.2.2).\
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

## Taqqu on ARIMA

Taqqu tells us about *fractional* ARIMA, or FARIMA, along with
Fractional Gaussian Noise (FGN). These are useful, we are told in a
completely unqualified claim, because\
*These are the simplest models which display long range dependence.*\
So there you go, let's just believe Taqqu and have a go at understanding
FARIMA.

### FARIMA

FARIMA is ARIMA$(0,d,0)$ where $d$ is fractional. Taqqu puts it in the
form $$
z_t  = \nabla^{-d}a_t, ~~ t\geq 1
$$ Apparently the best way to interpret *this* is as a
moving average: $$
z_t = \sum_{j=0}^\infty c_j a_{t-j}\\
c_j = \frac{\Gamma(j+d)}{\Gamma(d)\Gamma(j+1)} \rightarrow \frac{j^{d-1}}{\Gamma(d)}.
$$

The book (beran1994) might provide a useful algorithm to generate
FARIMA series. Taqqu says Haslett 1989 does this (p.12-13) but I can't
work it out.

# Auto-Correlation Function

## Lag-1 ACF of decreasing noise model

I have looked at the lag-1 autocorrelation of a time series.


![](../images/decresing_noise.png)





![](../images/lag1.png)



Figure [3.1](#series) shows a
series produced by the system $$
\dot{z}(t) & = -(z^4 - 2z^2)' + \sigma(t)\eta \\
\sigma(t) & = -0.00007t+1.50045
$$ Figure [3.2](#auto_correlation)
 shows the lag-1 autocorrelation (AC) of
the series in a sliding window of length $5000$. The AC increases
towards $1$ as the series spends more time in each state, until the
point just after $t=10^4$ when the series spends all the time in just
one state. At this point the AC drops to a value of $0$.

# DFA Method

From (kantelhardt2001), DFA is a four-step process. We have our data
$x$, the size of $x$, $N$, the length of the segments, $s$, and the
order of the polynomial fit, $n$.

#### Step 1

Determine the 'profile' $Y$, which seems to be defined as the cumulative
sum: $$Y(i) = \sum_{k=0}^{i} x(k).$$ Kantelhardt subtracts the mean but
then says that it isn't necessary.

#### Step 2

Divide the profile $Y$ into non overlapping segments of length $s$,
there will be $N_s = \lfloor N/s \rfloor$ such segments starting from
the first entry in $Y$, and this collection of $N_s$ segments will
exclude the last few entries of $Y$ if $N$ is not an exact multiple of
$s$. To make use of those entries, also define another $N_s$ segments
starting from the last entry in $Y$, thus excluding the first few
entries.

#### Step 3

For each segment (there are $2N_s$ segments), find a polynomial fit (of
order $n$) and evaluate it on the same range as $x$ (or $Y$) to give the
series $\{p(i)\}_i$. The *Detrended* time series is given in each
segment: $$Y_s(i) = Y(i) - p(i).$$ Figure
[4.1](#DFApolyfit) shows an
example of the first part of this step. The figure shows the segments
starting from the first entry, thus the last few entries are not used
and the polynomial fit is equal to 0.

![Polynomial (quadratic) fit on segments of length 100 for some
artificial series of length 440. The blue shows the 'profile' of the
data $\{Y(i)\}$ and the red show the quadratic fit. Note that the last
40 points in $Y$ are not fitted because the segments run
out.](../images/polyfit_for_DFA.png){#DFApolyfit
width="0.5\\paperwidth"}

#### Step 4

For each segment calculate the variance
$$F_s = \frac{1}{s}\sum_i Y_s(i)^2,$$ the sum is over all points in the
segment. Then calculate $$F^{(n)}(s) = \sqrt{\frac{1}{2N_s}\sum F_s}$$
where the sum here is over all segments ($F_s$ is calculated *for each*
segment).

## A closer look at DFA

(kantelhardt2001) quotes the equation $$
F^{(n)}(s) \propto s^\alpha 

$$ which holds for large $s$. The 'fluctuations exponent'
$\alpha$ is related to the 'correlation exponent' $\gamma$.\

### MatLab

We use MatLab to try to replicate the results in (kantelhardt2001), or
at least to see if we can implement DFA accurately. The function `DFA.m`
takes 3 arguments: `data`, `segment_length` ($s$) and `order` ($n$). The
output is the fluctuation function $F^{(n)}(s)$. The function
`DFA_analysis.m` takes 2 arguments: `data` and `order`. The output is an
array of `DFA.m` outputs evaluated with $n = 1, ..., \texttt{order}$.\
Using the data Valerie generated (`data05`, `data09`, `data15`, with
correlations $0.5$, $0.9$ and $1.5$) we perform `DFA_analysis.m` for
`order`=5, the results are in Figure
[4.2](#DFA_comparison).



![](../images/DFA_05.png)


![](../images/DFA_09.png)

DFA analysis. The scaled fluctuation function 
$F^{(n)}(s)/\sqrt{s}$ over increasing 
s. (left) shows artificial data
`data05`, (right) shows `data09`.


And the same sort of thing is shown in Figure
[4.3](#graceproject1)
only produced using grace, so there you go.

![DFA. Correlations, from top to bottom: 1.5, 0.9 and
0.5](../images/graceproject1.png)

## The Idea

The idea surely is that one could use DFA to obtain this exponent
$\alpha$ using Eqn. [\[F=s\]](#F=s)
.\
(kantelhardt2001) plots $F^{(n)}(s)/\sqrt{s}$ over increasing $s$, as
we have done, and says you could use a linear fit to estimate $\alpha$.
Since with White Noise you have a horizontal line (see Fig.
[4.3](#graceproject1)
(bottom)) you have $$
  F^{(3)}(s) / s^{1/2} &= k \\
\Rightarrow  F^{(3)}(s) &= ks^{1/2} \\
\Rightarrow  \alpha &= 1/2 
$$ With the data `data09` (Fig.
[4.3](#graceproject1)
(middle)) we can do a linear fit and get $$
  \log( F^{(3)}(s) / s^{1/2} ) &\approx 0.44\log(s) - 3.3 \\
\Rightarrow  F^{(3)}(s) / s^{1/2} &= 10^{-3.3}s^{0.44} \\
\Rightarrow  F^{(3)}(s) &= 10^{-3.3}s^{0.94} \\
\Rightarrow  \alpha &= 0.94
$$

Which is pretty close to $0.9$ I guess. Maybe the linear fit is a bit
too steep because of the 'deviation' that Kantelhardt talks about. We
can use $F_{\text{mod}}$ instead to get a better estimate.

## Why does DFA work? / what is it doing?

(kantelhardt2001) says that Eqn. [\[F=s\]](#F=s)
 holds and says a derivation is to be found in a
paper[^1] that I cannot access. Well maybe I'll try and access it later
if I need to.\
It seems that this Eqn. [\[F=s\]](#F=s)
 is very closely related to the other equation
Kantelhardt gives us: $$
F^{(n)}(s) \sim s^{1-\gamma/2}

$$ Which, they say derives from something like
$$
\langle Y^2(i)\rangle \sim i^{2-\gamma}
$$ only using $F$ instead of $Y$.

## What next?

Make a function `DFA_mod.m` which does the modified DFA Kantelhardt is
doing, then use that to make another function which determines $\alpha$
by doing `DFA_mod` at a few points and finding a linear fit.\
Then use this to determine $\alpha$ in a sliding window and use it on
some data to see how this compares to ACF. The window size must be at
least 1000 points to do modified DFA effectively ($s'>50$ and
$s'\approx N/20$ (kantelhardt2001)). Even with $s=50$ the liner fit
will be poor using our unmodified DFA, so far we have gone as far as
$s=1000$.

## The modified fluctuation function

We have written the function `DFA_mod.m` which finds the fluctuation
function $F^{(n)}(s)$ for the data and also for *several random
shufflings* of the data, also finds the fluctuation function
$F^{(n)}(s')$ for several shufflings where $s'=\lfloor N/20 \rfloor$.\
We then have, for each shuffling (indexed $i$), a number $F_i^{(n)}(s)$
and also a number $F_i^{(n)}(s')$ which form two lists of numbers:
$F_{\text{shuff}}^{(n)}(s) = \{F_{i}^{(n)}(s)\}_{i=1}^{\text{\# shuffles}}$
and $F_{\text{shuff}}^{(n)}(s')$.\
We take the variance (?[^2]) to get $$
K_\alpha^{(n)}(s) = \frac{\langle F_{\text{shuff}}^{(n)}(s)^2 \rangle^{1/2}s'^\alpha }{\langle F_{\text{shuff}}^{(n)}(s')^2 \rangle^{1/2}s^\alpha},

$$ where we use $\alpha = 0.5$ by default. Then we can
finally get the *modified* fluctuation function $$
 F_{\text{mod}}^{(n)}(s) = \frac{ F^{(n)}(s)}{K_\alpha^{(n)}(s)}
$$

## Using $F_\text{mod}$

![Showing $F_{\text{mod}}^{(3)}(s)$ and $F^{(3)}(s)$ for
`data09`.](../images/Fmod_vs_F.png)

Figure [4.4](#Fmod) shows the
same sort of thing as Fig.[4.3](#graceproject1)
, but only for `data09` and only for a cubic
polynomial fit ($n=3$). The two sets shown are very similar, although
they diverge a bit for low $s$, it appears that
$F_{\text{mod}}^{(3)}(s)$ is *more* linear than the other. However, if
you just use $s>30$ or even $s>50$ then you're still going to get a
pretty good linear fit.\
Using the points shown in Fig.[4.4](#Fmod)
 we can do a linear fit to estimate $\alpha$ (it should
be about 0.9). The linear fit for the regular $F$ (red line) gives
$\alpha = 0.9368$. Fitting to the blue points (which used $F_\text{mod}$
gives $\alpha = 0.9246$, which is a little bit better I suppose but not
worth[^3] the huge amount of extra time it takes to run the modified
version.\
The regular version needs to find $F(s)$ several times to find a good
linear fit, I would suggest *at least* three (as seen in
Fig.[4.4](#Fmod), we have used
eight). For each of these you have to divide the data into
$2\lfloor N/s \rfloor$ segments. So for eight values of $s$ space
logarithmically from 10 to 500 (as we have used), and data of length
$N=10000$ (as we have), you have a total of
$\sum_s 2\lfloor N/s \rfloor = 4664$ segments, and you have to do a
polynomial fit (here cubic) to the data profile in each of these
segments.\
However, using *modified* DFA we do DFA for all the different shufflings
(here we have used 20 shufflings), plus one extra time to get the
regular $F(s)$, plus $20\times2\lfloor N/s' \rfloor$ extra times. For
our same example this is $21\times 4664 + 20\times 40 = 98744$ cubic
fits, which is a lot more than $4664$. Accordingly, using $F_\text{mod}$
takes at least 20 times longer. Although I suppose 20 shuffles are not
necessary, how would you work out the optimum number of shuffles?\
Truncating the first two points from the un-modified DFA in
Fig.[4.4](#Fmod) so we only use
$F(s)$ for $s>30$ looks like it ought to be just as good as
$F_\text{mod}$, but it isn't because of that last point at $s=500$ which
is not in-line with the rest, and it is the same for $F$ and
$F_\text{mod}$. I wonder why\... Anyway, if we knock off the $s=500$
value then we've got a lovely $\alpha=0.91$.\
(kantelhardt2001) does say something about *short term* data so maybe
the point is that we can use DFA even with data sets of length 1000 or
even shorter if we are able to use small value of $s$ for the linear
(i.e. logarithmic) fit.

### The correction function

The correction function $K_\alpha^{(n)}(s)$, where we use $\alpha=0.5$
by default, is asymptotically (i.e for large $s$) constant in $s$. Lets
have a look at the formula
(Eqn.[\[correction_func\]](#correction_func)
) again: $$
K_\alpha^{(n)}(s) = \frac{\langle F_{\text{shuff}}^{(n)}(s)^2 \rangle^{1/2}s'^\alpha }{\langle F_{\text{shuff}}^{(n)}(s')^2 \rangle^{1/2}s^\alpha}.
$$ I think I need to understand what DFA is doing, that is,
what physical relevance $\alpha$ and $F(s)$ have, before I can
understand why this is constant. It boils down to:
$\langle F_{\text{shuff}}^{(n)}(s)^2 \rangle \propto s$.[^4] So the
larger segment size $s$ we use to find the fluctuation function $F(s)$
of some shuffled data, the greater the variance of the values of $F(s)$
over several shuffles, and the relation is linear. I suppose this makes
sense, intuitively, because by taking larger segment size $s$ the
polynomial fit will be less accurate, so we have greater variance in the
$Y_s$, $\Rightarrow$ the value of $F(s)$ will be larger, since this is
related to $\text{Var}(Y_s)$. And I suppose that the larger $F(s)$
potentially is, the larger its variance potentially is, although why the
relationship should be linear remains a mystery.

## Comparison of ACF and DFA

We estimate the value of $\alpha$ using DFA in a sliding window of data,
that is, for index $i$ we perform DFA on the selection
$\texttt{data(i-999:i)}$ (for a window size 1000, for example). Using
the "decreasing noise, 2-state system" model the results are shown in
Figure [4.5](#graceproject2)
.

![The decreasing noise model. The time series $z(t)$ is shown in black.
DFA indicators are found at intervals of 1000 (points shown by square
symbols), ACF indicators are found at every
point.](../images/graceproject2.png)

Figure [4.5](#graceproject2)
 also shows the lag-1 autocorrelation (ACF1)
of the data in a sliding window, in a similar way to the DFA indicator
$\alpha$.\
Predictably, the ACF1 settles down to a value of $0$ when the system
falls into one state and is just white noise, also the DFA indicator
$\alpha$ settles to the value $0.5$, which corresponds to white noise
(livina2007).\
Using window size 1000 obviously gives a "faster response" to changes in
the correlation of the data than size 5000 because you're going to still
be detecting the correlation from 4000 points before even though the
system *now* has no correlation.\
The final 'jump' from state $z\approx -1$ to state $z\approx 1$ occurs
in the interval $t\in [9746, 9751]$, the data *in* that interval is
obviously highly correlated, although both before and after it is just
white noise. The ACF (window 1000) JUMPS back up to $\approx 1$ but the
DFA just carries on downwards[^5] I guess because the ACF1 is lag-1 it
is more sensitive to this sort of thing.

## Notes on FA, no detrending

(peng1994) introduces DFA and defines it in the same way as
(kantelhardt2001), although possibly slightly simpler:

1.  Divide the entire sequence of length $N$ into $N/l$ non-overlapping
    boxes, each containing $l$ nucleotides, and define the \"local
    trend\" in each box (proportional to the compositional bias in the
    box) to be the ordinate of a linear least-squares fit for the DNA
    walk displacement in that box

2.  Define the "detrended walk", denoted by $y_l(n)$, as the difference
    between the original walk $y(n)$ and the local trend. Calculate the
    variance about the detrended walk for each box, and calculate the
    average of these variances over all the boxes of size $l$, denoted
    $F_d^2(l)$.

Peng et al., then, use only a liner fit to describe the trend in each
'box'. In their previous paper (peng1992) they study the (simpler,
non-detrended) fluctuation $F(l)$ defined: $$
F^2(l) = \overline{ \left[ \Delta y(l) \right]^2 } -  \left[ \overline{ \Delta y(l) } \right]^2 ,
$$ where $$
\Delta y(l) = y(l_0 +l) - y(l_0).
$$ So basically the *variance* of the $\Delta y(l)$ where
$l_0$ is allowed to vary. In fact $\Delta y(1)$ is just the original
data[^6] $u$, and so $F^2(1)$ is the variance of the data. The claim is
that $F$ is related to the "auto-correlation function" $$
C(l) = \overline{u(l_0)u(l_0 +l)} - \overline{u(l_0)}^2
$$ by the relation $$
F^2(l) = \sum_{i=1}^l\sum_{j=1}^l C(j-i).
$$

# To-do lists

## 12$^{th}$ September 2015

- reread *Held and Kleinen, 2004* and *Livina and Lenton 2007*.

- become better acquainted with MatLab.

- plot the Autocorrelation of a time series.

- plot the Power Spectrum.

- read about the Fourier transform and the Power spectrum to the point
  of being able to ask questions.

## 23$^{rd}$ September 2015

I'm not sure what to do now. I've had a look at the other system (with
the forcing) to look at the autocorrelation, but I'm not sure how useful
that is. Clearly the autocorrelation approaching 1 is an indicator of a
change (as in Figure [3.2](#auto_correlation)
, so it's good that I appreciate that.\
I have also been attempting to figure out how the power spectrum relates
to anything. We said that we should look at the fourier transform of the
autocorrelation. Does this mean to do a FFT on the data in Figure
[3.2](#auto_correlation)
? There does not appear to be any frequency
patterns in that data. Maybe with other data produced by other systems
(or maybe real data).\
I feel like it is good to be at the messing-around stage, but I would
like some hints on what to mess around with next. Obviously I have not
done very much work recently; I don't want to bugger off to the library
all day yet and leave Amber with the 5-day-old, so I'm working at home,
which is quite distracting. As I say, it would be good to have some
advice about what to do next, and to have some closure on Figures 3a and
3b in *Changing climate states and stability: from Pliocene to present,
2011*.

## 29$^{th}$ September 2015

I have been reading (BoxJenkinsBook) to learn about AR and MA and ARMA
models. Valerie also recommends Taqqu et al. papers on FARIMA models.

[^1]: M.S. Taqqu, V. Teverovsky, and W. Willinger, Fractals 3 (1995) 785

[^2]: (kantelhardt2001) uses $\langle x^2 \rangle$ to mean
    $\frac{1}{N}\sum_{i=1}^N x_i^2$, (that is, $\langle ... \rangle$ is
    the mean) and call *this* the variance. We follow their lead here.

[^3]: In my opinion, right now

[^4]: By squaring out, provided $\alpha = 1/2$.

[^5]: I calculated $\alpha$ at 'better resolution' for $9000<t<11000$
    but it is the same roughly linear decline shown in the graph by the
    dashed line

[^6]: Note that $u(i)$ is the signal, $y(i)$ is the cumulative sum.
