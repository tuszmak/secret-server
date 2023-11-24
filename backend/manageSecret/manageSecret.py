import sys
sys.path.append('../')
from model.secretData import SecretData
from db.createSecret import createSecret


def createSecretDAO(data : SecretData):
    if(data.text != "" and data.numberOfVisits != 0 and data.expDate!=None):
        createSecret(data)
    else: print("Something is missing :c")