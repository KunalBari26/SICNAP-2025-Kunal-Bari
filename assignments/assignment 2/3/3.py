import pandas as pd
from pandas.errors import ParserError

try:
    data = pd.read_csv("student_data.csv")
except FileNotFoundError:
    print("file student_data.csv was not found.")    
except ParserError:
    print("Failed to parse the file student_data.csv.")

if data is not None:
    print("File read successfully")

required_columns = ['Name', 'Age', 'Gender']
for col in required_columns:
    if col not in data.columns:
        raise ValueError(f"Missing columns in the file: {col}")
