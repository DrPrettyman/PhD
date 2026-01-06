# Introduction

The method of Empirical Orthogonal Functions (EOF) is commonly used in
climate research (vonstorch Chapter 13) to reduce the dimensionality of
multi-dimensional systems. The method aims to "capture" most of the
"interesting" behaviour of the system (held2004). We project the
multi-dimensional system onto an orthogonal basis such that the first
component of the system in the new basis has maximal variance and the
$n^{\text{th}}$ component has maximal variance given the first $n-1$
basis vectors. One may then study only the first $k$ components of the
system in the new basis, where $k$ is less than the dimension of the
system and is chosen so that, say, 95% of the total variance is
captured. In many applications only the one-dimensional system of the
first component is considered.\
We wish to ask the question: how useful or relevant is the first EOF in
the detection or prediction of tipping points? That is, are there cases
where the relevant information relevant to tipping, such increasing
autocorrelation (scheffer2009), is not captured by the first EOF? We
attempt to answer this question by studying the stochastic system
eqn.[\[sytem_eqn_1\]](#sytem_eqn_1)
, $$
{\mathbf x}_{k+1} = B{\mathbf x}_k + S\eta_k,

$$ where the ${\mathbf \eta}_k$ are column vectors with each
element $\sim N(0,1)$, iid. Suppose that $B$ is diagonalisable with real
eigenvalues $\mu_{i}$. In the case that all $|\mu_{i}|<1$,
${\mathbf x}_n$ will tend to zero but it will tend to zero more slowly
in the direction $\mathbf{v}_{\max}$, the eigenvector corresponding to
$\mu_{\max} = \max_{i}|\mu_{i}|$. If we allow $\mu_{\max}$ to vary a
critical transition occurs at $|\mu_{\max}|=1$ and $|\mu_{\max}|>1$ will
cause the ${\mathbf x}_n$ to tend to infinity in the direction
$\mathbf{v}_{\max}$. If we project the series ${\mathbf x}_n$ onto the
vector $\mathbf{v}_{\max}$, we expect to see an increase in
autocorrelation as $\mu_{\max} \rightarrow 1$ (scheffer2009). If the
first EOF is to capture this autocorrelation and provide a good
predictor of the tipping point, we would expect that the first EOF
score, $\mathbf{w}_1$, is very close to $\mathbf{v}_{\max}$.\
To simplify our working, we observe that $$
{\mathbf x}_k &= B^k{\mathbf x}_0 + \sum_{i=1}^{k} B^{k-i}S{\mathbf \eta}_i \\
&= \sum_{s=0}^{\infty} B^{s} S {\mathbf \eta}_{k-s} - B^k \left(\sum_{s=0}^{\infty} B^{s} S {\mathbf \eta}_{-s} - {\mathbf x}_0\right).
$$ We now have only a single dependence on $k$, in the $B^k$
term, except for in the noise term $\eta_{k-s}$ which is relevant when
calculating variance (if we take the expectation of the product of two
$\eta$ terms).

# Empirical calculation of the EOFs

The EOF method requires a mean-centred series, it is common to replace
the $i\textsuperscript{th}$ element of a series ${\mathbf x}_n$, which
we call ${\mathbf x}_n^{(i)}$, with $$
{\mathbf y}_n^{(i)} = {\mathbf x}_n^{(i)} - \frac{1}{N}\sum_{j = 1}^N {\mathbf x}_j^{(i)},

$$ forming a new series $[{\mathbf y}_n]_{n=1}^N$, then form
a matrix $Y$ where the $n\textsuperscript{th}$ row from the bottom is
the row vector ${\mathbf y}_n^\top$. We next project $Y$ onto a new
basis to form $T = YW$ where $W$ is the matrix of eigenvectors of
$C = \text{Cov}(Y) = \frac{1}{N-1}Y^\top Y$. The columns of $W$ are
arranged such that the first column, $\mathbf{w}_1$, corresponds to the
largest eigenvalue of $C$, $\lambda_1$, and so on. If we only require
the first EOF (the first column of $T$), we need calculate
$Y\mathbf{w}_1$.\
We here attempt to calculate $C$ and its eigenvectors for a general
stochastic system in the form of
eqn.[\[sytem_eqn_1\]](#sytem_eqn_1)
.

## Finding the mean

We wish to calculate the emipical mean of the series
$\{{\mathbf x}_k\}$: $$
\frac{1}{n}\sum_{k=0}^{n-1} {\mathbf x}_{N_0+k} &= \sum_{s=0}^{\infty} B^s S \frac{1}{n}\sum_{k=0}^{n-1}\eta_{N_0+k-s} - B^{N_0} \frac{1}{n}\sum_{k=0}^{n-1} B^k \left(\sum_{s=0}^{\infty} B^{s} S {\mathbf \eta}_{-s} - {\mathbf x}_0\right)\\
&=  B^{N_0} \frac{1}{n} (I-B)^{-1}(I-B^n)\left({\mathbf x}_0 - \sum_{s=0}^{\infty} B^{s} S {\mathbf \eta}_{-s} \right),

$$ since
$\frac{1}{n}\sum_{k=0}^{n-1}\eta_{N_0+k-s} \rightarrow \mathbb{E}(\eta_0) = 0$
and $\sum_{k=0}^{n-1} B^k = (I-B)^{-1}(I-B^n)$, where we have replaced
$k$ with $N_0+k$. Where all eigenvalues of $B$ are $<1$, we may choose
$N_0$ such that the RHS in
eqn.[\[empirical_mean\]](#empirical_mean)
 is arbitrarily close to zero. In this case
there is no tipping point. Assume that $B$ is diagonalizable with real
eigenvalues, therefore we may use a change of basis to assume $B$ is
diagonal. Assume all elements of $B$ are $<1$ but the first element on
the diagonal is made to vary such that it approaches $1$, so that $B$ is
looks like, for example, $$
B(t) = \left(\begin{array}{ccc}
0.99+10^{-8}t & 0 & 0\\
0 & 0.6 & 0\\
0 & 0 & 0.7
\end{array}
\right).
$$ In this example the critical transition will occur at
$t=10^{6}$ and

Which we might as well say is arbitrarily close to zero, for a choice of
$n$ and $N_0$.\
Obviously each element of $\bar{{\mathbf x}}$ is either $0$, $1$ or
$\pm\infty$.

## Finding the covariance

The covariance matrix $C$ of $[{\mathbf x}_{m+N_0}]$ is given by
$$
C[i,j] = \mathbb{E}\left[ ({\mathbf x}_{k+N_0}^{(i)} - \mathbb{E}({\mathbf x}_{k+N_0}^{(i)}))({\mathbf x}_{k+N_0}^{(j)} - \mathbb{E}({\mathbf x}_{k+N_0}^{(j)}))  \right].
$$ Using the result $\mathbb{E}({\mathbf x})=0$ we write
$$
C &= \frac{1}{N}\sum_{k=0}^{N-1}\left[ ({\mathbf x}_{k+N_0})({\mathbf x}_{k+N_0})^\top \right]\\
&= \frac{1}{N}\sum_{k=0}^{N-1}\left[ (\mathbf{p}_{k+N_0} - B^{k+N_0}\mathbf{q})(\mathbf{p}_{k+N_0} - B^{k+N_0}\mathbf{q})^\top \right]\\
& = \frac{1}{N}\sum_{k=0}^{N-1}\left[(\mathbf{p}_{k+N_0})(\mathbf{p}_{k+N_0})^\top \right]
$$ Where $$
\mathbf{p}_k := \sum_{s=0}^{\infty} B^{s} S {\mathbf \eta}_{k-s} ~~~~~
\mathbf{q} := \sum_{s=0}^{\infty} B^{s} S {\mathbf \eta}_{-s} - {\mathbf x}_0
$$ and we have used a choice of $N_0$ to dismiss the
$\mathbf{q}$ as zero. Now we take the expected value $$
\mathbb{E}(C) &= \frac{1}{N}\sum_{k=0}^{N-1}\left[\mathbb{E}\left((\mathbf{p}_{k+N_0})(\mathbf{p}_{k+N_0})^\top\right)\right]\\
&= \frac{1}{N}\sum_{k=0}^{N-1}\left[\sum_{s=0}^\infty \sum_{r=0}^\infty B^s S\mathbb{E}\left[(\eta_{k+N_0-s})(\eta_{k+N_0-r})^\top\right] S^\top (B^\top)^r\right]\\
& = \sum_{s=0}^\infty B^s S S^\top (B^\top)^s
$$ since
$\mathbb{E}((\eta_{k+N_0-s})(\eta_{k+N_0-r})^\top) = 0$ except where
$r = s$ it is the identity matrix. Diminishing this removes dependence
on $k$, therefore removing the sum over $k$. Note that when we have
$B = \text{diag}(b_1, b_2, ...)$ and $S = \text{diag}(s_1, s_2, ...)$,
we get the diagonal matrix: $$
\mathbb{E}([C]_{ii}) = s_i^2\sum_{r=0}^\infty b_i^{2r}
$$

## Time-lag covariance

We may also consider the covariance of a time-shifted series:
$$
C[i,j] &= \mathbb{E}\left[ ({\mathbf x}_{k+N_0}^{(i)} - \mathbb{E}({\mathbf x}_{k+N_0}^{(i)}))({\mathbf x}_{k+l+N_0}^{(j)} - \mathbb{E}({\mathbf x}_{k+l+N_0}^{(j)}))  \right]
$$ In this case we find that $$
\mathbb{E}(C) = \mathbb{E}\left[(\mathbf{p}_{k+N_0})(\mathbf{p}_{k+l+N_0})^\top\right] = & \sum_{s=0}^\infty B^s S S^\top (B^\top)^{s+l}
$$ which happens to be the same as what we found for the lag
zero ($l=0$) case, end-multiplied by $(B^\top)^l$.

# Finding Eigenvectors

Recall that we have found $$
D:=\mathbb{E}(C) = & \sum_{s=0}^\infty B^s S S^\top (B^\top)^s,
$$ where we have chosen a large enough $N_0$. It might be
useful to note that we can define $D$ intrinsically by $$
D = & SS^\top + B D B^\top.
$$ In the fairly trivial 1-dimension case we can solve for
$D$: $$
d = \frac{s^2 }{1-b^2}
$$

## $B$ diagonal - 2D system

If we stick to the 2-Dimensional case, and use the restriction that $B$
is diagonal, then we get $$
D = \left[ 
\begin{array}{cc}
\frac{s_{12}^2+s_{11}^2}{1-b_{11}^2} & \frac{s_{12}s_{22}+s_{11}s_{21}}{1-b_{11}b_{22}}\\
\frac{s_{12}s_{22}+s_{11}s_{21}}{1-b_{11}b_{22}} & \frac{s_{22}^2+s_{21}^2}{1-b_{22}^2}
\end{array}
\right]

$$ which is pleasingly similar to the 1-D case. In general,
the eigenvalues of symmetric matrix $\left(
\begin{array}{cc}
a&b\\
b&c
\end{array}
\right)$ are $\frac{1}{2}\left(a+c\pm\sqrt{(a-c)^2+4b^2}\right)$ and the
positive square root will give the largest eigenvalue. Note that for
$b=0$ the difference between the two eigenvalues is $|a-c|$ but for non
zero $b$ this difference increases -- the eigenvalues become more
distinct. For matrix $D$ this corresponds to the situation where $S$ is
diagonal (or reverse-diagonal, or one of the rows is zero).\
The eigenvector corresponding to the largest eigenvalue (taking the
positive root) is $$
\left(
\begin{array}{c}
a-c + \sqrt{(a-c)^2+4b^2}\\
2b
\end{array}
\right)

$$ In the case of matrix $D$ the first and second components
are $$
\frac{s_{12}^2+s_{11}^2}{1-b_{11}^2}-\frac{s_{22}^2+s_{21}^2}{1-b_{22}^2} + \sqrt{\left(\frac{s_{12}^2+s_{11}^2}{1-b_{11}^2}-\frac{s_{22}^2+s_{21}^2}{1-b_{22}^2}\right)^2+4\left(\frac{s_{12}s_{22}+s_{11}s_{21}}{1-b_{11}b_{22}}\right)^2}
$$ and $$
2\left(\frac{s_{12}s_{22}+s_{11}s_{21}}{1-b_{11}b_{22}}
\right)
$$ respectively.\
The assumption is that projecting onto this eigenvector, which maximises
variance, captures the interesting behaviour of the system. We would
therefore expect that this eigenvector has something to do with the
eigenvector corresponding to the Largest eigenvalue of $B$ (closest to
1), since this is the direction in which the system travels slowest to
zero. A bifurcation occurs when one eigenvalue approaches 1.\
Make the choice that $b_{11}\approx 1$ (from below), then $1-b_{11}$ is
very small. In \[the longer version of this\] we expand the terms in the
eigenvector formula (eqn.
[\[largest_eigenvector\]](#largest_eigenvector)
) in leading order terms of
$(1-b_{11})$, if we ignore terms in $\mathcal{O}(1-b_{11})$ then the
principal eigenvector becomes $$
\left(\frac{s_{12}^2+s_{11}^2}{1-b_{11}^2}-\frac{s_{22}^2+s_{21}^2}{1-b_{22}^2} ~,~\frac{s_{12}s_{22}+s_{11}s_{21}}{1-b_{22}}
\right)^\top
$$ which we would expect to be equivalent to $(1,0)^\top$,
given that $1/(1-b_{11}^2)$ is very large. If $S$ is diagonal then this
is always the case, otherwise it may be the case that this will be
closer to the direction of $(0,1)^\top$ (corresponding to $b_{22}$), but
this is only if $s_{11},s_{12}$ are very small and $s_{21},s_{22}$ are
very large. In this case it is already very obvious that the largest
variance will be on the second-component timeseries rather than the
first-component timeseries, it is simply a case of a very large noise
obscuring the signal (in this case the 'signal' is the impending tipping
point as $b_{11}$ approaches 1).

### summary of $B$ diagonal case

Where $B$ is diagonal we have the two systems $$
x_t &= b_{11}x_{t-1} + (s_{11},s_{12})\underline{\eta}_t\\
y_t &= b_{22}y_{t-1} + (s_{21},s_{22})\underline{\eta}_t
$$ The EOF method projects the $x$ and $y$ onto a vector such
that the variance is maximised. Usually this would be (close to) the $x$
direction if $b_{11}$ is close to 1, however it may not be if
$(s_{11},s_{12})$ are small and $(s_{21},s_{22})$ are large. In this
case $x$ is a slow curve towards zero and $y$ is white noise with a
large variance. It is obvious (and unfortunately trivial) that this
"breaks the EOF method" --the variance is actually larger in the $y$
direction-- and really did not require so much analysis.\
We also discovered that the eigenvalues of $D$ become less distinct as
$S$ becomes 'more diagonal' - the non-diagonal elements become smaller.
That is, when there is less correlation in the noise terms, it becomes
more difficult to determine which is the principal eigenvalue (and
therefore which eigenvector to project onto).

## $B$ non-diagonal

If $S$ is diagonal but $B$ is not, then we have a lot more terms, but
using a *computer* we find that $$
d_{11}=&
-\frac{1}{k}\left[
(b_{11}b_{12}^2b_{22}-b_{12}^3b_{21}+b_{12}^2)s_{22}^2+(b_{11}b_{22}^3+(-b_{12}b_{21}-1)b_{22}^2-b_{11}b_{22}-b_{12}b_{21}+1)s_{11}^2
\right]\\
d_{12}=&
\frac{1}{k}\left[
((b_{11}^2-1)b_{12}b_{22}-b_{11}b_{12}^2b_{21})s_{22}^2+
(b_{11}b_{21}b_{22}^2-b_{12}b_{21}^2b_{22}-b_{11}b_{21})s_{11}^2
\right]\\
d_{21}=&
\frac{1}{k}\left[
((b_{11}^2-1)b_{12}b_{22}-b_{11}b_{12}^2b_{21})s_{22}^2+
(b_{11}b_{21}b_{22}^2-b_{12}b_{21}^2b_{22}-b_{11}b_{21})s_{11}^2
\right]\\
d_{22}=&
-\frac{1}{k}\left[
((b_{11}^3-b_{11})b_{22}+(-b_{11}^2-1)b_{12}b_{21}-b_{11}^2+1)s_{22}^2+
(b_{11}b_{21}^2b_{22}-b_{12}b_{21}^3+b_{21}^2)s_{11}^2
\right]
$$ where $$
k =& (b_{11}^3-b_{11})b_{22}^3+
((1-3b_{11}^2)b_{12}b_{21}-b_{11}^2+1)b_{22}^2+\\
 & (3b_{11}b_{12}^2b_{21}^2-b_{11}^3+b_{11})b_{22}-b_{12}^3b_{21}^3+b_{12}^2b_{21}^2+\\
 & (b_{11}^2+1)b_{12}b_{21}+b_{11}^2-1
$$ If neither $S$ nor $B$ is diagonal then it is very hard
to fit on the page. The denominator $k$ is the same but there are even
more terms in the numerator.
