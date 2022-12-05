# ForLoop9.py
# Author: Jessa Candelario
# Date: 27.10.22

# Learning Activity 39: # 21: Print letter "L"

letter = ""

for row in range(0, 7):
    for column in range(0, 7):
        if (column == 1
                or (row == 6 and column != 0 and column < 6)):
            letter = letter + "*"
        else:
            letter = letter + " "
    letter = letter + "\n"

print(letter)
