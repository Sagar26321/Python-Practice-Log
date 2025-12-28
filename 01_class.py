class employee:
   
    language = "Python" # This is a class attribute.
    salary = 1200000

sagar = employee()
sagar.language = "Javascript" # This is an instance attribute.
print(sagar.name, sagar.language, sagar.salary)
