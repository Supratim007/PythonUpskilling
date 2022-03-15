#Create a dataframe with top 10 best attack data. the data frame should contain only Name and attack column.

import pandas as pd

df=pd.read_csv("data.csv")
df_largest=df.nlargest(10,'Attack')
df_largest=df_largest[['Name','Attack']]
print(df_largest)
