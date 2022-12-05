# ForLoop12.py
# Author: Jessa Candelario
# Date: 27.10.22

# Learning Activity 39: # 30: Print letter "Z"

letter = ""

for row in range(0, 7):
    for column in range(0, 7):
        if (row == 0
                or row == 6
                or (column == 5 and row == 1)
                or (column == 4 and row == 2)
                or (column == 3 and row == 3)
                or (column == 2 and row == 4)
                or (column == 1 and row == 5)):
            letter = letter + "*"
        else:
            letter = letter + " "
    letter = letter + "\n"

print(letter)
