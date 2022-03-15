import pandas as pd

df=pd.read_csv('<fie_name>.csv') #reads a csv file into a dataframe
OR
weather_data={'...'}
df=pd.DataFrame(weather_data)

df.shape #returns dimensions of dataset

rows,columns=df.shape #returns rows,columns of the dataset
rows #returns rows,columns of the dataset
columns #returns columns

df.head() #returns 1st 5 records of the dataset
df.head(2) #returns 1st 2 records of the dataset

df.tail() #returns last 5 records of the dataset
df.tail(2) #returns last 2 records of the dataset

df[2:5] #returns record with row no 2 to 4

df.columns #prints the no of columns in the dataset

df['event'] OR df.event #returns event column

type(df['event']) #returns column type

df[['event','day']] #print event, day column

df['temperature'].max() #returns max temperature

df['temperature'].mean() #returns avg temperature

df[df.temperature<=32] #returns records for which temperature>=32



df.describe() #returns statistics of columns

df[df.temperature==df.temperature.max()] # returns record value for which tem is max
OR
df[df.temperature==df['Temperature'].max()]

df['day'][df.temperature==df['Temperature'].max()] #returns day column value for which tem is max

df[['day','Temperature']][df.temperature==df['Temperature'].max()] #returns day and temperature column value for which tem is max

df.index() #returns index

df.set_index('day') #makes the day column as index only displays the modified dataset but doesn't actually modify the dataset

df.set_index('day',inplace=True) #to modify the actual dataset we use inplace cmd

df.loc['1/3/2017'] # return the row for which the mentioned date is the index

df.reset_index(inplace=True) #reset the index to its original format

df.set_index('event',inplace=True) #makes the event column as index

df.loc['Snow'] #returns column for which index=Snow

----------------------------------------------------------------------------------------------------------------------------------------

df=pd.read_excel("<file_name>.xlsx","Sheet1") #read excel file into a dataframe

reading ds in python dictionary or python tuple list

 
#to read dataset as tuple list

weather_data=[(...),(...),(,,,)]
df=pd.DataFrame(weather_data,columns=["day","temperature","windspeed","event"]) #create a dataframe from a list of tuples

----------------------------------------------------------------------------------------------------------------------------------------

df=pd.read_csv('<file_name>.csv',skiprows=1) #skip 1 row from the top of the csv file

df=pd.read_csv('<file_name>.csv',header=None) #displays header as 0,1,2,3,4...
df=pd.read_csv('<file_name>.csv',header=None,names=["ticker","eps","revenue","price","people"]) #whenever there is a missing header in the csv file

df=pd.read_csv('<file_name>.csv',nrows=3) #read only 3 rows from top

df=pd.read_csv('<file_name>.csv',na_values=["not available","n.a."]) #turn not available,n.a. cell values into NaN....for cleansing messy dataframe

df=pd.read_csv('<file_name>.csv',na_values={ #turn certain column cell values as NaN
	'aps':["not available","n.a."],
	'reveue':["not available","n.a.",-1],
	'people':["not available","n.a."]
	})
	
df.to_csv("<file_name>.csv") #write csv file
df.to_csv("<file_name>.csv",index=False) #skip exporting index column to csv file

df.to_csv("<file_name>.csv",columns=["tickers","eps"]) #only write the mentioned columns in the target csv file

df.to_csv("<file_name>.csv",header=False) #skip exporting header

def convert_people_cell(cell):
	if cell=='n.a':
		return 'sam walton'
	else:
		return cell
		
df=pd.read_excel("<file_name>.xlsx","Sheet1",converters={
		'people':convert_people_cell
		})
		
df.to_excel("<file_name>.xlsx",sheet_name='stocks')

df.to_excel("<file_name>.xlsx",sheet_name='stocks',startcol=1,startrow=2) #writes by shifting 1 column from left and 2 rows from top in excel file

df.to_excel("<file_name>.xlsx",sheet_name='stocks',index=False) #to skip exporting index

