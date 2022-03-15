#Suppose you have a number n. You have to print all numbers from 1 to n (both numbers included) provided the following constraints.
#    ◦ If the number is divisible by 3, write Fizz instead of the number
#    ◦ If the number is divisible by 5, write Buzz instead of the number
#    ◦ If the number is divisible by 3 and 5 both, write FizzBuzz instead of the number

n=int(input("Enter value of n: "))
for i in range(1,n+1):
	if i % 3 == 0 and i % 5 == 0:
		print("FizzBuzz")
	elif i % 3 == 0:
		print("Fizz")
	elif i % 5 == 0:
		print("Buzz")
	else:
		print(i)
	
#try in single line

