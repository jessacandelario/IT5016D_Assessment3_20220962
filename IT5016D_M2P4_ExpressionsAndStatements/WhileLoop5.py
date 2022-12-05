# WhileLoop5.py
# Author: Jessa Candelario
# Date: 27.10.22

# Learning Activity 37 : Challenge 5
# Guessing game

import random

print("\t\tWelcome to 'Guess My Number'!\n")

print("I am thinking of a number between 1 and 100.\n"
      "Try to guess it in as few attempts as possible.\n")

# set the values
secret_number = random.randint(1, 100)
guess = int(input("Take a guess:"))
last_guess = int
attempt = 0
found = False

# guess loop
while not found:
    if guess > secret_number:
        print("Lower...")
        if last_guess != guess:
            attempt += 1
        last_guess = guess
        guess = int(input("Take a guess:"))
    elif guess < secret_number:
        print("Higher...")
        if last_guess != guess:
            attempt += 1
        last_guess = guess
        guess = int(input("Take a guess:"))
    else:
        attempt += 1
        found = True

print("\nCongratulations! You got it right! The number was", secret_number)
print("It took you", attempt, "tries")
