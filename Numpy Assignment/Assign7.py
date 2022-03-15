#Write a NumPy program to find the set difference of two arrays. The set difference will return the sorted, unique values in array1 that are not in array2.
import numpy as np

arr1=np.array([0,10,20,40,60,80])
arr2=np.array([10, 30, 40, 50, 70, 90])

arr1=np.sort(arr1)
arr2=np.sort(arr2)

print(np.setdiff1d(arr1,arr2))