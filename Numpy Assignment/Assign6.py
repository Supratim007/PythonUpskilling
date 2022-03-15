#Write a program to test whether each element of a 1-D array is also present in a second array.
import numpy as np

arr1=np.array([0,10,20,40,60])
arr2=np.array([0,40])
print(str(np.in1d(arr1,arr2)))



