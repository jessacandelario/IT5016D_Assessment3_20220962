# Fibonacci.py
# Author: Jessa Candelario
# Date: 27.10.22

# Fibonacci sequence in While loop, code from "Fibonacci Using While", edited and added comments

print("\nThe Fibonacci Sequence:\n")

position = 0  # this is the position in the series
while int(position) < 3:
    position = input("Please enter a number corresponding to the position in the sequence (should be at least 3): ")

term = 0  # this is the amount of numbers to be printed
while term <= 0:
    term = int(input("Please enter number of terms to generate (should be a positive integer): \n"))

print("\n", term, "numbers in the sequence starting from term \n", position, ":")

# convert position and term to integers
position = int(position)
term = int(term)

# initialise term counters to zero
position_counter = 2
term_counter = 0

# initialise the first two terms in the sequence
n1 = 0
n2 = 1

while term_counter < term:

    nth = n1 + n2  # 3rd number = 1st number + 2nd number
    n1 = n2  # 1st number becomes 2nd number
    n2 = nth  # 2nd number becomes 3rd number
    position_counter += 1
    if position_counter >= position:
        term_counter += 1
        if term_counter < term:
            print(nth, end=", ")
        else:
            print(nth)
