# NumericTypes.py
# Author: Jessa Candelario
# Date: 18.10.22

# Area of Circle
print("Area of Circle")
r = 6
pi = 3.1415926535897931
Area = pi*r**2  # ** meant 'raised to'

print("The radius of the circle is", r)
print("The area of the circle is", Area, "\n")  # \n means next line


# Variables
print("Variables")
x = 4
y = 7
z = 34.7
add = x+y+z
print(type(x))
print(type(y))
print(type(z))
print(add, "\n")

# Complex Number
print("Complex Number")
complex_number1 = 3+7j  # x+yj where x is real, y is imaginary
complex_number2 = 0+9j
print(complex_number1.real)
print(complex_number1.imag)
print(complex_number2.real)
print(complex_number2.imag)
print(type(complex_number1))

