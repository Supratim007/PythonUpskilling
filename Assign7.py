#Write a Python function to determine whether a given year is a leap year.
#The year is a leap year if it is a multiple of 4 and not a multiple of 100 or a multiple of 400
#Use function
def checkLeapYear(year):
	if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
		print("Leap year")
	else:
		print("Not a leap year")
		
checkLeapYear(int(input("Enter year:")))
	
