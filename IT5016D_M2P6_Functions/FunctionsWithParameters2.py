# FunctionsWithParameters2.py
# Author: Jessa Candelario
# Date: 16.11.22

# Learning Activity 46: Challenge 2
# Write a program that prompts the user for a number and then outputs the first 4 multiples of that number.
# You must use a loop in your method. Assume that the user enters a valid positive integer.


def multiples(number):
    """Prints the first 4 multiples of the number provided"""
    counter = 1
    multiple = number
    while counter <= 4:
        multiple += number
        counter += 1
        print(multiple)


number = int(input("Please enter a number:\n"))
multiples(number)

# Testing
'''
print("My assertion is:"
      "input = 3, output = 6, 9, 12, 15"
      "input = 12, output = 24, 36, 48, 60"
'''
