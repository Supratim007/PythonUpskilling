#Write a Python program to subtract five days from the current date.

from datetime import timedelta, date
print(date.today()-timedelta(days=5))
