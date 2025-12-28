class Employee:
    language = "Python" # This is a class attribute.
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. \nThe salary is {self.salary}.")

    @staticmethod
    def greet():
        print("Good morning!")

sagar = Employee() # This is an instance attribute.
sagar.language = "Javascript"
# print( sagar.language, sagar.salary)
sagar.greet()
sagar.getInfo()