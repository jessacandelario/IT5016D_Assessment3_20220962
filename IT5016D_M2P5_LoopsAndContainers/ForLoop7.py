# ForLoop7.py
# Author: Jessa Candelario
# Date: 27.10.22

# Learning Activity 39: # 42: Calculate sum and average of integers

print("Input some integers to calculate their sum and average.\n"
      "Input 0 to exit.")

count = 0
total = 0.0
number = 1

while number != 0:
    number = int(input(""))
    total = total + number
    count += 1

if count == 0:
    print("Input some numbers")
else:
    print("Average = ", round(total / (count - 1), 2),
          "\nSum = ", total)
