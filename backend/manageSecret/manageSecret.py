import sys
sys.path.append('../')
from model.secretData import secretData

def manageSecret(data : secretData):
    if(True):
        print("Fetch is cool!")
        print(data.expDate.minute)