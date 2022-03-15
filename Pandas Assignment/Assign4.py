#Top 10 combination of Type1 and Type2 records.

import pandas as pd
"""  
with open("data.csv") as csv_file:
    # read the csv file
    csv_reader = csv.reader(csv_file)
  
    # now we can use this csv files into the pandas
    df = pd.DataFrame([csv_reader], index = None)
#read=pd.read_csv('data.csv')
#df=pd.Dataframe(read)
print(np.unique(df[['Type 1', 'Type 2']].values))

#concatenating 2 columns and then select unique values from the column
Assign4
df=pd.read_csv('data.csv')
cn=df['Type 1'].unique()
pwr=df.groupby(['Type 1'])["Total"].sum().nsmallest(len(cn))
pwr.plot.bar(x='Type 1',y='Total',rot=0,figsize=(14,9))

#x= df.groupby("Type 1").Total.sum().sort_values(ascending= False)

df.sortvalues('Attack',ascending=True)
df=df[df['Type 1']=='Grass']
"""
"""

df_typeone=df['Type 1'].unique()
df_typetwo=df['Type 2'].unique()
df = df[df_typeone,df_typetwo]
#det=det.unique()
print(df.head(10))
"""
df=pd.read_csv('data.csv')
df=df[['Type 1','Type 2']]
new_df=df.dropna()
new_df=new_df['Type 1']+"-"+new_df['Type 2']
new_df=pd.unique(new_df)
print(new_df[:10])