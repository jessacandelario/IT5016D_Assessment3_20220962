# Main.py
# Author: Jessa Candelario
# Date: 24.11.22

from Counter import TicketStatistics
from Username import Username
from Problem import Problem
from DisplayTicket import Display


class Ticket:

    def main(self):
        """Main menu function"""

        print("Welcome to Helpdesk Ticket System!\n")

        # Assign variables
        self.ticket_counter = TicketStatistics()  # contains all ticket statistics
        self.ticket_list = {}  # contains all tickets
        choice = int

        while choice != 0:
            print("\nPlease select from the following choices:\n"
                  "0: Exit\n"
                  "1: Submit helpdesk ticket\n"
                  "2: Show all tickets\n"
                  "3: Respond to ticket by number\n"
                  "4: Re-open resolved tickets\n"
                  "5: Display ticket stats")
            choice = int(input("\nPlease enter your selection:"))
            self.menu(choice)

    def ticket_info(self):
        """Gathers data of the ticket"""

        # user to input details
        user_id = input("\nEnter staff ID number: ")
        username = input("Enter your name: ")
        email = input("Enter your email address: ")

        # provide option for password change
        print("If you require password change, enter: Password change")
        problem = input("Enter problem: ")
        status = "Open"  # default status
        response = "Not yet provided"  # default response
        if problem.lower() == "password change":
            new_password = Problem.password_change(self, user_id, username)  # password changed
            status = "Closed"
            response = "Resolved"
            print("Your new password is:{0}".format(new_password))
            self.ticket_counter.total_closed_ticket()  # add to closed ticket
        else:
            print("Ticket added.")
            self.ticket_counter.total_open_ticket()  # add to open ticket

        user = Username(user_id, username, email)
        issue = Problem(problem)

        return Display(user, issue, response, status)

    def print_all_ticket(self):
        """Print the items stored in the list"""
        for key, value in self.ticket_list.items():
            print("\nTicket number: " + str(key),
                  "\nStaff ID:", value.user.user_id,
                  "\nEmployee name: ", value.user.username,
                  "\nEmail: ", value.user.email,
                  "\nProblem: ", value.issue.problem,
                  "\nResponse: ", value.response,
                  "\nStatus: ", value.status, "\n")

    def ticket_process(self):
        """Creates the ticket, and stores it in the list"""
        # receives the ticket info from input
        new_ticket = self.ticket_info()

        # add new ticket to the dictionary
        self.ticket_list[self.ticket_counter.ticket_key()] = new_ticket
        print("Ticket number: ", str(self.ticket_counter.ticket_key()))

        # increments the ticket number for the new input
        self.ticket_counter.increment_ticket_counter()

    def menu(self, choice):
        """Options for the main function"""
        if choice == 0:
            print("Quit")

        elif choice == 1:
            self.ticket_process()
            ticket_option = input("\nDo you have another problem to submit? Y/N").upper()
            while ticket_option == "Y":
                self.ticket_process()
                ticket_option = input("\nDo you have another problem to submit? Y/N").upper()

        elif choice == 2:
            print(self.print_all_ticket())

        elif choice == 3:
            ticket_number = input("Please enter ticket number:")
            respond_ticket = self.ticket_list[ticket_number]  # calls the ticket number from ticket_list dictionary
            respond_ticket.change_response(ticket_number)  # changes response of specific ticket number

            # adjust ticket statistics
            self.ticket_counter.minus_open_ticket()  # subtracts open ticket
            self.ticket_counter.total_closed_ticket()  # adds closed ticket

            # print updated ticket statistics
            print(self.ticket_counter.total_ticket_statistics())

        elif choice == 4:
            ticket_number = input("Please enter ticket number:")
            reopen_ticket = self.ticket_list[ticket_number]
            reopen_ticket.reopen_ticket(ticket_number)

            # adjust ticket statistics
            self.ticket_counter.minus_closed_ticket()  # subtracts closed ticket
            self.ticket_counter.total_open_ticket()  # adds open ticket

            # print updated ticket statistics
            print(self.ticket_counter.total_ticket_statistics())

        elif choice == 5:
            print(self.ticket_counter.total_ticket_statistics())

        else:
            print("Please enter a valid option.")


if __name__ == "__main__":
    ticket = Ticket()
    ticket.main()
