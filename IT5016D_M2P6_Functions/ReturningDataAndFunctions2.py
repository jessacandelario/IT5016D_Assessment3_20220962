# ReturningDataAndFunctions2.py
# Author: Jessa Candelario
# Date: 16.11.22

# Learning Activity 47:
# Challenge 2: Create a simple calculator that just sums 2 numbers entered by the user. Use the
# function to return the calculated answer to the calling code.

print("\nSum Calculator")


def calculate(number1, number2):
    """Calculates the sum of 2 numbers"""
    total = number1 + number2
    return total


number1 = int(input("\nEnter the first number:"))
number2 = int(input("\nEnter the second number:"))
print("\nThe sum is:", calculate(number1, number2))

# Testing
'''
print("My assertion are:"
      "number1 = 8, number2 = 7, sum = 15"
      "number1 = 16, number2 = 95, sum = 111"
'''