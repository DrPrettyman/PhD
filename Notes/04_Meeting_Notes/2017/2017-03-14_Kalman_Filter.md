# Unscented Kalman Filter

We are looking towards the paper *Deriving dynamical models from
paleoclimatic records* (kwasniok2009).\
It is said that "Estimation of states and parameters in chaotic systems
using only noisy and incomplete observations is a difficult task"
(sitz2002). Well obviously\...\

## The system

We have the dynamical equation that governs the system: $$
z_t = f(z_{t-1},\lambda)+\eta
$$ where $f$ is non-linear, $\eta$ is Gaussian with
covariance $Q$. And we have the observation equation: $$
y_t = g(z_{t},\lambda)+\varepsilon
$$ where $\varepsilon$ is gaussian and has covariance $R$. We
can consider both $z$ and $\lambda$ as being variables of a system,
where $\lambda_t = \lambda_{t-1}$. Thus we have a system in
$n = n_s+n_p$ dimensions, where $n_s$ is the dimension of $z$ and $n_p$
is the dimension on $\lambda$.\

## The UKF algorithm

Assume at each step we have an estimate of the system at the previous
step given knowledge of the observations up to the previous step
($\hat{x}_{t-1|t-1}$) and its covariance matrix $P_{t-1|t-1}^{xx}$. We
choose several test points (sigma points) labelled $\{x_{t-1|t-1}^i\}$.
The first $n_s$ elements of each sigma point make the vector
$z_{t-1|t-1}^i$ and the following $n_p$ elements make the vector
$\lambda_{t-1|t-1}^i$.\
We now apply the system and observation equations (prediction step):
$$
z_{t|t-1}^i &= f(z_{t-1|t-1}^i,\lambda_{t-1|t-1}^i) & \forall i\\
\lambda_{t|t-1}^i &= \lambda_{t-1|t-1}^i &\forall i\\
y_{t|t-1}^i &= g(z_{t|t-1}^i) & \forall i
$$ and take the mean of the sigma points: $$
\hat{z}_{t|t-1} &= \sum_i W_iz_{t|t-1}^i\\
\hat{\lambda}_{t|t-1} &= \sum_iW_i\lambda_{t|t-1}^i\\
\hat{y}_{t|t-1} &= \text{mean}_i(y_{t|t-1}^i)
$$ Where $W_i$ are weights but in Kwasniok
$W_i = 1/\#(\text{sigma points})$ for all $i$, so it is just taking the
mean.
