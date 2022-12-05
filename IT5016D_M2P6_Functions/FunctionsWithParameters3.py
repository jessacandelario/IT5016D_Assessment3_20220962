# FunctionsWithParameters3.py
# Author: Jessa Candelario
# Date: 16.11.22

# Learning Activity 46
# Challenge 3: Write a program that prompts the user to enter the integers x and y. The program
# must then output the first y multiples of x separated by commas. An example is: x = 4 and y = 3  output = 4, 8, 12.


def display(number, multiple):
    """outputs the first y multiples of x"""
    counter = 1
    base = number
    while counter <= multiple:
        base += number
        counter += 1
        print(base, ",")


# let user input integers
number = int(input("Please enter a number:\n"))
multiple = int(input("Please enter the number of multiples to be generated:\n"))
# call the function
display(number, multiple)

# Testing
'''
print("My assertion is:"
      "number = 3, multiple = 3, output = 6, 9, 12"
      "number = 5, multiple = 4, output = 10, 15, 20, 25")
'''