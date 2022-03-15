#Update the legendary column to True where the type1 = Grass

import pandas as pd

df=pd.read_csv("data.csv")
df.loc[df['Type 1'] == 'Grass', ['Legendary']] = 'True'
pd.set_option('display.max_rows',None)
print(df)