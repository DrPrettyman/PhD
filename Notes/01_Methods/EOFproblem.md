Say we have a dynamical system ${\mathbf x}_n$ described by
${\mathbf x}_{n+1} = B{\mathbf x}_n + S{\mathbf \eta}_n$ where $B, S$
are symmetric and the ${\mathbf \eta}_n$ are column vectors with each
element $\sim N(0,1)$, iid.\
If ${\mathbf x}$ is 1-dimension, then the system is an AR(1) model. If
${\mathbf x}$ is many dimensions we might want to only study only the
first EOF score as in (held2004), in the hope that it "captures" most
of the interesting behaviour of the system.\
The question posed: How useful or relevant is the first EOF score?

# Thinking

Let us consider the deterministic system
${\mathbf x}_{n+1} = B{\mathbf x}_n$, what does it look like? It is
possible that the norm of ${\mathbf x}$ gets larger with $n$, so will
quickly go to infinity. We can control this with the condition that $B$
is contacting, or that all of its eigenvalues are $<1$. Now we have a
system that spirals towards zero,
$\exists n \text{~such that~} |{\mathbf x}_n|<c ~ \forall c$.\
Say $W$ is the matrix of eigenvectors of $B$, and $\Lambda$ is the
diagonal matrix of eigenvalues, $BW = W\Lambda$, in the basis of
eigenvectors, $B$ is diagonal. We project ${\mathbf x}_n$ onto the new
basis, $\tilde{{\mathbf x}}_n = W^{-1}{\mathbf x}_n$. So in the new
basis we have $\tilde{{\mathbf x}}_n = \Lambda\tilde{{\mathbf x}}_{n-1}$
or $$
\tilde{x}^{(i)}_n = \lambda^n_{(i)}\tilde{x}^{(i)}_0
$$ component wise, where $\tilde{x}^{(i)}_n$ is the
$i^\text{th}$ component of $\tilde{{\mathbf x}}_n$ and $\lambda_{(i)}$
is the $i^\text{th}$ component of $\Lambda$, or the $i^\text{th}$
eigenvalue of $B$. So all components go to zero, but fastest in the
component where $\lambda_{(i)}$ is smallest. So back to the original
basis, the system goes towards zero fastest in the direction given by
the eigenvector corresponding to the smallest eigenvalue.

# PCA (or EOF) method

The method requires a mean-centred series, it is common to replace the
$i\textsuperscript{th}$ element of ${\mathbf x}_n$, which we call
${\mathbf x}_n^{(i)}$, with $$
{\mathbf y}_n^{(i)} = {\mathbf x}_n^{(i)} - \frac{1}{N}\sum_{j = 1}^N {\mathbf x}_j^{(i)},
$$ forming a new series $[{\mathbf y}_n]_{n=1}^N$. This makes
everything very complicated. Then form a matrix $Y$ where the
$n\textsuperscript{th}$ row from the bottom is the row vector
${\mathbf y}_n^\top$.\
Then all is required is to find a matrix $T$, which is a projection of
$Y$ onto a different basis, and to take the first column.\
The common way to do this is to find the covariance matrix
$C = \frac{1}{N-1}Y^\top Y$, and to find the eigenvectors. The
eigenvector corresponding to the *largest* eigenvalue is the *first*
column of the matrix $W$ and so on. Then $T = YW$. So if we only need
the first EOF score (the first column of $T$), we can find $Y{\bf v}$,
where ${\bf v}$ is the first eigenvalue.

# Initial observations

- The series can be simplified: $$
  {\mathbf x}_n &= B^n{\mathbf x}_0 + B^{n-1}S{\mathbf \eta}_1 + B^{n-2}S{\mathbf \eta}_2 + ... + B^{1}S{\mathbf \eta}_{n-1} + S{\mathbf \eta}_n\\
  &= B^n{\mathbf x}_0 + \sum_{i=1}^{n} B^{n-i}S{\mathbf \eta}_i 
  $$

- : $$
  {\mathbf y}_n &= {\mathbf x}_n - \frac{1}{N}\sum_{j = 1}^N {\mathbf x}_j\\
  &= B^n{\mathbf x}_0 + \sum_{i=1}^{n} B^{n-i}S{\mathbf \eta}_i - \frac{1}{N}\sum_{j = 1}^N \left(B^j{\mathbf x}_0 + \sum_{k=1}^{j} B^{j-k}S{\mathbf \eta}_k \right)\\
  &= \left[ B^n - \frac{1}{N}\sum_{j = 1}^N B^j\right]{\mathbf x}_0 + \left[ \sum_{i=1}^{n} B^{n-i}S{\mathbf \eta}_i  - \frac{1}{N}\sum_{j = 1}^N\sum_{k=1}^{j} B^{j-k}S{\mathbf \eta}_k \right]
  $$

# Calculating the EOF on paper: Hammering approach

We have $N$ observations of a $P$-dimensional system. Each observation
is the $P\times 1$ vector $\underline{x_n}$. There are $N$ observations.
The whole lot of observations is written in an $N\times P$ matrix $X$
where the $n^{th}$ row is $\underline{x_n}^\top$.

$$
X = \begin{bmatrix}
 \underline{x_1}^\top  \\
