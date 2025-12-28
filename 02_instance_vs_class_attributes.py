class Employee:
    language = "Python" # This is a class attribute.
    salary = 1200000

sagar = Employee() # This is an instance attribute.
sagar.language = "Javascript"
print( sagar.language, sagar.salary)
