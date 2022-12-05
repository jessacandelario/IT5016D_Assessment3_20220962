# ForLoop2.py
# Author: Jessa Candelario
# Date: 27.10.22

# Learning Activity 39: #3
# Guess a number between 1 - 9

import random

number = random.randint(1, 10)
guess = 0

while number != guess:
    guess = int(input("Guess a number between 1 and 10: "))

print("Well guessed!")

