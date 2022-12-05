# SleepCalculator.py
# Author: Jessa Candelario
# Date: 19.10.22

print("Welcome to your sleep calculator\n")
user_name = input("Please enter your name...\n")
user_yob = int(input("Please enter your year of birth...\n"))
age = 2022 - user_yob
sleep_per_year = 365 * 7  # assuming 7hrs sleep per day

print("Thank you for your input\n")
print("Your name is", user_name)
print("You are now", age, "years old.")
print("You have slept for a total of", age * sleep_per_year, "hours.")
