# Problem 1 :
''' class Programmers :
    company = "Microsoft"
    def __init__(self , name , salary , pincode ):
        self.name = name 
        self.salary = salary
        self.pincode = pincode

p = Programmers("Prince" , 1200000 , 245001)
print(p.name ,p.salary ,p.pincode, p.company)
h = Programmers("Harry" , 1200000 , 245001)
print(h.name , h.salary ,h.pincode, h.company)'''

# Problem 2 :
'''class Calculator:
    def __init__(self , n ):
        self.n = n 

    def square (self):
        print(f"The Sqaure is {self.n*self.n}")

    def cube (self):
        print(f"The Cube is {self.n*self.n*self.n}")

    def squareroot (self):
        print(f"The SqaureRoot is {self.n**1/2}")        

a = Calculator(4)
a.square()
a.cube()
a.squareroot()'''

# Problem 3 :
''' class Demo :
    a = 4 

o = Demo()
print(o.a)  # Prints the class attribute because instance attribute is not present . 
o.a = 0 # Instance attribute is set . 
print(o.a)  # Prints the instance attribute because instance attribute is present . 
print(Demo.a) # Prints the class atttribute . Therefore No ! this does not change the class attribute . '''

# Problem 4 :
''' class Calculator:
    def __init__(self , n ):
        self.n = n 

    def square (self):
        print(f"The Sqaure is {self.n*self.n}")

    def cube (self):
        print(f"The Cube is {self.n*self.n*self.n}")

    def squareroot (self):
        print(f"The SqaureRoot is {self.n**1/2}")

    @staticmethod
    def hello():
        print("Hello there !")


a = Calculator(4)
a.hello()
a.square()
a.cube()
a.squareroot()'''

# Problem 5 :
''' from random import randint
class Train :

    def __init__(self , trainNo , ):
        self.trainNo = trainNo

    def book (self , fro , to):
        print(f"Ticket is booked in train No : {self.trainNo} from {fro} to {to}")

    def getStatus(self , trainNo):
        print(f"Train no : {self.trainNo} is running on time ")

    def getFare(self , fro , to):
        print(f"Ticket fare in train No : {self.trainNo} from {fro} to {to} is {randint(222 , 555)}")

t = Train(12399)
t.book("Rampur", "Dhanbad")
t.getStatus(12399)
t.getFare("Rampur", "Dhanbad")'''

# Problem 6 :
''' from random import randint
class Train :

    def __init__(slf , trainNo , ): # Nothing will happen to output if we write slf . 
        slf.trainNo = trainNo

    def book (harry , fro , to): # Nothing will happen to output if we write harry . 
        print(f"Ticket is booked in train No : {harry.trainNo} from {fro} to {to}")

    def getStatus(self , trainNo):
        print(f"Train no : {self.trainNo} is running on time ")

    def getFare(self , fro , to):
        print(f"Ticket fare in train No : {self.trainNo} from {fro} to {to} is {randint(222 , 555)}")

t = Train(12399)
t.book("Rampur", "Dhanbad")
t.getStatus(12399)
t.getFare("Rampur", "Dhanbad")''' 

