# DateAndTime.py
# Author: Jessa Candelario
# Date 19.10.22

# Learning Activity 23 : compilation of all challenges

from datetime import datetime
from datetime import timedelta

# Challenge 1: prints 125 days earlier than the date entered
date_input = input("Please enter date in DD Mmm YYYY format: \n")

# cast to datetime object
date_object = datetime.strptime(date_input, '%d %b %Y')

# compute 125 days ago
days_ago = date_object - timedelta(days=125)
print("The date you entered is", date_object.date())  # using .date() takes just the date part
print("It was", days_ago.date(), "125 days ago.\n \n")


# Challenge 2: display 2 weeks later to the date entered
date_input_2 = input("Please enter a date in DD Mmm YYYY format: \n")

# cast to datetime object
date_object_2 = datetime.strptime(date_input_2, '%d %b %Y')

# compute 2 weeks later
two_weeks_later = date_object_2 + timedelta(days=14)
print(two_weeks_later.date(), "is two weeks after", date_object_2.date(), "\n \n")

# Challenge 3: take 2 birthdays, and get age difference
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
      "years. \n \n")
# abs() gets the absolute value, round() rounds the number up


# Challenge 4: display welcome message, prompt user to enter date and integer for year
# Display date later than the date entered by the year provided
print("Welcome! \n")
date_input_3 = input("Please enter date in DD Mmm YYYY format: \n")
year_input = input("Please enter a number \n")

date_object_3 = datetime.strptime(date_input_3, '%d %b %Y')
print("You have entered the date", date_object_3.date())

# compute for the future date
new_year = date_object_3.year + int(year_input)
new_date = new_year, date_object_3.month, date_object_3.day
print("the date", year_input, "years after", date_object_3.date(), "is", new_date, "\n")


# Challenge 5: prompts 2 dates, print difference of dates in years
date_input_4 = input("Please enter first date in DD Mmm YYYY format: \n")
date_input_5 = input("Please enter second date in DD Mmm YYYY format: \n")

date_object_4 = datetime.strptime(date_input_4, '%d %b %Y')
date_object_5 = datetime.strptime(date_input_5, '%d %b %Y')

difference = abs(date_object_4.year - date_object_5.year)  # abs() gets the absolute value

print("The dates are", difference, "years apart. \n")
