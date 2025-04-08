class Employee:
    a = 1 
    @classmethod # This is a decorator which is used to define a class method
    def show(cls):
        print(f"The class attribute is {cls.a}")
        
e = Employee()
e.a = 45 # This will create a instance attribute
e.show()