import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("sample_data.csv")
required_columns = ['StudyHours', 'ExamScore', 'Attendance']
for col in required_columns:
    if col not in data.columns:
        raise ValueError(f"Missing column: {col}")
fig, axs = plt.subplots(1, 3)
axs[0].scatter(data['StudyHours'], data['ExamScore'])
axs[0].set_title('StudyHours vs StudyHours')
axs[0].set_xlabel('StudyHours')
axs[0].set_ylabel('ExamScore')


axs[1].scatter(data['ExamScore'], data['Attendance'])
axs[1].set_title('ExamScore vs Attendance')
axs[1].set_xlabel('ExamScore')
axs[1].set_ylabel('Attendance')

axs[2].scatter(data['Attendance'], data['SleepHours'])
axs[2].set_title('Attendance vs SleepHours')
axs[2].set_xlabel('Attendance')
axs[2].set_ylabel('SleepHours')

plt.show()
