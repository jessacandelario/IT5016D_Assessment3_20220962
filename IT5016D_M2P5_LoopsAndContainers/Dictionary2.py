# Dictionary2.py
# Author: Jessa Candelario
# Date: 15.11.22

# Learning Activity 43: #2
# Challenge 4: Write a program that sums all the values of a stored dictionary.
# Assume that all the values are integers.

score = {"Test 1": 10,
         "Test 2": 15,
         "Test 3": 35,
         "Test 4": 40}

print("Test scores:")
for item in score.items():
    print(item)

# find the sum
total = 0
for value in score.values():
    total += value

print("\nThe total score is:", total)