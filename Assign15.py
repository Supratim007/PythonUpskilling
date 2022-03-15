#Given a list of pairs (tuples with exactly two elements) of the form (a, b) populate a dictionary 
#where the first element of the tuple represent keys and the second element represent their corresponding values.
"""
inputList=tempList=[]
n=int(input("Enter no of tuples:")) #Enter no of tuples

for i in range(n):
	print("Enter tuple values:")
	tempList=input().split() #Split each individual item in list
	inputList.append(tuple(tempList))
print("Input: "+str(inputList))

tempList=[]

for i in inputList:
	for j in i:
		tempList.append(j)
	
dictType={}
dict_iter=iter(tempList)
dictType=dict(zip(dict_iter,dict_iter))
print("Output: "+str(dictType))
"""
#pass the arg as input of a function. Try in 1 line [Hint:Dictionary Comprehension].Use standard func.

def tupleToDict(inputList):
	tempList=[]
	for i in inputList:
		for j in i:
			tempList.append(j)
	
	dictType={}
	dict_iter=iter(tempList)
	dictType=dict(zip(dict_iter,dict_iter))
	print("Output: "+str(dictType))

tupleToDict([('Name', 'Atul'), ('Age', 32), ('Is Member?', True)])