class Employee:
    a = 1

    @classmethod
    def show(cls):
        print(f"The class attribute of a: {cls.a}")

    @property
    def name(self):
        return self.ename
    @name.setter
    def name(self, value):
        self.ename = value
    

e = Employee()
e.a = 10


e.name = "Sagar"  
print(e.name)
e.show()  