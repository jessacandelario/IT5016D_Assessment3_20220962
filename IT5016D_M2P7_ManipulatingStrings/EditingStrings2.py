# EditingStrings2.py
# Author: Jessa Candelario
# Date: 22.11.22

# Learning Activity 51
# Challenge 2: Write a program that accepts a user input sentence and then replaces all the spaces with dashes
# before displaying the output to screen.

sentence = input("Please enter a sentence: \n")

print("Replacing spaces with dash...\n{0}".format(sentence.replace(" ","-")))

# Challenge 3: Write a program that reverses the letters in a stored string.
print("Reversing the sentence...\n{0}".format(''.join(reversed(sentence))))


# Testing
'''
print("My assertion is:"
      "input = I love you; output = I-love-you , uoy evol i"
      "input = Hello there; output = Hello-there , ereht olleh"
'''