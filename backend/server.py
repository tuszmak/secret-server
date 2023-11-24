
import sys
import json
# setting path

from flask import Flask, Response, request
from manageSecret.manageSecret import createSecret
from model.secretData import SecretData
from datetime import datetime
from db.init_db import init
sys.path.append('../')
app = Flask(__name__)
conn = init()
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
@app.get("/api/secret")
def getSecret():
    print("a")
@app.post("/api/secret")
def createSecretEndpoint():
    print("Fetch is here!")
    
    data = json.loads(request.data.decode()) #This is a dictionary. 
    parsedDate = datetime.fromisoformat( data.get("expiryDate"))
    newSecretData = SecretData(data.get("secret"),data.get("numberOfVisits"), parsedDate)
    createSecret(newSecretData)
    return Response("igen", status=200, mimetype='application/json')
