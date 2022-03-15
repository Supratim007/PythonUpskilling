#Write a Python program for getting the sum of all numbers in a nested list of varying sizes.
#Sample Data: [1, 2, [3, 4], [5, [6]]]
#Expected Result: 21

def nestedListSum(listInput):								
	sum = 0 #sum initialization
	for i in listInput: #iterates over the entire input list
		if isinstance(i,int):
			sum += i #calculates the sum of all the integers in the nested list
		else:
			sum += nestedListSum(i) #recursion performed to move the next iteration into the next nested list
	return sum
		
print(nestedListSum([1, 2, [3, 4], [5, [6]]]))
	
