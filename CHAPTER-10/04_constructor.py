class Employee:
    language = "Python"
    age = 21 
    salery = 1000000
    
    def __init__(self , name , salery , language): #The __init__() function is called automatically every time the class is being used to create a new object also known as dunder method
        self.name = name
        self.salery = salery
        self.language = language
        print("i am  creatinng an object")
        
    def getInfo(self):
        print(f"The Language is {Employee.language} , The age is {Employee.age} , The salery is {Employee.salery}")
        
    @staticmethod #Sometimes we need a function that does not use the self-parameter. We can define a static method using the @staticmethod decorator.
    def greet(self): 
        print("Good Morning")
    
rudra = Employee("Rudra" ,1500000 , "Javascript")
#rudra.name = "Rudra" 
print(rudra.name , rudra.salery , rudra.language)
#rudra.getInfo()