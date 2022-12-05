# SlicingChangingList1.py
# Author: Jessa Candelario
# Date: 14.11.22

# Learning Activity 41: #1

# Challenge 1: Write a program that prints a slice showing the 3rd, 4th and 5th elements of this list

print("Challenge 1")
list_1 = [34, 123, 5, 77, 59, 2, 4]

print(list_1[2:5], "\n")

# Testing
'''
print("My assertion is:"
      "output = [5, 77, 59]"
'''

# Challenge 2: Create a stored list with an even number of elements. The list must have no fewer than 6 elements.
# Write a program that returns the first half of all the elements  of any list containing an even number of elements.

print("Challenge 2")
list_2 = [34, 123, 5, 77, 59, 2, 4, 16]

length = len(list_2)
half = (int(length/2))
print(list_2[0:half], "\n")

# Testing
'''
print("My assertion is:"
      "output = [34, 123, 5, 77]"
'''

# Challenge 3: Write a program that returns the last quarter of all the elements of any list whose total number of
# elements is a multiple of four.

print("Challenge 3")
list_3 = [14, 38, 7, 12, 34, 123, 5, 77, 59, 2, 4, 16]

length = len(list_3)
if length % 4 == 0:
    quarter = (int(length/4))
    three_quarters = quarter * 3
    print(list_3[three_quarters: length])

# Testing
'''
print("My assertion is:"
      "output = [2, 4, 16]"
'''