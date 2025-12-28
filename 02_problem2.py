class calculator:
    def __init__(self,n):
        self.n = n

    def square(self):
        print(f"The square is {self.n*self.n}")
    def cube(self):
        print(f"The cube is {self.n*self.n*self.n}")
    def squareroot(self):
        print(f"The square root is {self.n**0.5}")

a = calculator(9)
a.square()
a.cube()
a.squareroot()
        