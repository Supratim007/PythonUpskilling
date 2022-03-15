#Provided two sets A & B, write a Python program to remove the intersection of B from A.
#find A-(A intersection B)
n=int(input("Enter no of set elements: "))
print("Enter the elements of the first set")
setA=set()
for x in range(0,n):
	setA.add(input())

m=int(input("Enter no of set elements: "))	
print("Enter the elements of the second set")
setB=set()
for x in range(0,m):
	setB.add(input())
setC=set()	
setC=setA.intersection(setB)	
print(setA-setC)