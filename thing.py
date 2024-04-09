# %%
import numpy as np

x, y, z = np.ogrid[-10: 10: 100j, -10: 10: 100j, -10: 10: 100j]
print((x**2 + y**2 + z**2 - x * y * z)[0][0])

# %%
