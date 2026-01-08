import matplotlib.pyplot as plt

from .ecdf import ecdf


def plot_ecdf_with_band(x, Fn, lower, upper, ax=None, label="ECDF"):
    """
    Plot ECDF with confidence band.
    """
    if ax is None:
        fig, ax = plt.subplots()

    ax.step(x, Fn, where="post", label=label)
    ax.fill_between(x, lower, upper, step="post", alpha=0.3)

    ax.set_xlabel("x")
    ax.set_ylabel("ECDF")
    return ax