# Dictionary3.py
# Author: Jessa Candelario
# Date: 15.11.22

# Learning Activity 44: #2: Creating a login program

print("\nWelcome to your login portal\n")

# create stored login
login = {"Penpen": "12345",
         "Koko": "abcde",
         "Sulley": "abc123"}

print("You have three allowed attempts to enter your login details")

# use while loop for 3 attempts
attempt = 0
while attempt < 3:
    user_name = input("Please enter your username:\n").title()
    password = input("Please enter your password:\n")
    correct = False
    # use for loop to check each item
    for key, value in login.items():
        if key == user_name and value == password:
            correct = True
            attempt = 3
            print("Login successful")
            break
    attempt += 1
    if not correct:
        # check the number of attempts used
        if attempt < 3:
            print("Incorrect username or password, please try again.\n")
            attempt += 1
        else:
            print("Sorry, that was your third attempt.")
    else:
        break
