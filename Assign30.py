#Write a Python program to convert the below sample JSON to a Python object. 
#After that, again convert this newly created Python object to a JSON string and display it.

import json

f=open('sampleJSON.json')
jsonData=json.load(f) #JSON converted into python object

outputJson=json.dumps(jsonData)
print(outputJson)

#use pojo to access the info...getter setter func
