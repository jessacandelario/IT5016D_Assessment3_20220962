# SplittingStrings3.py
# Author: Jessa Candelario
# Date: 23.11.22

# Learning Activity 52
# Challenge 1: Write a program that takes a single user input of 3 integers separated by commas
# and then outputs the average of the numbers.

# let user input 3 numbers
numbers = input("\nPlease enter 3 numbers separated by commas: \n")

# split the string into 3 numbers
split_numbers = numbers.split(",")

# create the list containing 3 given numbers as integers
int_num_list = [int(x) for x in split_numbers]

# get the average
average = sum(int_num_list) / len(int_num_list)
print("The average of the given numbers is:\n", average)

# Challenge 2: Write a program that takes a single user input of any number of integers separated by commas
# and then outputs the sum of the numbers.

# get the sum
total = sum(int_num_list)
print("\nThe sum of the given numbers is: \n", total)

# Testing
'''
print("My assertion is:
      "input = 4, 6, 8, average = 6.0, sum = 18"
      "input = 5, 10, 15, average = 10.0, sum = 30"
'''