# Tuple5.py
# Author: Jessa Candelario
# Date: 14.11.22

# Learning Activity 42: #3

# Challenge 1: Write a program to create a tuple.
print("Challenge 1:")

tuple_1 = (1, 2, 3, 4, 5)
print(tuple_1, "\n")


# Challenge 2: Write a program to create a tuple with different data types.
print("\nChallenge 2:")

tuple_2 = ("Jessa", 31, "F", 50.1)
print(tuple_2, "\n")


# Challenge 3: Write a program to create a tuple with 5 numbers. Print the 3rd number.
print("\nChallenge 3:")

tuple_3 = (2, 4, 6, 8, 10)
print("The third number is:", tuple_3[2], "\n")


# Challenge 4: Write a program to create a tuple with 3 strings. Write code that extracts each element into a
# separate variable.
print("\nChallenge 4:")

tuple_4 = ("Chicken", "Beef", "Pork")
# assign elements into separate variables
meat_1 = tuple_4[0]
meat_2 = tuple_4[1]
meat_3 = tuple_4[2]
# print variables
print("", meat_1, "\n", meat_2, "\n", meat_3, "\n")


# Challenge 5: Write a program to create a 6 element integer tuple. Write code that prints the 4th element and the
# 4th from last elements.
print("\nChallenge 5:")

tuple_5 = (1, 2, 3, 4, 5, 6)
# 4th element
print("The 4th number is:", tuple_5[3])
# 4th from the last element
print("The 4th number from the end is:", tuple_5[-4], "\n")


# Challenge 6: Write a program that prints the repeated items of a tuple. It should print the item just once
# regardless of how many duplicates exist.
print("\nChallenge 6:")

tuple_6 = (5, 10, 15, 15, 20, 25, 25, 25, 30)

# create empty list for repeated number
repeated_number = []

# for loop to find out the repeating numbers
for counter in range (0,len(tuple_6)):
    for number in range(counter+1, len(tuple_6)):
        if tuple_6[counter] == tuple_6[number]:
            # add the repeated number to the empty list
            repeated_number.append(tuple_6[number])
individual_number = set(repeated_number)
print("The numbers that repeat are:", individual_number, "\n")


# Challenge 7: Write a program that displays a tuple and asks the user to type a value that is contained in the
# tuple. The program should say whether the tuple contains the entered value. If the tuple contains duplicates of the
# value, it should say that as well.
print("\nChallenge 7:")

items = (2, 10, 2, 15, 20, 10, 25, 30, 35, 40)
found = 0

number = int(input("Enter the value you wish to search for\n"))

for counter in range (0,len(items)):
    if items[counter] == number:
        found += 1
if found == 0:
    print("The number was not in the tuple")
elif found == 1:
    print("The number was in the tuple once")
else:
    print("The number was in the tuple more than once")

# Testing
'''
Challenge 1: output = (1, 2, 3, 4, 5) 
Challenge 2: output = ('Jessa', 31, 'F', 50.1) 
Challenge 3: output = The third number is: 6 
Challenge 4: output = Chicken, Beef, Pork
Challenge 5: output = The 4th number is: 4
                      The 4th number from the end is: 3 
Challenge 6: output = The numbers that repeat are: {25, 15} 
Challenge 7: input = 2, output = The number was in the tuple more than once
             input = 15, output = The number was in the tuple once
             input = 3, output = The number was not in the tuple
'''