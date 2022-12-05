# Tuple1.py
# Author: Jessa Candelario
# Date: 14.11.22

# Learning Activity 42: #1

# Hero's Inventory
# Demonstrates tuple creation

inventory = ()  # create an empty tuple

# treat the tuple as a condition
if not inventory:
    print("You are empty-handed.")

input("\nPress the enter key to continue.")

# create a tuple with some items
inventory = ("sword",
             "armor",
             "shield",
             "healing potion")

# print the tuple
print("\nThe tuple inventory is:", inventory)

# print each element in the tuple
print("\nYour items:")

for item in inventory:  # for loop to print each item in the tuple
    print(item)

input("\n\nPress the enter key to exit.")
