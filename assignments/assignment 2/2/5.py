import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("student_data.csv")
gender = data.groupby('Gender')[['Physics', 'Chemistry', 'Mathematics']].mean()
gender.plot(kind='bar')
plt.title("Average Subject-wise Marks by Gender")
plt.ylabel("Marks")
plt.show()

data[['Physics', 'Chemistry', 'Mathematics', 'Attendance']].hist()

plt.show()
