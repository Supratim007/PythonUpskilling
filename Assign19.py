#Write a Python program which accepts a sentence. First split the string on a " " (space) delimiter, then join using a hyphen (-) and print the result.

sentence=input("Enter sentence: ")
list=[]
list=sentence.split(" ")
newSentence=""
for ele in list:
	newSentence+=(ele+"-")
print(newSentence[:-1])
	
	
