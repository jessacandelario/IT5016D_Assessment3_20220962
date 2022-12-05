# MoreFunctionPractice1.py
# Author: Jessa Candelario
# Date: 18.11.22

# Learning Activity 49
# Challenge 1: Write a currency conversion program that accepts user entry to set the conversion
# rate between New Zealand dollars and any other currency of your choosing. The program must then request a
# conversion type (either to or from) and the amount being converted. The program must do the conversion and display
# the result to the user before terminating.

# input exchange rate
rate = float(input("\nPlease enter the conversion rate between NZD and USD\n"))
# let user choose how to convert
choice = input("\nPlease enter 'to' or 'from\n")
# let user input amount to be converted
amount = float(input("\nPlease enter the amount you wish to convert\n"))


# function for conversion
def convert(x, y, z):
    """calculates the conversion"""
    result = float
    if type == "to":
        result = amount * rate
    else:
        result = amount * (1 / rate)
    return result


exchange_rate = convert(rate, type, amount)

print("Amount when converted to NZD = {0} USD".format(exchange_rate, type))


# Testing
'''
print("My assertion is:"
      "0.5, to, 100, output = 200"
      "0.5, to, 100, output = 50")
'''