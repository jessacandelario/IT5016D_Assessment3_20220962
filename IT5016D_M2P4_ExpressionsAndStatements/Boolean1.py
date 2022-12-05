# Boolean1.py
# Author: Jessa Candelario
# Date: 24.10.22

# Learning Activity 31 : Challenge 1: Enrollment eligibility

# inform the user on what the program does
print("This will check your eligibility for enrollment\n")
print("The student must be between 10 - 18 years old")
print("Foreign students are subject to International student fees\n")

# let user input details
name = input("Please enter student name: \n")
distance = float(input("Please enter distance in kilometers:\n"))
age = int(input("Please enter student age:\n"))
resident = True
foreign = False

# Test assertions
print("Eligibility of", name, "to enroll is:",
      distance < 4
      and 18 > age > 10
      and resident
      or 18 > age > 10
      and foreign, "\n")
