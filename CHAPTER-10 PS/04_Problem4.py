'''. Add a static method in problem 2, to greet the user with hello.'''
class Calculator():
    def __init__(self, num):
        self.num = num

    def square(self):
        print(f"The square of {self.num} is {self.num ** 2}")

    def cube(self):
        print(f"The cube of {self.num} is {self.num ** 3}")
        
    def square_root(self):
        print(f"the square root of {self.num} is {self.num ** 0.5}")
    
    @staticmethod
    def greet():
        print("Hello")
        
c = Calculator(4)
c.square()
c.cube()
c.square_root()
c.greet() # greet the user with hello