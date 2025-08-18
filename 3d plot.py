import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = [1, 2, 3, 4]
y = [5, 6, 7, 8]
z = [9, 10, 11, 12]
ax.scatter(x, y, z)
plt.title('3D Scatter Plot Example')
plt.show()
