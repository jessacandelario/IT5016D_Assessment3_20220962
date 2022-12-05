# BooleanComparison2
# Author: Jessa Candelario
# Date: 26.10.22

# Learning Activity 32 : Challenge 2: Eligibility to enter the bar

# import date to calculate age
from datetime import date

# Let user input details
name = input("Please enter your name: \n")
year_of_birth = input("Please enter your year of birth: \n")

# assign variable to current year
current_year = date.today().year

print("\nThe result of this application is",
      str(current_year - int(year_of_birth) >= 21)
      and name != "Suzanne May"
      and name != "Wiremu Rangi")