\vdots \\
\vdots \\
\underline{x_n}^\top 
\end{bmatrix}
= \begin{bmatrix}
x_{11} & \hdots & x_{1P} \\
\vdots & \hdots & \vdots \\
\vdots & \hdots & \vdots \\
x_{N1} & \hdots & x_{NP} 
\end{bmatrix}
$$

suppose we ignore the massively complicating step of "mean-centering",
and skip straight to calculating the $P\times P$ covariance matrix
$C = \frac{1}{N-1} X^\top X$:

$$
[C]_{ab} = \frac{1}{N-1} \sum_{i=1}^N x_{ia} x_{ib} 

$$

Which is the dot product of the time series of the $a^{th}$ variable and
the time series of the $b^{th}$ variable (scaled by the fraction
$\frac{1}{N-1}$). Bear in mind that the value $x_{np}$ is the $p^{th}$
element in the vector $\underline{x_n}$, that is, the value of the
$p^{th}$ variable at time $n$.\
In the particular case of our simple system, we have a form for
$\underline{x_n}$: $$
\underline{x_n} = B^n \underline{x_0} + \sum_{i=1}^n B^{n-i}S{\mathbf \eta}_i

$$

where $B$ and $S$ are given matrices (the index on $B$ represents
exponentiation) and the ${\mathbf \eta}_i$ are a series of random
vectors with each element iid Gaussian.

Now the value $x_{np}$ is the $p^{th}$ element of this vector, so it is
the sum of the $p^{th}$ elements of all the vectors in the sum. Let's
start at the beginning: the $p^{th}$ element of $B^n \underline{x_0}$ is
$\underline{[B^n]_p}^\top \cdot \underline{x_0}$ where
$\underline{[B^n]_p}$ is the $p^{th}$ row of the matrix $B^n$.

Clearly, this is going to get insanely complicated, let's just say that
$B$ is diagonal, with the vector
$\underline{b} = (b_1, b_2, \dots, b_P)$ on the diagonal. Now the
$p^{th}$ element of $B^n \underline{x_0}$ is $b_p^n x_{0p}$. Also, if we
say $S$ is diagonal, the $p^{th}$ element of $B^{n-i}S{\mathbf \eta}_i$
is $b_p^{n-i}s_p[{\mathbf \eta}_i]_p$, where $[{\mathbf \eta}_i]_p$ is
the $p^{th}$ elmt of ${\mathbf \eta}_i$. What the hell, let's just call
it ${\mathbf \eta}_{ip}$.

Now, $$
x_{np} = b_p^n x_{0p} + \sum_{i=1}^n b_p^{n-i}s_p{\mathbf \eta}_{ip}.

$$

So, $$
\sum_{i=1}^N x_{ia}x_{ib} = \sum_{i=1}^N \left[\left(b_a^i x_{0a} + \sum_{j=1}^i b_a^{i-j}s_a{\mathbf \eta}_{ja}\right) \left(b_b^i x_{0b} + \sum_{j=1}^i b_b^{i-j}s_b{\mathbf \eta}_{jb}\right)\right]

$$

which is much uglier than it needs to be because $b$ appears as a
subscript, but even with better notation it doesn't look at all helpful.
These sums inside the brackets aren't going to do anything nice.

I suppose we can take the expected value of all of this, since the
$\eta$ will somehow cancel out or be evaluated in a sense. In any case,
the following is true:

$$
\mathbb{E}(\eta_{ab}\eta_{cd}) = 
\begin{cases}
1 & a=c ~\text{and}~ b=d\\
0 & \text{otherwise}
\end{cases}.

$$

Let's expand the brackets inside the sum:

$$
b_a^i x_{0a}b_b^i x_{0b} + b_a^i x_{0a}\sum_{j=1}^i b_b^{i-j}s_b{\mathbf \eta}_{jb} + b_b^i x_{0b}\sum_{j=1}^i b_a^{i-j}s_a{\mathbf \eta}_{ja} + \left(\sum_{j=1}^i b_a^{i-j}s_a{\mathbf \eta}_{ja}\right)\left(\sum_{k=1}^i b_b^{i-k}s_b{\mathbf \eta}_{kb}\right)

$$

if $a\neq b$ then the expected value of all of this is zero except for
the first part, $$
b_a^i x_{0a}b_b^i x_{0b} = (x_{0a}x_{0b})(b_a b_b)^i.
$$ Then we can write

$$
\mathbb{E}\left(\sum_{i=1}^N \underbrace{x_{ia}x_{ib}}_{a\neq b}\right) = (x_{0a}x_{0b})\sum_{i=1}^N (b_a b_b)^i = (x_{0a}x_{0b})(b_a b_b)\frac{(b_a b_b)^N-1}{(b_a b_b)-1}

$$

If $a=b$ (on the diagonal of the covariance matrix) then the final term
also contributes something. In all the "diagonal" terms in the
expansion, i.e. where $j=k$, then the expected value of the
$\eta_{ja}^2$ is 1, thus we get

$$
\left(b_a^i x_{0a}\right)^2 + \sum_{j=1}^i \left(b_a^{i-j}s_a\right)^2

$$

from the expansion. So we could write

$$
\mathbb{E}\left(\sum_{i=1}^N \underbrace{x_{ia}x_{ib}}_{b=a}\right) = x_{0a}^2\sum_{i=1}^N \left(b_a^i\right)^2 + s_a^2\sum_{i=1}^N\sum_{j=1}^i \left(b_a^{i-j}\right)^2

$$

