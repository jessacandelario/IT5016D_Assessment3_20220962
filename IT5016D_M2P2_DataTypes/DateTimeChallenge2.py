# DateAndTime.py
# Author: Jessa Candelario
# Date 19.10.22

# Learning Activity 23: Challenge 2
# display 2 weeks later to the date entered

from datetime import datetime
from datetime import timedelta

date_input_2 = input("Please enter a date in DD Mmm YYYY format: \n")

# cast to datetime object
date_object_2 = datetime.strptime(date_input_2, '%d %b %Y')

# compute 2 weeks later
two_weeks_later = date_object_2 + timedelta(days=14)
print(two_weeks_later.date(), "is two weeks after", date_object_2.date(), "\n \n")
