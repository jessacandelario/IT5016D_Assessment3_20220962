# IfElifStatement1.py
# Author: Jessa Candelario
# Date: 26.10.22

# Learning Activity 35 : Challenge 3: Alphabet

letter = input("Enter a letter from the Alphabet: ")

if letter.lower() == ('a' or 'e' or 'i' or 'o' or 'u'):
    print("Letter", letter.upper(), "is a vowel letter.")

elif letter.lower() == 'y':
    print("Letter", letter.upper(), "is sometimes a vowel letter, "
          "and sometimes a consonant letter." )

else:
    print("Letter", letter.upper(), "is is consonant letter.")

# Test assertions
'''
print("My assertions are:"
      "letter = a, output = vowel"
      "letter = b, output = consonant"
'''