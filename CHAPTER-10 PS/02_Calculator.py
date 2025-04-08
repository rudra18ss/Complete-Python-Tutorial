'''Write a class “Calculator” capable of finding square, cube and square root of a 
number'''

class Calculator():
    def __init__(self, num):
        self.num = num

    def square(self):
        print(f"The square of {self.num} is {self.num ** 2}")

    def cube(self):
        print(f"The cube of {self.num} is {self.num ** 3}")
        
    def square_root(self):
        print(f"the square root of {self.num} is {self.num ** 0.5}")
        
c = Calculator(4)
c.square()
c.cube()
c.square_root()

