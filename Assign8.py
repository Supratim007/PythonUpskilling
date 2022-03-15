#Write a Python function that takes a list of integers as an argument and returns the largest of all the items in the list.
#Use list functions

def findLargest(list):
	if len(list)>0:
		return max(list)
	else:
		return None
		
print("Largest: "+str(findLargest([1,3,5])))


	