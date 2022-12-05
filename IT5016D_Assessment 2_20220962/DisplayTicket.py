class Display:

    def __init__(self, user, issue, response, status):
        self.user = user
        self.issue = issue
        self.response = response
        self.status = status

    def get_user_info(self):
        return self.user

    def reopen_ticket(self, ticket_number):
        """Reopens ticket"""
        self.status = "Reopened"
        self.response = "Ticket reopened"
        print("\nTicket number: ", ticket_number,
              "\nStaff ID: ", self.user.user_id,
              "\nEmployee name: ", self.user.username,
              "\nEmail: ", self.user.email,
              "\nProblem: ", self.issue.problem,
              "\nResponse: ", self.response,
              "\nStatus: ", self.status, "\n")

    def change_response(self, ticket_number):
        """Updates the response of the ticket"""
        self.response = input("Enter your response: ")
        self.status = "Closed"
        print("\nTicket number: ", ticket_number,
              "\nStaff ID: ", self.user.user_id,
              "\nEmployee name: ", self.user.username,
              "\nEmail: ", self.user.email,
              "\nProblem: ", self.issue.problem,
              "\nResponse: ", self.response,
              "\nStatus: ", self.status, "\n")
