# FunctionsWithParameters1.py
# Author: Jessa Candelario
# Date: 16.11.22

# Learning Activity 46 Challenge 1: Write a program that prompts the user for their name and then their phone number
# (The program may store both as text) Use a function to output the following text: Hello there, my name is < name of
# user > and my number is < phone number >.


def display(name, number):
    """Displays the name and the number from user input"""
    print("\nHello there, my name is", name, "and my number is", number)


# ask user to input details
name = input("Please enter your name:\n")
number = input("Please enter your mobile number:\n")
# call the function
display(name, number)


# Testing
'''
print("My assertion is:"
      "name = Jessa, number = 02012345678,"
      "output = Hello there, my name is Jessa and my number is 02012345678"
'''