#Replace the Type1 value Fire to Flammer

import pandas as pd

df=pd.read_csv("data.csv")
df['Type 1']=df['Type 1'].replace('Fire','Flammer') #replace
pd.set_option('display.max_rows',None) #display all rows
print(df)