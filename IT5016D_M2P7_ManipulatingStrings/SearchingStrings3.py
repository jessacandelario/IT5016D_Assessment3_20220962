# SearchingStrings3.py
# Author: Jessa Candelario
# Date: 20.11.22

# Learning Activity 50: Challenge 8
# Write a program that contains a stored pin as a string.
# The program must evaluate the string and say whether it contains numbers only.

pin = "1234"
if pin.isdigit():  # .isdigit() checks if the string contains digits
    print("This pin is made up only of digits\n\n")
else:
    print("This pin contains characters other than digits\n\n")

# Testing
'''
print("My assertion is:"
      "pin = 1234, output = only digit"
      "pin = abc1, output = contains characters")
'''