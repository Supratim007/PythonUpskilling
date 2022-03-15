#Write a Python function that takes a list of integers as an argument and returns the product of all the items in the list.

def productListItem(list):
	pdt=1
	for item in list:
		pdt*=item
	return pdt

print("Product: "+str(productListItem([2,3,4])))

#Re-do based on q