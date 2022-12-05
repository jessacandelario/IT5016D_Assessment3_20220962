# SimpleFunction2.py
# Author: Jessa Candelario
# Date: 16.11.22

# Learning Activity 45: #2

# Write a program that displays a welcome message,then displays the result of adding 2 integers.
# The integers must be defined in the add_numbers( ) function.

print("\nLet's add 2 numbers!")


def add_numbers(a, b):
    """Adds the given numbers."""
    s = a + b
    return s


print(add_numbers(3, 6))
input("Press enter to continue.")


# Write a program that stores an integer value x and a string of value y (you can choose these values).
# The program must use a method that displays the y text, x number of times.


def print_me(x, y):
    """Prints y, x number of times"""
    return y * x


print("\n", print_me(5, "hello "))