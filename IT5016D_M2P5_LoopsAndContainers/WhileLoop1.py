# WhileLoop1.py
# Author: Jessa Candelario
# Date: 27.10.22

# Learning Activity 37
# Challenge 1: prints 1 through to n in square brackets.

number = int(input("Please enter a number\n"))
counter = 0

while counter < number:
    print("[", counter + 1, "] ", end="")
    counter +=1

# Test assertions
'''
print("My assertions are"
    "number = 3, output = [1] [2] [3]"
    "number = 1, output = [1]")
'''