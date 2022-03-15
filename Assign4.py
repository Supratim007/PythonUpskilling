#Write a Python function greet() which takes someone’s name as argument and then greets them with hello.
#Try to use format
"""
def helloUser(userName):
	print("Hello "+ userName +"!")
	
userName=input("Enter username:")
helloUser(userName)
"""
txt="Hello {fname}!".format(fname=input("Enter username:"))
print(txt)

	