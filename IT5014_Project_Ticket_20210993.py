import time

class Ticket: 

    counter = 2000 
    overall_ticket = []

    def __init__(self, staff_id, issue):
        self.staff_id = staff_id
        self.issue = issue
        Ticket.counter += 1
        self.ticket_number = Ticket.counter
        self.ticket_status = ""

    @staticmethod # passwordGenerator
    def create_password(ticket_item):
        timestamp = int(time.time())
        return str(ticket_item.staff_id[:2]) + hex(ticket_item.ticket_number).lstrip("0x").rstrip("L") + (hex(timestamp).lstrip("0x").rstrip("L")[:3])

    def resolve_pw_change(self):
        self.ticket_status = "Closed"
        print("Response: New password generated: " + str(Ticket.create_password(self)))
        print("Ticket Status: " + str(self.ticket_status))
        
    def respond(self, ticket_response): 
        if self.issue == "change password":
            return self.resolve_pw_change()
        elif ticket_response == "":
            print("Response: Not Yet Provided")
        else:
            print("Response: " + str(ticket_response))
    
    def resolve(self, new_status): 
        self.ticket_status = new_status
        if self.ticket_status == "Open":
            ticket_status = "Open"
            print("Ticket Status: " + str(self.ticket_status))
        else:
            self.ticket_status = "Closed"
            print("Ticket Status: " + str(self.ticket_status))
    
    def reopen(self): 
        self.ticket_status = "Reopened"
        print("Ticket Status: " + str(self.ticket_status))

class Submission_Type_A(Ticket):

    def __init__(self, staff_id, issue):
        super().__init__(staff_id, issue)
    
    def displayTicket(self):
        ticket_list = []
        ticket_list.append(self.ticket_number)
        ticket_list.append(self.staff_id)
        ticket_list.append(self.issue)
        
        print(str("Ticket Number: " + str(ticket_list[0])))
        print(str("Ticket Creator: Not Specified"))
        print(str("Staff ID: " + str(ticket_list[1])))
        print(str("Email Address: " + "Not Specified"))
        print(str("Description: " + str(ticket_list[2])))
            
class Submission_Type_B(Ticket):

    def __init__(self, creator_name, staff_id, email, issue):
        super().__init__(staff_id, issue)
        self.creator_name = creator_name
        self.email = email
      
    def displayTicket(self):
        ticket_list = []
        ticket_list.append(self.ticket_number)
        ticket_list.append(self.creator_name)
        ticket_list.append(self.staff_id)
        ticket_list.append(self.email)
        ticket_list.append(self.issue)

        print(str("Ticket Number: " + str(ticket_list[0])))
        print(str("Ticket Creator: " + str(ticket_list[1])))
        print(str("Staff ID: " + str(ticket_list[2])))
        print(str("Email Address: " + str(ticket_list[3])))
        print(str("Description: " + str(ticket_list[4])))  