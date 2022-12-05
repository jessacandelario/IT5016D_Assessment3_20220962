# NumericOperators9
# Author: Jessa Candelario
# Date: 22.10.22

# Learning Activity 30: #3 Shape 3

# import math to aid in computation
import math

# let user input value for sides
side_e = int(input("Please enter the length of side e:\n"))
side_g = int(input("Please enter the length of side g:\n"))

# find the missing length of the triangle
new_side = side_new = side_g / math.cos(math.radians(38))

# compute for the area
# area = circle area / 2 + rectangle area + triangle area

figure_area = (math.pi * side_g ** 2 /2
               + side_g * side_e +
               side_g * new_side / 2)

print("The area of the figure is", figure_area)

# Testing
'''
print("My assertions are:"
      "\ne = 5, g = 16, output = 644.6"
      "\ne = 3, g = 10, output = 250.5")
'''
