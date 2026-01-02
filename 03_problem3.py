class Employee:
    salary = 234 # Class variable
    increment = 20 # Class variable

    @property
    def salary_after_increment(self):
        return self.salary + self.salary * self.increment / 100
    @salary_after_increment.setter
    def salary_after_increment(self, salary):
        self.increment = ((salary/self.salary)-1)*100

e= Employee()
e.salary_after_increment = 280.8
print(e.increment)  