# NumericOperators6
# Author: Jessa Candelario
# Date: 22.10.22

# Learning Activity 30: #2 Shape 3

# import math to get the value of pi
import math

# let user input value for sides
side_e = int(input("Please enter the length of side e:\n"))
side_g = int(input("Please enter the length of side g:\n"))
side_f = int(input("Please enter the length of side f:\n"))

# compute for the area
# area = circle area / 2 + rectangle area + triangle area

figure_area = (math.pi * side_g ** 2 /2
               + side_g * side_e +
               side_g * side_f / 2)

print("The area of the figure is", figure_area)

# Testing
'''
print("My assertions are:"
      "\ne = 5, g = 16, f = 18, output = 626.1"
      "\ne = 3, g = 10, f = 12, output = 247.1")
'''
