# SearchingStrings1.py
# Author: Jessa Candelario
# Date: 20.11.22

# Learning Activity 50

string_1 = "The first rule of fight club is: do not talk about fight club."

# Challenge 1: Write a program that returns the number of spaces in the string.
print("\nThe number of spaces in the string is:{0}".format(string_1.count(" ")))

# Challenge 2: Write a program that returns the total number of punctuations (full stops and colons) used
print("\nThe number of punctuations used is: {0}".format(string_1.count(".")+(string_1.count(":"))))

# Challenge 3: Write a program that gets user input and determines whether the text matches the start of the string.
first_word = input("\nCan you guess the first word in the stored string?\n")
print("Does this string start with the given text?....{0}\n"
      .format(string_1.startswith(first_word.title())))

# Challenge 4: Write a program that gets user input and determines whether the text matches the start or the end of
# the string.
guess_word = input("Please enter a word:")
print("Does this string start with the given text?....{0}\n"
      .format(string_1.startswith(guess_word.title())))
print("Does this string end with the given text?....{0}\n"
      .format(string_1.endswith(guess_word)))

# Challenge 5: Write a program that returns the index position of the first instance of the text "fight".
print("The index position of fight is {0}\n"
      .format(string_1.find("fight")))

# Challenge 6: Write a program that returns the position of the instance of the text "fight"
# that appears after the colon.
string_1_colon_index = string_1.find(":")
fight_position = string_1.find("fight", string_1_colon_index, len(string_1))
print("\nFinding the word fight, anytime after :...\n\n"
      "The word fight appears at index position..{0}"
      .format(fight_position))

# Testing
'''
print("My assertion is:"
      "Challenge 1 = 12"
      "Challenge 2 = 2"
      "Challenge 3: input = t, output = true; input = a, output = false"
      "Challenge 4: input = The, output = first word - true, last word - false
                    input = club., output = first word - false, last word - true"
      "Challenge 5: 18"
      "Challenge 6: 51"
'''