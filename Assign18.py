#Write a Python program which accepts the user’s full name and prints each part of the name in reverse without breaking the order 
#and with correct capitalization.
"""
def listToString(s):
 str1 = " " 
 # return string  
 return (str1.join(s))

nameInput=input("Enter the name: ")
temp=nameInput.lower()  #converting the entire string into lowercase
tempList=list(temp.split(" ")) #split the string based on space and then convert the string into list 
strTemp=""
for i in range(0,len(tempList)):
		tempList[i]=tempList[i][::-1] #reversing each item in list

strTemp=listToString(tempList) #converts the list into string
print(strTemp.title()) #converts first character of every word of string into uppercase
"""
nameInput=input("Enter the name: ")
nameInput=nameInput[::-1]
nameInput=nameInput.split(" ")
strTemp=""
for i in range(0,len(nameInput)):
	strTemp=strTemp+nameInput[i].capitalize()+" "
print(strTemp)