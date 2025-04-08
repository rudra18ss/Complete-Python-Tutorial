'''Write a program to find out the line number where python is present from ques 6'''

with open('log.txt' , 'r') as f:
    lines = f.readlines()
    
lineno = 1 
for line in lines:
    if ("python" in line):
      print(f"Yes, the file contains 'python'" , lineno)
      break
    lineno += 1
else:
    print("No, the file does not contain 'python'")