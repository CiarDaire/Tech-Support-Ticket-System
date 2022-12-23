from IT5014_Project_Ticket_20210993 import Ticket
from IT5014_Project_Ticket_20210993 import Submission_Type_B
from IT5014_Project_Ticket_20210993 import Submission_Type_A
from IT5014_Project_ticketStats_20210993 import ticketStats

class main:
    
    print(Ticket.overall_ticket)

    Ticket.overall_ticket.append(Submission_Type_B("Inna", "INNAM", "inna@whitecliffe.co.nz", "My monitor stopped working"))
    Ticket.overall_ticket.append(Submission_Type_B("Mariah", "MARIAH", "maria@gmail.com", "Request for video camera to conduct webinars"))
    Ticket.overall_ticket.append(Submission_Type_A("JOELS", "change password"))
    
    stats = ticketStats()

    print("\nPrinting Tickets:\n")

    # Ticket 1
    Ticket.overall_ticket[0].displayTicket()
    Ticket.overall_ticket[0].respond("")
    Ticket.overall_ticket[0].resolve("Open")
    print()

    # Ticket 2
    Ticket.overall_ticket[1].displayTicket()
    Ticket.overall_ticket[1].respond("")
    Ticket.overall_ticket[1].resolve("Open")
    print()

    # Ticket 3
    Ticket.overall_ticket[2].displayTicket()
    Ticket.overall_ticket[2].respond("")
    print()

    # Overall Statistics
    stats.displayStats()

    print("\nPrinting Tickets:\n")

    # Ticket 1
    Ticket.overall_ticket[0].displayTicket()
    Ticket.overall_ticket[0].respond("Monitor has been replaced")
    Ticket.overall_ticket[0].resolve("Closed")
    print()

    # Ticket 2
    Ticket.overall_ticket[1].displayTicket()
    Ticket.overall_ticket[1].respond("Request Accepted")
    Ticket.overall_ticket[1].resolve("Closed")
    print()

    # Ticket 3
    Ticket.overall_ticket[2].displayTicket()
    Ticket.overall_ticket[2].respond("")
    print()

    # Overall Statistics
    stats.displayStats()

    print("\nPrinting Tickets:\n")

    # Ticket 1
    Ticket.overall_ticket[0].displayTicket()
    Ticket.overall_ticket[0].respond("Monitor has been replaced")
    Ticket.overall_ticket[0].resolve("Closed")
    print()

    # Ticket 2
    Ticket.overall_ticket[1].displayTicket()
    Ticket.overall_ticket[1].respond("Acceptance rescinded: need more information")
    Ticket.overall_ticket[1].reopen()
    print()

    # Ticket 3
    Ticket.overall_ticket[2].displayTicket()
    Ticket.overall_ticket[2].respond("")
    print()

    # Overall Statistics
    stats.displayStats()