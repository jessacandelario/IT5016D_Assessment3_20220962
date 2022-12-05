
class TicketStatistics:

    def __init__(self):
        self.ticket_number = 2000
        self.open_ticket = 0
        self.closed_ticket = 0
        self.tickets_sum = 0

    def ticket_key(self):
        return str(self.ticket_number)

    def increment_ticket_counter(self):
        """Adds one to the counter for every new ticket"""
        self.ticket_number += 1

    def total_open_ticket(self):
        """Adds to the open ticket count"""
        self.open_ticket += 1

    def total_closed_ticket(self):
        """Adds to the closed ticket count"""
        self.closed_ticket += 1

    def minus_open_ticket(self):
        """Subtracts one from total open ticket"""
        self.open_ticket -= 1

    def minus_closed_ticket(self):
        """Subtracts one from total closed tickets"""
        self.closed_ticket -= 1

    def overall_tickets(self):
        """Total of all tickets created"""
        self.tickets_sum = self.open_ticket + self.closed_ticket
        return self.tickets_sum

    def total_ticket_statistics(self):
        """Prints detailed ticket statistics"""
        print("\nTicket statistics",
              "\nTotal tickets: ", self.overall_tickets(),
              "\nOpen tickets: ", self.open_ticket,
              "\nClosed tickets: ", self.closed_ticket)
        return ""

