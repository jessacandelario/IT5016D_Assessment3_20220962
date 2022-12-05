# ReturningDataAndFunctions4.py
# Author: Jessa Candelario
# Date: 16.11.22

# Learning Activity 47
# Challenge 8: Write a function that takes 3 integer parameters and returns boolean. If the
# first number is within the range between the second and third numbers (inclusive) then the function should return
# True, otherwise it should return false.

# welcome message
print("\nLet's find out if the first number is between the second and the third number.")


# create the function to test boolean conditions
def test(num1, num2, num3):
    if (num2 < num1 < num3) or (num2 > num1 > num3):
        return True
    else:
        return False


# ask user to input integers to be tested
num1 = int(input("\nEnter first number:"))
num2 = int(input("\nEnter second number:"))
num3 = int(input("\nEnter third number:"))

# print result
print("It is", test(num1, num2, num3),
      "that", num1, "is between", num2, "and", num3)


# Testing
'''
print("My assertion is:"
      "num1 = 100, num2 = 10, num3 = 16, output = False"
      "num1 = 15, num2 = 4, num3 = 38, output = True")
'''
