#If you list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
#The sum of these multiples is 23. Write a python program to find the sum of all the multiples of 3 or 5 below 1000.

n=int(input("Enter value of n: "))
sum=0
for i in range(1,n):
	if i%3==0 or i%5==0:
		sum+=i
print("Sum of multiples of 3 or 5 <"+str(n)+": "+str(sum))

#Do in linear time


