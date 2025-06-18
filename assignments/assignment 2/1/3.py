import numpy as np
import matplotlib.pyplot as plt

radius = 100  
ang_velocity = 0.1 
angle = 0
orbit = []

while angle <= 2 * np.pi:
    x = radius * np.cos(angle)
    y = radius * np.sin(angle)
    orbit.append((x, y))
    angle += 0.01 

orbit = np.array(orbit)
x_vals = []
y_vals = []

for point in orbit:
    x_vals.append(point[0])
    y_vals.append(point[1])
plt.plot(x_vals, y_vals)

plt.title("Planetary Motion")
plt.show()
