import pandas as pd

data = pd.read_csv("student_data.csv")

data['Average Marks'] = data[['Physics', 'Chemistry', 'Mathematics']].mean(axis=1)
data['Pass'] = (
    (data['Physics'] >= 40) & 
    (data['Chemistry'] >= 40) & 
    (data['Mathematics'] >= 40)
).map({True: 'Yes', False: 'No'})

print(data.groupby('Gender')[['Average Marks', 'Attendance']].mean())
print(data.sort_values(by='Average Marks', ascending=False).head(5))
print(data['Pass'].value_counts())
