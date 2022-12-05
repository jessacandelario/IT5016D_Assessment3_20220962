# EditingStrings3.py
# Author: Jessa Candelario
# Date: 22.11.22

# Learning Activity 51
# Challenge 4: Write a program that randomly picks a character from a stored string and then places that character
# between every character in the string.

from random import randint

stored_string = "Welcome to the program"
letter = randint(0, len(stored_string))
random_letter = stored_string[letter]

print("Inserting a random letter into the sentence...\n{0}".format(random_letter.join(stored_string)))


# Testing
'''
print("My assertion is:"
      "string = Welcome to the program, 
      "output = Wpeplpcpopmpep ptpop ptphpep ppprpopgprpapm")
'''