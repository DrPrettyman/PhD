# Kwasniok 2009

Let's have a read of (kwasniok2009), to see if there is anything
useful.\
First of all:

- "We follow a complementary approach in deriving a dynamical model
  purely from the data. The method is based on unscented Kalman
  filtering, a nonlinear extension of conventional Kalman filtering.
  This technique allows to consistently estimate parameters in
  deterministic and stochastic nonlinear models."

So it seems that we are looking at something useful indeed. The
difference is the application but maybe we can work it out.

## testing for non-linearity

The method used here is designed for estimating parameters in a
*non-linear* system, Kwasniok therefore tests the data for non-linearity
before proceeding. The test he uses ("the method of surrogate time
series") is outsourced to \[T. Schreiber and A. Schmitz, Phys. Rev.
Lett. 77, 635 ͑199͒6.\] but it is noted that

- "The generated surrogate time series have both the same power spectrum
  and the same probability distribution as the original data. This
  technique yields a stronger test for genuine nonlinear structure ͑and
  not just non-Gaussianity͒ than earlier methods which suffer from higher
  rates of spurious detection of nonlinearity."

## The dynamical model

Kwasniok is using a (familiar) model:

$$
\dot{z} = -\frac{dU}{dz} + \sigma\eta
$$

where

$$
U(z) = a_4 z^4 + a_3 z^3 + a_2 z^2 + a_1 z
$$

and $\eta$ is a Gaussian white-noise process.

## The Unscented Kalman Filter 

We have a dynamical equation and an observation equation:

$$
\mathbf{z}_{t} &= f(\mathbf{z}_{t-1}, \mathbf{\lambda}) + \mathbf{\eta}_t\\
\mathbf{y}_{t} & = g(\mathbf{z}_t) + \mathbf{\varepsilon}
$$

The Kalman Filter wants to estimate the $z$'s given the $y$'s.\
We use an augmented state vector $\mathbf{x}$ because $\mathbf{z}$ isn't
good enough. This is just $\mathbf{z}$ and also $\lambda$, but
$\lambda_t = \lambda_{t-1}$ so there isn't anything new going on. In the
example it means that we are now estimating the position of $\mathbf{x}$
in the 5-dimensional state space with coordinates
$(z_t, a_4, a_3, a_2, a_1)$ at time $t$.\
For details of the Kalman filter, we are referred to four sources:

- S. Julier, J. Uhlmann, and H. F. Durrant-Whyte, IEEE Trans. Autom.
  Control 45, 477 ͑2000͒.

- S. J. Julier and J. K. Uhlmann, Proc. IEEE 92, 401 ͑2004͒.

- A. Sitz, U. Schwarz, J. Kurths, and H. U. Voss, Phys. Rev. E 66,
  016210 ͑2002͒.

- H. U. Voss, J. Timmer, and J. Kurths, Int. J. Bifurcation Chaos Appl.
  Sci. Eng. 14, 1905 ͑2004͒.

It's all pretty confusing as eqns. (9) to (18) in the paper explain
what's going on, but out of the process we get an estimation for
$(z_t, a_4, a_3, a_2, a_1)$ at time $t$.
