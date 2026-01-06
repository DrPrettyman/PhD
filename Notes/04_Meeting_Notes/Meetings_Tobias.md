# 26 May 2017

## Tipping points

We discussed that there is no good definition of a tipping point. That
the typical tipping from one state to another in a double well system is
a combination of noise (c.f. "noise induced transition") and a
becoming-shallower of the well (c.f. "genuine bifurcation"). A
transition caused only by the white noise, we cannot predict, because it
happens at random. However, if the potential changes shape, we can see
that the noise moves all in one direction. Hence autocorrelation.\
I commented some time ago about the example in (livina2011):
$$


\dot{z}(t) & = -(z^4 - 2z^2)' + \sigma(t)\eta \\
\sigma(t) & = -0.00007t+1.50045.

$$ In this system, the noise term grows smaller, but the
exact same output is found by making the wells steeper. Because the size
of the noise changes, this is a genuine bifurcation. A "noised-induced
transition", simply precipitated by the noise alone, surely cannot be
predicted. However, I think there is a separate problem where we can
estimate the shape of the potential, then we can see if we are already
close to a saddle and so more likely to tip over into the other well.\

1.  If we see that $x$ has increased 5 time-steps in a row, is this by
    chance? and then it will just as likely decrease next time as
    continue too increase. Or is it because the well has become
    shallower (or convex) and so we can say \"yes, it will continue to
    increase.\"\

2.  A separate problem: we see that $x$ is close to a value for some
    time, so it is in well. How steep is the well? How close is the
    saddle to the trough?

## Improving 2D ACF

Also, the equation for a 2D analogue of the ACF: $$
\mathbf{x}_{t+1} = A\mathbf{x}_t + \mathbf{c} + \mathbf{\varepsilon}_t
$$ $$
A=  \left[E({\mathbf x}_t{\mathbf x}_t^\top)-\bar{{\mathbf x}}\bar{{\mathbf x}}^\top\right]^{-1} \left[E({\mathbf x}_{t+1}{\mathbf x}_t^\top)-\bar{{\mathbf x}}\bar{{\mathbf x}}^\top\right]
$$ (williamson2015), which is designed to look such as the
1D version: $$
x_{t+1} = ax_t + c + \varepsilon_t,
$$ $$
a = \frac{E(x_{t+1}x_t)-\bar{x}^2}{E(x_{t}^2)-\bar{x}^2}.
$$\
We have been already studying the system $$
{\mathbf x}_{k+1} = B{\mathbf x}_k + S\eta_k,

$$ So should make some informed judgement of how to
reconstruct $B$ from a measurement of the covariance of the
${\mathbf x}$'s. Did we already calculate
$\left[E({\mathbf x}_t{\mathbf x}_t^\top)-\bar{{\mathbf x}}\bar{{\mathbf x}}^\top\right]$?
This is just covariance of ${\mathbf x}$, which is what we call $C$ in
our notes ($D = \mathbb{E}(C)$).\
We calculated that $$
D = \sum_{s=0}^\infty B^s S S^\top (B^\top)^s

