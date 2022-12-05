# GameOver.py
# Author: Jessa Candelario
# Date: 20.10.22

# Learning Activity 25: enter the GameOver code and try to run it

# use double quote to bookend the string, so you can put single quote in within the string
print("Program 'Game Over' 2.0")

# example of printing multiple values in one string
print("Same", "message", "as before")

# break the code to make the multiple lines, to make it easier to read
print("Just",
      "a bit",
      "bigger")  # this will print the same as print("Just", "a bit", "bigger")

# end="" means the next print line would print there
print("Here", end=" ")
print("it is...")  # these 2 lines can also be written as print("Here it is...")

# triple quote string can span to multiple lines prints exactly what you type in
print(
    """
     _____       ___       ___  ___   _____  
    /  ___|     /   |     /   |/   | |  ___| 
    | |        / /| |    / /|   /| | | |__   
    | |  _    / ___ |   / / |__/ | | |  __|  
    | |_| |  / /  | |  / /       | | | |___  
    \_____/ /_/   |_| /_/        |_| |_____|

     _____   _     _   _____   _____   
    /  _  \ | |   / / |  ___| |  _  \  
    | | | | | |  / /  | |__   | |_| |  
    | | | | | | / /   |  __|  |  _  /  
    | |_| | | |/ /    | |___  | | \ \  
    \_____/ |___/     |_____| |_|  \_\
    """
)

input("\n\nPress the enter key to exit.")