# NumericOperators7
# Author: Jessa Candelario
# Date: 22.10.22

# Learning Activity 30: #3 Shape 1

# import math for triangle area computation
import math

# let user input value for sides
side_d = int(input("Please enter the length of side d:\n"))
side_e = int(input("Please enter the length of side e:\n"))

# compute for the area
figure_area = side_d / 2 * math.sqrt(side_e ** 2 - side_d ** 2)

print("The area of the figure is", figure_area)

# Testing
'''
print("My assertions are:"
      "\nd = 12, g = 16, output = 63.5"
      "\nd = 6, e = 14, output = 37.9")
'''
