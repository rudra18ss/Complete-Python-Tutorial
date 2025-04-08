class Employee:                                   # Base Class / Parent Class
    company = "Google"
    name = "Saurabh"
    def show(self):                               
        print(f"The name of a Employee is {self.name} and the salary is {self.salary}")


class Coder:
    language = "Python"
    def printLanguage(self):
        print(f"out of all your languages here is your Languages {self.language}")
        
class Programmer(Employee ,Coder):                       # Derived Class / Child Class/ inherited class
    Company = "YouTube"             
    def show(self):
        print(f"The name of a Programmer is {self.Company} and he is good in{self.language}")
        
        
e = Employee()
b = Programmer()

b.show()
b.printLanguage()
