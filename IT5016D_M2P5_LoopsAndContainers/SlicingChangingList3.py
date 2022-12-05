# SlicingChangingList3.py
# Author: Jessa Candelario
# Date: 14.11.22

# Learning Activity 41: #2
# Challenge 4: An online shopping cart contains the following items: iPhone 7, MacBook Air and a Surface Tablet.
# Write a program that asks the user which item they wish to remove. Assume that the user types in either 0, 1 or 2.
# Use the pop( ) method.

shopping_cart = ["iPhone 7", "MacBook Air", "Surface Tablet"]

item = int(input("Which item would you like to remove. Enter 0,1 or 2\n"))
shopping_cart.pop(item)  # .pop() takes out the item in the list
print(shopping_cart, "\n")

# Testing
'''
print("My assertion is:"
      "input = 0, output = ["MacBook Air", "Surface Table"]"
      "input = 1, output = ["iPhone7", "Surface Tablet"]"
'''