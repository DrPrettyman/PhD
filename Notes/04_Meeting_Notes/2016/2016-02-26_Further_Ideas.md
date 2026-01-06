# Testing on real data, further ideas

[\[ashwin2012\]](#ashwin2012)


Valerie sends the paper (gao2016) with the note:\

------------------------------------------------------------------------

A very interesting paper just published by the Barabasi group: They
investigate networks and 1D resilience function of a multi-dimensional
complex system, which is similar to what we are doing when use
approximate 1D stochastic equations for studying tipping points.\
I think we could attempt to derive the 1D resilience function for
gridded 2D data on the hurricane track using the eigenvalues to identify
network dependencies. Then this function could be studied for tipping.
It is an alternative idea for multivariate tipping.\
Joshua, can you try this?

------------------------------------------------------------------------

Therefore I will thy this!

## Goa, Barabasi, et al. method: G-method

Model the $N$-dimensional dynamical system using equation:

$$
\frac{dx_i}{dt} = F(x_i) + \sum_{j=1}^{N} A_{ij}G(x_i,x_j)

$$

Of course we have to work out what $F$, $G$, and - importantly - $A$
should be.\
If we have an (approximately) linear system that we're just going to
write as

$$
\dot{\mathbf{x}} = A\mathbf{x} + \mathbf{c}
$$

we could always rewrite this as in Eqn. [\[G\]](#G)
 where $G(x_i,x_j) = x_j$ and $F(x_i) = c_i$.\
The method then calls to reduce the system to one dimension in a new
"effective" variable
$x_\text{eff} = \langle s^{\text{out}}x\rangle / \langle s\rangle$.
Which means the whole system becomes

$$
\dot{x_\text{eff}} = F(x_\text{eff}) + \beta G(x_\text{eff},x_\text{eff})
$$ where
$\beta = \langle s^\text{out} s^\text{in}\rangle / \langle s \rangle$.
But how to evaluate $F(x_\text{eff})$ and $G(x_\text{eff},x_\text{eff})$
when $F$ and $G$ may be node-dependent? (gao2016) gets around this by
assuming, in the supplementary information, that these are
node-independent, although in the paper they write a general form
$F_i(x_i)$. It may be possible to salvage some of the method anyway. In
any case the method relies mainly on an analysis of $\beta$ which is
calculated using only the matrix $A$, which we can estimate in the
linear case. Note that the diagonal of $A$ is arbitrary since it can be
absorbed into the $F(x)$ term. It is therefore hard to see how the
method can be useful if it relies on an analysis of $A$ or $\beta$ and
not $F$.

# comparisons

## Williamson method: W-method

Model the $N$-dimensional dynamical system using equation:

$$
\frac{dx_i}{dt} = f(x_1,...,x_N)+\varepsilon_i
$$

Then "linearise" the system, writing it as

$$
\mathbf{x}_{t+1} = A\mathbf{x}_t + \mathbf{c} + \mathbf{\varepsilon}_{t+1}
$$ where $A$ is estimated as $A=B\Sigma^{-1}$ where
$$
 B &= \frac{1}{T-1} \sum_{t=1}^{T-1} \mathbf{x}_{t+1}\mathbf{x}_t^T - \mu\mu^T \\
  \Sigma &= \frac{1}{T} \sum_{t=1}^{T} \mathbf{x}_{t}\mathbf{x}_t^T - \mu\mu^T \\
  \mu &= \frac{1}{T} \sum_{t=1}^T \mathbf{x}_t
 
$$

We then look at the first eigenvalue of $A$ in the hope that this will
tell us something useful.

## PCA method