df_stocks=pd.DataFrame({
	"key1":[" "," "," "],
	...
	})
df_weather=pd.DataFrame({
	"key1":[" "," "," "],
	...
	})
with pd.ExcelWriter('<file_name>.xlsx') as writer:
	df_stocks.to_excel(writer,sheet_name="stocks")
	df_weather.to_excel(writer,sheet_name="weather")

----------------------------------------------------------------------------------------------------------------------------------------

new_df=df.fillna(0)

new_df=df.fillna({
	'temperature':0,
	'windspped':0,
	'event':"no event"
	})

new_df=df.fillna(method='ffill') #fill in the empty cells with the previous day cell value

new_df=df.fillna(method='bfill')#fill in the empty cells with the next day cell value

new_df=df.fillna(method='bfill',axis='columns')

new_df=df.fillna(method='ffill',limit=2)

new_df=df.interpolate()

new_df=df.interpolate(method='time')

new_df=df.dropna() #drops all rows having anomaly

new_df=df.dropna(how 'all') #displays all rows

new_df=df.dropna(thresh=1) #if there is atleast 1 valid (non n.a.) value in a row, then that row is kept

new_df=df.dropna(thresh=2) #if there is 2 valid (non n.a.) value in a row, then that row is kept

dt=pd.date_range("01-01-2019","07-01-2019")
idx=pd.DateTimeIndex(dt)
df=df.reindex(idx)

----------------------------------------------------------------------------------------------------------------------------------------

import pandas as pd
import numpy as np

df=pd.read_csv("data.csv")
new_df=df.replace(-9999,np.NaN)

new_df=df.replace([-9999,-8888],np.NaN)

new_df=df.replace({
	'temperature':-9999,
	'windspeed':-9999,
	'events':0
	},np.NaN)

new_df=df.replace({
	'temperature': '[A-Za-z]',
	'windspeed': '[A-Za-z]',
	},'',regex=True)
	

new_df=df.replace(['poor','average','good','exceptional'],[1,2,3,4])

----------------------------------------------------------------------------------------------------------------------------------------
g=df.groupBy('city')
for city,city_df in g:
	print(city)
	print(city_df)
g.get_group('mumbai') #get dataframe for mumbai
g.max() #get max temp in each of the cities
g.mean() #get mean temp in each of the cities
g.describe() #get statistics in each of the cities

%matplotlib inline
g.plot() #plots corresponding to temp & windspeed

----
ind_weather=pd.DataFrame({
	'city':[" "," "," "],
	'temperature':[,,],
	'humidity':[,,]
	})

us_weather=pd.DataFrame({
	'city':[" "," "," "],
	'temperature':[,,],
	'humidity':[,,]
	})
df=pd.concat([ind_weather,us_weather],ignore_index=True) #remove individual index

df=pd.concat([ind_weather,us_weather],keys=["india","us"]) #creates additional index the data based on dataset

df.loc['india']#retrieve subset of dataframe

----
temperature_df=pd.DataFrame({
	'city':[" "," "," "],
	'temperature':[,,]
},index=[0,1,2])

windspeed_df=pd.DataFrame({
	'city':[" "," "," "],
	'windspeed':[,,]
},index=[1,0])
df=pd.concat([temperature_df,windspeed_df],axis=1) #by default, axis=0 appends the 2 dataframes as rows, while axis=0 appends 2 dataframes as column
#index is a way to align rows of different dataframes
s=pd.Series(["Humid","Dry","Rain"],name="event")
df=pd.concat([temperature_df,s],axis=1)
#concatenating dataset with series
----------------------------------------------------------------------------------

import pandas as pd
df1 = pd.DataFrame({
    "city": ["new york","chicago","orlando"],
    "temperature": [21,14,35],
})

df2 = pd.DataFrame({
    "city": ["chicago","new york","orlando"],
    "humidity": [65,68,75],
})

df3 = pd.merge(df1, df2, on="city")
df3 #print merged dataframes






















