class Employee:
    language = "python" # This is a class attribute 
    salary = 1200000

    def __init__(self , name , salary , language ):  # dunder method which is automatically called . 
        self.name = name 
        self.salary = salary
        self.language = language
        print("I am creating an Object")


    def getInfo(self):
        print(f"The language is {self.language} . The salary is {self.salary}")

    @staticmethod  # decorator to mark greet as a static method
    def greet():
        print("Good Morning")


harry = Employee("Harry" , 1300000 , "Java")
# harry.name = "Harry"
print(harry.name , harry.salary , harry.language)

# rohan = Employee()
