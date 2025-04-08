# Create an empty sictionary. Allow 4 frienss to enter their favorite language as 
# value ans use key as their names. Assume that the names are unique.

s={}

name = input("enter frienss name: ")
lang = input("enter language name: ")
s.update({name:lang})

name = input("enter frienss name: ")
lang = input("enter language name: ")
s.update({name:lang})

name = input("enter frienss name: ")
lang = input("enter language name: ")
s.update({name:lang})

name = input("enter frienss name: ")
lang = input("enter language name: ")
s.update({name:lang})

print(s)