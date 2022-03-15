#Find out top10 and least10 powerful records based on totals.

import pandas as pd

df=pd.read_csv("data.csv")
df_largest=df.nlargest(10,'Total')
print(df_largest)
df_smallest=df.nsmallest(10,'Total')
print(df_smallest)