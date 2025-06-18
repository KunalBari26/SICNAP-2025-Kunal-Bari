import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("sample_data.csv")

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
scatter = ax.scatter(data["StudyHours"], data["ExamScore"], data["SleepHours"],c=data['Attendance'],cmap='viridis')

cbar = fig.colorbar(scatter, ax=ax, pad=0.1)
cbar.set_label('Color Value')
ax.set_xlabel("StudyHours")
ax.set_ylabel("ExamScore")
ax.set_zlabel("SleepHours")
plt.title("3D plot")
plt.show()
