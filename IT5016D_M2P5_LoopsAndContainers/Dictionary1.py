# Dictionary1.py
# Author: Jessa Candelario
# Date: 15.11.22

# Learning Activity 43: #2

# Challenge 1: Write a program that adds a stored dictionary item to a stored dictionary
# Challenge 2: Write a program that joins 2 stored dictionaries.
# Challenge 3: Write a program that outputs all the contents of a stored dictionary.
# Challenge 5: Write a program that removes a dictionary item from a stored dictionary.
# Challenge 6: Write a program that removes entries from a stored dictionary where the length of the key is 2.

# create stored dictionary
airport_code = {"HKG": "Hong Kong International Airport",
                "KUL": "Kuala Lumpur International Airport",
                "MNL": "Ninoy Aquino International Airport",
                "PEK": "Beijing International Airport",
                "HND": "Tokyo International Airport"}

# add items in dictionary
airport_code["SIN"] = "Singapore International Airport"

# print stored dictionary
print("Asia airport codes:")
for item in airport_code.items():
    print(item)

# create new stored dictionary
usa_airport_code = {"ORD": "O'Hare International Airport",
                    "LAX": "Los Angeles International Airport",
                    "DFW": "Dallas-Fort Worth International Airport",
                    "JFK": "John F. Kennedy International Airport",
                    "MIA": "Miami International Airport",
                    "DEN": "Denver International Airport,",
                    "KSFO": "San Francisco International Airport",
                    "KIAH": "George Bush International Airport"}

# print second stored dictionary
print("\nUSA airport codes:")
for item in usa_airport_code.items():
    print(item)

# join the 2 stored dictionary
airport_code.update(usa_airport_code)

# print joined dictionary
print("\nAirport Codes:")
for item in airport_code.items():
    print(item)

# delete an item in the stored dictionary
del(airport_code["MIA"])
print("\nDeleting some items..."
      "\nAirport Codes:")
for item in airport_code.items():
    print(item)

# I will delete the length of keys is 4 instead of 2 (Challenge 6)
# delete items with length of keys of 4
index_to_delete = []
for val in airport_code.keys():
    if 4 == len(val):
        index_to_delete.append(val)
for item in index_to_delete:
    del(airport_code[item])

print("\nIATA Airport Codes:")
for item in airport_code.items():
    print(item)