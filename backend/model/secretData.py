from datetime import datetime

class secretData:
    def __init__(self,text:str,numberOfVisits:int, expDate:datetime):
        self.text = text
        self.numberOfVisits = numberOfVisits
        self.expDate = expDate

def igen():
    print("a")