# WhileLoop2.py
# Author: Jessa Candelario
# Date: 27.10.22

# Learning Activity 37
# Challenge 2: computes the sum of the first n positive integers: sum = 1 + 2 + 3 + ... + n

number = int(input("Please enter a number:"))
counter = 0
total = 0

while counter <= number:
    total = total + counter
    counter += 1

print("n =", number, "sum =", total)

# Test assertions
'''
print("My assertions are"
    "number = 5, sum = 15"
    "number = 8, output = 36")
'''