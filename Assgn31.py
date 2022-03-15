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