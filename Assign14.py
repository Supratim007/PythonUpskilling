#Given a list of tuples of the form (a, b, 0) 
#replace the last value of the tuples with the sum of their first two values such that the new tuple is (a, b, a+b)
"""
inputList=[]
tempList=[]
n=int(input()) #Enter no of tuples
for i in range(n):
	tempList=input().split()
	for j in range(len(tempList)):
		tempList[j]=int(tempList[j])
	inputList.append(tuple(tempList))
print("Input: ")
print(inputList)
tempList=outputList=[]
for i in range(len(inputList)):
	tempList=list(inputList[i])	
	tempList[2]=tempList[0]+tempList[1]
	outputList.append(tuple(tempList))
	
print("Output: ")
print(outputList)
"""
#Try in 1 line. Hint:List Comprehension, range is not expected from the user

def sumTuple(inputList):
	outputList=[]
	for i in range(len(inputList)):
		tempList=list(inputList[i])	
		tempList[2]=tempList[0]+tempList[1]
		outputList.append(tuple(tempList))
	print("Output: "+str(outputList))
	
sumTuple([(10, 20, 0), (40, 50, 0), (70, 80, 0)])