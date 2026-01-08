import numpy as np


def bootstrap_ecdf_band(data, n_boot=1000, alpha=0.05):
    """
    Bootstrap confidence band for the ECDF (pointwise).

    Returns
    -------
    x : ndarray
    lower : ndarray
    upper : ndarray
    """
    data = np.asarray(data)
    n = len(data)
    x = np.sort(data)

    ecdfs = np.empty((n_boot, n))

    for i in range(n_boot):
        sample = np.random.choice(data, size=n, replace=True)
        sample.sort()
        ecdfs[i] = np.searchsorted(sample, x, side="right") / n

    lower = np.percentile(ecdfs, 100 * alpha / 2, axis=0)
    upper = np.percentile(ecdfs, 100 * (1 - alpha / 2), axis=0)

    return x, lower, upper