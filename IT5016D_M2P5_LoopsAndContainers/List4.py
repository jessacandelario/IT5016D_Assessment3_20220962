# List4.py
# Author: Jessa Candelario
# Date: 01.11.22

# Learning Activity 40 : #2
# Challenge 2: use the last two lists, outputs the list with the most elements

list_2 = [1, 19, 4, 8]
list_3 = ["land of", "the", "the long white cloud"]

temp_list = [list_2, list_3]
list_print = []

for item in temp_list:
    if len(item) > len(list_print):
        list_print = item

print("The longest list contains {0} elements.\n"
      .format(len(list_print)))

print("The list is {0}"
      .format(list_print))

# Testing
'''
print("My assertion is:"
      "The longest list contains 4 elements."
'''