#Inheritance is a way of creating a new class from an existing class. The new class is called the derived class and the existing class is called the base class.
#The derived class inherits all the features from the base class and can have additional features of its own. Inheritance is a powerful feature in 
#object-oriented programming. It provides code reusability and makes the code easier to manage. Inheritance is a way of creating a new class from an existing class.
#The new class is called the derived class and the existing class is called the base class. The derived class inherits all the features from the base class and can have 
#additional features of its own. Inheritance is a powerful feature in object-oriented programming. It provides code reusability and makes the code easier to manage.

class Employee:                                   # Base Class / Parent Class
    company = "Google"
    def show(self):                               
        print(f"The name of a Employee is {self.name} and the salary is {self.salary}")
        
# class Programmer(Employee):
    # company = "YouTube"
    # def show(self):
        # print(f"The name of a Programmer is {self.name} and the salary is {self.salary}")
        
    # def showLanguage(self):
        # print(f"The name is {self.name} and he is good in  {self.language}")
        
class Programmer(Employee):                       # Derived Class / Child Class/ inherited class
    company = "YouTube"             
    def show(self):
        print(f"The name of a Programmer is {self.name} and he is good in{self.language}")
        
        
e = Employee()
b = Programmer()
print(e.company , b.company)


#and this is called single level inheritance.
#In single inheritance, a class is derived from a single base class.
# In the above example, the Programmer class is derived from the Employee class.