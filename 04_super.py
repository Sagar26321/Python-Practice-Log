class employee:
    def __init__(self):
        print("constructor of employee class")
    a = 1

class programmer (employee):
    def __init__(self):
        print("constructor of programmer class")
    b = 2

class manager(programmer):
    def __init__(self):
        super().__init__()
        print("constructor of manager class")
    c = 3

# o = employee()
# print(o.a) # prints the a attribute of employee class

# o = programmer()
# print(o.a, o.b) # prints the a attribute of employee class and b attribute of programmer class

o = manager()
print(o.a, o.b, o.c) # prints the a attribute of employee class , b attribute of programmer class and c attribute of manager class