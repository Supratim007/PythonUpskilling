#Write a Python program to convert UNIX timestamp string to readable date.
from datetime import datetime

print(datetime.fromtimestamp(int(input())/1000))
