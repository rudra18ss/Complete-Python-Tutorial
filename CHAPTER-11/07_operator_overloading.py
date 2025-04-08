class Number:
    def __init__(self, n):
        self.n = n
    
    def __add__(self, num):
        return self.n + num.n

n = Number(9)
m = Number(6)
print(n + m)
# This will give an error because the + operator is
# not defined for the object of the class Number but we can define it by using the __add__ method.
# This is called operator overloading.