Is there a neat way to write those series? Yes there is, but how helpful
is it to do so?

$$
x_{0a}^2\sum_{i=1}^N \left(b_a^i\right)^2 & = x_{0a}^2 b_a^2 \frac{b_a^{2N} -1}{b_a^2-1}\\
 s_a^2\sum_{i=1}^N\sum_{j=1}^i \left(b_a^{i-j}\right)^2 & = s_a^2\frac{-1 + 2b_a^2 - (N-1)b_a^{2N} + (N-2)b_a^{2N+2} }{(b_a^2-1)^2}
$$

## Summary so far

Let's take a break and review what we have. We were trying to find the
covariance matrix $C$ and we worked out that we could write:

$$
[C]_{ab} = \frac{1}{N-1} \sum_{i=1}^N x_{ia} x_{ib}. 
$$

In our dynamical system, all values of $\underline{x}$ can be written in
terms of $\underline{x}_0$, so we plugged that in to get equation 3.5:

$$
[C]_{ab} = \frac{1}{N-1}\sum_{i=1}^N \left[\left(b_a^i x_{0a} + \sum_{j=1}^i b_a^{i-j}s_a{\mathbf \eta}_{ja}\right) \left(b_b^i x_{0b} + \sum_{j=1}^i b_b^{i-j}s_b{\mathbf \eta}_{jb}\right)\right].

$$

We noticed that the iid Gaussian terms ($\eta$) appear, so decided that
it might be a good idea to take the expected value. This gives us:

$$
\mathbb{E}([C]_{ab}) =   \begin{cases}
     \frac{1}{N-1} \sum_{i=1}^N \left( x_{0a}^2 \left(b_a^i\right)^2 + s_a^2\sum_{j=1}^i \left(b_a^{i-j}\right)^2 \right) & \text{for } a = b \\     
     \frac{1}{N-1} (x_{0a}x_{0b})\sum_{i=1}^N (b_a b_b)^i & \text{for } a \neq b
  \end{cases}
  
$$

We manipulated these a bit in an attempt to write them without the sums,
this gives us

$$
 \frac{x_{0a}^2 b_a^2 (b_a^{2N} -1)}{(N-1)(b_a^2-1)} + s_a^2 \frac{ -1 + 2b_a^2 - (N-1)b_a^{2N} + (N-2)b_a^{2N+2} }{(N-1)(b_a^2-1)^2}
$$

for the $a=b$ case, and

$$
\frac{1}{N-1}(x_{0a}x_{0b})(b_a b_b)\frac{(b_a b_b)^N-1}{(b_a b_b)-1}
$$

for the $a\neq b$ case.

# Take a step back

## mean-centering

It seems we couldn't be bothered to perform this important step, maybe
because it would be very difficult in general. However, in dealing with
our specific system it is easier. We introduce a constraint on $B$ so
that the system is not unstable. In the case of a diagonal $B$ we just
require that $|b_p|<1\forall p$.

