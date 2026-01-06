# Problem set by Tobias about PCA method

Say we have a dynamical system ${\mathbf x}_n$ described by
${\mathbf x}_{n+1} = B{\mathbf x}_n + S{\mathbf \eta}_n$ where $B, S$
are symmetric and the ${\mathbf \eta}_n$ are column vectors with each
element $\sim N(0,1)$, iid.\
If ${\mathbf x}$ is 1-dimension, then the system is an AR(1) model. If
${\mathbf x}$ is many dimensions we might want to only study only the
first EOF score as in (held2004), in the hope that it "captures" most
of the interesting behaviour of the system.\
The question posed: How useful or relevant is the first EOF score?

## First observations

- The series can be simplified: $$
  {\mathbf x}_n &= B^n{\mathbf x}_0 + B^{n-1}S{\mathbf \eta}_1 + B^{n-2}S{\mathbf \eta}_2 + ... + B^{1}S{\mathbf \eta}_{n-1} + S{\mathbf \eta}_n\\
  &= B^n{\mathbf x}_0 + \sum_{i=1}^{n} B^{n-i}S{\mathbf \eta}_i 
  $$

## PCA (or EOF) method

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

## Later observations

- : $$
  {\mathbf y}_n &= {\mathbf x}_n - \frac{1}{N}\sum_{j = 1}^N {\mathbf x}_j\\
  &= B^n{\mathbf x}_0 + \sum_{i=1}^{n} B^{n-i}S{\mathbf \eta}_i - \frac{1}{N}\sum_{j = 1}^N \left(B^j{\mathbf x}_0 + \sum_{k=1}^{j} B^{j-k}S{\mathbf \eta}_k \right)\\
  &= \left[ B^n - \frac{1}{N}\sum_{j = 1}^N B^j\right]{\mathbf x}_0 + \left[ \sum_{i=1}^{n} B^{n-i}S{\mathbf \eta}_i  - \frac{1}{N}\sum_{j = 1}^N\sum_{k=1}^{j} B^{j-k}S{\mathbf \eta}_k \right]
  $$
