# Generalized Auto Correlation

Notes from (williamson2015).\
Familiarly a dynamical system is described by $$
\dot{x} = f(x) + \varepsilon
$$ and can be linearised in $x$ and euler-discretised in
time by $$
x_{t+1} = ax_t + c + \varepsilon_t
$$ where $$
a &= 1+ J(x^*)\Delta t\\
c &= -x^*J(x^*)\Delta t.
$$ In the multivariate case where we have a vector
$\mathbf{x}$, we find that $$
\dot{\mathbf{x}} = f(\mathbf{x}) + \varepsilon
$$ becomes $$
\mathbf{x}_{t+1} = A\mathbf{x}_t + \mathbf{c} + \mathbf{\varepsilon}_t
$$ where $$
A &= \mathbf{I}+ J(\mathbf{x}^*)\Delta t\\
\mathbf{c} &= \left[ f(\mathbf{x}^*) - \mathbf{x}^*J(\mathbf{x}^*)\right]\Delta t.
$$

It is hoped that from a (multivariate) time series we can reconstruct
the matrix $A$. Note that in the 1D case we estimate $a$ using
$$
a = \frac{E(x_{t+1}x_t)-\mu^2}{E(x_{t}^2)-\mu^2}
$$ or $a = b\sigma^{-1}$ where $$
b &= E(x_{t+1}x_t)-\mu^2\\
\sigma &= E(x_{t}^2)-\mu^2.
$$ In the multivariate case we do exactly the same:
$A = B\Sigma^{-1}$ where $$
B &= E(\mathbf{x}_{t+1}\mathbf{x}_t)-\mu\mu^T\\
\Sigma &= E(\mathbf{x}_{t}^2)-\mu\mu^T.
$$

# Implementing

Attempt to replicate results from (williamson2015). We have used
`ode45` to integrate the system $$
\dot{x} &= y + \varepsilon^{(x)}\\
\dot{y} &= \mu - x^2 + \varepsilon^{(y)}\\
\mu &= 0.5-0.005t
$$ Where $\mu$ varies from $1/2$ at $t=0$ to zero at $t=100$
and $\varepsilon$ is white noise with standard deviation
$\sigma = 0.01$. The solution should circle about the moving centre at
$(\sqrt{\mu},0)$ (given an initial condition $\mathbf{x}_0$ sufficiently
close) until it escapes the orbit. At $t=100$ the centre
$(\sqrt{\mu},0)$ and the saddle point $(-\sqrt{\mu},0)$ collide.\
In (williamson2015) this system is integrated to give the solution
shown in Figure [1](#williamsonorbit)
. Using `ode45` we get the solution shown in
Figure [2](#ourownonorbit)
. Which looks fairly similar although there
appears to be more noise in Figure
[1](#williamsonorbit),
possibly just a difference in plotting.

![Reproduced from (williamson2015). The ODE system integrated with
varying $\mu$.](../images/williamsonorbit.png){#williamsonorbit
width="5in"}

![Our own attempt to replicate the results in Figure
[1](#williamsonorbit)
.](../images/ourownorbit.png){#ourownonorbit
width="5in"}

Next we attempt to replicate the results in Figure
[3](#williamsoneigenvals)
. These are the real and imaginary parts
of the Jacobian's eigenvalues in a sliding window of length 50.
Supposedly the eigenvalues of the Jacobian, the $\lambda_j$'s, are
calculated from the $\tilde{a}_j$'s, the eigenvalues of the matrix
$A = B\Sigma^{-1}$ described above, using the formulae: $$
\Re(\lambda_j) &= \frac{1}{\Delta t}\log |a_j|\\
\Im(\lambda_j) &= \frac{1}{\Delta t}\phi_j
$$ where the (possibly) complex $\tilde{a}_j$'s are
decomposed as $\tilde{a}_j= |a_j| e^{i\phi_j}$. Our code calculates the
matrix $A$ in a 50-point sliding window. Figures
[4](#ourowneigenvals_R)
 and
[5](#ourowneigenvals_I)
 show the magnitude and the angle (resp.)
of the eigenvalues $\tilde{a}$. As can be seen, our results don't look
anything like those in (williamson2015).

![Reproduced from (williamson2015).
](../images/williamsoneigenvals.png){#williamsoneigenvals width="5in"}

![](../images/ourowneigenvals_R.png){#ourowneigenvals_R width="5in"}

![](../images/ourowneigenvals_I.png){#ourowneigenvals_I width="5in"}
