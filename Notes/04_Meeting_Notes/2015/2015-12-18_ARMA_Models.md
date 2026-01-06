# Idea

ARMA models allow us to approximate an intrinsically stochastic system
(e.g. $x_{n} = \theta x_{n-1} + \eta_n$) as a deterministic system $y$,
plus some noise ($x_n = y_n + \eta_n$).\
No, I don't think that's correct. I was thinking about being able to
represent a general ARMA process as an infinite AR or MA process.

# Meeting with Valerie, 17/12/15

We discussed looking at different ARMA models:

- Non-linear ARMA (NARMA)

- Seasonal ARMA (SARMA)

- ARMAX: $$
  x_n = \eta_n + \sum_{i=1}^p \theta_i x_{n-i} + \sum_{i=1}^q \phi_i \eta_{n-i} + \sum_{i=0}^b \psi_i d_{n-i}
  $$ where $\{d_i\}$ is an external time series.

We also discussed the possibility to look at multidimensional models
which could be complicated, and using numerical methods to extrapolate
dynamics.\
Valerie suggests using Kalman filter to get parameters of FARIMA model
from the timeseries data[^1].\
Keep in mind that we are trying to find a method to determine the
*proximity* of a tipping point.\
Get Tobias to give some input. In particular looking at dynamical
systems - use different models and different methods. Try to classify
different dynamical systems wrt. whether one can predict a tipping
point.\
Valerie once cycled 600km in 40hours and slept for 1hour in a bush.

## Valerie recommends - reading list

- *Climate Time Series Analysis* (mudelsee2012) might be a useful book.
  Can't find in the library though, will have to order.

- *Nonlinear dynamics and chaos* (strogatz2014) Also may be a useful
  book as an introduction to some non-linear systems. Available from ICL
  Library.

- *Cenozoic climate changes: A review* (mudelsee2014) Is a good review
  paper.

- *False alarms: How early warning signals falsely predict abrupt sea
  ice loss* (wagner2015) is a good review of EWS and applications to
  sea-ice.

- *Foundations of Complex Systems* (nicolis2007) is a book about
  "Nonlinear Dynamics, Statistical Physics, Information and Predicition"
  which Valerie has leant to me.

- Papers (not specified) by Dakos, who looks at EWS in ecological
  models.

- Paper (not specified) by Taqqu on Estimators.

- Papers (not specified) by Ditlevsen, building simple models with
  bifurcations, connected to the paleoclimate records.

[^1]: Learn what a Kalman filter is
