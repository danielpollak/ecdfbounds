import numpy as np


def ecdf(x):
    """
    Compute the empirical CDF.

    Returns
    -------
    x_sorted : ndarray
    Fn : ndarray
    """
    x = np.asarray(x)
    x_sorted = np.sort(x)
    n = len(x_sorted)
    Fn = np.arange(1, n + 1) / n
    return x_sorted, Fn