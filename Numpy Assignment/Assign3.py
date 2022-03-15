import numpy as np

arr = np.array([10,2,9,1,8,4,5])
arr=np.sort(arr)
print("Second largest number: "+str(arr[len(arr)-2]))