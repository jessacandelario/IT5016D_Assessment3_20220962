# DateAndTime.py
# Author: Jessa Candelario
# Date 19.10.22

# Learning Activity 23: Challenge 4
# display welcome message,
# prompt user to enter date and integer for year,
# Display date later than the date entered by the year provided

from datetime import datetime

print("Welcome! \n")  # welcome message
date_input_3 = input("Please enter date in DD Mmm YYYY format: \n")
year_input = input("Please enter a number \n")

date_object_3 = datetime.strptime(date_input_3, '%d %b %Y')  # cast to datetime object
print("You have entered the date", date_object_3.date())

# compute for the future date
new_year = date_object_3.year + int(year_input)
new_date = new_year, date_object_3.month, date_object_3.day
print("the date", year_input, "years after", date_object_3.date(), "is", new_date, "\n")