Now we will take a look at eqn. [\[3p4\]](#3p4)
. Let us take the empirical mean over $n$:

$$
\frac{1}{N}\sum_{n=1}^N x_{np} = \frac{1}{N}\sum_{n=1}^N b_p^n x_{0p} + \frac{1}{N}\sum_{n=1}^N \sum_{i=1}^n b_p^{n-i}s_p{\mathbf \eta}_{ip}
$$

As $N$ gets large, the first term goes to zero because the terms quickly
go to zero thanks to $b^n$, and so we are left with the first few terms
divided by (very large) $N$. Also the second part goes to zero,
probably. So if we take a very large $N$ we can say the mean is zero so
no need for mean-centering. I mean obviously the mean is zero because
the system is spiralling around the point $(0,0)$.

## Getting rid of $x_0$

Let's assume that the system is stationary, or at least that it doesn't
matter if we ignore the first few terms. That is, that if we only look
at $x_{k},...,x_N$ instead of $x_1,...,x_N$, the covariance will be the
same. Then you could say that it really doesn't matter what $x_0$ is.
There is some randomness in the system, if $x_k = \alpha$, for all we
know $x_0$ may have been zero. In that case we could just say $x_0=0$,
this saves some trouble. Then eqn [\[3p15\]](#3p15)
 is a bit easier.

## Why?

Why are we doing this with $B$ and $S$ diagonal? This is just a load of
1D systems stuck together, it's not a $P$-dimensional system at all. We
should at least have a more complicated $B$. Maybe stick to finding the
answer to the easy one first though\...

# A new direction

We have so far written

$$
{\mathbf x}_n &= B^n{\mathbf x}_0 + \left[ B^{n-1}S{\mathbf \eta}_1 + B^{n-2}S{\mathbf \eta}_2 + ... + B^{1}S{\mathbf \eta}_{n-1} + S{\mathbf \eta}_n \right]\\
&= B^n{\mathbf x}_0 + \sum_{i=1}^{n} B^{n-i}S{\mathbf \eta}_i 
$$

Without any change to the system, to make things easier, let's do the
following:

$$
{\mathbf x}_k &= B^k{\mathbf x}_0 + \left[S{\mathbf \eta}_k + B^{1}S{\mathbf \eta}_{k-1} + ... + B^{k-2}S{\mathbf \eta}_2 +  B^{k-1}S{\mathbf \eta}_1 \right]\\
&= B^k{\mathbf x}_0 + \sum_{s=0}^{k-1} B^{s} S {\mathbf \eta}_{k-s}\\
&= B^k{\mathbf x}_0 + \left[ \sum_{s=0}^{\infty} B^{s} S {\mathbf \eta}_{k-s} - \sum_{s=k}^{\infty} B^{s} S {\mathbf \eta}_{k-s}\right]\\
&= B^k{\mathbf x}_0 + \left[ \sum_{s=0}^{\infty} B^{s} S {\mathbf \eta}_{k-s} - \sum_{s=0}^{\infty} B^{s+k} S {\mathbf \eta}_{-s}\right]\\
&= \sum_{s=0}^{\infty} B^{s} S {\mathbf \eta}_{k-s} - B^k \left(\sum_{s=0}^{\infty} B^{s} S {\mathbf \eta}_{-s} - {\mathbf x}_0\right)
$$

Now we have only a single dependence on $k$, in the $B^k$, except for in
the noise term $\eta_{k-s}$ which may be relevant when calculating
variance (if we take the expectation of the product of two $\eta$
terms).

## Finding the mean

For later convenience, we also replace $k$ with $N_0+k$. Now to find the
empirical mean of ${\mathbf x}_k$, that is,

$$
\frac{1}{n}\sum_{k=0}^{n-1} {\mathbf x}_k &= \sum_{s=0}^{\infty} B^s S \frac{1}{n}\sum_{k=0}^{n-1}\eta_{N_0+k-s} - B^{N_0} \frac{1}{n}\sum_{k=0}^{n-1} B^k \left(\sum_{s=0}^{\infty} B^{s} S {\mathbf \eta}_{-s} - {\mathbf x}_0\right)
$$

Note that
$\frac{1}{n}\sum_{k=0}^{n-1}\eta_{N_0+k-s} \rightarrow \mathbb{E}(\eta_0)$
since it the empirical mean of some noise. In this case it is zero, so
we may as well ignore the first term. Also note that
$\sum_{k=0}^{n-1} B^k = (I-B)^{-1}(I-B^n)$, therefore we can write:

$$
\frac{1}{n}\sum_{k=0}^{n-1} {\mathbf x}_k &=  B^{N_0} \frac{1}{n} (I-B)^{-1}(I-B^n)\left({\mathbf x}_0 - \sum_{s=0}^{\infty} B^{s} S {\mathbf \eta}_{-s} \right)\\
\left\|\frac{1}{n}\sum_{k=0}^{n-1} {\mathbf x}_k\right\| &\leq \frac{1}{n}\|B\|^{N_0}  \|(I-B)^{-1}\| \left\|{\mathbf x}_0 - \sum_{s=0}^{\infty} B^{s} S {\mathbf \eta}_{-s} \right\| \\
&=: Z
$$

Here we have put the $1/n$ in front and used $\|I-B^n\|\leq 1$ to get
rid of that factor, and we have called it $Z$ so that it has a name.
Note that only $1/n$ and $\|B\|^{N_0}$ have any dependence on anything.
If we "assign a value" to the $\eta$ terms by taking the expectation of
everything, we get that $$
{Z} = C\frac{\|B\|^{N_0}}{n}
$$

where
$C = \left(\|(I-B)^{-1}\|\right)\mathbb{E}\left(\left\|{\mathbf x}_0 - \sum_{s=0}^{\infty} B^{s} S {\mathbf \eta}_{-s} \right\|\right)$
and is just a value. Now say we want to ask the question: What is
$\mathbf{P}(|Z|>c)$? (or $|Z|/c>1$). We can use

$$
\mathbf{P}\left(\frac{|Z|}{c}>1\right) ~\leq~ \frac{1}{c}\mathbb{E}(Z) ~\leq~ C\|B\|^{N_0}\frac{1}{nc}
$$

Which clearly gets very small with very large $n$, but gets small even
faster with a fairly large $N_0$. So choosing an appropriate $N_0$, we
can say that

$$
\left\|\frac{1}{n}\sum_{k=0}^{n-1} {\mathbf x}_k\right\| \leq c ~~~ \forall c
$$ almost surely.

## Finding the covariance

Next we want to calculate the empirical covariance, we will have to
compute something like this:

$$
\frac{1}{N} \sum_{n=1}^N (x_{n+N_0}) - \frac{1}{n}\sum_{k=1}^n x_{k+N_0}) (x_{m+N_0}) - \frac{1}{m}\sum_{k=1}^m x_{k+N_0}),
$$

this is what Tobias sent but clearly there is some mistake with typing.
Lets work it out ourselves.\
The covariance matrix $C$ of $[{\mathbf x}_{m+N_0}]$ is given by

$$
C[i,j] = \mathbb{E}\left[ ({\mathbf x}_{m+N_0}^{(i)} - \mathbb{E}({\mathbf x}_{m+N_0}^{(i)}))({\mathbf x}_{m+k+N_0}^{(j)} - \mathbb{E}({\mathbf x}_{m+k+N_0}^{(j)}))  \right].
$$

We can consider the diagonal, $i=j$, where this then becomes the
auto-covariance of a 1D series (the $i^{th}$ component), then we have

$$
\mathbb{E}\left( x_{m+N_0} x_{m+k+N_0} \right) + \mathbb{E}\left( x_{m+N_0} \right) \mathbb{E}\left( x_{m+k+N_0} \right)

