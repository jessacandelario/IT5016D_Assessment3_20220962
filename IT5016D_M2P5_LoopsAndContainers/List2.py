# List2.py
# Author: Jessa Candelario
# Date: 01.11.22

# Learning Activity 40 : #1 Task 2: Create a list containing the days of the week in Maori, print 2nd and 5th days
# Print the day of the week 3 days from the end of the week

Maori_days = ["Rāhina", "Rātū", "Rāapa", "Rāpare", "Rāmere", "Rāhoroi", "Rātapu"]

print(Maori_days[1], end=" ")  # end= changes the end of the print() statement instead of the default new line
print(Maori_days[4], end=" ")  # by putting end=" " at the end of the print statements, the list items are printed on
print(Maori_days[-3], end=" ")  # the same line rather than on separate new lines

# Test assertions:
'''
print("my assertions are"
      "output = Rātū Rāmere Rāmere")
'''

