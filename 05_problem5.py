from random import randint

class Train:
    def __init__(self,train_no):
        self.train_no = train_no

    def book(self, fro, to):
        print(f"Your ticket from {fro} to {to} on train number {self.train_no} is booked.")
    
    def getstatus(self):
        print(f"Train number {self.train_no} is running on time.")

    def getfare(self, fro, to):
        print(f"The fare from {fro} to {to} on train number {self.train_no} is Rs.{randint(200,5000)}.")
        
t  = Train(12876)
t.book("Delhi","Mumbai")
t.getstatus()
t.getfare("Delhi","Mumbai")
        