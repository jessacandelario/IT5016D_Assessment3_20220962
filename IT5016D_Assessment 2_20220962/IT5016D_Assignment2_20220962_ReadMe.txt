README file
IT5016D_Assignment1_20220962
Jessa Candelario

The Helpdesk Ticket System is a program that allows user to create new tickets. Upon user input of ticket details, the user is given an option to change password or to input other problems. After creating tickets, it stores the data and the system allows the user to show all stored tickets, respond to existing tickets, and reopen closed tickets.  

In order to initialize the program, the following files must be stored in the same folder:
•	Main.py
•	DisplayTicket.py
•	Problem.py
•	User.py
•	Counter.py

The program can be run in Main.py

When you start the program, you will be prompted to choose from the menu options (0-5).
•	0: exits the program
•	1: allows you to create tickets
•	2: prints all the tickets created
•	3: allows you to respond to stored tickets
•	4: allows you to reopen resolved tickets
•	5: prints ticket statistics

Upon selecting option 1, the user will be prompted to input the details needed for the ticket
•	Staff ID:
•	Name:
•	Email address:
•	Problem:

When requiring password change, key in “password change” for the problem and the program will provide the new password and the ticket will be closed. Otherwise, input the problem (e.g.: printer not working, internet not working, etc.)

Once the ticket has been done, user will be asked if there are other tickets to be input. If the response is “Y”, then the program will prompt for another ticket info. Otherwise, user will be returned to the menu

Upon selecting option 2, the program will print out all the tickets created in this format:
•	Ticket number:
•	Staff ID:
•	Employee Name:
•	Email:
•	Problem:
•	Response:
•	Status:

Upon selecting option 3, the user will be prompter for the ticket number to be responded, and the response provided. The ticket will then be printer incorporating the updated response and status, along with the updated ticket statistics. The user will then be brought back to the menu options.

Upon selecting option 4, the user will be prompted for the ticket number of the ticket to be reopened. The program will then print the ticket with the status changed to “reopened”, along with the updated ticket statistics. The user will then be brought back to the menu options.

Upon selecting option 5, the program will print out ticket statistics in this format:
•	Total Tickets:
•	Open Tickets:
•	Closed Tickets:
The user will then be brought back to the menu options.
To quit the program, select option 0 in the menu

