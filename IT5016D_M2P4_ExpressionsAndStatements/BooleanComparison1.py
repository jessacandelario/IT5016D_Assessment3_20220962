# BooleanComparison1
# Author: Jessa Candelario
# Date: 26.10.22

# Learning Activity 32 : Challenge 1: Enrollment eligibility

# inform the user on what the program does
print("This program works out eligibility for enrolment....\n")
print("Foreign students are subject to International student fees\n")

# let user input details
name = input("Please enter student name: \n")
distance = float(input("Please enter distance in kilometers:\n"))
age = int(input("Please enter student age:\n"))
resident = True
foreign = False

# Test case assertion 1: result should be True
print("Eligibility of", name, "to enroll is:",
      distance < 4
      and 18 > age > 10
      and resident
      or 18 > age > 10
      and foreign, "\n")

print("The student waited for too long...\n")
age = 18

# Test case assertion 2: result should be False
print("The student's eligibility to enrol now is ",
      distance < 4
      and age < 18
      and resident
      or age < 18
      and foreign, "\n")