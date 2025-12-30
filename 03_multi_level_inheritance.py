class employee:
    a = 1

class programmer (employee):
    b = 2

class manager(programmer):
    c = 3

o = employee()
print(o.a) # prints the a attribute of employee class
# print(o.b)  throws an error because b is not present in employee class
# print(o.c)  throws an error because c is not present in employee class

o = programmer()
print(o.a, o.b) # prints the a attribute of employee class and b attribute of programmer class

o = manager()
print(o.a, o.b, o.c) # prints the a attribute of employee class , b attribute of programmer class and c attribute of manager class