# SlicingChangingList4.py
# Author: Jessa Candelario
# Date: 14.11.22

# Learning Activity 41: #2 Challenge 6: Write a program that removes duplicates from a stored list. For this
# challenge you must research and use the Python set() function.

my_list = [44, 12, 5, 71, 60, 34, 16, 4, 12]

print("Initial stored list is...\n", my_list, "\n")

print("Removing the duplicates...\n The stored list is now...\n")

# set() = unordered, duplicate elements not allowed
list_1 = set(my_list)  # this removes the duplicate items in my_list
print(list_1, "\n\n")

# Testing
'''
print("My assertion is:"
      "list = 44, 12, 5, 71, 60, 34, 16, 4, 12"
      "output = 34, 4, 5, 71, 44, 12, 16, 60")
'''