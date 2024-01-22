from model import SecretData
from db import createSecret
from datetime import datetime

def createSecretDAO(data : dict, envVariables):
    parsedDate = datetime.fromisoformat(str(data.get("expiryDate")))
    newSecretData = SecretData(data.get("secret"),data.get("numberOfVisits"), parsedDate)
    if(newSecretData.text != "" and newSecretData.numberOfVisits != 0 and newSecretData.expDate!=None):
        return createSecret(data, envVariables)
    else: 
        raise Exception("Some data is not provided.")