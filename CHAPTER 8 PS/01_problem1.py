# Write a program using functions to find greatest of three numbers.

def greatest(a,b,c):
    if(a>b and a>c):
        return a 
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
    
a = 55
b = 4
c = 14
print(greatest(a,b,c))