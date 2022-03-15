#Write a Python function to find the largest of three numbers provided as arguments.
"""
def largest(numberOne,numberTwo,numberThree):
	largest=numberThree if numberThree>(numberOne if numberOne>numberTwo else numberTwo) else (numberOne if numberOne>numberTwo else numberTwo)
	print("Largest:"+str(largest))
	
numberOne=int(input("Enter 1st number:"))
numberTwo=int(input("Enter 2nd number:"))
numberThree=int(input("Enter 3rd number:"))
largest(numberOne,numberTwo,numberThree)
"""
#Try to send 1 arg in largest()
def largest(number):
	largest=number[2] if number[2]>(number[0] if number[0]>number[1] else number[1]) else (number[0] if number[0]>number[1] else number[1])
	print("Largest:"+str(largest))

largest([10,20,30])