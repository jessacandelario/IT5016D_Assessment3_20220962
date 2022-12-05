# ReturningDataAndFunctions3.py
# Author: Jessa Candelario
# Date: 16.11.22

# Learning Activity 47: Challenge 3
# This task is repeated from earlier in the course. Parking Meter
# IfStatement1.py

print("\nThe Parking Meter"
      "\nRates as follows:"
      "\n$4 for first 2 hours, $3 per succeeding hour")


def parking_fee(hours):
    """Calculates the parking rate"""
    cost = (hours - 2) * 3 + 4
    return cost


hours = int(input("\nEnter the number of hours parked:\n"))
print("The total cost of parking for", hours, "hours is", parking_fee(hours))


# Testing
'''
print("My assertion are:"
      "hours = 3, cost = 7"
      "hours = 10, cost = 28"
'''