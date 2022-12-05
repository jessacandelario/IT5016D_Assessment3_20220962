# List3.py
# Author: Jessa Candelario
# Date: 01.11.22

# Learning Activity 40 : #2
# Challenge 1: Display first 2 lists, prompt for either sum or average

list_1 = [23, 66, 23, 12]
list_2 = [1, 19, 4, 8]

list_sum = (sum(list_1) + sum(list_2))
average = list_sum / (len(list_1) + len(list_2))

choice = input("Please choose between sum or average: \n")
answer = choice.lower()

while answer != "sum" or "average":
    if choice.lower() == "sum":
        print("The sum is:", list_sum)
        break

    elif choice.lower() == "average":
        print("The average is:", average)
        break

    else:
        choice = input("Please choose between sum or average: \n")

# Test assertions:
'''
print("my assertions are:
      "choice = sum, output = 156
      "choice = average, output = 19.5")
'''