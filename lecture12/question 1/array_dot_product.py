import numpy as np
import matplotlib.pyplot as plt

v = np.array([2., 2., 4.])
fig = plt.figure()
ax = plt.axes(projection="3d")
e0 = v[0]
e1 = v[1]
e2 = v[2]
ax.scatter3D(e0, e1, e2, c="r", cmap='hsv')
plt.show()
