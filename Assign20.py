"""
The word or whole phrase which has the same sequence of letters in both directions is called a palindrome. Here are few examples:
   ◦ Stats
   ◦ Amore, Roma               
   ◦ No 'x' in Nixon
   ◦ Was it a cat I saw?
As you see, case of the letters is ignored. Spaces and punctuation are ignored too. Your goal in this programming exercise is to determine, whether the phrase represents a palindrome or not. Input data contains number of phrases in the first line. Next lines contain one phrase each.
Answer should have a single letter (space separated) for each phrase: Y if it is a palindrome and N if not.

"""
import string
k=string.punctuation+" "
n=int(input())
inputText=[]
answer=""
for j in range(n):
	inputText.append(input())
for c in inputText:
	for i in c:
		if i in k:
			c=c.replace(i,"")
	if c.lower()==(c.lower())[::-1]:
		answer+="Y "
	else:
		answer+="N "

print(answer)