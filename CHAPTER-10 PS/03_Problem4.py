'''Create a class with a class attribute a; create an object from it and set ‘a’
directly using ‘object.a = 0’. Does this change the class attribute?'''

class  Demo:
    a = 4
    
o = Demo()
print(o.a) # print the class attribute because instance attribute is not defined
o.a = 0 #  instance attribute sets
print(o.a) # print the instance attribute because instance attribute is defined
print(Demo.a) # print the class attribute because instance attribute is not defined