#In a barplot show fastest type 1 record in ascending order. (use the speed column to find out the fastest)

import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv("data.csv")
df=df[['Type 1','Speed']] #narrowing the dataframe to two columns-Type 1 & Speed
df=df.groupby('Type 1') #applying groupby based on Type 1 records
df=df.sum() #finding the sum of the Speed column per Type 1 record
df=df.sort_values(by=['Speed'],ascending=True) #sorting the dataframe based on Speed value in ascending order
df.plot.bar(figsize=(6,20)) #declaring width and height of the bar chart
plt.show() #display bar chart
