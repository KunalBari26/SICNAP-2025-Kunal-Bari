import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("student_data.csv")

data['City'].value_counts().plot(kind='bar', title='Number of Students per City')
plt.xlabel("City")
plt.ylabel("Count")
plt.show()

data[['Physics', 'Chemistry', 'Mathematics']].hist()
plt.show()

data['Average Marks'] = data[['Physics', 'Chemistry', 'Mathematics']].mean(axis=1)
plt.scatter(data['Attendance'], data['Average Marks'])
plt.xlabel("Attendance (%)")
plt.ylabel("Average Marks")
plt.title("Attendance vs Average Marks")
plt.show()

data['Gender'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90, title='Gender Distribution')
plt.show()
