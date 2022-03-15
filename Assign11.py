"""
Write a Python function that takes a list of complex numbers as an argument and returns the sum of all the items in the list as a string.
Sample input: ["2+3i", "3-i"]
Expected Result: "5+2i"
"""
def findComplexSum(list):
	real=0
	imaginary=0
	for x in list:
		if "+" in x:
			re=int(x.split('+')[0]) #assigning real part of a complex number
			img=x.split('+')[1] #assigning complex part of a complex number
			if img=="i":
				imaginary+=1
			else:
				imaginary+=int(img[0])
		elif "-" in x:
			re=int(x.split('-')[0])
			img=x.split('-')[1]
			if img=="i":
				imaginary-=1
			else:
				imaginary-=int(img[:-1])
		real+=re
	if imaginary>0:	
		print(str(real)+"+"+str(imaginary)+"i")
	else:
		print(str(real)+str(imaginary)+"i")
	
findComplexSum(["2+3i", "3-i"])

#Range of list as i/p is not expected