import pandas as pd

data = pd.read_csv("student_data.csv")

numeric_columns = ['Age', 'Physics', 'Chemistry', 'Mathematics', 'Attendance']
data[numeric_columns] = data[numeric_columns].apply(pd.to_numeric, errors='coerce')

data.dropna(inplace=True)
