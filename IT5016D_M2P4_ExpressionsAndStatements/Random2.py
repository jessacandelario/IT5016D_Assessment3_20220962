# Random2.py
# Author: Jessa Candelario
# Date: 27.10.22

# Learning Activity 36: Dice rolling

import random

print("Let's get the dice rolling!")
print(input("Press Enter to roll your dice!"))

# generate random numbers 1 - 6
dice1 = random.randint(1, 6)
dice2 = random.randrange(6) + 1
total = dice1 + dice2

print("You rolled a", dice1, "and a", dice2, "for a total of", total)
input("\n\nPress the enter key to exit.")