$$

where $[x_m]:=[{\mathbf x}_m^{(i)}]$ is a 1D series.

Wait a minute, this is all wrong. We're finding covariance not
correlation. I think rather we're trying to calculate:

$$
C[i,j] &= \mathbb{E}\left[ ({\mathbf x}_{m+N_0}^{(i)} - \mathbb{E}({\mathbf x}_{m+N_0}^{(i)}))({\mathbf x}_{m+N_0}^{(j)} - \mathbb{E}({\mathbf x}_{m+N_0}^{(j)}))  \right]
$$

Let's have a go:

$$
C = \frac{1}{N}\sum_{k=0}^{N-1}\left[ \left({\mathbf x}_{k+N_0} - \mathbb{E}({\mathbf x}) \right) \left({\mathbf x}_{k+N_0} - \mathbb{E}({\mathbf x}) \right)^\top \right]
$$

If we say (because it simplified things) that
$\mathbb{E}({\mathbf x}) = \frac{1}{N}\sum_{k=0}^{N-1} {\mathbf x}_{k+N_0} = 0$,
which we can probably do by choosing an appropriate $N_0$, then we are
left with:

$$
C = \frac{1}{N}\sum_{k=0}^{N-1}\left[ ({\mathbf x}_{k+N_0})({\mathbf x}_{k+N_0})^\top \right]
$$

Will it help to remember that

$$
{\mathbf x}_k = \sum_{s=0}^{\infty} B^{s} S {\mathbf \eta}_{k-s} - B^k \left(\sum_{s=0}^{\infty} B^{s} S {\mathbf \eta}_{-s} - {\mathbf x}_0\right)?
$$

Probably not\... Maybe we should go back to doing thing component-wise,
but then we have to say things like $B$ is diagonal. Let's have a try
anyway. Say

$$
\mathbf{p}_k &:= \sum_{s=0}^{\infty} B^{s} S {\mathbf \eta}_{k-s}\\
\mathbf{q} &:= \sum_{s=0}^{\infty} B^{s} S {\mathbf \eta}_{-s} - {\mathbf x}_0
$$ Unfortunately $\mathbf{p}_k$ depends on $k$, and both
involve the same $\eta$. Now,

$$
C & = \frac{1}{N}\sum_{k=0}^{N-1}\left[ (\mathbf{p}_{k+N_0} - B^{k+N_0}\mathbf{q})(\mathbf{p}_{k+N_0} - B^{k+N_0}\mathbf{q})^\top \right]\\
& = \frac{1}{N}\sum_{k=0}^{N-1}\left[(\mathbf{p}_{k+N_0})(\mathbf{p}_{k+N_0})^\top + B^{k+N_0}\mathbf{q}\mathbf{q}^\top (B^\top)^{k+N_0} - B^{k+N_0}\mathbf{q}(\mathbf{p}_{k+N_0})^\top - (\mathbf{p}_{k+N_0}) \mathbf{q}^\top(B^\top)^{k+N_0}\right]
$$

Well I think we know that if we split this up into four sums and bring a
$B^{N_0}$ outside whenever we can, we're just going to end up saying
that all these terms are basically zero. Then all we have left is:

$$
C & = \frac{1}{N}\sum_{k=0}^{N-1}\left[(\mathbf{p}_{k+N_0})(\mathbf{p}_{k+N_0})^\top \right]
$$

Let's expand the inside, that is, expand
$(\mathbf{p}_{k+N_0})(\mathbf{p}_{k+N_0})^\top$:

$$
= & \sum_{s=0}^\infty \sum_{r=0}^\infty B^s S(\eta_{k+N_0-s})(\eta_{k+N_0-r})^\top S^\top (B^\top)^r

$$

The matrix $(\eta_{k+N_0-s})(\eta_{k+N_0-r})^\top$ is maybe interesting.
It's expected value is the zero matrix for $r\neq s$ and the identity
matrix for $r=s$. Therefore

$$
\mathbb{E}\left[(\mathbf{p}_{k+N_0})(\mathbf{p}_{k+N_0})^\top\right] = & \sum_{s=0}^\infty B^s S S^\top (B^\top)^s
$$

Which gets rid of $k$, and so this is equal to $\mathbb{E}(C)$, because
the sum disappears with the $k$ (since we sum $N$ terms and divide by
$N$). Also note that we've already agreed to treat $B^n$ as zero for
$n>N_0$, therefore we might as well only sum to $N_0$, where $N_0$ is
large enough. Note that this is symmetric, which is reassuring. Note
that when we have $B = \text{diag}(b_1, b_2, ...)$ and
$S = \text{diag}(s_1, s_2, ...)$, we get the diagonal matrix:

$$
\mathbb{E}([C]_{ii}) = s_i^2\sum_{r=0}^\infty b_i^{2r}
$$

But when we worked the whole thing out component wise we got:

$$
\mathbb{E}([C]_{ii}) &= s_i^2\frac{1}{N-1}\sum_{r=1}^{N}\sum_{t=1}^{r} b_i^{2(t-r)}\\
&= s_i^2\frac{1}{N-1}\sum_{r=0}^{N-1}(N-r)b_i^{2r} \\
&= s_i^2\sum_{r=0}^{N}b_i^{2r} - s_i^2\sum_{r=0}^{N}\frac{r-1}{N-1}b_i^{2r}\\
&= s_i^2\sum_{r=0}^{\infty}b_i^{2r} - s_i^2\sum_{r=0}^{\infty}\frac{r-1 - (r+1)b^{2(N+1)}}{N-1}b_i^{2r}
$$

