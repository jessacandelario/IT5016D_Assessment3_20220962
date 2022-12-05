# MoreFunctionPractice2.py
# Author: Jessa Candelario
# Date: 18.11.22

# Learning Activity 49
# Challenge 2: Write a program that takes a list of numbers (for example, list_1 = [5, 10, 15,
# 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code
# inside a function.

# create the list
list_1 = [2, 4, 6, 8, 10]


# define the function that makes the new list
def get_first_last(list_1):
    """Takes the first and last element in the list"""
    list_2 = [list_1[0], list_1[-1]]
    return list_2


print("\nThe first and last items from the list are: ", get_first_last(list_1))

# Testing
'''
print("My assertion is:"
      "list = [2, 4, 6, 8, 10], new list = [2, 10")
'''
