#Write a program to test element-wise for complex number, real number of a given array. Also test whether a given number is a scalar type or not.

import numpy as np

arr=np.array(["1","2+3i","7F"])
for x in arr:
	if np.is_integer(x):
		print(str(x)+":"+"Real")
	elif 'i' in x:
		print(str(x)+":"+"Complex")
	elif np.isalpha() in x:
		print(str(x)+":"+"Scalar")
	else:
		print()
