# IfStatement2.py
# Author: Jessa Candelario
# Date: 26.10.22

# Learning Activity 33 : Challenge 2
# 5 Trivia about New Zealand

# import time to be able to calculate total time taken
import time

start_time = time.time()  # assign variable for start time
score_counter = 0  # assign value for score counter

print("Welcome to New Zealand Trivia!\n")

# Trivia question 1
print("Trivia Question 1: Answer with Yes or No\n"
      "Are there snakes in New Zealand?")
trivia_1 = input("Your answer is:")
answer_1 = trivia_1.lower()
if answer_1 == "no":
    print("Correct!\n")
    score_counter += 1
elif answer_1 == "yes":
    print("Sorry, wrong answer!\n"
          "There are no snakes in New Zealand\n")
else:
    print("Sorry, that is not in the options")

input("Press enter for the next question\n")

# Trivia question 2
print("Trivia Question 2: Choose the correct answer\n"
      "What is the capital of New Zealand\n"
      "A. Auckland\n"
      "B. Wellington\n"
      "C. Queenstown")
trivia_2 = input("Your answer is:")
answer_2 = trivia_2.lower()
if answer_2 == "b":
    print("Correct!\n")
    score_counter += 1
elif answer_2 == ("a" or "c"):
    print("Sorry, wrong answer!\n"
          "Wellington in the capital of New Zealand\n")
else:
    print("Sorry, that's not in the options.\n"
          "Wellington in the capital of New Zealand\n")

input("Press enter for the next question\n")

# Trivia question 3
print("Trivia Question 3: Choose the correct answer\n"
      "What is by far the most famous sport in New Zealand?\n"
      "A. Soccer\n"
      "B. Basketball\n"
      "C. Rugby")
trivia_3 = input("Your answer is:")
answer_3 = trivia_3.lower()
if answer_3 == "c":
    print("Correct!\n")
    score_counter += 1
elif answer_3 == ("a" or "b"):
    print("Sorry, wrong answer!\n"
          "Rugby is the correct answer\n")
else:
    print("Sorry, that's not in the options.\n"
          "Rugby is the correct answer\n")

input("Press enter for the next question\n")

# Trivia question 4
print("Trivia Question 4: Choose the BEST answer\n"
      "What is a Kiwi?\n"
      "A. Person\n"
      "B. Bird\n"
      "C. Fruit\n"
      "D. All of the above")
trivia_4 = input("Your answer is: ")
answer_4 = trivia_4.lower()
if answer_4 == "d":
    print("Correct!\n")
    score_counter += 1
elif answer_4 == ("a" or "b" or "c"):
    print("Sorry, it's all of them,\n"
          "In New Zealand, all three choices are considered correct\n"
          "We call locals as Kiwi\n"
          "We have a bird specie that is called Kiwi\n"
          "and we have a Kiwi fruit\n")
else:
    print("Sorry, that is not in the options.\n"
          "In New Zealand, all three choices are considered correct\n"
          "We call locals as Kiwi\n"
          "We have a bird specie that is called Kiwi\n"
          "and we have a Kiwi fruit\n")

input("Press enter for the next question\n")

# Trivia question 5
print("Trivia Question 5: Type in the correct answer"
      "What is the Maori name of New Zealand")
trivia_5 = input("Your answer is:")
answer_5 = trivia_5.lower()
if answer_5 == "aotearoa":
    print("Correct!\n"
          "It means 'Land of the Long White Cloud'\n")
    score_counter += 1
else:
    print("Sorry, that is not the right answer.\n"
          "The correct answer is Aotearoa\n"
          "It means 'Land of the Long White Cloud'\n")

# assign variable for end time
end_time = time.time()

input("Press enter to know your score\n")

# print score
print("Your score is:", score_counter, "out of 5")
if score_counter == 5:
    print("Good job!")
elif 0 < score_counter < 5:
    print("Not bad!")
else:
    print("Oh no!")

# print total time taken
print("Total time:", round((end_time - start_time),2), "seconds")