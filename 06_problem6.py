from random import randint

class Train:
    def __init__(slf,train_no):
        slf.train_no = train_no

    def book(slf, fro, to):
        print(f"Your ticket from {fro} to {to} on train number {slf.train_no} is booked.")
    
    def getstatus(slf):
        print(f"Train number {slf.train_no} is running on time.")

    def getfare(slf, fro, to):
        print(f"The fare from {fro} to {to} on train number {slf.train_no} is Rs.{randint(200,5000)}.")
        
t  = Train(12876)
t.book("Delhi","Mumbai")
t.getstatus()
t.getfare("Delhi","Mumbai")
        