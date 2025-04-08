class Employee:
    a = 1
    
class Programmer(Employee):
    b = 2
    
    
class Coder(Programmer):
    c = 3
    
o = Employee()
print(o.a)

o = Programmer()
print(o.a , o.b)

o = Coder()
print(o.a , o.b , o.c)
#and this is called multi-level inheritance