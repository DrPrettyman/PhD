# Extension to multivariate and gridded data

The methods described so far (degenerate fingerprinting, potential
analysis) are applied only to a single one-dimensional time series.
Since this project aims to study geophysical variables we must consider
cases where we have more than one time series, either because:

1.  There is more than one measured variable that may affect an EWS.

2.  A variable is measured at several locations on a grid.

3.  Both of the above simultaneously.

In the first case it may suffice to attempt an EWS detection on each
time series individually but one can envision a scenario where it is not
possible to detect an EWS in $X(t)$ nor $Y(t)$ but, considered together
in some way, an EWS is visible. It may therefore be worthwhile to
investigate the possibility of a 2D (or multidimensional) analogue to
the one-dimensional methods described previously. In the case of gridded
data it is common to use Empirical Orthogonal Functions (EOF)[^1] to
reduce the dimensionality (vonstorch Chapter 13), but it may be worth
investigating other methods. It is also possible to use the EOF method
for multivariate data.

# Extension to multivariate data

## A 2D analogue of the ACF fingerprinting method

We may linearly approximate many dynamical systems using an
autoregressive model: $$
x_{t+1} = ax_t + c + \varepsilon_t,
$$ and we can estimate the lag-1 autocorrelation coefficient
$a$ using $$
a = \frac{E(x_{t+1}x_t)-\bar{x}^2}{E(x_{t}^2)-\bar{x}^2}.
$$ It is proposed that the same method could be applied to a
higher dimension system $$
\mathbf{x}_{t+1} = A\mathbf{x}_t + \mathbf{c} + \mathbf{\varepsilon}_t
$$ using a straight-forward translation of the
one-dimensional formula: $$
A= \frac{E({\mathbf x}_{t+1}{\mathbf x}_t^\top)-\bar{{\mathbf x}}\bar{{\mathbf x}}^\top}{E({\mathbf x}_t{\mathbf x}_t^\top)-\bar{{\mathbf x}}\bar{{\mathbf x}}^\top}
$$ (williamson2015), where the fraction is an obvious abuse
of notation. For a system of three variables, the matrix $A$ has nine
elements, thus we have not done much to reduce the dimension of the
problem. It is proposed in the same paper that the eigenvalues of the
Jacobian of $A$ should be studied. This method is applied to the system
in equation
[\[eqn_homoclinic_system\]](#eqn_homoclinic_system)
 $$

\dot{x} &= y + \varepsilon^{(x)}\\
\dot{y} &= \mu - x^2 + \varepsilon^{(y)}\\
\mu &= 0.5-0.005t


$$ with a homoclinic bifurcation at $\mu(t)=0$ ($t=100$). The
system is integrated from $t=0$ to $t=100$ with $\varepsilon$ white
noise with standard deviation $\sigma = 0.5$. The solution is given at
intervals of $\Delta t=0.5$. The result is shown in figure
[1](#ourownonorbit0p5)
 and the eigenvalue analysis is shown in
figure [2](#Jeigenvals0p5)
.

![Attempt to replicate the results in (williamson2015), with the noise
std of 0.5.](../../notes/images/ourownorbit0p5.png){#ourownonorbit0p5
width="5in"}

![The Jacobian eigenvalue (both real and imaginary parts) plotted in a
sliding window. These are derived from the time series shown in figure
[1](#ourownonorbit0p5)
](../../notes/images/Jeigenvals0p5.png){#Jeigenvals0p5
width="5.5in"}

The decreasing imaginary part of the principal eigenvalue predicates the
bifurcation, as predicted by the analysis, but it is not clear that this
could serve as an EWS without working out beforehand which changes to
look for, already having perfect knowledge of the equations describing
the system. Also, for an $n$-dimensional system we have $2n$ variables
to analyse ($n$ eigenvalues, each with real and imaginary parts).
However, studying the principal eigenvalue, rather than the $n$
individual components of the system, does at least incorporate part of
the information of each variable into a single statistic, even if much
information is lost by ignoring the other eigenvalues. We must
investigate in which cases the principal eigenvalue provides a useful
EWS.

## Using an EOF method to reduce dimensions

The use of EOF to reduce dimensionality is common in climate research
(vonstorch Chapter 13). The method aims to "capture" most of the
"interesting" behaviour of the system (held2004). We project the
multi-dimensional system onto an orthogonal basis such that the first
component of the system in the new basis has maximal variance, and the
$n^{\text{th}}$ component has maximal variance given the first $n-1$
basis vectors. One may then study only the first $k$ components of the
system in the new basis, where $k$ is chosen so that, say, 95% of the
total variance is captured. In many applications only the
one-dimensional system of the first component is considered.

The EOF method involves finding the eigenvalues of the covariance matrix
of a time series ${\mathbf x}_t$, then projecting ${\mathbf x}_t$ onto
the eigenvectors corresponding to the $k$ largest eigenvalues. What we
have achieved is a $k$-dimensional time series where the variance in the
first dimension is as large as possible, the variance in the second
dimension is as large as possible given the first, etc..

# Application to hurricane project: 2 variable

## Data

We use the same sample of 14 tropical cyclones, with measurements taken
for each at a single, fixed weather station. We now include both wind
speed and sea level pressure data, rather than only pressure, and apply
the methods described in section
[2](#sec_multivariate)
 to see if there is a detectable EWS.

## Applying the method of (williamson2015)

We note that the method presented by (williamson2015) is in some way an
extension of the ACF-propagator method that we see in (held2004), etc.,
and also that the ACF-indicator was not the most useful indicator in the
comparison of PS, DFA and ACF, so we do not expect that this method will
be useful either. However, it my be instructive to test it.

### Application to a new bifurcating model

Why not continue the research of (williamson2015) and apply the method
to a different model?

## Reducing dimensionality with EOF

We use the familiar EWS indicator techniques (Power Spectrum, DFA, ACF)
with a 1D time series created by reducing the dimension of the
wind-speed/pressure system. We thus have three 1D time series: pressure,
wind speed and the EOF score, for each of the 14 cyclones. Figure
[3](#EOF_PSindicator)
shows the PS-indicator applied to all three series for each cyclone, the
mean is taken over the 14 cyclones. We can see that the indicator rises
earlier, though less steeply, when applied to wind speed, but there is
little difference between the results for the first EOF score and the
pressure alone. Figure [4](#EOF_ACF1indicator)
 shows the same thing, now using the
ACF(1)-indicator. The ACF(1)-indicator applied to pressure shows no sign
at all of an EWS -as we have previously found- but applied to the wind
speed there is a definite trend, therefore we might hope that taking the
wind speed into consideration will improve our EWS over considering only
pressure.

![showing the PS-indicator applied to the pressure, wind speed and the
first EOF score of the two considered together. The indicator appears to
rise earlier, but less steeply, in the wind speed. There appears to be
little difference between the pressure and the
EOF.](../../notes/images/EOF_PSindicator.png){#EOF_PSindicator
width="5in"}

![showing the ACF1-indicator applied to the pressure, wind speed and the
first EOF score of the two considered together. Unlike the pressure time
series, the wind speed series shows a strong EWS with the ACF(1)
indicator. The signal for the EOF score is somewhere between the
two.](../../notes/images/EOF_ACF1indicator.png){#EOF_ACF1indicator
width="5in"}

# Analytic investigation of the EOF method

The use of EOF to reduce dimensionality is common in climate research
(vonstorch Chapter 13). The method aims to "capture" most of the
"interesting" behaviour of the system (held2004). We project the
multi-dimensional system onto an orthogonal basis such that the first
component of the system in the new basis has maximal variance, and the
$n^{\text{th}}$ component has maximal variance given the first $n-1$
basis vectors. One may then study only the first $k$ components of the
system in the new basis, where $k$ is chosen so that, say, 95% of the
total variance is captured. In many applications only the
one-dimensional system of the first component is considered.

We wish to ask the question: how useful or relevant is the first EOF in
the detection or prediction of tipping points? That is, are there cases
where the information relevant to tipping, such increasing
autocorrelation (scheffer2009), is not captured by the first EOF?

## Study of a simple dynamical system

We attempt to answer this question by studying the stochastic system
eqn.[\[sytem_eqn_1\]](#sytem_eqn_1)
, $$
{\mathbf x}_{k+1} = B{\mathbf x}_k + S\eta_k,

$$ where the ${\mathbf \eta}_k$ are column vectors with each
element $\sim N(0,1)$, iid. Suppose that $B$ is diagonalisable with real
eigenvalues $\mu_{i}$. In the case that all $|\mu_{i}|<1$,
${\mathbf x}_n$ will tend to zero but it will tend to zero more slowly
in the direction $\mathbf{v}_{\max}$, the eigenvector corresponding to
$\mu_{\max} := \max_{i}|\mu_{i}|$. If we allow $\mu_{\max}$ to vary a
critical transition occurs at $|\mu_{\max}|=1$ and $|\mu_{\max}|>1$ will
cause the ${\mathbf x}_n$ to tend to infinity in the direction
$\mathbf{v}_{\max}$. If we project the series ${\mathbf x}_n$ onto the
vector $\mathbf{v}_{\max}$, we expect to see an increase in
autocorrelation as $\mu_{\max} \rightarrow 1$. If the first EOF is to
capture this autocorrelation and provide a good predictor of the tipping
point, we would expect that the first EOF score, $\mathbf{w}_1$, is very
close to $\mathbf{v}_{\max}$.\

## An empirical calculation of EOF, with simplifications

We attempt to calculate empirically the eigenvectors of the covariance
matrix of the series $\{{\mathbf x}\}$ described by equation
[\[sytem_eqn_1\]](#sytem_eqn_1)
. In the first instance we assume that $B$ is
constant with eigenvalues $\mu_i<1$ $\forall i$ so that there is no
tipping point and the long-term mean of $\{{\mathbf x}\}$ is zero. We
also assume that $B$ is diagonal, which is equivalent --via a change of
basis-- to saying that $B$ is diagonalisable.

We first write out the terms of equation
[\[sytem_eqn_1\]](#sytem_eqn_1)
 in terms of ${\mathbf x}_0$: $$
{\mathbf x}_k &= B^k{\mathbf x}_0 + \sum_{i=1}^{k} B^{k-i}S{\mathbf \eta}_i \\
&= \sum_{s=0}^{\infty} B^{s} S {\mathbf \eta}_{k-s} - B^k \left(\sum_{s=0}^{\infty} B^{s} S {\mathbf \eta}_{-s} - {\mathbf x}_0\right).
$$ And we replace $k$ with $k+N_0$ where $N_0$ is large
enough so that $B^{N_0} \approx 0$ and the mean of $\{x_i\}_{i=0}^{N_0}$
is also approximately zero. It is then possible to calculate the
expectation of the covariance of the time series: $$
\mathbb{E}(C) &= \frac{1}{N}\sum_{k=0}^{N-1}\left[\sum_{s=0}^\infty \sum_{r=0}^\infty B^s S\mathbb{E}\left[(\eta_{k+N_0-s})(\eta_{k+N_0-r})^\top\right] S^\top (B^\top)^r\right]\\
& = \sum_{s=0}^\infty B^s S S^\top (B^\top)^s \\
D :=\mathbb{E}(C) &= SS^\top + B D B^\top
$$ It is then possible to calculate the eigenvalues and
eigenvectors of $D$. We here assume that $B$ is diagonal and that the
system is two-dimensional, with $b_{11}$ very close to $1$ and greater
than $b_{22}$. We note that $$
D = \left[ 
\begin{array}{cc}
\frac{s_{12}^2+s_{11}^2}{1-b_{11}^2} & \frac{s_{12}s_{22}+s_{11}s_{21}}{1-b_{11}b_{22}}\\
\frac{s_{12}s_{22}+s_{11}s_{21}}{1-b_{11}b_{22}} & \frac{s_{22}^2+s_{21}^2}{1-b_{22}^2}
\end{array}
\right].

$$ In general, the eigenvalues of symmetric matrix $\left(
\begin{array}{cc}
a&b\\
b&c
\end{array}
\right)$ are $$
\frac{1}{2}\left(a+c\pm\sqrt{(a-c)^2+4b^2}\right)

$$ and since everything is positive the positive square root
will give the largest eigenvalue. Note that for $b=0$ the difference
between the two eigenvalues is $|a-c|$ but for non zero $b$ this
difference increases -- the eigenvalues become more distinct. For matrix
$D$ this $b=0$ corresponds to the situation where $S$ is diagonal or
reverse-diagonal, or one of the rows or columns is zero. The eigenvector
corresponding to this largest eigenvalue (the principal eigenvector) is
$$
\left(
\begin{array}{c}
a-c + \sqrt{(a-c)^2+4b^2}\\
2b
\end{array}
\right).

$$

We substitute the terms from equation
[\[D_for_B_diag\]](#D_for_B_diag)
 into equation
[\[largest_eigenvector\]](#largest_eigenvector)
 and expand out the roots and
reciprocals upto terms $\mathcal{O}((1-b_{11})^2)$, since
$(1-b_{11})\approx 0$. We find that the first component is
$$
 v_1 = \frac{2p}{(1-b_{11}^2)} + 
\frac{-2q}{(1-b_{22}^2)}+
(1-b_{11}^2) \left[ \frac{2r^2(1+ b_{22})^2 -  q^2 }{p(1-b_{22}^2)^2}\right]
$$ and the second vector component is $$
v_2 = 2r\left[\frac{1}{1-b_{22}} -
\frac{b_{22}(1-b_{11})}{(1-b_{22})^2}
\right]
$$ where $p := s_{11}^2+s_{12}^2$, $q := s_{21}^2+s_{22}^2$
and $r := s_{12}s_{22}+s_{11}s_{21}$. We expect this eigenvector,
$\mathbf{v} = (v_1, v_2)^\top$, to be approximately $(1,0)^\top$, since
the "interesting" behaviour is happening in this (the $x$) direction.
The system tends to zero much more quickly in the $y$ direction. If $S$
is diagonal ($r=0$) then this is always the case, otherwise it may be
the case that this will be closer to the direction of $(0,1)^\top$, but
this is only if $s_{11},s_{12}$ are very small and $s_{21},s_{22}$ are
very large. In this case it is already very obvious that the largest
variance will be in the $(0,1)^\top$ projection, it is simply a case of
a very large noise obscuring the signal (in this case the 'signal' is
the impending tipping point as $b_{11}$ 'approaches' 1).

## Full calculation of EOF - without assumptions

We have so far considered the system in equation
[\[sytem_eqn_1\]](#sytem_eqn_1)
 from the point $N_0$. That is, we have
considered the series $$
{\mathbf x}_{N_0}, {\mathbf x}_{N_0+1}, \dots, {\mathbf x}_{N-1}, {\mathbf x}_{N}
$$ where $N_0 < N$ is chosen to be large such that $B^{N_0}$
is approximately zero, and ignored in our calculation. What we actually
wish to study is a system where at least one eigenvalue of $B^n$
approaches 1, so this is a bad assumption. We therefore have to
recalculate the EOF without disregarding any terms. Effectively, we have
so far calculated $$
\lim_{N\gg N_0 \rightarrow\infty}\left[D\right]= \sum_{s=0}^\infty B^s S S^\top (B^\top)^s
$$ now we want to find $$
D=\mathbb{E}(C) = \sum_{s=0}^\infty B^s S S^\top (B^\top)^s + \text{error}.
$$ and evaluate the error term.

First, we simplify the notation using: $$
\eta &= \{\eta_i\}_{i \in \mathbb{Z}}\\
\theta_n : \{\eta_i\}_i &\mapsto \{\eta_{n+i}\}_i\\
F(\eta) &:= \sum_{j=0}^\infty B^j S \eta_{-j}
$$ Then we can rewrite $$
{\mathbf x}_n &= \sum_{j=0}^\infty B^j S \eta_{n-j} + B^n\left[{\mathbf x}_o - \sum_{j=0}^\infty B^j S \eta_{-j}\right]\\
&=B^n({\mathbf x}_0 - F(\eta)) +F(\theta_n \eta)
$$

Ergodic theorem for stationary processes: $$
\lim_{N \rightarrow \infty}\frac{1}{N} \sum_{n=1}^N G(\theta_n \eta) = \mathbb{E}[G]
$$ For finite $N$ we expect something like: $$
\frac{1}{N} \sum_{n=1}^N G(\theta_n \eta) = \mathbb{E}[G] + \mathcal{O}(1/\sqrt{N})
$$

Also mentioned: $$
\frac{1}{N^2}\sum_{n,m} F(\theta_n \eta) F(\theta_m \eta) \rightarrow D
$$

$$
\overline{x}_N = \frac{1}{N-N_0}\sum_{n=N_0}^N x_n
$$

$$
\frac{1}{N-N_0}\sum_{m=N_0}^N (x_m - \overline{x}_N)=0
$$

Let's start with the working from before: $$
C_{\text{lag}k} &= \frac{1}{N-N_0}\sum_{n=0}^{N-N_0}\left[ \left({\mathbf x}_{n+N_0} - \mathbb{E}({\mathbf x}) \right) \left({\mathbf x}_{n+N_0+k} - \mathbb{E}({\mathbf x}) \right)^\top \right]\\
&= \frac{1}{N-N_0}\sum_{n=N_0}^{N}\left[ \left({\mathbf x}_{n} - \mathbb{E}({\mathbf x}) \right) \left({\mathbf x}_{n+k} - \mathbb{E}({\mathbf x}) \right)^\top \right]
$$ Concentrating on the inside: $$
\text{summand} =&~ \left[B^n({\mathbf x}_0 - F(\eta)) +F(\theta_n \eta) - \bar{{\mathbf x}}\right]\left[B^{n+k}({\mathbf x}_0 - F(\eta)) +F(\theta_{n+k} \eta) - \bar{{\mathbf x}}\right]^\top\\
=&~ \left[B^n \left({\mathbf x}_0 - F(\eta)\right)\right]^2 (B^\top)^k + F(\theta_n \eta)F(\theta_{n+k} \eta)^\top + \bar{{\mathbf x}}^2 ...\\
&+ \left[B^n \left({\mathbf x}_0 - F(\eta)\right)\right]F(\theta_{n+k} \eta)^\top... \\
&+ F(\theta_n \eta)\left[B^n \left({\mathbf x}_0 - F(\eta)\right)\right]^\top (B^\top)^k ...\\
&- \left[B^n \left({\mathbf x}_0 - F(\eta)\right)\right]\bar{{\mathbf x}}^\top... \\
&- \bar{{\mathbf x}}\left[B^n \left({\mathbf x}_0 - F(\eta)\right)\right]^\top (B^\top)^k ...\\
&- \bar{{\mathbf x}}F(\theta_{n+k} \eta)^\top... \\
&- F(\theta_n \eta)\bar{{\mathbf x}}^\top 
$$ The reason we changed notation in the first place to
introduce the sums to infinity was to give the expression for
${\mathbf x}_n$ only a single[^2] dependence on $n$, i.e. not summing to
$n$. Is this useful if we intend to keep all the terms anyway? The
expression for ${\mathbf x}_n$ becomes: $$
{\mathbf x}_n = B^n{\mathbf x}_0 + F_{n-1}(\theta_n \eta)
$$ if we reintroduce the second dependence by defining
$$
F_{m}(\theta_n \eta) := \sum_{j = 0}^{m}B^{j}S\eta_{n-j}
$$ Also, just for fun, note that: $$
F(\theta_n\eta) &= B^n F(\eta) + F_{n-1}(\theta_n \eta)\\
F(\theta_{n+k}\eta) &= B^k F(\theta_n\eta) + F_{k-1}(\theta_{n+k} \eta)\\
(k=1)~~~F(\theta_{n+1}\eta) &= B F(\theta_n\eta) + S\eta_{n+1}
$$ (obviously). Maybe this is a good idea, or maybe there was
a good reason that we decided to get rid of those sums. $$
\text{summand} =&~ \left[B^n{\mathbf x}_0 +F_{n-1}(\theta_n \eta) - \bar{{\mathbf x}}\right]^2\\
=&~ \left[B^n {\mathbf x}_0 \right]^2 + F_{n-1}(\theta_n \eta)^2 + \bar{{\mathbf x}}^2 ...\\
&+ \left[B^n {\mathbf x}_0 \right]F_{n-1}(\theta_{n} \eta)^\top... \\
&+ F_{n-1}(\theta_n \eta)\left[B^n {\mathbf x}_0 \right]^\top ...\\
&- \left[B^n {\mathbf x}_0 \right]\bar{{\mathbf x}}^\top... \\
&- \bar{{\mathbf x}}\left[B^n {\mathbf x}_0 \right]^\top ...\\
&- \bar{{\mathbf x}}F_{n-1}(\theta_{n} \eta)^\top... \\
&- F_{n-1}(\theta_n \eta)\bar{{\mathbf x}}^\top 
$$ Actually, I think it will probably be good for us to
separate the terms, so forget all this.

## The mean

Probably best to start with the mean actually: $$
\overline{x}_N &= \frac{1}{N-N_0}\sum_{n=N_0}^{N} x_n\\
&= \frac{1}{N-N_0}\sum_{n=N_0}^{N} \left[ B^n({\mathbf x}_0 - F(\eta)) +F(\theta_n \eta) \right]\\
&= \left[\frac{1}{N-N_0}\sum_{n=N_0}^{N} B^n \right]({\mathbf x}_0 - F(\eta)) + \left[\frac{1}{N-N_0}\sum_{n=N_0}^{N}F(\theta_n \eta) \right]
$$ Let's simplify the notation a little bit: $$
p(\eta) & := {\mathbf x}_0 - F(\eta)\\
\overline{B^n}_N & := \left[\frac{1}{N-N_0}\sum_{n=N_0}^{N} B^n \right]\\
\overline{F(\theta_n \eta)}_N & := \left[\frac{1}{N-N_0}\sum_{n=N_0}^{N}F(\theta_n \eta) \right]
$$ Which is consistent with how we defined
$\overline{{\mathbf x}}_N$.

## The covariance

Now we need $$
C =&~ \frac{1}{N-N_0}\sum_{n=N_0}^{N}\text{summand}\\
=&~ \frac{1}{\star}\sum \left[ \left[B^n p(\eta)\right]^2 B^{k\top} + F(\theta_n \eta)F(\theta_{n+k} \eta)^\top + \overline{{\mathbf x}}^2\right] ...\\
&+ \frac{1}{\star}\sum \left[B^n p(\eta) F(\theta_{n+k} \eta)^\top \right]... \\
&+ \frac{1}{\star}\sum \left[ F(\theta_n \eta) p(\eta)^\top B^{n\top}\right] B^{k\top} ...\\
&- \overline{B^n}~ p(\eta)\overline{{\mathbf x}}^\top... \\
&- \overline{{\mathbf x}} p(\eta)^\top \overline{B^n}^\top B^{k\top} ...\\
&- \overline{{\mathbf x}}\overline{F(\theta_{n} \eta)}^\top B^{k\top} - \overline{{\mathbf x}}\frac{1}{\star}\sum F_{k-1}(\theta_{n+k} \eta)^\top ... \\
&- \overline{F(\theta_n \eta)}\overline{{\mathbf x}}^\top 
$$ If we use our formula
$\overline{{\mathbf x}} = \overline{B^n}p(\eta) + \overline{F(\theta_n\eta)}$
we can factor out the last four lines into the expression
$$
-\overline{{\mathbf x}}^2\left[\mathbf{I} + B^{k\top}\right] - \overline{{\mathbf x}}\frac{1}{N-N_0}\sum_{n=N_0}^{N} F_{k-1}(\theta_{n+k} \eta)^\top 
$$ which becomes $-2\overline{{\mathbf x}}^2$ for $k=0$, as
you would expect.

Remember that we are calculating $$
\frac{1}{N}\sum \left({\mathbf x}-\overline{{\mathbf x}}\right)^2
$$ which is effectively $$
\mathbb{E}\left({\mathbf x}-\mathbb{E}({\mathbf x})\right)^2 & = \mathbb{E}({\mathbf x}^2) - \left(\mathbb{E}({\mathbf x})\right)^2
$$ Also, let's simplify the notation a little bit. We said
$p(\eta) := {\mathbf x}_0 - F(\eta)$, it would be more useful, or at
least more attractive, to define $$
F_0(\eta) & := F(\eta) - {\mathbf x}_0
$$ equal to $-p(\eta)$.\
Now, recall that we are trying to find $$
\sum_n (x_n - \overline{x})^2
$$ We ought to group the terms more sensibly here.
$$
{\mathbf x}_n - \overline{{\mathbf x}} &= B^nF_0(\eta) + F(\theta_n\eta) - \overline{B_N}F_0(\eta) - \overline{F_N}\\
&= \left[B^n - \overline{B_N}\right]F_0(\eta) + \left[F(\theta_n\eta) - \overline{F_N}\right]
$$ We then can write $$
C &= \frac{1}{N-N_0}\sum_{n=N_0}^{N} ({\mathbf x}_n - \overline{{\mathbf x}})^2 \\
& = \frac{1}{\cdot}\sum 
$$

## Further comments

So far in this section we have shown that the EOF assumption is valid in
the case of the system of equation
[\[sytem_eqn_1\]](#sytem_eqn_1)
, subject to several assumptions. The next step
is to consider the cases of a three (or higher) dimensional system, an
$n$-dimensional system, where $B$ is non-diagonalisable, and where the
system is non-stationary. That is, where $B$ is has a time dependence
and one of its eigenvalues approaches 1 (from below).

It will probably not be possible to calculate the EOF explicitly where
$B$ is non-diagonalisable, and when $B$ is time-dependent, therefore we
may infer patterns from repeated simulations in Matlab.

[^1]: also known as Principal Component Analysis (PCA)

[^2]: actually there is still a second dependence in the $\eta_n$ terms.
