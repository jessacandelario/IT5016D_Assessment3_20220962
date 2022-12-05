# DateAndTime.py
# Author: Jessa Candelario
# Date 19.10.22

# Learning Activity 23: Challenge 5
# Prompts 2 dates, print difference of dates in years

from datetime import datetime

date_input_4 = input("Please enter first date in DD Mmm YYYY format: \n")
date_input_5 = input("Please enter second date in DD Mmm YYYY format: \n")

date_object_4 = datetime.strptime(date_input_4, '%d %b %Y')
date_object_5 = datetime.strptime(date_input_5, '%d %b %Y')

difference = abs(date_object_4.year - date_object_5.year)  # .year takes just the year

print("The dates are", difference, "years apart. \n")
