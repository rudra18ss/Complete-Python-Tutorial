'''Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) 
and get fare information of train running under Indian Railways'''

class Train():
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats  
        
    def book_ticket(self):
        if self.seats > 0:
            print(f"Ticket Booked for {self.name}")
            self.seats -= 1
        else:
            print("Sorry, No Seats Available")
            
            
    def get_status(self):
        print(f"The number of seats available in {self.name} are {self.seats}")
        
    def get_fare(self):
        print(f"The fare of the ticket is {self.fare}") 
        
t = Train("Rajdhani Express", 1000, 2)
t.book_ticket()
t.get_status()
t.get_fare()
