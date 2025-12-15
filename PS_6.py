# Problem 1 :
'''a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))
c = int(input("Enter 3rd number : "))
d = int(input("Enter 4th number : "))

if(a>b and a>c and a>d ):
    print("Greatest number is a :" , a)
elif(b>a and b>c and b>d ):
    print("Greatest number is b :" , b )
elif(c>a and c>b and c>d ):
    print("Greatest number is c :" , c )
elif(d>a and d>b and d>c ):
    print("Greatest number is d :" , d )'''

# Problem 2 :
'''marks1 = int(input("Enter marks 1 : "))
marks2 = int(input("Enter marks 2 : "))
marks3 = int(input("Enter marks 3 : "))

# Check for total percentage :
total_percentage =((100)*(marks1 + marks2 + marks3) /300 )
if(total_percentage >=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You have passed the examination " , total_percentage)
else:
    print("You have failed the examination " , total_percentage)'''

# Problem 3 :
'''p1 = "Make a lot of money" 
p2 = "buy now" 
p3 = "subscribe this" 
p4 = "click this"
message = input("Enter your comment : ")
if(p1 in message or p2 in message or p3 in message or p4 in message ):
    print("This comment is a spam ")
else:
    print("Comment is not a spam ")'''

# Problem 4 :
'''username = input("Enter user Name : ")
if(len(username)<10):
    print("Your username contains less than 10 characters ")
else:
    print("Your useranme contains more than 10 characters ")'''

# Problem 5 :
'''l = ["Harry" , "Samir" , "Aadarsh" , "Prince" , "Aditya"]
name = input("Enter your name :") # Case Sensetive 
if(name in l ):
    print("The name is present in the list")
else:
    print("Name is not present in the list ")'''

# Problem 6 :
'''marks = int(input("Enter the marks :"))
if(marks<=100 and marks>=90):
    grade = "Ex"
elif(marks<90 and marks>=80):
        grade = "A"
elif(marks<80 and marks>=70):
        grade = "B"
elif(marks<70 and marks>=60):
        grade = "C"
elif(marks<60 and marks>=50):
        grade = "D"
elif(marks<50 ):
        grade = "F"

print("Your Grade is " , grade )'''

# Problem 7 :
'''post = input("Enter the post :")
if ("Harry".lower() in post.lower() ):
    print("This post is talking about Harry ")
else:
    print("This post is not talking about Harry ")'''
