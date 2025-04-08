class Employee:
    language = "Python"
    age = 21 
    salery = 1000000
    
rudra = Employee()
rudra.language = "Java" #this is a instace attribute
print(rudra.language , rudra.age , rudra.salery)

# Instance attributes, take preference over class attributes during assignment & retrieval
# If an instance attribute is not found, the class attribute is retrieved