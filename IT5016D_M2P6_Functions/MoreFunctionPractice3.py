# MoreFunctionPractice2.py
# Author: Jessa Candelario
# Date: 18.11.22

# Learning Activity 49: Challenge 5
# Write a program that maps a list of words into a list of integers representing the lengths of the corresponding words.


def word_length(fruits):
    """converts the words in fruits[] to their corresponding length"""
    for count in range(0, len(fruits)):
        number = len(fruits[count])
        lengths.append(number)


# create the list
fruits = ["apple", "orange", "banana", "strawberry", "watermelon"]
lengths = []

word_length(fruits)
print(lengths)


# Testing
'''
print("My assertion is:"
      "fruits = ["apple", "orange", "banana", "strawberry", "watermelon"]"
      "length = [5, 6, 6, 10, 10]")
'''