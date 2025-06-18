import numpy as np
import matplotlib.pyplot as plt

k = 10  
masses = [1, 2, 5] 
t = np.linspace(0, 10, 100)  

for m in masses:
    vel = np.sqrt(k / m)
    x = np.cos(vel * t)  
    plt.plot(t, x, label=f"Mass = {m} kg")

plt.title("Simple Harmonic Motion")
plt.xlabel("Time (s)")
plt.ylabel("Displacement (m)")
plt.legend()
plt.show()
