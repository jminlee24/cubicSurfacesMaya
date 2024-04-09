import numpy as np
from mayavi import mlab

t = np.linspace(0, 4 * np.pi, 20)

print(t)
x = [1]
y = [0]
z = [0]
s = 2 + np.sin(t)

mlab.points3d(x, y, z, colormap="copper", scale_factor=.25)

mlab.axes()
mlab.show()
