# NumericOperators3.py
# Author: Jessa Candelario
# Date: 22.10.22

# Learning Activity 30: #1 Shape 3

# let user input value for sides
side_u = int(input("Please enter the length of the rectangle:\n"))
side_m = int(input("Please enter the width of the rectangle:\n"))
side_n = int(input("Please enter the side of the triangle:\n"))

# area = area of rectangle + area of triangle
figure_area = (side_u * side_m +
               side_n / 2 * side_n)

print("The area of the figure is", figure_area)

# Testing
'''
print("My assertions are:"
      "\nu = 9, m = 5, n = 7, output = 269.5"
      "\nu = 15, m = 9, n = 13, output = 219.5")
'''