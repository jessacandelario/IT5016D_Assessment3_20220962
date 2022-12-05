# NumericOperators8
# Author: Jessa Candelario
# Date: 22.10.22

# Learning Activity 30: #3 Shape 2

# import math for triangle area computation
import math

# let user input value for sides
side_f = int(input("Please enter the length of side f:\n"))

# compute for the area
figure_area = side_f / 2 * side_f * math.cos(math.radians(40))

print("The area of the figure is", figure_area)

# Testing
'''
print("My assertions are:"
      "\nf = 12, output = 55.1"
      "\nf = 6, output = 13.8")
'''
