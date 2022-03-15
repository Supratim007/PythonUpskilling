#Write a Python program which accepts the radius of a circle from the user and compute the area.
#Try to run w/o using math
"""
import math
radius=input("Enter radius:")
area=math.pi*pow(float(radius),2)
print("Area of circle:"+ str(area))
"""

radius=float(input("Enter radius:"))
area=3.14*radius*radius
print("Area of circle:"+ str(area))