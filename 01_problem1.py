class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

    def getDetails(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Pin: {self.pin}")

p = Programmer("Sagar", 500000, 18764)
print(p.company, p.name, p.salary, p.pin)
r = Programmer("Rohan", 300000, 44321)
print(r.company, r.name, r.salary, r.pin)

