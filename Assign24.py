"""
Consider a list (list = []) where you can perform the following commands:
        1. insert i e: Insert integer e at position i.
        2. print: Print the list.
        3. remove e: Delete the first occurrence of integer.
        4. append e: Insert integer at the end of the list.
        5. sort: Sort the list.
        6. pop: Pop the last element from the list.
        7. reverse: Reverse the list.
Initialize your list and read in the value of n followed by n lines of commands where each command will be of the types listed above. Iterate through each command in order and perform the corresponding operation on your list.
Input Format: The first line contains an integer, n, denoting the number of commands. Each line i of the n subsequent lines contains one of the commands described above.
Constraints: The elements added to the list must be integers.
Output Format: For each command of type print, print the list on a new line.
"""			
n=int(input())
lst=[]
while n>0:
	cmd=input()
	temp=cmd.split()
	if temp[0]=="insert":
		index,item=temp[1],int(temp[2])
		lst.insert(int(index),item)
	elif temp[0]=="print":
		print(lst)
	elif temp[0]=="remove":
			if int(temp[1]) in lst:
				lst.remove(int(temp[1]))
	elif temp[0]=="append":
		lst.append(int(temp[1]))
	elif temp[0]=="sort":
		lst.sort()
	elif temp[0]=="pop":
		lst.pop(-1)
	elif temp[0]=="reverse":
		lst.reverse()
	else:
		print("Wrong input")
	n-=1

		
	
	