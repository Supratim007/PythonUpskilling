#Given the names and grades for each student in a class of n students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade. 
#If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

namenestedList=[]
marksList=[]
n=int(input())
while n>0:
	name=input()
	marks=float(input())
	templst=[marks,name]
	namenestedList.append(templst)
	marksList.append(marks)
	n-=1

namenestedList=sorted(namenestedList)
marksList=sorted(list(set(marksList))) #to sort the list and to remove duplicate marks values

secondLowest=marksList[1]
finalnamelist=[]
for i in namenestedList:
	if i[0]==secondLowest:
		finalnamelist.append(i[1])
	elif i[0]<secondLowest:
		continue
	else:
		break

print(sorted(finalnamelist))