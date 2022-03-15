"""
Provided two integers from STDIN (say) a & b. Print three lines where:
    ◦ The first line contains the sum of the two numbers.
    ◦ The second line contains the difference of the two numbers (a – b).
    ◦ The third line contains the product of the two numbers.
"""
print("Enter 2 numbers:")
a=b=int(input())
print("Sum:"+ str(int(a)+int(b)))
print("Difference:"+ str(int(a)-int(b)))
print("Product:"+ str(int(a)*int(b)))