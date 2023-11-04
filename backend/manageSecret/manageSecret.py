import sys
sys.path.append('../')
from model.secretData import secretData

def createSecret(data : secretData):
    if(data.text != None & data.numberOfVisits != 0 & data.expDate!=None):
        print("Fetch is cool!")
        print(data.expDate.minute)
    else: print("Something is missing :c")