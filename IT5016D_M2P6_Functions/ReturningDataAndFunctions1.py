# ReturningDataAndFunctions1.py
# Author: Jessa Candelario
# Date: 16.11.22

# Learning Activity 47: Challenge 1
# Write a short 2 question quiz that uses a function to evaluate each answer and return a score.

# crete introduction for the program
print("\nWelcome to the quiz!"
      "\nThis quiz will have 2 questions."
      "\nCan you get both correctly?")


# create a function for the questions
def quiz(question, answer, score):
    print(question)
    user_answer = input("Your answer is:")
    if user_answer == answer:
        score += 1
        print("Correct answer, you get a point!")
    else:
        print("Sorry, wrong answer!")
    return score


# call the function for the first question
score = quiz("\nHow many legs does an elephant have?", "4", 0)

# call the function for the second question
score = quiz("\nHow many colors are there in a rainbow?", "7", score)

# print the score
print("\nYour score is:", score)

# Testing
'''
print("My assertion are:"
      "answer 1 = 4, answer 2 = 7, score = 2"
      "answer 1 = 4, answer 2 = 5, score = 1"
'''