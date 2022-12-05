# SplittingStrings3.py
# Author: Jessa Candelario
# Date: 23.11.22

# Learning Activity 52

from random import shuffle

sentence = "The world is full of unsolved mysteries."

# split the sentence
split_sentence = sentence.split()

# Challenge 4: Write a program to get a string made of the first 2 and the last 2 words from a given a sentence.
# If the sentence contains less than 2 words, return instead the empty string.
if len(split_sentence) < 2:
    print(split_sentence)
else:
    list_1 = [split_sentence[0], split_sentence[1], split_sentence[-2], split_sentence[-1]]
    print(list_1, "\n")


# Challenge 6: Write a program to remove the nth word from a string containing words separated by spaces.
def remove_word(one_word):
    """Removes a word from the sentence"""
    print("Please enter a number between 1 and", len(split_sentence), "\n")
    x = int(input())
    split_sentence.pop(x-1)
    return split_sentence


print(remove_word(split_sentence), "\n")

# Challenge 3: Write a program that randomly jumbles the words in a stored sentence then displays the output.
# Research and use the Python shuffle function.
sentence_2 = sentence.split()
shuffle(sentence_2)
print(sentence_2, "\n")


# Challenge 5: Write a program that takes a list of words and returns the length of the longest one.
def longest_word(sentence_2):
    """Prints out the longest word in the sentence"""
    the_longest_word = ""
    for count in range(0, len(sentence_2)):
        if len(sentence_2[count]) > len(the_longest_word):
            the_longest_word = sentence_2[count]
    return the_longest_word


print(longest_word(sentence_2))
