# write a class Train which has methods to book a ticket , get status (no of seats)
# and get fare information of train running under indian railways

from random import randint 

class Train:
     def __init__(self, trainNo):
        self.trainNo = trainNo

     def book(self, fro, to):
        print(f"Train no: {self.trainNo} is running on time")

     def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time")

     def getFare(self, fro, to):
        print(f"Ticket fare in train no:{self.trainNo} from {fro} tp {to} is {randint(333, 6666)}")

t= Train(12399)
t.book("haryana", "Jaipur")
t.getStatus()
t.getFare("haryana", "Jaipur")