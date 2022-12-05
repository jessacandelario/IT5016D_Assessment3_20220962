# SimpleFunction2.py
# Author: Jessa Candelario
# Date: 16.11.22

# Learning Activity 45: #2

# Write a simple program that outputs a random number to the screen every time the user types r.
# If the user types anything else then the program should terminate.

import random


def letter(answer):
    """Prints a random number to the screen everytime 'r' in entered"""
    if answer == "r":
        print(random.randint(0, 10))
        answer = input("Enter a letter\n")
        return letter(answer)
    else:
        return "Wrong letter"


answer = input("enter a letter")
print(letter(answer))