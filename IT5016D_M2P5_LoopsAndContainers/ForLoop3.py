# ForLoop3.py
# Author: Jessa Candelario
# Date: 27.10.22

# Learning Activity 39: # 8: Print all numbers from 0 to 6 except 3 and 6

for i in range(6):
    if i == 3 or i == 6:
        continue
    print(i, end=",")