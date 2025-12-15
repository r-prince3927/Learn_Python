class Employee:
    language = "python" # This is a class attribute 
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language} . The salary is {self.salary}")

    @staticmethod  # decorator to mark greet as a static method
    def greet():
        print("Good Morning")


harry = Employee()
# harry.language = "JavaScript" # This is an instance attribute 
harry.greet()
harry.getInfo()
# Employee.getInfo(harry)
