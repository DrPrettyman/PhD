# DFA Method

From (kantelhardt2001), DFA is a four-step process. We have our data
$x$, the size of $x$, $N$, the length of the segments, $s$, and the
order of the polynomial fit, $n$.

### Step 1

Determine the 'profile' $Y$, which seems to be defined as the cumulative
sum: $$Y(i) = \sum_{k=0}^{i} x(k).$$ Kantelhardt subtracts the mean but
then says that it isn't necessary.

### Step 2

Divide the profile $Y$ into non overlapping segments of length $s$,
there will be $N_s = \lfloor N/s \rfloor$ such segments starting from
the first entry in $Y$, and this collection of $N_s$ segments will
exclude the last few entries of $Y$ if $N$ is not an exact multiple of
$s$. To make use of those entries, also define another $N_s$ segments
starting from the last entry in $Y$, thus excluding the first few
entries.

### Step 3

For each segment (there are $2N_s$ segments), find a polynomial fit (of
order $n$) and evaluate it on the same range as $x$ (or $Y$) to give the
series $\{p(i)\}_i$. The *Detrended* time series is given in each
segment: $$Y_s(i) = Y(i) - p(i).$$ Figure
[1](#DFApolyfit) shows an
example of the first part of this step. The figure shows the segments
starting from the first entry, thus the last few entries are not used
and the polynomial fit is equal to 0.

![Polynomial (quadratic) fit on segments of length 100 for some
artificial series of length 440. The blue shows the 'profile' of the
data $\{Y(i)\}$ and the red show the quadratic fit. Note that the last
40 points in $Y$ are not fitted because the segments run
out.](../images/polyfit_for_DFA.png){#DFApolyfit
width="0.5\\paperwidth"}

### Step 4

For each segment calculate the variance
$$F_s = \frac{1}{s}\sum_i Y_s(i)^2,$$ the sum is over all points in the
segment. Then calculate $$F^{(n)}(s) = \sqrt{\frac{1}{2N_s}\sum F_s}$$
where the sum here is over all segments ($F_s$ is calculated *for each*
segment).

# A closer look at DFA

(kantelhardt2001) quotes the equation $$
F^{(n)}(s) \propto s^\alpha 

$$ which holds for large $s$. The 'fluctuations exponent'
$\alpha$ is related to the 'correlation exponent' $\gamma$.\

## MatLab

We use MatLab to try to replicate the results in (kantelhardt2001), or
at least to see if we can implement DFA accurately. The function `DFA.m`
takes 3 arguments: `data`, `segment_length` ($s$) and `order` ($n$). The
output is the fluctuation function $F^{(n)}(s)$. The function
`DFA_analysis.m` takes 2 arguments: `data` and `order`. The output is an
array of `DFA.m` outputs evaluated with $n = 1, ..., \texttt{order}$.\
Using the data Valerie generated (`data05`, `data09`, `data15`, with
correlations $0.5$, $0.9$ and $1.5$) we perform `DFA_analysis.m` for
`order`=5, the results are in Figure
[2](#DFA_comparison).



![](../images/DFA_05.png)


![](../images/DFA_09.png)

DFA analysis. The scaled fluctuation function 
$F^{(n)}(s)/\sqrt{s}$ over increasing 
s. (left) shows artificial data
`data05`, (right) shows `data09`.


And the same sort of thing is shown in Figure
[3](#graceproject1) only
produced using grace, so there you go.

![DFA. Correlations, from top to bottom: 1.5, 0.9 and
0.5](../images/graceproject1.png)

## The Idea

The idea surely is that one could use DFA to obtain this exponent
$\alpha$ using Eqn. [\[F=s\]](#F=s)
.\
(kantelhardt2001) plots $F^{(n)}(s)/\sqrt{s}$ over increasing $s$, as
we have done, and says you could use a linear fit to estimate $\alpha$.
Since with White Noise you have a horizontal line (see Fig.
[3](#graceproject1)
(bottom)) you have $$
  F^{(3)}(s) / s^{1/2} &= k \\
\Rightarrow  F^{(3)}(s) &= ks^{1/2} \\
\Rightarrow  \alpha &= 1/2 
$$ With the data `data09` (Fig.
[3](#graceproject1)
(middle)) we can do a linear fit and get $$
  \log( F^{(3)}(s) / s^{1/2} ) &\approx 0.44\log(s) - 3.3 \\
\Rightarrow  F^{(3)}(s) / s^{1/2} &= 10^{-3.3}s^{0.44} \\
\Rightarrow  F^{(3)}(s) &= 10^{-3.3}s^{0.94} \\
\Rightarrow  \alpha &= 0.94
$$

Which is pretty close to $0.9$ I guess. Maybe the linear fit is a bit
too steep because of the 'deviation' that Kantelhardt talks about. We
can use $F_{\text{mod}}$ instead to get a better estimate.

# Why does DFA work? / what is it doing?

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

# What next?

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

# Using $F_\text{mod}$

![Showing $F_{\text{mod}}^{(3)}(s)$ and $F^{(3)}(s)$ for
`data09`.](../images/Fmod_vs_F.png)

Figure [4](#Fmod) shows the same
sort of thing as Fig.[3](#graceproject1)
, but only for `data09` and only for a cubic
polynomial fit ($n=3$). The two sets shown are very similar, although
they diverge a bit for low $s$, it appears that
$F_{\text{mod}}^{(3)}(s)$ is *more* linear than the other. However, if
you just use $s>30$ or even $s>50$ then you're still going to get a
pretty good linear fit.\
Using the points shown in Fig.[4](#Fmod)
 we can do a linear fit to estimate $\alpha$ (it should
be about 0.9). The linear fit for the regular $F$ (red line) gives
$\alpha = 0.9368$. Fitting to the blue points (which used $F_\text{mod}$
gives $\alpha = 0.9246$, which is a little bit better I suppose but not
worth[^3] the huge amount of extra time it takes to run the modified
version.\
The regular version needs to find $F(s)$ several times to find a good
linear fit, I would suggest *at least* three (as seen in
Fig.[4](#Fmod), we have used
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

### Comment

Truncating the first two points from the un-modified DFA in
Fig.[4](#Fmod) so we only use
$F(s)$ for $s>30$ looks like it ought to be just as good as
$F_\text{mod}$, but it isn't because of that last point at $s=500$ which
is not in-line with the rest, and it is the same for $F$ and
$F_\text{mod}$. I wonder why\... Anyway, if we knock off the $s=500$
value then we've got a lovely $\alpha=0.91$.\
(kantelhardt2001) does say something about *short term* data so maybe
the point is that we can use DFA even with data sets of length 1000 or
even shorter if we are able to use small value of $s$ for the linear
(i.e. logarithmic) fit.

## The correction function

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

# Comparison of ACF and DFA

We estimate the value of $\alpha$ using DFA in a sliding window of data,
that is, for index $i$ we perform DFA on the selection
$\texttt{data(i-999:i)}$ (for a window size 1000, for example). Using
the "decreasing noise, 2-state system" model the results are shown in
Figure [5](#graceproject2)
.

![The decreasing noise model. The time series $z(t)$ is shown in black.
DFA indicators are found at intervals of 1000 (points shown by square
symbols), ACF indicators are found at every
point.](../images/graceproject2.png)

Figure [5](#graceproject2)
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

[^1]: M.S. Taqqu, V. Teverovsky, and W. Willinger, Fractals 3 (1995) 785

[^2]: (kantelhardt2001) uses $\langle x^2 \rangle$ to mean
    $\frac{1}{N}\sum_{i=1}^N x_i^2$, (that is, $\langle ... \rangle$ is
    the mean) and call *this* the variance. We follow their lead here.

[^3]: In my opinion, right now

[^4]: By squaring out, provided $\alpha = 1/2$.

[^5]: I calculated $\alpha$ at 'better resolution' for $9000<t<11000$
    but it is the same roughly linear decline shown in the graph by the
    dashed line
