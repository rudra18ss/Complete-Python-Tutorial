# 5. Write a program which finds out whether a given name is 
# present in a list or not.

l = [ "rudra" , "binni", "bunny", "nishu"]

name= input("enter the name: ")

if(name in l ):
    print("your name is in the list: ")
    
else:
    print("your name is not in the list")