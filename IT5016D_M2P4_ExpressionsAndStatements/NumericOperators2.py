# NumericOperators1
# Author: Jessa Candelario
# Date: 21.10.22

# Learning Activity 30: #1 Shape 2

# let user input value for sides
print("Let us find the area of a figure.\n")
side_q = int(input("Please enter the length of the small rectangle \n"))
side_w = int(input("Please enter the width of the small rectangle \n"))
side_s = int(input("Please enter the length of the big rectangle \n"))
side_g = int(input("Please enter the width of the big rectangle \n"))

# compute for the area
figure_area = side_s * side_g - side_q * side_w
print("\nThe area of the figure is ", figure_area, "\n\n")

# Testing
'''
print("My assertions are:"
      "\nq = 6, w = 4, s = 18, g = 15, output = 246"
      "\nq = 5, w = 3, s = 20, g = 14, output = 265")
'''