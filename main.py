import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {'name': ['Bob', 'Jessica', 'Mary', 'John', 'Mel', 'Tom', 'Dan', 'Bill', 'Alex', 'Kate'],
        'Maths': [5, 8, 7, 9, 6, 7, 8, 7, 5, 6],
        'Science': [9, 5, 4, 5, 9, 3, 8, 6, 7, 5],
        'English': [7, 55, 6, 3, 8, 3, 5, 6, 7, 8],
        'History': [7, 5, 6, 7, 3, 6, 8, 9, 4, 6],
        'Chemistry': [4, 5, 8, 9, 5, 8, 6, 5, 9, 6]}

df = pd.DataFrame(data)

print(df.head(5))
print('------')
print(f'Mean value in subject: {dict(zip([subj for subj in df.columns[1:]], [float(df[subj].mean()) for subj in df.columns[1:]]))}')
print('------')
print(f'Median value in subject: {dict(zip([subj for subj in df.columns[1:]], [float(df[subj].median()) for subj in df.columns[1:]]))}')
print('------')
print(f'Lower quartile in Maths: {float(df["Maths"].quantile(0.25))}')
print('------')
print(f'Upper quartile in Maths: {float(df["Maths"].quantile(0.75))}')
print('------')
print(f'IQR in Maths: {float(df["Maths"].quantile(0.75) - df["Maths"].quantile(0.25))}')
print('------')
print(f'Standard deviation of marks in subject: {dict(zip([subj for subj in df.columns[1:]], [round(float(df[subj].std()), 2) for subj in df.columns[1:]]))}')
print('------')
