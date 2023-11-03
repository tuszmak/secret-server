
import sys
import json
# setting path

from flask import Flask, Response, request
from manageSecret.manageSecret import manageSecret
from model.secretData import secretData
from datetime import datetime
sys.path.append('../')
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
@app.get("/api/secret")
def getSecret():
    print("a")
@app.post("/api/secret")
def createSecret():
    print("Fetch is here!")
    
    data = json.loads(request.data.decode()) #This is a dictionary. 
    print(data.get("secret"))
    parsedDate = datetime.fromisoformat( data.get("expiryDate"))
    newSecretData = secretData(data.get("secret"),data.get("numberOfVisits"), parsedDate)
    manageSecret(newSecretData)
    return Response("igen", status=200, mimetype='application/json')
    # data = secretData("igen", 5, "")