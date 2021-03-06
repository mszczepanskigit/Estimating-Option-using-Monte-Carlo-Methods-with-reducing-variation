from imports import *


def cmc_european(s0, k, r, s, R):
    """
    Crude Monte Carlo estimator of european option with discounted payoff at time 1.
    :param s0: S(0) - fixed
    :param k: K - fixed
    :param r: r - fixed
    :param s: sigma - fixed
    :param R: total number of replications
    :return: estimated value
    """
    seed = 465726236011 % (2 ** 32 - 1)  # 6C 6F 72 65 6B
    np.random.seed(seed)
    z = np.random.normal(0, 1, R)
    mu = r - s ** 2 / 2
    return exp(-r)*(np.mean(np.maximum(s0 * np.exp(mu + s * z) - k, 0)))
