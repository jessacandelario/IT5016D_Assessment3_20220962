# IfStatementPractice6.py
# Author: Jessa Candelario
# Date: 26.10.22

# Learning Activity 34 : Challenge 6, pyramid
# Create 2 options : surface area or volume

option = input("If you would like to find out the surface area "
               "of the shape, enter 'Surface',\n"
               "If you would like to find the volume "
               "of the shape, enter 'Volume'\n")

if option.lower() != 'surface' and option.lower() != 'volume':
    print("You can only enter Surface or Volume\n")

else:
    base = int(input("Enter the base: "))
    height = int(input("Enter the height: "))

    if option.lower() == 'surface':
        print("The surface area is:",
              base / 2 * height * 4 + base ** 2)

    if option.lower() == 'volume':
        print("The volume is: ",
              base ** 2 * height / 3)

# Test
'''
print("my assertions are:
      option = surface, base = 9, height = 4, output = 153
      option = volume, base = 9, height = 4, output = 108
      option != volume or surface,
        output = 'You can only enter Surface or Volume"
'''