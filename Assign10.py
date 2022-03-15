#Write a Python function that takes a list as an argument and returns the second smallest of all the items in the list.
"""
def findSecondSmallest(list):
	if len(list)<2:
		print("Invalid condition")
	else:
		smallest=list[0] if list[0]<list[1] else list[1]
		secondSmallest=list[1] if list[0]<list[1] else list[0]
		for x in range(2,len(list)):
			if list[x]<secondSmallest and list[x]<smallest:
				secondSmallest=smallest
				smallest=list[x]
			elif list[x]<secondSmallest:
					secondSmallest=list[x]
		print("Second Smallest:"+str(secondSmallest))

maxIndex=int(input("Enter range of list:"))
list=[]
print("Enter list elements: ")
for x in range (0,maxIndex):
	ele=int(input())
	list.append(ele)
	
findSecondSmallest(list)	
"""

#Re-do
def findSecondSmallest(list):
	if len(list)<2:
		print("Invalid condition")
	else:
		list.remove(min(list))
		print("Second smallest: "+str(min(list)))

findSecondSmallest([1,3,5])
		

	
		
		
		
	
	
