# Find out the records having the biggest attack and lowest defense.

import pandas as pd

df=pd.read_csv('data.csv')

max_attack=df['Attack'].max()
df.set_index('Attack',inplace=True)
print(df.loc[max_attack]) #record for biggest attack

df.reset_index(inplace=True)

min_defense=df['Defense'].min()
df.set_index('Defense',inplace=True)
print(df.loc[min_defense]) #record for lowest defense
