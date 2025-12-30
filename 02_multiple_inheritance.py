class employee:
    company = "Google"
    name = "John"
    def show (self):
        print(f"The name is {self.name} and the name of the company is {self.company}")

class coder ():
    languages = "Python"
    def printlanguages(self):
        print(f"out of all languages, here is your language: {self.languages}")


class programmer (employee, coder):
    company = "Youtube"
    def showlanguages(self):
        print(f"The name is {self.company} and he is good in {self.languages}")

a = employee()
b = programmer() 

b.show()
b.printlanguages()
b.showlanguages()