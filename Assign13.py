"""
Create a function that takes an integer n and returns the identity matrix of n x n dimensions. 
If the integer is negative (-n), return the mirror image of the identity matrix of n x n dimensions. 
It does not matter if the mirror image is left-right or top-bottom.
Sample Input: 3
Expected Output: [[1, 0,  0], [0, 1, 0], [0, 0, 1]]

Sample Input: -3
Expected Output: [[0, 0,  1], [0, 1, 0], [1, 0, 0]]
"""

"""
Normal solution:

n=int(input("Enter value of n: "))
if n>0:
	for i in range(0,n):
		for j in range(0,n):
			if i==j:
				print("1",end=" ")
			else:
				print("0",end=" ")
		print()
elif n<0:
	for i in range(0,abs(n)):
		for j in range(0,abs(n)):
			if j==abs(n)-i-1:
				print("1",end=" ")
			else:
				print("0",end=" ")
		print()	
"""
#Optimized Solution
n=int(input("Enter value of n: "))
for i in range(0,abs(n)):
		for j in range(0,abs(n)):
			if n>0:
				if i==j:
					print("1",end=" ")
				else:
					print("0",end=" ")
			elif n<0:
				if j==abs(n)-i-1:
					print("1",end=" ")
				else:
					print("0",end=" ")
		print()

#Try in 1 line		