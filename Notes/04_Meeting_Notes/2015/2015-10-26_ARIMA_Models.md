# ARIMA models

Taqqu tells us about *fractional* ARIMA, or FARIMA, along with
Fractional Gaussian Noise (FGN). These are useful, we are told in a
completely unqualified claim, because\
*These are the simplest models which display long range dependence.*\
So there you go, let's just believe Taqqu and have a go at understanding
FARIMA.

## Fractional ARIMA

FARIMA is ARIMA$(0,d,0)$ where $d$ is fractional. Taqqu puts it in the
form $$
z_t  = \nabla^{-d}a_t, ~~ t\geq 1
$$ Apparently the best way to interpret *this* is as a
moving average: $$
z_t = \sum_{j=0}^\infty c_j a_{t-j}\\
c_j = \frac{\Gamma(j+d)}{\Gamma(d)\Gamma(j+1)} \rightarrow \frac{j^{d-1}}{\Gamma(d)}.
$$

We reproduce Defn. 2.7 from (beran1994):\
Let $X_t$ be a stationary process such that $$
\Phi(B)(1-B)^dX_t = \Psi(B)\epsilon_t
$$ (That is, an ARIMA$(p,d,q)$ process. Then for
$-\frac{1}{2}< d < \frac{1}{2}$, $X_t$ is a *fractional* ARIMA$(p,d,q)$
process. The $<\frac{1}{2}$ is important because the process is not
stable for $d=\frac{1}{2}$.\
This definition is due to *Granger and Joyeux (1980)* and *Hosking
(1981)*. The interesting range is $0 \leq d < \frac{1}{2}$.

The book (beran1994) might provide a useful algorithm to generate
FARIMA series but it is in some weird pseudocode. Must get Beran from
the library, google books misses some pages. Taqqu says Haslett 1989
also provides an algorithm (p.12-13) but I can't work it out.

# Fractional Brownian Motion

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
$H\neq 1/2$).\
In Fig.[1](#BrownvsRMD) we
have used the Random Midpoint Displacement method with Hurst exponent
$H=0.5$ to simulate a regular Brownian walk. If we adjust $H$ we can
simulate other fractional Brownian motion.

![The Blue and purple walks are generated using the Random Midpoint
Displacement method with Hurst exponent $H=0.5$. The Red and Yellow
walks are good old fashioned summing up Gaussian noise. It looks like
the RMD method works very well and simulates Brownian motion as it's
supposed to. If you think about iit, it really make
sense.](../images/fBrownvsBrownian.png)

## Fractional Gaussian Noise (FGN)

Lets take the term-wise difference of the fractional Brownian walk to
get some FGN.\

   Hurst exponent  $\alpha$ from DFA1   $\alpha$ from DFA0   ACF lag-1
  ---------------- -------------------- -------------------- -----------------
        0.2        0.2574               0.2285               -0.2019 (0.40)
        0.5        0.5058               0.4826               -0.0108 (0.49)
        0.8        0.7852               0.8083                 0.4219 (0.71)
        0.9        0.9108               0.9374                 0.5965 (0.80)

  : estimation of $\alpha$ for synthetic FGN from simulated Brownian
  Walks using the Random Midpoint method. Data sets of length $2^{14}$.

Now this data in table [1](#FGNtable)
 was obtained by using DFA, not *modified* DFA, so
it's not perfect, it's not even the best it could be using the code I've
already written, but even so it seems to be estimating the exponent
fairly accurately.

## Other values of $H$

What happens if you use $H=1.5$? You get a load of complex numbers,
really big complex numbers. Because, your scaling factors
($D_1, D_2,..$) are all complex because $D_1$ is complex if $H>1$. If
$H=1$ then all the $D_1, D_2,..$ are zero.

Data in the table is from the Brownian motion with $H<0$, not the
differences of the terms.\

   Hurst exponent  $\alpha$ from DFA1   $\alpha$ from DFA0   ACF lag-1
  ---------------- -------------------- -------------------- ---------------
        -0.8       0.5689               0.5571               0.2116 (0.61)
        -0.5       0.6572               0.6575               0.3392 (0.67)
        -0.1       0.9240               0.8406               0.7033 (0.85)

\

Hey, if we use $H<0$ we get what looks like white noise (to the
untrained eye). It's so uncorrelated that it just oscillates about 0 and
doesn't "add up". (see box above). fBrownian with $H=-10$ looks very
cool. See figure [2](#fBm10).

There is a magic number in the range $-73.1429 \leq H \leq -73.1428$.
Rather than being sue to any property of the method, this is due to
matlab's precision.

![$H=-10$](../images/fBm10.png)

# Other Models

(beran1994)(page 121) also talks about fractional EXP, or FEXP models.
(beran1994) also gives an algorithm to simulate ARIMA process but it is
quite hard to follow. Basically the jist is that we have to know what
kind of spectral density we want to approximate.

Spectral Density vs Power Spectrum
