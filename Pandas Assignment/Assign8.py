#Create pie chart Legendary vs non Legendary

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("data.csv")
df=df["Legendary"].dropna() #removes all null records in the Legendary column
df=df.value_counts() #returns the count of each unique record in the Legendary column
df.plot.pie(figsize=(20,15)) #plots pie chart
plt.show() #display pie chart