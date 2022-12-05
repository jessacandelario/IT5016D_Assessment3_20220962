# IfStatementPractice1.py
# Author: Jessa Candelario
# Date: 26.10.22

# Learning Activity 34 : Challenge 1: Identify the color of the tile on the board

# black tiles = row letter value of 1
row_letter = 1

# ask user to input row choice
row_choice = input("Enter the row letter of the square:\n")
# white tiles = row letter value of 2
if row_choice == ("b" or "d" or "f" or "h"):
    row_letter = 2

# ask user to input column of choice
column_choice = int(input("Enter the column number on the square:\n"))

# convert row and column to odd or even numbers
coordinate = column_choice + row_letter

# even numbers = black tiles
# odd numbers = white tiles
if coordinate % 2 == 0:
    print("The tile is black")
else:
    print("The tile is white")

# test assertions
'''
print("My assertions are:"
      "row_choice = c, column_choice = 3, output = black"
      "row-choice = g, column_choice = 4, output = white"
'''