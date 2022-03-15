"""
matrix = []
  
for i in range(5):  
    # Append an empty sublist inside the list
    matrix.append([])
      
    for j in range(5):
        matrix[i].append(j)
          
print(matrix)
"""
"""
def nested_sum(L):
    total = 0  
    for i in L:
        # checks if `i` is a list
        if isinstance(i, list):  
            total += nested_sum(i)
        else:
            total += i
    return total


print(nested_sum([1, 2, [3, 4], [5, [6]]]))
"""
"""
sample="boy"
print(sample.capitalize())
test="supratim nag"
print(test.title())
"""
"""
def my_function(name="Ajay Kumar Jha"):
	name=name[::-1]
	print(name)
	name=name.split()
	print(name)
	text=""
	x=len(name)
	i=0
	while i<x:
		text=name[x-1].capitalize()
		print(text, end=" ")
		x-=1


my_function()
"""
"""
x,y=input().split()
x=int(x)
print (x+" "+y)
"""
"""
def my_function(n=[4,"Stats", "Amore, Roma", "No 'x' in Nixon", "Was it a cat I saw?"]):
	temp=[]
	num=[]
	result=[]
	x=len(n)
	punc = ''''",?  '''
	for i in range(1,x):
		temp=n[i]
		for k in temp:
			if k in punc:
				temp=temp.replace(k,"")
				temp=temp.lower()
			else:
				temp=temp.lower()
		num=temp[::-1]
		if num == temp:
			result.append("Y")
		else:
			result.append("N")
		
		
	print(result, end=" ")


my_function()
"""
"""
stri=[]
stri=["I","am","a good boy"]
for i in stri:
	print(i)
"""
"""
t=(20,30,40)
c=60
m=list(t)
print(m[:-1]+c)
"""
"""
def my_function(a=[(10, 20, 0), (40, 50, 0), (70, 80, 0)]):
	z=[]
	sum=0
	for i in range (len(a)):
		if type(a[i]) is tuple:
			x=len(a[i])
			m=list(a[i])
			z=a[i]
			for j in range (x):
				y=z[j]	
				if y != 0:
					sum=sum+y
				else:
					break
			print([z[:-1] + (sum,)])
			sum=0



my_function()
"""
"""
import time
  
# ts stores the time in seconds
ts = time.time()
  
# print the current timestamp
print(ts)
"""
"""
import csv 


a=[{11, 'Ram', 20}, {102, 'Shyam', 45},{ 1010, 'Derek', 28},{ 1, 'Sheetal', 20}]
filename = "SampleCSV.csv"
with open(filename, 'w') as csvfile: 
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(a)
file=open("SampleCSV.csv","r")
Read=file.read()
print(Read.strip().replace(',', ' '))
"""
"""
import csv

n = int(input("Enter the number of rows : "))
m = int(input("Enter the number of columns : "))
list = []

for i in range(0, n):

    # Append an empty sublist inside the list
    list.append([])
    for j in range(0, m):
        list[i].append(0)
        print("Enter the elements of Row ", i+1, " of column", j+1, " : ")
        k = input()
        if k.isdigit():
            list[i][j] = int(k)
        else:
            list[i][j] = k

print("\nThe list is : ", list)

# data to be written row-wise in csv file

# opening the csv file in 'w+' mode
file = open('sample.csv', 'w+', newline='')

# writing the data into the file
with file:
    write = csv.writer(file)
    write.writerows(list)

# Using readlines()
file1 = open('sample.csv', 'r')
Lines = file1.readlines()


# Strips the newline character
print("\nThe sample output is : ")
for line in Lines:
    print(line.strip().replace(',', ' '))
    
file.close()
file1.close()
"""
"""
modlst=[]
tmplst=[]
for i in sampleList:
	for j in i:
		print(j)
		#tmplst.append(j)
	print()
	#modlst.append(tmplst)
	#tmplst.clear()

print(modlst)
fileread=open('sampleRead.csv', 'w',newline='')
with fileread:
    dict_writer = csv.writer(fileread)
	#print(dict_writer)
    dict_writer.writerows(modlst)
	


#f=(open('sampleRead.csv','r')).read()

#print(f.replace("'","").strip())
file1 = open('sampleRead.csv', 'r')
Lines = file1.readlines()


# Strips the newline character
print("\nThe sample output is : ")
for line in Lines:
    print(line.strip().replace(',', ' '))


cmd for pip upgrade:
'c:\users\supratim\appdata\local\programs\python\python39\python.exe -m pip install --upgrade pip'
"""

import csv
#import copy
#import pandas

mumberOfelementsinLIst=int(input("Enter number of dict in List: "))

NumnerOfInputs=int(input("Enter number of elements to be inserted: "))
dictElement ={}
list_dict=[]

for i in range(mumberOfelementsinLIst):
    dictElement ={}
    for j in range(NumnerOfInputs):
        k= input("Enter Key: ")
        v=input("Enter Values: ")
        dictElement.update({k:v})
    
    print(dictElement)
    list_dict.append(dictElement)
    #list_dict[i] = copy.deepcopy(dictElement)
    print(list_dict)



keys = list_dict[0]. keys()
a_file = open("output.csv", "w")
dict_writer = csv. DictWriter(a_file, keys)
dict_writer. writeheader()
dict_writer. writerows(list_dict)
a_file. close()


file1=open("output.csv", "r")
lines=file1.readlines()
for line in lines:
    print(line.strip().replace(',',' '))
file1.close()