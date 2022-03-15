import csv

sampleList = [{11, 'Ram', 20}, {102, 'Shyam', 45}, {1010, 'Derek', 28}, {1, 'Sheetal', 20}]

fileread=open('sampleRead.csv', 'w',newline='')
with fileread:
    dict_writer = csv.writer(fileread)
    dict_writer.writerows(sampleList)
	
f=(open('sampleRead.csv','r')).read()
print(f.replace("'","").strip())
