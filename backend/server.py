
import sys
import json
# setting path

from flask import Flask, Response, request
from manageSecret.manageSecret import createSecretDAO
from model import SecretData
from datetime import datetime
from db import init
from encrypt import decryptSecret
sys.path.append('../')
app = Flask(__name__)
conn = init()

@app.post("/api/v1/secret")
def createSecretEndpoint():
    data = json.loads(request.data.decode()) #This is a dictionary. 
    parsedDate = datetime.fromisoformat( data.get("expiryDate"))
    newSecretData = SecretData(data.get("secret"),data.get("numberOfVisits"), parsedDate)
    link = createSecretDAO(newSecretData)
    return Response(link, status=200, mimetype='text/html')

@app.post("/api/v1/getSecret")
def getSecretByHash():
    data = json.loads(request.data.decode())
    parsedHash = data.get("hash")
    secret = decryptSecret(parsedHash)
    responseData = {"secret": secret}
    return Response(json.dumps(responseData), status=200, mimetype='application/json')
