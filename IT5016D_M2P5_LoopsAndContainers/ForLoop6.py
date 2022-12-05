# ForLoop6.py
# Author: Jessa Candelario
# Date: 27.10.22

# Learning Activity 39: # 36: Check type of triangle

print("Input the length of the triangle sides:")
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

if x != y != z:
    print("Scalene Triangle")
elif x == y == z:
    print("Equilateral Triangle")
else:
    print("Isosceles Triangle")