which is not the same thing. Maybe it is basically the same thing in the
$N\rightarrow\infty$ limit, but still, that's not too great. It's
probably because we introduced $N_0$ and proceeded to ignore a load of
stuff. When I went back to the component wise result I just ignored
everything with $x_0$ based on the $N_0$ principal, probably if I'd done
this properly we would get the same thing. It is curious how the sum to
infinity comes from the rewriting of ${\mathbf x}_k$ whereas the sum to
$N$ comes from the fact that we are taking an empirical covariance by
summing to $N$ and dividing by $N$. And yet the two sums appear in the
final thing in the same place.\
Anyway, why were we doing all of this?

## Time-lag covariance

Equation [\[time_shift_cov\]](#time_shift_cov)
 was dismissed, but maybe it will come in
useful to work it out. In fact the working is very simple, everything is
the same except we replace one of the $k$ with, say, $k+l$. Then when we
get to eqn.
[\[double_sum_expansion\]](#double_sum_expansion)
 we have $$
= & \sum_{s=0}^\infty \sum_{r=0}^\infty B^s S(\eta_{k+N_0-s})(\eta_{k+l+N_0-r})^\top S^\top (B^\top)^r
$$ instead, and the matrix
$(\eta_{k+N_0-s})(\eta_{k+l+N_0-r})^\top$ is equal to (or rather, its
expected value is) the identity matrix when $r = s+l$, rather than
$r=s$, and zero otherwise. So we simply have $$
\mathbb{E}(C) = \mathbb{E}\left[(\mathbf{p}_{k+N_0})(\mathbf{p}_{k+l+N_0})^\top\right] = & \sum_{s=0}^\infty B^s S S^\top (B^\top)^{s+l}
$$ which happens to be the same as what we found for the lag
zero ($l=0$) case, end-multiplied by $(B^\top)^l$.

# Finding Eigenvectors

Recall that we have found

$$
D:=\mathbb{E}(C) = & \sum_{s=0}^\infty B^s S S^\top (B^\top)^s,
$$ and $$
D_{\text{lag }m} = & \sum_{s=0}^\infty B^s S S^\top (B^\top)^{s+m} = D(B^\top)^m
$$ where we have chosen a large enough $N_0$. It might be
useful to note that we can define $D$ intrinsically by $$
D = & SS^\top + B D B^\top.
$$ which we could solve component-wise, but it would be very
messy. In the fairly trivial 1-dimension case we clearly have
$$
d = \frac{s^2 }{1-b^2}
$$ If we stick to the $2\times 2$ case, and use the
restriction that $B$ is diagonal, then we get $$
D = \left[ 
\begin{array}{cc}
\frac{s_{12}^2+s_{11}^2}{1-b_{11}^2} & \frac{s_{12}s_{22}+s_{11}s_{21}}{1-b_{11}b_{22}}\\
\frac{s_{12}s_{22}+s_{11}s_{21}}{1-b_{11}b_{22}} & \frac{s_{22}^2+s_{21}^2}{1-b_{22}^2}
\end{array}
\right]

$$ which is pleasingly similar to the 1-D case. If $S$ is
diagonal but $B$ is not, then we have a lot more terms, but using a
*computer* we find that $$
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

## $B$ diagonal

If we take the $B$ diagonal case
(eqn.[\[B_diag\]](#B_diag)). In
general, the eigenvectors of symmetric matrix $\left(
\begin{array}{cc}
a&b\\
b&c
\end{array}
\right)$ are $\frac{1}{2}\left(a+c\pm\sqrt{(a-c)^2+4b^2}\right)$ and
since everything is positive the positive square root will give the
largest eigenvalue. Note that for $b=0$ the difference between the two
eigenvalues is $|a-c|$ but for non zero $b$ this difference increases --
the eigenvalues become more distinct. For matrix $D$ this corresponds to
the situation where $S$ is diagonal (or reverse-diagonal, or one of the
rows is zero).\
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
very small. In section [7.1.2](#extra_working)
 we expand the terms in the eigenvector
formula (eqn.
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
variance will be on the $b_{22}$ timeseries rather than the $b_{11}$
timeseries, it is simply a case of a very large noise obscuring the
signal (in this case the 'signal' is the impending tipping point as
$b_{11}$ approaches 1).

### summary of $B$ diagonal case

Where $B$ is diagonal we have the two systems $$
x_t &= b_{11}x_{t-1} + (s_{11},s_{12})\underline{\eta}_t\\
y_t &= b_{22}y_{t-1} + (s_{21},s_{22})\underline{\eta}_t
$$ The EOF method projects the $x$ and $y$ onto a vector such
that the variance is maximised. Usually this would be (close to) the $x$
direction if $b_{11}$ is close to 1, however it may not be if
$(s_{11},s_{12})$ are small and $(s_{21},s_{22})$ are large. In this
case $x$ is a slow curve towards zero and $y$ is white noise with a
large variance.\
We also discovered that the eigenvalues of $D$ become less distinct as
$S$ becomes 'more diagonal' - the non-diagonal elements become smaller.
That is, when there is less correlation in the noise terms, it becomes
more difficult to determine which is the principal eigenvalue (and
therefore which eigenvector to project onto).

### Some Extra working

We would like to expand the square root $$
\sqrt{\left(\frac{s_{12}^2+s_{11}^2}{1-b_{11}^2}-\frac{s_{22}^2+s_{21}^2}{1-b_{22}^2}\right)^2+4\left(\frac{s_{12}s_{22}+s_{11}s_{21}}{1-b_{11}b_{22}}\right)^2}.
$$ For clarity, say $\varepsilon:=1-b_{11}$,
$p := s_{11}^2+s_{12}^2$, $q := s_{21}^2+s_{22}^2$ and
$r := s_{12}s_{22}+s_{11}s_{21}$, then we have $$
& \sqrt{\left(\frac{p}{\varepsilon(1+b_{11})}-\frac{q}{1-b_{22}^2}\right)^2+4\left(\frac{r}{1-(1-\varepsilon) b_{22}}\right)^2}\\
=& \frac{1}{\varepsilon}\sqrt{\frac{p^2}{(1+b_{11})^2}-\varepsilon\frac{2pq}{(1+b_{11})(1-b_{22}^2)}-\varepsilon^2\frac{q^2}{(1-b_{22}^2)^2}+\varepsilon^2\frac{4r^2}{(1-(1-\varepsilon) b_{22})^2}}
$$ We need to express
$\varepsilon^2\frac{4r^2}{(1-(1-\varepsilon) b_{22})^2}$ in leading
order terms of $\varepsilon$:\
$$
\frac{1}{1-(1-\varepsilon) b_{22}} &= 1+(1-\varepsilon) b_{22}+(1-\varepsilon)^2 b_{22}^2+...\\
&=\frac{1}{1-b_{22}} -
\varepsilon\sum_{k=1}^\infty kb_{22}^k + \varepsilon^2\sum_{k=2}^\infty\left(\begin{array}{c}k\\2\end{array}\right)b_{22}^k + \mathcal{O}(\varepsilon^3)\\
\varepsilon^2\frac{4r^2}{(1-(1-\varepsilon) b_{22})^2} & = \varepsilon^2\frac{4r^2}{(1-b_{22})^2}+\mathcal{O}(\varepsilon^3) \text{   (as you'd expect)}
$$ Then we can return to our square root: $$
& \frac{1}{\varepsilon}\sqrt{\frac{p^2}{(1+b_{11})^2}-\varepsilon\frac{2pq}{(1+b_{11})(1-b_{22}^2)}+\varepsilon^2\left[ \frac{4r^2(1+ b_{22})^2 -  q^2 }{(1-b_{22}^2)^2} \right] + \mathcal{O}(\varepsilon^3)}\\
= & \frac{p}{\varepsilon (1+b_{11})} \sqrt{1+\varepsilon\frac{-2q(1+b_{11})}{p(1-b_{22}^2)}+\varepsilon^2(1+b_{11})^2\left[ \frac{4r^2(1+ b_{22})^2 -  q^2 }{p^2(1-b_{22}^2)^2} \right] + \mathcal{O}(\varepsilon^3)}\\
=& \frac{p}{\varepsilon (1+b_{11})}\left[1+
\varepsilon\frac{-q(1+b_{11})}{p(1-b_{22}^2)}+\varepsilon^2\frac{(1+b_{11})^2}{2}\left[ \frac{4r^2(1+ b_{22})^2 -  q^2 }{p^2(1-b_{22}^2)^2}\right] - 
\frac{1}{8}\left(\varepsilon\frac{-2q(1+b_{11})}{p(1-b_{22}^2)} \right)^2
+ \mathcal{O}(\varepsilon^3)
\right]\\
=& \frac{p}{\varepsilon (1+b_{11})}\left[1+
\varepsilon\frac{-q(1+b_{11})}{p(1-b_{22}^2)}+
\varepsilon^2 \left[ \frac{4r^2(1+ b_{22})^2(1+b_{11})^2 -  q^2(1+b_{11})^2 }{2p^2(1-b_{22}^2)^2}\right] - 
\varepsilon^2\left[\frac{q^2(1+b_{11})^2}{2p^2(1-b_{22}^2)^2}\right]
+ \mathcal{O}(\varepsilon^3)
\right]\\
=& \frac{p}{\varepsilon (1+b_{11})}\left[1+
\varepsilon\frac{-q(1+b_{11})}{p(1-b_{22}^2)}+
\varepsilon^2(1+b_{11})^2 \left[ \frac{4r^2(1+ b_{22})^2 -  2q^2 }{2p^2(1-b_{22}^2)^2}\right]
+ \mathcal{O}(\varepsilon^3)
\right]\\
=&
\frac{p}{\varepsilon (1+b_{11})} + 
\frac{-q}{(1-b_{22}^2)}+
\varepsilon(1+b_{11}) \left[ \frac{2r^2(1+ b_{22})^2 -  q^2 }{p(1-b_{22}^2)^2}\right]
+ \mathcal{O}(\varepsilon^2)\\
=&
\frac{p}{(1-b_{11}^2)} + 
\frac{-q}{(1-b_{22}^2)}+
(1-b_{11}^2) \left[ \frac{2r^2(1+ b_{22})^2 -  q^2 }{p(1-b_{22}^2)^2}\right]
+ \mathcal{O}((1-b_{11})^2)
$$ Returning to our eigenvector, we can now replace the
square root term in the first component with its expansion to find
$$
& \frac{2p}{(1-b_{11}^2)} + 
\frac{-2q}{(1-b_{22}^2)}+
(1-b_{11}^2) \left[ \frac{2r^2(1+ b_{22})^2 -  q^2 }{p(1-b_{22}^2)^2}\right]
+ \mathcal{O}((1-b_{11})^2)\\
\text{Or, }& \frac{2p}{(1-b_{11}^2)} + 
\frac{-2q}{(1-b_{22}^2)}
+ \mathcal{O}((1-b_{11}))\\
$$ where we also know that the second vector component is
$$
\frac{2r}{1-b_{11}b_{22}} & = 2r\left[\frac{1}{1-b_{22}} -
\varepsilon\sum_{k=1}^\infty kb_{22}^k + \varepsilon^2\sum_{k=2}^\infty\left(\begin{array}{c}k\\2\end{array}\right)b_{22}^k + \mathcal{O}(\varepsilon^3)
\right]\\
& = 2r\left[\frac{1}{1-b_{22}} -
\varepsilon\frac{b_{22}}{(1-b_{22})^2}
\right]
+ \mathcal{O}(\varepsilon^2)\\
& = \frac{2r(1 - 2b_{22} + b_{11}b_{22})}{(1-b_{22})^2}
+ \mathcal{O}((1-b_{11})^2)\\
\text{Or,  }& \frac{2r}{1-b_{22}}+ \mathcal{O}((1-b_{11}))
$$

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

$$
d_{11}=
-\frac{1}{k}\left[
(b_{11}b_{12}^2b_{22}-b_{12}^3b_{21}+b_{12}^2)s_{22}^2+
(-2b_{11}b_{12}b_{22}^2+2b_{12}^2b_{21}b_{22}+2b_{11}b_{12})s_{12}s_{22}+
(b_{11}b_{12}^2b_{22}-b_{12}^3b_{21}+b_{12}^2)s_{21}^2+
(-2b_{11}b_{12}b_{22}^2+2b_{12}^2b_{21}b_{22}+2b_{11}b_{12})s_{11}s_{21}+
(b_{11}b_{22}^3+(-b_{12}b_{21}-1)b_{22}^2-b_{11}b_{22}-b_{12}b_{21}+1)s_{12}^2+
(b_{11}b_{22}^3+(-b_{12}b_{21}-1)b_{22}^2-b_{11}b_{22}-b_{12}b_{21}+1)s_{11}^2
\right]
$$

$$
d_{12}=
\frac{1}{k}\left[
((b_{11}^2-1)b_{12}b_{22}-b_{11}b_{12}^2b_{21})s_{22}^2+
((1-b_{11}^2)b_{22}^2+b_{12}^2b_{21}^2+b_{11}^2-1)s_{12}s_{22}+
((b_{11}^2-1)b_{12}b_{22}-b_{11}b_{12}^2b_{21})s_{21}^2+
((1-b_{11}^2)b_{22}^2+b_{12}^2b_{21}^2+b_{11}^2-1)s_{11}s_{21}+
(b_{11}b_{21}b_{22}^2-b_{12}b_{21}^2b_{22}-b_{11}b_{21})s_{12}^2+
(b_{11}b_{21}b_{22}^2-b_{12}b_{21}^2b_{22}-b_{11}b_{21})s_{11}^2
\right]
$$

$$
d_{21}=
\frac{1}{k}\left[
((b_{11}^2-1)b_{12}b_{22}-b_{11}b_{12}^2b_{21})s_{22}^2+
((1-b_{11}^2)b_{22}^2+b_{12}^2b_{21}^2+b_{11}^2-1)s_{12}s_{22}+
((b_{11}^2-1)b_{12}b_{22}-b_{11}b_{12}^2b_{21})s_{21}^2+
((1-b_{11}^2)b_{22}^2+b_{12}^2b_{21}^2+b_{11}^2-1)s_{11}s_{21}+
(b_{11}b_{21}b_{22}^2-b_{12}b_{21}^2b_{22}-b_{11}b_{21})s_{12}^2+
(b_{11}b_{21}b_{22}^2-b_{12}b_{21}^2b_{22}-b_{11}b_{21})s_{11}^2
\right]
$$

$$
d22=
-\frac{1}{k}\left[
((b_{11}^3-b_{11})b_{22}+(-b_{11}^2-1)b_{12}b_{21}-b_{11}^2+1)s_{22}^2+
((2-2b_{11}^2)b_{21}b_{22}+2b_{11}b_{12}b_{21}^2)s_{12}s_{22}+
((b_{11}^3-b_{11})b_{22}+(-b_{11}^2-1)b_{12}b_{21}-b_{11}^2+1)s_{21}^2+
((2-2b_{11}^2)b_{21}b_{22}+2b_{11}b_{12}b_{21}^2)s_{11}s_{21}+
(b_{11}b_{21}^2b_{22}-b_{12}b_{21}^3+b_{21}^2)s_{12}^2+
(b_{11}b_{21}^2b_{22}-b_{12}b_{21}^3+b_{21}^2)s_{11}^2
\right]
$$

This little factoid might be handy: $$
\sum_{k=1}^n kz^k = z\frac{1-(n+1)z^n+nz^{n+1}}{(1-z)^2}
$$ or it might not.
