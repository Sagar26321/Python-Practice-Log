class employee:
    company = "Google"
    def show (self):
        print(f"the name is {self.name} and the salary is {self.salary}")

# class programmer:
#     company = "Youtube"
#     def show(self):
#         print(f"the name is {self.name} and the salary is {self.salary}")
    
#     def showlanguages(self):
#         print(f"the name is {self.name} and he is good in {self.languages}")

class programmer (employee):
    company = "Youtube"
    def showlanguages(self):
        print(f"the name is {self.name} and he is good in {self.languages}")

a = employee()
b = programmer()
print(a.company, b.company)
