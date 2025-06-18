import numpy as np
import matplotlib.pyplot as plt

velocity = 20 
angle_deg = 45
g = 9.81  
angle_rad = np.radians(angle_deg)
velocityx = velocity * np.cos(angle_rad)
velocityy = velocity * np.sin(angle_rad)

x_vals = []
y_vals = []

t = 0
step = 0.01

while True:
    x = velocityx * t
    y = velocityy * t - 0.5 * g * t**2

    if y < 0:
        print(f"The projectile hit the ground at distance {x} after time {t}")
        break  

    x_vals.append(x)
    y_vals.append(y)
    t += step
plt.plot(x_vals, y_vals)
plt.title("Projectile Motion")
plt.xlabel("Horizontal Distance (m)")
plt.ylabel("Vertical Distance (m)")
plt.show()
