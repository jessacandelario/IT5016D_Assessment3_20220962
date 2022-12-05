# ReturningDataAndFunctions4.py
# Author: Jessa Candelario
# Date: 16.11.22

# Learning Activity 47: Challenge 13
# Write a Calculator program that meets the following requirements:
# The program displays an appropriate welcome message and user instructions.
# It prompts the user for their required operation, first number and second number.
# It performs the required operation using the 2 numbers and displays the result on screen.
# The program loops until the user enters "exit".
# Assume that the user enters only valid integers or "exit".
# The operations to be performed are add, subtract, multiply and divide.

# Welcome message
print("\nWelcome to Calculator!"
      "\nEnter the desired operation: add, subtract, multiply, divide."
      "\nEnter 'exit' to end the program.")

# create a dictionary for operations
operations = {"add": "+",
              "subtract": "-",
              "multiply": "*",
              "divide": "/",
              "exit": "X"}


# Define the function for number input
def get_number(nth):
    """Prompts for number input"""
    while True:
        n1 = input('\nPlease enter the ' + nth + ' number: ')
        if n1.isnumeric():  # .isnumeric() check if string  is numeric
            return int(n1)
        elif n1.lower() == "exit":
            return n1
        else:
            print("You need to enter an integer, try again")


# create the function for operations
def compute(op, n1, n2):
    """Performs the operation"""
    if op == "add":
        result = n1 + n2
    elif op == "subtract":
        result = n1 - n2
    elif op == "multiply":
        result = n1 * n2
    elif op == "divide":
        result = n1 / n2
    else:
        return "Error: operation not found."
    return result


while True:
    op = input("\nPlease enter the desired operation:\n").lower()
    if op in operations.keys():
        if op != "exit":
            n1 = get_number("first")
            if n1 == "exit":
                break
            n2 = get_number("second")
            if n2 == "exit":
                break
            result = compute(op, n1, n2)
            print('\n', n1, operations[op], n2, '=', result)
        else:
            print("Thanks for using the calculator")
            break
    else:
        print("Please enter one of these: add, subtract, multiply, divide, or exit")


# Testing
'''
print("My assertion is:"
      "n1 = 9, n2 = 10, op = add, result = 9 + 10 = 19"
      "n1 = 9, n2 = 10, op = multiply, result = 9 * 10 = 90")
'''
