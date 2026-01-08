import numpy as np


def dkw_band(n, alpha=0.05):
    """
    DKW epsilon for a (1 - alpha) confidence band.
    """
    return np.sqrt(np.log(2 / alpha) / (2 * n))


def dkw_confidence_band(Fn, alpha=0.05):
    """
    Compute lower and upper DKW confidence bands.

    Parameters
    ----------
    Fn : ndarray
        Empirical CDF values
    alpha : float

    Returns
    -------
    lower, upper : ndarray
    """
    n = len(Fn)
    eps = dkw_band(n, alpha)
    lower = np.maximum(Fn - eps, 0.0)
    upper = np.minimum(Fn + eps, 1.0)
    return lower, upper