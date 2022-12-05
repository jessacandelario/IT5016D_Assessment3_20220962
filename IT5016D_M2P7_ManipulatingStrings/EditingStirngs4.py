# EditingStrings3.py
# Author: Jessa Candelario
# Date: 22.11.22

# Learning Activity 51: Challenge 5: Here is a string template:
# "Welcome <first_name>. Thank you for joining <bank_name>. Your balance is $<balance>" Write a program that contains
# a stored container with 3 bank records. You must decide what container to use. The program must use the template
# string to display the text for all 3 customers.

accounts = [["Koko", "ANZ", 150], ["Penpen", "BNZ", 145], ["Potty", "ASB", 190]]

for count in range(0, len(accounts)):
    account_list = accounts[count]
    print(f"Welcome {account_list[0]}. Thank you for joining {account_list[1]}. Your balance is ${account_list[2]}")
