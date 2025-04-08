'''6. Write a program to mine a log file and find out whether it contains ‘python’.'''

with open('file.txt' , 'r') as f:
    content = f.read()
    
if ("python" in content):
    print("Yes, the file contains 'python'")
else:
    print("No, the file does not contain 'python'")
