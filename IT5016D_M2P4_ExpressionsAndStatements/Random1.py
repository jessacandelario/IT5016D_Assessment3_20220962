# Random1.py
# Author: Jessa Candelario
# Date: 27.10.22

# Learning Activity 36: Guess My Number Game

import random

print("\t\tWelcome to 'Guess My Number'!\n")

print("I am thinking of a number between 1 and 100.\n"
      "Try to guess it in as few attempts as possible.\n")

# set the values
number = random.randint(1, 100)
guess = int(input("Take a guess:"))
attempt = 1

# guess loop
while guess != number:
    if guess > number:
        print("Lower...")
    else:
        print("Higher...")

    guess = int(input("Take a guess:"))
    attempt += 1

print("\nCongratulations! You got it right! The number was", number)
print("It took you", attempt, "tries")


