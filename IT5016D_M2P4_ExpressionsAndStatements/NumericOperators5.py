# NumericOperators5
# Author: Jessa Candelario
# Date: 22.10.22

# Learning Activity 30: #2 Shape 2

# import math to get the value of pi
import math

# let user input value for sides
side_c = int(input("Please enter the radius of the circle:\n"))

# compute for the area
# figure area can be computed from circle area / 4
figure_area = math.pi * side_c ** 2 * 3/4

print("The area of the figure is", figure_area)

# Testing
'''
print("My assertions are:"
      "\nx = 23, output = 1246.4"
      "\nx = 8, output = 150.8")
'''
