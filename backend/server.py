
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

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.post("/api/secret")
def createSecretEndpoint():
    data = json.loads(request.data.decode()) #This is a dictionary. 
    parsedDate = datetime.fromisoformat( data.get("expiryDate"))
    newSecretData = SecretData(data.get("secret"),data.get("numberOfVisits"), parsedDate)
    createSecretDAO(newSecretData)
    return Response("igen", status=200, mimetype='application/json')

@app.post("/api/getSecret")
def getSecretByHash():
    data = json.loads(request.data.decode())
    parsedHash = data.get("hash")
    secret = decryptSecret(parsedHash)
    responseData = {"secret": secret}
    return Response(json.dumps(responseData), status=200, mimetype='application/json')
