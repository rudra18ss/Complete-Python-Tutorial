class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a = 1
    
class Programmer(Employee):
    def __init__(self):
        print("Constructor of Programmer")
    b = 2
    
    
class Coder(Programmer):
    def __init__(self):
        super().__init__()
        print("Conmstructor of Coder")
    c = 3
    
# o = Employee()
# print(o.a)

# o = Programmer()
# print(o.a , o.b)

o = Coder()
print(o.a , o.b , o.c)

# Super method is used to call the constructor of the parent class.