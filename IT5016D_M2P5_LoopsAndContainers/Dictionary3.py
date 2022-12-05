# Dictionary3.py
# Author: Jessa Candelario
# Date: 15.11.22

# Learning Activity 44: #1: Creating morse code encoder

print("\nWelcome to Morse Code encoder!\n")

# copy morse code dictionary from MorseCode.py
morse = {"A": ".-",
         "B": "-...",
         "C": "-.-.",
         "D": "-..",
         "E": ".",
         "F": "..-.",
         "G": "--.",
         "H": "....",
         "I": "..",
         "J": ".---",
         "K": "-.-",
         "L": ".-..",
         "M": "--",
         "N": "-.",
         "O": "---",
         "P": ".--.",
         "Q": "--.-",
         "R": ".-.",
         "S": "...",
         "T": "-",
         "U": "..-",
         "V": "...-",
         "W": ".--",
         "X": "-..-",
         "Y": "-.--",
         "Z": "--..",
         "0": "-----",
         "1": ".----",
         "2": "..---",
         "3": "...--",
         "4": "....-",
         "5": ".....",
         "6": "-....",
         "7": "--...",
         "8": "---..",
         "9": "----.",
         ".": ".-.-.-",
         ",": "--..--"}

# let user input a word, use .upper() since all the keys are in uppercase
word = input("Please enter a string:").upper()

# create an empty string for the code
morse_code = ""

# use for loop to convert each letter in the string into morse code
for key in word:
    morse_code += morse[key]  # add each letter
    morse_code += " "  # add space between each letter

# print the result
print("The Morse Code for", word, "is\n",
      morse_code)

# Test assertions
'''
print("My assertions are"
    "input = hello, output = .... . .-.. .-.. ---"
    "input = good, output = --. --- --- -.."
    "input = eat, output = . .- -")
'''