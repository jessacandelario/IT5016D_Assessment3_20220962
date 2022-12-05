# List6.py
# Author: Jessa Candelario
# Date: 07.11.22

# Learning Activity 40 : #2
# Challenge 8: randomly selects 2 different integers from List_2

import random

list_2 = [1, 19, 4, 8]

item_1 = random.choice(list_2)
item_2 = random.choice(list_2)

while item_1 == item_2:
    item_2 = random.choice(list_2)

print(item_1, item_2)