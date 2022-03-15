#Write a program to convert a NumPy array into a csv file.

import numpy as np

arr=np.array([10,20,30,40])
arr.tofile('data1.csv', sep = ',')