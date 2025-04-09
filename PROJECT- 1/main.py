''' 
1  for snake 
-1 for water
0 for gun 
'''
import random
computer = random.choice([1, 0 ,-1])
yourstr = input("Enter your choice: ")
youDict = {"s":1 , "w":-1 , "g":0}
reverseDict = {1 : "Snake" , -1 : "Water" , 0 : "Gun"}

you = youDict[yourstr]

print(f"you chose {reverseDict[you]}\n computer chose {reverseDict[computer]}")

if (computer == you):
    print("Draw")
    
else:
    if( computer == -1 and you == 1):
        print("You win")
        
    elif(computer == -1 and you == 0):
        print("you Lose")
        
    elif(computer == 1 and you == -1):
        print("you Lose")
        
    elif(computer == 1 and you == 0):
        print("you win")
        
    elif(computer == 0 and you == 1):
        print("you Lose")
        
    elif(computer == 0 and you == -1):
        print("you win")
        
    else:
        print("Something went wrong")
        
 