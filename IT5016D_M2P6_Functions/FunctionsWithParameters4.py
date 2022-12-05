# FunctionsWithParameters4.py
# Author: Jessa Candelario
# Date: 16.11.22

# Learning Activity 46
# Challenge 4: Write a function that sums all the numbers in a stored list.

# create a list
list_1 = [12, 5, 16, 3]


def total(x):
    """calculates the sum of the values in the list"""
    list_sum = 0
    for value in list_1:
        list_sum += value
    return list_sum


print("The sum of the values is:", total(list_1))

# Testing
'''
print("My assertion is:"
      "list = 12, 5, 16, 3"
      "sum = 36"
'''