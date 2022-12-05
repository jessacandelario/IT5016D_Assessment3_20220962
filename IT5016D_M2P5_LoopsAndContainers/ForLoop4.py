# ForLoop4.py
# Author: Jessa Candelario
# Date: 27.10.22

# Learning Activity 39: # 10: Iterated integers from 1 to 50, multiples of 3 = "Fizz", multiples of 5 = "Buzz"
# multiples of both 3 and 5 = "FizzBuzz"

for i in range(50):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        continue
    elif i % 3 == 0:
        print("Fizz")
        continue
    elif i % 5 == 0:
        print("Buzz")
        continue
    print(i)

