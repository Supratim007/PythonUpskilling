#In a barplot show Most powerful type 1 record in ascending order ( power = summation of "Total" column for each "Type1" type )

import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv("data.csv")
df=df[['Type 1','Total']]
df=df.groupby('Type 1')
df=df.sum()
df=df.sort_values(by=["Total"],ascending=True)
df.plot.bar(figsize=(10,13))
plt.show()
	