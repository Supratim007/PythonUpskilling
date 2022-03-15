#Find the not null count for each column.

import pandas as pd

df = pd.read_csv('data.csv')
print(df.info())