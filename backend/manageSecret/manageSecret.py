import sys
sys.path.append('../')
from model import SecretData
from db import createSecret


def createSecretDAO(data : SecretData):
    if(data.text != "" and data.numberOfVisits != 0 and data.expDate!=None):
        return createSecret(data)
    else: 
        raise Exception("Something is missing :c")