# SlicingChangingList2.py
# Author: Jessa Candelario
# Date: 14.11.22

# Learning Activity 41: #2 Challenge 1: Write a program that prompts the user 3 times to integers. These must be
# appended to a list and then displayed at the end of the program.

my_list = []

for counter in range(0, 3):
    item = int(input("Please enter an integer:"))
    my_list.append(item)

print(my_list)

# Testing
'''
print("My assertion is:"
      "input = 23, 16, 3
      "output = [23, 16, 3]"
'''
