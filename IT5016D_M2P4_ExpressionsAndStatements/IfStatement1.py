# IfStatement1.py
# Author: Jessa Candelario
# Date: 26.10.22

# Learning Activity 33 : Challenge 1
# Parking meter

print("Kia Ora, this is a parking meter\n")
park_time = int(input("Please enter park time in hours: "))

rate = 4
cost = 0
if park_time > 3:
    cost = rate * 3
    rate -= 2  # drop the rate by $2
    park_time -= 3  # get the remainder of the parking time
    cost += rate * park_time  # add to the current cost
    print("The cost of the parking is $", cost)
else:
    cost = rate * park_time
    print("The cost of the parking is $", cost)

# test case assertion 1
'''
park_time = 6
total cost of parking = $18
'''

# test case assertion 2
'''
park_time = 2
total cost of parking = $8
'''