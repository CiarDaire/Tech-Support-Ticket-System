from IT5014_Project_Ticket_20210993 import Ticket

class ticketStats(object): 
    
    def allTickets(self): 
        return len(Ticket.overall_ticket)

    def closedTickets(self):
        __countClosed = 0
        for ticket_item in Ticket.overall_ticket:
            if ticket_item.ticket_status == "Closed":
                __countClosed = __countClosed + 1
        return int(__countClosed)

    def openTickets(self):
        __countOpen = 0
        for ticket_item in Ticket.overall_ticket:
            if ticket_item.ticket_status == "Open" or ticket_item.ticket_status == "Reopened":
                __countOpen = __countOpen + 1
        return int(__countOpen)
     
    def displayStats(self): # prints ticket statistics
        print("Displaying Ticket Statistics\n")
        print("Tickets Created: " + str(self.allTickets()) + "\nTickets Resolved: " + str(self.closedTickets()) + "\nTickets to Solve: " + str(self.openTickets())) 