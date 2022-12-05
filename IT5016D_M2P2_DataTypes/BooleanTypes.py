# Baby.py
#
# author: A. N. Other
# date: September 2016

import random

male = False  # assign variable as False
male = bool(random.randint(0, 1))  # generates random number

if (male):
    print("We will use name Rangi")
else:
    print("We will use name Anihera")

# BoolTests.py
print("Test 1 ", bool(True))
print("Test 2 ", bool(False))
print("Test 3 ", bool("text"))
print("Test 4 ", bool(""))
print("Test 5 ", bool(" "))
print("Test 6 ", bool(0))
print("Test 7 ", bool())
print("Test 8 ", bool(3))
print("Test 9 ", bool(None))
