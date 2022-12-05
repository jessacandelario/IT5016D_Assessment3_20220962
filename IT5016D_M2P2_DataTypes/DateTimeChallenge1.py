# DateAndTime.py
# Author: Jessa Candelario
# Date 19.10.22

# Learning Activity 23: Challenge 1
# prints 125 days earlier than the date entered

from datetime import datetime
from datetime import timedelta

date_input = input("Please enter a date in DD Mmm YYYY format: \n")

# cast to datetime object
date_object = datetime.strptime(date_input, '%d %b %Y')

# compute 125 days ago
days_ago = date_object - timedelta(days=125)
print("The date you entered is", date_object.date())
print(days_ago.date(), "is 125 days before ", date_object, "\n")  # using .date() takes just the date, no time
