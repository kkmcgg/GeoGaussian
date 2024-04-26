# create 100 rnadom 3d points as a numpy array
import numpy as np
points = np.random.rand(100, 3)
# print(points)

#display points to the screen
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(points[:,0], points[:,1], points[:,2])
plt.show()

