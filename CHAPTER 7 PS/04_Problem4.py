# 4. Write a program to find whether a given number is prime or not.

n = int(input("enter the number : "))

for i in range(2, n):
    if(n%i)==0:
        print("Number is not prime")
        break
else:
    print("number is prime: ")