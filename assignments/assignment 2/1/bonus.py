import numpy as np
import matplotlib.pyplot as plt

g = 9.81
length = 1
theta0 = np.pi / 6
t = np.linspace(0, 10, 500)
omega = np.sqrt(g / length)

theta = theta0 * np.cos(omega * t)

plt.plot(t, theta)
plt.title("Simple Pendulum")
plt.xlabel("Time (s)")
plt.ylabel("Angle (rad)")
plt.show()
