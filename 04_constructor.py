class Employee:
    language = "Python" # This is a class attribute.
    salary = 1200000

    def __init__(self, name, salary, language): # dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an Object")

    def getInfo(self):
        print(f"The language is {self.language}. \nThe salary is {self.salary}.")

    def greet(self):
        print("Good morning!")

sagar = Employee("Sagar", 1500000, "Python") # This is an instance attribute.
# sagar.language = "Javascript"
# sagar.name = "Sagar"

print(sagar.name, sagar.language, sagar.salary)