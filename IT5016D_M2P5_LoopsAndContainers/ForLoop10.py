# ForLoop10.py
# Author: Jessa Candelario
# Date: 27.10.22

# Learning Activity 39: # 22: Print letter "M"

letter = ""

for row in range(0, 7):
    for column in range(0, 7):
        if (column == 1
                or column == 5
                or (row == 2 and (column == 2 or column == 4))
                or (row == 3 and column == 3)):
            letter = letter + "*"
        else:
            letter = letter + " "
    letter = letter + "\n"

print(letter)
