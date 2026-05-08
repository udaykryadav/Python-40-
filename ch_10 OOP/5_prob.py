from random import randint

class train:
    def __init__(self, trainNo):
        self.trainNo =trainNo
    
    def book(self , frm, to):
        print(f"ticket is booked for train no {self.trainNo} from {frm} to {to}")
    
    def getStatus(self):
        print(f"ticket no {self.trainNo} is running on time")
    
    def getfair(self , frm, to):
        print(f"ticket fair for train no {self.trainNo} from {frm} to {to} is {randint(222,5555)}")

t =train(12399)
t.book('ramput','delhi')
t.getfair('ramput','delhi')
t.getStatus()