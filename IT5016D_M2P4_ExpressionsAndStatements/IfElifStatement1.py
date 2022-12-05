# IfElifStatement1.py
# Author: Jessa Candelario
# Date: 26.10.22

# Learning Activity 35 : Challenge 1: Richter Scale

print("The Richter scale")

magnitude = float(input("Please enter the magnitude of earthquake: "))

if magnitude < 2.0:
    print("A magnitude", magnitude, "earthquake "
          "is considered to be a Micro earthquake")

elif 3.0 > magnitude >= 2.0:
    print("A magnitude", magnitude, "earthquake "
          "is considered to be a Very minor earthquake")

elif 4.0 > magnitude >= 3.0:
    print("A magnitude", magnitude, "earthquake "
          "is considered to be a Minor earthquake")

elif 5.0 > magnitude >= 4.0:
    print("A magnitude", magnitude, "earthquake "
          "is considered to be a Light earthquake")

elif 6.0 > magnitude >= 5.0:
    print("A magnitude", magnitude, "earthquake "
          "is considered to be a Moderate earthquake")

elif 7.0 > magnitude >= 6.0:
    print("A magnitude", magnitude, "earthquake "
          "is considered to be a Strong earthquake")

elif 8.0 > magnitude >= 7.0:
    print("A magnitude", magnitude, "earthquake "
          "is considered to be a Major earthquake")

elif 10.0 > magnitude >= 8.0:
    print("A magnitude", magnitude, "earthquake "
          "is considered to be a Great earthquake")

elif magnitude >= 10.0:
    print("A magnitude", magnitude, "earthquake "
          "is considered to be a Meteoric earthquake")

# Test assertions
'''
print("My assertions are:"
      "magnitude = 2.1, output = Very minor,"
      "magnitude = 6.8, output = Strong"
'''