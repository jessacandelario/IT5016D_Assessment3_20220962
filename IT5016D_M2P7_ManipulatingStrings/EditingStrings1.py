# EditingStrings1.py
# Author: Jessa Candelario
# Date: 22.11.22

# Learning Activity 51
# Challenge 1:Write a program that produces the following output:
# Please enter your class size: 3
# Please enter student 1 name: Beyonce
# Please enter student 2 name: Michelle
# Please enter student 3 name: Kelly
# Thank you, the names of your students in swapped case are: bEYONCE, kELLY, mICHELLE

class_size = int(input("\nPlease enter your class size:"))
students = []

for count in range (0, class_size):
    name = input("Please enter student {0} name:".format(count+1))
    students.append(name)

string_students = ",".join(students)
print("Thank you, the names of your students in swapped case are:\n{0}".format(string_students.swapcase()))


# Testing
'''
print("My assertion is:"
      "input = 3, Joy, Dan, Ann; output = jOY, dAN, aNN"
      "input = 2, Samuel, Manny; output = sAMUEL, mANNY"
'''