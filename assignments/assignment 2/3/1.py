import pandas as pd
import matplotlib.pyplot as plt

def scatter_plot(data, x_col, y_col):
    if x_col not in data.columns or y_col not in data.columns:
        raise ValueError(f"Columns '{x_col}' or '{y_col}' not found")
    
    plt.scatter(data[x_col], data[y_col])
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(f'Scatter Plot: {x_col} vs {y_col}')
    plt.show()

data = pd.read_csv("sample_data.csv")
scatter_plot(data, 'StudyHours', 'ExamScore') 

data = pd.read_csv("3d_sample_data.csv")
scatter_plot(data, 'X', 'Y')  
