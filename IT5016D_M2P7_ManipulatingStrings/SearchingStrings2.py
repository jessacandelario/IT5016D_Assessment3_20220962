# SearchingStrings2.py
# Author: Jessa Candelario
# Date: 20.11.22

# Learning Activity 50: Challenge 7
# Write a program that gets a username from a stored email address.
# The email address should be a person's first name, followed by a dot, followed by their last name.
# The username should be the person's last name followed by their first initial. Here is an example test case assertion:
# "robert.paulson@hotmail.com" produces the username "paulsonr"

email = "robert.paulson@hotmail.com"
dot_index = email.find(".")  # .find to search through the string
at_index = email.find("@")
user_surname = email[dot_index + 1:at_index]
username = user_surname + email[0]

print(username)

# Testing
'''
print("My assertion is:"
      "output = paulsonr"
'''
