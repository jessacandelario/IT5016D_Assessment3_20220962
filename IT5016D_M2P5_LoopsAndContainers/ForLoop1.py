# ForLoop1.py
# Author: Jessa Candelario
# Date: 27.10.22

# Learning Activity 39: #1: Numbers divisible by 7 and multiple of 5 between 1500 and 2700

for i in range(1500, 2701, 5):
    if i % 7 == 0:
        print(i, ",", end="")