$$ and it is easy to show that the 'time lag covariance''
$$
D_{\text{lag}=1} = \sum_{s=0}^\infty B^s S S^\top (B^\top)^{s+1}
$$ so $D_{\text{lag}=0}^{-1}D_{\text{lag}=1} = B$. With a
finite series such as would be available from data, we must ask if this
equation ([\[may17_eqn_for_D\]](#may17_eqn_for_D)
) is correct, because although
$D = \mathbb{E}(C)$, $D$ may be in fact very different to $C$ when $C$
is calculated using a short, single series of real data. Then we must
express $$
C = \sum_{s=0}^\infty B^s S S^\top (B^\top)^s + \text{error}.
$$

## other news

We discussed that the 2D method is useful in the event that for a system
$(x,y)$, we see no rising ACF (or other EWS) in the series $x$, nor in
the series $y$, but when we somehow combine the two (such as taking
eigenvectors of a Jacobian etc.) we see a signal. IS such a system
realistic? It is presumably possible to construct such a system, but it
may not occur so often in physical systems.\
I was attempting to devise such a system by taking $X$ as a classic
pitchfork bifurcation, and attempting to decompose
$x_t = \sqrt{\alpha p_t^2 + \beta q_t^2}$ where $p$ and $q$ are simply
non-bifurcating systems (such that probably no rise in ACF will be
observed). I think this is a bit difficult for a first attempt, maybe
just try a simple projection.\
On the other hand, whichever method one creates (such as the
(williamson2015) method) it will presumably be possible to construct a
system for which it doesn't work - when you perform the method it says
nothing, but when you simply plot the ACF of either $x$ or $y$ you see a
clear signal.\
Note: it is more useful to determine for which systems a method *does*
work, than it is to create one system for which it does not.

# 30 May 2017

## Tipping point definition

We discussed the definition of tipping point, further from the previous
meeting. My comment about equation
[\[may17_decreasing_noise_wells\]](#may17_decreasing_noise_wells)
 is essentially that to
increase the noise is the same as to make the well shallower (in this
sort of system at least). There are three parameters (the coefficients
of $z^4$, $z^2$ and $\eta$) and we are able to change what we see by
rescaling $z$ and $t$, so really we are able to eliminate two parameters
and see that the whole thing is governed by a single parameter dictating
the steepness of the wells -- at least up to a rescaling of $z$ and $t$.

## Autocorrelation

To measure the autocorrelation is to approximate the system by a linear
model. I have previously been concerned by this but, it seems, this is
usually all right if the system doesn't change much inside the time
window. However, note that we need an infinitely large window for the
statistics to be correct. Also note that the system looks less linear as
we leave the bottom of the well: as we approach the tipping point the
ACF (the method for detecting the tipping point) becomes less accurate.\
Also, close to the saddle point the curvature decreases, it becomes
easier to approach the saddle the close we get.\
It all is worth considering.

## Recalculating equation [\[may17_sytem_eqn_1\]](#may17_sytem_eqn_1) 

Tobias suggests that we recalculate equation
[\[may17_sytem_eqn_1\]](#may17_sytem_eqn_1)
 using a notation: $$
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

# 6 June 2017

## calculating the error

What is required is to revisit all the calculations involved in the EOF
method, without discarding any $N_0$ or $N$ terms, attempting to use a
more compact notation. Then when we have an enormous expression for
$D=\mathbb{E}(C)$ we can try to group the terms into $$
D=\mathbb{E}(C) = \sum_{s=0}^\infty B^s S S^\top (B^\top)^s + \text{error}.
$$ We could say that previously we have calculated
$$
\lim_{N\gg N_0 \rightarrow\infty}\left[D\right]= \sum_{s=0}^\infty B^s S S^\top (B^\top)^s
$$ but now we want to remove this limit assumption.\
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
${\mathbf x}_n$ only a single[^1] dependence on $n$, i.e. not summing to
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

# 8 June 2017 - meeting in Reading with Valerie also

## notes taken from conversation with Valerie and Tobias about writing a paper

1.  Novel results already exist in report - write it up

2.  Reproduction of results from Williamson et al. in report -- do this
    with a 'new' system instead of reproducing.

3.  It is good practice to create all plots in the same style (.fig in
    matlab so that it can be edited later, also .eps). This has the
    benefit of removing the need to think for ages about the format of a
    figure - it becomes automatic.

4.  data $\rightarrow$ data analysis $\rightarrow$ conjecture "what is
    the simplest model to reproduce this data?" $\rightarrow$ create
    model $\rightarrow$ analysis of artificial model data. Cannot expect
    the result to be universal.

5.  Noise properties change over time - this is not usually appreciated
    in meteorology etc. where maybe only white noise in imposed
    uniformly.

6.  Redo all figures **NOW**.

7.  Keep a lab book. What to do each day, at the end of the day write
    what is done. Small picture thinking.

8.  read technical specifications required by the journal. If it makes
    no sense, ask.

9.  Springer: climate dynamics

10. email Valerie all the time.

11. Valerie is coming to Exeter in July so possibly could meet.

12. Literature on hurricane models?

13. In the introduction there will be 20 to 30 citations "they did is
    this way", "they did it another way". If it is not *your* way, you
    don't need to know it in detail - just skim.

## notes on the ongoing calculation of the error terms in equation [\[may17_eqn_for_D\]](#may17_eqn_for_D)

Remember that we are calculating $$
\frac{1}{N}\sum \left({\mathbf x}-\overline{{\mathbf x}}\right)^2
$$ which is effectively $$
\mathbb{E}\left({\mathbf x}-\mathbb{E}({\mathbf x})\right)^2 & = \mathbb{E}({\mathbf x}^2) - \left(\mathbb{E}({\mathbf x})\right)^2
$$

# 21 June 2017 

Also, let's simplify the notation a little bit. We said
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

# 11th December 2017

Meeting with Valeria and Tobias in Reading.

- We have discussed the hurricane model in (holland1980), probably it
  is possible to adapt this model to what we want - a model of the sea
  level pressure at a fixed point in the vicinity of a hurricane,
  changing over time as the hurricane approaches.

- When designing a model, we should play with the parameters (including
  adding noise) until the PS-, ACF- and DFA-indicators behave
  realistically. Maybe this will give an insight into why some
  hurricanes show a strong increasing PS-indicator and others do not at
  all (although in the mean over all hurricanes, there is an increase).

- Also, we want to move to look at the EOF components of gridded data -
  i.e. to reduce the dimension of gridded data. Maybe it will be nice to
  see an EWS in this, the same as we can see with the weather station
  data.

- Also, having sourced some gridded data, maybe from ECMWF, we can
  attempt to triangulate the trajectory of a hurricane be observing the
  strength of the EWS in two or three different locations nearby. Maybe
  this will also involve EOF.

- I have already experimented trying to see an EWS from two variables.
  In the case of wind speed + pressure there was no noticable benefit
  over just using pressure. I should write this up -with plots.

**Next meeting 2pm 10th January.** also meeting Tobias via Skype, Monday
18th December - 9:30am.

[^1]: actually there is still a second dependence in the $\eta_n$ terms.
