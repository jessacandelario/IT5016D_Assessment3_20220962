# DateAndTime.py
# Author: Jessa Candelario
# Date 19.10.22

# Learning Activity 23: Challenge 3
# take 2 birthdays, and get age difference

from datetime import datetime

print("Let's find the age difference of 2 people")

# assign variables
dob_1 = input("Please enter date of birth of the first person in DD Mmm YYYY format: \n")
dob_2 = input("Please enter date of birth of the second person in DD Mmm YYYY format: \n")

# cast to datetime object
dob_object_1 = datetime.strptime(dob_1, '%d %b %Y')
dob_object_2 = datetime.strptime(dob_2, '%d %b %Y')

# compute for age difference
age_difference = dob_object_1 - dob_object_2
print("Their age difference is", abs(age_difference.days), "days or", round(abs(age_difference.days / 365), 0),
      "years.\n\n")
# abs() gets the absolute value, round() rounds the number up
