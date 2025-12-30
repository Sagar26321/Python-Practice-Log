class Employee:
    a = 1

    @classmethod
    def show(cls):
        print(f"The class attribute of a: {cls.a}")

e = Employee()
e.a = 10  # Instance attribute
e.show()  