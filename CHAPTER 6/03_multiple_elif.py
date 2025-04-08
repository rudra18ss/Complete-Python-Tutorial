a = int(input("Enter Your Age: "))

# if statement no 1
if(a%2 == 0):
    print("a is even")
#if statement 1 ends here


# if statement no 2
if (a>=18):
    print("you are adult and above age concent")
    print("good for you")
    
elif(a<0):
    print("you are entering a invalid negative age")
    
else:
    print("you are not an adult and belove age consent")
#if statement no 2 ends here


print("end of program")

# short hand if statement (CODE WAS WRITTEN IN SINGLE LINE)
# marks = 50
# if(marks > 33): print("pass")


'''Short hand if else statement (CODE WAS WRITTEN IN SINGLE LINE)
marks = 50 
print("pass") if marks > 33 else print("fail")'''
