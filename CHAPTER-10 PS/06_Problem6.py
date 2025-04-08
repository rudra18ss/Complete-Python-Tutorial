'''Can you change the self-parameter inside a class to something else (say
“harry”). Try changing self to “slf” or “harry” and see the effects.'''

class Train():
    def __init__(slf, name, fare, seats):
        slf.name = name
        slf.fare = fare
        slf.seats = seats  
        
    def book_ticket(slf):
        if slf.seats > 0:
            print(f"Ticket Booked for {slf.name}")
            slf.seats -= 1
        else:
            print("Sorry, No Seats Available")
            
            
    def get_status(slf):
        print(f"The number of seats available in {slf.name} are {slf.seats}")
        
    def get_fare(slf):
        print(f"The fare of the ticket is {slf.fare}") 
        
t = Train("Rajdhani Express", 1000, 2)
t.book_ticket()
t.get_status()
t.get_fare()


# we see that the code runs perfectly fine even after changing the self parameter to something else.
# This is because self is just a convention and not a keyword. We can change it to anything we want.
# However, it is recommended to use self as it is a convention and makes the code more readable.
