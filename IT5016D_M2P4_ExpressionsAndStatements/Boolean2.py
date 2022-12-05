# Boolean2.py
# Author: Jessa Candelario
# Date: 24.10.22

# Learning Activity 31 : Challenge 2: Shopping cart feature

print("Welcome to our webstore!\n",
      "Customers without account can use Guest login.")

# Let user input details
name = input("Please enter your name:\n")
cart = int(input("How many items in your cart?:"))
registered = True
not_registered = False

# Test assertions
print("Eligibility of", name, "to proceed with payment:",
      cart > 0
      and registered,
      "\n")
