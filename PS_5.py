# Problem 1 : 
'''words = {
    "madat": "Help",
    "Kursi": "Chair",
    "Billi": "Cat"
}
word = input("Enter the owrd you want meaning of : ")
print(words[word]) '''

# Problem 2 : 
''' s = set()
n = input("Enter Number : ")
s.add(int(n))
n = input("Enter Number : ")
s.add(int(n))
n = input("Enter Number : ")
s.add(int(n))
n = input("Enter Number : ")
s.add(int(n))
n = input("Enter Number : ")
s.add(int(n))
n = input("Enter Number : ")
s.add(int(n))
n = input("Enter Number : ")
s.add(int(n))
n = input("Enter Number : ")
s.add(int(n))

print(s)'''

# Problem 3 : 
'''s = set()  
s.add(18)
s.add("18")

print(s)'''

# Problem 4 :
'''s = set() 
s.add(20) 
s.add(20.0) # 1 == 1.0 in Python 
s.add('20') # length of s after these operations?
print(len(s))'''  # 2 

# Problem 5 :
'''s = {}
print(type(s)) # Dictionary '''

# Problem 6 :
'''d = {}
name = input("Enter friends Name : ")
lang = input("Enter Language Name : ")
d.update({name: lang})

name = input("Enter friends Name : ")
lang = input("Enter Language Name : ")
d.update({name: lang})

name = input("Enter friends Name : ")
lang = input("Enter Language Name : ")
d.update({name: lang})

name = input("Enter friends Name : ")
lang = input("Enter Language Name : ")
d.update({name: lang})

print(d)'''

# Problem 7 :
# It will update the language with the given anme twice . 

#  Problem 8 :
# Nothing will happen 

# Problem 9 :
''' s = {8, 7, 12, "Harry", [1,2]} 
In Python, set elements must be hashable (i.e., immutable).
A list is mutable (its contents can change), so it’s not hashable and cannot be placed inside a set.'''

