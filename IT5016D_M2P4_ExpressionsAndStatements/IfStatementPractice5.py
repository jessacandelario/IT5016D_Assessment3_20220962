# IfStatementPractice5.py
# Author: Jessa Candelario
# Date: 26.10.22

# Learning Activity 34 : Challenge 5, cylinder
# Create 2 options : surface area or volume

import math  # to get the value of pi

option = input("If you would like to find out the surface area "
               "of the shape, enter 'Surface',\n"
               "If you would like to find the volume "
               "of the shape, enter 'Volume'\n")

if option.lower() != 'surface' and option.lower() != 'volume':
    print("You can only enter Surface or Volume\n")

else:
    length = int(input("Enter the length: "))
    radius = int(input("Enter the radius: "))

    if option.lower() == 'surface':
        print("The surface area is:",
              round((2 * math.pi * radius * length
                     + math.pi * radius ** 2), 2))

    if option.lower() == 'volume':
        print("The volume is: ",
              round((math.pi * radius ** 2 * length), 2))

# Test
'''
print("my assertions are:
      option = surface, length = 10, radius = 6, output = 490.09
      option = volume, length = 10, radius = 6, output = 1130.97
      option != volume or surface,
        output = 'You can only enter Surface or Volume"
'''
