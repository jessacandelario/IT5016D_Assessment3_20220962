# SlicingChangingList5.py
# Author: Jessa Candelario
# Date: 14.11.22

# Learning Activity 41: #2
# Challenge 10: Write a Python program to shuffle and print a stored list.

import random

my_list = [26, 15, 98, 16, 35]
print("The list is:\n", my_list)

print("Shuffling the list...\n")

# shuffle items using random.shuffle
random.shuffle(my_list)

print("Shuffled list is:\n", my_list)

# Testing
# output may be in different order every run because of shuffle
'''
print("My assertion is:"
      "list = 26, 15, 98, 16, 35"
      "output = 16, 35, 98, 15, 26")
'''