# LoopPractice.py
# Author: Jessa Candelario
# Date: 27.10.22

# Learning Activity 38

print("Welcome to our figure calculator!\n")
print("This calculator helps you calculate the \n"
      "volume and/or the surface area of the given figure\n")

# given values
length = 10
width = 3
height = 8

option = False
chosen_option = str
choice = input("Enter 'volume' to calculate the volume,\n"
               "enter 'surface' to calculate the surface area\n")

while not option:  # instead of putting option == True
    if choice.lower() == 'surface':
        chosen_option = "surface"
        option = True
    elif choice.lower() == 'volume':
        chosen_option = "volume"
        option = True
    elif choice.lower() == 'exit':
        chosen_option = "exit"
        option = True
        print("Thank you for using the program.")
        quit()
    else:
        choice = input("Invalid option, please enter correct option.\n")

# Assume that the user will only enter integers
x = int
x_valid = False
y = int
y_valid = False

# prompt for value of x
# x should fall between 1 - 10 (figure length = 10)
x = int(input("\nPlease enter the value of x: \n"))
while not x_valid:  # instead of x-valid == True
    if 0 < x <= 10:
        x_valid = True
    else:
        x = int(input("Invalid number, please enter a new number:"))

# prompt for value of y
# y should fall between 1 - 8 (figure height = 8)
y = int(input("\nPlease enter the value of y: \n"))
while not y_valid:  # instead of y_valid == True
    if 0 < y <= 8:
        y_valid = True
    else:
        y = int(input("Invalid number, please enter a new number:"))

# calculate for Surface Area
if chosen_option == 'surface':
    surface = (length * height - x * y) * 2 \
              + (length * width - x * width) * 2 \
              + (height * width - y * width) * 2
    print("The surface area is", surface)

# calculate for Volume
if chosen_option == 'volume':
    volume = (length * width * height) \
             - (x * y * width)
    print("The volume is", volume)

# Test assertions
'''
print("My assertions are:"
      "chosen_option = 'volume', x = 10, y = 6, volume = 60"
      "chosen_option = 'surface', x = 10, y = 6, surface = 52"
      "chosen_option = 'exit', program ends")
'''
