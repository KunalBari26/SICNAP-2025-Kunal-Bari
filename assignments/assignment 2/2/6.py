import pandas as pd
import matplotlib as plt

data = pd.read_csv("student_data.csv")
numeric_columns = ['Age', 'Physics', 'Chemistry', 'Mathematics', 'Attendance']
data[numeric_columns] = data[numeric_columns].apply(pd.to_numeric, errors='coerce')
data.dropna(inplace=True)


data['Average Marks'] = data[['Physics', 'Chemistry', 'Mathematics']].mean(axis=1)
data['Pass'] = (
    (data['Physics'] >= 40) & 
    (data['Chemistry'] >= 40) & 
    (data['Mathematics'] >= 40)
).map({True: 'Yes', False: 'No'})
data.to_csv("student_data_cleaned.csv", index=False)

data[['Physics', 'Chemistry', 'Mathematics', 'Attendance']].hist()
plt.savefig('student analysis')
plt.show()
