import numpy as np
import matplotlib.pyplot as plt

# iteration time step
dt = 0.0001

# set values
B = np.array([0, 0, 2])
E = np.array([0, 0.1, 0])
pos = [np.array([0, 0, 0])]
v = [np.array([1, 1, 1])]
e = 1
m = 1
start, stop = 0, 10

# create time stamps
t = np.arange(start, stop, dt)

# Compute movement using euler method
for i in t:
    a = ((np.cross(v[-1], B)) + E)*e/m
    pos.append(pos[-1] + v[-1]*dt)
    v.append(v[-1] + a*dt)

# Prepare lists of positions for chart
x, y, z = [], [], []
for i in pos:
    x.append(i[0])
    y.append(i[1])
    z.append(i[2])

# Create chart
ax = plt.axes(projection='3d')
ax.plot(x, y, z)

# Set labels
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

# show chart
plt.show()