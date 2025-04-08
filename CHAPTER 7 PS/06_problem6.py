# 6. Write a program to calculate the factorial of a given number using for loop.

# 5! = 1x2x3x4x5

n= int(input("enter the number: "))
product = 1 
for i in range(1, n+1):
    product=product * i 
    
print(f"The factorial of {n} is {product}")