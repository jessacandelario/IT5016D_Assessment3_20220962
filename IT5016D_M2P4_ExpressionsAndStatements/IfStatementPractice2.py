# IfStatementPractice2.py
# Author: Jessa Candelario
# Date: 26.10.22

# Learning Activity 34 : Challenge 2: Name the triangle

print("Let us find the type of triangle\n")

# assign variables
side_1 = int(input("Please enter the length of first side: "))
side_2 = int(input("Please enter the length of second side: "))
side_3 = int(input("Please enter the length of third side: "))

# Find out which type of triangle
if side_1 != side_2 != side_3:
    print("It is a Scalene triangle\n"
          "Scalene triangle has no equal sides")
elif side_1 == side_2 == side_3:
    print("It is an Equilateral triangle\n"
          "Equilateral triangle has all sides equal")
else:
    print("Is is an Isosceles triangle\n"
          "Isosceles triangle has 2 equal sides")

# Test assertions
'''
print("My assertions are:"
      "side_1 = 12, side_2 = 12, side_3 = 16, output = Isosceles"
      "side_1 = 10, side_2 = 10, side_3 = 10, output = Equilateral"
      "side_1 = 16, side_2 = 5, side_3 = 8, output = Scalene")
'''


