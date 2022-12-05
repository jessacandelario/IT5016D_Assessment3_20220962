# WhileLoop3.py
# Author: Jessa Candelario
# Date: 27.10.22

# Learning Activity 37
# Challenge 3: Prints multiples of p from 10 until the value of q (inclusive)

p = int(input("Please enter the preferred increment:"))
q = int(input("Please enter the ending number"))

# start_number has to start from 10
start_number = (10 % p) + 10
counter = 10

while counter <= q:
    print(start_number, end=", ")
    start_number += p
    counter += p

# Test assertions
'''
print("My assertions are"
    "p = 2, q = 20, output = 10, 12, 14, 16, 18, 20"
    "p = 5, q = 30, output = 10, 15, 20, 25, 30")
'''