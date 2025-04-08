class Employee:
    language = "Python"
    age = 21 
    salery = 1000000
    
    # self refers to the instance of the class. It is automatically passed with a function call from an instance
    # self is not a keyword, you can use any other name in place of self
    
    
    def getInfo(self):
        print(f"The Language is {self.language} , The age is {self.age} , The salery is {self.salery}")
        
    @staticmethod #Sometimes we need a function that does not use the self-parameter. We can define a static method using the @staticmethod decorator.
    def greet(self): 
        print("Good Morning")
    
rudra = Employee()
rudra.getInfo()
#rudra.greet() 
#rudra.language = "Java" #this is a instace attribute
# print(rudra.language , rudra.age , rudra.salery)
