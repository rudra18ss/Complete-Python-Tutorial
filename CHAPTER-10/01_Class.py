class Employee:
    language = "Python"
    age = 21 
    salery = 1000000
    
rudra = Employee()
rudra.name = "Rudra" #this is a instace attribute
print(rudra.name , rudra.language , rudra.age , rudra.salery)

rohan = Employee()
rohan.name = "Rohan"
print(rohan.name , rohan.salery , rohan.age , rohan.language)

#here name is instance atrribute and language , age , salery is class attribute 
# as they directly belong to the class

