# List1.py
# Author: Jessa Candelario
# Date: 28.10.22

# Learning Activity 40 : #1 Task 1
# Copy List.py, @ author: A. N. Other, date: September 2016, Change 3 index variables, including at least one negative index

# empty list
my_list_empty = []

# list of integers
my_list_int = [1, 2, 3]

# list with mixed datatypes
my_list_mix = [1, "Hello", 3.4]

# nested list (list within a list)
my_list_nested = ["mouse", [8, 4, 6]]

my_list = ['p', 'r', 'o', 'b', 'e']
print(my_list[3])  # Output: b
print(my_list[-1])  # Output: e
print(my_list[-4])  # Output: r

# Error! Only integer can be used for indexing
# my_list[4.0]

# Nested List
n_list = ["Happy", [2, 0, 1, 6]]

# Nested indexing
print(n_list[0][1])  # Output: a
print(n_list[1][3])  # Output: 6

# using negative indexing
print(my_list[-1])  # Output: e
print(my_list[-5])  # Output: p
