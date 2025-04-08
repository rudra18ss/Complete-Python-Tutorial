'''
Write a program to read the text from a given file ‘poems.txt’ and find out 
whether it contains the word ‘twinkle’
'''
f = open("poem.txt")
content = f.read()
if ("Twinkle" in content):
    print("The word twinkle present in the Content")
else:
    print("The word twinkle not present in the Content")

f.close()