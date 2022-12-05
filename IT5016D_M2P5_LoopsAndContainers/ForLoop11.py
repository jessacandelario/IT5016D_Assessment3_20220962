# ForLoop11.py
# Author: Jessa Candelario
# Date: 27.10.22

# Learning Activity 39: # 27: Print letter "T"

letter = ""

for row in range(0, 7):
    for column in range(0, 7):
        if (column == 3
                or (row == 0 and column != 0 and column < 6)):
            letter = letter + "*"
        else:
            letter = letter + " "
    letter = letter + "\n"

print(letter)
