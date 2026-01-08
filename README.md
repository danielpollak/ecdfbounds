# ecdfbounds

Confidence bounds for empirical CDFs using
- Dvoretzky–Kiefer–Wolfowitz (DKW) inequality
- Bootstrap resampling

## Installation
`pip install git+https://github.com/danielpollak/ecdfbounds.git`

## Example

```python
import numpy as np
import matplotlib.pyplot as plt

from ecdfbounds import (
    ecdf,
    dkw_confidence_band,
    bootstrap_ecdf_band,
    plot_ecdf_with_band,
)

# Reproducibility
rng = np.random.default_rng(0)

# Dummy data: non-uniform on purpose

# Hypothesis confirmed
# data = rng.random(size=200)

# Hypothesis rejected
data = rng.beta(2, 5, size=200)

# --- ECDF ---
x, Fn = ecdf(data)

# --- DKW band ---
lower_dkw, upper_dkw = dkw_confidence_band(Fn, alpha=0.05)

# --- Bootstrap band ---
x_boot, lower_boot, upper_boot = bootstrap_ecdf_band(
    data, n_boot=1000, alpha=0.05
)

# --- Plot ---
fig, ax = plt.subplots(figsize=(6, 4))

# ECDF + DKW band
plot_ecdf_with_band(
    x, Fn, lower_dkw, upper_dkw, ax=ax, label="ECDF (DKW)"
)

# Overlay bootstrap band
ax.fill_between(
    x_boot, lower_boot, upper_boot,
    step="post", alpha=0.25, label="Bootstrap 95% band"
)

# Theoretical uniform CDF for reference
ax.plot(x, x, "k--", label="Uniform CDF")

ax.legend()
ax.set_title("ECDF with DKW and Bootstrap Confidence Bands of\nbeta distributionagainst Uniform CDF null hypothesis")
plt.show()
```
<img width="536" height="414" alt="ecdfbounds_beta" src="https://github.com/user-attachments/assets/42438e4b-f06f-4b73-a12a-0dbd038da133" />
