# IfStatementPractice4.py
# Author: Jessa Candelario
# Date: 26.10.22

# Learning Activity 34 : Challenge 4: cube
# Create 2 options : surface area or volume

option = input("If you would like to find out the surface area "
               "of the shape, enter 'Surface',\n"
               "If you would like to find the volume "
               "of the shape, enter 'Volume'\n")

if option.lower() != 'surface' and option.lower() != 'volume':
    print("You can only enter Surface or Volume\n")

else:
    length = int(input("Enter the length: "))
    width = int(input("Enter the width: "))
    height = int(input("Enter the height: "))

    if option.lower() == 'surface':
        print("The surface area is:",
              length * width * 2
              + length * height * 2
              + width * height * 2)

    if option.lower() == 'volume':
        print("The volume is: ",
              length * width * height)

# Test
'''
print("my assertions are:
      option = surface, length = 12, width = 10,
        height = 5, output = 460
      option = volume, length = 12, width = 10,
        height = 5, output = 600
      option != volume or surface,
        output = 'You can only enter Surface or Volume"
'''


