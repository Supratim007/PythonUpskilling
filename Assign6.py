#Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
"""
def factorial(number):
	fact=1
	while number > 0:
		fact*=number
		number-=1
	print("Factorial:"+str(fact))

number=int(input("Enter number:"))
factorial(number)
"""
#Try to use recursion
def factorial(number):
	if number > 0:
		return number*factorial(number-1)
	else:
		return 1
	
	
print("Factorial: "+str(factorial(6)))