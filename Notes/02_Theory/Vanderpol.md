# Hopf-bifurcation

As per Williamson and Lenton, we use the system $$
\dot{r} &=& \mu r  - r^3+ \eta_r\\
\dot{\theta} &=& 1 + r^2 + \eta_\theta.
$$ where $\mu$ varies linearly from $\mu=-2.8$ at $t=0$ to
$\mu=0.2$ at $t=60$ and $\eta$ are white noise processes with standard
deviation 0.01.

We have decided to integrate the system with a time step of
$\Delta_t = 0.01$ then sample every 50 to get a time series with time
step 0.5. A bifurcation occurs at $t=58$.

The method of finding the Jacobian matrix's eigenvalues is performed,
the result of 100 trials are presented in figure
[1](#hopf100). Encouragingly,
it looks a lot like the one in the W& L paper.

# Homoclinic-bifurcation

This looks nothing like in the paper.


![](../images/Hopf100_evals.png)
 100 trials
of the hopf bifurcation example are all analysed using the eigenvalue
method. The mean of first eigenvalues is shown here, the dashed lines
show 1 standard deviation from the mean.


# Van der Pol oscillator

We use the Van der Pol oscillator: $$
\ddot{x} - \epsilon(1-x^2)\dot{x}+x = F\cos\left(2\pi t / T\right)
$$ which we conveniently rewrite as a system of first
order ODEs: $$
\dot{x} &=& \epsilon\left(x - \frac{1}{3}x^3\right) +y\\
\dot{y} &=& -x + F\cos\left(2\pi t / T\right).
$$ We integrate the system from $t=0$ to $t=6000$, where
the value of $\epsilon$ is made to vary linearly over that time
increasing from $\epsilon = 5$ to $\epsilon = 11$. Figure
[2](#xyseries) shows the
outcome. Figure [3](#eigenvals)
 shows the Jacobian eigenvalue according to the
Williamson and Lenton Method. It doesn't seem to provide any sort of
indicator, but at least there seems to be some correlation in that the
imaginary part goes crazy when the oscillator is chaotic and is flat
when the oscillator is periodic.

![[] Showing the integrated VDP system in
$x$ (top) and $y$ (bottom).](../images/VDP_xyseries.png){#xyseries


![[] Showing the first eigenvalue of the
Jacobian (according to Williamson and Lenton method). Real part (top)
and imaginary part (bottom).](../images/VDP_evals.png){#eigenvals

