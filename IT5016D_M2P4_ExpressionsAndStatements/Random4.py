# Random3.py
# Author: Jessa Candelario
# Date: 27.10.22

# Learning Activity 36: Mood Computer

import random

print("I sense your energy."
      "Your true emotions are coming across my screen.\n")
print("You are...")

mood = random.randint(1, 3)

if mood == 1:
    print("""
    -----------
     |       |
     | O   O |
     |   <   |
     |       |
     |  . .  |
     | `...` |
    -----------
    """)
elif mood == 2:
    print("""
    -----------
     |        |
     | O   O  |
     |   <    |
     |        |
     | ------ |
     |        |
    -----------
     """)
elif mood == 3:
    print("""
    -----------
     |        |
     | O   O  |
     |   <    |
     |        |
     |   .'.  |
     |  '   ' |
    -----------
        """)
else:
    print("Illegal mood value! (You must be in a really bad mood).")

print("...today.")

input("\n\nPress the enter key to exit.")