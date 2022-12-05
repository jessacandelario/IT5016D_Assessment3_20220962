# ForLoop5.py
# Author: Jessa Candelario
# Date: 27.10.22

# Learning Activity 39: # 31: Calculate dog age in dog years

human_age = int(input("Input dog's age in human years: "))

if human_age < 0:
    print("Please enter a positive number")
elif human_age <= 2:
    dog_age = human_age * 10.5
elif human_age > 2:
    dog_age = 21 + (human_age - 2) * 4

print("The dog's age in dog's years is", dog_age)


