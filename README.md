# ecdfbounds

Confidence bounds for empirical CDFs using
- Dvoretzky–Kiefer–Wolfowitz (DKW) inequality
- Bootstrap resampling

## Installation
`pip install git+https://github.com/danielpollak/ecdfbounds.git`

## Example

```python
import numpy as np
from ecdfbounds import ecdf, dkw_confidence_band, plot_ecdf_with_band

data = np.random.rand(100)

x, Fn = ecdf(data)
lower, upper = dkw_confidence_band(Fn)

plot_ecdf_with_band(x, Fn, lower, upper)