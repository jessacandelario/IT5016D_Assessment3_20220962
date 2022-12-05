# SplittingStrings3.py
# Author: Jessa Candelario
# Date: 23.11.22

# Learning Activity 52
# Challenge 7: Write a program that accepts a comma separated sequence of words as input and prints the unique words.

words = input("Enter a series of words separated by comma\n")

split_words = words.split(",")  # .split divides the string

new_list = set(split_words)

print(new_list)


# Testing
'''
print("My assertion is:
      "input = hello, how, do, you, do"
      "output = ' how', ' do', 'hello', ' you'"
'''