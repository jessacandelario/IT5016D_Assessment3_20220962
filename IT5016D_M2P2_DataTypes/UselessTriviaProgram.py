# UselessTriviaProgram.py
# Author: Jessa Candelario
# Date: 20.10.22

# Learning Activity 25

# variable name as string
name = input("Hi,what is your name? ")

# variable age and weight as integer
age = int(input("How old are you? "))
weight = int(input("Ok, last question. How many kgs do you weigh? "))

# casting strings with string method
print("\nif poet ee cummings were to send you an email, he will address you as", name.lower())
# .lower() prints string in lowercase
print("But if ee was mad, he'd call you", name.upper())  # .upper() prints string in uppercase

# print the variable multiple times
print("\nIf a small child will try to get you attention")
print("your name will become:")
print(name * 5)

# compute age in seconds
# 1 year = 31536000 seconds
seconds_per_year = int(31536000)
print("\nYou are over", age * seconds_per_year, "seconds old.")

# compute weight on moon
# weight on moon is 16.5% of weight on Earth
print("\nDo you know that on the moon, you would only weigh", weight*0.165, "kgs?")

# compute weight on sun
# weight on sun is weight on Earth * 27.9307
print("On the sun, you would weigh", weight*27.9, "kgs.")
