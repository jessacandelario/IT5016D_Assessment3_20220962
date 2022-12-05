# WhileLoop4.py
# Author: Jessa Candelario
# Date: 27.10.22

# Learning Activity 37
# Challenge 4: Password program

password = input("Enter Password: \n")
stored_password = "welcome"
counter = 0
correct = False

while not correct and counter < 2:
    if password == stored_password:
        print("Correct password")
        correct = True
    elif password == "Exit" or password == "exit":
        print("Program Terminated")
        correct = True
    else:
        print("Incorrect password, please try again\n")
        password = input("Enter Password")
        counter += 1

if counter == 2:
    print("Sorry, you have used up all your attempts")

# Test assertions
'''
print("My assertions are"
    "password = welcome, output = Correct Password"
    "password = Exit, output = Program terminated"
    "password = try, output = gives attempts 
    until correct password entered or attempts maxed")
'''
