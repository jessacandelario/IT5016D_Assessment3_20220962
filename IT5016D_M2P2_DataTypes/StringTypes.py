# StringTypes.py
# Author: Jessa Candelario
# Date: 18.10.22

my_int = 7
print(my_int)

my_float = 7.0
print(my_float)
my_float = float(7)
print(my_float)

my_string = 'hello'
print(my_string)
my_string = "hello"
print(my_string)

my_string = "Don't worry about apostrophes"
print(my_string)

one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

a, b = 3, 4  # same as a = 3, b = 4
print(a, b)

my_string = "hello"
my_float = 10.0
my_int = 20
if my_string == "hello":
    print("String: %s" % my_string)
if isinstance(my_float, float) and my_float == 10.0:
    print("Float: %f" % my_float)
if isinstance(my_int, int) and my_int == 20:
    print("Integer: %d" % my_int)

# Learning Activity 18: New Zealand Anthem
quote = "God Defend New Zealand"
print("\nIn swap case:")
print(quote.swapcase())
