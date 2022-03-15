"""
open file
create a character list
remove all character other than alphabets
insert char and count as key-value pair in dictionary
"""
#Write a Python program to get the frequency distribution of alphabets (case insensitive) in a provided text file. 
#The frequency distribution should be represented as a dictionary.

import re

f=open("sample.txt")
letterList=[]
for words in f:
	for characters in words:
		letterList.append(characters)
print(letterList)

for i in range(len(letterList)):
	letterList[i]=letterList[i].lower()

refinedList=[]		
for i in range(len(letterList)):
	if letterList[i].isalpha():
			refinedList.append(letterList[i])
print(refinedList)

dictType={}
for item in refinedList:
	if item in dictType:
		dictType[item]+=1
	else:
		dictType[item]=1

print(dictType)

#Use Dictionary Comprehension


